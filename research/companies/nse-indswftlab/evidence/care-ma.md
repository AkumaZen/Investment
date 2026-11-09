# Evidence: CARE monitoring agency reports on preferential issues

Sources (BSE filings, filed by the company on 3 Nov 2026):
- Final report on the first warrant issue, text `docs/INDSWFTLAB/text/care-ma-final.txt` (BSE e0af5fc1-e457-4aa2-abdd-655b65463742). Tag [CARE-F pN].
- Q2 FY27 report on the second warrant issue, text `docs/INDSWFTLAB/text/care-ma-q2fy27.txt`. Tag [CARE-Q2 pN].
- [NSE-A] NSE filing, allotment of warrants, 17 Sep 2026: https://nsearchives.nseindia.com/corporate/INDSWFTLAB_17092026174502_Outcome_Allotment.pdf (local `docs/INDSWFTLAB/raw/nse-warrant-allotment-17sep26.pdf`).
- [NSE-C] NSE filing, conversion of 14 lakh warrants, 8 Oct 2026: https://nsearchives.nseindia.com/corporate/INDSWFTLAB_08102026183706_Committee_Meeting_Outcome_08102026.pdf (local `docs/INDSWFTLAB/raw/nse-warrant-conversion-08oct26.pdf`).
Rs crore. Read by Claude in this session; no worker model.

## Issue 1: warrants at Rs 121, allotted 30 Aug 2024

- Promoter: Mr. Navrattan Munjal [CARE-F p4].
- Fully convertible warrants, 18 months to convert; issue size Rs 314.60 cr [CARE-F p4]. 2,60,00,000 warrants x Rs 121 = Rs 314.60 cr [E], PASS.
- Saral Incorporated VCC Sub Fund 1 "did not exercise the option to convert 65,00,000 warrants within the stipulated period of 18 months ... (on or before February 28, 2026)"; the warrants lapsed, "resulting in shortfall in overall funds-raising of Rs.58.99 crore" [CARE-F p8, p10].
  Check: 65,00,000 x Rs 121 x 75% = Rs 58.99 cr [E], PASS; so the 25% upfront of about Rs 19.66 cr was forfeited to the company [E].
- Proceeds fully used by 30 Sep 2026, including Rs 3.77 cr in Q2 FY27 [CARE-F p8].
- Commingling: "While we have reviewed the bank statements, the commingling of funds (mixing proceeds with other cash flows) has limited our ability to directly ascertain" end use for some payments [CARE-F p5, p10].
- Land: "the company acquired 40 bighas (~10 acres) of land in January 2025 at village Behra, Derabassi, Punjab, using the issue proceeds for setting up of a formulation's manufacturing facility" [CARE-F p10].
  It was "subsequently found unsuitable for establishing a finished dosages facility" and sold in Aug 2026 "for a consideration of Rs.17.50 crore (at loss of Rs.0.22 crore)", with only Rs 1.96 cr received as advance, moved to the issue account and used [CARE-F p5-p6, p10].
  The buyer is not named in the report. Rs 15.54 cr of the consideration is still to be received [E].
- Deviation: "No, there is no major deviation observed" [CARE-F p6], apart from the shortfall caused by the lapse [CARE-F p7].

## Issue 2: warrants at Rs 196, allotted 17 Sep 2026

