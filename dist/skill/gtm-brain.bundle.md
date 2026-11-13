# go-to-market-brain, single-file bundle

Generated 2026-11-13 in `compact` mode from the go-to-market-brain skill.

You are reading a directory flattened into one document because the tool you are running in cannot open files. Each section below was a separate file. The section headed `SKILL.md` is the procedure and everything after it is the detail that procedure names. Read the procedure, decide which mode you are in, then read only the section it points at.

Where the text says to open a file, look for that path as a section heading here instead. Where it names a script you cannot run, do the work the script describes by hand and say that you did.

Contents:

- `SKILL.md`
- `reference/blueprint.md`
- `reference/extraction.md`
- `reference/ledgers.md`
- `reference/compounding.md`
- `reference/operating.md`
- `reference/portability.md`
- `adapters/skill/system-prompt.md`

---

## SKILL.md

*When to use this: Turn a go-to-market into a Go-to-Market Brain, a governed context repository that any AI agent or human operator loads as the single source of truth for strategy, messaging, claims, and voice. Use this skill when the user has GTM dashboards, strategy decks, positioning docs, ICP research, competitive analysis, value proposition frameworks, customer journey maps, or a campaign plan and wants them turned into a repo, a context repo, a GTM brain, a command center, a brand or messaging source of truth, or agent guardrails. Also use it to operate an existing brain: logging a signal from a lead, prospect, customer call, churn reason, review, or competitor move and deciding whether it changes positioning, ICP, messaging, or the claim ledger; capturing a periodic snapshot; updating a feature or claim status; or auditing a brain for staleness and broken guardrails. Also use it to wire a brain, or this procedure, into another agent tool: Codex, Cursor, Windsurf, Copilot, Gemini, Grok, a custom GPT, or a chat window with no file access. Triggers include "GTM brain", "go-to-market repo", "context repo", "single source of truth for our messaging", "turn these dashboards into a repo", "rules so the AI stops overclaiming", "did this change our positioning", "log this customer signal", "make this work in Codex", "port the brain to another agent".*

# Go-to-Market Brain

A Go-to-Market Brain is a plain-text repository that holds one company's entire go-to-market in a form an AI agent can load and execute against without re-deriving anything, and that a human operator can use as a command center for decisions. It is content and context, not application code.

It solves four problems at once. Strategy stops living in one person's head and in scattered files. Every asset inherits the same positioning and voice. Agents stop overclaiming, because what may be said is written down and checked. And the whole thing compounds: every lead conversation, customer signal, and periodic snapshot feeds back into the ledgers, so the brain gets sharper with use instead of going stale.

## Route first

Three modes. Decide which one you are in before doing anything.

| The user has | Mode | Go to |
|---|---|---|
| Source material and no brain yet | **BUILD** | Phases 1 to 9 below |
| A brain, plus new input: a call note, an objection, a churn reason, a competitor move, a shipped feature, a metrics snapshot | **UPDATE** | `reference/compounding.md` |
| A brain, and wants an asset produced, reviewed, or shipped | **OPERATE** | `reference/operating.md` |

If a brain exists, never write customer-facing output without loading its entry file and control layer first. That is the point of the brain.

## The three-layer architecture

Everything in the build serves one of three layers. Keep them distinct.

1. **Control layer.** Small, authoritative, checked on every task: the entry files, the rules, the QA checklist. This is what governs output. Keep it short enough that loading it costs nothing.
2. **Reference layer.** Large, authoritative, loaded on demand: the master context and one file per source artifact. This is the brain's memory.
3. **Execution layer.** Templates, examples, prompts, finished pages. This is how work gets produced fast and on-voice.

Under all three sits the **state layer** (`ops/` and `snapshots/`), which records what was decided, what language is approved, what has been heard from the market, and when each ledger was last reviewed. The state layer is what makes the brain compound.

Full file map, purposes, and size budgets: `reference/blueprint.md`.

## BUILD: nine phases

Work in order. Do not skip Phase 2, and do not start Phase 4 before Phase 3 is drafted.

### Phase 1. Inventory the sources
Run `scripts/extract_sources.py <source_dir> <out_dir>` to convert XLSX, DOCX, PPTX, PDF, and CSV into readable Markdown. Read every extract. Then write a source manifest: for each artifact, its name, type, what decision it settles, and its date. Flag any two artifacts that disagree, and resolve the conflict explicitly with the user rather than silently picking one.

Method and the source-to-file mapping table: `reference/extraction.md`.

### Phase 2. Interview for gaps
The sources will not carry everything. Ask only for what is missing, in one batched round, and prefer questions whose answers change the build. The standing gap list is in `reference/extraction.md`. The four that are almost always missing: the channel mix and which channels are forbidden, the exact permissioned proof points, feature or delivery status by capability, and the words this brand refuses to use.

If the user cannot answer something, record it as an open question in `ops/decisions.md` under "Open, owned elsewhere" rather than inventing an answer. An invented answer becomes a rule, and a wrong rule propagates into every asset.

### Phase 3. Draft the master context
One file, `context/<Project>_GTM_Master_Context.md`, that distills every source into a single read. Numbered sections, YAML frontmatter carrying version, last updated, and status notes, and Section 0 written as operating instructions to the agent reading it.

Target 300 to 500 lines. If it runs longer, you are transcribing instead of distilling. Section order and the frontmatter contract: `reference/blueprint.md`. Skeleton: `assets/context/master-context.md`.

### Phase 4. Derive the control layer
Lift the governing parts of the master context out into standalone files under `rules/`. This duplication is deliberate: the master is the reference brain, the rules are the layer that gets checked on every single task. The master stays authoritative when they diverge, and both get updated together.

Derive in this order, because each depends on the last:
1. `rules/glossary.md`, the canonical vocabulary. Names first, since every other rule refers to things by name.
2. `rules/feature-status.md`, what is shipped versus in build versus roadmap. Rename it to fit the business: a services firm ships capabilities, not features.
3. `rules/do-not-say.md`, the claim hygiene spine. Two columns: forbidden or risky on the left, the safe replacement on the right. Never a bare prohibition without a replacement.
4. `rules/writing-rules.md`, mechanics, tone, channel discipline, and the approved signature lines.
5. `ops/QA-checklist.md`, which is the mechanical, tickable mirror of the four files above. If a rule cannot be checked, it is not a rule yet.

Derivation method, including how to turn a competitive claim into a scoped safe form: `reference/ledgers.md`.

### Phase 5. Build the reference layer
One short file in `reference/` per source artifact, each opening with a line naming the source it distills and what to load it for. Then add the synthesized files the sources imply but do not contain, typically battlecards, objection handling, and a channel engine for whatever the primary channel is.

Each file earns its place by answering a question an operator actually asks. Sixty lines is usually enough. If a reference file is only a restatement of the master context, cut it.

### Phase 6. Build the execution layer
Instantiate a template per channel in the mix, and only those. A template the business will never use is noise that dilutes retrieval. Start from `assets/templates/`, then rewrite each one in the project's own vocabulary and guardrails.

Write at least one gold-standard example per major asset type into `examples/`. Examples are the few-shot voice reference and they do more work than any amount of tone description. If no approved asset exists yet, write one and get it approved before the brain is declared built.

