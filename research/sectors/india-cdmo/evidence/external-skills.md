# External research-skill review for the CDMO prompt

## Files read

- `~/.claude/skills/market-research-reports/SKILL.md` and `references/evidence_model.md`.
- `~/.claude/skills/cc-equity-research/SKILL.md`; lens references `community-skills/analyze/{financial-forensics,reporting-quality,management,earnings-scorecard,business-model}.md`.
- `~/.claude/skills/initiating-coverage/SKILL.md`, `references/valuation-methodologies.md`, and `assets/quality-checklist.md`.

## Additions to preserve in the CDMO prompt

- Define the CDMO market before sizing: service scope/stage, buyer, geography, period, revenue vs capacity measure, currency/base, taxonomy and inclusions/exclusions. Reconcile non-overlapping top-down and bottom-up views; preserve residuals, source conflicts, scenario ranges and assumptions rather than claiming a single certain TAM.
- Maintain linked source and claim IDs. Record source producer, dates/vintage, scope, units/denominator, method, limitations and local snapshot. Every material statement is classified as fact, estimate, calculation, forecast, opinion or recommendation; cite calculation inputs and separate assumptions.
- Extend CDMO conversion analysis through program/service stage, customer concentration, qualification/validation, timing, capacity, yield, realized price and repeat commercial work. Unknown public customer/program details remain unknown.
- Add earnings-quality/comparability checks: cash conversion, receivables/inventory vs revenue, capex/capitalization policy, adjusted-vs-reported gap, definition drift, segment recuts, reclassifications and restatements; recompute on old definitions where possible.
- Management review can cover capex/M&A outcomes, disclosed compensation alignment, ownership/promoter/insider changes and leadership transitions, using Indian filings and time periods the evidence supports. Transcript analysis should compare full call language and guidance with later actuals; use tone scores only as an evidence-backed optional lens, not a standalone conclusion.
- Valuation should show traceable DCF and peer methods, operating bear/base/bull drivers, WACC/cash-flow consistency, dilution/net debt, sensitivity and sanity checks. Precedent M&A only when relevant transactions have comparable scope and usable public evidence. Present a range and explain method weights; do not inherit canned valuation assumptions.

## Overlap and conflicts resolved

- **Overlap:** market research evidence discipline reinforces the project rules for primary sources, dated evidence, explicit assumptions, reproducible math and disconfirming evidence. Financial forensics, reporting quality, business model, management and earnings scorecard add checklists that fit the planned risks, economics and company templates.
- **India adaptation:** CC Equity Research explicitly says its upstream source is wired for US/Japan data; apply its India mapping (annual reports and notes, quarterly filings/limited review, SEBI LODR disclosures, promoter/pledge data, ESOP dilution, INR crore and April–March periods). Its US-centric numeric thresholds are only starting points. Quarterly cash-flow/balance-sheet series may not exist; use half-year/year periods and label the substitution.
- **Design conflict:** Initiating Coverage defaults to Times New Roman, whereas the selected AX visual family is measured in Arial. The design handoff governs visual reconstruction: use its measured family where available, or a named tested substitute; no mixed typography.
- **Scope/production conflict:** Initiating Coverage imposes a five-request, one-task-at-a-time sequence and a hard 30–50-page, 25–35-chart, 10k–15k-word DOCX minimum, while the report-design manual says report length and page count should follow actual scope/evidence. These are not adopted as fixed requirements for a CDMO sector prompt. Preserve the existing project prompt/scope and user-authorized workflow; deliver depth proportionate to actual coverage and evidence.
- **Valuation conflict:** valuation reference describes US Treasury/CAPM conventions, generic maintenance-capex ranges, typical growth, peer counts, transaction premiums and weighted method ranges. These are examples only. Require India-appropriate dated inputs, explicit model choices and source support; never import its example assumptions or force precedent transactions.
- **Quality-checklist conflict:** its fixed checklist requires extensive documents, charts and workbook tabs unrelated to this prompt-building handoff. Retain its useful cross-file/source/number consistency principle when reports are built, but do not impose its page/chart/word/table quotas or a DOCX/XLS deliverable format here.
- **Skill citation note:** market-research-reports asks for a Scientific Agent Skills paper citation if it materially contributes to a released report/code. This is a prompt-design handoff, not a public report/code release; no research-paper citation was added.

## Preserved original AX source

Copied the recovered Axis Securities Building Materials initiating-coverage PDF to `references/originals/Axis_Building_Materials_Initiating_Coverage_2025-07-16.pdf`. Its `source_link` and visual-review details are documented in `evidence/design-notes.md`. It remains a design reference only, not CDMO evidence.
