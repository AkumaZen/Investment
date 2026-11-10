import {chromium} from '../../../../tools/report-visual-check/node_modules/playwright/index.mjs';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url));
const expectedPages=JSON.parse(fs.readFileSync(path.join(root,'page-specifications.json'),'utf8')).length;
const browser=await chromium.launch({channel:'msedge'});const results=[];
for(const mobile of [false,true]){
 const context=await browser.newContext({viewport:{width:mobile?390:1440,height:900},isMobile:mobile,hasTouch:mobile});
 const p=await context.newPage();await p.goto(pathToFileURL(path.resolve(root,'../report/report.html')).href);
 await p.locator('nav a[href="#S20"]').click();
 const data=await p.evaluate(()=>({hash:location.hash,pages:document.querySelectorAll('section.page').length,exhibits:[...document.querySelectorAll('figcaption')].filter(x=>!x.hasAttribute('data-repeat')&&x.textContent.startsWith('Exhibit')).length,productGalleries:document.querySelectorAll('.product-gallery').length,productPhotos:document.images.length,imagesLoaded:[...document.images].every(x=>x.complete&&x.naturalWidth>0),allNumericCellLabels:[...document.querySelectorAll('.mobile-stack td')].every(x=>x.hasAttribute('data-label')),horizontalOverflow:document.documentElement.scrollWidth>innerWidth+1,scrollY}));
 await p.mouse.wheel(0,350);await p.waitForTimeout(100);
 data.scrollResponds=(await p.evaluate(()=>scrollY))>data.scrollY;
 if(data.hash!=='#S20'||data.pages!==expectedPages||data.exhibits!==47||data.productPhotos!==6||data.productGalleries!==2||!data.imagesLoaded||data.horizontalOverflow||!data.scrollResponds||!data.allNumericCellLabels)throw new Error(JSON.stringify(data));
 results.push({viewport:mobile?'390 touch':'1440 desktop',...data});await context.close();
}
fs.writeFileSync(path.join(root,'qa/delivery-interaction-check.json'),JSON.stringify(results,null,2));
console.log(JSON.stringify(results));await browser.close();
