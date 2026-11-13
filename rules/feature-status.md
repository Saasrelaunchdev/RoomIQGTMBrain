# Feature status ledger

Governs what can be promised. Update this file the moment status changes, before any copy follows.
last_reviewed: 2026-11-13

Legend, graded by evidence because the only source so far is 15 product screenshots (2026-11-10):
- **SHIPPED**: seen working in the product. Present tense, described only as far as the screens show.
- **PARTIAL**: partly seen. Describe the visible part only.
- **UNVERIFIED**: the control exists in the UI, the output was never captured. Name it, never describe what it returns. Founder confirms (G03).
- **IN BUILD**: committed, not shipped. "Coming soon" or omit. None confirmed today.
- **ROADMAP**: inferred direction. Never a launch claim.

Line format, parsed by `tools/brain.py`: `- **ID Name** [aliases]: STATUS. Note.`

## Discover (Dashboard)
- **C01 Market search and selection** [market picker, choose markets]: SHIPPED. City, ZIP, or metro group, up to 3 per dashboard.
- **C02 Market ranking by Market Score** [top us markets, leaderboard, market score]: PARTIAL. Ranked list seen; score inputs unknown.
- **C03 Seasonality analysis** [seasonality, fill speed curve]: SHIPPED. Occupancy and fill speed, with a national fallback label.
- **C04 Market forecasts** [forecasts tab, market forecast]: UNVERIFIED.
- **C05 Submarket demand map** [hex cells, occupancy health, submarket signals]: SHIPPED. Evidence-adjusted cells, Strong, Watch, Weak, Thin.
- **C06 Supply map with listing status** [explore map, listing status]: SHIPPED. Listed, Coming soon, Never listed, Delisted.
- **C07 Flood-risk overlay** [fema, flood]: UNVERIFIED. Toggle seen, layer never rendered.
- **C08 Market filters** [advanced filters, dormant properties]: UNVERIFIED.
- **C09 Saved views** [saved view]: UNVERIFIED.
- **C10 Market report export** [market report]: UNVERIFIED. Button looked disabled in the capture.

## Analyze (Property Analyzer)
- **C11 Property search** [search by city, property id]: SHIPPED. Matches listing-title text as well as city.
- **C12 Property performance and revenue** [performance snapshot, estimated rental revenue]: SHIPPED.
- **C13 Property signal and recommendation** [property signal, useful benchmark]: SHIPPED. One label seen; full label set unknown.
- **C14 Room-segment economics** [room segments, bathroom premium, best spread]: SHIPPED.
- **C15 Rolling performance windows** [rolling windows, 7d, 30d, 90d]: SHIPPED.
- **C16 Evidence quality scoring** [evidence quality, completeness]: PARTIAL.
- **C17 Visual comps** [visually similar rooms, similar rooms]: SHIPPED. Searches across markets, not only the local one.
- **C18 AI upgrade concepts** [media studio, ai concept]: SHIPPED. Five presets seen; output watermarked.
- **C19 Property trends** [trends tab]: UNVERIFIED.
- **C20 Room-level history** [rooms tab, room history]: UNVERIFIED.

## Underwrite (Property Predictor)
- **C21 Nearby supply check** [nearby coliving supply]: SHIPPED. About 3 miles around any US address.
- **C22 Bedroom layout recommendation** [compare layouts, bedroom mix]: UNVERIFIED.
- **C23 Amenity ROI shortlist** [amenity roi, recommend amenities]: UNVERIFIED.
- **C24 House rules checklist** [house rules, recommend rules]: UNVERIFIED.
- **C25 Per-room rent guidance** [rent guidance, price optimizer]: UNVERIFIED.
- **C26 Cohort lease-up outcomes** [cohort outcomes, lease-up]: UNVERIFIED.
- **C27 Revenue forecast for any address** [forecast, decision board, stabilized revenue]: SHIPPED. Formula, support, and confidence shown. See defect D-Q26.
- **C28 Forecast stability test** [evidence lookback]: SHIPPED.
- **C29 Comp set review** [support details, caution flags]: UNVERIFIED.
- **C30 Garage conversion scenario** [garage conversion]: UNVERIFIED.

## Decide and Monitor
- **C31 Deal calculator** [deal calculator, cash on cash, dscr, cap rate]: PARTIAL. Inputs seen, outputs never captured. Pro only.
- **C32 Saved underwrites with re-run** [my underwrites, saved underwrites]: PARTIAL. Empty state only.

## Roadmap, inferred and never claimable
- **R01 Upgrade economics per AI concept** [upgrade economics]: ROADMAP. From "no validated economics for this edit yet".
- **R02 Alerts on market moves** [market alerts, market-move alerts]: ROADMAP. Not seen anywhere; implied by the re-run copy.
- **R03 Markets outside the US** [international markets, outside the us]: ROADMAP. Only hint is "this country's" in one helper line.

## Known defects that gate claims
- D-Q26: forecast banner says full bedroom count, the math uses 1.0 active rooms.
- D-Q28: uncovered addresses still forecast, on comps a median 82.88 mi away.
- D-Q30: Deal Calculator interest default may read 22%. D-Q31: vacancy may double count.
- D-Q18: closet photos appear as visual comps.

## Demo rule
Nothing UNVERIFIED, IN BUILD, or ROADMAP is screen-recorded, narrated, or shown as if a customer can do it today. No demo crosses a known defect. See `reference/demo-playbook.md`.
