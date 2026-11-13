# RoomIQ GTM, agent entry point

This repository is the RoomIQ go-to-market brain: a governed context repository, not application code. You are an AI agent working inside it. Read this file, then follow its pointers. Do not improvise strategy that is already decided here.

RoomIQ is room-level market intelligence and underwriting for US rent-by-the-room investors (Dashboard, Property Analyzer, Property Predictor).

## Read before any customer-facing output
1. `rules/writing-rules.md`: how every word is written.
2. `rules/do-not-say.md`: claims you must never make, and the safe replacements.
3. `rules/feature-status.md`: SHIPPED, PARTIAL, UNVERIFIED, ROADMAP per capability. Check before describing anything.
4. `rules/glossary.md`: product and metric names exactly as the UI spells them.
5. `context/RoomIQ_GTM_Master_Context.md`: the full strategy, when the task needs it. Section 0 first.

`llms.txt` indexes every file. `reference/` is loaded on demand: demos load `reference/demo-playbook.md`; content loads `reference/content-engine.md`.

## Channels (WORKING, D-10)
In: founder-led demos and calls, education content, communities, product-led trial, product and release copy. Not yet: paid ads and cold outreach at volume. If asked for those, say they are out of scope today and offer the nearest in-scope channel.

## Pick the audience first, never blend
- **A, acquiring investors** (primary): `reference/value-proposition-investors.md`
- **B, operating hosts** (secondary): `reference/value-proposition-operators.md`

## Non-negotiables (full detail in rules/)
- No forecast accuracy claims. Claim the visible evidence: formula, support level, comp distance, confidence.
- "Any US address" always carries the fallback clause in the same sentence.
- Never name or imply the data source, or any platform partnership.
- No prices, trials, limits, coverage numbers, testimonials, or outcome metrics. Write `[PROOF POINT NEEDED]`.
- UNVERIFIED capabilities are named, never described. ROADMAP items are never mentioned externally.
- Financial outputs say "for information, not financial advice". House rules never reference a protected class.
- AI concepts are always labeled and watermarked.
- No em dashes, no banned words.

## Before you ship
Run `python3 tools/brain.py lint <draft>`, then `ops/QA-checklist.md`. Name the rule the draft came closest to breaking.

## When something happens
- Something was done (demo, post, release): `ops/activity-log.md`.
- Something was heard or observed: `ops/signal-log.md`, verbatim.
- A rule must change: ledger in `rules/` first, then the master context, then `ops/decisions.md`, then copy, then `adapters/portable-control-layer.md`, then `python3 tools/brain.py build`. Never the other way around.
- An experiment: `innovation/experiments.md`, threshold set before results.

## Skills and tools here
- `.claude/skills/go-to-market-brain/`: the method that built this brain (BUILD, UPDATE, OPERATE).
- `.claude/skills/gtm-slop-filter/`: copy rules.
- `.claude/commands/`: slash commands for the recurring jobs in `prompts/common-tasks.md`.
- `.mcp.json`: the brain as an MCP server (`tools/mcp_server.py`).
