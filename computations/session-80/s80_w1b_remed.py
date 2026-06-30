#!/usr/bin/env python3
"""
S80-W0-1 / S80-W1-B-REMED -- PRU-Spec Clean Re-Run of W1-B F_amp Independence

Agent: nazarewicz-nuclear-structure-theorist
Gate: S80-W1-B-REMED  ([AUDIT] trigger)
Classification: GEOMETRIC + PHONONIC
Scheme tag: SDW (Seeley-DeWitt convention, canonical, L_max=5 nominal)

-------------------------------------------------------------------
PRU (Pre-Registration Underspecification) Discipline
-------------------------------------------------------------------
Per .claude/rules/epistemic-discipline.md (Class 8) and S79 P1-3 closer,
this script runs the W1-B F_amp independence verification ONCE under a
fully pre-registered machinery specification. Every free parameter is
pinned BEFORE compute and logged as the first 20 lines of stdout.

The S78 iteration history
  1st run: rel_diff = 45.15% (FAIL by original < 20% threshold)
  Iterations 2-8: rel_diff in {9.94, 17.21, 17.21, 5.83, 6.30, 6.30, 6.30}%
was the PRU Class 8 signature: plan left machinery parameters
(N_eval offset, Hankel order convention, epsilon-scan window, integrator
max_step) unpinned. Execution-time freedom produced multi-iteration
verdict-log floatation.

S80 Pre-Registration (all FROZEN below, never varied at runtime):
  1. SHA-256 of canonical_constants.py (source of M_Pl_reduced, PI)
  2. SHA-256 of this script
  3. SHA-256 of s78_norm_indep_verify.py (predecessor reference)
  4. Hankel formula order fixed: F_amp_A = (Gamma(nu)/Gamma(3/2))^2 * 2^(2nu - 3)
     with nu = 3/2 + eps_pivot + 0.5 * eta_H (single evaluation, no scan)
  5. epsilon-scan range PRE-REGISTERED: [EPS0, EPS0] (single value 0.01 -- no scan)
  6. Import closure hash = SHA-256(canonical_constants.py || s78_norm_indep_verify.py)
  7. N_eval = N_pivot + 3 (fixed)
  8. Integration pins: DOP853, rtol=1e-10, atol=1e-12, max_step=0.01, X_BD_IC=100
  9. k-grid pin: single k = aH(N_PIVOT_TARGET=3.0), logged with SHA of np.array([k])
  10. Slow-roll background: EPS0=0.01, ETA_H_BG=0.08, N_TOTAL=8.0

RUN ONCE. Do NOT iterate on any parameter.

-------------------------------------------------------------------
Gate Semantics
-------------------------------------------------------------------
S78 printed "F_amp agreement = X%" where X = rel_diff_percent.
The S80 plan reads "PASS if F_amp agreement >= 60%" (higher = better),
which INVERTS the S78 convention. Mapping:

  agreement_pct = 100 * (1 - rel_diff)
  PASS: agreement_pct >= 60  (equivalently rel_diff <= 0.40)
  INFO: agreement_pct in [40, 60]  (rel_diff in [0.40, 0.60])
  FAIL: agreement_pct < 40  (rel_diff > 0.60)

This reading is consistent with plan text "recovering above the INFO-band
into PASS" (single frozen run should land EITHER above INFO or structurally
below it). Under PRU-free conditions, a converged mode-function verification
should yield rel_diff consistent with slow-roll O(epsilon) truncation
(residuals ~ 5-20% for eps0 = 0.01, eta_H = 0.08), placing agreement_pct
most likely in [80, 95] bracket.

-------------------------------------------------------------------
Substrate Framing
-------------------------------------------------------------------
The mode equation u_k'' + (k^2 - z''/z) u_k = 0 describes the linearized
dynamics of a fiber excitation on the D_K-spectral fabric during the
Jensen-deformation-driven transit. "a(N)", "H(N)" are shorthands for
the a_2 Seeley-DeWitt coefficient's evolution -- space IS the fabric's
spectral weight distribution, not a container. "Horizon crossing" is
the spectral degeneracy k = (aH) at which the mode's wavenumber matches
the instantaneous inverse coherence scale. F_amp is a power ratio
between two fiber-excitation normalizations -- it is dimensionless,
scheme-independent by construction, and IS a phononic observable.

Classification: PHONONIC + GEOMETRIC
  - PHONONIC: F_amp normalizes curvature-perturbation power spectrum,
    which in the substrate picture is the P_zeta(k) power of acoustic
    GGE excitations after the fold.
  - GEOMETRIC: The z''/z potential is constructed from a_2 via
    d ln z^2 / dN = 2 + d ln eps / dN, so the mode-equation potential
    is a functional of the spectral triple.

-------------------------------------------------------------------
Output contract (plan lines 133-138):
  - computations/session-80/s80_w1b_remed.py       (this file)
  - computations/session-80/s80_w1b_remed.npz
  - computations/session-80/s80_w1b_remed.png
  - Results block in sessions/archive/session-80/session-80-results-workingpaper.md W0-1
  - Appended verdict line in computations/session-80/s80_gate_verdicts.txt

Written by nazarewicz-nuclear-structure-theorist, S80 W0-1.
"""

