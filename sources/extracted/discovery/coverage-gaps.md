# RoomIQ: Screenshot Coverage Gaps (click checklist)

These are suggestions, not facts. The list has two parts:
- **Part A:** buttons, tabs and links that **are visible in the screenshots but were never opened**. They definitely exist.
- **Part B:** screens that SaaS products like this **usually have**. These are **assumptions**; they may not exist in RoomIQ.

**PRD rule:** the PRD will only use what is visible in the screenshots. Anything inferred stays out of the PRD and goes into a separate "to confirm" list.

Priority: **P1** = needed for an accurate PRD/GTM brief · **P2** = fills in detail · **P3** = nice to have.

---

## Part A: Visible but unopened (confirmed to exist)

### Global shell (every page)
| # | Where to click | What it likely reveals | Pri |
|---|---|---|---|
| A1 | `RoomIQ Pro` badge (top right) | Plan / billing / upgrade page | P1 |
| A2 | Account card `⋮` menu (bottom of the sidebar) | Account, settings, billing, sign out | P1 |
| A3 | Avatar `A` (top right) | Profile menu | P2 |
| A4 | `Privacy choices` (sidebar footer) | Consent / data-sharing controls | P3 |
| A5 | Moon icon beside the logo | Dark mode (one screenshot of any page is enough) | P3 |
| A6 | Sidebar collapse icon (top left) | Collapsed navigation | P3 |

### Dashboard
| # | Where to click | What it likely reveals | Pri |
|---|---|---|---|
| A7 | `Forecasts` tab | The market forecast feature (never seen) | **P1** |
| A8 | `Views` | Saved views: create / list / share | P1 |
| A9 | `Filters` (and "Advanced filters" inside it) | Filter set, dormant-properties toggle | P1 |
| A10 | `Last 365d` | Date-range presets / custom range | P2 |
| A11 | `Market Report` | Whether it is disabled or gated, plus **the exported report itself** (open the file and screenshot each page) | **P1** |
| A12 | `Overview` tab: scroll below `Top US markets` | The rest of the Overview content | P1 |
| A13 | `Trends` tab: scroll below `Seasonality`, then click `Fill speed` | Other trend charts, the fill-speed curve | P2 |
| A14 | A row in `Top US markets` (e.g., Richmond, VA) | Whether it drills into that market | P2 |
| A15 | Search: select **2–3 cities** (not a metro) | The multi-market dashboard / comparison layout | P2 |
| A16 | Map `COLOR BY`, `SIZE BY` and `SIGNAL` dropdowns (open each) | All the map encodings and signals | P2 |
| A17 | Map `FEMA NFHL` toggle on | Flood layer rendering + legend | P2 |
| A18 | `OCCUPANCY SCORE` date `2026-11-10 ⌄` | Snapshot history options | P2 |
| A19 | Tap a legend band (e.g., `Watch`), then click a hex cell and a single property dot | Band filtering, cell popup, marker tooltip | P2 |
| A20 | Map `⤢` (fullscreen) and the map search | Fullscreen map mode | P3 |
| A21 | Property drawer → `Forecast Stabilized Revenue ↗` | **Hand-off into the Predictor: is it prefilled with the tracked property?** | **P1** |
| A22 | Property drawer → `Analyzer`, and scroll inside the drawer | The hand-off + any drawer content below the revenue | P2 |

### Property Analyzer
| # | Where to click | What it likely reveals | Pri |
|---|---|---|---|
| A23 | `Trends` tab (Analyze step) | Property trend charts | **P1** |
| A24 | `Rooms` tab (Analyze step) | Room-level history (promised in the header copy) | **P1** |
| A25 | Search a city (e.g., `Dallas, TX`) → the `Pick property` step | Results list with many properties, sorting/filters | P1 |
| A26 | `History window` dropdown | Window options | P2 |
| A27 | Scroll: the card right **below** `Performance Snapshot` (cut off: "O… lif… · Establish…") | Lifecycle/stage card | P1 |
| A28 | Scroll: the **top** of the room-segment card (above `Shared Bath`) | Card title + Private Bath segment | P2 |
| A29 | Scroll: the `Property Photos` section at the bottom (+ its badge) | Photo gallery | P2 |
| A30 | Look for any **Export / Save / Download** button on the Analyzer page | Property report export (My Underwrites says "Export a property … report") | **P1** |
| A31 | Click a `Visually Similar Rooms` card | Navigation to that property | P3 |
| A32 | Media Studio: another preset (e.g., `Stage empty room`) | A second example output | P3 |
| A33 | Analyze a property with **Flagged rooms > 0** or a **different Signal label** | Other signal states | P2 |

