# Amanta Healthcare: verification summary

Prepared 10 November 2026. Evidence cut-off and price date: 9 November 2026. Standalone statements; INR crore unless specified.

## Deliverable and prompt execution

The revised PDF has **33 pages, 47 analytical exhibits, two product galleries with six official photographs, 20 section bookmarks and 440 clickable links**. The saved research prompt was executed without rewriting it. Its S1–S20 sequence and all 15 original research questions are covered; all question answers are on page 31. The user's later instruction expanded the original call-only source scope. The original prompt hash and per-page source groups are preserved in the source manifest.

The research corpus contains 16 issuer PDFs: the FY26 annual report, all four historical calls and four matching decks found in the official archive, official H1 results, and six material commissioning, monitoring, management and rating disclosures. A peer rating PDF, an official peer capability page and four dated market/secondary snapshots make 22 research records. The visual revision adds six original product images and four official catalogue HTML snapshots, bringing the manifest to **32 source records**. Images illustrate representative current packs, not future-line output or country approvals. Local copies, original URLs and SHA-256 hashes are included. Older publicly listed calls were not located; archive coverage is not proof that no other call exists.

## Financial and source checks

- Reconciled FY25/FY26 audited statements to annual-report PDF pages 52–53 and EPS/share-count notes. Converted original INR lakhs to crore by dividing by 100.
- Read the scanned official H1 results visually, including P&L, balance sheet, cash flow and exceptional-item note on physical pages 3–7. Q1 plus Q2 revenue and PAT reconcile to H1.
- Reconciled September borrowings ₹194.5582cr + leases ₹9.3255cr − cash ₹1.6660cr = **cash-only net debt ₹202.2177cr**. Other bank balances are separately identified and excluded from opening net debt.
- Verified the official NSE 9 November closing price **₹202.15**, rather than the different last-traded price. Current issued shares are **38,829,351**, from annual-report physical page 59.
- Corrected prior-period ex-other-income EBITDA to ₹14.6505cr for Q2 FY26 and ₹29.5439cr for H1 FY26. Distinguished company EBITDA including other income from operating EBITDA throughout. The IPO expense reduces FY26 PBT; it is not an operating improvement.
- Compared all four calls and decks for dated project, sales and margin statements. Preserved the Q2 call's annualised/full-year revenue ambiguity and the analyst-originated FY28 question. The ₹16cr SVP contribution remains explicitly speculative.
- Independently checked a ten-claim primary-source sample covering capacity, utilization, solar, ownership/remuneration, financial statements and contingencies. Corrections include annual-report utilization, geography, solar and share-count page locators. This is a sample review, not an external audit of every issuer claim.

An independent second calculation re-derived **all nine scenario-year rows**, including revenue, operating profit, interest, depreciation, tax, PAT, working capital, cash/capex funding, net debt, EV, equity and per-share values. Differences were below 1e-8. The visual revision preserves the valuation-model file byte for byte (SHA-256: 61f60279941bd932b290b8afc2d6469c0dc97d7f1fb6c6e20d4bd656e9a25226). A separate delivery script verifies model identities, source/output hashes, embedded photo counts and all 33 PDF page numbers.

| FY28E, 31 March 2028 | Bear | Base | Bull |
|---|---:|---:|---:|
| Revenue, ₹cr | 380.68 | 413.68 | 454.94 |
| Operating EBITDA, ₹cr | 79.94 | 103.42 | 122.83 |
| Closing net debt incl leases, ₹cr | 180.55 | 161.05 | 150.25 |
| EV/operating EBITDA | 11x | 14x | 17x |
| Conditional value, ₹/share | 179.97 | 331.40 | 499.08 |

These are undiscounted future scenario values, not a current fair-value estimate or price forecast. Incrementality, margins, funding, WC, capex and multiples are estimates. FY27's cash bridge is H2 only; the first half is not charged twice. Solar is embedded in margins once. The model is a P&L/net-debt bridge, not a fully balanced three-statement forecast. No new equity, dividends or lease additions are assumed. Interest and tax cash use employ accrual proxies.

## Design and visual verification

