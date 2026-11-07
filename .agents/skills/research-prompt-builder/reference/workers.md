# Worker briefs

Spawn with the Agent tool: `subagent_type: "general-purpose"`, `model: "sonnet"`. Never another model. Paste the brief, filled in, as the prompt. Run workers in parallel. If a worker cannot start on Sonnet, stop and tell the user.

## doc-reader

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

End with: PAGES READ: <n> of <total>. Reply with only the output path and that line.
```

## financials-scanner

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

```
Check these numbers against their source pages. For each, open the cited page (pdf_pages.py --text --pages <n>, or --render for tables) and report MATCH, MISMATCH (with the number actually on the page) or NOT FOUND.

<list: number | claim | source tag | document path>

Reply with a table: claim | cited | found | result.
```
