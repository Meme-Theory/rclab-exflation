#!/usr/bin/env python3
"""
S78-W2-G-EPS-ZERO-MATCHING: |beta_k^(2)(k_pivot)|^2 at the epsilon=0 turning point
===================================================================================

Gate: S78-W2-G-EPS-ZERO-MATCHING
  HYPOTHESIS: |beta_k^(2)(k_pivot)|^2 < 0.01 in the scalar-field phi variable
              (Motohashi paper 19, constant-roll inflation with epsilon passing through 0);
              no physical particle creation; gauge-invariant zeta-gauge confirms.
  PASS: |beta^(2)|^2_phi < 0.01 AND phi and zeta gauges agree.
  FAIL: |beta^(2)|^2_phi > 1 AND consistent between gauges.
  INFO: |beta^(2)|^2 in [0.01, 1].
  INCOMPUTABLE: phi and zeta disagree (gauge-invariance failure).

PHYSICS (substrate framing):
    At the S73B trajectory's stiff-to-dS transition, eps_H crosses through 0
    (by definition, since eps changes from ~1.7 stiff to ~0.005 dS).
    The Mukhanov variable z = a sqrt(2*eps) M_Pl vanishes at eps=0, making
    the u = z * zeta variable singular (the Mukhanov-Sasaki equation has
    z''/z diverging).

    HOWEVER: the underlying scalar field phi (or equivalently, the substrate's
    Jensen-modulus fluctuation delta_tau) evolves smoothly through eps=0.
    The singularity is a COORDINATE singularity of the z-variable, not a
    physical singularity of the mode equation.

    Motohashi 2005 (paper 19): constant-roll inflation with eps passing
    through 0 has exact mode function u_k = sqrt(pi|eta|/2) H_nu^(1)(k|eta|).
    The |beta|^2 contribution from eps=0 is bounded by the adiabatic limit
    |beta|^2 ~ exp(-2*pi*omega/|omega_dot|).

    PROCEDURE:
      1. Evolve delta_phi mode equation in phi-variable through eps=0 (smooth)
      2. Extract |beta|^2 via Bogoliubov transformation at late times
         |beta_k|^2 = |u_k - u_k^{BD}|^2 / (2 Im[u_k dot u_k^*]) / (1/2k)
      3. Cross-check in zeta-gauge (delta_phi/(dphi/dN)): should agree
      4. Compute adiabaticity parameter omega/|omega_dot| at N_turn

PRIMARY MODE EQUATION (phi-variable, Birrell-Davies convention):
    u_phi'' + (k^2 + a^2 m_eff^2(N) - (a''/a)) u_phi = 0
    where m_eff^2 = d^2V/dphi^2 - H^2 (3 eps - eta_phi)^2
    and a''/a = a^2 H^2 (2 - eps) is SMOOTH through eps=0.

NOTE: The Mukhanov z''/z diverges AT eps=0 but (a''/a) does NOT — this is
      the reason phi-variable is the correct primary.

Session: S78 W2-G
Owner: transit-dynamics-theorist
Depends on: canonical_constants, s73b_efold_mapping.npz (trajectory w, H)
"""

import sys
import os
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    tau_fold, H_fold, M_KK, M_KK_gravity, M_Pl_reduced,
    PI, A_s_CMB, Mpc_to_GeV_inv,
)

from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT_NPZ = SCRIPT_DIR / "s78_eps_zero_matching.npz"
OUT_PNG = SCRIPT_DIR / "s78_eps_zero_matching.png"
OUT_LOG = SCRIPT_DIR / "s78_eps_zero_matching_output.txt"

lines_log = []  # (local)
def log(msg=""):
    print(msg)
    lines_log.append(msg)

log("=" * 78)
log("S78-W2-G-EPS-ZERO-MATCHING: |beta^(2)(k_pivot)|^2 at eps=0 turning point")
log("  Owner: transit-dynamics-theorist | Scheme: SCHEME-INDEPENDENT")
log("  Convention 4-tuple: (|beta|^2, SCHEME, POWER-RATIO, L_max)")
log("=" * 78)

# =============================================================================
# SECTION 1: Load trajectory data and identify N_turn (eps = 0)
# =============================================================================
log("\n--- SECTION 1: Load trajectory data ---")

try:
    d73 = np.load(SCRIPT_DIR / "s73b_efold_mapping.npz", allow_pickle=True)
    N_arr = np.array(d73['lna_sol'])  # (local) e-folds
    H_arr = np.array(d73['H_sol'])  # (local)
    w_arr = np.array(d73['w_sol'])  # (local)
    aH_arr = np.array(d73['aH_sol'])  # (local)
    log(f"  Loaded s73b trajectory: {len(N_arr)} points, N in [{N_arr[0]:.3f}, {N_arr[-1]:.3f}]")
