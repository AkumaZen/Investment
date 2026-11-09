"""Build the Concord Biotech client report (single self-contained HTML).

Run:  python -I -X utf8 report/build.py      (from the company folder)
Out:  report/report.html, report/chart-data.json

All money is Rs crore unless stated. Every exhibit carries its source line.
Valuation numbers are read from ../model/valuation.json (model/valuation.py), never typed in.
Derived numbers are computed in calc() and tied back to filed totals with asserts.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import charts as C  # noqa: E402

VAL = json.load(open(os.path.join(HERE, "..", "model", "valuation.json"), encoding="utf-8"))


def _responsive(fn):
    """Charts wider than a phone get a second, phone-sized drawing swapped in by CSS at 820px."""
    def wrap(*a, **kw):
        w = kw.get("w", 520)
        if w < 420:
            return fn(*a, **kw)
        mk = dict(kw, w=360)
        if kw.get("h"):
            mk["h"] = int(kw["h"] * (1.0 if w < 600 else 1.08))
        return f'<div class="cw-d">{fn(*a, **kw)}</div><div class="cw-m">{fn(*a, **mk)}</div>'
    return wrap


for _n in ("bars", "grouped", "lines", "hbars", "waterfall", "value_range"):
    setattr(C, _n, _responsive(getattr(C, _n)))

# ---------------------------------------------------------------- sources
BSE = "https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname={}.pdf"
SRC = {
    "deck27": ("Q2 FY27 investor presentation, 27 Oct 2026", BSE.format("118d1eac-e193-46cb-ae1b-a1caa31993e0")),
    "deck426": ("Q4 FY26 investor presentation, 30 May 2026", BSE.format("f7e81595-7124-4fa1-9ea0-20682d51d8fa")),
    "deck226": ("Q2 FY26 investor presentation, 13 Nov 2025", BSE.format("f934c394-3b55-470f-b81b-acb031601389")),
    "tr27": ("Q2 FY27 call transcript, 28 Oct 2026", BSE.format("ea74d0f1-395f-4d3a-ad8e-4d0cfb5182d6")),
    "tr127": ("Q1 FY27 call transcript, 3 Aug 2026", BSE.format("105c5d3d-a70a-4fd0-a0f9-fcd4dafcd984")),
    "tr426": ("Q4 FY26 call transcript, 1 Jun 2026", BSE.format("a5e51736-3b9f-4286-89d2-b5fe20aa9ef7")),
    "tr326": ("Q3 FY26 call transcript, 12 Feb 2026", BSE.format("612d3269-a756-4bb6-9599-02449be09d0b")),
    "tr226": ("Q2 FY26 call transcript, 14 Nov 2025", BSE.format("a2e1d840-994f-4249-8e2a-2721ae943b2c")),
    "tr126": ("Q1 FY26 call transcript, 11 Aug 2025", BSE.format("addbb564-28e8-4082-9a21-e5db2523d4b7")),
    "tr425": ("Q4 FY25 call transcript, 30 May 2025", BSE.format("c83e1980-61c3-4e31-ab22-68b8c1eb05c7")),
    "tr325": ("Q3 FY25 call transcript, 14 Feb 2025", BSE.format("2331ef6f-b29f-45a9-8504-a240ea1b4f36")),
    "tr225": ("Q2 FY25 call transcript, 12 Nov 2024", BSE.format("b067a150-a0a4-454a-9225-2566e17b404a")),
    "tr125": ("Q1 FY25 call transcript, 12 Aug 2024", BSE.format("fd223f7b-18e4-401e-bbad-966b3a7d7533")),
    "tr324": ("Q3 FY24 call transcript, 9 Feb 2024", BSE.format("fc8098c1-b016-4bd2-b819-9ca4582d883f")),
    "tr124": ("Q1 FY24 call transcript, 7 Sep 2023", BSE.format("3a010362-24c5-4b39-83f1-87b465d43b52")),
    "ar26": ("Annual Report FY2025-26",
             "https://www.bseindia.com/xml-data/corpfiling/AttachHis/ec74e0d2-8c48-4a0b-9961-f4be126f5dda.pdf"),
    "bonus": ("Bonus allotment filing, 4 Nov 2026", BSE.format("2f88d61b-23a5-4e8e-adfb-82ac09d13ff7")),
    "press27": ("Q2 FY27 results filing, 28 Oct 2026", BSE.format("efd072c7-89b4-40ce-a718-eeaf8374dcdb")),
    "rhp": ("IPO red herring prospectus, Aug 2023",
            "https://www.bseindia.com/corporates/download/383248/IPO%20Open/RHP_20230802171607.pdf"),
    "scr": ("Screener.in consolidated data, fetched 9 Nov 2026", "https://www.screener.in/company/CONCORDBIO/consolidated/"),
    "decks": ("Company investor presentations Q1 FY24 to Q2 FY27 (our extraction)", None),
    "ledger": ("Our promises-vs-delivery ledger of all 14 calls, Q1 FY24 to Q2 FY27", None),
    "model": ("Our valuation model (model/valuation.py)", None),
    "peers": ("Screener.in peer pages, fetched 9 Nov 2026", "https://www.screener.in/company/CONCORDBIO/consolidated/"),
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


# ---------------------------------------------------------------- data (facts)
D = {
    "price": 594.0, "shares_cr": 20.9232408, "hi52": 808, "lo52": 494, "bv": 99.2,
    "years": ["FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"],
    "sales": [512, 616, 713, 853, 1017, 1200, 1055], "sales_ttm": 1170,
    "op": [205, 327, 270, 344, 432, 506, 368], "op_ttm": 403,
    "opm": [40, 53, 38, 40, 42, 42, 35],
    "oi": [32, 14, 23, 37, 37, 44, 52], "dep": [21, 28, 50, 54, 54, 54, 74],
    "pbt": [214, 313, 238, 322, 413, 495, 345],
    "pat": [169, 235, 175, 240, 308, 372, 259], "pat_ttm": 279,
    "eps_adj": [8.09, 11.26, 8.37, 11.48, 14.73, 17.76, 12.47], "eps_ttm": 13.50,
    "payout": [22, 0, 3, 30, 30, 25, 30],
    "reserves": [761, 990, 1094, 1280, 1516, 1802, 2007],
    "borrow": [52, 86, 62, 32, 10, 3, 2],
    "fa": [240, 546, 573, 593, 575, 795, 789], "cwip": [141, 18, 74, 173, 211, 51, 79],
    "inv_book": [199, 141, 74, 137, 246, 335, 491],
    "cfo": [155, 167, 207, 246, 265, 245, 267], "fcf": [-1, -38, 52, 101, 180, 134, 172],
    "debtor_d": [131, 105, 119, 117, 125, 159, 159], "inv_d": [312, 503, 434, 430, 331, 286, 485],
    "pay_d": [201, 152, 185, 190, 150, 135, 151], "ccc": [242, 456, 368, 357, 306, 310, 493],
    "roce": [None, 32, 21, 26, 28, 28, 17],
    # Screener quarterly (consolidated)
    "q": ["Dec-24", "Mar-25", "Jun-25", "Sep-25", "Dec-25", "Mar-26", "Jun-26", "Sep-26"],
    "ql": ["Q3 FY25", "Q4 FY25", "Q1 FY26", "Q2 FY26", "Q3 FY26", "Q4 FY26", "Q1 FY27", "Q2 FY27"],
    "q_sales": [244, 430, 204, 247, 278, 326, 257, 309],
    "q_op": [98, 189, 61, 88, 98, 118, 82, 104],
    "q_pat": [76, 140, 44, 63, 64, 88, 58, 70],
    # margin excluding injectables and Stellon, as stated on calls (ledger M4, Q2 FY27 p5/p7)
    "q_adj": [None, None, 37, 41, 40, 39, None, 37.1],
    # segments (decks)
    "seg_years": ["FY23", "FY24", "FY25", "FY26"],
    "api": [761.3, 828.0, 940.1, 828.8], "form": [91.9, 188.9, 260.0, 226.1],
    "api_h1": [345.6, 469.1], "form_h1": [105.5, 97.5],
    "q4": ["Q4 FY23", "Q4 FY24", "Q4 FY25", "Q4 FY26"], "q4_sales": [272.6, 319.0, 429.9, 326.1],
    "geo": {"India": 563.60, "United States": 108.03, "Other overseas": 383.25},
    "geo25": {"India": 661.83, "United States": 137.97, "Other overseas": 400.28},
    "top10": {"FY22": 47.7, "FY23": 44.3, "FY24": 42.0, "FY25": 37.8, "FY26": 37.6},
    "util_q2fy27": {"Unit I Dholka (API)": 75, "Unit III Limbasi (API)": 55, "Unit II Valthera (tablets)": 21,
                    "Unit IV Valthera (injectables)": 5},
    "util_hist_cats": ["H1 FY24", "Q1 FY25", "H1 FY25", "FY25", "Q1 FY26", "Q3 FY26", "FY26", "Q2 FY27"],
    "util_u1": [78, 76.5, 79, 84, 75, 81, 77, 75],
    "util_u2": [14.5, 24, 50, 36, 26, 27, 30, 21],
    "util_u3": [36, 38, 38, 40, 57, 40, 53, 55],
    # Q2 FY27 / H1 FY27 results (deck p11, results filing)
    "h1": {"rev": 566.6, "rev_ly": 451.1, "gm": 77.4, "gm_ly": 79.1, "ebitda": 187, "ebitda_ly": 150,
           "pat": 127.3, "pat_ly": 107.0, "cfo": 168.2, "cfo_ly": 151.1},
    "q2": {"rev": 309.1, "rev_ly": 247.1, "gm": 76.2, "gm_ly": 80.2, "ebitda": 104.4, "ebitda_ly": 88.5,
           "pat": 69.6, "pat_ly": 63.1},
    "h2fy26": 603.9, "fy26_rev": 1054.9, "fy25_rev": 1200.1, "fy26_pat_owners": 259.2,
    "cash_liquid_sep26": 445.8, "inv_noncurrent_sep26": 96.0, "inv_current_sep26": 438.1,
    "inventory_sep26": 397.8, "inventory_mar26": 326.4, "recv_sep26": 412.5, "recv_mar26": 460.2,
    "promoter": 44.09,
    "holders": {"Sudhir Vaid": 28.84, "Manju Vaid": 9.55, "Sudman Consultants LLP": 4.54, "Ankur Vaid": 0.56,
                "Megha Vaid": 0.52, "Sonal Kumra": 0.07},
    "kmp_pay": [13.81, 14.05], "median_raise": 8.59,
    "peers": [  # name, sales FY26, g25, g26, gttm, opm25, opm26, opmttm, pe, roce
        ("Concord Biotech", 1055, 18, -12, 4, 42, 35, 34, 43.6, 17.1),
        ("Divi's Laboratories", 10560, 19, 13, 22, 32, 33, 38, 89.8, 22.0),
        ("Neuland Laboratories", 2023, -5, 37, 50, 22, 29, 31, 58.2, 26.5),
        ("Laurus Labs", 6813, 10, 23, 23, 19, 26, 30, 98.5, 17.8),
        ("Sai Life Sciences", 2192, 16, 29, 16, 24, 29, 29, 102.0, 19.6),
        ("Gland Pharma", 6431, -1, 14, 22, 23, 25, 27, 43.9, 15.1),
        ("Biocon", 16927, 3, 11, 6, 21, 21, 20, 87.9, 3.6),
        ("Aarti Drugs", 2565, -6, 7, 15, 12, 12, 13, 19.6, 12.0),
    ],
}

CALC = {}


def calc():
    d = D
    s = d["sales"]
    CALC["mcap"] = d["price"] * d["shares_cr"]
    CALC["net_cash"] = d["cash_liquid_sep26"] - 2.0
    CALC["cagr_20_25"] = (s[5] / s[0]) ** (1 / 5) - 1
    CALC["cagr_20_26"] = (s[6] / s[0]) ** (1 / 6) - 1
    CALC["cagr_24_26"] = (s[6] / s[4]) ** (1 / 2) - 1
    CALC["q_opm"] = [o / v * 100 for o, v in zip(d["q_op"], d["q_sales"])]
    CALC["fy26_fall"] = d["fy25_rev"] - d["fy26_rev"]
    CALC["h1fy25"] = d["fy25_rev"] - 244 - 430           # derived [E]
    CALC["h2fy25"] = 244 + 430
    CALC["need19"] = d["fy26_rev"] * 1.19 - d["h1"]["rev"]
    CALC["need20"] = d["fy26_rev"] * 1.20 - d["h1"]["rev"]
    CALC["need19_g"] = CALC["need19"] / d["h2fy26"] - 1
    CALC["need20_g"] = CALC["need20"] / d["h2fy26"] - 1
    CALC["need18"] = d["fy26_rev"] * 1.18 - d["h1"]["rev"]
    CALC["need18_g"] = CALC["need18"] / d["h2fy26"] - 1
    CALC["h1_growth"] = d["h1"]["rev"] / d["h1"]["rev_ly"] - 1
    CALC["api_h1_g"] = d["api_h1"][1] / d["api_h1"][0] - 1
    CALC["form_h1_g"] = d["form_h1"][1] / d["form_h1"][0] - 1
    CALC["api_share_h1"] = d["api_h1"][1] / d["h1"]["rev"]
    CALC["fat"] = [s[i] / d["fa"][i] for i in range(7)]
    CALC["cfo_ebitda"] = [c / o * 100 for c, o in zip(d["cfo"], d["op"])]
    CALC["capex"] = [c - f for c, f in zip(d["cfo"], d["fcf"])]
    rev = d["fy26_rev"]
    CALC["per100"] = {
        "ebitda": 368 / rev * 100, "dep_int": (74 + 1) / rev * 100, "oi": 52 / rev * 100,
        "pbt": 345 / rev * 100, "pat": d["fy26_pat_owners"] / rev * 100,
        "cfo": 267 / rev * 100, "capex": 95 / rev * 100, "fcf": 172 / rev * 100}
    CALC["adj_gap_fy26"] = 0.04 * rev                # 39% vs 35% (Q4 FY26 p5)
    CALC["adj_gap_h1"] = (0.378 - 0.330) * d["h1"]["rev"]
    CALC["kmp_pct_pat"] = d["kmp_pay"][1] / d["fy26_pat_owners"] * 100
    CALC["pat_chg"] = d["pat"][6] / d["pat"][5] - 1
    CALC["inv_book_sep26"] = d["inv_current_sep26"] + d["inv_noncurrent_sep26"]
    CALC["geo_share"] = {k: v / rev * 100 for k, v in d["geo"].items()}
    CALC["geo_chg"] = {k: d["geo"][k] / d["geo25"][k] - 1 for k in d["geo"]}
    CALC["halve"] = d["price"] / 2
    CALC["halve_pe"] = CALC["halve"] * d["shares_cr"] / d["pat_ttm"]
    CALC["peak3000_cagr"] = (3000 / rev) ** (1 / 6) - 1
    CALC["unit3_80_years"] = __import__("math").log(80 / 55) / __import__("math").log(1.18)

    # ---- tie-outs against filed totals
    assert sum(d["q_sales"][2:6]) == 1055, "FY26 quarters must sum to FY26 sales"
    assert sum(d["q_pat"][2:6]) == 259, "FY26 quarter PAT must sum to FY26 PAT"
    assert sum(d["q_sales"][4:]) == d["sales_ttm"], "TTM must be last four quarters"
    assert abs(sum(d["q_sales"][6:]) - d["h1"]["rev"]) < 1.0
    assert abs(sum(d["q_sales"][4:6]) - d["h2fy26"]) < 0.5
    for i in range(4):
        tot = [853, 1017, 1200, 1055][i]
        assert abs(d["api"][i] + d["form"][i] - tot) < 1.0, ("segments", i)
    assert abs(d["api_h1"][0] + d["form_h1"][0] - d["h1"]["rev_ly"]) < 0.1
    assert abs(d["api_h1"][1] + d["form_h1"][1] - d["h1"]["rev"]) < 0.1
    assert abs(sum(d["geo"].values()) - rev) < 0.05
    assert abs(sum(d["holders"].values()) - d["promoter"]) < 0.05
    assert abs(d["inv_current_sep26"] + 7.7 - d["cash_liquid_sep26"]) < 0.05
    for i in range(7):
        assert abs(d["cfo"][i] - d["fcf"][i] - CALC["capex"][i]) < 1e-9
        assert abs(d["op"][i] / d["sales"][i] * 100 - d["opm"][i]) < 0.8, ("opm", i)
    p = CALC["per100"]
    assert abs((p["ebitda"] - p["dep_int"] + p["oi"]) - p["pbt"]) < 0.1
    # model ties
    base = VAL["scenarios"]["Base"]
    assert abs(base["rows"][0]["revenue"] - rev * 1.19) < 0.01
    assert abs(CALC["mcap"] - VAL["inputs"]["price"][0] * VAL["inputs"]["shares_cr"][0]) < 0.01
    return CALC


calc()
V = {k: VAL["scenarios"][k]["value"] for k in ("Bear", "Base", "Bull")}
ROWS = {k: VAL["scenarios"][k]["rows"] for k in ("Bear", "Base", "Bull")}
READOUT = VAL["readout"]
assert READOUT == "FAIR"


# ---------------------------------------------------------------- formatting
def f0(v):
    return C._fmt(v, 0)


def f1(v):
    return C._fmt(v, 1)


def pc(v, dec=0, sign=False):
    s = C._fmt(v * 100, dec)
    return ("+" if sign and v > 0 else "") + s + "%"


def neg(v, dec=0):
    """Accounting style: negatives in brackets."""
    if v is None:
        return "-"
    return f"({C._fmt(-v, dec)})" if v < 0 else C._fmt(v, dec)


# ---------------------------------------------------------------- page helpers
SECTIONS = []      # (sid, part, short, kicker, headline, html)
EX = [0]


def exhibit(title, svg, source, note=None):
    EX[0] += 1
    n = f'<p class="xnote">{note}</p>' if note else ""
    return (f'<figure class="ex"><figcaption>Exhibit {EX[0]}: {title}</figcaption>{svg}{n}'
            f'<p class="src">{source}</p></figure>')


def duo(a, b):
    return f'<div class="duo">{a}{b}</div>'


def table(head, rows, cls="", first_left=True, caption=None, source=None):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = []
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            klass = "l" if (i == 0 and first_left) else "r"
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
    cls = {"OK": "ok", "WATCH": "watch", "RED": "red", "MET": "ok", "MISSED": "red", "LATE": "watch",
           "OPEN": "open", "SOFTENED": "watch", "STRONG": "ok", "MODERATE": "watch", "WEAK": "red",
           "MAKES AND SELLS": "ok", "FIRST ORDERS": "watch", "IN DEVELOPMENT": "open",
           "NOT DISCLOSED": "nd", "DOES NOT MAKE": "nd", "FAIR": "watch"}.get(word, "open")
    return f'<span class="chip {cls}">{word}</span>'


def section(sid, part, short, kicker, headline, answer, body, means):
    html = (f'<p class="answer">{answer}</p>{body}'
            f'<h4 class="mfy">What this means for you</h4><p class="means">{means}</p>')
    SECTIONS.append((sid, part, short, kicker, headline, html))


def ul(items, cls=""):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def flow(cols, cls=""):
    """cols: list of (heading, [box html], gold?)."""
    out = []
    for i, (h, boxes, gold) in enumerate(cols):
        if i:
            out.append('<div class="farrow" aria-hidden="true">&#8594;</div>')
        bx = "".join(f'<div class="fb{" gold" if gold else ""}">{b}</div>' for b in boxes)
        out.append(f'<div class="fcol"><p class="fh">{h}</p>{bx}</div>')
    return f'<div class="flow {cls}">{"".join(out)}</div>'


# ================================================================= S1 summary
base_v, bear_v, bull_v = V["Base"]["value_ps"], V["Bear"]["value_ps"], V["Bull"]["value_ps"]
n19, n19g, n20, n20g = CALC["need19"], CALC["need19_g"], CALC["need20"], CALC["need20_g"]

rail = f"""<aside class="rail">
<div class="verdict"><p class="rk">Valuation readout</p><p class="rv">{READOUT}</p>
<p class="rs">Our base value is Rs {f0(base_v)} a share, {pc(V['Base']['vs_price'], 0, True)} vs the price. Within 20% either way counts as fair. This is not a buy or sell call.</p></div>
<div class="rbox"><p class="rh">Value range (Rs a share)</p>
{table(["Case", "Value", "vs price"], [["Bear", f0(bear_v), (pc(V['Bear']['vs_price'], 0, True), "neg")], ["Base", (f0(base_v), "bold"), pc(V['Base']['vs_price'], 0, True)], ["Bull", f0(bull_v), pc(V['Bull']['vs_price'], 0, True)]], "kv")}</div>
<div class="rbox"><p class="rh">Key data, 9 Nov 2026</p>
{table(["Item", "Value"], [
    ["Price (after 1:1 bonus)", "Rs 594"],
    ["Market value", f"Rs {f0(CALC['mcap'])} cr"],
    ["52-week range", "Rs 494 - 808"],
    ["Sales, last 12 months", "Rs 1,170 cr"],
    ["Profit, last 12 months", "Rs 279 cr"],
    ["P/E, last 12 months", f"{f1(VAL['cross_checks']['pe_ttm'])}x"],
    ["Cash less debt", f"Rs {f0(CALC['net_cash'])} cr"],
    ["Promoter holding", "44.09%"],
    ["Management verdict", "WATCH"]], "kv")}</div>
