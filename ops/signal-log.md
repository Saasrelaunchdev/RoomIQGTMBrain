# Signal log

Raw market input, captured before judgment. Every signal from a prospect, customer, competitor, channel, or the product itself lands here first. Newest at the top. Append with `python3 tools/brain.py log-signal` or by hand in the format below.

**Keep the verbatim.** The words a real buyer used, before we taught them ours, are the most valuable thing a signal carries.

## How to use this file

**Types:** OBJECTION, LANGUAGE, PROOF, STATUS, COMPETITIVE, SEGMENT, CHANNEL, LOSS, RISK.

**Dispositions:**
- `UNTRIAGED`: captured by a tool or a person, awaiting the weekly triage. Never left past one triage cycle.
- `NOISE`: one instance, no pattern. Logged and closed.
- `WATCH (n/N)`: plausible pattern awaiting corroboration. Increment as instances arrive.
- `PATCH`: changes copy, not strategy. Route, edit, done.
- `AMEND`: changes a ledger, a position, or a rule. Full amendment procedure plus a `ops/decisions.md` entry.

**Corroboration thresholds** (proposed 2026-11-13, confirm with G10):

| Signal class | Threshold to act |
|---|---|
| Opinion, preference, language, objection | 3 independent instances within 60 days |
| Verifiable fact: status, proof, competitive, risk | 1 verified instance, act immediately |
| Loss reason | 2 instances, or 1 if the deal was a design partner |
| Channel performance | A full measurement cycle, never a single week |

Default disposition is NOISE. Triage runs weekly (`ops/review-cadence.md`). A WATCH item with no increment in two cycles expires to NOISE, and the expiry is written here.

---

## Entries

### 2026-11-13 | COMPETITIVE | desk scan, DealCheck public site
**Verbatim:** "buy & hold, rehab & hold, Airbnb, vacation and other types of rental properties"
**Context:** Property types a leading deal calculator lists; coliving is not among them.
**Disposition:** PATCH
**Routed to:** reference/competitor-battlecards.md

### 2026-11-13 | COMPETITIVE | desk scan, marketplace host help pages
**Verbatim:** "x% of metro area avg"
**Context:** A marketplace's host Rooms tab shows each room's price against the metro average. Room-level benchmarking exists inside at least one platform, for its own hosts.
**Disposition:** AMEND
**Routed to:** rules/do-not-say.md (scoping of "the only room-level analytics tool"), reference/competitive-analysis.md

### 2026-11-10 | SEGMENT | product UI, screen 12
**Verbatim:** "Property facts that investors actually underwrite: type, bedroom count, bathroom count, and gross size."
**Context:** The product's own copy addresses investors; the Predictor nudges toward "investor-grade scenarios".
**Disposition:** AMEND
**Routed to:** ops/decisions.md D-07, reference/icp-personas.md

### 2026-11-10 | RISK | product capture, screen 15
**Verbatim:** "INTEREST RATE" field reading 22% in the Deal Calculator capture; "VACANCY 5%" applied to revenue that already includes 89.5% occupancy
**Context:** Possible wrong default and possible double counting in a Pro financial output.
**Disposition:** AMEND
**Routed to:** rules/feature-status.md (D-Q30, D-Q31), reference/demo-playbook.md

### 2026-11-10 | RISK | product capture, screens 11 and 14
**Verbatim:** "No active properties found within ~3 mi of this address." then "Broader fallback evidence was used; median comp distance is 82.88 mi."
**Context:** An Upper East Side address forecast at $282 per room per week on distant comps. Labeled Low confidence, but a poor first run for a prospect.
**Disposition:** AMEND
**Routed to:** rules/do-not-say.md (fallback clause), ops/decisions.md D-06, innovation/assumptions.md R2

### 2026-11-10 | RISK | product capture, screen 14
**Verbatim:** "Only 1 of 3 bedrooms have a room entry, so the forecast is based on the full bedroom count with typical rooms."
**Context:** The formula on the same screen uses 1.0 active rooms ($1,098). Copy and math disagree on the core output.
**Disposition:** AMEND
**Routed to:** rules/feature-status.md (D-Q26), reference/demo-playbook.md

### 2026-11-10 | RISK | product capture, screen 08
**Verbatim:** "Rooms across the market that look like this one."
**Context:** Two of twelve matches were empty-closet photos at 95 percent match, and results spanned Texas and Florida.
**Disposition:** PATCH
**Routed to:** reference/demo-playbook.md, rules/feature-status.md (D-Q18)

### 2026-11-10 | PROOF | product capture, screens 09, 10, 14
**Verbatim:** "AI-GENERATED - NOT ACTUAL PROPERTY CONDITION" and "Revenue assumptions, not a calibrated prediction interval."
**Context:** The product discloses its own limits on screen. Product-fact proof of the transparency posture, not customer proof.
**Disposition:** PATCH
**Routed to:** ops/copy-bank.md (product facts)

### 2026-11-10 | STATUS | product capture, batches 01 to 03
**Verbatim:** "Features and capabilities (32)" with evidence "14 seen, 4 partly seen, 14 button only"
**Context:** The full capability inventory from 15 screens.
**Disposition:** AMEND
**Routed to:** rules/feature-status.md, ops/decisions.md D-03

---

*An empty run of weeks in this log after demos begin means the loop is not running.*
