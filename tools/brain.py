#!/usr/bin/env python3
"""
RoomIQ GTM Brain CLI. Standard library only.

    python3 tools/brain.py audit                 skill audit + structural checks (CI runs this)
    python3 tools/brain.py lint draft.md         mechanical QA on a draft (or '-' for stdin)
    python3 tools/brain.py status [query]        feature status ledger, filtered
    python3 tools/brain.py search "query"        BM25 search over the brain, authority-boosted
    python3 tools/brain.py load demo             print the files a task loads (control layer first)
    python3 tools/brain.py glossary [term]       canonical vocabulary
    python3 tools/brain.py log-signal ...        append a signal (verbatim first)
    python3 tools/brain.py log-activity ...      append an activity (expected outcome first)
    python3 tools/brain.py new-experiment ...    append a pre-registered experiment
    python3 tools/brain.py ingest --payload-env PAYLOAD --event brain-signal
                                                 append from a JSON payload (webhooks, CI)
    python3 tools/brain.py metrics [--json]      innovation accounting and learning velocity
    python3 tools/brain.py build [--check]       regenerate dist/ (bundle, llms-full, chunks, ledgers)
    python3 tools/brain.py adapters [--check|--write|--install REPO --brain-path PATH]
    python3 tools/brain.py validate              schema and cross-reference checks only

Exit codes: 0 ok, 1 findings that fail the check, 2 bad usage.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brain_lib as B  # noqa: E402

try:
    from signal import SIG_DFL, SIGPIPE, signal
    signal(SIGPIPE, SIG_DFL)
except (ImportError, AttributeError, ValueError):
    pass


def out(obj, as_json: bool):
    if as_json:
        print(json.dumps(obj, indent=2, ensure_ascii=False))
        return True
    return False


# ---------------------------------------------------------------------------------------------

def structural_checks() -> tuple[list[str], list[str]]:
    """Checks the skill's audit does not know about: ledgers parse, IDs cross-reference,
    generated files are fresh, adapters match their template, the portable layer is current."""
    errors, warns = [], []
    feats = B.parse_features()
    ids = [f["id"] for f in feats]
    if len([i for i in ids if i.startswith("C")]) != 32:
        errors.append(f"feature-status.md: expected 32 C-capabilities, parsed {len([i for i in ids if i.startswith('C')])}")
    if len(ids) != len(set(ids)):
        errors.append("feature-status.md: duplicate capability IDs")
    assumptions = {a["id"]: a for a in B.parse_assumptions()}
    for a in assumptions.values():
        errors += B.validate(a, "assumption")
    exps = B.parse_experiments()
    exp_ids = {e["id"] for e in exps}
    for e in exps:
        errors += [f"{e['id']}: {m}" for m in B.validate(e, "experiment")]
        for t in re.findall(r"\b[ARG]\d+\b", e.get("tests", "")):
            if t not in assumptions:
                errors.append(f"{e['id']} tests {t}, which is not in innovation/assumptions.md")
    for a in assumptions.values():
        for x in re.findall(r"EXP-\d{3}", a["tested_by"]):
            if x not in exp_ids:
                errors.append(f"assumption {a['id']} names {x}, which is not in innovation/experiments.md")
    for s in B.parse_signals():
        errors += [f"signal {s['date']} {s['type']}: {m}" for m in B.validate(s, "signal")]
    act_ids = []
    for a in B.parse_activities():
        errors += [f"activity {a.get('id', '?')}: {m}" for m in B.validate(a, "activity")]
        act_ids.append(a.get("id"))
    if len(act_ids) != len(set(act_ids)):
        errors.append("activity-log.md: duplicate ACT ids")
    for d in B.parse_decisions():
        errors += [f"decision {d['id']}: {m}" for m in B.validate(d, "decision")]
    # Generated files
    for path, content in B.dist_outputs().items():
        disk = B.ROOT / path
        if not disk.exists() or disk.read_text(encoding="utf-8") != content:
            errors.append(f"{path} is stale; run python3 tools/brain.py build")
    for dest, content in B.adapter_plan(B.ROOT, "", False).items():
        if not dest.exists() or dest.read_text(encoding="utf-8") != content:
            errors.append(f"adapter {B.rel(dest)} is stale; run python3 tools/brain.py adapters --write")
    for dest, content in B.adapter_plan(B.ROOT / "adapters" / "consuming-repo", "gtm-brain/", True).items():
        if not dest.exists() or dest.read_text(encoding="utf-8") != content:
            errors.append(f"adapter {B.rel(dest)} is stale; run python3 tools/brain.py adapters --write")
    # The portable control layer carries ledger content, so it must be at least as new as the ledgers.
    portable = B.ROOT / "adapters" / "portable-control-layer.md"
    if portable.exists():
        m = re.search(r"(\d{4}-\d{2}-\d{2})", "\n".join(portable.read_text(encoding="utf-8").splitlines()[:12]))
        newest = max(filter(None, (B.last_reviewed(B.read(f)) for f in
                                   ["rules/feature-status.md", "rules/do-not-say.md",
                                    "rules/glossary.md", "rules/writing-rules.md"])))
        if not m:
            errors.append("adapters/portable-control-layer.md has no generation date in its header")
        elif m.group(1) < newest:
            errors.append(f"adapters/portable-control-layer.md ({m.group(1)}) is older than the newest ledger ({newest}); regenerate it")
    else:
        errors.append("adapters/portable-control-layer.md is missing")
    # The master context must not be newer than the control layer it summarizes.
    master_date = B.brain_version()["last_updated"]
    for f in ["rules/feature-status.md", "rules/do-not-say.md", "rules/glossary.md", "rules/writing-rules.md"]:
        lr = B.last_reviewed(B.read(f))
        if lr and master_date and lr < master_date:
            warns.append(f"{f} last_reviewed {lr} is older than the master context ({master_date}); a change may not have reached the control layer")
    if sum(1 for s in B.parse_signals() if s.get("disposition") == "UNTRIAGED") > 0:
        oldest = min(s["date"] for s in B.parse_signals() if s.get("disposition") == "UNTRIAGED")
        if (date.today() - date.fromisoformat(oldest)).days > 7:
            warns.append(f"UNTRIAGED signals older than 7 days (oldest {oldest}); run the weekly triage")
    return errors, warns


def cmd_audit(args) -> int:
    rc = 0
    audit_path = B.SKILL_DIR / "scripts" / "audit_brain.py"
    if audit_path.exists():
        spec = importlib.util.spec_from_file_location("audit_brain", audit_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        # The installed skill, generated files, and raw sources are not brain prose.
        mod.SKIP_DIRS.update({".claude", "dist", "sources"})
        argv = sys.argv
        sys.argv = ["audit_brain.py", str(B.ROOT)] + (["--quiet"] if args.quiet else [])
        try:
            rc = mod.main()
        finally:
            sys.argv = argv
    else:
        print(f"Skill audit not found at {audit_path}; reinstall the skill. Running structural checks only.")
    print("\nStructural checks (tools/brain.py):\n")
    errors, warns = structural_checks()
    for e in errors:
        print(f"  [ERROR] {e}")
    for w in warns:
        print(f"  [WARN] {w}")
    print(f"\n{len(errors)} error(s), {len(warns)} warning(s).")
    return 1 if (rc or errors) else 0


def cmd_validate(args) -> int:
    errors, warns = structural_checks()
    for e in errors:
        print(f"[ERROR] {e}")
    for w in warns:
        print(f"[WARN] {w}")
    print(f"{len(errors)} error(s), {len(warns)} warning(s).")
    return 1 if errors else 0


def cmd_lint(args) -> int:
    worst = 0
    for f in args.files:
        text = sys.stdin.read() if f == "-" else Path(f).read_text(encoding="utf-8")
        res = B.lint(text)
        if args.json:
            print(json.dumps({"file": f, **res}, indent=2, ensure_ascii=False))
        else:
            print(f"{f}: {res['errors']} error(s), {res['warnings']} warning(s), {res['info']} info")
            for x in res["findings"]:
                if x["severity"] == "info" and not args.verbose:
                    continue
                fix = f"  -> {x['fix']}" if x["fix"] else ""
                print(f"  {x['severity'].upper():5} L{x['line']:<4} {x['rule']}: {x['message']}{fix}")
            print(f"  {res['next']}")
        if res["errors"]:
            worst = 1
        if args.strict and res["warnings"]:
            worst = 1
    return worst


def cmd_status(args) -> int:
    feats = B.parse_features()
    if args.query:
        q = args.query.lower()
        feats = [f for f in feats if q in f["id"].lower() or q in f["name"].lower()
                 or any(q in a for a in f["aliases"]) or q == f["status"].lower()]
    if out(feats, args.json):
        return 0
    for f in feats:
        print(f"{f['id']}  {f['status']:<10}  {f['name']}  [{f['area']}]" + (f"  {f['note']}" if f["note"] else ""))
    return 0


def cmd_search(args) -> int:
    res = B.search(args.query, args.k, args.sources)
    if out(res, args.json):
        return 0
    for r in res:
        print(f"{r['score']:>7}  {r['path']}  ::  {r['heading']}\n         {r['snippet'][:180]}")
    return 0


def cmd_load(args) -> int:
    if args.list or not args.task:
        for k, v in B.LOAD_POLICY.items():
            print(f"{k:<14} {', '.join(v)}")
        return 0
    if args.task not in B.LOAD_POLICY:
        print(f"unknown task; choose from {', '.join(B.LOAD_POLICY)}", file=sys.stderr)
        return 2
    files = B.CONTROL_LAYER + [f for f in B.LOAD_POLICY[args.task] if f not in B.CONTROL_LAYER]
    if args.paths:
        print("\n".join(files))
        return 0
    for f in files:
        print(f"\n<<<FILE {f}>>>\n{B.read(f).strip()}\n<<<END {f}>>>")
    return 0


def cmd_glossary(args) -> int:
    rows = B.parse_glossary()
    if args.term:
        rows = [r for r in rows if args.term.lower() in r["term"].lower()]
    if out(rows, args.json):
        return 0
    for r in rows:
        print(f"{r['term']}: {r['rule']}")
    return 0


def cmd_log_signal(args) -> int:
    entry = B.log_signal(args.type, args.source, args.verbatim, args.context, args.disposition,
                         args.routed_to, args.date)
    print(entry)
    return 0


def cmd_log_activity(args) -> int:
    entry = B.log_activity(args.type, args.title, args.what, args.audience, args.linked,
                           args.expected, args.date)
    print(entry)
    return 0


def cmd_new_experiment(args) -> int:
    print(B.new_experiment(args.title, args.tests, args.audience, args.method, args.metric,
                           args.threshold, args.sample, args.end))
    return 0


def cmd_ingest(args) -> int:
    """Append from a JSON payload. Used by .github/workflows/brain-intake.yml and any webhook."""
    raw = os.environ.get(args.payload_env, "") if args.payload_env else Path(args.payload).read_text(encoding="utf-8")
    payload = json.loads(raw or "{}")
    if args.event in ("brain-signal", "signal"):
        payload.setdefault("disposition", "UNTRIAGED")
        payload.setdefault("date", date.today().isoformat())
        errs = B.validate(payload, "signal")
        if errs:
            print("\n".join(errs), file=sys.stderr)
            return 1
        print(B.log_signal(payload["type"], payload["source"], payload["verbatim"], payload.get("context", ""),
                           payload["disposition"], payload.get("routed_to", "none"), payload["date"]))
    elif args.event in ("brain-activity", "activity"):
        payload.setdefault("date", date.today().isoformat())
        payload.setdefault("id", B.next_activity_id())
        errs = B.validate(payload, "activity")
        if errs:
            print("\n".join(errs), file=sys.stderr)
            return 1
        print(B.log_activity(payload["type"], payload["title"], payload["what"], payload.get("audience", "internal"),
                             payload.get("linked", "none"), payload["expected"], payload["date"]))
    else:
        print("event must be brain-signal or brain-activity", file=sys.stderr)
        return 2
    return 0


def cmd_metrics(args) -> int:
    m = B.metrics()
    if out(m, args.json):
        return 0
    s, a, e, asm, d = m["signals"], m["activities"], m["experiments"], m["assumptions"], m["decisions"]
    print(f"# RoomIQ GTM Brain metrics, {m['as_of']} (brain v{m['brain']['version']})\n")
    print("## Learning velocity")
    print(f"- Signals: {s['total']} total, {s['last_7_days']} in 7 days, {s['last_30_days']} in 30 days, {s['untriaged']} untriaged")
    print(f"- Activities: {a['total']} total, {a['last_7_days']} in 7 days, {a['outcome_pending']} with outcome pending")
    print(f"- Experiments: {e['by_status']}  decisions {e['by_decision']}")
    print(f"- Assumptions: {asm['by_status']}; riskiest untested: {', '.join(asm['riskiest_untested'])}")
    print(f"- Decisions: {d['by_status']}, {d['last_30_days']} dated in the last 30 days")
    print(f"- Open WATCH items: {len(s['open_watch'])}")
    for w in s["open_watch"]:
        print(f"  - {w['date']} {w['type']} {w['count']}: {w['source']}")
    print("\n## Signals by type\n- " + ", ".join(f"{k} {v}" for k, v in sorted(s["by_type"].items())))
    print("\n## Capability status\n- " + ", ".join(f"{k} {v}" for k, v in m["features"].items()))
    print("\n## Ledger age (days)")
    for f, age in m["ledger_age_days"].items():
        print(f"- {f}: {age}")
    print(f"\n## Latest snapshot\n- {m['latest_snapshot']} ({m['snapshot_age_days']} days old)")
    return 0


def cmd_build(args) -> int:
    stale = []
    for path, content in B.dist_outputs().items():
        disk = B.ROOT / path
        current = disk.read_text(encoding="utf-8") if disk.exists() else None
        if current != content:
            stale.append(path)
            if not args.check:
                disk.parent.mkdir(parents=True, exist_ok=True)
                disk.write_text(content, encoding="utf-8")
    if args.check:
        for p in stale:
            print(f"stale: {p}")
        print("dist/ is up to date." if not stale else "Run: python3 tools/brain.py build")
        return 1 if stale else 0
    print("\n".join(f"wrote {p}" for p in stale) or "dist/ already up to date.")
    return 0


def cmd_adapters(args) -> int:
    targets = []
    if args.install:
        repo = Path(args.install).expanduser().resolve()
        if not repo.is_dir():
            print(f"not a directory: {repo}", file=sys.stderr)
            return 2
        prefix = args.brain_path.rstrip("/") + "/"
        targets = [(repo, prefix, True)]
    else:
        targets = [(B.ROOT, "", False), (B.ROOT / "adapters" / "consuming-repo", "gtm-brain/", True)]
    stale = 0
    for target, prefix, consuming in targets:
        for dest, content in B.adapter_plan(target, prefix, consuming).items():
            current = dest.read_text(encoding="utf-8") if dest.exists() else None
            if current == content:
                continue
            stale += 1
            label = dest.relative_to(target).as_posix()
            if args.check:
                print(f"stale: {target.name}/{label}")
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(content, encoding="utf-8")
                print(f"wrote {target.name}/{label}")
    if args.check:
        print("adapters are up to date." if not stale else "Run: python3 tools/brain.py adapters --write")
        return 1 if stale else 0
    if not stale:
        print("adapters already up to date.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("audit", help="skill audit plus structural checks")
    a.add_argument("--quiet", action="store_true")
    a.set_defaults(fn=cmd_audit)

    a = sub.add_parser("validate", help="structural checks only")
    a.set_defaults(fn=cmd_validate)

    a = sub.add_parser("lint", help="mechanical QA on drafts")
    a.add_argument("files", nargs="+")
    a.add_argument("--json", action="store_true")
    a.add_argument("--verbose", "-v", action="store_true", help="also show info findings")
    a.add_argument("--strict", action="store_true", help="fail on warnings too")
    a.set_defaults(fn=cmd_lint)

    a = sub.add_parser("status", help="feature status ledger")
    a.add_argument("query", nargs="?")
    a.add_argument("--json", action="store_true")
    a.set_defaults(fn=cmd_status)

    a = sub.add_parser("search", help="search the brain")
    a.add_argument("query")
    a.add_argument("-k", type=int, default=8)
    a.add_argument("--sources", action="store_true", help="include raw discovery sources")
    a.add_argument("--json", action="store_true")
    a.set_defaults(fn=cmd_search)

    a = sub.add_parser("load", help="print the files a task loads")
    a.add_argument("task", nargs="?")
    a.add_argument("--list", action="store_true")
    a.add_argument("--paths", action="store_true", help="paths only")
    a.set_defaults(fn=cmd_load)

    a = sub.add_parser("glossary", help="canonical vocabulary")
    a.add_argument("term", nargs="?")
    a.add_argument("--json", action="store_true")
    a.set_defaults(fn=cmd_glossary)

    a = sub.add_parser("log-signal", help="append to ops/signal-log.md")
    a.add_argument("--type", required=True, choices=B.SIGNAL_TYPES)
    a.add_argument("--source", required=True)
    a.add_argument("--verbatim", required=True)
    a.add_argument("--context", default="")
    a.add_argument("--disposition", default="UNTRIAGED")
    a.add_argument("--routed-to", default="none")
    a.add_argument("--date")
    a.set_defaults(fn=cmd_log_signal)

    a = sub.add_parser("log-activity", help="append to ops/activity-log.md")
    a.add_argument("--type", required=True, choices=B.ACTIVITY_TYPES)
    a.add_argument("--title", required=True)
    a.add_argument("--what", required=True)
    a.add_argument("--audience", default="internal")
    a.add_argument("--linked", default="none")
    a.add_argument("--expected", required=True)
    a.add_argument("--date")
    a.set_defaults(fn=cmd_log_activity)

    a = sub.add_parser("new-experiment", help="append a pre-registered experiment")
    for flag in ("title", "tests", "audience", "method", "metric", "threshold", "sample", "end"):
        a.add_argument(f"--{flag}", required=True)
    a.set_defaults(fn=cmd_new_experiment)

    a = sub.add_parser("ingest", help="append from a JSON payload")
    a.add_argument("--event", required=True)
    g = a.add_mutually_exclusive_group(required=True)
    g.add_argument("--payload-env", help="name of an environment variable holding the JSON")
    g.add_argument("--payload", help="path to a JSON file")
    a.set_defaults(fn=cmd_ingest)

    a = sub.add_parser("metrics", help="innovation accounting rollup")
    a.add_argument("--json", action="store_true")
    a.set_defaults(fn=cmd_metrics)

    a = sub.add_parser("build", help="regenerate dist/")
    a.add_argument("--check", action="store_true")
    a.set_defaults(fn=cmd_build)

    a = sub.add_parser("adapters", help="render tool adapters from tools/templates/")
    g = a.add_mutually_exclusive_group()
    g.add_argument("--check", action="store_true")
    g.add_argument("--write", action="store_true")
    g.add_argument("--install", metavar="REPO", help="write consuming-repo adapters into another repo")
    a.add_argument("--brain-path", default="gtm-brain", help="path from REPO to this brain")
    a.set_defaults(fn=cmd_adapters)

    args = p.parse_args()
    if args.cmd == "adapters" and not (args.check or args.write or args.install):
        args.check = True
    try:
        return args.fn(args)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
