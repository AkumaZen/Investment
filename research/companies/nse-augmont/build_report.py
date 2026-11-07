"""Build the evidence-labelled interim report. Run model.py first for an audit copy."""
import json
import re
from html import escape
from pathlib import Path
from model import calculate
from render_report import render

B = Path(__file__).resolve().parent
M = calculate()
sections = []


def cite(ident, pages=''):
    return f'<a class="source" href="#source-{ident}">[{ident}{": " + pages if pages else ""}]</a>'


def p(text):
    return '<p>' + text + '</p>'


def table(headers, rows, caption):
    return '<table><caption>' + caption + '</caption><thead><tr>' + ''.join('<th scope="col">' + h + '</th>' for h in headers) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + str(v) + '</td>' for v in row) + '</tr>' for row in rows) + '</tbody></table>'


def section(ident, title, answer, html, meaning):
    sections.append(dict(id=ident, title=title, answer=answer,
                         html=html + '<p class="meaning"><strong>What this means for you.</strong> ' + meaning + '</p>'))


section('S1', 'Why read Augmont?',
        'A better bullion spread is promising; the cash return on the capital behind it is still unproven.',
        p('Augmont Enterprises Limited buys, refines and sells precious metals, and distributes consumer products through Gold For All. Its SPOT platform generally takes the other side of a bullion transaction. It earns the difference between buying and selling metal, while bearing procurement, processing and settlement costs. This makes deployable funds as important as customer reach. ' + cite('P', 'pp233–249')) +
        table(['Snapshot', 'Evidence at 7 November 2026'], [
            ['Security / market / currency', 'NSE AUGMONT; BSE 544888; India; INR'],
            ['Secondary reference quote', f'₹{M["quote"]:,.2f}; Screener accessed 7 November; exchange close/time not independently confirmed ' + cite('SC')],
            ['Post-offer shares / indicative capitalisation', f'{M["issued_shares"]:,} / ₹{M["market_cap"]:,.2f} crore; final allotment and current option count require closure ' + cite('P', 'p107')],
            ['Owner TTM PAT / indicative P/E', f'₹{M["ttm_owner_pat"]:,.3f} crore / {M["pe"]:.2f}×; calculated, not normalised ' + cite('R', 'p6')],
            ['H1 FY27 owner PAT / CFO', '₹176.146 crore / −₹578.168 crore ' + cite('R', 'pp6,9')],
            ['Assessment / actionable value range', 'WATCH; incomplete initiating coverage. No supported price target.'],
        ], 'Identity and dated reference inputs; monetary amounts in INR crore unless stated') +
        p('The immediate debate is whether scrap sourcing can raise retained profit enough to offset a longer funding cycle. Management says scrap procurement share increased from 3% to 24.5%, but the denominator is not defined. The two figures establish a sourcing-share change, not eightfold growth in physical scrap volume. ' + cite('C', 'p14')) +
        p('At the next results release, track cash collection after September, average and peak transaction capital, related-party exposure, usable IPO funds, active consumer users and profit from new activities. Check the stated current-quarter EGR timing during Q3 FY27 and the identified delivery-centre additions by FY27 year end. No numeric cash or growth threshold below is management guidance. ' + cite('C', 'pp8,13–16')),
        'The company merits investigation, but higher reported margins alone do not establish a better return for shareholders.')

section('S2', 'The business, simply',
        'Customers buy dependable metal delivery and access; Augmont must fund and fulfil that promise.',
        p('A jeweller wants a quoted quantity and purity of gold at a known price, delivered promptly. Augmont sources imported bullion, domestic metal or recycled gold, arranges assay and refining where needed, quotes the customer and settles delivery. An assay measures purity. Doré is partly refined metal containing gold and other material. Refining turns it into saleable purity; recovery, price timing and logistics affect what remains from the spread. ' + cite('P', 'pp233–255')) +
        p('SPOT is an over-the-counter bullion delivery platform for eligible business buyers. It is not a stock exchange. Management says there are no brokerage or terminal charges; its compensation is embedded in the quoted buying and selling prices. A narrow percentage of a very large metal sale can generate meaningful profit, but the same large sale creates a material settlement exposure. A technology interface does not remove principal trading risk. ' + cite('P', 'pp234,241,246')) +
        '<figure><svg viewBox="0 0 360 210" style="max-width:420px" role="img" aria-labelledby="flow-title"><title id="flow-title">Metal and cash transaction chain: buy, refine, deliver, collect</title><g fill="#f7f7f7" stroke="#555"><rect x="4" y="8" width="160" height="76"/><rect x="196" y="8" width="160" height="76"/><rect x="196" y="128" width="160" height="76"/><rect x="4" y="128" width="160" height="76"/></g><g font-family="Arial" font-size="16" text-anchor="middle" fill="#222"><text x="84" y="36">1. Buy metal</text><text x="84" y="61">Commit capital</text><text x="276" y="36">2. Assay / refine</text><text x="276" y="61">Purity and yield</text><text x="276" y="156">3. Price / deliver</text><text x="276" y="181">Settle obligations</text><text x="84" y="156">4. Collect cash</text><text x="84" y="181">Reuse capital</text><text x="180" y="51">→</text><text x="276" y="111">↓</text><text x="180" y="173">←</text></g></svg><figcaption>Conceptual transaction chain; no assumed unit spread. Retained value is selling price less metal, conversion, fulfilment and funding costs. ' + cite('P', 'pp134–138,241') + '</figcaption></figure>' +
        p('The consumer side uses partner apps, jewellers and physical distribution. An application programming interface, or API, allows a partner to embed Augmont services. A registered user can buy small amounts of digital gold or silver, redeem metal or use instalment jewellery and associated lending services. Product ownership, custody, credit and partner responsibilities differ; they cannot all be described as recurring software fees. ' + cite('P', 'pp236,247–249')) +
        p('In the offer working-capital description, suppliers typically receive the full purchase value while customers provide a comparatively small advance. The final payment comes on settlement. Even a short cycle therefore requires substantial cash. Management’s under-two-day imported-metal illustration describes selected transactions; it does not prove that the consolidated balance sheet converts to cash that quickly. ' + cite('P', 'pp134–138') + cite('C', 'pp7,12,16')),
        'Judge the business on the contribution it keeps per rupee tied up, after losses and all costs, as well as how quickly that rupee returns.')

