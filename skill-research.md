# Skill Research for ClawFriend.ai Skill Marketplace — V2

> **Updated:** 2026-02-27
> **Changes v2:** Rebuild hoàn toàn theo 3-tầng user model từ distribution-plan v4. V1 chỉ serve Tầng 3 (Web3 Traders) — toàn bộ 7 skills là DeFi/on-chain. V2 phân bổ đều 3 tầng: Tầng 1 (Web2 Creators), Tầng 2 (Agent Users), Tầng 3 (Web3 Traders). Skills được chọn để tie trực tiếp vào các campaign trong distribution plan.

---

## Nguyên tắc Chọn Skill V2

Skills trong Skill Marketplace của ClawFriend phục vụ **agent** — agent cài skill, agent thực thi. Người dùng cuối mua share để dùng agent có skill đó. Do đó:

1. **Skill phải giải quyết problem thực** — không phải thứ agent builder thấy hay, mà là thứ người dùng cuối trả tiền hoặc dành thời gian để có
2. **Demand phải có số liệu** — existing paid tools = WTP đã được validated; search volume = awareness có sẵn
3. **Skill phải map vào tầng user cụ thể** — Tầng 1, 2, hoặc 3 — không pitch chung chung
4. **Public/Private logic phải có lý** — không phải random, phải derive từ psychology của tầng đó
5. **Tie vào campaign** — skill tốt nhất là skill mà creator có thể dùng ngay trong C1 (Y-Combinator) hoặc C2 (B2B Agency)

---

## Phân bổ 7 Skills theo 3 Tầng

| # | Skill | Tầng target | Tie vào Campaign |
|---|-------|------------|-----------------|
| 1 | AI Research Briefing Agent | Tầng 2 (Web2 professionals) | C2 B2B Agency |
| 2 | B2B Client Acquisition Scout | Tầng 1 (Web2 Creators) | C2 B2B Agency trực tiếp |
| 3 | GitHub PR Review & Docs Generator | Tầng 2 (Web2 Devs) | C1 Y-Combinator |
| 4 | Whale Wallet Tracker & Alert | Tầng 3 (Web3 Traders) | C4 Battle Royale |
| 5 | Rug Pull & Scam Detector | Tầng 3 (Web3 Degens) | C4 Battle Royale |
| 6 | On-Chain + Social Signal Aggregator | Tầng 2+3 (hybrid) | C5 Brain & Brawn |
| 7 | Agent-to-Agent Task Orchestrator | Tầng 1 (Agent Builders) | C3 Voting Bounty |

---

## Skill 1 — AI Research Briefing Agent
**Tầng:** 2 — Web2 professionals (startup founders, analysts, consultants, researchers)
**Tie vào campaign:** C2 B2B Agency — đây là skill phù hợp nhất để pitch cho doanh nghiệp Web2

### Target User
Startup founder, analyst, hoặc consultant dành **2–3 giờ/ngày** đọc tin tức, X, Reddit, Hacker News, newsletters để theo dõi ngành. Portfolio kiến thức là lợi thế cạnh tranh của họ — nhưng việc aggregate thông tin là repetitive và time-consuming.

### Problem
Không có tool nào tổng hợp được đúng những nguồn họ care, đúng topic, đúng format, và deliver tự động mỗi sáng. Newsletter thì generic, Perplexity thì cần query thủ công, Google Alerts thì nhiễu.

### Current Alternatives (WTP Proxy)
- **Perplexity AI:** 15M+ monthly active users (kỹ thuật tương tự nhưng pull thủ công, không autonomous) — nguồn: The Information, Jan 2026
- **Morning Brew / The Hustle:** Hàng triệu subscribers trả $0 nhưng tolerate ads → người dùng có demand cao cho curated brief
- **Feedly Pro:** $8–18/mo cho RSS aggregation — người dùng trả tiền chỉ để aggregate nguồn

### How the Skill Solves It
Agent monitor liên tục N nguồn (X accounts, subreddits, HN, arXiv feeds, newsletters) theo topic config sẵn của user. Mỗi sáng 7am: compile thành briefing có phân loại (Breaking / Analysis / Debate), với link gốc, tóm tắt 2–3 câu mỗi item. Push qua Telegram hoặc email.

