# Amanta Healthcare report: prompt execution audit

**Review basis:** current 37-page report composition in `report_content.py` and `page-specifications.json`, checked against the saved research prompt (`prompts/Amanta Healthcare Research Prompt.md`). The report follows the prompt's S1–S20 architecture and answers all 15 original questions on report pages 34–35; page 37 adds the evidence key and source index. The report reflects the later expanded evidence instruction: FY26 annual report, four available historical calls and four presentations, announcements and dated market data are used in addition to the latest Q2 FY27 call. That expansion supersedes the prompt's original latest-call-only restriction; the prompt file itself remains unchanged.

Report page numbers below are the `page` values in `page-specifications.json` (37 entries). Q2 call locators in the report are intended as **physical PDF pages**, consistent with `build_report.py` and the rendered source notes. The physical PDF has a filing cover; printed transcript page *n* is physical PDF page *n+1*.

## S1–S20 destination map

| Prompt section | Report pages | Execution / coverage | Remaining gap or qualification |
|---|---:|---|---|
| S1. Why read / snapshot | 1–2 | Executive thesis, key evidence, dated price and conditional valuation context, watch items and missing-input limits. | Market expectations are not reverse-engineered; price-based values are scenarios rather than a rating supported by a complete cash/debt bridge. |
| S2. Business simply | 3 | Plain-language sterile-products model, product qualification-to-cash chain and business mechanism. | No explicit ₹100-of-sales waterfall; the cost/profit/cash explanation is elsewhere in the financial section. |
| S3. Platforms and products | 4–5 | Product mix, SteriPort/ISBM, BFS/SVP, inhalation, ophthalmics, product statuses, transfer and market gates; pipeline-count ambiguity retained. | Product-country approval and molecule-level revenue/margins are not complete; named customer/licensee contracts remain undisclosed. |
| S4. Segments / entities | 6 | Separates therapeutic, platform, geography and channel views; warns against adding overlapping sales descriptions. | No product-level operating profit is disclosed, so no segment margin allocation is made. |
| S5. Customers / partners | 7 | Channel network, hospital conversion and absence of disclosed named product customers. | Customer names, contract terms, concentration and reorder history are not disclosed in sources reviewed. |
| S6. Moat / competition | 8 | Sterile process/access differentiation, claims and counterpoints, product cost and competitors. | No independent share, switching-cost or comparative safety dataset; several moat statements are management-reported. |
| S7. Quantity vs quality | 9 | Distinguishes installed/plantwide/new-line utilization, qualified output, mix and cash quality. | Line-specific sold units and net incremental contribution are still unavailable. |
| S8. Line 3 commercial test | 10 | ₹60cr FY27 estimate versus ₹110cr optimal annual potential, with partial-year/cannibalization caveats. | No disclosed output-to-revenue or old-line displacement bridge. |
| S9. Capacity, capex and cash | 11–12 | Separate SteriPort, SVP and solar timelines/cost/funding mechanisms; delivery dates and solar economics. | Project-level spent-to-date, return/payback and complete cash funding bridges are not consistently disclosed; estimates remain explicitly conditional. |
| S10. Management | 13 | Ownership, governance, related-party and communication evidence with WATCH framing. | Some independence, compensation and verification matters remain not verified where the disclosed source set has no evidence. |
| S11. Claims / delivery register | 14 | Historical expected-versus-later actual tracker across calls and disclosures; no simplistic promises-met percentage. | Management's commissioning retrospective and “about five months late” do not establish independent event verification. |
| S12. Guidance | 15 | Speaker/period-qualified current targets, two-year aim, FY27/FY28 ambiguity and near-term outlook. | The CEO's ₹420–430cr “annualized” then “full-year” FY27 wording is unresolved; it is not normalized into one clean promise. |
| S13. Growth / triggers | 16 | Separates volume, mix, licensing, export, solar and automation paths; dates and proof gates. | Monetary impact and catalyst strength remain limited where the sources give no quantified bridge. |
| S14. Peers | 17 | Capability/economic comparison and appropriate peer limitations. | Not a full peer valuation or clean comparable multiple set; only cited, source-supported comparisons are used. |
| S15. Reality vs optionality | 18 | Operating assets, work-in-progress, registrations, licensing and speculative projects are separated. | Pipeline value is not booked as established revenue. |
| S16. Causal chain | 19 | Tracks mechanism from installation through qualification, sale, margin and cash; identifies unproven links. | No product-specific audited contribution or customer conversion dataset. |
| S17. Financials / earnings quality | 20–24 | Q2/H1 earnings bridge, longer quarterly and annual trends, cash conversion and leverage. | Cash-flow, net-debt and repayment bases remain dependent on reconciled filing data; no customer/product allocation is inferred. |
| S18. Governance / verification | 25 | Audit, control, related parties and disclosure watchpoints. | External checks not available or outside the frozen report sources remain marked as such. |
| S19. Risks / anti-thesis | 26–27 | Downside mechanisms, contrary evidence and falsification signals. | Per-share risk impacts and precise probability estimates are not supportable without additional inputs. |
| S20. Valuation / verdict | 28–36 | Scenario method and cases, funding bridge, sensitivity, 15 Q&A responses and final WATCH/valuation-sensitive conclusion. | Scenario outputs are conditional, not a price target; assumptions and missing inputs are stated. |

