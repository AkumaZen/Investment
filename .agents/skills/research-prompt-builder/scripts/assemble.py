"""Assemble a research prompt: paste the locked sections into a filled skeleton.

Usage: python assemble.py <draft.md> <slots.json> <output.md> --references-dir <staged-folder>

The draft is assets/skeleton.txt with every company slot filled and the
{{INCLUDE:6A}}, {{INCLUDE:7}}, {{INCLUDE:8}}, {{INCLUDE:8B}} lines left in place.
slots.json holds ACCENT_MAPPING, TAG_LIST, DIAGRAMS, MUST_HAVE_CHARTS, VISUAL_PLAN,
REPORT_PROFILE and REPORT_PAGE_PLAN. Stage the reference pack first.
Stdlib only.
"""
import argparse
import json
import os
from pathlib import Path
import sys

from report_references import MANUAL, PDF, SPEC, validate_bundle, validate_plan

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
INCLUDES = {
    "6A": "visual-intelligence.txt",
    "7": "design-system.txt",
    "8": "visual-check.txt",
    "8B": "visual-review.txt",
}
SLOT_KEYS = ["ACCENT_MAPPING", "TAG_LIST", "DIAGRAMS", "MUST_HAVE_CHARTS", "VISUAL_PLAN",
             "REPORT_PROFILE", "REPORT_PAGE_PLAN"]


def read(path):
    with open(path, encoding="utf-8-sig") as f:
        return f.read().replace("\r\n", "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft_path")
    parser.add_argument("slots_path")
    parser.add_argument("out_path")
    parser.add_argument("--references-dir", required=True, type=Path)
    args = parser.parse_args()
    draft_path, slots_path, out_path = args.draft_path, args.slots_path, args.out_path
    draft = read(draft_path)
    slots = json.loads(read(slots_path))
    missing = [k for k in SLOT_KEYS if not isinstance(slots.get(k), str) or not slots[k].strip()]
    if missing:
        sys.exit("Missing or empty slots: " + ", ".join(missing))
    root = args.references_dir.expanduser().resolve()
    try:
        spec = validate_bundle(root)
        validate_plan(slots["REPORT_PROFILE"].strip(), slots["REPORT_PAGE_PLAN"].strip(), spec)
        if not (root / "report_references.py").is_file():
            raise ValueError("Portable reference reader is missing; run report_references.py stage first")
    except (OSError, ValueError, KeyError, TypeError) as error:
        sys.exit("Invalid reference handoff: " + str(error))
    slots["REPORT_REFERENCE_DIR"] = "`%s`" % root
    roles = [("Markdown manual", MANUAL), ("Agent specification JSON", SPEC),
             ("PDF manual", PDF), ("Reference guide", "guide.md"),
             ("Portable reference reader", "report_references.py")]
    slots["REPORT_REFERENCE_FILES"] = "\n".join("- %s: `%s`" % (role, root / name) for role, name in roles)
    for key, fname in INCLUDES.items():
        marker = "{{INCLUDE:%s}}" % key
        if marker not in draft:
            sys.exit("Draft has no %s line" % marker)
        text = read(os.path.join(ASSETS, fname)).rstrip("\n")
        for k in [*SLOT_KEYS, "REPORT_REFERENCE_DIR", "REPORT_REFERENCE_FILES"]:
            text = text.replace("{{%s}}" % k, str(slots[k]).strip())
        draft = draft.replace(marker, text)
    if os.path.exists(out_path):
        sys.exit("Refusing to overwrite existing file: " + out_path)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(draft.rstrip("\n") + "\n")
    print("Wrote %s (%d bytes)" % (out_path, len(draft.encode("utf-8"))))


if __name__ == "__main__":
    main()
