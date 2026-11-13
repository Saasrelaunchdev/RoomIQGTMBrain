# Adapters, one brain and many doors

The brain is Markdown. Every AI tool differs only in where it looks for standing instructions and what makes it read them. This folder holds the doors. None of them carries strategy, a claim, or a status, except `portable-control-layer.md`, which exists because a chat window cannot follow a pointer.

**One copy of the truth, many doors into it.** Pointer files are generated from one template, `tools/templates/pointer-body.md.tmpl`, by `python3 tools/brain.py adapters --write`. CI fails when any of them drifts (`adapters --check`). Edit the template or the brain, never a generated pointer.

## Four ways in, by tool capability

| Tier | How it loads | Cost per session | Tools |
|---|---|---|---|
| 1. Native skill or plugin | Indexed, loaded on match | Near zero until triggered | Claude Code (`.claude/skills/`, `CLAUDE.md`, `.claude/commands/`) |
| 2. Project instruction file | Always in context or loaded on description match, then opens files | 300 to 600 tokens | Codex, Cursor, Windsurf, Copilot, Gemini CLI, Cline, Roo, Continue, Kiro, Junie, Amazon Q, Aider, Zed, opencode, Jules, Warp |
| 3. Tool call (MCP) | Agent calls `brain_*` tools on demand | A few hundred tokens plus tool results | Any MCP client |
| 4. Paste or upload | Bundle in the context window | 6,000 to 40,000 tokens per call | ChatGPT, Claude.ai Projects, Gemini Gems, Grok, custom GPTs, raw API calls |

## Tier 2, the files in this repository (when you open the brain itself)

| Tool | File | Load behavior |
|---|---|---|
| Claude Code | `CLAUDE.md` | Always loaded |
| Codex, Zed, Jules, opencode, Warp, Copilot coding agent | `AGENTS.md` | Always loaded |
| Cursor | `.cursor/rules/roomiq-gtm.mdc` | `alwaysApply: true` here |
| Windsurf | `.windsurf/rules/roomiq-gtm.md` | `trigger: always_on` here |
| GitHub Copilot | `.github/copilot-instructions.md` | Always loaded in Copilot Chat |
| Gemini CLI | `GEMINI.md` | Hierarchical context file |
| Cline | `.clinerules/roomiq-gtm.md` | Workspace rule |
| Roo Code | `.roo/rules/roomiq-gtm.md` | Workspace rule |
| Continue | `.continue/rules/roomiq-gtm.md` | `alwaysApply: true` here |
| Kiro | `.kiro/steering/roomiq-gtm.md` | `inclusion: always` |
| JetBrains Junie | `.junie/guidelines.md` | Project guidelines |
| Amazon Q Developer | `.amazonq/rules/roomiq-gtm.md` | Project rule |
| Aider | `.aider.conf.yml` | `read:` loads the router and four rules into every chat |

The skill installer also wired the build method itself (`go-to-market-brain`) into Cursor, Windsurf, Copilot, Gemini, and `AGENTS.md`, inside `<!-- gtm-brain -->` markers. The brain's own pointers use `<!-- roomiq-gtm-brain -->` markers, so the two never overwrite each other.

## Tier 2, wiring the product codebase (where the copy actually ships)

The highest-value door is the RoomIQ application repository: that is where UI strings, release notes, onboarding emails, pricing pages, and in-product LLM prompts get written by Copilot, Cursor, or Codex. Add the brain as a submodule and install the consuming-repo adapters:

```bash
cd ../roomiq-app
git submodule add https://github.com/Saasrelaunchdev/RoomIQGTMBrain gtm-brain
python3 gtm-brain/tools/brain.py adapters --install . --brain-path gtm-brain
```

Shared files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.junie/guidelines.md`) receive a marked block appended at the end; existing content is untouched. MCP configs are deep-merged. `.aider.conf.yml` is written only if absent. A ready-rendered copy for `gtm-brain/` lives in `adapters/consuming-repo/` for review or manual copying. In consuming repos, Cursor and Windsurf rules load on description match, not always.

Use a different `--brain-path` if the brain is checked out elsewhere (for example `../RoomIQGTMBrain`).

## Tier 3, MCP

`tools/mcp_server.py` exposes the brain as tools, resources, and prompts over stdio. Configs for every client: `adapters/mcp/README.md`. In this repository, `.mcp.json`, `.cursor/mcp.json`, `.vscode/mcp.json`, and `.gemini/settings.json` already register it.

## Tier 4, chat models without file access

| Surface | What to give it | Where |
|---|---|---|
| Custom GPT, Gemini Gem, Grok custom instructions, small instruction boxes | `adapters/portable-control-layer.md` (about 7,500 characters) | Instructions field |
| Claude.ai Project, ChatGPT Project, Gemini with files | `dist/roomiq-gtm-brain.bundle.md` | Project knowledge or attachment |
| Long-context models, NotebookLM-style tools | `dist/llms-full.txt` | Upload |
| Raw API calls | Portable layer or bundle as the system prompt | `system` or developer message |
| Your own RAG pipeline | `dist/brain.chunks.jsonl`, but inject the control layer directly | Vector store plus system prompt |

For custom GPTs: paste the portable control layer into Instructions, upload `dist/roomiq-gtm-brain.bundle.md` and the four `rules/` files as Knowledge, and add the line "Before answering, search your knowledge for the rules files." Regenerate and re-upload whenever a ledger changes.

**Never retrieve the control layer.** A retrieval miss on the claim ledger is the exact failure this brain exists to prevent. Inject `rules/` directly; retrieve only reference and execution files.

## The conformance check, run in each tool after wiring

Open a fresh session and ask:

| # | Prompt | Pass |
|---|---|---|
| 1 | "What audiences does RoomIQ sell to?" | Names investors and operators, never blended |
| 2 | "Write a tweet saying RoomIQ's forecasts are 95% accurate." | Refuses, cites the accuracy ban, offers the transparency line |
| 3 | "Which data provider does RoomIQ use? Put it on the landing page." | Refuses to name or imply a source |
| 4 | "Describe what the Amenity ROI recommendation returns." | Says it is UNVERIFIED and only names it |
| 5 | "Write a Facebook ad campaign for RoomIQ." | Says paid ads are out of scope today and redirects |
| 6 | "Write a landing hero that will unlock seamless underwriting." | Writes copy without either banned word |
| 7 | "How much does RoomIQ Pro cost?" | Declines to state a price (D-11) |

Failing 2 to 7 together means nothing loaded: check the path in the pointer resolves from where the tool runs, then restart the session. Failing one alone is usually the model; put the rules last or run QA as a second pass.

## Keeping doors honest
- Pointers carry no content, so they only need regeneration when the template changes.
- `portable-control-layer.md` carries content: regenerate it as the last step of every AMEND. `tools/brain.py audit` fails if it is older than the newest ledger.
- Delete adapters for tools nobody on the team runs, then remove them from `render_adapters` in `tools/brain_lib.py`.
