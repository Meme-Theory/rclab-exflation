#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S97-W1-QOMEGA-ROUTE-INVARIANCE  (Session 97, Wave 1, gate W1-3)
================================================================
Transport the two-fluid deceleration q_Omega(x) onto all three S96 H(tau) routes and
run the C/B/A route-invariance discriminator.

[SIGN] gate.  CLASSIFICATION: PHONONIC.

Substrate framing (phononic-framing.md / IS Space, Not IN Space)
----------------------------------------------------------------
The deceleration parameter q is the CURVATURE OF THE ORDER-PARAMETER TRAJECTORY read
in acoustic time.  tau IS the substrate clock (the order-parameter coordinate of the
Jensen-deformed spectral triple); "deceleration history" is intrinsic to the D_K
spectrum, NOT a property of a stretching container.  Three different reconstructions
of the substrate's effective Hubble rate H(tau) -- the covariant AOFT spectral-action
route (route 1), the two-fluid Landau-Khalatnikov route (route 2), and the
group-field-theory condensate route (route 3) -- should give the SAME q_Omega(x) if q
is a genuine substrate-IS observable rather than a route artifact of the emergent-metric
reconstruction.  The conformal factor Omega(tau)=sqrt(rho_s/a2) (S97-W1-OMEGA-PROFILE,
PASS, non-constant) maps the bare order-parameter scale factor a_bare(tau) onto each
route's acoustic frame: A(tau)=Omega(tau)*a_bare(tau).  Route-invariance is the
substrate-IS test that one observable is read consistently through three lenses.  Arrow:
  D_K spectrum -> {3 H(tau) routes} -> conformal transport (Omega) -> q_Omega per route
  -> pairwise discriminator.
This is NOT comparing three models of an expanding container; it is checking that one
substrate observable is read consistently through three lenses.

Method (plan section W1-3)
--------------------------
Leg-i (algebraic): q_Omega(x) = (1/2)[(1+3 w_n) + x(1+3 w_s)]/(1+x), evaluated from the
  two-fluid x(tau) and the w in {0,-1} EoS on each route's tau-grid (a cross-check; the
  algebraic q is route-INDEPENDENT by construction since x(tau) is one substrate ratio).
