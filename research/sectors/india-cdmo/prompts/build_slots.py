"""Prepare only the seven sector-specific slots for the installed assembler."""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parents[1]
notes = (BASE / 'evidence/design-notes.md').read_text(encoding='utf-8')
plan = '\n'.join(line for line in notes.splitlines() if line.startswith('|'))
plan = re.sub(r'AX-(\d{2})[\u2013-](\d{2})', lambda m: ', '.join(f'AX-{i:02}' for i in range(int(m[1]), int(m[2])+1)), plan)
rows = [
('What work does each supplier sell?', 'Similar CDMO labels may hide different services and more than 1 revenue mechanism', 'Service-stage/modality matrix', 'S2-S3', 'Issuer annual reports, RHP and service disclosures'),
('Who can address each outsourcing opportunity?', 'Installed capability may be broader than qualified commercial customer supply', 'Evidence-coded capability matrix', 'S3, S8', 'Site records, current product/platform disclosures, regulatory and customer evidence'),
('Where does sponsor demand become supplier revenue?', 'Clinical programme growth can be faster than commercial revenue growth because attrition and qualification intervene', 'Sponsor-to-cash causal diagram with stage gates', 'S8, S16', 'Sponsor filings, regulator data and dated supplier programme disclosures'),
('Are global demand and Indian opportunity comparable?', 'Global TAM can be larger than the serviceable Indian opportunity after modality and qualification limits', 'Market-scope reconciliation table and bridge', 'S8', 'Original industry methodology, sponsor and supplier filings'),
('Which demand signals lead actual orders?', 'Commercial launches may support demand more than aggregate early-stage funding alone', 'Dated funding, approvals and supplier-order small multiples', 'S8', 'Regulators, sponsor filings, original funding datasets, supplier results'),
('Does backlog represent committed future revenue?', 'Headline backlog may be larger than executable service commitments when milestones are included', 'Backlog definition and timing comparison table', 'S5, S8', 'Original global and Indian results, contractual definitions and call Q&A'),
('What does a manufacturing site really do?', 'A reactor or filling line provides fewer clues than the full validated manufacturing process', 'Real category/site photos beside editable process flow', 'S3, S9', 'Issuer images, annual reports and process/site disclosures with captions'),
('When does capex become saleable supply?', 'Equipment commissioning can precede qualified commercial revenue by more than 1 reporting period', 'Site/project milestone timelines', 'S9', 'All historical calls/decks, project filings and release milestones'),
('Which peer economics can be compared?', 'Within-cohort comparisons may reveal more than a single blended CDMO league table', 'Cohort tables and separate growth/margin/ROIC charts', 'S14, S17', 'Reconciled audited histories and segment notes'),
('What changed in sales and margins?', 'Acquisitions or FX may explain growth more than organic volume and mix', 'Reported-to-organic revenue bridge and margin bridge', 'S7, S17', 'Results, accounting notes and management explanations'),
('Did management deliver its promises?', 'Commissioning promises may score better than actual revenue and cash delivery', 'Dated promise/outcome matrix with due-promise denominator', 'S11-S12', 'Every available historical transcript/deck and actual filings'),
('Where does profit stop becoming cash?', 'Reported EBITDA can grow faster than FCF when ramp assets absorb capital', 'EBITDA-to-FCF waterfall and working-capital history', 'S17', 'Audited cash flows, balance sheets, capex and lease notes'),
('Which assets earn their required return?', 'A higher margin can coexist with lower than required incremental capital returns', 'Incremental ROIC and capital-turn comparison with sensitivities', 'S9, S17', 'Reconciled invested capital, operating profit, tax and project dates'),
('How does demand translate into forecasts?', 'Qualified programme conversion may explain more than a blanket sector CAGR', 'Yearwise programme/site growth bridge', 'S13', 'Company guidance, disclosed programme stages and qualified output constraints'),
('What can invalidate the opportunity?', 'Correlated sponsor or qualification shocks can affect more than 1 apparently diversified supplier', 'Risk exposure table with triggers and scenario links', 'S19', 'Customer concentration, inspection records, programme disclosures and stress calculations'),
('What is already priced into each stock?', 'A stronger business may offer less upside than a weaker peer at a different price', 'Separate quality and valuation tables, reverse expectations and scenario ranges', 'S20', 'Common-cutoff verified prices, reconciled models and sourced assumptions'),
]
slots = {
 'REPORT_PROFILE': 'AX',
 'REPORT_PAGE_PLAN': plan,
 'ACCENT_MAPPING': 'Use one restrained AX-family magenta accent (measured source #AB2862/#951A4E; choose one for the report), dark ink and neutral fills. Historical, guidance [G] and estimated [E] data differ by labels/patterns as well as colour. Colour distinguishes cohort only when necessary; do not imply that all firms in a cohort have equal quality.',
 'TAG_LIST': 'CDMO; CRDMO; CRO; small molecule; biologics; advanced modality; formulation; mixed group; Disclosed; [G]; [E]; [Inferred]; [Not Disclosed]. Explain each technical term at first use and preserve a compact glossary.',
 'DIAGRAMS': 'Drug-owner-to-CDMO money flow; discovery/development/commercial value chain; modality and service capability matrix; sponsor-to-qualified-order-to-cash chain; site qualification gates; process flows by relevant modality; corporate-action/ownership genealogy. Use editable inline SVG, concise labels and original evidence; pictures never prove undisclosed customer approvals.',
 'MUST_HAVE_CHARTS': 'Comparable five-year and eight-quarter histories by cohort; CDMO versus other segment mix where disclosed; global demand indicators with explicit scope; qualified-capacity/project timeline; revenue and EBITDA bridges; utilisation only when disclosed or clearly labelled proxy; capex and cash conversion; working-capital trends; ROIC/ROCE and asset turns; due promises versus actual delivery; three-year incremental revenue build; Bear/Base/Bull valuation and reverse-expectations comparison for every included issuer. Exact numbers belong in tables when that is clearer. Omit an unsupported exhibit and disclose the evidence gap, never fabricate data.',
 'VISUAL_PLAN': '\n'.join('| ' + ' | '.join(r) + ' |' for r in rows),
}
slots = {k: re.sub('[\u2012-\u2015]', '-', v) for k,v in slots.items()}
(BASE/'prompts/slots.json').write_text(json.dumps(slots, ensure_ascii=False, indent=2), encoding='utf-8')
print('Wrote seven sector design slots')
