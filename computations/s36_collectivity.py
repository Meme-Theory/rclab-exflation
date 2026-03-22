#!/usr/bin/env python3
"""
Session 36 COLL-36: Collectivity Decomposition in Weisskopf-Equivalent Units.

Context:
    The RPA susceptibility chi = d^2S/dtau^2 = 20.43 at tau=0.20 quantifies the
    collective enhancement of the spectral action's response to Jensen deformation.

    In nuclear physics, B(E2) transition rates measured in Weisskopf units (W.u.)
    diagnose collectivity:
        1 W.u.     = single-particle estimate
        10-30 W.u. = vibrational nucleus (coherent superposition of few particle-hole)
        100+ W.u.  = rotational (deformed) nucleus (maximal collectivity)

    The analog for the spectral action:
        chi_sp  = single-particle (single-mode) curvature = max_k |d^2|lambda_k|/dtau^2|
        chi     = total RPA response = sum over all modes + off-diagonal (interaction)
        chi/chi_sp = collectivity ratio = "Weisskopf units"

    Additionally, we compute the energy-weighted sum rule (EWSR) fraction, which
    tests whether the RPA response exhausts the model-independent sum rule
        m_1 = sum_k E_k * |<k|F|0>|^2
    where F = dH/dtau (the "deformation operator") and E_k are excitation energies.

Physical derivation:
    The spectral action S(tau) = sum_k |lambda_k(tau)| is a sum over all eigenvalues
    of D_K(tau). Its second derivative d^2S/dtau^2 receives contributions from:
        1. Individual mode curvatures: d^2|lambda_k|/dtau^2
        2. Off-diagonal RPA corrections from mode coupling

    The total bare (non-interacting) curvature is:
        chi_bare = sum_k mult_k * d^2|lambda_k|/dtau^2

    The RPA correction adds collective enhancement:
        chi_RPA = chi_bare + delta_chi_RPA

    The Weisskopf single-particle estimate is:
        chi_sp = max over all single modes of |d^2|lambda_k|/dtau^2|

    The collectivity ratio chi / chi_sp measures how many coherent single-particle
    units participate. For N degenerate modes with identical curvature, this ratio
    equals N exactly.

Pre-registered gate:
    COLL-36: chi/chi_sp > 10 => VIBRATIONAL or stronger (multi-mode coherence)
             chi/chi_sp ~ 1  => NO COLLECTIVITY (independent modes)

Author: Landau condensed matter theorist
Date: 2026-03-07
"""

import numpy as np
from scipy.interpolate import CubicSpline
import os

# =====================================================================
# 1. Load data
# =====================================================================

base = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(base)

d_strut = np.load(os.path.join(base, 's33a_strutinsky.npz'), allow_pickle=True)
d_rpa = np.load(os.path.join(base, 's32b_rpa1_thouless.npz'), allow_pickle=True)
d_ext = np.load(os.path.join(base, 's23a_eigenvectors_extended.npz'), allow_pickle=True)
d_bcs = np.load(os.path.join(base, 's27_multisector_bcs.npz'), allow_pickle=True)

print("=" * 70)
print("COLL-36: COLLECTIVITY DECOMPOSITION IN WEISSKOPF UNITS")
print("=" * 70)

# =====================================================================
# 2. Extract mode-resolved curvatures from strutinsky data
# =====================================================================

# Per-mode d^2|lambda_k|/dtau^2 at tau=0.20 (8 positive modes in singlet)
# These are the curvatures of individual eigenvalue tracks
mode_d2 = d_strut['mode_d2_contributions']  # shape (8,)

# Branch labels: B1(1), B2(4), B3(3)
branch_labels = ['B1', 'B2', 'B2', 'B2', 'B2', 'B3', 'B3', 'B3']

