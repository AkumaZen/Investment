# Sources and narrative. Executed within build_report.py's deterministic renderer.
SOURCES['R27']=('Q2/H1 FY27 official results, 3 Nov 2026','https://www.amanta.co.in/public/assets/pdf/Investors/exchange-announcements/amanta-outcome-of-board-meeting-held-on-03112026.pdf')
for a in json.loads((ROOT/'annual-facts.json').read_text(encoding='utf-8'))['sources']:
 short={'ipo_ma_sep26':'MA','steriport_commission':'AS','solar_commission':'AP','anil_rathi':'COO','agm_sep26':'AGM','rating_upgrade':'CR','remuneration':'PAY'}.get(a['id'],a['id'])
 SOURCES[short]=(a['title'],a['url'])
SOURCES['GF']=('Gufic official manufacturing capabilities','https://gufic.com/manufacturing/navsari-facility')
SOURCES['GS']=('Gufic standalone Screener snapshot','https://www.screener.in/company/GUFICBIO/')
SOURCES['DS']=('Denis Chem Lab standalone Screener snapshot','https://www.screener.in/company/537536/')
SOURCES['DR']=('Denis Chem Lab CRISIL rating rationale, Oct 2025','https://bsmedia.business-standard.com/_media/bs/data/announcements/bse/28102025/a0a240b8-582b-4575-b1ec-055a70638207.pdf')

# Executive is composed from the completed model and evidence, displayed first.
base28=MODEL['Base']['rows']['FY28E'];bear28=MODEL['Bear']['rows']['FY28E'];bull28=MODEL['Bull']['rows']['FY28E']
rail=h('Market reference')+table(['9 Nov 2026 close',''],[['NSE / BSE','AMANTA / 544502'],['ISIN','INE084K01015'],['Price','₹202.15'],['Issued shares','3.8829 cr'],['Equity value (calc.)',f'₹{CMP*SHARES:,.1f} cr'],['Sep debt + leases','₹203.9 cr'],['Cash equivalents','₹1.7 cr'],['EV, cash-only (calc.)','₹987.1 cr']])+src('NSE',('AR',59),('R27',4))+h('Research stance')+p('<b>WATCH / valuation-sensitive</b><br>Execution is improving. Cash conversion and the price paid remain decisive.')+h('FY28E scenario values')+table(['Illustrative value','₹/share'],[['Bear',f(bear28['price'],0)],['Base',f(base28['price'],0)],['Bull',f(bull28['price'],0)]])+p('<span class="deck">31 Mar 2028 horizon. Undiscounted scenario values, not a broker target. Assumptions and sensitivity on the final valuation pages.</span>')+h('Next evidence')+p('Q3 FY27 line sales and margin; December SVP factory acceptance; cash funding; Q1 FY28 qualified launches.')
summary=p('Amanta makes sterile liquid medicines and the containers that deliver them. Its premium SteriPort IV-fluid platform supplies the volume engine. Small-volume parenterals (SVP), especially inhalation and ophthalmic products, offer a potentially better mix. A captive solar plant can reduce electricity cost. These are three different profit mechanisms, with different evidence and timing.')+h('Capacity has arrived; earnings quality is the test')+p('The new SteriPort line began production on 2 September 2026. Capacity rose from 6.6 crore to 11.6 crore bottles a year. Q2 FY27 revenue rose 17.3% to ₹83.13 crore. Yet operating EBITDA excluding other income was only 20.7% of sales. Finance cost and depreciation still consumed roughly two thirds of that operating profit.')+src(('AS',1),('P2',5),('R27',3))+h('The stronger opportunity is also the slower one')+p('The planned SVP expansion adds 10.8 crore units and targets Q1 FY28 commissioning. Specialized tooling, formulation transfer and market registrations must follow the right sequence. Management explicitly called its ₹16 crore first-year sales illustration speculative. We do not value an unapproved glass-injectables idea or assume advanced-market approvals.')+src(('C2',5),('C2',12),('C2',14),('C2',15))+h('Debt ratios improved faster than cash generation')+p('FY26 net worth increased with the ₹126 crore gross IPO. Gross borrowings excluding leases nevertheless rose to ₹234.42 crore at March 2026, before falling to ₹194.56 crore in September. H1 FY27 operating cash of ₹21.94 crore did not cover ₹37.60 crore capex, even before interest payments classified as financing cash flows.')+src(('AR',52),('AR',53),('R27',4),('R27',5),('R27',6))+h('What the price requires')+p(f'Our conditional base illustration reaches ₹{base28["sales"]:.1f} crore sales and 25% operating margin in FY28E. At 14x operating EBITDA, the value is ₹{base28["price"]:.0f} a share versus ₹202.15 today. The result is highly sensitive to both the multiple and cash conversion. The upside requires both earnings delivery and a sustained valuation multiple.')+note('Follow sold output, contribution after input costs, and cash after interest and capex. Installed capacity alone is insufficient evidence for paying a premium.')
page('S1','Turning capacity into earnings and cash','A credible operating step-up is underway, but the current price already demands execution.', '<div class="executive"><div>'+summary+'</div><aside class="rail">'+rail+'</aside></div>',tag='Investment view',layout='cover',sources=['AS1','P2:5','R27:3-6','AR:52-53'])

page('S1','The investment argument in four exhibits','Revenue accelerated, but operating margin and capital productivity have more to prove.',
pair(exhibit('Sales are accelerating from a low first quarter',bars(['Q1 FY26','Q2 FY26','Q3 FY26','Q4 FY26','Q1 FY27','Q2 FY27'],[65.31,70.89,74.49,76.99,68.80,83.13],'Revenue, ₹ crore',height=245,maxval=100,fmt='.1f'),src('SC',('R27',3))),exhibit('New SteriPort capacity is a large discrete step',bars(['Before Line 3','After Line 3'],[6.6,11.6],'Crore bottles per year',height=245,maxval=14,fmt='.1f'),src(('P2',5),note='Capacity is not shipped volume.')))+
pair(exhibit('Operating EBITDA has barely grown over two years',bars(['FY25','FY26'],[59.6685,59.8585],'₹ crore; excludes other income',height=200,maxval=75,fmt='.1f'),src(('AR',52))),exhibit('Capex exceeded operating cash in FY26',bars(['CFO FY26','Cash capex'],[48.4464,80.1864],'₹ crore; before financing interest',height=200,maxval=100,fmt='.1f'),src(('AR',53))))+
p('Read the charts together. A new line can increase shipments quickly, but higher depreciation, financing costs and working capital can delay the benefit to owners. The next two quarters should reveal whether physical output growth is also profitable growth. The FY26 step in assets largely precedes the corresponding revenue opportunity.')+note('The thesis needs both a commercial ramp and a cash ramp. A better revenue chart without better returns on capital is incomplete.'),tag='Story in charts',sources=['SC','AR:52-53','P2:5'])

page('S2','A sterile manufacturer sells reliability with each dose','Amanta earns when qualified, usable sterile products are sold and collected, not when bottles are merely produced.',
p('A parenteral is a medicine administered by injection or infusion. Large-volume parenterals (LVP) include IV fluids used for hydration and carrying medicines. Small-volume parenterals (SVP) include water for injection, small injections and other sterile packs. Ophthalmic means eye care. Respiratory solutions are delivered through a nebuliser. These terms describe the use or dosage form, not separate listed subsidiaries.')+
exhibit('The revenue engine has five commercial gates',steps([('Formulate and validate','Make a stable medicine and demonstrate a repeatable sterile process.'),('Qualify the product','Secure the product, site and country permissions that actually apply.'),('Reach the buyer','Domestic distributors reach hospitals; export partners need market access.'),('Manufacture and release','Produce, test and release saleable batches. Rejects and downtime reduce usable output.'),('Ship and collect','Recognise sales and receive payment while funding inventories and receivables.')]),src(('AR',8),('AR',9),('P2',12),('C2',5)))+
h('Why the container matters')+p('The medicine and its delivery system are linked. SteriPort uses a two-port polypropylene bottle made through injection stretch-blow moulding (ISBM). Aseptic blow-fill-seal (BFS) forms, fills and seals a plastic container in an integrated process. The container affects compatibility, handling and the risk of contamination. Specialized tooling and validated processes can create barriers, but manufacturing automation alone does not prove superior clinical outcomes or permanent pricing power.')+src(('P2',13),('P2',16))+
h('Where the cash comes from')+p('Domestic branded products use a distribution network. Exports and product partnering add other routes to market. Product sales generated ₹281.6 crore of FY26 revenue before services and other operating items. The economic unit is a released, sold dose or bottle at a realized net price. More litres, more units and higher-value formulations need separate interpretation.')+src(('AR',65))+note('Ask which gate has been passed for each growth idea. A machine installation proves only one part of the route to cash.'),tag='Business in plain language',sources=['AR:8-9','P2:12-16','C2:5'])

page('S3','The product base is broad; fluid therapy still dominates','Most sales come from established sterile liquids. Higher-value ranges remain smaller and require product-specific proof.',
exhibit('Six therapeutic groups, with different adoption mechanisms',table(['Range / disclosed mix¹','What Amanta sells','Buyer logic and constraint'],[
['Fluid therapy, 63%','Normal saline, dextrose, dextrose-saline, Ringer lactate and electrolytes; 100-1,000 ml, single- and two-port packs.','Recurring hospital need; SteriPort premium must justify higher cost.'],
['Formulations, 17%','Anti-infectives such as ciprofloxacin, metronidazole and fluconazole; paracetamol, mannitol and linezolid also listed.','Drug plus packaging capability; molecule, pack and registration matter.'],
['Diluents / injectables, 9%','WFI and saline in 5/10 ml; lidocaine, potassium chloride, magnesium sulphate, calcium chloride/gluconate.','Sterility and compatibility are essential; tenders/customer access can govern price.'],
['Respiratory, 5%','Budesonide suspension; salbutamol, levosalbutamol and combinations with ipratropium.','Nebuliser use; suspension homogeneity and market registration gate scale.'],
['Irrigation, 5%','Eye wash and wound-cleaning solutions, including sodium chloride.','Smaller applications; no separate profit disclosure.'],
['Ophthalmic, 2%','Anti-infective/glaucoma drops and lubricants in FFS or conventional three-piece packs.','Preservative-free multi-dose delivery is a development/partnering opportunity.'],
]),src(('P2',13),('P2',14),('P2',29),('P2',30),('P2',31),('P2',32),('P2',33),note='¹ Deck mix has no clear period label and sums to 101% due to rounding; indicative product mix, not Q2 segment reporting.'))+
h('Current catalogue is not the same as approval in every market')+p('The deck lists commercial products, including budesonide, but the latest call discusses fresh validation and transfer of a suspension formulation to the future line. Existing domestic or export sales do not imply that the new process is validated, or that advanced-market dossiers are approved. Approval must be matched to the formulation, manufacturing line, presentation and destination.')+src(('C2',13),('C2',14))+
note('Fluid-therapy volume can fund development. A richer mix can improve profit per unit, but the report does not assign invented margins to each molecule.'),tag='Products and uses',sources=['P2:13-14,29-33','C2:13-14'])

