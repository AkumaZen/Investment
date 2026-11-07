"""Render trusted analyst-authored HTML content into an offline research document.

Usage: python render_report.py [report-content.json] [report.html]
Metadata and source fields are plain text. executive, section html and appendix
are trusted local HTML, not an interface for untrusted user submissions.
"""
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


CSS = r"""
:root{--ink:#202327;--muted:#565b61;--accent:#c00000;--rule:#c8ccd0;--wash:#f3f4f5}
*{box-sizing:border-box}html{scroll-padding-top:20px}body{margin:0;background:white;color:var(--ink);font:16px/1.5 Calibri,Arial,sans-serif;font-variant-numeric:tabular-nums}
a{color:var(--accent);text-underline-offset:3px;overflow-wrap:anywhere}a:hover{text-decoration-thickness:2px}a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:4px}
.skip{position:absolute;left:-9999px}.skip:focus{left:12px;top:12px;background:white;padding:12px;z-index:10}
.layout{max-width:1250px;margin:auto;display:grid;grid-template-columns:210px minmax(0,920px);gap:48px;padding:34px 30px 70px}.toc{position:sticky;top:24px;align-self:start;max-height:calc(100vh - 48px);overflow:auto;font-size:13px;line-height:1.3;padding-right:12px}.toc-title{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin:0 0 14px}.toc a{display:block;color:var(--muted);text-decoration:none;padding:5px 0}.toc a:hover,.toc a:focus{color:var(--accent)}.toc .n{display:inline-block;min-width:28px;color:var(--accent);font-weight:700}.mobile-toc{display:none}
main{min-width:0}.masthead{border-top:4px solid var(--accent);padding-top:18px}.eyebrow{color:var(--accent);font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}.masthead h1{font-size:34px;line-height:1.12;margin:12px 0 8px;letter-spacing:-.02em}.subtitle{font-size:19px;line-height:1.35;margin:0 0 18px}.meta{display:flex;flex-wrap:wrap;gap:8px 24px;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:10px 0;font-size:13px;color:var(--muted)}.meta strong{color:var(--ink)}button{background:white;border:1px solid var(--rule);padding:5px 12px;font:inherit;color:var(--ink);cursor:pointer;margin-left:auto}
.executive{padding:22px 0 26px;border-bottom:1px solid var(--rule)}.report-section{padding-top:32px;margin-top:20px;border-top:1px solid var(--rule);scroll-margin-top:20px}h2{font-size:24px;line-height:1.2;margin:0 0 16px}h2 .number{color:var(--accent);margin-right:12px}h3{font-size:18px;line-height:1.3;margin:24px 0 8px}h4{font-size:16px;margin:18px 0 6px}p{margin:8px 0 13px}.answer{font-size:18px;line-height:1.4;font-weight:700;margin-bottom:20px}.meaning{margin-top:20px;padding-top:10px;border-top:1px solid var(--rule)}.meaning strong{display:block;margin-bottom:5px}ul,ol{padding-left:22px}li{margin:5px 0}blockquote{margin:16px 0;padding-left:16px;border-left:2px solid var(--rule);color:var(--muted)}
.table-wrap{max-width:100%;overflow-x:auto;margin:16px 0;overscroll-behavior-x:contain}table{width:100%;border-collapse:collapse;font-size:14px;line-height:1.35;margin:14px 0} .table-wrap table{margin:0}caption{text-align:left;font-weight:700;font-size:16px;margin-bottom:8px}th,td{padding:8px 9px;text-align:left;vertical-align:top;border-bottom:1px solid #dedfe1}th{background:var(--wash);font-weight:700;border-top:1px solid var(--rule);border-bottom:1px solid #999}th:first-child,td:first-child{padding-left:6px}td.num,th.num,.number-cell{text-align:right;white-space:nowrap}tr.total td,tfoot td{font-weight:700;border-top:1px solid #777}thead{display:table-header-group}.source,.sources,.footnote,figcaption,.caption{font-size:12px;line-height:1.4;color:var(--muted)}.source{margin-top:6px}.sources li{margin-bottom:12px}.sources a{font-weight:700}.sources .detail{display:block;margin-top:3px}.sources li:target{background:#fff4ec}.muted{color:var(--muted)}.accent{color:var(--accent)}.status{font-weight:700}.exhibit,figure{margin:22px 0}figure svg,.exhibit svg,svg.chart{display:block;max-width:100%;height:auto}svg text{font-family:Calibri,Arial,sans-serif}.exhibit-title{font-weight:700;font-size:17px;margin-bottom:8px}.chart-pair{display:grid;grid-template-columns:1fr 1fr;gap:24px}.appendix{margin-top:40px;padding-top:22px;border-top:2px solid var(--ink)}footer{border-top:1px solid var(--rule);margin-top:32px;padding-top:14px;font-size:12px;color:var(--muted)}
@media(max-width:1000px){.layout{gap:25px;grid-template-columns:180px minmax(0,1fr);padding:24px 22px}.masthead h1{font-size:30px}}
@media(max-width:767px){body{font-size:16px}.layout{display:block;padding:20px 18px 45px}.toc{display:none}.mobile-toc{display:block;border-bottom:1px solid var(--rule);margin-bottom:22px;padding-bottom:12px;font-size:14px}.mobile-toc summary{cursor:pointer;font-weight:700}.mobile-toc nav{columns:2;column-gap:18px;padding-top:10px}.mobile-toc a{display:block;padding:5px 0;break-inside:avoid;color:var(--ink);text-decoration:none}.mobile-toc .n{color:var(--accent);font-weight:700;margin-right:6px}.masthead h1{font-size:29px}.subtitle{font-size:18px}h2{font-size:23px}.answer{font-size:18px}.report-section{margin-top:14px;padding-top:24px}.chart-pair{grid-template-columns:1fr}th,td{padding:7px}button{margin-left:0}}
@page{size:A4 portrait;margin:36pt}
@media print{body{font-size:10pt;line-height:13pt;color:#111}.layout{display:block;max-width:none;padding:0;margin:0}.toc,.mobile-toc,.skip,button{display:none!important}.masthead{border-top:2pt solid var(--accent);padding-top:10pt}.masthead h1{font-size:23pt}.subtitle{font-size:13pt}.eyebrow,.meta{font-size:8pt}.meta{padding:6pt 0}.executive{padding:10pt 0}h2{font-size:14pt;line-height:17pt}h3{font-size:11pt;line-height:14pt;margin-top:14pt}h4{font-size:10pt}.answer{font-size:11pt;line-height:14pt;margin-bottom:12pt}.report-section{break-before:page;margin:0;padding-top:10pt;border-top:.5pt solid var(--rule)}h2,h3,h4,.exhibit-title,caption{break-after:avoid}p{orphans:3;widows:3;margin:5pt 0 7pt}table{font-size:8.5pt;line-height:11pt;table-layout:auto}th,td{padding:4pt 5pt;overflow-wrap:anywhere}thead{display:table-header-group}tr{break-inside:avoid}.table-wrap{overflow:visible;max-width:none;margin:9pt 0}.source,.sources,.footnote,figcaption,.caption,footer{font-size:7.5pt;line-height:10pt}.exhibit-title{font-size:10pt;line-height:13pt}figure,.exhibit{margin:12pt 0;break-inside:avoid}svg{max-width:100%!important}.appendix{break-before:page;margin:0;padding-top:10pt}.sources li{break-inside:avoid}.meaning{padding-top:6pt;margin-top:10pt}a{color:inherit;text-decoration:none}.chart-pair{gap:16pt}footer{margin-top:18pt}*{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""


def plain(value: object) -> str:
    return escape(str(value), quote=True)


def analytical_html(value: str) -> str:
    # Table overflow belongs to an internal container, never the document body.
    # An existing wrapper is harmless: only the inner wrapper will need to scroll.
    return re.sub(r'(<table\b[^>]*>.*?</table\s*>)',
                  r'<div class="table-wrap" tabindex="0" role="region" aria-label="Scrollable evidence table">\1</div>',
                  value, flags=re.IGNORECASE | re.DOTALL)


def validate(content: dict) -> None:
    for name in ('title', 'subtitle', 'date', 'status', 'executive', 'sections', 'sources'):
        if name not in content:
            raise ValueError(f'Missing report field: {name}')
    if not isinstance(content['sections'], list) or not content['sections']:
        raise ValueError('sections must be a nonempty list')
    ids = set()
    for section in content['sections']:
        for name in ('id', 'title', 'answer', 'html'):
            if not isinstance(section.get(name), str) or not section[name].strip():
                raise ValueError(f'Section requires nonempty {name}')
        ident = section['id']
        if not re.fullmatch(r'S[1-9][0-9]*', ident) or ident in ids:
            raise ValueError(f'Invalid or duplicate section id: {ident}')
        ids.add(ident)
    source_ids = set()
    for source in content['sources']:
        ident = str(source['id'])
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', ident) or ident in source_ids:
            raise ValueError(f'Invalid or duplicate source id: {ident}')
        source_ids.add(ident)
        url = str(source.get('url', ''))
        if url and urlsplit(url).scheme not in ('https', 'http'):
            raise ValueError(f'Unsupported source URL: {ident}')


def render(content: dict) -> str:
    """Return complete HTML. Supplied analytical HTML is intentionally preserved."""
    validate(content)
    toc = ''.join(f'<a href="#{s["id"]}"><span class="n">{s["id"][1:]}</span>{plain(s["title"])}</a>' for s in content['sections'])
    toc += '<a href="#sources">Sources and evidence</a>'
    sections = ''.join(f'<section class="report-section" id="{s["id"]}" aria-labelledby="heading-{s["id"]}"><h2 id="heading-{s["id"]}"><span class="number">{s["id"]}</span>{plain(s["title"])}</h2><p class="answer">{plain(s["answer"])}</p>{s["html"]}</section>' for s in content['sections'])
    sources = []
    for source in content['sources']:
        title = plain(source['title'])
        if source.get('url'):
            title = f'<a href="{plain(source["url"])}" rel="noopener noreferrer">{title}</a>'
        sources.append(f'<li id="source-{plain(source["id"])}"><strong>[{plain(source["id"])}]</strong> {title}<span class="detail">{plain(source.get("detail", ""))}</span></li>')
    appendix = content.get('appendix', '')
    appendix = f'<div class="appendix" id="appendix"><h2>Appendix</h2>{appendix}</div>' if appendix else ''
    document = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><title>{plain(content['title'])} | Equity research</title><style>{CSS}</style></head>
<body><a class="skip" href="#report">Skip to report</a><div class="layout">
<nav class="toc" aria-label="Report contents"><p class="toc-title">Contents</p>{toc}</nav>
<main id="report"><details class="mobile-toc"><summary>Report contents</summary><nav aria-label="Mobile report contents">{toc}</nav></details>
<header class="masthead"><div class="eyebrow">Independent research | India equities</div><h1>{plain(content['title'])}</h1><p class="subtitle">{plain(content['subtitle'])}</p><div class="meta"><span><strong>Analysis date</strong> {plain(content['date'])}</span><span><strong>Status</strong> {plain(content['status'])}</span><button type="button" onclick="window.print()">Print / Save PDF</button></div></header>
<div class="executive" aria-label="Executive assessment">{content['executive']}</div>
{sections}{appendix}<section class="appendix" id="sources"><h2>Sources and evidence</h2><ol class="sources">{''.join(sources)}</ol></section>
<footer>Research for learning and independent analysis. This document is not a recommendation to transact. Estimates and illustrative scenarios are uncertain; consult the stated limitations and original evidence.</footer>
</main></div></body></html>'''
    return analytical_html(document)


def main() -> None:
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='?', type=Path, default=base / 'report-content.json')
    parser.add_argument('output', nargs='?', type=Path, default=base / 'report.html')
    args = parser.parse_args()
    content = json.loads(args.input.read_text(encoding='utf-8-sig'))
    args.output.write_text(render(content), encoding='utf-8')
    print(f'Wrote {args.output} ({len(content["sections"])} sections)')


if __name__ == '__main__':
    main()
