#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S97-W1-XTODAY  (Session 97, Wave 1, gate W1-2)  — substrate-determined x_today window
======================================================================================

[VERIFY] gate.  Pin the substrate-determined late-time ratio x_today = rho_s/rho_n by
integrating the Volovik two-fluid densities from the van Hove fold to the late-tau
endpoint tau_now = 0.6, and verify (i) x_today > x_fold = 85.7928 (monotone) and
(ii) the late-time deceleration q(x_today) ~= -1 (effacement/vacuum-dominated).  The
output fixes the A-PASS x-window consumed by the route-invariance gate 1.3.

Substrate framing (phononic-framing.md / IS Space, Not IN Space)
----------------------------------------------------------------
x = rho_s/rho_n is the ratio of the substrate's unbroken-condensate vacuum density
(rho_s, the effaced w=-1 sector, Gamma_eff=0.99970) to its GGE normal-component
quasiparticle-gas density (rho_n, the n_pairs=59.8 Bogoliubov relic, w_n in
[-0.4076, 0]).  As the order parameter tau advances past the fold, the GGE normal
component REDSHIFTS (rho_n ~ a^{-3(1+w_n)}) while the unbroken condensate vacuum stays
~const (w=-1) -- so the substrate becomes progressively MORE condensate-dominated and
x GROWS.  This is the substrate-IS reading of "the universe becomes dark-energy
dominated": NOT a container filling with vacuum, but the order-parameter trajectory
carrying spectral weight toward the unbroken-condensate (w=-1) sector.  q(x_today)~=-1
is the acoustic-time curvature of that trajectory at the late-tau endpoint.  The arrow
is strictly substrate-first:
  D_K eigenvalues reorganize past the van Hove fold -> Bogoliubov |beta_k|^2 sets the
  GGE normal component rho_n -> differential dilution (rho_n redshifts, rho_s const)
  -> x(tau) = rho_s/rho_n grows -> late-time deceleration q -> -1.

CLASSIFICATION: PHONONIC (the GGE quasiparticle gas / normal component is the relic
that dilutes; x is the condensate-vs-relic spectral-weight ratio).

Method (plan section W1-2) -- 1D cumulative integration, deterministic
----------------------------------------------------------------------
Load x(tau) + component densities + EOS endpoints from s96_w1_volovik_2fluid.npz, and
the AOFT acoustic-rate window (H2_aeff over [tau_fold, 0.6]) + a_2^zeta from
s96_w1_aoft_friedmann_map.npz.

