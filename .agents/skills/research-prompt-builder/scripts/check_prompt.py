"""Pass/fail quality gate for a research prompt built by research-prompt-builder.

Usage: python check_prompt.py <prompt.md>

Prints PASS, FAIL and WARN lines. Exit code 1 if any FAIL. Stdlib only.
It checks that required topics and locked text are present. It cannot judge
whether the analysis is good; the fund-manager read in SKILL.md step 6 does that.
"""
import os
from pathlib import Path
import re
import sys

from report_references import MANUAL, PDF, SPEC, validate_bundle, validate_plan

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
ORDER = ["0A", "0B", "1", "2", "3", "4", "5", "6", "6A", "7", "8", "8B", "9"]
LOCKED = {"6A": "visual-intelligence.txt", "7": "design-system.txt",
          "8": "visual-check.txt", "8B": "visual-review.txt"}
PARTS_0A = ["What it is", "Why it caught our attention", "Why now", "The core debate",
            "What the market seems to believe",
            "What would make us care, and what would make us drop it",
            "What the reader will be able to decide"]
CORE = ["Why read", "Business", "Revenue model", "Products", "Customers", "Moat", "Capacity",
        "Capex tracker", "Management: who they are", "Management: skin in the game",
        "Management: capital allocation", "Management: delivery record",
        "Management: communication", "Management: fairness to minorities",
        "Management: red flags", "Current guidance", "Next-quarter outlook",
        "Future growth build", "Trigger table", "Peers", "Reality vs optionality",
        "Causal chain", "Cash and earnings quality", "Governance", "Risk cards with signals",
        "Anti-thesis", "Valuation", "Assumed vs grounded"]
# Dashes are checked by codepoint, never by byte grep: a byte-level grep falsely
# flagged 48 lines in the RBA prompt because the rupee sign shares bytes with the dashes.
DASHES = {0x2012: "figure dash", 0x2013: "en dash", 0x2014: "em dash", 0x2015: "horizontal bar"}

results = []


def gate(ok, name, detail=""):
    results.append(("PASS" if ok else "FAIL", name, detail))


def warn(name, detail):
    results.append(("WARN", name, detail))


def read(path):
    with open(path, encoding="utf-8-sig") as f:
        return f.read().replace("\r\n", "\n")


def split_sections(text):
    """Return (header, [(id, body_lines)]) split on '## <id>. ' headings."""
    header, sections, cur = [], [], None
    for line in text.split("\n"):
        m = re.match(r"^## (\d+[A-Z]?)\.\s", line)
        if m:
            cur = (m.group(1), [line])
            sections.append(cur)
        elif cur is None:
            header.append(line)
        else:
            cur[1].append(line)
    return header, sections


def subsection(lines, title):
    out, on = [], False
    for line in lines:
        if line.startswith("### "):
            on = line[4:].strip().lower().startswith(title.lower())
            continue
        if on:
            out.append(line)
    return out


def match_locked(template, lines):
    """Fixed template lines must appear in order; a {{SLOT}} line allows free lines after it."""
    t = [l.rstrip() for l in template.split("\n") if l.strip()]
    p = [l.rstrip() for l in lines if l.strip()]
    i = j = 0
    free = False
    while i < len(t):
        tl = t[i]
        if "{{" in tl:
            prefix = tl.split("{{")[0]
            if j >= len(p) or not p[j].startswith(prefix):
                return "slot line '%s' missing or changed" % tl
            j += 1
            free = True
            i += 1
            continue
        if free:
            while j < len(p) and p[j].strip() != tl.strip():
                j += 1
            if j == len(p):
                return "locked line missing: '%s'" % tl[:90]
            free = False
        elif j >= len(p) or p[j].strip() != tl.strip():
            got = p[j][:90] if j < len(p) else "end of section"
            return "expected '%s' but found '%s'" % (tl[:90], got)
        i += 1
        j += 1
    if j < len(p) and not free:
        return "extra line not in locked text: '%s'" % p[j][:90]
    return None


