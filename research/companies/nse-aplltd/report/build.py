"""Build the Alembic Pharmaceuticals quick-analysis report (single self-contained HTML).

Run:  python -I -X utf8 report/build.py      (from the company folder)
Out:  report/report.html, report/chart-data.json

Rs crore unless stated. Valuation numbers come from ../model/valuation.json (model/valuation.py).
Derived numbers are computed here and tied back to filed totals with asserts.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import charts as C  # noqa: E402

VAL = json.load(open(os.path.join(HERE, "..", "model", "valuation.json"), encoding="utf-8"))
DEC = VAL["decomposition"]
CROSS = VAL["cross"]
SC = {k: VAL["scenarios"][k] for k in ("Bear", "Base", "Bull")}


def _responsive(fn):
    """Charts wider than a phone get a second, phone-sized drawing swapped in by CSS at 820px."""
    def wrap(*a, **kw):
        w = kw.get("w", 520)
        if w < 420:
            return fn(*a, **kw)
        mk = dict(kw, w=360)
        if kw.get("h"):
            mk["h"] = int(kw["h"] * 1.05)
        return f'<div class="cw-d">{fn(*a, **kw)}</div><div class="cw-m">{fn(*a, **mk)}</div>'
    return wrap


for _n in ("bars", "grouped", "lines", "hbars", "value_range", "stacked"):
    setattr(C, _n, _responsive(getattr(C, _n)))

# ---------------------------------------------------------------- sources
BSE = "https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname={}.pdf"
SRC = {
    "q2c": ("Q2 FY27 call transcript, 4 Nov 2026", BSE.format("5991f5bd-f70d-4eb3-bd32-07b794edf376")),
    "q2d": ("Q2 FY27 investor presentation, 4 Nov 2026", BSE.format("f6ef52d7-552d-47ae-adce-c82ce091ad53")),
    "q1c": ("Q1 FY27 call transcript, 4 Aug 2026", BSE.format("b8f27d1b-f644-4885-a463-793dbbfce7ca")),
    "q1d": ("Q1 FY27 investor presentation, Aug 2026", BSE.format("d85cc438-3429-4b83-a89a-b1afb9824454")),
    "q4c": ("Q4 FY26 call transcript, 15 May 2026", BSE.format("1e5987cb-3bd7-4832-852e-ec765d86c045")),
    "q4d": ("Q4 FY26 investor presentation, May 2026", BSE.format("7304396a-752a-453f-9789-5d41d3d422c0")),
    "q3c": ("Q3 FY26 call transcript, 5 Feb 2026", BSE.format("7eca3970-89d2-42e5-ba67-8ab7bc7e1dc9")),
    "q3d": ("Q3 FY26 investor presentation, Feb 2026", BSE.format("46c93f24-1700-455c-b9cd-ab997c99dfbc")),
    "a1": ("USFDA approval, Olopatadine 0.7% OTC, 4 Nov 2026", BSE.format("e3ffd3f1-dc5f-4bd1-92a9-9de2c85a2380")),
    "a2": ("Trade report on the expanded DifGen collaboration, 5 Nov 2026",
           "https://www.indianpharmapost.com/news/alembic-pharma-expands-us-complex-generics-portfolio-via-difgen-partnership-22328"),
    "a3": ("Company press release, Binimetinib tentative approval, 19 Jun 2026",
           "https://alembicpharmaceuticals.com/webfiles/pdf/Investor/notices/2026-2027/Press-Release-Binimetinib-Tablets-45-mg.pdf"),
    "a4": ("Company press release, Dapagliflozin approval, 7 Apr 2026",
           "https://alembicpharmaceuticals.com/webfiles/pdf/Investor/notices/2026-2027/press-release-dapagliflozin-tablets-5mg-and-10mg.pdf"),
    "scr": ("Screener consolidated financials, fetched 10 Nov 2026", "https://www.screener.in/company/APLLTD/consolidated/"),
    "model": ("Our model, model/valuation.py and valuation.md [E]", None),
}


def src(*items):
    """items: key or (key, page). Physical PDF page numbers, so #page= opens the right page."""
    parts = []
    for it in items:
        key, pg = (it, None) if isinstance(it, str) else it
        name, url = SRC[key]
        label = name + (f", p.{pg}" if pg else "")
        if url:
            first = str(pg).split("-")[0].split(",")[0] if pg else ""
            u = url + (f"#page={first}" if pg and first.isdigit() else "")
            parts.append(f'<a href="{u}">{label}</a>')
        else:
            parts.append(label)
    return "Source: " + "; ".join(parts) + "."


# ---------------------------------------------------------------- data (facts.md)
D = {
    "price": 1017.0, "mcap": 19996.0, "shares": VAL["shares_cr"], "net_debt": 1236.0, "promoter": 69.87,
    "years": ["FY22", "FY23", "FY24", "FY25", "FY26", "TTM"],
    "sales_y": [5306, 5653, 6229, 6672, 7345, 8477],
    "op_y": [874, 682, 932, 1008, 1121, 1413],
    "pat_y": [521, 342, 616, 582, 671, 840],
    "cfo_y": [552, 724, 803, 88, 783],
    "quarters": ["Dec24", "Mar25", "Jun25", "Sep25", "Dec25", "Mar26", "Jun26", "Sep26"],
    "sales_q": [1693, 1770, 1711, 1910, 1876, 1848, 2150, 2603],
    "op_q": [260, 271, 281, 316, 292, 228, 332, 562],
    "seg": ["India", "US", "Ex-US", "API"],
    "seg_h1_26": [12.38, 10.89, 7.19, 5.75], "seg_h1_27": [13.67, 17.81, 8.23, 7.82],
    "seg_q2_26": [6.39, 5.66, 3.92, 3.14], "seg_q2_27": [7.25, 10.03, 4.40, 4.36],
    "seg_fy22": [19.26, 16.66, 7.75, 9.39], "seg_fy26": [24.58, 22.06, 14.94, 11.87],
    "ah_fy22": 2.32, "ah_fy26": 5.19,
}
CALC = {}


