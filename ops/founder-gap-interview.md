# Founder gap interview, Phase 2 of the build

One batched round of questions the sources could not answer. Each one changes the build. Each carries the **working default** the brain runs on today, so the founder can confirm with a word instead of composing an answer.

How to answer: reply inline (`G07: confirmed` or `G07: no, it is X`). Every answer is applied with the amendment procedure: ledger in `rules/` first, then the master context, then a dated entry in `ops/decisions.md`, then copy. Answers also close the matching item in `innovation/assumptions.md` where one exists.

Sent: 2026-11-13. Owner of answers: RoomIQ founder.

## A. The four that are almost always missing

| ID | Question | Working default in the brain | Changes |
|---|---|---|---|
| G01 | Which channels are in, and which are explicitly out? | In: founder-led demos and sales calls, data-led content (education and product walkthroughs), community participation, product-led trial. Not yet: paid ads, cold outreach at volume. | `rules/writing-rules.md`, `rules/do-not-say.md`, `reference/content-engine.md`, `prompts/common-tasks.md` |
| G02 | What real, permissioned proof exists? Customers, pilots, quotes, metrics, logos. Give the exact permitted wording. | None. The customer proof set is empty, so every asset uses product facts only. | `ops/copy-bank.md` proof section, `rules/do-not-say.md` |
| G03 | Status by capability: confirm SHIPPED for the 14 seen features and give real status for the 14 "button only" ones and the 4 partly seen ones. | Evidence-graded: seen = SHIPPED, partly seen = PARTIAL, button only = UNVERIFIED. | `rules/feature-status.md` |
| G04 | Words and claims RoomIQ refuses to use, beyond the defaults. Any phrasing legal has rejected? | Default banned-word list plus RoomIQ-specific bans on accuracy, coverage, data-source, and financial-advice claims. | `rules/writing-rules.md`, `rules/do-not-say.md` |

## B. Often missing

| ID | Question | Working default | Changes |
|---|---|---|---|
| G05 | Who is the primary customer? | Acquiring investors first (Discover to Decide flow), operating hosts second. Lenders and brokers are not a GTM audience yet. | `reference/icp-personas.md`, value propositions, `ops/decisions.md` |
| G06 | Two brands whose voice is right, two that are wrong. | Right: plain, numerate, evidence-first, like a good underwriting memo. Wrong: hype-driven "passive income" real estate marketing. | `rules/writing-rules.md` |
| G07 | Pricing: decided, or separate work? Tier names beyond `RoomIQ Pro`, prices, limits, trial, AI credits. | Undecided. No prices, limits, or trials in any copy. `RoomIQ Pro` may be named because it is visible in the product. | `reference/pricing-packaging.md`, `rules/do-not-say.md` |
| G08 | Anything historical to handle: a prior product, a rebrand, a public incident? | None known. | `rules/do-not-say.md` |
| G09 | Who signs off on a claim change, and who owns each ledger? | Founder approves every AMEND. Anyone may PATCH. | `ops/review-cadence.md` |
| G10 | Review cadence and corroboration thresholds. | Weekly triage, monthly ledger sweep and snapshot, quarterly audit. Opinions need 3 instances in 60 days, facts need 1 verified. | `ops/review-cadence.md`, `ops/signal-log.md` |

## C. RoomIQ-specific, highest consequence first

| ID | Question | Working default | Changes |
|---|---|---|---|
| G11 | Where does the listing data come from, how is it collected, and under what terms? | Never named, never implied, no partnership or affiliation claims. | `rules/do-not-say.md`, `reference/trust-and-risk.md` |
| G12 | Do you have the rights to show listing photos and host names, and to generate AI edits of listing photos? | Public assets blur host names and avoid third-party photos. AI concepts appear only watermarked. | `rules/do-not-say.md`, `reference/demo-playbook.md` |
| G13 | Coverage: how many US markets, properties, rooms, and photos are tracked, and how often is data refreshed? | No coverage numbers in copy. "In the markets RoomIQ covers." | `ops/copy-bank.md`, `rules/do-not-say.md` |
| G14 | Has either forecast path been backtested (MAPE, calibration)? | No accuracy claims of any kind. | `rules/do-not-say.md`, `innovation/experiments.md` EXP-002 |
| G15 | Q26: the results banner says the forecast uses the full bedroom count, the math uses 1.0 active rooms. Which is right, and is a fix scheduled? | Treated as a live defect. Never shown in demos. | `rules/feature-status.md`, `reference/demo-playbook.md` |
| G16 | Q30: is the Deal Calculator interest-rate default really 22%? Q31: is vacancy double counted? | Treated as unverified. Deal Calculator demos always use typed inputs. | `reference/demo-playbook.md` |
| G17 | Q28: should the Predictor refuse or soft-block uncovered metros (median comp distance 82.88 mi in the NYC example)? | Demos stay in well-covered Sun Belt metros. Copy names fallback labeling as the safeguard. | `rules/do-not-say.md`, `reference/demo-playbook.md` |
| G18 | Market Score: inputs, weights, grade bands, and what the `High` badge means. | Described only as "a 0 to 100 score with a letter grade". | `rules/glossary.md` |
| G19 | Which outputs are LLM-generated, rules-based, or statistical (layouts, amenities, house rules, rent guidance, cohorts)? | None of them is called "AI" in copy. Only Visually Similar Rooms and Media Studio carry AI framing. | `rules/glossary.md`, `rules/do-not-say.md` |
| G20 | Is anything outside the US planned? | US only. | `rules/feature-status.md` |
| G21 | Which of the 50 Part A coverage gaps can you capture next? The P1 set is the priority. | The brain treats every uncaptured screen as UNVERIFIED. | `sources/README.md`, `rules/feature-status.md` |

## After the answers land

1. Apply each answer as an AMEND, one decision entry per answer or per group.
2. Re-run `python3 tools/brain.py audit` and `python3 tools/brain.py build`.
3. Regenerate `adapters/portable-control-layer.md`, since it carries ledger content.
4. Take a snapshot in `snapshots/` labeled `founder-answers`, recording what changed and what did not.
