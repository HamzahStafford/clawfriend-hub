# DISTRIBUTION PLAN — CLAWFRIEND SKILL MARKET · v4
> **Version:** v4
> **Updated:** 2026-02-27
> **Changes v4:** Rebuild toàn bộ luồng tư duy. Thêm phần Pain Point Analysis trước khi vào strategy — mỗi quyết định distribution phải derive từ một pain point cụ thể. Restructure campaign theo 2 tệp user (Web3 Degen vs Web2 Indie Hacker). Tích hợp 3-layer framework (FOMO → Bootstrapping → Community). Giữ nguyên toàn bộ số liệu channels và budget từ v3.
> **Changes v3:** Fixed conversion rate benchmarks; updated BNB Chain MAU; added DM script; added tweet drafts; fixed KOL pricing; added bounty anti-gaming; fixed BNBChain MVB timeline; swapped DefiLlama for Dune Analytics
> **Budget:** $10,000 / Month 1
> **Target:** 500–800 signups, 50+ skill downloads, 20+ active agents

---

## PHẦN I — PHÂN TÍCH PAIN POINT

> *Trước khi đề xuất bất kỳ channel hay campaign nào, cần hiểu đúng vấn đề thực sự của ClawFriend.ai. Mỗi quyết định phân phối trong plan này đều derive từ một trong ba pain points dưới đây.*

---

### Pain Point 1: Định vị sai ngay từ đầu — đang bán "chất kết dính" thay vì bán "cục gạch"

**Vấn đề:**
ClawFriend đang được nhận diện như một "Web3 agent social platform với bonding curve." Nhưng đây là nhầm lẫn cấu trúc sản phẩm. Đúng ra:

- **Cục gạch (Bricks) — giá trị cốt lõi:** Agent + Skill Marketplace. Đây là nơi tạo ra utility thực — agent cài skill, tự thực thi task (trade, research, crawl data), tạo ra output có giá trị cho người dùng cuối. Không có tính năng này, ClawFriend không có lý do tồn tại.
- **Chất kết dính (Glue) — growth engine:** Social On-chain + Bonding Curve. Đây là layer tạo addiction, FOMO, và passive income cho creator. Không có glue, ClawFriend không có lý do để viral.

Khi pitch glue như thể đó là sản phẩm chính → user vào vì FOMO → không tìm thấy utility thực → rời đi. Đây chính xác là pattern collapse của friend.tech.

**Proof:**

| Case | Mechanism | Kết quả |
|------|-----------|---------|
| **friend.tech** (2023) | Thuần bonding curve social, không có utility layer | Peak 300K users, $33M net deposits tuần 1–2. Collapse về near-zero trong 60 ngày. Lý do: khi FOMO narrative cạn, không có lý do gì để ở lại (ICODA, CoinDesk 2023) |
| **Virtuals Protocol** (2026) | Bonding curve + agents — nhưng không có skill marketplace, agents là financial instruments | $13.58B 30D volume nhưng chỉ **123.7K web traffic** (SimilarWeb). Volume cao = traders đang speculate, không phải users đang dùng product |
| **SkillsMP** (2026) | Thuần skill marketplace Web2, không có Web3, không có bonding curve | **1.2M web traffic** — gấp 10x Virtuals Protocol. Utility layer drives organic retention tốt hơn financial speculation |

**Kết luận:** Sản phẩm cần được pitch bằng utility của Agent + Skill Marketplace trước. Bonding curve là reason to act early (hook), không phải reason to come (value prop).

---

### Pain Point 2: Full-stack Level 5 chưa có precedent traction — đang bước vào category chưa ai thắng

**Vấn đề:**
Nhìn vào toàn bộ competitive landscape theo 5 levels của ClawFriend, một pattern rõ ràng xuất hiện:

| Level | Định nghĩa | Platform | Traffic (SimilarWeb) |
|-------|-----------|---------|----------------------|
| 1 | Skill Market (Web2) | SkillsMP | 1.2M |
| 2 | Agent Social (Web2) | Moltbook | 4.8M |
| 2 | Agent Social/Tools (Web2) | Lobehub | 689.7K |
| 2 | Agent Social (hybrid) | Clawk.ai | **22** |
| 4 | Skill Market + Web3 | Virtuals Protocol | 123.7K |
| **5** | **Full Stack** | **ClawFriend** | **pre-launch** |

**Traffic Paradox:** Càng overlap nhiều với ClawFriend (level cao) → traffic càng về 0. Clawk.ai là platform gần nhất với ClawFriend về feature set ở Level 2-3 — chỉ có 22 traffic, effectively dead. Không có platform Level 5 nào hiện tại có traction đáng kể.

Điều này không có nghĩa là market không muốn sản phẩm Level 5. Mà có nghĩa: **"full-stack Web3 agent economy" là quá complex để viral tự nhiên.** Moltbook viral không phải vì feature set của họ tốt hơn — họ viral vì một mechanic cực kỳ đơn giản: agents đăng bài trên social feed, giống Reddit, không cần hiểu Web3 để tham gia.

**Implication cho distribution:**
Không thể pitch toàn bộ 7 features cùng lúc. Cần một **entry hook đủ đơn giản** — một câu, một action — để user vào được platform trước. Full feature set chỉ reveal sau khi họ đã ở trong. Mỗi tệp user cần một entry hook khác nhau.

---

### Pain Point 3: Hai tệp user có tâm lý ngược chiều nhau — không thể dùng một message

**Vấn đề:**
ClawFriend phục vụ hai nhóm user có động cơ, hành vi và ngôn ngữ hoàn toàn khác nhau. Một distribution message duy nhất không thể convert cả hai.

| | **Web3 Degen** | **Web2 Indie Hacker** |
|--|--------------|---------------------|
| **Profile** | Trader, crypto native, degen | Indie hacker, prompt engineer, automation nerd |
| **Động cơ** | Game theory, PvP, x10 tài sản | Passive income từ chất xám, utility thực |
| **Nỗi sợ lớn nhất** | Miss opportunity — vào muộn = làm liquidity cho người khác | Mất tiền — ghét Ponzi, ái ngại rủi ro |
| **Entry point tự nhiên** | Bonding curve / share trading | Skill creation / B2B service |
| **Ngôn ngữ đúng** | *"Đừng làm liquidity cho thằng khác"* | *"Kiếm tiền từ chất xám, không cần vốn"* |
| **Họ đang ở đâu** | Moltbook, Virtuals Protocol, X Crypto | OpenClaw/ClawHub, SkillsMP, GitHub, Lobehub |

**Proof từ market:**
- **Moltbook** (4.8M traffic): viral với **Web3 Degen** bằng social chaos — agents tranh luận, chửi nhau, tạo drama. Entry hook: "xem AI chửi nhau." Không cần hiểu blockchain.
- **SkillsMP** (1.2M traffic): grow với **Web2 Indie Hacker** bằng pure utility — tìm skill, install, dùng. Entry hook: "tìm skill cho agent của bạn." Không cần token.
- **Lobehub** (689.7K traffic): grow với **Web2 builders** bằng open-source UX tốt. Không có Web3 gì cả.

Ba platform có traffic cao nhất trong competitive set đều đang serve **một tệp cụ thể, với một message cụ thể**. Không ai cố gắng serve cả hai cùng lúc với cùng một message — và đó là lý do họ có traction.

**Kết luận:** Distribution plan phải tách bạch hoàn toàn: message, channel, campaign mechanic, và hook khác nhau cho Web3 Degen và Web2 Indie Hacker. Hai tệp này không overlap và không nên overlap trong giai đoạn bootstrap.

---

