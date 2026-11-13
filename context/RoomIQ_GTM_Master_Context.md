---
title: RoomIQ Go-To-Market Master Context
project: RoomIQ
type: gtm_context_file
purpose: Single source of truth for any AI agent or human executing RoomIQ go-to-market work.
version: 1.0
last_updated: 2026-11-13
status_notes: Built from 15 product screenshots (2026-11-10) and a desk scan of competitors (2026-11-13). Founder interview pending (ops/founder-gap-interview.md). ICP, positioning, and channel mix are WORKING hypotheses. Pricing undecided. Data source and rights unconfirmed, so never named. No customer proof exists. No forecast backtest exists, so no accuracy claims. 14 of 32 capabilities are UNVERIFIED. Known defects D-Q26, D-Q28, D-Q30 gate demos.
canonical_vocabulary: RoomIQ, RoomIQ Pro, Dashboard, Property Analyzer, Property Predictor, Deal Calculator, My Underwrites, Media Studio, Visually Similar Rooms, Explore map, Market Score, Occupancy, Avg weekly asking, Fill speed, Occupancy Health, Evidence Quality, Property Signal, Best spread, Room segment, Rolling windows, Estimated rental revenue, Forecast, Baseline profile, Fallback support, Confidence, Illustrative scenarios, Model routing, Evidence lookback, Underwrite, AI concept, rent-by-the-room, coliving, residents
---

# RoomIQ Go-To-Market Master Context

This file is the complete, distilled go-to-market for RoomIQ. Any AI agent or operator can absorb the product, the audiences, the claim rules, the competitive frame, the funnels, and the experiment plan in one read, then execute without re-deriving anything.

If you are an AI agent, read Section 0 first.

---

## 0. Agent operating instructions

**What this file is.** The distilled output of the RoomIQ discovery pack (15 screenshots captured in three batches on 2026-11-10: screen inventory, working notes, feature classification, coverage gaps) plus a competitive desk scan (2026-11-13). Sources are listed in `sources/README.md`.

**Authority labels used below.**
- **FACT**: seen in the product. Safe to state, within the limits of what the screen showed.
- **WORKING**: a provisional default the brain operates on until the founder answers. Use it; do not present it as settled strategy to outsiders.
- **OPEN**: undecided. Do not assume an answer. Write `[NEEDS BRAIN]` and keep going.

**How to use it.**
1. Before any customer-facing copy, load the four control files: `rules/writing-rules.md`, `rules/do-not-say.md`, `rules/feature-status.md`, `rules/glossary.md`. They override instinct and older phrasing.
2. Pick one audience (Section 8). Never blend investors and operators in one asset.
3. Write to one funnel stage (Section 13).
4. Obey the verdicts in Section 9, including the WORKING ones.
5. Run `ops/QA-checklist.md` before returning anything.

**Hard guardrails, never violate:**
1. No accuracy claims about forecasts. RoomIQ has no published backtest. Claim transparency instead.
2. "Underwrite any US address" always travels with the fallback clause in the same sentence.
3. Never name, imply, or describe the data source, and never claim a partnership or affiliation with any platform.
4. No coverage numbers, customer counts, testimonials, or outcome metrics. The customer proof set is empty.
5. UNVERIFIED capabilities are named, never described. ROADMAP items are never mentioned externally.
6. No prices, trials, or limits. `RoomIQ Pro` is the only tier name you may use.
7. Financial outputs are "for information, not financial advice". House rules never reference a protected class.
8. AI concepts are always labeled and watermarked, never presented as the real property.

---

## 1. House writing rules

Full rules: `rules/writing-rules.md`. The short form:

- No em dashes. No banned words (leverage, unlock, seamless, robust, and the rest of the list).
- Plain, numerate, candid. Write like an underwriting memo, not like real estate hype.
- Every number carries its unit and window. Rents are weekly per room; revenue is monthly per property.
- Say the uncomfortable part first. The product itself labels "Fallback support" and "Confidence Low"; the copy matches that candor.
- One reader, second person, short paragraphs.

