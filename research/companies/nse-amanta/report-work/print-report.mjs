import { chromium } from '../../../../tools/report-visual-check/node_modules/playwright/index.mjs';
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const root=path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/,'$1'));
const base=decodeURIComponent(root);
const browser=await chromium.launch({channel:'msedge'});
const ctx=await browser.newContext({viewport:{width:1280,height:900}});
const page=await ctx.newPage();
await page.goto(pathToFileURL(path.join(base,'../report/report.html')).href);
await page.emulateMedia({media:'print'});
await page.evaluate(()=>document.fonts.ready);
const metrics=await page.evaluate(()=>[...document.querySelectorAll('section.page')].map((p,i)=>{
 const r=p.getBoundingClientRect(),f=p.querySelector('footer').getBoundingClientRect();
 const els=[...p.children].filter(x=>!x.matches('footer'));
 const bottom=Math.max(...els.map(x=>x.getBoundingClientRect().bottom));
 return {page:i+1,id:p.id,height:r.height,contentBottom:bottom-r.top,footerTop:f.top-r.top,footerCollision:bottom>f.top-6};
}));
fs.writeFileSync(path.join(base,'qa/print-metrics.json'),JSON.stringify(metrics,null,2));
const output=path.resolve(base,'../report/amanta-healthcare-equity-research.pdf');
await page.pdf({path:output,format:'A4',printBackground:true,preferCSSPageSize:true,displayHeaderFooter:false});
console.log(JSON.stringify({output,pages:metrics.length,overflow:metrics.filter(x=>x.height>1123),footerCollisions:metrics.filter(x=>x.footerCollision)}));
await browser.close();