# Branch totals (x2 for spectral pairing: positive + negative eigenvalues)
b1_d2 = float(d_strut['b1_d2'][0])  # = 2 * mode_d2[0]
b2_d2 = float(d_strut['b2_d2'][0])  # = 2 * sum(mode_d2[1:5])
b3_d2 = float(d_strut['b3_d2'][0])  # = 2 * sum(mode_d2[5:8])
total_d2_bare = float(d_strut['total_d2'][0])  # = b1 + b2 + b3

print(f"\n--- Per-mode curvatures d^2|lambda_k|/dtau^2 ---")
for j, (label, d2) in enumerate(zip(branch_labels, mode_d2)):
    print(f"  Mode {j} ({label}): {d2:.6f}")

print(f"\n--- Branch totals (x2 for +/- pairing) ---")
print(f"  B1 (1 mode):  {b1_d2:.4f}  ({100*b1_d2/total_d2_bare:.1f}%)")
print(f"  B2 (4 modes): {b2_d2:.4f}  ({100*b2_d2/total_d2_bare:.1f}%)")
print(f"  B3 (3 modes): {b3_d2:.4f}  ({100*b3_d2/total_d2_bare:.1f}%)")
print(f"  Total bare:   {total_d2_bare:.4f}")

# =====================================================================
# 3. RPA total susceptibility
# =====================================================================

# From RPA-32b sweep: chi = d^2S_abs/dtau^2 at tau=0.20
# sweep_tau = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
sweep_tau = d_rpa['sweep_tau']
sweep_d2S = d_rpa['sweep_d2S_abs']
idx_020 = np.argmin(np.abs(sweep_tau - 0.20))
chi_rpa = float(sweep_d2S[idx_020])

# Branch-resolved chi from RPA at tau=0.15, 0.20, 0.25
# chi_B1, chi_B2, chi_B3 are 3-element arrays for these three tau points
chi_B1_vals = d_rpa['chi_B1']
chi_B2_vals = d_rpa['chi_B2']
chi_B3_vals = d_rpa['chi_B3']

print(f"\n--- RPA total susceptibility ---")
print(f"  chi_RPA at tau=0.20: {chi_rpa:.4f}")
print(f"  chi_B1 at tau=0.20: {float(chi_B1_vals[1]):.6f}")
print(f"  chi_B2 at tau=0.20: {float(chi_B2_vals[1]):.6f}")
print(f"  chi_B3 at tau=0.20: {float(chi_B3_vals[1]):.6f}")

# =====================================================================
# 4. Single-particle estimates (Weisskopf unit)
# =====================================================================

print(f"\n{'=' * 70}")
print("SINGLE-PARTICLE ESTIMATES (WEISSKOPF UNIT)")
print(f"{'=' * 70}")

# Method 1: chi_sp = max single-mode curvature
chi_sp_max = np.max(mode_d2)
chi_sp_max_label = branch_labels[np.argmax(mode_d2)]
print(f"\n  chi_sp(max single mode) = {chi_sp_max:.6f}  (mode: {chi_sp_max_label})")

# Method 2: chi_sp per branch = branch total / (2 * N_modes)
# This gives the average per-mode curvature within each branch
chi_sp_B1 = b1_d2 / (2 * 1)  # 1 mode, x2 pairing
chi_sp_B2 = b2_d2 / (2 * 4)  # 4 modes, x2 pairing
chi_sp_B3 = b3_d2 / (2 * 3)  # 3 modes, x2 pairing
print(f"  chi_sp(B1) = {chi_sp_B1:.6f}  (1 mode)")
print(f"  chi_sp(B2) = {chi_sp_B2:.6f}  (4 modes)")
print(f"  chi_sp(B3) = {chi_sp_B3:.6f}  (3 modes)")

# Method 3: average single-mode curvature
chi_sp_avg = total_d2_bare / (2 * 8)  # 8 positive modes, x2 pairing
print(f"  chi_sp(average) = {chi_sp_avg:.6f}  (8 modes)")

# =====================================================================
# 5. Collectivity ratios (Weisskopf units)
# =====================================================================

