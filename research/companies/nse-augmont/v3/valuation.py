"""Bear / base / bull scenarios for Augmont to FY29 (consolidated, INR crore).

Run:  python -I valuation.py      (from this folder; build_v3.py also imports it)
Out:  data/valuation-scenarios.json

Management gave NO numerical guidance on the Q2 FY27 call (transcript p.14),
so every projected line is a modeller estimate. FY27E = H1 FY27 actual (results
filing p.6) + an H2 estimate. Primary metric: P/E on owner profit (after
minority share). Cross-checks: P/B and EV/EBITDA.
"""
import json
import os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))

CMP = 922.0                     # Screener, 7 Nov 2026
PRICE_DATE = date(2026, 11, 7)
SHARES = 9.1373505              # crore, post-IPO (prospectus p.107); no further dilution disclosed
OWNER_EQ_SEP26 = 1696.7         # results filing p.8 (456.87m + 16,510.49m)
NET_CASH_SEP26 = 161.1          # cash 170.7 - debt and leases 9.6 (results p.8)
NCI_BOOK = 30.9                 # minority interest at book (proxy)

# Reported years (FY25 Screener rounded; FY26 audited AR p.84 / results p.6)
HIST = {
    "FY25": dict(sales=66231.0, op=305.0, oi=21.0, interest=13.0, dep=8.0, pbt=305.0, pat=227.0,
                 owner=218.1, eps=26.89),
    "FY26": dict(sales=94186.2, op=385.95, oi=96.3, interest=1.9, dep=7.3, pbt=473.1, pat=348.3,
                 owner=333.9, eps=40.45),
}
H1FY27 = dict(sales=34781.1, op=217.4, oi=47.5, interest=18.5, dep=3.9, owner=176.1)

TAX = 25.2      # % ; Q2 FY27 25.1%, FY26 26.4%, statutory 25.17%
NCI = 3.5       # % of PAT to minorities ; FY26 4.1%, H1 FY27 2.8%

# H2 FY27 estimate + FY28/FY29 drivers per scenario.
# growth = YoY sales growth %, opm = operating margin %, oi/interest/dep in Rs cr.
SCEN = {
    "Bear": dict(
        pe=14,
        h2=dict(sales=32000, opm=0.50, oi=20, interest=25, dep=4.1),
        years={"FY28E": dict(growth=8, opm=0.45, oi=60, interest=40, dep=10),
               "FY29E": dict(growth=8, opm=0.45, oi=60, interest=40, dep=12)},
        why="Old-gold margin fades back to the FY25-26 level (0.41-0.46%); receivables stay high, so the "
            "same capital turns over slower; finance cost stays at the Q2 run-rate; P/E compresses on "
            "cash and related-party worries."),
    "Base": dict(
        pe=20,
        h2=dict(sales=37200, opm=0.75, oi=30, interest=20, dep=4.1),
        years={"FY28E": dict(growth=18, opm=0.66, oi=80, interest=30, dep=10),
               "FY29E": dict(growth=16, opm=0.68, oi=90, interest=30, dep=12)},
        why="Old gold stays near 24% of buying, silver one-off does not repeat; growth funded only by "
            "retained profit (no dividend, no new equity), so sales per rupee of equity stays near the "
            "Q2 FY27 level; consumer mix and delivery centres lift margin slightly; P/E below today's 25x "
            "until cash conversion is proven."),
    "Bull": dict(
        pe=26,
        h2=dict(sales=40000, opm=0.90, oi=35, interest=15, dep=4.1),
        years={"FY28E": dict(growth=25, opm=0.85, oi=90, interest=25, dep=10),
               "FY29E": dict(growth=22, opm=0.88, oi=100, interest=25, dep=12)},
        why="Receivables normalise so capital turns faster; old-gold share holds or rises; EGR and "
            "Gold For All add higher-margin volume; P/E holds near today's level."),
}


def _yrs(fy):
    """Years from the price date to 31 March of that fiscal year."""
    end = date(2000 + int(fy[2:4]), 3, 31)
    return (end - PRICE_DATE).days / 365.25


