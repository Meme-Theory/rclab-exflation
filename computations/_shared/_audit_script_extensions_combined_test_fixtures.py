#!/usr/bin/env python
"""
_audit_script_extensions_combined_test_fixtures.py — S89 W6-3 fixtures
=======================================================================

Combined synthetic test fixtures for the 4 sub-item extensions in
S89 W6-3 (S89-AUDIT-SCRIPT-EXTENSIONS-COMBINED).

Six sub-fixtures (per plan §W6-3 §6 sub-item descriptions):

  Fixture 1A — cohomology-class surrogate WITH all 3 §(iv-bis) clauses → PASS
  Fixture 1B — cohomology-class surrogate MISSING combinatorial lock → FAIL
  Fixture 2  — registry-md citing §VII.AN with script-not-found → conflation/FAIL
  Fixture 3A — falsifier-inventory row with absolute-value wrap → tautology/FAIL
  Fixture 3B — falsifier-inventory row with signed prediction → PASS
  Fixture 4A — §VII.AE Level-2 + §VII.AD Level-1 + cocycle functor cited → PASS
  Fixture 4B — §VII.AE missing Level-2 declaration → FAIL

Sub-item PASS criterion: BOTH calibration cases (positive + negative)
return expected verdicts. Combined PASS = AND over the 4 sub-items.

CLI
---
    python _audit_script_extensions_combined_test_fixtures.py
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: E402,F401,F403  (per CLAUDE.md mandatory)

from _substrate_first_provenance_audit import cohomology_class_surrogate_audit  # noqa: E402
from _falsifier_inventory_audit import sign_pass_tautology_audit  # noqa: E402
from _v4_anchor_structure_audit import v4_anchor_structure_audit  # noqa: E402
from _source_reconciliation_audit import class_g_registry_anchor_route_audit  # noqa: E402


# ===========================================================================
# Sub-item (i) — cohomology-class surrogate detection (§(iv-bis))
# ===========================================================================
FIXTURE_1A_BLOCK = (  # (local) all 3 clauses present → PASS
    "Surrogate proposal: substrate-distance-1 spectral-moment ratio "
    "R_surrogate = (Σ_BdG_A − Σ_BdG_M_3C) / (Σ_BdG_A + Σ_BdG_M_3C).\n"
    "Step 1 (Definitions): substitution chain reduces R_surrogate to "
    "Peter-Weyl combinatorial fraction f via R = 2*f − 1.\n"
    "The sign of R_surrogate is mechanically locked to the Peter-Weyl "
    "combinatorial fraction f.\n"
    "A surrogate FAIL does NOT falsify the canonical observable; "
    "surrogate is uninformative on canonical PASS/FAIL.\n"
)

FIXTURE_1B_BLOCK = (  # (local) missing combinatorial-lock disclosure → FAIL
    "Surrogate proposal: substrate-distance-1 spectral-moment ratio "
    "R_surrogate = (Σ_BdG_A − Σ_BdG_M_3C) / (Σ_BdG_A + Σ_BdG_M_3C).\n"
    "Step 1 (Definitions): substitution chain reduces R_surrogate to "
    "component substrate-physics quantities.\n"
    "A surrogate FAIL does NOT falsify the canonical observable; "
    "surrogate is uninformative on canonical PASS/FAIL.\n"
)


def fixture_1a() -> dict:
    r = cohomology_class_surrogate_audit(FIXTURE_1A_BLOCK)
    return {"fixture": "1A", "expected": "PASS", "got": r["verdict"],
            "passes": r["verdict"] == "PASS", "report": r}


def fixture_1b() -> dict:
    r = cohomology_class_surrogate_audit(FIXTURE_1B_BLOCK)
    return {"fixture": "1B", "expected": "FAIL", "got": r["verdict"],
            "passes": r["verdict"] == "FAIL"
                      and r.get("severity") == "MANDATORY",
            "report": r}


# ===========================================================================
# Sub-item (ii) — Class-(g) REGISTRY-ANCHOR conflation
# ===========================================================================
FIXTURE_2_REGISTRY_MD = (  # (local) §VII.AN cite + script not on disk
    "## §VII.AN Path-H/Path-C multi-valued classification\n"
    "Anchor: S82 W3-9 single-pole Mellin closure derivation per the f0/f2/f4 "
    "Mellin moment pins (Route-A).\n"
)


def fixture_2() -> dict:
    """
    Fixture-by-construction: write FIXTURE_2_REGISTRY_MD to a temp file,
    run class_g_registry_anchor_route_audit pointing at a scripts_dir
    that is empty (so cited_script not found → conflation=True).
    """
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        registry = td / "_fixture_registry.md"
        registry.write_text(FIXTURE_2_REGISTRY_MD, encoding="utf-8")
        scripts = td / "_fixture_scripts"
        scripts.mkdir()
        # No scripts in scripts_dir; cited script not found
        r = class_g_registry_anchor_route_audit(registry, scripts)
    expected_verdict = "FAIL"
    expected_conflation = True
    has_correct_verdict = (r.get("verdict") == expected_verdict)
    has_correct_conflation = any(
        f.get("conflation") == expected_conflation for f in r.get("findings", []))
    return {"fixture": "2", "expected_verdict": expected_verdict,
            "got": r.get("verdict"),
            "passes": has_correct_verdict and has_correct_conflation,
            "n_findings": len(r.get("findings", [])),
            "report": {k: r[k] for k in r if k != "findings"}}


# ===========================================================================
# Sub-item (iii) — sign-PASS-tautology detection
# ===========================================================================
FIXTURE_3A_INVENTORY = (  # (local) row wrapped in |...| with > bound → tautology
    "| F1 | |3He-B BDI vortex-core| > 0.2 | substrate-clean | NULL on F1 |\n"
)

FIXTURE_3B_INVENTORY = (  # (local) row with signed prediction → PASS
    "| F2 | n_s − 0.965 = -0.0089 | substrate-physics | PASS at +/-0.005 |\n"
)


def fixture_3a() -> dict:
    r = sign_pass_tautology_audit(FIXTURE_3A_INVENTORY)
    return {"fixture": "3A", "expected": "FAIL", "got": r["verdict"],
            "passes": r["verdict"] == "FAIL"
                      and r["n_tautology_rows"] >= 1,
            "report": r}


def fixture_3b() -> dict:
    r = sign_pass_tautology_audit(FIXTURE_3B_INVENTORY)
    return {"fixture": "3B", "expected": "PASS", "got": r["verdict"],
            "passes": r["verdict"] == "PASS"
                      and r["n_tautology_rows"] == 0,
            "report": r}


# ===========================================================================
# Sub-item (iv) — V_4 §VII.AE-vs-§VII.AD anchor-structure
# ===========================================================================
FIXTURE_4A_REGISTRY = (  # (local) all 3 markers present → PASS
    "## §VII.AD Δ_0 LOCALIZATION FORMULA (Level-1 single-τ-slice substrate-IS)\n"
    "Δ_0 = 4·c_{σ⁻¹((-1,-1))} on substrate (2,4,8,6) at single-τ-slice τ_fold = 0.190.\n"
    "\n"
    "## §VII.AE moduli-space τ-asymmetry (Level-2 moduli-deformation substrate-IS)\n"
    "τ-asymmetric breakdown geometry under the cocycle functor F : m(p,q) → Δ_0\n"
    "across the V_4-triality multi-orbit deformation manifold.\n"
)

FIXTURE_4B_REGISTRY = (  # (local) §VII.AE missing Level-2 declaration → FAIL
    "## §VII.AD Δ_0 LOCALIZATION FORMULA (Level-1 single-τ-slice substrate-IS)\n"
    "Δ_0 = 4·c_{σ⁻¹((-1,-1))} on substrate (2,4,8,6).\n"
    "\n"
    "## §VII.AE moduli-space τ-asymmetry\n"
    "τ-asymmetric breakdown geometry. (No Level-2 declaration; no cocycle functor cited.)\n"
)


def fixture_4a() -> dict:
    r = v4_anchor_structure_audit(FIXTURE_4A_REGISTRY)
    return {"fixture": "4A", "expected": "PASS", "got": r["verdict"],
            "passes": r["verdict"] == "PASS",
            "report": r}


def fixture_4b() -> dict:
    r = v4_anchor_structure_audit(FIXTURE_4B_REGISTRY)
    return {"fixture": "4B", "expected": "FAIL", "got": r["verdict"],
            "passes": r["verdict"] == "FAIL",
            "report": r}


# ===========================================================================
# Combined runner
# ===========================================================================
def run_all() -> dict:
    f1a, f1b = fixture_1a(), fixture_1b()
    f2 = fixture_2()
    f3a, f3b = fixture_3a(), fixture_3b()
    f4a, f4b = fixture_4a(), fixture_4b()

    sub_item_i = f1a["passes"] and f1b["passes"]
    sub_item_ii = f2["passes"]
    sub_item_iii = f3a["passes"] and f3b["passes"]
    sub_item_iv = f4a["passes"] and f4b["passes"]
    combined_pass = sub_item_i and sub_item_ii and sub_item_iii and sub_item_iv

    return {
        "gate": "S89-AUDIT-SCRIPT-EXTENSIONS-COMBINED",
        "sub_item_i_pass": sub_item_i,
        "sub_item_ii_pass": sub_item_ii,
        "sub_item_iii_pass": sub_item_iii,
        "sub_item_iv_pass": sub_item_iv,
        "combined_pass": combined_pass,
        "verdict": "PASS" if combined_pass else "FAIL",
        "fixtures": {
            "1A": f1a, "1B": f1b,
            "2": f2,
            "3A": f3a, "3B": f3b,
            "4A": f4a, "4B": f4b,
        },
    }


def main() -> int:
    report = run_all()
    print(json.dumps(report, indent=2))
    return 0 if report["combined_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