def calc():
    c = CALC
    assert abs(sum(D["seg_h1_27"]) - 47.53) < 0.02 and abs(sum(D["seg_h1_26"]) - 36.21) < 0.02
    assert abs(sum(D["seg_q2_27"]) - 26.03) < 0.02 and abs(sum(D["seg_q2_26"]) - 19.10) < 0.02
    c["opm_q"] = [o / s * 100 for o, s in zip(D["op_q"], D["sales_q"])]
    c["opm_y"] = [o / s * 100 for o, s in zip(D["op_y"], D["sales_y"])]
    c["seg_h1_g"] = [b / a - 1 for a, b in zip(D["seg_h1_26"], D["seg_h1_27"])]
    c["h1_g"] = 47.53 / 36.21 - 1
    c["q2_g"] = D["sales_q"][-1] / D["sales_q"][3] - 1
    c["cagr_22_26"] = (D["sales_y"][4] / D["sales_y"][0]) ** 0.25 - 1
    c["seg_cagr"] = [(b / a) ** 0.25 - 1 for a, b in zip(D["seg_fy22"], D["seg_fy26"])]
    c["ah_cagr"] = (D["ah_fy26"] / D["ah_fy22"]) ** 0.25 - 1
    launch = DEC["q2_us_launch_bn"] * 100
    c["launch_cr"] = launch
    c["yoy_add"] = D["sales_q"][-1] - D["sales_q"][3]
    c["launch_share_of_add"] = launch / c["yoy_add"]
    c["q2_ex_launch_g"] = (D["sales_q"][-1] - launch) / D["sales_q"][3] - 1
    c["launch_ebitda_mid"] = (DEC["q2_launch_ebitda_lo"] + DEC["q2_launch_ebitda_hi"]) / 2
    c["launch_ebitda_share"] = c["launch_ebitda_mid"] / DEC["q2_ebitda_company"]
    c["us_fy_g"] = D["seg_fy26"][1] / 19.57 - 1
    c["cfo_conv"] = [cf / op for cf, op in zip(D["cfo_y"], D["op_y"][:5])]
    assert abs(c["q2_g"] - 0.363) < 0.005
    return c


calc()


def f0(v):
    return f"{v:,.0f}"


def pc(v, dec=0, sign=False):
    return f"{v * 100:{'+' if sign else ''}.{dec}f}%"


# ---------------------------------------------------------------- page helpers
SECTIONS = []
EX = [0]


def exhibit(title, svg, source, note=None):
    EX[0] += 1
    n = f'<p class="xnote">{note}</p>' if note else ""
    return (f'<figure class="ex"><figcaption>Exhibit {EX[0]}: {title}</figcaption>{svg}{n}'
            f'<p class="src">{source}</p></figure>')


def duo(a, b):
    return f'<div class="duo">{a}{b}</div>'


def table(head, rows, cls="", caption=None, source=None):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = []
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            klass = "l" if i == 0 else "r"
            if isinstance(c, tuple):
                c, extra = c
                klass += " " + extra
            cells.append(f'<td class="{klass}">{c}</td>')
        tr.append("<tr>" + "".join(cells) + "</tr>")
    t = f'<div class="tw"><table class="t {cls}"><thead><tr>{th}</tr></thead><tbody>{"".join(tr)}</tbody></table></div>'
    if caption:
        EX[0] += 1
        s = f'<p class="src">{source}</p>' if source else ""
        return f'<figure class="ex tbl"><figcaption>Exhibit {EX[0]}: {caption}</figcaption>{t}{s}</figure>'
    return t


def chip(word):
    cls = {"OK": "ok", "MET": "ok", "BEAT": "ok", "WATCH": "watch", "LATE": "watch", "RAISED": "open",
           "RED": "red", "MISSED": "red", "OPEN": "open", "STRUCTURAL": "ok", "ONE-OFF": "watch", "MIXED": "open"}.get(word, "open")
    return f'<span class="chip {cls}">{word}</span>'


def section(sid, short, kicker, headline, answer, body, means):
    html = (f'<p class="answer">{answer}</p>{body}'
            f'<h4 class="mfy">What this means for you</h4><p class="means">{means}</p>')
    SECTIONS.append((sid, short, kicker, headline, html))


def ul(items, cls=""):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def flow(cols):
    out = []
    for i, (h, boxes, gold) in enumerate(cols):
        if i:
            out.append('<div class="farrow" aria-hidden="true">&#8594;</div>')
        bx = "".join(f'<div class="fb{" gold" if gold else ""}">{b}</div>' for b in boxes)
        out.append(f'<div class="fcol"><p class="fh">{h}</p>{bx}</div>')
    return f'<div class="flow">{"".join(out)}</div>'


def quote(text, cite):
    return f'<blockquote class="q"><p>"{text}"</p><cite>{cite}</cite></blockquote>'


B = {k: SC[k]["table"]["proj"] for k in SC}   # projected rows per scenario
TP29 = {k: B[k][2]["tp"] for k in B}
TP28 = {k: B[k][1]["tp"] for k in B}

# ================================================================ S1 snapshot and verdict
rail = f"""<div class="rail">
<div class="verdict"><p class="rk">Our answer</p><p class="rv">Partly structural</p>
<p class="rs">The base business is growing faster than before. The margin jump is mostly the one-off launch block.</p></div>
<div class="rbox"><p class="rh">Key data, 10 Nov 2026</p>
{table(["", ""], [["Price", "Rs 1,017"], ["Market cap", "Rs 19,996 cr"], ["Shares [E]", f"{D['shares']:.2f} cr"],
                   ["P/E, trailing", f"{CROSS['pe_ttm']:.1f}x"], ["EV / trailing EBITDA", f"{CROSS['ev_ttm_ebitda']:.1f}x"],
                   ["Net debt, Sep 2026", "Rs 1,236 cr"], ["Promoter holding", "69.87%"], ["52-week range", "Rs 635 to 1,056"]], "kv")}</div>
<div class="rbox"><p class="rh">FY29 value per share [E]</p>
{table(["", ""], [["Bear", f"Rs {f0(TP29['Bear'])}"], ["Base", f"Rs {f0(TP29['Base'])}"], ["Bull", f"Rs {f0(TP29['Bull'])}"]], "kv")}
<p class="tiny">22x FY29 EPS, at 31 Mar 2029, not discounted. No rating is given.</p></div></div>"""

s1_main = f"""<p class="lede">Alembic's revenue jumped {pc(CALC['q2_g'])} in Q2 FY27 and its operating margin hit 22%.
For five years before that, sales grew about {pc(CALC['cagr_22_26'], 1)} a year and the margin sat between 12% and 16%.
This report answers one question: is that jump the new normal, or a one-time boost?</p>
<h3>The short answer</h3>
{ul([
    f"<b>Structural, a little over half of the growth.</b> Strip out the launch block and Q2 revenue still grew about {pc(CALC['q2_ex_launch_g'])}. "
    "Management says the US base portfolio grew 23% without new launches, and the US base now runs at about $75m a quarter, against $60m to $65m before.",
    f"<b>One-off, most of the margin.</b> About Rs {f0(CALC['launch_cr'])} cr of Q2 US sales sits above the base path [E]. "
    f"We estimate it earned about Rs {f0(DEC['q2_launch_ebitda_lo'])} to {f0(DEC['q2_launch_ebitda_hi'])} cr of EBITDA, roughly a third of the quarter's total. "
    f"Without it, the Q2 margin is about {pc(DEC['q2_margin_ex_launch_mid'], 1)}, no better than a year ago.",
    "<b>The key launch, bosutinib, loses its 180-day exclusivity in late November 2026.</b> Management itself says it does not know what happens after that.",
    "<b>What can make the margin step-up stick:</b> the US branded business stops losing money in FY28 (worth 150 to 200 bp), the new plants fill up, "
    "and first-to-file launches such as dapagliflozin and binimetinib arrive. These are disclosed plans, not results yet.",
])}
<p>Our working view: a sustainable margin of about 18% to 20%, not 22%.
The price of Rs 1,017 is 22x the earnings per share our base case expects for FY27, a year that includes the exclusivity boost.
So the stock already pays for guidance being met.</p>"""
section("s1", "Snapshot and verdict", "Summary", "A real step-up in the base, a temporary boost in the margin",
        "The base business has moved up a gear, but most of the record Q2 margin comes from a launch whose exclusivity ends this month.",
        f'<div class="cover"><div>{s1_main}</div>{rail}</div>'
        + exhibit("Sales grew 36% in Q2 FY27, well above the trend of the previous eight quarters",
                  C.bars(D["quarters"], D["sales_q"], "Quarterly sales, Rs crore", highlight={7}, w=720, h=230,
                         notes={7: "+36% YoY"}),
                  src("scr"), "Rs crore, consolidated. Q2 FY27 (Sep26) shown in indigo."),
        "Treat the Q2 FY27 numbers as a peak, not a run rate. Watch the Q3 FY27 results (due February 2027) for how fast bosutinib sales fall and whether the base keeps growing above 20%.")

