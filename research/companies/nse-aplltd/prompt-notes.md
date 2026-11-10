# Alembic Pharmaceuticals - prompt notes (11 Nov 2026)

## User request (verbatim)

"Now I want you to build a short report prompt for Alembic Pharmaceuticals Ltd for quick analysis , use only latest 4 concall transcripts and ppt , only four and latest important annocements and try to answer the question whether the change is structural or one of use my research prompt builder, and execute the prompt quickly don't use mulitagents use opus 5.5 only for quick analysis and Make sure you stage and push all the changes when the report is done, make sure report is pushed and I don't have to say you again, I am sleeping you so you all the task autonomously ,"

## Scope and overrides

- Size: Concise.
- Documents: the 4 latest transcripts (Q3 FY26 to Q2 FY27), the 4 matching decks, and 4 announcements (Olopatadine, DifGen, Binimetinib, Dapagliflozin). See facts.md.
- Workers: the user said no multi-agent workers, so the lead agent (Opus 5.5) reads, models and writes everything. This replaces the skeleton's GPT-6 Luna worker lines and the step 6.5/6.7 worker checks. The recorded evidence is that no workers were spawned.
- Rating: none. Scenario bands only, per the user's standing constraint on paid-client reports. The skeleton's rating bands line is replaced.
- Push: the user pre-authorised staging and pushing once the report is done.

## Diagnosis (step 4)

1. Why it matters: Q2 FY27 revenue rose 36% and EBITDA margin hit 22.2%, against a five-year history of 6% to 10% growth and a 12% to 16% margin. The core debate is whether that step-up is structural or a one-off from the bosutinib 180-day exclusivity, which ends in late November 2026.
2. How one unit earns:
   - US generics: file an ANDA, win approval, launch, and earn from price x volume. Prices erode as competitors enter.
   - The best money comes from first-to-file (FTF) exclusivity, which is a temporary 180-day monopoly or duopoly.
   - India branded: field reps detail doctors, giving recurring prescription sales. Animal Health sits inside India.
   - Ex-US: partner-led sales in Europe, Australia, Canada and similar markets.
   - API: bulk drug sales to other formulators.
   - US branded (Alembic Therapeutics): Pivya and others, now a loss-making J-curve.
3. Management:
   - The Amin family (Shaunak Amin, MD) owns 69.87%, steady, with no pledge shown.
   - Capex of Rs 2,000 cr plus went into new oncology, injectable and ophthalmic plants. Utilisation was low until FY27.
   - Delivery record: the FY26 US guide of 10% to 12% was met (+13%). India "back to market" was promised and is only partly met. The 20% margin aim has been repeated since FY24 and is not yet sustained.
4. Guidance:
   - FY27 consolidated growth was raised twice: from low double digit (May) to mid-teens (Aug) to 20% to 25% (Nov).
   - FY28 US growth of 10% to 12%. Branded breakeven in H1 FY28. DifGen revenue from FY28.
   - Capex is behind them. More than 30 launches over 18 months.
5. Anti-thesis: strip out about Rs 300 cr of bosutinib and exclusivity-linked Q2 revenue [E] and Q2 growth falls to roughly 20%, with a margin of about 16% to 17%. FY23 shows how fast US price erosion took the margin to 12%. India has grown 6% a year for 4 years. At 22x trailing P/E, the price already capitalises a TTM EPS that includes a one-off.
6. Model, story and sector:
   - Model: pharma formulations and API, project-like for US launches, recurring for India.
   - Story: a quarterly update and an inflection test.
   - Family: MQ (quarterly update for an understood company).
7. Separate X from Y: base business vs exclusivity-led launches, and constant currency vs INR.
   - Chain: launches → share → price holding → utilisation → operating leverage → margin.
   - First unproven link: whether the base keeps about 23% growth after bosutinib erodes.
8. The 15 questions: in the prompt, 0B.
9. Connecting the dots: in the prompt, 0B.
10. Conflicts C1 to C4: in facts.md.
11. Metric: P/E. The company is profitable, stable and generic-pharma, which is the Step 1 table's "profitable and stable" row. Cross-check with EV/EBITDA.
12. Sections: concise merges (S7 into S4, S16 into S15, S18 into S17). S8 becomes "Structural or one-off?". S3 becomes "Pipeline and launches".
13. Visual plan: in slots.json. The forms are columns for the annual and quarterly series, a stacked decomposition, a margin bridge, a guidance-drift ladder, and a scenario range bar.
14. Learnings rows: each is forced by 0B rules 5 and 8, S8, S12 and section 5. Concise scope noted.
15. Report design: family MQ, because this is a recurring update on a known company where the results bridge and call evidence lead.
    - Pages: MQ-01 executive, MQ-02 results bridge, MQ-03 monitoring, MQ-04/05 call evidence, MQ-06 model.
16. References staged to `references/report-design` (see the build log).
- Checker size WARN (53.9 KB vs 15-25 KB concise band) accepted: the locked sections 6A, 7, 8 and 8B pasted by assemble.py are about 19 KB on their own, so the band cannot be met without dropping locked text.