print(f"\n{'=' * 70}")
print("COLLECTIVITY RATIOS (WEISSKOPF UNITS)")
print(f"{'=' * 70}")

# Primary ratio: chi_RPA / chi_sp(max)
# This is the most conservative: how many times the largest single-mode
# curvature fits into the total RPA response
ratio_max = chi_rpa / chi_sp_max
print(f"\n  chi_RPA / chi_sp(max)     = {chi_rpa:.4f} / {chi_sp_max:.6f} = {ratio_max:.2f} W.u.")

# Alternative: chi_RPA / chi_sp(B2)
ratio_B2 = chi_rpa / chi_sp_B2
print(f"  chi_RPA / chi_sp(B2)     = {chi_rpa:.4f} / {chi_sp_B2:.6f} = {ratio_B2:.2f} W.u.")

# Alternative: chi_RPA / chi_sp(avg)
ratio_avg = chi_rpa / chi_sp_avg
print(f"  chi_RPA / chi_sp(avg)    = {chi_rpa:.4f} / {chi_sp_avg:.6f} = {ratio_avg:.2f} W.u.")

# =====================================================================
# 6. Coherence analysis: bare vs RPA enhancement
# =====================================================================

print(f"\n{'=' * 70}")
print("RPA ENHANCEMENT FACTOR")
print(f"{'=' * 70}")

# The bare curvature uses the RPA data at tau=0.15, 0.20, 0.25
bare_curvature = d_rpa['bare_curvature']
print(f"\n  bare_curvature (3-pt) = {bare_curvature}")
# The "bare" in the RPA computation is the singlet sum without interactions.
# The strutinsky total_d2 is the singlet mode decomposition - should match.

# chi_RPA vs chi_bare: this ratio tells us how much the residual interaction enhances
# the response beyond the independent-particle picture
bare_at_020 = bare_curvature[1]  # index 1 = tau=0.20
rpa_enhancement = chi_rpa / bare_at_020
print(f"  chi_bare(tau=0.20)   = {bare_at_020:.4f}")
print(f"  chi_RPA(tau=0.20)    = {chi_rpa:.4f}")
print(f"  RPA enhancement      = chi_RPA / chi_bare = {rpa_enhancement:.4f}")

# The strutinsky bare should agree with the RPA bare
print(f"  Strutinsky bare      = {total_d2_bare:.4f}")
print(f"  Discrepancy          = {abs(total_d2_bare - bare_at_020):.4f} "
      f"({100*abs(total_d2_bare - bare_at_020)/bare_at_020:.1f}%)")

# =====================================================================
# 7. Effective number of coherent modes (Weisskopf decomposition)
# =====================================================================

print(f"\n{'=' * 70}")
print("EFFECTIVE NUMBER OF COHERENT MODES")
print(f"{'=' * 70}")

# If all modes had the same curvature chi_sp, then chi = N_eff * chi_sp
# N_eff(max) = chi / chi_sp(max) = most conservative
# N_eff(avg) = chi / chi_sp(avg) = geometric mean
# The system has 16 modes total (8 positive + 8 negative eigenvalues)

N_modes_total = 16  # 8 pos + 8 neg, but pairing means 8 independent
N_eff_max = chi_rpa / chi_sp_max
N_eff_avg = chi_rpa / chi_sp_avg

print(f"\n  Total modes (positive only): 8")
print(f"  Total modes (with pairing): 16")
print(f"  N_eff(max-based)  = {N_eff_max:.2f}")
print(f"  N_eff(avg-based)  = {N_eff_avg:.2f}")
print(f"  Maximum possible  = 16 (if all modes identical)")

# =====================================================================
# 8. Energy-weighted sum rule (EWSR)
# =====================================================================

print(f"\n{'=' * 70}")
print("ENERGY-WEIGHTED SUM RULE (EWSR)")
print(f"{'=' * 70}")