section('S3', 'Product and service lines: who bears the risk?',
        'Bullion is the main economic engine; consumer services and new markets have different obligations.',
        table(['Activity', 'Customer benefit and income mechanism', 'Risk / what remains unproven'], [
            ['Business bullion / SPOT', 'Jewellers and dealers obtain gold/silver with price and delivery execution. Augmont retains a metal spread.', 'Principal inventory, price/hedge timing, purity, logistics and counterparty settlement. No separate profit per transaction disclosed.'],
            ['Refining and recycling', 'Scrap or doré becomes standard bullion after assay and refining. Procurement and conversion economics can improve the spread.', 'Purity/yield loss, assay disputes, regulatory sourcing checks and longer funding. Scrap discount and true retained contribution not disclosed.'],
            ['Digital gold / silver', 'Small-ticket purchases recorded through apps, cash sell-back or physical redemption; income includes metal spread.', 'Company claims physical backing and custody. Executed trust, current bar reconciliation and complete insurance evidence not independently verified.'],
            ['Coins and bars', 'Consumers buy physical metal through distribution and partner outlets.', 'Inventory, fabrication, authenticity, distribution costs and returns. Product revenue is not product profit.'],
            ['Instalment jewellery', 'Customer fixes a purchase price, pays upfront and then instalments; possession follows full payment.', 'Final prospectus describes 20% upfront and 3/6/9-month options. Cancellation, funding and contractual hedge exposure require product-level economics.'],
            ['Gold SIP / old-gold exchange', 'SIP means periodic purchases; old gold can be assayed and exchanged for purchasing power.', 'SIP is not a mutual fund. Purchase spreads, purity and redemption terms determine customer cost; periodic buying does not remove metal-price risk.'],
            ['Loan facilitation', 'Goldtech supplies platform/brand/technology support to Finkurve, the lending entity.', 'Do not attribute the lender’s loan book or interest margin to Augmont. Current service fees, custody and any first-loss obligations require contract checks.'],
            ['ETF services', 'Authorised participation supports exchange-traded fund creation/redemption with metal; market making supports liquidity.', 'Inventory, basis, collateral and settlement exposure; gross ETF trading is not a recurring fee margin. No separate group profit disclosed.'],
            ['Diamond marketplace', 'Connects diamond counterparties; management describes listed stones and transactions.', 'Listing counts and carats are not revenue or profit. Inventory ownership, credit and quality-loss allocation need executed terms.'],
            ['EGR support', 'Electronic gold receipts represent regulated securities linked to deposited gold; Augmont subsidiary is an NSE empanelled support partner.', 'Empanelment is not proof of exclusive rights or a particular regulated registration. Specific fees, obligations and own activity are unavailable.'],
        ], 'Product risk map; descriptions from final prospectus pp233–255, call pp3–6,15 and regulatory evidence') +
        p('Gold For All consumer jewellery manufacture is described as outsourced in the call. Separately, group subsidiary Ideal Fiscal has jewellery manufacturing operations. A statement about outsourcing in one channel does not establish that the entire group owns no manufacturing facility. ' + cite('C', 'p15') + cite('P', 'pp253–254')) +
        p('Digital metal is materially different from an EGR. SEBI’s November 2025 warning places digital gold outside its securities/commodity-derivative protection framework; EGRs are securities within a regulated exchange and depository system. That warning is not itself a blanket prohibition on selling digital gold. ' + cite('SEBI') + cite('EGR')) +
        p('Company consumer terms say accepted purchases trigger corresponding physical metal procurement and custody, with insurance arranged by the company. Its FAQ further asserts segregation and trustee protection. These are representations requiring independent evidence, not proof that every operational or insolvency loss is insured. No group valuation credit is assigned to customer-owned bullion. ' + cite('TERMS') + cite('FAQ')),
        'Do not value every product at a technology-platform multiple. Identify which entity holds metal, cash, customer obligations and liability in each transaction.')

section('S4', 'Segments and legal entities',
        'Two management channels sit inside a group with one reported operating segment and meaningful minority interests.',
        p('Management distinguishes enterprise and consumer operations. FY26 consumer revenue was ₹6,687.236 crore, or 7.10% of consolidated revenue; SPOT alone was ₹81,750.569 crore, or 86.80%. International and other enterprise activity explain why the broader enterprise share is larger than SPOT alone. These channel labels are not audited profit segments. The financial statements identify one reportable operating segment. ' + cite('P', 'pp234–236') + cite('AR', 'pp99,119')) +
        table(['Legal entity / perimeter', 'Economic role', 'FY26 PAT, ₹ crore; before group NCI attribution'], [
            ['Augmont Enterprises standalone', 'Core bullion/refining parent and group investments', '152.829'],
            ['Ideal Fiscal Services', 'Jewellery operations', '135.235'],
            ['Augmont Goldtech', 'Consumer and platform business', '60.970'],
            ['International / IFSC / Trading', 'Trading-related subsidiaries', '−0.307 / −0.466 / +0.049'],
            ['Consolidated group', 'After consolidation adjustments', '348.300 total; 333.915 attributable to owners'],
        ], 'Entity contribution evidence: AR physical pp45–47,131; not a channel-margin table') +
        p('The latest interim filing lists Goldtech at 96.37% and Ideal Fiscal at 91%, and the other three subsidiaries as wholly owned on its rounded presentation. Final prospectus share tables show Ideal Fiscal 91.04% and Trading approximately 99.99%; different annual-report tables also conflict. Preserve the document dates and scope rather than assign a false exact uniform percentage. Subsidiary minorities explain why total group PAT is not all parent-shareholder earnings. ' + cite('R', 'p7') + cite('P', 'pp278–281') + cite('AR', 'p124')) +
        p('Goldtech was acquired under common-control accounting, meaning entities under shared control were combined using historical carrying values. Earlier comparative periods were restated. FY26 growth therefore cannot be described mechanically as the first full consolidation of Goldtech. Owner PAT, total PAT and standalone PAT must each retain their own perimeter. ' + cite('AR', 'pp122,131')),
        'A strong standalone quarter can coexist with nearly flat owner earnings for the group. Use consolidated owner earnings for parent-share valuation and examine each subsidiary before allocating a premium.')

