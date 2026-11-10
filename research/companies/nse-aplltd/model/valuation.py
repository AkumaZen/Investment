"""Alembic Pharmaceuticals: structural-vs-one-off arithmetic and bear/base/bull valuation to FY29.

Run: python -I -X utf8 model/valuation.py
Writes model/valuation.md and model/valuation.json next to this file.
Money in Rs crore unless stated. Every input carries its source.
"""
import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent

INPUTS = {
    "price": (1017.0, "Screener overview, 10 Nov 2026"),
    "mcap": (19996.0, "Screener overview, 10 Nov 2026"),
    "ttm_eps": (42.92, "Screener TTM (Sep-26)"),
    "ttm_ebitda": (1413.0, "Screener TTM operating profit"),
    "fy26_sales": (7345.0, "Screener FY26"),
    "fy26_eps": (34.33, "Screener FY26"),
    "net_debt_sep26": (1236.0, "Q2 FY27 call p6"),
    "h1_sales": (4753.0, "Q2 FY27 call p5 (Rs 47.53 bn, Q2 deck)"),
    "h1_ebitda_screener": (894.0, "Screener Jun-26 332 + Sep-26 562"),
    "q1_ebitda_company": (348.0, "Q1 FY27 call"),
    "q2_ebitda_margin_company": (0.222, "Q2 FY27 call p5"),
    "h2_fy26_sales": (3724.0, "Screener Dec-25 1,876 + Mar-26 1,848"),
    # segment revenue, Rs bn [Q2 deck]
    "us_q2fy26": (5.66, "Q2 deck"), "us_q2fy27": (10.03, "Q2 deck"),
    "us_h1fy26": (10.89, "Q2 deck"), "us_q1fy27": (7.78, "Q1/Q2 deck"),
    "group_q2fy27": (26.03, "Q2 deck"), "group_q2fy26": (19.10, "Q2 deck"),
    "base_growth_q2": (0.23, "Q2 FY27 call p6: base grew 23% without new launches"),
    "base_growth_q1": (0.25, "Q2 FY27 call p6: Q1 ex-bosutinib growth 'mid-20s' (25% used) [E]"),
    "q2_ebitda_screener": (562.0, "Screener Sep-26"), "q2fy26_ebitda_screener": (316.0, "Screener Sep-25"),
    "q2_sales": (2603.0, "Screener Sep-26"), "q2fy26_sales": (1910.0, "Screener Sep-25"),
    "us_growth_q1_reported": (0.49, "Q1 FY27 call p4"), "us_growth_q1_cc": (0.375, "Q1 FY27 call p14: 37-38% constant currency"),
}
V = {k: v[0] for k, v in INPUTS.items()}
SHARES = V["mcap"] / V["price"]          # 19.66 cr [E]
TAX = 0.25                               # [G] Q2 FY27 call p5
VALUE_DATE = date(2026, 11, 10)
YEAR_END = {"FY27": date(2027, 3, 31), "FY28": date(2028, 3, 31), "FY29": date(2029, 3, 31)}
OTHER_INCOME = [20.0, 25.0, 30.0]        # [E] Screener TTM Rs 6 cr; FY25 Rs 56 cr
DEPRECIATION = [400.0, 430.0, 455.0]     # [E] Q2 FY27 run rate Rs 101 cr x 4, rising with launches
INTEREST = [130.0, 120.0, 105.0]         # [E] Q2 FY27 Rs 38 cr; net debt falls as capex is "behind us"
PE = 22.0                                # held flat; close to the trailing 22.3x (Screener) to 23.7x (price / TTM EPS)

SCENARIOS = {
    "Bear": {"growth": [0.20, 0.02, 0.08], "margin": [0.185, 0.165, 0.17],
             "why": "Built from risk cards R1 (bosutinib erodes fast), R2 (rupee reverses), R3 (US price erosion as in FY23) and R4 (India lags): FY27 at the bottom of the guide with H2 margin sliding, FY28 revenue +2% as the launch block fades, margin back to the pre-exclusivity 16% to 17%"},
    "Base": {"growth": [0.225, 0.11, 0.10], "margin": [0.195, 0.20, 0.20],
             "why": "Management guidance with no haircut: FY27 +22.5% (midpoint of 20% to 25%) at the 19.5% H1 margin the CFO says continues (company basis); FY28 US +10% to 12% with India at market, ex-US mid-teens and API about 10% gives about +11%; margin 'closer to 20%' in FY28 and FY29"},
    "Bull": {"growth": [0.25, 0.14, 0.13], "margin": [0.205, 0.21, 0.215],
             "why": "Guidance realised faster from disclosed triggers only: FY27 at the top of the guide; FY28 lifted by dapagliflozin shared exclusivity, binimetinib sole FTF and the first DifGen products; branded drag of 150 to 200 bp gone in FY28 (Q2 FY27 call p8, p11) takes margin above 20%"},
}
HIST = [
    {"year": "FY25A", "sales": 6672.0, "op": 1008.0, "other_income": 56.0, "interest": 79.0, "depreciation": 279.0,
     "pbt": 707.0, "tax_pct": 0.18, "pat": 582.0, "eps": 29.68, "pat_prev": 616.0},
    {"year": "FY26A", "sales": 7345.0, "op": 1121.0, "other_income": -14.0, "interest": 94.0, "depreciation": 319.0,
     "pbt": 694.0, "tax_pct": 0.03, "pat": 671.0, "eps": 34.33, "pat_prev": 582.0},
]


