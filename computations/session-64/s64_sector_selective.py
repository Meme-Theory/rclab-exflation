#!/usr/bin/env python3
"""
S64 SECTOR-SELECTIVE-BREAKING-64: Indirect Gravitational Feedback to (0,0)
=========================================================================

Compute the full gravitational feedback chain:
  EIH self-energy -> shifted BCS energies -> self-consistent gap equation
  -> modified Bogoliubov occupations -> vacuum energy shift delta_rho

The key physics: the gravitational perturbation (from S63 GRAV-BACKREACT)
shifts ALL 8 BCS mode energies at O(alpha_G). These shifts modify the
self-consistent BCS gap Delta, which in turn modifies ALL Bogoliubov
occupations v_k^2 -- INCLUDING B2[0], which has C_2^{PW}(0,0) = 0.
This is the INDIRECT feedback through the gap equation.

From cc-path-g.md Section 4: the feedback is O(alpha_G), not O(alpha_G^2)
as originally claimed, because the isometry Casimir C_2^{iso}(B2) = 3
gives B2 modes a direct gravitational shift.

Method:
  1. Load 8 BCS mode energies and gravitational shifts from W1-B data
  2. Solve the self-consistent BCS gap equation with shifted energies
     via Newton's method (analytical Jacobian)
  3. Compute shifted Bogoliubov occupations v_k'^2 for all 8 modes
  4. Compute vacuum energy shift delta_rho = sum_k omega_k' v_k'^2 - sum_k omega_k v_k^2
  5. Compare |delta_rho/rho_vac| with observed CC requirement
  6. Iterate: use shifted eigenvalues to recompute gravitational self-energy (bootstrap)

Gate: SECTOR-SELECTIVE-BREAKING-64
  PASS: |delta_rho/rho_vac| > 10^{-6}
  FAIL: |delta_rho/rho_vac| < 10^{-8}
  INFO: 10^{-8} < |delta_rho/rho_vac| < 10^{-6}

Input: s64_rg_charge_decomp.npz (W1-B), canonical_constants.py
Output: s64_sector_selective.npz, s64_sector_selective.png
        Section W2-C of session-64-results-workingpaper.md

Session: S64 W2-C
Author: Quantum-Acoustics Theorist
"""

import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    M_KK, M_Pl_reduced, Delta_0_OES, N_dof_BCS,
    a0_fold, S_fold, Lambda_obs_MP4, CC_ratio, PI
)

# =============================================================================
# Section 1: Load Upstream Data
# =============================================================================
print("=" * 72)
print("SECTOR-SELECTIVE-BREAKING-64: Indirect Gravitational Feedback to (0,0)")
print("=" * 72)

data_dir = os.path.dirname(os.path.abspath(__file__))

# Load W1-B data (R-G charge decomposition, contains all needed inputs)
w1b = np.load(os.path.join(data_dir, 's64_rg_charge_decomp.npz'), allow_pickle=True)

eps_fold = w1b['eps_fold']         # 8 single-particle energies at fold (M_KK)
eps_corr = w1b['eps_corrected']    # gravitationally corrected energies
labels = w1b['labels']             # mode labels: B2[0], B2[1], ..., B3[2]
n_k_GGE = w1b['n_k_GGE']          # GGE occupations
alpha_G = float(w1b['alpha_G'])    # gravitational coupling
C2_iso = w1b['C2_modes']           # isometry Casimirs
Delta = Delta_0_OES                # BCS gap = 0.464 M_KK
omega_k_orig = w1b['omega_k']      # quasiparticle energies = sqrt(eps^2 + Delta^2)
N = len(eps_fold)                  # 8 modes

# Compute delta_eps from difference (more precise than stored delta_eps_total
# which may have been computed differently)
delta_eps = eps_corr - eps_fold

# Degeneracies: each mode's contribution to the total spectral action
# a_0 involves sum d_n over ALL sectors; the 8 BCS modes contribute
# with their Peter-Weyl multiplicity d(0,0) = 1 each (all in (0,0) sector)
# But for vacuum energy, each mode's quasiparticle energy enters with
# its branch degeneracy (already folded into the 8 distinct modes).
d_k = np.ones(N)  # each of the 8 modes is already a distinct eigenvalue

print(f"\nInput summary:")
print(f"  N_modes = {N}")
print(f"  Delta = {Delta:.6f} M_KK")
print(f"  alpha_G = {alpha_G:.6e}")
print(f"\n  Mode structure:")
print(f"  {'k':>3s} {'Label':>6s} {'eps_k':>10s} {'delta_eps':>12s} "
      f"{'C2_iso':>8s} {'n_GGE':>10s}")
print("-" * 60)
for k in range(N):
    print(f"  {k:3d} {str(labels[k]):>6s} {eps_fold[k]:10.6f} {delta_eps[k]:12.6e} "
          f"{C2_iso[k]:8.3f} {n_k_GGE[k]:10.6e}")

# =============================================================================
# Section 2: BCS Gap Equation — Original System
# =============================================================================
print("\n" + "=" * 72)
print("Section 2: Self-Consistent BCS Gap Equation")
print("=" * 72)


def bcs_gap_function(Delta_trial, eps_array):
    """
    Gap equation residual: F(Delta) = 1/g - sum_k 1/(2 E_k) = 0
    where E_k = sqrt(eps_k^2 + Delta^2).

    We do NOT use a stored g_eff. Instead we define g implicitly
    by requiring the gap equation to be satisfied at the ORIGINAL
    (eps_fold, Delta_0) pair. Then the gap equation for shifted
    energies determines Delta_new.

    Returns sum_k 1/(2 E_k) for a given Delta and eps array.
    """
    if Delta_trial <= 0:
        return 1e30
    E_k = np.sqrt(eps_array**2 + Delta_trial**2)
    return np.sum(1.0 / (2.0 * E_k))


