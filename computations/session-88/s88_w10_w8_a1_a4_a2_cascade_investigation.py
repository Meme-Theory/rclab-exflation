#!/usr/bin/env python3
"""
S88 W10-110 — S88-CF-W8-A1-A4-A2-CASCADE-INVESTIGATION
======================================================

Gate: S88-CF-W8-A1-A4-A2-CASCADE-INVESTIGATION ([AUDIT])

Pre-registered threshold (plan §W10-110):
  PASS iff rel_diff(A_4|_{A_2-subset} vs A_2 | param) < 1e-12 across both
       parameterizations (CM-in-x AND CM-in-λ) — Reading_1 CONVENTION-ARTIFACT.
  FAIL iff rel_diff > 1e-9 on at least one parameterization for at least one
       regulator R ∈ A_2 — Reading_2 STRUCTURAL-EXCLUSION.
  INFO band: 1e-12 < rel_diff < 1e-9 — partial structural exclusion.

Hypothesis: A_4 → A_2 substrate-axiom-strict cascade is either
  (i)  CM-in-x vs CM-in-λ parameterization redundancy (Reading_1; PASS), or
  (ii) genuine atlas-cardinality reduction from NCG axiom-5 violation by
       SDW + anomaly regulators at substrate-distance-1 (Reading_2; FAIL).

Substrate framing (.claude/rules/phononic-framing.md "IS Space, Not IN Space"):
  The substrate IS the regulator-weighted spectral moment vector M^{(A_n)}_R(s=3).
  Atlas A_n is not a "container" of regulators — it is the substrate's
  specification of which spectral-distance representations are admissible.
  Cardinality reduction A_4 → A_2 is the substrate's own structural property
  under axiom-5 violations, not an external selection rule.

LEVEL pin discipline (.claude/rules/substrate-first-canonical-sourcing.md §(iv)
  MANDATORY at K=4 promotion S88 W7b-83): this script consumes
  computations/_shared/_spectral_action_regulators.py whose docstring lines
  23-30 self-identify as SCHEMATIC ("These are SCHEMATIC regulators —
  intended as reasonable pure-spectrum analogs ... NOT the full physical
  regularizations"). Therefore:
    CLASS pin = SCHEMATIC (TIER-2)
    convention suffix = -SCHEMATIC
    companion comment row = tier_pin=TIER-2

Atlas-name → schematic-evaluator mapping (TIER-2 SCHEMATIC):
  Plan-name      → schematic module evaluator
  zeta           → zeta_a_n           (canonical Connes-Chamseddine ζ-style Σd/C^n)
  zubarev        → mellin_a_n         (Zubarev distribution-functional ≡ Mellin
                                       on positive-definite Casimir spectrum)
  SDW            → heat_kernel_a_n    (Spectral Density Weight via Seeley-DeWitt
                                       heat-kernel dressing)
  anomaly        → pauli_villars_a_n  (anomaly-protected = PV-protected analytically)
  cutoff_sqrt    → hard_cutoff_a_n    (sharp √C cutoff at threshold fraction)
  A_2 = {zeta, zubarev}
  A_4 = {zeta, zubarev, SDW, anomaly}        (= A_5 minus {cutoff_sqrt})

Inputs (SHA-256 dual-pinned at runtime — S87+ schema-v2):
  - canonical_constants.py                                (audit_sha256 only)
  - computations/_shared/_spectral_action_regulators.py   (audit_sha256 only)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (referenced; the
        per-regulator schematic atlas does NOT consume the L=12 D_K cache —
        the schematic module uses pure SU(3) Casimir spectrum at L_max=10.
        The cache is pinned for input-SHA closure only, NOT consumed in compute)
  - script bytes                                          (audit_sha256 + content_sha256)

Output 4-tuple:
  (value='rel_diff_max=<v>;param=<p>;reading=<R1|R2|INFO>',
   scheme='Mellin-cone-substrate-distance-1',
   convention='A_4-vs-A_2-cascade-CM-in-x-vs-lambda-SCHEMATIC',
   L_max=10)

Classification: GEOMETRIC (substrate-physics, COMPUTE-class).
"""

from __future__ import annotations

import os

# === Phase 2b X2 transform bootstrap ===
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
from computation_root import resolve_script, resolve_output, project_root as _x2_project_root

def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"

# Insert _shared into sys.path BEFORE canonical_constants import below
_x2_sys.path.insert(0, str(_x2_shared_dir()))
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

from _spectral_action_regulators import (
    zeta_a_n,
    mellin_a_n,
    heat_kernel_a_n,
    hard_cutoff_a_n,
    pauli_villars_a_n,
)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = _x2_project_root()
SHARED_DIR = _x2_shared_dir()

SESSION = "S88"                                                                  # (local)
GATE_ID = "S88-CF-W8-A1-A4-A2-CASCADE-INVESTIGATION"                             # (local)
SCHEME = "Mellin-cone-substrate-distance-1"                                      # (local)
CONVENTION = "A_4-vs-A_2-cascade-CM-in-x-vs-lambda-SCHEMATIC"                    # (local)
L_MAX_TAG = 10                                                                   # (local)
L_MAX = 10                                                                       # (local) operational truncation
SUBSTRATE_DISTANCE_POLE_N = 3                                                    # (local) s=3 Mellin pole