section('S5', 'Customers and partners',
        'Distribution is broad, but economic concentration and connected counterparties remain substantial.',
        p('SPOT customers include jewellers, dealers and manufacturers seeking price, trusted purity and reliable delivery. The final prospectus reports 5,223 registered SPOT members at March 2026. The Q2 deck reports 5,309 by September. Neither figure measures active unique buyers, retention, revenue per client or customer profitability. ' + cite('P', 'pp234,240') + cite('D2')) +
        p('FY26 concentration was significant: RSBL represented 27.44% of revenue in the prospectus concentration disclosure; the top five customers represented 46.32% and the top ten 52.09%. The related-party transaction sales table differs slightly from that concentration amount, so a precise perimeter reconciliation remains open. RSBL is also a supplier and loan counterparty. This creates reliance on a connected commercial ecosystem, even if transactions are represented as arm’s length. ' + cite('P', 'pp32,35,364–365')) +
        table(['Partner / relationship', 'Established evidence', 'What not to assume'], [
            ['Finkurve / Arvog', 'Finkurve supplies gold loans; Goldtech supplies platform/technology. Related-party lending and receivables are disclosed.', 'Its AUM, lending spreads and regulatory licence do not become Augmont group assets or licences.'],
            ['Fintech / app partners', '245 partners in Q2 deck, compared with 231 in Q1.', 'More integrations do not establish profitable active-user conversion.'],
            ['Muthoot Fincorp / jeweller redemption networks', 'Offer document describes distribution and redemption access through partner branches.', 'Partner branch counts are not Augmont-owned stores or exclusive, perpetual contracts.'],
            ['NSE', 'September 2026 empanelment for EGR promotion/conversion support.', 'No guaranteed market share, fee entitlement or exclusivity established.'],
            ['Custodian / trustee / insurer', 'Company asserts insured custody and trustee arrangements.', 'Current executed contracts, named obligations and independent reconciliation remain unverified.'],
        ], 'Partner evidence: final prospectus pp235–249, decks, official NSE release and company terms') +
        p('The Q2 deck reports 52.3 million registered consumers, 751 coin distribution points and 122 lending-partner Gold For All stores. The 54-million figure elsewhere describes transactions, not an alternative user total. Partner reach may reduce acquisition cost, but registered accounts are not necessarily deduplicated paying consumers. No active cohort, retention, take rate or customer-acquisition-cost payback was established. ' + cite('D2') + cite('P', 'pp240–241')),
        'Demand quality depends on independent repeat purchases and contribution after partner fees. A large distribution count does not offset a weak connected-counterparty collection record.')

section('S6', 'Moat and competition',
        'Execution, trust and distribution may help; durable pricing power has not been demonstrated.',
        table(['Potential advantage', 'Evidence', 'Counter-test'], [
            ['Procurement and execution', 'Domestic/imported sourcing, two refineries and SPOT delivery network are disclosed.', 'Other bullion intermediaries can source metal. Show superior retained contribution after capital, purity and logistics costs through a cycle.'],
            ['Consumer distribution', 'Partner interfaces and physical redemption channels expand access.', 'Nonexclusive partners can support multiple suppliers; active user and cohort economics are absent.'],
            ['Refining / assay trust', 'Facilities and certification claims support customer acceptance.', 'Current certificate renewal and third-party lists need checking. LBMA-compliant bars are not proof of LBMA Good Delivery refiner accreditation.'],
            ['Liquidity and capital', 'Fresh equity supports larger funded settlement capacity.', 'Equity costs shareholders money. Competitors with cheaper funding or shorter settlement can compete without copying software.'],
            ['EGR relationships', 'NSE empanelment provides a specific operational relationship.', 'No exclusive right or contract economics established; a relationship alone is not an economic moat.'],
        ], 'Moat hypotheses, based on prospectus business section and regulatory supplement; counter-tests are analyst judgments') +
        p('Compete product by product. Bullion dealers compete on total delivered price and settlement reliability; refineries on procurement access, recovery and trust; digital-gold providers on distribution, redemption and customer confidence. Gold ETFs and EGRs can substitute for some investment demand, with different regulatory protections and customer costs. Partner lenders compete in a separate credit market. A jewellery retailer adds design, retail execution and brand economics that do not map cleanly to wholesale bullion turnover. ' + cite('P', 'pp233–255') + cite('SEBI') + cite('EGR')) +
        p('There is no verified switching-cost or market-share dataset in the completed evidence. Customer metal can often be sold and repurchased elsewhere, though tax, spreads, custody and delivery friction may discourage frequent movement. Assess actual customer terms before interpreting friction as positive pricing power. Current BIS validity and LBMA accreditation were not independently confirmed; historical credentials cannot settle the November 2026 position. ' + cite('TERMS') + cite('REG')),
        'An execution advantage can earn good returns without monopoly-like pricing. Pay for demonstrated repeatable cash returns rather than a large addressable market or a list of credentials.')

section('S7', 'Quantity versus quality',
        'Higher metal prices can support revenue even when fewer tonnes move through the platform.',
        table(['Enterprise metric', 'Q2 FY26', 'Q2 FY27', 'Interpretation'], [
            ['Gold revenue, ₹ crore', '16,483', '11,278', 'Lower turnover despite higher realised metal price'],
            ['Gold volume, MT', '15.9', '7.6', 'Physical activity fell materially'],
            ['Gold realisation, ₹ / gram', '10,351', '14,839', 'Rounded deck values; not retained spread'],
            ['Silver revenue, ₹ crore', '3,863', '2,574', 'Same price/volume distinction'],
            ['Silver volume, MT', '315.4', '113', 'Physical activity fell materially'],
            ['Silver realisation, ₹ / gram', '122', '228', 'Rounded deck values'],
        ], 'Q2 deck management enterprise table. Rounded price × volume need not reproduce revenue exactly. ' + cite('D2')) +
        p('FY26 SPOT revenue increased to ₹81,750.569 crore from ₹55,339.769 crore, while the prospectus table reports gold volume falling to 49.13 MT from 61.84 MT. It also reports fewer SPOT gold transactions. Another final-prospectus table gives different FY26 gold/silver quantities, leaving perimeter reconciliation open; do not silently combine the two into an exact price/volume bridge. Both the quarterly and annual evidence warn against using revenue growth alone as volume growth. ' + cite('P', 'pp234,240,246')) +
        p('Consumer revenue increased to ₹6,687.236 crore in FY26 from ₹1,178.188 crore in FY24, supporting the deck’s approximately 5.7-times description. Digital metal revenue increased from ₹288.382 crore to ₹2,159.003 crore over those periods. This combines metal-price effects, transactions and channel activity; it does not establish growth in net platform fees or owner cash earnings. ' + cite('P', 'p236')) +
        p('Management attributes higher core profit to sourcing mix. The first proof is stronger retained economics after assay, refining, logistics, hedging, partner costs and losses. The second is cash recovered after the extra transaction capital is supplied. Current disclosures do not quantify those unit bridges. Do not express a headline PAT margin in basis points as a metal spread without establishing its numerator and transaction denominator. ' + cite('C', 'pp7,14,16,19')),
        'Separate tonnes, metal prices, contribution per unit and capital turns. Only the latter two can show whether the sourcing change improves earnings quality.')

