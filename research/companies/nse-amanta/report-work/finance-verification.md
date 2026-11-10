# Financial model verification

## Result

I independently recalculated all three scenario paths for FY27E–FY29E from the published `report/valuation-model.json` and matched every stored result to less than 1e-8. Reconciled formulas: sales = legacy + Line 3 + SVP; operating EBITDA = sales × margin; PBT = operating EBITDA + other income − interest − depreciation; PAT = PBT − tax; EV = operating EBITDA × exit multiple; equity = EV − net debt; per-share value = equity ÷ 3.8829351 crore shares. The report builder was not executed. Detailed checks are in `finance-verification.json`.

## Working capital and FY28 value

Opening net debt is ₹202.2177 crore (₹194.5582 crore borrowings + ₹9.3255 crore lease liabilities − ₹1.6660 crore cash). Operating WC is ₹80.9638 crore at March 2026 and ₹89.7662 crore at September 2026. Base-case FY27 incremental WC is ₹14.3757 crore, using March WC plus the full FY27 sales increment at the assumed 141 days and charging only the difference from September opening WC in H2. Base FY28 WC addition is ₹25.4959 crore and FY29 is ₹11.7373 crore. The previous full-year-growth double count is absent.

| FY28E | Sales (₹cr) | Operating EBITDA (₹cr) | Net debt (₹cr) | Value/share (₹) |
|---|---:|---:|---:|---:|
| Bear | 380.6767 | 79.9421 | 180.5490 | 179.97 |
| Base | 413.6767 | 103.4192 | 161.0489 | 331.40 |
| Bull | 454.9373 | 122.8331 | 150.2520 | 499.08 |

## Interpretation and limits

The arithmetic is internally consistent. This does not verify the assumptions as forecasts. The scenario bridge explicitly treats FY27 as H2 only, applies cash-like operating flows from accrual P&L amounts, uses separate restricted-deposit release assumptions, and holds lease liabilities static. Lease principal and future lease-liability movements are not rolled forward. Deposits and capex are separated in the bridge, so the modeled deposit release reduces operating funding required for the separately budgeted capex; avoid interpreting it as additional operating profit.

The FY23/FY24 historical operating EBITDA source values are Screener standalone “Operating Profit” rows rounded to ₹53 crore and ₹58 crore (20% and 21% margins). These are ex-other-income figures; they must not be replaced by the larger EBITDA including other income series.