from __future__ import annotations

import os
import sys
import hashlib
import time

import numpy as np
import scipy.special as sp
from scipy.integrate import solve_ivp
from scipy.special import gamma as _gamma
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# MANDATORY: canonical constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import M_Pl_reduced, PI

# ------------------------------------------------------------------
# SECTION 1: PRU PIN REGISTRATION -- all machinery FROZEN below
# ------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Pre-registered frozen machinery (treated as constants for this run):
N_PIVOT_TARGET = 3.0                # (local) pre-reg: horizon crossing e-fold
EPS0_PIN = 1.0e-2                   # (local) pre-reg: slow-roll eps at N=0
ETA_H_PIN = 8.0e-2                  # (local) pre-reg: d ln eps / dN
N_TOTAL_PIN = 8.0                   # (local) pre-reg: integration window size
H0_PIN = 1.0                        # (local) pre-reg: dimensionless Hubble norm
X_BD_IC_PIN = 100.0                 # (local) pre-reg: BD IC at k/(aH) = 100
N_EVAL_OFFSET_PIN = 3.0             # (local) pre-reg: N_eval = N_pivot + this
N_END_PIN = 7.5                     # (local) pre-reg: super-horizon eval
RTOL_PIN = 1.0e-10                  # (local) pre-reg: integrator rtol
ATOL_PIN = 1.0e-12                  # (local) pre-reg: integrator atol
MAX_STEP_PIN = 0.01                 # (local) pre-reg: integrator max_step
EPS_SCAN_RANGE = (EPS0_PIN, EPS0_PIN)   # (local) pre-reg: NO scan, single value
L_MAX_TAG = 5                       # (local) nominal 4-tuple tag per plan
WKB_BOUND = 0.3                     # (local) pre-reg: WKB cross-check threshold

# Gate thresholds (pre-registered, plan lines 102-104):
PASS_AGREEMENT_PCT = 60.0           # (local) pre-reg: agreement >= 60 -> PASS
INFO_LOW_PCT = 40.0                 # (local) pre-reg: agreement in [40,60] -> INFO