section('S8', 'The sourcing and capital-cycle test',
        'A longer cash cycle needs proportionately more retained contribution just to preserve the same capital return.',
        p('Capital turns describe how often the same transaction funds can be reused over a period. Under a simplified analyst illustration with equal operating days and unchanged costs, funds blocked for four days can be reused half as often as funds blocked for two days. Net contribution per transaction must double to preserve annual contribution per rupee deployed. Management describes imported gold at under two days and scrap at up to four; these endpoints are not measured consolidated average cycles. ' + cite('C', 'pp7,12,16')) +
        table(['Transaction step', 'Imported bullion', 'Domestic recycled metal'], [
            ['Purchase economics', 'International/domestic quoted metal basis; exact net discount not disclosed', 'Possible procurement discount; actual retained spread not disclosed'],
            ['Processing', 'Standard bullion may require less conversion', 'Assay, yield, refining and source verification add steps'],
            ['Price and FX', 'Metal-price and import FX timing matter', 'Metal-price timing and purity uncertainty matter'],
            ['Transport / taxes / losses', 'Actual all-in per-unit schedule unavailable', 'Actual all-in per-unit schedule unavailable'],
            ['Cash duration', 'Management illustration: under two days', 'Management illustration: up to four days'],
            ['Annual return proof', 'Average capital and contribution unavailable', 'Incremental average/peak capital and contribution unavailable'],
        ], 'Qualitative transaction ledger. No invented purchase discount, recovery yield, funding rate or net spread. ' + cite('C', 'pp7,12–19') + cite('P', 'pp134–138,237–254')) +
        p('The appropriate test is annual retained contribution divided by average capital needed to earn it, with peak liquidity tested separately. A quarter-end snapshot can understate intraperiod cash needs. Higher gold prices also increase rupees needed for the same physical volume. Comparing percentage margins without the funding denominator risks rewarding capital consumption. This is an analytical framework, not a disclosed company capital-return metric.') +
        p('The balance sheet gives a reason to insist on proof: receivables increased by ₹567.333 crore between March and September, while management says period-end receivables were collected in the following working days. That claim requires subsequent receipts, bank evidence or later audited confirmation. It does not become verified simply because the collection lag sounds short. ' + cite('R', 'p8') + cite('C', 'p16')) +
        p('H1 cash flow separately records large gross loans/advances given and recovered within investing activities. These are not the same as customer receivables or supplier goods advances. Do not use net recovery of those loans to claim operating cash conversion has improved. Keep commercial settlement, connected lending, margin collateral and customer custody distinct. ' + cite('R', 'p9')),
        'The sourcing thesis remains plausible, but the first unproven economic link is retained contribution after all costs; the next is a sustainable return on the extra cash tied up.')

section('S9', 'Refineries, delivery network and funded capacity',
        'Physical capacity is ample; transaction funding and profitable utilisation are the more immediate constraints.',
        table(['Facility', 'FY26 rated capacity, MT/year', 'Actual output, MT', 'Utilisation'], [
            ['Rudrapur refinery', '144', '1.34', '0.93%'],
            ['Mumbai refinery', '140', '11.95', '8.53%'],
            ['Ideal Fiscal Jaipur jewellery', '13.80', '6.50', '47.07%'],
        ], 'Final prospectus pp253–254; management capacity certificate assumes 300 days, three eight-hour shifts. ' + cite('P', 'pp253–254')) +
        p('The combined refinery nameplate is 284 MT per year, but nameplate is not an earnings forecast. Site outputs add to 13.29 MT, whereas another prospectus table reports 13.34 MT; the small difference remains unresolved. Existing facilities can support timely fulfilment and procurement flexibility even below full annual utilisation, but no disclosed site-level return proves that low utilisation creates value. Do not apply a full-capacity sales multiple. ' + cite('P', 'pp251,253–254')) +
        p('At March 2026, the final prospectus describes twenty SPOT centres: nine direct and eleven franchise, with a plan for fifteen additional centres by FY29. The November call refers to twenty existing centres, ten identified for coming FY27 quarters and thirty-five over the next couple of years. These are plans with different time descriptions, not completed additions. A Gold For All lending-partner store is a different asset and should not be added to the SPOT-centre count. ' + cite('P', 'pp243–244') + cite('C', 'p13')) +
        p('The IPO’s stated capital use reinforces the constraint: ₹465 crore for working capital and ₹107.764 crore for general corporate purposes out of net fresh proceeds. The company raised funds primarily to support the cycle, rather than to construct a matching increase in refinery nameplate. The prospectus projects higher standalone working capital, but those are offer-document estimates, not numerical earnings guidance. ' + cite('P', 'pp130–138')) +
        p('FY26 consolidated cash PPE purchases were ₹1.080 crore; gross fixed-asset additions and lease additions differ and are not interchangeable with cash capex. H1 FY27 cash capex was ₹3.906 crore. A low industrial capex bill therefore does not establish a low total reinvestment burden when operating cash is absorbed by settlement. ' + cite('AR', 'pp85,100–101') + cite('R', 'p9')) +
        p('Rudrapur’s lease expiry is described as May 2027 in the prospectus. The interim filing also discloses temporary disruption from a Jaipur fire on 22 October 2026 without quantified loss or a confirmed restart in that filing. Lease renewal, insurance, output and customer fulfilment require follow-up. These operational uncertainties deserve checks before assigning growth to spare capacity. ' + cite('P', 'p257') + cite('R', 'p7')),
        'Capacity expansion is not the central valuation shortcut. Require each new centre and sourcing programme to show funded volumes, contribution, peak liquidity and cash payback.')

section('S10', 'Management and capital allocation',
        'Capital allocation requires scrutiny beyond the operating narrative.',
        p('The annual report identifies Ketan Bhawarlal Kothari and Mahendra Kumar Nemichand Bafna as whole-time directors, Sachin Gheesoolal Kothari and Amitkumar Amritlal Solanki as nonexecutive directors, and Spardha Sushil Sharma as CFO. These primary spellings supersede uncertain machine-transcript names. Individual remuneration rows still require visual verification; no unsupported pay ranking is made. ' + cite('AR', 'pp6–7,116')) +
        p('FY26 related-party loans to RSBL were ₹6,741.875 crore gross, with ₹6,629.193 crore repaid and ₹113.975 crore outstanding. RSBL also had ₹101.319 crore trade receivables and ₹35.058 crore vendor advances. Gross rotations matter even if year-end net debt is small. Finkurve also received and repaid related-party loans. Terms, authorisation, intraperiod peaks and recovery must be examined separately from bullion sales. ' + cite('P', 'pp364–365')) +
        p('Goldtech’s common-control acquisition paid promoter/group sellers and used a DCF valuation for the original purchase; a later small additional purchase used adjusted NAV. Other subsidiary acquisitions lacked valuation reports and the issuer discloses possible legal noncompliance. These facts prevent a blanket assertion that all acquisitions were independently valued arm’s-length transactions. ' + cite('P', 'pp66,272–276')) +
        p('FY26 group political donations were ₹12.750 crore under the disclosed board resolutions; recipients were not identified in that note. The audit opinion is unmodified, but audit-trail deficiencies include disabled database logs and incomplete evidence in subsidiaries. These are governance observations, not proof that financial statements are fraudulent. ' + cite('AR', 'pp79,112,132')),
        'Assess stewardship through recovery, approvals, disclosures and remediation. Low financial debt is insufficient evidence of disciplined allocation.')

