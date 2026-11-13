# Leap-of-faith assumptions register

The beliefs RoomIQ's go-to-market rests on, stated so they can be proven wrong. Parsed by `tools/brain.py metrics` (one table row per assumption). Protocol: `reference/innovation-accounting.md`.
last_reviewed: 2026-11-13

Types: **VALUE** (customers get value), **GROWTH** (customers find RoomIQ and bring others), **RISK** (something outside the funnel that can stop the business).
Statuses: **UNTESTED**, **TESTING**, **VALIDATED**, **INVALIDATED**. Riskiness: 1 (low) to 5 (would end the current GTM if false).

| ID | Assumption | Type | Riskiness | Status | Evidence so far | Tested by |
|---|---|---|---|---|---|---|
| R1 | RoomIQ has the rights to display the listing data, photos, and host names it shows, and to make AI derivatives of the photos | RISK | 5 | UNTESTED | None in sources; flagged high priority in S2 | G11, G12 |
| R2 | Coverage in the Sun Belt preset metros is deep enough that most investor addresses there forecast better than Low confidence | RISK | 5 | UNTESTED | DFW capture: 163 of 205 cells Thin | EXP-005 |
| A1 | Acquiring investors will run real, live deals through the Predictor instead of only their spreadsheet | VALUE | 5 | UNTESTED | Product flow built for it; no user evidence | EXP-001 |
| R3 | Forecast error is small enough that investors and lenders act on it | RISK | 4 | UNTESTED | No backtest | EXP-002 |
| A3 | Investors will pay for RoomIQ Pro to reach the Deal Calculator and saved underwrites | VALUE | 4 | UNTESTED | Pro gate visible; pricing undecided | EXP-003 |
| A2 | Visible uncertainty (formula, support, confidence) increases trust more than it scares buyers off | VALUE | 4 | UNTESTED | Product posture; no user evidence | EXP-001 |
| G1 | Education content on room-level underwriting reaches Audience A at low cost | GROWTH | 3 | UNTESTED | None | EXP-004 |
| A4 | Operators change a room price after seeing segment premiums or visual comps | VALUE | 3 | UNTESTED | None | EXP-006 |
| G2 | Investor communities convert to demos when the founder answers questions with worked examples | GROWTH | 3 | UNTESTED | None | EXP-004 |
| A7 | Saved underwrites and re-runs bring investors back weekly | VALUE | 3 | UNTESTED | My Underwrites empty state only | After C32 verified |
| G3 | Activated investors refer a JV partner, lender, or community peer | GROWTH | 2 | UNTESTED | None | Snapshot cohort review |
| A5 | AI concepts help operators decide on upgrades, rather than being a novelty | VALUE | 2 | UNTESTED | Feature SHIPPED; no economics | EXP-006 follow-up |
| A6 | Market Score is used to choose markets, not only browsed | VALUE | 2 | UNTESTED | None | Product analytics |

## How to update a row
1. A signal or experiment result arrives. Add the evidence in a short phrase with its date and source ID (signal date, EXP id).
2. Change status only when an experiment's pre-set threshold is met or missed, or a single verified fact settles a RISK row.
3. A status change to VALIDATED or INVALIDATED is an AMEND: write a decision entry in `ops/decisions.md` naming what it changes and what it does not.
4. Re-rank riskiness monthly in the snapshot. Work on the highest riskiness first.
