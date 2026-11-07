# Learnings

What the user had to ask after a report was built. Every new prompt must force each answer up front. In step 4, map every row to the line of the prompt that forces it. Append new corrections at the bottom with the date.

## Standing rules from the user's own words

| User's words (date) | Rule |
|---|---|
| "Great Research analyst... explains the business and it's products flawlessly... acting like a robot" (04-Oct) | Read the documents before writing. Business and every product first, then peers, then numbers. Add material topics without being asked |
| "avoid sections which are not related" (04-Oct), "sections which are irrelavant" (02-Oct) | Sections are chosen for the business. Anything dropped is named with a reason |
| Types, what's new, capacity, utilisation, capex (04-Oct) | Always covered wherever the business has them |
| The 10-point framework, "think bottom-up, question every narrative" (06-Oct) | The 10 rules stay in every prompt, reworded for the company |
| "simple and easy to digest" (06-Oct) | Simple words; terms explained before use |
| "only use one annual report, all the important annoucements only", RHP, regulator databases (23-Oct) | Default document set plus company-specific primary checks; "all documents" switches mode |
| Concall downloader, then Screener if it fails (26-Sep, 23-Oct) | The prompt runs the downloader once, then falls back to Screener |
| The design block (04-Oct, 23-Oct) and visual verification (06-Oct) | Sections 7 and 8 are locked text |
| "why to read this business?" (24-Oct), the semiconductor trigger "was my first goal to find the company" (09-Oct) | Every prompt opens with 0A, why we are covering this business |

## Follow-up questions the prompt must answer up front

| The user asked | The prompt must force |
|---|---|
| "what is the moat for Kabra in battery? anyone can do that" | Moat tested against who else can do it, with a counter-point (S6) |
| "who are the actual customers? is this the only company" | Named customers, what each buys, and all competitors (S5, S6) |
| "Products also be discussed in detail", "types and which types they make", "what are they brining new" | Product grid, product cards, what's-new timeline (S3) |
| "production capacity, utilisation, new capex", "Exisiting capaicty, New Capacity Live, Planned capacity" | Three-way capacity table (S9) |
| "what is take and pay... will it benefit or not" | Every contract term explained, with who benefits (S2) |
| "margins for Merchant vs Onsite" | Margin by business model, assumptions in brackets (S4) |
| "only gives plants, then what about recurring revenue... this model is not good" | One-time vs recurring revenue, and a judgement on model quality (S2) |
| "why did BHEL gave this massive order, what is happening inside BHEL" | Why the big customer is buying, and whether it repeats (S5) |
| "where is the money going in investments" | Where all the cash sits and goes (S10 capital allocation, section 1 balance sheet) |
| "Has shares really pleged by management?" | Pledge checked in primary filings, marked Verified or Not found (S10, section 2) |
| "Why is solar cell trigger not mentioned and management talks about solar cell" | Everything management talks about, in the numbers or not (S10, S13) |
| "what things are assumed and what are actually grounded?", "show the calculation" | Assumed vs grounded list, working shown for every estimate (S20, section 6) |
| "we cannot value this based on it's past earnings" (Suven) | Valuation method follows the business; on the asset when there are no earnings (section 5) |
| "how many actually patients were happy", "lot of jargon" (Suven) | Phase-wise evidence in plain tables, no unexplained terms (S3 biotech version) |
| "Tell about that minear and europe company... what is the relation" (Anlon) | Every named partner: relation, status, what is unverified (S5) |
| "list of approvals... how it matches the management guiding 70%" (Anlon) | Approvals held vs applied for, tested against guidance; exports and order book traced across calls (S3, S12) |
| "Use their website" (Anlon) | Company website product list and brochures as sources (section 2) |
| "use this valuation", management's guidance unchanged (Anlon) | Management guidance table, no haircut, with a Source column (section 5) |
| "key trackables consolidated on one page", "Mention the triggers on the first" | One page of trackables and dated triggers near the start (S1) |
| "scroll is not working", "I want a light mode theme" (Anlon) | Scroll check, light theme default (sections 7, 8) |
| "Still this report does not explain capex properly" (Ellenbarrie) | Project-by-project capex tracker with funding and return on past capex (S9) |
| "What is expected in the next quarter according to the management" (24-Oct), Q1FY27 outlook (Anlon, Amanta) | Current guidance table and next-quarter outlook in management's words (S12) |
| "future derived growth" (Savita), "Semiconductor trigger is currently not there" (Ellenbarrie) | Growth built by driver; full trigger table that says which expected triggers are absent (S13) |
| "this model is not good then" (Ellenbarrie) | The anti-thesis argued with real numbers (S19) |

## Valuation rules (from memory, 29-Sep)

- Base = management guidance exactly, never a more conservative number.
- Bull = the same earnings as base at a higher multiple. Never revenue above guidance.
- Bear = guidance missed and a lower multiple.
- A multiple the user names is used for base.

## New corrections

Append here: date, what the user asked, why the prompt missed it, the line that now forces it.

