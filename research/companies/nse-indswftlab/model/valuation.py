"""Ind-Swift Laboratories sum-of-the-parts valuation (bear / base / bull).

Run: python -I -X utf8 model/valuation.py
Writes model/valuation.md and model/valuation.json next to this file.
Money in Rs crore unless stated. Every input carries its source tag; every derived number is [E].

Method (prompt section 5):
  value per share = ( core EV + net cash at 31 Mar 2027 + warrant cash still to come + Synthimed stake, net )
                    / diluted shares, discounted from 31 Mar 2027 to today at the cost of equity.
  core EV         = EV/EBITDA multiple x FY28E EBITDA (a one-year-forward multiple at 31 Mar 2027).
  net cash Mar-27 = net cash Sep-26 + Oct 2026 warrant conversion cash + H2 FY27 free cash flow
                    (so working-capital days change the value, not only the multiple).
  stake, net      = (look-through value - tax on the gain over the Rs 32 cr cost) x (1 - holding/illiquidity discount).
"""
import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---- Inputs (facts, with source tags) ------------------------------------------------
INPUTS = {
    "price": (349.0, "[Screener] close, 9 Nov 2026"),
    "shares_printed": (8.6961558, "8,69,61,558 shares [deck p31, NSE-C]; used for the market-value check"),
    "shares_diluted": (9.3961558, "8,83,61,558 after the 8 Oct conversion [E, Inferred] + 56,00,000 warrants [evidence/care-ma.md]"),
    "shares_diluted_alt": (9.2561558, "8,69,61,558 printed + 56,00,000 warrants (sensitivity)"),
    "fy26_revenue": (635.89, "[deck p23] FY26 operating revenue"),
    "h1_revenue_op": (420.97, "[deck p3, call p2] H1 FY27 operating revenue"),
    "h1_revenue_line": (416.35, "[deck p29] H1 FY27 revenue from operations line"),
    "q2_revenue_op": (234.89, "[call p2] Q2 FY27 operating revenue"),
    "h1_ebitda": (75.65, "[deck p29] H1 FY27 operating EBITDA"),
    "h1_pat": (55.47, "[deck p29]"),
    "h1_tax": (17.20, "[deck p29]"),
    "h1_pbt": (73.49, "[deck p29]"),
    "h1_depreciation": (15.35, "[deck p29]"),
    "h1_finance_cost": (2.04, "[deck p29]"),
    "h1_nonop_other_income": (15.23, "[deck p29]"),
    "cash_sep26": (322.81, "[deck p30]"),
    "current_investments_sep26": (45.03, "[deck p30]"),
    "borrowings_sep26": (19.48, "[deck p30] long-term 15.14 + short-term 4.34"),
    "inventory_sep26": (168.35, "[deck p30]"),
    "receivables_sep26": (234.79, "[deck p30]"),
    "payables_sep26": (133.70, "[deck p30]"),
    "ppe_cwip_sep26": (351.43, "[deck p30] PP&E 309.61 + CWIP 41.82"),
    "oct26_conversion_cash": (20.58, "[NSE-C] 14,00,000 x Rs 147, received 8 Oct 2026"),
    "warrant_cash_to_come": (82.32, "56,00,000 x Rs 147 [E, evidence/care-ma.md]"),
    "stake_pct": (0.078, "[deck p6, AR26 p10] 7.80% of Synthimed"),
    "stake_cost": (32.0, "[AR26 p80] 32,00,000 CCDs at Rs 32.00 cr, FVTPL"),
    "treasury_book_excluded": (307.6, "[AR26 p80-p81, E] promoter-linked or unlisted instruments, not counted"),
    "land_receivable_excluded": (15.54, "[CARE-F p10, E] Behra land, not counted"),
    "mgmt_wc_at_1500": (350.0, "[call p13] CFO: about Rs 350 cr of working capital at Rs 1,500 cr"),
    "fy26_ocf": (-68.0, "[Screener]"),
}
V = {k: v[0] for k, v in INPUTS.items()}

# ---- Assumptions (all [E]) ------------------------------------------------------------
TODAY = date(2026, 11, 9)
VALUE_DATE = date(2027, 3, 31)
YEARS_TO_VALUE_DATE = (VALUE_DATE - TODAY).days / 365.0
COST_OF_EQUITY = 0.13      # small-cap Indian pharma with concentration and governance WATCH points
TAX_RATE = 0.2517          # 22% + 10% surcharge + 4% cess (section 115BAA); H1 FY27 effective 23.4%
STAKE_TAX = 0.1495         # LTCG on unlisted 12.5% + 12% surcharge + 4% cess, for a company [assumption]
OTHER_INCOME_YEAR = 30.0   # non-operating other income, H1 FY27 Rs 15.23 cr x 2; P/E cross-check only
FINANCE_COST_YEAR = 4.0    # H1 FY27 Rs 2.04 cr x 2
DEPRECIATION_BASE = 30.7   # H1 FY27 Rs 15.35 cr x 2
DEP_RATE_ON_NEW = 0.08     # about 12-year life on new capex
# Capex: Rs 250 cr over 2.5 years from Oct 2026 [call p1-p2] + maintenance Rs 20 cr a year [assumption]
CAPEX = {"H2FY27": 50.0 + 10.0, "FY28": 100.0 + 20.0, "FY29": 100.0 + 20.0, "FY30": 20.0}

