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

This project keeps its go-to-market as files, not as tribal knowledge.

For marketing, sales, positioning, messaging, or any customer-facing copy, read
`.claude/skills/go-to-market-brain/SKILL.md` first and follow its procedure. It covers three modes: building a
governed context repository from source material, updating one from a market signal, and
producing an asset against one that exists.

When this project holds a built brain, load its entry file and its `rules/` layer before
suggesting copy. Three rules override any suggestion you would otherwise make: a capability
that is not shipped is never described in the present tense, a number or customer name that
is not in the brain is never written, and every draft passes the brain's `ops/QA-checklist.md`
before it is offered.
<!-- gtm-brain:end -->
