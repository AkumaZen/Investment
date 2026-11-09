"""Preservation gate: confirms every decision from reference/plan.md is still in the built skill.

Usage: python check_skill.py
Run after ANY change to this skill. Exit code 1 if a decision is missing. Stdlib only.
Each entry: (file, phrase that must appear, the plan decision it protects).
Matching ignores case and collapses whitespace.
"""
import hashlib
import os
import re
import sys

from report_references import validate_bundle

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

REQUIRED = [
    # SKILL.md workflow
    ("SKILL.md", "reference/plan.md", "plan is the source of truth"),
    ("SKILL.md", "Never overwrite an existing prompt", "V2 instead of overwrite"),
    ("SKILL.md", "word for word in `prompt-notes.md`", "user's own reason feeds 0A"),
    ("SKILL.md", "User instructions beat the skeleton and the playbooks", "your instructions win"),
    ("SKILL.md", "never used instead of it, unless the user says to use only the uploads", "uploads combine with fetched docs"),
    ("SKILL.md", "Important announcements stay filtered in both modes", "announcement filter"),
    ("SKILL.md", "newest document wins when numbers conflict", "newest wins"),
    ("SKILL.md", "Write the mode into the prompt's section 2", "mode written into prompt"),
    ("SKILL.md", "found vs missing list", "found vs missing feeds To find"),
    ("SKILL.md", "Always ask which documents to use", "later user change: ask documents first"),
    ("SKILL.md", "downloader currently returns 0 filings", "reason Screener is used"),
    ("SKILL.md", "model: \"gpt-6.1-sol\"", "GPT-6.1 Sol workers"),
    ("SKILL.md", "Never substitute another worker model without user approval", "no Haiku fallback"),
    ("SKILL.md", "Never edit the agent files", "agent files stay unchanged"),
    ("SKILL.md", "stock-screen", "stock-screen relies on pinned agents"),
    ("SKILL.md", "Do not read whole documents yourself", "Opus does not read in bulk"),
    ("SKILL.md", "written before the bull case hardens", "anti-thesis before bull"),
    ("SKILL.md", "do not copy it", "valuation table: one source of truth"),
    ("SKILL.md", "read each external skill", "external skills read before building"),
    ("SKILL.md", "Target 13 to 20 KB", "concise target"),
    ("SKILL.md", "S7 into S4, S16 into S15", "concise merges"),
    ("SKILL.md", "Locked, never overridden", "override rules"),
    ("SKILL.md", "sceptical fund manager", "fund-manager read"),
    ("SKILL.md", "Follow-up replay", "test 4"),
    ("SKILL.md", "evidence-verifier", "test 5"),
    ("SKILL.md", "Adaptation", "test 6"),
    ("SKILL.md", "Model check", "test 7"),
    ("SKILL.md", "check_skill.py", "test 9 preservation"),
    ("SKILL.md", "Paste the full prompt only if the user asks", "delivery default"),
    ("SKILL.md", "append the lesson to `reference/learnings.md`", "corrections go to learnings"),
    # Skeleton
    ("assets/skeleton.txt", "The job is NOT to retell", "0B real job"),
    ("assets/skeleton.txt", "at least half the report", "Part A half"),
    ("assets/skeleton.txt", "What this means for you", "section opening"),
    ("assets/skeleton.txt", "Sector versions keep the same depth", "S3 sector versions"),
    ("assets/skeleton.txt", "R&D centre and trial spend", "S9 sector versions"),
    ("assets/skeleton.txt", "a biotech gets a timeline tracker", "S10 Suven timeline tracker"),
    ("assets/skeleton.txt", "Together they feed the management guidance row", "S11 plus S12 feed valuation"),
    ("assets/skeleton.txt", "value the asset", "valuation on the asset with no earnings"),
    ("assets/skeleton.txt", "never a more conservative number of our own", "base = guidance"),
    ("assets/skeleton.txt", "guidance realised faster or better", "bull = guidance beaten from disclosed triggers (10 Nov 2026 change)"),
    ("assets/skeleton.txt", "business-valuation-scenarios", "section 5 points to the valuation skill"),
    ("assets/skeleton.txt", "built from the S19 risk cards", "bear from risks"),
    ("assets/skeleton.txt", "Do not retry the downloader", "downloader once"),
    ("assets/skeleton.txt", "Broker numbers stay out", "no broker numbers"),
    ("assets/skeleton.txt", "STRONG only if it appears in 2 or more primary filings", "trigger strength"),
    ("assets/skeleton.txt", "If an expected trigger is absent, say so", "absent triggers"),
    ("assets/skeleton.txt", "A RED caps the rating", "RED caps rating"),
    ("assets/skeleton.txt", "Coverage map", "coverage map"),
    ("assets/skeleton.txt", "Leave out", "leave-out list"),
    ("assets/skeleton.txt", "re-check 10 random numbers", "10-number re-check"),
    ("assets/skeleton.txt", "Written from the documents in plain words, in under 15 lines", "0A length and source"),
    ("assets/skeleton.txt", "such as debtor days above 150", "risk card threshold example"),
    # 6A
    ("assets/visual-intelligence.txt", "does not change the research method, the design system, the section 8 checks, the model assignments or the document workflow", "6A preservation rule"),
    ("assets/visual-intelligence.txt", "readable, responsive and printable", "readable responsive printable"),
    ("assets/visual-intelligence.txt", "only if the user asks or the output format changes", "Plotly/D3 rule"),
    ("assets/visual-intelligence.txt", "historical thick-border card style is superseded", "user-requested reference-design amendment replaces old card rule"),
    ("assets/visual-intelligence.txt", "market-research-reports", "external skill K-Dense"),
    ("assets/visual-intelligence.txt", "cc-equity-research", "external skill CC"),
    ("assets/visual-intelligence.txt", "the chart decision library", "dataviz drives chart decisions in the prompt"),
    ("assets/visual-intelligence.txt", "anti-patterns.md", "dataviz critique step"),
    ("SKILL.md", "Load the `dataviz` skill", "builder loads dataviz before the visual plan"),
    ("reference/plan.md", "ignore `equity-research-html-studio`", "user dropped html studio, recorded as a later change"),
    ("assets/visual-intelligence.txt", "initiating-coverage", "local skill initiating coverage"),
    ("assets/visual-intelligence.txt", "remains the single source of truth", "external skill rule 4"),
    ("assets/visual-intelligence.txt", "never depends on an external skill", "external skill rule 5"),
    ("assets/visual-intelligence.txt", "Expected insight (to be confirmed by data)", "visual plan columns"),
    # Locked 7, 8, 8B
    ("assets/design-system.txt", "Chart.js 4.4.1", "pinned Chart.js"),
    ("assets/design-system.txt", "light by default", "light theme"),
    ("assets/visual-check.txt", "Scroll:", "scroll check"),
    ("assets/visual-review.txt", "Does every visual improve understanding", "8B 12 checks"),
    ("assets/visual-review.txt", "As a report designer", "two-role review"),
    # References
    ("reference/playbooks.md", "likely peers", "peers per business type"),
    ("reference/playbooks.md", "untested", "banks marked untested"),
    ("reference/playbooks.md", "peers and charts", "peers and charts per sector"),
    ("reference/visual-intelligence.md", "Where this meets the locked design system", "design system resolution"),
    ("reference/visual-intelligence.md", "Conflicts (ignored, rule 4)", "external skills: adds, overlaps, conflicts noted"),
    ("reference/learnings.md", "Valuation rules", "valuation memory rules"),
    # plan.md must stay the user's exact text, never a summary (lines below were lost once when it was compressed)
    ("reference/plan.md", "Your framework, reworded for the company:", "10 rules reworded per company"),
    ("reference/plan.md", "| \"Great Research analyst... explains the business and it's products flawlessly... acting like a robot\" (04-Oct) |", "requests-to-rules table kept in plan"),
    ("reference/plan.md", "| \"this model is not good then\" (Ellenbarrie) | The anti-thesis, argued with real numbers |", "follow-up table kept in plan"),
    ("reference/plan.md", "| Valuation | Bear, base and bull comparison | S20 |", "topic to form table kept in plan"),
    ("reference/plan.md", "- Does every visual improve understanding rather than add length?", "8B 12 checks kept in plan"),
    ("reference/plan.md", "The skill never stops for permission.", "original step 2 wording kept, later change noted in header"),
    ("reference/plan.md", "If not, read more.", "diagnose: read more if it cannot be explained"),
    ("reference/plan.md", "marked untested because no prompt of yours covers them yet", "reason banks are untested"),
    ("reference/plan.md", "because they predate those", "test 1 reason"),
    ("reference/plan.md", "has a folder, no prompt yet, and is a manufacturer with a capex story", "test 2 reason for Supreme Power"),
    ("reference/plan.md", "is a services business, not a factory, so it tests whether the skill really adapts", "test 3 reason for Jeena Sikho"),
    ("reference/plan.md", "During tests 2 and 3, I confirm from the run transcripts", "test 7 timing"),
    ("reference/plan.md", "which cost more than Haiku, and they will take some run time", "cost note"),
    ("reference/plan.md", "No existing file gets changed.", "no existing file changed"),
    ("reference/plan.md", "Defaults (change any of these when you approve)", "defaults heading"),
    ("reference/plan.md", "Your block says section 7 stays locked and existing technology stays unless you ask for a change", "design system resolution reason"),
    ("reference/plan.md", "install all the skills this skill needs", "request that came with the plan"),
    # Checker
    ("scripts/check_prompt.py", "codepoint", "dash check by codepoint, with reason"),
    ("scripts/check_prompt.py", "warn-only", "citation density warn-only, with reason"),
    ("scripts/check_prompt.py", "haiku", "no smaller model in prompt"),
    ("SKILL.md", "reference/report-design/guide.md", "separate references, not pasted content"),
    ("SKILL.md", "REPORT_PAGE_PLAN", "page-plan handoff reaches prompt assembly"),
    ("SKILL.md", "report_references.py stage", "later run gets portable local references"),
    ("assets/design-system.txt", "{{REPORT_REFERENCE_FILES}}", "three reference paths are assembled"),
    ("assets/design-system.txt", "Report design family:", "one coherent report family"),
    ("assets/design-system.txt", "unboxed note", "reference typography supersedes dashboard boxes"),
    ("assets/design-system.txt", "No shadows, thick card borders", "old decorative defaults replaced"),
    ("assets/design-system.txt", "page-specification schema", "page-by-page process"),
    ("assets/visual-check.txt", "Unrun checks are NOT RUN, never PASS", "honest validation status"),
    ("reference/report-design/guide.md", "physical PDF page number", "no cover-offset ambiguity"),
    ("reference/report-design/guide.md", "None supplies factual evidence for the new company", "design corpus does not supply company facts"),
    ("reference/learnings.md", "reference-design amendment", "narrow supersession is documented"),
    ("reference/plan.md", "reference-design amendment", "historical style conflict is explicit"),
]

