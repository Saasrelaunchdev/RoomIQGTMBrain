# Activity log

Everything the team does that could teach the brain something: demos, calls, content shipped, releases, experiments started, outreach, partnerships, pricing tests, coverage changes. The signal log records what the market said; this log records what we did to make it speak. Pairing the two is what innovation accounting reads.

Newest at the top. Append with `python3 tools/brain.py log-activity` or by hand. Parsed by `tools/brain.py metrics`.

## Format
```
### YYYY-MM-DD | TYPE | short title
**ID:** ACT-NNNN
**What:** one or two sentences
**Audience:** A | B | internal
**Linked:** experiment and assumption IDs, for example EXP-001, A1
**Expected:** what signal or metric this should move, written before the outcome
**Outcome:** filled later, from data; "pending" until then
**Signals logged:** count, or "none"
```

**Types:** DEMO, CALL, CONTENT, COMMUNITY, RELEASE, EXPERIMENT, OUTREACH, PARTNERSHIP, PRICING, COVERAGE, RESEARCH, BRAIN.

---

## Entries

### 2026-11-13 | BRAIN | Phase 9 live test: design-partner invitation
**ID:** ACT-0005
**What:** Produced the Campaign 1 warm invitation using only the brain, then ran lint and the QA checklist
**Audience:** A
**Linked:** EXP-001, A1
**Expected:** Asset passes lint and QA with no fact missing from the brain
**Outcome:** Passed: 0 lint errors, QA ticked, 114-word body after one cut. Missing from the brain: the founder's sign-off name and a booking link (founder inputs; product URL already open in ops/asset-index.md). Asset saved as examples/outreach-warm-design-partner.md.
**Signals logged:** none

### 2026-11-13 | BRAIN | GTM Brain v1.0 built
**ID:** ACT-0004
**What:** Built the RoomIQ GTM Brain from the discovery pack with the go-to-market-brain skill: control layer, reference layer, innovation accounting, adapters for AI tools, CLI, and MCP server.
**Audience:** internal
**Linked:** D-12
**Expected:** every later activity and signal lands in a ledger; founder answers the gap interview
**Outcome:** pending
**Signals logged:** none

### 2026-11-13 | RESEARCH | Founder gap interview prepared
**ID:** ACT-0003
**What:** Batched 21 questions the sources could not answer, each with the working default the brain runs on.
**Audience:** internal
**Linked:** G01 to G21, R1, R2, R3, A3
**Expected:** answers convert WORKING decisions to DECIDED and promote UNVERIFIED capabilities
**Outcome:** pending
**Signals logged:** none

### 2026-11-13 | RESEARCH | Competitive desk scan
**ID:** ACT-0002
**What:** Scanned public pages of platform host tools, STR analytics, whole-unit rent comps, deal calculators, and data vendors.
**Audience:** internal
**Linked:** reference/competitive-analysis.md
**Expected:** a candidate rival set and scoped superlatives
**Outcome:** no direct room-level investor analytics rival found; one platform's host tools benchmark rooms for its own hosts; "the only" claim scoped
**Signals logged:** 2

### 2026-11-10 | RESEARCH | Product discovery capture, batches 01 to 03
**ID:** ACT-0001
**What:** Captured and analyzed 15 screens across the Dashboard, Property Analyzer, and Property Predictor.
**Audience:** internal
**Linked:** D-01, D-02, D-03
**Expected:** a facts-only capability inventory
**Outcome:** 32 features (14 seen, 4 partly seen, 14 button only), 36 QA issues, 26 open questions
**Signals logged:** 7