def _row(sales, op, oi, interest, dep):
    pbt = op + oi - interest - dep
    pat = pbt * (1 - TAX / 100)
    owner = pat * (1 - NCI / 100)
    return dict(sales=sales, op=op, oi=oi, interest=interest, dep=dep, pbt=pbt, pat=pat, owner=owner,
                eps=owner / SHARES)


def run():
    out = dict(cmp=CMP, price_date=str(PRICE_DATE), shares_cr=SHARES, tax_pct=TAX, nci_pct=NCI,
               hist=HIST, h1fy27=H1FY27, scenarios={})
    for name, s in SCEN.items():
        h2 = s["h2"]
        h2_op = h2["sales"] * h2["opm"] / 100
        fy27 = _row(H1FY27["sales"] + h2["sales"], H1FY27["op"] + h2_op, H1FY27["oi"] + h2["oi"],
                    H1FY27["interest"] + h2["interest"], H1FY27["dep"] + h2["dep"])
        rows = {"FY27E": fy27}
        prev = fy27
        for fy, y in s["years"].items():
            sales = prev["sales"] * (1 + y["growth"] / 100)
            rows[fy] = prev = _row(sales, sales * y["opm"] / 100, y["oi"], y["interest"], y["dep"])
        # book value: owner equity at Sep 2026 + owner profit retained (no dividend)
        bv = OWNER_EQ_SEP26 + (fy27["owner"] - H1FY27["owner"])
        last_pat = HIST["FY26"]["owner"]
        for fy, r in rows.items():
            if fy != "FY27E":
                bv += r["owner"]
            r["bv"] = bv
            r["bvps"] = bv / SHARES
            r["opm"] = r["op"] / r["sales"] * 100
            r["pat_margin"] = r["pat"] / r["sales"] * 100
            r["owner_growth"] = (r["owner"] / last_pat - 1) * 100
            last_pat = r["owner"]
            r["target"] = r["eps"] * s["pe"]
            r["ret"] = (r["target"] / CMP - 1) * 100
            t = _yrs(fy)
            r["cagr"] = ((r["target"] / CMP) ** (1 / t) - 1) * 100
            r["years_from_now"] = t
            r["pb_at_target"] = r["target"] / r["bvps"]
            r["roe"] = r["owner"] / ((bv - r["owner"] / 2) if fy != "FY27E" else (OWNER_EQ_SEP26 + bv) / 2) * 100
            mcap = r["target"] * SHARES
            r["ev_ebitda_at_target"] = (mcap - NET_CASH_SEP26 + NCI_BOOK) / r["op"]
            r["sales_per_equity"] = r["sales"] / (bv - r["owner"] / 2)
        out["scenarios"][name] = dict(pe=s["pe"], why=s["why"], h2=h2, drivers=s["years"], rows=rows)
    # checks
    b = out["scenarios"]["Base"]["rows"]
    assert abs(b["FY27E"]["sales"] - 71981.1) < 0.1
    for sc in out["scenarios"].values():
        for r in sc["rows"].values():
            assert abs(r["pbt"] - (r["op"] + r["oi"] - r["interest"] - r["dep"])) < 1e-9
    return out


if __name__ == "__main__":
    res = run()
    p = os.path.join(HERE, "data", "valuation-scenarios.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
    for n, sc in res["scenarios"].items():
        print(f"\n{n}  (P/E {sc['pe']}x)")
        for fy, r in sc["rows"].items():
            cg = f"{r['cagr']:.1f}%" if r["cagr"] is not None else "-"
            print(f"  {fy}: sales {r['sales']:,.0f} op {r['op']:.0f} OPM {r['opm']:.2f}% PBT {r['pbt']:.0f} "
                  f"PAT {r['pat']:.0f} owner {r['owner']:.0f} g {r['owner_growth']:.0f}% EPS {r['eps']:.1f} "
                  f"TP {r['target']:,.0f} ret {r['ret']:.0f}% CAGR {cg} BVPS {r['bvps']:.0f} "
                  f"P/B {r['pb_at_target']:.1f} ROE {r['roe']:.1f}% EV/EBITDA {r['ev_ebitda_at_target']:.1f} "
                  f"S/E {r['sales_per_equity']:.0f}x")
