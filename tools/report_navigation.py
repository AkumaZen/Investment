"""Visible HTML section index and PDF navigation, preserving report content."""
import argparse
import html as html_lib
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup
import fitz


def add_html_navigation(html, labels):
    html = re.sub(r'<!--quick-navigation-start-->.*?<!--quick-navigation-end-->', '', html, flags=re.S)
    # Augmont's original contents list is replaced by the same destinations, now clickable.
    html = re.sub(r'<h4>Inside this report</h4>\s*<ol class="toc">.*?</ol>', '', html, flags=re.S)
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.select('section.page')
    assert len(pages) == len(labels)
    ids = [p['id'] for p in pages]
    index = '<div class="quick-index" id="quick-navigation"><p>QUICK NAVIGATION / CLICK A SECTION</p><div>'
    index += ''.join(f'<a href="#{sid}">{i+1:02d} &nbsp;{html_lib.escape(label)}</a>' for i,(sid,label) in enumerate(zip(ids,labels)))
    index += '</div></div>'
    css = '''<style>
.quick-index{background:#f2f4f6;padding:12px 14px;margin:16px 0;color:#14213d}
.quick-index p{margin:0 0 9px;font-size:12px;font-weight:700;letter-spacing:.03em}
.quick-index>div{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:7px 14px}
.quick-index a{font-size:12px;line-height:1.35;text-decoration:none;color:#244b6a}
.page-navigation{display:flex;justify-content:flex-end;gap:22px;margin:8px 26px 10px;font-size:12px}
.page-navigation a{color:#244b6a;text-decoration:underline;text-underline-offset:2px}
@media screen and (max-width:600px){.quick-index>div{grid-template-columns:repeat(2,minmax(0,1fr))}.page-navigation{margin:10px 16px;gap:24px}}
@media print{.page-navigation,.quick-index{display:none}}
</style>'''
    marker = lambda text: '<!--quick-navigation-start-->'+text+'<!--quick-navigation-end-->'
    html = html.replace('</head>', marker(css)+'</head>')
    count = [0]
    def section(match):
        i = count[0]; count[0] += 1
        body = match.group(0)
        controls = f'<div class="page-navigation"><a href="#quick-navigation">Contents</a><a href="#{ids[max(0,i-1)]}">Previous</a><a href="#{ids[min(len(ids)-1,i+1)]}">Next</a></div>'
        addition = marker((index if i == 0 else '')+controls)
        return body.replace('</section>',addition+'</section>')
    result = re.sub(r'<section\b[^>]*class="page(?: [^"]*)?"[^>]*>.*?</section>',section,html,flags=re.S)
    assert count[0] == len(pages)
    return result


def package_pdf(source, output, labels, titles, cover_rect):
    doc = fitz.open(source)
    for page in doc:
        page.wrap_contents()
    destinations = []
    for title in titles:
        hits = [(i, rect) for i,p in enumerate(doc) for rect in p.search_for(title)]
        if not hits:
            raise ValueError('Section heading not found: '+title)
        # Prefer prominent headings over the cover's former contents list.
        ranked = []
        for i,rect in hits:
            spans = [s for b in doc[i].get_text('dict')['blocks'] if 'lines' in b for line in b['lines'] for s in line['spans'] if fitz.Rect(s['bbox']).intersects(rect)]
            ranked.append((max((s['size'] for s in spans),default=0),-i,i,rect))
        _,_,i,rect = max(ranked,key=lambda x:(x[0],x[1]))
        destinations.append((i,fitz.Point(0,max(0,rect.y0-24))))
    assert all(destinations[i][0] <= destinations[i+1][0] for i in range(len(destinations)-1)),destinations
    rect = fitz.Rect(cover_rect)
    assert not any(fitz.Rect(w[:4]).intersects(rect) for w in doc[0].get_text('words')), 'Index covers existing text'
    doc[0].draw_rect(rect,color=None,fill=(.95,.96,.97))
    x0,y0,x1,y1=rect
    doc[0].insert_text((x0+10,y0+14),'QUICK NAVIGATION / CLICK A SECTION',fontname='hebo',fontsize=8,color=(.09,.24,.39))
    cols=3;rows=(len(labels)+cols-1)//cols;cw=(x1-x0-20)/cols;rh=(y1-y0-27)/rows
    for n,(label,(target,point)) in enumerate(zip(labels,destinations)):
        col,row=divmod(n,rows);x=x0+10+col*cw;y=y0+29+row*rh
        text=f'{n+1:02d}  {label}'
        assert fitz.get_text_length(text,fontsize=7)<=cw-5,(label,cw)
        doc[0].insert_text((x,y),text,fontsize=7,color=(.09,.24,.39))
        doc[0].insert_link({'kind':fitz.LINK_GOTO,'from':fitz.Rect(x,y-9,x+cw-4,y+3),'page':target,'to':point})
    for i,p in enumerate(doc):
        for label,x,target in [('Contents',360,0),('Previous',424,max(0,i-1)),('Next',488,min(len(doc)-1,i+1))]:
            r=fitz.Rect(x-2,815,x+fitz.get_text_length(label,fontsize=7.5)+2,829)
            assert not any(fitz.Rect(w[:4]).intersects(r) for w in p.get_text('words')),(i,label)
            p.insert_text((x,825),label,fontname='NavigationArial',fontfile='C:/Windows/Fonts/arial.ttf',fontsize=7.5,color=(.09,.24,.39))
            p.insert_link({'kind':fitz.LINK_GOTO,'from':r,'page':target,'to':fitz.Point(0,0)})
    doc.set_toc([[1,label,target+1] for label,(target,_) in zip(labels,destinations)])
    output.parent.mkdir(parents=True,exist_ok=True)
    doc.save(output,garbage=4,deflate=True)
    doc.close()
    return [{'label':label,'page':target+1,'y':point.y} for label,(target,point) in zip(labels,destinations)]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode',choices=['html','pdf'])
    parser.add_argument('config',type=Path)
    args=parser.parse_args();cfg=json.loads(args.config.read_text(encoding='utf-8'));base=args.config.resolve().parent
    path=base/cfg['html']
    if args.mode=='html':
        path.write_bytes(add_html_navigation(path.read_text(encoding='utf-8'),cfg['labels']).encode('utf-8'))
    else:
        titles=[p.select_one('h1,h2').get_text(' ',strip=True) for p in BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser').select('section.page')]
        result=package_pdf(base/cfg['pdf_input'],base/cfg['pdf'],cfg['labels'],titles,cfg['cover_rect'])
        (base/cfg['section_map']).write_text(json.dumps(result,indent=2),encoding='utf-8')
        print(json.dumps(result))


if __name__=='__main__':
    main()