# ================================================================ S2 quarter and segments
s2 = duo(
    exhibit("Operating margin hit 22% in Q2 FY27, after 12% to 17% for two years",
            C.lines(D["quarters"], [("OPM, Screener basis", CALC["opm_q"], C.PRIMARY, False)], "Quarterly operating margin, %",
                    unit="%", ymin=0, ymax=25, grid=5, all_labels=True, end_labels=False, w=520, h=240),
            src("scr"), "Screener's operating profit runs about Rs 16 cr a quarter below company EBITDA (22.2% in Q2 on the company's basis)."),
    exhibit("The US drove the first half; India grew at about 10%",
            C.grouped(D["seg"], [("H1 FY26", D["seg_h1_26"], C.GREY), ("H1 FY27", D["seg_h1_27"], C.PRIMARY)],
                      "Segment revenue H1 FY26 vs H1 FY27, Rs bn", dec=1, w=520, h=240),
            src(("q2d", 5)), "Rs billion. Growth: " + ", ".join(f"{s} {pc(g, 0, True)}" for s, g in zip(D["seg"], CALC["seg_h1_g"])) + "."))
seg_tbl = table(["Segment, Rs bn", "Q2 FY26", "Q2 FY27", "Growth", "H1 FY26", "H1 FY27", "Growth"],
                [[s, f"{a:.2f}", f"{b:.2f}", pc(b / a - 1, 0, True), f"{c:.2f}", f"{d:.2f}", pc(d / c - 1, 0, True)]
                 for s, a, b, c, d in zip(D["seg"], D["seg_q2_26"], D["seg_q2_27"], D["seg_h1_26"], D["seg_h1_27"])]
                + [[("Total", "bold"), "19.10", "26.03", (pc(26.03 / 19.10 - 1, 0, True), "bold"), "36.21", "47.53", (pc(CALC["h1_g"], 0, True), "bold")]],
                "fin", caption="Segment revenue: US nearly doubled in Q2, API up 39%", source=src(("q2d", 5)))
section("s2", "The quarter", "What happened", "One segment, the US, did most of the work",
        f"Q2 FY27 revenue was Rs 2,603 cr, up {pc(CALC['q2_g'])}, and the US alone added Rs 437 cr of the Rs 693 cr increase.",
        s2 + seg_tbl + ul([
            "US sales rose 77% in Q2 (72% for US generics alone), helped by the bosutinib launch in June 2026 and a weaker rupee.",
            "API (bulk drug sales to other drug makers) grew 39%. Management guides at least high-teens growth for the year, so part of this is lumpy order timing.",
            "India grew 14% in Q2: human health 11%, animal health 23%. That is the best India quarter in this set, after 5% to 7% for most of FY26.",
            "Ex-US markets (Europe, Canada, Australia and others) grew 12%, in line with their mid-teens trend.",
        ]),
        "The quarter's strength is concentrated in the US. Any view on Alembic now rests on what the US looks like once the launch boost fades.")

# ================================================================ S3 structural or one-off
us_split = C.stacked(["Q2 FY26", "Q1 FY27", "Q2 FY27"],
                     [("Base path [E]", [5.66, DEC["q1_us_base_bn"], DEC["q2_us_base_bn"]], C.PRIMARY),
                      ("Launch block, mostly bosutinib [E]", [0, DEC["q1_us_launch_bn"], DEC["q2_us_launch_bn"]], C.SECOND)],
                     "US revenue split into base path and launch block, Rs bn", dec=2, w=520, h=260,
                     hatch_series={"Launch block, mostly bosutinib [E]"})
margin_split = C.hbars(["Q2 FY26, whole company", "Q2 FY27, whole company", "Q2 FY27, without launch block [E]", "Launch block alone [E]"],
                       [17.0, 22.2, DEC["q2_margin_ex_launch_mid"] * 100, (DEC["q2_launch_margin_lo"] + DEC["q2_launch_margin_hi"]) / 2 * 100],
                       "EBITDA margin with and without the launch block, %", dec=1, unit="%", w=520, lab_w=200,
                       colors=[C.GREY, C.PRIMARY, C.PRIMARY, C.SECOND])