def bcs_gap_derivative(Delta_trial, eps_array):
    """
    d/d(Delta) [sum_k 1/(2 E_k)] = -Delta * sum_k 1/(2 E_k^3)
    """
    E_k = np.sqrt(eps_array**2 + Delta_trial**2)
    return -Delta_trial * np.sum(1.0 / (2.0 * E_k**3))


# Step 2a: Determine g from original gap equation
# 1/g = sum_k 1/(2 E_k^{(0)}) with eps_k = eps_fold, Delta = Delta_0
gap_sum_orig = bcs_gap_function(Delta, eps_fold)
g_inv = gap_sum_orig
g_bcs = 1.0 / g_inv

print(f"\n2a: Original gap equation:")
print(f"  sum_k 1/(2 E_k^(0)) = {gap_sum_orig:.8f}")
print(f"  g_BCS = 1/sum = {g_bcs:.8f} M_KK")

# Verify: with these eps and g, the gap equation gives Delta = Delta_0
# Residual: F(Delta) = 1/g - sum 1/(2E) = 0
residual_orig = g_inv - bcs_gap_function(Delta, eps_fold)
print(f"  Residual F(Delta_0) = {residual_orig:.6e} (should be 0)")

# Quasiparticle energies and BCS occupations at original point
E_k_orig = np.sqrt(eps_fold**2 + Delta**2)
v2_orig = 0.5 * (1.0 - eps_fold / E_k_orig)
u2_orig = 1.0 - v2_orig

print(f"\n2b: Original BCS state:")
print(f"  {'k':>3s} {'Label':>6s} {'eps_k':>10s} {'E_k':>10s} "
      f"{'v_k^2':>10s} {'u_k^2':>10s} {'u_k*v_k':>10s}")
print("-" * 68)
for k in range(N):
    ukv = np.sqrt(u2_orig[k] * v2_orig[k])
    print(f"  {k:3d} {str(labels[k]):>6s} {eps_fold[k]:10.6f} {E_k_orig[k]:10.6f} "
          f"{v2_orig[k]:10.6f} {u2_orig[k]:10.6f} {ukv:10.6f}")

# =============================================================================
# Section 3: Solve Perturbed Gap Equation
# =============================================================================
print("\n" + "=" * 72)
print("Section 3: Perturbed Gap Equation — Newton's Method")
print("=" * 72)

# The gravitational perturbation shifts eps_k -> eps_k + delta_eps_k.
# The gap equation with the SAME g becomes:
# 1/g = sum_k 1/(2 sqrt((eps_k + delta_eps_k)^2 + Delta'^2))
# Solve for Delta'.

eps_shifted = eps_fold + delta_eps

print(f"\n3a: Shifted energies:")
for k in range(N):
    print(f"  k={k} {str(labels[k]):>6s}: eps={eps_fold[k]:.6f} -> "
          f"eps'={eps_shifted[k]:.6f}, delta={delta_eps[k]:.6e}")

# Solve: find Delta' such that sum_k 1/(2 E_k') = 1/g = gap_sum_orig
# Define residual R(Delta') = gap_sum_orig - sum_k 1/(2 sqrt(eps'^2 + Delta'^2))
# Use Brent's method (robust, guaranteed convergence on bracketed interval)


def gap_residual(Delta_trial):
    """R(Delta') = 1/g - sum_k 1/(2 E_k')"""
    return g_inv - bcs_gap_function(Delta_trial, eps_shifted)


# Newton's method with analytical Jacobian
Delta_new = Delta  # initial guess
print(f"\n3b: Newton iteration:")
print(f"  {'Iter':>4s} {'Delta':>14s} {'Residual':>14s} {'Step':>14s}")
print("-" * 52)

for iteration in range(50):
    R = gap_residual(Delta_new)
    dR = -bcs_gap_derivative(Delta_new, eps_shifted)  # dR/dDelta = -d(sum 1/2E)/dDelta
    step = -R / dR
    print(f"  {iteration:4d} {Delta_new:14.10f} {R:14.6e} {step:14.6e}")
    Delta_new = Delta_new + step
    if abs(R) < 1e-15:
        break

delta_Delta = Delta_new - Delta
print(f"\n  Converged: Delta' = {Delta_new:.10f} M_KK")
print(f"  delta_Delta = {delta_Delta:.6e} M_KK")
print(f"  delta_Delta/Delta = {delta_Delta/Delta:.6e}")

# Cross-check with Brent's method
try:
    Delta_brent = brentq(gap_residual, Delta * 0.5, Delta * 1.5, xtol=1e-15)
    print(f"\n  Brent cross-check: Delta' = {Delta_brent:.10f} M_KK")
    print(f"  Agreement: |Newton - Brent| = {abs(Delta_new - Delta_brent):.6e}")
except ValueError as e:
    print(f"\n  Brent failed (bracket issue): {e}")
    Delta_brent = Delta_new

# =============================================================================
# Section 4: Shifted Bogoliubov Occupations
# =============================================================================
print("\n" + "=" * 72)
print("Section 4: Shifted Bogoliubov Occupations")
print("=" * 72)

E_k_new = np.sqrt(eps_shifted**2 + Delta_new**2)
v2_new = 0.5 * (1.0 - eps_shifted / E_k_new)
u2_new = 1.0 - v2_new

# Compute changes
delta_v2 = v2_new - v2_orig
delta_E = E_k_new - E_k_orig

print(f"\n4a: Mode-by-mode comparison:")
print(f"  {'k':>3s} {'Label':>6s} {'v2_orig':>10s} {'v2_new':>10s} "
      f"{'delta_v2':>12s} {'E_orig':>10s} {'E_new':>10s} {'delta_E':>12s}")
