# Research prompt builder: review before activation

Prepared 7 November 2026. **Review draft only. The installed skill and original
ZIP have not been changed.** This package is ready for you to inspect before
any installation or final activation.

## What the revision changes

The prompt builder now refers to the three supplied files as separate bundled
resources. Its main file contains a short routing instruction rather than the
full manual or JSON. The generated company prompt must include accessible paths,
one selected report family and a company-specific decision/page plan.

The current package explicitly locks a neo-brutalist dashboard style. A new link
could not override that. This draft replaces those conflicting style defaults
with the manuals' report construction and typography, and records the proposed
change in the plan header and learnings. The complete approved plan body is
preserved exactly. Company-document collection, document-scope question, worker
model assignments, core research topics, valuation rules and section order remain.
The builder still writes a prompt; report generation remains the later step.

| Resource | Required use |
|---|---|
| PDF manual | Formatted reading and review of the manual |
| Markdown manual | Main explanatory reference for structure, typography, depth, process and page examples |
| Agent JSON | Select relevant physical-page records and font/geometry measurements; request coordinates only for selected layouts |

All three original files are included under `reference/report-design/`, unchanged.
Original links, sizes and hashes are retained in its manifest. A signed-in Library
session is not needed for normal use of the packaged resources.

## Checks completed

- Original preservation gate before editing: PASS, 111 of 111 checks.
- Revised preservation/reference gate: PASS, 129 of 129 checks.
- Seven offline regression tests: PASS. They cover original resource integrity;
  selective JSON and coordinate retrieval; selective manual retrieval; portable
  staging and overwrite protection; generated-prompt assembly plus the existing
  prompt checker; missing slots and invalid pages; missing or tampered resources.
- All Python scripts parse. The main SKILL.md is 146 lines.
- All three resources match their originals byte for byte: 7 reports, 239 physical
  pages and 6,417 text regions. Approved-plan body also matches byte for byte.
- The assembly fixture is explicitly synthetic. Its prompt checker passes with
  the following existing warning(s): WARN  size  :: 36.2 KB, outside the concise band of 15 to 25 KB; it is a plumbing test, not investment research.
- No live company research, Screener access, Sonnet workers, report rendering or
  installed-skill execution was performed. Those are not claimed as tested.

## Exact additions to the main skill

The following is the actual routing instruction:

- `reference/report-design/guide.md`: how to consult the three separately bundled design references. Read this router, then only the relevant manual chapters and JSON page records. The PDF is the reading/review copy. Do not paste the manuals or full JSON into the skill or generated prompt.

The following are the actual new diagnosis/staging steps:

15. Report design: follow `reference/report-design/guide.md`. Verify the supplied files with `python SKILL_DIR/scripts/report_references.py check`. Select one family (BF, MP, CC, EL, SU, AX or MQ) for the economics and scope. Read the applicable manual chapters and selected physical source pages; use JSON measurements selectively, never all 6,417 rectangles. Log the chapters/pages actually read and the reason for the family. Build a company-specific page plan linking decision questions to evidence/calculations, source page IDs, exhibit forms and justified adaptations. Preserve the existing core coverage and valuation rules.
16. Stage the pack for the later research run: `python SKILL_DIR/scripts/report_references.py stage --dest "<absolute company research folder>/references/report-design"`. This copies the three references, guide, manifest and portable reader. Keep them distinct from company factual sources. Recover missing/unreadable files before releasing a prompt that claims reference compliance. The historical neo-brutalist style is superseded only as recorded in the 7 November 2026 reference-design amendment in `reference/learnings.md`.

The writing step now reads:

1. Copy `assets/skeleton.txt` to a draft and fill every `{{SLOT}}` for this company. Text after the colon in a slot is an instruction, not text to keep.
2. Leave the `{{INCLUDE:6A}}`, `{{INCLUDE:7}}`, `{{INCLUDE:8}}` and `{{INCLUDE:8B}}` lines as they are.
3. Write a slots file (JSON) with seven keys: `ACCENT_MAPPING`, `TAG_LIST`, `DIAGRAMS`, `MUST_HAVE_CHARTS`, `VISUAL_PLAN`, `REPORT_PROFILE`, `REPORT_PAGE_PLAN`. `VISUAL_PLAN` is markdown table rows only, five cells each. `REPORT_PROFILE` is one family ID. `REPORT_PAGE_PLAN` is the six-column table specified in `reference/report-design/guide.md`, including its header and explicit physical source IDs such as BF-06. No full reference content is inlined.
4. Assemble: `python SKILL_DIR/scripts/assemble.py <draft> <slots.json> "<final prompt path>" --references-dir "<staged reference folder>"`. This pastes the current locked sections 6A, 7, 8 and 8B in word for word and inserts verified absolute paths to the staged references. The later report agent reads those files; copying links without a page plan is not sufficient.
5. Section 1 holds cited facts, conflicts and the "To find" list. Every local path in section 1 is absolute, in backticks, and exists.
6. Section 5: bear, base and bull are each marked `[E]`; base equals management guidance exactly; bull has the same earnings as base at a higher multiple; bear is built from the S19 risk cards; a management guidance table with a Source column sits alongside.

