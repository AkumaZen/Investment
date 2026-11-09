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
| [2] Screener numbers | In progress | data/ |
| [3] Diagnose, 15 questions, anti-thesis | Not started | notes.md |
| [4] Model | Not started | model/valuation.py |
| [5] Report | Not started | report/report.html |
| [6] Checks, PDF, final reply | Not started | report/qa/ |

## Step [1] findings to carry forward

- New warrant issue: 70,00,000 at Rs 196 allotted 17 Sep 2026 (Rs 137.20 cr; Rs 34.30 cr received). Diluted shares 9,39,61,558; Rs 102.90 cr still to come.
- Synthimed 7.80% stake appears to be held as CCDs carried at Rs 32 cr (FVTPL, unchanged).
- About Rs 308 cr in related or unlisted instruments (Khandelwal OCRPS, SFRE loan, Ashok NCDs, Essix shares, Fortune, small caps).
- Essix conversion conflict in AR FY26: 51 lakh (chairman) vs 80 lakh (directors' report).
- Guidance drift and claims ledger in evidence/q2fy27-deck.md and evidence/claims-ledger.md.
