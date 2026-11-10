"""Check original content, all navigation targets and render the final PDFs."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import fitz
from bs4 import BeautifulSoup
from PIL import Image,ImageDraw

p=argparse.ArgumentParser();p.add_argument('config',type=Path);p.add_argument('--before-html',type=Path,required=True);args=p.parse_args()
cfg=json.loads(args.config.read_text(encoding='utf-8'));base=args.config.resolve().parent
def content(path):
 s=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
 for tag in s.select('.quick-index,.page-navigation,.toc'):tag.decompose()
 for tag in s.find_all('h4',string='Inside this report'):tag.decompose()
 return re.sub(r'\s+',' ', ' '.join(t.get_text(' ',strip=True) for t in s.select('section.page'))).strip()
assert content(args.before_html)==content(base/cfg['html']),'Original report text changed'
s=BeautifulSoup((base/cfg['html']).read_text(encoding='utf-8'),'html.parser');ids={t['id'] for t in s.select('[id]')}
assert len(s.select('.quick-index'))==1 and len(s.select('.page-navigation'))==len(cfg['labels'])
for link in s.select('.quick-index a,.page-navigation a'):assert link['href'][1:] in ids
source=fitz.open(base/cfg['pdf_input']);d=fitz.open(base/cfg['pdf']);assert len(d)==len(source)
section_map=json.loads((base/cfg['section_map']).read_text());assert len(d.get_toc())==len(section_map)
out=base/'qa/navigation';out.mkdir(parents=True,exist_ok=True)
original_links=sum(len(p.get_links()) for p in source);added=len(cfg['labels'])+3*len(d)
assert sum(len(p.get_links()) for p in d)==original_links+added
index_links=[l for l in d[0].get_links() if fitz.Rect(cfg['cover_rect']).contains(l['from'])]
assert [l['page'] for l in index_links]==[r['page']-1 for r in section_map]
thumbs=[]
for i,(old,page) in enumerate(zip(source,d)):
 oldwords=[(tuple(round(v,2) for v in w[:4]),w[4]) for w in old.get_text('words')]
 newwords={(tuple(round(v,2) for v in w[:4]),w[4]) for w in page.get_text('words')}
 assert all(w in newwords for w in oldwords),(i,'Original text moved/lost')
 assert len(old.get_images())==len(page.get_images())
 footer=[l for l in page.get_links() if l['kind']==fitz.LINK_GOTO and 814<=l['from'].y0 and l['from'].y1<=830]
 assert [l['page'] for l in footer]==[0,max(0,i-1),min(len(d)-1,i+1)]
 for link in footer:
  crop=page.get_pixmap(clip=link['from'],matrix=fitz.Matrix(2,2))
  assert sum(v<180 for v in crop.samples)>20,(i,'Invisible navigation label')
 for l in index_links if i==0 else []:assert l['kind']==fitz.LINK_GOTO
 for l in page.get_links():
  if l['kind']==fitz.LINK_GOTO:assert 0<=l['page']<len(d)
 pix=page.get_pixmap(matrix=fitz.Matrix(1.35,1.35));pix.save(out/f'page-{i+1:02d}.png')
 small=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);small.thumbnail((238,337));thumbs.append(small)
 # The additions must leave all prior visual pixels untouched outside reserved rectangles.
 before=old.get_pixmap();after=page.get_pixmap();a=Image.frombytes('RGB',[before.width,before.height],before.samples);b=Image.frombytes('RGB',[after.width,after.height],after.samples)
 for im in (a,b):
  draw=ImageDraw.Draw(im);draw.rectangle((355,812,525,832),fill='white')
  if i==0:
   r=fitz.Rect(cfg['cover_rect']);draw.rectangle((int(r.x0)-2,int(r.y0)-2,int(r.x1)+2,int(r.y1)+2),fill='white')
 assert a.tobytes()==b.tobytes(),(i,'Unexpected rendering change outside navigation')
for start in range(0,len(d),12):
 sheet=Image.new('RGB',(1000,1080),'#ddd')
 for n,im in enumerate(thumbs[start:start+12]):sheet.paste(im,((n%4)*250+6,(n//4)*360+12))
 sheet.save(out/f'sheet-{start//12+1}.jpg')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result={'pdf':str((base/cfg['pdf']).resolve()),'pages':len(d),'sections':len(section_map),'new_navigation_links':added,'total_links':sum(len(p.get_links()) for p in d),'all_destinations_verified':True,'original_html_analytical_text_preserved':True,'original_pdf_text_positions_and_images_preserved':True,'original_visual_pixels_preserved_outside_navigation':True,'rendered_pages':len(d),'manual_review':'pending','outputs':[{'path':str((base/cfg[k]).resolve()),'sha256':sha(base/cfg[k])} for k in ['html','pdf','section_map']]}
(out/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
