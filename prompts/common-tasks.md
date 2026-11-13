# Prompt library, common RoomIQ GTM tasks

Filled, runnable prompts for recurring jobs. Each assumes the agent loaded the router (`CLAUDE.md` or `AGENTS.md`) and the four `rules/` files. Copy, fill the brackets, run. In Claude Code the same prompts exist as slash commands in `.claude/commands/`.

There is no paid ad or cold outreach in this go-to-market today (D-10), so there are no prompts for them. If asked, the agent says so and offers the nearest in-scope channel.

## Draft a landing page
"Draft a landing page for the [investors / operators] audience at stage [3 / 4], following `templates/landing-page.md` and the voice of `examples/landing-hero-investors.md`. Use only that audience's value proposition file. Every capability must be checked in `rules/feature-status.md`. Run `python3 tools/brain.py lint` on the draft, then `ops/QA-checklist.md`, and list every capability you mentioned with its status."

## Write a demo script
"Write a [20-minute / 2-minute] demo script for [investors / operators] in [covered metro], following `templates/demo-script.md` and `reference/demo-playbook.md`. Avoid every landmine in the playbook. Write for the ear. Then QA it."

## Write an education article
"Plan, then write, a [worked example / method piece / myth check / honest limitation] article for [audience] answering '[search question]', following `templates/seo-article.md` and `reference/content-engine.md`. Show the plan first and wait for approval. No market statistics as data (G11, G12)."

## Answer a community question
"Here is a question from [community]: '[paste verbatim]'. Draft an answer following `templates/community-answer.md`: answer fully without the product, one worked number, disclosure if RoomIQ is mentioned. Then log the question as a LANGUAGE signal in `ops/signal-log.md`."

## Handle an objection
"A prospect said: '[verbatim]'. Draft the response from `reference/objection-handling.md`, honest about anything unshipped or unknown. If the objection is not in the file, say so, draft a candidate answer, and log it as an OBJECTION signal."

## Prepare for a competitive call
"I have a call with an investor who uses [rival or spreadsheet]. Using `reference/competitor-battlecards.md`, give me the rival's real strength, its gap for this buyer, and how RoomIQ wins, in three spoken lines. Check every superlative against `rules/do-not-say.md`."

## Review product copy
"Review these UI strings [paste or path] against `rules/glossary.md`, `rules/do-not-say.md`, and `templates/in-app-copy.md`. Return a table: location, current, proposed, rule. Flag any string whose explanation disagrees with the number it explains."

## Write a release note
"Capabilities [IDs] changed in this release: [what changed]. First propose the edits to `rules/feature-status.md` and the known-defects list. Then draft the note with `templates/release-note.md`. Do not draft until the ledger edits are listed."

## Log a signal
"Log this in `ops/signal-log.md`: [paste note, quote, or competitor move]. Keep the verbatim. Classify the type, assign a disposition with the thresholds in that file, check whether it corroborates an open WATCH, and if it is a PATCH or AMEND, list exactly which files change. Also note which assumption in `innovation/assumptions.md` it bears on."

## Log an activity
"Log this activity in `ops/activity-log.md`: [what was done]. Assign the next ACT id, the experiment and assumption it serves, and the expected signal, written now, before the outcome."

## Design an experiment
"Design an experiment for assumption [ID] in `innovation/assumptions.md`. Write it in the format of `innovation/experiments.md`, with metric, threshold, sample, and end date set before any result. One assumption only."

## Weekly triage
"Run the weekly triage: read new entries in `ops/signal-log.md` and `ops/activity-log.md` since [date], update dispositions and WATCH counters, update experiment statuses, and list proposed PATCHes and AMENDs with their files. Then run `python3 tools/brain.py metrics` and summarize learning velocity."

## Take a snapshot
"Build this month's snapshot in `snapshots/` from [data]. Fill every section of `snapshots/2026-11-13-baseline.md`'s shape, diff section 6 against `rules/feature-status.md`, compare metrics to baselines in `innovation/metrics.md`, and end with what this changes, including 'no ledger change this period' if that is the honest answer."

## Apply founder answers
"The founder answered [G-ids]: [answers]. Apply each as an AMEND in order: `rules/`, the master context, `ops/decisions.md`, copy bank and templates, `adapters/portable-control-layer.md`, then run `python3 tools/brain.py build` and `audit`. Report what changed and what did not."

## Audit the brain
"Run `python3 tools/brain.py audit`, fix what it reports, then produce one real asset using only the brain and QA it. Report anything the brain could not supply."
