<!-- roomiq-gtm-brain:begin -->
## RoomIQ go-to-market brain

The RoomIQ go-to-market lives in this repository. It is the source of truth for positioning, messaging, claims, product status, and voice. Do not restate strategy from memory when the brain settles it. This file is a generated pointer (`tools/brain.py adapters`); edit the brain, not this file.

Before any customer-facing writing (web pages, docs, release notes, UI strings, sales or support text, and LLM output shown to users), read in this order:

1. `AGENTS.md`, the router.
2. `rules/writing-rules.md`
3. `rules/do-not-say.md`
4. `rules/feature-status.md`
5. `rules/glossary.md`

Pick one audience and never blend them: acquiring investors (primary) or operating hosts (secondary).

Non-negotiables:
- No forecast accuracy claims. Claim the visible evidence: formula, support level, confidence.
- "Any US address" always carries the fallback clause in the same sentence.
- Never name or imply the data source or a platform partnership.
- No prices, trials, limits, coverage numbers, or invented proof. Write `[PROOF POINT NEEDED]`.
- UNVERIFIED capabilities are named, never described. ROADMAP items are never mentioned.
- No em dashes and none of the banned words in the writing rules.

Run `python3 tools/brain.py lint <file>` and `ops/QA-checklist.md` before returning a draft. New market input goes to `ops/signal-log.md` and work done to `ops/activity-log.md`, never straight into copy.
<!-- roomiq-gtm-brain:end -->

<!-- gtm-brain:begin -->
## Go-to-Market Brain

Before any go-to-market work in this project, read `.claude/skills/go-to-market-brain/SKILL.md` and follow it.
It routes to BUILD (source material becomes a governed context repository), UPDATE (a market
signal or snapshot gets triaged into a ledger), or OPERATE (produce and QA an asset against a
brain that exists). Load the reference file it names for that mode when you reach it.

Where a built brain exists, its entry file and `rules/` layer load before any customer-facing
writing. No unshipped capability in the present tense, no invented numbers, and the brain's
`ops/QA-checklist.md` runs before a draft comes back.
<!-- gtm-brain:end -->
