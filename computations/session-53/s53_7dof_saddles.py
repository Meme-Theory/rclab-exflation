#!/usr/bin/env python3
"""
S53 — 7-DOF-SADDLES-53: Saddle Points of Unified Action at N_pair=1
====================================================================

With N_pair = 1 (W2-6), the 7-DOF unified action S[tau, Delta, theta_12,
theta_23, theta_13, phi, chi] simplifies drastically:

  - Only 1 Cooper pair: no relative phases between sectors (angular DOFs frozen)
  - Delta is determined by ED, not variational GL
  - Effective action reduces to S_eff[tau] = V_KK(tau) + E_cond(tau)

where:
  V_KK(tau) = -(M_p^2/2) R_K(tau)  [geometric/gravitational sector]
  E_cond(tau) = ED ground state energy at N_pair=1

The BCS Hamiltonian uses single-particle energies RELATIVE to the Fermi
level eps_F = mean(E_B2). This is the convention in which E_cond < 0
represents bound-state energy gain from pairing.

Gate: 7-DOF-SADDLES-53 — INFO (saddle enumeration)
Output: s53_7dof_saddles.npz, s53_7dof_saddles.png, text

Author: Feynman-Theorist (Session 53)
Date: 2026-03-21
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, exp, log
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import *

print("=" * 72)
print("  S53 — 7-DOF-SADDLES-53: Saddle Points at N_pair=1")
print("=" * 72)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(os.path.dirname(DATA_DIR), 'computations/_shared')

# ============================================================================
#  SECTION 1: Geometric potential V_KK(tau)
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 1: Geometric potential V_KK(tau)")
print("=" * 72)

alpha_K = g0_diag  # = 3.0

def R_K(s):
    """Scalar curvature of Jensen-deformed SU(3)."""
    return (12.0 / alpha_K) * (2.0 * exp(2.0*s) - 1.0 + 8.0 * exp(-s) - exp(-4.0*s)) / 8.0

def dR_K_ds(s):
    """dR_K/ds analytically."""
    return (12.0 / alpha_K) * (4.0 * exp(2.0*s) - 8.0 * exp(-s) + 4.0 * exp(-4.0*s)) / 8.0

def d2R_K_ds2(s):
    """d^2 R_K/ds^2 analytically."""
    return (12.0 / alpha_K) * (8.0 * exp(2.0*s) + 8.0 * exp(-s) - 16.0 * exp(-4.0*s)) / 8.0

M_KK_val = M_KK_kerner
M_P_over_MKK = M_Pl_reduced / M_KK_val
M_p2_val = M_P_over_MKK**2

def V_KK_func(s):
    """KK potential: V_KK = -(M_p^2/2) * R_K(s)."""
    return -0.5 * M_p2_val * R_K(s)

def dV_KK_ds(s):
    return -0.5 * M_p2_val * dR_K_ds(s)

def d2V_KK_ds2(s):
    return -0.5 * M_p2_val * d2R_K_ds2(s)

print(f"\n  V_KK(0) = {V_KK_func(0):.6f} M_KK^4")
print(f"  V_KK(fold={tau_fold}) = {V_KK_func(tau_fold):.6f} M_KK^4")
print(f"  dV_KK/ds(0) = {dV_KK_ds(0):.6e}")
print(f"  dV_KK/ds(fold) = {dV_KK_ds(tau_fold):.6f}")
print(f"  d2V_KK/ds2(fold) = {d2V_KK_ds2(tau_fold):.6f}")

# ============================================================================
#  SECTION 2: BCS pairing Hamiltonian at the fold
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 2: BCS pairing Hamiltonian (fold calibration)")
print("=" * 72)

# Load the s36 ED data
ed_data = np.load(os.path.join(ARCHIVE_DIR, 's36_multisector_ed.npz'), allow_pickle=True)
V_fold = ed_data['V_8x8_full']    # 8x8 pairing matrix at fold
E_sp_fold = ed_data['E_8_full']   # 8 single-particle energies at fold
labels = ed_data['branch_labels']  # mode labels

# Convention: single-particle energies relative to Fermi level
eps_F_fold = np.mean(E_sp_fold[:4])  # Fermi level = B2 mean
E_rel_fold = E_sp_fold - eps_F_fold

print(f"\n  8-mode spectrum at fold (tau = {tau_fold}):")
print(f"    eps_F = {eps_F_fold:.6f} M_KK (Fermi level = B2 mean)")
for i in range(8):
    print(f"    {labels[i]}: eps = {E_sp_fold[i]:.6f}, eps_rel = {E_rel_fold[i]:+.6f}")

# Verify: N=1 Hamiltonian at fold
H1_fold = V_fold.copy()
for k in range(8):
    H1_fold[k, k] += 2.0 * E_rel_fold[k]

evals_fold = np.linalg.eigvalsh(H1_fold)
E_cond_H1 = evals_fold[0]
E_cond_ED = float(ed_data['E_cond_full'])

print(f"\n  N=1 sector Hamiltonian at fold:")
print(f"    H1[k,l] = 2*eps_k_rel * delta_kl + V_kl")
print(f"    min eigenvalue = {E_cond_H1:.6f} M_KK^4")
print(f"    Full ED E_cond = {E_cond_ED:.6f} M_KK^4")
print(f"    Discrepancy: {abs(E_cond_H1 - E_cond_ED):.6e} (N>1 sector mixing)")

# V matrix statistics
print(f"\n  V matrix structure:")
print(f"    V_kk (diagonal): {np.diag(V_fold)}")
print(f"    B1-B2 coupling: V_B1_B2 = {V_fold[4,0]:.6f} (all equal by C2 symmetry)")
print(f"    max |V_kl|: {np.max(np.abs(V_fold)):.6f}")
print(f"    V eigenvalues: {np.linalg.eigvalsh(V_fold)}")

# ============================================================================
#  SECTION 3: Single-particle energy model E_k(tau)
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 3: Single-particle energy model")
print("=" * 72)

# The Dirac eigenvalues on Jensen-deformed SU(3) depend on tau through:
#   D_K^2 ~ sum_a g^{aa}(s) T_a^2 + R(s)/4
# For Jensen: g^{aa} = e^{-2s} (coset, a=1..4) or e^{s} (stab, a=5..8)
#
# For B1 singlet (0,0): all T_a = 0, so D_K^2 = R_K(s)/4
#   eps_B1(s) = C_norm * sqrt(R_K(s)/4)
#
# For B2 adjoint (1,1): C_2 = 3
#   eps_B2^2(s) = C_norm^2 * [c_B2 * e^{-2s} + (3-c_B2) * e^s + R_K(s)/4]
#
# For B3 fundamental (1,0): C_2 = 4/3
#   eps_B3^2(s) = C_norm^2 * [c_B3 * e^{-2s} + (4/3-c_B3) * e^s + R_K(s)/4]

# Calibration: match fold-point values
C_norm = E_sp_fold[4] / sqrt(R_K(tau_fold) / 4.0)  # from B1

f = tau_fold
e_2f = exp(-2.0 * f)
ef = exp(f)

# B2: C_2 = 3
C2_B2 = 3.0  # (local)
eps_B2_scaled = (E_sp_fold[0] / C_norm)**2
c_B2 = (eps_B2_scaled - R_K(f)/4.0 - C2_B2 * ef) / (e_2f - ef)
s_B2 = C2_B2 - c_B2

# B3: C_2 = 4/3
C2_B3 = 4.0/3.0
eps_B3_scaled = (E_sp_fold[5] / C_norm)**2
c_B3 = (eps_B3_scaled - R_K(f)/4.0 - C2_B3 * ef) / (e_2f - ef)
s_B3 = C2_B3 - c_B3

print(f"\n  Calibration constants:")
print(f"    C_norm = {C_norm:.6f} (overall normalization)")
print(f"    B2: c_coset = {c_B2:.6f}, c_stab = {s_B2:.6f}, sum = {c_B2+s_B2:.6f} (target: 3)")
print(f"    B3: c_coset = {c_B3:.6f}, c_stab = {s_B3:.6f}, sum = {c_B3+s_B3:.6f} (target: 1.333)")

def eps_B1(s):
    return C_norm * sqrt(R_K(s) / 4.0)

def eps_B2(s):
    val = c_B2 * exp(-2.0*s) + s_B2 * exp(s) + R_K(s)/4.0
    return C_norm * sqrt(max(val, 0.01))

def eps_B3(s):
    val = c_B3 * exp(-2.0*s) + s_B3 * exp(s) + R_K(s)/4.0
    return C_norm * sqrt(max(val, 0.01))

# Verify at fold
print(f"\n  Verification at fold:")
print(f"    eps_B1({tau_fold}) = {eps_B1(tau_fold):.6f} (target: {E_sp_fold[4]:.6f})")
print(f"    eps_B2({tau_fold}) = {eps_B2(tau_fold):.6f} (target: {E_sp_fold[0]:.6f})")
print(f"    eps_B3({tau_fold}) = {eps_B3(tau_fold):.6f} (target: {E_sp_fold[5]:.6f})")

# Check at s=0
print(f"\n  At round point (s=0):")
print(f"    eps_B1(0) = {eps_B1(0):.6f}")
print(f"    eps_B2(0) = {eps_B2(0):.6f}")
print(f"    eps_B3(0) = {eps_B3(0):.6f}")
print(f"    B1-B2 gap: {eps_B2(0) - eps_B1(0):.6f}")
print(f"    B2-B3 gap: {eps_B3(0) - eps_B2(0):.6f}")

# ============================================================================
#  SECTION 4: ED sweep of E_cond(tau)
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 4: E_cond(tau) from N=1 ED sweep")
print("=" * 72)

N_tau = 500  # (local)
tau_grid = np.linspace(0.001, 0.50, N_tau)

E_cond_arr = np.zeros(N_tau)
eps_B1_arr = np.zeros(N_tau)
eps_B2_arr = np.zeros(N_tau)
eps_B3_arr = np.zeros(N_tau)
eps_F_arr = np.zeros(N_tau)
gap_B1B2_arr = np.zeros(N_tau)

for i, s in enumerate(tau_grid):
    # Single-particle energies at this tau
    eB1 = eps_B1(s)
    eB2 = eps_B2(s)
    eB3 = eps_B3(s)

    eps_B1_arr[i] = eB1
    eps_B2_arr[i] = eB2
    eps_B3_arr[i] = eB3

    # 8-mode spectrum: [B2, B2, B2, B2, B1, B3, B3, B3]
    E_sp = np.array([eB2, eB2, eB2, eB2, eB1, eB3, eB3, eB3])

    # Fermi level = B2 mean
    eps_F_s = np.mean(E_sp[:4])  # = eB2
    eps_F_arr[i] = eps_F_s
    E_rel = E_sp - eps_F_s

    gap_B1B2_arr[i] = eB2 - eB1

    # N=1 Hamiltonian: H1[k,l] = 2*eps_k_rel * delta_kl + V_kl
    # Using fold-point V matrix (structure is tau-independent by Peter-Weyl)
    H1 = V_fold.copy()
    for k in range(8):
        H1[k, k] += 2.0 * E_rel[k]

    evals = np.linalg.eigvalsh(H1)
    E_cond_arr[i] = evals[0]

# Build smooth spline
E_cond_spline = CubicSpline(tau_grid, E_cond_arr)
dE_cond_dtau = E_cond_spline(tau_grid, 1)
d2E_cond_dtau2 = E_cond_spline(tau_grid, 2)

# Verify at fold
idx_fold = np.argmin(np.abs(tau_grid - tau_fold))
print(f"\n  E_cond(fold) = {E_cond_arr[idx_fold]:.6f} M_KK^4")
print(f"  E_cond from H1 at fold = {E_cond_H1:.6f} M_KK^4")
print(f"  E_cond from full ED = {E_cond_ED:.6f} M_KK^4")
print(f"  Match: {abs(E_cond_arr[idx_fold] - E_cond_H1):.2e}")

print(f"\n  E_cond range: [{E_cond_arr.min():.6f}, {E_cond_arr.max():.6f}]")
print(f"  E_cond(0.001) = {E_cond_arr[0]:.6f}")
print(f"  E_cond(0.50) = {E_cond_arr[-1]:.6f}")
print(f"  Variation: {(E_cond_arr.max()-E_cond_arr.min())/abs(E_cond_arr[idx_fold])*100:.2f}%")

print(f"\n  dE_cond/dtau at fold: {dE_cond_dtau[idx_fold]:.6f}")
print(f"  d2E_cond/dtau2 at fold: {d2E_cond_dtau2[idx_fold]:.6f}")

# B1-B2 gap
print(f"\n  B1-B2 gap:")
print(f"    At s=0.001: {gap_B1B2_arr[0]:.6f}")
print(f"    At fold: {gap_B1B2_arr[idx_fold]:.6f}")
print(f"    At s=0.50: {gap_B1B2_arr[-1]:.6f}")
print(f"    Min gap: {gap_B1B2_arr.min():.6f} at tau = {tau_grid[np.argmin(gap_B1B2_arr)]:.4f}")

# ============================================================================
#  SECTION 5: Effective potential and saddle search
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 5: S_eff(tau) = V_KK(tau) + E_cond(tau)")
print("=" * 72)

V_KK_arr = np.array([V_KK_func(s) for s in tau_grid])
dV_KK_arr = np.array([dV_KK_ds(s) for s in tau_grid])

# Effective potential
V_eff_arr = V_KK_arr + E_cond_arr
dV_eff_arr = dV_KK_arr + dE_cond_dtau

print(f"\n  V_KK(fold) = {V_KK_arr[idx_fold]:.6f} M_KK^4")
print(f"  E_cond(fold) = {E_cond_arr[idx_fold]:.6f} M_KK^4")
print(f"  V_eff(fold) = {V_eff_arr[idx_fold]:.6f} M_KK^4")
print(f"  |E_cond/V_KK| = {abs(E_cond_arr[idx_fold]/V_KK_arr[idx_fold]):.6e}")

print(f"\n  GRADIENT COMPARISON at fold:")
print(f"    dV_KK/dtau = {dV_KK_arr[idx_fold]:.6f} M_KK^4")
print(f"    dE_cond/dtau = {dE_cond_dtau[idx_fold]:.6f} M_KK^4")
print(f"    dV_eff/dtau = {dV_eff_arr[idx_fold]:.6f} M_KK^4")
print(f"    |dE_cond/dV_KK| = {abs(dE_cond_dtau[idx_fold]/dV_KK_arr[idx_fold]):.6e}")

# Search for sign changes in dV_eff/dtau
print(f"\n  SADDLE POINT SEARCH:")
sign_changes = []
for i in range(len(dV_eff_arr) - 1):
    if dV_eff_arr[i] * dV_eff_arr[i+1] < 0:
        tau_zero = tau_grid[i] - dV_eff_arr[i] * (tau_grid[i+1] - tau_grid[i]) / (dV_eff_arr[i+1] - dV_eff_arr[i])
        sign_changes.append(tau_zero)

print(f"  Sign changes in dV_eff/dtau: {len(sign_changes)} found")
for sc in sign_changes:
    print(f"    tau = {sc:.6f}")

# Newton's method from 20 starting points
print(f"\n  Newton search from 20 initial conditions:")
tau_inits = np.linspace(0.01, 0.49, 20)
V_eff_spline = CubicSpline(tau_grid, V_eff_arr)

saddle_results = []
for tau0 in tau_inits:
    tau_curr = tau0
    for step in range(5000):
        dV = float(V_eff_spline(tau_curr, 1))
        d2V = float(V_eff_spline(tau_curr, 2))
        if abs(dV) < 1e-12:
            break
        if abs(d2V) > 1e-15:
            delta = -dV / d2V
            delta = max(-0.01, min(0.01, delta))
            tau_curr = tau_curr + delta
        else:
            tau_curr = tau_curr - 0.001 * dV
        tau_curr = max(0.002, min(0.498, tau_curr))

    V_at = float(V_eff_spline(tau_curr))
    dV_at = float(V_eff_spline(tau_curr, 1))
    d2V_at = float(V_eff_spline(tau_curr, 2))

    is_interior = 0.005 < tau_curr < 0.495
    is_converged = abs(dV_at) < 1e-6

    if is_interior and is_converged:
        stype = 'minimum' if d2V_at > 0 else ('maximum' if d2V_at < 0 else 'inflection')
    elif not is_interior:
        stype = 'boundary'
    else:
        stype = 'unconverged'

    saddle_results.append({
        'tau_init': tau0, 'tau_final': tau_curr, 'V_eff': V_at,
        'dV_eff': dV_at, 'd2V_eff': d2V_at, 'type': stype, 'converged': is_converged
    })
    print(f"    tau_0={tau0:.3f} -> tau_f={tau_curr:.6f}, "
          f"dV={dV_at:.2e}, d2V={d2V_at:.2e}, type={stype}")

# Collect unique critical points
unique_saddles = {}
for sr in saddle_results:
    if sr['type'] in ('minimum', 'maximum', 'inflection'):
        key = round(sr['tau_final'], 4)
        if key not in unique_saddles:
            unique_saddles[key] = sr

n_saddles = len(unique_saddles)
n_minima = sum(1 for sr in unique_saddles.values() if sr['type'] == 'minimum')
n_maxima = sum(1 for sr in unique_saddles.values() if sr['type'] == 'maximum')

print(f"\n  UNIQUE INTERIOR CRITICAL POINTS: {n_saddles}")
print(f"    Minima: {n_minima}")
print(f"    Maxima: {n_maxima}")
for tau_s, sr in sorted(unique_saddles.items()):
    print(f"    tau = {tau_s:.6f}, V_eff = {sr['V_eff']:.6f}, "
          f"d2V = {sr['d2V_eff']:.4e}, type = {sr['type']}")

# ============================================================================
#  SECTION 6: Hessian and classification
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 6: Hessian at critical points")
print("=" * 72)

for tau_s, sr in sorted(unique_saddles.items()):
    print(f"\n  tau = {tau_s:.6f}:")
    print(f"    V_eff = {sr['V_eff']:.6f} M_KK^4")
    print(f"    dV_eff/dtau = {sr['dV_eff']:.4e}")
    print(f"    d2V_eff/dtau2 = {sr['d2V_eff']:.4e}")

    if sr['type'] == 'minimum':
        omega = sqrt(abs(sr['d2V_eff']))
        print(f"    ==> LOCAL MINIMUM: omega = {omega:.4f} M_KK")
        print(f"    ==> STABILIZATION POINT FOR EXFLATION")

        # At this minimum, what are the contributions?
        V_KK_at = V_KK_func(tau_s)
        E_cond_at = float(E_cond_spline(tau_s))
        dVKK_at = dV_KK_ds(tau_s)
        dEcond_at = float(E_cond_spline(tau_s, 1))
        print(f"    V_KK(tau) = {V_KK_at:.6f}, dV_KK/dtau = {dVKK_at:.6f}")
        print(f"    E_cond(tau) = {E_cond_at:.6f}, dE_cond/dtau = {dEcond_at:.6f}")
        print(f"    Gradient cancellation: dV_KK + dE_cond = {dVKK_at + dEcond_at:.4e}")

    elif sr['type'] == 'maximum':
        print(f"    ==> LOCAL MAXIMUM (unstable saddle)")
        # Check what's happening
        V_KK_at = V_KK_func(tau_s)
        E_cond_at = float(E_cond_spline(tau_s))
        dVKK_at = dV_KK_ds(tau_s)
        dEcond_at = float(E_cond_spline(tau_s, 1))
        print(f"    V_KK(tau) = {V_KK_at:.6f}, dV_KK/dtau = {dVKK_at:.6f}")
        print(f"    E_cond(tau) = {E_cond_at:.6f}, dE_cond/dtau = {dEcond_at:.6f}")

# If no saddle points found
if n_saddles == 0:
    print("\n  NO INTERIOR CRITICAL POINTS.")
    print("  V_eff is monotonic (dV_eff/dtau has constant sign).")
    print(f"  min dV_eff/dtau = {dV_eff_arr.min():.6f}")
    print(f"  max dV_eff/dtau = {dV_eff_arr.max():.6f}")

# ============================================================================
#  SECTION 7: Physics analysis
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 7: Physics of E_cond(tau)")
print("=" * 72)

# The key physics: E_cond depends on tau through the B1-B2 gap.
# As the gap closes (Van Hove), the pairing matrix element V_B1_B2
# has a larger effect relative to the energy denominator.
# E_cond ~ -V_B1_B2^2 / delta_eps (perturbative estimate)

delta_E_fold = gap_B1B2_arr[idx_fold]
V_B1_B2 = V_fold[4, 0]
E_cond_pert = -V_B1_B2**2 / (2.0 * delta_E_fold)

print(f"\n  Perturbative estimate at fold:")
print(f"    V_B1_B2 = {V_B1_B2:.6f}")
print(f"    delta_eps = {delta_E_fold:.6f}")
print(f"    E_cond_pert ~ -V^2/(2*delta) = {E_cond_pert:.6f}")
print(f"    E_cond_ED = {E_cond_arr[idx_fold]:.6f}")
print(f"    Perturbation theory is {abs(E_cond_pert/E_cond_arr[idx_fold])*100:.1f}% of exact")
print(f"    (Multi-mode mixing dominates: B1 hybridizes with ALL 4 B2 modes)")

# dE_cond/dtau physics: as gap changes with tau, E_cond changes
# dE_cond/dtau ~ V^2 / delta_eps^2 * d(delta_eps)/dtau
dgap_dtau = np.gradient(gap_B1B2_arr, tau_grid)
print(f"\n  B1-B2 gap dynamics:")
print(f"    d(gap)/dtau at fold: {dgap_dtau[idx_fold]:.6f}")
print(f"    Gap is {'CLOSING' if dgap_dtau[idx_fold] < 0 else 'OPENING'} at fold")
print(f"    Min gap: {gap_B1B2_arr.min():.6f} at tau = {tau_grid[np.argmin(gap_B1B2_arr)]:.4f}")

# Scale hierarchy
print(f"\n  SCALE HIERARCHY:")
print(f"    |V_KK(fold)| = {abs(V_KK_arr[idx_fold]):.4f} M_KK^4")
print(f"    |E_cond(fold)| = {abs(E_cond_arr[idx_fold]):.4f} M_KK^4")
print(f"    Ratio: |E_cond/V_KK| = {abs(E_cond_arr[idx_fold]/V_KK_arr[idx_fold]):.6e}")
print(f"")
print(f"    |dV_KK/dtau(fold)| = {abs(dV_KK_arr[idx_fold]):.4f} M_KK^4")
print(f"    |dE_cond/dtau(fold)| = {abs(dE_cond_dtau[idx_fold]):.4f} M_KK^4")
grad_ratio = abs(dE_cond_dtau[idx_fold] / dV_KK_arr[idx_fold])
print(f"    Gradient ratio: |dE_cond/dV_KK| = {grad_ratio:.4f}")

if grad_ratio > 1.0:
    print(f"    ==> E_cond gradient EXCEEDS V_KK gradient!")
    print(f"    ==> Saddle points EXPECTED in V_eff(tau)")
else:
    amplification = 1.0 / grad_ratio
    print(f"    ==> E_cond gradient is {amplification:.1f}x TOO SMALL")
    print(f"    ==> Saddle points require {amplification:.0f}x amplification")

# ============================================================================
#  SECTION 8: What creates the critical points (or not)?
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 8: Mechanism analysis")
print("=" * 72)

# Find where E_cond has extrema
idx_Econd_min = np.argmin(E_cond_arr)
idx_Econd_max = np.argmax(E_cond_arr)

print(f"\n  E_cond extrema:")
print(f"    Most negative: E_cond = {E_cond_arr[idx_Econd_min]:.6f} at tau = {tau_grid[idx_Econd_min]:.4f}")
print(f"    Least negative: E_cond = {E_cond_arr[idx_Econd_max]:.6f} at tau = {tau_grid[idx_Econd_max]:.4f}")
print(f"    Variation: {(E_cond_arr.max()-E_cond_arr.min()):.6f} M_KK^4")

# Check: does the E_cond gradient ever match the V_KK gradient in magnitude?
gradient_match = np.abs(dE_cond_dtau) / np.abs(dV_KK_arr + 1e-30)
idx_best_match = np.argmax(gradient_match)
print(f"\n  Best gradient match:")
print(f"    tau = {tau_grid[idx_best_match]:.4f}")
print(f"    |dE_cond/dtau| = {abs(dE_cond_dtau[idx_best_match]):.4f}")
print(f"    |dV_KK/dtau| = {abs(dV_KK_arr[idx_best_match]):.4f}")
print(f"    Ratio: {gradient_match[idx_best_match]:.4f}")

# N_cells amplification analysis
print(f"\n  N_cells amplification (fabric):")
print(f"    N_cells = {N_cells}")
print(f"    N_cells * E_cond(fold) = {N_cells * E_cond_arr[idx_fold]:.4f} M_KK^4")
print(f"    N_cells * |E_cond/V_KK| = {N_cells * abs(E_cond_arr[idx_fold]/V_KK_arr[idx_fold]):.4e}")

# Check if N_cells amplification creates a saddle
E_cond_fabric = N_cells * E_cond_arr
dE_cond_fabric = N_cells * dE_cond_dtau
V_eff_fabric = V_KK_arr + E_cond_fabric
dV_eff_fabric = dV_KK_arr + dE_cond_fabric

# Sign changes in fabric case
fabric_sign_changes = []
for i in range(len(dV_eff_fabric) - 1):
    if dV_eff_fabric[i] * dV_eff_fabric[i+1] < 0:
        tau_zero = tau_grid[i] - dV_eff_fabric[i] * (tau_grid[i+1] - tau_grid[i]) / (dV_eff_fabric[i+1] - dV_eff_fabric[i])
        fabric_sign_changes.append(tau_zero)
print(f"    Sign changes in dV_eff_fabric: {len(fabric_sign_changes)}")
for sc in fabric_sign_changes:
    print(f"      tau = {sc:.6f}")

# ============================================================================
#  SECTION 9: 7-DOF reduction summary
# ============================================================================
print("\n" + "=" * 72)
print("  SECTION 9: 7-DOF -> 1-DOF reduction at N_pair=1")
print("=" * 72)

# Load the S52 unified action eigenvalues
s52_data = np.load(os.path.join(DATA_DIR, 's52_unified_action.npz'), allow_pickle=True)
omega2_full = s52_data['omega2_full']

print(f"""
  S52 unified action: 7 DOFs = [tau, Delta_B1, Delta_B2, Delta_B3, theta_12, theta_23, theta_13]

  S52 normal mode frequencies (omega^2):
    {np.sort(omega2_full)}

  At N_pair = 1 (W2-6):
    - Delta is NOT variational: determined by ED (N=1 sector)
    - Only 1 pair: no relative phases (theta = 0 by definition)
    - 6 BCS DOFs (3 amplitudes + 3 phases) are FROZEN
    - Effective action: S_eff[tau] = V_KK(tau) + E_cond(tau)

  E_cond(tau) computed by diagonalizing the N=1 BCS Hamiltonian
  at {N_tau} tau points with the Jensen metric model for eps_k(tau).

  Result: {n_saddles} interior critical points. {n_minima} local minima.