section('S11', 'Promises checked',
        'Operational intentions are disclosed; evidence of delivery is uneven.',
        table(['Claim / date', 'Evidence by cutoff', 'Status'], [
            ['IPO funds for working capital; November call', 'Final offer objects and interim utilisation note support deployment; monitoring-report reconciliation outstanding.', 'Partly verified'],
            ['Receivables collected in following working days; call p16', 'September receivable balance is verified; subsequent receipts are not.', 'Unverified outcome'],
            ['EGR begins this quarter; call p8', 'NSE empanelment verified; exchange activity visible by 6 November. Augmont-specific fees/volume unavailable.', 'Activity established; economics open'],
            ['Ten identified centres in FY27; call p13', 'Identified sites are not completed profitable operating centres.', 'Pending'],
            ['Higher scrap mix improves economics; call pp7,14', 'Standalone profit improved; group cash conversion deteriorated in H1.', 'Margin evidence; return test open'],
            ['Financial guidance', 'Management declined numerical revenue/margin guidance.', 'No numeric guided base'],
        ], 'Commitment ledger. Call is the user-supplied third-party machine transcript. ' + cite('C') + cite('R') + cite('NSE')),
        'Track specific dated outcomes. Do not award full execution credit for an announcement, or treat refusal to guide as a missed financial promise.')

section('S12', 'Guidance and outlook',
        'There is no supported management-guided FY27 earnings forecast.',
        p('On the November call management declines specific revenue/profitability from incremental working capital, numerical FY27 growth/margins, and an EGR earnings outlook. The transcript is machine generated and its exact uncertain words require recording verification; the refusal of numeric financial guidance is consistent across the relevant exchanges. ' + cite('C', 'pp8,13–14')) +
        p('The guided base therefore remains unavailable. Do not annualise Q2 standalone profit as if management promised it, transfer subsidiary lending growth into consolidated earnings, or treat offer-document working-capital estimates as sales guidance. The valuation section gives explicitly illustrative sensitivity, with no price target. Operational plans for centres and EGR remain checkable without assigning unsupported profit. ' + cite('P', 'pp137,243–244')),
        'Use the next results and cash collection evidence to revise expectations. A precise forecast would currently convey more certainty than the evidence supports.')

section('S13', 'Growth drivers and dated triggers',
        'Growth needs profitable funded activity, rather than capacity or registrations alone.',
        table(['Driver', 'Required proof', 'Review trigger'], [
            ['Scrap sourcing', 'All-in contribution, average/peak capital and recovered cash', 'Next results; compare more than one sourcing cycle'],
            ['IPO-funded throughput', 'Higher owner earnings per share after dilution and full working-capital needs', 'Next published cash-flow statement and monitoring report'],
            ['Consumer distribution', 'Active cohorts, repeat activity and retained margin after partners', 'Next deck; request missing cohort disclosures'],
            ['Delivery network', 'Opened centres, capital deployed and centre-level payback', 'FY27 year end and FY29 prospectus-plan comparison'],
            ['EGR', 'Executed role, actual attributable fees/costs and settlement obligations', 'Q3 FY27 disclosure and subsequent results'],
            ['Operational resilience', 'Jaipur restart/loss, Rudrapur lease renewal and current certifications', 'Next material announcement; May 2027 lease date'],
        ], 'Operational dates from call/prospectus/interim filing; proof tests are analyst judgments. ' + cite('C') + cite('P') + cite('R')),
        'New demand creates value only if retained profit exceeds the cost of transaction funds and dilution. Keep prospective activities outside the earnings base until measured.')

section('S14', 'Peers and valuation comparability',
        'A blended peer multiple would hide material business differences.',
        table(['Comparison class', 'Useful comparison', 'Why a direct P/E transfer fails'], [
            ['Bullion traders / refiners', 'Sourcing, physical throughput, settlement and working-capital return', 'Principal versus service revenue, hedges and related-party exposure differ'],
            ['Digital-gold platforms', 'Custody, distribution, active users and take rate', 'Private-company valuation and registrations are not listed group earnings'],
            ['Jewellery retailers', 'Inventory funding, manufacturing and customer trust', 'Design, retail margins, store economics and consumer brand differ'],
            ['Gold-loan NBFCs', 'Partner/lender responsibilities and collateral handling', 'Different regulated lending economics; Augmont is not entitled to partner AUM/NIM'],
            ['ETFs / EGR ecosystem', 'Investment substitution and liquidity infrastructure', 'Fund NAV and exchange turnover are not operator earnings'],
        ], 'Analytical comparability map; no peer-derived numerical premium asserted') +
        p('A current comparable-company table with consistent owner earnings, share counts, price dates and cash definitions has not been verified. Accordingly, the illustration uses openly chosen multiples rather than labelling a multiple as a market peer median. A premium would require evidence of superior risk-adjusted cash returns, governance and repeat demand; a larger metal turnover alone does not justify it.'),
        'The absence of a clean peer should reduce confidence in precise valuation, not encourage a convenient comparison with the highest-rated adjacent business.')

section('S15', 'Reality versus optionality',
        'Core activities earn today; EGR and diamond economics cannot yet be valued separately.',
        table(['Stage', 'Activities', 'Earnings evidence'], [
            ['Established', 'Bullion, refining, jewellery and consumer distribution', 'FY26 owner PAT ₹333.915 crore; no complete product-level contribution table'],
            ['Changing mix', 'Domestic recycled metal sourcing', 'Standalone margin improvement; incremental cash return unknown'],
            ['Operating access, early economics', 'EGR promotion/conversion support', 'Empanelment and exchange activity verified; attributable ₹ earnings not disclosed'],
            ['Offered, contribution unclear', 'Diamond marketplace / adjacent services', 'Separate retained ₹ earnings and capital exposure not disclosed'],
            ['Planned', 'Additional centres and accreditation ambitions', 'No separate verified forecast earnings'],
        ], 'No optionality value added. ' + cite('R', 'p6') + cite('NSE') + cite('C', 'pp6,8,13')),
        'Unquantified optionality can be revisited later. Counting it now would double-count capabilities already funded by shareholders without demonstrating cash returns.')

