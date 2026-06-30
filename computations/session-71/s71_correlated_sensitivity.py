#!/usr/bin/env python3
"""
s71_correlated_sensitivity.py -- CORRELATED-SENSITIVITY-71
==========================================================

Gate: CORRELATED-SENSITIVITY-71
  INFO: Report sensitivity coefficient d(ln omega_L)/d(alpha) and omega_L range.
  Robust if |d(ln omega_L)/d(alpha)| < 0.5.
  Sensitive if |d(ln omega_L)/d(alpha)| > 2.0.

Physics:
--------
The Leggett frequency omega_L = 0.138 M_KK (GL-JOSEPHSON-52) emerges from the
inter-sector Josephson coupling in the 3-band BCS Hamiltonian on M^4 x SU(3).
The GL-Josephson spectrum is computed from:

  V_phase * x = omega^2 * T_phase * x

where V_phase is the phase stiffness matrix (Josephson coupling) and T_phase
is the Anderson-Bogoliubov inertia matrix (superfluid density * gap^2).

The spectral function f(x) = x^{alpha/2} parametrizes a family of spectral
functionals. The canonical choice is alpha = 1 (f(x) = sqrt(x)), giving the
framework's cutoff spectral action. Varying alpha modifies:

  1. The effective gauge coupling: g^2 ~ 1/a_4(alpha), where a_4(alpha) is the
     4th Seeley-DeWitt coefficient extracted from S_alpha.
  2. The BCS pairing interaction: lambda_BCS = g * rho(E_F).
  3. The BCS gaps: Delta_alpha ~ omega_D * exp(-1/lambda_BCS).
  4. The Josephson couplings: J_{ij} ~ g^2 * |<i|T^a|j>|^2.
  5. The Leggett frequency: omega_L^2 = eigenvalue of V_phase / T_phase.

CONTEXT FROM W1-A (NON-PERT-SA-70):
  The spectral action naturally terminates at L=6 (L=7 modes decouple because
  omega_min(L=7) = 2.153 > Lambda = 2.048). S_inf = 2.353 with 10.2% truncation
  error. The zeta action (alpha -> analytic continuation) eliminates f_0 entirely.

This computation scans alpha in {0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0} and
propagates the modified spectral action through the BCS chain to omega_L,
measuring the correlated sensitivity coefficient d(ln omega_L)/d(alpha).

FUNCTIONAL CLASSIFICATION: GEOMETRIC
  This computation concerns the spectral triple structure and its sensitivity
  to the choice of spectral functional. The Leggett frequency is a property
  of the fiber eigenvalue spectrum, not of excitations per se.

Author: Lizzi Spectral Functional Theorist
Session: S71, Wave 3-B
"""

import numpy as np
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.linalg import eigh

from canonical_constants import (
    # Spectral action
    a0_fold, a2_fold, a4_fold,
    S_fold, tau_fold, Vol_SU3_Haar, PI,
    # BCS quantities
    Delta_0_GL, Delta_0_OES, Delta_BCS, Delta_B3,
    E_cond, rho_B2_per_mode,
    E_B1, E_B2_mean, E_B3_mean,
    # Josephson
    J_C2, J_su2, J_u1,
    # Leggett (canonical)
    omega_L1, omega_L2,
    # GL coefficients
    a_GL, b_GL,
    # Gauge
    g_SU2_fold, g_U1_fold,
    # Other
    M_KK, M_KK_gravity,
    xi_BCS, IBO_ratio, N_dof_BCS,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8,
    collect_spectrum,
)

from spectral_action import dim_su3_irrep

# =============================================================================
# STEP 0: CONFIGURATION
# =============================================================================
print("=" * 78)
print("CORRELATED-SENSITIVITY-71: Leggett Frequency Sensitivity to alpha")
print("=" * 78)

t0_global = time.time()

# Alpha values to scan (task-specified)
alpha_scan = np.array([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0])
n_alpha = len(alpha_scan)

# Dense grid for smooth derivatives
alpha_dense = np.linspace(0.25, 1.05, 81)

# Tau grid centered on fold for BCS chain computation
tau_grid = np.array([0.0, 0.05, 0.10, 0.15, 0.16, 0.17, 0.18, 0.19,
                     0.20, 0.21, 0.22, 0.25, 0.30, 0.35, 0.40, 0.50])
n_tau = len(tau_grid)
idx_fold = np.argmin(np.abs(tau_grid - tau_fold))

print(f"""
  Spectral function family: f_alpha(x) = x^{{alpha/2}}
  Alpha values: {alpha_scan}
  Tau grid: {n_tau} points, fold at index {idx_fold} (tau = {tau_grid[idx_fold]:.2f})
  Canonical: omega_L1 = {omega_L1} M_KK at alpha = 1
""")

