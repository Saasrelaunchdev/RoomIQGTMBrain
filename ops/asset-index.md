# Asset index

Where the sources, live surfaces, adapters, and generated artifacts live. An amendment consults this file to find everything that carries an old claim, so keep it current.

## Source deliverables
Full manifest: `sources/README.md`.

| Artifact | Type | What it settles | Dated | Location |
|---|---|---|---|---|
| Discovery pack (S1 to S5) | Markdown | As-built product, features, gaps, QA, open questions | 2026-11-10 | `sources/extracted/discovery/` |
| Product screenshots (S6) | 15 images | Primary evidence | 2026-11-10 | `Saasrelaunchdev/roomIQGTMBuild`, `docs/discovery/screenshots/`, commit `9ed7a8b` |
| Competitive desk scan (S7) | Notes | Rival set, public positioning | 2026-11-13 | `reference/competitive-analysis.md` |
| Founder gap interview | Questionnaire | Everything the sources could not | 2026-11-13 | `ops/founder-gap-interview.md` |

## Product and brand
- Live product URL: [NEEDS BRAIN] founder to provide.
- Public website or landing page: not captured (coverage gap B1).
- Pricing page: not captured (B2).
- Brand cues seen in the product: `ROOMIQ` spaced-caps wordmark with a heavier final Q, deep navy, cyan eyebrow labels, light blue-grey canvas, Inter-like type. No brand guide on file.

## Live surfaces (every place a claim is published)
None recorded yet. Add each one when it ships: URL, owner, last reviewed date, and the claim IDs it carries.

| Surface | URL | Owner | Last reviewed | Claims carried |
|---|---|---|---|---|

## AI tool adapters (where the guardrails load)

| Tool | File in this repo | For consuming repos | Runs it |
|---|---|---|---|
| Claude Code | `CLAUDE.md`, `.claude/skills/`, `.claude/commands/`, `.mcp.json` | `adapters/consuming-repo/` | Founder |
| Codex, Zed, Jules, opencode | `AGENTS.md` | `adapters/consuming-repo/AGENTS.block.md` | Founder |
| Cursor | `.cursor/rules/roomiq-gtm.mdc` | `adapters/consuming-repo/cursor.mdc` | Unknown |
| Windsurf | `.windsurf/rules/roomiq-gtm.md` | `adapters/consuming-repo/windsurf.md` | Unknown |
| GitHub Copilot | `.github/copilot-instructions.md` | `adapters/consuming-repo/copilot-instructions.block.md` | Unknown |
| Gemini CLI | `GEMINI.md` | `adapters/consuming-repo/GEMINI.block.md` | Unknown |
| Cline, Roo, Continue, Kiro, Junie, Amazon Q, Aider | dot-folder rules, see `adapters/README.md` | same files | Unknown |
| Any MCP client | `tools/mcp_server.py` | `adapters/mcp/` | Founder |
| Chat models without files | `adapters/portable-control-layer.md`, `dist/roomiq-gtm-brain.bundle.md` | paste | Anyone |

Confirm which tools the team runs (G-adapters in the next review) and delete adapters nobody uses.

## Generated artifacts (do not edit by hand)
Rebuilt by `python3 tools/brain.py build`; CI fails if they are stale.
- `dist/llms-full.txt`: every brain file concatenated in load order.
- `dist/brain.manifest.json`: file map with layer, purpose, size, hash.
- `dist/brain.chunks.jsonl`: heading-level chunks with metadata, for vector stores.
- `dist/roomiq-gtm-brain.bundle.md`: control layer plus master context for chat models and system prompts.
- `dist/ledgers.json`: feature status, claim ledger, glossary, decisions, assumptions, experiments as JSON.

## Related engagements
- Product discovery and PRD: `Saasrelaunchdev/roomIQGTMBuild` (screenshot-product-discovery skill).
- Pricing: not started (D-11).
- Legal review of data rights and AI derivatives: not started (G11, G12).
