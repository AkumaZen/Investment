# Concord Biotech - gap research (9 Nov 2026)

This file closes, or narrows, the 11 known gaps listed in report/qa/qa-notes.md section 9.
Page tags are physical PDF pages of the local copies in docs/CONCORDBIO/raw (gitignored).
Each gap ends with a status: CLOSED, NARROWED or STILL OPEN.

## Sources added in this round

| Key | Document | URL | Local file |
|---|---|---|---|
| RHP | Red herring prospectus, 27 Jul 2023 (380 pages, now text-extracted) | https://www.bseindia.com/corporates/download/383248/IPO%20Open/RHP_20230802171607.pdf | raw/rhp-2023-07-27.pdf |
| STL | Intimation of investment in Stellon Biotech Inc., Jul 2025 (company website copy) | https://concordbiotech.com/wp-content/uploads/2025/07/Intimation-of-Investment-in-Stellon-Biotech-Inc.pdf | raw/ann-stellon-investment-2025-07.pdf |
| FDA483 | Intimation of USFDA inspection at Dholka, 2 May 2025 (company website copy) | https://concordbiotech.com/wp-content/uploads/2025/07/concord-USFDA-Inspection.pdf | raw/ann-usfda-inspection-dholka-2025.pdf |
| CS | Resignation of company secretary, 24 Dec 2025 (BSE filing, Business Standard mirror) | https://bsmedia.business-standard.com/_media/bs/data/announcements/bse/24122025/55d6c936-9fe4-433d-9b17-0cb45106c684.pdf | raw/ann-cs-resignation-2025-12-24.pdf |
| OB | US FDA Orange Book data files, edition with approvals up to 8 Sep 2026 | https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files | not kept (public file) |
| TL | Trendlyne shareholding pages, Dec 2023 to Sep 2026 (built from exchange shareholding filings) | https://trendlyne.com/equity/share-holding/1587026/CONCORDBIO/latest/concord-biotech-ltd | none |
| CFO | CFO early-retirement filing, 8 Dec 2025 (NSE copy located, would not load) | https://nsearchives.nseindia.com/corporate/CONCORD_08122025135843_Upload.pdf | none |
| CFO-2 | ScanX and Informist reports of the CFO filing | https://scanx.trade/stock-market-news/stocks/concord-biotech-cfo-lalit-sethi-announces-early-retirement-effective-january-2026/26728108 ; https://informistmedia.com/EquityWire/41075/concord-biotech-appoints-raviraj-karia-as-cfo-in-place-of-lalit-sethi | none |

Access limits in this round:
NSE archive PDFs timed out on every attempt (curl and web fetch).
BSE's announcement API was not used after an automated access check refused it.
The Chrome extension was not connected, so no browser session was available.

## 1. Owner of the other 25% of Stellon - NARROWED

- Stellon Biotech Inc. was incorporated in Delaware in December 2024 and was pre-revenue at the time of the deal [STL p2].
- Before the deal Stellon had issued 5,000,000 shares at USD 0.0001, a net worth of USD 500 [STL p2].
- Concord subscribed 15,000,000 new shares for USD 1,500, giving it 75% [STL p1].
  So the 25% holder owns the original 5,000,000 shares, paid USD 500 for them, and put in a quarter of the equity against Concord's three quarters.
- The filing says Concord expands in the US "through its own subsidiary with a local partner" in the US [STL p2].
- The filing says the deal is a related-party transaction only because Stellon becomes a subsidiary, and that "None of the promoter/ promoter group/ group companies have any interest in the entity" [STL p2].
- The FY26 annual report lists Stellon under "subsidiary in which directors are interested" [AR FY26 p79].
  This conflicts in wording with the filing; the AR heading may simply group all subsidiaries that have common directors, but the AR does not say which directors.
- Secondary sources (LinkedIn and Dun & Bradstreet listings) name Sanjeev Krishan as Stellon's CEO, based in Woodcliff Lake, New Jersey; these are not company documents.
- Status: the 25% holder is the unnamed "local partner"; no filing names it.
  Concord has lent Stellon Rs 14.55 cr against USD 500 of partner equity [AR FY26 p79, p173], so Concord carries almost all the funding risk while the partner holds 25% of any upside.

## 2. USFDA database and Orange Book - CLOSED

Orange Book ANDAs (applicant field, edition with approvals to 8 Sep 2026) [OB]:

| ANDA | Product | Approved | Applicant |
|---|---|---|---|
| 210181 | Mycophenolate mofetil capsules 250 mg | 8 Jan 2019 | Concord Biotech Ltd |
| 211173 | Mycophenolate sodium delayed-release tablets 180/360 mg | 13 Dec 2019 | Concord Biotech Ltd |
| 212087 | Mycophenolate mofetil tablets 500 mg | 31 Jul 2020 | Concord Biotech Ltd |
| 213112 | Tacrolimus capsules 0.5/1/5 mg | 10 Nov 2020 | Concord Biotech Ltd |
| 218821 | Tofacitinib tablets 5/10 mg | 9 Jun 2026 | Concord Biotech Ltd |
| 218663 | Teriflunomide tablets 7/14 mg | 7 Apr 2025 | Neocubes Pharma LLP |
| 218566 | Mycophenolate mofetil for oral suspension 200 mg/ml | 1 Jun 2026 | Neocubes Pharma LLP |