# =============================================================================
# STEP 1: COMPUTE EIGENVALUE SPECTRUM (max_pq_sum=6 for L_max=6)
# =============================================================================
print("=" * 78)
print("STEP 1: Eigenvalue Spectrum (max_pq_sum=6) at all tau values")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# Store per-tau eigenvalue data: list of (p, q, eigenvalues) per tau
all_eval_data = []

t_start = time.time()
for i_tau, tau in enumerate(tau_grid):
    _, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                   max_pq_sum=6, verbose=False)
    all_eval_data.append(eval_data)
    if (i_tau + 1) % 4 == 0 or i_tau == n_tau - 1:
        print(f"  tau[{i_tau}] = {tau:.2f} done ({time.time()-t_start:.1f}s)")

dt_spec = time.time() - t_start
print(f"\n  Total: {n_tau} spectra in {dt_spec:.1f}s")

# =============================================================================
# STEP 2: COMPUTE S_alpha(tau) FOR EACH ALPHA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: S_alpha(tau) for alpha scan")
print("=" * 78)

# S_alpha[i_alpha, i_tau] = sum d_pq^2 * sum |lambda_j|^alpha
S_alpha_grid = np.zeros((n_alpha, n_tau))

for ia, alpha in enumerate(alpha_scan):
    for it in range(n_tau):
        S_val = 0.0  # (local)
        for p, q, evals in all_eval_data[it]:
            d_pq = dim_su3_irrep(p, q)
            omega = np.abs(evals)
            mask = omega > 1e-12
            omega_nz = omega[mask]
            S_val += d_pq**2 * np.sum(omega_nz**alpha)
        S_alpha_grid[ia, it] = S_val

# Cross-check: alpha=1 should match S_fold at max_pq_sum=6
# Note: S_fold is computed at max_pq_sum=3, so we expect a different value
# but can verify the ratio is consistent with L_max scaling
idx_a1 = np.argmin(np.abs(alpha_scan - 1.0))
S_a1_fold = S_alpha_grid[idx_a1, idx_fold]

print(f"\n  S_alpha at fold (tau = {tau_fold}) with max_pq_sum=6:")
print(f"  {'alpha':>6}  {'S_alpha':>16}  {'S/S(alpha=1)':>14}")
print(f"  {'-----':>6}  {'-'*16}  {'-'*14}")
for ia, alpha in enumerate(alpha_scan):
    S_val = S_alpha_grid[ia, idx_fold]
    ratio = S_val / S_a1_fold if S_a1_fold > 0 else 0
    print(f"  {alpha:6.2f}  {S_val:16.5f}  {ratio:14.6f}")

print(f"\n  S(alpha=1, fold, L_max=6) = {S_a1_fold:.5f}")
print(f"  S_fold (canonical, L_max=3) = {S_fold:.5f}")
print(f"  Ratio L_max=6/L_max=3 = {S_a1_fold/S_fold:.4f}")

# =============================================================================
# STEP 3: EXTRACT EFFECTIVE a_4(alpha)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Extract effective a_4(alpha) from spectral action")
print("=" * 78)

# The spectral action has the heat kernel expansion:
#   S_alpha(tau) = sum_{k} c_k(alpha) * a_{2k}(tau) * Lambda^{d-2k+alpha*correction}
#
# For the direct spectral sum, we extract a_4 by comparing S_alpha to
# the known form S(tau) = sum d^2 * sum |lambda|^alpha.
#
# The key insight: a_4 controls the Yang-Mills kinetic term.
# For different alpha, the RELATIVE weight of different eigenvalue
# ranges changes. High alpha weights UV (large |lambda|) more.
#
# The effective a_4(alpha) is defined through the gauge coupling:
#   1/g^2(alpha) propto sum d^2 * sum |lambda|^{alpha-2} * lambda^2
#
# However, for the BCS chain, what matters is how the full spectral
# action changes, which modifies g^2, and hence lambda_BCS, Delta, J, omega_L.
#
# Approach: Rather than extracting individual Seeley-DeWitt coefficients
# (which mix in a complex way for general alpha), we compute the
# FRACTIONAL CHANGE in the spectral action and propagate through the chain.
#
# The spectral action derivatives dS/dtau and d2S/dtau2 at the fold
# determine the BCS pairing through the gradient of the effective potential.
# The Leggett frequency is set by the curvature of the inter-sector coupling.

# For each alpha, fit S_alpha(tau) with cubic spline and extract derivatives
dS_dtau_arr = np.zeros(n_alpha)
d2S_dtau2_arr = np.zeros(n_alpha)
S_at_fold_arr = np.zeros(n_alpha)

