import { chromium } from './tools/report-visual-check/node_modules/playwright/index.mjs';
import fs from 'node:fs';import path from 'node:path';import {pathToFileURL} from 'node:url';
const browser=await chromium.launch({channel:'msedge'});let results=[];
for(const file of ['research/companies/nse-augmont/v3/navigation.json','research/companies/nse-concordbio/report/navigation.json']){
 const cfg=JSON.parse(fs.readFileSync(file));const base=path.dirname(file);
 for(const width of [1280,390]){
  const page=await browser.newPage({viewport:{width,height:900}});await page.goto(pathToFileURL(path.resolve(base,cfg.html)).href);
  const ids=await page.locator('section.page').evaluateAll(es=>es.map(e=>e.id));
  for(let i=0;i<ids.length;i++){
   const a=page.locator('.quick-index a').nth(i);await a.click();if(await page.evaluate(()=>decodeURIComponent(location.hash))!=='#'+ids[i])throw Error('Index target');
   const nav=page.locator('section.page').nth(i).locator('.page-navigation a');
   for(const [n,target] of [[1,ids[Math.max(0,i-1)]],[2,ids[Math.min(ids.length-1,i+1)]],[0,'quick-navigation']]){
    await nav.nth(n).click();if(await page.evaluate(()=>decodeURIComponent(location.hash))!=='#'+target)throw Error('Control target');
   }
  }
  results.push({file,width,index_links_clicked:ids.length,page_controls_clicked:ids.length*3,passed:true});await page.close();
 }
}
await browser.close();fs.writeFileSync('tmp/pdfs/navigation/browser-interactions.json',JSON.stringify(results,null,2));console.log(JSON.stringify(results));