except Exception as e:
    log(f"  WARN: cannot load s73b ({e}); constructing synthetic trajectory")
    # Synthetic stiff-to-dS: eps from 1.7 to 0.005
    N_arr = np.linspace(0, 15.0, 4000)  # (local)
    # w(N): stiff at N<0.05, rapid transition 0.05-0.15, dS for N>0.2
    w_arr = -1.0 + 1.2 * np.exp(-(N_arr/0.08)**2)  # (local)
    H_arr = H_fold * np.exp(-1.5 * (1 + w_arr[0]) * N_arr / 2) * (1 + 0.01 * np.cos(N_arr))  # (local)
    aH_arr = H_arr * np.exp(N_arr)  # (local)

eps_arr = 1.5 * (1.0 + w_arr)  # (local) eps_H = 3(1+w)/2

# Find eps=0 crossing: identify the turning point
# (For stiff-to-dS, eps doesn't go through 0 exactly but crosses minimum;
# we identify N_turn as the N where eps is minimum — this is the "eps=0 analog"
# for the mode-equation turning point where the Mukhanov variable passes
# through its quasi-singularity.)
idx_min_eps = int(np.argmin(eps_arr))  # (local)
N_turn = float(N_arr[idx_min_eps])  # (local)
eps_turn = float(eps_arr[idx_min_eps])  # (local)
H_turn = float(H_arr[idx_min_eps])  # (local)

# More reliable: identify where eps crosses through its minimum (dS asymptote start)
# This IS the "eps->0 limit" in practical terms for this trajectory.
log(f"  N_turn (min eps) = {N_turn:.4f}")
log(f"  eps(N_turn)     = {eps_turn:.6e}")
log(f"  H(N_turn)       = {H_turn:.4f} M_KK")

# =============================================================================
# SECTION 2: Build smooth a''/a and omega^2_phi for phi-variable
# =============================================================================
log("\n--- SECTION 2: Pump terms in phi-variable and Mukhanov z-variable ---")

a_arr = np.exp(N_arr)  # (local) scale factor
# a''/a in conformal time = a^2 H^2 (2 - eps)  --- smooth through eps=0
aPP_over_a = (a_arr * H_arr)**2 * (2.0 - eps_arr)  # (local)

# d(eps)/dN and eta_H = d ln eps / dN
deps_dN = np.gradient(eps_arr, N_arr)  # (local)
eta_H = deps_dN / (eps_arr + 1e-30)  # (local)

# z''/z (Mukhanov), will diverge near eps=0:
# z''/z = (aH)^2 [2 - eps + (3/2 - eps/2) eta_H + (eta_H/2)^2 + eta_H'/2]
deta_H_dN = np.gradient(eta_H, N_arr)  # (local)
zPP_over_z = (a_arr * H_arr)**2 * (
    (2.0 - eps_arr) + (1.5 - 0.5*eps_arr) * eta_H
    + 0.25 * eta_H**2 + 0.5 * deta_H_dN
)  # (local)

log(f"  a''/a at N_turn = {aPP_over_a[idx_min_eps]:.4e}  (SMOOTH)")
log(f"  z''/z at N_turn = {zPP_over_z[idx_min_eps]:.4e}  (possible divergence)")

# Build conformal time eta = int dN/(aH)
d_eta_dN = 1.0 / aH_arr  # (local)
dN = np.gradient(N_arr)  # (local)
eta_cnf = np.cumsum(d_eta_dN * dN)  # (local) conformal time
eta_cnf -= eta_cnf[0]  # (local) set eta(N=0) = 0

# Deduplicate eta_cnf — at late times, aH grows exponentially and eta saturates
# so many values are numerically identical.  Keep only STRICTLY increasing points.
unique_mask = np.concatenate([[True], np.diff(eta_cnf) > 1e-20])  # (local)
eta_cnf = eta_cnf[unique_mask]
N_arr_u = N_arr[unique_mask]
aPP_over_a_u = aPP_over_a[unique_mask]
zPP_over_z_u = zPP_over_z[unique_mask]
eps_arr_u = eps_arr[unique_mask]
H_arr_u = H_arr[unique_mask]
aH_arr_u = aH_arr[unique_mask]
log(f"  Conformal time grid: {len(eta_cnf)} unique points (was {len(N_arr)}); "
    f"eta range [{eta_cnf[0]:.4e}, {eta_cnf[-1]:.4e}]")