page('S3','The SVP opportunity depends on product transfer, not just speed','Inhalation and preservative-free eye care have credible technical requirements; commercial receipts remain stage-dependent.',
exhibit('What is commercial, what is being built, and what is only an idea',table(['Platform','Status at 9 Nov 2026','Next gate / economic implication'],[
['SteriPort ISBM','MAKES AND SELLS. Line 3 production formally started 2 Sep.','Stable throughput, net realization and hospital use; volume is the principal lever.'],
['Existing SVP / BFS','MAKES AND SELLS. WFI/diluents and respiratory/eye products already in catalogue.','Maintain service to existing customers while transferring selected products.'],
['New inhalation line','UNDER CONSTRUCTION. Dedicated shapes/tooling, engraved information and variable data requirements.','Factory acceptance, installation, qualification and product transfer. New capacity is not automatic approval.'],
['Budesonide suspension transfer','VALIDATION UPDATE. Call reports validation/transfer on existing equipment; new-line transfer follows installation.','Preserve suspension homogeneity at scale; management indicates 6-7 months for transfer-related process.'],
['Multi-dose preservative-free eyes','IN DEVELOPMENT / MODIFICATION of conventional three-piece line.','Device/formulation suitability and licensing; partner economics not disclosed.'],
['Glass vials / ampoules / cartridges','IDEA. Management discussed an alternative future investment.','No approved capex, firm customer or revenue plan; zero incremental value in our model.'],
]),src(('AS',1),('C2',5),('C2',6),('C2',11),('C2',13),('C2',14)))+
h('Why inhalation is different from conventional BFS')+p('Management explains that some export markets do not want paper labels on the container because of spore risk. Product names may need engraving, with variable data printed on a tab. The line must match the intended commercial presentation. This explains why generic spare capacity cannot simply be relabelled as qualified inhalation output.')+src(('C2',5))+
h('Do not add the pipeline counts')+p('The call refers to 20 pipeline products, roughly 12 SVP products, six inhalation products, two already commercialised and an additional six to be developed. The categories overlap and the wording does not reconcile into a unique count. We retain 20 as the management total and do not sum the subsets. No customer orders, molecule-level margin or approval calendar was supplied.')+src(('C2',5))+
note('The valuable milestone is a qualified product with a buyer. Track that separately from equipment acceptance and the number of molecules in development.'),tag='Products, stages and gates',sources=['AS:1','C2:5-6,11,13-14'])

page('S4','One company, several overlapping views of the same revenue','Therapy, manufacturing platform, geography and channel are different classifications. Adding them would overstate the business.',
exhibit('Four lenses; only one total revenue',table(['Lens','What is disclosed','What is not safe to infer'],[
['Legal reporting','One standalone company; no subsidiaries, associates or joint ventures.','A separate listed SVP entity, minority interests or a group SOTP.'],
['Therapy','Fluid therapy, formulations, diluents/injectables, respiratory, eye care and irrigation.','Therapy-level reported EBITDA or capital employed.'],
['Platform','LVP / SteriPort / SVP, with different container technologies and capacity units.','Sum of SteriPort sales plus every therapy sales bucket.'],
['Geography','FY26 external-customer revenue outside India ₹110.70cr; India ₹173.50cr. Q2 FY27 international share about 32%.','A constant export mix or a regulated-market share equal to total exports.'],
['Commercial channel','Domestic brand, exports, CMO, development/licensing.','Add licensing estimates to revenue again if already embedded in existing sales.'],
]),src(('AR',54),('AR',75),('C2',4),('C2',13),('C2',15)))+
exhibit('Geographic sales in FY26 were material but not the whole story',bars(['Outside India','India'],[110.6963,173.4976],'₹ crore; external-customer revenue',height=210,maxval=200,fmt='.1f'),src(('AR',75),note='The note totals ₹284.19cr, excluding other operating revenue; denominator differs from ₹287.68cr reported revenue.'))+
p('The latest deck describes 47 products registered across 120 jurisdictions and sales into 21 export markets, while the annual report cites 20 FY26 export countries. Those are different dates and definitions. Registrations can exist in a country without current sales. Likewise, small-volume business sales of ₹55-65 crore and licensing/development activity of ₹25-30 crore are overlapping commercial descriptions, not additional independent segments.')+src(('AR',11),('P2',19),('C2',9),('C2',13),('C2',15))+note('The model uses one company total. It adds only explicitly incremental new-line sales and makes the no-cannibalisation assumption visible.'),tag='Segments and entities',sources=['AR:54,75','P2:19','C2:4,9,13,15'])

page('S5','A distribution network helps; hospital conversion still matters','Customer diversification reduces single-buyer exposure, while hospital adoption and collections determine the quality of growth.',
exhibit('Commercial routes have different bottlenecks',table(['Route','Disclosed evidence','Cash and execution test'],[
['Domestic branded','About 320 distributors/stockists and 96 sales/marketing staff in FY26/deck. Latest call cites roughly 200-250 channel partners.','Definitions differ. Count distributors separately from active hospital penetration and realized price.'],
['Exports','FY26 geographic note: no customer or group accounts for 10% or more of revenue. Established market relationships.','Watch country/customer payment terms, currency, local registrations and receivable ageing.'],
['Classic CMO','Latest call describes only 2-3% of sales.','Low weight today; do not mistake the whole company for a commodity contract manufacturer.'],
['Development / out-licensing','Management discusses ₹25-30cr a year, not a quarter; no named licensee or split between milestones and supply.','Contracts, milestone timing, royalties and recurring supply economics are not disclosed.'],
]),src(('AR',11),('AR',74),('C2',9),('C2',13),('C2',15)))+
h('Why a hospital might pay more')+p('Management positions SteriPort for oncology, critical care, cardiac intensive care, anaesthesia and paediatrics. In these settings, handling and delivery-system reliability may matter more than the lowest acquisition cost. But hospital budgets still constrain substitution. Management itself says the product is costlier than legacy and other two-port alternatives. Wide distribution is necessary; it is not evidence that every hospital will pay the premium.')+src(('C2',7),('C2',8),('C2',9))+
h('What we can and cannot say about named customers')+p('The source set does not identify customer names or licensees with product-level contracts. Analyst affiliations and the call organizer are not customers. There is no disclosed binding order book supporting the Line 3 annual revenue potential. The annual report’s no-customer-above-10% statement is useful, but it does not establish low geographic concentration, short collection periods or guaranteed repeat orders.')+src(('AR',74),('C2',5))+
exhibit('Sales-to-cash evidence at March and September 2026',table(['₹ crore','Mar 2026','Sep 2026'],[['Net trade receivables','43.02','44.22'],['Inventories','82.71','88.65'],['Trade payables','35.89','34.73']],'numeric'),src(('AR',52),('R27',4)))+
note('Watch whether receivables and inventories grow faster than shipped sales. The first failure can appear in cash before it appears in reported profit.'),tag='Customers and partners',sources=['AR:11,52,74','R27:4','C2:7-9,13,15'])

page('S6','The moat is process-and-access, with limits to pricing power','Sterile manufacturing and established routes to market create friction for entrants; they do not create an unconstrained monopoly.',
exhibit('The moat test: evidence, mechanism and counter-evidence',table(['Potential advantage','Why it can matter','Counterpoint / proof still needed'],[
['Validated sterile process','Process consistency, trained operators, utilities and testing take time and capital to establish.','The disclosed WHO-GMP and ISO certificates support process credibility; they do not establish exclusive access or country-specific approvals.'],
['SteriPort platform','Two-port design, polypropylene compatibility and automated ISBM support high-acuity use.','No independently verified comparative contamination data or molecule-level premium disclosed.'],
['Distribution / history','Three-decade operating history, domestic reach and export registrations reduce market-entry friction.','Distributor counts differ by definition; retention and share of hospital spend are not disclosed.'],
['Shared infrastructure','New line uses existing facilities/utilities; marginal output can absorb fixed overhead.','A ramping line still adds depreciation, maintenance, validation and working capital.'],
['Portfolio development','Inhalation and preservative-free products can differentiate the value proposition.','Transfer, approval and partner execution can defer cash for several quarters.'],
]),src(('AR',9),('AR',10),('P2',16),('C2',3),('C2',5),('C2',8)))+
h('Two attractive claims that need careful handling')+p('Management reports more than 35 crore SteriPort bottles sold since 2016 without a fungal-contamination complaint. This is an attributed safety claim, not an independent comparative trial or audit. The deck’s statement of 50-60% domestic share has an unclear market denominator; the call’s rough 6% IV-fluid share is obtained from around 12 crore capacity versus a 190-200 crore-unit market. Capacity divided by a market estimate is not actual sold market share.')+src(('P2',16),('C2',7),('C2',8))+
h('A business advantage must show up in economics')+p('Operating EBITDA excluding other income was ₹59.67 crore in FY25 and ₹59.86 crore in FY26, despite revenue growth. High utilization and technical differentiation have not yet produced expanding operating profit. That does not disprove the platform’s value, but it limits the claim that capacity addition alone deserves a structural multiple premium.')+src(('AR',52))+
note('The defensible view is a qualified manufacturing and distribution franchise with execution risk. Sustained net price, cash returns and product retention would strengthen the moat evidence.'),tag='Moat and competition',sources=['AR:9-10,52','P2:16','C2:3,5,7-8'])

page('S7','High utilisation can hide different economic realities','The old plant, the new line and newly qualified products must be measured separately.',
exhibit('Separate quantity from quality before forecasting',table(['Headline metric','Useful interpretation','Misleading interpretation'],[
['Legacy line utilisation near full','Existing capacity is tight; incremental units may require the new line.','Every additional unit of nameplate capacity is already demanded.'],
['Line 3 around 55% initially','The line was balancing and ramping after September startup.','95-97% companywide utilisation also applies to Line 3.'],
['11.6cr SteriPort capacity','A physical annual production ceiling under the stated operating assumptions.','11.6cr bottles sold, collected or at a uniform price.'],
['32% international sales in Q2','International customers already matter.','32% advanced-regulated-market sales or a guaranteed premium margin.'],
['₹9cr solar saving [G]','Annual gross electricity cost avoided at the expected generation/tariff.','₹9cr incremental PAT or free cash after debt service.'],
['₹16cr new SVP illustration','A small, explicitly speculative early revenue illustration.','A committed order book or the entire existing SVP business.'],
]),src(('P2',5),('P2',18),('C2',4),('C2',7),('C2',15)))+
exhibit('Existing lines had limited spare capacity before expansion',table(['Reported utilisation','FY23','FY24','FY25','FY26'],[['Conventional LVP','97%','93%','91%','93%'],['SVP','89%','94%','99%','98%'],['SteriPort','73%','83%','91%','90%']],'numeric'),src(('AR',10),note='Issuer-reported production utilisation. The “current 96%” aggregate has no stated weighting method.'))+
p('The business mechanism is operating leverage: a greater number of sold, released units shares existing overhead. The constraint changes as the plant ramps. At first it may be engineering stability; later it may be qualified products, hospital demand, polymer cost or cash to carry stock. A single utilization percentage cannot capture all of these constraints.')+note('Request shipped volume, average net realisation and line-specific contribution together. Production without profitable shipments can consume working capital.'),tag='Quantity versus quality',sources=['AR:10','P2:5,18','C2:4,7,15'])

