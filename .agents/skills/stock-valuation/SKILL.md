---
name: stock-valuation
description: Estimate stock value, compare valuation scenarios, or inspect valuation assumptions and calculations.
---

# Stock Valuation

Paths below are relative to the repository root.

1. Identify the security, valuation date, currency, reporting period, and valuation purpose. Follow the root AGENTS.md research rules.
2. Select and justify suitable methods: discounted cash flow, comparable multiples, asset value, or a sector-appropriate approach.
3. Source and reconcile inputs, including diluted shares, debt, cash, and relevant earnings or cash flows. Treat unavailable inputs as explicit gaps.
4. Calculate bear, base, and bull scenarios. Build and lay them out per the `business-valuation-scenarios` skill (`~/.claude/skills/business-valuation-scenarios/SKILL.md`), Steps 1 to 4: read it there, do not copy it. Show formulas, units, growth, margins, discount rates, terminal assumptions, and enterprise-to-equity adjustments where applicable.
5. Test sensitivity to the dominant assumptions and explain limitations. Use the valuation section of templates/stock-analysis.md for saved output.
6. Check each scenario is feasible against the business's constraint (for example capital: sales per rupee of equity versus the latest actual). With no management guidance, start the current year from reported half-year actuals and label every projected line as an estimate.
7. If the valuation is added to a report, run the visual verification step in learnings/concepts/equity-report-quality-process.md before calling it done.

Complete when calculations can be reproduced and the output separates sourced inputs, estimates, and scenario-dependent conclusions.
