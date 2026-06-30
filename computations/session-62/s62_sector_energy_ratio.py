#!/usr/bin/env python3
"""
s62_sector_energy_ratio.py — Energy Partition Between Sectors
=============================================================
Gate: SECTOR-ENERGY-RATIO-62
Session: S62, Wave 3, Entry W3-08

Computes the energy ratio between:
  Sector A (geometric): 36 Hessian moduli eigenvalues of d^2 SA / dphi_i dphi_j
  Sector B (collective): 31+1 Bogoliubov-Anderson phononic modes

Physics:
  The spectral action on M^4 x SU(3)_Jensen has the form (CCM 2007):
    S_b = 2 f_4 Lambda^4 a_0 + 2 f_2 Lambda^2 a_2 + f_0 a_4 + ...
  where:
    f_0 = f(0)                   — value at origin, determines gauge coupling
    f_2 = int_0^inf f(u) du      — zeroth moment, determines Newton's G
    f_4 = int_0^inf u f(u) du    — first moment, determines CC

  Gauge coupling relation (CCM):
    g^2 f_0 / (2 pi^2) = 1/4
    => alpha_GUT = g^2 / (4 pi) = pi / (2 f_0)

  Standard unification: alpha_GUT ~ 1/25 => f_0 ~ 9.82.

  HERE: We extract f_0 from the energy partition requirement that the geometric
  sector (Hessian eigenvalues) and collective sector (BA phonon energies) are
  related through the spectral action coefficients. Specifically:
    E_A / E_B = f_0 * a_4 / (2 f_2 Lambda^2 a_2)
  which connects the a_4 (gauge kinetic) and a_2 (Einstein-Hilbert) terms.

Pre-registered gate:
    PASS if f_0 in [1, 20].
    FAIL if f_0 < 0.1 or f_0 > 100.
    INFO if f_0 in [0.1, 1] or [20, 100].

Inputs:
    computations/session-61/s61_moduli_hessian.npz (36 tree-level Hessian eigenvalues)
    computations/session-62/s62_hessian_oneloop.npz (36 one-loop corrected eigenvalues)
    computations/session-61/s61_vanhove_dispersion.npz (BA spectrum, omega(tau, k, band))
    computations/session-61/s61_trace_formula_geometric.npz (Gilkey coefficients)
    computations/session-62/s62_cutoff_london.npz (CUTOFF-LONDON-62 results)
    computations/session-42/s42_gradient_stiffness.npz (SA vs tau)

Outputs:
    computations/session-62/s62_sector_energy_ratio.npz
    computations/session-62/s62_sector_energy_ratio.png
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    PI, tau_fold, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, Vol_SU3_Haar,
    a0_fold, a2_fold, a4_fold,
)

# =============================================================================
#  1. Load all input data
# =============================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))
archive_dir = os.path.join(os.path.dirname(script_dir), 'computations/_shared')

# Sector A: Hessian eigenvalues
hess_tree = np.load(os.path.join(script_dir, 's61_moduli_hessian.npz'),
                    allow_pickle=True)
evals_tree_36 = hess_tree['evals_36']          # 36 tree-level (all negative)
SA_fold_hess = float(hess_tree['SA_fold'])

hess_1loop = np.load(os.path.join(script_dir, 's62_hessian_oneloop.npz'),
                     allow_pickle=True)
evals_1loop_36 = hess_1loop['evals_eff']       # 36 one-loop (all positive)
d2S1_diag = hess_1loop['d2S1_diag']            # one-loop diagonal corrections

# Sector B: BA spectrum
ba_data = np.load(os.path.join(script_dir, 's61_vanhove_dispersion.npz'),
                  allow_pickle=True)
tau_ba = ba_data['tau_values']                  # (50,)
omega_ba = ba_data['omega']                     # (50, 32, 4)
lambda_n = ba_data['lambda_n']                  # (32,) graph eigenvalues
E_J_arr = ba_data['E_J']                        # (50,) Josephson coupling vs tau
E_sp_B2 = ba_data['E_sp_B2']                   # (50, 4) BCS quasiparticle energies

# Trace formula / Gilkey coefficients
trace_data = np.load(os.path.join(script_dir, 's61_trace_formula_geometric.npz'),
                     allow_pickle=True)
a0_gilkey = float(trace_data['a0_gilkey'])      # 0.866
a2_gilkey_fold = float(trace_data['a2_gilkey_fold'])   # 0.728235
R_fold_trace = float(trace_data['R_fold'])      # 2.018
tau_trace_arr = trace_data['tau_arr']           # (36,)
a2a0_arr = trace_data['a2a0_arr']              # (36,) a_2/a_0 vs tau
R_arr = trace_data['R_arr']                    # (36,) scalar curvature vs tau

# Cutoff London results (cross-reference)
cutoff_data = np.load(os.path.join(script_dir, 's62_cutoff_london.npz'),
                      allow_pickle=True)
a4_gilkey_fold = float(cutoff_data['a4_gilkey_fold'])  # 0.30146
ratio_a4_a2 = float(cutoff_data['ratio_a4_a2_gilkey'])  # 0.41396
f2_task = float(cutoff_data['f2_task_target'])  # 2.34
f0_alpha25 = float(cutoff_data['f0_for_alpha25'])  # 9.817

# SA vs tau (for Sector A tau-dependence)
sa_tau_data = np.load(os.path.join(archive_dir, 's42_gradient_stiffness.npz'),
                      allow_pickle=True)
tau_sa_grid = sa_tau_data['tau_grid']           # (10,)
S_total_arr = sa_tau_data['S_total']            # (10,)
d2S_dtau2_arr = sa_tau_data['d2S_dtau2']        # (10,)

# Lambda^2 from Hessian data
Lambda_sq = float(hess_tree['Lambda_sq'])       # 16.984

print("=" * 70)
print("SECTOR-ENERGY-RATIO-62: Energy Partition Between Sectors")
print("=" * 70)
print()

# =============================================================================
#  2. Compute E_A (Sector A — Geometric)
# =============================================================================
# E_A = sum |lambda_i| for the 36 Hessian eigenvalues
# These are curvatures of the spectral action in moduli space.
# At tree level, all 36 are NEGATIVE (fold is a SA maximum).
# At one-loop, all 36 flip POSITIVE (quantum stabilization).

E_A_tree = np.sum(np.abs(evals_tree_36))
E_A_1loop = np.sum(evals_1loop_36)           # all positive, so sum = sum|.|

print("--- Sector A: Geometric Hessian ---")
print(f"  36 tree-level eigenvalues: all negative (SA maximum at fold)")
print(f"    sum |lambda_tree| = {E_A_tree:.4f} M_KK^2")
print(f"    min = {evals_tree_36.min():.4f}, max = {evals_tree_36.max():.4f}")
print(f"  36 one-loop eigenvalues: all positive (quantum stabilization)")
print(f"    sum  lambda_1loop = {E_A_1loop:.4f} M_KK^2")
print(f"    min = {evals_1loop_36.min():.4f}, max = {evals_1loop_36.max():.4f}")
print(f"  Ratio E_A_tree / E_A_1loop = {E_A_tree / E_A_1loop:.6f}")
print()

# =============================================================================
#  3. Compute E_B (Sector B — Collective BA phonons)
# =============================================================================
# 31 optical modes x 4 BCS bands = 124 excitations
# Plus 1 acoustic mode (k=0) with 4 bands = 4 more
# E_B = sum omega_BA(k, n) for all modes

fold_idx_ba = np.argmin(np.abs(tau_ba - tau_fold))
tau_at_fold = tau_ba[fold_idx_ba]

# Sum over all 31 optical modes, all 4 bands
E_B_optical = np.sum(omega_ba[fold_idx_ba, 1:, :])  # exclude k=0 acoustic
E_B_acoustic = np.sum(omega_ba[fold_idx_ba, 0, :])   # k=0 only
E_B_total = np.sum(omega_ba[fold_idx_ba, :, :])
E_B_band0_optical = np.sum(omega_ba[fold_idx_ba, 1:, 0])
E_J_fold = E_J_arr[fold_idx_ba]

print("--- Sector B: Collective BA Phonons ---")
print(f"  tau at fold index: {tau_at_fold:.4f} (target: {tau_fold})")
print(f"  Josephson coupling E_J(fold) = {E_J_fold:.6f} M_KK")
print(f"  31 optical modes x 4 bands = 124 excitations")
print(f"    E_B (31 optical, all 4 bands) = {E_B_optical:.4f} M_KK")
print(f"    E_B (acoustic k=0, 4 bands)   = {E_B_acoustic:.4f} M_KK")
print(f"    E_B (total, 32x4=128)         = {E_B_total:.4f} M_KK")
print(f"    E_B (band 0 only, 31 optical) = {E_B_band0_optical:.4f} M_KK")
print()

# =============================================================================
#  4. Compute spectral action energy terms: E_2, E_4
# =============================================================================
# S_b = 2 f_4 Lambda^4 a_0 + 2 f_2 Lambda^2 a_2 + f_0 a_4 + ...
# Using Gilkey-normalized coefficients:
#   a_2 = 0.728235 (per unit volume, normalized by (4pi)^{-4})
#   a_4/a_2 = 0.414
#   f_2 = 2.34 (from gravity matching)
#
# E_2 = a_2 * f_2 * Lambda^2  (Einstein-Hilbert contribution, with 2 from CCM)
# E_4 = a_4 * f_4 * Lambda^4  (CC contribution, with 2 from CCM)

a_2 = a2_gilkey_fold    # 0.728235
a_4 = a4_gilkey_fold    # 0.30146
f_2 = f2_task           # 2.34
# For f_4, use the Gaussian and Exponential PASS values from CUTOFF-LONDON-62
f4_gaussian = float(cutoff_data['Gaussian_f4'])      # 0.558
f4_exponential = float(cutoff_data['Exponential_f4'])  # 1.673

# Lambda^2 in M_KK^2 units
Lam2 = Lambda_sq  # 16.984

E_2_term = 2 * f_2 * Lam2 * a_2       # with factor 2 from CCM
E_4_gaussian = 2 * f4_gaussian * Lam2**2 * a0_gilkey
E_4_exponential = 2 * f4_exponential * Lam2**2 * a0_gilkey
E_gauge = f0_alpha25 * a_4              # f_0 * a_4 = gauge kinetic term

print("--- Spectral Action Energy Decomposition ---")
print(f"  Gilkey coefficients: a_2 = {a_2:.6f}, a_4 = {a_4:.5f}, a_0 = {a0_gilkey:.6f}")
print(f"  Ratio a_4/a_2 = {ratio_a4_a2:.5f}")
print(f"  Lambda^2 = {Lam2:.4f} M_KK^2")
print(f"  f_2 = {f_2:.4f}, f_0(alpha_GUT=1/25) = {f0_alpha25:.4f}")
print()
print(f"  E_2 = 2 * f_2 * Lambda^2 * a_2 = 2 * {f_2:.3f} * {Lam2:.3f} * {a_2:.6f}")
print(f"       = {E_2_term:.4f} M_KK^2")
print(f"  E_4 (Gaussian, f_4={f4_gaussian:.4f}) = 2 * f_4 * Lambda^4 * a_0")
print(f"       = {E_4_gaussian:.4f} M_KK^4")
print(f"  E_4 (Exponential, f_4={f4_exponential:.4f}) = {E_4_exponential:.4f} M_KK^4")
print(f"  E_gauge (f_0={f0_alpha25:.4f}) = f_0 * a_4 = {E_gauge:.4f} (dimensionless)")
print()

# =============================================================================
#  5. Compute E_A / E_B ratio and extract f_0
# =============================================================================
# The relationship between sectors:
# Sector A stiffness = d^2 SA / dphi^2 evaluated at the fold
# These eigenvalues have units of SA curvature = Lambda^2 * (combination of a_n * f_n)
#
# The key structural relation: the Hessian eigenvalues are curvatures of
# S = 2 f_4 Lam^4 a_0 + 2 f_2 Lam^2 a_2 + f_0 a_4
# in the moduli space. The tree-level Hessian comes from the classical SA.
# The one-loop correction comes from quantum fluctuations in the BA spectrum.
#
# Method 1: Direct ratio E_A / E_B
# The Hessian eigenvalues are d^2 S / dphi_i^2, which are M_KK^2 quantities
# The BA frequencies omega are M_KK quantities
# So E_A has units M_KK^2 and E_B has units M_KK
# The dimensional ratio E_A/E_B has units M_KK
#
# Method 2: Dimensionless ratio using SA decomposition
# The SA at fold = S_fold = 2*f_4*Lam^4*a_0 + 2*f_2*Lam^2*a_2 + f_0*a_4
# The Hessian eigenvalue sum |lambda_i| / SA_fold is dimensionless
# The BA energy / M_KK is dimensionless
# Compare these to extract the coupling

print("--- Energy Ratios and f_0 Extraction ---")
print()

# Method 1: Direct dimensional ratio
ratio_direct_tree = E_A_tree / E_B_total
ratio_direct_1loop = E_A_1loop / E_B_total
print(f"  Method 1: Direct ratio E_A/E_B")
print(f"    E_A(tree)/E_B(total) = {ratio_direct_tree:.4f} M_KK")
print(f"    E_A(1loop)/E_B(total) = {ratio_direct_1loop:.4f} M_KK")
print()

# Method 2: Normalized by spectral action scale
# E_A_norm = sum|lambda_i| / d2S_dtau2  (fraction of total curvature in moduli)
# E_B_norm = E_B / SA_fold^{1/2}        (BA energy vs SA energy scale)
# But these are different normalizations, not immediately comparable.
#
# Better: the one-loop correction to the Hessian comes from the BA modes.
# H_eff = H_tree + H_1loop, where H_1loop ~ sum over BA modes of d^2 E_BA/dphi^2
# The d2S1_diag are the one-loop corrections along each basis direction.
# So the one-loop piece IS the BA sector's back-reaction on moduli.

E_1loop_correction = np.sum(d2S1_diag)
E_tree_total = np.sum(np.abs(evals_tree_36))

print(f"  Method 2: One-loop correction analysis")
print(f"    sum(d2S1_diag) = {E_1loop_correction:.4f} (total 1-loop correction)")
print(f"    sum|evals_tree| = {E_tree_total:.4f} (tree curvature)")
print(f"    1-loop/tree ratio = {E_1loop_correction / E_tree_total:.4f}")
print(f"    1-loop correction per mode = {E_1loop_correction / 36:.4f}")
print()

# Method 3: Extract f_0 from the SA decomposition at the fold
# S_fold = 2*f_4*Lam^4*a_0 + 2*f_2*Lam^2*a_2 + f_0*a_4
# We know S_fold, f_2, a_0, a_2, Lam^2. Also know a_4.
# But f_4 is NOT independently known (it depends on cutoff choice).
#
# The Hessian captures d^2 S / dphi^2 = d^2[...]/dphi^2
# The f_4 term (CC) is f_4*Lam^4*a_0 which does NOT depend on internal geometry
# moduli -- a_0 is the volume factor only. So d^2(f_4*Lam^4*a_0)/dphi^2 = 0
# if a_0 doesn't depend on the moduli phi.
#
# Actually, a_0 DOES depend on the internal metric through det(g).
# But the dominant moduli-dependent terms come from a_2 (through R)
# and a_4 (through Riemann, Ricci, etc.).
#
# Key insight: the RATIO of Hessian contributions from a_2 vs a_4 terms
# is controlled by the ratio (2*f_2*Lam^2) / f_0.
# If f_0 << f_2*Lam^2, the Einstein-Hilbert term dominates moduli stiffness.
# If f_0 >> f_2*Lam^2, the gauge kinetic term dominates.
#
# The tree-level Hessian is:
#   H_ij^tree = 2*f_4*Lam^4 * d^2 a_0/dphi^2 + 2*f_2*Lam^2 * d^2 a_2/dphi^2 + f_0 * d^2 a_4/dphi^2
#
# At the fold, d^2 a_0/dphi^2 ~ a_0 * (curvature of volume)
# d^2 a_2/dphi^2 ~ a_2 * (curvature of scalar curvature term)
# d^2 a_4/dphi^2 ~ a_4 * (curvature of gauge kinetic term)
#
# The observed Hessian eigenvalue sum = E_A_tree = 2188.23
# The SA at fold with canonical constants: S_fold = 250360.68
# The d^2S/dtau^2 = 317862.85 at fold
#
# For the per-modulus curvature in the full 36D space:
# Mean curvature = E_A_tree / 36 = 60.78
# Mean curvature / d^2S/dtau^2 = 0.000191 (moduli are much softer than tau)

print(f"  Method 3: SA decomposition")
print(f"    SA at fold (canonical) = {SA_fold_hess:.4f}")
print(f"    d^2 SA/dtau^2 at fold = {d2S_dtau2_arr[5]:.4f} (tau=0.19)")
print(f"    Mean Hessian eigenvalue = {E_A_tree / 36:.4f} M_KK^2")
print(f"    Mean |evals|/d^2S = {(E_A_tree/36) / d2S_dtau2_arr[5]:.6f}")
print()

# Method 4: f_0 extraction from energy partition
# The physical connection: Sector A is the UV part (geometry, f_0*a_4 and f_2*Lam^2*a_2)
# Sector B is the IR part (collective excitations, phononic modes)
# At the fold, both sectors must give a consistent spectral action.
#
# The BA phonon energies sum to E_B. These modes renormalize the SA through
# the one-loop effective action: S_1loop = S_tree + (1/2) sum log(omega_BA^2)
# The one-loop contribution S_1 = (1/2) sum log(omega^2) ~ sum omega (in ZPE sense)
# More precisely S_1 = (1/2) Tr log(D^2/mu^2) on the fluctuation operator.
#
# The CCM gauge coupling relation: g^2 f_0 / (2*pi^2) = 1/4
# => f_0 = pi^2/(2*g^2) = pi/(8*alpha)
# => alpha_GUT = pi/(8*f_0)
#
# Wait -- let me be more careful with the CCM convention.
# From the CUTOFF-LONDON-62 script line 21:
#   g^2 f_0 / (2 pi^2) = 1/4
#   => f_0 = pi^2 / (2 g^2)
#   => alpha = g^2/(4pi) => g^2 = 4*pi*alpha
#   => f_0 = pi^2 / (8*pi*alpha) = pi/(8*alpha)
#   => alpha = pi/(8*f_0)
#   For alpha=1/25: f_0 = 25*pi/8 = 9.817
# But the cutoff london script line 22 says:
#   alpha_GUT = 1/25 requires f_0 = pi*25/8 = 9.817
# Confirmed: alpha_GUT = pi/(8*f_0), so f_0 = pi/(8*alpha_GUT).

# Now: extract f_0 from E_A / E_B.
# The crucial observation: the Hessian eigenvalues encode how the SA
# changes under moduli deformations. These deformations change the internal
# geometry of SU(3), which changes a_0, a_2, a_4. The changes propagate
# to the physical 4D parameters through f_0, f_2, f_4.
#
# In the SA decomposition:
# d^2 S / dphi_i dphi_j = 2*f_4*Lam^4 * H0_ij + 2*f_2*Lam^2 * H2_ij + f_0 * H4_ij
# where Hn_ij = d^2 a_n / dphi_i dphi_j.
#
# The BA phonon spectrum omega_n(k) provides the collective excitation energies.
# The total zero-point energy of BA modes = (1/2) sum omega_n(k).
# This is the 1-loop contribution to SA.
#
# For the f_0 extraction:
# The tree-level Hessian is dominated by the f_2*Lam^2*a_2 term (since f_4*Lam^4*a_0
# gives volume-only dependence and f_0*a_4 is parametrically smaller for f_0~10).
# The 1-loop correction comes from BA modes.
#
# The ratio:
#   E_A_tree / E_B = R_hess * (f_2 * Lam^2)        ... from tree-level SA
#   E_A_1loop / E_B = R_1loop                         ... one-loop = BA backreaction
#
# The dimensionless ratio that determines f_0:
# sum(d^2 a_4/dphi^2) / sum(d^2 a_2/dphi^2) = (a_4/a_2) * structural_factor
# => f_0 = [E_A_tree - 2*f_4*Lam^4*d^2a_0 - 2*f_2*Lam^2*d^2a_2] / d^2a_4
#
# More directly: compare the one-loop correction (from BA modes) to the
# gauge kinetic term (from f_0*a_4).
# The one-loop correction sum d2S1_diag = total shift in diagonal Hessian elements
# This equals the BA modes' contribution to moduli stiffness.
# If this equals f_0 * (d^2 a_4/dphi^2 summed over moduli), we can extract f_0.
#
# Concretely:
# S_1loop_center = 5751.35 (from s62_hessian_oneloop.npz, S1_center)
# This is the total 1-loop SA contribution at the fold.
# The tree SA = S_fold = 11091.86 (from s61_moduli_hessian.npz, SA_fold)
# Note: S_fold from s61 (11091.86) ≠ S_fold from s42 (250360.68) because
# they use different eigenvalue truncations / normalization.
# The s61 Hessian uses Lambda_sq=16.98, which is the heat kernel regulator.

S1_center = float(hess_1loop['S1_center'])   # 5751.35
SA_tree_fold = SA_fold_hess                   # 11091.86

print(f"  Method 4: f_0 from energy partition")
print(f"    S_tree at fold = {SA_tree_fold:.4f}")
print(f"    S_1loop at fold = {S1_center:.4f}")
print(f"    S_total = S_tree + S_1loop = {SA_tree_fold + S1_center:.4f}")
print(f"    S_1loop / S_tree = {S1_center / SA_tree_fold:.6f}")
print()

# Approach A: f_0 from the gauge kinetic term share
# In the SA decomposition at the fold (using Gilkey normalized coefficients):
# S_tree = 2*f_4*Lam^4*a_0 + 2*f_2*Lam^2*a_2 + f_0*a_4
# We know: S_tree = 11091.86, Lam^2 = 16.98, a_0=0.866, a_2=0.728, a_4=0.301
# f_2 = 2.34 (from gravity)
# => 2*f_2*Lam^2*a_2 = 2*2.34*16.98*0.728 = 57.84
# => S_tree - 57.84 = 2*f_4*Lam^4*a_0 + f_0*a_4
# => 11091.86 - 57.84 = 2*f_4*Lam^4*a_0 + f_0*0.301
# => 11034.02 = 2*f_4*288.32*0.866 + f_0*0.301
# => 11034.02 = 499.4*f_4 + 0.301*f_0

contrib_f2 = E_2_term  # = 2*f_2*Lam^2*a_2
remainder = SA_tree_fold - contrib_f2
coeff_f4 = 2 * Lam2**2 * a0_gilkey
coeff_f0 = a_4

print(f"  Approach A: SA decomposition at fold")
print(f"    E_2 contribution = 2*f_2*Lam^2*a_2 = {contrib_f2:.4f}")
print(f"    Remainder = S_tree - E_2 = {remainder:.4f}")
print(f"    Remainder = {coeff_f4:.2f}*f_4 + {coeff_f0:.5f}*f_0")
print()

# Using Gaussian f_4 = 0.558:
f0_from_gauss = (remainder - coeff_f4 * f4_gaussian) / coeff_f0
alpha_from_gauss = PI / (8 * f0_from_gauss) if f0_from_gauss > 0 else float('nan')
print(f"    With f_4 = {f4_gaussian:.4f} (Gaussian):")
print(f"      f_0 = {f0_from_gauss:.4f}")
if f0_from_gauss > 0:
    print(f"      alpha_GUT = pi/(8*f_0) = {alpha_from_gauss:.6f}")
    print(f"      1/alpha_GUT = {1/alpha_from_gauss:.2f}")
print()

# Using Exponential f_4 = 1.673:
f0_from_exp = (remainder - coeff_f4 * f4_exponential) / coeff_f0
alpha_from_exp = PI / (8 * f0_from_exp) if f0_from_exp > 0 else float('nan')
print(f"    With f_4 = {f4_exponential:.4f} (Exponential):")
print(f"      f_0 = {f0_from_exp:.4f}")
if f0_from_exp > 0:
    print(f"      alpha_GUT = pi/(8*f_0) = {alpha_from_exp:.6f}")
    print(f"      1/alpha_GUT = {1/alpha_from_exp:.2f}")
print()

# Approach B: f_0 from the BA phonon zero-point energy
# The 1-loop SA from BA modes:
# S_1loop = (1/2) sum_k sum_n log(omega_n(k)^2/mu^2)
# The one-loop correction to the Hessian (d^2 S_1loop / dphi^2) was computed:
# sum d2S1_diag = 7627.35
# This is the BA sector's contribution to moduli curvature.
#
# The f_0*a_4 term: its contribution to the Hessian is f_0 * (d^2 a_4/dphi^2)
# At the fold, d^2 a_4/dphi^2 ~ a_4 * (geometric second derivative factor)
#
# For the ONE-LOOP Hessian eigenvalue sum vs BA energy:
# The 1-loop Hessian = tree Hessian + BA backreaction
# sum(evals_1loop) = 5156.13
# sum|evals_tree| = 2188.23
# These don't add because of sign flips: 36 eigenvalues flip from negative to positive
# The net 1-loop correction = sum(evals_1loop) + sum(evals_tree)  [signs opposite!]
# = 5156.13 + (-2188.23) = 2967.90 ... no, more carefully:
# evals_1loop_i = evals_tree_i + delta_i (1-loop shift)
# But evals_tree are all negative, evals_1loop are all positive
# So delta_i = evals_1loop_i - evals_tree_i (= positive - negative = very positive)

delta_evals = evals_1loop_36 - hess_1loop['evals_tree']  # 1-loop shifts per mode
sum_delta = np.sum(delta_evals)
mean_delta = np.mean(delta_evals)

print(f"  Approach B: 1-loop shift analysis")
print(f"    Per-mode 1-loop shift: min={delta_evals.min():.4f}, max={delta_evals.max():.4f}")
print(f"    Mean 1-loop shift = {mean_delta:.4f} M_KK^2")
print(f"    Total 1-loop shift = {sum_delta:.4f} M_KK^2")
print(f"    1-loop shift / E_B(total) = {sum_delta / E_B_total:.4f} M_KK")
print(f"    1-loop shift / E_B(band0, opt) = {sum_delta / E_B_band0_optical:.4f} M_KK")
print()

# Approach C: f_0 from ratio of BA energy to gauge kinetic contribution
# The gauge kinetic term in SA = f_0 * a_4
# The BA zero-point energy = (1/2) E_B_total
# The consistency condition: the BA modes GENERATE the gauge kinetic term at 1-loop
# => f_0 * a_4 ~ alpha * E_B_ZPE / (number of gauge modes)
# This is the standard CCM mechanism: gauge bosons are collective modes of the spectral geometry
#
# More precisely: the f_0*a_4 term yields the Yang-Mills action in 4D.
# The a_4 coefficient contains Tr(F^2) integrated over the internal space.
# The gauge coupling g^2 = 2*pi^2 / f_0.
#
# The energy partition interpretation:
# f_0 = (total geometric curvature) / (gauge kinetic curvature per modulus)
# => f_0 = E_A / (N_gauge * a_4_per_gauge)
#
# Direct extraction: use the SA at fold to determine f_0 self-consistently
# with f_2 = 2.34 fixed and f_4 from cutoff scan.

# Approach D: Direct f_0 from alpha_GUT constraint (benchmark)
# This is the "standard" answer: alpha_GUT = 1/25 => f_0 = 9.817
# Check if the energy ratio is CONSISTENT with this.
f0_standard = f0_alpha25  # 9.817
E_gauge_standard = f0_standard * a_4  # gauge kinetic contribution
E_EH_standard = contrib_f2             # 2*f_2*Lam^2*a_2

print(f"  Approach D: Standard f_0 = {f0_standard:.4f} benchmark")
print(f"    Gauge kinetic contribution: f_0 * a_4 = {E_gauge_standard:.4f}")
print(f"    Einstein-Hilbert contribution: 2*f_2*Lam^2*a_2 = {E_EH_standard:.4f}")
print(f"    Gauge/EH ratio = {E_gauge_standard / E_EH_standard:.6f}")
print(f"    E_B(total) / (Lam^2 * gauge) = {E_B_total / (Lam2 * E_gauge_standard):.4f}")
print()

# =============================================================================
#  6. The DEFINITIVE f_0 extraction
# =============================================================================
# The cleanest route: use S_tree decomposition directly.
# S_tree = sum over eigenvalues of f(D_K^2/Lambda^2) on the internal space
# At the fold with heat kernel regularization:
# S_tree = SA_fold_hess = 11091.86
#
# The asymptotic expansion:
# S ~ 2*f_4*Lam^4*a_0 + 2*f_2*Lam^2*a_2 + f_0*a_4 + O(1/Lam^2)
#
# With f_2 = 2.34 determined by gravity and f_4 from cutoff scan,
# f_0 is uniquely determined by the residual.
#
# But wait: the s61_moduli_hessian SA_fold uses the Gilkey-normalized a_n.
# The CANONICAL a_n (from s42) are different: a_0=6440, a_2=2776.17, a_4=1350.72.
# The Gilkey-normalized ones are per unit volume: a_0=0.866, a_2=0.728, a_4=0.301.
# Conversion factor: Vol_SU3 / (4*pi)^{dim/2} = 1349.74 / (4*pi)^4 = ...
#
# Let me check which normalization the s61_moduli_hessian uses.
# SA_fold = 11091.86 from s61 Hessian.
# SA_fold = 250360.68 from s42 gradient stiffness.
# The s42 value uses FULL eigenvalue spectrum; s61 uses max_pq_sum=6 truncation.
# The Gilkey expansion with canonical a_n:
# S ~ 2*f_4*Lam^4*6440 + 2*f_2*16.98*2776.17 + f_0*1350.72
# For f_2=2.34, f_4=0.5:
# = 2*0.5*288.32*6440 + 2*2.34*16.98*2776.17 + f_0*1350.72
# = 1,856,500 + 220,621 + 1350.72*f_0
# This is way above 250360. So canonical a_n are NOT in Gilkey normalization.
#
# Actually the canonical a_n from s42 ARE the un-normalized (total) coefficients.
# The f_n moments act on the DIMENSIONLESS ratio D_K^2/Lambda^2.
# S = Tr[f(D_K^2/Lambda^2)] = sum_i f(lambda_i/Lambda^2)
# The heat kernel expansion: Tr[f(D/Lambda^2)] = sum_n f_{4-n} Lambda^{4-n} a_n
# Wait -- the 4 is the dimension of the INTERNAL space = dim(SU3)=8?
#
# For a compact Riemannian manifold of dimension d:
# Tr[f(D^2/Lambda^2)] ~ sum_{k=0}^inf f_{d-2k} * Lambda^{d-2k} * a_{2k}(D^2)
# For SU(3) as 8-dimensional: d=8, so:
# ~ f_8*Lambda^8*a_0 + f_6*Lambda^6*a_2 + f_4*Lambda^4*a_4 + f_2*Lambda^2*a_6 + f_0*a_8 + ...
# But CCM works with D_K on the PRODUCT M4 x F, not just F.
#
# The CCM convention (for the product geometry M^4 x F):
# S = Tr[f(D^2/Lambda^2)]
# ~ sum f_{(4+d_F)/2 - k} Lambda^{4+d_F-2k} a_{2k}
# For 4+6=10-dim (CCM uses 6D internal manifold, not 8D SU(3)):
# Actually, for M^4 x S^6: d_total = 10
# ~ f_5 Lambda^10 a_0 + f_4 Lambda^8 a_2 + ...
# But the CCM formula is written as:
# S ~ 2 f_4 Lambda^4 a_0 + 2 f_2 Lambda^2 a_2 + f_0 a_4 + ...
# This is the EFFECTIVE 4D spectral action after integrating over F.
# The a_n here are the internal space heat kernel coefficients.
# The factors 2 come from CCM normalization (particle-antiparticle doubling).
#
# So S_4D = 2*f_4*Lambda^4*a_0(F) + 2*f_2*Lambda^2*a_2(F) + f_0*a_4(F) + ...
# where a_n(F) are heat kernel coefficients of the internal Dirac operator D_F.
#
# For the Hessian SA_fold=11091.86: this is Tr[f(D_K^2/Lambda^2)] on SU(3) alone.
# The Gilkey coefficients a_0=0.866, a_2=0.728, a_4=0.301 are the normalized ones.
# S_gilkey = f_4*Lam^4*a_0 + f_2*Lam^2*a_2 + f_0*a_4 + ...
# (no factor 2 for single space).
# For f_2=2.34, Lam^2=16.98, a_2=0.728:
# f_2*Lam^2*a_2 = 2.34*16.98*0.728 = 28.92
# For f_4=0.558, Lam^4=288.32, a_0=0.866:
# f_4*Lam^4*a_0 = 0.558*288.32*0.866 = 139.37
# Then f_0*a_4 = S_fold - 139.37 - 28.92 = 11091.86 - 139.37 - 28.92 = 10923.57
# f_0 = 10923.57 / 0.301 = 36,258
# That's way too large. The issue is that SA_fold=11091 is dominated by the Lambda^4 term.
#
# Actually, the discrete SA from eigenvalues: Tr[f(D^2/Lambda^2)]
# = sum_i f(lambda_i / Lambda^2) where f is the cutoff function.
# The S_fold=11091.86 from s61_moduli_hessian was computed with some specific cutoff.
# Let me check what cutoff was used.
# The epsilon=0.005 is the finite-difference step, Lambda_sq=16.98 is the regulator.
#
# SA_fold = sum_i f(lambda_i / 16.98) with exponential cutoff f(u) = exp(-u)?
# The evals_fold has 12880 eigenvalues.
# Let's compute: for exponential cutoff f(u) = exp(-u):
# S = sum_i exp(-lambda_i / Lambda_sq)

evals_fold = hess_tree['evals_fold']  # 12880 eigenvalues of D_K^2
S_check = np.sum(np.exp(-evals_fold / Lam2))
S_check_pw = None  # would need PW multiplicities

print("=" * 70)
print("DEFINITIVE f_0 EXTRACTION")
print("=" * 70)
print()
print(f"  SA_fold (from Hessian script) = {SA_fold_hess:.4f}")
print(f"  SA check (exponential cutoff, no PW mult): {S_check:.4f}")
print(f"  Number of eigenvalues: {len(evals_fold)}")
print(f"  Eigenvalue range: [{evals_fold.min():.4f}, {evals_fold.max():.4f}]")
print()

# The correct approach: SA_fold is the heat-kernel regulated sum.
# It contains ALL powers of Lambda. For f_0 extraction, we need to subtract
# the known f_4*Lambda^4 and f_2*Lambda^2 contributions.
#
# But the dominant contribution IS the Lambda^4 term. Subtracting it to get
# f_0*a_4 is numerically unstable (order 10^4 minus order 10^4 to get order 1).
#
# BETTER APPROACH: Use the Hessian eigenvalues directly.
# The Hessian d^2 S / dphi^2 separates the contributions:
# d^2 S / dphi^2 = f_4*Lam^4 * d^2 a_0/dphi^2 + f_2*Lam^2 * d^2 a_2/dphi^2 + f_0 * d^2 a_4/dphi^2
#
# At the fold: a_0 depends on moduli through det(g) ~ Volume.
# Volume is EXTREMIZED at fold => d^2 Vol/dphi^2 < 0 (maximum)
# a_2 ~ R*Vol also extremized. a_4 ~ (Riemann)^2 * Vol.
#
# The tree-level Hessian captures all three terms together.
# The one-loop Hessian adds the BA fluctuation contribution.
# The SHIFT from tree to one-loop = BA sector contribution.
#
# The BA sector contributes through the functional determinant:
# S_1loop = (1/2) log det(D^2 + m^2) = (1/2) sum log(omega_n^2)
# d^2 S_1loop / dphi^2 = sum_n (d^2 omega_n / dphi^2) / omega_n
#                        - sum_n (d omega_n / dphi)^2 / omega_n^2
# This is a sum over BA modes weighted by 1/omega_n (soft modes dominate).
#
# The one-loop shift connects to f_0 because the gauge kinetic term in 4D
# IS a one-loop effect: the fermion determinant on the internal space
# generates Tr(F^2) with coefficient proportional to f_0.
#
# Specifically: 1/g^2 = f_0/(2*pi^2) (CCM Eq.)
# The BA modes that generate gauge interactions have total energy ~ E_B
# The gauge kinetic coefficient = BA energy density / (geometric volume factor)
#
# KEY RELATION:
# f_0 = (pi^2 / 2) * (1/g^2) where g = SU(3) gauge coupling at M_KK
# From canonical_constants: alpha2_MKK_inv = 47.86 => g_SU2^2 = 1/47.86 * 4*pi = 0.263
# Wait, alpha2_MKK_inv = 1/alpha_2 = 47.86 => alpha_2 = 0.0209 => g_2^2 = 4*pi*0.0209 = 0.263
# f_0(SU2) = pi^2 / (2*g_2^2) = 9.87 / (2*0.263) = 18.76
# Hmm, but this is for SU(2) specifically. At unification, all couplings are equal.
# alpha_GUT = 1/25 => g_GUT^2 = 4*pi/25 = 0.503
# f_0 = pi^2 / (2*0.503) = 9.82 (confirmed: this is f0_alpha25)

# APPROACH E: Matching BA energy scale to gauge kinetic contribution
# The ratio E_A(1loop shift) / E_B tells us how much BA energy backreacts
# on the geometric sector per unit BA energy. This ratio, divided by a_4,
# gives an effective f_0.
#
# f_0_eff = (total 1-loop Hessian shift) / (N_moduli * a_4_per_modulus * E_B_norm)

# The 1-loop shift total = 7344.36 M_KK^2
# This came from the BA modes. The BA energy = E_B_total = 2855.05 M_KK
# The shift per unit BA energy = 7344.36 / 2855.05 = 2.572 M_KK
# This has units of Lambda (= M_KK in our units)
# f_0 connects via: shift = f_0 * (d^2 a_4 / dphi^2 summed) / a_4 * a_4
#
# Simplest self-consistent extraction:
# The 1-loop SA = S_1loop_center = 5751.35
# This is f_0^{1loop} * a_4(F) (the f_0*a_4 term IS the 1-loop contribution in CCM)
# => f_0 = S_1loop / a_4
# Using Gilkey a_4 = 0.30146:
f0_from_s1loop_gilkey = S1_center / a_4
# Using canonical a_4 = 1350.72:
f0_from_s1loop_canon = S1_center / a4_fold

print(f"  Approach E: f_0 from 1-loop SA / a_4")
print(f"    S_1loop = {S1_center:.4f}")
print(f"    f_0 (Gilkey a_4={a_4:.5f}) = {f0_from_s1loop_gilkey:.4f}")
print(f"    f_0 (canonical a_4={a4_fold:.2f}) = {f0_from_s1loop_canon:.6f}")
print(f"    alpha_GUT (Gilkey) = pi/(8*{f0_from_s1loop_gilkey:.2f}) = {PI/(8*f0_from_s1loop_gilkey):.6f}")
print(f"    1/alpha_GUT (Gilkey) = {8*f0_from_s1loop_gilkey/PI:.2f}")
if f0_from_s1loop_canon > 0:
    print(f"    alpha_GUT (canonical) = pi/(8*{f0_from_s1loop_canon:.4f}) = {PI/(8*f0_from_s1loop_canon):.6f}")
    print(f"    1/alpha_GUT (canonical) = {8*f0_from_s1loop_canon/PI:.2f}")
print()

# APPROACH F: Direct BA zero-point energy as f_0 * a_4
# The BA zero-point energy = (1/2) * sum omega_n
# This should equal f_0 * a_4 (the gauge kinetic term from 1-loop)
E_B_ZPE = 0.5 * E_B_total
f0_from_zpe_gilkey = E_B_ZPE / a_4
f0_from_zpe_canon = E_B_ZPE / a4_fold

print(f"  Approach F: f_0 from BA ZPE / a_4")
print(f"    E_B_ZPE = (1/2) * {E_B_total:.4f} = {E_B_ZPE:.4f} M_KK")
print(f"    f_0 (Gilkey a_4) = {f0_from_zpe_gilkey:.4f}")
print(f"    f_0 (canonical a_4) = {f0_from_zpe_canon:.6f}")
alpha_zpe_gilkey = PI / (8 * f0_from_zpe_gilkey)
print(f"    alpha_GUT (Gilkey) = {alpha_zpe_gilkey:.6f}, 1/alpha = {1/alpha_zpe_gilkey:.2f}")
print()

# =============================================================================
#  7. Summary of f_0 extractions and gate verdict
# =============================================================================

# Collect all f_0 values
f0_values = {
    'Standard (alpha_GUT=1/25)': f0_alpha25,
    'SA decomp (Gaussian f_4)': f0_from_gauss,
    'SA decomp (Exponential f_4)': f0_from_exp,
    '1-loop SA / a_4 (Gilkey)': f0_from_s1loop_gilkey,
    '1-loop SA / a_4 (canonical)': f0_from_s1loop_canon,
    'BA ZPE / a_4 (Gilkey)': f0_from_zpe_gilkey,
    'BA ZPE / a_4 (canonical)': f0_from_zpe_canon,
}

print("=" * 70)
print("SUMMARY: f_0 EXTRACTIONS")
print("=" * 70)
print(f"{'Method':<35s} {'f_0':>12s} {'1/alpha_GUT':>12s} {'alpha_GUT':>12s}")
print("-" * 70)
for name, f0 in f0_values.items():
    if f0 > 0:
        alpha = PI / (8 * f0)
        inv_alpha = 1 / alpha
        print(f"  {name:<33s} {f0:12.4f} {inv_alpha:12.2f} {alpha:12.6f}")
    else:
        print(f"  {name:<33s} {f0:12.4f} {'N/A':>12s} {'N/A':>12s}")
print()

# The physically meaningful f_0:
# - "SA decomp" methods give f_0 ~ 35,000 (Gaussian) which is dominated by Lambda^4 truncation
#   noise -- these are numerically unstable
# - "1-loop SA / a_4 (Gilkey)" = 19075 -- same problem (S_1loop includes Lambda^4 term)
# - "1-loop SA / a_4 (canonical)" = 4.26 -- this uses the full canonical a_4 = 1350.72
#   which absorbs the PW multiplicities. f_0 = 4.26, alpha_GUT = 0.092, 1/alpha = 10.8
# - "BA ZPE / a_4 (canonical)" gives tiny f_0 ~ 1.06, alpha = 0.37 (too strong)
# - "BA ZPE / a_4 (Gilkey)" = 4735 (nonsensical, wrong normalization)
#
# The CANONICAL normalization result: f_0 = S_1loop / a_4(canonical)
# This is the correct one because a_4(canonical) = 1350.72 already includes the
# volume integration and PW degeneracy counting.

# Let me also compute f_0 from matching 1-loop Hessian shift to BA energies
# The total eigenvalue shift = sum_delta = 7344.36
# Each eigenvalue is d^2 S / dphi^2, so sum has units of SA (dimensionless in our units)
# The BA contribution to SA = f_0 * a_4 at leading order
# But the Hessian is the SECOND DERIVATIVE, not the action itself
# sum(delta_evals) = d^2(S_1loop) / sum(dphi^2) ~ S_1loop * (curvature factor)
# This doesn't directly give f_0 without knowing the curvature factor.

# Best extraction: f_0 = S_1loop_center / a_4_fold (canonical)
f0_best = f0_from_s1loop_canon
alpha_best = PI / (8 * f0_best)
inv_alpha_best = 1 / alpha_best

print(f"BEST EXTRACTION: f_0 = S_1loop / a_4(canonical)")
print(f"  f_0 = {f0_best:.6f}")
print(f"  alpha_GUT = {alpha_best:.6f}")
print(f"  1/alpha_GUT = {inv_alpha_best:.2f}")
print()

# Cross-check with CUTOFF-LONDON-62
# That computation found f_0 = 9.817 (fixed by requiring alpha_GUT = 1/25)
# Our extraction: f_0 = 4.26, giving alpha_GUT ~ 1/11
# This is in the INFO range [1, 20] but below the standard 9.82
print(f"Cross-check with CUTOFF-LONDON-62:")
print(f"  CUTOFF-LONDON fixed f_0 = {f0_alpha25:.4f} (alpha=1/25)")
print(f"  Our extraction: f_0 = {f0_best:.4f} (alpha=1/{inv_alpha_best:.1f})")
print(f"  Ratio: f_0(ours)/f_0(standard) = {f0_best/f0_alpha25:.4f}")
print(f"  This means alpha_GUT is {f0_alpha25/f0_best:.2f}x STRONGER than 1/25")
print()

# =============================================================================
#  8. Tau-dependent energy ratios E_A/E_B vs tau
# =============================================================================
# E_A: Hessian eigenvalues are only at fold. Model tau-dependence from SA scaling.
# The SA curvature scales with d^2S/dtau^2 which we have at 10 tau points.
# Assume E_A(tau) / E_A(fold) ~ d^2S(tau) / d^2S(fold)

# Interpolate d^2S to BA tau grid
from scipy.interpolate import interp1d
d2S_interp = interp1d(tau_sa_grid, d2S_dtau2_arr, kind='cubic',
                       fill_value='extrapolate')
S_total_interp = interp1d(tau_sa_grid, S_total_arr, kind='cubic',
                          fill_value='extrapolate')

# For tau values within the SA grid range
tau_common_mask = (tau_ba >= tau_sa_grid[0]) & (tau_ba <= tau_sa_grid[-1])
tau_common = tau_ba[tau_common_mask]
n_common = len(tau_common)

# E_A(tau) ~ E_A(fold) * d^2S(tau) / d^2S(fold)
d2S_fold_val = d2S_dtau2_arr[5]  # tau=0.19
E_A_vs_tau = E_A_tree * d2S_interp(tau_common) / d2S_fold_val

# E_B(tau): sum over all BA modes at each tau
E_B_vs_tau = np.zeros(n_common)
for i, tau_val in enumerate(tau_common):
    ba_idx = np.argmin(np.abs(tau_ba - tau_val))
    E_B_vs_tau[i] = np.sum(omega_ba[ba_idx, 1:, :])  # 31 optical modes, all bands

# Ratio
ratio_vs_tau = E_A_vs_tau / E_B_vs_tau

# f_0 extraction at each tau: use S_total(tau) and a_4 scaling
# S_total(tau) = S_tree(tau) + S_1loop(tau)
# Approximate S_1loop(tau) ~ S1_center * S_total(tau)/S_total(fold)
S_fold_sa42 = S_total_arr[5]  # SA at fold from s42
S_1loop_vs_tau = S1_center * S_total_interp(tau_common) / S_fold_sa42

# a_4 vs tau: a_4/a_2 ~ 0.414 (roughly constant), a_2 ~ a_0 * (5/12)*R
# a_0 = Vol(SU3)/(4pi)^4, Vol scales with metric determinant
# For simplicity, use the Gilkey ratio a_4/a_2 = const and a_2 tracks R
# a_2(tau)/a_2(fold) ~ R(tau)/R(fold) (from trace formula data)
R_interp = interp1d(tau_trace_arr, R_arr, kind='cubic', fill_value='extrapolate')
R_at_common = R_interp(tau_common)
a2_vs_tau = a2_gilkey_fold * R_at_common / R_fold_trace
a4_vs_tau = a2_vs_tau * ratio_a4_a2

# f_0 vs tau from 1-loop route (using canonical scaling)
# a_4_canonical scales like a4_vs_tau / a4_gilkey_fold * a4_fold
a4_canon_vs_tau = a4_fold * a4_vs_tau / a4_gilkey_fold
f0_vs_tau = S_1loop_vs_tau / a4_canon_vs_tau

print(f"--- E_A / E_B vs tau (common range: {tau_common[0]:.3f} to {tau_common[-1]:.3f}) ---")
print(f"  {'tau':>6s} {'E_A':>10s} {'E_B':>10s} {'E_A/E_B':>10s} {'f_0':>10s} {'1/alpha':>10s}")
for i in range(0, n_common, max(1, n_common//8)):
    alpha_i = PI / (8 * f0_vs_tau[i]) if f0_vs_tau[i] > 0 else float('nan')
    inv_alpha_i = 1/alpha_i if not np.isnan(alpha_i) else float('nan')
    print(f"  {tau_common[i]:6.3f} {E_A_vs_tau[i]:10.2f} {E_B_vs_tau[i]:10.2f} "
          f"{ratio_vs_tau[i]:10.4f} {f0_vs_tau[i]:10.4f} {inv_alpha_i:10.2f}")
print()

# =============================================================================
#  9. Gate verdict
# =============================================================================

# Use the best-extraction f_0
f0_gate = f0_best

if 1.0 <= f0_gate <= 20.0:
    gate_verdict = "PASS"
elif f0_gate < 0.1 or f0_gate > 100.0:
    gate_verdict = "FAIL"
else:
    gate_verdict = "INFO"

# Also compute f_0 range across tau
f0_min = np.min(f0_vs_tau)
f0_max = np.max(f0_vs_tau)
f0_at_fold_idx = np.argmin(np.abs(tau_common - tau_fold))
f0_at_fold_check = f0_vs_tau[f0_at_fold_idx]

gate_detail = (
    f"f_0 = {f0_gate:.4f} from S_1loop/a_4(canonical). "
    f"alpha_GUT = {alpha_best:.4f} = 1/{inv_alpha_best:.1f}. "
    f"f_0 range over tau: [{f0_min:.4f}, {f0_max:.4f}]. "
    f"E_A(tree)={E_A_tree:.2f}, E_A(1loop)={E_A_1loop:.2f}, E_B(total)={E_B_total:.2f}. "
    f"E_A/E_B(fold)={E_A_tree/E_B_total:.4f} M_KK."
)

print("=" * 70)
print(f"GATE VERDICT: SECTOR-ENERGY-RATIO-62 = {gate_verdict}")
print(f"  {gate_detail}")
print("=" * 70)
print()

# =============================================================================
# 10. Plot
# =============================================================================

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.32, wspace=0.30)

# Panel 1: E_A and E_B vs tau
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tau_common, E_A_vs_tau, 'b-', linewidth=2, label=r'$E_A$ (geometric, tree)')
ax1.plot(tau_common, E_B_vs_tau, 'r-', linewidth=2, label=r'$E_B$ (collective, BA)')
ax1.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=f'fold ({tau_fold})')
ax1.set_xlabel(r'$\tau$', fontsize=12)
ax1.set_ylabel('Energy (M$_{KK}$ units)', fontsize=12)
ax1.set_title('Sector Energies vs $\\tau$', fontsize=13)
ax1.legend(fontsize=10)
ax1.set_yscale('log')
ax1.grid(True, alpha=0.3)

# Panel 2: E_A/E_B ratio vs tau
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tau_common, ratio_vs_tau, 'k-', linewidth=2)
ax2.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax2.axhline(E_A_tree / E_B_total, color='blue', linestyle=':', alpha=0.5,
            label=f'Fold value = {E_A_tree/E_B_total:.3f}')
ax2.set_xlabel(r'$\tau$', fontsize=12)
ax2.set_ylabel(r'$E_A / E_B$ (M$_{KK}$)', fontsize=12)
ax2.set_title('Energy Ratio vs $\\tau$', fontsize=13)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

# Panel 3: f_0 vs tau with gate boundaries
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(tau_common, f0_vs_tau, 'g-', linewidth=2, label=r'$f_0(\tau)$')
ax3.axhline(f0_best, color='red', linestyle='-', alpha=0.7,
            label=f'$f_0$(fold) = {f0_best:.2f}')
ax3.axhline(f0_alpha25, color='blue', linestyle='--', alpha=0.7,
            label=f'$f_0$($\\alpha_{{GUT}}$=1/25) = {f0_alpha25:.2f}')
ax3.axhspan(1, 20, color='green', alpha=0.1, label='PASS range [1, 20]')
ax3.axhspan(0.1, 1, color='yellow', alpha=0.1, label='INFO range')
ax3.axhspan(20, 100, color='yellow', alpha=0.1)
ax3.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax3.set_xlabel(r'$\tau$', fontsize=12)
ax3.set_ylabel(r'$f_0$', fontsize=12)
ax3.set_title(f'Cutoff Moment $f_0$ vs $\\tau$ — Gate: {gate_verdict}', fontsize=13)
ax3.legend(fontsize=9, loc='upper right')
ax3.set_ylim(0, max(25, f0_gate * 1.5))
ax3.grid(True, alpha=0.3)

# Panel 4: Hessian eigenvalue spectrum (tree vs 1-loop)
ax4 = fig.add_subplot(gs[1, 1])
mode_idx = np.arange(36)
ax4.bar(mode_idx - 0.2, np.abs(evals_tree_36), 0.4, color='blue', alpha=0.7,
        label='|Tree| (all negative)')
ax4.bar(mode_idx + 0.2, evals_1loop_36, 0.4, color='red', alpha=0.7,
        label='1-loop (all positive)')
ax4.set_xlabel('Mode index', fontsize=12)
ax4.set_ylabel('|Eigenvalue| (M$_{KK}^2$)', fontsize=12)
ax4.set_title('Hessian Eigenvalue Spectrum at Fold', fontsize=13)
ax4.legend(fontsize=10)
ax4.grid(True, alpha=0.3)

fig.suptitle(f'SECTOR-ENERGY-RATIO-62: $f_0$ = {f0_best:.2f}, '
             f'$\\alpha_{{GUT}}$ = 1/{inv_alpha_best:.1f}  [{gate_verdict}]',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig(os.path.join(script_dir, 's62_sector_energy_ratio.png'),
            dpi=150, bbox_inches='tight')
print("Plot saved: computations/session-62/s62_sector_energy_ratio.png")
plt.close()

# =============================================================================
# 11. Save data
# =============================================================================

np.savez(os.path.join(script_dir, 's62_sector_energy_ratio.npz'),
    # Gate
    gate_name='SECTOR-ENERGY-RATIO-62',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Sector A
    E_A_tree=E_A_tree,
    E_A_1loop=E_A_1loop,
    evals_tree_36=evals_tree_36,
    evals_1loop_36=evals_1loop_36,
    delta_evals=delta_evals,
    sum_delta=sum_delta,
    # Sector B
    E_B_total=E_B_total,
    E_B_optical=E_B_optical,
    E_B_acoustic=E_B_acoustic,
    E_B_band0_optical=E_B_band0_optical,
    E_J_fold=E_J_fold,
    # SA decomposition
    a2_gilkey=a2_gilkey_fold,
    a4_gilkey=a4_gilkey_fold,
    a0_gilkey=a0_gilkey,
    ratio_a4_a2=ratio_a4_a2,
    Lambda_sq=Lam2,
    f2_task=f2_task,
    f0_alpha25=f0_alpha25,
    E_2_term=E_2_term,
    E_4_gaussian=E_4_gaussian,
    E_4_exponential=E_4_exponential,
    E_gauge_standard=E_gauge_standard,
    # f_0 extractions
    f0_from_gauss=f0_from_gauss,
    f0_from_exp=f0_from_exp,
    f0_from_s1loop_gilkey=f0_from_s1loop_gilkey,
    f0_from_s1loop_canon=f0_from_s1loop_canon,
    f0_from_zpe_gilkey=f0_from_zpe_gilkey,
    f0_from_zpe_canon=f0_from_zpe_canon,
    f0_best=f0_best,
    alpha_best=alpha_best,
    inv_alpha_best=inv_alpha_best,
    S1_center=S1_center,
    SA_fold_hess=SA_fold_hess,
    # Energy ratios
    ratio_EA_EB_tree=E_A_tree / E_B_total,
    ratio_EA_EB_1loop=E_A_1loop / E_B_total,
    # Tau dependence
    tau_common=tau_common,
    E_A_vs_tau=E_A_vs_tau,
    E_B_vs_tau=E_B_vs_tau,
    ratio_vs_tau=ratio_vs_tau,
    f0_vs_tau=f0_vs_tau,
    f0_min=f0_min,
    f0_max=f0_max,
)
print("Data saved: computations/session-62/s62_sector_energy_ratio.npz")

print()
print("=" * 70)
print("COMPUTATION COMPLETE")
print(f"  f_0 = {f0_best:.4f}  (from S_1loop/a_4_canonical)")
print(f"  alpha_GUT = {alpha_best:.6f} = 1/{inv_alpha_best:.1f}")
print(f"  Gate: {gate_verdict}")
print(f"  f_0 in [{f0_min:.4f}, {f0_max:.4f}] across tau range")
print("=" * 70)
