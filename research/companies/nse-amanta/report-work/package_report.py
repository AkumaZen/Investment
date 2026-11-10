"""Add PDF bookmarks, preserve original sources, emit reviewable manifests."""
from pathlib import Path
import json,hashlib,re,fitz
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent;OUT=ROOT.parent/'report'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
spec=json.loads((ROOT/'page-specifications.json').read_text(encoding='utf-8'))
pdf=OUT/'amanta-healthcare-equity-research.pdf'
doc=fitz.open(pdf);assert len(doc)==len(spec)
toc=[];seen=set()
for q in spec:
 for start in q.get('section_starts',[dict(section=q['page_id'].split('-')[0],question=q['question'])]):
  s=start['section']
  if s not in seen:toc.append([1,s+' | '+start['question'],q['page']]);seen.add(s)
doc.set_toc(toc)

# Visible navigation complements the sidebar bookmarks without reflowing research.
nav_labels=['Investment view','Business model','Products & photographs','Revenue mix','Distribution','Competitive advantage','Utilisation','SteriPort economics','Capacity & funding','Management','Promises vs delivery','Guidance register','Growth routes','Peer comparison','Earnings vs optionality','Thesis mechanisms','Financial performance','Governance','Risks & downside','Valuation & scenarios']
nav_blue=(0.09,0.24,0.39)
cover=doc[0]
cover.draw_rect(fitz.Rect(31.5,689,564,798),color=None,fill=(0.95,0.96,0.97))
cover.insert_text((41,703),'QUICK NAVIGATION  /  CLICK A SECTION',fontsize=8,fontname='hebo',color=nav_blue)
for i,(_,title,page_number) in enumerate(toc):
 col,row=divmod(i,5);x=41+col*131;y=720+row*15
 cover.insert_text((x,y),f'{i+1:02d}  {nav_labels[i]}',fontsize=7,fontname='helv',color=nav_blue)
 cover.insert_link({'kind':fitz.LINK_GOTO,'from':fitz.Rect(x,y-9,x+128,y+3),'page':page_number-1,'to':fitz.Point(0,0)})
for i,page in enumerate(doc):
 for text,x,target in [('Contents',409,0),('Previous',468,max(0,i-1)),('Next',526,min(len(doc)-1,i+1))]:
  page.insert_text((x,825),text,fontsize=7.5,fontname='helv',color=nav_blue)
  page.insert_link({'kind':fitz.LINK_GOTO,'from':fitz.Rect(x-3,815,x+fitz.get_text_length(text,fontsize=7.5)+3,829),'page':target,'to':fitz.Point(0,0)})
doc.set_metadata({'title':'Amanta Healthcare | Turning capacity into earnings and cash','author':'Investment Research','subject':'Standalone equity research; evidence through 9 November 2026; scenario valuation','keywords':'Amanta Healthcare, AMANTA, equity research, capacity, cash flow, valuation'})
tmp=OUT/'_bookmarked.pdf';doc.save(tmp,garbage=4,deflate=True);doc.close();tmp.replace(pdf)
sources=[];urls=set()
old=json.loads((ROOT/'document-manifest.json').read_text())
annual=json.loads((ROOT/'annual-facts.json').read_text())['sources']
idmap={'outcome-transcript-16-02-2026.pdf':'C3','intimation-under-regulation-30-investor-presentation.pdf':'P3','amanta-outcome-transcript-q4-fy-2025-26.pdf':'C4','amanta-investor-presentation-q4-fy-2025-26.pdf':'P4','amanta-outcome-transcript-q1-fy-2026-27.pdf':'C1','amanta-investor-presentation-fy-2026-27-q1.pdf':'P1','amanta-outcome-transcript-q2-fy-2026-27.pdf':'C2','amanta-investor-presentation-fy-2026-27-q2.pdf':'P2','amanta-annual-report-2025-26.pdf':'AR','amanta-monitoring-agency-report-september-2026.pdf':'MA','amanta-commissioning-of-new-sterilport-line.pdf':'AS','amanta-commissioning-solar-power-plant.pdf':'AP','amanta-intimation-for-change-in-management-30102026.pdf':'COO','amanta-intimation-for-change-in-management-16092026.pdf':'AGM','intimation-for-upgrade-in-credit-rating.pdf':'CR'}
for a in old+annual:
 url=a['url'];name=url.rsplit('/',1)[-1];local=ROOT/'docs'/name
 if url in urls or not local.exists():continue
 urls.add(url)
 sources.append(dict(id=idmap.get(name,name),title=a.get('title',a.get('text',name)),url=url,local_path=str(local.resolve()),pages=len(fitz.open(local)) if local.suffix=='.pdf' else None,bytes=local.stat().st_size,sha256=sha(local),status='retrieved',role='Primary issuer disclosure',accessed='2026-11-10'))
extra=[('R27','Official Q2/H1 FY27 results, board outcome 3 Nov 2026','amanta-q2-fy27-board-outcome.pdf','https://www.amanta.co.in/public/assets/pdf/Investors/exchange-announcements/amanta-outcome-of-board-meeting-held-on-03112026.pdf','Primary issuer disclosure'),('DR','Denis Chem Lab CRISIL rationale, 27 Oct 2025','denis-rating-2025.pdf','https://bsmedia.business-standard.com/_media/bs/data/announcements/bse/28102025/a0a240b8-582b-4575-b1ec-055a70638207.pdf','Primary rating rationale hosted in exchange-announcement mirror'),('GF','Gufic official manufacturing capabilities','gufic-manufacturing.html','https://gufic.com/manufacturing/navsari-facility','Primary corporate website')]
for sid,title,name,url,role in extra:
 local=ROOT/'docs'/name
 sources.append(dict(id=sid,title=title,url=url,local_path=str(local.resolve()),pages=len(fitz.open(local)) if local.suffix=='.pdf' else None,bytes=local.stat().st_size,sha256=sha(local),status='retrieved',role=role,accessed='2026-11-10'))