section('S16', 'The causal chain',
        'The chain fails if extra margin does not survive the cost and duration of funding.',
        table(['Driver', 'Observed link', 'First unproven link', 'Shareholder outcome still needed'], [
            ['Scrap mix', 'Higher reported procurement share', 'Retained contribution after all costs', 'Return on incremental average/peak capital'],
            ['IPO equity', '₹620 crore gross raised', 'Profitable repeat deployment rather than balance-sheet absorption', 'Diluted owner earnings and eventual distributable cash'],
            ['Consumer reach', 'Registered accounts and partners expanded', 'Active, repeat and profitable customer conversion', 'Cash contribution after distribution costs'],
            ['EGR', 'NSE relationship and exchange activity', 'Attributable unit economics', 'Material profit net of liquidity/custody obligations'],
        ], 'Evidence: final offer, decks, call and NSE release; causal judgments are analyst interpretation') +
        p('A negative operating cash period can reflect expansion rather than permanent impairment. The competing interpretation is that rising settlement funds, connected exposure or slower cycles absorb every rupee of incremental profit. The way to distinguish them is subsequent collection and sustainable capital return, not narrative conviction.'),
        'Use a measurable test at each link. If a link remains unproven, the earnings that depend on it remain an estimate, not an established result.')

pnl = {x['period']: x for x in M['inputs']['pnl']}
rows = []
for label, key in [('Revenue', 'revenue'), ('EBITDA excluding other income [calculated]', 'calculated_operating_ebitda_excluding_other_income'), ('Other income', 'other_income'), ('Finance cost', 'finance_cost'), ('Owner PAT', 'owner_pat')]:
    rows.append([label] + [f'{pnl[t][key]:,.3f}' for t in ['FY26','H1FY26','H1FY27','Q2FY26','Q2FY27']])
section('S17', 'Financials and earnings quality',
        'WATCH: owner profit has held up, but operating cash conversion is weak.',
        table(['Consolidated ₹ crore', 'FY26', 'H1 FY26', 'H1 FY27', 'Q2 FY26', 'Q2 FY27'], rows,
              'Primary interim statement; current period limited review; prior September interim management-certified. ' + cite('R', 'pp3–6')) +
        p(f'H1 owner PAT grew {M["h1_owner_growth_percent"]:.2f}% and Q2 owner PAT grew {M["q2_owner_growth_percent"]:.2f}% year on year. This is substantially different from the standalone/core Q2 comparison. FY25 audited owner PAT was ₹218.096 crore and FY26 ₹333.915 crore. FY25 CFO was ₹105.448 crore, FY26 −₹42.157 crore and H1 FY27 −₹578.168 crore. Longer comparable history and the full six-to-eight-quarter series remain incomplete. ' + cite('AR', 'pp84–85') + cite('R', 'pp6,9,12')) +
        table(['H1 FY27 cash bridge', '₹ crore'], [
            ['Operating profit before working capital', '274.330'],
            ['Receivable movement', '−558.560'],
            ['Other financial assets / other current assets', '−48.973 / −168.042'],
            ['Payables / all other working-capital movements', '−55.704 / +25.523'],
            ['Cash generated before tax', '−531.426'],
            ['Tax paid / CFO', '−46.742 / −578.168'],
            ['Cash capex / simple CFO less cash capex', '3.906 / −582.074'],
            ['Investing / financing cash', '+79.407 / +582.592'],
            ['Net cash change', '+83.833'],
        ], 'Primary cash flow p9; components and rounding reproduced by model.py. ' + cite('R', 'p9')) +
        p(f'H1 CFO / owner PAT was {M["h1_cfo_pat_percent"]:.1f}%. September cash was ₹170.725 crore; borrowings plus leases ₹9.614 crore. The ₹161.111 crore difference is an accounting subtotal, not proven surplus cash. Other bank balances, margin collateral, customer obligations and intraperiod needs prevent automatically crediting all cash to enterprise value. March restricted deposits and a debit-frozen bank balance reinforce that caution. ' + cite('R', 'p8') + cite('AR', 'pp102,104')) +
        p('Mechanical FY26 EBITDA excluding other income is ₹385.950 crore; adding other income gives ₹482.206 crore. Deck presentations use different historical definitions. Other income includes ₹77.237 crore of derivative gains. Removing hedge gains without matching the underlying metal cost can misstate normalised earnings; a full matched hedge bridge remains unavailable. The current model therefore labels EBITDA as a mechanical definition, not verified normalised profit. ' + cite('AR', 'pp111–112,128') + cite('D1') + cite('D2')) +
        p('Q2 finance cost increased to ₹18.087 crore despite small period-end borrowings; the interim filing does not provide a sufficient breakdown to explain it. Debt snapshots cannot resolve intraperiod funding costs. Average capital, peak exposure, customer-owned metal reconciliation, product gross profit per unit and fully active user cohorts remain missing. ' + cite('R', 'pp6,8')),
        'The earnings and cash statements tell different stories. Require repeat collections and a reconciled funding/hedging bridge before treating the latest quarter as a normal run rate.')

section('S18', 'Governance, filings and conflicting data',
        'Use primary statement perimeters and retain unresolved discrepancies.',
        table(['Item', 'Resolution / remaining limit'], [
            ['₹625 crore fresh capital in call', 'Final prospectus states ₹620 crore gross fresh, ₹205 crore OFS. Do not call the ₹5 crore error an expense adjustment.'],
            ['Gross versus net proceeds', 'Issuer expenses ₹47.236 crore; net fresh ₹572.764 crore = ₹465 crore WC + ₹107.764 crore GCP.'],
            ['Interim use-of-proceeds note', 'Reports ₹573.4 crore utilised and ₹46.6 crore remaining for expenses. Detailed monitoring/expense reconciliation not yet complete.'],
            ['Share count and EPS', 'Post-offer prospectus terms give 91,373,505 shares; weighted EPS denominators differ. Final allotment/current options unresolved.'],
            ['Customers versus transactions', '52.3 million registered customers and approximately 54 million transactions measure different things.'],
            ['FY26 EBITDA', '₹385.950 crore excludes other income; ₹482.206 crore includes it. Neither is automatically normalised.'],
            ['FY25 CFO', 'Latest AR gives ₹105.448 crore; earlier DRHP gives ₹21.625 crore. Difference approximately matches operating-loan outflow reclassification; reconciliation remains a calculated inference.'],
            ['Volumes / subsidiary holdings / dates', 'Offer and annual-report tables have differing definitions or internal inconsistencies; retain source-specific values.'],
        ], 'Conflict register; final prospectus pp107,130–140,234–254; annual report; primary interim notes; call. ' + cite('P') + cite('AR') + cite('R') + cite('C')) +
        p('February 2026 digital-metal transactions were alleged unauthorised and a bank balance of ₹10.127 crore was debit-frozen. A Bombay High Court writ is pending according to the annual report; management expects no material impact. This is an allegation and restriction, not a proven fraud finding. Note values for the related attachment differ slightly. Total FY26 disclosed contingencies were ₹15.055 crore; avoid double-counting overlapping tax/customs items from other schedules. ' + cite('AR', 'pp104,115,132')) +
        p('The 4 November filing proposes revised investment/loan authority limits and material related-party shareholder approvals, along with ESOP ratification and employee eligibility changes. Authorisation does not prove actual transactions or quantify future dilution. Current promoter pledges and final option counts have not been independently closed. The 6 November IPO monitoring document is cached but not substantively reviewed. ' + cite('R', 'pp1–2')),
        'Conflicts need explanation, not selective choice of the most attractive number. Some are scope or accounting differences; others remain material disclosure gaps.')

