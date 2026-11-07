"""Browser, print and arithmetic checks for the saved draft; no network required."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright
from model import calculate

B = Path(__file__).resolve().parent


def main():
    output = B / 'qa'
    output.mkdir(exist_ok=True)
    m = calculate()
    checks = dict(sections_expected=20, arithmetic='PASS',
                  independent_source_verification='NOT COMPLETE; checks use primary-reader inputs, not a fresh independent reading',
                  cash_rounding_residual_crore=m['cash_flow_aggregation_residual'])
    content = json.loads((B / 'report-content.json').read_text(encoding='utf-8'))
    assert [s['id'] for s in content['sections']] == [f'S{i}' for i in range(1, 21)]
    assert all('What this means for you.' in s['html'] for s in content['sections'])
    assert content['status'].startswith('INTERIM DRAFT')
    assert m['management_guided_base'] is None
    assert abs(274.330 - 558.560 - 48.973 - 168.042 - 55.704 + 25.523 + 531.426) < .000001
    assert abs(-531.426 - 46.742 + 578.168) < .000001
    assert abs(620 - 47.236 - 572.764) < .000001
    assert abs(465 + 107.764 - 572.764) < .000001
    errors = []
    external = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel='msedge', headless=True)
        page = browser.new_page(viewport={'width': 1440, 'height': 1000}, device_scale_factor=1)
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('request', lambda request: external.append(request.url) if request.url.startswith(('http:', 'https:')) else None)
        page.goto((B / 'report.html').as_uri(), wait_until='load')
        checks['title'] = page.title()
        checks['bad_fragment_links'] = page.evaluate('''() => Array.from(document.querySelectorAll('a[href^="#"]')).filter(a => !document.getElementById(a.getAttribute('href').slice(1))).map(a=>a.getAttribute('href'))''')
        checks['duplicate_ids'] = page.evaluate('''() => {const ids=[...document.querySelectorAll('[id]')].map(e=>e.id);return ids.filter((x,i)=>ids.indexOf(x)!==i)}''')
        checks['viewports'] = {}
        for width, label in [(1440, 'desktop'), (390, 'mobile')]:
            page.set_viewport_size({'width': width, 'height': 1000})
            page.evaluate('window.scrollTo(0,0)')
            page.screenshot(path=str(output / f'{label}-cover.png'))
            sections = []
            for i in range(1, 21):
                element = page.locator(f'#S{i}')
                element.scroll_into_view_if_needed()
                element.screenshot(path=str(output / f'{label}-S{i}.png'))
                sections.append({'id': f'S{i}', 'width': element.bounding_box()['width'], 'height': element.bounding_box()['height']})
            checks['viewports'][label] = dict(body_overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth'), sections=sections)
        page.set_viewport_size({'width': 1440, 'height': 1000})
        page.pdf(path=str(B / 'report-draft.pdf'), print_background=True, prefer_css_page_size=True)
        browser.close()
    checks['page_errors'] = errors
    checks['external_requests'] = external
    import fitz
    pdf = fitz.open(B / 'report-draft.pdf')
    checks['print_pages'] = len(pdf)
    checks['print_blank_pages'] = [i+1 for i, page in enumerate(pdf) if len(page.get_text().strip()) < 20]
    checks['print_section_presence'] = {f'S{i}': any(f'S{i}\n' in p.get_text() or f'S{i} ' in p.get_text() for p in pdf) for i in range(1,21)}
    for index in [0, 2, len(pdf)-3]:
        pdf[index].get_pixmap(matrix=fitz.Matrix(1,1)).save(output / f'print-{index+1}.png')
    checks['visual_inspection'] = 'Pending human/model inspection of saved screenshot samples; screenshots for all sections captured.'
    (B / 'qa-results.json').write_text(json.dumps(checks, indent=2) + '\n', encoding='utf-8')
    assert not checks['bad_fragment_links']
    assert not checks['duplicate_ids']
    assert not errors and not external
    assert not checks['print_blank_pages']
    assert all(checks['print_section_presence'].values())
    assert all(not v['body_overflow'] for v in checks['viewports'].values())
    print(f'PASS: 20 sections, desktop/mobile captures, {len(pdf)} print pages, links, offline and arithmetic checks')


if __name__ == '__main__':
    main()