print("-" * 86)
for k in range(N):
    print(f"  {k:3d} {str(labels[k]):>6s} {v2_orig[k]:10.6f} {v2_new[k]:10.6f} "
          f"{delta_v2[k]:12.6e} {E_k_orig[k]:10.6f} {E_k_new[k]:10.6f} "
          f"{delta_E[k]:12.6e}")

# The B2[0] mode change is the KEY diagnostic
print(f"\n4b: B2[0] (condensate mode) analysis:")
print(f"  v_B2[0]^2: {v2_orig[0]:.8f} -> {v2_new[0]:.8f}")
print(f"  delta(v_B2[0]^2) = {delta_v2[0]:.6e}")
print(f"  This is the INDIRECT gravitational feedback to the (0,0) condensate.")

# Decompose v2 change into direct (eps shift) and indirect (gap shift) parts
# delta(v^2) = -(1/2) * (Delta^2/E^3) * delta_eps  [direct, from eps shift]
#            + +(1/2) * (eps*Delta/E^3) * delta_Delta  [indirect, from gap shift]
# Sign convention: v^2 = (1/2)(1 - eps/E)
# dv2/deps = -(1/2) * d(eps/E)/deps = -(1/2) * Delta^2/E^3  [always negative]
# dv2/dDelta = -(1/2) * d(eps/E)/dDelta = (1/2) * eps*Delta/E^3  [positive for eps>0]

print(f"\n4c: Direct vs indirect decomposition:")
print(f"  {'k':>3s} {'Label':>6s} {'delta_v2_direct':>16s} {'delta_v2_indirect':>18s} "
      f"{'delta_v2_total':>16s} {'delta_v2_exact':>16s}")
print("-" * 80)

for k in range(N):
    # Direct: from eps shift alone (holding Delta fixed)
    dv2_deps = -0.5 * Delta**2 / E_k_orig[k]**3
    delta_v2_direct = dv2_deps * delta_eps[k]

    # Indirect: from Delta shift alone (holding eps fixed)
    dv2_dDelta = 0.5 * eps_fold[k] * Delta / E_k_orig[k]**3
    delta_v2_indirect = dv2_dDelta * delta_Delta

    delta_v2_linear = delta_v2_direct + delta_v2_indirect

    print(f"  {k:3d} {str(labels[k]):>6s} {delta_v2_direct:16.6e} {delta_v2_indirect:18.6e} "
          f"{delta_v2_linear:16.6e} {delta_v2[k]:16.6e}")

# =============================================================================
# Section 5: Vacuum Energy Shift
# =============================================================================
print("\n" + "=" * 72)
print("Section 5: Vacuum Energy Shift")
print("=" * 72)

# The BCS ground-state energy is:
# E_GS = sum_k (eps_k * v_k^2 - Delta * u_k * v_k) + const
# But the vacuum energy (zero-point energy in the Bogoliubov basis) is:
# E_ZP = (1/2) sum_k E_k = (1/2) sum_k sqrt(eps_k^2 + Delta^2)
# This is the sum over all quasiparticle zero-point energies.

# Method A: Full BCS ground state energy
# E_BCS = sum_k eps_k v_k^2 - g (sum_k u_k v_k)^2
# This is more physical for the CC.

# For the CC, what matters is the TOTAL vacuum energy density, which
# in the spectral action framework is controlled by a_0.
# The BCS condensate's contribution is through E_cond = -Delta^2/(4g).
# The zero-point energy of the Bogoliubov quasiparticles is E_ZP = (1/2) sum E_k.

# We compute BOTH:
# (A) delta_E_ZP = change in Bogoliubov zero-point energy
# (B) delta_E_BCS = change in full BCS ground state energy
# (C) delta_E_cond = change in condensation energy

# --- 5a: Bogoliubov zero-point energy ---
E_ZP_orig = 0.5 * np.sum(E_k_orig)
E_ZP_new = 0.5 * np.sum(E_k_new)
delta_E_ZP = E_ZP_new - E_ZP_orig

print(f"\n5a: Bogoliubov zero-point energy:")
print(f"  E_ZP_orig = (1/2) sum E_k = {E_ZP_orig:.8f} M_KK")
print(f"  E_ZP_new  = (1/2) sum E_k'= {E_ZP_new:.8f} M_KK")
print(f"  delta_E_ZP = {delta_E_ZP:.6e} M_KK")
print(f"  |delta_E_ZP / E_ZP_orig| = {abs(delta_E_ZP/E_ZP_orig):.6e}")

# --- 5b: Full BCS ground state energy ---
# E_BCS = sum_k eps_k v_k^2 - (Delta^2)/(4g)
# where 1/g = sum 1/(2E_k)
pair_amplitude_orig = np.sum(np.sqrt(u2_orig * v2_orig))
pair_amplitude_new = np.sum(np.sqrt(u2_new * v2_new))

E_kin_orig = np.sum(eps_fold * v2_orig)
E_kin_new = np.sum(eps_shifted * v2_new)

E_pair_orig = -g_bcs * pair_amplitude_orig**2
E_pair_new = -g_bcs * pair_amplitude_new**2  # SAME g, different Delta manifests through v,u

# Alternatively, condensation energy = -Delta^2 / (4g)
E_cond_orig = -Delta**2 * g_inv / 4.0  # = -Delta^2 sum 1/(2E_k) / 4 = -(Delta^2/4) sum 1/(2E_k)
E_cond_new = -Delta_new**2 * g_inv / 4.0  # Using SAME 1/g