snapshots=[('NSE','Official NSE EQ bhavcopy, 9 Nov 2026','nse-bhavcopy.csv','https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_09112026.csv','Official dated price: CLOSE_PRICE 202.15; LAST_PRICE 202.50 is different'),('SC','Screener standalone Amanta snapshot','screener-standalone.json','https://www.screener.in/company/AMANTA/','Secondary historical quarters, ownership and ratios; audited statement controls differences'),('GS','Screener standalone Gufic snapshot','peer-0.json','https://www.screener.in/company/GUFICBIO/','Secondary peer financials, dated 10 Nov retrieval'),('DS','Screener standalone Denis snapshot','peer-denis.json','https://www.screener.in/company/537536/','Secondary peer financials, dated 10 Nov retrieval')]
for sid,title,name,url,role in snapshots:
 local=ROOT/name
 sources.append(dict(id=sid,title=title,url=url,local_path=str(local.resolve()),pages=None,bytes=local.stat().st_size,sha256=sha(local),status='retrieved',role=role,accessed='2026-11-10'))
assets=ROOT/'product-assets'
used=['pro-img-slide-1.png','pro-img-slide-2.png','respiratory-P1.jpg','ophthalmics-P5.jpg','ophthalmics-P4.jpg','diluents-P1.jpg']
for a in json.loads((assets/'manifest.json').read_text()):
 if a['file'] not in used:continue
 local=assets/a['file']
 sources.append(dict(id='IMG-'+a['file'],title='Official Amanta product photograph: '+a['file'],url=a['url'],local_path=str(local.resolve()),pages=None,bytes=local.stat().st_size,sha256=sha(local),status='retrieved',role='Issuer product photograph; representative current pack, not proof of future line or market approval',accessed='2026-11-10'))
for name in ['fluid-therapy','respiratory','ophthalmics','diluents']:
 local=assets/(name+'.html')
 sources.append(dict(id='CAT-'+name,title='Amanta official '+name+' catalogue',url='https://www.amanta.co.in/'+name,local_path=str(local.resolve()),pages=None,bytes=local.stat().st_size,sha256=sha(local),status='retrieved',role='Primary corporate product catalogue; photographs accessed for visual revision, research cutoff unchanged',accessed='2026-11-10'))
limitations=[
 'Company archive and Screener document feed yielded four historical call transcripts and four matching investor presentations. No older publicly listed call was located; completeness is limited to discoverable archive coverage.',
 'The original BSE annual-report download and live NSE quote API returned access errors; official company-hosted annual report and official NSE archived bhavcopy were recovered. Failure logs retained in report-work/document-manifest.json.',
 'Screener consolidated data were empty; standalone statements are appropriate because the annual report discloses no subsidiaries, associates or JVs.',
 'The direct 6 Nov promoter purchase disclosure was not retrieved. Its secondary feed summary is explicitly qualified in the governance section and is not evidence of price-paid conviction.',
 'MD remuneration archive item was identified; annual report p42 and official AGM disclosure supply the report evidence. That separate remuneration PDF is not part of the downloaded corpus.',
 'Actual line-specific sold volume, net realization, product margins, binding orders and audited solar project profit are not disclosed in this source set. Missing facts are not filled with invented figures.',
 'Management revenue language on Q2 call p10 mixes annualised and full-year wording, alongside FY28 range on p14. No single clean FY27 promise is imputed.',
 'Valuation includes analyst assumptions for incrementality, margins, financing, depreciation, taxes, WC, capex, restricted-fund use and multiples. It is not a fully balanced three-statement forecast or licensed investment advice.'
]
manifest=dict(company='Amanta Healthcare Limited',exchange='NSE: AMANTA; BSE:544502',isin='INE084K01015',market='India',currency='INR',analysis_date='2026-11-10',evidence_cutoff='2026-11-09',price_date='2026-11-09',closing_price=202.15,shares=38829351,source_locator_convention='Physical PDF pages. Annual report often displays two printed pages per physical page.',saved_prompt=dict(path=str((ROOT.parent/'prompts/Amanta Healthcare Research Prompt.md').resolve()),sha256=sha(ROOT.parent/'prompts/Amanta Healthcare Research Prompt.md'),scope='Original preserved. Latest user request expands original call-only scope.'),sources=sources,report_page_sources=[dict(page=x['page'],section=x['page_id'],title=x['question'],references=x['source_refs']) for x in spec],limitations=limitations,outputs=[dict(path=str(p.resolve()),sha256=sha(p),bytes=p.stat().st_size) for p in [pdf,OUT/'report.html',OUT/'valuation-model.json']])
(OUT/'source-manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
md=['# Amanta Healthcare source manifest','', 'Prepared 10 November 2026; evidence through 9 November. INR; standalone. Source locators in the report are physical PDF pages.','', '| ID | Original source | Local evidence / SHA-256 |','|---|---|---|']
for s in sources:md.append(f'| {s["id"]} | [{s["title"]}]({s["url"]}) | [{Path(s["local_path"]).name}](<{s["local_path"]}>) · {s["pages"] or "non-PDF"} pages · `{s["sha256"]}` |')
md+=['','## Coverage and limits','']+['- '+x for x in limitations]+['','The JSON companion records per-report-page source groups, output hashes and the preserved prompt hash. Hashes establish file identity, not the truth of every issuer statement.']
(OUT/'source-manifest.md').write_text('\n'.join(md),encoding='utf-8')
print('Packaged',len(sources),'sources,',len(spec),'report pages;',len(toc),'PDF bookmarks')