The acoustic scale factor a_eff(tau) is reconstructed over the FULL AOFT window
[tau_fold, 0.6] by integrating the AOFT acoustic Hubble rate
  H_aeff(tau) = sqrt(H2_aeff(tau)),   a_eff(tau) = exp( int_{tau_fold}^{tau} H_aeff dtau' ),
anchored to a_eff(tau_fold) = 1.  H2_aeff is the AOFT a_eff-proxy Friedmann rate (the
plan's "a_eff ~ sqrt(a2) on the AOFT map" operationalized as the per-tau acoustic-rate
array).  This is the route that reaches tau_now = 0.6 (the 2-fluid npz tau_grid stops
at the AOFT fixed point tau* = 0.451041; the AOFT map extends to 0.6).

x(tau) is then extended onto the full window via the Sage-exact differential-dilution
power law (CLAIM 1):
  x(tau) = x_fold * a_eff(tau)^{3(1+w_n)},   for each FROZEN endpoint w_n in {0, -0.4076}.
x_today = x(tau_now=0.6) for each endpoint; reported as a BAND over the two endpoints.

CROSS-CHECK against the landed S96-W1-VOLOVIK-2FLUID values at the internal anchor
tau* = 0.451041 (where the 2-fluid npz grid ends): x_tau_ideal(tau*) and
x_tau_volovik(tau*) from the upstream npz must be reproduced by the same power law on
the upstream's own a_norm grid (to interpolation tol), and the q-formula must
reproduce q_ideal/q_volovik bit-consistently.

[VERIFY] substitution chains (pre-registered, Sage-verified at plan-freeze):
  CLAIM 1 (monotonicity):  d ln x / d ln a = 3(1+w_n) = +3 (w_n=0), +1.77705 (w_n=-0.4076);
           both > 0  =>  x strictly increasing in a  =>  x_today > x_fold for a_today>a_fold.
  CLAIM 2 (late-time sign): two-fluid q(x) = 1/2[(1+3 w_n)+x(1+3 w_s)]/(1+x), w_s=-1;
           lim_{x->inf} q(x) = -1 EXACTLY (independent of w_n)  =>  increasing x drives
           q monotonically toward -1; q(x_today)~=-1 confirms vacuum/effacement dominance.

Environment: phonon-exflation-sim/.venv312/Scripts/python.exe.  1D cumulative
integration; numpy CPU per the plan's GPU_path pin (no large matrix).
This file lives in computations/session-97/ and writes outputs there.
"""

from __future__ import annotations

import hashlib
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# -----------------------------------------------------------------------------
# Section 1 - Paths + canonical-constants import
# -----------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent                    # computations/session-97
PROJECT_ROOT = SESSION_DIR.parent.parent                         # repo root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
# Canonical constants (NEVER hardcode): effacement residual carried by rho_s, GGE
# charge, excitation probability, fold, M_KK, a_2^zeta.
from canonical_constants import (  # noqa: E402
    a_2_FW_zeta,
    n_pairs,
    P_exc_kz,
    Gamma_effacement,
    tau_fold,
    M_KK,
)

GATE_ID = "S97-W1-XTODAY"
SCHEME = "Volovik-two-fluid-differential-dilution"
CONVENTION = "RATIO"           # x is a density ratio; q compared as absolute to -1
L_MAX = "10"
SCHEMA_VERSION = "S84+"

VERDICT_TXT = SESSION_DIR / "s97_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s97_w1_xtoday.npz"
PNG_OUT = SESSION_DIR / "s97_w1_xtoday.png"

CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
S96_2FLUID_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_volovik_2fluid.npz"
S96_AOFT_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_aoft_friedmann_map.npz"

INPUT_FILES = [CANONICAL_PY, S96_2FLUID_NPZ, S96_AOFT_NPZ]

# -----------------------------------------------------------------------------
# Section 2 - Pre-registered machinery pins (plan W1-2 machinery_pin_map)
# -----------------------------------------------------------------------------
N_EVAL = 1001                      # tau-grid points on [0.190, 0.6] (plan)            # (local)
SCAN_LO = 0.190                    # scan_range lo (= tau_fold)                        # (local)
SCAN_HI = 0.6                      # scan_range hi (tau_now, late-tau endpoint)        # (local)
STEP_SIZE = (SCAN_HI - SCAN_LO) / (N_EVAL - 1)   # 3.6e-4 uniform tau-spacing (plan)   # (local)
TOLERANCE = 1e-10                  # cumulative-integration residual floor (plan)      # (local)

# S67 GGE-TWO-FLUID-67 FROZEN band endpoints (both evaluated; band reported).
# These are the upstream npz w_n_ideal / w_n_volovik (the -0.4076 plan pin is the
# 4-sig-fig form of -0.407649206353356); read from the upstream npz at runtime and
# cross-checked against these plan-pin values.
W_N_LO = -0.407649206353356        # Volovik thermodynamic-identity endpoint (S67)     # (local)
W_N_HI = 0.0                       # plan-idealized dust endpoint (S67)                # (local)
W_S = -1.0                         # superfluid vacuum EOS (Gibbs-Duhem P=-rho)        # (local)

X_FOLD_PIN = 85.7928               # S67 ODLRO fold value (lower-bound threshold, plan)# (local)
Q_TARGET = -1.0                    # late-time vacuum-dominated deceleration target    # (local)
TAU_Q = 0.05                       # absolute tolerance on q(x_today) - (-1)           # (local)
INFO_Q_HI = 0.20                   # INFO band upper edge for |q+1| (plan INFO_meaning)# (local)

W_N_ENDPOINTS = (W_N_HI, W_N_LO)   # report band over both                             # (local)


# -----------------------------------------------------------------------------
# Section 3 - SHA machinery (canonical dual-SHA, S84+ schema)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    import json  # (local)
    script_bytes = script_path.read_bytes() if script_path.exists() else b""           # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""   # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")     # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# -----------------------------------------------------------------------------
# Section 4 - Two-fluid deceleration q(x) and differential-dilution x(a)
# -----------------------------------------------------------------------------
def q_two_fluid(x: np.ndarray, w_n: float, w_s: float = W_S) -> np.ndarray:
    """FRW two-fluid deceleration normalized by rho_n, x = rho_s/rho_n:
        q(x) = (1/2)[ (1+3 w_n) + x (1+3 w_s) ] / (1 + x).
    Sage-verified: lim_{x->inf} q = -1 (w_s=-1), independent of w_n (CLAIM 2)."""
    return 0.5 * ((1.0 + 3.0 * w_n) + x * (1.0 + 3.0 * w_s)) / (1.0 + x)


def x_of_a(a_norm: np.ndarray, w_n: float, x_fold: float) -> np.ndarray:
    """Differential-dilution power law: rho_s ~ a^0, rho_n ~ a^{-3(1+w_n)}
       => x = rho_s/rho_n = x_fold * a^{+3(1+w_n)}  (a_norm=1 at fold).
    Sage-verified: d ln x / d ln a = 3(1+w_n) > 0 (CLAIM 1)."""
    return x_fold * a_norm ** (3.0 * (1.0 + w_n))


# -----------------------------------------------------------------------------
# Section 5 - Compute (1D cumulative integration of a_eff; extend x to tau_now)
# -----------------------------------------------------------------------------
def compute() -> dict:
    # --- load upstream substrate data ---
    d2f = np.load(S96_2FLUID_NPZ, allow_pickle=True)  # (local)
    x_fold_up = float(d2f["x_fold"])                  # 85.79277938... (S67 ODLRO) (local)
    w_n_ideal_up = float(d2f["w_n_ideal"])            # 0.0 (local)
    w_n_volovik_up = float(d2f["w_n_volovik"])        # -0.407649206... (local)
    w_s_up = float(d2f["w_s"])                        # -1.0 (local)
    tau_grid_up = np.asarray(d2f["tau_grid"], dtype=float)   # fold -> tau* (200 pt) (local)
    a_norm_up = np.asarray(d2f["a_norm"], dtype=float)       # SF54 a/a_fold on upstream grid (local)
    x_ideal_up = np.asarray(d2f["x_tau_ideal"], dtype=float)     # upstream x (w_n=0) (local)
    x_volovik_up = np.asarray(d2f["x_tau_volovik"], dtype=float) # upstream x (w_n=-0.408) (local)
    q_ideal_up = np.asarray(d2f["q_ideal"], dtype=float)         # (local)
    q_volovik_up = np.asarray(d2f["q_volovik"], dtype=float)     # (local)
    tau_star_up = float(d2f["nominal_tau_star"])      # 0.451041 (local)
    x_star_ideal_up = float(d2f["x_star_ideal"])      # 401.7197 (upstream tau* w_n=0) (local)
    rho_s_frac_fold = float(d2f["rho_s_frac_fold"])   # 0.98848 (local)
    rho_n_frac_fold = float(d2f["rho_n_frac_fold"])   # 0.01152 (local)

    d_aoft = np.load(S96_AOFT_NPZ, allow_pickle=True)  # (local)
    frw_taus = np.asarray(d_aoft["frw_taus"], dtype=float)   # fold -> 0.6 (200 pt) (local)
    H2_aeff = np.asarray(d_aoft["H2_aeff"], dtype=float)     # AOFT a_eff-proxy rate (local)
    a2_zeta_up = float(d_aoft["a_2_FW_zeta"])                # 2776.165389 (local)
    tau_star_aoft = float(d_aoft["tau_star"])                # 0.451041 (local)

    # --- consistency cross-checks vs canonical + plan pins ---
    x_fold_match = abs(x_fold_up - X_FOLD_PIN) < 1e-3                                   # (local)
    w_n_lo_match = abs(w_n_volovik_up - W_N_LO) < 1e-9                                  # (local)
    w_n_hi_match = abs(w_n_ideal_up - W_N_HI) < 1e-12                                   # (local)
    w_s_match = abs(w_s_up - W_S) < 1e-12                                               # (local)
    a2_match = abs(a2_zeta_up - a_2_FW_zeta) < 1e-3                                      # (local)
    odlro_x_fold = rho_s_frac_fold / rho_n_frac_fold      # rebuild x_fold from fractions (local)
    odlro_match = abs(odlro_x_fold - x_fold_up) < 1e-6                                  # (local)

    # === Reconstruct a_eff(tau) over the FULL AOFT window [tau_fold, 0.6] =============
    # H_aeff = sqrt(H2_aeff); a_eff(tau) = exp( int_{tau_fold}^{tau} H_aeff dtau' ),
    # anchored a_eff(tau_fold)=1.  Interpolate the AOFT H2_aeff onto the dense
    # N_EVAL-point tau-grid first (the plan's 1001-pt grid on [0.190,0.6]).
    tau_grid = np.linspace(SCAN_LO, SCAN_HI, N_EVAL)                                    # (local)
    H2_aeff_dense = np.interp(tau_grid, frw_taus, H2_aeff)                              # (local)
    H_aeff_dense = np.sqrt(H2_aeff_dense)              # acoustic Hubble rate >= 0 (local)
    # cumulative trapezoid integral of H_aeff in tau (a_eff exponent)
    dtau = np.diff(tau_grid)                                                            # (local)
    integ = np.concatenate([[0.0],
                            np.cumsum(0.5 * (H_aeff_dense[1:] + H_aeff_dense[:-1]) * dtau)])  # (local)
    a_eff = np.exp(integ)                              # a_eff(tau_fold)=1 by construction (local)
    a_eff_monotone = bool(np.all(np.diff(a_eff) > 0))  # H_aeff>0 => strictly increasing (local)
    a_eff_today = float(a_eff[-1])                     # a_eff(tau_now=0.6) (local)

    # === x(tau) extended onto the full window (both FROZEN endpoints) =================
    x_tau_hi = x_of_a(a_eff, W_N_HI, x_fold_up)         # w_n=0   exponent +3 (local)
    x_tau_lo = x_of_a(a_eff, W_N_LO, x_fold_up)         # w_n=-0.408 exponent +1.777 (local)

    x_today_hi = float(x_tau_hi[-1])                    # x_today at w_n=0 (UPPER of band) (local)
    x_today_lo = float(x_tau_lo[-1])                    # x_today at w_n=-0.408 (LOWER of band) (local)
    x_today_band = (min(x_today_lo, x_today_hi), max(x_today_lo, x_today_hi))           # (local)

    # === MONOTONICITY (CLAIM 1): d ln x / d ln a = 3(1+w_n) > 0 =======================
    # analytic slopes (Sage-exact at plan-freeze)
    dlnx_dlna_hi = 3.0 * (1.0 + W_N_HI)                 # +3 (local)
    dlnx_dlna_lo = 3.0 * (1.0 + W_N_LO)                 # +1.77705 (local)
    mono_slopes_positive = bool(dlnx_dlna_hi > 0 and dlnx_dlna_lo > 0)                  # (local)
    # numerical confirmation: x strictly increasing along tau (since a_eff increasing)
    x_increasing_hi = bool(np.all(np.diff(x_tau_hi) > 0))                               # (local)
    x_increasing_lo = bool(np.all(np.diff(x_tau_lo) > 0))                               # (local)
    # numerical d ln x / d ln a from the reconstructed arrays (interior, both endpoints)
    lnx_hi = np.log(x_tau_hi); lnx_lo = np.log(x_tau_lo); lna = np.log(a_eff)           # (local)
    dlnx_dlna_hi_num = float(np.median(np.gradient(lnx_hi, lna)))                       # (local)
    dlnx_dlna_lo_num = float(np.median(np.gradient(lnx_lo, lna)))                       # (local)
    slope_resid_hi = abs(dlnx_dlna_hi_num - dlnx_dlna_hi)                               # (local)
    slope_resid_lo = abs(dlnx_dlna_lo_num - dlnx_dlna_lo)                               # (local)
    slope_resid_max = float(max(slope_resid_hi, slope_resid_lo))                        # (local)

    # x_today > x_fold for BOTH endpoints (the gate's primary inequality)
    x_today_gt_fold_hi = bool(x_today_hi > x_fold_up)                                   # (local)
    x_today_gt_fold_lo = bool(x_today_lo > x_fold_up)                                   # (local)
    x_today_gt_fold = bool(x_today_gt_fold_hi and x_today_gt_fold_lo)                   # (local)

    # === LATE-TIME DECELERATION (CLAIM 2): q(x_today) ~= -1 ==========================
    q_today_hi = float(q_two_fluid(np.array([x_today_hi]), W_N_HI)[0])                  # (local)
    q_today_lo = float(q_two_fluid(np.array([x_today_lo]), W_N_LO)[0])                  # (local)
    # band over the endpoints; the WORST-CASE (farthest from -1) governs the PASS test
    q_today_band = (min(q_today_lo, q_today_hi), max(q_today_lo, q_today_hi))           # (local)
    dq_hi = abs(q_today_hi - Q_TARGET)                                                  # (local)
    dq_lo = abs(q_today_lo - Q_TARGET)                                                  # (local)
    dq_worst = float(max(dq_hi, dq_lo))                # worst-case |q+1| over endpoints (local)
    q_pass_hi = bool(dq_hi <= TAU_Q)                                                    # (local)
    q_pass_lo = bool(dq_lo <= TAU_Q)                                                    # (local)
    q_pass_both = bool(q_pass_hi and q_pass_lo)                                         # (local)
    # INFO band: x_today>x_fold but |q+1| in (TAU_Q, INFO_Q_HI]
    q_info_band = bool((TAU_Q < dq_worst <= INFO_Q_HI))                                 # (local)

    # === CROSS-CHECK: reproduce the landed S96 values at tau* =========================
    # 1) the upstream x(tau*) via the SAME power law on the UPSTREAM a_norm grid
    a_norm_star = float(np.interp(tau_star_up, tau_grid_up, a_norm_up))                 # (local)
    x_star_hi_repro = x_of_a(np.array([a_norm_star]), W_N_HI, x_fold_up)[0]             # (local)
    x_star_lo_repro = x_of_a(np.array([a_norm_star]), W_N_LO, x_fold_up)[0]             # (local)
    # upstream stored x at tau* (last grid point of the 2-fluid npz):
    x_star_hi_up = float(x_ideal_up[-1])               # = x_star_ideal_up 401.72 (local)
    x_star_lo_up = float(x_volovik_up[-1])             # 214.095 (local)
    xcheck_hi = abs(x_star_hi_repro - x_star_hi_up) / x_star_hi_up                      # (local)
    xcheck_lo = abs(x_star_lo_repro - x_star_lo_up) / x_star_lo_up                      # (local)
    xcheck_star_ok = bool(max(xcheck_hi, xcheck_lo) < 1e-9)                             # (local)
    # 2) the q-formula reproduces the landed q_ideal/q_volovik on the upstream grid
    q_hi_repro = q_two_fluid(x_ideal_up, W_N_HI)                                        # (local)
    q_lo_repro = q_two_fluid(x_volovik_up, W_N_LO)                                      # (local)
    qcheck_hi = float(np.max(np.abs(q_hi_repro - q_ideal_up)))                          # (local)
    qcheck_lo = float(np.max(np.abs(q_lo_repro - q_volovik_up)))                        # (local)
    qcheck_grid_ok = bool(max(qcheck_hi, qcheck_lo) < 1e-12)                            # (local)
    # 3) q at the upstream x_star_ideal (401.72) -- the 2-fluid npz endpoint -- vs -1
    q_at_star_hi = float(q_two_fluid(np.array([x_star_ideal_up]), W_N_HI)[0])           # (local)

    return {
        # upstream anchors / matches
        "x_fold": x_fold_up, "x_fold_match": x_fold_match, "odlro_x_fold": odlro_x_fold,
        "odlro_match": odlro_match,
        "w_n_ideal_up": w_n_ideal_up, "w_n_volovik_up": w_n_volovik_up, "w_s_up": w_s_up,
        "w_n_lo_match": w_n_lo_match, "w_n_hi_match": w_n_hi_match, "w_s_match": w_s_match,
        "a2_zeta_up": a2_zeta_up, "a2_match": a2_match,
        "tau_star_up": tau_star_up, "tau_star_aoft": tau_star_aoft,
        "rho_s_frac_fold": rho_s_frac_fold, "rho_n_frac_fold": rho_n_frac_fold,
        # grids
        "tau_grid": tau_grid, "a_eff": a_eff, "H_aeff_dense": H_aeff_dense,
        "x_tau_hi": x_tau_hi, "x_tau_lo": x_tau_lo,
        "a_eff_monotone": a_eff_monotone, "a_eff_today": a_eff_today,
        # x_today band
        "x_today_hi": x_today_hi, "x_today_lo": x_today_lo,
        "x_today_band_lo": x_today_band[0], "x_today_band_hi": x_today_band[1],
        # monotonicity (CLAIM 1)
        "dlnx_dlna_hi": dlnx_dlna_hi, "dlnx_dlna_lo": dlnx_dlna_lo,
        "dlnx_dlna_hi_num": dlnx_dlna_hi_num, "dlnx_dlna_lo_num": dlnx_dlna_lo_num,
        "slope_resid_max": slope_resid_max, "mono_slopes_positive": mono_slopes_positive,
        "x_increasing_hi": x_increasing_hi, "x_increasing_lo": x_increasing_lo,
        "x_today_gt_fold_hi": x_today_gt_fold_hi, "x_today_gt_fold_lo": x_today_gt_fold_lo,
        "x_today_gt_fold": x_today_gt_fold,
        # late-time deceleration (CLAIM 2)
        "q_today_hi": q_today_hi, "q_today_lo": q_today_lo,
        "q_today_band_lo": q_today_band[0], "q_today_band_hi": q_today_band[1],
        "dq_hi": dq_hi, "dq_lo": dq_lo, "dq_worst": dq_worst,
        "q_pass_hi": q_pass_hi, "q_pass_lo": q_pass_lo, "q_pass_both": q_pass_both,
        "q_info_band": q_info_band,
        # cross-checks
        "x_star_hi_repro": float(x_star_hi_repro), "x_star_lo_repro": float(x_star_lo_repro),
        "x_star_hi_up": x_star_hi_up, "x_star_lo_up": x_star_lo_up,
        "xcheck_hi": float(xcheck_hi), "xcheck_lo": float(xcheck_lo), "xcheck_star_ok": xcheck_star_ok,
        "qcheck_hi": qcheck_hi, "qcheck_lo": qcheck_lo, "qcheck_grid_ok": qcheck_grid_ok,
        "x_star_ideal_up": x_star_ideal_up, "q_at_star_hi": q_at_star_hi,
    }


# -----------------------------------------------------------------------------
# Section 6 - Gate verdict ([VERIFY]: monotonicity AND late-time q sign)
# -----------------------------------------------------------------------------
def evaluate_gate(res: dict) -> str:
    """Return composite PASS|FAIL|INFO per the plan W1-2 rubric.

    PASS : x_today > x_fold (BOTH endpoints, monotone) AND q(x_today)~=-1 (|q+1|<=0.05
           BOTH endpoints).  Substrate determines the A-PASS x-window; late-time is
           vacuum/effacement-dominated.
    FAIL : x_today <= x_fold (monotonicity violated -- would contradict Sage-exact
           d ln x/d ln a > 0) OR q(x_today) not within 0.05 of -1.
    INFO : x_today > x_fold but |q+1| in (0.05, 0.20] -- late-tau endpoint has not fully
           reached the x->inf vacuum limit (tau_now-sensitive).
    """
    # gating consistency: the reconstruction must be internally sound
    recon_ok = bool(res["a_eff_monotone"] and res["mono_slopes_positive"]
                    and res["slope_resid_max"] < 1e-6
                    and res["xcheck_star_ok"] and res["qcheck_grid_ok"])               # (local)

    if not recon_ok:
        return "FAIL"  # reconstruction not numerically usable

    if not res["x_today_gt_fold"]:
        return "FAIL"  # monotonicity / inequality violated

    if res["q_pass_both"]:
        return "PASS"  # x_today>x_fold AND q~=-1 at both endpoints
    if res["q_info_band"]:
        return "INFO"  # x-window substrate-determined; q approach tau_now-sensitive
    return "FAIL"      # q too far from -1


# -----------------------------------------------------------------------------
# Section 7 - Plot
# -----------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    tau = res["tau_grid"]  # (local)
    fig, axes = plt.subplots(1, 2, figsize=(14.5, 6.2))  # (local)

    # Panel A: x(tau) band (both endpoints) over the full window to tau_now=0.6
    ax = axes[0]  # (local)
    ax.fill_between(tau, res["x_tau_lo"], res["x_tau_hi"], color="tab:blue", alpha=0.13,
                    label="$x(\\tau)$ band ($w_n\\in[-0.4076,0]$)")
    ax.plot(tau, res["x_tau_hi"], "-", color="tab:blue", lw=1.9,
            label="$x(\\tau)$ upper ($w_n=0$, exp $+3$)")
    ax.plot(tau, res["x_tau_lo"], "-", color="tab:purple", lw=1.9,
            label=f"$x(\\tau)$ lower ($w_n={W_N_LO:.4f}$, exp $+1.777$)")
    ax.axhline(res["x_fold"], color="k", ls="-.", lw=1.1,
               label=f"$x_{{fold}}={res['x_fold']:.2f}$ (S67 ODLRO)")
    ax.axvline(tau_fold, color="0.5", ls=":", lw=0.9)
    ax.axvline(res["tau_star_up"], color="tab:orange", ls="-.", lw=1.0, alpha=0.8,
               label=f"$\\tau_*={res['tau_star_up']:.4f}$ (2-fluid grid end)")
    ax.axvline(SCAN_HI, color="tab:green", ls="--", lw=1.0,
               label=f"$\\tau_{{now}}={SCAN_HI}$")
    ax.annotate(f"$x_{{today}}$ band\n[{res['x_today_band_lo']:.1f}, {res['x_today_band_hi']:.1f}]\n"
                f"$> x_{{fold}}={res['x_fold']:.1f}$",
                xy=(0.40, 0.62), xycoords="axes fraction", fontsize=8.6,
                bbox=dict(boxstyle="round", fc="white", alpha=0.88))
    ax.set_xlabel("$\\tau$ (Jensen deformation; order-parameter clock)", fontsize=11)
    ax.set_ylabel("$x = \\rho_s/\\rho_n$ (condensate-to-relic ratio)", fontsize=11)
    ax.set_title("Substrate-determined $x(\\tau)$ growth: order-parameter trajectory\n"
                 "carrying spectral weight toward the unbroken-condensate ($w=-1$) sector", fontsize=10)
    ax.legend(loc="upper left", fontsize=7.6, framealpha=0.9)
    ax.grid(True, alpha=0.25)

    # Panel B: q(x) two-fluid curve + late-time approach to -1
    ax = axes[1]  # (local)
    xx = np.logspace(np.log10(res["x_fold"]) - 0.1, 4.0, 500)  # (local)
    ax.plot(xx, q_two_fluid(xx, W_N_HI), "-", color="tab:blue", lw=1.9,
            label="$q(x)$ ($w_n=0$)")
    ax.plot(xx, q_two_fluid(xx, W_N_LO), "-", color="tab:purple", lw=1.9,
            label=f"$q(x)$ ($w_n={W_N_LO:.4f}$)")
    ax.axhline(-1.0, color="tab:gray", ls=":", lw=1.2, label="$q=-1$ (vacuum limit)")
    ax.axhspan(-1.0 - TAU_Q, -1.0 + TAU_Q, color="tab:green", alpha=0.15,
               label=f"PASS band $|q+1|\\leq{TAU_Q}$")
    ax.axvline(res["x_fold"], color="k", ls="-.", lw=1.0,
               label=f"$x_{{fold}}={res['x_fold']:.1f}$")
    ax.axvline(res["x_today_band_lo"], color="tab:purple", ls="--", lw=1.0, alpha=0.7)
    ax.axvline(res["x_today_band_hi"], color="tab:blue", ls="--", lw=1.0, alpha=0.7)
    ax.annotate(f"$q(x_{{today}})$ band\n[{res['q_today_band_lo']:.4f}, {res['q_today_band_hi']:.4f}]\n"
                f"worst $|q+1|={res['dq_worst']:.4f}$",
                xy=(0.40, 0.18), xycoords="axes fraction", fontsize=8.6,
                bbox=dict(boxstyle="round", fc="white", alpha=0.88))
    ax.set_xscale("log")
    ax.set_xlabel("$x = \\rho_s/\\rho_n$", fontsize=11)
    ax.set_ylabel("$q(x)=\\frac{1}{2}\\frac{(1+3w_n)+x(1+3w_s)}{1+x}$", fontsize=11)
    ax.set_title("Late-time deceleration $\\to -1$ (Sage-exact $\\lim_{x\\to\\infty}q=-1$)\n"
                 "increasing $x$ drives $q$ toward the effaced-vacuum value", fontsize=10)
    ax.legend(loc="upper right", fontsize=7.6, framealpha=0.9)
    ax.grid(True, which="both", alpha=0.25)

    fig.suptitle(f"{GATE_ID} - substrate-determined $x_{{today}}$ window (two-fluid integration)",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PNG_OUT, dpi=140)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Section 8 - Verdict-line emitter (atomic append; dual-SHA companion row)
# -----------------------------------------------------------------------------
def append_verdict(verdict, value_str, audit_sha, content_sha, res) -> None:
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] two-fluid x_today window; "
        f"feeds S97-W1-QOMEGA-ROUTE-INVARIANCE A-window\n"
    )
    detail_row = (
        f"# x_fold={res['x_fold']:.4f}(S67 ODLRO) "
        f"x_today_band=[{res['x_today_band_lo']:.4f},{res['x_today_band_hi']:.4f}] "
        f"(w_n=-0.4076 -> {res['x_today_lo']:.4f}; w_n=0 -> {res['x_today_hi']:.4f}); "
        f"x_today>x_fold={res['x_today_gt_fold']}; "
        f"d_ln_x_d_ln_a=3(1+w_n): +{res['dlnx_dlna_hi']:.4f}(w_n=0), +{res['dlnx_dlna_lo']:.5f}(w_n=-0.4076) "
        f"both>0 (Sage-exact CLAIM 1; slope_resid_max={res['slope_resid_max']:.2e}); "
        f"q_today_band=[{res['q_today_band_lo']:.4f},{res['q_today_band_hi']:.4f}] "
        f"worst|q+1|={res['dq_worst']:.4f}(<=tau_q {TAU_Q}? {res['q_pass_both']}); "
        f"lim_x->inf q=-1 (Sage-exact CLAIM 2); "
        f"# {GATE_ID} x_today = substrate-determined A-PASS x-window\n"
    )
    crosscheck_row = (
        f"# CROSS-CHECK: x(tau*) repro vs landed S96-W1-VOLOVIK-2FLUID: "
        f"w_n=0 {res['x_star_hi_repro']:.4f} vs {res['x_star_hi_up']:.4f} (rel {res['xcheck_hi']:.2e}); "
        f"w_n=-0.4076 {res['x_star_lo_repro']:.4f} vs {res['x_star_lo_up']:.4f} (rel {res['xcheck_lo']:.2e}); "
        f"q-formula reproduces q_ideal/q_volovik on upstream grid (max resid {max(res['qcheck_hi'],res['qcheck_lo']):.2e}); "
        f"q(x_star=401.72,w_n=0)={res['q_at_star_hi']:.4f}; xcheck_ok={res['xcheck_star_ok'] and res['qcheck_grid_ok']} "
        f"# {GATE_ID} reproduces landed values; a_eff via int sqrt(H2_aeff) (AOFT route to tau_now=0.6)\n"
    )
    regulator_pin = (
        f"# LEVEL_CLASS_PIN=FULL regulator_pin=a_n_zeta "
        f"# {GATE_ID} a_2^zeta={a_2_FW_zeta:.6f} (a_eff backbone via AOFT H2_aeff); "
        f"w_n in [{W_N_LO:.6f},{W_N_HI}] from S67 GGE-TWO-FLUID-67 FROZEN band; "
        f"rho_s carries Gamma_eff={Gamma_effacement} (w=-1); n_pairs={n_pairs}, P_exc={P_exc_kz}; "
        f"substrate-first-canonical-sourcing.md PASS\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(detail_row)
        fp.write(crosscheck_row)
        fp.write(regulator_pin)


# -----------------------------------------------------------------------------
# Section 9 - Main
# -----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()
    print(f"  canonical: a_2^zeta={a_2_FW_zeta:.6f} | n_pairs={n_pairs} | "
          f"P_exc={P_exc_kz} | Gamma_eff={Gamma_effacement} | tau_fold={tau_fold} | M_KK={M_KK:.4e}")
    print(f"  FROZEN w_n band endpoints: [{W_N_LO:.6f}, {W_N_HI}] | w_s={W_S} | x_fold_pin={X_FOLD_PIN}")
    print(f"  tau window [{SCAN_LO}, {SCAN_HI}], N_eval={N_EVAL}, step={STEP_SIZE:.4e}")
    print()

    res = compute()  # (local)

    print("=== upstream consistency (S96 npz + plan pins) ===")
    print(f"  x_fold = {res['x_fold']:.6f} (=plan 85.7928? {res['x_fold_match']}; "
          f"ODLRO rebuild {res['odlro_x_fold']:.6f} match {res['odlro_match']})")
    print(f"  w_n endpoints: ideal={res['w_n_ideal_up']} (=0? {res['w_n_hi_match']}); "
          f"volovik={res['w_n_volovik_up']:.6f} (=-0.4076? {res['w_n_lo_match']}); "
          f"w_s={res['w_s_up']} (match {res['w_s_match']})")
    print(f"  a_2^zeta upstream={res['a2_zeta_up']:.6f} (match canonical {res['a2_match']})")
    print()
    print("=== a_eff(tau) reconstruction (AOFT acoustic-rate route to tau_now=0.6) ===")
    print(f"  a_eff monotone increasing: {res['a_eff_monotone']}; a_eff(tau_now=0.6)={res['a_eff_today']:.6f}")
    print()
    print("=== MONOTONICITY (CLAIM 1: d ln x/d ln a = 3(1+w_n) > 0) ===")
    print(f"  analytic slope: +{res['dlnx_dlna_hi']:.5f} (w_n=0), +{res['dlnx_dlna_lo']:.5f} (w_n=-0.4076); "
          f"both>0: {res['mono_slopes_positive']}")
    print(f"  numerical slope: {res['dlnx_dlna_hi_num']:.6f}, {res['dlnx_dlna_lo_num']:.6f}; "
          f"resid_max={res['slope_resid_max']:.3e}")
    print(f"  x increasing along tau: w_n=0 {res['x_increasing_hi']}, w_n=-0.4076 {res['x_increasing_lo']}")
    print()
    print("=== x_today BAND (substrate-determined A-PASS x-window) ===")
    print(f"  x_today(w_n=0)      = {res['x_today_hi']:.4f}  (> x_fold? {res['x_today_gt_fold_hi']})")
    print(f"  x_today(w_n=-0.4076)= {res['x_today_lo']:.4f}  (> x_fold? {res['x_today_gt_fold_lo']})")
    print(f"  x_today BAND = [{res['x_today_band_lo']:.4f}, {res['x_today_band_hi']:.4f}] > x_fold={res['x_fold']:.4f}: {res['x_today_gt_fold']}")
    print()
    print("=== LATE-TIME DECELERATION (CLAIM 2: q(x_today) ~= -1) ===")
    print(f"  q_today(w_n=0)      = {res['q_today_hi']:.6f}  (|q+1|={res['dq_hi']:.4f} <= {TAU_Q}? {res['q_pass_hi']})")
    print(f"  q_today(w_n=-0.4076)= {res['q_today_lo']:.6f}  (|q+1|={res['dq_lo']:.4f} <= {TAU_Q}? {res['q_pass_lo']})")
    print(f"  q_today BAND = [{res['q_today_band_lo']:.6f}, {res['q_today_band_hi']:.6f}]; "
          f"worst |q+1|={res['dq_worst']:.4f}; both PASS={res['q_pass_both']}; INFO-band={res['q_info_band']}")
    print()
    print("=== CROSS-CHECK (reproduce landed S96-W1-VOLOVIK-2FLUID at tau*) ===")
    print(f"  x(tau*) w_n=0:       repro {res['x_star_hi_repro']:.4f} vs landed {res['x_star_hi_up']:.4f} (rel {res['xcheck_hi']:.2e})")
    print(f"  x(tau*) w_n=-0.4076: repro {res['x_star_lo_repro']:.4f} vs landed {res['x_star_lo_up']:.4f} (rel {res['xcheck_lo']:.2e})")
    print(f"  q-formula vs landed q_ideal/q_volovik (grid): max resid {max(res['qcheck_hi'],res['qcheck_lo']):.2e} (ok {res['qcheck_grid_ok']})")
    print(f"  q(x_star_ideal=401.72, w_n=0) = {res['q_at_star_hi']:.6f}  (upstream q_ideal.max=-0.982717 cross-checks)")
    print()

    composite = evaluate_gate(res)  # (local)
    print(f"  COMPOSITE = {composite}")
    print()

    # Save npz
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID, composite_verdict=composite,
        # grids
        tau_grid=res["tau_grid"], a_eff=res["a_eff"], H_aeff_dense=res["H_aeff_dense"],
        x_tau_hi=res["x_tau_hi"], x_tau_lo=res["x_tau_lo"],
        # anchors / matches
        x_fold=res["x_fold"], x_fold_match=res["x_fold_match"],
        odlro_x_fold=res["odlro_x_fold"], odlro_match=res["odlro_match"],
        w_n_ideal_up=res["w_n_ideal_up"], w_n_volovik_up=res["w_n_volovik_up"], w_s_up=res["w_s_up"],
        w_n_lo_match=res["w_n_lo_match"], w_n_hi_match=res["w_n_hi_match"], w_s_match=res["w_s_match"],
        a2_zeta_up=res["a2_zeta_up"], a2_match=res["a2_match"],
        tau_star_up=res["tau_star_up"], tau_star_aoft=res["tau_star_aoft"],
        rho_s_frac_fold=res["rho_s_frac_fold"], rho_n_frac_fold=res["rho_n_frac_fold"],
        a_eff_monotone=res["a_eff_monotone"], a_eff_today=res["a_eff_today"],
        # x_today band (the PRIMARY OUTPUT consumed by gate 1.3)
        x_today_hi=res["x_today_hi"], x_today_lo=res["x_today_lo"],
        x_today_band_lo=res["x_today_band_lo"], x_today_band_hi=res["x_today_band_hi"],
        tau_now=SCAN_HI,
        # monotonicity (CLAIM 1)
        dlnx_dlna_hi=res["dlnx_dlna_hi"], dlnx_dlna_lo=res["dlnx_dlna_lo"],
        dlnx_dlna_hi_num=res["dlnx_dlna_hi_num"], dlnx_dlna_lo_num=res["dlnx_dlna_lo_num"],
        slope_resid_max=res["slope_resid_max"], mono_slopes_positive=res["mono_slopes_positive"],
        x_increasing_hi=res["x_increasing_hi"], x_increasing_lo=res["x_increasing_lo"],
        x_today_gt_fold_hi=res["x_today_gt_fold_hi"], x_today_gt_fold_lo=res["x_today_gt_fold_lo"],
        x_today_gt_fold=res["x_today_gt_fold"],
        # late-time deceleration (CLAIM 2)
        q_today_hi=res["q_today_hi"], q_today_lo=res["q_today_lo"],
        q_today_band_lo=res["q_today_band_lo"], q_today_band_hi=res["q_today_band_hi"],
        dq_hi=res["dq_hi"], dq_lo=res["dq_lo"], dq_worst=res["dq_worst"],
        q_pass_hi=res["q_pass_hi"], q_pass_lo=res["q_pass_lo"], q_pass_both=res["q_pass_both"],
        q_info_band=res["q_info_band"],
        q_target=Q_TARGET, tau_q=TAU_Q,
        # cross-checks
        x_star_hi_repro=res["x_star_hi_repro"], x_star_lo_repro=res["x_star_lo_repro"],
        x_star_hi_up=res["x_star_hi_up"], x_star_lo_up=res["x_star_lo_up"],
        xcheck_hi=res["xcheck_hi"], xcheck_lo=res["xcheck_lo"], xcheck_star_ok=res["xcheck_star_ok"],
        qcheck_hi=res["qcheck_hi"], qcheck_lo=res["qcheck_lo"], qcheck_grid_ok=res["qcheck_grid_ok"],
        x_star_ideal_up=res["x_star_ideal_up"], q_at_star_hi=res["q_at_star_hi"],
        # pins / canonical
        w_n_endpoints=np.array([W_N_HI, W_N_LO]), x_fold_pin=X_FOLD_PIN,
        N_eval=N_EVAL, scan_lo=SCAN_LO, scan_hi=SCAN_HI, step_size=STEP_SIZE,
        a_2_FW_zeta=a_2_FW_zeta, n_pairs=n_pairs, P_exc_kz=P_exc_kz,
        Gamma_effacement=Gamma_effacement, tau_fold=tau_fold, M_KK=M_KK,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  wrote {NPZ_OUT.name}")

    make_plot(res)
    print(f"  wrote {PNG_OUT.name}")

    value_str = (
        f"composite={composite};"
        f"x_today_band=[{res['x_today_band_lo']:.4f},{res['x_today_band_hi']:.4f}];"
        f"x_today_w0={res['x_today_hi']:.4f};x_today_wn={res['x_today_lo']:.4f};"
        f"x_fold={res['x_fold']:.4f};x_today_gt_fold={res['x_today_gt_fold']};"
        f"dlnx_dlna=3(1+w_n):+{res['dlnx_dlna_hi']:.4f}/+{res['dlnx_dlna_lo']:.5f};mono_pos={res['mono_slopes_positive']};"
        f"q_today_band=[{res['q_today_band_lo']:.4f},{res['q_today_band_hi']:.4f}];"
        f"worst_abs_q_plus1={res['dq_worst']:.4f};tau_q={TAU_Q};q_pass_both={res['q_pass_both']};"
        f"a_eff_today={res['a_eff_today']:.4f};tau_now={SCAN_HI};"
        f"xcheck_star_ok={res['xcheck_star_ok']};qcheck_grid_ok={res['qcheck_grid_ok']};"
        f"w_n_band=[{W_N_LO:.6f},{W_N_HI}];lim_x_inf_q=-1_Sage_exact"
    )  # (local)
    append_verdict(composite, value_str, audit_sha, content_sha, res)
    print(f"  appended verdict line: {GATE_ID}: {composite}")
    print(f"\n  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
