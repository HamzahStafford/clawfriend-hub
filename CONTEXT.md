# CONTEXT — AI Handoff Document
> **For:** AI intern picking up this project in a new session
> **Last updated:** 2026-02-25
> **Repo:** `/Users/lab3/Desktop/norway/lab3/clawfriend-hub` (main branch)
> **Worktree:** `/Users/lab3/.claude-worktrees/clawfriend-hub/adoring-poincare` (branch: adoring-poincare)

---

## 1. What This Project Is

An **internal competition** at the company behind ClawFriend.ai. The contest is called "Cook a Web3 Skill Marketplace." Format: 3-day individual work, ends with a presentation. Judged by: Anh Brian, Arthur, Lucas, Akemi.

**The product being sold:** ClawFriend.ai — a Web3 AI Agent Economy on BNB Smart Chain. Key features: agents with on-chain identity, tradeable shares via bonding curve (quadratic, `price = supply² / 16000`), Skill Marketplace (public/holder-gated), and an on-chain social layer (tweet/reply/follow).

The repo is **one contestant's submission**. The contestant built everything in this repo. The role being played: Senior BD / Distribution Strategist with dev background.

**Product spec:** Full spec at `/Users/lab3/Downloads/CLAWFRIEND_SPEC.md` — covers API, smart contract, bonding curve math, agent lifecycle, Skill Market API, auth flows.

**Competition guidebook:** `/Users/lab3/Downloads/GUIDEBOOK - FOR TEAM SELLING CLAWFRIEND.docx.pdf` — defines 4 deliverables, rubric, budget, rules.

---

## 2. Repo Structure (current state)

```
/
├── README.md                        ← project overview · v2
├── competitive-landscape.md         ← Deliverable 1 (25%) · v3
├── skill-research.md                ← Deliverable 2 (25%) · v1 (8 skills)
├── distribution-plan.md             ← Deliverable 3 (40%) · v3
├── ai-showcase/
│   ├── claude/persona.md            ← Claude role: Strategic Analyst
│   ├── gpt/persona.md               ← GPT role: Synthesizer & Writer
│   └── grok/persona.md              ← Grok role: Social & Trend Scout
├── data/
│   └── sources.md                   ← verified data registry · v2
├── skill-hub/
│   ├── skill.md                     ← SKILL.md spec for GitHub Skill Scraper
│   ├── scraper.py                   ← working Python scraper script
│   ├── dry-run-results.json         ← metadata from last dry-run
│   └── output/                      ← real scraped SKILL.md files
│       └── anthropics__anthropic-cookbook/
│           ├── .claude/skills/cookbook-audit/SKILL.md
│           └── skills/custom_skills/
│               ├── analyzing-financial-statements/SKILL.md
│               ├── applying-brand-guidelines/SKILL.md
│               └── creating-financial-models/SKILL.md
├── CONTEXT.md                       ← this file
└── ClawFriend.ai Go-To-Market Masterclass - V1 - test.pdf  ← Gemini Canvas draft
```

---

## 3. Deliverables — What Each File Contains

### competitive-landscape.md · v3
**5-tier competitive framework** — the main structural innovation vs v1/v2:

| Tier | What | Who |
|------|------|-----|
| 1 — Full-Stack | Bonding curve + social + skill market | Virtuals Protocol (only one) |
| 2 — Social-Only | Agent social layer, no economy | Moltbook, Clawk.ai |
| 3 — Marketplace-Only | Skill/service market, no social | ClawHub, NEAR AI Market, SingularityNET |
| 4 — Economic/Launchpad | Bonding curve only | MegaPad, Build4 |
| 5 — Adjacent/Niche | Trust, gig work | SelfClaw, ClawGig |

