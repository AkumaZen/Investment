---
name: stock-research
description: Research listed companies, assess financial quality, or build and update an evidence-backed investment thesis.
---

# Stock Research

Paths below are relative to the repository root.

1. Resolve the exchange, ticker, analysis date, and research horizon from the request. Mark unresolved scope before drawing security-specific conclusions.
2. Gather current filings, results, exchange disclosures, and relevant industry evidence under the root AGENTS.md research rules.
3. Explain the business, competitive position, financial trends, governance, and capital allocation. Distinguish evidence from interpretation.
4. Develop the thesis and strongest counterarguments. Use the stock-valuation skill when a valuation is requested.
5. Fill templates/stock-analysis.md, including sources, gaps, risks, and invalidation conditions. Save only to the requested location, or the standard company folder when saving is requested without a path.
6. When the output is a client report (HTML), follow learnings/concepts/equity-report-quality-process.md: plain language, a chart on almost every page, conclusion headlines, sources under each exhibit.
7. Visual verification is mandatory for every report build: run `node review.mjs <report.html>` in tools/report-visual-check, then look at every contact sheet and every changed or chart page at full size, desktop and phone. Fix, rebuild and repeat until both the script and the by-eye pass are clean. Record defects in the report's qa-notes.md.

Complete when material claims are sourced or marked unverified, the conclusion states remaining uncertainty and the next review trigger, and (for reports) the visual verification passed with its evidence recorded.
