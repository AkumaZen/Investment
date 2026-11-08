"""Build the plain-language, chart-led Augmont report (v3).

Run:  python -I build_v3.py      (from this folder)
Out:  augmont-report.html, chart-data.json

All figures are INR crore unless stated. Sources are attached to every exhibit.
Derived numbers are computed here (see CALC) so they can be re-checked.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import charts as C  # noqa: E402


def _responsive(fn):
    """Full-width charts get a second, phone-sized drawing so labels stay readable on small screens."""
    def wrap(*a, **kw):
        w = kw.get("w", 520)
        if w < 600:
            return fn(*a, **kw)
        mk = dict(kw, w=360)
        if kw.get("h"):
            mk["h"] = int(kw["h"] * 0.95)
        return f'<div class="cw-d">{fn(*a, **kw)}</div><div class="cw-m">{fn(*a, **mk)}</div>'
    return wrap


for _n in ("bars", "grouped", "stacked", "bar_line", "hbars", "waterfall", "diverging"):
    setattr(C, _n, _responsive(getattr(C, _n)))

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- sources
SRC = {
    "deck": ("Company Q2 FY27 investor presentation, 4 Nov 2026",
             "https://augmont.com/assets/files/stakeholders/board-meetings/Q2%20FY%202026-27_Investor%20Presentation.pdf"),
    "deck1": ("Company Q1 FY27 investor presentation, 21 Sep 2026",
              "https://augmont.com/assets/files/stakeholders/board-meetings/Investors%20presentation%20for%20financial%20results_June%20Quarter%202026.pdf"),
    "res": ("Q2 FY27 results filing (board outcome), 4 Nov 2026",
            "https://augmont.com/assets/files/stakeholders/board-meetings/Outcome%20of%20Board%20Meeting%20dated%2004%20November%202026.pdf"),
    "ar": ("Annual Report FY2025-26",
           "https://augmont.com/assets/files/stakeholders/financials/Annual%20Report%202025-26.pdf"),
    "pros": ("IPO prospectus, 25 Aug 2026",
             "https://augmont.com/assets/files/stakeholders/ipo%20disclosures/Project%20Almond%20-%20Prospectus%20%28filing%20version%29%28signed%29.pdf"),
    "scr": ("Screener.in (consolidated and standalone), fetched 7 Nov 2026",
            "https://www.screener.in/company/AUGMONT/consolidated/"),
    "call": ("Q2 FY27 earnings call transcript, 5 Nov 2026 (machine transcript)", None),
    "sebi": ("SEBI caution on digital gold, 8 Nov 2025",
             "https://www.sebi.gov.in/sebi_data/attachdocs/nov-2025/1762580259409.pdf"),
    "nse": ("NSE press release on EGR partner, 26 Sep 2026",
            "https://nsearchives.nseindia.com//web/pressrelease/2026-09/PR_cc_26092026_20260926125056.pdf"),
}


def src(*items):
    """items: key or (key, page). Returns a short linked source line."""
    parts = []
    for it in items:
        key, pg = (it, None) if isinstance(it, str) else it
        name, url = SRC[key]
        label = name + (f", p.{pg}" if pg else "")
        if url:
            u = url + (f"#page={str(pg).split('-')[0].split(',')[0]}" if pg else "")
            parts.append(f'<a href="{u}">{label}</a>')
        else:
            parts.append(label)
    return "Source: " + "; ".join(parts) + "."


# ---------------------------------------------------------------- data
D = {
    "price": {"cmp": 922, "mcap": 8420.07, "hi52": 1405, "lo52": 798, "ipo_price": 788,
              "shares_cr": 9.1373505, "fv": 5},
    "share_sep26": {"Promoters": 81.91, "FIIs": 1.78, "DIIs": 2.92, "Public": 13.37, "holders": 62362},
    # consolidated annual (Screener; FY26 matches audited AR p84)
    "years": ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"],
    "rev": [20641, 25865, 30513, 34921, 66231, 94186],
    "op": [11, 37, 70, 106, 305, 387],
    "oi": [26, 7, 10, 27, 21, 96],
    "pat": [19, 32, 40, 76, 227, 348],
    "sa_pat": [18, 32, 39, 57, 111, 153],
    "cfo": [None, 53, -55, 97, 105, -42],
    # deck p31 (consolidated, incl. other income in EBITDA)
    "deck31": {"cats": ["FY24", "FY25", "FY26", "H1 FY27"], "ebitda": [131, 325, 482, 265],
               "pat": [76, 227, 348, 181], "equity": [187, 415, 933, 1728],
               "roe": [49.9, 74.2, 51.0, 27.1], "roce": [49.3, 70.1, 40.3, 24.6]},
    # quarters, consolidated (results p6, Q1 deck p31/42); Q3 FY26 derived
    "q": ["Q1 FY26", "Q2 FY26", "Q3 FY26*", "Q4 FY26", "Q1 FY27", "Q2 FY27"],
    "q_rev": [14551.6, 21692.2, 27948.6, 29993.8, 18945.6, 15835.5],
    "q_pat": [72.0, 112.7, 97.1, 66.6, 60.9, 120.3],
    "q_ebitda": [103.2, 155.8, 130.6, 92.5, 84.1, 180.8],
    "q_sa_pat": [26.7, 34.2, 49.9, 42.0, 21.9, 84.6],
}

CALC = {}


def calc():
    q = D
    CALC["pat_per100"] = [round(p / r * 100, 2) for p, r in zip(q["pat"], q["rev"])]
    CALC["q_margin"] = [round(e / r * 100, 2) for e, r in zip(q["q_ebitda"], q["q_rev"])]
    CALC["owner_ttm"] = round(333.915 - 174.649 + 176.146, 1)
    CALC["pe"] = round(q["price"]["mcap"] / CALC["owner_ttm"], 1)
    CALC["owner_eq"] = round((456.87 + 16510.49) / 10, 1)
    CALC["bvps"] = round(CALC["owner_eq"] / q["price"]["shares_cr"], 0)
    CALC["pb"] = round(q["price"]["mcap"] / CALC["owner_eq"], 1)
    CALC["cash_less_debt"] = round(170.725 - 9.614, 1)
    CALC["ev"] = round(q["price"]["mcap"] - CALC["cash_less_debt"], 0)
    CALC["ttm_ebitda_ex_oi"] = round(385.95 - (259.1 - 64.389) + 217.408, 1)
    CALC["ev_ebitda"] = round(CALC["ev"] / CALC["ttm_ebitda_ex_oi"], 1)
    CALC["vs_ipo"] = round((q["price"]["cmp"] / q["price"]["ipo_price"] - 1) * 100, 0)
    CALC["rev_x"] = round(q["rev"][-1] / q["rev"][0], 1)
    CALC["pat_x"] = round(q["pat"][-1] / q["pat"][0], 0)
    CALC["sum_pat"] = sum(q["pat"][1:])
    CALC["sum_cfo"] = sum(v for v in q["cfo"][1:])
    # checks against filed numbers
    assert abs(sum(q["q_rev"][:4]) - 94186.2) < 1.0, sum(q["q_rev"][:4])
    assert abs(sum(q["q_pat"][:4]) - 348.3) < 0.5
    assert abs(3675.185 + 2159.003 + 846.908 + 6.140 - 6687.236) < 0.01
    assert abs(620 - 47.236 - 572.764) < 1e-9
    return CALC


calc()

# ---------------------------------------------------------------- page helpers
EX = [0]


def exhibit(title, svg, source, note=None):
    EX[0] += 1
    n = f'<p class="xnote">{note}</p>' if note else ""
    return (f'<figure class="ex"><figcaption>Exhibit {EX[0]}: {title}</figcaption>{svg}{n}'
            f'<p class="src">{source}</p></figure>')


def duo(a, b):
    return f'<div class="duo">{a}{b}</div>'


PAGES = []


def page(kicker, headline, body, notes=None, cls=""):
    notes_html = ""
    if notes:
        notes_html = '<aside class="notes"><p class="nh">In short</p>' + "".join(
            f"<p>{n}</p>" for n in notes) + "</aside>"
    PAGES.append((kicker, headline, body, notes_html, cls))


def table(head, rows, cls="", first_left=True, num_cols=None):
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
    t = f'<table class="t {cls}"><thead><tr>{th}</tr></thead><tbody>{"".join(tr)}</tbody></table>'
    return f'<div class="tw">{t}</div>'


def chip(level):
    return f'<span class="chip {level.lower()}">{level}</span>'


f0 = lambda v: f"{v:,.0f}"  # noqa: E731

# ================================================================= PAGE 1
rail = f"""
<div class="rail">
  <div class="rbox verdict"><p class="rk">Base case FY29 value</p><p class="rv">Rs __BASE29__</p>
  <p class="rs">Scenario value at 20x FY29 owner EPS (page 20). Bear Rs __BEAR29__, bull Rs __BULL29__. No rating in this edition.</p></div>
  <div class="rbox"><p class="rh">Company data</p>
  {table(["", ""], [
      ["NSE / BSE", "AUGMONT / 544888"],
      ["Price (7 Nov 2026)", "Rs 922"],
      ["Market cap", "Rs 8,420 cr"],
      ["52-week high / low", "Rs 1,405 / 798"],
      ["IPO price (Aug 2026)", "Rs 788"],
      ["Shares outstanding", "9.14 cr"],
      ["Face value", "Rs 5"],
      ["Sector", "Precious metals"],
  ], cls="kv")}</div>
  <div class="rbox"><p class="rh">Shareholding, Sep 2026 (%)</p>
  {table(["Holder", "%"], [["Promoters", "81.91"], ["DIIs", "2.92"], ["FIIs", "1.78"], ["Public", "13.37"]], cls="kv")}</div>
  <div class="rbox"><p class="rh">Key financials (consolidated, Rs cr)</p>
  {table(["", "FY24", "FY25", "FY26", "H1 FY27"], [
      ["Revenue", "34,921", "66,231", "94,186", "34,781"],
      ["EBITDA*", "131", "325", "482", "265"],
      ["Net profit", "76", "227", "348", "181"],
      ["Profit per Rs 100 sales", "0.22", "0.34", "0.37", "0.52"],
      ["ROE %", "49.9", "74.2", "51.0", "27.1^"],
  ], cls="fin")}
  <p class="tiny">*EBITDA includes other income, as the company reports it. ^Annualised; falls after IPO cash was added.
  {src(("deck", 31), "scr")}</p></div>
</div>"""

summary = f"""
<p class="lede">Augmont buys gold and silver, refines it, and sells it to jewellers, investors and app users.
It is one of India's largest bullion companies. Revenue is huge because it sells the metal itself, but it keeps only a small slice of every sale.</p>

<div class="kpis">
 <div class="kpi"><p class="kn">Rs 94,186 cr</p><p class="kl">FY26 revenue</p></div>
 <div class="kpi"><p class="kn">Rs 348 cr</p><p class="kl">FY26 net profit</p></div>
 <div class="kpi gold"><p class="kn">Rs 120 cr</p><p class="kl">Q2 FY27 profit, a record</p></div>
 <div class="kpi"><p class="kn">24.5%</p><p class="kl">old gold share of buying</p></div>
 <div class="kpi red"><p class="kn">-Rs 578 cr</p><p class="kl">H1 FY27 operating cash</p></div>
 <div class="kpi"><p class="kn">52.3 mn</p><p class="kl">registered consumers</p></div>
</div>
<h3>What the company does</h3>
<p>Augmont runs two platforms on one engine. <b>SPOT</b> is an online bullion counter for about 5,300 jewellers, dealers and manufacturers.
It brought in 93% of FY26 revenue. <b>Gold For All</b> sells coins, digital gold, EMI jewellery and gold-loan services to consumers through apps and partners.
It brought in 7%, but is growing fastest. Behind both sit two refineries with 284 tonnes a year of capacity, the second-largest in India.</p>