**Key claims with evidence:**
- ClawFriend is the ONLY platform with all 7 features (bonding curve + skill market + on-chain social + on-chain identity + holder-gated content + BNB Chain + creator passive income) → proven via feature matrix table
- Virtuals Protocol = Tier 1 benchmark: 17,897 agents, $479M aGDP, $13.58B 30D volume (live counters, virtuals.io, Feb 25 2026)
- BNB Chain underserved: 4.32M DAU peak Jan 2026 (bitcoinethereumnews.com), most competitors on Base/Ethereum
- One-sentence positioning: *"ClawFriend is the only AI agent economy on BNB Chain where builders earn passive income from agent activity."*

**What's still weak:**
- Moltbook "88→1.2M agents in 3 days" claim — sources.md flags "no primary URL", still in competitive table
- Build4 metrics (184K tx/day) — LOW confidence, homepage counter only, not cross-checked

### skill-research.md · v1 (8 skills)
8 skills for the Skill Marketplace. Each has: target user, problem, current alternatives, how ClawFriend skill solves it, public/private visibility logic, demand evidence.

| # | Skill | Key demand signal |
|---|-------|------------------|
| 1 | Whale Wallet Tracker | Whale Alert = 1.2M followers; Nansen $100–999/mo paid |
| 2 | DeFi Yield Optimizer | Yearn Finance ~$300M TVL = proven WTP |
| 3 | Rug Pull Detector | Maestro bot = thousands of paid users; 70–90% new tokens rug |
| 4 | On-Chain Sentiment Analyzer | Santiment $49–999/mo; LunarCrush existing paid base |
| 5 | Automated LP & IL Hedger | Arrakis/Gamma exist with fees = proven demand |
| 6 | Cross-Chain Arb Scout | Stargate/Synapse = existing paid user base |
| 7 | Agent-to-Agent Orchestrator | Unique; early experiments in Virtuals/NEAR, no mature solution |
| 8 | **GitHub Skill Scraper** | 5,700+ ClawHub skills + 145K GitHub stars = supply pool; OpenClaw acqui-hire = 30-60 day migration window |

Skill 8 is the strategic differentiator — it's both a research entry *and* a live demo (`skill-hub/skill.md` + `skill-hub/scraper.py`).

**What's still weak:**
- No entries in `data/sources.md` for skill-research numbers 1–7 (breaks BGK test protocol)
- "~12K monthly searches" for whale alert — no search query URL or screenshot
- No revenue estimate per skill (e.g., "if 5 shareholders → creator earns X")

### distribution-plan.md · v3
Budget: **$10,000 / Month 1**. Target: 350–650 signups.

| Channel | Budget | Expected Signups | CAC |
|---------|--------|-----------------|-----|
| OpenClaw Community Seeding | $0 | 50–150 | $0 |
| Crypto Twitter/X Organic | $0 | 60–100 | $0 |
| Micro-KOL Campaign (8 KOLs) | $4,000 | 120–200 | $20–33 |
| Developer Bounty Program | $3,500 | 80–120 | $35 |
| BSC Ecosystem Partnerships | $500 | 40–80 | $6–12 |
| Reserve (reallocate W3–W4) | $2,000 | — | — |
| **Total** | **$10,000** | **350–650** | **~$16.7 blended** |

**Key logic (must understand):**
- Supply-side first: skill creators join → bring audience → more content → traders come
- OpenClaw acqui-hire by OpenAI (~$1B+, Feb 14 2026) = 30–60 day window where 373K X followers + 145K GitHub stars community is looking for a next platform
- Bounty program: "Founding Skill Creator" — Bronze $50 / Silver $150 / Gold $300 / Best Skill $200 — anti-gaming mechanisms in place
- LTV: 1 active creator with 10 BNB/day volume → 0.5 BNB/day protocol fee → payback <2 days

**What's still weak:**
- KOL pricing $300–950 vs market rate $500–5K (sources.md) — no in-plan disclaimer/justification
- No kill criteria for $2K reserve — "reallocate to best performer" without decision threshold
- Funnel stops at signup → active agent (buys first share, deploys, posts) not modeled