page('S8','The ₹60 crore Line 3 target is commercially demanding','The late FY27 start leaves little room for a slow ramp at the disclosed steady-state revenue rate.',
exhibit('Annual potential and partial-year expectation are different',bars(['FY27 Line 3 [G]','Annual potential'],[60,110],'₹ crore revenue; different time bases',height=200,maxval=130,fmt='.0f'),src(('C2',5),note='The deck quotes ₹110-120cr annual potential; use ₹110cr for this timing test.'))+
exhibit('A transparent timing test, not a sales forecast',table(['Calculation','Result','Interpretation'],[
['Added capacity: 11.6 minus 6.6','5.0cr bottles/year','~75.8% addition (company rounds to 75%).'],
['₹110cr / 5cr added bottles','₹22 / bottle (calc.)','Blended effective revenue if all added units support the annual potential. Not a quoted list price.'],
['₹110cr × 7 / 12','₹64.2cr','Maximum timing illustration for Sep-Mar at the steady annual rate, before ramp losses.'],
['₹60cr / ₹64.2cr','93.5%','Required share of that simple seven-month maximum. Not measured utilisation.'],
['₹60cr / ₹110cr × 12','6.55 months','Equivalent full-rate revenue months; September startup and balancing make this demanding.'],
]),src(('P2',5),('C2',5),note='Calculations assume uniform realisation and seven complete months. Actual days, SKU mix and ramp timing can differ.'))+
h('What would reconcile the ambition')+p('Higher realizations, favourable product mix, a higher ₹120 crore annual potential or rapid stabilization can help. The management target may also reflect a revenue definition broader than a simple nameplate-times-price calculation. The call does not give line-specific monthly units, sold output, yields or transferred sales. We therefore do not label the target impossible; we flag the evidence needed to substantiate it.')+
h('Incrementality is an explicit model assumption')+p('Our base illustration holds the FY26 legacy revenue pool flat and adds ₹60 crore from Line 3 in FY27E. This is a no-cannibalisation assumption, not a reported fact. If existing products migrate to Line 3 or the new line displaces old-line sales, consolidated growth would be lower than the simple sum. A clean line-revenue-to-group-revenue reconciliation is a high-priority future disclosure.')+src(('C2',5),('C2',10))+note('The next disclosure should bridge new-line production to net incremental company sales. That is more informative than another capacity announcement.'),tag='Line 3 revenue test',sources=['P2:5','C2:5,10'])

page('S9','Three projects, three clocks, three funding profiles','SteriPort and solar are operating; SVP is still a project with a separate commercial qualification clock.',
exhibit('Asset and capital tracker',table(['Project','Capital / funding','Status and capacity','Economic gate'],[
['SteriPort Line 3','~₹90cr project scope [G]; IPO capex plus other funding.','Production announced 2 Sep 2026. Adds 5cr bottles, total 11.6cr/year.','₹60cr FY27 contribution [G]; ₹110-120cr annual optimum [G]. No orders disclosed.'],
['SVP expansion','~₹30.13cr project scope; IPO-related.','+10.8cr units, 20.9 to 31.7cr/year. Q1 FY28 commissioning [G].','Inhalation tooling, product transfer and filings; capacity and launch dates differ.'],
['Captive solar','₹34.8cr project; ₹5.8cr company contribution, balance largely debt.','10.8MWp; generation announced 30 May 2026.','₹9cr annual gross saving [G]; generation, tariff, maintenance and financing determine net benefit.'],
['Routine / development spend','Latest call cites ₹7-20cr range without a defined period/budget.','F&D, filings and automation considered.','Do not turn an undefined range into a sanctioned annual budget.'],
['Glass-packaged injectables','Uncommitted concept, not an approved current project.','Vials, ampoules, cartridges and F&D discussed.','No incremental revenue/capital in base model.'],
]),src(('AR',12),('AR',30),('AS',1),('AP',1),('C2',10),('C2',11)))+
h('The latest SVP schedule is a chain, not one date')+
exhibit('Factory acceptance is earlier than qualified customer sales',steps([('13-19 Dec 2026 [G]','Factory acceptance test (FAT), shifted from November.'),('January 2027 [G]','Equipment delivery after acceptance.'),('March / Q1 FY28 [G]','Installation and commissioning, with fiscal-quarter wording that needs confirmation.'),('After commissioning','Product transfer and validation; market registration and commercial ramp follow.')]),src(('C2',12),('C2',14)))+
p('The presentation’s capex graphic carries FY26P ₹130 crore and FY27P ₹25 crore, while audited FY26 cash capex was ₹80.19 crore. Project scope, accrual capex, cash expenditure and the letter P are not interchangeable. We use audited cash for cash analysis and disclosed project costs for the project ledger.')+src(('P2',18),('AR',53))+note('Track spent, committed, delivered, qualified and sold as separate stages. The project can be mechanically complete while cash returns remain unproven.'),tag='Capacity, capex and timeline',sources=['AR:12,30,53','AS:1','AP:1','C2:10-12,14'])

page('S9','Solar improves operating cost, not rupee-for-rupee owner cash','At the disclosed project cost, the gross saving is attractive; funding, depreciation and actual generation reduce the benefit.',
exhibit('Solar benefit bridge: disclosed versus estimated',table(['₹ crore unless stated','Basis','Annual amount'],[
['Project cost','Company annual report','34.8'],
['Own contribution','Company annual report','5.8'],
['Implied other funding (calc.)','34.8 minus 5.8; primarily term loan','29.0'],
['Gross electricity saving [G]','Management annual run-rate estimate','9.0'],
['Illustrative interest [E]','29 × 9-11% financing assumption','(2.6) to (3.2)'],
['Illustrative depreciation [E]','34.8 / 20-year life, simplified','(1.7)'],
['Incremental PBT before O&M [E]','Gross saving minus interest and depreciation','4.07 to 4.65'],
['Incremental PAT before O&M [E]','Prior line × 72%, assumed 28% tax','2.93 to 3.35'],
]),src(('AR',12),('AP',1),('C2',4),('C2',5),note='Interest/life/tax are analyst illustrations, not project-specific disclosures. Excludes maintenance, degradation and repayment.'))+
h('Two important payback distinctions')+p('₹34.8 crore divided by ₹9 crore is 3.87 years of gross simple payback by arithmetic. The annual report cites a 3.6-year pre-interest payback, but does not reconcile that difference. Neither measure is an equity return or discounted project value. Loan principal is not a P&L cost but does consume cash; depreciation is a P&L cost but does not consume cash in the year charged.')+src(('AR',12))+
h('The first operating evidence is encouraging but incomplete')+p('The 30 May announcement establishes generation start. The Q2 CFO says solar savings have begun to help, while solar-loan interest has already entered finance cost. The company does not isolate metered generation, avoided tariff, operating cost, net project profit or cash saving in the latest reporting package. Group EBITDA cannot identify the solar contribution because utilization, price, mix and polymer cost changed at the same time.')+src(('AP',1),('C2',4))+
note('We embed solar within scenario margins. Adding ₹9 crore again to the same projected EBITDA would double-count the benefit.'),tag='Solar economics',sources=['AR:12','AP:1','C2:4-5'])

page('S10','Management has substantial ownership and a mixed execution record','The right governance label is WATCH: aligned ownership and formal oversight coexist with delays and related-party dealings.',
exhibit('Who makes the decisions',table(['Person / board structure','Role and evidence','Investor interpretation'],[
['Bhavesh Girishbhai Patel','Chairman/MD and promoter since incorporation; mechanical engineering and finance background, 30+ years in the business.','Product and process depth, with key-person concentration.'],
['Paras Mehta','CFO; presents the financial and funding bridge on calls.','Debt, cash and adjusted-profit definitions need more precise reconciliation.'],
['Six-member board','Three independent directors: Nitin Jain, Anjali Choksi and Kshitij Patel. Nonexecutives include Nimesh Patel and Pratik Gandhi.','Formal independence is half the board; it is not proof that every transaction is arm’s length.'],
['Nimesh Patel','Nonexecutive director; AGM disclosure identifies him as the CMD’s cousin.','Family relationships should be visible when assessing independent challenge.'],
['Senior management change','COO Anil Rathi resigned effective 29 Oct 2026 for a better opportunity/growth, per filing.','Continuity matters during ramp; no evidence supplied of a broader operational dispute.'],
]),src(('P2',21),('P2',22),('AR',32),('AGM',2),('COO',1)))+
exhibit('Promoter ownership increased modestly after listing',table(['Screener / reported holding','Sep 2025','Mar 2026','Sep 2026'],[['Promoters','63.56%','63.72%','63.80%'],['FIIs','1.00%','0.85%','0.07%'],['DIIs','11.34%','12.88%','12.20%']],'numeric'),src('SC',note='Holding changes do not by themselves prove purchases; classifications and transfers can also change. Latest promoter trade is discussed in governance notes.'))+
h('Pay, control and capital allocation')+p('FY26 disclosed total CMD remuneration was ₹1.20 crore, roughly 8.1% of reported PAT (calc.). The related-party note’s salary/short-term benefit figure is ₹1.08 crore, a different scope. Shareholders approved a monthly remuneration revision to ₹13.29 lakh effective 1 April 2026. IPO money has funded business expansion; the monitor reports schedule delay, not object diversion. Detailed transaction and audit issues appear in S18.')+src(('AR',42),('AR',70),('AGM',1),('MA',9))+
h('Communication assessment: cautiously optimistic, with loose bridges')+p('The calls contain useful admissions: polymer uncertainty, a five-month Line 3 delay, and no simulated SVP margin model. They also mix annualised potential with fiscal-year numbers and normalized profit growth with reported profit growth. We value the candour but apply wider scenario bands until management supplies precise reconciliations.')+src(('C2',10),('C2',13),('C2',15))+note('Ownership alignment is a positive. It does not remove the need to monitor project timing, remuneration, related parties and minority-shareholder outcomes.'),tag='People, incentives and communication',sources=['P2:21-22','AR:32,42,70','AGM:1-2','COO:1','MA:9'])

page('S11','The expansion was delivered later than first envisaged','The delivery record supports technical progress, while commercial timing deserves a discount for uncertainty.',
exhibit('Promise versus delivery, with the original period preserved',table(['Topic','Earlier evidence','Latest evidence / assessment'],[
['SteriPort start','Feb call: bottles by end-Mar 2026, commercialization in April. May call: commissioning next month. Aug call: validation and late-Aug start targeted.','Formal production-start filing 2 Sep 2026. Nov call acknowledges about five months late. DELAYED, now operating.'],
['SteriPort scale','Earlier calls round total capacity to ~12cr bottles.','Latest deck 11.6cr: 6.6+5.0cr. Rounding, not evidence of 12cr actual shipments.'],
['Solar operation','Feb call expected Q1 FY27. May call spoke of 5-6 days.','Generation-start filing 30 May 2026. Within Q1; latest call says generating since end-Q1. Formal dated filing is the more precise event source.'],
['SVP commissioning','Feb Q&A envisaged January 2027; ₹6-7cr initial-quarter sales illustration.','Latest target Q1 FY28. Equipment acceptance shifted from Nov to mid-Dec; qualification still follows. DELAYED / pending.'],
['Revenue framing','Feb FY27 hope ~₹400cr, excluding SVP. Later discussion moved toward ₹420-430cr.','Nov mixes ₹420-430cr annualised/full-year wording with affirmed ₹400-420cr FY28. Period bridge unresolved; not a clean current-year promise.'],
['Margin ambition','Earlier 3-4pp improvement discussed for FY27, conditional on scale and costs.','Q2 company EBITDA margin 21.6%; two-year 25%+ aim retained. NOT YET PROVEN.'],
]),src(('C3',6),('C3',7),('C3',16),('C3',17),('C4',3),('C1',8),('AS',1),('AP',1),('C2',10),('C2',12),('C2',14)))+
h('Why the historical record matters for valuation')+p('Delay costs are more than a shifted revenue line. Capital remains tied up before sales; fixed costs, regulatory work and interest can continue. Inhalation adds a further dependency: equipment timing affects product transfer and filings. A single delayed project is not proof of chronic failure, but repeated date movement warrants explicit delay cases rather than immediate full-year steady-state revenue.')+
p('We do not produce a misleading “promises met” percentage. The milestones are interdependent and have different economic weights. Revenue language is also too ambiguous for a mechanical pass/fail score. The next proof is the amount of incremental sales and cash, not another revised commissioning date.')+note('Use the original dates as a baseline. Preserve both delivered assets and missed timing when assessing management credibility.'),tag='Historical delivery tracker',sources=['C3:6-7,16-17','C4:3','C1:8','AS:1','AP:1','C2:10,12,14'])