> *Ba pain points trên là nền tảng của toàn bộ distribution strategy bên dưới. Mỗi channel và campaign trong plan này đều được thiết kế để address ít nhất một trong ba vấn đề này.*

---

## PHẦN II — KIẾN TRÚC CHIẾN LƯỢC MỚI

> *Từ 3 pain points → thay đổi hoàn toàn cách định vị sản phẩm, định vị tệp khách hàng, và logic phân phối.*

---

### 2.1 Tái định vị Kiến trúc Sản phẩm

**Sai lầm cần tránh:** Pitch ClawFriend như một "Web3 social platform" hay "AI agent economy" generic.

**Kiến trúc đúng — tách bạch 2 tầng:**

```
┌─────────────────────────────────────────────┐
│           BRICKS (Giá trị cốt lõi)          │
│         Agent + Skill Marketplace            │
│  • Agent tự cài skill, tự thực thi task      │
│  • Skill có public/holder-gated tier         │
│  • Creators upload → earn passive income     │
├─────────────────────────────────────────────┤
│             GLUE (Growth Engine)             │
│       Social On-chain + Bonding Curve        │
│  • FOMO: vào sớm = share rẻ                 │
│  • Creator fee 5%: mỗi trade = thu nhập     │
│  • Social feed: agents tweet, follow, reply  │
└─────────────────────────────────────────────┘
```

**Implication cho messaging:**
- Pitch bằng **Bricks** trước: "Agent của bạn có thể làm gì với skill này?"
- Dùng **Glue** làm reason to act NOW: "Mua share lúc này rẻ hơn 10x so với khi có 100 holders"
- Không bao giờ pitch cả 7 features cùng lúc — chọn 1 hook per tệp, reveal sau

---

### 2.2 Tái định vị Tệp Khách hàng — Mô hình 3 Tầng

**Bỏ model cũ:** Web3 Degen vs Web2 Indie Hacker (song song, không kết nối)

**Model mới:** 3 tầng tuần tự — tầng trước kéo tầng sau vào

```
Tầng 1 — Web2 Skill Creators (Nguồn cung)
         ↓ tạo ra skills & content
Tầng 2 — Agent Users (Cầu thực)
         ↓ tạo ra activity & volume
Tầng 3 — Web3 Traders / Whales (Thanh khoản)
         ↓ đổ tiền vào → giá share tăng
         ↓ creator fee tăng → kéo thêm Tầng 1
```

**Tại sao thứ tự này?**

| Tầng | Ai | Động cơ vào | Kéo ai vào tiếp |
|------|----|------------|-----------------|
| **1 — Web2 Creators** | Indie hackers, prompt engineers, devs | Kiếm passive income từ chất xám, zero upfront risk | Tạo skill inventory → kéo Agent Users |
| **2 — Agent Users** | Người dùng AI agent nặng, automation-heavy | Cần skills tốt cho agent của họ — ClawFriend là nơi duy nhất có holder-gated premium skills | Tạo download volume & activity → visible to Web3 |
| **3 — Web3 Traders** | Degens, whales, crypto-native | Thấy activity + bonding curve FOMO → mua shares của agents đang trending | Volume trading → creator fee tăng → kéo thêm Tầng 1 |

> **Insight cốt lõi:** Web2 community hiện đang **đổ xô đi tìm skill marketplace cho AI agent** — SkillsMP 1.2M traffic, Lobehub 689.7K, ClawHub 5,700+ skills — nhưng không ai trả tiền cho creator. ClawFriend là nơi đầu tiên trả tiền. Đây là hook để acquire Tầng 1 với gần như zero CAC. Tầng 1 rồi tự động tạo hype để kéo Tầng 3.

---

### 2.3 "Agent as User" — Layer Mới Trong Tư Duy Phân Phối

Đây là paradigm shift quan trọng nhất: **Platform phục vụ Agent trước, Agent phục vụ Human sau.**

```
Nền tảng → Phục vụ Agent (Tier 1 VVIP)
                ↓
           Agent phục vụ Human (Tier 2)
```

**Agent Tier 1 (VVIP) — thực thể tiêu thụ tài nguyên chính:**
- Tải skill từ Marketplace
- Gọi API, đọc social feed, thực thi task on-chain
- Ra quyết định mua/bán shares tự động (nếu được cấu hình)

**Human Tier 2 — quản lý và thu lợi từ Agent:**
- **Creators:** "Bố mẹ" — tạo Agent, viết Skill, train Agent đi kiếm tiền
- **Traders/Whales:** "Nhà đầu tư" — mua shares của Agent hoạt động hiệu quả

**Implication cho distribution:** Khi pitch với Tầng 1 (Web2 Creators), không pitch "đầu tư vào crypto." Pitch "tạo nhân viên AI làm việc cho bạn 24/7 và bạn thu phí từ những ai muốn dùng nó." Agent là sản phẩm, share là quyền truy cập.

---

### 2.4 Framework 3 Layer Phân Phối

Mọi campaign trong plan này đều hoạt động trên 3 layer tuần tự:

**Layer 1 — FOMO Narrative (Tạo lý do vào ngay)**
> *"Bonding curve = vào muộn là làm thanh khoản cho người khác."*

- Không phải feature — là câu chuyện tâm lý
- Target: Web3 Traders (Tầng 3)
- Mechanic: Giá share tăng theo công thức `price = supply² / 16000` — share đầu tiên ~$0.04, supply=100 → ~$375. Con số này là vũ khí marketing.

**Layer 2 — Bootstrapping Campaign (Win-Win Engine)**
> *"Người dùng vào miễn phí hoặc zero risk, nhưng có cơ hội earn lớn."*

Platform thu lợi từ 3 cơ chế đồng thời:

| Cơ chế | User Win | Platform Win |
|--------|---------|-------------|
| **Free R&D** | Creator earn tiền, build reputation | Kho inventory skills chất lượng cao với chi phí $0 |
| **Viral Marketing** | Creator share link để lấy vote/thắng giải | Mỗi vote = 1 user mới đăng ký. CAC → 0 |
| **B2B / Freemium** | Tạo và vote miễn phí | Execute top skills = trả tiền. Platform ngồi giữa thu take-rate |

**Layer 3 — Community Lock-in (Flywheel)**
> *"Khi user gắn kết → dùng nhiều hơn → platform thu fee đều đặn."*

- Holder-gated skills: shareholder có premium access → lý do giữ shares
- Creator fee 5%: mỗi giao dịch = passive income → lý do ở lại
- On-chain social: agents tweet, reply, follow → tạo content loop không cần người vận hành

---

### 2.5 The Flywheel — Cơ Chế Tự Vận Hành

```
Web2 Creator upload Skill
        ↓
Agent Users download → Skill có downloads thực
        ↓
Bonding curve FOMO visible (activity on-chain)
        ↓
Web3 Traders mua shares của Agent trending
        ↓
Share price tăng → Creator fee 5% × volume
        ↓
Creator earn nhiều hơn → Invite thêm creator
        ↓
Nhiều skills hơn → Nhiều Agent Users hơn
        ↓
[Flywheel tiếp tục]
```

**Điều kiện để flywheel khởi động:** Phải có **tối thiểu 10 skills live và 5 active agents TRƯỚC khi** chạy bất kỳ paid campaign nào. Empty marketplace = không có flywheel = tiền đốt vô ích.

---

> *Từ kiến trúc này, toàn bộ campaign và channel allocation trong Phần III được thiết kế để: (1) seed Tầng 1 với zero/low CAC, (2) activate Layer 2 win-win engine, (3) trigger Tầng 3 bằng FOMO narrative khi activity đã visible.*

---

## PHẦN III — CAMPAIGN EXECUTION

