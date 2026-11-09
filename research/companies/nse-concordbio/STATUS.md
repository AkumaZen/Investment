# Concord Biotech (NSE: CONCORDBIO) - research status

Resume from this file after any context loss.
Analysis date: 2026-11-09.
Latest results: Q2 FY27 (deck Oct 27, 2026; call Oct 28, 2026).

## Brief (from the user, verbatim intent)

- Phase 1: build a company-specific prompt with `.agents/skills/research-prompt-builder`, using only the latest transcript and deck, save it, then execute it myself.
- Phase 2: collect the latest annual report, ALL transcripts, ALL decks and material announcements; source priority is IR site, then NSE/BSE, then Screener; record URLs, dates and pages.
- Phase 3: full research with facts, guidance [G] and estimates [E] kept separate; promises-vs-delivery ledger; bull/base/bear valuation; risks; optionalities.
- Phase 4: report in the user's reference designs (references/equity-reports plus the skill's report-design manual); plain English; real charts; render and inspect every page; final output is a PDF.
- Phase 5: autonomous, no approval requests, checkpoints on disk, never invent data, never call a partial draft complete.
- Deliverables: PDF report, reusable prompt, source manifest, evidence and calculations, QA summary.

## Standing constraints

- Do not push. Commit locally in small steps, with no agent co-author line.
- Do not stage the root PDFs (Augmont_Equity_Research_Revamped.pdf, Augmont_Report_Critique.pdf).
- Keep raw downloaded PDFs out of git.
- No em dashes. No rating and no personal advice; scenarios and valuation attractiveness only.
- HTML report must pass tools/report-visual-check plus a by-eye pass at desktop and phone width (learnings/concepts/equity-report-quality-process.md).
- Prompt-builder workers (gpt-6.1-sol) are not available to Claude; extraction is done directly and this is disclosed in the QA summary.

## Document inventory

All files in docs/CONCORDBIO/raw, text in docs/CONCORDBIO/text, index in data/doc-index.json, BSE ids in data/doc-urls.txt.

- Transcripts: 14, Q1 FY24 to Q2 FY27.
- Decks: 14, Q1 FY24 to Q2 FY27.
- Annual reports: FY24, FY25, FY26.
- Other: results press release Q2 FY27, bonus allotment (Nov 4, 2026, 1:1, 10,46,16,204 shares), call recording notice Q2 FY27.
- Not yet found: RHP (Aug 2023 IPO), company IR site copies, NSE filings.

## Stages

| Stage | State | Output |
|---|---|---|
| Documents collected and text extracted | Done | docs/CONCORDBIO |
| Latest deck and transcript facts | Done | facts-latest.md |
| Phase 1 prompt build | In progress | prompts/Concord Biotech Research Prompt.md |
| Screener data pull | Pending | data/screener-*.json |
| RHP and IR site check | Pending | data/source-manifest.md |
| Promises-vs-delivery ledger (14 calls) | Pending | evidence/guidance-ledger.md |
| Deck history (capacity, utilisation, segments) | Pending | evidence/deck-history.md |
| FY26 annual report extraction | Pending | evidence/ar-fy26.md |
| Model and valuation | Pending | model/valuation.py |
| HTML report build | Pending | report/ |
| Visual check and by-eye pass | Pending | qa-notes.md |
| PDF export and page inspection | Pending | report/*.pdf |
| QA summary | Pending | qa-notes.md |
