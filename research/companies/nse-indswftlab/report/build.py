"""Build the Ind-Swift Laboratories client report (single self-contained HTML).

Run:  python -I -X utf8 report/build.py      (from the company folder)
Out:  report/report.html, report/chart-data.json

All money is Rs crore unless stated. Every exhibit carries its source line.
Valuation numbers are read from ../model/valuation.json (model/valuation.py), never typed in.
Derived numbers are computed in calc() and tied back to filed totals with asserts.
"""
import datetime as _dt
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
        if "lab_w" in kw:
            mk["lab_w"] = min(kw["lab_w"], 112)
        return f'<div class="cw-d">{fn(*a, **kw)}</div><div class="cw-m">{fn(*a, **mk)}</div>'
    return wrap


for _n in ("bars", "grouped", "lines", "hbars", "waterfall", "value_range", "stacked100"):
    setattr(C, _n, _responsive(getattr(C, _n)))


def hd(iso):
    """Human date: 'Wed, 4 Nov 2026'."""
    d = _dt.date.fromisoformat(iso)
    return f"{d.strftime('%a')}, {d.day} {d.strftime('%b %Y')}"


# ---------------------------------------------------------------- sources
BSE = "https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname={}.pdf"
BSEAR = "https://www.bseindia.com/xml-data/corpfiling/AttachHis/{}.pdf"
SRC = {
    "deck": (f"Q2 FY27 investor presentation, filed {hd('2026-11-04')}", BSE.format("6385edbd-a83b-4fd6-9885-0743f7cb9a2e")),
    "call": (f"Q2 FY27 call transcript, {hd('2026-11-04')} (machine transcript supplied by the reader; BSE carries the audio)", None),
    "audio": ("Q2 FY27 call audio link on BSE", BSE.format("3c6a2f5f-35f6-41c7-9c0f-7b7ea47c9ea3")),
    "trq1": ("Q1 FY27 call transcript, Aug 2026", BSE.format("20e51151-92d1-4584-b075-38946d071365")),
    "dq1": ("Q1 FY27 investor presentation, Aug 2026", BSE.format("53bc6695-3b3b-4d54-9e49-fd338cb7b144")),
    "dq3": (f"Q3 FY26 investor presentation, {hd('2026-02-04')}", BSE.format("b38c0cc9-6ef5-4074-a68b-0d45a9dfcee5")),
    "djan": (f"Corporate presentation, {hd('2026-01-14')}", BSE.format("1aea0d8d-53f1-4c67-9417-9110bc29ff21")),
    "ar26": ("Annual Report FY2025-26", BSEAR.format("1030038a-682c-455c-9ee3-7f2c273fa639")),
    "ar25": ("Annual Report FY2024-25", BSEAR.format("00dc7b70-03cb-4573-99ed-0b3e05ebf276")),
    "ar24": ("Annual Report FY2023-24", BSEAR.format("255c9918-ec21-425b-9dbb-88eaf0bd13a1")),
    "caref": (f"CARE monitoring agency final report, warrant issue 1 (Rs 314.60 cr), filed {hd('2026-11-03')}", BSE.format("e0af5fc1-e457-4aa2-abdd-655b65463742")),
    "careq2": (f"CARE monitoring agency Q2 FY27 report, warrant issue 2 (Rs 137.20 cr), filed {hd('2026-11-03')}", BSE.format("e6ff1c5d-b9c5-4e88-a6a8-2662fb3398e5")),
    "carer24": ("CARE Ratings rationale, Mar 2024 (history)", "https://www.careratings.com/upload/CompanyFiles/PR/202403130346_Ind-Swift_Laboratories_Limited.pdf"),
    "nsea": (f"NSE filing: allotment of 70,00,000 warrants at Rs 196, {hd('2026-09-17')}", "https://nsearchives.nseindia.com/corporate/INDSWFTLAB_17092026174502_Outcome_Allotment.pdf"),
    "nsec": (f"NSE filing: conversion of 14,00,000 warrants, {hd('2026-10-08')}", "https://nsearchives.nseindia.com/corporate/INDSWFTLAB_08102026183706_Committee_Meeting_Outcome_08102026.pdf"),
    "scr": ("Screener.in consolidated data, fetched 9 Nov 2026", "https://www.screener.in/company/INDSWFTLAB/consolidated/"),
    "peers": ("Screener.in peer pages and compare tool, fetched 9 Nov 2026", "https://www.screener.in/company/INDSWFTLAB/consolidated/"),
    "ledger": ("Our claims ledger, Jan 2026 to Nov 2026 (evidence/claims-ledger.md)", None),
    "model": ("Our valuation model (model/valuation.py)", None),
}


def src(*items):
    """items: key or (key, page). Physical PDF page numbers, so #page= opens the right page."""
    groups = {}                      # key -> pages, in first-seen order; one name per source
    for it in items:
        key, pg = (it, None) if isinstance(it, str) else it
        groups.setdefault(key, [])
        if pg is not None and pg not in groups[key]:
            groups[key].append(pg)
    parts = []
    for key, pgs in groups.items():
        name, url = SRC[key]
        if not pgs:
            parts.append(f'<a href="{url}">{name}</a>' if url else name)
            continue
        pre = "p." if len(pgs) == 1 else "pp."
        if url:
            links = []
            for j, pg in enumerate(pgs):
                first = str(pg).split("-")[0].split(",")[0]
                u = url + (f"#page={first}" if first.isdigit() else "")
                links.append(f'<a href="{u}">{(name + ", " + pre) if j == 0 else ""}{pg}</a>')
            parts.append(", ".join(links))
        else:
            parts.append(f"{name}, {pre}" + ", ".join(str(x) for x in pgs))
    return "Source: " + "; ".join(parts) + "."


# ---------------------------------------------------------------- data (facts)
INP = {k: v[0] for k, v in VAL["inputs"].items()}
DER = VAL["derived"]
D = {
    "price": INP["price"], "shares_printed": INP["shares_printed"], "shares_diluted": INP["shares_diluted"],
    "hi52": 427, "lo52": 87, "bv": 170,
    # Screener consolidated, years to March
    "years": ["FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"],
    "sales": [780, 891, 1039, 1207, 1281, 574, 649], "sales_ttm": 753,
    "op": [144, 183, 202, 229, 252, -7, 47], "op_ttm": 104,
    "oi": [33, 23, 37, 7, 434, 292, 36], "oi_ttm": 33,
    "pat": [-21, -3, -2, 48, 421, 250, 43], "pat_ttm": 84,
    "pbt": [-20, 18, 13, 87, 582, 258, 51],
    "dep": [90, 87, 131, 57, 53, 24, 31],
    "ocf": [125, 135, 150, 195, -163, -29, -68],
    "fcf": [114, 131, 137, 182, -205, -54, -155],
    "debt": [1031, 1005, 953, 862, 17, 33, 18], "debt_sep26": 20,
    "fa": [843, 753, 630, 587, 8, 273, 304],
    # Screener quarterly
    "q": ["Dec-24", "Mar-25", "Jun-25", "Sep-25", "Dec-25", "Mar-26", "Jun-26", "Sep-26"],
    "q_sales": [129, 138, 153, 159, 151, 170, 191, 240],
    "q_op": [-7, -9, 4, 7, 4, 21, 33, 45],
    "q_opm": [-5, -7, 2.4, 4.7, 2.8, 12, 17, 19],
    "q_pat": [-5, 222, 9, 8, 10, 15, 25, 34],
    "promoter": [42.01, 40.94, 40.94, 39.49, 39.49, 43.00, 42.93, 42.93],
    "fii": [0.46, 3.07, 4.27, 14.80, 14.33, 13.88, 10.70, 10.78],
    "holders": [28752, 28117, 28709, 43780, 42121, 39222, 40881, 42667],
    # Deck p28: Q4 FY26, Q1 FY27, Q2 FY27
    "dq": ["Q4 FY26", "Q1 FY27", "Q2 FY27"],
    "dq_rev": [164.72, 186.12, 230.23], "dq_ooi": [7.98, -0.03, 4.66],
    "dq_rm": [64.86, 75.21, 106.04], "dq_emp": [37.20, 38.95, 37.36], "dq_oth": [51.94, 38.59, 49.16],
    "dq_ebitda": [18.69, 33.32, 42.33], "dq_margin": [10.82, 17.91, 18.02],
    "dq_dep": [8.08, 7.58, 7.77], "dq_tax": [-3.22, 7.98, 9.21], "dq_pat": [14.94, 24.44, 31.03],
    "q2_op": 234.89, "q2fy26_op": 156.43,
    # Deck p29: H1 FY26 vs H1 FY27
    "h1": {"rev": [298.43, 416.35], "op_rev": [310.02, 420.97], "ebitda": [16.98, 75.65], "margin": [5.47, 17.97],
           "pbt": [20.88, 73.49], "pat": [16.88, 55.47], "nonop_oi": [20.86, 15.23]},
    "fy26_op_rev": INP["fy26_revenue"],
    # Deck p30: H1 FY26 -> H1 FY27 balance sheet
    "bs": {"share_cap": [81.61, 86.96], "equity": [1298.66, 1460.59], "lt_debt": [8.78, 15.14], "st_debt": [12.77, 4.34],
           "payables": [117.09, 133.70], "ppe": [282.84, 309.61], "cwip": [0, 41.82], "oth_nca": [428.64, 434.22],
           "inventory": [102.83, 168.35], "receivables": [168.53, 234.79], "cash": [388.31, 322.81],
           "cur_inv": [19.37, 45.03], "total": [1530.06, 1754.29]},
    # Deck p20: line mix, % of revenue
    "mix_lines": ["Own brands (export)", "Contract manufacturing (export)", "Branded generics (India)", "Ethical (India)", "P2P (India)"],
    "mix_q1": [56.72, 26.64, 6.41, 6.62, 3.61], "mix_q2": [55.75, 26.99, 6.84, 5.43, 5.00],
    # Deck p14: exports by region, % of export revenue
    "geo": {"Europe": 47, "Southeast Asia": 18, "Australia": 10, "Africa": 5, "Canada": 4, "Middle East": 4, "UAE": 3,
            "Latin America": 3, "CIS": 2, "French West Africa": 2, "Mexico": 1, "South Africa": 1},
    # Deck p15-p16: registrations held and expected in FY27, regions grouped to match
    "reg_regions": ["Africa", "Southeast Asia", "Europe", "CIS and Central Asia", "Latin America", "Middle East and GCC", "Australia and NZ", "Canada"],
    "reg_held": [209 + 19, 177, 170, 116 + 9, 86, 51 + 47, 34 + 6, 11],
    "reg_exp": [109, 144, 18, 21, 19, 17, 4, 1],
    # Deck p19: FY26 top nine products, Rs lakh (FY25, FY26)
    "top9": [("Atorvastatin", 4795.71, 8549.74), ("Ezetimibe + Atorvastatin", 2328.13, 8077.82),
             ("Fexofenadine", 7967.32, 7432.38), ("Metformin", 2571.26, 2833.61), ("Quetiapine", 990.10, 1975.22),
             ("Famciclovir", 890.97, 1864.06), ("Spagulax", 2230.09, 1450.49), ("Aripiprazole", 1095.34, 755.11),
             ("Ramipril", 2353.62, 593.13)],
    # Deck p21: launches, USD mn
    "launches": [("Ibuprofen sachet", 12.0, "Commercialised", "FY27"), ("Clarithromycin dry suspension", 6.0, "Validated; partner variation awaited", "FY27"),
                 ("Macrogol sachet", 5.5, "Commercialised", "FY27"), ("Esomeprazole", 10.0, "Planned", "FY28"),
                 ("Clarithromycin (second line)", 9.9, "Planned", "FY29"), ("Ibuprofen (second line)", 0.4, "Planned", "FY29")],
    "usd_inr": 88,
    "pipeline13": ["Rosuvastatin", "Spironolactone", "Mirabegron PR", "Rifaximin", "Dapagliflozin", "Sitagliptin", "Linagliptin",
                   "Edoxaban", "Mesalamine PR", "Sulfasalazine EC", "Nitazoxanide", "Sacubitril + Valsartan", "Empagliflozin"],
    # AR26 p93 standalone segment revenue
    "exp_dom": {"FY25": (399.23, 150.41), "FY26": (484.39, 128.24)},
    # AR26 p64, p92
    "kmp_pay": (12.65, 16.26), "pat_standalone_fy26": 42.56,
    # warrants
    "w1": {"n": 2.60, "price": 121, "amt": 314.60, "lapsed_n": 0.65, "lapsed_amt": 58.99},
    "w2": {"n": 0.70, "price": 196, "amt": 137.20, "upfront": 34.30, "conv_n": 0.14, "conv_amt": 20.58},
    "stake_pct": INP["stake_pct"],
}

CALC = {}