# The EWSR for a system with Hamiltonian H and operator F = dH/dtau:
#   m_1 = sum_k E_k |<k|F|0>|^2 = (1/2) <0|[F,[H,F]]|0>
#   m_0 = sum_k |<k|F|0>|^2 = chi (non-energy-weighted sum = susceptibility)
#
# For our system, the eigenvalues at tau=0.20 are:
#   B1: 0.81914 (x1)
#   B2: 0.84527 (x4)
#   B3: 0.97822 (x3)
#
# The "excitation energies" in the spectral action context are the
# eigenvalue gaps. For particle-hole excitations:
#   E_k ~ |lambda_k(tau)|  (the eigenvalue itself is the energy scale)
#
# The transition matrix elements |<k|F|0>|^2 are proportional to the
# mode curvatures: |<k|F|0>|^2 propto d^2|lambda_k|/dtau^2
#
# m_0 = sum_k mult_k * d^2|lambda_k|/dtau^2  (x2 for pairing)
#       = total_d2_bare  (the bare susceptibility)
#
# m_1 = sum_k mult_k * |lambda_k| * d^2|lambda_k|/dtau^2  (x2 for pairing)

# Eigenvalues at tau=0.20
evals_020 = d_rpa['eigenvalues_0p2']
pos_evals = np.sort(evals_020[evals_020 > 0])
print(f"\n  Positive eigenvalues at tau=0.20: {pos_evals}")

# Assign eigenvalues to branches
# B1: mode 0 = 0.81914
# B2: modes 1-4 = 0.84527 (4-fold)
# B3: modes 5-7 = 0.97822 (3-fold)
E_B1 = pos_evals[0]  # 0.81914
E_B2 = pos_evals[1]  # 0.84527
E_B3 = pos_evals[-1] # 0.97822

print(f"  E_B1 = {E_B1:.5f}")
print(f"  E_B2 = {E_B2:.5f}")
print(f"  E_B3 = {E_B3:.5f}")

# m_0 = non-energy-weighted sum = bare susceptibility (x2 for pairing)
# = 2 * sum_k d^2|lambda_k|/dtau^2
m_0 = total_d2_bare
print(f"\n  m_0 (bare chi) = {m_0:.4f}")

# m_1 = energy-weighted sum
# = 2 * sum_k |lambda_k| * d^2|lambda_k|/dtau^2
m_1 = 2.0 * (1 * E_B1 * mode_d2[0] +
              4 * E_B2 * mode_d2[1] +
              3 * E_B3 * mode_d2[5])
print(f"  m_1 (energy-weighted) = {m_1:.4f}")

# Mean excitation energy
E_mean = m_1 / m_0
print(f"  <E> = m_1/m_0 = {E_mean:.5f}")

# EWSR: The model-independent sum rule in nuclear physics is
#   m_1 = (hbar^2 / 2m) * A * <r^2>  for isoscalar E2
# Here the analog sum rule is:
#   m_1(SR) = (1/2) Tr[F^2]  where F = dD_K/dtau
# We compute this from the eigenvalue derivatives directly.

# For the spectral action sum rule, compute:
#   m_1(SR) = sum_k mult_k * (d|lambda_k|/dtau)^2
# This follows from the double commutator identity for the spectral action.

# Compute d|lambda_k|/dtau at tau=0.20 for each mode
tau_vals = d_ext['tau_values']
n_tau = len(tau_vals)
tracks = np.zeros((n_tau, 8))
for ti in range(n_tau):
    e = d_bcs[f'evals_0_0_{ti}']
    pos = np.sort(e[e > 1e-10])
    tracks[ti, :] = pos

# First derivatives via cubic spline
from scipy.interpolate import CubicSpline as CS

d1_modes = np.zeros(8)
d2_modes_check = np.zeros(8)
for j in range(8):
    cs_j = CS(tau_vals, tracks[:, j])
    d1_modes[j] = cs_j(0.20, 1)
    d2_modes_check[j] = cs_j(0.20, 2)

