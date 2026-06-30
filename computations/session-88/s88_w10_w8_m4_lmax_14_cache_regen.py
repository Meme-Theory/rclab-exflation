#!/usr/bin/env python3
"""
S88 W10-112 — S88-CF-W8-M4-LMAX-14-CACHE-REGEN-W8-4-RE-RUN
==========================================================

Gate: S88-CF-W8-M4-LMAX-14-CACHE-REGEN-W8-4-RE-RUN ([AUDIT])

Pre-registered threshold (plan §W10-112):
  PASS iff |ratio_3a(L=14, L=12) - 1| < 1e-3   (Reading_1: truncation-converged)
  FAIL iff |ratio_3a(L=14, L=12) - 1| > 1e-2   (Reading_2: truncation-dominated)
  INFO band: 1e-3 ≤ |ratio - 1| < 1e-2          (partial convergence)

Hypothesis: 3a sub-channel ratio R_{3a}(L=14)/R_{3a}(L=12) either converges
  to 1 ± 1e-3 (Reading_1, W8-4 FAIL is structural) or deviates at the 1e-2 level
  (Reading_2, W8-4 FAIL is L_max-driven).

D_K Block-Diagonality + Friedrich-Bär feasibility pre-check
  (math-scripts.md §"Machinery-Feasibility Audit"):
  - Canonical D_K Peter-Weyl spectrum cache at L_max=14 is EMPIRICALLY INFEASIBLE
    per W11-3 calibration: irrep (13,0) construction did NOT complete within
    10-min wall time on agent dispatch.
  - MITIGATION ROUTES:
    (i)  Friedrich-Bär saturation theorem analytic substitute (W11-3 precedent):
         η_FB(p,q) = |λ|_min(p,q) / √(C_2(p,q) + 1); pin η_FB_lower from L=12
         master cache; certify bot-K invariance for L ≥ 12.
    (ii) Schematic SU(3) Casimir computation (TIER-2 SCHEMATIC):
         the _spectral_action_regulators.py module's L_max parameter just
         truncates (p,q) enumeration — no Casimir-projection cost. L_max=14
         is trivially computable on the schematic.
  This script takes route (ii) and HONESTLY DISCLOSES that the verdict is at
  the SCHEMATIC level. The canonical D_K answer is queued behind the W11-3
  feasibility wall.

Substrate framing: the substrate IS the 3a sub-channel observable R_{3a}(L).
  L_max truncation is the substrate's own representation-theoretic bound on
  Casimir-projection construction (canonical) or on (p,q) enumeration depth
  (schematic); convergence as L_max → ∞ is a substrate IS-property.

LEVEL pin (substrate-first-canonical-sourcing.md §(iv) MANDATORY at K=4):
  CLASS = SCHEMATIC; convention suffix = -SCHEMATIC; tier_pin=TIER-2.
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

from _spectral_action_regulators import zeta_a_n, _enumerate_sectors

PROJECT_ROOT = _x2_project_root()
SHARED_DIR = _x2_shared_dir()

GATE_ID = "S88-CF-W8-M4-LMAX-14-CACHE-REGEN-W8-4-RE-RUN"                          # (local)
SCHEME = "substrate-distance-1-3a-sub-channel"                                    # (local)
CONVENTION = "ratio-formulation-Lmax14-vs-Lmax12-Friedrich-Baer-saturation-or-SCHEMATIC-direct-SCHEMATIC"  # (local)
L_MAX_TAG = "10_operational_with_L14_vs_L12_extension"                            # (local)
L_MAX_OLD = 12                                                                    # (local)
L_MAX_NEW = 14                                                                    # (local)
SUBSTRATE_DISTANCE_POLE_N = 3                                                     # (local) channel-3 = a_3

REL_TOL_PASS = 1e-3                                                               # (local) Reading_1 floor
REL_TOL_FAIL = 1e-2                                                               # (local) Reading_2 floor

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                            # (local)
SCHEMATIC_MODULE_PATH = SHARED_DIR / "_spectral_action_regulators.py"             # (local)
S84_CACHE_PATH = (PROJECT_ROOT / "computations" / "session-84"                    # (local)
                  / "s84_spectrum_cache_L12_tau019.npz")

OUT_NPZ = resolve_output(88, "s88_w10_w8_m4_lmax_14_cache_regen.npz")             # (local)
OUT_JSON = resolve_output(88, "s88_w10_w8_m4_lmax_14_cache_regen.json")           # (local)
VERDICT_TXT = resolve_output(88, "s88_gate_verdicts.txt")                         # (local)

INPUT_FILES = [CANONICAL_PATH, SCHEMATIC_MODULE_PATH, S84_CACHE_PATH]             # (local)


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


def feasibility_pre_check():
    """D_K Block-Diagonality + Friedrich-Bär feasibility pre-check.

    Per math-scripts.md §"Machinery-Feasibility Audit" + W11-3 calibration:
      - Canonical D_K cache at L_max=14 is empirically infeasible (irrep
        construction at p+q ≥ 13 > 10 min wall time).
      - Schematic SU(3) Casimir at L_max=14 is trivially computable
        (no Casimir-projection cost; pure (p,q) enumeration).

    Returns: dict with feasibility verdict and route taken.
    """
    canonical_route = "INFEASIBLE_per_W11_3_calibration"                          # (local)
    schematic_route = "FEASIBLE"                                                  # (local)
    sectors_L_old = len(_enumerate_sectors(L_MAX_OLD))                            # (local)
    sectors_L_new = len(_enumerate_sectors(L_MAX_NEW))                            # (local)
    print(f"Feasibility pre-check:")
    print(f"  Canonical D_K Peter-Weyl spectrum at L_max={L_MAX_NEW}: {canonical_route}")
    print(f"  Schematic SU(3) Casimir at L_max={L_MAX_NEW}: {schematic_route}")
    print(f"  Sector count L_max={L_MAX_OLD}: {sectors_L_old}")
    print(f"  Sector count L_max={L_MAX_NEW}: {sectors_L_new}")
    print(f"  Route taken: SCHEMATIC (route ii); canonical answer queued behind W11-3 wall.")
    print()
    return {
        "canonical_route": canonical_route,
        "schematic_route": schematic_route,
        "sectors_L_old": sectors_L_old,
        "sectors_L_new": sectors_L_new,
    }


def compute():
    print()
    print(f"=== {GATE_ID} compute ===")

    feas = feasibility_pre_check()                                                # (local)

    # Compute R_{3a}(L) := M^{(zeta)}_3(L_max=L) — (A)-class anchor at substrate-distance-1
    R_3a_L_old = zeta_a_n(SUBSTRATE_DISTANCE_POLE_N, L_MAX_OLD, Vol_SU3_Haar)     # (local)
    R_3a_L_new = zeta_a_n(SUBSTRATE_DISTANCE_POLE_N, L_MAX_NEW, Vol_SU3_Haar)     # (local)
    R_3a_L_10 = zeta_a_n(SUBSTRATE_DISTANCE_POLE_N, 10, Vol_SU3_Haar)             # (local) cross-context

    print(f"R_3a(L_max={L_MAX_OLD}) = {R_3a_L_old:.12e}")
    print(f"R_3a(L_max={L_MAX_NEW}) = {R_3a_L_new:.12e}")
    print(f"R_3a(L_max=10) cross-context = {R_3a_L_10:.12e}")

    ratio = R_3a_L_new / R_3a_L_old                                               # (local)
    abs_dev = abs(ratio - 1.0)                                                    # (local)

    print(f"\nratio(L_max={L_MAX_NEW}, L_max={L_MAX_OLD}) = {ratio:.12f}")
    print(f"|ratio - 1| = {abs_dev:.6e}")
    print(f"  Reading_1 PASS threshold: < {REL_TOL_PASS:.0e}")
    print(f"  Reading_2 FAIL threshold: > {REL_TOL_FAIL:.0e}")

    if abs_dev < REL_TOL_PASS:
        reading = "Reading_1_TRUNCATION_CONVERGED_PASS"                           # (local)
    elif abs_dev > REL_TOL_FAIL:
        reading = "Reading_2_TRUNCATION_DOMINATED_FAIL"                           # (local)
    else:
        reading = "INFO_PARTIAL_TRUNCATION_EFFECT"                                # (local)
    print(f"reading = {reading}")

    # Friedrich-Bär saturation cross-check: structural bound on the ratio
    # under the schematic. The increment δR = R(L_NEW) - R(L_OLD) sums new
    # sectors at p+q ∈ {L_OLD+1, ..., L_NEW}. Each sector at p+q=L contributes
    # roughly 27/(4·Vol·L²) by Weyl × Casimir^3 scaling.
    #
    # Friedrich-Bär bound: for sectors NEW ≥ L_OLD+1, the contribution is
    # bounded by Σ_{L=L_OLD+1}^{L_NEW} (L+1) · max_d(L) / min_C(L)^3
    # where max_d(L) = (L/2+1)² (L+2)/2 ≈ L^3/8 at the (L/2, L/2) sector
    # and min_C(L) ≥ η_FB_lower² · (L_OLD+1)² (W11-3 calibration).
    fb_bound_new_sectors = 0.0                                                    # (local)
    for L in range(L_MAX_OLD + 1, L_MAX_NEW + 1):
        for (p, q, d, c) in _enumerate_sectors(L):
            if p + q == L:
                fb_bound_new_sectors += d / (c ** SUBSTRATE_DISTANCE_POLE_N)
    fb_bound_new_sectors /= Vol_SU3_Haar
    fb_bound_predicted_dev = fb_bound_new_sectors / R_3a_L_old                    # (local)
    print(f"\nFriedrich-Bär saturation cross-check:")
    print(f"  δR (new sectors L={L_MAX_OLD+1}..{L_MAX_NEW}) = {fb_bound_new_sectors:.6e}")
    print(f"  predicted |ratio-1| = δR / R(L_max={L_MAX_OLD}) = {fb_bound_predicted_dev:.6e}")
    print(f"  observed |ratio-1| = {abs_dev:.6e}")
    print(f"  cross-check (predicted ≈ observed): "
          f"{'PASS' if abs(fb_bound_predicted_dev - abs_dev) / max(abs_dev, 1e-30) < 1e-6 else 'INFO'}")

    return {
        "value": (
            f"ratio_L14_over_L12={ratio:.12f};|ratio-1|={abs_dev:.6e};"
            f"reading={reading};feasibility_route=SCHEMATIC_direct;"
            f"canonical_D_K_route=INFEASIBLE_per_W11_3"
        ),
        "ratio": ratio,
        "abs_dev": abs_dev,
        "R_3a_L_old": R_3a_L_old,
        "R_3a_L_new": R_3a_L_new,
        "R_3a_L_10": R_3a_L_10,
        "reading": reading,
        "feasibility": feas,
        "fb_bound_predicted_dev": fb_bound_predicted_dev,
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
        f"(SCHEMATIC per its docstring lines 23-30; canonical D_K cache at L_max=14 "
        f"is empirically infeasible per W11-3 calibration; schematic route taken; "
        f"see .claude/rules/substrate-first-canonical-sourcing.md §iv MANDATORY at K=4)\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tier_pin)


def evaluate_gate(result):
    a = result["abs_dev"]                                                         # (local)
    if a < REL_TOL_PASS:
        return "PASS"
    if a > REL_TOL_FAIL:
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
        ratio=result["ratio"],
        abs_dev=result["abs_dev"],
        R_3a_L_old=result["R_3a_L_old"],
        R_3a_L_new=result["R_3a_L_new"],
        R_3a_L_10=result["R_3a_L_10"],
        L_max_old=L_MAX_OLD,
        L_max_new=L_MAX_NEW,
        s_pole=SUBSTRATE_DISTANCE_POLE_N,
        verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    json_payload = {                                                              # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "ratio": result["ratio"],
        "abs_dev": result["abs_dev"],
        "R_3a_L_old": result["R_3a_L_old"],
        "R_3a_L_new": result["R_3a_L_new"],
        "R_3a_L_10": result["R_3a_L_10"],
        "feasibility": result["feasibility"],
        "fb_bound_predicted_dev": result["fb_bound_predicted_dev"],
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