---

## 2. Canonical vocabulary

Full table: `rules/glossary.md`. The terms most often gotten wrong:

| Term | Rule |
|---|---|
| RoomIQ | One word, R, I, Q capitalized. |
| Property Predictor, Property Analyzer | Full names first, then "the Predictor", "the Analyzer". |
| Forecast vs baseline profile | Forecast is the output. Baseline profile is the input form. |
| Estimated rental revenue | Observed asking rents times occupancy. Never income or earnings. |
| Illustrative scenarios | Plus and minus 10 percent. Never an interval or a range. |
| Thin | Too little evidence. Never "weak demand". |
| coliving | One word, as in the product. |
| residents | Not "members", not "tenants". |

The distinction that must never blur: estimated versus actual.

---

## 3. Status ledger

Full ledger, machine-parseable: `rules/feature-status.md`.

Evidence grading, because screenshots are the only source: **SHIPPED** (seen), **PARTIAL** (partly seen), **UNVERIFIED** (control seen, output never captured), **IN BUILD** (none confirmed), **ROADMAP** (inferred only).

| Stage | Capabilities | SHIPPED | PARTIAL | UNVERIFIED |
|---|---|---|---|---|
| Discover (Dashboard) | C01 to C10 | C01, C03, C05, C06 | C02 | C04, C07, C08, C09, C10 |
| Analyze (Analyzer) | C11 to C20 | C11, C12, C13, C14, C15, C17, C18 | C16 | C19, C20 |
| Underwrite (Predictor) | C21 to C30 | C21, C27, C28 | none | C22 to C26, C29, C30 |
| Decide | C31 | none | C31 | none |
| Monitor | C32 | none | C32 | none |

Totals: 14 SHIPPED, 4 PARTIAL, 14 UNVERIFIED. ROADMAP, never claimable: upgrade economics per AI concept, market-move alerts, markets outside the US.

**Defects that gate demos and claims (FACT, from the captures):**
- D-Q26: the results banner says the forecast uses the full bedroom count; the formula uses 1.0 active rooms ($282 x 1.0 x 89.5% x 4.35 = $1,098).
- D-Q28: an uncovered address (Upper East Side, 0 coliving supply within about 3 mi) still forecasts, on comps a median 82.88 mi away.
- D-Q30: the Deal Calculator interest-rate default may read 22%. D-Q31: a 5% vacancy haircut may double count occupancy.
- D-Q18: two of twelve visual comps were empty-closet photos.

---

## 4. Claim hygiene ledger

Full ledger with safe replacements: `rules/do-not-say.md`. The spine:

| Never | Instead |
|---|---|
| Accurate, precise, proven forecasts | Every forecast shows its formula, comps, support level, and confidence. |
| Any market, every property, complete coverage | Any US address, with fallback support labeled where evidence is thin. |
| Named data source, partnership, "real-time" | Observed room listings in covered markets, with an as-of date. |
| Income, earnings, collected rent | Estimated rental revenue, not collected payments. |
| Best deals, guaranteed returns, lender-ready | Model the deal with your own inputs. For information, not financial advice. |
| "AI-powered" on everything | Name the capability. Only visual comps and AI concepts carry AI framing. |
| Prices, trials, limits | Nothing. Pricing is OPEN. |
| Testimonials, counts, outcomes | `[PROOF POINT NEEDED]`. |

---

## 5. What RoomIQ is

**FACT.** RoomIQ is a web SaaS product for the US rent-by-the-room (coliving) market. It tracks room-level listings: weekly asking rent per room, room move-in fees, occupied and available rooms, listing status, price drops, reviews, and photos. From those it builds market, property, and deal-level views.

**Three modules, one workflow.**