def calc():
    d, h, b = D, D["h1"], D["bs"]
    C_ = CALC
    C_["mcap"] = d["price"] * d["shares_printed"]
    C_["mcap_dil"] = d["price"] * d["shares_diluted"]
    C_["net_cash"] = INP["cash_sep26"] + INP["current_investments_sep26"] - INP["borrowings_sep26"]
    C_["stake_624"] = d["stake_pct"] * 8000
    C_["stake_vals"] = {k: d["stake_pct"] * k for k in (7000, 8000, 9000)}
    C_["core_ev"] = C_["mcap"] - C_["net_cash"] - C_["stake_624"]
    C_["cash_stake_share"] = (C_["net_cash"] + C_["stake_624"]) / C_["mcap"]
    C_["h1_g"] = h["op_rev"][1] / h["op_rev"][0] - 1
    C_["h1_rev_g"] = h["rev"][1] / h["rev"][0] - 1
    C_["h1_inc"] = h["op_rev"][1] - h["op_rev"][0]
    C_["q2_yoy"] = d["q2_op"] / d["q2fy26_op"] - 1
    C_["q_op_rev"] = [r + o for r, o in zip(d["dq_rev"], d["dq_ooi"])]       # Q4 FY26, Q1, Q2 FY27 operating revenue
    C_["h2fy26"] = d["fy26_op_rev"] - h["op_rev"][0]
    C_["q3fy26"] = C_["h2fy26"] - C_["q_op_rev"][0]
    C_["q1fy26"] = h["op_rev"][0] - d["q2fy26_op"]
    C_["h2_need"] = DER["h2_need"]
    C_["h2_need_g"] = C_["h2_need"] / C_["h2fy26"] - 1
    C_["h2_need_vs_q2"] = DER["h2_need_q"] / d["q2_op"] - 1
    C_["h2_1000"] = 1000 - h["op_rev"][1]
    C_["h2_1000_g"] = C_["h2_1000"] / C_["h2fy26"] - 1
    C_["h2_margin_1000_20"] = (200 - h["ebitda"][1]) / C_["h2_1000"]
    C_["inv_rec_up"] = (b["inventory"][1] - b["inventory"][0]) + (b["receivables"][1] - b["receivables"][0])
    C_["inv_g"] = b["inventory"][1] / b["inventory"][0] - 1
    C_["rec_g"] = b["receivables"][1] / b["receivables"][0] - 1
    C_["cash_fall"] = b["cash"][0] - b["cash"][1]
    C_["nwc"] = [b["inventory"][i] + b["receivables"][i] - b["payables"][i] for i in (0, 1)]
    ann = [x * 2 for x in h["rev"]]          # same base as model/valuation.py: revenue line x 2
    C_["rec_days"] = [b["receivables"][i] / ann[i] * 365 for i in (0, 1)]
    C_["inv_days"] = [b["inventory"][i] / ann[i] * 365 for i in (0, 1)]
    C_["nwc_days"] = [C_["nwc"][i] / ann[i] * 365 for i in (0, 1)]
    # per Rs 100 of H1 FY27 operating revenue
    rev = h["op_rev"][1]
    rm, emp, oth = sum(d["dq_rm"][1:]), sum(d["dq_emp"][1:]), sum(d["dq_oth"][1:])
    C_["h1_costs"] = (rm, emp, oth)
    C_["per100"] = {"rm": rm / rev * 100, "emp": emp / rev * 100, "oth": oth / rev * 100,
                    "ebitda": h["ebitda"][1] / rev * 100,
                    "dep_int": (INP["h1_depreciation"] + INP["h1_finance_cost"]) / rev * 100,
                    "oi": INP["h1_nonop_other_income"] / rev * 100, "pbt": h["pbt"][1] / rev * 100,
                    "tax": INP["h1_tax"] / rev * 100, "pat": h["pat"][1] / rev * 100,
                    "other": (h["pbt"][1] - INP["h1_tax"] - h["pat"][1]) / rev * 100}
    C_["h1_other_items"] = h["pbt"][1] - INP["h1_tax"] - h["pat"][1]   # 0.82 cr between PBT less tax and filed PAT
    C_["fy26_ocf_per100"] = d["ocf"][6] / d["sales"][6] * 100
    C_["rm_pct"] = [rm_ / r_ * 100 for rm_, r_ in zip(d["dq_rm"], d["dq_rev"])]
    C_["emp_pct"] = [e / r_ * 100 for e, r_ in zip(d["dq_emp"], d["dq_rev"])]
    C_["oth_pct"] = [o / r_ * 100 for o, r_ in zip(d["dq_oth"], d["dq_rev"])]
    C_["top9_cr"] = [(n, a / 100, b_ / 100) for n, a, b_ in d["top9"]]
    C_["top9_tot"] = sum(x[2] for x in C_["top9_cr"])
    C_["top9_share"] = C_["top9_tot"] / d["fy26_op_rev"]
    C_["ator2"] = C_["top9_cr"][0][2] + C_["top9_cr"][1][2]
    C_["ator2_share"] = C_["ator2"] / d["fy26_op_rev"]
    C_["launch_usd"] = sum(x[1] for x in d["launches"])
    C_["launch_inr"] = C_["launch_usd"] * d["usd_inr"] / 10
    C_["q2_line_rs"] = [s / 100 * d["q2_op"] for s in d["mix_q2"]]
    C_["export_share_q2"] = (d["mix_q2"][0] + d["mix_q2"][1])
    C_["own_cmo_split"] = d["mix_q2"][0] / C_["export_share_q2"] * 100
    C_["reg_held_tot"] = sum(d["reg_held"])
    C_["reg_exp_tot"] = sum(d["reg_exp"])
    C_["per_reg"] = 125 * 4 / 540
    C_["capex_hist"] = [o - f for o, f in zip(d["ocf"], d["fcf"])]
    C_["ocf_3y"] = sum(d["ocf"][4:7])
    C_["kmp_pct"] = d["kmp_pay"][1] / d["pat_standalone_fy26"] * 100
    C_["w1_raised"] = d["w1"]["amt"] - d["w1"]["lapsed_amt"]
    C_["w2_left_n"] = d["w2"]["n"] - d["w2"]["conv_n"]
    C_["w2_to_come"] = C_["w2_left_n"] * d["w2"]["price"] * 0.75
    C_["exp_g"] = d["exp_dom"]["FY26"][0] / d["exp_dom"]["FY25"][0] - 1
    C_["dom_g"] = d["exp_dom"]["FY26"][1] / d["exp_dom"]["FY25"][1] - 1
    C_["at_now"] = VAL["cross_checks"]["asset_turnover_now"]
    C_["new_cust_share"] = (80 / C_["h1_inc"], 90 / C_["h1_inc"])
    C_["peer_med"] = 17.9
    # tie-outs against filed totals
    assert abs(C_["mcap"] - VAL["reverse"][0]["mcap"]) < 0.01
    assert abs(C_["net_cash"] - DER["net_cash_sep26"]) < 0.01
    assert abs(C_["core_ev"] - VAL["reverse"][0]["core_ev"]) < 0.01
    assert abs(sum(C_["q_op_rev"][1:]) - h["op_rev"][1]) < 0.05, "Q1+Q2 must tie to H1 operating revenue"
    assert abs(C_["q_op_rev"][2] - d["q2_op"]) < 0.01
    assert abs(rm + emp + oth - (h["rev"][1] + sum(d["dq_ooi"][1:]) - h["ebitda"][1])) < 0.1, "H1 cost lines tie to EBITDA"
    p = C_["per100"]
    assert abs(p["ebitda"] - p["dep_int"] + p["oi"] - p["pbt"]) < 0.1
    assert abs(p["pbt"] - p["tax"] - p["other"] - p["pat"]) < 1e-9 and abs(CALC["h1_other_items"] - 0.82) < 0.005
    assert abs(sum(d["geo"].values()) - 100) < 0.01
    assert abs(sum(d["mix_q1"]) - 100) < 0.1 and abs(sum(d["mix_q2"]) - 100) < 0.1
    assert C_["reg_exp_tot"] == 333
    assert abs(C_["top9_tot"] - 335.32) < 0.01
    assert abs(C_["ator2"] - 166.28) < 0.01
    assert abs(C_["launch_usd"] - 43.8) < 0.01
    assert abs(C_["inv_rec_up"] - 131.78) < 0.01
    assert abs(C_["nwc"][1] - DER["nwc_sep26"]) < 0.01
    assert abs(C_["rec_days"][1] - DER["receivable_days"]) < 0.01
    assert abs(C_["h2_need"] - (DER["base_fy27"] - h["op_rev"][1])) < 0.01
    assert abs(C_["w2_to_come"] - INP["warrant_cash_to_come"]) < 0.01
    assert abs(sum(b[k][1] for k in ("ppe", "cwip")) - INP["ppe_cwip_sep26"]) < 0.01
    for i in range(7):
        assert abs(d["ocf"][i] - d["fcf"][i] - C_["capex_hist"][i]) < 1e-9
    assert abs(sum(d["q_sales"][4:]) - d["sales_ttm"]) <= 1, "TTM is the last four quarters (Screener rounds each to Rs 1 cr)"
    assert abs(sum(d["q_pat"][4:]) - d["pat_ttm"]) <= 1
    assert DER["fy26_fy30_cagr"] > 0.20 and DER["base_growth_fy28_30"] < 0.17
    return C_


calc()
V = {k: VAL["scenarios"][k]["value"] for k in ("Bear", "Base", "Bull")}
ROWS = {k: VAL["scenarios"][k]["rows"] for k in ("Bear", "Base", "Bull")}
ASM = {k: VAL["scenarios"][k]["assumptions"] for k in ("Bear", "Base", "Bull")}
READOUT = VAL["readout"]
FRAG = VAL["fragility"]
assert READOUT == "ATTRACTIVE" and VAL["mgmt_verdict"] == "WATCH"


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
    labs = [re.sub(r"<[^>]+>", "", h).replace('"', "&quot;") for h in head]
    tr = []
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            klass = "l" if (i == 0 and first_left) else "r"
            if isinstance(c, tuple):
                c, extra = c
                klass += " " + extra
            cells.append(f'<td class="{klass}" data-label="{labs[i]}">{c}</td>')
        tr.append("<tr>" + "".join(cells) + "</tr>")
    t = f'<div class="tw"><table class="t {cls}"><thead><tr>{th}</tr></thead><tbody>{"".join(tr)}</tbody></table></div>'
    if caption:
        EX[0] += 1
        s = f'<p class="src">{source}</p>' if source else ""
        return f'<figure class="ex tbl"><figcaption>Exhibit {EX[0]}: {caption}</figcaption>{t}{s}</figure>'
    return t


def chip(word):
    cls = {"OK": "ok", "WATCH": "watch", "BULLISH": "ok", "CAUTIOUSLY OPTIMISTIC": "watch", "RED": "red", "MET": "ok", "MISSED": "red", "LATE": "watch",
           "OPEN": "open", "SOFTENED": "watch", "STRONG": "ok", "MODERATE": "watch", "WEAK": "red",
           "MAKES AND SELLS": "ok", "FIRST ORDERS": "watch", "IN DEVELOPMENT": "open",
           "NOT DISCLOSED": "nd", "DOES NOT MAKE": "nd", "NOT VERIFIED": "nd", "FAIR": "watch",
           "DELIVERED": "ok", "ON TRACK": "ok", "CHANGED": "watch", "MISSTATED": "red", "ATTRACTIVE": "ok",
           "PROVEN": "ok", "UNPROVEN": "red", "STRETCHED": "red", "PROBABLE": "watch", "CONFIRMED": "ok",
           "PARTLY PROVEN": "watch", "COMMERCIALISED": "ok", "VALIDATED": "watch", "PLANNED": "open",
           "GREEN": "ok", "AMBER": "watch", "CLEAN": "ok", "MIXED": "watch"}.get(word, "open")
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


# ================================================================= shared numbers
base_v, bear_v, bull_v = V["Base"]["value_ps"], V["Bear"]["value_ps"], V["Bull"]["value_ps"]
SH = D["shares_diluted"]
DISC = (1 + VAL["assumptions"]["cost_of_equity"]) ** VAL["assumptions"]["years_to_value_date"]
MULT = ASM["Base"]["multiple"]


def ps(ebitda_cr, mult=MULT):
    """Rs a share today for Rs X cr of FY28 EBITDA at a multiple (same maths as the model's sensitivity grid) [E]."""
    return ebitda_cr * mult / SH / DISC


# the grid's slope must match ps(): Rs 28.16 cr more FY28 EBITDA at 15x
_g = VAL["sensitivity"]["rows"]
assert abs((_g[3]["values"][2] - _g[2]["values"][2]) - ps(_g[3]["fy28_ebitda"] - _g[2]["fy28_ebitda"])) < 0.05
h, b, p = D["h1"], D["bs"], CALC["per100"]
B27, B28 = ROWS["Base"][0], ROWS["Base"][1]
h2n, h2g = CALC["h2_need"], CALC["h2_need_g"]
cs_share = CALC["cash_stake_share"]

# ================================================================= S1 summary
rail = f"""<aside class="rail">
<div class="verdict"><p class="rk">Valuation readout</p><p class="rv">{READOUT}</p>
<p class="rs">Our base value is Rs {f0(base_v)} a share, {pc(V['Base']['vs_price'], 0, True)} vs the price of Rs {f0(D['price'])}. Within 20% either way counts as fair. The margin over that line is thin, and the readout turns FAIR if the stake is ignored. This is not a buy or sell call.</p></div>
<div class="rbox"><p class="rh">Value range (Rs a share)</p>
{table(["Case", "Value", "vs price"], [["Bear", f0(bear_v), (pc(V['Bear']['vs_price'], 0, True), "neg")], ["Base", (f0(base_v), "bold"), pc(V['Base']['vs_price'], 0, True)], ["Bull", f0(bull_v), pc(V['Bull']['vs_price'], 0, True)]], "kv")}</div>
<div class="rbox"><p class="rh">Key data, 9 Nov 2026</p>
{table(["Item", "Value"], [
    ["Price", f"Rs {f0(D['price'])}"],
    ["Market value (printed shares)", f"Rs {f0(CALC['mcap'])} cr"],
    ["52-week range", f"Rs {D['lo52']} to {D['hi52']}"],
    ["Sales, last 12 months", f"Rs {D['sales_ttm']} cr"],
    ["Profit, last 12 months", f"Rs {D['pat_ttm']} cr"],
    ["P/E, last 12 months", f"{f1(VAL['cross_checks']['ttm_pe_screener'])}x"],
    ["Cash less debt, Sep 2026", f"Rs {f0(CALC['net_cash'])} cr"],
    ["Promoter holding", "42.93%"],
    ["Management verdict", chip("WATCH")]], "kv")}</div>
<div class="rbox"><p class="rh">Dates to watch</p>
<p class="tiny">Q3 FY27 results: about early Feb 2027 (Q3 FY26 deck was filed {hd('2026-02-04')}). Test: quarterly sales of at least Rs {f0(DER['h2_need_q'])} cr and margin near 22%.<br>
FY27 results: about late May 2027. Test: full-year sales near Rs {f0(DER['base_fy27'])} cr and positive operating cash flow.<br>
Warrants: 56 lakh at Rs 196 to be converted by about Mar 2028 (18 months from allotment).</p></div>
</aside>"""

ann_cats = D["years"] + ["TTM"]
annual = C.grouped(ann_cats, [("Sales", D["sales"] + [D["sales_ttm"]], C.GREY), ("Operating profit (EBITDA)", D["op"] + [D["op_ttm"]], C.PRIMARY)],
                   "Annual sales and EBITDA FY20 to TTM", w=600, h=230)
s1_main = f"""<p class="lede">Ind-Swift Laboratories makes tablets, capsules and sachets in Punjab and Jammu and sells most of them abroad, under its own registrations or for partner companies such as Viatris.
Until 2024 it was mainly a maker of drug ingredients (APIs). It sold that business for Rs 1,650 cr, paid off its debt, kept a 7.80% stake in the buyer, and merged in its sister company's finished-medicine business.</p>
<p>In the first half of FY27 sales rose {pc(CALC['h1_g'], 1)} to Rs {f1(h['op_rev'][1])} cr and operating margin jumped from {f1(h['margin'][0])}% to {f1(h['margin'][1])}%.
This report answers one question first: <b>is that step-up a durable export business heading to Rs 1,500 cr, or a launch bump sitting on top of cash and a stake?</b></p>
<p>Our answer: <b>the step-up is real in the profit and loss account, but it is not yet a proven business.</b>
Most of the growth came from new partner launches: about Rs 80 to 90 cr of the Rs {f1(CALC['h1_inc'])} cr increase was from new customers, and one partner molecule went from Rs 25 cr in Q1 to Rs 58 cr in Q2.
The first link that is not yet proven is repeat orders turning into cash. Receivables and inventory rose Rs {f1(CALC['inv_rec_up'])} cr in a year, and operating cash flow was negative for three years running.</p>
<p>At Rs {f0(D['price'])}, cash and the stake (at management's own value) make up about {pc(cs_share)} of the market value.
The rest, about Rs {f0(CALC['core_ev'])} cr, buys the medicine business at {f1(VAL['reverse'][0]['x_fy27'])} times management's FY27 operating profit.
That is cheap only if the second half delivers: sales of Rs {f0(h2n)} cr, {pc(h2g, 0, True)} on last year's second half.</p>
<p>Of 22 management claims we tracked, 3 were met (2 delivered, 1 on track), 7 changed, 2 missed and 3 misstated, all three misstatements understating its own progress. We rate it WATCH, not RED.</p>"""
s1_charts = exhibit("After the FY25 break, sales and profit are rebuilding from a smaller base (Rs cr)", annual, src("scr"),
                    "FY20 to FY24 include the API business that was sold in FY24; FY25 onward is the finished-medicine business. The two periods are not comparable.")
s1_body = f'<div class="cover"><div class="cmain">{s1_main}{s1_charts}</div>{rail}</div>'
section("s1", "A", "Why read this", "S1 | Summary", "A real step-up in sales that still has to turn into cash",
        f"The first-half jump is real, but it rests on new partner launches and has not yet produced cash; at Rs {f0(D['price'])} our base value is {f0(V['Base']['vs_price'] * 100)}% higher, just past the attractive line, but only if the second half delivers; without that the bear case is {f0(-V['Bear']['vs_price'] * 100)}% lower.",
        s1_body,
        f"Our base value of Rs {f0(base_v)} is {pc(V['Base']['vs_price'], 0, True)} above the price, just past the line we call attractive. "
        f"It drops to Rs {f0(FRAG['no_stake']['value_ps'])} if the stake is never sold and to Rs {f0(FRAG['multiple_12']['value_ps'])} if the market keeps paying 12 times profit. "
        f"Three numbers will decide it: Q3 FY27 sales against Rs {f0(DER['h2_need_q'])} cr (Feb 2027), receivable days against {f0(DER['receivable_days'])} today, and operating cash flow for FY27 (May 2027).")

# ================================================================= S2 business simply
wf = C.waterfall([("Sales", 100, "total"), ("Materials", p["rm"], "down"), ("Staff", p["emp"], "down"), ("Other|costs", p["oth"], "down"),
                  ("EBITDA", p["ebitda"], "total"), ("Depreciation|and interest", p["dep_int"], "down"), ("Other|income", p["oi"], "up"),
                  ("Profit before|tax", p["pbt"], "total"), ("Tax and|other", p["tax"] + p["other"], "down"), ("Profit|after tax", p["pat"], "total")],
                 "What happens to Rs 100 of H1 FY27 sales", dec=1, w=760, h=270)
chain = flow([
    ("1. Develop", ["R&D at Panchkula (70+ scientists) builds a copy of an off-patent medicine. <small>About Rs 12 cr a year.</small>"], False),
    ("2. Register", ["A dossier is filed in each country. <small>1 to 1.5 years per approval; 900+ held, 540+ in its own name.</small>"], True),
    ("3. Approve the site", ["Regulators inspect the plant. <small>Derabassi: UK MHRA, Australia TGA, Health Canada.</small>"], False),
    ("4. Make", ["Tablets, capsules, sachets at Derabassi (export) and Samba (India). <small>70-75% used.</small>"], False),
    ("5. Sell", ["Own brands through local distributors, or contract supply to partners like Viatris. <small>About 83% of sales is export.</small>"], True),
    ("6. Get paid", ["Partners and distributors pay on credit. <small>Receivables about 103 days of sales today.</small>"], False),
])
milestones = [("1995", "Ind-Swift Laboratories incorporated; grows into an API maker with 481+ drug master files"),
              ("Aug 2024", "Warrant issue 1: 2.6 cr warrants at Rs 121 (Rs 314.60 cr)"),
              ("FY24", "API business sold to Synthimed (IndiaRF) for Rs 1,650 cr; about Rs 1,250-1,300 cr of debt repaid; 7.80% stake kept"),
              ("31 Mar 2024", "Ind-Swift Ltd's finished-medicine business merged in (effective date)"),
              ("FY26", "First full year as a finished-medicine exporter: Rs 636 cr sales, EBITDA margin about 7%"),
              ("Sep 2026", "Warrant issue 2 to the promoter entity Essix: 70 lakh at Rs 196; Viatris Ibuprofen supplies begin")]
