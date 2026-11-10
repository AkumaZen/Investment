"""Amanta research report. Primary-source data, editable HTML/SVG; PDF via Edge print.
All source locators are PHYSICAL PDF pages. Financial values INR crore.
"""
from pathlib import Path
import json, math, html, hashlib, re
from datetime import date

ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'report'
OUT.mkdir(exist_ok=True)
SOURCES={
 'AR':('FY26 Annual report','https://www.amanta.co.in/public/assets/pdf/Investors/Annual-Report/amanta-annual-report-2025-26.pdf'),
 'C3':('Q3 FY26 call, 11 Feb 2026','https://www.amanta.co.in/public/assets/pdf/Investors/investor-meet/outcome-transcript-16-02-2026.pdf'),
 'C4':('Q4 FY26 call, 19 May 2026','https://www.amanta.co.in/public/assets/pdf/Investors/investor-meet/amanta-outcome-transcript-q4-fy-2025-26.pdf'),
 'C1':('Q1 FY27 call, 6 Aug 2026','https://www.amanta.co.in/public/assets/pdf/Investors/investor-meet/amanta-outcome-transcript-q1-fy-2026-27.pdf'),
 'C2':('Q2 FY27 call, 4 Nov 2026','https://www.amanta.co.in/public/assets/pdf/Investors/investor-meet/amanta-outcome-transcript-q2-fy-2026-27.pdf'),
 'P3':('Q3 FY26 presentation','https://www.amanta.co.in/public/assets/pdf/Investors/investor-meet/intimation-under-regulation-30-investor-presentation.pdf'),
 'P4':('Q4 FY26 presentation','https://www.amanta.co.in/public/assets/pdf/Investors/investor-meet/amanta-investor-presentation-q4-fy-2025-26.pdf'),
 'P1':('Q1 FY27 presentation','https://www.amanta.co.in/public/assets/pdf/Investors/investor-meet/amanta-investor-presentation-fy-2026-27-q1.pdf'),
 'P2':('Q2 FY27 presentation','https://www.amanta.co.in/public/assets/pdf/Investors/investor-meet/amanta-investor-presentation-fy-2026-27-q2.pdf'),
 'NSE':('NSE EQ bhavcopy, 9 Nov 2026','https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_09112026.csv'),
 'SC':('Screener standalone, retrieved 10 Nov 2026','https://www.screener.in/company/AMANTA/'),
 'EA':('Official announcement archive','https://www.amanta.co.in/exchange-announcements'),
}
def ref(s,p=None):
 label,url=SOURCES[s]
 return f'<a href="{url}'+(f'#page={p}' if p else '')+'">'+s+(f' p.{p}' if p else '')+'</a>'
def src(*r,note=''):
 return '<div class="source">Source: '+ '; '.join(ref(x[0],x[1]) if isinstance(x,tuple) else ref(x) for x in r)+('. '+note.rstrip('.') if note else '')+'. PDF locators are physical pages.</div>'