| Stage | Module | What the user gets |
|---|---|---|
| Discover | Dashboard | Choose up to 3 US cities, ZIPs, or a metro group. See Top US markets by Market Score, seasonality (occupancy, fill speed), and an Explore map with hex submarket cells banded Strong, Watch, Weak, Thin, plus property dots by listing status. A property drawer shows KPIs and estimated rental revenue, with hand-offs to the Analyzer and the Predictor. |
| Analyze | Property Analyzer | Search by city, property ID, or listing-title text. Get a Property Signal with a recommendation, a Performance Snapshot, room-segment economics (Private vs Shared bath, Cozy vs Standard size), 7, 30, and 90-day rolling windows, Evidence Quality, Visually Similar Rooms, and Media Studio AI concepts. |
| Underwrite | Property Predictor | Underwrite any US address via geocoded search or a map pin, with fallback support labeled where nearby evidence is thin. See nearby coliving supply within about 3 mi. Fill a baseline profile (type, bedrooms, baths, square feet, bathroom mix, room mix, common areas, garage, transit distance). Run a forecast with automatic model routing and an evidence lookback slider (default 270 days). Get monthly revenue with the formula printed, support level, confidence, illustrative scenarios, comp count, median comp distance, and a best next step. |
| Decide | Deal Calculator (Pro) | Scenario (Conservative, Base, Aggressive), income prefilled from the forecast, purchase, financing. Outputs cash flow, CoC, DSCR, cap rate (outputs not yet captured). |
| Monitor | My Underwrites | Saved property or market reports, re-run to see how the market moved since export (empty state only). |

**The trust design is the product's most distinctive trait (FACT).** The formula is printed under the forecast. "Fallback support" and "Confidence Low" are labeled openly. The median comp distance is disclosed. The scenarios state "not a calibrated prediction interval". Local and expanded comps are shown separately. Soft signals (listing copy, operator behavior) are excluded from forecast inputs on purpose. Revenue estimates carry "Based on observed rents and occupancy, not collected payments." AI concepts carry a burned-in watermark and a disclaimer. The numbers reconcile: segment occupancy rolls up to the property's 62.5%, the best spread is $310 minus $238 = $72, and the forecast formula reproduces to the dollar.

**An AI and computer-vision layer (FACT).** Visually Similar Rooms matches room photos across markets (94 to 96 percent match seen) and shows each match's weekly price and days to fill. Media Studio generates upgrade concepts on listing photos with five presets (Add desk, Add ceiling fan, Repaint neutral, LVP flooring, Stage empty room).

**Platform (FACT).** A `RoomIQ Pro` badge, entitlement chips ("Unlimited analyzer access", "Unlimited baseline runs"), a Pro-only Deal Calculator, light and dark themes, and a Privacy choices link. Maps run on Leaflet with OpenStreetMap and CARTO tiles. A FEMA flood layer toggle exists.

**What RoomIQ is not.** Not a listing marketplace, not a property manager, not a short-term rental tool, not a lender, not a legal or compliance service.

---

## 6. Feature matrix

Source: `reference/feature-matrix.md` (32 features, C01 to C32; 31 non-feature elements kept apart). Demand and competitiveness scoring is the next analytical step and is OPEN. The working split below is a hypothesis to test, not a score.

**WORKING, leads messaging (differentiating and SHIPPED):**
- Room-level economics: room segments, best spread, rolling windows (C14, C15, C12).
- A forecast for any US address that shows its work, fallback support included: formula, support, confidence, comp distance (C27, C28).
- Visual comps: price and days to fill of rooms that look like yours (C17).

**WORKING, table stakes (expected, must work, rarely the reason to buy):**
- Market search, maps, property search, filters (C01, C05, C06, C08, C11).
- A deal calculator with CoC, DSCR, cap rate (C31). Calculators are widely available elsewhere.