tl = '<div class="tl">' + "".join(f'<div class="tli"><span class="tly">{y}</span>{t}</div>' for y, t in milestones) + "</div>"
gloss = [("FDF", "Finished dosage form: the tablet, capsule or sachet a patient takes."),
         ("API", "Active pharmaceutical ingredient: the chemical in a medicine that does the work."),
         ("Registration", "A country's approval to sell one product from one site, also called a marketing authorisation."),
         ("Own brand / own registration", "The approval is in Ind-Swift's name; a local distributor sells the product."),
         ("CMO / CDMO", "Contract (development and) manufacturing: making a product for a partner who holds the customer."),
         ("Transfer price", "The agreed price per pack a partner pays; Ind-Swift's margin is what is left after its cost."),
         ("P2P", "Product-to-product: making medicines in India for other Indian drug companies, paid in advance."),
         ("EOU", "Export-oriented unit: a plant set up mainly for exports, with duty benefits."),
         ("MHRA / TGA", "UK and Australian drug regulators; their approval of a plant opens those markets."),
         ("EU / PIC/S", "European and international inspection standards that open regulated markets."),
         ("EBITDA", "Operating profit before depreciation, interest and tax."),
         ("Working capital", "Cash tied up in stock and unpaid bills, less what is owed to suppliers."),
         ("Warrant", "A right to buy a new share later at a fixed price; 25% is paid upfront."),
         ("CCD", "Compulsorily convertible debenture: the instrument in which the Synthimed stake is held."),
         ("[E] and [G]", "[E] is our estimate or calculation; [G] is management guidance.")]
glossary = '<dl class="gl cols2">' + "".join(f"<div><dt>{a}</dt><dd>{b_}</dd></div>" for a, b_ in gloss) + "</dl>"

s2 = f"""<h3>The revenue equation</h3>
<p class="eq">Sales = own brands (registrations launched &times; units &times; price) + contract supply (partner volume &times; transfer price) + India (brands &times; units &times; price, plus P2P orders).</p>
<p>The three parts behave differently. Own brands grow slowly as each new registration earns money about two years after it is filed. Contract supply can jump in a quarter when a partner launches, but the partner decides the volume. India is small and was shrinking in FY26.</p>
{exhibit(f"Out of Rs 100 of H1 FY27 sales, Rs {f1(p['pat'])} was profit after tax", wf, src(("deck", 28), ("deck", 29)) + " Our calculation [E].",
         f"Cash view [E]: in FY26 operating cash flow was Rs {f1(CALC['fy26_ocf_per100'])} per Rs 100 of sales because stock and unpaid bills grew faster than profit. The H1 FY27 cash flow statement is not in the deck. 'Tax and other' includes Rs {f1(CALC['h1_other_items'])} cr between profit before tax less tax and the filed profit, which the deck does not explain.")}
<h3>How it makes money</h3>
{table(["Line", "What is sold", "To whom", "Share of Q2 FY27 sales"], [
    ["Own brands (export)", "Generic medicines registered in Ind-Swift's name in 60+ countries", "Local distributors; Europe is 47% of exports", f"{f1(D['mix_q2'][0])}%"],
    ["Contract manufacturing (export)", "Products made for partners at a transfer price", "Viatris, Arrotex (Australia), Manx (UK), a European partner for Ezetimibe+Atorvastatin", f"{f1(D['mix_q2'][1])}%"],
    ["Branded generics (India)", "Own brands sold through stockists", "3,000 stockists, 20,000 retailers", f"{f1(D['mix_q2'][2])}%"],
    ["Ethical (India)", "Brands promoted to doctors", "25,000+ doctors", f"{f1(D['mix_q2'][3])}%"],
    ["P2P (India)", "Contract supply to Indian drug companies, paid in advance", "Cipla, Lupin, Mankind, Concord; 39 repeat clients", f"{f1(D['mix_q2'][4])}%"]],
    "std", caption="Five lines, two of them export", source=src(("deck", 20), ("deck", 10), ("deck", 22), ("call", 5)))}
<h3>Contract terms and who benefits</h3>
{table(["Term", "What is known", "Who benefits"], [
    ["Viatris pricing", "Transfer price, not cost plus", "Ind-Swift if its costs fall; Viatris if prices in the market fall and it renegotiates"],
    ["Viatris volume", "Viatris decides volumes", "Viatris"],
    ["Exclusivity", "Ind-Swift is the sole worldwide maker of Viatris's Ibuprofen and Clarithromycin; it cannot sell the technology to others", "Both: Ind-Swift gets a locked-in customer, Viatris a locked-in supplier"],
    ["Length, minimum volumes, take-or-pay, price resets", "Not disclosed", "Unknown"],
    ["P2P in India", "Advance payment", "Ind-Swift (no credit risk)"],
    ["Own-brand distributors", "Credit terms not disclosed; CFO says collection averages 75 days", "Distributors today: receivables are 103 days [E]"]],
    "std", caption="What the contracts say, and who holds the power", source=src(("call", 16), ("deck", 14), ("call", 13), ("deck", 10)))}
<h3>The value chain</h3>
{chain}
<p class="src">{src(("deck", 7), ("deck", 8), ("call", 15))}</p>
<div class="keep"><h3>Six milestones</h3>
{tl}
<p class="src">{src(("deck", 6), ("ar26", 40), ("caref", 4), "nsea", ("trq1", 9))}</p></div>
<h3>Words used in this report</h3>
{glossary}"""
section("s2", "A", "The business simply", "S2 | The everyday picture", "A medicine maker that sells abroad, mostly through other people's hands",
        "Ind-Swift makes copies of off-patent medicines in India and sells about 83% of them abroad; it earns from approvals it holds and from partners it supplies, and it waits about 103 days to be paid.",
        s2,
        "The business is simple to describe but slow to prove: each approval takes years to earn money, and the fastest-growing part, contract supply, is the part where the partner holds the power. Watch the share of sales from own brands; the company aims for 65:35 own brands to contract supply.")

# ================================================================= S3 products
types = [("Tablets", "9 bn a year"), ("Capsules", "120 mn"), ("Sachets", "150 mn"), ("Stick packs", "184 mn"), ("Dry-syrup bottles", "33 mn"), ("Pellets", "30 tonnes")]
tgrid = '<div class="plants">' + "".join(f'<div class="plant"><p class="pn">{a}</p><p class="pl">Derabassi capacity</p><p class="pu">{b_}</p></div>' for a, b_ in types) + "</div>"
t9 = CALC["top9_cr"]
top9 = C.hbars([n for n, _, _ in t9], [v for _, _, v in t9], "FY26 sales of the top nine products, Rs cr", dec=1, w=760, lab_w=170,
               notes={i: f"({pc(v / a - 1, 0, True)} on FY25)" for i, (n, a, v) in enumerate(t9)}, highlight={0, 1})
cards = [("Atorvastatin", "Cholesterol", f"Rs {f1(t9[0][2])} cr in FY26, up from Rs {f1(t9[0][1])} cr", "Largest single product; Europe-heavy"),
         ("Ezetimibe + Atorvastatin", "Cholesterol, combination", f"Rs {f1(t9[1][2])} cr in FY26, up from Rs {f1(t9[1][1])} cr; Rs 58 cr in Q2 FY27 alone", "One European partner; partner name not verified"),
         ("Fexofenadine", "Allergy", f"Rs {f1(t9[2][2])} cr in FY26, down {pc(1 - t9[2][2] / t9[2][1], 0)}", "Old product, slowly falling"),
         ("Ibuprofen sachet (Viatris)", "Pain, new", "USD 12.0 mn launch value; Rs 20 cr expected in Q3 FY27 and Rs 20-25 cr in Q4 [G]", "Supplying since Sep 2026; Viatris sets volume")]
pcards = '<div class="cards">' + "".join(f'<div class="card"><p class="ct">{a}</p><p class="cs">{b_}</p><p class="cm">{c_}</p><p class="cn">{d_}</p></div>' for a, b_, c_, d_ in cards) + "</div>"
s3 = f"""<h3>What it can make</h3>
{tgrid}
<p class="src">{src(("deck", 8))}</p>
{exhibit(f"Nine products were {pc(CALC['top9_share'], 1)} of FY26 sales; two cholesterol products alone were {pc(CALC['ator2_share'], 1)}", top9, src(("deck", 19)) + " Rs lakh converted to Rs cr; shares of Rs 635.89 cr FY26 operating revenue [E].")}
<h3>The products that matter</h3>
{pcards}
<p class="src">{src(("deck", 19), ("deck", 21), ("call", 4), ("call", 5))}</p>
<h3>What is new</h3>
{table(["Launch", "Launch value (USD mn)", "About Rs cr [E]", "Status", "Year"], [[a, f1(u), f0(u * D['usd_inr'] / 10), chip(st.split(";")[0].upper()) + ("" if ";" not in st else f" <span class='tiny'>{st.split(';')[1].strip()}</span>"), y] for a, u, st, y in D["launches"]]
        + [[("Total", "bold"), (f1(CALC['launch_usd']), "bold"), (f0(CALC['launch_inr']), "bold"), "", ""]], "std",
        caption="Six launches worth about USD 44 mn a year at full run rate, if partners order as planned", source=src(("deck", 21), ("call", 3), ("call", 10)) + f" Rupees at Rs {D['usd_inr']} to the dollar [E].")}
<p>Behind these, 13 molecules are in development (Rosuvastatin, Dapagliflozin, Sitagliptin, Empagliflozin, Edoxaban and others), with revenue from Q4 FY29. Management says there is no new molecule in FY28, so FY28 growth must come from products already on sale.</p>
<p class="src">{src(("deck", 24), ("call", 17))}</p>
<h3>The biggest threat</h3>
<p>Two cholesterol products are a quarter of sales, sold mostly in Europe, where generic prices fall each year in tenders. A large customer moving one of them to another supplier would take out more than the whole Q2 profit. The partner for the faster-growing one is not verified.</p>"""
section("s3", "A", "Products", "S3 | What it sells", "A wide product list, but two cholesterol pills carry the growth",
        f"Ind-Swift can make most common tablet and sachet types at scale, but nine products are {pc(CALC['top9_share'])} of sales and two cholesterol products are {pc(CALC['ator2_share'])}.",
        s3,
        "The product list looks broad, but the money is concentrated. When the company reports, look for whether growth spreads beyond the two Atorvastatin products and the Viatris launches; if it does not, the business is more fragile than its 900+ approvals suggest.")

# ================================================================= S4 segments
mix = C.stacked100(["Q1 FY27", "Q2 FY27"], [(n, [a, b_], col) for n, a, b_, col in zip(D["mix_lines"], D["mix_q1"], D["mix_q2"], [C.PRIMARY, C.SECOND, C.THIRD, C.FOURTH, C.GREY])],
                   "Share of sales by line, Q1 and Q2 FY27", w=760, lab_w=80)
geo = C.hbars(list(D["geo"].keys()), list(D["geo"].values()), "Export sales by region, % of exports", unit="%", w=460, lab_w=130, highlight={0})
seg_rows = [[D["mix_lines"][i], f1(D["mix_q1"][i]) + "%", f1(D["mix_q2"][i]) + "%", f1(CALC["q2_line_rs"][i]), gm, ("Not disclosed", "flag")]
            for i, gm in enumerate(["50-55%", "About 42% (analyst figure, not disputed)", "Not disclosed", "70-80% (chronic 76%)", "Not disclosed"])]
s4 = f"""{exhibit("Contract supply edged up as a share in Q2; own brands are still the largest line", mix, src(("deck", 20)))}
{table(["Line", "Q1 FY27 share", "Q2 FY27 share", "Q2 Rs cr [E]", "Gross margin", "Line EBITDA"], seg_rows, "std",
       caption="Margins by line are partly disclosed; line profits are not", source=src(("deck", 20), ("deck", 22), ("deck", 23), ("trq1", 5)) + " Q2 rupees are shares of Rs 234.89 cr operating revenue [E].")}
<p>The call gave Q2 own-brand exports as Rs 125 cr and contract supply as Rs 65 cr; our split of the deck shares gives Rs {f0(CALC['q2_line_rs'][0])} cr and Rs {f0(CALC['q2_line_rs'][1])} cr. The deck puts the export split at 69:31, the call at 68:32; the target is 65:35.
India fell {pc(-CALC['dom_g'], 1)} in FY26 while exports rose {pc(CALC['exp_g'], 1)}.</p>
<p class="src">{src(("call", 5), ("deck", 20), ("ar26", 93))}</p>
{duo(exhibit("Europe is nearly half of exports", geo, src(("deck", 14))),
     table(["Year", "Export", "India", "Export share"], [[y, f1(e), f1(d_), pc(e / (e + d_), 1)] for y, (e, d_) in D["exp_dom"].items()], "std",
           caption="Standalone revenue by segment (Rs cr)", source=src(("ar26", 93))))}"""
section("s4", "A", "Segments", "S4 | Where the money comes from", "Exports carry the business; India is small and shrinking",
        f"About {pc(CALC['export_share_q2'] / 100)} of sales is export, split roughly two-thirds own brands and one-third contract supply; the company does not disclose profit by line, so which line earns the 18% margin is unknown.",
        s4,
        "Own brands earn a higher gross margin than contract supply (50-55% vs about 42%), so a rising contract share can lift sales while holding margin back. Ask for line-level profit; until it is given, the margin story rests on totals.")

# ================================================================= S5 customers and partners
s5 = f"""{table(["Partner or channel", "What they buy", "Status", "What is known about terms"], [
    ["Viatris", "Ibuprofen sachet (USD 12.0 mn) and Clarithromycin (USD 6.0 mn), exclusive worldwide supply", chip("CONFIRMED") + " Ibuprofen supplying; Clarithromycin awaiting the customer's variation", "Transfer price; Viatris drives volume; about Rs 200 cr by FY29 [G]; 10-year relationship"],
    ["European partner, Ezetimibe+Atorvastatin", "One cholesterol combination", chip("CONFIRMED") + " Rs 25 cr in Q1, Rs 58 cr in Q2 FY27", "Name not verified; terms not disclosed"],
    ["Arrotex (Australia)", "Contract supply", chip("CONFIRMED") + " named in filings", "Not disclosed"],
    ["Manx (UK)", "Macrogol sachets (USD 5.5 mn)", chip("CONFIRMED") + " commercialised", "Not disclosed"],
    ["Abbott", "Listed against two FY29 launch lines in Feb 2026", chip("PROBABLE") + " dropped from the Nov 2026 table", "Not disclosed"],
    ["Two further contract customers", "Not named", chip("OPEN") + " 'hope to sign off in the last quarter'", "Not disclosed"],
    ["Own-brand distributors", "Own registrations in 60+ countries", chip("CONFIRMED"), "Credit terms not disclosed"],
    ["Indian drug companies (P2P)", "Contract supply in India", chip("CONFIRMED") + " Cipla, Lupin, Mankind, Concord", "Advance payment"]],
    "std stack", caption="Who buys, and how much is locked in", source=src(("deck", 14), ("deck", 21), ("call", 5), ("call", 10), ("call", 13), ("call", 16), ("trq1", 3), ("trq1", 5), ("dq3", 16), ("deck", 10)))}
<p>About Rs 80 to 90 cr of the Rs {f1(CALC['h1_inc'])} cr first-half increase came from new customers, which is {pc(CALC['new_cust_share'][0])} to {pc(CALC['new_cust_share'][1])} of the growth [E]. The partner molecule's Rs 83 cr in H1 is an upper bound on its share of the increase, because its H1 FY26 sales are not disclosed.</p>
<blockquote class="q"><p>"it is VITRIS only who is driving the sales"</p><cite>Management on the Viatris volumes, Q2 FY27 call, p.16 (machine transcript spelling)</cite></blockquote>"""
section("s5", "A", "Customers", "S5 | Customers and partners", "A few partners drive the growth, and they set the volumes",
        "Viatris and one European partner explain most of the new growth; both are real and supplying, but neither contract's length, minimums or price resets is disclosed.",
        s5,
        "Partner launches can lift sales fast and cut them just as fast. The useful signal is whether Q3 and Q4 orders from the same partners repeat at Q2 levels; a fall back would show Q2 was stocking, not demand.")

# ================================================================= S6 moat
moat = [("Site approvals (MHRA, TGA, Health Canada)", "MODERATE", "Derabassi is approved by three strict regulators; a new site takes years to qualify.", "Approvals are company claims; regulator databases were not checked, and EU GMP status is not stated."),
        ("Registration library", "MODERATE", "900+ approvals, 540+ in its own name; each takes 1 to 1.5 years.", "How many earn money is not disclosed; average yield is about Rs 0.93 cr per own registration a year [E]."),
        ("Exclusive partner supply", "MODERATE", "Sole worldwide maker for two Viatris products; the partner filed variations naming the site.", "The partner holds the customer and the volume; a transfer price can be renegotiated."),
        ("Low-cost Indian manufacturing", "WEAK", "Export-oriented unit with Indian labour costs; margin rose to 18% on a flat staff bill.", "Every Indian generic exporter has this; it is a ticket to play, not a moat."),
        ("Customer relationships in India (P2P)", "WEAK", "Cipla, Lupin, Mankind and Concord as repeat clients, paid in advance.", "Only 5% of sales; India fell in FY26."),
        ("Brand", "WEAK", "Ethical brands with 25,000+ doctors.", "About 5% of sales; not a source of advantage abroad.")]
