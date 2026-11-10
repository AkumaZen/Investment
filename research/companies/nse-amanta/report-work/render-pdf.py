from pathlib import Path
import fitz
from PIL import Image, ImageDraw
base=Path(__file__).resolve().parent
root=base/'qa/pdf';root.mkdir(parents=True,exist_ok=True)
doc=fitz.open(base.parent/'report/amanta-healthcare-equity-research.pdf')
for i,p in enumerate(doc):
 p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(str(root/f'page-{i+1:02}.png'))
for start in range(0,len(doc),4):
 canvas=Image.new('RGB',(2400,880),'#ddd');draw=ImageDraw.Draw(canvas)
 for j in range(4):
  i=start+j
  if i>=len(doc):break
  im=Image.open(root/f'page-{i+1:02}.png');im.thumbnail((590,845));canvas.paste(im,(j*600,25));draw.text((j*600+10,5),f'PDF page {i+1}',fill='black')
 canvas.save(root/f'sheet-{start//4+1}.png')
print('Rendered',len(doc),'pages;',sum(len(p.get_links()) for p in doc),'links')