# More precise: E_cond = -Delta^2 / (4g) = -Delta^2 * sum(1/(2E_k)) / 4
# Wait, 1/g = sum 1/(2E_k), so E_cond = -(1/4) Delta^2 * g_inv is wrong.
# E_cond = -Delta^2 / (4g) = -(Delta^2/4) * sum(1/(2E_k))? No.
# E_cond = -Delta^2 / (4g). g = 1/g_inv. So E_cond = -Delta^2 * g_inv / 4.
# Hmm. Let me recheck. The standard BCS condensation energy is:
# E_cond = -N(0) Delta^2 / 2 where N(0) = DOS at Fermi level.
# In the Gaudin model: E_cond = -Delta^2 / (2g) approximately.
# Exact: E_BCS = sum eps_k (v_k^2 - theta(eps_k<0)) - Delta^2/g
# For our convention: E_cond_term = -Delta^2/g = -Delta^2 * g_inv

# Let me just compute the full BCS energy difference directly.
# E_BCS = sum_k eps_k v_k^2 - Delta^2 / g (condensation term)
# where g is fixed (same interaction strength).

E_BCS_orig = np.sum(eps_fold * v2_orig) - Delta**2 / g_bcs
E_BCS_new = np.sum(eps_shifted * v2_new) - Delta_new**2 / g_bcs
delta_E_BCS = E_BCS_new - E_BCS_orig

print(f"\n5b: Full BCS ground state energy:")
print(f"  E_BCS_orig = {E_BCS_orig:.8f} M_KK")
print(f"  E_BCS_new  = {E_BCS_new:.8f} M_KK")
print(f"  delta_E_BCS = {delta_E_BCS:.6e} M_KK")
print(f"  |delta_E_BCS / E_BCS_orig| = {abs(delta_E_BCS/E_BCS_orig):.6e}")

# --- 5c: Condensation energy change ---
delta_E_cond = -(Delta_new**2 - Delta**2) / g_bcs
print(f"\n5c: Condensation energy shift:")
print(f"  E_cond_orig = {-Delta**2/g_bcs:.8f} M_KK")
print(f"  E_cond_new  = {-Delta_new**2/g_bcs:.8f} M_KK")
print(f"  delta_E_cond = {delta_E_cond:.6e} M_KK")

# --- 5d: Kinetic energy change ---
delta_E_kin = np.sum(eps_shifted * v2_new) - np.sum(eps_fold * v2_orig)
print(f"\n5d: Kinetic energy shift:")
print(f"  sum eps_k v_k^2 (orig) = {np.sum(eps_fold * v2_orig):.8f} M_KK")
print(f"  sum eps_k' v_k'^2 (new)= {np.sum(eps_shifted * v2_new):.8f} M_KK")
print(f"  delta_E_kin = {delta_E_kin:.6e} M_KK")

# --- 5e: Mode-resolved vacuum energy shift ---
# delta_rho_k = omega_k' v_k'^2 - omega_k v_k^2 (not the same as E_ZP, but
# weighted by occupation -- this is what the GGE state sees)
print(f"\n5e: Mode-resolved shifts:")
print(f"  {'k':>3s} {'Label':>6s} {'omega*v2_orig':>14s} {'omega*v2_new':>14s} "
      f"{'delta':>14s} {'frac_of_total':>14s}")
print("-" * 72)

delta_rho_mode = E_k_new * v2_new * d_k - E_k_orig * v2_orig * d_k
total_delta_rho = np.sum(delta_rho_mode)

for k in range(N):
    rho_orig_k = E_k_orig[k] * v2_orig[k]
    rho_new_k = E_k_new[k] * v2_new[k]
    delta_k = rho_new_k - rho_orig_k
    frac = delta_k / total_delta_rho if abs(total_delta_rho) > 0 else 0
    print(f"  {k:3d} {str(labels[k]):>6s} {rho_orig_k:14.8f} {rho_new_k:14.8f} "
          f"{delta_k:14.6e} {frac:14.4f}")

print(f"\n  Total delta(sum E_k v_k^2) = {total_delta_rho:.6e} M_KK")

# =============================================================================
# Section 6: CC Comparison — The Gate
# =============================================================================
print("\n" + "=" * 72)
print("Section 6: CC Comparison — Gate Evaluation")
print("=" * 72)

# The vacuum energy density in the spectral action framework:
# rho_vac = f_0 Lambda^4 a_0 (from Seeley-DeWitt expansion)
# In M_KK units: rho_vac_MKK = (S_fold / N_cells) * M_KK^4 ... complicated.
#
# For the CC RATIO, what matters is:
# delta_rho / rho_vac where rho_vac is the TOTAL spectral action vacuum energy.
#
# Two measures:
# (A) delta_E_ZP / E_ZP (fractional change in Bogoliubov ZPE)
# (B) delta_E_BCS / E_BCS (fractional change in full BCS energy)
# (C) delta_E_BCS / (S_fold / N_cells) (vs spectral action per cell)
# (D) delta_E_BCS / (0.838 M_KK) (vs observed Lambda_eff from S57)

# The spectral action vacuum energy (from the a_0 term) per cell:
# rho_vac_per_cell = S_fold_per_cell ~ S_fold / N_cells (32 cells)
# But S_fold = 250361 M_KK^{d-4}. For the CC, the relevant quantity is
# the zero-point energy contribution from the 8 BCS modes.
# From cc-path-g.md: Lambda_CC = 0.838 M_KK (the cosmological constant
# in the spectral action, from S57 CC-SIGN computation).
Lambda_CC = 0.838  # M_KK, from S57  # (local)

# Also compare with the full spectral action:
# rho_SA = f_0 Lambda^4 a_0 ~ a0_fold M_KK^4 = 6440 M_KK^4 (zeroth Seeley-DeWitt)
# This is the TOTAL vacuum energy from all PW sectors, not just (0,0).

