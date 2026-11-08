# Augmont report v3 - plain-language, chart-led rebuild

**Read this file first when resuming.** Tick a stage only when its output file exists.

## Brief (fixed by the user, 2026-11-07)

- Readers: paid clients. Language must be light and plain. Every page needs real visuals of metrics, like the reference broker reports.
- Output: one HTML file `v3/augmont-report.html`. No PDF yet.
- No rating for now. Bear/base/bull scenario values to FY29 added 2026-11-08 on user request (`valuation.py`, pages 20-21).
- Refresh price and financials with the Screener MCP tool.
- Do not push. Local commits are OK. Do not stage the two root PDFs (`Augmont_Equity_Research_Revamped.pdf`, `Augmont_Report_Critique.pdf`).
- References: `references/equity-reports/` (7 PDFs + README with design lessons). Do not ask the user about them.
- ChatGPT share conversation was read (5 user turns; last attempt hit usage limit, no output). Nothing in it beyond the request already captured here.

## Inputs to reuse (already verified in earlier work)

- `../facts-research-q2-deck.md` (32-page Q2 FY27 deck), `../facts-q2-fy27-call.md` (call), `../facts-research-ar26.md` (FY26 AR),
  `../facts-research-q2-results.md`, `../facts-research-q1-deck.md`, `../facts-research-prospectus.md`, `../regulatory-and-competition.md`,
  `../research-financials.md`, `../data/*.json`, `../model.py` / `../data/model-output.json`.
- Earlier caveats in `../HANDOFF.md` still hold (owner vs standalone profit, negative CFO, unverified items).

## Stages

| # | Stage | Output | Status |
|---|---|---|---|
| 1 | Download + study references | `references/equity-reports/README.md` | DONE |
| 2 | Refresh Screener data | `v3/data/screener-refresh-2026-11-07.md` | DONE |
| 3 | Facts with sources (kept inside the build script per exhibit, dumped to chart-data.json) | `v3/build_v3.py`, `v3/chart-data.json` | DONE |
| 4 | Page plan / storyboard (headline + exhibit per page) | `v3/storyboard.md` | DONE |
| 5 | Chart helpers (dependency-free SVG) | `v3/charts.py` | DONE |
| 6 | Build script + HTML | `v3/build_v3.py` -> `v3/augmont-report.html` | DONE (23 pages, 43 exhibits) |
| 7 | QA: number checks, screenshots, Playwright design lint | `v3/qa-notes.md`, `v3/qa_shots.py`, `v3/playwright/review.mjs` | DONE (0 issues desktop + mobile) |
| 8 | Local commit (no push) | git log | DONE |
| 9 | Bear/base/bull scenarios to FY29 (business-valuation-scenarios skill) | `v3/valuation.py`, `v3/data/valuation-scenarios.json`, pages 19-21 | DONE (awaiting user approval of numbers; dashboard JSON only after approval) |

## How to continue

- Edit text or data in `v3/build_v3.py`, then run `python -I build_v3.py` from `v3/`.
- Re-check visuals: `python -I qa_shots.py desktop 1 4` (or `mobile 1 2`); PNGs land in `v3/qa/`.
- Scenario drivers live in `SCEN` in `valuation.py`; rebuild with `python -I build_v3.py`.
- Next edition (when the user asks): rating, PDF export, fill the SEBI RA disclaimer placeholder, update with Q3 FY27 results.

## Log

- 2026-11-07: Stage 1 done. Chrome extension unavailable (account mismatch); ChatGPT share read via headless Edge.
- 2026-11-08: Stage 9 done. Base FY29 value Rs 1,134 (20x FY29E owner EPS 56.7); bear 397 (14x); bull 2,191 (26x). 25 pages, 46 exhibits.
- 2026-11-07: Stages 2-8 done. Report built and reviewed at desktop and phone widths; 9 defects fixed (see qa-notes.md).