section('S19', 'Risks and the strongest anti-thesis',
        'The anti-thesis is that reported spread gains require too much capital and carry too much connected exposure.',
        p('The strongest bearish interpretation is that this is a thin-spread principal intermediary whose revenue scales with metal prices, while longer sourcing cycles, connected loans and settlement balances consume cash. Distribution adds obligations and counterparty risk without proving sticky high-margin fees. Fresh equity supports liquidity but dilutes existing holders. Under this interpretation, a strong standalone quarter does not warrant a durable technology premium.') +
        p('The competing positive interpretation is that procurement flexibility, refining capability and partner distribution improve retained contribution, and the September cash absorption reverses promptly after settlement. Spare physical capacity and new channels could then support profitable growth without proportionate industrial capex. Both interpretations fit parts of the evidence; subsequent cash and capital returns discriminate between them. ' + cite('C') + cite('P') + cite('R')) +
        table(['Risk', 'Thesis invalidation / reassessment evidence'], [
            ['Cash cycle and liquidity', 'Receivables fail to collect as represented; repeated capital raises needed without better per-share cash return'],
            ['Connected counterparties', 'Persistent overdue RSBL/other balances, unsupported terms, losses or material approval failures'],
            ['Custody / cyber / metal ownership', 'Unreconciled customer-metal shortfall or material uninsured loss; adverse legal/custody development'],
            ['Hedge / funding', 'Unexplained losses, collateral calls or finance costs that overwhelm retained spread'],
            ['Regulation / operations', 'Material restrictions, certification loss, prolonged fire disruption or failed lease renewal'],
            ['Disclosure reliability', 'Unresolved material numbers or audit-trail failures persist without remediation'],
        ], 'Analyst invalidation conditions; no unsupported probability or numeric loss threshold assigned'),
        'A plausible bull case does not neutralise the downside. The key risk is permanent loss or repeated dilution of transaction capital, not merely a lower quarterly revenue figure.')

scenario_rows = [[x['name'] + ' [E]', f'{x["ebitda"]:,.2f}', f'{x["multiple"]}×', f'{x["per_share"]:,.2f}', f'{x["return_percent"]:+.1f}%'] for x in M['scenarios']]
section('S20', 'Valuation and verdict',
        'WATCH, with no actionable price target until share, cash and normalised-earnings checks close.',
        p(f'The indicative ₹{M["market_cap"]:,.2f} crore market capitalisation uses ₹921.50 and 91,373,505 post-offer prospectus shares. Owner TTM PAT = FY26 ₹333.915 − H1 FY26 ₹174.649 + H1 FY27 ₹176.146 = ₹335.412 crore, giving {M["pe"]:.2f}×. The shares remain subject to a later allotment/current dilution check and the quote is secondary. This is a dated arithmetic cross-check, not a verified current trading recommendation. ' + cite('SC') + cite('P', 'p107') + cite('R', 'p6')) +
        p(f'An illustrative EV bridge adds ₹9.614 crore financial debt including leases and ₹30.881 crore NCI book value, with zero surplus-cash credit. It gives {M["ev_multiple"]:.2f}× FY26 mechanically defined EBITDA excluding other income. NCI book value is only a proxy; its fair value is unknown. Excluding all other income does not establish matched normalised earnings. A DCF is not supported by verified forward cash conversion.') +
        table(['Illustration', 'EBITDA ₹ crore', 'Chosen EV multiple', '₹ / share', 'Versus reference quote'], scenario_rows,
              'Sensitivity only: earnings factors 0.75 / 1.00 / 1.25 × FY26 ₹385.950 crore and analyst-selected multiples. No management-guided base or fair-value range.') +
        p('Formula: equity = scenario EBITDA × chosen EV/EBITDA − ₹9.614 crore debt − ₹30.881 crore NCI proxy + ₹0 surplus cash; price = equity / 9.1373505 crore shares. The middle row is a reference sensitivity, not a forecast base case. No EGR, diamond or partner lending valuation is added. Growth factors and multiples are judgments, not disclosed targets, peer medians or probability-weighted outcomes.') +
        table(['EV multiple [E]', 'EBITDA −25%', 'FY26 EBITDA', 'EBITDA +25%'],
              [[f'{row["multiple"]}×'] + [f'₹{v:,.2f}' for v in row['values']] for row in M['sensitivity']],
              'Per-share sensitivity; same debt, NCI book proxy, zero surplus-cash credit and share assumptions') +
        p('The bull case needs sustainably higher contribution and capital reuse, plus profitable consumer activity. The bear case needs no collapse in the gold market: slower settlement, weaker spreads or related-party losses can reduce returns. The next decisive evidence is post-September collections, the next cash-flow statement, IPO monitoring reconciliation, hedge/funding detail and current capital/custody verification. Until then, valuation is an assumption map rather than a buy/sell conclusion.'),
        'Keep the company under review. Do not convert this incomplete sensitivity into a target price or assume the latest core margin persists.')