page('S12','The current guidance register needs explicit qualifiers','The targets form a useful operating agenda; they do not supply a complete annual financial forecast.',
exhibit('Management guidance as stated, without an analyst haircut',table(['Metric [G]','Target and period','How to use it'],[
['Line 3 FY27 sales','About ₹60cr in FY27.','Partial-year contribution. Incrementality versus old-line sales not quantified.'],
['Line 3 steady annual sales','~₹110cr in call; ₹110-120cr in latest deck.','At optimal utilisation, not current booked orders.'],
['Full utilization','20 Nov in Q&A; next-quarter full ramp in prepared remarks; deck also says within 12 months.','Different formulations of the ramp horizon; request measured output.'],
['SVP capacity/start','20.9 to31.7cr units; Q1 FY28 target.','Commissioning, product transfer and commercial launches are separate dates.'],
['Solar saving','~₹9cr annual gross power saving.','Not incremental PAT or debt-free cash.'],
['Growth / margin','20%+ revenue CAGR and 25%+ EBITDA margin; two-year aim.','No starting base, exact annual path or ex-other-income bridge.'],
['SVP SBU ambition','₹55-65cr current sales toward ₹100-120cr short/mid-term.','No firm fiscal-year endpoint; includes existing business.'],
['SVP first-year illustration','₹16cr for FY27-28, explicitly speculative.','Not committed guidance; conditional model anchor only.'],
['Debt repayment','~₹35cr/year; FY27 gross borrowing ₹175-180cr, FY28 term~₹100cr plus WC~₹50cr.','Borrowing guidance excludes a precise lease/cash bridge.'],
]),src(('C2',3),('C2',4),('C2',5),('C2',6),('C2',7),('C2',9),('C2',14),('C2',15),('P2',9)))+
h('Next-quarter outlook: what can be inferred')+p('Line 3 should contribute a longer operating period in Q3 FY27, with fixed-cost absorption and solar supporting margin. Price increases of roughly ₹0.7-1.8 per bottle, averaging about ₹1, may support realization. Polymer volatility is the offset. Management explicitly avoided a confident Q3 margin number. We expect the new-line direction to be positive, but do not present a precise quarterly profit forecast without volume, pricing and material-cost data.')+src(('C2',13))+
note('Require guidance updates in a comparable table: original target, period, basis, current target and reason for change. This prevents annual potential from silently becoming next-quarter revenue.'),tag='Guidance and near-term outlook',sources=['C2:3-7,9,13-15','P2:9'])

page('S13','Growth has two routes: more bottles and more value per unit','SteriPort is the nearer volume driver; SVP must earn a higher-value product and market mix.',
exhibit('Growth drivers connect to specific economic mechanisms',table(['Driver','Transmission into profit / cash','First material proof needed'],[
['SteriPort hospital depth','More sold units on existing infrastructure improve fixed-cost absorption, if net price holds.','Line-specific sold units, net incremental sales, contribution after polymer and channel costs.'],
['Inhalation / respiratory','A differentiated presentation can earn greater revenue per unit and expand exports.','Repeat orders in named product/market categories; transfer and registration completion.'],
['Preservative-free ophthalmic','Partnering can monetize development while reducing own marketing burden.','Executed license agreement, upfront/milestone/supply/royalty terms and product approval.'],
['New export markets','A qualified line and dossiers can broaden customers beyond existing markets.','Product/site-specific authorization, first shipment and receivable collection.'],
['Solar / automation','Lower power cost, fewer manual interventions and shared overhead can lift conversion.','Metered savings and productivity at saleable output, not just theoretical throughput.'],
]),src(('C2',3),('C2',5),('C2',6),('C2',11),('C2',12),('C2',13),('C2',14)))+
h('Regulated-market opportunity has a long lead time')+p('Management names Australia, New Zealand, Canada and South Africa as targets and describes a MedSafe process. That is not a market authorization. The Q2 call corrects the idea that SteriPort was already supplied to Canada: the earlier Canada/Australia products were WFI/diluents. The call also gives inconsistent sequencing between January-February filings and filing after new-line commissioning. We assume no advanced-market windfall in the base model.')+src(('C2',10),('C2',11),('C2',12))+
exhibit('Dated catalysts and required evidence',table(['Window [G unless stated]','Event','What would make it investable evidence'],[
['Nov 2026','20 Nov full-line operation target; promised SVP model in about15days.','Measured throughput and a published sales/margin bridge.'],
['Dec 2026 - Jan 2027','SVP FAT and equipment delivery.','Completed acceptance, site installation schedule, remaining spend.'],
['Q1 FY28','Expanded SVP commissioning.','Qualification and commercial product transfer, not equipment photos alone.'],
['End calendar2027 / from2028','Portfolio development and Indian inhalation front end plans.','Country approvals, launch economics and repeat receipts.'],
]),src(('C2',5),('C2',6),('C2',9),('C2',12),('C2',15)))+
note('Value each opportunity at its stage. The model includes modest SVP revenue and excludes approvals or contracts that the source set does not establish.'),tag='Growth and dated triggers',sources=['C2:3,5-6,9-15'])

def peer_snapshot(file):
 q=json.loads((ROOT/file).read_text(encoding='utf-8'))
 if 'result' in q:q=q['result']
 return q['data']['sections']
g=peer_snapshot('peer-0.json');d=peer_snapshot('peer-denis.json')
def annualcell(q,label,year='Mar 2026'):
 a=q['profit_loss'];i=a['years'].index(year)
 return next(r['values'][i] for r in a['rows'] if r['label']==label)
page('S14','Compare manufacturing economics before comparing P/E','No listed company is a clean twin: IV-fluid exposure, specialty mix and funding explain much of the valuation gap.',
exhibit('Capability comparison: close competitor versus broader sterile peer',table(['Company','Overlap / distinction','How to use the comparison'],[
['Amanta','IV fluids and SteriPort plus SVP, respiratory and ophthalmic platforms; established domestic and export channels.','A volume ramp with product-mix optionality, still leveraged.'],
['Denis Chem Lab','IV-fluid manufacturing is a closer product overlap; CRISIL describes a broad bottle-based portfolio.','Useful for commodity-fluid economics and funding discipline, not a direct substitute for SVP optionality.'],
['Gufic Biosciences','Broader sterile capabilities including lyophilized and liquid vials/ampoules, prefilled syringes and dual-chamber systems.','Better specialty-platform context; not an identical product mix or a justified automatic multiple for Amanta.'],
['Otsuka / B. Braun','Amanta management identifies them as two-port category participants.','Evidence of competition, not a complete independent market-share study; no comparable listed Indian valuation used.'],
]),src(('P2',13),('P2',16),('DR',2),('DR',3),'GF',('C4',9)))+
exhibit('Same fiscal year and statement basis; market snapshots are dated',table(['Standalone, FY26 unless stated','Amanta','Denis','Gufic'],[
['Sales, ₹cr','287.7',annualcell(d,'Sales +'),annualcell(g,'Sales +')],
['Operating EBITDA, ₹cr','59.9',annualcell(d,'Operating Profit'),annualcell(g,'Operating Profit')],
['Operating margin','20.8%',annualcell(d,'OPM %'),annualcell(g,'OPM %')],
['PAT, ₹cr','14.9',annualcell(d,'Net Profit +'),annualcell(g,'Net Profit +')],
['Snapshot P/E, times¹','~42.9',d['overview']['key_ratios'].get('Stock P/E','NA'),g['overview']['key_ratios'].get('Stock P/E','NA')],
['Screener ROCE, FY26','~12%',d['overview']['key_ratios'].get('ROCE','NA')+'%',g['overview']['key_ratios'].get('ROCE','NA')+'%'],
],'numeric'),src(('AR',52),'SC','DS','GS',note='Peer figures are rounded Screener MCP standalone data retrieved 10Nov2026. ¹ Amanta exact-close P/E uses TTM PAT ~₹18.3cr; peer P/E reflects each source snapshot, not identical exchange timestamps.'))+
p('Our scenario EV/EBITDA multiples of11x/14x/17x are analyst sensitivities, not a peer-regression result. Gufic’s higher snapshot P/E does not establish that Amanta deserves the same premium. Amanta’s qualification, collection and capital return evidence should determine whether a rerating is earned. Peer market multiples are context, not primary proof of fair value.')+note('Relative cheapness is unreliable when earnings, leverage and product stages differ. Compare the cash needed to deliver the forecast as carefully as the multiple.'),tag='Peers and relative economics',sources=['AR:52','P2:13,16','DR','GF','SC','DS','GS','C4:9'])

page('S15','Keep current earnings separate from future possibilities','The existing business earns today; unapproved markets and hypothetical projects must not be capitalized as accomplished facts.',
exhibit('An evidence ladder for the revenue opportunity',table(['Economic bucket','Evidence and ₹ magnitude','Model treatment'],[
['Earning today','FY26 revenue ₹287.68cr; LVP product sales ₹232.99cr, SVP ₹47.29cr, other products ₹1.38cr.','Historical business anchors; do not confuse these legal-product buckets with SBU commentary.'],
['Operating, ramping','Line3live; ~₹60cr FY27 and ₹110-120cr annual potential [G].','Separate incremental sales assumption and ramp downside.'],
['Operating cost asset','Solar live; ₹9cr annual gross saving [G].','Embedded in margin; no separate additive EBITDA line.'],
['Announced and under construction','SVP +10.8cr units, Q1 FY28. ₹16cr first-year illustration explicitly speculative.','Base FY28E new-line revenue16cr is a conditional illustration, not committed guidance.'],
['Development / market access','20-product pipeline; advanced-market and preservative-free ambitions.','No blanket pipeline NPV; earnings only as scenario sales within physical capacity.'],
['Idea / unsanctioned capital','Glass vials/ampoules/cartridges and future F&D discussed.','Zero incremental value and capex in all three scenarios. Reassess only after a funded, approved plan.'],
]),src(('AR',65),('P2',5),('C2',5),('C2',11),('C2',15)))+
h('A disconfirming detail: SVP sales fell in FY26')+p('The audited product note shows SVP product sales of ₹47.29 crore in FY26 versus ₹53.39 crore in FY25, down11.4% (calc.). LVP product sales rose10.1% to ₹232.99 crore. That distinction is obscured by a simple companywide expansion story. Management’s later ₹55-65 crore SBU sales description may use a broader period or perimeter; it is not a direct like-for-like replacement for the audited product-sales note.')+src(('AR',65),('C2',9))+
h('Why we avoid a sum-of-the-parts valuation')+p('The company has one operating/legal reporting perimeter and no disclosed product-level capital employed, contribution or overhead allocation. A separate high multiple for the whole SVP “option” plus a multiple on company EBITDA would double-count current earnings. We use one EV/operating EBITDA valuation and test the incremental product mix within that model.')+note('Optionality earns a larger weight as the first unproven gate is passed. A portfolio list is not a licence to add unsupported value.'),tag='Reality versus optionality',sources=['AR:65','P2:5','C2:5,9,11,15'])