NET_CASH_SEP26 = V["cash_sep26"] + V["current_investments_sep26"] - V["borrowings_sep26"]
NWC_SEP26 = V["inventory_sep26"] + V["receivables_sep26"] - V["payables_sep26"]
NWC_DAYS_SEP26 = NWC_SEP26 / (2 * V["h1_revenue_line"]) * 365
MGMT_WC_DAYS = V["mgmt_wc_at_1500"] / 1500 * 365
FY30_TARGET = 1500.0

BASE_FY27 = V["fy26_revenue"] * 1.50
BASE_G = (FY30_TARGET / BASE_FY27) ** (1 / 3) - 1
BEAR_FY27 = V["h1_revenue_op"] + 2 * V["q2_revenue_op"]
BULL_FY30 = V["fy26_revenue"] * 1.25 ** 4          # top of the guided 20-25% FY26-FY30 CAGR [deck p23]
BULL_G = (BULL_FY30 / BASE_FY27) ** (1 / 3) - 1

YEARS = ["FY27", "FY28", "FY29", "FY30"]
SCENARIOS = {
    "Bear": {
        "fy27_revenue": BEAR_FY27,
        "growth": [None, 0.12, 0.12, 0.12],
        "margin": [0.175, 0.175, 0.175, 0.175],
        "wc_days": [NWC_DAYS_SEP26] * 4,
        "multiple": 10.0,
        "stake_equity": 7000.0, "stake_discount": 0.50,
        "why": ("Risk cards R1 (partner concentration), R2 (H2 FY27 miss), R3 (working capital keeps eating cash), "
                "R5 (stake sale does not happen) and R7 (multiple stays at contract-maker levels): "
                "H2 FY27 at the Q2 run rate, FY27 Rs {fy27:,.0f} cr (+{g27:.0f}%), margin 17.5%, 12% growth after FY27 as partner volumes flatten, "
                "working capital held at today's {wc:.0f} days, 10x (Lincoln, Indoco), stake at Rs 7,000 cr less tax and a 50% discount"),
    },
    "Base": {
        "fy27_revenue": BASE_FY27,
        "growth": [None, BASE_G, BASE_G, BASE_G],
        "margin": [0.19, 0.20, 0.20, 0.20],
        "wc_days": [110.0, 100.0, 92.0, MGMT_WC_DAYS],
        "multiple": 15.0,
        "stake_equity": 8000.0, "stake_discount": 0.25,
        "why": ("Management guidance exactly: FY27 +50% to Rs {fy27:,.0f} cr at 19%, then {g:.2f}% a year to Rs 1,500 cr in FY30 at 20%; "
                "working capital falling to the CFO's Rs 350 cr ({mwc:.0f} days) at Rs 1,500 cr; 15x forward EBITDA (Unichem 15.1x, "
                "a discount to the 17.9x peer median for ROCE of 4.9%, negative OCF and concentration); stake at management's Rs 8,000 cr less tax and a 25% discount"),
    },
    "Bull": {
        "fy27_revenue": BASE_FY27,
        "growth": [None, BULL_G, BULL_G, BULL_G],
        "margin": [0.19, 0.205, 0.21, 0.21],
        "wc_days": [110.0, 100.0, 92.0, MGMT_WC_DAYS],
        "multiple": 18.0,
        "stake_equity": 9000.0, "stake_discount": 0.15,
        "why": ("Guidance realised at the top of its range (business-valuation-scenarios Step 2): FY27 +50% to Rs {fy27:,.0f} cr at 19%, then {gb:.2f}% a year to "
                "Rs {fy30b:,.0f} cr in FY30, the 25% end of the guided 20-25% FY26-FY30 CAGR [deck p23], from triggers already disclosed and not in the base build: "
                "Viatris Clarithromycin (USD 6.0 mn launch value [deck p21]), the 100-150 registrations not yet earning [call p12] and the two unnamed customers due to sign in Q4 [call p13-p14]; "
                "margin 20.5% to 21% as staff-cost leverage continues (employee cost fell from 20.93% to 16.23% of revenue in Q2 [deck p28]); working capital as the base; "
                "18x, the peer median, for a proven exporter that collects its cash; stake at Rs 9,000 cr less tax and a 15% discount"),
    },
}

# ---- Screener history for the year-wise tables (consolidated, Rs cr) [Screener, fetched 9 Nov 2026] ----
HIST = {
    "FY25": {"sales": 574.0, "expenses": 581.0, "op": -7.0, "opm": -0.012, "other_income": 292.0, "interest": 3.0,
             "depreciation": 24.0, "pbt": 258.0, "tax_pct": 0.03, "pat": 250.0, "eps": 41.32, "pat_prev": 421.0},
    "FY26": {"sales": 649.0, "expenses": 602.0, "op": 47.0, "opm": 0.07, "other_income": 36.0, "interest": 1.0,
             "depreciation": 31.0, "pbt": 51.0, "tax_pct": 0.15, "pat": 43.0, "eps": 4.97, "pat_prev": 250.0},
}
SHARES_PRE = 8.8361558   # 8,83,61,558 after the 8 Oct 2026 conversion, before the 56,00,000 warrants [E, Inferred]
YEAR_END = {"FY27": date(2027, 3, 31), "FY28": date(2028, 3, 31), "FY29": date(2029, 3, 31), "FY30": date(2030, 3, 31)}