FILES = ["SKILL.md", "assets/skeleton.txt", "assets/visual-intelligence.txt", "assets/design-system.txt",
         "assets/visual-check.txt", "assets/visual-review.txt", "reference/plan.md", "reference/learnings.md",
         "reference/playbooks.md", "reference/analysis-guide.md", "reference/visual-intelligence.md",
         "reference/examples.md", "reference/workers.md", "scripts/check_prompt.py", "scripts/assemble.py",
         "reference/report-design/guide.md", "scripts/report_references.py", "reference/report-design/manifest.json"]


def norm(s):
    return re.sub(r"\s+", " ", s).lower()


def main():
    fails = 0
    cache = {}
    for f in FILES:
        p = os.path.join(ROOT, f)
        if not os.path.exists(p):
            print("FAIL  file missing: %s" % f)
            fails += 1
        else:
            with open(p, encoding="utf-8-sig") as fh:
                cache[f] = norm(fh.read())
    # Size floor: the exact plan is about 38 KB. A compressed copy (35.9 KB once) fails here.
    plan_path = os.path.join(ROOT, "reference/plan.md")
    if os.path.exists(plan_path) and os.path.getsize(plan_path) < 38000:
        print("FAIL  reference/plan.md is %d bytes, under 38000: it has been compressed, restore the user's exact text" % os.path.getsize(plan_path))
        fails += 1
    for f, phrase, why in REQUIRED:
        if f in cache and norm(phrase) in cache[f]:
            continue
        print("FAIL  %s :: missing '%s' (%s)" % (f, phrase, why))
        fails += 1
    # Exact-body guard supplements the original phrase and size checks. Only the
    # header's recorded user amendments may differ from the supplied approved plan.
    original_body_hash = "bc411c171ce1a708853ad0d1ef568a0a27baa13eb1c602c25afd8f6d951324f5"
    try:
        with open(plan_path, "rb") as fh:
            body = fh.read().split(b"\n---\n", 1)[1]
        if hashlib.sha256(body).hexdigest() != original_body_hash:
            raise ValueError("approved plan body changed")
    except (OSError, ValueError, IndexError) as error:
        print("FAIL  reference/plan.md :: " + str(error))
        fails += 1
    try:
        validate_bundle(os.path.join(ROOT, "reference", "report-design"))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print("FAIL  report-design resource pack :: " + str(error))
        fails += 1
    total = len(REQUIRED) + len(FILES) + 2
    print("\nRESULT: %s  (%d of %d decisions present)" % ("FAIL" if fails else "PASS", total - fails, total))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