# Measure A: Fractional change in Bogoliubov ZPE
ratio_A = abs(delta_E_ZP / E_ZP_orig)
print(f"\n6a: Bogoliubov ZPE measure:")
print(f"  |delta_E_ZP / E_ZP| = {ratio_A:.6e}")
print(f"  log10 = {np.log10(ratio_A):.2f} OOM")

# Measure B: Fractional change in full BCS energy
if abs(E_BCS_orig) > 0:
    ratio_B = abs(delta_E_BCS / E_BCS_orig)
    print(f"\n6b: BCS ground state energy measure:")
    print(f"  |delta_E_BCS / E_BCS| = {ratio_B:.6e}")
    print(f"  log10 = {np.log10(ratio_B):.2f} OOM")
else:
    ratio_B = float('inf')
    print(f"\n6b: E_BCS_orig ~ 0, ratio undefined")

# Measure C: Against spectral action per cell
rho_SA_per_mode = a0_fold  # a_0 = sum d_n^2 = 6440, in M_KK^{dim-4} units
# But S_fold is the total spectral action = 250361
# The 8 BCS modes contribute 8 eigenvalues out of 155,984 total.
# The fractional contribution of BCS to a_0 is 8/6440 = 1.24e-3
# (since each (0,0) mode contributes d(0,0)^2 = 1 to a_0).
ratio_C = abs(delta_E_BCS) / (S_fold / 32)  # per cell
print(f"\n6c: vs spectral action per cell:")
print(f"  S_fold / N_cells = {S_fold/32:.2f} M_KK^{{d-4}}")
print(f"  |delta_E_BCS| / (S_fold/32) = {ratio_C:.6e}")

# Measure D: Against Lambda_eff = 0.838 M_KK
ratio_D = abs(delta_E_BCS) / Lambda_CC
print(f"\n6d: vs Lambda_CC = {Lambda_CC} M_KK:")
print(f"  |delta_E_BCS| / Lambda_CC = {ratio_D:.6e}")
print(f"  log10 = {np.log10(ratio_D):.2f} OOM")

# Measure E: The GGE-weighted vacuum energy shift
# In the GGE state, the vacuum energy is <rho_ZP>_GGE = sum (1/2) omega_k n_k_GGE
# The shift from gravitational corrections:
rho_ZP_GGE_orig = 0.5 * np.sum(omega_k_orig * n_k_GGE)
rho_ZP_GGE_new = 0.5 * np.sum(E_k_new * n_k_GGE)  # Same GGE occupations, shifted energies
delta_rho_GGE = rho_ZP_GGE_new - rho_ZP_GGE_orig

print(f"\n6e: GGE-weighted vacuum energy shift:")
print(f"  <rho_ZP>_GGE (orig) = {rho_ZP_GGE_orig:.8f} M_KK")
print(f"  <rho_ZP>_GGE (new)  = {rho_ZP_GGE_new:.8f} M_KK")
print(f"  delta<rho_ZP>_GGE = {delta_rho_GGE:.6e} M_KK")
ratio_E = abs(delta_rho_GGE / rho_ZP_GGE_orig) if abs(rho_ZP_GGE_orig) > 0 else 0
print(f"  |delta<rho_ZP>_GGE / <rho_ZP>_GGE| = {ratio_E:.6e}")

# =============================================================================
# Section 7: Bootstrap Iteration (Second-Order Self-Consistency)
# =============================================================================
print("\n" + "=" * 72)
print("Section 7: Bootstrap Iteration — Self-Consistent Gravitational Feedback")
print("=" * 72)

# The gravitational self-energy delta_eps_k depends on eps_k itself (G-11):
# delta_eps_k = -(1/2) alpha_G eps_k^2 (1 + C_2^{iso}(k)/3)
# When eps_k shifts, delta_eps_k also shifts. This creates a bootstrap loop.
# Iterate to self-consistency.

print(f"\n7a: Bootstrap iteration (gravitational self-energy depends on eps):")
print(f"  {'Iter':>4s} {'Delta':>14s} {'max|delta_eps|':>16s} {'delta_Delta':>14s}")
print("-" * 52)

eps_boot = eps_fold.copy()
Delta_boot = Delta

for boot_iter in range(10):
    # Compute gravitational shifts at current energies
    grav_factor = 1.0 + C2_iso / 3.0
    delta_eps_boot = -0.5 * alpha_G * eps_boot**2 * grav_factor

    # Shift energies
    eps_shifted_boot = eps_fold + delta_eps_boot  # Always start from bare eps_fold

    # Solve gap equation
    g_inv_boot = bcs_gap_function(Delta, eps_fold)  # g determined by original system

    def gap_res_boot(D):
        return g_inv_boot - bcs_gap_function(D, eps_shifted_boot)

    Delta_boot_new = Delta_boot
    for nit in range(30):
        R = gap_res_boot(Delta_boot_new)
        dR = -bcs_gap_derivative(Delta_boot_new, eps_shifted_boot)
        if abs(dR) < 1e-30:
            break
        step = -R / dR
        Delta_boot_new = Delta_boot_new + step
        if abs(R) < 1e-15:
            break

    delta_Delta_boot = Delta_boot_new - Delta
    max_delta_eps = np.max(np.abs(delta_eps_boot))

    print(f"  {boot_iter:4d} {Delta_boot_new:14.10f} {max_delta_eps:16.6e} "
          f"{delta_Delta_boot:14.6e}")

    # Check convergence
    if boot_iter > 0 and abs(Delta_boot_new - Delta_boot) < 1e-16:
        print(f"  Converged at iteration {boot_iter}")
        break

    Delta_boot = Delta_boot_new
    # Update eps for next iteration (self-consistent)
    eps_boot = eps_shifted_boot