- The Q2 FY27 deck lists exactly these seven products as "7 United States ANDA approved products" [deck Q2 FY27 p22].
  The "12" on the same page is the count of emerging-market products, so the "12 / 7" on p20 is 12 emerging-market products and 7 US ANDA products, not 12 ANDAs.
  The earlier report wording "12 approved ANDAs, 7 marketed" was a misreading and is corrected.
- Five of the seven are held in Concord's own name; two (teriflunomide and MMF oral suspension) are held by Neocubes Pharma LLP.
  The FY26 deck already showed teriflunomide with an ANDA tick [deck Q4 FY26 p22], so the partner-held filing predates Stellon.
- Neocubes Pharma LLP is not named in any Concord annual report, deck, transcript or the RHP (text search of all extracted files returned no hit), and a web search found no stated link.
  Its relationship to Concord (licensing partner, filing agent or other) is not disclosed.
- No Concord rows are marked discontinued.
- Inspection record (company disclosures; FDA's public inspection dashboard was not reachable in this session):
  - Dholka (Unit I API): inspected 28 Apr to 2 May 2025; Form 483 with four observations, "procedural in nature and none of them are related to data integrity" [FDA483 p1]; EIR later received (Q1 FY26 call p5).
  - Limbasi (Unit III API): USFDA inspection completed in 2023 with no Form 483 issued as of the RHP date [RHP p33, p146].
  - Dholka earlier history: fifth USFDA inspection in 2018 with a "no action indicated" classification [RHP p176].
  - Valthera (Unit II formulations): 2018 one 483 observation, then EIR; 28 Apr 2023 EIR with no critical observations [RHP p33]; Q2 FY27 inspection with "one minor procedural observation unrelated to GMP" [deck Q2 FY27 p5].
- No warning letter or import alert appears in any document read.
- Status: ANDA list verified against the FDA's own file; inspection outcomes are company-reported.

## 3. Promoter pledge - CLOSED (secondary)

- Trendlyne's shareholding pages, built from the quarterly exchange filings, show promoter shares pledged at 0.0% for every quarter from Dec 2023 to Sep 2026, and locked-in shares at 0% from Mar 2025 [TL].
- Screener shows promoters at 44.08% to 44.09% for the eight quarters to Sep 2026 [Screener, fetched 9 Nov 2026].
- The promoter's annual Regulation 31(4) no-encumbrance declaration for FY26 (April 2026, NSE) was located by web search but the NSE copy would not load.
- Status: no pledge in any quarter since listing, on a source built from exchange filings; the primary declaration itself was not opened.

## 4. CFO and company secretary exits - CLOSED

- CFO Lalit Sethi: letter dated 8 Dec 2025; early retirement "due to personal reasons", effective close of business 5 Jan 2026 [CFO-2, quoting the filing at CFO].
  Raviraj Karia was appointed CFO from 18 Dec 2025 [AR FY26 p243].
- Company secretary Hina Patel: resigned "to pursue opportunities outside the Organization", relieved at close of business on 21 Jan 2026 [CS p1].
  Paritosh Trivedi took over from 9 Feb 2026 per the annual report [AR FY26 p243]; secondary sources say 11 Feb 2026.
- Prakash Sajnani, the company secretary before Hina Patel, served until May 2025 [AR FY26 p243]; no reason was found for that change.
- Older context found while searching: two independent directors resigned within six weeks of the 2023 listing, Anil Katyal on 25 Aug 2023 ("pre-occupation and other personal commitments") and Utpal Sheth on 30 Sep 2023 ("personal pre-occupations"); Amit Varma, the Quadria nominee, left on 19 Aug 2023 after the offer for sale (BSE filings AttachHis d27bc7ec, a5d85c13, 0cfc7bca).
- Status: stated reasons found; they are routine wording and give no sign of a dispute.

## 5. Molecule and therapy splits - NARROWED

- RHP product split [RHP p40]:

| Year | APIs | Formulations |
|---|---|---|
| FY21 | Rs 506.9 cr (82.16%) | Rs 110.1 cr (17.84%) |
| FY22 | Rs 574.9 cr (80.64%) | Rs 138.0 cr (19.36%) |
| FY23 | Rs 761.3 cr (89.23%) | Rs 91.9 cr (10.77%) |

- All 29 pages of the Q2 FY27 deck and all 30 pages of the Q4 FY26 deck were rendered and read as images.
  The charts show only API versus formulation and domestic versus export splits, which match the text already used.
  The only therapy-level figures are counts: immunosuppressants 8 APIs, oncology 8, antibacterials 6, antifungals 5, others 3 [deck Q2 FY27 p16].
- Status: no revenue by molecule or therapy is disclosed in the RHP, any deck (text or images), transcript or annual report.

## 6. Project returns - NARROWED

Management's capacity economics (all company statements, none audited):

| Plant | Statement | Source |
|---|---|---|
| Dholka (Unit I) | Revenue potential about Rs 600 cr | Q2 FY26 call p22 (analyst restating the Q1 FY24 call; not disputed) |
| Limbasi (Unit III) | Rs 1,600-1,700 cr at 75-80% use | Q2 FY26 call p22 |
| Injectables (Unit IV) | Built for about Rs 200 cr; asset turn 2.5-3x; 3-4 years to reach 70-80% use | Q3 FY24 call p15 |
| Injectables (Unit IV) | Rs 500-600 cr at full use; Rs 300 cr in 3-4 years | Q3 FY25 call p17; Q4 FY25 call p17 |
| Injectables (Unit IV), restated | Peak revenue potential about Rs 600 cr (WHO-GMP facility; not Valthera) | Q3 FY26 call p4 |
| All four units | Peak revenue potential about Rs 3,000 cr | Q4 FY26 call p5 |

- Status: peak revenue and asset turn are disclosed; project-level ROCE, IRR or payback are not.

## 7. Largest customer and contract terms - NARROWED

- Customer concentration at IPO [RHP p35]:

| Year | Top 5 | Top 10 | Of which formulations top 10 |
|---|---|---|---|
| FY21 | 33.19% | 44.17% | 11.31% of revenue |
| FY22 | 34.79% | 43.51% | 11.51% |
| FY23 | 33.47% | 44.28% | 5.69% |

- The overall top 5 equals the API top 5 in every year [RHP p35], so the largest customers are API buyers.
- Named customers: "Our API customers include Intas Pharmaceuticals Limited and Glenmark Pharmaceuticals Limited", described as long-term customers [RHP p146, p150].
- Average relationship with the ten largest customers: eight years at 31 Mar 2023 [RHP p146].
- No top-10 customer stopped buying in FY21 to FY23 [RHP p35].
- Contract terms disclosed in the RHP:
  - Business is "typically" on purchase orders; long-term supply agreements exist with "a few" customers [RHP p161].
  - Long-term agreements brought Rs 86.8 cr, Rs 88.8 cr and Rs 107.1 cr, or 14.06%, 12.45% and 12.56% of revenue in FY21, FY22 and FY23 [RHP p150].
  - Late delivery against a purchase order is a breach that can lead to cancellation of the order or termination of the agreement, and some agreements carry delay penalties [RHP p46].
  - A distributor terminated an exclusive supply agreement in 2022 (letters of 5 Aug and 14 Dec 2022) and Concord had to buy back its unsold stock [RHP p37].
  - Raw materials are bought on purchase orders with no long-term supplier contracts [RHP p162].
- Status: two large customers named; the single largest is not, and price-reset clauses are not disclosed.

## 8. Deck images - CLOSED

- See gap 5: the Q2 FY27 and Q4 FY26 decks were read as images; no number appears in a chart that is not also in the text layer, apart from the therapy API counts above.

## 9. IR site, NSE copies and RHP text - CLOSED (NSE partly)

- RHP: downloaded and text-extracted (380 pages); used for gaps 5 and 7 and the Japan JV history.
- IR site: used for the Stellon and Dholka filings (plain downloads).
- NSE: archive PDFs did not load in this session; the same filings were read from BSE copies, the company website or a Business Standard mirror of the BSE file.

## 10. Q1 FY27 adjusted margin - CLOSED

- 37% for Q1 FY27, excluding the injectable facility and Stellon expenses [deck Q1 FY27 p6; Q1 FY27 call p5].
- Inconsistency: Q1 at 37% and Q2 at 37.1% [Q2 FY27 call p7] cannot average to the 37.8% the company gives for H1 FY27 [Q2 FY27 call p5, p7]; a revenue-weighted average is about 37.1%.
  Either one of the quarterly figures was restated or the H1 figure is off by about 0.7 points; the report uses the quarterly numbers and flags the H1 figure.

## 11. Japan JV sales - CLOSED

Sales of products by Concord to Concord Biotech Japan K.K. (50% JV):

| Year | Rs cr | Source |
|---|---|---|
| FY21 | 29.03 | RHP p21 |
| FY22 | 46.20 | RHP p21 |
| FY23 | 53.96 | RHP p21; AR FY24 p219 |
| FY24 | 43.06 | AR FY24 p219 |
| FY25 | 30.35 | AR FY25 p173 |
| FY26 | 29.09 | AR FY26 p244 (2,908.57 lakh) |

- The FY26 figure (Rs 29.1 cr) is confirmed; the earlier text search missed it because the table uses Rs lakh.
- Sales to the JV have fallen 46% from the FY23 peak.
