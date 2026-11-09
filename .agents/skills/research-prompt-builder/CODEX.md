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

- Screener MCP is registered as `screener`. Its `search_company`, `get_document_list`, and financial tools provide the data this workflow expects. Tool naming varies by client; select the registered server's matching tool instead of depending on Claude's exact `mcp__screener__` prefix.
- Python and PyMuPDF are available on the installation machine. PDF rendering uses PyMuPDF; most bundled checks use only the standard library.
- User-approved amendment (2026-11-07): use gpt-6.1-sol workers with reasoning_effort="low" and fork_turns="none" for readers, scanner and verifier. Supply complete task context. This supersedes historical Sonnet assignments.
- `business-valuation-scenarios` is installed at `~/.claude/skills/business-valuation-scenarios/SKILL.md` (found 10 Nov 2026) and is referenced, not bundled. `dataviz` is referenced but was not bundled and was not found in the standard local skill directories at installation. Obtain the intended originals before a run needing them; do not fabricate the missing valuation table or chart library. Other external design skills are optional under the supplied workflow.
- Claude-specific `Agent`, `Skill`, and `AskUserQuestion` calls describe capabilities. Use equivalent available tools only when they satisfy the same requirements. Existing `.claude/agents` files are left untouched.

## Validation

From the repository root:

```powershell
python .agents/skills/research-prompt-builder/scripts/check_skill.py
python .agents/skills/research-prompt-builder/scripts/test_report_references.py
python .agents/skills/research-prompt-builder/scripts/report_references.py check
```

These checks validate packaging and the reference handoff, not the financial conclusions or external worker availability. See `docs/screener-mcp.md` for MCP setup. Invoke this installed skill with `$research-prompt-builder` on the next turn. Restart Codex to load the newly registered MCP server.