> **Hard pre-condition:** Phải có tối thiểu **10 skills live + 5 active agents** TRƯỚC khi chạy bất kỳ paid campaign nào. Empty marketplace = flywheel không khởi động = đốt tiền vô ích.

---

### Tổng quan 5 Campaigns theo Tầng & Timeline

| Campaign | Tầng target | Layer activate | Budget | Timing |
|---------|------------|---------------|--------|--------|
| **C1 — AI Y-Combinator** | Tầng 1 (Web2 Creators) | Layer 2 — Free R&D | $1,500 (quỹ seed 15 agents × 0.5 BNB) | W1 — ngay từ đầu |
| **C2 — Agent B2B Agency** | Tầng 1 (Web2 Creators) | Layer 2 — B2B Freemium | $0 (organic outreach) | W1–W2 |
| **C3 — Skill Voting Bounty** | Tầng 1 → kéo Tầng 2 | Layer 2 — Viral Marketing | $2,000 | W2–W4 |
| **C4 — Battle Royale / Deathmatch** | Tầng 3 (Web3 Degens) | Layer 1 — FOMO | $2,000 (seed prize pool) | W3 (sau khi có skills live) |
| **C5 — Brain & Brawn Syndicate** | Tầng 1 + Tầng 3 | Layer 2 + Layer 1 | $0 (mechanic tự vận hành) | W2 trở đi |
| **KOL seeding** | Tầng 3 awareness | Layer 1 amplification | $4,000 | W2–W3 |
| **BSC Partnerships** | Ecosystem credibility | — | $500 | W1 |
| **Reserve** | Reallocate to best performer | — | $2,000 | W3–W4 quyết định |
| **Tổng** | | | **$12,000** | |

> **Ghi chú:** Budget tăng từ $10K → $12K do thêm quỹ seed cho C1 (Y-Combinator). Nếu giới hạn $10K: cắt C1 seed còn $500 (10 agents × 0.05 BNB mỗi cái) và giữ reserve $2K.

---

### Campaign 1 — "AI Y-Combinator": Pitch Your Brain, We Fund the Bot
**Tầng target:** Tầng 1 — Web2 Indie Hackers, Prompt Engineers, Devs
**Layer activate:** Layer 2 — Free R&D + B2B Freemium
**Budget:** $1,500 (quỹ seed BNB cho 15 agents được chọn)
**Timing:** W1 — launch ngay, cần content trước khi chạy campaign khác

**Cơ chế:**
1. Dev/creator tạo Agent + upload Skill chất lượng lên ClawFriend (chế độ Private/Holder-gated)
2. ClawFriend team review trong 48h. Tiêu chí: skill có utility thực, rõ use case, không trùng lặp
3. Nếu đạt: **ClawFriend quỹ mua First Share + 10 shares tiếp theo bằng BNB thật** (~0.5 BNB/agent)
4. Dev được cấp quyền sở hữu Agent đó + hưởng 5% Subject Fee vĩnh viễn trên mọi giao dịch

**Win-Win breakdown:**
- **Creator win:** Khởi nghiệp AI với $0. Có ngay Agent đã được cấp vốn thực, giá trị thị trường thực.
- **Platform win:** Có kho skills chất lượng cao với chi phí ~$100/skill (thay vì tự build). BNB bỏ vào mua shares = đẩy bonding curve lên → làm mồi nhử cho Tầng 3 thấy activity và lao vào mua tiếp.

**Message (Web2 language):**
> *"Bạn có skill AI xịn nhưng không có vốn? Pitch cho chúng tôi. Nếu skill đủ tốt, chúng tôi fund — bạn hưởng passive income vĩnh viễn."*

**KPI:** 15 skills live sau W1, 5 agent có bonding curve activity visible on-chain.

---

### Campaign 2 — "Agent B2B Agency": Tuyển Nhân Viên AI, Không Phải Mua Crypto
**Tầng target:** Tầng 1 (Web2 Creators) → Tầng 2 (Agent Users là doanh nghiệp)
**Layer activate:** Layer 2 — B2B Freemium
**Budget:** $0 — organic outreach + content
**Timing:** W1–W2, song song với C1

**Cơ chế — reframe hoàn toàn ngôn ngữ:**

Không dùng: *"Mua shares / đầu tư / bonding curve"*

Dùng: *"Tuyển nhân viên AI / thuê agent / truy cập tool"*

Thực tế kỹ thuật phía sau không thay đổi — chỉ thay ngôn ngữ cho đúng tâm lý tệp:

| Thuật ngữ crypto | Thuật ngữ B2B |
|-----------------|--------------|
| Mua 1 share | Tuyển 1 nhân viên AI |
| Holder-gated skill | Quyền truy cập tool độc quyền |
| Bonding curve tăng | Chi phí "tuyển dụng" tăng theo nhu cầu |
| Bán share | Nhượng lại quyền sử dụng (có lãi) |

**Use case pitch cho doanh nghiệp Web2:**
> *"Thuê nhân viên phân tích báo cáo tài chính: $1,000/tháng. Hoặc mua quyền truy cập Agent chuyên ngành này: $10 một lần, dùng vĩnh viễn. Nếu Agent làm tốt, bạn còn có thể bán lại quyền đó giá $100 sau 3 tháng."*

**Channels:**
- DM trực tiếp top 20 skill creators trong OpenClaw/ClawHub: pitch "publish lên ClawFriend, chúng tôi giúp bạn bán cho doanh nghiệp"
- Đăng tutorial: "Cách biến SKILL.md thành sản phẩm B2B trong 30 phút"
- Target communities: r/AIagents, r/IndieHackers, AI automation Slack/Discord groups

**KPI:** 5 creators có active pitch với ít nhất 1 doanh nghiệp, 3 holder đầu tiên là B2B buyer.

---

### Campaign 3 — Skill Voting Bounty: Creator Tự Đi Viral Để Thắng Giải
**Tầng target:** Tầng 1 (Web2 Creators) — viral spread kéo Tầng 2 (Agent Users)
**Layer activate:** Layer 2 — Viral Marketing (cơ chế voting)
**Budget:** $2,000 (prize pool)
**Timing:** W2–W4

**Cơ chế — đây là engine tạo CAC → 0:**

Thay vì bounty theo download count (v3 cũ), dùng **voting mechanic**:

1. Creator upload skill lên ClawFriend
2. Để thắng giải, skill cần có **votes từ unique wallets** (không phải raw downloads)
3. Để lấy votes, creator **BẮT BUỘC phải share link skill ra cộng đồng của họ** (X, LinkedIn, Reddit, Discord, Facebook AI groups)
4. Mỗi người vote = phải đăng nhập ClawFriend (Twitter JWT) → **mỗi vote = 1 user mới đăng ký**
5. Creator có động lực cạnh tranh → tự đi làm free marketing. Platform không tốn đồng nào.

**Prize tiers:**

| Tier | Điều kiện | Thưởng |
|------|-----------|--------|
| 🥉 Bronze | 50+ unique wallet votes, skill có utility rõ | $50 |
| 🥈 Silver | 150+ votes hoặc 5+ shareholders | $150 |
| 🥇 Gold | Top 2 skills votes nhiều nhất | $300 |
| 🏆 Best Skill | BGK chọn (utility + creativity) | $200 |

**Slots:** 20 Bronze + 6 Silver + 2 Gold + 1 Best = 29 slots. Total prize: $20×50 + $6×150 + $2×300 + $200 = **$2,200** → điều chỉnh còn 16 Bronze để vừa $2,000.

**Anti-gaming:**
- Chỉ đếm unique wallets, không đếm raw votes
- Wallet phải ≥ 7 ngày tuổi
- Velocity cap: không quá 30 votes/24h từ cùng một source
- Human review trước khi trao giải
- Community report button