**WORKING, top-of-funnel hooks:**
- "Top US markets by Market Score" (C02) as a discovery entry point, subject to data-rights confirmation before any public publication.
- Nearby coliving supply for any address (C21) as a fast first answer.
- The garage conversion question (C30), once verified, because it is a decision investors already argue about.

**Novelty to handle with care:** Media Studio (C18). It demos well and has compute cost per generation; it leads nothing until upgrade economics exist.

---

## 7. Competitive market analysis

Full analysis: `reference/competitive-analysis.md`. Battlecards: `reference/competitor-battlecards.md`. Every rival fact is from public pages scanned on 2026-11-13 and must be re-verified before external use.

**Market shape (WORKING).** Rent-by-the-room investors today assemble an underwriting picture from five kinds of tools, none built at the room level for an investor evaluating properties they do not yet own:

| Alternative | Examples | What it does well | Where it stops |
|---|---|---|---|
| Spreadsheets and forums | Personal models, investor forums, coaches | Free, flexible, community wisdom | Assumptions typed by hand, no market evidence |
| Platform-native host tools | The marketplaces' own host dashboards and calculators | Real booking data for their own hosts, free to them | One platform's view, built for its hosts, self-reported |
| Short-term rental analytics | AirDNA, Mashvisor, Rabbu | Deep nightly-stay data, investor workflows | Nightly stays, not weekly room rents |
| Whole-unit rent comps | Rentometer, HelloData, RentCast | Address-level rent comps, APIs | Units, not rooms |
| Deal calculators | DealCheck and similar | Cash flow, CoC, DSCR, cap rate | No market evidence for room revenue |

**Scoring vectors (WORKING):** granularity (room vs unit vs night), evidence transparency (shows formula, support, confidence), underwriting depth (address to financed returns in one flow), and visual evidence (photo-based comps).

**The wedge (WORKING).** Room-level evidence plus visible uncertainty. Competitors either work at the wrong unit (night, unit) or ask the investor to type the revenue assumption. RoomIQ starts from observed room rents and says how much to trust the result.

**Primary rival (WORKING):** the status quo, a spreadsheet plus a platform's host calculator. Win by showing the room-level evidence the spreadsheet lacks and the uncertainty the calculator hides.

---

## 8. Ideal customer profile

Full personas and buying committee: `reference/icp-personas.md`.

**Audience A, acquiring investors (WORKING primary).** Individuals and small teams buying or converting single-family homes into rent-by-the-room properties in US Sun Belt metros. Jobs: pick a market, check supply near an address, forecast stabilized revenue, decide the room mix (garage, bathrooms), test financed returns, keep the underwrite. Evidence: the product's end-to-end flow (Dashboard to Predictor to Deal Calculator to My Underwrites), the "Forecast Stabilized Revenue" hand-off, the "investor-grade" and "investors actually underwrite" UI copy.

**Audience B, operating hosts (WORKING secondary).** Operators running one to roughly twenty rent-by-the-room houses who want to price rooms, benchmark properties, and plan upgrades. Evidence: the Analyzer (Property Signal, segments, rolling windows), visual comps, Media Studio, rent guidance, house rules.

**Not a GTM audience yet: lenders, brokers, acquisition analysts.** The product hints at them (DSCR, Evidence Quality) but targeting them needs a published backtest first. Do not write for them until a decision says so.

**Geography (FACT for presets, WORKING for targeting).** The seven preset metros are all Sun Belt: Dallas–Fort Worth, Orlando, Houston, Phoenix, Atlanta, Las Vegas, Jacksonville. Demos and early targeting stay there.

**Buying committee for Audience A:** the investor (decides and pays), a spouse or JV partner (approves capital), a DSCR or portfolio lender (influences, cares about evidence), a coach or mentor community (influences tool choice), the operator or property manager (uses the Analyzer later).

**Design-partner profile (WORKING):** an investor with at least one active rent-by-the-room deal under evaluation in a covered metro, who will run it through the Predictor live and share what they decided.

---

## 9. Strategic verdicts

