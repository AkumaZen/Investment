# Alembic Pharmaceuticals Ltd (NSE: APLLTD, BSE: 533573) - fact pack

Built 11 Nov 2026 by the lead analyst (Opus 5.5).
The user said no multi-agent workers, so I read every document in scope myself.
Money is Rs crore unless stated otherwise.
Page tags use the physical PDF page ("p6"), so they can be checked against `extracts/*.txt` ("=== p6 ===").

## Document set (latest 4 calls + 4 decks + 4 announcements, user scope)

| Tag | Document | Date | Pages | sha256 (10) | Local file |
|---|---|---|---|---|---|
| Q2C | Q2 FY27 call transcript | call 4 Nov 2026, filed 10 Nov 2026 | 14 | d4ab7dc99a | docs/APLLTD/d1-5991f5bd-f70d-4eb3-bd32-07b794edf376.pdf |
| Q2D | Q2 FY27 investor presentation | 4 Nov 2026 | 23 | 29cb9b6241 | docs/APLLTD/d2-f6ef52d7-552d-47ae-adce-c82ce091ad53.pdf |
| Q1C | Q1 FY27 call transcript | call 4 Aug 2026 | 16 | 5600ff0e32 | docs/APLLTD/d3-b8f27d1b-f644-4885-a463-793dbbfce7ca.pdf |
| Q1D | Q1 FY27 investor presentation | Aug 2026 | 21 | 314064ff1f | docs/APLLTD/d4-d85cc438-3429-4b83-a89a-b1afb9824454.pdf |
| Q4C | Q4 FY26 call transcript | call 15 May 2026 | 17 | bbc6350208 | docs/APLLTD/d5-1e5987cb-3bd7-4832-852e-ec765d86c045.pdf |
| Q4D | Q4 FY26 investor presentation | May 2026 | 21 | d09caac9dd | docs/APLLTD/d6-7304396a-752a-453f-9789-5d41d3d422c0.pdf |
| Q3C | Q3 FY26 call transcript | call 5 Feb 2026 | 14 | e68e1d2e53 | docs/APLLTD/d7-7eca3970-89d2-42e5-ba67-8ab7bc7e1dc9.pdf |
| Q3D | Q3 FY26 investor presentation (revised) | Feb 2026 | 21 | d1c37189fd | docs/APLLTD/d8-46c93f24-1700-455c-b9cd-ab997c99dfbc.pdf |
| A1 | USFDA final approval, Olopatadine HCl ophthalmic 0.7% (OTC) | 4 Nov 2026 | 2 | 33878c9aff | docs/APLLTD/d11-e3ffd3f1-dc5f-4bd1-92a9-9de2c85a2380.pdf |
| A2 | Expanded DifGen collaboration (20+ US complex generics) | 5 Nov 2026 (disclosed in Q2C p4, p12-13) | - | - | trade report: https://www.indianpharmapost.com/news/alembic-pharma-expands-us-complex-generics-portfolio-via-difgen-partnership-22328 |
| A3 | USFDA tentative approval, Binimetinib 45 mg, sole first PIV filer | 19 Jun 2026 | 1 | e7f733ae77 | docs/APLLTD/ann/a3-binimetinib.pdf |
| A4 | USFDA final approval, Dapagliflozin 5/10 mg, 180-day shared exclusivity | 7 Apr 2026 | 1 | c9e0aff7dc | docs/APLLTD/ann/a2-dapagliflozin.pdf |

BSE link pattern for d1 to d11: `https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=<uuid>.pdf`.
A2 and A3 come from the company's investor notices on alembicpharmaceuticals.com.
The exchange announcement APIs returned nothing (Screener said "No announcements found"; BSE said "Access Denied"), so I chose the 4 announcements from the company press releases and the Q2 call.
I did not fetch the CARE rating (Jun 2026) or the Annual Report 2026; both are out of scope.

## Screener consolidated (fetched 10 Nov 2026, https://www.screener.in/company/APLLTD/consolidated/)

### Annual figures