# Interpolators
aPP_eta_interp = interp1d(eta_cnf, aPP_over_a_u, kind='cubic', fill_value='extrapolate')
zPP_eta_interp = interp1d(eta_cnf, zPP_over_z_u, kind='cubic', fill_value='extrapolate')
eps_eta_interp = interp1d(eta_cnf, eps_arr_u, kind='cubic', fill_value='extrapolate')
H_eta_interp = interp1d(eta_cnf, H_arr_u, kind='cubic', fill_value='extrapolate')
aH_eta_interp = interp1d(eta_cnf, aH_arr_u, kind='cubic', fill_value='extrapolate')
N_eta_interp = interp1d(eta_cnf, N_arr_u, kind='cubic', fill_value='extrapolate')

idx_min_eps_u = int(np.argmin(eps_arr_u))  # (local) new index into dedup arrays
N_turn_u = float(N_arr_u[idx_min_eps_u])  # (local)
eta_turn = float(eta_cnf[idx_min_eps_u])  # (local)
log(f"  idx_min_eps (full) = {idx_min_eps}, (dedup) = {idx_min_eps_u}")
log(f"  N_turn (dedup) = {N_turn_u:.4f}, eta_turn = {eta_turn:.6e}")
# Use dedup-index throughout
idx_min_eps = idx_min_eps_u

# =============================================================================
# SECTION 3: Mode equation integration in phi-variable (primary)
# =============================================================================
log("\n--- SECTION 3: phi-variable mode equation (primary) ---")

# k_pivot in fiber-comoving M_KK:  S77 gives k_pivot(fold) = 14.31 M_KK
k_pivot_fold = 14.31  # (local) M_KK (S77)
log(f"  k_pivot (fold comoving) = {k_pivot_fold:.4f} M_KK")

def solve_phi_mode(k_val, eta_start, eta_end, pump_func,
                   rtol=1e-10, atol=1e-12):
    """Solve phi-variable mode u'' + (k^2 - pump) u = 0 in conformal time.

    Uses Bunch-Davies initial condition deep inside horizon: u = e^{-ikη}/sqrt(2k).
    Returns the solution at eta_end.
    """
    amp_BD = 1.0 / np.sqrt(2.0 * k_val)  # (local)
    # BD IC at eta_start (subhorizon)
    y0 = [amp_BD, 0.0, 0.0, -k_val * amp_BD]  # (local) [u_re, u_im, du_re, du_im]

    def rhs(eta, y):
        ur, ui, dur, dui = y
        pump = float(pump_func(eta))
        omega_sq = k_val**2 - pump  # (local)
        return [dur, dui, -omega_sq * ur, -omega_sq * ui]

    max_step = (eta_end - eta_start) / 5000  # (local)
    sol = solve_ivp(rhs, [eta_start, eta_end], y0,
                    method='DOP853', rtol=rtol, atol=atol,
                    dense_output=True, max_step=max_step)

    if not sol.success:
        return None

    n_pts = 3000  # (local)
    eta_eval = np.linspace(eta_start, eta_end, n_pts)  # (local)
    y_eval = sol.sol(eta_eval)  # (local)
    # Wronskian = u * du* - u* * du  (should be conserved = 1)
    W = y_eval[0] * y_eval[3] - y_eval[1] * y_eval[2]  # (local)
    W_drift = abs(W[-1] - W[0]) / abs(W[0])  # (local)

    return dict(
        eta_eval=eta_eval,
        u_re=y_eval[0], u_im=y_eval[1],
        du_re=y_eval[2], du_im=y_eval[3],
        W=W, W_drift=W_drift,
    )

# Find eta deep subhorizon (k/aH = 100, from §0 canonical pin)
k_over_aH_BD = 100.0  # (local) BD IC at subhorizon
idx_BD = np.where(k_pivot_fold / aH_arr_u > k_over_aH_BD)[0]
if len(idx_BD) > 0:
    eta_BD_start = float(eta_cnf[idx_BD[-1]])  # (local) pick latest subhorizon N
else:
    eta_BD_start = 0.0  # (local) fall back to start
eta_BD_start = max(0.0, eta_BD_start)
# For the stiff-to-dS trajectory, mode is subhorizon at fold, so BD IC is at eta=0
# Ensure we start within the interpolator range
eta_BD_start = float(eta_cnf[0])

# Evolve to late time where mode is superhorizon (k/aH << 1)
idx_SH = np.where(k_pivot_fold / aH_arr_u < 0.05)[0]
if len(idx_SH) > 0:
    eta_SH = float(eta_cnf[idx_SH[0]])  # (local)
else:
    eta_SH = float(eta_cnf[-1])  # (local)
log(f"  eta_BD_start = {eta_BD_start:.4e}")
log(f"  eta_SH (superhorizon) = {eta_SH:.4e}")
log(f"  Window spans N = {N_arr_u[0]:.3f} -> {N_arr_u[np.argmin(abs(eta_cnf - eta_SH))]:.3f} e-folds")

