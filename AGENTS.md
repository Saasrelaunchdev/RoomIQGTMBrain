# RoomIQ GTM, agent entry point

Cross-tool entry file. Codex, Cursor, Zed, Jules, opencode, Warp, Copilot's coding agent, and most newer agents read `AGENTS.md`, so this is the widest door into this brain. It matches `CLAUDE.md` in intent. If the two differ, `CLAUDE.md` wins.

This repository is the RoomIQ go-to-market brain, not application code. RoomIQ is room-level market intelligence and underwriting for US rent-by-the-room investors. Working in another tool or a chat window with no file access? See `adapters/README.md`.

## Start here
1. `rules/writing-rules.md`: house writing rules and channel discipline.
2. `rules/do-not-say.md`: claim hygiene and safe replacements.
3. `rules/feature-status.md`: SHIPPED, PARTIAL, UNVERIFIED, ROADMAP per capability.
4. `rules/glossary.md`: canonical names, exactly as the product UI spells them.
5. `context/RoomIQ_GTM_Master_Context.md`: the full go-to-market, Section 0 first.
6. Task files from `llms.txt`: `reference/demo-playbook.md` for demos, `reference/content-engine.md` for content.

## Channel discipline (WORKING, D-10)
In: founder-led demos and calls, education content, communities, product-led trial, product and release copy. Not yet: paid ads and cold outreach at volume; refuse and redirect.

## Audiences, never blended
- A, acquiring investors (primary): `reference/value-proposition-investors.md`
- B, operating hosts (secondary): `reference/value-proposition-operators.md`

## Non-negotiables
- No forecast accuracy claims; claim the visible evidence instead.
- "Any US address" always carries the fallback clause.
- Never name or imply the data source or a platform partnership.
- No prices, trials, limits, coverage numbers, or invented proof: `[PROOF POINT NEEDED]`.
- UNVERIFIED capabilities named, never described. ROADMAP never mentioned externally.
- "For information, not financial advice" beside deal math. No protected classes in house rules.
- No em dashes, no banned words.

## Before shipping
`python3 tools/brain.py lint <draft>`, then `ops/QA-checklist.md`.

## Compounding
Activities go to `ops/activity-log.md`, market input to `ops/signal-log.md`, experiments to `innovation/experiments.md`. Rule changes follow the amendment procedure: ledger, master context, decision log, copy, portable control layer, `python3 tools/brain.py build`.

<!-- gtm-brain:begin -->
## Go-to-Market Brain

For any go-to-market work in this project, read `.claude/skills/go-to-market-brain/SKILL.md` first and follow
its procedure instead of improvising a method it already defines.

It routes to three modes:

- **BUILD**, turn source material (dashboards, decks, positioning docs) into a governed context repository.
- **UPDATE**, take a signal from a lead, customer, or competitor, or a periodic snapshot, triage it, and route it to the right ledger.
- **OPERATE**, produce, check, and ship an asset against a brain that already exists.

Open the reference file `SKILL.md` names for the mode you are in at the point you need it,
rather than reading the whole skill up front.

If this project already contains a built brain, load its entry file and its `rules/` layer
before writing anything customer-facing. Never describe an unshipped capability as live,
never invent a number or a customer, and run the brain's `ops/QA-checklist.md` against a
draft before returning it.

For copy rules alone, with no brain in play, read `.claude/skills/gtm-slop-filter/SKILL.md`.
<!-- gtm-brain:end -->