Full log with rationale and "what this does not change": `ops/decisions.md`.

| ID | Verdict | Status |
|---|---|---|
| D-01 | Facts-only rule: capabilities are described only as far as a screenshot shows them. | DECIDED |
| D-02 | Features are scored; UI, inputs, disclosures, and account items are not features. | DECIDED |
| D-03 | Evidence-graded status ledger with an UNVERIFIED flag. | DECIDED |
| D-04 | Never name or imply the data source; no partnership claims. | DECIDED (guardrail until G11) |
| D-05 | No accuracy claims until a backtest is published. | DECIDED (guardrail until G14) |
| D-06 | Demos only in well-covered metros; no demo crosses a known defect. | DECIDED |
| D-07 | Acquiring investors first, operating hosts second, never blended. | WORKING |
| D-08 | Category: room-level market intelligence and underwriting for rent-by-the-room. | WORKING |
| D-09 | Lead message: evidence you can see (transparency), not accuracy. | WORKING |
| D-10 | Channel mix: founder-led sales, education content, communities, product-led trial. Paid and cold outreach not yet. | WORKING |
| D-11 | Pricing and packaging. | OPEN |
| D-12 | Innovation accounting is the operating model: every activity logged, thresholds set before results. | DECIDED |

---

## 10. Value proposition: acquiring investors

Full pillars and reasons to believe: `reference/value-proposition-investors.md`.

**Promise (WORKING):** Know what each room can earn before you buy the house, and how much to trust the number.

**Pillars:**
1. **Find the market.** Rank US markets by Market Score, see seasonality, and spot strong and thin submarkets on the map (C01, C02, C03, C05).
2. **Underwrite at the room level.** Forecast monthly revenue for any US address from weekly room rents, occupancy, and your room mix, with the formula, support level, and confidence on screen, and fallback support labeled where nearby evidence is thin (C21, C27, C28).
3. **Decide with the financing math.** Carry the forecast into cash flow, CoC, DSCR, and cap rate on RoomIQ Pro, and save the underwrite to re-run later (C31, C32, both PARTIAL: say only what is visible).

---

## 11. Value proposition: operating hosts

Full pillars: `reference/value-proposition-operators.md`.

**Promise (WORKING):** See how every room in your house earns against rooms like it.

**Pillars:**
1. **Benchmark at the room level.** A Property Signal, room segments, and 7, 30, and 90-day windows show where a property earns its premium (C13, C14, C15).
2. **Price from rooms that look like yours.** Visual comps show the weekly price and days to fill of similar-looking rooms (C17).
3. **Plan upgrades with eyes open.** Preview an upgrade as a watermarked AI concept (C18). Amenity ROI and rent guidance exist in the product and are UNVERIFIED: name them, do not describe them.

---

## 12. Positioning statement

**Category (WORKING):** room-level market intelligence and underwriting.
**Niche:** US rent-by-the-room housing.

For US rent-by-the-room investors deciding where to buy, what a house will earn, and how to price its rooms, RoomIQ is room-level market intelligence and underwriting that shows its evidence. Short-term rental analytics model nightly stays and rent comps model whole units; RoomIQ works in the unit this business runs on, the room, priced weekly. And where a spreadsheet hides its guesses, every RoomIQ forecast prints its formula, its comps, and how much to trust it.

**Differentiation and defensibility (WORKING).** Room-level history compounds: each day of observed room rents and fill events deepens the evidence behind every score and forecast. The transparency design is a product posture, not a feature, and is hard to retrofit onto tools built to show a single confident number.

**The two objections that matter most:**
- "Where does your data come from?" Answer from `reference/objection-handling.md` only, without naming a source, until G11 is answered.
- "How accurate is the forecast?" "We do not claim accuracy yet. Every forecast shows its formula, its comps, how far away they are, and a confidence label, so you can judge it yourself."

---

## 13. Customer journey funnels

