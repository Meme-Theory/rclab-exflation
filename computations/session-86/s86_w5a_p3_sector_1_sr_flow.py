#!/usr/bin/env python3
"""
S86 W5a-1 — S86-SECTOR-1-SR-FLOW-Z-FACTOR
==========================================

Gate ID:        S86-SECTOR-1-SR-FLOW-Z-FACTOR  (PIVOT55 + PIVOT312, two verdict lines)
Triggers:       [VERIFY] [SIGN]
Classification: PHONONIC (substrate transit-physics; SR-flow ODE integrates the
                substrate quantum-pressure-factor evolution across e-folds, NOT
                LCDM inflation).

Pre-registered (plan §W5a-1):
  PASS iff |Z_ratio - 1| <= 0.05  (ABSOLUTE 5% on Z_substrate / Z_LCDM)
  INFO iff 0.05 < |Z_ratio - 1| <= 0.10  (band-overshoot diagnostic)
  FAIL iff |Z_ratio - 1| > 0.10  OR  ODE diverges  OR  LSODA-RK45 deviation > 1e-4

§10 substitution-chain analytic pre-registration:
  PIVOT55  expected FAIL  (Z_ratio - 1 ~ 0.22)
  PIVOT312 expected PASS  (Z_ratio - 1 ~ 0.025)

Substrate-framing (mandatory, per phononic-framing.md "IS Space, Not IN Space"):
  We integrate substrate dynamics, NOT LCDM inflation. ξ²(N) is the substrate's
  quantum-pressure factor. The ξ²(0) IC encodes the substrate's spectral state at
  the fold via the s=−1 spectral diagnostic against E-class operators (W4 P4 pin:
  ξ_E_GGE^{-1} = 13.6425). Z(N_pivot) measures how the substrate's quantum-pressure
  normalization evolves across e-folds. The Mukhanov-Sasaki form is borrowed as a
  calculational scaffold; it is NOT an inflaton-as-fundamental-field assertion.

Inputs (S84+ dual-SHA):
  - computations/_shared/canonical_constants.py
  - computations/session-86/s86_w5a_p3_sector_1_sr_flow.py (this file)

Output 4-tuples (one per pivot):
  (value=Z_ratio_at_<pivot>, scheme=SR-LO-Mukhanov-Sasaki,
   convention=substrate-first-xi2(0)-IC, L_max=10)

Author: transit-dynamics-theorist (S86 W5a runtime)
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
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------- Project paths -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SCRIPT_DIR))

# Canonical constants (HARD: xi_E_GGE_inv pinned by W4 P4)
from canonical_constants import (  # noqa: E402
    tau_fold,
    xi_E_GGE_inv,
    M_Pl_reduced,
    n_s_framework,
)

# ----------------------------- Gate identity -----------------------------

SESSION = "S86"
GATE_ID_BASE = "S86-SECTOR-1-SR-FLOW-Z-FACTOR"
SCHEME = "SR-LO-Mukhanov-Sasaki"
CONVENTION = "substrate-first-xi2(0)-IC"
L_MAX = 10                  # (local) plan §0.10 canonical for substrate spectra

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
SCRIPT_PATH = Path(__file__).resolve()
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')
NPZ_PATH = resolve_output(86, 's86_w5a_p3_sector_1_z_factor.npz')
PNG_PATH = resolve_output(86, 's86_w5a_p3_sector_1_z_factor.png')
JSON_PATH = resolve_output(86, 's86_w5a_p3_sector_1_z_factor.json')

# ----------------------------- Pre-registered IC + machinery pins -----------------------------
# Plan §0.10 PRDR machinery-enumeration table (D_PRU_raw = 0; every free param pinned)

EPS_0 = 0.020              # (local) S85 W1a-1 baseline anchor; canonical_constants if registered
ETA_0 = 0.005              # (local) canonical small-η; documented in MS literature (Mukhanov 2005 §8.1)
ALPHA_S_0 = 0.0            # (local) SR-LO IC (α_s sourced dynamically)
XI2_0_SUB = float(xi_E_GGE_inv)   # (local) SUBSTRATE-FIRST IC = xi_E_GGE^{-1} (W4 P4 pin)
XI2_0_LCDM = 0.0           # (local) LCDM-baseline reference IC

N_SPAN = (0.0, 60.0)       # (local) covers both pivots (3.12 and 55) plus margin
N_EVAL_COUNT = 6001        # (local) 0.01 e-fold resolution × 60 e-folds + 1
N_EVAL = np.linspace(N_SPAN[0], N_SPAN[1], N_EVAL_COUNT)

RTOL = 1.0e-8              # (local) plan §0.10 tolerance pin
ATOL = 1.0e-10             # (local) plan §0.10 tolerance pin
MAX_STEP = 0.01            # (local) e-folds; plan §0.10 max_step pin

PIVOTS = {
    "MS_canonical": 55.0,
    "substrate_native_zeta": 3.12,
}  # (local)

PASS_BAND_ABS = 0.05       # (local) plan §0.10 PASS band
INFO_BAND_ABS = 0.10       # (local) plan §0.10 INFO band
LSODA_RK45_REL_TOL = 1.0e-4  # (local) plan §0.10 numerical-method robustness


# ----------------------------- SHA helpers -----------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID_BASE} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        if sha:
            print(f"  {rel}: {sha[:16]}...")
        else:
            print(f"  {rel}: ABSENT")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    machinery_pin_map: dict,
) -> tuple[str, str]:
    """audit_sha256 = SHA(script + canonical + sorted-pins-json + machinery-json)
    content_sha256 = SHA(script_only)"""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    machinery_json = json.dumps(
        machinery_pin_map, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(machinery_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict_line(
    gate_id: str,
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> None:
    """W9a-99 dual-SHA schema + 16-hex companion comment row."""
    line = (
        f"{gate_id}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ----------------------------- The four-component coupled ODE (SR-LO) -----------------------------
# Refs: Mukhanov 2005 §8.1, Sasaki 1986 (MS), gen-physicist 9A §4.5a, mack 9A §VI.3
#
# Substrate dynamics (NOT LCDM inflation):
#   d ε / dN  = ε (2 η - 4 ε + 2 ξ²)            — SR-LO ε-flow with substrate ξ² source
#   d η / dN  = -ε η + α_s + (η - ε) η          — SR-LO η-flow
#   d α_s / dN = -2 ε α_s + 2 η α_s             — SR-LO α_s-flow (truncated)
#   d ξ² / dN = -2 ε ξ²                         — substrate-source closure at SR-LO
#
# ξ²(N) is the substrate's quantum-pressure factor in the MS equation
#   v_k'' + (k² − z''/z + ξ² k²/(aH)²) v_k = 0
# with substrate-first IC ξ²(0) = ξ_E_GGE^{-1} (W4 P4 pin) sourcing the SECTOR-1 anchor.

def rhs(N: float, y: np.ndarray) -> list[float]:
    eps, eta, alpha_s, xi2 = y
    deps_dN = eps * (2.0 * eta - 4.0 * eps + 2.0 * xi2)
    deta_dN = -eps * eta + alpha_s + (eta - eps) * eta
    dalpha_s_dN = -2.0 * eps * alpha_s + 2.0 * eta * alpha_s
    dxi2_dN = -2.0 * eps * xi2
    return [deps_dN, deta_dN, dalpha_s_dN, dxi2_dN]


# ----------------------------- Z-factor -----------------------------
# z(N, k) = a(N) · sqrt(2·ε(N)) · M_Pl_eff(k)        [Mukhanov 2005 §8.1]
# Z(N_pivot) ≡ z(N_pivot, k_pivot) / z(0, k_pivot)
#            = (a_pivot/a_0) · sqrt(ε_pivot/ε_0)     [k cancels at SR-LO]
#            = exp(N_pivot) · sqrt(ε(N_pivot) / ε_0)

def Z_factor(sol, N_pivot: float, eps_0: float) -> float:
    idx = int(np.argmin(np.abs(sol.t - N_pivot)))  # (local)
    eps_pivot = float(sol.y[0, idx])  # (local)
    if eps_pivot <= 0.0 or not np.isfinite(eps_pivot):
        return float("nan")
    a_ratio = float(np.exp(N_pivot))  # (local) a(N)/a(0) = exp(N)
    return a_ratio * np.sqrt(eps_pivot / eps_0)


# ----------------------------- Verdict logic -----------------------------

def classify(z_ratio_val: float, lsoda_rk45_dev: float, ode_diverged: bool) -> str:
    """Plan §9 classifier."""
    if ode_diverged:
        return "FAIL"
    if not np.isfinite(z_ratio_val):
        return "FAIL"
    if lsoda_rk45_dev > LSODA_RK45_REL_TOL:
        return "FAIL"
    dev = abs(z_ratio_val - 1.0)  # (local)
    if dev <= PASS_BAND_ABS:
        return "PASS"
    elif dev <= INFO_BAND_ABS:
        return "INFO"
    else:
        return "FAIL"


# ----------------------------- Main -----------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # Banner
    print(f"=== {GATE_ID_BASE} — runtime ===")
    print(f"  session: {SESSION}")
    print(f"  scheme: {SCHEME}")
    print(f"  convention: {CONVENTION}")
    print(f"  L_max: {L_MAX}")
    print()

    # Input pins (first 20 lines per gate-verdicts.md §"During computation")
    pins = log_input_pins([CANONICAL_PATH, SCRIPT_PATH])
    print()

    # Constants pin echo
    print(f"=== Canonical constants used (W4 P4 pin: xi_E_GGE_inv) ===")
    print(f"  tau_fold       = {tau_fold!r}")
    print(f"  xi_E_GGE_inv   = {xi_E_GGE_inv!r}    (W4 P4; substrate-first IC)")
    print(f"  M_Pl_reduced   = {M_Pl_reduced!r} GeV")
    print(f"  n_s_framework  = {n_s_framework!r}")
    print()

    # IC echo
    print(f"=== IC at N=0 (fold) ===")
    print(f"  eps_0          = {EPS_0}")
    print(f"  eta_0          = {ETA_0}")
    print(f"  alpha_s_0      = {ALPHA_S_0}")
    print(f"  xi2_0 (substrate-first) = {XI2_0_SUB}    (= xi_E_GGE_inv)")
    print(f"  xi2_0 (LCDM-baseline)   = {XI2_0_LCDM}")
    print()

    # ----------------------------- Integrate (substrate, LCDM, RK45 cross-check) -----------------------------
    print(f"=== ODE integration: LSODA primary + RK45 cross-check ===")

    sol_sub = solve_ivp(
        rhs, N_SPAN,
        [EPS_0, ETA_0, ALPHA_S_0, XI2_0_SUB],
        method="LSODA", rtol=RTOL, atol=ATOL, max_step=MAX_STEP,
        t_eval=N_EVAL,
    )
    print(f"  substrate (LSODA): success={sol_sub.success}, message={sol_sub.message}")

    sol_lcdm = solve_ivp(
        rhs, N_SPAN,
        [EPS_0, ETA_0, ALPHA_S_0, XI2_0_LCDM],
        method="LSODA", rtol=RTOL, atol=ATOL, max_step=MAX_STEP,
        t_eval=N_EVAL,
    )
    print(f"  LCDM      (LSODA): success={sol_lcdm.success}, message={sol_lcdm.message}")

    sol_sub_RK45 = solve_ivp(
        rhs, N_SPAN,
        [EPS_0, ETA_0, ALPHA_S_0, XI2_0_SUB],
        method="RK45", rtol=RTOL, atol=ATOL, max_step=MAX_STEP,
        t_eval=N_EVAL,
    )
    print(f"  substrate  (RK45): success={sol_sub_RK45.success}, message={sol_sub_RK45.message}")
    print()

    # Diagnose ODE breakdown if any
    eps_sub_traj = sol_sub.y[0, :]  # (local)
    breakdown_idx_arr = np.where((eps_sub_traj > 0.5) | ~np.isfinite(eps_sub_traj))[0]  # (local)
    if breakdown_idx_arr.size > 0:
        N_breakdown = float(sol_sub.t[breakdown_idx_arr[0]])
    else:
        N_breakdown = float(N_SPAN[1])
    print(f"  N_breakdown (substrate ε > 0.5 or non-finite) = {N_breakdown:.4f}")
    print()

    # ----------------------------- CC1: IC fidelity at N=0 -----------------------------
    cc1_eps_dev = abs(float(sol_sub.y[0, 0]) - EPS_0)  # (local)
    cc1_xi2_dev = abs(float(sol_sub.y[3, 0]) - XI2_0_SUB)  # (local)
    cc1_PASS = (cc1_eps_dev < 1e-12) and (cc1_xi2_dev < 1e-12)  # (local)
    print(f"  CC1 (IC fidelity at N=0):  ε dev = {cc1_eps_dev:.3e}, "
          f"ξ² dev = {cc1_xi2_dev:.3e}  -> {'PASS' if cc1_PASS else 'FAIL'}")

    # ----------------------------- CC2: ε(N) monotone-non-decreasing on [0, min(55, N_breakdown)] -----------------------------
    mask = sol_sub.t <= min(55.0, N_breakdown)  # (local)
    eps_traj_window = eps_sub_traj[mask]  # (local)
    diffs = np.diff(eps_traj_window)  # (local)
    cc2_min_diff = float(np.min(diffs)) if diffs.size > 0 else 0.0  # (local)
    cc2_PASS = bool(np.all(diffs >= -1e-9))  # (local)
    print(f"  CC2 (ε monotone on [0, min(55,N_breakdown)]): min diff = {cc2_min_diff:.3e}  "
          f"-> {'PASS' if cc2_PASS else 'FAIL'}")

    # ----------------------------- Compute Z(N_pivot) at both pivots, both ICs -----------------------------
    print()
    print(f"=== Z(N_pivot) computation ===")

    z_results: dict[str, dict] = {}  # (local)
    for name, N_pivot in PIVOTS.items():
        Z_sub_lsoda = Z_factor(sol_sub, N_pivot, EPS_0)  # (local)
        Z_lcdm_lsoda = Z_factor(sol_lcdm, N_pivot, EPS_0)  # (local)
        Z_sub_rk45 = Z_factor(sol_sub_RK45, N_pivot, EPS_0)  # (local)

        if Z_lcdm_lsoda > 0 and np.isfinite(Z_lcdm_lsoda) and np.isfinite(Z_sub_lsoda):
            z_ratio = Z_sub_lsoda / Z_lcdm_lsoda  # (local)
        else:
            z_ratio = float("nan")

        # LSODA vs RK45 numerical-method robustness on substrate-IC run
        if Z_sub_lsoda > 0 and np.isfinite(Z_sub_lsoda) and np.isfinite(Z_sub_rk45):
            lsoda_rk45_rel_dev = abs(Z_sub_lsoda - Z_sub_rk45) / abs(Z_sub_lsoda)  # (local)
        else:
            lsoda_rk45_rel_dev = float("inf")

        ode_diverged = (
            (not sol_sub.success) or (not sol_lcdm.success)
            or (not np.isfinite(Z_sub_lsoda)) or (not np.isfinite(Z_lcdm_lsoda))
        )  # (local)

        verdict_class = classify(z_ratio, lsoda_rk45_rel_dev, ode_diverged)  # (local)

        z_results[name] = {
            "N_pivot": N_pivot,
            "Z_substrate_LSODA": Z_sub_lsoda,
            "Z_LCDM_LSODA": Z_lcdm_lsoda,
            "Z_substrate_RK45": Z_sub_rk45,
            "Z_ratio": z_ratio,
            "lsoda_rk45_rel_dev": lsoda_rk45_rel_dev,
            "verdict": verdict_class,
            "abs_dev_from_unity": abs(z_ratio - 1.0) if np.isfinite(z_ratio) else float("nan"),
        }

        print(f"  pivot={name}  N={N_pivot}")
        print(f"    Z_substrate (LSODA) = {Z_sub_lsoda:.6e}")
        print(f"    Z_LCDM      (LSODA) = {Z_lcdm_lsoda:.6e}")
        print(f"    Z_substrate (RK45)  = {Z_sub_rk45:.6e}")
        print(f"    Z_ratio             = {z_ratio:.6f}")
        print(f"    |Z_ratio - 1|       = {abs(z_ratio - 1.0):.6f}")
        print(f"    LSODA-RK45 rel dev  = {lsoda_rk45_rel_dev:.3e}")
        print(f"    -> verdict: {verdict_class}")
        print()

    # ----------------------------- CC3: LSODA vs RK45 cross-check (already computed per-pivot) -----------------------------
    cc3_max_dev = max(z_results[k]["lsoda_rk45_rel_dev"] for k in z_results)  # (local)
    cc3_PASS = cc3_max_dev < LSODA_RK45_REL_TOL  # (local)
    print(f"  CC3 (LSODA vs RK45 max rel dev): {cc3_max_dev:.3e}  "
          f"-> {'PASS' if cc3_PASS else 'FAIL'}")
    print()

    # ----------------------------- Numerical substitution chain (mandatory per math-scripts.md §Double-Check Logic) -----------------------------
    print(f"=== Numerical substitution chain (per math-scripts.md §Double-Check Logic) ===")
    print(f"  Definitions:")
    print(f"    Z(N_pivot) = exp(N_pivot) · sqrt(ε(N_pivot)/ε_0)")
    print(f"    Z_ratio    = Z_substrate / Z_LCDM = sqrt(ε_substrate(N_pivot) / ε_LCDM(N_pivot))")
    print(f"  Substitute (PIVOT55):")
    eps_sub_55_idx = int(np.argmin(np.abs(sol_sub.t - 55.0)))  # (local)
    eps_lcdm_55_idx = int(np.argmin(np.abs(sol_lcdm.t - 55.0)))  # (local)
    eps_sub_55 = float(sol_sub.y[0, eps_sub_55_idx])  # (local)
    eps_lcdm_55 = float(sol_lcdm.y[0, eps_lcdm_55_idx])  # (local)
    print(f"    ε_substrate(55) = {eps_sub_55:.6e}")
    print(f"    ε_LCDM     (55) = {eps_lcdm_55:.6e}")
    print(f"    ratio (ε_sub/ε_LCDM) = {eps_sub_55/eps_lcdm_55 if eps_lcdm_55 > 0 else float('nan'):.6f}")
    print(f"    sqrt(ratio)          = {np.sqrt(eps_sub_55/eps_lcdm_55) if eps_lcdm_55 > 0 else float('nan'):.6f}")
    print(f"    -> matches Z_ratio (PIVOT55) = {z_results['MS_canonical']['Z_ratio']:.6f}: "
          f"{'YES' if abs(np.sqrt(eps_sub_55/eps_lcdm_55) - z_results['MS_canonical']['Z_ratio']) < 1e-6 else 'NO'}")

    print(f"  Substitute (PIVOT312):")
    eps_sub_312_idx = int(np.argmin(np.abs(sol_sub.t - 3.12)))  # (local)
    eps_lcdm_312_idx = int(np.argmin(np.abs(sol_lcdm.t - 3.12)))  # (local)
    eps_sub_312 = float(sol_sub.y[0, eps_sub_312_idx])  # (local)
    eps_lcdm_312 = float(sol_lcdm.y[0, eps_lcdm_312_idx])  # (local)
    print(f"    ε_substrate(3.12) = {eps_sub_312:.6e}")
    print(f"    ε_LCDM     (3.12) = {eps_lcdm_312:.6e}")
    print(f"    ratio                = {eps_sub_312/eps_lcdm_312 if eps_lcdm_312 > 0 else float('nan'):.6f}")
    print(f"    sqrt(ratio)          = {np.sqrt(eps_sub_312/eps_lcdm_312) if eps_lcdm_312 > 0 else float('nan'):.6f}")
    print(f"    -> matches Z_ratio (PIVOT312) = {z_results['substrate_native_zeta']['Z_ratio']:.6f}: "
          f"{'YES' if abs(np.sqrt(eps_sub_312/eps_lcdm_312) - z_results['substrate_native_zeta']['Z_ratio']) < 1e-6 else 'NO'}")
    print()
    print(f"  Direction (read off canonical form):")
    print(f"    Z_ratio = sqrt(ε_substrate / ε_LCDM)")
    print(f"    Z_ratio - 1  > 0  iff  ε_substrate > ε_LCDM  iff  substrate-first IC ENHANCES ε at the pivot")
    print(f"  §10 analytic pre-registration: PIVOT55 ~ 0.22 (FAIL), PIVOT312 ~ 0.025 (PASS)")
    print(f"  Numerical replacement:")
    for name in z_results:
        z_results_dev = z_results[name]["abs_dev_from_unity"]  # (local)
        print(f"    {name}: |Z_ratio - 1| = {z_results_dev:.6f}  -> {z_results[name]['verdict']}")
    print()

    # ----------------------------- Save .npz -----------------------------
    np.savez(
        NPZ_PATH,
        N_eval=N_EVAL,
        eps_substrate=sol_sub.y[0, :],
        eta_substrate=sol_sub.y[1, :],
        alpha_s_substrate=sol_sub.y[2, :],
        xi2_substrate=sol_sub.y[3, :],
        eps_lcdm=sol_lcdm.y[0, :],
        eta_lcdm=sol_lcdm.y[1, :],
        alpha_s_lcdm=sol_lcdm.y[2, :],
        xi2_lcdm=sol_lcdm.y[3, :],
        Z_at_pivots_substrate=np.array(
            [z_results["MS_canonical"]["Z_substrate_LSODA"],
             z_results["substrate_native_zeta"]["Z_substrate_LSODA"]]
        ),
        Z_at_pivots_lcdm=np.array(
            [z_results["MS_canonical"]["Z_LCDM_LSODA"],
             z_results["substrate_native_zeta"]["Z_LCDM_LSODA"]]
        ),
        N_pivots=np.array([55.0, 3.12]),
        eps_0=EPS_0,
        eta_0=ETA_0,
        alpha_s_0=ALPHA_S_0,
        xi2_0_substrate=XI2_0_SUB,
        xi2_0_lcdm=XI2_0_LCDM,
        n_breakdown=N_breakdown,
        cc1_eps_dev=cc1_eps_dev,
        cc1_xi2_dev=cc1_xi2_dev,
        cc2_min_diff=cc2_min_diff,
        cc3_max_dev=cc3_max_dev,
    )
    print(f"  npz: {NPZ_PATH.name}")

    # ----------------------------- Save .png (4-panel ε, η, α_s, ξ² overlay) -----------------------------
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    panels = [
        (axes[0, 0], 0, "ε(N)", "ε"),
        (axes[0, 1], 1, "η(N)", "η"),
        (axes[1, 0], 2, "α_s(N)", "α_s"),
        (axes[1, 1], 3, "ξ²(N)", "ξ²"),
    ]  # (local)
    for ax, idx, title, ylab in panels:
        ax.plot(N_EVAL, sol_sub.y[idx, :], "b-", label="substrate-first IC", lw=1.5)
        ax.plot(N_EVAL, sol_lcdm.y[idx, :], "r--", label="LCDM-baseline IC", lw=1.5)
        ax.axvline(3.12, color="gray", linestyle=":", lw=1.0, label="N=3.12 (substrate ζ)")
        ax.axvline(55.0, color="black", linestyle=":", lw=1.0, label="N=55 (MS canonical)")
        ax.set_xlabel("N (e-folds)")
        ax.set_ylabel(ylab)
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
        ax.legend(loc="best", fontsize=8)
        # Use symlog for ε / ξ² panels which span large ranges
        if idx in (0, 3):
            ax.set_yscale("symlog", linthresh=1e-3)
    fig.suptitle(
        f"S86 W5a-1 SECTOR-1 SR-flow Z-factor: substrate-first vs LCDM-baseline IC\n"
        f"ε_0={EPS_0}, η_0={ETA_0}, α_s,0={ALPHA_S_0}, "
        f"ξ²_0(sub)={XI2_0_SUB:.4f}=xi_E_GGE_inv, ξ²_0(LCDM)=0\n"
        f"Z_ratio(55)={z_results['MS_canonical']['Z_ratio']:.4f}, "
        f"Z_ratio(3.12)={z_results['substrate_native_zeta']['Z_ratio']:.4f}",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=120)
    plt.close(fig)
    print(f"  png: {PNG_PATH.name}")

    # ----------------------------- Save .json (full Z + verdict per pivot) -----------------------------
    diag = {
        "gate_id_base": GATE_ID_BASE,
        "session": SESSION,
        "wave": "W5a",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "machinery_pin_map": {
            "L_max": L_MAX,
            "n_eval": N_EVAL_COUNT,
            "N_span": list(N_SPAN),
            "scheme": SCHEME,
            "convention": CONVENTION,
            "cutoff_axis": "spectral",
            "numerical_method_primary": "LSODA",
            "numerical_method_crosscheck": "RK45",
            "rtol": RTOL,
            "atol": ATOL,
            "max_step": MAX_STEP,
            "GPU_path": "CPU OMP_NUM_THREADS=8",
            "PASS_band_abs": PASS_BAND_ABS,
            "INFO_band_abs": INFO_BAND_ABS,
            "lsoda_rk45_rel_tol": LSODA_RK45_REL_TOL,
            "eps_0": EPS_0,
            "eta_0": ETA_0,
            "alpha_s_0": ALPHA_S_0,
            "xi2_0_substrate": XI2_0_SUB,
            "xi2_0_lcdm": XI2_0_LCDM,
            "xi_E_GGE_inv_used": float(xi_E_GGE_inv),
        },
        "input_pin_map": pins,
        "z_results": z_results,
        "cross_checks": {
            "CC1_IC_fidelity_at_N0": {
                "eps_dev": cc1_eps_dev,
                "xi2_dev": cc1_xi2_dev,
                "PASS": bool(cc1_PASS),
            },
            "CC2_eps_monotone_window": {
                "min_diff": cc2_min_diff,
                "window_upper": float(min(55.0, N_breakdown)),
                "PASS": bool(cc2_PASS),
            },
            "CC3_LSODA_RK45_max_rel_dev": {
                "max_rel_dev": cc3_max_dev,
                "tol": LSODA_RK45_REL_TOL,
                "PASS": bool(cc3_PASS),
            },
        },
        "ODE_breakdown_N": N_breakdown,
        "ODE_success": {
            "substrate_LSODA": bool(sol_sub.success),
            "lcdm_LSODA": bool(sol_lcdm.success),
            "substrate_RK45": bool(sol_sub_RK45.success),
        },
        "analytic_pre_registration": {
            "PIVOT55_expected_dev": 0.22,
            "PIVOT55_expected_verdict": "FAIL",
            "PIVOT312_expected_dev": 0.025,
            "PIVOT312_expected_verdict": "PASS",
            "note": "Plan §10 analytic estimate; numerical verdict above replaces it."
        },
    }  # (local)

    # Compute SHAs (audit + content) — done over the script + canonical + pin/machinery JSON
    audit_sha, content_sha = compute_dual_sha(
        SCRIPT_PATH, CANONICAL_PATH, pins, diag["machinery_pin_map"]
    )
    diag["audit_sha256"] = audit_sha
    diag["content_sha256"] = content_sha

    # Per-pivot dual-SHA — same inputs but appending pivot-name distinguishes the verdict line
    # The audit_sha covers the FULL machinery pin map; both verdicts share it (single script run, single closure).
    JSON_PATH.write_text(json.dumps(diag, indent=2, default=str), encoding="utf-8")
    print(f"  json: {JSON_PATH.name}")
    print()

    # ----------------------------- Emit two verdict lines (one per pivot) -----------------------------
    print(f"=== Emit two verdict lines (PIVOT55, PIVOT312) ===")

    pivot_to_gate = {
        "MS_canonical": f"{GATE_ID_BASE}-PIVOT55",
        "substrate_native_zeta": f"{GATE_ID_BASE}-PIVOT312",
    }  # (local)

    for name, gid in pivot_to_gate.items():
        verdict = z_results[name]["verdict"]  # (local)
        z_ratio_val = z_results[name]["Z_ratio"]  # (local)
        # Per-pivot audit_sha differentiator: append the pivot name to the audit input so each verdict carries
        # a unique audit_sha256 (per dual-SHA uniqueness audit; the closure must distinguish PIVOT55 from PIVOT312).
        h_pivot = hashlib.sha256()
        h_pivot.update(audit_sha.encode("utf-8"))
        h_pivot.update(gid.encode("utf-8"))
        per_pivot_audit = h_pivot.hexdigest()  # (local)
        h_pivot_c = hashlib.sha256()
        h_pivot_c.update(content_sha.encode("utf-8"))
        h_pivot_c.update(gid.encode("utf-8"))
        per_pivot_content = h_pivot_c.hexdigest()  # (local)

        # 4-tuple printout per gate-verdicts.md
        value_str = f"{z_ratio_val:.6f}"  # (local)
        print(
            f"  ({gid})  (value={value_str}, scheme={SCHEME}, "
            f"convention={CONVENTION}, L_max={L_MAX})"
        )
        print(f"    audit_sha256:   {per_pivot_audit[:16]}... (script+canonical+pinmap+machinery+pivot)")
        print(f"    content_sha256: {per_pivot_content[:16]}... (script+pivot)")
        print(f"    verdict:        {verdict}")

        append_verdict_line(gid, verdict, value_str, per_pivot_audit, per_pivot_content)

    # ----------------------------- Self-test summary -----------------------------
    overall_verdicts = {k: z_results[k]["verdict"] for k in z_results}  # (local)
    print()
    print(f"=== Summary ===")
    for k, v in overall_verdicts.items():
        print(f"  {k}: {v}  (Z_ratio={z_results[k]['Z_ratio']:.6f}, "
              f"|Z_ratio-1|={z_results[k]['abs_dev_from_unity']:.6f})")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID_BASE}: complete (wall {wall:.2f}s) ===")
    print(f"  PIVOT55:  {overall_verdicts['MS_canonical']}")
    print(f"  PIVOT312: {overall_verdicts['substrate_native_zeta']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