<div class="rbox"><p class="rh">Dates to watch</p>
<p class="tiny">Q3 FY27 results: about mid-Feb 2027 (past Q3 calls: 9 Feb 2024, 14 Feb 2025, 12 Feb 2026).<br>FY27 results: about end-May 2027 (past: 28 May 2024, 30 May 2025, 1 Jun 2026).</p></div>
</aside>"""

annual = C.bars(D["years"] + ["TTM"], D["sales"] + [D["sales_ttm"]], "Annual sales FY20 to TTM",
                highlight={6, 7}, w=460, h=230, hatch=set(), notes={5: "bulk Q4"})
annual_pat = C.bars(D["years"] + ["TTM"], D["pat"] + [D["pat_ttm"]], "Annual profit after tax FY20 to TTM",
                    highlight={6, 7}, w=460, h=230)

s1_main = f"""<p class="lede">Concord Biotech makes complex drug ingredients by fermentation, the way beer or yoghurt is made but in steel tanks under drug-plant rules.
Few companies can do this well, which is why it earned 40%+ operating margins for years.</p>
<p>In FY26 sales fell 12% and profit 30%, the first fall since listing.
This report answers one question first: <b>was FY26 a pause or a step down?</b>
Our answer: <b>a pause in volumes, but a step down in margin that has not yet reversed.</b>
Half-year sales are back up {pc(CALC['h1_growth'])}, led by ingredient (API) sales up {pc(CALC['api_h1_g'])}.
But margin is 33-34% against 42% two years ago, part of the recovery was won with lower prices, and two new businesses (injectables and a US sales arm) still lose money.</p>
<p>At Rs 594 the market is paying about {f1(VAL['cross_checks']['pe_ttm'])} times the last year's profit.
That price needs close to management's full plan: about 19% sales growth a year and margins back to 38% by FY29.
For FY27 alone, 19% growth needs second-half sales of about Rs {f0(n19)} cr, {pc(n19g, 0, True)} on last year's second half.</p>
<p>Management has met 10 of 23 promises that have come due across 14 earnings calls.
It is open about what went wrong but late on timing, so we rate it WATCH, not RED.</p>"""
s1_charts = duo(exhibit("Sales fell in FY26 after six years of growth (Rs cr)", annual, src("scr"), "FY25 was lifted by a Rs 430 cr fourth quarter of bulk buying; see S8."),
                exhibit("Profit fell 30% in FY26 and is recovering slowly (Rs cr)", annual_pat, src("scr")))

s1_body = f'<div class="cover"><div class="cmain">{s1_main}</div>{rail}</div>{s1_charts}'
section("s1", "A", "Why read this", "S1 | Summary", "A strong niche business on a pause, priced for a full recovery",
        f"Concord is a high-quality fermentation API maker; FY26 looks like a pause in buying, not lost customers, but the margin has not come back and the price already assumes it will.",
        s1_body,
        f"The share is priced near our base value (Rs {f0(base_v)}), so most of the good outcome is already paid for. "
        f"The useful thing to track is not the story but three numbers: second-half FY27 sales against Rs {f0(n19)} cr, the margin against 38%, and whether injectable contracts are signed by the FY27 results in late May 2027.")

# ================================================================= S2 business simply
p = CALC["per100"]
wf = C.waterfall([("Sales", 100, "total"), ("Operating|costs", 100 - p["ebitda"], "down"), ("EBITDA", p["ebitda"], "total"),
                  ("Depreciation|and interest", p["dep_int"], "down"), ("Other|income", p["oi"], "up"),
                  ("Profit before|tax", p["pbt"], "total"), ("Tax and|minorities", p["pbt"] - p["pat"], "down"),
                  ("Profit|after tax", p["pat"], "total")], "What happens to Rs 100 of FY26 sales", dec=1, w=760, h=260)
chain = flow([
    ("1. Strain", ["A microbe (bacteria or fungus) that naturally makes the molecule. <small>Concord has its own strains.</small>"], False),
    ("2. Ferment", ["Microbes grow in steel tanks for days. <small>1,250 m3 of tanks at Dholka and Limbasi.</small>"], True),
    ("3. Purify", ["The molecule is extracted and cleaned to drug grade. <small>The hard, yield-driving step.</small>"], False),
    ("4. API", ["Sold by the kg to drug makers. <small>About 79-83% of sales.</small>"], True),
    ("5. Dossier", ["A DMF (drug master file) is lodged with the regulator; the buyer's approval names Concord as source. <small>150+ DMFs.</small>"], False),
    ("6. Medicine", ["Tablets, capsules or injections, made by the customer or by Concord's own Units II and IV. <small>17-21% of sales.</small>"], False),
])
milestones = [("1984", "Company incorporated in Gujarat"), ("FY2000", "Unit I Dholka, 450 m3 fermentation"),
              ("FY2016", "Unit II Valthera, tablets and capsules; Quadria invests (about 20%)"),
              ("FY2021", "Unit III Limbasi, 800 m3, about Rs 400 cr"), ("Aug 2023", "IPO: Quadria sells at Rs 741, no new money raised"),
              ("FY2025", "Unit IV injectables commissioned"), ("Jul 2025", "Stellon Biotech, US sales arm (75%)"),
              ("Nov 2026", "1:1 bonus; 20.92 cr shares")]
tl = '<div class="tl">' + "".join(f'<div class="tli"><span class="tly">{y}</span>{t}</div>' for y, t in milestones) + "</div>"
geo_chart = C.hbars(list(D["geo"].keys()), list(D["geo"].values()), "FY26 sales by market", unit="", w=460,
                    notes={i: f"({pc(CALC['geo_chg'][k], 1, True)})" for i, k in enumerate(D["geo"])})
gloss = [("API", "Active pharmaceutical ingredient: the chemical in a medicine that does the work."),
         ("Fermentation", "Making a molecule by growing microbes that produce it, instead of building it by chemistry."),
         ("DMF", "Drug master file: a confidential file on how an API is made, lodged with a regulator and cited by the buyer."),
         ("ANDA", "Abbreviated new drug application: US approval to sell a generic medicine."),
         ("KSM", "Key starting material: an input made before the final API step."),
         ("CDMO", "Contract development and manufacturing: making a molecule for one innovator company."),
         ("NCE", "New chemical entity: a new, patented drug."),
         ("Immunosuppressant", "A drug that calms the immune system, used after organ transplants (Tacrolimus, MMF)."),
         ("483 / EIR", "US FDA inspection findings (Form 483) and the report that closes an inspection (EIR)."),
         ("EBITDA", "Operating profit before depreciation, interest and tax."),
         ("Utilisation", "How much of a plant's capacity is used."),
         ("Working capital", "Cash tied up in stock and unpaid bills, less what the company owes suppliers."),
         ("P/E", "Price to earnings: share price divided by profit per share."),
         ("TTM", "Trailing twelve months: the latest four quarters."),
         ("[E] and [G]", "[E] is our estimate or calculation; [G] is management guidance.")]
glossary = '<dl class="gl cols2">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in gloss) + "</dl>"

s2 = f"""<h3>The revenue equation</h3>
<p class="eq">Sales = tank capacity used &times; batches a year &times; kg per batch &times; price per kg, across 30+ molecules, plus finished medicines made from those APIs.</p>
<p>Every term matters. Capacity is fixed until a new plant is built. Yield per batch comes from years of process know-how. Price depends on how many other approved makers a buyer can switch to, usually two or three.</p>
{exhibit("Out of Rs 100 of FY26 sales, Rs 24.6 was profit and Rs 16.3 was free cash", wf, src("scr", ("ar26", 233)) + " Our calculation from FY26 consolidated figures.",
         f"Cash view [E]: operating cash flow Rs {f1(p['cfo'])}, capex Rs {f1(p['capex'])}, free cash flow Rs {f1(p['fcf'])} per Rs 100 of sales. A split of operating costs into materials, staff and other is in the annual report but not extracted here.")}
