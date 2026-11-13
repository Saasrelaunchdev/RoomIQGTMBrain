# Product surface, RoomIQ as built

Load for: describing what RoomIQ does, writing walkthroughs, release notes, demo scripts, or support answers. Distills: S1 screen inventory and S2 working notes (IA, entities).

Everything here is FACT from the 2026-11-10 captures unless marked. Status per capability lives in `rules/feature-status.md`; this file describes shape, not status.

## Information architecture

```
RoomIQ
  ANALYTICS
    Dashboard            gate: choose up to 3 cities, ZIPs, or a metro group
      Overview (n props) Top US markets by Market Score
      Trends             Seasonality: Occupancy | Fill speed, national fallback
      Forecasts          (never opened)
      Explore map        clusters, hex submarket cells, layers, FEMA toggle
      Property drawer    KPIs, estimated revenue, hand-offs to Predictor and Analyzer
    Property Analyzer    Search -> Pick property -> Analyze
      Overview           Property Signal, Performance Snapshot, segments,
                         rolling windows, Evidence Quality, Visually Similar
                         Rooms, Media Studio, Property Photos
      Trends, Rooms      (never opened)
  PREDICTOR
    Property Predictor   Location -> Baseline -> Forecast -> Results
      1 Location         address or pin, nearby coliving supply (~3 mi)
      2 Baseline Profile core specs, bathroom mix, amenity ROI, house rules,
                         room pricing, cohort outcomes, room mix, access
      3 Run Forecast     model routing (Automatic), evidence lookback (270d)
      4 Decision Board   monthly revenue, support, confidence, scenarios,
                         best next step, garage conversion
      5 Deal Calculator  Pro: scenario, income, purchase, financing
      My Underwrites     saved reports, re-run against the market
  Global                 RoomIQ Pro badge, theme toggle, Privacy choices
```

## The workflow the product is built around

Discover a market (Dashboard), inspect comparable properties (Analyzer), underwrite a target (Predictor), model financed returns (Deal Calculator), save and monitor (My Underwrites). The drawer button "Forecast Stabilized Revenue" connects the Dashboard to the Predictor.

## Data entities visible in the product

| Entity | Fields seen |
|---|---|
| Market | name, type (city, ZIP, metro), property count, Market Score, grade, badge, occupancy, trend per month |
| Submarket cell | Occupancy Health, band (Strong, Watch, Weak, Thin), snapshot date |
| Property | title, host display name, city, type, bedrooms, bathrooms, rooms total, occupied, available, occupancy, avg weekly asking, move-in fee, reviews, price drops, status, signal, evidence level |
| Room segment | dimension (bath, size), value, room count, avg weekly, 90-day occupancy |
| Rolling window | 7, 30, 90 days: occupancy, avg daily price, volatility, occupancy delta, price delta |
| Similar-room match | match percent, price per week, days to fill, location |
| Baseline profile | type, bedrooms, bathrooms, square feet, private-bath rooms, room entries, common space, garage, transit distance |
| Forecast result | monthly revenue, formula terms, model path, lookback, support, confidence, comp count, median comp distance, scenarios, next step |
| Deal scenario | scenario, revenue, other income, vacancy, price, ARV, concessions, closing costs, financing mode, down payment, rate |

## Numbers that reconcile (use in demos as "the math is on the screen")

- Segment occupancy rolls up both ways to the property's 62.5 percent (screen 07).
- Best spread: Private Bath $310 minus Shared Bath $238 = $72 (screens 06, 07).
- Forecast: $282 x 1.0 rooms x 89.5% x 4.35 weeks = $1,098 (screen 14). Scenarios are $988 and $1,207, plus and minus 10 percent.
- Visual comp medians: $245 per week and 9.5 days to fill (screen 08).

## Third-party surfaces in the product

Leaflet, OpenStreetMap, and CARTO for maps; FEMA NFHL as a toggle; a geocoder (provider unknown); a generative image model and an image-embedding model (vendors unknown). Compliance notes for each: `reference/trust-and-risk.md`.
