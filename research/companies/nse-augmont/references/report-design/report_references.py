"""Select, verify and stage report-design references. Python stdlib only.

Run with --help. The staged copy works directly from its reference folder.
Full-corpus JSON and the full manual audit are never printed by default.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

MANUAL = "Equity_Research_Design_Page_by_Page_Manual.md"
PDF = "Equity_Research_Design_Page_by_Page_Manual.pdf"
SPEC = "Equity_Research_Design_Agent_Specification.json"
RESOURCE_NAMES = (MANUAL, PDF, SPEC)


def bundle_root():
    here = Path(__file__).resolve().parent
    installed = here.parent / "reference" / "report-design"
    return installed if (installed / "manifest.json").is_file() else here


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def validate_bundle(root):
    root = Path(root)
    manifest = read_json(root / "manifest.json")
    records = manifest.get("files", [])
    if {r["filename"] for r in records} != set(RESOURCE_NAMES) or len(records) != 3:
        raise ValueError("Reference manifest must identify the three supplied files")
    for record in records:
        path = root / record["filename"]
        data = path.read_bytes()
        if len(data) != record["bytes"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
            raise ValueError("Reference integrity mismatch: " + path.name)
    spec = read_json(root / SPEC)
    reports = spec["reports"]
    pages = [p for r in reports for p in r["pages"]]
    regions = sum(len(p["measured"].get("text_regions", [])) for p in pages)
    counts = (len(reports), len(pages), regions)
    expected = tuple(manifest[k] for k in ("expected_reports", "expected_pages", "expected_text_regions"))
    if counts != expected:
        raise ValueError("Reference corpus counts differ: %r, expected %r" % (counts, expected))
    for report in reports:
        physical = [p["physical_pdf_page"] for p in report["pages"]]
        if physical != list(range(1, report["page_count"] + 1)):
            raise ValueError("Invalid physical page sequence in " + report["id"])
    if not (root / "guide.md").is_file():
        raise ValueError("Reference guide is missing")
    return spec


def page_records(spec):
    return {"%s-%02d" % (r["id"], p["physical_pdf_page"]): p
            for r in spec["reports"] for p in r["pages"]}


def select_pages(spec, ids):
    records = page_records(spec)
    bad = [page_id for page_id in ids if page_id not in records]
    if bad:
        raise ValueError("Unknown physical source page IDs: " + ", ".join(bad))
    return {page_id: records[page_id] for page_id in dict.fromkeys(ids)}


def validate_plan(profile, table, spec):
    if profile not in {r["id"] for r in spec["reports"]}:
        raise ValueError("REPORT_PROFILE must be one of BF, MP, CC, EL, SU, AX, MQ")
    lines = [line.strip() for line in table.splitlines() if line.strip()]
    if not lines or any(not line.startswith("|") or not line.endswith("|") for line in lines):
        raise ValueError("REPORT_PAGE_PLAN must be a six-column Markdown table")
    rows = [[cell.strip() for cell in line.strip("|").split("|")]
            for line in lines if not re.fullmatch(r"[| :\-]+", line)]
    expected = ["Destination section", "Decision question", "Source page IDs",
                "Evidence and calculations", "Form", "Adaptation or omission"]
    if not rows or rows[0] != expected or len(rows) < 2:
        raise ValueError("REPORT_PAGE_PLAN needs the documented header and at least one company-specific row")
    if len(rows) > 61:
        raise ValueError("Keep the page plan selective; at most 60 rows")
    for row in rows[1:]:
        if len(row) != 6 or not all(row):
            raise ValueError("Every page-plan row must have six nonempty cells")
        ids = re.findall(r"\b(?:BF|MP|CC|EL|SU|AX|MQ)-\d{2}\b", row[2])
        if not ids:
            raise ValueError("Each page-plan row needs explicit physical source page IDs")
        residue = re.sub(r"\b(?:BF|MP|CC|EL|SU|AX|MQ)-\d{2}\b", "", row[2])
        if residue.strip(" ,;` "):
            raise ValueError("Use explicit source IDs separated by commas or semicolons, not ranges")
        select_pages(spec, ids)
    return len(rows) - 1


def stage(root, dest):
    validate_bundle(root)
    dest = Path(dest).expanduser()
    if not dest.is_absolute():
        raise ValueError("Stage destination must be an absolute path")
    pairs = [(Path(root) / name, dest / name)
             for name in (*RESOURCE_NAMES, "guide.md", "manifest.json")]
    pairs.append((Path(__file__).resolve(), dest / "report_references.py"))
    for source, target in pairs:
        if target.exists() and (not target.is_file() or source.read_bytes() != target.read_bytes()):
            raise ValueError("Refusing to overwrite a different existing reference: " + str(target))
    dest.mkdir(parents=True, exist_ok=True)
    for source, target in pairs:
        if source.resolve() != target.resolve() and not target.exists():
            shutil.copyfile(source, target)
    print(str(dest.resolve()))


def manual_extract(root, sections, ids, spec):
    text = (Path(root) / MANUAL).read_text(encoding="utf-8-sig")
    if sections:
        chunks = re.split(r"(?m)(?=^## \d+\. )", text)
        found = {}
        for chunk in chunks:
            match = re.match(r"## (\d+)\. ", chunk)
            if match:
                found[int(match.group(1))] = chunk.rstrip()
        if 12 in sections:
            raise ValueError("Select audit entries with manual --pages, not the whole section 12")
        if any(n not in found for n in sections):
            raise ValueError("Unknown manual section")
        return "\n\n".join(found[n] for n in dict.fromkeys(sections))
    select_pages(spec, ids)
    entries = re.split(r"(?m)(?=^#### [A-Z]{2}-\d{2}\. )", text)
    found = {}
    for entry in entries:
        match = re.match(r"#### ([A-Z]{2}-\d{2})\. ", entry)
        if match:
            found[match.group(1)] = re.split(r"(?m)^### [A-Z]{2}\. ", entry)[0].rstrip()
    return "\n\n".join(found[page_id] for page_id in dict.fromkeys(ids))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="Reference folder; defaults to bundled or staged folder")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="Verify resource hashes and corpus counts")
    index = sub.add_parser("index", help="List families/tokens, or one report's page roles")
    index.add_argument("--report")
    pages = sub.add_parser("pages", help="Read selected JSON page records")
    pages.add_argument("ids", nargs="+")
    pages.add_argument("--regions", action="store_true", help="Include selected pages' text-region coordinates")
    manual = sub.add_parser("manual", help="Read front chapters or selected audit entries")
    group = manual.add_mutually_exclusive_group(required=True)
    group.add_argument("--sections", nargs="+", type=int)
    group.add_argument("--pages", nargs="+")
    staging = sub.add_parser("stage", help="Copy references and reader beside company research")
    staging.add_argument("--dest", required=True, type=Path)
    args = parser.parse_args()
    root = args.root or bundle_root()
    spec = validate_bundle(root)
    if args.command == "check":
        print("PASS: three original resources; 7 reports; 239 physical pages; 6,417 text regions")
    elif args.command == "stage":
        stage(root, args.dest)
    elif args.command == "manual":
        print(manual_extract(root, args.sections, args.pages, spec))
    elif args.command == "index":
        if args.report:
            matches = [r for r in spec["reports"] if r["id"] == args.report]
            if not matches:
                raise ValueError("Unknown report ID: " + args.report)
            report = matches[0]
            print(report["id"] + ": " + report["title"])
            for page in report["pages"]:
                print("%s-%02d | printed %s | %s" % (report["id"], page["physical_pdf_page"],
                      page["printed_page"], page["role"]))
        else:
            print(json.dumps({"reports": [{k: r[k] for k in ("id", "title", "page_count", "source_url")}
                                          for r in spec["reports"]],
                              "recommended_tokens": spec["recommended_tokens"]}, indent=2, ensure_ascii=False))
    else:
        result = select_pages(spec, args.ids)
        if not args.regions:
            result = {key: {**{k: v for k, v in page.items() if k != "measured"},
                       "measured": {k: v for k, v in page["measured"].items() if k != "text_regions"},
                       "text_region_count": len(page["measured"].get("text_regions", []))}
                      for key, page in result.items()}
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        main()
    except (OSError, ValueError, KeyError, TypeError) as error:
        sys.exit("FAIL: " + str(error))