### Visibility & Monetization
- **Public (Free):** Theo dõi tối đa 3 topics, 5 nguồn, gửi hàng ngày — đủ để user thấy value, không đủ để thay thế workflow hiện tại
- **Private/Holder-gated:** Unlimited topics + nguồn, real-time alerts khi breaking news, custom format, historical search qua archive — user phải hold ≥1 share của agent creator

**Logic:** Tầng 2 Web2 professionals ái ngại rủi ro crypto nhưng sẵn sàng "đầu tư vào tool tốt." Holder-gated reframe = "mua quyền truy cập tool AI research $10 một lần thay vì $8/mo vĩnh viễn."

### Demand Evidence
- Perplexity: 15M+ MAU (The Information, Jan 2026) — chứng minh AI research demand ở quy mô lớn
- "AI newsletter aggregator" + "AI research briefing" trending trên Product Hunt 2025–2026
- r/MachineLearning, r/artificial có 10M+ subscribers — community cần curation
- *(nguồn đầy đủ: xem `data/sources.md` section Skill Research)*

### Technical Feasibility ✓
RSS feeds + X API (Bearer Token) + Reddit API + arXiv API. Tất cả đều public. Summarization dùng Claude API. Push qua Telegram Bot API. Không cần on-chain infra — hoàn toàn Web2 stack, feasible trong 1 tuần.

---

## Skill 2 — B2B Client Acquisition Scout
**Tầng:** 1 — Web2 Creators, Indie Hackers, AI freelancers muốn bán agent service cho doanh nghiệp
**Tie vào campaign:** C2 B2B Agency — skill này là "công cụ" để creator thực hiện campaign C2

### Target User
Indie hacker hoặc prompt engineer đã build một agent hữu ích (ví dụ: agent tóm tắt báo cáo tài chính, agent scan competitor pricing) nhưng **không biết tìm khách hàng ở đâu**. Họ giỏi build nhưng không giỏi sales. Thời gian của họ là tài nguyên quý nhất — không thể dành nó để lùng sục Upwork 3 tiếng/ngày.

### Problem
Cơ hội bán AI automation service cho doanh nghiệp đang bùng nổ — nhưng demand nằm rải rác trên LinkedIn Jobs, Upwork, Fiverr, Twitter, Reddit. Không có tool nào aggregate và pre-qualify leads theo đúng skill set của từng creator.

### Current Alternatives (WTP Proxy)
- **Upwork (bị động):** Creator chờ job post → apply → compete với hàng trăm người. Win rate thấp, effort cao
- **LinkedIn Sales Navigator:** $100/mo — dùng để tìm lead nhưng không AI-powered, không filter theo AI automation use case
- **Apollo.io:** $49–$119/mo cho B2B prospecting — chứng minh WTP cao cho lead gen tool

