# QA notes: Ind-Swift Laboratories company study

Report: `report/report.html` (21 sections, 56 exhibits), built by `report/build.py` from `model/valuation.py`.
Checks run on 10 Nov 2026.
PDF proof: `report/qa/pdf/report.pdf` (32 A4 pages, gitignored).
Screenshots: `report/qa/pw/` (desktop-p01..p21.png at 1280px, mobile-p01..p21.png at 390px, d1440-top.png, sheet-*.png; gitignored).

## Method and departures

- No worker models were used; Claude read every source document and wrote every section directly.
- Charts are inline SVG built in Python (`report/charts.py`), not Chart.js 4.4.1 as the prompt suggested. Reason: one self-contained file with no external script, identical output in print and on screen, and values drawn from the same model dictionaries as the tables. Every chart has a `<title>`, `role="img"` and printed values or a nearby table.
- No rating box. The house readout (ATTRACTIVE / FAIR / STRETCHED vs price, plus a WATCH management verdict) replaces the reference report's rating stamp and target price.
- Colour: teal and amber house palette instead of EL's red linework.

## Data notes

- Top nine FY26 products: Rs 335.32 cr, not 334.32 (addition slip corrected; the build asserts the total).
- H1 FY27 PAT: PBT Rs 73.49 cr less tax Rs 17.20 cr is Rs 56.29 cr, but the filed PAT is Rs 55.47 cr. The Rs 0.82 cr gap equals the exceptional item on deck p29 and is shown as "other items"; the build asserts it.
- Receivable days: Sep 2026 receivables Rs 234.79 cr over annualised H1 revenue (H1 line x 2), giving 102.9 days. This is a half-year basis, not a full-year average.
- Share count: 9,39,61,558 fully diluted is used; 9,25,61,558 is the sensitivity because the NSE filings conflict (see evidence/care-ma.md).

## Visual defects found and fixed during step [6]

- Wide tables: stack mode on phone instead of sideways scroll.
- Waterfall: staggered labels so they do not overlap.
- Value-range chart: label halo.
- Line charts: end-label collision.
- Oversized standalone charts made wider and shorter.
- Source lines grouped by document with page lists.
- S7 table width.
- S14 duplicate source line replaced by a caption.
- An unformatted float in the text.
- Capex range now computed from the model.
- Claim counts made consistent across S1, S11 and S16.
- Label-wrap assert added to the chart builder.
- Grouped bars show a y-axis when bars are too narrow for value labels (S9 capex on phone).
- The anti-thesis bear multiple (13.2x) is now computed, not typed.
- Source tag "[tr-q1 p14]" renamed "[Q1 call p14]".
- PDF: S2 milestones kept on one page; two-column source list removed a final page holding only the disclaimer (33 pages to 32).
- Source re-check: "Operating revenue H1 FY27 Rs 420.97 cr" now cites deck p3 (where the figure is printed) as well as p29 (revenue Rs 416.35 cr plus operating other income Rs 4.63 cr).
- Analyst review: the S1 lede said "fair to slightly cheap" while the readout said ATTRACTIVE; the lede now states the computed +22% and -29% and matches the readout.
- Tried and reverted: a sticky side contents rail at 1440px. The house quality process forbids sticky and fixed elements (reports scroll as one document), and review.mjs flagged it.