calc_tbl = table(["Step", "Working", "Result"], [
    ["1. US base path, Q2 FY27", "Q2 FY26 US Rs 5.66 bn x (1 + 23% base growth, call p6)", f"Rs {DEC['q2_us_base_bn']:.2f} bn"],
    ["2. Launch block", f"Q2 FY27 US Rs 10.03 bn minus step 1", f"Rs {DEC['q2_us_launch_bn']:.2f} bn ({pc(DEC['q2_launch_share_of_group'], 1)} of group sales)"],
    ["3. EBITDA of everything else", f"Rs {f0(DEC['q2_rest_sales'])} cr at the pre-exclusivity 16% to 17% (call p14)", f"Rs {f0(DEC['q2_rest_ebitda_lo'])} to {f0(DEC['q2_rest_ebitda_hi'])} cr"],
    ["4. EBITDA of the launch block", f"Company Q2 EBITDA Rs {f0(DEC['q2_ebitda_company'])} cr minus step 3", f"Rs {f0(DEC['q2_launch_ebitda_lo'])} to {f0(DEC['q2_launch_ebitda_hi'])} cr ({pc(DEC['q2_launch_margin_lo'])} to {pc(DEC['q2_launch_margin_hi'])} margin)"],
    ["5. Q1 FY27 FX effect on US growth", "49% reported minus 37% to 38% constant currency (Q1 call)", f"about {pc(DEC['q1_fx_points'], 0)} points"],
], "std", caption="How we split the quarter [E]", source=src(("q2c", 6), ("q2c", 14), ("q2d", 5), ("q1c", 14), "model"))
chain = flow([
    ("Launches", ["30+ US launches in 18 months, a quarter of them first-to-file or day-1 <small>Q2 call p4</small>"], False),
    ("Share and price", ["Exclusivity gives high prices for 180 days, then competitors enter <small>Q1 call p8: erosion will be 'quite drastic'</small>"], True),
    ("Base holds?", ["<b>First unproven link:</b> the base keeps growing about 20%+ after bosutinib fades <small>tested in Q3 and Q4 FY27</small>"], True),
    ("Plants fill", ["New oncology, injectable and ophthalmic lines were at 40% to 60% use <small>Q4 FY26 call</small>"], False),
    ("Margin", ["Branded drag of 150 to 200 bp ends in FY28; aim is 'closer to 20%' <small>Q2 call p11, p14</small>"], False),
])
tests = table(["Test", "Evidence", "Reads as"], [
    ["Did the base grow faster than history?", "US base +23% in Q2 and mid-20s in Q1 vs a 7% FY22 to FY26 US CAGR; US run rate $60m to $65m, now about $75m", chip("STRUCTURAL")],
    ["How much is currency?", "About 11 to 12 points of Q1 US growth was the weaker rupee; Q2 split not disclosed", chip("ONE-OFF")],
    ["Did margin rise without the launch?", f"Ex-launch Q2 margin about {pc(DEC['q2_margin_ex_launch_mid'], 1)} vs 17% a year ago [E]", chip("ONE-OFF")],
    ["Incremental margin", f"Q2 EBITDA rose Rs 246 cr on Rs 693 cr more sales: {pc(DEC['q2_incremental_margin'])} (Screener basis)", chip("MIXED")],
    ["Does guidance assume it lasts?", "FY27 guide 'incorporates the expected normalization of exclusivity-led sales'; implies H2 7% to 15% below H1", chip("ONE-OFF")],
    ["Is there a pipeline to replace it?", "Dapagliflozin shared exclusivity, binimetinib sole FTF, DifGen complex generics from FY28", chip("MIXED")],
    ["Are fixed costs now covered?", "Capex cycle 'behind us'; plants were under-used; branded loss ends FY28", chip("STRUCTURAL")],
], "std", caption="Seven tests of structural vs one-off", source=src(("q2c", 5), ("q2c", 6), ("q1c", 8), ("q1c", 14), "q4c", "model"))
section("s3", "Structural or one-off?", "The core question", "The growth is mostly real; the margin is mostly the launch",
        f"About {pc(1 - CALC['launch_share_of_add'])} of the Q2 sales increase came from the base business, but about {pc(CALC['launch_ebitda_share'])} of Q2 EBITDA came from the launch block [E].",
        duo(exhibit("About Rs 307 cr of Q2 US sales sits above a 23% base growth path [E]", us_split,
                    src(("q2d", 5), ("q2c", 6), "model"), "Base path = last year's US sales grown at the base growth management disclosed. The amber block is everything above it, mostly bosutinib."),
            exhibit("Without the launch block, the Q2 margin is about where it was a year ago [E]", margin_split,
                    src(("q2c", 5), ("q2c", 14), "model"), "Mid-points of the ranges in Exhibit 6. Company EBITDA basis."))
        + calc_tbl + "<h3>The chain that has to hold</h3>" + chain + tests
        + quote("If you take the new launches out, so the base portfolio grew by 23% in the quarter.", 'Management, Q2 FY27 call, p6')
        + "<p class=\"small\">Limits of this split: the company does not disclose bosutinib revenue, and the 23% base growth includes some currency gain. The launch block also holds a few smaller H1 launches. Treat the split as a range, not a reported number.</p>",
        "Do not extrapolate the 22% margin. The part that looks structural is base growth in the high teens to low twenties and a margin that can reach 18% to 20% if the branded loss ends on schedule.")

# ================================================================ S4 business in five years
s4 = duo(
    exhibit("Five years of mid-single-digit growth before FY27",
            C.bars(D["years"], D["sales_y"], "Annual sales, Rs crore", highlight={5}, w=520, h=230),
            src("scr"), f"TTM = 12 months to Sep 2026. FY22 to FY26 CAGR {pc(CALC['cagr_22_26'], 1)}."),
    exhibit("Margin sat at 12% to 16% for five years; FY23 shows how fast it can fall",
            C.lines(D["years"], [("OPM", CALC["opm_y"], C.PRIMARY, False)], "Annual operating margin, %", unit="%",
                    ymin=0, ymax=20, grid=4, all_labels=True, end_labels=False, w=520, h=230),
            src("scr"), "FY23: US price erosion took the margin to 12%."))
cfo = exhibit("Cash flow did not always follow profit: FY25 cash from operations was Rs 88 cr",
              C.grouped(D["years"][:5], [("EBITDA", D["op_y"][:5], C.GREY), ("Cash from operations", D["cfo_y"], C.PRIMARY)],
                        "EBITDA vs cash from operations, Rs crore", w=720, h=230),
              src("scr"), "FY25 working capital rose sharply; Q2 FY27 call p6 says new US launches again lengthen collection cycles.")
seg_cagr = table(["Segment", "FY22, Rs bn", "FY26, Rs bn", "4-year CAGR", "How it earns"], [
    ["India branded", "19.26", "24.58", pc(CALC["seg_cagr"][0], 0), "5,800+ reps detail doctors; rank 20, 1.1% share"],
    ["of which Animal Health", "2.32", "5.19", pc(CALC["ah_cagr"], 0), "Fastest grower inside India"],
    ["US generics and branded", "16.66", "22.06", pc(CALC["seg_cagr"][1], 0), "ANDA approvals and launches; prices erode as rivals enter"],
    ["Ex-US", "7.75", "14.94", pc(CALC["seg_cagr"][2], 0), "Partner-led in Europe, Canada, Australia"],
    ["API", "9.39", "11.87", pc(CALC["seg_cagr"][3], 0), "Bulk drug sales; order timing is lumpy"],
], "std", caption="Segments over FY22 to FY26", source=src("q2d"))
section("s4", "Business and history", "Context", "A steady, slow grower that has just spent heavily on new plants",
        "Before FY27, Alembic grew sales about 8.5% a year with a 12% to 16% margin; the new plants built in that period are what FY27 is starting to use.",
        s4 + seg_cagr + cfo + ul([
            "R&D fell from 15.8% of sales in FY22 to 7.6% in FY24 and was 9.6% in FY26; US filings fell from 23 in FY22 to 8 in FY25 and 10 in FY26. In our view, the lower filing years limit launches from FY29 onward.",
            "Cumulative: 283 US filings, 245 approvals and 188 products launched [Q2 deck].",
            "Promoters own 69.87%, steady, with no pledge shown on Screener.",
        ]),
        "History argues for caution on any long-term margin above 20%. The new element is capacity that was idle and is now filling.")