<h3>Why revenue is big but profit is small</h3>
<p>In FY26 Augmont sold metal worth Rs 94,186 cr and made Rs 348 cr of profit. That is about 37 paise for every Rs 100 of sales.
So revenue growth alone says little. What matters is the profit made on each gram, and how many days the company's cash stays locked in metal.</p>

<h3>What changed in Q2 FY27</h3>
<p>Revenue fell 27% to Rs 15,836 cr, yet group profit hit a record Rs 120 cr. The core company's profit rose 2.5 times to Rs 85 cr.
The reason: Augmont bought much more old gold (scrap), which pays a better margin but ties up cash for longer. Scrap rose from about 3% to 24.5% of all buying.
A one-off silver import advantage also helped.</p>

<h3>What to watch</h3>
<p>Cash. In the first half of FY27 the business used Rs 578 cr of cash in operations while reporting Rs 181 cr of profit. Money owed by customers jumped to Rs 749 cr.
Management says this was month-end sales that were collected in early October. One promoter-group company bought 27% of FY26 sales.
Management gives no numerical guidance.</p>
"""

PAGES.append(("cover", None, f'<div class="cover"><div class="cmain">{summary}</div>{rail}</div>', "", "p1"))

# ================================================================= PAGE 2: story in charts
s1 = exhibit("Revenue grew 4.6x in five years",
             C.bars(D["years"], D["rev"], "Revenue FY21-FY26", w=270, h=200, highlight=5,
                    cagr=(0, 5, "4.6x")), src("scr"))
s2 = exhibit("Net profit grew about 18x in the same period",
             C.bars(D["years"], D["pat"], "Net profit FY21-FY26", w=270, h=200, highlight=5,
                    cagr=(0, 5, "18x")), src("scr"))
s3 = exhibit("Yet profit is still under 40 paise per Rs 100 of sales",
             C.bars(D["years"], CALC["pat_per100"], "Profit per Rs 100 of sales", dec=2, w=270, h=200,
                    highlight=5, value_labels=[f"Rs {v:.2f}" for v in CALC["pat_per100"]]),
             src("scr") + " Net profit / revenue x 100 (calc.).")
s4 = exhibit("Consumer revenue grew 5.7x in two years",
             C.bars(["FY24", "FY25", "FY26"], [1178, 2835, 6687], "Consumer revenue", w=270, h=200,
                    highlight=2, cagr=(0, 2, "5.7x")), src(("pros", 236)))
s5 = exhibit("Old gold is now a quarter of what Augmont buys",
             C.bars(["Q2 FY26", "Q2 FY27"], [3, 24.5], "Scrap share of buying", dec=1, unit="%", w=270, h=200,
                    highlight=1, value_labels=["~3%", "~24.5%"]), src(("deck", 13)))
s6 = exhibit("Core company profit jumped in Q2 FY27",
             C.bars(D["q"], D["q_sa_pat"], "Standalone quarterly net profit", dec=1, w=270, h=200, highlight=5,
                    hatch={2}), src(("res", 12), "scr") + " *Q3 FY26 = FY26 less other quarters (calc.).")
body = f'<div class="grid3">{s1}{s2}{s3}{s4}{s5}{s6}</div>'
page("The story in charts", "Six charts that explain Augmont", body,
     ["Sales and profit have grown very fast.",
      "But the business keeps well under 1% of sales as profit, so small changes in margin matter a lot.",
      "The newest change is a shift to buying old gold, which lifted the core company's profit in Q2 FY27.",
      "All figures Rs cr unless shown. Consolidated unless marked standalone."])

# ================================================================= PAGE 3: industry
demand = exhibit("India buys roughly 700-800 tonnes of gold a year",
                 C.bars(["2020", "2021", "2022", "2023", "2024", "2025", "2026E"],
                        [446, 797, 774, 761, 803, 711, 700], "India gold demand tonnes", w=360, h=230,
                        hatch={6}, value_labels=["446", "797", "774", "761", "803", "711", "650-750"]),
                 src(("deck", 20)) + " Data: World Gold Council. 2026E is WGC's range.")
mix = exhibit("Jewellery buying fell this year; coins, bars and ETFs rose",
              C.grouped(["Jewellery", "Bars & coins", "Gold ETFs", "Imports", "Recycled"],
                        [("Apr-Jun 2025", [88.8, 46.1, 2.8, 127.4, 23.1], C.GREY),
                         ("Apr-Jun 2026", [75.1, 50.3, 4.2, 98.1, 19.2], C.NAVY)],
                        "India gold flows tonnes", dec=1, w=380, h=240),
              src(("deck", 20)) + " Data: World Gold Council, calendar quarter, tonnes.")
flow = """
<figure class="ex"><figcaption>Exhibit __EX__: How gold moves in India, and where Augmont sits</figcaption>
<div class="flow">
  <div class="fcol"><p class="fh">1. Sources</p><div class="fb">Banks importing pure bars</div><div class="fb">Dore (semi-refined) imports</div>
  <div class="fb">IIBX exchange, GIFT City</div><div class="fb gold">Old gold / scrap from jewellers and people</div></div>
  <div class="farrow">&#9654;</div>
  <div class="fcol"><p class="fh">2. Refiners</p><div class="fb gold">Melt, test, purify to 995/999 bars<br><small>Augmont: 2 refineries, 284 t/yr</small></div></div>
  <div class="farrow">&#9654;</div>
  <div class="fcol"><p class="fh">3. Bullion dealers</p><div class="fb gold">Sell bars to jewellers at live prices<br><small>Augmont SPOT: 5,309 members</small></div></div>
  <div class="farrow">&#9654;</div>
  <div class="fcol"><p class="fh">4. Jewellers / makers</p><div class="fb">Turn bars into jewellery</div></div>
  <div class="farrow">&#9654;</div>
  <div class="fcol"><p class="fh">5. Consumers</p><div class="fb gold">Coins, digital gold, EMI jewellery<br><small>Augmont Gold For All: 52.3 mn registered</small></div></div>
</div>
<p class="loop">&#8634; Old gold flows back to refiners. Management estimates 300-400 tonnes are recycled in India each year. Gold-coloured boxes are where Augmont earns.</p>
<p class="src">__SRC__</p></figure>""".replace("__SRC__", src(("deck", "8-13"), "call"))
EX[0] += 1
flow = flow.replace("__EX__", str(EX[0]))
body = f"""
<p>Indians hold about <b>31,000 tonnes</b> of gold at home, worth roughly US$3.4 trillion. That is close to the value of the whole Indian stock market (US$5.1 trillion),
according to figures the company cites from the World Gold Council. Yet most gold is still bought and sold through small, informal dealers.</p>
<p>Gold reaches buyers in steps: it is imported or recycled, refined to a standard purity, sold to jewellers in bars, and finally sold to people as jewellery or coins.
Each step earns a small margin. Augmont works in four of the five steps.</p>
{flow}
{duo(demand, mix)}
"""
page("Industry", "India is one of the world's biggest gold buyers, and most of the trade is still informal", body,
     ["Household gold is almost as large as the Indian stock market.",
      "Annual demand is about 700-800 tonnes. 2026 is expected at 650-750 t as high prices cut jewellery buying.",
      "Investment buying (coins, bars, ETFs) is rising while jewellery is falling.",
      "Recycling old gold is a big, growing supply source. This matters for Augmont (see page 8)."])

# ================================================================= PAGE 4: competition
cap = exhibit("Augmont has India's second-largest refining capacity",
              C.hbars(["MMTC-PAMP", "Augmont", "Zaveri", "Kundan", "Sovereign", "MD Overseas"],
                      [300, 284, 216, 146, 100, 73], "Refining capacity tonnes per year", unit=" t", highlight=1, w=660),
              src(("deck1", 17)) + " Company-compiled comparison; peers may measure capacity differently.")
dg = exhibit("Digital gold is expected to roughly double by FY30",
             C.bars(["FY20", "FY25", "FY26E", "FY30P"], [5, 25, 30, 55], "Digital gold market tonnes",
                    unit=" t", w=360, h=220, hatch={2, 3}), src(("deck", 20)) + " Data: Technopak (forecast).")
lgd = exhibit("Lab-grown diamond jewellery market (Rs bn)",
              C.bars(["FY20", "FY25", "FY26E", "FY30P"], [16, 30, 36, 63], "LGD jewellery market Rs bn",
                     w=360, h=220, hatch={2, 3}), src(("deck", 20)) + " Data: Technopak (forecast).")
reg = table(["Product", "Who regulates it", "Augmont's role"], [
    ["Gold ETF", "SEBI (mutual funds)", "Supplies metal to fund houses; market maker"],
    ["Electronic Gold Receipt (EGR)", "SEBI, traded on NSE", "NSE-empanelled partner (via Augmont Goldtech)"],
    ["Digital gold (app gold)", "<b>Not SEBI-regulated</b>", "Seller and counterparty; metal held with a custodian"],
    ["Coins, bars, jewellery", "BIS hallmarking rules", "Makes and sells through 751 channel partners"],
], cls="std")
body = f"""
<p>Refining is concentrated in a few players. Augmont's two plants, at Rudrapur (Uttarakhand) and Navi Mumbai, give it 284 tonnes a year of capacity.
On the company's own comparison that is second only to MMTC-PAMP. Capacity is not the same as output, though. Augmont's plants ran far below capacity in FY26 (page 10).</p>
{cap}
{duo(dg, lgd)}
<h4>Not every gold product has the same protection</h4>
{reg}
<p class="src">{src("sebi", "nse", ("deck", 18))}</p>
<p>SEBI warned the public in November 2025 that digital gold sits outside its rules. That does not ban it, but buyers do not get stock-market style protection.
EGRs and ETFs are regulated, and Augmont now has a role in both.</p>
"""
page("Industry and competition", "Augmont is one of the largest refiners, and new gold products are growing fast", body,
     ["Only MMTC-PAMP has more refining capacity in the company's comparison.",
      "Digital gold and lab-grown diamonds are small markets today but expected to grow quickly.",
      "Digital gold is not SEBI-regulated. EGRs and ETFs are. Rule changes here can help or hurt Augmont."])

# ================================================================= PAGE 5: business model
tree = """
<figure class="ex"><figcaption>Exhibit __EX__: Two platforms, one engine (share of FY26 revenue)</figcaption>
<div class="tree">
  <div class="troot">Augmont Enterprises<br><small>FY26 revenue Rs 94,186 cr</small></div>
  <div class="tbranches">
    <div class="tbranch"><div class="tnode navy">Enterprise platform<br><b>92.9%</b></div>
      <div class="tleaf"><b>SPOT</b>: online bullion counter for 5,309 members; live prices, no brokerage, delivery in 2 days from 20 centres</div>
      <div class="tleaf"><b>International</b>: exports, Rs 5,701 cr in FY26</div>
      <div class="tleaf"><b>ETF supply</b>: provides metal to fund houses; market maker</div>
      <div class="tleaf"><b>Refinery sales</b> and diamond marketplace</div></div>
    <div class="tbranch"><div class="tnode gold">Consumer: Gold For All<br><b>7.1%</b></div>
      <div class="tleaf"><b>Coins and bars</b>: Rs 3,675 cr</div>
      <div class="tleaf"><b>Digital gold and silver</b>: Rs 2,159 cr; buy from Rs 10, SIPs</div>
      <div class="tleaf"><b>EMI jewellery</b>: Rs 847 cr; pay over 3/6/9 months</div>
      <div class="tleaf"><b>Gold loans and old-gold exchange</b>: technology for partner lender Finkurve; 122 centres</div></div>
  </div>
  <div class="tengine">Shared engine: 2 refineries (284 t/yr) &middot; pricing engine &middot; partner APIs &middot; vault and delivery network</div>