def p(t):return '<p>'+t+'</p>'
def h(t):return '<h3>'+t+'</h3>'
def note(t):return '<p class="implication"><b>What this means for you.</b> '+t+'</p>'
def table(head,rows,cls=''):
 if 'numeric' in cls and len(head)>=5:cls+=' mobile-stack'
 return '<div class="table-wrap"><table class="'+cls+'"><thead><tr>'+''.join('<th>'+str(x)+'</th>' for x in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td data-label="'+html.escape(str(head[i]),quote=True)+'">'+str(x)+'</td>' for i,x in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'

EX=0
def exhibit(title,content,sources=''):
 global EX
 EX+=1
 return f'<figure><figcaption>Exhibit {EX}. {title}</figcaption>{content}{sources}</figure>'
def pair(a,b):return '<div class="pair">'+a+b+'</div>'
def bars(labels,vals,unit='',colors=None,height=220,maxval=None,fmt='.0f'):
 def draw(w):
  left=112;right=66 if w==680 else 48;top=30;row=(height-55)/len(vals);xmax=maxval or max(vals)*1.12
  parts=[f'<svg role="img" aria-label="{html.escape(unit)}" viewBox="0 0 {w} {height}">',f'<text x="0" y="14" class="unit">{html.escape(unit)}</text>']
  for j in range(5):
   x=left+(w-left-right)*j/4
   parts += [f'<line x1="{x}" y1="25" x2="{x}" y2="{height-22}" stroke="#e6e8eb"/>',f'<text x="{x}" y="{height-4}" text-anchor="middle" class="tick">{xmax*j/4:.0f}</text>']
  for i,(label,v) in enumerate(zip(labels,vals)):
   y=top+i*row;bw=max(0,v)/xmax*(w-left-right);color=(colors[i] if colors else ('#39608e' if i==len(vals)-1 else '#b4becb'))
   parts += [f'<text x="{left-10}" y="{y+row*.49}" text-anchor="end">{html.escape(label)}</text>',f'<rect x="{left}" y="{y+3}" width="{bw}" height="{row*.63}" fill="{color}"/>',f'<text x="{left+bw+7}" y="{y+row*.49}" class="value">{v:{fmt}}</text>']
  return ''.join(parts+['</svg>'])
 return '<div class="chart-desktop">'+draw(680)+'</div><div class="chart-mobile">'+draw(340)+'</div>'

def steps(items):
 return '<ol class="process">'+''.join('<li><b>'+a+'</b><span>'+b+'</span></li>' for a,b in items)+'</ol>'
PAGES=[]
def page(section,title,answer,body,tag='',layout='standard',question='',sources=()):
 PAGES.append(dict(section=section,title=title,answer=answer,body=body,tag=tag,layout=layout,question=question or title,sources=sources))

# Reconciled audited anchors. AR physical52,53; R27 physical3-6; INR lakh /100.
CMP=202.15; SHARES=3.8829351
HIST={
 'FY25':dict(sales=274.7082,op=59.6685,oi=1.3852,interest=27.9479,dep=18.3989,pbt=14.7069,pat=10.5007,eps=3.71),
 'FY26':dict(sales=287.6767,op=59.8585,oi=3.3707,interest=20.7457,dep=18.73,pbt=21.1247,pat=14.8752,eps=4.33,exceptional=2.6288),
}
# Exact FY25 P&L anchors are overwritten from primary extraction below before release.
H1=dict(sales=151.9356,op=31.7343,oi=1.3984,interest=11.8490,dep=9.9652,pbt=11.3185,pat=8.1714)
Q2=dict(sales=83.1324,op=17.1949,oi=.7554,interest=5.8442,dep=5.2799,pbt=6.8262,pat=4.8609)

def make_model():
 # All projected values are E, conditional illustrations of disclosed drivers, never company forecasts.
 cfg={
 'Bear':dict(multiple=11,line3=[40,85,95],svp=[0,8,16],legacy=[1,1,1.02],margins=[20,21,22],dep=[21,25,26],rates=[11,10.5,10],tax=29,wc=150,capex=[22,18,15],release=[15,8,0]),
 'Base':dict(multiple=14,line3=[60,110,110],svp=[0,16,32],legacy=[1,1,1.05],margins=[23,25,25],dep=[21,25,26],rates=[10.5,9.5,9],tax=28,wc=141,capex=[22,18,15],release=[15,8,0]),
 'Bull':dict(multiple=17,line3=[65,120,120],svp=[0,30,60],legacy=[1.03,1.06,1.09],margins=[24,27,28],dep=[21,25,27],rates=[10,9,8.5],tax=27,wc=125,capex=[22,20,20],release=[15,8,0]),
 }
 out={}
 for name,c in cfg.items():
  net=202.2177;prevsales=287.6767;prevpat=HIST['FY26']['pat'];rows={};book=228.1289
  # Opening Sep26 operating working capital. Inventory+receivables-payables-contract liabilities.
  wc_open=88.6476+44.2206-34.7321-8.3699
  wc_march=82.7094+43.0235-35.8939-8.8752
  for j,fy in enumerate(['FY27E','FY28E','FY29E']):
   sales=287.6767*c['legacy'][j]+c['line3'][j]+c['svp'][j];op=sales*c['margins'][j]/100;oi=1.6 if j==0 else 1
   fraction=.5 if j==0 else 1
   # H2 financing costs plus actual H1; later full-year opening net-debt basis, simplifying intra-year balances.
   interest=(H1['interest']+net*c['rates'][j]/100*.5) if j==0 else net*c['rates'][j]/100
   dep=c['dep'][j];pbt=op+oi-interest-dep;tax=pbt*c['tax']/100;pat=pbt-tax
   # WC days is an E operating-days proxy applied to sales, not the issuer's unbridged 141-day definition.
   # Normalised opening to September sales run-rate prevents artificially releasing all working capital.
   targetwc=wc_march+(sales-prevsales)*c['wc']/365 if j==0 else wc_open+(sales-prevsales)*c['wc']/365
   dwc=targetwc-wc_open;wc_open=targetwc
   # Cash available after interest/tax: H2 only in FY27, full-year thereafter. Depreciation non-cash.
   cashop=(op-H1['op'])-(interest-H1['interest'])-(tax-3.1471)-dwc if j==0 else op-interest-tax-dwc
   aftercapex=cashop-c['capex'][j]
   net=net-aftercapex-c['release'][j]
   book+=pat-(H1['pat'] if j==0 else 0)
   ev=op*c['multiple'];equity=ev-net;price=equity/SHARES
   yrs=(date(2000+int(fy[2:4]),3,31)-date(2026,11,9)).days/365.25
   r=dict(sales=sales,expenses=sales-op,op=op,opm=c['margins'][j],oi=oi,interest=interest,dep=dep,pbt=pbt,tax_pct=c['tax'],tax=tax,pat=pat,eps=pat/SHARES,pat_growth=(pat/prevpat-1)*100,pat_margin=pat/sales*100,multiple=c['multiple'],net_debt=net,ev=ev,equity=equity,price=price,ret=(price/CMP-1)*100,cagr=((price/CMP)**(1/yrs)-1)*100,wc_add=dwc,capex=c['capex'][j],reserved_release=c['release'][j],cashop=cashop,fcf=aftercapex,book=book,years=yrs,line3=c['line3'][j],svp=c['svp'][j],legacy=287.6767*c['legacy'][j])
   assert abs(pbt-(op+oi-interest-dep))<1e-8
   assert abs(equity-(ev-net))<1e-8
   assert abs(price*SHARES-equity)<1e-8
   assert net>0
   rows[fy]=r;prevsales=sales;prevpat=pat
  out[name]=dict(inputs=c,rows=rows)
 return out
MODEL=make_model()
def f(v,d=1):return f'({abs(v):,.{d}f})' if v<0 else f'{v:,.{d}f}'

CSS='''
.chart-mobile{display:none}.pair .chart-desktop{display:none}.pair .chart-mobile{display:block}
*{box-sizing:border-box}body{margin:0;color:#171b20;background:#e8eaed;font-family:Arial,sans-serif;font-size:13.5px;line-height:1.35;font-variant-numeric:tabular-nums}a{color:#31567e;text-decoration:none}nav{position:absolute;left:max(12px,calc(50% - 603px));top:30px;width:170px;font-size:12px;line-height:1.6}nav a{display:block}nav b{display:block;border-bottom:1px solid #a9b5c3;padding-bottom:5px;margin-bottom:6px}.document{width:794px;margin:20px auto}.page{position:relative;background:#fff;min-height:1120px;padding:31px 42px 48px;margin:0 0 22px;break-after:page}.topline{display:flex;justify-content:space-between;font-size:11px;color:#565d67;margin-bottom:16px}.identity{letter-spacing:1.3px;font-weight:bold;color:#39608e}.band{background:#d9d9d9;margin:0 -42px 18px;padding:15px 42px 16px}.band .kicker{font-size:12px;margin-bottom:6px}.band h1{font-size:22px;line-height:1.16;margin:0;font-weight:normal}.answer{font-weight:bold;font-size:14px;line-height:1.4;margin:0 0 15px;color:#182f49}p{margin:0 0 10px}h3{font-size:14px;line-height:1.25;margin:16px 0 7px}h4{font-size:13px;margin:10px 0 5px}.source{font-size:10.8px;line-height:1.25;color:#626974;margin-top:6px}.source a{color:#536d8a}.implication{border-top:1px solid #a4b3c4;padding-top:9px;margin-top:15px}.implication b{color:#39608e}figure{margin:16px 0 17px;break-inside:avoid}figcaption{font-weight:bold;font-size:12.5px;line-height:1.3;margin-bottom:7px}svg{display:block;width:100%;height:auto;font:13px Arial,sans-serif}svg .tick{font-size:11px;fill:#6a737d}svg .unit{font-size:12px;fill:#596471}svg .value{font-weight:bold;fill:#223d5d}.pair{display:grid;grid-template-columns:1fr 1fr;gap:22px}.pair figure{margin-top:10px}.table-wrap{width:100%;overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:11.7px;line-height:1.3}th{background:#39608e;color:white;font-weight:bold;text-align:left;padding:7px 7px}td{vertical-align:top;padding:7px 7px;border-bottom:0.5px solid #d5dbe1}tr:nth-child(even) td{background:#f3f5f7}table.numeric td:not(:first-child),table.numeric th:not(:first-child){text-align:right;white-space:nowrap}.numeric td:first-child{width:31%}tbody tr:last-child td{border-bottom:1px solid #6a7d94}.smalltable td{padding-top:5px;padding-bottom:5px}.process{list-style:none;padding:0;margin:14px 0;counter-reset:step}.process li{counter-increment:step;display:grid;grid-template-columns:27px 180px 1fr;gap:10px;border-bottom:1px solid #d5dbe1;padding:11px 0}.process li:before{content:counter(step);color:#39608e;font-weight:bold}.process span{color:#4a535e}.footer{position:absolute;bottom:20px;left:42px;right:42px;display:flex;justify-content:space-between;border-top:0.5px solid #bdc7d2;padding-top:6px;font-size:10px;color:#67717d}.executive{display:grid;grid-template-columns:2fr 1fr;gap:25px}.rail{border-left:1px solid #adb8c5;padding-left:16px}.rail h3{background:#dedede;color:#222;font-size:12px;padding:5px;text-align:center;margin:10px 0 6px}.rail table{font-size:11px}.rail td{padding:5px 1px;border-bottom:0}.rail td:last-child{text-align:right;font-weight:bold}.status{font-weight:bold;color:#39608e}.deck{font-size:12px;color:#69737f}.subtle{color:#596675}.estimate{color:#39608e}.contentsline{border-top:1px solid #bec7d2;padding-top:8px;font-size:11px}.twocol{columns:2;column-gap:25px}.twocol p{break-inside:avoid}.quote{border-left:2px solid #39608e;padding-left:12px}.scenario table{font-size:11.7px}.scenario td{padding:6px}.scenario td:nth-child(n+4){background:#edf2f8}.scenario p{margin-bottom:9px}.scenario th:nth-child(n+4){background:#6684a6}.source-index td:first-child{width:12%;font-weight:bold}.source-index td:last-child{width:68%}.source-index a{overflow-wrap:anywhere}
@media screen and (max-width:1180px){nav{position:static;width:auto;margin:15px auto;padding:10px 16px;max-width:794px;columns:3}.document{margin-top:10px}}@media screen and (max-width:820px){.chart-desktop{display:none}.chart-mobile{display:block}body{font-size:15px;background:#fff}.document{width:100%;margin:0}.page{width:100%;min-height:0;padding:25px 19px 52px;margin:0;border-bottom:6px solid #e8ebef}.band{margin:0 -19px 16px;padding:15px 19px}.band h1{font-size:22px}.answer{font-size:15px}h3{font-size:16px}.pair,.executive{grid-template-columns:1fr}.rail{border-left:0;border-top:1px solid #adb8c5;padding:10px 0 0}.rail table{font-size:13px}.source{font-size:11px}.footer{left:19px;right:19px;font-size:10px}.topline{font-size:10px}.process li{grid-template-columns:22px 1fr}.process span{grid-column:2}table{font-size:12px;min-width:0}.mobile-stack thead{display:none}.mobile-stack,.mobile-stack tbody{display:block;width:100%}.mobile-stack tr{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));border-bottom:1px solid #a4b3c4}.mobile-stack td{display:flex;justify-content:space-between;gap:8px;width:auto!important;padding:8px 6px!important;text-align:right!important}.mobile-stack td:first-child{grid-column:1/-1;font-weight:bold;background:#e8edf3!important;text-align:left!important}.mobile-stack td:not(:first-child):before{content:attr(data-label);text-align:left;color:#596675;font-size:11px;font-weight:normal}.mobile-stack td:nth-child(n+4){background:transparent}table:not(.numeric) td:first-child,table:not(.numeric) th:first-child{width:25%}td,th{padding:7px 5px;overflow-wrap:anywhere}.numeric td:not(:first-child),.numeric th:not(:first-child){white-space:normal}.numeric td:first-child{width:27%}.funding{table-layout:fixed}.funding td:first-child{width:22%}.funding td,.funding th{white-space:normal!important;font-size:11.5px;padding:6px 3px}.scenario table{font-size:11px;line-height:1.28}.scenario td,.scenario th{padding:6px 3px}.twocol{columns:1}nav{columns:2;font-size:12px}.pair svg{max-width:100%}.table-wrap{overflow-x:auto}svg{min-width:0}}
@media print{@page{size:A4;margin:0}body{background:#fff;font-size:10pt;line-height:1.3}.document{width:210mm;margin:0}nav{display:none}.page{width:210mm;min-height:296.5mm;margin:0;padding:28px 42px 46px;break-after:page;page-break-after:always}.page:last-child{break-after:auto;page-break-after:auto}.band{margin-bottom:17px}.band h1{font-size:16.5pt}.answer{font-size:10.5pt}h3{font-size:10.5pt}table{font-size:8.7pt}.source{font-size:7.8pt}.footer{bottom:18px}.table-wrap{overflow:visible}.scenario table{font-size:8.7pt}a{color:inherit}.source a{color:#536d8a}tr,figure{break-inside:avoid}thead{display:table-header-group}.pair{grid-template-columns:1fr 1fr}.executive{grid-template-columns:2fr 1fr}.rail{border-left:1px solid #adb8c5;border-top:0;padding:0 0 0 16px}}
'''

def write_report():
 spec=[];chunks=[];seen=set();toc=[]
 for i,q in enumerate(PAGES,1):
  section=q['section'];ident=section if section not in seen else section+'-'+str(i);seen.add(section)
  if ident==section:toc.append((ident,q['tag'] or q['title']))
  chunks.append(f'<section class="page {q["layout"]}" id="{ident}"><div class="topline"><span>10 November 2026 | India equities | INR</span><span class="identity">INVESTMENT RESEARCH</span></div><header class="band"><div class="kicker">AMANTA HEALTHCARE | {section} {q["tag"]}</div><h1>{q["title"]}</h1></header><div class="answer">{q["answer"]}</div>{q["body"]}<footer class="footer"><span>Amanta Healthcare | Evidence through 9 November 2026</span><span>{i}</span></footer></section>')
  spec.append(dict(page=i,page_id=ident,report_type='Comprehensive company research',family='MQ',question=q['question'],answer=q['answer'],layout=q['layout'],evidence_status='Reported facts; G management targets; E estimates identified',source_refs=q['sources'],interpretation=q['answer'],limitation='See page source notes and assumptions',next_question=PAGES[i]['question'] if i<len(PAGES) else 'Monitor the dated thesis tests',qa=dict(arithmetic=True,source_checked=False,visual_checked=False)))
 nav='<nav aria-label="Report contents"><b>Report contents</b>'+''.join(f'<a href="#{a}">{a} {b}</a>' for a,b in toc)+'</nav>'
 doc='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Amanta Healthcare | Capacity into cash</title><style>'+CSS+'</style></head><body>'+nav+'<main class="document">'+''.join(chunks)+'</main></body></html>'
 head,sep,body=doc.partition('<body>')
 def tidy_text(m):
  t=re.sub(r'(?<=[a-z])(?=[0-9₹])|(?<=[0-9])(?=cr\b)|(?<=₹)(?=[A-Za-z])',' ',m[1])
  t=re.sub(r'(?<=\d)(?=Nov\b|Dec\b|Jan\b|Feb\b|Mar\b|Apr\b|May\b|Jun\b|Jul\b|Aug\b|Sep\b|Oct\b|days\b|sales\b|years\b|months\b)',' ',t)
  return '>'+t.replace('A10%','A 10%')+'<'
 doc=head+sep+re.sub(r'>([^<>]+)<',tidy_text,body)
 assert '\u2014' not in doc and '\u2013' not in doc
 (OUT/'report.html').write_text(doc,encoding='utf-8')
 (ROOT/'page-specifications.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
 (OUT/'valuation-model.json').write_text(json.dumps(dict(cmp=CMP,shares_cr=SHARES,historical=HIST,h1=H1,scenarios=MODEL),indent=2),encoding='utf-8')
 print('Wrote',len(PAGES),'pages;',EX,'exhibits;',len(doc),'HTML bytes')

# Company-specific page composition is in report_content.py to keep data/model auditable.
exec((ROOT/'report_content.py').read_text(encoding='utf-8'))
write_report()
