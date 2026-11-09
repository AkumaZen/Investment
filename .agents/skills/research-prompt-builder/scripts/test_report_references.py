"""Offline regression tests for the new reference handoff, not company research.

Usage: python scripts/test_report_references.py
Uses a labelled synthetic fixture and temporary files. Python stdlib only.
"""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

from check_prompt import CORE
from report_references import MANUAL, PDF, SPEC, bundle_root, validate_bundle

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"


class ReferenceHandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="report reference test ")
        # resolve() expands Windows 8.3 short names (ROHITN~1), matching the resolved paths assemble.py writes
        self.work = Path(self.temp.name).resolve()
        self.addCleanup(self.temp.cleanup)

    def run_script(self, script, *args, success=True):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
        result = subprocess.run([sys.executable, "-B", str(script), *map(str, args)],
                                capture_output=True, text=True, encoding="utf-8", env=env)
        if success:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def stage(self):
        dest = self.work / "company research" / "references" / "report-design"
        self.run_script(SCRIPTS / "report_references.py", "stage", "--dest", dest)
        return dest

    def fixture(self):
        draft = self.work / "draft.md"
        slots = self.work / "slots.json"
        output = self.work / "TEST_ONLY_prompt.md"
        facts = self.work / "TEST_ONLY_facts.md"
        facts.write_text("Synthetic plumbing test. No investment facts or analysis.\n", encoding="utf-8")
        mapped = {"Why read": 1, "Business": 2, "Revenue model": 2, "Products": 3,
                  "Customers": 5, "Moat": 6, "Capacity": 9, "Capex tracker": 9,
                  "Current guidance": 11, "Next-quarter outlook": 12,
                  "Future growth build": 13, "Trigger table": 13, "Peers": 14,
                  "Reality vs optionality": 15, "Causal chain": 16,
                  "Cash and earnings quality": 17, "Governance": 18,
                  "Risk cards with signals": 19, "Anti-thesis": 19,
                  "Valuation": 20, "Assumed vs grounded": 20}
        values = {
            "COMPANY": "TEST ONLY, synthetic handoff fixture",
            "SIZE": "Concise", "RESEARCH_TYPE": "Initiating coverage deep dive",
            "DOC_MODE": "Default", "VERSION": "TEST", "BUILD_DATE": "7 Nov 2026",
            "LOCAL_FILES": "- Synthetic source: `%s`" % facts,
            "FRAME": "The job is NOT to retell a report. This is a synthetic handoff test, not company research.",
            "QUESTIONS": "\n".join("%d. TEST ONLY: what source verifies driver %d before a decision?" % (i, i)
                                    for i in range(1, 16)),
            "COVERAGE_MAP": "\n".join("| %s | S%d |" % (topic, mapped.get(topic, 10)) for topic in CORE),
            "RESEARCH_FOLDER": str(self.work),
        }
        def fill(match):
            raw = match.group(1)
            if raw.startswith("INCLUDE:"):
                return match.group(0)
            key = raw.split(":", 1)[0].strip()
            return values.get(key, "TEST ONLY: evidence to be supplied; no company fact asserted")
        skeleton = (ROOT / "assets" / "skeleton.txt").read_text(encoding="utf-8-sig")
        draft.write_text(re.sub(r"\{\{([^}]+)\}\}", fill, skeleton), encoding="utf-8")
        table = ("| Destination section | Decision question | Source page IDs | Evidence and calculations | Form | Adaptation or omission |\n"
                 "|---|---|---|---|---|---|\n"
                 "| S9 test | Is the handoff inspectable? | BF-06, CC-16 | Synthetic evidence task, not investment data | Table | Keep BF typography; test explicit physical IDs |")
        data = {"ACCENT_MAPPING": "BF navy/coral, subject emphasis only",
                "TAG_LIST": "[TEST ONLY]", "DIAGRAMS": "None required by the synthetic scope",
                "MUST_HAVE_CHARTS": "None required by the synthetic scope",
                "VISUAL_PLAN": "| Can a reader inspect a source? | Test whether 2 explicit pages resolve from the local pack | Table | S9 | Synthetic fixture |",
                "REPORT_PROFILE": "BF", "REPORT_PAGE_PLAN": table}
        slots.write_text(json.dumps(data), encoding="utf-8")
        return draft, slots, output, data

    def test_original_resources_and_corpus(self):
        spec = validate_bundle(bundle_root())
        self.assertEqual(len(spec["reports"]), 7)
        self.assertEqual(sum(r["page_count"] for r in spec["reports"]), 239)

    def test_selective_json_and_region_opt_in(self):
        reader = SCRIPTS / "report_references.py"
        out = self.run_script(reader, "pages", "BF-06", "CC-16")
        data = json.loads(out.stdout)
        self.assertEqual(set(data), {"BF-06", "CC-16"})
        self.assertNotIn("text_regions", data["BF-06"]["measured"])
        self.assertEqual(data["BF-06"]["physical_pdf_page"], 6)
        self.assertEqual(data["BF-06"]["printed_page"], 5)
        out = self.run_script(reader, "pages", "BF-06", "--regions")
        self.assertTrue(json.loads(out.stdout)["BF-06"]["measured"]["text_regions"])
        self.run_script(reader, "pages", "BF-99", success=False)

    def test_selective_manual_and_no_full_audit_dump(self):
        reader = SCRIPTS / "report_references.py"
        out = self.run_script(reader, "manual", "--pages", "BF-06", "CC-16")
        self.assertEqual(len(re.findall(r"^#### ", out.stdout, re.M)), 2)
        self.assertNotIn("#### BF-07", out.stdout)
        out = self.run_script(reader, "manual", "--pages", "BF-37")
        self.assertNotIn("### MP.", out.stdout)
        self.run_script(reader, "manual", "--sections", "12", success=False)

    def test_standalone_staging_and_no_overwrite(self):
        dest = self.stage()
        for name in (MANUAL, PDF, SPEC):
            self.assertEqual((dest / name).read_bytes(), (bundle_root() / name).read_bytes())
        self.run_script(dest / "report_references.py", "check")
        self.run_script(SCRIPTS / "report_references.py", "stage", "--dest", dest)
        (dest / "guide.md").write_text("User-modified guide", encoding="utf-8")
        self.run_script(SCRIPTS / "report_references.py", "stage", "--dest", dest, success=False)
        self.assertEqual((dest / "guide.md").read_text(), "User-modified guide")

    def test_assembly_and_existing_prompt_checks(self):
        dest = self.stage()
        draft, slots, output, _ = self.fixture()
        self.run_script(SCRIPTS / "assemble.py", draft, slots, output, "--references-dir", dest)
        text = output.read_text(encoding="utf-8")
        for name in (MANUAL, PDF, SPEC, "guide.md", "report_references.py"):
            self.assertIn(str(dest / name), text)
        self.assertNotIn("{{", text)
        self.assertNotIn('"bbox_pt"', text)
        self.assertNotIn("hard offset shadow", text)
        result = self.run_script(SCRIPTS / "check_prompt.py", output)
        self.assertIn("RESULT: PASS", result.stdout)
        self.run_script(SCRIPTS / "assemble.py", draft, slots, output, "--references-dir", dest, success=False)
        output.write_text(text.replace("BF-06, CC-16", "BF-99, CC-16"), encoding="utf-8")
        result = self.run_script(SCRIPTS / "check_prompt.py", output, success=False)
        self.assertIn("Unknown physical source page IDs", result.stdout)

    def test_missing_slot_and_invalid_page_are_blocked(self):
        dest = self.stage()
        draft, slots, output, data = self.fixture()
        data.pop("REPORT_PROFILE")
        slots.write_text(json.dumps(data), encoding="utf-8")
        self.run_script(SCRIPTS / "assemble.py", draft, slots, output, "--references-dir", dest, success=False)
        data["REPORT_PROFILE"] = "BF"
        data["REPORT_PAGE_PLAN"] = data["REPORT_PAGE_PLAN"].replace("BF-06", "BF-99")
        slots.write_text(json.dumps(data), encoding="utf-8")
        self.run_script(SCRIPTS / "assemble.py", draft, slots, output, "--references-dir", dest, success=False)
        self.assertFalse(output.exists())

    def test_missing_and_tampered_resources_are_blocked(self):
        dest = self.stage()
        draft, slots, output, _ = self.fixture()
        pdf = dest / PDF
        original = pdf.read_bytes()
        pdf.unlink()
        self.run_script(SCRIPTS / "assemble.py", draft, slots, output, "--references-dir", dest, success=False)
        pdf.write_bytes(original + b"tampered")
        result = self.run_script(dest / "report_references.py", "check", success=False)
        self.assertIn("integrity mismatch", result.stderr)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