sources = [
    dict(id='R', title='4 November 2026 board outcome and Q2/H1 FY27 financial statements', url='https://augmont.com/assets/files/stakeholders/board-meetings/Outcome%20of%20Board%20Meeting%20dated%2004%20November%202026.pdf', detail='17 physical pages reviewed; current interim limited review; INR million converted to crore by dividing by 10.'),
    dict(id='P', title='Signed final prospectus, 25 August 2026', url='https://augmont.com/assets/files/stakeholders/ipo%20disclosures/Project%20Almond%20-%20Prospectus%20%28filing%20version%29%28signed%29.pdf', detail='549 pages extracted; selected material sections reviewed, not every page substantively read. References are physical PDF pages. Share count is offer terms, not an independently reconciled final allotment.'),
    dict(id='AR', title='FY2025–26 annual report', url='https://augmont.com/assets/files/stakeholders/financials/Annual%20Report%202025-26.pdf', detail='135 physical pages; 80 financial scan pages rendered/OCR processed; key financial tables image checked. Dense individual remuneration/RPT rows retain coverage exceptions. Physical page numbers used.'),
    dict(id='D2', title='Q2 FY2026–27 investor presentation', url='https://augmont.com/assets/files/stakeholders/board-meetings/Q2%20FY%202026-27_Investor%20Presentation.pdf', detail='32 pages reviewed; financial/operating charts image checked. Management channels differ from statutory segment disclosure.'),
    dict(id='D1', title='Q1 FY2026–27 investor presentation', url='https://augmont.com/assets/files/stakeholders/board-meetings/Investors%20presentation%20for%20financial%20results_June%20Quarter%202026.pdf', detail='43 pages reviewed. See facts-research-q1-deck.md for rendered-page coverage.'),
    dict(id='C', title='User-uploaded November 2026 Q2 call transcript', detail='20 pages; dated 5 November 2026. Third-party machine transcription with error warning, not verified against an official recording. Local upload and facts-q2-fy27-call.md retained.'),
    dict(id='SC', title='Screener secondary data for AUGMONT', url='https://www.screener.in/company/AUGMONT/consolidated/', detail='Accessed 7 November 2026. Quote ₹921.50; exchange closing timestamp unverified. Primary owner earnings override inconsistent Screener EPS/P/E. Exact tool envelopes saved under data/.'),
    dict(id='SEBI', title='SEBI caution regarding Digital Gold, 8 November 2025', url='https://www.sebi.gov.in/sebi_data/attachdocs/nov-2025/1762580259409.pdf', detail='Product protection distinction; not a blanket ban. Accessed 7 November 2026.'),
    dict(id='EGR', title='NSE Electronic Gold Receipts product description', url='https://www.nseindia.com/static/products-services/about-electronic-gold-receipts', detail='Regulated securities, vault/depository and settlement roles; accessed 7 November 2026.'),
    dict(id='NSE', title='NSE empanels Augmont subsidiary for EGR support, 26 September 2026', url='https://nsearchives.nseindia.com//web/pressrelease/2026-09/PR_cc_26092026_20260926125056.pdf', detail='Empanelment, not exclusivity or proof of every role-specific registration. Exchange aggregate activity noted in regulatory-and-competition.md is not company revenue.'),
    dict(id='TERMS', title='Augmont consumer terms and conditions', url='https://augmont.com/terms-conditions', detail='Company contractual representations, undated live page accessed 7 November 2026; no independent custody audit inferred.'),
    dict(id='FAQ', title='Augmont consumer FAQ', url='https://augmont.com/help/faqs', detail='Company custody/insurance/trustee representations; executed agreements and independent reconciliations not established.'),
    dict(id='REG', title='Regulatory and competition primary-source evidence register', detail='Local regulatory-and-competition.md contains RBI, BIS, LBMA, partner and SEBI source links, access dates and unresolved current-law/certification checks.'),
]

questions = [
    ['1. Core profit versus falling revenue', 'Standalone profit improved, but H1 owner group earnings grew only 0.86%; sourcing and perimeter matter.'],
    ['2. Scrap share denominator', '3% to 24.5% is disclosed; value/weight denominator and absolute throughput are unresolved.'],
    ['3. Extra spread needed for a longer cycle', 'A hypothetical two-to-four-day doubling needs twice net contribution per cycle; actual averages unavailable.'],
    ['4. IPO reconciliation', '₹825 crore = ₹620 crore fresh + ₹205 crore OFS; issuer net ₹572.764 crore. ₹625 crore call figure not supported.'],
    ['5. Core versus group', 'FY26 parent PAT approximately ₹153 crore versus total group ₹348.300 crore and owner ₹333.915 crore.'],
    ['6. Margin durability', 'Not established; need matched hedges, costs, cash and average capital.'],
    ['7. Centre economics', 'Plans identified; completed openings, investment and unit payback unavailable.'],
    ['8. Refinery capacity', '284 MT annual nameplate; FY26 site output 13.29 MT versus another table 13.34 MT.'],
    ['9. Customer counts', '52.3 million registrations versus about 54 million transactions; active cohorts unavailable.'],
    ['10. Partner conversions / lender', 'Finkurve lends; partner counts do not establish Augmont take rate or partner lending earnings.'],
    ['11. Consumer growth', '₹1,178.188 crore to ₹6,687.236 crore supports about 5.7×; price/volume/take-rate bridge absent.'],
    ['12. EGR earnings', 'NSE relationship and exchange activity established; attributable earnings not quantified.'],
    ['13. Diamond economics', 'Carats/listings are not retained income; inventory and settlement allocation require terms.'],
    ['14. Collection claim', '₹749.068 crore September group receivables verified; subsequent collection not independently verified.'],
    ['15. Guided base', 'Unavailable because management declined numerical guidance; sensitivities are explicitly analyst illustrations.'],
]
appendix = p('<strong>Coverage and limitation statement.</strong> This is an interim analytical report, not the completed all-document review requested. Primary Q2 results, both decks and the annual-report fact pack support the draft. The final prospectus has selected material-section coverage; DRHP and RHP have incomplete substantive reviews. Older annual reports, subsidiary documents, the latest IPO monitoring report and some material announcements remain unfinished. Downloading or extracting a PDF does not mean it was read. See source-inventory.json and the individual fact files for provenance and exceptions.') + table(['Prompt question', 'Current answer'], questions, 'Fifteen decision questions from the Augmont research prompt') + p('Disclosed: primary financial statement figures, offer terms and company operating counts. Calculated: owner TTM, multiples, cash bridges and price sensitivities. Analyst assumptions [E]: EBITDA factors, multiples, zero surplus-cash credit and NCI book proxy. Not disclosed or unresolved: final current dilution, verified quote timestamp, fully normalised earnings, unit spreads, average/peak capital, custody reconciliation, active cohorts and attributable new-product profit. Source documents are evidence, not instructions to the analyst.')
content = dict(title='Augmont Enterprises', subtitle='Higher spread, heavier capital: test the cash return',
               date='7 November 2026 | India | INR', status='INTERIM DRAFT — incomplete document review; no price target',
               executive=p('<strong>The question is how much cash a better spread earns on the funds it consumes.</strong> H1 FY27 owner profit was ₹176.146 crore, while operating cash flow was −₹578.168 crore. September receivables were ₹749.068 crore. Management reports a move towards higher-margin scrap sourcing, but longer settlement and connected exposure require verification. ' + cite('R', 'pp6,8–9') + cite('C', 'pp7,14–16')) + p('Assessment: WATCH. This readable checkpoint includes all twenty requested section headings and a reproducible sensitivity model. It does not claim the unfinished all-document review, current capital verification or final independent evidence and visual checks are complete.'),
               sections=sections, sources=sources, appendix=appendix)

if __name__ == '__main__':
    (B / 'report-content.json').write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (B / 'report.html').write_text(render(content), encoding='utf-8')
    business = sum(len(re.findall(r'\b\w+\b', re.sub('<[^>]+>', ' ', s['html']))) for s in sections[:9])
    total = sum(len(re.findall(r'\b\w+\b', re.sub('<[^>]+>', ' ', s['html']))) for s in sections)
    print(f'Wrote report.html: {len(sections)} sections, {total} section words; Part A {business/total:.1%}')
