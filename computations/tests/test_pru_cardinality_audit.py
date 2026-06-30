#!/usr/bin/env python3
"""
Tests for _pru_cardinality_audit.py (S84-W9A-97).

Covers:
  - Self-audit: D_PRU_raw(self) = 0 under the 6 pinned PRDR parameters.
  - Positive test: fully pinned synthetic gate emits D_PRU_raw = 0.
  - Negative test: gate with missing pin emits D_PRU_raw = 1.
  - Coupling-rank: tool returns rank(A) of an adjacency matrix with N vertices.
  - Plan-parser: markdown table + bullet PRDR forms both recognized.
  - Script-parser: `# (local)` tagged assignments are excluded from F_script.
  - Substitution-chain arithmetic: F minus P = empty iff D_PRU_raw = 0.

Run:
  "phonon-exflation-sim/.venv312/Scripts/python.exe" -m unittest \
      computations/_shared/tests/test_pru_cardinality_audit.py
"""

from __future__ import annotations

import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(COMPUTATIONS_DIR))

import _pru_cardinality_audit as pru  # noqa: E402


# ---------------------------------------------------------------------------
# Fixture gates (markdown text, as-in plan)
# ---------------------------------------------------------------------------
GATE_FULLY_PINNED = """## §TEST-1 — Fully pinned gate

### Gate ID
`TEST-1`

### Method
Script: `computations/_shared/_fixture_fully_pinned.py`

### PRDR
- `ALPHA` (float) — **PIN**: 0.5
- `BETA` (int) — **PIN**: 7
- `GAMMA` (str) — **PIN**: "hello"
"""

GATE_MISSING_PIN = """## §TEST-2 — Missing pin gate

### Gate ID
`TEST-2`

### Method
Script: `computations/_shared/_fixture_missing_pin.py`

### PRDR
- `ALPHA` (float) — **PIN**: 0.5
"""

GATE_TABLE_FORM = """## §TEST-3 — Table form gate

### Gate ID
`TEST-3`

### Method
Script: `computations/_shared/_fixture_table.py`

### 7. Machinery pin (PRDR)

| Parameter | Pinned value | Rationale |
|:----------|:-------------|:----------|
| ALPHA | 0.5 | reason |
| BETA  | 7   | reason |
| GAMMA | "hi" | reason |
"""

SCRIPT_FULLY_PINNED = """# fully pinned fixture
ALPHA = 0.5
BETA = 7
GAMMA = "hello"
_tmp = ALPHA + BETA  # (local)
"""

SCRIPT_MISSING_PIN = """# missing pin fixture
ALPHA = 0.5
BETA = 7  # NOT pinned in plan -> must surface as unpinned
"""