Fill `prompts/common-tasks.md` with a filled, ready-to-run prompt per recurring job.

### Phase 7. Build the routers, and the doors for other tools
Three entry files, all small, all pointing at the same load order, all restating the non-negotiables in short form: `CLAUDE.md`, `AGENTS.md` (for Codex, Cursor, Zed, opencode, and the rest of the tools that read AGENTS.md), and `llms.txt` (a linked index of every file). Add `README.md` for humans: what this is, how it is organized, what it is for, and the maintenance rule.

Keep each router under about sixty lines. The always-loaded layer must stay small and authoritative. Everything else is pulled in on demand.

Then ask which tools the team actually runs, and write one pointer file per tool into `adapters/`, from the templates in `adapters/brain/`. A guardrail that loads in one tool and not the others is not a guardrail: the person on the tool you skipped ships copy nothing checked. For anyone working in a chat window with no file access, render the dated portable control layer. Method, the tool table, and how to keep adapters from drifting: `reference/portability.md`.

### Phase 8. Install the compounding loop
This is what separates a brain from a folder of documents. Create `ops/signal-log.md`, `ops/decisions.md`, `ops/copy-bank.md`, `ops/asset-index.md`, `ops/review-cadence.md`, and the `snapshots/` directory. Seed the decision log with every strategic call the sources already settled, each with its date, verdict, and rationale, so settled strategy is never relitigated.

Set the review cadence and the corroboration thresholds with the user. Full protocol: `reference/compounding.md`.

### Phase 9. Audit and hand off
Run `scripts/audit_brain.py <brain_dir>`. It checks required files, broken relative links, files missing from the index, size budgets, banned words and forbidden mechanics inside the brain's own prose, and ledger staleness.

Then run a live test: produce one real asset using only the brain, and run it through `ops/QA-checklist.md`. If the asset needed a fact that is not in the brain, the brain is not finished. Fix it, then hand off.

## Invariants

These hold for every brain, regardless of company, category, or channel mix.

- **Ledgers before copy, always.** When status changes, update the ledger, then let copy follow. Never the other way around.
- **Every capability carries a status flag.** Shipped, partial, in build, or roadmap. No claim about an unshipped capability without the flag attached.
- **Every prohibition carries a replacement.** A do-not-say entry without a "say instead" gets ignored under deadline pressure.
- **Audience before writing.** If the business has more than one audience, they get separate value propositions and are never blended in one asset. Pick first.
- **Proof points are a closed set.** Only real, permissioned, sourced facts. The brain names them explicitly, and anything not on the list is fabrication.
- **Scope every superlative.** "Only," "first," "best," and "never" get checked against the claim ledger and narrowed to the form that survives scrutiny.
- **Name the mode when a claim is conditional.** If a claim is true in one configuration and false in another, the mode is part of the claim.
- **Channel discipline is a rule, not a preference.** If the GTM excludes a channel, the brain refuses to produce for it and says so.
- **The always-loaded layer stays small.** Routers and rules are short. Depth lives in files loaded on demand.
- **The brain is tool-neutral.** It is Markdown. Any agent that can read a file can be pointed at it, and the guardrails reach every tool the team runs, not just the one that built the brain.
- **Decisions are dated and never relitigated.** Including an explicit note of what the decision did not change.

## Files in this skill

| File | Load it when |
|---|---|
| `reference/blueprint.md` | Building or extending the file structure. Full map, purposes, load policy, size budgets. |
| `reference/extraction.md` | Phase 1 and 2. Reading source material, mapping artifacts to files, the gap interview. |
| `reference/ledgers.md` | Phase 4. Deriving glossary, status ledger, claim ledger, writing rules, QA checklist. |
| `reference/compounding.md` | UPDATE mode. Signal intake, triage, routing, snapshots, review cadence. |
| `reference/operating.md` | OPERATE mode. Producing, checking, and shipping an asset against a built brain. |
| `reference/portability.md` | Phase 7. Making the brain load in every tool the team runs, not only this one. |
| `reference/worked-example.md` | Any phase, for a real instance of the blueprint end to end. |
| `assets/` | Phase 3 to 8. Skeletons to copy and rewrite in the project's own terms. |
| `adapters/` | Phase 7. Pointer templates per tool, for the brain and for this skill. |
| `scripts/extract_sources.py` | Phase 1. Converts XLSX, DOCX, PPTX, PDF, CSV to Markdown. |
| `scripts/audit_brain.py` | Phase 9 and every review cycle. Lints a built brain. |
| `scripts/bundle_skill.py` | When a tool cannot read files. Flattens this skill into one pasteable document. |

## If you are not running in Claude Code

Nothing here is Claude-specific. You are reading Markdown, and every path above is relative to this skill's own directory, so the procedure works wherever these files landed. Two adjustments:

- **You cannot open a file.** Everything you need is in the bundle you were given. Where the text says to open `reference/x.md`, look for that path as a section heading in the same document. Where it names a script, do the work the script describes by hand and say that you did.
- **Someone wants this wired into their tool.** Use the pointer templates in `adapters/skill/`, substituting the real install path for `{{SKILL_PATH}}` and `{{SKILLS_DIR}}`. The per-tool recipes, and the five-prompt check that proves the wiring works, are in `PORTING.md` at the root of the GTM Brain repository.

Templates are starting points, never final output. A brain that reads like a filled-in template is a brain nobody trusts. Rewrite every line in the project's own vocabulary, and delete every section the project does not need.

---

## reference/blueprint.md

# Blueprint, the file map of a Go-to-Market Brain

The full structure, what each file holds, when it loads, and how big it is allowed to get. Build only what the project needs, but do not drop a layer.

```
<project>-gtm/
  CLAUDE.md                                  router, Claude Code and Claude apps
  AGENTS.md                                  router, tools that read AGENTS.md
  llms.txt                                   machine-readable index of every file
  README.md                                  human orientation and ROI
  context/
    <Project>_GTM_Master_Context.md          the distilled source of truth
  rules/
    writing-rules.md                         how every word is written
    do-not-say.md                            claim hygiene, forbidden and safe forms
    feature-status.md                        shipped / partial / in build / roadmap
    glossary.md                              canonical vocabulary
  reference/
    <one file per source artifact>           positioning, ICP, competitive, journey, value props
    <synthesized files>                      battlecards, objection handling, channel engine
  templates/
    <one per channel in the mix>             skeletons to fill, not blank pages
  examples/
    <one per major asset type>               approved gold standard, the voice reference
  pages/
    <finished long-form assets>              shipped copy, updated rather than rewritten
  prompts/
    common-tasks.md                          filled prompts for recurring jobs
  ops/
    copy-bank.md                             approved language, reusable verbatim
    decisions.md                             what was decided, when, and why
    signal-log.md                            raw market input and its disposition
    asset-index.md                           where sources and surfaces live
    QA-checklist.md                          the pre-ship gate
    review-cadence.md                        who reviews what, how often
  snapshots/
    YYYY-MM-DD-<label>.md                    dated state captures and what they changed
  adapters/
    <one pointer file per tool in use>       Codex, Cursor, Windsurf, Copilot, Gemini
    portable-control-layer.md                dated, for chat models with no file access
  sources/
    raw/                                     original dashboards and decks
    extracted/                               machine-readable text dumps
```

