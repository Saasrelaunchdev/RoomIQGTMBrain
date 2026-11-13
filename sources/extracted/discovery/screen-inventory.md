# RoomIQ: Screen Inventory (raw capture)

What this file is: a screen-by-screen record of everything visible in the screenshots, kept as observation and not yet turned into a PRD. Copy is transcribed word for word wherever it matters. Inferences are labeled **[Inferred]**. Questions for the founder are labeled **[Q]**.

Status: **Batches 1–3 received (screens 01–15).** Synthesis into the GTM brief/PRD is **on hold** until all screenshots are in.

---

## Global shell (seen on every screen)

### Left sidebar (dark navy)
| Element | Detail |
|---|---|
| Logo | `ROOMIQ` wordmark in white, spaced caps. The final "Q" is stylized and heavier. |
| Theme toggle | Moon icon beside the logo. **[Inferred]** Light/dark mode switch. |
| Section `ANALYTICS` | `Dashboard` (grid icon), `Property Analyzer` (magnifier icon) |
| Section `PREDICTOR` | `Property Predictor` (sparkle icon). **[Inferred]** The sparkle suggests an AI/ML-powered feature. |
| Active state | Filled pill in a lighter navy behind the active nav item |
| Footer | `Privacy choices` link. **[Inferred]** Consent and "Do not sell/share" controls for US state privacy laws (CCPA/CPRA etc.). |
| Account card | Avatar (initial), username, email (truncated), and a kebab menu `⋮`. **[Inferred]** The menu holds account, billing and sign-out. |

### Top bar
| Element | Detail |
|---|---|
| Sidebar collapse | Panel-toggle icon at top left. The sidebar can collapse. |
| Plan badge | `✓ RoomIQ Pro` with a green check, top right. Shows the current subscription tier. **[Inferred]** There are at least two tiers, so a free or lower tier probably exists. |
| Avatar | Circle with an `A` initial, top right. |

### Visual language
- Palette: deep navy (sidebar, headings, primary buttons), cyan/teal eyebrow labels (`CHOOSE MARKETS`, `PROPERTY ANALYZER`), very light blue-grey canvas, white cards with soft shadows and large radii.
- Typography: a clean grotesk (Inter-like). Spaced-caps eyebrows sit above bold navy H1s.
- Components: pill chips, segmented tabs, score rings, colored status dots, KPI tiles, a stepper, toggles and dropdowns.
- Layout: desktop-first with a two-pane dashboard (analytics on the left, map on the right). The property detail opens in a narrow drawer or sheet.

---

## 01: Dashboard, empty state / market picker
File: `screenshots/batch-01/01-dashboard-empty-market-picker.webp`
Route context: `Dashboard` active, before any market is chosen.

**Copy (word for word)**
- Eyebrow: `CHOOSE MARKETS`
- H1: `Pick your dashboard cities first`
- Sub: `Choose up to 3 cities anywhere in the US, or a metro group, to load your dashboard.`
- Search placeholder: `Search any US city or ZIP...`

**Preset metro chips (7)**
1. Dallas–Fort Worth Metroplex
2. Orlando–Kissimmee–Sanford Metro
3. Houston–The Woodlands–Sugar Land Metro
4. Phoenix–Mesa–Chandler Metro
5. Atlanta Metro
6. Las Vegas–Henderson Metro
7. Jacksonville Metro

**Capabilities observed**
- The dashboard is **gated on market selection**. Nothing loads until a market is chosen.
- Selection can be a **city, a ZIP, or a predefined metro group** (a group of cities).
- Limit: **up to 3 cities** per dashboard. **[Q]** Is the 3-city cap tied to the plan (Pro vs. a lower tier) or the same for everyone? Does a metro group count as 1?
- Coverage is pitched nationally ("anywhere in the US").

**[Inferred]**
- All 7 featured metros are in the Sun Belt (TX ×2, FL ×2, AZ, GA, NV). They are probably where data density is highest and where the ICP is concentrated.
- Metro names follow US Census MSA naming (e.g. "Houston–The Woodlands–Sugar Land"), so the metro groups are probably built on CBSA/MSA definitions.

---

## 02: Dashboard, DFW Metroplex loaded, Overview tab + Explore map
File: `screenshots/batch-01/02-dashboard-dfw-overview-map.webp`

### Left pane: market analytics
**Header**
- H1: `Dallas–Fort Worth Metroplex`
- Date range: `Nov 11, 2025 → Nov 10, 2026`, a trailing 365 days ending today (today = 2026-11-10).

**Toolbar buttons**
| Button | Icon | Notes |
|---|---|---|
| `Views` | Bookmark | **[Inferred]** Saved views or presets of the market + filter + map state. |
| `Last 365d` | Calendar | Date-range preset picker. **[Q]** What are the other presets (30/90/180d, custom)? |
| `Filters` | Funnel | Filter panel. The map legend mentions "Advanced filters" (including a "dormant properties" option). |
| `Market Report` | Download | Downloadable report for the market. It looks **greyed or disabled** in this capture. **[Q]** Is it disabled, still loading, or gated? What format (PDF?)? |

**Market selection**
- Search: `Search any US city or ZIP...` with a clear `✕`
- Selected chip: purple `METRO` tag + `Dallas–Fort Worth Metro...` (truncated) + `✕`
- `Clear all` link

**Tabs:** `Overview (412)` · `Trends` · `Forecasts`
- `(412)` is **412 properties** in the selected market.