page('S16','The causal chain shows where each thesis can break','A growth driver becomes valuable only after product, customer, margin and cash tests all work.',
exhibit('Driver to owner cash, with the first unproven link marked',table(['Driver','Established evidence','First unproven link','Profit / cash effect and falsifier'],[
['Line3volume','Production announced; larger installed capacity.','Net incremental, sold output at stable realization.','Fixed-cost absorption if demand holds. Fails if inventories grow while line sales disappoint.'],
['SVP mix','Existing products and a funded expansion project.','Timely acceptance/commissioning, then qualified transfer.','Higher-value mix after launch. Fails if capex is complete but approvals or repeat orders stall.'],
['Advanced exports','Existing WFI/diluent history and international revenue.','New product/site-specific market authorization.','Potential customer diversification and value. Fails if “registration” remains a process without shipments.'],
['Ophthalmic partnering','Modification/development plan and existing eye-care range.','An executed commercial arrangement with disclosed economics.','Partner access without a full own front end. Fails if fees are one-off or supply margins weak.'],
['Solar savings','Formal generation-start announcement.','Measured annual saving net of financing and O&M.','Structural cost relief. Fails if tariff/generation shortfall or debt burden absorbs most savings.'],
['Debt reduction','Borrowings fell March to September; IPO-funded net worth increase.','Recurring cash after interest, capex and WC sufficient for repayments.','Interest falls and equity value expands. Fails if deposits fund cash gaps and refinancing continues.'],
]),src(('AS',1),('AP',1),('R27',4),('R27',5),('C2',5),('C2',6),('C2',11),('C2',14)))+
h('An integrated test is more useful than isolated bullish facts')+p('A factory can run at a high rate and still earn disappointing returns if it makes lower-priced products, needs large inventories or carries expensive debt. A pipeline can be technically credible but commercially slow. Conversely, a modest revenue increase can improve PAT sharply if funding costs fall. The report therefore links every major thesis to a model input and an observable failure signal.')+
p('For the base model, the first uncertainties are incremental Line3sales and SVP launch timing. The next are operating margin and working capital. Valuation is deliberately last because none of the attractive product statements removes the need to pay a reasonable price for the eventual cash.')+
note('At each update, change the first unproven link to “verified” only with new evidence. Do not move it merely because the narrative became more confident.'),tag='Causal proof and falsification',sources=['AS:1','AP:1','R27:4-5','C2:5-6,11,14'])

page('S17','Q2 improved; reported PAT growth needs an exceptional-item bridge','Revenue rose17.3%, while operating EBITDA margin was nearly flat. The prior-year IPO charge exaggerates reported PAT growth.',
exhibit('Latest results, reconciled to the official statement',table(['₹ crore except margin','Q2 FY26','Q1 FY27','Q2 FY27','H1 FY26','H1 FY27'],[
['Revenue','70.8873','68.8032','83.1324','136.1944','151.9356'],
['Operating EBITDA, ex-OI¹','14.6505','14.5394','17.1949','29.5439','31.7343'],
['Other income','0.0707','0.6430','0.7554','1.0316','1.3984'],
['Company EBITDA¹','14.7212','15.1824','17.9503','30.5755','33.1327'],
['Company margin','20.77%','22.07%','21.59%','22.45%','21.81%'],
['Finance cost','5.1516','6.0048','5.8442','11.4385','11.8490'],
['Depreciation','4.6630','4.6853','5.2799','9.3039','9.9652'],
['PBT before exceptional','4.9066','4.4923','6.8262','9.8331','11.3185'],
['Exceptional expense','2.6288','0','0','2.6288','0'],
['PBT reported','2.2778','4.4923','6.8262','7.2043','11.3185'],
['Tax','1.0703','1.1818','1.9653','2.4896','3.1471'],
['PAT','1.2075','3.3105','4.8609','4.7147','8.1714'],
],'numeric smalltable'),src(('R27',3),note='¹ EBITDA calculated as PBT + finance + depreciation, adding back exceptional expense; operating EBITDA also excludes other income. Extra decimals retained here for auditability.'))+
h('Why the PAT story sounds different on the call')+p('Reported Q2 PAT increased302.6% and H1 PAT73.3% (calc.). The call says26% and12%, respectively. Adding back the prior-year ₹2.6288 crore exceptional IPO expense to prior-year PAT gives Q2 adjusted PAT₹3.8363 crore and H1₹7.3435 crore, producing26.7% and11.3% growth. That broadly explains the spoken comparison, but is a simple pre-tax add-back to PAT, with no explicit tax normalization. We use reported figures and show the adjustment rather than silently replacing them.')+src(('R27',3),('R27',7),('C2',4),('C2',5))+
h('What improved operationally')+p('Q2 revenue rose20.8% sequentially. Operating EBITDA increased18.3% from Q1, so operating margin slipped from21.13% to20.68%. Compared with Q2 last year, it was nearly flat at20.67%. Depreciation and finance cost rose; the new-line benefit has not yet produced a clear margin breakout. This is a volume acceleration, with earnings conversion still at an early stage.')+note('Use both reported PAT and pre-exception profit. A lower comparison base is not evidence of a fourfold improvement in underlying operating economics.'),tag='Results and earnings quality',sources=['R27:3,7','C2:4-5'])

page('S17','A longer quarterly record shows why the new line matters','The earlier business was growing slowly; the recent sequential acceleration is meaningful but not yet a durable trend.',
exhibit('Ten quarters of sales and profit',table(['Quarter','Sales ₹cr','Op. EBITDA ₹cr¹','Margin','PAT ₹cr'],[
['Q1 FY25','68.10','13.40','19.68%','(0.36)'],['Q2 FY25','66.73','13.88','20.80%','2.26'],['Q3 FY25','67.81','15.06','22.21%','4.28'],['Q4 FY25','72.06','18.96','26.31%','5.96'],
['Q1 FY26','65.31','14.90','22.81%','3.51'],['Q2 FY26','70.89','14.65','20.67%','1.21'],['Q3 FY26','74.49','15.36','20.62%','4.63'],['Q4 FY26','76.99','14.96','19.43%','5.53'],
['Q1 FY27','68.80','14.54','21.13%','3.31'],['Q2 FY27','83.13','17.19','20.68%','4.86'],
],'numeric smalltable'),src('SC',('R27',3),note='¹ Excludes other income. Screener series rounded. FY25 quarter PAT sum ₹12.14cr versus audited ₹10.50cr is unreconciled; older quarters are indicative only. Official latest results control.'))+
exhibit('Operating margin has not yet returned to the stronger historical quarters',bars(['Q3 FY25','Q4 FY25','Q1 FY26','Q2 FY26','Q3 FY26','Q4 FY26','Q1 FY27','Q2 FY27'],[22.21,26.31,22.81,20.67,20.62,19.43,21.13,20.68],'Operating EBITDA margin, %; ex-other-income',height=225,maxval=30,fmt='.1f'),src('SC',('R27',3)))+
p('Seasonality, inventory movements and mix make an individual quarter an unreliable steady-state margin. Management historically noted export ordering patterns can be uneven. We do not extrapolate the strongest quarter’s margin across the new capacity. The test is whether sequentially higher sales translate into several quarters of better contribution and collections.')+src(('C3',16))+note('The new line creates the capacity for a step-up. The historical range shows why margin stability must be demonstrated rather than assumed.'),tag='Quarterly comparison',sources=['SC','R27:3','C3:16'])

page('S17','FY26 PAT growth came mainly below operating EBITDA','Operating profit was flat, while lower financing cost and more other income supported shareholder earnings.',
exhibit('Historical financial statements in a consistent analytical layout',table(['₹ crore except EPS / margin','FY23¹','FY24¹','FY25','FY26'],[
['Revenue','259.1','280.3',f(HIST['FY25']['sales'],2),f(HIST['FY26']['sales'],2)],
['Operating EBITDA, ex-OI','~53','~58','59.67','59.86'],
['Operating margin','~20%','~21%','21.72%','20.81%'],
['Other income','~4','~1','1.39','3.37'],
['Finance cost','~35','~34','27.95','20.75'],
['Depreciation','~18','~20','18.40','18.73'],
['Exceptional expense','0','0','0','2.63'],
['PBT','~3','~5','14.71','21.12'],
['PAT','~(2)','~4','10.50','14.88'],
['Reported weighted-average EPS, ₹','(0.79)','1.35','3.71','4.33'],
['CFO, before financing interest','~43','~58','46.62','48.45'],
['Cash capex','Not comparable²','Not comparable²','20.77','80.19'],
],'numeric'),src(('AR',52),('AR',53),('AR',70),'SC',note='¹ Earlier historical series rounded from Screener; latest audited comparative controls FY25/FY26. ² Deck project-capex graphic is not a cash-flow series.'))+
h('The FY25 to FY26 profit bridge')+p('Revenue grew4.72%, operating EBITDA only0.32%, and PAT41.66% (calc.). Finance cost fell₹7.20 crore; other income rose₹1.99 crore. Depreciation increased₹0.33 crore and exceptional expense reduced PBT by₹2.63 crore. These movements reconcile the roughly₹6.42 crore increase in PBT. Refinancing and repayment helped, but the new capacity had not yet produced the operating earnings uplift.')+src(('AR',52),('AR',65))+
h('A further accounting distinction: capitalised interest')+p('FY26 gross financing costs were₹23.15 crore, of which₹2.409 crore was allocated to capital work in progress, leaving₹20.75 crore charged to profit. As assets enter use, financing costs are less protected by project capitalization and depreciation begins. This helps explain why FY27 finance cost need not fall immediately despite lower gross borrowing.')+src(('AR',65))+
note('The next phase must improve operating earnings, not rely only on refinancing. Forecasting PAT directly from a headline growth ambition would miss the capital-cost bridge.'),tag='Annual proof and accounting bridge',sources=['AR:52-53,65,70','SC'])

page('S17','Cash generation has not funded the investment cycle','Operating cash is real, but expansion and interest have required IPO liquidity and refinancing.',
exhibit('Cash flow: distinguish investment from financing',table(['₹ crore','FY25','FY26','H1 FY27'],[
['Cash from operations (after tax)','46.62','48.45','21.94'],
['Cash capex¹','(20.77)','(80.19)','(37.60)'],
['CFO less capex (calc.)','25.85','(31.74)','(15.66)'],
['Investing cash flow, total','(24.47)','(93.61)','(48.36)'],
['Financing cash flow, total','(23.47)','125.95','(52.92)'],
['End cash equivalents','0.22','81.01','1.67'],
['Equity issue proceeds','20.0²','126.0','0'],
],'numeric'),src(('AR',53),('R27',5),('R27',6),note='¹ Includes PPE/intangibles/CWIP/capital advances cash scope. ² FY25 issue shown in equity note; financing totals include many other flows. CFO excludes interest classified in financing.'))+
h('Why CFO divided by PAT looks unusually strong')+p('FY26 CFO of₹48.45 crore is3.26x PAT, but it is not all cash freely available to equity. Depreciation is non-cash, and interest is classified as financing. In H1 FY27, cash interest and other borrowing costs were about₹10.65 crore, plus₹0.53 crore loan processing fees. CFO less cash capex and the₹10.65 crore financing costs was approximately negative₹26.31 crore, before principal repayments and lease principal. That is the cash burden the investment thesis must eventually reverse.')+src(('AR',53),('R27',5),('R27',6))+
h('The H1 working-capital movement explains cash softness')+p('Profit before working-capital changes was₹31.915 crore. Inventory absorbed₹5.938 crore, receivables₹0.991 crore and other assets₹1.626 crore; lower payables absorbed₹1.162 crore. Other changes partly offset these uses. Cash generated before tax was₹23.692 crore; after₹1.756 crore tax paid, CFO was₹21.936 crore, below prior H1₹27.649 crore. Rising inventories after expansion require monitoring rather than an automatic quality red flag.')+src(('R27',5))+
note('The key question is whether post-ramp cash after interest can fund maintenance, remaining projects and principal. A strong CFO/PAT ratio alone does not answer it.'),tag='Cash conversion and funding',sources=['AR:53','R27:5-6'])

