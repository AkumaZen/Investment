# How to build a client-grade equity research report

Recorded: 2026-11-08
Type: process lesson

## Lesson

A research report is finished only when it reads easily, shows its numbers as real charts, and has passed both an automated visual check and a page-by-page look at the rendered pages.
Good research in heavy prose is not a finished report.
This applies to every company report in this repository that goes to paid clients.

## Evidence

The Augmont (NSE: AUGMONT) report went through three versions between 6 and 8 November 2026.
The ChatGPT "revamp" PDF had about 10,300 words over 26 pages, abstract headings, inline source tags and almost no charts.
The client feedback was that it was hard to understand and had no visuals.
Version 3 (`research/companies/nse-augmont/v3/`) fixed this by copying the structure of seven broker reports (`references/equity-reports/README.md`) and adding a visual review loop.
The review loop found 9 defects on the first build, 13 more with Playwright, and 4 more by eye that the automated checks missed.
Details are in `research/companies/nse-augmont/v3/qa-notes.md`.

## The process

### 1. Brief and resumability

Fix the brief before writing: readers, output format, whether a rating or target is wanted, data refresh source, and git limits (push, files not to stage).
Write it at the top of a `STATUS.md` with numbered stages, and tick a stage only when its output file exists.
That way the work can resume after the context runs out without redoing anything.
Store the user's standing answers in memory so the same questions are never asked twice.

### 2. Study references before designing

Keep broker reports locally in `references/equity-reports/` and read the design lessons in its README.
The patterns that matter most:
- a visual on almost every page;
- headlines that state the conclusion ("Profit is not yet turning into cash", not "Cash flow");
- a "story in charts" page right after the summary;
- a cover with a summary and a right-hand rail of key data;
- teach the industry before the company;
- a one-line "In short" side note per page;
- one brand colour plus grey;
- standard back pages (risks, management, financial statements, disclaimer).

### 3. Plain language

Write for a smart reader who is not an analyst.
Short sentences, one idea each.
Explain every term the first time, and keep a glossary.
Put sources in a small line under each exhibit, not inside sentences.
Say "our estimate" or "(calc.)" next to every derived number.
No em dashes.

### 4. Build from data, not by hand

Keep every number in one build script (`build_v3.py` pattern) with its source next to it.
Add asserts that tie the numbers back to filings (quarters sum to the year, parts sum to totals).
Draw charts as dependency-free SVG (`charts.py` pattern) so the HTML is one portable file.
Number exhibits at render time so they always run in reading order.
For full-width charts, render a second phone-sized copy and swap them with CSS at 820px, or labels become unreadable on phones.

### 5. Valuation

Diagnose the business before picking a multiple; do not default to P/E.
For a thin-margin trader like Augmont, price to sales is meaningless and EV/EBITDA adds little, so use P/E on owner profit (after minorities) with a price-to-book cross-check.
When management gives no guidance, say so on the page, start the current year from actual half-year results, and label every projected line as an estimate.
Check that each case is physically possible: for Augmont, sales per rupee of equity had to stay near the latest quarter's level, because growth is limited by capital.
Keep the scenario model in its own script (`valuation.py`) so the report and any dashboard export use the same numbers.

### 6. Visual verification (mandatory, every build)

Run the shared check after every build that changes layout, charts or tables:

```
cd tools/report-visual-check
npm install            # first time only; uses installed Edge, no browser download
node review.mjs <path/to/report.html>
```

It screenshots every page at desktop (1280px) and phone (390px) width, writes contact sheets, and flags:
- sideways scroll, sticky or fixed elements, elements wider than their container, tables that need scrolling;
- chart labels under 9px, clipped labels, labels overlapping each other, labels spilling onto a neighbouring bar;
- body text under 11px, console errors, em dashes.

A clean automated run is the floor, not the finish.
Then do the by-eye pass:
1. Open every `sheet-desktop-N.png` and `sheet-mobile-N.png` and look at the whole page layout: gaps, cramped blocks, misaligned columns, boxes out of place.
2. Open the full-size page screenshot for every page you changed, and every page with a chart, and read each chart label, legend and table cell.
3. Check these by eye because the script cannot judge them: bars that sit off-centre in their slot, text that wraps awkwardly in a narrow column, lists whose numbers clash with page numbers, charts that do not match their headline, colours that mean different things on different pages.
4. Fix, rebuild, and rerun both the script and the by-eye pass until both are clean.
5. Record the defects found and fixed in the report's `qa-notes.md`, including anything the script missed, and add a check to `review.mjs` when a miss can be detected automatically.

Report the evidence (the command, its output, and what the by-eye pass found) instead of saying it looks right.

### 7. Commit and hand over

Commit in small steps with messages that say what changed and why.
Never push or stage files the user excluded.
In the reply, show the key numbers and tables, state what is estimated, and ask the user to approve numbers before any export (for example the dashboard JSON).

## Limits and counterexamples

This was learned on one company and one report style.
A quarterly update needs fewer pages (see the MQ reference) but the same verification step.
The automated checks only test SVG charts and HTML tables; images of charts need the by-eye pass alone.
The by-eye pass depends on looking at full-size images; contact sheets alone are too small to read chart labels.

## Application

Trigger: any request to build, revamp or extend a company research report or valuation page.
Action: follow steps 1-7, reusing the Augmont v3 build, chart and valuation scripts as the starting point.
Next verification: on the next company report, count defects found by the script vs by eye, and turn any repeat by-eye defect into a script check.