def table_rows(lines):
    rows = []
    for line in lines:
        s = line.strip()
        if s.startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", s):
            rows.append([c.strip() for c in s.strip("|").split("|")])
    return rows


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    text = read(path)
    header, sections = split_sections(text)
    sec = {sid: body for sid, body in sections}
    ids = [sid for sid, _ in sections]
    concise = bool(re.search(r"^Size:\s*Concise", "\n".join(header), re.M | re.I))

    # Order and presence
    gate(bool(ids) and ids[0] == "0A", "0A is the first section", "first is %s" % (ids[0] if ids else "none"))
    gate(ids == ORDER, "sections 0A to 9 present and in order", "found " + ", ".join(ids))

    # 0A parts
    a = "\n".join(sec.get("0A", []))
    missing = [p for p in PARTS_0A if not re.search(r"^- %s:\s*\S" % re.escape(p), a, re.M)]
    gate(not missing, "0A has all seven parts", "missing: " + "; ".join(missing))

    # 0B rules and questions
    b = sec.get("0B", [])
    rules = [l for l in subsection(b, "The 10 rules") if re.match(r"^\s*\d+[.)]\s+\S", l)]
    gate(len(rules) >= 10, "0B has the 10 rules", "%d found" % len(rules))
    gate(any("The job is NOT to retell" in l for l in b), "0B states the real job ('The job is NOT to retell')")
    qs = [l for l in subsection(b, "The 15 questions") if re.match(r"^\s*\d+[.)]\s+\S", l)]
    with_digit = [q for q in qs if re.search(r"\d", re.sub(r"^\s*\d+[.)]\s+", "", q))]
    need_q, need_d = (10, 8) if concise else (15, 12)
    gate(len(qs) >= need_q, "at least %d questions" % need_q, "%d found" % len(qs))
    gate(len(with_digit) >= need_d, "at least %d questions carry a number" % need_d, "%d found" % len(with_digit))

    # Section 4: coverage map, order, anti-thesis
    s4 = sec.get("4", [])
    cov = {r[0].lower(): r[1] if len(r) > 1 else "" for r in table_rows(subsection(s4, "Coverage map"))}
    bad = []
    for topic in CORE:
        loc = cov.get(topic.lower(), "")
        if not loc:
            bad.append(topic + " (no row)")
        elif loc.lower().startswith("not covered") and not re.search(r"not covered\s*:\s*\S", loc, re.I):
            bad.append(topic + " (not covered, no reason)")
    gate(not bad, "coverage map has every core topic", "; ".join(bad))

    def snum(topic):
        m = re.search(r"S(\d+)", cov.get(topic.lower(), ""))
        return int(m.group(1)) if m else None

    early = [snum("Business"), snum("Products")]
    late = [snum("Peers"), snum("Cash and earnings quality"), snum("Valuation")]
    if None in early or None in late:
        warn("Business and Products before peers and numbers", "could not read section numbers from the coverage map")
    else:
        gate(max(early) < min(late), "Business and Products come before peers, financials and valuation",
             "business/products %s vs peers/financials/valuation %s" % (early, late))
    gate(any("anti-thesis" in l.lower() and not l.strip().startswith("|") for l in s4),
         "anti-thesis section present in the report structure")
    gate(bool(subsection(s4, "Leave out")) and any(l.strip() for l in subsection(s4, "Leave out")),
         "leave-out list present")
    n_s = len([l for l in s4 if re.match(r"^\*\*S\d+", l)])
    if not 9 <= n_s <= 22:
        warn("report section count", "%d S-sections, outside 9 to 22" % n_s)

    # Section 5: valuation
    s5 = sec.get("5", [])
    for case in ("Bear case", "Base case", "Bull case"):
        gate(any(case.lower() in l.lower() and "[E]" in l for l in s5), "%s marked [E]" % case)
    gate(any("bear" in l.lower() and "risk" in l.lower() for l in s5), "bear case linked to the risk cards")
    gate("business-valuation-scenarios" in "\n".join(s5), "section 5 points to the business-valuation-scenarios skill")
    gate(any(r and "source" in " ".join(r).lower() for r in table_rows(s5)[:1]),
         "management guidance table with a Source column")

    # Section 2 and 9
    gate(any(l.startswith("Citation rule:") for l in sec.get("2", [])), "citation rule present")
    gate("not investment advice" in "\n".join(sec.get("9", [])).lower(), "disclaimer present")

    # Locked sections
    for sid, fname in LOCKED.items():
        if sid not in sec:
            gate(False, "section %s matches the locked text" % sid, "section missing")
            continue
        err = match_locked(read(os.path.join(ASSETS, fname)), sec[sid])
        gate(err is None, "section %s matches the locked text" % sid, err or "")

    # The downstream report run must receive accessible files and valid source pages,
    # not just links to a manual that never shapes the prompt.
    s7 = "\n".join(sec.get("7", []))
    directory = re.search(r"^Report-design reference directory: `([^`]+)`\s*$", s7, re.M)
    profile = re.search(r"^Report design family: (BF|MP|CC|EL|SU|AX|MQ)\s*$", s7, re.M)
    gate(bool(directory), "staged reference directory is specified")
    gate(bool(profile), "one valid report-design family is selected")
    if directory:
        try:
            root = Path(directory.group(1))
            if not root.is_absolute():
                raise ValueError("Reference directory must be absolute")
            spec = validate_bundle(root)
            for name in (MANUAL, PDF, SPEC, "guide.md", "report_references.py"):
                if not (root / name).is_file() or "`%s`" % (root / name) not in s7:
                    raise ValueError("Missing accessible reference handoff: " + name)
            gate(True, "three original references and portable reader are accessible and intact")
            plan = s7.split("Report page plan:\n", 1)[1].split("\n\nEach row", 1)[0].strip()
            count = validate_plan(profile.group(1) if profile else "", plan, spec)
            gate(True, "page plan has six complete columns and valid physical source-page IDs", "%d rows" % count)
        except (OSError, ValueError, KeyError, TypeError, IndexError) as error:
            gate(False, "reference handoff and page plan", str(error))

    # Visual plan rows
    vi = sec.get("6A", [])
    rows, seen = [], False
    for line in vi:
        if line.strip().startswith("| Research question"):
            seen = True
            continue
        if seen and line.strip().startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", line.strip()):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    incomplete = [r[0][:40] for r in rows if len(r) != 5 or not all(r)]
    gate(bool(rows), "visual plan has rows", "%d rows" % len(rows))
    gate(not incomplete, "every visual plan row has question, insight, form, section and source",
         "; ".join(incomplete))
    generic = [r[0][:40] for r in rows if len(r) == 5 and (len(r[1].split()) < 6 or not re.search(r"\d|vs|but|than", r[1]))]
    if generic:
        warn("visual plan rows look generic, review by eye", "; ".join(generic))

    # Whole-file checks
    gate("{{" not in text, "no unfilled {{slots}}",
         "; ".join(sorted(set(re.findall(r"\{\{[^}]{0,40}", text)))[:6]))
    dash_lines = []
    for n, line in enumerate(text.split("\n"), 1):
        for ch in line:
            if ord(ch) in DASHES:
                dash_lines.append("line %d (%s)" % (n, DASHES[ord(ch)]))
                break
    gate(not dash_lines, "no em or en dashes", "; ".join(dash_lines[:10]))
    gate(not re.search(r"haiku", text, re.I), "no mention of a smaller worker model")

    # Local files in section 1
    s1 = "\n".join(sec.get("1", []))
    paths = re.findall(r"`((?:[A-Za-z]:[\\/]|/)[^`]+)`", s1)
    absent = [p for p in paths if not os.path.exists(p)]
    gate(not absent, "every local file named in section 1 exists", "; ".join(absent[:5]))
    if not paths:
        warn("section 1 local files", "no local file paths found in section 1")

    # Warnings. Citation density is warn-only because tags often apply to a block,
    # not each line (RBA tags 19 of 57 number lines yet is well cited).
    num_lines = [l for l in sec.get("1", []) if re.search(r"\d", l) and not l.startswith("#") and "`" not in l]
    tagged = [l for l in num_lines if re.search(r"\[[^\]]+\]", l)]
    if num_lines and len(tagged) / len(num_lines) < 0.3:
        warn("citation density in section 1", "%d of %d number lines carry a source tag; check tags apply per block" % (len(tagged), len(num_lines)))
    size = len(text.encode("utf-8")) / 1024
    lo, hi = (15, 25) if concise else (30, 55)
    if not lo <= size <= hi:
        warn("size", "%.1f KB, outside the %s band of %d to %d KB" % (size, "concise" if concise else "full", lo, hi))

    fails = 0
    for status, name, detail in results:
        if status == "FAIL":
            fails += 1
        line = "%s  %s" % (status, name)
        if detail and status != "PASS":
            line += "  :: " + detail
        print(line)
    passes = sum(1 for r in results if r[0] == "PASS")
    warns = sum(1 for r in results if r[0] == "WARN")
    print("\nRESULT: %s  (%d pass, %d fail, %d warn)  %s" % ("FAIL" if fails else "PASS", passes, fails, warns, path))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
