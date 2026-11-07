# Stock workspace instructions

## Scope

Use this repository for stock research, analysis prompts, analyst role briefs, and investment learnings. Read README.md for the layout.

## Research quality

- Resolve exchange, ticker, market, currency, and analysis date before researching a security.
- Verify current prices, filings, results, corporate actions, and material news using current sources. Prefer company filings, exchange disclosures, and regulator publications.
- Link sources beside material claims; identify reporting periods and distinguish reported facts, estimates, and judgments.
- Show valuation inputs, formulas, units, and assumptions. Use comparable accounting periods and explain adjustments.
- Mark missing information explicitly. When sources are unavailable, produce a clearly labeled incomplete draft rather than inventing figures or citations.
- Include downside cases, thesis invalidation conditions, and uncertainties in investment conclusions.

## Workflow routing

Use `.agents/skills/stock-research/SKILL.md` for company analysis, `.agents/skills/stock-valuation/SKILL.md` for valuation, and `.agents/skills/investment-review/SKILL.md` for decision reviews.
Read a role in `agents/` when its perspective is needed. Role briefs are instructions, not installed agent configurations; use them in the current session unless delegation is requested.
Use templates for saved output and keep reusable lessons separate from dated company observations.

## Boundaries

Treat external services as read-only unless the user explicitly authorizes a specific write. Trade execution, posting, publishing, pushing, credential changes, and paid jobs require explicit approval. Keep secrets and private account data out of tracked files.
