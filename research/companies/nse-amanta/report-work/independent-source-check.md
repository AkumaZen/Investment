# Independent source check — Amanta FY26 and Q2 FY27

As-of date: 10 November 2026. Sample reviewed against official company PDFs in `docs/`. Annual-report citations include both printed pages shown on each two-page spread. Q2 results are scanned single-page exhibits with no printed page numbers; cited physical PDF pages refer to the official board-outcome PDF.

| # | Requested number | Verification | Source and location | Notes |
|---:|---|---|---|---|
| 1 | FY26 revenue ₹287.6767 crore | **PASS** | FY26 Annual Report, PDF p.52, printed pp.98–99 | Statement of Profit and Loss: revenue from operations ₹28,767.67 lakh = ₹287.6767 crore. |
| 2 | FY26 PAT ₹14.8752 crore | **PASS** | FY26 Annual Report, PDF p.52, printed pp.98–99 | Statement of Profit and Loss: profit for year ₹1,487.52 lakh = ₹14.8752 crore. |
| 3 | FY26 CFO ₹48.4464 crore | **PASS** | FY26 Annual Report, PDF p.53, printed pp.100–101 | Cash flow from operating activities ₹4,844.64 lakh = ₹48.4464 crore. |
| 4 | FY26 capex cash outflow ₹80.1864 crore | **PASS** | FY26 Annual Report, PDF p.53, printed pp.100–101 | Payments for PPE, intangible assets, CWIP and capital advances ₹8,018.64 lakh = ₹80.1864 crore. This is the cash-flow line, not an assertion about accrual-basis additions. |
| 5 | Latest debt ₹194.5582 crore; leases ₹9.3255 crore; cash ₹1.666 crore | **PASS (debt and leases derived)** | Q2 FY27 Board Outcome, scanned results exhibit, PDF p.4; no printed page | Borrowings ₹4,898.88L non-current + ₹14,556.94L current = ₹19,455.82L debt. Lease liabilities ₹743.43L + ₹189.12L = ₹932.55L. Cash and cash equivalents ₹166.60L; excludes other bank balances of ₹2,513.08L. |
| 6 | IPO proceeds utilized ₹74.9543 crore | **PASS** | September 2026 Monitoring Agency Report, PDF p.9; printed p.9 | CRISIL report quotes certified/management-undertaking-based utilization of ₹7,495.43 lakh at 30 Sep 2026. It separately gives ₹4,766.36 lakh as at FY26 close. The report does not independently audit/verify the underlying utilization. |
| 7 | Solar project cost ₹34.8 crore | **PASS** | FY26 Annual Report, PDF p.12, printed pp.20–21 | The page states ₹34.8 crore total project cost, ₹5.8 crore equity outlay, ₹9 crore expected annual saving and 3.6-year pre-interest payback. These are management-reported project economics, not audited FY26 cash payment / realized savings. |
| 8 | Shares outstanding 38,829,351 | **PASS** | FY26 Annual Report, PDF p.59, printed pp.112–113 | Note 18 share capital: issued, subscribed and paid-up shares at 31 Mar 2026. |
| 9 | SteriPort capacity 11.6 crore bottles | **PASS (management claim)** | Q2 FY27 Investor Presentation, PDF p.5, slide 3; no two-page spread | Presentation says capacity rose from 6.6 crore to 11.6 crore bottles after Line 3 commissioning. This is company-reported capacity. |
| 10 | SVP capacity 31.7 crore units | **PASS (management target)** | Q2 FY27 Investor Presentation, PDF p.5, slide 3; no two-page spread | Presentation says capacity is to rise from 20.9 crore to 31.7 crore units during Q1 FY28. This is a forward-looking target, not installed capacity at 30 Sep 2026. |

## Auditor name check

The annual report's exact statutory auditor name is **Price Waterhouse Chartered Accountants LLP** (FRN 012754N/N500016), not the shortened “PwC Chartered Accountants LLP.” The exact name appears in the annual report's corporate information (PDF p.15, printed pp.26–27) and audit report/signature pages (e.g. PDF p.52, printed pp.98–99). “PwC” may be used only as an informal brand shorthand; for formal firm identification, use the legal name.

## Draft audit: `report_content.py`

- Corrected the annual report chart's LVP FY24 utilization from 94% to **93%**, after visual inspection of annual-report physical PDF p.10 (printed pp.16–17). The SVP and SteriPort chart series match the source.
- Corrected the solar citation to annual-report physical PDF p.12 (printed pp.20–21). Physical p.10 is manufacturing infrastructure and does not contain the solar project cost.
- Corrected the geography-note citations to annual-report physical PDF p.75 (printed pp.144–145); physical p.74 (printed pp.142–143) supports the customer credit-risk concentration statement.
- Corrected the issued-share-count citation to annual-report physical PDF p.59 (printed pp.112–113), where Note 18 directly states 38,829,351 shares.
- Confirmed physical PDF p.54 (printed pp.102–103) states there are no subsidiaries, joint ventures or associates; p.42 (printed pp.78–79) reports CMD remuneration; p.70 (printed pp.134–135) has related-party disclosure; p.65 (printed pp.124–125) has disaggregated product revenue.
- Report source notes currently display physical PDF page locators. If the parent report needs the printed-page pair beside every annual-report citation, that formatting still needs to be added; the PDF-to-printed-page mapping is not uniform enough to infer from a simple formula.

## Scope note

The Q2 balance-sheet numbers above were checked visually against the scanned official exhibit image, not accepted solely from OCR text. All 10 sampled items reconcile. The current report-content draft was also checked for the annual-report citation and utilization corrections listed above; other narrative or non-annual-report sources were not comprehensively fact-checked.