| | FY22 | FY23 | FY24 | FY25 | FY26 | TTM |
|---|---|---|---|---|---|---|
| Sales | 5,306 | 5,653 | 6,229 | 6,672 | 7,345 | 8,477 |
| Operating profit | 874 | 682 | 932 | 1,008 | 1,121 | 1,413 |
| OPM | 16% | 12% | 15% | 15% | 15% | 17% |
| Other income | 56 | -2 | 28 | 56 | -14 | 6 |
| Interest | 18 | 50 | 56 | 79 | 94 | 112 |
| Depreciation | 287 | 275 | 273 | 279 | 319 | 367 |
| PBT | 625 | 355 | 632 | 707 | 694 | 940 |
| Tax | 17% | 4% | 3% | 18% | 3% | |
| Net profit | 521 | 342 | 616 | 582 | 671 | 840 |
| EPS (Rs) | 26.50 | 17.40 | 31.33 | 29.68 | 34.33 | 42.92 |
| CFO | 552 | 724 | 803 | 88 | 783 | |
| FCF | 128 | 282 | 487 | -466 | 290 | |

### Quarterly figures

| | Dec24 | Mar25 | Jun25 | Sep25 | Dec25 | Mar26 | Jun26 | Sep26 |
|---|---|---|---|---|---|---|---|---|
| Sales | 1,693 | 1,770 | 1,711 | 1,910 | 1,876 | 1,848 | 2,150 | 2,603 |
| Operating profit | 260 | 271 | 281 | 316 | 292 | 228 | 332 | 562 |
| OPM | 15% | 15% | 16% | 17% | 16% | 12% | 15% | 22% |
| PBT | 178 | 192 | 190 | 224 | 162 | 119 | 222 | 438 |
| Net profit | 138 | 157 | 154 | 184 | 132 | 202 | 172 | 334 |
| EPS (Rs) | 7.04 | 7.98 | 7.85 | 9.40 | 6.76 | 10.31 | 8.80 | 17.05 |

### Balance sheet and market data

- Balance sheet, Sep 2026: equity 39, reserves 5,905, borrowings 1,547, fixed assets 3,293, CWIP 543.
- Balance sheet, Mar 2026: equity 39, reserves 5,636, borrowings 1,430.
- Market data: price Rs 1,017; market cap 19,996 cr; 52-week range 635 to 1,056; P/E 22.3; book value 302; ROCE 12.6%; ROE 13.4%; face value Rs 2.
- Shares: 19.66 cr [E], derived as market cap / price.
- Shareholding, Sep 2026: promoters 69.87% (69.61% in Dec 2024, steady); FII 4.55%; DII 15.44%; public 10.16%.
- Pledge: none shown [Screener]; verify against the SAST filing.

## Segment revenue (Rs bn) [Q2D p5, p10-14; Q1D]

### Quarterly and half-year

| Segment | Q2 FY26 | Q1 FY27 | Q2 FY27 | YoY | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|
| India branded (includes Animal Health) | 6.39 | 6.42 | 7.25 | +14% | 12.38 | 13.67 |
| US generics + branded | 5.66 | 7.78 | 10.03 | +77% | 10.89 | 17.81 |
| Ex-US | 3.92 | 3.83 | 4.40 | +12% | 7.19 | 8.23 |
| API | 3.14 | 3.46 | 4.36 | +39% | 5.75 | 7.82 |
| Total | 19.10 | 21.50 | 26.03 | +36% | 36.21 | 47.53 |

### Annual, FY22 to FY26 [Q2D]

| Segment | FY22 | FY23 | FY24 | FY25 | FY26 | CAGR |
|---|---|---|---|---|---|---|
| India | 19.26 | 20.63 | 22.00 | 23.39 | 24.58 | 6% |
| US | 16.66 | 15.72 | 17.30 | 19.57 | 22.06 | 7% |
| Ex-US | 7.75 | 8.52 | 10.52 | 12.43 | 14.94 | 18% |
| API | 9.39 | 11.66 | 12.46 | 11.33 | 11.87 | 6% |
| Animal Health, inside India | 2.32 | 2.81 | 3.55 | 4.31 | 5.19 | 22% |

### R&D and pipeline

