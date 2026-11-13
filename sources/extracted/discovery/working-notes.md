# RoomIQ: Working Notes (cross-screen analysis)

These are running notes that tie the screens together. They feed the GTM brief and PRD, which are **not drafted yet** and wait until every screenshot batch is in. Each batch adds to this file.

Last updated: 2026-11-10 (batches 1–3, screens 01–15)

---

## 1. What the product appears to be (working hypothesis)
RoomIQ is a market and property intelligence SaaS for the **US rent-by-the-room / co-living** segment. It tracks room-level listings (weekly asking rent, move-in fees, occupied versus available rooms, listing status, price drops, reviews, photos). From those it builds:
- **market-level** scores, leaderboards, seasonality and forecasts (Dashboard),
- **property-level** deep dives (Property Analyzer):
  - signal classification and recommendations,
  - room-segment economics,
  - 7/30/90-day rolling windows,
  - evidence quality,
  - **computer-vision visual comps** (Visually Similar Rooms),
  - **generative-AI upgrade concepts** (Media Studio),
- **underwriting** of *any* US address, tracked or not (Property Predictor):
  - a guided baseline profile (room mix, bathroom mix, physical context),
  - in-form recommendation helpers (layouts, amenity ROI, house rules, per-room pricing, cohort lease-up),
  - a revenue forecast with model routing, evidence lookback, fallback and confidence labeling,
  - conversion scenarios (garage),
  - a **Deal Calculator** (Pro): cash flow, CoC, DSCR, cap rate,
  - saved **My Underwrites** that can be re-run.

**End-to-end workflow, as seen in batch 3:** Discover a market (Dashboard) → Inspect comparable properties (Analyzer) → Underwrite a target (Predictor) → Model financed returns (Deal Calculator) → Save and monitor (My Underwrites). The drawer CTA "Forecast Stabilized Revenue" links Dashboard → Predictor. This makes the **acquisition-minded investor/operator** the clearest primary ICP.

The batch-2 screens add a clear **AI/CV layer**. RoomIQ ranks markets, and it can also *see* rooms (visual similarity → price and fill-time comps) and *imagine* upgrades (AI staging/renovation previews). That differentiation matters for GTM.

**[Inferred] ICP candidates**
- Rent-by-the-room operators and investors deciding where to buy, convert or price (the Dashboard plus market scores).
- Hosts benchmarking their own properties and planning upgrades (Analyzer: segment premiums, visual comps, Media Studio).
- Lenders and underwriters (evidence quality, rolling windows, revenue estimates).
- Brokers and acquisition analysts (stabilized revenue forecasts).

**[Q]** Where does the data come from? The data model matches listings on a rent-by-the-room marketplace platform:
- weekly room pricing and a room move-in fee,
- host first name + last initial,
- room-level occupancy,
- Listed / Coming soon / Delisted states,
- listing titles and photos.

Confirm the source(s), the collection method and the terms. These are core to GTM risk and messaging, and the risk is now higher because the product **makes AI-generated derivatives of listing photos**.

---

## 2. Information architecture (so far)
```
ROOMIQ
├── ANALYTICS
│   ├── Dashboard
│   │   ├── [gate] Choose markets (≤3 cities / ZIP / metro group)
│   │   ├── Header: market name + date range
│   │   ├── Toolbar: Views · Date preset · Filters · Market Report
│   │   ├── Tabs: Overview (n props) · Trends · Forecasts
│   │   │   ├── Overview → Top US markets by Market Score (+ more below the fold)
│   │   │   ├── Trends → Seasonality (Occupancy | Fill speed)
│   │   │   └── Forecasts → (not yet seen)
│   │   ├── Explore map (Leaflet) → clusters, hex submarket cells, layers, legend
│   │   └── Property detail drawer → KPIs, revenue estimate, CTAs (→ Predictor, → Analyzer)
│   └── Property Analyzer
│       ├── Search (city / property ID / free text) + History window (90d…)
│       ├── Stepper: Search → Pick property → Analyze
│       ├── Left: Properties results list
│       └── Right: Property analysis
│           ├── Property Signal header (label, recommendation, Signal/Evidence/Flagged rooms/Best spread)
│           ├── Tabs: Overview · Trends · Rooms
│           └── Overview (scroll order)
│               ├── Performance Snapshot (+ 30d occ Δ)
│               ├── [card cut off: "O… lif… · Establish…"]
│               ├── Room segments: Bathroom (Private / Shared) · Room size mix (Cozy / Standard)
│               ├── Rolling windows: 7d · 30d · 90d
│               ├── Evidence Quality (Completeness · History coverage · Media)
│               ├── Visually Similar Rooms (CV comps)
│               ├── Media Studio (AI upgrade concept)
│               └── Property Photos (reference gallery)
├── PREDICTOR
│   └── Property Predictor: "Underwrite a property"
│       ├── Baseline Forecast card (Unlimited baseline runs · Draft autosave · Reset · Start fresh)
│       ├── Stepper: Location → Baseline → Forecast → Results
│       ├── 1 Location: address search / draggable pin · Nearby coliving supply (~3 mi)
│       ├── 2 Baseline Profile
│       │   ├── Core Specifications (Required: type, bedrooms · Recommended: baths, sqft)
│       │   ├── Bathroom Mix (active rooms, private-bath rooms, shared-bath pressure) + Bedroom mix recommendation
│       │   ├── Amenity ROI recommendation
│       │   ├── House Rules for this Area
│       │   ├── Room Pricing: Per-room price optimizer (+ expand comps to 10 mi)
│       │   ├── Cohort outcomes (lease-up trajectories)
│       │   ├── Room Mix (room-level entries)
│       │   └── Access & Common Areas (common space, garage, transit distance)
│       ├── 3 Run Forecast: Model Routing (Automatic) · Market Evidence lookback (270d)
│       ├── 4 Decision Board: monthly revenue, support/confidence, scenarios, comps, next step, Garage conversion
│       ├── 5 Deal Calculator [Pro]: Scenario · Income · Purchase · Financing · (Expenses?) → Deal snapshot
│       └── My Underwrites (saved/exported reports, re-run)
└── Global: theme toggle · sidebar collapse · plan badge · account menu · Privacy choices
```

