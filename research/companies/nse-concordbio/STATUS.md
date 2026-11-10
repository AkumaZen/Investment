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
- RHP text-extracted; IR-site filings, the US FDA Orange Book and Trendlyne pledge history checked in the gap-research round; NSE copies did not load. See data/source-manifest.md and evidence/gap-research.md.

## Stages

| Stage | State | Output |
|---|---|---|
| Documents collected and text extracted | Done | docs/CONCORDBIO |
| Latest deck and transcript facts | Done | facts-latest.md |
| Phase 1 prompt build | Done (67a4583) | prompts/Concord Biotech Research Prompt.md |
| Screener data pull | Done | data/screener-2026-11-09.md |
| Source manifest | Done; updated after gap research | data/source-manifest.md |
| Promises-vs-delivery ledger (14 calls) | Done (6d3ce1d), verdict AMBER | evidence/guidance-ledger.md |
| Deck history (capacity, utilisation, segments) | Done (f33973f) | evidence/deck-history.md |
| FY26 annual report extraction | Done (9024b4c) | evidence/ar-fy26.md |
| Peers and notes (15 questions) | Done | notes.md, evidence/peers.md |
| Model and valuation | Done (base Rs 696, FAIR) | model/valuation.py, valuation.md, valuation.json |
| HTML report build | Done (4a403a0, aa5b781) | report/build.py, report/report.html |
| Visual check and by-eye pass | Done (aa5b781); touch scroll NOT RUN | report/qa/qa-notes.md |
| PDF export and page inspection | Done (a029a48), 26 pages | report/Concord_Biotech_Company_Study.pdf |
| QA summary | Done | report/qa/qa-notes.md |
| Gap research (11 known gaps) | Done: 7 closed, 4 narrowed; report rebuilt, visual check clean, PDF 26 pages | evidence/gap-research.md |

- 2026-11-10: Navigation complete in HTML and existing 26-page PDF. Clickable 21-section index, bookmarks and Contents / Previous / Next on every PDF page. Original analysis/layout preserved; all targets and all-page visual QA passed. See report/qa/navigation/verification-summary.md.
- 2026-11-11: Valuation restructured per business-valuation-scenarios. S20 now has year-wise Bear/Base/Bull tables in Screener P&L layout (FY25A, FY26A, FY27E-FY29E) with pre and post-dilution EPS (same; no dilution instruments), PAT growth and margin, target price at each 31 Mar, return and CAGR vs Rs 594, multiple held flat, and a caveats list. Bull rebuilt from disclosed upside (22% FY27, injectables Rs 75/150 cr in FY28/FY29, margin to 40%, 45x): Rs 894 to Rs 1,051. Bear Rs 352 and base Rs 696 unchanged, readout FAIR. PDF re-exported (30 pages) with the PDF tool footer now config-driven. See report/qa/qa-notes.md section 11.
