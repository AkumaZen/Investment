# Equity research reports: a measured design and analytical production manual

A full-corpus audit of seven reports, 239 physical PDF pages. Prepared 7 November 2026.

## 1. What this manual is and how an agent should use it

This is an original critical description of the reports' page construction and analytical organisation. It is not a reproduction of their investment research, an endorsement of their recommendations, or a verification of their historical financial forecasts. The design lessons are reusable; the companies' historical assumptions are not inputs for a new company.

Load sections 2-7 to choose a report family and build the operating argument. Load the appropriate publisher specification in section 3 before laying out pages. Use section 8 as the production contract. Consult the page-by-page audit for concrete precedents, not as a fixed 239-page template. A new company should get the pages its economics require.

Every source page has an individual audit entry with (a) its role, (b) observed composition, (c) analytical function and (d) a transfer instruction. The accompanying JSON contains those entries and measured font/geometry evidence in a form an agent can process, including 6,417 text-region rectangles with dominant font, size and available line-spacing measurements. Load the relevant report and page records selectively rather than inserting the entire JSON into every prompt. Extraction regions can merge chart labels or columns; they are measurement aids, not a semantic layout tree. The PDF and Markdown contain the same research; the JSON is a supporting specification.

### Evidence classes

- **Measured:** PDF page dimensions, embedded font names, font sizes, span positions, colour values and extracted word counts. These come from the actual files, not visual estimation.
- **Observed:** arrangement of text, tables, photographs, diagrams, chart grids, captions, headers, footers and page sequence. Every physical page was inspected in rendered contact sheets; representative layouts and important analytical pages received closer examination.
- **Interpretation:** why a composition helps a reader, what question a page answers and where its reasoning is weak. These are this audit's judgements.
- **Recommended:** reconstruction dimensions, safeguards, analytical workflow and acceptance tests for a new report. These are engineering decisions informed by the corpus.
- **Inferred process:** how a coherent report of this kind could be produced. PDF output cannot establish the original author's software, internal workflow, time spent, unpublished interviews or model construction history.

The audit extracts text and font evidence across the full PDFs and close-reads selected operating, model and valuation sections. It does not claim to independently validate every sentence or number in 239 pages. Chart text and disclosures count as extracted words; rasterised pages may contain substantial visible content but little or no extractable text.

### Corpus and precise page addressing

| ID | Report / publisher | Date on report | Physical PDF pages | Page-number convention |
| --- | --- | --- | ---: | --- |
| BF | Balu Forge / Nuvama Professional Clients Group | 21 May 2025 | 37 | Cover is physical 1; physical 2 is printed 1 |
| MP | MedPlus initiation / Keynote Capitals | 13 January 2025 | 31 | Physical and printed numbers generally match |
| CC | CCL Products / Keynote Capitals | 9 September 2024 | 28 | Physical and printed numbers generally match |
| EL | Elecon Engineering / Keynote Capitals | 2 May 2025 | 36 | Physical and printed numbers generally match |
| SU | Suprajit Engineering / Equirus | Cover 26 April 2022; interior 27 April 2022 | 44 | Cover is physical 1; physical 2 is printed 1 |
| AX | Building Materials / Axis Securities | 16 July 2025 | 54 | Cover is physical 1; physical 2 is printed 1 |
| MQ | MedPlus Q2 FY27 update / Keynote Capitals | 30 October 2026 | 9 | Physical and printed numbers generally match |

The page-by-page audit always uses physical PDF page numbers, starting at 1. Direct source links use `#page=N` in the same convention. Printed numbers are a separate field. This matters: asking an agent to copy Balu Forge page 14 without specifying the convention can select the wrong page.

## 2. The fundamental design: make the investment argument inspectable

### Three reading speeds, one consistent argument

**First pass: decide whether the company deserves attention.** The opening combines company identity, economic change, headline forecasts, valuation and a factual rail. A reader can locate the claim without reading the entire report. It is dense, not a large decorative cover disguised as a summary.

**Second pass: understand the mechanisms.** Business trees, product explanations, unit examples, segment chapters and comparative exhibits explain how the model works. The strongest pages connect an operational change to sales, costs, capital and cash. They do not simply enlarge a collection of ratios.

**Third pass: challenge the conclusion.** Detailed statements, assumptions, sensitivity, peers, ownership and risk evidence let the reader test the model. The report becomes useful when the reader can disagree precisely: with utilisation, price, margins, capital employed, share count or the valuation multiple.

A visually convincing report can still have weak evidence or inconsistent arithmetic. The correct goal is low effort to inspect a claim, not low effort to accept it.

### The houses solve different editorial problems

| Family | Actual organising choice | Strong use | Weakness to avoid |
| --- | --- | --- | --- |
| Nuvama BF | Executive argument, chart summary, thesis chapters, valuation, governance, background, statements | A company undergoing a specific operating/capital transformation | Repeated exhibits and growth figures that require reconciliation across text and charts |
| Keynote MP/CC/EL | Executive page, industry education, business operating manual, opportunities, risks, statements, valuation | An unfamiliar business where reader education is essential | Long context sections, repeated strengths and compressed statement tables |
| Equirus SU | Executive page, business map, division chapters, acquisitions, financial economics, options, assumptions, valuation, reference | A diversified business requiring segment and acquisition analysis | Extensive white gutters, very small labels and repeated background after valuation |
| Axis AX | Shared sector thesis and drivers, peer work, risks, management, repeated company mini-reports | Comparing companies under a common sector mechanism | Broad thematic prose, uneven density and some categorical comparisons drawn as lines |
| Keynote MQ | What changed, results table, monitoring charts, call explanations, revised model, history | A recurring earnings update for a known company | Missing explicit old-versus-new estimate bridge and a dense all-in-one statement page |

Do not average these into one visually inconsistent hybrid. Choose a base family, then borrow only compatible analytical components. A product teaching page can be inserted into a thesis-first report without inheriting every decorative feature of its source publisher.

### Actual sequence maps

BF: physical 1 cover; 2 executive memorandum; 3 contents; 4-5 chart summary; 6-15 operating and capital thesis; 16-17 valuation/sensitivity/risks; 18-20 governance and relationships; 21-30 business/industry/product reference; 31-33 statements; 34-37 authorship and disclosures.

MP: 1 executive; 2-5 pharmacy industry; 6-23 company, stores, distribution, products, diagnostics, management and peers; 24-25 opportunities; 26 challenges; 27 statements; 28 valuation; 29-31 publisher/disclosures.

CC: 1 executive; 2-6 industry and inputs; 7-18 company, business models, distribution, assets, people and peers; 19-22 investment drivers and commodity history; 23 risks; 24 statements; 25 valuation; 26-28 back matter.

EL: 1 executive; 2-6 products and end-market demand; 7-28 company and segment operating economics; 29-31 opportunity and risk synthesis; 32 statements; 33 valuation; 34-36 back matter.

SU: 1 cover; 2 executive; 3-4 business map and mix; 5-15 existing divisions; 16-20 acquisition and capital allocation; 21-23 financial economics; 24-26 adjacent products; 27 assumptions/sensitivity; 28 risks/governance; 29-31 valuation; 32-39 reference background; 40 decision recap/consensus; 41-43 statements; 44 disclosures.

AX: 1 cover; 2-4 summary and contents; 5-25 sector education and demand mechanisms; 26-27 valuation/peers; 28 risks; 29-30 management; 31 divider; 32-38 first company; 39-46 second company; 47-52 third company; 53-54 disclosures.

MQ: 1 executive update; 2 results and unit metrics; 3 operating chart dashboard; 4-5 call explanation; 6 forecast model; 7 rating history and definitions; 8-9 disclosures. A nine-page update contains only six pages before its largely administrative closing section; page count is not a depth measure.

## 3. Measured typography, page geometry and visual grammar

### Measurement rules

Coordinates are PDF points with a top-left origin for extracted positions. There are 72 points per inch. Text sizes such as 9.96 pt reflect the source PDF export; an implementation may use 10 pt. Bounding boxes describe visible text, not necessarily original text-frame geometry. Representative positions are not an assertion that every page uses exactly the same margins.

Fonts can be identified only where the PDF contains text. A raster cover or embedded corporate collage does not reveal its original font family or point size. The reports often place logos or an entire page background as images while keeping analytical text as editable vectors.

### Exact observed house specifications

| Element | Nuvama BF | Keynote MP/CC/EL | Equirus SU | Axis AX | Keynote MQ |
| --- | --- | --- | --- | --- | --- |
| Interior sheet | 595.32 x 841.92 pt | 540 x 780 pt | 595.32 x 841.92 pt | 595.44 x 841.68 pt | 594.72 x 842.40 pt |
| Main narrative face | Calibri | Calibri | FuturaBT-Light | ArialMT | ArialMT |
| Main narrative size | 9.96 pt; BF executive opening 9.48 pt bold | 9.96 pt, occasional 9.98 pt export variation | 9 pt; executive bullets 9.96 pt | 9 pt sector body; 8.04 pt on dense company entry pages | 10.08-10.10 pt |
| Main bold hierarchy | Calibri-Bold; 12 pt coral thesis headings | Calibri-Bold; normal subheads near 9.96 pt | Main headings often 14.04 pt Light; blue secondary heading 12 pt | Arial-BoldMT; 11.04-12 pt sections; smaller entry headings | Arial-BoldMT; section headings about 12.24-12.98 pt |
| Running/company title | 18 pt appears in recurring company labels | 15.96 pt running label; MP opening company title 18.96 pt | 8.04 pt running strip labels; 20.04 pt executive thesis banner | Compact branded header; company name often 9.96 pt | 13.70 pt opening thesis line; grey running title band |
| Analytical table / chart scale | Mostly 8.04-9 pt; selected captions 9.96 pt | Often 8.04-9 pt; statement grids as small as 6.96 pt | Often 8.04-9 pt | Often 8.04 pt tables; many source notes 6.48-6.96 pt | Results tables about 7.92-7.94 pt; statement grids 7.20-7.22 pt |
| Source-note style | Often small Calibri, black/grey | Calibri-Italic near 6.96 pt | FuturaBT-LightItalic around 8.04 pt, some smaller labels | Arial near 6.48-6.96 pt | Arial-ItalicMT around 7.20 pt |
| Dense legal text | 6.96 pt | Commonly 8.04 pt with smaller detail | 6 pt | 6.48 pt | Mostly about 7.92 pt |
| Dominant analytical accent | Navy #03002F; coral #F04E45 | Red #C00000 | Blue #064884; orange #F79646 | Magenta #AB2862 / #951A4E | Blue #39608E / #4E81BD |
| Secondary fills | #FAB8B5 / #FDEAE9 | #D69999 / #BE5E5E / pale red | #F2F2F2 / #D9D9D9 / greys | #D9D9D9 / #FCEBE0 / grey | #BCC9DF / #93A9CF / greys |

These are measurements of examples in the corpus, not a recommendation to use six-point labels. Do not scale a 540-point Keynote page to A4 while preserving tiny typography blindly. Select a new minimum readable size, then repaginate.

Axis's cover is 540 x 780 pt while its other 53 pages are approximately A4. Suprajit's cover differs slightly from its 43 interior pages. BF's 37 pages are consistently sized. Geometry is verified per page in the JSON.

### Reading columns and spacing: specific anchors

**BF thesis page physical 6:** ordinary prose starts near x=36.4 and extends to x=557.6, a text measure of roughly 521.2 pt. A 12 pt coral section heading sits near y=108.6. Body lines are 9.96 pt with baseline progression around 12.2 pt. Short bold subheads are similar in size to the body and obtain hierarchy through weight and spacing. The two lower exhibit captions begin around y=480.5. This is a full-width narrative plus paired-evidence composition, not a two-column newspaper article.

**BF executive page physical 2:** left opening spans roughly x=36.1-406.6. The right rail begins beyond that narrative area and extends close to the right margin. The financial table is aligned to the narrative column. The rail does not use equal-sized KPI tiles; each module takes the height required by its content.

**MP ordinary page physical 2:** text starts near x=23.0 and ends near x=341.0, a 318 pt reading measure on a 540 pt sheet. Body text is 9.96 pt with line progression near 12.8-12.9 pt. The large right gutter is intentional: it holds side notes, images or empty space. The running label begins near x=22.2, y=32.2 and is 15.96 pt bold. Content begins below the coloured rule near y=66. The house is not generally using two equal prose columns.

**MP executive page physical 1:** opening company title is near x=19.4, y=66.7 at 18.96 pt bold; subtitle is 12 pt. Main prose spans about x=19.4-348.0, while the right facts rail is approximately x=363-522. The page is narrower than A4, and this geometry is important to its appearance.

**SU segment page physical 5:** the main column starts near x=193.7 and reaches about x=575.8, leaving a broad left gutter. The section heading sits near y=51.6 at 14.04 pt. Narrative is 9 pt with line progression around 13 pt. Blue italic takeaways in the left gutter align vertically with the passage they interpret. Many tables and charts occupy the main column only; business maps and statement pages can span the full width. Copying the narrow column onto every page would waste space.

**AX sector-driver page physical 15:** main narrative begins around x=43.2 and extends to about x=442.7. A callout occupies approximately x=452-581. The full-width exhibits extend beyond the prose column. The 9 pt narrative has roughly 12.9 pt line progression. The report uses a narrow reading measure plus wider exhibits rather than shrinking all content into one fixed column.

**AX company-entry page physical 32:** left thesis spans approximately x=30.5-368; the facts rail is about x=391-551. Dense entry prose drops to 8.04 pt and differs from the 9 pt sector body. This density change is an observed compromise, not a good universal default.

**MQ executive page physical 1:** main prose spans approximately x=22.2-358.7 at 10.08-10.10 pt; the rail is approximately x=384-576. The opening thesis line is around y=96.5 at 13.70 pt. On physical 3, chart rows occupy roughly y=154-338, 380-569 and 610-799. This is a compact operational dashboard with a fixed two-column grid.

### Letterforms, weight and emphasis

The corpus mostly uses ordinary office/document sans-serif typefaces. Its professional appearance does not depend on an exotic font. Hierarchy comes from consistent alignment, modest size changes, bold subheads, colour used sparingly, and repeated table/exhibit conventions.

BF and older Keynote pages use bold opening paragraphs as a summary layer. Their body prose is largely black on white. Red/coral is used to distinguish argument structure, not to colour every important word. SU demonstrates that a light typeface can carry a serious report if the column and leading are consistent, although its light strokes and small size are less robust on low-resolution screens.

The old Keynote pale geometric background and BF diagonal/navy header are publisher identity devices. They are not necessary for good analysis. For an original report, keep your own identity and use a white analytical field. Do not copy brokerage logos, conviction stamps, signatures, regulatory registrations or a recommendation history that belongs to another firm.

### Recommended reconstruction tokens, explicitly not source measurements

For a new A4 PDF choose one primary face available in the runtime, ideally with regular, bold and italic files. If Calibri, Arial or Futura are unavailable, use an explicitly named substitute such as Carlito, Liberation Sans or a licensed equivalent and measure the changed line breaks. A visually similar substitute is not an exact typographic match.

| Token | Recommended starting value | Reason |
| --- | --- | --- |
| Sheet | A4 portrait, 595.28 x 841.89 pt | Standard reproducible output |
| Left / right analysis margins | 36 / 36 pt | Keeps a usable full-width table measure |
| Narrative body | 10 pt, 13 pt leading | Close to the readable company-report examples |
| Major thesis heading | 13-14 pt bold | Clear but does not waste vertical space |
| Subhead | 10 pt bold, 6-9 pt before | Weight carries hierarchy without giant headings |
| Exhibit title | 9-10 pt bold, up to two lines | Claims and units remain readable |
| Table text | 8.5-9 pt; 8 pt only for a deliberate dense appendix | Avoid statement-grid illegibility |
| Source / footnote | 7.5-8 pt | Useful at normal size; not hidden metadata |
| Normal paragraph gap | 5-7 pt | Distinguishes thought units without social-post whitespace |
| Two-chart gutter | 16-22 pt | Preserves independent labels and captions |
| Hairline rule | 0.35-0.6 pt | Structures data without a boxed dashboard look |
| Main colours | One dark ink, one accent, two neutral fills | Keeps semantic use of colour stable |

Numbers must use consistent precision and aligned columns. Do not use monospaced numerals as a substitute for alignment. Use the chosen font's tabular numerals if available. Reserve italic type for notes, attribution or a clear secondary reading layer; never italicise entire analytical pages.

## 4. Reconstruct representative pages, step by step

### 4.1 BF physical 4: a chart sequence that behaves like a model

The page has six small multiples, two columns by three rows. The top row establishes available production and the change in product economics. The next row converts those assets into sold output and unit value. The bottom row shows the resulting sales and operating profitability. In reading order the grid forms an argument; individual charts are not simply six attractive facts.

To reproduce the logic for a different manufacturer, create one common asset-and-output table first. Chart capacity by asset cohort; show which products the new equipment can make; then chart the utilisation/volume assumptions and realised price. Calculate revenue from the same inputs used by the model. Only after that should a margin chart be added, including cost offsets. A hospital would substitute beds, occupancy, patient volume, revenue per occupied bed and operating costs. A GPU cloud would substitute deployable capacity, availability, billable utilisation, realised rental rate and power/platform costs.

Titles should state what the data supports, with forecast language where needed. Use a consistent dark colour for the subject, a neutral colour for existing assets and an accent for additions. Keep chart positions and baseline labels aligned. Put units in the axis or subtitle; distinguish stock capacity from flow output. Use one clear source note per exhibit or a genuinely shared source note for a grid built from the same dataset.

The original is compact. If a title needs three lines or tick labels become unreadable, reduce the exhibit count or split the page. Six is an observed arrangement, not a sacred quota.

### 4.2 BF physical 6-8: opportunity, implementation and proof

Physical 6 moves from an external demand/supply condition to a company action, then supports the action with capacity/output evidence. Physical 7 adds the implementation detail: individual assets, commissioning and ramp assumptions. Physical 8 provides a reference table of physical equipment and peer scale. The three pages use different evidence densities for different tasks.

A new report needs three linked work products: an industry opportunity table, an asset-status ledger and a forecast input table. The opportunity table should show the geography, product, customer need, evidence date and competing supply. The asset ledger should show project, cost, process, nameplate capacity, status, commercial qualification and funding. The model should apply utilisation to the assets that are genuinely available during each period.

Write the narrative only after those ledgers exist. The reader should be able to trace a sentence about growth to an actual assumption, rather than find a generic phrase next to an unrelated factory photograph. Reconcile all dates across opening summary, project table and charts. Management target, analyst estimate and reported fact require distinct labels.

### 4.3 BF physical 14-15: explain a return ratio, then test its durability

These pages do more than display high returns. They investigate how the acquisition cost of machinery affects depreciation, accounting profit and the capital denominator, then ask how a new investment cycle changes that effect. The teaching structure is mechanism first, peer evidence second, normalisation third.

For another business create a short capital-base bridge: original investment, acquired assets, write-downs, goodwill, assets still under construction and replacement cost. Then define the return metric precisely. A high ROIC can reflect productive advantages, unusually low book cost, outsourced production, supplier funding or temporary working-capital conditions. Each interpretation implies a different future return profile.

Use a procurement or capital table above paired comparison charts; follow with an explicit forward qualification. Do not write that a ratio will normalise unless the forecast denominator and numerator support it. The source's design is strong because it invites this inspection, not because its historical assumptions are guaranteed correct.

### 4.4 BF physical 16-17: make the valuation arithmetic visible

The first page discusses peers and relative premiums; the next shows a calculation and an earnings/multiple sensitivity grid. It separates the question of what profit might be earned from what multiple might be paid. Dilution is a visible ingredient.

Build the target price from a common model: earnings attributable to owners divided by diluted shares, multiplied by a justified P/E; or enterprise value from operating earnings, adjusted for net debt and other claims, then divided by diluted shares. Use consistent dates and currency. Explain why the multiple differs from peers in terms of growth quality, returns, duration and risk.

The sensitivity grid should use actual recalculations, not manually coloured numbers. Label rows, columns, valuation horizon and the base cell. Add a genuine bear operating case when necessary: changing only the multiple does not model commissioning delays, lower volumes or funding dilution. The source includes a sensitivity surface, but that does not imply an evidence-based probability distribution.

### 4.5 MP physical 2 and 19: teach where profit comes from

Physical 2 locates the company in a value chain with annotations attached to the relevant participants. Physical 19 uses an equal-ticket comparison to explain why a different product ownership model changes the customer's discount and the retailer's gross profit. These are teaching pages with an analytical purpose: they prepare the reader to understand the later margin thesis.

For a new sector first identify the payment and risk flows. Who buys raw material? Who owns inventory? Who carries credit, warranty, expiry or returns? Who sets the final price? Then create a unit example with a common base. Reconcile customer payment less product cost to gross profit, then state which costs are excluded before EBITDA.

Use a compact table with one row per arithmetic step. Mark illustrative or undisclosed inputs. Avoid presenting an assumed cost as a reported figure. A gross-margin comparison does not establish net profitability if advertising, store labour, logistics or inventory losses differ. The value-chain diagram and unit table should be adjacent to the explanation, not relegated to an appendix the reader must search.

### 4.6 MP physical 10-12: separate network growth from cohort maturation

The report moves through outlet count, same-store growth, average store size, maturity stages and the age structure of the network. The insight is that new units and mature units contribute differently to profit. The charts make a growth-rate number interpretable.

Build monthly or quarterly store cohorts. Each cohort needs openings, closures, surviving stores, sales ramp, contribution ramp, initial investment and working capital. Consolidated sales is the sum of cohort sales, not total stores multiplied by mature-store revenue. A fast rollout can temporarily depress profit even when individual mature stores are attractive.

The sequence can transfer to hospital beds, hotel rooms, restaurants, factories or data-centre capacity, but the ramp curve must be researched separately for each business. Do not assume all assets mature on a pharmacy timetable. Use a cohort stacked bar and a profitability line only with clearly different axes and an explicit warning that correlation is not a causal proof.

### 4.7 CC physical 15-16 and 19-22: distinguish capacity, commodity revenue and cash

The facilities diagram and two capacity decompositions teach what is installed and where. Later pages discuss capex, leverage, commodity costs and margins. The same assets are viewed by geography and product, so those totals must reconcile; they must not be added together.

For another processor calculate physical production and contribution per unit before interpreting sales growth. Under pass-through contracts, a commodity price can inflate sales and receivables without the same improvement in profit. Conversely a falling input price can release working capital while reducing reported revenue. Plotting only sales and PAT can obscure this mechanism.

