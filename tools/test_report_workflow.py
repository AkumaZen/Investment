"""Behavior checks for extract invalidation and fail-fast build execution."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

import fitz

spec = importlib.util.spec_from_file_location('workflow', Path(__file__).with_name('report-workflow.py'))
workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)


class WorkflowChecks(unittest.TestCase):
    def test_cached_extracts_deduplicate_and_invalidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pdf, cache = root / 'first.pdf', root / 'cache'
            with fitz.open() as doc:
                doc.new_page().insert_text((30, 30), 'Original evidence')
                doc.new_page().insert_text((30, 30), 'Second physical page')
                doc.save(pdf)
            def call(path):
                capture = io.StringIO()
                with contextlib.redirect_stdout(capture):
                    workflow.extract(path, cache)
                return json.loads(capture.getvalue())
            first = call(pdf)
            self.assertFalse(first['cache_hit'])
            text = Path(first['text'])
            self.assertIn('=== PHYSICAL PAGE 2 ===', text.read_text())
            duplicate = root / 'different-url.pdf'
            duplicate.write_bytes(pdf.read_bytes())
            self.assertTrue(call(duplicate)['cache_hit'])
            text.write_text('corrupted extraction')
            self.assertFalse(call(pdf)['cache_hit'])
            self.assertIn('Original evidence', text.read_text())
            with fitz.open() as doc:
                doc.new_page().insert_text((30, 30), 'Corrected filing')
                doc.save(pdf)
            changed = call(pdf)
            self.assertFalse(changed['cache_hit'])
            self.assertNotEqual(first['text'], changed['text'])

    def test_build_stops_on_failure_and_checks_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = root / 'build.json'
            stages = [
                {'name': 'first', 'argv': [sys.executable, '-c', "from pathlib import Path; Path('first.txt').write_text('ok')"]},
                {'name': 'fail', 'argv': [sys.executable, '-c', 'raise SystemExit(7)']},
                {'name': 'must-not-run', 'argv': [sys.executable, '-c', "from pathlib import Path; Path('third.txt').touch()"]},
            ]
            def write(config):
                manifest.write_text(json.dumps(config))
            write({'stages': stages, 'outputs': ['first.txt']})
            self.assertEqual(workflow.run(manifest, True), 0)
            self.assertFalse((root / 'first.txt').exists())
            self.assertEqual(workflow.run(manifest, False), 7)
            self.assertFalse((root / 'third.txt').exists())
            log = json.loads((root / 'qa/build-run.json').read_text())
            self.assertEqual(log['status'], 'failed')
            self.assertEqual(len(log['stages']), 2)
            write({'stages': stages[:1], 'outputs': ['missing.txt']})
            self.assertEqual(workflow.run(manifest, False), 1)
            write({'stages': stages[:1], 'outputs': ['first.txt']})
            self.assertEqual(workflow.run(manifest, False), 0)
            log = json.loads((root / 'qa/build-run.json').read_text())
            self.assertEqual(log['outputs'][0]['sha256'], workflow.sha(root / 'first.txt'))
            self.assertIsNone(log['token_usage'])


if __name__ == '__main__':
    unittest.main()