page('S17','Leverage fell after March, but near-term liquidity remains important','The debt definition is reconciled; the cash required to service it remains the central capital constraint.',
exhibit('Debt and cash reconcile once leases are separated',table(['₹ crore','Mar 2025','Mar 2026','Sep 2026'],[
['Borrowings excluding leases','195.00','234.42','194.56'],['Lease liabilities','8.94','10.03','9.33'],['Debt including leases','203.94','244.44','203.88'],['Cash equivalents','0.22','81.01','1.67'],['Cash-only net debt (calc.)','203.72','163.43','202.22'],['Other bank balances','3.26','11.63','25.13'],['Net worth','96.39','220.21','228.13'],['Current borrowings excl. leases','63.0¹','72.45','145.57'],
],'numeric'),src(('AR',52),('R27',4),note='¹ FY25 current borrowing rounded from deck. Other bank balances are not treated as freely distributable cash; IPO and deposit commitments require a separate bridge.'))+
h('Why a better debt ratio is not the same as lower net debt')+p('Gross debt excluding leases rose₹39.42 crore in FY26, while net worth more than doubled after the IPO. By September gross debt had declined₹39.86 crore, but cash equivalents fell₹79.34 crore, so cash-only net debt increased. The March cash balance included refinancing proceeds held temporarily; the May call explains subsequent repayment. It is wrong to describe all of this as recurring operating deleveraging.')+src(('AR',52),('C4',10),('R27',4))+
h('Capital productivity has room to recover')+p('FY26 revenue/closing total assets was0.52x versus0.72x in FY25 (calc.). Revenue divided by closing PPE plus CWIP was1.03x versus1.28x. The asset base expanded before commercial revenue. Using operating EBIT and average equity plus debt/leases less cash gives a simple FY26 pre-tax return on capital of about12%, broadly near Screener’s rounded12% but different from the company’s11.1% definition. These are definitions, not conflicting economic facts.')+src(('AR',52),'SC')+
h('Current maturities and refinancing deserve attention')+p('September current borrowings were₹145.57 crore versus₹48.99 crore noncurrent. The reclassification is not proof that all current borrowing is due immediately or callable; it includes working capital and maturities. However, the annual₹35 crore repayment agenda is material relative to current profit and cash. Continued access to lenders and successful project conversion matter.')+note('The business needs a sustained cash surplus before the debt story is fully self-funding. Our scenario equity bridge includes leases and avoids treating committed deposits as spare cash.'),tag='Debt, liquidity and returns',sources=['AR:52','C4:10','R27:4','SC'])

page('S18','An unmodified audit does not eliminate governance watchpoints','No audit qualification was identified; IPO timing, related-party transactions and contingent claims still warrant scrutiny.',
exhibit('Governance and accounting diligence register',table(['Item','Primary evidence','Assessment'],[
['Audit / controls','Price Waterhouse Chartered Accountants LLP: unmodified FY26 opinion. Tax contingencies are a key audit matter.','OK on opinion; do not call every accounting risk resolved.'],
['Audit trail','Database-level edit-log operation not independently verified; auditor notes no tampering observed.','WATCH. Evidence limitation, not an adverse audit opinion or a finding of manipulation.'],
['IPO use','Net proceeds₹103.1519cr; cumulative object use₹74.9543cr atSep30. Monitor reports schedule delays, no object deviation.','WATCH timing. Unspent~₹28.20cr is committed business funding, not automatically excess distributable cash.'],
['Related parties','FY26 land purchase from CMD₹1.0246cr; vehicle lease₹0.288cr; CSR foundation₹0.1191cr, CMD trustee.','WATCH. Approval/valuation and arm’s-length disclosures deserve review; no evidence of diversion established.'],
['Tax / other contingencies','Litigation₹16.9878cr, predominantly GST; separate potential customs duty₹7.1392cr under export obligations.','WATCH. Not booked debt; adverse resolution would consume cash. Avoid double-counting the separate exposures.'],
['Promoter-linked borrowing','Annual note describes company/director jointly availed bank loan and guarantees, with separate obligations.','WATCH transparency, terms and settlement. Do not classify as a loan to a promoter without the actual contract.'],
]),src(('AR',47),('AR',48),('AR',63),('AR',67),('AR',68),('AR',70),('AR',71),('MA',9)))+
h('Capital raised versus capital deployed')+p('The IPO raised₹126 crore gross. The monitor’s revised net proceeds are₹103.15 crore after₹22.85 crore issue costs, which differs from cash issue expenses paid within one reporting period. Those scopes must not be substituted. The September monitor records project timing delays associated with supply/payment and machinery-order finalisation. It relies on issuer and third-party information; it is not an independent audit of every expenditure.')+src(('MA',3),('MA',9),('AR',53))+
h('Latest ownership event, with a verification limit')+p('Screener’s document feed reports a 6November off-market acquisition of300,150 shares by Jitendrakumar Patel, with a9.79% stake in the filing summary. The direct BSE disclosure was not retrieved in this run, so this is not used as independently verified evidence of investment conviction or a market-price purchase. No unverified pledge-free assertion is made.')+src('SC')+
note('Overall WATCH. The report identifies specific issues without claiming misconduct or certifying governance as clean.'),tag='Governance and material disclosures',sources=['AR:47-48,63,67-68,70-71','MA:3,9','SC'])

page('S19','The downside travels through margin, timing and cash','Most risks reinforce each other: delayed high-value sales leave more fixed cost and debt against the existing business.',
exhibit('Risk transmission and observable thesis-break signals',table(['Risk','How it reaches earnings / value','Monitor / analyst threshold [E]'],[
['Line3demand or yield','Lower incremental sales; fixed costs and depreciation continue; stock absorbs cash.','Quarterly line sales versus ₹60cr FY27 aim; inventory rising faster than sales for two quarters.'],
['SVP transfer / registration','Defers high-value mix and export receipts while capex is spent.','FAT/installation/validation dates; Q1 FY28 slip without a funded revised plan.'],
['Polymer / energy / FX','Input inflation or imported-packaging cost outruns price realization.','Operating margin persistently below20% despite higher sales; no verifiable price-cost bridge.'],
['Quality / regulator','Sterility failure, recall or adverse inspection can stop supply, damage trust and raise remediation cost.','Formal regulator findings, recall disclosures and batch-release disruptions. No current event assumed.'],
['Working capital / credit','Production and exports consume inventories and receivables before cash.','CFO after financing interest fails to cover maintenance and debt service after ramp.'],
['Refinancing / rate','Large current maturities, input shocks or capex could keep debt expensive.','Debt reduction below cash budget; interest not declining after utilization stabilises.'],
['Governance / claims','Adverse tax/customs outcomes or related-party issues consume cash and compress multiples.','Material cash settlement; weak approvals/disclosure or object-use deviation.'],
['Valuation compression','Even better earnings can deliver poor returns if the multiple falls.','Compare achieved cash returns with the multiple embedded at ₹202.15.'],
]),src(('C2',7),('C2',10),('C2',12),('C2',13),('R27',4),('R27',5),('AR',67),('MA',9)))+
h('Raw-material sensitivity is meaningful')+p('The latest deck says the top ten suppliers account for76% of materials consumed and identifies imported plastic sourcing concentrated in South Korea and Thailand. FY26 materials consumed were₹96.93 crore, including₹39.65 crore packing material. A5% increase in the packing-material cost base, with no recovery or volume change, would reduce pre-tax earnings by roughly₹1.98 crore (illustrative calc.). This is not a forecast of a5% price move; it shows why pass-through timing matters.')+src(('P2',12),('AR',65))+
note('The thresholds are analyst monitoring rules, not reported breaches. The most informative warning is volume rising without margin or cash improvement.'),tag='Risks with early warning signals',sources=['C2:7,10,12-13','R27:4-5','AR:65,67','MA:9','P2:12'])

page('S19','A persuasive bear case does not require the factory to fail','A functioning plant can still deliver disappointing equity returns if sales ramp slowly and cash stays tied up.',
exhibit('Bull argument and the strongest counterargument',table(['Positive thesis','What could make it wrong','Evidence that would settle it'],[
['Capacity shortage is solved.','Demand may not absorb all output at the same price or mix; old-line sales can migrate.','Incremental sales and net unit realization, reconciled to group totals.'],
['The SVP mix will lift margins.','Products may launch later, with a low-value interim mix and licensing economics below expectations.','Qualified launches, product mix and repeat orders with a measurable contribution bridge.'],
['Solar structurally raises profit.','Savings may partly offset polymer inflation and added finance/depreciation rather than add to PAT.','Metered cost saving, funding and net project cash evidence.'],
['Debt/equity proves financial strength.','New IPO equity improves the denominator; cash balances can fund debt reduction temporarily.','Recurring post-interest, post-capex cash surplus and declining net debt.'],
['Technical superiority deserves a premium.','Hospital budgets, alternative systems and competition can erode premium pricing.','Sustained realized price, stable retention and superior capital returns.'],
]),src(('AS',1),('C2',5),('C2',8),('C2',14),('AR',52),('R27',4)))+
h('The highest-conviction negative fact')+p('FY26 operating EBITDA was essentially flat at₹59.86 crore despite the revenue increase. H1 FY27 CFO declined while capex remained heavy. These are observed outcomes. The strongest bear case is not that every product claim is wrong; it is that the earnings and cash benefit takes longer than the share price assumes.')+src(('AR',52),('R27',5))+
h('What would change our view positively')+p('Two or more quarters of clearly incremental Line3sales, better operating margin net of other income, and cash generation that reduces net debt without depleting committed project funds would materially strengthen the case. SVP product transfer and country-specific approvals would support a larger mix benefit. A lower share price could also improve prospective returns without any change to the business.')+
h('What would cause us to drop the thesis')+p('A material quality event, persistent project delays without a funded path, inventory growth unsupported by collections, or evidence of unfair treatment of minorities would impair the thesis. A valuation that requires every ambition to succeed leaves little room for ordinary manufacturing variability. We do not offset these risks with an assumed future glass-injectables venture.')+
note('The investment decision is about the probability, timing and price of owner cash. Optimistic product descriptions do not invalidate the cash-based counter-thesis.'),tag='Anti-thesis and decision tests',sources=['AS:1','C2:5,8,14','AR:52','R27:4-5'])

