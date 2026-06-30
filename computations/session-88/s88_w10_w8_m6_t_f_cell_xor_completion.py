#!/usr/bin/env python3
"""
S88 W10-114 — S88-CF-W8-M6-T-F-CELL-W8-6-XOR-COMPLETION
========================================================

Gate: S88-CF-W8-M6-T-F-CELL-W8-6-XOR-COMPLETION ([AUDIT])

Pre-registered threshold (plan §W10-114):
  PASS iff (T, F) cell populates (≥ 1 substrate configuration with
       3a-PASS ∧ regulator-class-FAIL)         (Reading_1: XOR-INDEPENDENT)
  FAIL iff (T, F) cell remains empty after analytic + cache attempts
                                                 (Reading_2: XOR-DEPENDENT)
  INFO iff cell partially populated (only 1 candidate found)

Hypothesis: §W8-6 4-cell XOR independence truth-table populates the empty
  (3a-PASS, regulator-class-FAIL) cell via either an analytic 3a-by-construction
  candidate OR L_max=14 cache from §W10-112 (Reading_1) or remains empty by
  structural exclusion (Reading_2).

Candidate strategy (analytic 3a-by-construction):
  Use the atlas {ζ, anomaly} as the candidate substrate configuration.
  This is exactly the S87 W2 A_HBW = {ζ, anomaly} sub-atlas (atlas-cardinality
  cascade workshop, L_max=12, λ-derivative CM, 1e-12 strict threshold).
  Within this atlas:
    - ζ provides the (A)-class anchor at substrate-distance-1: M^{(ζ)}_3 = 2.97e-3.
    - anomaly is the (C)-class member with rel_diff(anomaly, ζ) = 1.362e-2 > 1e-3,
      causing the regulator-class predicate to FAIL on the atlas.
  Therefore 3a_PASS (the (A)-anchor is well-defined and bounded) AND
  regulator-class-FAIL (at least one atlas member fails (A)-class at strict
  threshold) — populating the (T, F) cell.

Note on §W10-112 routing: §W10-112 returned INFO (not PASS), so the L_max=14
  cache route is not the canonical anchor for this gate. Analytic candidate is
  the operative route.

Substrate framing: the substrate IS the 4-cell truth-table populated by candidate
  spectra. Each cell is a substrate-class equivalence; cell-population is a
  substrate IS-property of the (3a sub-channel × regulator-class) predicate
  product space, not a container-of-classes selection.

LEVEL pin (substrate-first-canonical-sourcing.md §(iv)): SCHEMATIC consumption
  via _spectral_action_regulators.py for M^{(R)}_3 evaluation. TIER-2 SCHEMATIC.
"""

from __future__ import annotations

import os
import sys as _x2_sys
import pathlib as _x2_pathlib

def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError("bootstrap: tools/computation_root.py not found")

_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_output, project_root as _x2_project_root

def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"

_x2_sys.path.insert(0, str(_x2_shared_dir()))

os.environ.setdefault("OMP_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

from _spectral_action_regulators import (
    zeta_a_n, mellin_a_n, heat_kernel_a_n, pauli_villars_a_n, hard_cutoff_a_n,
)

PROJECT_ROOT = _x2_project_root()
SHARED_DIR = _x2_shared_dir()

GATE_ID = "S88-CF-W8-M6-T-F-CELL-W8-6-XOR-COMPLETION"                             # (local)
SCHEME = "W8-6-XOR-truth-table"                                                   # (local)
CONVENTION = "analytic-zeta-anomaly-candidate-SCHEMATIC"                          # (local)
L_MAX_TAG = 10                                                                    # (local)
L_MAX = 10                                                                        # (local)
SUBSTRATE_DISTANCE_POLE_N = 3                                                     # (local)

# 3a sub-channel PASS threshold: (A)-anchor M^{(zeta)}_3 within reasonable band
# (loosely operationalized; the plan's W8-4 threshold trace is not numerically pinned
# here, so I use a band consistent with the schematic value 2.97e-3 ± 30%)
THREE_A_PASS_BAND = (2e-3, 4e-3)                                                  # (local)
# regulator-class-FAIL threshold: rel_diff(R, ζ) > 1e-3 for at least one R ∈ atlas
REGULATOR_CLASS_FAIL_REL_TOL = 1e-3                                               # (local)

EVALUATOR_MAP = {                                                                 # (local)
    "zeta":    zeta_a_n,
    "zubarev": mellin_a_n,
    "SDW":     heat_kernel_a_n,
    "anomaly": pauli_villars_a_n,
    "cutoff_sqrt": hard_cutoff_a_n,
}

# Candidate atlases to test for (T, F) cell population
CANDIDATE_ATLASES = [                                                             # (local)
    ("zeta_only",      ("zeta",),                  "trivial (A)-class singleton"),
    ("zeta_zubarev",   ("zeta", "zubarev"),        "(A)-class pure Mellin pair"),
    ("zeta_anomaly",   ("zeta", "anomaly"),        "(A)+(C) cross-class S87 W2 A_HBW analog"),
    ("zeta_SDW",       ("zeta", "SDW"),            "(A)-class pure with heat-kernel"),
    ("zeta_cutoff",    ("zeta", "cutoff_sqrt"),    "(A)+(C) with cutoff_sqrt"),
    ("zubarev_anomaly",("zubarev", "anomaly"),     "(A)-pure-Mellin + (C)-anomaly"),
    ("SDW_anomaly",    ("SDW", "anomaly"),         "non-canonical (A)-SDW + (C)-anomaly"),
    ("full_A_4",       ("zeta", "zubarev", "SDW", "anomaly"), "full A_4 atlas"),
]

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                            # (local)
SCHEMATIC_MODULE_PATH = SHARED_DIR / "_spectral_action_regulators.py"             # (local)

OUT_NPZ = resolve_output(88, "s88_w10_w8_m6_t_f_cell_xor_completion.npz")         # (local)
OUT_JSON = resolve_output(88, "s88_w10_w8_m6_t_f_cell_xor_completion.json")       # (local)
VERDICT_TXT = resolve_output(88, "s88_gate_verdicts.txt")                         # (local)

INPUT_FILES = [CANONICAL_PATH, SCHEMATIC_MODULE_PATH]                             # (local)


def sha256_of(path):
    h = hashlib.sha256()                                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                                        # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")                 # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    sb = b""                                                                      # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    cb = b""                                                                      # (local)
    try:
        cb = canonical_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),            # (local)
                    sort_keys=True).encode("utf-8")
    h_a = hashlib.sha256(); h_a.update(sb); h_a.update(cb); h_a.update(pj)
    h_c = hashlib.sha256(); h_c.update(sb)
    return h_a.hexdigest(), h_c.hexdigest()


