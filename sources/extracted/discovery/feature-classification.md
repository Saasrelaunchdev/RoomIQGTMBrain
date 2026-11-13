# RoomIQ: Features vs. Other Product Elements

This is the source list for go-to-market scoring. It is facts only, drawn from the 15 screenshots. It replaces the mixed C1–C62 list in `working-notes.md` §3, which is kept for history.

## Definitions
- **Feature (capability):** gives the user an outcome (an answer, an artifact or a decision) or moves them to the next step in the flow, **and** a competitor could offer it too. Only features are scored on demand and competitiveness.
- **Not a feature:** UI components, input steps, workflow utilities, trust and disclosure items, account and settings, data sources. These hold, feed or explain features.
- **Evidence:** Seen = fully visible · Partly seen = some of it visible · Button only = the control is on screen but was not opened.

## Features and capabilities (32)

| ID | Feature | Stage | Module | Outcome for the user | Evidence | Screens |
|---|---|---|---|---|---|---|
| C01 | Market search and selection | Discover | Dashboard | Scope the analysis to chosen US cities, ZIPs or metros (up to 3) | Seen | 01, 02 |
| C02 | Market ranking by Market Score | Discover | Dashboard | Shortlist the strongest US markets | Partly seen | 02 |
| C03 | Seasonality analysis | Discover | Dashboard | See when demand and fill speed peak | Seen | 03 |
| C04 | Market forecasts | Discover | Dashboard | Forward view of the selected market | Button only | 02 |
| C05 | Submarket demand map | Discover | Dashboard | Find strong and weak pockets inside a metro | Seen | 02 |
| C06 | Supply map with listing status | Discover | Dashboard | See where properties are and whether they are live | Seen | 02 |
| C07 | Flood-risk overlay | Discover | Dashboard | Check FEMA flood exposure on the map | Button only | 02 |
| C08 | Market filters | Discover | Dashboard | Narrow the property set, including dormant ones | Button only | 02 |
| C09 | Saved views | Discover | Dashboard | Return to a saved market setup | Button only | 02 |
| C10 | Market report export | Discover | Dashboard | Keep or share a market report | Button only | 02, 11 |
| C11 | Property search | Analyze | Analyzer | Find a property by city, listing title or ID | Seen | 05, 06 |
| C12 | Property performance and revenue | Analyze | Dashboard and Analyzer | Occupancy, rent, rooms and estimated revenue now | Seen | 04, 06 |
| C13 | Property signal and recommendation | Analyze | Analyzer | A verdict and a next action for a property | Seen | 06 |
| C14 | Room-segment economics | Analyze | Analyzer | Price and occupancy by bath type and room size | Seen | 06, 07 |
| C15 | Rolling performance windows | Analyze | Analyzer | 7, 30 and 90-day direction and stability | Seen | 07 |
| C16 | Evidence quality scoring | Analyze | Analyzer | How far to trust a property's numbers | Partly seen | 07 |
| C17 | Visual comps | Analyze | Analyzer | Price a room against rooms that look like it | Seen | 08 |
| C18 | AI upgrade concepts | Analyze | Analyzer | Preview an upgrade on a listing photo | Seen | 09, 10 |
| C19 | Property trends | Analyze | Analyzer | Trend view for one property | Button only | 06 |
| C20 | Room-level history | Analyze | Analyzer | History for each room in a property | Button only | 05, 06 |
| C21 | Nearby supply check | Underwrite | Predictor | Active co-living supply within about 3 miles of any address | Seen | 11 |
| C22 | Bedroom layout recommendation | Underwrite | Predictor | Suggest a better room mix | Button only | 12 |
| C23 | Amenity ROI shortlist | Underwrite | Predictor | Find upgrades worth checking | Button only | 12 |
| C24 | House rules checklist | Underwrite | Predictor | Operating checklist compared with local policies | Button only | 12 |
| C25 | Per-room rent guidance | Underwrite | Predictor | Starting weekly rent for each room | Button only | 12 |
| C26 | Cohort lease-up outcomes | Underwrite | Predictor | How similar launches nearby filled their rooms | Button only | 12 |
| C27 | Revenue forecast for any address | Underwrite | Predictor | Monthly revenue with confidence and comps | Seen | 11–14 |
| C28 | Forecast stability test | Underwrite | Predictor | Re-test against recent or seasonal history | Seen | 13 |
| C29 | Comp set review | Underwrite | Predictor | Inspect the comps and caution flags | Button only | 14 |
| C30 | Garage conversion scenario | Underwrite | Predictor | Parking vs bedrooms, forecast both ways | Button only | 14 |
| C31 | Deal calculator (Pro) | Decide | Predictor | Cash flow, CoC, DSCR and cap rate | Partly seen | 11, 15 |
| C32 | Saved underwrites with re-run | Monitor | Predictor | See how the market moved since export | Partly seen | 11, 12 |

Totals: Discover 10 · Analyze 10 · Underwrite 10 · Decide 1 · Monitor 1. Evidence: 14 seen · 4 partly seen · 14 button only.

## Other product elements (31): not features

| Category | IDs and elements |
|---|---|
| UI components (14) | E01 Left sidebar navigation · E02 Top bar · E03 Market header and date range · E04 Market chips and Clear all · E05 Dashboard tabs · E06 Map layers panel and legend card · E07 Map controls · E08 Property detail drawer · E09 Drawer hand-off buttons · E10 Analyzer stepper · E11 Properties results list · E12 Analyzer tabs · E13 Property Photos gallery · E14 Predictor stepper and locked sections |
| Input steps (6) | E15 Date preset · E16 History window · E17 Address and map pin · E18 Core specifications form · E19 Bathroom and room mix inputs · E20 Access and common areas inputs |
| Workflow utility (1) | E21 Draft autosave, reset and Start fresh |
| Trust and disclosure (4) | E22 AI watermark and disclaimer · E23 Revenue disclaimers · E24 Support and confidence labels · E25 Live-listings rule |
| Account and settings (4) | E26 Plan badge and entitlements · E27 Account card and menu · E28 Privacy choices · E29 Theme toggle |
| Data sources (2) | E30 Basemap (Leaflet, OpenStreetMap, CARTO) · E31 FEMA NFHL flood data |

The full detail for every row (how it works, notes, the features each element supports) is in the Miro board's frames 03 and 04.

## Next step
Score each feature C01–C32 on **demand** and **competitiveness** against competitors. The Miro feature table has empty `Demand (later)` and `Competitiveness (later)` columns for this.
