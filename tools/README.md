# Tools, the brain as an executable system

Python 3.9+ standard library only. No install step, no network calls, no third-party packages. Markdown stays the source of truth; these tools read it, check it, export it, and append to its logs.

| File | What it is |
|---|---|
| `brain_lib.py` | Shared parsers (ledgers, logs, decisions, experiments), linter, BM25 search, exports, adapter renderer |
| `brain.py` | The CLI. Run with `--help` |
| `mcp_server.py` | The brain over MCP (stdio JSON-RPC). See `adapters/mcp/README.md` |
| `templates/pointer-body.md.tmpl` | The single source for every tool adapter |
| `tests/test_brain.py` | Unit tests: parsers, linter, writers, adapters, MCP handshake |

## Common commands

```bash
python3 tools/brain.py audit                      # what CI runs
python3 tools/brain.py lint drafts/landing.md     # mechanical QA, exit 1 on errors
python3 tools/brain.py status unverified          # what may not be described
python3 tools/brain.py search "data source objection"
python3 tools/brain.py load demo --paths          # files a demo task loads
python3 tools/brain.py metrics                    # innovation accounting rollup
python3 tools/brain.py build                      # regenerate dist/
python3 tools/brain.py adapters --write           # regenerate tool adapters
python3 -m unittest discover -s tools/tests -v
```

Intake from the shell:

```bash
python3 tools/brain.py log-signal --type OBJECTION --source "demo, Dallas investor" \
  --verbatim "Where does your data come from?" --context "Stage 4, design partner"

python3 tools/brain.py log-activity --type DEMO --title "Design-partner session 1" \
  --what "Ran a Dallas townhouse through the Predictor" --audience A \
  --linked "EXP-001, A1, A2" --expected "Investor asks to run a second address within 7 days"
```

## Contracts other code can rely on
- `dist/ledgers.json`: features, claims, glossary, decisions, assumptions, experiments, signals, activities.
- `dist/brain.chunks.jsonl`: one JSON object per heading-level section, with `path`, `layer`, `always_load`, `heading`, `last_reviewed`, `brain_version`, `tokens_est`, `text`.
- `dist/brain.manifest.json`: every file with layer, purpose, size, token estimate, hash, and the load policy.
- `schemas/*.schema.json`: JSON Schema (2020-12) for signal, activity, experiment, assumption, decision, and feature objects. Webhook producers validate against these.

## Design rules for changes here
- Never write to `rules/` or `context/` from a tool. Ledger changes go through a reviewed pull request.
- Appends are the only writes, and they always carry the verbatim or the expected outcome.
- Output must be deterministic so `build --check` and `adapters --check` can gate CI.
