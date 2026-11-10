import {chromium} from './report-visual-check/node_modules/playwright/index.mjs';
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const cfgPath=path.resolve(process.argv[2]);
const cfg=JSON.parse(fs.readFileSync(cfgPath,'utf8'));
const base=path.dirname(cfgPath);
const browser=await chromium.launch({channel:'msedge'});
const page=await browser.newPage({viewport:{width:1280,height:900}});
await page.goto(pathToFileURL(path.resolve(base,cfg.html)).href);
await page.emulateMedia({media:'print'});
await page.evaluate(()=>document.fonts.ready);
// HTML panel numbers become section numbers when physical PDF pages reflow.
await page.evaluate(()=>{
 const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
 while(walker.nextNode())walker.currentNode.textContent=walker.currentNode.textContent.replace(/\bpage (\d+)\b/g,'section $1');
});
await page.addStyleTag({content:`
@page{size:A4;margin:36pt 36pt 42pt}
@media print{
body{font-size:10pt;line-height:1.3;background:white}
.page{break-after:auto;page-break-after:auto;margin:0 0 16pt;border:0;max-width:none}
.page:first-child{break-after:page;page-break-after:always}
.band,.goldline,.kicker,h2,h3,h4,figcaption{break-after:avoid}
p{orphans:3;widows:3}thead{display:table-header-group}tr{break-inside:avoid}
.inner{padding:12pt 0 6pt}.band{padding:7pt 10pt;font-size:8pt}
.foot{display:none}.cover,.grid{grid-template-columns:minmax(0,1fr) 160pt;gap:14pt}
.duo,.cols2,.tbranches{grid-template-columns:repeat(2,minmax(0,1fr))}
.grid3,.kpis{grid-template-columns:repeat(3,minmax(0,1fr))}
.lede{font-size:11pt;line-height:1.3}.kpis{gap:5pt;margin:7pt 0 4pt}
.cover h3{margin:8pt 0 3pt}.cover .notes{font-size:8.5pt}
.cover .t.kv td{font-size:8pt;padding:2pt 3pt}
.cover .t.fin td,.cover .t.fin th{font-size:7.5pt;padding:2pt}
.cover .rbox{margin-bottom:7pt}.cover .rbox .tiny{font-size:7pt;line-height:1.25}
h2{font-size:16pt}h3{font-size:11pt}h4{font-size:10.5pt}.ctitle{font-size:23pt}
.ex{margin:10pt 0;break-inside:avoid}figcaption{font-size:10pt}
.src,.tiny{font-size:7.5pt}.xnote,.small{font-size:8pt}
.t{font-size:8.5pt}.t.fin td,.t.fin th{font-size:8pt;padding:3pt}
.t th,.t td{padding:4pt}.notes,.fb,.tleaf,.tengine,.tli,.cstep{font-size:9pt}
.notes .nh{font-size:8pt}.notes{padding:7pt}.notes p{margin-bottom:6pt}
.cw-d svg,.cw-d{max-width:100%;height:auto}.cw-m{display:none}.cw-d{display:block}
.quick-index,.page-navigation,.toc{display:none}
}`});
const output=path.resolve(base,cfg.pdf_input);fs.mkdirSync(path.dirname(output),{recursive:true});
// cfg.footer: running footer text for reports without their own @page margin boxes; omit it when the HTML prints its own.
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
await page.pdf({path:output,format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:Boolean(cfg.footer),
headerTemplate:'<div></div>',footerTemplate:cfg.footer?`<div style="font:7.5px Arial;width:100%;margin:0 36pt;display:flex;justify-content:space-between;color:#67717c"><span>${esc(cfg.footer)}</span><span class="pageNumber"></span></div>`:'<div></div>'});
await browser.close();console.log(output);
