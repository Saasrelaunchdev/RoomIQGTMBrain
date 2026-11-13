"""Tests for the brain tooling. Run: python3 -m unittest discover -s tools/tests -v"""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import brain_lib as B  # noqa: E402


class Ledgers(unittest.TestCase):
    def test_feature_ledger_parses_32_capabilities(self):
        feats = B.parse_features()
        self.assertEqual(len([f for f in feats if f["id"].startswith("C")]), 32)
        self.assertTrue(all(f["status"] in B.STATUSES for f in feats))
        c27 = next(f for f in feats if f["id"] == "C27")
        self.assertEqual(c27["status"], "SHIPPED")

    def test_claim_ledger_has_replacements(self):
        claims = B.parse_claims()
        self.assertGreater(len(claims), 10)
        for c in claims:
            self.assertTrue(c["say_instead"], c["do_not_say"])
        self.assertTrue(any(c["kind"] == "fair_housing" for c in claims))

    def test_decisions_and_innovation_files_parse(self):
        self.assertGreaterEqual(len(B.parse_decisions()), 10)
        self.assertGreaterEqual(len(B.parse_assumptions()), 10)
        self.assertGreaterEqual(len(B.parse_experiments()), 5)
        self.assertGreaterEqual(len(B.parse_signals()), 5)
        self.assertGreaterEqual(len(B.parse_activities()), 3)

    def test_glossary_has_brand_row(self):
        terms = [r["term"] for r in B.parse_glossary()]
        self.assertIn("RoomIQ", terms)


class Lint(unittest.TestCase):
    def rules(self, text):
        return {f["rule"] for f in B.lint(text)["findings"]}

    def test_em_dash_and_banned_word_are_errors(self):
        res = B.lint("RoomIQ will unlock deals — fast.")
        self.assertEqual(res["errors"], 2)

    def test_accuracy_claim_is_flagged(self):
        self.assertIn("do-not-say:hard_ban", self.rules("Our accurate forecast predicts revenue within 5%."))

    def test_fair_housing_is_an_error(self):
        res = B.lint('House rules: "women only" in this home.')
        self.assertTrue(any(f["rule"] == "do-not-say:fair_housing" and f["severity"] == "error" for f in res["findings"]))

    def test_unverified_capability_is_warned(self):
        self.assertIn("status:unverified", self.rules("Get an amenity ROI shortlist for your house."))

    def test_roadmap_capability_is_an_error(self):
        self.assertIn("status:roadmap", self.rules("Set market-move alerts for your saved deals."))

    def test_fallback_clause(self):
        self.assertIn("fallback-clause", self.rules("Underwrite any US address in minutes."))
        self.assertNotIn("fallback-clause", self.rules(
            "Underwrite any US address. Where evidence is thin, RoomIQ labels fallback support."))

    def test_clean_copy_has_no_errors(self):
        res = B.lint("Every forecast shows its formula, its comps, and a confidence label.")
        self.assertEqual(res["errors"], 0)


class Search(unittest.TestCase):
    def test_rules_rank_for_claim_questions(self):
        top = B.search("accuracy forecast claim", 5)
        self.assertTrue(top)
        # The rule lives in the control layer and is restated in every router; either may lead.
        self.assertTrue(any(r["layer"] in ("control", "router") for r in top[:3]))
        fair = B.search("fair housing protected class house rules", 3)
        self.assertIn("rules/do-not-say.md", [r["path"] for r in fair])


