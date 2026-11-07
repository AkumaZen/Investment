# Report-design reference guide

Read this guide before drafting a report-producing company prompt. Keep the
three resources separate. Do not paste them into SKILL.md, generated prompts or
every worker's context. The prompt builder stops at the prompt; the later report
agent performs the report-production steps below.

## Three resources, three roles

| File beside this guide | Role | When to use |
|---|---|---|
| `Equity_Research_Design_Page_by_Page_Manual.md` | Explanatory authority for report architecture, typography, analysis depth, process and page-by-page transfer | Planning and production, using selected chapters and page entries |
| `Equity_Research_Design_Agent_Specification.json` | Report/page records, measured fonts, geometry and 6,417 text-region rectangles across 239 physical source pages | Select precedents and query measurements for particular pages |
| `Equity_Research_Design_Page_by_Page_Manual.pdf` | Formatted reading and review version of the same manual | Human review; it is not a bundle of all original brokerage page images |

The PDF and Markdown contain the same manual. JSON supports the explanation
with measurements. None supplies factual evidence for the new company.
`manifest.json` preserves supplied filenames, hashes and original Library links.
Use local packaged copies normally; use those links to recover a missing file.

## Selective reading

1. Read manual sections 1-3 for evidence classes, report families and measured
   versus recommended typography. Read sections 5-9 for depth, page archetypes,
   sector transfer, production and acceptance criteria. Read section 10 before
   approval. These front chapters are much shorter than the full page audit.
2. Read the relevant worked examples in section 4 and selected entries from
   section 12. Include the chosen family's first analytical page and enough
   precedents to solve the material company questions. There is no page quota.
3. Query matching JSON records by report ID and **physical PDF page number**.
   `BF-04` means physical page 4, not printed page 4. Keep physical page,
   printed page and source link distinct; cover offsets vary by report.
4. Preserve the evidence classes: measured, observed, interpretation,
   recommended and inferred process. Text rectangles can merge columns or
   chart labels; they are not a semantic layout tree or exact CSS frame map.
5. For a close visual match, inspect the original brokerage page through its
   JSON `source_link`. The manual PDF does not replace that page image. Record
   unavailable source images as a gap; never claim an exact match from boxes.

The stdlib helper selects content without dumping the corpus:

```text
python SKILL_DIR/scripts/report_references.py check
python SKILL_DIR/scripts/report_references.py index
python SKILL_DIR/scripts/report_references.py index --report BF
python SKILL_DIR/scripts/report_references.py manual --sections 2 3 5 6 7 8 9 10
python SKILL_DIR/scripts/report_references.py manual --pages BF-04 BF-06 BF-14
python SKILL_DIR/scripts/report_references.py pages BF-04 BF-06 BF-14
python SKILL_DIR/scripts/report_references.py pages BF-06 --regions
python SKILL_DIR/scripts/report_references.py stage --dest "<absolute company research folder>/references/report-design"
```

`pages` omits individual rectangles unless `--regions` is requested. `manual`
refuses a full section-12 dump. Staging includes the three resources, this guide,
manifest and a portable copy of the reader. A later research run can execute
that copy without the installed skill.

## Choose one family

| ID | Best editorial use | Useful physical page IDs |
|---|---|---|
| BF | Thesis-led manufacturing and capital transformation | BF-02 executive; BF-04, BF-05 operating chart sequence; BF-06, BF-07, BF-08 asset/ramp; BF-14, BF-15 returns; BF-16, BF-17 valuation |
| MP | Retail unit economics, value chain and store cohorts | MP-01 executive; MP-02 value chain; MP-10, MP-11, MP-12 cohorts; MP-19 unit example; MP-26 risks; MP-27, MP-28 model/value |
| CC | Processing, commodity exposure, capacity and cash | CC-01 executive; CC-09 revenue model; CC-15, CC-16 capacity; CC-19, CC-20, CC-21, CC-22 capex/cash/commodity; CC-24, CC-25 model/value |
| EL | Engineering products, commercial gates and turnaround | EL-01 executive; EL-10 unit economics; EL-18, EL-19, EL-20 programme conversion; EL-23, EL-24, EL-25, EL-26 turnaround; EL-32, EL-33 model/value |
| SU | Diversified groups, segment chapters and acquisitions | SU-02 executive; SU-03 business map; SU-05 through SU-15 divisions; SU-16 through SU-23 capital allocation/economics; SU-27 assumptions; SU-28 risks |
| AX | Sector mechanisms compared across companies | AX-02 thesis; AX-05 taxonomy; AX-15 through AX-21 demand transmission; AX-26, AX-27 peers; AX-28 risks; AX-42 process |
| MQ | Recurring quarterly updates for an understood company | MQ-01 executive; MQ-02 results bridge; MQ-03 monitoring; MQ-04, MQ-05 call evidence; MQ-06 model |