---

## 3. Current product features: capability list (observed and inferred, not yet prioritized)

### 3a. Dashboard and market intelligence (batch 1)
| # | Capability | Where | Evidence |
|---|---|---|---|
| C1 | Market selection by city, ZIP or metro group, up to 3 | Dashboard gate | Observed |
| C2 | Curated metro presets (7, all Sun Belt) | Dashboard gate | Observed |
| C3 | Multi-market dashboard header with a trailing date range | Dashboard | Observed |
| C4 | Date-range presets (Last 365d, …) | Dashboard toolbar | Observed (other presets unknown) |
| C5 | Saved Views | Dashboard toolbar | Observed button, behavior inferred |
| C6 | Filters + Advanced filters (dormant properties toggle) | Dashboard toolbar / map | Observed button + helper copy |
| C7 | Downloadable Market Report | Dashboard toolbar | Observed button (disabled?), format unknown |
| C8 | Property count per selected market | Overview tab badge | Observed (412) |
| C9 | National leaderboard: Top US markets by Market Score (score/100, grade, badge, occ %, trend/mo, property count) | Overview | Observed |
| C10 | Seasonality curves (Occupancy, Fill speed) with a national fallback | Trends | Observed |
| C11 | Forecasts | Forecasts tab | Tab seen, content unknown |

### 3b. Map and geospatial (batch 1)
| # | Capability | Where | Evidence |
|---|---|---|---|
| C12 | Interactive map with clustering, reset view, fullscreen, zoom, map search | Explore map | Observed |
| C13 | Color-by / Size-by encodings (Occupancy / Total rooms + others?) | Map layers | Observed |
| C14 | Property lifecycle status legend (Listed, Coming soon, Never listed, Delisted) | Map layers | Observed |
| C15 | Hex-grid submarket signal layer (Occupancy Health + other signals?) | Map layers | Observed |
| C16 | Evidence-adjusted cell scoring with Strong / Watch / Weak / Thin bands; tap a band to filter | Map legend | Observed |
| C17 | Snapshot-date selector on the score (point in time) | Map legend | Observed |
| C18 | FEMA flood-hazard overlay (NFHL) | Map layers | Observed toggle |

### 3c. Property detail drawer (batch 1)
| # | Capability | Where | Evidence |
|---|---|---|---|
| C19 | Property detail drawer: photo, type/BR/BA, occupancy, avg weekly asking, move-in fee, rooms occupied/total, available, reviews, price drops | Drawer | Observed |
| C20 | Estimated rental revenue for a window, with a disclaimer | Drawer + Analyzer | Observed |
| C21 | Hand-off: property → Forecast Stabilized Revenue (Predictor) | Drawer CTA | Observed |
| C22 | Hand-off: property → Analyzer | Drawer CTA | Observed |

