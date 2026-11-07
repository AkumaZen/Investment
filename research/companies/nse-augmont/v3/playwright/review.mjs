// Design review for the Augmont v3 report, using Playwright with the installed Edge.
// Run from this folder:  node review.mjs
// Output: ../qa/pw/<viewport>-pNN.png per page, and ../qa/pw/report.json with flagged issues.
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const html = path.resolve(here, '..', 'augmont-report.html');
const out = path.resolve(here, '..', 'qa', 'pw');
fs.mkdirSync(out, { recursive: true });

const viewports = [
  { name: 'desktop', width: 1280, height: 900 },
  { name: 'mobile', width: 390, height: 844, isMobile: true, deviceScaleFactor: 2 },
];
const MIN_TEXT_PX = 9; // rendered SVG text smaller than this is hard to read

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
      const sec = el.closest('section.page');
      const cap = el.closest('figure')?.querySelector('figcaption')?.textContent?.slice(0, 70);
      return `${sec ? sec.id : '?'}${cap ? ' | ' + cap : ''}`;
    };
    // sticky / fixed elements (the user wants none)
    for (const el of document.querySelectorAll('body *')) {
      const pos = getComputedStyle(el).position;
      if (pos === 'sticky' || pos === 'fixed') found.push({ type: 'sticky-or-fixed', where: where(el), detail: el.className });
    }
    // element wider than its container (excluding intentional table scrollers)
    for (const el of document.querySelectorAll('.inner *')) {
      if (el.closest('svg') || el.closest('.tw')) continue;
      const p = el.parentElement;
      const r = el.getBoundingClientRect(), pr = p.getBoundingClientRect();
      if (r.width > 0 && r.right > pr.right + 2 && getComputedStyle(p).overflowX === 'visible')
        found.push({ type: 'overflows-parent', where: where(el), detail: `${el.tagName}.${el.className} +${Math.round(r.right - pr.right)}px` });
    }
    // tables that need sideways scrolling
    for (const el of document.querySelectorAll('.tw'))
      if (el.scrollWidth > el.clientWidth + 1)
        found.push({ type: 'table-scrolls', where: where(el), detail: `${el.scrollWidth} > ${el.clientWidth}` });
    // SVG text: too small, clipped, or overlapping
    for (const svg of document.querySelectorAll('svg')) {
      const sr = svg.getBoundingClientRect();
      const texts = [...svg.querySelectorAll('text')].map(t => ({ t: t.textContent, r: t.getBoundingClientRect() }))
        .filter(x => x.t.trim() && x.r.width > 0);
      const small = texts.filter(x => x.r.height < MIN_TEXT_PX);
      if (small.length) found.push({ type: 'tiny-chart-text', where: where(svg),
        detail: `${small.length} labels < ${MIN_TEXT_PX}px tall (smallest ${Math.min(...small.map(x => x.r.height)).toFixed(1)}px), e.g. "${small[0].t}"` });
      for (const x of texts)
        if (x.r.left < sr.left - 1 || x.r.right > sr.right + 1 || x.r.top < sr.top - 1 || x.r.bottom > sr.bottom + 1)
          found.push({ type: 'chart-text-clipped', where: where(svg), detail: `"${x.t}"` });
      for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
        const a = texts[i].r, b = texts[j].r;
        const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        const oy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        if (ox > 1.5 && oy > 1.5)
          found.push({ type: 'chart-text-overlap', where: where(svg), detail: `"${texts[i].t}" x "${texts[j].t}"` });
      }
    }
    // body text that is too small to read comfortably
    for (const el of document.querySelectorAll('.inner p, .inner li, .inner td')) {
      const fs = parseFloat(getComputedStyle(el).fontSize);
      if (fs < 11) found.push({ type: 'tiny-body-text', where: where(el), detail: `${fs}px: ${el.textContent.slice(0, 50)}` });
    }
    return found;
  }, { MIN_TEXT_PX });

  const pages = await page.$$('section.page');
  for (let i = 0; i < pages.length; i++)
    await pages[i].screenshot({ path: path.join(out, `${vp.name}-p${String(i + 1).padStart(2, '0')}.png`) });
  report[vp.name] = { pages: pages.length, consoleErrors, issues };
  await ctx.close();
}
await browser.close();
fs.writeFileSync(path.join(out, 'report.json'), JSON.stringify(report, null, 1));
for (const [vp, r] of Object.entries(report)) {
  const counts = {};
  r.issues.forEach(i => { counts[i.type] = (counts[i.type] || 0) + 1; });
  console.log(vp, 'pages', r.pages, 'console errors', r.consoleErrors.length, JSON.stringify(counts));
}