page('S20','Value the operating ramp, then deduct its funding','EV/EBITDA is the primary lens, with cash conversion and asset turnover as essential checks. The range is wide because the ramp is unproven.',
p('Amanta is a leveraged, asset-heavy sterile manufacturer entering a capacity ramp. PAT is sensitive to capitalisation, depreciation, interest and tax. We therefore value operating EBITDA excluding other income, rather than apply a P/E to a single quarter. This does not make capex free: net debt, post-interest cash and capital efficiency constrain the equity value. There is one operating segment and no subsidiary requiring a separate sum-of-the-parts valuation.')+src(('AR',54),('AR',74),('R27',3))+
exhibit('The model has a disclosed skeleton and explicit estimated bridges',table(['Driver','Disclosed anchor [G / reported]','Scenario treatment [E]'],[
['Existing business','FY26 revenue ₹287.68cr; historical low growth.','FY26 base held flat initially in Base; Bear weaker ramp; Bull legacy growth 3%, 6%, 9%.'],
['Line 3','₹60cr FY27 contribution expectation; ₹110cr optimal annual potential.','Bear 40/85/95; Base 60/110/110; Bull 65/120/120, FY27-29 in ₹cr. All incremental: displacement is a downside risk.'],
['New SVP','Q1 FY28 commissioning aim; ₹16cr illustration explicitly speculative.','No FY27 new-line sales. FY28/29: Bear 8/16, Base 16/32, Bull 30/60. Product timing and mix remain unverified.'],
['Operating margin','Two-year 25%+ company EBITDA aim includes other income.','Ex-OI OPM: Bear 20/21/22%, Base 23/25/25%, Bull 24/27/28%. Not firm annual guidance; Base is demanding.'],
['Debt and reinvestment','September net debt incl leases ₹202.22cr; projects consume cash.','Cash roll-forward, explicit WC and capex budgets; ₹23cr reserved deposit use over FY27-28 is assumed.'],
['Multiple','No objective fair multiple provided by filings.','11x/14x/17x judgments reflect execution and funding risk, not observed peer medians. Constant within each scenario.'],
]),src(('AR',52),('C2',5),('C2',14),('C2',15),('R27',4)))+
h('Revenue formulas, not invented PAT')+p('Sales = legacy revenue + incremental Line 3 + new SVP. Expenses = sales × (1 − OPM). PBT = operating EBITDA + other income − interest − depreciation. PAT = PBT × (1 − tax rate). EPS = PAT ÷ current 3.8829351 crore shares. Each projected line is marked E. The ₹9cr annual solar saving is already reflected within margin assumptions, never added a second time.')+
note('Do not treat a scenario as a forecast or its value as a present-value target. The tables value earnings and net debt at each March year-end; there is no probability-weighted fair-value claim.'),tag='Valuation method and discipline',sources=['AR:52,54,74','C2:5,14-15','R27:4'])

for name in ['Bear','Base','Bull']:
 c=MODEL[name]['inputs'];rs=MODEL[name]['rows']; ys=list(rs)
 hist=[]
 for fy,a in HIST.items():
  hist.append(dict(a,expenses=a['sales']-a['op'],opm=a['op']/a['sales']*100,tax_pct=(a['pbt']-a['pat'])/a['pbt']*100,pat_margin=a['pat']/a['sales']*100))
 keys=[('Sales','sales',1),('Expenses¹','expenses',1),('Operating Profit¹','op',1),('OPM %','opm',1),('Other Income','oi',1),('Interest','interest',1),('Depreciation','dep',1),('Exceptional expense²','exceptional',1),('Profit before tax','pbt',1),('Tax %','tax_pct',1),('Net Profit','pat',1),('EPS ₹³','eps',2)]
 rows=[]
 for label,key,d in keys:
  rows.append([label]+[f(a.get(key,0),d) for a in hist]+[f(rs[y].get(key,0),d) for y in ys])
 rows += [['PAT Growth %','n/c',f((HIST['FY26']['pat']/HIST['FY25']['pat']-1)*100)]+[f(rs[y]['pat_growth']) for y in ys],['PAT Margin %']+[f(a['pat_margin']) for a in hist]+[f(rs[y]['pat_margin']) for y in ys],['EV/EBITDA, x','-','-']+[f(rs[y]['multiple'],0)+'x' for y in ys],['Net debt incl leases ₹cr','-','-']+[f(rs[y]['net_debt']) for y in ys],['Target price / value ₹⁴','-','-']+[f(rs[y]['price'],0) for y in ys],['Total return vs CMP %','-','-']+[f(rs[y]['ret']) for y in ys],['Stock-price CAGR %⁴','-','-']+['n/a' if rs[y]['cagr'] is None else f(rs[y]['cagr']) for y in ys]]
 desc={'Bear':'Slower Line 3 sales, limited SVP conversion and weak margin keep net debt high. The lower multiple compounds the operating disappointment.','Base':'Line 3 reaches its disclosed revenue potential; SVP begins at the speculative ₹16cr illustration. A 25% ex-OI margin requires stronger mix and execution than demonstrated so far.','Bull':'Line 3 slightly exceeds the ₹110cr potential, legacy sales grow and SVP ramps faster. A 28% margin and 17x multiple require sustained differentiation and cash delivery.'}[name]
 page('S20',name+' case: earnings and per-share value by year',desc,
 exhibit(name+' scenario | ₹ crore except per-share, multiples and percentages',table(['March year-end','FY25 A','FY26 A']+ys,rows,'numeric smalltable'),src(('AR',52),('AR',70),('R27',3),note='A audited; E analyst estimates. FY25 PAT growth not comparable here (n/c): prior year is outside this precise audited model base.'))+
 p('¹ Operating Profit is EBITDA excluding other income; Expenses exclude finance, depreciation and tax. ² FY26 ₹2.63cr IPO charge is shown separately to reconcile PBT. No exceptional item assumed in E years. ³ Audited historical EPS uses weighted-average shares; E uses current issued shares. ⁴ Year-end undiscounted scenario value. CMP ₹202.15 on 9 Nov 2026; horizons 0.39, 1.39 and 2.39 years. FY27 return is not annualised. CAGR excludes dividends.')+
 h('What has to be true')+p(f'Line 3 sales [E]: ₹{c["line3"][0]}/{c["line3"][1]}/{c["line3"][2]}cr. New SVP [E]: ₹{c["svp"][0]}/{c["svp"][1]}/{c["svp"][2]}cr. Operating margins [E]: '+ '/'.join(str(x)+'%' for x in c['margins'])+f'. The {c["multiple"]}x exit multiple stays constant across the three years in this scenario; its difference across scenarios captures valuation compression or expansion as well as earnings risk.')+
 note('Read the cash-budget and sensitivity pages before using these values. Cash funding, replacement capex, registration and dilution can materially change the outcomes.'),tag=name+' scenario',layout='scenario',sources=['AR:52,70','R27:3','E:model'])

cashrows=[]
for name in ['Bear','Base','Bull']:
 for y,r in MODEL[name]['rows'].items():
  cashrows.append([name+' '+y,f(r['cashop']),f(r['capex']),f(r['fcf']),f(r['reserved_release']),f(r['net_debt'])])
page('S20','The equity bridge must carry the cash cost of growth','Profits do not automatically repay debt. Working capital and remaining capex can absorb most of the initial improvement.',
exhibit('Cash and funding bridge [E], ₹ crore',table(['Period','Cash after WC¹','Capex²','After capex','Deposit use³','End net debt'],cashrows,'numeric smalltable funding'))+
p('¹ Operating EBITDA less financing cost, tax and incremental operating WC. It is an accrual-based cash proxy, not a forecast cash-flow statement. FY27 is H2 only: actual H1 EBITDA, interest and tax accruals are removed from the full-year P&L bridge. September debt already incorporates H1 cash movements. Depreciation is noncash and is not deducted again. Negative cash raises net debt; surplus cash is swept against debt.')+
p('² FY27 ₹22cr is remaining H2 cash capex, additional to ₹37.60cr already spent in H1. FY28/29 budgets are ₹18/15cr in Bear/Base and ₹20/20cr in Bull. These are analyst budgets, not disclosed completion quotes. A ₹15cr maintenance/replacement envelope is included, not independently verified engineering cost. No future glass plant is funded.')+
p('³ ₹15cr in FY27 and ₹8cr in FY28 assumed use of bank deposits excluded from opening net debt. This is committed funding, not operating FCF or additional profit. The model does not also deduct those deposits from opening debt. The disclosed September other-bank balance is ₹25.13cr; monitoring-report unspent net IPO funds are ₹28.20cr on its separate scope.')+src(('R27',4),('R27',5),('R27',6),('MA',9))+
h('Working capital and financing assumptions')+p('Operating WC = inventories + receivables − trade payables − contract liabilities: ₹80.96cr in March, ₹89.77cr in September. FY27 year-end WC = March WC + revenue increase × assumed days/365; only the increment from September is charged in H2. Subsequent years apply days to incremental sales. Days are Bear150/Base141/Bull125, analyst marginal proxies. They do not reproduce the issuer’s 141-day definition; simple March operating WC/revenue implies about103 days.')+
p('Interest uses actual H1 plus opening September net debt × half-year rate for FY27; subsequent years use prior closing net debt × rate. Rates: Bear11/10.5/10%, Base10.5/9.5/9%, Bull10/9/8.5%. This net-debt shortcut omits gross-debt/deposit spread and intra-year timing. Tax rates29/28/27%; depreciation21/25/26cr Bear/Base,21/25/27cr Bull. Other income1.6/1/1cr. Lease additions zero; net debt includes existing leases. No dividends or new equity. This is a P&L and net-debt scenario bridge, not a fully balanced three-statement forecast.')+
note('The principal risk to the value is a funding miss: higher capex or WC can leave debt materially above the illustrated path even if reported PAT improves.'),tag='Funding assumptions and limitations',sources=['R27:4-6','MA:9','E:model'])

b=MODEL['Base']['rows']['FY28E']; sensitiv=[]
for m in [11,12,14,16,17]:
 sensitiv.append([str(m)+'x']+[f((b['sales']*o/100*m-b['net_debt'])/SHARES,0) for o in [20,23,25,27]])
