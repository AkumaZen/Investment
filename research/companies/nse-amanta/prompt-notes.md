# Amanta Healthcare prompt diagnosis

Prepared 10 November 2026, Asia/Kolkata. Output is a research prompt, not a report or investment recommendation.

## User scope and definition of done

User instruction, verbatim: "I want you build a prompt for Amanta Healthcare, Use latest concall and transcript only".

NSE AMANTA, BSE 544502; Indian listed equity; INR; analysis cutoff 10 November 2026. Company archive and Screener document discovery identify the 4 November 2026 Q2/H1 FY27 call, transcript filed 9 November. No other company document is used as evidence. The audio and transcript are the same underlying call, not independent corroboration. Audio URL is recorded but not listened to during preparation. The transcript is fully read by a GPT-6.1 Sol worker. Do not call this audio-verified research.

Done: a versioned prompt with all core sections, a company-specific diagnostic and questions, the installed valuation skill referenced by absolute path, staged design resources, explicit source limitations, passing prompt checks and an independent ten-number source check.

## Diagnosis before drafting

1. Why it matters: commissioned sterile capacity, solar savings and an upcoming SVP line may change earnings, but qualification, demand and financing determine the result. Core debate: whether equipment becomes profitable collected sales rather than just capacity.
2. Unit economics: qualified available physical units x sell-through x yield x realised price, with product/channel economics separate. Call names SteriPort/ISBM, Classic/Legacy Pack, SVP/BFS, inhalation, budesonide suspension, ophthalmics including multi-dose preservative-free, WFI/diluents. Glass vials/ampoules/cartridges and F&D facility are optionality, not sanctioned projects. Molecule-level sales/approvals remain missing.
3. Management: Bhavesh Patel CMD and Paras Mehta CFO. IPO-funded SVP mentioned, but IPO proceeds/use reconciliation, holdings, remuneration, pledge and governance cannot be assessed. Debt repayment statements do not establish net debt or cash adequacy.
4. Guidance: distinguish Line 3 FY27 contribution, annual optimal revenue potential, two-year CAGR/margin aims, full-utilisation target, SVP FAT/commissioning/contribution/filing milestones, speculative SVP revenue and promised model disclosure. No silent FY27/FY28 assignment of conflicting ranges.
5. Anti-thesis first: output does not guarantee incremental sales; polymer inflation can consume pricing gains; qualification can delay SVP sales; interest, depreciation and cash demands can absorb operating improvement. Do not infer current breaches from these hypotheses.
6. Playbook: regulated finished-dosage manufacturing plus capex ramp and product qualification. Not hospital services, generic API-only economics or clinical-stage biotech.
7. Separate capacity from qualification and sold demand; separate gross savings from earnings and cash. First unproven links: sustained full-output sales, product transfer and variation approvals; data for cash conversion is absent.
8. Fifteen tailored questions are in build_prompt.py and the final prompt: include Line 3 60/110, solar 9, 20-product counts, SVP 20.9/31, 190 gross borrowing, 420-430 annualised vs 400-420 FY28, and missing per-share inputs.
9. Connecting dots: H1 151.9 less Q2 83.1 implies Q1 68.8; Q2 sequential growth 20.78%. The 60/110 ratio is not utilisation because periods differ. Arithmetic recomputed by script.
10. Conflicts: source capacity INR prefixes, 52% vs computed SVP expansion, September 2027 date, pipeline counts, market-development versus approvals, commissioning versus revenue, gross borrowing versus net-debt question, repayment 30-32 versus 35, and speculative versus guided revenue. Facts and financials retain page references.
11. Valuation: read C:\Users\Rohit Negi\.codex\skills\business-valuation-scenarios\SKILL.md. EV/EBITDA provisionally fits leverage and capex/depreciation transition. Asset/fixed-asset turnover and cash checks need missing statements. Current price, diluted shares, cash/net debt and defensible multiples are unavailable. Keep separate scenario tables with missing cells and NOT RATED, not a fabricated target or return. User source scope takes precedence over fetching required valuation inputs.
12. Structure: keep S1-S20 core coverage; rename S3 sterile products, S8 incremental Line 3 sales, S9 capacity/capital/cash, S11 single-call claims register. Add indexed Q&A appendix. Exclude outside-source evidence, price move maps, unsupported regulatory/governance verification, historical delivery score and rNPV. No core topic disappears silently.

## Visual and reference decisions

Design bundle check passed. Read manual sections 1-3, 5-10 and MQ-01, MQ-02, MQ-04, MQ-05, MQ-06 entries and corresponding JSON page records. Selected MQ because evidence scope is the latest quarter/call, with compact results and forward monitoring. Expand product teaching to meet Business/Products-first coverage, not an initiation based on missing historical documents. Keep MQ blue/grey grammar; no broker branding or copied forecasts. Original brokerage source images were not inspected; no exact visual-match claim. The three supplied manuals/specification and portable reader are staged beside this company's research.

Visual questions: Line 3 sales versus annual potential is best a date/status table; SVP product/qualification gates a matrix/timeline; solar gross-to-net effect a formula bridge with unknowns; quarter/half-year financial comparison a period-labelled table; guidance a claims register; valuation three separate scenario tables with unknown cells. Each final visual-plan row supplies question, hypothesis, form, section and source. No arbitrary chart count; no invented series.

