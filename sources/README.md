# Sources, the evidence this brain distills

Load this when a ledger entry is questioned. The argument ends by opening the source.

Everything in `context/`, `rules/`, and `reference/` traces back to the artifacts below. When a source changes, update the master context and the affected ledger in `rules/` in the same change, then record it in `ops/decisions.md`.

## Source manifest

| # | Artifact | Type | What it settles | Dated | Location |
|---|---|---|---|---|---|
| S1 | Screen inventory | Markdown, 15 screens | Verbatim UI copy, every visible number, observed vs inferred capability per screen | 2026-11-10 | `extracted/discovery/screen-inventory.md` |
| S2 | Working notes | Markdown, cross-screen analysis | IA map, glossary draft, data entities, monetization signals, third-party dependencies, 36 QA issues, 26 open questions | 2026-11-10 | `extracted/discovery/working-notes.md` |
| S3 | Feature classification | Markdown | The 32 features (C01 to C32) kept apart from 31 non-feature elements (E01 to E31), with evidence level per feature | 2026-11-10 | `extracted/discovery/feature-classification.md` |
| S4 | Coverage gaps | Markdown | 50 visible-but-unopened controls (A1 to A50) and 14 assumed SaaS screens (B1 to B14) still to capture | 2026-11-10 | `extracted/discovery/coverage-gaps.md` |
| S5 | Discovery README and intake log | Markdown | Batch dates, the facts-only PRD rule, synthesis status | 2026-11-10 | `extracted/discovery/README.md` |
| S6 | Product screenshots, batches 01 to 03 | 15 images (WEBP, PNG) | The primary evidence for S1 to S4 | 2026-11-10 | Kept out of this repo, see below |
| S7 | Competitive desk scan | Web search notes | Candidate competitor set and each rival's public positioning, unverified beyond public pages | 2026-11-13 | `reference/competitive-analysis.md` |
| S8 | GTM Brain skill | Method | The build procedure, file blueprint, compounding protocol | 2026-11-13 | `.claude/skills/go-to-market-brain/` |

## Why the screenshots are not in this repo

The screenshots show third-party listing photos, host display names, and the signed-in account's email address. Rights to show listing photos and host names are an open question (see `ops/decisions.md`, open item on data rights). The brain therefore records their location instead of copying them:

- Repository: `Saasrelaunchdev/roomIQGTMBuild`
- Path: `docs/discovery/screenshots/batch-01/` to `batch-03/`
- Commit at build time: `9ed7a8bfe272bd92b1bdc9e11b84e33e54ceb684`

## How the sources were read

1. Every extract in `extracted/discovery/` was read in full. Nothing was sampled.
2. Two evidence rules from the discovery pack carry into the brain unchanged:
   - **Facts only, traced to a screen.** A capability is described only as far as a screenshot shows it.
   - **Inferred is not observed.** Anything labeled `[Inferred]` or `[Q]` in the sources stays out of the shipped-capability list and becomes an open question or a working hypothesis.
3. Conflicts between sources: none found. The C1 to C62 capability list in `working-notes.md` is superseded by the C01 to C32 list in `feature-classification.md`, which the sources themselves state. The brain uses C01 to C32 everywhere.

## Source gaps (what no artifact settles yet)

Data provenance and rights, coverage numbers, pricing and tiers, the ICP the founder intends, channel mix, any customer proof, forecast accuracy (backtest), and the outputs of the 14 "button only" capabilities. Each is an open item in `ops/decisions.md` and a question in `ops/founder-gap-interview.md`.