</div>
<p class="src">__SRC__</p></figure>""".replace("__SRC__", src(("deck", "10-12"), ("pros", "234-236")))
EX[0] += 1
tree = tree.replace("__EX__", str(EX[0]))
tl = [("2012", "Founded in Mumbai; SPOT platform and EMI jewellery start"),
      ("2013", "Digital gold launched"),
      ("2016", "First refinery at Rudrapur, Uttarakhand"),
      ("2020-21", "Gold For All consumer platform built during COVID"),
      ("2023", "Sell Old Gold service starts"),
      ("Aug 2024", "Augmont Goldtech brought into the group"),
      ("Aug 2026", "Listed on NSE and BSE at Rs 788"),
      ("Sep 2026", "NSE names Augmont Goldtech a partner for EGRs")]
EX[0] += 1
timeline = (f'<figure class="ex"><figcaption>Exhibit {EX[0]}: Journey so far</figcaption><div class="tl">'
            + "".join(f'<div class="tli"><span class="tly">{y}</span><span class="tlt">{t}</span></div>' for y, t in tl)
            + f'</div><p class="src">{src(("deck", 6), "call", "nse", ("ar", 122))} The Navi Mumbai refinery was operating by FY24; its start year is not stated.</p></figure>')
body = f"""
<p>Think of Augmont as a wholesale gold shop with a factory behind it. It buys metal from banks, importers and people selling old gold.
It refines some of it. Then it sells bars to jewellers (the big business) and coins or digital gold to the public (the small, fast-growing business).</p>
{tree}
{timeline}
"""
page("Business model", "What Augmont does: two platforms running on one engine", body,
     ["SPOT (business buyers) is 93% of revenue. Gold For All (consumers) is 7% and growing fastest.",
      "Both use the same refineries, pricing engine and delivery network.",
      "Augmont does not lend money in gold loans. Partner lender Finkurve does; Augmont supplies the technology.",
      "Jewellery for EMI sales is made by outside partners."])

# ================================================================= PAGE 6: how it earns
m_chart = exhibit("Profit per Rs 100 of sales has risen, but stays below Re 1",
                  C.bars(D["years"] + ["H1 FY27", "Q2 FY27"], CALC["pat_per100"] + [0.52, 0.76],
                         "Profit per 100 rupees of sales", dec=2, w=660, h=230, highlight=7,
                         value_labels=[f"{v:.2f}" for v in CALC["pat_per100"] + [0.52, 0.76]]),
                  src("scr", ("res", 6)) + " Net profit / revenue x 100, rupees (calc.).")
EX[0] += 1
cycle = f"""
<figure class="ex"><figcaption>Exhibit {EX[0]}: The money cycle: Augmont pays first and gets paid later</figcaption>
<div class="cycle">
  <div class="cstep"><span class="cday">Day 0</span>Augmont pays the supplier in full</div>
  <div class="carrow">&#9654;</div>
  <div class="cstep"><span class="cday">Day 0-2</span>Metal tested, refined if needed, delivered</div>
  <div class="carrow">&#9654;</div>
  <div class="cstep"><span class="cday">Day 2-4</span>Jeweller pays; cash is free to use again</div>
</div>
<div class="duo small">
  <div class="kbox"><p class="kt">Imported pure gold</p><p class="kv">~2 days</p><p class="ks">Fast turns, thin spread</p></div>
  <div class="kbox gold"><p class="kt">Old gold / scrap</p><p class="kv">3-4 days</p><p class="ks">Slower turns, wider spread + refining fee</p></div>
</div>
<p class="src">{src(("deck", 26), ("pros", 135), "call")}</p></figure>"""
body = f"""
<p>Augmont is a <b>principal</b>, not a broker. It buys the metal, owns it for a short time, and sells it. It charges no brokerage.
It earns the gap between its buying and selling price (the <b>spread</b>), plus refining and handling fees on old gold.</p>
<p>Because the full metal value is booked as revenue, sales look enormous and margins look tiny. A better way to judge the business is:
<b>how much profit does each rupee of its own capital earn in a year?</b> That depends on two things: the spread per trade, and how many times the same cash can be reused.</p>
{m_chart}
{cycle}
<div class="callout"><p><b>A simple example (illustration, not company data).</b> If Rs 100 of capital is reused every 2 days, it can do about 150 trades a year.
If it is reused every 4 days, only about 75. So old gold must earn at least twice the spread per trade just to match the yearly profit from imported gold.
Management says it does earn more, but has not disclosed the exact spreads.</p></div>
<p>Banks generally will not lend against gold bought for trading, management says. So growth needs the company's own money (equity).
That is why most of the IPO money went into working capital (page 16).</p>
"""
page("How it earns", "Augmont earns a small spread on a very large volume, so speed of cash matters", body,
     ["Profit per Rs 100 of sales went from 9 paise (FY21) to 76 paise (Q2 FY27).",
      "Revenue mostly reflects gold prices and volumes, not pricing power.",
      "The key numbers to track: spread per gram and days of cash tied up. The company does not disclose either directly."])

# ================================================================= PAGE 7: enterprise
spot = exhibit("SPOT revenue rose in FY26 even though less gold was sold",
               C.bar_line(["FY24", "FY25", "FY26"], [31839, 55340, 81751], [44.04, 61.84, 49.13],
                          "SPOT revenue and gold tonnes", bar_name="SPOT revenue, Rs cr",
                          line_name="Gold sold, tonnes", line_dec=1, w=660, h=250),
               src(("pros", 234)))
chg = exhibit("Q2 FY27 vs Q2 FY26: fewer tonnes at much higher prices",
              C.diverging(["Gold tonnes", "Gold price/g", "Silver tonnes", "Silver price/g"], [-52, 43, -64, 87],
                          "Enterprise volume and price change", w=360),
              src(("deck", 28)) + " Change in % (calc.).")
q2box = ('<div class="ex"><p class="figt">Enterprise metal sales, Q2</p>' + table(["", "Q2 FY26", "Q2 FY27"], [
    ["Gold sold (t)", "15.9", "7.6"], ["Gold price (Rs/g)", "10,351", "14,839"], ["Gold revenue (Rs cr)", "16,483", "11,278"],
    ["Silver sold (t)", "315.4", "113.0"], ["Silver price (Rs/g)", "122", "228"], ["Silver revenue (Rs cr)", "3,863", "2,574"]],
    cls="std") + '<p class="src">' + src(("deck", 28)) + '</p></div>')
body = f"""
<p>The enterprise business sells bars to jewellers, dealers, manufacturers, fund houses and overseas buyers. SPOT, the online counter, is most of it.
Buyers see a live price, place an order, and receive the metal within about two working days from one of 20 delivery centres.</p>
<p>When gold prices rise, revenue can grow even as fewer tonnes are sold. That is exactly what happened in FY26 and again in Q2 FY27.
Management's explanation: the business has a fixed pool of cash, and at higher prices the same cash buys fewer tonnes.</p>
{spot}
{duo(chg, q2box)}
{table(["Enterprise metric", "FY24", "FY25", "FY26"], [
    ["SPOT revenue (Rs cr)", "31,839", "55,340", "81,751"],
    ["Gold sold on SPOT (t)", "44.0", "61.8", "49.1"],
    ["Silver sold on SPOT (t)", "759", "1,035", "1,034"],
    ["SPOT gold transactions", "116,354", "179,008", "99,579"],
    ["International revenue (Rs cr)", "1,631", "8,052", "5,701"],
], cls="std")}
<p class="src">{src(("pros", "234-241"))} SPOT counts include some transactions within the group.</p>
"""
page("Enterprise platform (SPOT)", "Enterprise revenue rose, but tonnes sold fell, because gold got dearer", body,
     ["Revenue tracks the gold price more than real business growth.",
      "FY26 gold tonnes on SPOT fell 21% even as SPOT revenue rose 48%.",
      "In Q2 FY27, enterprise revenue fell 32% to Rs 13,852 cr.",
      "International sales also slowed: Rs 1,806 cr in Q1 FY27 vs Rs 3,696 cr a year earlier."])

# ================================================================= PAGE 8: sourcing
scrap = exhibit("Scrap share of buying rose about eight times in a year",
                C.bars(["Q2 FY26", "Q2 FY27"], [3, 24.5], "Scrap share", dec=1, w=360, h=220, highlight=1,
                       value_labels=["~3%", "~24.5%"]), src(("deck", 13)))
proc = exhibit("FY26 gold buying by type (tonnes)",
               C.hbars(["Pure gold bars", "Dore (to refine)", "Scrap (old gold)"], [65.56, 10.78, 3.49],
                       "FY26 gold procurement", dec=1, unit=" t", w=660, highlight=2),
               src(("pros", "237-250")) + " FY26 buying was 82% domestic, 18% imported (by value).")
sog = exhibit("Old gold bought from consumers rose 4.3x (Q1, Rs cr)",
              C.bars(["Q1 FY26", "Q1 FY27"], [414, 1798], "Sell old gold amount", w=360, h=220, highlight=1),
              src(("deck1", 23)) + " Value of old gold bought, not revenue.")
body = f"""
<p>Augmont buys gold from five places: Indian banks that import it, foreign banks, dore (semi-refined) imports, the IIBX exchange in GIFT City,
and <b>old gold</b> from jewellers and the public. Old gold has to be tested and refined before it can be sold as bars.</p>
<p>In the last year Augmont pushed hard into old gold. It now makes up about a quarter of all buying. Management gives three reasons:
it earns a better margin (spread plus a refining fee), it builds loyalty with jewellers, and it supports the government's aim of cutting imports.
The cost is that cash stays tied up for 3-4 days instead of about 2.</p>
{duo(scrap, sog)}
{proc}
<div class="callout"><p><b>Two separate profit boosts in Q2 FY27.</b> 1) More old gold: management calls this lasting ("structural").
2) Silver: when silver imports were restricted, Augmont held a government (DGFT) licence and imported via IIBX while others struggled.
Management itself calls this "situational", meaning it should not be expected to repeat. The split between the two was not disclosed.</p></div>
"""
page("Sourcing", "Old gold (scrap) jumped from 3% to 24.5% of buying, lifting margins", body,
     ["Buying more old gold raised profit per gram but slowed cash turns.",
      "Part of the Q2 profit came from a temporary silver import advantage.",
      "Management expects scrap to stay at 'healthy levels' but gave no number.",
      "Watch: scrap share and margin in Q3 FY27."])

# ================================================================= PAGE 9: consumer
cons = exhibit("Consumer revenue by product (Rs cr)",
               C.stacked(["FY24", "FY25", "FY26"],
                         [("Coins and bars", [539.2, 1651.5, 3675.2], C.NAVY),
                          ("Digital gold/silver", [288.4, 664.6, 2159.0], C.GOLD),
                          ("EMI jewellery", [342.2, 515.9, 846.9], C.SLATE),
                          ("Gold-loan tech", [8.4, 3.0, 6.1], C.GREY)], "Consumer revenue mix", w=660, h=260),
               src(("pros", 236)))
growth = exhibit("Q1 FY27 growth vs Q1 FY26 (%)",
                 C.hbars(["Old gold bought", "Gold-loan book*", "Digital gold", "EMI jewellery", "Coins and bars"],
                         [335, 134, 121, 66, 65], "Q1 growth", unit="%", w=360, highlight={0}),
                 src(("deck1", "22-23")) + " *Loans made by partner lender, not on Augmont's books.")
tx = exhibit("More transactions, and bigger ones",
             C.bar_line(["FY24", "FY25", "FY26"], [28.5, 35.7, 54.9], [224, 331, 548], "Gold For All transactions",
                        bar_name="Transactions (mn)", line_name="Average ticket (Rs)", bar_dec=1, line_dec=0,
                        w=360, h=230), src(("pros", 241)))
body = f"""
<p>Gold For All sells gold to ordinary people in small amounts. It works through apps and partners rather than its own shops:
245 partner brands embed Augmont's digital gold, 751 channel partners sell coins, and products are also sold on Zepto, Amazon and Flipkart.</p>
<p>It is only 7% of revenue, but it is growing much faster than the enterprise side. In Q2 FY27 consumer revenue rose 47% to Rs 1,984 cr,
about 13% of the quarter's revenue.</p>
{cons}
{duo(growth, tx)}
<p><b>A note on user numbers.</b> Augmont reports 52.3 million <i>registered</i> consumers (Sep 2026). That counts sign-ups across partner apps,
not active buyers. The company does not disclose active users or repeat rates.</p>
"""
page("Consumer platform (Gold For All)", "The consumer business is small but growing fastest", body,
     ["Consumer revenue grew from Rs 1,178 cr (FY24) to Rs 6,687 cr (FY26).",
      "Coins and digital gold drive most of it.",
      "Average purchase size more than doubled to Rs 548, helped by higher gold prices.",
      "Registered users (52.3 mn) are not the same as active customers."])

# ================================================================= PAGE 10: network and refineries
kpi = table(["Network", "Jun 2026", "Sep 2026", "Change"], [
    ["Gold For All stores", "118", "122", "+4"],
    ["Fintech partners", "231", "245", "+14"],
    ["Coin distribution partners", "731", "751", "+20"],
    ["Retail touchpoints", "5,517", "5,558", "+41"],
    ["SPOT registered members", "5,271", "5,309", "+38"],
    ["Registered consumers (mn)", "50.6", "52.3", "+1.7"],
    ["SPOT delivery centres", "20", "20", "plan: 35"],
], cls="std")
ref = exhibit("Refinery output was far below capacity (tonnes)",
              C.grouped(["FY24", "FY25", "FY26"],
                        [("Rudrapur", [12.35, 4.52, 1.34], C.NAVY), ("Navi Mumbai", [2.63, 10.56, 11.95], C.GOLD)],
                        "Refinery actual output", dec=1, w=660, h=230),
              src(("pros", "253-254")) + " Capacity: Rudrapur 144 t, Navi Mumbai 140 t a year. FY26 use: 0.9% and 8.5%.")
body = f"""
<p>Augmont's reach keeps widening, slowly. Management plans to grow delivery centres from 20 to 35 over the next couple of years. It has picked 10 sites to open in FY27.</p>
{kpi}
<p class="src">{src(("deck", 7), "call")}</p>
{ref}
<p>The refineries ran at a small fraction of capacity in FY26. Management says this is by design: plants are sized to process a large batch quickly so costly metal is not stuck waiting,
and idle equipment costs little to keep. That is plausible. But it also means refining is a support function today, not a big profit source on its own.
More old gold should raise refinery use; the company has not published FY27 output.</p>
<div class="callout warn"><p><b>Jaipur jewellery plant fire, 22 Oct 2026.</b> A fire temporarily disrupted manufacturing at the group's Jaipur jewellery facility
(capacity 13.8 t a year, 47% used in FY26). No loss amount, insurance claim or restart date was given. {src(("res", 7))}</p></div>
"""
page("Network and capacity", "Reach is wide; the refineries are mostly idle by design", body,
     ["The network grew a little in one quarter. Big expansion is planned, not done.",
      "Combined refinery use was about 4.7% in FY26 (13.3 t of 284 t, calc.).",
      "The Rudrapur refinery lease runs to May 2027 (prospectus p.257).",
      "A fire at the Jaipur jewellery plant is a near-term watch item."])

# ================================================================= PAGE 11: group
ent = exhibit("FY26 profit by group company (Rs cr)",
              C.hbars(["Parent company", "Ideal Fiscal", "Augmont Goldtech"],
                      [152.8, 135.2, 61.0], "FY26 PAT by entity", dec=1, w=360, colors=[C.NAVY, C.GOLD, C.GOLD]),
              src(("ar", 131)) + " Before minority share. The other three subsidiaries made a combined loss of Rs 0.7 cr.")
wf = exhibit("Q2 FY27: parent profit rose Rs 50 cr, but the rest of the group gave back Rs 39 cr",
             C.waterfall([("Q2 FY26|owner profit", 106.5, "total"), ("Parent|company", 50.5, "up"),
                          ("Subsidiaries|& adjustments", 38.6, "down"), ("Q2 FY27|owner profit", 118.4, "total")],
                         "Owner profit bridge", w=360, h=250),
             src(("res", "6, 12")) + " Owner profit = profit belonging to Augmont shareholders. Middle bar is the balancing figure (calc.).")
EX[0] += 1
gtree = f"""
<figure class="ex"><figcaption>Exhibit {EX[0]}: Group structure (ownership at Sep 2026)</figcaption>
<div class="gtree">
 <div class="gparent">Augmont Enterprises Ltd (listed)<br><small>SPOT, refineries, enterprise trading</small></div>
 <div class="gkids">
  <div class="gk gold">Ideal Fiscal Services<br><b>91%</b><br><small>gold jewellery</small></div>
  <div class="gk gold">Augmont Goldtech<br><b>96.4%</b><br><small>Gold For All / digital gold platform</small></div>
  <div class="gk">Augmont International<br><b>100%</b><br><small>trading</small></div>
  <div class="gk">Augmont IFSC<br><b>100%</b><br><small>GIFT City trading</small></div>
  <div class="gk">Augmont Trading<br><b>100%</b><br><small>SEBI-registered broker</small></div>
 </div>
