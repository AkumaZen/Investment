# Augmont prompt evidence check

Date: 7 November 2026. Verifier: gpt-6.1-sol, low reasoning effort, fork_turns none.

Scope: company-specific factual numerical claims in `prompts/Augmont Enterprises Research Prompt.md`, checked only against `docs/AUGMONT/uploads/Augmont_Enterprises_Ltd_Nov_2026_Transcript.pdf`. This establishes fidelity to the supplied machine-generated transcript, not independent confirmation of the underlying business figures. No other company document was used. Source pages below are physical PDF pages, which match the printed page numbers.

Method: deduplicate repeated factual claims into the following 30 material numerical claim groups, excluding generic template numbers, design specifications and hypothetical valuation inputs. Select without replacement using Python `random.Random(20261107).sample(range(1,31),10)`. The resulting order is **19, 22, 13, 15, 26, 2, 5, 20, 10, 8**. Page text was read using the required `pdf_pages.py <PDF> --text --pages <n>` reader. Text was clear for these claims; rendering was unnecessary.

## Candidate population

| ID | Deduplicated company fact group | Prompt citation |
|---|---|---|
| 1 | FY26 revenue above INR94,000 crore | p.1 |
| 2 | FY26 introductory ROE 51%, perimeter unspecified | p.1 |
| 3 | Present across 24 states | pp.1-3 |
| 4 | Refining capacity 284 metric tonnes, time/metal basis unverified | pp.1-2 |
| 5 | Two refineries | pp.1-2 |
| 6 | 122 Gold4All centres | pp.2,4 |
| 7 | 245 fintech partners | p.2 |
| 8 | 751 distribution points | pp.2,4 |
| 9 | Registered customers 50.6 million to 52.3 million | p.2 |
| 10 | Separate 54 million customer total | p.5 |
| 11 | Spot around 93% of FY26 revenue | p.3 |
| 12 | Gold4All 7% FY26, 13% current-quarter revenue contribution | pp.3,11 |
| 13 | Broad PAT INR76 crore to INR348 crore; endpoints/perimeter unclear | p.5 |
| 14 | Revenue growth 2.7x over last two financial years | p.5 |
| 15 | Gold4All INR1,100 crore to INR6,600 crore, stated 5.7x | p.5 |
| 16 | About one million diamond stones listed | p.6 |
| 17 | About 8,000 carats sold | p.6 |
| 18 | About 250 diamond dealers | p.6 |
| 19 | Core Q2 PAT INR34 crore to INR85 crore | p.7 |
| 20 | Core Q2 EBITDA INR50 crore to INR113 crore | p.7 |
| 21 | Core Q2 PAT margin 0.18% to 0.65% | p.7 |
| 22 | Enterprise revenue down 32% YoY | p.7 |
| 23 | Consumer revenue up 47% YoY | p.7 |
| 24 | Core H1 PAT INR107 crore; stated 75% higher than FY26, about 70% of full-year INR153 crore | p.7 |
| 25 | Imports cash cycle under two days; scrap up to four days | p.7 |
| 26 | Fresh issue INR620 crore versus INR625 crore primary in INR825 crore IPO | pp.7,12-13 |
| 27 | Supplier advances/customer collection three to four days later | p.12 |
| 28 | 20 to 35 delivery centres; 10 identified for current financial year | p.13 |
| 29 | Scrap procurement share 3% Q2 FY26 to approximately 24.5% Q2 FY27 | p.14 |
| 30 | INR700–800 crore debtor range comes from analyst question, not management-confirmed recurring balance | p.16 |

## Ten sampled checks

All monetary figures below are INR crore unless stated otherwise.

