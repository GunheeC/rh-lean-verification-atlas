#!/usr/bin/env python3
"""Exercise the boundaries that distinguish source citations from cone size."""
from copy import deepcopy
from pathlib import Path
import json
from tempfile import TemporaryDirectory
import unittest

from reading_coverage import KINDS, citations, cited_totals
from snapshot import ROOT, TOTAL, headline_guard, read_history, validate_counts
from source_inventory import load_inventory
from index_position import nearest_positions
from snapshot import snapshot_digest


class ReadingCoverageTests(unittest.TestCase):
    def test_unions_use_file_identity_and_each_denominators_population(self):
        inventory = {"files": {"a.lean": {"lines": 15}}, "outside_files": {"b.lean": {"lines": 20}},
                     "core_ranges": {"a.lean": [[2, 8], [10, 10]], "b.lean": [[5, 7]]},
                     "core_overlaps": {"a.lean": [[5, 6, 2]]}}
        pools = {k: set() for k in KINDS}
        first = {("a.lean", 1, 6), ("a.lean", 6, 9)}
        second = {("a.lean", 7, 11), ("b.lean", 5, 7)}
        rows = [{"citations": dict(pools, written=first, full=first)},
                {"citations": dict(pools, written=second, outlined=second)}]
        sums = cited_totals(rows, inventory)
        self.assertEqual(sums["written"], {"all_files": 14, "in_raw_files": 11, "in_weighted_core": 11, "weighted_core_weight": 15})
        self.assertLess(sums["written"]["all_files"], sums["full"]["all_files"] + sums["outlined"]["all_files"])
        for pin in [("not-pinned.lean", 1, 1), ("a.lean", 1, 16), ("a.lean", 0, 1)]:
            with self.subTest(pin=pin), self.assertRaises(ValueError):
                cited_totals([{"citations": dict(pools, written={pin})}], inventory)

    def test_scope_current_edition_withdrawal_and_dispute(self):
        unit = {"id": "A", "status": "Full"}
        active = {"id": "S1", "status": "active", "source": "a.md", "sha256": "one", "uses": [],
                  "lean": [{"file": "a.lean", "line0": 1, "line1": 3}],
                  "ai_review": [{"step_sha256": "one", "edition_sha256": "new"}]}
        manifest = {"edition_sha256": "new", "steps": [active, {"id": "S2", "status": "withdrawn"}]}
        human = {"steps": {"S1": {"state": "disputed"}}}
        counted = citations(unit, manifest, human, set())
        self.assertEqual(counted["written"], counted["ai_reviewed"])
        self.assertFalse(counted["human_checked"] or counted["ai_reviewed_prose"])
        active["ai_review"] = []
        human["steps"]["S1"]["state"] = "human-checked"
        counted = citations(unit, manifest, human, {"a.md"})
        self.assertEqual(counted["written"], counted["human_checked"])
        self.assertEqual(counted["written"], counted["ai_reviewed_prose"])
        self.assertFalse(counted["ai_reviewed"])
        for record in [{"step_sha256": "two", "edition_sha256": "new"}, {"step_sha256": "one", "edition_sha256": "old"}]:
            active["ai_review"] = [record]
            with self.subTest(record=record), self.assertRaises(ValueError):
                citations(unit, manifest, human, set())

    def test_nearest_statements_give_a_partition_and_deterministic_shared_ownership(self):
        graph = {"allChi": {"parent": None,"weight": 40}, "context": {"parent": "allChi","weight": 25},
                 "child": {"parent": "context","weight": 12}, "nested": {"parent": "child","weight": 3}}
        units = {"Z": {"heads": ["child"], "status": "Full", "grade": "L2"},
                 "B": {"heads": ["nested"], "status": "Full", "grade": "L2"},
                 "A": {"heads": ["child"], "status": "Outlined", "grade": "L0"},
                 "R": {"heads": ["allChi"], "status": "Statement only", "grade": "L0"}}
        actual = nearest_positions(units,graph)
        self.assertEqual(actual["status"], {"Full": 3, "Outlined": 9, "Statement only": 28})
        self.assertEqual(actual["full_l2"], 3)
        self.assertEqual(actual["shared_heads"], 1)
        self.assertEqual(actual, nearest_positions(dict(reversed(list(units.items()))), graph))

    def test_history_content_digest_is_sensitive_to_prior_counts(self):
        row = deepcopy(read_history(ROOT)[0])
        self.assertEqual(snapshot_digest(row), row["snapshot_sha256"])
        row["counts"]["all"]["full"] += 1
        self.assertNotEqual(snapshot_digest(row), row["snapshot_sha256"])
    def test_synthetic_p009_checks_only_cover_that_notes_physical_citations(self):
        unit = json.loads((ROOT/"units/P009.yaml").read_bytes())
        manifest = json.loads((ROOT/"units/P009.steps.yaml").read_bytes())
        states = {"steps": {s["id"]: {"state": "human-checked"} for s in manifest["steps"] if s["status"] == "active"}}
        counted = cited_totals([{"citations": citations(unit, manifest, states, set())}], load_inventory(ROOT))
        self.assertEqual(counted["written"], counted["human_checked"])
        expected = {(pin["file"], line)
                    for step in manifest["steps"] if step["status"] == "active"
                    for pin in step["lean"] for line in range(pin["line0"], pin["line1"]+1)}
        self.assertGreater(len(expected), 0)
        self.assertEqual(counted["human_checked"]["all_files"], len(expected))
        self.assertLess(len(expected), unit["lean"][0]["dominated"])

    def test_retired_headlines_rejected_in_archive_and_live_pages(self):
        inventory = load_inventory(ROOT)
        original = read_history(ROOT)
        counts = deepcopy(original[-1]["counts"])
        counts["tracks"]["formal"]["lines"] = {"3": TOTAL}
        with self.assertRaises(ValueError):
            validate_counts(counts, inventory)
        counts = deepcopy(original[-1]["counts"])
        counts["all"]["cited_lines"]["written"]["all_files"] = TOTAL
        with self.assertRaises(ValueError):
            validate_counts(counts, inventory)
        counts = deepcopy(original[0]["counts"])
        counts["all"]["cited_lines"]["written"]["all_files"] = 1
        with self.assertRaises(ValueError):
            validate_counts(counts, inventory)
        with TemporaryDirectory() as temp:
            root = Path(temp)
            path = root/"site/STATUS.html"
            path.parent.mkdir(parents=True)
            path.write_text("<p>Written: <b>9,567,045</b> (100.00%)</p>")
            with self.assertRaises(ValueError):
                headline_guard(root)
            path.write_text("Written · stage 3: 9,567,045.")
            with self.assertRaises(ValueError):
                headline_guard(root)
            path.write_text("Core denominator 9,567,045. Cited: 12,505 (0.1307%).")
            headline_guard(root)


if __name__ == "__main__":
    unittest.main()
