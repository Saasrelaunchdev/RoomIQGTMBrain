# Metric tree and baselines

The numbers that decide pivot or persevere. Every baseline starts as "not measured" and is filled only from real data with its date and source. Never estimate a baseline. Protocol: `reference/innovation-accounting.md`.
last_reviewed: 2026-11-13

## North Star (WORKING)
**Qualified underwrites per week:** forecasts run on addresses in covered metros that return better than Low confidence, by distinct users.

Why this one: it counts the moment RoomIQ delivers its core value (room-level evidence on a real deal), it penalizes runs on uncovered addresses that disappoint, and it moves only when acquisition, activation, and coverage all work.

## Input metrics

| ID | Metric | Definition | Audience | Stage | Kind | Baseline | Target | Source |
|---|---|---|---|---|---|---|---|---|
| M01 | Qualified underwrites per week | As above | A | 5 to 6 | North Star | not measured | founder to set | Product analytics |
| M02 | Activation rate | Share of new trials reaching the activation definition in 7 days | A | 5 | Actionable | not measured | set after EXP-001 | Product analytics |
| M03 | Time to first forecast | Median minutes from signup to first forecast | A | 4 to 5 | Actionable | not measured | none yet | Product analytics |
| M04 | Fallback share | Share of forecasts returned with fallback support | A | 5 | Actionable, coverage health | not measured | falling | Product analytics |
| M05 | Deal Calculator reach | Share of activated users who open the Deal Calculator | A | 5 to 7 | Actionable | not measured | none yet | Product analytics |
| M06 | Trial-to-Pro conversion | Share of a weekly trial cohort paying within 30 days | A | 7 | Actionable | not measured | none yet | Billing |
| M07 | Week-4 retention | Share of an activation cohort running a forecast in week 4 | A | 6 | Actionable | not measured | none yet | Product analytics |
| M08 | Qualified demos per week | Demos with Audience A in covered metros | A | 4 | Actionable | not measured | 2 by EXP-004 week 6 | `ops/activity-log.md` |
| M09 | Operator price changes | Operators reporting a price change after the Analyzer | B | 5 | Actionable | not measured | 2 of 5 | EXP-006 |
| M10 | Referred signups | Signups naming a referring user | A | 8 | Actionable | not measured | none yet | Signup form |

## Vanity guards
Track these only as context, never as success: total signups, page views, follower counts, AI concept generations, properties tracked, markets selected. Each becomes actionable only when divided by a cohort and tied to a decision.

## Brain health (learning velocity), computed by `tools/brain.py metrics`

| ID | Metric | Healthy |
|---|---|---|
| L1 | Signals logged per week | At least 5 during the design-partner program |
| L2 | Open WATCH items | Moving, none older than two triage cycles |
| L3 | AMENDs per month | At least 1 while proof is being built |
| L4 | Experiments DONE per month | At least 1 |
| L5 | Assumptions resolved (VALIDATED or INVALIDATED) | Riskiest first |
| L6 | Days since last snapshot | 31 or fewer |
| L7 | Ledger staleness | `rules/feature-status.md` reviewed within 30 days |

## Cohorts
Weekly signup cohorts, split by audience (A, B) and by metro coverage (covered preset metro or not). Every rate above is read per cohort, never as a blended total.