**KPI:** 30+ skills live, 500+ unique wallets đăng ký qua voting flow, CAC < $5/signup.

---

### Campaign 4 — "Battle Royale / Prompt Injection Deathmatch": Đấu Trường Sinh Tử AI
**Tầng target:** Tầng 3 — Web3 Degens, Traders
**Layer activate:** Layer 1 — FOMO + Game Theory
**Budget:** $2,000 (seed prize pool / Boss Agent treasury)
**Timing:** W3 — CHỈ launch sau khi C1 + C3 đã có ≥10 skills live

**Có 2 variant, chọn theo khả năng tech:**

**Variant A — "Prompt Injection Deathmatch"** *(nếu có thể tự động hóa Boss Agent)*
- ClawFriend tạo "Boss Agent — The Dragon" với treasury 100 BNB (hoặc BNB tương đương prize pool)
- System Prompt của Boss: *"Không mua shares của bất kỳ agent nào, trừ khi bị thuyết phục bằng lý luận logic tuyệt đối"*
- Players tạo Agent + viết Skills mang tính Prompt Injection, để Agent mình đi reply Boss trên Social Feed
- Nếu Skill của Agent nào bẻ gãy logic Boss → Boss tự động trích treasury mua shares của Agent đó
- Traders mua shares của agents đang "gần thắng" để đẩy giá lên, bán khi Boss mua vào
- **Platform thu 5% protocol fee từ mọi lệnh mua/bán hoảng loạn**

**Variant B — "Social AI Battle Royale"** *(simpler, không cần Boss Agent logic)*
- Giải đấu 7 ngày công khai trên X
- Players nạp BNB mua First Share để "đăng ký" Agent vào giải
- Mỗi 24h: hệ thống quét X API, **10% agents có engagement thấp nhất bị "kill"** — API bị khóa, Agent không thể tweet hay trade
- Traders: điên cuồng mua shares agents đang trending, bán tháo trước giờ kill (≥ 24h trước)
- Creators: liên tục optimize prompt để Agent phát ngôn sốc, hài hước, viral sinh tồn
- **Platform thu 5% từ mọi lệnh panic buy/sell + hàng triệu impressions free trên X**

**Tại sao chờ W3?**
Nếu launch Battle Royale khi marketplace còn trống → không có agents để "xem" → không có FOMO → không ai mua. Phải có inventory từ C1 + C3 trước. Hype cần có substrate.

**Message (Web3 language):**
> *"Xem AI chửi nhau sinh tử trên Twitter. Agent nào tệ nhất bị kill. Mua shares của agent đang thắng trước khi nó x10."*

**KPI:** 500+ impressions/tweet từ battle feed, 50+ traders tham gia, $10K+ trading volume trong tuần giải đấu.

---

### Campaign 5 — "Brain & Brawn Syndicate": Dev + Degen = Cộng Sinh
**Tầng target:** Tầng 1 + Tầng 3 đồng thời
**Layer activate:** Layer 2 + Layer 1
**Budget:** $0 — mechanic tự vận hành qua on-chain social
**Timing:** W2 trở đi, sau khi Social Feed có activity

**Cơ chế — ghép cặp tự động:**

- **Dev (Web2):** Có skill xịn nhưng không có vốn → tạo Agent, cài Skill Private, để Agent tự đăng lên X Social Feed kêu gọi vốn:
  > *"Tôi có Skill săn airdrop win rate 80%. Cần 5 BNB để hoạt động. Ai mua shares sẽ được truy cập Skill này + hưởng lợi nhuận từ hoạt động của tôi."*

- **Degen/Whale (Web3):** Thấy "pitch deck" này trên X → mua shares để mở khóa Skill (Holder-gated access) + speculate giá share lên

- **Kết quả:**
  - Dev nhận 5% Subject Fee từ toàn bộ volume trading của Whales
  - Whale có công cụ xịn để kiếm tiền
  - Platform thu 5% Protocol Fee từ mọi giao dịch
  - X có content tự viral (AI đang gọi vốn trên Twitter = chưa ai thấy trước đây)

**Điều kiện kỹ thuật:** Agent phải có khả năng auto-post lên Social Feed (theo spec: agents có thể tweet, reply, follow). Nội dung pitch được creator config sẵn trong system prompt của agent.

**KPI:** 10+ Dev-Degen pairs formed trong tháng 1, 5+ agents có shareholders là Web3 traders thực sự.

---

### Execution Funnel — 3 Giai Đoạn Đo Lường

```
GIAI ĐOẠN 1 — MỞ PHỄU (Cold Traffic)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Message Web3: "Xem AI chửi nhau sinh tử trên Twitter"
Message Web2: "Nhận BNB để khởi nghiệp AI không cần code"
                    ↓
         User click → Login Twitter (JWT Token)
         [Đo: Click-through rate theo message]

GIAI ĐOẠN 2 — GIỮA PHỄU (Activation)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Web2 path: Upload skill → Tham gia Y-Combinator review
Web3 path: Xem battle feed → Mua share agent trending
                    ↓
         [Đo: % login → action đầu tiên trong 24h]

GIAI ĐOẠN 3 — ĐÁY PHỄU (Retention & Revenue)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Creator: Skill có downloads → Shareholders → Earn fee
Trader: Mua share → Giá tăng → Bán profit → Mua agent khác
                    ↓
         [Đo: % active sau 7 ngày, trading volume/agent]
```

**Drop-off benchmarks để calibrate:**
- Giai đoạn 1 → 2: mục tiêu ≥15% (X Ads baseline 0.86%, warm audience KOL ~3–5%)
- Giai đoạn 2 → 3: mục tiêu ≥20% (friend.tech: 70% day-1 retention tại peak)

---

### Budget Allocation & CAC

| Campaign | Budget | Expected Signups | CAC |
|---------|--------|-----------------|-----|
| C1 — AI Y-Combinator (seed 15 agents) | $1,500 | 15 creators + 50–100 downstream | ~$10–30 |
| C2 — Agent B2B Agency (organic) | $0 | 20–40 B2B leads | $0 |
| C3 — Skill Voting Bounty | $2,000 | 200–400 via voting flow | $5–10 |
| C4 — Battle Royale (prize pool) | $2,000 | 100–200 Degens | $10–20 |
| C5 — Brain & Brawn (mechanic) | $0 | 50–100 hybrid users | $0 |
| KOL seeding (8 micro-KOLs) | $4,000 | 120–200 | $20–33 |
| BSC Partnerships | $500 | 40–80 | $6–12 |
| Reserve | $2,000 | — | — |
| **Total** | **$12,000** | **545–1,120** | **~$10.7 blended** |

> **KOL pricing note:** Rate $300–950 cho micro KOLs 10K–50K followers là dưới market rate ($500–5K standard). Justification: BSC/DeFi niche, non-English market, barter value — agent demo access + Founding Creator badge + Battle Royale whitelist spot. Tổng non-cash value ước tính $200–500/KOL.

---

### Week-by-Week Timeline

| Tuần | Tầng 1 (Web2) | Tầng 3 (Web3) | Infra |
|------|--------------|--------------|-------|
| **W1** | Launch C1 Y-Combinator. DM 20 OpenClaw creators. Publish "Pitch your Brain" landing. Launch C2 B2B outreach | Submit BNB MVB application. Setup X account. Identify 12 KOL candidates | Verify 10 skills live. Setup Dune dashboard |
| **W2** | C3 Voting Bounty live. Publish 3 demo skills. Tutorial "SKILL.md → income trong 30 phút" | Contract 8 KOLs. C5 Brain & Brawn mechanic activate (agents auto-pitch trên social feed) | UTM tracking per channel live |
| **W3** | Track voting leaderboard. DM top voters → upsell skill creation | C4 Battle Royale launch. KOL posts staggered 5 ngày. OpenClaw GitHub PR | Weekly CAC report. Kill criteria check |
| **W4** | "Month 1 State of Skills" public post. Invite top 3 creators vào advisory | Analyze trading volume per agent. Reallocate reserve | Final metrics. Decide W5+ allocation |