def decomposition():
    d = {}
    # Q2 US split
    base_q2 = V["us_q2fy26"] * (1 + V["base_growth_q2"])
    d["q2_us_base_bn"] = base_q2
    d["q2_us_launch_bn"] = V["us_q2fy27"] - base_q2
    d["q2_launch_share_of_us"] = d["q2_us_launch_bn"] / V["us_q2fy27"]
    d["q2_launch_share_of_group"] = d["q2_us_launch_bn"] / V["group_q2fy27"]
    # Q1 US split
    us_q1fy26 = V["us_h1fy26"] - V["us_q2fy26"]
    base_q1 = us_q1fy26 * (1 + V["base_growth_q1"])
    d["q1_us_prev_bn"] = us_q1fy26
    d["q1_us_base_bn"] = base_q1
    d["q1_us_launch_bn"] = V["us_q1fy27"] - base_q1
    d["q1_fx_points"] = V["us_growth_q1_reported"] - V["us_growth_q1_cc"]
    # Q2 margin split
    q2_ebitda_co = V["q2_sales"] * V["q2_ebitda_margin_company"]
    launch_cr = d["q2_us_launch_bn"] * 100
    rest = V["q2_sales"] - launch_cr
    d["q2_ebitda_company"] = q2_ebitda_co
    d["q2_rest_sales"] = rest
    d["q2_rest_ebitda_lo"], d["q2_rest_ebitda_hi"] = rest * 0.16, rest * 0.17
    d["q2_launch_ebitda_lo"] = q2_ebitda_co - d["q2_rest_ebitda_hi"]
    d["q2_launch_ebitda_hi"] = q2_ebitda_co - d["q2_rest_ebitda_lo"]
    d["q2_launch_margin_lo"] = d["q2_launch_ebitda_lo"] / launch_cr
    d["q2_launch_margin_hi"] = d["q2_launch_ebitda_hi"] / launch_cr
    d["q2_incremental_margin"] = (V["q2_ebitda_screener"] - V["q2fy26_ebitda_screener"]) / (V["q2_sales"] - V["q2fy26_sales"])
    d["q2_margin_ex_launch_mid"] = (q2_ebitda_co - (d["q2_launch_ebitda_lo"] + d["q2_launch_ebitda_hi"]) / 2) / rest
    # H1 margin, conflict C1
    d["h1_margin_company"] = (V["q1_ebitda_company"] + q2_ebitda_co) / V["h1_sales"]
    d["h1_margin_screener"] = V["h1_ebitda_screener"] / V["h1_sales"]
    # implied H2 from guidance
    for tag, g in (("lo", 0.20), ("hi", 0.25)):
        fy = V["fy26_sales"] * (1 + g)
        h2 = fy - V["h1_sales"]
        d[f"fy27_guided_{tag}"] = fy
        d[f"h2_implied_{tag}"] = h2
        d[f"h2_vs_h1_{tag}"] = h2 / V["h1_sales"] - 1
        d[f"h2_vs_h2fy26_{tag}"] = h2 / V["h2_fy26_sales"] - 1
    return d


def project(s):
    rows, rev = [], V["fy26_sales"]
    for i, y in enumerate(["FY27", "FY28", "FY29"]):
        rev = rev * (1 + s["growth"][i])
        op = rev * s["margin"][i]
        pbt = op + OTHER_INCOME[i] - DEPRECIATION[i] - INTEREST[i]
        pat = pbt * (1 - TAX)
        rows.append({"year": y, "sales": rev, "growth": s["growth"][i], "op": op, "opm": s["margin"][i],
                     "other_income": OTHER_INCOME[i], "interest": INTEREST[i], "depreciation": DEPRECIATION[i],
                     "pbt": pbt, "tax_pct": TAX, "pat": pat, "eps": pat / SHARES})
    return rows


def skill_table(rows):
    hist = []
    for h in HIST:
        hist.append(dict(h, expenses=h["sales"] - h["op"], opm=h["op"] / h["sales"],
                         pat_growth=h["pat"] / h["pat_prev"] - 1, pat_margin=h["pat"] / h["sales"]))
    proj, prev = [], HIST[-1]["pat"]
    for r in rows:
        tp = r["eps"] * PE
        yrs = (YEAR_END[r["year"]] - VALUE_DATE).days / 365
        proj.append(dict(r, year=r["year"] + "E", expenses=r["sales"] - r["op"], pat_growth=r["pat"] / prev - 1,
                         pat_margin=r["pat"] / r["sales"], tp=tp, ret=tp / V["price"] - 1, years=yrs,
                         cagr=(tp / V["price"]) ** (1 / yrs) - 1))
        prev = r["pat"]
    return {"multiple": PE, "hist": hist, "proj": proj}


