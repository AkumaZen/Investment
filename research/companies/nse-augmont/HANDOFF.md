# Compact handoff

## Objective and authority

Build the full Augmont report from `prompts/Augmont Enterprises Research Prompt.md`, then verify it and push the completed work. User also authorises incremental Git pushes so status survives quota/context exhaustion. No extra approval is required for those scoped pushes. No trades, messages or unrelated external writes are authorised.

User requests automatic context compaction at 40% token use. Official config supports a token threshold and turn-end percentage. Project .codex/config.toml sets auto_compact_token_limit200000 (40% of locally cached500000 context), total scope, and post-turn40%. TOML validated; this does not prove active-session reload. Preserve this handoff at phase changes. Reference: https://learn.chatgpt.com/docs/config-file/config-reference . Recompute the absolute threshold if model/context changes.

## Working directory and constraints

Repository: `C:/Users/RNEGI/Desktop/Investment/Investment`. Remote: `https://github.com/AkumaZen/Investment.git`, current branch `main` at start. Exchange NSE AUGMONT / BSE544888; India; INR; cutoff 7 November 2026. Keep current pricing dated and separate standalone/consolidated/owner earnings.

All document readers/scanners/verifiers use **gpt-6.1-sol, reasoning_effort low, fork_turns none**, per explicit user model amendment. Parent context must be supplied in the task. Worker usage quota interrupted several tasks; record completed pages only. Do not pass off cached or machine-extracted text as a finished document review.

## Durable completed work

- Finished prompt, call evidence, prompt source verifier, arithmetic checks and follow-up replay are saved.
- `facts-research-q2-deck.md`: complete 32-page primary Q2 deck review, including exact financial, volume and source-mix tables. Use this before reading PDFs in bulk.
- `research-financials.md` plus `data/screener-*.json`: 15 tool responses across consolidated/standalone annual/quarterly/balance/cash/ratio/peer/shareholder data.
- `regulatory-and-competition.md`: source-linked primary legal/product evidence and explicit gaps.
- `render_report.py` and `render-design-notes.md`: finished renderer. Input `report-content.json`, output `report.html`. Schema: title/subtitle/date/status/executive HTML, sections array of id/title/plain-text answer/html, appendix HTML, sources array id/title/url/detail. Source anchors `source-{id}`. No remote scripts are required for static SVGs.
- `references/report-design/`: original three resources, manifest and portable reader. CC family; physical precedents CC-01/09/15/16/19/20/21/22/24/25. White field, Calibri or named substitute, red #C00000, A4 36pt margins, readable body/table/source sizes. No dashboard cards, shadows or invented charts.
- `source-inventory.json`: recovered actual investor download URLs. Local PDFs under `docs/AUGMONT/`, about 1 GB including duplicates. Public cache is ignored by Git; keep inventory and derived work. User-uploaded transcript remains in `uploads/`.

## Critical provisional findings

Call says core PAT85 vs34, EBITDA113 vs50, source-cycle under2 days imported versus up to4 scrap, scrap share3% to24.5%, no FY27 numeric guidance. Deck confirms group Q2 PAT120 and FY26 group348 vs core153; consumers52.3m but54+m is transactions; GFA1178 to6687=5.7x; enterprise gold7.6 vs15.9 MT and silver113 vs315.4 MT. Deck Sep26 cash171, otherbank50, borrowings3, lease7 crore; restriction/owner claims need primary notes.

AR26 reader verified physical p84 total PAT3483.00m, owner3339.15m, NCI143.84m; p85 CFO-421.57m versus1054.48m FY25. Units are INR million: divide by10 for crore. Physical p1 directors summary appears to put tax1247.96m into a PAT field: do not use it over the audited statements. Full fact pack incomplete.

NSE Goldtech EGR partnership and Nov6 exchange activity verified; not Augmont-specific earnings. Digital gold outside SEBI framework differs from regulated EGRs. Finkurve/Arvog is lending counterparty, Goldtech service/platform provider. Do not consolidate Finkurve by brand. LBMA-compliant is not proven accreditation. BIS old-list validity not current. Custody/trust deed/current audit/insurance remain unverified. RBI finance restrictions need activity-specific current rules. SEBI Rajesh Exports order mentions Augmont as customer but does not establish Augmont misconduct.

## Next actions

1. Check Git checkpoint/remote, read STATUS.md and any newly completed fact files.
2. Resume pinned workers when quota permits. Complete one fact file per document: FY26 AR, latest Q2 board-outcome/results (including H1 CFO/owner PAT/shares), DRHP, RHP, final prospectus. Read older annual reports, prior deck/results and material subsidiary accounts; deduplicate by hash, preserve separate periods and versions. Inventory completeness and source-access gaps need an honest audit.
3. Resolve fresh issue620/625, gross/net/expenses/OFS, actual allotted shares/options, promoter holdings and pledges, related-party acquisitions/payments, diluted shares, segment ownership/NCI, normalised EBITDA definition versus other income, cash restrictions, hedge/custody exposure and actual source-mix denominator. Read IPO monitoring Nov6 and refinery fire Oct22. Do not just extrapolate the latest quarter.
4. Write anti-thesis before bull: higher spreads may absorb more funding; FY26 cash conversion already weak. Reconcile full P&L, balance and cash from primary statements.
5. Build `model.py` with source-tagged inputs, derived ratios, transaction-capital sensitivities, risk-linked bear and explicit guidance table. If no financial guidance, guided base/bull unavailable; independently labelled illustrative sensitivities can remain separate. Bull re-rating uses exactly the same earnings as its comparator. No final rating/value without reconciled required inputs.
6. Assemble all S1-S20, Business/Products before peers/numbers, business understanding at least half the report, 15 questions answered, guidance/outlook, project funding, management, risks and thesis-break signals. Every number carries unit/period/source, every estimate [E] with arithmetic. No fabricated utilisation/active-user history.
7. Generate report HTML, verify 10 sampled numbers, model rerun, 1440 desktop and390 mobile section screenshots, console/network, every anchor/interaction/chart, table overflow, full native scroll, print all pages and reader test. Unrun checks are NOT RUN. Record design adaptation/page storyboard and independent analytical/design reviews.
8. Update STATUS/state/HANDOFF and push incremental/final scoped commits. Review staged diff and exclude secrets/private configuration. Do not push raw 1GB duplicates into Git.

The final report is **not complete** at this checkpoint. No final model or report has been delivered.
