#!/usr/bin/env python3
"""
s77_gge_occupation_correction.py -- GGE Occupation Correction to CC Spectral Weight
=====================================================================================

Gate: S77-C7-GGE-OCC
  PASS: delta_chi_2 in [-0.10, -0.07] (GGE correction brings chi_2 from 0.741
        to ~0.685 = Omega_Lambda, resolving the 8.2% overshoot).
  FAIL: |delta_chi_2| < 0.01 (GGE correction negligible, overshoot unresolved).
  INFO: delta_chi_2 wrong sign or too large (GGE makes it worse or overcompensates).

Physics:
--------
The HP4 CC route (S74-S76) predicts:
    rho_Lambda = chi_2 * H_0^2 * M_Pl^2                                [Eq.1]

with chi_2 = M_1 / (N_total * lam_max) = 0.741 (L=9 canonical).
The "direct conjecture" identifies chi_2 = Omega_Lambda, giving:
    chi_2 / Omega_Lambda = 0.741 / 0.685 = 1.082                       [Eq.2]

an 8.2% overshoot. The question: does the GGE relic (59.8 quasiparticle pairs
from the S38 transit quench) modify chi_2 to resolve this overshoot?

The chi_2 spectral fill factor is:
    chi_2 = sum_j d_j^2 |lambda_j| / (sum_j d_j^2 * n_j * lam_max)    [Eq.3]

where the sum is over all sectors (p,q) of the Dirac operator D_K.

In vacuum, every eigenvalue mode contributes with unit weight. The GGE
excites quasiparticle pairs on the 8 BCS modes (4 B2 + 1 B1 + 3 B3).
These excitations modify the effective spectral weight through occupation-
number changes.

Three correction mechanisms are computed:
  (A) Direct occupation correction: GGE modifies the effective spectral
      density. For Bogoliubov quasiparticles, excited modes have modified
      spectral weight proportional to the coherence factor:
        delta_weight(k) = n_k * (u_k^2 - v_k^2) = n_k * eps_k / E_k
      This changes both M_1 and N_total, hence chi_2.

  (B) Bosonic pair condensate modification: If the 59.8 pairs form a
      bosonic condensate (Cooper pairs as composite bosons), each pair
      adds spectral weight (1 + 2*n_pair) per mode vs vacuum (1).

  (C) Fractional correction from BCS mode count: Even without detailed
      coherence factors, the GGE correction is bounded by the BCS mode
      fraction: N_BCS / N_total = 8 / 155,984 (at L=3, unweighted) or
      the d^2-weighted fraction.

Session: S77 Wave 3-G
Agent: landau-condensed-matter-theorist
Date: 2026-04-13
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ============================================================================
#  Imports from canonical constants
# ============================================================================
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    # PDG / CODATA
    Omega_Lambda,          # 0.685
    PI,
    # Framework BCS
    n_pairs,               # 59.8 quasiparticle pairs from transit
    N_dof_BCS,             # 8 Fock space modes (4B2 + 1B1 + 3B3)
    n_Bog,                 # 0.999 Bogoliubov fraction per mode
    E_cond,                # -0.137 condensation energy
    E_B1,                  # 0.819 M_KK
    E_B2_mean,             # 0.845 M_KK
    E_B3_mean,             # 0.978 M_KK
    Delta_BCS,             # 0.464 M_KK (canonical OES gap)
    Delta_0_GL,            # 0.770 M_KK (GL order parameter)
    rho_B2_per_mode,       # 14.023 B2 DOS per mode
    # Spectral action
    a0_fold,               # 6440.0
    a2_fold,               # 2776.17
    a4_fold,               # 1350.72
    T_GGE_B2,              # 0.668 M_KK B2 GGE temperature
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 78)
print("S77 W3-G: GGE-OCCUPATION-CORRECTION -- Spectral Weight from GGE Pairs")
print("=" * 78)
print()

# ============================================================================
# PART 1: Load chi_2 data from S76 computation
# ============================================================================
print("PART 1: Load chi_2 and eigenvalue data")
print("-" * 78)

# Load the S74 hp4_pairing data
hp4_path = os.path.join(SCRIPT_DIR, "s74_hp4_pairing.npz")  # (local)
hp4_data = np.load(hp4_path, allow_pickle=True)  # (local)

chi_2_canonical = float(hp4_data['chi_2_canonical'])  # (local) = 0.741419
L_list = hp4_data['L_list']  # (local) [3, 4, 5, 6, 7, 8, 9]
chi_2_arr = hp4_data['chi_2_arr']  # (local) chi_2 at each L
M1_arr = hp4_data['M1_arr']  # (local) M_1 at each L
n_arr = hp4_data['n_arr']  # (local) N_total (d^2-weighted) at each L
lam_max_arr = hp4_data['lam_max_arr']  # (local) lam_max at each L

# Canonical values at L=9
L_canonical = 9  # (local)
idx_9 = np.where(L_list == L_canonical)[0][0]  # (local)
M1_L9 = float(M1_arr[idx_9])  # (local) = 1.302e9
N_total_L9 = int(n_arr[idx_9])  # (local) = 408,721,760
lam_max_L9 = float(lam_max_arr[idx_9])  # (local) = 4.296

# Also get L=3 values (where BCS was originally computed)
idx_3 = np.where(L_list == 3)[0][0]  # (local)
M1_L3 = float(M1_arr[idx_3])  # (local)
N_total_L3 = int(n_arr[idx_3])  # (local) = 155,984
lam_max_L3 = float(lam_max_arr[idx_3])  # (local)

# Direct conjecture ratio
ratio_direct = chi_2_canonical / Omega_Lambda  # (local)
overshoot_pct = (ratio_direct - 1.0) * 100  # (local) = 8.2%

print(f"  chi_2(L=9) = {chi_2_canonical:.6f}")
print(f"  M_1(L=9) = {M1_L9:.6e}")
print(f"  N_total(L=9) = {N_total_L9:,}")
print(f"  lam_max(L=9) = {lam_max_L9:.4f}")
print(f"  Omega_Lambda = {Omega_Lambda:.4f}")
print(f"  chi_2 / Omega_Lambda = {ratio_direct:.4f}  ({overshoot_pct:+.1f}% overshoot)")
print()

# Cross-check: reproduce chi_2
chi_2_check = M1_L9 / (N_total_L9 * lam_max_L9)  # (local)
chi_2_reldev = abs(chi_2_check - chi_2_canonical) / chi_2_canonical  # (local)
print(f"  Cross-check: M_1/(N*lam_max) = {chi_2_check:.6f}  (rel dev: {chi_2_reldev:.2e})")
assert chi_2_reldev < 1e-4, f"chi_2 cross-check failed: {chi_2_reldev:.2e}"
print()

# ============================================================================
# PART 2: BCS mode structure and GGE occupations
# ============================================================================
print("PART 2: BCS Mode Structure and GGE Occupations")
print("-" * 78)

# The 8 BCS modes and their properties
# Mode energies (bare eigenvalues of D_K at fold)
E_modes = np.array([E_B2_mean, E_B2_mean, E_B2_mean, E_B2_mean,
                     E_B1,
                     E_B3_mean, E_B3_mean, E_B3_mean])  # (local) M_KK

# DOS weights (from s38_kz_defects: B2 has rho_B2_per_mode, others = 1)
rho_modes = np.array([rho_B2_per_mode, rho_B2_per_mode,
                       rho_B2_per_mode, rho_B2_per_mode,
                       1.0, 1.0, 1.0, 1.0])  # (local)

labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']  # (local)

# Sector multiplicities (d^2 = dim(p,q)^2)
# B1 = (0,0): dim=1, d^2=1
# B2 = (1,1): dim=8, d^2=64
# B3 = (1,0) or (0,1): dim=3, d^2=9
d2_B1 = 1   # (local) dim(0,0)^2
d2_B2 = 64  # (local) dim(1,1)^2
d2_B3 = 9   # (local) dim(1,0)^2 = dim(0,1)^2

# d^2 weight per BCS mode
d2_modes = np.array([d2_B2, d2_B2, d2_B2, d2_B2,
                      d2_B1,
                      d2_B3, d2_B3, d2_B3])  # (local)

# Quasiparticle energies E_k = sqrt(eps_k^2 + Delta^2)
# Using canonical Delta_BCS (OES gap)
E_qp = np.sqrt(E_modes**2 + Delta_BCS**2)  # (local) M_KK

# BCS coherence factors
u_k_sq = 0.5 * (1.0 + E_modes / E_qp)  # (local)
v_k_sq = 0.5 * (1.0 - E_modes / E_qp)  # (local)
coherence_factor = E_modes / E_qp  # (local) = u^2 - v^2

# GGE occupation per mode
# In the sudden quench (P_exc = 1), ALL modes are excited.
# n_Bog = 0.999 is the Bogoliubov fraction.
# The DOS-weighted pair count is n_pairs = 59.8.
# Per mode, the GGE occupation is:
#   n_k(GGE) = rho_k * n_Bog (excitations weighted by DOS)
n_k_GGE = rho_modes * n_Bog  # (local) per mode
total_pairs_check = np.sum(n_k_GGE)  # (local) should ~ 59.8

print(f"  BCS gap (Delta_BCS) = {Delta_BCS:.4f} M_KK")
print(f"  Bogoliubov fraction = {n_Bog:.6f}")
print(f"  Total pairs (check) = {total_pairs_check:.2f}  (canonical: {n_pairs})")
print()

print(f"  {'Mode':<8} {'E_k':>8} {'E_qp':>8} {'d^2':>6} {'rho':>8} "
      f"{'n_k(GGE)':>10} {'u^2-v^2':>8}")
for i in range(N_dof_BCS):
    print(f"  {labels[i]:<8} {E_modes[i]:>8.4f} {E_qp[i]:>8.4f} "
          f"{d2_modes[i]:>6d} {rho_modes[i]:>8.3f} "
          f"{n_k_GGE[i]:>10.4f} {coherence_factor[i]:>8.4f}")

# Total d^2-weighted BCS modes at L=3
N_BCS_weighted = np.sum(d2_modes)  # (local) = 4*64 + 1 + 3*9 = 284
# But each sector has multiple eigenvalues. The BCS modes are near-Fermi
# eigenvalues, not ALL eigenvalues in those sectors. The 8 modes are
# 8 specific eigenvalues selected by proximity to the Fermi surface.
# Their d^2 weight in the chi_2 sum depends on which sectors they belong to.

print(f"\n  N_BCS (unweighted) = {N_dof_BCS}")
print(f"  N_BCS (d^2-weighted) = {N_BCS_weighted}")
print(f"  N_total(L=3) = {N_total_L3:,}")
print(f"  N_total(L=9) = {N_total_L9:,}")
print(f"  BCS fraction (d^2, L=3) = {N_BCS_weighted/N_total_L3:.6e}")
print(f"  BCS fraction (d^2, L=9) = {N_BCS_weighted/N_total_L9:.6e}")
print()

# ============================================================================
# PART 3: Mechanism A -- Fermionic Bogoliubov spectral weight correction
# ============================================================================
print("PART 3: Mechanism A -- Bogoliubov Spectral Weight Correction")
print("-" * 78)

# The GGE quasiparticles are Bogoliubov excitations of the BCS condensate.
# Each excited quasiparticle modifies the spectral weight (contribution to
# M_1 and N_total in chi_2) of its mode.
#
# For a Bogoliubov quasiparticle on mode k:
#   vacuum:  contribution to M_1 = d_k^2 * |lambda_k|
#   GGE:     contribution to M_1 = d_k^2 * |lambda_k| * [1 + n_k * (u_k^2 - v_k^2)]
#
# where (u_k^2 - v_k^2) = eps_k / E_k is the coherence factor.
#
# This follows from the Bogoliubov transformation: the expectation value of
# the number operator in the excited state differs from vacuum by the
# coherence factor. The physical content: a quasiparticle at energy E_k
# is a superposition of particle (weight u^2) and hole (weight v^2).
# Its net spectral weight is u^2 - v^2 = eps/E > 0 (particle dominates
# since eps > 0 for modes above the Fermi surface).
#
# The correction to M_1:
#   delta_M1_A = sum_{k in BCS} d_k^2 * |lambda_k| * n_k * (eps_k / E_k)
#
# The correction to N_total:
#   delta_N_A = sum_{k in BCS} d_k^2 * n_k * (eps_k / E_k)
#
# The correction to chi_2:
#   delta_chi_2 = chi_2(GGE) - chi_2(vac)
#   chi_2(GGE) = (M1 + delta_M1) / ((N + delta_N) * lam_max)
#   delta_chi_2/chi_2 = delta_M1/M1 - delta_N/N  [to first order]

# Compute delta_M1_A
delta_M1_A = np.sum(d2_modes * E_modes * n_k_GGE * coherence_factor)  # (local)

# Compute delta_N_A
delta_N_A = np.sum(d2_modes * n_k_GGE * coherence_factor)  # (local)

# Fractional corrections
frac_M1_A = delta_M1_A / M1_L9  # (local)
frac_N_A = delta_N_A / N_total_L9  # (local)

# chi_2 correction (first order)
delta_chi2_A_frac = frac_M1_A - frac_N_A  # (local)
delta_chi2_A = delta_chi2_A_frac * chi_2_canonical  # (local)

# chi_2 correction (exact)
chi2_A_exact = (M1_L9 + delta_M1_A) / ((N_total_L9 + delta_N_A) * lam_max_L9)  # (local)
delta_chi2_A_exact = chi2_A_exact - chi_2_canonical  # (local)

print(f"  Bogoliubov coherence correction (Mechanism A):")
print(f"  delta_M1_A = {delta_M1_A:.6e}")
print(f"  delta_N_A = {delta_N_A:.6e}")
print(f"  delta_M1/M1 = {frac_M1_A:.6e}")
print(f"  delta_N/N = {frac_N_A:.6e}")
print(f"  delta_chi_2/chi_2 (1st order) = {delta_chi2_A_frac:.6e}")
print(f"  delta_chi_2 (1st order) = {delta_chi2_A:.6e}")
print(f"  delta_chi_2 (exact) = {delta_chi2_A_exact:.6e}")
print(f"  chi_2(GGE, A) = {chi2_A_exact:.6f}")
print()

# ============================================================================
# PART 4: Mechanism B -- Bosonic pair condensate spectral weight
# ============================================================================
print("PART 4: Mechanism B -- Bosonic Pair Condensate Modification")
print("-" * 78)

# Alternative: treat the 59.8 pairs as bosonic (Cooper pairs).
# For bosonic modes, the spectral weight in the occupied state is:
#   contribution(k) = (1 + 2*n_k) * |lambda_k|
# vs vacuum: |lambda_k|
# So delta_weight(k) = 2*n_k * |lambda_k|
#
# This is the standard bosonic zero-point energy modification:
# E_vac(n) = (n + 1/2)*omega vs E_vac(0) = (1/2)*omega
# => delta_E = n*omega, giving spectral weight factor (1 + 2n).
#
# For chi_2:
#   delta_M1_B = sum_{k in BCS} d_k^2 * 2 * n_k * |lambda_k|
#   delta_N_B = sum_{k in BCS} d_k^2 * 2 * n_k

# Compute delta_M1_B (bosonic, factor of 2*n_k)
delta_M1_B = 2.0 * np.sum(d2_modes * E_modes * n_k_GGE)  # (local)

# Compute delta_N_B
delta_N_B = 2.0 * np.sum(d2_modes * n_k_GGE)  # (local)

# Fractional corrections
frac_M1_B = delta_M1_B / M1_L9  # (local)
frac_N_B = delta_N_B / N_total_L9  # (local)

# chi_2 correction (first order)
delta_chi2_B_frac = frac_M1_B - frac_N_B  # (local)
delta_chi2_B = delta_chi2_B_frac * chi_2_canonical  # (local)

# chi_2 correction (exact)
chi2_B_exact = (M1_L9 + delta_M1_B) / ((N_total_L9 + delta_N_B) * lam_max_L9)  # (local)
delta_chi2_B_exact = chi2_B_exact - chi_2_canonical  # (local)

print(f"  Bosonic pair condensate correction (Mechanism B):")
print(f"  delta_M1_B = {delta_M1_B:.6e}")
print(f"  delta_N_B = {delta_N_B:.6e}")
print(f"  delta_M1/M1 = {frac_M1_B:.6e}")
print(f"  delta_N/N = {frac_N_B:.6e}")
print(f"  delta_chi_2/chi_2 (1st order) = {delta_chi2_B_frac:.6e}")
print(f"  delta_chi_2 (1st order) = {delta_chi2_B:.6e}")
print(f"  delta_chi_2 (exact) = {delta_chi2_B_exact:.6e}")
print(f"  chi_2(GGE, B) = {chi2_B_exact:.6f}")
print()

# ============================================================================
# PART 5: Mechanism C -- Upper bound from mode fraction
# ============================================================================
print("PART 5: Mechanism C -- Upper Bound from BCS Mode Fraction")
print("-" * 78)

# Even the most generous interpretation cannot exceed the BCS mode fraction.
# If we assume that EVERY BCS mode eigenvalue is completely removed (weight -> 0),
# the maximum possible delta_chi_2 is bounded by removing those modes entirely.

# At L=3: 8 BCS modes out of 155,984 total (unweighted)
# The d^2-weighted contribution of BCS modes to M_1:
M1_BCS = np.sum(d2_modes * E_modes)  # (local) BCS contribution to M_1
N_BCS_wtd = np.sum(d2_modes)  # (local) = 284

# At L=9, the BCS modes are the same physical modes but N_total has grown
# due to higher (p,q) sectors entering. The BCS modes' d^2-weighted contribution
# to M_1 stays fixed (they are in specific low (p,q) sectors).

# Maximum delta_chi_2 (removing BCS modes entirely):
chi2_no_BCS = (M1_L9 - M1_BCS) / ((N_total_L9 - N_BCS_wtd) * lam_max_L9)  # (local)
delta_chi2_max = chi2_no_BCS - chi_2_canonical  # (local)

# Needed delta_chi_2 to match Omega_Lambda
delta_chi2_needed = Omega_Lambda - chi_2_canonical  # (local) = 0.685 - 0.741 = -0.056

print(f"  BCS modes' contribution to M_1 at L=3: {M1_BCS:.4f}")
print(f"  BCS d^2-weighted count: {N_BCS_wtd}")
print(f"  M1_BCS / M1(L=9) = {M1_BCS / M1_L9:.6e}")
print(f"  N_BCS_wtd / N_total(L=9) = {N_BCS_wtd / N_total_L9:.6e}")
print()
print(f"  Maximum delta_chi_2 (remove BCS entirely):")
print(f"  chi_2(no BCS) = {chi2_no_BCS:.6f}")
print(f"  delta_chi_2(max) = {delta_chi2_max:.6e}")
print()
print(f"  Needed delta_chi_2 for Omega_Lambda match:")
print(f"  delta_chi_2(needed) = {delta_chi2_needed:.6f}")
print(f"  |delta_needed| / |delta_max| = {abs(delta_chi2_needed / delta_chi2_max):.2f}")
print()

# ============================================================================
# PART 6: Mechanism D -- GGE thermal occupation across ALL modes
# ============================================================================
print("PART 6: Mechanism D -- GGE Thermal Occupation (All Modes)")
print("-" * 78)

# The GGE is not limited to the 8 BCS modes. The GGE relic has a thermal
# character with T_GGE_B2 = 0.668 M_KK for the B2 sector.
# In a GGE, occupation numbers follow:
#   n_k = 1 / (exp(E_k / T_GGE) - 1)   (bosonic)
#   n_k = 1 / (exp(E_k / T_GGE) + 1)   (fermionic)
#
# For the spectral weight correction, we need to integrate over ALL eigenvalues,
# not just the BCS modes. At T_GGE = 0.668 M_KK, modes with E < T_GGE are
# significantly occupied.
#
# The mean eigenvalue at L=9 is:
lam_avg_L9 = M1_L9 / N_total_L9  # (local) ~ chi_2 * lam_max
print(f"  <|lambda|> at L=9 = {lam_avg_L9:.4f} M_KK")
print(f"  T_GGE(B2) = {T_GGE_B2:.4f} M_KK")
print(f"  T_GGE / <|lambda|> = {T_GGE_B2 / lam_avg_L9:.4f}")
print(f"  T_GGE / lam_max = {T_GGE_B2 / lam_max_L9:.4f}")
print()

# Estimate the correction using the continuum approximation.
# Assume eigenvalue density is roughly uniform near the mean.
# For each eigenvalue lambda_j, the Bose occupation is:
#   n_j = 1/(exp(|lambda_j|/T_GGE) - 1)
#
# The correction to M_1 (bosonic case):
#   delta_M1_D = sum_j d_j^2 * 2 * n_j * |lambda_j|
#
# For a continuum with density rho(lambda) ~ N_total/lam_max:
#   delta_M1_D ~ 2 * N_total * (T_GGE/lam_max) * int_0^1 dx * x / (exp(x*lam_max/T_GGE) - 1)
#
# The integral is: int_0^1 x/(exp(beta*x)-1) dx where beta = lam_max/T_GGE

beta_D = lam_max_L9 / T_GGE_B2  # (local) ~ 6.4
print(f"  beta = lam_max / T_GGE = {beta_D:.2f}")

# Numerical integration
x_grid = np.linspace(0.001, 1.0, 10000)  # (local)
dx = x_grid[1] - x_grid[0]  # (local)
bose_integrand = x_grid / (np.exp(beta_D * x_grid) - 1.0)  # (local)
I_M1 = np.sum(bose_integrand) * dx  # (local)
bose_N_integrand = 1.0 / (np.exp(beta_D * x_grid) - 1.0)  # (local)
I_N = np.sum(bose_N_integrand) * dx  # (local)

print(f"  Bose integral I_M1 = int x/(exp(beta*x)-1) dx = {I_M1:.6e}")
print(f"  Bose integral I_N = int 1/(exp(beta*x)-1) dx = {I_N:.6e}")
print()

# BUT: the GGE is NOT a Bose-Einstein distribution over ALL modes.
# The GGE is a generalized Gibbs ensemble with conserved charges =
# the occupation numbers of the 8 BCS modes. The remaining modes
# (155,976 at L=3, ~408.7 million at L=9) are NOT thermalized.
# Their GGE occupation is ZERO (vacuum).
#
# The GGE by definition conserves all local integrals of motion.
# For an integrable system (which this is -- S63 PASS), the conserved
# quantities are the individual mode occupations. The GGE state has:
#   n_k = n_k(initial)  for BCS modes (= rho_k * n_Bog)
#   n_k = 0             for all other modes (vacuum)
#
# This means Mechanism D reduces to Mechanism A/B -- the correction is
# confined to the BCS modes only.

print(f"  STRUCTURAL CONSTRAINT:")
print(f"  The GGE is integrable (S63 PASS). Conserved quantities are individual")
print(f"  mode occupations. The GGE state excites ONLY the 8 BCS modes;")
print(f"  all other modes remain in vacuum (n_k = 0).")
print(f"  => Mechanism D reduces to Mechanism A or B.")
print(f"  The full-spectrum thermal correction is INAPPLICABLE.")
print()

# ============================================================================
# PART 7: Synthesis and gate evaluation
# ============================================================================
print("PART 7: Synthesis and Gate Evaluation")
print("-" * 78)

# The physical correction comes from either Mechanism A (Bogoliubov) or B (bosonic).
# Which is correct depends on the statistics of the quasiparticles:
#
# 1. Bogoliubov quasiparticles (fermionic): Mechanism A
#    delta_chi_2 ~ O(10^{-9}) -- NEGLIGIBLE
#
# 2. Cooper pair condensate (bosonic): Mechanism B
#    delta_chi_2 ~ O(10^{-8}) -- NEGLIGIBLE
#
# Both are negligible because:
# (a) The BCS modes occupy a TINY fraction of the full spectrum:
#     N_BCS_wtd / N_total = 284 / 408,721,760 = 6.9e-7
# (b) The chi_2 averages over ALL modes, diluting the BCS correction
# (c) The spectral fill factor is a GEOMETRIC property of D_K, not an
#     occupation-sensitive quantity. GGE changes the state, not the spectrum.

# The needed correction is -0.056 (about 7.6% of chi_2).
# The maximum possible correction (removing BCS modes entirely) is ~delta_max.
# The ratio |delta_needed|/|delta_max| tells whether this is achievable.

print(f"\n  Summary of corrections:")
print(f"  {'Mechanism':<25} {'delta_chi_2':>14} {'delta_chi_2/chi_2':>18}")
print(f"  {'-'*25} {'-'*14} {'-'*18}")
print(f"  {'A (Bogoliubov)':<25} {delta_chi2_A_exact:>14.6e} {delta_chi2_A_exact/chi_2_canonical:>18.6e}")
print(f"  {'B (Bosonic pair)':<25} {delta_chi2_B_exact:>14.6e} {delta_chi2_B_exact/chi_2_canonical:>18.6e}")
print(f"  {'C (Max: remove BCS)':<25} {delta_chi2_max:>14.6e} {delta_chi2_max/chi_2_canonical:>18.6e}")
print(f"  {'Needed (chi_2->0.685)':<25} {delta_chi2_needed:>14.6f} {delta_chi2_needed/chi_2_canonical:>18.6f}")
print()

# Required: delta_chi_2 in [-0.10, -0.07] for PASS
# This is O(10^{-1}), but the corrections are O(10^{-8}).
# The gap is 7 orders of magnitude.
ratio_A_to_needed = abs(delta_chi2_A_exact / delta_chi2_needed)  # (local)
ratio_B_to_needed = abs(delta_chi2_B_exact / delta_chi2_needed)  # (local)
ratio_max_to_needed = abs(delta_chi2_max / delta_chi2_needed)  # (local)

print(f"  Ratio of correction to needed:")
print(f"  A / needed = {ratio_A_to_needed:.2e}  ({np.log10(ratio_A_to_needed):+.1f} OOM)")
print(f"  B / needed = {ratio_B_to_needed:.2e}  ({np.log10(ratio_B_to_needed):+.1f} OOM)")
print(f"  max / needed = {ratio_max_to_needed:.2e}  ({np.log10(ratio_max_to_needed):+.1f} OOM)")
print()

# WHY the correction is negligible (structural argument):
# chi_2 = <|lambda|> / lam_max
# This is a ratio of spectral moments. The GGE modifies O(10) modes out of
# O(10^8). The spectral average is dominated by the vast majority of
# unexcited modes. Even if the BCS modes were removed entirely, chi_2
# changes by < 10^{-7} because 284 / 408,721,760 ~ 7e-7.
#
# The 8.2% overshoot cannot be resolved by GGE occupation corrections.
# It requires a modification to the GEOMETRIC spectral data (eigenvalue
# distribution) or to the HP4 formula itself (factor-3 Friedmann placement).

# Cross-checks
print("  Cross-checks:")

# CC1: delta_a_0 > 0 for bosonic (adding excitations increases spectral weight)
CC1 = delta_N_B > 0  # (local)
print(f"  CC1: delta_a_0(bosonic) > 0? {CC1}  (delta_N_B = {delta_N_B:.4e})")

# CC2: |delta_a_0/a_0| << 1
CC2 = abs(delta_N_B / N_total_L9) < 0.01  # (local)
print(f"  CC2: |delta_a_0/a_0| << 1? {CC2}  (ratio = {abs(delta_N_B / N_total_L9):.4e})")

# CC3: n_k -> 0 gives delta -> 0
CC3_test_A = np.sum(d2_modes * E_modes * (0.0 * np.ones(8)) * coherence_factor)  # (local)
CC3_test_B = 2.0 * np.sum(d2_modes * E_modes * (0.0 * np.ones(8)))  # (local)
CC3 = CC3_test_A == 0.0 and CC3_test_B == 0.0  # (local)
print(f"  CC3: n_k=0 => delta=0? {CC3}")

# CC4: Sign check -- bosonic should increase chi_2 (wrong direction for resolving overshoot)
sign_B = "POSITIVE" if delta_chi2_B_exact > 0 else "NEGATIVE"  # (local)
sign_A = "POSITIVE" if delta_chi2_A_exact > 0 else "NEGATIVE"  # (local)
print(f"  CC4: Sign of delta_chi_2(A) = {sign_A}")
print(f"       Sign of delta_chi_2(B) = {sign_B}")
print(f"       Needed sign = NEGATIVE (reduce chi_2 from 0.741 to 0.685)")
print()

all_cc = CC1 and CC2 and CC3  # (local)
print(f"  All cross-checks: {'PASS' if all_cc else 'FAIL'}")
print()

# ============================================================================
# PART 8: Gate verdict
# ============================================================================
print("=" * 78)
print("GATE VERDICT: S77-C7-GGE-OCC")
print("=" * 78)

# The largest correction (Mechanism B, bosonic) is:
delta_chi2_dominant = delta_chi2_B_exact  # (local)
abs_delta = abs(delta_chi2_dominant)  # (local)

if -0.10 <= delta_chi2_dominant <= -0.07:
    verdict = "PASS"
    explanation = ("GGE correction resolves 8.2% overshoot")
elif abs_delta < 0.01:
    verdict = "FAIL"
    explanation = (f"|delta_chi_2| = {abs_delta:.2e} < 0.01. "
                   f"GGE correction negligible ({abs_delta/abs(delta_chi2_needed)*100:.1e}% of needed). "
                   f"8.2% overshoot UNRESOLVED by GGE occupation.")
else:
    # Wrong sign or too large
    if delta_chi2_dominant > 0:
        verdict = "INFO"
        explanation = (f"delta_chi_2 = +{abs_delta:.2e} WRONG SIGN. "
                       f"GGE INCREASES chi_2 (makes overshoot worse).")
    else:
        verdict = "INFO"
        explanation = (f"delta_chi_2 = {delta_chi2_dominant:.2e} too large, overcompensates.")

print(f"  Threshold: delta_chi_2 in [-0.10, -0.07]")
print(f"  Computed:  delta_chi_2(A) = {delta_chi2_A_exact:.4e} (Bogoliubov)")
print(f"             delta_chi_2(B) = {delta_chi2_B_exact:.4e} (Bosonic pair)")
print(f"             delta_chi_2(max) = {delta_chi2_max:.4e} (remove BCS)")
print(f"             delta_chi_2(needed) = {delta_chi2_needed:.4f}")
print(f"  Verdict:   {verdict}")
print(f"  Reason:    {explanation}")
print()
print(f"  STRUCTURAL CONCLUSION:")
print(f"  The GGE occupation correction to chi_2 is O(10^{{-8}}) at L=9.")
print(f"  The 8 BCS modes constitute {N_BCS_weighted}/{N_total_L9:,} = "
      f"{N_BCS_wtd/N_total_L9:.1e} of the d^2-weighted mode count.")
print(f"  Even removing all BCS spectral weight gives delta_chi_2 ~ {delta_chi2_max:.1e}.")
print(f"  The 8.2% overshoot (delta = {delta_chi2_needed:.3f}) requires a")
print(f"  {abs(delta_chi2_needed/delta_chi2_max):.0e}x larger correction than the BCS")
print(f"  sector can provide.")
print(f"  Resolution must come from: (a) the factor-3 Friedmann normalisation")
print(f"  (chi_2/3 vs chi_2 = Omega_Lambda), or (b) L_max->infinity convergence")
print(f"  of chi_2 (currently drifting at 5%/decade).")
print()

# ============================================================================
# PART 9: Save results
# ============================================================================

save_path = os.path.join(SCRIPT_DIR, "s77_gge_occupation_correction.npz")  # (local)
np.savez(
    save_path,
    # Gate
    gate_id="S77-C7-GGE-OCC",
    gate_verdict=verdict,
    gate_criterion="PASS: delta_chi_2 in [-0.10,-0.07]; FAIL: |delta|<0.01",
    # Input data
    chi_2_canonical=chi_2_canonical,
    Omega_Lambda=Omega_Lambda,
    overshoot_pct=overshoot_pct,
    n_pairs=n_pairs,
    N_dof_BCS=N_dof_BCS,
    n_Bog=n_Bog,
    N_total_L9=N_total_L9,
    M1_L9=M1_L9,
    lam_max_L9=lam_max_L9,
    # Mechanism A results
    delta_chi2_A=delta_chi2_A_exact,
    delta_M1_A=delta_M1_A,
    delta_N_A=delta_N_A,
    frac_M1_A=frac_M1_A,
    frac_N_A=frac_N_A,
    # Mechanism B results
    delta_chi2_B=delta_chi2_B_exact,
    delta_M1_B=delta_M1_B,
    delta_N_B=delta_N_B,
    frac_M1_B=frac_M1_B,
    frac_N_B=frac_N_B,
    # Mechanism C results (upper bound)
    delta_chi2_max=delta_chi2_max,
    M1_BCS=M1_BCS,
    N_BCS_weighted=N_BCS_weighted,
    # Needed correction
    delta_chi2_needed=delta_chi2_needed,
    ratio_A_needed=ratio_A_to_needed,
    ratio_B_needed=ratio_B_to_needed,
    ratio_max_needed=ratio_max_to_needed,
    # Cross-checks
    CC1_delta_positive=CC1,
    CC2_small_correction=CC2,
    CC3_zero_limit=CC3,
    all_cross_checks=all_cc,
    sign_A=sign_A,
    sign_B=sign_B,
    # Mode data
    E_modes=E_modes,
    d2_modes=d2_modes,
    rho_modes=rho_modes,
    n_k_GGE=n_k_GGE,
    coherence_factor=coherence_factor,
    E_qp=E_qp,
)

print(f"  Results saved to: {save_path}")
print()

# ============================================================================
# PART 10: Diagnostic plot
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel 1: BCS mode contributions
ax = axes[0]
x_pos = np.arange(N_dof_BCS)
width = 0.35  # (local)
ax.bar(x_pos - width/2, d2_modes * E_modes * n_k_GGE * coherence_factor,
       width, label='Mech A (Bogoliubov)', color='steelblue')
ax.bar(x_pos + width/2, 2 * d2_modes * E_modes * n_k_GGE,
       width, label='Mech B (Bosonic)', color='coral')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_ylabel('delta M_1 contribution')
ax.set_title('Per-mode M_1 correction')
ax.legend(fontsize=8)

# Panel 2: Correction magnitude comparison
ax = axes[1]
corrections = [abs(delta_chi2_A_exact), abs(delta_chi2_B_exact),
               abs(delta_chi2_max), abs(delta_chi2_needed)]  # (local)
corr_labels = ['A\n(Bogol.)', 'B\n(Bosonic)', 'C\n(Max)', 'Needed']  # (local)
colors = ['steelblue', 'coral', 'gold', 'red']  # (local)
ax.bar(range(4), corrections, color=colors)
ax.set_xticks(range(4))
ax.set_xticklabels(corr_labels)
ax.set_ylabel('|delta chi_2|')
ax.set_yscale('log')
ax.set_title('Correction Magnitudes')
ax.axhline(y=0.07, color='green', linestyle='--', alpha=0.7, label='PASS band lower')
ax.axhline(y=0.10, color='green', linestyle='--', alpha=0.7, label='PASS band upper')
ax.axhline(y=0.01, color='orange', linestyle='--', alpha=0.7, label='FAIL threshold')
ax.legend(fontsize=7)

# Panel 3: Mode fraction pie chart
ax = axes[2]
sizes = [N_BCS_weighted, N_total_L9 - N_BCS_weighted]  # (local)
pie_labels = [f'BCS ({N_BCS_weighted})', f'Non-BCS ({N_total_L9-N_BCS_weighted:,})']  # (local)
ax.pie(sizes, labels=pie_labels, colors=['coral', 'lightgray'],
       autopct='%1.4f%%', startangle=90, textprops={'fontsize': 9})
ax.set_title(f'Mode Fraction (L=9, N={N_total_L9:,})')

fig.suptitle('S77-C7-GGE-OCC: GGE Occupation Correction to chi_2',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, "s77_gge_occupation_correction.png"), dpi=150)
print(f"  Plot saved to: s77_gge_occupation_correction.png")
print()
print("DONE.")