# ================================================================ S5 pipeline and announcements
ann = table(["Date", "Announcement", "Why it matters", "Structural or one-off"], [
    ["4 Nov 2026", "USFDA final approval, Olopatadine 0.7% ophthalmic, OTC", "Uses the ophthalmic line that was 'chock-a-block'; OTC eye drops are a steady, smaller product", chip("STRUCTURAL")],
    ["5 Nov 2026", "Expanded DifGen collaboration, 20+ US complex generics", "Patches, complex injectables and ophthalmics on a profit share; revenue from FY28", chip("STRUCTURAL")],
    ["19 Jun 2026", "Tentative approval, Binimetinib 45 mg; sole first Paragraph IV filer", "May earn 180-day exclusivity after final approval; US market about $259m", chip("ONE-OFF")],
    ["7 Apr 2026", "Final approval, Dapagliflozin 5/10 mg; 180-day shared exclusivity", "US market about $10.5 bn, but shared exclusivity and launch timing not disclosed", chip("ONE-OFF")],
], "std", caption="The four announcements in scope",
    source=src(("a1", 2), "a2", "a3", "a4", ("q2c", 12)))
cycle = flow([
    ("File", ["ANDA filed; first filer may get 180-day exclusivity"], False),
    ("Approve", ["USFDA approval; tentative if patents still block"], False),
    ("Exclusivity", ["180 days with one or a few sellers: high price"], True),
    ("Entry", ["Competitors launch; price falls fast"], True),
    ("Base", ["Product joins the base at a much lower price"], False),
])
section("s5", "Pipeline and announcements", "What is coming", "The pipeline offers more exclusivity windows, each one temporary",
        "Two of the four announcements add lasting capacity use (Olopatadine, DifGen); two are first-to-file chances that, like bosutinib, would be large but temporary.",
        exhibit("How a US generic earns over its life", cycle, src(("q1c", 8)), "Amber steps are the one-off phase.")
        + ann + ul([
            "Management guides more than 30 US launches over 18 months, about a quarter first-to-file or shared day-1 [Q2 call p4, p12].",
            "A steady flow of exclusivity windows can make one-off gains recur. That is the bull case. It is not yet a track record: bosutinib is the first large one in this set of documents.",
            "Dapagliflozin's launch date depends on its patent position, which the documents do not disclose.",
        ]),
        "Count each exclusivity launch as a one-off when it lands. If they arrive every year or two, the average lifts; watch the launch count each quarter against the 30-in-18-months target.")

# ================================================================ S6 guidance drift
ladder = C.bars(["May 2026", "Aug 2026", "Nov 2026"], [11, 14, 22.5], "FY27 consolidated growth guidance by call date, %",
                unit="%", w=520, h=230, highlight={2},
                value_labels=["low double digit", "closer to mid-teen", "20% to 25%"])
h2 = C.bars(["H2 FY26 actual", "H1 FY27 actual", "H2 FY27 at 20% [E]", "H2 FY27 at 25% [E]"],
            [3724, 4753, DEC["h2_implied_lo"], DEC["h2_implied_hi"]], "Half-year sales, Rs crore", w=520, h=230,
            colors=[C.GREY, C.PRIMARY, C.PRIMARY, C.PRIMARY], hatch={2, 3})
drift = table(["Item", "Q3 FY26 (Feb)", "Q4 FY26 (May)", "Q1 FY27 (Aug)", "Q2 FY27 (Nov)"], [
    ["FY27 consolidated growth", "-", "Low double digit", "Closer to mid-teen", "About 20% to 25%"],
    ["FY27 US growth", "10% to 15% a year (FY27/28)", "10% to 15% in INR", "Mid to high teens", "Up to 40%"],
    ["FY27 India growth", "Back to market by Q1 FY27", "At market", "High single digit", "At market, nearing double digit"],
    ["FY27 API growth", "-", "About 10%", "Above 10%", "At least high teens"],
    ["EBITDA margin", "No margin from Pivya until it scales", "20% in 2 to 3 years", "Reported 'flattish' to slightly better", "About 22% H1 (19.5% by our sum); 'closer to 20%' FY28 to FY29"],
    ["US branded drag", "-", "100 to 150 bp", "About 150 bp", "150 to 200 bp; none in FY28"],
], "std", caption="Guidance across the four calls", source=src(("q3c", 9), "q4c", ("q1c", 11), ("q2c", 5), ("q2c", 8), ("q2c", 14)))
section("s6", "Guidance and implied H2", "Guidance", "Guidance was raised twice in six months, and still implies a weaker second half",
        f"The 20% to 25% FY27 guide implies H2 sales of Rs {f0(DEC['h2_implied_lo'])} to {f0(DEC['h2_implied_hi'])} cr, {pc(-DEC['h2_vs_h1_hi'])} to {pc(-DEC['h2_vs_h1_lo'])} below H1, but still {pc(DEC['h2_vs_h2fy26_lo'])} to {pc(DEC['h2_vs_h2fy26_hi'])} above H2 FY26.",
        duo(exhibit("FY27 growth guidance rose from low double digit to 20% to 25%", ladder, src("q4c", "q1c", ("q2c", 5)),
                    "Bar heights are our numeric reading of the words: 11%, 14% and the 22.5% mid-point [E]."),
            exhibit("The guide implies H2 FY27 below H1 FY27 [E]", h2, src(("q2c", 5), "scr", "model"),
                    "H2 implied = FY26 sales Rs 7,345 cr x (1.20 or 1.25) minus H1 FY27 Rs 4,753 cr."))
        + drift
        + quote("guidance incorporates the expected normalization of exclusivity-led sales", "Management, Q2 FY27 call, p5"),
        "Management is telling you the exclusivity boost fades in H2. A Q3 that falls back toward Rs 2,000 to 2,200 cr is in line with guidance, not a miss.")

# ================================================================ S7 management claims vs record
claims = table(["Said", "When", "What happened", "Status"], [
    ["FY26 US growth 10% to 12%", "Q3 FY26 call p9", f"FY26 US grew {pc(CALC['us_fy_g'])}", chip("MET")],
    ["India back in line with the market by Q1 FY27", "Q3 FY26 call p5, p8", "Q1 FY27 +7%, Q2 +14% (human health +11%)", chip("LATE")],
    ["FY27 consolidated low double digit", "Q4 FY26 call", "H1 +31%; guide now 20% to 25%", chip("BEAT")],
    ["Bosutinib: 'I don't see that opportunity over 6 months'", "Q1 FY27 call p13", "Q2: sales 'far higher than expectations'", chip("BEAT")],
    ["Branded drag 100 to 150 bp", "Q4 FY26 call", "Raised to 150 to 200 bp", chip("WATCH")],
    ["20% EBITDA margin in 2 to 3 years", "Q4 FY26 call", "Q2 22.2% with exclusivity; H1 19.5%", chip("OPEN")],
    ["Branded breakeven from H1 FY28", "Q2 FY27 call p11", "Not yet testable", chip("OPEN")],
], "std", caption="What management said and what happened", source=src(("q3c", 9), ("q3c", 5), "q4c", ("q1c", 13), ("q2c", 6), ("q2c", 11)))
section("s7", "Management record", "Credibility", "Good on the US, slow on India",
        "Management met or beat its US and group targets in this period, but India took longer than promised and the branded loss got bigger before it shrinks.",
        claims + quote("historically, Alembic has not been a high-growth company.", "Shaunak Amin, Q3 FY26 call, p11")
        + "<p>The one number management got clearly wrong was the size of bosutinib, and it was too low. That cuts both ways: it shows how much one exclusivity launch can move the numbers, and how much can fall away.</p>",
        "Give weight to the US guidance, which has been met. Give less weight to India and margin promises until two more quarters confirm them.")

