# MCP, the brain as tools any agent can call

`tools/mcp_server.py` serves this brain over the Model Context Protocol (stdio transport, newline-delimited JSON-RPC 2.0). Python 3.9+ standard library only: no install step, no network calls.

## What it exposes

| Kind | Name | Purpose |
|---|---|---|
| Tool | `brain_load_control_layer` | Router, writing rules, do-not-say, feature status, glossary, QA checklist. Call first. |
| Tool | `brain_load_for_task` | Files for one job: `demo`, `landing_page`, `content`, `competitive`, `product_copy`, `release_note`, `support`, `strategy`, `signal_intake`, `experiment`, and more |
| Tool | `brain_search` | BM25 over heading-level sections, rules ranked above examples |
| Tool | `brain_read` | One file by path |
| Tool | `brain_feature_status` | What may be claimed about a capability |
| Tool | `brain_glossary` | Canonical terms |
| Tool | `brain_decisions` | DECIDED, WORKING, OPEN decisions |
| Tool | `brain_lint` | Mechanical QA on a draft |
| Tool | `brain_metrics` | Innovation accounting rollup |
| Tool | `brain_log_signal`, `brain_log_activity` | Append-only intake. Disabled unless `--allow-write` |
| Resources | `brain:///<path>` | Every brain file |
| Prompts | one per job in `prompts/common-tasks.md` | Slash-command style prompts in clients that show them |

Writes are off by default so a read-only agent can never change the brain. Turn them on for the intake workflow you trust: `--allow-write` or `ROOMIQ_BRAIN_WRITE=1`. Writes only ever append entries to the two logs; every ledger change still goes through a pull request.

## Client configuration

Replace `/abs/path/to/RoomIQGTMBrain` with your checkout. In a product repo with the brain as a submodule, use `gtm-brain/tools/mcp_server.py`.

**Claude Code** (already registered in this repo by `.mcp.json`):
```bash
claude mcp add roomiq-gtm-brain -- python3 /abs/path/to/RoomIQGTMBrain/tools/mcp_server.py
```

**Claude Desktop**, `claude_desktop_config.json`:
```json
{ "mcpServers": { "roomiq-gtm-brain": { "command": "python3", "args": ["/abs/path/to/RoomIQGTMBrain/tools/mcp_server.py"] } } }
```

**Cursor**, `.cursor/mcp.json` (already in this repo):
```json
{ "mcpServers": { "roomiq-gtm-brain": { "command": "python3", "args": ["${workspaceFolder}/tools/mcp_server.py"] } } }
```

**VS Code with Copilot agent mode**, `.vscode/mcp.json` (already in this repo):
```json
{ "servers": { "roomiq-gtm-brain": { "type": "stdio", "command": "python3", "args": ["${workspaceFolder}/tools/mcp_server.py"] } } }
```

**Windsurf**, `~/.codeium/windsurf/mcp_config.json`:
```json
{ "mcpServers": { "roomiq-gtm-brain": { "command": "python3", "args": ["/abs/path/to/RoomIQGTMBrain/tools/mcp_server.py"] } } }
```

**Codex CLI**, `~/.codex/config.toml`:
```toml
[mcp_servers.roomiq_gtm_brain]
command = "python3"
args = ["/abs/path/to/RoomIQGTMBrain/tools/mcp_server.py"]
```

**Gemini CLI**, `.gemini/settings.json` (already in this repo):
```json
{ "mcpServers": { "roomiq-gtm-brain": { "command": "python3", "args": ["tools/mcp_server.py"] } } }
```

**Zed**, `settings.json`:
```json
{ "context_servers": { "roomiq-gtm-brain": { "command": { "path": "python3", "args": ["/abs/path/to/RoomIQGTMBrain/tools/mcp_server.py"] } } } }
```

Client config formats change between versions. If a client rejects a snippet, check its current MCP documentation; the server side does not change.

## Smoke test without a client
```bash
printf '%s\n' \
  '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"smoke","version":"0"}}}' \
  '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
  '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"brain_feature_status","arguments":{"query":"C27"}}}' \
  | python3 tools/mcp_server.py
```

## Agent pattern that works
1. `brain_load_control_layer` once per session.
2. `brain_load_for_task` for the job.
3. Draft.
4. `brain_lint` on the draft, fix errors, check warnings against the ledger.
5. Return the draft with the capability statuses used and the rule it came closest to breaking.