The new handoff check reads:

9. Reference handoff: confirm the three original resources match their manifest, every selected physical source page exists, the prompt carries accessible local paths and one declared family, and the page plan fits this company. Confirm the later report instructions require the manual's model-first process, page storyboard, rendered-page inspection and reader decision test. The checker verifies structure and access; it cannot prove that the agent read the files or produced good analysis.

## Exact contract passed to the later report agent

This is the actual section-7 asset. The assembler fills the short slots with
paths, the selected family, the page plan and company-specific exhibit choices.
It does not expand the manuals or full JSON into the prompt.

```markdown
## 7. Design system

Locked reference contract. Fill only the reference handoff, family, page-plan table and company lines. The 7 November 2026 reference-design amendment supersedes the historical neo-brutalist styling in the approved plan.

Report-design reference directory: {{REPORT_REFERENCE_DIR}}
Reference handoff:
{{REPORT_REFERENCE_FILES}}
Reference family selected for this company:
Report design family: {{REPORT_PROFILE}}

Before planning pages, open the staged guide and applicable Markdown sections, then query the selected JSON page records. Use the PDF manual for formatted review. These design and analytical-method references are separate from primary evidence for the new company. Source IDs such as BF-04 mean physical PDF pages, not printed numbers. Log what was actually read; links alone do not establish compliance.
Read selectively: use the guide's chapter and page routing. Query coordinates only for a selected layout. Never paste the full manuals, 239-page audit or all 6,417 rectangles into this prompt or every worker context. If a required file cannot be read, recover it or report the exact blocker; do not silently substitute a generic design.
Process: source manifest and business map, evidence ledgers, reconciled operating/financial model, thesis and contrary evidence, exhibit register, page storyboard, deterministic layout, numerical/editorial review, rendered-page review and reader decision test. Write the executive summary last. The later report agent uses manual section 9's page-specification schema. The prompt builder itself stops at the prompt.
Depth: connect each material thesis through driver, mechanism, primary evidence, timing, earnings/cash effect, capital need and a disconfirming signal. Preserve the existing coverage and valuation rules. Historical broker forecasts, recommendations and prose are never evidence for the new company.
Output: one self-contained HTML file, report.html, in the research folder. Keep Chart.js 4.4.1 from https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js plus inline SVG, with no new chart library. The pinned CDN remains the existing offline exception; disclose unavailable dependencies. Use local/system fonts or embedded licensed font files.
Theme: light by default, white analytical field, dark ink, one restrained family accent and neutral fills. No shadows, thick card borders, oversized KPI grids or decorative backgrounds. Use the new report's own identity, never broker logos, signatures, registrations or invented recommendation history.
Type and geometry: declare the family's measured values separately from chosen reconstruction values, using manual section 3 and the JSON. Name font substitutes and recheck wrapping. Recommended A4 starting values: 595.28 x 841.89 pt; 36 pt side margins; 10 pt body with 13 pt leading; 13-14 pt headings; 8.5-9 pt tables; 7.5-8 pt sources; 0.35-0.6 pt rules. These are recommendations, not measurements of every source page. Keep screen text readable, about 15px where needed, while retaining the declared print sizes. Split dense content before shrinking labels below the chosen floor.
Layout: one coherent family and a document-width field with aligned narrative, exhibits and captions. Desktop contents sit outside that field and become a top menu under 768px. Every S-section has an id and a contents entry. Business and Products precede peers and financials; detailed valuation and verdict remain last. Borrow analytical components without mixing publishers' visual systems. Page and chart counts follow evidence, never a source quota.
Section opening: every S-section starts with the answer in one bold line, then evidence, then a short unboxed note titled "What this means for you". Place management explanations beside the relevant numbers. Prefer plain narrative, tables and source notes over repeated cards.
Tables: restrained header bands and hairline total rules; right-aligned comparable numbers; units and fiscal periods in headers; consistent precision; negative numbers in brackets. Use the chosen face's tabular numerals. Mobile overflow stays inside the table container. Repeat headers for long printed tables and split deliberately when needed.
Charts: one y-axis, honest scales, units, periods and adjacent sources. Distinguish reported, guidance [G] and estimates [E] with text and pattern or line treatment. Interactive charts have working hover tooltips; static SVG has labelled values or a table view. Every chart must remain intelligible in print and match the reconciled model.
Diagrams and images: editable inline SVG text for exact flows; real company deck, annual report or website images with source captions only. Never stock or generated imagery for company evidence, financial tables or precise charts.
Scroll and print: native scrolling; never hide overflow on html or body, trap the wheel in charts, or fix section heights. Print hides controls and navigation, preserves all in-scope sections and sources, and avoids clipped exhibits, orphaned headings and accidental blank pages. Inspect the actual page transitions.
Accessibility and tags: colour is never the only signal; text contrast at least 4.5 to 1; labelled values or tables make charts accessible. [E] shows working; [G], [Inferred], [Not Disclosed] and source tags remain compact textual labels. OK, WATCH and RED include the word as well as colour. Avoid a pill around every number or source.

Report page plan:
{{REPORT_PAGE_PLAN}}

Each row connects a company decision, evidence/calculation task, physical source precedents, form and justified adaptation. The later report agent expands it into page specifications and compares actual rendered pages with the selected precedents. Report departures and missing evidence.
Accent mapping: {{ACCENT_MAPPING}}
Company tags: {{TAG_LIST}}
Diagrams to draw: {{DIAGRAMS}}
Must-have charts: {{MUST_HAVE_CHARTS}}
```