| Date | User asked | Why it was missed | Line that now forces it |
|---|---|---|---|
| Sat, 07 Nov 2026 | "This skill never asked me but which documents to use" (Supreme Power build) | Step 2 said "never stop for permission" and picked the Default set silently. The guess was that fewer questions is better, but the document choice shapes the whole prompt and belongs to the user. The silent pick also skipped the Q1 FY27 transcript (Aug 2026) | SKILL.md step 2: list what was found, then ask Default / All / Pick / Upload before any worker reads |
| Sat, 07 Nov 2026 | "you didn't use my design format, my design skills mentioned in the research prompt builder at all ... you just gave me a generic sloppy html" (Supreme Power capex one-pager sample) | Section 7 was read only for colours and fonts and treated as a style sheet, so the page came out as a card dashboard. The structure rules were skipped: insight titles, S-numbers, answer line then evidence then "What this means for you" in every section, few cards, sticky contents, management quotes beside the numbers, the three-way capacity table, a capex tracker with return on past capex, and the visual plan's own forms (capacity timeline, type test step diagram). The guess was that "design" meant the look; it means how information is structured | Any HTML sample or report: before writing, list every rule in sections 6A, 7 and 8B plus the learnings rows for that topic, and tick each one in the build |
| Sat, 07 Nov 2026 | "My this intruction has key small decisoins from my learnings and thought process which your skill made from this does not have and you have cleveryly omitted it" | The plan was compressed while building; small decisions with their reasons were treated as optional detail. Gaps found in audit, still to restore: 6A preservation rule wording (method, design, section 8, models, document workflow unchanged); external-skill five rules and the skills list (market-research-reports, cc-equity-research, equity-research-html-studio charts-and-tables.md, initiating-coverage) missing from 6A and wrongly marked not needed; "Plotly, D3 or Python only if asked or the output format changes"; "readable, responsive and printable"; S3 and S9 sector-version depth lines; S10 biotech timeline tracker (Suven); S11 plus S12 feed the valuation guidance row; valuation on the asset when there are no earnings; playbooks missing likely peers per type and peers and charts per sector; concise target 13 to 20 KB (skill says 15 to 25); never edit the Haiku-pinned agent files, stock-screen relies on them; reason Screener is used (downloader returns 0 filings); reasons for codepoint dash check and warn-only citation density; verification tests 4 to 9 | `reference/plan.md` saved word for word as the source of truth and read first; every gap above restored; step 6 runs tests 4 to 8; `scripts/check_skill.py` fails if any plan decision goes missing. Rule: never compress an approved plan while building; a decision with a reason is not optional detail |
| Sat, 07 Nov 2026 | "equity-research-html-studio, ignore this then" | It was a local skill on the user's other machine and does not exist publicly | Dropped from 6A and the external skills table; recorded as a later change in plan.md so the plan text and the skill do not disagree silently |
| Sat, 07 Nov 2026 | "equity-research-html-studio is not there so use this library Dataviz for chart decision making" | dataviz was only an optional reference ("read it if installed"), so nothing made the builder or the research run actually open it | dataviz is now loaded with the Skill tool before the visual plan and before the first chart; its choosing-a-form, marks, interaction and components files drive each chart; anti-patterns.md is the critique step before 8B |
| Sat, 07 Nov 2026 | "why are these points which are fine grained thought process not in the V2 skill plan ?" (user pasted the full plan again) | plan.md was labelled "word for word" but was itself a summary: the requests-to-rules table and the follow-up table were replaced by pointers to this file, the topic-to-form table and the 8B checks by pointers to other files, step 4 flattened into one paragraph, and the reasons behind small decisions dropped ("Your framework, reworded for the company", "The skill never stops for permission", why banks are untested, why Supreme Power and Jeena Sikho were chosen as tests, test 7 timing, the Sonnet cost note, "No existing file gets changed", "Defaults (change any of these when you approve)", the design-system resolution reason). The guess was that pointing to where a decision lives counts as keeping it. It does not: plan.md is where the user checks that their thinking survived, so a pointer reads as an omission | plan.md replaced with the exact pasted text (44.7 KB), with the later changes listed in its header only; check_skill.py fails if plan.md drops under 38 KB or loses any of 17 fine-grained lines. Rule: a file called word for word is copied, never summarised, moved or pointed elsewhere |

| Sat, 07 Nov 2026, DRAFT for review | "refer these instead pasting everthing inside the skill"; "Let me verify it before you finally save the skill" | Links alone would leave the locked neo-brutalist block and boxed dashboard conventions in force. A later research run might also lack the actual references | Proposed reference-design amendment: keep the three original files separately bundled; read them selectively through the guide; stage them beside each company prompt; require a family and physical-page plan in section 7; use the manuals for typography, model-first depth and rendered-page review. Supersede only the conflicting decoration, boxed-note and chart-quota defaults. Preserve the approved plan body and all unrelated research, source, model and valuation decisions. Deliver a review ZIP; do not install before approval |