<h3>How it makes money</h3>
{table(["Line", "What is sold", "To whom", "Share of sales"], [
    ["API", "Fermentation ingredients by the kg", "Generic drug makers in 70+ countries", "79% FY26; 83% H1 FY27"],
    ["Formulations", "Tablets, capsules (Unit II); own brands in India; partner supply in emerging markets and the US", "Distributors, hospitals, partners; US via ANDAs", "21% FY26; 17% H1 FY27"],
    ["Injectables", "Vials from Unit IV", "Contract and government buyers; no contract signed yet", "Not disclosed (plant at 5%)"],
    ["CDMO", "One molecule made exclusively for an innovator", "One unnamed partner", "About USD 2 mn a year"]], "std")}
<p class="small">Contract terms: the only terms disclosed are that API supply runs against Concord's DMF and that the CDMO project makes Concord the exclusive supplier of a new drug. Contract length, minimum volumes and price-reset clauses are not disclosed.</p>
<h3>From microbe to medicine</h3>
{exhibit("The fermentation value chain: Concord earns most at steps 2 to 4", chain, src(("deck27", 7), ("tr27", 4)), "Shaded steps are where most of the value and the difficulty sit.")}
<h3>Why this business is hard to copy</h3>
{ul(["<b>A DMF ties a customer in.</b> A generic maker's approval names its API source. Switching means new testing and a filing change, which takes time and money [judgment], so suppliers are rarely dropped for small price gaps.",
     "<b>Fermentation is slow to start.</b> A new plant needs strains, years of process tuning and large tanks; Limbasi alone cost about Rs 400 cr (Q1 FY24 call).",
     "<b>The market grows slowly; Concord grows by winning second-source slots.</b> Management puts immunosuppressant market growth at about 10% a year and says its own growth comes from becoming a buyer's second supplier (Q2 FY27 call)."])}
<h3>Where it sells</h3>
{duo(exhibit("India is half of sales; the US fell fastest in FY26 (Rs cr, change vs FY25)", geo_chart, src(("ar26", 247)),
             "India includes Middle East formulation supply routed through Indian partners (Q4 FY26 call p15)."),
     '<figure class="ex"><figcaption>Milestones</figcaption>' + tl + '<p class="src">' + src(("deck27", 7), ("ar26", 56), "rhp", "bonus")[8:] + '</p></figure>')}
<h3>Glossary</h3>{glossary}"""
section("s2", "A", "The business simply", "S2 | The business", "A microbe, a tank and a regulatory file: why this niche pays well",
        "Concord grows microbes in tanks to make hard-to-make drug ingredients, sells them by the kg to generic drug makers, and keeps customers because switching suppliers needs a new regulatory filing.",
        s2,
        "This is a quality niche, not a commodity chemical maker. The risk is not that customers leave overnight; it is that price is used to win new slots, which lowers margins slowly. Watch gross margin each quarter.")

# ================================================================= S3 molecules
fam = [
    ("Immunosuppressants", "Tacrolimus, MMF, MPS, Cyclosporine, Sirolimus, Pimecrolimus, Everolimus premix, Voclosporin", "MAKES AND SELLS",
     "The core franchise. Revenue by molecule is not disclosed."),
    ("Oncology", "Temsirolimus, Everolimus, Romidepsin, Mitomycin, Dactinomycin, Midostaurin", "MAKES AND SELLS",
     "Nearly doubled in H1 FY27; Romidepsin up on customer US launches (Q2 FY27 call)."),
    ("Anti-bacterials", "Mupirocin, Polymyxin B, Teicoplanin, Vancomycin, Fidaxomicin; Fusidic acid", "MAKES AND SELLS",
     "US DMF filed for Fidaxomicin. Fusidic acid is launching (FIRST ORDERS)."),
    ("Anti-fungals", "Anidulafungin, Caspofungin, Micafungin, Amphotericin B; Nystatin", "MAKES AND SELLS",
     "Nystatin is qualified with US customers on validation quantities only (FIRST ORDERS)."),
    ("Statins", "Lovastatin, Pravastatin", "MAKES AND SELLS", "Older, cholesterol molecules."),
    ("US generics (ANDAs)", "12 approved ANDAs, 7 marketed; Tofacitinib and MMF oral suspension approved in Q2 FY27", "MAKES AND SELLS",
     "US business moving from partner Advergent to Stellon."),
    ("Injectables (Unit IV)", "Vials and lyophilised products", "IN DEVELOPMENT",
     "Plant built and WHO-GMP certified; 5% used; contracts 'expected in H2' FY27."),
    ("Dermatology brand (Inspira)", "Own-brand India skin products", "FIRST ORDERS",
     "Launched Q2 FY27; India market about Rs 5,000 cr; Rs 400-500 cr needs 4-5 years [G]."),
    ("CDMO", "One new drug for one innovator", "FIRST ORDERS", "About USD 2 mn a year; aim of 1-4% of FY27 sales [G]."),
    ("Pipeline", "10+ products, 22+ non-infringing processes", "NOT DISCLOSED", "Names and timing not disclosed."),
]
cards = '<div class="cards">' + "".join(
    f'<div class="card"><p class="ct">{n}</p><p class="cs">{chip(st)}</p><p class="cm">{m}</p><p class="cn">{note}</p></div>'
    for n, m, st, note in fam) + "</div>"
s3 = f"""<p>Concord lists more than 30 fermentation APIs across five families, plus finished medicines.
The table below shows what it makes today, what is just starting and what is not disclosed.</p>
{cards}
<p class="src">{src(("deck27", 8), ("tr27", 4), ("tr27", 7), ("tr426", 4))[8:]}</p>
<h3>The biggest threat: price, not a lost product</h3>
<p>Management says FY26 was "not related to lower demand, loss of market share or pricing pressure" (Q4 FY26 call p4).
But in Q1 FY27 it said share gains were "primarily driven by pricing" (Q1 FY27 call p10), and gross margin fell from 79.1% to 77.4% in H1 FY27.
Competition is two or three makers per product, mostly European and Southeast Asian; management says China is not a major rival in its molecules (Q2 FY25 call p9).
A second threat is quieter: emerging-market customers are buying the API and making their own tablets instead of buying Concord's tablets, which is why formulation sales fell {pc(-CALC['form_h1_g'])} in H1 FY27.</p>
<p class="small">Not disclosed: sales by molecule, the share of immunosuppressants in revenue, and the largest customer. We do not estimate them.</p>"""
section("s3", "A", "Molecule portfolio", "S3 | Products", "Thirty molecules in five families, with new launches still small",
        "Concord's sales rest on immunosuppressants and a widening set of oncology, anti-infective and anti-fungal molecules; the newer bets (injectables, a skin brand, CDMO) are real but tiny today.",
        s3,
        "Do not pay for the new bets yet. They are worth something only when they show up as revenue lines in the decks. Oncology doubling is the most concrete new driver so far.")

# ================================================================= S4 segments and entities
seg = C.grouped(D["seg_years"], [("API", D["api"], C.PRIMARY), ("Formulations", D["form"], C.SECOND)],
                "API and formulation sales FY23 to FY26", w=460, h=240)
segh1 = C.grouped(["H1 FY26", "H1 FY27"], [("API", D["api_h1"], C.PRIMARY), ("Formulations", D["form_h1"], C.SECOND)],
                  "API and formulation sales H1 FY26 vs H1 FY27", dec=1, w=460, h=240)
ent = table(["Entity", "Stake", "What it does", "FY26 numbers"], [
    ["Concord Biotech Ltd", "Parent", "All four plants, all APIs and formulations", "Almost all group sales"],
    ["Stellon Biotech Inc. (US)", "75%", "US sales and marketing front end, from Jul 2025", ("Nil sales; loss Rs 7.2 cr; owes Concord Rs 14.6 cr", "flag")],
    ["Concord Biotech Japan K.K.", "50% JV", "Sells into Japan", "Bought Rs 29.1 cr from Concord"],
    ["Concord Lifegen Ltd", "100%", "New Indian subsidiary, Jul 2025", "Sales Rs 0.4 cr"],
    ["Clean Max Everglades", "26%", "Captive power supply", "Investment Rs 0.8 cr"],
    ["Celliimune Biotech", "100% from Apr 2026", "Cell and gene therapy start-up, bought from a director", "Rs 0.66 cr price"]], "std",
    caption="Group entities: one parent does the work; the US arm is the one to watch", source=src(("ar26", 56), ("ar26", 79), ("ar26", 244)))
s4 = f"""<p>The company reports one segment in its accounts, but the decks split sales into API and formulations.
API fell 11.8% in FY26 and rebounded {pc(CALC['api_h1_g'])} in H1 FY27. Formulations fell 13.0% in FY26 and another {pc(-CALC['form_h1_g'])} in H1 FY27.</p>
{duo(exhibit("API carried FY24-FY25 growth and the H1 FY27 rebound (Rs cr)", seg, src("decks")),
     exhibit("In H1 FY27 API rose 36%, formulations fell 8% (Rs cr)", segh1, src(("deck27", 10))))}
