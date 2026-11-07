# Screener MCP setup

The research prompt builder uses `search_company`, `get_document_list`, and financial-data tools from Screener MCP. The server is an external dependency, not vendored into this repository.

## This machine

An existing installation was reused from `D:/My Projects/Test/screener-mcp/` and registered with Codex under the name `screener`. Other MCP entries and Claude settings were preserved.

```powershell
codex mcp add screener -- "D:/My Projects/Test/screener-mcp/.venv/Scripts/python.exe" "D:/My Projects/Test/screener-mcp/run_server.py"
codex mcp get screener
```

The registration lives in the user's Codex configuration and is not committed. Restart Codex after registering a server. The [official MCP documentation](https://developers.openai.com/codex/mcp/) describes client configuration.

## Another machine

Use the [AkumaZen fork](https://github.com/AkumaZen/screener-mcp), matching this machine's installed implementation. Its local README specifies installing from this fork rather than the similarly named PyPI package.

```powershell
git clone https://github.com/AkumaZen/screener-mcp.git screener-mcp
python -m venv screener-mcp/.venv
& ./screener-mcp/.venv/Scripts/python.exe -m pip install ./screener-mcp
```

Register the absolute interpreter and `run_server.py` paths from the new checkout using the command above. For reproducibility, use the same source commit recorded below, or review and test a newer revision before updating.

Installed server source commit: `cbecb9cf135751890c6d280f50868fc3945f04ad`.

## Credentials and optional components

Public company search, financial data, and document lists work without credentials. Account-based stock screening needs `SCREENER_USERNAME` and `SCREENER_PASSWORD` in the server environment. Keep them outside tracked files. No credentials were added during this installation.

The prompt builder downloads documents and reads PDFs with its own scripts. It does not need Screener's optional ChromaDB/embedding stack to list documents. Its `pdf_pages.py --render` command needs PyMuPDF, available on this machine. On another machine, install it in the Python environment used for the skill scripts with `python -m pip install PyMuPDF`.

## Verified on 2026-11-07

- MCP initialization and tool discovery: passed; 21 tools exposed.
- Required `search_company`, `get_document_list`, and `get_financials` tools: present.
- Live `search_company` request for TCS: returned Tata Consultancy Services.
- Live `get_document_list` request for TCS: returned annual reports and earnings-call transcripts.
- Credentials: not configured; verified in public mode.

This checks the data connection. The skill's separate Sonnet worker and missing skill requirements are recorded in its [Codex notes](../.agents/skills/research-prompt-builder/CODEX.md).

## Existing environment audit

The installation audit checked 121 installed package versions from the reused Screener environment plus PyMuPDF. `pip-audit` reported advisories for four existing packages: `certifi`, `chromadb`, `pillow`, and `pypdf`. This is not a clean vulnerability audit. The shared environment was not upgraded during skill installation. These findings are separate from the passing MCP connection and bundled packaging tests.