# ================================================================ S8 triggers and risks
watch = table(["What to watch", "When", "Structural if", "One-off if"], [
    ["Q3 FY27 US sales", "Feb 2027", "Above $90m with bosutinib fading", "Back near $75m to $80m"],
    ["Ex-launch growth", "Q3 and Q4 FY27", "Group growth stays above 18% excluding new launches", "Falls back to about 10%"],
    ["Operating margin", "Q3 FY27 to Q2 FY28", "Holds 18% or more after exclusivity", "Back to 15% to 16%"],
    ["US branded loss", "H1 FY28", "Breakeven as guided", "Drag still above 100 bp"],
    ["Dapagliflozin and binimetinib", "Disclosure dates not given", "Launched with exclusivity", "Delayed by patents"],
    ["India growth", "Each quarter", "At or above market, near 10%", "Back to 5% to 7%"],
    ["Cash conversion", "FY27 annual report", "Cash from operations above 60% of EBITDA", "Working capital absorbs the profit, as in FY25"],
], "std", caption="Watch list with thresholds", source=src(("q2c", 6), ("q2c", 11), ("q2c", 13), "scr"))
risks = ul([
    "<b>R1, bosutinib erodes faster.</b> Q1 call p8: erosion will be 'quite drastic' because volumes are small. If H2 sales come in at the bottom of the guide, FY27 PAT growth drops sharply in FY28.",
    "<b>R2, the rupee reverses.</b> About 11 to 12 points of Q1 US growth was currency. A stronger rupee removes it.",
    "<b>R3, US price erosion.</b> FY23's margin of 12% shows how fast US pricing can hit Alembic.",
    "<b>R4, India keeps lagging.</b> India has grown about 6% a year for four years; the new head of human health is still new.",
    "<b>R5, cash.</b> FY25 cash from operations was Rs 88 cr on Rs 1,008 cr EBITDA. New US launches again lengthen collection cycles.",
    "<b>Anti-thesis in one line:</b> take out the launch block and Q2 was a 20% growth, 16% to 17% margin quarter, priced at 22x trailing earnings that include the one-off.",
])
section("s8", "Triggers and risks", "Monitoring", "Q3 FY27 is the first real test",
        "The next two quarters will show whether the base holds above 20% growth once bosutinib exclusivity ends in late November 2026.",
        watch + "<h3>Risks</h3>" + risks,
        "If Q3 US sales hold above $90m and margin stays at 18% or more, the structural case strengthens. If both fall back, the bear case is the better guide.")

# ================================================================ S9 valuation


def skill_tbl(name):
    t = SC[name]["table"]
    cols = t["hist"] + t["proj"]

    def row(label, key, fmt, bold=False, sign=False):
        cells = [(label, "bold") if bold else label]
        for c in cols:
            v = c.get(key)
            if v is None:
                cells.append("-")
                continue
            k = ("neg " if sign and v < 0 else "") + ("bold" if bold else "")
            cells.append((fmt(v), k.strip()) if k.strip() else fmt(v))
        return cells

    n = lambda v: f"{v:,.0f}"
    p1 = lambda v: f"{v * 100:.1f}%"
    rows = [row("Sales", "sales", n), row("Expenses", "expenses", n), row("Operating profit", "op", n), row("OPM", "opm", p1),
            row("Other income", "other_income", n), row("Interest", "interest", n), row("Depreciation", "depreciation", n),
            row("Profit before tax", "pbt", n), row("Tax rate", "tax_pct", p1), row("Net profit", "pat", n, bold=True),
            row("EPS (Rs), pre and post-dilution", "eps", lambda v: f"{v:.2f}"), row("PAT growth", "pat_growth", p1, sign=True),
            row("PAT margin", "pat_margin", p1), row("Target price at 31 Mar (Rs)", "tp", n, bold=True),
            row("Return vs CMP Rs 1,017", "ret", lambda v: f"{v * 100:+.0f}%", sign=True),
            row("CAGR vs CMP to 31 Mar", "cagr", lambda v: f"{v * 100:+.1f}%", sign=True)]
    return table(["Rs cr"] + [c["year"] for c in cols], rows, "fin",
                 caption=f"{name}: 22x P/E held flat, FY27E to FY29E (Screener layout; FY25A and FY26A actual) [E]",
                 source=src("model", "scr"))


rng = C.value_range([("Bear", TP29["Bear"], C.RED, "FY29E"), ("Base", TP29["Base"], C.PRIMARY, "FY29E"),
                     ("Bull", TP29["Bull"], C.GREEN, "FY29E")], D["price"], "FY29 value per share by scenario vs price",
                    w=720, lo=600, hi=1800)
assump = table(["", "Bear", "Base", "Bull"], [
    ["Sales growth FY27 / FY28 / FY29"] + [" / ".join(pc(g, 1 if g * 1000 % 10 else 0) for g in SC[k]["assumptions"]["growth"]) for k in SC],
    ["Operating margin FY27 / FY28 / FY29"] + [" / ".join(pc(m, 1) for m in SC[k]["assumptions"]["margin"]) for k in SC],
    ["Built from"] + [SC[k]["assumptions"]["why"] for k in SC],
], "std", caption="Scenario inputs [E]", source=src(("q2c", 5), ("q2c", 13), ("q2c", 14), "model"))
cross = table(["Check", "Working", "Result"], [
    ["P/E on trailing EPS", "Rs 1,017 / Rs 42.92", f"{CROSS['pe_ttm']:.1f}x (Screener shows 22.3x)"],
    ["P/E on FY26 EPS", "Rs 1,017 / Rs 34.33", f"{CROSS['pe_fy26']:.1f}x"],
    ["EPS the price needs at 22x", "Rs 1,017 / 22", f"Rs {CROSS['eps_needed_at_22x']:.1f}, about our FY27 base EPS of Rs {B['Base'][0]['eps']:.1f}"],
    ["EV / trailing EBITDA", f"(Rs 19,996 + 1,236 cr) / Rs 1,413 cr", f"{CROSS['ev_ttm_ebitda']:.1f}x"],
    ["EV / FY28 base EBITDA", f"Rs {f0(CROSS['ev'])} cr / Rs {f0(B['Base'][1]['op'])} cr", f"{CROSS['ev_fy28_base_ebitda']:.1f}x"],
], "std", caption="Reverse check and EV/EBITDA cross-check", source=src("scr", ("q2c", 6), "model"))
skill_note = """<p><b>How to read the year-by-year tables.</b> Each case is laid out like a Screener profit and loss page: two actual years, then our three projected years.
The target price at 31 March of each year is that year's earnings per share times 22, not discounted.
Return and CAGR are measured from Rs 1,017 on 10 November 2026. FY27E CAGR is annualised over the 0.39 years to 31 Mar 2027, so small moves show as large yearly rates; read it with the return row.
No warrants or convertibles were found in the documents read, so earnings per share is the same before and after dilution.</p>"""
section("s9", "Value in three scenarios", "Valuation", "The price already pays for guidance being met",
        f"At 22x earnings, FY29 value is about Rs {f0(TP29['Bear'])} in the bear case, Rs {f0(TP29['Base'])} in the base case and Rs {f0(TP29['Bull'])} in the bull case, against Rs 1,017 today.",
        exhibit("FY29 value per share by scenario vs today's price [E]", rng, src("model"),
                f"FY28 values: bear Rs {f0(TP28['Bear'])}, base Rs {f0(TP28['Base'])}, bull Rs {f0(TP28['Bull'])}. The bear FY28 dip is the year the launch block fades.")
        + "<p>Why P/E: Alembic is profitable and its earnings are not in a deep cycle, so earnings per share is the most direct measure. EV/EBITDA is shown as a check because it includes the Rs 1,236 cr of net debt.</p>"
        + assump + cross + skill_note + skill_tbl("Bear") + skill_tbl("Base") + skill_tbl("Bull")
        + "<h3>Key assumptions and caveats</h3>" + ul(VAL["caveats"], "small"),
        "The base case gives about 14% a year to March 2029 if management delivers its guidance with no slip. The bear case loses money even at an unchanged 22x, and a bear outcome would usually come with a lower multiple too. This is not investment advice.")

