import re,json,pathlib,urllib.request,urllib.parse,concurrent.futures
BASE=pathlib.Path(__file__).parent
s=(BASE/'augmont-investor.js').read_text(encoding='utf-8')
a=re.findall(r'title:"([^"]+)"[^{}]{0,250}?link:"([^"]+)"',s)
items=[]
for title,u in a:
 if not u.lower().endswith('.pdf'): continue
 url='https://augmont.com'+u if u.startswith('/') else u
 if any(x['url']==url for x in items): continue
 items.append({'title':title,'url':url})
(BASE/'discovered-links.json').write_text(json.dumps(items,indent=2),encoding='utf-8')
def fetch(x):
 name=re.sub('[^a-z0-9]+','-',x['title'].lower()).strip('-')+'.pdf'
 dest=BASE/'docs'/'AUGMONT'/name
 x['local_path']=str(dest.resolve());x['status']='found'
 try:
  if not dest.exists():
   url=urllib.parse.quote(x['url'],safe=':/%?=&')
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r: data=r.read(60*1024*1024)
   if not data.startswith(b'%PDF'): raise ValueError('not PDF')
   dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
  x['bytes']=dest.stat().st_size;x['status']='cached'
 except Exception as e:x['status']='download_failed';x['error']=str(e)
 print(x['status'],x['title'],flush=True)
 return x
priority=lambda x:0 if any(k in x['title'].lower() for k in ['q2','2025-26','consolidated drhp','prospectus','red herring']) else 1
selected=[x for x in items if not any(k in x['url'].lower() for k in ['downloadable','policies','governance'])]
selected.sort(key=priority)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(fetch,selected))
(BASE/'source-inventory.json').write_text(json.dumps({'as_of':'2026-11-07','discovery_source':'https://augmont.com/investors/stakeholders','concall_downloader':'not installed among available tools; not invoked','screener_get_document_list':'invoked once AUGMONT; no annual reports or transcripts found','documents':results},indent=2),encoding='utf-8')