**Panel: `🏆 Top US markets` by Market Score** (collapsible chevron)

| Rank | Market | Score | Grade | Badge | Occupancy | Trend | Properties |
|---|---|---|---|---|---|---|---|
| 1 | Richmond, VA | 78 / 100 | B | High | 85.8% occ | ↘ −0.5%/mo | 61 props |
| 2 | Tampa, FL | 75 / 100 | B | High | 81.2% occ | ↘ −0.6%/mo | 343 props |
| 3 | Fort Worth, TX | 74 / 100 | B | High | 78.5% occ | ↗ +0.2%/mo | 88 props |
| 4 | Mesa, AZ | 74 / 100 | B | High | 78.3% occ | ↗ +0.4%/mo | 72 props |
| … | (list keeps going below the fold) | | | | | | |

- Each score is drawn as a ring gauge colored green.
- **[Inferred]** **Market Score** is a 0–100 composite (occupancy is clearly an input; trend and depth may be too). The **letter grade** (B) is a banded version of the score.
- **[Q]** Does the `High` badge mean confidence/data sufficiency or demand level? It needs a tooltip.
- **[Q]** Is the leaderboard national? Richmond and Tampa sit outside DFW, so it looks like a cross-market ranking shown while DFW is selected. Is that intended, as a discovery hook?
- Trend is shown as **percentage-point change per month** in occupancy.

### Right pane: `Explore map`
- Title: `Explore map`. Sub: `Submarket signals and property-level evidence`
- Buttons: `⌖ Reset view`, expand/fullscreen `⤢`, zoom `+` / `−`, and a map search (magnifier in the top bar of the map).
- Basemap: **Leaflet** + **OpenStreetMap** + **CARTO** (from the attribution line).
- Markers: **clustered** circles with counts (8, 18, 12, 4, 4, 14, 25, 54, 45, 12, 4…) plus single light-blue property dots.
- Overlay: dotted **hexagonal cells** around the clusters. **[Inferred]** An H3-style hex grid used for "submarket" cells.
- Visible places: Frisco, McKinney, Plano, Prosper, Melissa, Anna, Howe, Whitesboro, The Colony, Wylie, Farmersville, Fate, Heath, Rockwall, Seagoville, Lancaster, Red Oak, Kaufman. This is the north and east DFW suburbs.

**Map Layers panel: `MAP LAYERS / Display`** (collapsible)
| Control | Current value | Notes |
|---|---|---|
| `COLOR BY` | `Occupancy` (dropdown) | **[Q]** What are the other options (price, fill speed, status…)? |
| `SIZE BY` | `Total rooms` (dropdown) | Marker size encodes how many rooms a property has. |
| `MARKET STATUS` legend | ● Listed (blue) · ● Coming soon (orange) · ● Never listed (grey) · ● Delisted (red) | Property lifecycle states. |
| Helper text | `Dormant properties are shown dimmed when enabled in Advanced filters. Market metrics only count live listings.` | Metrics count **live listings only**. Dormant properties are opt-in. |
| Toggle `Submarket sig...` (truncated: "Submarket signals") ⓘ | **ON** | Turns the hex-cell signal layer on or off. |
| `SIGNAL` | `Occupancy Health` (dropdown) | `Demand signal based on observed occupied rooms in the selected market.` **[Q]** What other signals are there? |
| Toggle `FEMA NFHL` ⓘ | OFF | **FEMA National Flood Hazard Layer** overlay for flood-risk due diligence. |

**Legend card: `OCCUPANCY SCORE`** (dated `2026-11-10 ⌄`, a snapshot-date selector)
| Band | Cells |
|---|---|
| ● Strong (green) | 2 |
| ● Watch (amber) | 29 |
| ● Weak (red) | 11 |
| ● Thin (grey) | 163 |
| **Total** | **205** |
- Copy: `Demand signal based on observed occupied rooms in the selected market.`
- Footer: `ⓘ 205 cells · evidence-adjusted · tap a band to filter`
- The bands are **interactive filters**. Scores are **evidence-adjusted**, meaning they are shrunk for low sample size.
- **[Inferred]** `Thin` means too little evidence. 163/205 cells (~80%) are Thin in DFW, so the data is sparse at cell level. This matters for how claims are worded in GTM.
- The snapshot date selector suggests **daily snapshots** and time travel through history.

---

## 03: Dashboard, DFW Metroplex, Trends tab (Seasonality)
File: `screenshots/batch-01/03-dashboard-dfw-trends-seasonality.webp`
The shell, toolbar, selection and map are the same as in 02. `Trends` is the active tab.

**Card: `Seasonality`**
- Badge: amber `National pattern`
- Toggle: `Occupancy` (selected) | `Fill speed`
- Sub: `US national seasonal pattern`
- Helper: `Index 100 = this country's typical level. Higher = stronger.`
- Chart: line chart with a Y axis labeled `+5%` and `0%`. The curve:
  - starts below 0% at the left (early in the period), climbs steeply to a peak of about +4%,
  - holds a plateau around +3.5–4% with a small dip,
  - falls through the middle of the period to around 0 and then slightly below,
  - ends at about −1% on the right.
  - X-axis labels are below the fold. **[Q]** Is the X axis month of year?