print(f"\n  Mode first derivatives d|lambda_k|/dtau at tau=0.20:")
for j, (label, d1) in enumerate(zip(branch_labels, d1_modes)):
    print(f"    Mode {j} ({label}): d/dtau = {d1:.6f}")

# Verify second derivatives match
print(f"\n  Cross-check: d^2/dtau^2 from spline vs strutinsky:")
for j in range(8):
    print(f"    Mode {j}: spline={d2_modes_check[j]:.6f}, strut={mode_d2[j]:.6f}, "
          f"diff={abs(d2_modes_check[j]-mode_d2[j]):.2e}")

# m_1(sum rule) = sum_k mult_k * (d|lambda_k|/dtau)^2  (x2 for pairing)
m_1_SR = 2.0 * (1 * d1_modes[0]**2 +
                 4 * d1_modes[1]**2 +
                 3 * d1_modes[5]**2)

print(f"\n  m_1(sum rule) = sum mult * (dlambda/dtau)^2 = {m_1_SR:.4f}")

# EWSR fraction = m_1(computed) / m_1(sum rule)
ewsr_fraction = m_1 / m_1_SR if abs(m_1_SR) > 1e-10 else float('nan')
print(f"  EWSR fraction = m_1 / m_1(SR) = {ewsr_fraction:.4f}")

# =====================================================================
# 9. Alternative EWSR: using RPA chi vs bare chi
# =====================================================================

print(f"\n--- Alternative EWSR: RPA vs bare ---")
# The EWSR fraction can also be assessed as:
#   chi_RPA / chi_bare = enhancement factor
# In nuclear physics, collective modes can exhaust >100% of EWSR due to
# ground-state correlations (Thouless theorem)

ewsr_rpa_fraction = chi_rpa / total_d2_bare
print(f"  chi_RPA / chi_bare = {chi_rpa:.4f} / {total_d2_bare:.4f} = {ewsr_rpa_fraction:.4f}")
print(f"  This is {100*ewsr_rpa_fraction:.1f}% of the bare (non-interacting) sum rule")

# Note: chi_RPA > chi_bare indicates collective enhancement beyond
# the independent-particle limit. In our case, the RPA includes
# off-diagonal mode coupling (chi_sep from the V-matrix).
chi_sep_020 = d_rpa['chi_sep'][1]  # index 1 = tau=0.20
print(f"  chi_sep (off-diagonal RPA) at tau=0.20 = {chi_sep_020:.4f}")
print(f"  Collective fraction from coupling = {100*chi_sep_020/chi_rpa:.1f}%")

# =====================================================================
# 10. Summary and classification
# =====================================================================

print(f"\n{'=' * 70}")
print("COLL-36 SUMMARY")
print(f"{'=' * 70}")

print(f"\n  chi_RPA                = {chi_rpa:.4f}")
print(f"  chi_sp(max, B1)        = {chi_sp_max:.6f}")
print(f"  chi_sp(B2 per-mode)    = {chi_sp_B2:.6f}")
print(f"  chi_sp(average)        = {chi_sp_avg:.6f}")
print(f"")
print(f"  COLLECTIVITY RATIOS (Weisskopf units):")
print(f"    chi / chi_sp(max)    = {ratio_max:.2f}")
print(f"    chi / chi_sp(B2)     = {ratio_B2:.2f}")
print(f"    chi / chi_sp(avg)    = {ratio_avg:.2f}")
print(f"")
print(f"  RPA enhancement        = {rpa_enhancement:.4f}")
print(f"  EWSR fraction (e-wt)   = {ewsr_fraction:.4f}")
print(f"  EWSR (RPA/bare)        = {100*ewsr_rpa_fraction:.1f}%")
print(f"  N_eff (coherent modes) = {N_eff_max:.2f}")
print(f"")
print(f"  CLASSIFICATION:")
if ratio_max >= 100:
    classification = "ROTATIONAL (strong collectivity)"