req=(CMP*SHARES+b['net_debt'])/14
page('S20','The multiple and margin matter more than false precision','At the same FY28 revenue, a lower margin and multiple can erase much of the apparent upside.',
exhibit('FY28E value ₹/share | Base sales and net debt, varying operating margin and EV/EBITDA',table(['Multiple','20% OPM','23% OPM','25% OPM','27% OPM'],sensitiv,'numeric'))+
p(f'Sensitivity fixes FY28 sales at ₹{b["sales"]:.1f}cr and net debt at ₹{b["net_debt"]:.1f}cr to isolate valuation effects; it does not re-run cash and debt for different margins. Each ₹10cr additional net debt removes ₹{10/SHARES:.2f} per share. A 1 percentage-point operating-margin change on Base FY28 sales changes EBITDA by ₹{b["sales"]/100:.2f}cr and equity value by ₹{b["sales"]/100*14/SHARES:.1f}/share at14x, before taxes and cash feedback.')+
h('What the current price implies')+p(f'At ₹202.15, equity value is ₹{CMP*SHARES:.1f}cr. Add September cash-only net debt ₹202.22cr: EV is ₹{CMP*SHARES+202.2177:.1f}cr, or {(CMP*SHARES+202.2177)/HIST["FY26"]["op"]:.1f}x FY26 operating EBITDA. Using Base FY28 net debt, preserving today’s price at14x requires ₹{req:.1f}cr operating EBITDA, a {req/b["sales"]*100:.1f}% margin on Base sales. That is a no-price-return test, not an attractive-return hurdle.')+src('NSE',('AR',52),('R27',4))+
h('Capital-turn and cash sanity checks')+p(f'FY26 revenue divided by average FY25/FY26 total assets is about0.61x; revenue/closing PPE plus CWIP was about1.03x. The capital base grew ahead of sales. At Base FY28 sales, revenue divided by September PPE+ROU+CWIP+intangibles of about₹321.45cr would be1.29x, using a static denominator. Future capital additions and depreciation change that denominator. A ramp is plausible, but neither this ratio nor EBITDA proves an adequate return on incremental capital.')+src(('AR',52),('R27',4))+
h('Caveats required for use')+p('Management supplied capacity, broad timing and selected revenue/margin ambitions. Annual revenue paths, incremental attribution, interest, depreciation, tax, WC, capex, deposit release and valuation multiples are analyst estimates. Current shares remain3.8829351cr; no announced incremental dilution is assumed. A10% increase in shares would reduce per-share values by9.1% at unchanged equity value, before considering the cash raised. Multiples11x/14x/17x are judgments, held flat by year; they are not a peer-derived price target.')+
note('Not investment advice. The author is not a licensed financial advisor. These are conditional scenario bands, not forecasts.'),tag='Sensitivity, reverse test and caveats',sources=['NSE','AR:52','R27:4','E:model'])

answers=[
['1. Line 3 commercial change','5cr additional bottles/year removes a supply bottleneck. Full ramp by20Nov is an aim; sales, yield and collections must verify it. '+ref('P2',5),('C2',7)],
['2. ₹60cr versus ₹110cr','Partial-year sales expectation versus optimal annual potential;54.5% is not physical utilization. Net displacement remains undisclosed.',('C2',5)],
['3. Solar after finance/depreciation','₹9cr annual gross saving is management’s aim. Net saving depends on funding and depreciation; no audited project PAT bridge exists.',('AR',12)],
['4. Scale versus shareholder profit','₹83.13cr Q2 sales generated₹17.19cr ex-OI EBITDA, but₹5.84cr finance and₹5.28cr depreciation left₹4.86cr PAT. '+ref('C2',4),('R27',3)],
['5. SVP scale and timing','20.9cr units +10.8cr planned =31.7cr units/year; call rounds near31cr. Q1 FY28 sales still require qualification. '+ref('C2',4),('P2',5)],
['6. CAGR versus H1','12% H1 growth does not mathematically invalidate a multi-year20%+ aim, but requires acceleration; it is not exact annual guidance.',('C2',4)],
['7. Margin lift','More high-value mix, usable output, shared overhead and solar can help; resin inflation, transfer costs and debt can offset the gain.',('C2',8)],
['8. Pipeline to cash','Formulation/technology, validation, product-country permissions, licensing/customer orders and repeat sales must follow development. '+ref('C2',5)+', '+ref('C2',14)+', '+ref('C2',15),('C2',12)],
['9. Inhalation counts','Six discussed, two commercialised and additional six under development may overlap. No consistent molecule-level roll-forward is disclosed.',('C2',5)],
['10. International demand','About32% Q2 revenue; existing export relationships support the base. Registrations alone prove neither orders nor repeat demand.',('C2',4)],
['11. Funding the ramp','H1 CFO did not cover capex before interest. SVP, WC and principal repayments require cash, committed funds or financing; self-funding unproven. '+ref('C2',6),('R27',5)],
['12. Debt/equity improvement','The IPO lifted net worth; gross borrowings actually rose into March. The ratio is not evidence of equivalent debt retirement. '+ref('C2',3),('AR',52)],
['13. ₹420-430 versus ₹400-420','Latest call uses annualised and full-year wording and affirms FY28 range. Keep the ambiguity; do not impose one clean FY27 promise. '+ref('C2',14),('C2',10)],
['14. Approximate borrowing answer','₹190cr is approximate gross borrowing, not net debt. Official September borrowings₹194.56cr plus leases₹9.33cr less cash₹1.67cr gives₹202.22cr. '+ref('C2',6),('R27',4)],
['15. First thesis breaks / target','Unsold output and cash absorption would break first, followed by SVP delay/quality. Calls alone lack CMP and cash; expanded sources now permit conditional values.',('C2',14)],
]
for i in range(0,15,8):
 part=answers[i:i+8]
 page('S20','The original research questions, answered'+(' (continued)' if i else ''),'Each answer distinguishes reported evidence from the next assumption that an investor must test.',
 table(['Original question','Conclusion and evidence'],[[a,b+' '+ref(*r)] for a,b,r in part])+
 h('Dated evidence to watch')+p('20Nov2026: Line3 full-utilisation aim. Around19Nov: promised SVP outlook in roughly15days after the call, not a fixed filing deadline. 13-19Dec: planned factory acceptance test; January arrival and March commissioning preparation; Q1 FY28 commercial contribution aim. Calendar2027 product development and calendar2028 market-entry language are distinct from fiscal-year deadlines. These were future events at the analysis cut-off.')+src(('C2',7),('C2',9),('C2',12),('C2',14),('C2',15))+
 note('Update the thesis with actual commercial sales, contribution and cash. Change the assumed inputs when evidence changes, rather than retain the same target and change the story.'),tag='Prompt questions and monitoring',sources=['C2:4-15','AR:12,52','P2:6','R27:3-5'])

page('S20','Verdict: attractive mechanisms, a demanding cash test','WATCH / valuation-sensitive. The new line strengthens the business opportunity; the evidence has not yet established a durable cash return on the enlarged capital base.',
exhibit('Bull and bear side by side at 31 March 2028 [E]',table(['','Bear','Base','Bull'],[
['Revenue ₹cr']+[f(MODEL[n]['rows']['FY28E']['sales']) for n in MODEL],
['Operating margin']+[f(MODEL[n]['rows']['FY28E']['opm'])+'%' for n in MODEL],
['Net debt incl leases ₹cr']+[f(MODEL[n]['rows']['FY28E']['net_debt']) for n in MODEL],
['EV/EBITDA']+[str(MODEL[n]['inputs']['multiple'])+'x' for n in MODEL],
['Value ₹/share']+[f(MODEL[n]['rows']['FY28E']['price'],0) for n in MODEL],
['Return vs ₹202.15']+[f(MODEL[n]['rows']['FY28E']['ret'])+'%' for n in MODEL],
],'numeric'))+
h('Grounded versus assumed')+p('<b>Grounded:</b> commissioned SteriPort and solar assets, disclosed physical capacity, audited FY26 statements, official H1 results, selected product capabilities, project spending, and dated management statements. <b>Assumed:</b> all future demand/mix, the amount genuinely incremental, sustained operating margin, qualification timing, funding cost, cash conversion, maintenance needs and exit valuation. The scenario spread is evidence of uncertainty, not a price prediction.')+
h('Decision discipline')+p('For an existing holder, focus on the next evidence that can invalidate or strengthen the cash bridge. For a prospective investor, test a conservative margin and multiple before paying for the pipeline. A low apparent forward P/E can be misleading if its denominator assumes an unqualified product ramp. Higher volume is useful only if value per unit and cash collection survive.')+
h('Scope and reproducibility')+p('Research cut-off: documents available through9Nov2026; prepared10Nov2026. Latest annual report FY26; all four official publicly listed historical call transcripts and four matching investor decks located in the archive were read. Material commissioning, IPO-monitoring, management, remuneration and rating disclosures were reviewed. No older publicly listed call was located; this is an archive-coverage statement, not proof that none exists. Prices are dated, not live.')+
p('Source IDs on every page link to the original document, with physical PDF locators. The annual report places two printed pages on many PDF pages; physical locators avoid confusing printed and PDF numbering. The companion source manifest records local copies, URLs, SHA-256 hashes, coverage, and limitations. The editable HTML, model and verification summary accompany this report. The saved research prompt was executed with the user’s later expanded source instruction; it was not rewritten.')+
note('Not investment advice; not a licensed financial advisor. The valuation is a set of conditional scenarios. Verify new filings, current price and your own risk constraints before any investment decision.'),tag='Investment conclusion',sources=['AR','C3','C4','C1','C2','P3','P4','P1','P2','R27','MA'])

page('S20','Reading key and original document index','Original documents, reported facts, management ambitions and analyst estimates play different roles in this report.',
exhibit('Plain-language glossary',table(['Term','Meaning in this report'],[
['LVP / SVP','Large- / small-volume parenterals: sterile medicines given by infusion or injection. Capacity is stated in physical containers, not rupees.'],
['BFS / ISBM','Blow-fill-seal integrates forming, filling and sealing; injection stretch-blow moulding makes the SteriPort container.'],
['FAT / plant start','Factory acceptance test checks equipment before dispatch. Commissioning establishes operation; it does not itself establish qualified product sales.'],
['Registration / validation','Country/product permission and proof of a repeatable process. A site certificate is different from approval for each medicine and destination.'],
['Operating EBITDA / EBIT','Profit before interest, tax, depreciation and amortisation, excluding other income here. EBIT also subtracts depreciation/amortisation.'],
['EV / net debt','Enterprise value is equity value plus debt and leases less cash. Net debt here excludes other bank deposits until explicitly released in the model.'],
['Working capital / FCF','Cash tied in stocks and receivables less operating liabilities. Free cash requires a clearly specified deduction for capex, interest and tax.'],
['ROCE / CAGR','Return on capital employed tests profit against invested capital; definitions vary. Compound annual growth rate measures annualised change over a stated horizon.'],
['A / G / E / inferred','A audited actual; G management aim, not certainty; E analyst estimate. An inference is calculated or interpreted, not directly reported.'],
]))+
exhibit('Source IDs used beside claims; each link opens the original',table(['ID','Original source'],[
['AR',ref('AR')+' | Annual Report FY2025-26, physical PDF pages; many spreads contain two printed pages.'],
['C3 / C4',ref('C3')+' | 11Feb2026 call; '+ref('C4')+' | 19May2026 call.'],
['C1 / C2',ref('C1')+' | 6Aug2026 call; '+ref('C2')+' | 4Nov2026 call.'],
['P3 / P4',ref('P3')+' | Q3 FY26 presentation; '+ref('P4')+' | Q4 FY26 presentation.'],
['P1 / P2',ref('P1')+' | Q1 FY27 presentation; '+ref('P2')+' | Q2 FY27 presentation.'],
['R27 / MA',ref('R27')+' | interim official results; '+ref('MA')+' | IPO monitoring.'],
['AS / AP',ref('AS')+' | SteriPort start; '+ref('AP')+' | solar generation start.'],
['COO / AGM',ref('COO')+' | senior-management change; '+ref('AGM')+' | AGM approvals.'],
['NSE / SC',ref('NSE')+' | official dated closing price; '+ref('SC')+' | secondary historical/ownership snapshots.'],
['Peers',ref('GF')+' | Gufic capability; '+ref('DR')+' | Denis rating; '+ref('GS')+' / '+ref('DS')+' | secondary peer statements.'],
],'smalltable'))+
note('The downloadable source manifest adds hashes, local source paths, archive coverage and retrieval limits. The verification summary records numerical and visual checks; it is not an external audit opinion.'),tag='Glossary and source index',sources=list(SOURCES))
