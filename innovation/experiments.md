# Experiment ledger

Every experiment states its assumption, metric, threshold, sample, and end date before it starts. Results are written once, verbatim from the data, then the decision. Parsed by `tools/brain.py` (heading `### EXP-NNN | title`, fields `- **Field:** value`). Protocol: `reference/innovation-accounting.md`.
last_reviewed: 2026-11-13

Statuses: **PLANNED**, **RUNNING**, **DONE**, **BLOCKED**. Decisions: **PERSEVERE**, **PIVOT**, **ITERATE**, **KILL**, or **PENDING**.

---

### EXP-001 | Design-partner underwriting sessions
- **Status:** PLANNED
- **Tests:** A1, A2
- **Audience:** A, acquiring investors in covered metros
- **Method:** 30-minute founder session per investor; they bring a live deal; the founder runs it through the Predictor with them.
- **Metric:** share of sessions where the investor asks to run a second address or requests access, within 7 days
- **Threshold (set before results):** at least 6 of 10 sessions
- **Sample:** 10 sessions
- **End:** 2027-01-15
- **Also capture:** every objection and phrase verbatim into `ops/signal-log.md`; what else they looked at (competitive)
- **Result:** none yet
- **Decision:** PENDING

### EXP-002 | Forecast backtest
- **Status:** PLANNED
- **Tests:** R3
- **Audience:** internal, then lenders if it passes
- **Method:** hold out tracked properties with at least 180 days of history; forecast from earlier evidence; compare to observed.
- **Metric:** median absolute percentage error by confidence label; share of outcomes inside the illustrative scenarios
- **Threshold (set before results):** founder sets before running; record here first
- **Sample:** all tracked properties in the seven preset metros meeting the history rule
- **End:** founder to set
- **Result:** none yet
- **Decision:** PENDING

### EXP-003 | Deal Calculator paywall interest
- **Status:** PLANNED
- **Tests:** A3
- **Audience:** A
- **Method:** in design-partner sessions, show the Pro gate at the Deal Calculator and ask a fixed willingness-to-pay question; no prices quoted until D-11 closes.
- **Metric:** share who say they would pay for Pro to use the Deal Calculator on their next deal
- **Threshold (set before results):** at least 4 of 10
- **Sample:** the EXP-001 cohort
- **End:** 2027-01-15
- **Result:** none yet
- **Decision:** PENDING

### EXP-004 | Education content in investor communities
- **Status:** PLANNED
- **Tests:** G1, G2
- **Audience:** A
- **Method:** publish 6 "Underwrite the room" pieces over 6 weeks; answer community questions with worked examples; one call to action per piece.
- **Metric:** demos booked from content and community per week, by piece
- **Threshold (set before results):** at least 2 qualified demos per week by week 6
- **Sample:** 6 pieces, 6 weeks
- **End:** 6 weeks after the first piece ships
- **Result:** none yet
- **Decision:** PENDING

### EXP-005 | Coverage audit of preset metros
- **Status:** PLANNED
- **Tests:** R2
- **Audience:** internal
- **Method:** forecast 20 randomly chosen single-family addresses per preset metro; record support level and confidence.
- **Metric:** share of addresses with better than Low confidence and no fallback support, per metro
- **Threshold (set before results):** at least 60 percent in a metro to keep it in demos and targeting
- **Sample:** 140 addresses
- **End:** 2026-12-15
- **Result:** none yet
- **Decision:** PENDING

### EXP-006 | Operator pricing change
- **Status:** BLOCKED
- **Tests:** A4, A5
- **Audience:** B, operating hosts
- **Method:** five operators review their own comparable property in the Analyzer; follow up after 14 days.
- **Metric:** operators who changed a room price or planned an upgrade because of what they saw
- **Threshold (set before results):** at least 2 of 5
- **Sample:** 5 operators
- **End:** set when unblocked
- **Blocked by:** D-07 puts operators second; starts after EXP-001
- **Result:** none yet
- **Decision:** PENDING