Build a site/product capacity ledger, a raw-material yield equation, pricing/pass-through assumptions, inventory and debtor requirements, then maintenance and expansion capex. A harvest phase after expansion is a forecast to test, not an automatic consequence of completing a factory. Credit terms and commodity volatility can absorb the expected cash release.

### 4.8 EL physical 10 and 18-20: commercial architecture before growth arithmetic

The standard-versus-engineered comparison explains how customisation changes delivery time and economics. The OEM pages then move from agreements to prototype conversion and target revenue contribution. These are separate mechanisms: a signed relationship, a qualified product and a repeat production order are not the same thing.

Build a programme funnel with stage, customer, product, qualification gate, expected serial date, mature annual value, expected margin and evidence. Model a ramp rather than assuming every agreement is mature on day one. Keep aftermarket, OEM and custom products separate when their margins and cash cycles differ.

This is also a cautionary example. The report's adjacent OEM discussion gives inconsistent revenue magnitudes across physical 18-19. A design audit can identify that the figures need reconciliation; it cannot choose the correct one without returning to the underlying company sources. Your agent must perform that reconciliation before borrowing the economic argument.

### 4.9 EL physical 23-26: explain a turnaround as a change in economics

The segment introduction explains the old project model. The next page identifies its problems and restructuring actions. Later pages show revenue, profitability and recurring aftermarket work. The structure makes a turnaround more understandable than simply charting a move from loss to profit.

For another turnaround make a before/after table: contract type, payment milestones, retention, working capital, fixed costs, utilisation, warranty risk and recurring share. Create a separate ledger of write-offs and cash settlements. Quantify what remains unresolved. A non-cash loss can still represent earlier capital destruction; calling it non-cash does not make it irrelevant.

Use a compact action timeline, a revenue/profit history and a cash-conversion check. Identify whether improved margins come from a different business mix, lower overhead, price recovery, cycle recovery or the absence of old losses. These mechanisms imply different durability.

### 4.10 SU physical 5-15 and 27: segment chapters should terminate in model inputs

The Equirus sequence gives each material division a demand/customer discussion, competitive economics and forecast endpoint. The consolidated assumptions page later exposes segment growth and margin inputs and tests margin sensitivity. This is the clearest reusable pattern for a diversified business.

For each segment use the same analytical questions, not necessarily the same page count: what is sold, to whom, on what terms, with what assets, under which cycle, at what return and with what disruption risk? End with the segment's forecast drivers. Consolidate only after intersegment eliminations, corporate expenses, financing and tax.

A segment sensitivity table should change one input and recompute the group. It should not list arbitrary upside/downside percentages. Preserve a common definition of EBITDA and return ratios. The broad left gutter can carry the one-sentence implication, but is optional; do not inherit its space cost when tables need a larger readable measure.

### 4.11 AX physical 15-21 and 42: macro and manufacturing need different proof

The sector-driver sequence links property activity, spending and demographics to building-material demand. The manufacturing-process page later explains how a specific company's product is made. Both are useful, but they answer different questions. A macro chart does not prove company execution; a process diagram does not prove demand.

Build a common sector driver sheet and a company exposure matrix. Identify which end markets, price tiers, regions and construction stages the company serves. Use time lags supported by the relevant product, rather than applying a single sector delay. For a production process annotate yield, cycle time, bottleneck, energy and quality only where evidence exists. Translate those constraints into the company model.

The sector report is a useful reference for modular chapters. It is less efficient when generic lifestyle prose or near-empty classification pages do not change the investment decision. Your agent should preserve the cross-company logic while shortening such material.

### 4.12 MQ physical 2-5: an update is a test of the earlier thesis

The update puts reported results, unit metrics and a short operating dashboard before detailed call takeaways. This is the right dependency: identify what moved, then explain why. A reader already familiar with the initiation does not need the entire pharmacy value chain again.

Create a results table with current quarter, comparable quarter and sequential quarter, plus the appropriate year-to-date period. Follow with recurring-profit reconciliation, thesis-driver KPIs, old versus new forecasts, changed valuation and unresolved questions. The source provides much of the monitoring information but does not supply a prominent old/new estimate bridge; the rebuilt version should.

Use the same underlying KPIs as the initiation wherever possible. If a metric definition changes, record the change and its effect on comparability. One-off benefits, wage changes, franchise economics and mix shifts belong in the explanation and model, not merely in a list of call highlights.

## 5. How much analysis is actually deep?

### Depth is a chain of evidence, not a page count

Level 0 is description: product names and corporate history. Level 1 is measurement: sales, margin and capacity. Level 2 is decomposition: volume versus price, mature versus new units, or segment versus group. Level 3 is explanation: why mix or cost changed. Level 4 is a model: how the mechanism affects future earnings and capital. Level 5 is falsification: what observation would make the estimate or thesis wrong.

The strongest pages in the corpus reach decomposition and mechanism. Selected assumption, cash, return and sensitivity pages make the forecast inspectable. Product photographs, biographies and long legal sections may help context or compliance but do not themselves add depth. Some thematic and competitive claims remain broad even when professionally typeset.

### Minimum evidence for recurring analytical claims

| Claim | Evidence needed before writing | Required calculation or test | Suitable exhibit |
| --- | --- | --- | --- |
| Capacity will create growth | Asset ledger, commissioning, qualification, demand | Capacity by period x utilisation x yield; constrain by orders/demand | Asset bridge plus output forecast |
| Product mix improves margins | Product/channel shares and contribution economics | Weighted mix bridge, net of overhead/logistics/marketing changes | Mix bars and margin bridge |
| A business has a moat | Customer qualification, retention, economics, competitive alternatives | Test durability and customer value; distinguish inputs from outcomes | Peer capability/economic matrix |
| Returns are superior | Consistent profit and capital definitions | NOPAT and average invested capital; book-cost/replacement-cost context | ROIC calculation and capital bridge |
| Cash conversion will improve | Receivables, inventory, payables, capex, tax | PAT-to-CFO and CFO-to-FCF reconciliation | Cash waterfall or table |
| An acquisition creates value | Price, funding, integration costs, operating outcomes | Per-share accretion, post-deal ROIC and cumulative cash | Deal ledger plus pre/post economics |
| Backlog creates visibility | Opening orders, intake, execution, cancellations | Roll-forward and time-to-revenue assumptions | Backlog bridge and maturity buckets |
| Valuation is attractive | Forecast, peer set, dated price and chosen method | Earnings/multiple or EV bridge; dilution and downside | Valuation table and sensitivity |
| Optionality matters | Commercial stage, rights, investment and customer proof | Separate base and contingent cases; avoid double counting | Stage-gated opportunity table |

These are recommended research requirements. They are not a claim that every source report fully meets them.

### An explicit test for ease of understanding

A reader should be able to answer the following from the first analytical page and its cross-references: What changes in the business? Why does it change? What evidence supports that? How does it affect owners' earnings and cash? What capital is needed? What is assumed in valuation? What would change the conclusion?

To test actual accessibility, ask a reader unfamiliar with the company to explain one key unit example, trace one forecast and identify one thesis-break condition. A report can be visually orderly while still requiring specialist accounting knowledge. The corpus is comparatively scannable; it is not automatically beginner-proof. Definitions of EBITDA, enterprise value, diluted shares, working capital and returns remain necessary where the audience needs them.

## 6. Page archetypes with concrete construction instructions

### A. Executive memorandum

Reserve roughly two-thirds of usable width for argument and one-third for reference, with a narrow gutter. Order the narrative as business identity, material change, two or three mechanisms, forecast consequence, valuation and principal uncertainty. A compact forecast table belongs at the bottom of the main column. The rail holds dated price, shares, market value, ownership and analyst identity. It must not become a row of equally weighted vanity KPIs.

Recommended content budget: about 450-650 words including facts and table labels at 10 pt, depending on the rail and sheet. BF physical 2 contains about 812 extracted words and is visibly very dense; that is an observed upper-density case, not a target. If body type must shrink, shorten or move detail.

### B. Business teaching page

Use a 310-360 pt main text measure with a side note gutter. Open with a 2-4 sentence definition. Place one dominant business tree, flow, process or unit example in the central field. Close with the economic implication and one limitation. If the diagram needs more than about eight labelled concepts, split it into levels or use a table. Prefer explicit payment and risk flows to decorative circular arrows.

### C. Driver-and-evidence page

Use the full body width for one short argument, then a table or paired exhibits. Each driver paragraph should contain a claim, mechanism, evidence and implication. Two exhibits should answer related questions: available capacity versus sold output, margin versus cost, orders versus execution. Do not pair unrelated positive facts just because both are bar charts.

### D. Chart summary page

Start from a fixed two-column grid. Use two or three rows according to title length, label complexity and narrative need. Keep plot areas, title baselines and sources aligned. Page count should increase before labels become unreadable. Each title states the supported finding or forecast. Historical and estimated periods need clear labelling beyond colour alone.

### E. Comparison table

Make the left descriptor column wide enough to avoid ugly wraps. Right-align numbers, use the same unit and period, and place a clear header band above. Use subtle zebra fills only when row tracking benefits. Bold the subject and key totals. Put comparability caveats before the table and methodological notes immediately below. A table must not imply comparability the research does not establish.

### F. Product and application reference

Use authentic isolated product images on white where possible, preserve aspect ratio, and give each a short function/customer caption. Pair the catalogue with economic relevance: share of sales, price tier, qualification stage or capital need. If these are unknown, say so. Corporate collages are reference material and often need redrawing into editable, legible components.

### G. Valuation and sensitivity

Show the calculation first, followed by justification, sensitivity and the material assumptions that could break it. A table is often clearer than a decorative target-price card. Keep method, fiscal year, horizon, currency, share count and claims on enterprise value explicit. Include a downside operating scenario if execution is uncertain; colour gradients do not supply scenario realism.

### H. Statements and audit trail

Use one common fiscal-year grid for income, capital, cash and ratios. Prefer separate legible pages to four statements squeezed into one. The detailed model should be available in a machine-readable or spreadsheet form when possible. Every chart should use these same model cells or tables. Use bold and hairlines for totals rather than a new colour for every section.

### I. Risk and monitoring page

Use rows for risk, mechanism, exposure, observable trigger, forecast effect and monitoring frequency. Distinguish a possible mitigation from one actually implemented. Put the material thesis-break risks in the executive page as well. A catalogue of ten generic risks is weaker than three mechanisms tied to the model.

### J. Quarterly change page

Lead with results and deviations, then recurring-profit reconciliation, changed drivers and forecast revisions. Keep the original business explanation available by reference. Use consistent monitoring KPIs so the reader can test earlier assumptions over time. A call transcript summary is supporting evidence, not the entire analytical product.

## 7. Transfer the structure to a different business

| Business model | Primary economic unit | Operating bridge | Capital/cash constraint | Important false inference |
| --- | --- | --- | --- | --- |
| Manufacturing | Sellable units or tonnes by product | Available capacity x utilisation x yield x realisation | Project timing, working capital, maintenance and replacement | Installed capacity is not sales |
| Retail chain | Store cohort | Surviving stores x cohort sales; product and format contribution | Opening cash, deposits, inventory, closures | Total stores x mature-store profit overstates the ramp |
| GPU/cloud provider | Billable resource-hour by hardware class | Deployable resources x available hours x billable utilisation x realised rate | Hardware delivery, power, customer contracts, depreciation and financing | GPUs installed are not billable or contracted demand |
| Pharma/API | Approved product/site/customer combination | Qualified capacity x yield x demand x price by molecule | Validation, regulatory approval, customer qualification, inventory | A filed dossier or installed reactor is not approved revenue |
| Hospital | Bed/specialty/location cohort | Operational beds x occupancy x revenue per occupied bed plus outpatient activity | Doctor availability, ramp losses, capex and payer collections | Licensed beds are not operating or occupied beds |
| Project engineering | Executable order by stage | Opening backlog + orders - execution - cancellation; margin by project | Milestone billing, retentions, guarantees, working capital | Backlog value is not next-year revenue or cash |
| Software/subscription | Paying customer/seat/usage cohort | Opening recurring base + new + expansion - contraction - churn | Acquisition cost, implementation, retention, stock compensation | Bookings, ARR, revenue and cash are not interchangeable |
| Financial services | Earning assets/deposits or managed assets | Average balances x yield/spread/fee rate, less credit and operating costs | Capital adequacy, funding, liquidity, credit losses | Industrial EBITDA/EV frameworks do not transfer mechanically |

Choose the economic unit before the template. For banks and insurers create a separate analytical model and page family rather than forcing an industrial ROIC and EV/EBITDA layout. Stable visual identity is compatible with very different financial questions.

## 8. A reproducible production process for your agent

### Stage 1: Freeze the brief and source perimeter

Set company, report type, audience, as-of date, valuation horizon, scope and source hierarchy. Obtain filings, presentations, transcripts, annual reports and project disclosures. Broker reports can teach structure; they should not replace primary evidence for a new company's claims. Keep a manifest with document date, reporting period and page location.

**Output:** source manifest and a list of critical questions. Do not begin by writing a glossy executive summary.

### Stage 2: Establish the business and entity maps

Identify product, customer, payer, channel, legal entity, geography and revenue recognition. Record which taxonomy each metric uses. Build an entity-contribution bridge where necessary. For a new sector, explain only the process steps needed to understand economics and risks.

**Output:** business map, process map and segment dictionary. Reject ambiguous segment names and unreconciled totals before modelling.

### Stage 3: Build evidence and operating ledgers

Create separate ledgers for capacity/status, customers/orders, prices/mix, costs, working capital, capex/funding, acquisitions, dilution and governance. Each input carries value, unit, period, perimeter, source, factual status and uncertainty. Preserve the original disclosure even when the narrative uses a rounded value.

**Output:** evidence ledger and an unknowns list. Label reported fact, management guidance, analyst assumption and calculation. Unknown inputs must not be silently filled from peer data or management adjectives.

### Stage 4: Build and reconcile the financial model

Forecast the economic unit and operating drivers first. Consolidate segment earnings, corporate costs, depreciation, financing, tax, minority interests and diluted shares. Forecast working capital, capex and funding. Derive all ratios and chart series from that model.

**Output:** a model that balances, cash that reconciles, and a clear actual/estimate boundary. Validate signs, fiscal periods, units and one-off treatment. A high-quality report cannot be recovered from an inconsistent model by good typography.

### Stage 5: Write the thesis and counter-thesis

Choose the two to four mechanisms that materially change expectations or value. For each write: change, cause, evidence, timing, earnings/cash implication and disconfirming evidence. Specify where your view differs from management, consensus or a simple historical extrapolation. When no consensus source exists, do not invent one.

**Output:** thesis cards as internal research records, not final decorative page cards. Each must terminate in a model input or an explicit qualitative limitation.

### Stage 6: Specify the exhibits before composing prose

For every important claim decide whether a table, trend, decomposition, flow, map, photograph or unit example best answers the question. Record source cells, chart type, units, period, title claim, actual/estimate treatment, footnote and reader inference. Remove redundant charts before layout.

**Output:** exhibit register. Repetition is justified only when a summary and a detailed explanation genuinely serve different reading speeds and share identical data.

### Stage 7: Build a page storyboard

Each page needs a question, supported answer, evidence, implication and handoff to the next page. Select an archetype and a density budget. Decide which sections are front matter, core argument, background, audit trail and legal back matter. Keep a full-disclosure appendix for material detail that does not deserve equal visual emphasis in the core argument.

**Output:** ordered page specifications. Do not force the same page count as a source report. The structure should respond to the new business and available evidence.

### Stage 8: Compose with explicit layout constraints

Apply a single chosen family of page dimensions, type roles, colours, rules, margins, tables and captions. Use reusable layouts for executive, explanation, chart grid, comparison, valuation and statements. Keep text and charts editable where possible. A deterministic renderer should handle layout; an LLM should supply the research structure, specifications and language.

**Output:** draft pages plus generated exhibits. Do not use image generation for exact charts or financial tables. Do not turn every paragraph into a rounded card.

### Stage 9: Run financial and editorial review

Recompute calculations independently. Check source attribution, management versus analyst language, valuation periods, diluted shares, margin definitions, units, and narrative-to-chart agreement. Trace every headline claim to its detailed evidence. Check contradictory facts across repeated pages.

**Output:** corrected model and narrative. Specifically test common traps found or suggested by this corpus: inconsistent growth rates, programme revenue magnitudes, mixed capacity units, EBIT/EBITDA definitions, unlabelled assumptions and mismatched current versus targeted mix.

### Stage 10: Render and inspect the actual pages

Review at normal reading size, then inspect dense tables and labels. Check clipping, collisions, orphaned headings, reading order, source-note association, alignment and whether colour has a stable meaning. Inspect page transitions, not only isolated pages. A long report needs both a complete contact-sheet pass and close examination of dense or novel layouts.

**Output:** a report with no unresolved layout defects and no hidden missing evidence. Page number, contents and links are regenerated only after the document is stable.

### Stage 11: Reader decision test

A reader should be able to explain the key mechanism, reproduce one calculation, name the main capital constraint and identify what would change the thesis. Measure whether the document supports that task, not whether it has a certain number of charts or an expensive-looking cover.

**Output:** final report, model/evidence package and watchlist. If the user asks for exhaustive transcript coverage, retain all material points in an indexed appendix and map them to the core thesis or an explicit non-material category.

## 9. Agent-facing production contract

Use this as a reference block in the report-generation agent. It is a specification, not an installed skill.

1. Research the business before choosing pages. Identify the economic unit, segment perimeter and revenue-recognition model.
2. Choose one visual family and declare page geometry, fonts, sizes, colours, column rules and table conventions. Do not mix all source houses.
3. Build a reconciled operating and financial model before writing forecasts. Maintain reported/guided/assumed/calculated labels internally and expose them where interpretation depends on them.
4. Specify each page as a question and supported answer. Give every exhibit a purpose, source, unit, period and limitation.
5. Write the executive page last. Include the material change, economic mechanism, earnings/cash consequence, valuation assumptions and thesis-break risk.
6. Include product/process education only when it makes a later economic claim understandable. Remove unrelated industry trivia.
7. Explain growth through the relevant inputs. Do not replace utilisation, pricing, cohorts, qualification or cash needs with the word tailwind.
8. Use unit examples and reconciliations for counterintuitive economics. Mark illustrative inputs and excluded costs.
9. Make valuation arithmetic inspectable and account for dilution, debt, leases, minority claims and horizon as appropriate. State why the method fits the business.
10. Keep forecasts and current facts distinct. Management ambition is not committed revenue; technical capability is not customer qualification; customer logos are not orders.
11. Preserve material contrary evidence. Explain capital requirements and cash conversion beside growth, not only in a dense appendix.
12. Render and inspect every final page. Split content before shrinking analytical labels below the declared legibility floor.
13. Keep the exhaustive evidence archive and the reader-facing argument linked but hierarchically different. Completeness does not require equal visual weight.
14. Use the new publisher's identity and authorised disclosures. Never inherit a broker's signature, registration, conviction label or historical recommendation series.
15. Deliver the report with its data/model and evidence trail when requested, so future quarterly updates can test the same thesis drivers.

### Page specification schema

```json
{
  "page_id": "thesis-capacity-ramp",
  "report_type": "initiation",
  "family": "thesis-first",
  "question": "Can the new assets produce the forecast sales on time?",
  "answer": "A supported conclusion expressed with its main condition",
  "evidence_status": "reported facts plus explicitly labelled assumptions",
  "layout": "narrative-plus-two-exhibits",
  "driver_inputs": ["available_capacity", "qualified_capacity", "utilisation", "yield", "realisation"],
  "exhibits": [
    {"id": "asset-ramp", "type": "stacked_bar", "units": "sector-appropriate", "source_cells": [], "forecast_boundary": "explicit"},
    {"id": "sales-bridge", "type": "table", "source_cells": [], "reconciles_to": "segment_revenue"}
  ],
  "interpretation": "What the evidence means for earnings, cash or valuation",
  "limitation": "The commercial or evidence dependency that remains unresolved",
  "source_refs": [],
  "next_question": "What capital and cost does the ramp require?",
  "qa": {"arithmetic": false, "source_checked": false, "visual_checked": false}
}
```

### Definition of done

Financial statements reconcile; every chart ties to the model; material claims have original evidence; dates/units/periods are explicit; observed and forecast series are distinguishable; no unresolved contradiction survives across summary and detail; valuation includes the relevant claims and dilution; critical unknowns remain visible; all pages have been rendered and checked; a reader can trace the argument and challenge it.

## 10. Specific defects to avoid inheriting from the references

- BF uses multiple growth descriptions across summary, prose and charts. The model and narrative require a reconciliation pass before a new report uses the same argument structure.
- EL's adjacent OEM discussion has an apparent order-of-magnitude inconsistency. Return to the original company disclosure before using either value; typography does not resolve it.
- Several older Keynote statement pages use approximately seven-point type for a full set of statements. The compactness is real; comfortable normal-size readability is not. Repaginate.
- SU's large annotation gutter and late background chapters help layered reading but create sparse pages and repeated context. Use the space only when the notes add interpretation.
- AX uses some line charts across company categories. Those lines imply continuity and ordering that companies do not possess. Grouped dots or bars are a better reconstruction.
- Some image-heavy catalogues and corporate process diagrams are rasterised. Their labels and source data cannot be assumed editable or reliably extractable.
- Generic phrases about market leadership, diversification, innovation and lifestyle change recur across the corpus. Require causal and company-specific evidence before treating these as thesis support.
- Product pictures, customer logos, biographies and market size are context. They become analysis only when connected to commercial evidence, economic consequence and limitations.
- Do not equate the presence of a risk section with a balanced model. Important risks need forecast transmission and observable thesis-break conditions.

## 11. Source register

The full downloaded files were used for this audit. Links point to the original hosts; publication dates and forecasts are historical. No original report text or page images are bundled into this manual.

- BF: https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf
- MP: https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf
- CC: https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf
- EL: https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf
- SU: https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf
- AX: https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental
- MQ: https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf

## 12. Full page-by-page audit

Each entry below is specific to one physical source page. Typeface and size lists are weighted by extracted character count on that page; they include tables and boilerplate and are not an automatic body-font classifier. Word counts include chart labels and legal copy and exclude text that exists only inside images. Frame coordinates and design interpretation should be read with the house specifications above.