for ia in range(n_alpha):
    cs = CubicSpline(tau_grid, S_alpha_grid[ia, :])
    S_at_fold_arr[ia] = cs(tau_fold)
    dS_dtau_arr[ia] = cs(tau_fold, 1)
    d2S_dtau2_arr[ia] = cs(tau_fold, 2)

print(f"\n  Spectral action derivatives at fold:")
print(f"  {'alpha':>6}  {'S(fold)':>14}  {'dS/dtau':>14}  {'d2S/dtau2':>14}")
print(f"  {'-----':>6}  {'-'*14}  {'-'*14}  {'-'*14}")
for ia, alpha in enumerate(alpha_scan):
    print(f"  {alpha:6.2f}  {S_at_fold_arr[ia]:14.5f}  "
          f"{dS_dtau_arr[ia]:14.5f}  {d2S_dtau2_arr[ia]:14.5f}")

# =============================================================================
# STEP 4: LOAD BCS GROUND STATE DATA AND GL PARAMETERS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Load BCS Ground State (s48) and GL Parameters")
print("=" * 78)

leggett_data = np.load(os.path.join(SCRIPT_DIR, "s48_leggett_mode.npz"),
                       allow_pickle=True)

Delta_fold_vec = leggett_data['Delta_fold']  # [Delta_B1, Delta_B2, Delta_B3]
rho_fold_vec = leggett_data['rho_fold']      # [rho_B1, rho_B2, rho_B3]
J_12_ref = float(leggett_data['J_12_fold'])
J_23_ref = float(leggett_data['J_23_fold'])
J_13_ref = float(leggett_data['J_13_fold'])

Delta_B1, Delta_B2, Delta_B3_val = Delta_fold_vec
rho_B1, rho_B2, rho_B3 = rho_fold_vec

print(f"  BCS ground state at tau = {tau_fold}:")
print(f"    Delta = [{Delta_B1:.6f}, {Delta_B2:.6f}, {Delta_B3_val:.6f}] M_KK")
print(f"    rho   = [{rho_B1:.4f}, {rho_B2:.4f}, {rho_B3:.4f}]")
print(f"    J_12  = {J_12_ref:.6e}")
print(f"    J_23  = {J_23_ref:.6e}")
print(f"    J_13  = {J_13_ref:.6e}")

# Load s52 GL-Josephson data for the canonical V_phase_0 and T_phase
gl_data = np.load(os.path.join(SCRIPT_DIR, "s52_gl_josephson.npz"),
                  allow_pickle=True)
V_phase_0_ref = gl_data['V_phase_0']   # 3x3 phase stiffness at K=0
T_phase_ref = gl_data['T_phase']       # 3x3 Anderson-Bogoliubov inertia
omega_L1_s52 = float(gl_data['omega_branches'][0, 1])  # Leggett-1 at K=0

print(f"\n  GL-Josephson (S52) at K=0:")
print(f"    omega_L1 = {omega_L1_s52:.6f} M_KK")
print(f"    omega_L2 = {float(gl_data['omega_branches'][0, 2]):.6f} M_KK")
print(f"    Canonical: omega_L1 = {omega_L1} M_KK")

# Verify reconstruction: diagonalize V_phase / T_phase
evals_ref, evecs_ref = eigh(V_phase_0_ref, T_phase_ref)
omega_reconstructed = np.sqrt(np.maximum(evals_ref, 0))
print(f"\n  Reconstructed from V_phase/T_phase:")
print(f"    omega = {omega_reconstructed}")
print(f"    omega_L1_reconstructed = {omega_reconstructed[1]:.6f} M_KK")
print(f"    Match to S52: {abs(omega_reconstructed[1] - omega_L1_s52) < 1e-6}")

# =============================================================================
# STEP 5: PROPAGATE ALPHA THROUGH THE BCS CHAIN TO omega_L
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Propagate alpha-dependence through BCS chain")
print("=" * 78)

