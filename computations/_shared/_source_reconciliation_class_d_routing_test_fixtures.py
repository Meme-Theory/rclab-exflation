#!/usr/bin/env python
"""
_source_reconciliation_class_d_routing_test_fixtures.py — S89 W6-8 fixtures
============================================================================

Three synthetic test fixtures + 1 live-input cross-check for the
`class_d_inheritance_routing` extension function in
`_source_reconciliation_audit.py`.

Fixtures (per plan §W6-8 §6):

  Fixture 1 — `class_d_w4_2_inheritance_detect`:
    pin_provenance contains "s86_w4_p5_sector_2_k_invariant"
    → expected: inheritance_class='Class-(d)',
                calibration_corpus_match='W4-2',
                severity_band='MANDATORY'.

  Fixture 2 — `class_d_w9b_2_inheritance_detect`:
    pin_provenance contains "s87_w9b_pole_specificity_scan"
    → expected: inheritance_class='Class-(d)',
                calibration_corpus_match='W9b-2',
                severity_band='MANDATORY'.

  Fixture 3 — `not_in_class_d_corpus_route`:
    pin_provenance contains "s85_w0_zubarev_lmax_convergence_to_minus_one"
    → expected: inheritance_class='NOT-IN-CLASS-D-CORPUS',
                calibration_corpus_match=None,
                route via standard 6-class taxonomy.

Live cross-check:
    Use the W6-7 (A.41) output as a live test case: pin_provenance
    "computations/session-89/s89_w6_d_max_measurement_w9b_2_vs_pv_pipeline.npz
    consumes W9b-2 SCHEMATIC output" → expected: Class-(d), W9b-2 match.

CLI
---
    python _source_reconciliation_class_d_routing_test_fixtures.py
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: E402,F401,F403  (per CLAUDE.md mandatory)
from _source_reconciliation_audit import class_d_inheritance_routing  # noqa: E402


# ---------------------------------------------------------------------------
# Fixture 1 — W4-2 inheritance detection
# ---------------------------------------------------------------------------
FIXTURE_1_PROVENANCE = (  # (local) per plan §W6-8 fixture-1 description
    "pin computed in s86_w4_p5_sector_2_k_invariant.npz consumed at S88 W-9 §V.1"
)


def fixture_1() -> dict:
    r = class_d_inheritance_routing(FIXTURE_1_PROVENANCE)
    expected_class = "Class-(d)"
    expected_match = "W4-2"
    expected_band = "MANDATORY"
    passes = (
        r["inheritance_class"] == expected_class
        and r["calibration_corpus_match"] == expected_match
        and r["severity_band"] == expected_band
    )
    return {"fixture": 1, "name": "class_d_w4_2_inheritance_detect",
            "expected_class": expected_class, "got_class": r["inheritance_class"],
            "expected_match": expected_match, "got_match": r["calibration_corpus_match"],
            "expected_band": expected_band, "got_band": r["severity_band"],
            "passes": passes, "report": r}


# ---------------------------------------------------------------------------
# Fixture 2 — W9b-2 inheritance detection
# ---------------------------------------------------------------------------
FIXTURE_2_PROVENANCE = (  # (local)
    "pin computed in s87_w9b_pole_specificity_scan.npz consumed at S89 W-6 A.41"
)


def fixture_2() -> dict:
    r = class_d_inheritance_routing(FIXTURE_2_PROVENANCE)
    expected_class = "Class-(d)"
    expected_match = "W9b-2"
    expected_band = "MANDATORY"
    passes = (
        r["inheritance_class"] == expected_class
        and r["calibration_corpus_match"] == expected_match
        and r["severity_band"] == expected_band
    )
    return {"fixture": 2, "name": "class_d_w9b_2_inheritance_detect",
            "expected_class": expected_class, "got_class": r["inheritance_class"],
            "expected_match": expected_match, "got_match": r["calibration_corpus_match"],
            "expected_band": expected_band, "got_band": r["severity_band"],
            "passes": passes, "report": r}


# ---------------------------------------------------------------------------
# Fixture 3 — NOT-IN-CLASS-D-CORPUS route
# ---------------------------------------------------------------------------
FIXTURE_3_PROVENANCE = (  # (local)
    "pin computed in s85_w0_zubarev_lmax_convergence_to_minus_one.npz"
)


def fixture_3() -> dict:
    r = class_d_inheritance_routing(FIXTURE_3_PROVENANCE)
    expected_class = "NOT-IN-CLASS-D-CORPUS"
    passes = (
        r["inheritance_class"] == expected_class
        and r["calibration_corpus_match"] is None
    )
    return {"fixture": 3, "name": "not_in_class_d_corpus_route",
            "expected_class": expected_class, "got_class": r["inheritance_class"],
            "got_match": r["calibration_corpus_match"],
            "passes": passes, "report": r}


# ---------------------------------------------------------------------------
# Live cross-check — W6-7 (A.41) output as test case
# ---------------------------------------------------------------------------
A41_LIVE_PROVENANCE = (  # (local)
    "computations/session-89/s89_w6_d_max_measurement_w9b_2_vs_pv_pipeline.npz "
    "consumes W9b-2 SCHEMATIC output (s87_w9b_pole_specificity_scan.npz key 'rho_S_s4')"
)


def live_cross_check_a41() -> dict:
    r = class_d_inheritance_routing(A41_LIVE_PROVENANCE)
    expected_class = "Class-(d)"
    expected_match = "W9b-2"
    passes = (
        r["inheritance_class"] == expected_class
        and r["calibration_corpus_match"] == expected_match
    )
    return {"live_cross_check": "A.41_W6_7_output",
            "provenance": A41_LIVE_PROVENANCE,
            "expected_class": expected_class, "got_class": r["inheritance_class"],
            "expected_match": expected_match, "got_match": r["calibration_corpus_match"],
            "passes": passes, "report": r}


def run_all() -> dict:
    f1 = fixture_1()
    f2 = fixture_2()
    f3 = fixture_3()
    live = live_cross_check_a41()
    all_pass = (f1["passes"] and f2["passes"] and f3["passes"]
                and live["passes"])
    return {
        "gate": "S89-SOURCE-RECONCILIATION-CLASS-D-ROUTING-EXTENSION",
        "fixture_1": f1,
        "fixture_2": f2,
        "fixture_3": f3,
        "live_cross_check": live,
        "all_pass": all_pass,
        "verdict": "PASS" if all_pass else "FAIL",
    }


def main() -> int:
    report = run_all()
    print(json.dumps(report, indent=2))
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