CAVEATS = [
    "Guided by management: FY27 revenue growth about 20% to 25% including the expected normalisation of exclusivity sales (Q2 FY27 call p5); FY28 US growth about 10% to 12% (p13); EBITDA margin 'closer to 20%' for FY28 to FY29 (p14); tax 25% from FY27 (p5); no branded drag in FY28 (p11).",
    "Estimated by us [E]: FY28 and FY29 group growth (guidance covers only the US for FY28), every bear and bull line, other income Rs 20 to 30 cr, depreciation Rs 400 to 455 cr, interest Rs 130 to 105 cr.",
    "Margin basis: the model uses Screener's operating profit, which ran about Rs 16 cr a quarter below company EBITDA in FY27 (conflict C2); the FY27 base margin of 19.5% is the company-basis H1 figure (conflict C1).",
    f"Share count: {SHARES:.2f} cr shares (market cap / price, face value Rs 2). No warrants or convertibles found in the documents read, so pre and post-dilution EPS are the same.",
    "The P/E is held flat at 22x across years and scenarios. That is a simplification: a bear outcome would usually also compress the multiple, and a bull outcome could expand it.",
    "Target price at 31 Mar of each year = that year's EPS x 22, not discounted. Return and CAGR run from Rs 1,017 on 10 Nov 2026. FY27E CAGR is annualised over the 0.39 years to 31 Mar 2027, so small moves show as large yearly rates; read it with the return row.",
    "Not investment advice. The author is not a licensed financial advisor. These are scenario bands, not forecasts, and no rating is given.",
]


def main():
    d = decomposition()
    out = {"inputs": INPUTS, "shares_cr": SHARES, "pe": PE, "tax": TAX, "decomposition": d, "scenarios": {}}
    for name, s in SCENARIOS.items():
        rows = project(s)
        out["scenarios"][name] = {"assumptions": s, "rows": rows, "table": skill_table(rows)}
    # reverse check and cross-checks
    ev = V["mcap"] + V["net_debt_sep26"]
    base = out["scenarios"]["Base"]["rows"]
    out["cross"] = {
        "pe_ttm": V["price"] / V["ttm_eps"], "pe_fy26": V["price"] / V["fy26_eps"],
        "eps_needed_at_22x": V["price"] / PE,
        "ev": ev, "ev_ttm_ebitda": ev / V["ttm_ebitda"],
        "ev_fy28_base_ebitda": ev / base[1]["op"], "pe_fy28_base": V["price"] / base[1]["eps"],
        "pe_fy27_base": V["price"] / base[0]["eps"],
    }
    out["caveats"] = CAVEATS

    f = lambda v: f"{v:,.0f}"
    p = lambda v: f"{v*100:.1f}%"
    md = ["# Alembic Pharmaceuticals - model output", "", "Generated by model/valuation.py; do not edit by hand.", "",
          "## Structural vs one-off arithmetic [E]", ""]
    for k, v in d.items():
        md.append(f"- {k}: {v:,.3f}")
    md += ["", f"Shares {SHARES:.4f} cr; P/E {PE:.0f}x flat; tax {TAX*100:.0f}%.", ""]
    for name, sc in out["scenarios"].items():
        t = sc["table"]
        cols = t["hist"] + t["proj"]
        md += [f"## {name}", "", sc["assumptions"]["why"] + ".", "",
               "| Rs cr | " + " | ".join(c["year"] for c in cols) + " |", "|---|" + "---|" * len(cols)]
        for lab, key, fm in [("Sales", "sales", f), ("Expenses", "expenses", f), ("Operating Profit", "op", f), ("OPM %", "opm", p),
                             ("Other Income", "other_income", f), ("Interest", "interest", f), ("Depreciation", "depreciation", f),
                             ("Profit before tax", "pbt", f), ("Tax %", "tax_pct", p), ("Net Profit", "pat", f),
                             ("EPS (Rs)", "eps", lambda v: f"{v:.2f}"), ("PAT Growth %", "pat_growth", p), ("PAT Margin %", "pat_margin", p),
                             ("Target price at 31 Mar (Rs)", "tp", f), ("Return vs CMP", "ret", lambda v: f"{v*100:+.0f}%"),
                             ("CAGR vs CMP", "cagr", lambda v: f"{v*100:+.1f}%")]:
            md.append(f"| {lab} | " + " | ".join("-" if c.get(key) is None else fm(c[key]) for c in cols) + " |")
        md.append("")
    md += ["## Cross-checks", ""] + [f"- {k}: {v:,.2f}" for k, v in out["cross"].items()]
    md += ["", "## Caveats", ""] + [f"- {c}" for c in CAVEATS]
    (HERE / "valuation.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (HERE / "valuation.json").write_text(json.dumps(out, indent=1, default=float), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