### 3d. Property Analyzer (batches 1–2)
| # | Capability | Where | Evidence |
|---|---|---|---|
| C23 | Search by city, property ID **or free text in listing titles**; history window (90d…); 3-step flow with completion checks | Analyzer | Observed (b1 + b2) |
| C24 | Analyzer outputs: snapshot KPIs, rolling windows, room-level history, data-quality coverage | Analyzer | **Now observed** (b2): snapshot, rolling windows and evidence quality seen; room-level history assumed to be in the `Rooms` tab |
| C28 | Property results list: count, result cards (title, host, city, bd · type), selected state, "Showing X of Y" | Analyzer: Pick property | Observed |
| C29 | **Property Signal classification**: an action label (e.g., `Useful benchmark`) plus a plain-language recommendation ("Use this as a benchmark read…") | Analyzer header | Observed |
| C30 | Signal tiles: Signal · Evidence (coverage-based) · Flagged rooms (n of tracked) · Best spread (segment premium, e.g., bathroom premium) | Analyzer header | Observed |
| C31 | "Metrics as of" freshness stamp | Analyzer header | Observed |
| C32 | Analyzer tabs: Overview · Trends · Rooms | Analyzer | Observed (Trends / Rooms content not yet seen) |
| C33 | Performance Snapshot: occupancy, avg weekly asking, estimated revenue (window), rooms occupied/available, reviews/drops, 30d occ Δ | Analyzer Overview | Observed |
| C34 | **Room segmentation economics**: bathroom type (Private / Shared) and room size mix (Cozy / Standard), each with room count, avg weekly and 90d occupancy | Analyzer Overview | Observed |
| C35 | **Rolling windows 7d / 30d / 90d**: avg occupancy, avg daily price, volatility, Occ Δ and Price Δ against the prior window | Analyzer Overview | Observed |
| C36 | **Evidence Quality**: completeness %, history coverage %, media count, overall badge (High) | Analyzer Overview | Observed |
| C37 | Lifecycle/stage card (probably "… lifecycle · Established") | Analyzer Overview | Partly visible; confirm |

### 3e. AI and computer vision (batch 2)
| # | Capability | Where | Evidence |
|---|---|---|---|
| C38 | **Visually Similar Rooms**: image-similarity search across markets; % match, price/wk, days-to-fill (color-coded), location; summary medians (price, days to fill); click through to the property | Analyzer | Observed |
| C39 | **Media Studio, AI upgrade concepts**: pick a listing photo, choose an upgrade preset (Add desk, Add ceiling fan, Repaint neutral, LVP flooring, Stage empty room), generate, compare side by side, download | Analyzer | Observed |
| C40 | **Responsible-AI safeguards**: burned-in watermark (tiled "AI CONCEPT" + banner "AI-GENERATED - NOT ACTUAL PROPERTY CONDITION"), in-app disclaimer, and a "no validated economics" note | Media Studio + exported file | Observed |
| C41 | Upgrade-economics roadmap (ROI per edit) | Media Studio footer | Inferred from "no validated economics for this edit yet" |
| C42 | Property Photos reference gallery ("merchandising review"), placed below the operating signal | Analyzer | Partly visible |

### 3f. Property Predictor: underwriting (batch 3)
| # | Capability | Where | Evidence |
|---|---|---|---|
| C43 | **Guided underwriting wizard**: 4-step stepper + accordion with locked steps; **draft autosave**; reset; Start fresh; "Unlimited baseline runs" entitlement | Predictor | Observed |
| C44 | **Underwrite any US address**: geocoded address search or a draggable map pin | Predictor: Location | Observed |
| C45 | **Nearby coliving supply** count within ~3 mi, on a map | Predictor: Location | Observed (NYC: 0) |
| C46 | Baseline Core Specifications with tiered inputs (Required / Recommended), inline validation and a blocker count | Predictor: Baseline | Observed |
| C47 | **Bathroom Mix modeling**: active rooms, private-bath rooms, shared-bath pressure (shared rooms per shared bath); "Use bedrooms as rooms"; "Add room" | Predictor: Baseline | Observed |
| C48 | **Bedroom mix recommendation**: "Compare layouts" using property details + nearby room evidence | Predictor: Baseline | Observed (disabled until inputs) |
| C49 | **Amenity ROI recommendation**: automatic shortlist of upgrades worth checking | Predictor: Baseline | Observed button, output not seen |
| C50 | **House Rules for this Area**: an operating checklist compared with recorded local policies | Predictor: Baseline | Observed button, output not seen |
| C51 | **Per-room price optimizer**: starting weekly rent for an unpriced room or a check on an existing rent; optional expansion of the comp radius to 10 mi, with local vs expanded support shown separately | Predictor: Baseline | Observed |
| C52 | **Cohort outcomes**: listed-room occupancy trajectories (lease-up curves, including stalls) of comparable active launches nearby | Predictor: Baseline | Observed `Load`, output not seen |
| C53 | Room Mix: room-level entries (sellable rooms, room sqft, private-bath status) | Predictor: Baseline | Observed (empty state) |
| C54 | Access & Common Areas: common space, garage parking, transit distance. Physical inputs only; soft signals excluded on purpose | Predictor: Baseline | Observed |
| C55 | **Automatic model routing**: the tracked-history model when available, otherwise a bounded underwriting path with conservative structural adjustments | Predictor: Run Forecast | Observed |
| C56 | **Evidence lookback slider** (Recent signal ↔ Seasonal depth; default 270d) for forecast-stability testing | Predictor: Run Forecast | Observed |
| C57 | **Forecast results / Decision Board**: monthly revenue with the formula shown, support level (e.g., Fallback), confidence (Low…), illustrative ±10% scenarios, forecast support (comp count, median comp distance), best next step, KPI tiles (weekly room price, occupancy, active rooms, revenue/room), incomplete-data banner | Predictor: Results | Observed |
| C58 | Support details: comparable properties + caution flags (expandable) | Predictor: Results | Observed (collapsed) |
| C59 | **Garage conversion scenario**: 1-car / 2-car; re-runs the forecast as parking vs bedrooms; Compare | Predictor: Results | Observed, output not seen |
| C60 | **Deal Calculator (Pro)**: Conservative / Base / Aggressive scenario; income (room revenue prefilled, other income, vacancy); purchase (price + slider, ARV, seller concessions, closing costs %/$); financing (Financed / Cash, down payment, interest rate…); Deal snapshot → cash flow, CoC, DSCR, cap rate | Predictor | Observed (inputs), outputs not yet seen |
| C61 | **My Underwrites**: saved/exported property or market reports; **re-run to see market movement since export** | Predictor | Observed (empty state) |
| C62 | Property report export (an "underwrite" is created on export) | Predictor / Analyzer? | Inferred from the My Underwrites copy |

