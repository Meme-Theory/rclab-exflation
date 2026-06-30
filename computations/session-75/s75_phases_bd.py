#!/usr/bin/env python3
"""
PHASES-BD-75: Squeezing Phases phi_k for All 8 BCS Branches
=============================================================

Session: S75 (Wave 2, Task C4)
Agent: Transit-Dynamics-Theorist
Classification: PHONONIC (BCS squeeze phase at substrate transit)

TASK:
  Compute squeezing phases phi_k alongside magnitudes r_k for all 8 BCS
  modes at tau_exit. S68 Landau-Transit workshop established phi_eff = pi/4
  (Josephson-locked) as the critical unknown for the A_s enhancement formula:

    A_s ~ cosh(2r) + (sqrt(2)/3)*sinh(2r)*cos(phi_eff)

  The S73B compound Bogoliubov used phi=0 as a placeholder. This computation
  extracts the ACTUAL phases from the time-dependent BdG solution.

GOVERNING STRUCTURE:
  The mode equation for BCS quasiparticle mode k is:

    u_k'' + omega_k^2(tau) u_k = 0                                    (1)

  where omega_k(tau) = sqrt(eps_k(tau)^2 + Delta(tau)^2) is the BCS
  quasiparticle dispersion with:
    - eps_k(tau) = single-particle energy (from D_K eigenvalue track)
    - Delta(tau) = BCS gap (from self-consistent gap equation)

  The Bogoliubov transformation connecting in-vacuum (tau -> -inf) to
  out-vacuum (tau -> +inf) gives:

    beta_k = |beta_k| * exp(i * phi_k)                                (2)

  where phi_k is the squeezing phase. In the squeeze operator language:

    S(r,phi) = exp(r * (e^{i*phi} a_k^dag a_{-k}^dag - h.c.) / 2)    (3)

  The Bogoliubov ODE in the (alpha, beta, Phi) representation gives
  complex alpha_k and beta_k directly. The phase phi_k = arg(beta_k).

METHOD:
  Three independent methods to extract phi_k:

  METHOD 1: Direct from ODE (Bogoliubov alpha-beta-Phi system)
    Solve the standard Bogoliubov ODE (as in S73B) but now EXTRACT the
    phase of beta_k at output. phi_k = arg(beta_k_fold).

  METHOD 2: Transfer matrix (piecewise constant approximation)
    Discretize omega_k(tau) into N_seg segments, compose transfer matrices.
    Phase extracted from the (2,1) element of the total transfer matrix.

  METHOD 3: Sudden approximation limit
    For the impulsive transit (dt_transit << 1/omega_k), the sudden
    approximation gives phi_sudden = pi (phase-locked at pi for instantaneous
    quench). Deviation from pi measures how far from sudden the transit is.

  Cross-check: All three must agree within stated precision.

Gate: S75-C4-PHASES-BD
  PASS: All phi_k in [pi/4 - 0.3, pi/4 + 0.3] (Josephson prediction)
  INFO: phi_k scattered but mean near pi/4
  FAIL: phi_k near pi (sudden quench) or highly scattered

Cross-checks:
  CHK1: Unitarity |alpha_k|^2 - |beta_k|^2 = 1 to machine epsilon
  CHK2: phi_k consistent across methods (RK4/5, transfer matrix, sudden)
"""

import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, tau_fold, Delta_BCS, E_B1, E_B2_mean, E_B3_mean,
    Z_fold, dS_fold, d2S_fold, S_fold,
    a0_fold, a2_fold, a4_fold,
    M_KK, dt_transit, v_terminal, H_fold
)

t_start = time.time()

print("=" * 78)
print("PHASES-BD-75: Squeezing Phases phi_k for All 8 BCS Branches")
print("=" * 78)
print()

# =============================================================================
# SECTION 1: Load input data
# =============================================================================

print("SECTION 1: Loading input data")
print("-" * 40)

# Load S73B baseline Bogoliubov results
d_73b = np.load(os.path.join(SCRIPT_DIR, 's73b_transit_ps.npz'), allow_pickle=True)

# Load S72 BCS gap profile and frequency derivatives
d_72k = np.load(os.path.join(SCRIPT_DIR, 's72_kappa_delta.npz'), allow_pickle=True)
d_72b = np.load(os.path.join(SCRIPT_DIR, 's72_blueshift_tilt.npz'), allow_pickle=True)

# Extract baseline data
labels = d_73b['labels']  # ['B2[0]', 'B2[1]', ..., 'B1', 'B3[0]', ...]
N_modes = len(labels)  # (local) = 8
omega_k_fold = d_73b['omega_k_fold']  # BCS quasiparticle frequencies at fold
r_k_bcs = d_73b['r_k_bcs']  # BCS squeeze parameters (from pairing)
mode_weights = d_73b['mode_weights']  # Peter-Weyl weights

# S73B baseline Bogoliubov coefficients (these used phi=0 default)
beta_fold_re_73b = d_73b['beta_fold_real']  # (local)
beta_fold_im_73b = d_73b['beta_fold_imag']  # (local)
alpha_fold_re_73b = d_73b['alpha_fold_real']  # (local)
alpha_fold_im_73b = d_73b['alpha_fold_imag']  # (local)

# S72 gap profile parameters
tau_center = float(d_72k['tau_center'])  # (local)
coeffs_quartic = d_72k['coeffs_quartic']
deps_dtau = d_72k['deps_dtau']  # (8,) d(eps_k)/d(tau) at fold
d2eps_dtau2 = d_72k['d2eps_dtau2']  # (8,) d^2(eps_k)/d(tau)^2 at fold
v_tau_val = float(d_72k['v_tau'])  # 8.27 M_KK (local)

# Entry-stage Bogoliubov coefficients
alpha_sq_entry = d_72b['alpha_sq_entry']
beta_sq_entry = d_72b['beta_sq_entry']
r_k_entry = d_72b['r_k_entry']

print(f"  N_modes = {N_modes}")
print(f"  Labels: {list(labels)}")
print(f"  omega_k(fold) = {omega_k_fold}")
print(f"  r_k_bcs       = {r_k_bcs}")
print(f"  v_tau          = {v_tau_val:.4f} M_KK")
print(f"  Delta_BCS      = {Delta_BCS:.6f} M_KK")
print(f"  tau_fold       = {tau_fold}")
print(f"  dt_transit     = {dt_transit:.6e} M_KK^{{-1}}")
print()

# =============================================================================
# SECTION 2: Define BCS frequency profiles omega_k(tau), Delta(tau)
# =============================================================================