def project(s):
    rows, rev, cum_capex = [], None, CAPEX["H2FY27"]
    prev_nwc = NWC_SEP26
    for i, y in enumerate(YEARS):
        rev = s["fy27_revenue"] if i == 0 else rev * (1 + s["growth"][i])
        ebitda = rev * s["margin"][i]
        if i > 0:
            cum_capex += CAPEX[y]
        dep = DEPRECIATION_BASE + DEP_RATE_ON_NEW * cum_capex
        pbt = ebitda + OTHER_INCOME_YEAR - dep - FINANCE_COST_YEAR
        pat = pbt * (1 - TAX_RATE)
        nwc = s["wc_days"][i] / 365 * rev
        if i == 0:
            # H2 FY27 only: Oct 2026 to Mar 2027
            h2_ebitda = ebitda - V["h1_ebitda"]
            h2_pbt = h2_ebitda + OTHER_INCOME_YEAR / 2 - dep / 2 - FINANCE_COST_YEAR / 2
            tax = h2_pbt * TAX_RATE
            fcf = h2_ebitda + OTHER_INCOME_YEAR / 2 - FINANCE_COST_YEAR / 2 - tax - CAPEX["H2FY27"] - (nwc - prev_nwc)
            capex = CAPEX["H2FY27"]
        else:
            tax = pbt * TAX_RATE
            fcf = ebitda + OTHER_INCOME_YEAR - FINANCE_COST_YEAR - tax - CAPEX[y] - (nwc - prev_nwc)
            capex = CAPEX[y]
        rows.append({"year": y, "revenue": rev, "growth": rev / (V["fy26_revenue"] if i == 0 else rows[-1]["revenue"]) - 1,
                     "ebitda": ebitda, "margin": s["margin"][i], "depreciation": dep, "pbt": pbt, "pat": pat,
                     "eps_diluted": pat / V["shares_diluted"], "nwc": nwc, "nwc_days": s["wc_days"][i],
                     "delta_nwc": nwc - prev_nwc, "capex": capex, "fcf": fcf,
                     "fcf_period": "H2 FY27 (Oct-Mar)" if i == 0 else y})
        prev_nwc = nwc
    return rows


def stake_net(equity_value, discount):
    gross = V["stake_pct"] * equity_value
    tax = (gross - V["stake_cost"]) * STAKE_TAX
    return {"gross": gross, "tax": tax, "after_tax": gross - tax, "discount": discount,
            "net": (gross - tax) * (1 - discount)}


def value(s, rows, shares=None, include_stake=True, treasury_haircut=None):
    shares = shares or V["shares_diluted"]
    fy28 = rows[1]
    core_ev = s["multiple"] * fy28["ebitda"]
    net_cash_mar27 = NET_CASH_SEP26 + V["oct26_conversion_cash"] + rows[0]["fcf"]
    stake = stake_net(s["stake_equity"], s["stake_discount"])
    stake_v = stake["net"] if include_stake else 0.0
    treasury = 0.0 if treasury_haircut is None else V["treasury_book_excluded"] * (1 - treasury_haircut)
    equity_mar27 = core_ev + net_cash_mar27 + V["warrant_cash_to_come"] + stake_v + treasury
    ps_mar27 = equity_mar27 / shares
    ps_today = ps_mar27 / (1 + COST_OF_EQUITY) ** YEARS_TO_VALUE_DATE
    return {"fy28_ebitda": fy28["ebitda"], "multiple": s["multiple"], "core_ev": core_ev,
            "net_cash_sep26": NET_CASH_SEP26, "h2fy27_fcf": rows[0]["fcf"], "net_cash_mar27": net_cash_mar27,
            "warrant_cash": V["warrant_cash_to_come"], "stake": stake, "stake_counted": stake_v,
            "treasury_counted": treasury, "equity_mar27": equity_mar27, "shares": shares,
            "value_ps_mar27": ps_mar27, "value_ps": ps_today, "vs_price": ps_today / V["price"] - 1,
            "parts_ps": {"core": core_ev / shares / (1 + COST_OF_EQUITY) ** YEARS_TO_VALUE_DATE,
                         "cash": (net_cash_mar27 + V["warrant_cash_to_come"]) / shares / (1 + COST_OF_EQUITY) ** YEARS_TO_VALUE_DATE,
                         "stake": stake_v / shares / (1 + COST_OF_EQUITY) ** YEARS_TO_VALUE_DATE}}


def readout(base_gap, mgmt_verdict):
    label = "ATTRACTIVE" if base_gap >= 0.20 else ("STRETCHED" if base_gap <= -0.20 else "FAIR")
    if mgmt_verdict == "RED" and label == "ATTRACTIVE":
        label = "FAIR"
    return label


def fmt_why(s):
    return s["why"].format(fy27=s["fy27_revenue"], g27=(s["fy27_revenue"] / V["fy26_revenue"] - 1) * 100,
                           wc=NWC_DAYS_SEP26, g=BASE_G * 100, mwc=MGMT_WC_DAYS, gb=BULL_G * 100, fy30b=BULL_FY30)