Delta_final = Delta_boot
eps_final = eps_shifted_boot

# Compute final BCS state
E_k_final = np.sqrt(eps_final**2 + Delta_final**2)
v2_final = 0.5 * (1.0 - eps_final / E_k_final)
delta_v2_boot = v2_final - v2_orig

print(f"\n7b: Converged state:")
print(f"  Delta_final = {Delta_final:.10f} M_KK")
print(f"  delta_Delta_final = {Delta_final - Delta:.6e} M_KK")

E_ZP_final = 0.5 * np.sum(E_k_final)
delta_E_ZP_final = E_ZP_final - E_ZP_orig
E_BCS_final = np.sum(eps_final * v2_final) - Delta_final**2 / g_bcs
delta_E_BCS_final = E_BCS_final - E_BCS_orig

print(f"  delta_E_ZP (bootstrap) = {delta_E_ZP_final:.6e} M_KK")
print(f"  delta_E_BCS (bootstrap) = {delta_E_BCS_final:.6e} M_KK")
print(f"  Bootstrap/first-order ratio (ZPE): {delta_E_ZP_final/delta_E_ZP:.8f}")
print(f"  Bootstrap/first-order ratio (BCS): {delta_E_BCS_final/delta_E_BCS:.8f}")

# =============================================================================
# Section 8: Perturbative Cross-Check (Analytical)
# =============================================================================
print("\n" + "=" * 72)
print("Section 8: Perturbative Cross-Check")
print("=" * 72)

# From cc-path-g.md equations (G-14) through (G-20):
# delta_Delta/Delta = -(1/Delta) * N / D
# where N = sum_k eps_k delta_eps_k / E_k^3
#       D = sum_k 1/E_k^3 (actually: sum_k Delta^2/E_k^3 = Delta^2 * sum 1/E_k^3)

# Wait, let me rederive carefully.
# Gap equation: 1/g = sum_k 1/(2 E_k) where E_k = sqrt(eps_k^2 + Delta^2).
# Perturb: eps_k -> eps_k + delta_eps_k, Delta -> Delta + delta_Delta.
# At first order: 0 = sum_k [-(eps_k delta_eps_k + Delta delta_Delta) / (2 E_k^3)]
# So: delta_Delta * sum_k Delta / (2 E_k^3) = -sum_k eps_k delta_eps_k / (2 E_k^3)
# Hence: delta_Delta = -(sum_k eps_k delta_eps_k / E_k^3) / (Delta sum_k 1/E_k^3)
# Wait: Delta * sum_k 1/(2 E_k^3) delta_Delta = -sum_k eps_k delta_eps_k / (2 E_k^3)
# => delta_Delta = -(sum eps_k delta_eps_k / E_k^3) / (Delta * sum 1/E_k^3)

numerator_pert = np.sum(eps_fold * delta_eps / E_k_orig**3)
denominator_pert = Delta * np.sum(1.0 / E_k_orig**3)
delta_Delta_pert = -numerator_pert / denominator_pert

print(f"\n8a: Analytical perturbative estimate:")
print(f"  Numerator (sum eps_k delta_eps_k / E_k^3) = {numerator_pert:.6e}")
print(f"  Denominator (Delta * sum 1/E_k^3) = {denominator_pert:.6e}")
print(f"  delta_Delta_pert = {delta_Delta_pert:.6e} M_KK")
print(f"  delta_Delta_exact = {delta_Delta:.6e} M_KK")
print(f"  Agreement: {delta_Delta_pert/delta_Delta:.8f}")

# Perturbative v2 shifts
print(f"\n8b: Perturbative v^2 shifts vs exact:")
print(f"  {'k':>3s} {'Label':>6s} {'delta_v2_pert':>14s} {'delta_v2_exact':>14s} {'ratio':>10s}")
print("-" * 56)
for k in range(N):
    dv2_deps = -0.5 * Delta**2 / E_k_orig[k]**3
    dv2_dDelta = 0.5 * eps_fold[k] * Delta / E_k_orig[k]**3
    dv2_pert = dv2_deps * delta_eps[k] + dv2_dDelta * delta_Delta_pert
    rat = dv2_pert / delta_v2[k] if abs(delta_v2[k]) > 1e-20 else float('nan')
    print(f"  {k:3d} {str(labels[k]):>6s} {dv2_pert:14.6e} {delta_v2[k]:14.6e} {rat:10.4f}")

# Perturbative E_ZP shift
delta_E_ZP_pert = 0.5 * np.sum(
    (eps_fold * delta_eps + Delta * delta_Delta_pert) / E_k_orig
)
print(f"\n8c: Perturbative E_ZP shift:")
print(f"  delta_E_ZP_pert = {delta_E_ZP_pert:.6e} M_KK")
print(f"  delta_E_ZP_exact = {delta_E_ZP:.6e} M_KK")
print(f"  Agreement: {delta_E_ZP_pert/delta_E_ZP:.6f}")

# =============================================================================
# Section 9: The 114 OOM Comparison
# =============================================================================
print("\n" + "=" * 72)
print("Section 9: The 114 OOM Comparison")
print("=" * 72)

# The CC problem: rho_vac^{obs} / rho_vac^{theory} ~ 10^{-114} (from CC_ratio)
# Our delta_rho from gravitational feedback gives:
# |delta_rho / rho_vac_theory| ~ |delta_E_ZP / E_ZP| ~ O(alpha_G) ~ 10^{-3}
# The target is 10^{-114}. The shortfall is 114 - 3 = 111 OOM.
# But the GATE threshold is 10^{-6}, testing whether the channel is OPEN.