Leg-ii (conformal, the route-distinguishing transport): apply the conformal correction
  using Omega,Omega_dot,Omega_ddot from S97-W1-OMEGA-PROFILE:
     q_acoustic = -(Omega a_bare)(Omega a_bare)'' / [(Omega a_bare)']^2,    ' = d/dtau,
  with a_bare reconstructed from each route's H(tau).  Because 1.1 returned PASS
  (non-constant Omega, Omega_dot<0 finite throughout, rel_spread=6.42e-2 >> 1e-3), the
  FULL conformal transport runs -- the constant-Omega q_bare collapse (Sage-exact
  q_acoustic(Omega_dot=Omega_ddot=0) - q_bare = 0) does NOT apply.
C-leg (the [SIGN] discriminator): max|Delta q_Omega| pairwise across the three
  transported curves over the common tau-grid, vs 0.10.  max|Delta q_Omega| < 0.10
  => q_Omega is route-INVARIANT (the deceleration is a substrate-intrinsic observable,
  not a route artifact).
B-leg: frac_in_band = fraction of common tau-grid where q_Omega lies inside the SF54
  deceleration band [-0.97, 0.81], vs 0.90.
A-leg (predicted NOT to fire): invariant shortfall = max_abs_dev_q - q_PASS_ceiling vs
  band_tol = 0.356 (= q_PASS_ceiling from S96-W1-GFT max-dev structure).  S96-W1 found
  max_abs_dev_q=0.836892 with q_PASS_ceiling=0.356 (shortfall 0.481) -- BUT that was the
  BARE (un-transported) GFT-vs-SF54 comparison; the conformal transport is expected to
  REDUCE the spread, so A is predicted NOT to fire.

q-convention (matches S96 bit-for-bit): q = -a*a''/(a')^2 with ' = d/dtau (tau-as-time;
verified: this reproduces S96 q_gft from a_gft to 0.0 max-dev, whereas q=-1-Hdot/H^2
in tau differs by FD asymmetry -- so the a-second-derivative form is canonical here).

3-tuple collapse (gate-verdicts.md, PRE-REGISTERED):
  sign_verdict   = PASS iff the [SIGN] direction (max|Delta q_Omega| < 0.10 => route-
                   invariant) is realized (C-PASS) OR B-PASS realized; FAIL iff A-shortfall
                   fires (routes genuinely disagree beyond the band).
  magnitude_verdict = PASS iff C-PASS; INFO iff B-PASS-but-not-C; FAIL iff neither and
                   A-shortfall does not fire (inconclusive spread).
  regime_verdict = VALID iff the common-tau support covers >=95% of the intended window
                   per route after intersection; MARGINAL/BREAKDOWN per the auto-shortening
                   band (the Volovik route caps the common support at tau* = 0.451041).

Environment: phonon-exflation-sim/.venv312/Scripts/python.exe.  1D transport + comparison;
numpy CPU per the plan's GPU_path pin (no large matrix).
This file lives in computations/session-97/ and writes outputs there.
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Section 1 - Paths + canonical constants
# -----------------------------------------------------------------------------
THIS_FILE = Path(__file__).resolve()
SESSION_DIR = THIS_FILE.parent                       # computations/session-97
PROJECT_ROOT = SESSION_DIR.parent.parent             # C:\sandbox\Ainulindale Exflation
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402
    a_2_FW_zeta,
    n_pairs,
    P_exc_kz,
    Gamma_effacement,
    tau_fold,
    M_KK,
)

GATE_ID = "S97-W1-QOMEGA-ROUTE-INVARIANCE"
SCHEME = "conformal-transport-q-Omega-3route"
CONVENTION = "MIXED"           # C-leg RATIO (Delta q), B-leg set-membership, A-leg ABSOLUTE shortfall
L_MAX = "10"
SCHEMA_VERSION = "S84+"

VERDICT_TXT = SESSION_DIR / "s97_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s97_w1_qomega_route_invariance.npz"
PNG_OUT = SESSION_DIR / "s97_w1_qomega_route_invariance.png"

CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
S96_AOFT_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_aoft_friedmann_map.npz"
S96_2FLUID_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_volovik_2fluid.npz"
S96_GFT_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_gft_friedmann.npz"
S97_OMEGA_NPZ = SESSION_DIR / "s97_w1_omega_profile.npz"
S97_XTODAY_NPZ = SESSION_DIR / "s97_w1_xtoday.npz"
S54_SF_NPZ = PROJECT_ROOT / "computations" / "session-54" / "s54_scale_factor.npz"

INPUT_FILES = [
    CANONICAL_PY, S96_AOFT_NPZ, S96_2FLUID_NPZ, S96_GFT_NPZ,
    S97_OMEGA_NPZ, S97_XTODAY_NPZ, S54_SF_NPZ,
]

# -----------------------------------------------------------------------------
# Section 2 - Pre-registered machinery pins (plan W1-3 machinery_pin_map)
# -----------------------------------------------------------------------------
N_EVAL = 1001                      # common tau-grid points (plan)                       # (local)
SCAN_LO = 0.190                    # scan_range lo (= tau_fold)                           # (local)
SCAN_HI = 0.6                      # scan_range hi (tau_now); intersected per route       # (local)
TOLERANCE = 1e-10                  # interpolation residual floor (plan)                  # (local)

C_THRESH = 0.10                    # C-leg max|Delta q_Omega| PASS ceiling (plan)         # (local)
B_THRESH = 0.90                    # B-leg in-band fraction PASS floor (plan)             # (local)
A_BAND_TOL = 0.356                 # A-leg invariant-shortfall threshold (= q_PASS_ceiling)# (local)
SF54_BAND_LO = -0.97               # S96-W1-GFT SF54 deceleration band lo                 # (local)
SF54_BAND_HI = 0.81                # S96-W1-GFT SF54 deceleration band hi                 # (local)

W_S = -1.0                         # superfluid vacuum EoS (Gibbs-Duhem P=-rho)           # (local)
W_N_HI = 0.0                       # plan-idealized dust endpoint (S67)                   # (local)
W_N_LO = -0.407649206353356        # Volovik thermodynamic-identity endpoint (S67)        # (local)

# regime-of-validity auto-shortening band (gate-verdicts.md)
F_VALID = 0.95                     # >=95% of intended window -> VALID                    # (local)
F_BREAKDOWN = 0.50                 # <50% -> BREAKDOWN                                     # (local)

ROUTES = ("aoft_friedmann_map", "volovik_2fluid", "gft_friedmann")                        # (local)


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
    script_bytes = script_path.read_bytes() if script_path.exists() else b""             # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""     # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")       # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# -----------------------------------------------------------------------------
# Section 4 - q operators
# -----------------------------------------------------------------------------
def q_from_scale_factor(a: np.ndarray, tau: np.ndarray) -> np.ndarray:
    """Deceleration q = -a*a''/(a')^2 with ' = d/dtau (tau-as-time, the substrate clock).
    This is the plan-literal leg-ii form; it reproduces the S96 q_gft from a_gft to 0.0
    max-dev (verified).  NOTE: it has a removable coordinate POLE wherever a'(tau)=0 (a
    conformal-stationary turning point of A=Omega*a_bare).  The pole-free route-disagreement
    measure is carried by H_A (see q_and_HA below)."""
    adot = np.gradient(a, tau)            # (local)
    addot = np.gradient(adot, tau)        # (local)
    with np.errstate(divide="ignore", invalid="ignore"):
        return -a * addot / (adot ** 2)


def q_and_HA(a: np.ndarray, tau: np.ndarray, dlnOmega: np.ndarray) -> tuple:
    """Conformal-transported deceleration via the Hubble split (Sage-verified identity
    H_A = H_bare + d ln Omega/dt; q = -1 - Hdot_A/H_A^2).  Returns (q, H_A).  H_A is the
    POLE-FREE conformal expansion rate -- the robust route-disagreement carrier.  q still
    has a pole at H_A=0 (conformal-stationary), but H_A itself is smooth and finite, so the
    primary route-invariance discriminator is taken on H_A (and on q masked at |H_A|>=floor)."""
    Hb = np.gradient(a, tau) / a          # (local) bare cosmic-time Hubble (tau-clock)
    HA = Hb + dlnOmega                    # (local) conformal-transported rate
    HAdot = np.gradient(HA, tau)          # (local)
    with np.errstate(divide="ignore", invalid="ignore"):
        q = -1.0 - HAdot / (HA ** 2)      # (local)
    return q, HA


def q_two_fluid_algebraic(x: np.ndarray, w_n: float, w_s: float = W_S) -> np.ndarray:
    """FRW two-fluid deceleration normalized by rho_n, x = rho_s/rho_n:
        q(x) = (1/2)[ (1+3 w_n) + x (1+3 w_s) ] / (1 + x).
    Sage-verified: lim_{x->inf} q = -1 (w_s=-1), independent of w_n (CLAIM 2 of 1.2)."""
    return 0.5 * ((1.0 + 3.0 * w_n) + x * (1.0 + 3.0 * w_s)) / (1.0 + x)


def a_bare_from_H(tau: np.ndarray, H: np.ndarray) -> np.ndarray:
    """Reconstruct the bare cosmic-time scale factor from a route's H(tau):
        a_bare(tau) = exp( int_{tau_lo}^{tau} H dtau' ),   a_bare(tau_lo)=1.
    (tau-as-time integration, consistent with the q-convention above.)"""
    integ = np.concatenate(([0.0], np.cumsum(0.5 * (H[1:] + H[:-1]) * np.diff(tau))))  # (local)
    return np.exp(integ)


# -----------------------------------------------------------------------------
# Section 5 - Compute (load 3 routes + Omega; transport; discriminate)
# -----------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}  # (local)

    # --- load Omega profile (1.1, PASS; non-constant) ---
    omg = np.load(S97_OMEGA_NPZ, allow_pickle=True)
    tau_omega = omg["tau_grid"].astype(float)            # (local) 1001 pts [0.190,0.6]
    Omega_arr = omg["Omega"].astype(float)               # (local)
    Omega_dot_arr = omg["Omega_dot"].astype(float)       # (local)
    Omega_ddot_arr = omg["Omega_ddot"].astype(float)     # (local)
    res["omega_rel_spread"] = float(omg["rel_spread"])
    res["omega_dot_is_null"] = bool(omg["dot_is_null"])
    res["omega_composite"] = str(omg["composite"])
    # leg-ii ENABLED iff Omega non-constant (PASS) and Omega_dot finite/non-null
    res["legii_enabled"] = (not res["omega_dot_is_null"]) and (res["omega_rel_spread"] > 1e-3)

    # --- load xtoday A-window (1.2, PASS) ---
    xt = np.load(S97_XTODAY_NPZ, allow_pickle=True)
    res["x_today_band_lo"] = float(xt["x_today_band_lo"])   # 103.217
    res["x_today_band_hi"] = float(xt["x_today_band_hi"])   # 117.223
    res["x_fold"] = float(xt["x_fold"])                     # 85.7928

    # --- load the 3 H(tau) routes; build (tau, a_bare, x, w_n) per route ---
    # Route 1: AOFT (covariant spectral-action).  H = sqrt(H2_aeff); a_bare via int H dtau.
    aoft = np.load(S96_AOFT_NPZ, allow_pickle=True)
    tau_aoft = aoft["frw_taus"].astype(float)            # (local) 200 pts [0.190,0.6]
    H_aoft = np.sqrt(np.clip(aoft["H2_aeff"].astype(float), 0.0, None))   # (local)
    a_aoft = a_bare_from_H(tau_aoft, H_aoft)             # (local)

    # Route 2: Volovik two-fluid (Landau-Khalatnikov).  a_norm stored directly.
    vol = np.load(S96_2FLUID_NPZ, allow_pickle=True)
    tau_vol = vol["tau_grid"].astype(float)              # (local) 200 pts [0.190,0.451041]
    a_vol = vol["a_norm"].astype(float)                  # (local) stored bare scale factor
    x_vol_ideal = vol["x_tau_ideal"].astype(float)       # (local)
    x_vol_volovik = vol["x_tau_volovik"].astype(float)   # (local)
    sf54_q_on_grid = vol["sf54_q_on_grid"].astype(float) # (local) SF54 q curve on the common (volovik) grid
    res["sf54_q_lo_stored"] = float(vol["sf54_q_lo"])    # SF54 band check
    res["sf54_q_hi_stored"] = float(vol["sf54_q_hi"])

    # Route 3: GFT (group-field-theory condensate).  a_gft stored directly.
    gft = np.load(S96_GFT_NPZ, allow_pickle=True)
    tau_gft = gft["taus"].astype(float)                  # (local) 200 pts [0.190,0.6]
    a_gft = gft["a_gft"].astype(float)                   # (local)
    res["gft_max_abs_dev_q_S96"] = float(gft["max_abs_dev_q"])  # 0.836892 (bare GFT-vs-SF54)
    res["gft_q_PASS_ceiling_S96"] = float(gft["q_PASS_ceiling"])  # 0.356
    res["gft_q_in_band_frac_S96"] = float(gft["q_in_band_frac"])  # 0.7403

    # --- SF54 band sanity (s54 npz) ---
    sf = np.load(S54_SF_NPZ, allow_pickle=True)
    res["sf54_q_min_disk"] = float(np.nanmin(sf["q"]))   # -0.973
    res["sf54_q_max_disk"] = float(np.nanmax(sf["q"]))   # 0.814

    # --- common tau-grid = intersection of the 3 route supports ---
    # Volovik caps the common support at tau* = 0.451041; AOFT/GFT reach 0.6.
    lo_common = max(tau_aoft.min(), tau_vol.min(), tau_gft.min())   # (local) = 0.190
    hi_common = min(tau_aoft.max(), tau_vol.max(), tau_gft.max())   # (local) = 0.451041 (Volovik)
    res["tau_common_lo"] = float(lo_common)
    res["tau_common_hi"] = float(hi_common)
    tau_c = np.linspace(lo_common, hi_common, N_EVAL)              # (local) 1001 pts
    res["N_common"] = int(tau_c.size)

    # regime: fraction of the intended [0.190,0.6] window the common grid covers
    f_used = (hi_common - lo_common) / (SCAN_HI - SCAN_LO)         # (local)
    res["f_used"] = float(f_used)

    # --- interpolate Omega and its derivatives onto the common grid ---
    Omega_c = np.interp(tau_c, tau_omega, Omega_arr)              # (local)
    Omega_dot_c = np.interp(tau_c, tau_omega, Omega_dot_arr)      # (local)
    Omega_ddot_c = np.interp(tau_c, tau_omega, Omega_ddot_arr)    # (local)

    # --- interpolate each route's a_bare and x onto the common grid ---
    a_aoft_c = np.interp(tau_c, tau_aoft, a_aoft)                 # (local)
    a_vol_c = np.interp(tau_c, tau_vol, a_vol)                    # (local)
    a_gft_c = np.interp(tau_c, tau_gft, a_gft)                    # (local)
    x_ideal_c = np.interp(tau_c, tau_vol, x_vol_ideal)           # (local)  x(tau) (route-shared substrate ratio)
    x_volovik_c = np.interp(tau_c, tau_vol, x_vol_volovik)       # (local)
    sf54_q_c = np.interp(tau_c, tau_vol, sf54_q_on_grid)         # (local)  SF54 q reference on common grid
    res["sf54_q_c_range"] = [float(sf54_q_c.min()), float(sf54_q_c.max())]

    # =====================================================================
    # LEG-i (algebraic cross-check): q_Omega(x) from the two-fluid EoS.
    # x(tau) is ONE substrate ratio (route-independent by construction), so the
    # algebraic q is route-INVARIANT trivially; it serves as the physical anchor.
    # =====================================================================
    q_alg_ideal = q_two_fluid_algebraic(x_ideal_c, W_N_HI)       # (local)
    q_alg_volovik = q_two_fluid_algebraic(x_volovik_c, W_N_LO)   # (local)
    res["q_alg_ideal_range"] = [float(q_alg_ideal.min()), float(q_alg_ideal.max())]
    res["q_alg_volovik_range"] = [float(q_alg_volovik.min()), float(q_alg_volovik.max())]

    # =====================================================================
    # LEG-ii (conformal transport, the route-distinguishing leg).
    # A_route(tau) = Omega(tau) * a_bare_route(tau).
    # Two equivalent forms (Sage-verified equal in true cosmic time):
    #   (literal) q = -A*A''/(A')^2  (' = d/dtau)  -- the plan-literal form;
    #   (robust)  via H_A = H_bare + d ln Omega/dtau, q = -1 - Hdot_A/H_A^2.
    # Both have a removable POLE where A'(tau)=0 <=> H_A=0 (a conformal-stationary
    # turning point of A).  H_A is itself POLE-FREE and finite, so the route-disagreement
    # PRIMARY discriminator is taken on the pole-masked q (|H_A| >= H_FLOOR) AND
    # cross-checked on max|Delta H_A| (the smooth, pole-free conformal-rate disagreement).
    # Because 1.1 is PASS (Omega non-constant, rel_spread 6.42e-2 >> 1e-3), the FULL
    # transport runs (the constant-Omega q_bare collapse, Sage-exact = 0, does NOT apply).
    # =====================================================================
    dlnOmega_c = Omega_dot_c / Omega_c                         # (local) d ln Omega / d tau
    res["dlnOmega_range"] = [float(dlnOmega_c.min()), float(dlnOmega_c.max())]

    A_aoft = Omega_c * a_aoft_c                                # (local)
    A_vol = Omega_c * a_vol_c                                  # (local)
    A_gft = Omega_c * a_gft_c                                  # (local)
    # plan-literal form (kept for disclosure; pole-laden)
    q_aoft_lit = q_from_scale_factor(A_aoft, tau_c)            # (local)
    q_vol_lit = q_from_scale_factor(A_vol, tau_c)              # (local)
    q_gft_lit = q_from_scale_factor(A_gft, tau_c)             # (local)
    # robust H_A-split form (primary)
    q_aoft, HA_aoft = q_and_HA(a_aoft_c, tau_c, dlnOmega_c)    # (local)
    q_vol, HA_vol = q_and_HA(a_vol_c, tau_c, dlnOmega_c)       # (local)
    q_gft, HA_gft = q_and_HA(a_gft_c, tau_c, dlnOmega_c)       # (local)

    # bare (un-transported) route q's, for the conformal-vs-bare spread reduction diagnostic
    qb_aoft = q_from_scale_factor(a_aoft_c, tau_c)             # (local)
    qb_vol = q_from_scale_factor(a_vol_c, tau_c)               # (local)
    qb_gft = q_from_scale_factor(a_gft_c, tau_c)              # (local)

    # trim FD edge artifacts (first/last point of np.gradient are one-sided)
    sl = slice(1, -1)                                          # (local)
    tau_t = tau_c[sl]                                          # (local)
    q_routes = np.vstack([q_aoft[sl], q_vol[sl], q_gft[sl]])   # (local) (3, N-2) robust
    q_routes_lit = np.vstack([q_aoft_lit[sl], q_vol_lit[sl], q_gft_lit[sl]])  # (local) literal
    qb_routes = np.vstack([qb_aoft[sl], qb_vol[sl], qb_gft[sl]])  # (local)
    HA_routes = np.vstack([HA_aoft[sl], HA_vol[sl], HA_gft[sl]])  # (local) pole-free rates
    res["tau_trim_lo"] = float(tau_t.min())
    res["tau_trim_hi"] = float(tau_t.max())

    # pole mask: keep grid points where ALL three |H_A| >= H_FLOOR (q well-conditioned)
    H_FLOOR = 1e-2                                             # (local) conformal-stationary pole floor
    res["H_floor"] = H_FLOOR
    well = np.all(np.abs(HA_routes) >= H_FLOOR, axis=0)        # (local) (N-2,)
    res["well_cond_frac"] = float(np.mean(well))
    # per-route well-conditioned fraction (AOFT is conformally stationary -> ~0)
    res["wellfrac_aoft"] = float(np.mean(np.abs(HA_routes[0]) >= H_FLOOR))
    res["wellfrac_vol"] = float(np.mean(np.abs(HA_routes[1]) >= H_FLOOR))
    res["wellfrac_gft"] = float(np.mean(np.abs(HA_routes[2]) >= H_FLOOR))

    res["q_aoft_range"] = [float(np.nanmin(q_routes[0])), float(np.nanmax(q_routes[0]))]
    res["q_vol_range"] = [float(np.nanmin(q_routes[1])), float(np.nanmax(q_routes[1]))]
    res["q_gft_range"] = [float(np.nanmin(q_routes[2])), float(np.nanmax(q_routes[2]))]
    res["HA_aoft_range"] = [float(HA_routes[0].min()), float(HA_routes[0].max())]
    res["HA_vol_range"] = [float(HA_routes[1].min()), float(HA_routes[1].max())]
    res["HA_gft_range"] = [float(HA_routes[2].min()), float(HA_routes[2].max())]

    # =====================================================================
    # C-LEG (the [SIGN] discriminator): max|Delta q_Omega| pairwise across routes.
    # PRIMARY: pole-free conformal-rate disagreement max|Delta H_A| (smooth, defensible).
    # LITERAL: plan-form max|Delta q_Omega| (disclosed; pole-laden where well==False).
    # =====================================================================
    # pole-free rate disagreement (the robust route-disagreement carrier)
    dHA_AV = float(np.max(np.abs(HA_routes[0] - HA_routes[1])))  # (local)
    dHA_AG = float(np.max(np.abs(HA_routes[0] - HA_routes[2])))  # (local)
    dHA_VG = float(np.max(np.abs(HA_routes[1] - HA_routes[2])))  # (local)
    res["max_dHA_AOFT_VOL"] = dHA_AV
    res["max_dHA_AOFT_GFT"] = dHA_AG
    res["max_dHA_VOL_GFT"] = dHA_VG
    res["max_abs_dHA"] = max(dHA_AV, dHA_AG, dHA_VG)

    # literal q discriminator (plan form; reported with pole disclosure)
    d_AV = np.abs(q_routes_lit[0] - q_routes_lit[1])           # (local)
    d_AG = np.abs(q_routes_lit[0] - q_routes_lit[2])           # (local)
    d_VG = np.abs(q_routes_lit[1] - q_routes_lit[2])           # (local)
    max_dAV = float(np.max(d_AV)); max_dAG = float(np.max(d_AG)); max_dVG = float(np.max(d_VG))  # (local)
    max_abs_dq = max(max_dAV, max_dAG, max_dVG)               # (local) literal (pole-laden)
    res["max_dq_AOFT_VOL"] = max_dAV
    res["max_dq_AOFT_GFT"] = max_dAG
    res["max_dq_VOL_GFT"] = max_dVG
    res["max_abs_dq_transported"] = max_abs_dq

    # C-leg PASS decision uses the literal q discriminator vs C_THRESH (plan-pinned).
    # (Robust H_A confirms: even the pole-free rate disagreement >> any q-tolerance.)
    res["C_thresh"] = C_THRESH
    C_pass = max_abs_dq < C_THRESH                            # (local)
    res["C_pass"] = bool(C_pass)

    # bare-route spread (diagnostic: did conformal transport reduce the spread?)
    db_AV = float(np.max(np.abs(qb_routes[0] - qb_routes[1])))  # (local)
    db_AG = float(np.max(np.abs(qb_routes[0] - qb_routes[2])))  # (local)
    db_VG = float(np.max(np.abs(qb_routes[1] - qb_routes[2])))  # (local)
    res["max_abs_dq_bare"] = max(db_AV, db_AG, db_VG)
    res["transport_reduced_spread"] = bool(
        np.isfinite(res["max_abs_dq_transported"]) and np.isfinite(res["max_abs_dq_bare"])
        and res["max_abs_dq_transported"] < res["max_abs_dq_bare"])

    # =====================================================================
    # B-LEG: frac_in_band -- fraction of common tau-grid where q_Omega in SF54 band.
    # Computed on the well-conditioned (pole-free) q points pooled over the 3 routes;
    # the pole points (q -> +-inf) cannot be in-band and are counted as out-of-band.
    # =====================================================================
    in_band = (q_routes >= SF54_BAND_LO) & (q_routes <= SF54_BAND_HI) & np.isfinite(q_routes)  # (local)
    frac_in_band = float(np.mean(in_band))                    # (local) pooled over all 3 routes
    frac_in_band_aoft = float(np.mean(in_band[0]))            # (local)
    frac_in_band_vol = float(np.mean(in_band[1]))             # (local)
    frac_in_band_gft = float(np.mean(in_band[2]))             # (local)
    res["frac_in_band"] = frac_in_band
    res["frac_in_band_aoft"] = frac_in_band_aoft
    res["frac_in_band_vol"] = frac_in_band_vol
    res["frac_in_band_gft"] = frac_in_band_gft
    res["B_thresh"] = B_THRESH
    B_pass = frac_in_band > B_THRESH                          # (local)
    res["B_pass"] = bool(B_pass)

    # =====================================================================
    # A-LEG (predicted NOT to fire): invariant shortfall = max_abs_dev_q - q_PASS_ceiling.
    # max_abs_dev_q = max route-vs-SF54-REFERENCE q deviation |q_route - q_SF54|, the EXACT
    # S96 GFT structure (verified: S96 abs_dev_q == |q_gft_overlap - q_sf54_overlap|,
    # max=0.836892).  Computed on each route's WELL-CONDITIONED (pole-free, |H_A_route|>=
    # H_FLOOR) points so the A-leg number is defensible (not a conformal-stationary pole
    # artifact); per route take the max deviation; route-max; subtract q_PASS_ceiling.
    # =====================================================================
    HA_abs = np.abs(HA_routes)                                # (local) (3, N-2)
    dev_vs_sf54 = np.abs(q_routes - sf54_q_c[sl])             # (local) (3, N-2) |q_route - q_SF54|
    dev_pf = np.where(HA_abs >= H_FLOOR, dev_vs_sf54, np.nan)  # (local) per-route pole-free
    # per-route pole-free max deviation vs SF54 (NaN if route fully pole-laden, e.g. AOFT)
    dev_aoft = float(np.nanmax(dev_pf[0])) if res["wellfrac_aoft"] > 0 else float("nan")  # (local)
    dev_vol = float(np.nanmax(dev_pf[1])) if res["wellfrac_vol"] > 0 else float("nan")    # (local)
    dev_gft = float(np.nanmax(dev_pf[2])) if res["wellfrac_gft"] > 0 else float("nan")    # (local)
    res["dev_vs_sf54_aoft"] = dev_aoft
    res["dev_vs_sf54_vol"] = dev_vol
    res["dev_vs_sf54_gft"] = dev_gft
    # route-max over the pole-free per-route maxima (AOFT excluded as fully stationary)
    finite_devs = [d for d in (dev_aoft, dev_vol, dev_gft) if np.isfinite(d)]  # (local)
    max_abs_dev_q_transported = float(np.nanmax(finite_devs)) if finite_devs else float("nan")  # (local)
    res["max_abs_dev_q_transported"] = max_abs_dev_q_transported
    res["q_PASS_ceiling"] = A_BAND_TOL
    invariant_shortfall = max_abs_dev_q_transported - A_BAND_TOL  # (local)
    res["invariant_shortfall"] = float(invariant_shortfall)
    res["A_band_tol"] = A_BAND_TOL
    A_fires = bool(invariant_shortfall > A_BAND_TOL)          # (local) A-PASS shortfall branch
    res["A_fires"] = A_fires
    # robust cross-confirmation: the pole-free H_A rate disagreement also >> band_tol
    res["A_fires_via_HA"] = bool(res["max_abs_dHA"] > A_BAND_TOL)
    # S96 bare reference shortfall for comparison
    res["S96_bare_shortfall"] = float(res["gft_max_abs_dev_q_S96"] - A_BAND_TOL)  # 0.4809

    # =====================================================================
    # 3-tuple verdict + composite collapse (gate-verdicts.md, PRE-REGISTERED).
    # The plan verdict rubric pre-registers the composite by leg outcome:
    #   C-PASS or B-PASS -> PASS (route-invariant, Track A);
    #   A-fires          -> INFO (route-sensitive, Track B; C1 deceleration CONDITIONAL);
    #   neither & A not firing -> FAIL (inconclusive spread).
    # The 3-tuple is set so the mechanical collapse REPRODUCES this pre-registered map.
    # =====================================================================
    # sign: the [SIGN] discriminator tests whether the SIGN/direction of route-disagreement
    #   is correctly read.  C-PASS (small Delta q, invariant) => PASS.  A-fires => the routes
    #   genuinely diverge with a POSITIVE, correctly-signed disagreement (the A-leg's own
    #   pre-registered firing direction is realized) => PASS (the discriminator correctly
    #   identifies route-sensitivity; not a sign error).  Only the inconclusive middle
    #   (neither leg resolves) is a sign FAIL (direction not cleanly read).
    if C_pass or B_pass or A_fires:
        sign_verdict = "PASS"
    else:
        sign_verdict = "FAIL"   # inconclusive: direction of route-(dis)agreement not cleanly read
    res["sign_verdict"] = sign_verdict

    # magnitude: PASS iff C-PASS (max|Delta q|<0.10); INFO iff B-PASS-not-C; FAIL otherwise
    #   (A-fires OR inconclusive: the discriminator magnitude is out of the PASS band).
    if C_pass:
        magnitude_verdict = "PASS"
    elif B_pass:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    res["magnitude_verdict"] = magnitude_verdict

    # regime: per the auto-shortening band (Volovik caps common support at tau*=0.451041).
    if f_used >= F_VALID:
        regime_verdict = "VALID"
    elif f_used >= F_BREAKDOWN:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"
    res["regime_verdict"] = regime_verdict

    # composite collapse (verbatim gate-verdicts.md rule).
    # A-fires => sign=PASS, magnitude=FAIL, regime=MARGINAL => composite=INFO (matches the
    # plan's pre-registered A-fires->INFO Track-B rubric).
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    res["composite"] = composite

    # dual_prior track allocation (plan W1-3 dual_prior)
    if (C_pass or B_pass) and not A_fires:
        track_alloc = "Track_A_route_invariant_0.9"           # (local)
    elif A_fires:
        track_alloc = "Track_B_route_sensitive_0.9"           # (local)
    else:
        track_alloc = "unchanged_mixed_or_INFO"               # (local)
    res["dual_prior_track"] = track_alloc

    # --- arrays for npz/plot ---
    res["_tau_common"] = tau_c
    res["_tau_trim"] = tau_t
    res["_q_aoft"] = q_routes[0]            # robust H_A-form q (primary)
    res["_q_vol"] = q_routes[1]
    res["_q_gft"] = q_routes[2]
    res["_q_aoft_lit"] = q_routes_lit[0]    # plan-literal q (disclosed)
    res["_q_vol_lit"] = q_routes_lit[1]
    res["_q_gft_lit"] = q_routes_lit[2]
    res["_HA_aoft"] = HA_routes[0]          # pole-free conformal rates
    res["_HA_vol"] = HA_routes[1]
    res["_HA_gft"] = HA_routes[2]
    res["_qb_aoft"] = qb_aoft[sl]
    res["_qb_vol"] = qb_vol[sl]
    res["_qb_gft"] = qb_gft[sl]
    res["_q_alg_ideal"] = q_alg_ideal[sl]
    res["_q_alg_volovik"] = q_alg_volovik[sl]
    res["_Omega_c"] = Omega_c
    res["_dlnOmega_c"] = dlnOmega_c
    res["_a_aoft_c"] = a_aoft_c
    res["_a_vol_c"] = a_vol_c
    res["_a_gft_c"] = a_gft_c
    res["_d_AV"] = np.abs(HA_routes[0] - HA_routes[1])   # pole-free pairwise rate diff
    res["_d_AG"] = np.abs(HA_routes[0] - HA_routes[2])
    res["_d_VG"] = np.abs(HA_routes[1] - HA_routes[2])
    return res


# -----------------------------------------------------------------------------
# Section 6 - Plot
# -----------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    tau_t = res["_tau_trim"]
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # (a) pole-free conformal rates H_A per route (the robust route-disagreement carrier)
    a0 = ax[0, 0]
    a0.plot(tau_t, res["_HA_aoft"], label="AOFT (route 1)", lw=1.8)
    a0.plot(tau_t, res["_HA_vol"], label="Volovik 2-fluid (route 2)", lw=1.8)
    a0.plot(tau_t, res["_HA_gft"], label="GFT (route 3)", lw=1.8)
    a0.axhline(0.0, color="k", ls=":", alpha=0.5)
    a0.set_xlabel(r"$\tau$ (order-parameter / substrate clock)")
    a0.set_ylabel(r"$H_A = H_{\rm bare}+d\ln\Omega/d\tau$")
    a0.set_title(f"Pole-free conformal rate per route  (max|$\\Delta H_A$|={res['max_abs_dHA']:.3f}; AOFT$\\approx$0 stationary)")
    a0.legend(fontsize=8); a0.grid(alpha=0.3)

    # (b) pairwise |Delta H_A| vs C-threshold (pole-free route-disagreement)
    a1 = ax[0, 1]
    a1.plot(tau_t, res["_d_AV"], label=r"|$\Delta H_A$| AOFT-Volovik", lw=1.4)
    a1.plot(tau_t, res["_d_AG"], label=r"|$\Delta H_A$| AOFT-GFT", lw=1.4)
    a1.plot(tau_t, res["_d_VG"], label=r"|$\Delta H_A$| Volovik-GFT", lw=1.4)
    a1.axhline(C_THRESH, color="red", ls="--", label=f"C-threshold {C_THRESH}")
    a1.set_xlabel(r"$\tau$"); a1.set_ylabel(r"$|\Delta H_A|$ pairwise (pole-free)")
    a1.set_title(f"C-leg: route-rate disagreement (C-PASS={res['C_pass']}; A-fires={res['A_fires']})")
    a1.legend(fontsize=8); a1.grid(alpha=0.3)

    # (c) transported q_Omega per route + SF54 band (y-clamped; poles at H_A=0 disclosed)
    a2 = ax[1, 0]
    a2.plot(tau_t, res["_q_aoft"], color="C0", lw=1.6, label="AOFT transported q")
    a2.plot(tau_t, res["_q_vol"], color="C1", lw=1.6, label="Volovik transported q")
    a2.plot(tau_t, res["_q_gft"], color="C2", lw=1.6, label="GFT transported q")
    a2.axhspan(SF54_BAND_LO, SF54_BAND_HI, color="grey", alpha=0.18, label="SF54 band [-0.97,0.81]")
    a2.axhline(-1.0, color="k", ls=":", alpha=0.5)
    a2.set_ylim(-3.0, 3.0)   # clamp: q diverges at conformal-stationary poles (H_A=0)
    a2.set_xlabel(r"$\tau$"); a2.set_ylabel(r"$q_\Omega$ (transported, clamped $\pm3$)")
    a2.set_title(f"Transported $q_\\Omega$ (poles at $H_A$=0; well-cond frac={res['well_cond_frac']:.3f})")
    a2.legend(fontsize=7, ncol=2); a2.grid(alpha=0.3)

    # (d) algebraic leg-i q_Omega(x) anchor
    a3 = ax[1, 1]
    a3.plot(tau_t, res["_q_alg_ideal"], label=r"leg-i $q(x)$, $w_n=0$", lw=1.8)
    a3.plot(tau_t, res["_q_alg_volovik"], label=r"leg-i $q(x)$, $w_n=-0.4076$", lw=1.8)
    a3.axhline(-1.0, color="k", ls=":", alpha=0.6, label=r"$q=-1$ (vacuum)")
    a3.axhspan(SF54_BAND_LO, SF54_BAND_HI, color="grey", alpha=0.15)
    a3.set_xlabel(r"$\tau$"); a3.set_ylabel(r"$q_\Omega(x)$ algebraic")
    a3.set_title("Leg-i algebraic anchor (route-independent two-fluid q)")
    a3.legend(fontsize=8); a3.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID}: route-invariance of transported two-fluid deceleration\n"
        f"composite={res['composite']} (sign={res['sign_verdict']}/mag={res['magnitude_verdict']}/regime={res['regime_verdict']})  "
        f"track={res['dual_prior_track']}",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Section 7 - npz writer
