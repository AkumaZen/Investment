# Research prompt builder: reference-design review draft

Prepared 7 November 2026. This ZIP is for the user's verification. It does not
install or update an active skill. Keep the existing installation until this
revision is approved. The internal skill name remains research-prompt-builder.

The update adds the supplied PDF manual, Markdown manual and agent JSON as
separate resources under reference/report-design/. SKILL.md routes to guide.md;
it does not contain the manuals or the 6,417 text-region coordinates.

The builder selects a report family and a company-specific decision/page plan.
It stages the resources beside company research so the later report agent can
open them. The generated prompt includes short binding instructions, accessible
paths and selected physical-page IDs. It never substitutes old broker forecasts
for the new company's primary evidence.

Read reference/report-design/guide.md for the exact workflow. The supplied three
files are unchanged. Their manifest retains original links, sizes and SHA-256
hashes. The original approved plan body is unchanged; its header and learnings
record the proposed styling supersession explicitly.

The active defaults change from heavy bordered dashboards to the referenced
report families: restrained document typography, tables, source notes and
hairline rules. The company-source, Sonnet worker, section coverage and
valuation workflow stays in place. No external skills are newly installed.

## Python commands

From this folder (Python 3.9+; standard library only for the new reference path):

```text
python scripts/check_skill.py
python scripts/test_report_references.py
python scripts/report_references.py check
python scripts/report_references.py index
python scripts/report_references.py pages BF-06 --regions
python scripts/report_references.py stage --dest "<absolute company research folder>/references/report-design"
python scripts/assemble.py <draft.md> <slots.json> <new-prompt.md> --references-dir "<staged reference folder>"
python scripts/check_prompt.py <new-prompt.md>
```

The seven required slot strings are ACCENT_MAPPING, TAG_LIST, DIAGRAMS,
MUST_HAVE_CHARTS, VISUAL_PLAN, REPORT_PROFILE and REPORT_PAGE_PLAN. The last is
a six-column table whose exact header and example are in guide.md. The assembler
refuses missing references and invalid page IDs; it still refuses prompt
replacement. Staging refuses to overwrite a different existing reference.

The validators check structure, integrity and file access. Reading the references,
research quality, financial accuracy and rendered output still require the
explicit human/agent review steps. A packaging test is not a completed company
research run or a test of the user's external Screener and worker services.