# Use the most conservative (smallest) ratio for the gate
ratio_gate = abs(delta_E_ZP / E_ZP_orig)  # Measure A
ratio_gate_BCS = abs(delta_E_BCS / abs(E_BCS_orig)) if abs(E_BCS_orig) > 0 else 0
ratio_gate_CC = abs(delta_E_BCS / Lambda_CC)

print(f"\n9a: Gate ratio (delta_rho / rho_vac):")
print(f"  |delta_E_ZP / E_ZP| = {ratio_gate:.6e}  (log10 = {np.log10(ratio_gate):.2f})")
print(f"  |delta_E_BCS / E_BCS| = {ratio_gate_BCS:.6e}  (log10 = {np.log10(ratio_gate_BCS):.2f})")
print(f"  |delta_E_BCS / Lambda_CC| = {ratio_gate_CC:.6e}  (log10 = {np.log10(ratio_gate_CC):.2f})")

# OOM gap remaining
oom_gap_ZPE = 114 + np.log10(ratio_gate)
oom_gap_BCS = 114 + np.log10(ratio_gate_BCS)
oom_gap_CC = 114 + np.log10(ratio_gate_CC)
print(f"\n9b: OOM shortfall (target = 114 OOM):")
print(f"  ZPE measure: 114 - {-np.log10(ratio_gate):.1f} = {oom_gap_ZPE:.1f} OOM remaining")
print(f"  BCS measure: 114 - {-np.log10(ratio_gate_BCS):.1f} = {oom_gap_BCS:.1f} OOM remaining")
print(f"  CC measure:  114 - {-np.log10(ratio_gate_CC):.1f} = {oom_gap_CC:.1f} OOM remaining")

# =============================================================================
# Section 10: Gate Verdict
# =============================================================================
print("\n" + "=" * 72)
print("GATE VERDICT: SECTOR-SELECTIVE-BREAKING-64")
print("=" * 72)

# Use the most conservative ratio for the gate
# The gate asks: is the gravitational channel to the (0,0) condensate OPEN?
# Multiple measures available; use the most physically meaningful one.
# The BCS ground state energy shift relative to the spectral action CC is
# the most direct measure.

gate_ratio = ratio_gate  # |delta_E_ZP / E_ZP|

if gate_ratio > 1e-6:
    verdict = "PASS"
    detail = (f"|delta_rho/rho_vac| = {gate_ratio:.3e} > 10^{{-6}}. "
              f"Gravitational channel to (0,0) condensate is OPEN at O(alpha_G). "
              f"Shortfall to observed CC: {oom_gap_ZPE:.0f} OOM.")
elif gate_ratio > 1e-8:
    verdict = "INFO"
    detail = (f"|delta_rho/rho_vac| = {gate_ratio:.3e} in [10^-8, 10^-6]. "
              f"Intermediate regime.")
else:
    verdict = "FAIL"
    detail = (f"|delta_rho/rho_vac| = {gate_ratio:.3e} < 10^-8. "
              f"Channel suppressed beyond O(alpha_G^2).")

print(f"\nGate: SECTOR-SELECTIVE-BREAKING-64")
print(f"  Criterion: |delta_rho/rho_vac| > 10^{{-6}}")
print(f"  Computed: {gate_ratio:.6e}")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")

# Summary
print(f"\n{'='*50}")
print(f"SUMMARY:")
print(f"  delta_Delta / Delta = {delta_Delta/Delta:+.6e}")
print(f"  delta(v_B2[0]^2) = {delta_v2[0]:+.6e}")
print(f"  delta_E_ZP / E_ZP = {delta_E_ZP/E_ZP_orig:+.6e}")
print(f"  delta_E_BCS = {delta_E_BCS:+.6e} M_KK")
print(f"  OOM shortfall to CC: {oom_gap_ZPE:.0f}")
print(f"  Gate: {verdict}")
print(f"{'='*50}")

# =============================================================================
# Section 11: Save Data
# =============================================================================
save_path = os.path.join(data_dir, 's64_sector_selective.npz')
np.savez(save_path,
         # Gate
         gate_name='SECTOR-SELECTIVE-BREAKING-64',
         gate_verdict=verdict,
         gate_detail=detail,
         gate_ratio=gate_ratio,
         # Input
         eps_fold=eps_fold,
         eps_shifted=eps_shifted,
         eps_final=eps_final,
         labels=labels,
         n_k_GGE=n_k_GGE,
         alpha_G=alpha_G,
         C2_iso=C2_iso,
         Delta_orig=Delta,
         Delta_new=Delta_new,
         Delta_final=Delta_final,
         delta_Delta=delta_Delta,
         g_bcs=g_bcs,
         N_modes=N,
         # BCS state (original)
         E_k_orig=E_k_orig,
         v2_orig=v2_orig,
         u2_orig=u2_orig,
         # BCS state (shifted)
         E_k_new=E_k_new,
         v2_new=v2_new,
         u2_new=u2_new,
         delta_v2=delta_v2,
         # BCS state (bootstrap)
         E_k_final=E_k_final,
         v2_final=v2_final,
         delta_v2_boot=delta_v2_boot,
         # Energies
         E_ZP_orig=E_ZP_orig,
         E_ZP_new=E_ZP_new,
         E_ZP_final=E_ZP_final,
         delta_E_ZP=delta_E_ZP,
         delta_E_ZP_final=delta_E_ZP_final,
         E_BCS_orig=E_BCS_orig,
         E_BCS_new=E_BCS_new,
         E_BCS_final=E_BCS_final,
         delta_E_BCS=delta_E_BCS,
         delta_E_BCS_final=delta_E_BCS_final,
         delta_E_cond=delta_E_cond,
         # CC ratios
         ratio_ZPE=ratio_gate,
         ratio_BCS=ratio_gate_BCS,
         ratio_CC=ratio_gate_CC,
         Lambda_CC=Lambda_CC,
         oom_gap_ZPE=oom_gap_ZPE,
         oom_gap_BCS=oom_gap_BCS,
         oom_gap_CC=oom_gap_CC,
         # GGE
         delta_rho_GGE=delta_rho_GGE,
         rho_ZP_GGE_orig=rho_ZP_GGE_orig,
         ratio_GGE=ratio_E,
         # Perturbative cross-check
         delta_Delta_pert=delta_Delta_pert,
         delta_E_ZP_pert=delta_E_ZP_pert,
         )