## Layer by layer

### Routers, always loaded

Three files, same content, three audiences. They are traffic control, not content. If a router starts explaining strategy, move that text into `context/` and leave a pointer.

Each router carries five things and nothing else: what this repo is, the numbered read order for the control layer, the audience split, the non-negotiables in short form, and the pre-ship instruction. Budget sixty lines. `CLAUDE.md` wins if the routers ever disagree, and `AGENTS.md` should say so.

`llms.txt` is different in kind: a linked index of every file with a one-line purpose each, grouped by layer. It exists so an agent can decide what to open without opening anything. Every new file gets a line here or it is effectively invisible.

`README.md` is for people. What the company is, why the GTM is shaped this way, the folder table, the use cases, where the return comes from, and the maintenance rule.

### adapters/, one door per tool

Pointer files, about twenty lines each, that make a tool other than Claude Code load the control layer before it writes. One per tool someone on the team actually runs, and no more, since an adapter for a tool nobody uses goes stale unnoticed. An adapter never carries strategy, a claim, or a status: it names the load order and stops. The single exception is `portable-control-layer.md`, which carries content because a chat model cannot follow a pointer, and is therefore dated and regenerated whenever a ledger changes.

Templates and the tool table: `portability.md`.

### context/, the source of truth

One file. Every source artifact distilled into numbered sections that an agent can read once and execute from.

Frontmatter contract:

```yaml
---
title: <Project> Go-To-Market Master Context
project: <Project>
type: gtm_context_file
purpose: Single source of truth for any AI agent executing <Project> go-to-market work.
version: 1.0
last_updated: YYYY-MM-DD
status_notes: <the live caveats, what is undecided, what is not yet true>
canonical_vocabulary: <comma-separated canonical terms>
---
```

`status_notes` is the most useful field in the brain. It is where an agent learns, in one line, what it is not allowed to assume. Keep it current.

Section order, adapt names but keep the sequence, because it moves from governance to strategy to execution:

0. Agent operating instructions. What this file is, how to use it, the hard guardrails.
1. House writing rules.
2. Canonical vocabulary.
3. Status ledger for capabilities.
4. Claim hygiene ledger.
5. What the product or service actually is.
6. Feature or capability matrix, what leads and what is table stakes.
7. Competitive market analysis.
8. Ideal customer profile and buying committee.
9. Strategic verdicts already decided.
10. Value proposition, audience one.
11. Value proposition, audience two.
12. Positioning statement.
13. Customer journey funnels.
14. Campaign and asset plan.
15. Quick-reference execution cheatsheet.

Section 0 is written in the second person to the agent. Section 15 is a flat list of the twenty facts an operator looks up most, so common questions never require a full read.

Budget 300 to 500 lines. Over 500 means transcription, not distillation.

### rules/, the control layer

Four files, each short enough to load on every task. They repeat material from the master context on purpose. The master is the reference brain, the rules are the enforcement layer, and enforcement has to be cheap to load or it does not happen.

- `glossary.md`. A table of canonical terms and the rule for each, including the terms that are banned because a partner or platform owns them. Ends with the distinction that must never blur, if the business has one.
- `feature-status.md`. Grouped by capability area, one line per capability, status flag in caps. Opens with the legend and the instruction to update this file before any copy follows. Name it `capability-status.md` or `service-status.md` where "feature" does not fit.
- `do-not-say.md`. Three parts: hard bans as a two-column table, channel-specific bans, and claims that need scoping with the safe form spelled out. Then any historical or reputational material that must be handled rather than repeated.
- `writing-rules.md`. Mechanics, tone, medium-specific rules such as writing for the ear, claim discipline, channel discipline, the approved signature lines, and formatting.

Budget eighty lines each. A control file nobody finishes reading controls nothing.

### reference/, loaded on demand

One file per source artifact, plus synthesized files. Each opens with one line naming what to load it for and which source it distills, so an agent can skip it accurately.

Typical set:

| File | Answers |
|---|---|
| `positioning.md` | What category are we in and what do we lead on |
| `positioning-verdict.md` | The strategic fork that was settled, and the reasoning |
| `icp-personas.md` | Who we sell to, who blocks, what wins each level |
| `competitive-analysis.md` | Market shape, scoring vectors, the wedge |
| `competitor-battlecards.md` | Per rival: strength, gap, how we win |
| `feature-matrix.md` | What leads messaging, what is table stakes |
| `customer-journey.md` | Stage by stage mindset, asset, KPI, owner |
| `value-proposition-<audience>.md` | Pillars and approved reasons to believe, per audience |
| `objection-handling.md` | The recurring pushbacks and the honest answers |
| `marketing-campaigns.md` | The campaign structure and asset backlog |
| `<channel>-engine.md` | The strategy and method behind the primary channel |

The channel engine does the most work of any synthesized file. Whatever the GTM runs on, that channel gets a file holding its thesis, its archetypes, and its plan, write, and edit methodology, and every template for that channel points back to it.

Budget sixty lines each.

### templates/, examples/, prompts/, the execution layer

Templates are shape, not content: the sections, the order, the fields to fill, and the guardrails at the bottom. Every template ends with a guardrail line pointing at the rules files, because a template is where a hurried operator stops reading.

Examples are approved output, matched one to one with the major asset types, and ideally annotated with a short "why this works" so the voice is teachable rather than only imitable.

Prompts are filled, runnable strings for recurring jobs, each naming the files to load and ending with the QA instruction.

`pages/` holds finished long-form assets. The rule is update rather than rewrite, because a shipped page carries approvals a fresh draft does not.

### ops/ and snapshots/, the state layer

This layer is why the brain compounds. Without it you have a style guide.

- `copy-bank.md`. Approved language grouped by use: reframes, hooks, one-line positioning, per-audience headlines, proof points, calls to action. Every line here has passed the claim ledger, so it is safe to reuse verbatim.
- `decisions.md`. Newest first. Each entry: date, title, DECIDED or OPEN, the verdict, the rationale, and an explicit note of what did not change. Ends with an "open, owned elsewhere" section for questions deliberately not answered here.
- `signal-log.md`. Raw market input with source, verbatim, type, and disposition. See `compounding.md`.
- `asset-index.md`. Where the source deliverables, product surfaces, channels, and related engagements live.
- `QA-checklist.md`. Tickable, grouped by writing, channel, claims, naming, audience and stage, medium-specific, and voice.
- `review-cadence.md`. Who reviews which ledger, how often, and the staleness threshold for each.

`snapshots/` holds dated captures of external state: funnel numbers, channel performance, win and loss reasons, competitive moves, product status. Each snapshot ends with a "what this changes" section that either routes to a ledger update or explicitly records that nothing changed. A snapshot that changes nothing is still worth keeping, because it is the evidence that the strategy is holding.

### sources/

Keep the originals. `sources/raw/` for the dashboards and decks as delivered, `sources/extracted/` for the machine-readable dumps. When a ledger entry is questioned six months later, the argument ends by opening the source. If the material is confidential, keep the folder out of the repo and record its location in `ops/asset-index.md` instead.