mcards = '<div class="cards">' + "".join(f'<div class="card"><p class="ct">{a}</p><p class="cs">{chip(b_)}</p><p class="cm">{c_}</p><p class="cn"><b>Counter-point:</b> {d_}</p></div>' for a, b_, c_, d_ in moat) + "</div>"
s6 = f"""{mcards}
<p class="src">{src(("deck", 7), ("deck", 8), ("deck", 10), ("deck", 14), ("deck", 28), ("call", 11), ("call", 15), ("call", 16))}</p>
"""
section("s6", "A", "Moat", "S6 | What protects it", "Approvals and partner ties give a moderate moat, not a wide one",
        "The advantages are regulatory approvals and partner exclusivity, which take years to copy; they are real but shared with many Indian exporters, and none yet shows in high returns on capital.",
        s6,
        "Do not pay for a wide moat. What would widen it is proof that registrations earn steadily without partners and that cash returns rise; neither is shown yet.")

# ================================================================= S7 quantity vs quality
s7 = f"""{table(["Measure", "Quantity (what is growing)", "Quality (what it is worth)"], [
    ["Sales", f"H1 FY27 {pc(CALC['h1_g'], 1, True)}; Q2 {pc(CALC['q2_yoy'], 1, True)}", f"72-81% of the H1 increase from new customers; one partner molecule Rs 83 cr of H1"],
    ["Approvals", "900+ registrations; 333 expected in FY27 [G]", "Revenue-earning count not disclosed; about Rs 0.93 cr per own registration a year [E]"],
    ["Margin", f"EBITDA margin {f1(h['margin'][0])}% to {f1(h['margin'][1])}%", "Driven by staff cost spread over more sales, not by higher gross margin; raw material share rose Q1 to Q2"],
    ["Profit", f"H1 profit after tax Rs {f1(h['pat'][0])} cr to Rs {f1(h['pat'][1])} cr", f"Inventory plus receivables up Rs {f1(CALC['inv_rec_up'])} cr in a year, more than twice H1 profit"],
    ["Cash", f"Rs {f0(CALC['net_cash'])} cr net cash", f"Operating cash flow negative three years, Rs {f0(CALC['ocf_3y'])} cr in total; Rs 16 cr of deposits pledged"],
    ["Concentration", "Nine products", f"{pc(CALC['top9_share'])} of FY26 sales; two products {pc(CALC['ator2_share'])}"]],
    "std", caption="Growth is strong on volume and weak on quality so far", source=src(("deck", 19), ("deck", 28), ("deck", 29), ("deck", 30), ("call", 5), ("call", 11), "scr"))}
{duo(exhibit("Raw material took a larger share of sales in Q2 as contract supply grew (%)",
             C.lines(D["dq"], [("Raw material", CALC["rm_pct"], C.SECOND, False), ("Staff", CALC["emp_pct"], C.PRIMARY, False), ("Other costs", CALC["oth_pct"], C.GREY, True)],
                     "Cost lines as % of revenue", dec=1, w=460, h=230, ymin=0, ymax=60, all_labels=True), src(("deck", 28)) + " Our calculation on the deck revenue line [E]."),
     exhibit("Inventory and receivables grew far faster than sales (Rs cr)",
             C.grouped(["Inventory", "Receivables", "Payables"], [("Sep 2025", [b["inventory"][0], b["receivables"][0], b["payables"][0]], C.GREY), ("Sep 2026", [b["inventory"][1], b["receivables"][1], b["payables"][1]], C.PRIMARY)],
                       "Working capital items, Sep 2025 and Sep 2026", w=460, h=230), src(("deck", 30))))}"""
section("s7", "A", "Quantity vs quality", "S7 | Quantity vs quality", "The growth is large in volume and thin in quality, so far",
        f"Sales and margin have stepped up sharply, but the growth is narrow, leans on new partners, and has tied up Rs {f0(CALC['inv_rec_up'])} cr in stock and unpaid bills.",
        s7,
        "Quantity is easy to report; quality shows up in cash. The single best test of quality in the next two results is whether receivables stop rising faster than sales.")

# ================================================================= S8 API exit before and after
before = f"""<div class="fb"><p class="pn">Before: API maker (FY23)</p><p>Sales Rs {f0(D['sales'][3])} cr; EBITDA Rs {f0(D['op'][3])} cr ({pc(D['op'][3] / D['sales'][3], 0)})</p><p>Debt Rs {f0(D['debt'][3])} cr; interest Rs 92 cr</p><p>Profit after tax Rs {f0(D['pat'][3])} cr</p><small>Ingredient sales to drug makers; 481+ drug master files</small></div>"""
after = f"""<div class="fb gold"><p class="pn">After: medicine exporter (FY26)</p><p>Sales Rs {f0(D['sales'][6])} cr; EBITDA Rs {f0(D['op'][6])} cr ({pc(D['op'][6] / D['sales'][6], 0)})</p><p>Debt Rs {f0(D['debt'][6])} cr; interest Rs 1 cr</p><p>Profit after tax Rs {f0(D['pat'][6])} cr, of which other income Rs {f0(D['oi'][6])} cr</p><small>Plus Rs 348 cr net cash (Sep 2026) and a 7.80% Synthimed stake carried at Rs 32 cr</small></div>"""
ba = f'<div class="ba">{before}<div class="farrow" aria-hidden="true">&#8594;</div>{after}</div>'
oi = C.bars(D["years"] + ["TTM"], D["oi"] + [D["oi_ttm"]], "Other income FY20 to TTM, Rs cr", w=760, h=220, highlight={4, 5}, notes={4: "sale gains", 5: "sale gains"})
pat_ex = [D["pat"][4] - 434, D["pat"][5] - 292]
s8 = f"""{ba}
<p class="src">{src("scr", ("deck", 6), ("trq1", 9))}</p>
{exhibit("FY24 and FY25 profits were mostly one-off gains from the sale (Rs cr)", oi, src("scr"),
         f"Other income was Rs 434 cr in FY24 and Rs 292 cr in FY25. Taking it out of profit after tax before tax effects leaves Rs {f0(pat_ex[0])} cr and Rs {f0(pat_ex[1])} cr [E], so the headline profits of Rs 421 cr and Rs 250 cr say nothing about the business that remains.")}
{table(["Item", "What happened", "Status"], [
    ["Sale price", "Rs 1,650 cr for the API business to Synthimed (IndiaRF)", chip("CONFIRMED")],
    ["Debt", "About Rs 1,250-1,300 cr repaid; debt Rs 862 cr (FY23) to Rs 17 cr (FY24)", chip("CONFIRMED")],
    ["Stake kept", "7.80% of Synthimed as 32 lakh CCDs, carried at Rs 32 cr at fair value through profit and loss, unchanged from FY25", chip("CONFIRMED")],
    ["Raw material from Synthimed", "About Rs 100 cr of Rs 400 cr purchases this year; Synthimed is not a related party, so terms are not reported", chip("NOT DISCLOSED")],
    ["Escrow, indemnities, tax on the sale", "Not found in documents read", chip("NOT DISCLOSED")],
    ["Merger of Ind-Swift Ltd", "Effective 31 Mar 2024; 45,15,495 shares issued; pre-merger accounts not collected", chip("NOT DISCLOSED")]],
    "std", caption="The sale and merger, item by item", source=src(("deck", 6), ("ar26", 80), ("ar26", 92), ("ar26", 40), ("call", 14), ("trq1", 9)))}"""
section("s8", "A", "The API exit", "S8 | Before and after the sale", "A new, smaller company was born in FY24, and its old profits do not count",
        "Selling the API business cleared Rs 1,250 cr of debt and left a smaller medicine exporter with cash and a stake; the large FY24 and FY25 profits were one-off gains, so the real track record starts in FY26.",
        s8,
        "Any long-term chart of this company mixes two different businesses. Judge it on FY26 onward only, and treat the Rs 434 cr and Rs 292 cr gains as history.")

# ================================================================= S9 capacity and capex
plants = f"""<div class="plants p2">
<div class="plant"><p class="pn">Derabassi, Punjab</p><p class="pl">Export-oriented unit, 81,325 sq m</p><p class="pu">70-75% used</p><p class="pr">Approved by UK MHRA, Australia TGA, Health Canada. Deck says it supports more than Rs 1,000 cr of sales; CFO says enough for Rs 1,200 cr by FY28.</p></div>
<div class="plant"><p class="pn">Samba, Jammu</p><p class="pl">WHO-GMP, 14,700 sq m</p><p class="pu">70-75% used</p><p class="pr">India and emerging markets today. Rs 45 cr upgrade for EU/PIC/S approval expected "anytime next year"; Brazil ANVISA inspection held.</p></div>
</div>"""
util = C.hbars(["Derabassi", "Samba"], [72.5, 72.5], "Plant utilisation, midpoint of the 70-75% given", unit="%", w=460, lab_w=90, max_v=100, track=True, dec=1)
hist_capex = CALC["capex_hist"]
cap = C.grouped(D["years"], [("Capex", hist_capex, C.SECOND), ("Operating cash flow", D["ocf"], C.PRIMARY), ("Depreciation", D["dep"], C.GREY)],
                "Capex, operating cash flow and depreciation FY20 to FY26", w=760, h=250)
plan = C.bars(["H2 FY27", "FY28", "FY29", "FY30"], [r["capex"] for r in ROWS["Base"]], "Planned capex in our base case, Rs cr", hatch={0, 1, 2, 3}, w=460, h=200,
              colors=[C.PRIMARY] * 4)
s9 = f"""{plants}
<p class="src">{src(("deck", 8), ("call", 3), ("call", 8))}</p>
{duo(exhibit("Both plants are about three-quarters used", util, src(("call", 3), ("call", 8)), "Management gave the same 70-75% for both plants; we show the midpoint."),
     exhibit("The Rs 250 cr plan, as spread in our model [E]", plan, src(("call", 1), ("trq1", 5), "model"), "Rs 320 cr in the model including maintenance; project-wise detail is not disclosed."))}
{exhibit("In the new business, capex has run ahead of cash from operations (Rs cr)", cap, src("scr"),
         f"Capex is operating cash flow less free cash flow [E]. FY24 includes the sale year. Capex of Rs {f0(min(hist_capex[-3:]))}-{f0(max(hist_capex[-3:]))} cr a year in FY24 to FY26 against negative operating cash flow means growth has been funded by sale proceeds and warrants.")}
{table(["Item", "Plan or claim", "Status"], [
    ["Total plan", "Rs 250 cr over 2 to 2.5 years from internal accruals [G]", chip("ON TRACK") + " on spend; funding claim " + chip("CHANGED")],
    ["Capital work in progress", f"Rs 0 (Sep 2025) to Rs {f1(b['cwip'][1])} cr (Sep 2026)", chip("CONFIRMED")],
    ["Samba EU/PIC/S upgrade", "Rs 45 cr", chip("OPEN")],
    ["Warehouse", "18,000 sq yd, 10 to 12 months", chip("OPEN")],
    ["New warrant money", "Rs 137.20 cr from Essix in Sep 2026; Rs 41.40 cr for expansion, Rs 53.00 cr working capital", chip("CONFIRMED")],
    ["Behra land (from issue 1)", "Bought for a new plant; found unsuitable; sold Aug 2026 at a Rs 0.22 cr loss, Rs 1.96 cr of Rs 17.50 cr received", chip("MISSED")]],
    "std", caption="Capex tracker", source=src(("call", 1), ("call", 2), ("deck", 30), ("careq2", 7), ("caref", 6), ("caref", 10)))}
<p>Asset turnover is {f1(CALC['at_now'])}x today (H1 sales annualised over plant and work in progress) and {f1(VAL['cross_checks']['asset_turnover_fy30'])}x at Rs 1,500 cr on the base plus Rs 250 cr, so the plan is roughly sized for the target if most of it is growth capex [E].</p>"""
section("s9", "A", "Capacity", "S9 | Plants and capex", "Enough capacity for about Rs 1,000 to 1,200 cr; Rs 1,500 cr needs the new spend",
        "The two plants are about 70-75% used and can carry roughly Rs 1,000-1,200 cr of sales; the Rs 250 cr plan is sized for the Rs 1,500 cr target, but it was described as self-funded and then a promoter warrant issue was raised.",
        s9,
        "Capacity is not the constraint for FY27 or FY28; orders and cash are. Watch Samba's EU approval, which would let the second plant serve regulated markets, and whether capex keeps running ahead of operating cash flow.")


# ================================================================= S10 management
people = table(["Person", "Role", "What the filings show"], [
    ["N.R. (Navrattan) Munjal", "Chairman and Whole Time Director, promoter", "Pay unchanged in FY26; ratio to median employee among the highest on the board"],
    ["Sahil Munjal", "Managing Director, Global Operations", "FY26 pay +72.13%"],
    ["Himanshu Jain", "Managing Director, Domestic Operations", "FY26 pay -5.06%"],
    ["Rishav Mehta", "Whole Time Director", "FY26 pay +100.08%"],
    ["Gagan Agarwal", "Chief Financial Officer", "20+ years at the group, rose from management trainee; leads the calls; pay +20.28%"]],
    "std", caption="Who runs the company", source=src(("deck", 24), ("deck", 25), ("ar26", 64), ("carer24", 1)))
skin = C.lines(D["q"], [("Promoter holding", D["promoter"], C.PRIMARY, False), ("Foreign investors", D["fii"], C.SECOND, False)],
               "Promoter and foreign investor holding, Dec 2024 to Sep 2026, %", unit="%", dec=1, w=900, h=250, ymin=0, ymax=60, end_labels=True)
cap_alloc = table(["Money", "Stated use", "What happened", "Status"], [
    ["Rs 1,650 cr API sale (FY24)", "Clear debt, build the medicine business", "About Rs 1,250-1,300 cr of debt repaid; Rs 348 cr net cash today; about Rs 308 cr in promoter-linked or unlisted instruments", chip("WATCH")],
    [f"Warrants 1: Rs {D['w1']['amt']} cr at Rs {D['w1']['price']}", "Expansion, a new plant on the Behra land", f"Rs {D['w1']['lapsed_amt']} cr lapsed; Rs {f1(CALC['w1_raised'])} cr raised and used; Behra land sold at a loss; some end use not traceable (funds commingled)", chip("MISSED")],
    [f"Warrants 2: Rs {D['w2']['amt']} cr at Rs {D['w2']['price']}, promoter only", "Expansion Rs 41.40 cr, working capital Rs 53.00 cr", f"Rs {D['w2']['upfront']} cr upfront; 14 lakh converted for Rs {D['w2']['conv_amt']} cr; Rs {f1(CALC['w2_to_come'])} cr still to come", chip("OPEN")],
    ["Capex Rs 250 cr", "From internal accruals", "A promoter warrant issue was raised anyway; reason not explained", chip("CHANGED")],
    ["Dividends and buybacks", "None", "None since the sale", chip("OPEN")]],
    "std", caption="Capital allocation: every rupee raised and where it went", source=src(("trq1", 9), ("caref", 5), ("caref", 8), ("caref", 10), ("careq2", 4), ("careq2", 7), ("nsec", 1), ("ar26", 80)))
tone = table(["Call", "Tone", "What they pushed", "What they avoided"], [
    ["Q1 FY27, Aug 2026", chip("BULLISH"), "\"18% is fully sustainable\"; Rs 900 cr for FY27; CDMO Rs 200-220 cr", "Quarterly utilisation (\"annual basis only\")"],
    ["Q2 FY27, Nov 2026", chip("CAUTIOUSLY OPTIMISTIC"), "\"we don't foresee any risk\" on FY27; Rs 1,000 cr \"minimum internal target\"; 22% Q3 margin", "FY28 (\"Very difficult for me to comment\"), capex detail, constant-currency growth, how many registrations earn revenue"]],
    "std", caption="How they communicate, call by call (our tone reading)", source=src(("trq1", 6), ("trq1", 10), ("trq1", 13), ("call", 6), ("call", 11), ("call", 13), ("call", 16)))
flags = table(["Hard red flag", "Found?", "Detail"], [
    ["Qualified audit or going-concern language", chip("OK"), "Unmodified opinion with two emphasis-of-matter items (share issues; Baddi Unit IV sale)"],
    ["Rising promoter pledge", chip("NOT DISCLOSED"), "No pledge disclosure found in AR FY26, AR FY25, decks or CARE reports; SAST filings not queried"],
    ["Deviation in use of proceeds", chip("WATCH"), "CARE reports no deviation, but could not trace some end use because funds were commingled"],
    ["Loans to promoter-linked entities", chip("WATCH"), "SFRE society loan Rs 62.89 cr with no repayment terms; related-party loans Rs 10.65 cr (or Rs 25.20 cr; two notes disagree)"],
    ["Active investigation", chip("OK"), "None found in documents read"],
    ["Repeated guidance misses", chip("WATCH"), "Seven claims changed and two missed in ten months; the H2 FY27 number is the test"]],
    "std", caption="Hard red-flag checklist", source=src(("ar26", 37), ("ar26", 68), ("ar26", 81), ("ar26", 92), ("caref", 5), ("caref", 10)))