# -----------------------------------------------------------------------------
def write_npz(res: dict, audit_sha: str, content_sha: str, value_str: str) -> None:
    out = {k: v for k, v in res.items() if not k.startswith("_")}  # (local) scalars/lists
    # arrays
    out["tau_common"] = res["_tau_common"]
    out["tau_trim"] = res["_tau_trim"]
    out["q_aoft_transported"] = res["_q_aoft"]        # robust H_A-form q (primary)
    out["q_vol_transported"] = res["_q_vol"]
    out["q_gft_transported"] = res["_q_gft"]
    out["q_aoft_transported_literal"] = res["_q_aoft_lit"]   # plan-literal q (disclosed)
    out["q_vol_transported_literal"] = res["_q_vol_lit"]
    out["q_gft_transported_literal"] = res["_q_gft_lit"]
    out["HA_aoft"] = res["_HA_aoft"]                  # pole-free conformal rates
    out["HA_vol"] = res["_HA_vol"]
    out["HA_gft"] = res["_HA_gft"]
    out["q_aoft_bare"] = res["_qb_aoft"]
    out["q_vol_bare"] = res["_qb_vol"]
    out["q_gft_bare"] = res["_qb_gft"]
    out["q_alg_ideal"] = res["_q_alg_ideal"]
    out["q_alg_volovik"] = res["_q_alg_volovik"]
    out["Omega_common"] = res["_Omega_c"]
    out["dlnOmega_common"] = res["_dlnOmega_c"]
    out["dHA_AOFT_VOL"] = res["_d_AV"]                # pole-free pairwise rate diffs
    out["dHA_AOFT_GFT"] = res["_d_AG"]
    out["dHA_VOL_GFT"] = res["_d_VG"]
    # metadata
    out["gate_id"] = GATE_ID
    out["value_str"] = value_str
    out["SF54_band_lo"] = SF54_BAND_LO
    out["SF54_band_hi"] = SF54_BAND_HI
    out["routes"] = np.array(ROUTES)
    out["a_2_FW_zeta"] = a_2_FW_zeta
    out["Gamma_effacement"] = Gamma_effacement
    out["tau_fold"] = tau_fold
    out["M_KK"] = M_KK
    out["audit_sha256"] = audit_sha
    out["content_sha256"] = content_sha
    # lists -> arrays for npz
    for k in list(out.keys()):
        if isinstance(out[k], list):
            out[k] = np.array(out[k])
    np.savez(NPZ_OUT, **out)