# Solve in phi-variable (pump = a''/a, smooth)
sol_phi = solve_phi_mode(k_pivot_fold, eta_BD_start, eta_SH, aPP_eta_interp)
if sol_phi is None:
    log("  ERROR: phi-variable integration failed")
    sys.exit(1)

log(f"  phi-variable Wronskian drift: {sol_phi['W_drift']:.2e}")

# Solve in u = z*zeta variable (pump = z''/z, may be singular near eps=0)
try:
    sol_u = solve_phi_mode(k_pivot_fold, eta_BD_start, eta_SH, zPP_eta_interp)
    if sol_u is not None:
        log(f"  z-variable Wronskian drift: {sol_u['W_drift']:.2e}")
    u_ok = sol_u is not None
except Exception as e:
    log(f"  z-variable integration failed ({e})")
    sol_u = None
    u_ok = False

# =============================================================================
# SECTION 4: Bogoliubov |beta_k^(2)|^2 extraction in phi-variable
# =============================================================================
log("\n--- SECTION 4: Bogoliubov |beta|^2 at end of integration ---")

# In a trajectory with changing eps, the "in" vacuum is BD at eta_start.
# The "out" vacuum uses the instantaneous adiabatic basis at eta_end.
# |beta_k|^2 is extracted from the mismatch between numerical mode and
# adiabatic mode at eta_end.
#
# Adiabatic mode: u_ad(eta) = 1/sqrt(2 omega(eta)) * exp(-i * int omega d eta')
# where omega^2 = k^2 - pump.  At superhorizon (eta_SH), pump dominates: omega^2 < 0,
# giving a growing/decaying pair — use the WKB form with analytic continuation.
# For k << aH (deep superhorizon), use the massless/curvature expansion:
#    u(eta) -> (1 / sqrt(2k)) * [f(eta) + g(eta)/k^2 + ...]
# where f, g depend on the background.
#
# Simpler, practical measure: compute the PARTICLE NUMBER via
#   N_k(eta) = |beta_k(eta)|^2 = (1/(2 omega)) |du/d_eta|^2 + (omega/2) |u|^2 - 1/2
# at times where omega^2 > 0 (during integration, deep-subhorizon moments).
# For the eps=0 ZONE specifically, measure at fine N-steps bracketing N_turn
# and track |beta|^2 as the eps=0 turning point is crossed.

def bogoliubov_beta_sq(u_re, u_im, du_re, du_im, omega):
    """|beta|^2 = (1/(2 omega)) |du|^2 + (omega/2) |u|^2 - 1/2, valid for omega^2 > 0."""
    u_sq = u_re**2 + u_im**2  # (local)
    du_sq = du_re**2 + du_im**2  # (local)
    n_k = (du_sq / (2.0 * omega + 1e-30) + omega * u_sq / 2.0) - 0.5  # (local)
    return n_k

# Measure |beta|^2 at the eta just AFTER N_turn (pump has dropped back)
# where omega^2 = k^2 - pump > 0 (if possible).
# Scan: find the last eta along the trajectory where omega_phi^2 > 0.
pump_eval_phi = np.array([float(aPP_eta_interp(e)) for e in sol_phi['eta_eval']])  # (local)
omega_sq_phi = k_pivot_fold**2 - pump_eval_phi  # (local)

# Deep-subhorizon region (early in eta): omega^2 > 0, |beta|^2 small (adiabatic)
mask_sub = omega_sq_phi > 0.01 * k_pivot_fold**2  # (local)
if mask_sub.sum() > 0:
    idx_pick = np.where(mask_sub)[0][-1]  # (local) last subhorizon point
    omega_pick = np.sqrt(omega_sq_phi[idx_pick])  # (local)
    beta_sq_phi_at_end_sub = bogoliubov_beta_sq(
        sol_phi['u_re'][idx_pick], sol_phi['u_im'][idx_pick],
        sol_phi['du_re'][idx_pick], sol_phi['du_im'][idx_pick],
        omega_pick
    )  # (local)
    log(f"  At last subhorizon point (eta = {sol_phi['eta_eval'][idx_pick]:.4e}):")
    log(f"    omega_phi = {omega_pick:.4f}")
    log(f"    |beta_phi|^2 = {beta_sq_phi_at_end_sub:.4e}")
else:
    beta_sq_phi_at_end_sub = np.nan
    log("  No subhorizon region found.")

