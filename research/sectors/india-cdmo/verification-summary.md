# Prompt verification summary

18 primary-source check rows were completed independently by the Luna medium verifier; all matched the issuer releases. A reproducible 10-row audit sample was then drawn from that fully checked population with seed 20261110. This is not a substitute for later company-report verification. See evidence/verification.md for source locations.

| Fact | Figure / scope | Source location | Result |
|---|---|---|---|
| API reactor volume | More than 4,000 kL at year-end; small-molecule API sites | “Small molecule D&M service remains strong,” line 77; repeated line 45  PASS |
| Phase II projects | 377; subset of the same D&M pipeline | Same section, line 76  PASS |
| Service backlog | US$11.5 billion, part of total backlog | Same  PASS |
| TIDES backlog | +20.2% YoY at year-end 2025; combined TIDES backlog | Same TIDES section, line 81  PASS |
| TIDES revenue | RMB 11.37 billion, +96.0% YoY; combined peptide and oligonucleotide business | “TIDES business (oligo and peptides) sustains rapid growth,” line 81  PASS |
| Potential milestone backlog | US$12.2 billion, part of total backlog; conditional/project-success dependent | Same; annual report calls it “upcoming potential milestone fees”  PASS |
| TIDES customer and molecule counts | D&M customers +25% YoY; molecules +45% YoY | Same TIDES section, line 82  PASS |
| D&M pipeline size | 3,452 molecules at year-end 2025; small-molecule D&M | Same section, line 76; total also line 44  PASS |
| Discovery-to-development conversions | 310 molecules converted from R to D phase during 2025 | “WuXi Chemistry” > small-molecule drug discovery service (“R”), line 73  PASS |
| Total backlog | US$23.7 billion at 31 Dec 2025 | FY2025 release, “Backlog” section; annual report p. 8  PASS |

Script-recomputed arithmetic:

```json
{
  "backlog_total_bn_usd": 23.7,
  "three_year_share_pct": 19.0,
  "molecule_total": 3452,
  "illustrative_incremental_sales_cr": 20.0,
  "illustrative_incremental_ebitda_cr": 6.0
}
```

Prompt checker: 33 PASS, 0 FAIL, 1 WARN. The warning is size (87.1 KB versus the company-prompt 30-55 KB heuristic): retained deliberately for whole-sector scope, issuer atlas, full coverage, comparative modelling and unchanged locked quality controls. No unresolved placeholder, citation-density, generic-visual or reference-access warning remains.

Reference hash/count check passed: three original resources, seven reference reports, 239 physical pages and 6,417 regions. These are reference corpus counts, not CDMO source coverage.

Editorial resolutions: stronger source/claim/calculation IDs and KPI-definition checks added; inherited rating bands labelled house convention; S17 earnings-quality verdict distinguished from management and stock verdicts; Luna model-substitution prohibition preserved as explicitly required by the installed skill; generic non-CDMO sector examples replaced. Candidate identity/exposure and complete historical document inventories remain report-execution tasks, not missing prompt text.

This audit verifies the prompt and bounded grounding facts. It does not verify future company valuations, produce a PDF or claim every company filing has been read.