Select one ID as `REPORT_PROFILE`, explaining why it fits the economics and
scope. Keep that family's visual grammar. Borrow analytical components from
other reports without mixing their fonts, colours and gutters. Adapt the
economic unit: an API company needs qualification and yield; a GPU cloud needs
billable resource-hours. Banks and insurers need a different financial model.

Keep the existing core topics and section order. The executive snapshot can
mention value, but detailed valuation and verdict remain last. Do not inherit
late business-background placement that breaks Business and Products before
peers and financials. Do not copy source page counts, broker disclosures or
irrelevant content. A small sample retains depth for its actual stated scope.

## Builder handoff

Record the family and reason, manual sections and source pages actually read,
missing evidence and adaptations in `prompt-notes.md`. Stage the resources in
the company research folder before assembly. The assembler inserts existing
absolute paths for all three, this guide and the portable reader. Bare chat
links or an installed-skill-only path are insufficient for the later run.

Write `REPORT_PAGE_PLAN` as a table with these exact six columns:

| Destination section | Decision question | Source page IDs | Evidence and calculations | Form | Adaptation or omission |
|---|---|---|---|---|---|
| S9 capacity and capex | Can qualified output support the forecast sales? | BF-06, BF-07, CC-16 | Dated company asset ledger; available capacity by quarter x utilisation x yield x realisation; funding and working-capital bridge from primary filings | Narrative, asset tracker and output bridge | Keep BF typography; borrow CC reconciliation; split dense exhibits; flag missing qualification dates |

This illustrates structure, not a compulsory industrial template. Write
company-specific rows covering the opening argument, business/unit economics,
material growth and capital questions, contrary evidence and valuation when
in scope. Keep the existing coverage-map entry for every other core topic.
Say why a visual or source pattern changes or is omitted. Name new-company
sources or research tasks in the evidence cell, never an old broker forecast.
Expected conclusions remain hypotheses until the evidence supports them.

Keep full manuals, all 6,417 rectangles, source prose, forecasts,
recommendations, logos, signatures and registrations out of the prompt.
Use precise page IDs for retrieval. Merely listing links is not reference use.

## Later report-agent sequence

1. Open this guide, applicable Markdown chapters and selected JSON records
   before planning pages. Log what was read. Separate design sources from
   company evidence in the source manifest.
2. Build source/evidence ledgers and a reconciled operating/financial model.
   Connect each important claim through driver, mechanism, primary evidence,
   timing, earnings/cash effect, capital need and a disconfirming observation.
   Keep reported, guidance [G], estimates [E], calculations and unknowns distinct.
3. Expand the section plan into the page-specification schema in manual
   section 9. Every page needs a question, supported answer, evidence, exhibit
   inputs, interpretation, limitation and next question. Flowing HTML still
   needs its final printed page boundaries checked.
4. Declare page geometry, type roles, fonts or named substitutes, leading,
   margins, columns, table text, captions and semantic colours from section 3.
   Separate observed measurements from recommended reconstruction tokens.
   Apply readable type floors; repaginate instead of copying tiny statement
   or legal text. Use white analytical fields, restrained accents and hairlines,
   without shadows, thick dashboard borders or giant KPI cards.
5. Generate editable HTML/SVG/Chart.js exhibits from the same model and write
   the executive summary last. Explain terms and use a worked unit example
   where useful. Put source notes directly beneath the relevant exhibits.
6. Run all existing numeric, source, desktop, mobile, print and visual checks.
   Inspect every rendered page and dense table at normal reading size. Compare
   selected precedents with the actual output; record justified departures.
   Check reading order, alignment, source association, clipping, page transitions
   and actual/forecast distinctions. Unrun checks are NOT RUN, never PASS.
7. Test whether an unfamiliar reader can explain the business, reproduce one
   unit or forecast calculation, identify its capital constraint and name a
   thesis-break signal. Deliver source/model traceability, reference-use notes
   and remaining gaps with the report.

If a required file is missing, unreadable or changed without a deliberate
version update, do not release a prompt claiming reference compliance. Restore
it from the bundle or original link; if recovery fails, report the exact blocker
and continue only work independent of that missing resource.