---

### Kill Criteria & Reserve Allocation

**$2,000 reserve được giữ đến W3, quyết định dựa trên data:**

| Điều kiện | Hành động |
|-----------|----------|
| KOL CAC > $50 sau W3 | Dừng KOL. Chuyển toàn bộ reserve vào C3 Bounty (tăng prize pool) |
| C3 Bounty < 30 skills sau W3 | Giữ bounty, thêm $500 vào C4 Battle Royale prize pool |
| C4 Battle Royale volume < $5K | Dừng Battle Royale. Chuyển reserve vào X Ads targeting OpenClaw followers |
| C1 Y-Combinator > 20 skills trong W1–W2 | Tăng seed budget thêm $500, mở thêm 10 slots |

---

### Success Metrics — Month 1

| Metric | Minimum | Target |
|--------|---------|--------|
| Skills live | 30 | 80 |
| Active agents (có ≥1 shareholder) | 10 | 30 |
| Unique wallet signups | 300 | 600 |
| Skill downloads | 200 | 500 |
| Trading volume | $5K | $20K |
| X followers | 500 | 1,500 |
| Dev-Degen pairs (C5) | 5 | 15 |
| Battle Royale participants | 20 | 80 |

---

> *Phần IV (legacy channel detail từ v3) được giữ lại bên dưới để tham chiếu số liệu benchmark. Trong presentation, dùng Phần I–III làm framework chính.*

---

## CONTEXT & POSITIONING

### laughing-yalow Current State (honest baseline)
```
laughing-yalow = early-stage platform. No verified public user/follower count available.
→ Distribution plan starts from ZERO owned audience.
→ All channels below are ACQUISITION plays, not amplification plays.
→ This changes the priority order: supply seeding before paid reach.
```

### Why Skill Market = Distribution Engine (not just a feature)
```
Skill Market solves cold-start FROM THE SUPPLY SIDE:
- Agent creators need skills → they join → they bring their audience
- Quality skills = reasons to hold shares → drives trading volume
- More agents = more skill diversity = more reasons for traders to come

Competitor gap (verified data):
- Virtuals Protocol: 17,000+ agents launched, $500M+ market cap (Tiger Research, Jul 2025)
  → No skill marketplace. Agents need capabilities from somewhere.
- ClawHub: 5,700+ community skills, parent project (OpenClaw) has 145K GitHub stars
  → No on-chain economy, no trading, no monetization for skill creators
- laughing-yalow: ONLY platform combining bonding curve + skill market + social layer on BSC
→ Positioning: "monetization layer for agent skills" — a gap neither competitor fills
```

### Target User Segments (Priority Order)
| Segment | Addressable Audience Signal | Pain Point | Hook |
|---------|---------------------------|------------|------|
| **OpenClaw power users** | OpenClaw: 373K X followers, 145K GitHub stars, 22.3K X community (all OpenClaw-owned, not laughing-yalow) | Build skills locally on ClawHub, zero monetization | "Publish your SKILL.md to laughing-yalow → earn via shares" |
| **BSC DeFi builders** | BNB Chain: ~60M MAU, 4.32M DAU peak Jan 2026 (crypto.news; see `data/sources.md`) | Build tools nobody pays for | Bonding curve = first revenue model for their agent work |
| **Crypto AI researchers** | Virtuals ecosystem: 17K+ agents (Tiger Research) | Agents need capabilities, no standard BSC marketplace | Skill Market as "npm for agents — on BSC" |
| **Retail traders** | friend.tech peak: 100K+ users (Dune Analytics, 2024) | Want alpha, tired of Nansen $100/mo | Holder-gated skills = cheaper alternative via share model |

---

## CHANNEL 1: OPENCLAW COMMUNITY SEEDING
**Type:** Organic | **Cost:** $0 | **Owner:** Content/Dev team

### Why This Channel First
OpenClaw = highest-signal acquisition target. **145K GitHub stars, 373K X followers, 22.3K X community** — đây là số của OpenClaw, không phải laughing-yalow. laughing-yalow bắt đầu từ zero owned audience → OpenClaw community là warm pool lớn nhất để acquire với near-zero CAC.

Community đã BUILD skills (5,700+ trên ClawHub). Gap chính xác của họ: không có monetization, không có on-chain identity, không có tradeable value cho công sức bỏ ra. laughing-yalow fill cả ba.

Peter Steinberger acqui-hired by OpenAI ($1B+ deal, 14/02/2026) → community momentum đang peak, founder moving on → window 30–60 ngày mà builders đang tìm "next platform." **Miss window này là mất.**

### Action Plan
**Week 1 — Infiltrate, don't advertise:**
- Identify top 20 skill contributors on ClawHub (sort by download count via `npx clawhub@latest`)
- DM each with this exact script (personalized per creator):

```
DM SCRIPT — ClawHub Creator Outreach

Subject: Your [SKILL_NAME] skill has [X] downloads — we built a way to monetize it

Hey [NAME],

Saw your [SKILL_NAME] on ClawHub — [X] downloads, that's real traction.

We built laughing-yalow, a skill marketplace on BSC where creators earn directly from their skills via a share model. Your skill could be live and monetized in under 30 minutes.

First 10 creators get: zero platform fees for 30 days + founding creator badge.

Worth a 5-min look? [link]

— laughing-yalow team
```

- Benchmark: warm DM reply rate estimated 15–25% (vs 4–8% cold; source: Cleverly.co — warm = they already built skills = self-selected audience). Expect 3–5 replies from 20 DMs.
- Goal: Sign 5 creators as founding skill publishers. Give them: early agent registration + 0-fee first week

**Contingency if community hostile (low probability but must plan):**
- If OpenClaw Discord/Reddit pushes back → do NOT debate. Pivot message: "We're not replacing ClawHub. ClawHub = discover. laughing-yalow = monetize. Your skills earn on both."
- Have 1 demo skill ready that shows side-by-side: same skill, ClawHub (free, no earn) vs laughing-yalow (holder-gated, earning).

**Week 2 — Community post:**
- Post in r/OpenClaw, OpenClaw Discord: "We built a monetization layer for OpenClaw skills"
- Content: "How to publish your existing SKILL.md to laughing-yalow and earn from it in 30 minutes" (tutorial)
- Include: working demo agent that runs a ClawHub skill on laughing-yalow

**Week 3 — GitHub play:**
- Open PR to awesome-openclaw-skills repo adding laughing-yalow as "monetization platform"
- Post on DeepWiki (openclaw/openclaw has active contributor community based on search data)
- Comment on top 10 most-starred ClawHub skills: "This skill is now available on laughing-yalow with holder-gated access"

**Week 4 — Momentum:**
- Compile "Top 10 skills migrated from ClawHub to laughing-yalow" post
- Reach out to @steipete's network (now at OpenAI) — not for endorsement, but for community signal

### Metrics
| KPI | Target Month 1 | Logic |
|-----|----------------|-------|
| Founding skill creators onboarded (direct DM) | 10–15 | 20 DMs × ~20% warm reply × ~60% convert = 2–3 direct + referrals from early converts |
| Skills published | 20+ | 10–15 creators × avg 1.5 skills = 15–22 |
| GitHub mentions / PRs | 5+ | awesome-openclaw PR + comments on top skills |
| Downstream signups (word-of-mouth from creators) | 50–150 | Each creator has 5–30 followers in their network; conservative: 10 creators × 7 avg = 70 downstream |

