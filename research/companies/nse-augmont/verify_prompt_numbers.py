"""Recompute derived figures used in the research prompt, not company forecasts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKS = [
    ('Core PAT multiple', 85 / 34, 2.50, 2, 'Call p.7; INR crore / INR crore'),
    ('Core PAT growth percent', (85 / 34 - 1) * 100, 150.0, 1, 'Call p.7'),
    ('Core EBITDA multiple', 113 / 50, 2.26, 2, 'Call p.7'),
    ('Core EBITDA growth percent', (113 / 50 - 1) * 100, 126.0, 1, 'Call p.7'),
    ('Scrap procurement share change, percentage points', 24.5 - 3, 21.5, 1, 'Call p.14; percentage points, not percent'),
    ('Scrap procurement share multiple', 24.5 / 3, 8.17, 2, 'Call p.14; not absolute volume growth'),
    ('Gold4All endpoint revenue multiple', 6600 / 1100, 6.00, 2, 'Call p.5; conflicts with stated 5.7x'),
    ('Fresh issue description difference, INR crore', 625 - 620, 5, 0, 'Call pp.7,12; no assumed explanation'),
    ('Illustrative four-day versus two-day capital turns ratio', (1 / 4) / (1 / 2), 0.5, 2, '[E] equal capital/time; boundary examples, not realised cycles'),
    ('Illustrative contribution hurdle multiple', (1 / 2) / (1 / 4), 2, 2, '[E] same costs/funds/operating days; not guidance'),
]
rows = []
for name, actual, expected, places, source in CHECKS:
    ok = round(actual, places) == expected
    rows.append({'claim': name, 'calculated': actual, 'rounded_expected': expected,
                 'source': source, 'result': 'PASS' if ok else 'FAIL'})
assert all(row['result'] == 'PASS' for row in rows)
(ROOT/'number-checks.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')
print(f'PASS: {len(rows)}/{len(rows)} derived-number checks. No valuation forecast or current market price invented.')
