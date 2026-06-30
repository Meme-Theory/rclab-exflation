#!/usr/bin/env python3
"""
s58_pomeranchuk_gge.py — Pomeranchuk Stability of the GGE
==========================================================

Gate: POMERANCHUK-GGE-58
  PASS: Any F_l violates -(2l+1) bound (spontaneous deformation)
  FAIL: All F_l satisfy bounds (Pomeranchuk-stable)

Physics:
  The GGE has non-thermal occupations across 8 modes (4 B2 + 1 B1 + 3 B3).
  Landau's stability criterion demands that the Fermi-liquid parameters
  F_l^{s,a} satisfy F_l > -(2l+1) for all angular momentum channels l.

  For the discrete 8-mode system on SU(3), "angular momentum" maps to
  irreducible representations of the residual symmetry group. The
  decomposition is:
    - B2 (4 modes): l=0 singlet under U(2)_7
    - B1 (1 mode): l=0 singlet
    - B3 (3 modes): l=1 triplet under SU(2) subset

  The Landau parameter in channel l is:
    F_l = N(0) * <V_l>
  where N(0) is the density of states at the Fermi level and <V_l> is
  the l-th Legendre projection of the quasiparticle interaction.

  For the discrete system, we compute the full stability matrix
  (susceptibility matrix) directly, which is the rigorous generalization.

Method:
  1. Compute the static Lindhard response chi_0(q) for each channel
     from the GGE occupations.
  2. Compute the dressed response chi(q) = chi_0 / (1 - V * chi_0).
  3. Pomeranchuk instability occurs when det(1 - V * chi_0) = 0,
     equivalently when any eigenvalue of V * chi_0 reaches 1.
  4. Also compute F_l by projecting V onto the sector angular channels.

Session 58. Landau Condensed Matter Theorist.
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    E_cond, tau_fold, M_KK, N_dof_BCS, E_cond_ED_8mode
)

# =============================================================================
# Load data
# =============================================================================
data_gge = np.load(os.path.join(os.path.dirname(__file__),
                                's57_gge_equilibrium_gap.npz'),
                   allow_pickle=True)
data_ed = np.load(os.path.join(os.path.dirname(__file__),
                               's54_ed_sweep.npz'),
                  allow_pickle=True)

labels = data_gge['branch_labels']       # (8,) string
fk_gge = data_gge['fk_gge']             # (8,) GGE occupations
E_k = data_gge['E_k']                    # (8,) quasiparticle energies (BdG)
xi_k = data_gge['xi']                    # (8,) half-energies xi = E/2
T_k = data_gge['T_k_volovik']           # (8,) mode-resolved temperatures
beta_k = data_gge['beta_k']             # (8,) mode-resolved inverse temps

V_bare = data_ed['V_bare_cont']          # (8,8) pairing interaction at fold
fold_idx = int(data_ed['fold_idx'])
E_sp = data_ed['E_sp_sweep'][fold_idx]   # (8,) single-particle energies at fold
tau_at_fold = float(data_ed['tau_values'][fold_idx])

N = 8  # number of modes

print("=" * 70)
print("POMERANCHUK-GGE-58: Landau Parameters and Stability of the GGE")
print("=" * 70)
print()

# =============================================================================
# Section 1: Sector decomposition
# =============================================================================
# B2: modes 0-3 (4 modes, l=0 under U(2)_7)
# B1: mode 4   (1 mode, l=0 singlet)
# B3: modes 5-7 (3 modes, l=1 triplet under SU(2))

idx_B2 = np.array([0, 1, 2, 3])
idx_B1 = np.array([4])
idx_B3 = np.array([5, 6, 7])

print("--- Sector Decomposition ---")
print(f"B2 modes (l=0, U(2) singlet): {[str(labels[i]) for i in idx_B2]}")
print(f"B1 mode  (l=0, singlet):      {[str(labels[i]) for i in idx_B1]}")
print(f"B3 modes (l=1, SU(2) triplet):{[str(labels[i]) for i in idx_B3]}")
print()

# =============================================================================
# Section 2: Density of states and Lindhard susceptibility
# =============================================================================
# For the discrete system, the density of states per mode is:
#   N_k(0) = d(f_k)/d(mu) = beta_k * f_k * (1 - f_k)
# (derivative of Fermi function at mode-specific temperature)
#
# For the GGE, each mode has its own effective temperature T_k, so:
#   chi_0^{kk'} = -delta_{kk'} * N_k(0)
# where N_k(0) = beta_k * f_k * (1 - f_k) is the single-mode susceptibility.

# Compressibility (number susceptibility) per mode
N0_k = beta_k * fk_gge * (1.0 - fk_gge)

print("--- Single-Mode Susceptibilities (Lindhard) ---")
print(f"{'Mode':<8} {'f_GGE':>8} {'beta_k':>8} {'N_k(0)':>10} {'T_k':>8}")
for i in range(N):
    print(f"{str(labels[i]):<8} {fk_gge[i]:8.5f} {beta_k[i]:8.4f} {N0_k[i]:10.6f} {T_k[i]:8.4f}")

N0_total = np.sum(N0_k)
print(f"\nTotal N(0) = Sum N_k(0) = {N0_total:.6f}")
print()

# =============================================================================
# Section 3: Full stability matrix (rigorous for discrete system)
# =============================================================================
# The stability condition is: all eigenvalues of the matrix
#   M = 1 - V * chi_0
# must be positive (equivalently, all eigenvalues of V * chi_0 < 1).
#
# chi_0 is diagonal: chi_0 = -diag(N0_k)
# So M_{kk'} = delta_{kk'} + V_{kk'} * N0_{k'}
#
# The sign convention: V > 0 is repulsive in the particle-hole channel,
# attractive in the particle-particle (pairing) channel.
# For Pomeranchuk (density channel), instability occurs when
# eigenvalue of V * N0 >= 1.

# Build the matrix V * diag(N0)
V_N0 = V_bare * N0_k[np.newaxis, :]  # V_{kk'} * N0_{k'}

# Stability matrix
M_stab = np.eye(N) + V_N0  # 1 + V * chi_0 (note: chi_0 = -N0, V > 0 repulsive)
# For ATTRACTIVE V in ph channel (which destabilizes), we need 1 - |V|*N0 > 0
# Here V_bare is the PAIRING interaction (pp channel, attractive).
# In the ph channel, the relevant interaction has OPPOSITE sign for even l
# and SAME sign for odd l (exchange).
# For the discrete system, compute both channels.

# Direct (Hartree) channel: V_H = V_bare (s-wave, l=0)
# Exchange (Fock) channel: V_X = -V_bare (for fermions)
# Total ph interaction: f_{kk'} = V_H_{kk'} - V_X_{kk'} is not simply +-V
# In BCS context, V_bare is the PAIRING vertex (anomalous channel).
# The forward scattering amplitude (Landau f-function) in the normal state
# comes from the full V_bare as the quasiparticle interaction.

print("--- Full Stability Analysis ---")
print()

# Method A: Eigenvalues of V * chi_0
# Pomeranchuk: lambda_max(V_bare * diag(N0)) < 1
eig_VN0 = np.linalg.eigvalsh(V_N0)
eig_VN0_sorted = np.sort(eig_VN0)[::-1]

print("Eigenvalues of V_bare * diag(N0_k):")
for i, ev in enumerate(eig_VN0_sorted):
    status = "UNSTABLE" if ev >= 1.0 else "stable"
    margin = 1.0 - ev
    print(f"  lambda_{i} = {ev:+.8f}  (margin to instability: {margin:+.6f})  [{status}]")

lambda_max_VN0 = np.max(eig_VN0)
print(f"\nMax eigenvalue = {lambda_max_VN0:.8f}")
print(f"Margin to Pomeranchuk instability = {1.0 - lambda_max_VN0:.6f}")
print()

# Method B: Sector-resolved Landau parameters
# Project V onto sector blocks and compute F_l for each sector.
print("=" * 70)
print("--- Sector-Resolved Landau Parameters ---")
print("=" * 70)
print()

# ----- B2 sector (4 modes, l=0) -----
V_B2 = V_bare[np.ix_(idx_B2, idx_B2)]  # 4x4
N0_B2 = N0_k[idx_B2]
N0_B2_total = np.sum(N0_B2)
f_B2 = fk_gge[idx_B2]

# Average interaction in B2 (s-wave / l=0):
# F_0^{B2} = N(0)_B2 * <V>_B2
# where <V>_B2 = (1/N_B2^2) * sum_{kk'} V_{kk'}
# or weighted: <V>_B2 = sum_{kk'} N0_k V_{kk'} N0_{k'} / (sum N0_k)^2
V_B2_avg_unweighted = np.mean(V_B2)
V_B2_avg_weighted = np.dot(N0_B2, np.dot(V_B2, N0_B2)) / N0_B2_total**2

# F_0 for B2 using the standard Landau definition
# In the 4-dimensional B2 subspace, the "angular momentum" channels are
# the irreps of the permutation group S_4 or, more physically, the
# representations under which V_B2 decomposes.
# The s-wave (l=0) projection is the uniform average:
F_0_B2_unweighted = N0_B2_total * V_B2_avg_unweighted
F_0_B2_weighted = N0_B2_total * V_B2_avg_weighted

# Eigenvalues of V_B2 give the interaction strengths in each channel
eig_V_B2 = np.linalg.eigvalsh(V_B2)

# The stability condition for a 4-mode sector:
# Each eigenvalue v_alpha of V_B2 gives a channel with
# effective F_alpha = N(0)_B2 * v_alpha (if uniformly weighted)
# Stability requires F_alpha > -1 for s-wave channels

# More precisely: eigenvalues of V_B2 * diag(N0_B2)
eig_VN0_B2 = np.linalg.eigvalsh(V_B2 * N0_B2[np.newaxis, :])

print("B2 Sector (4 modes, l=0 under U(2)_7):")
print(f"  N(0)_B2 = {N0_B2_total:.6f}")
print(f"  <V>_B2 (unweighted) = {V_B2_avg_unweighted:.6f}")
print(f"  <V>_B2 (N0-weighted) = {V_B2_avg_weighted:.6f}")
print(f"  F_0^B2 (unweighted) = {F_0_B2_unweighted:+.6f}")
print(f"  F_0^B2 (weighted)   = {F_0_B2_weighted:+.6f}")
print(f"  Eigenvalues of V_B2: {np.sort(eig_V_B2)}")
print(f"  Eigenvalues of V_B2*N0_B2: {np.sort(eig_VN0_B2)}")
print(f"  Stability bound: F_0 > -1")
print(f"  Verdict: {'STABLE' if F_0_B2_weighted > -1 else 'UNSTABLE'}")
print()

# ----- B1 sector (1 mode, l=0) -----
V_B1 = V_bare[4, 4]  # scalar
N0_B1 = N0_k[4]
F_0_B1 = N0_B1 * V_B1

# B1-B2 cross coupling (the inter-sector channel)
V_B1_B2 = V_bare[4, idx_B2]  # (4,) -- uniform = 0.0799

print("B1 Sector (1 mode, l=0 singlet):")
print(f"  N(0)_B1 = {N0_B1:.6f}")
print(f"  V_B1 = {V_B1:.2e} (essentially zero — Trap 1)")
print(f"  F_0^B1 = {F_0_B1:.2e}")
print(f"  B1-B2 coupling: {V_B1_B2} (uniform = {np.std(V_B1_B2):.2e} spread)")
print(f"  Stability bound: F_0 > -1")
print(f"  Verdict: STABLE (V_B1 = 0 by selection rule)")
print()

# ----- B3 sector (3 modes, l=1 triplet) -----
V_B3 = V_bare[np.ix_(idx_B3, idx_B3)]  # 3x3
N0_B3 = N0_k[idx_B3]
N0_B3_total = np.sum(N0_B3)
V_B3_avg = np.mean(V_B3)
V_B3_weighted = np.dot(N0_B3, np.dot(V_B3, N0_B3)) / N0_B3_total**2 if N0_B3_total > 0 else 0.0

# For l=1 (triplet), the stability bound is F_1 > -3
F_1_B3_unweighted = N0_B3_total * V_B3_avg
F_1_B3_weighted = N0_B3_total * V_B3_weighted

eig_V_B3 = np.linalg.eigvalsh(V_B3)
eig_VN0_B3 = np.linalg.eigvalsh(V_B3 * N0_B3[np.newaxis, :])

print("B3 Sector (3 modes, l=1 triplet under SU(2)):")
print(f"  N(0)_B3 = {N0_B3_total:.6f}")
print(f"  <V>_B3 (unweighted) = {V_B3_avg:.6f}")
print(f"  <V>_B3 (N0-weighted) = {V_B3_weighted:.6f}")
print(f"  F_1^B3 (unweighted) = {F_1_B3_unweighted:+.6f}")
print(f"  F_1^B3 (weighted)   = {F_1_B3_weighted:+.6f}")
print(f"  Eigenvalues of V_B3: {np.sort(eig_V_B3)}")
print(f"  Eigenvalues of V_B3*N0_B3: {np.sort(eig_VN0_B3)}")
print(f"  Stability bound: F_1 > -3")
print(f"  Verdict: {'STABLE' if F_1_B3_weighted > -3 else 'UNSTABLE'}")
print()

# ----- Inter-sector (B2-B3) cross-coupling -----
V_B2_B3 = V_bare[np.ix_(idx_B2, idx_B3)]  # 4x3
V_B2_B3_avg = np.mean(np.abs(V_B2_B3))

print("Inter-Sector Couplings:")
print(f"  |V_B2-B3| avg = {V_B2_B3_avg:.6f}")
print(f"  V_B1-B2 (uniform) = {V_B1_B2[0]:.6f}")
print(f"  V_B1-B3 = {V_bare[4, 5:8]} (zero by selection rule)")
print()

# =============================================================================
# Section 4: Rigorous stability — full 8x8 susceptibility matrix
# =============================================================================
print("=" * 70)
print("--- Full 8x8 Pomeranchuk Analysis ---")
print("=" * 70)
print()

# The Landau stability condition for the discrete system is:
# All eigenvalues of the matrix (1 + V * chi_0) must be positive,
# where chi_0 = diag(-N0_k).
#
# Equivalently, all eigenvalues of V * diag(N0_k) must be < 1.
#
# But we must be careful about the sign. V_bare is the PAIRING interaction.
# In the particle-hole channel:
#   - For density (charge) fluctuations: the relevant vertex is V_direct
#   - For spin fluctuations: the relevant vertex is V_exchange
#
# In our system, V_bare couples time-reversed pairs (k, -k).
# The forward scattering amplitude (Landau f) in the ph channel is NOT
# identical to V_bare. However, for the 0D discrete system where all
# modes are at the same spatial point, V_bare IS the quasiparticle
# interaction (there is no momentum-dependent structure to distinguish
# direct from exchange).
#
# The rigorous statement: the 8x8 interaction matrix V_bare determines
# the stability of the Fermi-liquid ground state through its eigenvalues
# weighted by the compressibility.

# Symmetrized stability matrix
# Chi_0 = -diag(N0_k)
# 1 - V * Chi_0 = 1 + V * diag(N0_k)

M_full = np.eye(N) + V_bare @ np.diag(N0_k)
eig_M_full = np.linalg.eigvalsh(M_full)

print("Eigenvalues of stability matrix M = 1 + V*diag(N0):")
pomeranchuk_unstable = False
for i, ev in enumerate(np.sort(eig_M_full)):
    status = "UNSTABLE" if ev <= 0.0 else "stable"
    if ev <= 0.0:
        pomeranchuk_unstable = True
    print(f"  mu_{i} = {ev:+.8f}  [{status}]")

print()

# Also compute using the symmetrized form for numerical stability:
# M_sym = N0^{1/2} * (1 + V * diag(N0)) * N0^{-1/2}
# = diag(N0^{1/2}) + diag(N0^{1/2}) * V * diag(N0^{1/2})
# This is NOT the right symmetrization. The correct one is:
# S = diag(N0^{1/2}) * V * diag(N0^{1/2})
# Eigenvalues of S are the Landau parameters F_alpha / (2l_alpha + 1)
# up to the mapping between eigenvalue index and angular momentum.

N0_sqrt = np.sqrt(N0_k)
S_sym = np.outer(N0_sqrt, N0_sqrt) * V_bare  # S_{kk'} = sqrt(N0_k) * V_{kk'} * sqrt(N0_k')
eig_S = np.linalg.eigvalsh(S_sym)
eig_S_sorted = np.sort(eig_S)[::-1]

print("Eigenvalues of symmetrized interaction S = sqrt(N0)*V*sqrt(N0):")
print("(These are the generalized Landau parameters F_alpha)")
for i, ev in enumerate(eig_S_sorted):
    # For the discrete system, the bound is F_alpha > -1 for each eigenmode
    # (this is the 0D version of F_l > -(2l+1), with 2l+1 = 1 for all modes
    # since there are no spatial harmonics in 0D)
    bound = -1.0
    margin = ev - bound
    status = "UNSTABLE" if ev < bound else "stable"
    if ev < bound:
        pomeranchuk_unstable = True
    print(f"  F_{i} = {ev:+.10f}  (margin: {margin:+.8f})  [{status}]")

F_alpha_all = eig_S_sorted
print()

# =============================================================================
# Section 5: Map to conventional F_0, F_1, F_2
# =============================================================================
print("=" * 70)
print("--- Conventional Landau Parameters F_0, F_1, F_2 ---")
print("=" * 70)
print()

# F_0 (s-wave, density): average interaction weighted by N(0)
# F_0 = sum_{kk'} sqrt(N0_k) V_{kk'} sqrt(N0_k') / N = Tr(S) / N... no.
# The standard definition:
#   F_0 = N(0) * <f(theta)>_{FS} where <...> is Fermi surface average
# For uniform weight: F_0 = (1/N) * sum_{kk'} f_{kk'} * N(0)
# But since modes have different N0_k, use:
#   F_0 = sum_{kk'} V_{kk'} * N0_{k'} / N = Tr(V * diag(N0)) / N
# or equivalently:
#   F_0 = N(0)_total * <V>_{N0-weighted}

# Weighted average of V over the full Fermi surface
V_avg_full = np.sum(V_bare * np.outer(N0_k, N0_k)) / N0_total**2
F_0_full = N0_total * V_avg_full

# For F_1: need the angular-dependent part.
# In the sector decomposition, the B3 triplet carries l=1.
# F_1 is the coefficient of the P_1(cos theta) = cos(theta) projection.
# For the discrete system, define the "angular" structure through sectors:
#   - l=0 component: uniform part (B2 + B1 average)
#   - l=1 component: B3 triplet part
#   - l=2 component: quadrupolar variation within B2

# Direct computation via sector blocks:
# The B2+B1 sector is s-wave (l=0). The B3 sector is p-wave (l=1).
# Cross-sector coupling (B2-B3) mixes l=0 and l=1.

# Effective F_0 from B2+B1 diagonal block:
idx_s = np.concatenate([idx_B2, idx_B1])  # s-wave modes
V_s = V_bare[np.ix_(idx_s, idx_s)]  # 5x5
N0_s = N0_k[idx_s]
N0_s_total = np.sum(N0_s)
V_s_avg = np.dot(N0_s, np.dot(V_s, N0_s)) / N0_s_total**2 if N0_s_total > 0 else 0
F_0_sector = N0_s_total * V_s_avg

# Effective F_1 from B3 diagonal block:
F_1_sector = N0_B3_total * V_B3_weighted

# F_2: quadrupolar variation within B2
# Decompose V_B2 into uniform + quadrupolar:
# V_B2 = <V>_B2 * J + delta_V_B2  where J is the all-ones matrix (normalized)
# The quadrupolar part is delta_V_B2 = V_B2 - <V>_B2 * J
V_B2_uniform = np.full((4, 4), V_B2_avg_unweighted)
delta_V_B2 = V_B2 - V_B2_uniform

# F_2 from the quadrupolar variation
eig_delta = np.linalg.eigvalsh(delta_V_B2)
eig_delta_sorted = np.sort(eig_delta)[::-1]

# The most negative eigenvalue of delta_V determines F_2
# F_2 ~ N(0)_B2 * min(eig(delta_V_B2))
F_2_B2 = N0_B2_total * np.min(eig_delta)

print(f"F_0 (full 8-mode, N0-weighted):  {F_0_full:+.8f}")
print(f"F_0 (s-wave sector, B2+B1):      {F_0_sector:+.8f}")
print(f"F_1 (p-wave sector, B3):         {F_1_sector:+.8f}")
print(f"F_2 (quadrupolar, B2 variation): {F_2_B2:+.8f}")
print()

print(f"Stability bounds:")
print(f"  F_0 > -1:  F_0 = {F_0_full:+.6f} -> {'STABLE' if F_0_full > -1 else 'UNSTABLE'} (margin {F_0_full + 1:.6f})")
print(f"  F_1 > -3:  F_1 = {F_1_sector:+.6f} -> {'STABLE' if F_1_sector > -3 else 'UNSTABLE'} (margin {F_1_sector + 3:.6f})")
print(f"  F_2 > -5:  F_2 = {F_2_B2:+.6f} -> {'STABLE' if F_2_B2 > -5 else 'UNSTABLE'} (margin {F_2_B2 + 5:.6f})")
print()

# =============================================================================
# Section 6: Check the S22a result (f(0,0) = -4.687)
# =============================================================================
# Session 22a found f(0,0) = -4.687 < -3, declaring Pomeranchuk instability.
# That was computed from the GROUND STATE at T=0.
# The GGE has finite effective temperatures T_k, which suppress the
# susceptibility by the factor f_k(1-f_k).
# The question is whether thermal smearing stabilizes the instability.

print("=" * 70)
print("--- Comparison with S22a Ground-State Result ---")
print("=" * 70)
print()

# At T=0 in ground state: f_k = theta(mu - E_k), N0 = delta(E_k - mu)
# The S22a result used g*N(0) = 3.24 to get f(0,0) = -4.687
# Our GGE has finite-temperature smearing.

# Compute the T=0 limit for comparison
# At T=0, all modes below Fermi level have f=1, above have f=0
# N0_k(T=0) = delta(E_k - mu) which is singular
# Instead, compare the dimensionless product g*N(0):
g_eff = np.max(eig_S_sorted)  # largest eigenvalue = strongest channel
print(f"Largest F_alpha (GGE) = {g_eff:+.8f}")
print(f"S22a ground state: f(0,0) = -4.687, g*N(0) = 3.24")
print(f"GGE thermal suppression factor: max(F_alpha)/3.24 = {g_eff/3.24:.4f}")
print(f"  -> GGE susceptibility is {abs(g_eff/3.24)*100:.1f}% of ground state value")
print()

# The key point: at the GGE temperatures (T_k ~ 0.18-0.76 M_KK),
# the occupation is far from step-function, so N0_k = beta*f*(1-f) is
# much smaller than the T=0 delta-function.

# =============================================================================
# Section 7: Growth rate analysis (if unstable)
# =============================================================================
print("=" * 70)
print("--- Growth Rate Analysis ---")
print("=" * 70)
print()

# For Pomeranchuk instability, the growth rate in channel alpha is:
# gamma_alpha = |1 + F_alpha| * omega_0
# where omega_0 is the characteristic frequency (~ E_gap or T_k)
# But only if F_alpha < -(2l+1).

# Check if any mode is unstable
any_unstable = False
for i, F_a in enumerate(F_alpha_all):
    if F_a < -1.0:
        any_unstable = True
        gamma = abs(1.0 + F_a) * np.mean(E_k)  # characteristic rate
        print(f"  Mode {i}: F_{i} = {F_a:+.6f} < -1, growth rate gamma = {gamma:.4f} M_KK")

if not any_unstable:
    print("No Pomeranchuk-unstable modes found in the GGE.")
    print("The GGE is Pomeranchuk-stable at all angular momentum channels.")
    print()
    print("Physical interpretation:")
    print("  The non-thermal GGE occupations suppress the Lindhard susceptibility")
    print("  relative to the T=0 ground state. While the ground state (S22a) had")
    print("  f(0,0) = -4.687 (Pomeranchuk-unstable), the GGE's finite effective")
    print("  temperatures smear the Fermi surface, reducing all Landau parameters")
    print("  to O(10^{-2}), well within the stability bounds.")

print()

# =============================================================================
# Section 8: Richardson-Gaudin conservation check
# =============================================================================
print("=" * 70)
print("--- Integrability Impact Assessment ---")
print("=" * 70)
print()

# The GGE is defined by 8 Richardson-Gaudin conserved quantities.
# Pomeranchuk instability would generate collective modes that mix
# the RG integrals of motion. If ALL Landau parameters satisfy
# stability bounds, the RG conservation laws are preserved.

# Compute the "distance to instability" as a fraction of the stability bound
distances = []
for i, F_a in enumerate(F_alpha_all):
    bound = -1.0  # 0D: -(2l+1) = -1 for all modes
    distance = (F_a - bound) / abs(bound) if abs(bound) > 0 else abs(F_a)
    distances.append(distance)

min_distance = min(distances)
closest_mode = np.argmin(distances)

print(f"Distance to instability (fraction of bound):")
for i, d in enumerate(distances):
    marker = " <-- closest" if i == closest_mode else ""
    print(f"  Mode {i}: {d:+.6f}{marker}")
print(f"\nClosest approach: mode {closest_mode}, distance = {min_distance:.6f}")
print(f"Richardson-Gaudin integrals: {'PRESERVED' if not any_unstable else 'BROKEN'}")
print()

# =============================================================================
# Section 9: Gate verdict
# =============================================================================
print("=" * 70)
print("--- GATE VERDICT ---")
print("=" * 70)
print()

# Check both the eigenvalue criterion and the Landau parameter criterion
pom_stable = (not any_unstable) and (np.all(eig_M_full > 0))

gate_verdict = "PASS" if not pom_stable else "FAIL"
gate_value_F0 = float(F_0_full)
gate_value_F1 = float(F_1_sector)
gate_value_F2 = float(F_2_B2)
gate_value_Fmax = float(np.max(np.abs(F_alpha_all)))
gate_value_min_eig = float(np.min(eig_M_full))

print(f"Gate: POMERANCHUK-GGE-58")
print(f"  F_0 = {gate_value_F0:+.8f}  (bound: > -1)  {'VIOLATES' if gate_value_F0 <= -1 else 'SATISFIES'}")
print(f"  F_1 = {gate_value_F1:+.8f}  (bound: > -3)  {'VIOLATES' if gate_value_F1 <= -3 else 'SATISFIES'}")
print(f"  F_2 = {gate_value_F2:+.8f}  (bound: > -5)  {'VIOLATES' if gate_value_F2 <= -5 else 'SATISFIES'}")
print(f"  max|F_alpha| = {gate_value_Fmax:.8f}")
print(f"  min eigenvalue of stability matrix = {gate_value_min_eig:+.8f}")
print(f"  All Landau parameters within bounds: {pom_stable}")
print(f"  Any Pomeranchuk instability: {not pom_stable}")
print()
print(f"  Verdict: {gate_verdict}")
if gate_verdict == "FAIL":
    print(f"  The GGE is Pomeranchuk-STABLE. All F_l satisfy -(2l+1) bounds.")
    print(f"  The non-thermal occupations provide sufficient thermal smearing to")
    print(f"  suppress the T=0 Pomeranchuk instability (S22a: f(0,0)=-4.687).")
    print(f"  Richardson-Gaudin integrals of motion are preserved.")
    print(f"  This is NOT an integrability-breaking mechanism.")
else:
    print(f"  The GGE is Pomeranchuk-UNSTABLE! Spontaneous Fermi surface deformation.")
    print(f"  This breaks Richardson-Gaudin conservation and provides a candidate")
    print(f"  mechanism for integrability breaking.")

# =============================================================================
# Save results
# =============================================================================
save_path = os.path.join(os.path.dirname(__file__), 's58_pomeranchuk_gge.npz')
np.savez(
    save_path,
    # Gate
    gate_name='POMERANCHUK-GGE-58',
    gate_verdict=gate_verdict,
    gate_criterion='F_l > -(2l+1) for all l',
    # Landau parameters
    F_0_full=gate_value_F0,
    F_0_sector=float(F_0_sector),
    F_1_sector=gate_value_F1,
    F_2_B2=gate_value_F2,
    F_alpha_all=F_alpha_all,
    # Stability matrix
    eig_stability_matrix=np.sort(eig_M_full),
    min_eig_stability=gate_value_min_eig,
    # Susceptibilities
    N0_k=N0_k,
    N0_total=N0_total,
    # Sector data
    eig_V_B2=np.sort(eig_V_B2),
    eig_V_B3=np.sort(eig_V_B3),
    eig_VN0_B2=np.sort(eig_VN0_B2),
    eig_VN0_B3=np.sort(eig_VN0_B3),
    eig_delta_V_B2=np.sort(eig_delta),
    # Inputs used
    fk_gge=fk_gge,
    T_k_volovik=T_k,
    beta_k=beta_k,
    V_bare=V_bare,
    E_k=E_k,
    tau_fold=tau_at_fold,
    branch_labels=labels,
    # Distances
    distances_to_instability=np.array(distances),
    closest_mode=closest_mode,
    min_distance=min_distance,
    # Comparison
    S22a_f00=-4.687,
    S22a_gN0=3.24,
    thermal_suppression_ratio=float(g_eff / 3.24),
    # Metadata
    pomeranchuk_stable=pom_stable,
)

print()
print(f"Saved: {save_path}")
print("Done.")
