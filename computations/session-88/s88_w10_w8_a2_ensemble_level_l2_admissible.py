#!/usr/bin/env python3
"""
S88 W10-111 — S88-CF-W8-A2-ENSEMBLE-LEVEL-L2-FULLY-ADMISSIBLE-RE-DERIVATION
==========================================================================

Gate: S88-CF-W8-A2-ENSEMBLE-LEVEL-L2-FULLY-ADMISSIBLE-RE-DERIVATION ([VERIFY])

Pre-registered threshold (plan §W10-111):
  PASS iff 10/10 pairs (R, R') ∈ A_4 × A_4 satisfy
       rel_diff(M^{(R)}_4, M^{(R')}_4) ≤ 1e-12   (Reading_1 ENSEMBLE-PRESERVES-COMPOSITION)
  FAIL iff ≤ 1/10 pairs PASS                       (Reading_2 ZUBAREV-SINGLETON-BINDING)
  INFO iff 2 ≤ pair_count ≤ 9                      (partial ensemble admissibility)

Hypothesis: §VII.K-PROP A/B/C-trio L2-FULLY-ADMISSIBLE composition theorem
  extends from Zubarev-singleton-bound (CAC) to ensemble-bound across A_4.
  Reading_1 PASS = ensemble preserves composition; Reading_2 FAIL = singleton.

MCP-pre-registered context (from search_knowledge):
  - §VII.K-PROP-W8 registry text states L2_FULLY_ADMISSIBLE is EXISTENTIAL:
    "(∃ R ∈ A_4 : 3c PASS_R) AND (other 3 channels PASS)" — NOT pairwise.
  - S87 atlas-cardinality cascade workshop established
    A_HBW = {R ∈ A_4 : 3c PASS_R} = {ζ, anomaly} = A_2 at L_max=12, s=3,
    1e-12 strict threshold. Only 2 of 4 regulators are HBW-positive at s=3.
  - The present gate tests at substrate-distance-2 pole s=4 with L_max=10
    (a different pole + truncation than S87's s=3 + L_max=12 result).
  - F_4 = {ζ, Zubarev, SDW} = pure-a_4-Mellin-support cluster (the (A)-class).
  - The (C)-class member in A_4 is just {anomaly} (cutoff_sqrt excluded
    from plan A_4).

Substrate framing (.claude/rules/phononic-framing.md "IS Space, Not IN Space"):
  The substrate IS the 4-channel layer-2 weight vector W^{(R)}_i. The
  composition law is the substrate's own algebraic structure under Mellin
  convolution; the ensemble-level admissibility predicate is the substrate
  IS-property, not an externally-imposed selection rule.

LEVEL pin discipline (.claude/rules/substrate-first-canonical-sourcing.md §(iv)
  MANDATORY at K=4): consumes _spectral_action_regulators.py SCHEMATIC.
  CLASS pin = SCHEMATIC (TIER-2); convention suffix = -SCHEMATIC.

Atlas-name → schematic-evaluator mapping (TIER-2 SCHEMATIC; same as §W10-110):
  zeta    → zeta_a_n
  zubarev → mellin_a_n
  SDW     → heat_kernel_a_n
  anomaly → pauli_villars_a_n

Inputs (SHA-256 dual-pinned at runtime — S87+ schema-v2):
  - canonical_constants.py
  - computations/_shared/_spectral_action_regulators.py
  - script bytes
"""

from __future__ import annotations

import os

# === Phase 2b X2 transform bootstrap ===
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
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

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

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = _x2_project_root()
SHARED_DIR = _x2_shared_dir()

GATE_ID = "S88-CF-W8-A2-ENSEMBLE-LEVEL-L2-FULLY-ADMISSIBLE-RE-DERIVATION"         # (local)
SCHEME = "ensemble-level-L2-pairwise"                                             # (local)
CONVENTION = "A_4-Mellin-pairwise-rel-diff-substrate-distance-2-SCHEMATIC"        # (local)
L_MAX_TAG = 10                                                                    # (local)
L_MAX = 10                                                                        # (local)
SUBSTRATE_DISTANCE_POLE_N = 4                                                     # (local) s=4 pole