# ================================================================ S10 sources and method
srcs = "".join(f'<li>{f"<a href=\"{u}\">{n}</a>" if u else n}</li>' for n, u in SRC.values())
section("s10", "Sources and method", "Appendix", "What we read and how",
        "This quick analysis uses only the latest four call transcripts, the four matching investor presentations, four announcements and Screener financials.",
        f'<ol class="srcs">{srcs}</ol>' + ul([
            "Tags: [E] our estimate; [G] management guidance. Everything else is reported.",
            "Data conflicts: (C1) the CFO called H1 EBITDA margin 'about 22%', but the company's own quarterly numbers sum to 19.5%; we treat 22% as the Q2 rate. "
            "(C2) Screener operating profit runs about Rs 16 cr a quarter below company EBITDA; the model uses Screener. "
            "(C3) Q4 FY26 revenue is Rs 1,838 cr on the call and Rs 1,848 cr on Screener. "
            "(C4) Q2 US growth is 72% for generics (call) and 77% for all US (deck). "
            "(C5) Trailing P/E is 23.7x on price / TTM EPS and 22.3x on Screener.",
            "Gaps: BSE and NSE announcement feeds were not reachable, so the four announcements were picked from company press releases and the Q2 call. "
            "The DifGen announcement is cited from a trade report and the Q2 call. Bosutinib revenue is not disclosed.",
            "Analysis by a single analyst (Opus 5.5); no sub-agents were used. Data as of 10 November 2026; report dated 11 November 2026.",
            "Not investment advice. The author is not a licensed financial advisor. No rating is given.",
        ], "small"),
        "Every number in this report can be traced to the linked documents or to model/valuation.py.")

