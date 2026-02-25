#!/usr/bin/env python3
"""
GitHub Skill Scraper — ClawFriend.ai
Scrapes SKILL.md / WORKFLOW.md / prompt.txt from public GitHub repos (main branch only)
and publishes them to the ClawFriend Skill Market.

Usage:
    python3 scraper.py --repos "https://github.com/owner/repo1" "https://github.com/owner/repo2"
    python3 scraper.py --repos-file repos.txt
    python3 scraper.py --repos "https://github.com/owner/repo" --dry-run

Env vars:
    GITHUB_TOKEN      — optional, boosts rate limit from 60 to 5000 req/hr
    CLAWFRIEND_API_KEY — required for publishing (skip with --dry-run)
"""

import argparse
import hashlib
import json
import os
import sys
import time
from urllib.parse import urlparse

import requests

# ── Config ────────────────────────────────────────────────────────────────────

GITHUB_API = "https://api.github.com"
RAW_BASE   = "https://raw.githubusercontent.com"
CF_API     = "https://api.clawfriend.ai/v1/academy"

TARGET_FILES = {
    "SKILL.md":    "skill",
    "WORKFLOW.md": "workflow",
    "prompt.txt":  "prompt",
}

REQUEST_DELAY = 0.15  # seconds between GitHub API calls


# ── Helpers ───────────────────────────────────────────────────────────────────

def parse_repo(url: str) -> tuple[str, str]:
    """'https://github.com/owner/repo' → ('owner', 'repo')"""
    url = url.strip().rstrip("/")
    if url.startswith("http"):
        parts = urlparse(url).path.strip("/").split("/")
    else:
        parts = url.strip("/").split("/")
    if len(parts) < 2:
        raise ValueError(f"Cannot parse repo from: {url}")
    return parts[0], parts[1]