s10 = f"""<h3>Who they are</h3>
{people}
<p>The Munjal family controls the board; the CFO is the public face on calls. Board independence and succession plans were not assessed beyond the annual report's governance section, and the deck's experience bullets do not line up cleanly with names, so we do not attribute tenures.</p>
<h3>Skin in the game</h3>
{exhibit("The promoter has bought back up to 43% through warrants while foreign investors came and partly left", skin, src("scr", "nsea", "nsec"),
         "If all 56 lakh outstanding warrants convert, promoter holding rises to about 47.2% on 9,39,61,558 shares [E].")}
<p>Key managers were paid Rs {D['kmp_pay'][1]} cr in FY26 (Rs {D['kmp_pay'][0]} cr in FY25), about {f0(CALC['kmp_pct'])}% of standalone profit of Rs {D['pat_standalone_fy26']} cr [E]. Two promoter directors got raises of 72% and 100% while the median employee got 8.07%.</p>
<h3>Capital allocation</h3>
{cap_alloc}
<p>The company holds Rs 28.85 cr of shares in Essix Biosciences, the promoter entity that is funding it through warrants. Money flows both ways between the company and its promoter.</p>
<h3>Do they deliver?</h3>
<p>Of 22 claims we tracked from Jan to Nov 2026, 15 can be judged today. Three were met as stated (2 delivered, 1 on track): a <b>credibility score of 20%</b> of judged claims. Seven changed, two missed and three were misstated. Detail in S11.</p>
<h3>How they communicate</h3>
{tone}
<p>Hard questions get deferrals rather than numbers. Asked how many registrations earn revenue, the CFO said "we can come back to you on this" [call p11]. Asked for FY28, he said a number would come on the next call [call p6].</p>
<h3>Hard red flags and fairness to minorities</h3>
{flags}"""
section("s10", "B", "Management", "S10 | Management", "Delivering on margin, loose on promises and on where the cash sits",
        "Verdict WATCH: no qualified audit, no disclosed pledge and no reported deviation in use of funds, but loans without terms, a promoter-linked treasury book, steep pay rises for promoter directors and a 20% credibility score on judged claims.",
        s10,
        "WATCH does not cap the valuation readout; RED would. A RED would need a qualified audit, a disclosed pledge, a CARE deviation or a clear H2 FY27 miss. Until then, discount management's numbers and trust the filed deck tables over spoken figures.")

# ================================================================= S11 claims ledger
L = [
    (1, "18% EBITDA margin \"fully sustainable\"", "Aug 2026, CFO", "Q2 FY27 margin 18.02%", "DELIVERED"),
    (2, "Margin above 18% from Q3; 22% target in Q3", "Aug and Nov 2026, CFO", "Q3 not yet reported", "OPEN"),
    (3, "FY27 revenue growth above 50%", "Aug and Nov 2026, deck and CFO", f"H1 +35.8%; H2 must be Rs {f0(h2n)} cr, {pc(h2g, 1, True)} on H2 FY26 [E]", "OPEN"),
    (4, "FY27 revenue Rs 900 cr", "Aug 2026, CFO", "Raised to a Rs 1,000 cr \"minimum internal target\" in Nov", "CHANGED"),
    (5, "CDMO adds Rs 200-220 cr in FY27", "Feb and Aug 2026, deck and call", "Cut to Rs 100-130 cr in Nov", "CHANGED"),
    (6, "CDMO from Rs 180 cr to Rs 550-600 cr in 4 years", "Feb 2026, deck", "Became Rs 635 cr in 3 years, then Rs 200-220 cr over 2 years", "CHANGED"),
    (7, "Revenue Rs 1,200+ cr by FY29", "Feb and Aug 2026, decks", "Replaced by Rs 1,500+ cr by FY30", "CHANGED"),
    (8, "Margin up 250-300 bp, then 600-800 bp, then 200-300 bp", "Three decks", "Three numbers in ten months", "CHANGED"),
    (9, "400+ new registrations in FY27", "Feb and Aug 2026", "Cut to 333; 100-150 done by Nov", "CHANGED"),
    (10, "Viatris supplies begin in 2026", "Feb 2026, deck", "Ibuprofen approved and supplying", "DELIVERED"),
    (11, "Clarithromycin launch in FY27", "Feb 2026, deck", "Validation done; partner's site variation awaited", "OPEN"),
    (12, "Ibuprofen Rs 20 cr in Q3, Rs 20-25 cr in Q4", "Nov 2026, CFO", "Not yet reported", "OPEN"),
    (13, "Rs 250 cr capex from internal accruals", "Aug and Nov 2026", "Capital work in progress Rs 41.82 cr; but a Rs 137.20 cr warrant issue raised", "ON TRACK"),
    (14, "No Synthimed stake sale this year", "Aug 2026, CFO", "Nov: buyer diligence under way, may tag along", "CHANGED"),
    (15, "Behra land for a new plant", "Jan 2025, use of issue money", "Unsuitable; sold Aug 2026 at a Rs 0.22 cr loss", "MISSED"),
    (16, "Warrant issue 1 to raise Rs 314.60 cr", "Aug 2024 allotment", "Rs 58.99 cr lapsed", "MISSED"),
    (17, "Q2 growth \"15.15%\"", "Nov 2026, call", "50.16% computed [E]", "MISSTATED"),
    (18, "Q1 EBITDA \"2.85x\", PAT \"2.04x\"", "Aug 2026, deck", "3.85x and 3.04x computed [E]", "MISSTATED"),
    (19, "\"completely debt-free\"", "Nov 2026, call", "Borrowings Rs 19.48 cr; net cash positive", "MISSTATED"),
    (20, "Debtors 60 days, inventory 90 days", "Nov 2026, CFO", "Receivables up Rs 66.26 cr in a year", "OPEN"),
    (21, "Capacity enough for Rs 1,200 cr by FY28", "Nov 2026, CFO", "Deck says Derabassi supports more than Rs 1,000 cr", "OPEN"),
    (22, "Two more CDMO customers to sign", "Aug and Nov 2026, CFO", "Not signed by Nov 2026", "OPEN")]
_cnt = {}
for *_, s_ in L:
    _cnt[s_] = _cnt.get(s_, 0) + 1
assert _cnt == {"DELIVERED": 2, "OPEN": 7, "CHANGED": 7, "ON TRACK": 1, "MISSED": 2, "MISSTATED": 3}, _cnt
order = ["DELIVERED", "ON TRACK", "OPEN", "CHANGED", "MISSED", "MISSTATED"]
score = C.hbars(order, [_cnt[k] for k in order], "Claims by status, 22 claims Jan to Nov 2026",
                colors=[C.GREEN, C.GREEN, C.GREY, C.SECOND, C.RED, C.RED], w=900, lab_w=110)
s11 = f"""{exhibit("Only 3 of 22 claims were met as stated; 7 are still open", score, src("ledger"),
         "Credibility score: 3 met of 15 that can be judged = 20% [E]. All three misstatements understated the company's own progress.")}
{table(["#", "Claim", "When and who", "What happened", "Status"], [[str(n), c_, w_, h_, chip(s_)] for n, c_, w_, h_, s_ in L],
       "std", caption="The claims ledger since Jan 2026", source=src("ledger", ("dq3", 18), ("dq1", 3), ("trq1", 6), ("trq1", 13), ("call", 1), ("call", 2), ("call", 6), ("deck", 23), ("caref", 8)))}
<p class="small">Scope: the Jan 2026 and Q3 FY26 decks and the Q1 and Q2 FY27 calls and decks. Calls of the merged business before Aug 2026 were not available, so this is the full ledger for the documents read, not the full record since the merger.</p>
<p>The pattern: the far-off revenue targets moved up (Rs 900 cr to Rs 1,000 cr; Rs 1,200 cr by FY29 to Rs 1,500 cr by FY30), while the near-term building blocks moved down (CDMO halved, registrations cut from 400+ to 333). Both missed items concern money raised from shareholders.</p>"""
section("s11", "B", "Claims ledger", "S11 | Claims checked", "Targets drift up while the building blocks drift down",
        "Management met 3 of 15 claims that can be judged (20%), changed 7, missed 2 and misstated 3; the misstatements were careless rather than flattering, but they lower trust in spoken numbers.",
        s11,
        "Use the near-term building blocks (CDMO revenue, registrations, Ibuprofen sales) as the real guidance, not the headline targets. Q3 FY27 settles rows 2, 3 and 12.")

# ================================================================= S12 guidance
h1v = h["op_rev"]
hh = C.bars(["H1 FY26", "H2 FY26", "H1 FY27", "H2 FY27 need"], [h1v[0], CALC["h2fy26"], h1v[1], h2n],
            "Half-year operating revenue and the H2 FY27 need, Rs cr", hatch={3}, colors=[C.GREY, C.GREY, C.PRIMARY, C.PRIMARY], w=520, h=230,
            notes={3: f"{pc(h2g, 0, True)} YoY"})
mg = C.lines(D["q"], [("Operating margin", D["q_opm"], C.PRIMARY, False)], "Quarterly operating margin Dec 2024 to Sep 2026, %",
             unit="%", dec=1, w=520, h=230, band=(18, 22, "Guided 18-22% from Q3 [G]"), ymin=-10, ymax=30, all_labels=True)
guid = table(["Metric", "Guidance", "Period", "Speaker and words", "Type"], [
    ["Revenue growth", "Above 50% (at least Rs 954 cr)", "FY27", "Deck: \"over 50%\"", "[G]"],
    ["Revenue", "Rs 1,000 cr", "FY27", "CFO, to an analyst's number: \"A minimum internal target\"", "Internal target"],
    ["Revenue", "Rs 1,500+ cr", "FY30", "Deck; CFO: \"we might revise this\"", "[G]"],
    ["Profit after tax", "About Rs 200+ cr", "FY30", "CFO, Aug 2026", "[G] spoken"],
    ["EBITDA margin", "Above 18% from Q3; 22% in Q3", "Q3 FY27", "CFO, Aug and Nov 2026", "[G]"],
    ["EBITDA margin", "20% vision; \"&gt;19%\" in the opening remarks", "FY27 to FY30", "CFO", "Conflict"],
    ["CDMO revenue", "Rs 100-130 cr extra; Rs 200-220 cr over two years", "FY27, FY28", "CFO, Nov 2026", "[G] (cut)"],
    ["Ibuprofen (Viatris)", "Rs 20 cr in Q3, Rs 20-25 cr in Q4", "H2 FY27", "CFO", "[G]"],
    ["Registrations", "333", "FY27", "Deck", "[G] (cut)"],
    ["Capex", "Rs 250 cr", "2 to 2.5 years", "CFO", "[G]"],
    ["FY28 revenue", "None given; \"Very difficult for me to comment\"", "FY28", "CFO", "No guidance"]],
    "std", caption="Current guidance", source=src(("deck", 3), ("deck", 16), ("deck", 23), ("call", 1), ("call", 3), ("call", 4), ("call", 6), ("call", 15), ("trq1", 8)))
must = table(["For this to hold", "H2 FY27 needs", "vs H2 FY26", "vs the Q2 run rate"], [
    ["Above 50% growth (Rs 954 cr)", f"Rs {f0(h2n)} cr, Rs {f1(DER['h2_need_q'])} cr a quarter", pc(h2g, 1, True), pc(CALC['h2_need_vs_q2'], 1, True)],
    ["Rs 1,000 cr internal target", f"Rs {f0(CALC['h2_1000'])} cr", pc(CALC['h2_1000_g'], 1, True), "-"],
    ["19% FY27 margin", f"{f1(DER['h2_margin_needed_19'] * 100)}% H2 margin", "-", "-"],
    ["20% margin on Rs 1,000 cr", f"{f1(CALC['h2_margin_1000_20'] * 100)}% H2 margin", "-", "-"]],
    "std", caption="What must be true in the second half [E]", source=src(("deck", 29), "model"))
s12 = f"""{duo(exhibit("The second half has to be the biggest half ever by a wide margin", hh, src(("deck", 29), "model"), "The hatched bar is our arithmetic [E], not a reported number."),
     exhibit("Margin has climbed into the guided band; Q3 must reach the top of it", mg, src("scr", ("call", 4)), "Screener basis, rounded to whole rupees crore; deck margin for Q2 is 18.02%."))}
{guid}
<p><b>Next quarter, in their words:</b> Ibuprofen "approximately Rs 20 crores" in Q3, and margin moving toward 22% [call p4]. No Q3 revenue number was given; we do not infer one.</p>
<p><b>Direction across calls:</b> FY27 revenue raised (Rs 900 cr to Rs 1,000 cr), long-range target raised and pushed out (Rs 1,200 cr FY29 to Rs 1,500 cr FY30), CDMO cut, registrations cut, margin bridge changed three times.</p>
{must}
<p>The Rs 1,500 cr FY30 goal needs only {pc(DER['base_growth_fy28_30'], 1)} a year after FY27 if FY27 lands at Rs {f0(DER['base_fy27'])} cr [E]. The long target is less demanding than the next six months.</p>"""
section("s12", "C", "Guidance", "S12 | Guidance and outlook", "The next six months carry the whole FY27 promise",
        f"Above 50% growth for FY27 needs second-half sales of Rs {f0(h2n)} cr, {pc(h2g, 1, True)} on last year and {pc(CALC['h2_need_vs_q2'], 1, True)} above the Q2 run rate; there is no formal FY28 guidance.",
        s12,
        f"Q3 FY27 sales of at least Rs {f0(DER['h2_need_q'])} cr with a margin near 22% keep guidance alive. Q3 sales near the Q2 level of about Rs 235 cr would put FY27 nearer our bear case of Rs {f0(DER['bear_fy27'])} cr.")

# ================================================================= S13 growth and triggers
bu = VAL["bottom_up_fy28"]
build = C.hbars(["Own brands, export", "Contract manufacturing", "Viatris Ibuprofen", "New registrations", "Domestic"],
                [bu["own_brand_run_rate"], bu["cmo_run_rate"], bu["viatris_ibuprofen"], bu["new_registrations"], bu["domestic_fy28"]],
                f"Bottom-up FY28 revenue build, Rs cr, total {f0(bu['total'])}; export lines at the Q2 run rate", w=900, lab_w=230, colors=[C.PRIMARY, C.SECOND, C.THIRD, C.FOURTH, C.GREY])
trig = table(["Trigger", "Timing", "What management said", "Rs impact", "Bias", "Strength", "Status"], [
    ["Q3 FY27 results", "Early Feb 2027", "22% margin; Ibuprofen Rs 20 cr", f"Rs {f0(DER['h2_need_q'])} cr sales test", "+/-", chip("STRONG"), chip("CONFIRMED")],
    ["Viatris Ibuprofen ramp", "Q3 to Q4 FY27", "Rs 20 cr, then Rs 20-25 cr a quarter", "About Rs 90 cr a year by FY28 [E]", "+", chip("STRONG"), chip("CONFIRMED")],
    ["Clarithromycin (Viatris)", "FY27 to FY28", "Validation done; site variation awaited", "USD 6 mn, about Rs 53 cr", "+", chip("MODERATE"), chip("PROBABLE")],
    ["Ezetimibe+Atorvastatin partner", "Running", "\"100+ Cr\"; Rs 25 cr Q1, Rs 58 cr Q2", "Largest single driver", "+/-", chip("MODERATE"), chip("CONFIRMED")],
    ["Macrogol (Manx, UK; Australia)", "FY28", "Rs 80 cr projected", "About Rs 80 cr", "+", chip("WEAK"), chip("PROBABLE")],
    ["Two new CDMO customers", "\"in the last quarter\"", "Unnamed; first mentioned Aug 2026", "Not sized", "+", chip("WEAK"), chip("OPEN")],
    ["Samba EU/PIC/S approval", "\"anytime next year\"", "Rs 45 cr upgrade; ANVISA visit held", "Second plant for regulated markets", "+", chip("WEAK"), chip("PROBABLE")],
    ["Synthimed stake sale", "\"a couple of years more\"", "Buyer diligence; tag-along right", "Rs 546-702 cr gross", "+", chip("WEAK"), chip("OPEN")],
    ["Warrant conversion", "By about Mar 2028", "56 lakh at Rs 196", f"Rs {f1(CALC['w2_to_come'])} cr cash; 6% more shares", "-", chip("STRONG"), chip("CONFIRMED")],
    ["FY28 guidance", "Q3 FY27 call", "\"Very difficult\"; to be given next call", "Sets the base for FY28", "+/-", chip("WEAK"), chip("OPEN")]],
    "std stack", caption="Trigger table", source=src(("call", 3), ("call", 4), ("call", 5), ("call", 6), ("call", 10), ("call", 13), ("deck", 21), ("dq3", 16), ("nsea", 1)))
absent = ul(["US filings: named as a direction only, no filing or date [deck p14].",
             "A new molecule in FY28: \"no new molecule\" [call p17]; FY28 grows on existing products.",
             "A signed Synthimed stake sale: none.",
             "The named second CDMO partner beyond Arrotex and Manx: none."])
