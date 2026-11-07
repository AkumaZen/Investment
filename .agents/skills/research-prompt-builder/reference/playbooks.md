# Playbooks

Diagnose three axes, then layer any special situation and optional modules on top. The result decides what the report leads with, which sections are renamed, swapped or added, and the valuation metric (always confirmed against the `business-valuation-scenarios` Step 1 table).

## Axis 1: business model

Each entry: unit economics, the "separate X from Y" rule, the causal chain, valuation metric, likely peers, must-have charts. Peer lists are a starting point: confirm with `get_peer_comparison` and keep only companies that truly do the same thing.

### Consumer and store chains (from RBA)
- Unit economics: stores x sales per store per day x 365; store EBITDA; payback per new store; delivery vs dine-in.
- Split: same-store vs new-store growth.
- Chain: stores opened, ramp to mature sales, store EBITDA positive, overhead absorbed, company EBITDA and cash.
- Metric: EV/Sales while EBITDA is thin; EV/EBITDA (pre-Ind AS 116) once stable.
- Likely peers: Jubilant FoodWorks, Devyani International, Sapphire Foods, Westlife Foodworld.
- Charts: store count by format; SSSG by quarter; store EBITDA vs company EBITDA.
- S3 becomes "Formats and menu"; S9 becomes store capex and payback.

### Process manufacturing and gases (from Ellenbarrie, Savita)
- Unit economics: capacity x utilisation x realisation; spread over raw material, or contract price.
- Split: volume vs price or spread; merchant vs onsite; recurring vs one-time plant sales.
- Chain: capex commissioned, utilisation ramp, offtake, spread holds, cash.
- Metric: EV/EBITDA with fixed asset turnover as a check.
- Likely peers: Linde India for gases; Gulf Oil Lubricants, Castrol India and Tide Water Oil for lubricants and speciality oils.
- Charts: capacity timeline with utilisation; spread per unit; capex vs OCF.
- Contract terms (take-or-pay, pass-through) explained with who benefits.

### Pharma APIs and regulated products (from Anlon)
- Unit economics: molecules x volume x price; regulated vs semi-regulated mix; approvals as gates.
- Split: regulated vs rest of world; established vs new molecules; organic vs acquired.
- Chain: filing, approval, customer validation, commercial supply, margin mix shift.
- Metric: P/E for steady earners; EV/EBITDA if leverage or capex is moving.
- Likely peers: API makers with a similar molecule set and regulated-market mix, such as Aarti Drugs, Supriya Lifescience and IOL Chemicals; pick by molecule overlap.
- Charts: approvals held vs applied for; export share; revenue by molecule group.
- Primary checks: regulator databases for approvals and warning letters.

### Pre-revenue clinical biotech (from Suven)
- Unit economics: rNPV per molecule = market x peak share x price x probability of success, discounted.
- Split: cash burn vs pipeline progress; promoter vs external funding.
- Chain: trial result, next phase, partner or approval, launch, royalty or sales.
- Metric: rNPV and cash runway; never past earnings.
- Likely peers: few listed Indian peers; compare with global companies on the same mechanism or indication, and with comparable licensing deals.
- Charts: phase timeline; cash runway; plain phase-wise evidence tables.
- S3 becomes "Pipeline" with molecule cards and evidence grades; S9 swapped for trial spend and runway.

### Engineered products and auto components (from SEDEMAC, Balu, Kabra)
- Unit economics: design wins x volume per programme x content per unit; order book x execution rate.
- Split: new programmes vs existing; domestic vs export; product vs project.
- Chain: design win or order, validation, start of production, volume ramp, margin.
- Metric: P/E for steady earners; EV/EBITDA during a capex ramp.
- Likely peers: Uno Minda, Varroc, Sona BLW for auto electronics; Bharat Forge, Ramkrishna Forgings for forgings; for transformers and T&D, TARIL, Shilchar, Voltamp, Skipper and the user's transformer proxies watchlist.
- Charts: order book movement and execution; revenue by product family; capex tracker.
- Name the biggest product threat (such as EV for petrol-engine parts).

### Services and asset-light chains (untested: no saved prompt yet)
- Unit economics: centres x patients or clients per day x revenue per visit; or headcount x utilisation x rate.
- Split: same-centre vs new-centre growth; recurring vs one-time revenue.
- Chain: centre opened, patient ramp, centre EBITDA, overhead absorbed.
- Metric: P/E if profitable and stable; EV/EBITDA otherwise.
- Likely peers: listed healthcare and wellness chains with a similar centre model; name the closest and say how close.
- Charts: centre growth; revenue per centre; same-centre growth.
- S3 becomes "Service lines"; S9 becomes centre capex and payback; capacity means beds, centres or seats.

### Banks, NBFCs and insurers (untested: no saved prompt yet)
- Unit economics: loan book x spread minus credit cost minus opex; for insurers, premium x margin.
- Metric: P/B linked to RoE.
- Likely peers: lenders of similar size and segment (such as gold, MSME or housing).
- Charts: AUM growth, NIM, GNPA and NNPA, credit cost, RoA and RoE.
- S9 swapped for capital adequacy and funding.

## Axis 2: business story

| Story | Example | What the report leads with |
|---|---|---|
| Turnaround and control change | RBA | The new owner's plan and cash; "what changes now" right after S2 |
| What broke | Kabra | "What broke" right after S2 |
| Binary readout | Suven | Pipeline and cash runway first |
| Bought growth | Anlon | Organic vs acquired split, and the deal terms |
| Capex ramp and cash gap | Balu | Capex tracker and funding early |
| Margin spike | Savita | Whether the margin is spread luck or structural |
| Recently listed | SEDEMAC | RHP promises vs delivery, products first |
| Order-book driven growth | Power equipment makers | Order book quality, execution and raw material pass-through |

## Axis 3: sector

Terms to explain, metrics, regulators to check, peers and charts. For each sector, also name the peers to compare and the sector charts (use the matching business-model entry above for both):
- Pharma: DMF, CEP, ANDA, USFDA, EU GMP; USFDA and EDQM databases.
- QSR and retail: SSSG, ADS (average daily sales), store EBITDA, Ind AS 116.
- Industrial gases: ASU, merchant, onsite, take-or-pay, tonnes per day.
- Auto components: SOP, content per vehicle, PPAP, design win.
- Forgings and castings: tonnage, realisation per kg, export share.
- Lubricants: base oil spread, distribution reach.
- Power equipment: MVA, kV class, order book, L1 bidding, copper and CRGO steel pass-through, type testing (CPRI).
- Healthcare services: patients per day, ARPP (average revenue per patient), occupancy, AYUSH regulation.

## Special situations (layer on top)

- Control change or fresh cash pile (RBA): deep dive on the new owner and the use of cash.
- Share swap or related-party deal (Anlon): deal deep dive with valuation report and fairness.
- Recently listed (Anlon, SEDEMAC): use the RHP; objects of the issue vs actual use.
- Dilution or warrants (Balu, RBA): dilution maths and a diluted share count.
- Annual report only (Kabra): S11 becomes a statements register; S12 says no guidance.
- Big capex ramp (Balu, Ellenbarrie): capex tracker early in Part A.
- Promoter-funded cash burn (Suven): runway and promoter funding as a deep dive.
- SME platform listing: half-yearly results only, so quarterly tables become half-yearly; check migration to main board.

## Optional modules (only when they earn their place)

Forensic first pass; concall checklist; metrics checklist; catalyst scoring on top of the S13 table; stock price move map; sum of the parts; rNPV and evidence grades; comparable deal table; dilution maths; images from company documents.