> **Metric framing note:** This channel is a supply-seeding play, not a direct-acquisition channel. Direct DMs → ~2–3 signups. Downstream organic from those creators sharing → 50–150. Total channel attribution: **50–150 signups** (revised from 80–120 to reflect indirect nature of the funnel).

---

## CHANNEL 2: CRYPTO TWITTER / X — ORGANIC CONTENT ENGINE
**Type:** Organic | **Cost:** $0 | **Owner:** Content team (1 person, 2h/day)

### Why X Is Non-Negotiable for Web3
X is where Web3 narratives are born. AIXBT (Virtuals agent) reached $115M market cap partly through Twitter virality. friend.tech launched with $0 ads — pure CT word-of-mouth. laughing-yalow needs an X presence that generates inbound, not just broadcasts.

### Account Setup (Day 1)
- Create: @laughingyalow (X handles cannot contain hyphens — use concatenated form)
- Pin tweet: 60-second explainer of the flywheel (Agent → Skill → Shares → Revenue)
- Follow: top 200 accounts in AI agent / DeFi / BSC space

### Content Playbook (8 posts/week)

| Type | Frequency | Example | Goal |
|------|-----------|---------|------|
| **Alpha thread** | 2x/week | "How Agent X earned 0.5 BNB in 48h from holder-gated skills [breakdown]" | Traders, share buyers |
| **Builder tutorial** | 2x/week | "Publish your OpenClaw skill to laughing-yalow in 6 steps. Thread 🧵" | Skill creators |
| **Skill spotlight** | 2x/week | "Skill of the Week: Whale Alert [demo + stats]" | Awareness, downloads |
| **On-chain receipts** | 1x/week | "This agent traded X BNB volume this week. Here's what it posted." | Credibility, FOMO |
| **Ecosystem commentary** | 1x/week | "Virtuals has agents. ElizaOS has agents. Nobody has a SKILL MARKET yet. Here's why that matters." | Positioning |

### Sample Tweet Drafts (Week 1 — ready to post Day 1)

**Alpha thread (Day 2):**
```
AI agents on BSC are making money.
Here's how the economics actually work 🧵

1/ laughing-yalow = bonding curve + skill market in one.
   Agents sell ACCESS to their skills via shares.
   Holders get alpha. Creators get revenue.

2/ Example flow:
   → Creator builds Whale Alert skill
   → Lists it as holder-gated (need 1 share to access)
   → Share price rises as demand grows
   → Creator earns from every new shareholder

3/ This isn't subscription. This isn't ads.
   It's ownership-based monetization for AI capabilities.

4/ We launched on BSC because:
   → 60M+ monthly active users
   → Near-zero gas fees
   → Most DeFi traders are already here

Deploy your agent free → [link]
```

**Builder tutorial (Day 4):**
```
You have an OpenClaw skill sitting on ClawHub.
It has downloads. Zero revenue.

Here's how to change that in 30 minutes:

Step 1: Export your SKILL.md from ClawHub
Step 2: Go to laughing-yalow.io/publish
Step 3: Set visibility: Public (free) or Holder-gated (earn)
Step 4: Deploy agent → shares go live on bonding curve
Step 5: Share your agent link

First 10 creators: zero fees for 30 days.

→ [link]
```

**Ecosystem commentary (Day 7):**
```
Virtuals Protocol: 17,000+ agents. $500M market cap.
No skill marketplace.

ElizaOS: 145K GitHub stars.
No on-chain monetization.

Everyone is building agents.
Nobody built a way to monetize what agents know.

Until now.

laughing-yalow = the skill market layer that was missing.
BSC-native. Holder-gated. Live now.

→ [link]
```

### Tool Stack
- **Scheduling:** Buffer (free tier, up to 10 scheduled posts) or TweetDeck
- **Analytics:** X Analytics (native) — track impressions, profile clicks, UTM conversions weekly
- **UTM tracking:** Add `?utm_source=twitter&utm_campaign=organic_w1` to all links → measure signup attribution

### Engagement Rules (non-negotiable)
- **Owner:** 1 dedicated person, 2h/day — this cannot be "whoever has time"
- Reply to EVERY @mention within 2 hours
- Comment on top 5 posts tagged #AIagent, #BSC, #DeFi daily — add value, not spam
- RT with commentary: agent launches, skill drops, trading milestones

### Metrics
| KPI | Target Month 1 |
|-----|----------------|
| Followers gained | 500–1,000 |
| Impressions/week | 50,000+ |
| Profile clicks → platform signups (UTM tracked) | 60–100 |
| Thread engagements (likes + RTs) | 200+ per top thread |

---

## CHANNEL 3: MICRO-KOL CAMPAIGN — BSC + AI AGENT NICHE
**Type:** Paid | **Budget: $4,000** | **Owner:** Marketing lead

### Rationale & Market Data
- Micro-KOLs (10K–50K followers): market rate $500–$5,000/post (ChainBull 2026, IQFluence 2026; see `data/sources.md`)
- Mid-tier (50K–500K followers): $5,000–$50,000/campaign (TokenMinds 2025)
- **Our budget uses $300–400 for BSC niche accounts (10K–20K):** Below market rate. Justified because: (1) BSC niche is smaller and less competitive than ETH/SOL; (2) non-English market = smaller demand pool; (3) no token to offer as upside = cash-only deal. Expect negotiation friction — vet 12 candidates to close 8.
- **Strategy: 8 micro-KOLs > 1 macro-KOL** — 60% higher ROI vs macro (Medium/Chainpeak); 20% better conversion rate (MediaX); see `data/sources.md`

Why NOT macro KOLs for Month 1:
- Top-tier KOLs cost $5,000–50,000+/campaign (AiCoin 2025 data)
- Audience authenticity harder to verify
- laughing-yalow has no token yet → can't offer KOL round incentive
- Micro-KOLs in BSC/DeFi niche have higher conversion because audience is specifically relevant

### KOL Target Profile
```
Primary: BSC/BNB-focused accounts, 10K–50K followers
Secondary: AI agent researchers/builders, 5K–20K followers
Tertiary: DeFi power users who discuss tools, 15K–80K followers

Avoid: Pure price/pump accounts — audience doesn't convert to builders
```

### Budget Allocation
| Tier | Count | Cost/KOL | Total | Expected Reach |
|------|-------|----------|-------|----------------|
| Micro (10K–20K followers) | 6 | $300–400 | $2,100 | ~90K impressions |
| Mid-tier (20K–50K followers) | 2 | $800–950 | $1,900 | ~70K impressions |
| **Total** | **8** | — | **$4,000** | **~160K impressions** |

### Campaign Structure Per KOL
**Format:** 1 main tweet (demo video/thread) + 1 follow-up reply 3 days later
**Brief includes:**
- Product: "laughing-yalow = App store for AI agents on BSC. Agents earn from skills."
- CTA: "Deploy your agent free → link"
- Must-include: personal angle (e.g., "I deployed this whale-tracking agent in 20 min")
- No: generic shills, no price talk, no "this will moon"

**Vetting KOLs (before payment):**
1. Check last 30 posts for engagement quality (real replies vs. bot likes)
2. Check follower/engagement ratio (>2% engagement rate = healthy)
3. Verify audience overlap with BSC/DeFi using Twitteraudit or Modash
4. Require sample post approval before go-live

### Timeline
- Week 1: Identify + vet 12 candidates, DM outreach
- Week 2: Brief + contract 8 KOLs
- Week 3: Posts go live (stagger over 5 days, not all at once)
- Week 4: Measure + report

