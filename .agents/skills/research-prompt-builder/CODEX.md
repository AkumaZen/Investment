# Codex installation notes

Installed from the user-supplied `research-prompt-builder-review.zip` on 2026-11-07. Installation was explicitly requested; the archive README describes its earlier review-only packaging state.

## Paths in this repository

Resolve paths from the repository root, not the shell working directory. In Codex, this table replaces the Claude-specific path table in SKILL.md:

| Item | Repository path |
| --- | --- |
| SKILL_DIR | `.agents/skills/research-prompt-builder/` |
| Generated prompts | `research/companies/<exchange>-<ticker>/prompts/<Company> Research Prompt.md` |
| Company research folder | `research/companies/<exchange>-<ticker>/` |
| Cached documents | `research/companies/<exchange>-<ticker>/docs/<TICKER>/` |
| Fact pack | `research/companies/<exchange>-<ticker>/facts.md` |
| Scratch notes | `research/companies/<exchange>-<ticker>/prompt-notes.md` |

Use absolute paths in generated prompts and preserve the versioning/no-overwrite rule. Existing research outside this repository may be read when relevant; save new work here unless the user requests another location. The approved historical plan and bundled reference resources remain unchanged.

## Runtime requirements

User-approved efficient-execution amendment (10 Nov 2026): read `learnings/concepts/research-report-efficient-execution.md` from the repository root. Reuse full hashed extracts and complete reader outputs, use bounded Luna handoffs (low for routine extraction/indexing, medium for analytical work and verification), and preserve all document/analysis/QA requirements. Standing default scope is latest annual report, all historical calls/decks, latest results, material announcements, relevant RHP and uploads. Future prompts include first-build product imagery, PDF navigation and density checks; execution of an existing prompt never rebuilds it. `tools/report-workflow.py` supplies extract caching and a fail-fast ordered build runner; templates live in `templates/research-run.md` and `templates/report-build.json`.

- Screener MCP is registered as `screener`. Its `search_company`, `get_document_list`, and financial tools provide the data this workflow expects. Tool naming varies by client; select the registered server's matching tool instead of depending on Claude's exact `mcp__screener__` prefix.
- Python and PyMuPDF are available on the installation machine. PDF rendering uses PyMuPDF; most bundled checks use only the standard library.
- Latest user-approved amendment (2026-11-10): use gpt-6-luna with reasoning_effort="low" for routine extraction/indexing and reasoning_effort="medium" for interpretation, comparisons, reconciliation, valuation and final verification. Mixed or ambiguous assignments use medium. Use fork_turns="none" and bounded task context. This supersedes the earlier blanket-medium rule and older Sonnet/GPT-6.1 Sol assignments. Keep file-based milestone checkpoints. The user declined optional compaction: do not initiate manual compaction or configure a custom automatic threshold. Built-in runtime context management is unchanged.
- `business-valuation-scenarios` is installed at `C:\Users\Rohit Negi\.codex\skills\business-valuation-scenarios\SKILL.md` (verified 10 Nov 2026) and is referenced, not bundled. Read it when selecting the valuation metric and require the later research run to read it before building the valuation. `dataviz` is referenced but was not bundled and was not found in the standard local skill directories at installation. Obtain the intended originals before a run needing them; do not fabricate the missing valuation table or chart library. Other external design skills are optional under the supplied workflow.
- Claude-specific `Agent`, `Skill`, and `AskUserQuestion` calls describe capabilities. Use equivalent available tools only when they satisfy the same requirements. Existing `.claude/agents` files are left untouched.

## Validation

From the repository root:

```powershell
python .agents/skills/research-prompt-builder/scripts/check_skill.py
python .agents/skills/research-prompt-builder/scripts/test_report_references.py
python .agents/skills/research-prompt-builder/scripts/report_references.py check
```

These checks validate packaging and the reference handoff, not the financial conclusions or external worker availability. See `docs/screener-mcp.md` for MCP setup. Invoke this installed skill with `$research-prompt-builder` on the next turn. Restart Codex to load the newly registered MCP server.