class Writers(unittest.TestCase):
    """Run the append-only writers against a throwaway copy of the brain."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        for d in ("ops", "innovation", "schemas"):
            shutil.copytree(B.ROOT / d, self.tmp / d)
        self._root = B.ROOT
        B.ROOT = self.tmp
        B.SCHEMAS = self.tmp / "schemas"

    def tearDown(self):
        B.ROOT = self._root
        B.SCHEMAS = self._root / "schemas"
        shutil.rmtree(self.tmp)

    def test_log_signal_inserts_newest_first(self):
        B.log_signal("OBJECTION", "demo call", "Where does the data come from?", "Investor, Dallas", when="2030-01-01")
        first = B.parse_signals()[0]
        self.assertEqual(first["date"], "2030-01-01")
        self.assertEqual(first["disposition"], "UNTRIAGED")
        self.assertEqual(B.validate(first, "signal"), [])

    def test_log_activity_requires_expected(self):
        with self.assertRaises(ValueError):
            B.log_activity("DEMO", "t", "w", expected="")
        B.log_activity("DEMO", "Demo with investor", "Ran a Dallas address", "A", "EXP-001", "asks for access")
        self.assertEqual(B.parse_activities()[0]["type"], "DEMO")

    def test_experiment_needs_known_assumption(self):
        with self.assertRaises(ValueError):
            B.new_experiment("x", "A99", "A", "m", "metric", "t", "s", "e")


class Adapters(unittest.TestCase):
    def test_block_merge_is_idempotent_and_preserves_content(self):
        existing = "# App rules\n\nUse tabs.\n"
        once = B.merge_block(existing, "body one")
        twice = B.merge_block(once, "body two")
        self.assertIn("Use tabs.", twice)
        self.assertEqual(twice.count(B.BLOCK_BEGIN), 1)
        self.assertIn("body two", twice)
        self.assertNotIn("body one", twice)

    def test_json_merge_keeps_other_servers(self):
        merged = json.loads(B.merge_json('{"mcpServers": {"other": {"command": "x"}}}',
                                         '{"mcpServers": {"roomiq-gtm-brain": {"command": "python3"}}}'))
        self.assertEqual(set(merged["mcpServers"]), {"other", "roomiq-gtm-brain"})

    def test_rendered_adapters_have_no_placeholders(self):
        for _path, (_mode, content) in B.render_adapters("gtm-brain/", True).items():
            self.assertNotIn("{{", content)


class MCP(unittest.TestCase):
    def call(self, *msgs):
        proc = subprocess.run([sys.executable, str(TOOLS / "mcp_server.py")],
                              input="\n".join(json.dumps(m) for m in msgs) + "\n",
                              capture_output=True, text=True, timeout=60)
        return [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]

    def test_handshake_tools_and_call(self):
        out = self.call(
            {"jsonrpc": "2.0", "id": 1, "method": "initialize",
             "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "t", "version": "0"}}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
             "params": {"name": "brain_feature_status", "arguments": {"query": "C27"}}},
            {"jsonrpc": "2.0", "id": 4, "method": "tools/call",
             "params": {"name": "brain_log_signal", "arguments": {"type": "RISK", "source": "t", "verbatim": "v"}}},
            {"jsonrpc": "2.0", "id": 5, "method": "prompts/list"},
            {"jsonrpc": "2.0", "id": 6, "method": "resources/read", "params": {"uri": "brain:///rules/glossary.md"}},
            {"jsonrpc": "2.0", "id": 7, "method": "nope"},
        )
        self.assertEqual(len(out), 7)  # the notification gets no response
        self.assertEqual(out[0]["result"]["protocolVersion"], "2025-06-18")
        names = {t["name"] for t in out[1]["result"]["tools"]}
        self.assertIn("brain_load_control_layer", names)
        self.assertIn('"C27"', out[2]["result"]["content"][0]["text"])
        self.assertTrue(out[3]["result"]["isError"])  # writes disabled by default
        self.assertGreater(len(out[4]["result"]["prompts"]), 5)
        self.assertIn("RoomIQ", out[5]["result"]["contents"][0]["text"])
        self.assertEqual(out[6]["error"]["code"], -32601)

    def test_path_traversal_is_refused(self):
        out = self.call({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                         "params": {"name": "brain_read", "arguments": {"path": "../../etc/passwd"}}})
        self.assertTrue(out[0]["result"]["isError"])


if __name__ == "__main__":
    unittest.main()
