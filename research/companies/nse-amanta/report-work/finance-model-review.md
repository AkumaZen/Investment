# Review of `build_report.py` financial model

Reviewed the model prefix and executed `make_model()` without executing or depending on `report_content.py`. No changes were made to the build script. Scenario outputs below are mechanical outputs from its current assumptions, not forecasts.

## Main issue to resolve: H1 working capital is included twice in FY27 cash flow

`wc_open` starts from the actual Sep-26 operating working-capital balance (inventory + receivables - payables - contract liabilities = ₹89.77 crore). The FY27 `wc_add`, however, applies 141 days to the entire FY27 revenue increase over FY26. That full-year increase already includes H1 working capital absorbed before the Sep-26 opening balance.

Using the same balance-sheet items, Mar-26 operating working capital was ₹80.96 crore and Sep-26 was ₹89.77 crore, an increase of about ₹8.80 crore during H1. The Base case currently charges the full ₹23.18 crore FY26-to-FY27 incremental working-capital requirement again after the Sep opening point. If 141 days is intended as a marginal working-capital ratio on the annual sales uplift, the FY27 post-Sep add should first subtract the H1 increase already embedded in Sep working capital: approximately ₹14.38 crore. This would raise FY27 modeled cash flow by about ₹8.80 crore and reduce Sep-to-year-end net-debt growth by the same amount. The same adjustment is scenario-specific because the actual H1 WC movement is fixed across cases.

Minimal fix: compute the full-year working-capital increase versus FY26 and subtract the actual Mar-to-Sep change from that amount for FY27, while preserving subsequent-year deltas. Alternatively, keep the current conservative amount but label it as a deliberate stress assumption and include its effect in sensitivity. Do not claim the current formula normalizes opening working capital to the September sales run-rate: the code never calculates that run-rate.

There is a separate denominator limitation: the AR's 141 net-working-capital-days metric does not reconcile directly to the simple balance-sheet operating-WC definition above. The forecast therefore needs to label 141 days as an analyst proxy and show at least a lower and higher days sensitivity; it should not be presented as an issuer-defined cash-conversion formula.

## Cash-flow bridge and debt treatment

- **No EBITDA/depreciation double count found.** PBT uses operating EBITDA + other income - finance cost - depreciation. Cash available then starts from operating EBITDA, subtracts interest, cash tax proxy, working-capital increase and capex. Depreciation is noncash and is correctly omitted from this cash bridge while remaining in PBT/tax.
- **Opening net debt reconciles.** At 30 Sep 2026, borrowings of ₹194.5582 crore plus lease liabilities of ₹9.3255 crore less cash equivalents of ₹1.6660 crore equals approximately ₹202.2177 crore. The code's `net=202.2177` is correct. Screener's ₹204 crore borrowings include lease liabilities; the audited borrowings line does not. Other bank balances of ₹25.1308 crore are excluded from opening net debt.
- **Restricted cash release is not inherently double counted.** `release=[15, 8, 0]` lowers net debt because the opening net-debt calculation excludes other bank balances. FY26 and interim filings show IPO-related cash/deposits restricted to capex. This treatment is coherent only if the scenario labels ₹15 crore and ₹8 crore as assumed future use of currently excluded restricted funds, separate from operating FCF. It must not be described as earnings or free operating cash. The total ₹23 crore assumed release should be shown against the disclosed Sep balance and monitored IPO proceeds; any unspent remainder stays excluded from cash in the model.
- **Interest and tax use accruals where the bridge is described as cash.** FY27 annual interest expense and tax are reduced by H1 P&L accruals (`H1['interest']`, `3.1471`) to derive H2 cash costs. The official H1 cash flow reports ₹10.6543 crore of interest-related/borrowing-cost payments versus ₹11.8490 crore finance expense, and ₹1.7562 crore tax paid versus ₹3.1471 crore tax expense. This is a reasonable accrual-based shortcut for P&L, but it is not an actual cash bridge. Minimal fix: either label FY27 `cashop` as an accrual proxy, or subtract H1 cash payments from projected full-year cash-interest and cash-tax assumptions. Keep accrued interest/depreciation in PBT.
- **Lease principal is omitted from future cash use.** The model includes lease liabilities in opening net debt but does not pay them down. FY26/H1 show principal lease payments (₹2.1720 crore FY26; ₹1.0329 crore H1 FY27). Holding lease debt flat can be a conservative simplifying assumption; state it or add scheduled lease-principal amortisation and roll the liability down consistently.
- **No separate principal-repayment line is required if net debt is a cash-flow roll-forward.** The model applies post-interest/post-tax FCF against net debt. Principal repayment changes gross debt and cash by the same amount, so it is already reflected in net debt when surplus cash is swept to debt. The assumption should be explicit that net cash is applied to debt and not accumulated separately.

## Revenue and valuation conventions

1. The current annual anchors use operating EBITDA excluding other income; that matches the quarterly operating-profit series and the parent model's exit multiple base. This is distinct from the company's statutory EBITDA line, which includes other income. The code separates `op` and `oi` in PBT and calculates EV from `op`, so no double counting of other income was found.
2. Base sales are ₹347.68 crore in FY27E and ₹413.68 crore in FY28E: FY26 revenue plus assumed ₹60 crore Line 3 contribution in FY27, then ₹110 crore Line 3 contribution and ₹16 crore SVP in FY28. This is a clear, conditional interpretation of management figures, not independent guidance. It assumes these contributions are incremental to the FY26 base. The report should say so and flag displacement of existing SteriPort sales as a key downside sensitivity.
3. Exit EV uses operating EBITDA times the scenario multiple; equity value subtracts net debt; share price divides by 3.8829351 crore issued shares. Internal identity checks pass. At Base FY29, the script returns operating EBITDA ₹111.02 crore, 14x EV ₹1,554.21 crore, net debt ₹121.31 crore, equity ₹1,432.91 crore, and ₹369.03/share. These are entirely driven by assumptions: 25% margin, 9% interest rate, assumed debt/cash sweep, ₹15 crore FY29 capex, and 14x multiple.
4. The 11x/14x/17x multiples and the associated bear/base/bull returns are valuation judgments. Mark them explicitly subjective and add one sentence on what would justify a multiple change. No arithmetic defect found in return/CAGR formula; dates use 9 Nov 2026 CMP and the relevant March fiscal year-end.

## Executed outputs

Current model outputs, before any WC adjustment:

| Scenario | FY27E revenue / EBITDA | FY28E revenue / EBITDA | FY29E revenue / EBITDA | FY29E value per share | Return vs ₹202.15 CMP |
|---|---:|---:|---:|---:|---:|
| Bear (11x) | ₹327.68 / ₹65.54 cr | ₹380.68 / ₹79.94 cr | ₹404.43 / ₹88.97 cr | ₹211.41 | +4.6% |
| Base (14x) | ₹347.68 / ₹79.97 cr | ₹413.68 / ₹103.42 cr | ₹444.06 / ₹111.02 cr | ₹369.03 | +82.6% |
| Bull (17x) | ₹361.31 / ₹86.71 cr | ₹454.94 / ₹122.83 cr | ₹493.57 / ₹138.20 cr | ₹580.62 | +187.2% |

Bear CAGR from CMP to FY29 is 1.9%, Base 28.6%, and Bull 55.5%, using the fiscal year-end horizon. If the report foregrounds these returns, include a compact valuation bridge and the scenario assumptions beside them; don't let a point estimate imply precision that the model inputs do not have.