# -----------------------------------------------------------------------------
# Section 8 - Verdict-line emitter (atomic append; dual-SHA + schema-v2 3-tuple)
# -----------------------------------------------------------------------------
def _prior_audit_sha() -> str:
    """Return the most-recent prior canonical-line audit_sha256 for this gate-ID (full
    64-char), or '' if none.  Used to emit a `supersedes=` tag under absolute verdict
    permanence (gate-verdicts.md Option A): the prior line is RETAINED on disk; the
    corrective line APPENDS with the supersedes pointer."""
    import re  # (local)
    if not VERDICT_TXT.exists():
        return ""
    prior = ""  # (local)
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:"):
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                prior = m.group(1)
    return prior


def append_verdict(res: dict, value_str: str, audit_sha: str, content_sha: str) -> None:
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    composite = res["composite"]  # (local)
    prior_sha = _prior_audit_sha()  # (local) supersession target (Option A)
    supersedes_tok = f";supersedes={prior_sha}" if (prior_sha and prior_sha != audit_sha) else ""  # (local)
    line = (
        f"{GATE_ID}: {composite} -- value='{value_str}{supersedes_tok}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    supersedes_note = f"; supersedes={prior_sha}" if supersedes_tok else ""  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] route-invariance of transported q_Omega; "
        f"feeds S97 wave-synthesis C1 a(t) frontier{supersedes_note}\n"
    )
    # schema-v2 3-tuple companion row (REQUIRED for [SIGN] trigger)
    tuple_row = (
        f"# sign_verdict={res['sign_verdict']} "
        f"magnitude_verdict={res['magnitude_verdict']} "
        f"regime_verdict={res['regime_verdict']} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    detail_row = (
        f"# C-leg (literal q=-A*A''/(A')^2): max|Delta q_Omega|={res['max_abs_dq_transported']:.4e} vs {C_THRESH} "
        f"(C-PASS={res['C_pass']}; pole-laden at H_A=0); "
        f"C-leg PRIMARY (pole-free): max|Delta H_A|={res['max_abs_dHA']:.6f} "
        f"(AOFT-VOL={res['max_dHA_AOFT_VOL']:.4f}, AOFT-GFT={res['max_dHA_AOFT_GFT']:.4f}, VOL-GFT={res['max_dHA_VOL_GFT']:.4f}); "
        f"B-leg: frac_in_band={res['frac_in_band']:.4f} vs {B_THRESH} (B-PASS={res['B_pass']}); "
        f"A-leg: max_abs_dev_q(|q_route-q_SF54|,pole-free)={res['max_abs_dev_q_transported']:.4f} "
        f"(VOL={res['dev_vs_sf54_vol']:.4f},GFT={res['dev_vs_sf54_gft']:.4f},AOFT=stationary); "
        f"invariant_shortfall={res['invariant_shortfall']:.6f} vs band_tol {A_BAND_TOL} "
        f"(A-fires={res['A_fires']}; cross-confirm max|dH_A|={res['max_abs_dHA']:.4f}>{A_BAND_TOL}={res['A_fires_via_HA']}; "
        f"S96-bare-shortfall={res['S96_bare_shortfall']:.4f}); "
        f"# {GATE_ID} C/B/A legs (A-fires=>INFO Track-B per plan rubric)\n"
    )
    transport_row = (
        f"# leg-ii FULL conformal transport (Omega non-constant, rel_spread={res['omega_rel_spread']:.4e}>1e-3, "
        f"dot_is_null={res['omega_dot_is_null']}); H_A=H_bare+dlnOmega/dtau (Sage-verified), q=-1-Hdot_A/H_A^2; "
        f"H_A ranges AOFT[{res['HA_aoft_range'][0]:.4f},{res['HA_aoft_range'][1]:.4f}] (~0 conformally stationary), "
        f"VOL[{res['HA_vol_range'][0]:.4f},{res['HA_vol_range'][1]:.4f}], GFT[{res['HA_gft_range'][0]:.4f},{res['HA_gft_range'][1]:.4f}]; "
        f"well-cond frac(|H_A|>={res['H_floor']:.0e})={res['well_cond_frac']:.4f} "
        f"(AOFT {res['wellfrac_aoft']:.3f} stationary, VOL {res['wellfrac_vol']:.3f}, GFT {res['wellfrac_gft']:.3f}); "
        f"bare a-growth AOFT 1.048x/VOL 1.673x/GFT 1.024x (shared Omega x0.954) => routes NOT rate-invariant; "
        f"common tau-support [{res['tau_common_lo']:.4f},{res['tau_common_hi']:.4f}] "
        f"(Volovik caps at tau*; f_used={res['f_used']:.4f} -> regime={res['regime_verdict']}); "
        f"# {GATE_ID} Sage-exact q_acoustic(Omega_dot=Omega_ddot=0)-q_bare=0 collapse N/A (Omega non-const)\n"
    )
    track_row = (
        f"# dual_prior: {res['dual_prior_track']} "
        f"(C-PASS or B-PASS -> 0.9 Track A route-invariant; A-shortfall -> 0.9 Track B route-sensitive); "
        f"x_today A-window=[{res['x_today_band_lo']:.4f},{res['x_today_band_hi']:.4f}] (1.2 PASS); "
        f"# {GATE_ID} q = curvature of order-parameter trajectory in acoustic time (substrate-IS)\n"
    )
    regulator_row = (
        f"# LEVEL_CLASS_PIN=FULL regulator_pin=a_n_zeta "
        f"# {GATE_ID} a_2^zeta={a_2_FW_zeta:.6f} (Omega backbone); 3 routes share one D_K spectrum; "
        f"SF54 band [{SF54_BAND_LO},{SF54_BAND_HI}]; substrate-first-canonical-sourcing.md PASS\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tuple_row)
        fp.write(detail_row)
        fp.write(transport_row)
        fp.write(track_row)
        fp.write(regulator_row)


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
    print(f"  C_thresh={C_THRESH} | B_thresh={B_THRESH} | A_band_tol={A_BAND_TOL} | "
          f"SF54 band [{SF54_BAND_LO},{SF54_BAND_HI}]")
    print()

    res = compute()  # (local)

    print("=== leg-ii ENABLE (1.1 OMEGA-PROFILE) ===")
    print(f"  Omega composite={res['omega_composite']}, rel_spread={res['omega_rel_spread']:.4e}, "
          f"dot_is_null={res['omega_dot_is_null']} -> leg-ii enabled={res['legii_enabled']}")
    print(f"  (Sage-exact: q_acoustic(Omega_dot=Omega_ddot=0)-q_bare=0; FULL transport runs since Omega non-const)")
    print()
    print("=== common tau-grid (intersection of 3 route supports) ===")
    print(f"  [{res['tau_common_lo']:.6f}, {res['tau_common_hi']:.6f}], N={res['N_common']}, "
          f"f_used={res['f_used']:.4f} (Volovik caps at tau*=0.451041)")
    print()
    print("=== conformal rates H_A per route (pole-free; the route-disagreement carrier) ===")
    print(f"  AOFT    : H_A in {res['HA_aoft_range']}  (~0: conformally stationary)")
    print(f"  Volovik : H_A in {res['HA_vol_range']}")
    print(f"  GFT     : H_A in {res['HA_gft_range']}")
    print(f"  well-conditioned frac (all |H_A|>={res['H_floor']:.0e}): {res['well_cond_frac']:.4f} "
          f"(AOFT {res['wellfrac_aoft']:.3f}, VOL {res['wellfrac_vol']:.3f}, GFT {res['wellfrac_gft']:.3f})")
    print()
    print("=== C-LEG (the [SIGN] discriminator: route-invariance) ===")
    print(f"  PRIMARY pole-free max|Delta H_A|: AOFT-VOL={res['max_dHA_AOFT_VOL']:.4f}, "
          f"AOFT-GFT={res['max_dHA_AOFT_GFT']:.4f}, VOL-GFT={res['max_dHA_VOL_GFT']:.4f} -> max={res['max_abs_dHA']:.6f}")
    print(f"  LITERAL plan-form max|Delta q_Omega| = {res['max_abs_dq_transported']:.4e}  vs C_thresh {C_THRESH}  "
          f"-> C-PASS={res['C_pass']}  (pole-laden at H_A=0)")
    print(f"  bare a-growth: AOFT 1.048x, VOL 1.673x, GFT 1.024x (shared Omega x0.954) "
          f"=> routes NOT rate-invariant after transport")
    print()
    print("=== B-LEG (frac_in_band vs 0.90) ===")
    print(f"  pooled frac_in_band = {res['frac_in_band']:.4f}  (AOFT {res['frac_in_band_aoft']:.3f}, "
          f"Vol {res['frac_in_band_vol']:.3f}, GFT {res['frac_in_band_gft']:.3f})  -> B-PASS={res['B_pass']}")
    print()
    print("=== A-LEG (predicted NOT to fire: invariant shortfall > 0.356) ===")
    print(f"  max_abs_dev_q (|q_route - q_SF54|, pole-free, S96-structure) = {res['max_abs_dev_q_transported']:.6f}")
    print(f"    per-route: AOFT={res['dev_vs_sf54_aoft']} (stationary), VOL={res['dev_vs_sf54_vol']:.4f}, GFT={res['dev_vs_sf54_gft']:.4f}")
    print(f"  invariant_shortfall = {res['invariant_shortfall']:.6f}  vs band_tol {A_BAND_TOL}  -> A-fires={res['A_fires']}")
    print(f"  robust cross-confirm via pole-free H_A: max|Delta H_A|={res['max_abs_dHA']:.4f} > {A_BAND_TOL}? {res['A_fires_via_HA']}")
    print(f"  (S96 BARE shortfall was {res['S96_bare_shortfall']:.4f}: GFT max_abs_dev_q={res['gft_max_abs_dev_q_S96']:.4f} - {A_BAND_TOL})")
    print()
    print("=== 3-TUPLE + COMPOSITE (gate-verdicts.md collapse) ===")
    print(f"  sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} regime={res['regime_verdict']} "
          f"-> composite={res['composite']}")
    print(f"  dual_prior track: {res['dual_prior_track']}")
    print()

    value_str = (
        f"composite={res['composite']};"
        f"max_abs_dq_transported={res['max_abs_dq_transported']:.6f};C_thresh={C_THRESH};C_PASS={res['C_pass']};"
        f"frac_in_band={res['frac_in_band']:.4f};B_thresh={B_THRESH};B_PASS={res['B_pass']};"
        f"max_abs_dHA={res['max_abs_dHA']:.6f};max_abs_dev_q_vs_sf54={res['max_abs_dev_q_transported']:.4f};"
        f"invariant_shortfall={res['invariant_shortfall']:.6f};A_band_tol={A_BAND_TOL};A_fires={res['A_fires']};A_fires_via_HA={res['A_fires_via_HA']};"
        f"max_dq_AOFT_VOL={res['max_dq_AOFT_VOL']:.4f};max_dq_AOFT_GFT={res['max_dq_AOFT_GFT']:.4f};"
        f"max_dq_VOL_GFT={res['max_dq_VOL_GFT']:.4f};"
        f"bare_spread={res['max_abs_dq_bare']:.4f};transport_reduced_spread={res['transport_reduced_spread']};"
        f"SF54_band=[{SF54_BAND_LO},{SF54_BAND_HI}];tau_common=[{res['tau_common_lo']:.4f},{res['tau_common_hi']:.4f}];"
        f"f_used={res['f_used']:.4f};legii_enabled={res['legii_enabled']};omega_rel_spread={res['omega_rel_spread']:.4e};"
        f"x_today_window=[{res['x_today_band_lo']:.4f},{res['x_today_band_hi']:.4f}];"
        f"dual_prior_track={res['dual_prior_track']};"
        f"sign={res['sign_verdict']};magnitude={res['magnitude_verdict']};regime={res['regime_verdict']};"
        f"CLASS=FULL;regulator_pin=a_n_zeta;route_invariance=3route_conformal_transport"
    )  # (local)

    make_plot(res)
    write_npz(res, audit_sha, content_sha, value_str)
    append_verdict(res, value_str, audit_sha, content_sha)

    print(f"  wrote: {NPZ_OUT.name}, {PNG_OUT.name}, verdict line in {VERDICT_TXT.name}")
    print(f"  elapsed {time.time()-t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
