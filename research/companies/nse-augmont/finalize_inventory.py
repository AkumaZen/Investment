import pathlib,json,hashlib,collections
import fitz
B=pathlib.Path(__file__).parent;j=json.loads((B/'source-inventory.json').read_text());groups=collections.defaultdict(list)
for x in j['documents']:
 p=pathlib.Path(x['local_path'])
 if x['status']!='cached' or not p.exists():continue
 data=p.read_bytes();h=hashlib.sha256(data).hexdigest();x['sha256']=h;groups[h].append(x['title'])
 try:
  doc=fitz.open(p);x['pages']=len(doc);x['pages_with_extractable_text']=sum(bool(page.get_text().strip()) for page in doc);x['text_coverage_note']='Mechanical text availability count only; document not substantively read by inventory agent'
 except Exception as e:x['pdf_inspection_error']=str(e)
 x['priority']='core' if x['type'] in ['annual report','investor deck','offer document','financial results'] or any(z in x['title'].lower() for z in ['monitoring agency report september','statement of deviation','fire incident','insider trading disclosure','financials 2025-26']) else 'support archive'
j['duplicate_groups']=[v for v in groups.values() if len(v)>1]
upload=B/'docs/AUGMONT/uploads/Augmont_Enterprises_Ltd_Nov_2026_Transcript.pdf'
if upload.exists():
 doc=fitz.open(upload);j['user_uploads']=[dict(title='Q2 FY27 earnings call transcript supplied by user',type='transcript',period='Q2 FY27',date='2026-11-05',url=None,local_path=str(upload.resolve()),status='cached user upload',pages=len(doc),sha256=hashlib.sha256(upload.read_bytes()).hexdigest(),pages_with_extractable_text=sum(bool(p.get_text().strip()) for p in doc))]
(B/'source-inventory.json').write_text(json.dumps(j,indent=2),encoding='utf-8')
cached=sum(x['status']=='cached' for x in j['documents']);failed=[x for x in j['documents'] if x['status']!='cached']
lines=['# Augmont filing discovery as of 7 November 2026','',f'Cached {cached} public PDF records; {len(failed)} links failed PDF validation/download. Duplicate hashes identify copies, so record count is not unique-document count. User transcript is additional.','', 'Concall downloader not installed among available tools; unavailable and not invoked. Screener get_document_list invoked once for AUGMONT: no annual reports or official transcripts. Fallback: public company investor page and its application module, then NSE announcements (120 days, 24 returned). No whole document was substantively read during discovery. PDF page/text counts are mechanical metadata.','', 'Primary discovery: https://augmont.com/investors/stakeholders . Actual click-handler URLs recovered from https://augmont.com/chunk-APZDGZBM.js . Exact source URLs, local paths, hash, page count, text coverage and failure reasons are in source-inventory.json.','', '## Core sources','', '| Document | Period | Pages | Text pages | File |','|---|---|---:|---:|---|']
for x in j['documents']:
 if x.get('priority')=='core':lines.append(f"| {x['title']} | {x.get('period') or 'See filing'} | {x.get('pages','?')} | {x.get('pages_with_extractable_text','?')} | {pathlib.Path(x['local_path']).name} |")
lines+=['','## Missing and limits','']+['- '+v for v in j['missing']]+['','## Failed links','']+['- '+x['title']+': '+x.get('error','') for x in failed]+['','## Duplicate groups','']+['- '+'; '.join(v) for v in j['duplicate_groups']]
(B/'filing-discovery.md').write_text('\n'.join(lines)+'\n',encoding='utf-8');print(cached,'cached',len(failed),'failed',len(j['duplicate_groups']),'duplicate groups')
