# Prompt evidence verification

Verified 10 November 2026 using only the actual local transcript PDF via PyMuPDF (`fitz`). No external company evidence or audio used. Printed page N is physical PDF page N+1 (zero-based document index N).

Sampling: Python `random.Random(20261110)`, `sample(opening_population, 5)` followed by `sample(qa_population, 5)`. Stable population order listed below; distinct claims deduplicated across prompt repetitions. The sample is stratified to ensure opening-remarks and later-Q&A coverage; not a random sample of design/section numbers.

| Claim | Cited | Found in actual PDF | Result | Page / qualifier correctness |
|---|---|---|---|---|
| International Q2 FY27 revenue approximately 32% | Printed p.3, physical p.4 | vanced markets. In Q2 FY '27, approximately 32% of our revenue came from international markets. The second is manufacturing sca | MATCH | Page correct. International markets; quarter qualifier correct. |
| Line 3 optimal annual revenue about Rs 110 crore | Printed p.4, physical p.5 | our earlier guidance of about INR110 crore annual revenue will be met with the optimal utilization of the line. Captive so | MATCH | Page correct. Conditional on optimal utilization. |
| Debt/equity 3.5x FY23 to about 1.1x FY26 | Printed p.2, physical p.3 | debt-to-equity ratio has come down from 3.5x in FY '23 to about 1.1 in FY '26, giving us the financial headroom to fund our next phase of grow | MATCH | Page correct. Historical management comparison, not independently verified. |
| Q2 FY27 PAT Rs 4.86 crore | Printed p.3, physical p.4 | Profit after tax has stood at INR4.86 crores, up by 26% year-on-year basis with a PAT margin of about 6%. Coming to half | MATCH | Page correct. Q2 FY27, not H1. |
| Two-year 20%-plus revenue CAGR and 25%-plus EBITDA margin aim | Printed p.3, physical p.4 | s a clear 2-year aim, revenue growth of 20%-plus CAGR and EBITDA margins of 25%-plus. We believe we are well positioned to deliver this. The capacity | MATCH | Page correct. Aim, not exact annual guidance. |
| 200-250 channel partners | Printed p.8, physical p.9 | ar is? Bhavesh Patel: We have roughly 200 to 250 channel partners across the country. Yes, yes and that is more than sufficient to | MATCH | Page correct. Approximate number across country. |
| Whole-plant utilization 95-97% | Printed p.6, physical p.7 |  is roughly around 95% or so, 95% to 97%. SteriPort Line 3, which we have commissioned in September, is r | MATCH | Page correct. Current whole plant; distinguished from Line 3. |
| FAT December 13-19 | Printed p.11, physical p.12 | th. It was to be in November, now it's December 13 to 19. So we will have equipment by January. So by March end we should | MATCH | Page correct. Delayed from November; distinct from commissioning. |
| SVP next-year Rs 16 crore | Printed p.14, physical p.15 |  Page 14 of 15 Bhavesh Patel: SVP in the next year, we are taking only INR16 crore top line. Vedant: Is there any... Bhavesh Patel: And gain, it is | MATCH | Page correct. Explicitly speculative; exact fiscal wording flagged. |
| Full utilization target from 20 November | Printed p.6, physical p.7 | capacity utilization would be 100% from November 20 onwards, all the lines put together. That's how typically it has been. D | MATCH | Page correct. Future target for all lines; not accomplished result. |

## Sampling populations (ordered)

Opening: Line 3 capacity increase about 75%; Solar capacity 10.8 MW; Debt/equity 3.5x FY23 to about 1.1x FY26; Annual debt repayment roughly Rs 35 crore including solar; International Q2 FY27 revenue approximately 32%; Two-year 20%-plus revenue CAGR and 25%-plus EBITDA margin aim; Q2 FY27 revenue Rs 83.1 crore; Q2 FY27 PAT Rs 4.86 crore; H1 FY27 PAT Rs 8.17 crore; Line 3 FY27 contribution about Rs 60 crore; Line 3 optimal annual revenue about Rs 110 crore; Annual solar saving about Rs 9 crore.

Q&A: September borrowing about Rs 190 crore, working capital Rs 45 crore; FY27-end total borrowing Rs 175-180 crore; Whole-plant utilization 95-97%; Full utilization target from 20 November; Small-volume SBU sales Rs 55-65 crore; 200-250 channel partners; Revenue Rs 420-430 crore annualised/full-year wording; Hypothetical additional SteriPort line Rs 120 crore; FAT December 13-19; Product price hikes Rs 0.70-1.80 per bottle; SVP initial utilization 45-50% first two quarters; SVP next-year Rs 16 crore.

## Additional actionable findings

Final prompt re-read after the lead's edits. The stale Sonnet/Opus model assignment, generic outside-filing instructions and corrupt reverse-check sentence have been resolved. No remaining material inaccurate company assertion, unqualified numerical guidance, or active source-scope contradiction found. Section 5 explicitly gives the user's source restriction precedence over missing skill inputs; unknown valuation cells stay blocked.

## Other source checks

Checked actual printed pp.2-14 for material statements outside the sample. No material false numerical assertion found. Source peculiarities are appropriately retained: INR-prefixed capacity units, September 2027 slip, 52% versus raw SVP capacity arithmetic, approximate debt arithmetic, 420-430 annualised/full-year versus affirmed FY28 400-420, and explicitly speculative SVP figures. Q&A supplies physical bottle/unit language but does not independently verify nameplate capacity. No audio verification claimed. The standalone printed-page citations in the prompt are consistent with PDF pagination.