</div><p class="src">{src(("res", 7), ("ar", 124), ("deck", 6))}</p></figure>"""
body = f"""
<p>Augmont is a group of six companies. The listed parent runs SPOT and the refineries. Two subsidiaries, Ideal Fiscal Services and Augmont Goldtech,
earned more than half of FY26 group profit. Small outside shareholders own 9% and 3.6% of them, so a slice of their profit does not belong to Augmont's shareholders.</p>
{gtree}
{duo(ent, wf)}
<p>This explains why the company talks about two different profit numbers. The <b>parent</b> ("core") profit rose 2.5 times in Q2 FY27.
<b>Group</b> profit belonging to shareholders rose only 11%, from Rs 106.5 cr to Rs 118.4 cr, because the rest of the group (subsidiaries, minority share and consolidation adjustments)
contributed Rs 39 cr less than a year earlier. The filings do not break this down. Investors should use the group figure.</p>
"""
page("Group structure", "More than half of group profit comes from subsidiaries", body,
     ["Parent: 44% of FY26 group profit. Ideal Fiscal: 39%. Goldtech: 18%.",
      "The 'core profit up 2.5x' headline is the parent only.",
      "Profit belonging to Augmont shareholders rose 11% in Q2 FY27.",
      "Minority holders' share of FY26 profit: Rs 14.4 cr."])

# ================================================================= PAGE 12: quarter
qt = table(["Rs cr", "Q2 FY27", "Q2 FY26", "YoY", "Q1 FY27", "QoQ"], [
    ["Revenue", "15,836", "21,692", "-27.0%", "18,946", "-16.4%"],
    ["EBITDA (incl. other income)", "180.8", "155.8", "+16.0%", "84.1", "+115%"],
    ["EBITDA margin", "1.14%", "0.72%", "+42 bps", "0.44%", "+70 bps"],
    ["Other income", "16.5", "61.7", "-73%", "31.0", "-47%"],
    ["Finance cost", ("18.1", "flag"), "0.4", "n.m.", "0.4", "n.m."],
    ["Profit before tax", "160.7", "153.7", "+4.5%", "81.8", "+96%"],
    ["Net profit (group)", "120.3", "112.7", "+6.8%", "60.9", "+98%"],
    ["Owner profit (group)", ("118.4", "bold"), "106.5", ("+11.2%", "bold"), "57.7", "+105%"],
    ["Parent (standalone) profit", "84.6", "34.2", "+148%", "21.9", "+286%"],
], cls="std")
qrev = exhibit("Quarterly revenue (Rs cr)",
               C.bars(D["q"], D["q_rev"], "Quarterly revenue", w=360, h=220, hatch={2}),
               src(("res", 6), ("deck1", 31)) + " *Q3 FY26 derived (calc.).")
qpat = exhibit("Quarterly profit: group vs parent (Rs cr)",
               C.grouped(D["q"], [("Group", D["q_pat"], C.NAVY), ("Parent", D["q_sa_pat"], C.GOLD)],
                         "Quarterly profit", dec=0, w=360, h=220),
               src(("res", "6, 12"), "scr") + " *Q3 FY26 derived (calc.).")
qm = exhibit("EBITDA margin hit a record 1.14%",
             C.bars(D["q"], CALC["q_margin"], "Quarterly EBITDA margin", dec=2, unit="%", w=660, h=220, highlight=5, hatch={2}),
             src(("res", 6), ("deck1", 31)) + " EBITDA incl. other income / revenue (calc.).")
body = f"""
<p>Q2 FY27 (July-September 2026) was the first full quarter after listing. Revenue fell sharply, but margins and profit rose.</p>
{qt}
<p class="src">{src(("res", "6, 12"), ("deck", 29))}</p>
{duo(qrev, qpat)}
{qm}
<p><b>Two things the filings do not explain:</b> finance cost jumped to Rs 18.1 cr from Rs 0.4 cr, though borrowings at 30 Sep were only about Rs 2.6 cr.
And other income fell to Rs 16.5 cr from Rs 61.7 cr. Both are worth asking management about.</p>
"""
page("Q2 FY27 results", "Record profit on lower revenue", body,
     ["Revenue -27% YoY; group net profit +7%; owner profit +11%.",
      "Margin more than doubled vs Q1, driven by old gold and silver.",
      "Finance cost of Rs 18 cr is unexplained and new.",
      "Q3 FY26 is derived from annual less other quarters, so treat it as approximate."])

# ================================================================= PAGE 13: concall
body = """
<div class="cols2">
<div><h4>Margins and sourcing</h4><ul>
<li>Old gold rose to about 24.5% of buying from about 3%. Management expects scrap to stay at "healthy levels" but gave no target.</li>
<li>Old gold earns the bid-ask spread plus a handling and refining fee. Management would not share the exact margin gap vs imported gold: "market determined".</li>
<li>The silver gain came from holding a DGFT licence during import curbs. Management called it situational.</li>
<li>"Our focus is not on maintaining a particular margin," said management; it depends on prices, supply and mix.</li>
</ul></div>
<div><h4>Cash and capital</h4><ul>
<li>Customers' unpaid bills jumped because of month-end sales. Management says these were collected within a couple of working days in October.</li>
<li>Asked if Rs 700-800 cr of receivables could recur, management said it would "not be a common recurrence".</li>
<li>Banks do not fund gold stock for trading, so growth needs equity. IPO money has been put into working capital.</li>
<li>Management would not link a revenue or profit number to the new working capital.</li>
</ul></div>
<div><h4>Growth plans</h4><ul>
<li>EGR: NSE picked Augmont as a partner. Management expects the product to start "this quarter" (Q3 FY27) but said it is too early to size.</li>
<li>Delivery centres: 20 today, aiming for 35 in a couple of years; 10 sites identified for FY27.</li>
<li>Wants LBMA accreditation for its refinery (global standard). No date given.</li>
<li>More products for jewellers on SPOT: diamonds, alloys, chemicals.</li>
</ul></div>
<div><h4>What was not given</h4><ul>
<li>No FY27 revenue, margin or profit guidance: "we'll just not be able to provide any specific numerical guidance".</li>
<li>No volume numbers by segment, no refinery use, no active users.</li>
<li>No split of Q2 profit between the old-gold gain and the silver gain.</li>
<li>Note: the transcript is machine-generated, so names and some figures may be misheard (e.g. it says Rs 625 cr primary issue; the prospectus says Rs 620 cr).</li>
</ul></div>
</div>
<p class="src">Source: Q2 FY27 earnings call transcript, 5 Nov 2026 (machine transcript). Quotes are reproduced as transcribed.</p>
"""
page("Earnings call", "What management said on the Q2 FY27 call", body,
     ["The margin story rests on old gold, which management calls lasting.",
      "The silver gain is not expected to repeat.",
      "No numerical guidance for FY27.",
      "EGR and new delivery centres are the near-term growth items."])

# ================================================================= PAGE 14: track record
rp = exhibit("Revenue and profit, FY21-FY26",
             C.bar_line(D["years"], D["rev"], D["pat"], "Revenue and profit", bar_name="Revenue, Rs cr",
                        line_name="Net profit, Rs cr", line_dec=0, w=660, h=250), src("scr"))
roe = exhibit("Returns are high, but are falling as IPO cash comes in (%)",
              C.grouped(D["deck31"]["cats"], [("ROE", D["deck31"]["roe"], C.NAVY), ("ROCE", D["deck31"]["roce"], C.GOLD)],
                        "ROE and ROCE", dec=1, w=360, h=220), src(("deck", 31)) + " H1 FY27 annualised.")
eq = exhibit("Shareholders' equity grew 9x in two and a half years (Rs cr)",
             C.bars(D["deck31"]["cats"], D["deck31"]["equity"], "Total equity", w=360, h=220, highlight=3),
             src(("deck", 31)) + " Includes Rs 620 cr IPO in Aug 2026.")
body = f"""
<p>Over five years revenue grew {CALC['rev_x']}x and profit about {CALC['pat_x']:.0f}x. Most of the jump came in FY25 and FY26, helped by rising gold prices,
a bigger consumer business and better margins. Return on equity has been very high (about 50-74%) because the business needs little equipment and profit was
earned on a small equity base.</p>
{rp}
{duo(roe, eq)}
<p>Return ratios will look lower for a while. Equity nearly doubled after the IPO in August 2026, and that cash needs time to earn.
Annualised H1 FY27 ROE was 27%.</p>
"""
page("Track record", "Six years of fast growth, with high returns on a small equity base", body,
     [f"Revenue {CALC['rev_x']}x and profit about {CALC['pat_x']:.0f}x from FY21 to FY26.",
      "ROE of 51% in FY26 is high, but will fall as IPO money is put to work.",
      "Growth was helped by gold prices; tonnes sold did not grow the same way (page 7)."])

# ================================================================= PAGE 15: cash
cash = exhibit("Profit vs cash from operations (Rs cr)",
               C.grouped(["FY22", "FY23", "FY24", "FY25", "FY26", "H1 FY27"],
                         [("Net profit", [32, 40, 76, 227, 348, 181], C.NAVY),
                          ("Cash from operations", [53, -55, 97, 105, -42, -578], C.GOLD)],
                         "Profit vs CFO", w=660, h=260),
               src("scr", ("ar", 85), ("res", 9)))
recv = exhibit("Money owed by customers jumped (Rs cr)",
               C.bars(["Mar 2025", "Mar 2026", "Sep 2026"], [38.4, 181.7, 749.1], "Trade receivables",
                      dec=0, w=360, h=220, highlight=2), src(("ar", 83), ("res", 8)))
EX[0] += 1
cashbox = f"""
<figure class="ex"><figcaption>Exhibit {EX[0]}: Not all cash is free cash (Sep 2026, Rs cr)</figcaption>
{table(["Item", "Rs cr"], [
    ["Cash and cash equivalents", "170.7"],
    ["Other bank balances (much under lien in FY26)", "50.3"],
    ["Borrowings + lease liabilities", "(9.6)"],
    ["Cash less debt (calc.)", ("161.1", "bold")],
], cls="std")}
<p class="xnote">In FY26, Rs 64.3 cr of deposits were under lien or frozen, including Rs 10.1 cr frozen in a cyber-fraud case on digital gold sales (under court review).</p>
<p class="src">{src(("res", 8), ("ar", "104, 132"))}</p></figure>"""
body = f"""
<p>This is the most important open question. A trading business should turn profit into cash quickly. Augmont has not done so recently.
From FY22 to FY26 it reported Rs {CALC['sum_pat']:,} cr of profit but only Rs {CALC['sum_cfo']:,} cr of cash from operations.
In H1 FY27 operations <b>used</b> Rs 578 cr while profit was Rs 181 cr. The IPO money largely filled this gap.</p>
{cash}
{duo(recv, cashbox)}
<p><b>Management's explanation:</b> large sales on the last days of September were collected in the first days of October, so the 30 Sep snapshot looks worse than normal.
That may be right, and the Q3 results will show it. But in FY26 too, most receivables were owed by a single related company (page 17),
and operating cash was negative. Two clean quarters of cash would go a long way.</p>
"""
page("Cash flow", "Profit is not yet turning into cash", body,
     ["FY22-FY26: Rs 723 cr profit, Rs 158 cr operating cash.",
      "H1 FY27: Rs 578 cr cash used vs Rs 181 cr profit.",
      "Receivables went from Rs 182 cr (Mar 2026) to Rs 749 cr (Sep 2026).",
      "Watch the Q3 FY27 balance sheet: did receivables come back down?"])

# ================================================================= PAGE 16: IPO
ipo = exhibit("Of the Rs 825 cr IPO, Rs 573 cr reached the company",
              C.waterfall([("Total|offer", 825, "total"), ("Sold by|promoters (OFS)", 205, "down"),
                           ("Fresh|issue", 620, "total"), ("Issue|expenses", 47.2, "down"),
                           ("Net to|company", 572.8, "total")], "IPO bridge", dec=0, w=660, h=250),
              src(("pros", "107, 130")))
use = exhibit("How the net money was planned to be used (Rs cr)",
              C.hbars(["Working capital", "General corporate purposes"], [465.0, 107.8], "Use of IPO proceeds",
                      dec=1, w=660, highlight={0}), src(("pros", "130-131"), ("res", 16))
              + " Company reports Rs 573.4 cr used by 30 Sep 2026, with no deviation.")
body = f"""
<p>Augmont listed in August 2026 at Rs 788 a share. The issue had two parts. In the <b>offer for sale</b>, three promoter-family members sold
shares for Rs 205 cr; that money went to them, not to the company. In the <b>fresh issue</b>, the company raised Rs 620 cr of new money.</p>
{ipo}
{use}
<p>Almost all of it was spent on working capital, meaning metal and supplier advances, within weeks. That matches the business need explained on page 6.
It also means future growth needs more profit kept in the business, or more equity. Management would not say how much extra revenue or profit the new money should bring.</p>
<p>The selling shareholders' average cost was Rs 1.86 a share (prospectus p.1). Promoters still own 81.9%. No promoter shares were pledged at the IPO.</p>
"""
page("IPO and use of money", "IPO money went straight into working capital", body,
     ["Rs 620 cr fresh issue; Rs 573 cr after costs.",
      "Rs 465 cr earmarked for working capital, Rs 108 cr for general use.",
      "The company says all of it was used by 30 Sep 2026.",
      "A CARE Ratings monitoring agency reports on use each quarter."])

# ================================================================= PAGE 17: concentration
cust = exhibit("FY26 customer and supplier concentration (% of total)",
               C.grouped(["Top 1", "Top 5", "Top 10"],
                         [("Customers (share of sales)", [27.44, 46.32, 52.09], C.NAVY),
                          ("Suppliers (share of buying)", [19.93, 58.24, 74.18], C.GOLD)],
                         "Concentration", dec=1, w=660, h=240),
               src(("pros", "32, 251")) + " Top customer is RSBL, a promoter-group company.")
geo = exhibit("SPOT sales by state, FY26 (%)",
              C.donut([("Maharashtra", 63.24, C.NAVY), ("Gujarat", 12.57, C.GOLD), ("Other states", 24.19, C.GREY)],
                      "SPOT state mix", w=360, h=200, center="63%", sub="Maharashtra"),
              src(("pros", 33)))
rpt = table(["Dealings with RSBL (Riddisiddhi Bullions), FY26", "Rs cr"], [
    ["Sales to RSBL", "25,826"],
    ["Purchases from RSBL", "5,954"],
    ["Loans given to RSBL during the year (repaid: 6,629)", "6,742"],
    ["Loan owed by RSBL at 31 Mar 2026", "114"],
    ["Trade receivable from RSBL at 31 Mar 2026", "101"],
], cls="std")
body = f"""
<p>Augmont's largest customer is <b>Riddisiddhi Bullions (RSBL)</b>, a company in the promoter group. RSBL bought 27% of FY26 sales and was also a supplier and a borrower.
Related-party deals are legal if approved and priced fairly, and the company says they are at arm's length. But size like this needs close watching.</p>
{cust}
{duo(geo, '<div class="ex">' + rpt + '<p class="src">' + src(("pros", "364-365"), ("ar", "103-104")) + '</p></div>')}
<p>Positive sign: loans to related parties fell from Rs 119 cr (Mar 2026) to about Rs 1.5 cr (Sep 2026). Also note: RSBL faced SEBI and DGFT actions in the past
(2015-2021); a DGFT matter is still pending in court. These are RSBL's cases, not findings against Augmont (prospectus p.41, 47).</p>
"""
page("Customers and related parties", "One related company bought 27% of sales", body,
     ["Top 10 customers: 52% of sales. Top 10 suppliers: 74% of buying.",
      "SPOT sales are heavily concentrated in Maharashtra.",
      "Related-party loans were mostly repaid by Sep 2026, a good sign.",
      "Watch the size of RSBL sales and receivables each year."])

# ================================================================= PAGE 18: management & ownership
mgmt = table(["Name", "Role", "Background"], [
    ["Ketan B. Kothari", "Whole-time Director", "Promoter family; leads the business"],
    ["Mahendra Kumar N. Bafna", "Whole-time Director", "Re-appointed to Mar 2031"],
    ["Sachin G. Kothari", "Non-executive Director", "15+ yrs in gold; CA, MBA"],
    ["Amitkumar A. Solanki", "Non-executive Director", "18+ yrs accounting and audit; FCA"],
    ["Raghupathi N. Cavale", "Independent Director", "Former Sr VP, Infosys"],
    ["Suhas N. Sahakari", "Independent Director", "31+ yrs banking (RBL, Axis)"],
    ["Minal B. Khona", "Independent Director", "30+ yrs, practising lawyer"],
    ["Nishant T. Ranka", "Independent Director", "21+ yrs, chartered accountant"],
    ["Spardha S. Sharma", "CFO (since Aug 2025)", "Previous CFO left May 2025"],
    ["Vivek Kothari", "Head, SPOT and dealing", "Promoter family"],
], cls="std")
sh = exhibit("Shareholding, Sep 2026 (%)",
             C.donut([("Promoters", 81.91, C.NAVY), ("Public", 13.37, C.GREY), ("DIIs", 2.92, C.GOLD), ("FIIs", 1.78, C.SLATE)],
                     "Shareholding", w=360, h=200, center="81.9%", sub="promoters"), src("scr"))
ph = exhibit("Largest promoter holders after IPO (%)",
             C.hbars(["Mohinidevi", "Kalawati", "Devkumari", "Namita", "Manakchand", "Vivek", "Dimple", "Dimpal"],
                     [18.33, 16.56, 10.21, 9.97, 9.43, 6.42, 6.25, 4.74], "Promoter holders", dec=1, unit="%", w=360),
             src(("pros", "125-126")))
body = f"""
<p>Augmont is run by the Kothari family and associates, with four independent directors. The family owns about 82% after the IPO,
spread across several members. Ketan Kothari, who leads the company, holds no shares in the parent directly (prospectus p.111).</p>
{mgmt}
<p class="src">{src(("deck", "22-23"), ("ar", "6-7"))}</p>
{duo(sh, ph)}
<div class="callout warn"><p><b>Governance points to know.</b> The FY26 auditor flagged that accounting software audit trails were not fully enabled.
The company gave Rs 12.75 cr in political donations in FY26. The auditor changed in Feb 2025 and the CFO in 2025. None of these were qualified opinions;
the accounts were signed off cleanly. {src(("ar", "79, 112, 132"), ("pros", 102))}</p></div>
"""
page("Management and ownership", "A family-run company with four independent directors", body,
     ["Promoters own 81.9%; public float is small, so the stock can move sharply.",
      "FIIs and mutual funds own under 5% combined.",
      "No promoter pledge at IPO.",
      "Audit-trail gaps and political donations are worth tracking."])

# ================================================================= PAGE 19: valuation snapshot
vt = table(["Measure", "Value", "How it is worked out"], [
    ["Share price", "Rs 922", "Screener, 7 Nov 2026"],
    ["Market cap", "Rs 8,420 cr", "9.14 cr shares x price"],
    ["Owner profit, last 12 months", f"Rs {CALC['owner_ttm']} cr", "FY26 333.9 - H1 FY26 174.6 + H1 FY27 176.1"],
    ["Price / earnings", f"{CALC['pe']}x", "Market cap / owner profit (12 months)"],
    ["Owner equity, Sep 2026", f"Rs {CALC['owner_eq']:,} cr", "Share capital + other equity"],
    ["Book value per share", f"Rs {CALC['bvps']:.0f}", "Owner equity / shares"],
    ["Price / book", f"{CALC['pb']}x", "Market cap / owner equity"],
    ["Cash less debt", f"Rs {CALC['cash_less_debt']} cr", "Cash 170.7 - debt and leases 9.6"],
    ["EV / EBITDA (excl. other income)", f"{CALC['ev_ebitda']}x", f"EV Rs {CALC['ev']:,.0f} cr / 12-month EBITDA Rs {CALC['ttm_ebitda_ex_oi']} cr"],
    ["Price vs IPO price", f"+{CALC['vs_ipo']:.0f}%", "922 vs 788"],
], cls="std")
body = f"""
<p>First, where the share price stands today, using reported numbers only. The next two pages build bear, base and bull cases to FY29.</p>
{vt}
<p class="src">{src("scr", ("res", "6, 8"), ("ar", 84))} All ratios are calculated (calc.).</p>
<h4>Which yardstick fits this business?</h4>
<p><b>Price to sales is not useful</b>: revenue mostly reflects the gold price, and Augmont keeps under Rs 1 of every Rs 100 of sales.
<b>EV/EBITDA adds little</b>: the company has almost no debt and tiny depreciation, so EBITDA and profit move together.
<b>Price to earnings (P/E) is our main yardstick</b>, on profit that belongs to Augmont's shareholders (after the minority partners' share),
and on the full 9.14 cr shares in issue after the IPO.
<b>Price to book is the cross-check</b>: profit is capped by how much capital the company has, because banks do not fund gold stock for trading.
So a P/E only makes sense if the return on equity behind it does too.</p>
"""
page("Valuation snapshot", "Where the stock stands today", body,
     [f"About {CALC['pe']}x the last 12 months' owner profit.",
      f"About {CALC['pb']}x book value after the IPO.",
      "Price is 17% above the IPO price and 34% below the 52-week high.",
      "Main yardstick: P/E on owner profit. Cross-check: price to book."])

# ================================================================= PAGES 20-21: scenarios
import valuation as V  # noqa: E402
VAL = V.run()
SC = VAL["scenarios"]
FYS = ["FY27E", "FY28E", "FY29E"]
B29 = SC["Base"]["rows"]["FY29E"]
CALC["base_fy29_target"] = round(B29["target"], 0)
CALC["base_fy29_eps"] = round(B29["eps"], 1)
SC_COL = {"Bear": C.RED, "Base": C.NAVY, "Bull": C.GREEN}

tp = exhibit("FY29 value per share in each case vs today's price (Rs)",
             C.bars(["Today (7 Nov 2026)", "Bear FY29", "Base FY29", "Bull FY29"],
                    [VAL["cmp"]] + [SC[k]["rows"]["FY29E"]["target"] for k in ("Bear", "Base", "Bull")],
                    "FY29 scenario values", colors=[C.GREY, C.RED, C.NAVY, C.GREEN], w=660, h=250,
                    value_labels=[f"{VAL['cmp']:,.0f}"] + [
                        f"{SC[k]['rows']['FY29E']['target']:,.0f} ({SC[k]['rows']['FY29E']['ret']:+.0f}%)"
                        for k in ("Bear", "Base", "Bull")]),
             "Source: our estimates (calc.) on owner earnings per share x P/E (Bear 14x, Base 20x, Bull 26x). "
             "Price from Screener, 7 Nov 2026.")
epsx = exhibit("Owner earnings per share (Rs)",
               C.grouped(["FY25", "FY26"] + FYS,
                         [(k, [None, None] + [SC[k]["rows"][f]["eps"] for f in FYS], SC_COL[k]) for k in SC]
                         + [("Reported", [VAL["hist"]["FY25"]["eps"], VAL["hist"]["FY26"]["eps"], None, None, None], C.GREY)],
                         "EPS path", dec=0, w=360, h=230),
               "Source: FY25 Screener; FY26 results filing p.6; FY27E-FY29E our estimates on 9.14 cr shares.")
opmx = exhibit("Operating margin: reported vs FY29 assumed (% of sales)",
               C.bars(["FY25", "FY26", "H1 FY27", "Bear FY29", "Base FY29", "Bull FY29"],
                      [305 / 66231 * 100, 385.95 / 94186.2 * 100, 217.4 / 34781.1 * 100]
                      + [SC[k]["rows"]["FY29E"]["opm"] for k in ("Bear", "Base", "Bull")],
                      "Margin path", dec=2, w=360, h=230,
                      colors=[C.GREY, C.GREY, C.GREY, C.RED, C.NAVY, C.GREEN]),
               "Source: Screener; results filing p.6; our estimates.")
drv = table(["What we assume", "Bear", "Base", "Bull"], [
    ["H2 FY27 sales (Rs cr); H1 actual 34,781", *[f0(SC[k]["h2"]["sales"]) for k in SC]],
    ["H2 FY27 operating margin; H1 actual 0.63%", *[f'{SC[k]["h2"]["opm"]:.2f}%' for k in SC]],
    ["Sales growth FY28 / FY29", *[f'{SC[k]["drivers"]["FY28E"]["growth"]}% / {SC[k]["drivers"]["FY29E"]["growth"]}%' for k in SC]],
    ["Operating margin FY28 / FY29", *[f'{SC[k]["drivers"]["FY28E"]["opm"]:.2f}% / {SC[k]["drivers"]["FY29E"]["opm"]:.2f}%' for k in SC]],
    ["Finance cost per year, FY28-29 (Rs cr)", *[f0(SC[k]["drivers"]["FY29E"]["interest"]) for k in SC]],
    ["P/E applied (held flat across years)", *[f'{SC[k]["pe"]}x' for k in SC]],
    ["FY29 return on equity (calc.)", *[f'{SC[k]["rows"]["FY29E"]["roe"]:.0f}%' for k in SC]],
    ["FY29 price to book at the value (calc.)", *[f'{SC[k]["rows"]["FY29E"]["pb_at_target"]:.1f}x' for k in SC]],
    ["FY29 value per share (Rs)", *[(f'{SC[k]["rows"]["FY29E"]["target"]:,.0f}', "bold") for k in SC]],
    ["Yearly return from Rs 922 to Mar 2029", *[f'{SC[k]["rows"]["FY29E"]["cagr"]:+.1f}%' for k in SC]],
], cls="fin")
body = f"""
<p>Management gives no numerical guidance ("we'll just not be able to provide any specific numerical guidance", call p.14).
So all three cases are our own estimates, built from what the business has already shown. FY27 starts from the actual first half and adds our estimate for the second half.</p>
<div class="callout"><p><b>Base case FY29 value: Rs {B29['target']:,.0f} per share</b>, which is {B29['eps']:.1f} of owner earnings per share in FY29 x 20 P/E.
That is {B29['ret']:+.0f}% from Rs 922, or about {B29['cagr']:.0f}% a year to March 2029. This is a scenario value, not a rating or a recommendation.</p></div>
{tp}
{duo(epsx, opmx)}
<h4>The three cases at a glance</h4>
{drv}
<p class="src">Source: our estimates (calc.); H1 FY27 actuals from the results filing p.6. Full year-wise tables on the next page.</p>
<h4>What each case means</h4>
<p><b style="color:{C.RED}">Bear.</b> {SC['Bear']['why']}</p>
<p><b style="color:{C.NAVY}">Base.</b> {SC['Base']['why']}</p>
<p><b style="color:{C.GREEN}">Bull.</b> {SC['Bull']['why']}</p>
<div class="callout warn"><p><b>Why the base value is below today's price for FY27 and only a little above it for FY28.</b>
At 20x, the stock needs about Rs {VAL['cmp']/20:.0f} of earnings per share to justify Rs 922. The base case gets there only in FY28.
Today's 25x P/E already prices in part of the base-case growth.</p></div>
"""
page("Valuation scenarios", f"Base case puts Augmont at Rs {B29['target']:,.0f} by FY29, {B29['ret']:.0f}% above today", body,
     [f"Base FY29: EPS Rs {B29['eps']:.1f} x 20 = Rs {B29['target']:,.0f}.",
      f"Bear FY29: Rs {SC['Bear']['rows']['FY29E']['target']:,.0f}, if old-gold margins fade back to FY26 levels.",
      f"Bull FY29: Rs {SC['Bull']['rows']['FY29E']['target']:,.0f}, if cash turns faster and margins rise.",
      f"The case hinges on margin: each 0.1% of sales is about Rs {B29['sales']*0.001*(1-VAL['tax_pct']/100)*(1-VAL['nci_pct']/100):.0f} cr of owner profit at FY29 base sales.",
      "No guidance from management; all projections are ours."])


def sc_table(name):
    s = SC[name]
    h = VAL["hist"]
    cols = ["FY25", "FY26"] + FYS
    rows_all = [h["FY25"], h["FY26"]] + [s["rows"][f] for f in FYS]
    prev_owner = [None, h["FY25"]["owner"]]

    def line(label, fn, bold=False):
        cells = [fn(r, i) for i, r in enumerate(rows_all)]
        return [label] + [((c, "bold") if bold else c) for c in cells]

    def est(i):
        return i >= 2
    tax = lambda r: (r["pbt"] - r["pat"]) / r["pbt"] * 100  # noqa: E731
    out = [
        line("Sales", lambda r, i: f0(r["sales"]), True),
        line("Expenses", lambda r, i: f0(r["sales"] - r["op"])),
        line("Operating profit", lambda r, i: f0(r["op"]), True),
        line("OPM %", lambda r, i: f'{r["op"] / r["sales"] * 100:.2f}'),
        line("Other income", lambda r, i: f0(r["oi"])),
        line("Interest", lambda r, i: f0(r["interest"])),
        line("Depreciation", lambda r, i: f0(r["dep"])),
        line("Profit before tax", lambda r, i: f0(r["pbt"])),
        line("Tax %", lambda r, i: f"{tax(r):.1f}"),
        line("Net profit", lambda r, i: f0(r["pat"]), True),
        line("Owner profit (after minority)", lambda r, i: f0(r["owner"])),
        line("EPS, Rs", lambda r, i: f'{r["eps"]:.1f}', True),
        line("Owner profit growth %", lambda r, i: "" if i == 0 else
             f'{(r["owner"] / (prev_owner[1] if i == 1 else rows_all[i - 1]["owner"]) - 1) * 100:.0f}'),
        line("Net profit margin %", lambda r, i: f'{r["pat"] / r["sales"] * 100:.2f}'),
        line(f"Value per share at {s['pe']}x P/E, Rs", lambda r, i: f'{r["target"]:,.0f}' if est(i) else "", True),
        line("Return vs Rs 922", lambda r, i: f'{r["ret"]:+.0f}%' if est(i) else ""),
        line("Yearly return (CAGR) from 7 Nov 2026", lambda r, i: (f'{r["cagr"]:+.1f}%' if r.get("cagr") is not None
                                                                   else "under 1 yr") if est(i) else ""),
    ]
    return table([f"{name} case, Rs cr"] + cols, out, cls=f"fin wide sc {name.lower()}")


body = f"""
<p>Laid out like a Screener profit and loss table. FY25 and FY26 are reported; FY27E to FY29E are our estimates.
FY27E = H1 FY27 actual + our H2 estimate. EPS uses the full 9.14 cr shares for every projected year.</p>
<h4 style="color:{C.RED}">Bear case (P/E 14x)</h4>{sc_table("Bear")}
<h4 style="color:{C.NAVY}">Base case (P/E 20x)</h4>{sc_table("Base")}
<h4 style="color:{C.GREEN}">Bull case (P/E 26x)</h4>{sc_table("Bull")}
<p class="src">Source: FY25 Screener (rounded); FY26 Annual Report p.84 and results filing p.6; H1 FY27 results filing p.6; FY27E-FY29E our estimates (calc.).
Reported FY25/FY26 EPS use the weighted share count before the IPO, so they are not exactly comparable with the projected EPS.</p>
<h4>Key assumptions and caveats</h4>
<ul class="small">
<li><b>Guided vs estimated.</b> Nothing here is company guidance. Management declined to give FY27 numbers (call p.14).
Sales, margins, other income, interest, depreciation, tax ({VAL['tax_pct']}%) and minority share ({VAL['nci_pct']}% of profit) are all our estimates.
Interest, depreciation and tax are the least certain bridge lines. The Q2 FY27 finance cost of Rs 18 cr is not explained in the filings, so we keep a similar cost in every case.</li>
<li><b>Capital check.</b> Banks do not fund gold stock for trading (call p.12), so growth must come from retained profit.
We assume no dividend and no new shares. In every case, sales per rupee of equity stays at about 36-43x, close to the Q2 FY27 level of about 37x (annualised).
Faster growth than this would need more equity, which would dilute EPS.</li>
<li><b>Shares.</b> 9.14 cr shares after the IPO (prospectus p.107). No further dilution is disclosed. ESOPs or options, if any, are not captured.</li>
<li><b>Multiples.</b> P/E is held flat across the years within each case and differs between cases (bear 14x, base 20x, bull 26x vs about 25x today).
That is a simplification. In reality the multiple moves with sentiment and with proof of cash conversion.</li>
<li><b>Gold price.</b> We assume no big change in the rupee gold price. Higher prices raise sales but cut the tonnes the same capital can buy, so profit moves much less than sales.</li>
<li><b>One-offs.</b> No repeat of the Q2 FY27 silver import gain is assumed. Other income includes derivative gains that can swing either way.</li>
<li><b>Not modelled.</b> A sum-of-the-parts view (SPOT, Gold For All, refining, EGR) is possible but segment profit is not disclosed. EGR income is not included in any case.</li>
<li>These are scenario bands, not forecasts. This is not investment advice, and the author is not acting as a licensed financial adviser.</li>
</ul>
"""
page("Scenario tables", "Bear, base and bull: year-wise projections to FY29", body, None, cls="fs")

# ================================================================= PAGE 20: triggers
trig = table(["When", "What to watch", "Status (7 Nov 2026)"], [
    ["Q3 FY27 (Oct-Dec 2026)", "EGR products go live with Augmont as liquidity provider", "NSE shows EGR trading on 6 Nov 2026; Augmont's volumes not disclosed"],
    ["Feb 2027 (expected)", "Q3 FY27 results: Diwali quarter, receivables, cash flow", "Pending"],
    ["FY27", "10 new SPOT delivery centres", "Sites identified, per management"],
    ["Next 2 years", "Delivery centres from 20 to 35", "Plan"],
    ["No date", "LBMA refinery accreditation", "Aspiration only"],
    ["May 2027", "Rudrapur refinery lease expires", "Renewal not yet disclosed"],
    ["Ongoing", "Scrap share of buying stays near 24.5%", "Management: 'healthy levels'"],
    ["Ongoing", "Cyber-fraud case: Rs 10.1 cr frozen account", "Under court review"],
    ["Ongoing", "Jaipur jewellery plant back to normal after 22 Oct fire", "No restart date given"],
], cls="std")
body = f"""
<p>These are the dated events that will show whether the story is playing out. Most can be checked in the next two quarterly results.</p>
{trig}
<p class="src">{src("call", "nse", ("pros", "243, 257"), ("res", 7), ("ar", 132))}</p>
<div class="callout"><p><b>What would make the story stronger:</b> receivables back near normal at 31 Dec, positive operating cash in H2 FY27,
margins holding without the silver gain, and EGR volumes showing up in results.<br>
<b>What would weaken it:</b> another half-year of negative operating cash, margins falling back toward 0.4%, or RSBL's share of sales and receivables rising.</p></div>
"""
page("Triggers", "What to watch in the next 6-12 months", body,
     ["The Q3 FY27 results are the key test of cash conversion.",
      "EGR is the biggest new opportunity, but there are no numbers yet.",
      "Several operational items (refinery lease, plant fire, frozen account) need follow-up."])

# ================================================================= PAGE 21: risks
risk = table(["Risk", "Why it matters", "Level*"], [
    ["Thin margins", "Profit is under 1% of sales; a small fall in spreads wipes out a large share of profit", (chip("High"), "c")],
    ["Cash conversion", "Profit has not turned into operating cash in FY26 or H1 FY27", (chip("High"), "c")],
    ["Related-party concentration", "RSBL bought 27% of FY26 sales and borrowed from Augmont", (chip("High"), "c")],
    ["One-off gains", "Q2 silver gain is situational; FY26 had Rs 77 cr derivative gains in other income", (chip("Medium"), "c")],
    ["Gold and silver prices", "Higher prices cut tonnes sold for the same capital; sharp swings test hedging", (chip("Medium"), "c")],
    ["Digital gold rules", "Not SEBI-regulated; new rules or a ban could hit Gold For All", (chip("Medium"), "c")],
    ["Subsidiary profit", "Over half of FY26 profit came from subsidiaries; the rest of the group contributed less in Q2 FY27", (chip("Medium"), "c")],
    ["Governance", "Audit-trail gaps; political donations; past regulatory actions against RSBL", (chip("Medium"), "c")],
    ["Fraud and cyber", "Rs 10.1 cr frozen after alleged unauthorised digital gold sales", (chip("Low"), "c")],
    ["Low free float", "Promoters hold 81.9%; thin trading can mean big price swings", (chip("Low"), "c")],
], cls="std")
body = f"""
<p>Every business has risks. These are the ones that could most change the view on Augmont.</p>
{risk}
<p class="src">*Level is our judgment, not a company figure. {src(("ar", "111, 79, 132"), ("pros", "32, 41-47"), "sebi", ("deck", 26))}</p>
"""
page("Risks", "Key risks", body,
     ["The three biggest: thin margins, weak cash conversion and related-party concentration.",
      "Several risks are checkable every quarter (see page 22)."])

# ================================================================= PAGE 22: statements
pl = table(["Rs cr", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26", "H1 FY27"], [
    ["Revenue"] + [f0(v) for v in D["rev"]] + ["34,781"],
    ["Operating profit"] + [f0(v) for v in D["op"]] + ["217"],
    ["Margin %"] + [f"{o/r*100:.2f}" for o, r in zip(D["op"], D["rev"])] + ["0.63"],
    ["Other income"] + [f0(v) for v in D["oi"]] + ["48"],
    ["Interest", "10", "2", "21", "20", "13", "2", "18"],
    ["Depreciation", "1", "1", "3", "8", "8", "7", "4"],
    ["Profit before tax", "26", "41", "57", "104", "305", "473", "242"],
    ["Net profit", *[f0(v) for v in D["pat"]], "181"],
    ["Owner profit", "", "", "", "", "218", "334", "176"],
    ["Parent (standalone) profit", *[f0(v) for v in D["sa_pat"]], "107"],
], cls="fin wide")
bs = table(["Rs cr", "FY22", "FY23", "FY24", "FY25", "FY26", "Sep 2026"], [
    ["Equity capital + reserves", "92", "284", "184", "402", "907", "1,697"],
    ["Borrowings (incl. leases)", "176", "198", "60", "23", "18", "10"],
    ["Other liabilities", "113", "269", "515", "1,431", "332", "331"],
    ["Total", "381", "751", "760", "1,857", "1,257", "2,038"],
    ["Fixed assets", "12", "21", "26", "25", "30", "32"],
    ["Inventory", "", "", "", "264", "342", "341"],
    ["Trade receivables", "", "", "", "38", "182", "749"],
    ["Cash and equivalents", "", "", "", "174", "87", "171"],
], cls="fin wide")
cf = table(["Rs cr", "FY22", "FY23", "FY24", "FY25", "FY26", "H1 FY27"], [
    ["Cash from operations", "53", "-55", "97", "105", "-42", "-578"],
    ["Cash from investing", "3", "-13", "168", "-61", "-51", "79"],
    ["Cash from financing", "-4", "180", "-160", "-47", "7", "583"],
    ["Net change in cash", "51", "112", "105", "-3", "-87", "84"],
], cls="fin wide")
body = f"""
<h4>Profit and loss (consolidated)</h4>{pl}
<h4>Balance sheet (consolidated)</h4>{bs}
<h4>Cash flow (consolidated)</h4>{cf}
<p class="src">{src("scr", ("ar", "83-85"), ("res", "6, 8, 9"))} H1 FY27 and FY26 owner profit from filings; earlier years from Screener (rounded).
Equity excludes minority interest for FY26 and Sep 2026. Blank = not collected. H1 FY27 operating profit excludes other income (calc.).</p>
"""
page("Financial statements", "Financial summary", body, None, cls="fs")

# ================================================================= PAGE 23: glossary + sources
gl = [("Spread", "The gap between the price Augmont buys metal at and the price it sells at."),
      ("Scrap / old gold", "Used gold (old jewellery or melted lumps) that must be purified before reuse."),
      ("Dore", "Semi-refined gold bars from mines, imported for refining."),
      ("SPOT", "Augmont's online bullion counter for businesses."),
      ("Gold For All", "Augmont's consumer brand: coins, digital gold, EMI jewellery, gold loans."),
      ("Digital gold", "Gold bought online in small amounts; the metal is stored in a vault for the buyer. Not SEBI-regulated."),
      ("EGR", "Electronic Gold Receipt: gold held in a vault and traded like a share on NSE. SEBI-regulated."),
      ("Working capital", "Cash tied up in day-to-day trading: metal, supplier advances and unpaid customer bills."),
      ("Receivables", "Money customers owe for goods already delivered."),
      ("Owner profit", "Group profit belonging to Augmont's shareholders, after minority holders' share."),
      ("Standalone / parent", "The listed company alone, without its subsidiaries."),
      ("EBITDA", "Profit before interest, tax, depreciation and amortisation."),
      ("Related party", "A company or person linked to the promoters or management."),
      ("(calc.)", "Worked out by us from reported figures.")]
body = ('<div class="cols2"><div><h4>Glossary</h4><dl class="gl">'
        + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in gl) + "</dl></div><div><h4>Sources</h4><ol class=\"srcs\">"
        + "".join(f'<li>{"<a href=\'%s\'>%s</a>" % (u, n) if u else n}</li>' for n, u in SRC.values())
        + """</ol>
