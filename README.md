# COOK A WEB3 SKILL MARKETPLACE
**Last updated:** 2026-02-25

---

## TL;DR

laughing-yalow = Web3 AI Agent Economy on BSC. Product is built.
This repo answers 3 questions: **Who are the competitors? What skills should exist? How do we get 600 users with $10K?**

---

## REPO STRUCTURE

```
/
├── README.md                        ← you are here
├── competitive-landscape.md         ← Deliverable 1 (25%) · v3
├── skill-research.md                ← Deliverable 2 (25%) · v1
├── distribution-plan.md             ← Deliverable 3 (40%) · v3
├── ai-showcase/
│   ├── claude/persona.md            ← Claude role: Strategic Analyst
│   ├── gpt/persona.md               ← GPT role: Synthesizer & Writer
│   └── grok/persona.md              ← Grok role: Social & Trend Scout
└── data/
    └── sources.md                   ← Raw sources & verified data points · v2
```

---

## DELIVERABLES

### 1. Competitive Landscape · `competitive-landscape.md` · v3
10 competitors analyzed across **5 tiers**: Full-Stack / Social-Only / Marketplace-Only / Economic-Launchpad / Adjacent.
Strategic verdict per tier answers the only question that matters: **who is actually competing for our user?**

**Conclusion:** laughing-yalow is the only platform combining bonding curve + skill market + on-chain social layer + holder-gated content on BNB Chain. No single competitor has all four.

→ [competitive-landscape.md](./competitive-landscape.md)

---

### 2. Skill Research · `skill-research.md` · v1
7 proposed skills with proven demand. Each includes: target user, problem, current alternatives, PMF evidence, visibility strategy (public → private/holder-gated).
**No skill is justified by gut feel — every claim has a data source.**

→ [skill-research.md](./skill-research.md)

---

### 3. Distribution Plan · `distribution-plan.md` · v3
$10,000 / Month 1. 5 channels. Unit economics specific enough for an intern to execute tomorrow.

| Channel | Budget | Expected Signups |
|---------|--------|-----------------|
| OpenClaw Community Seeding | $0 | 50–150 |
| Crypto Twitter / X Organic | $0 | 60–100 |
| Micro-KOL Campaign (8 KOLs) | $4,000 | 120–200 |
| Developer Bounty Program | $3,500 | 80–120 |
| BSC Ecosystem Partnerships | $500 | 40–80 |
| Reserve (reallocate Week 3–4) | $2,000 | — |
| **Total** | **$10,000** | **350–650** |

**Blended CAC:** ~$16.7–$28.6 | **Payback:** <2 days if creator runs 10 BNB/day volume

→ [distribution-plan.md](./distribution-plan.md)

---

## KEY INSIGHT

> OpenClaw founder acqui-hired by OpenAI ($1B+, Feb 14 2026).
> The ecosystem — 373K X followers, 145K GitHub stars — is looking for a next platform.
> **Window: 30–60 days. laughing-yalow needs to move now.**

---

## AI SHOWCASE

Research pipeline used across all 3 deliverables:

| Role | Tool | Persona |
|------|------|---------|
| Social & trend scout | Grok | [grok/persona.md](./ai-showcase/grok/persona.md) |
| Strategic analyst | Claude | [claude/persona.md](./ai-showcase/claude/persona.md) |
| Synthesis & writer | GPT | [gpt/persona.md](./ai-showcase/gpt/persona.md) |

Grok scouts real-time X signals → Claude analyzes and structures → GPT synthesizes into deliverable format.

---

## DATA INTEGRITY

Every data point has a verifiable source. No AI-hallucinated numbers.
All conflicts between files are documented and resolved in [`data/sources.md`](./data/sources.md).

---

## VERSION LOG

| File | Version | Changes |
|------|---------|---------|
| competitive-landscape.md | v3 | 5-tier framework; fixed BNB DAU source (artemis.xyz→bitcoinethereumnews 4.32M); fixed GitHub stars 135K→145K; removed SingularityNET TVL (no source); flagged Build4 as indicative; added one-sentence positioning + win/lose table |
| competitive-landscape.md | v2 | Added feature matrix; inline source links; win/lose by segment; expand conclusion |
| distribution-plan.md | v3 | Fixed conversion rate benchmarks (WebFX 2026, Flexe.io); updated BNB MAU 1M→60M; added DM script + tweet drafts; fixed KOL pricing note; added bounty anti-gaming; swapped DefiLlama→Dune Analytics |
| distribution-plan.md | v2 | Fixed OpenClaw stats attribution (TAM vs owned assets); added zero-baseline section; corrected data sources table |
| data/sources.md | v2 | Added competitor sections (Virtuals, Moltbook, ClawHub, SingularityNET, Build4); added TAM section; resolved all cross-file conflicts; expanded flagged table |
| data/sources.md | v1 | Written from scratch — 15+ verified data points, confidence levels, flagged unverified claims |
| skill-research.md | v1 | 7 skills with demand evidence (GrokX research) |
| ai-showcase/ | v1 | 3 AI persona files: Grok (scout) → Claude (analyst) → GPT (synthesizer) |
| README.md | v2 | Updated structure, versions, AI showcase section |