- Fully convertible warrants; 18 months to convert; issue size Rs 137.20 cr [CARE-Q2 p4]. Rs 137.20 cr / Rs 196 = 70,00,000 warrants [E].
- Raised so far: Rs 34.30 cr (25% upfront) [CARE-Q2 p8, p10].
- Objects [CARE-Q2 p7]: expansion of the existing facility and warehouse, R&D and technology upgrade Rs 41.40 cr (with R&D Rs 2.00 cr inside it); investment in subsidiary Rs 5.00 cr; working capital Rs 53.00 cr; general corporate purposes Rs 34.30 cr. Sum Rs 133.70 cr plus issue-related items to Rs 137.20 cr [E; the residual Rs 3.50 cr line was not re-checked].
- Used in Q2 FY27: expansion Rs 6.315 cr, R&D Rs 0.335 cr, ISLL Middle East L.L.C-FZ Dubai Rs 4.853 cr, working capital Rs 3.989 cr, general purposes Rs 0.108 cr [CARE-Q2 p8-p10].
- Expansion completion date stated as 31 Dec 2029; no deviation reported [CARE-Q2 p5].
- Allottees: not named in the CARE report. The NSE allotment filing names one allottee: Essix Biosciences Limited, "Promoter & Promoter Group", all 70,00,000 warrants at Rs 196 (premium Rs 186), Rs 49 per warrant upfront, Rs 34.30 cr [NSE-A 17 Sep 2026].
- Conversion: on 8 Oct 2026, 14,00,000 warrants were converted into equity shares for Essix on receipt of the 75% balance of Rs 147 per warrant, Rs 20.58 cr; paid-up capital "increased from" 8,67,11,558 to 8,69,61,558 shares [NSE-C 8 Oct 2026].
  Check: 8,69,61,558 - 8,67,11,558 = 2,50,000 shares, not 14,00,000 [E]. The filing's own before and after counts do not reconcile with the shares it says it allotted.
  Resolution [Inferred]: the Q1 FY27 deck (Aug 2026) already shows 8,69,61,558 shares before this conversion [D-Q1], and Sep-26 share capital of Rs 86.96 cr [deck p30] equals the same count. 8,69,61,558 - 8,68,36,558 (31 Mar 2026 [AR26]) = 1,25,000, matching the remaining ESOP 2014 options [AR26 audit emphasis of matter]. So the filing's before and after figures look stale, and shares after 8 Oct are likely 8,69,61,558 + 14,00,000 = 8,83,61,558 [E]. The Q2 deck p31 (2 Nov) still shows 8,69,61,558, so this stays a disclosed data conflict.
- Circular flow: Ind-Swift holds 15,35,000 Essix shares at Rs 28.85 cr [AR26 p80], while Essix funds the company through warrants [Inferred governance point for S10 and S18].

## Model consequences

- Shares outstanding after the 8 Oct 2026 conversion: 8,83,61,558 [E, Inferred], against 8,69,61,558 printed in the filing and the Q2 deck (data conflict, see above).
- Warrants still outstanding: 70,00,000 - 14,00,000 = 56,00,000 [E].
- Diluted share count used in the model (conservative): 8,83,61,558 + 56,00,000 = 9,39,61,558 [E]. Sensitivity: 9,25,61,558 if the printed 8,69,61,558 is right.
- Market value for the price check still uses 8,69,61,558 x Rs 349 = Rs 3,035 cr, the count Screener and the deck use.
- Cash received on issue 2 so far: Rs 34.30 cr + Rs 20.58 cr = Rs 54.88 cr [E]; the Rs 20.58 cr came in after 30 Sep 2026, so it is not in the H1 balance sheet.
- Cash still to come if the rest convert: 56,00,000 x Rs 147 = Rs 82.32 cr [E].
- At Rs 349 the warrants are in the money by Rs 153 a share; the promoter has already converted 20% within three weeks [E].
- Pending land receivable Rs 15.54 cr is not counted in net cash.

## Capital raised since the merger (for S18)

| Item | Rs cr | Source |
|---|---|---|
| Issue 1 raised (Rs 314.60 cr less Rs 58.99 cr lapsed) | 255.61 | CARE-F p8 [E] |
| Of which promoter (Essix), full FY26 conversions | 96.80 (80 lakh x Rs 121) | AR26 p40 [E] |
| Issue 2 raised to date (upfront Rs 34.30 cr plus 8 Oct conversion Rs 20.58 cr) | 54.88 | CARE-Q2 p8; NSE-C [E] |
| Issue 2 still to come | 82.32 | [E] |

Why a company with about Rs 348 cr of net cash and a Rs 250 cr capex plan funded "from internal accruals" [deck p3] raised Rs 137.20 cr more in Sep 2026 is not explained in the documents read. This goes to S18 as an open question.
