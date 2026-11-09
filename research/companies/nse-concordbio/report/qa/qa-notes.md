# Concord Biotech company study - QA summary

Report: `report/report.html` (built by `report/build.py`), exported to `report/Concord_Biotech_Company_Study.pdf`.
Analysis date: 9 November 2026.
QA run on the same date.

## 1. Automated visual check (tools/report-visual-check)

Command: `node review.mjs ../../research/companies/nse-concordbio/report/report.html` from `tools/report-visual-check`.

Final output:

```
desktop pages 21 console errors 0 {}
mobile pages 21 console errors 0 {}
automated checks clean - now do the by-eye pass
```

The first run flagged 11 issues.
All 11 were fixed in the generator before the by-eye pass.
Screenshots are in `report/qa/pw/` (git-ignored, regenerable with the command above).

## 2. Defects found by eye and fixed

Content:

- Cash from operations was stated as 100% of EBITDA; the correct figure is 73% (it is 103% of profit after tax).
- The capex caption said capex was "four" times depreciation when it was three, and the table rows were out of year order.
- The USFDA row in the regulatory table was marked OK although the USFDA database was not checked; it now says NOT VERIFIED.
- The RHP was cited as read when its text had not been extracted; the citation now says located, not read.
- The governance summary in S18 listed four of the five watch items; the fifth (promoter pay) was added.

Visual:

- Margin chart: crowded tick labels and a label colliding with a bar; ticks thinned and labels moved.
- Peer bar charts were unsorted; they are now ranked.
- The valuation waterfall had no headroom above the tallest bar; the scale was extended.
- The cover had a large blank area under the summary; the layout was tightened.

Print and PDF:

- A forced page break per section produced 33 pages, several almost empty; sections now flow with keep-together rules and a running header, giving 26 pages.
- The first keep-together attempt split Exhibit 9 inside its SVG because SVG tags were treated as void HTML tags; the splitter now treats only HTML void tags as void.
- The cover forced section 2 onto a new page and left page 2 half blank; that break was removed.

## 3. Ten-number re-check against source pages

| # | Number in report | Source page | Result |
|---|---|---|---|
| 1 | Q2 FY27 revenue Rs 309.1 cr | Q2 FY27 deck p6 | PASS |
| 2 | Q2 FY27 EBITDA Rs 104.4 cr | Q2 FY27 deck p6 | PASS |
| 3 | Q2 FY27 PAT Rs 69.6 cr | Q2 FY27 deck p6 | PASS |
| 4 | Top-10 customers 37.6% of FY26 sales | Q2 FY27 deck p23 | PASS |
| 5 | Current investments Rs 438.1 cr | Q2 FY27 deck p11 | PASS |
| 6 | FY26 EPS Rs 24.78 | Annual report FY26 p196, p233 | PASS |
| 7 | Bonus allotment 10,46,16,204 shares | Bonus allotment filing p1 | PASS |
| 8 | Utilisation Unit III 55%, Unit I 75% | Q2 FY27 transcript p18 | PASS |
| 9 | Tax rate guide 24-25% | Q2 FY27 transcript p10 | PASS |
| 10 | FY26 revenue Rs 1,054.9 cr (1,05,489.07 lakh) | Annual report FY26 p196, p230, p247 | PASS |

Extra checks: Palvella stake Rs 84.1 cr (AR FY26 p238) PASS; promoter pay Rs 14.05 cr (AR FY26 p244) PASS.
Japan JV sales of Rs 29.1 cr could not be re-found by text search and is listed as a gap.

## 4. Model re-run

Command: `python -I -X utf8 model/valuation.py`, then `git diff --stat model/`.
The diff was empty, so the committed valuation (bear Rs 352, base Rs 696, bull Rs 894) reproduces exactly.
The report build prints `base 696 bear 352 bull 894`, matching the model.

## 5. Section 8 checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Desktop 1440px, nothing overlaps or clips | PASS | review.mjs clean; `qa/pw/desktop-p01..p21.png` inspected by eye |
| 2 | Mobile 390px, no sideways scroll, tables scroll in place | PASS | review.mjs clean; `qa/pw/mobile-p01..p21.png` and contact sheets inspected |
| 3 | Console errors and failed requests | PASS | 0 errors desktop and mobile; page loads no network resources |
| 4 | Interaction: TOC links, tooltips, toggles | PASS | Playwright: 42/42 anchor links land on their section at both widths; 21 link targets all exist; charts are static SVG with printed value labels and 475 `<title>` hover tooltips; no toggles or tabs |
| 5 | Charts render with data, axis labels and source line | PASS | 45 exhibits, 48 SVGs, 0 canvas; 50 source lines; inspected by eye |
| 6 | Chart numbers match their tables | PASS | Charts and tables are drawn from the same data dict in build.py; values exported to `report/chart-data.json` |
| 7 | Print: all sections in order, no cut tables, no blank pages | PASS | 26-page PDF, every page inspected on contact sheets (`qa/pdf/`, git-ignored) |
| 8a | Scroll with mouse wheel over a chart and over a table | PASS | 1440px: 2 to 602 and 103 to 703; 390px: 1076 to 1676 and 1676 to 2276; reached bottom at both widths; no `overflow: hidden` on html or body; no `touch-action` rules |
| 8b | Scroll with touch | NOT RUN | Synthesised touch gestures in headless Edge did not scroll even over plain paragraph text, so the harness cannot test this; no CSS blocks touch scrolling |
| 9 | Light theme on load | PASS | No dark-theme rules or theme switch; light only |
| 10 | References logged and compared | PASS | Family BF; pages consulted BF-02, BF-04, BF-06, BF-14, BF-16 (plus BF-07 and BF-17 in planning); see section 7 below |
| 11 | Reader test | PASS | S2 explains the business; S12 shows the H2 sales calculation (Rs 689 cr); S9 names the capital constraint (finished-dose plants at 5% and 21%); S19 risk cards each carry a thesis-break signal |
| 12 | Every check reported honestly | PASS | Touch scrolling is NOT RUN, not PASS |

