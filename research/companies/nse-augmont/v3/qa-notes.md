# v3 QA notes - 7 Nov 2026

## Checks run

- `python -I build_v3.py`: builds 23 pages, 43 exhibits.
  Built-in asserts pass: quarterly revenue sums to FY26 (94,186), quarterly PAT sums to FY26 (348.3),
  consumer product lines sum to 6,687.2, IPO net = 620 - 47.236 = 572.764. No em dash in output.
- Screenshots (`python -I qa_shots.py desktop|mobile A B`, files in `qa/`, git-ignored):
  all 23 pages at 1200px desktop; pages 1-2 and 7 at a true 390px phone width.
- Mobile: page fits 390px with no sideways scroll after switching grids to `minmax(0,1fr)`.

## Defects found and fixed during review

1. Exhibit numbers out of reading order. Now renumbered at render time.
2. Full-width charts oversized and small-multiple labels unreadable. Chart widths now match their column (660 / 360 / 270).
3. Q2 gold/silver chart compared tonnes and Rs/g on one scale. Replaced with a % change chart plus a table.
4. Indian-style "1,16,354" mixed with western commas. Now western throughout.
5. FY24 consumer stack totalled 1,177 from rounded parts. Now uses exact parts (1,178).
6. "Other 3 subsidiaries" bar showed a loss as a positive bar. Removed; loss stated in the source note.
7. Wording said subsidiaries "earned less" in Q2. Only the residual is known, so it now says "rest of the group contributed Rs 39 cr less".
8. Cover had a blank gap. Added a KPI strip.
9. Cash chart: the -578 label collided with the axis label. Added negative-axis padding.

## Known limits (not fixed, by design or pending data)

- Q3 FY26 quarter is derived (FY26 less the other three quarters) and marked with * on every chart.
- The earnings call is a machine transcript; quotes are shown as transcribed.
- Full-width charts are small on phones (they scale down). Readable, but tighter than desktop.
- No verdict, rating or fair value (user instruction). Valuation page shows dated facts only.
- Disclaimer has a placeholder for the publisher's SEBI RA registration details. The user must fill it in before distribution.
- PDF export not done (user asked for HTML first). `@media print` rules exist but print layout was not reviewed.
