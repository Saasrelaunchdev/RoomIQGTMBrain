# Decision log

What was decided and why, so settled strategy is not relitigated. Newest at the top. Parsed by `tools/brain.py metrics`.

Statuses: **DECIDED** (settled, change only by AMEND with new evidence), **WORKING** (the default the brain runs on; flips on the named trigger), **OPEN** (do not assume).

---

## 2026-11-13 D-12 Innovation accounting is the operating model (DECIDED)
Every GTM activity is logged in `ops/activity-log.md`, every market input in `ops/signal-log.md`, and every experiment states its metric and success threshold before it runs (`innovation/experiments.md`).

Rationale: RoomIQ is pre-proof. Without a baseline and pre-registered thresholds, early activity produces vanity numbers and no learning. The brain already holds the ledgers, so adding the accounting costs one file per concept.

**What this does not change:** the claim ledger, the status ledger, or any channel rule.
**Downstream:** `innovation/` files seeded 2026-11-13. Owner: founder.

## 2026-11-13 D-11 Pricing and packaging (OPEN)
No prices, trials, limits, or tier names other than `RoomIQ Pro` appear in any asset. Monetization signals seen in the product are recorded in `reference/pricing-packaging.md` as hypotheses.

**Trigger to close:** founder answer to G07.
**What this does not change:** `RoomIQ Pro` may be named, and the Deal Calculator may be described as Pro, because both are visible in the product.

## 2026-11-13 D-10 Channel mix (WORKING)
In: founder-led demos and sales calls, education content, community participation, product-led trial, product and release copy. Not yet: paid ads and cold outreach at volume.

Rationale: pre-baseline, paid spend buys traffic without a measured activation rate to judge it against, and cold outreach at volume carries brand risk while the data-source question is open. Founder-led conversations produce the signals the ledgers need fastest.
**Trigger to flip:** founder answer to G01, or a snapshot showing an activation baseline exists.
**What this does not change:** warm follow-ups to people who asked for information are in scope.

## 2026-11-13 D-09 Lead message is visible evidence, not accuracy (WORKING)
RoomIQ leads with "every number shows its evidence": formula, support level, comp distance, confidence.

Rationale: accuracy cannot be claimed (D-05), while the transparency design is SHIPPED and visible on screen 14. For buyers who put debt behind a decision, a number that admits its uncertainty is more credible than a confident one.
**Trigger to revisit:** a published backtest (G14), which would allow adding a scoped accuracy claim beside transparency.
**What this does not change:** the fallback clause stays mandatory on "any US address".

## 2026-11-13 D-08 Category framing (WORKING)
Room-level market intelligence and underwriting for US rent-by-the-room housing.

Rationale: "coliving analytics" is narrower than the product's underwriting depth; "real estate analytics" invites comparison with whole-unit and short-term rental tools on their own terms.
**Trigger to revisit:** founder answer to G05, or three independent prospects describing the category in other words (signal log).
**What this does not change:** glossary terms.

## 2026-11-13 D-07 Audience order (WORKING)
Acquiring investors first, operating hosts second, never blended in one asset. Lenders, brokers, and analysts are not a GTM audience yet.

Rationale: the product's full flow (Dashboard to Predictor to Deal Calculator to My Underwrites) and its UI copy ("investor-grade", "Property facts that investors actually underwrite") point at acquisition decisions. The Analyzer and Media Studio serve operators.
**Trigger to revisit:** founder answer to G05, or the design-partner program (EXP-001) showing operators activate faster.
**What this does not change:** operators keep their own value proposition and funnel.

## 2026-11-13 D-06 Demo rule (DECIDED)
Demos run only in well-covered metros (Dallas, Austin, Houston, Atlanta, Phoenix, Tampa) and never cross a known defect (D-Q26, D-Q28, D-Q30, D-Q18).

Rationale: the NYC capture produced a $282 per week room price on comps a median 82.88 mi away. A prospect's first run is the moment of highest drop-off risk.
**What this does not change:** copy may still say "any US address" with the fallback clause.
**Downstream:** `reference/demo-playbook.md`.

## 2026-11-13 D-05 No accuracy claims until a backtest is published (DECIDED)
**Trigger to amend:** a backtest with a stated method (MAPE, calibration of confidence labels), approved for publication.
**What this does not change:** transparency claims, which are SHIPPED facts.

## 2026-11-13 D-04 Data source never named or implied (DECIDED)
No source names, no "scraped", no partnership, integration, or affiliation claims with any platform.

Rationale: provenance and rights are unconfirmed (G11, G12), and the product creates AI derivatives of listing photos, which raises the stakes.
**What this does not change:** "observed room listings in the markets RoomIQ covers" is allowed.

## 2026-11-13 D-03 Evidence-graded status ledger (DECIDED)
Seen = SHIPPED, partly seen = PARTIAL, button only = UNVERIFIED, inferred = ROADMAP.

Rationale: a capability with a visible button and no captured output cannot be described without inventing its output.
**What this does not change:** founder confirmation (G03) can promote any line in one AMEND.

## 2026-11-10 D-02 Features are kept apart from UI and other elements (DECIDED)
32 features (C01 to C32) are scored on demand and competitiveness; 31 elements (E01 to E31: UI, inputs, disclosures, account, data sources) are not.
Source: `sources/extracted/discovery/feature-classification.md`.
**What this does not change:** elements still appear in copy where they explain a feature (for example the AI watermark).

## 2026-11-10 D-01 Facts-only rule (DECIDED)
The PRD and every capability claim use only what the screenshots show. Inferred items go to a "to confirm" list.
Source: `sources/extracted/discovery/README.md`.

---

## Open, owned elsewhere
Each is a question in `ops/founder-gap-interview.md`. Owner for all: founder.

| Question | Gap ID | Blocks |
|---|---|---|
| Data source, collection method, terms | G11 | Market intelligence content, any provenance copy |
| Rights to show listing photos, host names, and generate AI edits | G12 | Public screenshots, Media Studio marketing |
| Coverage numbers and refresh cadence | G13 | Any scale claim |
| Backtest of either forecast path | G14 | Any accuracy claim, lender audience |
| Status of 14 UNVERIFIED and 4 PARTIAL capabilities | G03 | Describing their outputs |
| Pricing, tiers, limits, trial, AI credits | G07 | Pricing page, packaging copy |
| Market Score inputs and grade bands | G18 | Explaining the score |
| Fixes for D-Q26, D-Q28, D-Q30, D-Q31 | G15 to G17 | Relaxing the demo rule |
| Primary ICP and channel mix | G05, G01 | Flipping D-07 and D-10 to DECIDED |
