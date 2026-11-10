# Worker briefs

Spawn with collaboration.spawn_agent: `model: "gpt-6-luna", fork_turns: "none"`. Set `reasoning_effort: "low"` for literal extraction, document/source/image indexing and routine formatting; set `reasoning_effort: "medium"` for guidance/Q&A interpretation, historical comparison, ambiguous evidence, reconciliation, valuation and final review. Mixed analytical assignments use medium. Never another model. Paste the bounded brief, filled in, as the prompt. Run independent workers in parallel. If a worker cannot start on GPT-6 Luna, stop and tell the user.

10 November 2026 execution amendment: reuse complete, hash-matched document fact/coverage files before dispatch. A worker may read a bounded batch of related short documents, fully and with one output/coverage record per document. Provide only relevant requirements, source paths, existing extracts, output schema and unresolved questions; never the whole session. Reuse cached full page-labelled extracts produced by `tools/report-workflow.py extract` (repository root). Render every chart/table/scan needing visual reading, including text-rich pages. Full reading and source checks remain mandatory.

## doc-reader

Use low for literal extraction; preserve every assigned page and all qualifications. Flag ambiguous tables, conflicting claims or interpretive questions with source pages for a medium pass. Use medium from the start if the assignment requires interpreting Q&A or reconciling evidence. Reuse complete reading; escalation targets the unresolved passages.

```
You are reading one company document for an equity research prompt. Read it fully. Do not summarise loosely and do not add facts that are not on the page.

Document: <absolute path>
Company: <name> (<ticker>)
Short tag for citations: <such as AR FY26, Q2 FY27 call, Q2 FY27 deck, RHP>
Write your output to: <research folder>\facts-<tag>.md

Text: run `python <SKILL_DIR>/scripts/pdf_pages.py "<path>" --text` for page-tagged text. For a page whose chart, table or scan the text misses, run `python <SKILL_DIR>/scripts/pdf_pages.py "<path>" --render --pages <n> --out <dir>` and read the image.

One fact per line, in this form:
- [<tag> p.<page>] <fact, with number, unit and period exactly as printed>

Group lines under these headings, writing "None found" under any empty heading:
## Business and revenue model
## Products, formats or service lines (every one named, with type, application, stage, approvals)
## Customers and partners (named only)
## Capacity and utilisation
## Capex projects (name, cost, spent, funding, dates, status, every change of date or cost)
## Management and board (names, roles, holdings, pledges, pay, related parties)
## Guidance (verbatim quotes with speaker)
## What management talks about that is not yet in the numbers
## Growth triggers (with dates)
## Risks and red flags (auditor remarks, contingent liabilities, litigation)
## Analyst questions and management answers (verbatim, with speakers; calls only)
## Numbers that look inconsistent

Record source SHA-256, extractor/reader version, physical pages read, rendered/OCR pages reviewed and gaps. Preserve important Q&A qualifications and contradictions in the guidance register. Do not treat an extract as proof of reading.
End with: PAGES READ: <n> of <total>. Reply with only the output path, that line, material conflicts and unresolved blockers.
```

## financials-scanner

Use low for literal data retrieval/transcription. Reconciliation, adjustments and interpretation require medium; arithmetic should be reproduced by script.

```
Pull the financials for <company> (<ticker>) with the Screener tools: get_company_overview, get_financials, get_quarterly_results, get_shareholding_pattern, get_peer_comparison.

Write to <research folder>\financials.md:
- Price, market cap, shares outstanding, date of the data.
- Annual P&L for every year available: sales, expenses, operating profit, OPM %, other income, interest, depreciation, PBT, tax %, PAT, EPS.
- Last 8 quarters, same lines.
- Balance sheet: borrowings, reserves, fixed assets, CWIP, investments, cash where shown.
- Cash flow: CFO, CFI, CFF, and capex where shown.
- Ratios: ROCE, debtor days, inventory days, payable days, working capital days.
- Shareholding: promoter, FII, DII, public for the last 8 quarters, and pledge %.
- Peers as listed by Screener.
Tag every table [Screener, <date>]. Copy numbers exactly; compute nothing except lines labelled [computed].
Reply with only the output path.
```

## evidence-verifier

Use medium for verification and resolution of discrepancies; preserve required random-number checks and material-claim verification.

```
Check these numbers against their source pages. For each, open the cited page (pdf_pages.py --text --pages <n>, or --render for tables) and report MATCH, MISMATCH (with the number actually on the page) or NOT FOUND.

<list: number | claim | source tag | document path>

Reply with a table: claim | cited | found | result.
```

Record the actual model and effort per assignment. Every worker uses fork_turns="none" with the relevant task context and file paths; choose low/medium using the task rules above.