REL_TOL_PASS_PAIR = 1e-12                                                         # (local)
REL_TOL_FAIL_PAIR = 1e-9                                                          # (local)

ATLAS_A_4 = ("zeta", "zubarev", "SDW", "anomaly")                                 # (local)

EVALUATOR_MAP = {                                                                 # (local)
    "zeta":    zeta_a_n,
    "zubarev": mellin_a_n,
    "SDW":     heat_kernel_a_n,
    "anomaly": pauli_villars_a_n,
}

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                            # (local)
SCHEMATIC_MODULE_PATH = SHARED_DIR / "_spectral_action_regulators.py"             # (local)

OUT_NPZ = resolve_output(88, "s88_w10_w8_a2_ensemble_level_l2_admissible.npz")    # (local)
OUT_JSON = resolve_output(88, "s88_w10_w8_a2_ensemble_level_l2_admissible.json")  # (local)
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


def compute():
    print()
    print(f"=== {GATE_ID} compute ===")
    print(f"L_max={L_MAX}  s_pole={SUBSTRATE_DISTANCE_POLE_N}")
    print(f"A_4 = {ATLAS_A_4}")
    print()

    # Compute M^{(R)}_4(L_max=10) for each R ∈ A_4
    moments = {}                                                                  # (local)
    for R in ATLAS_A_4:
        evaluator = EVALUATOR_MAP[R]                                              # (local)
        moments[R] = evaluator(SUBSTRATE_DISTANCE_POLE_N, L_MAX, Vol_SU3_Haar)
        print(f"  M^({R})_{SUBSTRATE_DISTANCE_POLE_N}(L_max={L_MAX}) = {moments[R]:.12e}")
    print()

    # Build 4×4 pairwise rel_diff matrix
    pair_matrix = {}                                                              # (local)
    pass_count = 0                                                                # (local)
    info_count = 0                                                                # (local)
    fail_count = 0                                                                # (local)
    pair_rows = []                                                                # (local)

    for i, R1 in enumerate(ATLAS_A_4):
        for j, R2 in enumerate(ATLAS_A_4):
            m1 = moments[R1]                                                      # (local)
            m2 = moments[R2]                                                      # (local)
            if i == j:
                rel_diff = 0.0                                                    # (local)
                kind = "diagonal"                                                 # (local)
            else:
                denom = max(abs(m1), abs(m2)) if max(abs(m1), abs(m2)) > 0 else 1.0  # (local)
                rel_diff = abs(m1 - m2) / denom
                kind = "off_diagonal"                                             # (local)
            if rel_diff <= REL_TOL_PASS_PAIR:
                pair_verdict = "PASS"                                             # (local)
                pass_count += 1
            elif rel_diff > REL_TOL_FAIL_PAIR:
                pair_verdict = "FAIL"                                             # (local)
                fail_count += 1
            else:
                pair_verdict = "INFO"                                             # (local)
                info_count += 1
            pair_matrix[f"{R1}--{R2}"] = {
                "rel_diff": rel_diff,
                "verdict": pair_verdict,
                "kind": kind,
            }
            pair_rows.append({
                "R1": R1, "R2": R2, "rel_diff": rel_diff,
                "verdict": pair_verdict, "kind": kind,
            })

    print("Pairwise admissibility matrix:")
    print(f"  {'R1':<10s} {'R2':<10s} {'rel_diff':<14s} {'verdict':<6s} kind")
    for row in pair_rows:
        print(f"  {row['R1']:<10s} {row['R2']:<10s} {row['rel_diff']:.6e}    "
              f"{row['verdict']:<6s} {row['kind']}")
    print()

    print(f"PASS pairs: {pass_count}/16  (4 diagonal + {pass_count - 4} off-diagonal)")
    print(f"INFO pairs: {info_count}/16")
    print(f"FAIL pairs: {fail_count}/16")
    print()
    # The plan threshold is on "pairs" interpreted as the 10 distinct pairs
    # (4 diagonal + 6 off-diagonal). With unordered pair indexing the count is
    # symmetric: out of 16 ordered pairs, the PASS count divided by 2 (with
    # diagonal counted once) gives the unordered count.
    # Convert ordered → unordered:
    #   unordered_PASS = 4 (diag) + ordered_PASS_off_diag / 2
    #   ordered_PASS_off_diag = pass_count - 4
    pass_count_unordered = 4 + (pass_count - 4) // 2                              # (local)
    info_count_unordered = info_count // 2                                        # (local)
    fail_count_unordered = fail_count // 2                                        # (local)
    print(f"Unordered pair counts (4 diag + 6 off-diag = 10):")
    print(f"  PASS: {pass_count_unordered}/10")
    print(f"  INFO: {info_count_unordered}/10")
    print(f"  FAIL: {fail_count_unordered}/10")

    # Verdict per plan thresholds
    if pass_count_unordered == 10:
        reading = "Reading_1_ENSEMBLE_PRESERVES_COMPOSITION_PASS"                 # (local)
    elif pass_count_unordered <= 1:
        reading = "Reading_2_ZUBAREV_SINGLETON_BINDING_FAIL"                      # (local)
    else:
        reading = "INFO_PARTIAL_ENSEMBLE_ADMISSIBILITY"                           # (local)

    # HBW-positive subset {R : R is L2-admissible against itself trivially AND
    # against at least one other regulator at PASS}
    hbw_positive = []                                                             # (local)
    for R in ATLAS_A_4:
        # Self-pair always PASSes; check off-diagonal pairs for any PASS
        any_off_diag_pass = any(
            pair_matrix[f"{R}--{R2}"]["verdict"] == "PASS"
            for R2 in ATLAS_A_4 if R2 != R
        )
        if any_off_diag_pass:
            hbw_positive.append(R)
    print(f"\nHBW-positive subset (regulators with at least one PASSing off-diagonal pair):")
    print(f"  {hbw_positive}  → cardinality {len(hbw_positive)}")

    return {
        "value": (
            f"pair_count_PASS_unordered={pass_count_unordered}/10;"
            f"INFO={info_count_unordered}/10;FAIL={fail_count_unordered}/10;"
            f"reading={reading};HBW_positive_subset={hbw_positive}"
        ),
        "moments": moments,
        "pair_matrix": pair_matrix,
        "pass_count_unordered": pass_count_unordered,
        "info_count_unordered": info_count_unordered,
        "fail_count_unordered": fail_count_unordered,
        "reading": reading,
        "hbw_positive": hbw_positive,
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
    pc = result["pass_count_unordered"]                                           # (local)
    if pc == 10:
        return "PASS"
    if pc <= 1:
        return "FAIL"
    return "INFO"


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
        moments_zeta=result["moments"]["zeta"],
        moments_zubarev=result["moments"]["zubarev"],
        moments_SDW=result["moments"]["SDW"],
        moments_anomaly=result["moments"]["anomaly"],
        pass_count_unordered=result["pass_count_unordered"],
        info_count_unordered=result["info_count_unordered"],
        fail_count_unordered=result["fail_count_unordered"],
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
        "moments": result["moments"],
        "pair_matrix": {k: {"rel_diff": v["rel_diff"], "verdict": v["verdict"], "kind": v["kind"]}
                        for k, v in result["pair_matrix"].items()},
        "pass_count_unordered": result["pass_count_unordered"],
        "info_count_unordered": result["info_count_unordered"],
        "fail_count_unordered": result["fail_count_unordered"],
        "reading": result["reading"],
        "hbw_positive": result["hbw_positive"],
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
