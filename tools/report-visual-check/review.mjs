// Visual check for HTML research reports, using Playwright with the installed Edge (no browser download).
//
// Usage (from this folder, after `npm install` once):
//   node review.mjs <report.html> [outDir]
// outDir defaults to <report folder>/qa/pw. Keep it git-ignored.
//
// Output:
//   <outDir>/<desktop|mobile>-pNN.png   one screenshot per page (section.page), or a full-page shot if none
//   <outDir>/sheet-<desktop|mobile>-N.png  contact sheets (4 pages each) for the by-eye pass
//   <outDir>/report.json                 every flagged issue with page id and exhibit title
//
// The automated checks are a floor, not a pass. Always do the by-eye pass described in
// learnings/concepts/equity-report-quality-process.md, step "Visual verification".
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const htmlArg = process.argv[2];
if (!htmlArg) {
  console.error('usage: node review.mjs <report.html> [outDir]');
  process.exit(2);
}
const html = path.resolve(htmlArg);
const out = path.resolve(process.argv[3] || path.join(path.dirname(html), 'qa', 'pw'));
fs.mkdirSync(out, { recursive: true });

const viewports = [
  { name: 'desktop', width: 1280, height: 900 },
  { name: 'mobile', width: 390, height: 844, isMobile: true, deviceScaleFactor: 2 },
];
const MIN_TEXT_PX = 9; // rendered SVG text smaller than this is hard to read
const PER_SHEET = 4;

