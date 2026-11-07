"""Record the learnings replay and the five decisions behind each visual."""
from pathlib import Path
import json

r = Path(__file__).resolve().parent
lines = (r/'prompts/Augmont Enterprises Research Prompt.md').read_text(encoding='utf-8').splitlines()
src = Path('.agents/skills/research-prompt-builder/reference/learnings.md').read_text(encoding='utf-8').splitlines()
rows = [x.split('|') for x in src if x.startswith('|') and not x.startswith('|---')]
anchors = {
    1:'**S2.',2:'### Leave out',3:'**S9.',4:'### The 10 rules',5:'- Simple words.',
    6:'Document mode: All documents for the later',7:'2. Concall transcripts:',8:'## 7.',9:'## 0A.',
    11:'**S6.',12:'**S5.',13:'**S3.',14:'- Capacity table:',15:'- Every contract term explained',
    16:'**S4.',17:'- Revenue model:',18:'**S5.',19:'- Capital allocation:',20:'- Skin in the game:',
    21:'All triggers listed',22:'- Assumed vs grounded:',23:'- Main metric:',24:'- Clinical phases and patient tables:',
    25:'For each named jeweller',26:'**S12.',27:'4. Company website:',28:'- Management guidance row,',
    29:'**S1.',30:'Scroll and print:',31:'- Capex tracker,',32:'- Next quarter:',33:'- Growth build by driver:',
    34:'**S19.',36:'Document mode: All documents for the later',37:'Section opening:',38:'### Coverage map',
    39:'External skills (read if installed',40:'External skills (read if installed',41:'### Coverage map',
    42:'Process: source manifest',43:'Models: all document readers',
}
out = ['# Follow-up replay','',
       'Historical examples transfer as analytical obligations. Process corrections are recorded in prompt-notes.md as well.',
       '', '| Learning row | Prompt line | Requirement forced |', '|---|---|---|']
for i, anchor in anchors.items():
    matches = [(n+1,l) for n,l in enumerate(lines) if anchor in l]
    assert matches, (i,anchor)
    n,l = matches[0]
    label = rows[i][1 if i<35 else 2].strip().replace('|','/')
    out.append(f'| {label[:180]} | {n} | {l[:230].replace("|","/")} |')
assert len(anchors)==41
(r/'follow-up-replay.md').write_text('\n'.join(out)+'\n',encoding='utf-8')

d = json.loads((r/'design-slots.json').read_text(encoding='utf-8'))
comparisons = [
    ('Earlier source mix versus current mix and retained contribution per unit', 'Share is not absolute volume; cycle boundaries are not realised averages'),
    ('Spot principal versus fee-only agency transactions', 'Verify title and cash timing; gross sales are an income-statement item, despite loose call wording'),
    ('Core, consolidated and owner PAT for matched periods', 'Scope differences can explain values; no inferred segment margin'),
    ('Equal funds at alternative cycles and retained spreads', 'Illustrative boundary examples are not management forecasts'),
    ('Existing, operating, identified and aspirational centres; processed throughput versus nameplate', '284 metric tonnes lacks a verified time/metal basis in this call'),
    ('Gross primary versus net proceeds, OFS and deployment', '620/625 conflict is unresolved, not automatically explained by expenses'),
    ('Matched-period PAT versus CFO and cash reinvestment', 'H1 profit cannot be paired with a different cash-flow perimeter'),
    ('Registered versus active/paying consumers; revenue versus retained contribution', '52.3/54 million and 13% share definitions require resolution'),
    ('Announced integration versus live transactions and retained cash earnings', 'Q3 timing is inferred; contribution is unquantified'),
    ('Financial guidance versus independently labelled illustrative assumptions', 'No guided base means no fabricated guided valuation'),
]
v = ['# Visual decision notes','', 'Dataviz unavailable. Use the internal fallback and CC precedents; no external-library compliance claim.','']
for i, line in enumerate(d['VISUAL_PLAN'].splitlines()):
    c = [x.strip() for x in line.strip('|').split('|')]
    comp, caveat = comparisons[i]
    v += [f'## Visual {i+1}',f'1. Information: {c[0]}',f'2. Hypothesis: {c[1]}',
          f'3. Comparison: {comp}',f'4. Form: {c[2]}. Exact observations use tables; mechanisms use flows; changes use bars.',
          f'5. Context/caveat: {caveat}',f'Section/source: {c[3]} / {c[4]}','']
(r/'visual-decision-notes.md').write_text('\n'.join(v),encoding='utf-8')
print('PASS: 41 learnings rows mapped to lines; 10 visual decisions documented.')
