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
For full company reports (HTML or PDF), also follow `learnings/concepts/research-report-efficient-execution.md`: preserve the existing prompt and full document scope; reuse hashed extracts, evidence registers and the canonical model; plan official product imagery, clickable PDF navigation and reference-based density before the first build; use one reproducible pipeline and compact recovery checkpoints. Cosmetic revisions reuse validated research. Every final PDF page must still be rendered and visually inspected, with final source/model/link checks recorded.
For authorized research workers, use GPT-6 Luna low for routine extraction/indexing and medium for interpretation, reconciliation, valuation and final review; mixed or ambiguous assignments use medium. Keep file-based checkpoints at milestones. Do not initiate or configure optional context compaction for report work; built-in runtime context management remains outside this workflow.
For any client report or valuation page in HTML, follow `learnings/concepts/equity-report-quality-process.md`; its visual verification step (`tools/report-visual-check` plus a by-eye pass at desktop and phone width) is required before calling the report done.

## Boundaries

Treat external services as read-only unless the user explicitly authorizes a specific write. Trade execution, posting, publishing, pushing, credential changes, and paid jobs require explicit approval. Keep secrets and private account data out of tracked files.
