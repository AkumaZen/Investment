---
name: research-prompt-builder
description: Write a finished company research PROMPT (not the research itself) for an Indian listed company. Reads the company's documents and any uploads, works out what matters in that business, and saves a tailored prompt to Desktop\Investment\Research Prompts\. Use when the user asks for a research prompt, a prompt to research a company, or to "prepare the prompt" for a company deep dive. Do NOT use when the user asks for the research, report or analysis itself.
---

# Research prompt builder

For this repository in Codex, read [CODEX.md](CODEX.md) before using the workflow below. It defines the local paths and records runtime requirements without replacing the research rules.

You write the prompt that a later research run will follow. You stop at the prompt. Building the report is a separate step the user starts.

A good prompt reads like it was written by a senior analyst who has already read the filings: it knows what this business sells, where the debate is, which numbers conflict and what is still missing. A prompt that only swaps the company name into a template is a failure.

## Paths

| What | Where |
|---|---|
| Skill folder | `~/.claude/skills/research-prompt-builder/` (called `SKILL_DIR` below) |
| Prompts | `C:\Users\RNEGI\Desktop\Investment\Research Prompts\<Company> Research Prompt.md` |
| Company research folder | `C:\Users\RNEGI\Desktop\Investment\<Company>\research\` |
| Cached documents | `...\<Company>\research\docs\<TICKER>\` |
| Fact pack | `...\<Company>\research\facts.md` |
| Scratch notes | `...\<Company>\research\prompt-notes.md` |

Never overwrite an existing prompt. If `<Company> Research Prompt.md` exists, save as `<Company> Research Prompt V2.md` (then V3, and so on) and leave the old file untouched.

## Read before starting

- `reference/plan.md`: the user's approved plan, word for word. It is the source of truth. Every decision in it, however small, must be followed; if this file disagrees with it, the plan wins unless `learnings.md` records the user changing it.
- `reference/learnings.md`: the questions the user had to ask after past reports. Every prompt must force these answers up front.
- `reference/playbooks.md`: business model, story, sector, situations and optional modules. Used in step 4.
- `reference/analysis-guide.md`: how each core analysis is done well. Used in step 5.
- `reference/visual-intelligence.md`: how to write the visual plan. Used in step 4.
- `reference/report-design/guide.md`: how to consult the three separately bundled design references. Read this router, then only the relevant manual chapters and JSON page records. The PDF is the reading/review copy. Do not paste the manuals or full JSON into the skill or generated prompt.
- `reference/workers.md`: the worker briefs for step 3.
- `reference/examples.md`: which saved prompt to read for which case.
- The valuation metric table lives in the `business-valuation-scenarios` skill, Step 1. Read it there; do not copy it.

## Workflow

### Step 1: Resolve the company

1. Find the company and ticker with `mcp__screener__search_company`. Ask the user only if the name matches more than one listed company.
2. Look for an existing prompt, `facts.md` and cached documents for this company, and reuse them.
3. If the user gave their own reason for looking at the company, record it word for word in `prompt-notes.md`. It becomes "Why it caught our attention" in 0A.
4. Note any user instruction that changes the default: document mode, size, a section list, a valuation multiple, a trigger they expect. User instructions beat the skeleton and the playbooks.

### Step 2: Collect the documents

Sources, in this order:
1. User uploads (`@file`, a folder path or pasted text). Copy them into `research\docs\<TICKER>\uploads\` and cite them as user uploads.
2. Files already cached in `research\docs\<TICKER>\`.
3. `mcp__screener__get_document_list` (the skill uses Screener, not the concall downloader, because the downloader currently returns 0 filings; the generated prompt still keeps the run-once-then-fallback line), then `python SKILL_DIR/scripts/fetch_doc.py <url> <out_dir>`. Also the company website for product pages, brochures and decks.

| Mode | When | Documents |
|---|---|---|
| Default | The user says nothing about scope | The latest annual report; the latest deck and transcript, plus any older call a guidance quote depends on; the latest results; the RHP if listed in the last 3 years; important announcements only; every upload |
| All documents | The user says "all documents", "use everything" or similar | Every annual report, deck, transcript and results filing on Screener and in the cache, plus important announcements, plus every upload |

- Uploads are always added to the fetched set, never used instead of it, unless the user says to use only the uploads.
- Important announcements stay filtered in both modes: orders, capex, fund raises, acquisitions, rating actions, auditor or KMP changes, litigation, pledge disclosures. Skip trading-window closures, newspaper advertisements, compliance certificates and similar.
- In all-documents mode the newest document wins when numbers conflict, and the conflict is recorded.
- Write the mode into the prompt's section 2, so the research run uses the same set.
- Keep a found vs missing list in `prompt-notes.md`. Every missing item goes into the prompt's "To find" list.
- Always ask which documents to use before any worker reads anything, unless the user already said in this request. Run `get_document_list` and check the cache first, then ask one question (AskUserQuestion) that lists what was found by type and period (annual reports, transcripts, decks, results, RHP) and offers: Default set (recommended, name the exact files), All documents, Pick specific ones, or "I'll upload my own" (uploads are added to the fetched set). Record the answer word for word in `prompt-notes.md`.
- After that one question, never stop for permission. Ask again only if the ticker is ambiguous or no documents can be found at all.

### Step 3: Extract (Sonnet workers read, you do not)

- Spawn one worker per document with the `doc-reader` brief in `reference/workers.md`, and one `financials-scanner` worker for the Screener numbers. Use the Agent tool with `subagent_type: "general-purpose"` and `model: "sonnet"` on every call. Run them in parallel.
- Each worker writes its own `facts-<doc>.md`; you merge them into `facts.md`. Charts, tables and scanned pages are read from page images made by `python SKILL_DIR/scripts/pdf_pages.py <pdf> --render --pages 12-15 --out <dir>`.
- If a Sonnet worker cannot be started, stop and tell the user. Never fall back to a smaller model.
- Never edit the agent files in `.claude/agents/` (doc-reader, financials-scanner, evidence-verifier). Other skills such as stock-screen rely on their pinned model. Pass `model: "sonnet"` on each call instead, which overrides the pin for that call only.
- Do not read whole documents yourself. Read `facts.md`, and open a specific page only to settle a conflict or check a key number.

### Step 4: Diagnose (you, before drafting)

Write these to `prompt-notes.md` first. This is the core of the skill.
1. Why this business matters, and the core debate in one question.
2. How one unit of this business earns money. Explain it as you would to a first-time investor, and list every product, format or service line. If you cannot, read more of `facts.md` or send a worker back.
3. Who runs it, what they own, what they did with raised money, and whether they delivered.
4. What management guides now, what capex is under way, and which triggers would drive growth. Note anything management talks about that is not yet in the numbers, and any trigger the user expects that the documents do not support.
5. The strongest case against the stock, written before the bull case hardens.
6. Business model, story and sector from `playbooks.md`, plus any special situation, and the structure that follows.
7. The "separate X from Y" rule that fits, and the causal chain with its first unproven link.
8. 15 company-specific questions, each with a real number or name.
9. One connecting-the-dots example with real numbers.
10. Data conflicts between documents.
11. The valuation metric from the `business-valuation-scenarios` Step 1 table, with the reason.
12. Sections to keep, rename, swap, add and drop, each with a reason.
13. Load the `dataviz` skill (Skill tool) first: it is the chart decision library. Pick each visual plan form with its `choosing-a-form.md` and check the plan against its `anti-patterns.md`. Then read each external skill besides dataviz listed in `reference/visual-intelligence.md` that is installed, with its five rules. Never stop if one is missing.
    The visual plan: the five questions in `reference/visual-intelligence.md` answered for each key visual, based on this company's economics and the data that actually exists.
14. Every row of `reference/learnings.md`: which line of the prompt will force that answer for this company.
15. Report design: follow `reference/report-design/guide.md`. Verify the supplied files with `python SKILL_DIR/scripts/report_references.py check`. Select one family (BF, MP, CC, EL, SU, AX or MQ) for the economics and scope. Read the applicable manual chapters and selected physical source pages; use JSON measurements selectively, never all 6,417 rectangles. Log the chapters/pages actually read and the reason for the family. Build a company-specific page plan linking decision questions to evidence/calculations, source page IDs, exhibit forms and justified adaptations. Preserve the existing core coverage and valuation rules.
16. Stage the pack for the later research run: `python SKILL_DIR/scripts/report_references.py stage --dest "<absolute company research folder>/references/report-design"`. This copies the three references, guide, manifest and portable reader. Keep them distinct from company factual sources. Recover missing/unreadable files before releasing a prompt that claims reference compliance. The historical neo-brutalist style is superseded only as recorded in the 7 November 2026 reference-design amendment in `reference/learnings.md`.

### Step 5: Write

1. Copy `assets/skeleton.txt` to a draft and fill every `{{SLOT}}` for this company. Text after the colon in a slot is an instruction, not text to keep.
2. Leave the `{{INCLUDE:6A}}`, `{{INCLUDE:7}}`, `{{INCLUDE:8}}` and `{{INCLUDE:8B}}` lines as they are.
3. Write a slots file (JSON) with seven keys: `ACCENT_MAPPING`, `TAG_LIST`, `DIAGRAMS`, `MUST_HAVE_CHARTS`, `VISUAL_PLAN`, `REPORT_PROFILE`, `REPORT_PAGE_PLAN`. `VISUAL_PLAN` is markdown table rows only, five cells each. `REPORT_PROFILE` is one family ID. `REPORT_PAGE_PLAN` is the six-column table specified in `reference/report-design/guide.md`, including its header and explicit physical source IDs such as BF-06. No full reference content is inlined.
4. Assemble: `python SKILL_DIR/scripts/assemble.py <draft> <slots.json> "<final prompt path>" --references-dir "<staged reference folder>"`. This pastes the current locked sections 6A, 7, 8 and 8B in word for word and inserts verified absolute paths to the staged references. The later report agent reads those files; copying links without a page plan is not sufficient.
5. Section 1 holds cited facts, conflicts and the "To find" list. Every local path in section 1 is absolute, in backticks, and exists.
6. Section 5: bear, base and bull are each marked `[E]`; base equals management guidance exactly; bull has the same earnings as base at a higher multiple; bear is built from the S19 risk cards; a management guidance table with a Source column sits alongside.

Override rules:
- Locked, never overridden: section order 0A, 0B, 1 to 6, 6A, 7, 8, 8B, 9; 0A first; the 10 rules; the 15 questions; the citation rule; sections 6A, 7, 8 and 8B; Business and Products before peers and numbers; management, capex, guidance, growth triggers and the anti-thesis always covered; valuation and verdict last.
- Rename: S3 can become Pipeline, Formats and menu, or Service lines. S9 and S11 have sector versions.
- Swap: replace a default section when it does not fit, such as phase tables and cash runway in place of capacity for a pre-revenue biotech, or a statements register in place of claims checked for an annual-report-only company.
- Add: extra deep dives when material, such as a control change or an overseas subsidiary.
- Drop: only if it truly does not apply, named with its reason in the leave-out list.
- Concise mode (the user says "concise" or "short"): merge sections rather than delete analysis (S7 into S4, S16 into S15, S18 into S17), keep sections 0A to 9, and keep Business, Products, Management, capex, guidance, growth triggers and the anti-thesis. Target 13 to 20 KB (the checker warns only outside 15 to 25 KB).

Core topics. Each is a row in the coverage map with the exact name below, and a section number or "Not covered: reason":
Why read; Business; Revenue model; Products; Customers; Moat; Capacity; Capex tracker; Management: who they are; Management: skin in the game; Management: capital allocation; Management: delivery record; Management: communication; Management: fairness to minorities; Management: red flags; Current guidance; Next-quarter outlook; Future growth build; Trigger table; Peers; Reality vs optionality; Causal chain; Cash and earnings quality; Governance; Risk cards with signals; Anti-thesis; Valuation; Assumed vs grounded.

### Step 6: Check

1. `python SKILL_DIR/scripts/check_prompt.py "<final prompt path>"`. Fix every FAIL and re-run until it passes. Read every WARN and fix it unless there is a reason not to.
2. Recompute every derived number in the prompt (growth rates, margins, multiples, per-share values) by script, and fix any difference.
3. Read the prompt as a sceptical fund manager: what obvious question about this company is unanswered? Fix it and re-run the checker.
4. Follow-up replay: for every row of `reference/learnings.md`, name the prompt line that forces the answer. A row with no line is a FAIL.
5. Accuracy: an `evidence-verifier` worker (model "sonnet") re-reads 10 random numbers from the prompt against their source pages.
6. Adaptation: compare with the closest earlier prompt; 0A, structure, the 15 questions, rules, capex, triggers, anti-thesis, valuation metric and visual plan must truly differ, not only the names.
7. Model check: confirm every worker ran on Sonnet 5.5 and quote it.
8. Preservation: after ANY change to this skill (not per prompt), run `python SKILL_DIR/scripts/check_skill.py`. It must PASS, so no decision from `reference/plan.md` is ever dropped.
9. Reference handoff: confirm the three original resources match their manifest, every selected physical source page exists, the prompt carries accessible local paths and one declared family, and the page plan fits this company. Confirm the later report instructions require the manual's model-first process, page storyboard, rendered-page inspection and reader decision test. The checker verifies structure and access; it cannot prove that the agent read the files or produced good analysis.

### Step 7: Deliver

Reply with:
- The file path.
- Why this business, in two lines.
- How the structure was tailored: business model, story, sector, and sections added, renamed, swapped or dropped.
- What is specific to this company: the core debate, the "separate X from Y" rule, the first unproven link.
- The checker result and every WARN.
- Gaps: documents missing and what the research run must find.
- The chosen report family, key source-page precedents and any reference-access gaps.

Paste the full prompt only if the user asks.

## Rules

- Simple words. Explain a term before using it.
- No em dashes or en dashes in anything you write.
- Workers run on Sonnet 5.5 only. The prompt never names any other worker model.
- Facts in the prompt come from documents and carry source tags. Your own estimates are marked `[E]` with the working.
- When the user corrects a prompt, append the lesson to `reference/learnings.md`: what they asked, why the prompt missed it, and the line that will force it next time.
