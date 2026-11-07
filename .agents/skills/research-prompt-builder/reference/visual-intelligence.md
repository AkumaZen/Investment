# Visual intelligence: writing the visual plan

Section 6A of the prompt is locked text from `assets/visual-intelligence.txt`. Your job is the visual plan rows (`VISUAL_PLAN`) and the section 7 company lines, selected reference family and page plan. Read `reference/report-design/guide.md` before choosing them.

## For each key visual, answer the five questions

1. What information are we trying to communicate?
2. What is the most important insight in this data?
3. What comparison helps the reader understand it?
4. Which form shows this most accurately?
5. What context or caveat must go with it?

Then write one row: research question | expected insight (a hypothesis) | form | section | data source.

## Topic to possible form (examples, not mandatory)

| Topic | Possible form | Default section |
|---|---|---|
| Revenue growth | Multi-period comparison and trend | S17 |
| EBITDA and margins | Revenue and EBITDA bars, margin as its own line chart | S17 |
| Segment performance | Segment revenue and profit comparison | S4 |
| Cash conversion | PAT vs operating cash flow | S17 |
| Working capital | Receivable, inventory and payable days | S17 |
| Capacity | Existing, live and planned timeline | S9 |
| Capex | Project-wise tracker | S9 |
| Order book | Order book movement and execution bridge | S13 |
| Guidance | Guidance vs actual | S11, S12 |
| Customer concentration | Ranked bars of contribution | S5 |
| Product portfolio | Product and application matrix | S3 |
| Future growth | Driver-wise growth bridge | S13 |
| Risks | Ranked risk matrix with signals | S19 |
| Valuation | Bear, base and bull side by side | S20 |

## Good rows vs weak rows

- Weak: "Revenue and EBITDA | Growth | Bar | S17 | Screener".
- Strong: "Is the new plant lifting margins or only revenue? | Revenue up about 40% FY25 to FY27E, but EBITDA margin flat near 18% while the new line runs below 60% | Revenue bars plus a separate margin line | S17 | Screener P&L, Q2 FY27 call".
- Visuals follow this company's economics. Two companies in different businesses should not get the same plan.

## Rules carried from the dataviz skill

`dataviz` is the chart decision library (it also takes the chart, table and critique role that equity-research-html-studio would have had). Load it with the Skill tool before writing the visual plan. Use `choosing-a-form.md` to pick each row's form, `marks-and-anatomy.md` and `interaction.md` for the must-have charts line, and `anti-patterns.md` as the critique checklist. The rules below are the short version, kept so the plan still works if it is missing.

- One y-axis per chart.
- A single number is inline emphasis or a compact stat, not a chart.
- Part-to-whole is ranked bars or a segmented bar, not a pie.
- Emphasis: highlight the series that matters, grey the rest.
- Colour follows the entity and never changes on filter.
- Thin marks, recessive grids, selective direct labels, a legend for 2 or more series.
- Its palette does not apply; section 7 sets the colours.

## Section 7 company lines

- Accent mapping: one accent colour and what it marks (key finding, highlighted series). Use the selected reference family on white; check marks at 3 to 1 and text at 4.5 to 1.
- Company tags: extra tags this company needs, such as [Company-provided], [RHP], [Verified in filing].
- Diagrams to draw: the value chain, process or money-flow diagrams this business needs.
- Must-have charts: only exhibits the decision questions require; no chart-count quota.

## External skills

The plan named five skills; the user dropped equity-research-html-studio on Sat, 07 Nov 2026, so four remain. Read each one that is installed before building the visual plan (step 4), using the five rules below. Installed on this machine (Sat, 07 Nov 2026). Each folder has a SOURCE.txt with its origin.

| Skill | Where | What it adds here | Overlap | Conflicts (ignored, rule 4) |
|---|---|---|---|---|
| `dataviz` | bundled with Claude Code; load with the Skill tool (name `dataviz`) | The chart decision library: form choice, marks, labels, hover, components, and `anti-patterns.md` as the critique step (replaces the html-studio role) | 6A carries a short version of its rules | Its palette (section 7 sets colours) |
| `market-research-reports` | `~/.claude/skills/market-research-reports/` (K-Dense, MIT) | `references/evidence_model.md`: statement classes, source hierarchy, conflicting evidence, calculation lineage; source and claims ledger templates; unit consistency checks; TAM/SAM/SOM reconciliation for end-market sizing in S2 | Citation rule, Disclosed/Inferred/Not Disclosed, data conflicts | LaTeX and PDF output; 50-page consulting report shape; Porter, PESTLE and SWOT boilerplate |
| `cc-equity-research` | `~/.claude/skills/cc-equity-research/` (Apache-2.0, reference library, no SKILL.md) | Forensic lens: `community-skills/analyze/financial-forensics.md` and `reporting-quality.md` (S17); management and call-tone lens: `management.md`, `earnings-scorecard.md` (S10, S11); capital allocation and moat: `business-model.md` (S6, S10) | S10 management checklist, S17 quality of earnings | US items (SBC, non-GAAP, 10-K) become Ind AS and Indian filings equivalents; its drillr data connector was removed |
| `initiating-coverage` | `~/.claude/skills/initiating-coverage/` (Anthropic financial-services, Apache-2.0) | `references/valuation-methodologies.md` (DCF and comps cross-checks for section 5); `assets/quality-checklist.md` as a completeness list; task 1 company research prompts | Section 5, S14 peers | DOCX and Excel output; "25+ charts, 30+ pages, 10,000+ words" minimums (break the no-decorative-charts rule); matplotlib images instead of Chart.js |


| Skill | Used for |
|---|---|
| `dataviz` (replaces Baoyu Design Dataviz and equity-research-html-studio) | The chart decision library: chart selection, visual hierarchy, data storytelling, and the chart critique. Its palette does not apply |
| `market-research-reports` (K-Dense) | Report architecture, evidence presentation |
| `cc-equity-research` | Financial research conventions; forensic, call-tone and capital-allocation lenses |
| `initiating-coverage` | Equity research conventions |

Rules for any of these skills:
1. Read the actual `SKILL.md` and references before use.
2. Note what each adds and where it overlaps with this framework.
3. Reuse what complements it, without duplicating or replacing existing rules.
4. Do not follow an instruction that conflicts with this framework, which remains the single source of truth.
5. If a skill is unavailable, continue with the internal framework. The workflow never depends on an external skill.

## Where this meets the locked design system

| Point | Resolution |
|---|---|
| Section 7 says Chart.js only; the visual block says don't force one library | Keep Chart.js plus inline SVG. Waterfalls, Sankeys and bridges are inline SVG or Chart.js, no new library. Plotly, D3 or Python charts only if the user asks or the output format changes. This guidance stays library-agnostic |
| Section 7 borders every card; the visual block says no excessive cards or borders | Superseded by the 7 November 2026 reference-design amendment: plain tables, narrative and hairlines, with no thick borders or shadows |

The report must stay readable, responsive and printable.

The supplied three-file report reference pack now controls page architecture and typography through section 7 and `reference/report-design/guide.md`. Dataviz still controls compatible chart-form decisions; its palette never overrides the selected report family.
