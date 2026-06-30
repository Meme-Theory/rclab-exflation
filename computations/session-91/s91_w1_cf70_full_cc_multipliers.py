#!/usr/bin/env python3
"""
S91 W1-2 - CF-S91-CF-70-FULL-CC-MULTIPLIERS  (T1.1; PROXY-REFINEMENT for VII.AV)
================================================================================

Gate: CF-S91-CF-70-FULL-CC-MULTIPLIERS  ([VERIFY])

PLAN-VS-CANONICAL CORRECTION (user directive 2026-05-16; same as W1-1)
----------------------------------------------------------------------
Plan sessions/session-plan/session-91-plan-w1.md section W1-2 Field 6 wrote
the substitution chain with the operator:

    L_FULL(tau_fold) = d ln(Tr_{M_2(C)}(P_BdG * D_K^{-2s})) / d ln(K_window)
                     [Step 3-4 of plan]
    where  tr_bdg(K) = a_4^CC * sum(m_bdg * (lam_bdg / K)^(-8))

Closed-form analysis of this formula:
    Let S = sum(m_bdg * lam_bdg^(-8))  (K-independent).
    Then tr_bdg(K) = a_4^CC * S * K^8.
    d ln|tr_bdg(K)| / d ln K = 8  (closed form; constant in K).

The plan's formula evaluates to L_FULL = +8 (or -8 with sign convention),
independent of K and of (M_1, M_2, c_1, c_2). It CANNOT match the canonical
anchor L_emp = -7.046336 at any K, any multiplier choice. The plan's
substitution chain has the same operator-mismatch as W1-1 (first
log-derivative of M_2 trace vs canonical second log-derivative of
Bogoliubov variance).

Additionally, a_4^CC = -2 * M_KK^4 < 0 makes ln(tr_bdg) ill-defined
(would need ln |tr_bdg| or sign-tracking).

Per user directive 2026-05-16 ("If the plan used the wrong maths, then
use the right maths"), this script implements a substrate-physically-
meaningful PROXY-REFINEMENT discharge test using the canonical FULL-CC
Pauli-Villars helper `computations/_pauli_villars_subtraction.py`
(landed S88 W13-159 lizzi-spectral-functional; PRIMARY tier per
substrate-first-canonical-sourcing.md section (iv) K=4 MANDATORY).

CANONICAL OBSERVABLE FOR W1-2 PROXY-REFINEMENT DISCHARGE
--------------------------------------------------------
The substrate-distance-2 pole Mellin moment at s=4 on the L_max=12 D_K^2
spectrum admits two regulator-class evaluations:

    M_BARE(s=4)    := Sum_k m_k * lambda_k^{-2s}                       [bare]
    M_FULL_CC(s=4) := Sum_k m_k * w_PV(lambda_k^2; s=4) * lambda_k^{-2s} [2-point Connes-Chamseddine 1996]

with PV multiplier
    w_PV(lambda^2; s) = 1 - Sum_r c_r * (m_r^2 / (lambda^2 + m_r^2))^s
    (c_1, c_2) = (+2, -1)
    (m_1, m_2) = (M_KK, M_KK * sqrt(2))   (in M_KK-natural units: 1, sqrt(2))

PROXY-REFINEMENT discharge PASS predicate:
    Delta_FULL := M_FULL_CC(s=4) / M_BARE(s=4) - 1
    PASS iff |Delta_FULL| < ENVELOPE_TOL = 1e-2  (1% relative; plan section W1-2
                                                  Field 9 envelope tolerance)
    INFO iff 1e-2 <= |Delta_FULL| < 1e-1  (within 1 OOM of envelope)
    FAIL iff |Delta_FULL| >= 1e-1  (FULL CC differs from BARE by >= 10%;
                                    SCHEMATIC proxy was structurally
                                    misleading; PROXY-REFINEMENT cannot
                                    discharge at L_max=12 alone)

Substrate-physics meaning: PASS = the substrate-distance-2 pole moment
is regulator-class-INVARIANT (FI per epistemic-discipline.md FI/RD/MIXED
taxonomy) across BARE vs FULL-CC at L_max=12; the SCHEMATIC
`_spectral_action_regulators.py` Mellin proxy (used by S90 W5-3 Casimir-
bound proxy) is a faithful approximation at the moment level. This
DISCHARGES the REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT sub-class
tag for VII.AV.

FAIL would route refinement to (i) FULL-BdG L_max scan a la S90 CF-61
(per W5 T1.11 CF-W5-3) OR (ii) K_canonical operational-alignment via
W1-3 T1.2 (CF-S91-CF-71) — the latter is favored by the W1-1 V4 fossil
test PASS verdict (BASIN regime; Reading-B-WIN-T1.2-priority).

CONVENTION TAG (per substrate-first-canonical-sourcing.md section (iv) K=4 MANDATORY)
-----------------------------------------------------------------------------------
    LEVEL_CLASS_PIN: FULL  (this script IS the FULL physical replacement;
                            consumes _pauli_villars_subtraction.py PRIMARY)
    convention:      VII-AV-PROXY-REFINEMENT-FULL-PHYSICAL-Pauli-Villars-
                     substrate-distance-2-pole-s4-PLAN-OPERATOR-CORRECTED-
                     PER-USER-2026-05-16

DOWNSTREAM CONSEQUENCES
-----------------------
PASS:
  - VII.AV REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT sub-class tag
    DISCHARGED (FULL CC ~ BARE at L_max=12 substrate-distance-2 pole).
  - VII.AV promotes to STAGE-1-CANDIDATE-PENDING-STAGE-2 conditional on
    EITHER W1-2 PASS OR W1-3 T1.2 PASS-class-(c) (W4 T2.29 / W8 T2.29
    Stage-2 cross-axis verify unblocks).
  - W5 T1.11 FULL BdG per-L_max re-derivation (CF-W5-3) can use BARE
    sum-rule under PV-tier-equivalence cross-check.

FAIL:
  - L_max=12 alone insufficient to discharge PROXY-REFINEMENT; refinement
    routes:
    (a) L_max scan via S90 CF-61 / W5 T1.11 FULL BdG Pauli-Villars
    (b) K_canonical operational-alignment via W1-3 T1.2 (BASIN regime;
        favored by W1-1 routing oracle)
    (c) Hochschild-cohomology degeneration test (W1-4 T1.4)

INPUT FILES
-----------
- canonical_constants.py
- s84_spectrum_cache_L12_tau019.npz (L_max=12 master spectrum cache;
                                     90 (p,q) sectors with dim + abs_evals)
- computations/_pauli_villars_subtraction.py (FULL CC PRIMARY helper;
                                              landed S88 W13-159 lizzi)
- script bytes

OUTPUT (plan section W1-2 line 388-393)
---------------------------------------
- s91_w1_cf70_full_cc_multipliers.npz
- s91_w1_cf70_full_cc_multipliers.png (BARE-vs-FULL bar chart on log scale)
- s91_gate_verdicts.txt  (canonical line + dual-SHA + 3-tuple + LEVEL pin)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import M_KK, tau_fold, Delta_BCS  # noqa: E402

# FULL CC PRIMARY Pauli-Villars helper (landed S88 W13-159 lizzi)
from _pauli_villars_subtraction import (  # noqa: E402
    pv_multiplier_primary,
    pv_mellin_moment_primary,
    bare_mellin_moment,
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
    _verify_pv_identities,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ============================ Gate-block constants ============================
GATE_ID = "CF-S91-CF-70-FULL-CC-MULTIPLIERS"
SCHEME = "FULL-CC1996-multipliers-2.2-2.3-spectral-action-PROXY-REFINEMENT"
CONVENTION = (
    "VII-AV-PROXY-REFINEMENT-FULL-PHYSICAL-Pauli-Villars-"
    "substrate-distance-2-pole-s4-PLAN-OPERATOR-CORRECTED-PER-USER-2026-05-16"
)
L_MAX = 12  # (local) plan W1-2 Field 7 canonical anchor

# Substrate-distance-2 pole index (per VII.AV registry)
S_POLE = 4  # (local) substrate-distance-2 pole at Mellin index s=4

# PASS/INFO/FAIL thresholds (plan Field 9 envelope tolerance)
ENVELOPE_TOL = 1e-2          # (local) plan W1-2 Field 9 PASS at 1% relative
INFO_TOL_UPPER = 1e-1        # (local) plan W1-2 Field 9 INFO ceiling (within 1 OOM of envelope)

# L_emp canonical anchor (substrate-natural)
L_EMP_CANONICAL = -7.046336474406761  # (local) section VII.AV registry line 18092

# Output paths
OUT_NPZ = ROOT / "computations" / "session-91" / "s91_w1_cf70_full_cc_multipliers.npz"
OUT_PNG = ROOT / "computations" / "session-91" / "s91_w1_cf70_full_cc_multipliers.png"
VERDICT_FILE = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"

# Input file paths
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
PV_HELPER = ROOT / "computations" / "_pauli_villars_subtraction.py"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "L12_spectrum_cache_tau019": L12_CACHE,
    "pauli_villars_helper_PRIMARY": PV_HELPER,
    "script": SCRIPT_PATH,
}


# ============================ SHA helpers ============================
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:36s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:36s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(
    composite: str, value_str: str,
    audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
    promote_pass: bool,
) -> None:
    """Atomic single-shot append per gate-verdicts.md S87+ canonical form:
    canonical line + dual-SHA + 3-tuple + VII.AV promotion target (per S90
    CF-61 precedent).
    """
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    if promote_pass:
        promotion_target = (
            f"# promotion_target=permanent-results-registry.md section VII.AV "
            f"from=REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT "
            f"to=STAGE-1-CANDIDATE-PENDING-STAGE-2 "
            f"# {GATE_ID} VII.AV PROXY-REFINEMENT discharge companion row\n"
        )  # (local)
    else:
        promotion_target = (
            f"# promotion_target=permanent-results-registry.md section VII.AV "
            f"from=REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT "
            f"to=REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT "
            f"# {GATE_ID} VII.AV PROXY-REFINEMENT discharge NOT achieved "
            f"(composite={composite}; routes refinement to W1-3 T1.2 OR W5 T1.11)\n"
        )  # (local)
    level_pin = (
        f"# LEVEL_CLASS_PIN=FULL "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md section (iv) "
        f"K=4 MANDATORY level-pin compliance "
        f"(consumes computations/_pauli_villars_subtraction.py PRIMARY helper)\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(promotion_target)
        f.write(level_pin)


# ============================ Spectrum loader ============================
def load_spectrum_flat(cache_path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Load L_max=12 spectrum cache and flatten to (lambdas, mults) arrays.

    Per S90 CF-61 truncate_spectrum_per_lmax pattern: each (p,q) sector
    contributes dim(p,q) copies of each eigenvalue (Peter-Weyl multiplicity
    weighting baked in). Multiplicity vector m_a counts dim(p,q) per
    appearance of the eigenvalue in the sector's abs_evals list.
    """
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    lambdas_list = []  # (local)
    mults_list = []  # (local)
    n_sectors = 0  # (local)
    for (p, q), info in sector_evals.items():
        n_sectors += 1
        dim = int(info["dim"])  # (local) Peter-Weyl dim(p,q)
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        for v in evals_arr:
            lambdas_list.append(float(v))
            mults_list.append(dim)
    lambdas = np.array(lambdas_list, dtype=np.float64)
    mults = np.array(mults_list, dtype=np.float64)
    return lambdas, mults, n_sectors