**Capabilities observed**
- **Seasonality analysis** for two metrics: **Occupancy** and **Fill speed**.
- **Fallback logic:** when local data is too thin, the US national pattern is used and flagged with a badge. **[Inferred]** A market-specific pattern shows once there is enough history.
- `Fill speed`: **[Inferred]** how quickly vacant rooms get re-leased (days to fill, or velocity).
- "this country's" hints that the architecture is **ready for more than one country**.

**[Q] Copy and axis mismatch:** the helper says "Index 100", but the axis is in % (+5% / 0%). One of them should change.

---

## 04: Property detail drawer
File: `screenshots/batch-01/04-property-detail-drawer.webp`
This is a narrow drawer sliding over the dashboard. The dimmed map-layers panel and map are visible behind it on the left.

**Header**
- Eyebrow: `PROPERTY DETAIL`. Building icon tile.
- Title: `🥇Newly renovated🥇 Comfortable Mesqu...` (listing title, truncated, with the listing's own emoji)
- Subline: host first name + last initial · `Mesquite, TX`

**Media**
- Hero photo of the listing (kitchen). **[Inferred]** The listing's own photos are ingested.

**Attribute chips:** `house` · `8 BR` · `2 BA`

**KPI tiles**
| Tile label (word for word) | Value |
|---|---|
| `OCCUPANCY` | 62.5% |
| `AVG WEEKLY ASKING` | $178 |
| `AVG ROOM MOVE-IN FEE` | $1 |
| `ROOMS OCCUPIED / TOTAL` | 5 / 8 |
| `AVAILABLE ROOMS` | 1 |
| `REVIEWS · PRICE DROPS` | 0 reviews · 0 drops |

**Revenue block**
- `Estimated rental revenue`
- **$4,370**
- `Partial period total`
- `2026-10-11 – 2026-11-09` (a 30-day window)
- `Based on observed rents and occupancy, not collected payments.` This is a deliberate disclaimer that the figure is an estimate.

**CTAs**
- Primary: `Forecast Stabilized Revenue ↗` (navy). **[Inferred]** Hands off to the **Property Predictor**.
- Secondary: `Analyzer`. Opens this property in the **Property Analyzer**.

**Data model clues**
- Pricing is **per room, per week**, and there is a **per-room move-in fee**. This is the economics of rent-by-the-room / co-living.
- Inventory is tracked **room by room** (occupied, available, total).
- **Price-drop tracking** and a **review count** come from the listing.
- Host identity is shown (first name + last initial).

**[Q] Data checks before launch**
- 5 occupied + 1 available = 6, but there are 8 rooms in total. What state are the other 2 rooms in (unknown, off-market, unlisted)? Showing that would avoid confusion.
- `AVG ROOM MOVE-IN FEE` $1 needs checking. It could be a real promo or a data artifact or default.
- Arithmetic check on the revenue: $178 × 5 rooms × 30/7 weeks ≈ $3,814, but the screen shows $4,370. The rates of occupied rooms probably differ from the average asking price. Worth documenting the formula.
- "Partial period": does that mean the property was only observed for part of the selected range, or is it always the last 30 days?

---

## 05: Property Analyzer, empty state
File: `screenshots/batch-01/05-property-analyzer-empty.webp`
Route context: `Property Analyzer` active.

**Header card**
- Eyebrow: `PROPERTY ANALYZER`
- H1: `Deep property intelligence`
- Sub: `Snapshot KPIs, rolling windows, room-level history, and data quality coverage.`
- Badge (green, top right): `Unlimited analyzer access`. **[Inferred]** This is a plan entitlement on Pro, which implies **metered or limited analyzer use on lower tiers**.

**Search row**
- Label: `Search by city or property ID`
- Input placeholder: `Enter a city (Atlanta, GA) or property ID`
- `History window` dropdown: `90 days` (sliders icon). **[Q]** What are the other options?
- `Search` button (muted lavender, disabled until there is input).

**Stepper (3 steps):** `Search` (active) → `Pick property` → `Analyze`

**Empty state**
- Magnifier icon tile
- H2: `Search a city or enter a property ID`
- Body: `Use a market like Dallas, TX to browse properties, or paste a property ID to open its analyzer directly.`
- Quick chips: `Atlanta, GA` · `Dallas, TX` · `Houston, TX` · `Phoenix, AZ` · `Tampa, FL`

**Capabilities promised by the copy (screens not yet seen)**
- Snapshot KPIs
- Rolling windows (time-windowed metrics)
- Room-level history
- Data quality coverage (how complete the observations are)
- Two entry paths: browse by city, or deep-link by property ID

---

## 06: Property Analyzer, Analyze step: property list + Property Signal + Performance Snapshot
File: `screenshots/batch-02/06-analyzer-property-signal-overview.webp`
Route context: `Property Analyzer` active. The stepper shows `Search ✓` and `Pick property ✓` (green checks), with `Analyze` active (navy).

**Search row (state)**
- The input holds `huston` with a clear `✕`. History window = `90 days`. `Search` is now **enabled** (solid navy).
- Behavior: the typo "huston" was **not** corrected to Houston, TX. It returned the one property whose **listing title** contains "Huston-Tillotson" (a university in Austin). **[Inferred]** Search matches free text in listing titles as well as city names. **[Q]** Is that intended? Is there fuzzy matching or "Did you mean Houston, TX?"

**Left pane: `Properties`**
- `1 results` (grammar; see QA)
- Selected result card (navy border):
  - Title: `🏚️ Modern Co-Living near Huston-Tillotson University & East Austin Transit Hubs 🚀`
  - `Host: Justin G`
  - `Austin, TX`
  - `8 bd · house`
- Footer: `Showing 1 of 1 matching properties`

**Right pane: `PROPERTY SIGNAL` header card**
- Title (same listing) + `Austin, TX · 8 bedrooms · house` + `Host: Justin G`
- Chips: `Metrics as of Nov 10, 2026` · `Useful benchmark`
- Recommendation callout (mint background, green left rule):
  - `Use this as a benchmark read`
  - `Treat the strongest room segment as the clearest benchmark for how this property earns its premium.`
- 2×2 signal tiles:

| Tile | Value | Sub-label |
|---|---|---|
| `SIGNAL` | **Useful benchmark** | none |
| `EVIDENCE` | **High** | `Coverage-based` |
| `FLAGGED ROOMS` | **0** | `8 tracked` |
| `BEST SPREAD` | **$72** | `Bathroom premium` |

- **[Inferred]** The **Property Signal** is a classification that sorts each property into an action-oriented label (`Useful benchmark` here) and pairs it with a plain-language recommendation. **[Q]** What is the full set of signal labels and the rules behind each?
- **[Inferred]** `Flagged rooms` = rooms with anomalies (stale, suspicious pricing, data gaps). **[Q]** What triggers a flag?
- `Best spread` = the biggest price gap between room segments. It is confirmed in screen 07: Private Bath $310 − Shared Bath $238 = **$72** ✔.

**Analyzer tabs:** `Overview` (active) · `Trends` · `Rooms`

**Card: `Performance Snapshot`**
- Sub: `Compact property performance view with recent directional deltas.`
- Top-right meta: `30d occ Δ 51.4%`

| Tile | Value | Sub |
|---|---|---|
| `OCCUPANCY` | 87.5% | none |
| `AVG WEEKLY ASKING PRICE` | $260 | none |
| `Estimated rental revenue` | **$7,742** | `Partial period total` · `2026-10-11 – 2026-11-09` · `Based on observed rents and occupancy, not collected payments.` |
| `ROOMS OCCUPIED` | 7/8 | `0 available` |
| `REVIEWS / DROPS` | 0 / 0 | none |

- Revenue check: $260 × 7 rooms × 30/7 weeks = $7,800, close to $7,742 ✔. Here the formula can be reproduced, unlike screen 04.
- Rooms: 7 occupied + 0 available = 7 of 8, so again **1 room is in a third, unlabeled state** (see QA; this confirms the batch-1 pattern).
- Below the fold, the next card is cut off. Its title appears to begin `O… lif… · Establish…`. **[Q]** Possibly an "occupancy lifecycle · Established" stage card. Needs a screenshot.

---

## 07: Property Analyzer, room segments, rolling windows, Evidence Quality
File: `screenshots/batch-02/07-analyzer-room-segments-rolling-windows-evidence.png`
This is the same property as 06, scrolled down.

**Room segmentation card(s)**
- The top segment is cut off: `$310 avg weekly · 71.5% 90d occ`. **[Inferred]** It is **Private Bath**, the counterpart to Shared Bath, probably 3 rooms.
- `Shared Bath`: `5 rooms`: `$238 avg weekly · 57.1% 90d occ`
- `Room size mix`, badge `2 segments`:
  - `Cozy`: `1 rooms`: `$231 avg weekly · 60.0% 90d occ`
  - `Standard`: `7 rooms`: `$270 avg weekly · 62.9% 90d occ`
- **Consistency check ✔:** the room-weighted 90d occupancy reconciles both ways.
  - Bath: (3×71.5 + 5×57.1)/8 = 62.5%
  - Size: (1×60.0 + 7×62.9)/8 = 62.5%
  - Both equal the 90-day average occupancy below.
- **[Inferred]** Rooms are tagged by **bathroom type** (private/shared) and **size class** (Cozy/Standard, maybe more classes in other properties). **[Q]** Where do the tags come from (listing fields or CV/NLP extraction)? Which segment dimensions exist?

**Rolling-window cards (3)**

| Window | Badge | Avg Occupancy | Avg Daily Price | Volatility | Occ Δ | Price Δ |
|---|---|---|---|---|---|---|
| `7 Days` (`7 day signal`) | `7d` | 98.2% | $37 | 4.37 | 5.8% (green) | 0.0% |
| `30 Days` (`30 day signal`) | `30d` | 88.3% | $37 | 11.15 | 51.4% (green) | 0.0% |
| `90 Days` (`90 day signal`) | `90d` | 62.5% | $38 | 22.82 | N/A (blue) | N/A (blue) |

- Avg daily price ≈ weekly / 7 ($260 / 7 = $37.14 ✔).
- The 30d Occ Δ of 51.4% matches the `30d occ Δ 51.4%` header in 06. **[Inferred]** It is a **relative** % change against the previous equal-length window, not percentage points. **[Q]** Confirm.
- 90d deltas show N/A. **[Inferred]** The history window is 90 days, so there is no prior 90-day window to compare against.
- Volatility has no unit. **[Q]** Is it the standard deviation of daily occupancy in pp? Of price?
- Story in the data: occupancy is climbing fast (62.5% → 88.3% → 98.2%) while price stays flat. That reads as a **lease-up / stabilizing** property and fits the "Establish…" lifecycle card in 06.

**Card: `Evidence Quality`**
- Sub: `How much supporting information is available for this property.`
- Badge: `🛡 High`

| Tile | Value |
|---|---|
| `COMPLETENESS` | 100.0% |
| `HISTORY COVERAGE` | 100.0% |
| `MEDIA` | 9 + 34 |

- **[Q]** Does `MEDIA 9 + 34` mean 9 property photos + 34 room photos? It needs a label.
- **[Inferred]** Evidence Quality powers the `EVIDENCE: High (Coverage-based)` tile in 06 and is the property-level counterpart of the "evidence-adjusted" market cells.

---

## 08: Property Analyzer, Visually Similar Rooms
File: `screenshots/batch-02/08-analyzer-visually-similar-rooms.webp`

**Header**
- H: `Visually Similar Rooms`
- Sub: `Rooms across the market that look like this one. Click to open a property.`
- Summary chips: `📷 12 similar rooms` · `median $245/wk` · `median 9.5 days to fill`

**Result grid (12 cards: photo with a `% match` overlay, price, fill-time chip, location)**

| # | Match | Price | Filled in | Chip color | Location |
|---|---|---|---|---|---|
| 1 | 96% | $214/wk | 1 day | green | Austin, TX |
| 2 | 96% | $189/wk | 8 days | grey | DeSoto, TX |
| 3 | 95% | $278/wk | 43 days | yellow | Austin, TX |
| 4 | 95% | $179/wk | 41 days | yellow | DeSoto, TX |
| 5 | 95% | $275/wk | 1 day | green | Miami, FL (photo is an **empty closet**) |
| 6 | 95% | $198/wk | 2 days | green | Austin, TX |
| 7 | 95% | $189/wk | 5 days | green | Austin, TX |
| 8 | 95% | $300/wk | 11 days | grey | Austin, TX |
| 9 | 95% | $289/wk | 33 days | yellow | Houston, TX (photo is an **empty closet**) |
| 10 | 95% | $285/wk | 17 days | grey | Austin, TX |
| 11 | 94% | $179/wk | 4 days | green | Zephyrhills, FL |
| 12 | 94% | $284/wk | 27 days | grey | Austin, TX |

- **Consistency check ✔:** median price = ($214 + $275)/2 = $244.5 → `$245`. Median days to fill = (8 + 11)/2 = `9.5`.
- Fill-time chip colors work out to about **green ≤ 5 days**, **grey 8–27 days** and **yellow ≥ 33 days**. **[Q]** What are the exact thresholds?
- **[Inferred]** This is **image-embedding similarity search** (computer vision) over room photos, used as **visual comps**. It ties look and finish quality to rent and demand (days to fill).
- Scope: the copy says "across the market", but the results span **TX and FL** (Austin, DeSoto, Houston, Miami, Zephyrhills), so the search runs **nationally**. **[Q]** Is that intended? Should there be a same-market filter?
- Quality: 2 of 12 matches are closet-only photos, which aren't meaningful room comps (see QA).
- The cards are **clickable**: they deep-link to that property, which supports cross-property exploration.

---

## 09: Property Analyzer, Media Studio (AI upgrade concept)
File: `screenshots/batch-02/09-analyzer-media-studio-ai-concept.webp`

**Header**
- H: `Media Studio`
- Sub: `Preview an AI concept of an upgrade on a listing photo, side by side with the original.`
- Badge (top right): `✨ AI concept` (magic-wand icon)

**Controls**
- **Photo picker:** a horizontal, scrollable thumbnail strip of the listing's photos (7+ visible: living/kitchen ×5, kitchen, stairs). The first is selected with a navy border.
- **Upgrade preset chips** (single select): `Add desk` (selected) · `Add ceiling fan` · `Repaint neutral` · `LVP flooring` · `Stage empty room`
- **Actions:** `✨ Generate concept` (primary) · `⬇ Download concept` (secondary)

**Output**
- Side by side: `ORIGINAL` | `CONCEPT ·`. A trailing separator follows with no value after it (see QA).
- The concept adds a desk, an office chair and a lamp to the right side of the living area. The room's geometry, fan, wall pattern and kitchen are kept, so this is an **edit/in-painting** model, not a full re-render.
- The concept image has a burned-in banner: `RoomIQ CONCEPT  AI-GENERATED - NOT ACTUAL PROPERTY CONDITION`
- Disclaimer callout (yellow): `AI-generated concept for visualization only — this image does not depict the actual current condition of the property.`
- Footer note: `Concept visualization — no validated economics for this edit yet.`
  - **[Inferred]** **Roadmap hint:** they plan to attach ROI/economics to each upgrade (e.g., "adding a desk lifts rent by $X/wk, based on similar rooms").

**Next section (cut off): `Property Photos`**
- Sub (partly legible): `Reference imagery for context and merchandising review, kept below the operating signal.`
- A badge at the top right appears to be a camera icon + count. **[Q]** Needs a screenshot.
- **[Inferred]** It is a deliberate design choice to put photos *below* the operating data, so the product stays data-first rather than looking like a listing site.

---

## 10: Media Studio, downloaded concept output
File: `screenshots/batch-02/10-media-studio-concept-output-watermarked.webp` (1195×896)

- This is the full-resolution **downloaded** concept (the "Add desk" edit on the living-room photo).
- Watermarking is **layered**:
  1. a tiled diagonal semi-transparent `AI CONCEPT` watermark across the whole image, and
  2. a solid bottom bar: `RoomIQ CONCEPT  AI-GENERATED - NOT ACTUAL PROPERTY CONDITION`.
- **[Inferred]** The watermark is burned into the exported file. This guards against using AI-enhanced photos as real listing photos, which helps with misrepresentation, advertising and platform-policy risk.
- Edit quality: the desk, office chair and lamp blend in with believable lighting and perspective, and the original furniture is preserved. The output is good enough to sell as a feature.

---

## 11: Property Predictor, Step 1 Location + Nearby coliving supply
File: `screenshots/batch-03/11-predictor-step1-location-nearby-supply.webp`
Route context: `Property Predictor` active (sparkle icon).

**Page header**
- Eyebrow: `PROPERTY PREDICTOR`
- H1: `Underwrite a property`
- Sub: `Room mix, structural details, and local market context.`

**Card: `Baseline Forecast`**
- Chips: `Unlimited baseline runs` (entitlement) · `Draft saved Just now` (green). The draft **autosaves**.
- Actions: reset icon (circular arrow, maybe undo or reload) · `Start fresh`

**Stepper (4 steps):** `Location` ✓ (green) → `Baseline` (house) → `Forecast` (sliders) → `Results` (chart)

**Accordion section 1: `Location`** (✓, expanded)
- Summary line: `515 East 70th Street, New York City, New York 10021, United States`
- `Choose property location`: `Type the address, or drop a pin on the map below.`
- Address search input (geocoded, full formatted address)
- Sub-card `Nearby coliving supply` ⓘ, top right: `0 active properties within ~3 mi`
  - Map (Leaflet / OSM / CARTO) of the Upper East Side of Manhattan (Lenox Hill, St. Catherine's Park, FDR Drive, East River, Roosevelt Island, Ravenswood in Queens) with a draggable pin and zoom `+`/`−`
  - `No active properties found within ~3 mi of this address.`
  - `Drag the pin to move the property location.`
- CTA: `Continue to Baseline`

**Remaining accordion (collapsed / locked)**
- `2` `Baseline Profile`: `Property type and bedrooms are required to continue.`
- `3` `Run Forecast` 🔒: `Choose the property type to anchor the baseline.`
- `4` `Decision Board` 🔒: `Run the baseline to unlock the decision board.`

**Card `5` `Deal Calculator` [`Pro`]**
- `Convert the Predictor revenue estimate into acquisition cash flow, CoC, DSCR, and cap-rate outputs.`

**Card `📄 My Underwrites`** (refresh icon)
- `Re-run a saved report to see how the market moved since you exported it.`
- Empty: `No saved underwrites yet. Export a property or market report and it'll appear here.`

**Observations**
- The Predictor works on **any US address**, including addresses RoomIQ doesn't track, via geocoding plus a pin. This is the path for underwriting *new* deals.
- **Coverage gap shown:** Manhattan UES has **0 active co-living properties within ~3 mi**. This feeds straight into the fallback forecast in screen 14.
- Exporting a property or market report saves an "underwrite" that can be **re-run later** to see how the market moved since export. **[Inferred]** This is a monitoring and retention loop.

---

## 12: Property Predictor, Step 2 Baseline Profile (full page)
File: `screenshots/batch-03/12-predictor-step2-baseline-profile-full-page.webp` (full-page capture, low-res; read by zooming)
The stepper shows `Location` ✓ with `Baseline` active. The Location section is collapsed to its address summary.

**Section `2` `Baseline Profile`**: `Property type and bedrooms are required to continue.`

Each sub-card has an eyebrow showing **input priority**: `REQUIRED FIRST`, `INVESTOR DETAIL`, `COMPARE ROOM UPGRADES`, `RECOMMENDED`, `ROOM-LEVEL DETAIL`, `PHYSICAL CONTEXT`.

**A. `REQUIRED FIRST`: `Core Specifications`**
- `Property facts that investors actually underwrite: type, bedroom count, bathroom count, and gross size.`

| Field | Tag | Helper / validation copy |
|---|---|---|
| `Property Type` (dropdown `Select type`) | `Required` (red error state) | `Choose the property type to anchor the baseline.` |
| `Bedrooms / rentable rooms` | `Required` (red error state) | `Enter the bedroom count so the room mix can be checked properly.` |
| `Total bathrooms` | `Recommended` (amber) | `Add bathrooms to make the baseline more comparable-driven.` |
| `Property square feet` | `Recommended` (amber) | `Add property square footage when known; it helps separate small dense conversions from larger co-living homes.` |

**B. `INVESTOR DETAIL`: `Bathroom Mix`**
- `Private-bath supply and shared-bath pressure are structural revenue drivers, so they stay first-class.`
- Tiles: `Active rooms` `-` · `Private-bath rooms` (input, `0`) · `Shared-bath pressure` `-` (`shared rooms per shared bath`)
- Buttons: `Use bedrooms as rooms` (ghost) · `+ Add room` (navy)
- Sub-card ✨ `Bedroom mix recommendation`: `Compare your room mix using your property details and nearby room evidence. No extra inputs needed.` / `Choose an address and add bedrooms to unlock a recommendation.` Button `✨ Compare layouts` (disabled).

**C. `COMPARE ROOM UPGRADES`: `Amenity ROI`**
- `Find upgrades worth checking using your property details and nearby room evidence.`
- Sub-card `Amenity ROI recommendation`: `Get an automatic shortlist. No upgrade quote or extra inputs needed.` Button `Recommend amenities` (enabled).

**D. `RECOMMENDED`: `House Rules for this Area`**
- `Build a practical operating checklist, with local listing patterns available as supporting context.`
- Sub-card `House-rule recommendation`: `Get a practical operating checklist, then compare it with recorded local policies.` Button `Recommend rules` (enabled).

**E. `RECOMMENDED`: `Room Pricing`**
- `Find a starting weekly rent for an unpriced room, or compare an existing rent with supported nearby rooms.`
- Sub-card `Per-room price optimizer`:
  - `Add rooms and confirm their bath types. Existing weekly rents are optional; supported comps provide a starting guide.`
  - `Add at least one active room and confirm its bath type for starting-rent guidance.`
  - ☑ (checked) `Expand sparse comparable searches up to 10 miles. Results show local and expanded support separately.`
  - Button `Get rent guidance` (disabled)

**F. `Cohort outcomes`** (pulse icon), button `Load`
- `How comparable market launches filled listed rooms, including occupancy stalls — not business failures or delistings.`
- `Loads the listed-room occupancy trajectory of comparable genuinely-active launches nearby.`
- **[Inferred]** Shows **lease-up curves** for comparable new listings: how fast similar launches nearby filled up.

**G. `ROOM-LEVEL DETAIL`: `Room Mix`**
- `Add sellable rooms, room square footage, and private-bath status. These are the room details investors can verify and underwrite.`
- Empty: `No room mix added yet`: `The forecast can still run, but room count and private-bath mix are strongly recommended for investor-grade scenarios.`

**H. `PHYSICAL CONTEXT`: `Access & Common Areas`**
- `Only stable, physical inputs remain here. Listing copy, operator behavior, and other soft signals are intentionally excluded from the controls.`
- Toggles: `Common space available` (`Shared living, dining, or other usable common space.`) · `Garage parking` (`A physical garage space is part of the property.`)
- Input: `Distance to nearest public transit (miles)`

**Footer:** `Fix 2 blockers before moving on.` + `Continue to Run Forecast` (disabled lavender)
After that: `3 Run Forecast` 🔒, `4 Decision Board` 🔒, `5 Deal Calculator [Pro]`, `My Underwrites` (same as 11).

**Observations**
- There is a clear **input-quality hierarchy** (Required → Recommended → Investor detail). The forecast can run on the minimum inputs, but the UI keeps nudging toward "investor-grade" detail.
- **Four AI/recommendation helpers sit inside the form:** Bedroom mix (Compare layouts), Amenity ROI, House rules, and the Per-room price optimizer. Cohort outcomes is a fifth evidence tool.
- A stated modeling principle: **only physical, verifiable inputs**. Soft signals (listing copy, operator behavior) are excluded on purpose. That's a strong credibility message for investors and lenders.

---

## 13: Property Predictor, Step 3 Run Forecast (Model Routing + Market Evidence)
File: `screenshots/batch-03/13-predictor-step3-run-forecast-model-routing.webp`

**Baseline summary (above, completed ✓):** `Type: townhouse • Beds: 3 • Baths: 2 • 400 sqft • 1 room`
- 400 sqft for a 3-bed, 2-bath townhouse is unrealistic, and no sanity warning appears (see QA).

**Section `3` `Run Forecast`**: `Automatic model routing • 270 day lookback • Ready to run`

**Card `Model Routing`**, badge `Automatic`
- `RoomIQ automatically uses tracked history when available. New manual forecasts stay on the bounded underwriting path, with structural details applied as conservative adjustments.`
- **[Inferred]** There are **two model paths**:
  1. a **tracked-history** model for properties RoomIQ already observes, and
  2. a **bounded underwriting** (comp-based) model for new manual entries, with capped, conservative structural adjustments.

**Card `Market Evidence`**, badge `History`
- `Sets the evidence window used for market priors and comparable support. Changing it can compare against a different cohort.`
- Slider `Evidence lookback`: **270 days**, from `Recent signal` (left) to `Seasonal depth` (right). The knob sits at about 72% of the track. **[Q]** Range 30–365d?
- `This changes the evidence set, not the property itself. Use it to test how stable the forecast is across recent versus deeper market history.`
- **[Inferred]** A built-in **sensitivity / robustness test** for the forecast.

**CTA:** `Run Forecast` (large gradient pill, navy → cyan)
Below: `4 Decision Board` 🔒: `Run the baseline to unlock the decision board.`

---

## 14: Property Predictor, forecast results (Decision Board)
File: `screenshots/batch-03/14-predictor-results-forecast-fallback.webp`
This is the output for the 515 E 70th St (NYC) townhouse: 3 bd / 2 ba / 400 sqft / 1 room entry.

**Warning banner (amber, shield icon):** `Incomplete room mix`: `Only 1 of 3 bedrooms have a room entry, so the forecast is based on the full bedroom count with typical rooms.`

**Chips:** `Fallback support` (red/pink) · `Confidence Low`

**Headline**
- Eyebrow: `MONTHLY REVENUE`
- **`$1,098 /mo`**
- Formula shown: `Price x rooms x occupancy x 4.35 weeks = $1,098`
  - Check ✔: $282 × 1.0 × 0.895 × 4.35 = **$1,097.9**
- `This estimate found 10 comparables, but the local evidence was sparse enough that RoomIQ used fallback market support.`

**Three insight cards**
| Card | Value | Copy |
|---|---|---|
| `Illustrative scenarios` | **$988 - $1,207** | `Revenue assumptions, not a calibrated prediction interval. Edit them in the calculator.` (= −10% / +10% of $1,098 ✔) |
| `Forecast support` | **10 comps, fallback support** | `Broader fallback evidence was used; median comp distance is 82.88 mi.` |
| `Best next step` | **Incomplete room mix** | `Only 1 of 3 bedrooms have a room entry, so the forecast is based on the full bedroom count with typical rooms.` |

**KPI tiles:** `Weekly room price` **$282** · `Occupancy` **89.5%** · `Active rooms` **1.0** · `Revenue per room` **$1,098**

**`Support details`**: `Comparable properties and key caution flags.` Badge `10 comps`, expandable ⌄.

**`Garage conversion`** (building icon)
- `Keep the garage as parking, or convert it into bedrooms? RoomIQ re-runs the forecast both ways.`
- Segmented `1-car` | **`2-car`** (selected) + `Compare` button
- **[Inferred]** A **conversion scenario engine** that models adding bedrooms in a garage. Other conversion types (basement, den) may exist.

**Observations**
- It is very transparent: the formula is spelled out, the evidence level is labeled, the confidence is labeled, the comp distance is disclosed, and it says outright "not a calibrated prediction interval". Strong for investor and lender trust.
- **Contradiction (see QA):** the banner says the forecast uses "the full bedroom count (3) with typical rooms", but the math uses **Active rooms = 1.0**, so the revenue covers 1 room. The full count would give about $3,294/mo.
- **Coverage risk:** the comps for a Manhattan address have a median distance of **83 miles**, and a $282/wk room price is implausible for the Upper East Side.

---

## 15: Property Predictor, Step 5 Deal Calculator (Pro)
File: `screenshots/batch-03/15-predictor-deal-calculator.webp`

**Header:** `5` (green) `Deal Calculator` [`Pro`]: `Convert the Predictor revenue estimate into acquisition cash flow, CoC, DSCR, and cap-rate outputs.` (expanded ^)

**Left column: inputs**
- **`Scenario`** ⓘ: `Predicted revenue + RoomIQ default assumptions`. Segmented: `Conservative` · **`Base`** · `Aggressive`.
- **`Income baseline`** ($ icon)
  - `Base revenue uses the predictor estimate. Conservative and aggressive revenues are illustrative assumptions, not confidence bounds; edit the monthly revenue to test your own scenario.`
  - `MONTHLY ROOM REVENUE` `$ 1098` (prefilled from the Predictor)
  - `OTHER MONTHLY INCOME` `$ 0`
  - `VACANCY` ⓘ `5%`: input `5 %` + slider
- **`Purchase`** (house icon)
  - `PURCHASE PRICE` with a `Set price` link: `$` (empty) + slider at 0
  - `AFTER-REPAIR VALUE` ⓘ: `$ Optional`
  - `SELLER CONCESSIONS` ⓘ: `$ 0`
  - `CLOSING COSTS` ⓘ: toggle **`%`** | `$`, value `5 %`
- **`Financing`** (bank icon): toggle **`Financed`** | `Cash`
  - `DOWN PAYMENT` `20%`
  - `INTEREST RATE`: the value appears to read **`22%`** (cut off at the bottom edge; see QA)
  - (more fields below the fold: term, opex and so on, not yet seen)

**Right column: `Deal snapshot`** (calculator icon)
- Empty state (amber): `Add a purchase price to calculate cash flow.`
- **[Inferred]** Once filled, it shows monthly/annual cash flow, cash-on-cash (CoC), DSCR and cap rate.

**Observations**
- This turns RoomIQ from an analytics tool into an **underwriting tool**: market → property → revenue forecast → financed deal returns, all in one flow.
- The revenue is prefilled from the forecast, which ties the Predictor to the calculator.
- **[Q]** Vacancy (5%) is applied on top of revenue that already includes 89.5% occupancy. Is vacancy being double-counted?
- **[Q]** Expense inputs are not yet seen (utilities, management, furnishing, platform fees, insurance, taxes, capex reserve). For co-living, utilities and furnishing are material.

---

## Screens referenced but not yet captured
- `Forecasts` tab (Dashboard)
- `Overview` tab below the Top US markets panel
- Property Predictor: the Decision Board top section (above the banner in 14), the `Support details` expanded comps list, `Garage conversion` Compare output, the outputs of the recommendation helpers (Compare layouts, Recommend amenities, Recommend rules, Get rent guidance, Cohort outcomes), the Room Mix with rooms added, the Deal Calculator below the fold (financing terms, expenses, filled Deal snapshot), the `Property type` dropdown options, and `My Underwrites` with saved items
- Property Analyzer: the `Pick property` step with many results (a city search), the `Trends` and `Rooms` tabs, the card cut off below Performance Snapshot ("O… lif… · Establish…"), the top of the room-segment card (Private Bath), and the `Property Photos` section
- Media Studio: the other presets' outputs, and any generation limits or credits
- `Views`, `Filters` / Advanced filters, `Market Report` output
- Map dropdown options (Color by / Size by / Signal), FEMA NFHL layer on
- Dark mode
- Account menu, billing/plans, sign-up/onboarding, `Privacy choices`
- Mobile layout (beyond the drawer)
