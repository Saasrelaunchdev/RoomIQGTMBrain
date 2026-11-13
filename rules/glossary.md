# Glossary, canonical vocabulary

Mirrors the product UI exactly. Where the UI and a draft disagree, the UI wins. Terms marked (confirm) carry a working definition pending founder sign-off (`ops/founder-gap-interview.md`).
last_reviewed: 2026-11-13

## Brand and modules

| Term | Rule |
|---|---|
| RoomIQ | One word, capital R, I, Q. Never "Room IQ", "Roomiq", or "ROOMIQ" in prose. The wordmark is spaced caps; prose is not. |
| RoomIQ Pro | The only plan name visible in the product. Name it only as shown. No other tier names. |
| Dashboard | Market-level view: market picker, Overview, Trends, Forecasts tabs, Explore map. Capitalized. |
| Property Analyzer | Property-level deep dive. "the Analyzer" on second mention. Never "analyser". |
| Property Predictor | Underwriting flow for any US address. "the Predictor" on second mention. |
| Deal Calculator | Step 5 of the Predictor, marked Pro in the product. |
| My Underwrites | Saved property or market reports that can be re-run. |
| Media Studio | AI concept images of upgrades on listing photos. |
| Visually Similar Rooms | Image-similarity comps. Short form: "visual comps". |
| Explore map | The Dashboard map with submarket cells and property dots. |

## Metrics and outputs

| Term | Rule |
|---|---|
| Market Score | A 0 to 100 score with a letter grade. Never describe its inputs (confirm). |
| Occupancy | Occupied rooms divided by total rooms. Room-level, never unit-level. |
| Avg weekly asking | Mean asking rent per room per week. Rents are weekly in this category. |
| Fill speed, days to fill | How fast a vacant room is re-leased (confirm formula). |
| Occupancy Health | Submarket cell signal from observed occupied rooms. |
| Strong, Watch, Weak, Thin | Occupancy Score bands. "Thin" means too little evidence, never "low demand". |
| Evidence Quality | Completeness, history coverage, and media count for one property. |
| Property Signal | The action label on a property (seen: `Useful benchmark`) plus its recommendation. |
| Best spread | Largest average weekly price gap between room segments. |
| Room segment | Rooms grouped by bathroom (Private, Shared) or size (Cozy, Standard). |
| Rolling windows | 7, 30, and 90-day views of occupancy, daily price, volatility, and deltas. |
| Estimated rental revenue | Observed asking rents times occupancy for a window. Never "income", "earnings", or "collected". |
| Forecast | The Predictor's monthly revenue output. Use "forecast" for the output and "baseline profile" for the inputs. Never "baseline" for the output. |
| Fallback support | Local evidence was thin, so broader comps were used. Always shown with the confidence label. |
| Confidence | The forecast's label (seen: Low). Never translate into a percentage. |
| Illustrative scenarios | Plus and minus 10 percent of the forecast. Never "range", "interval", or "bounds". |
| Model routing | Automatic choice between the tracked-history path and the bounded underwriting path. |
| Evidence lookback | The window of market evidence (default 270 days) behind priors and comps. |
| Underwrite | Noun: a saved report in My Underwrites. Verb: to run a property through the Predictor. |
| AI concept | A watermarked, AI-generated edit of a listing photo. Never "render", "preview of results", or "after photo". |

## Category words

| Term | Rule |
|---|---|
| rent-by-the-room | The category, hyphenated as an adjective. Investors search for this phrase. |
| coliving | One word, lowercase, as in the product ("Nearby coliving supply"). Not "co-living" in RoomIQ copy. |
| residents | The people who rent rooms. Not "members" (a marketplace's own term), not "boarders". Avoid "tenants": legal status varies by state. |
| investors, operators | The two audiences. Never blend them in one asset. See `reference/icp-personas.md`. |
| short-term rental, Airbnb | Banned as descriptions of RoomIQ or its category. RoomIQ models weekly room rents, not nightly stays. |
| AI-powered | Banned as a blanket label. Name the capability: visual comps, AI concepts. |

## The distinction that must never blur

**Estimated** versus **actual**. Every RoomIQ number is an estimate built from observed listings, and it travels with its evidence: the as-of date, the support level, the confidence label. A forecast is never "accurate", an estimate is never "income", and an AI concept is never the property.