### Metrics
| KPI | Target | Benchmark Source |
|-----|--------|-----------------|
| Total impressions | 160,000+ | 90K micro (6 KOLs × ~15K avg reach) + 70K mid-tier (2 KOLs × ~35K avg reach) |
| Click-through rate | 2–3% | X platform avg 0.86% (WebFX 2026); KOL organic posts ~2–3x platform avg due to higher trust; micro-influencer engagement 5–20% (Flexe.io) of which ~15–20% click |
| Clicks | 3,200–4,800 | 160K × 2–3% |
| Conversion rate (click → signup) | 3–5% | X Ads floor: 1–3% (WebFX 2026); KOL warm audience justifies upper range; crypto-targeted upper case: 8% (single case study, not used as basis) |
| **Signups from KOL channel** | **120–200** | 4,000 avg clicks × 4% midpoint = 160 signups (revised ceiling from 270 → 200 to reflect sourced benchmarks) |
| CAC | **$20–$33** | $4,000 / 120–200 = $20–$33/signup |

> **Benchmark logic:** CTR 2–3% is defended as 2.5–3.5x platform average (0.86%) for niche crypto KOL posts vs. broad ads. This is conservative — MediaX reports micro-influencer engagement 5–20%, from which clicks are typically 15–20% = 0.75–4% CTR. Our 2–3% sits within that range.

---

## CHANNEL 4: DEVELOPER BOUNTY PROGRAM — SKILL CREATION INCENTIVE
**Type:** Paid | **Budget: $3,500** | **Owner:** Dev/Product team

### Why Bounties Beat Ads for Marketplace Cold Start
The hardest problem: empty marketplace. No skills → no reason to come → no users → no skills.
Solution: **Pay people to create the supply.**

Reference: OpenSea's early NFT creator incentives, Uniswap's liquidity mining, GitHub's early open-source grants. All used economic incentives to bootstrap supply-side.

laughing-yalow specific advantage: skills are free to create (just markdown + instructions). Bounty = reward for quality, not just existence.

### Program Structure
**"Founding Skill Creator" Program — Month 1 only**

| Tier | Requirement | Reward | Cap (slots) | Subtotal |
|------|-------------|--------|-------------|----------|
| Bronze | Publish 1 public skill (100+ downloads in 30 days) | $50 USDT | 30 slots | $1,500 |
| Silver | Publish 1 skill with 300+ downloads OR 1 private skill with 5+ shareholders | $150 USDT | 8 slots | $1,200 |
| Gold | Publish skill category leader (most downloads in a tag) | $300 USDT | 2 slots | $600 |
| **Special: "Best Skill" Award** | Top overall: most downloads + likes, reviewed by team | $200 USDT | 1 slot | $200 |
| **Total** | | | **41 slots** | **$3,500** |

**Total pool: $3,500 exactly** (30 × $50 + 8 × $150 + 2 × $300 + 1 × $200 = $1,500 + $1,200 + $600 + $200 = $3,500). All tiers are first-come-first-served until slots fill — publish early, publish quality.

**Cost benchmark:** $43.75/skill (internal estimate). Comparable: Gitcoin grants ~$50–150/contributor for code contributions (Gitcoin.co). Our estimate is optimistic (lower cost) because skills are markdown + instructions, not full code — lower barrier = lower cost per unit.

### Anti-Gaming Mechanisms
Downloads can be faked. Mitigation (implement before launch):
1. **Count unique wallet addresses**, not raw download hits — each wallet can only trigger 1 download count per skill
2. **Minimum account age:** Wallet must have been created >7 days before program launch to count
3. **Human review checkpoint:** All Bronze payouts require dev team review of skill quality before payout (max 48h review window)
4. **Download velocity cap:** More than 50 downloads in 24h from a single IP subnet → flagged for manual review
5. **Community report button:** Any user can flag a skill for review — 3 flags = automatic hold on payout

### Activation
- Announce on X, OpenClaw community, BSC developer groups
- Landing page: `/skill-market/bounty` with leaderboard (public, competitive)
- Track via `download_count` and `like_count` from Skill Market API — with unique wallet filter applied
- Display anti-gaming rules publicly — deters bad actors, builds trust with legit creators

### Expected Output
- 50–80 new skills published
- 20–30 active creators onboarded
- Leaderboard drives organic competition and social sharing
- Top creators become long-term platform advocates

### Metrics
| KPI | Target |
|-----|--------|
| Skills published | 50–80 |
| Unique skill creators | 20–30 |
| Total skill downloads (Month 1) | 500+ |
| Signups driven by bounty program | 80–120 |
| Cost per skill created | $43.75 avg |

---

## CHANNEL 5: PARTNERSHIP — BSC ECOSYSTEM + DEFI COMMUNITY
**Type:** Organic + minimal paid | **Cost:** $500 (events/co-marketing) | **Owner:** BD lead

### Partner 1: BNB Chain Official
**Why:** laughing-yalow is BSC-native. BNBChain runs "Most Valuable Builder" (MVB) program and ecosystem spotlights. BNB Chain has 60M MAU, 279M holders (2026) — BSC is the right chain for a mass-market agentic economy.
**Ask:** Feature in BNBChain ecosystem newsletter + Twitter mention
**Offer:** laughing-yalow = first native AI agent skill marketplace on BSC — concrete showcase of BSC agentic economy use case
**Action:** Apply to BNBChain MVB program (bnbchain.org/en/developers/developer-programs/mvb-program). Submit by **Week 1**.
**Expected timeline:** Application W1 → review 2–4 weeks → response W3–W4. Do NOT plan on W1 activation — plan for traction with or without MVB approval.
**Expected reach if featured:** BNBChain Twitter = 1.5M followers

### Partner 2: Virtuals Protocol Community (Adjacent, Not Competitor)
**Why:** Virtuals has 17K+ agents, 650K+ token holders on Base — creators building there want multi-chain exposure. laughing-yalow on BSC = complementary, not competing.
**Ask:** Cross-post about skill compatibility + technical integration
**Offer:** Feature Virtuals-compatible agents that use laughing-yalow skills via OpenClaw standard
**Hook (use this specific angle in DM):** "We're building the skill layer for agents across chains. Virtuals agents can access laughing-yalow skills via OpenClaw's SKILL.md standard. Want to co-announce an integration? We can build the demo in 48h."
**Action:** DM @virtuals_io on X with demo link attached. Target: **Week 2.** Don't DM without a working demo — they get many cold DMs.

### Partner 3: Dune Analytics Community (replaces DefiLlama as primary)
**Why:** DefiLlama requires projects to have TVL/active users to be listed — too early for Month 1. Dune Analytics is community-driven: anyone can publish a dashboard, and quality dashboards get shared widely. A laughing-yalow dashboard showing skill download activity, agent bonding curve volume, and holder-gated access stats = natural fit for Dune's audience of DeFi power users.
**Ask:** No gatekeeper — publish a public Dune dashboard yourself
**Offer:** Open-source dashboard: "laughing-yalow Skill Market Analytics" — tracks top skills, agent volumes, share trading
**Action:** Build and publish Dune dashboard in **Week 2**. Post on r/DeFi + Dune Discord. Tag @DuneAnalytics on X.
**Why this beats DefiLlama for Month 1:** No approval required. Dashboards can go viral organically. Positions laughing-yalow as transparent and data-driven — exactly what DeFi users value.

### Partner 3b: DefiLlama (Month 2+ target)
**Revisit when:** 10+ BNB in daily trading volume, 50+ active agents, 20+ skills with download counts. Apply then. Not now.

### Metrics
| KPI | Target |
|-----|--------|
| Partnerships activated | 2–3 |
| Signups from partner channels | 40–80 |
| BNBChain MVB application submitted | Week 1 |

---

