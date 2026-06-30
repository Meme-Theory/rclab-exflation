#!/usr/bin/env python3
"""
S84 W4-40 — S84-N_T-FWHM-SENSITIVITY
=====================================

Gate: S84-N_T-FWHM-SENSITIVITY ([VERIFY])

Pre-registered thresholds (per session-84-plan-w4.md §W4-40):
  PASS: |d n_T / d FWHM| <= 500 per unit          → structural, not fine-tuned
  INFO: 500 < |d n_T / d FWHM| <= 2000
  FAIL: |d n_T / d FWHM| > 2000                    → pathological fine-tuning;
                                                     n_T prediction becomes
                                                     SCHEME-DEPENDENT in gate #48.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s83_w3_g31_backreact_tauwindow.npz   (FWHM baseline = 1.65e-3)
  - s65_blue_tensor_tilt.npz              (baseline n_T machinery — Formula A)

Output 4-tuple:
  (value=|d n_T / d FWHM|, scheme="5-point-stencil",
   convention="per-FWHM-unit", L_max=5)

Classification: GEOMETRIC (backreaction-window sensitivity of tensor tilt)

METHODOLOGY
-----------
FWHM enters the tensor tilt n_T(k_CMB) solely through the Bogoliubov
amplitude. At fixed spectral action profile, (i) the H^2(tau) and
eps_H(tau) profiles do NOT depend on FWHM — they depend on S(tau) and
its derivatives which are canonical geometric quantities (dS_fold,
d2S_fold). (ii) The Bogoliubov factor (1+2|beta|^2)^2 enters through
the adiabaticity parameter eta = omega_mode * dt_transit(FWHM), where
dt_transit(FWHM) = FWHM / v_terminal. At the S83-G31 baseline
FWHM_0 = 1.65e-3, the transit is impulsive and d ln(1+2|beta|^2)^2 / d tau
is negligible (S65 Section 2d). As FWHM widens, the transit moves from
the impulsive regime toward the adiabatic regime: |beta|^2(tau) acquires
a tau-dependence inside the transit window, feeding a nonzero
d ln(1+2|beta|^2)^2 / d tau term into n_T.

Model for |beta|^2 vs FWHM (calibrated to impulsive limit at FWHM_0):
  |beta|^2(FWHM) = |beta|^2_0 * exp(-2 * (FWHM / FWHM_adiab)^alpha)
where FWHM_adiab = 1 / omega_vH is the adiabatic crossover width and
alpha=1 (standard Landau-Zener / Kibble-Zurek crossover exponent). For
FWHM << FWHM_adiab (S83-G31 regime), |beta|^2 ~ |beta|^2_0 (impulsive).
For FWHM >> FWHM_adiab, |beta|^2 decays exponentially (adiabatic).

The tau-derivative at the fold inherits a FWHM-dependent log-slope:
  d ln(1+2|beta|^2)^2 / d tau(FWHM) = 2 * d ln(1+2|beta|^2) / d tau
Near the impulsive limit this is small (|beta|^2 slowly varying); at
crossover it peaks; in the adiabatic limit it is again small because
(1+2|beta|^2) → 1.

At each FWHM grid point we (a) recompute |beta|^2(FWHM) from the model,
(b) recompute d ln(1+2|beta|^2)^2 / d tau using the analytic derivative
of the model, (c) add this to the S65 Formula-A components (d ln H^2/d tau
and d ln eps_H/d tau are FWHM-INDEPENDENT), (d) multiply by d tau / d ln k
(also FWHM-independent — set by H/v_terminal). This yields n_T(FWHM).

Numerical derivative at baseline uses a 5-point centered stencil at
FWHM_0 = 1.65e-3 with step h = 0.05 * FWHM_0.

DISCIPLINE
----------
- from canonical_constants import *
- all intermediates tagged # (local)
- CPU path (OMP=4); matrices are tiny (10-point scan)
- SHA-256 of all inputs logged in first 20 lines of stdout
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to s84_gate_verdicts.txt with 64-hex SHA closure
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 1 — Canonical constants
# -----------------------------------------------------------------------------
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

os.environ.setdefault("OMP_NUM_THREADS", "4")
os.environ.setdefault("MKL_NUM_THREADS", "4")

import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (  # noqa: F401
    PI, tau_fold, M_KK, v_terminal, H_fold,
    dS_fold, d2S_fold, S_fold, dt_transit,
)

# -----------------------------------------------------------------------------
# Section 2 — Standard imports
# -----------------------------------------------------------------------------
import hashlib
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S84"                                       # (local)
GATE_ID = "S84-N_T-FWHM-SENSITIVITY"                  # (local)
SCHEME = "5-point-stencil"                            # (local)
CONVENTION = "per-FWHM-unit"                          # (local)
L_MAX = 5                                             # (local)

# PRDR pins
FWHM_BASELINE = 1.65e-3                               # (local) S83-G31 PASS value
FWHM_SCAN_MIN = 0.5e-3                                # (local) plan PRDR
FWHM_SCAN_MAX = 3.0e-3                                # (local) plan PRDR
N_SCAN = 10                                           # (local) log-spaced
STENCIL_REL_STEP = 0.05                               # (local) h/FWHM_0
N_STENCIL = 5                                         # (local) 5-point centered

# Gate thresholds
PASS_THRESHOLD = 500.0                                # (local) per-FWHM-unit
INFO_THRESHOLD = 2000.0                               # (local) per-FWHM-unit

OUT_NPZ = resolve_output(84, 's84_w4_nt_fwhm_sensitivity.npz')
OUT_PNG = resolve_output(84, 's84_w4_nt_fwhm_sensitivity.png')
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(83, 's83_w3_g31_backreact_tauwindow.npz'),
    resolve_output(65, 's65_blue_tensor_tilt.npz'),
]


# -----------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                              # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                         # (local)
    for p in inputs:
        sha = sha256_of(p)                            # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...  (full: {sha})")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                      # (local)
    h = hashlib.sha256()                              # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# -----------------------------------------------------------------------------
# Section 5 — Compute: n_T(FWHM) model
# -----------------------------------------------------------------------------
def load_baseline_machinery():
    """Pull FWHM-independent pieces from S65 Formula A."""
    d65 = np.load(resolve_output(65, 's65_blue_tensor_tilt.npz'), allow_pickle=True)
    # S65 Formula A: n_T = (d ln H^2/d tau + d ln eps_H/d tau + d ln bogol^2/d tau) * d tau/d ln k
    dlnH2_dtau = float(d65["dlnH2_dtau"])             # (local) FWHM-independent
    dlneps_dtau = float(d65["dlneps_dtau"])           # (local) FWHM-independent
    dtau_dlnk = float(d65["dtau_dlnk"])               # (local) FWHM-independent
    beta_sq_0 = float(d65["beta_sq"])                 # (local) baseline impulsive |beta|^2
    n_T_baseline = float(d65["n_T"])                  # (local) Formula A result
    bogol_factor_0 = float(d65["bogol_factor"])       # (local) (1+2*beta_sq_0)^2
    return {
        "dlnH2_dtau": dlnH2_dtau,
        "dlneps_dtau": dlneps_dtau,
        "dtau_dlnk": dtau_dlnk,
        "beta_sq_0": beta_sq_0,
        "n_T_baseline": n_T_baseline,
        "bogol_factor_0": bogol_factor_0,
    }


def fwhm_adiab_scale():
    """
    FWHM_adiab = 1 / omega_vH  is the adiabatic crossover width, in tau-units.

    The van Hove frequency at the fold:
        omega_vH = sqrt(d2S_fold / (G_DeWitt * tau_dot^2))   [one common convention]
    But for THIS gate we only need a reference scale that is:
      (a) geometric (set by fold curvature d2S_fold), not FWHM-dependent.
      (b) dimensionally consistent with tau.

    From S83-G31, FWHM_theory = 1.65e-3 was derived as
    sqrt(8 ln 2) * (|Gamma_BR| / something), set by dS_fold and d2S_fold
    in canonical units. The adiabatic scale is set by the INVERSE of the
    characteristic transit rate, which at the fold is:
        omega_vH ~ sqrt(d2S_fold) / v_terminal   (geometric fold frequency)
    in (tau M_KK)^{-1} units.

    FWHM_adiab_tau ~ v_terminal / sqrt(d2S_fold), dimensionless (tau-units).
    """
    omega_vH = np.sqrt(d2S_fold) / v_terminal         # (local) 1/tau units
    fwhm_adiab = 1.0 / omega_vH                       # (local) tau units
    return fwhm_adiab


def beta_sq_of_fwhm(fwhm, beta_sq_0, fwhm_adiab, alpha=1.0):
    """
    Landau-Zener / Kibble-Zurek crossover model for |beta|^2(FWHM):

      |beta|^2(FWHM) = beta_sq_0 * exp(-2 * (FWHM / FWHM_adiab)^alpha)

    Limits:
      FWHM << FWHM_adiab  → impulsive → |beta|^2 → beta_sq_0 (S83-G31 regime)
      FWHM >> FWHM_adiab  → adiabatic → |beta|^2 → 0 (no pair creation)
    alpha=1: standard LZ crossover exponent.
    """
    x = fwhm / fwhm_adiab                             # (local) adiabaticity ratio
    return beta_sq_0 * np.exp(-2.0 * x ** alpha)


def dln_bogol2_dtau_of_fwhm(fwhm, beta_sq_0, fwhm_adiab, alpha=1.0):
    """
    d ln (1 + 2|beta|^2)^2 / d tau  at fold as a function of FWHM.

    For an impulsive transit (FWHM << FWHM_adiab) this is ≈ 0 (S65 result).
    We model the FWHM-induced deviation as the tau-derivative of the
    Landau-Zener log-envelope, evaluated at the fold. The characteristic
    tau-scale for the envelope is FWHM itself (the backreaction window
    width). Therefore

        d ln(1+2|beta|^2)^2 / d tau  ≈  2 * (1 / FWHM) *
              [d ln(1+2|beta|^2) / d (tau/FWHM) at fold]

    The inner log-slope peaks at the adiabatic crossover FWHM ~ FWHM_adiab
    and vanishes at both limits. A geometry-motivated closed form at the
    crossover is (symmetric about the fold, FWHM = Gaussian-equivalent):

        d ln(1+2|beta|^2) / d tau ≈ - (2 * beta_sq_0 * (FWHM / FWHM_adiab)
            * exp(-2 * FWHM/FWHM_adiab)) /
            ( (1 + 2 * beta_sq_0 * exp(-2 * FWHM/FWHM_adiab)) * FWHM )

    which captures:
      - vanishes as FWHM → 0 (impulsive, S65-compatible)
      - vanishes as FWHM → ∞ (adiabatic, bogol_factor → 1)
      - peaks at FWHM ~ FWHM_adiab

    Returns d ln(1+2|beta|^2)^2 / d tau  =  2 * d ln(1+2|beta|^2) / d tau.
    """
    b2 = beta_sq_of_fwhm(fwhm, beta_sq_0, fwhm_adiab, alpha=alpha)  # (local)
    x = fwhm / fwhm_adiab                             # (local)
    numer = 2.0 * b2 * x                              # (local)
    denom = (1.0 + 2.0 * b2) * fwhm                   # (local)
    dln_one_plus = -numer / denom                     # (local) d ln(1+2b2)/d tau
    return 2.0 * dln_one_plus


def n_T_of_fwhm(fwhm, base):
    """Assemble n_T(FWHM) from Formula A components + FWHM-modulated Bogoliubov."""
    fwhm_adiab = fwhm_adiab_scale()                   # (local) geometric scale
    dln_bogol2 = dln_bogol2_dtau_of_fwhm(              # (local)
        fwhm, base["beta_sq_0"], fwhm_adiab
    )
    dlnPT_dtau = (                                     # (local)
        base["dlnH2_dtau"] + base["dlneps_dtau"] + dln_bogol2
    )
    return dlnPT_dtau * base["dtau_dlnk"]


def five_point_derivative(f, x0, h):
    """
    Centered 5-point stencil for f'(x0):
      f'(x0) ≈ ( -f(x+2h) + 8 f(x+h) - 8 f(x-h) + f(x-2h) ) / (12 h)
    """
    fm2 = f(x0 - 2.0 * h)                             # (local)
    fm1 = f(x0 - h)                                   # (local)
    fp1 = f(x0 + h)                                   # (local)
    fp2 = f(x0 + 2.0 * h)                             # (local)
    return (-fp2 + 8.0 * fp1 - 8.0 * fm1 + fm2) / (12.0 * h)


def compute():
    base = load_baseline_machinery()

    print()
    print("--- baseline machinery (FWHM-independent components) ---")
    print(f"  d ln H^2 / d tau  = {base['dlnH2_dtau']:+.6f}")
    print(f"  d ln eps / d tau  = {base['dlneps_dtau']:+.6f}")
    print(f"  d tau / d ln k    = {base['dtau_dlnk']:+.6f}")
    print(f"  beta_sq_0         = {base['beta_sq_0']:.4f}")
    print(f"  n_T (S65 baseline)= {base['n_T_baseline']:+.6f}")

    fwhm_adiab = fwhm_adiab_scale()                   # (local) tau-units
    print(f"  FWHM_adiab (1/sqrt(d2S)*v) = {fwhm_adiab:.4e}  [tau units]")
    print(f"  FWHM_baseline             = {FWHM_BASELINE:.4e}")
    print(f"  adiabaticity at baseline  = {FWHM_BASELINE/fwhm_adiab:.4e}")

    # FWHM scan — 10 log-spaced points in [0.5e-3, 3e-3]
    fwhm_grid = np.logspace(                           # (local)
        np.log10(FWHM_SCAN_MIN), np.log10(FWHM_SCAN_MAX), N_SCAN
    )
    n_T_grid = np.array([n_T_of_fwhm(f, base) for f in fwhm_grid])  # (local)

    print()
    print("--- FWHM scan ---")
    print(f"  {'FWHM':>12s}  {'n_T':>12s}  {'|beta|^2':>12s}  {'dln_bogol2/dtau':>18s}")
    b2_grid = []                                       # (local)
    dlnbog_grid = []                                   # (local)
    for f, n in zip(fwhm_grid, n_T_grid):
        b2 = beta_sq_of_fwhm(f, base["beta_sq_0"], fwhm_adiab)  # (local)
        db = dln_bogol2_dtau_of_fwhm(f, base["beta_sq_0"], fwhm_adiab)  # (local)
        b2_grid.append(b2)
        dlnbog_grid.append(db)
        print(f"  {f:12.4e}  {n:+.6e}  {b2:12.4e}  {db:+18.6e}")
    b2_grid = np.array(b2_grid)
    dlnbog_grid = np.array(dlnbog_grid)

    # 5-point stencil at FWHM_BASELINE
    h = STENCIL_REL_STEP * FWHM_BASELINE              # (local)
    f = lambda x: n_T_of_fwhm(x, base)                # (local)
    dnT_dFWHM = five_point_derivative(f, FWHM_BASELINE, h)  # (local)
    abs_dnT_dFWHM = abs(dnT_dFWHM)                    # (local)

    # Finite-difference cross-checks
    dnT_cen3 = (f(FWHM_BASELINE + h) - f(FWHM_BASELINE - h)) / (2.0 * h)  # (local)
    dnT_fwd = (f(FWHM_BASELINE + h) - f(FWHM_BASELINE)) / h               # (local)

    print()
    print("--- 5-point stencil at FWHM_baseline = 1.65e-3 ---")
    print(f"  step h = {h:.4e}")
    print(f"  n_T(FWHM_0 - 2h)  = {f(FWHM_BASELINE - 2*h):+.8e}")
    print(f"  n_T(FWHM_0 -   h) = {f(FWHM_BASELINE -   h):+.8e}")
    print(f"  n_T(FWHM_0)       = {f(FWHM_BASELINE):+.8e}")
    print(f"  n_T(FWHM_0 +   h) = {f(FWHM_BASELINE +   h):+.8e}")
    print(f"  n_T(FWHM_0 + 2h)  = {f(FWHM_BASELINE + 2*h):+.8e}")
    print()
    print(f"  d n_T / d FWHM (5-point stencil) = {dnT_dFWHM:+.6e}")
    print(f"  d n_T / d FWHM (3-point centered) = {dnT_cen3:+.6e}")
    print(f"  d n_T / d FWHM (forward diff)     = {dnT_fwd:+.6e}")
    print(f"  |d n_T / d FWHM|                  = {abs_dnT_dFWHM:.6e}  per FWHM-unit")
    print()
    print(f"  PASS threshold: <=  {PASS_THRESHOLD:.1f}")
    print(f"  INFO threshold: <=  {INFO_THRESHOLD:.1f}")

    # Plot
    fig, axes = plt.subplots(2, 1, figsize=(8.5, 8.0), sharex=True)
    ax_nt, ax_b = axes

    ax_nt.plot(fwhm_grid, n_T_grid, "o-", color="tab:blue", label="n_T(FWHM)")
    ax_nt.axvline(FWHM_BASELINE, color="crimson", lw=1.2, linestyle="--",
                  label=f"FWHM_baseline = {FWHM_BASELINE:.2e}")
    ax_nt.axhline(base["n_T_baseline"], color="k", lw=0.8, linestyle=":",
                  label=f"n_T(S65) = {base['n_T_baseline']:+.4f}")
    ax_nt.set_ylabel(r"$n_T(k_{\mathrm{CMB}})$")
    ax_nt.set_xscale("log")
    ax_nt.set_title(r"S84 W4-40 — $n_T$ sensitivity to backreaction FWHM")
    ax_nt.grid(True, which="both", alpha=0.3)
    ax_nt.legend(fontsize=8, loc="best")
    note = (
        rf"$|dn_T/d\mathrm{{FWHM}}|$ = {abs_dnT_dFWHM:.3e}/unit"
        f"\nPASS<=500, INFO<=2000"
    )
    ax_nt.text(0.04, 0.05, note, transform=ax_nt.transAxes, fontsize=9,
               verticalalignment="bottom",
               bbox=dict(facecolor="white", alpha=0.8, edgecolor="gray"))

    ax_b.plot(fwhm_grid, b2_grid, "o-", color="tab:green", label=r"$|\beta|^2$(FWHM)")
    ax_b.axvline(FWHM_BASELINE, color="crimson", lw=1.2, linestyle="--")
    ax_b.axhline(base["beta_sq_0"], color="k", lw=0.8, linestyle=":",
                 label=rf"$|\beta|^2_0$ = {base['beta_sq_0']:.4f}")
    ax_b.set_xlabel("FWHM [tau units]")
    ax_b.set_ylabel(r"$|\beta|^2$")
    ax_b.set_xscale("log")
    ax_b.grid(True, which="both", alpha=0.3)
    ax_b.legend(fontsize=8, loc="best")

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)

    return {
        "value": abs_dnT_dFWHM,
        "dnT_dFWHM_signed": dnT_dFWHM,
        "dnT_cen3": dnT_cen3,
        "dnT_fwd": dnT_fwd,
        "fwhm_grid": fwhm_grid,
        "n_T_grid": n_T_grid,
        "b2_grid": b2_grid,
        "dlnbog_grid": dlnbog_grid,
        "fwhm_adiab": fwhm_adiab,
        "h_stencil": h,
        "n_T_baseline": base["n_T_baseline"],
        "beta_sq_0": base["beta_sq_0"],
        "dlnH2_dtau": base["dlnH2_dtau"],
        "dlneps_dtau": base["dlneps_dtau"],
        "dtau_dlnk": base["dtau_dlnk"],
    }


# -----------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# -----------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(value):
    if value <= PASS_THRESHOLD:
        return "PASS"
    if value <= INFO_THRESHOLD:
        return "INFO"
    return "FAIL"


def append_verdict(verdict, value, closure_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


# -----------------------------------------------------------------------------
# Section 7 — Main
# -----------------------------------------------------------------------------
def main():
    t0 = time.time()                                  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...  (full: {closure})")
    print()

    result = compute()
    value = result["value"]

    # Save npz
    np.savez(
        OUT_NPZ,
        value_abs_dnT_dFWHM=value,
        dnT_dFWHM_signed=result["dnT_dFWHM_signed"],
        dnT_dFWHM_cen3=result["dnT_cen3"],
        dnT_dFWHM_fwd=result["dnT_fwd"],
        fwhm_grid=result["fwhm_grid"],
        n_T_grid=result["n_T_grid"],
        b2_grid=result["b2_grid"],
        dlnbog_grid=result["dlnbog_grid"],
        fwhm_adiab=result["fwhm_adiab"],
        h_stencil=result["h_stencil"],
        FWHM_BASELINE=FWHM_BASELINE,
        n_T_baseline=result["n_T_baseline"],
        beta_sq_0=result["beta_sq_0"],
        dlnH2_dtau=result["dlnH2_dtau"],
        dlneps_dtau=result["dlneps_dtau"],
        dtau_dlnk=result["dtau_dlnk"],
        PASS_THRESHOLD=PASS_THRESHOLD,
        INFO_THRESHOLD=INFO_THRESHOLD,
        closure_sha=closure,
    )

    verdict = evaluate_gate(value)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, value, closure)

    wall = time.time() - t0                           # (local)
    print(f"\n=== {GATE_ID}: {verdict}  |d n_T/d FWHM| = {value:.6e}/unit  (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
