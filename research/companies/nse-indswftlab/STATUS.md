# Ind-Swift Laboratories (NSE: INDSWFTLAB, BSE: 532305) - research status

Resume from this file after any context loss.
Analysis date: 2026-11-09.
Latest results: Q2 FY27 (deck and call 4 Nov 2026).
Prompt being executed: prompts/Ind-Swift Laboratories Research Prompt.md (V1, commit e7aa250).

## Brief

- Execute the prompt: full HTML report (EL design family, teal #0E5A63), A4 PDF for paid clients.
- No rating, no personal advice; valuation readout ATTRACTIVE / FAIR / STRETCHED only.
- Never invent data; mark Disclosed / Inferred / Not Disclosed.

## Standing constraints

- Do not push. Commit locally in small steps, no agent co-author line.
- Do not stage the root Augmont PDFs. Keep raw PDFs out of git (docs/ stays untracked).
- No em or en dashes.
- report-visual-check plus by-eye desktop and phone pass before calling the report done.
- No worker models; Claude reads everything directly (disclosed in QA notes).

## Document inventory (docs/INDSWFTLAB/raw, text in docs/INDSWFTLAB/text)

- Calls: Q2 FY27 (4 Nov 2026, user upload, stockscans machine transcript), Q1 FY27 (BSE 20e51151, Aug 2026). Screener lists no other transcripts.
- Decks: Q2 FY27, Q1 FY27, Q3 FY26 (4 Feb 2026), corporate deck 14 Jan 2026. Two 2020 decks (old API company) downloaded, history only.
- Annual reports FY24, FY25, FY26.
- CARE monitoring agency reports (final and Q2 FY27), CARE rating Mar 2024.

## Stages

| Stage | State | Output |
|---|---|---|
| [0] Set up, documents collected, text extracted | Done | docs/INDSWFTLAB, data/doc-index.json |
| [1] Evidence files | Done | evidence/ (q2fy27-call, q1fy27-call, q2fy27-deck, ar-fy26, care-ma, claims-ledger) |
| [2] Screener numbers, peers, source manifest | Done | data/screener-2026-11-09.md, data/source-manifest.md |
| [3] Diagnose, 15 questions, anti-thesis | In progress | notes.md |
| [4] Model | Not started | model/valuation.py |
| [5] Report | Not started | report/report.html |
| [6] Checks, PDF, final reply | Not started | report/qa/ |

## Step [1] findings to carry forward

- New warrant issue: 70,00,000 at Rs 196 allotted 17 Sep 2026 to Essix Biosciences (promoter) [NSE-A]; 14,00,000 converted 8 Oct 2026 [NSE-C]. Shares likely 8,83,61,558 after conversion (filing and Q2 deck print 8,69,61,558, which the Q1 deck already showed before the conversion; data conflict in evidence/care-ma.md); 56,00,000 warrants left; diluted 9,39,61,558 used in the model, 9,25,61,558 as sensitivity; Rs 54.88 cr received, Rs 82.32 cr still to come.
- Synthimed 7.80% stake appears to be held as CCDs carried at Rs 32 cr (FVTPL, unchanged).
- About Rs 308 cr in related or unlisted instruments (Khandelwal OCRPS, SFRE loan, Ashok NCDs, Essix shares, Fortune, small caps).
- Essix conversion conflict in AR FY26: 51 lakh (chairman) vs 80 lakh (directors' report).
- Guidance drift and claims ledger in evidence/q2fy27-deck.md and evidence/claims-ledger.md.

## Step [2] findings to carry forward

- Peer median market cap / TTM operating profit 17.9x (eight peers, range 10.4x to 25.9x); see data/screener-2026-11-09.md.
- Operating cash flow negative FY24 to FY26 (Rs -260 cr in total) [Screener].
- NSE-C filing's own share counts move by 2,50,000, not the 14,00,000 it says were allotted: data conflict.
- Ind-Swift holds Rs 28.85 cr of Essix shares while Essix funds the company through warrants (circular flow, governance point).

## Resume point (2026-11-09)

- Step [3]: share-count conflict recorded. notes.md (15 answers, anti-thesis, closed To-find list, AR FY26 related-party, pay, ESOP, pledged FD and pledge Not Disclosed facts) still to write.
- AR FY26 facts found but not yet in notes.md: Synthimed is not a related party [AR26 p92]; promoter-linked loans Rs 25.17 cr (ar-fy26.md says Rs 10.65 cr, conflict); Sahil Munjal pay +72.13%, Rishav Mehta +100.08% vs median employee +8.07% [AR26 p64]; unmodified audit opinion with two emphasis-of-matter items; Rs 16.00 cr FDs pledged, Rs 15 cr against the Rs 66.34 cr sales tax demand.
- Steps [4] to [6] not started.
