# Review cadence

Who reviews what, how often, and when a file is stale. Proposed 2026-11-13; confirm with G09 and G10. Until then the founder owns every ritual.

## Rituals

| Ritual | Frequency | Owner | Work |
|---|---|---|---|
| Signal triage | Weekly, Monday | Founder | Disposition every new signal, increment WATCH counters, execute PATCHes, update experiment status |
| Activity review | Weekly, Monday | Founder | Fill outcomes for last week's activities; link each to its experiment |
| Ledger sweep | Monthly, first Monday | Founder | Read all four `rules/` files against the product; update `last_reviewed`; expire stale WATCH items |
| Snapshot | Monthly | Founder | Full capture in `snapshots/`, metrics against baselines, ending in what it changed |
| Pivot or persevere | Every 90 days or at a learning milestone | Founder | Compare experiments to thresholds; decision entry either way |
| Master context version | Quarterly, or on any AMEND | Founder | Bump version, refresh `status_notes`, verify sections against the ledgers |
| Brain audit | Quarterly, and in CI on every push | Founder | `python3 tools/brain.py audit`, then produce one live asset using only the brain |
| Adapter check | With the ledger sweep | Founder | `python3 tools/brain.py adapters --check`; run the conformance prompts in one tool |

## Ledger ownership and staleness

| File | Owner | Stale after |
|---|---|---|
| `rules/feature-status.md` | Founder (product) | 30 days, or any release |
| `rules/do-not-say.md` | Founder, plus counsel once engaged | 90 days |
| `rules/glossary.md` | Founder (product) | 90 days |
| `rules/writing-rules.md` | Founder | 180 days |
| `context/RoomIQ_GTM_Master_Context.md` | Founder | 90 days |
| `innovation/assumptions.md` | Founder | 30 days |
| `adapters/portable-control-layer.md` | Founder | Any ledger change |

`rules/feature-status.md` goes stale fastest and does the most damage: it stands between the roadmap and a promise. Any product release triggers a review of it the same day.

## Authority
- A PATCH can be made by anyone producing work, including an AI agent, in a pull request.
- An AMEND to any `rules/` file requires the founder's approval on the pull request.
- A change to positioning, ICP, channel mix, or pricing requires the founder and a dated entry in `ops/decisions.md`.
- Generated files in `dist/` are never edited by hand.

## Order of operations for an AMEND
Ledger in `rules/`, then the master context, then `ops/decisions.md`, then `ops/copy-bank.md` and templates, then `adapters/portable-control-layer.md`, then `python3 tools/brain.py build`, then the affected live surfaces listed in `ops/asset-index.md`.