<h3>Margin with and without the start-ups</h3>
<p>Management now reports a second margin that leaves out the injectables plant and Stellon.
In Q2 FY27 it was 37.1% against 33.8% reported; for H1 FY27, 37.8% against 33.0%; for FY26, 39% against 35% (Q2 FY27 call p5, p7; Q4 FY26 call p5).
That gap is about Rs {f0(CALC['adj_gap_fy26'])} cr of EBITDA in FY26 and Rs {f0(CALC['adj_gap_h1'])} cr in H1 FY27 [E].
But the adjusted margin itself fell from 41% in Q2 FY26 to 37.1% in Q2 FY27, so the core business is also earning less, not only the start-ups.</p>
{ent}"""
section("s4", "A", "Segments and entities", "S4 | Segments", "The API engine is back; formulations and the start-ups are holding margins down",
        f"API sales (83% of H1 FY27) are growing again, formulations are shrinking, and the two start-ups cost about 4 margin points; even without them the core margin is 37%, below the 38-40% guide.",
        s4,
        "Judge FY27 on two numbers the company now gives every quarter: reported margin and the margin without start-ups. If both rise together, the recovery is real. If only the adjusted one rises, the start-ups are still bleeding.")

# ================================================================= S5 customers
top10 = C.bars(list(D["top10"].keys()), list(D["top10"].values()), "Top-10 customer share of sales FY22 to FY26",
               unit="%", dec=1, highlight={4}, w=460, h=230)
s5 = f"""{duo(exhibit("Top-10 customers fell from 48% to 38% of sales in four years", top10, src(("deck27", 23))),
     '<div><h3>Who buys</h3>' + ul(["300+ customers in 70+ countries; no single customer is above 10% of sales in FY26 or FY25 (annual report p247).",
        "The 50% Japan joint venture bought Rs 29.1 cr in FY26, 2.8% of sales, and is the only named related customer (annual report p244).",
        "The largest customer is not named. Customer churn is not disclosed."]) +
     '<h3>Who partners</h3>' + ul(["<b>Advergent</b>: the US partner for Concord's ANDA products; the business is moving to Concord's own Stellon (Q2 FY27 call p4).",
        "<b>Stellon Biotech</b>: 75% owned US arm; commercial operations began Q1 FY27; contribution now expected in H2 FY27, one half later than first said.",
        "<b>CDMO partner</b>: one unnamed innovator; Concord is the exclusive supplier of its new drug, about USD 2 mn a year."]) + '</div>')}"""
section("s5", "A", "Customers and partners", "S5 | Customers", "No customer is big enough to hurt; the US hand-over is the open question",
        "Customer risk is low and falling: the top 10 buy 38% of sales and none buys more than 10%; the open item is the hand-over of US formulation sales from Advergent to Stellon.",
        s5,
        "A lost customer is unlikely to sink the year. A slow Stellon start would, at the margin, keep US formulation sales weak; check that Stellon shows revenue in the H2 FY27 numbers.")

# ================================================================= S6 moat & competition
peers = D["peers"]
opm_chart = C.hbars([p_[0] for p_ in peers], [p_[7] for p_ in peers], "Operating margin, trailing twelve months, peers",
                    unit="%", w=460, highlight={0}, lab_w=150)
s6 = f"""<p>Three things protect Concord: 1,250 m3 of fermentation tanks that took 20 years to build, 150+ drug master files that tie customers in, and a cost position that still gives the best margin among Indian API makers except Divi's.</p>
{duo(exhibit("Concord still earns one of the highest margins among listed API makers", opm_chart, src("peers"), "Divi's leads on the last twelve months; Concord led in FY25 (42%)."),
     '<div><h3>Competition, as management describes it</h3>' + ul([
        "Two or three makers per product (Q3 FY26 call p14).",
        "Only one other fermentation company competes on four or five of its molecules (Q1 FY25 call p11).",
        "Rivals are mainly European and Southeast Asian; little from China (Q2 FY25 call p9).",
        "Biocon is the listed Indian rival in immunosuppressants; it is not a clean comparison because most of its business is biosimilars.",
        "Independent market-share data was not found; the share gain claims are management's."]) + '</div>')}
{table(["What protects the business", "What the moat did not stop"], [
    ["Customers name Concord in their filings, so switching is slow", "A 12% sales fall in FY26 when customers simply bought less"],
    ["Fermentation know-how and scale (1,250 m3)", "Price cuts to win share in Q1 FY27; gross margin down 1.7 points in H1"],
    ["150+ DMFs and 30+ APIs spread the risk", "Customers switching from Concord's tablets to buying its API"],
    ["Debt-free with Rs 445 cr of cash and liquid funds", "Three straight years without the promised 25% growth"]], "std two")}"""
section("s6", "A", "Moat and competition", "S6 | Moat", "The moat protects customers, not prices",
        "Concord's moat is real: few rivals, sticky customers and top-tier margins; but it did not prevent a volume fall in FY26 or price cuts in FY27.",
        s6,
        "Treat the moat as protection against collapse, not as a promise of 40%+ margins. The bear case in S20 keeps margins at 33-34% for this reason.")

# ================================================================= S7 quantity vs quality
roce = C.lines(D["years"][1:], [("ROCE", D["roce"][1:], C.PRIMARY, False), ("Operating margin", D["opm"][1:], C.SECOND, False)],
               "Return on capital and operating margin FY21 to FY26", unit="%", w=460, h=240, ymin=0, ymax=80, all_labels=True, end_labels=False)
fat = C.bars(D["years"], [round(x, 2) for x in CALC["fat"]], "Sales per rupee of fixed assets FY20 to FY26", dec=2, unit="x",
             highlight={6}, w=460, h=240)
s7 = f"""<p>Growth is only worth paying for if it comes with good returns. Concord's growth from FY21 to FY25 did: return on capital stayed at 26-32% outside FY22.
In FY26 return on capital fell to 17% and margin to 35%, because sales fell while the new plants added fixed costs.</p>
{duo(exhibit("Returns halved in FY26 as sales fell onto a larger cost base (%)", roce, src("scr")),
     exhibit("Each rupee of plant now earns less sales than before Unit IV was built (x)", fat, src("scr"), "Our calculation: sales divided by net fixed assets [E]. FY21 fell as Limbasi was added; FY25-FY26 fell as Unit IV was added."))}