## Load policy

What an agent should read, and when.

| Task | Load |
|---|---|
| Any session | Router only |
| Any customer-facing writing | Router, all four `rules/`, the relevant `reference/` file |
| Strategy question | Master context, `ops/decisions.md` |
| Channel content | Add the channel engine, the template, the matching example |
| Competitive or sales work | Add battlecards and objection handling |
| Ingesting a signal or snapshot | `ops/signal-log.md`, `ops/decisions.md`, and the ledger the signal points at |
| Pre-ship | `ops/QA-checklist.md` |

The one rule that matters most: keep the always-loaded layer small and authoritative, and pull everything else in on demand. A brain that must be read in full to be used will not be used.

---

## reference/extraction.md

# Extraction, turning source material into a brain

Phase 1 and 2 of the build. The job is to read everything, decide what each artifact settles, map it to a destination, and interview only for what is genuinely missing.

## Step 1, convert and read everything

```bash
python3 scripts/extract_sources.py <source_dir> sources/extracted
```

The script walks a directory and writes one Markdown file per source: every sheet of every workbook, every paragraph and table of every document, every slide of every deck, every page of every PDF. Read all of it. Do not sample. The single line that becomes a hard guardrail is usually buried in a cell comment or a footnote, not in a heading.

If a source is a live tool rather than a file, a CRM view, a board, an analytics dashboard, ask for an export or a screenshot set. If neither exists, interview the owner and record the answers as a source artifact in `sources/extracted/` with the date and the person's name, so the provenance survives.

## Step 2, write the source manifest

Before distilling anything, produce a table:

| Artifact | Type | What it settles | Dated | Destination |
|---|---|---|---|---|

"What it settles" is the important column. An artifact that settles nothing is background reading, not a source. If two artifacts settle the same question differently, stop and resolve it with the user. Silent resolution is how a brain gets a confident wrong answer at its core.

Record the manifest in `ops/asset-index.md` when the build is done.

## Step 3, map artifacts to destinations

The mapping is stable across engagements, because GTM work produces a recognizable set of artifacts whatever the consultancy calls them.

| Source artifact, by any name | Reference file | Also feeds |
|---|---|---|
| Positioning deck, category map, brand strategy | `reference/positioning.md` | Master context Section 12, `ops/copy-bank.md` one-liners |
| Strategic verdict or fork document | `reference/positioning-verdict.md` | Master context Section 9, `ops/decisions.md` |
| ICP dashboard, persona research, segmentation | `reference/icp-personas.md` | Master context Section 8 |
| Competitive market analysis, landscape, teardown | `reference/competitive-analysis.md` | Master context Section 7, `rules/do-not-say.md` scoping section |
| Feature or capability matrix, scoring model | `reference/feature-matrix.md` | Master context Section 6, `rules/feature-status.md` |
| Value proposition framework, one per audience | `reference/value-proposition-<audience>.md` | Master context Sections 10 and 11, `ops/copy-bank.md` headlines |
| Customer journey, funnel map, lifecycle model | `reference/customer-journey.md` | Master context Section 13 |
| Marketing asset library, campaign plan, calendar | `reference/marketing-campaigns.md` | Master context Section 14 |
| Product spec, roadmap, release plan | `rules/feature-status.md` | Master context Sections 3 and 5 |
| Brand voice guide, tone of voice doc | `rules/writing-rules.md` | `ops/QA-checklist.md` |
| Naming or terminology doc, product taxonomy | `rules/glossary.md` | Master context Section 2 |
| Legal review, compliance notes, security posture | `rules/do-not-say.md` | Master context Section 4 |
| Pricing model or workbook | `pages/` and `ops/decisions.md` | Only if pricing is decided. If not, it is an open question. |

### Synthesized files, the ones no source contains

Three files usually have to be written rather than extracted, and they are among the most used:

- **Battlecards.** The competitive analysis holds scores and gaps. A battlecard holds the three lines an operator says out loud. Derive one per rival: their real strength, their real gap, and how we win, in that order. Leading with the rival's genuine strength is what makes the card credible internally.
- **Objection handling.** Derive from the ICP dashboard's blockers, the competitive weaknesses, and the claim ledger. One heading per objection in the prospect's own words, then the honest answer. Where the honest answer is "not yet," say not yet. An objection file that pretends every objection is a misunderstanding trains agents to argue with prospects.
- **Channel engine.** For whichever channel the GTM actually runs on. Thesis, how the channels feed each other, the archetypes to rotate, the plan / write / edit method, hook patterns, calls to action, and what good looks like in measurement. This is the file that turns a channel strategy into repeatable production.

## Step 4, distill rather than transcribe

The compression is the value. A twelve-tab workbook becomes forty lines, and those forty lines are the ones an operator would actually consult.

What survives distillation:

- **Decisions and their reasoning.** Especially the reasoning, because it is what stops the decision being reopened.
- **Numbers with consequences.** A score that determines whether a capability leads messaging survives. A score that changes nothing does not.
- **Language that was approved.** Headlines, reframes, and taglines move to `ops/copy-bank.md` verbatim.
- **Constraints.** Anything that starts "we cannot say," "not until," or "only in" becomes a rule.
- **The shape of a model.** Keep the axes, the quadrants, and the placements. Drop the intermediate arithmetic.

What gets dropped: process notes, meeting history, alternatives that were considered and rejected without a live rationale, formatting, and every restatement.

Two tests for a distilled line. First, would an operator look this up? If not, cut it. Second, if this line were wrong, would an asset go out wrong? If yes, it belongs in a ledger, not in prose.

### Preserve, do not paraphrase

Three categories must be copied exactly, never reworded:

1. Approved copy. A paraphrased headline is an unapproved headline.
2. Legal and compliance phrasing. The exact permitted form of a claim is the claim.
3. Canonical terms. Including the capitalization.

## Step 5, the gap interview

Ask in one batched round. Prefer questions whose answers change the build, and offer a default so the user can confirm rather than compose.

**Almost always missing:**

1. **Channel mix.** Which channels are in, and which are explicitly out. "Out" matters more than "in," because it becomes a refusal rule. A GTM that excludes cold outreach, or paid, or a platform, needs that written as a hard ban.
2. **Proof points.** The exact set of real, permissioned facts: customer counts, metrics, named logos, quotes, certifications. This becomes a closed list, and everything outside it is fabrication. Get the precise permitted wording of each.
3. **Status by capability.** Which capabilities are live today, which are partial, which are committed but unshipped, which are vision. Without this the brain will describe a roadmap as a product.
4. **Forbidden words and claims.** The house bans, the competitor terms, the phrases legal has already rejected, the words that belong to a partner or platform.

**Often missing:**

5. Audience count and split. One audience or several, and the rule for never blending them.
6. Tone anchors. Two brands whose voice is right, and two that are wrong.
7. Pricing status. Decided, or a separate engagement. If undecided, prices become a hard ban.
8. Anything historical to handle rather than repeat: a rebrand, a prior product's reputation, a public incident.
9. Review authority. Who signs off on a claim change, and who owns each ledger.
10. Cadence. How often the ledgers get reviewed, and what the corroboration threshold is for acting on a signal.

