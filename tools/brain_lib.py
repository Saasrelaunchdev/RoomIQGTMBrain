"""
Shared parsing, linting, search, export, and adapter rendering for the RoomIQ GTM Brain.

Standard library only (Python 3.9+). Markdown is the source of truth; everything here reads
it, and the only writes are append-only log entries and generated files under dist/ and the
adapter locations. Imported by tools/brain.py (CLI), tools/mcp_server.py (MCP), and the tests.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
MASTER = "context/RoomIQ_GTM_Master_Context.md"
SKILL_DIR = ROOT / ".claude" / "skills" / "go-to-market-brain"
TEMPLATES_DIR = ROOT / "tools" / "templates"
DIST = ROOT / "dist"
SCHEMAS = ROOT / "schemas"

STATUSES = ("SHIPPED", "PARTIAL", "UNVERIFIED", "IN BUILD", "ROADMAP")
SIGNAL_TYPES = ("OBJECTION", "LANGUAGE", "PROOF", "STATUS", "COMPETITIVE", "SEGMENT",
                "CHANNEL", "LOSS", "RISK")
ACTIVITY_TYPES = ("DEMO", "CALL", "CONTENT", "COMMUNITY", "RELEASE", "EXPERIMENT", "OUTREACH",
                  "PARTNERSHIP", "PRICING", "COVERAGE", "RESEARCH", "BRAIN")
DISPOSITION_RE = re.compile(r"^(UNTRIAGED|NOISE|PATCH|AMEND|WATCH \(\d+/\d+\))$")

# The always-loaded control layer, in load order. Guardrails come last in bundles.
CONTROL_LAYER = [
    "AGENTS.md",
    "rules/writing-rules.md",
    "rules/do-not-say.md",
    "rules/feature-status.md",
    "rules/glossary.md",
    "ops/QA-checklist.md",
]

# Task -> files loaded on top of the control layer. Mirrors the load policy in the skill's
# blueprint, instantiated for RoomIQ. The MCP tool brain_load_for_task and `brain.py load` use it.
LOAD_POLICY: dict[str, list[str]] = {
    "landing_page": ["reference/positioning.md", "reference/value-proposition-investors.md",
                     "reference/value-proposition-operators.md", "reference/objection-handling.md",
                     "templates/landing-page.md", "examples/landing-hero-investors.md",
                     "ops/copy-bank.md"],
    "one_pager": ["reference/positioning.md", "reference/metrics-methodology.md",
                  "templates/one-pager.md", "examples/one-pager-investors.md", "ops/copy-bank.md"],
    "demo": ["reference/demo-playbook.md", "reference/product-surface.md",
             "templates/demo-script.md", "examples/demo-talk-track.md"],
    "content": ["reference/content-engine.md", "reference/customer-journey.md",
                "templates/seo-article.md", "templates/social-post.md", "ops/copy-bank.md"],
    "community": ["reference/content-engine.md", "templates/community-answer.md",
                  "examples/community-answer-operators.md"],
    "outreach": ["reference/marketing-campaigns.md", "templates/outreach-warm.md",
                 "reference/icp-personas.md"],
    "competitive": ["reference/competitive-analysis.md", "reference/competitor-battlecards.md",
                    "reference/objection-handling.md"],
    "objection": ["reference/objection-handling.md", "reference/trust-and-risk.md"],
    "product_copy": ["templates/in-app-copy.md", "examples/in-app-copy-fixes.md",
                     "reference/metrics-methodology.md", "reference/product-surface.md"],
    "release_note": ["templates/release-note.md", "reference/product-surface.md"],
    "support": ["reference/metrics-methodology.md", "reference/product-surface.md",
                "reference/objection-handling.md"],
    "strategy": [MASTER, "ops/decisions.md", "reference/positioning.md",
                 "reference/icp-personas.md", "reference/feature-matrix.md"],
    "pricing": ["reference/pricing-packaging.md", "ops/decisions.md"],
    "signal_intake": ["ops/signal-log.md", "ops/decisions.md", "innovation/assumptions.md",
                      "reference/innovation-accounting.md"],
    "experiment": ["reference/innovation-accounting.md", "innovation/assumptions.md",
                   "innovation/experiments.md", "innovation/metrics.md"],
    "snapshot": ["innovation/metrics.md", "innovation/assumptions.md", "ops/decisions.md"],
}

# Directories whose Markdown is brain content (searchable, exportable).
CONTENT_DIRS = ["context", "rules", "reference", "innovation", "ops", "snapshots", "templates",
                "examples", "prompts", "pages"]
ROOT_FILES = ["CLAUDE.md", "AGENTS.md", "GEMINI.md", "README.md", "llms.txt"]

LAYER_BY_DIR = {
    "context": "reference", "rules": "control", "reference": "reference",
    "innovation": "state", "ops": "state", "snapshots": "state", "templates": "execution",
    "examples": "execution", "prompts": "execution", "pages": "execution",
    "adapters": "adapter", "sources": "source",
}


# ---------------------------------------------------------------------------------------------
# Files and layers
# ---------------------------------------------------------------------------------------------

def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def read(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")


def layer_of(relpath: str) -> str:
    if relpath in ("CLAUDE.md", "AGENTS.md", "GEMINI.md", "llms.txt", "README.md"):
        return "router"
    if relpath == "ops/QA-checklist.md":
        return "control"
    return LAYER_BY_DIR.get(relpath.split("/", 1)[0], "other")


def content_files(include_sources: bool = False) -> list[str]:
    """Brain content in a stable order: routers, then layers, alphabetical within each."""
    out = [f for f in ROOT_FILES if (ROOT / f).exists()]
    dirs = CONTENT_DIRS + ["adapters"] + (["sources"] if include_sources else [])
    for d in dirs:
        base = ROOT / d
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.suffix not in (".md", ".txt"):
                continue
            r = rel(p)
            if d == "adapters" and r not in ("adapters/README.md", "adapters/portable-control-layer.md"):
                continue
            out.append(r)
    return out


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    meta = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def last_reviewed(text: str) -> str | None:
    m = re.search(r"(?:last_reviewed|last_updated)\s*:\s*(\d{4}-\d{2}-\d{2})", text)
    return m.group(1) if m else None


def brain_version() -> dict[str, str]:
    meta = frontmatter(read(MASTER))
    return {"version": meta.get("version", "0"), "last_updated": meta.get("last_updated", "")}


def llms_index() -> list[tuple[str, str, str]]:
    """(title, path, purpose) for every Markdown link in llms.txt, in order."""
    out = []
    for m in re.finditer(r"^- \[([^\]]+)\]\(([^)]+)\)(?::\s*(.*))?$", read("llms.txt"), re.M):
        out.append((m.group(1), m.group(2), (m.group(3) or "").strip()))
    return out


def headings(text: str) -> list[tuple[int, str, int]]:
    """(level, title, line index) for Markdown headings outside code fences."""
    out, fence = [], False
    for i, line in enumerate(text.splitlines()):
        if line.startswith("```"):
            fence = not fence
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m and not fence:
            out.append((len(m.group(1)), m.group(2).strip(), i))
    return out


def sections(relpath: str) -> list[dict]:
    """Split a file at H2 and H3 headings. Each section keeps its heading path."""
    text = read(relpath)
    lines = text.splitlines()
    hs = [h for h in headings(text) if h[0] in (1, 2, 3)]
    title = next((t for lvl, t, _ in hs if lvl == 1), relpath)
    cuts = [h for h in hs if h[0] in (2, 3)]
    out = []
    if not cuts:
        return [{"path": relpath, "title": title, "heading": title, "text": text.strip()}]
    first = cuts[0][2]
    if any(l.strip() for l in lines[:first]):
        out.append({"path": relpath, "title": title, "heading": title,
                    "text": "\n".join(lines[:first]).strip()})
    h2 = ""
    for idx, (lvl, t, start) in enumerate(cuts):
        end = cuts[idx + 1][2] if idx + 1 < len(cuts) else len(lines)
        if lvl == 2:
            h2 = t
        heading = t if lvl == 2 else f"{h2} > {t}" if h2 else t
        body = "\n".join(lines[start:end]).strip()
        if body:
            out.append({"path": relpath, "title": title, "heading": heading, "text": body})
    return out


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80]


def sha(text: str, n: int = 12) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:n]


# ---------------------------------------------------------------------------------------------
# Ledger parsers
# ---------------------------------------------------------------------------------------------

FEATURE_RE = re.compile(
    r"^- \*\*(?P<id>[CR]\d{2}) (?P<name>.+?)\*\*(?: \[(?P<aliases>[^\]]*)\])?: "
    r"(?P<status>SHIPPED|PARTIAL|UNVERIFIED|IN BUILD|ROADMAP)\.\s*(?P<note>.*)$")


def parse_features() -> list[dict]:
    area, out = "", []
    for line in read("rules/feature-status.md").splitlines():
        if line.startswith("## "):
            area = line[3:].strip()
            continue
        m = FEATURE_RE.match(line)
        if m:
            aliases = [a.strip().lower() for a in (m.group("aliases") or "").split(",") if a.strip()]
            out.append({"id": m.group("id"), "name": m.group("name"), "area": area,
                        "status": m.group("status"), "aliases": aliases,
                        "note": m.group("note").strip()})
    return out


def _table_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
    return rows


def _section(text: str, heading_prefix: str) -> str:
    m = re.search(rf"^## {re.escape(heading_prefix)}.*?$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def parse_claims() -> list[dict]:
    """Rows of the do-not-say ledger with their quoted trigger phrases."""
    text = read("rules/do-not-say.md")
    out = []
    for cells in _table_rows(_section(text, "Hard bans"))[1:]:
        if len(cells) < 2:
            continue
        out.append({"kind": "hard_ban", "do_not_say": cells[0], "say_instead": cells[1],
                    "phrases": re.findall(r'"([^"]+)"', cells[0])})
    fair = _section(text, "Fair housing")
    m = re.search(r"Do not say (.*?)\. Say instead: (.*?)$", fair, re.M | re.S)
    if m:
        out.append({"kind": "fair_housing", "do_not_say": m.group(1).strip(),
                    "say_instead": m.group(2).strip(), "phrases": re.findall(r'"([^"]+)"', m.group(1))})
    return out


def parse_glossary() -> list[dict]:
    out, group = [], ""
    for line in read("rules/glossary.md").splitlines():
        if line.startswith("## "):
            group = line[3:].strip()
        elif line.startswith("|") and not re.match(r"^\|\s*(-|Term\b)", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2:
                out.append({"group": group, "term": cells[0], "rule": cells[1]})
    return out


DECISION_RE = re.compile(r"^## (?P<date>\d{4}-\d{2}(?:-\d{2})?) (?P<id>D-\d+) (?P<title>.+?) "
                         r"\((?P<status>DECIDED|WORKING|OPEN)\)\s*$")


def parse_decisions() -> list[dict]:
    lines = read("ops/decisions.md").splitlines()
    out = []
    matches = [(m, i) for i, line in enumerate(lines) for m in [DECISION_RE.match(line)] if m]
    for idx, (m, start) in enumerate(matches):
        end = matches[idx + 1][1] if idx + 1 < len(matches) else len(lines)
        body = "\n".join(lines[start + 1:end]).split("\n---")[0].strip()
        out.append({"id": m.group("id"), "date": m.group("date"), "title": m.group("title"),
                    "status": m.group("status"), "body": body})
    return out


def _entries(relpath: str, header_re: re.Pattern) -> list[dict]:
    """Generic parser for '### header' entries followed by '**Field:** value' lines."""
    lines = read(relpath).splitlines()
    out, cur = [], None
    for line in lines:
        m = header_re.match(line)
        if m:
            cur = {k: v.strip() for k, v in m.groupdict().items()}
            out.append(cur)
            continue
        if cur is None:
            continue
        if line.startswith("## ") or line.strip() == "---":
            cur = None
            continue
        f = re.match(r"^(?:- )?\*\*([A-Za-z ()]+):\*\*\s*(.*)$", line)
        if f:
            cur[f.group(1).strip().lower().replace(" ", "_").replace("(", "").replace(")", "")] = f.group(2).strip()
    return out


SIGNAL_HDR = re.compile(r"^### (?P<date>\d{4}-\d{2}-\d{2}) \| (?P<type>[A-Z]+) \| (?P<source>.+)$")
ACTIVITY_HDR = re.compile(r"^### (?P<date>\d{4}-\d{2}-\d{2}) \| (?P<type>[A-Z]+) \| (?P<title>.+)$")
EXPERIMENT_HDR = re.compile(r"^### (?P<id>EXP-\d{3}) \| (?P<title>.+)$")


def parse_signals() -> list[dict]:
    return _entries("ops/signal-log.md", SIGNAL_HDR)


def parse_activities() -> list[dict]:
    return _entries("ops/activity-log.md", ACTIVITY_HDR)


def parse_experiments() -> list[dict]:
    return _entries("innovation/experiments.md", EXPERIMENT_HDR)


def parse_assumptions() -> list[dict]:
    out = []
    for cells in _table_rows(read("innovation/assumptions.md")):
        if len(cells) >= 7 and re.fullmatch(r"[ARG]\d+", cells[0]):
            out.append({"id": cells[0], "assumption": cells[1], "type": cells[2],
                        "riskiness": int(cells[3]) if cells[3].isdigit() else None,
                        "status": cells[4], "evidence": cells[5], "tested_by": cells[6]})
    return out


def latest_snapshot() -> str | None:
    snaps = sorted((ROOT / "snapshots").glob("[0-9][0-9][0-9][0-9]-*.md"))
    return rel(snaps[-1]) if snaps else None


# ---------------------------------------------------------------------------------------------
# Lint: the mechanical part of ops/QA-checklist.md
# ---------------------------------------------------------------------------------------------

SUPERLATIVES = ["only", "first", "best", "never", "most", "fastest", "no other", "#1",
                "number one", "guarantee", "guaranteed"]


def banned_words() -> list[str]:
    m = re.search(r"[Bb]anned words:\s*([^\n.]+)", read("rules/writing-rules.md"))
    if not m:
        return []
    return [w.strip(" `*_").lower() for w in m.group(1).split(",") if w.strip()]


def _phrase_regex(phrase: str) -> re.Pattern:
    esc = re.escape(phrase.lower())
    esc = re.sub(r"(?<![a-z])x(?![a-z])", r"\\d+(?:\\.\\d+)?", esc)
    return re.compile(rf"(?<![a-z]){esc}(?![a-z])", re.I)


def lint(text: str) -> dict:
    """Return findings with severity error, warn, or info, plus a summary.

    Errors break hard rules mechanically (em dash, banned words, fair-housing phrases, ROADMAP
    capabilities). Warnings need a human or agent to check against the ledger. The linter never
    approves copy; it narrows what the QA checklist has to look at.
    """
    findings: list[dict] = []
    lines = text.splitlines()

    def add(sev, rule, line_no, msg, fix=""):
        findings.append({"severity": sev, "rule": rule, "line": line_no, "message": msg, "fix": fix})

    for i, line in enumerate(lines, 1):
        if "—" in line:
            add("error", "em-dash", i, "Em dash found.", "Use a comma, a colon, or two sentences.")
    words = banned_words()
    for i, line in enumerate(lines, 1):
        for w in words:
            if re.search(rf"\b{re.escape(w)}\w*", line, re.I):
                add("error", "banned-word", i, f"Banned word: {w}.", "Find the specific claim, or cut.")

    for claim in parse_claims():
        sev = "error" if claim["kind"] == "fair_housing" else "warn"
        for phrase in claim["phrases"]:
            rx = _phrase_regex(phrase)
            for i, line in enumerate(lines, 1):
                if rx.search(line):
                    add(sev, f"do-not-say:{claim['kind']}", i,
                        f'Matches do-not-say phrase "{phrase}".', f"Say instead: {claim['say_instead']}")

    for f in parse_features():
        terms = [f["name"].lower()] + f["aliases"]
        hit_lines = sorted({i for i, line in enumerate(lines, 1) for t in terms
                            if re.search(rf"(?<![a-z0-9]){re.escape(t)}s?(?![a-z0-9])", line, re.I)})
        if not hit_lines:
            continue
        msg = f"{f['id']} {f['name']} is {f['status']}."
        if f["status"] == "ROADMAP":
            add("error", "status:roadmap", hit_lines[0], msg, "Remove. ROADMAP is never mentioned externally.")
        elif f["status"] in ("UNVERIFIED", "IN BUILD"):
            add("warn", "status:unverified", hit_lines[0], msg, "Name it only. Do not describe its output.")
        elif f["status"] == "PARTIAL":
            add("warn", "status:partial", hit_lines[0], msg, "Describe only the visible part.")
        else:
            add("info", "status:shipped", hit_lines[0], msg)

    for i, line in enumerate(lines, 1):
        prose = re.sub(r"\]\([^)]*\)", "]", line)  # ignore link targets such as (#1-quickstart)
        for s in SUPERLATIVES:
            if re.search(rf"(?<![a-z#]){re.escape(s)}(?![a-z0-9])", prose, re.I):
                add("warn", "superlative", i, f'Superlative "{s}".', "Check the scoping section of rules/do-not-say.md.")
        if re.search(r"\$\s?\d[\d,]*(?:\.\d+)?\s*(?:/|per\s+)(?:mo\b|month|year|yr|seat|user)", line, re.I):
            add("warn", "price-pattern", i, "Looks like a price. Plan pricing is undecided (D-11).",
                "If this is a product example (a forecast), label it as one.")

    for para_start, para in _paragraphs(lines):
        if re.search(r"\bany\s+U\.?S\.?\s+address", para, re.I) and "fallback" not in para.lower():
            add("warn", "fallback-clause", para_start, '"Any US address" without the fallback clause.',
                "Add: where nearby evidence is thin, RoomIQ labels the forecast fallback support.")

    order = {"error": 0, "warn": 1, "info": 2}
    findings.sort(key=lambda f: (order[f["severity"]], f["line"]))
    counts = Counter(f["severity"] for f in findings)
    return {"errors": counts.get("error", 0), "warnings": counts.get("warn", 0),
            "info": counts.get("info", 0), "findings": findings,
            "next": "Then tick ops/QA-checklist.md by reading; the linter only covers the mechanical items."}


def _paragraphs(lines: list[str]) -> Iterable[tuple[int, str]]:
    buf, start = [], 1
    for i, line in enumerate(lines, 1):
        if line.strip():
            if not buf:
                start = i
            buf.append(line)
        elif buf:
            yield start, " ".join(buf)
            buf = []
    if buf:
        yield start, " ".join(buf)


# ---------------------------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------------------------

AUTHORITY_BOOST = {"control": 1.6, "router": 1.2, "reference": 1.1, "state": 1.0,
                   "execution": 0.9, "adapter": 0.6, "source": 0.5, "other": 0.8}


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9][a-z0-9\-]+", text.lower())


def search(query: str, limit: int = 8, include_sources: bool = False) -> list[dict]:
    """BM25 over heading-level sections, boosted by layer authority."""
    docs = [s for f in content_files(include_sources) for s in sections(f)]
    if not docs:
        return []
    toks = [_tokens(d["heading"] + " " + d["text"]) for d in docs]
    df = Counter(t for ts in toks for t in set(ts))
    n, avg = len(docs), sum(len(t) for t in toks) / len(docs)
    q = [t for t in _tokens(query) if t]
    results = []
    for d, ts in zip(docs, toks):
        tf = Counter(ts)
        score = 0.0
        for t in q:
            if t not in tf:
                continue
            idf = math.log(1 + (n - df[t] + 0.5) / (df[t] + 0.5))
            score += idf * tf[t] * 2.2 / (tf[t] + 1.2 * (0.25 + 0.75 * len(ts) / avg))
        if score <= 0:
            continue
        if query.lower() in (d["heading"] + " " + d["text"]).lower():
            score *= 1.5
        score *= AUTHORITY_BOOST.get(layer_of(d["path"]), 1.0)
        snippet = re.sub(r"\s+", " ", d["text"])[:280]
        results.append({"path": d["path"], "heading": d["heading"], "layer": layer_of(d["path"]),
                        "score": round(score, 3), "snippet": snippet})
    results.sort(key=lambda r: -r["score"])
    return results[:limit]


# ---------------------------------------------------------------------------------------------
# Innovation accounting rollup
# ---------------------------------------------------------------------------------------------

def metrics(today: date | None = None) -> dict:
    today = today or date.today()
    signals, acts = parse_signals(), parse_activities()
    exps, assumptions, decisions = parse_experiments(), parse_assumptions(), parse_decisions()
    watches = [s for s in signals if s.get("disposition", "").startswith("WATCH")]
    open_watch = []
    for s in watches:
        m = re.match(r"WATCH \((\d+)/(\d+)\)", s["disposition"])
        if m and int(m.group(1)) < int(m.group(2)):
            open_watch.append({"date": s["date"], "type": s["type"], "source": s["source"],
                               "count": s["disposition"]})

    def recent(items, days):
        return [x for x in items if (today - date.fromisoformat(x["date"])).days <= days]

    staleness = {}
    for f in ["rules/feature-status.md", "rules/do-not-say.md", "rules/glossary.md",
              "rules/writing-rules.md", MASTER, "innovation/assumptions.md"]:
        lr = last_reviewed(read(f))
        staleness[f] = (today - date.fromisoformat(lr)).days if lr else None
    snap = latest_snapshot()
    snap_age = (today - date.fromisoformat(Path(snap).name[:10])).days if snap else None
    return {
        "as_of": today.isoformat(),
        "brain": brain_version(),
        "signals": {"total": len(signals), "last_7_days": len(recent(signals, 7)),
                    "last_30_days": len(recent(signals, 30)),
                    "by_type": dict(Counter(s["type"] for s in signals)),
                    "by_disposition": dict(Counter(s.get("disposition", "?").split(" (")[0] for s in signals)),
                    "untriaged": sum(1 for s in signals if s.get("disposition") == "UNTRIAGED"),
                    "open_watch": open_watch},
        "activities": {"total": len(acts), "last_7_days": len(recent(acts, 7)),
                       "last_30_days": len(recent(acts, 30)),
                       "by_type": dict(Counter(a["type"] for a in acts)),
                       "outcome_pending": sum(1 for a in acts if a.get("outcome", "").lower().startswith("pending"))},
        "experiments": {"total": len(exps), "by_status": dict(Counter(e.get("status", "?") for e in exps)),
                        "by_decision": dict(Counter(e.get("decision", "?") for e in exps))},
        "assumptions": {"total": len(assumptions),
                        "by_status": dict(Counter(a["status"] for a in assumptions)),
                        "riskiest_untested": [a["id"] for a in sorted(assumptions, key=lambda a: -(a["riskiness"] or 0))
                                              if a["status"] == "UNTESTED"][:5]},
        "decisions": {"total": len(decisions), "by_status": dict(Counter(d["status"] for d in decisions)),
                      "last_30_days": len(recent([{"date": d["date"] if len(d["date"]) == 10 else d["date"] + "-01"}
                                                  for d in decisions], 30))},
        "features": dict(Counter(f["status"] for f in parse_features())),
        "ledger_age_days": staleness,
        "latest_snapshot": snap, "snapshot_age_days": snap_age,
    }


# ---------------------------------------------------------------------------------------------
# Append-only writers (signal log, activity log)
# ---------------------------------------------------------------------------------------------

def _insert_entry(relpath: str, entry: str) -> None:
    path = ROOT / relpath
    text = path.read_text(encoding="utf-8")
    marker = "## Entries\n"
    i = text.find(marker)
    if i == -1:
        raise ValueError(f"{relpath} has no '## Entries' section")
    j = i + len(marker)
    while text[j:j + 1] == "\n":
        j += 1
    path.write_text(text[:j].rstrip("\n") + "\n\n" + entry.strip() + "\n\n" + text[j:], encoding="utf-8")


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").replace("—", ", ")).strip()


def log_signal(type_: str, source: str, verbatim: str, context: str = "",
               disposition: str = "UNTRIAGED", routed_to: str = "none", when: str | None = None) -> str:
    type_ = type_.upper()
    if type_ not in SIGNAL_TYPES:
        raise ValueError(f"type must be one of {', '.join(SIGNAL_TYPES)}")
    if not DISPOSITION_RE.match(disposition):
        raise ValueError("disposition must be UNTRIAGED, NOISE, PATCH, AMEND, or WATCH (n/N)")
    if not verbatim.strip():
        raise ValueError("verbatim is required; keep the buyer's own words")
    when = when or date.today().isoformat()
    entry = (f"### {when} | {type_} | {_clean(source)}\n"
             f"**Verbatim:** \"{_clean(verbatim)}\"\n"
             f"**Context:** {_clean(context) or 'none given'}\n"
             f"**Disposition:** {disposition}\n"
             f"**Routed to:** {_clean(routed_to)}")
    _insert_entry("ops/signal-log.md", entry)
    return entry


def next_activity_id() -> str:
    nums = [int(a["id"].split("-")[1]) for a in parse_activities() if a.get("id", "").startswith("ACT-")]
    return f"ACT-{(max(nums) + 1) if nums else 1:04d}"


def log_activity(type_: str, title: str, what: str, audience: str = "internal",
                 linked: str = "none", expected: str = "", when: str | None = None) -> str:
    type_ = type_.upper()
    if type_ not in ACTIVITY_TYPES:
        raise ValueError(f"type must be one of {', '.join(ACTIVITY_TYPES)}")
    if not expected.strip():
        raise ValueError("expected is required: write what this should move before the outcome exists")
    when = when or date.today().isoformat()
    entry = (f"### {when} | {type_} | {_clean(title)}\n"
             f"**ID:** {next_activity_id()}\n"
             f"**What:** {_clean(what)}\n"
             f"**Audience:** {_clean(audience)}\n"
             f"**Linked:** {_clean(linked)}\n"
             f"**Expected:** {_clean(expected)}\n"
             f"**Outcome:** pending\n"
             f"**Signals logged:** none")
    _insert_entry("ops/activity-log.md", entry)
    return entry


def next_experiment_id() -> str:
    nums = [int(e["id"].split("-")[1]) for e in parse_experiments()]
    return f"EXP-{(max(nums) + 1) if nums else 1:03d}"


def new_experiment(title: str, tests: str, audience: str, method: str, metric: str,
                   threshold: str, sample: str, end: str) -> str:
    ids = {a["id"] for a in parse_assumptions()}
    for t in re.findall(r"[ARG]\d+", tests):
        if t not in ids:
            raise ValueError(f"assumption {t} is not in innovation/assumptions.md")
    if not threshold.strip():
        raise ValueError("threshold is required before the experiment starts")
    entry = (f"\n### {next_experiment_id()} | {_clean(title)}\n"
             f"- **Status:** PLANNED\n- **Tests:** {_clean(tests)}\n- **Audience:** {_clean(audience)}\n"
             f"- **Method:** {_clean(method)}\n- **Metric:** {_clean(metric)}\n"
             f"- **Threshold (set before results):** {_clean(threshold)}\n- **Sample:** {_clean(sample)}\n"
             f"- **End:** {_clean(end)}\n- **Result:** none yet\n- **Decision:** PENDING\n")
    path = ROOT / "innovation/experiments.md"
    path.write_text(path.read_text(encoding="utf-8").rstrip("\n") + "\n" + entry, encoding="utf-8")
    return entry.strip()


# ---------------------------------------------------------------------------------------------
# Minimal JSON Schema check (required + enum + type), enough for schemas/*.json
# ---------------------------------------------------------------------------------------------

def validate(obj: dict, schema_name: str) -> list[str]:
    schema = json.loads((SCHEMAS / f"{schema_name}.schema.json").read_text(encoding="utf-8"))
    errors = []
    for key in schema.get("required", []):
        if key not in obj or obj[key] in (None, ""):
            errors.append(f"{schema_name}: missing required field '{key}'")
    for key, spec in schema.get("properties", {}).items():
        if key not in obj or obj[key] in (None, ""):
            continue
        val = obj[key]
        if "enum" in spec and val not in spec["enum"]:
            errors.append(f"{schema_name}: '{key}' = {val!r} not in {spec['enum']}")
        if "pattern" in spec and isinstance(val, str) and not re.search(spec["pattern"], val):
            errors.append(f"{schema_name}: '{key}' = {val!r} does not match {spec['pattern']}")
        if spec.get("type") == "integer" and not isinstance(val, int):
            errors.append(f"{schema_name}: '{key}' must be an integer")
    return errors


# ---------------------------------------------------------------------------------------------
# Exports for other AI tools (dist/)
# ---------------------------------------------------------------------------------------------

BUNDLE_ORDER = [
    "CLAUDE.md",
    MASTER,
    "reference/value-proposition-investors.md",
    "reference/value-proposition-operators.md",
    "reference/objection-handling.md",
    "reference/metrics-methodology.md",
    "ops/copy-bank.md",
    # Guardrails last: models weight the end of a long prompt more heavily.
    "rules/glossary.md",
    "rules/feature-status.md",
    "rules/writing-rules.md",
    "rules/do-not-say.md",
    "ops/QA-checklist.md",
]


def build_bundle() -> str:
    v = brain_version()
    parts = [f"# RoomIQ GTM Brain, single-file bundle (v{v['version']}, {v['last_updated']})\n",
             "Generated by `tools/brain.py build` from the RoomIQGTMBrain repository. Do not edit. "
             "Paste into a chat model's project instructions or knowledge, or send as a system prompt. "
             "Each section below is a separate file in the repository; where text says to open a file, "
             "find that path as a section heading here. Guardrails are placed last on purpose.\n"]
    for f in BUNDLE_ORDER:
        parts.append(f"\n---\n\n## File: {f}\n\n{read(f).strip()}\n")
    parts.append("\n---\n\nBefore returning anything: check the draft against the status ledger, the "
                 "closed proof set, and the do-not-say table above. If a fact is missing, write "
                 "[NEEDS BRAIN] instead of inventing it. Name the rule the draft came closest to breaking.\n")
    return "".join(parts)


def build_llms_full() -> str:
    v = brain_version()
    order, seen = [], set()
    for _, p, _ in llms_index():
        if p.endswith((".md", ".txt")) and (ROOT / p).is_file() and p not in seen and not p.startswith("dist/"):
            order.append(p)
            seen.add(p)
    for p in content_files():
        if p not in seen:
            order.append(p)
            seen.add(p)
    out = [f"# RoomIQ GTM Brain, full text (v{v['version']}, {v['last_updated']})\n\n"
           "> Every brain file concatenated in llms.txt order. Generated by tools/brain.py build.\n"]
    for p in order:
        out.append(f"\n\n<<<FILE {p}>>>\n\n{read(p).strip()}\n\n<<<END {p}>>>\n")
    return "".join(out)


def build_manifest() -> dict:
    purposes = {p: purpose for _, p, purpose in llms_index()}
    files = []
    for p in content_files(include_sources=True):
        text = read(p)
        files.append({"path": p, "layer": layer_of(p), "always_load": p in CONTROL_LAYER,
                      "purpose": purposes.get(p, ""), "lines": len(text.splitlines()),
                      "bytes": len(text.encode("utf-8")), "tokens_est": len(text) // 4,
                      "last_reviewed": last_reviewed(text), "sha256_12": sha(text)})
    return {"name": "roomiq-gtm-brain", **brain_version(), "control_layer": CONTROL_LAYER,
            "load_policy": LOAD_POLICY, "files": files}


def build_chunks() -> list[dict]:
    v = brain_version()
    out = []
    for p in content_files():
        if p in ("README.md", "llms.txt"):
            continue
        lr = last_reviewed(read(p))
        for i, s in enumerate(sections(p)):
            out.append({"id": f"{p}#{i:02d}-{slug(s['heading'])}", "path": p, "layer": layer_of(p),
                        "always_load": p in CONTROL_LAYER, "title": s["title"], "heading": s["heading"],
                        "last_reviewed": lr, "brain_version": v["version"],
                        "tokens_est": len(s["text"]) // 4, "text": s["text"]})
    return out


def build_ledgers() -> dict:
    return {"brain": brain_version(), "features": parse_features(), "claims": parse_claims(),
            "glossary": parse_glossary(), "decisions": [{k: v for k, v in d.items() if k != "body"}
                                                       for d in parse_decisions()],
            "assumptions": parse_assumptions(), "experiments": parse_experiments(),
            "signals": parse_signals(), "activities": parse_activities()}


def dist_outputs() -> dict[str, str]:
    return {
        "dist/roomiq-gtm-brain.bundle.md": build_bundle(),
        "dist/llms-full.txt": build_llms_full(),
        "dist/brain.manifest.json": json.dumps(build_manifest(), indent=2, ensure_ascii=False) + "\n",
        "dist/brain.chunks.jsonl": "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in build_chunks()),
        "dist/ledgers.json": json.dumps(build_ledgers(), indent=2, ensure_ascii=False) + "\n",
    }


# ---------------------------------------------------------------------------------------------
# Adapters: one pointer body, many doors. Rendered, never hand-edited.
# ---------------------------------------------------------------------------------------------

BLOCK_BEGIN, BLOCK_END = "<!-- roomiq-gtm-brain:begin -->", "<!-- roomiq-gtm-brain:end -->"


def _pointer_body(prefix: str, where: str) -> str:
    tmpl = (TEMPLATES_DIR / "pointer-body.md.tmpl").read_text(encoding="utf-8")
    return tmpl.replace("{{P}}", prefix).replace("{{WHERE}}", where).strip() + "\n"


def _fm(lines: list[str]) -> str:
    return "---\n" + "\n".join(lines) + "\n---\n\n"


def render_adapters(prefix: str = "", consuming: bool = False) -> dict[str, tuple[str, str]]:
    """Map relative output path -> (mode, content).

    Modes: 'file' overwrites a file this brain owns (namespaced roomiq-gtm), 'block' merges a
    marked block into a shared file, 'json' deep-merges a server entry into an MCP config, and
    'once' writes only when the file is absent (shared config we must not clobber).
    """
    where = f"`{prefix.rstrip('/')}/`" if prefix else "this repository"
    body = _pointer_body(prefix, where)
    desc = ("RoomIQ go-to-market brain. Load before any customer-facing copy, positioning, "
            "messaging, release notes, UI strings, or competitive work.")
    always = "false" if consuming else "true"
    script = f"{prefix}tools/mcp_server.py"
    mcp_std = json.dumps({"mcpServers": {"roomiq-gtm-brain": {"command": "python3", "args": [script]}}},
                         indent=2) + "\n"
    ws = "${workspaceFolder}/"
    mcp_ws = json.dumps({"mcpServers": {"roomiq-gtm-brain": {"command": "python3",
                                                             "args": [ws + script]}}}, indent=2) + "\n"
    mcp_vscode = json.dumps({"servers": {"roomiq-gtm-brain": {"type": "stdio", "command": "python3",
                                                              "args": [ws + script]}}}, indent=2) + "\n"
    aider = ("# RoomIQ GTM brain: files Aider reads into every chat. Generated by tools/brain.py adapters.\n"
             "read:\n" + "".join(f"  - {prefix}{f}\n" for f in CONTROL_LAYER[:5]))
    out = {
        ".cursor/rules/roomiq-gtm.mdc": ("file", _fm([f"description: {desc}", "globs:",
                                                      f"alwaysApply: {always}"]) + body),
        ".windsurf/rules/roomiq-gtm.md": ("file", _fm(["trigger: " + ("model_decision" if consuming else "always_on"),
                                                       f"description: {desc}"]) + body),
        ".github/copilot-instructions.md": ("block", body),
        "GEMINI.md": ("block", body),
        ".clinerules/roomiq-gtm.md": ("file", body),
        ".roo/rules/roomiq-gtm.md": ("file", body),
        ".continue/rules/roomiq-gtm.md": ("file", _fm(["name: RoomIQ GTM brain", f"description: {desc}",
                                                       f"alwaysApply: {always}"]) + body),
        ".kiro/steering/roomiq-gtm.md": ("file", _fm(["inclusion: always"]) + body),
        ".junie/guidelines.md": ("block", body),
        ".amazonq/rules/roomiq-gtm.md": ("file", body),
        ".aider.conf.yml": ("once", aider),
        ".mcp.json": ("json", mcp_std),
        ".cursor/mcp.json": ("json", mcp_ws),
        ".vscode/mcp.json": ("json", mcp_vscode),
        ".gemini/settings.json": ("json", mcp_std),
    }
    if consuming:
        out["AGENTS.md"] = ("block", body)
        out["CLAUDE.md"] = ("block", body)
    return out


def merge_block(existing: str, body: str) -> str:
    """Replace the content between our markers, or append the block if the markers are absent."""
    block = f"{BLOCK_BEGIN}\n{body.strip()}\n{BLOCK_END}\n"
    if BLOCK_BEGIN in existing and BLOCK_END in existing:
        pre = existing.split(BLOCK_BEGIN, 1)[0]
        post = existing.split(BLOCK_END, 1)[1]
        return pre + block.rstrip("\n") + post if post.strip() else pre + block
    if not existing.strip():
        return block
    return existing.rstrip("\n") + "\n\n" + block


def merge_json(existing: str, ours: str) -> str:
    """Deep-merge our server entry into an existing MCP config without touching other servers."""
    try:
        base = json.loads(existing) if existing.strip() else {}
    except json.JSONDecodeError:
        raise ValueError("existing MCP config is not valid JSON; merge it by hand")
    for key, servers in json.loads(ours).items():
        base.setdefault(key, {}).update(servers)
    return json.dumps(base, indent=2) + "\n"


def adapter_plan(target: Path, prefix: str, consuming: bool) -> dict[Path, str]:
    """Final file contents for every adapter at target, merging marked blocks."""
    plan = {}
    for relpath, (mode, content) in render_adapters(prefix, consuming).items():
        dest = target / relpath
        existing = dest.read_text(encoding="utf-8") if dest.exists() else ""
        if mode == "block":
            plan[dest] = merge_block(existing, content)
        elif mode == "json":
            plan[dest] = merge_json(existing, content)
        elif mode == "once" and existing:
            plan[dest] = existing
        else:
            plan[dest] = content
    return plan