## Original 15 questions: response locations

| # | Prompt question (short form) | Report page | Assessment |
|---:|---|---:|---|
| 1 | Line 3 commercial change / full ramp | 34 | Answered: capacity is a volume opportunity; 20 November is a target; realized sales, yield and cash remain to be proved. Add a source locator for the capacity increment (see locator audit below). |
| 2 | ₹60cr FY27 vs ₹110cr annual potential | 34 | Answered: partial-year contribution versus optimal annual revenue; 54.5% ratio is explicitly not physical utilization; cannibalization not disclosed. |
| 3 | Solar net saving after financing/depreciation | 34 | Answered qualitatively; no project-specific net profit/cash bridge. Locator should include the latest call's ₹9cr annual power-saving statement (physical p.5). |
| 4 | Q2 sales/EBITDA/PAT conversion | 34 | Answered with reported values and financing/depreciation bridge. |
| 5 | SVP capacity and physical units / Q1 FY28 | 34 | Answered arithmetically; preserve the call/deck difference (call says ~20.9 to ~31; deck says 20.9 to 31.7). Cite the capacity statement and the deck, not only call physical p.5. |
| 6 | 20%+ CAGR aspiration vs 12% H1 growth | 34 | Answered without turning the aim into annual guidance. |
| 7 | Required margin drivers and timing | 34 | Answered as mechanisms and offsets, without unsupported timing precision. |
| 8 | Development-to-approval/licensing/sales gates | 34 | Answered. Broader source locator should include pipeline/product and post-commission transfer/filling claims, not only one filing page. |
| 9 | Six inhalation / two commercial / additional six ambiguity | 35 | Conclusion is correct, but cited Q2 call physical p.13 does **not** contain the six/two/additional-six wording; it is on physical p.5. Correct this locator. |
| 10 | 32% international revenue and demand vs registration | 35 | Answered; add Q2 call physical p.4 for the 32% statement alongside the deck locator if retaining latest-call attribution. |
| 11 | Funding SVP, working capital and debt service | 35 | Answered from cash flow and management borrowing/repayment data; no self-funding conclusion is overstated. |
| 12 | Debt/equity decline and IPO equity effect | 35 | Answered with annual-report balance-sheet context and no false debt-retirement inference. |
| 13 | ₹420–430cr and ₹400–420cr FY28 wording | 35 | Correctly flags ambiguity and does not collapse the figures; citation should include Q2 call physical p.14 for the analyst's FY28 question and CEO confirmation, as well as p.10 for ₹420–430cr. |
| 14 | ₹190cr borrowing, net debt and repayment | 35 | Answered with a later exact borrowing reconciliation, but cite Q2 call physical p.6 for Paras Mehta's approximate ₹190cr / ₹45cr working-capital answer. |
| 15 | First thesis-break risks / no target-price limits | 35 | Answered as analyst judgment and supported by operating/cash risks; consider linking the cited Q2 physical p.14 SVP risk to physical p.7 utilization and the official cash-flow source. |

## Primary-source locator review: Q2 FY27 transcript

The following transcript locators were checked against the text's `PHYSICAL PDF PAGE` markers and page contents. These are certain locator changes for the rendered references; page numbers are physical PDF pages, not printed page numbers.