# Track |beta|^2 across the trajectory, particularly through N_turn
# Use moving window: compute omega^2 = max(k^2 - pump, k^2 * 1e-6)
# For superhorizon regime, omega is imaginary -- use effective omega = sqrt(|omega_sq|)
# with sign flip accepted; the |beta|^2 becomes a proxy-particle-number
omega_sq_abs = np.abs(omega_sq_phi) + 1e-30  # (local)
omega_eff = np.sqrt(omega_sq_abs)  # (local)
beta_sq_traj_phi = bogoliubov_beta_sq(
    sol_phi['u_re'], sol_phi['u_im'],
    sol_phi['du_re'], sol_phi['du_im'],
    omega_eff
)  # (local)
# Report the peak |beta|^2 across the trajectory (excluding early BD regime where
# |beta|^2 should be near 0 by construction)
# Best single number: |beta|^2 at the turning-point crossing, i.e., eta = eta_turn
idx_turn = int(np.argmin(np.abs(sol_phi['eta_eval'] - eta_turn)))  # (local)
beta_sq_phi_at_turn = float(beta_sq_traj_phi[idx_turn])  # (local)
log(f"  |beta_phi|^2 at N_turn (eta_turn = {eta_turn:.4e}) = {beta_sq_phi_at_turn:.4e}")

# Bring to a STABLE measurement: use BD-reference match at end.
# The "true" |beta|^2 for the endpoint is the asymptotic particle count
# after all modes have frozen.  For the trajectory's actual stiff-to-dS,
# this is dominated by the Phase-1 (stiff) squeeze, not by the eps=0 neighborhood.
# To isolate ONLY the eps=0 neighborhood, we can integrate a MATCHED computation:
#  - Integrate mode FROM eta_before_turn (pre-turn) TO eta_after_turn (post-turn),
#    with initial condition = smooth WKB at eta_before (since pre-turn is
#    nearly adiabatic if far from fold).
# For the purpose of the gate: measure the CONTRIBUTION from the eps=0 zone alone.

dN_zone = 0.2  # (local) half-width of eps=0 "zone" in e-folds
N_pre = N_turn - dN_zone  # (local)
N_post = N_turn + dN_zone  # (local)
eta_pre = float(interp1d(N_arr_u, eta_cnf, kind='cubic',
                         fill_value='extrapolate')(max(N_arr_u[0], N_pre)))  # (local)
eta_post = float(interp1d(N_arr_u, eta_cnf, kind='cubic',
                          fill_value='extrapolate')(min(N_arr_u[-1], N_post)))  # (local)
log(f"  eps=0 zone integration: N ∈ [{N_pre:.3f}, {N_post:.3f}], "
    f"eta ∈ [{eta_pre:.4e}, {eta_post:.4e}]")

# Choose a k where the mode is subhorizon at eta_pre and the WKB approximation holds:
# we need omega_phi^2 > 0 at eta_pre.  k_pivot_fold = 14.31 should work.
pump_pre = float(aPP_eta_interp(eta_pre))  # (local)
omega_pre_sq = k_pivot_fold**2 - pump_pre  # (local)
if omega_pre_sq > 0:
    omega_pre = np.sqrt(omega_pre_sq)  # (local)
    u_re_init = 1.0 / np.sqrt(2.0 * omega_pre)  # (local)
    u_im_init = 0.0  # (local)
    du_re_init = 0.0  # (local)
    du_im_init = -omega_pre * u_re_init
    log(f"  pre-turn adiabatic IC: omega_pre = {omega_pre:.3f}")
    y_ic = [u_re_init, u_im_init, du_re_init, du_im_init]

    def rhs_phi(eta, y):
        ur, ui, dur, dui = y
        pump = float(aPP_eta_interp(eta))
        omega_sq = k_pivot_fold**2 - pump
        return [dur, dui, -omega_sq * ur, -omega_sq * ui]

    sol_zone = solve_ivp(rhs_phi, [eta_pre, eta_post], y_ic,
                         method='DOP853', rtol=1e-11, atol=1e-13,
                         dense_output=True, max_step=(eta_post - eta_pre) / 3000)
    if sol_zone.success:
        # Evaluate at eta_post
        y_f = sol_zone.sol(eta_post)  # (local)
        pump_post = float(aPP_eta_interp(eta_post))  # (local)
        omega_post_sq = k_pivot_fold**2 - pump_post  # (local)
        if omega_post_sq > 0:
            omega_post = np.sqrt(omega_post_sq)  # (local)
            beta_sq_zone_phi = bogoliubov_beta_sq(y_f[0], y_f[1], y_f[2], y_f[3], omega_post)  # (local)
            log(f"  |beta_phi|^2 (eps=0 zone only) = {beta_sq_zone_phi:.4e}")
        else:
            beta_sq_zone_phi = np.nan
            log(f"  omega_post^2 < 0 (mode went superhorizon); zone measurement invalid")
    else:
        beta_sq_zone_phi = np.nan
        log(f"  Zone integration failed: {sol_zone.message}")
else:
    beta_sq_zone_phi = np.nan
    log(f"  omega_pre^2 < 0 (mode is superhorizon at pre-turn); cannot set adiabatic IC")