If an answer does not exist yet, write it into `ops/decisions.md` as an open question with an owner. An open question recorded is a working brain. An open question guessed is a broken one.

## Step 6, seed the decision log during the build

Every strategic call the sources already settled becomes a dated entry in `ops/decisions.md` as you distill it, not afterwards. Include the rationale in one or two sentences, because the rationale is what prevents the decision being reopened in six months by someone who was not in the room.

By the end of the build the decision log should already hold five to ten entries. A brain that ships with an empty decision log has thrown away the most valuable thing the source material contained.

---

## reference/ledgers.md

# Ledgers, deriving the control layer

Phase 4 of the build. The control layer is what stops an agent, or a hurried human, from shipping something the company cannot stand behind. It is derived from the master context, not invented, and it is written to be checked rather than admired.

Derive in this order. Each step depends on the one before it.

## 1. Glossary, the canonical vocabulary

Names come first, because every other rule refers to things by name.

Collect every term the business uses for its own entities, then decide the single canonical form of each. A term earns a row when getting it wrong would be visibly wrong to a customer.

Three kinds of rows:

- **Canonical terms.** The word, and what it means in this business. Include capitalization and whether it is one word.
- **Banned near-synonyms.** The word customers or the team reach for instead, and why it is wrong. Terms owned by a platform, a partner, or a competitor are the common case, and they are the ones that damage credibility fastest.
- **Distinctions that must never blur.** Two terms that sound interchangeable but where a claim is true of one and false of the other. This row usually explains a rule in the claim ledger, so cross-reference it.

Close the file with the single distinction that matters most, stated plainly. If the business has one pair of terms that a wrong claim hinges on, an agent should meet it at the end of the shortest file in the repo.

## 2. Status ledger

What may be promised. The most operationally important file in the brain, and the one that goes stale fastest.

Pick four flags and define them in a legend at the top:

- **SHIPPED**, live now, claimable in the present tense.
- **PARTIAL**, partially shipped. Say what works today, not what it will do.
- **IN BUILD**, committed and unshipped. Mark "coming soon" or omit.
- **ROADMAP**, vision. Never a launch claim.

Group by capability area, one line per capability, flag in caps at the end so the file can be scanned in seconds. Where a single capability is split across states, split the line, because "backups are shipped" and "instant backups are in build" are different promises.

Open the file with the maintenance rule in one sentence: update this file the moment status changes, before any copy follows. Add `last_reviewed: YYYY-MM-DD` so staleness is detectable.

Rename to fit the business. A services firm has a capability or service status ledger. An agency has a deliverable status ledger. The mechanism is identical.

Add a demo rule where relevant: nothing unshipped may be screen-recorded, narrated, or shown as if a customer could do it today. Video and live demos are where status discipline breaks first.

## 3. Claim ledger, the do-not-say file

The claim hygiene spine. Two columns, forbidden or risky on the left, the safe replacement on the right. **Never write a prohibition without a replacement.** A ban with no alternative gets ignored by whoever is on deadline, and it teaches an agent to route around the rule rather than obey it.

Four sections:

### Hard bans

The claims that are always wrong. Sources:

- Certifications and compliance not yet earned. The safe form is almost always "in progress," with the timeline if it is public.
- Unshipped capabilities described as live. Points at the status ledger.
- Blanket versions of conditional claims. Scope them to the mode, tier, or configuration where they are true.
- Pricing, tiers, and plan names when pricing is undecided.
- Invented proof: testimonials, customer counts, metrics, logos. The replacement names the closed set of real proof points.
- Banned vocabulary from the glossary.
- Framing that contradicts a strategic verdict, for example single-platform framing when expansion is decided.
- Channels the GTM excludes. The replacement is a redirect, not a softer version.

### Channel and medium specific bans

Some rules only bite in one medium. Spoken and video content is where unshipped capability gets demonstrated as live and where a caveat gets dropped for pacing. Write those rules separately, because a general rule does not survive contact with a script.

### Claims that need scoping

The valuable section, and the one that takes real work. For every superlative in the source material, run this drill:

1. State the claim as the strategy document phrases it.
2. Name the counter-example. Search for it properly. There is almost always one.
3. Write the narrowed form that survives the counter-example.
4. Record the verdict: the safe form, or "holds" if the claim is genuinely defensible.

Keep the counter-example in the file. It is what stops the broad form creeping back in six months, and it is what an operator needs when a prospect pushes back mid-call.

A claim that cannot be narrowed into a defensible form goes to hard bans.

### Historical and reputational material

Prior products, rebrands, public incidents, competitor history. State the accurate version and the instruction: handle it, do not repeat it as a selling point, and do not pretend it did not happen. Include competitor facts that are commonly misremembered, because an operator repeating a stale rumor about a rival is a credibility loss that is entirely avoidable.

## 4. Writing rules

How every word is written. Six sections:

- **Mechanics.** Punctuation bans, banned words and their obvious variants, paragraph length, and the preference for specifics over adjectives. Be concrete enough to check mechanically.
- **Tone.** Two or three sentences naming the register, then the reason it fits this product and this audience. The reason matters more than the adjectives: "the audience is technical and accountable" gives an agent something to reason from, "professional yet friendly" does not.
- **Medium-specific rules.** Writing for the ear if there is spoken content, and whatever the equivalent is for the mediums in the mix. Spoken writing has genuinely different rules and needs its own block.
- **Claim discipline.** One paragraph pointing at the claim ledger and the status ledger, and naming what triggers a check: every superlative, every capability mention, every conditional claim.
- **Channel discipline.** What this GTM writes and what it refuses to write.
- **Signature lines.** The reframes and phrases that are approved and reusable. This is where voice becomes concrete.

**Default starting set, to confirm or replace with the user.** Ship a brain with a real control layer rather than an empty one, then tune:

- No em dashes. Use commas, or restructure.
- Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower, and their obvious variants.
- Short paragraphs, one to three sentences.
- Specific numbers, named capabilities, and verifiable facts over adjectives.
- No stacked adjectives, no hype, no superlative that is not backed by the claim ledger.
- Prose over lists. Use a list only when the content is genuinely a list.

These are defaults, not doctrine. Ask the user to confirm each one and to add the bans specific to their brand. A brand with its own strong voice will replace half of this list, and that is the correct outcome.

## 5. QA checklist

The mechanical mirror of everything above. It is the last thing anyone reads before shipping, so every item must be answerable yes or no by looking at the draft. If an item requires judgment, rewrite it until it does not.

Group in this order, cheapest checks first:

1. **Writing.** Mechanics and banned words.
2. **Channel.** Is this a channel we produce for at all.
3. **Claims.** One line per hard ban, each pointing at its ledger.
4. **Naming and strategy.** Canonical vocabulary, and no framing that contradicts a decided verdict.
5. **Audience and stage.** One audience only, and copy matched to the funnel stage.
6. **Medium-specific.** A separate block for scripts, video, or anything with its own failure modes.
7. **Voice.** Does it read like the matching file in `examples/`.

The rule that keeps this honest: if a rule exists that cannot be turned into a checkbox, it is not a rule yet, it is a preference. Either sharpen it or move it to the writing rules as guidance.