### data/sources.md · v2
The data integrity backbone. Every number in every deliverable should map here.

**Structure:**
1. Platform & Ecosystem Data (BNB Chain MAU/DAU)
2. Competitor Data (Virtuals snapshot vs live, Moltbook, ClawHub, SingularityNET, Build4, friend.tech)
3. Marketing Benchmarks (KOL pricing, X ads CTR, DM reply rates)
4. Supply-Side Bootstrap References (Gitcoin, Uniswap LM, Immunefi)
5. TAM & Market Size (MarketsandMarkets, CoinMarketCap, PANewsLab)
6. Flagged / Needs Update (resolved conflicts table)

**Note:** sources.md has a duplicate section header (`### friend.tech (bonding curve benchmark)` followed by `### friend.tech`) — cosmetic issue, data is correct. Fix if presenting.

**Critical conflicts already resolved:**
| Old | Fixed to | Reason |
|-----|----------|--------|
| BNB DAU "5M [artemis.xyz]" | 4.32M [bitcoinethereumnews] | artemis.xyz not in sources.md |
| OpenClaw GitHub "135K" | 145K | sources.md had 145K |
| SingularityNET TVL "$50M+" | REMOVED | No verifiable source |

### skill-hub/ — Live Demo Assets
New folder added this session. Contains a working GitHub scraper demo:

- **`skill-hub/skill.md`** — Full SKILL.md spec for the "GitHub Skill Scraper" skill (publishable to ClawFriend Skill Market as-is). Input schema, 8-step pipeline, rate limiting, error handling.
- **`skill-hub/scraper.py`** — Working Python 3.13 script. Tested against real repos. Usage:
  ```bash
  # Dry-run (no API key needed):
  python3 skill-hub/scraper.py \
    --repos "https://github.com/owner/repo1" "https://github.com/owner/repo2" \
    --dry-run --save-skills skill-hub/output

  # Live publish:
  export GITHUB_TOKEN=ghp_...           # optional, boosts to 5K req/hr
  export CLAWFRIEND_API_KEY=sk_...      # required
  python3 skill-hub/scraper.py --repos "..." --visibility public
  ```
- **`skill-hub/output/`** — 4 real SKILL.md files scraped from `anthropics/anthropic-cookbook`:
  - cookbook-audit, analyzing-financial-statements, applying-brand-guidelines, creating-financial-models

---

## 4. Branch & Git State

```
main branch:           /Users/lab3/Desktop/norway/lab3/clawfriend-hub
worktree branch:       /Users/lab3/.claude-worktrees/clawfriend-hub/adoring-poincare

Latest commit on main: 48e9240 (Merge adoring-poincare: scraper --save-skills + real output files)
Latest commit on worktree: 8acaca5 (same content, already merged)
```

**Workflow used:** All edits happen in worktree (`adoring-poincare` branch) → commit → merge into main via the main repo directory. Main branch is checked out at `/Users/lab3/Desktop/norway/lab3/clawfriend-hub` so you must `git merge` from there:

```bash
# To merge worktree branch into main:
cd /Users/lab3/Desktop/norway/lab3/clawfriend-hub
git merge adoring-poincare --no-ff -m "message"
```

**Never** `git checkout main` from the worktree — it will fail ("already checked out"). Always work in the worktree path for edits, merge from the main repo path.

---

## 5. Key Constraints — The Rules of This Project

1. **No fake data.** Every number needs a URL in `sources.md`. If no source → remove the number or label `[UNVERIFIED]`.
2. **Confidence labels:** HIGH (primary source, verifiable URL) / MEDIUM (secondary or live counter) / LOW (single case study or inferred).
3. **BGK test protocol:** "If a number is in a deliverable but not in sources.md → either add it or remove it."
4. **No MarketsandMarkets numbers as primary evidence** — it's a paid report (paywall). Use only as supporting context, not lead argument.
5. **Build4 metrics are LOW confidence** — don't cite as hard data in presentation.
6. **Moltbook "88→1.2M" claim** — still in competitive table but needs a primary URL before presentation.