Studied actual MQ reference pages 1, 2, 4, 5 and 6 and the BF capacity reference visually. Retained the MQ Arial typography, blue/grey palette, grey headline band, summary/data rail, compact striped tables, conclusion-led narrative and dense white field. Borrowed the BF capacity-tracker mechanism. The report is expanded for the wider research scope; it is not a pixel-identical replica or a report issued by either reference broker.

Executed:

```text
node tools/report-visual-check/review.mjs research/companies/nse-amanta/report/report.html research/companies/nse-amanta/report-work/qa/pw
node research/companies/nse-amanta/report-work/print-report.mjs
python research/companies/nse-amanta/report-work/render-pdf.py
node research/companies/nse-amanta/report-work/check-delivery.mjs
python research/companies/nse-amanta/report-work/verify_delivery.py
```

Final automated desktop (1280px) and mobile (390px) results: **33 pages each, zero flagged issues, zero console errors**. Separate 1440px desktop/390px touch checks confirm working section navigation, normal scrolling, six loaded images, two galleries, complete numeric-cell labels and no page-wide horizontal overflow. Print checks show **zero overflowing pages or footer collisions**. The PDF contains selectable text, original-source links, metadata and section bookmarks.

The original report was reviewed across three reviewers. For this revision, the primary agent inspected every revised PDF page at full size, all mobile contact sheets, and the product galleries. The review corrected a single-row opening in the question table, a footer collision, nested headline-band overflow and a duplicated continuation label. Large financial tables become labeled rows on phones while retaining their institutional table layout in the PDF. Review logs and rendered evidence remain under `report-work/qa/`.

### Visual revision requested by the user

Official photographs are grouped beside the product discussion: SteriPort/ISBM and conventional FFS on page 4; respiratory, ophthalmic and diluent packs on page 5. Captions identify the category, and source links sit directly below each gallery. Images preserve their aspect ratio and are embedded in both the portable HTML and PDF.

Content was reflowed from 37 to 33 A4 pages with tighter spacing, compact secondary headings, repeated table headers on continued tables and balanced use of existing charts. Body fonts were not reduced. One verbatim duplicate monitoring block was removed; its complete copy remains after the final question. Unique analytical content, all 15 answers, all 47 analytical exhibits and every valuation assumption remain. The paginator checks that its input text survives pagination unchanged, ignoring only whitespace and generated repeated headings.

Measured bottom-of-content gaps fell from 5,715.80 to 2,576.80 CSS print pixels in aggregate, a **54.9% reduction**. This measures the vertical gap to the footer, not every white pixel in the report. No page has a bottom content gap above 206 pixels; the densest pages retain clear footer separation. Before/after evidence is in `report-work/qa/visual-revision/layout-comparison.json`.

## Explicit evidence limits

- FY25 secondary quarterly PAT totals ₹12.14cr versus audited annual PAT ₹10.5007cr, an unreconciled ₹1.6393cr difference. Page 19 identifies this directly; older quarters are indicative context. Audited annual figures control the valuation.
- Line-specific sold units, net realization, displacement, product margins, binding orders, detailed qualification calendars and metered solar project net profit are not disclosed. They are not fabricated.
- The direct 6 November promoter-purchase filing was not retrieved. Page 23 qualifies the secondary summary and does not use it to infer conviction or a market-price purchase.
- BSE annual-report/live NSE quote access failed; official company-hosted financial documents and the official NSE archived closing-price file were recovered. The separate remuneration PDF was identified; remuneration evidence is supplied by the annual report and AGM disclosure.
- Company claims about technical superiority, market share and pipeline potential remain attributed claims. A registration, installed machine or distributor count is not equated with an order, sale or cash receipt.

Not investment advice. These conditional scenarios and the verification work are not a licensed financial-adviser opinion or an external audit.


## Click navigation update - 10 November 2026

Added a 20-section clickable index on the first page and Contents / Previous / Next controls in every page footer. Verified all 119 new internal destinations, checked every rendered page for layout changes, and confirmed no navigation overlap with existing text. The report remains 33 pages; analysis, imagery, and valuation model are unchanged. Source manifest output hashes have been refreshed. Reproduction: print-report.mjs, package_report.py, verify_delivery.py, verify_navigation.py.