""")

# ============================================================================
#  SECTION 10: Gate verdict
# ============================================================================
print("=" * 72)
print("  GATE VERDICT")
print("=" * 72)

verdict = "INFO"
if n_minima > 0:
    detail = (f"7-DOF reduces to 1-DOF at N_pair=1. "
              f"{n_saddles} critical points, {n_minima} minima. "
              f"Stabilization point EXISTS.")
elif n_saddles > 0:
    detail = (f"7-DOF reduces to 1-DOF at N_pair=1. "
              f"{n_saddles} critical points (all maxima/inflections, NO minima). "
              f"|dE_cond/dV_KK| = {grad_ratio:.4f} at fold.")
else:
    detail = (f"7-DOF reduces to 1-DOF at N_pair=1. "
              f"NO critical points. V_eff monotonic. "
              f"|dE_cond/dV_KK| = {grad_ratio:.4f}.")

print(f"\n  Gate: 7-DOF-SADDLES-53 = {verdict}")
print(f"  Detail: {detail}")

# ============================================================================
#  SECTION 11: Save data and plot
# ============================================================================
print("\n" + "=" * 72)
print("  Saving data and plot")
print("=" * 72)

np.savez(os.path.join(DATA_DIR, 's53_7dof_saddles.npz'),
         tau_grid=tau_grid, N_tau=N_tau,
         V_KK=V_KK_arr, E_cond=E_cond_arr, V_eff=V_eff_arr,
         dV_KK=dV_KK_arr, dE_cond=dE_cond_dtau, dV_eff=dV_eff_arr,
         d2E_cond=d2E_cond_dtau2,
         eps_B1=eps_B1_arr, eps_B2=eps_B2_arr, eps_B3=eps_B3_arr,
         eps_F=eps_F_arr, gap_B1B2=gap_B1B2_arr,
         n_saddles=n_saddles, n_minima=n_minima, n_maxima=n_maxima,
         saddle_taus=np.array([sr['tau_final'] for sr in unique_saddles.values()]) if unique_saddles else np.array([]),
         saddle_types=np.array([sr['type'] for sr in unique_saddles.values()]) if unique_saddles else np.array([]),
         saddle_d2V=np.array([sr['d2V_eff'] for sr in unique_saddles.values()]) if unique_saddles else np.array([]),
         grad_ratio_at_fold=grad_ratio,
         E_cond_over_VKK=abs(E_cond_arr[idx_fold]/V_KK_arr[idx_fold]),
         C_norm=C_norm, c_B2=c_B2, s_B2=s_B2, c_B3=c_B3, s_B3=s_B3,
         V_eff_fabric=V_eff_fabric, dV_eff_fabric=dV_eff_fabric,
         n_fabric_sign_changes=len(fabric_sign_changes),
         gate_name='7-DOF-SADDLES-53', gate_verdict=verdict, gate_detail=detail,
         )
print(f"  Saved: s53_7dof_saddles.npz")

# --- Plot ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S53 — 7-DOF Saddle Analysis at $N_{\\rm pair}=1$',
             fontsize=14, fontweight='bold')

# Panel 1: V_KK and V_eff
ax = axes[0, 0]
ax.plot(tau_grid, V_KK_arr, 'b-', lw=2, label='$V_{KK}(\\tau)$')
ax.plot(tau_grid, V_eff_arr, 'r-', lw=2, label='$V_{eff} = V_{KK} + E_{cond}$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'fold $\\tau={tau_fold}$')
for tau_s, sr in unique_saddles.items():
    marker = 'o' if sr['type'] == 'minimum' else ('x' if sr['type'] == 'maximum' else 's')
    color = 'green' if sr['type'] == 'minimum' else 'red'
    ax.plot(tau_s, sr['V_eff'], marker, color=color, ms=10, zorder=5,
            label=f'{sr["type"]} $\\tau$={tau_s:.3f}')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$V$ [$M_{KK}^4$]')
ax.set_title('Effective Potential')
ax.legend(fontsize=7, loc='best')
ax.grid(True, alpha=0.3)

# Panel 2: E_cond(tau) zoomed
ax = axes[0, 1]
ax.plot(tau_grid, E_cond_arr, 'g-', lw=2, label='$E_{cond}(\\tau)$ (ED, $N=1$)')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.axhline(E_cond_H1, color='k', ls=':', alpha=0.3,
           label=f'$E_{{cond}}^{{fold}} = {E_cond_H1:.4f}$')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$E_{cond}$ [$M_{KK}^4$]')
ax.set_title('BCS Condensation Energy ($N_{pair}=1$)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Gradients
ax = axes[1, 0]
ax.plot(tau_grid, dV_KK_arr, 'b-', lw=2, label='$dV_{KK}/d\\tau$')
ax.plot(tau_grid, dE_cond_dtau, 'g-', lw=2, label='$dE_{cond}/d\\tau$')
ax.plot(tau_grid, dV_eff_arr, 'r-', lw=2, label='$dV_{eff}/d\\tau$')
ax.axhline(0, color='k', ls='-', alpha=0.3)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
for tau_s, sr in unique_saddles.items():
    marker = 'o' if sr['type'] == 'minimum' else 'x'
    color = 'green' if sr['type'] == 'minimum' else 'red'
    ax.plot(tau_s, 0, marker, color=color, ms=10, zorder=5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$dV/d\\tau$ [$M_{KK}^4$]')
ax.set_title('Potential Gradients')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Single-particle spectrum
ax = axes[1, 1]
ax.plot(tau_grid, eps_B1_arr, 'b-', lw=2, label='$\\epsilon_{B1}$ (singlet)')
ax.plot(tau_grid, eps_B2_arr, 'r-', lw=2, label='$\\epsilon_{B2}$ (adjoint)')
ax.plot(tau_grid, eps_B3_arr, 'orange', lw=2, label='$\\epsilon_{B3}$ (fund.)')
ax.fill_between(tau_grid, eps_B1_arr, eps_B2_arr, alpha=0.15, color='purple',
                label='B1-B2 gap')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\epsilon_k$ [$M_{KK}$]')
ax.set_title('Single-Particle Spectrum (Jensen model)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, 's53_7dof_saddles.png'), dpi=150, bbox_inches='tight')
print(f"  Saved: s53_7dof_saddles.png")

# ============================================================================
#  Final summary
# ============================================================================
print("\n" + "=" * 72)
print("  SUMMARY")
print("=" * 72)
print(f"""
  1. At N_pair = 1, the 7-DOF unified action reduces to 1-DOF: S_eff[tau].

  2. S_eff(tau) = V_KK(tau) + E_cond(tau):
     V_KK(fold) = {V_KK_arr[idx_fold]:.4f} M_KK^4 (gravitational, monotonically decreasing)
     E_cond(fold) = {E_cond_arr[idx_fold]:.4f} M_KK^4 (BCS pairing)
     |E_cond/V_KK| = {abs(E_cond_arr[idx_fold]/V_KK_arr[idx_fold]):.4e}

  3. E_cond(tau) varies as tau changes through the single-particle spectrum
     (B1-B2 gap closes at the fold, strengthening pairing).
     E_cond range: [{E_cond_arr.min():.4f}, {E_cond_arr.max():.4f}]

  4. SADDLE SEARCH: {n_saddles} interior critical points, {n_minima} minima.
     Gradient ratio |dE_cond/dV_KK| = {grad_ratio:.4f} at fold.

  5. PHONONIC FRAMING: {'A stabilization point EXISTS.' if n_minima > 0 else 'No equilibrium at N_pair=1. The modulus dynamics is dominated by V_KK. E_cond is a perturbative correction that can create local features but not overcome the monotonic geometric potential.'}

  6. CONSTRAINT MAP UPDATE:
     - V_eff(tau) at N_pair=1: {'HAS' if n_minima > 0 else 'NO'} local minimum
     - The spectral action monotonicity (W4) {'is broken' if n_minima > 0 else 'survives'} when E_cond is added
     - {'STABILIZATION via BCS backreaction on geometry: OPEN' if n_minima > 0 else 'Stabilization requires either N_pair >> 1 (CLOSED by W2-6) or a mechanism beyond BCS (OPEN)'}

  Gate: 7-DOF-SADDLES-53 = {verdict}
""")