## 6. Section 8B questions

1. Each chart answers a research question - YES; every exhibit sits under a section question, and its title or caption states what it shows.
2. Chart type fits the data - YES; time series as bars or lines, rankings as sorted bars, the valuation as a waterfall.
3. Figures match the source data - YES; ten-number re-check passed and charts share data with tables.
4. Historical and projected figures are easy to tell apart - YES; estimates are tagged [E] (42 tags) and guidance [G] (14 tags), and projected or adjusted series use patterned fills or dashed lines.
5. Units, periods and legends are clear - YES; Rs cr, fiscal years and quarters are named on every exhibit.
6. Titles are insight-led - YES; titles state a conclusion, not a label.
7. Management's explanation sits next to the numbers - YES; management's stated reasons are quoted with call page numbers in the text beside the relevant exhibit (for example the FY26 slowdown explanation next to the volume charts).
8. Tables readable on desktop and mobile - YES; wide tables scroll inside their own box at 390px.
9. Axes and scales are honest - YES; bar axes start at zero; the one line chart with a non-zero floor (quarterly EBITDA margin, 20-50%) prints its axis range and the 38-40% guide band.
10. Every source can be traced - YES; source lines link to BSE filings with page numbers.
11. Consistent with the locked design system - YES; BF palette (teal #0E5A63), Calibri, banded section heads.
12. Every visual adds understanding - YES; no visual repeats a table shown next to it.
13. One reference family with documented precedents - YES; BF, pages listed in section 7.
14. Each thesis traces from evidence to falsification - YES; S16 causal chains run from contract or volume to margin, cash and a stop signal.
15. Reference patterns applied to page construction - YES; layouts were rebuilt in HTML and CSS, not traced from PDF text boxes.

## 7. Reference use

Family: BF (thesis-led manufacturing and capacity ramp).
Pages consulted: BF-02 (memo with right rail), BF-04 (operating chart sequence from inputs to outcomes), BF-06, BF-14 and BF-16, with BF-07 (asset-status ledger) and BF-17 (valuation bridge plus sensitivity) used in planning.
Borrowed from other families: CC-16 (capacity through two lenses) and CC-20 (capex to free cash flow).
Font: Calibri, embedded in the PDF (Calibri, Calibri-Bold, Calibri-Italic); no substitute needed.
Departures: the right rail of BF-02 becomes a stacked block on phones; the report flows in print instead of fixed one-section-per-page, to avoid near-empty pages.
Design references are not company evidence and were not cited as such.

## 8. Final review, done twice

As an equity research analyst:

- The fund manager's first question (pause or step down?) is answered on the cover and in S8: volumes look like a pause, margin and pricing have stepped down.
- Unsupported claims found and fixed: the CFO-to-EBITDA ratio, the FDA status and the RHP citation (section 2 above).
- Still open and disclosed rather than hidden: who owns the other 25% of Stellon, the largest customer's name, and contract terms (section 9 below).

As a report designer:

- The key finding is on the cover above the fold, and every section opens with a one-line answer.
- No visual repeats data shown elsewhere; the peer table and peer charts show different measures.
- Hierarchy is section band, headline, answer line, exhibits, then "what it means".

## 9. Known gaps

- Owner of the other 25% of Stellon not found.
- USFDA inspection database and Orange Book not checked.
- Promoter pledge status not verified in exchange filings.
- Reasons for the CFO and company secretary exits not disclosed in the documents read.
- Molecule-level and therapy-area sales splits not disclosed.
- Project-level returns on Units III and IV not disclosed.
- Largest customer's name and contract terms not disclosed.
- Images inside decks were not extracted; only text was read.
- Company IR site, NSE copies of filings and the RHP text were not checked.
- Q1 FY27 adjusted margin is not given by the company.
- Japan JV sales of Rs 29.1 cr not re-found in the extracted text.

## 10. Disclosure

The prompt-builder workflow names worker models that are not available here.
No worker models were used; all extraction and checks were done directly in this session.