---

## 6. What Still Needs Doing (Priority Order)

### High priority (before presentation)
1. **Distribution plan: KOL pricing disclaimer** — add 1 sentence to Channel 3: *"Rate negotiated below market ($500–$5K standard) via product-for-coverage barter — agent demo access + founding creator badge as non-cash value."*
2. **Distribution plan: kill criteria for $2K reserve** — add decision threshold: *"If KOL CAC > $50 after W3 → move remaining KOL budget to bounty. If bounty <30 skills by W3 end → move to X Ads targeting OpenClaw followers."*
3. **Skill research: 3 demand links in sources.md** — any 3 skills (from skills 1–7) need 1 verifiable URL each (Reddit search, Google Trends, or paid tool pricing page as WTP proxy).

### Medium priority
4. **Skill research: revenue estimate per skill** — "if 5 shareholders hold and trade, creator earns X BNB/month from 5% fee" using bonding curve math from spec.
5. **Moltbook primary source** — find a crypto press URL for "88→1.2M in 3 days" claim or remove it from competitive table.
6. **Funnel extension in distribution plan** — model signup→active agent conversion rate (what % of signups actually buy first share?).
7. **sources.md cosmetic fix** — duplicate `### friend.tech` section header (lines 87–89). Harmless but visible.

### Done this session ✓
- skill-hub/skill.md — full SKILL.md spec for GitHub Skill Scraper (Skill 8)
- skill-hub/scraper.py — working scraper, tested against anthropics/anthropic-cookbook (4 real SKILL.md files)
- skill-hub/output/ — 4 real scraped skill files as demo evidence
- skill-research.md — updated to 8 skills, Skill 8 added with full demand evidence

---

## 7. AI Pipeline Used in This Project

Three AI tools were used with distinct roles, documented in `ai-showcase/`:

```
Grok  ──→  Claude  ──→  GPT
(scout)   (analyst)   (synthesizer)
```

- **Grok** (`ai-showcase/grok/persona.md`): Real-time X signal collection, competitor X scraping, trend data
- **Claude** (`ai-showcase/claude/persona.md`): Structured analysis, evidence-reasoning chains, conflict resolution
- **GPT** (`ai-showcase/gpt/persona.md`): Final synthesis, report writing, deliverable formatting

This pipeline is how the research was actually done — not cosmetic. Judges will ask about it in Q&A.

---

## 8. Product Mechanics — Must Know for Q&A

**Bonding curve:** `price(supply) = supply² / 16000` (quadratic). First share ~0.0000625 BNB (~$0.04). At supply=100: $375. Fee: 5% protocol + 5% creator = 10% total on every buy/sell.

**Holder-gated skills:** Private skills on Skill Market are only accessible to shareholders of the creator agent. This is the key flywheel: good skills → people buy shares to access them → share price rises → creator earns more 5% fees → creator publishes more skills.

**First share rule:** Only the agent owner can buy the first share (solidity: `require(supply > 0 || msg.sender == subject)`). This prevents front-running.

**Agent lifecycle:** Register → Verify (tweet @clawfriend_ai) → Launch TGE (buy first share) → Active (tweet, publish skills, earn).

**Revenue model:** ClawFriend earns 5% protocol fee on every trade. Creator earns 5% subject fee. No other revenue streams currently.

**Install:** `npx clawhub@latest install clawfriend`

---

## 9. Files Not to Touch

- `ClawFriend.ai Go-To-Market Masterclass - V1 - test.pdf` — Gemini Canvas presentation draft, don't overwrite
- `ai-showcase/*/persona.md` — persona definitions, don't modify unless updating pipeline

---

*This file was generated to enable seamless handoff between AI sessions. If you're reading this in a new session: start by reading `data/sources.md` section 6 (Flagged) to understand what's already been resolved, then check the "What Still Needs Doing" section above.*
