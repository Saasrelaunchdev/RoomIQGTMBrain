# Innovation accounting, the protocol

Load for: planning any experiment, reviewing results, deciding pivot or persevere, and the weekly triage. The files it governs live in `innovation/` and `ops/`. Status: DECIDED operating model (D-12).

## Why RoomIQ needs it
RoomIQ is a shipped product with no customer proof, no measured funnel, and several leap-of-faith assumptions (data rights, coverage depth, willingness to pay). In that state, activity is easy to confuse with progress. Innovation accounting forces every activity to answer one question: what did we learn, and does it move a decision?

## The three steps, mapped to files
1. **Establish the baseline.** Measure where the funnel actually is today. `innovation/metrics.md` holds the metric tree; every baseline starts as "not measured" and is filled only from real data.
2. **Tune the engine.** Run experiments that each target one assumption and one metric, with the success threshold written before the result exists. `innovation/experiments.md`.
3. **Pivot or persevere.** On a fixed cadence, compare results to thresholds and decide. Decisions go to `ops/decisions.md` with the evidence that moved them.

## The data flow (the snowball)
```
ACTIVITY (what we did)        -> ops/activity-log.md
   produces
SIGNAL (what we heard/saw)    -> ops/signal-log.md      triage: NOISE | WATCH | PATCH | AMEND
   moves
ASSUMPTION (what we believe)  -> innovation/assumptions.md  UNTESTED | TESTING | VALIDATED | INVALIDATED
   tested by
EXPERIMENT (pre-registered)   -> innovation/experiments.md  PLANNED | RUNNING | DONE
   produces
LEARNING + DECISION           -> ops/decisions.md       PERSEVERE | PIVOT | ITERATE | KILL
   amends
LEDGERS -> COPY -> ASSETS     -> rules/, ops/copy-bank.md, pages/
   which create the next ACTIVITY
```
Every arrow is a file edit, so git history is the audit trail. `python3 tools/brain.py metrics` rolls the counts up.

## Rules that keep it honest
- **Thresholds before results.** An experiment with no pre-set threshold is an anecdote. Write metric, threshold, sample size, and end date when it is PLANNED.
- **Actionable metrics only.** A metric must be per cohort, per audience, and tied to a decision. Totals (signups, page views, generations) are vanity unless divided by something that matters.
- **One assumption per experiment.** If a result could be explained by two assumptions, split the experiment.
- **Learning counts even when the result is bad.** An INVALIDATED assumption is progress; log it with the same care.
- **No result inflates a claim.** A validated assumption changes a ledger only through the AMEND procedure, and only proof that is permissioned enters `ops/copy-bank.md`.

## Cadence
- Weekly: triage signals, update experiment status, increment WATCH counters.
- Monthly: snapshot (`snapshots/`), compare each metric to its baseline, review assumptions.
- Every 90 days or at a learning milestone: pivot or persevere meeting, logged as a decision.

## Learning milestones (WORKING)
1. Ten design-partner sessions logged with verbatims (EXP-001).
2. Activation defined from evidence and measured on a first cohort.
3. Data rights and coverage confirmed (R1, R2).
4. A backtest published or explicitly deferred (R3).
5. First paid conversions at the Deal Calculator gate (A3).

## Brain health metrics (learning velocity)
Signals logged per week, WATCH items promoted, AMENDs per month, median days from signal to decision, experiments completed per month, assumptions resolved, ledger staleness. These measure whether the brain is compounding. `tools/brain.py metrics` reports them.