# The chain of dependence:
#
# 1. S_alpha(tau) determines the effective gauge coupling.
#    At alpha=1: g^2 ~ 1/a_4. For general alpha, the spectral action
#    S_alpha = sum d^2 * sum |lambda|^alpha reweights eigenvalues.
#    The effective coupling is:
#      g^2(alpha) propto [S_alpha(fold)]^{-1} * [normalisation]
#    More precisely, the gauge kinetic term in the spectral action is:
#      S_YM = sum d^2 * sum_j lambda_j^{alpha-2} * (D_mu F)_j^2
#    So the coupling scales as:
#      1/g^2(alpha) propto sum d^2 * sum |lambda_j|^{alpha}
#    (The full YM extraction involves the Casimir structure, but the
#    alpha-dependence enters through the spectral weight.)
#
# 2. Therefore g^2(alpha) / g^2(1) = S(1, fold) / S(alpha, fold)
#    This is the key scaling relation.
#
# 3. The BCS pairing strength lambda_BCS = g(alpha) * rho(E_F).
#    rho(E_F) is a SPECTRAL property (eigenvalue density at Fermi level).
#    It does NOT depend on alpha -- alpha is the spectral function
#    exponent, not a property of the D_K eigenvalue spectrum itself.
#    The eigenvalues of D_K are alpha-independent.
#
# 4. Delta_alpha(alpha) ~ omega_D * exp(-1/lambda_BCS(alpha))
#    This exponential amplifies the coupling change.
#
# 5. J_{ij}(alpha) ~ g^2(alpha) * |<i|T|j>|^2
#    The overlap integral is alpha-independent (set by D_K eigenvectors).
#
# 6. The GL phase stiffness matrix V_phase scales as:
#    V_phase(alpha) = V_phase_ref * [J(alpha)/J_ref]
#    where J(alpha)/J_ref = [g^2(alpha)/g^2_ref] * [Delta(alpha)/Delta_ref]^2
#
# 7. The inertia matrix T_phase scales as:
#    T_phase(alpha) = T_phase_ref * [rho(alpha)/rho_ref] * [Delta(alpha)/Delta_ref]^2
#    Since rho is alpha-independent: T_phase(alpha) = T_phase_ref * [Delta(alpha)/Delta_ref]^2

# Reference values (alpha=1)
S_ref = S_at_fold_arr[idx_a1]
g2_ref = g_SU2_fold  # = 2.052

# BCS pairing parameters
omega_D = 2.0 * 0.835  # Debye cutoff ~ 2 * min eigenvalue (S70)
lambda_BCS_B2 = -1.0 / np.log(Delta_B2 / omega_D)
lambda_BCS_B3 = -1.0 / np.log(Delta_B3_val / omega_D)
lambda_BCS_avg = -1.0 / np.log(Delta_BCS / omega_D)

print(f"  Reference (alpha=1):")
print(f"    S_ref = {S_ref:.5f}")
print(f"    g^2_ref = {g2_ref:.4f}")
print(f"    lambda_BCS_B2 = {lambda_BCS_B2:.4f}")
print(f"    lambda_BCS_B3 = {lambda_BCS_B3:.4f}")
print(f"    omega_D = {omega_D:.4f}")

# Compute omega_L for each alpha
omega_L1_arr = np.zeros(n_alpha)
omega_L2_arr = np.zeros(n_alpha)
g2_arr = np.zeros(n_alpha)
lambda_BCS_B2_arr = np.zeros(n_alpha)
lambda_BCS_B3_arr = np.zeros(n_alpha)
Delta_B2_arr = np.zeros(n_alpha)
Delta_B3_arr_val = np.zeros(n_alpha)
Delta_B1_arr = np.zeros(n_alpha)

print(f"\n  {'alpha':>6}  {'g^2':>8}  {'lam_B2':>8}  {'lam_B3':>8}  "
      f"{'Delta_B2':>10}  {'Delta_B3':>10}  {'omega_L1':>10}  {'omega_L2':>10}")