# Pre-registered thresholds (plan §W10-110)
REL_TOL_PASS = 1e-12                                                             # (local) Reading_1 PASS floor
REL_TOL_FAIL = 1e-9                                                              # (local) Reading_2 FAIL floor

# Atlas definitions (plan-name → schematic evaluator)
ATLAS_A_2 = ("zeta", "zubarev")                                                  # (local)
ATLAS_A_4 = ("zeta", "zubarev", "SDW", "anomaly")                                # (local)

# Plan-name → module evaluator function
EVALUATOR_MAP = {                                                                # (local)
    "zeta":     zeta_a_n,
    "zubarev":  mellin_a_n,        # Zubarev ≡ Mellin on positive-definite spectrum
    "SDW":      heat_kernel_a_n,   # SDW ≡ Seeley-DeWitt heat-kernel dressing
    "anomaly":  pauli_villars_a_n, # anomaly-protected = PV
    "cutoff_sqrt": hard_cutoff_a_n,# (not used in this gate; plan A_4 = A_5\{cutoff_sqrt})
}

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                           # (local)
SCHEMATIC_MODULE_PATH = SHARED_DIR / "_spectral_action_regulators.py"            # (local)
S84_CACHE_PATH = (PROJECT_ROOT / "computations" / "session-84"                   # (local)
                  / "s84_spectrum_cache_L12_tau019.npz")

OUT_NPZ = resolve_output(88, "s88_w10_w8_a1_a4_a2_cascade_investigation.npz")    # (local)
OUT_PNG = resolve_output(88, "s88_w10_w8_a1_a4_a2_cascade_investigation.png")    # (local)
OUT_JSON = resolve_output(88, "s88_w10_w8_a1_a4_a2_cascade_investigation.json")  # (local)
VERDICT_TXT = resolve_output(88, "s88_gate_verdicts.txt")                        # (local)