## Section 8: visual verification

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Desktop | PASS | review.mjs at 1280px: 21 pages, no overlap, clip or overflow flags (desktop-p01..p21.png); extra pass at 1440px: no sideways scroll (d1440-top.png). |
| 2 | Mobile | PASS | review.mjs at 390px: 21 pages, no sideways scroll, wide tables stack (mobile-p01..p21.png); by-eye pass of all 21 tiles. |
| 3 | Console | PASS | 0 console errors and 0 failed requests at 1280, 1440 and 390px. |
| 4 | Interaction | PASS | 42 contents links, 0 broken anchors; 4 of 4 sampled links land on their section at 1440px and at 390px. All 44 SVG charts have `<title>` and printed values. No toggles or tabs exist. |
| 5 | Charts | PASS | 44 SVG charts all render with values, labels and a source line. |
| 6 | Numbers | PASS | Charts and tables read the same model dictionaries in build.py; spot checks: Exhibit 1 FY26 649 / 47, Exhibit 50 vs Exhibit 51 (Rs 426 = 4,196 cr discounted, divided by diluted shares), Exhibit 52 points vs model. |
| 7 | Print | PASS | 32-page A4 PDF, every page inspected; sections in order, no cut tables, no blank pages. |
| 8 | Scroll | PASS | html and body overflow visible; mouse wheel over a chart and over a table each moved the page 600px. Touch scroll not tested on a real device; 390px emulation only. |
| 9 | Theme | PASS | Light theme only; body background rgb(238, 241, 243), pages white. |
| 10 | References | PASS with gaps | See the reference-use log below. |
| 11 | Reader test | PASS | See below. |

### Reader test

- Explain the business: S2's revenue equation (own registrations x units x price, plus partner supply, plus India) and the 83% export share.
- Reproduce a calculation: H2 FY27 need = Rs 953.84 cr (Rs 635.89 cr x 1.5) - Rs 420.97 cr = Rs 532.87 cr, +63.5% on H2 FY26 (S12).
- Capital constraint: working capital (118 days, receivables 103 days) and Rs 250 cr of capex needed beyond about Rs 1,000-1,200 cr of sales (S9, S17).
- Thesis-break signal: Q3 FY27 sales below Rs 250 cr, or a fourth year of negative operating cash flow (Exhibit 55).

## Reference-use log (check 10)

- Family: EL (Keynote Capitals, Elecon Engineering initiation, May 2025).
- Tool run in step [6]: `python -I report_references.py check` gave "PASS: three original resources; 7 reports; 239 physical pages; 6,417 text regions".
- Manual entries read in step [6]: EL-01, EL-07, EL-10, EL-16, EL-18, EL-20, EL-25, EL-27, EL-28, EL-31, EL-32, EL-33.
- The step [5] page plan also used EL-14, 19, 21, 23, 24, CC-20, SU-18 and SU-20; these were not re-read in step [6].
- Gap: page images of the reference PDFs were not viewed. The comparison uses the manual's measured layout, type evidence and page jobs only.

| Reference | Pattern | Where applied | Result |
|---|---|---|---|
| EL-01 | Narrative column plus facts rail | S1: answer, story and Exhibit 1 on the left; readout, value range, key data and dates on the right | Matches. Composed last, and its numbers match S20. |
| EL-07 | Identity then milestone timeline | S2 milestones kept as one block in print | Matches. Only events that changed capability, ownership or cash. |
| EL-10 | Parallel-column comparison | S7 quantity vs quality and S8 old vs new company tables | Matches. |
| EL-16, EL-25 | Margin chart with operating explanation | S7 and S17 | Matches. EBIT and EBITDA kept separate; S9 links capex to capacity. No decorative circles. |
| EL-18 | Pipeline by stage | S13 partners signed, validating and commercial | Matches. No mature revenue applied to unsigned programmes. |
| EL-27 | Management tables | S10 management and S18 governance | Matches. |
| EL-28 | Multi-year peer histories | S14 peers | Partial: peers on one period (TTM) with a caption on the segment mismatch, not two multi-year tables. |
| EL-31 | Positive case, then a risk subsection | S19 risks and anti-thesis | Matches. |
| EL-32 | Dense forecast reference | S17 financials split into tables | Departure on purpose: split for screen reading, as the manual advises. |
| EL-33 | Valuation table, then synthesis | S20: Exhibit 50 table, bridge, range, sensitivity, verdict | Matches. Multiple justified (Exhibit 54) and stress-tested (Exhibit 53). |

- Typography: EL measured Calibri / Calibri-Bold, body 9.96pt, tables and notes 6.96-8.04pt. Ours: Calibri with Carlito then Segoe UI as fallbacks; print body 10pt / 13pt leading, h2 14pt, tables 8.5pt (financial tables 8pt), sources 7.5pt; screen body 15px. Calibri is installed on this machine, so no substitute was rendered in the checks.
- Geometry: A4 with 36pt side margins, not EL's 540 x 780pt page. No text-rectangle geometry was copied.
- Design references are not company evidence; no figure in the report comes from them.

