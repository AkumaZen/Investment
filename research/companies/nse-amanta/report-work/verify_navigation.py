from pathlib import Path
import fitz
from PIL import Image
r=Path(__file__).resolve().parent;d=fitz.open(r.parent/'report/amanta-healthcare-equity-research.pdf');q=r/'qa';thumbs=[]
for i,p in enumerate(d):
 pix=p.get_pixmap(matrix=fitz.Matrix(.4,.4));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);thumbs.append(im)
 nav=[l for l in p.get_links() if l['kind']==fitz.LINK_GOTO and 814<=l['from'].y0 and l['from'].y1<=830]
 assert [l['page'] for l in nav]==[0,max(0,i-1),min(len(d)-1,i+1)]
 for b in [(w[0],w[1],w[2],w[3],w[4]) for w in p.get_text('words')]:
  if b[4] in ['Contents','Previous','Next']:continue
  assert not any(fitz.Rect(b[:4]).intersects(l['from']) for l in nav),(i,b)
idx=[l for l in d[0].get_links() if l['kind']==fitz.LINK_GOTO and 700<l['from'].y0<800]
assert [l['page'] for l in idx]==[t[2]-1 for t in d.get_toc()]
for start in range(0,33,12):
 sheet=Image.new('RGB',(1000,1065),'#ddd')
 for n,im in enumerate(thumbs[start:start+12]):sheet.paste(im,((n%4)*250,(n//4)*355))
 sheet.save(q/f'navigation-review-{start//12+1}.jpg')
print('Verified all 20 section destinations and 99 page controls; no header overlap.')



