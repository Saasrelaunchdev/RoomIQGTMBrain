#!/usr/bin/env python3
"""
RoomIQ GTM Brain as a Model Context Protocol (MCP) server. Standard library only.

Transport: stdio, newline-delimited JSON-RPC 2.0, as in the MCP specification. Works with any MCP
client: Claude Code, Claude Desktop, Cursor, Windsurf, VS Code (Copilot agent mode), Zed, Codex
CLI, Gemini CLI, and agent frameworks with an MCP adapter.

    python3 tools/mcp_server.py                 read-only (default)
    python3 tools/mcp_server.py --allow-write   also expose brain_log_signal and brain_log_activity
    ROOMIQ_BRAIN_WRITE=1 python3 tools/mcp_server.py

Exposes:
  tools      load the control layer, load per task, search, read, status, glossary, decisions,
             lint, metrics, and (opt-in) append-only logging
  resources  every brain file as brain:///<path>
  prompts    every recurring job in prompts/common-tasks.md

Nothing is written to stdout except protocol messages. Diagnostics go to stderr.
"""

from __future__ import annotations

import json
import os
import re
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brain_lib as B  # noqa: E402

SUPPORTED_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"]
ALLOW_WRITE = "--allow-write" in sys.argv or os.environ.get("ROOMIQ_BRAIN_WRITE") == "1"
READABLE_SUFFIXES = (".md", ".txt", ".json", ".jsonl", ".mdc", ".yml", ".yaml")

INSTRUCTIONS = (
    "This server is the RoomIQ go-to-market brain: the source of truth for RoomIQ positioning, "
    "claims, product status, and voice. Before writing anything customer-facing about RoomIQ, call "
    "brain_load_control_layer once per session, then brain_load_for_task for the job. Check every "
    "capability with brain_feature_status and run brain_lint on drafts before returning them. Never "
    "claim forecast accuracy, never name a data source, never state prices or invented proof."
)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def text_result(text: str, is_error: bool = False) -> dict:
    return {"content": [{"type": "text", "text": text}], "isError": is_error}


def json_result(obj) -> dict:
    return text_result(json.dumps(obj, indent=2, ensure_ascii=False))


def concat(files: list[str]) -> str:
    return "\n\n".join(f"<<<FILE {f}>>>\n{B.read(f).strip()}\n<<<END {f}>>>" for f in files)


def safe_path(path: str) -> Path:
    p = (B.ROOT / path.lstrip("/")).resolve()
    if B.ROOT not in p.parents and p != B.ROOT:
        raise ValueError("path escapes the brain repository")
    if ".git" in p.relative_to(B.ROOT).parts or not p.is_file() or p.suffix not in READABLE_SUFFIXES:
        raise ValueError(f"not a readable brain file: {path}")
    return p


# ---------------------------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------------------------

def t_control_layer(_args):
    return text_result(concat(B.CONTROL_LAYER))


def t_load_for_task(args):
    task = args.get("task", "")
    if task not in B.LOAD_POLICY:
        return text_result(f"Unknown task. Choose one of: {', '.join(B.LOAD_POLICY)}", True)
    files = [f for f in B.LOAD_POLICY[task] if f not in B.CONTROL_LAYER]
    if args.get("include_control_layer", False):
        files = B.CONTROL_LAYER + files
    return text_result(concat(files))


def t_search(args):
    return json_result(B.search(args["query"], int(args.get("limit", 8)), bool(args.get("include_sources", False))))


def t_read(args):
    p = safe_path(args["path"])
    return text_result(p.read_text(encoding="utf-8"))


def t_status(args):
    feats = B.parse_features()
    q = (args.get("query") or "").lower().strip()
    if q:
        feats = [f for f in feats if q in f["id"].lower() or q in f["name"].lower()
                 or any(q in a for a in f["aliases"]) or q == f["status"].lower()]
    legend = ("SHIPPED: present tense, describe only what was seen. PARTIAL: describe the visible part. "
              "UNVERIFIED: name it, never describe its output. IN BUILD: 'coming soon' or omit. "
              "ROADMAP: never mention externally.")
    return json_result({"legend": legend, "capabilities": feats})


def t_glossary(args):
    rows = B.parse_glossary()
    term = (args.get("term") or "").lower()
    if term:
        rows = [r for r in rows if term in r["term"].lower() or term in r["rule"].lower()]
    return json_result(rows)


def t_decisions(args):
    ds = B.parse_decisions()
    st = (args.get("status") or "").upper()
    if st:
        ds = [d for d in ds if d["status"] == st]
    return json_result(ds)


def t_lint(args):
    return json_result(B.lint(args["text"]))