### 3g. Platform (batch 1)
| # | Capability | Where | Evidence |
|---|---|---|---|
| C25 | Plan tiers / entitlements (Pro, "Unlimited analyzer access") | Global / Analyzer | Observed badges |
| C26 | Light/dark theme | Sidebar | Observed toggle |
| C27 | Privacy choices (consent management) | Sidebar footer | Observed link |

---

## 4. Metric and term glossary (draft definitions to confirm)
| Term (as shown in the UI) | Working definition | Confirm? |
|---|---|---|
| Occupancy | Occupied rooms ÷ total rooms (property: 5/8 = 62.5% ✔, 7/8 = 87.5% ✔) | Market-level aggregation method? Weighted by rooms? |
| Market Score (/100) | Composite market attractiveness score | Inputs and weights |
| Grade (B) | Letter band of the Market Score | Band cutoffs |
| `High` badge (leaderboard) | Probably confidence or data sufficiency | Meaning |
| Trend %/mo | Monthly change in occupancy (pp or %?) | Unit |
| Fill speed / Days to fill | How fast a vacant room is re-leased; at room level, "filled in N days" | Formula; chip thresholds (≈ ≤5 green, 8–27 grey, ≥33 yellow) |
| Occupancy Health | Cell-level demand signal from observed occupied rooms | Formula |
| Occupancy Score bands | Strong / Watch / Weak / Thin | Thresholds; Thin = minimum-evidence cutoff |
| Evidence-adjusted | Shrinkage or Bayesian adjustment for small samples | Method |
| Cells | Hex submarket units (205 in DFW) | Grid type and resolution (H3 res?) |
| Live listing | Listed status, counted in market metrics | Is "Coming soon" counted too? |
| Dormant property | Non-live property, hidden unless Advanced filters are on | Definition |
| Avg weekly asking | Mean asking rent per room per week | Across all rooms or vacant only? Which window? |
| Avg daily price | Weekly price ÷ 7 ($260 / 7 ≈ $37 ✔) | Confirm |
| Avg room move-in fee | Mean one-time move-in fee per room | Check the $1 value |
| Estimated rental revenue | ≈ avg weekly asking × occupied rooms × weeks in window ($260 × 7 × 30/7 = $7,800 vs. $7,742 shown) | Exact formula (daily occupancy-weighted?) |
| Partial period | The last 30 days (2026-10-11 → 2026-11-09) in both examples | Why "partial"? |
| Stabilized revenue | Forecast revenue at stabilized occupancy (Predictor) | Definition |
| National pattern | US-wide seasonality used when local data is thin | Threshold for using local data |
| Property Signal | Action label for a property (seen: `Useful benchmark`) | Full label set and rules |
| Evidence (Coverage-based) | Property-level confidence from Evidence Quality | Bands (High / Med / Low?) |
| Flagged rooms | Rooms with anomalies or data issues, out of rooms tracked | Flag rules |
| Best spread | Largest avg-price gap between room segments (Private $310 − Shared $238 = $72 ✔) | Across which dimensions? |
| Bathroom premium | Best spread on the bathroom dimension | none |
| Room segment | A grouping of rooms by attribute: bathroom (Private / Shared), size (Cozy / Standard …) | Source of the tags; full taxonomy |
| 90d occ (segment) | Room-weighted occupancy of the segment over 90 days (reconciles to the property's 62.5% ✔) | none |
| Volatility | Dispersion of occupancy (or price) within the window (4.37 / 11.15 / 22.82) | Unit and formula |
| Occ Δ / Price Δ | Change against the prior equal-length window. 51.4% is probably **relative**, not pp | Confirm; N/A when there isn't enough history |
| Completeness | % of expected data fields present | Definition |
| History coverage | % of the history window with observations | Definition |
| Media (9 + 34) | Probably property photos + room photos | Label |
| % match | Visual-similarity score between room photos (94–96% seen) | Model; minimum threshold |
| AI concept | Generative edit of a listing photo showing an upgrade | Model/vendor; cost per generation |
| Underwrite | A saved Predictor or market report that can be re-run against fresh market data | Retention/versioning |
| Baseline (forecast / run) | The Predictor's revenue forecast from the baseline profile. "Baseline" and "Forecast" are used for the same thing | Pick one term |
| Tracked history | The path used when RoomIQ already observes the property | none |
| Bounded underwriting path | The comp-based model for new manual properties; structural details as conservative adjustments | Bounds / caps |
| Model routing (Automatic) | Picks the tracked-history vs bounded path | Can a user override it? |
| Evidence lookback | Window of market evidence used for priors and comps (default 270d) | Range |
| Market priors | Market-level baseline expectations the forecast leans on | Method (Bayesian?) |
| Fallback support | Local evidence was too thin, so broader-area comps were used | Radius steps |
| Confidence (Low / …) | Forecast confidence label | Levels and criteria |
| Median comp distance | Median miles from the subject to its comps (82.88 mi in NYC) | Max allowed? |
| Illustrative scenarios | ±10% of base revenue; explicitly **not** a prediction interval | Fixed 10%? |
| Shared-bath pressure | Shared rooms per shared bathroom | none |
| Active rooms | Sellable rooms entered in Room Mix (1.0 in the example) | Why a decimal? |
| Revenue per room | Monthly revenue ÷ active rooms | none |
| 4.35 weeks | Weeks per month factor in the Predictor (52.2/12). The Analyzer's 30-day windows imply 4.29 | Document both |
| Cohort outcomes | Occupancy trajectories of comparable launches nearby, including stalls | "Genuinely-active" definition |
| Expanded support (10 mi) | Comps from a wider radius, shown separately from local | none |
| Amenity ROI | Expected rent/occupancy uplift from an amenity upgrade | Method |
| House rules (recorded local policies) | Common local listing rules ("recorded local policies") used to build an operating checklist | Source: listings or municipal law? |
| CoC / DSCR / Cap rate | Cash-on-cash return / debt-service coverage ratio / capitalization rate | Expense model used |
| ARV | After-repair value | Used for BRRRR-style refinance? |
| Vacancy (calculator) | % income haircut in the Deal Calculator (default 5%) | Double counting with occupancy? |

---

## 5. Entities and data fields seen so far
- **Market**: name, type (city / ZIP / metro), property count, Market Score, grade, confidence badge, occupancy %, trend/mo.
- **Metro group**: name (MSA-style), member cities.
- **Submarket cell**: id, Occupancy Health score, band, evidence level, snapshot date.
- **Property**: id, title (with the listing's own emoji), host display name (first name + initial), city/state, lat/lng, photos, type (house…), bedrooms, bathrooms, total rooms, occupied rooms, available rooms, occupancy %, avg weekly asking, avg move-in fee, review count, price-drop count, status (Listed / Coming soon / Never listed / Delisted), dormant flag, **signal label, recommendation text, evidence level, flagged-room count, tracked-room count, best spread (amount + dimension), metrics-as-of date, lifecycle stage(?)**.
- **Room** *(new)*: id, property id, bathroom type, size class, weekly price, occupancy history, fill events (days to fill), photos, flagged state.
- **Room segment** *(new)*: dimension (bath / size), value, room count, avg weekly, 90d occupancy.
- **Rolling window stat** *(new)*: window (7/30/90d), avg occupancy, avg daily price, volatility, occ Δ, price Δ.
- **Evidence quality** *(new)*: completeness %, history coverage %, media counts, level.
- **Similar-room match** *(new)*: source room/photo, matched room, match %, price/wk, days to fill, location.
- **AI concept** *(new)*: source photo, preset, generated image, watermark, timestamp, (future) economics.
- **Revenue estimate**: amount, window start/end, partial-period flag, method note.
- **Underwrite draft** *(new)*: id, address, lat/lng, autosave timestamp, baseline profile, step state, run count.
- **Baseline profile** *(new)*: property type (e.g., townhouse), bedrooms, bathrooms, sqft, private-bath rooms, room entries, common space, garage (1-car / 2-car), transit distance.
- **Room entry** *(new)*: sellable flag, room sqft, private-bath flag, existing weekly rent (optional).
- **Forecast result** *(new)*: monthly revenue, formula terms (price, rooms, occupancy, 4.35), model path, lookback days, support level, confidence, comp count, median comp distance, scenario low/high, next-step recommendation, caution flags.
- **Comparable** *(new)*: property id, distance, local vs expanded, price, occupancy.
- **Deal scenario** *(new)*: scenario type, room revenue, other income, vacancy, purchase price, ARV, seller concessions, closing costs, financing mode, down payment, interest rate, (expenses), outputs: cash flow, CoC, DSCR, cap rate.
- **Saved underwrite / report** *(new)*: type (property / market), export date, snapshot, re-run diff.
- **User/account**: username, email, avatar, plan (Pro), entitlements (unlimited analyzer).

---

## 6. Monetization and packaging signals
- `RoomIQ Pro` badge → named paid tier.
- `Unlimited analyzer access` → the Analyzer is probably metered on lower tiers (e.g., N analyses per month).
- `Market Report` download → a candidate for gating as a premium or export feature.
- 3-city cap on the dashboard → possibly a tier lever.
- **Media Studio** (generative AI) → has a real compute cost per generation. Natural candidates for **credits / usage metering** or an add-on.
- **Visually Similar Rooms** → a differentiating "wow" feature, a candidate for the paid tier or a teaser.
- `Unlimited baseline runs` → Predictor runs are probably metered on lower tiers.
- `Deal Calculator [Pro]` badge → **Pro-only feature**: the clearest gating line seen so far.
- **My Underwrites** (saved reports, re-run against the market) → a retention and upsell lever (saved-report limits, alerts on market moves).
- **[Q]** Full tier list, prices, limits, trial, annual versus monthly billing, and any AI credit limits.

---

## 7. Third-party and compliance dependencies seen
| Dependency | Where | GTM / legal note |
|---|---|---|
| Leaflet | Map | Open source (BSD-2). Fine. |
| OpenStreetMap data | Map | ODbL attribution required (shown ✔). |
| CARTO basemap tiles | Map | Check the CARTO basemap terms for commercial SaaS use; a paid plan may be needed at scale. |
| FEMA NFHL | Map layer | Public US government data. Add a "not for insurance/regulatory determination" disclaimer. |
| Listing data + photos | Drawer, Analyzer, Similar Rooms | Confirm the rights to show third-party listing photos, titles and host names. **High priority.** |
| **Generative image model** *(new)* | Media Studio | Vendor/model, cost per image, terms of use, and output ownership. Editing third-party listing photos creates **derivative works**, so copyright and platform-terms exposure goes up. **High priority.** |
| **Image-embedding model** *(new)* | Visually Similar Rooms | Vendor or self-hosted; the cost of indexing every room photo; refresh cadence. |
| AI disclosure / watermarking *(new)* | Media Studio | A strong point already (watermark + disclaimer). Keep it in line with FTC deceptive-advertising guidance and listing-platform rules against altered photos. |
| Privacy choices | Sidebar | Good sign for CCPA/CPRA readiness. Confirm the cookie/consent vendor. |
| **Geocoding / address autocomplete** *(new)* | Predictor: Location | Which provider? Free OSM Nominatim forbids autocomplete-style heavy use, and Google requires a Google basemap. Check the terms and cost at scale. |
| **Financial outputs** *(new)* | Deal Calculator | CoC / DSCR / cap rate shown to investors and lenders. Add an "informational, not financial or lending advice" disclaimer. |
| **Local policy data** *(new)* | House Rules | If "recorded local policies" includes municipal rules (rooming-house or occupancy ordinances), state the source and that it is not legal advice. |

---

## 8. Data consistency checks (trust evidence for GTM) *(new)*
These checks **passed** and can be used as proof points in demos:
- ✔ Segment occupancy reconciles to the property: (3×71.5 + 5×57.1)/8 = (1×60.0 + 7×62.9)/8 = **62.5%** = 90d avg occupancy.
- ✔ Best spread: $310 − $238 = **$72**.
- ✔ Similar-room medians: price $244.5 → $245; days to fill (8 + 11)/2 = 9.5.
- ✔ Avg daily price ≈ weekly / 7.
- ✔ Revenue roughly reproducible in screen 06 ($7,800 computed vs. $7,742 shown).

- ✔ Predictor formula: $282 × 1.0 rooms × 89.5% × 4.35 = **$1,097.9** → $1,098.
- ✔ Illustrative scenarios: $1,098 × 0.9 = $988 and × 1.1 = $1,207.

Transparency proof points (batch 3), worth leading with in GTM:
- The formula is printed under the forecast.
- "Fallback support" and "Confidence Low" are labeled openly.
- The median comp distance is disclosed.
- "Not a calibrated prediction interval" is stated outright.
- Local and expanded comps are shown separately.
- Soft signals are excluded from model inputs on purpose.

Still unexplained:
- room-state totals (QA Q3/Q15),
- the revenue in screen 04 (Q13),
- the room count used in the Predictor (Q26).

---

## 9. Pre-launch UX/QA issues spotted
| # | Screen | Issue | Severity (my take) |
|---|---|---|---|
| Q1 | 03 Trends | Helper says "Index 100", but the axis is in % (+5% / 0%). Units are inconsistent. | Medium (trust) |
| Q2 | 03 Trends | Awkward copy: "this country's typical level" | Low |
| Q3 | 04 Drawer | Rooms: 5 occupied + 1 available ≠ 8 total. 2 rooms are unexplained. | Medium (data trust) |
| Q4 | 04 Drawer | Avg room move-in fee of $1 looks like an artifact or default | Medium (data trust) |
| Q5 | 02 Map | The FEMA NFHL row is clipped or hidden behind the Occupancy Score legend card, so the panels overlap | Medium (usability) |
| Q6 | 02 Map | The toggle label is cut to "Submarket sig..." | Low |
| Q7 | 02 Dashboard | The metro chip is cut to "Dallas–Fort Worth Metro..." | Low |
| Q8 | 02 Overview | "Top US markets" shows national results while DFW is selected, which may confuse users about scope | Medium (clarity) |
| Q9 | 02 Overview | The `High` badge and the grade `B` have no visible explanation or tooltip | Low–Medium |
| Q10 | 02 Toolbar | The `Market Report` button looks disabled, with no reason given | Low–Medium |
| Q11 | 02 Map | 80% of cells (163/205) are "Thin", which can make the product look empty in demos | High (GTM/demo) |
| Q12 | Sidebar | The avatar initial in the account card has very low contrast | Low (a11y) |
| Q13 | 04 Drawer | The revenue arithmetic can't be reproduced from the visible KPIs; the method needs explaining | Low–Medium |
| Q14 | 06 / 07 | Pluralization: "1 results", "1 rooms" | Low (polish) |
| Q15 | 06 Snapshot | 7 occupied + 0 available ≠ 8 total. This is the **same pattern as Q3, so it's systemic**: a third room state (unlisted? unknown?) needs a label | Medium (data trust) |
| Q16 | 06 Search | The typo "huston" isn't corrected to Houston, TX. It silently matches listing-title text, with no "Did you mean…" or "matched in title" hint | Medium (usability) |
| Q17 | 08 Similar | The copy says "across the market", but the results span TX + FL (Miami, Zephyrhills). The scope copy doesn't match, and there's no same-market filter | Medium (clarity) |
| Q18 | 08 Similar | 2 of 12 matches are **empty-closet photos** at 95% match. Non-bedroom shots should be filtered out before matching, or comps lose credibility | Medium–High (trust) |
| Q19 | 09 Media Studio | The label `CONCEPT ·` has a trailing separator and an empty value (preset name missing?) | Low |
| Q20 | 07 Windows | Occ Δ unit is ambiguous (relative % vs pp), and Volatility has no unit or tooltip | Medium (trust) |
| Q21 | 07 Windows | 90d Occ Δ / Price Δ show `N/A` with no reason. Explain it (e.g., "needs 180 days of history") or hide it | Low |
| Q22 | 06 Snapshot | `30d occ Δ 51.4%` is shown with no color or context (good or bad?) | Low |
| Q23 | 07 Evidence | `MEDIA 9 + 34` has no label | Low |
| Q24 | 06 Header | A card below the Performance Snapshot is cut off ("O… lif… · Establish…"). Confirm it renders fully | Info |
| Q25 | 13 Baseline | A 3-bed / 2-bath townhouse at **400 sqft** is accepted with no warning. Add sanity checks (sqft per bedroom, baths ≤ beds…) | Medium (data quality) |
| Q26 | 14 Results | **Message contradicts the math:** the banner says the forecast "is based on the full bedroom count (3) with typical rooms", but the formula uses **Active rooms = 1.0**, so the revenue covers one room ($1,098). Three rooms would be about $3,294. Either the copy or the calculation is wrong | **High** (core output correctness) |
| Q27 | 14 Results | Grammar: "Only 1 of 3 bedrooms have" → "has" | Low |
| Q28 | 11 / 14 | NYC address: 0 supply within 3 mi, and the forecast still runs on comps with a **median distance of 82.88 mi**. It is labeled Low confidence (good), but an 83-mile comp set isn't meaningful for Manhattan. Consider a hard floor ("insufficient local coverage") and show the coverage map before the run | **High** (trust/GTM) |
| Q29 | 14 Results | A $282/wk room price for the Upper East Side is implausible, which follows from Q28. A bad first run in an untracked market will put prospects off | High (demo risk) |
| Q30 | 15 Calculator | The `INTEREST RATE` default appears to read **22%**. Verify the default (a typical mortgage rate is roughly 6–8%) | **High if real** (financial correctness) |
| Q31 | 15 Calculator | A 5% `VACANCY` haircut is applied to revenue that already includes 89.5% forecast occupancy, which may **double-count vacancy** | Medium–High (financial correctness) |
| Q32 | 11 IA | The stepper has 4 steps, but the sections number up to 5 (the Deal Calculator is #5, outside the stepper) | Low |
| Q33 | 11–14 Copy | "Baseline" and "Forecast" are used interchangeably (e.g., "Run the baseline to unlock…" next to a "Run Forecast" button; a "Baseline Forecast" card) | Low–Medium (clarity) |
| Q34 | 12 Baseline | Prerequisites are inconsistent: `Recommend amenities` / `Recommend rules` are enabled while `Compare layouts` / `Get rent guidance` are disabled, and the reasons aren't shown on the buttons | Low |
| Q35 | Predictor vs Analyzer | Weeks/month factor: 4.35 (Predictor) vs 30/7 ≈ 4.29 (Analyzer 30-day windows). Document it so cross-module numbers reconcile | Low |
| Q36 | 14 Results | `Active rooms 1.0` is shown with a decimal; it's unclear why a room count would be fractional | Low |

---

## 10. Open questions for the founder (running list)
1. Data source(s), refresh cadence (daily?), history depth, and coverage (how many US markets / properties / rooms / photos in total).
2. Is the 3-city cap plan-based? Does a metro group count as 1?
3. Market Score: inputs, weights, grade bands, and what `High` means.
4. Leaderboard scope: national on purpose?
5. Occupancy Score band thresholds and the evidence-adjustment method.
6. Other options in Color by / Size by / Signal / date presets / history window.
7. What's in Forecasts and in Property Predictor (model, horizon, accuracy/backtest)?
8. Market Report format and contents, and whether it is gated.
9. Plan tiers, pricing, limits, trial, and AI credits.
10. Target ICP(s) and current customers or pilots, if any.
11. Rights to show listing photos and host names, and to **generate AI edits of them**.
12. Is anything outside the US planned (the copy says "this country's")?
13. *(new)* The full set of **Property Signal** labels (beyond `Useful benchmark`) and their logic.
14. *(new)* Room segment taxonomy: which dimensions and values exist (bath, size, …?), and are they from listing fields or CV/NLP extraction?
15. *(new)* Visually Similar Rooms: which model, the index size, whether results can be limited to the same market, and the match threshold.
16. *(new)* Media Studio: which model or vendor, cost per generation, usage limits, and the list of presets. Is custom prompting planned? Is there an ROI-per-upgrade roadmap?
17. *(new)* What do the `Trends` and `Rooms` tabs in the Analyzer contain?
18. What is the cut-off card below the Performance Snapshot (lifecycle stage)?
19. *(new)* Predictor: how does the tracked-history model differ from the bounded underwriting path? Has either been **backtested** (MAPE, calibration)? That proof is key for investor and lender GTM.
20. *(new)* What are the fallback rules: radius steps, the maximum comp distance, and the minimum comps? Should the Predictor refuse or soft-block in uncovered metros (e.g., NYC)?
21. *(new)* What are the Confidence levels and criteria (Low / Medium / High?)?
22. *(new)* What do the outputs of Compare layouts, Recommend amenities, Recommend rules, Get rent guidance and Cohort outcomes look like? Are they LLM-generated, rules-based or statistical?
23. *(new)* Deal Calculator: the expense model (utilities, furnishing, management, platform fees, taxes, insurance, capex), the loan term and amortization, what "Set price" does (AVM?), and whether the 22% interest-rate default is real.
24. *(new)* My Underwrites: what gets saved, export formats (PDF?), limits per plan, and whether market-move alerts are planned.
25. *(new)* Which conversion scenarios are supported besides the garage (basement, den, attic)?
26. *(new)* Which property types are in the dropdown (house, townhouse, condo, multifamily…)?