SCRIPT_TABLE = """# table-form fixture
ALPHA = 0.5
BETA = 7
GAMMA = "hi"
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _mk_plan(tmp: Path, body: str) -> Path:
    p = tmp / "fake_plan.md"
    p.write_text(body, encoding="utf-8")
    return p


def _mk_script(tmp: Path, name: str, body: str) -> Path:
    p = tmp / name
    p.write_text(body, encoding="utf-8")
    return p


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
class TestSubstitutionChain(unittest.TestCase):
    """Directly verify Definition-3 arithmetic:  D_PRU_raw = 1 iff F \\ P != {}."""

    def test_D_PRU_raw_definition(self):
        F = {"a", "b", "c"}
        P1 = {"a", "b", "c"}
        P2 = {"a", "b"}
        self.assertEqual(0 if not (F - P1) else 1, 0)
        self.assertEqual(0 if not (F - P2) else 1, 1)

    def test_plan_closed_iff_sum_zero(self):
        # sum_g D_PRU_raw = 0  <=>  for all g, F_g subset P_g
        drs = [0, 0, 0, 0]
        self.assertEqual(sum(drs), 0)
        drs = [0, 1, 0, 0]
        self.assertEqual(sum(drs), 1)


class TestExtractPinKeys(unittest.TestCase):
    def test_bullet_form(self):
        pins = pru.extract_pin_keys(GATE_FULLY_PINNED)
        self.assertIn("ALPHA", pins)
        self.assertIn("BETA", pins)
        self.assertIn("GAMMA", pins)

    def test_table_form(self):
        pins = pru.extract_pin_keys(GATE_TABLE_FORM)
        self.assertIn("ALPHA", pins)
        self.assertIn("BETA", pins)
        self.assertIn("GAMMA", pins)

    def test_missing_pin_extraction(self):
        pins = pru.extract_pin_keys(GATE_MISSING_PIN)
        self.assertIn("ALPHA", pins)
        self.assertNotIn("BETA", pins)


class TestAuditScript(unittest.TestCase):
    def test_local_tagged_excluded(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            script = _mk_script(tmp, "s.py", SCRIPT_FULLY_PINNED)
            # Temporarily rebase the project root so the walker can resolve
            # the relative path.
            saved_root = pru.PROJECT_ROOT
            pru.PROJECT_ROOT = tmp
            try:
                sa = pru.audit_script(script)
            finally:
                pru.PROJECT_ROOT = saved_root
            # _tmp tagged (local) must be excluded; the other three stay.
            self.assertIn("ALPHA", sa.module_assigns)
            self.assertIn("BETA", sa.module_assigns)
            self.assertIn("GAMMA", sa.module_assigns)
            self.assertNotIn("_tmp", sa.module_assigns)

    def test_missing_pin_surfaces_param(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            script = _mk_script(tmp, "s.py", SCRIPT_MISSING_PIN)
            saved_root = pru.PROJECT_ROOT
            pru.PROJECT_ROOT = tmp
            try:
                sa = pru.audit_script(script)
            finally:
                pru.PROJECT_ROOT = saved_root
            self.assertIn("BETA", sa.module_assigns)

    def test_syntax_error_resilience(self):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            script = _mk_script(tmp, "s.py", "def broken(:\n")
            saved_root = pru.PROJECT_ROOT
            pru.PROJECT_ROOT = tmp
            try:
                sa = pru.audit_script(script)
            finally:
                pru.PROJECT_ROOT = saved_root
            self.assertEqual(sa.module_assigns, set())


class TestPerGateAudit(unittest.TestCase):
    def _run(self, plan_text: str, script_name: str, script_body: str):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            (tmp / "computations").mkdir()
            _mk_script(tmp / "computations", script_name, script_body)
            plan = tmp / "plan.md"
            plan.write_text(plan_text, encoding="utf-8")

            saved_root = pru.PROJECT_ROOT
            pru.PROJECT_ROOT = tmp
            try:
                gates = pru.parse_plan_file(plan)
                results = [pru.audit_gate(g) for g in gates]
            finally:
                pru.PROJECT_ROOT = saved_root
            return gates, results

    def test_fully_pinned_passes(self):
        gates, results = self._run(
            GATE_FULLY_PINNED,
            "_fixture_fully_pinned.py",
            SCRIPT_FULLY_PINNED,
        )
        self.assertEqual(len(results), 1)
        r = results[0]
        self.assertEqual(r.D_PRU_raw, 0)
        self.assertIn(r.verdict, ("PASS", "INFO"))

    def test_missing_pin_fails(self):
        gates, results = self._run(
            GATE_MISSING_PIN,
            "_fixture_missing_pin.py",
            SCRIPT_MISSING_PIN,
        )
        self.assertEqual(len(results), 1)
        r = results[0]
        self.assertEqual(r.D_PRU_raw, 1)
        self.assertEqual(r.verdict, "FAIL")
        self.assertIn("BETA", r.unpinned_params)

    def test_table_form_passes(self):
        gates, results = self._run(
            GATE_TABLE_FORM,
            "_fixture_table.py",
            SCRIPT_TABLE,
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].D_PRU_raw, 0)


class TestCouplingRank(unittest.TestCase):
    def test_singleton_is_zero(self):
        self.assertEqual(pru.coupling_rank({"a"}, []), 0)

    def test_two_connected_is_two(self):
        # rank of [[0,1],[1,0]] = 2
        self.assertEqual(pru.coupling_rank({"a", "b"}, [("a", "b")]), 2)

    def test_disconnected_pair_is_zero(self):
        self.assertEqual(pru.coupling_rank({"a", "b"}, []), 0)


class TestSelfAudit(unittest.TestCase):
    """The tool's own plan entry (§W9a-97) must yield D_PRU_raw(self) = 0."""

    def test_self_audit_zero(self):
        result = pru.self_audit()
        self.assertEqual(result.D_PRU_raw, 0,
                         f"Self-audit failed: unpinned = {result.unpinned_params}")


if __name__ == "__main__":
    unittest.main()