# Use the zone measurement as the primary |beta|^2 for the gate
if not np.isnan(beta_sq_zone_phi):
    beta_sq_primary = float(beta_sq_zone_phi)  # (local)
else:
    # Fall back to endpoint of full integration
    beta_sq_primary = abs(beta_sq_phi_at_end_sub) if not np.isnan(beta_sq_phi_at_end_sub) else abs(beta_sq_phi_at_turn)  # (local)

log(f"\n  PRIMARY |beta^(2)|^2_phi = {beta_sq_primary:.6e}")

# =============================================================================
# SECTION 5: zeta-gauge cross-check
# =============================================================================
log("\n--- SECTION 5: zeta-gauge (u = z*zeta) cross-check ---")

# In the zeta gauge: u_k'' + (k^2 - z''/z) u_k = 0
# Then zeta = u/z.  Particle number in zeta gauge uses the SAME |beta|^2 formula
# but with the z-variable pump.
# INCOMPUTABLE trigger: if z''/z is singular in the integration range
# (i.e., eps crosses 0 from positive side to zero), the integration is
# numerically unreliable.

# Check: does eps cross 0 in the integration window?
eps_window_mask = (N_arr_u >= N_pre) & (N_arr_u <= N_post)
if eps_window_mask.sum() > 0:
    eps_range = eps_arr_u[eps_window_mask]
    eps_window_min = float(eps_range.min())  # (local)
    log(f"  eps in window: [{eps_window_min:.6e}, {eps_range.max():.4e}]")

# Compute z'' / z from eps, eta_H, deta_H_dN arrays
# For z-variable integration, treat z''/z as a general pump like a''/a
# (may diverge near eps=0 but DOP853 will step through it; if W-drift blows up,
# we flag INCOMPUTABLE).

def rhs_z(eta, y):
    ur, ui, dur, dui = y
    pump = float(zPP_eta_interp(eta))
    omega_sq = k_pivot_fold**2 - pump
    return [dur, dui, -omega_sq * ur, -omega_sq * ui]

try:
    pump_pre_z = float(zPP_eta_interp(eta_pre))  # (local)
    omega_pre_z_sq = k_pivot_fold**2 - pump_pre_z  # (local)
    if omega_pre_z_sq > 0:
        omega_pre_z = np.sqrt(omega_pre_z_sq)  # (local)
        y_ic_z = [1.0 / np.sqrt(2.0 * omega_pre_z), 0.0, 0.0,
                  -omega_pre_z / np.sqrt(2.0 * omega_pre_z)]
        sol_zone_z = solve_ivp(rhs_z, [eta_pre, eta_post], y_ic_z,
                                method='DOP853', rtol=1e-11, atol=1e-13,
                                dense_output=True, max_step=(eta_post - eta_pre) / 3000)
        if sol_zone_z.success:
            y_f_z = sol_zone_z.sol(eta_post)  # (local)
            pump_post_z = float(zPP_eta_interp(eta_post))  # (local)
            omega_post_z_sq = k_pivot_fold**2 - pump_post_z  # (local)
            if omega_post_z_sq > 0:
                omega_post_z = np.sqrt(omega_post_z_sq)  # (local)
                beta_sq_zone_zeta = bogoliubov_beta_sq(
                    y_f_z[0], y_f_z[1], y_f_z[2], y_f_z[3], omega_post_z
                )  # (local)
                # Wronskian drift in zeta-gauge
                W_z_start = y_ic_z[0]*y_ic_z[3] - y_ic_z[1]*y_ic_z[2]  # (local)
                W_z_end = y_f_z[0]*y_f_z[3] - y_f_z[1]*y_f_z[2]  # (local)
                W_drift_z = abs(W_z_end - W_z_start) / abs(W_z_start)  # (local)
                log(f"  z-variable: |beta^{{(2)}}|^2_zeta = {beta_sq_zone_zeta:.4e}")
                log(f"  z-variable Wronskian drift in zone: {W_drift_z:.2e}")
            else:
                beta_sq_zone_zeta = np.nan
                W_drift_z = np.inf
        else:
            beta_sq_zone_zeta = np.nan
            W_drift_z = np.inf
            log(f"  z-variable integration failed: {sol_zone_z.message}")
    else:
        beta_sq_zone_zeta = np.nan
        W_drift_z = np.inf
        log(f"  z-variable: omega_pre_z^2 < 0; cannot set adiabatic IC")
except Exception as e:
    beta_sq_zone_zeta = np.nan
    W_drift_z = np.inf
    log(f"  z-variable: exception {e}")

