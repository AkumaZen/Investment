# Approved plan (source of truth)

Everything below the line is the user's approved plan exactly as they pasted it on Sat, 07 Nov 2026: nothing summarised, moved or reworded. Every decision in it, however small, must stay in the skill. If SKILL.md, an asset or a script disagrees with this file, this file wins unless a later row in `learnings.md` records the user changing it. `scripts/check_skill.py` checks that this file is still complete (it must keep every heading and fine-grained line, and must not be compressed again) and that the key decisions reach the working files.

Known later changes by the user (also recorded in learnings.md). These are the only differences allowed between this plan and the working files:
- Tue, 10 Nov 2026, latest context instruction: the user declined compaction. Do not initiate optional/manual compaction or configure a custom automatic threshold. Retain file-based milestone checkpoints, original documents and full QA; built-in runtime context management remains unchanged. This supersedes earlier optional compaction suggestions.
- Tue, 10 Nov 2026, latest model amendment: user approved GPT-6 Luna low for routine extraction/indexing with medium retained for analytical work, ambiguity and final review. This supersedes the earlier all-workers-medium assignment; fork_turns none and full document/QA scope remain. Milestone and approximately 50% measured-context checkpoints preserve recovery state; no runtime compaction threshold has been changed.
- Tue, 10 Nov 2026: user approved the complete efficient-execution proposal after Amanta: keep document coverage and analytical/QA gates; cache full page extracts and completed hash-matched readings; maintain evidence/guidance registers and one canonical model; use compact Luna/medium handoffs and checkpoints; include official product photos, visible PDF navigation and reference-based density in the first build; use one reproducible pipeline and scoped cosmetic revisions, followed by every-page final PDF review. Standing default becomes latest annual report, all historical calls/decks, latest results, material announcements, applicable RHP and uploads; do not repeat document-choice questions already answered by that scope. This supersedes fresh worker-per-file and narrower default-set mechanics only. Read learnings/concepts/research-report-efficient-execution.md from the repository root; the original approved plan body below remains unchanged.
- Draft for review, 07 Nov 2026, reference-design amendment: the user asked this package to refer to the supplied PDF manual, Markdown manual and agent JSON instead of pasting them into the skill. The draft working files use their report architecture, typography, analysis-depth and page-review process in place of the historical neo-brutalist styling, boxed notes and fixed chart quota. This is the only new supersession; research scope, source workflow, models, section order, core coverage and valuation rules remain. This draft is not installed or approved until the user verifies it.
- Sat, 07 Nov 2026: step 2 now asks which documents to use before any worker reads (the plan below says "The skill never stops for permission").
- Sat, 07 Nov 2026: the user said to ignore `equity-research-html-studio` (it is not public and not on this machine). It is dropped from the external skills; the others stay.
- Sat, 07 Nov 2026: the user said to use the `dataviz` library for chart decision making in place of equity-research-html-studio. dataviz is loaded with the Skill tool before the visual plan (builder) and before the first chart (research run), and its anti-patterns.md is the chart critique step.
- Tue, 10 Nov 2026: valuation modelling follows the `business-valuation-scenarios` skill, Steps 1 to 4, by reference. The bull case becomes guidance realised faster or better from disclosed triggers (the skill's Step 2), in place of "same earnings at a higher multiple" in the valuation rules below.
- Path on this machine is `C:\Users\RNEGI\.claude\skills\research-prompt-builder\` (the plan was written on a machine with `C:\Users\Rohit Negi\`).
- The user's request that came with the plan: install all the skills this skill needs, read them, and ask clarifying questions before building.

- Tue, 10 Nov 2026: user requested all reader, financial-scanner and evidence-verifier workers use gpt-6-luna with medium reasoning effort and fork_turns none. This supersedes earlier worker model assignments; completed-run records remain unchanged.

---

# Plan: `research-prompt-builder` skill

## Context

You have asked for a company research prompt 7 times in this session: Suven, Savita, Kabra, SEDEMAC, Ellenbarrie, Anlon and Restaurant Brands Asia.
Each time the structure was rebuilt by hand, and you had to correct the same things again.
The skill makes that repeatable.
You name a company, and optionally upload documents.
It reads the documents, works out what actually matters in that business, and writes a finished prompt to `Desktop\Investment\Research Prompts\`.

The skill stops at the prompt.
Building the report stays a separate step, as it is today.

## What the session history shows

**The format settled over time.**
The older prompts (Balu, Suven, Savita, Kabra) have 12 sections, with leads marked UNVERIFIED.
From SEDEMAC and Ellenbarrie onward they became `0. How to think` to `9. Final reply`, with facts verified first.
Anlon and RBA are the mature form, so they are the base template.
RBA and Anlon share the same skeleton, and sections 7-9 differ only in these lines:
- the accent mapping
- the tag list
- the diagrams
- the must-have charts
- the final-reply finding

**The base template gets stronger material from the other prompts.**
- SEDEMAC has the deepest business and product work: "Part A: Understand the business (at least half the report)", a product grid and product cards.
- Balu, Savita, Suven and Kabra have the deepest management work: bios, incentives and hard red flags, and Balu adds tone per call.
- The older prompts also have useful modules: catalyst scoring, the price move map, the concall checklist, the forensic first pass, the metrics checklist. SEDEMAC adds the "leave out" list.
- Their structures differ by company: Kabra leads with "what broke", Suven with cash and the pipeline, SEDEMAC with products.

**Your requests, which become rules:**

| Your words (date) | Rule in the skill |
|---|---|
| "Great Research analyst... explains the business and it's products flawlessly... acting like a robot" (04-Oct) | Read the documents before writing. Business and every product come first, then peers, then numbers. Add material topics without being asked |
| "avoid sections which are not related" (04-Oct), "sections which are irrelavant" (02-Oct) | Sections are chosen for the business. Anything dropped is named with a reason |
| Types, what's new, capacity, utilisation, capex (04-Oct) | Always covered wherever the business has them |
| The 10-point framework, "think bottom-up, question every narrative" (06-Oct) | The 10 rules stay in every prompt, reworded for the company |
| "simple and easy to digest" (06-Oct) | Simple words, and terms are explained before they are used |
| "only use one annual report, all the important annoucements only", RHP, regulator databases (23-Oct) | Default: a fixed document set, plus company-specific primary checks. If you say to use all documents, the skill uses all documents and important announcements, together with anything you uploaded |
| Concall downloader, then Screener if it fails (26-Sep, 23-Oct) | The generated prompt runs the downloader once, then falls back to Screener |
| The design block (04-Oct, 23-Oct) and visual verification (06-Oct) | Sections 7 and 8 are locked text |
| "why to read this business?" (24-Oct), the semiconductor trigger "was my first goal to find the company" (09-Oct) | Every prompt opens with why we are covering this business |

**Things you had to ask for after the report was built, which the prompt should now cover up front** (seeded into `reference/learnings.md`):

| You asked | Prompt must force |
|---|---|
| "what is the moat for Kabra in battery? anyone can do that" | Moat tested against who else can do it, with a counter-point |
| "who are the actual customers? is this the only company" | Named customers, what each buys, and all competitors |
| "Products also be discussed in detail", "types and which types they make", "what are they brining new" | Product grid, product cards, what's-new timeline |
| "production capacity, utilisation, new capex" and "Exisiting capaicty, New Capacity Live, Planned capacity" | A three-way capacity table |
| "what is take and pay... will it benefit or not" | Every contract term explained, with who benefits |
| "margins for Merchant vs Onsite" | Margin by business model, with assumptions marked in brackets |
| "only gives plants, then what about recurring revenue... this model is not good" | One-time vs recurring revenue, and a judgement on model quality |
| "why did BHEL gave this massive order, what is happening inside BHEL" | Why the big customer is buying, and whether it repeats |
| "where is the money going in investments" | Where all the cash sits and goes |
| "Has shares really pleged by management?" | Pledge checked in primary filings, and the claim marked Verified or Not found |
| "Why is solar cell trigger not mentioned and management talks about solar cell" | Everything management talks about, whether or not it is in the numbers yet |
| "what things are assumed and what are actually grounded?", "show the calculation" | Assumed vs grounded list, with the working shown for every estimate |
| "we cannot value this based on it's past earnings" (Suven) | Valuation method follows the business, on the asset when there are no earnings yet |
| "how many actually patients were happy", "lot of jargon" (Suven) | Phase-wise evidence in plain tables, and no unexplained terms |
| "Tell about that minear and europe company... what is the relation" (Anlon) | Every named partner: relation, status, what is unverified |
| "list of approvals... how it matches the management guiding 70%" (Anlon) | Approvals held vs applied for, tested against guidance; exports and order book traced across calls |
| "Use their website" (Anlon) | Company website product list and brochures used as sources |
| "use this valuation", management's guidance unchanged (Anlon) | A table of management's guidance with no haircut and a Source column |
| "key trackables consolidated on one page", "Mention the triggers on the first" | One page of trackables and dated triggers near the start |
| "scroll is not working", "I want a light mode theme" (Anlon) | Scroll check and light theme as default |
| "Still this report does not explain capex properly" (Ellenbarrie) | Project-by-project capex tracker, with funding and return on past capex |
| "What is expected in the next quarter according to the management" (24-Oct), the Q1FY27 outlook questions on Anlon and Amanta | Current guidance table and a next-quarter outlook in management's words |
| "future derived growth" (Savita), "Semiconductor trigger is currently not there" (Ellenbarrie) | Growth built by driver, and a full trigger table that also says which expected triggers are absent |
| "this model is not good then" (Ellenbarrie) | The anti-thesis, argued with real numbers |

## Default prompt skeleton

Every prompt starts from this structure, stored in `assets/skeleton.txt`.
The agent fills it for the company and can override it when the business calls for that, as described under "Override rules" and "How the structure adapts".

**Header box:** company, research type, NSE and BSE codes, lead analyst, output format.

| Section | Default content |
|---|---|
| **0A. Why we are covering this business** | See below. Always first |
| **0B. How to think** | What the company is and the real job of the research ("the job is NOT to retell..."); the 10 rules; 15 questions; one connecting-the-dots example with real numbers |
| **1. What we already know** | Local files and fact pack; business; multi-year and quarterly trends; latest quarter by segment; balance sheet and cash; capital and control; guidance quotes with speaker; data conflicts; "To find" list |
| **2. Tools and sources** | Document mode and set; local files first; concall downloader once; Screener tools; important-announcements list; primary checks; what is not allowed; citation rule |
| **3. Working method** | Research folder, steps [0] to [6], `state.md` updated after each step, run to completion, Sonnet 5.5 workers read and Opus decides |
| **4. Report structure** | The default sections below, then the coverage map and the "leave out" list. Each section: the answer in one bold line, the evidence, then "What this means for you" |
| **5. Valuation** | Share count including dilution; main metric and cross-check, with the reason; how revenue is built bottom-up; management-guidance row with Source column; bear, base and bull marked `[E]`; reverse check of today's price; rating bands |
| **6. Writing, design, checks** | Simple words; answer first; units and tags on every number; re-check 10 random numbers against source pages; model maths re-run by script |
| **6A. Visual intelligence (added)** | The visual thinking rules, plus a company-specific visual plan. See "Visual intelligence" below |
| **7. Design system** | Locked neo-brutalist block; only the accent mapping, tags, diagrams and must-have charts change |
| **8. Visual verification** | Locked checklist: desktop, mobile, console, interaction, print, plus scroll |
| **8B. Visual quality review (added)** | Your 12 extra checks and the final review as analyst and report designer. Section 8 stays as it is |
| **9. Final reply** | Rating, value range vs price, 3 key findings, checks with results, known gaps, disclaimer, progress line |

### 0A. Why we are covering this business

Written from the documents in plain words, in under 15 lines:
- **What it is**, in two sentences a first-time investor can follow.
- **Why it caught our attention:** your own reason if you gave one, otherwise the specific number or event in the filings.
- **Why now:** what changed recently, with dates.
- **The core debate:** the one question that decides whether this is worth owning.
- **What the market seems to believe**, from the price vs the numbers.
- **What would make us care, and what would make us drop it.**
- **What the reader will be able to decide** after reading.

### The 10 rules in 0B

Your framework, reworded for the company:
1. Start simple: what it makes, who buys it, how it earns money.
2. Explain every technical term before using it.
3. Split the business into segments or entities.
4. Go product by product.
5. Separate quantity from quality (the company-specific version, such as organic vs acquired or same-store vs new-store).
6. Separate profit from cash.
7. Separate reality from optionality.
8. Check every management promise against what happened.
9. Follow the causal chain and mark the first unproven link.
10. Never fill gaps with assumptions: Disclosed, Inferred or Not Disclosed.

### Default report sections in section 4

The original S1-S14 stay. S1 and capacity are expanded, and these sections are added: customers and partners, moat, management analysis, guidance and outlook, future growth and triggers, and risks and anti-thesis.
Parts A to E follow SEDEMAC's rule that understanding the business takes at least half the report.

| # | Section | Answers |
|---|---|---|
| | **Part A: understand the business** | |
| S1 | Why read this business, and snapshot | The 0A answer with evidence; what it does, latest numbers, price, diluted shares, rating, value range; one page of key trackables and dated triggers |
| S2 | The business, simply | Depth checklist below |
| S3 | Products | Depth checklist below |
| S4 | Segments and entities | Revenue and margin for each part; which part earns and which part loses; margin by business model |
| S5 | Customers and partners (added) | Named customers and what each buys, concentration, why they buy, what is happening inside the biggest customer, whether large orders repeat, contract terms, every named partner with status |
| S6 | Moat and competition (added) | Who else can do this, per product; moat cards each with evidence and a counter-point; switching costs; a plain answer to "can anyone do this?" |
| S7 | Quantity vs quality | Rule 5 for this company, such as organic vs acquired growth |
| S8 | Company-specific deep dive | The biggest question for this company, such as a share swap, control change or clinical data |
| S9 | Capability, capacity and capex (expanded) | Depth checklist below |
| | **Part B: management** | |
| S10 | Management analysis (added) | Depth checklist below, ending in OK, WATCH or RED |
| S11 | Management claims checked | Claim, date, speaker, what happened, status, credibility in one line |
| | **Part C: the future** | |
| S12 | Guidance and outlook (added) | Depth checklist below, including what management expects next quarter |
| S13 | Future growth and triggers (added) | Depth checklist below |
| | **Part D: proof** | |
| S14 | Peers, granularly | Business comparison first (who can do what, how close), then numbers; where it can and can't compete; whether it deserves a higher or lower multiple |
| S15 | Reality vs optionality | Earning today, ramping, announced and idea, with ₹ in each |
| S16 | The causal chain | One row per growth driver, proven or unproven at each link |
| S17 | Financials and quality of earnings | P&L, cash vs profit, working capital, debt, share count, sector metrics; OK, WATCH or RED |
| S18 | Governance and filings | Material filings in date order, promoters, related parties, auditor, rating, data conflicts |
| | **Part E: risks, value and verdict** | |
| S19 | Risks and anti-thesis (added) | Depth checklist below |
| S20 | Valuation and verdict | Bear, base and bull; bull vs bear side by side; the 15 questions in one line each; assumed vs grounded list; dated signals to watch |
| Appendix | Sources | All sources with links; Disclosed, Inferred and Not Disclosed list for key numbers |

### Depth checklist: S2, business understanding

- An everyday picture of what it does, and how the money is made step by step.
- The revenue equation, such as units x price or stores x sales per day x 365.
- What happens to ₹100 of sales: costs, what is left and what is kept as cash.
- Revenue model: product, project, recurring or service; one-time vs repeat; and a plain judgement on model quality.
- Every contract term explained, with who benefits (take-or-pay, royalty, pass-through).
- Value chain diagram and history in 5-6 milestones.
- End markets and demand drivers, each mapped to this company's revenue. Figures from the company are labelled company-provided.
- Growth derived from real drivers and capped by capacity and balance sheet, not quoted.
- Glossary box.

### Depth checklist: S3, product understanding

- **Type grid:** type x application x technology, each marked MAKES AND SELLS, FIRST ORDERS, IN DEVELOPMENT, DOES NOT MAKE or NOT DISCLOSED.
- **One card per product:**
  - what it is, the problem it solves and what it replaces
  - where it is used and who buys it
  - the technology and why it is hard to copy
  - stage and approvals held vs applied for
  - size today and room to grow
  - competitors and how it differs
  - margin and how it makes money
  - what could go wrong
  - a real image from the deck or website
- **What's new:** past, now and next 2 years, each with date, status and firm orders vs "likely".
- **Biggest product threat:** the one question that matters, such as EV for petrol parts.

Sector versions follow the same depth: stores, formats and menu for a restaurant chain; molecule cards with plain phase tables and evidence grades for a biotech; service lines for a services company.

### Depth checklist: S10, management analysis

- **Who they are:** founders, KMP and board; background and tenure from filings; succession and key-person risk; independence of the board.
- **Skin in the game:** holding trend, who sold and at what price, preferential or warrant participation, pledges checked in primary filings, pay vs profit, ESOPs.
- **Capital allocation:** every rupee raised and where it went vs the stated plan, acquisitions and the returns on them, unrelated ventures, where the cash sits today, dividends and buybacks.
- **Do they deliver?** Links to S11, with a credibility score as % met. An annual-report-only company gets a statements register instead, as in Kabra, and a biotech gets a timeline tracker, as in Suven.
- **How they communicate:** tone per call (BULLISH, CAUTIOUSLY OPTIMISTIC, NEUTRAL, CAUTIOUS or DEFENSIVE), guidance direction across calls, what they repeat and what they stop mentioning, how they answer hard analyst questions (verbatim, with speakers), and what they talk about that isn't yet in the numbers.
- **Fair to minorities?** Related parties, promoter-linked deals, valuation reports, disclosure quality, auditor remarks, ratings, litigation.
- **Hard red flags:** qualified audit, going-concern language, rising pledge, deviation in use of proceeds, loans to promoter entities, active investigation, repeated guidance misses.
- **Verdict:** OK, WATCH or RED, with one line of reasoning. A RED caps the rating.

### Depth checklist: S9, capacity and capex

- **Capacity table:** existing, live now and planned, with utilisation and when the next plant is needed.
- **Capex tracker, one row per project (from Balu):** project, type (maintenance or growth), status, cost, spent so far, funding (internal, debt or equity), commissioning date and any slippage, capacity added, expected revenue and margin impact, risk, source.
- **Promised vs actual:** every date and cost first given, later changes, and what happened.
- **Did past capex earn anything?** Revenue and return on each rupee spent; asset turnover before and after.
- **Can it be paid for?** Capex vs operating cash flow vs depreciation, and whether more debt or equity is needed.

Sector versions: store capex and payback for a chain, R&D centre and trial spend for a biotech, and capitalised R&D where relevant.

### Depth checklist: S12, guidance and outlook

- **Current guidance table:** metric, number or range, period, speaker, verbatim quote, source. Covers revenue, margin, PAT, volume, capex, order book, exports and new products.
- **Next quarter:** what management expects, in their words. If they gave no number, the report says so instead of inferring one.
- **Direction across calls:** first given, later changes, current; guidance marked raised, held or cut (from Balu).
- **What must be true:** the growth and margin the remaining quarters need for guidance to hold, such as what H2 must deliver.
- **Conflicts:** deck vs call, and analyst claims never presented as guidance. Broker numbers stay out, as in Balu.
- **No guidance:** said plainly, as in RBA, with the statements register used for an annual-report-only company.

S11 checks past promises, and S12 sets out what is promised now. Together they feed the management-guidance row in valuation.

### Depth checklist: S13, future growth and triggers

- **Growth build by driver:** each driver sized bottom-up (such as stores x sales, or capacity x utilisation x price) for the next 3 years and capped by capacity and balance sheet. Derived, not quoted (your Savita request).
- **Trigger table (from Balu, Savita, Suven, Kabra):** catalyst, timing, what management said, ₹ impact, bias, Confirmed or Probable, source.
- **Strength rating:** STRONG only if it appears in 2 or more primary filings with numbers and a date. Otherwise MODERATE or WEAK.
- **All triggers listed:** including what management talks about but isn't yet in the numbers, sector or government moves, and anything you raised. If a trigger you expected isn't there, the report says so (your Ellenbarrie solar and semiconductor questions).
- **Near-term vs long-term:** the next 2 quarters kept separate from the next 2-3 years.
- **Trigger dates:** results, commissioning, approvals, warrant deadlines, each with what would confirm or break it.

Catalyst scoring stays an optional module on top of this table.

### Depth checklist: S19, risks and anti-thesis

- **Anti-thesis:** the strongest case against owning this stock, written as a sceptic would argue it, with real numbers. It is not a list of generic risks.
- **Bull claim vs rebuttal:** each main bull point, the best counter-evidence, and which side the evidence favours today.
- **What if we are wrong?** The failure story: if the stock halves in 2 years, what most likely caused it?
- **Risk cards, 6-8 ranked (from Balu, Savita, Suven, Kabra):** specific and falsifiable, each with likely ₹ or per-share impact, and a "signal that confirms it" with a threshold, such as debtor days above 150.
- **Link to value:** the bear case in valuation must be built from these risks, and the signals feed the dated watch list.
- **What would change our mind:** the evidence that would kill the anti-thesis, and the evidence that would kill the thesis.

### Override rules

- **Locked, never overridden:** section order 0-9, 0A first, the 10 rules, the 15 questions, the citation rule, sections 7 and 8, Business and Products before peers and numbers, Management, capex, guidance, growth triggers and the anti-thesis always covered, and Valuation and verdict last.
- **Rename:** S3 can become "Pipeline" or "Formats and menu" to suit the business.
- **Swap:** a default section is replaced when it doesn't fit. A pre-revenue biotech replaces S9 capacity with phase-wise trial tables and cash runway; an annual-report-only company replaces S11 with a statements register, as in Kabra.
- **Add:** extra deep dives are allowed when material. RBA used control change and Indonesia.
- **Drop:** a section can go if it truly doesn't apply. The agent names it and gives the reason in the leave-out list.
- **Concise mode:** merges default sections rather than deleting analysis (for example S7 into S4, and S16 into S15), keeps sections 0-9 and keeps 0A, Business, Products, Management, capex, guidance, growth triggers and the anti-thesis. Targets 13-20 KB.
- **Your instructions win:** anything you ask for, including a section list, overrides the default and the playbook.

### How the structure adapts

The default above is the starting point.
The agent diagnoses three things in `playbooks.md` and rearranges the report to fit:

| Axis | Examples from your prompts | What it changes |
|---|---|---|
| **Business model** | Stores (RBA), plants and contracts (Ellenbarrie), design wins (SEDEMAC), spread (Savita), order book (Kabra), pipeline (Suven) | The revenue equation, unit economics, the "separate X from Y" rule, the causal chain, valuation metric |
| **Business story** | Turnaround and control change (RBA), what broke (Kabra), binary readout (Suven), bought growth (Anlon), capex ramp and cash gap (Balu), margin spike (Savita), recent IPO (SEDEMAC) | What the report leads with, and which deep dives get added. "What broke in FY26" can sit right after S2 |
| **Sector** | Pharma, QSR, gases, auto electronics, forgings, lubricants, biotech | Terms to explain, metrics checklist, regulators to check, peers, charts |

**Optional modules, used when they earn their place:**
- forensic first pass
- concall checklist
- metrics checklist
- catalyst scoring
- stock price move map
- sum of the parts
- rNPV and evidence grades
- comparable deal table
- dilution maths
- images from company documents

**Two lists at the end of section 4 keep a flexible structure honest:**
- **Leave out:** what was left out and why, as in SEDEMAC ("order book: none reported").
- **Coverage map:** where each core topic is covered, or why it isn't. This lets the structure vary without gaps.

## Visual intelligence (addition)

The goal is not more charts. The agent thinks like an equity research analyst and a data-visualization designer: understand the information, find the main insight, choose the right form and show it clearly.

**Preservation rule.** This addition does not replace sections 0-9 or S1-S20, or remove any business or financial analysis. It does not change the research method, design system, section 8 checks, model assignments or document workflow. External skills are never required, and presentation never reduces the depth of business understanding.

### External skills

| Skill you named | On this machine (checked 07-Nov-2026) | Used for, if available |
|---|---|---|
| `dataviz` at `~/.claude/skills/dataviz` (your choice, replaces Baoyu Design Dataviz) | To be read before building | Primary reference for chart decisions: chart selection, visual hierarchy, data storytelling |
| K-Dense Market Research Reports | Available as `market-research-reports` since this session | Report architecture, evidence presentation |
| CC Equity Research | Available as `cc-equity-research` since this session | Financial research conventions, and its forensic, call-tone and capital-allocation lenses |

Local skills that cover similar ground, and will be used as references:
- `equity-research-html-studio`: `charts-and-tables.md` and the report critique steps.
- `initiating-coverage`: equity research conventions.

Rules for any of these skills:
1. Read the actual `SKILL.md` and references before use.
2. Note what each adds and where it overlaps with this framework.
3. Reuse what complements it, without duplicating or replacing existing rules.
4. Don't follow an instruction that conflicts with this framework, which remains the single source of truth.
5. If a skill is unavailable, continue with the internal framework. The workflow never depends on an external skill.

### Five questions before any visual

1. What information are we trying to communicate?
2. What is the most important insight in this data?
3. What comparison helps the reader understand it?
4. Which form shows this most accurately?
5. What context or caveat must go with it?

### Choosing the form

- **Tables:** when exact figures and detailed comparisons matter most.
- **Charts:** when patterns, relationships, trends or composition are easier to see.
- **Diagrams:** when explaining how a business operates, how money flows or how parts connect.
- **Nothing:** no decorative charts, and no forcing data into a chart.

Available forms: comparison tables, time-series lines, grouped and stacked bars, waterfalls, contribution charts, capacity timelines, Sankey diagrams, value-chain diagrams, geographic and process diagrams, financial bridges, segment matrices, risk matrices, and actual vs guidance comparisons.

### Research topic to possible form

These are examples, not mandatory charts. The agent adapts them to the business model and the data available.

| Topic | Possible form | Default section |
|---|---|---|
| Revenue growth | Multi-period comparison and trend | S17 |
| EBITDA and margins | Revenue and EBITDA with margin trend | S17 |
| Segment performance | Segment revenue and profitability comparison | S4 |
| Cash conversion | PAT vs operating cash flow | S17 |
| Working capital | Receivable, inventory and payable trends | S17 |
| Capacity | Existing, operational and planned timeline | S9 |
| Capex | Project-wise investment and commissioning tracker | S9 |
| Order book | Order book movement and execution bridge | S13 |
| Guidance | Guidance vs actual | S11, S12 |
| Customer concentration | Contribution and dependency | S5 |
| Product portfolio | Product and application matrix | S3 |
| Future growth | Driver-wise growth bridge | S13 |
| Risks | Ranked risk matrix with warning signals | S19 |
| Valuation | Bear, base and bull comparison | S20 |

### Data storytelling rules

- Titles state the insight, such as "Revenue grew 42%, but EBITDA margins contracted as new capacity ramped up", and only when the evidence supports it.
- The most important number or change is highlighted.
- Historical, current and projected figures are clearly distinct.
- Reported figures, estimates and management guidance are kept separate.
- Units, periods and comparison bases are shown.
- Unusual movements and divergences are explained.
- Sources sit near the visual.
- Axes and scales are never manipulated, and missing data is never created.

### Presentation priorities

1. Clear information hierarchy.
2. Consistent typography and spacing.
3. Insight-led section introductions.
4. Financial tables that are easy to compare.
5. Charts that explain business economics.
6. Management commentary placed beside the numbers it explains.
7. Key findings visibly distinct from supporting information.
8. Traceable sources and assumptions.
9. No excessive cards, icons, borders or decoration.
10. No repeating the same data in several visual forms.

### Where this meets the locked design system

Your block says section 7 stays locked and existing technology stays unless you ask for a change, so these two points resolve as follows:

| Point | Resolution |
|---|---|
| Section 7 says Chart.js only; your block says don't force one library | The report keeps Chart.js plus inline SVG. Waterfalls, Sankeys and bridges are drawn as inline SVG or Chart.js, with no new library. Plotly, D3 or Python charts are used only if you ask or the output format changes. The skill's guidance stays library-agnostic |
| Section 7 puts borders on every card; your block says no excessive cards or borders | The agent uses fewer cards and more plain tables and text. The border style on what remains doesn't change |

The report must stay readable, responsive and printable.

### Section 6A in each generated prompt

Fixed rules, plus one company-specific **visual plan** written by the skill. One row per key visual:

| Research question | Expected insight (to be confirmed by data) | Form | Section | Data source |
|---|---|---|---|---|

The plan works with section 7's must-have charts and doesn't replace them.
Expected insights are hypotheses: the research run writes the final title only after the data supports it, and drops or changes a visual that doesn't earn its place.

### Section 8B in each generated prompt

Runs after section 8, with every section 8 check still in force:
- Does each chart answer a meaningful research question?
- Is the chart type right for the data?
- Are all figures consistent with source data?
- Are historical and projected figures distinguishable?
- Are units, periods and legends clear?
- Are titles insight-led?
- Are management explanations near the relevant financial data?
- Are tables readable on desktop and mobile?
- Are axes and scales honest?
- Are sources traceable?
- Is the report consistent with the locked design system?
- Does every visual improve understanding rather than add length?

The agent then does a final review twice: once as an equity research analyst and once as a report designer. Findings go in the final reply.

## What gets built

New global skill at `C:\Users\Rohit Negi\.claude\skills\research-prompt-builder\`, laid out like your `market-story-post` skill:

```
SKILL.md                     workflow, triggers, rules
assets/skeleton.txt          the default skeleton above: sections 0-6 and 9, S1-S20, fixed wording plus {{slots}}
assets/design-system.txt     section 7: locked text, with slots only for the lines above
assets/visual-check.txt      section 8: locked text, plus the scroll check
assets/visual-intelligence.txt  section 6A: fixed rules plus a {{visual plan}} slot
assets/visual-review.txt     section 8B: locked checks and the final two-role review
reference/visual-intelligence.md  form selection, topic table, storytelling rules, external-skill rules
reference/playbooks.md       business model, story and sector, special situations, optional modules
reference/analysis-guide.md  how to do business, product, management, capex, guidance, growth and anti-thesis analysis, with good examples
reference/learnings.md       the follow-up table above; new corrections get appended
reference/examples.md        which saved prompt to read for which case
scripts/check_prompt.py      pass/fail quality gate, stdlib only
```

The description says "write a research PROMPT", so it does not fire when you ask for research or a report (`company-research`, `stock-research`).

## Workflow inside the skill

**Step 1: Resolve the company.**
Find the ticker with Screener.
Check for an existing prompt, `facts.md` and cached documents, and reuse them.
Never overwrite an existing prompt: a new one is saved as `V2`, and the older file stays.
If you gave your own reason for looking at the company, record it for 0A.

**Step 2: Collect the documents.**
Three sources, in this order:
1. Your uploads: `@file`, a folder path or pasted text. These are copied into `Investment\<Company>\research\docs\` and cited as such.
2. Files already cached in `research\docs\<TICKER>\`.
3. Screener's `get_document_list`, then `scripts/fetch_doc.py`, plus the company website for product and brochure PDFs.

Which documents get used depends on the mode:

| Mode | When | Documents |
|---|---|---|
| **Default** | You say nothing about scope | One annual report; the latest deck and transcript, plus a call that guidance quotes depend on; the latest results; the RHP if recently listed; important announcements only; everything you uploaded |
| **All documents** | You say "all documents", "use everything" or similar | Every annual report, deck, transcript and results filing available from Screener and the cache, plus important announcements, plus everything you uploaded |

Your uploads are always included and are combined with the fetched documents in both modes, never used instead of them, unless you say to use only your uploads.
"Important announcements" stays filtered in both modes, so routine filings such as trading-window closures, newspaper ads and compliance certificates are skipped.
In all-documents mode, Sonnet 5.5 workers read older documents and the newest ones take priority when numbers conflict.
The mode is written into the generated prompt's section 2, so the research run uses the same document set.

A documents-found vs missing list is recorded, and missing items feed the prompt's "To find" list.
The skill never stops for permission.
It asks only if the ticker is ambiguous, or if no documents can be found at all.

**Step 3: Extract.**
Sonnet 5.5 `doc-reader` workers read each document and write page-tagged lines into `facts.md`, with briefs covering business, products, customers, management, capex projects, guidance quotes, growth triggers and risk factors, including management and analyst exchanges.
A `financials-scanner` worker pulls the Screener numbers.
Charts, tables and scanned pages are read from rendered pages via `scripts/pdf_pages.py --render`.
Opus does not read in bulk.

**No Haiku anywhere in this skill.**
`doc-reader`, `financials-scanner` and `evidence-verifier` are pinned to Haiku in `.claude/agents/`, and `stock-screen` relies on that.
So those files stay unchanged, and this skill passes `model: "sonnet"` on every worker call, which overrides the pin for that call only.
If Sonnet 5.5 isn't available, the skill stops and tells you, and never falls back to Haiku.
Generated prompts carry the same instruction in section 3, so the research run also reads with Sonnet 5.5.

**Step 4: Diagnose (Opus).**
This is the core of the skill, written to scratch notes before drafting:
- Why this business matters, and the core debate.
- How one unit of this business earns money. Can it be explained to a first-time investor, with every product listed? If not, read more.
- Who runs it, what they own, what they did with the money, and whether they delivered.
- What management guides now, what capex is under way, and which triggers would drive growth.
- The strongest case against the stock, written before the bull case hardens.
- The business model, story and sector from `playbooks.md`, any special situations, and the resulting structure.
- Which "separate X from Y" rule fits, and the causal chain with its first unproven link.
- 15 company-specific questions, each with a real number or name.
- One connecting-the-dots example with real numbers.
- Data conflicts between documents.
- Valuation metric: uses the table in `business-valuation-scenarios` Step 1, not a copy, so there is one source of truth.
- Sections to keep, add and drop, with reasons.
- The visual plan: the five questions answered for each key visual, based on this company's economics and the data actually available.

**Step 5: Write.**
Fill the default skeleton, applying the override rules and the chosen structure.
Section 1 holds cited facts, conflicts and a "To find" list.
The bear, base and bull settings are marked `[E]`, and a management-guidance row sits alongside them.

**Step 6: Check.**
Run `check_prompt.py` and recompute every derived number by script.
Then read it as a sceptical fund manager: "what obvious question is unanswered?"
Fix and re-run.

**Step 7: Deliver.**
Give the file path, why this business, how the structure was tailored, what is specific to this company, the check output and the gaps.

### `playbooks.md` contents

Each business-type entry gives the unit economics to build, the split rule, the causal chain, the valuation metric, likely peers and must-have charts.
Each one comes from a prompt you already have:

| Type | Drawn from |
|---|---|
| Consumer and store chains | RBA |
| Process manufacturing and gases | Ellenbarrie, Savita |
| Pharma APIs and regulated products | Anlon |
| Pre-revenue clinical biotech (rNPV, phase tables) | Suven |
| Engineered products and auto components | SEDEMAC, Balu, Kabra |

Banks, NBFCs and insurers get a short P/B-and-RoE entry, marked untested because no prompt of yours covers them yet.

Situations layered on top:
- Control change or fresh cash pile (RBA)
- Share swap or related-party deal (Anlon)
- Recently listed (Anlon, SEDEMAC)
- Dilution or warrants (Balu, RBA)
- Annual report only (Kabra)
- Big capex ramp (Balu, Ellenbarrie)
- Promoter-funded cash burn (Suven)

### `check_prompt.py` gates

Measured on your saved prompts on 06-Nov-2026: RBA has 15 questions with a number or name in all 15, and Anlon has 15 with 12. Both have 14 report sections and 0 dashes.

Hard failures:
- 0A missing, not first, or missing any of its parts.
- Sections 0-9 missing or out of order.
- Coverage map missing a core topic without a reason. Core topics: why read, business, revenue model, products, customers, moat, capacity, capex tracker, management (all subtopics), current guidance, next-quarter outlook, future growth build, trigger table, peers, reality vs optionality, causal chain, cash and earnings quality, governance, risk cards with signals, anti-thesis, valuation, assumed vs grounded.
- The anti-thesis section missing, or valuation's bear case not linked to the risks.
- Peers, financials or valuation placed before Business and Products.
- Fewer than 15 questions in full mode, or fewer than 12 with a digit (concise mode: at least 10, relaxed in proportion).
- Fewer than the 10 framework rules in 0B.
- Unfilled `{{slots}}`.
- Any em or en dash, checked by codepoint. A byte-level grep falsely flagged 48 lines in RBA, because `₹` shares bytes with the dashes.
- Section 8 not matching the locked text, or section 7's fixed lines changed.
- Section 6A's fixed rules or section 8B not matching the locked text, or either one missing.
- A visual plan with no rows, or a row missing its question, insight, form, section or source.
- Citation rule or disclaimer missing.
- The word "Haiku" anywhere in the prompt.
- `[E]` missing from valuation cases.
- A local file named in section 1 that does not exist.

Warning only:
- Citation density in section 1. Tags apply to a block rather than to each line (RBA has tags on only 19 of 57 number lines, yet is well cited), so this can't be a hard rule.
- Size outside the band (full 30-55 KB, concise 15-25 KB).
- Visual plan rows with generic titles such as "Revenue and EBITDA". This needs judgement, so it is reviewed by eye as well.
- Report sections outside 9-22, because the structure is meant to flex.

The script can confirm that topics are present, but not whether the analysis is any good.
The fund-manager read and tests 4-6 below cover that.

## Defaults (change any of these when you approve)

- **Documents:** the capped default set plus your uploads, unless you say to use all documents.
- **Size:** full prompt, unless you say "concise" or "short".
- **Delivery:** saved file plus a summary in chat. A 34 KB paste is hard to use; say "paste it" to get the full text.
- **External skills:** `dataviz` drives chart decisions, in place of Baoyu Design Dataviz. Its colours and palette don't apply to the report, because section 7's locked design system stays in charge. `market-research-reports` and `cc-equity-research` are read before building and reused where they add something. Nothing gets downloaded.
- **Concall downloader:** the skill itself uses Screener, because the project notes say the downloader currently returns 0 filings. The generated prompt keeps your run-once-then-fallback line.

## Verification

1. **Gate test.** On RBA and Anlon, the only failures must be the new gates (0A and the coverage map), because they predate those. A good sample must pass. Balu Forge (old format) must fail, along with samples that have a planted dash, an edited section 8, or Management removed. All output is quoted to you.
2. **Screener path, end to end.** Supreme Power Equipment: has a folder, no prompt yet, and is a manufacturer with a capex story.
3. **Upload and all-documents path, end to end.** Jeena Sikho, starting from the PDFs already in your Investment folder (FY26 PPT and transcript, deck-only quarters) and combined with what Screener has. It has no prompt yet and is a services business, not a factory, so it tests whether the skill really adapts and whether the two sources merge correctly.
4. **Follow-up replay.** I go through the follow-up table row by row for both new prompts, and report which lines force each answer. Any row with no answer is a failure.
5. **Accuracy check.** `evidence-verifier` re-reads 10 random numbers from each new prompt against the source page.
6. **Adaptation check.** I read the two prompts side by side and report whether 0A, the structure, the 15 questions, rules, product and management questions, capex, triggers, anti-thesis and valuation metric truly differ, or only the names changed.

7. **Model check.** During tests 2 and 3, I confirm from the run transcripts that every worker ran on Sonnet 5.5 and none on Haiku, and quote the result.

8. **Visual plan check.** For both new prompts, I check that visuals follow each company's economics and differ between them, that titles state insights the data can support, and that sections 7 and 8 match the locked text. The skill must also run correctly with no external skill present.
9. **Preservation check.** After the visual additions, I confirm that every section, depth checklist, gate and test in this plan is still in the built skill, and report the result.

Tests 2 and 3 add two new prompt files to your folder and new `facts.md` files. They use Sonnet 5.5 workers, which cost more than Haiku, and they will take some run time.
No existing file gets changed.

## After building

Add a one-line pointer to the skill in `MEMORY.md`, with a note that new prompt corrections go in `reference/learnings.md`.