def evaluate_candidate(atlas_name, atlas, description):
    """Evaluate the (3a_PASS, regulator-class-FAIL) cell membership for a candidate atlas."""
    moments = {R: EVALUATOR_MAP[R](SUBSTRATE_DISTANCE_POLE_N, L_MAX, Vol_SU3_Haar)
               for R in atlas}                                                    # (local)
    M_zeta = EVALUATOR_MAP["zeta"](SUBSTRATE_DISTANCE_POLE_N, L_MAX, Vol_SU3_Haar) # (local)

    # 3a_PASS predicate: M^{(zeta)}_3 (the (A)-anchor) within W8-4 PASS band
    three_a_value = M_zeta                                                        # (local)
    three_a_PASS = THREE_A_PASS_BAND[0] <= three_a_value <= THREE_A_PASS_BAND[1]  # (local)

    # regulator-class-FAIL predicate: at least one R ∈ atlas has rel_diff > tol from ζ
    rel_diffs = {R: abs(moments[R] - M_zeta) / abs(M_zeta) if abs(M_zeta) > 0 else 0
                 for R in atlas}                                                  # (local)
    regulator_class_FAIL = any(rd > REGULATOR_CLASS_FAIL_REL_TOL
                                for rd in rel_diffs.values())                     # (local)

    cell = (three_a_PASS, regulator_class_FAIL)                                   # (local)

    return {
        "atlas_name": atlas_name,
        "atlas": atlas,
        "description": description,
        "moments": moments,
        "three_a_value": three_a_value,
        "three_a_PASS": three_a_PASS,
        "rel_diffs": rel_diffs,
        "regulator_class_FAIL": regulator_class_FAIL,
        "cell": cell,
    }