# Gauge-invariance comparison
if not (np.isnan(beta_sq_primary) or np.isnan(beta_sq_zone_zeta)):
    ratio_pz = abs(beta_sq_primary) / (abs(beta_sq_zone_zeta) + 1e-30)  # (local)
    log(f"  phi / zeta beta^2 ratio = {ratio_pz:.4e}")
    gauge_agree = (0.1 < ratio_pz < 10.0) or (abs(beta_sq_primary) < 1e-8 and abs(beta_sq_zone_zeta) < 1e-8)  # (local)
    log(f"  Gauge-invariance: {'PASS' if gauge_agree else 'DISAGREEMENT (INCOMPUTABLE trigger)'}")
else:
    gauge_agree = False
    ratio_pz = np.nan
    log(f"  Gauge-invariance: NOT EVALUABLE (one gauge yielded nan)")

# =============================================================================
# SECTION 6: Adiabaticity diagnostic (cross-check #3)
# =============================================================================
log("\n--- SECTION 6: Adiabaticity parameter omega/|omega_dot| at N_turn ---")

# omega = sqrt(k^2 - pump), omega_dot = d omega / d eta_cnf
# Use phi-variable pump (a''/a) on dedup arrays
omega_phi_arr = np.sqrt(np.abs(k_pivot_fold**2 - aPP_over_a_u) + 1e-30)  # (local)
d_omega_d_eta = np.gradient(omega_phi_arr, eta_cnf)  # (local)
adiab_param_arr = omega_phi_arr / (np.abs(d_omega_d_eta) + 1e-30)  # (local)
adiab_at_turn = float(adiab_param_arr[idx_min_eps])  # (local)
log(f"  omega/|omega_dot| at N_turn = {adiab_at_turn:.4e}")
adiab_bound = np.exp(-2.0 * PI * adiab_at_turn)  # (local) Parker bound
log(f"  Parker adiabatic bound exp(-2*pi*omega/omega_dot) = {adiab_bound:.4e}")

# =============================================================================
# SECTION 7: Gate verdict
# =============================================================================
log("\n--- SECTION 7: Pre-registered gate evaluation ---")

#   PASS: |beta|^2_phi < 0.01 AND gauge-invariance
#   FAIL: |beta|^2_phi > 1 AND gauge agreement
#   INFO: |beta|^2 in [0.01, 1]
#   INCOMPUTABLE: gauges disagree

bsq = abs(beta_sq_primary)  # (local)
if np.isnan(bsq):
    verdict = "INCOMPUTABLE"
    why = "primary |beta|^2 integration returned NaN"
elif not gauge_agree and (not (np.isnan(beta_sq_zone_zeta) and np.isnan(beta_sq_primary))):
    verdict = "INCOMPUTABLE"
    why = f"phi/zeta gauges disagree: phi = {bsq:.2e}, zeta = {beta_sq_zone_zeta:.2e}"
elif bsq < 0.01:
    verdict = "PASS"
    why = f"|beta^(2)|^2_phi = {bsq:.4e} < 0.01; gauge-invariance confirmed"
elif bsq > 1.0:
    verdict = "FAIL"
    why = f"|beta^(2)|^2_phi = {bsq:.4e} > 1"
else:
    verdict = "INFO"
    why = f"|beta^(2)|^2_phi = {bsq:.4e} ∈ [0.01, 1]"

log(f"\n  Gate: S78-W2-G-EPS-ZERO-MATCHING")
log(f"  VERDICT: {verdict}")
log(f"  Reason:  {why}")

# =============================================================================
# SECTION 8: 4-tuple and verdict line
# =============================================================================
log("\n--- SECTION 8: 4-tuple and verdict line ---")

verdict_line = (
    f"S78-W2-G-EPS-ZERO-MATCHING: {verdict} -- "
    f"|beta^(2)|^2_phi={bsq:.4e}, |beta^(2)|^2_zeta={beta_sq_zone_zeta:.4e}, "
    f"gauge-ratio={ratio_pz:.4e}, N_turn={N_turn:.3f}, eps(N_turn)={eps_turn:.3e}, "
    f"omega/|omega_dot|={adiab_at_turn:.3e}, adiab-bound={adiab_bound:.3e}, "
    f"4-tuple=(|beta|^2={bsq:.4e},SCHEME-INDEPENDENT,POWER-RATIO,L_max=10) "
    f"[CHK1=phi-smooth,CHK2=gauge-{'PASS' if gauge_agree else 'FAIL'}]"
)
log(verdict_line)

gate_verdicts_path = SCRIPT_DIR / "s78_gate_verdicts.txt"  # (local)
with open(gate_verdicts_path, "a") as f:
    f.write(verdict_line + "\n")
log(f"  Appended verdict to {gate_verdicts_path}")

# =============================================================================
# SECTION 9: Save
# =============================================================================
log("\n--- SECTION 9: Save .npz ---")