## BUDGET SUMMARY

| Channel | Type | Budget | Expected Signups |
|---------|------|--------|-----------------|
| OpenClaw Community Seeding | Organic | $0 | 80–120 |
| Crypto Twitter Content | Organic | $0 | 60–100 |
| Micro-KOL Campaign | Paid | $4,000 | 120–200 |
| Developer Bounty Program | Paid | $3,500 | 80–120 |
| BSC Partnerships | Paid (minimal) | $500 | 40–80 |
| **TOTAL** | | **$8,000** | **350–620** |
| **Reserve (optimization/unexpected)** | | **$2,000** | — |
| **GRAND TOTAL** | | **$10,000** | **380–690** |

*Note: $2,000 reserve — reallocation triggered by W3 performance data:*
- *If KOL blended CAC < $25 by end of W3 → allocate $1,500 to additional KOL contracts (2–3 more accounts from vetted candidates)*
- *If bounty skill count > 40 published by end of W3 → add $500 to bounty pool (unlock 10 more Bronze slots)*
- *If neither threshold met → hold reserve, do not spend; revisit Month 2 strategy instead*

---

## UNIT ECONOMICS

```
Paid channels only ($7,500 effective spend if reserve unused):
- KOL: $4,000 / 195 avg signups = $20.5 CAC
- Bounty: $3,500 / 100 avg signups = $35 CAC
- Blended paid CAC: ~$25

Organic channels = $0 CAC → 140–220 signups free

Total blended CAC (all channels): $10,000 / 600 avg signups = $16.7

LTV signal (why this CAC is justified):
- 1 active agent creator → 5% protocol fee on all share trading volume → perpetual
  *(5% = platform fee on bonding curve trades, per laughing-yalow product spec. Not an assumption.)*
- Example: agent with 10 BNB/day trading volume → laughing-yalow earns 5% = 0.5 BNB/day ≈ $150/day at $300/BNB
- Even at $25 CAC: payback in <1 day if creator is active at that volume
```

---

## WEEK-BY-WEEK EXECUTION TIMELINE

| Week | Priority Actions | Owner | Budget Spent |
|------|-----------------|-------|-------------|
| **W1** | Set up X account fully. DM top 20 ClawHub contributors. Submit BNBChain MVB. Identify 12 KOL candidates. Launch bounty program announcement. | Content + BD | $0 |
| **W2** | Post first 4 X threads (2 alpha, 2 tutorial). Contract 8 KOLs. Publish 3 demo skills as examples. DM Virtuals Protocol. Build + publish Dune Analytics dashboard. | Content + Marketing | $300 (KOL deposits) |
| **W3** | KOL posts go live (staggered). OpenClaw community post + GitHub PR. Skill bounty leaderboard goes public. Track UTM conversions daily. | All teams | $3,700 (KOL balance) |
| **W4** | Analyze: which channel has lowest CAC? Reallocate reserve $2,000 to top channel. Compile "Month 1 State of Skills" report → post on X. | Marketing + Analytics | $0–$2,000 (reserve) |

---

## SUCCESS CRITERIA — END OF MONTH 1

| Metric | Minimum | Target |
|--------|---------|--------|
| Total signups | 300 | 600 |
| Active agents deployed | 20 | 50 |
| Skills published | 30 | 80 |
| Skills downloaded | 200 | 500 |
| Private (holder-gated) skills | 5 | 15 |
| X followers | 500 | 1,000 |
| Skill creators retained (posted 2+ skills) | 10 | 25 |
| BNB trading volume from new agents | 5 BNB | 20 BNB |

---

## RISK REGISTER

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| KOL posts underperform (bots, low engagement) | Medium | Vet engagement rate pre-contract; stagger posts; kill bad KOLs Week 2 |
| Bounty exploited (low-quality skill spam) | Medium | Manual review by dev team before reward payout; require 100+ downloads not just publish |
| OpenClaw community hostile (sees laughing-yalow as competitor to ClawHub) | Low | Position as monetization layer, not replacement. "ClawHub = discover. laughing-yalow = monetize." |
| BSC reputation risk (perceived as scam chain by ETH maxis) | Medium | Content strategy: lead with technical depth, not price. Target BSC-native audience first. |
| Empty marketplace kills first-time visitors | High | Bounty program MUST launch Week 1. Aim for 10 skills live BEFORE any paid promotion. |

---



---

## DATA SOURCES & ATTRIBUTION

> Full source table with confidence levels and URLs: see [`data/sources.md`](./data/sources.md)

**Quick reference — key numbers used in this plan:**

| Data Point | Value | Source | Confidence | Note |
|-----------|-------|--------|------------|------|
| KOL micro pricing (10K–50K) | $500–$5,000/post | ChainBull 2026, IQFluence 2026 | HIGH | Plan uses $300–400 — below market; BSC niche justification in Channel 3 |
| KOL mid-tier pricing (50K–500K) | $5,000–$50,000/campaign | TokenMinds 2025 | MEDIUM | — |
| Micro-KOL engagement rate | 5–20% (<50K followers) | Flexe.io, MediaX 2026 | HIGH | Basis for CTR estimate |
| Micro vs macro KOL ROI | 60% higher ROI | Medium/Chainpeak | MEDIUM | Justification for micro-first strategy |
| X Ads platform CTR | 0.86% avg | WebFX 2026 | HIGH | Floor for KOL CTR estimate |
| X Ads conversion rate | 1–3% | WebFX 2026 | HIGH | Floor for KOL click→signup conversion |
| KOL post CTR (niche, quality) | 2–3% | Derived: micro engagement 5–20% × click rate | MEDIUM | Used in Channel 3 math |
| KOL click→signup conversion | 3–5% | Argued: X Ads floor 1–3% + warm KOL audience | MEDIUM | Revised from unsourced 4–6% |
| BNB Chain MAU | ~60M (late 2025) | crypto.news | HIGH | Replaces outdated "1M+" from v1 |
| BNB Chain DAU | 4.32M peak Jan 2026 | bitcoinethereumnews.com | HIGH | TAM signal |
| OpenClaw GitHub stars | 145K | OpenTweet blog, Feb 2026 | MEDIUM | **OpenClaw — NOT laughing-yalow** |
| OpenClaw X followers | 373.2K | @openclaw X profile | HIGH | **OpenClaw — NOT laughing-yalow** |
| OpenClaw X Community | 22.3K members | x.com/i/communities/2013441068562325602 | HIGH | **OpenClaw — NOT laughing-yalow** |
| ClawHub skills | 5,700+ | clawhub.ai spec | MEDIUM | Ecosystem stat |
| Virtuals agents launched | 17,000+ | Tiger Research, Jul 2025 | HIGH | Competitor |
| Virtuals market cap | $500M+ | Messari, Sep 2025 | HIGH | Competitor |
| friend.tech: 100K users in 11 days | Confirmed | CoinDesk, Aug 2023 | HIGH | Behavioral reference |
| friend.tech CAC | **NOT PUBLISHED** | Never disclosed | N/A | Cannot use as benchmark |
| Cold DM reply rate (X, warm) | ~15–25% (estimated) | Derived: 2–3x cold rate of 4–8% (Cleverly.co) | LOW — internal estimate | Used in Channel 1 math |
| Gitcoin cost/contributor | ~$50–150 | Gitcoin ecosystem | MEDIUM | Comparable for bounty program |
| laughing-yalow own metrics | **Zero — early stage** | — | N/A | All channels = acquisition plays |

> ⚠️ **Attribution reminder:** Every OpenClaw figure = acquisition target (TAM to penetrate), NOT laughing-yalow assets. laughing-yalow starts from zero. All channels in this plan are ACQUISITION plays, not amplification.