### BF. Balu Forge - Nuvama


#### BF-01. Industrial identity and promise

**Source:** [BF, PDF page 1](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=1); printed unnumbered cover. **Measured:** 595.32 x 841.92 pt; 0 extracted words. **Type evidence:** raster page; original text font and point sizes are not measurable from embedded text.

**Observed layout.** A raster cover uses a navy upper-left field, a large coral sweep, white company title and a cropped machining photograph. Analyst details sit in a dark lower-left plaque.

**Analytical job / reader use.** The photograph establishes a tangible manufacturing context before any valuation argument. The large title carries identity rather than financial evidence.

**Instruction for the new report.** Use one business-specific photograph and one restrained identity block. A cover can be omitted when rapid analyst access matters. Do not treat a photograph as proof of capability.


#### BF-02. Compressed investment memorandum

**Source:** [BF, PDF page 2](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=2); printed 1. **Measured:** 595.32 x 841.92 pt; 812 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.48 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A narrow right rail holds stock facts and analyst contact; the wide left column contains a bold opening, short coral subheads, prose and a compact forecast table. The branding header and navy footer frame the page.

**Analytical job / reader use.** The reader can inspect the recommendation, operating argument and financial endpoint without advancing a page. Density is high: the opening does not explain every term.

**Instruction for the new report.** Write this page last. Reconcile every headline forecast with the detailed model. Keep the right rail factual and reserve the left column for the causal argument.


#### BF-03. Navigation into the argument

**Source:** [BF, PDF page 3](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=3); printed 2. **Measured:** 595.32 x 841.92 pt; 119 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 18 pt.

**Observed layout.** A single table of contents sits in the upper half with a navy column header, dotted leaders and right-aligned page numbers. The rest is deliberately empty.

**Analytical job / reader use.** The contents separates thesis, valuation, governance, context and statements. The report permits selective reading rather than assuming a linear read.

**Instruction for the new report.** Generate navigable links after pagination. Use physical and printed page numbers consistently; the unnumbered cover creates a one-page offset in this PDF.


#### BF-04. Operating thesis as six exhibits

**Source:** [BF, PDF page 4](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=4); printed 3. **Measured:** 595.32 x 841.92 pt; 231 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A two-column, three-row chart grid progresses through capacity, product economics, volumes, realisation, revenue and margin. Navy dominates quantitative marks; coral and grey distinguish components.

**Analytical job / reader use.** This is a compact visual model of the argument. Its sequencing matters more than the fact that there are six charts. Installed capacity and sold volume remain separate concepts.

**Instruction for the new report.** Build a chart sequence from operating inputs to outcomes. Keep units, forecast suffixes and data labels visible. Do not place six unrelated favourable KPIs in this grid.


#### BF-05. Relative economics and market context

**Source:** [BF, PDF page 5](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=5); printed 4. **Measured:** 595.32 x 841.92 pt; 248 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** The same six-chart grid compares profitability, depreciation and returns, then introduces price performance and a relative valuation history. Plot headers are declarative and similar in size.

**Analytical job / reader use.** The report changes from absolute growth to relative attractiveness. Cross-company ratios are used to explain why similar EBITDA economics can yield different bottom-line returns.

**Instruction for the new report.** Keep peer periods and definitions comparable. Price weakness and a historical multiple are context, not standalone evidence of cheapness or a future rerating.


#### BF-06. Demand opportunity to owned capacity

**Source:** [BF, PDF page 6](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=6); printed 5. **Measured:** 595.32 x 841.92 pt; 485 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A coral thesis heading precedes two explanatory blocks, a striped industry expansion table and two bottom charts. Paragraphs span the full body width; the exhibit pair forms the lower evidence band.

**Analytical job / reader use.** Industry supply disruption is connected to the company's acquisition and production ramp. A competitor table prevents the opportunity being presented as exclusive to one company.

**Instruction for the new report.** Use a demand-evidence paragraph, an action paragraph, a capacity bridge and a realistic volume forecast. Distinguish industry opportunity from orders already won.


#### BF-07. Commissioning and utilisation mechanics

**Source:** [BF, PDF page 7](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=7); printed 6. **Measured:** 595.32 x 841.92 pt; 650 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** The page interleaves dense prose, a short numbered machinery list, a defence subsection, two aligned charts and a closing integration paragraph. Chart labels remain outside heavy boxes.

**Analytical job / reader use.** Expansion is unpacked into machines, timing, utilisation and more valuable output. The closing paragraph adds the upstream integration mechanism rather than repeating the headline capacity figure.

**Instruction for the new report.** Create an asset-status ledger before writing: ordered, delivered, installed, trial, qualified and commercial. Never convert a planned line directly into revenue.


#### BF-08. Capacity and equipment verification

**Source:** [BF, PDF page 8](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=8); printed 7. **Measured:** 595.32 x 841.92 pt; 198 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9 pt, 9.96 pt, 8.04 pt.

**Observed layout.** Two charts occupy the upper row; a full-width machinery specification table follows. Navy table bands define categories, with alternating coral-tinted rows below.

**Analytical job / reader use.** The table supplies physical detail behind the investment thesis, while the peer bar chart places the expansion in scale context.

**Instruction for the new report.** For another industry use the actual productive constraint: racks, beds, reactors, stores or machines. Keep nameplate rating, output capacity and product size in distinct columns.


#### BF-09. Capability against named peers

**Source:** [BF, PDF page 9](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=9); printed 8. **Measured:** 595.32 x 841.92 pt; 584 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** Two broad comparison tables are separated by explanatory paragraphs. The page starts a second thesis section with coral hierarchy; dark table headers and shaded rows highlight the subject company.

**Analytical job / reader use.** A technical capability claim becomes inspectable against competing firms. The comparison moves beyond tonnage to the size and nature of components that can be processed.

**Instruction for the new report.** Choose technical metrics that a customer would use in supplier selection. Explain how each metric affects addressable work; do not equate largest equipment with strongest economics.


#### BF-10. Capability to product value

**Source:** [BF, PDF page 10](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=10); printed 9. **Measured:** 595.32 x 841.92 pt; 415 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 8.04 pt.

**Observed layout.** A small technical peer table leads into two side-by-side realisation charts and a lower product-mix comparison table. The text supplies the link between these exhibit groups.

**Analytical job / reader use.** This page attempts to bridge equipment capability into selling price and customer-sector mix. It is the economic interpretation of the preceding machinery detail.

**Instruction for the new report.** Model price as a consequence of product mix and commercial terms. Separate quoted management ambitions from analyst assumptions; volume and value units must not be confused.


#### BF-11. Revenue input assumptions

**Source:** [BF, PDF page 11](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=11); printed 10. **Measured:** 595.32 x 841.92 pt; 424 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Four charts form a two-by-two grid beneath a short forecast paragraph: capacity, utilisation, volume and price. The upper pair supplies constraints; the lower pair supplies revenue inputs.

**Analytical job / reader use.** The sequence makes the production model more transparent. Conservative utilisation is a claim that readers should be able to test against commissioning dates and historical ramps.

**Instruction for the new report.** Recalculate the implied volumes from capacity by asset cohort. Reconcile prose growth rates with chart endpoints; this report contains differing volume-growth descriptions across pages.


#### BF-12. Consolidated growth and end markets

**Source:** [BF, PDF page 12](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=12); printed 11. **Measured:** 595.32 x 841.92 pt; 556 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Two charts sit below the opening forecast discussion; the lower half uses bold inline sector labels with short paragraphs. A stacked chart separates group entities.

**Analytical job / reader use.** The report distinguishes group growth from the parent and subsidiary contributions, then explains possible new applications. Commercial maturity differs across the listed sectors.

**Instruction for the new report.** Use an entity bridge and an application-status table. Treat development, qualification, orders and sales as different evidence stages. Prevent optional businesses from silently entering base forecasts.


#### BF-13. Margin gains and cost offsets

**Source:** [BF, PDF page 13](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=13); printed 12. **Measured:** 595.32 x 841.92 pt; 286 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A wide multi-peer historical margin chart spans the middle; a paragraph interprets it; two smaller bottom charts show the subject's margin path and staffing costs.

**Analytical job / reader use.** Higher realisation is explicitly balanced against higher employment costs. This is useful because it prevents a revenue-growth story from automatically becoming a margin-expansion story.

**Instruction for the new report.** Build a margin bridge with positive and negative drivers. Where a headcount plan exists, connect hiring dates and wage assumptions to the cost line.


#### BF-14. Asset purchase economics

**Source:** [BF, PDF page 14](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=14); printed 13. **Measured:** 595.32 x 841.92 pt; 461 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 8.04 pt.

**Observed layout.** Narrative and a procurement table occupy the upper portion, followed by an explanation and two peer charts for depreciation and asset efficiency. Coral row fills do comparison work.

**Analytical job / reader use.** This page links asset acquisition cost to depreciation, PAT and return ratios. It identifies an accounting and capital-base mechanism rather than merely celebrating high profitability.

**Instruction for the new report.** Show acquisition price, asset condition, useful life and replacement capex separately. High accounting returns on cheap old assets are not evidence that replacement economics will be identical.


#### BF-15. Normalisation after expansion

**Source:** [BF, PDF page 15](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=15); printed 14. **Measured:** 595.32 x 841.92 pt; 200 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Two peer-return charts share the top half. A short paragraph underneath discusses how new assets entering service change depreciation and returns. A large lower white area remains.

**Analytical job / reader use.** The report qualifies an attractive historical ratio rather than extrapolating it unchanged. The page is a counterweight to the preceding return-comparison page.

**Instruction for the new report.** Keep the historical advantage and its fade visible together. Test return ratios on the future capital base, including working capital, rather than using only historic book values.


#### BF-16. Peer-based valuation rationale

**Source:** [BF, PDF page 16](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=16); printed 15. **Measured:** 595.32 x 841.92 pt; 457 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** Two paragraphs explain relative positioning above two wide peer tables. The subject, selected comparators and relative premiums receive row emphasis without large decorative cards.

**Analytical job / reader use.** Valuation is supported through differences in scale, mix and growth. The reader can inspect the rationale for a discount to one comparator and a premium to another.

**Instruction for the new report.** State the valuation date, fiscal year, peer subset and premium logic. A selected peer average must not be presented as an objective intrinsic value.


#### BF-17. Target-price construction and sensitivity

**Source:** [BF, PDF page 17](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=17); printed 16. **Measured:** 595.32 x 841.92 pt; 429 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** A valuation bridge table leads into a compact earnings-by-multiple heatmap. Supporting prose and numbered risks share the page. Colour intensifies around selected valuation combinations.

**Analytical job / reader use.** The valuation becomes a combination of earnings and multiple assumptions, while dilution and execution risks are visible nearby. This is more useful than displaying only one target price.

**Instruction for the new report.** Calculate diluted shares explicitly and label sensitivity axes. Add a genuine downside scenario when rebuilding; a heatmap is not a probability distribution or a substitute for bear-case operating assumptions.


#### BF-18. Governance examination

**Source:** [BF, PDF page 18](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=18); printed 17. **Measured:** 595.32 x 841.92 pt; 387 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 8.04 pt.

**Observed layout.** An opening assessment is followed by a director/pay table, a shareholding pie and committee-independence bars; a lower subsection introduces related-party items.

**Analytical job / reader use.** Governance is treated as a separate analytical topic rather than hidden in a generic risk paragraph. Board composition and financial relationships use different evidence formats.

**Instruction for the new report.** Separate disclosed structures from conclusions about behaviour. Independence percentages alone do not establish governance quality; date the evidence and record unresolved issues.


#### BF-19. Ownership through time

**Source:** [BF, PDF page 19](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=19); printed 18. **Measured:** 595.32 x 841.92 pt; 401 extracted words. **Type evidence:** Calibri-Italic, Calibri-BoldItalic; most-used sizes 6.96 pt, 18 pt, 11.04 pt.

**Observed layout.** A dense, almost full-page matrix uses many quarter columns and named owners. Navy, coral and a muted orange distinguish ownership categories and totals.

**Analytical job / reader use.** A time series reveals changes that a single shareholding pie cannot. The detail is available for readers who wish to trace dilution and investor turnover.

**Instruction for the new report.** Keep the first column wide, right-align share counts and distinguish percentages from absolute shares. Add a short interpretation when reproducing; a raw ownership dump is difficult to read.


#### BF-20. Related-party balance movements

**Source:** [BF, PDF page 20](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=20); printed 19. **Measured:** 595.32 x 841.92 pt; 154 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9 pt, 6.96 pt, 8.04 pt.

**Observed layout.** A short striped table occupies only the upper portion, with period columns and opening, movement and closing balances. Most of the page remains empty.

**Analytical job / reader use.** This is an audit-trail page, not a new thesis section. The movement structure helps the reader distinguish transactions during a period from balances at period end.

**Instruction for the new report.** Use a roll-forward and reconcile opening plus additions less repayments to closing. Add parties, terms, approvals and collection status where available rather than filling the blank space with decoration.


#### BF-21. Business context after the thesis

**Source:** [BF, PDF page 21](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=21); printed 20. **Measured:** 595.32 x 841.92 pt; 389 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Three short explanatory paragraphs sit above a two-by-two grid of geographic mix, sector mix, ownership and capacity. Existing exhibit styles recur.

**Analytical job / reader use.** Readers who started with the investment case now receive the business profile. Reused charts consolidate context but also create repetition across the document.

**Instruction for the new report.** Use this as optional background in a thesis-first report. Repeated exhibits need identical periods and definitions; otherwise combine them into a single authoritative exhibit.


#### BF-22. Subsidiary economics

**Source:** [BF, PDF page 22](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=22); printed 21. **Measured:** 595.32 x 841.92 pt; 251 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 14.04 pt.

**Observed layout.** A brief full-width text page profiles one operating entity and distinguishes the other entities. There are no charts or tables despite substantial unused space.

**Analytical job / reader use.** The group structure is clarified, including where current revenue is generated and where operations are not yet active.

**Instruction for the new report.** For a new business add ownership, revenue, profit, cash and intercompany flows in a compact entity table. Do not treat incorporation as evidence of an operating business.


#### BF-23. Leadership profiles

**Source:** [BF, PDF page 23](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=23); printed 22. **Measured:** 595.32 x 841.92 pt; 215 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 9 pt.

**Observed layout.** A two-column table pairs portraits and names with short biographies across three horizontal rows. Fine rules replace heavy coloured containers.

**Analytical job / reader use.** The reader can associate individuals with roles and experience. The portraits add recognition, not financial proof.

**Instruction for the new report.** Use concise experience relevant to execution. Add tenure, prior delivery and succession information; avoid copying promotional biographies as independent assessments.


#### BF-24. Industry opportunity evidence

**Source:** [BF, PDF page 24](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=24); printed 23. **Measured:** 595.32 x 841.92 pt; 505 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Explanatory paragraphs and a peer expansion table precede a discussion of disrupted overseas supply. The layout resembles the first thesis page.

**Analytical job / reader use.** The report supplies background for a macro premise already used in the thesis. This duplication reveals a layered reading strategy but can be shortened.

**Instruction for the new report.** In a new report cross-reference the earlier argument and add fresh evidence. Show whether competitors' expansions will also increase supply and pressure pricing.


#### BF-25. Geographic disruption illustrated

**Source:** [BF, PDF page 25](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=25); printed 24. **Measured:** 595.32 x 841.92 pt; 348 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A horizontal sector-loss chart occupies the top, a map the middle, and numbered economic drivers the lower section. Coral and navy connect the visual language.

**Analytical job / reader use.** Spatial concentration and sector exposure make a macro claim more concrete. The reader sees where the disruption sits rather than receiving only a broad geopolitical statement.

**Instruction for the new report.** Use a map only when geography is causal. Date it, identify the measured variable, and avoid assuming all disrupted output becomes orders for the subject company.


#### BF-26. Supply chains and process education

**Source:** [BF, PDF page 26](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=26); printed 25. **Measured:** 595.32 x 841.92 pt; 539 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A plant-action table and railway-capacity table divide text sections. The final block switches into plain-language manufacturing definitions.

**Analytical job / reader use.** The page connects demand and supply evidence before teaching technical distinctions needed to interpret the company. Its multiple functions make the hierarchy crowded.

**Instruction for the new report.** Split this into an opportunity page and a process explainer if content grows. Explain technical terms before using them to support a competitive claim.


#### BF-27. Process comparison

**Source:** [BF, PDF page 27](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=27); printed 26. **Measured:** 595.32 x 841.92 pt; 349 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** Short paragraphs compare production methods, followed by a broad application matrix. Navy headers and coral alternating rows preserve the house table system.

**Analytical job / reader use.** The reader learns why different equipment serves different applications. It is useful prerequisite knowledge for interpreting the earlier capability comparisons.

**Instruction for the new report.** Compare method, precision, throughput, component range and unit economics. Technical simplifications must be checked with a primary engineering source when used for a fresh company.


#### BF-28. Physical product catalogue

**Source:** [BF, PDF page 28](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=28); printed 27. **Measured:** 595.32 x 841.92 pt; 30 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 6.96 pt, 18 pt, 14.04 pt.

**Observed layout.** An image-led page presents labelled product families in an orderly multi-row grid. Corporate imagery carries most content; extracted text is minimal.

**Analytical job / reader use.** The products become recognisable to a non-specialist. The page builds vocabulary and physical familiarity but contains little independent financial analysis.

**Instruction for the new report.** Choose representative products and add their role, customer and economics. Preserve aspect ratios and legibility; do not stretch a low-resolution corporate collage to fill the page.


#### BF-29. Application catalogue

**Source:** [BF, PDF page 29](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=29); printed 28. **Measured:** 595.32 x 841.92 pt; 28 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 6.96 pt, 18 pt, 8.04 pt.

**Observed layout.** Two large corporate collages distinguish application families and show multiple components. Their own colours partly override the report palette.

**Analytical job / reader use.** The report makes adjacent business opportunities tangible. The collages show what can be made, not whether commercial scale or profits have been achieved.

**Instruction for the new report.** Attach operating status and revenue relevance to each family when adapting. Technical captions should be readable at normal viewing size.


#### BF-30. Equipment reference appendix

**Source:** [BF, PDF page 30](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=30); printed 29. **Measured:** 595.32 x 841.92 pt; 136 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9 pt, 6.96 pt, 18 pt.

**Observed layout.** Two relatively narrow specification tables sit in the upper half, grouped under forging and machining. The lower area is empty.

**Analytical job / reader use.** The machinery list provides a reference lookup after the visual product pages. It largely repeats earlier equipment detail.

**Instruction for the new report.** Maintain one authoritative equipment ledger and cross-reference it. If retaining the appendix, include provenance and status rather than duplicating unchanged rows.


#### BF-31. Income statement and operating ratios

**Source:** [BF, PDF page 31](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=31); printed 30. **Measured:** 595.32 x 841.92 pt; 302 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9 pt, 6.96 pt, 18 pt.

**Observed layout.** Three full-width tables stack income statement, common-size metrics and growth measures. Navy headers, coral alternate rows and bold subtotals organise the small type.

**Analytical job / reader use.** The model can be checked beyond the headline forecast. Common-size and growth views help identify assumptions embedded in raw rupee figures.

**Instruction for the new report.** Tie reported, adjusted and diluted earnings explicitly. Mark actual and estimated periods and keep the same fiscal horizon throughout the report.


#### BF-32. Return calculations and working capital

**Source:** [BF, PDF page 32](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=32); printed 31. **Measured:** 595.32 x 841.92 pt; 268 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9 pt, 6.96 pt, 18 pt.

**Observed layout.** Three stacked tables expose ROIC construction, ROE construction and operating ratios. The middle of each calculation is visible rather than only the final percentage.

**Analytical job / reader use.** The reader can inspect denominators and identify why returns are changing. This is a useful safeguard against interpreting all high returns as a superior operating moat.

**Instruction for the new report.** Define tax treatment, average versus closing capital, goodwill and cash exclusions. Recompute all ratios from the statement model; do not type them independently.


#### BF-33. Balance sheet and cash conversion

**Source:** [BF, PDF page 33](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=33); printed 32. **Measured:** 595.32 x 841.92 pt; 383 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9 pt, 6.96 pt, 18 pt.

**Observed layout.** The balance sheet occupies the upper portion and the cash-flow bridge the lower portion. All years share fixed column positions and consistent banding.

**Analytical job / reader use.** Growth is tested against funding and cash generation, adding a constraint to the earnings story.

**Instruction for the new report.** Reconcile the balance sheet, CFO, investing and financing flows. Put PAT-to-CFO conversion and cumulative capex beside the investment argument if they are material.


#### BF-34. Authorship and recommendation definitions

**Source:** [BF, PDF page 34](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=34); printed 33. **Measured:** 595.32 x 841.92 pt; 147 extracted words. **Type evidence:** Calibri, MyriadPro-Regular; most-used sizes 6.96 pt, 9.96 pt, 7 pt.

**Observed layout.** A sparse page combines contact information, a signature block, rating thresholds and a historical price chart.

**Analytical job / reader use.** The page supplies provenance and explains the vocabulary of recommendations. It is administrative support rather than company analysis.

**Instruction for the new report.** Use accurate authorship and definitions for the new publisher. Do not reproduce a broker signature, registration or rating history as though it belongs to the new report.


#### BF-35. Domestic disclosures

**Source:** [BF, PDF page 35](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=35); printed 34. **Measured:** 595.32 x 841.92 pt; 1335 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 6.96 pt, 18 pt, 8.04 pt.

**Observed layout.** Very small single-column text fills much of the page under the recurring header. Paragraph separation carries the hierarchy.

**Analytical job / reader use.** This page records report limitations, relationships and distribution terms. It explains why page count is not a measure of analytical depth.

**Instruction for the new report.** Keep authorised publisher-specific disclosures in a separate back-matter style. Do not reuse this very small type for analytical body text.


#### BF-36. Jurisdictional disclosures

**Source:** [BF, PDF page 36](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=36); printed 35. **Measured:** 595.32 x 841.92 pt; 1585 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 6.96 pt, 18 pt, 8.04 pt.

**Observed layout.** Long regional sections continue in small black type with bold labels. Visual rhythm is almost entirely textual.

**Analytical job / reader use.** The content concerns distribution rather than the operating thesis. Its density should not be imitated in decision pages.

**Instruction for the new report.** Preserve necessary legal text supplied for the intended publisher and jurisdiction. Let disclosure pages have a different density budget.


#### BF-37. Closing distribution terms