## Section 8B: visual quality review

| # | Question | Answer |
|---|---|---|
| 1 | Each chart answers a research question | YES. Every exhibit title states its finding. |
| 2 | Chart type fits the data | YES. Bars for levels, lines for trends, a waterfall for the value bridge, a dot range for cases. |
| 3 | Figures consistent with source data | YES. 10-number re-check: 10 values PASS, 1 citation fixed; model re-run matches. |
| 4 | History vs projection easy to tell apart | YES. No chart mixes actual and forecast bars. Projected figures carry [E] (our estimate) or [G] (guidance), guidance lines are dashed and labelled, and forecasts sit in model tables (Exhibits 18, 31, 50, 53). |
| 5 | Units, periods and legends clear | YES. Rs cr in every exhibit title or axis; legends whenever there are two or more series. |
| 6 | Insight-led titles | YES. |
| 7 | Management's words beside the numbers | YES. Call quotes sit beside the exhibits they explain (S5, S12, S13). |
| 8 | Tables readable on desktop and mobile | YES. Tables stack on phone. |
| 9 | Honest axes | YES. Bars start at zero; the value range uses one linear scale with the price marked. |
| 10 | Every source traceable | YES. Tags in the form [deck pN] and [call pN] resolve in the sources appendix. |
| 11 | Matches the locked section 7 design system | YES, with the declared departures (SVG instead of Chart.js, house palette, readout instead of a rating). |
| 12 | Every visual adds understanding | YES. Exhibit 1's annual history repeats in S17 in table form on purpose: S1 is the summary, S17 the audit. |
| 13 | One reference family with logged precedents | YES (EL), with the image gap noted. |
| 14 | Thesis traceable from evidence to falsification | YES. S16 causal chain: launches, then partner volume, then H2 sales, working capital, cash, and the Exhibit 55 signals. |
| 15 | Reference patterns applied with readable type | YES. |

### Final review 1: equity research analyst

- A fund manager's first question ("is H2 achievable, and does it turn into cash?") is answered in S1 and S12, with numbers.
- Fixed: the S1 lede and readout did not match. The H1 revenue citation was imprecise.
- Unsupported items are labelled, not filled:
  - pre-merger formulation accounts;
  - line-wise margins;
  - partner contract terms;
  - Synthimed sale terms (the stake value is management's estimate);
  - the share-count conflict.
- The machine transcript garbles some names and numbers; affected quotes are flagged.

### Final review 2: report designer

- Hierarchy: the S1 answer bar, readout and value range are visible first on desktop and in the first phone screens.
- Repeated data: Exhibit 1 and the S17 table overlap on purpose (summary vs audit); no other duplicate visuals found.
- Fixed in this pass: none beyond the lede. The sticky contents rail was tried and reverted per the house rule.

### Valuation restructure, 10 Nov 2026

- What changed:
  - S20 now has the three year-wise scenario tables required by the business-valuation-scenarios skill (Exhibits 51-53), each in Screener P&L layout with FY25A and FY26A beside FY27E-FY30E.
  - A key assumptions and caveats list follows the tables.
  - The bull case was moved to the top of the guided 20-25% CAGR; its value went from Rs 504 to Rs 519.
- Checks:
  - `python -I -X utf8 model/valuation.py`, then `python -I -X utf8 report/build.py`, gives: sections 21, exhibits 59, base 425.8, bear 246.32, bull 519.41, readout ATTRACTIVE.
  - `node review.mjs`: desktop 21 pages and mobile 21 pages, 0 console errors, automated checks clean.
  - By eye: S20 at 1280 px is clean; at 390 px the 7-column tables fit with no sideways scroll; in the value-range chart, the bull label sits above its dot with no overlap.
  - PDF: 34 A4 pages; pages 29-32 (S20) were rendered and inspected, and every table is unbroken.