def skill_table(s, rows, v):
    """Year-wise table in the business-valuation-scenarios Step 3 layout: Screener P&L rows for FY25-FY26 actual and
    FY27E-FY30E, plus PAT growth, PAT margin, target price per year (pre and post dilution) and return / CAGR vs CMP.
    Target price at 31 Mar of each year = (multiple, held flat, x that year's EBITDA + net cash at that year end
    + stake net [+ warrant cash, post-dilution only]) / shares. Net cash rolls forward by each year's FCF."""
    stake = v["stake"]["net"]
    cols, cash = [], v["net_cash_mar27"]
    prev_pat = HIST["FY26"]["pat"]
    for i, r in enumerate(rows):
        if i > 0:
            cash += r["fcf"]
        ev = s["multiple"] * r["ebitda"]
        tp_post = (ev + cash + V["warrant_cash_to_come"] + stake) / V["shares_diluted"]
        tp_pre = (ev + cash + stake) / SHARES_PRE
        yrs = (YEAR_END[r["year"]] - TODAY).days / 365.0
        other, interest = OTHER_INCOME_YEAR, FINANCE_COST_YEAR
        cols.append({"year": r["year"] + "E", "sales": r["revenue"], "expenses": r["revenue"] - r["ebitda"], "op": r["ebitda"],
                     "opm": r["margin"], "other_income": other, "interest": interest, "depreciation": r["depreciation"],
                     "pbt": r["pbt"], "tax_pct": TAX_RATE, "pat": r["pat"], "eps_pre": r["pat"] / SHARES_PRE,
                     "eps_post": r["eps_diluted"], "pat_growth": r["pat"] / prev_pat - 1, "pat_margin": r["pat"] / r["revenue"],
                     "net_cash_end": cash, "ev": ev, "tp_pre": tp_pre, "tp_post": tp_post,
                     "return_post": tp_post / V["price"] - 1, "years": yrs,
                     "cagr_post": (tp_post / V["price"]) ** (1 / yrs) - 1 })
        prev_pat = r["pat"]
    hist = [dict(year=y + "A", eps_pre=h["eps"], eps_post=None, pat_growth=h["pat"] / h["pat_prev"] - 1, pat_margin=h["pat"] / h["sales"],
                 **{k: h[k] for k in ("sales", "expenses", "op", "opm", "other_income", "interest", "depreciation", "pbt", "tax_pct", "pat")})
            for y, h in HIST.items()]
    return {"multiple": s["multiple"], "multiple_flat": True, "hist": hist, "proj": cols}


def skill_md(name, t):
    allc = t["hist"] + t["proj"]
    def row(label, key, fmt, hist_ok=True):
        cells = []
        for c in allc:
            x = c.get(key)
            cells.append("-" if x is None or (not hist_ok and c in t["hist"]) else fmt(x))
        return f"| {label} | " + " | ".join(cells) + " |"
    cr = lambda x: f"{x:,.1f}"
    p1 = lambda x: f"{x*100:.1f}%"
    rs = lambda x: f"{x:,.0f}"
    out = [f"### {name} ({t['multiple']:.0f}x EV/EBITDA, held flat FY27E-FY30E)", "",
           "| Rs cr | " + " | ".join(c["year"] for c in allc) + " |", "|---|" + "---|" * len(allc),
           row("Sales", "sales", cr), row("Expenses", "expenses", cr), row("Operating Profit", "op", cr), row("OPM %", "opm", p1),
           row("Other Income", "other_income", cr), row("Interest", "interest", cr), row("Depreciation", "depreciation", cr),
           row("Profit before tax", "pbt", cr), row("Tax %", "tax_pct", p1), row("Net Profit", "pat", cr),
           row("EPS pre-dilution (Rs)", "eps_pre", lambda x: f"{x:.2f}"), row("EPS post-dilution (Rs)", "eps_post", lambda x: f"{x:.2f}"),
           row("PAT Growth %", "pat_growth", p1), row("PAT Margin %", "pat_margin", p1),
           row("Net cash at year end", "net_cash_end", cr, False),
           row("Target price pre-dilution (Rs)", "tp_pre", rs, False), row("Target price post-dilution (Rs)", "tp_post", rs, False),
           row("Return vs CMP Rs 349 (post-dilution)", "return_post", lambda x: f"{x*100:+.0f}%", False),
           row("CAGR vs CMP to 31 Mar (post-dilution)", "cagr_post", lambda x: f"{x*100:+.1f}%", False), ""]
    return out