const browser = await chromium.launch({ channel: 'msedge' });
const report = {};
for (const vp of viewports) {
  const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height },
    isMobile: !!vp.isMobile, deviceScaleFactor: vp.deviceScaleFactor || 1 });
  const page = await ctx.newPage();
  const consoleErrors = [];
  page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text()); });
  page.on('pageerror', e => consoleErrors.push(String(e)));
  await page.goto(pathToFileURL(html).href);

  const issues = await page.evaluate(({ MIN_TEXT_PX }) => {
    const found = [];
    const doc = document.documentElement;
    if (doc.scrollWidth > window.innerWidth + 1)
      found.push({ type: 'page-horizontal-scroll', detail: `${doc.scrollWidth}px > ${window.innerWidth}px` });
    const where = el => {
      const sec = el.closest('section.page, section, article');
      const cap = el.closest('figure')?.querySelector('figcaption')?.textContent?.slice(0, 70);
      return `${sec && sec.id ? sec.id : '?'}${cap ? ' | ' + cap : ''}`;
    };
    const visible = r => r.width > 0 && r.height > 0;
    // sticky / fixed elements (reports should scroll as one document)
    for (const el of document.querySelectorAll('body *')) {
      const pos = getComputedStyle(el).position;
      if (pos === 'sticky' || pos === 'fixed') found.push({ type: 'sticky-or-fixed', where: where(el), detail: String(el.className) });
    }
    // element wider than its container (excluding intentional table scrollers)
    for (const el of document.querySelectorAll('body *')) {
      if (el.closest('svg') || el.closest('.tw')) continue;
      const p = el.parentElement;
      if (!p || p === document.body) continue;
      const r = el.getBoundingClientRect(), pr = p.getBoundingClientRect();
      if (r.width > 0 && r.right > pr.right + 2 && getComputedStyle(p).overflowX === 'visible')
        found.push({ type: 'overflows-parent', where: where(el), detail: `${el.tagName}.${el.className} +${Math.round(r.right - pr.right)}px` });
    }
    // tables that need sideways scrolling
    for (const el of document.querySelectorAll('.tw, .table-wrap'))
      if (el.scrollWidth > el.clientWidth + 1)
        found.push({ type: 'table-scrolls', where: where(el), detail: `${el.scrollWidth} > ${el.clientWidth}` });
    // SVG charts
    for (const svg of document.querySelectorAll('svg')) {
      const sr = svg.getBoundingClientRect();
      if (!visible(sr)) continue;
      const texts = [...svg.querySelectorAll('text')].map(t => ({ t: t.textContent, r: t.getBoundingClientRect() }))
        .filter(x => x.t.trim() && visible(x.r));
      const small = texts.filter(x => x.r.height < MIN_TEXT_PX);
      if (small.length) found.push({ type: 'tiny-chart-text', where: where(svg),
        detail: `${small.length} labels < ${MIN_TEXT_PX}px tall (smallest ${Math.min(...small.map(x => x.r.height)).toFixed(1)}px), e.g. "${small[0].t}"` });
      for (const x of texts)
        if (x.r.left < sr.left - 1 || x.r.right > sr.right + 1 || x.r.top < sr.top - 1 || x.r.bottom > sr.bottom + 1)
          found.push({ type: 'chart-text-clipped', where: where(svg), detail: `"${x.t}"` });
      // text on text
      for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
        const a = texts[i].r, b = texts[j].r;
        const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        const oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        if (ox > 1.5 && oy > 1.5)
          found.push({ type: 'chart-text-overlap', where: where(svg), detail: `"${texts[i].t}" x "${texts[j].t}"` });
      }
      // text on a neighbouring bar: a label that spills onto a bar it does not belong to
      // (its centre lies outside that bar's x-range). Labels drawn inside their own bar are fine.
      const bars = [...svg.querySelectorAll('rect')].map(r => r.getBoundingClientRect())
        .filter(r => visible(r) && r.width < sr.width * 0.5 && r.width > 3 && r.height > 3);
      for (const x of texts) {
        const cx = (x.r.left + x.r.right) / 2;
        for (const b of bars) {
          if (cx >= b.left && cx <= b.right) continue;
          const ox = Math.min(x.r.right, b.right) - Math.max(x.r.left, b.left);
          const oy = Math.min(x.r.bottom, b.bottom) - Math.max(x.r.top, b.top);
          if (ox > 2 && oy > 3) {
            found.push({ type: 'chart-text-on-bar', where: where(svg), detail: `"${x.t}" spills ${ox.toFixed(0)}px onto a neighbouring bar` });
            break;
          }
        }
      }
    }
    // body text that is too small to read comfortably
    for (const el of document.querySelectorAll('p, li, td')) {
      if (!visible(el.getBoundingClientRect())) continue;
      const fs = parseFloat(getComputedStyle(el).fontSize);
      if (fs < 11) found.push({ type: 'tiny-body-text', where: where(el), detail: `${fs}px: ${el.textContent.slice(0, 50)}` });
    }
    // em dash (house style: plain hyphen only)
    if (document.body.innerText.includes('—')) found.push({ type: 'em-dash', detail: 'found in visible text' });
    return found;
  }, { MIN_TEXT_PX });

  let pages = await page.$$('section.page');
  const shots = [];
  if (!pages.length) {
    const f = path.join(out, `${vp.name}-p01.png`);
    await page.screenshot({ path: f, fullPage: true });
    shots.push(f);
  }
  for (let i = 0; i < pages.length; i++) {
    const f = path.join(out, `${vp.name}-p${String(i + 1).padStart(2, '0')}.png`);
    await pages[i].screenshot({ path: f });
    shots.push(f);
  }
  report[vp.name] = { pages: shots.length, consoleErrors, issues };
  await ctx.close();

  // contact sheets: PER_SHEET pages side by side, for a quick layout pass
  const sheetCtx = await browser.newContext({ viewport: { width: vp.name === 'mobile' ? 1600 : 2400, height: 900 } });
  const sp = await sheetCtx.newPage();
  for (let s = 0; s * PER_SHEET < shots.length; s++) {
    const group = shots.slice(s * PER_SHEET, (s + 1) * PER_SHEET);
    const cells = group.map(f => `<figure><figcaption>${path.basename(f)}</figcaption><img src="${path.basename(f)}"></figure>`).join('');
    // written next to the screenshots so relative image paths load (setContent pages cannot read file:// images)
    const sheetHtml = path.join(out, `_sheet-${vp.name}.html`);
    fs.writeFileSync(sheetHtml, `<!doctype html><style>body{margin:0;background:#ddd;font:14px sans-serif}
      .g{display:grid;grid-template-columns:repeat(${PER_SHEET},1fr);gap:10px;padding:10px;align-items:start}
      figure{margin:0;background:#fff}figcaption{padding:4px}img{width:100%;display:block}</style>
      <div class="g">${cells}</div>`);
    await sp.goto(pathToFileURL(sheetHtml).href, { waitUntil: 'load' });
    fs.rmSync(sheetHtml);
    await sp.screenshot({ path: path.join(out, `sheet-${vp.name}-${s + 1}.png`), fullPage: true });
  }
  await sheetCtx.close();
}
await browser.close();
fs.writeFileSync(path.join(out, 'report.json'), JSON.stringify(report, null, 1));
let total = 0;
for (const [vp, r] of Object.entries(report)) {
  const counts = {};
  r.issues.forEach(i => { counts[i.type] = (counts[i.type] || 0) + 1; });
  total += r.issues.length + r.consoleErrors.length;
  console.log(vp, 'pages', r.pages, 'console errors', r.consoleErrors.length, JSON.stringify(counts));
}
console.log(total ? `FLAGGED ${total} - see ${path.join(out, 'report.json')}` : 'automated checks clean - now do the by-eye pass');
process.exitCode = total ? 1 : 0;
