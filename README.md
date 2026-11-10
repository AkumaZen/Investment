# Stock research workspace

A simple home for stock research, reusable AI workflows, and lessons from investment decisions. Start with one company and build a traceable thesis before expanding.

## Where things go

| Folder | Purpose |
| --- | --- |
| `.agents/skills/` | Repeatable stock research workflows that Codex can discover |
| `prompts/` | Copyable requests for common research tasks |
| `agents/` | Focused analyst role instructions |
| `research/` | Company notes, watchlist, and source records |
| `learnings/` | Concepts, decision reviews, and lessons |
| `templates/` | Starting documents for consistent notes |
| `tools/report-visual-check/` | Playwright visual check for HTML reports (screenshots, contact sheets, layout and chart-label lint) |

## Start here

1. Add a company to [the watchlist](research/watchlist.md), including its exchange and ticker.
2. Copy [the stock template](templates/stock-analysis.md) to `research/companies/<exchange>-<ticker>/analysis.md`.
3. Use [the stock research prompt](prompts/stock-research.md), or ask Codex to use `$stock-research`.
4. Record a dated decision using [the decision template](templates/decision-review.md). Store it in `learnings/reviews/`.
5. Revisit the thesis after results or a material event; capture reusable lessons in [the learning log](learnings/README.md).

Use [the workflow catalog](prompts/README.md) to choose a prompt and role. Agent files are reusable role briefs; they do not automatically configure or launch agents.

## Conventions

- Use lowercase, hyphenated filenames and `YYYY-MM-DD` dates.
- Identify securities by exchange and ticker; company names alone can be ambiguous.
- Keep one company folder per listed security, with dated updates alongside `analysis.md`.
- Cite sources beside claims. Record publication date, reporting period, currency, units, and access date where relevant.
- Keep forecasts separate from reported facts and record the assumptions behind calculations.
- Store only material you have permission to retain. Keep account exports and credentials out of Git.

This starter contains workflows and blank templates, not completed company research. Add tools or automation only when a recurring task needs them.

## Company-specific research prompt builder

The [research-prompt-builder skill](.agents/skills/research-prompt-builder/SKILL.md) prepares a tailored prompt for a later research run. Read its [Codex setup notes](.agents/skills/research-prompt-builder/CODEX.md) for repository paths and runtime requirements, and [Screener MCP setup](docs/screener-mcp.md) for its data connection.

Use `$research-prompt-builder` when you want the research prompt itself. Use `$stock-research` when you want company analysis.

For full reports, use the [efficient execution workflow](learnings/concepts/research-report-efficient-execution.md), [run checkpoint](templates/research-run.md) and [build manifest template](templates/report-build.json). `python tools/report-workflow.py extract <pdf> --cache <folder>` caches full page-labelled text; `python tools/report-workflow.py run <build.json> --check` checks the configured commands and `run <build.json>` executes them with timings and output hashes. Document scope and final visual/source/model QA remain unchanged.