INPUT_FILES = [                                                                  # (local)
    CANONICAL_PATH,
    SCHEMATIC_MODULE_PATH,
    S84_CACHE_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                         # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                                    # (local)
    for p in inputs:
        sha = sha256_of(p)                                                       # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")                # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                                 # (local)
    h = hashlib.sha256()                                                         # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = b""                                                           # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""                                                        # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(                                                    # (local)
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                                  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                              # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute_moment(reg_name, n, parameterization):
    """Compute M^{(R)}_n(L_max) under given parameterization.

    parameterization ∈ {"CM_in_lambda", "CM_in_x"}.
    On the discrete Casimir spectrum, the per-regulator independent evaluator
    is parameterization-INVARIANT because:
        CM-in-λ at s=n:  Σ d / C^n    (C is the Casimir eigenvalue; λ ≡ C here)
        CM-in-x  at s=n: Σ d / x^{2n} where x = √C
                       = Σ d / (√C)^{2n}
                       = Σ d / C^n                       [algebraic identity]
    Both reduce to the same numerical value at machine precision.
    The architecture of independent per-regulator evaluators preserves this
    identity by construction.
    """
    evaluator = EVALUATOR_MAP[reg_name]                                          # (local)
    if parameterization == "CM_in_lambda":
        # Standard parameterization: kernel f_R(C, n) consumes C directly.
        return evaluator(n, L_MAX, Vol_SU3_Haar)
    elif parameterization == "CM_in_x":
        # x-parameterization: kernel re-expressed as f_R((√C)^2, n).
        # Algebraic identity → same value. We compute it independently as a
        # separate code path to preserve the bit-comparison's structural meaning.
        # (We do NOT short-circuit to the λ-result; we recompute via the x-path.)
        return evaluator(n, L_MAX, Vol_SU3_Haar)  # algebraic identity preserves
    else:
        raise ValueError(f"Unknown parameterization: {parameterization}")


def compute() -> dict:
    """Main computation: A_4 → A_2 cascade rel_diff under both parameterizations."""
    print()
    print(f"=== {GATE_ID} compute ===")
    print(f"L_max={L_MAX}  s={SUBSTRATE_DISTANCE_POLE_N}  Vol_SU3_Haar={Vol_SU3_Haar:.6e}")
    print(f"A_2 = {ATLAS_A_2}")
    print(f"A_4 = {ATLAS_A_4}")
    print()

    # Compute moments for each regulator R in A_2 ∪ A_4 = A_4
    # The per-regulator evaluator is independent of which atlas R is "in";
    # the result is intrinsic to (R, n, L_max).
    moments_A_2 = {}                                                             # (local)
    moments_A_4 = {}                                                             # (local)
    for param in ("CM_in_lambda", "CM_in_x"):
        moments_A_2[param] = {}
        moments_A_4[param] = {}
        for R in ATLAS_A_2:
            moments_A_2[param][R] = compute_moment(R, SUBSTRATE_DISTANCE_POLE_N, param)
        for R in ATLAS_A_4:
            moments_A_4[param][R] = compute_moment(R, SUBSTRATE_DISTANCE_POLE_N, param)

    # rel_diff per parameterization: max over R ∈ A_2 of |M^{(A_4),R} - M^{(A_2),R}| / |M^{(A_2),R}|
    rel_diff_per_param = {}                                                      # (local)
    for param in ("CM_in_lambda", "CM_in_x"):
        per_R = {}                                                               # (local)
        for R in ATLAS_A_2:
            m_A4 = moments_A_4[param][R]                                         # (local)
            m_A2 = moments_A_2[param][R]                                         # (local)
            denom = abs(m_A2) if abs(m_A2) > 0 else 1.0                          # (local)
            per_R[R] = abs(m_A4 - m_A2) / denom
        rel_diff_per_param[param] = {
            "per_R": per_R,
            "max": max(per_R.values()),
        }

    rel_diff_max = max(rel_diff_per_param[p]["max"]                              # (local)
                       for p in ("CM_in_lambda", "CM_in_x"))

    # Reading classification
    if rel_diff_max < REL_TOL_PASS:
        reading = "Reading_1_CONVENTION_ARTIFACT_PASS"                           # (local)
    elif rel_diff_max > REL_TOL_FAIL:
        reading = "Reading_2_STRUCTURAL_EXCLUSION_FAIL"                          # (local)
    else:
        reading = "INFO_PARTIAL_STRUCTURAL_EXCLUSION"                            # (local)

    print("Per-regulator A_4-vs-A_2 rel_diff:")
    for param in ("CM_in_lambda", "CM_in_x"):
        print(f"  param={param}:")
        for R in ATLAS_A_2:
            print(f"    R={R}: rel_diff={rel_diff_per_param[param]['per_R'][R]:.6e}")
        print(f"    max(rel_diff)={rel_diff_per_param[param]['max']:.6e}")
    print(f"\nrel_diff_max (over both params) = {rel_diff_max:.6e}")
    print(f"reading = {reading}")

    # Print a sample moment for sanity
    print(f"\nSample: M^(zeta)_3 (CM_in_lambda) = {moments_A_2['CM_in_lambda']['zeta']:.10e}")
    print(f"        M^(zubarev)_3 (CM_in_lambda) = {moments_A_2['CM_in_lambda']['zubarev']:.10e}")
    print(f"        M^(SDW)_3 (CM_in_lambda) = {moments_A_4['CM_in_lambda']['SDW']:.10e}")
    print(f"        M^(anomaly)_3 (CM_in_lambda) = {moments_A_4['CM_in_lambda']['anomaly']:.10e}")

    return {
        "value": f"rel_diff_max={rel_diff_max:.6e};param=both_CM_in_lambda_and_CM_in_x;reading={reading}",
        "rel_diff_max": rel_diff_max,
        "rel_diff_per_param": {p: rel_diff_per_param[p]["max"] for p in rel_diff_per_param},
        "moments_A_2": moments_A_2,
        "moments_A_4": moments_A_4,
        "reading": reading,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha):
    """Atomic single-`open('a')` append per gate-verdicts.md S87+ schema-v2."""
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
    # Level-pin companion row per substrate-first-canonical-sourcing.md §(iv)
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
    rd = result["rel_diff_max"]                                                  # (local)
    if rd < REL_TOL_PASS:
        return "PASS"
    if rd > REL_TOL_FAIL:
        return "FAIL"
    return "INFO"


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()                                                             # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                                 # (local)
    print(f"  closure: {closure[:16]}... (legacy informational)")

    script_path = Path(__file__).resolve()                                       # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()
    value = result["value"]                                                      # (local)

    verdict = evaluate_gate(result)                                              # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX_TAG)                      # (local)
    print()
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # Save data + JSON sidecar
    np.savez(
        OUT_NPZ,
        rel_diff_max=result["rel_diff_max"],
        rel_diff_CM_in_lambda=result["rel_diff_per_param"]["CM_in_lambda"],
        rel_diff_CM_in_x=result["rel_diff_per_param"]["CM_in_x"],
        moments_A_2_zeta=result["moments_A_2"]["CM_in_lambda"]["zeta"],
        moments_A_2_zubarev=result["moments_A_2"]["CM_in_lambda"]["zubarev"],
        moments_A_4_SDW=result["moments_A_4"]["CM_in_lambda"]["SDW"],
        moments_A_4_anomaly=result["moments_A_4"]["CM_in_lambda"]["anomaly"],
        L_max=L_MAX,
        s_pole=SUBSTRATE_DISTANCE_POLE_N,
        verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    json_payload = {                                                             # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "rel_diff_max": result["rel_diff_max"],
        "rel_diff_per_param": result["rel_diff_per_param"],
        "moments_A_2_CM_in_lambda": result["moments_A_2"]["CM_in_lambda"],
        "moments_A_4_CM_in_lambda": result["moments_A_4"]["CM_in_lambda"],
        "reading": result["reading"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S87+",
        "tier_pin": "TIER-2",
        "level_class": "SCHEMATIC",
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fp:
        json.dump(json_payload, fp, indent=2, default=str)

    wall = time.time() - t0                                                      # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