print(f"  {'-----':>6}  {'-'*8}  {'-'*8}  {'-'*8}  "
      f"{'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

for ia, alpha in enumerate(alpha_scan):
    # Step 1: g^2(alpha) = g^2_ref * S_ref / S_alpha
    S_alpha_fold = S_at_fold_arr[ia]
    g2_alpha = g2_ref * S_ref / S_alpha_fold
    g2_arr[ia] = g2_alpha

    # Step 2: lambda_BCS(alpha) = g(alpha) * rho (rho is alpha-independent)
    # lambda = g * rho, so lambda(alpha) / lambda(1) = g(alpha) / g(1) = sqrt(g2(alpha)/g2_ref)
    g_ratio = np.sqrt(g2_alpha / g2_ref)

    lam_B2 = lambda_BCS_B2 * g_ratio
    lam_B3 = lambda_BCS_B3 * g_ratio
    lambda_BCS_B2_arr[ia] = lam_B2
    lambda_BCS_B3_arr[ia] = lam_B3

    # Step 3: Delta(alpha) = omega_D * exp(-1/lambda(alpha))
    Delta_B2_a = omega_D * np.exp(-1.0 / lam_B2)
    Delta_B3_a = omega_D * np.exp(-1.0 / lam_B3)
    # B1 sector: same scaling
    lambda_BCS_B1 = -1.0 / np.log(Delta_B1 / omega_D)
    lam_B1 = lambda_BCS_B1 * g_ratio
    Delta_B1_a = omega_D * np.exp(-1.0 / lam_B1)

    Delta_B2_arr[ia] = Delta_B2_a
    Delta_B3_arr_val[ia] = Delta_B3_a
    Delta_B1_arr[ia] = Delta_B1_a

    Delta_vec_alpha = np.array([Delta_B1_a, Delta_B2_a, Delta_B3_a])

    # Step 4: Scale V_phase and T_phase
    # V_phase_{ij} ~ J_{ij} * |Delta_i| * |Delta_j| where J_{ij} ~ g^2 * overlap
    # So V_phase(alpha) = V_phase_ref * (g2_alpha/g2_ref) * (Delta_i(a)*Delta_j(a))/(Delta_i_ref*Delta_j_ref)
    Delta_ref_vec = np.array([Delta_B1, Delta_B2, Delta_B3_val])

    # Build scaling matrix for V_phase
    V_scale = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            if abs(Delta_ref_vec[i]) > 1e-15 and abs(Delta_ref_vec[j]) > 1e-15:
                V_scale[i, j] = (g2_alpha / g2_ref) * \
                    (Delta_vec_alpha[i] * Delta_vec_alpha[j]) / \
                    (Delta_ref_vec[i] * Delta_ref_vec[j])
            else:
                V_scale[i, j] = 1.0

    V_phase_alpha = V_phase_0_ref * V_scale

    # T_phase = diag(rho_i * Delta_i^2) -- rho is alpha-independent
    T_phase_alpha = np.diag(rho_fold_vec * Delta_vec_alpha**2)

    # Step 5: Solve generalized eigenvalue problem
    # V_phase * x = omega^2 * T_phase * x
    try:
        evals_a, _ = eigh(V_phase_alpha, T_phase_alpha)
        omega_a = np.sqrt(np.maximum(evals_a, 0))
        omega_L1_arr[ia] = omega_a[1]  # First non-zero = Leggett-1
        omega_L2_arr[ia] = omega_a[2]  # Second = Leggett-2
    except Exception as e:
        print(f"  WARNING: eigenvalue problem failed at alpha={alpha}: {e}")
        omega_L1_arr[ia] = np.nan
        omega_L2_arr[ia] = np.nan

    print(f"  {alpha:6.2f}  {g2_alpha:8.4f}  {lam_B2:8.4f}  {lam_B3:8.4f}  "
          f"{Delta_B2_a:10.6f}  {Delta_B3_a:10.6f}  "
          f"{omega_L1_arr[ia]:10.6f}  {omega_L2_arr[ia]:10.6f}")

# =============================================================================
# STEP 6: COMPUTE SENSITIVITY COEFFICIENT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Sensitivity Coefficient d(ln omega_L)/d(alpha)")
print("=" * 78)

# Use cubic spline interpolation on the full scan for smooth derivative
mask_valid = ~np.isnan(omega_L1_arr)
alpha_valid = alpha_scan[mask_valid]
omega_L1_valid = omega_L1_arr[mask_valid]
omega_L2_valid = omega_L2_arr[mask_valid]

if len(alpha_valid) >= 3:
    # Fit cubic spline to ln(omega_L1) vs alpha
    ln_omega_L1 = np.log(omega_L1_valid)
    cs_L1 = CubicSpline(alpha_valid, ln_omega_L1)

    # Evaluate derivative at alpha=1 (if in range) or at canonical alpha=0.5
    # Note: alpha=1 may be at the edge. Evaluate at center of scan too.
    alpha_eval_pts = [0.5, 0.7, 1.0]
    print(f"\n  d(ln omega_L1)/d(alpha) at specific alpha values:")
    for a_eval in alpha_eval_pts:
        if a_eval >= alpha_valid[0] and a_eval <= alpha_valid[-1]:
            deriv = cs_L1(a_eval, 1)
            print(f"    alpha = {a_eval:.1f}: d(ln omega_L1)/d(alpha) = {deriv:+.4f}")

    # Primary result: evaluate at canonical alpha=1
    if 1.0 <= alpha_valid[-1]:
        sensitivity_L1 = float(cs_L1(1.0, 1))
    else:
        # Extrapolate from last valid point
        sensitivity_L1 = float(cs_L1(alpha_valid[-1], 1))

    # Also compute finite-difference sensitivity near alpha=1
    # Use the two points closest to alpha=1
    idx_08 = np.argmin(np.abs(alpha_scan - 0.8))
    idx_10 = np.argmin(np.abs(alpha_scan - 1.0))
    if not np.isnan(omega_L1_arr[idx_08]) and not np.isnan(omega_L1_arr[idx_10]):
        fd_sensitivity = (np.log(omega_L1_arr[idx_10]) - np.log(omega_L1_arr[idx_08])) / \
                        (alpha_scan[idx_10] - alpha_scan[idx_08])
        print(f"\n  Finite-difference check (alpha=0.8->1.0):")
        print(f"    d(ln omega_L1)/d(alpha) = {fd_sensitivity:+.4f}")

    # Leggett-2 sensitivity
    ln_omega_L2 = np.log(omega_L2_valid)
    cs_L2 = CubicSpline(alpha_valid, ln_omega_L2)
    if 1.0 <= alpha_valid[-1]:
        sensitivity_L2 = float(cs_L2(1.0, 1))
    else:
        sensitivity_L2 = float(cs_L2(alpha_valid[-1], 1))

    print(f"\n  SENSITIVITY COEFFICIENTS:")
    print(f"    d(ln omega_L1)/d(alpha) |_{{alpha=1}} = {sensitivity_L1:+.4f}")
    print(f"    d(ln omega_L2)/d(alpha) |_{{alpha=1}} = {sensitivity_L2:+.4f}")
    print(f"    |sensitivity_L1| = {abs(sensitivity_L1):.4f}")

    # Classification
    if abs(sensitivity_L1) < 0.5:
        class_L1 = "ROBUST (|d(ln omega_L)/d(alpha)| < 0.5)"
    elif abs(sensitivity_L1) > 2.0:
        class_L1 = "STRONGLY SCHEME-DEPENDENT (|d(ln omega_L)/d(alpha)| > 2.0)"
    else:
        class_L1 = "MODERATELY SENSITIVE (0.5 < |d(ln omega_L)/d(alpha)| < 2.0)"

    print(f"\n  Classification: {class_L1}")

else:
    sensitivity_L1 = np.nan
    sensitivity_L2 = np.nan
    class_L1 = "INSUFFICIENT DATA"
    print("  WARNING: Too few valid data points for sensitivity computation")

# =============================================================================
# STEP 7: omega_L RANGE ACROSS ALPHA SCAN
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: omega_L Range and Fractional Variation")
print("=" * 78)

omega_L1_min = np.nanmin(omega_L1_arr)
omega_L1_max = np.nanmax(omega_L1_arr)
omega_L1_at_1 = omega_L1_arr[idx_a1]

frac_range = (omega_L1_max - omega_L1_min) / omega_L1_at_1

print(f"  omega_L1 range:")
print(f"    min = {omega_L1_min:.6f} M_KK (at alpha = {alpha_scan[np.nanargmin(omega_L1_arr)]:.1f})")
print(f"    max = {omega_L1_max:.6f} M_KK (at alpha = {alpha_scan[np.nanargmax(omega_L1_arr)]:.1f})")
print(f"    at alpha=1: {omega_L1_at_1:.6f} M_KK")
print(f"    canonical:   {omega_L1} M_KK")
print(f"    fractional range: {frac_range:.4f} ({frac_range*100:.1f}%)")

omega_L2_min = np.nanmin(omega_L2_arr)
omega_L2_max = np.nanmax(omega_L2_arr)
omega_L2_at_1 = omega_L2_arr[idx_a1]

frac_range_L2 = (omega_L2_max - omega_L2_min) / omega_L2_at_1

print(f"\n  omega_L2 range:")
print(f"    min = {omega_L2_min:.6f} M_KK (at alpha = {alpha_scan[np.nanargmin(omega_L2_arr)]:.1f})")
print(f"    max = {omega_L2_max:.6f} M_KK (at alpha = {alpha_scan[np.nanargmax(omega_L2_arr)]:.1f})")
print(f"    at alpha=1: {omega_L2_at_1:.6f} M_KK")
print(f"    canonical:   {omega_L2} M_KK")
print(f"    fractional range: {frac_range_L2:.4f} ({frac_range_L2*100:.1f}%)")

# =============================================================================
# STEP 8: DECOMPOSE INTO STRUCTURAL VS SCHEME-DEPENDENT COMPONENTS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Structural Analysis")
print("=" * 78)

print("""
  CHAIN OF alpha-DEPENDENCE:

  alpha --> S_alpha(fold) --> g^2(alpha) --> lambda_BCS(alpha) --> Delta(alpha) --> omega_L(alpha)
          [direct]         [~1/S]          [~ sqrt(g^2)*rho]    [exp(-1/lam)]    [sqrt(J/rhoD^2)]

  STRUCTURAL (alpha-INDEPENDENT) components:
    - D_K eigenvalue spectrum {lambda_j}: set by Jensen deformation, NOT by alpha
    - rho(E_F): density of states at Fermi level, from eigenvalue distribution
    - Overlap integrals <i|T^a|j>: set by eigenvectors of D_K
    - Sector structure (B1, B2, B3): block-diagonal structure (proven S22)

  SCHEME-DEPENDENT (alpha-DEPENDENT) components:
    - S_alpha = sum d^2 * sum |lambda|^alpha: UV weighting changes with alpha
    - g^2(alpha): effective coupling changes
    - lambda_BCS(alpha): pairing strength (exponentially amplified)
    - Delta(alpha): BCS gap (exponentially sensitive through BCS gap equation)
    - omega_L(alpha): propagated through V_phase and T_phase
""")

# Print the fractional changes at each stage
print(f"  Fractional changes relative to alpha=1:")
print(f"  {'alpha':>6}  {'S/S_ref':>10}  {'g2/g2_ref':>10}  {'lam_B2/ref':>10}  "
      f"{'D_B2/ref':>10}  {'wL1/ref':>10}")
print(f"  {'-----':>6}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")

for ia, alpha in enumerate(alpha_scan):
    s_r = S_at_fold_arr[ia] / S_ref
    g2_r = g2_arr[ia] / g2_ref
    lam_r = lambda_BCS_B2_arr[ia] / lambda_BCS_B2
    d_r = Delta_B2_arr[ia] / Delta_B2
    wl_r = omega_L1_arr[ia] / omega_L1_at_1 if omega_L1_at_1 > 0 else np.nan
    print(f"  {alpha:6.2f}  {s_r:10.6f}  {g2_r:10.6f}  {lam_r:10.6f}  "
          f"{d_r:10.6f}  {wl_r:10.6f}")

# =============================================================================
# STEP 9: COMPARISON WITH eps_H SENSITIVITY (S70)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Cross-Reference with eps_H Sensitivity (S70)")
print("=" * 78)

# S70 EPSH-ALPHA-70 found d(ln eps_H)/d(alpha) = 1.076 (moderately sensitive)
epsh_sensitivity = 1.076  # (local)
print(f"  eps_H sensitivity (S70): d(ln eps_H)/d(alpha) = {epsh_sensitivity:.3f}")
print(f"  omega_L sensitivity (this): d(ln omega_L)/d(alpha) = {sensitivity_L1:+.4f}")
print(f"  Ratio: |omega_L| / |eps_H| = {abs(sensitivity_L1) / abs(epsh_sensitivity):.3f}")

if abs(sensitivity_L1) < abs(epsh_sensitivity):
    print(f"  omega_L is LESS sensitive to alpha than eps_H")
else:
    print(f"  omega_L is MORE sensitive to alpha than eps_H")

# =============================================================================
# STEP 10: PLOT AND SAVE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Plot and Save Results")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("CORRELATED-SENSITIVITY-71: omega_L vs Spectral Function alpha", fontsize=14)

# Panel 1: omega_L1 vs alpha
ax1 = axes[0, 0]
ax1.plot(alpha_scan, omega_L1_arr, 'bo-', ms=8, label='omega_L1')
ax1.axhline(omega_L1, color='r', ls='--', alpha=0.5, label=f'canonical {omega_L1}')
ax1.axvline(1.0, color='gray', ls=':', alpha=0.3)
ax1.set_xlabel('alpha')
ax1.set_ylabel('omega_L1 (M_KK)')
ax1.set_title('Leggett-1 Frequency vs alpha')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Panel 2: omega_L2 vs alpha
ax2 = axes[0, 1]
ax2.plot(alpha_scan, omega_L2_arr, 'rs-', ms=8, label='omega_L2')
ax2.axhline(omega_L2, color='b', ls='--', alpha=0.5, label=f'canonical {omega_L2}')
ax2.axvline(1.0, color='gray', ls=':', alpha=0.3)
ax2.set_xlabel('alpha')
ax2.set_ylabel('omega_L2 (M_KK)')
ax2.set_title('Leggett-2 Frequency vs alpha')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Panel 3: S_alpha at fold (normalized)
ax3 = axes[1, 0]
ax3.plot(alpha_scan, S_at_fold_arr / S_ref, 'gD-', ms=8)
ax3.axhline(1.0, color='gray', ls='--', alpha=0.3)
ax3.set_xlabel('alpha')
ax3.set_ylabel('S_alpha / S(alpha=1)')
ax3.set_title('Normalized Spectral Action at Fold')
ax3.grid(True, alpha=0.3)

# Panel 4: BCS chain ratios
ax4 = axes[1, 1]
ax4.plot(alpha_scan, g2_arr / g2_ref, 'ko-', ms=6, label='g^2/g^2_ref')
ax4.plot(alpha_scan, lambda_BCS_B2_arr / lambda_BCS_B2, 'b^-', ms=6, label='lambda_B2/lambda_ref')
ax4.plot(alpha_scan, Delta_B2_arr / Delta_B2, 'rv-', ms=6, label='Delta_B2/Delta_ref')
ax4.plot(alpha_scan, omega_L1_arr / omega_L1_at_1, 'gs-', ms=6, label='omega_L1/omega_ref')
ax4.axhline(1.0, color='gray', ls='--', alpha=0.3)
ax4.set_xlabel('alpha')
ax4.set_ylabel('Ratio to alpha=1 value')
ax4.set_title('BCS Chain Propagation')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's71_correlated_sensitivity.png'), dpi=150)
print(f"  Plot saved: s71_correlated_sensitivity.png")