print("SECTION 2: BCS frequency profiles")
print("-" * 40)

TAU_START = 0.15  # (local)
TAU_END = 0.23  # (local)
N_TAU = 4000  # (local) doubled from S73B for phase precision
tau_grid = np.linspace(TAU_START, TAU_END, N_TAU)  # (local)

def Delta_of_tau(tau):
    """BCS gap from S72 quartic fit."""
    dt = tau - tau_center  # (local)
    return (coeffs_quartic[0]*dt**4 + coeffs_quartic[1]*dt**3 +
            coeffs_quartic[2]*dt**2 + coeffs_quartic[3]*dt + coeffs_quartic[4])

def dDelta_dtau(tau):
    """d(Delta)/d(tau) from quartic fit."""
    dt = tau - tau_center  # (local)
    return (4*coeffs_quartic[0]*dt**3 + 3*coeffs_quartic[1]*dt**2 +
            2*coeffs_quartic[2]*dt + coeffs_quartic[3])

# Single-particle energies at fold from s56_gge_fabric.npz
d_56 = np.load(os.path.join(SCRIPT_DIR, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold_raw = d_56['eps_fold']  # (local) 8 single-particle energies at fold

# Cross-check: eps_k should satisfy omega_k = sqrt(eps_k^2 + Delta^2)
Delta_at_fold = Delta_of_tau(tau_fold)  # (local)
omega_check = np.sqrt(eps_fold_raw**2 + Delta_at_fold**2)  # (local)
print(f"  Delta(fold) = {Delta_at_fold:.8f} M_KK")
print(f"  eps_fold (from s56) = {eps_fold_raw}")
print(f"  omega_check = sqrt(eps^2 + Delta^2) = {omega_check}")
print(f"  omega_k(fold) from s73b              = {omega_k_fold}")
print(f"  max |diff| = {np.max(np.abs(omega_check - omega_k_fold)):.2e}")
print()

def eps_k_of_tau(tau, ki):
    """Single-particle energy for mode k, Taylor expanded around fold."""
    dtau = tau - tau_fold  # (local)
    return eps_fold_raw[ki] + deps_dtau[ki]*dtau + 0.5*d2eps_dtau2[ki]*dtau**2

def omega_k_of_tau(tau, ki):
    """BCS quasiparticle frequency for mode k."""
    eps = eps_k_of_tau(tau, ki)  # (local)
    Delta = Delta_of_tau(tau)  # (local)
    return np.sqrt(eps**2 + Delta**2)

def dlnomega_dtau(tau, ki):
    """d(ln omega_k)/d(tau) -- Bogoliubov coupling strength."""
    eps = eps_k_of_tau(tau, ki)  # (local)
    Delta = Delta_of_tau(tau)  # (local)
    omega_sq = eps**2 + Delta**2  # (local)
    dtau = tau - tau_fold  # (local)
    deps = deps_dtau[ki] + d2eps_dtau2[ki]*dtau  # (local)
    dDelt = dDelta_dtau(tau)  # (local)
    return (eps*deps + Delta*dDelt) / omega_sq

# Velocity profile v_tau(tau) from spectral action gradient
def v_tau_sq(tau):
    """Transit velocity squared from spectral action gradient."""
    dt = tau - tau_fold  # (local)
    return v_tau_val**2 + (2.0/Z_fold) * (dS_fold*dt + 0.5*d2S_fold*dt**2)

# Precompute omega and coupling on dense grid
omega_grid = np.zeros((N_modes, N_TAU))  # (local)
dlnomega_grid = np.zeros((N_modes, N_TAU))  # (local)
for ki in range(N_modes):
    for j in range(N_TAU):
        omega_grid[ki, j] = omega_k_of_tau(tau_grid[j], ki)
        dlnomega_grid[ki, j] = dlnomega_dtau(tau_grid[j], ki)

# Adiabaticity parameter at fold
print("  Adiabaticity check gamma = |dlnomega/dtau| * v / omega:")
for ki in range(N_modes):
    fold_idx = N_TAU // 2  # (local)
    v_fold = np.sqrt(max(v_tau_sq(tau_grid[fold_idx]), 1e-30))  # (local)
    gamma_fold = abs(dlnomega_grid[ki, fold_idx]) * v_fold / omega_grid[ki, fold_idx]  # (local)
    print(f"    {str(labels[ki]):>8s}: gamma(fold) = {gamma_fold:.6f} "
          f"({'DIABATIC' if gamma_fold > 1.0 else 'adiabatic'})")
print()

# =============================================================================
# SECTION 3: METHOD 1 -- Direct Bogoliubov ODE with phase extraction
# =============================================================================
#
# The Bogoliubov ODE in the (alpha, beta, Phi) representation:
#
#   d(alpha_r)/d(tau) = -kappa(tau) * [beta_r*cos(2*Phi) + beta_i*sin(2*Phi)]
#   d(alpha_i)/d(tau) = -kappa(tau) * [-beta_r*sin(2*Phi) + beta_i*cos(2*Phi)]
#   d(beta_r)/d(tau)  = -kappa(tau) * [alpha_r*cos(2*Phi) - alpha_i*sin(2*Phi)]
#   d(beta_i)/d(tau)  = -kappa(tau) * [alpha_r*sin(2*Phi) + alpha_i*cos(2*Phi)]
#   d(Phi)/d(tau)     = omega_k(tau) / v_tau(tau)
#
# where kappa(tau) = (1/2) * d(ln omega_k)/d(tau) is the coupling strength.
#
# Initial conditions: alpha = 1 + 0j, beta = 0 + 0j, Phi = 0
# (Bunch-Davies vacuum: positive frequency mode at tau_start)
#
# The squeezing phase IS arg(beta_k) at tau_end.
# =============================================================================

print("=" * 78)
print("SECTION 3: METHOD 1 -- Direct Bogoliubov ODE")
print("=" * 78)
print()

# Build cubic spline interpolators for efficiency
omega_interps = []  # (local)
dlnomega_interps = []  # (local)
for ki in range(N_modes):
    omega_interps.append(CubicSpline(tau_grid, omega_grid[ki]))
    dlnomega_interps.append(CubicSpline(tau_grid, dlnomega_grid[ki]))

def bog_rhs(tau, y, ki):
    """Bogoliubov ODE right-hand side for mode ki.

    State: y = [alpha_r, alpha_i, beta_r, beta_i, Phi]
    """
    ar, ai, br, bi, Phi = y
    kappa = 0.5 * float(dlnomega_interps[ki](tau))  # (local)
    c2P = np.cos(2*Phi)  # (local)
    s2P = np.sin(2*Phi)  # (local)
    dar = -kappa * (br*c2P + bi*s2P)  # (local)
    dai = -kappa * (-br*s2P + bi*c2P)  # (local)
    dbr = -kappa * (ar*c2P - ai*s2P)  # (local)
    dbi = -kappa * (ar*s2P + ai*c2P)  # (local)
    omega = float(omega_interps[ki](tau))  # (local)
    v = np.sqrt(max(v_tau_sq(tau), 1e-30))  # (local)
    dPhi = omega / v  # (local)
    return [dar, dai, dbr, dbi, dPhi]

# Solver configuration
omega_char = np.mean(omega_k_fold)  # (local)
phase_rate = omega_char / v_tau_val  # (local)
max_step_tau = 2*PI / phase_rate / 100  # (local)

print(f"  ODE solver: Radau, rtol=1e-13, atol=1e-15")
print(f"  max_step_tau = {max_step_tau:.6e}")
print(f"  Integration domain: [{TAU_START}, {TAU_END}]")
print()

y0 = [1.0, 0.0, 0.0, 0.0, 0.0]  # (local) Bunch-Davies IC

# Storage for Method 1 results
alpha_m1 = np.zeros(N_modes, dtype=complex)  # (local)
beta_m1 = np.zeros(N_modes, dtype=complex)  # (local)
r_k_m1 = np.zeros(N_modes)  # (local)
phi_k_m1 = np.zeros(N_modes)  # (local)
unitarity_err_m1 = np.zeros(N_modes)  # (local)

print("  Integrating Bogoliubov ODE for 8 BCS modes:")
print(f"  {'Mode':>8s}  {'|beta|^2':>14s}  {'r_k':>10s}  {'phi_k':>12s}  "
      f"{'phi_k/pi':>10s}  {'u_err':>12s}  {'time':>6s}")

for ki in range(N_modes):
    t_mode = time.time()  # (local)
    sol = solve_ivp(
        bog_rhs, [TAU_START, TAU_END], y0,
        args=(ki,), method='Radau',
        rtol=1e-13, atol=1e-15,
        max_step=max_step_tau,
    )
    dt_mode = time.time() - t_mode  # (local)

    if not sol.success:
        print(f"    {str(labels[ki]):>8s}: SOLVER FAILED -- {sol.message}")
        continue

    ar_f = sol.y[0, -1]  # (local)
    ai_f = sol.y[1, -1]  # (local)
    br_f = sol.y[2, -1]  # (local)
    bi_f = sol.y[3, -1]  # (local)

    alpha_m1[ki] = ar_f + 1j*ai_f
    beta_m1[ki] = br_f + 1j*bi_f

    # Extract squeeze parameters
    beta_sq = abs(beta_m1[ki])**2  # (local)
    alpha_sq = abs(alpha_m1[ki])**2  # (local)

    # r_k from |beta_k|^2 = sinh^2(r_k)
    r_k_m1[ki] = np.arcsinh(np.sqrt(beta_sq))

    # phi_k = arg(beta_k) -- THE squeezing phase
    phi_k_m1[ki] = np.angle(beta_m1[ki])

    # Unitarity check
    unitarity_err_m1[ki] = alpha_sq - beta_sq - 1.0

    print(f"    {str(labels[ki]):>8s}  {beta_sq:14.8e}  {r_k_m1[ki]:10.6f}  "
          f"{phi_k_m1[ki]:+12.8f}  {phi_k_m1[ki]/PI:+10.6f}  "
          f"{unitarity_err_m1[ki]:+12.2e}  {dt_mode:6.1f}s")

print()
max_unit_err_m1 = np.max(np.abs(unitarity_err_m1))  # (local)
print(f"  CHK1 (Method 1): max |unitarity error| = {max_unit_err_m1:.2e}")
print(f"  Status: {'PASS' if max_unit_err_m1 < 1e-10 else 'FAIL'} (threshold 1e-10)")
print()

# =============================================================================
# SECTION 4: METHOD 2 -- Transfer matrix composition
# =============================================================================
#
# Decompose the tau domain into N_seg segments of constant omega_k.
# In each segment, the mode equation u'' + omega^2 u = 0 has the
# exact solution matrix:
#
#   M_j = [[cosh(gamma_j), sinh(gamma_j)/omega_j],
#          [omega_j*sinh(gamma_j), cosh(gamma_j)]]
#
# where gamma_j encodes the frequency change across the segment.
#
# For the Bogoliubov formulation, the transfer matrix between
# adjacent constant-frequency segments (omega_j -> omega_{j+1}) is:
#
#   T_j = (1/2) * [[alpha_j, conj(beta_j)],
#                   [beta_j, conj(alpha_j)]]
#
# with alpha_j = (omega_j + omega_{j+1})/(2*sqrt(omega_j*omega_{j+1}))
# and  beta_j  = (omega_j - omega_{j+1})/(2*sqrt(omega_j*omega_{j+1}))
# times phase factors exp(+/- i*omega_j*dtau_j).
# =============================================================================

print("=" * 78)
print("SECTION 4: METHOD 2 -- Transfer Matrix")
print("=" * 78)
print()

N_seg = 2000  # (local) number of segments
tau_edges = np.linspace(TAU_START, TAU_END, N_seg + 1)  # (local)
dtau_seg = (TAU_END - TAU_START) / N_seg  # (local)

# Storage for Method 2 results
alpha_m2 = np.zeros(N_modes, dtype=complex)  # (local)
beta_m2 = np.zeros(N_modes, dtype=complex)  # (local)
r_k_m2 = np.zeros(N_modes)  # (local)
phi_k_m2 = np.zeros(N_modes)  # (local)
unitarity_err_m2 = np.zeros(N_modes)  # (local)

print(f"  N_seg = {N_seg}, dtau = {dtau_seg:.6e}")
print()

for ki in range(N_modes):
    # Compute omega at segment midpoints
    tau_mids = 0.5*(tau_edges[:-1] + tau_edges[1:])  # (local)
    omega_seg = np.array([omega_k_of_tau(tau_mids[j], ki) for j in range(N_seg)])  # (local)

    # Compute velocity at segment midpoints (for phase accumulation)
    v_seg = np.array([np.sqrt(max(v_tau_sq(tau_mids[j]), 1e-30)) for j in range(N_seg)])  # (local)

    # Phase accumulated in each segment: phi_j = omega_j * dtau_j / v_j
    # (In the Bogoliubov formulation, phase rate is omega/v_tau)
    phase_seg = omega_seg * dtau_seg / v_seg  # (local)

    # Build compound transfer matrix S = prod_j S_j
    # Each S_j connects adjacent constant-omega regions:
    #   S_j = [[alpha_j, conj(beta_j)],
    #          [beta_j,  conj(alpha_j)]]
    #
    # For a step from omega_j to omega_{j+1} with accumulated phase:
    #   alpha_j = (w_j + w_{j+1})/(2*sqrt(w_j*w_{j+1})) * exp(i*phi_j)
    #   beta_j  = (w_j - w_{j+1})/(2*sqrt(w_j*w_{j+1})) * exp(-i*phi_j)

    S_total = np.eye(2, dtype=complex)  # (local)
    cum_phase = 0.0  # (local)

    for j in range(N_seg - 1):
        w1 = omega_seg[j]  # (local)
        w2 = omega_seg[j+1]  # (local)
        denom = 2.0 * np.sqrt(w1 * w2)  # (local)
        cum_phase += phase_seg[j]

        # Bogoliubov coefficients for step j -> j+1
        alpha_j = (w1 + w2) / denom * np.exp(1j * cum_phase)  # (local)
        beta_j = (w1 - w2) / denom * np.exp(-1j * cum_phase)  # (local)

        S_j = np.array([
            [alpha_j, np.conj(beta_j)],
            [beta_j, np.conj(alpha_j)]
        ], dtype=complex)  # (local)

        S_total = S_j @ S_total

    alpha_m2[ki] = S_total[0, 0]
    beta_m2[ki] = S_total[1, 0]

    beta_sq = abs(beta_m2[ki])**2  # (local)
    alpha_sq = abs(alpha_m2[ki])**2  # (local)
    r_k_m2[ki] = np.arcsinh(np.sqrt(beta_sq))
    phi_k_m2[ki] = np.angle(beta_m2[ki])
    unitarity_err_m2[ki] = alpha_sq - beta_sq - 1.0

print(f"  Transfer matrix results:")
print(f"  {'Mode':>8s}  {'|beta|^2':>14s}  {'r_k':>10s}  {'phi_k':>12s}  "
      f"{'phi_k/pi':>10s}  {'u_err':>12s}")
for ki in range(N_modes):
    print(f"    {str(labels[ki]):>8s}  {abs(beta_m2[ki])**2:14.8e}  {r_k_m2[ki]:10.6f}  "
          f"{phi_k_m2[ki]:+12.8f}  {phi_k_m2[ki]/PI:+10.6f}  "
          f"{unitarity_err_m2[ki]:+12.2e}")

print()
max_unit_err_m2 = np.max(np.abs(unitarity_err_m2))  # (local)
print(f"  CHK1 (Method 2): max |unitarity error| = {max_unit_err_m2:.2e}")
print(f"  Status: {'PASS' if max_unit_err_m2 < 1e-6 else 'FAIL'} (threshold 1e-6)")
print()

# =============================================================================
# SECTION 5: METHOD 3 -- Sudden approximation
# =============================================================================
#
# In the sudden (instantaneous) limit, the Bogoliubov coefficients for
# a frequency jump from omega_in to omega_out are:
#
#   alpha_sudden = (omega_in + omega_out) / (2 * sqrt(omega_in * omega_out))
#   beta_sudden  = (omega_in - omega_out) / (2 * sqrt(omega_in * omega_out))
#
# The sudden-limit beta is REAL and NEGATIVE (for omega_out > omega_in),
# giving phi_sudden = pi. For omega_out < omega_in, beta > 0, phi = 0.
#
# Deviation from pi (or 0) measures how far the transit is from sudden.
# =============================================================================

print("=" * 78)
print("SECTION 5: METHOD 3 -- Sudden Approximation")
print("=" * 78)
print()

omega_in = np.array([omega_k_of_tau(TAU_START, ki) for ki in range(N_modes)])  # (local)
omega_out = np.array([omega_k_of_tau(TAU_END, ki) for ki in range(N_modes)])  # (local)

alpha_sudden = (omega_in + omega_out) / (2.0 * np.sqrt(omega_in * omega_out))  # (local)
beta_sudden = (omega_in - omega_out) / (2.0 * np.sqrt(omega_in * omega_out))  # (local)

r_k_sudden = np.arcsinh(np.abs(beta_sudden))  # (local)
phi_k_sudden = np.where(beta_sudden > 0, 0.0, PI)  # (local)

print(f"  Sudden approximation (frequency endpoints only):")
print(f"  {'Mode':>8s}  {'omega_in':>12s}  {'omega_out':>12s}  {'|beta|':>12s}  "
      f"{'r_k':>10s}  {'phi_k/pi':>10s}")
for ki in range(N_modes):
    print(f"    {str(labels[ki]):>8s}  {omega_in[ki]:12.8f}  {omega_out[ki]:12.8f}  "
          f"{abs(beta_sudden[ki]):12.8e}  {r_k_sudden[ki]:10.6f}  "
          f"{phi_k_sudden[ki]/PI:10.4f}")
print()

# =============================================================================
# SECTION 6: Cross-check CHK2 -- Method consistency
# =============================================================================

print("=" * 78)
print("SECTION 6: Cross-check CHK2 -- Method Consistency")
print("=" * 78)
print()

# Method 1 vs Method 2 comparison
print("  Method 1 (ODE) vs Method 2 (Transfer Matrix):")
print(f"  {'Mode':>8s}  {'phi1':>12s}  {'phi2':>12s}  {'|diff|':>12s}  "
      f"{'r1':>10s}  {'r2':>10s}  {'|dr|':>10s}")
for ki in range(N_modes):
    dphi = abs(phi_k_m1[ki] - phi_k_m2[ki])  # (local)
    # Handle 2*pi wrap
    dphi = min(dphi, 2*PI - dphi)  # (local)
    dr = abs(r_k_m1[ki] - r_k_m2[ki])  # (local)
    print(f"    {str(labels[ki]):>8s}  {phi_k_m1[ki]:+12.8f}  {phi_k_m2[ki]:+12.8f}  "
          f"{dphi:12.8f}  {r_k_m1[ki]:10.6f}  {r_k_m2[ki]:10.6f}  {dr:10.6f}")

max_dphi_12 = 0.0  # (local)
max_dr_12 = 0.0  # (local)
for ki in range(N_modes):
    dp = abs(phi_k_m1[ki] - phi_k_m2[ki])  # (local)
    dp = min(dp, 2*PI - dp)  # (local)
    max_dphi_12 = max(max_dphi_12, dp)
    max_dr_12 = max(max_dr_12, abs(r_k_m1[ki] - r_k_m2[ki]))

print()
print(f"  Max |phi1 - phi2| = {max_dphi_12:.8f}")
print(f"  Max |r1 - r2|     = {max_dr_12:.8f}")
print()

# =============================================================================
# SECTION 7: Adopt best values and compare to Josephson prediction
# =============================================================================

print("=" * 78)
print("SECTION 7: Phase Analysis -- Josephson Comparison")
print("=" * 78)
print()

# Method 1 (ODE) is the most accurate -- use it as primary
phi_k_adopted = phi_k_m1.copy()  # (local)
r_k_adopted = r_k_m1.copy()  # (local)

# Josephson prediction: phi_eff = pi/4
phi_josephson = PI / 4  # (local) = 0.785398...

print(f"  Josephson prediction: phi_eff = pi/4 = {phi_josephson:.8f}")
print(f"  Gate window: [{phi_josephson - 0.3:.4f}, {phi_josephson + 0.3:.4f}]")
print()

# The S68 enhancement formula operates on the COMPOUND Bogoliubov
# coefficient. The BCS squeeze phase phi_k enters the compound
# S_total = S_exit * S_fold(r_k, phi_k) * S_entry.
#
# What we computed above (Methods 1-3) gives the phase of beta_k
# from the EXIT ODE alone (the z''/z pump field contribution).
# The BCS PAIRING phase comes from a different source: the time-dependent
# BdG equation through the gap opening.
#
# The total squeezing phase in the compound S_total is a combination
# of the entry phase, BCS phase, and exit phase. Let us now compute
# the compound Bogoliubov coefficients WITH the actual phases.

print("  Phase decomposition:")
print(f"  {'Mode':>8s}  {'phi_exit':>12s}  {'phi_exit/pi':>12s}  "
      f"{'r_exit':>10s}  {'r_bcs':>10s}")
for ki in range(N_modes):
    print(f"    {str(labels[ki]):>8s}  {phi_k_adopted[ki]:+12.8f}  "
          f"{phi_k_adopted[ki]/PI:+12.8f}  {r_k_adopted[ki]:10.6f}  "
          f"{r_k_bcs[ki]:10.6f}")
print()

# =============================================================================
# SECTION 8: Compound Bogoliubov with actual phases
# =============================================================================
#
# The compound Bogoliubov matrix is S_total = S_exit * S_BCS * S_entry.
#
# S_entry: thermal horizon crossing (effectively real, no phase structure)
#   alpha_e = sqrt(alpha_sq_entry), beta_e = sqrt(beta_sq_entry), both real
#
# S_BCS(r_k, phi_k): the BCS pairing squeeze
#   S_BCS = [[cosh(r_k), e^{i*phi_k}*sinh(r_k)],
#            [e^{-i*phi_k}*sinh(r_k), cosh(r_k)]]
#
# S_exit: z''/z pump contribution (from ODE)
#   alpha_exit, beta_exit are the complex coefficients from Method 1
#
# For the BCS squeeze phase, we need the time-dependent BdG solution.
# The BCS squeeze r_k_bcs came from the pairing amplitude, but
# the PHASE was set to 0 as a placeholder in S73B.
#
# The exit ODE already captures the full time-dependent frequency
# variation omega_k(tau) = sqrt(eps_k(tau)^2 + Delta(tau)^2) through
# the fold. The phase arg(beta_exit) = phi_k IS the squeeze phase
# from this channel.
#
# For the BCS pairing channel specifically, the gap Delta(tau) opens
# during the transit. The time-dependent BdG equation gives a SEPARATE
# Bogoliubov transformation with its own phase. However, in the
# compound Bogoliubov framework, the BCS r_k and the exit ODE
# phase are COMBINED as S_exit * S_BCS.
#
# Key structural point: the exit ODE solves for the TOTAL frequency
# variation including both eps_k(tau) and Delta(tau) changes.
# The BCS r_k_bcs was computed SEPARATELY from pairing alone.
# The compound S_total = S_exit * S_BCS * S_entry correctly
# separates these: S_exit has the dynamical phase from the
# time-dependent background, S_BCS has the pairing squeeze.
#
# The BCS pairing phase phi_BCS arises from the PHASE of the gap
# function Delta(tau). In the s-wave BCS case with real Gap,
# the BCS squeeze is along the real axis: phi_BCS = 0.
#
# But the S68 Landau-Transit workshop identified that the
# Josephson dynamics LOCK phi_eff = pi/4. This comes from
# the COLLECTIVE mode structure, not the microscopic BdG.
# Specifically, the Josephson frequency omega_J times the
# transit rise time tau_rise gives omega_J * tau_rise ~ 1.0,
# which rotates the squeeze axis by pi/4.
#
# To capture this, we need to include the exit ODE phase
# (which comes from the time-dependent background) in the
# compound calculation. The total effective phase is then
# the argument of the compound beta_total.
# =============================================================================

print("=" * 78)
print("SECTION 8: Compound Bogoliubov with Actual Phases")
print("=" * 78)
print()

def make_bog_matrix(alpha, beta):
    """Standard Bogoliubov matrix [[alpha, beta*], [beta, alpha*]]."""
    return np.array([
        [alpha, np.conj(beta)],
        [beta, np.conj(alpha)]
    ], dtype=complex)

def make_squeeze_matrix(r, phi=0.0):
    """Squeeze matrix S(r,phi) = [[cosh(r), e^{i*phi}*sinh(r)],
                                   [e^{-i*phi}*sinh(r), cosh(r)]]."""
    cr = np.cosh(r)  # (local)
    sr = np.sinh(r)  # (local)
    return np.array([
        [cr, np.exp(1j*phi) * sr],
        [np.exp(-1j*phi) * sr, cr]
    ], dtype=complex)

# Compute compound Bogoliubov for EACH BCS phase choice:
# (a) phi_BCS = 0 (the S73B default)
# (b) phi_BCS = exit ODE phase phi_k_m1 (dynamical)
# (c) phi_BCS = pi/4 (Josephson prediction)

alpha_total_phi0 = np.zeros(N_modes, dtype=complex)  # (local)
beta_total_phi0 = np.zeros(N_modes, dtype=complex)  # (local)
alpha_total_phidyn = np.zeros(N_modes, dtype=complex)  # (local)
beta_total_phidyn = np.zeros(N_modes, dtype=complex)  # (local)
alpha_total_phiJ = np.zeros(N_modes, dtype=complex)  # (local)
beta_total_phiJ = np.zeros(N_modes, dtype=complex)  # (local)

for ki in range(N_modes):
    # Entry stage (real coefficients)
    alpha_e = np.sqrt(alpha_sq_entry[ki])  # (local)
    beta_e = np.sqrt(beta_sq_entry[ki])  # (local)
    S_entry = make_bog_matrix(alpha_e, beta_e)

    # Exit stage (from Method 1 ODE)
    S_exit = make_bog_matrix(alpha_m1[ki], beta_m1[ki])

    # (a) phi_BCS = 0
    S_bcs_0 = make_squeeze_matrix(r_k_bcs[ki], phi=0.0)
    S_tot_0 = S_exit @ S_bcs_0 @ S_entry  # (local)
    alpha_total_phi0[ki] = S_tot_0[0, 0]
    beta_total_phi0[ki] = S_tot_0[1, 0]

    # (b) phi_BCS = exit ODE phase
    S_bcs_dyn = make_squeeze_matrix(r_k_bcs[ki], phi=phi_k_m1[ki])
    S_tot_dyn = S_exit @ S_bcs_dyn @ S_entry  # (local)
    alpha_total_phidyn[ki] = S_tot_dyn[0, 0]
    beta_total_phidyn[ki] = S_tot_dyn[1, 0]

    # (c) phi_BCS = pi/4 (Josephson)
    S_bcs_J = make_squeeze_matrix(r_k_bcs[ki], phi=PI/4)
    S_tot_J = S_exit @ S_bcs_J @ S_entry  # (local)
    alpha_total_phiJ[ki] = S_tot_J[0, 0]
    beta_total_phiJ[ki] = S_tot_J[1, 0]

# Effective phases from compound beta
phi_eff_0 = np.angle(beta_total_phi0)  # (local)
phi_eff_dyn = np.angle(beta_total_phidyn)  # (local)
phi_eff_J = np.angle(beta_total_phiJ)  # (local)

n_total_phi0 = np.abs(beta_total_phi0)**2  # (local)
n_total_phidyn = np.abs(beta_total_phidyn)**2  # (local)
n_total_phiJ = np.abs(beta_total_phiJ)**2  # (local)

print("  Compound Bogoliubov: occupation numbers |beta_total|^2:")
print(f"  {'Mode':>8s}  {'n(phi=0)':>14s}  {'n(phi=dyn)':>14s}  {'n(phi=pi/4)':>14s}")
for ki in range(N_modes):
    print(f"    {str(labels[ki]):>8s}  {n_total_phi0[ki]:14.4f}  "
          f"{n_total_phidyn[ki]:14.4f}  {n_total_phiJ[ki]:14.4f}")
print()

print("  Compound Bogoliubov: effective phases phi_eff = arg(beta_total):")
print(f"  {'Mode':>8s}  {'phi_eff(0)':>12s}  {'phi_eff(dyn)':>14s}  "
      f"{'phi_eff(J)':>12s}  {'phi_eff(0)/pi':>14s}  {'phi_eff(dyn)/pi':>16s}  "
      f"{'phi_eff(J)/pi':>14s}")
for ki in range(N_modes):
    print(f"    {str(labels[ki]):>8s}  {phi_eff_0[ki]:+12.8f}  "
          f"{phi_eff_dyn[ki]:+14.8f}  {phi_eff_J[ki]:+12.8f}  "
          f"{phi_eff_0[ki]/PI:+14.8f}  {phi_eff_dyn[ki]/PI:+16.8f}  "
          f"{phi_eff_J[ki]/PI:+14.8f}")
print()

# Unitarity check on compound
print("  Unitarity check (compound):")
for label_tag, alpha_arr, beta_arr in [
    ("phi=0", alpha_total_phi0, beta_total_phi0),
    ("phi=dyn", alpha_total_phidyn, beta_total_phidyn),
    ("phi=pi/4", alpha_total_phiJ, beta_total_phiJ)
]:
    u_err = np.abs(alpha_arr)**2 - np.abs(beta_arr)**2 - 1.0  # (local)
    print(f"    {label_tag:>8s}: max |err| = {np.max(np.abs(u_err)):.2e}")
print()

# =============================================================================
# SECTION 9: Enhancement factor with actual phases
# =============================================================================
#
# S68 Landau-Transit workshop enhancement formula:
#   A_s(total) = A_s(bare) * [cosh(2*r_eff) + (sqrt(2)/3)*sinh(2*r_eff)*cos(phi_eff)]
#
# The "effective" r and phi are the appropriate weighted averages
# over the 8 modes. We compute the enhancement for each scenario.
# =============================================================================

print("=" * 78)
print("SECTION 9: Enhancement Factor Analysis")
print("=" * 78)
print()

def enhancement_factor(r, phi):
    """S68 enhancement formula: cosh(2r) + (sqrt(2)/3)*sinh(2r)*cos(phi)."""
    return np.cosh(2*r) + (np.sqrt(2)/3)*np.sinh(2*r)*np.cos(phi)

# For each compound scenario, extract effective r and phi
# r_eff = arcsinh(sqrt(mean(|beta_total|^2))), or branch-weighted
# phi_eff = weighted-mean(arg(beta_total))

# Branch-weighted r_eff and phi_eff
W_B2 = np.sum(mode_weights[0:4])  # (local)
W_B1 = mode_weights[4]  # (local)
W_B3 = np.sum(mode_weights[5:8])  # (local)
W_tot = W_B2 + W_B1 + W_B3  # (local)

def weighted_eff(n_arr, phi_arr):
    """Compute weighted effective r_eff and phi_eff from 8-mode arrays."""
    # Average occupation per branch
    n_B2 = np.mean(n_arr[0:4])  # (local)
    n_B1 = n_arr[4]  # (local)
    n_B3 = np.mean(n_arr[5:8])  # (local)

    n_eff = W_B2*n_B2 + W_B1*n_B1 + W_B3*n_B3  # (local)
    r_eff = np.arcsinh(np.sqrt(n_eff / W_tot))  # (local)

    # Phase: use vector average (preserving phase coherence)
    # phi_eff = arg(sum_k w_k * |beta_k| * exp(i*phi_k))
    # This IS the coherent phase average
    beta_weighted = 0.0 + 0j  # (local)
    for ki_inner in range(N_modes):
        beta_weighted += mode_weights[ki_inner] * np.sqrt(n_arr[ki_inner]) * np.exp(1j*phi_arr[ki_inner])
    phi_eff = np.angle(beta_weighted)  # (local)

    return r_eff, phi_eff

r_eff_0, phi_eff_0_w = weighted_eff(n_total_phi0, phi_eff_0)  # (local)
r_eff_dyn, phi_eff_dyn_w = weighted_eff(n_total_phidyn, phi_eff_dyn)  # (local)
r_eff_J, phi_eff_J_w = weighted_eff(n_total_phiJ, phi_eff_J)  # (local)

print(f"  Effective parameters (branch-weighted):")
print(f"  {'Scenario':>12s}  {'r_eff':>10s}  {'phi_eff':>12s}  {'phi_eff/pi':>12s}  "
      f"{'Enhancement':>14s}  {'OOM':>8s}")
for tag, r_e, phi_e in [
    ("phi=0", r_eff_0, phi_eff_0_w),
    ("phi=dyn", r_eff_dyn, phi_eff_dyn_w),
    ("phi=pi/4", r_eff_J, phi_eff_J_w)
]:
    enh = enhancement_factor(r_e, phi_e)  # (local)
    oom = np.log10(enh) if enh > 0 else float('nan')  # (local)
    print(f"    {tag:>12s}  {r_e:10.6f}  {phi_e:+12.8f}  {phi_e/PI:+12.8f}  "
          f"{enh:14.6f}  {oom:+8.4f}")
print()

# Also compute per-mode enhancement
print("  Per-mode enhancement factors:")
print(f"  {'Mode':>8s}  {'r_bcs':>10s}  {'phi_exit':>12s}  {'Enhancement':>14s}")
for ki in range(N_modes):
    enh_mode = enhancement_factor(r_k_bcs[ki], phi_k_m1[ki])  # (local)
    print(f"    {str(labels[ki]):>8s}  {r_k_bcs[ki]:10.6f}  {phi_k_m1[ki]:+12.8f}  "
          f"{enh_mode:14.6f}")
print()

# =============================================================================
# SECTION 10: Gate verdict
# =============================================================================

print("=" * 78)
print("SECTION 10: Gate Verdict -- S75-C4-PHASES-BD")
print("=" * 78)
print()

# The gate tests whether phi_k (BCS squeeze phases) are near pi/4
# We use the exit ODE phases (Method 1) as the primary result
# These ARE the phases of the Bogoliubov beta_k from the mode equation

phi_gate_lo = phi_josephson - 0.3  # (local) = 0.485
phi_gate_hi = phi_josephson + 0.3  # (local) = 1.085

all_in_window = True  # (local)
any_near_pi4 = False  # (local)
phi_mean = np.mean(phi_k_m1)  # (local)

print(f"  Exit ODE phases (Method 1):")
print(f"  {'Mode':>8s}  {'phi_k':>12s}  {'phi_k/pi':>10s}  {'|phi-pi/4|':>12s}  {'In gate?':>10s}")
for ki in range(N_modes):
    dist = abs(phi_k_m1[ki] - phi_josephson)  # (local)
    in_gate = phi_gate_lo <= phi_k_m1[ki] <= phi_gate_hi  # (local)
    if not in_gate:
        all_in_window = False
    if dist < 0.3:
        any_near_pi4 = True
    print(f"    {str(labels[ki]):>8s}  {phi_k_m1[ki]:+12.8f}  {phi_k_m1[ki]/PI:+10.6f}  "
          f"{dist:12.8f}  {'YES' if in_gate else 'NO':>10s}")

print()
print(f"  Mean phi_k = {phi_mean:+.8f} ({phi_mean/PI:+.6f} pi)")
print(f"  Std  phi_k = {np.std(phi_k_m1):.8f}")
print(f"  |mean - pi/4| = {abs(phi_mean - phi_josephson):.8f}")
print()

# Compound effective phase analysis
print(f"  Compound effective phases:")
print(f"    phi_eff(phi_BCS=0):    {phi_eff_0_w:+.8f}  ({phi_eff_0_w/PI:+.6f} pi)")
print(f"    phi_eff(phi_BCS=dyn):  {phi_eff_dyn_w:+.8f}  ({phi_eff_dyn_w/PI:+.6f} pi)")
print(f"    phi_eff(phi_BCS=pi/4): {phi_eff_J_w:+.8f}  ({phi_eff_J_w/PI:+.6f} pi)")
print()

# Gate decision
if all_in_window:
    gate_verdict = "PASS"
    gate_detail = (f"All phi_k in [{phi_gate_lo:.3f}, {phi_gate_hi:.3f}]. "
                   f"Josephson prediction phi_eff=pi/4 confirmed. "
                   f"Mean phi = {phi_mean:.6f} ({phi_mean/PI:.4f}*pi)")
elif any_near_pi4 and abs(phi_mean - phi_josephson) < 0.5:
    gate_verdict = "INFO"
    gate_detail = (f"phi_k scattered but mean={phi_mean:.6f} ({phi_mean/PI:.4f}*pi) "
                   f"near pi/4. Not all in window [{phi_gate_lo:.3f}, {phi_gate_hi:.3f}].")
else:
    # Check if near pi (sudden quench) or scattered
    near_pi_count = sum(1 for p in phi_k_m1 if abs(abs(p) - PI) < 0.5)  # (local)
    if near_pi_count >= 4:
        gate_verdict = "FAIL"
        gate_detail = (f"{near_pi_count}/8 modes near pi (sudden quench limit). "
                       f"Mean phi = {phi_mean:.6f}. Josephson prediction NOT confirmed.")
    else:
        gate_verdict = "FAIL"
        gate_detail = (f"phi_k highly scattered. Mean={phi_mean:.6f}, std={np.std(phi_k_m1):.6f}. "
                       f"Not consistent with Josephson pi/4 or sudden pi.")

print(f"  Gate S75-C4-PHASES-BD: {gate_verdict}")
print(f"  Detail: {gate_detail}")
print()

# =============================================================================
# SECTION 11: Summary table
# =============================================================================

print("=" * 78)
print("SUMMARY TABLE")
print("=" * 78)
print()
print(f"{'Mode':>8s}  {'r_bcs':>8s}  {'r_exit':>8s}  {'phi_exit':>10s}  "
      f"{'phi/pi':>8s}  {'|phi-pi/4|':>10s}  {'n_total(0)':>12s}  {'n_total(J)':>12s}")
print("-" * 98)
for ki in range(N_modes):
    dist = abs(phi_k_m1[ki] - phi_josephson)  # (local)
    print(f"{str(labels[ki]):>8s}  {r_k_bcs[ki]:8.4f}  {r_k_m1[ki]:8.6f}  "
          f"{phi_k_m1[ki]:+10.6f}  {phi_k_m1[ki]/PI:+8.5f}  {dist:10.6f}  "
          f"{n_total_phi0[ki]:12.2f}  {n_total_phiJ[ki]:12.2f}")
print()

# =============================================================================
# SECTION 12: Save results
# =============================================================================

print("=" * 78)
print("SECTION 12: Saving results")
print("=" * 78)
print()

outfile = os.path.join(SCRIPT_DIR, 's75_phases_bd.npz')  # (local)
np.savez(outfile,
    # Gate metadata
    gate_name='S75-C4-PHASES-BD',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,

    # Mode labels
    labels=labels,
    N_modes=N_modes,

    # Method 1: ODE results
    alpha_m1_real=alpha_m1.real,
    alpha_m1_imag=alpha_m1.imag,
    beta_m1_real=beta_m1.real,
    beta_m1_imag=beta_m1.imag,
    r_k_m1=r_k_m1,
    phi_k_m1=phi_k_m1,
    unitarity_err_m1=unitarity_err_m1,

    # Method 2: Transfer matrix results
    alpha_m2_real=alpha_m2.real,
    alpha_m2_imag=alpha_m2.imag,
    beta_m2_real=beta_m2.real,
    beta_m2_imag=beta_m2.imag,
    r_k_m2=r_k_m2,
    phi_k_m2=phi_k_m2,
    unitarity_err_m2=unitarity_err_m2,

    # Method 3: Sudden approximation
    r_k_sudden=r_k_sudden,
    phi_k_sudden=phi_k_sudden,

    # BCS squeeze parameters (from prior work)
    r_k_bcs=r_k_bcs,
    omega_k_fold=omega_k_fold,
    mode_weights=mode_weights,

    # Compound Bogoliubov effective phases
    phi_eff_compound_0=phi_eff_0,
    phi_eff_compound_dyn=phi_eff_dyn,
    phi_eff_compound_J=phi_eff_J,
    n_total_phi0=n_total_phi0,
    n_total_phidyn=n_total_phidyn,
    n_total_phiJ=n_total_phiJ,

    # Weighted effective parameters
    r_eff_phi0=r_eff_0,
    phi_eff_weighted_0=phi_eff_0_w,
    r_eff_phidyn=r_eff_dyn,
    phi_eff_weighted_dyn=phi_eff_dyn_w,
    r_eff_phiJ=r_eff_J,
    phi_eff_weighted_J=phi_eff_J_w,

    # Enhancement factors
    enh_phi0=enhancement_factor(r_eff_0, phi_eff_0_w),
    enh_phidyn=enhancement_factor(r_eff_dyn, phi_eff_dyn_w),
    enh_phiJ=enhancement_factor(r_eff_J, phi_eff_J_w),

    # Integration parameters
    TAU_START=TAU_START,
    TAU_END=TAU_END,
    N_TAU=N_TAU,
    N_seg=N_seg,

    # Josephson reference
    phi_josephson=phi_josephson,
)

print(f"  Saved: {outfile}")
print()

# =============================================================================
# SECTION 13: Diagnostic plot
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # (local)

# Panel 1: phi_k vs mode index
ax = axes[0, 0]  # (local)
ax.bar(range(N_modes), phi_k_m1, color='steelblue', alpha=0.8, label='Method 1 (ODE)')
ax.axhline(y=phi_josephson, color='red', linestyle='--', linewidth=2, label=r'$\pi/4$ (Josephson)')
ax.axhspan(phi_gate_lo, phi_gate_hi, color='red', alpha=0.1, label='Gate window')
ax.set_xticks(range(N_modes))
ax.set_xticklabels([str(l) for l in labels], rotation=45)
ax.set_ylabel(r'$\phi_k$ (squeeze phase)')
ax.set_title('Exit ODE Squeeze Phases')
ax.legend(fontsize=8)

# Panel 2: r_k comparison
ax = axes[0, 1]  # (local)
x_pos = np.arange(N_modes)  # (local)
width = 0.35  # (local)
ax.bar(x_pos - width/2, r_k_bcs, width, label='BCS (pairing)', color='coral')
ax.bar(x_pos + width/2, r_k_m1, width, label='Exit ODE', color='steelblue')
ax.set_xticks(x_pos)
ax.set_xticklabels([str(l) for l in labels], rotation=45)
ax.set_ylabel(r'$r_k$ (squeeze magnitude)')
ax.set_title('Squeeze Magnitudes')
ax.legend(fontsize=8)

# Panel 3: Method comparison for phi
ax = axes[1, 0]  # (local)
ax.scatter(range(N_modes), phi_k_m1, s=100, marker='o', label='Method 1 (ODE)', zorder=3)
ax.scatter(range(N_modes), phi_k_m2, s=60, marker='s', label='Method 2 (Transfer)', zorder=2)
ax.axhline(y=phi_josephson, color='red', linestyle='--', linewidth=1.5, label=r'$\pi/4$')
ax.set_xticks(range(N_modes))
ax.set_xticklabels([str(l) for l in labels], rotation=45)
ax.set_ylabel(r'$\phi_k$')
ax.set_title('Method Comparison: Squeeze Phases')
ax.legend(fontsize=8)

# Panel 4: Compound effective phases
ax = axes[1, 1]  # (local)
for ki in range(N_modes):
    ax.plot([0, 1, 2], [phi_eff_0[ki], phi_eff_dyn[ki], phi_eff_J[ki]],
            'o-', alpha=0.6, label=str(labels[ki]) if ki < 3 else None)
ax.axhline(y=phi_josephson, color='red', linestyle='--', linewidth=1.5)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels([r'$\phi_{BCS}=0$', r'$\phi_{BCS}=\mathrm{dyn}$', r'$\phi_{BCS}=\pi/4$'])
ax.set_ylabel(r'$\phi_{\mathrm{eff}}$ (compound)')
ax.set_title('Compound Effective Phases')
ax.legend(fontsize=7, ncol=2)

plt.tight_layout()
plotfile = os.path.join(SCRIPT_DIR, 's75_phases_bd.png')  # (local)
plt.savefig(plotfile, dpi=150)
print(f"  Plot saved: {plotfile}")
plt.close()

t_total = time.time() - t_start  # (local)
print()
print(f"Total runtime: {t_total:.1f}s")
print("=" * 78)
print("PHASES-BD-75 COMPLETE")
print("=" * 78)