def t_metrics(_args):
    return json_result(B.metrics())


def t_log_signal(args):
    if not ALLOW_WRITE:
        return text_result("Writes are disabled. Start the server with --allow-write or ROOMIQ_BRAIN_WRITE=1.", True)
    return text_result(B.log_signal(args["type"], args["source"], args["verbatim"], args.get("context", ""),
                                    args.get("disposition", "UNTRIAGED")))


def t_log_activity(args):
    if not ALLOW_WRITE:
        return text_result("Writes are disabled. Start the server with --allow-write or ROOMIQ_BRAIN_WRITE=1.", True)
    return text_result(B.log_activity(args["type"], args["title"], args["what"], args.get("audience", "internal"),
                                      args.get("linked", "none"), args["expected"]))


def _obj(props: dict, required: list[str] | None = None) -> dict:
    return {"type": "object", "properties": props, "required": required or [], "additionalProperties": False}


TOOLS = [
    ("brain_load_control_layer",
     "Load the RoomIQ control layer: router, writing rules, do-not-say ledger, feature status, glossary, "
     "and QA checklist. Call once per session before writing anything customer-facing.",
     _obj({}), t_control_layer, True),
    ("brain_load_for_task",
     "Load the files a specific job needs, per the brain's load policy (demo, landing_page, content, "
     "competitive, product_copy, release_note, support, strategy, signal_intake, experiment, and more).",
     _obj({"task": {"type": "string", "enum": list(B.LOAD_POLICY)},
           "include_control_layer": {"type": "boolean", "default": False}}, ["task"]),
     t_load_for_task, True),
    ("brain_search",
     "Search the brain (BM25 over heading-level sections, boosted by authority: rules outrank examples). "
     "Returns path, heading, layer, score, snippet.",
     _obj({"query": {"type": "string"}, "limit": {"type": "integer", "default": 8, "minimum": 1, "maximum": 30},
           "include_sources": {"type": "boolean", "default": False}}, ["query"]),
     t_search, True),
    ("brain_read", "Read one brain file by repository-relative path, for example rules/do-not-say.md.",
     _obj({"path": {"type": "string"}}, ["path"]), t_read, True),
    ("brain_feature_status",
     "Look up what may be claimed about a RoomIQ capability: SHIPPED, PARTIAL, UNVERIFIED, IN BUILD, ROADMAP. "
     "Query by ID (C27), name, alias, or status. Empty query returns all.",
     _obj({"query": {"type": "string"}}), t_status, True),
    ("brain_glossary", "Canonical RoomIQ vocabulary and the rule for each term. Optional filter.",
     _obj({"term": {"type": "string"}}), t_glossary, True),
    ("brain_decisions", "Dated strategic decisions with status DECIDED, WORKING, or OPEN. Optional status filter.",
     _obj({"status": {"type": "string", "enum": ["DECIDED", "WORKING", "OPEN"]}}), t_decisions, True),
    ("brain_lint",
     "Run the mechanical part of the QA checklist on a draft: em dashes, banned words, do-not-say phrases, "
     "capability status, superlatives, price patterns, the fallback clause. Returns findings with fixes.",
     _obj({"text": {"type": "string"}}, ["text"]), t_lint, True),
    ("brain_metrics",
     "Innovation accounting rollup: signals, activities, experiments, assumptions, decisions, ledger "
     "staleness, open WATCH items.",
     _obj({}), t_metrics, True),
    ("brain_log_signal",
     "Append a market signal to ops/signal-log.md, verbatim, disposition UNTRIAGED by default. "
     "Requires the server to run with --allow-write.",
     _obj({"type": {"type": "string", "enum": list(B.SIGNAL_TYPES)}, "source": {"type": "string"},
           "verbatim": {"type": "string"}, "context": {"type": "string"},
           "disposition": {"type": "string", "default": "UNTRIAGED"}}, ["type", "source", "verbatim"]),
     t_log_signal, False),
    ("brain_log_activity",
     "Append an activity to ops/activity-log.md with the expected outcome written first. "
     "Requires the server to run with --allow-write.",
     _obj({"type": {"type": "string", "enum": list(B.ACTIVITY_TYPES)}, "title": {"type": "string"},
           "what": {"type": "string"}, "audience": {"type": "string"}, "linked": {"type": "string"},
           "expected": {"type": "string"}}, ["type", "title", "what", "expected"]),
     t_log_activity, False),
]
TOOL_FN = {name: fn for name, _, _, fn, _ in TOOLS}


def tools_list():
    out = []
    for name, desc, schema, _fn, read_only in TOOLS:
        out.append({"name": name, "description": desc, "inputSchema": schema,
                    "annotations": {"readOnlyHint": read_only, "destructiveHint": False,
                                    "idempotentHint": read_only, "openWorldHint": False}})
    return {"tools": out}


