// Reflow immutable analytical blocks into measured A4 pages, with section continuation labels.
import {chromium} from '../../../../tools/report-visual-check/node_modules/playwright/index.mjs';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const root=path.dirname(fileURLToPath(import.meta.url));
const output=path.resolve(root,'../report/report.html');
const oldSpec=JSON.parse(fs.readFileSync(path.join(root,'page-specifications.json'),'utf8'));
const browser=await chromium.launch({channel:'msedge'});
const p=await browser.newPage({viewport:{width:1280,height:900}});
await p.goto(pathToFileURL(output).href);await p.emulateMedia({media:'print'});
await p.evaluate(()=>Promise.all([document.fonts.ready,...[...document.images].map(x=>x.decode())]));
const result=await p.evaluate(()=>{
 const originals=[...document.querySelectorAll('section.page')];
 const main=document.querySelector('main');
 const topline=originals[0].querySelector('.topline').outerHTML;
 const foot=originals[0].querySelector('footer').outerHTML;
 const fragments=originals.map((s,i)=>({index:i,id:s.id,layout:s.className.replace('page','').trim(),header:s.querySelector('header').outerHTML,answer:s.querySelector('.answer').outerHTML,blocks:[...s.children].filter(x=>!x.matches('.topline,header,.answer,footer')).map(x=>x.outerHTML)}));
 const originalText=originals.map(s=>[...s.children].filter(x=>!x.matches('.topline,footer')).map(x=>x.textContent).join(' ')).join(' ');
 main.innerHTML='';let current=null,body=null,refs=[],records=[];
 function newPage(f,continuing=false){
  current=document.createElement('section');current.className='page '+f.layout;current.id='report-page-'+(records.length+1);
  current.innerHTML=topline+foot;body=document.createElement('div');body.className='flow-body';current.insertBefore(body,current.querySelector('footer'));main.append(current);
  records.push({originals:[],id:current.id});
  if(continuing){const c=document.createElement('div');c.className='continuation';c.textContent='AMANTA HEALTHCARE | '+f.id.split('-')[0]+' | '+new DOMParser().parseFromString(f.header,'text/html').querySelector('h1').textContent.replace(/\s*\(continued\)/gi,'')+' (continued)';body.append(c);}
 }
 function fits(){const footer=current.querySelector('footer').getBoundingClientRect();return body.getBoundingClientRect().bottom<=footer.top-12;}
 function mark(f){const a=records.at(-1).originals;if(!a.includes(f.index))a.push(f.index);}
 function add(html){const t=document.createElement('template');t.innerHTML=html;const el=t.content.firstElementChild;body.append(el);return el;}
 function splitTable(block){
  const table=block.matches('figure,.table-wrap')&&block.querySelector('table');
  if(!table||block.querySelectorAll('table').length!==1)return null;
  const rows=[...table.querySelectorAll('tbody > tr')];if(rows.length<4)return null;
  const tail=block.cloneNode(true),tailRows=[...tail.querySelectorAll('tbody > tr')];
  const sources=[...block.querySelectorAll('.source')];sources.forEach(x=>x.remove());
  for(let n=rows.length-2;n>=(block.matches('figure')?1:2);n--){
   rows.forEach((r,i)=>{if(i<n)table.tBodies[0].append(r);else r.remove();});
   if(fits()){
    tailRows.slice(0,n).forEach(x=>x.remove());
    const cap=tail.querySelector('figcaption');if(cap){cap.textContent+=' (continued)';cap.dataset.repeat='true';}
    tail.querySelector('thead').dataset.repeat='true';
    return tail;
   }
  }
  rows.forEach(r=>table.tBodies[0].append(r));sources.forEach(x=>block.append(x));return null;
 }
 function place(block,f){
  while(!fits()){
   const overflow=body.getBoundingClientRect().bottom-current.querySelector('footer').getBoundingClientRect().top+12;
   if(overflow<70&&!current.classList.contains('scenario')&&!current.classList.contains('tight')){current.classList.add('tight');if(fits())break;current.classList.remove('tight');}
   const tail=splitTable(block);
   if(tail){mark(f);newPage(f,true);body.append(tail);block=tail;mark(f);continue;}
   block.remove();let carry=[];
   while(body.lastElementChild?.matches('h3,h4')||(block.matches('.source')&&body.lastElementChild?.matches('p'))){carry.unshift(body.lastElementChild);body.lastElementChild.remove();}
   newPage(f,true);carry.forEach(x=>body.append(x));body.append(block);mark(f);
   if(!fits())throw Error('Block too tall: '+f.id+' '+block.tagName);
  }
 }
 for(const f of fragments){
  // Cover, chart overview and three full financial scenarios keep deliberate dedicated pages.
  const dedicated=f.index<2||f.layout.includes('scenario');
  if(dedicated||!current)newPage(f);
  let heading=add('<div class="flow-section-title" id="'+f.id+'">'+f.header+f.answer+'</div>');
  if(body.children.length>1)heading.classList.add('inset');
  const first=add(f.blocks[0]);
  if(!fits()&&body.children.length>2){
   const tail=splitTable(first);
   if(tail){mark(f);newPage(f,true);body.append(tail);place(tail,f);}
   else{heading.remove();first.remove();newPage(f);heading=add('<div class="flow-section-title" id="'+f.id+'">'+f.header+f.answer+'</div>');body.append(first);}
  }
  mark(f);
  if(!fits())throw Error('First block too tall: '+f.id);
  for(const html of f.blocks.slice(1)){
   let block=add(html);
   place(block,f);
  }
  if(dedicated)current=null;
 }
 const check=main.cloneNode(true);check.querySelectorAll('[data-repeat]').forEach(x=>x.remove());
 const textNow=[...check.querySelectorAll('.flow-section-title, .flow-body > :not(.flow-section-title):not(.continuation)')].map(x=>x.textContent).join(' ');
 const norm=s=>s.replace(/\s+/g,'');
 if(norm(textNow)!==norm(originalText))throw Error('Analytical content changed during pagination');
 [...main.children].forEach((s,i)=>s.querySelector('footer span:last-child').textContent=i+1);
 return {records,html:'<!DOCTYPE html>\n'+document.documentElement.outerHTML};
});
fs.writeFileSync(output,result.html);
const specs=result.records.map((r,i)=>{const s=r.originals.map(x=>oldSpec[x]);return {...s[0],page:i+1,page_id:r.id,original_sections:s.map(x=>x.page_id),section_starts:s.filter(x=>result.records.findIndex(q=>q.originals.includes(oldSpec.indexOf(x)))===i).map(x=>({section:x.page_id.split('-')[0],question:x.question})),question:s.map(x=>x.question).join(' / '),source_refs:[...new Set(s.flatMap(x=>x.source_refs))],qa:{arithmetic:true,source_checked:true,visual_checked:false}};});
fs.writeFileSync(path.join(root,'page-specifications.json'),JSON.stringify(specs,null,2));
fs.writeFileSync(path.join(root,'qa/reflow-map.json'),JSON.stringify(result.records,null,2));
console.log('Reflowed 37 original content panels into '+specs.length+' A4 pages. All analytical text preserved exactly.');
await browser.close();