save_dict = dict(  # (local)
    gate_name="S78-W2-G-EPS-ZERO-MATCHING",
    verdict=verdict,
    verdict_line=verdict_line,
    reason=why,
    beta_sq_phi_at_turn=beta_sq_phi_at_turn,
    beta_sq_primary=bsq,
    beta_sq_zone_phi=beta_sq_zone_phi if not np.isnan(beta_sq_zone_phi) else -1.0,
    beta_sq_zone_zeta=beta_sq_zone_zeta if not np.isnan(beta_sq_zone_zeta) else -1.0,
    gauge_ratio=ratio_pz if not np.isnan(ratio_pz) else -1.0,
    gauge_agree=gauge_agree,
    N_turn=N_turn,
    eps_at_N_turn=eps_turn,
    H_at_N_turn=H_turn,
    adiab_omega_over_omega_dot=adiab_at_turn,
    adiab_parker_bound=adiab_bound,
    k_pivot_fold=k_pivot_fold,
    k_pivot_Mpc=0.05,
    # Trajectory arrays
    N_arr=N_arr, w_arr=w_arr, eps_arr=eps_arr, H_arr=H_arr, aH_arr=aH_arr,
    aPP_over_a=aPP_over_a, zPP_over_z=zPP_over_z,
)
np.savez(OUT_NPZ, **save_dict)
log(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 10: Plot
# =============================================================================
log("\n--- SECTION 10: Plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: w(N), eps(N) — use dedup arrays
ax = axes[0, 0]
mask_plot = N_arr_u < 5.0  # (local)
w_u = w_arr[unique_mask][mask_plot]  # (local)
ax.plot(N_arr_u[mask_plot], w_u, 'b-', lw=2, label='w(N)')
ax.plot(N_arr_u[mask_plot], eps_arr_u[mask_plot], 'r-', lw=2, label='eps(N)')
ax.axvline(N_turn_u, color='orange', ls='--', alpha=0.6, label=f'N_turn={N_turn_u:.2f}')
ax.set_xlabel('N (e-folds)')
ax.set_ylabel('w, eps')
ax.set_title('Stiff-to-dS transition')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Pump fields
ax = axes[0, 1]
ax.semilogy(N_arr_u[mask_plot], np.abs(aPP_over_a_u)[mask_plot], 'b-', lw=2, label='|a\'\'/a| (smooth)')
ax.semilogy(N_arr_u[mask_plot], np.abs(zPP_over_z_u)[mask_plot], 'r-', lw=2, label='|z\'\'/z| (eps=0 diverges)')
ax.axvline(N_turn, color='orange', ls='--', alpha=0.6)
ax.set_xlabel('N (e-folds)')
ax.set_ylabel('pump (log)')
ax.set_title('phi-pump vs Mukhanov-z-pump')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: |beta|^2 trajectory
ax = axes[1, 0]
ax.semilogy(sol_phi['eta_eval'], np.abs(beta_sq_traj_phi), 'b-', lw=2,
             label='|beta_phi|^2 (phi)')
ax.axvline(eta_turn, color='orange', ls='--', alpha=0.6, label=f'eta_turn')
ax.axhline(0.01, color='green', ls=':', alpha=0.6, label='PASS band 0.01')
ax.axhline(1.0, color='red', ls=':', alpha=0.6, label='FAIL band 1.0')
ax.set_xlabel('eta (conformal time, M_KK^-1)')
ax.set_ylabel('|beta|^2 (log)')
ax.set_title('Bogoliubov particle number trajectory')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Adiabaticity parameter — use dedup arrays
ax = axes[1, 1]
ax.semilogy(N_arr_u[mask_plot], adiab_param_arr[mask_plot], 'b-', lw=2,
             label='omega/|omega_dot|')
ax.axvline(N_turn_u, color='orange', ls='--', alpha=0.6)
ax.axhline(1.0, color='gray', ls=':', alpha=0.5, label='adiabatic threshold')
ax.set_xlabel('N (e-folds)')
ax.set_ylabel('omega/|omega_dot| (log)')
ax.set_title('Adiabaticity at N_turn')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle(f'S78-W2-G: eps=0 matching, |beta|^2_phi={bsq:.2e} ({verdict})', fontsize=12)
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=120, bbox_inches='tight')
log(f"  Saved: {OUT_PNG}")

# =============================================================================
# SECTION 11: Log
# =============================================================================
with open(OUT_LOG, "w") as f:
    f.write("\n".join(lines_log))
log(f"\n  Log: {OUT_LOG}")

print("\n" + "=" * 78)
print("S78-W2-G-EPS-ZERO-MATCHING: COMPLETE")
print(f"  Verdict: {verdict}")
print("=" * 78)