# Save data
np.savez(os.path.join(SCRIPT_DIR, 's71_correlated_sensitivity.npz'),
         # Gate info
         gate_name='CORRELATED-SENSITIVITY-71',
         gate_verdict='INFO',
         gate_detail=f'd(ln omega_L1)/d(alpha)={sensitivity_L1:+.4f}, '
                     f'omega_L1 range [{omega_L1_min:.6f}, {omega_L1_max:.6f}] M_KK, '
                     f'classification: {class_L1}',
         # Alpha scan
         alpha_scan=alpha_scan,
         # Spectral action
         S_alpha_at_fold=S_at_fold_arr,
         dS_dtau=dS_dtau_arr,
         d2S_dtau2=d2S_dtau2_arr,
         # BCS chain
         g2_arr=g2_arr,
         lambda_BCS_B2_arr=lambda_BCS_B2_arr,
         lambda_BCS_B3_arr=lambda_BCS_B3_arr,
         Delta_B2_arr=Delta_B2_arr,
         Delta_B3_arr=Delta_B3_arr_val,
         Delta_B1_arr=Delta_B1_arr,
         # Leggett frequencies
         omega_L1_arr=omega_L1_arr,
         omega_L2_arr=omega_L2_arr,
         # Sensitivity
         sensitivity_L1=sensitivity_L1,
         sensitivity_L2=sensitivity_L2,
         # Reference values
         omega_L1_ref=omega_L1_at_1,
         omega_L2_ref=omega_L2_at_1,
         omega_L1_canonical=omega_L1,
         omega_L2_canonical=omega_L2,
         S_ref=S_ref,
         g2_ref=g2_ref,
         lambda_BCS_B2_ref=lambda_BCS_B2,
         lambda_BCS_B3_ref=lambda_BCS_B3,
         )
