#!/usr/bin/env python3
"""
LEGGETT-PROPAGATOR-50: 3-Pole Propagator from Inter-Sector Josephson Coupling
==============================================================================

Physics:
  S49 proved alpha_s = n_s^2 - 1 = -0.069 for the O-Z propagator (EXACT).
  6-sigma tension with Planck. The escape hypothesis: the BCS state on SU(3)
  has 3 inter-sector bands coupled by Josephson interaction, giving a 3-pole
  propagator instead of a single O-Z pole.

  KEY STRUCTURAL THEOREM (derived here):
  When all 3 sectors share the same spatial stiffness (same lattice geometry),
  the 3-pole propagator decomposes as:
    P(K) = sum_{i=1}^3 <1/(J_eff(Omega)*K^2 + lambda_i)>_angle
  where lambda_i = m_base^2 + sigma_i are the eigenvalues of the total mass
  matrix M_total = m_base^2 * I + M_Jos.

  Each term is a standard O-Z propagator with mass^2 = lambda_i.
  The identity alpha_s = n_s^2 - 1 holds for EACH pole individually.
  For the SUM, the identity breaks by a correction term proportional to
  the spectral weight derivatives dw_i/d(ln K).

  The magnitude of breaking depends on (sigma_max - sigma_min) / m_base^2,
  where sigma_i are the Josephson eigenvalues and m_base^2 is the universal
  mass from the n_s constraint.

  For the physical couplings:
    sigma_max = 0.072 M_KK^2 (Leggett 2)
    m_base^2 = 140 M_KK^2 (from n_s = 0.965)
    Splitting ratio: 0.05% — poles are nearly degenerate
  This means the 3-pole propagator is indistinguishable from the O-Z form.

Gate: LEGGETT-PROPAGATOR-50
  PASS: alpha_s in [-0.040, 0] AND n_s in [0.950, 0.980]
  FAIL: alpha_s still satisfies n_s^2 - 1 (3-pole reduces to O-Z)
  INFO: alpha_s deviates from n_s^2 - 1 but outside Planck range

Author: landau-condensed-matter-theorist
Session: S50 W1-A
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

t0 = time.time()

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, N_cells, M_KK, M_KK_gravity,
    E_cond, Delta_0_GL, Delta_0_OES, Delta_B3,
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    xi_BCS, xi_GL, omega_PV, PI,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 78)
print("LEGGETT-PROPAGATOR-50: 3-Pole Propagator from Inter-Sector Josephson")
print("=" * 78)

# =============================================================================
# STEP 1: Load upstream data
# =============================================================================
print("\n--- Step 1: Load Upstream Data ---")

d_legg = np.load(os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz'), allow_pickle=True)
J_12 = float(d_legg['J_12_fold'])
J_23 = float(d_legg['J_23_fold'])
J_13 = float(d_legg['J_13_fold'])
omega_L1 = float(d_legg['omega_L1_fold'])
omega_L2 = float(d_legg['omega_L2_fold'])
Delta_fold = np.array(d_legg['Delta_fold'])
rho_fold = np.array(d_legg['rho_fold'])

d_oz = np.load(os.path.join(SCRIPT_DIR, 's48_aniso_oz.npz'), allow_pickle=True)
J_C2 = float(d_oz['J_C2'])
J_su2 = float(d_oz['J_su2'])
J_u1 = float(d_oz['J_u1'])
K_pivot = float(d_oz['K_pivot_lattice'])
T_acoustic = float(d_oz['T_acoustic'])
m_star_s48 = float(d_oz['m_star_angular'])
alpha_s_s48 = float(d_oz['alpha_s_framework'])

nx_lat, ny_lat, nz_lat = 4, 4, 2

print(f"  Josephson couplings (M_KK units):")
print(f"    J_12 (B1-B2) = {J_12:.6f}")
print(f"    J_23 (B2-B3) = {J_23:.6f}")
print(f"    J_13 (B1-B3) = {J_13:.6f}")
print(f"    J_12/J_23    = {J_12/J_23:.2f}")
print(f"  BCS gaps: {Delta_fold}")
print(f"  Sector DOS: {rho_fold}")
print(f"  Leggett: omega_L1={omega_L1:.5f}, omega_L2={omega_L2:.5f}")
print(f"  Lattice: J_C2={J_C2:.4f}, J_su2={J_su2:.4f}, K_pivot={K_pivot:.4f}")

# =============================================================================
# STEP 2: Construct mass matrices
# =============================================================================
print("\n--- Step 2: Mass Matrix Construction ---")

# Josephson mass matrix (Leggett 1966)
M_Jos = np.array([
    [J_12 + J_13,  -J_12,        -J_13],
    [-J_12,         J_12 + J_23,  -J_23],
    [-J_13,        -J_23,         J_13 + J_23]
])

evals_Jos, evecs_Jos = eigh(M_Jos)
print(f"  Josephson eigenvalues: {evals_Jos}")
print(f"    Zero mode: {evals_Jos[0]:.2e} (Goldstone)")
print(f"    Leggett 1: {evals_Jos[1]:.6f}")
print(f"    Leggett 2: {evals_Jos[2]:.6f}")

# Effective isotropic stiffness (all sectors share the same lattice)
J_eff = (2*J_C2 + J_su2) / 3.0
eps_pivot = J_eff * K_pivot**2

print(f"  Spatial stiffness: J_eff = {J_eff:.6f}")
print(f"  epsilon(K_pivot) = J_eff*K^2 = {eps_pivot:.4f}")
print(f"  Josephson/epsilon ratio: sigma_max/eps = {evals_Jos[2]/eps_pivot:.6f}")

# =============================================================================
# STEP 3: Angular sampling (fixed for all computations)
# =============================================================================

N_ANGLE = 30000
rng_fixed = np.random.RandomState(42)
theta_s = np.arccos(2*rng_fixed.random(N_ANGLE) - 1)
phi_s = 2*PI*rng_fixed.random(N_ANGLE)
nx_h = np.sin(theta_s)*np.cos(phi_s)
ny_h = np.sin(theta_s)*np.sin(phi_s)
nz_h = np.cos(theta_s)
J_eff_dir = J_C2*(nx_h**2 + ny_h**2) + J_su2*nz_h**2

# =============================================================================
# STEP 4: Core propagator functions
# =============================================================================

def P_3pole(K_val, m_base_sq, M_mass):
    """Angular-averaged 3-pole propagator. All sectors share same stiffness."""
    M_total = m_base_sq * np.eye(3) + M_mass
    lam = np.linalg.eigvalsh(M_total)
    eps = J_eff_dir * K_val**2
    return sum(np.mean(1.0 / (eps + lam[i])) for i in range(3)), lam

def P_OZ(K_val, m_sq):
    """Angular-averaged single-pole O-Z propagator."""
    eps = J_eff_dir * K_val**2
    return np.mean(1.0 / (eps + m_sq))

def ns_from_P_func(P_func, K_pivot_val, dK=0.005):
    """Compute n_s via central difference."""
    K_p = K_pivot_val * (1 + dK)
    K_m = K_pivot_val * (1 - dK)
    P_p = P_func(K_p)
    P_m = P_func(K_m)
    return 1.0 + (np.log(P_p) - np.log(P_m)) / (np.log(K_p) - np.log(K_m))

def ns_alpha_from_P_func(P_func, K_pivot_val):
    """Compute n_s and alpha_s via 7-point quadratic fit."""
    K_factors = np.array([0.85, 0.90, 0.95, 1.00, 1.05, 1.10, 1.15])
    K_pts = K_pivot_val * K_factors
    P_pts = np.array([P_func(K) for K in K_pts])

    ln_K = np.log(K_pts) - np.log(K_pivot_val)
    ln_P = np.log(P_pts)
    c = np.polyfit(ln_K, ln_P, 2)
    n_s = 1.0 + c[1]
    alpha_s = 2.0 * c[0]

    # Also get n_s at each K for cross-check
    ns_at_K = np.zeros(len(K_pts) - 2)
    for j in range(1, len(K_pts) - 1):
        dl_K = np.log(K_pts[j+1]) - np.log(K_pts[j-1])
        dl_P = np.log(P_pts[j+1]) - np.log(P_pts[j-1])
        ns_at_K[j-1] = 1.0 + dl_P / dl_K

    return n_s, alpha_s, K_pts, P_pts, K_pts[1:-1], ns_at_K

# =============================================================================
# STEP 5: Root-finding for m_base (3-pole, n_s = 0.965)
# =============================================================================
print("\n--- Step 5: Root-Finding for m_base ---")

target_ns = 0.965

# Linear bisection with arithmetic mean (more stable than geometric for this problem)
m_lo, m_hi = 8.0, 15.0
for iteration in range(100):
    m_mid = (m_lo + m_hi) / 2.0
    ns_mid = ns_from_P_func(lambda K: P_3pole(K, m_mid**2, M_Jos)[0], K_pivot)
    if ns_mid < target_ns:
        m_lo = m_mid
    else:
        m_hi = m_mid
    if abs(ns_mid - target_ns) < 1e-8:
        break

m_base = (m_lo + m_hi) / 2.0
m_base_sq = m_base**2
ns_at_m = ns_from_P_func(lambda K: P_3pole(K, m_base_sq, M_Jos)[0], K_pivot)
print(f"  m_base = {m_base:.8f}")
print(f"  m_base^2 = {m_base_sq:.4f}")
print(f"  n_s = {ns_at_m:.10f} (target: {target_ns})")
print(f"  Iterations: {iteration+1}")

# =============================================================================
# STEP 6: Root-finding for m_star (O-Z, n_s = 0.965)
# =============================================================================
print("\n--- Step 6: O-Z Reference ---")

m_lo_oz, m_hi_oz = 8.0, 15.0
for iteration in range(100):
    m_mid_oz = (m_lo_oz + m_hi_oz) / 2.0
    ns_mid_oz = ns_from_P_func(lambda K: P_OZ(K, m_mid_oz**2), K_pivot)
    if ns_mid_oz < target_ns:
        m_lo_oz = m_mid_oz
    else:
        m_hi_oz = m_mid_oz
    if abs(ns_mid_oz - target_ns) < 1e-8:
        break

m_star_OZ = (m_lo_oz + m_hi_oz) / 2.0
ns_oz_check = ns_from_P_func(lambda K: P_OZ(K, m_star_OZ**2), K_pivot)
print(f"  m_star_OZ = {m_star_OZ:.8f}")
print(f"  n_s = {ns_oz_check:.10f}")

# =============================================================================
# STEP 7: Full n_s and alpha_s computation
# =============================================================================
print("\n--- Step 7: Full n_s and alpha_s ---")

n_s_3p, alpha_s_3p, K_pts_3p, P_pts_3p, K_mid_3p, ns_at_K_3p = \
    ns_alpha_from_P_func(lambda K: P_3pole(K, m_base_sq, M_Jos)[0], K_pivot)

n_s_oz, alpha_s_oz, K_pts_oz, P_pts_oz, K_mid_oz, ns_at_K_oz = \
    ns_alpha_from_P_func(lambda K: P_OZ(K, m_star_OZ**2), K_pivot)

# Analytic continuum isotropic result (S49 identity)
# n_s = 0.965 => alpha_s = n_s^2 - 1 = -0.068775
alpha_s_analytic = target_ns**2 - 1

print(f"  3-POLE RESULTS:")
print(f"    n_s     = {n_s_3p:.10f}")
print(f"    alpha_s = {alpha_s_3p:.10f}")
print(f"    n_s^2-1 = {n_s_3p**2 - 1:.10f}")
print(f"    Deviation: alpha_s - (n_s^2-1) = {alpha_s_3p - (n_s_3p**2-1):.10f}")

print(f"\n  O-Z SINGLE-POLE RESULTS:")
print(f"    n_s     = {n_s_oz:.10f}")
print(f"    alpha_s = {alpha_s_oz:.10f}")
print(f"    n_s^2-1 = {n_s_oz**2 - 1:.10f}")
print(f"    Deviation: alpha_s - (n_s^2-1) = {alpha_s_oz - (n_s_oz**2-1):.10f}")

print(f"\n  COMPARISON:")
print(f"    Delta(n_s) = {n_s_3p - n_s_oz:.10f}")
print(f"    Delta(alpha_s) = {alpha_s_3p - alpha_s_oz:.10f}")
print(f"    3-pole dev - O-Z dev = {(alpha_s_3p - (n_s_3p**2-1)) - (alpha_s_oz - (n_s_oz**2-1)):.10f}")

# The deviation from the analytic identity has TWO components:
# (a) Numerical discretization (7-point quadratic fit vs true derivative)
# (b) Anisotropy (angular averaging vs isotropic)
# (c) Multi-pole splitting
# Components (a) and (b) are COMMON to both 3-pole and O-Z.
# Component (c) is SPECIFIC to the 3-pole case.
# So the GENUINE multi-pole effect is:
#   Delta = (3-pole deviation) - (O-Z deviation)

multi_pole_effect = (alpha_s_3p - (n_s_3p**2-1)) - (alpha_s_oz - (n_s_oz**2-1))
print(f"\n  GENUINE MULTI-POLE EFFECT:")
print(f"    Delta(alpha_s) = {multi_pole_effect:.10e}")
print(f"    |Delta|/|alpha_s| = {abs(multi_pole_effect)/abs(alpha_s_3p):.4e}")

# =============================================================================
# STEP 8: Pole structure
# =============================================================================
print("\n--- Step 8: Pole Structure ---")

M_total = m_base_sq * np.eye(3) + M_Jos
lam_total, U_total = eigh(M_total)
mu_poles = np.sqrt(lam_total)

print(f"  Pole masses (M_total eigenvalues):")
for i in range(3):
    print(f"    Pole {i+1}: mu = {mu_poles[i]:.8f}, mu^2 = {lam_total[i]:.6f}")

split = (lam_total[2] - lam_total[0]) / lam_total[0]
print(f"\n  Pole splitting: (lam_3-lam_1)/lam_1 = {split:.8f} ({100*split:.4f}%)")
print(f"  m_base^2 = {m_base_sq:.4f}")
print(f"  Josephson max eigenvalue = {evals_Jos[2]:.6f}")
print(f"  Ratio Josephson/m_base^2 = {evals_Jos[2]/m_base_sq:.6f}")

# Spectral weights at pivot
P_per_pole_pivot = np.array([P_OZ(K_pivot, lam_total[i]) for i in range(3)])
w_poles = P_per_pole_pivot / np.sum(P_per_pole_pivot)

print(f"\n  Spectral weights at K_pivot:")
for i in range(3):
    print(f"    w_{i+1} = {w_poles[i]:.8f}")
print(f"  Max weight difference: {(w_poles.max() - w_poles.min()):.6e}")

# Per-pole n_s and alpha_s
ns_per_pole = np.zeros(3)
alpha_per_pole = np.zeros(3)
for i in range(3):
    ns_i, alpha_i, _, _, _, _ = ns_alpha_from_P_func(
        lambda K, lam_i=lam_total[i]: P_OZ(K, lam_i), K_pivot)
    ns_per_pole[i] = ns_i
    alpha_per_pole[i] = alpha_i

print(f"\n  Per-pole spectral indices:")
for i in range(3):
    print(f"    Pole {i+1}: n_s = {ns_per_pole[i]:.8f}, "
          f"alpha_s = {alpha_per_pole[i]:.10f}, "
          f"n_s^2-1 = {ns_per_pole[i]**2-1:.10f}")

# =============================================================================
# STEP 9: Analytic estimate of the multi-pole correction
# =============================================================================
print("\n--- Step 9: Analytic Multi-Pole Correction ---")

# For the sum P = sum_i P_i, the running of n_s involves the weight derivatives.
# At leading order in the splitting delta_lam = lam_i - lam_0:
#   n_s(sum) - n_s(single) ~ O(delta_lam^2 / lam_0^2)
#   alpha_s(sum) - alpha_s(single) ~ O(delta_lam / lam_0 * (n_s - 1))
#
# More precisely: the correction to alpha_s from the spectral weight evolution is:
#   Delta(alpha_s) = sum_i (dw_i/d ln K) * (n_s_i - 1)
# where n_s_i - 1 ~ -2*eps/(eps + lam_i) and
#   dw_i/d ln K = w_i * [(n_s_i - 1) - (n_s_avg - 1)]
# (the weight of a softer pole increases at lower K because it decays slower).
#
# Numerically estimate:

K_test = K_pivot * np.array([0.995, 1.005])
w_test = np.zeros((3, 2))
for j, K_t in enumerate(K_test):
    P_poles_t = np.array([P_OZ(K_t, lam_total[i]) for i in range(3)])
    w_test[:, j] = P_poles_t / np.sum(P_poles_t)

dw_dlnK = (w_test[:, 1] - w_test[:, 0]) / (np.log(K_test[1]) - np.log(K_test[0]))
correction = np.sum(dw_dlnK * (ns_per_pole - 1.0))

print(f"  Weight derivatives dw_i/d(ln K):")
for i in range(3):
    print(f"    dw_{i+1}/d(ln K) = {dw_dlnK[i]:.6e}")
print(f"  Correction term = sum dw_i * (n_s_i - 1) = {correction:.6e}")
print(f"  This should match the multi-pole effect: {multi_pole_effect:.6e}")

# The correction is tiny because:
# (a) All weights are ~ 1/3 (splitting is 0.05%)
# (b) All n_s_i are nearly identical
# (c) dw_i/d ln K ~ O(split) * w_i

# To get O(1) corrections, we need splitting comparable to m_base^2,
# i.e., Josephson couplings J ~ m_base^2 ~ 140.
# The physical couplings are J_12 = 0.035, J_23 = 0.002 — a factor
# ~4000 too small.

J_needed = m_base_sq / 10  # to get 10% splitting
print(f"\n  SCALING ESTIMATE:")
print(f"    m_base^2 = {m_base_sq:.1f}")
print(f"    Current J_max = {evals_Jos[2]:.4f}")
print(f"    J needed for 10% splitting = {J_needed:.1f}")
print(f"    Enhancement factor needed: {J_needed/evals_Jos[2]:.0f}x")
print(f"    Enhancement factor for 1% alpha_s shift: ~{m_base_sq/(10*evals_Jos[2]):.0f}x")

# =============================================================================
# STEP 10: Josephson strength scan
# =============================================================================
print("\n--- Step 10: Josephson Coupling Scan ---")

# Scale M_Jos by large factors to map when the identity truly breaks
J_factors = np.array([0, 1, 10, 50, 100, 200, 500, 1000, 2000, 4000])
scan_results = []

for f in J_factors:
    M_Jos_f = f * M_Jos

    # Find m_base
    m_lo_f, m_hi_f = 1.0, 500.0
    for _ in range(100):
        m_mid_f = (m_lo_f + m_hi_f) / 2.0
        ns_f = ns_from_P_func(lambda K, m2=m_mid_f**2: P_3pole(K, m2, M_Jos_f)[0], K_pivot)
        if ns_f < target_ns:
            m_lo_f = m_mid_f
        else:
            m_hi_f = m_mid_f
        if abs(ns_f - target_ns) < 1e-6:
            break

    m_f = (m_lo_f + m_hi_f) / 2.0
    ns_f, alpha_f, _, _, _, _ = ns_alpha_from_P_func(
        lambda K, m2=m_f**2: P_3pole(K, m2, M_Jos_f)[0], K_pivot)

    # Pole structure
    M_tot_f = m_f**2 * np.eye(3) + M_Jos_f
    lam_f = np.linalg.eigvalsh(M_tot_f)
    spread_f = (lam_f[2] - lam_f[0]) / lam_f[0]

    # O-Z identity deviation
    dev_f = alpha_f - (ns_f**2 - 1)

    scan_results.append({
        'factor': f,
        'n_s': ns_f,
        'alpha_s': alpha_f,
        'identity': ns_f**2 - 1,
        'deviation': dev_f,
        'm_base': m_f,
        'spread': spread_f,
        'lam': lam_f.copy(),
    })

    print(f"  J x {f:5d}: n_s={ns_f:.6f}, alpha_s={alpha_f:+.6f}, "
          f"n_s^2-1={ns_f**2-1:+.6f}, dev={dev_f:+.8f}, "
          f"split={spread_f:.4f}")

# =============================================================================
# STEP 11: Dense P(K) curves
# =============================================================================
print("\n--- Step 11: P(K) Spectrum ---")

K_dense = np.logspace(np.log10(0.3), np.log10(8.0), 100)
P_3p_dense = np.array([P_3pole(K, m_base_sq, M_Jos)[0] for K in K_dense])
P_oz_dense = np.array([P_OZ(K, m_star_OZ**2) for K in K_dense])
P_poles_dense = np.array([[P_OZ(K, lam_total[i]) for K in K_dense] for i in range(3)])

# n_s(K) curves
ns_3p_dense = np.zeros(len(K_dense))
ns_oz_dense = np.zeros(len(K_dense))
for j in range(1, len(K_dense) - 1):
    dln_K = np.log(K_dense[j+1]) - np.log(K_dense[j-1])

    dln_P_3p = np.log(P_3p_dense[j+1]) - np.log(P_3p_dense[j-1])
    ns_3p_dense[j] = 1.0 + dln_P_3p / dln_K

    dln_P_oz = np.log(P_oz_dense[j+1]) - np.log(P_oz_dense[j-1])
    ns_oz_dense[j] = 1.0 + dln_P_oz / dln_K

# =============================================================================
# STEP 12: Gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: LEGGETT-PROPAGATOR-50")
print("=" * 78)

# The genuine multi-pole effect on alpha_s
identity_deviation_3p = abs(alpha_s_3p - (n_s_3p**2 - 1))
identity_deviation_oz = abs(alpha_s_oz - (n_s_oz**2 - 1))
genuine_effect = abs(multi_pole_effect)

# The 3-pole propagator gives alpha_s ~ -0.067 (same as O-Z to 4 decimal places)
# The identity deviation is shared with O-Z (numerical artifact of 7-point fit)
# The GENUINE multi-pole effect is < 10^{-6}

# Verdict: the 3-pole form REDUCES to effective O-Z because
# Josephson splitting (0.072 M_KK^2) << m_base^2 (140 M_KK^2)
# The poles are 99.95% degenerate.

alpha_in_pass = -0.040 <= alpha_s_3p <= 0.0
ns_in_pass = 0.950 <= n_s_3p <= 0.980

# The identity effectively holds: the genuine multi-pole effect is negligible
identity_effectively_holds = genuine_effect < 0.001  # less than 0.1% of alpha_s

if alpha_in_pass and ns_in_pass and not identity_effectively_holds:
    verdict = "PASS"
    detail = (f"alpha_s = {alpha_s_3p:.6f} in [-0.040, 0], "
              f"n_s = {n_s_3p:.6f} in [0.950, 0.980], "
              f"genuine multi-pole effect = {genuine_effect:.2e}")
elif identity_effectively_holds:
    verdict = "FAIL"
    detail = (f"3-pole alpha_s = {alpha_s_3p:.6f} matches O-Z alpha_s = {alpha_s_oz:.6f} "
              f"to {abs(alpha_s_3p-alpha_s_oz):.1e}. Genuine multi-pole effect = {genuine_effect:.1e}. "
              f"Pole splitting = {100*split:.3f}% (Josephson/m_base^2 = {evals_Jos[2]/m_base_sq:.4f}). "
              f"Identity alpha_s = n_s^2-1 survives at physical Josephson strength.")
else:
    verdict = "INFO"
    detail = (f"alpha_s = {alpha_s_3p:.6f}, identity deviation {identity_deviation_3p:.4f}, "
              f"outside PASS range.")

sigma_planck = 0.008
tension_3p = abs(alpha_s_3p) / sigma_planck

print(f"\n  VERDICT: {verdict}")
print(f"  {detail}")
print(f"")
print(f"  KEY NUMBERS:")
print(f"    n_s (3-pole)     = {n_s_3p:.8f}")
print(f"    alpha_s (3-pole) = {alpha_s_3p:.8f}")
print(f"    n_s (O-Z)        = {n_s_oz:.8f}")
print(f"    alpha_s (O-Z)    = {alpha_s_oz:.8f}")
print(f"    |Delta alpha_s|  = {abs(alpha_s_3p - alpha_s_oz):.2e} (3-pole vs O-Z)")
print(f"    Genuine effect   = {genuine_effect:.2e}")
print(f"")
print(f"  IDENTITY TEST:")
print(f"    n_s^2 - 1 (3p) = {n_s_3p**2-1:.8f}")
print(f"    n_s^2 - 1 (OZ) = {n_s_oz**2-1:.8f}")
print(f"    3-pole dev from identity: {alpha_s_3p-(n_s_3p**2-1):.8f} (includes discretization)")
print(f"    O-Z dev from identity:    {alpha_s_oz-(n_s_oz**2-1):.8f} (pure discretization)")
print(f"    Multi-pole contribution:  {multi_pole_effect:.8f}")
print(f"")
print(f"  POLE STRUCTURE:")
for i in range(3):
    print(f"    Pole {i+1}: mu = {mu_poles[i]:.6f}, w = {w_poles[i]:.6f}")
print(f"    Splitting: (mu_3^2 - mu_1^2)/mu_1^2 = {split:.6f} ({100*split:.3f}%)")
print(f"    All residues = 1 (equal-stiffness theorem)")
print(f"")
print(f"  WHY THE IDENTITY SURVIVES:")
print(f"    Josephson max eigenvalue: {evals_Jos[2]:.6f} M_KK^2")
print(f"    On-site mass:             {m_base_sq:.1f} M_KK^2")
print(f"    Ratio:                    {evals_Jos[2]/m_base_sq:.2e}")
print(f"    The poles are {100*(1-split):.2f}% degenerate.")
print(f"    To break identity at 1% level: need J factor > ~{m_base_sq/evals_Jos[2]/10:.0f}x")
print(f"")
print(f"  PLANCK TENSION:")
print(f"    alpha_s = {alpha_s_3p:.6f}")
print(f"    Planck: 0 +/- {sigma_planck}")
print(f"    Tension: {tension_3p:.1f} sigma (unchanged from S49 O-Z)")

# =============================================================================
# STEP 13: Save
# =============================================================================
print("\n--- Step 13: Save ---")

out_file = os.path.join(SCRIPT_DIR, 's50_leggett_propagator.npz')
np.savez(out_file,
    # Gate
    gate_name='LEGGETT-PROPAGATOR-50',
    gate_verdict=verdict,
    gate_detail=detail,

    # Key results
    n_s_3pole=n_s_3p,
    alpha_s_3pole=alpha_s_3p,
    n_s_OZ=n_s_oz,
    alpha_s_OZ=alpha_s_oz,
    alpha_s_analytic=alpha_s_analytic,
    identity_deviation_3p=identity_deviation_3p,
    identity_deviation_oz=identity_deviation_oz,
    multi_pole_effect=multi_pole_effect,

    # Masses
    m_base=m_base,
    m_base_sq=m_base_sq,
    m_star_OZ=m_star_OZ,

    # Poles
    pole_masses_sq=lam_total,
    pole_masses=mu_poles,
    pole_weights=w_poles,
    pole_splitting=split,
    M_Jos=M_Jos,
    evals_Jos=evals_Jos,

    # Per-pole
    ns_per_pole=ns_per_pole,
    alpha_per_pole=alpha_per_pole,

    # Couplings
    J_12=J_12, J_23=J_23, J_13=J_13,
    J_C2=J_C2, J_su2=J_su2, J_eff=J_eff,

    # Dense
    K_dense=K_dense,
    P_3pole_dense=P_3p_dense,
    P_OZ_dense=P_oz_dense,
    P_poles_dense=P_poles_dense,
    ns_3pole_dense=ns_3p_dense,
    ns_OZ_dense=ns_oz_dense,

    # Scan
    J_factors=np.array([r['factor'] for r in scan_results]),
    scan_alpha_s=np.array([r['alpha_s'] for r in scan_results]),
    scan_ns=np.array([r['n_s'] for r in scan_results]),
    scan_deviation=np.array([r['deviation'] for r in scan_results]),
    scan_spread=np.array([r['spread'] for r in scan_results]),

    # Metadata
    tau_fold=tau_fold,
    K_pivot=K_pivot,
    T_acoustic=T_acoustic,
    tension_sigma=tension_3p,
)
print(f"  Saved: {out_file}")

# =============================================================================
# STEP 14: Plot
# =============================================================================
print("\n--- Step 14: Plotting ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3)

# --- Panel 1: P(K) ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.loglog(K_dense, P_3p_dense, 'b-', lw=2.5, label='3-pole total', zorder=5)
ax1.loglog(K_dense, P_oz_dense, 'r--', lw=2, label='O-Z single-pole')
for i in range(3):
    ax1.loglog(K_dense, P_poles_dense[i], ':', lw=1.2, alpha=0.6,
               label=f'Pole {i+1} ($\\mu$={mu_poles[i]:.2f})')
ax1.axvline(K_pivot, color='gray', ls=':', alpha=0.4)
ax1.set_xlabel('K')
ax1.set_ylabel('P(K)')
ax1.set_title('3-Pole vs O-Z Propagator')
ax1.legend(fontsize=7, loc='upper right')
ax1.grid(True, alpha=0.3)

# --- Panel 2: n_s(K) ---
ax2 = fig.add_subplot(gs[0, 1])
mask = (ns_3p_dense != 0)
ax2.semilogx(K_dense[mask], ns_3p_dense[mask], 'b-', lw=2, label='3-pole $n_s(K)$')
ax2.semilogx(K_dense[mask], ns_oz_dense[mask], 'r--', lw=2, label='O-Z $n_s(K)$', alpha=0.7)
ax2.axhline(0.965, color='green', ls='--', lw=1, label='Planck $n_s$')
ax2.axhspan(0.950, 0.980, color='green', alpha=0.08)
ax2.axvline(K_pivot, color='gray', ls=':', alpha=0.4)
ax2.set_xlabel('K')
ax2.set_ylabel('$n_s(K)$')
ax2.set_title('Spectral Index: 3-Pole vs O-Z (Indistinguishable)')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0.90, 1.01)

# --- Panel 3: Identity deviation vs J factor ---
ax3 = fig.add_subplot(gs[1, 0])
factors = [r['factor'] for r in scan_results if r['factor'] > 0]
devs = [r['deviation'] for r in scan_results if r['factor'] > 0]
alphas_scan = [r['alpha_s'] for r in scan_results if r['factor'] > 0]
identities = [r['identity'] for r in scan_results if r['factor'] > 0]

ax3_twin = ax3.twinx()
ax3.semilogx(factors, devs, 'ko-', ms=5, label=r'$\alpha_s - (n_s^2-1)$ [left]')
ax3_twin.semilogx(factors, alphas_scan, 'bs-', ms=4, alpha=0.5,
                   label=r'$\alpha_s$ [right]')
ax3.axhline(0, color='red', ls='--', alpha=0.4)
ax3.axvline(1, color='gray', ls=':', alpha=0.4, label='Physical $J_{12}$')
ax3_twin.axhspan(-0.008, 0.008, color='green', alpha=0.1)
ax3.set_xlabel('Josephson scaling factor')
ax3.set_ylabel(r'$\alpha_s - (n_s^2-1)$', color='black')
ax3_twin.set_ylabel(r'$\alpha_s$', color='blue')
ax3.set_title(r'Identity Breaking vs Josephson Strength')
lines1 = ax3.get_legend_handles_labels()
lines2 = ax3_twin.get_legend_handles_labels()
ax3.legend(lines1[0] + lines2[0], lines1[1] + lines2[1], fontsize=7, loc='upper left')
ax3.grid(True, alpha=0.3)

# --- Panel 4: Pole structure diagram ---
ax4 = fig.add_subplot(gs[1, 1])
# Show the mass hierarchy: m_base >> Josephson splitting
bars_mass = [m_base_sq, evals_Jos[1], evals_Jos[2]]
labels_mass = ['$m_{\\mathrm{base}}^2$\n(from $n_s$)', '$\\sigma_1$\n(Leggett 1)',
               '$\\sigma_2$\n(Leggett 2)']
colors_mass = ['#2196F3', '#FF9800', '#F44336']
x_pos = np.arange(3)
ax4.bar(x_pos, bars_mass, color=colors_mass, alpha=0.8)
ax4.set_xticks(x_pos)
ax4.set_xticklabels(labels_mass, fontsize=9)
ax4.set_ylabel('Value ($M_{KK}^2$ units)')
ax4.set_title('Mass Hierarchy: Why Identity Survives')
ax4.set_yscale('log')
# Annotate ratio
ax4.annotate(f'$\\sigma_2/m_{{base}}^2$ = {evals_Jos[2]/m_base_sq:.2e}',
            xy=(1.5, evals_Jos[2]), fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
ax4.grid(True, alpha=0.3, axis='y')

fig.text(0.5, 0.01,
         f"GATE: {verdict} | 3-pole $\\alpha_s$ = {alpha_s_3p:.5f} = O-Z $\\alpha_s$ | "
         f"Pole splitting = {100*split:.3f}% | Tension = {tension_3p:.1f}$\\sigma$",
         ha='center', fontsize=10,
         bbox=dict(boxstyle='round', facecolor='#FFCDD2' if verdict=='FAIL' else 'wheat', alpha=0.8))

plot_file = os.path.join(SCRIPT_DIR, 's50_leggett_propagator.png')
plt.savefig(plot_file, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_file}")

elapsed = time.time() - t0
print(f"\n  Total elapsed: {elapsed:.1f} s")
print("=" * 78)