s13 = f"""{exhibit("Our bottom-up FY28 build lands within 1% of management's path", build, src(("call", 5), ("call", 4), ("deck", 16), ("trq1", 5), "model"),
         f"Bottom-up total Rs {f1(bu['total'])} cr vs Rs {f1(bu['base_fy28'])} cr on the guided path [E]. Own brands and contract manufacturing are held at the Q2 run rate. Export Rs {f0(bu['export_fy28'])} cr. Capped by Derabassi capacity of about Rs 1,000-1,200 cr; above that needs Samba or new lines.")}
<p><b>Near term (next two quarters):</b> Q3 and Q4 FY27 results, Ibuprofen ramp, the 22% margin, and FY28 guidance on the Q3 call.<br>
<b>Long term (two to three years):</b> Clarithromycin, Macrogol, Samba approval, new CDMO customers, the 333 FY27 registrations earning from about FY29 (registration takes 1-1.5 years, revenue about 2 years [call p15]), and the stake sale.</p>
{trig}
<h4>Expected triggers that are absent</h4>
{absent}"""
section("s13", "C", "Growth and triggers", "S13 | Future growth and triggers", "Growth to FY28 rests on partners already signed; after that, on registrations not yet earning",
        "Bottom-up, FY28 revenue of about Rs 1,119 cr is reachable from today's run rates plus Viatris and new registrations; the confirmed triggers are near term, while the large long-term ones (Samba, new CDMO customers, the stake sale) are weak or open.",
        s13,
        "Watch Q3 for the Ibuprofen number and a margin near 22%. A named new CDMO customer or a Samba approval would be the first long-term trigger to move from weak to confirmed.")

# ================================================================= S14 peers
PEERS = [("Marksans Pharma", 13970, 3392, 784, 23, "+24%", 17.8, "25.0", 18.8, "UK, EU, US, Australia finished doses; own front end in UK"),
         ("Caplin Point", 19080, 2287, 797, 35, "+15%", 23.9, "28.7", 24.2, "Own brands in Latin America; US injectables"),
         ("Unichem", 3584, 2369, 237, 10, "+6%", 15.1, "30.2", 4.1, "US and EU generics; parent-owned"),
         ("Indoco", 2026, 1909, 169, 9, "+11%", 12.0, "n/a", 1.0, "India brands plus UK contract work"),
         ("Lincoln Pharma", 1042, 722, 100, 14, "+14%", 10.4, "10.8", 16.0, "India plus emerging-market exports"),
         ("Senores", 5414, 719, 209, 29, "+39%", 25.9, "40.6", 15.1, "US niche generics and contract work"),
         ("Akums", 12029, 4826, 668, 14, "+18%", 18.0, "31.9", 14.9, "India's largest contract maker"),
         ("Innova Captab", 6111, 1749, 259, 15, "+34%", 23.6, "39.7", 15.0, "Contract maker, India and exports"),
         ("Ind-Swift Labs", 3032, 753, 104, 14, "n/a", 29.2, "33.0", 4.9, "EU, Australia, Canada own registrations plus partner supply")]
_med = sorted(p_[6] for p_ in PEERS[:-1])
assert abs((_med[3] + _med[4]) / 2 - CALC["peer_med"]) < 0.06
pm = C.hbars([p_[0] for p_ in PEERS], [p_[6] for p_ in PEERS], "Market value / last 12 months operating profit, x", dec=1, unit="x", w=900, lab_w=130,
             highlight=len(PEERS) - 1)
s14 = f"""<h3>Who can do what</h3>
{table(["Company", "What it does", "How close to Ind-Swift"], [[p_[0], p_[9], c_] for p_, c_ in zip(PEERS[:-1], [
    "Closest: regulated-market finished doses, but with its own UK front end and 4x the scale",
    "Own-brand emerging markets at 35% margin; a model for what own brands can earn",
    "Similar size and low ROCE; the valuation anchor for our base 15x",
    "UK contract work overlaps; weaker margin",
    "Small exporter; the floor for a low-return maker",
    "Fast-growing contract and niche work; priced for growth",
    "Contract maker for India; scale player",
    "Contract maker; priced for growth"])], "std", caption="Peers: business comparison first", source=src("peers"))}
{exhibit("On last year's profit Ind-Swift looks expensive; on next year's guided profit it looks cheap", pm, src("peers"),
          f"Peer median {CALC['peer_med']}x. Ind-Swift's 29.2x uses a TTM operating profit of Rs 104 cr that still includes the weak FY26 quarters; on FY27 base EBITDA the core trades at {f1(VAL['reverse'][0]['x_fy27'])}x [E]. Market value / operating profit ignores each peer's own net cash or debt [E].")}
{table(["Company", "Operating margin, TTM", "Sales growth, TTM", "P/E", "ROCE"], [[p_[0], f"{p_[4]}%" + (" (Q2 FY27: 18%)" if p_[0] == "Ind-Swift Labs" else ""), p_[5], p_[7], f"{p_[8]}%"] for p_ in PEERS], "std", caption="Peers: margin, growth and returns", source=src("peers")[:-1] + ". Registrations and working-capital days for peers were not collected.")}
<p><b>Where it can compete:</b> regulated-market approvals (MHRA, TGA, Health Canada), a dossier library of 2,100+ filings, and a decade-long Viatris relationship. <b>Where it cannot:</b> scale, its own front end in Europe, and the US.</p>
<p><b>Which multiple fits:</b> peer-level margin but ROCE of 4.9%, three years of negative operating cash flow and two-molecule concentration argue for a discount to the {CALC['peer_med']}x median. We use 10x bear (Lincoln, Indoco), 15x base (Unichem), and 18x bull (the median, for a proven exporter that collects its cash).</p>"""
section("s14", "D", "Peers", "S14 | Peers", "A peer-level margin, but not yet peer-level returns or cash",
        f"Ind-Swift's 18% margin matches the peer group, but its 4.9% ROCE and negative cash flow do not; a discount to the {CALC['peer_med']}x peer median is earned until cash arrives.",
        s14,
        "Re-rating toward the median needs two things peers already show: positive operating cash flow and ROCE in double digits. Marksans is the template for what a regulated-market finished-dose exporter can become.")

# ================================================================= S15 reality vs optionality
proven_ps = (D["op_ttm"] * MULT + CALC["net_cash"] + CALC["w2_to_come"]) / SH
stake_ps = VAL["scenarios"]["Base"]["value"]["stake"]["net"] / SH
assert abs(proven_ps - 212) < 2, proven_ps
s15 = f"""{table(["Layer", "What", "Rs cr", "Status"], [
    ["Earning today", f"Last 12 months operating profit Rs {D['op_ttm']} cr; Q2 FY27 sales Rs 235 cr a quarter", f"{f0(D['sales_ttm'])} sales", chip("PROVEN")],
    ["Ramping", "Ezetimibe+Atorvastatin partner (Rs 58 cr in Q2), Viatris Ibuprofen (Rs 20 cr a quarter from Q3)", "About 320 a year at run rate [E]", chip("PARTLY PROVEN")],
    ["Announced", "Clarithromycin, Macrogol, Rs 1,000 cr FY27, 333 registrations, Samba approval", "53 + 80 + registrations", chip("UNPROVEN")],
    ["Idea", "Rs 1,500 cr by FY30, US entry, two unnamed CDMO customers", "Not sized", chip("UNPROVEN")],
    ["Balance sheet", "Net cash Rs 348 cr; warrant money Rs 82 cr to come", "430", chip("PROVEN")],
    ["Stake", "7.80% of Synthimed at management's Rs 8,000 cr, after tax and 25% discount", f"{f0(VAL['scenarios']['Base']['value']['stake']['net'])}", chip("UNPROVEN")]],
    "std stack", caption="Reality vs optionality, with rupees", source=src("scr", ("call", 4), ("call", 5), ("deck", 6), ("deck", 21), ("deck", 30), "model"))}
<p>What is proven, valued simply: last year's operating profit at our 15x base multiple plus net cash and warrant money is about <b>Rs {f0(proven_ps)} a share</b> [E]. The stake adds about Rs {f0(stake_ps)} if management's value is right. The price of Rs {f0(D['price'])} sits about Rs {f0(D['price'] - proven_ps - stake_ps)} above both, which is what the market pays today for the ramp continuing.</p>"""
section("s15", "D", "Reality vs optionality", "S15 | Reality vs optionality", "The price pays for the ramp continuing, not for the ideas",
        f"Proven earnings plus cash are worth about Rs {f0(proven_ps)} a share and the stake about Rs {f0(stake_ps)}; the remaining Rs {f0(D['price'] - proven_ps - stake_ps)} of the Rs {f0(D['price'])} price is a bet on the partner ramp holding, while the Rs 1,500 cr idea is barely priced.",
        s15,
        "Downside to about Rs 212 to 255 needs the ramp to stall, not collapse. Upside to our base needs only the guided FY27 and FY28 to be delivered in cash.")

# ================================================================= S16 causal chain
chain = flow([("Registrations and approvals", [f"MHRA, TGA, Health Canada site approvals; 540+ own registrations<br>{chip('PROVEN')}"], False),
              ("Partner launches", [f"Viatris Ibuprofen supplying; Ezetimibe+Atorvastatin Rs 58 cr in Q2<br>{chip('PROVEN')}"], False),
              ("Repeat orders turn into cash", [f"Receivables up Rs 66 cr, inventory up Rs 66 cr; operating cash flow negative 3 years<br>{chip('UNPROVEN')} <b>first unproven link</b>"], True),
              ("20% margin", [f"18.02% in Q2; 22% guided for Q3<br>{chip('PARTLY PROVEN')}"], False),
              ("Rs 1,500 cr by FY30", [f"Needs 16.3% a year after FY27<br>{chip('UNPROVEN')}"], False)], "cchain")
drv = table(["Driver", "Approval", "Launch", "Repeat orders", "Cash collected", "First unproven link"], [
    ["Own brands, export", chip("PROVEN"), chip("PROVEN"), chip("PROVEN"), chip("UNPROVEN"), "Cash collected"],
    ["Ezetimibe+Atorvastatin partner", chip("PROVEN"), chip("PROVEN"), chip("PARTLY PROVEN"), chip("UNPROVEN"), "Repeat orders (two quarters only)"],
    ["Viatris Ibuprofen", chip("PROVEN"), chip("PROVEN"), chip("UNPROVEN"), chip("UNPROVEN"), "Repeat orders"],
    ["Clarithromycin", chip("PARTLY PROVEN"), chip("UNPROVEN"), chip("UNPROVEN"), chip("UNPROVEN"), "Partner's site variation"],
    ["333 FY27 registrations", chip("PARTLY PROVEN"), chip("UNPROVEN"), chip("UNPROVEN"), chip("UNPROVEN"), "Revenue from about FY29"],
    ["Samba exports", chip("UNPROVEN"), chip("UNPROVEN"), chip("UNPROVEN"), chip("UNPROVEN"), "EU/PIC/S approval"],
    ["Domestic", chip("PROVEN"), chip("PROVEN"), chip("PROVEN"), chip("PROVEN"), "None; but sales fell 14.7% in FY26"]],
    "std stack", caption="The causal chain by driver", source=src(("deck", 7), ("deck", 8), ("deck", 30), ("call", 3), ("call", 5), ("call", 10), ("ar26", 93), "scr"))
s16 = f"""{exhibit("From approvals to Rs 1,500 cr, the chain breaks at cash", chain, src(("deck", 7), ("deck", 28), ("deck", 30), ("call", 4), "scr"))}
{drv}"""
section("s16", "D", "Causal chain", "S16 | The causal chain", "Approvals and launches are proven; turning repeat orders into cash is not",
        "Every growth driver clears approval and launch, but none has yet shown the last link, cash collected: receivables and inventory rose Rs 132 cr in a year and operating cash flow was negative for three years.",
        s16,
        "The one number that would prove the chain is a positive H2 FY27 operating cash flow with receivable days below 90. That arrives with the FY27 annual results, about late May 2027.")

# ================================================================= S17 financials
ocf_pat = C.grouped(D["years"], [("Profit after tax", D["pat"], C.GREY), ("Operating cash flow", D["ocf"], C.PRIMARY)],
                    "Profit after tax vs operating cash flow FY20 to FY26, Rs cr", w=900, h=260)
rd = C.lines(["Sep 2025", "Sep 2026"], [("Receivable days", CALC["rec_days"], C.PRIMARY, False)], "Receivable days", dec=0, w=520, h=230,
             band=(55, 65, "CFO target about 60 [G]"), ymin=0, ymax=120, all_labels=True)
wd = C.lines(["Sep 2025", "Sep 2026"], [("Working-capital days", CALC["nwc_days"], C.SECOND, False)], "Net working-capital days", dec=0, w=520, h=230,
             band=(80, 90, "85 days at Rs 1,500 cr [G]"), ymin=0, ymax=160, all_labels=True)
qoe = table(["Metric", "Value", "Reading", "Verdict"], [
    ["Operating margin H1 FY27", f"{f1(h['margin'][1])}% vs {f1(h['margin'][0])}%", "Operating leverage: employee cost fell from 20.9% to 16.2% of sales Q1 to Q2", chip("OK")],
    ["Raw material % of revenue", "46.06% Q2 vs 40.41% Q1 (deck basis)", "Rose as contract volume grew; the call's 45.15% uses another base", chip("WATCH")],
    ["R&D % of sales", "Not Disclosed in the deck", "AR FY26 R&D line not separately read", chip("NOT DISCLOSED")],
    ["Receivable days", f"{f0(CALC['rec_days'][1])} (target about 60)", "Flat at about 103 for a year", chip("WATCH")],
    ["Inventory days", f"{f0(CALC['inv_days'][1])} vs {f0(CALC['inv_days'][0])}", "Rising with launches", chip("WATCH")],
    ["Net working-capital days", f"{f0(CALC['nwc_days'][1])} vs {f0(CALC['nwc_days'][0])}", "Rs 485 cr needed at Rs 1,500 cr at today's days vs the CFO's Rs 350 cr", chip("RED")],
    ["Operating cash flow vs profit", f"OCF Rs {CALC['ocf_3y']} cr over FY24 to FY26", "Profit positive all three years", chip("RED")],
    ["Other income % of profit before tax", "Rs 36 cr in FY26, mostly treasury income", "Large but now separately shown; H1 FY27 margin is operating", chip("WATCH")],
    ["Fixed asset turnover", f"{f1(CALC['at_now'])}x", "Reasonable for a finished-dose maker", chip("OK")],
    ["ROCE (Screener)", "4.9%", "Diluted by cash and the stake; ex-cash ROCE not computable without a split of other assets", chip("WATCH")],
    ["Debt", f"Rs {D['debt_sep26']} cr gross; net cash Rs {f0(CALC['net_cash'])} cr", "Not a constraint", chip("OK")],
    ["Share count", "9,39,61,558 fully diluted vs 8,69,61,558 printed", "Data conflict; we use the higher count", chip("WATCH")]],
    "std", caption="Quality of earnings scorecard", source=src(("deck", 28), ("deck", 29), ("deck", 30), ("call", 2), ("call", 13), "scr", "model"))
fin = table(["Rs cr"] + D["years"], [
    ["Sales"] + [f0(v) for v in D["sales"]],
    ["Operating profit"] + [neg(v) for v in D["op"]],
    ["Other income"] + [f0(v) for v in D["oi"]],
    ["Profit after tax"] + [neg(v) for v in D["pat"]],
    ["Operating cash flow"] + [neg(v) for v in D["ocf"]],
    ["Free cash flow"] + [neg(v) for v in D["fcf"]],
    ["Debt"] + [f0(v) for v in D["debt"]]], "fin", caption="Seven years of numbers: two different companies", source=src("scr"))
s17 = f"""{fin}
<p class="small">FY24 and FY25 include gains of Rs 434 cr and Rs 292 cr from the API sale in other income; FY20 to FY24 sales are the old API-plus-formulation company.</p>
{exhibit("Profit has not become cash for three years", ocf_pat, src("scr"), "FY24 profit and cash include the sale year. The FY25 break separates the old company from the new one.")}
{duo(exhibit("Receivables are not falling toward the 60-day target", rd, src(("deck", 30), ("call", 13), "model"), "Receivables over annualised half-year sales [E]."),
     exhibit("Working capital is moving away from the 85-day target", wd, src(("deck", 30), ("call", 13), "model"), "Inventory plus receivables less payables [E]."))}
{qoe}"""
section("s17", "D", "Financials", "S17 | Financials and quality of earnings", "Good margins, poor cash: verdict WATCH, close to RED on cash",
        f"The H1 FY27 margin is real operating profit, but working capital rose to {f0(CALC['nwc_days'][1])} days and operating cash flow was Rs {CALC['ocf_3y']} cr over three years; quality of earnings is WATCH until a half year of positive operating cash flow.",
        s17,
        "The single test for the whole thesis sits here: H2 FY27 operating cash flow. Positive, with receivable days below 90, moves this to OK. Negative again moves it to RED.")

# ================================================================= S18 governance and filings
filings = table(["Date", "Filing", "Why it matters"], [
    [hd("2024-03-31"), "Merger of Ind-Swift Ltd effective; 45,15,495 shares issued", "The finished-dose business moved in"],
    ["Aug 2024", "Warrant issue 1: 2.60 cr at Rs 121 (Rs 314.60 cr)", "Rs 58.99 cr later lapsed"],
    ["Jan 2025", "Behra land bought with issue money", "Sold Aug 2026 at a loss"],
    [hd("2026-02-04"), "Q3 FY26 deck: Rs 1,200+ cr by FY29; CDMO Rs 200-220 cr", "Both later changed"],
    ["Aug 2026", "Q1 FY27 call and deck: Rs 900 cr FY27", "Raised in Nov"],
    [hd("2026-09-17"), "Warrant issue 2: 70 lakh at Rs 196 to Essix (promoter)", "New promoter money despite net cash"],
    [hd("2026-10-08"), "14 lakh warrants converted", "Share count conflict starts here"],
    [hd("2026-11-03"), "CARE monitoring reports on both issues", "No deviation; some end use not traceable"],
    [hd("2026-11-04"), "Q2 FY27 deck and call", "Rs 1,500 cr FY30; CDMO cut; 15.15% misstatement"]],
    "std", caption="Material filings in date order", source=src(("ar26", 40), ("caref", 4), ("caref", 10), "dq3", "dq1", "nsea", "nsec", "caref", "careq2", "deck"))