<h4>Notes on data</h4><p class="small">Figures are INR crore unless stated. 1 crore = 10 million. FY = year to 31 March.
Consolidated figures unless marked standalone or parent. Screener rounds to whole crore; filings are used where they differ.
Q3 FY26 quarterly figures are derived as FY26 less the other three quarters.</p>
<h4>Disclaimer</h4><p class="small">This report is for information and education only. It is not an offer or a recommendation to buy or sell any security.
It does not contain a rating. The bear, base and bull values are scenario estimates built on stated assumptions, not forecasts or price targets for trading. Figures come from public filings and data providers believed to be reliable, but accuracy is not guaranteed.
Past performance does not guarantee future results. Readers should make their own decisions or consult a registered adviser.
[Add the publisher's SEBI research analyst registration and disclosure details here before distribution.]</p>
</div></div>""")
page("Reference", "Glossary, sources and disclaimer", body, None)

# ================================================================= render
CSS = """
:root{--navy:#14213D;--gold:#C8962E;--goldlt:#F6EEDC;--ink:#1F2733;--muted:#6B7480;--line:#E3E6EB;--bg:#EEF0F3;--red:#B23A3A}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 Calibri,Carlito,'Segoe UI',Arial,sans-serif}
a{color:#2C4F8C}
.page{max-width:1040px;margin:22px auto;background:#fff;border:1px solid var(--line);page-break-after:always}
.band{background:var(--navy);color:#fff;display:flex;justify-content:space-between;align-items:center;padding:9px 26px;font-size:12.5px;letter-spacing:.04em}
.band b{color:var(--gold)}
.goldline{height:3px;background:var(--gold)}
.inner{padding:18px 26px 8px}
.kicker{color:var(--gold);font-weight:700;font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;margin:4px 0 2px}
h2{font-size:25px;line-height:1.2;margin:0 0 12px;color:var(--navy)}
h3{font-size:16px;margin:14px 0 4px;color:var(--navy)}
h4{font-size:15px;margin:16px 0 6px;color:var(--navy)}
.grid{display:grid;grid-template-columns:minmax(0,1fr) 220px;gap:24px}
.notes{border-left:3px solid var(--gold);background:var(--goldlt);padding:10px 14px;align-self:start;font-size:13.5px}
.notes .nh{font-weight:700;color:var(--navy);text-transform:uppercase;font-size:12px;letter-spacing:.06em;margin:0 0 6px}
.notes p{margin:0 0 9px}
.foot{display:flex;justify-content:space-between;border-top:1px solid var(--line);margin:10px 26px 0;padding:7px 0 10px;font-size:11.5px;color:var(--muted)}
.ex{margin:14px 0;padding:0}
figcaption{font-weight:700;color:var(--navy);font-size:14px;margin-bottom:6px}
.src{font-size:11.5px;color:var(--muted);margin:4px 0 0}
.xnote{font-size:12.5px;margin:6px 0 0}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px 18px}
.grid3 .ex{margin:4px 0}
.grid3 figcaption{font-size:13px;min-height:2.6em}
.t{border-collapse:collapse;width:100%;font-size:13.5px;margin:6px 0}
.t th{background:var(--navy);color:#fff;font-weight:600;padding:6px 8px;text-align:right}
.t th:first-child{text-align:left}
.t td{padding:5px 8px;border-bottom:1px solid var(--line)}
.t td.l{text-align:left}.t td.r{text-align:right}.t td.c{text-align:center}
.t.std td.r{text-align:left}
.t.std th{text-align:left}
.t tbody tr:nth-child(even){background:#F7F8FA}
.t td.flag{color:var(--red);font-weight:700}.t td.bold{font-weight:700}
.t.kv th{display:none}.t.kv td{padding:3px 4px;font-size:13px}
.t.fin td,.t.fin th{font-size:12.5px;padding:4px 6px}
.tw{overflow-x:auto;max-width:100%}
.chip{display:inline-block;padding:1px 9px;border-radius:9px;font-size:12px;font-weight:700}
.chip.high{background:#F4D9D9;color:#8E2525}.chip.medium{background:#F6EEDC;color:#7A5A12}.chip.low{background:#E3EEE8;color:#22593F}
.callout{background:#F4F6F9;border-left:4px solid var(--navy);padding:9px 14px;margin:12px 0;font-size:14px}
.callout p{margin:0}.callout.warn{border-left-color:var(--red);background:#FBF1F1}
.small{font-size:13px}
.cw-m{display:none}
.figt{font-weight:700;color:var(--navy);font-size:14px;margin:0 0 6px}
.kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:12px 0 6px}
.kpi{border:1px solid var(--line);border-top:3px solid var(--navy);padding:7px 10px;background:#FAFBFC}
.kpi.gold{border-top-color:var(--gold)}.kpi.red{border-top-color:var(--red)}
.kn{margin:0;font-size:19px;font-weight:700;color:var(--navy)}.kpi.red .kn{color:var(--red)}
.kl{margin:0;font-size:12.5px;color:var(--muted)}.tiny{font-size:11px;color:var(--muted)}
.lede{font-size:17px;line-height:1.5;color:var(--navy);margin:2px 0 6px}
/* cover */
.p1 .inner{padding-top:22px}
.ctitle{font-size:34px;font-weight:700;color:var(--navy);margin:0;line-height:1.1}
.csub{font-size:19px;color:var(--gold);margin:4px 0 2px;font-weight:700}
.cmeta{font-size:13px;color:var(--muted);margin:0 0 12px}
.cover{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:26px}
.cmain p{margin:0 0 8px}
.rail{background:#F7F8FA;border:1px solid var(--line);padding:12px}
.rbox{margin-bottom:12px}
.rh{font-weight:700;color:#fff;background:var(--navy);margin:0 0 4px;padding:4px 8px;font-size:12.5px}
.verdict{background:var(--goldlt);border:1px solid var(--gold);padding:8px 10px}
.verdict .rk{margin:0;font-size:11.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.verdict .rv{margin:0;font-size:18px;font-weight:700;color:var(--navy)}
.verdict .rs{margin:2px 0 0;font-size:12px}
/* diagrams */
.flow{display:flex;align-items:stretch;gap:6px}
.fcol{flex:1;display:flex;flex-direction:column;gap:5px;min-width:0}
.fh{margin:0;font-weight:700;font-size:12.5px;color:var(--navy)}
.fb{background:#EEF1F6;border:1px solid #D5DBE5;padding:6px;font-size:12.5px;line-height:1.3;border-radius:3px}
.fb.gold{background:var(--goldlt);border-color:var(--gold)}
.fb small{color:var(--muted)}
.farrow{align-self:center;color:var(--gold);font-size:16px}
.loop{font-size:13px;margin:6px 0 0}
.tree{border:1px solid var(--line);padding:10px}
.troot{background:var(--navy);color:#fff;text-align:center;padding:8px;font-weight:700;border-radius:3px}
.troot small{font-weight:400;color:#D9DEE8}
.tbranches{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0}
.tnode{text-align:center;padding:7px;color:#fff;border-radius:3px;margin-bottom:6px}
.tnode.navy{background:#2C3E63}.tnode.gold{background:var(--gold)}
.tleaf{border-left:3px solid var(--line);padding:4px 8px;margin:4px 0;font-size:13.5px}
.tengine{background:#EEF1F6;text-align:center;padding:7px;font-size:13.5px;border-radius:3px}
.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.tli{border-top:3px solid var(--gold);padding:6px 4px;font-size:13px}
.tly{display:block;font-weight:700;color:var(--navy)}
.cycle{display:flex;gap:6px;align-items:stretch}
.cstep{flex:1;background:#EEF1F6;border-radius:3px;padding:8px;font-size:13.5px}
.cday{display:block;font-weight:700;color:var(--gold)}
.carrow{align-self:center;color:var(--gold)}
.duo.small{margin-top:10px}
.kbox{border:1px solid var(--line);padding:8px 12px;border-radius:3px}
.kbox.gold{border-color:var(--gold);background:var(--goldlt)}
.kt{margin:0;font-size:12.5px;color:var(--muted)}.kv{margin:0;font-size:22px;font-weight:700;color:var(--navy)}.ks{margin:0;font-size:12.5px}
.gtree{border:1px solid var(--line);padding:10px}
.gparent{background:var(--navy);color:#fff;text-align:center;padding:8px;border-radius:3px;font-weight:700}
.gparent small{font-weight:400;color:#D9DEE8}
.gkids{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:10px}
.gk{border:1px solid #D5DBE5;background:#EEF1F6;text-align:center;padding:6px;font-size:12.5px;border-radius:3px}
.gk.gold{background:var(--goldlt);border-color:var(--gold)}
.gk small{color:var(--muted)}
.cols2{display:grid;grid-template-columns:1fr 1fr;gap:6px 26px}
.cols2 ul{padding-left:18px;margin:4px 0}.cols2 li{margin:0 0 6px;font-size:14px}
.gl dt{font-weight:700;color:var(--navy);margin-top:6px}.gl dd{margin:0 0 0 0;font-size:13.5px}
.srcs{font-size:13px;padding-left:18px}
.toc{columns:2;column-gap:36px;font-size:13.5px;margin:6px 0 0;padding-left:18px}
@media (max-width:820px){
 body{font-size:15px}
 .page{margin:0 0 12px;border-left:0;border-right:0}
 .inner{padding:14px 16px 6px}.band{padding:8px 16px}.foot{margin:8px 16px 0}
 .grid,.cover,.duo,.cols2,.tbranches{grid-template-columns:minmax(0,1fr)}
 .grid3{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
 .kpis{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}
 .band span:last-child{display:none}
 .toc{columns:1}
 .cw-d{display:none}.cw-m{display:block}
 .t.fin td,.t.fin th{font-size:11px;padding:3px 3px}
 .t{font-size:12.5px}.t th,.t td{padding:4px 5px}
 .flow,.cycle{flex-direction:column}.farrow,.carrow{transform:rotate(90deg)}
 .gkids{grid-template-columns:1fr 1fr}.tl{grid-template-columns:1fr 1fr}
 h2{font-size:21px}.ctitle{font-size:27px}
}
@media (max-width:480px){.grid3{grid-template-columns:minmax(0,1fr)}}
@media print{body{background:#fff}.page{margin:0;border:0;max-width:none}}
"""


def render():
    out = []
    total = len(PAGES)
    toc = [f"<li>{h} <span class='tiny'>p.{i+1}</span></li>" for i, (_, h, *_r) in enumerate(PAGES) if h]
    for i, (kicker, headline, body, notes, cls) in enumerate(PAGES):
        n = i + 1
        band = (f'<div class="band"><span><b>AUGMONT ENTERPRISES</b> &nbsp;|&nbsp; Initiating coverage: company study</span>'
                f'<span>7 November 2026</span></div><div class="goldline"></div>')
        if kicker == "cover":
            head = ('<p class="kicker">NSE: AUGMONT &nbsp;|&nbsp; BSE: 544888 &nbsp;|&nbsp; Precious metals</p>'
                    '<h1 class="ctitle">Augmont Enterprises Ltd</h1>'
                    '<p class="csub">India\'s gold supply chain, from refinery to app</p>'
                    '<p class="cmeta">Initiating coverage: company study &nbsp;|&nbsp; Data as of 7 November 2026 &nbsp;|&nbsp; All figures INR crore unless stated</p>')
            inner = head + body + '<h4>Inside this report</h4><ol class="toc">' + "".join(toc) + "</ol>"
        else:
            content = f'<div class="grid"><div class="main">{body}</div>{notes}</div>' if notes else body
            inner = f'<p class="kicker">{kicker}</p><h2>{headline}</h2>{content}'
        out.append(f'<section class="page {cls}" id="p{n}">{band}<div class="inner">{inner}</div>'
                   f'<div class="foot"><span>Augmont Enterprises | Company study | Not a recommendation</span><span>{n} / {total}</span></div></section>')
    body_html = "".join(out)
    import re
    cnt = [0]

    def _renum(m):
        cnt[0] += 1
        return f"<figcaption>Exhibit {cnt[0]}:"
    body_html = re.sub(r"<figcaption>Exhibit \d+:", _renum, body_html)
    for k, v in (("__BASE29__", "Base"), ("__BEAR29__", "Bear"), ("__BULL29__", "Bull")):
        body_html = body_html.replace(k, f'{SC[v]["rows"]["FY29E"]["target"]:,.0f}')
    html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Augmont Enterprises Study</title>'
            '<meta name="description" content="Plain-language, chart-led company study of Augmont Enterprises (NSE: AUGMONT), data as of 7 Nov 2026.">'
            f'<style>{CSS}</style></head><body>' + body_html + "</body></html>")
    with open(os.path.join(HERE, "augmont-report.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    with open(os.path.join(HERE, "chart-data.json"), "w", encoding="utf-8") as fh:
        json.dump({"data": D, "calc": CALC, "sources": SRC}, fh, indent=1, ensure_ascii=False)
    return html


if __name__ == "__main__":
    h = render()
    assert "—" not in h, "em dash found"
    print("pages", len(PAGES), "exhibits", EX[0], "bytes", len(h))
    print("calc", json.dumps(CALC))