dataviz was absent from standard local skill folders, so use the internal compatible chart rules in visual-intelligence.md. Read installed market-research-reports and evidence_model.md for claim classification and calculation lineage. Read cc-equity-research forensic, reporting-quality, management, earnings-scorecard and business-model references for definition discipline and Q&A candour. Read initiating-coverage valuation-methodologies and quality-checklist selectively for inputs and completeness. Their external-data workflows, DOCX/Excel defaults, US-specific measures, chart/page minimums and single-task gating do not apply to this prompt builder and user-selected scope. These references do not supply company facts. Their overlaps with core coverage are not duplicated.

## Found, missing and deliberately excluded

Found: latest transcript, matching audio link, all 16 physical pages, complete page-tagged facts and financial extraction. No deck, annual report, RHP, release or older call was read. Current shares, price, cash, complete annual P&L, cash flow, working capital, project cost/spend, customer identities, approval proof and governance filings are missing/outside scope. Do not fetch them during the later run without a changed user brief. Use the missing-input register rather than inventing them.

## Follow-up replay

| Learning | Prompt forces the answer or scope limitation |
|---|---|
| Moat and who else can do it | S6 requires evidence and counterpoint; independent competitor proof unavailable |
| Actual customers and competitors | S5/S14 distinguish named buyers from analysts and state no named customers |
| Products, types and what is new | S3 complete call inventory and stage matrix; budesonide and preservative-free details |
| Existing, live and planned capacity | S9 three-way project table and denominator/unit conflicts |
| Contract terms and who benefits | S2 licensing/export/front-ending economics; absent terms explicit |
| Margin by business model | S4 prohibits invented product margin allocations |
| Recurring versus one-time revenue | S2 distinguishes repeat clinical use from contracted recurring revenue |
| Why large buyers purchase and repeat | S5, not disclosed where names/orders absent |
| Where cash goes | S9/S10/S17 debt, capex and missing cash reconciliation |
| Pledge status checked | S10/S18 explicitly Not verified under permitted scope, never assumed unpledged |
| Topics not in numbers | S3/S13/S15, including glass injectable/F&D optionality |
| Assumed versus grounded, calculations | 0B, section 5 safeguard, S20, section 6 |
| Business-appropriate valuation | Section 5 installed skill pointer and conditional EV/EBITDA reasoning |
| Plain clinical/pipeline evidence | S3 qualification/validation stages; no irrelevant clinical-trial/rNPV template |
| Every named partner's relation | S5 excludes analyst/advisor names from buyer identities |
| Approvals versus applied, guidance fit | S3/S12/S16, filing timing and variation approval gates |
| Website product catalogue | Explicitly excluded by user's newer source-only instruction; no catalogue claims |
| Management guidance unchanged | S12 and section 5 preserve ranges, horizons, ambiguity and speculative qualifiers |
| Trackables and triggers upfront | S1 milestone list, full-utilisation and model-disclosure targets |
| Light theme and scroll | Locked sections 7/8 |
| Capex properly explained | S9 one row per project, actual vs hypothetical cost, missing funding data |
| Next-quarter management outlook | S12, Q3/Q4 mix statements versus no assured margin improvement |
| Derived future growth and absent triggers | S13 and explicit inability to quantify unsupported drivers |
| Anti-thesis | S19 precedes scenario completion and supplies bear mechanisms |
| Design references actually shape output | MQ page plan, staged sources, model-first/storyboard/render/reader-test contract |
| GPT worker amendment | Reader, scanner and verifier use gpt-6.1-sol, low, fork_turns none |
| Valuation skill referenced, not pasted | Section 5 exact installed Codex path and Steps 1-4 reference |

## Adaptation review

Compared the nearby Concord Biotech prompt opening for depth/tone, without copying facts. Concord is an all-documents fermentation/API recovery with multi-year financials; Amanta is a single-call sterile finished-dosage ramp with unresolved guidance and missing price/share/cash inputs. Business, 15 questions, product economics, management evaluation limits, capacity gates, anti-thesis, scenario completeness and MQ visual plan differ accordingly. No legacy example financial inputs are reused.

## Validation record

- Prompt checker: 33 PASS, zero FAIL. One WARN: roughly 67.5 KB exceeds the 30-55 KB guidance band. Retained intentionally: full locked design/verification contract plus detailed single-call scope overrides and Q&A conflicts prevent the later agent from importing outside data or flattening speculative statements into guidance. No user size limit was requested.
- Fifteen financial-scanner calculations independently recomputed; additional prompt arithmetic checked in calculation-check.md.
- All three workers (reader, scanner, independent verifier) launched with gpt-6.1-sol, reasoning_effort low, fork_turns none.
- Later report visual checks have not been run because this deliverable is a Markdown prompt, not an HTML report. The prompt retains the full later report visual contract.
`n- Independent verifier: 10/10 sampled claims MATCH (seed 20261110), including five opening-remarks and five Q&A claims; no remaining material scope or guidance-qualification issues. See verification.md.
