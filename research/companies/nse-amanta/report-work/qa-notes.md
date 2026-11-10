# Final visual and calculation QA

Final report: ../report/amanta-healthcare-equity-research.pdf (37 pages, 47 exhibits).

## Evidence

- Shared Playwright check at 1280 desktop / 390 phone: 37 pages per surface; zero flagged issues; zero console errors.
- Print metrics: 37 sections fit A4; no footer collisions or overflow.
- Final PDF rendered to 37 individual PNGs. All pages reviewed in full size by the three Luna medium reviewers across 1-13, 14-26, 27-37. Parent reviewed all PDF contact sheets, all desktop/mobile contact sheets, full-size source documents and selected final PDF/HTML charts and tables.
- Original MQ pages 1,2,4,5,6 and BF capacity example were viewed, not inferred from prose.
- Section navigation and scrolling tested at 1440 desktop and 390 touch. Financial tables use labeled row layout on phones and conventional tables in PDF.
- Independent calculation audit recomputed all 9 scenario rows, including H2-only FY27 WC/cash, with differences below 1e-8.
- Source and output SHA-256 hashes, page numbering and PDF links checked by verify_delivery.py.

## Defects corrected

1. Chart clipping: shortened two left-axis labels; phone SVGs use their own 340-unit viewBox rather than shrink 680-unit charts.
2. Mobile cash table overflow: fixed column sizing and wrapping.
3. PDF print splitting: screen-width media rules had applied during pagination; restricted them to screen, then confirmed exactly 37 pages.
4. Page 21 density: reduced chart height and table padding, retained readable labels.
5. Mobile table labels: widened nonnumeric first columns; dense numeric tables become paired, dated cells. Glossary uses FAT / plant start to avoid splitting the term.
6. Duplicated source punctuation and compressed dates/copy: corrected and re-rendered.
7. Prior-year financial cells: recalculated scanned Q2/H1 statement; corrected H1 pre-exception PBT, operating/company EBITDA and rounding.
8. FY23/FY24 operating-profit series: use raw Screener ex-other-income 53/58, not company EBITDA 56.31/58.76.
9. FY25 quarter PAT mismatch: quantify it on page 21 and treat older secondary quarters as indicative context, not audited roll-forward.
10. Valuation WC double charge: March target less actual September WC; no repeated H1 cash absorption. Solar saving embedded once.
11. Primary locators: corrected annual geography, utilization, solar and share count; strengthened latest-call Q&A page references.
12. Solar sensitivity endpoints: explicit two-decimal PBT/PAT calculations.

## Final rechecks

Original reviewer notes in qa/visual-review-1.md, -2.md and -3.md record intermediate findings. Later parent checks resolve the remaining copy-spacing and glossary-wrap observations. Final shared checker, screenshots, print metrics and interaction JSON are in qa/. The report and verification summary explicitly retain evidence/model limitations; a clean visual check is not an external audit.

## Visual revision — 10 November 2026
User requested official product photography and less unused space. Added six issuer product photographs in two category/platform galleries on pages 4–5. Recorded original asset URLs, hashes and four catalogue snapshots. Preserved aspect ratios, embedded image bytes, attributed each gallery and distinguished existing packs from unbuilt-line/approval evidence.

Reflowed 37 original content panels into 33 A4 pages. Unique analysis and all 47 analytical exhibits remain; removed one verbatim duplicated monitoring block. Valuation model SHA-256 unchanged. Measured total content-to-footer gap reduced 54.9%. No body-font reduction.

Defects found and fixed: nested header bands overflowed the new wrapper on screens; first-row-only question-table opening; a page lost its tighter spacing when a later block moved, causing one footer collision; repeated '(continued)' label. Final PDF print metrics show zero collisions and overflows. Final desktop/mobile checks show zero issues and errors; six images loaded at both interaction-check widths. Every revised PDF page was opened at full size; all mobile contact sheets inspected. Original source and numerical checks retained and final identities/hashes rerun.

Final evidence: qa/visual-revision/final-page-01.jpg through final-page-33.jpg; qa/pw/; qa/print-metrics.json; qa/visual-revision/layout-comparison.json. Build order: build_report.py, refine_layout.py, paginate-report.mjs, print-report.mjs, package_report.py, visual review and verify_delivery.py.