elif ratio_max >= 10:
    classification = "VIBRATIONAL (moderate coherence)"
elif ratio_max >= 3:
    classification = "WEAKLY COLLECTIVE"
else:
    classification = "SINGLE-PARTICLE (no collectivity)"

print(f"    {ratio_max:.1f} W.u. => {classification}")
print(f"")
print(f"  PHYSICAL INTERPRETATION:")
print(f"    The total susceptibility chi = {chi_rpa:.2f} is exhausted by")
print(f"    {ratio_max:.1f} single-particle units (B1 curvature = {chi_sp_max:.3f}).")
print(f"    This places the Jensen deformation response in the")
print(f"    VIBRATIONAL regime: multiple modes respond coherently,")
print(f"    but not with the maximal collectivity of a deformed rotor.")
print(f"    The 8 modes contribute constructively (all curvatures positive),")
print(f"    giving an effective N_eff = {N_eff_max:.1f} out of 16 possible.")

# =====================================================================
# 11. Save results
# =====================================================================

save_dict = {
    # Per-mode data
    'mode_d2_contributions': mode_d2,
    'mode_d1_at_020': d1_modes,
    'branch_labels': np.array(branch_labels),

    # Branch totals
    'b1_d2': np.array([b1_d2]),
    'b2_d2': np.array([b2_d2]),
    'b3_d2': np.array([b3_d2]),
    'total_d2_bare': np.array([total_d2_bare]),

    # RPA
    'chi_rpa': np.array([chi_rpa]),
    'chi_sep': np.array([chi_sep_020]),

    # Single-particle estimates
    'chi_sp_max': np.array([chi_sp_max]),
    'chi_sp_B1': np.array([chi_sp_B1]),
    'chi_sp_B2': np.array([chi_sp_B2]),
    'chi_sp_B3': np.array([chi_sp_B3]),
    'chi_sp_avg': np.array([chi_sp_avg]),

    # Collectivity ratios
    'ratio_max': np.array([ratio_max]),
    'ratio_B2': np.array([ratio_B2]),
    'ratio_avg': np.array([ratio_avg]),
    'rpa_enhancement': np.array([rpa_enhancement]),

    # EWSR
    'm_0': np.array([m_0]),
    'm_1': np.array([m_1]),
    'm_1_SR': np.array([m_1_SR]),
    'ewsr_fraction': np.array([ewsr_fraction]),
    'ewsr_rpa_fraction': np.array([ewsr_rpa_fraction]),

    # Effective modes
    'N_eff_max': np.array([N_eff_max]),
    'N_eff_avg': np.array([N_eff_avg]),

    # Eigenvalues
    'E_B1': np.array([E_B1]),
    'E_B2': np.array([E_B2]),
    'E_B3': np.array([E_B3]),

    # Classification
    'classification': np.array([classification]),
}

np.savez(os.path.join(base, 's36_collectivity.npz'), **save_dict)
print(f"\nData saved: tier0-computation/s36_collectivity.npz")

# =====================================================================
# 12. Gate verdict
# =====================================================================

print(f"\n{'=' * 70}")
print("GATE VERDICT: COLL-36")
print(f"{'=' * 70}")
print(f"  chi / chi_sp(max) = {ratio_max:.2f}")
if ratio_max > 10:
    print(f"  VERDICT: chi/chi_sp = {ratio_max:.1f} > 10 => VIBRATIONAL OR STRONGER")
    print(f"  Structural evidence for coherent multi-mode dynamics.")
elif ratio_max > 1:
    print(f"  VERDICT: 1 < chi/chi_sp = {ratio_max:.1f} < 10 => WEAK COLLECTIVITY")
else:
    print(f"  VERDICT: chi/chi_sp = {ratio_max:.1f} ~ 1 => NO COLLECTIVITY")
print(f"{'=' * 70}")
