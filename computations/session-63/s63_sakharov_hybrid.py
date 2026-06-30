#!/usr/bin/env python3
"""
SAKHAROV-HYBRID-63 — G_N from Coupled 45-Mode Spectrum
=======================================================

Computes Sakharov induced G_N from the full 45-mode coupled phonon spectrum
(S62 PHONON-DISPERSION-FULL-62) and compares to:
  1. Uncoupled sector-by-sector Sakharov integral
  2. S53 SAKHAROV-PHONON-53 (192 GL modes, G/G_obs = 1.04e4)
  3. S44/S45 Dirac-tower Sakharov (6440 PW modes, G/G_obs = 0.436)

Physics: Sakharov (1967) induced gravity via one-loop vacuum polarization.
Volovik (Paper 06, Eq.12; Paper 28, Eq.1): G^{-1} depends on species content
and UV cutoff. For N_f Weyl fermions + N_s scalars + N_v vectors at cutoff Lambda:

    G^{-1} = G_0^{-1} + (Lambda^2 / 12*pi) * (n_0 + n_{1/2} - 4*n_1)

The Sakharov integral form:
    1/(16*pi*G) = (1/48*pi^2) * sum_modes integral_0^Lambda dk k^2 / omega(k)

The coupled 45-mode spectrum hybridizes A-sector (36 Dirac eigenvalues),
B-sector (8 BCS quasiparticle branches), and C-sector (1 Leggett mode)
through inter-sector coupling V_AB, V_BC, V_AC. This computation measures
the hybridization correction to G_N.

Gate: SAKHAROV-HYBRID-63 (INFO)
Author: volovik-superfluid-universe-theorist
Session: S63
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from canonical_constants import (
    M_KK, M_Pl_reduced, M_Pl_unreduced,
    G_N, N_cells, a0_fold, a2_fold,
    PI
)

# =============================================================================
# STEP 0: Load input data
# =============================================================================
base_dir = os.path.dirname(os.path.abspath(__file__))
d62_disp = np.load(os.path.join(base_dir, "s62_phonon_dispersion_full.npz"),
                   allow_pickle=True)
d62_meissner = np.load(os.path.join(base_dir, "s62_meissner_gge.npz"),
                       allow_pickle=True)
d53 = np.load(os.path.join(base_dir, "s53_sakharov_phonon.npz"),
              allow_pickle=True)

# Coupled spectrum
omega_full = d62_disp['omega_full']      # (32, 45)
evecs_full = d62_disp['evecs_full']      # (32, 45, 45)
sector_weight = d62_disp['sector_weight']  # (32, 45, 3) -> [A, B, C]
k_eff = d62_disp['k_eff']                 # (32,) effective k
lambda_n = d62_disp['lambda_n']            # (32,) CG(24) eigenvalues

# Uncoupled sector spectra
omega_A = d62_disp['omega_A']              # (36,) k-independent Dirac eigenvalues
omega_B_uncoupled = d62_disp['omega_B_uncoupled']  # (32, 8)
omega_C_uncoupled = d62_disp['omega_C_uncoupled']  # (32, 1)

# Coupling matrices
V_AB = d62_disp['V_AB']                   # (36, 8)
V_BC = d62_disp['V_BC']                   # (8,)
V_AC = d62_disp['V_AC']                   # (36,)

# Meissner data (GGE)
D_s_GGE = float(d62_meissner['D_s_GGE'])
n_k_GGE = d62_meissner['n_k_GGE']          # (8,) occupation numbers

# S53 reference
ratio_G_S53 = float(d53['ratio_G_phonon'])  # 1.04e4
Lambda_S53 = float(d53['Lambda_phonon'])    # K_BZ = 0.716

N_k = omega_full.shape[0]   # 32
N_modes = omega_full.shape[1]  # 45
N_A = omega_A.shape[0]  # 36
N_B = omega_B_uncoupled.shape[1]  # 8
N_C = omega_C_uncoupled.shape[1]  # 1

print("=" * 72)
print("SAKHAROV-HYBRID-63: G_N from Coupled 45-Mode Spectrum")
print("=" * 72)
print()

# =============================================================================
# STEP 1: Spectrum summary
# =============================================================================
print("--- STEP 1: Coupled Spectrum Summary ---")
print(f"  N_k = {N_k} k-points (CG(24) cells)")
print(f"  N_modes = {N_modes} per cell ({N_A} A + {N_B} B + {N_C} C)")
print(f"  k_eff range: [{k_eff[0]:.4f}, {k_eff[-1]:.4f}] M_KK^{{-1}}")
print(f"  Lambda_UV = k_max = {k_eff[-1]:.6f} M_KK")
print()

# Count negative eigenvalues (instability modes from hybridization)
n_neg = np.sum(omega_full < 0)
neg_cells = np.where(np.any(omega_full < 0, axis=1))[0]
print(f"  Negative eigenvalues: {n_neg} (in cells {neg_cells})")
for c in neg_cells:
    neg_modes = np.where(omega_full[c] < 0)[0]
    for m in neg_modes:
        w = sector_weight[c, m]
        print(f"    Cell {c}: mode {m}, omega = {omega_full[c,m]:.4f}, "
              f"A={w[0]:.3f} B={w[1]:.3f} C={w[2]:.3f}")
print()

# Hybridization count
all_max_weight = np.max(sector_weight, axis=2)  # (32, 45)
n_hybrid_95 = np.sum(all_max_weight < 0.95)
n_hybrid_80 = np.sum(all_max_weight < 0.80)
n_hybrid_50 = np.sum(all_max_weight < 0.50)
print(f"  Hybridized modes (max sector weight < threshold):")
print(f"    < 0.95: {n_hybrid_95} / {N_k * N_modes}")
print(f"    < 0.80: {n_hybrid_80} / {N_k * N_modes}")
print(f"    < 0.50: {n_hybrid_50} / {N_k * N_modes}")
print()

# =============================================================================
# STEP 2: Sakharov integral — Coupled spectrum
# =============================================================================
# 1/(16*pi*G) = (1/(48*pi^2)) * sum_modes integral_0^Lambda dk k^2 / |omega(k)|
#
# For the discrete CG(24) spectrum, we have eigenvalues at 32 k-points.
# We use trapezoidal numerical integration over k_eff.
#
# Physical point: negative eigenvalues correspond to unstable modes.
# In Sakharov induction, the relevant quantity is |omega| (the excitation energy).
# We use |omega| for all modes (Volovik Paper 06: the integrand is k^2/E(k)
# where E is the excitation energy, always positive for stable excitations).

print("--- STEP 2: Sakharov Integral — Coupled Spectrum ---")
print()

Lambda_UV = k_eff[-1]  # 1.417 M_KK

# Method: numerical integration for each mode branch across k-points
I_coupled_per_mode = np.zeros(N_modes)
for m in range(N_modes):
    omega_branch = np.abs(omega_full[:, m])  # |omega| at each k
    # Avoid 0/0 at k=0: integrand = k^2/omega, at k=0 this is 0/omega(0) = 0
    integrand = np.zeros(N_k)
    for i in range(N_k):
        if k_eff[i] > 1e-10 and omega_branch[i] > 1e-10:
            integrand[i] = k_eff[i]**2 / omega_branch[i]
    I_coupled_per_mode[m] = np.trapezoid(integrand, k_eff)

I_coupled_total = np.sum(I_coupled_per_mode)

# 1/(16*pi*G) in M_KK^2
inv_16piG_coupled = I_coupled_total / (48 * PI**2)

# M_Pl_eff from coupled spectrum
M_Pl_eff_coupled = np.sqrt(2 * inv_16piG_coupled)  # M_KK units
M_Pl_eff_coupled_GeV = M_Pl_eff_coupled * M_KK

# Ratio to observed
ratio_G_coupled = (M_Pl_reduced / M_Pl_eff_coupled_GeV)**2

print(f"  Lambda_UV = {Lambda_UV:.6f} M_KK")
print(f"  I_coupled_total = {I_coupled_total:.6f}")
print(f"  1/(16*pi*G_coupled) = {inv_16piG_coupled:.6e} M_KK^2")
print(f"  M_Pl_eff(coupled) = {M_Pl_eff_coupled:.6e} M_KK = {M_Pl_eff_coupled_GeV:.4e} GeV")
print(f"  G_coupled / G_obs = {ratio_G_coupled:.4e}")
print(f"  |log10(G_coupled/G_obs)| = {abs(np.log10(ratio_G_coupled)):.4f} OOM")
print()

# =============================================================================
# STEP 3: Sakharov integral — Uncoupled spectrum (sector by sector)
# =============================================================================
print("--- STEP 3: Sakharov Integral — Uncoupled Spectrum ---")
print()

# A-sector: 36 modes, each at constant omega_A[i] across all k
# I_A[i] = integral_0^Lambda dk k^2 / omega_A[i] = Lambda^3 / (3 * omega_A[i])
I_A_per_mode = Lambda_UV**3 / (3.0 * omega_A)
I_A_total = np.sum(I_A_per_mode)

# B-sector: 8 modes, k-dependent omega_B(k)
# Numerical integration
I_B_per_mode = np.zeros(N_B)
for b in range(N_B):
    omega_b = omega_B_uncoupled[:, b]
    integrand = np.zeros(N_k)
    for i in range(N_k):
        if k_eff[i] > 1e-10 and omega_b[i] > 1e-10:
            integrand[i] = k_eff[i]**2 / omega_b[i]
    I_B_per_mode[b] = np.trapezoid(integrand, k_eff)
I_B_total = np.sum(I_B_per_mode)

# C-sector: 1 mode, k-dependent omega_C(k)
I_C_per_mode = np.zeros(N_C)
for c_idx in range(N_C):
    omega_c = omega_C_uncoupled[:, c_idx]
    integrand = np.zeros(N_k)
    for i in range(N_k):
        if k_eff[i] > 1e-10 and omega_c[i] > 1e-10:
            integrand[i] = k_eff[i]**2 / omega_c[i]
    I_C_per_mode[c_idx] = np.trapezoid(integrand, k_eff)
I_C_total = np.sum(I_C_per_mode)

I_uncoupled_total = I_A_total + I_B_total + I_C_total

# 1/(16*pi*G) from uncoupled
inv_16piG_uncoupled = I_uncoupled_total / (48 * PI**2)
M_Pl_eff_uncoupled = np.sqrt(2 * inv_16piG_uncoupled)
M_Pl_eff_uncoupled_GeV = M_Pl_eff_uncoupled * M_KK
ratio_G_uncoupled = (M_Pl_reduced / M_Pl_eff_uncoupled_GeV)**2

print(f"  A-sector (36 Dirac modes):")
print(f"    I_A_total = {I_A_total:.6f}")
print(f"    Fraction of total: {I_A_total/I_uncoupled_total*100:.2f}%")
print()
print(f"  B-sector (8 BCS modes):")
print(f"    I_B_total = {I_B_total:.6f}")
print(f"    Fraction of total: {I_B_total/I_uncoupled_total*100:.2f}%")
print()
print(f"  C-sector (1 Leggett mode):")
print(f"    I_C_total = {I_C_total:.6f}")
print(f"    Fraction of total: {I_C_total/I_uncoupled_total*100:.2f}%")
print()
print(f"  I_uncoupled_total = {I_uncoupled_total:.6f}")
print(f"  1/(16*pi*G_uncoupled) = {inv_16piG_uncoupled:.6e} M_KK^2")
print(f"  M_Pl_eff(uncoupled) = {M_Pl_eff_uncoupled:.6e} M_KK = {M_Pl_eff_uncoupled_GeV:.4e} GeV")
print(f"  G_uncoupled / G_obs = {ratio_G_uncoupled:.4e}")
print(f"  |log10(G_uncoupled/G_obs)| = {abs(np.log10(ratio_G_uncoupled)):.4f} OOM")
print()

# =============================================================================
# STEP 4: Hybridization correction
# =============================================================================
print("--- STEP 4: Hybridization Correction ---")
print()

delta_I = I_coupled_total - I_uncoupled_total
frac_correction = delta_I / I_uncoupled_total

# delta(1/G) / (1/G) = delta_I / I_uncoupled
# G_coupled / G_uncoupled = I_uncoupled / I_coupled (inverse relation)
ratio_G_hybrid = I_uncoupled_total / I_coupled_total
delta_G_frac = (I_uncoupled_total - I_coupled_total) / I_coupled_total

print(f"  I_coupled   = {I_coupled_total:.6f}")
print(f"  I_uncoupled = {I_uncoupled_total:.6f}")
print(f"  delta_I = {delta_I:.6f}")
print(f"  delta_I / I_uncoupled = {frac_correction:.6e} = {frac_correction*100:.4f}%")
print()
print(f"  G_coupled / G_uncoupled = {ratio_G_hybrid:.6f}")
print(f"  Hybridization shifts G_N by {delta_G_frac*100:.4f}%")
print()

# =============================================================================
# STEP 5: Sector-resolved analysis of hybridization
# =============================================================================
print("--- STEP 5: Sector-Resolved Hybridization ---")
print()

# For each mode in the coupled spectrum, decompose its Sakharov contribution
# by sector weight
I_coupled_A = 0.0  # (local)
I_coupled_B = 0.0  # (local)
I_coupled_C = 0.0  # (local)

for m in range(N_modes):
    omega_branch = np.abs(omega_full[:, m])
    integrand = np.zeros(N_k)
    for i in range(N_k):
        if k_eff[i] > 1e-10 and omega_branch[i] > 1e-10:
            integrand[i] = k_eff[i]**2 / omega_branch[i]

    I_m = np.trapezoid(integrand, k_eff)

    # Weighted by average sector composition
    avg_weight = np.mean(sector_weight[:, m, :], axis=0)  # (3,)
    I_coupled_A += I_m * avg_weight[0]
    I_coupled_B += I_m * avg_weight[1]
    I_coupled_C += I_m * avg_weight[2]

print(f"  Sakharov integral decomposed by sector weight (coupled):")
print(f"    A-sector contribution: {I_coupled_A:.6f} ({I_coupled_A/I_coupled_total*100:.2f}%)")
print(f"    B-sector contribution: {I_coupled_B:.6f} ({I_coupled_B/I_coupled_total*100:.2f}%)")
print(f"    C-sector contribution: {I_coupled_C:.6f} ({I_coupled_C/I_coupled_total*100:.2f}%)")
print()

# Compare sector-by-sector
print(f"  Sector corrections from hybridization:")
print(f"    A: uncoupled = {I_A_total:.6f}, coupled = {I_coupled_A:.6f}, "
      f"delta = {(I_coupled_A - I_A_total)/I_A_total*100:+.4f}%")
print(f"    B: uncoupled = {I_B_total:.6f}, coupled = {I_coupled_B:.6f}, "
      f"delta = {(I_coupled_B - I_B_total)/I_B_total*100:+.4f}%")
if I_C_total > 1e-12:
    print(f"    C: uncoupled = {I_C_total:.6f}, coupled = {I_coupled_C:.6f}, "
          f"delta = {(I_coupled_C - I_C_total)/I_C_total*100:+.4f}%")
else:
    print(f"    C: uncoupled = {I_C_total:.6e}, coupled = {I_coupled_C:.6e}")
print()

# =============================================================================
# STEP 6: Species counting — N_eff for Sakharov
# =============================================================================
print("--- STEP 6: Effective Species Count N_eff ---")
print()

# In Volovik Paper 28, Eq. (1):
#   G^{-1} = G_0^{-1} + (Lambda^2 / 12*pi) * (n_0 + n_{1/2} - 4*n_1)
#
# For our system at cutoff Lambda = k_max:
#   1/(16*pi*G) = N_eff * Lambda^2 / (48*pi^2)
#
# So: N_eff = 48*pi^2 * inv_16piG / Lambda^2

N_eff_coupled = 48 * PI**2 * inv_16piG_coupled / Lambda_UV**2
N_eff_uncoupled = 48 * PI**2 * inv_16piG_uncoupled / Lambda_UV**2

# Also compute for S44 Dirac tower
# S44: a_0 = 6440, Lambda = 10*M_KK
# 1/(16piG) = a_0 * Lambda^2 / (48*pi^2)  where Lambda=10 M_KK
# So N_eff_S44 = a_0 = 6440 at Lambda=10
N_eff_S44 = a0_fold

# For a massless mode with speed c: I = Lambda^2/(2c)
# For a massive mode with mass m and speed c: I < Lambda^2/(2c)
# So N_eff < N_modes * Lambda^2 / (2*c_min) [upper bound]

print(f"  N_eff = 48*pi^2 * [1/(16*pi*G)] / Lambda^2")
print(f"  Lambda = {Lambda_UV:.6f} M_KK")
print()
print(f"  Coupled:   N_eff = {N_eff_coupled:.2f} (of {N_modes} modes)")
print(f"  Uncoupled: N_eff = {N_eff_uncoupled:.2f} (of {N_modes} modes)")
print(f"  Ratio:     {N_eff_coupled/N_eff_uncoupled:.6f}")
print()
print(f"  For comparison:")
print(f"    S44 Dirac tower: N_eff = {N_eff_S44:.0f} at Lambda = 10 M_KK")
print(f"    S53 GL phonons:  N_modes = 192 at Lambda = {Lambda_S53:.4f} M_KK")
print()

# A-sector dominance check
N_eff_A_only = 48 * PI**2 * (I_A_total / (48 * PI**2)) / Lambda_UV**2
print(f"  A-sector only: N_eff_A = {N_eff_A_only:.2f} (of 36 modes)")
print(f"  B+C sectors:   N_eff_BC = {N_eff_coupled - N_eff_A_only:.2f} (of 9 modes)")
print(f"  Ratio A/(B+C): {N_eff_A_only / (N_eff_coupled - N_eff_A_only + 1e-30):.2f}")
print()

# =============================================================================
# STEP 7: Comparison table
# =============================================================================
print("--- STEP 7: Full Comparison Table ---")
print()
print(f"  {'Method':<35} {'N_eff':>8} {'Lambda':>10} {'G/G_obs':>12} {'OOM':>6}")
print(f"  {'-'*35} {'-'*8} {'-'*10} {'-'*12} {'-'*6}")

methods = [
    ("Coupled 45-mode (this)", N_eff_coupled, Lambda_UV, ratio_G_coupled),
    ("Uncoupled A+B+C", N_eff_uncoupled, Lambda_UV, ratio_G_uncoupled),
    ("A-sector only (36 Dirac)", N_eff_A_only, Lambda_UV,
     (M_Pl_reduced / (np.sqrt(2 * I_A_total / (48*PI**2)) * M_KK))**2),
    ("S53 GL phonons (192)", 192, Lambda_S53, ratio_G_S53),
    ("S44 Dirac tower (6440)", N_eff_S44, 10.0, 0.436),
    ("Spectral action (f_2=1)", a2_fold, 1.0,
     (M_Pl_reduced / (np.sqrt(2 * a2_fold * M_KK**2 / (2*PI)) ))**2 ),
]

for name, neff, lam, ratio in methods:
    oom = abs(np.log10(ratio)) if ratio > 0 else float('inf')
    print(f"  {name:<35} {neff:>8.1f} {lam:>10.4f} {ratio:>12.4e} {oom:>6.2f}")
print()

# =============================================================================
# STEP 8: GGE weighting
# =============================================================================
print("--- STEP 8: GGE-Weighted Sakharov Integral ---")
print()

# The GGE state from the S62 Meissner computation provides occupation numbers
# n_k_GGE for the 8 B-sector modes. For the Sakharov integral in the
# non-equilibrium GGE state, the relevant quantity is whether the
# quasiparticle spectrum is modified. In Volovik's framework, the Sakharov
# integral is a GROUND STATE property (vacuum polarization), not a thermal
# property. The GGE occupation changes the thermal correction to G but
# not the zero-temperature Sakharov integral itself.

print(f"  n_k_GGE = {n_k_GGE}")
print(f"  n_condensate_GGE = {float(d62_meissner['n_condensate_GGE']):.6f}")
print()

# However, the superfluid density (D_s) does modify the effective acoustic metric
# and hence the effective cutoff. The Meissner effect confirms the condensate
# survives (98.85% of fold).
D_s_ratio = D_s_GGE / float(d62_meissner['D_s_fold'])
print(f"  D_s(GGE) / D_s(fold) = {D_s_ratio:.4f}")
print(f"  Interpretation: superfluid fraction {D_s_ratio*100:.2f}% -> ")
print(f"    Sakharov integral reduced by factor sqrt(D_s_ratio) for phonon modes")
print(f"    = {np.sqrt(D_s_ratio):.4f}")
print()

# Compute GGE-corrected Sakharov (phonon sector only)
I_B_GGE = I_B_total * np.sqrt(D_s_ratio)
I_C_GGE = I_C_total * np.sqrt(D_s_ratio)
I_GGE_total = I_A_total + I_B_GGE + I_C_GGE
inv_16piG_GGE = I_GGE_total / (48 * PI**2)
M_Pl_eff_GGE_GeV = np.sqrt(2 * inv_16piG_GGE) * M_KK
ratio_G_GGE = (M_Pl_reduced / M_Pl_eff_GGE_GeV)**2

print(f"  GGE-corrected Sakharov:")
print(f"    I_total(GGE) = {I_GGE_total:.6f}")
print(f"    G(GGE)/G_obs = {ratio_G_GGE:.4e}")
print(f"    G(GGE)/G(uncoupled) = {ratio_G_GGE/ratio_G_uncoupled:.6f}")
print(f"    GGE shift to G_N: {(ratio_G_GGE/ratio_G_uncoupled - 1)*100:+.4f}%")
print()

# =============================================================================
# STEP 9: Physical interpretation — Volovik diagnostic
# =============================================================================
print("--- STEP 9: Volovik Physical Interpretation ---")
print()

print("  STRUCTURAL ANALYSIS:")
print()
print("  1. A-SECTOR DOMINANCE:")
A_frac = I_A_total / I_uncoupled_total * 100
print(f"     A-sector provides {A_frac:.1f}% of uncoupled Sakharov integral")
print(f"     This is the Dirac-tower contribution (36 eigenvalues of D_K)")
print(f"     Masses range: [{omega_A.min():.3f}, {omega_A.max():.3f}] M_KK")
print(f"     Average: {np.mean(omega_A):.3f} M_KK")
print()

print("  2. B-SECTOR (BCS QUASIPARTICLES):")
B_frac = I_B_total / I_uncoupled_total * 100
print(f"     B-sector provides {B_frac:.1f}% of uncoupled Sakharov integral")
print(f"     These are the phonon/Goldstone/Leggett-type modes")
print(f"     Much lighter than A-sector -> larger I per mode (slower modes)")
print()

print("  3. C-SECTOR (LEGGETT):")
C_frac = I_C_total / I_uncoupled_total * 100
print(f"     C-sector provides {C_frac:.1f}% of uncoupled Sakharov integral")
print()

print("  4. HYBRIDIZATION EFFECT:")
print(f"     Total correction: {frac_correction*100:+.4f}%")
print(f"     Number of significantly hybridized modes: {n_hybrid_95}")
if abs(frac_correction) < 0.01:
    print("     CONCLUSION: hybridization is PERTURBATIVE")
    print("     Consistent with weak coupling V_AB << omega_A - omega_B at most crossings")
elif abs(frac_correction) < 0.1:
    print("     CONCLUSION: hybridization is MODERATE")
else:
    print("     CONCLUSION: hybridization is SIGNIFICANT")
print()

print("  5. COMPARISON WITH S53 (UNCOUPLED GL PHONONS):")
print(f"     S53: 192 modes, Lambda={Lambda_S53:.4f}, G/G_obs = {ratio_G_S53:.4e} (4.02 OOM)")
print(f"     This: {N_modes} modes, Lambda={Lambda_UV:.4f}, G/G_obs = {ratio_G_coupled:.4e}")
ratio_S53_this = ratio_G_S53 / ratio_G_coupled
print(f"     Improvement factor: {ratio_S53_this:.4e}")
print(f"     Sources of improvement:")
print(f"       - More modes: {N_modes}/{192} = {N_modes/192:.2f}x (but A-sector dominates)")
print(f"       - Larger cutoff: ({Lambda_UV}/{Lambda_S53})^2 = {(Lambda_UV/Lambda_S53)**2:.2f}x")
print(f"       - A-sector (Dirac) masses >> B-sector (phonon) gaps")
print()

print("  6. COMPARISON WITH S44 DIRAC TOWER:")
print(f"     S44: 6440 modes, Lambda=10 M_KK, G/G_obs = 0.436 (0.36 OOM)")
print(f"     This: {N_modes} modes, Lambda={Lambda_UV:.4f} M_KK, G/G_obs = {ratio_G_coupled:.4e}")
print(f"     The S44 result wins because:")
print(f"       - 6440 >> {N_modes} modes (species counting)")
print(f"       - Lambda = 10 >> {Lambda_UV:.2f} M_KK (higher cutoff)")
print(f"       - Combined: {6440 * 100 / (N_modes * Lambda_UV**2):.0f}x advantage")
print()

# Volovik Paper 28 species formula
# G^{-1} ~ (Lambda^2 / 12*pi) * (n_0 + n_{1/2} - 4*n_1)
# For our system: n_0 ~ N_B + N_C = 9 (bosonic), n_{1/2} ~ N_A = 36 (fermionic Dirac)
# n_1 = 0 (no vector bosons in this sector)
# Sign: fermionic contribution ADDS to 1/G (makes G smaller)
n_species_volovik = N_B + N_C + N_A  # n_0 + n_{1/2}
print("  7. VOLOVIK SPECIES FORMULA (Paper 28, Eq.1):")
print(f"     G^{{-1}} ~ (Lambda^2/12*pi) * (n_0 + n_{{1/2}} - 4*n_1)")
print(f"     n_0 (scalars/bosonic) = {N_B + N_C}")
print(f"     n_{{1/2}} (Weyl/fermionic) = {N_A}")
print(f"     n_1 (vectors) = 0")
print(f"     N_species = {n_species_volovik}")
print(f"     Both fermions and bosons ADD to 1/G (make G smaller)")
print(f"     Only vectors SUBTRACT (reduce 1/G, make G larger)")
print()

# =============================================================================
# STEP 10: Cross-check — direct sum vs matrix diagonalization
# =============================================================================
print("--- STEP 10: Cross-Check — Sum Rules ---")
print()

# The coupled eigenvalues should satisfy the trace sum rule:
# sum omega_coupled(k) = sum omega_uncoupled(k) for each k
# (trace is invariant under similarity transformation)
print("  Trace sum rule (sum of eigenvalues):")
for c in [0, 5, 10, 15, 20, 25, 31]:
    trace_coupled = np.sum(omega_full[c])
    trace_uncoupled = np.sum(omega_A) + np.sum(omega_B_uncoupled[c]) + np.sum(omega_C_uncoupled[c])
    ratio_trace = trace_coupled / trace_uncoupled if trace_uncoupled != 0 else float('inf')
    print(f"    Cell {c:2d}: coupled = {trace_coupled:.4f}, uncoupled = {trace_uncoupled:.4f}, "
          f"ratio = {ratio_trace:.6f}")

# Note: the trace sum rule holds exactly only if the coupling matrix is traceless
# (which V_AB generally is not). The deviation measures the coupling strength.
print()

# =============================================================================
# SUMMARY
# =============================================================================
print("=" * 72)
print("SUMMARY: SAKHAROV-HYBRID-63")
print("=" * 72)
print()
print(f"  COUPLED 45-mode spectrum:")
print(f"    G_coupled / G_obs = {ratio_G_coupled:.4e}")
print(f"    |log10| = {abs(np.log10(ratio_G_coupled)):.4f} OOM")
print(f"    M_Pl_eff = {M_Pl_eff_coupled_GeV:.4e} GeV")
print()
print(f"  UNCOUPLED (sector sum):")
print(f"    G_uncoupled / G_obs = {ratio_G_uncoupled:.4e}")
print(f"    |log10| = {abs(np.log10(ratio_G_uncoupled)):.4f} OOM")
print()
print(f"  HYBRIDIZATION CORRECTION:")
print(f"    delta(1/G) / (1/G) = {frac_correction*100:+.4f}%")
print(f"    G_coupled / G_uncoupled = {ratio_G_hybrid:.6f}")
print()
print(f"  SECTOR DECOMPOSITION (uncoupled):")
print(f"    A (Dirac, 36 modes): {A_frac:.1f}%")
print(f"    B (BCS, 8 modes):    {B_frac:.1f}%")
print(f"    C (Leggett, 1 mode): {C_frac:.1f}%")
print()
print(f"  COMPARISON:")
print(f"    S53 GL phonons (192 modes): G/G_obs = {ratio_G_S53:.4e} (4.02 OOM)")
print(f"    S44 Dirac tower (6440 modes): G/G_obs = 0.436 (0.36 OOM)")
print(f"    This (45 coupled modes): G/G_obs = {ratio_G_coupled:.4e} ({abs(np.log10(ratio_G_coupled)):.2f} OOM)")
print()
print(f"  N_eff (effective species at Lambda={Lambda_UV:.3f}):")
print(f"    Coupled: {N_eff_coupled:.2f}")
print(f"    Uncoupled: {N_eff_uncoupled:.2f}")
print()
print(f"  GATE VERDICT: SAKHAROV-HYBRID-63 = INFO")
print(f"    Hybridization correction to Sakharov G_N is {abs(frac_correction)*100:.2f}%.")
print(f"    A-sector (Dirac) dominates ({A_frac:.0f}%). Phonon corrections subleading.")
print(f"    Consistent with Volovik (1998, Paper 06): 1/G ~ N_species * Lambda^2.")
print(f"    S44 Dirac-tower result (0.36 OOM) remains the primary G_N computation.")
print()

# =============================================================================
# Save .npz
# =============================================================================
npz_path = os.path.join(base_dir, "s63_sakharov_hybrid.npz")
np.savez(npz_path,
    # Spectrum metadata
    N_k=N_k,
    N_modes=N_modes,
    N_A=N_A,
    N_B=N_B,
    N_C=N_C,
    Lambda_UV=Lambda_UV,
    k_eff=k_eff,
    # Coupled results
    I_coupled_total=I_coupled_total,
    I_coupled_per_mode=I_coupled_per_mode,
    inv_16piG_coupled=inv_16piG_coupled,
    M_Pl_eff_coupled_GeV=M_Pl_eff_coupled_GeV,
    ratio_G_coupled=ratio_G_coupled,
    log10_ratio_coupled=abs(np.log10(ratio_G_coupled)),
    N_eff_coupled=N_eff_coupled,
    # Uncoupled results
    I_A_total=I_A_total,
    I_B_total=I_B_total,
    I_C_total=I_C_total,
    I_uncoupled_total=I_uncoupled_total,
    inv_16piG_uncoupled=inv_16piG_uncoupled,
    M_Pl_eff_uncoupled_GeV=M_Pl_eff_uncoupled_GeV,
    ratio_G_uncoupled=ratio_G_uncoupled,
    log10_ratio_uncoupled=abs(np.log10(ratio_G_uncoupled)),
    N_eff_uncoupled=N_eff_uncoupled,
    # Hybridization
    delta_I=delta_I,
    frac_correction_I=frac_correction,
    ratio_G_hybrid=ratio_G_hybrid,
    n_hybrid_95=n_hybrid_95,
    n_hybrid_80=n_hybrid_80,
    # Sector decomposition (coupled, weighted)
    I_coupled_A=I_coupled_A,
    I_coupled_B=I_coupled_B,
    I_coupled_C=I_coupled_C,
    # Sector fractions (uncoupled)
    A_frac=A_frac,
    B_frac=B_frac,
    C_frac=C_frac,
    # GGE
    ratio_G_GGE=ratio_G_GGE,
    D_s_ratio=D_s_ratio,
    # S53 comparison
    ratio_G_S53=ratio_G_S53,
    improvement_over_S53=ratio_S53_this,
    # Gate
    gate_name=np.array(["SAKHAROV-HYBRID-63"]),
    gate_verdict=np.array(["INFO"]),
    gate_detail=np.array([
        f"INFO: G_coupled/G_obs = {ratio_G_coupled:.4e} ({abs(np.log10(ratio_G_coupled)):.2f} OOM). "
        f"Hybridization correction {frac_correction*100:+.2f}%. "
        f"A-sector (Dirac) dominates at {A_frac:.0f}%. "
        f"N_eff(coupled) = {N_eff_coupled:.1f}. "
        f"Consistent with Volovik (1998): phonons subleading."
    ])
)
print(f"  Data saved to: {npz_path}")

# Save output text
out_path = os.path.join(base_dir, "s63_sakharov_hybrid_output.txt")
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    print("=" * 72)
    print("SAKHAROV-HYBRID-63 RESULTS")
    print("=" * 72)
    print(f"G_coupled/G_obs = {ratio_G_coupled:.4e} ({abs(np.log10(ratio_G_coupled)):.2f} OOM)")
    print(f"G_uncoupled/G_obs = {ratio_G_uncoupled:.4e} ({abs(np.log10(ratio_G_uncoupled)):.2f} OOM)")
    print(f"Hybridization correction: {frac_correction*100:+.4f}%")
    print(f"A-sector fraction: {A_frac:.1f}%")
    print(f"N_eff(coupled) = {N_eff_coupled:.2f}")
    print(f"N_eff(uncoupled) = {N_eff_uncoupled:.2f}")
    print(f"Lambda_UV = {Lambda_UV:.6f} M_KK")
    print(f"S53 comparison: {ratio_S53_this:.4e}x improvement")
    print(f"S44 Dirac tower: 0.436 (0.36 OOM) remains primary")
    print(f"GATE: SAKHAROV-HYBRID-63 = INFO")
with open(out_path, 'w') as f:
    f.write(buf.getvalue())
print(f"  Output saved to: {out_path}")
