---
trigger: model_decision
description: RoomIQ go-to-market brain. Load before any customer-facing copy, positioning, messaging, release notes, UI strings, or competitive work.
---

## RoomIQ go-to-market brain

The RoomIQ go-to-market lives in `gtm-brain/`. It is the source of truth for positioning, messaging, claims, product status, and voice. Do not restate strategy from memory when the brain settles it. This file is a generated pointer (`tools/brain.py adapters`); edit the brain, not this file.

Before any customer-facing writing (web pages, docs, release notes, UI strings, sales or support text, and LLM output shown to users), read in this order:

1. `gtm-brain/AGENTS.md`, the router.
2. `gtm-brain/rules/writing-rules.md`
3. `gtm-brain/rules/do-not-say.md`
4. `gtm-brain/rules/feature-status.md`
5. `gtm-brain/rules/glossary.md`

Pick one audience and never blend them: acquiring investors (primary) or operating hosts (secondary).

Non-negotiables:
- No forecast accuracy claims. Claim the visible evidence: formula, support level, confidence.
- "Any US address" always carries the fallback clause in the same sentence.
- Never name or imply the data source or a platform partnership.
- No prices, trials, limits, coverage numbers, or invented proof. Write `[PROOF POINT NEEDED]`.
- UNVERIFIED capabilities are named, never described. ROADMAP items are never mentioned.
- No em dashes and none of the banned words in the writing rules.

Run `python3 gtm-brain/tools/brain.py lint <file>` and `gtm-brain/ops/QA-checklist.md` before returning a draft. New market input goes to `gtm-brain/ops/signal-log.md` and work done to `gtm-brain/ops/activity-log.md`, never straight into copy.