Full stage tables: `reference/customer-journey.md`. Both funnels are WORKING; stage KPIs have no baseline yet.

**Investor funnel:** Unaware, Problem aware (guessing room rents in a spreadsheet), Solution aware (room-level evidence exists), Evaluating (demo or first forecast), Activated (first forecast in a covered market at better than Low confidence, then the Deal Calculator), Habit (saved underwrites, repeat forecasts), Paid (RoomIQ Pro), Advocate (refers a JV partner or community).

**Operator funnel:** Unaware, Problem aware (rooms sit empty, pricing by gut), Solution aware, Evaluating (Analyzer on their own property), Activated (finds a segment premium or a visual comp that changes a price), Habit (weekly check of rolling windows), Paid, Advocate.

**Critical success factor:** the first forecast lands in a covered market. A first run on an uncovered address (D-Q28) loses the prospect.

---

## 14. Campaign, asset, and experiment plan

Campaigns: `reference/marketing-campaigns.md`. Content engine: `reference/content-engine.md`. Innovation accounting: `reference/innovation-accounting.md` and `innovation/`.

**Campaigns (WORKING, priority order):**
1. **Design-partner program.** Ten investors in covered metros run live deals through the Predictor with the founder. Output: proof points, objections, activation definition.
2. **"Underwrite the room" education series.** How to underwrite a rent-by-the-room deal: room mix, bathroom pressure, fill speed, garage conversion, DSCR. Product walkthroughs with blurred data.
3. **"Show your work" trust campaign.** Demos built on the transparency design: formula, support, confidence, reconciling numbers.
4. **Operator benchmarking.** "How does your house compare?" built on the Analyzer, for Audience B.
5. **Market intelligence content.** Blocked until data rights are confirmed (G11, G12).

**Innovation accounting (DECIDED operating model).** Every activity goes into `ops/activity-log.md`, every market input into `ops/signal-log.md`. Leap-of-faith assumptions live in `innovation/assumptions.md`, experiments with pre-set thresholds in `innovation/experiments.md`, and the metric tree with baselines in `innovation/metrics.md`. Riskiest assumptions today: data rights (R1), coverage depth in target metros (R2), investors underwriting real deals with room-level evidence (A1), and willingness to pay for the Deal Calculator (A3).

---

## 15. Quick-reference execution cheatsheet

- **One-line positioning:** Room-level market intelligence and underwriting for US rent-by-the-room investors, with the evidence on screen.
- **Flagship differentiator:** a forecast for any US address that prints its formula, support level, comp distance, and confidence, and labels fallback support where evidence is thin.
- **Table stake to win:** markets, maps, property search, deal calculator.
- **Top-of-funnel hook:** "Underwrite the room, not just the house."
- **Audiences:** acquiring investors (primary), operating hosts (secondary). Never blended.
- **Geography:** US Sun Belt metros, starting with the seven presets.
- **Proof points on file:** product facts only (Section 5 trust design). Customer proof: none.
- **Signature reframe:** "When the evidence is thin, RoomIQ says so."
- **Primary rival:** the spreadsheet plus a platform host calculator.
- **Channels in (WORKING):** founder-led demos, education content, communities, product-led trial.
- **Channels not yet:** paid ads, cold outreach at volume.
- **Do not say:** accurate, complete coverage, data source names, income, guaranteed, AI-powered, prices.
- **Always say it with:** units and windows, the fallback clause, the as-of date, "not financial advice" next to deal math.
- **Demo in:** Dallas, Austin, Houston, Atlanta, Phoenix, Tampa. **Never demo:** an uncovered address, the D-Q26 banner, Deal Calculator defaults.
- **Before shipping:** `python3 tools/brain.py lint <draft>`, then `ops/QA-checklist.md`.

---

*End of the RoomIQ GTM master context. When status changes, update the relevant ledger in `rules/` first, then this file, then `ops/decisions.md`, then the copy.*