**Source:** [BF, PDF page 37](https://www.nuvamawealth.com/ewwebimages/WebFiles/Research/ee79d6e7-1853-4137-83d2-8bc15821d3b9.pdf#page=37); printed 36. **Measured:** 595.32 x 841.92 pt; 467 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 6.96 pt, 9.96 pt, 18 pt.

**Observed layout.** A shorter legal block occupies the top portion and ends with an emphatic warning; a large blank area follows.

**Analytical job / reader use.** The document ends when its required material ends, rather than inventing a conclusion to fill the sheet.

**Instruction for the new report.** Do not add fabricated analysis, signatures or affiliations to occupy remaining space. Blank area can be an honest consequence of pagination.


### MP. MedPlus initiation - Keynote


#### MP-01. Opening thesis with factual rail

**Source:** [MP, PDF page 1](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=1); printed 1. **Measured:** 540 x 780 pt; 652 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 9.98 pt.

**Observed layout.** The page uses a wide left narrative column and narrow right factual rail, under a red/black rule and a large wordmark. A conviction stamp overlaps the header area; red rules divide rail modules.

**Analytical job / reader use.** A reader sees the business, drivers, valuation and forecast summary in one place. The bold opening is visibly differentiated from the supporting discussion.

**Instruction for the new report.** Use a comparable information hierarchy but do not copy the broker's stamp or identity. Confirm that all headline economics match the later valuation page.


#### MP-02. Teach the value chain

**Source:** [MP, PDF page 2](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=2); printed 2. **Measured:** 540 x 780 pt; 311 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 9.98 pt.

**Observed layout.** An introductory paragraph leads to a vertical supply-chain diagram, with market-player and margin annotations. Explanatory prose follows below within the main column.

**Analytical job / reader use.** The reader learns where the retailer sits and who captures economics before seeing the company thesis.

**Instruction for the new report.** For another business explain payer, supplier, distributor and end customer. Put annotations on the relevant node; define whether margins are gross, operating or channel markups.


#### MP-03. Market size and channel taxonomy

**Source:** [MP, PDF page 3](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=3); printed 3. **Measured:** 540 x 780 pt; 194 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** A market-growth bar chart sits between plain-language industry context and a branching channel diagram. The right gutter stays mostly open.

**Analytical job / reader use.** The page answers both how large the market is and how it is organised, keeping sizing separate from business classification.

**Instruction for the new report.** State value versus volume, source year and forecast basis. Ensure the addressable market is the relevant segment rather than the entire adjacent industry.


#### MP-04. Channel economics and formalisation

**Source:** [MP, PDF page 4](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=4); printed 4. **Measured:** 540 x 780 pt; 310 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** Paragraphs and numbered subtypes explain traditional and digital models above a stacked-share chart. The chart has a small italic side takeaway.

**Analytical job / reader use.** The report distinguishes different fulfilment and inventory structures, then supplies evidence for channel share movement.

**Instruction for the new report.** Explain who owns inventory and bears returns for each channel. A category growth trend needs a company-specific route to participation.


#### MP-05. Retail model comparison

**Source:** [MP, PDF page 5](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=5); printed 5. **Measured:** 540 x 780 pt; 340 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 9.98 pt.

**Observed layout.** Numbered industry trends surround a red-headed comparison table of chain and independent-store economics. Small footnotes explain definitions.

**Analytical job / reader use.** A vague formalisation argument becomes a comparison of store size, sales, assortment, margins and investment requirements.

**Instruction for the new report.** Use a standard unit of business to compare competitors. Define denominators and avoid mixing gross margin with store-level EBITDA in the same conclusion.


#### MP-06. Company history and identity

**Source:** [MP, PDF page 6](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=6); printed 6. **Measured:** 540 x 780 pt; 429 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** Text explains the business before a large circular milestone diagram fills the lower half. The upper text remains in the narrow reading column.

**Analytical job / reader use.** The history establishes how the current model developed. The decorative circular chronology is less efficient than the surrounding analytical exhibits.

**Instruction for the new report.** Use only milestones that change economics, scale or capital structure. Prefer a straight timeline when event labels become difficult to place around a circle.


#### MP-07. Segment and product mix

**Source:** [MP, PDF page 7](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=7); printed 7. **Measured:** 540 x 780 pt; 190 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** A hierarchy diagram maps the main and ancillary businesses; a stacked product-mix chart follows; a lower text block interprets pharmacy operations.

**Analytical job / reader use.** The reader can distinguish operating segments from product categories. Their revenue shares answer different questions.

**Instruction for the new report.** Build two explicit taxonomies rather than treating segments and SKUs as interchangeable. Reconcile each mix to the same reported total.


#### MP-08. Store rollout and initial investment

**Source:** [MP, PDF page 8](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=8); printed 8. **Measured:** 540 x 780 pt; 343 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 8.04 pt, 9.98 pt.

**Observed layout.** A simple channel branch at the top leads into operating-process paragraphs and a capex discussion. A small right-side note explains the internal site-selection tool.

**Analytical job / reader use.** The report teaches how a store is opened and why that process can be replicated. Capital requirements are introduced before growth forecasts.

**Instruction for the new report.** Document site selection, approvals, fit-out, opening and cash break-even. Separate lease deposits, inventory and capitalised fit-out from recurring expenses.


#### MP-09. Store cost and franchise trade-offs

**Source:** [MP, PDF page 9](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=9); printed 9. **Measured:** 540 x 780 pt; 424 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 9 pt.

**Observed layout.** A compact cost table opens the page, followed by expansion, relocation and franchise-model paragraphs. The right gutter holds a rent-related note.

**Analytical job / reader use.** The reader can assess both investment per outlet and alternatives to company-owned growth. Failure and relocation costs appear alongside expansion.

**Instruction for the new report.** Show ownership model, initial cash, recurring cost, revenue share and risk bearer. Define how closures affect revenue and capital recovery.


#### MP-10. Store count versus same-store growth

**Source:** [MP, PDF page 10](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=10); printed 10. **Measured:** 540 x 780 pt; 264 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 8.04 pt.

**Observed layout.** A wide store-count chart sits above explanatory paragraphs and a smaller growth-rate table; a same-store-sales chart follows below.

**Analytical job / reader use.** Revenue growth is decomposed into more outlets and performance of existing outlets. These are different sources of growth with different capital needs.

**Instruction for the new report.** Build a store roll-forward and show gross additions, closures and net additions separately. Avoid applying same-store growth to new-store revenue.


#### MP-11. Store size and maturity ladder

**Source:** [MP, PDF page 11](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=11); printed 11. **Measured:** 540 x 780 pt; 189 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** A bar chart of average size leads into short interpretation and a large sequence of overlapping maturity circles. An otherwise open right gutter preserves the text width.

**Analytical job / reader use.** The sequence explains the delay between opening and mature profitability. It provides the mechanism behind the operating-leverage thesis.

**Instruction for the new report.** Use cohort economics with opening month, ramp sales, losses and break-even. Keep maturity assumptions separate from actual observed cohort performance.


#### MP-12. Cohorts and city-tier mix

**Source:** [MP, PDF page 12](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=12); printed 12. **Measured:** 540 x 780 pt; 289 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** A stacked cohort chart with a margin line occupies the top; three sequential doughnuts show city tiers below; explanatory prose follows.

**Analytical job / reader use.** The report relates age mix to profitability and distinguishes geographic expansion from cohort maturation.

**Instruction for the new report.** Keep percentage bases explicit. Matching trends do not establish causation; validate margin differences with cohort or store-level data where available.


#### MP-13. Cluster expansion geography

**Source:** [MP, PDF page 13](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=13); printed 13. **Measured:** 540 x 780 pt; 269 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A short explanation precedes a large India map with highlighted operating states and outlet labels. A small side note adds regulatory context.

**Analytical job / reader use.** The map makes adjacency and regional concentration visible, supporting the cluster-expansion explanation.

**Instruction for the new report.** Use maps when location affects logistics or customer density. Include an as-of date and a text/table alternative for small map labels.


#### MP-14. Regional scale and supply chain

**Source:** [MP, PDF page 14](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=14); printed 14. **Measured:** 540 x 780 pt; 344 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 9.98 pt.

**Observed layout.** A grouped state-level store chart occupies the top, with a substantial warehousing discussion below. Red shades encode annual series.

**Analytical job / reader use.** The report connects expansion patterns to replenishment and logistics rather than treating stores as independent assets.

**Instruction for the new report.** Translate network density into delivery frequency, warehouse cost and inventory implications. Too many similar red shades reduce year-to-year comparability; simplify if needed.


#### MP-15. Digital channel and fulfilment

**Source:** [MP, PDF page 15](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=15); printed 15. **Measured:** 540 x 780 pt; 207 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 9 pt, 6.96 pt.

**Observed layout.** A three-platform schematic and desktop/mobile screenshots occupy the top and middle; the lower paragraphs describe delivery and pickup.

**Analytical job / reader use.** The digital product becomes concrete, while the text explains the fulfilment model supporting it.

**Instruction for the new report.** Use a current product screenshot only to explain workflow or customer experience. For economics add delivery cost, basket size and fulfilment source.


#### MP-16. Online sales and channel strategy

**Source:** [MP, PDF page 16](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=16); printed 16. **Measured:** 540 x 780 pt; 384 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** A combined sales/share chart leads into several paragraphs explaining why the digital channel exists. The page continues the prior channel discussion.

**Analytical job / reader use.** Revenue share is separated from strategic purpose; an online channel can support store retention without maximising standalone growth.

**Instruction for the new report.** Specify whether digital is acquisition, convenience, retention or a separate profit centre. Avoid assuming higher online mix automatically improves margins.


#### MP-17. External user experience evidence

**Source:** [MP, PDF page 17](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=17); printed 17. **Measured:** 540 x 780 pt; 73 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 8.04 pt, 15.96 pt.

**Observed layout.** App ratings and selected review screenshots form an image-heavy page with short introductory commentary and small labels.

**Analytical job / reader use.** The report broadens evidence beyond management claims, but selected reviews are anecdotal and may not represent the full user base.

**Instruction for the new report.** Record capture date, sample method and review count. Use review evidence to identify questions for research, not as a reliable measure of company-wide service quality.


#### MP-18. Product ownership and revenue mix

**Source:** [MP, PDF page 18](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=18); printed 18. **Measured:** 540 x 780 pt; 223 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 9 pt, 8.04 pt.

**Observed layout.** A two-branch product diagram leads into a stacked mix chart, branded-product images and a discount table. A sidebar discusses purchasing relationships.

**Analytical job / reader use.** The reader learns that product ownership changes both margin and commercial risk. The examples make unfamiliar product categories recognisable.

**Instruction for the new report.** Define own label, third-party brand and category mix separately. Show returnability, expiry risk and procurement terms alongside gross-margin differences.


#### MP-19. Unit economics of own label

**Source:** [MP, PDF page 19](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=19); printed 19. **Measured:** 540 x 780 pt; 318 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 8.04 pt, 9 pt.

**Observed layout.** Explanatory paragraphs and product images precede a worked comparison table built on an equal ticket basis. The right gutter carries a sourcing note.

**Analytical job / reader use.** The strongest teaching device is the unit-level reconciliation from customer discount through cost to gross profit. It explains why customer savings can coexist with better retailer margin.

**Instruction for the new report.** Recreate the arithmetic using disclosed inputs. Mark assumed procurement costs explicitly; do not turn an illustrative basket into a forecast margin for all sales.


#### MP-20. Ancillary diagnostic model

**Source:** [MP, PDF page 20](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=20); printed 20. **Measured:** 540 x 780 pt; 306 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 15.96 pt.

**Observed layout.** A service-tier diagram sits between a prescription-fulfilment discussion and paragraphs on centre economics and subscriptions.

**Analytical job / reader use.** The report treats the ancillary segment as its own operating model, rather than presenting it as automatic additional upside.

**Instruction for the new report.** For each optional business state current scale, capital required, break-even, losses and strategic fit. Keep unrelated KPIs from competing for the same page hierarchy.


#### MP-21. Ancillary performance and limits

**Source:** [MP, PDF page 21](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=21); printed 21. **Measured:** 540 x 780 pt; 93 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 9 pt.

**Observed layout.** A small revenue/EBITDA chart occupies the top, followed by an outlook paragraph. Most of the lower page is unfilled.

**Analytical job / reader use.** The page gives an economic check on the ancillary story and acknowledges limited expansion intentions.

**Instruction for the new report.** Pair optionality with observed profitability and management's actual commitment. Do not fill the blank space with speculative TAM claims.


#### MP-22. Management and ownership evidence

**Source:** [MP, PDF page 22](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=22); printed 22. **Measured:** 540 x 780 pt; 240 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 11.04 pt.

**Observed layout.** Three red-headed tables stack management roles, compensation/ownership and major shareholders. Fine rules make the dense page navigable.

**Analytical job / reader use.** The reader can inspect execution responsibility and financial alignment in one place.

**Instruction for the new report.** Include tenure and relevant delivery history. State dates and ownership bases; compensation as a share of profit needs consistent consolidated or standalone definitions.


#### MP-23. Peer comparison with limitations

**Source:** [MP, PDF page 23](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=23); printed 23. **Measured:** 540 x 780 pt; 199 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9 pt, 9.96 pt, 6.96 pt.

**Observed layout.** A short caveat about imperfect peers precedes a broad matrix of operating-model and financial metrics.

**Analytical job / reader use.** The report acknowledges that nominal peers may combine hospitals, pharmacy or online businesses and therefore be economically different.

**Instruction for the new report.** Explain comparability before displaying multiples. Segment-level comparison is preferable to comparing unlike consolidated businesses without adjustment.


#### MP-24. Expansion opportunity revisited

**Source:** [MP, PDF page 24](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=24); printed 24. **Measured:** 540 x 780 pt; 225 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** Two charts show additions and sales per store alongside mature-store share, with explanatory paragraphs between and below.

**Analytical job / reader use.** Earlier business education is assembled into a thesis about output from the installed store network.

**Instruction for the new report.** The thesis page should reference, not restate, the complete operating manual. Calculate mature-store share from cohorts and connect it to sales per store transparently.


#### MP-25. Expansion and own-label forecast logic

**Source:** [MP, PDF page 25](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=25); printed 25. **Measured:** 540 x 780 pt; 382 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 11.04 pt.

**Observed layout.** Text-led continuation discusses future openings, new regions and margin mix. Bold subheads separate the two opportunity mechanisms.

**Analytical job / reader use.** The report now turns descriptive history into expectations. This is where management aims and analyst assumptions must be distinguished.

**Instruction for the new report.** Publish a driver table: openings, closures, mature share, same-store growth and own-label mix by year. Record which inputs are guided versus modelled.


#### MP-26. Specific failure mechanisms

**Source:** [MP, PDF page 26](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=26); printed 26. **Measured:** 540 x 780 pt; 433 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 15.96 pt, 12 pt.

**Observed layout.** Three bold subheads introduce competition, promoter-level debt exposure and store closures. The page uses restrained text rather than warning cards.

**Analytical job / reader use.** Risk is attached to a mechanism: discounting, pledged ownership or failed unit economics. The distinction between promoter and company liabilities matters.

**Instruction for the new report.** For each risk state trigger, transmission into earnings or capital, observable indicator and thesis consequence. Avoid treating separate legal entities' debts as interchangeable.


#### MP-27. Compact complete financial model

**Source:** [MP, PDF page 27](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=27); printed 27. **Measured:** 540 x 780 pt; 716 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 6.96 pt, 6.98 pt, 15.96 pt.

**Observed layout.** Two tightly packed columns contain income statement/balance sheet and cash flow/ratios. Small red header bands subdivide the tables.

**Analytical job / reader use.** The reader has a complete model reference, but normal-size screen readability is poor. High information density creates a practical accessibility trade-off.

**Instruction for the new report.** Provide the detailed model separately or split across pages if labels become unreadable. Never achieve a compact report by reducing analytical table text to disclosure size.


#### MP-28. Valuation bridge and synthesis

**Source:** [MP, PDF page 28](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=28); printed 28. **Measured:** 540 x 780 pt; 272 extracted words. **Type evidence:** Calibri, MyriadPro-Regular; most-used sizes 9.96 pt, 9.98 pt, 9.92 pt.

**Observed layout.** A narrow valuation table sits above thesis-synthesis paragraphs and a digital signature. The table moves from operating earnings to enterprise and equity value.

**Analytical job / reader use.** The valuation endpoint is connected to the store and product assumptions developed earlier. Cash, debt and share count are visible components.

**Instruction for the new report.** Specify lease treatment and valuation-year consistency. Reconcile EV to equity and diluted shares, then add sensitivity rather than only a point estimate.


#### MP-29. Publisher catalogue and definitions

**Source:** [MP, PDF page 29](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=29); printed 29. **Measured:** 540 x 780 pt; 512 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 8.04 pt, 1.2 pt, 11.04 pt.

**Observed layout.** Three report-cover thumbnails occupy the top; rating methodology and initial disclosures fill the lower area.

**Analytical job / reader use.** This is publisher navigation and administrative context, not additional company research.

**Instruction for the new report.** Keep such material optional in an independent research product. Do not inflate perceived analysis depth by counting promotional back matter.


#### MP-30. Conflicts and distribution disclosures

**Source:** [MP, PDF page 30](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=30); printed 30. **Measured:** 540 x 780 pt; 866 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 8.04 pt, 8.06 pt, 9.96 pt.

**Observed layout.** A bordered disclosure matrix and small text sections occupy most of the page. The report's recurring red rule and footer remain.

**Analytical job / reader use.** The matrix makes yes/no relationship disclosures easier to inspect than dense paragraphs alone.

**Instruction for the new report.** Use accurate publisher-specific facts and authorised text. Maintain a separate legal template with versioning.


#### MP-31. Closing disclaimer and contact details

**Source:** [MP, PDF page 31](https://files.keynotecapitals.com/research/2025/01/Initiating-Coverage-Report-Medplus-Health-Services-Ltd.pdf#page=31); printed 31. **Measured:** 540 x 780 pt; 893 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 8.04 pt, 8.06 pt, 9.96 pt.

**Observed layout.** Small prose fills the upper and middle portions with contact information below. The page retains ample lower space.

**Analytical job / reader use.** The final page concerns use and limitations of the document, not a final investment conclusion.

**Instruction for the new report.** Do not copy the brokerage's legal identity or registration into a new report. Separate legal completeness from analytical page count.


### CC. CCL Products - Keynote


#### CC-01. One-page investment entry

**Source:** [CC, PDF page 1](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=1); printed 1. **Measured:** 540 x 780 pt; 582 extracted words. **Type evidence:** Calibri-Bold, Calibri; most-used sizes 9.96 pt, 8.04 pt, 9.98 pt.

**Observed layout.** The familiar Keynote left narrative and right facts rail combine a bold business description, thesis subheads, small financial table and relative-price chart. Red rules define modules.

**Analytical job / reader use.** The complete argument is visible at first glance, but readers unfamiliar with coffee require the education on following pages.

**Instruction for the new report.** Summarise business mix, capacity, earnings logic and valuation in the same order used later. Write the opening only after the detailed analysis is stable.


#### CC-02. Physical product education

**Source:** [CC, PDF page 2](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=2); printed 2. **Measured:** 540 x 780 pt; 305 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 9.98 pt.

**Observed layout.** A narrow text column explains the raw product and processing; small annotated bean photographs use the right gutter; a larger product photograph sits below.

**Analytical job / reader use.** The report establishes vocabulary so later differences in production methods and margins are understandable.

**Instruction for the new report.** Choose photographs that explain an actual product distinction. Define the technical words that will later change economics; remove unrelated industry trivia.


#### CC-03. Production methods and market geography

**Source:** [CC, PDF page 3](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=3); printed 3. **Measured:** 540 x 780 pt; 186 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 8.04 pt.

**Observed layout.** Paired photographs compare two instant-coffee methods above a global-market paragraph and geographic table. Each method has a short plain-language explanation.

**Analytical job / reader use.** The reader learns that visually similar products can have different processing costs and market positioning.

**Instruction for the new report.** Compare input, process, output, capex and unit margin. A picture explains appearance; a cost or customer specification explains economic relevance.


#### CC-04. Inputs, conversion and supply concentration

**Source:** [CC, PDF page 4](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=4); printed 4. **Measured:** 540 x 780 pt; 244 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 9 pt.

**Observed layout.** A small market-segmentation table opens the page; raw-material paragraphs and a country production bar chart follow.

**Analytical job / reader use.** The report identifies the key commodity and the geography of supply. A conversion relationship links raw inputs to finished output.

**Instruction for the new report.** Build a material-yield bridge and sourcing-risk table. Keep green-bean volume, finished-product volume and currency pricing bases distinct.


#### CC-05. Consumer behaviour and category trends

**Source:** [CC, PDF page 5](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=5); printed 5. **Measured:** 540 x 780 pt; 423 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** Several compact prose blocks and a brief bulleted list occupy the main column; a small italic definition uses the right gutter.

**Analytical job / reader use.** The narrative explains why formats and preferences may change. Much of this is contextual rather than company-specific evidence.

**Instruction for the new report.** Connect each proposed trend to observed channel data, a product mix or a measurable business driver. Cut themes that do not change the model.


#### CC-06. Domestic market context

**Source:** [CC, PDF page 6](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=6); printed 6. **Measured:** 540 x 780 pt; 195 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 15 pt, 12.96 pt.

**Observed layout.** A short text block occupies only the upper-left main column, with most of the page blank.

**Analytical job / reader use.** The page narrows the broad global market to the domestic branded opportunity. Its isolation produces weak information density.

**Instruction for the new report.** Combine this with a domestic competitor/share exhibit or the subsequent company page. Preserve the distinction between category opportunity and achievable company share.


#### CC-07. Group structure and current business

**Source:** [CC, PDF page 7](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=7); printed 7. **Measured:** 540 x 780 pt; 387 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** Company paragraphs precede a branching subsidiary tree with contribution annotations; short subsidiary explanations follow below.

**Analytical job / reader use.** Legal entities are connected to operating activities and consolidated revenue relevance.

**Instruction for the new report.** Use ownership and contribution labels with a common period. Separate dormant entities and intercompany elimination effects from external revenue.


#### CC-08. History and product range

**Source:** [CC, PDF page 8](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=8); printed 8. **Measured:** 540 x 780 pt; 232 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** A multi-row milestone timeline fills the upper section and a labelled product montage the lower section.

**Analytical job / reader use.** The report shows how the current product portfolio and footprint were assembled.

**Instruction for the new report.** Retain only capability, ownership and capacity milestones. A timeline should not be more visually complicated than the operating history it explains.


#### CC-09. Revenue model and buyers

**Source:** [CC, PDF page 9](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=9); printed 9. **Measured:** 540 x 780 pt; 178 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 9.98 pt.

**Observed layout.** A simple B2B/B2C split diagram sits above explanatory prose and a client-logo collage.

**Analytical job / reader use.** The reader understands whether the company sells ingredients to brands or owns the final consumer relationship.

**Instruction for the new report.** State who pays, who owns the brand, pricing basis and customer concentration. Logos establish relationships only when independently sourced and dated.


#### CC-10. Why customers choose the supplier

**Source:** [CC, PDF page 10](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=10); printed 10. **Measured:** 540 x 780 pt; 386 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** A central bubble cluster lists capabilities with explanations on either side; an export/domestic tree and geographic prose fill the lower section.

**Analytical job / reader use.** The report tries to explain supplier selection through scale, assortment, technology, logistics and certifications.

**Instruction for the new report.** Replace generic strength labels with proof: approval duration, rejection rates, cost position, retention or switching effort. Bubble shapes must not replace evidence.


#### CC-11. New markets and branded operations

**Source:** [CC, PDF page 11](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=11); printed 11. **Measured:** 540 x 780 pt; 439 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** A text-led page switches from geographic expansion to the consumer business, then uses a product/brand/description table.

**Analytical job / reader use.** It distinguishes business development from an established revenue model, although both share one page.

**Instruction for the new report.** Use explicit commercial status for new countries. Separate acquired brands, own launches and contract-manufacturing relationships before estimating revenue.


#### CC-12. Product shelf and distribution reach

**Source:** [CC, PDF page 12](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=12); printed 12. **Measured:** 540 x 780 pt; 155 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 15 pt.

**Observed layout.** A labelled pack-shot montage occupies most of the upper half; two short paragraphs discuss domestic brand presence below.

**Analytical job / reader use.** Physical packs help the reader recognise formats and price positioning. They do not establish sell-through or profitability.

**Instruction for the new report.** Select representative SKUs and add channel, price tier and relevance. Prefer a smaller clear montage to unreadable catalogue packaging labels.


#### CC-13. Three routes to branded growth

**Source:** [CC, PDF page 13](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=13); printed 13. **Measured:** 540 x 780 pt; 314 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 15 pt.

**Observed layout.** A three-branch diagram introduces product launches, acquisitions and distribution, each explained in prose below.

**Analytical job / reader use.** The growth plan is decomposed into distinct actions with different capital and execution needs.

**Instruction for the new report.** Attach an investment, milestone, KPI and risk to each route. Do not count an acquired brand's existing sales again as organic growth.


#### CC-14. Distribution operating map

**Source:** [CC, PDF page 14](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=14); printed 14. **Measured:** 540 x 780 pt; 225 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 15 pt.

**Observed layout.** A tall branching diagram connects channels to detailed white description boxes; a brief margin paragraph sits at the bottom.

**Analytical job / reader use.** The reader sees how the consumer business reaches customers and how channel breadth relates to sales ambition.

**Instruction for the new report.** Include outlet productivity, distribution cost and receivable terms where available. Outlet count without sales per outlet is incomplete economics.


#### CC-15. Manufacturing footprint by site

**Source:** [CC, PDF page 15](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=15); printed 15. **Measured:** 540 x 780 pt; 389 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.02 pt.

**Observed layout.** A location hierarchy with four tall text boxes occupies the upper section; prose explains site advantages below.

**Analytical job / reader use.** The page relates facilities to products and logistics. Dense text inside shapes is harder to scan than a proper comparison table.

**Instruction for the new report.** Use rows for sites and columns for ownership, product, capacity, status, capex and customer region. Keep the process common across sites outside the boxes.


#### CC-16. Capacity through two lenses

**Source:** [CC, PDF page 16](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=16); printed 16. **Measured:** 540 x 780 pt; 320 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** Two stacked-bar charts show capacity by geography and product across identical years; text explains capex and demand below.

**Analytical job / reader use.** The same total is decomposed in two ways, helping readers understand both regional exposure and product-mix change.

**Instruction for the new report.** Reconcile both decompositions to one total. Avoid adding product capacity to geographic capacity; they are alternate views of the same assets.


#### CC-17. People, incentives and holders

**Source:** [CC, PDF page 17](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=17); printed 17. **Measured:** 540 x 780 pt; 206 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 11.04 pt.

**Observed layout.** Three tables cover executives, pay/ownership and major shareholders, using the house red header band.

**Analytical job / reader use.** The page provides a compact alignment and responsibility check after the business-model explanation.

**Instruction for the new report.** Connect relevant leaders to expansion and consumer-brand execution. Distinguish ownership from evidence of operating competence.


#### CC-18. Peer selection and unit economics

**Source:** [CC, PDF page 18](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=18); printed 18. **Measured:** 540 x 780 pt; 202 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 9.98 pt.

**Observed layout.** An explicit comparability caveat leads into a table combining physical scale, unit economics and financial ratios.

**Analytical job / reader use.** The report acknowledges that large consumer groups are imperfect consolidated comparators and chooses a more focused business.

**Instruction for the new report.** Prefer segment or unit economics when clean listed peers are scarce. Explain residual differences in scale, mix and capital intensity before comparing multiples.


#### CC-19. Expansion investment case

**Source:** [CC, PDF page 19](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=19); printed 19. **Measured:** 540 x 780 pt; 355 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 9 pt.

**Observed layout.** A capex/capacity combination chart separates two prose blocks, including a site-specific strategic argument.

**Analytical job / reader use.** The page connects capital spending to productive capacity and geographic access.

**Instruction for the new report.** Evaluate incremental output and returns on the actual project cost. Label expenditure, commissioning and qualification separately and avoid equating capacity with orders.


#### CC-20. From capex to free cash flow

**Source:** [CC, PDF page 20](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=20); printed 20. **Measured:** 540 x 780 pt; 397 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** An opening explanation, a stacked debt chart with leverage annotations and lower margin discussion occupy the main column.

**Analytical job / reader use.** The report distinguishes long-term expansion debt from commodity-sensitive working-capital borrowing, then discusses the anticipated harvesting phase.

**Instruction for the new report.** Model maintenance capex and working capital even when expansion capex slows. A lower capex plan does not guarantee free cash flow if inventory costs rise.


#### CC-21. Consumer growth and commodity effect

**Source:** [CC, PDF page 21](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=21); printed 21. **Measured:** 540 x 780 pt; 373 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 15 pt.

**Observed layout.** A branded-sales bar chart separates the consumer-growth thesis from a raw-material discussion.

**Analytical job / reader use.** Different mechanisms affect revenue, contribution and cash requirements. Commodity movements can change reported sales without equivalent volume growth.

**Instruction for the new report.** Model volume, pass-through, contribution per unit and working capital separately. Do not assume falling input prices always improve reported revenue or margins.


#### CC-22. Raw-material price history

**Source:** [CC, PDF page 22](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=22); printed 22. **Measured:** 540 x 780 pt; 137 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9 pt, 6.96 pt, 9.96 pt.

**Observed layout.** Two wide red line charts stack vertically, with point labels and clear historical timelines; small notes identify incomplete-year data.

**Analytical job / reader use.** The page supplies evidence for commodity volatility and supports the preceding working-capital discussion.

**Instruction for the new report.** Preserve units and time coverage. The two source charts use different commodity quotation bases; standardise only with explicit conversion and do not compare raw levels directly.


#### CC-23. Competitive and cross-border risks

**Source:** [CC, PDF page 23](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=23); printed 23. **Measured:** 540 x 780 pt; 294 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 15 pt.

**Observed layout.** Two text sections explain consumer competition and trade exposure. Bold subheads carry the hierarchy without new decorative devices.

**Analytical job / reader use.** The growth thesis is challenged through customer acquisition difficulty, brand loyalty and regulatory or tariff effects.

**Instruction for the new report.** Quantify advertising intensity, market-entry cost and exposed revenue where possible. Explain the difference between a company's branded and cost-plus contract economics.


#### CC-24. Financial statement appendix

**Source:** [CC, PDF page 24](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=24); printed 24. **Measured:** 540 x 780 pt; 710 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 6.96 pt, 6.98 pt, 8.04 pt.

**Observed layout.** A dense two-column model contains the income statement, balance sheet, cash flow and ratios with tiny labels.

**Analytical job / reader use.** The detailed forecast is available, but it is not comfortable at normal-size screen viewing.

**Instruction for the new report.** Provide a separate model or split statements into legible pages. Maintain a common period order and distinguish estimates throughout.


#### CC-25. Valuation from operating forecast

**Source:** [CC, PDF page 25](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=25); printed 25. **Measured:** 540 x 780 pt; 232 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 11.04 pt, 9.98 pt.

**Observed layout.** A narrow valuation table opens the page; prose then restates the volume and margin assumptions; a signature ends the analytical content.

**Analytical job / reader use.** The table connects the chosen enterprise-value multiple to debt, shares and equity value.

**Instruction for the new report.** Reconcile the forecast EBITDA, net debt and share count to the statements. State which price and margin inputs are assumed rather than guided.


#### CC-26. Publisher catalogue and rating terms

**Source:** [CC, PDF page 26](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=26); printed 26. **Measured:** 540 x 780 pt; 599 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 8.04 pt, 8.06 pt, 11.04 pt.

**Observed layout.** Three cover thumbnails, a rating-definition table and initial disclosure paragraphs occupy the sheet.

**Analytical job / reader use.** The page adds publisher context and rating interpretation, not incremental company analysis.

**Instruction for the new report.** Separate administrative back matter from research depth. Reuse only the layout logic, never another publisher's identity or recommendation definitions without adapting them.


#### CC-27. Relationships and terms

**Source:** [CC, PDF page 27](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=27); printed 27. **Measured:** 540 x 780 pt; 770 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 8.04 pt, 9.96 pt, 8.06 pt.

**Observed layout.** A bordered yes/no disclosure table opens the page with supporting legal sections below.

**Analytical job / reader use.** The tabular structure makes conflicts easier to inspect than paragraphs alone.

**Instruction for the new report.** Use accurate current publisher relationships and authorised disclosure text; do not fabricate regulatory status.


#### CC-28. Final disclaimer and contact block

**Source:** [CC, PDF page 28](https://files.keynotecapitals.com/research/2024/09/Initiating-Coverage-Report-CCL-Products.pdf#page=28); printed 28. **Measured:** 540 x 780 pt; 895 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 8.04 pt, 8.06 pt, 9.96 pt.

**Observed layout.** A dense prose block and compact publisher contacts occupy the top and middle, with open space below.

**Analytical job / reader use.** The document stops once the back matter is complete.

**Instruction for the new report.** Use an independent legal template supplied for the actual publisher. Do not imitate this density in the investment argument.


### EL. Elecon Engineering - Keynote


#### EL-01. Investment overview and facts rail

**Source:** [EL, PDF page 1](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=1); printed 1. **Measured:** 540 x 780 pt; 633 extracted words. **Type evidence:** Calibri-Bold, Calibri; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A broad narrative column is paired with a narrower stock-data rail; the opening business description is bold, with short thesis subheads below. Red linework and a conviction stamp establish hierarchy.

**Analytical job / reader use.** The opening combines segment exposure, growth thesis and valuation. It is a dense summary intended to be revisited after reading the report.

**Instruction for the new report.** Compose it after the operating model and peer work. Check that segment percentages, earnings and target valuation match the detailed pages.


#### EL-02. Teach products through applications

**Source:** [EL, PDF page 2](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=2); printed 2. **Measured:** 540 x 780 pt; 294 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 8.04 pt, 9.98 pt.

**Observed layout.** Plain-language mechanical explanation leads to an industry/application matrix, with small equipment photographs in the right gutter and along the bottom.

**Analytical job / reader use.** The report makes an unfamiliar industrial product understandable through what it does in a customer's process.

**Instruction for the new report.** Define the product function and customer problem first. Attach technical terms to labelled photographs and show how the purchase affects customer throughput or reliability.


#### EL-03. Global and domestic market lenses

**Source:** [EL, PDF page 3](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=3); printed 3. **Measured:** 540 x 780 pt; 209 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 6.96 pt, 9 pt.

**Observed layout.** Four exhibits form a two-by-two structure: market sizes, product-type mix and domestic market organisation. Short paragraphs bridge the two geographies.

**Analytical job / reader use.** The reader can distinguish global category scale from the domestic segment where the company competes.

**Instruction for the new report.** Use a consistent market definition. Separate market growth from company addressable share and avoid treating organised share as total-market share.


#### EL-04. Customer capex intensity

**Source:** [EL, PDF page 4](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=4); printed 4. **Measured:** 540 x 780 pt; 252 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 6.96 pt, 15.96 pt.

**Observed layout.** Text surrounds a small industry table linking customer plant size to spend on the relevant equipment. The right gutter is mostly blank.

**Analytical job / reader use.** The page supplies a bottom-up link from downstream capex to supplier demand rather than relying only on a broad industrial-growth claim.

**Instruction for the new report.** Build customer capex times equipment intensity times attainable share, with qualification and timing constraints. Show ranges when intensity varies substantially.


#### EL-05. End-market demand and company exposure

**Source:** [EL, PDF page 5](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=5); printed 5. **Measured:** 540 x 780 pt; 375 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** Four numbered downstream-industry discussions occupy the left main column; a compact right-side exposure table shows their importance to the company.

**Analytical job / reader use.** Market growth is linked to actual revenue exposure, making relevance easier to judge.

**Instruction for the new report.** Weight end-market scenarios by company exposure. Explain order-to-revenue lags; a growing customer industry's total capex is not automatically supplier revenue.


#### EL-06. Second-segment education

**Source:** [EL, PDF page 6](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=6); printed 6. **Measured:** 540 x 780 pt; 256 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** A brief definition, a branching product diagram and a market-size bar chart share the page with relevant equipment photos in the gutter.

**Analytical job / reader use.** The report gives the smaller business its own vocabulary and demand structure before discussing group results.

**Instruction for the new report.** Treat distinct segments as separate operating models. Use common visual grammar while allowing different drivers and economics.


#### EL-07. Company identity and milestones

**Source:** [EL, PDF page 7](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=7); printed 7. **Measured:** 540 x 780 pt; 380 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** Company and network paragraphs lead into a horizontal multi-event timeline across the lower third.

**Analytical job / reader use.** The history explains how the present product range and international position emerged.

**Instruction for the new report.** Choose milestones that alter capabilities, ownership, geography or cash generation. Avoid crowded timeline labels for routine events.


#### EL-08. Segments, orders and visibility

**Source:** [EL, PDF page 8](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=8); printed 8. **Measured:** 540 x 780 pt; 135 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9 pt, 9.96 pt, 6.96 pt.

**Observed layout.** A segment hierarchy and stacked revenue bars occupy the top; order-intake mix and an order-to-revenue line appear below.

**Analytical job / reader use.** The report differentiates revenue already earned from orders received and the visibility those orders provide.

**Instruction for the new report.** Publish opening backlog plus intake less execution and cancellations. Keep short-cycle orders separate from long-duration backlog so coverage is not overstated.


#### EL-09. Core segment economics

**Source:** [EL, PDF page 9](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=9); printed 9. **Measured:** 540 x 780 pt; 314 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** Text introduces the gear business; a small right-side market-share chart complements a larger revenue-growth chart beneath.

**Analytical job / reader use.** Leadership and historical growth are presented together but answer different questions.

**Instruction for the new report.** State the share denominator and year. Explain whether growth came from market demand, price, share gain or acquisition rather than inferring a moat from growth alone.


#### EL-10. Standard versus custom economics

**Source:** [EL, PDF page 10](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=10); printed 10. **Measured:** 540 x 780 pt; 356 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** A parallel-column comparison lists product model, delivery time, margins and design work, followed by operating discussion.

**Analytical job / reader use.** The table explains why two products in one segment have different pricing, execution and capital characteristics.

**Instruction for the new report.** For another industry compare standardised and bespoke work on the same dimensions. Quantify the mix and margin effect rather than merely calling custom work premium.


#### EL-11. Product taxonomy and use cases

**Source:** [EL, PDF page 11](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=11); printed 11. **Measured:** 540 x 780 pt; 287 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9 pt, 9.96 pt, 9.02 pt.

**Observed layout.** A full-height four-column table pairs product names, isolated images, descriptions and end industries.

**Analytical job / reader use.** The page converts a catalogue into an educational reference and reduces dependence on specialist vocabulary.

**Instruction for the new report.** Use one clean image per row and short functional descriptions. Add revenue relevance where disclosed; leave it unknown where not available.


#### EL-12. Applications and incoming orders

**Source:** [EL, PDF page 12](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=12); printed 12. **Measured:** 540 x 780 pt; 154 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Six application tiles occupy the upper section and a small order-intake chart the lower section, with a side note on execution time.

**Analytical job / reader use.** The reader sees what demand supports the order flow, while the lead-time note constrains revenue timing.

**Instruction for the new report.** Use product-application tiles selectively. Distinguish an industry the company can serve from one supplying material current orders.


#### EL-13. Backlog composition and cycle commentary

**Source:** [EL, PDF page 13](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=13); printed 13. **Measured:** 540 x 780 pt; 384 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 9 pt.

**Observed layout.** A large ring chart shows end-market backlog mix between prose blocks explaining downstream conditions.

**Analytical job / reader use.** The report tests the demand story against actual order exposure and discusses weaker as well as stronger sectors.

**Instruction for the new report.** Date backlog, show cancellation rights and identify execution horizons. Backlog composition is not the same as current revenue mix.


#### EL-14. Distribution and manufacturing footprint

**Source:** [EL, PDF page 14](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=14); printed 14. **Measured:** 540 x 780 pt; 290 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 11.04 pt, 6.96 pt.

**Observed layout.** Several text sections describe diversification, distributors and production; a strip of plant photographs closes the main body.

**Analytical job / reader use.** The page explains how the company reaches markets and fulfils orders, although some diversification statements are broad.

**Instruction for the new report.** Connect network reach to delivery time, service revenue or customer retention. Plant photographs should accompany capacity and productivity evidence.


#### EL-15. Technical capabilities

**Source:** [EL, PDF page 15](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=15); printed 15. **Measured:** 540 x 780 pt; 300 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** Numbered capability sections and small innovation bullets lead to a three-item year-labelled illustration at the bottom.

**Analytical job / reader use.** The report attempts to connect facilities and engineering capabilities to product performance.

**Instruction for the new report.** Use customer-relevant measures such as precision, rejection rate, reliability or lead time. Automation and research headcount are inputs, not proof of economic advantage.


#### EL-16. Segment profitability and asset use

**Source:** [EL, PDF page 16](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=16); printed 16. **Measured:** 540 x 780 pt; 289 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** Explanatory paragraphs precede a combined EBIT/margin chart; circular utilisation and turnover graphics form the lower band.

**Analytical job / reader use.** Margin history is placed beside available capacity and asset efficiency, creating a path from mix to incremental returns.

**Instruction for the new report.** Separate EBIT from EBITDA and link capex to future depreciation. Replace decorative circles with a small data table if multiple denominators are involved.


#### EL-17. Engineering workflow and investment

**Source:** [EL, PDF page 17](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=17); printed 17. **Measured:** 540 x 780 pt; 368 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** A bubble-based engineering-process diagram occupies the top; a long capex explanation follows below.

**Analytical job / reader use.** The page combines capability development with the purpose, timing and funding of asset replacement.

**Instruction for the new report.** Identify whether capex expands capacity, replaces old assets or improves product capability. Different purposes need different return and utilisation assumptions.


#### EL-18. OEM programme pipeline

**Source:** [EL, PDF page 18](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=18); printed 18. **Measured:** 540 x 780 pt; 185 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 11.04 pt.

**Observed layout.** An arrow timeline of signed relationships leads to a boxed per-customer revenue expectation and a set of target-industry icons.

**Analytical job / reader use.** The report distinguishes a relationship pipeline from immediate commercial sales, creating a potential long-duration driver.

**Instruction for the new report.** Track signed, prototype, validation, nomination and commercial stages. Never multiply all signed programmes by mature revenue without ramp and probability assumptions.


#### EL-19. Programme conversion and future mix

**Source:** [EL, PDF page 19](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=19); printed 19. **Measured:** 540 x 780 pt; 318 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 15.96 pt.

**Observed layout.** Text explains progress from prototype to production; a three-doughnut sequence shows current and targeted OEM contribution.

**Analytical job / reader use.** The page tries to show the conversion of programme count into revenue contribution.

**Instruction for the new report.** Reconcile programme-level sales to segment revenue. This report's adjacent OEM pages contain inconsistent revenue magnitudes; copying polished prose would propagate the error.


#### EL-20. Contract structure and export strategy

**Source:** [EL, PDF page 20](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=20); printed 20. **Measured:** 540 x 780 pt; 285 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A directional diagram summarises OEM commercial features; prose and a stacked domestic/overseas chart occupy the lower section.

**Analytical job / reader use.** The report introduces the volume-versus-margin trade-off in OEM supplies and their role in international expansion.

**Instruction for the new report.** Model OEM, replacement and aftermarket economics separately. A higher export share can coexist with a lower-margin export mix.


#### EL-21. Geographic and customer concentration

**Source:** [EL, PDF page 21](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=21); printed 21. **Measured:** 540 x 780 pt; 365 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** Paragraphs lead into a geographic ring chart, followed by a discussion of customer diversification.

**Analytical job / reader use.** The reader can assess where revenue comes from and whether a few customers dominate it.

**Instruction for the new report.** Separate customers, countries and channels as distinct concentration dimensions. Broad diversification claims should not replace an actual top-customer table.


#### EL-22. Customer and network evidence

**Source:** [EL, PDF page 22](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=22); printed 22. **Measured:** 540 x 780 pt; 14 extracted words. **Type evidence:** Calibri-Bold, Calibri-Italic; most-used sizes 6.96 pt, 15.96 pt, 11.04 pt.

**Observed layout.** A client-logo grid occupies the upper half; a labelled global distribution map fills the lower half.

**Analytical job / reader use.** The page helps readers recognise customer types and service locations. It supplies context rather than quantified demand.

**Instruction for the new report.** Date relationships and classify facilities as owned, assembly, repair or sales. Do not imply a sales office is manufacturing capacity.


#### EL-23. Smaller-segment products and legacy model

**Source:** [EL, PDF page 23](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=23); printed 23. **Measured:** 540 x 780 pt; 274 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** A product table pairs photographs, descriptions and applications; the lower text introduces the former project-oriented business model.

**Analytical job / reader use.** The report prepares the reader to understand why the segment once had different risk and capital characteristics.

**Instruction for the new report.** Teach the old economic model before explaining the turnaround. Separate equipment sales, projects and maintenance revenue.


#### EL-24. Restructuring actions and revenue

**Source:** [EL, PDF page 24](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=24); printed 24. **Measured:** 540 x 780 pt; 177 extracted words. **Type evidence:** Calibri, Calibri-Italic; most-used sizes 9.96 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Risk statements appear in horizontal bands, followed by three numbered restructuring steps and a historical revenue chart.

**Analytical job / reader use.** The turnaround is decomposed into changes in bidding, operating model and legacy contract resolution.

**Instruction for the new report.** For each action show date, cost, completion evidence and financial consequence. Use before/after metrics rather than a generic transformation claim.


#### EL-25. Turnaround profitability and product strategy

**Source:** [EL, PDF page 25](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=25); printed 25. **Measured:** 540 x 780 pt; 297 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 9 pt.

**Observed layout.** A combined EBIT/margin chart spans the upper middle; explanatory paragraphs and a short product list follow.

**Analytical job / reader use.** The page shows that a recovery in revenue is distinct from a recovery in unit economics and losses.

**Instruction for the new report.** Separate accounting write-offs from operating cash costs and recurring margins. Rebuild underlying profitability rather than assuming all prior losses were non-recurring.


#### EL-26. Orders and aftermarket cash engine

**Source:** [EL, PDF page 26](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=26); printed 26. **Measured:** 540 x 780 pt; 268 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** Order-intake bars and a backlog ring chart share the top; text, two channel-share boxes and client logos fill the lower section.

**Analytical job / reader use.** The report contrasts new orders with recurring service activity and shows why business mix matters.

**Instruction for the new report.** Quantify installed base, service attachment, repeat frequency and margins. A large installed base only creates an opportunity until repeat revenue is evidenced.


#### EL-27. Management and financial alignment

**Source:** [EL, PDF page 27](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=27); printed 27. **Measured:** 540 x 780 pt; 193 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 11.04 pt, 9.98 pt.

**Observed layout.** Three stacked tables cover managers, compensation/ownership and large shareholders.

**Analytical job / reader use.** Execution ownership and incentive alignment are made inspectable.

**Instruction for the new report.** Connect executives to specific segment responsibilities and past delivery. Separate promoter remuneration from all management compensation.


#### EL-28. Comparable financial histories

**Source:** [EL, PDF page 28](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=28); printed 28. **Measured:** 540 x 780 pt; 336 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9 pt, 9.98 pt.

**Observed layout.** Two multi-year financial tables compare the subject with a focused listed peer; prose interprets margin and growth differences.

**Analytical job / reader use.** Longitudinal comparison adds depth beyond a single-year valuation table. The report acknowledges the segment mismatch.

**Instruction for the new report.** Compare like segments or show a bridge from group to segment. Use consistent accounting periods and definitions of cash-conversion metrics.


#### EL-29. Core opportunity synthesis

**Source:** [EL, PDF page 29](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=29); printed 29. **Measured:** 540 x 780 pt; 314 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** A text-led argument reassembles market position, capabilities and exports above a historical segment revenue chart.

**Analytical job / reader use.** Earlier descriptive sections are condensed into the reasons for expecting continued performance.

**Instruction for the new report.** Avoid reprinting the whole operating history. Specify which future change is not already represented by the historical chart.


#### EL-30. Smaller-segment opportunity synthesis

**Source:** [EL, PDF page 30](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=30); printed 30. **Measured:** 540 x 780 pt; 261 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 6.96 pt.

**Observed layout.** Paragraphs above revenue bars and an EBIT-margin line summarise the turnaround and prospective contribution.

**Analytical job / reader use.** The page connects a changed operating model to observed economics and a larger role in the group.

**Instruction for the new report.** Show revenue and profit contribution separately, and explain the capital needed for the next growth phase.


#### EL-31. Diversification and cycle risk

**Source:** [EL, PDF page 31](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=31); printed 31. **Measured:** 540 x 780 pt; 256 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 11.04 pt, 9.98 pt.

**Observed layout.** A positive diversification discussion is followed by a clear risk subsection on downstream cyclicality.

**Analytical job / reader use.** The same exposure can diversify customers while retaining a shared industrial capex cycle.

**Instruction for the new report.** Test correlations across end markets instead of counting sectors. State what happens to order intake and utilisation in a broad slowdown.


#### EL-32. Complete forecast reference

**Source:** [EL, PDF page 32](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=32); printed 32. **Measured:** 540 x 780 pt; 718 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 6.96 pt, 6.98 pt, 15.96 pt.

**Observed layout.** Two tightly packed columns contain all major statements and ratios with red header bands.

**Analytical job / reader use.** Readers can audit the point estimates, but the density is difficult on a normal screen.

**Instruction for the new report.** Split tables when necessary and provide an editable model. Keep actual-versus-forecast notation and fiscal years stable.


#### EL-33. Valuation and assumptions

**Source:** [EL, PDF page 33](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=33); printed 33. **Measured:** 540 x 780 pt; 233 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 9.96 pt, 9.98 pt, 9.05 pt.

**Observed layout.** A compact earnings-based valuation table precedes synthesis paragraphs and a signature block.

**Analytical job / reader use.** The report connects forecast profit, share count and a chosen earnings multiple to the conclusion.

**Instruction for the new report.** State why the chosen multiple is appropriate, then test lower growth or multiple compression. Do not let a table conceal a weakly justified multiple.


#### EL-34. Publisher catalogue and methodology

**Source:** [EL, PDF page 34](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=34); printed 34. **Measured:** 540 x 780 pt; 520 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 8.04 pt, 8.06 pt, 11.04 pt.

**Observed layout.** Report thumbnails, rating definitions and initial disclosures fill the page.

**Analytical job / reader use.** This is administrative and promotional back matter.

**Instruction for the new report.** Keep it out of the analytical page count and adapt publisher details truthfully.


#### EL-35. Conflicts and terms

**Source:** [EL, PDF page 35](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=35); printed 35. **Measured:** 540 x 780 pt; 866 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 8.04 pt, 8.06 pt, 9.96 pt.

**Observed layout.** Small prose and a bordered disclosure matrix fill most of the page.

**Analytical job / reader use.** Relationships are disclosed in a consistent lookup format.

**Instruction for the new report.** Use the actual research publisher's relationships and authorised legal text.


#### EL-36. Final legal notice

**Source:** [EL, PDF page 36](https://files.keynotecapitals.com/research/2025/05/Initiating-Coverage-Report-Elecon-Engineering-Company-Ltd.pdf#page=36); printed 36. **Measured:** 540 x 780 pt; 893 extracted words. **Type evidence:** Calibri, Calibri-Bold; most-used sizes 8.04 pt, 8.06 pt, 9.96 pt.

**Observed layout.** Dense small text and contact information end the report within the recurring frame.

**Analytical job / reader use.** The closing page explains document use and limitations.

**Instruction for the new report.** Maintain this as back matter; never transplant the broker's credentials into an independent report.


### SU. Suprajit Engineering - Equirus


#### SU-01. Product-led cover

**Source:** [SU, PDF page 1](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=1); printed unnumbered cover. **Measured:** 595.56 x 841.68 pt; 24 extracted words. **Type evidence:** FuturaBT-BoldCondensed, FuturaBT-Light; most-used sizes 18 pt, 9.96 pt, 35.04 pt.

**Observed layout.** A blue photographic collage combines cables, lamps and instrument clusters, with a large white company title and a lower white publisher strip.

**Analytical job / reader use.** The range of physical products introduces a diversified supplier before its financial story.

**Instruction for the new report.** Use authentic product families, not generic factory stock images. Let the cover preview the business breadth without making unsupported leadership claims.


#### SU-02. Executive argument and reference rail

**Source:** [SU, PDF page 2](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=2); printed 1. **Measured:** 595.32 x 841.92 pt; 647 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 9.96 pt, 8.04 pt, 20.04 pt.

**Observed layout.** A blue thesis banner spans the main column; a grey summary box and prose sit below; the right rail stacks rating, stock facts, owners, chart and analyst details.

**Analytical job / reader use.** The page compresses strategic change, financial forecasts and valuation, while allowing rapid lookup of factual context.

**Instruction for the new report.** Write the argument after modelling and keep the rail modular. Do not force prose into the rail or let reference facts interrupt the investment narrative.


#### SU-03. Map the businesses before analysing them

**Source:** [SU, PDF page 3](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=3); printed 2. **Measured:** 595.32 x 841.92 pt; 25 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 8.04 pt, 9 pt.

**Observed layout.** A full-width branching diagram groups divisions, routes to market and brief economics in coloured horizontal blocks. Much of the content is embedded as an image.

**Analytical job / reader use.** The reader can see how divisions, OEM/aftermarket channels and geographies relate. This prevents later segment references from becoming a vocabulary burden.

**Instruction for the new report.** Draw an editable business tree with mutually exclusive segments and reconciled shares. Retain a text alternative; image-only business maps are inaccessible to extraction and search.


#### SU-04. Portfolio transformation in six charts

**Source:** [SU, PDF page 4](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=4); printed 3. **Measured:** 595.32 x 841.92 pt; 416 extracted words. **Type evidence:** Calibri, FuturaBT-Light; most-used sizes 8.04 pt, 6.48 pt, 9 pt.

**Observed layout.** A two-column, three-row exhibit grid covers exposure shifts, revenue/profit contributions and pre/post-acquisition mix. Orange, dark blue and grey identify segments.

**Analytical job / reader use.** This page shows the portfolio change that underlies the thesis. Revenue and EBITDA contribution are deliberately separate views.

**Instruction for the new report.** Preserve segment colours across every exhibit. If comparing before and after a deal, label pro forma assumptions and avoid implying both periods are directly reported.


#### SU-05. Core division and demand recovery

**Source:** [SU, PDF page 5](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=5); printed 4. **Measured:** 595.32 x 841.92 pt; 284 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** The main reading column begins far to the right, leaving a wide left gutter for blue italic takeaways. A segment-mix pie and demand chart sit below the explanation.

**Analytical job / reader use.** The report establishes the incumbent business and the demand assumptions supporting it. The sidebar repeats the takeaway in compressed form.

**Instruction for the new report.** Use the main column for evidence and the gutter for interpretation. Keep market-share facts distinct from forecasts for the downstream industry.


#### SU-06. Exports and aftermarket growth

**Source:** [SU, PDF page 6](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=6); printed 5. **Measured:** 595.32 x 841.92 pt; 502 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** Several paragraphs surround one export-sales bar chart; left-gutter notes identify the two growth mechanisms.

**Analytical job / reader use.** The report separates growth through international OEM business from domestic replacement demand.

**Instruction for the new report.** Model geography and channel separately, with customer wins, distribution reach and repeat demand evidence. A low global share alone does not prove a large achievable opportunity.


#### SU-07. Technology substitution and content per vehicle

**Source:** [SU, PDF page 7](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=7); printed 6. **Measured:** 595.32 x 841.92 pt; 465 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** Text discusses different vehicle applications above a small component-presence matrix. Side notes explain what changes and what remains.

**Analytical job / reader use.** The reader can test whether electrification removes or preserves product demand. Product content is a more precise variable than vehicle-market growth alone.

**Instruction for the new report.** Construct a component-by-technology table and attach value per vehicle where available. Avoid equating more components with more revenue without pricing and penetration assumptions.


#### SU-08. Margin resilience and competitor cost base

**Source:** [SU, PDF page 8](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=8); printed 7. **Measured:** 595.32 x 841.92 pt; 295 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 12 pt.

**Observed layout.** A historical margin line is followed by explanatory bullets and a competitor financial table; the broad left gutter contains concise takeaways.

**Analytical job / reader use.** Stable margins are connected to pass-through and cost structure rather than left as an unexplained historical observation.

**Instruction for the new report.** Show pass-through mechanics, lag and uncovered inputs. Compare labour, scale and geography only where accounting boundaries and periods are comparable.


#### SU-09. Relative margins and capacity utilisation

**Source:** [SU, PDF page 9](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=9); printed 8. **Measured:** 595.32 x 841.92 pt; 279 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 9 pt, 8.04 pt, 12 pt.

**Observed layout.** A second competitor table, a multi-company margin chart and a combined production/capacity/utilisation chart stack down the main column.

**Analytical job / reader use.** The cost-position argument is tested against peers and physical asset use.

**Instruction for the new report.** Separate nameplate capacity, actual output and utilisation. Investigate whether peer losses reflect structural cost disadvantages or temporary company-specific problems.


#### SU-10. Location advantage and division forecast

**Source:** [SU, PDF page 10](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=10); printed 9. **Measured:** 595.32 x 841.92 pt; 226 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 12 pt.

**Observed layout.** A plant-location comparison table precedes short forecasting prose and a combined revenue/EBITDA/margin chart.

**Analytical job / reader use.** The page closes the core-division section by translating operating arguments into a forecast.

**Instruction for the new report.** End each segment chapter with its driver assumptions and resulting financials. Keep chart legends consistent when mixing rupees and percentages on separate axes.


#### SU-11. Legacy technology segment

**Source:** [SU, PDF page 11](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=11); printed 10. **Measured:** 595.32 x 841.92 pt; 385 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** A new segment heading, short threat statement, revenue-mix pie and channel discussion share the main column.

**Analytical job / reader use.** The report acknowledges technology substitution while examining replacement demand. This is a more balanced starting point than treating market leadership as permanent protection.

**Instruction for the new report.** Separate new-equipment demand from installed-base replacement demand. Estimate decline and cash-harvest scenarios instead of assuming consolidation offsets obsolescence.


#### SU-12. Pricing pressure and restructuring

**Source:** [SU, PDF page 12](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=12); printed 11. **Measured:** 595.32 x 841.92 pt; 373 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 12 pt.

**Observed layout.** Text frames overseas competition, a declining subsidiary-revenue bar chart supplies evidence, and further prose discusses restructuring.

**Analytical job / reader use.** Weak operating evidence is shown directly, making the recovery thesis testable.

**Instruction for the new report.** State what changed in price, cost or structure and when. Keep actual weak history visible rather than replacing it with only forecast improvement.


#### SU-13. Recovery levers and forecast

**Source:** [SU, PDF page 13](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=13); printed 12. **Measured:** 595.32 x 841.92 pt; 479 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 12 pt.

**Observed layout.** Two text blocks explain export strategy and restructuring before a combined segment forecast chart. Gutter notes summarise each mechanism.

**Analytical job / reader use.** The report moves from a challenged history to proposed repair actions and a financial endpoint.

**Instruction for the new report.** Build separate price, volume and cost-reduction assumptions. Do not attribute an entire forecast recovery to restructuring without a quantified bridge.


#### SU-14. Non-auto segment economics

**Source:** [SU, PDF page 14](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=14); printed 13. **Measured:** 595.32 x 841.92 pt; 450 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 12 pt.

**Observed layout.** A mix pie separates explanatory paragraphs; the left gutter summarises overseas exposure, sourcing strategy and restructuring.

**Analytical job / reader use.** The segment is treated as a distinct customer and cost ecosystem, rather than assumed to behave like automotive supply.

**Instruction for the new report.** Identify demand cycles and customer concentration specific to this segment. Segment diversification may still leave common geographic or consumer-spending exposure.


#### SU-15. Non-auto forecast endpoint

**Source:** [SU, PDF page 15](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=15); printed 14. **Measured:** 595.32 x 841.92 pt; 190 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** A brief forecast discussion leads to a single combined revenue/profit/margin chart. Large white space remains below.

**Analytical job / reader use.** The chapter closes with an explicit forecast rather than an open-ended strengths list.

**Instruction for the new report.** Keep the assumption-to-output connection visible. A sparse closing page can be merged if doing so does not obscure segment boundaries.


#### SU-16. Acquired business introduction

**Source:** [SU, PDF page 16](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=16); printed 15. **Measured:** 595.32 x 841.92 pt; 307 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A short deal description leads into client logos, product images and geographic/application pies in a two-by-two arrangement.

**Analytical job / reader use.** The acquired asset is introduced through what was bought, who it serves and where it operates.

**Instruction for the new report.** State transaction perimeter, consideration, debt/cash treatment and closing status. Logos and product breadth do not establish integration success.


#### SU-17. Strategic fit and combined footprint

**Source:** [SU, PDF page 17](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=17); printed 16. **Measured:** 595.32 x 841.92 pt; 495 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** Text explains cross-selling and geographic complementarity; a competitor table and coloured capability matrix follow.

**Analytical job / reader use.** The acquisition thesis is framed around capabilities that the combined business can offer beyond its standalone parts.

**Instruction for the new report.** Identify specific customer/product overlaps and integration dependencies. Put revenue synergies in a separate assumption set from cost savings.


#### SU-18. Capital-allocation track record

**Source:** [SU, PDF page 18](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=18); printed 17. **Measured:** 595.32 x 841.92 pt; 296 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A text introduction leads into two stacked-share histories with acquisition events annotated above the timelines.

**Analytical job / reader use.** The reader can see how portfolio and geographic diversification followed prior transactions.

**Instruction for the new report.** Treat acquisition-driven mix shifts separately from organic performance. Use constant-perimeter measures when evaluating execution quality.


#### SU-19. Deal-by-deal audit trail

**Source:** [SU, PDF page 19](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=19); printed 18. **Measured:** 595.32 x 841.92 pt; 782 extracted words. **Type evidence:** FuturaBT-Light, SymbolMT; most-used sizes 8.04 pt, 9 pt, 5.04 pt.

**Observed layout.** A dense full-width table lists acquisitions, consideration and detailed observations with alternating grey bands.

**Analytical job / reader use.** A broad claim of prudent acquisition strategy is supported with transaction-level detail.

**Instruction for the new report.** Use columns for date, perimeter, price, funding, promised benefits and realised results. A deal list becomes analysis only when outcomes are compared with promises.


#### SU-20. Portfolio change versus balance-sheet cost

**Source:** [SU, PDF page 20](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=20); printed 19. **Measured:** 595.32 x 841.92 pt; 256 extracted words. **Type evidence:** Calibri, FuturaBT-Light; most-used sizes 6.48 pt, 9 pt, 8.04 pt.

**Observed layout.** Two mix pies share the top, with margin/return and leverage charts below. Short text bridges the sections.

**Analytical job / reader use.** The report tests whether diversification was achieved at the expense of profitability or financial risk.

**Instruction for the new report.** Evaluate returns after goodwill and integration costs as well as before them. Show cumulative acquisition cash outflow against generated cash.


#### SU-21. Long-run revenue bridge

**Source:** [SU, PDF page 21](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=21); printed 20. **Measured:** 595.32 x 841.92 pt; 378 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** An explanation of organic and acquired growth sits above a long historical revenue chart with period annotations.

**Analytical job / reader use.** The growth record is decomposed by phase rather than presented as one undifferentiated CAGR.

**Instruction for the new report.** Build a constant-perimeter or acquisition bridge where possible. Mark forecast years clearly within a long historical series.


#### SU-22. Per-share growth, funding and asset use

**Source:** [SU, PDF page 22](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=22); printed 21. **Measured:** 595.32 x 841.92 pt; 136 extracted words. **Type evidence:** Calibri, FuturaBT-Light; most-used sizes 8.04 pt, 9 pt, 6.48 pt.

**Observed layout.** Three stacked charts show earnings per share, cash versus investment and asset turns. Titles carry the interpretation.

**Analytical job / reader use.** The report tests whether group growth also benefited owners and how it was financed.

**Instruction for the new report.** Include dilution, acquisition issuance and cumulative cash conversion. Growth in absolute profit can overstate shareholder benefit if shares or capital employed expand faster.


#### SU-23. Margin, returns and cash forecasts

**Source:** [SU, PDF page 23](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=23); printed 22. **Measured:** 595.32 x 841.92 pt; 133 extracted words. **Type evidence:** Calibri, FuturaBT-Light; most-used sizes 8.04 pt, 9 pt, 8.06 pt.

**Observed layout.** Three charts connect profitability, return ratios and CFO versus capex. The layout keeps one dominant column and a large annotation gutter.

**Analytical job / reader use.** The earnings story is tested against capital efficiency and cash requirements.

**Instruction for the new report.** Use a consistent definition of pre-tax and post-tax returns. CFO and capex must tie to the cash-flow model, not independent chart inputs.


#### SU-24. Engineering capability and future products

**Source:** [SU, PDF page 24](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=24); printed 23. **Measured:** 595.32 x 841.92 pt; 385 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 12 pt.

**Observed layout.** Narrative about development capability is followed by a technology-centre table and a product-platform image.

**Analytical job / reader use.** The report explains the process by which adjacent products could reach production.

**Instruction for the new report.** Evidence development through prototypes, validation, nominations and serial sales. Research resources are inputs and should not be valued as proven future revenue.


#### SU-25. Existing to adjacent product map

**Source:** [SU, PDF page 25](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=25); printed 24. **Measured:** 595.32 x 841.92 pt; 44 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt.

**Observed layout.** An image-led diagram maps existing product families to adjacent technologies; larger product images and use-case labels sit below.

**Analytical job / reader use.** The reader sees adjacency in capability rather than receiving a disconnected list of optional products.

**Instruction for the new report.** Mark each product's commercial status and relevance to existing customer relationships. Keep prototypes out of reported revenue mix.


#### SU-26. Application-led product expansion

**Source:** [SU, PDF page 26](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=26); printed 25. **Measured:** 595.32 x 841.92 pt; 58 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt.

**Observed layout.** Three vertically arranged exhibit groups show braking, parking and seeding components with coloured application tags.

**Analytical job / reader use.** Technical options become concrete through the customer task they perform.

**Instruction for the new report.** State addressable platform, approval stage, timing and unit value when available. Avoid multiplying all possible applications into a base-case TAM.


#### SU-27. Segment assumptions and sensitivity

**Source:** [SU, PDF page 27](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=27); printed 26. **Measured:** 595.32 x 841.92 pt; 178 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 8.04 pt, 9 pt, 14.04 pt.

**Observed layout.** A segment-by-year assumptions table occupies the top; a smaller margin-sensitivity table follows below.

**Analytical job / reader use.** The report exposes the inputs used to assemble consolidated forecasts and the sensitivity to segment performance.

**Instruction for the new report.** This is a strong reproducible analytical page: publish volumes or revenues, growth and margin by segment, then show consolidated effects of changing one input.


#### SU-28. Threats and governance

**Source:** [SU, PDF page 28](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=28); printed 27. **Measured:** 595.32 x 841.92 pt; 401 extracted words. **Type evidence:** FuturaBT-Light, SymbolMT; most-used sizes 9 pt, 8.04 pt, 14.04 pt.

**Observed layout.** Two text sections cover technology/cycle risks and governance-related disclosures, using bullets and indentation.

**Analytical job / reader use.** The report gives downside mechanisms and governance context their own space before valuation.

**Instruction for the new report.** Separate risk evidence, management response and analyst judgement. Add an explicit thesis-break condition for each material threat.


#### SU-29. Valuation argument begins

**Source:** [SU, PDF page 29](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=29); printed 28. **Measured:** 595.32 x 841.92 pt; 286 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 9 pt, 6.48 pt, 8.04 pt.

**Observed layout.** Two thesis bullets alternate with a revenue-mix pie and an industry-relative growth line chart. Gutter notes carry the compressed rationale.

**Analytical job / reader use.** The report uses business attributes and historical evidence to argue for a premium valuation.

**Instruction for the new report.** Require an incremental reason for the chosen multiple. Historical outperformance supports a question about durability; it does not mechanically justify any premium.


#### SU-30. Valuation endpoint and history

**Source:** [SU, PDF page 30](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=30); printed 29. **Measured:** 595.32 x 841.92 pt; 232 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** A short concluding valuation paragraph is followed by two long-run forward-multiple line charts with average reference lines.

**Analytical job / reader use.** The reader sees the proposed multiple in historical context.

**Instruction for the new report.** Match the earnings horizon to the target date and state the valuation method. Historical averages are context, not a floor or intrinsic-value calculation.


#### SU-31. Peer valuation reference

**Source:** [SU, PDF page 31](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=31); printed 30. **Measured:** 595.32 x 841.92 pt; 253 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 7.56 pt, 8.04 pt, 6 pt.

**Observed layout.** A broad comparative table occupies the top; three small historical multiple charts line the bottom, leaving a large gap.

**Analytical job / reader use.** The page provides a peer and history lookup but has inefficient space use and very small chart labels.

**Instruction for the new report.** Consolidate or enlarge the useful exhibits. Compare similar business models, growth and capital economics rather than only price multiples.


#### SU-32. Company background after valuation

**Source:** [SU, PDF page 32](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=32); printed 31. **Measured:** 595.32 x 841.92 pt; 407 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 14.04 pt.

**Observed layout.** Overview prose leads into a multi-column business-evolution graphic, with more division descriptions below.

**Analytical job / reader use.** The report keeps detailed company history after the main investment argument for reference readers.

**Instruction for the new report.** Use cross-references to prevent repeating earlier business education. Retain only history that explains the present economic model.


#### SU-33. Division summary and current mix

**Source:** [SU, PDF page 33](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=33); printed 32. **Measured:** 595.32 x 841.92 pt; 72 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 8.04 pt, 9 pt, 8.06 pt.

**Observed layout.** A three-column division comparison sits above a stacked revenue chart, with much open lower space.

**Analytical job / reader use.** The reader receives a compact reference to the main businesses and their contributions.

**Instruction for the new report.** Make the table self-contained with common metrics. Reconcile segment labels with the model and avoid introducing a new taxonomy here.


#### SU-34. Customers and application diagrams

**Source:** [SU, PDF page 34](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=34); printed 33. **Measured:** 595.32 x 841.92 pt; 166 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 8.04 pt, 9 pt.

**Observed layout.** A customer matrix and logo grid precede two labelled vehicle diagrams showing where components fit.

**Analytical job / reader use.** The page combines relationship evidence with physical product education.

**Instruction for the new report.** Use authenticated customer relationships and label the exposure year. The diagrams should explain component function, not imply all illustrated applications are supplied by the company.


#### SU-35. Diversification through time

**Source:** [SU, PDF page 35](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=35); printed 34. **Measured:** 595.32 x 841.92 pt; 305 extracted words. **Type evidence:** FuturaBT-Light, Calibri; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** A brief explanation precedes stacked bars for end-market mix and geographic mix.

**Analytical job / reader use.** The report demonstrates changes in exposure rather than asserting diversification abstractly.

**Instruction for the new report.** Distinguish portfolio change from a reduction in underlying risk. Several end markets can still share the same cycle or major customers.


#### SU-36. Manufacturing and service geography

**Source:** [SU, PDF page 36](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=36); printed 35. **Measured:** 595.32 x 841.92 pt; 227 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** Short prose sits above a large multi-region map and a legend distinguishing different facilities.

**Analytical job / reader use.** The reader can locate manufacturing, engineering and distribution relative to customers.

**Instruction for the new report.** Keep facility types distinct and add operational status and capacity to the evidence ledger. Geographic proximity matters only through a stated service, cost or lead-time mechanism.


#### SU-37. Legal group and milestones

**Source:** [SU, PDF page 37](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=37); printed 36. **Measured:** 595.32 x 841.92 pt; 235 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 8.04 pt, 9 pt.

**Observed layout.** A full-width organisational chart is followed by a dated event table. Colour and dashed boundaries distinguish business groupings.

**Analytical job / reader use.** The page separates corporate ownership from product-market segmentation and supplies a reference history.

**Instruction for the new report.** Show ownership percentages, consolidation and entity functions explicitly. Do not use a corporate chart as a substitute for segment financial disclosure.


#### SU-38. Management biographies

**Source:** [SU, PDF page 38](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=38); printed 37. **Measured:** 595.32 x 841.92 pt; 761 extracted words. **Type evidence:** FuturaBT-Light; most-used sizes 9 pt, 8.04 pt, 12 pt.

**Observed layout.** A narrow main column carries long role-labelled biographies; the wide left gutter remains empty.

**Analytical job / reader use.** The page provides experience context but has limited analytical interpretation and inefficient space use.

**Instruction for the new report.** Summarise relevant delivery, tenure and role in a table. Avoid equating a long biography or prestigious prior employer with demonstrated execution.


#### SU-39. Remaining directors and organisation

**Source:** [SU, PDF page 39](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=39); printed 38. **Measured:** 595.32 x 841.92 pt; 302 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 9 pt, 8.04 pt.

**Observed layout.** Biographical text continues above a formal leadership chart with hierarchy and dotted reporting lines.

**Analytical job / reader use.** Responsibilities become more visible than in biographies alone.

**Instruction for the new report.** Assign accountability to the major forecast drivers. Verify roles and reporting lines as of the report date and avoid inventing missing executives.


#### SU-40. Decision recap and consensus difference

**Source:** [SU, PDF page 40](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=40); printed 39. **Measured:** 595.32 x 841.92 pt; 277 extracted words. **Type evidence:** FuturaBT-Light, SymbolMT; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** A small analyst-versus-consensus table leads into investment arguments, risks, triggers and a brief company description.

**Analytical job / reader use.** This late recap is useful because it identifies where the forecast differs from external expectations and what might cause revision.

**Instruction for the new report.** Move a concise version near the front in a new report. Quantify the earnings disagreement and show the driver rather than only the percentage difference.


#### SU-41. Quarterly reference model

**Source:** [SU, PDF page 41](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=41); printed 40. **Measured:** 595.32 x 841.92 pt; 335 extracted words. **Type evidence:** FuturaBT-Light; most-used sizes 8.04 pt, 9 pt.

**Observed layout.** A full-width quarterly income table includes common-size and growth sections. Grey bands identify major rows.

**Analytical job / reader use.** The reader can inspect recent seasonality and the base from which annual forecasts start.

**Instruction for the new report.** Reconcile quarters to the full year and isolate exceptional items. State consolidated/standalone scope and prevent quarter labels from shifting across charts.


#### SU-42. Annual earnings and ratios

**Source:** [SU, PDF page 42](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=42); printed 41. **Measured:** 595.32 x 841.92 pt; 434 extracted words. **Type evidence:** FuturaBT-Light; most-used sizes 8.04 pt, 9.96 pt, 9 pt.

**Observed layout.** A full-page annual statement table stacks profit, growth, key ratios, longer-run growth and valuation blocks.

**Analytical job / reader use.** The detailed forecast and history are accessible in a consistent grid.

**Instruction for the new report.** Define recurring versus reported profit and pre-/post-tax return metrics. Calculate all derivative ratios from common source cells.


#### SU-43. Balance sheet and cash-flow detail

**Source:** [SU, PDF page 43](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=43); printed 42. **Measured:** 595.32 x 841.92 pt; 479 extracted words. **Type evidence:** FuturaBT-Light, FuturaBT-LightItalic; most-used sizes 8.04 pt, 9 pt.

**Observed layout.** Balance sheet, capital ratios, working-capital days and cash flows share one full-width table system.

**Analytical job / reader use.** The cash and funding consequences of growth are available for audit.

**Instruction for the new report.** Reconcile assets and liabilities, opening and closing cash, and financing needs. Flag negative cash generation rather than relying on earnings growth alone.


#### SU-44. Definitions and disclosures

**Source:** [SU, PDF page 44](https://suprajit.com/wp-content/uploads/2022/08/Equirus-Securities-Suprajit-Engineering-IC-26042022.pdf#page=44); printed 43. **Measured:** 595.32 x 841.92 pt; 1783 extracted words. **Type evidence:** FuturaBT-Light; most-used sizes 6 pt, 8.04 pt.

**Observed layout.** Very small text, registration/contact boxes and a short relationship disclosure table fill the closing sheet.

**Analytical job / reader use.** The report contains substantial administrative content on one highly dense page.

**Instruction for the new report.** Use only applicable authorised legal text for the actual publisher. The six-point legal size is not a suitable target for analytical reading.


### AX. Building Materials sector - Axis


#### AX-01. Sector identity cover

**Source:** [AX, PDF page 1](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=1); printed unnumbered cover. **Measured:** 540 x 780 pt; 33 extracted words. **Type evidence:** Impact, FuturaLT-CondensedBold; most-used sizes 18 pt, 27.96 pt, 14.04 pt.

**Observed layout.** A blue raster cover uses a honeycomb collage of products, a large sector title and a boxed list of covered companies; a magenta publisher strip anchors the bottom.

**Analytical job / reader use.** The cover frames the document as a shared sector thesis with several company applications.

**Instruction for the new report.** Use a restrained sector visual and identify which companies are initiation versus update. The cover has different physical dimensions from the interior, so do not infer a universal page size from page one.


#### AX-02. Sector thesis and recommendation rail

**Source:** [AX, PDF page 2](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=2); printed 1. **Measured:** 595.44 x 841.68 pt; 647 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 9.48 pt, 8.04 pt.

**Observed layout.** A dense left narrative column summarises several demand mechanisms; the tall rounded right rail holds coverage, valuation facts and analyst details.

**Analytical job / reader use.** The reader gets the common thesis before the individual-company chapters. The rail supports comparison without interrupting the main narrative.

**Instruction for the new report.** Write the shared mechanisms once and map each to company exposure. Separate sector evidence from individual recommendations and company-specific forecasts.


#### AX-03. Company implications in prose

**Source:** [AX, PDF page 3](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=3); printed 2. **Measured:** 595.44 x 841.68 pt; 449 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 9.96 pt, 8.04 pt.

**Observed layout.** Three text sections explain the covered companies under magenta labels; bold introductory sentences carry each recommendation.

**Analytical job / reader use.** The page translates the sector thesis into different business implications, rather than assuming all constituents benefit equally.

**Instruction for the new report.** For each company identify the distinct driver, valuation constraint and risk. Avoid repeating the same generic tailwind three times.


#### AX-04. Document navigation

**Source:** [AX, PDF page 4](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=4); printed 3. **Measured:** 595.44 x 841.68 pt; 110 extracted words. **Type evidence:** Arial-BoldMT, Arial-ItalicMT; most-used sizes 9 pt, 8.04 pt, 12.96 pt.

**Observed layout.** A broad contents table uses thin grey rules, grouped sections and page numbers. The analytical sequence and company chapters are clearly separated.

**Analytical job / reader use.** The reader can choose sector education, drivers, risks or a single company without reading the full document.

**Instruction for the new report.** Generate linked contents from the final page map. Preserve the one-page offset created by the cover in source references.


#### AX-05. Sector taxonomy

**Source:** [AX, PDF page 5](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=5); printed 4. **Measured:** 595.44 x 841.68 pt; 170 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 9.96 pt, 11.04 pt.

**Observed layout.** A brief introductory argument sits above a simple classification tree; a small right-gutter callout summarises the expected recovery.

**Analytical job / reader use.** The tree defines what the report includes before presenting the size or growth of the universe.

**Instruction for the new report.** Use mutually exclusive subsegments and state exclusions. Ensure any market total corresponds to this classification and period.


#### AX-06. Industry evolution

**Source:** [AX, PDF page 6](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=6); printed 5. **Measured:** 595.44 x 841.68 pt; 299 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 9.96 pt, 8.04 pt.

**Observed layout.** Five chronological phases appear as concise bullet groups, with a summary table at the bottom.

**Analytical job / reader use.** The report explains how demand and customer preferences changed through time, providing context for premiumisation and formalisation.

**Instruction for the new report.** Keep only historical transitions relevant to current economics. A phase narrative needs evidence when it is used to justify a forecast.


#### AX-07. Wood-panel segment economics

**Source:** [AX, PDF page 7](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=7); printed 6. **Measured:** 595.44 x 841.68 pt; 207 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Three stacked exhibits show product mix, industry growth and substitution between materials, preceded by short explanatory prose.

**Analytical job / reader use.** The reader can distinguish growth of the total market from movement between product categories.

**Instruction for the new report.** Separate value and volume. Product substitution can benefit one company while hurting another; map current and upcoming capacity to the relevant category.


#### AX-08. Formalisation and import competition

**Source:** [AX, PDF page 8](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=8); printed 7. **Measured:** 595.44 x 841.68 pt; 151 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 9 pt, 6.96 pt.

**Observed layout.** A pie and two vertical bar charts cover organised share, import values and country mix. Short titles identify the comparison.

**Analytical job / reader use.** The page introduces both market-share opportunity and external supply competition.

**Instruction for the new report.** Do not present formalisation as unopposed growth. Compare imports, domestic supply additions, pricing and utilisation together.


#### AX-09. Tile-market classification

**Source:** [AX, PDF page 9](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=9); printed 8. **Measured:** 595.44 x 841.68 pt; 184 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 10.41 pt, 6.96 pt.

**Observed layout.** Market context paragraphs sit above a three-part classification graphic, leaving substantial lower white space.

**Analytical job / reader use.** The report defines products, end uses and market organisation before deeper tile exhibits.

**Instruction for the new report.** Use a compact taxonomy and combine this page with a relevant demand exhibit if the description is short. Avoid multiple incompatible segmentation bases.


#### AX-10. Tile competitors and volume growth

**Source:** [AX, PDF page 10](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=10); printed 9. **Measured:** 595.44 x 841.68 pt; 73 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A branching company tree occupies the top and a domestic/export volume chart sits below.

**Analytical job / reader use.** Market participants and growth composition become visible in one page.

**Instruction for the new report.** Ensure company categories are complete enough for the question. Compare domestic and export volumes on identical units and periods.


#### AX-11. Tile exports through three lenses

**Source:** [AX, PDF page 11](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=11); printed 10. **Measured:** 595.44 x 841.68 pt; 182 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 9 pt, 6.96 pt.

**Observed layout.** Three stacked charts show industry value growth, monthly export performance and destination mix.

**Analytical job / reader use.** The page moves from long-run scale to recent momentum and geographic exposure.

**Instruction for the new report.** Keep value versus volume distinct and identify price/FX effects. Monthly growth rates can be base-effect driven; show absolute levels beside them.


#### AX-12. Export position and policy chronology

**Source:** [AX, PDF page 12](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=12); printed 11. **Measured:** 595.44 x 841.68 pt; 173 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** An export-volume line chart and organised-market pie precede a dated policy discussion.

**Analytical job / reader use.** The reader sees trade exposure and the regulatory developments affecting it.

**Instruction for the new report.** Use exact decision dates and distinguish investigation, provisional duty and final order. Do not extend historical policy claims to the current date without verification.


#### AX-13. Bathware segments and pricing

**Source:** [AX, PDF page 13](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=13); printed 12. **Measured:** 595.44 x 841.68 pt; 345 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 10.56 pt, 10.58 pt.

**Observed layout.** A market description and three-arrow demand graphic lead into a broad table of price tiers, players and characteristics.

**Analytical job / reader use.** The report makes premium and standard segments economically distinct instead of using one broad market label.

**Instruction for the new report.** Check market boundaries for overlap. Use a table to relate customer, price, channel and margin differences; do not sum overlapping market-size estimates.


#### AX-14. Competitive landscape cards

**Source:** [AX, PDF page 14](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=14); printed 13. **Measured:** 595.44 x 841.68 pt; 85 extracted words. **Type evidence:** Arial-ItalicMT, Arial-BoldMT; most-used sizes 9 pt, 6.96 pt, 8.04 pt.

**Observed layout.** Seven magenta tiles identify principal competitors and positioning, with a small source line underneath.

**Analytical job / reader use.** The page is an industry orientation device, not a financial comparison.

**Instruction for the new report.** Use short positioning statements and link to a proper peer table. Cards are acceptable for a finite taxonomy; they are weak substitutes for comparable numeric evidence.


#### AX-15. Real-estate linkage

**Source:** [AX, PDF page 15](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=15); printed 14. **Measured:** 595.44 x 841.68 pt; 282 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 11.04 pt.

**Observed layout.** An explanatory block and side callout lead into construction-mix and supply/absorption charts.

**Analytical job / reader use.** The report introduces the lag between property activity and demand for finishing materials.

**Instruction for the new report.** Model the causal milestones: booking, construction, completion, fit-out and replacement. Correlation in the charts does not alone establish the size or stability of the lag.


#### AX-16. Timing and public expenditure

**Source:** [AX, PDF page 16](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=16); printed 15. **Measured:** 595.44 x 841.68 pt; 371 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 6.96 pt, 8.04 pt.

**Observed layout.** A lag-comparison chart sits above interpretation, a government-spend exposure table and further prose. A right-side callout repeats the timing thesis.

**Analytical job / reader use.** The reader can see why different building materials enter at different stages of construction.

**Instruction for the new report.** Use segment-specific lags rather than applying one delay to all materials. Distinguish government allocation from actual disbursement and supplier revenue.


#### AX-17. Policy mechanisms and funding

**Source:** [AX, PDF page 17](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=17); printed 16. **Measured:** 595.44 x 841.68 pt; 138 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 9 pt, 6.96 pt.

**Observed layout.** A policy chronology table precedes two public-spending charts.

**Analytical job / reader use.** The page supplies concrete policy and funding evidence for demand rather than only naming schemes.

**Instruction for the new report.** Track budget, release, implementation and actual project progress separately. Do not infer a fixed revenue multiplier from a budget announcement.


#### AX-18. Urbanisation and housing cohorts

**Source:** [AX, PDF page 18](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=18); printed 17. **Measured:** 595.44 x 841.68 pt; 268 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** An opening discussion, side note and two demographic/housing charts structure the page.

**Analytical job / reader use.** The report identifies changes in the customer base that could support demand over time.

**Instruction for the new report.** Match geographic exposure and affordability to the company's price tier. Demographic growth is a long-run condition, not a near-term order forecast.


#### AX-19. Household purchasing power

**Source:** [AX, PDF page 19](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=19); printed 18. **Measured:** 595.44 x 841.68 pt; 362 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A dense opening block with a side takeaway leads into per-capita and disposable-income charts.

**Analytical job / reader use.** The demand argument moves from population to ability to spend.

**Instruction for the new report.** Distinguish nominal from real purchasing power and per-capita from household measures. Link income changes to observable category spending.


#### AX-20. Income distribution

**Source:** [AX, PDF page 20](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=20); printed 19. **Measured:** 595.44 x 841.68 pt; 110 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 9 pt, 6.96 pt.

**Observed layout.** Three stacked exhibits compare national income, household income bands and city-tier distributions.

**Analytical job / reader use.** Distributional change is more informative than an average alone for premium consumption.

**Instruction for the new report.** Keep income-band definitions stable across years. Explain whether the charts show households, people, share or absolute counts.


#### AX-21. From income to product demand

**Source:** [AX, PDF page 21](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=21); printed 20. **Measured:** 595.44 x 841.68 pt; 163 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A city-tier bar chart leads into a two-column mechanism table and interpretation.

**Analytical job / reader use.** The report attempts to translate an abstract demographic trend into concrete purchase behaviour.

**Instruction for the new report.** Require evidence for the mapping. Higher income may increase housing demand or premium mix, but the revenue effect depends on prices, penetration and channel access.


#### AX-22. Formalisation mechanism

**Source:** [AX, PDF page 22](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=22); printed 21. **Measured:** 595.44 x 841.68 pt; 357 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 11.04 pt, 8.04 pt.

**Observed layout.** Text and a side callout explain regulatory and consumer shifts; a grouped organised-share chart appears below.

**Analytical job / reader use.** The page identifies why share might move toward larger firms, beyond the fact that a shift occurred historically.

**Instruction for the new report.** Separate regulatory compliance, brand preference and distribution as mechanisms. Identify which firms have the capacity and economics to capture the shift.


#### AX-23. Premium bathware discussion

**Source:** [AX, PDF page 23](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=23); printed 22. **Measured:** 595.44 x 841.68 pt; 196 extracted words. **Type evidence:** ArialMT, Arial-ItalicMT; most-used sizes 9 pt, 8.04 pt.

**Observed layout.** A few long bullet paragraphs occupy the upper area beside a summary callout; most of the page remains empty.

**Analytical job / reader use.** The page explains brand and manufacturing differences but provides limited direct quantitative evidence.

**Instruction for the new report.** Add mix, price premium, distribution or customer data. Avoid treating unused page area as a reason to manufacture more qualitative claims.


#### AX-24. Lifestyle and sustainability demand

**Source:** [AX, PDF page 24](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=24); printed 23. **Measured:** 595.44 x 841.68 pt; 425 extracted words. **Type evidence:** ArialMT, Calibri; most-used sizes 9 pt, 6.96 pt, 12 pt.

**Observed layout.** Bullets and a side note sit above a horizontal category-spending comparison, followed by synthesis prose.

**Analytical job / reader use.** The report broadens the demand thesis to renovation and home use.

**Instruction for the new report.** Connect the spending categories to the products actually sold. Sustainability features require evidence of adoption, price and cost, not only consumer-interest language.


#### AX-25. Digital channels as demand influence

**Source:** [AX, PDF page 25](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=25); printed 24. **Measured:** 595.44 x 841.68 pt; 149 extracted words. **Type evidence:** Arial-BoldMT, ArialMT; most-used sizes 8.97 pt, 8.98 pt, 10.1 pt.

**Observed layout.** Four stacked arrow-headed panels group online inspiration, influencers, commerce and DIY content.

**Analytical job / reader use.** The page communicates a qualitative mechanism quickly, but contains little financial measurement.

**Instruction for the new report.** Use a qualitative diagram only where evidence is qualitative. Add measurable acquisition, conversion or channel contribution before translating it into company forecasts.


#### AX-26. Operating leverage and valuation

**Source:** [AX, PDF page 26](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=26); printed 25. **Measured:** 595.44 x 841.68 pt; 357 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 6.96 pt, 8.04 pt.

**Observed layout.** Explanatory prose leads into a two-year valuation comparison chart and a broad peer multiple/return table.

**Analytical job / reader use.** The sector thesis is connected to expected earnings improvement and relative valuation.

**Instruction for the new report.** For categorical companies use grouped dots or bars rather than a continuous line that implies a meaningful ordering. Distinguish earnings growth from multiple expansion.


#### AX-27. Cross-company financial forecasts

**Source:** [AX, PDF page 27](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=27); printed 26. **Measured:** 595.44 x 841.68 pt; 122 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6 pt, 9 pt.

**Observed layout.** A full-width table compares revenue, EBITDA and PAT across several forecast years, with covered names highlighted.

**Analytical job / reader use.** The reader can compare the scale and profit conversion of different companies under a shared sector view.

**Instruction for the new report.** Normalise definitions, units and forecast source dates. Compute incremental margins and return requirements rather than only comparing growth rates.


#### AX-28. Risks and responses

**Source:** [AX, PDF page 28](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=28); printed 27. **Measured:** 595.44 x 841.68 pt; 467 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 9.96 pt, 6.96 pt.

**Observed layout.** A long two-column table pairs each risk with a possible mitigation; bold lead phrases help scanning.

**Analytical job / reader use.** The format forces a link between a problem and a response, although many mitigations are generic suggestions rather than verified company actions.

**Instruction for the new report.** Add exposure, leading indicator and residual risk. Label a recommended mitigation separately from an implemented company measure.


#### AX-29. First company management

**Source:** [AX, PDF page 29](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=29); printed 28. **Measured:** 595.44 x 841.68 pt; 153 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** A role/biography table occupies the upper half with thin horizontal rules.

**Analytical job / reader use.** The report provides execution context before the company chapters.

**Instruction for the new report.** Include responsibility, tenure and relevant results. A positive governance heading should not be treated as a demonstrated conclusion from biographies alone.


#### AX-30. Second company management

**Source:** [AX, PDF page 30](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=30); printed 29. **Measured:** 595.44 x 841.68 pt; 450 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 9.96 pt.

**Observed layout.** A longer two-column management table fills most of the page.

**Analytical job / reader use.** The reader can identify operating and financial responsibilities across functions.

**Instruction for the new report.** Use consistent fields across companies so the reader can compare capability and incentives rather than biography length.


#### AX-31. Company-section divider

**Source:** [AX, PDF page 31](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=31); printed 30. **Measured:** 595.44 x 841.68 pt; 9 extracted words. **Type evidence:** Arial-ItalicMT, FuturaLT-CondensedBold; most-used sizes 8.04 pt, 21.96 pt, 20.04 pt.

**Observed layout.** A nearly empty sheet carries a centred magenta section label within the recurring page frame.

**Analytical job / reader use.** The divider creates a clear structural break between sector work and company applications.

**Instruction for the new report.** Use only when navigation benefits justify an entire page. In a digital report a section break and bookmark may achieve the same effect more efficiently.


#### AX-32. First company investment entry

**Source:** [AX, PDF page 32](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=32); printed 31. **Measured:** 595.44 x 841.68 pt; 875 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6.96 pt, 9 pt.

**Observed layout.** A dense left thesis column, compact lower forecast table and rounded right facts rail repeat the front-page design at company level.

**Analytical job / reader use.** Shared industry evidence is converted into a company-specific thesis, including product and project drivers.

**Instruction for the new report.** Reference shared sector pages instead of repeating them. Make the company assumptions and valuation logic independently inspectable.


#### AX-33. First company operating chart grid

**Source:** [AX, PDF page 33](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=33); printed 32. **Measured:** 595.44 x 841.68 pt; 199 extracted words. **Type evidence:** Arial-BoldMT, ArialMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Six exhibits in a two-by-three grid cover market share, footprint, capacity, output and product-level sales.

**Analytical job / reader use.** The chapter starts with operating variables before consolidated earnings.

**Instruction for the new report.** Keep installed capacity and output separate and tie geographic/project metrics to the same asset ledger. This ordering helps readers test growth feasibility.


#### AX-34. First company financial chart grid

**Source:** [AX, PDF page 34](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=34); printed 33. **Measured:** 595.44 x 841.68 pt; 250 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Seven charts occupy a two-column grid with one final lower-left plot. Earnings, leverage, returns, capex and working capital complete the story.

**Analytical job / reader use.** The operating forecast is checked against capital requirements and financial outcomes.

**Instruction for the new report.** Show adverse as well as favourable outcomes and maintain comparable periods. Avoid implying historical ratios will persist after a large investment cycle.


#### AX-35. First company product evidence

**Source:** [AX, PDF page 35](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=35); printed 34. **Measured:** 595.44 x 841.68 pt; 15 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 6.96 pt, 9 pt, 8.04 pt.

**Observed layout.** Two large corporate product/lifestyle collages occupy the upper and middle page.

**Analytical job / reader use.** The reader can recognise the physical products and customer setting; independent analytical content is limited.

**Instruction for the new report.** Use images to explain product differentiation. Add measurable pricing, distribution or revenue relevance instead of treating a premium-looking photograph as premium economics.


#### AX-36. First company statements

**Source:** [AX, PDF page 36](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=36); printed 35. **Measured:** 595.44 x 841.68 pt; 269 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6.96 pt, 9 pt.

**Observed layout.** A full-width P&L table stacks above a balance sheet. Grey header bands and light rules keep the table restrained.

**Analytical job / reader use.** Forecast profit is paired with its balance-sheet consequences in a readable single-column system.

**Instruction for the new report.** Reconcile totals and label actual/estimated years. Keep the valuation forecast linked to these exact statement rows.


#### AX-37. First company cash and ratios

**Source:** [AX, PDF page 37](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=37); printed 36. **Measured:** 595.44 x 841.68 pt; 245 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6.96 pt, 9 pt.

**Observed layout.** Cash-flow rows appear above a ratio table grouped by profitability, efficiency, share data and valuation.

**Analytical job / reader use.** The reader can test cash conversion and future returns on the same horizon as earnings.

**Instruction for the new report.** Define the return denominator and CFO starting point. Reconcile capex, cash and debt rather than typing ratios independently.


#### AX-38. First company recommendation history

**Source:** [AX, PDF page 38](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=38); printed 37. **Measured:** 595.44 x 841.68 pt; 25 extracted words. **Type evidence:** Arial-BoldMT, ArialMT; most-used sizes 9.96 pt, 15 pt, 8.04 pt.

**Observed layout.** A historical price chart sits above a dated recommendation table; magenta bands separate the modules.

**Analytical job / reader use.** The reader can identify the history and date of the publisher's view.

**Instruction for the new report.** Use real historical recommendations only. A new independent publisher should not inherit another firm's past calls or imply a track record it does not have.


#### AX-39. Second company investment entry

**Source:** [AX, PDF page 39](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=39); printed 38. **Measured:** 595.44 x 841.68 pt; 934 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6.96 pt, 9.96 pt.

**Observed layout.** The same dense thesis-left/facts-right layout introduces a different business, with product, capacity and demand discussion.

**Analytical job / reader use.** The reader can compare the investment argument in a stable format while the underlying economics change.

**Instruction for the new report.** Keep the layout reusable but the driver model sector-specific. Do not fill identical boxes with generic arguments simply to preserve symmetry.


#### AX-40. Second company earnings chart grid

**Source:** [AX, PDF page 40](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=40); printed 39. **Measured:** 595.44 x 841.68 pt; 260 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 9 pt, 6.96 pt.

**Observed layout.** Six exhibits cover segment mix, revenue, margins, profit and asset deployment.

**Analytical job / reader use.** The page connects product composition to consolidated profitability and capital use.

**Instruction for the new report.** Differentiate gross, EBITDA and EBIT margins. Verify internal chart labels and statement rows before carrying the design into a new model.


#### AX-41. Second company capital and returns

**Source:** [AX, PDF page 41](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=41); printed 40. **Measured:** 595.44 x 841.68 pt; 177 extracted words. **Type evidence:** Arial-BoldMT, ArialMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Six exhibits show balance-sheet position, working capital, CFO, return ratios and market share.

**Analytical job / reader use.** The report tests the investment story beyond sales and earnings.

**Instruction for the new report.** Do not describe an absolute return as improving if the plotted forecast is flat or declining. A chart title must match the data, including temporary deterioration.


#### AX-42. Manufacturing process and bottlenecks

**Source:** [AX, PDF page 42](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=42); printed 41. **Measured:** 595.44 x 841.68 pt; 286 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 9 pt, 6.96 pt, 9.96 pt.

**Observed layout.** Production prose and a process-flow image occupy the page, with a second product-line discussion below.

**Analytical job / reader use.** The reader learns why capacity, yield, energy and cycle time matter to this business.

**Instruction for the new report.** Redraw the process as editable vector elements and annotate bottleneck, utilisation, rejection and energy intensity where disclosed. Process detail matters when connected to economics.


#### AX-43. Process, brand and geography

**Source:** [AX, PDF page 43](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=43); printed 42. **Measured:** 595.44 x 841.68 pt; 67 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 6.96 pt, 9 pt, 8.04 pt.

**Observed layout.** A process strip, retail/experience-centre photographs, brand tiers and a geographic bar chart stack vertically.

**Analytical job / reader use.** The page links production, merchandising and customer segmentation in one visual reference.

**Instruction for the new report.** Use consistent source dates and state whether brand tiers have different economics. Consider splitting the page if the process is too small to read.


#### AX-44. Second company statements

**Source:** [AX, PDF page 44](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=44); printed 43. **Measured:** 595.44 x 841.68 pt; 286 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6.96 pt, 9 pt.

**Observed layout.** P&L and balance-sheet tables occupy the full width, with grouped grey headers.

**Analytical job / reader use.** The shared table system supports comparison with the previous company.

**Instruction for the new report.** Keep financial definitions consistent while respecting business-specific line items. Do not force a different accounting structure into an identical row set.


#### AX-45. Second company cash and ratios

**Source:** [AX, PDF page 45](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=45); printed 44. **Measured:** 595.44 x 841.68 pt; 253 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6.96 pt, 9 pt.

**Observed layout.** A cash-flow table precedes profitability, efficiency and valuation ratios.

**Analytical job / reader use.** The forecast's cash and capital implications are made available for inspection.

**Instruction for the new report.** Reconcile working capital and cash balances, and define invested capital. Show whether cash accumulation materially changes enterprise value.


#### AX-46. Second company recommendation history

**Source:** [AX, PDF page 46](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=46); printed 45. **Measured:** 595.44 x 841.68 pt; 25 extracted words. **Type evidence:** Arial-BoldMT, ArialMT; most-used sizes 15 pt, 9 pt, 9.96 pt.

**Observed layout.** A price chart and one dated recommendation row repeat the earlier historical-view page.

**Analytical job / reader use.** The format provides provenance for the initiation.

**Instruction for the new report.** Retain the actual publisher and date when referring to historical research; do not transplant the rating as a current conclusion.


#### AX-47. Third company update entry

**Source:** [AX, PDF page 47](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=47); printed 46. **Measured:** 595.44 x 841.68 pt; 806 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6.96 pt, 9.96 pt.

**Observed layout.** A thesis narrative and compact forecast table occupy the left, while the right rail holds facts and relative performance.

**Analytical job / reader use.** An existing coverage update shares the initiation format but focuses on current drivers and outlook.

**Instruction for the new report.** Explicitly identify what changed from the previous forecast: volume, price, margin, capex or valuation. Repeating the standing thesis is insufficient for an update.


#### AX-48. Third company operating and margin grid

**Source:** [AX, PDF page 48](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=48); printed 47. **Measured:** 595.44 x 841.68 pt; 182 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 9 pt, 6.96 pt.

**Observed layout.** Six charts cover segment revenue, total sales, gross margin, EBITDA, EBITDA margin and employee-cost ratio.

**Analytical job / reader use.** The chart sequence connects commercial growth to cost structure.

**Instruction for the new report.** Show volume/price decomposition where commodity pass-through matters. A declining cost ratio can reflect sales denominator inflation as well as efficiency.


#### AX-49. Third company cash and capital grid

**Source:** [AX, PDF page 49](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=49); printed 48. **Measured:** 595.44 x 841.68 pt; 190 extracted words. **Type evidence:** Arial-BoldMT, ArialMT; most-used sizes 9 pt, 8.04 pt, 6.96 pt.

**Observed layout.** Six exhibits address asset turns, capex, CFO, working capital and returns.

**Analytical job / reader use.** The report adds capital discipline and cash conversion to the earnings story.

**Instruction for the new report.** Link these exhibits to one model. Test whether stronger asset turns come from productive use, higher selling prices or a small historical asset base.


#### AX-50. Third company statements

**Source:** [AX, PDF page 50](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=50); printed 49. **Measured:** 595.44 x 841.68 pt; 308 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6.96 pt, 9 pt.

**Observed layout.** A full-width P&L table is followed by the balance sheet, using light grey subsection bands.

**Analytical job / reader use.** The same financial grid makes the company chapters easier to compare.

**Instruction for the new report.** Maintain consistent units and include associates, minority interests or exceptional items explicitly when relevant.


#### AX-51. Third company cash and ratios

**Source:** [AX, PDF page 51](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=51); printed 50. **Measured:** 595.44 x 841.68 pt; 271 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 6.96 pt, 9 pt.

**Observed layout.** Cash flows, opening/closing cash and a compact ratio section stack down the page.

**Analytical job / reader use.** The reader can inspect funding, cash accumulation and model assumptions.

**Instruction for the new report.** Show the CFO starting point and prevent tax or interest double counting. Reconcile ratios to the same year and share base used in valuation.


#### AX-52. Third company recommendation history

**Source:** [AX, PDF page 52](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=52); printed 51. **Measured:** 595.44 x 841.68 pt; 55 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.04 pt, 15 pt, 9.96 pt.

**Observed layout.** A price chart appears above a longer multi-date recommendation table with colour-coded rating words.

**Analytical job / reader use.** The report makes changes in its own view traceable over time.

**Instruction for the new report.** A new report should record its own actual revisions and reasons. Colour must not be the only way to distinguish recommendation categories.


#### AX-53. Disclosure framework

**Source:** [AX, PDF page 53](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=53); printed 52. **Measured:** 595.44 x 841.68 pt; 1372 extracted words. **Type evidence:** ArialMT, Arial-ItalicMT; most-used sizes 6.48 pt, 8.04 pt, 9.96 pt.

**Observed layout.** Very small prose, publisher details and a signature block fill the page within the standard magenta frame.

**Analytical job / reader use.** The page supplies administrative provenance and legal context.

**Instruction for the new report.** Use only applicable authorised disclosures and accurate publisher identity. Do not copy signatures or registration numbers.


#### AX-54. Closing disclosures and rating definitions

**Source:** [AX, PDF page 54](https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating%2BCoverage%2B-%2BBuilding%2BMaterials%2B-%2B16072025%2B%282%29_16-07-2025_10.pdf/type/fundamental#page=54); printed 53. **Measured:** 595.44 x 841.68 pt; 585 extracted words. **Type evidence:** ArialMT, MyriadPro-Regular; most-used sizes 6.48 pt, 5.91 pt, 8.04 pt.

**Observed layout.** Further legal prose and a rating-methodology table occupy the upper portion, followed by white space.

**Analytical job / reader use.** Definitions help readers interpret the recommendation scale and horizon.

**Instruction for the new report.** Treat definitions as part of the publisher's method and label them accurately. Avoid presenting inherited broker categories as an independent rating system.


### MQ. MedPlus quarterly update - Keynote


#### MQ-01. Current-quarter argument

**Source:** [MQ, PDF page 1](https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf#page=1); printed 1. **Measured:** 594.72 x 842.4 pt; 652 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 10.1 pt, 10.08 pt, 7.92 pt.

**Observed layout.** A wide grey title band replaces the older red decorative frame. A left narrative and right facts rail use Arial; blue charts and grey modules create a more restrained update format.

**Analytical job / reader use.** The opening focuses on earnings change, margin offsets, execution and valuation. It assumes the reader already understands the business.

**Instruction for the new report.** Lead with what changed and why. Reconcile the quarter, recurring earnings, forecast revisions and valuation before writing a conclusion.


#### MQ-02. Results and operating bridge

**Source:** [MQ, PDF page 2](https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf#page=2); printed 2. **Measured:** 594.72 x 842.4 pt; 325 extracted words. **Type evidence:** ArialMT, Arial-BoldItalicMT; most-used sizes 7.2 pt, 7.92 pt, 7.22 pt.

**Observed layout.** A large results table includes current/prior quarters, YoY/QoQ comparisons, half-year data and full-year reference; smaller segment and mature-store tables follow.

**Analytical job / reader use.** The page separates group financial performance from segment and mature-unit economics.

**Instruction for the new report.** Use percentage points or basis points for margins and percentages for growth. Preserve scope and avoid mistaking a mature-store metric for group profitability.


#### MQ-03. Six operational monitoring charts

**Source:** [MQ, PDF page 3](https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf#page=3); printed 3. **Measured:** 594.72 x 842.4 pt; 179 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 8.66 pt, 10.1 pt, 8.64 pt.

**Observed layout.** A two-by-three grid shows product/geographic mix, cohort age, gross/net additions, online sales and revenue per store over recent quarters.

**Analytical job / reader use.** These are the variables needed to test whether the original thesis is progressing, rather than a fresh business tutorial.

**Instruction for the new report.** Select the same driver KPIs used in the initiation model. Show closures as the difference between gross and net additions, and match quarter boundaries across all charts.


#### MQ-04. Call evidence behind the quarter

**Source:** [MQ, PDF page 4](https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf#page=4); printed 4. **Measured:** 594.72 x 842.4 pt; 503 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 10.08 pt, 10.1 pt, 15.86 pt.

**Observed layout.** Bold subheads and indented bullets organise financial performance, stores and private-label discussion. No charts compete with the detailed explanation.

**Analytical job / reader use.** The report records non-recurring items, management commentary and operating developments that explain the tables.

**Instruction for the new report.** For each important comment capture fact, cause, recurring status, forecast effect and source. Keep management attribution explicit instead of converting commentary into certainty.


#### MQ-05. Commercial terms and forward watchpoints

**Source:** [MQ, PDF page 5](https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf#page=5); printed 5. **Measured:** 594.72 x 842.4 pt; 407 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 10.1 pt, 10.08 pt, 15.86 pt.

**Observed layout.** The bullet-led continuation covers franchise mechanics and general operating updates.

**Analytical job / reader use.** The reader receives model-changing detail about revenue recognition, economics, labour costs, expansion and management expectations.

**Instruction for the new report.** Translate changed commercial terms into a worked unit example and revise the model. Separate existing commitments from plans awaiting future guidance.


#### MQ-06. Updated forecast reference

**Source:** [MQ, PDF page 6](https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf#page=6); printed 6. **Measured:** 594.72 x 842.4 pt; 700 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 7.2 pt, 7.22 pt, 7.92 pt.

**Observed layout.** A tightly packed two-column statement-and-ratio page uses small type and restrained grey headers.

**Analytical job / reader use.** The quarterly evidence feeds an updated multi-year model, though the compressed layout remains difficult to read at normal size.

**Instruction for the new report.** Provide a revisions table comparing old and new estimates in addition to the absolute model. Split statements if the typography drops below a practical reading size.


#### MQ-07. Actual recommendation history

**Source:** [MQ, PDF page 7](https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf#page=7); printed 7. **Measured:** 594.72 x 842.4 pt; 559 extracted words. **Type evidence:** ArialMT, Calibri; most-used sizes 7.92 pt, 7.94 pt, 10.1 pt.

**Observed layout.** A wide dated ratings table sits above rating definitions and initial disclosures.

**Analytical job / reader use.** The update makes its own evolving view inspectable rather than implying a timeless thesis.

**Instruction for the new report.** Record reasons for changes as well as dates and target outcomes. Do not fabricate history when starting a new report series.


#### MQ-08. Relationships and distribution terms

**Source:** [MQ, PDF page 8](https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf#page=8); printed 8. **Measured:** 594.72 x 842.4 pt; 865 extracted words. **Type evidence:** ArialMT, Calibri; most-used sizes 7.92 pt, 7.94 pt, 10.1 pt.

**Observed layout.** A bordered conflict matrix and compact legal paragraphs fill most of the page.

**Analytical job / reader use.** The same disclosure obligations persist despite a shorter research format.

**Instruction for the new report.** Use accurate current publisher disclosures in a separate small-text style; do not let legal copy dictate analytical typography.


#### MQ-09. Closing legal notice

**Source:** [MQ, PDF page 9](https://cdn.sanity.io/files/pc8ly5qk/production/a9201d2bb22c440cb825c9e4a1433d3c57963616.pdf#page=9); printed 9. **Measured:** 594.72 x 842.4 pt; 891 extracted words. **Type evidence:** ArialMT, Arial-BoldMT; most-used sizes 7.92 pt, 7.94 pt, 10.1 pt.

**Observed layout.** Small black text and publisher contacts close the document below the recurring grey title band.

**Analytical job / reader use.** The document ends with administrative material, not additional operating evidence.

**Instruction for the new report.** Keep the final company conclusion in the opening or analytical section. Reuse only authorised legal content and actual publisher details.