| Claim | Cited source/page | Found exact numbers and scope | Result |
|---|---|---|---|
| 19: Core Q2 PAT rose from 34 to 85 | Q2 FY27 call p.7 | Ketan explicitly introduces the core Augmont Enterprises/Spot business, then gives PAT 34 to 85, 2.5x Q2 FY26 and 3.9x Q1 FY27. It is PAT, not EBITDA; no consolidated attribution is inferred. | MATCH |
| 22: Enterprise revenue declined 32% YoY | Q2 FY27 call p.7 | Same management discussion: consumer revenue up 47% year on year, enterprise revenue down 32%. Prompt retains the management channel label rather than assuming a statutory segment. | MATCH |
| 13: Broad PAT grew from 76 to 348 | Q2 FY27 call p.5 | Ketan gives 4.6x PAT, 76 to 348, in a broad discussion of platform growth over the last two financial years. Exact endpoints and entity perimeter are not identified; prompt correctly keeps this apart from core FY26 PAT 153 on p.7. | MATCH |
| 15: Gold4All revenue 1,100 to 6,600 with stated 5.7x | Q2 FY27 call p.5 | The transcript contains both endpoints and 5.7x. Endpoints mathematically imply 6.00x; prompt explicitly records this unresolved source inconsistency. | MATCH |
| 26: Fresh-capital descriptions 620/625 and IPO 825 | Q2 FY27 call pp.7,12-13 | P.7 says entire 620 fresh issue used per RHP objectives. P.12 says IPO 825, primary 625, and 625 minus IPO expenses realised by company; p.13 continues working-capital purpose/use. Prompt preserves differing gross/net descriptions without asserting their reconciliation. | MATCH |
| 2: Introductory FY26 ROE 51%, scope unspecified | Q2 FY27 call p.1 | Ketan states ROE for FY26 was 51%, adjacent to revenue above 94,000. No clear standalone/consolidated or owner-profit denominator is given there; prompt marks scope unspecified. | MATCH |
| 5: Two refineries | Q2 FY27 call pp.1-2 | P.2 describes the first refinery at Rudrapur and second at Navi Mumbai, then explicitly says two refineries. Prompt's paired citation pp.1-2 supports the count. | MATCH |
| 20: Core EBITDA increased 50 to 113 | Q2 FY27 call p.7 | Following core PAT and PAT-margin statements, Ketan says EBITDA rose to 113 from 50 a year ago. Prompt correctly does not relabel this as PAT and requests definition/perimeter reconciliation. | MATCH |
| 10: Separate customer total 54 million | Q2 FY27 call p.5 | Ketan says reach increased from 28 million in FY24 to 54 million retail customers. P.2 separately says registered customers 50.6 million to 52.3 million. Prompt flags the unexplained cutoff/definition difference rather than equating the totals. | MATCH |
| 8: 751 distribution points | Q2 FY27 call pp.2,4 | P.2 says retail point distribution centres increased from 731 to 751; p.4 calls these 751 channel partners for coins/bars distribution. Prompt uses distribution points and does not equate them with the 122 Gold4All centres. | MATCH |

Result: **10 MATCH, 0 MISMATCH, 0 NOT FOUND.** The population is a documented deduplicated material-fact sample, not a claim that every numerical occurrence in the prompt had equal selection probability.

## Consequential cross-checks

- Arithmetic: 85/34 = 2.50x, or 150.0% growth; 113/50 = 2.26x, or 126.0% growth; 24.5% minus 3.0% = 21.5 percentage points; 24.5/3 = 8.1667x of the share. All are correct. Share multiplication does not establish absolute procurement-volume growth. The p.14 source specifically supplies the procurement denominator and periods but does not say volume versus value.
- Source conflicts: 6,600/1,100 = 6.00x, inconsistent with the transcript's stated 5.7x. Difference between 625 and 620 is 5. The prompt correctly flags both; it does not invent a five-crore issue-expense reconciliation. 107/153 = 69.93%, consistent with around 70%; the statement 75% higher than FY26 has an unclear comparator and is correctly not treated as H1-on-H1 confirmation.
- Margin durability: pp.7 and 12 explain the higher scrap spread and longer capital lock-up, but p.16 explicitly says there is no fixed margin on either metal. P.18 makes recycling share conditional on market circumstances. The prompt's durable-return proposition remains a question with a disconfirming signal, not an asserted fact. Its exactly-two/exactly-four-day illustration is correctly labelled hypothetical: a doubling of cycle duration halves turns at fixed deployable capital, requiring double net contribution per cycle under its stated assumptions. Neither boundary is an observed average.
- Guidance: p.8 declines to quantify EGR but expects the product to start this quarter. P.13 refuses incremental revenue/profitability numbers against working capital. P.14 refuses numerical FY27 revenue/margin guidance. Sections S12 and valuation properly require an unavailable guided base to remain blank, with separately labelled illustrative sensitivities and NOT RATED when required inputs are missing. The Q3 FY27 interpretation is explicitly an inference from the November call date. Operating centre ambitions are kept separate from financial guidance.
- Analyst premises: p.16's 700–800 debtor range is asked by Pakshal; Amit denies recurring treatment and says month-end receivables were realised within a couple of working days. The prompt correctly requests independent collection evidence and does not adopt the analyst's range as a fact. P.18's analyst-suggested 24–25% sustainable scrap share is likewise not adopted as management guidance.
- Attribution: sampled citations resolve to the correct pages. The broad PAT 348 on p.5 is not presented as core PAT 153 on p.7; PAT 85 is not confused with EBITDA 113. No concrete erroneous source citation or material factual misstatement was found in this review.

Remaining limits: source is machine-transcribed and self-warns about errors; issuer identity, exchange codes, primary filings, share counts, cash-flow conversion and realised unit economics are not validated by this check. The prompt appropriately routes these to later research. The check does not establish the absence of errors elsewhere in the full prompt.