def sha256(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()


def github_headers(token: str | None) -> dict:
    h = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def rate_limit_wait(resp: requests.Response):
    remaining = int(resp.headers.get("X-RateLimit-Remaining", 999))
    if remaining < 5:
        reset_at = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(0, reset_at - time.time()) + 2
        print(f"  ⚠ Rate limit low ({remaining} remaining). Waiting {wait:.0f}s...")
        time.sleep(wait)


# ── GitHub API ─────────────────────────────────────────────────────────────────

def get_file_tree(owner: str, repo: str, token: str | None) -> list[dict]:
    """Returns flat list of all files in main branch."""
    url = f"{GITHUB_API}/repos/{owner}/{repo}/git/trees/main?recursive=1"
    resp = requests.get(url, headers=github_headers(token), timeout=10)
    rate_limit_wait(resp)
    time.sleep(REQUEST_DELAY)

    if resp.status_code == 404:
        # Try 'master' fallback
        url = f"{GITHUB_API}/repos/{owner}/{repo}/git/trees/master?recursive=1"
        resp = requests.get(url, headers=github_headers(token), timeout=10)
        rate_limit_wait(resp)
        time.sleep(REQUEST_DELAY)

    if resp.status_code != 200:
        raise RuntimeError(f"GitHub API {resp.status_code}: {resp.text[:200]}")

    data = resp.json()
    return [item for item in data.get("tree", []) if item["type"] == "blob"]


def fetch_raw(owner: str, repo: str, path: str, branch: str = "main") -> str:
    url = f"{RAW_BASE}/{owner}/{repo}/{branch}/{path}"
    resp = requests.get(url, timeout=10)
    time.sleep(REQUEST_DELAY)
    if resp.status_code != 200:
        raise RuntimeError(f"Raw fetch {resp.status_code}: {url}")
    return resp.text


def filter_skill_files(tree: list[dict]) -> list[dict]:
    matches = []
    for item in tree:
        filename = item["path"].split("/")[-1]
        if filename in TARGET_FILES:
            item["skill_type"] = TARGET_FILES[filename]
            matches.append(item)
    return matches


# ── Name + Tag generation ──────────────────────────────────────────────────────

def make_skill_name(repo_name: str, file_path: str) -> str:
    parts = file_path.split("/")
    if len(parts) == 1:
        # Root-level file
        filename = parts[0].replace(".md", "").replace(".txt", "")
        return f"{repo_name}/{filename}"
    else:
        # Include directory path, drop filename
        dirs = parts[:-1]
        return f"{repo_name}/{'/'.join(dirs)}"


def make_tags(repo_name: str, file_path: str) -> list[str]:
    parts = file_path.split("/")
    dirs = parts[:-1]
    tags = [repo_name] + dirs
    # deduplicate, lowercase, max 5
    seen = set()
    result = []
    for t in tags:
        t = t.lower().replace("-", "_")
        if t not in seen and len(result) < 5:
            seen.add(t)
            result.append(t)
    return result


# ── ClawFriend publish ─────────────────────────────────────────────────────────

def publish_skill(name: str, content: str, skill_type: str,
                  tags: list[str], visibility: str, api_key: str) -> dict:
    url = f"{CF_API}/skills"
    payload = {
        "name": name,
        "content": content,
        "type": skill_type,
        "visibility": visibility,
        "tags": tags,
    }
    resp = requests.post(
        url,
        json=payload,
        headers={"X-API-Key": api_key, "Content-Type": "application/json"},
        timeout=15,
    )
    if resp.status_code not in (200, 201):
        raise RuntimeError(f"ClawFriend API {resp.status_code}: {resp.text[:300]}")
    return resp.json()


# ── Main scrape loop ───────────────────────────────────────────────────────────

def scrape_repo(owner: str, repo: str, token: str | None,
                api_key: str | None, visibility: str,
                dry_run: bool, seen_hashes: set) -> list[dict]:

    results = []
    repo_label = f"{owner}/{repo}"
    print(f"\n→ {repo_label}")

    try:
        tree = get_file_tree(owner, repo, token)
    except RuntimeError as e:
        print(f"  ✗ Cannot access repo: {e}")
        return [{"repo": repo_label, "status": "error", "reason": str(e)}]

    skill_files = filter_skill_files(tree)
    print(f"  Found {len(skill_files)} skill file(s) in main branch")

    if not skill_files:
        return []

    for item in skill_files:
        path = item["path"]
        skill_type = item["skill_type"]
        name = make_skill_name(repo, path)
        tags = make_tags(repo, path)

        record = {
            "repo": repo_label,
            "file": path,
            "skill_name": name,
            "type": skill_type,
            "tags": tags,
        }

        # Fetch raw content
        try:
            branch = "main"
            try:
                content = fetch_raw(owner, repo, path, "main")
            except RuntimeError:
                content = fetch_raw(owner, repo, path, "master")
                branch = "master"
        except RuntimeError as e:
            print(f"  ✗ Fetch failed [{path}]: {e}")
            record.update({"status": "error", "reason": str(e)})
            results.append(record)
            continue

        # Size guard (100KB)
        if len(content) > 100_000:
            print(f"  ⊘ Skipped [{path}]: file too large ({len(content)//1024}KB)")
            record.update({"status": "skipped", "reason": "file too large (>100KB)"})
            results.append(record)
            continue

        # Dedup
        h = sha256(content)
        if h in seen_hashes:
            print(f"  ⊘ Skipped [{path}]: duplicate content")
            record.update({"status": "skipped", "reason": "duplicate content hash"})
            results.append(record)
            continue
        seen_hashes.add(h)

        # Publish or dry-run
        if dry_run:
            print(f"  [DRY-RUN] Would publish: {name} ({skill_type})")
            record.update({"status": "dry_run", "content_preview": content[:120] + "..."})
        else:
            try:
                resp = publish_skill(name, content, skill_type, tags, visibility, api_key)
                skill_id = resp.get("id") or resp.get("skill_id") or "?"
                print(f"  ✓ Published: {name} → {skill_id}")
                record.update({"status": "published", "skill_id": skill_id})
            except RuntimeError as e:
                print(f"  ✗ Publish failed [{path}]: {e}")
                record.update({"status": "error", "reason": str(e)})

        results.append(record)

    return results


# ── CLI ────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="GitHub → ClawFriend Skill Market scraper")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--repos", nargs="+", help="GitHub repo URLs (space-separated)")
    group.add_argument("--repos-file", help="Text file with one repo URL per line")

    parser.add_argument("--visibility", choices=["public", "private"], default="public")
    parser.add_argument("--dry-run", action="store_true",
                        help="Scan and report without publishing")
    parser.add_argument("--out", help="Save JSON results to this file")
    args = parser.parse_args()

    # Collect repo list
    if args.repos:
        raw_repos = args.repos
    else:
        with open(args.repos_file) as f:
            raw_repos = [l.strip() for l in f if l.strip() and not l.startswith("#")]

    token   = os.environ.get("GITHUB_TOKEN")
    api_key = os.environ.get("CLAWFRIEND_API_KEY")

    if not args.dry_run and not api_key:
        print("ERROR: CLAWFRIEND_API_KEY env var required (or use --dry-run)")
        sys.exit(1)

    if token:
        print(f"GitHub token: set (5,000 req/hr limit)")
    else:
        print(f"GitHub token: NOT set (60 req/hr limit — set GITHUB_TOKEN to increase)")

    if args.dry_run:
        print("Mode: DRY RUN — no skills will be published\n")
    else:
        print(f"Mode: LIVE — publishing as {args.visibility}\n")

    all_results = []
    seen_hashes: set = set()

    for raw in raw_repos:
        try:
            owner, repo = parse_repo(raw)
        except ValueError as e:
            print(f"✗ Bad URL [{raw}]: {e}")
            continue
        results = scrape_repo(owner, repo, token, api_key,
                              args.visibility, args.dry_run, seen_hashes)
        all_results.extend(results)

    # Summary
    published = sum(1 for r in all_results if r.get("status") == "published")
    dry_found = sum(1 for r in all_results if r.get("status") == "dry_run")
    skipped   = sum(1 for r in all_results if r.get("status") == "skipped")
    errors    = sum(1 for r in all_results if r.get("status") == "error")

    print("\n" + "─" * 50)
    print(f"Repos scanned:    {len(raw_repos)}")
    print(f"Files found:      {len(all_results)}")
    if args.dry_run:
        print(f"Would publish:    {dry_found}")
    else:
        print(f"Published:        {published}")
    print(f"Skipped (dedup):  {skipped}")
    print(f"Errors:           {errors}")
    print("─" * 50)

    if args.out:
        with open(args.out, "w") as f:
            json.dump(all_results, f, indent=2)
        print(f"Results saved to: {args.out}")

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