# ---------------------------------------------------------------- render
CSS = """
:root{--brand:#1F2A5C;--p1:#2F3F8F;--p2:#B86E00;--brandt:#ECEEF7;--ink:#1F2733;--muted:#5F6873;--line:#DDE2E7;--bg:#EEF0F4;--red:#B23A3A}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;color-scheme:light}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 Calibri,Carlito,'Segoe UI',Arial,sans-serif}
a{color:#2F3F8F}
.wrap{display:grid;grid-template-columns:200px minmax(0,980px);gap:22px;justify-content:center;padding:0 16px}
.side{padding-top:22px;font-size:13px;align-self:start}
.side .brand{font-weight:700;color:var(--brand);font-size:15px;margin:0 0 2px}
.side .sub{color:var(--muted);margin:0 0 12px;font-size:12px}
.side ol{list-style:none;margin:0;padding:0}
.side li{margin:0 0 4px}
.side a{text-decoration:none;color:var(--ink)}
.side a:hover{color:var(--p1);text-decoration:underline}
.side .n{display:inline-block;width:30px;color:var(--muted)}
.page{background:#fff;border:1px solid var(--line);margin:22px 0}
.band{background:var(--brand);color:#fff;display:flex;justify-content:space-between;align-items:center;padding:8px 26px;font-size:12.5px;letter-spacing:.03em}
.band b{color:#C9D0F0}
.rule{height:3px;background:var(--p2)}
.inner{padding:16px 26px 10px}
.kicker{color:var(--p2);font-weight:700;font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;margin:4px 0 2px}
h1,h2,h3,h4{color:var(--brand)}
h2{font-size:24px;line-height:1.2;margin:0 0 10px}
h3{font-size:17px;margin:18px 0 6px}
h4{font-size:15px;margin:16px 0 4px}
p{margin:0 0 9px}
.answer{font-weight:700;font-size:16px;line-height:1.45;border-left:3px solid var(--p1);padding:2px 0 2px 12px;margin:4px 0 14px}
.mfy{margin-top:18px;border-top:1px solid var(--line);padding-top:10px}
.lede{font-size:17px;line-height:1.5;color:var(--brand)}
.ex{margin:14px 0;padding:0;break-inside:avoid}
figcaption{font-weight:700;color:var(--brand);font-size:14px;margin-bottom:6px}
.src{font-size:11.5px;color:var(--muted);margin:4px 0 0}
.xnote{font-size:12.5px;margin:6px 0 0;color:#3A434E}
.duo{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:22px;align-items:start}
.t{border-collapse:collapse;width:100%;font-size:13.5px;margin:4px 0}
.t th{border-bottom:1.5px solid var(--brand);color:var(--brand);font-weight:700;padding:5px 7px;text-align:right;vertical-align:bottom}
.t th:first-child{text-align:left}
.t td{padding:4px 7px;border-bottom:1px solid var(--line);vertical-align:top}
.t td.l{text-align:left}.t td.r{text-align:right}
.t.std td.r,.t.std th{text-align:left}
.t td.neg{color:var(--red)}.t td.bold{font-weight:700}
.t.kv th{display:none}.t.kv td{padding:3px 4px;font-size:13px}
.t.fin td,.t.fin th{font-size:12.5px;padding:3px 5px;white-space:nowrap}
.t.fin td.l{white-space:normal}
.tw{overflow-x:auto;max-width:100%}
.chip{display:inline-block;padding:0 7px;border-radius:3px;font-size:11.5px;font-weight:700;letter-spacing:.02em;border:1px solid;white-space:nowrap}
.chip.ok{color:#1F6B4C;border-color:#7FB79E;background:#EEF7F2}
.chip.watch{color:#8A520C;border-color:#D9AE6E;background:#FBF3E6}
.chip.red{color:#8E2525;border-color:#D69292;background:#FBEFEF}
.chip.open{color:#2F3F8F;border-color:#9BA6D6;background:#EEF0F9}
.small{font-size:13px}.tiny{font-size:12px;color:var(--muted)}
.cw-m{display:none}
ul{padding-left:20px;margin:4px 0 10px}li{margin:0 0 5px}
blockquote.q{margin:14px 0;padding:8px 14px;border-left:3px solid var(--p2);background:#FBF6EE}
blockquote.q p{margin:0 0 4px;font-style:italic}blockquote.q cite{font-size:12.5px;color:var(--muted);font-style:normal}
.ctitle{font-size:34px;font-weight:700;margin:0;line-height:1.1}
.csub{font-size:19px;color:var(--p2);margin:4px 0 2px;font-weight:700}
.cmeta{font-size:13px;color:var(--muted);margin:0 0 12px}
.cover{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:24px}
.rail{background:#F6F7FA;border:1px solid var(--line);padding:12px;align-self:start}
.rbox{margin-top:12px}
.rh{font-weight:700;color:#fff;background:var(--brand);margin:0 0 4px;padding:3px 8px;font-size:12.5px}
.verdict{border:1px solid var(--p2);background:#FBF3E6;padding:8px 10px}
.verdict .rk{margin:0;font-size:11.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.verdict .rv{margin:0;font-size:22px;font-weight:700;color:var(--brand)}
.verdict .rs{margin:2px 0 0;font-size:12.5px}
.flow{display:flex;align-items:stretch;gap:6px}
.fcol{flex:1;display:flex;flex-direction:column;gap:5px;min-width:0}
.fh{margin:0;font-weight:700;font-size:12.5px;color:var(--brand)}
.fb{background:var(--brandt);border:1px solid #C9CFE8;padding:7px;font-size:13px;line-height:1.35;border-radius:3px;flex:1}
.fb.gold{background:#FBF3E6;border-color:#D9AE6E}
.fb small{color:var(--muted);display:block;margin-top:3px}
.farrow{align-self:center;color:var(--p2);font-size:18px}
.srcs{font-size:13px;padding-left:22px}
.foot{display:flex;justify-content:space-between;border-top:1px solid var(--line);margin:8px 26px 0;padding:7px 0 10px;font-size:11.5px;color:var(--muted)}
.topnav{display:none}
@media screen and (max-width:1240px){.wrap{grid-template-columns:180px minmax(0,1fr)}}
@media screen and (max-width:820px){
 .cw-d{display:none}.cw-m{display:block}
 .duo,.cover{grid-template-columns:minmax(0,1fr)}
 .flow{flex-direction:column}.farrow{transform:rotate(90deg)}
 .t{font-size:12.5px}.t th,.t td{padding:4px 5px}
 .t.fin td,.t.fin th{font-size:11.5px;padding:3px 3px}
}
@media screen and (max-width:768px){
 .wrap{display:block;padding:0}
 .side{display:none}
 .topnav{display:block;background:var(--brand);padding:10px 16px}
 .topnav p{margin:0 0 6px;color:#fff;font-weight:700}
 .topnav ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px 12px}
 .topnav a{color:#DDE2F6;font-size:13px;text-decoration:none}
 .page{margin:0 0 10px;border-left:0;border-right:0}
 .inner{padding:14px 16px 8px}.band{padding:7px 16px}.foot{margin:6px 16px 0}
 .band span:last-child{display:none}
 h2{font-size:21px}.ctitle{font-size:27px}
}
@media print{
 body{background:#fff;font-size:10pt}.wrap{display:block;padding:0}.side,.topnav{display:none}
 .page{margin:0 0 18pt;border:0}.ex,.duo{break-inside:avoid}a{color:inherit;text-decoration:none}
}
"""


def render():
    total = len(SECTIONS)
    side = ['<nav class="side" aria-label="Contents"><p class="brand">Alembic Pharmaceuticals</p><p class="sub">Quick analysis, 11 Nov 2026</p><ol>']
    top = ['<nav class="topnav" aria-label="Contents"><p>Contents</p><ol>']
    for i, (sid, short, *_) in enumerate(SECTIONS):
        side.append(f'<li><a href="#{sid}"><span class="n">{i + 1}</span>{short}</a></li>')
        top.append(f'<li><a href="#{sid}">{i + 1} {short}</a></li>')
    side.append("</ol></nav>")
    top.append("</ol></nav>")
    out = []
    for i, (sid, short, kicker, headline, html) in enumerate(SECTIONS):
        band = ('<div class="band"><span><b>ALEMBIC PHARMACEUTICALS</b> &nbsp;|&nbsp; NSE: APLLTD &nbsp;|&nbsp; Quick analysis</span>'
                '<span>11 November 2026</span></div><div class="rule"></div>')
        head = ""
        if sid == "s1":
            head = ('<p class="kicker">NSE: APLLTD &nbsp;|&nbsp; BSE: 533573 &nbsp;|&nbsp; Generic pharmaceuticals</p>'
                    '<h1 class="ctitle">Alembic Pharmaceuticals Ltd</h1>'
                    '<p class="csub">Q2 FY27 step-up: structural or one-off?</p>'
                    '<p class="cmeta">Quick analysis, not a recommendation &nbsp;|&nbsp; Data as of 10 November 2026 &nbsp;|&nbsp; Rs crore unless stated</p>')
        out.append(f'<section class="page" id="{sid}">{band}<div class="inner">{head}<p class="kicker">{kicker}</p><h2>{headline}</h2>{html}</div>'
                   f'<div class="foot"><span>Alembic Pharmaceuticals | Quick analysis | Not investment advice</span><span>{i + 1} / {total}</span></div></section>')
    body = "".join(out)
    cnt = [0]

    def _renum(m):
        cnt[0] += 1
        return f"<figcaption>Exhibit {cnt[0]}:"
    body = re.sub(r"<figcaption>Exhibit \d+:", _renum, body)
    html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Alembic Quick Analysis</title>'
            '<meta name="description" content="Is Alembic Pharmaceuticals\' Q2 FY27 step-up structural or one-off? Quick analysis, data as of 10 Nov 2026.">'
            f'<style>{CSS}</style></head><body>{"".join(top)}<div class="wrap">{"".join(side)}<main>{body}</main></div></body></html>')
    assert "—" not in html and "–" not in html, "em or en dash found"
    with open(os.path.join(HERE, "report.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    with open(os.path.join(HERE, "chart-data.json"), "w", encoding="utf-8") as fh:
        json.dump({"data": D, "calc": CALC, "sources": SRC}, fh, indent=1, ensure_ascii=False, default=str)
    return html, cnt[0]


if __name__ == "__main__":
    h, nex = render()
    print("sections", len(SECTIONS), "exhibits", nex, "bytes", len(h))
    print({k: round(v, 3) for k, v in CALC.items() if isinstance(v, float)})
