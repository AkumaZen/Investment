"""Reproduce Augmont's dated financial bridges and illustrative valuation.

INR crore except shares and per-share INR. No financial guidance is assumed.
Run from any directory: python model.py
"""
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def calculate():
    inputs = json.loads((BASE / 'data/primary-results-inputs.json').read_text(encoding='utf-8-sig'))
    pnl = {row['period']: row for row in inputs['pnl']}
    bs = inputs['balance_sheet'][0]
    cf = inputs['cash_flow'][0]
    # Final prospectus physical p107; post-offer terms. Later allotment/ESOP check pending.
    issued_shares = 91373505
    shares_crore = issued_shares / 10000000
    # Secondary Screener quote accessed 7 Nov 2026; exchange timestamp unverified.
    quote = 921.50
    ttm_owner = pnl['FY26']['owner_pat'] - pnl['H1FY26']['owner_pat'] + pnl['H1FY27']['owner_pat']
    debt = sum(bs[k] for k in ('borrowing_current', 'borrowing_noncurrent', 'leases_current', 'leases_noncurrent'))
    market_cap = quote * shares_crore
    operating_ebitda = pnl['FY26']['calculated_operating_ebitda_excluding_other_income']
    # No EBITDA adjustment for hedge matching is supported. This is a mechanical
    # definition, not verified normalised earnings. NCI book value is only a proxy.
    nci_proxy = bs['nci_equity']
    scenarios = []
    for name, earnings_factor, multiple in [('Bear', .75, 12), ('Reference', 1, 18), ('Bull', 1.25, 24)]:
        earnings = operating_ebitda * earnings_factor
        ev = earnings * multiple
        equity = ev - debt - nci_proxy  # zero surplus-cash credit by assumption
        per_share = equity / shares_crore
        scenarios.append(dict(name=name, assumption='Illustrative analyst assumptions, not guidance or fair value',
                              ebitda_factor=earnings_factor, multiple=multiple, ebitda=earnings,
                              ev=ev, equity=equity, per_share=per_share,
                              return_percent=(per_share / quote - 1) * 100))
    sensitivity = [{'multiple': m, 'values': [
        (operating_ebitda * f * m - debt - nci_proxy) / shares_crore for f in (.75, 1, 1.25)]}
        for m in (12, 18, 24)]
    result = dict(units='INR crore except shares, per-share INR and percentages', analysis_date='2026-11-07',
                  inputs=inputs, issued_shares=issued_shares, shares_crore=shares_crore,
                  dilution_status='Post-offer prospectus terms; final allotment and current ESOP/options not independently closed',
                  quote=quote, quote_status='Secondary Screener quote accessed 2026-11-07; exchange close/time unverified',
                  market_cap=market_cap, ttm_owner_pat=ttm_owner, pe=market_cap / ttm_owner,
                  debt_including_leases=debt, nci_book_proxy=nci_proxy, surplus_cash_credit=0,
                  cash_minus_debt_accounting_only=bs['cash'] - debt,
                  ev_no_surplus_cash_credit=market_cap + debt + nci_proxy,
                  ev_multiple=(market_cap + debt + nci_proxy) / operating_ebitda,
                  h1_cfo_pat_percent=cf['cfo'] / pnl['H1FY27']['owner_pat'] * 100,
                  h1_cfo_minus_cash_capex=cf['cfo'] + cf['capex'],
                  h1_owner_growth_percent=(pnl['H1FY27']['owner_pat'] / pnl['H1FY26']['owner_pat'] - 1) * 100,
                  q2_owner_growth_percent=(pnl['Q2FY27']['owner_pat'] / pnl['Q2FY26']['owner_pat'] - 1) * 100,
                  receivables_increase=bs['receivables'] - inputs['balance_sheet'][1]['receivables'],
                  cash_flow_aggregation_residual=cf['net_cash_change'] - cf['cfo'] - cf['cfi'] - cf['cff'],
                  fy26_owner_pat=333.915, fy25_owner_pat=218.096,
                  fy26_cfo=-42.157, fy25_cfo=105.448,
                  scenarios=scenarios, sensitivity=sensitivity, management_guided_base=None,
                  limitations=['Operating EBITDA excludes other income mechanically; hedge-to-underlying matching unresolved.',
                               'Multiples and earnings factors are analyst illustrations, not peer-derived forecasts.',
                               'NCI fair value unknown; book proxy is not a valuation.',
                               'Cash retained for operating/custodial/restricted obligations; zero surplus credit is conservative assumption.',
                               'Current dilution and independent exchange quote remain open; no actionable price target.'])
    assert abs(ttm_owner - 335.412) < .00001
    assert abs(market_cap - 8420.06848575) < .00001
    assert abs(debt - 9.614) < .00001
    # Rounded primary subtotals leave a 0.002 crore residual; retain it, do not plug CFO.
    assert abs(cf['cfo'] + cf['cfi'] + cf['cff'] - cf['net_cash_change']) < .003
    assert abs(operating_ebitda + pnl['FY26']['other_income'] - 482.206) < .00001
    assert abs(result['h1_cfo_minus_cash_capex'] + 582.074) < .00001
    return result


if __name__ == '__main__':
    result = calculate()
    target = BASE / 'data/model-output.json'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Saved {target.name}; owner TTM PAT {result['ttm_owner_pat']:.3f}; P/E {result['pe']:.2f}x")