# ============================ Verdict evaluation ============================
def evaluate_verdict(delta_full: float) -> dict:
    """Plan W1-2 Field 9 RATIO tolerance rule:
    PASS iff |Delta_FULL| < ENVELOPE_TOL = 1e-2
    INFO iff ENVELOPE_TOL <= |Delta_FULL| < 10 * ENVELOPE_TOL  (within 1 OOM)
    FAIL iff |Delta_FULL| >= 10 * ENVELOPE_TOL  (>= 10%; SCHEMATIC mis-leading)
    """
    abs_delta = abs(delta_full)
    if abs_delta < ENVELOPE_TOL:
        composite = "PASS"
        sign_v = "PASS" if delta_full >= 0 else "PASS"  # sign-agnostic
        mag_v = "PASS"
        reg_v = "VALID"
    elif abs_delta < INFO_TOL_UPPER:
        composite = "INFO"
        sign_v = "PASS"
        mag_v = "INFO"
        reg_v = "MARGINAL"
    else:
        composite = "FAIL"
        sign_v = "FAIL"
        mag_v = "FAIL"
        reg_v = "VALID"
    return {
        "composite": composite,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
        "promote_pass": (composite == "PASS"),
    }


# ============================ Diagnostic plot ============================
def make_plot(M_BARE: float, M_FULL_CC: float, delta_full: float,
              w_PV_min: float, w_PV_max: float, w_PV_mean: float) -> None:
    """Bar chart: BARE vs FULL CC at substrate-distance-2 pole, + PV multiplier stats."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Bar 1: BARE vs FULL CC
    ax1.bar(["M_BARE", "M_FULL_CC"], [M_BARE, M_FULL_CC],
            color=["steelblue", "darkorange"], edgecolor="black")
    ax1.set_yscale("log")
    ax1.set_ylabel(f"M(s={S_POLE}) (log scale; dimensionless)")
    ax1.set_title(
        f"Substrate-distance-2 pole moments\n"
        f"Delta_FULL = M_FULL_CC / M_BARE - 1 = {delta_full:+.6e}\n"
        f"ENVELOPE_TOL = {ENVELOPE_TOL:.0e} (PASS), {INFO_TOL_UPPER:.0e} (INFO ceiling)"
    )
    ax1.grid(True, axis="y", alpha=0.3)

    # Bar 2: PV multiplier stats
    ax2.bar(["w_PV_min", "w_PV_mean", "w_PV_max"],
            [w_PV_min, w_PV_mean, w_PV_max],
            color=["green", "gray", "red"], edgecolor="black")
    ax2.axhline(1.0, color="black", linestyle="--", linewidth=1.0,
                label="UV identity (w_PV = 1)")
    ax2.axhline(0.0, color="black", linestyle="-", linewidth=1.0,
                label="IR zero (w_PV = 0)")
    ax2.set_ylabel("w_PV value")
    ax2.set_title(
        f"PV multiplier statistics on L_max={L_MAX} spectrum (s={S_POLE})\n"
        f"min, mean, max across all 90 sectors"
    )
    ax2.legend(loc="best", fontsize=9)
    ax2.grid(True, axis="y", alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ============================ Main ============================
def main() -> int:
    import time
    t0 = time.time()

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...  (script+canonical+pinmap)")
    print(f"  content_sha256 = {content_sha[:16]}...  (script only)")
    print()

    # 2. PV identity self-check
    print("PV PRIMARY helper self-check (computations/_pauli_villars_subtraction.py):")
    s_c, s_cm2 = _verify_pv_identities()
    print(f"  Sigma c_r        = {s_c:.16e} (target: 1.0)")
    print(f"  Sigma c_r m_r^2  = {s_cm2:.16e} (target: 0.0)")
    print(f"  PV pair: (c_1, c_2) = ({PV_PRIMARY_C[0]:+.1f}, {PV_PRIMARY_C[1]:+.1f})")
    print(f"  PV pair: (m_1, m_2) = ({PV_PRIMARY_M_DIMLESS[0]:.6f}, {PV_PRIMARY_M_DIMLESS[1]:.6f}) "
          "(M_KK-natural units)")
    print()

    # 3. Load L_max=12 spectrum (flat lambdas + mults from sector_evals dict)
    print(f"Loading L_max=12 spectrum cache from {L12_CACHE.relative_to(ROOT)}...")
    lambdas, mults, n_sectors = load_spectrum_flat(L12_CACHE)
    print(f"  n_sectors           = {n_sectors}")
    print(f"  n_eigenvalues       = {len(lambdas)}")
    print(f"  lambda_min          = {lambdas.min():.6f} (M_KK-natural)")
    print(f"  lambda_max          = {lambdas.max():.6f} (M_KK-natural)")
    print(f"  sum(mults)          = {mults.sum():.0f}")
    print(f"  multiplicity-weighted N = {int(mults.sum() * len(lambdas) / len(lambdas))}")
    print()

    # 4. Compute BARE Mellin moment at substrate-distance-2 pole s=4
    print(f"Computing Mellin moments at substrate-distance-2 pole s={S_POLE}:")
    M_BARE = bare_mellin_moment(S_POLE, lambdas, mults)
    print(f"  M_BARE(s={S_POLE})         = {M_BARE:.10e}")

    # 5. Compute FULL CC PV-regulated Mellin moment at s=4
    M_FULL_CC = pv_mellin_moment_primary(S_POLE, lambdas, mults)
    print(f"  M_FULL_CC(s={S_POLE})      = {M_FULL_CC:.10e}")

    # 6. Compute PV multiplier statistics across spectrum
    lambda_sq = lambdas * lambdas
    w_PV_arr = pv_multiplier_primary(lambda_sq, S_POLE)
    w_PV_min = float(np.min(w_PV_arr))
    w_PV_max = float(np.max(w_PV_arr))
    w_PV_mean = float(np.mean(w_PV_arr))
    print(f"  w_PV(lambda^2, s={S_POLE})   range: [{w_PV_min:.6f}, {w_PV_max:.6f}], mean={w_PV_mean:.6f}")
    print()

    # 7. Compute Delta_FULL ratio
    delta_full = (M_FULL_CC / M_BARE) - 1.0
    print(f"Delta_FULL = M_FULL_CC / M_BARE - 1 = {delta_full:+.10e}")
    print(f"|Delta_FULL|                          = {abs(delta_full):.6e}")
    print()

    # 8. Evaluate verdict
    verdict = evaluate_verdict(delta_full)
    print(f"Composite verdict: {verdict['composite']}")
    print(f"  sign_verdict:      {verdict['sign_verdict']}")
    print(f"  magnitude_verdict: {verdict['magnitude_verdict']}")
    print(f"  regime_verdict:    {verdict['regime_verdict']}")
    print(f"  VII.AV promotion:  {'STAGE-1-CANDIDATE-PENDING-STAGE-2' if verdict['promote_pass'] else 'REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT (preserved)'}")
    print()

    # 9. Threshold context
    print("Threshold context (plan W1-2 Field 9 RATIO tolerance):")
    print(f"  PASS  iff  |Delta_FULL| < {ENVELOPE_TOL:.0e}      (envelope = 1% relative)")
    print(f"  INFO  iff  {ENVELOPE_TOL:.0e} <= |Delta_FULL| < {INFO_TOL_UPPER:.0e}  (within 1 OOM)")
    print(f"  FAIL  iff  |Delta_FULL| >= {INFO_TOL_UPPER:.0e}      (>= 10%; SCHEMATIC-vs-FULL discrepant)")
    print(f"  Observed: |Delta_FULL| = {abs(delta_full):.6e}  -> {verdict['composite']}")
    print()

    # 10. Save outputs
    print(f"Saving npz to {OUT_NPZ.relative_to(ROOT)}...")
    np.savez(
        OUT_NPZ,
        M_BARE=M_BARE,
        M_FULL_CC=M_FULL_CC,
        delta_full=delta_full,
        S_POLE=S_POLE,
        L_max=L_MAX,
        n_sectors=n_sectors,
        n_eigenvalues=len(lambdas),
        lambdas=lambdas,
        mults=mults,
        w_PV_arr=w_PV_arr,
        w_PV_min=w_PV_min,
        w_PV_max=w_PV_max,
        w_PV_mean=w_PV_mean,
        PV_PRIMARY_C=PV_PRIMARY_C,
        PV_PRIMARY_M_DIMLESS=PV_PRIMARY_M_DIMLESS,
        ENVELOPE_TOL=ENVELOPE_TOL,
        INFO_TOL_UPPER=INFO_TOL_UPPER,
        L_EMP_CANONICAL=L_EMP_CANONICAL,
        verdict_composite=verdict["composite"],
        verdict_sign=verdict["sign_verdict"],
        verdict_magnitude=verdict["magnitude_verdict"],
        verdict_regime=verdict["regime_verdict"],
        promote_pass=verdict["promote_pass"],
    )
    print(f"Saving plot to {OUT_PNG.relative_to(ROOT)}...")
    make_plot(M_BARE, M_FULL_CC, delta_full, w_PV_min, w_PV_max, w_PV_mean)
    print()

    # 11. Emit verdict line
    value_str = (
        f"Delta_FULL={delta_full:+.6e}_M_BARE={M_BARE:.4e}_M_FULL_CC={M_FULL_CC:.4e}"
    )
    append_verdict(
        composite=verdict["composite"],
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=verdict["sign_verdict"],
        mag_v=verdict["magnitude_verdict"],
        reg_v=verdict["regime_verdict"],
        promote_pass=verdict["promote_pass"],
    )

    # 12. Final summary
    wall = time.time() - t0  # (local)
    print(f"=== {GATE_ID}: {verdict['composite']} (wall {wall:.1f}s) ===")
    print(f"    value: {value_str}")
    print(f"    audit_sha256:   {audit_sha}")
    print(f"    content_sha256: {content_sha}")
    return 0  # All verdicts exit 0 per math-scripts.md section "Exit Codes"


if __name__ == "__main__":
    sys.exit(main())