# ---------------------------------------------------------------------------------------------
# Resources and prompts
# ---------------------------------------------------------------------------------------------

def resources_list():
    purposes = {p: d for _, p, d in B.llms_index()}
    res = []
    for f in B.content_files(include_sources=True):
        res.append({"uri": f"brain:///{f}", "name": f, "title": f,
                    "description": purposes.get(f, B.layer_of(f) + " layer"),
                    "mimeType": "text/markdown" if f.endswith(".md") else "text/plain"})
    return {"resources": res}


def resources_read(params):
    uri = params.get("uri", "")
    if not uri.startswith("brain:///"):
        raise ValueError("unknown resource uri")
    path = uri[len("brain:///"):]
    p = safe_path(path)
    return {"contents": [{"uri": uri, "mimeType": "text/markdown" if path.endswith(".md") else "text/plain",
                          "text": p.read_text(encoding="utf-8")}]}


def _prompts():
    text = B.read("prompts/common-tasks.md")
    out = {}
    for m in re.finditer(r'^## (.+?)\n"(.+?)"\s*$', text, re.M | re.S):
        title, body = m.group(1).strip(), m.group(2).strip()
        out[B.slug(title)] = (title, body)
    return out


def prompts_list():
    return {"prompts": [{"name": k, "title": t, "description": f"RoomIQ GTM task: {t}",
                         "arguments": [{"name": "details", "description": "Fill the bracketed parts: audience, "
                                        "stage, paste, metro, IDs.", "required": False}]}
                        for k, (t, _b) in _prompts().items()]}


def prompts_get(params):
    name = params.get("name", "")
    prompts = _prompts()
    if name not in prompts:
        raise ValueError(f"unknown prompt {name}")
    title, body = prompts[name]
    details = (params.get("arguments") or {}).get("details", "")
    text = ("Load the RoomIQ control layer first (brain_load_control_layer).\n\n" + body
            + (f"\n\nDetails: {details}" if details else ""))
    return {"description": title, "messages": [{"role": "user", "content": {"type": "text", "text": text}}]}


# ---------------------------------------------------------------------------------------------
# JSON-RPC loop
# ---------------------------------------------------------------------------------------------

def handle(msg: dict):
    method, params, mid = msg.get("method"), msg.get("params") or {}, msg.get("id")
    if method is None:
        return None  # a response from the client; nothing to do
    if mid is None:
        return None  # notification (initialized, cancelled, ...)
    try:
        if method == "initialize":
            requested = params.get("protocolVersion", SUPPORTED_VERSIONS[0])
            version = requested if requested in SUPPORTED_VERSIONS else SUPPORTED_VERSIONS[0]
            result = {"protocolVersion": version,
                      "capabilities": {"tools": {"listChanged": False},
                                       "resources": {"subscribe": False, "listChanged": False},
                                       "prompts": {"listChanged": False}},
                      "serverInfo": {"name": "roomiq-gtm-brain", "title": "RoomIQ GTM Brain",
                                     "version": B.brain_version()["version"]},
                      "instructions": INSTRUCTIONS}
        elif method == "ping":
            result = {}
        elif method == "tools/list":
            result = tools_list()
        elif method == "tools/call":
            name = params.get("name")
            if name not in TOOL_FN:
                return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": f"Unknown tool: {name}"}}
            try:
                result = TOOL_FN[name](params.get("arguments") or {})
            except (KeyError, ValueError) as e:
                result = text_result(f"{type(e).__name__}: {e}", True)
        elif method == "resources/list":
            result = resources_list()
        elif method == "resources/templates/list":
            result = {"resourceTemplates": []}
        elif method == "resources/read":
            result = resources_read(params)
        elif method == "prompts/list":
            result = prompts_list()
        elif method == "prompts/get":
            result = prompts_get(params)
        else:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"Method not found: {method}"}}
        return {"jsonrpc": "2.0", "id": mid, "result": result}
    except ValueError as e:
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": str(e)}}
    except Exception as e:  # never crash the session
        log(traceback.format_exc())
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32603, "message": f"Internal error: {e}"}}


def main():
    log(f"roomiq-gtm-brain MCP server, brain v{B.brain_version()['version']}, writes "
        f"{'enabled' if ALLOW_WRITE else 'disabled'}, root {B.ROOT}")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}
        else:
            if isinstance(msg, list):  # JSON-RPC batch, accepted for older clients
                resps = [r for r in (handle(m) for m in msg) if r is not None]
                resp = resps or None
            else:
                resp = handle(msg)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
