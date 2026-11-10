# Concord Biotech: navigation verification — 10 November 2026

Completed: clickable section index, PDF bookmarks, and Contents / Previous / Next on every PDF page. The HTML edition has the same index and section controls. HTML build integration preserves navigation on future rebuilds.

- 26 physical PDF pages; 21 section destinations; 99 new PDF navigation links.
- Every PDF destination verified. All HTML section links and controls clicked at 1280px and 390px.
- Every PDF page rendered and visually reviewed; desktop and phone HTML reviewed. No navigation overlap found.
- Original HTML analytical text preserved exactly. Existing PDF text positions, images and pixels outside reserved navigation regions preserved against the clean export.
- Python compilation, idempotence and diff whitespace checks passed.
- Report analysis dates and underlying research remain unchanged. This update covers navigation only.

Repack PDF from its clean source: `python tools/report_navigation.py pdf research/companies/nse-concordbio/report/navigation.json` from workspace root. For Augmont, first create its clean PDF using `node tools/print-navigation-report.mjs research/companies/nse-augmont/v3/navigation.json`.

`verification.json` records output hashes and checks; `section-map.json` records section destinations; `browser/report.json` records automated layout checks. `clean-print.pdf` must be retained as the clean source for idempotent PDF repackaging.