rp = table(["Item", "FY26", "FY25"], [
    ["Purchases from promoter-linked entities", "14.70", "3.44"], ["Sales to promoter-linked entities", "10.60", "4.26"],
    ["Salary to relatives", "5.73", "-"], ["Investment in Essix shares", "28.88", "-"],
    ["Loans and advances given (flow)", "25.17", "11.00"], ["Debtors, related parties", "12.99", "6.73"],
    ["SFRE society loan, no repayment terms", "62.89", "-"]], "std", caption="Related parties, Rs cr", source=src(("ar26", 68), ("ar26", 92)))
treas = table(["Holding", "Rs cr"], [["Khandelwal (OCRPS)", "95.00"], ["Fortune", "72.48"], ["Ashok (NCDs)", "36.50"], ["Synthimed CCDs (the stake)", "32.00"],
                                     ["Essix Biosciences (promoter)", "28.85"], ["ISLL ME", "27.46"], ["IRF2", "18.04"], [("Total unquoted", "bold"), ("318.55", "bold")],
                                     ["Quoted small caps", "11.90"]], "std", caption="Where the treasury money sits", source=src(("ar26", 80), ("ar26", 81)))
CONF = [("Q2 growth", "15.15% on the call", "50.16% computed"), ("Q1 multiples", "2.85x EBITDA, 2.04x PAT", "3.85x and 3.04x"),
        ("Registrations", "900+ held, 540+ own (deck)", "950 and 520 (call)"), ("Synthimed value", "Rs 8,000-9,000 cr (deck, AR)", "Rs 7,000-8,000 cr (call)"),
        ("Capacity", "More than Rs 1,000 cr (deck)", "Rs 1,200 cr by FY28 (CFO)"), ("Utilisation", "70-75% at Derabassi", "The same 70-75% at Samba"),
        ("Share count", "8,69,61,558 printed after Oct", "8,83,61,558 inferred"), ("Conversion filing", "Counts move 2.5 lakh", "14 lakh converted"),
        ("Essix conversion", "51 lakh (chairman's letter)", "80 lakh (notes)"), ("Related-party loans", "Rs 10.65 cr (loans note)", "Rs 25.20 cr (note 93)"),
        ("Debt", "\"completely debt-free\"", "Borrowings Rs 19.48 cr"), ("Export split", "69:31", "68:32"),
        ("FY26 revenue", "Rs 635.89 cr (deck)", "Rs 649 cr (Screener), Rs 612.64 cr (standalone AR)"), ("FY24 share capital", "Rs 59 cr (Screener)", "Rs 62.7 cr implied"),
        ("Raw material Q2", "45.15% (call)", "46.06% on deck revenue; plus margin \"&gt;19%\" vs 20% and CDMO Rs 65 cr vs 58")]
assert len(CONF) == 15
s18 = f"""{filings}
<h3>Promoters, auditor and rating</h3>
<p>Promoter holding is 42.93% (Sep 2026), about 43.8% after the October conversion and 47.2% if all warrants convert [E]. No pledge disclosure was found; SAST filings were not queried.
The auditor, Rattan Kaur &amp; Associates, gave an unmodified opinion with two emphasis-of-matter items, for a fee of Rs 4 lakh. Rs 11.01 cr of old balances were written off. A Rs 66.34 cr sales-tax demand is a contingent liability, and Rs 16 cr of deposits are pledged against it.
The only credit rating read is CARE's Mar 2024 rationale, before the sale; no current rating was found in the documents read.</p>
{duo(rp, treas)}
<p>The CSR schedule shows Rs 2.40 cr as an "unspent" entry, and some offices are held in the chairman's name [AR26]. Neither is large; both are the kind of detail a cleaner company would not have.</p>
{table(["#", "Item", "One source says", "Another says"], [[str(i + 1), a_, b_, c_] for i, (a_, b_, c_) in enumerate(CONF)], "std",
       caption="Fifteen data conflicts we found and how we handled them", source=src("deck", "call", "trq1", "dq1", "ar26", "nsec", "scr"))}
<p class="small">Handling: deck tables over spoken figures; the higher share count; deck operating revenue (Rs 635.89 cr) as the FY26 base; the conservative stake value in the bear case.</p>"""
section("s18", "D", "Governance", "S18 | Governance and filings", "Clean audit opinion, untidy disclosure, and Rs 319 cr in unquoted instruments",
        "Nothing in the filings is a hard red flag, but Rs 319 cr of the treasury book is unquoted and partly promoter-linked, a Rs 62.89 cr loan has no terms, the audit fee is Rs 4 lakh, and we found 15 data conflicts across the company's own documents.",
        s18,
        "We do not count the treasury book in value beyond net cash. A clear disclosure of the SFRE loan terms and a sale of the promoter-linked holdings would remove most of the governance discount.")

# ================================================================= S19 risks
def _fv(k):
    return FRAG[k]["value_ps"]


def imp(dE):
    return ps(dE)


eu_rev = bu["export_fy28"] * D["geo"]["Europe"] / 100
r_partner = imp(-83 * ASM["Base"]["margin"][1])
r_h2 = imp(ROWS["Bear"][1]["ebitda"] - B28["ebitda"])
r_eu = imp(-0.05 * eu_rev)
r_syn = imp(-10)
RISK = [
    ("R1 Second half misses", f"FY27 lands near our bear Rs {f0(DER['bear_fy27'])} cr and FY28 EBITDA near Rs {f0(ROWS['Bear'][1]['ebitda'])} cr", f"About Rs {f0(-r_h2)} a share at 15x [E]", f"Q3 FY27 sales below Rs 250 cr"),
    ("R2 Profit stays in receivables", "Working capital stays at 118 days; Rs 485 cr needed at Rs 1,500 cr vs Rs 350 cr", f"About Rs {f0(base_v - _fv('bear_wc_days'))} a share; more via the multiple", "Receivable days above 110, or FY27 operating cash flow negative"),
    ("R3 Partner molecule halves", "The Ezetimibe+Atorvastatin partner cuts volume by half (Rs 83 cr a year)", f"About Rs {f0(-r_partner)} a share at the 20% margin [E]; more at contribution margin", "Q3 or Q4 partner sales below Rs 40 cr a quarter"),
    ("R4 European price cut", f"5% price cut on European exports (about Rs {f0(eu_rev)} cr in FY28)", f"About Rs {f0(-r_eu)} a share [E]", "Gross margin on exports below 50%"),
    ("R5 Stake worth nothing to us", "No sale, no mark, PE owner controls timing", f"Rs {f0(base_v - _fv('no_stake'))} a share", "No sale by FY29 or a down-round"),
    ("R6 A lower multiple", "The market pays 12x, not 15x, for a concentrated contract maker", f"Rs {f0(base_v - _fv('multiple_12'))} a share", "No re-rating after two good quarters"),
    ("R7 Synthimed raises API prices", "10% higher prices on Rs 100 cr of purchases", f"About Rs {f0(-r_syn)} a share [E]", "Raw material above 48% of sales"),
    ("R8 Governance turns RED", "Qualified audit, pledge, CARE deviation or an H2 miss", "Caps the readout at FAIR", "Any of the four in a filing")]
rcards = '<div class="risks">' + "".join(f'<div class="risk"><p class="rid">{a_}</p><p>{b_}</p><p><b>Impact:</b> {c_}</p><p class="thr"><b>Signal:</b> {d_}</p></div>' for a_, b_, c_, d_ in RISK) + "</div>"
anti = ul([
    f"Profit has not become cash: operating cash flow Rs {CALC['ocf_3y']} cr over three years; inventory plus receivables up Rs {f1(CALC['inv_rec_up'])} cr in a year, more than twice H1 profit of Rs {f1(h['pat'][1])} cr.",
    f"Growth is narrow: one partner molecule was Rs 83 cr of H1 sales; two molecules were {pc(CALC['ator2_share'])} of FY26 sales; new customers gave 72-81% of the H1 increase.",
    "Guidance keeps moving: 7 of 22 claims changed; CDMO for FY27 halved between Aug and Nov 2026.",
    f"About {pc(cs_share)} of the market value is cash and a stake valued by management, carried at Rs 32 cr.",
    "The cash is not obviously the minorities': Rs 319 cr in unquoted instruments, a loan without terms, and shares of the promoter entity that funds the company.",
    "More dilution is coming even with net cash: a promoter warrant issue for a plan called self-funded.",
    f"The price already assumes delivery: at the bear FY27 EBITDA of Rs {f0(ROWS['Bear'][0]['ebitda'])} cr, the core trades at {f1(CALC['core_ev'] / ROWS['Bear'][0]['ebitda'])}x a profit not yet shown in cash."])
bvr = table(["Bull claim", "Best counter-evidence", "Evidence favours"], [
    ["Margin went from 5.5% to 18.0% in a half year", "Raw material share rose Q1 to Q2; leverage came from flat staff cost", "Bull"],
    ["Approvals and 540+ registrations take years to copy", "How many earn revenue is Not Disclosed", "Bull"],
    ["Viatris is a 10-year partner with exclusive supply", "Viatris drives volume and price; contract terms Not Disclosed", "Even"],
    ["Cash and stake cover the downside", "Stake carried at Rs 32 cr; treasury partly promoter-linked", "Bear"],
    ["Core priced at 11.4x guided EBITDA vs 17.9x peers", "Peers convert profit to cash; Ind-Swift has not", "Bear"],
    ["Promoter is buying at Rs 196", "Promoter-linked money flows both ways", "Even"]], "std", caption="Bull claim vs rebuttal", source=src("ledger", ("deck", 14), ("deck", 28), ("ar26", 80), "peers"))
s19 = f"""<h3>The anti-thesis, argued as a sceptic would</h3>
{anti}
<p><b>If the stock halves in two years,</b> the most likely cause is all three together: H2 FY27 at the Q2 run rate, a fourth year of negative operating cash flow, and no Synthimed sale.</p>
{bvr}
<h3>Risk cards, ranked</h3>
{rcards}
<p class="src">{src("model", ("call", 5), ("call", 13), ("call", 14), ("deck", 20))} Impacts use Rs {f1(ps(1))} a share per Rs 1 cr of FY28 EBITDA at 15x [E]. The bear case uses R1, R2, R5 and R6.</p>
<h3>What would change our mind</h3>
<p><b>Kills the anti-thesis:</b> H2 FY27 sales of Rs 533 cr or more, positive H2 operating cash flow, receivable days below 90, and a named new CDMO customer.<br>
<b>Kills the thesis:</b> Q3 sales below Rs 250 cr, partner molecule sales falling, receivable days above 110, or a RED governance trigger.</p>"""
section("s19", "E", "Risks", "S19 | Risks and anti-thesis", "The case against is about cash and concentration, not about the margin",
        "The strongest case against is that profit is not yet cash and growth rests on one partner molecule; the largest single risk is a second-half miss, worth about Rs " + f0(-r_h2) + " a share.",
        s19,
        "Each risk card has a number to watch. Two of them, Q3 sales and receivable days, arrive within three months and decide most of the case.")

# ================================================================= S20 valuation and verdict
bv = VAL["scenarios"]["Base"]["value"]
wf = C.waterfall([("Core business, 15x FY28", bv["core_ev"], "up"), ("Net cash, Mar 2027", bv["net_cash_mar27"], "up"), ("Warrant money", bv["warrant_cash"], "up"),
                  ("Stake after tax and discount", bv["stake_counted"], "up"), ("Equity value, Mar 2027", bv["equity_mar27"], "total")],
                 "Sum of the parts, base case, Rs cr", dec=0, w=900, h=280)
vr = C.value_range([("Bear", bear_v, C.RED, "10x, stake at half"), ("12x multiple", _fv("multiple_12"), C.GREY, "base, lower multiple"),
                    ("No stake", _fv("no_stake"), C.GREY, "base without the stake"), ("Base", base_v, C.PRIMARY, "guidance, 15x"),
                    ("Bull", bull_v, C.GREEN, "25% CAGR to FY30, 18x")], D["price"], "Value per share by case vs the price", w=900, lo=150, hi=550)
sg = VAL["sensitivity"]
sens = table(["FY28 EBITDA, Rs cr"] + [f"{m:g}x" for m in sg["multiples"]],
             [[f0(r_["fy28_ebitda"])] + [((f0(v_), "bold") if (abs(r_["fy28_ebitda"] - 221.84) < 0.1 and m_ == 15) else (f0(v_), "neg" if v_ < D["price"] else "")) for m_, v_ in zip(sg["multiples"], r_["values"])] for r_ in sg["rows"]],
             "std", caption="Value per share by FY28 EBITDA and multiple (price Rs 349; below price in red)", source=src("model"))
scen = table(["", "Bear", "Base", "Bull"], [
    ["FY27 revenue, Rs cr", f0(ASM["Bear"]["fy27_revenue"]), f0(ASM["Base"]["fy27_revenue"]), f0(ASM["Bull"]["fy27_revenue"])],
    ["Margin", "17.5%", "19% to 20%", "19% to 21%"],
    ["Growth FY28 to FY30", "12%", pc(DER["base_growth_fy28_30"], 1), pc(DER["bull_growth_fy28_30"], 1)],
    ["Working-capital days", "118", "110 to 85", "110 to 85"],
    ["FY28 EBITDA, Rs cr", f0(ROWS["Bear"][1]["ebitda"]), f0(B28["ebitda"]), f0(ROWS["Bull"][1]["ebitda"])],
    ["Multiple", "10x", "15x", "18x"],
    ["Stake (company value, discount)", "Rs 7,000 cr, 50%", "Rs 8,000 cr, 25%", "Rs 9,000 cr, 15%"],
    [("Value per share", "bold"), (f"Rs {f0(bear_v)}", "bold"), (f"Rs {f0(base_v)}", "bold"), (f"Rs {f0(bull_v)}", "bold")],
    ["vs price", (pc(V["Bear"]["vs_price"], 0, True), "neg"), pc(V["Base"]["vs_price"], 0, True), pc(V["Bull"]["vs_price"], 0, True)]],
    "std", caption="Bear, base and bull side by side", source=src("model"))
ST = VAL["skill_tables"]


def skill_tbl(name):
    t = ST[name]
    cols = t["hist"] + t["proj"]
    n0 = lambda v: "-" if v is None else f1(v)
    p1 = lambda v: "-" if v is None else pc(v, 1)
    rs = lambda v: "-" if v is None else f0(v)
    eps = lambda v: "-" if v is None else f"{v:.2f}"
    def neg(v, txt):
        return (txt, "neg") if (v is not None and v < 0) else txt
    def row(label, key, fmt, bold=False):
        cells = [neg(c.get(key), fmt(c.get(key))) for c in cols]
        if bold:
            cells = [(c, "bold") if isinstance(c, str) else (c[0], c[1] + " bold") for c in cells]
        return [(label, "bold") if bold else label] + cells
    rows = [row("Sales", "sales", n0), row("Expenses", "expenses", n0), row("Operating profit", "op", n0), row("OPM", "opm", p1),
            row("Other income", "other_income", n0), row("Interest", "interest", n0), row("Depreciation", "depreciation", n0),
            row("Profit before tax", "pbt", n0), row("Tax rate", "tax_pct", p1), row("Net profit", "pat", n0, True),
            row("EPS pre-dilution, Rs", "eps_pre", eps), row("EPS post-dilution, Rs", "eps_post", eps),
            row("PAT growth", "pat_growth", p1), row("PAT margin", "pat_margin", p1), row("Net cash at year end", "net_cash_end", n0),
            row("Target price pre-dilution, Rs", "tp_pre", rs), row("Target price post-dilution, Rs", "tp_post", rs, True),
            row(f"Return vs CMP Rs {f0(D['price'])}", "return_post", lambda v: "-" if v is None else pc(v, 0, True)),
            row("CAGR vs CMP to 31 Mar", "cagr_post", lambda v: "-" if v is None else pc(v, 1, True))]
    return table(["Rs cr"] + [c["year"] for c in cols], rows, "fin",
                 caption=f"{name}: {t['multiple']:g}x EV/EBITDA, held flat FY27E to FY30E (Screener layout; FY25A and FY26A consolidated actuals)",
                 source=src("model", "scr"))


skill_note = ("<p>Target price at 31 Mar of each year = multiple x that year's EBITDA + net cash at that year end (rolled forward by free cash flow) "
              "+ the stake after tax and discount [+ Rs 82.32 cr of warrant money, post-dilution only], divided by 8,83,61,558 shares before dilution "
              "or 9,39,61,558 after. These are not discounted; CAGR runs from 9 Nov 2026, so FY27E (under five months away) shows no CAGR. "
              "FY27E growth is measured from the deck's Rs 635.89 cr operating revenue, not Screener's Rs 649 cr.</p>")