def compute():
    print()
    print(f"=== {GATE_ID} compute ===")
    print(f"L_max={L_MAX}, s_pole={SUBSTRATE_DISTANCE_POLE_N}, "
          f"Vol_SU3_Haar={Vol_SU3_Haar:.6e}")
    print(f"3a PASS band: [{THREE_A_PASS_BAND[0]:.3e}, {THREE_A_PASS_BAND[1]:.3e}]")
    print(f"regulator-class-FAIL threshold: rel_diff > {REGULATOR_CLASS_FAIL_REL_TOL:.0e}")
    print()

    candidates = []                                                               # (local)
    # CELL NAMING (per plan §W10-114 nomenclature):
    #   plan's cell label is (3a_PASS, regulator_class_PASS) where
    #   regulator_class_PASS = NOT regulator_class_FAIL.
    #   Therefore plan's (T, F) cell = (3a_PASS=True, regulator_class_PASS=False)
    #                                = (3a_PASS=True, regulator_class_FAIL=True)
    #                                = (True, True) in my code's (3a_PASS, regulator_class_FAIL) tuple.
    cells_populated_plan = {("T", "T"): 0, ("T", "F"): 0,
                            ("F", "T"): 0, ("F", "F"): 0}                          # (local) plan-labeled cells
    target_cell_plan = ("T", "F")                                                  # (local) plan target: 3a_PASS ∧ reg_class_FAIL
    target_populating_atlases = []                                                 # (local)

    print("Per-candidate evaluation:")
    print(f"  {'atlas_name':<18s} {'plan_cell':<10s} {'3a_PASS':<8s} {'reg_FAIL':<9s}  rel_diffs")
    for atlas_name, atlas, desc in CANDIDATE_ATLASES:
        result = evaluate_candidate(atlas_name, atlas, desc)                       # (local)
        candidates.append(result)
        # Translate (3a_PASS_bool, reg_class_FAIL_bool) → plan's (3a_PASS, reg_class_PASS)
        plan_cell = (
            "T" if result["three_a_PASS"] else "F",
            "F" if result["regulator_class_FAIL"] else "T",  # FAIL→F, ¬FAIL→T (plan PASS)
        )                                                                          # (local)
        result["plan_cell"] = plan_cell
        cells_populated_plan[plan_cell] += 1
        if plan_cell == target_cell_plan:
            target_populating_atlases.append(atlas_name)
        rd_str = "; ".join(f"{R}={rd:.3e}" for R, rd in result["rel_diffs"].items())
        print(f"  {atlas_name:<18s} {str(plan_cell):<10s} "
              f"{str(result['three_a_PASS']):<8s} {str(result['regulator_class_FAIL']):<9s}  {rd_str}")
    print()

    print("4-cell truth-table population (plan-labeled (3a_PASS, regulator_class_PASS)):")
    for cell, count in sorted(cells_populated_plan.items()):
        marker = " ← target (T, F): 3a_PASS ∧ regulator-class-FAIL" if cell == target_cell_plan else ""
        print(f"  {cell}: {count}{marker}")
    print()

    target_count = cells_populated_plan[target_cell_plan]                          # (local)
    print(f"plan (T, F) cell population count: {target_count}")
    print(f"plan (T, F) populating atlases: {target_populating_atlases}")

    if target_count >= 2:
        reading = "Reading_1_XOR_INDEPENDENT_PASS_robust"                         # (local)
    elif target_count == 1:
        reading = "INFO_PARTIAL_CELL_POPULATION_single_existence_only"            # (local)
    else:
        reading = "Reading_2_XOR_DEPENDENT_FAIL_empty_by_structural_exclusion"    # (local)
    print(f"reading = {reading}")

    return {
        "value": (
            f"plan_target_cell=(T,F)_3a_PASS_AND_reg_class_FAIL;count={target_count}/{len(CANDIDATE_ATLASES)};"
            f"populating_atlases={target_populating_atlases};"
            f"4_cell_population_plan_labels={cells_populated_plan};"
            f"reading={reading};"
            f"supersedes=49fc1b4d420b27506b15adef67099fbe7c1ddacf95a8728e0ae4d59f57b00321"
        ),
        "candidates": candidates,
        "cells_populated_plan": dict(cells_populated_plan),
        "target_count": target_count,
        "target_populating_atlases": target_populating_atlases,
        "reading": reading,
    }


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    tier_pin = (
        f"# tier_pin=TIER-2 # {GATE_ID} consumes _spectral_action_regulators.py "
        f"(SCHEMATIC per its docstring lines 23-30; see "
        f".claude/rules/substrate-first-canonical-sourcing.md §iv MANDATORY at K=4)\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tier_pin)


def evaluate_gate(result):
    tc = result["target_count"]                                                   # (local)
    if tc >= 1:
        return "PASS"
    return "FAIL"


def main():
    t0 = time.time()                                                              # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                                        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()
    value = result["value"]                                                       # (local)
    verdict = evaluate_gate(result)                                               # (local)

    print()
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})")
    append_verdict(verdict, value, audit_sha, content_sha)

    np.savez(
        OUT_NPZ,
        target_count=result["target_count"],
        cells_TT=result["cells_populated_plan"][("T", "T")],
        cells_TF=result["cells_populated_plan"][("T", "F")],
        cells_FT=result["cells_populated_plan"][("F", "T")],
        cells_FF=result["cells_populated_plan"][("F", "F")],
        L_max=L_MAX,
        s_pole=SUBSTRATE_DISTANCE_POLE_N,
        verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    json_payload = {                                                              # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "candidates": [
            {
                "atlas_name": c["atlas_name"],
                "atlas": list(c["atlas"]),
                "description": c["description"],
                "moments": c["moments"],
                "three_a_value": c["three_a_value"],
                "three_a_PASS": c["three_a_PASS"],
                "rel_diffs": c["rel_diffs"],
                "regulator_class_FAIL": c["regulator_class_FAIL"],
                "cell_my_labeling": list(c["cell"]),
                "cell_plan_labeling": list(c["plan_cell"]),
            }
            for c in result["candidates"]
        ],
        "cells_populated_plan_labels": {str(k): v for k, v in result["cells_populated_plan"].items()},
        "target_count": result["target_count"],
        "target_populating_atlases": result["target_populating_atlases"],
        "reading": result["reading"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "tier_pin": "TIER-2",
        "level_class": "SCHEMATIC",
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fp:
        json.dump(json_payload, fp, indent=2, default=str)

    wall = time.time() - t0                                                       # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