- R&D (Rs bn), FY22 to FY26: 8.4 / 7.2 / 4.8 / 5.2 / 7.1, which is 15.8% / 12.8% / 7.6% / 7.8% / 9.6% of sales. H1 R&D went from 3.32 to 4.07.
- ANDA filings, FY22 to FY26: 23 / 20 / 15 / 8 / 10.
- ANDA approvals, FY22 to FY26: 21 / 24 / 18 / 23 / 15.
- Cumulative: 283 filings, 245 approvals (20 tentative), 188 launched; 10 launches in H1 FY27 [Q2D].
- India: rank 20 in the Indian pharma market (IPM) with a 1.1% share; 5,800+ medical reps [Q2D].

## Q2 FY27 call, 4 Nov 2026 (Q2C)

- Revenue 2,603, up 36%. India up 14%: Human Health up 11%, Animal Health up 23% [p3-4].
- US generics grew 72% to more than $100m. The base business grew 23% without new launches [p4, p6]. Q1 growth without bosutinib was in the mid-20s [p6].
- Bosutinib sales were "far higher than expectations". Exclusivity runs until the end of November 2026; "What happens after that, I don't know" [p6].
- Pipeline: more than 30 launches over the next 18 months, about a quarter of them first-to-file (FTF) or shared day-1 [p4, p12].
- DifGen: 20+ products (transdermal patches, complex injectables, ophthalmics), on a profit share. DifGen does most of the manufacturing and Alembic does the front end. Revenue starts in FY28 [p4, p12-13].
- Guidance:
  - US: up to 40% growth in FY27.
  - API: at least high-teens growth.
  - India: at market growth, nearing double digits.
  - Ex-US: mid-teens growth.
  - Consolidated: about 20% to 25%, raised from mid-teens. This "incorporates the expected normalization of exclusivity-led sales" [p5].
- Margins:
  - Gross margin 73.7%, up 70 bp, within the 70% to 75% range [p5].
  - EBITDA up 78% to a 22.2% margin, from 17% [p5].
  - H1 revenue 4,753 (up 31%); H1 EBITDA up 51%, with the margin up 255 bp [p5].
  - CFO: "for the first half, we have about 22% EBITDA margins, which we expect to continue towards the second half" [p7]. See conflict C1.
- US branded drag:
  - Guided at 150 to 200 bp for FY27 [p8].
  - Breakeven expected from H1 FY28; "In FY28, we will not see the drag" [p11].
  - Alembic Therapeutics has 4 products (Pivya, Nuvessa, Nuvetest and one more); Pivya is on a "J-shaped curve" [p13].
- Before exclusivity, the business ran at a 70% to 72% gross margin and about 16% EBITDA. The FY28-29 aim is "closer to 20%", through operating leverage and the end of the branded drag [p14].
- FY28 US growth "about 10% to 12%" if launches pan out [p13].
- Tax and tax rate: ETR 24%. Normal 25% tax from FY27; cash tax about 18.75% because of the MAT credit [p5].
- Balance sheet:
  - H1 capex was 250; "major capex cycle now behind us" [p5].
  - Net debt 1,236, under 1x EBITDA [p6].
  - Working capital is up on longer collection cycles for new US launches [p6].
- Costs: crude-linked cost rises were offset by INR depreciation [p13]. Employee and other expenses rose on the US branded field force, promotion and freight [p7].

## Q1 FY27 call, 4 Aug 2026 (Q1C)

- Revenue 2,150, up 26%. US up 49%, or 37% to 38% in constant currency [p4, p14]. India up 7%. API up 33%.
- EBITDA 348 (16%). R&D 186 (9%). PAT 173 [call].
- Bosutinib: 180-day exclusivity on two strengths, launched June 2026, so only 1 month falls in Q1 [p6, p8].
  - Volumes are small, and when competition comes "it will be quite drastic" [p8].
  - "I don't see that opportunity over 6 months" [p13].
- The US base is now $75m to $76m a quarter, against $60m to $65m before. Management said "I would like it to be the new normal" and cautioned on erosion [p8].
- FY27 guidance: US raised to mid/high teens; consolidated "closer to mid-teen".
  - Core margin is guided to high teens, offset by about 150 bp of branded drag, so the reported margin is "flattish" to slightly better than FY26 [p11].