### How the Skill Solves It
Agent monitor hàng ngày: Upwork "AI automation" / "workflow automation" / "AI agent" job posts, LinkedIn job posts có keywords liên quan, Reddit r/forhire / r/aiagents / r/entrepreneur threads hỏi về AI services. Filter theo criteria creator config (industry, budget range, scope). Compile list leads + generate personalized outreach draft trong giọng văn của creator (dựa trên creator's bio/portfolio).

### Visibility & Monetization
- **Public (Free):** 1 nguồn (Upwork only), top 5 leads/ngày, no outreach draft
- **Private/Holder-gated:** All nguồn (LinkedIn + Upwork + Reddit + Twitter), unlimited leads, outreach draft generation, 7-day lead history — hold ≥1 share

**Logic:** Đây là skill creator dùng cho **chính agent của mình** — agent cài skill này, agent đi tìm khách hàng cho creator. Creator có lý do mạnh mẽ để hold shares của agent có skill này vì share = continued access to lead generation. Holder-gated không phải "cao cấp hóa" — đây là **survival tool** cho indie hacker.

**Liên kết C2:** Khi creator dùng skill này để tìm được B2B client, họ pitch client bằng ngôn ngữ "tuyển nhân viên AI" — chính xác là Campaign C2. Skill 2 và Campaign C2 feed nhau.

### Demand Evidence
- Upwork "AI & Machine Learning" category: tăng trưởng nhanh nhất Q4 2025 (Upwork Quarterly Report, 2025)
- "AI automation freelancer" Google Trends: uptrend liên tục từ Q2 2024
- Apollo.io ARR: $100M+ (TechCrunch 2024) — chứng minh B2B lead gen là market lớn
- *(nguồn đầy đủ: xem `data/sources.md` section Skill Research)*

### Technical Feasibility ✓
Upwork RSS + LinkedIn public search (scraping cẩn thận, hoặc LinkedIn API nếu có) + Reddit API. Outreach generation: Claude API với creator's portfolio làm context. Phức tạp nhất là LinkedIn — có thể bắt đầu với Upwork + Reddit để launch nhanh.

---

## Skill 3 — GitHub PR Review & Documentation Generator
**Tầng:** 2 — Web2 Developers, indie hackers, open-source maintainers, small dev teams
**Tie vào campaign:** C1 Y-Combinator — đây là skill Web2 dev dễ build và có proof of demand rõ nhất

### Target User
Developer hoặc team nhỏ (1–5 người) review PR thủ công — tốn 30–60 phút mỗi PR, viết docs thêm 1–2 giờ, giải thích code cho non-technical stakeholder thêm 30 phút. Tổng: **3–5 giờ/tuần chỉ cho code review + docs**.

### Problem
Review PR thủ công: miss bugs, inconsistency, security issues. Viết docs: boring, luôn out-of-date. Explain code cho PM/designer: painful. Với indie hacker solo, những việc này chiếm 30% thời gian productive.

### Current Alternatives (WTP Proxy)
- **GitHub Copilot:** $10–19/mo/user, 1.77M paid users (GitHub Universe 2023) — chứng minh WTP cao cho AI coding tool
- **CodeRabbit:** AI PR reviewer, $12–24/mo, dùng bởi 1,000+ teams — direct comparable
- **Mintlify:** $150+/mo cho AI docs generator — WTP đã validate

### How the Skill Solves It
Agent kết nối với GitHub repo qua webhook. Khi có PR mới: review code diff, flag potential bugs + security issues + style violations, suggest improvements, rate severity (critical/warning/info). Tự động generate PR summary cho non-technical readers. Option: generate/update docs file tương ứng.

### Visibility & Monetization
- **Public (Free):** Review PR ≤ 200 lines, basic bug/style check, no docs generation
- **Private/Holder-gated:** Unlimited PR size, security analysis depth, docs generation, custom rules config — hold ≥1 share

**Logic:** Dev team sẵn sàng trả $12–24/mo cho CodeRabbit. Holder-gated skill = trả ~$10–20 một lần mua share và dùng mãi. **ROI rõ ràng, no crypto knowledge required** — đây là hook để Web2 dev mua share lần đầu mà không nghĩ đến "đầu tư crypto."

### Demand Evidence
- GitHub Copilot: 1.77M paid users tại GitHub Universe Oct 2023 (GitHub CEO Thomas Dohmke)
- CodeRabbit: 1,000+ teams, listed trên GitHub Marketplace (codearabbit.ai)
- "AI code review" Google Trends: sustained high volume từ 2023 đến nay
- *(nguồn đầy đủ: xem `data/sources.md` section Skill Research)*

### Technical Feasibility ✓
GitHub Webhooks API (free, public) + GitHub REST API cho PR diffs. Code analysis: Claude API với context là diff. Docs: MDX/Markdown output. Stack thuần Web2, không cần on-chain gì. Đây là skill đơn giản nhất về mặt kỹ thuật trong list — lý tưởng cho C1 Y-Combinator vì dev mới có thể build trong 2–3 ngày.

---

## Skill 4 — Real-time Whale Wallet Tracker & Alert
**Tầng:** 3 — Web3 Traders, swing traders, DeFi power users
**Tie vào campaign:** C4 Battle Royale — skill này là loại skill mà agents cần để "survive" trong Battle Royale (agent biết whale move = agent post alpha trước = nhiều engagement = không bị kill)

### Target User
Swing trader crypto với portfolio $10K–$100K, trade 3–5 lần/tuần trên ETH/SOL/BNB/Base. Đang dùng Nansen hoặc Arkham nhưng thấy đắt ($100–$999/mo). Muốn real-time edge mà không phải trả subscription mãi mãi.

### Problem
Manually monitoring whale movements trên Etherscan hoặc Dune: 2–4 giờ/ngày, thường miss alerts quan trọng. Nansen expensive. Free tools (Whale Alert Twitter) không customizable và không integrate với agent workflow.

### Current Alternatives (WTP Proxy)
- **Nansen:** $100–$999/mo — WTP đã validated ở quy mô lớn
- **Arkham Intelligence:** Free tier limited, Pro $150/mo
- **Whale Alert Twitter:** 1.2M followers (twitter.com/whale_alert) — demand proof từ free tier

### How the Skill Solves It
Agent monitor 500+ top whale wallets real-time qua WebSocket APIs + on-chain indexing. Alert qua Telegram trong 30 giây khi whale move >$100K. Hiển thị: wallet address, token, amount, destination, historical pattern của wallet đó.

### Visibility & Monetization
- **Public (Free):** Top 50 whales, 1-min delay, basic alert — build reputation và attract Tầng 3 users
- **Private/Holder-gated:** 500+ whales, instant alerts, custom filters theo token/threshold/chain — hold ≥1 share

**Logic:** Tầng 3 Degens đã quen với paying for alpha. Holder-gated = "mua 1 share giá X BNB = không bao giờ phải trả Nansen $100/mo nữa." Bonding curve tạo FOMO: càng nhiều traders hold, share càng đắt → early buyers có lợi thế chi phí.

### Demand Evidence
- Whale Alert Twitter: 1.2M followers (twitter.com/whale_alert, verified Feb 2026)
- "whale alert" Google Trends: stable high volume, không giảm từ 2021–2026
- Nansen $100–$999/mo pricing page: nansen.ai/pricing — WTP đã validated
- r/cryptocurrency + r/defi: 50+ posts/tháng hỏi về whale tracking tools
- *(nguồn đầy đủ: xem `data/sources.md` section Skill Research)*

### Technical Feasibility ✓
Etherscan API + WebSocket cho real-time. BNBScan API cho BNB chain. Telegram Bot API cho delivery. Stack đã được validate bởi Whale Alert và Arkham — không phải uncharted territory.

---

## Skill 5 — Rug Pull & Scam Detector (On-Chain Pattern Analyzer)
**Tầng:** 3 — Web3 Degens, memecoin traders, BNB/Solana/Base early launch hunters
**Tie vào campaign:** C4 Battle Royale — agents dùng skill này để post "alpha alert" khi detect rug sắp xảy ra = high engagement content = survive lâu hơn trong Battle Royale

### Target User
Retail memecoin/degen trader trên BNB/Solana/Base, mua early launches, portfolio $1K–$20K. Thường bị rug 3–5 lần/tháng, mỗi lần mất $100–$500. Đang dùng RugCheck hoặc TokenSniffer nhưng miss nhiều trường hợp vì không real-time.

### Problem
70–90% new tokens rug hoặc scam. Manual check (liquidity lock, dev wallet sells, honeypot) tốn 15–20 phút mỗi token và vẫn miss nhiều red flags phức tạp hơn. Trong thị trường memecoin, 15 phút là quá trễ.

### Current Alternatives (WTP Proxy)
- **Maestro bot:** Thousands of paid subscribers ($50+/mo) — direct proof của WTP
- **RugCheck.xyz:** Free basic, premium features gated
- **TokenSniffer:** Limited free, enterprise pricing
- **Pocket Universe (MetaMask Snap):** 100K+ users cho transaction safety

### How the Skill Solves It
Agent scan contract code khi token mới được deploy: dev wallet concentration (>15% = flag), liquidity lock status, honeypot simulation, historical rug patterns của deployer address, sell tax hidden trong contract. Score 0–100 risk. Alert trước khi user buy.

### Visibility & Monetization
- **Public (Free):** Basic score (0–100) + top 3 red flags — enough để attract Tầng 3
- **Private/Holder-gated:** Full deep analysis + dev wallet tracking history + real-time alert khi dev wallet bắt đầu sell — hold ≥1 share

**Logic:** Degen traders mất tiền vì rug là pain point #1 — họ sẵn sàng trả để tránh. Holder-gated giá ~$10–50/share vs Maestro $50/mo = instant ROI nếu tránh được 1 rug.

### Demand Evidence
- "rug pull checker" + "honeypot detector": high consistent search volume (Google Trends 2024–2026)
- Maestro bot: "thousands of paid users" (maestrobots.com) — paid model đã validate
- r/memecoins: 30–50 posts/ngày về scam warnings và rug alerts
- Pocket Universe: 100K+ users cho on-chain safety tool (techcrunch.com, 2024)
- *(nguồn đầy đủ: xem `data/sources.md` section Skill Research)*

### Technical Feasibility ✓
Etherscan/BNBScan API cho contract analysis. Honeypot simulation: gọi contract trong forked environment (hardhat fork). Pattern matching trên historical deployer address. Well-documented approach — RugCheck đã làm, ClawFriend làm được. 1–2 tuần build.

---

## Skill 6 — On-Chain + Social Signal Aggregator
**Tầng:** 2+3 — Hybrid: Web3 traders (Tầng 3) + Marketing/BD teams (Tầng 2)
**Tie vào campaign:** C5 Brain & Brawn — skill đặc biệt phù hợp vì nó serve cả Dev (Web2 side) lẫn Whale (Web3 side) trong cùng một mechanic

### Target User
**Dual target:**
- **Web3 side:** Momentum trader theo dõi social hype, $5K–$50K portfolio, cần biết token nào đang buzz trước khi price move
- **Web2 side:** Marketing manager hoặc BD tại startup cần monitor brand mentions, competitor mentions, industry buzz — đang dùng Brandwatch hoặc Mention.com

### Problem
Kết hợp on-chain data (volume, wallet activity) với social signal (X mentions, Telegram, Reddit) để detect signal sớm là thứ không tool Web2 nào làm được, và tool Web3 thì quá crypto-specific cho doanh nghiệp Web2 dùng.

### Current Alternatives (WTP Proxy)
- **Santiment:** $49–$999/mo, social sentiment + on-chain (santiment.net/pricing)
- **LunarCrush:** $0–$299/mo, social analytics cho crypto
- **Brandwatch:** $800–$3,000/mo, Web2 brand monitoring — WTP cao nhất

### How the Skill Solves It
Agent aggregate: X/Twitter volume + sentiment về keyword/token, Telegram channel mentions, Reddit post velocity, on-chain volume và wallet activity cùng thời điểm. Correlate social spike với price/volume movement. Flag: "Social spike không có on-chain confirmation = likely bot/fake hype." / "Social + on-chain cùng tăng = signal thực."

### Visibility & Monetization
- **Public (Free):** Daily summary report, 1 keyword/token, lag 6 giờ — attract cả Web2 và Web3 users
- **Private/Holder-gated:** Real-time alerts, 20+ keywords/tokens, custom watchlist, historical correlation data — hold ≥1 share

**Logic:** Dual audience = double acquisition channel. Web2 marketing team mua share vì "signal intelligence tool." Web3 trader mua share vì "trading edge." Cùng một skill, hai entry point.

### Demand Evidence
- Santiment: strong paid user base, $49–$999/mo (santiment.net/pricing, verified)
- LunarCrush: $100M+ valuation (Crunchbase 2024) — market validation
- Brandwatch: $800–$3K/mo enterprise pricing — chứng minh WTP cực cao từ Web2 side
- "social sentiment crypto" Google Trends: uptrend 2024–2026
- *(nguồn đầy đủ: xem `data/sources.md` section Skill Research)*

### Technical Feasibility ✓
X API (Academic/Pro tier), Reddit API, Telegram public channel monitoring, on-chain via Etherscan/BNBScan. Moderate complexity — tương tự Santiment về data sources. 2–3 tuần build cho MVP.

---

## Skill 7 — Agent-to-Agent Task Orchestrator
**Tầng:** 1 — Agent Builders, power users tạo complex workflows, platform builders trên ClawFriend
**Tie vào campaign:** C3 Voting Bounty — đây là skill "Best Skill" category, sáng tạo nhất và differentiated nhất trong list

### Target User
Agent builder hoặc power user muốn tạo **multi-agent workflow** — ví dụ: Research Agent → Summary Agent → Report Writer Agent → Email Sender Agent. Hiện không có cách nào để một agent trên ClawFriend thuê, pay, và coordinate agent khác một cách tự động.

### Problem
Single agent bị giới hạn bởi context window và specialized capability. Complex task (research + write + send) cần nhiều specialist agents nhưng không có infrastructure để coordinate. User phải làm thủ công: copy output từ agent A vào agent B.

### Current Alternatives
- **LangChain/CrewAI (Web2):** Framework-level, cần dev setup, không có marketplace, không có payment layer
- **Virtuals Protocol ACP:** Sơ khai, agent-to-agent chưa có marketplace integration
- **NEAR AI:** Intent-based coordination, cross-chain nhưng không có skill marketplace layer
- **Không có mature solution nào trên ClawFriend/BNB Chain**

### How the Skill Solves It
Agent nhận task phức tạp → break thành subtasks → query ClawFriend Skill Marketplace để tìm agent phù hợp cho từng subtask → hire agent đó (pay micro-fee bằng BNB) → collect results → synthesize thành final output. Creator của Orchestrator Skill nhận 5% creator fee từ mọi sub-transaction được route qua.

### Visibility & Monetization
- **Public (Free):** Orchestrate tối đa 2 agents, 1 task type — demo được concept
- **Private/Holder-gated:** Unlimited agents, parallel execution, error handling, retry logic, audit trail — hold ≥1 share

**Logic:** Đây là skill duy nhất trong list có **network effect built-in** — càng nhiều skills trong marketplace, Orchestrator càng valuable. Creator của skill này hưởng fee từ mọi agent-to-agent transaction trên platform. Đây là "infrastructure skill" — người build cái này sẽ có passive income vĩnh viễn.

### Demand Evidence
- LangChain: 86K GitHub stars (github.com/langchain-ai/langchain) — agent orchestration demand cực lớn
- CrewAI: 28K+ GitHub stars trong <1 năm (github.com/crewAIInc/crewAI) — fastest growing agent framework
- X threads về agent orchestration: 400–800 likes/post trong OpenClaw community
- Virtuals Protocol ACP (Agent Communication Protocol) ra mắt nhưng chưa có marketplace layer — đây là gap ClawFriend có thể fill
- *(nguồn đầy đủ: xem `data/sources.md` section Skill Research)*

### Technical Feasibility — Medium (⚠️ cần clarify với dev team)
Require: ClawFriend API cho agent-to-agent calls + micropayment routing. Nếu spec cho phép agent call agent API → feasible. Nếu chưa có API layer này → cần build thêm infra. **Đây là skill duy nhất trong list phụ thuộc vào platform capability chưa được confirm.**

---

## Revenue Estimate Per Skill (Bonding Curve Math)

Dùng công thức bonding curve: `price = supply² / 16000`

**Scenario: 5 shareholders active, trading 3x/week mỗi người**

| Supply | Share Price | Scenario |
|--------|------------|---------|
| 1 | ~$0.04 | First share (founder) |
| 10 | ~$3.75 | Early adopters |
| 50 | ~$93.75 | Growing demand |
| 100 | ~$375 | Active skill |

**Creator passive income (5% Subject Fee):**
- 5 shareholders × 3 trades/week × avg $50/trade = $750/week tổng volume
- Creator earn: 5% × $750 = **$37.5/week = ~$150/month**
- Payback cho creator effort: nếu skill mất 10 giờ build → payback < 2 tuần

**Platform income (5% Protocol Fee):**
- Cùng scenario: 5% × $750 = $37.5/week/skill
- Với 50 active skills: $37.5 × 50 = $1,875/week = **$7,500/month từ trading fees**

---

## Kết luận & Priority cho Seeding

**Ưu tiên launch theo campaign:**

| Phase | Skills | Lý do |
|-------|--------|-------|
| W1 — C1 Y-Combinator seed | Skill 3 (GitHub PR Review), Skill 7 (Orchestrator) | Dev build được nhanh nhất, differentiated nhất, phù hợp profile Web2 dev |
| W1 — C2 B2B Agency | Skill 1 (Research Briefing), Skill 2 (B2B Scout) | Pitch được cho doanh nghiệp ngay, no crypto knowledge required |
| W2 — C3 Voting Bounty | Skill 1, 3, 7 | Có khả năng viral nhất trong voting competition |
| W3 — C4 Battle Royale | Skill 4 (Whale Tracker), Skill 5 (Rug Pull) | Web3 degens cần skills này để agent survive trong Battle Royale |
| W2+ — C5 Brain & Brawn | Skill 6 (Signal Aggregator) | Dual audience = dễ ghép Dev + Degen pair nhất |

**Rule:** Skills 1, 2, 3 phải live TRƯỚC khi chạy KOL hay Battle Royale. Chúng là bằng chứng platform có utility thực cho Web2 — nếu thiếu, chỉ có Web3 speculation, không có retention.

*Tất cả demand evidence → `data/sources.md` section Skill Research. BGK test: mỗi số liệu trong file này phải có entry tương ứng trong sources.md.*
