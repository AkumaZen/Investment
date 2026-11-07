import json,pathlib,urllib.request,concurrent.futures,re
B=pathlib.Path(__file__).parent
rows=[
('IPO monitoring agency report September 2026','2026-11-06','https://nsearchives.nseindia.com/corporate/AEL2012_06112026115309_MonitoringAgencyReport.pdf'),
('Statement of deviation September 2026','2026-11-04','https://nsearchives.nseindia.com/corporate/AEL2012_04112026212947_AELtatementofDeviationSeptember2026signed.pdf'),
('Insider trading disclosure Regulation 7(2)','2026-10-01','https://nsearchives.nseindia.com/corporate/AEL2012_01102026171225_AELintimationunderReg7_2_ofSEBIPITSigned.pdf'),
('Audio recording earnings call announcement Q2 FY27','2026-11-05','https://nsearchives.nseindia.com/corporate/AEL2012_05112026201756_AudioRecordingEarningsCall.pdf'),
('Appointment company secretary compliance officer','2026-08-31','https://nsearchives.nseindia.com/corporate/AEL2012_31082026192931_Intimationunderregulation6_1_ofLODRSigned.pdf'),
]
def download(row):
 title,date,url=row;p=B/'docs'/'AUGMONT'/(re.sub('[^a-z0-9]+','-',title.lower()).strip('-')+'.pdf');x=dict(title=title,date=date,url=url,local_path=str(p.resolve()),type='exchange announcement',period='2026')
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0','Referer':'https://www.nseindia.com/'}),timeout=40) as r:d=r.read(40*1024*1024)
  if not d.startswith(b'%PDF'):raise ValueError('not PDF')
  p.write_bytes(d);x.update(status='cached',bytes=len(d))
 except Exception as e:x.update(status='download_failed',error=str(e))
 print(x['status'],title,flush=True);return x
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:out=list(pool.map(download,rows))
j=json.loads((B/'source-inventory.json').read_text());j['documents']+=out
for x in j['documents']:
 t=x['title'].lower();x.setdefault('type','annual report' if 'annual report' in t else 'investor deck' if 'presentation' in t else 'offer document' if any(z in t for z in ['consolidated drhp','limited rhp','limited prospectus']) else 'financial results' if 'outcome of board' in t or 'financial results' in t else 'supporting filing')
 x.setdefault('period',next(iter(re.findall(r'20\d{2}-\d{2,4}',x['title'])),None));x.setdefault('date',None)
j['missing']=['Official Q2 FY27 transcript: company site explicitly lists no data; user upload exists separately','Standalone pledge disclosure or auditor-change announcement not surfaced by inspected post-listing NSE announcements','Some subsidiary/constitutional filings failed; see per-document errors','Any older results/decks/transcripts beyond items on company investor page or current NSE list remain unverified']
(B/'source-inventory.json').write_text(json.dumps(j,indent=2),encoding='utf-8')
