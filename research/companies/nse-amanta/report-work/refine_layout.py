"""Add attributed issuer product photographs; preserve the research and model."""
from pathlib import Path
from bs4 import BeautifulSoup
import base64, json

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'report'
soup=BeautifulSoup((OUT/'report.html').read_text(encoding='utf-8'),'html.parser')

def photo(name,label,caption):
    data=base64.b64encode((ROOT/'product-assets'/name).read_bytes()).decode()
    mime='image/png' if name.endswith('.png') else 'image/jpeg'
    return f'<div class="product-card"><img src="data:{mime};base64,{data}" alt="Amanta {label}"><b>{label}</b><span>{caption}</span></div>'

fluid='<figure class="product-gallery"><figcaption>Product gallery A. Fluid therapy: two container platforms</figcaption><div class="product-grid fluid">'+photo('pro-img-slide-1.png','SteriPort / ISBM','Two-port polypropylene bottles; the platform expanded by Line 3.')+photo('pro-img-slide-2.png','Conventional FFS','Fluid-therapy bottles from the established product range.')+'</div><div class="source">Product photographs: Amanta Healthcare, <a href="https://www.amanta.co.in/fluid-therapy">official fluid-therapy catalogue</a>, accessed 10 Nov 2026. Representative packs; images are not evidence of market approvals or sales mix.</div></figure>'
svp='<figure class="product-gallery"><figcaption>Product gallery B. SVP: respiratory, ophthalmic and diluent presentations</figcaption><div class="product-grid svp">'+photo('respiratory-P1.jpg','Respiratory','Single-dose respiratory presentation.')+photo('ophthalmics-P5.jpg','Ophthalmics / drops','Conventional multi-dose dropper pack.')+photo('ophthalmics-P4.jpg','Ophthalmics / unit pack','Alternative eye/ear drop presentation.')+photo('diluents-P1.jpg','Diluents','Sterile-water packs and small-volume containers.')+'</div><div class="source">Product photographs: Amanta official <a href="https://www.amanta.co.in/respiratory">respiratory</a>, <a href="https://www.amanta.co.in/ophthalmics">ophthalmic</a> and <a href="https://www.amanta.co.in/diluents">diluent</a> catalogues, accessed 10 Nov 2026. Existing representative products; not photographs of the future SVP line or preservative-free development.</div></figure>'
pages=soup.select('section.page')
pages[3].select_one('.answer').insert_after(BeautifulSoup(fluid,'html.parser'))
pages[4].select_one('.answer').insert_after(BeautifulSoup(svp,'html.parser'))
# The monitoring paragraph, sources and takeaway were repeated verbatim across
# both question-answer panels. Keep the complete copy after the final answer.
for title in pages[33].select('h3'):
    if title.get_text()=='Dated evidence to watch':
        node=title
        while node and node.name!='footer':
            following=node.find_next_sibling()
            node.decompose()
            node=following
        break
css='''
/* Visual revision: clear photography, compact hierarchy, measured pagination. */
.product-grid{display:grid;gap:16px}.product-grid.fluid{grid-template-columns:1fr 1fr}.product-grid.svp{grid-template-columns:repeat(4,1fr);gap:12px}.product-card{display:flex;flex-direction:column;border-bottom:1px solid #bec7d2;padding:3px 7px 9px}.product-card img{display:block;width:100%;height:172px;object-fit:contain;margin-bottom:8px}.fluid .product-card img{height:190px}.product-card b{color:#31567e;font-size:12px;margin-bottom:3px}.product-card span{font-size:11px;line-height:1.3;color:#505b68}.product-gallery{margin:12px 0 15px}.flow-section-title{break-after:avoid;margin-top:18px}.flow-section-title .band{margin:0 0 10px;padding:10px 12px}.flow-section-title .band h1{font-size:19px}.flow-section-title .answer{margin-bottom:10px}.continuation{font-size:11px;color:#536d8a;border-bottom:1px solid #bec7d2;padding-bottom:7px;margin-bottom:12px}.flow-body>figure:first-child,.flow-body>h3:first-child{margin-top:0}
@media screen and (max-width:820px){.product-grid.svp{grid-template-columns:1fr 1fr}.product-card img,.fluid .product-card img{height:155px}.product-card span{font-size:12px}.product-card b{font-size:13px}.flow-section-title .band h1{font-size:21px}}
@media print{.page{height:296.5mm;min-height:296.5mm;padding-top:24px;padding-bottom:45px}.topline{margin-bottom:12px}.band{padding-top:12px;padding-bottom:12px;margin-bottom:13px}.band h1{font-size:16pt}.answer{margin-bottom:11px}p{margin-bottom:8px}h3{margin-top:12px;margin-bottom:6px}figure{margin-top:12px;margin-bottom:13px}td,th{padding-top:6px;padding-bottom:6px}.implication{margin-top:11px;padding-top:8px}.flow-section-title{margin-top:15px}.flow-section-title .band{margin:0 0 10px;padding:10px 12px}.flow-section-title .band h1{font-size:14pt}.flow-section-title.inset .band{padding:7px 10px;margin-bottom:7px}.flow-section-title.inset .band h1{font-size:12pt}.flow-section-title.inset .kicker{font-size:10px;margin-bottom:3px}.flow-section-title.inset .answer{font-size:10pt;margin-bottom:7px}.tight p{margin-bottom:6px}.tight figure{margin-top:8px;margin-bottom:8px}.tight td,.tight th{padding-top:5px;padding-bottom:5px}.tight h3{margin-top:10px}.product-gallery .source{font-size:7.8pt}.flow-body{display:flow-root}.flow-body>h3:first-child{margin-top:0}.scenario .flow-body>figure:first-child{margin-top:0}}
'''
soup.style.string=soup.style.string+css
(OUT/'report.html').write_text(str(soup),encoding='utf-8')
print('Added six official product photos in two galleries; removed one verbatim duplicate monitoring block. Unique analysis and model unchanged.')