def sha256_of_file(path):
    """Return SHA-256 hex digest of file bytes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_array(arr):
    """Return SHA-256 hex digest of numpy array bytes + shape + dtype string."""
    h = hashlib.sha256()
    h.update(str(arr.shape).encode())
    h.update(str(arr.dtype).encode())
    h.update(arr.tobytes())
    return h.hexdigest()


# ------------------------------------------------------------------
# SECTION 2: Background kinematics (FROZEN functions of pinned parameters)
# ------------------------------------------------------------------

def eps_of_N(N):
    """Slow-roll eps(N) = EPS0_PIN * exp(ETA_H_PIN * N)."""
    return EPS0_PIN * np.exp(ETA_H_PIN * np.asarray(N, dtype=float))


def eta_H_of_N(N):
    """eta_H = d ln eps / dN = ETA_H_PIN (constant)."""
    return np.full_like(np.asarray(N, dtype=float), ETA_H_PIN)


def H_of_N(N):
    """H(N)/H0 = exp(-integral_0^N eps(N') dN')."""
    N = np.asarray(N, dtype=float)
    if abs(ETA_H_PIN) < 1e-12:
        integral = EPS0_PIN * N                                          # (local)
    else:
        integral = EPS0_PIN / ETA_H_PIN * (np.exp(ETA_H_PIN * N) - 1.0)  # (local)
    return H0_PIN * np.exp(-integral)


def a_of_N(N):
    """Scale factor a(N) = exp(N)."""
    return np.exp(np.asarray(N, dtype=float))


def aH_of_N(N):
    """Comoving inverse horizon a*H."""
    return a_of_N(N) * H_of_N(N)


def find_N_BD_IC(k):
    """Solve k/(aH) = X_BD_IC_PIN for N (bisection)."""
    N_lo, N_hi = -5.0, 8.0                                               # (local) bisection bracket
    for _ in range(200):
        N_mid = 0.5 * (N_lo + N_hi)
        if k / aH_of_N(N_mid) > X_BD_IC_PIN:
            N_lo = N_mid
        else:
            N_hi = N_mid
    return 0.5 * (N_lo + N_hi)


def find_N_horizon(k):
    """Solve k/(aH) = 1 for N_pivot (bisection)."""
    N_lo, N_hi = -5.0, 8.0                                               # (local) bisection bracket
    for _ in range(200):
        N_mid = 0.5 * (N_lo + N_hi)
        if k / aH_of_N(N_mid) > 1.0:
            N_lo = N_mid
        else:
            N_hi = N_mid
    return 0.5 * (N_lo + N_hi)


# ------------------------------------------------------------------
# SECTION 3: Method A -- analytic Hankel matching (PINNED nu, PINNED formula order)
# ------------------------------------------------------------------

def method_A_hankel_pinned(k, N_pivot):
    """F_amp_A from Hankel matching with nu PINNED pre-run.

    Pinned formula: F_amp_A = (Gamma(nu) / Gamma(3/2))^2 * 2^(2 nu - 3)
    where nu = 3/2 + eps_pivot + 0.5 * eta_H_pivot (single evaluation).
    No scan, no second-order terms, no post-hoc reformulations.
    """
    eps_pivot = float(eps_of_N(N_pivot))                                 # (local)
    eta_H_pivot = ETA_H_PIN                                              # (local) constant
    nu = 1.5 + eps_pivot + 0.5 * eta_H_pivot                             # (local) PINNED
    amp_ratio = (_gamma(nu) / _gamma(1.5))**2                            # (local)
    hankel_factor = 2.0 ** (2.0 * nu - 3.0)                              # (local) 2^(2 nu - 3) per PRU pin
    F_amp_A = amp_ratio * hankel_factor                                  # (local)
    n_s_minus_1 = 2.0 * eta_H_pivot - 4.0 * eps_pivot                    # (local) slow-roll tilt
    return {
        "F_amp_A": float(F_amp_A),
        "nu": float(nu),
        "amp_ratio": float(amp_ratio),
        "hankel_factor": float(hankel_factor),
        "n_s_minus_1": float(n_s_minus_1),
        "eps_pivot": float(eps_pivot),
        "eta_H_pivot": float(eta_H_pivot),
    }


# ------------------------------------------------------------------
# SECTION 4: Method B -- R-perturbation in e-folds with explicit Hubble friction
# ------------------------------------------------------------------

def method_B_integrate(k, N_start, N_end):
    """Method B: coupled first-order ODE for R = u/z.

    Equation: d2R/dN2 + (3 + eta_H) dR/dN + (k/(aH))^2 R = 0.
    BD IC: R = (1/sqrt(2k))/z at N_start; dR/dN = -R * (1 + 0.5 eta_H + i x).
    State vector: y = [Re R, Im R, Re dR/dN, Im dR/dN].
    """
    def rhs(N, y):
        R_re, R_im, Rp_re, Rp_im = y
        eta_N = eta_H_of_N(N)
        x = k / aH_of_N(N)
        coef = 3.0 + eta_N
        d2R_re = -coef * Rp_re - x**2 * R_re
        d2R_im = -coef * Rp_im - x**2 * R_im
        return [Rp_re, Rp_im, d2R_re, d2R_im]

    z0 = a_of_N(N_start) * np.sqrt(2.0 * eps_of_N(N_start))              # (local)
    u_amp = 1.0 / np.sqrt(2.0 * k)                                       # (local) BD amplitude
    R_amp = u_amp / z0                                                   # (local)
    R_re0 = R_amp                                                        # (local) phase 0
    R_im0 = 0.0                                                          # (local) phase 0
    x0 = k / aH_of_N(N_start)                                            # (local)
    eta_N0 = float(eta_H_of_N(N_start))                                  # (local)
    factor = 1.0 + 0.5 * eta_N0                                          # (local)
    dR_re0 = -R_re0 * factor + R_im0 * x0                                # (local)
    dR_im0 = -R_im0 * factor - R_re0 * x0                                # (local)

    y0 = [R_re0, R_im0, dR_re0, dR_im0]
    sol = solve_ivp(
        rhs, (N_start, N_end), y0,
        method="DOP853", rtol=RTOL_PIN, atol=ATOL_PIN,
        dense_output=True, max_step=MAX_STEP_PIN,
    )
    return sol


# ------------------------------------------------------------------
# SECTION 5: Cross-check -- Wronskian conservation
# ------------------------------------------------------------------

def wronskian_drift(sol, k):
    """Relative drift of (a^3 eps) * Im(R* dR/dN) over the integration.

    This is the Mukhanov-Sasaki conserved Wronskian (in R-parameterization).
    Any drift is integrator error, independent of slow-roll truncation.
    """
    N_check = np.linspace(sol.t[0], sol.t[-1], 1001)                     # (local)
    y = sol.sol(N_check)
    R = y[0] + 1j * y[1]
    dR = y[2] + 1j * y[3]
    a3eps = np.array([a_of_N(n)**3 * eps_of_N(n) for n in N_check])      # (local)
    W = a3eps * np.imag(np.conj(R) * dR)                                 # (local)
    drift = (W.max() - W.min()) / (np.abs(W.mean()) + 1e-30)             # (local)
    return float(drift)


# ------------------------------------------------------------------
# SECTION 6: MAIN -- single-shot run under PRU pins
# ------------------------------------------------------------------

def main():
    t0 = time.time()                                                     # (local)

    # --- Compute PRU hashes and closure hash BEFORE any physics run ---
    this_script = os.path.abspath(__file__)                              # (local)
    cc_path = os.path.join(SCRIPT_DIR, "canonical_constants.py")         # (local)
    s78_path = os.path.join(SCRIPT_DIR, "s78_norm_indep_verify.py")      # (local)

    sha_this = sha256_of_file(this_script)
    sha_cc = sha256_of_file(cc_path)
    sha_s78 = sha256_of_file(s78_path)
    # Import closure hash = hash of concatenation of all imported module bytes
    h_closure = hashlib.sha256()
    with open(cc_path, "rb") as f:
        h_closure.update(f.read())
    with open(s78_path, "rb") as f:
        h_closure.update(f.read())
    sha_closure = h_closure.hexdigest()

    # --- Pre-compute k-grid pin (single k, but hash the array anyway) ---
    K_PHYS = float(aH_of_N(N_PIVOT_TARGET))                              # (local)
    k_grid = np.array([K_PHYS])                                          # (local)
    sha_k = sha256_of_array(k_grid)

    # --- FIRST 20 LINES of output: pre-registered PRU pin dump ---
    print(f"=== S80-W1-B-REMED PRU PIN REGISTRY (pre-run, frozen) ===")     # 1
    print(f"gate_id = S80-W1-B-REMED  (trigger=AUDIT)")                    # 2
    print(f"scheme = SDW  convention = canonical  L_max_tag = {L_MAX_TAG}")  # 3
    print(f"sha256(s80_w1b_remed.py)      = {sha_this}")                   # 4
    print(f"sha256(canonical_constants.py) = {sha_cc}")                    # 5
    print(f"sha256(s78_norm_indep_verify.py)= {sha_s78}")                  # 6
    print(f"sha256(import_closure)        = {sha_closure}")                # 7
    print(f"sha256(k_grid)                = {sha_k}")                      # 8
    print(f"k_grid = {k_grid.tolist()}  (single value)")                   # 9
    print(f"Hankel formula = 2^(2*nu - 3),  nu = 3/2 + eps_pivot + 0.5*eta_H")  # 10
    print(f"eps-scan range (pre-reg, NO scan) = {EPS_SCAN_RANGE}")         # 11
    print(f"N_eval offset = N_pivot + {N_EVAL_OFFSET_PIN}")                # 12
    print(f"Background: EPS0={EPS0_PIN}, ETA_H={ETA_H_PIN}, N_TOTAL={N_TOTAL_PIN}, H0={H0_PIN}")  # 13
    print(f"Integrator: DOP853, rtol={RTOL_PIN}, atol={ATOL_PIN}, max_step={MAX_STEP_PIN}")  # 14
    print(f"BD IC pin: k/(aH) = {X_BD_IC_PIN}")                            # 15
    print(f"N_PIVOT_TARGET = {N_PIVOT_TARGET}  (horizon crossing e-fold)")  # 16
    print(f"Gate thresholds: PASS >= {PASS_AGREEMENT_PCT}%, INFO [{INFO_LOW_PCT},{PASS_AGREEMENT_PCT})%, FAIL < {INFO_LOW_PCT}%")  # 17
    print(f"agreement_pct definition: 100 * (1 - rel_diff),  rel_diff = |F_B - F_A| / (0.5*(F_B + F_A))")  # 18
    print(f"RUN COUNT = 1  (single pre-registered pass, no iteration)")   # 19
    print(f"=== END PRU PIN REGISTRY ===")                                 # 20
    print()

    # --- Single-shot physics run under frozen pins ---
    print(f"k_physical = {K_PHYS:.6f}  (= aH at N = {N_PIVOT_TARGET})")
    N_pivot_scalar = find_N_horizon(K_PHYS)
    N_start = find_N_BD_IC(K_PHYS)
    N_eval = N_pivot_scalar + N_EVAL_OFFSET_PIN                           # (local) pinned
    print(f"N_start (BD IC, k/aH = {X_BD_IC_PIN}) = {N_start:.6f}")
    print(f"N_pivot (horizon, k/aH = 1)       = {N_pivot_scalar:.6f}")
    print(f"N_eval  (N_pivot + {N_EVAL_OFFSET_PIN})                 = {N_eval:.6f}")
    print(f"N_end   (super-horizon eval)      = {N_END_PIN}")
    print()

    # Method A (Hankel matching, pinned nu and formula order)
    resA = method_A_hankel_pinned(K_PHYS, N_pivot_scalar)
    print(f"--- Method A (Hankel matching, pinned) ---")
    print(f"  eps_pivot       = {resA['eps_pivot']:.6e}")
    print(f"  eta_H_pivot     = {resA['eta_H_pivot']:.6e}")
    print(f"  nu              = {resA['nu']:.6f}")
    print(f"  amp_ratio       = (Gamma(nu)/Gamma(3/2))^2 = {resA['amp_ratio']:.6f}")
    print(f"  hankel_factor   = 2^(2 nu - 3)          = {resA['hankel_factor']:.6f}")
    print(f"  F_amp_A         = {resA['F_amp_A']:.6e}")
    print(f"  n_s - 1 (diag)  = {resA['n_s_minus_1']:.6f}")
    print()

    # Method B (numerical integration)
    sol = method_B_integrate(K_PHYS, N_start, N_END_PIN)
    print(f"--- Method B (R in e-folds, explicit friction) ---")
    print(f"  integrator status: {sol.status} ({sol.message})")
    print(f"  integration points: {len(sol.t)}")
    y_eval = sol.sol(N_eval)
    R_eval = y_eval[0] + 1j * y_eval[1]
    H_pivot = float(H_of_N(N_pivot_scalar))                               # (local)
    eps_pivot_v = float(eps_of_N(N_pivot_scalar))                         # (local)
    mag_R2_num = float(np.abs(R_eval)**2)                                 # (local)
    mag_R2_BD = (H_pivot**2) / (4.0 * eps_pivot_v * K_PHYS**3)            # (local)
    F_amp_B = mag_R2_num / mag_R2_BD                                      # (local)
    print(f"  |R(N_eval)|^2 numeric  = {mag_R2_num:.6e}")
    print(f"  |R|^2 BD reference     = {mag_R2_BD:.6e}")
    print(f"  F_amp_B                = {F_amp_B:.6e}")

    W_drift = wronskian_drift(sol, K_PHYS)
    print(f"  Wronskian drift        = {W_drift:.6e}  (integrator error proxy)")
    print()

    # --- Substitution chain for the PASS/INFO/FAIL decision ---
    # Step 1: rel_diff definition
    rel_diff = abs(F_amp_B - resA["F_amp_A"]) / (0.5 * (F_amp_B + resA["F_amp_A"]))  # (local)
    # Step 2: agreement_pct definition (inverts rel_diff into "higher is better")
    agreement_pct = 100.0 * (1.0 - rel_diff)                              # (local)
    # Step 3: Python verification of substitution
    print(f"--- Substitution chain (for [AUDIT] trigger) ---")
    print(f"  Step 1 (def): rel_diff = |F_B - F_A| / (0.5 * (F_B + F_A))")
    print(f"                         = |{F_amp_B:.6e} - {resA['F_amp_A']:.6e}| / (0.5 * ({F_amp_B:.6e} + {resA['F_amp_A']:.6e}))")
    print(f"                         = {rel_diff:.6f}")
    print(f"  Step 2 (def): agreement_pct = 100 * (1 - rel_diff)")
    print(f"                              = 100 * (1 - {rel_diff:.6f})")
    print(f"                              = {agreement_pct:.6f}%")
    print(f"  Step 3 (decision):")
    print(f"    if agreement_pct >= {PASS_AGREEMENT_PCT}% -> PASS")
    print(f"    if {INFO_LOW_PCT}% <= agreement_pct < {PASS_AGREEMENT_PCT}% -> INFO")
    print(f"    if agreement_pct < {INFO_LOW_PCT}% -> FAIL")
    print()

    # Decision (no adjustment, no iteration)
    if agreement_pct >= PASS_AGREEMENT_PCT:
        verdict = "PASS"
        verdict_reason = (
            f"Single PRU-pinned run: agreement = {agreement_pct:.2f}% "
            f">= {PASS_AGREEMENT_PCT}% threshold; rel_diff = {rel_diff*100:.2f}%. "
            f"PRU remediation RESTORES structural agreement above INFO-band. "
            f"Hypothesis (PRU Class 8 was root cause of S78 floatation) CONFIRMED."
        )
    elif agreement_pct >= INFO_LOW_PCT:
        verdict = "INFO"
        verdict_reason = (
            f"Single PRU-pinned run: agreement = {agreement_pct:.2f}% "
            f"in INFO-band [{INFO_LOW_PCT}, {PASS_AGREEMENT_PCT})%; rel_diff = {rel_diff*100:.2f}%. "
            f"PRU Class 8 confirmed: floatation not root-caused by parameter freedom "
            f"alone -- structural O(eps) Hankel-truncation residual remains. Do NOT retry."
        )
    else:
        verdict = "FAIL"
        verdict_reason = (
            f"Single PRU-pinned run: agreement = {agreement_pct:.2f}% "
            f"< {INFO_LOW_PCT}% threshold; rel_diff = {rel_diff*100:.2f}%. "
            f"STRUCTURAL failure under frozen inputs; UNIFIED-AS-79 ledger amendment required."
        )

    print(f"=== VERDICT: {verdict} ===")
    print(f"Reason: {verdict_reason}")
    print()

    # --- Save artifacts ---
    npz_path = os.path.join(SCRIPT_DIR, "s80_w1b_remed.npz")
    np.savez(
        npz_path,
        # PRU pins (all as arrays for npz compatibility)
        gate_id="S80-W1-B-REMED",
        scheme_tag="SDW",
        convention_tag="canonical",
        L_max_tag=L_MAX_TAG,
        sha_script=sha_this,
        sha_canonical_constants=sha_cc,
        sha_s78_predecessor=sha_s78,
        sha_import_closure=sha_closure,
        sha_k_grid=sha_k,
        k_grid=k_grid,
        # Pinned params
        EPS0_PIN=EPS0_PIN,
        ETA_H_PIN=ETA_H_PIN,
        N_PIVOT_TARGET=N_PIVOT_TARGET,
        N_EVAL_OFFSET=N_EVAL_OFFSET_PIN,
        N_END=N_END_PIN,
        X_BD_IC=X_BD_IC_PIN,
        RTOL=RTOL_PIN,
        ATOL=ATOL_PIN,
        MAX_STEP=MAX_STEP_PIN,
        H0=H0_PIN,
        # Physics
        k_physical=K_PHYS,
        N_start=N_start,
        N_pivot=N_pivot_scalar,
        N_eval=N_eval,
        F_amp_A=resA["F_amp_A"],
        F_amp_B=F_amp_B,
        nu=resA["nu"],
        amp_ratio=resA["amp_ratio"],
        hankel_factor=resA["hankel_factor"],
        mag_R2_num=mag_R2_num,
        mag_R2_BD=mag_R2_BD,
        Wronskian_drift=W_drift,
        # Gate outputs
        rel_diff=rel_diff,
        agreement_pct=agreement_pct,
        PASS_AGREEMENT_PCT=PASS_AGREEMENT_PCT,
        INFO_LOW_PCT=INFO_LOW_PCT,
        verdict=verdict,
        verdict_reason=verdict_reason,
    )
    print(f"Data saved: {npz_path}")

    # --- Plot ---
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel A: F_amp comparison (bar chart)
    ax = axes[0]
    labels = ["Method A\n(Hankel, pinned nu)", "Method B\n(R, DOP853)"]
    values = [resA["F_amp_A"], F_amp_B]
    colors = ["tab:blue", "tab:orange"]
    bars = ax.bar(labels, values, color=colors, alpha=0.75)
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, v, f"{v:.4f}",
                ha="center", va="bottom", fontsize=10)
    ax.set_ylabel("F_amp (power ratio)")
    ax.set_title(f"Panel A: F_amp agreement (rel_diff = {rel_diff*100:.2f}%, agreement = {agreement_pct:.2f}%)")
    ax.grid(True, alpha=0.3)

    # Panel B: Gate decision visualization
    ax = axes[1]
    ax.axvspan(0, INFO_LOW_PCT, color="tab:red", alpha=0.25, label="FAIL (<40%)")
    ax.axvspan(INFO_LOW_PCT, PASS_AGREEMENT_PCT, color="tab:orange", alpha=0.25, label="INFO [40,60)%")
    ax.axvspan(PASS_AGREEMENT_PCT, 100, color="tab:green", alpha=0.25, label=">= 60% PASS")
    ax.axvline(agreement_pct, color="k", linewidth=2.5, label=f"S80 run = {agreement_pct:.2f}%")

    # S78 iteration history for context
    s78_rel_diffs_pct = [45.15, 9.94, 17.21, 17.21, 5.83, 6.30, 6.30, 6.30]  # (local)
    s78_agreements = [100.0 - r for r in s78_rel_diffs_pct]                    # (local)
    for i, a in enumerate(s78_agreements):
        marker = "o" if i == 0 else "x"
        label = "S78 iter 1" if i == 0 else ("S78 iter 2-8" if i == 1 else None)
        ax.plot(a, 0.8 - 0.08*i, marker=marker, color="gray", markersize=9,
                label=label)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1)
    ax.set_xlabel("F_amp agreement %  = 100*(1 - rel_diff)")
    ax.set_yticks([])
    ax.set_title(f"Panel B: Gate decision -- verdict = {verdict}")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.suptitle(f"S80 W0-1 / W1-B-REMED  --  (F_amp={F_amp_B:.4f}, scheme=SDW, convention=canonical, L_max={L_MAX_TAG})",
                 fontsize=11)
    plt.tight_layout()
    png_path = os.path.join(SCRIPT_DIR, "s80_w1b_remed.png")
    plt.savefig(png_path, dpi=120)
    print(f"Plot saved: {png_path}")

    # --- Append verdict line (per .claude/rules/gate-verdicts.md) ---
    verdict_line = (
        f"S80-W1-B-REMED: {verdict} -- "
        f"F_amp_A={resA['F_amp_A']:.4e}, F_amp_B={F_amp_B:.4e}, "
        f"rel_diff={rel_diff*100:.3f}%, agreement={agreement_pct:.3f}%, "
        f"threshold_PASS={PASS_AGREEMENT_PCT}%, threshold_FAIL={INFO_LOW_PCT}%, "
        f"(F_amp={F_amp_B:.4e},scheme=SDW,convention=canonical,L_max={L_MAX_TAG}), "
        f"sha_closure={sha_closure[:16]}..."
    )
    verdicts_path = os.path.join(SCRIPT_DIR, "s80_gate_verdicts.txt")
    with open(verdicts_path, "a") as f:
        f.write(verdict_line + "\n")
    print(f"\nAppended to {verdicts_path}:")
    print(f"  {verdict_line}")

    elapsed = time.time() - t0                                            # (local)
    print(f"\nTotal elapsed: {elapsed:.2f}s")

    return {
        "verdict": verdict,
        "agreement_pct": agreement_pct,
        "rel_diff": rel_diff,
        "F_amp_A": resA["F_amp_A"],
        "F_amp_B": F_amp_B,
        "sha_closure": sha_closure,
    }


if __name__ == "__main__":
    result = main()
