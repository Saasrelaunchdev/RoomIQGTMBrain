# Metrics methodology, how each number is built

Load for: support answers, methodology pages, demo explanations, in-app help text, and grounding an in-product assistant. Distills: S2 glossary section 4 and consistency checks section 8. Each row says how far the definition is verified. "Verified" means the arithmetic reproduces from a screenshot; "working" means a reasonable reading pending founder confirmation (G18 and related).

| Metric | Definition | Status | Evidence |
|---|---|---|---|
| Occupancy | Occupied rooms divided by total rooms | Verified | 5/8 = 62.5%, 7/8 = 87.5% |
| Avg daily price | Weekly price divided by 7 | Verified | $260 / 7 = $37 |
| Best spread | Largest average weekly price gap between segments | Verified | $310 minus $238 = $72 |
| Segment 90-day occupancy | Room-weighted, rolls up to the property | Verified | (3 x 71.5 + 5 x 57.1) / 8 = 62.5% |
| Forecast monthly revenue | Price x rooms x occupancy x 4.35 weeks | Verified | $282 x 1.0 x 89.5% x 4.35 = $1,098 |
| Illustrative scenarios | Forecast minus and plus 10 percent | Verified | $988 and $1,207 |
| Visual comp medians | Median price and median days to fill of the matches | Verified | $245, 9.5 days |
| Estimated rental revenue | About avg weekly asking x occupied rooms x weeks in window | Working | Reproduces within 1% on screen 06; not on screen 04 |
| Occ delta, price delta | Change against the prior equal-length window, likely relative percent | Working | 51.4% on the 30-day window |
| Volatility | Dispersion within the window, unit unknown | Working | 4.37, 11.15, 22.82 |
| Market Score | 0 to 100 composite with a letter grade | Working | Inputs unknown (G18) |
| Occupancy Health | Cell demand signal from observed occupied rooms | Working | UI helper text |
| Evidence-adjusted | Scores shrunk for small samples | Working | Legend footer |
| Fill speed, days to fill | Time for a vacant room to re-lease | Working | Chip colors: about 5 days or less green, 33 or more yellow |
| Completeness, history coverage | Share of expected fields present; share of the window observed | Working | 100% and 100% seen |
| Confidence | Forecast label, Low seen | Working | Levels unknown |

## Two weekly-to-monthly factors, documented so numbers reconcile
The Predictor uses 4.35 weeks per month (52.2 / 12). The Analyzer's 30-day windows imply 30 / 7 = 4.29. Expect small differences between modules for the same rent.

## Two model paths
Model routing picks the tracked-history path when RoomIQ already observes the property, and the bounded underwriting path for new addresses, where structural details apply as conservative adjustments. Neither path has a published backtest (G14).

## How to answer a methodology question
1. Give the definition from this table.
2. If the status is Working, say "here is how it reads; I'll confirm the exact method".
3. Never invent a formula, weight, or threshold. Log the question as a signal.