## Keeping the layers in sync

The rules files duplicate the master context on purpose. Duplication has a cost, and the cost is paid by one convention:

- The master context is authoritative when the two disagree.
- A status or claim change updates the `rules/` file first, because that is what gets loaded on every task, then the corresponding master context section in the same change, then downstream copy.
- The audit script flags a rules file whose `last_reviewed` date is older than the master context's `last_updated`, because that ordering means a change landed in the reference layer and never reached the control layer.

---

## reference/compounding.md

# The compounding loop

UPDATE mode. This is what makes a brain a brain rather than a folder of documents. Every lead conversation, customer signal, competitor move, product change, and periodic snapshot enters here, gets triaged, and either changes a ledger or is recorded as having changed nothing. Both outcomes are valuable. The second one is the evidence that the strategy is holding.

The loop has one governing principle: **nothing enters the copy layer without passing through a ledger, and nothing enters a ledger without a dated decision.**

## The four-step loop

```
CAPTURE  ->  TRIAGE  ->  ROUTE  ->  PROPAGATE
   |                                     |
   +--------- snapshots, periodic -------+
```

### 1. Capture

Everything goes into `ops/signal-log.md`, raw, before any judgment. Cheap capture is the whole point. A signal that gets debated before it gets written down does not get written down.

One entry, five fields:

```markdown
### YYYY-MM-DD | <type> | <source>
**Verbatim:** "<what was actually said or observed, in their words>"
**Context:** <who, which stage, which segment, which channel>
**Disposition:** NOISE | WATCH (n/N) | PATCH | AMEND
**Routed to:** <file, or "none">
```

Keep the verbatim. Paraphrasing a customer into house vocabulary destroys the most valuable thing a signal carries, which is the language a real buyer used before we taught them ours. Copy-bank lines derived from real customer phrasing outperform lines written internally, and you cannot recover that phrasing later.

**Signal types:**

| Type | What it is | Where it usually lands |
|---|---|---|
| OBJECTION | A prospect pushed back | `reference/objection-handling.md` |
| LANGUAGE | A buyer described the problem in their own words | `ops/copy-bank.md`, value propositions |
| PROOF | A permissioned metric, quote, result, or logo | `ops/copy-bank.md` proof points, `rules/do-not-say.md` |
| STATUS | A capability shipped, a certification landed, pricing set | `rules/feature-status.md` |
| COMPETITIVE | A rival launched, repositioned, was acquired, or shut down | `reference/competitor-battlecards.md`, claim scoping |
| SEGMENT | A buyer type keeps appearing, or a named ICP is not converting | `reference/icp-personas.md`, master context |
| CHANNEL | A channel over or under performs against its role | `reference/marketing-campaigns.md`, channel engine |
| LOSS | A churn reason or a lost deal reason | Objection handling, ICP, positioning |
| RISK | A claim was challenged by a prospect, a reviewer, or legal | `rules/do-not-say.md`, immediately |

### 2. Triage

Every signal gets exactly one of four dispositions. Triage is a fixed weekly slot, not a reaction to whichever signal is loudest.

**NOISE.** One instance, no pattern, no consequence. Logged and closed. Logging noise is not waste: three noise entries that rhyme become a WATCH, and you only see the rhyme because they were written down.

**WATCH.** Plausible pattern, not yet corroborated. Record it as `WATCH (1/3)` and increment as instances arrive. When the threshold is met, it is promoted and triaged again.

Default thresholds, set with the user during the build:

| Signal class | Threshold to act |
|---|---|
| Opinion, preference, language, objection | 3 independent instances within 60 days |
| Verifiable fact: status, proof, competitive, risk | 1 verified instance, act immediately |
| Loss reason | 2 instances, or 1 if the deal was in the core ICP |
| Channel performance | A full measurement cycle, never a single week |

The distinction that matters: opinions need corroboration, facts need verification. A prospect disliking a headline is an opinion. A competitor shipping the capability that anchors your flagship claim is a fact, and it changes the claim ledger today.

**PATCH.** Changes copy, not strategy. Route it, make the edit, done. No decision entry, no version bump. Adding a heard objection to the objection file, banking a customer's phrasing, sharpening a headline: all patches.

**AMEND.** Changes a ledger, a strategic position, or a rule. This is the heavy path and it has a fixed procedure, below. Anything touching `rules/`, an ICP definition, positioning, or the channel mix is an AMEND.

**The default is NOISE.** A brain that amends on every input is a brain with no memory, and one that flip-flops on the last conversation is worse than a static document. The value of a settled decision is that it stays settled until real evidence moves it.

### 3. Route

PATCH and AMEND both route to a file. The routing rule is fixed and it is the one that keeps the brain coherent:

**Ledger first, master context second, copy third, assets last.** Never the reverse. Copy that leads the ledger is how a company ends up with a landing page making a claim its own rules forbid.

The AMEND procedure, all five steps or none:

1. **Update the ledger.** The `rules/` file that governs the thing that changed. Update its `last_reviewed` date.
2. **Update the master context.** The corresponding numbered section, in the same change. Bump `version` and `last_updated` in the frontmatter, and revise `status_notes` if the change alters what an agent may assume.
3. **Write the decision entry.** `ops/decisions.md`, newest at the top:

```markdown
## YYYY-MM Title of the decision (DECIDED)
<The verdict in one or two sentences.>
<The rationale, and the evidence that moved it: which signals, how many, over what period.>
**What this does not change:** <explicit list>
**Downstream:** <the assets that must now be revised, and who owns each>
```

   The "what this does not change" line is not filler. A positioning change that leaves the status ledger untouched must say so, or the next agent will assume the whole brain moved and rewrite things that were correct. It is also the line that stops a small amendment turning into an unplanned rewrite.

4. **Propagate to copy.** Update `ops/copy-bank.md`, and any template or reference file that repeated the old form. Grep the repo for the old phrasing. Stale approved copy is the most dangerous artifact in the brain, because it is pre-approved and therefore reused without a second look.
5. **List the affected shipped assets.** Everything in `pages/` and every live surface in `ops/asset-index.md` that carries the old claim. This becomes the downstream list in the decision entry, with an owner per item.

### 4. Propagate and close

Mark the signal entry `Routed to:` with the files changed. When the downstream list is complete, add the completion date to the decision entry. Open downstream items are the brain's debt, and the audit script reports them.

## Snapshots

A snapshot is a dated capture of external state. Signals arrive one at a time and are anecdotes. A snapshot is the periodic look at the whole board, and it catches the changes no single signal announces: a channel decaying, a segment converting better than the one the strategy prioritizes, a claim that quietly stopped being true.

Cadence: monthly for early-stage, quarterly once the motion is stable. Never skip one because "nothing changed." The record that nothing changed is the output.

File: `snapshots/YYYY-MM-DD-<label>.md`. Sections:

1. **Funnel.** Volume and conversion by stage, per audience, against the journey model.
2. **Channels.** Performance against each channel's assigned role. A channel can succeed on its own numbers and still fail its role.
3. **Segments.** Which ICP is actually converting, and which named segment is not showing up.
4. **Wins and losses.** Reasons, grouped. Loss reasons are the highest-yield input in the entire loop.
5. **Competitive.** What moved. Repositions, launches, pricing changes, funding, shutdowns.
6. **Product and delivery status.** Diffed against `rules/feature-status.md`. This diff alone justifies the ritual.
7. **What this changes.** The routing section. Either a list of AMENDs and PATCHes with owners, or the sentence "no ledger change this period," which is a real finding and should be written as one.

Every snapshot ends by updating `last_reviewed` on each ledger it examined, whether or not the ledger changed. That is what makes staleness visible.

## Review cadence

Record the agreed cadence in `ops/review-cadence.md` and give every ledger an owner.

| Ritual | Frequency | Work |
|---|---|---|
| Signal triage | Weekly, fixed slot | Disposition every new signal, increment WATCH counters, execute PATCHes |
| Ledger sweep | Monthly | Read all four `rules/` files against reality, update `last_reviewed`, clear stale WATCH items |
| Snapshot | Monthly or quarterly | The full capture above |
| Master context version | Quarterly, or on any AMEND | Bump version, refresh `status_notes`, verify sections against ledgers |
| Brain audit | Quarterly | `scripts/audit_brain.py`, plus produce one live asset using only the brain |

A WATCH item that has not incremented in two cycles expires to NOISE. Say so in the log. An indefinitely open watch list is a to-do list nobody reads.

## Why this compounds

Each mechanism converts a one-off event into a permanent asset, and each one raises the floor for every future piece of work.

- **Decisions stop being relitigated.** The dated verdict plus rationale means the same argument is had once. Time not spent reopening settled questions is the first return.
- **Language accumulates.** Every line that survives review is banked. Over a year the copy bank becomes a library of proven phrasing, and new work starts from proven language rather than a blank page.
- **Objections become pre-vetted answers.** The tenth time an objection is heard it has a tested response attached, and the response is in every agent's context.
- **Risk falls monotonically.** Every challenged claim tightens the claim ledger. The set of things that can go wrong shrinks, and it never grows back, because the counter-example stays in the file.
- **Onboarding collapses.** A new hire, freelancer, or agent absorbs the accumulated go-to-market in one read. The brain is the ramp.
- **Snapshots make drift visible.** Strategy fails slowly and quietly. A dated series of captures is the only way to see it while it is still cheap to correct.

The interest compounds because the ledgers are load-bearing. A patch to the copy bank improves the next asset. An amendment to a ledger improves every asset produced from that point on, by every operator and every agent, without anyone being told.

---

## reference/operating.md

# Operating a built brain

OPERATE mode. The brain exists and the job is to produce, check, or ship something with it. This is the mode most sessions are in, so it should be fast and mechanical.

## The session contract

Six steps, in order.

1. **Load the router.** `CLAUDE.md` or `AGENTS.md`. It carries the read order and the non-negotiables. Never skip it on the grounds that the task is small. Small tasks are where claims leak.
2. **Pick the audience.** If the business has more than one, choose before writing a word, and never blend them in a single asset. Blending is the most common failure and the hardest to spot in review, because each half reads fine.
3. **Load the control layer.** All four `rules/` files for anything customer-facing. They are short by design.
4. **Load what the task needs.** The load policy table in `blueprint.md` maps task to files. For channel content that means the channel engine, the template, and the matching example.
5. **Produce.** Fill the template. Use the copy bank verbatim where a line exists, because those lines have already passed the claim ledger. Never invent a proof point, a price, or a status.
6. **Run the QA checklist.** `ops/QA-checklist.md`, item by item, before returning anything. Then state which checks were run.

## While producing

**Copy bank first.** If an approved line covers the point, use it. Rewriting an approved line is how a checked claim becomes an unchecked one.

**Status flags travel with capabilities.** Any mention of an unshipped capability carries its marker in line, in the same sentence, not in a footnote and not once at the top of the page.

**Superlatives get checked, every time.** Every "only," "first," "best," "never," and "no other" goes through `rules/do-not-say.md`. Most will need the narrowed form.

**Conditional claims name the condition.** If a claim is true in one mode, tier, or configuration and false in another, the condition is part of the sentence.

**Refuse out-of-scope channels.** If the GTM excludes a channel, say so plainly and offer the in-scope alternative. Do not quietly produce it because the request was direct.

**Flag gaps rather than filling them.** If the task needs a fact the brain does not hold, say so and ask. Inventing a plausible fact is the single worst failure mode available here, because the output looks correct.

## Returning work

State the audience, the funnel stage, and the template used. List every capability mentioned with its status flag. Name any claim that was narrowed and why. Note anything the brain could not supply.

If the work produced a reusable line, propose it for `ops/copy-bank.md`. If it surfaced a gap, log it as a signal. Production work is a signal source, and treating it as one is free.

## After shipping

Two closing moves, both cheap and both routinely skipped:

- **File the asset.** Long-form assets go in `pages/`. Live surfaces get a line in `ops/asset-index.md` with their location, so the next amendment can find everything that carries the old claim.
- **Log what the work taught you.** A gap, a line that landed, an objection that came up in review. Into `ops/signal-log.md`. This is the loop closing on itself, and it is why the brain gets sharper through use rather than through maintenance.

---

## reference/portability.md

# Portability, making a brain every agent can read

Load this in Phase 7, and again whenever someone on the team shows up running a different tool.

A brain outlives the tool that built it. The operator who commissions it runs Claude Code, the
engineer who edits the product strings runs Codex, the founder rewrites the landing page in a
chat window with Grok or ChatGPT open, and the agency uses Cursor. If the guardrails only load
in one of those, the other three ship copy the brain would have refused. That is the failure this
file prevents.

## The rule that keeps it sane

**One copy of the truth, many doors into it.** The brain is the truth. Everything a tool reads is
a pointer file of about twenty lines that says where to look and when. No adapter ever restates
strategy, a claim, or a status. The moment an adapter carries content, it starts drifting, and a
stale guardrail is worse than none because it still carries authority.

The one deliberate exception is the portable control layer, below. It carries content because a
chat model cannot follow a pointer, and it is dated and regenerated for exactly that reason.

## What every brain ships

Three routers plus the index, built in Phase 7 and non-negotiable:

- `CLAUDE.md`, for Claude Code and the Claude apps.
- `AGENTS.md`, read by Codex, Cursor, Zed, Jules, opencode, and most newer tools. Widest reach of
  the three, so keep it complete rather than thin.
- `llms.txt`, the linked index. An agent reads it to decide what to open without opening anything.
- `README.md`, for people.

`CLAUDE.md` wins if the routers ever disagree, and `AGENTS.md` says so in a line.

## Adapters, one per tool in use

Add these only for tools someone actually runs. An adapter for a tool nobody uses is a file that
goes stale unnoticed. Templates are in `adapters/brain/`, and each takes `{{PROJECT}}`,
`{{BRAIN_PATH}}`, `{{PRIMARY_CHANNEL}}`, `{{AUDIENCE_LIST}}`, and `{{NON_NEGOTIABLES}}`.