print(f"  Data saved: s71_correlated_sensitivity.npz")

# =============================================================================
# SUMMARY
# =============================================================================
dt_total = time.time() - t0_global
print("\n" + "=" * 78)
print("SUMMARY: CORRELATED-SENSITIVITY-71")
print("=" * 78)

print(f"""
  Gate: CORRELATED-SENSITIVITY-71
  Verdict: INFO

  PRIMARY RESULT:
    d(ln omega_L1)/d(alpha) |_{{alpha=1}} = {sensitivity_L1:+.4f}
    d(ln omega_L2)/d(alpha) |_{{alpha=1}} = {sensitivity_L2:+.4f}

  LEGGETT FREQUENCY RANGE (alpha in [{alpha_scan[0]}, {alpha_scan[-1]}]):
    omega_L1: [{omega_L1_min:.6f}, {omega_L1_max:.6f}] M_KK
    omega_L1 at alpha=1: {omega_L1_at_1:.6f} M_KK
    Fractional variation: {frac_range*100:.1f}%

    omega_L2: [{omega_L2_min:.6f}, {omega_L2_max:.6f}] M_KK
    omega_L2 at alpha=1: {omega_L2_at_1:.6f} M_KK
    Fractional variation: {frac_range_L2*100:.1f}%

  CLASSIFICATION: {class_L1}

  COMPARISON WITH eps_H (S70):
    |d(ln omega_L)/d(alpha)| = {abs(sensitivity_L1):.3f}
    |d(ln eps_H)/d(alpha)|   = {epsh_sensitivity:.3f}
    Ratio: {abs(sensitivity_L1)/epsh_sensitivity:.3f}

  FUNCTIONAL-INDEPENDENCE ASSESSMENT:
    The Leggett frequency propagates alpha-dependence through the BCS chain:
    alpha -> S_alpha -> g^2 -> lambda_BCS -> Delta -> V_phase/T_phase -> omega_L
    The exponential BCS gap equation amplifies the coupling change,
    but the Leggett frequency involves ratios (V/T) that partially cancel.

  Total runtime: {dt_total:.1f}s
""")