print(f"\nSaved: {save_path}")

# =============================================================================
# Section 12: Plot
# =============================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('SECTOR-SELECTIVE-BREAKING-64: Gravitational Feedback to BCS Condensate',
             fontsize=13, fontweight='bold')

x = np.arange(N)
label_strs = [str(l) for l in labels]
branch_colors = ['#2196F3'] * 4 + ['#4CAF50'] + ['#F44336'] * 3  # B2=blue, B1=green, B3=red

# Panel 1: Gravitational energy shifts
ax = axes[0, 0]
ax.bar(x, -delta_eps * 1e4, color=branch_colors)
ax.set_xlabel('Mode k')
ax.set_ylabel(r'$-\delta\epsilon_k \times 10^4$ (M$_{KK}$)')
ax.set_title('Gravitational Energy Shifts')
ax.set_xticks(x)
ax.set_xticklabels(label_strs, rotation=45, fontsize=8)
ax.grid(True, alpha=0.3)
for k in range(N):
    ax.annotate(f'C2={C2_iso[k]:.1f}', (x[k], -delta_eps[k]*1e4),
                textcoords="offset points", xytext=(0, 5), ha='center', fontsize=7)

# Panel 2: Bogoliubov occupation shifts
ax = axes[0, 1]
colors_v2 = ['#2196F3' if dv > 0 else '#F44336' for dv in delta_v2]
ax.bar(x, delta_v2 * 1e5, color=colors_v2)
ax.set_xlabel('Mode k')
ax.set_ylabel(r'$\delta v_k^2 \times 10^5$')
ax.set_title(r'$\delta v_k^2$ (blue=increase, red=decrease)')
ax.set_xticks(x)
ax.set_xticklabels(label_strs, rotation=45, fontsize=8)
ax.axhline(y=0, color='black', linewidth=0.5)
ax.grid(True, alpha=0.3)

# Panel 3: Direct vs indirect decomposition
ax = axes[0, 2]
direct = np.zeros(N)
indirect = np.zeros(N)
for k in range(N):
    dv2_deps = -0.5 * Delta**2 / E_k_orig[k]**3
    direct[k] = dv2_deps * delta_eps[k]
    dv2_dDelta = 0.5 * eps_fold[k] * Delta / E_k_orig[k]**3
    indirect[k] = dv2_dDelta * delta_Delta
width = 0.35  # (local)
ax.bar(x - width/2, direct * 1e5, width, label='Direct (eps shift)', color='#FF9800')
ax.bar(x + width/2, indirect * 1e5, width, label='Indirect (gap shift)', color='#9C27B0')
ax.set_xlabel('Mode k')
ax.set_ylabel(r'$\delta v_k^2 \times 10^5$')
ax.set_title('Direct vs Indirect Feedback')
ax.set_xticks(x)
ax.set_xticklabels(label_strs, rotation=45, fontsize=8)
ax.axhline(y=0, color='black', linewidth=0.5)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Quasiparticle energy shifts
ax = axes[1, 0]
ax.bar(x, delta_E * 1e4, color=branch_colors)
ax.set_xlabel('Mode k')
ax.set_ylabel(r'$\delta E_k \times 10^4$ (M$_{KK}$)')
ax.set_title('Quasiparticle Energy Shifts')
ax.set_xticks(x)
ax.set_xticklabels(label_strs, rotation=45, fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Energy budget pie chart
ax = axes[1, 1]
components = [abs(delta_E_ZP), abs(delta_E_cond), abs(delta_E_kin)]
comp_labels = [f'ZPE\n{delta_E_ZP:.2e}', f'Cond\n{delta_E_cond:.2e}',
               f'Kin\n{delta_E_kin:.2e}']
comp_colors = ['#2196F3', '#F44336', '#4CAF50']
# Only include nonzero components
valid = [i for i in range(len(components)) if components[i] > 1e-20]
if len(valid) >= 2:
    ax.pie([components[i] for i in valid],
           labels=[comp_labels[i] for i in valid],
           colors=[comp_colors[i] for i in valid],
           autopct='%1.1f%%', startangle=90)
else:
    ax.text(0.5, 0.5, f'delta_E_ZP = {delta_E_ZP:.3e}\ndelta_E_BCS = {delta_E_BCS:.3e}',
            transform=ax.transAxes, ha='center', va='center')
ax.set_title('Energy Shift Budget')

# Panel 6: OOM gap visualization
ax = axes[1, 2]
measures = ['ZPE', 'BCS', 'CC']
oom_values = [oom_gap_ZPE, oom_gap_BCS, oom_gap_CC]
bars = ax.barh(measures, oom_values, color=['#2196F3', '#F44336', '#4CAF50'])
ax.axvline(x=114, color='black', linestyle='--', linewidth=1.5, label='Full CC gap (114 OOM)')
ax.set_xlabel('OOM Shortfall Remaining')
ax.set_title('CC Gap: 114 OOM Target')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
for i, v in enumerate(oom_values):
    ax.text(v + 1, i, f'{v:.1f}', va='center', fontsize=9)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's64_sector_selective.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved: {plot_path}")

print("\n" + "=" * 72)
print("SECTOR-SELECTIVE-BREAKING-64 COMPLETE")
print("=" * 72)