- About 15 more launches in the remaining 9 months, and a similar number in FY28 [p13].
- API guided "above that 10%" [p12].
- India guided to "high single digit", closing the gap to the market [p12].
- New India Human Health head: Ramesh Juneja [p12].
- Ex-US: a Saudi Arabia joint venture and a Canada entry [p13].
- Depreciation: 70% to 75% of the quarter-on-quarter rise is amortisation of US branded intangibles [p15].

## Q4 FY26 call, 15 May 2026 (Q4C)

- Q4 revenue 1,838 (up 4%). Gross margin 71%. R&D 209 (11%, peptide batches).
- Q4 PAT 203 includes a 101 one-time tax gain and a 24 exceptional item.
- FY26:
  - Revenue up 10%.
  - EBITDA before R&D 1,846 (25%); EBITDA after R&D 17%.
  - PAT 675 (up 16%).
  - India up 5%; ex-US up 20%.
- Initial FY27 guidance:
  - Consolidated: low double digit.
  - US: 10% to 15% in INR, with 5% to 6% from FX baked in.
  - ROW (rest of world): 15%+.
  - API: about 10%.
  - India: at market.
  - R&D: 750 to 800.
  - Capex: 300 to 350.
- Pivya launched at the end of February 2026; drag 100 to 150 bp. The target is a 20% EBITDA margin in 2 to 3 years.
- Capacity: the ophthalmic line is "chock-a-block"; other new lines run at about 40% and 60%.
- Net working capital about 3,000; gross debt 1,361.

## Q3 FY26 call, 5 Feb 2026 (Q3C)

- Revenue 1,876 (up 11%). Gross margin 72% vs 74%, hit by price pressure in the US and API [p3-4].
- EBITDA before R&D 464 (25%). R&D 165. PAT before exceptional items 168 (up 21%). Labour code provision 42 [p4].
- India up 6%. Shaunak Amin said India would be "back in line with the market growth rate" by Q1 FY27 [p5, p8].
  - He blamed UCPMP sensitivity (the marketing-practices code for drug companies); "historically, Alembic has not been a high-growth company" [p11].
- US up 6% on a high base. FY26 US guided at 10% to 12%. FY27/28 aim is "between 10% to 15%" a year [p9, p13].
- Out-licensing and manufacturing deals for injectables and oncology will fill the new facilities over 12 to 18 months [p6].
- Pivya launching in Q4 FY26; "we wouldn't have any margin" until it scales [p13].
- Net working capital 2,944; net debt 1,213 [p5].

## Announcements

- A1, 4 Nov 2026: final USFDA approval for Olopatadine HCl ophthalmic 0.7% OTC, the generic of Alcon's Pataday Once Daily Relief [d11 p2].
- A2, 5 Nov 2026: expanded DifGen collaboration. Terms as in Q2C p12-13: licensing, profit share, DifGen manufactures, revenue from FY28.
- A3, 19 Jun 2026: tentative approval for Binimetinib 45 mg, generic of Mektovi.
  - Alembic is the sole first Paragraph IV filer, so it may be eligible for 180-day exclusivity after final approval.
  - IQVIA market size $259m (12 months to Mar 2026).
  - 242 cumulative approvals.
- A4, 7 Apr 2026: final approval for Dapagliflozin 5/10 mg, generic of Farxiga.
  - Eligible for 180 days of shared exclusivity; IQVIA market size $10,487m (12 months to Dec 2025).
  - Launch timing depends on the patent position and is not disclosed in the documents read.

## Data conflicts

- C1, H1 FY27 EBITDA margin:
  - The CFO said "about 22%" for H1 [Q2C p7].
  - The CFO's own numbers give Q1 348 + Q2 578 = 926 on revenue of 4,753, which is 19.5% [E].
  - Screener operating profit gives 894 / 4,753 = 18.8%.
  - Treat 22% as the Q2 rate, not the H1 rate.
- C2, Q1 FY27 EBITDA: 348 (16.2%) on the call vs Screener operating profit 332 (15.4%).
  - Q2: deck 578 (22.2%) vs Screener 562.
  - Screener excludes some items that the company counts in EBITDA; the model uses the Screener basis throughout.
- C3, Q4 FY26 revenue: the call said 1,838, Screener says 1,848.
- C4, US growth in Q2 FY27: the call said 72% (US generics); the deck says 77% (all US including branded).
