# Feature matrix, what leads and what is table stakes

Load for: deciding which capability a page, demo, or post should lead with. Distills: S3 feature classification. Status is owned by `rules/feature-status.md`; the role column here is a WORKING hypothesis until scoring on demand and competitiveness is done (OPEN).

Roles: **LEAD** differentiating and SHIPPED, **HOOK** fast first answer for top of funnel, **STAKE** expected, must work, **SUPPORT** strengthens a lead, **HOLD** do not feature until status or evidence changes.

| ID | Feature | Stage | Status | Role | Why |
|---|---|---|---|---|---|
| C01 | Market search and selection | Discover | SHIPPED | STAKE | Every market tool has it |
| C02 | Market ranking by Market Score | Discover | PARTIAL | HOOK | National leaderboard is a natural entry point; publishing it needs data rights |
| C03 | Seasonality analysis | Discover | SHIPPED | SUPPORT | Room-level fill speed by season is uncommon |
| C04 | Market forecasts | Discover | UNVERIFIED | HOLD | Output never seen |
| C05 | Submarket demand map | Discover | SHIPPED | SUPPORT | Evidence-adjusted bands show where data is thin |
| C06 | Supply map with listing status | Discover | SHIPPED | STAKE | Maps are expected |
| C07 | Flood-risk overlay | Discover | UNVERIFIED | HOLD | Toggle only |
| C08 | Market filters | Discover | UNVERIFIED | HOLD | Never opened |
| C09 | Saved views | Discover | UNVERIFIED | HOLD | Never opened |
| C10 | Market report export | Discover | UNVERIFIED | HOLD | Button looked disabled |
| C11 | Property search | Analyze | SHIPPED | STAKE | Expected |
| C12 | Property performance and revenue | Analyze | SHIPPED | SUPPORT | Room-level KPIs with a revenue disclaimer |
| C13 | Property signal and recommendation | Analyze | SHIPPED | SUPPORT | A verdict plus a next action; one label seen |
| C14 | Room-segment economics | Analyze | SHIPPED | LEAD | Bath and size premiums are the room-level insight |
| C15 | Rolling performance windows | Analyze | SHIPPED | SUPPORT | Direction and stability over 7, 30, 90 days |
| C16 | Evidence quality scoring | Analyze | PARTIAL | SUPPORT | Backs the transparency message |
| C17 | Visual comps | Analyze | SHIPPED | LEAD | Prices a room against rooms that look like it; watch D-Q18 |
| C18 | AI upgrade concepts | Analyze | SHIPPED | HOLD | Demos well, but no upgrade economics yet |
| C19 | Property trends | Analyze | UNVERIFIED | HOLD | Never opened |
| C20 | Room-level history | Analyze | UNVERIFIED | HOLD | Never opened |
| C21 | Nearby supply check | Underwrite | SHIPPED | HOOK | Instant answer for any address |
| C22 | Bedroom layout recommendation | Underwrite | UNVERIFIED | HOLD | Output never seen |
| C23 | Amenity ROI shortlist | Underwrite | UNVERIFIED | HOLD | Output never seen |
| C24 | House rules checklist | Underwrite | UNVERIFIED | HOLD | Output never seen; fair-housing review needed |
| C25 | Per-room rent guidance | Underwrite | UNVERIFIED | HOLD | Likely LEAD once verified |
| C26 | Cohort lease-up outcomes | Underwrite | UNVERIFIED | HOLD | Likely LEAD once verified |
| C27 | Revenue forecast for any address | Underwrite | SHIPPED | LEAD | Formula, support, confidence on screen; watch D-Q26, D-Q28 |
| C28 | Forecast stability test | Underwrite | SHIPPED | SUPPORT | Lets the investor stress the evidence window |
| C29 | Comp set review | Underwrite | UNVERIFIED | HOLD | Collapsed in capture |
| C30 | Garage conversion scenario | Underwrite | UNVERIFIED | HOLD | Likely HOOK once verified |
| C31 | Deal calculator | Decide | PARTIAL | STAKE | Common elsewhere; Pro gate; watch D-Q30, D-Q31 |
| C32 | Saved underwrites with re-run | Monitor | PARTIAL | SUPPORT | Retention loop once outputs are seen |

## Reading the matrix

- Three LEADs today: C14, C17, C27. Every investor asset leads with C27; every operator asset leads with C14 or C17.
- Four likely promotions after founder verification: C25, C26 to LEAD, C30 to HOOK, C29 to SUPPORT. Each needs a status AMEND first.
- C18 stays HOLD for messaging even though it is SHIPPED, because a concept image without economics invites the "boost rent by" claim that `rules/do-not-say.md` bans.

## Next analytical step (OPEN)
Score each feature 1 to 5 on demand (from design-partner signals, `innovation/experiments.md` EXP-001) and competitiveness (from `reference/competitive-analysis.md`). Record the scores here with the date and the evidence count behind each.