| Claim currently in report content | Checked source location | Finding / recommended locator |
|---|---|---|
| Line 3 operational, capacity 6.6 to 11.6cr / roughly +75% | Q2 call physical p.3; Q2 deck physical p.5 | Correct evidence exists. Q&A answer 1 presently cites only call p.7, which supports utilization/ramp rather than the capacity increment; add physical p.3 and/or deck p.5. |
| ₹60cr FY27 and ₹110cr at optimal utilization; solar ₹9cr annual saving | Q2 call physical p.5 | Both estimates are stated here. Q&A answer 2's p.5 is correct; answer 3 currently cites annual-report p.12 only and should add Q2 call p.5. |
| SVP capacity increase and Q1 FY28 timing | Call physical p.4 says 20.9 to roughly 31 and ~52%; Q2 deck physical p.5 says 20.9 to 31.7cr units | Keep the cross-document discrepancy visible. Q&A answer 5 currently cites only call p.5, which supports the planned start, not capacity figures; add call p.4 and deck p.5. The call's “crores” capacity units are not unambiguously physical; deck provides the “units” wording. |
| Plantwide 95–97%, Line 3 ~55%, Nov. 20 full-utilization target | Q2 call physical p.7 | Supports the utilization comparisons. Physical p.9 also repeats that the line is 52–55% and full capacity from Nov. 20. |
| Pipeline count: six inhalation, two commercialized, additional six; 20 total | Q2 call physical p.5; physical p.13 separately says F&D working on 20 products and discusses budesonide validation/transfer | Q&A answer 9 currently cites p.13 only. Change/add p.5 for the six/two/additional-six ambiguity; retain p.13 only for the separate 20-product and budesonide statements. |
| International revenue ~32% | Q2 call physical p.4 | Latest-call source locator for 32% is p.4. |
| ₹420–430cr FY27 wording | Q2 call physical p.10 | CEO first calls ₹420–430cr an annualized run-rate, says Q3/Q4 should reach the same rate, then says ₹420–430cr on a full-year basis. The ambiguity is real and should remain. |
| FY28 ₹400–420cr question / inclusion of SVP; SVP revenue not quantified | Q2 call physical p.14 | Add this physical page to Q&A answer 13. The question is asked by an analyst; CEO confirms it includes SVP but does not quantify that contribution. Page 14 also forecasts 45–50% initial utilization and says no new-line revenue estimate has yet been simulated. |
| Approximate September borrowing answer | Q2 call physical p.6 | CFO says total borrowing ~₹190cr including ~₹45cr working capital, term balance ~₹150cr, FY27-end ~₹175–180cr, and repayments ~₹30–32cr, later saying ₹35cr annually. Q&A answer 14 should cite p.6 alongside exact filing reconciliation. |

**Cross-check of all Q2 call references in page specifications:** pages 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 and 15 are used as physical-page citations. Page 16 is the cover/closing page, not the source for management's key numerical claims. The page-specific citations should be reviewed for the fixes above before final rendering.

## Requirements that remain unavailable or deliberately limited

- Actual SteriPort line sales by month, produced/sold units, realized price, yield, line-specific margin and cannibalization are not disclosed; the report labels the incremental-revenue bridge as an assumption.
- Product-level approvals, molecule/customer contracts, repeat demand and license economics are absent. A development pipeline or registration count is not recognized as sales.
- SVP capacity units are inconsistent across call/deck wording; unit arithmetic is shown with attribution rather than silently normalized.
- The solar ₹9cr is an annual gross power-cost saving estimate. The record does not isolate project net profit, depreciation, metered savings or cash after its financing cost.
- Exact period attribution for the ₹420–430cr figure remains ambiguous within the Q2 call. FY28 ₹400–420cr came from the analyst's question and was confirmed to include SVP, with no segment bridge.
- No validated customer concentration, product-specific profitability, detailed registration calendar, or per-share risk impact is available.
- Valuation scenarios rely on analyst assumptions for future revenue, margin, working capital, capex, funding and multiples. They are conditional illustrations, not a supported target price or definitive rating.

Page 37 extends the source/index appendix; it does not change the S1–S20 or Q&A page assignments. The report is structurally complete for S1–S20 and all 15 questions, subject to the locator corrections above. This audit did not modify `build_report.py` or the generated report.