def main():
    mgmt_verdict = "WATCH"
    out = {"inputs": INPUTS, "assumptions": {
        "cost_of_equity": COST_OF_EQUITY, "tax_rate": TAX_RATE, "stake_tax": STAKE_TAX,
        "years_to_value_date": YEARS_TO_VALUE_DATE, "other_income_year": OTHER_INCOME_YEAR,
        "finance_cost_year": FINANCE_COST_YEAR, "depreciation_base": DEPRECIATION_BASE,
        "dep_rate_on_new": DEP_RATE_ON_NEW, "capex": CAPEX},
        "derived": {"net_cash_sep26": NET_CASH_SEP26, "nwc_sep26": NWC_SEP26, "nwc_days_sep26": NWC_DAYS_SEP26,
                    "mgmt_wc_days": MGMT_WC_DAYS, "base_fy27": BASE_FY27, "base_growth_fy28_30": BASE_G, "bull_growth_fy28_30": BULL_G,
                    "bear_fy27": BEAR_FY27,
                    "receivable_days": V["receivables_sep26"] / (2 * V["h1_revenue_line"]) * 365,
                    "inventory_days": V["inventory_sep26"] / (2 * V["h1_revenue_line"]) * 365,
                    "h2_need": BASE_FY27 - V["h1_revenue_op"], "h2_need_q": (BASE_FY27 - V["h1_revenue_op"]) / 2,
                    "h2_margin_needed_19": (0.19 * BASE_FY27 - V["h1_ebitda"]) / (BASE_FY27 - V["h1_revenue_op"]),
                    "fy26_fy30_cagr": (FY30_TARGET / V["fy26_revenue"]) ** 0.25 - 1},
        "scenarios": {}, "mgmt_verdict": mgmt_verdict}
    D = out["derived"]
    mcap = V["price"] * V["shares_printed"]
    md = ["# Ind-Swift Laboratories - valuation output", "",
          "Generated by model/valuation.py on " + TODAY.strftime("%a, %d %b %Y") + "; do not edit by hand.",
          f"Price Rs {V['price']:.0f}; printed shares 8,69,61,558 (market value Rs {mcap:,.2f} cr); diluted shares 9,39,61,558 used for value per share.",
          "Method: sum of the parts. Core EV = EV/EBITDA multiple x FY28E EBITDA, a one-year-forward multiple at 31 Mar 2027;"
          " plus net cash rolled to 31 Mar 2027 through H2 FY27 free cash flow; plus warrant cash still to come (Rs 82.32 cr);"
          " plus the Synthimed stake after tax and a holding and illiquidity discount; divided by diluted shares;"
          f" discounted {YEARS_TO_VALUE_DATE:.2f} years to today at {COST_OF_EQUITY*100:.0f}% cost of equity.",
          "Not counted: the Rs 307.6 cr treasury book in promoter-linked or unlisted instruments and the Rs 15.54 cr land receivable (upside case shown below).",
          "All derived figures are [E]; interest, depreciation and tax are an [E] bridge.", "",
          "## Starting point (Sep-26)", "",
          f"- Net cash: Rs {V['cash_sep26']} cash + Rs {V['current_investments_sep26']} current investments - Rs {V['borrowings_sep26']} borrowings = Rs {NET_CASH_SEP26:.2f} cr [deck p30, E]. Rs 16.00 cr of fixed deposits are pledged against a tax demand [AR26]; counted, because the deposit is still the company's.",
          f"- Net working capital: Rs {V['inventory_sep26']} + Rs {V['receivables_sep26']} - Rs {V['payables_sep26']} = Rs {NWC_SEP26:.2f} cr, {NWC_DAYS_SEP26:.1f} days of annualised H1 revenue (Rs {V['h1_revenue_line']} x 2); receivable days {D['receivable_days']:.1f}, inventory days {D['inventory_days']:.1f} [E].",
          f"- CFO's Rs 350 cr at Rs 1,500 cr is {MGMT_WC_DAYS:.1f} days; at today's days Rs 1,500 cr needs Rs {NWC_DAYS_SEP26/365*1500:,.2f} cr [E].",
          f"- FY27 guidance (+50%) is Rs {BASE_FY27:.2f} cr; H2 must be Rs {D['h2_need']:.2f} cr (Rs {D['h2_need_q']:.2f} cr a quarter), and a 19% full-year margin needs {D['h2_margin_needed_19']*100:.1f}% in H2 [E].",
          f"- FY26 to FY30 at Rs 1,500 cr is {D['fy26_fy30_cagr']*100:.2f}% a year; after a +50% FY27 it is {BASE_G*100:.2f}% a year [E].", ""]

    for name, s in SCENARIOS.items():
        rows = project(s)
        v = value(s, rows)
        out["scenarios"][name] = {"assumptions": {k: s[k] for k in s if k != "why"}, "why": fmt_why(s), "rows": rows, "value": v}
        st = v["stake"]
        md += [f"## {name}", "", fmt_why(s) + ".", "",
               "| Year | Revenue | Growth | EBITDA | Margin | Depreciation | PBT | PAT | EPS diluted (Rs) | NWC days | NWC | Capex | FCF |",
               "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            md.append(f"| {r['year']} | {r['revenue']:,.2f} | {r['growth']*100:.1f}% | {r['ebitda']:,.2f} | {r['margin']*100:.1f}% | {r['depreciation']:.1f} | {r['pbt']:,.1f} | {r['pat']:,.1f} | {r['eps_diluted']:.2f} | {r['nwc_days']:.0f} | {r['nwc']:,.1f} | {r['capex']:.0f} | {r['fcf']:,.1f} ({r['fcf_period']}) |")
        md += ["",
               f"- Core EV: {v['multiple']:.0f}x FY28E EBITDA Rs {v['fy28_ebitda']:.2f} cr = Rs {v['core_ev']:,.2f} cr.",
               f"- Net cash at Mar-27: Rs {NET_CASH_SEP26:.2f} + Rs {V['oct26_conversion_cash']} (Oct conversion) + Rs {v['h2fy27_fcf']:.2f} (H2 FY27 FCF) = Rs {v['net_cash_mar27']:.2f} cr; plus warrant cash Rs {V['warrant_cash_to_come']} cr.",
               f"- Stake: 7.8% x Rs {s['stake_equity']:,.0f} cr = Rs {st['gross']:.2f} cr; tax {STAKE_TAX*100:.2f}% on the gain over Rs 32 cr = Rs {st['tax']:.2f} cr; after tax Rs {st['after_tax']:.2f} cr; less {st['discount']*100:.0f}% = Rs {st['net']:.2f} cr.",
               f"- Equity at Mar-27 Rs {v['equity_mar27']:,.2f} cr / {v['shares']:.4f} cr shares = Rs {v['value_ps_mar27']:.2f}; today **Rs {v['value_ps']:.0f}** ({v['vs_price']*100:+.1f}% vs Rs {V['price']:.0f}).",
               f"- Per share today: core Rs {v['parts_ps']['core']:.0f}, cash Rs {v['parts_ps']['cash']:.0f}, stake Rs {v['parts_ps']['stake']:.0f}.", ""]

    # Year-wise tables per the business-valuation-scenarios skill, Steps 3 and 4
    out["skill_tables"] = {}
    md += ["## Year-wise scenario tables (business-valuation-scenarios layout)", "",
           "FY25A and FY26A are Screener consolidated actuals; FY27E-FY30E are the model. FY26 sales are Rs 649 cr on Screener (consolidated)"
           " but the guidance base is the deck's Rs 635.89 cr operating revenue, so FY27E growth is measured from Rs 635.89 cr.",
           "Target price at 31 Mar of each year = multiple x that year's EBITDA + net cash at that year end (rolled by free cash flow) + stake after tax and discount"
           " [+ Rs 82.32 cr warrant cash, post-dilution only], divided by 8,83,61,558 shares (pre-dilution) or 9,39,61,558 (post-dilution). Not discounted; CAGR is from 9 Nov 2026.", ""]
    for name, s in SCENARIOS.items():
        sc = out["scenarios"][name]
        t = skill_table(s, sc["rows"], sc["value"])
        out["skill_tables"][name] = t
        md += skill_md(name, t)
    md += ["### Key assumptions and caveats", "",
           "- Guided by management: FY27 revenue +50% (Rs 953.84 cr) and about 19% EBITDA margin [deck p3, call p4]; Rs 1,500 cr+ revenue by FY30 at a 20-25% CAGR [deck p23]; working capital about Rs 350 cr at Rs 1,500 cr [call p13]; Rs 250 cr capex [call p1-p2].",
           "- Estimated by us [E]: every bear line; the bull's top-of-range growth and 20.5-21% margins; FY28-FY29 path of the base; other income Rs 30 cr and interest Rs 4 cr a year (H1 FY27 x 2); depreciation (Rs 30.7 cr plus 8% of new capex); tax 25.17% (section 115BAA).",
           "- Dilution: 56,00,000 warrants (issue price Rs 196, Rs 147 a warrant still to pay, Rs 82.32 cr in all) are assumed converted, giving 9,39,61,558 shares post-dilution; pre-dilution uses 8,83,61,558 shares after the 8 Oct 2026 conversion (inferred from filings; the printed count is 8,69,61,558).",
           "- The multiple is held flat across years within each scenario (10x, 15x, 18x). That is a simplification: a real bear case usually also compresses the multiple and a bull case expands it, and a business that turns its cash flow positive would likely re-rate.",
           "- The headline value today applies the same multiple one year ahead (FY28 EBITDA at 31 Mar 2027) and discounts it to 9 Nov 2026 at 13%; the year-end target prices above are trailing and undiscounted, so the two are not the same number.",
           f"- Bull FY30 revenue of Rs {BULL_FY30:,.0f} cr is above the Rs 1,000-1,200 cr current plants carry; it needs Samba exports after EU/PIC/S approval and the full Rs 250 cr capex on time [deck p8, call p3, call p8, E].",
           "- Not investment advice. I am not a licensed financial advisor. These are scenario bands, not forecasts.", ""]

    base, bear, bull = (out["scenarios"][k]["value"] for k in ("Base", "Bear", "Bull"))
    out["readout"] = readout(base["vs_price"], mgmt_verdict)
    out["value_range"] = {"bear": bear["value_ps"], "base": base["value_ps"], "bull": bull["value_ps"]}
    md += ["## Readout", "",
           f"Value range Rs {bear['value_ps']:.0f} (bear) / Rs {base['value_ps']:.0f} (base) / Rs {bull['value_ps']:.0f} (bull) vs price Rs {V['price']:.0f}.",
           f"Base is {base['vs_price']*100:+.1f}% vs price: **{out['readout']}** (ATTRACTIVE at +20% or more, STRETCHED at -20% or worse; management verdict {mgmt_verdict}, so no cap applies).", ""]

    # Fragility: what the readout rests on
    bs = SCENARIOS["Base"]
    brows = out["scenarios"]["Base"]["rows"]
    frag = {
        "no_stake": value(bs, brows, include_stake=False),
        "alt_shares": value(bs, brows, shares=V["shares_diluted_alt"]),
        "treasury_50": value(bs, brows, treasury_haircut=0.5),
        "stake_50pct_discount": value(dict(bs, stake_discount=0.50), brows),
        "multiple_12": value(dict(bs, multiple=12.0), brows),
        "bear_wc_days": value(dict(bs, wc_days=[NWC_DAYS_SEP26] * 4), project(dict(bs, wc_days=[NWC_DAYS_SEP26] * 4))),
    }
    out["fragility"] = {k: {"value_ps": x["value_ps"], "vs_price": x["vs_price"], "readout": readout(x["vs_price"], mgmt_verdict)} for k, x in frag.items()}
    labels = {"no_stake": "Stake counted at zero", "alt_shares": "Diluted shares 9,25,61,558 (printed count)",
              "treasury_50": "Treasury book counted at 50% of Rs 307.6 cr", "stake_50pct_discount": "Stake discount 50% instead of 25%",
              "multiple_12": "12x instead of 15x", "bear_wc_days": "Working capital stays at today's days (moves only H2 FY27 cash; the forward multiple assumes normal working capital)"}
    md += ["## What the base readout rests on", "", "| Change to the base case | Value (Rs) | vs price | Readout |", "|---|---|---|---|"]
    for k, x in out["fragility"].items():
        md.append(f"| {labels[k]} | {x['value_ps']:.0f} | {x['vs_price']*100:+.1f}% | {x['readout']} |")
    md.append("")

    # Reverse check
    stake_mgmt = V["stake_pct"] * 8000
    rev_rows = []
    simple_core = mcap - NET_CASH_SEP26 - stake_mgmt
    dil_mcap = V["price"] * V["shares_diluted"]
    dil_cash = NET_CASH_SEP26 + V["oct26_conversion_cash"] + V["warrant_cash_to_come"]
    dil_core = dil_mcap - dil_cash - stake_mgmt
    dil_core_net = dil_mcap - dil_cash - base["stake"]["net"]
    f27, f28 = brows[0]["ebitda"], brows[1]["ebitda"]
    for label, mc, cash, stk in (("Simple: printed shares, stake at Rs 624 cr gross", mcap, NET_CASH_SEP26, stake_mgmt),
                                 ("Fully diluted: 9,39,61,558 shares, all warrant cash, stake at Rs 624 cr gross", dil_mcap, dil_cash, stake_mgmt),
                                 ("Fully diluted, stake after tax and 25% discount", dil_mcap, dil_cash, base["stake"]["net"])):
        core = mc - cash - stk
        rev_rows.append({"label": label, "mcap": mc, "cash": cash, "stake": stk, "core_ev": core,
                         "x_fy27": core / f27, "x_fy28": core / f28, "ebitda_at_15x": core / 15})
    out["reverse"] = rev_rows
    md += ["## What the price implies", "", f"FY27 base EBITDA Rs {f27:.2f} cr; FY28 base EBITDA Rs {f28:.2f} cr.", "",
           "| Reading | Market value | Cash netted | Stake netted | Core EV | x FY27 EBITDA | x FY28 EBITDA | EBITDA implied at 15x |", "|---|---|---|---|---|---|---|---|"]
    for r in rev_rows:
        md.append(f"| {r['label']} | {r['mcap']:,.2f} | {r['cash']:.2f} | {r['stake']:.2f} | {r['core_ev']:,.2f} | {r['x_fy27']:.2f}x | {r['x_fy28']:.2f}x | {r['ebitda_at_15x']:.2f} |")
    md.append("")

    # Sensitivity: FY28 EBITDA x multiple (base cash and stake)
    ebitdas = [150.0, 175.0, round(f28, 2), 250.0, 275.0]
    mults = [10.0, 12.0, 15.0, 18.0, 20.0]
    grid = []
    for e in ebitdas:
        cells = []
        for m in mults:
            eq = m * e + base["net_cash_mar27"] + V["warrant_cash_to_come"] + base["stake"]["net"]
            cells.append(eq / V["shares_diluted"] / (1 + COST_OF_EQUITY) ** YEARS_TO_VALUE_DATE)
        grid.append({"fy28_ebitda": e, "values": cells})
    out["sensitivity"] = {"multiples": mults, "rows": grid}
    md += ["## Sensitivity: value per share today (Rs), base cash and stake", "",
           "| FY28E EBITDA \\ EV/EBITDA | " + " | ".join(f"{m:.0f}x" for m in mults) + " |", "|---|" + "---|" * len(mults)]
    for g in grid:
        md.append(f"| Rs {g['fy28_ebitda']:.2f} cr | " + " | ".join(f"{c:.0f}" for c in g["values"]) + " |")
    md += ["", f"Price Rs {V['price']:.0f}. FY28 base EBITDA is Rs {f28:.2f} cr; bear Rs {out['scenarios']['Bear']['rows'][1]['ebitda']:.2f} cr.", ""]

    # Bottom-up FY28 revenue check
    own_run = 125.0 * 4
    new_regs = 125 * 0.93 * 0.5
    cmo_run = 65.0 * 4
    viatris_add = 22.5 * 4
    dom_run = (V["q2_revenue_op"] - 190.0) * 4
    dom_fy28 = dom_run * 1.175
    bu = {"own_brand_run_rate": own_run, "new_registrations": new_regs, "cmo_run_rate": cmo_run,
          "viatris_ibuprofen": viatris_add, "domestic_run_rate": dom_run, "domestic_fy28": dom_fy28}
    bu["total"] = own_run + new_regs + cmo_run + viatris_add + dom_fy28
    bu["base_fy28"] = brows[1]["revenue"]
    bu["export_fy28"] = own_run + new_regs + cmo_run + viatris_add
    out["bottom_up_fy28"] = bu
    md += ["## Bottom-up check on FY28 revenue", "",
           "| Block | Rs cr | Working |", "|---|---|---|",
           f"| Own-brand export, Q2 run rate | {own_run:.0f} | Rs 125 cr a quarter x 4 [call p5] |",
           f"| New registrations earning in FY28 | {new_regs:.0f} | 125 of the 100-150 already registered x Rs 0.93 cr a year x half a year [call p12, call p15, E] |",
           f"| CMO export, Q2 run rate | {cmo_run:.0f} | Rs 65 cr a quarter x 4 [call p5] |",
           f"| Viatris Ibuprofen added | {viatris_add:.0f} | Rs 20-25 cr a quarter from Q4 FY27 [call p4]; Clarithromycin not added |",
           f"| Domestic and other | {dom_fy28:.0f} | (Rs 234.89 - Rs 190) cr x 4 = Rs {dom_run:.0f} cr, +17.5% (15-20% guide) |",
           f"| **Total** | **{bu['total']:,.0f}** | vs base FY28 Rs {bu['base_fy28']:,.2f} cr ({(bu['total']/bu['base_fy28']-1)*100:+.1f}%) |", "",
           f"Export of Rs {bu['export_fy28']:,.0f} cr sits inside the Derabassi capacity of about Rs 1,050 cr at full use (Rs 760 cr a year at 72.5% use) [deck p8, call p5, call p8, E].",
           "The build adds no growth in existing own-brand or CMO volume, so FY28 guidance needs little beyond Q2 holding for a full year plus Viatris.",
           f"But the Q2 run rate already includes the Rs 58 cr partner quarter [call p5]: if that partner falls back to its Q1 Rs 25 cr, FY28 is about Rs {(58-25)*4:.0f} cr lower [E].", ""]

    # Cross-checks
    b28 = brows[1]
    b30 = brows[3]
    cross = {
        "pe_fy28_base": V["price"] / b28["eps_diluted"],
        "eps_fy28_base": b28["eps_diluted"],
        "pat_fy30_base": b30["pat"],
        "fcf_fy28_base": b28["fcf"],
        "fcf_yield_fy28_base": b28["fcf"] / dil_mcap,
        "fcf_fy28_bear": out["scenarios"]["Bear"]["rows"][1]["fcf"],
        "nwc_fy30_base": b30["nwc"],
        "nwc_fy30_at_today_days": NWC_DAYS_SEP26 / 365 * b30["revenue"],
        "asset_turnover_now": 2 * V["h1_revenue_line"] / V["ppe_cwip_sep26"],
        "asset_turnover_fy30": FY30_TARGET / (V["ppe_cwip_sep26"] + 250.0),
        "ttm_pe_screener": 33.0,
    }
    out["cross_checks"] = cross
    md += ["## Cross-checks", "",
           f"- P/E on FY28 base: Rs {V['price']:.0f} / EPS Rs {cross['eps_fy28_base']:.2f} (diluted) = {cross['pe_fy28_base']:.1f}x; Screener TTM P/E 33.0x [Screener].",
           f"- FY30 base PAT Rs {cross['pat_fy30_base']:.1f} cr vs the CFO's 'about Rs 200 cr' [tr-q1]: consistent.",
           f"- FCF: FY28 base Rs {cross['fcf_fy28_base']:.1f} cr, a {cross['fcf_yield_fy28_base']*100:.1f}% yield on the diluted market value; bear Rs {cross['fcf_fy28_bear']:.1f} cr. Capex and working capital absorb most of the EBITDA until FY29.",
           f"- Working capital at Rs 1,500 cr: Rs {cross['nwc_fy30_base']:.0f} cr if the CFO's target holds vs Rs {cross['nwc_fy30_at_today_days']:.0f} cr at today's days; the gap of Rs {cross['nwc_fy30_at_today_days']-cross['nwc_fy30_base']:.0f} cr is {((cross['nwc_fy30_at_today_days']-cross['nwc_fy30_base'])/NET_CASH_SEP26)*100:.0f}% of today's net cash.",
           f"- Asset turnover (revenue / PP&E plus CWIP): {cross['asset_turnover_now']:.2f}x now; {cross['asset_turnover_fy30']:.2f}x at Rs 1,500 cr after the Rs 250 cr capex [E].",
           ""]

    (HERE / "valuation.md").write_text("\n".join(md), encoding="utf-8")
    (HERE / "valuation.json").write_text(json.dumps(out, indent=1, default=float), encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