skill_caveats = """<h3>Key assumptions and caveats</h3>
<ul class="small">
<li>Guided by management: FY27 revenue +50% (Rs 953.84 cr) at about 19% EBITDA margin [deck p3, call p4]; Rs 1,500 cr+ revenue by FY30 at a 20-25% CAGR [deck p23]; working capital about Rs 350 cr at Rs 1,500 cr [call p13]; Rs 250 cr capex [call p1-p2].</li>
<li>Estimated by us [E]: every bear line; the bull's top-of-range 25% CAGR and 20.5-21% margins; the base path for FY28-FY29; other income Rs 30 cr and interest Rs 4 cr a year (H1 FY27 x 2); depreciation (Rs 30.7 cr plus 8% of new capex); tax 25.17% (section 115BAA).</li>
<li>Bull triggers already disclosed: Viatris Clarithromycin supply of USD 6.0 mn [deck p21]; 100-150 registrations planned [call p12]; two customers expected to sign in Q4 [call p13-p14]; staff cost down from 20.93% to 16.23% of revenue [deck p28].</li>
<li>Bull FY30 revenue of Rs 1,552 cr is above the Rs 1,000-1,200 cr current plants carry; it needs Samba exports after EU/PIC/S approval and the full Rs 250 cr capex on time [deck p8, call p3, call p8, E].</li>
<li>Dilution: 56,00,000 warrants (issue price Rs 196, Rs 147 a warrant still to pay, Rs 82.32 cr in all) are assumed converted, giving 9,39,61,558 shares; pre-dilution uses 8,83,61,558 shares after the 8 Oct 2026 conversion (inferred from filings; the printed count is 8,69,61,558).</li>
<li>The multiple is held flat across years in each case (10x, 15x, 18x). That is a simplification: a real bear case usually also compresses the multiple, and a bull case expands it.</li>
<li>The headline values (Rs {bear} / {base} / {bull}) apply the same multiple to FY28 EBITDA at 31 Mar 2027 and discount to today at 13%; the year-end target prices above are undiscounted, so the two do not match.</li>
<li>Not investment advice. We are not licensed financial advisors. These are scenario bands, not forecasts.</li>
</ul>""".format(bear=f0(bear_v), base=f0(base_v), bull=f0(bull_v))
Q15 = [
    "FY26 base: Rs 635.89 cr operating revenue; pre-merger formulation accounts Not Disclosed.",
    "Q2 growth was 50.16%, not 15.15%; the third arithmetic slip in two quarters, all understating.",
    "One partner molecule (Rs 83 cr) and new customers (Rs 80-90 cr) explain most of the Rs 111 cr H1 increase.",
    "Viatris: exclusive worldwide supply at a transfer price; length, minimums and exit terms Not Disclosed.",
    "Partners: Viatris, Arrotex (Australia), Manx (UK); the two hoped-for customers are unnamed.",
    "Registrations earning revenue: Not Disclosed; about Rs 0.93 cr a year per own registration on average [E].",
    "18% margin came from operating leverage on staff cost; line margins Not Disclosed.",
    "Plants carry about Rs 1,000-1,200 cr; Rs 1,500 cr needs Samba and the Rs 250 cr capex.",
    "Operating cash flow negative on rising receivables and inventory; working capital falls only if collections show in H2.",
    f"Equity raised Rs {f1(CALC['w1_raised'])} cr (issue 1) plus Rs 137.20 cr (issue 2, Rs {f1(CALC['w2_to_come'])} cr to come).",
    "Stake: Rs 546-702 cr gross, carried at Rs 32 cr; no sale date.",
    "About Rs 100 cr of Rs 400 cr purchases from Synthimed; not a related party, terms Not Disclosed.",
    "Rs 1,500 cr by FY30 needs only 16.3% a year after a 50% FY27; FY28 guidance not given.",
    "Promoter holding up to 42.93%; steep pay rises; pledge Not Disclosed.",
    f"Peers median {CALC['peer_med']}x; a discount is earned: 10x, 15x and 18x."]
assert len(Q15) == 15
asg = table(["Input", "Grounded or assumed", "Source"], [
    ["FY27 revenue Rs 954 cr, 19% margin", "Grounded in guidance", "[deck p3], [call p4]"],
    ["Rs 1,500 cr by FY30 at 20%", "Grounded in guidance", "[deck p23]"],
    ["Working capital falls to 85 days", "Grounded in a CFO statement, not yet shown", "[call p13]"],
    ["15x base multiple", "Assumed, anchored to Unichem and the peer median", "S14"],
    ["Stake at Rs 8,000 cr less tax and 25% discount", "Management value; tax and discount assumed", "[deck p6], [E]"],
    ["13% cost of equity", "Assumed", "model"],
    ["Treasury book counted at zero beyond net cash", "Our choice, conservative", "S18"],
    ["9,39,61,558 shares", "Inferred from filings; higher of two counts", "[NSE-C], [deck p30]"]], "std", caption="Assumed vs grounded")
watch = table(["Date", "Signal", "Confirms the base", "Breaks it"], [
    ["Early Feb 2027", "Q3 FY27 results", f"Sales of Rs {f0(DER['h2_need_q'])} cr or more; margin near 22%", "Sales below Rs 250 cr"],
    ["Feb 2027 call", "FY28 guidance", "Rs 1,100 cr or more", "No number again"],
    ["Late May 2027", "FY27 results and cash flow", "Positive H2 operating cash flow; receivable days below 90", "A fourth negative year"],
    ["During 2027", "Samba EU/PIC/S; new CDMO customers", "Approval; a named customer", "Delay past FY27"],
    ["By about Mar 2028", "Warrant conversion", "56 lakh converted at Rs 196", "Lapse, as in issue 1"]], "std", caption="Dated signals to watch")
s20 = f"""{scen}
<h3>Year by year: bear, base and bull</h3>
{skill_note}
{skill_tbl("Bear")}
{skill_tbl("Base")}
{skill_tbl("Bull")}
{skill_caveats}
{exhibit("The core business is about 80% of base value; cash and the stake are the rest", wf, src("model", ("deck", 30), ("deck", 6)),
         f"Discounted to today at 13% for {VAL['assumptions']['years_to_value_date']:.2f} years (9 Nov 2026 to 31 Mar 2027) and divided by 9,39,61,558 shares: Rs {f0(base_v)} a share [E].")}
{exhibit("The price sits between the bear case and the cases without the stake or at a lower multiple", vr, src("model"))}
{sens}
<p>Reverse check: at Rs {f0(D['price'])}, the market pays {f1(VAL['reverse'][0]['x_fy27'])}x FY27 and {f1(VAL['reverse'][0]['x_fy28'])}x FY28 base EBITDA for the core business [E]. Cross-checks on the base: FY28 P/E {f1(VAL['cross_checks']['pe_fy28_base'])}x; FY28 free cash flow yield {pc(VAL['cross_checks']['fcf_yield_fy28_base'], 1)}.</p>
<h3>Verdict</h3>
<p>Valuation readout: {chip(READOUT)}. Base value Rs {f0(base_v)} is {pc(V['Base']['vs_price'], 0, True)} above the price, just over the 20% line. Without the stake it falls to Rs {f0(_fv('no_stake'))}, which is FAIR. Management: {chip('WATCH')}. This is a company study, not a buy or sell call.</p>
<h3>The 15 questions, one line each</h3>
<ol class="small">{''.join(f'<li>{q}</li>' for q in Q15)}</ol>
{asg}
{watch}"""
section("s20", "E", "Valuation", "S20 | Valuation and verdict", f"Rs {f0(bear_v)} to Rs {f0(bull_v)}, base Rs {f0(base_v)}: attractive only if guidance turns into cash",
        f"On management's own guidance the shares are worth about Rs {f0(base_v)} ({pc(V['Base']['vs_price'], 0, True)}), so the readout is ATTRACTIVE by a thin margin; the bear case of Rs {f0(bear_v)} ({pc(V['Bear']['vs_price'], 0, True)}) is what happens if the second half and the cash do not arrive.",
        s20,
        "The asymmetry is modest: about +22% to the base and -29% to the bear. The Feb and May 2027 results move value more than any other input, so they matter more than today's price.")

# ================================================================= appendix
srcs = []
for k, (name, url) in SRC.items():
    srcs.append(f'<li><a href="{url}">{name}</a></li>' if url else f"<li>{name}</li>")
dil = table(["Key number", "Label", "Where"], [
    ["Operating revenue H1 FY27 Rs 420.97 cr", "Disclosed", "[deck p3], [deck p29]"], ["Net cash Rs 348.36 cr", "Inferred from disclosed balance sheet", "[deck p30]"],
    ["Stake value Rs 624 cr", "Inferred from management's company value", "[deck p6]"], ["Stake carrying value Rs 32 cr", "Disclosed", "[AR26 p80]"],
    ["Partner molecule Rs 25 cr / Rs 58 cr", "Disclosed (spoken)", "[Q1 call p14], [call p5]"], ["New-customer revenue Rs 80-90 cr", "Disclosed (spoken)", "[call p11]"],
    ["Registrations earning revenue", "Not Disclosed", "[call p11]"], ["Viatris contract terms", "Not Disclosed", "[call p16]"],
    ["Synthimed purchase terms", "Not Disclosed", "[AR26 p92]"], ["Promoter pledge", "Not Disclosed", "AR FY26, AR FY25"],
    ["Diluted shares 9,39,61,558", "Inferred", "[NSE-C], [deck p30]"], ["H2 need Rs 533 cr", "Inferred [E]", "model"],
    ["Tax on a stake sale 14.95%", "Assumed", "model"], ["Pre-merger formulation accounts", "Not Disclosed", "not collected"]], "std", caption="Disclosed, inferred and not disclosed")
app = f"""<h3>Sources</h3><ol class="srcs">{''.join(srcs)}</ol>
<p class="small">Page links open the filed PDF at the physical page cited. The Q2 FY27 call text is a machine transcript supplied by the reader; BSE carries the audio. All [E] figures are recomputed in model/valuation.py.</p>
{dil}
<h3>Disclaimer</h3>
<p class="small">This study is research for learning, not investment advice. The author is not a licensed financial advisor. It makes no buy, sell or hold recommendation and does not consider any reader's circumstances. Figures may contain errors; check filings before acting.</p>"""
SECTIONS.append(("appendix", "Z", "Sources", "Appendix | Sources", "Every source, and what is disclosed vs inferred",
                 f'<p class="answer">Every number traces to a filing, a call, Screener, or our model.</p>{app}'))
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
@media screen and (max-width:600px){
 .t.stack thead{display:none}
 .t.stack,.t.stack tbody,.t.stack tr,.t.stack td{display:block;width:100%}
 .t.stack tr{border-bottom:1px solid var(--line);padding:6px 0}
 .t.stack td{border:0;padding:2px 0;white-space:normal;text-align:left}
 .t.stack td.l{font-weight:600}
 .t.stack td:not(.l)::before{content:attr(data-label) ": ";color:var(--muted);font-weight:400}
}
@page:first{@top-left{content:none}@top-right{content:none}}
@page{size:A4;margin:40pt 36pt 40pt;@top-left{content:"IND-SWIFT LABORATORIES | NSE: INDSWFTLAB | Company study";font:bold 7.5pt Calibri,Carlito,sans-serif;color:#0E5A63}@top-right{content:"9 November 2026";font:7.5pt Calibri,Carlito,sans-serif;color:#0E5A63}@bottom-left{content:"Ind-Swift Laboratories | Company study | Not investment advice";font:7.5pt Calibri,Carlito,sans-serif;color:#5F6873}@bottom-right{content:counter(page) " / " counter(pages);font:7.5pt Calibri,Carlito,sans-serif;color:#5F6873}}
@media print{
 body{background:#fff;font-size:10pt;line-height:1.3}
 .wrap{display:block;padding:0}.side,.topnav{display:none}
 .page{margin:0 0 18pt;border:0;break-before:auto}
 .page:first-child,#appendix{break-before:page}
 .band,.rule,.kicker,h2,.answer,.mfy{break-after:avoid}
 .ex,.means,.mfy,.duo,.risk,.answer,.keep,.disc{break-inside:avoid}
 .foot{display:none}
 .page:not(#s1) .band,.page:not(#s1) .rule{display:none}
 .page:not(#s1) .inner{border-top:1.5pt solid #0E5A63;padding-top:6pt}
 .inner{padding:8pt 0 0}.band{padding:5pt 8pt;font-size:8.5pt}.foot{margin:6pt 0 0;font-size:7.5pt}
 h2{font-size:14pt}h3{font-size:11.5pt}h4{font-size:10.5pt}.ctitle{font-size:22pt}.csub{font-size:13pt}
 .answer{font-size:10.5pt}.lede{font-size:11pt}
 .srcs{columns:2;column-gap:18pt}.srcs li{break-inside:avoid}
 .t{font-size:8.5pt}.t.fin td,.t.fin th{font-size:8pt}.t.kv td{font-size:8.5pt}
 .src,.tiny,.foot{font-size:7.5pt}.xnote,.small{font-size:8.5pt}
 figcaption{font-size:10pt}
 .t th{border-bottom-width:.6pt}.t td{border-bottom-width:.35pt}
 .cover{grid-template-columns:minmax(0,1fr) 190pt}
 tr,.card,.risk,.plant,.fb{break-inside:avoid}
 h3,h4,figcaption{break-after:avoid}
 a{color:inherit;text-decoration:none}
}
.plants.p2{grid-template-columns:repeat(2,minmax(0,1fr))}
.ba{display:grid;grid-template-columns:minmax(0,1fr) 40px minmax(0,1fr);gap:10px;align-items:stretch}
.ba .farrow{align-self:center;text-align:center}
.cchain .fb{min-height:86px}
.big{font-size:22px;font-weight:700;color:var(--teal);margin:0}
@media screen and (max-width:820px){.plants.p2,.ba{grid-template-columns:minmax(0,1fr)}.ba .farrow{transform:rotate(90deg)}}
"""


_VOID = {"br", "img", "hr", "meta", "input", "col", "wbr", "source"}  # HTML void tags; SVG tags close explicitly or with />


def _split_top(html, n):
    """Return (first n top-level elements, rest) of an HTML fragment; used to keep a section's opening together in print."""
    depth, count = 0, 0
    for m in re.finditer(r"<(/?)([a-zA-Z0-9]+)[^>]*?(/?)>", html):
        close, tag, selfclose = m.group(1), m.group(2).lower(), m.group(3)
        if close:
            depth -= 1
            if depth == 0:
                count += 1
                if count == n:
                    return html[:m.end()], html[m.end():]
        elif not selfclose and tag not in _VOID:
            depth += 1
    return html, ""


def render():
    total = len(SECTIONS)
    side = ['<nav class="side" aria-label="Contents"><p class="brand">Ind-Swift Laboratories</p><p class="sub">Company study, 9 Nov 2026</p>']
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
        band = ('<div class="band"><span><b>IND-SWIFT LABORATORIES</b> &nbsp;|&nbsp; NSE: INDSWFTLAB &nbsp;|&nbsp; Company study</span>'
                '<span>9 November 2026</span></div><div class="rule"></div>')
        if sid == "s1":
            head = ('<p class="kicker">NSE: INDSWFTLAB &nbsp;|&nbsp; BSE: 532305 &nbsp;|&nbsp; Finished-dose exports</p>'
                    '<h1 class="ctitle">Ind-Swift Laboratories Ltd</h1>'
                    '<p class="csub">A real step-up in sales, not yet a proven business, sitting on cash and a stake</p>'
                    '<p class="cmeta">Company study, not a recommendation &nbsp;|&nbsp; Data as of 9 November 2026 &nbsp;|&nbsp; Rs crore unless stated &nbsp;|&nbsp; Per-share figures on 9,39,61,558 fully diluted shares</p>')
            inner = head + f'<p class="kicker">{kicker}</p><h2>{headline}</h2>' + html
        else:
            lead, rest = _split_top(html, 2)  # answer plus the first block after it
            inner = f'<div class="keep"><p class="kicker">{kicker}</p><h2>{headline}</h2>{lead}</div>{rest}'
        out.append(f'<section class="page" id="{sid}">{band}<div class="inner">{inner}</div>'
                   f'<div class="foot"><span>Ind-Swift Laboratories | Company study | Not investment advice</span><span>{i + 1} / {total}</span></div></section>')
    body = "".join(out)
    cnt = [0]

    def _renum(m):
        cnt[0] += 1
        return f"<figcaption>Exhibit {cnt[0]}:"
    body = re.sub(r"<figcaption>Exhibit \d+:", _renum, body)
    html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Ind-Swift Laboratories Study</title>'
            '<meta name="description" content="Plain-language, chart-led company study of Ind-Swift Laboratories (NSE: INDSWFTLAB), data as of 9 Nov 2026.">'
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
    print("base", round(V["Base"]["value_ps"], 2), "bear", round(V["Bear"]["value_ps"], 2), "bull", round(V["Bull"]["value_ps"], 2),
          "readout", READOUT, "h2_need", round(CALC["h2_need"], 1), f"{CALC['h2_need_g']:+.3f}", "top9", round(CALC["top9_tot"], 2))