### Property Predictor
| # | Where to click | What it likely reveals | Pri |
|---|---|---|---|
| A34 | **Run the full flow on a well-covered address** (e.g., Austin or Dallas), not NYC | The "good path" result: normal confidence, local comps. Needed for an accurate PRD and for demos | **P1** |
| A35 | Results: scroll **up** above the `Incomplete room mix` banner | Decision Board header/top section | P1 |
| A36 | Results: expand `Support details` (`10 comps`) | Comps list + caution flags | **P1** |
| A37 | Results: `Garage conversion` → `Compare` | Side-by-side conversion output | P1 |
| A38 | Results: scroll below `Garage conversion` | Any further cards or export/save buttons | P1 |
| A39 | `Compare layouts` (Bedroom mix recommendation) | Output | **P1** |
| A40 | `Recommend amenities` (Amenity ROI) | Output | **P1** |
| A41 | `Recommend rules` (House rules) | Output | **P1** |
| A42 | `Get rent guidance` (Per-room price optimizer) | Output | **P1** |
| A43 | `Load` (Cohort outcomes) | Lease-up trajectory chart | **P1** |
| A44 | `+ Add room` and `Use bedrooms as rooms` | Room-entry form | P2 |
| A45 | `Property Type` dropdown (open it) | Supported property types | P2 |
| A46 | Deal Calculator: **enter a purchase price**, then screenshot `Deal snapshot` | Cash flow / CoC / DSCR / cap-rate outputs | **P1** |
| A47 | Deal Calculator: scroll below `Financing` | Interest rate, term, **expenses**, etc. | **P1** |
| A48 | Deal Calculator: `Conservative` / `Aggressive`, `Cash`, `Set price` | Scenario and financing variants | P2 |
| A49 | `My Underwrites` with **one saved item** (after exporting), then refresh / re-run | Saved-report list + the "how the market moved" diff | **P1** |
| A50 | Reset icon / `Start fresh` | Reset confirmation | P3 |

### Tooltips: hover every `ⓘ` icon (P1, cheap and high value)
The tooltip text gives the product's **own definitions** and answers many open questions without guessing:
- Map: `Submarket sig…`, `FEMA NFHL`, the legend footer
- Predictor: `Nearby coliving supply`
- Deal Calculator: `Scenario`, `Vacancy`, `After-repair value`, `Seller concessions`, `Closing costs`
- Also hover the leaderboard `High` badge, the grade `B`, `Volatility` and `Occ Δ`, if they have tooltips.

---

## Part B: Usually present in similar SaaS (assumption, verify)
| # | Screen | Why it matters for the PRD/GTM | Pri |
|---|---|---|---|
| B1 | **Public website / landing page** | Current positioning, claims, messaging | **P1** |
| B2 | **Pricing / plans page** + the **upgrade / paywall modal** a non-Pro user sees (e.g., on the Deal Calculator) | Packaging and the tier boundaries the GTM depends on | **P1** |
| B3 | **Sign-up / log-in / onboarding** (first-run flow) | Activation path; whether "Pick your dashboard cities first" is the onboarding | P1 |
| B4 | **Free / lower-tier experience** (usage limits, "X analyses left") | Confirms metering ("Unlimited analyzer access" implies limits elsewhere) | P1 |
| B5 | **Billing / subscription management** (invoices, cancel) | Billing ops | P2 |
| B6 | **Account settings / profile** | Standard | P2 |
| B7 | **Methodology / data sources / FAQ page** | Trust and credibility; data provenance | P1 (if it exists) |
| B8 | **Terms of Service / Privacy Policy** | Legal readiness | P2 |
| B9 | **Notifications / alerts / email digests** | Retention ("see how the market moved") | P2 |
| B10 | **Team / workspace / seats / invites** | B2B packaging | P2 |
| B11 | **Help / support / contact / feedback** | Support model | P3 |
| B12 | **Error & limit states** (no-coverage market, quota reached, 404) | Edge-case handling | P3 |
| B13 | **Mobile layout** (one or two pages on a phone) | Responsive support | P3 |
| B14 | **Transactional emails** (welcome, report ready) | Lifecycle messaging | P3 |