<p>Quality of the growth that is coming back: H1 FY27 sales rose 26%, EBITDA 25% and profit 19%. Profit grew slower than sales because gross margin fell (solvents, power and fuel, product mix, and price), and other income fell.</p>"""
section("s7", "A", "Quantity vs quality", "S7 | Growth quality", "Growth is back, but it is lower-quality growth than before",
        "The H1 FY27 rebound is mostly volume and currency with some price cuts, so profit grew 19% on 26% sales growth; returns will recover only when Units III and IV fill up.",
        s7,
        "Look past headline sales growth. The number that tells you quality is back is gross margin returning towards 79-80%; it was 76.2% in Q2 FY27.")

# ================================================================= S8 pause or step down
hy = C.bars(["H1 FY25*", "H2 FY25", "H1 FY26", "H2 FY26", "H1 FY27", "H2 FY27 need"],
            [round(CALC["h1fy25"]), CALC["h2fy25"], 451.1, 603.9, 566.6, round(n19, 1)],
            "Half-year sales and the H2 FY27 sales a 19% year needs", dec=0, hatch={5}, highlight={4, 5}, w=760, h=250,
            value_labels=[f0(CALC["h1fy25"]), "674", "451", "604", "567", f"{f0(n19)} [G path]"])
q4 = C.bars(D["q4"], D["q4_sales"], "Fourth-quarter sales FY23 to FY26", dec=0, highlight={2}, w=460, h=230,
            notes={2: "+35%"})
qs = C.bars(D["ql"], D["q_sales"], "Quarterly sales, last eight quarters", highlight={6, 7}, w=460, h=230)
reasons = table(["Reason given (call)", "Size given", "Where it stands"], [
    ["EU sales blocked by a delayed Indian export certificate (Q2 FY26)", "Rs 20-25 cr", "Resolved"],
    ["Middle East government tender deferred by conflict (Q2 FY26)", "About Rs 20 cr", "Still 'in abeyance' at Q4 FY26"],
    ["US buyers paused on tariff fears (Q2 FY26)", "Not given", "Orders said to be back to normal"],
    ["Customers moved from bulk to quarterly buying (Q4 FY26)", "Not given", "Called a timing effect"],
    ["US Veterans Affairs tender not finalised (Q4 FY26)", "Not given", "On hold"],
    [("Total explained vs the fall", "bold"), ("Rs 40-45 cr of Rs 145 cr", "bold"), ("About Rs 100 cr unexplained", "flag")]], "std",
    caption="Management's reasons for FY26 explain less than a third of the fall in numbers", source=src(("tr226", 5), ("tr426", 4), "ledger"))
pause = table(["Evidence for a pause", "Evidence for a step down"], [
    ["H1 FY27 API sales +36%; trailing sales Rs 1,170 cr, above FY24's Rs 1,017 cr", "Margin 33-34% vs 42% in FY24-FY25, and the core (adjusted) margin is also lower"],
    ["Q4 FY26 (Rs 326 cr) is back to the Q4 FY24 level; Q4 FY25 (Rs 430 cr) was the odd one out", "Share gains in Q1 FY27 were 'primarily driven by pricing'"],
    ["No customer loss or lost product reported; top-10 share stable", "Formulations fell again in H1 FY27 (-8%)"],
    ["Inventory built for delayed shipments (Q4 FY26 call p15)", "About Rs 100 cr of the fall has no quantified reason"]], "std two")
s8 = f"""<p>Start with what FY25 really was. Its fourth quarter (Rs 430 cr) was 35% above the year before, mostly in domestic API sales.
In FY26, management said customers moved away from "bulk purchases" compared with the previous year (Q4 FY26 call p4).
So FY25 included front-loaded buying, and FY26 paid for it. Taken together, FY24 to FY26 sales grew {pc(CALC['cagr_24_26'], 1)} a year.</p>
{exhibit("The second half of FY27 has to beat last year's by 14% for a 19% year (Rs cr)", hy, src("scr", ("deck27", 10)) + " *H1 FY25 is our calculation: FY25 sales less Q3 and Q4.",
         f"Hatched bar: the H2 FY27 sales needed for 19% growth on FY26 [E]. For 18% growth it is Rs {f0(CALC['need18'])} cr ({pc(CALC['need18_g'], 0, True)}); for 20%, Rs {f0(n20)} cr ({pc(n20g, 0, True)}).")}
{duo(exhibit("Q4 FY25 was the outlier, not Q4 FY26 (Rs cr)", q4, src("decks")),
     exhibit("Quarterly sales are climbing back (Rs cr)", qs, src("scr")))}
{reasons}
<h3>Pause or step down: the evidence both ways</h3>
{pause}"""
section("s8", "A", "FY26: pause or step down", "S8 | The FY26 fall", "A pause in volume, a step down in margin",
        f"Volumes look like a pause: API sales are growing again and the trailing year (Rs 1,170 cr) is back above FY24; but margin and pricing have stepped down and have not yet recovered.",
        s8,
        f"The test comes in two results. If H2 FY27 sales reach about Rs {f0(n19)} cr and gross margin stops falling, FY26 was a pause. If H2 sales come in near last year's Rs 604 cr, treat FY25 as a peak and the growth story as a step down.")

# ================================================================= S9 capacity and capex
util = C.hbars(list(D["util_q2fy27"].keys()), list(D["util_q2fy27"].values()), "Plant utilisation Q2 FY27",
               unit="%", w=460, max_v=100, track=True, lab_w=190)
uh = C.lines(D["util_hist_cats"], [("Unit I Dholka", D["util_u1"], C.PRIMARY, False), ("Unit III Limbasi", D["util_u3"], C.SECOND, False),
                                   ("Unit II Valthera", D["util_u2"], C.THIRD, False)],
             "Plant utilisation by call", unit="%", w=760, h=250, ymin=0, ymax=100)
cap = C.grouped(D["years"], [("Operating cash flow", D["cfo"], C.PRIMARY), ("Capex [E]", CALC["capex"], C.SECOND),
                             ("Depreciation", D["dep"], C.GREY)], "Operating cash flow, capex and depreciation FY20 to FY26", w=760, h=250)
plants = '<div class="plants">' + "".join(
    f'<div class="plant"><p class="pn">{n}</p><p class="pl">{loc}</p><p class="pc">{c}</p><p class="pu">{u}</p><p class="pr">{r}</p></div>'
    for n, loc, c, u, r in [
        ("Unit I", "Dholka, Gujarat | FY2000", "450 m3 fermentation API", "Used: 75%", "USFDA: 483 observations at Q4 FY25, then EIR (closed)"),
        ("Unit III", "Limbasi, Gujarat | FY2021", "800 m3 fermentation API; 160-acre site, 20-25% used", "Used: 55% (20-25% without KSMs, analyst)", "USFDA: zero observations, Jun 2023; ANVISA approval Q2 FY27"),
        ("Unit II", "Valthera, Gujarat | FY2016", "869 mn tablets and capsules a year", "Used: 21%", "USFDA: one minor procedural observation, Q2 FY27"),
        ("Unit IV", "Valthera, Gujarat | FY2025", "13 mn liquid vials, 12 mn powder vials, 2,200 kg lyophilised", "Used: 5%", "WHO-GMP only; no USFDA inspection disclosed")]) + "</div>"
capex_t = table(["When said", "Capex guidance", "What happened"], [
    ["Q3 FY25", "Maintenance only, Rs 15-20 cr a year", "Superseded"],
    ["Q4 FY25", "Maintenance Rs 20-30 cr", ("FY26 capex Rs 65 cr (call); Rs 95 cr cash basis [E]", "flag")],
    ["Q3 FY26", "Maintenance restated to Rs 30-40 cr", "Restated up"],
    ["Q4 FY26", "FY27 general capex Rs 20-30 cr", "Q1 FY27 capex Rs 9.5 cr"],
    ["Q2 FY27", "Rs 20-30 cr plus Rs 50-60 cr in each of FY27 and FY28", "Raised two quarters after the last guide"],
    ["Q1 FY27", "New API capacity at Unit III once it reaches 80-85%", "Unit III at 55%"]], "std",
    caption="Capex guidance has moved up four times in two years", source=src("ledger", ("tr27", 13), ("tr127", 14)))
s9 = f"""<p>Concord has four plants in Gujarat. The two fermentation plants make almost all the API; the two Valthera plants make finished medicines and are mostly empty.</p>
<figure class="ex"><figcaption>Exhibit 0: Four plants, two of them mostly idle</figcaption>{plants}<p class="src">{src(("deck27", 9), ("tr27", 19), ("tr127", 14), ("tr425", 5), ("deck226", 5))[8:]}</p></figure>
{duo(exhibit("Unit III has room to grow; Units II and IV are mostly empty (% used)", util, src(("tr27", 19))),
     '<div><h3>When is the next fermentation plant needed?</h3><p>Management will add capacity at Limbasi once Unit III reaches 80-85%.'
     f' At 18% API growth, Unit III goes from 55% to 80% in about {f1(CALC["unit3_80_years"])} years [E], so a new block is a FY29-FY30 decision.'
     ' If the analyst estimate of 20-25% without KSMs is right, it is later.</p>'
     '<p><b>Absence test:</b> no new fermentation capacity beyond 1,250 m3 has been announced. Management says Limbasi could earn Rs 1,500-1,600 cr at peak against about Rs 600 cr from Dholka (Q1 FY24 call), so the existing tanks can carry the plan to FY29.</p></div>')}
{exhibit("Utilisation as stated on each call: Dholka steady near 75-84%, Limbasi rising unevenly (%)", uh, src("ledger"), "Unit II's 50% in H1 FY25 was confirmed on the call but sits far above the readings either side. Unit IV first reported at 5% in Q2 FY27.")}
{exhibit("Operating cash has paid for every year's capex since FY22 (Rs cr)", cap, src("scr"), "Capex is operating cash flow less free cash flow on Screener [E]; it differs from the Rs 65 cr management gave for FY26.")}
{capex_t}"""
section("s9", "A", "Capacity and capex", "S9 | Capacity", "The tanks for FY29 already exist; the empty plants are the drag",
        "There is enough fermentation capacity for the guided plan to FY29; the issue is two finished-dose plants running at 5% and 21%, which add costs before they add sales.",
        s9,
        "This lowers one risk: Concord does not need a big new plant to grow, so cash will build. It raises another: depreciation is already up from Rs 54 cr to Rs 74 cr, and it only pays off if Unit IV fills.")

# ================================================================= S10 management
tone = table(["Calls", "Tone [judgment]", "What drove it"], [
    ["Q1 FY24 to Q4 FY25 (8 calls)", "BULLISH", "18% growth delivered; 25% CAGR target introduced and repeated"],
    ["Q1 FY26, Q3 FY26", "CAUTIOUS", "Sales falling; 25% re-labelled 'not guidance'"],
    ["Q2 FY26, Q4 FY26", "DEFENSIVE", "Reasons listed for the fall; H2 recovery promised and missed"],
    ["Q1 FY27, Q2 FY27", "CAUTIOUSLY OPTIMISTIC", "H1 +26%; guide 'slightly better than 18%'; pushback from analysts"]], "std",
    caption="Call tone across 14 calls", source=src("ledger"))
idx = C.bars(["Profit after tax", "Top pay (KMP and relatives)", "Median employee pay"], [70, 102, 108.6],
             "FY26 vs FY25, indexed to FY25 = 100", dec=0, colors=[C.GREY, C.SECOND, C.PRIMARY], w=460, h=230,
             value_labels=["70", "102", "109"])
people = table(["Person", "Role", "Note"], [
    ["Sudhir Vaid", "Chairman and MD; founder", "Holds 28.84%; FY26 pay Rs 7.07 cr, 111.9x the median employee"],
    ["Ankur Vaid", "Joint MD and CEO", "Runs the calls; FY26 pay Rs 3.91 cr, 66.3x median"],
    ["Raviraj Karia", "CFO from 18 Dec 2025", "Replaced Lalit Sethi (left 5 Jan 2026); no reason given"],
    ["Company Secretary", "Three in 12 months", "Prakash Sajnani, Hina Patel, Paritosh Trivedi"]], "std")
s10 = f"""{people}
<p class="src">{src(("ar26", 243), ("ar26", 244), ("ar26", 61))[8:]}</p>
{tone}
{duo(exhibit("Profit fell 30%; top pay rose 2%; staff pay rose 9% (FY25 = 100)", idx, src(("ar26", 61), ("ar26", 244)),
             f"Top pay is all key managers plus relatives employed, Rs 14.05 cr, {f1(CALC['kmp_pct_pat'])}% of FY26 profit [E]. The two MDs took no raise."),
     '<div><h3>Capital decisions</h3>' + ul([
        f"<b>Cash pile:</b> Rs {f0(CALC['inv_book_sep26'])} cr of investments at Sep-26 (mutual funds plus Rs 96 cr non-current, including Palvella Therapeutics, a listed US stock). Earns other income, but lowers return on capital.",
        "<b>Dividends:</b> about 30% of profit paid out in FY23, FY24 and FY26.",
        "<b>Bonus:</b> 1:1 bonus allotted 4 Nov 2026. It changes the share count, not the value.",
        "<b>IPO:</b> the Aug 2023 IPO was entirely Quadria Capital selling at Rs 741; the company raised no money. The price is now Rs 594 after the bonus, or Rs 1,188 on the old share count.",
        "<b>Promoters</b> hold 44.09%, unchanged for eight quarters; no sale since listing."]) + '</div>')}"""
section("s10", "B", "Management", "S10 | Management", "Open about the facts, late on the timing",
        "Management explains problems clearly and has not sold shares, but its growth and margin targets have repeatedly slipped and been re-labelled rather than withdrawn; our verdict is WATCH.",
        s10,
        "Discount the medium-term targets (25% CAGR, Rs 3,000 cr) and take the facts (plant status, inspections, product launches) at face value. That is how the base case in S20 treats them: guidance is used, but no higher.")

# ================================================================= S11 ledger
areas = ["Annual growth", "25% CAGR path", "Margin", "Injectables", "Capex", "CDMO, Stellon, products, mix, tax"]
met = [3, 0, 1, 2, 0, 4]
miss = [3, 1, 2, 4, 1, 2]
score = C.grouped(["Growth", "25% path", "Margin", "Injectables", "Capex", "Other"], [("Met", met, C.PRIMARY), ("Missed or late", miss, C.SECOND)],
                  "Promises met vs missed by area", w=760, h=230)
L = [("G3", "Q3 FY24", "25% CAGR over five years", "FY24-FY26 CAGR 1.9%", "MISSED"),
     ("G4", "Q1 FY25", "Meet the annual guide (18%)", "FY25 +18.0%", "MET"),
     ("G6", "Q4 FY25", "'No specific guidance'; built for 25%", "FY26 -12.1%", "MISSED"),
     ("G8", "Q2 FY26", "Stronger H2 FY26", "H2 Rs 604 cr vs Rs 674 cr", "MISSED"),
     ("G9", "Q2 FY26", "25% 'is not guidance'", "Target re-labelled", "SOFTENED"),
     ("G12", "Q2 FY27", "FY27 'slightly better than 18%'", f"Needs H2 of Rs {f0(n19)} cr", "OPEN"),
     ("G13", "Q4 FY26", "Rs 3,000 cr peak in 5-6 years", "Needs about 19-20% a year", "OPEN"),
     ("M3", "Q3 FY25", "Margin 40-43% long term", "FY26 35%; TTM 34%", "MISSED"),
     ("M6", "Q2 FY27", "Margin 38-40% 'over the next few years'", "Lowered from 40-43%", "SOFTENED"),
     ("I1", "Q1 FY24", "Injectables commercial by Q1 FY25", "Commissioned Q4 FY25", "LATE"),
     ("I8", "Q4 FY25", "Injectables about Rs 300 cr in 3-4 years", "5% used; no contract yet", "OPEN"),
     ("C2", "Q4 FY25", "Only maintenance capex, Rs 20-30 cr", "FY26 Rs 65 cr", "MISSED"),
     ("S2", "Q4 FY26", "Stellon supplies in H1 FY27", "Now 'expected in H2'", "LATE"),
     ("P1", "Q1 FY24", "One or two new molecules a year", "Nystatin, Voclosporin in FY25", "MET"),
     ("X1", "Q4 FY24", "API to formulation mix 80:20", "79:21 in FY26", "MET"),
     ("T1", "Q2 FY27", "Tax rate 24-25%", "25% FY24-FY26", "MET")]
ledger = table(["#", "Call", "Promise", "What happened", "Status"],
               [[a, b, c, d, (chip(e), "c")] for a, b, c, d, e in L], "std",
               caption="Selected promises from the 14-call ledger", source=src("ledger"))
quote = """<blockquote class="q"><p>"if you take out the last year's degrowth ... we have grown at 18-19% ... more from a global phenomenon effect and nothing structural in nature"</p>
<cite>Ankur Vaid, answering a Kotak analyst who noted two-year sales were flat, Q2 FY27 call, p16</cite></blockquote>"""
s11 = f"""<p>We read every earnings call since listing (14 calls, Sep 2023 to Oct 2026) and logged each promise with the page it was made on. Of the 23 that have come due, 10 were met and 13 were missed or late.</p>
{exhibit("Operating facts get delivered; growth, margin and timing promises slip", score, src("ledger"), "Counted only promises that have come due. Open promises are not scored.")}
{ledger}
{quote}"""
section("s11", "B", "Claims ledger", "S11 | Promises vs delivery", "10 of 23 promises met",
        "Across 14 calls, management met 10 of 23 promises that came due; tax, product mix and launches were delivered, while growth, margin and new-business dates slipped.",
        s11,
        "Use the ledger as a discount rate on guidance. When management says 'H2' or 'next year', history says to allow one or two extra quarters.")

# ================================================================= S12 guidance & what must be true
mm = C.lines(D["ql"], [("Reported", [round(x, 1) for x in CALC["q_opm"]], C.PRIMARY, False),
                       ("Without injectables and Stellon", D["q_adj"], C.SECOND, True)],
             "EBITDA margin by quarter with the 38-40% guide", unit="%", dec=1, w=760, h=260, band=(38, 40, "Guide 38-40% [G]"),
             ymin=25, ymax=50)
wmt = table(["What must be true", "Needed", "Latest", "Check"], [
    ["FY27 sales growth 19% [G path]", f"H2 FY27 Rs {f0(n19)} cr ({pc(n19g, 0, True)})", "H1 FY27 +26%", chip("OPEN")],
    ["EBITDA margin back to 38% by FY29", "Base case 35% / 36.5% / 38%", "Q2 FY27 33.8%", chip("WATCH")],
    ["Gross margin stops falling", "Back to 79-80%", "Q2 FY27 76.2%", chip("WATCH")],
    ["Injectable contracts signed", "In H2 FY27 (management)", "None yet; plant 5%", chip("OPEN")],
    ["Stellon contributes", "In H2 FY27", "Slipped one half", chip("WATCH")],
    ["Inventory unwinds", "Below Mar-26's Rs 326 cr", f"Sep-26 Rs {f0(D['inventory_sep26'])} cr", ("<span class='chip red'>RED</span>", "c")],
    ["Rs 3,000 cr peak (5-6 years)", f"{pc(CALC['peak3000_cagr'], 0)} a year from FY26", "TTM Rs 1,170 cr", chip("OPEN")]], "std",
    caption="What has to happen for the price to be right", source=src(("tr27", 13), ("tr27", 16), ("deck27", 11), "model"))
s12 = f"""<p>Current guidance, from the Q2 FY27 call: FY27 growth "slightly better than our historical growth of 18%"; EBITDA margin 38-40% "over the next few years"; tax 24-25%; capex Rs 20-30 cr plus Rs 50-60 cr a year in FY27 and FY28.</p>
{exhibit("Margin is still below the guided band, with or without the start-ups (%)", mm, src("scr", ("tr27", 5), ("tr27", 7), "ledger"),
         "Reported margin is our calculation from Screener quarterly figures; the company's deck shows 33.8% for Q2 FY27. The adjusted margin was not given for Q3 FY25, Q4 FY25 or Q1 FY27, so the line has gaps.")}
{wmt}"""
section("s12", "C", "Guidance and must-be-true", "S12 | Guidance", f"A 19% year needs a 14% better second half",
        f"For FY27 growth of 19%, H2 sales must reach about Rs {f0(n19)} cr, up {pc(n19g)} on H2 FY26; margin must then climb about 4 points over three years to reach the bottom of the 38-40% guide.",
        s12,
        "The growth half looks reachable: H1 grew 26% and H2 only needs 14%. The margin half is the harder test, because it needs the start-ups to stop losing money and prices to hold.")

# ================================================================= S13 triggers
trig = table(["Trigger", "When", "Strength", "Why"], [
    ["H2 FY27 sales of about Rs 689 cr", "Q3 FY27 (Feb 2027) and FY27 (May 2027)", chip("STRONG"), "Decides whether FY26 was a pause"],
    ["First injectable contracts", "Promised H2 FY27", chip("MODERATE"), "Removes Rs 10-12 cr a quarter of drag over time"],
    ["Stellon US sales start", "Promised H2 FY27", chip("MODERATE"), "Restores US formulation sales"],
    ["Gross margin back above 78%", "Any quarter", chip("STRONG"), "Shows pricing has stabilised"],
    ["Nystatin, Fusidic acid commercial orders", "FY27-FY28", chip("WEAK"), "Small molecules; adds breadth"],
    ["Unit III towards 80%; new block announced", "FY29-FY30 [E]", chip("MODERATE"), "Signals demand beyond today's tanks"],
    ["CDMO to 1-4% of sales, then double digits", "FY27, then long term", chip("WEAK"), "One project today, about USD 2 mn"],
    ["Inspira skin brand to Rs 400-500 cr", "4-5 years [G]", chip("WEAK"), "Very early; new to Concord"]], "std",
    caption="Triggers: near-term ones are about proof, long-term ones about optionality", source=src(("tr27", 4), ("tr27", 13), ("tr127", 14), "ledger"))
s13 = f"""{trig}
<p><b>Absence test.</b> Things a fast-growing Concord would have done by now but has not: announced new fermentation capacity beyond 1,250 m3; signed an injectable contract; shown Stellon revenue; given an adjusted margin above 40% since Q2 FY26. Each absence is consistent with a business that is recovering, not yet accelerating.</p>"""
section("s13", "C", "Triggers", "S13 | Triggers", "The next two results matter more than any new product",
        "The strongest near-term triggers are H2 FY27 sales and gross margin; injectables and Stellon are moderate; CDMO, Inspira and new molecules are long-dated and small.",
        s13,
        "Mark mid-February 2027 (Q3 FY27) and end-May 2027 (FY27) in your diary. Those two releases settle most of the debate in this report.")

# ================================================================= S14 peers
pe_chart = C.hbars([p_[0] for p_ in peers], [p_[8] for p_ in peers], "P/E, trailing, peers", dec=1, unit="x",
                   w=460, highlight={0}, lab_w=150)
pt = table(["Company", "Sales FY26", "Growth FY26", "Growth TTM", "OPM FY26", "OPM TTM", "P/E", "ROCE"],
           [[(n, "bold" if i == 0 else ""), f0(s_), (f"{g26:+d}%", "flag" if g26 < 0 else ""), f"{gt:+d}%{' [E]' if i == 0 else ''}",
             f"{o26}%", f"{ot}%", f1(pe_), f1(rc)]
            for i, (n, s_, g25, g26, gt, o25, o26, ot, pe_, rc) in enumerate(peers)], "fin peer",
           caption="Concord is the only peer whose sales fell in FY26", source=src("peers") + ' <span class="mob">On a phone, growth TTM, OPM FY26 and ROCE are hidden; turn the phone sideways to see them.</span>')
s14 = f"""{pt}
{duo(exhibit("Concord trades in line with Gland and below most API makers (P/E, x)", pe_chart, src("peers"), "Biocon's P/E is distorted by its biosimilars business and debt."),
     '<div><h3>Reading the peer table</h3>' + ul([
        "Every listed API and CDMO peer grew 7-37% in FY26 while Concord fell 12%. That is why its multiple is lower.",
        "Its margin is still second only to Divi's.",
        "The API and CDMO group trades at 58-102x; Concord at 43.6x on Screener's basis (44.5x on our TTM calculation).",
        "No listed company is a pure fermentation peer, so these are reference points, not a fair-value anchor.",
        "Our base multiple of 35x on FY29 earnings sits below the whole API group for this reason."]) + '</div>')}"""
section("s14", "D", "Peers", "S14 | Peers", "Cheaper than API peers because it stopped growing",
        "Concord has top-tier margins but trades at a discount to API and CDMO peers because it was the only one to shrink in FY26; the discount narrows only if growth returns.",
        s14,
        "The peer group says Concord is not expensive for its quality, but also that the market already gives it credit for a recovery: 44x is not a distressed multiple.")

# ================================================================= S15 reality vs optionality
rvo = table(["Business", "Today", "Management's stated potential", "In our base case?"], [
    ["Fermentation API", "Rs 829 cr FY26; Rs 469 cr H1 FY27", "Grow 18-19% a year; Limbasi Rs 1,500-1,600 cr at peak", "Yes, at guidance"],
    ["Formulations (tablets)", "Rs 226 cr FY26; falling", "Earlier 35-40% CAGR (missed)", "Inside the 19%"],
    ["Injectables (Unit IV)", "Not disclosed; plant at 5%", "About Rs 300 cr in 3-4 years; plant Rs 500-600 cr", "Only through margin rising to 38%"],
    ["CDMO", "About USD 2 mn a year", "USD 40-50 mn opportunity; 1-4% of FY27 sales", "No separate value"],
    ["Inspira (skin brand)", "Launched Q2 FY27", "Rs 400-500 cr in 4-5 years", "No separate value"],
    ["Group target", "TTM Rs 1,170 cr", "Rs 3,000 cr peak in 5-6 years", "No; base reaches Rs 1,778 cr by FY29"]], "std",
    caption="What exists today vs what management says could exist", source=src(("tr27", 4), ("tr27", 13), ("tr126", 16), ("tr124", 12), "decks"))
s15 = f"""{rvo}
<p>Our base case uses guided growth of 19% a year and no more. It reaches Rs {f0(ROWS['Base'][2]['revenue'])} cr of sales in FY29, about 59% of the Rs 3,000 cr target.
If the options work, they are upside to the bull case; we do not add a separate value for them, because none yet has a contract, a revenue line or a disclosed margin.</p>"""
section("s15", "D", "Reality vs optionality", "S15 | Reality vs options", "Pay for the API engine; treat the rest as free options",
        "About 83% of sales today is fermentation API; injectables, CDMO, Inspira and the Rs 3,000 cr target are options with no contracts or revenue lines yet.",
        s15,
        "If you buy into the story because of injectables or CDMO, you are paying for things that do not show in the numbers yet. Our values do not depend on them.")

# ================================================================= S16 causal chains
inj = flow([("Trigger", ["Injectable contracts signed <small>(promised H2 FY27)</small>"], True),
            ("Operations", ["Unit IV use rises from 5% <small>(fixed costs already in place)</small>"], False),
            ("P&amp;L", ["Rs 10-12 cr a quarter drag shrinks <small>(Rs 38-39 cr in FY26)</small>"], False),
            ("Outcome", ["Reported margin moves towards the adjusted 37-39%"], True)])
api = flow([("Trigger", ["Customers' buying returns to normal <small>(tariff, EU, tender issues fade)</small>"], True),
            ("Operations", ["API volumes rise; Unit III from 55% towards 80%"], False),
            ("P&amp;L", ["Fixed costs spread over more kg <small>(but price cuts and solvent costs offset)</small>"], False),
            ("Outcome", ["Core margin back to 39-41% only if prices hold"], True)])
s16 = f"""{exhibit("Causal chain 1: injectables turn from cost to profit", inj, src(("tr326", 11), ("tr426", 8), ("tr27", 4)))}
{exhibit("Causal chain 2: the API recovery lifts margin only if price holds", api, src(("tr426", 4), ("tr127", 10), ("tr27", 5)))}
<p>The weak link in chain 1 is the first box: a contract. The weak link in chain 2 is the third box: if volumes come back at lower prices, the margin stays near 37% even with full tanks.</p>"""
section("s16", "D", "Causal chain", "S16 | Cause and effect", "Two chains decide the margin; each has one weak link",
        "Margin recovers through two chains: injectable contracts removing a Rs 40 cr-a-year drag, and API volumes filling Limbasi; the first needs a signature, the second needs prices to hold.",
        s16,
        "Watch the first box of each chain, not the last. A signed injectable contract and a stable gross margin will show up before the margin does.")

# ================================================================= S17 financials & QoE
wc = C.lines(D["years"], [("Inventory days", D["inv_d"], C.PRIMARY, False), ("Debtor days", D["debtor_d"], C.SECOND, False),
                          ("Payable days", D["pay_d"], C.THIRD, False)], "Working-capital days FY20 to FY26", w=760, h=250, ymin=0, ymax=600)
cfe = C.bars(D["years"], [round(x) for x in CALC["cfo_ebitda"]], "Operating cash flow as % of EBITDA FY20 to FY26", unit="%",
             highlight={6}, w=460, h=230)
pl = table(["Rs cr"] + D["years"] + ["TTM"], [
    ["Sales"] + [f0(v) for v in D["sales"]] + [f0(D["sales_ttm"])],
    ["EBITDA"] + [f0(v) for v in D["op"]] + [f0(D["op_ttm"])],
    ["EBITDA margin"] + [f"{v}%" for v in D["opm"]] + ["34%"],
    ["Other income"] + [f0(v) for v in D["oi"]] + ["46"],
    ["Depreciation"] + [f0(v) for v in D["dep"]] + ["75"],
    ["Profit before tax"] + [f0(v) for v in D["pbt"]] + ["374"],
    ["Profit after tax"] + [f0(v) for v in D["pat"]] + [f0(D["pat_ttm"])],
    ["EPS (Rs, post-bonus)"] + [f"{v:.2f}" for v in D["eps_adj"]] + ["13.50"],
    ["Operating cash flow"] + [f0(v) for v in D["cfo"]] + ["-"],
    ["Free cash flow"] + [neg(v) for v in D["fcf"]] + ["-"],
    ["Net worth (approx.)"] + [f0(r + 10) for r in D["reserves"]] + ["-"],
    ["Borrowings"] + [f0(v) for v in D["borrow"]] + ["-"],
    ["Investments"] + [f0(v) for v in D["inv_book"]] + ["-"],
    ["Return on capital"] + ["-"] + [f"{v}%" for v in D["roce"][1:]] + ["-"]], "fin",
    caption="Ten-line financial summary", source=src("scr") + " Net worth is reserves plus about Rs 10 cr of share capital (pre-bonus) [E]; negatives in brackets.")
s17 = f"""{pl}
{exhibit("Inventory days jumped back to 485 in FY26; FY25's 286 was the low point (days)", wc, src("scr"), "FY21-FY23 inventory days were 430-503, so FY26 is high but not new. Inventory rose again to Rs 398 cr at Sep-26 from Rs 326 cr at Mar-26.")}
{duo(exhibit("Profits turn into cash: operating cash flow was 100% of EBITDA in FY26", cfe, src("scr"), "Our calculation [E]."),
     '<div><h3>Quality-of-earnings verdict</h3>' + table(["Test", "Result"], [
        ["Cash conversion (CFO / EBITDA, FY20-FY26)", chip("OK")],
        ["Debt", chip("OK")],
        ["Audit opinion (unmodified, B S R &amp; Co.)", chip("OK")],
        ["Inventory and working capital (493-day cash cycle)", chip("WATCH")],
        ["Other income (Rs 52 cr, 15% of FY26 pre-tax profit)", chip("WATCH")],
        ["Palvella gain kept out of profit (through OCI)", chip("OK")]], "std") +
     '<p class="small">Overall: <b>OK on cash, WATCH on working capital.</b> Profits are real cash; the risk is that stock building ties up more of it.</p></div>')}"""
section("s17", "D", "Financials and earnings quality", "S17 | Financials", "Profits are real cash; stock is the soft spot",
        "Earnings quality is good: operating cash matched EBITDA in FY26, there is no debt and the audit is clean; the weak spot is a 485-day inventory cycle that rose again in H1 FY27.",
        s17,
        "If inventory does not fall by March 2027, the 'customers delayed shipments' explanation for FY26 weakens. That is one number in the FY27 balance sheet worth checking.")

# ================================================================= S18 governance & filings
gov = table(["Item", "Finding", "Level"], [
    ["Audit", "Unmodified opinion from B S R &amp; Co. (KPMG network); key audit matter is revenue timing", chip("OK")],
    ["Audit trail", "Operated all of FY26; had not been enabled for part of earlier years (note 44)", chip("WATCH")],
    ["CFO and company secretary", "New CFO in Dec 2025; three company secretaries in a year; no reasons given", chip("WATCH")],
    ["Stellon (75% US arm)", "Lists 'directors interested'; owner of the other 25% not disclosed; Rs 14.6 cr loan from Concord", chip("WATCH")],
    ["Celliimune", "Bought from director Ravi Kapoor for Rs 0.66 cr (immaterial, but a related purchase)", chip("WATCH")],
    ["Related-party trading", "Japan JV sales Rs 29.1 cr; rent to promoters Rs 2.0 cr; stated at arm's length", chip("OK")],
    ["Promoter pay", "Rs 14.05 cr incl. relatives, 5.4% of profit; flat while profit fell 30%", chip("WATCH")],
    ["Contingent liabilities", "Rs 3.76 cr disputed excise; immaterial", chip("OK")],
    ["Credit rating", "ICRA AA- (Stable) / A1+, Jul 2025", chip("OK")],
    ["Pledge", "None shown on Screener or in the annual report; exchange filing not checked", ("<span class='chip nd'>NOT VERIFIED</span>", "c")],
    ["US FDA record", "Company-reported only; FDA database not checked; no warning letter or import alert in any document read", chip("OK")]], "std",
    caption="Governance checklist: no red flags, five watch items", source=src(("ar26", 79), ("ar26", 123), ("ar26", 186), ("ar26", 243), ("ar26", 244), ("ar26", 245), ("ar26", 233), ("ar26", 77)))
s18 = f"""{gov}"""
section("s18", "D", "Governance and filings", "S18 | Governance", "No red flags; five things to keep an eye on",
        "The filings are clean on audit, debt and contingent liabilities; the watch items are the Stellon ownership, management turnover, an earlier audit-trail gap and a small purchase from a director.",
        s18,
        "None of this changes the numbers. It is a reason to read the FY27 annual report's related-party note, especially who owns the rest of Stellon and whether Concord lends it more.")

# ================================================================= S19 anti-thesis and risks
bvr = table(["The bull says", "The rebuttal"], [
    ["FY26 was a timing issue; H1 FY27 is up 26%", "FY24-FY26 sales grew 1.9% a year; Rs 100 cr of the FY26 fall has no quantified reason"],
    ["Margins go back to 40%+", "The core margin without start-ups fell from 41% to 37%; gross margin is down 4 points in Q2"],
    ["Injectables add Rs 300 cr", "First promised for Q1 FY25; no contract yet; plant at 5%"],
    ["Rs 3,000 cr peak sales", "Needs 19-20% a year for six years; the 25% target was already re-labelled"],
    ["Few rivals, sticky customers", "Share gains were bought partly with lower prices"]], "std two",
    caption="The case against, point by point", source=src("ledger", ("tr27", 5)))
risks = [
    ("R1", "Lumpy buying repeats", "Customers buy in bulk, then pause, as in FY25-FY26.", f"H2 FY27 sales below Rs 640 cr (+6%)", "Bear case"),
    ("R2", "Price erosion", "Share is won with lower prices; solvent and power costs rise.", "Gross margin below 75% for two quarters", "Bear case"),
    ("R3", "US FDA action", "An adverse outcome at Unit I or III, which make almost all API.", "Any OAI status, warning letter or import alert", "Not modelled"),
    ("R4", "Injectables stuck", "Unit IV stays nearly empty; Rs 40 cr a year of drag continues.", "No contract by the FY27 results (May 2027)", "Bear case"),
    ("R5", "Working capital", "Stock keeps building and cash conversion falls.", "Inventory days above 450 at FY27, or CFO/EBITDA below 70%", "Not modelled"),
    ("R6", "Multiple de-rates", "If growth stays low, the market pays a slower-company multiple.", "Growth below 15% for FY27 and FY28", "Bear case (25x)"),
    ("R7", "Related-party creep", "More money flows to Stellon or director-linked entities.", "Stellon loan above Rs 25 cr, or new related purchases", "Not modelled"),
    ("R8", "Currency", "The rupee strengthens; currency added about 10% to Q1 FY27 growth.", "Rupee up more than 5% against the dollar in a year", "Not modelled")]
rcards = '<div class="risks">' + "".join(
    f'<div class="risk"><p class="rid">{i} | {t}</p><p>{d}</p><p class="thr"><b>Threshold:</b> {th}</p><p class="tiny">{m}</p></div>'
    for i, t, d, th, m in risks) + "</div>"
s19 = f"""{bvr}
<h3>If the share halves</h3>
<p>At Rs {f0(CALC['halve'])} the market would value Concord at about {f1(CALC['halve_pe'])} times trailing profit, near Aarti Drugs' 19.6x, a commodity API maker.
That would mean the market had decided FY26 was a step down: growth near 10% and margins stuck at 33-34%. Our bear case (Rs {f0(bear_v)}) is built on exactly that and sits above Rs {f0(CALC['halve'])}, because the cash pile and existing tanks still earn something.
The share has already traded at Rs 494 in the last year.</p>
<h3>Risk cards</h3>
{rcards}
<p class="src">{src("ledger", ("ar26", 238), ("tr127", 10))[8:]}</p>
<h3>What would change our mind</h3>
{ul(["<b>More positive:</b> H2 FY27 sales above Rs 700 cr with gross margin back above 78%, and a signed injectable contract. That moves the base towards the bull case.",
     "<b>More negative:</b> H2 FY27 sales below Rs 640 cr, or gross margin below 75% for two quarters. That moves the base towards the bear case.",
     "<b>Thesis breaker:</b> an FDA warning letter at Dholka or Limbasi, or evidence of a lost major customer."])}"""
section("s19", "E", "Anti-thesis and risks", "S19 | Risks", "Most risks show up in two numbers: H2 sales and gross margin",
        "The strongest case against Concord is that FY25 was a peak, prices are softening and the new businesses keep slipping; four of eight risks feed directly into our bear case.",
        s19,
        "Each risk has a number attached. You do not need to guess which story is right; you need to check those thresholds as the results come out.")

# ================================================================= S20 valuation
vr = C.value_range([("Bear", bear_v, C.SECOND, pc(V["Bear"]["vs_price"], 0, True)),
                    ("Base", base_v, C.PRIMARY, pc(V["Base"]["vs_price"], 0, True)),
                    ("Bull", bull_v, C.FOURTH, pc(V["Bull"]["vs_price"], 0, True))], D["price"],
                   "Bear, base and bull value per share vs price", w=760, lo=0, hi=1000)
imp = VAL["implied"]
ib = C.hbars([f"Needed at {int(r['pe'])}x" for r in imp] + ["Base case FY29 [E]", "TTM (Sep-26)", "FY26 actual"],
             [round(r["pat_flat"]) for r in imp] + [round(ROWS["Base"][2]["pat"]), D["pat_ttm"], round(D["fy26_pat_owners"])],
             "FY29 profit the price needs at each P/E vs our base case", w=460,
             colors=[C.GREY] * 4 + [C.PRIMARY, C.SECOND, C.SECOND], lab_w=150)


def sc_rows(name):
    a = VAL["scenarios"][name]["assumptions"]
    rs = ROWS[name]
    return [[f"{name} {r['year']}", f0(r["revenue"]), pc(a["growth"][i], 0), f0(r["ebitda"]), pc(r["margin"], 1), f0(r["pat"]), f"{r['eps']:.2f}"]
            for i, r in enumerate(rs)]


sc = table(["Case and year", "Sales", "Growth", "EBITDA", "Margin", "Profit", "EPS (Rs)"],
           sc_rows("Bear") + sc_rows("Base"), "fin",
           caption="Bear and base projections (bull uses base earnings) [E]", source=src("model"))
val = table(["", "Bear", "Base", "Bull"], [
    ["FY29 EPS (Rs) [E]", f"{V['Bear']['fy29_eps']:.2f}", f"{V['Base']['fy29_eps']:.2f}", f"{V['Bull']['fy29_eps']:.2f}"],
    ["P/E applied", f"{V['Bear']['pe']:.0f}x", f"{V['Base']['pe']:.0f}x", f"{V['Bull']['pe']:.0f}x"],
    ["Value at Mar-28", f0(V["Bear"]["price_mar28"]), f0(V["Base"]["price_mar28"]), f0(V["Bull"]["price_mar28"])],
    ["Discounted to today (12%, 1.39 years)", f0(V["Bear"]["pv_today"]), f0(V["Base"]["pv_today"]), f0(V["Bull"]["pv_today"])],
    ["Plus Palvella stake per share", f0(V["Bear"]["palvella_ps"]), f0(V["Base"]["palvella_ps"]), f0(V["Bull"]["palvella_ps"])],
    [("Value per share", "bold"), (f0(bear_v), "bold"), (f0(base_v), "bold"), (f0(bull_v), "bold")],
    ["vs price Rs 594", (pc(V["Bear"]["vs_price"], 0, True), "flag"), pc(V["Base"]["vs_price"], 0, True), pc(V["Bull"]["vs_price"], 0, True)]], "fin",
    caption="From FY29 earnings to a value per share today", source=src("model"))
sens = table(["Sales growth FY26-29 \\ P/E", "25x", "30x", "35x", "40x", "45x"],
             [[pc(r["growth"], 0)] + [(f0(v), "bold" if (abs(r["growth"] - 0.19) < 1e-9 and j == 2) else ("hi" if v >= 594 else "")) for j, v in enumerate(r["values"])]
              for r in VAL["sensitivity"]], "fin",
             caption="Value per share by growth and P/E (base margins); shaded cells are above Rs 594", source=src("model"))
cc = VAL["cross_checks"]
qs15 = [
    ("Why did FY26 fall?", "Five buying and access problems, explained after the fact; about Rs 40-45 cr of the Rs 145 cr fall quantified."),
    ("Was Q4 FY25 a one-off?", "Mostly yes [E]: bulk buying; Q4 FY26 returned to the Q4 FY24 level."),
    ("Volume, price or new customers?", "FY26 all volume; Q1 FY27 gains 'primarily driven by pricing'; split not disclosed."),
    ("Who competes; is share rising?", "2-3 makers per product, mainly Europe and Southeast Asia; share gains are management's claim only."),
    ("How concentrated are sales?", "Top 10 at 37.6%; none above 10%; largest customer not named."),
    ("When is a new plant needed?", "About FY29-FY30 [E], when Limbasi nears 80%."),
    ("What do the start-ups cost?", "About Rs 42 cr of EBITDA in FY26 and Rs 27 cr in H1 FY27 [E]; breakeven not given."),
    ("Why did formulations fall?", "Customers buying API instead, and the US move to Stellon; size not disclosed."),
    ("What has past capex earned?", "Limbasi paid back; Unit IV has earned almost nothing yet; project returns not disclosed."),
    ("Why are inventory days 485?", "Delayed shipments and long cycles; FY25's 286 was the outlier."),
    ("How often is guidance met?", "10 of 23 promises; verdict WATCH."),
    ("What is in the investment book?", f"Rs {f0(CALC['inv_book_sep26'])} cr, mostly mutual funds, plus Palvella; Stellon loan is the related item."),
    ("Who owns it; any pledge?", "Promoters 44.09%, no sale since listing; pledge not verified in the exchange filing."),
    ("What is the US FDA record?", "No warning letters disclosed; Unit I had 483s then EIR; FDA database not checked."),
    ("What does Rs 594 imply?", f"About Rs {f0(imp[1]['pat_flat'])} cr of FY29 profit at 30x, against Rs {f0(ROWS['Base'][2]['pat'])} cr on guidance.")]
q15 = table(["#", "Question", "One-line answer"], [[str(i + 1), q, a] for i, (q, a) in enumerate(qs15)], "std",
            caption="The 15 research questions, answered in one line each", source="Source: notes.md, with sources cited in each section above.")
grounded = table(["Grounded in filings", "Assumed by us"], [
    ["FY26 base: sales Rs 1,055 cr, EBITDA Rs 368 cr, owner profit Rs 259 cr", "Growth path: 10-11% bear, 19% base and bull"],
    ["Shares 20.92 cr after bonus; price Rs 594", "Margins: 33-34% bear; 35% to 38% base"],
    ["Cash and liquid funds Rs 446 cr; no debt", "Multiples: 25x, 35x, 45x on FY29 earnings"],
    ["Tax 24-25% [G]; capex Rs 20-30 cr plus Rs 50-60 cr [G]", "Cost of equity 12%; other income Rs 45-55 cr"]], "std two")
s20 = f"""<p><b>Method.</b> We value Concord on price to earnings, because it is a steady, debt-free manufacturer whose profit is mostly cash.
We project sales and margin to FY29, apply a multiple to FY29 earnings to get a value at March 2028, discount it back 1.39 years at 12%, and add the Palvella stake at book value.</p>
{exhibit("Price sits between our bear and base values", vr, src("model"), f"Readout: {READOUT}. Base is {pc(V['Base']['vs_price'], 0, True)} vs price; ATTRACTIVE needs +20% or more, STRETCHED -20% or worse.")}
{val}
{sc}
<p class="small">Bear: built from risks R1, R2, R4 and R6: growth 10-11%, margin 33-34%, 25x. Base: management guidance with no haircut, 19% growth and margin rising to 38% by FY29, 35x. Bull: the same earnings as the base, valued at 45x (today's trailing multiple), because we never model sales above guidance.</p>
{duo(exhibit("At 30x, the price needs Rs 411 cr of FY29 profit; guidance gives Rs 484 cr (Rs cr)", ib, src("model"), "'Needed' assumes the price simply holds to Mar-28; for a 12% yearly return add about 17%."),
     sens)}
<p><b>Cross-checks [E].</b> Enterprise value Rs {f0(cc['ev'])} cr; {f1(cc['ev_ttm_ebitda'])}x trailing EBITDA and {f1(cc['ev_fy29_base_ebitda'])}x FY29 base EBITDA; free-cash-flow yield {pc(cc['fcf_yield_fy26'], 1)} on FY26; sales per rupee of fixed assets {cc['fat_fy26']:.2f}x in FY26 and {cc['fat_fy29_base']:.2f}x in the FY29 base, back above FY24's 1.77x.</p>
{grounded}
{q15}
<h3>Dated signals</h3>
{table(["Date", "Signal", "Moves value towards"], [
    ["Mid-Feb 2027 (Q3 FY27)", "Q3 sales above Rs 330 cr and gross margin 77%+", "Base"],
    ["Mid-Feb 2027 (Q3 FY27)", "Q3 sales below Rs 300 cr", "Bear"],
    ["End-May 2027 (FY27)", f"FY27 sales Rs {f0(VAL['scenarios']['Base']['rows'][0]['revenue'])} cr or more; injectable contract signed", "Base to bull"],
    ["End-May 2027 (FY27)", "FY27 sales below Rs 1,160 cr (+10%); inventory still rising", "Bear"]], "std")}
<p class="small">Signal thresholds are our judgment, set from the model paths: the Q3 levels assume H2 splits roughly as last year (46% in Q3).</p>"""
section("s20", "E", "Valuation", "S20 | Valuation", f"Base value Rs {f0(base_v)}: fair, not cheap",
        f"Our base value is Rs {f0(base_v)} a share ({pc(V['Base']['vs_price'], 0, True)}), with a bear case of Rs {f0(bear_v)} and a bull case of Rs {f0(bull_v)}; the readout is {READOUT} because the base is within 20% of the price.",
        s20,
        f"The range is wide and lopsided: {pc(V['Bear']['vs_price'], 0, True)} in the bear case against {pc(V['Bull']['vs_price'], 0, True)} in the bull. The price already assumes guidance is met, so the payoff depends on management doing better than its record.")

# ================================================================= Appendix
src_list = "".join(f'<li>{("<a href=" + chr(34) + u + chr(34) + ">" + n + "</a>") if u else n}</li>' for n, u in SRC.values())
dis = table(["Disclosed (company documents)", "Inferred (our calculation or reading) [E]", "Not disclosed or not checked"], [
    ["FY26 reasons for the fall; segment and market splits", "Q4 FY25 was bulk buying", "Sales by molecule; largest customer"],
    ["Utilisation by unit each call", "Start-up drag Rs 42 cr in FY26", "Revenue by plant; project returns"],
    ["Margin without injectables and Stellon", "Capex from cash flow (Rs 95 cr FY26)", "Owner of Stellon's other 25%"],
    ["Top-10 customer share; no customer above 10%", "Unit III reaches 80% by FY29-FY30", "Reasons for CFO and company secretary exits"],
    ["Inspection outcomes as reported by the company", "H1 FY25 sales Rs 526 cr", "US FDA database, Orange Book; pledge filing"],
    ["Guidance on growth, margin, capex, tax", "All valuation projections", "Injectables break-even date; contract terms"]], "std",
    caption="What is disclosed, inferred and missing", source="Source: this report.")
appendix = f"""{dis}
<h3>Sources</h3><ol class="srcs">{src_list}</ol>
<p class="small">Also read but not cited above: all 14 call transcripts and 14 investor presentations from Q1 FY24 to Q2 FY27, and annual reports FY24 and FY25 (listed in the source manifest). Not checked: the company's investor-relations site, NSE copies of filings, the IPO prospectus text, and US FDA databases. Images inside the decks were not extracted; all charts here are redrawn from the numbers.</p>
<h3>Disclaimer</h3>
<p class="small">This report is research for learning and discussion. It is not investment advice, a recommendation, or an offer to buy or sell any security. The author is not a SEBI-registered investment adviser or research analyst. The valuation readout describes where the price sits against our scenarios; it is not a rating. Figures come from company filings and Screener.in as of 9 November 2026 and may contain errors; estimates marked [E] are ours and guidance marked [G] is management's. Past performance does not guarantee future results. Make your own decisions or consult a registered adviser.</p>"""
SECTIONS.append(("appendix", "", "Sources and disclaimer", "Appendix", "Sources, disclosures and disclaimer", appendix))

# ================================================================= render
PARTS = {"A": "Part A | The business", "B": "Part B | Management", "C": "Part C | The future", "D": "Part D | Proof", "E": "Part E | Risks and value"}

CSS = """
:root{--teal:#0E5A63;--p1:#00849E;--p2:#C77A1A;--tealt:#E7F1F2;--ink:#1F2733;--muted:#5F6873;--line:#DDE2E7;--bg:#EEF1F3;--red:#B23A3A}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;color-scheme:light}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 Calibri,Carlito,'Segoe UI',Arial,sans-serif}
a{color:#00708A}
.wrap{display:grid;grid-template-columns:200px minmax(0,980px);gap:22px;justify-content:center;padding:0 16px}
.side{padding-top:22px;font-size:13px}
.side .brand{font-weight:700;color:var(--teal);font-size:15px;margin:0 0 2px}
.side .sub{color:var(--muted);margin:0 0 12px;font-size:12px}
.side .pt{font-weight:700;color:var(--teal);text-transform:uppercase;letter-spacing:.05em;font-size:11.5px;margin:12px 0 3px}
.side ol{list-style:none;margin:0;padding:0}
.side li{margin:0 0 3px}
.side a{text-decoration:none;color:var(--ink)}
.side a:hover{color:var(--p1);text-decoration:underline}
.side .n{display:inline-block;width:30px;color:var(--muted)}
.page{background:#fff;border:1px solid var(--line);margin:22px 0}
.band{background:var(--teal);color:#fff;display:flex;justify-content:space-between;align-items:center;padding:8px 26px;font-size:12.5px;letter-spacing:.03em}
.band b{color:#BFE3E8}
.rule{height:3px;background:var(--p2)}
.inner{padding:16px 26px 10px}
.kicker{color:var(--p2);font-weight:700;font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;margin:4px 0 2px}
h1,h2,h3,h4{color:var(--teal)}
h2{font-size:24px;line-height:1.2;margin:0 0 10px}
h3{font-size:17px;margin:18px 0 6px}
h4{font-size:15px;margin:16px 0 4px}
p{margin:0 0 9px}
.answer{font-weight:700;font-size:16px;line-height:1.45;border-left:3px solid var(--p1);padding:2px 0 2px 12px;margin:4px 0 14px}
.mfy{margin-top:18px;border-top:1px solid var(--line);padding-top:10px}
.means{margin-bottom:6px}
.lede{font-size:17px;line-height:1.5;color:var(--teal)}
.eq{background:var(--tealt);padding:8px 12px;font-weight:700;color:var(--teal)}
.ex{margin:14px 0;padding:0;break-inside:avoid}
figcaption{font-weight:700;color:var(--teal);font-size:14px;margin-bottom:6px}
.src{font-size:11.5px;color:var(--muted);margin:4px 0 0}
.xnote{font-size:12.5px;margin:6px 0 0;color:#3A434E}
.duo{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:22px;align-items:start}
.t{border-collapse:collapse;width:100%;font-size:13.5px;margin:4px 0}
.t th{border-bottom:1.5px solid var(--teal);color:var(--teal);font-weight:700;padding:5px 7px;text-align:right;vertical-align:bottom}
.t th:first-child{text-align:left}
.t td{padding:4px 7px;border-bottom:1px solid var(--line);vertical-align:top}
.t td.l{text-align:left}.t td.r{text-align:right}.t td.c{text-align:center}
.t.std td.r,.t.std th{text-align:left}
.t td.flag{color:var(--red);font-weight:700}.t td.neg{color:var(--red)}.t td.bold{font-weight:700}
.t td.hi{background:#E4F2F4}
.t.kv th{display:none}.t.kv td{padding:3px 4px;font-size:13px}
.t.fin td,.t.fin th{font-size:12.5px;padding:3px 5px;white-space:nowrap}
.t.fin td.l{white-space:normal}
.t.two td{width:50%}
.tw{overflow-x:auto;max-width:100%}
.chip{display:inline-block;padding:0 7px;border-radius:3px;font-size:11.5px;font-weight:700;letter-spacing:.02em;border:1px solid;white-space:nowrap}
.chip.ok{color:#1F6B4C;border-color:#7FB79E;background:#EEF7F2}
.chip.watch{color:#8A520C;border-color:#D9AE6E;background:#FBF3E6}
.chip.red{color:#8E2525;border-color:#D69292;background:#FBEFEF}
.chip.open{color:#245E86;border-color:#8FB4CF;background:#EEF4F9}
.chip.nd{color:#555E69;border-color:#B5BCC4;background:#F3F4F6}
.small{font-size:13px}.tiny{font-size:12px;color:var(--muted)}
.cw-m{display:none}
ul{padding-left:20px;margin:4px 0 10px}li{margin:0 0 5px}
blockquote.q{margin:14px 0;padding:8px 14px;border-left:3px solid var(--p2);background:#FBF6EE}
blockquote.q p{margin:0 0 4px;font-style:italic}blockquote.q cite{font-size:12.5px;color:var(--muted);font-style:normal}
/* cover */
.ctitle{font-size:34px;font-weight:700;margin:0;line-height:1.1}
.csub{font-size:19px;color:var(--p2);margin:4px 0 2px;font-weight:700}
.cmeta{font-size:13px;color:var(--muted);margin:0 0 12px}
.cover{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:24px}
.rail{background:#F6F8F9;border:1px solid var(--line);padding:12px;align-self:start}
.rbox{margin-top:12px}
.rh{font-weight:700;color:#fff;background:var(--teal);margin:0 0 4px;padding:3px 8px;font-size:12.5px}
.verdict{border:1px solid var(--p2);background:#FBF3E6;padding:8px 10px}
.verdict .rk{margin:0;font-size:11.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.verdict .rv{margin:0;font-size:22px;font-weight:700;color:var(--teal)}
.verdict .rs{margin:2px 0 0;font-size:12.5px}
/* diagrams */
.flow{display:flex;align-items:stretch;gap:6px}
.fcol{flex:1;display:flex;flex-direction:column;gap:5px;min-width:0}
.fh{margin:0;font-weight:700;font-size:12.5px;color:var(--teal)}
.fb{background:#EEF4F5;border:1px solid #C9DCDF;padding:7px;font-size:13px;line-height:1.35;border-radius:3px;flex:1}
.fb.gold{background:#FBF3E6;border-color:#D9AE6E}
.fb small{color:var(--muted);display:block;margin-top:3px}
.farrow{align-self:center;color:var(--p2);font-size:18px}
.tl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 14px}
.tli{border-top:2px solid var(--p2);padding:4px 2px;font-size:13px}
.tly{display:block;font-weight:700;color:var(--teal)}
.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 16px;margin:8px 0}
.card{border-top:2px solid var(--p1);padding:6px 2px 4px}
.card p{margin:0 0 3px}
.ct{font-weight:700;color:var(--teal)}.cm{font-size:13.5px}.cn{font-size:13px;color:var(--muted)}
.plants{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.plant{border:1px solid var(--line);border-top:3px solid var(--p1);padding:8px;font-size:13px}
.plant p{margin:0 0 4px}.pn{font-weight:700;color:var(--teal);font-size:15px}.pl{color:var(--muted);font-size:12px}
.pu{font-weight:700}.pr{font-size:12.5px}
.risks{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 16px}
.risk{border-top:2px solid var(--p2);padding:6px 2px;font-size:13.5px}
.risk p{margin:0 0 4px}.rid{font-weight:700;color:var(--teal)}.thr{font-size:13px}
.cols2{display:grid;grid-template-columns:1fr 1fr;gap:4px 24px}
.gl dt{font-weight:700;color:var(--teal);margin-top:6px}.gl dd{margin:0;font-size:13.5px}
.srcs{font-size:13px;padding-left:22px}
.foot{display:flex;justify-content:space-between;border-top:1px solid var(--line);margin:8px 26px 0;padding:7px 0 10px;font-size:11.5px;color:var(--muted)}
.topnav{display:none}
@media screen and (max-width:1240px){.wrap{grid-template-columns:180px minmax(0,1fr)}}
@media screen and (max-width:820px){
 .cw-d{display:none}.cw-m{display:block}
 .duo,.cover,.cols2,.cards,.risks{grid-template-columns:minmax(0,1fr)}
 .plants{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
 .flow{flex-direction:column}.farrow{transform:rotate(90deg)}
 .t{font-size:12.5px}.t th,.t td{padding:4px 5px}
 .t.fin td,.t.fin th{font-size:11.5px;padding:3px 3px}
}
.mob{display:none}
@media screen and (max-width:600px){
 .t.peer td:nth-child(4),.t.peer th:nth-child(4),.t.peer td:nth-child(5),.t.peer th:nth-child(5),
 .t.peer td:nth-child(8),.t.peer th:nth-child(8){display:none}
 .t.peer td.l{white-space:normal}
 .mob{display:inline}
}
@media screen and (max-width:768px){
 .wrap{display:block;padding:0}
 .side{display:none}
 .topnav{display:block;background:var(--teal);padding:10px 16px}
 .topnav p{margin:0 0 6px;color:#fff;font-weight:700}
 .topnav ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:4px 12px}
 .topnav a{color:#DDF0F2;font-size:13px;text-decoration:none}
 .page{margin:0 0 10px;border-left:0;border-right:0}
 .inner{padding:14px 16px 8px}.band{padding:7px 16px}.foot{margin:6px 16px 0}
 .band span:last-child{display:none}
 h2{font-size:21px}.ctitle{font-size:27px}
}
@media screen and (max-width:480px){.plants{grid-template-columns:minmax(0,1fr)}}
@page{size:A4;margin:36pt}
@media print{
 body{background:#fff;font-size:10pt;line-height:1.3}
 .wrap{display:block;padding:0}.side,.topnav{display:none}
 .page{margin:0;border:0;break-before:page}
 .page:first-child{break-before:auto}
 .inner{padding:8pt 0 0}.band{padding:5pt 8pt;font-size:8.5pt}.foot{margin:6pt 0 0;font-size:7.5pt}
 h2{font-size:14pt}h3{font-size:11.5pt}h4{font-size:10.5pt}.ctitle{font-size:22pt}.csub{font-size:13pt}
 .answer{font-size:10.5pt}.lede{font-size:11pt}
 .t{font-size:8.5pt}.t.fin td,.t.fin th{font-size:8pt}.t.kv td{font-size:8.5pt}
 .src,.tiny,.foot{font-size:7.5pt}.xnote,.small{font-size:8.5pt}
 figcaption{font-size:10pt}
 .t th{border-bottom-width:.6pt}.t td{border-bottom-width:.35pt}
 .cover{grid-template-columns:minmax(0,1fr) 190pt}
 tr,.card,.risk,.plant,.fb{break-inside:avoid}
 h3,h4,figcaption{break-after:avoid}
 a{color:inherit;text-decoration:none}
}
"""


def render():
    total = len(SECTIONS)
    side = ['<nav class="side" aria-label="Contents"><p class="brand">Concord Biotech</p><p class="sub">Company study, 9 Nov 2026</p>']
    top = ['<nav class="topnav" aria-label="Contents"><p>Contents</p><ol>']
    cur = None
    for sid, part, short, *_ in SECTIONS:
        if part != cur:
            if cur is not None:
                side.append("</ol>")
            side.append(f'<p class="pt">{PARTS.get(part, "Appendix")}</p><ol>')
            cur = part
        num = sid.upper() if sid != "appendix" else "App."
        side.append(f'<li><a href="#{sid}"><span class="n">{num}</span>{short}</a></li>')
        top.append(f'<li><a href="#{sid}">{num} {short}</a></li>')
    side.append("</ol></nav>")
    top.append("</ol></nav>")
    out = []
    for i, (sid, part, short, kicker, headline, html) in enumerate(SECTIONS):
        band = ('<div class="band"><span><b>CONCORD BIOTECH</b> &nbsp;|&nbsp; NSE: CONCORDBIO &nbsp;|&nbsp; Company study</span>'
                '<span>9 November 2026</span></div><div class="rule"></div>')
        if sid == "s1":
            head = ('<p class="kicker">NSE: CONCORDBIO &nbsp;|&nbsp; BSE: 543960 &nbsp;|&nbsp; Fermentation APIs</p>'
                    '<h1 class="ctitle">Concord Biotech Ltd</h1>'
                    '<p class="csub">A pause in volume, a step down in margin, and a price that expects a full recovery</p>'
                    '<p class="cmeta">Company study, not a recommendation &nbsp;|&nbsp; Data as of 9 November 2026 &nbsp;|&nbsp; Rs crore unless stated &nbsp;|&nbsp; Per-share figures after the 1:1 bonus</p>')
            inner = head + f'<p class="kicker">{kicker}</p><h2>{headline}</h2>' + html
        else:
            inner = f'<p class="kicker">{kicker}</p><h2>{headline}</h2>{html}'
        out.append(f'<section class="page" id="{sid}">{band}<div class="inner">{inner}</div>'
                   f'<div class="foot"><span>Concord Biotech | Company study | Not investment advice</span><span>{i + 1} / {total}</span></div></section>')
    body = "".join(out)
    cnt = [0]

    def _renum(m):
        cnt[0] += 1
        return f"<figcaption>Exhibit {cnt[0]}:"
    body = re.sub(r"<figcaption>Exhibit \d+:", _renum, body)
    html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Concord Biotech Study</title>'
            '<meta name="description" content="Plain-language, chart-led company study of Concord Biotech (NSE: CONCORDBIO), data as of 9 Nov 2026.">'
            f'<style>{CSS}</style></head><body>{"".join(top)}<div class="wrap">{"".join(side)}<main>{body}</main></div></body></html>')
    assert "—" not in html and "–" not in html, "em or en dash found"
    with open(os.path.join(HERE, "report.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    with open(os.path.join(HERE, "chart-data.json"), "w", encoding="utf-8") as fh:
        json.dump({"data": D, "calc": CALC, "sources": SRC, "valuation_readout": READOUT}, fh, indent=1, ensure_ascii=False, default=str)
    return html, cnt[0]


if __name__ == "__main__":
    h, nex = render()
    print("sections", len(SECTIONS), "exhibits", nex, "bytes", len(h))
    print("base", round(base_v), "bear", round(bear_v), "bull", round(bull_v), "need19", round(n19, 1), f"{n19g:+.3f}",
          "need20", round(n20, 1), f"{n20g:+.3f}", "cagr24_26", round(CALC["cagr_24_26"], 4), "unit3yrs", round(CALC["unit3_80_years"], 2))