| Tool | Write | From |
|---|---|---|
| Codex, Zed, Jules, opencode | `AGENTS.md` in the consuming repo | `adapters/brain/AGENTS.block.md` |
| Cursor | `.cursor/rules/<project>-gtm.mdc` | `adapters/brain/cursor.mdc` |
| Windsurf | `.windsurf/rules/<project>-gtm.md` | `adapters/brain/windsurf.md` |
| GitHub Copilot | `.github/copilot-instructions.md` | `adapters/brain/copilot-instructions.block.md` |
| Gemini CLI | `GEMINI.md` | `adapters/brain/GEMINI.block.md` |
| Any chat model, no file access | `adapters/portable-control-layer.md` | `adapters/brain/system-prompt.md` |

The brain repository holds the rendered adapters in its own `adapters/` folder. A consuming
repository, the product codebase for instance, gets the pointer file copied into it, aimed at
wherever the brain is checked out.

Files ending `.block.md` merge into a file the project already has. Keep the markers:

```
<!-- gtm-brain:begin -->
<!-- gtm-brain:end -->
```

Replace what sits between them on an update, append the block when they are absent, and never
edit inside them by hand.

## The portable control layer

For anyone working in a chat window, render `adapters/brain/system-prompt.md` into a filled file
under `adapters/`. It carries the audiences, positioning, status summary, proof points, the
do-not-say table, the channel list, and the writing rules. That is enough to keep a draft inside
the guardrails without any file access.

It carries content, so it decays. Three rules keep it honest:

1. It is dated in its own header.
2. It regenerates whenever a ledger changes, as the last step of the amendment procedure, after
   the ledger, the master context, and the decision log.
3. It is listed in `ops/asset-index.md` and named in `ops/review-cadence.md`, so a review catches
   it when nobody remembered to regenerate it.

## Wiring it in

Add to `ops/asset-index.md`: every adapter, where it is installed, and who runs that tool. Add to
`ops/review-cadence.md`: a line that adapters are checked on the same cycle as the ledgers. Add to
`llms.txt`: one line per adapter, so the set stays visible.

The amendment procedure gains a final step. Ledger, then master context, then decision log, then
copy, then the portable control layer. Adapters that are pointers need nothing, which is the point
of keeping them pointers.

## Retrofitting the skill itself

Someone will want to run BUILD or UPDATE from a tool that has no skill system. That is a separate
question from the brain being readable, and the full set of recipes lives in `PORTING.md` at the
root of the GTM Brain repository, covering Codex, Cursor, Windsurf, Copilot, Gemini, Grok, custom
GPTs, agent frameworks, and plain chat. The short version: install the skill files anywhere, write
the pointer file that tool reads, and where there is no file access at all, generate a bundle with
`scripts/bundle_skill.py` and paste it in.

## Check it works

Do not assume an adapter loaded. In each tool someone runs, open a fresh session and ask for
something the brain forbids: copy for an excluded channel, a claim about a capability that is in
build, a metric that is not a proof point. Then ask for something it allows.

A tool that is wired in refuses the first, names the rule and the file it came from, and produces
the second in voice. A tool that produces both is not loading the brain, and the person using it
has been shipping unchecked copy. Fix the adapter, then check what already shipped.

---

## adapters/skill/system-prompt.md

You operate a Go-to-Market Brain: one company's go-to-market held as governed context rather
than as tribal knowledge. You never invent strategy that has already been decided, and you
never state a claim the company has not earned.

**Route first.** Decide which of three modes you are in before producing anything.

- **BUILD.** The user has source material (dashboards, decks, positioning docs, ICP research,
  competitive analysis) and no brain yet. Distil it into: a master context file, a control layer
  (`glossary`, `feature-status`, `do-not-say`, `writing-rules`, `QA-checklist`), a reference layer
  (one short file per source, plus battlecards and objection handling), an execution layer
  (a template and a gold-standard example per channel in the mix), and a state layer (`decisions`,
  `signal-log`, `copy-bank`, `asset-index`, `review-cadence`, dated snapshots). Ask for what is
  missing in one batched round, never in a drip. Record what the user cannot answer as an open
  question. An invented answer becomes a rule, and a wrong rule propagates into every asset.
- **UPDATE.** The user brings a call note, an objection, a churn reason, a competitor move, a
  shipped feature, or a metrics snapshot. Capture the raw signal with its date and source, triage
  it against a corroboration threshold (one instance is an anecdote, the threshold the user sets
  is a pattern), then either amend a ledger with a dated decision, patch the approved copy, or
  record explicitly that it changes nothing. All three are real outcomes.
- **OPERATE.** The user wants an asset produced, reviewed, or shipped. Pick the audience, load
  the rules, write, then run the QA gate before returning anything.

**Invariants.** These hold in every mode.

1. Ledgers before copy. When status changes, the ledger changes first and copy follows.
2. Every capability carries a status flag: shipped, partial, in build, or roadmap. No claim about
   an unshipped capability without the flag attached.
3. Every prohibition carries a replacement. A ban with no "say instead" gets ignored under deadline.
4. Audience before writing. More than one audience means separate value propositions, never blended.
5. Proof points are a closed set. Only real, permissioned, sourced facts. If a number is not on the
   list, write `[PROOF POINT NEEDED]` and keep going. Never invent a statistic, customer, or quote.
6. Scope every superlative. "Only", "first", "best", and "never" get narrowed to the form that
   survives scrutiny, or they get cut.
7. Name the mode when a claim is conditional. True in one configuration and false in another means
   the configuration is part of the claim.
8. Channel discipline is a rule. If the strategy excludes a channel, refuse to produce for it and
   say why.
9. Decisions are dated and never relitigated, including a note of what the decision did not change.

**Writing rules.** Apply to every word of customer-facing output.

- Banned: leverage, unlock, seamless, robust, streamline, cutting-edge, empower, elevate,
  revolutionize, game-changing, best-in-class, world-class, supercharge, turbocharge, delve,
  tapestry, figurative landscape, figurative navigate, realm, testament, figurative journey,
  foster, facilitate, utilize, myriad, plethora, pivotal, crucial, vital. When a banned word is
  the only one that fits, the sentence carries no specific claim. Find the claim or cut the
  sentence. Do not reach for a synonym.
- No em dashes. No "It's not just X, it's Y." No "In today's fast-paced world." No decorative rule
  of three. No opener that restates the request. No rhetorical question as an opener. No emoji
  unless asked.
- One idea per sentence, varied lengths, point front-loaded, concrete nouns over abstract ones.
- Write to one reader, second person. Say the uncomfortable part. If a sentence would survive
  swapping in a competitor's name, delete it and write the one that would not.
- For anything spoken, use short spoken sentences and contractions, and signpost by voice rather
  than by headers.

**Before returning anything.** Re-read the draft against the invariants and the writing rules, fix
what breaks, and end with one line naming the rule the draft came closest to breaking. That line
tells the user where the copy is weakest.

**When the brain lives in files you cannot read**, ask the user to paste the control layer: the
entry file, `rules/do-not-say.md`, `rules/feature-status.md`, and `rules/writing-rules.md`. Those
four are small by design. Treat what they say as overriding anything above.

---

End of bundle. Nothing above this line is optional context: the rules are the point of the tool. If a request cannot be met inside them, say which rule blocks it and offer the nearest thing that is allowed.