## Full new reference-routing instructions

The text below is the new `reference/report-design/guide.md`. This is the compact
instruction layer that routes to the much larger supplied manual and JSON.

### Report-design reference guide

Read this guide before drafting a report-producing company prompt. Keep the
three resources separate. Do not paste them into SKILL.md, generated prompts or
every worker's context. The prompt builder stops at the prompt; the later report
agent performs the report-production steps below.

#### Three resources, three roles

| File beside this guide | Role | When to use |
|---|---|---|
| `Equity_Research_Design_Page_by_Page_Manual.md` | Explanatory authority for report architecture, typography, analysis depth, process and page-by-page transfer | Planning and production, using selected chapters and page entries |
| `Equity_Research_Design_Agent_Specification.json` | Report/page records, measured fonts, geometry and 6,417 text-region rectangles across 239 physical source pages | Select precedents and query measurements for particular pages |
| `Equity_Research_Design_Page_by_Page_Manual.pdf` | Formatted reading and review version of the same manual | Human review; it is not a bundle of all original brokerage page images |

The PDF and Markdown contain the same manual. JSON supports the explanation
with measurements. None supplies factual evidence for the new company.
`manifest.json` preserves supplied filenames, hashes and original Library links.
Use local packaged copies normally; use those links to recover a missing file.

#### Selective reading

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

#### Choose one family

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

#### Builder handoff

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

#### Later report-agent sequence

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

## Code and workflow changes available for inspection

Changed original files:

- `SKILL.md`
- `assets/design-system.txt`
- `assets/skeleton.txt`
- `assets/visual-check.txt`
- `assets/visual-intelligence.txt`
- `assets/visual-review.txt`
- `reference/learnings.md`
- `reference/plan.md`
- `reference/visual-intelligence.md`
- `scripts/assemble.py`
- `scripts/check_prompt.py`
- `scripts/check_skill.py`

Added resources include the guide, manifest, the three original files, a stdlib
reader/staging helper and seven runnable regression tests. `assemble.py` now
requires `--references-dir`, plus `REPORT_PROFILE` and `REPORT_PAGE_PLAN` in the
slots JSON. It refuses inaccessible or mismatched resources and invalid source
page IDs. The prompt checker checks the same handoff. Staging will not overwrite
a different existing reference, and assembly still refuses prompt replacement.
The reader's default output omits coordinate rectangles; `--regions` opts in.

## Review decision

This document and ZIP are review copies. No installed personal skill, external
repository or user research prompt has been updated. Approval is still pending.
