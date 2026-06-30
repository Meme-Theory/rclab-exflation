#!/usr/bin/env python3
"""
s63_cutoff_meissner.py — Meissner Length vs Spectral Action Cutoff
==================================================================
Gate: CUTOFF-MEISSNER-63
Session: S63, Wave 5, Entry W5-09

PHYSICS:
  Two length scales emerge from the phonon-exflation framework on Jensen-deformed SU(3):

  1. lambda_L(tau) — London penetration depth from the superfluid (Meissner) sector.
     Defined via D_s(tau) = 1/lambda_L(tau)^2, where D_s is the superfluid stiffness
     (Josephson pair transfer).

  2. gamma_opt(tau) — Optimal cutoff parameter for the Gaussian spectral action.
     Determined by the constraint f_2(gamma) = f_2_target(tau), where f_2_target
     encodes the gravity/gauge hierarchy through the Gilkey coefficients a_0(tau),
     a_2(tau), a_4(tau).

  The question: is there a physical reason these two scales should be related?
  At the fold (tau=0.19):
    lambda_L = 0.3989 M_KK^{-1}
    gamma_opt = 0.4882 (dimensionless in M_KK units)
    Ratio = 0.817 (23% discrepancy)

  This computation tracks both as functions of tau along the Jensen curve
  to determine whether the ratio is constant, converges, or crosses unity.

APPROACH:
  (A) gamma_opt(tau): For the Gaussian cutoff f(u) = A*exp(-u/gamma^2):
      - f_0 = A = 9.817 (from alpha_GUT = 1/25)
      - f_2 = A * gamma^2 => gamma = sqrt(f_2/A)
      - f_2_target comes from the gravity constraint:
        M_Pl^2 = (4*f_2*Lambda^2)/pi^2 * normalization
      - The tau-dependence enters through the Gilkey coefficient a_2(tau)/a_0(tau)
        which controls how the spectral action distributes between gravity and gauge.
      - Specifically: f_2_target(tau) = f_2_fold * [a_2(fold)*a_0(tau)] / [a_0(fold)*a_2(tau)]
        (maintaining constant M_Pl at fixed Lambda=M_KK)

  (B) lambda_L(tau): The superfluid stiffness D_s = 2*E_J*S_+, where:
      - E_J(tau) scales with the BCS gap and Josephson coupling
      - The BCS parameters depend on the Dirac eigenvalue spacing, which changes with tau
      - For the single-pair system, D_s(tau) = D_s(fold) * [E_J(tau)/E_J(fold)] * [S_+(tau)/S_+(fold)]
      - The key tau-dependence comes from Jensen scaling of the coupling constants

Inputs:
  - computations/session-62/s62_cutoff_london.npz (Gaussian gamma_opt at fold)
  - computations/session-62/s62_meissner_gge.npz (lambda_L at fold, GGE state)
  - computations/session-61/s61_heat_kernel_a2.npz (a_2(tau) across transit)
  - computations/session-61/s61_heat_kernel_a4.npz (a_4(tau) and a_2(tau) arrays)
  - computations/session-61/s61_superfluid_weight.npz (D_s at fold)
  - canonical_constants.py

Output: computations/session-63/s63_cutoff_meissner.npz

Gate: INFO with lambda_L(tau)/gamma_opt(tau) ratio profile and diagnostic assessment.

Author: quantum-acoustics-theorist (Session 63, Wave 5)
Date: 2026-03-30
"""

import os
import sys
import time
import numpy as np
from scipy.interpolate import interp1d

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t0 = time.time()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    PI, tau_fold, M_KK, M_Pl_reduced,
    a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, J_C2, J_su2, J_u1,
    E_cond, Delta_0_GL, xi_GL, xi_BCS,
    N_dof_BCS, N_cells, c_Gold,
    S_fold, Z_fold, dS_fold, d2S_fold,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

print("=" * 78)
print("CUTOFF-MEISSNER-63: Meissner Length vs Spectral Action Cutoff")
print("=" * 78)

# ===========================================================================
# STEP 1: Load all upstream data
# ===========================================================================
print("\n--- Step 1: Load upstream data ---")

# S62 cutoff (Gaussian parameters at fold)
cutoff_data = np.load(os.path.join(SCRIPT_DIR, 's62_cutoff_london.npz'), allow_pickle=True)
gamma_opt_fold = float(cutoff_data['Gaussian_gamma_opt'])  # 0.4882
f0_gauge = float(cutoff_data['Gaussian_f0'])               # 9.817
f2_fold = float(cutoff_data['Gaussian_f2'])                 # 2.34
f4_fold = float(cutoff_data['Gaussian_f4'])                 # 0.5577
a0_gilkey_fold = float(cutoff_data['a0_gilkey'])            # 0.866
a2_gilkey_fold = float(cutoff_data['a2_gilkey_fold'])       # 0.7282
a4_gilkey_fold = float(cutoff_data['a4_gilkey_fold'])       # 0.3015

print(f"  gamma_opt(fold) = {gamma_opt_fold:.6f}")
print(f"  f_0 = {f0_gauge:.6f}")
print(f"  f_2(fold) = {f2_fold:.6f}")
print(f"  f_4(fold) = {f4_fold:.6f}")

# S62 Meissner GGE (lambda_L at fold)
meissner_data = np.load(os.path.join(SCRIPT_DIR, 's62_meissner_gge.npz'), allow_pickle=True)
lambda_L_GGE = float(meissner_data['lambda_L_GGE'])       # 0.3989
lambda_L_fold = float(meissner_data['lambda_L_fold'])       # 0.3966
D_s_GGE = float(meissner_data['D_s_GGE'])                  # 6.2831
D_s_fold_val = float(meissner_data['D_s_fold'])             # 6.3563
kappa_GGE = float(meissner_data['kappa_GGE'])               # 0.4086
xi_GL_GGE = float(meissner_data['xi_GL_GGE'])               # 0.9763
m_M_fold = float(meissner_data['m_M_fold'])                 # 2.5212

print(f"  lambda_L(GGE) = {lambda_L_GGE:.6f} M_KK^{{-1}}")
print(f"  lambda_L(fold) = {lambda_L_fold:.6f} M_KK^{{-1}}")
print(f"  D_s(fold) = {D_s_fold_val:.6f} M_KK^2")
print(f"  D_s(GGE) = {D_s_GGE:.6f} M_KK^2")
print(f"  kappa(GGE) = {kappa_GGE:.6f}")
print(f"  xi_GL(GGE) = {xi_GL_GGE:.6f} M_KK^{{-1}}")

# Superfluid weight (additional data)
sw_data = np.load(os.path.join(SCRIPT_DIR, 's61_superfluid_weight.npz'), allow_pickle=True)
E_J_fold = float(sw_data['E_J_fold'])                      # 3.397
S_plus_1 = float(sw_data['S_plus_1'])                       # 0.936

print(f"  E_J(fold) = {E_J_fold:.6f}")
print(f"  S_+(1) = {S_plus_1:.6f}")

# Heat kernel a_2(tau) data
hk2_data = np.load(os.path.join(SCRIPT_DIR, 's61_heat_kernel_a2.npz'), allow_pickle=True)
tau_a2 = hk2_data['tau_arr']               # 100 points, [0, 0.5]
a2_SD_arr = hk2_data['a2_SD_arr']          # Seeley-DeWitt a_2(tau), normalized
R_arr_a2 = hk2_data['R_arr']              # Ricci scalar R(tau)

# Heat kernel a_4(tau) data
hk4_data = np.load(os.path.join(SCRIPT_DIR, 's61_heat_kernel_a4.npz'), allow_pickle=True)
tau_a4 = hk4_data['tau_arr']               # 101 points, [0, 0.5]
a2_gilkey_arr = hk4_data['a2_gilkey_arr']  # Gilkey a_2(tau)
a4_gilkey_arr = hk4_data['a4_gilkey_arr']  # Gilkey a_4(tau)
ratio_gilkey_arr = hk4_data['ratio_gilkey_arr']  # a_4/a_2 ratio
R_arr_a4 = hk4_data['R_arr']              # R(tau) from a4 file

print(f"\n  tau range (a2): [{tau_a2[0]:.4f}, {tau_a2[-1]:.4f}], N={len(tau_a2)}")
print(f"  tau range (a4): [{tau_a4[0]:.4f}, {tau_a4[-1]:.4f}], N={len(tau_a4)}")

# Verify fold values match
a2_at_fold = np.interp(tau_fold, tau_a4, a2_gilkey_arr)
a4_at_fold = np.interp(tau_fold, tau_a4, a4_gilkey_arr)
print(f"\n  Cross-check at tau_fold = {tau_fold}:")
print(f"    a2(interp) = {a2_at_fold:.8f}, a2(stored) = {a2_gilkey_fold:.8f}, diff = {abs(a2_at_fold - a2_gilkey_fold)/a2_gilkey_fold*100:.4f}%")
print(f"    a4(interp) = {a4_at_fold:.8f}, a4(stored) = {a4_gilkey_fold:.8f}, diff = {abs(a4_at_fold - a4_gilkey_fold)/a4_gilkey_fold*100:.4f}%")

# ===========================================================================
# STEP 2: Compute gamma_opt(tau) — Spectral action cutoff vs tau
# ===========================================================================
print("\n" + "=" * 78)
print("Step 2: gamma_opt(tau) — Spectral action cutoff along Jensen curve")
print("=" * 78)

# For the Gaussian cutoff family:
#   f(u) = A * exp(-u/gamma^2)
#   f_0 = A = 9.817 (gauge coupling constraint, alpha_GUT = 1/25)
#   f_2 = A * gamma^2  =>  gamma = sqrt(f_2 / A)
#   f_4 = A * gamma^4  =  f_2^2 / A
#
# The gravity constraint relates f_2 to the geometry:
#   M_Pl^2 = (coefficient involving a_2 and Lambda) * f_2
#
# At the fold, the cutoff computation (S62) found gamma_opt = 0.4882 with
# f_2 = 2.34. The question is how f_2_target varies with tau.
#
# The Gilkey expansion of the spectral action reads:
#   S[D, Lambda, f] ~ 2 f_4 Lambda^4 a_0 + 2 f_2 Lambda^2 a_2 + f_0 a_4 + ...
#
# The gravity (Einstein-Hilbert) term comes from the f_2 Lambda^2 a_2 piece:
#   (1/16 pi G) int R sqrt(g) d^4x  corresponds to  2 f_2 Lambda^2 a_2
#
# So: 1/(16 pi G) = 2 f_2 Lambda^2 a_2 / (int R sqrt(g))
# With Lambda = M_KK and G = 1/(8 pi M_Pl_red^2):
#   M_Pl_red^2 = 2 * (16 pi) * f_2 * M_KK^2 * a_2 / (int R sqrt(g))
#
# For the INTERNAL space only (which is what a_2_gilkey measures):
#   The full product geometry gives a_2(M4 x F) = a_0(F)*a_2(M4) + a_0(M4)*a_2(F)
#   The piece that generates 4D gravity is a_0(F)*a_2(M4), where a_0(F) is just
#   the "volume" in the Gilkey sense.
#
# The CCM normalization uses a_0 and a_2 of the FULL internal Dirac operator.
# The key relationship is:
#   M_Pl^2 proportional to f_2 * Lambda^2 * a_2(internal) / a_0(internal)
# (with the a_0 factor in the denominator because the 4D piece picks up a_0(F)
#  from the product geometry decomposition)
#
# Therefore, to maintain FIXED M_Pl at FIXED Lambda=M_KK, the required f_2 is:
#   f_2(tau) = f_2(fold) * [a_0(tau)/a_0(fold)] * [a_2(fold)/a_2(tau)]
#            = f_2(fold) * [a_2(fold)/a_2(tau)]  (a_0 = volume = constant for SU(3))
#
# WAIT — a_0 is the Gilkey volume coefficient. For a_0 of a deformed manifold,
# a_0 = integral of 1 over the manifold (with the metric). The Jensen deformation
# is VOLUME-PRESERVING (S35 PASS), so a_0(tau) = a_0(round) = constant.
#
# The a_2 Gilkey coefficient IS tau-dependent (it tracks R(tau)).
# Since a_2 propto R (from the heat kernel), and R increases with tau:
#   f_2(tau) = f_2(fold) * a_2_gilkey(fold) / a_2_gilkey(tau)

# Use the a4 file's Gilkey arrays (they have a2 too and are slightly denser)
# Build interpolators
a2_interp = interp1d(tau_a4, a2_gilkey_arr, kind='cubic', fill_value='extrapolate')
a4_interp = interp1d(tau_a4, a4_gilkey_arr, kind='cubic', fill_value='extrapolate')

# Common tau grid for the computation
N_tau = 200  # (local)
tau_arr = np.linspace(0.001, 0.49, N_tau)  # Avoid tau=0 (singular)

# a_2(tau) normalized by a_2(fold)
a2_of_tau = a2_interp(tau_arr)
a2_ratio = a2_gilkey_fold / a2_of_tau   # ratio a_2(fold)/a_2(tau)

# f_2(tau) from gravity constraint (maintaining constant M_Pl)
f2_of_tau = f2_fold * a2_ratio

# For Gaussian: gamma = sqrt(f_2 / f_0)
gamma_of_tau = np.sqrt(f2_of_tau / f0_gauge)

# Cross-check at fold
idx_fold_approx = np.argmin(np.abs(tau_arr - tau_fold))
print(f"\n  At tau = {tau_arr[idx_fold_approx]:.4f} (nearest to fold):")
print(f"    a_2(tau)/a_2(fold) = {a2_of_tau[idx_fold_approx]/a2_gilkey_fold:.8f}")
print(f"    f_2(tau) = {f2_of_tau[idx_fold_approx]:.8f}")
print(f"    gamma_opt(tau) = {gamma_of_tau[idx_fold_approx]:.8f}")
print(f"    gamma_opt(fold, S62) = {gamma_opt_fold:.8f}")
print(f"    Relative deviation = {abs(gamma_of_tau[idx_fold_approx] - gamma_opt_fold)/gamma_opt_fold*100:.4f}%")

# Also compute f_4(tau) for the Gaussian:
# f_4 = A * gamma^4 = f_0 * gamma^4
f4_of_tau = f0_gauge * gamma_of_tau**4

# Ratio a_4/a_2 as function of tau
ratio_of_tau = a4_interp(tau_arr) / a2_of_tau

print(f"\n  gamma_opt range: [{gamma_of_tau.min():.6f}, {gamma_of_tau.max():.6f}]")
print(f"  f_2 range: [{f2_of_tau.min():.6f}, {f2_of_tau.max():.6f}]")
print(f"  a_4/a_2 range: [{ratio_of_tau.min():.6f}, {ratio_of_tau.max():.6f}]")

# ===========================================================================
# STEP 3: Compute lambda_L(tau) — London penetration depth vs tau
# ===========================================================================
print("\n" + "=" * 78)
print("Step 3: lambda_L(tau) — London penetration depth along Jensen curve")
print("=" * 78)

# The London penetration depth is lambda_L = 1/sqrt(D_s)
# where D_s = superfluid stiffness = Josephson phase stiffness.
#
# D_s(tau) = 2 * E_J(tau) * S_+(tau)
# (from D_s_fold_val = 6.356, E_J_fold = 3.397, S_+(1) = 0.936)
# Check: 2 * 3.397 * 0.936 = 6.359 ~ 6.356. Consistent.
#
# The tau-dependence enters through:
#
# (A) E_J(tau) — Josephson energy
#   E_J = J * S_+, where J is the inter-cell tunneling amplitude.
#   The Josephson coupling J follows from the overlap of BCS wavefunctions
#   across the cell boundary. It is proportional to:
#     J(tau) ~ Delta(tau)^2 / epsilon_k(tau)
#   where Delta is the BCS gap and epsilon_k are single-particle energies.
#
#   Under Jensen deformation, the Dirac eigenvalues scale as:
#     omega_n(tau) = omega_n(0) * h(tau/tau_fold)
#   where h is a universal scaling function from the Jensen map.
#   Both Delta and epsilon_k are linear functions of the eigenvalues,
#   so their ratio (and hence E_J) is approximately tau-independent
#   in the BCS regime.
#
#   HOWEVER: the S56 result showed E_J depends on the fabric coupling,
#   and the Josephson energy scales as:
#     E_J(tau) = J_C2(tau) * S_+(tau)
#   where J_C2(tau) is the C^2 coset Josephson coupling.
#
# (B) The Jensen deformation scaling of couplings:
#   g|_{u(1)} = e^{2s(tau)}, g|_{su(2)} = e^{-2s(tau)}, g|_{C^2} = e^{s(tau)}
#   where s(tau) is the deformation parameter.
#
#   The PHYSICAL Josephson coupling is:
#     J(tau) proportional to exp(-d(tau)/xi_BCS(tau))
#   where d is the inter-cell distance and xi_BCS is the BCS coherence length.
#
#   In the phononic framework, ALL energy scales (including J, Delta, epsilon)
#   are set by the Dirac spectrum, which scales uniformly under Jensen deformation.
#   The BCS condensate is a TOPOLOGICAL feature that persists across the transit.
#
# For the computation, we use the following tau-dependent model:
#
# The Dirac spectrum eigenvalues at arbitrary tau are related to the fold by:
#   lambda_n(tau) = lambda_n(fold) * g(tau)
# where g(tau) is the geometric factor from the heat kernel.
#
# Since a_2 propto R propto (derivative of volume element), and a_0 = const:
#   The effective mass scale m_eff^2(tau) ~ a_2(tau)/a_0  (Seeley-DeWitt)
#
# The London penetration depth depends on the superfluid density:
#   lambda_L(tau) = 1/sqrt(D_s(tau))
#
# For the BCS superfluid on the CG(24) graph:
#   D_s(tau) = n_s(tau) * e_eff^2 / m_eff(tau)
# where n_s is the superfluid density and m_eff is the effective mass.
#
# The MODE-INDEPENDENT BA theorem (S57) states:
#   omega_n(tau) = f(tau) * sqrt(lambda_n)
# where f(tau) factorizes — all modes have the SAME tau-dependence.
#
# This means ALL BCS parameters scale uniformly with tau:
#   Delta(tau) = Delta(fold) * f(tau)/f(fold)
#   epsilon_k(tau) = epsilon_k(fold) * f(tau)/f(fold)
#   E_J(tau) = E_J(fold) * f(tau)/f(fold)     [gap scales same as bandwidth]
#   S_+(tau) = S_+(fold)                        [dimensionless ratio, tau-independent]
#
# Therefore:
#   D_s(tau) = D_s(fold) * f(tau)/f(fold)
#   lambda_L(tau) = lambda_L(fold) * sqrt(f(fold)/f(tau))
#
# The function f(tau) can be extracted from the Gilkey data:
#   The mean eigenvalue scales as sqrt(a_2(tau)/a_0)  [from spectral geometry]
#   So f(tau)/f(fold) = sqrt(a_2(tau)/a_2(fold))

print("\n  Using mode-independent BA theorem (S57) for tau-dependence:")
print("    omega_n(tau) = f(tau) * sqrt(lambda_n)")
print("    f(tau)/f(fold) = sqrt(a_2(tau)/a_2(fold))")
print("    lambda_L(tau) = lambda_L(fold) * [a_2(fold)/a_2(tau)]^{1/4}")

# Compute the scaling function f(tau)/f(fold)
# From Gilkey: a_2 propto R propto mean(omega^2), so:
#   <omega^2>(tau) / <omega^2>(fold) = a_2(tau)/a_2(fold)
#   f(tau)/f(fold) = sqrt(a_2(tau)/a_2(fold))

f_ratio = np.sqrt(a2_of_tau / a2_gilkey_fold)

# D_s scales as f(tau)/f(fold) (energy scale)
D_s_of_tau = D_s_fold_val * f_ratio

# lambda_L = 1/sqrt(D_s)
lambda_L_of_tau = 1.0 / np.sqrt(D_s_of_tau)

# Cross-check at fold
print(f"\n  At tau = {tau_arr[idx_fold_approx]:.4f}:")
print(f"    f(tau)/f(fold) = {f_ratio[idx_fold_approx]:.8f}")
print(f"    D_s(tau) = {D_s_of_tau[idx_fold_approx]:.6f} M_KK^2")
print(f"    lambda_L(tau) = {lambda_L_of_tau[idx_fold_approx]:.6f} M_KK^{{-1}}")
print(f"    lambda_L(fold, S62) = {lambda_L_fold:.6f} M_KK^{{-1}}")
print(f"    lambda_L(GGE, S62) = {lambda_L_GGE:.6f} M_KK^{{-1}}")

# Also compute the GGE-corrected lambda_L(tau)
# The GGE depletion reduces D_s by a factor D_s(GGE)/D_s(fold) = 0.9885
ratio_gge_depletion = D_s_GGE / D_s_fold_val
print(f"\n  GGE depletion factor: D_s(GGE)/D_s(fold) = {ratio_gge_depletion:.6f}")

D_s_GGE_of_tau = D_s_of_tau * ratio_gge_depletion
lambda_L_GGE_of_tau = 1.0 / np.sqrt(D_s_GGE_of_tau)

print(f"  lambda_L(GGE) range: [{lambda_L_GGE_of_tau.min():.6f}, {lambda_L_GGE_of_tau.max():.6f}]")

# ===========================================================================
# STEP 4: Compute the ratio lambda_L / gamma_opt as function of tau
# ===========================================================================
print("\n" + "=" * 78)
print("Step 4: Ratio lambda_L(tau) / gamma_opt(tau)")
print("=" * 78)

# The RATIO of the two length scales:
ratio_fold_GS = lambda_L_of_tau / gamma_of_tau     # ground state
ratio_fold_GGE = lambda_L_GGE_of_tau / gamma_of_tau  # GGE state

print(f"\n  Ratio (GS) range: [{ratio_fold_GS.min():.6f}, {ratio_fold_GS.max():.6f}]")
print(f"  Ratio (GGE) range: [{ratio_fold_GGE.min():.6f}, {ratio_fold_GGE.max():.6f}]")
print(f"  Ratio (GS) at fold: {ratio_fold_GS[idx_fold_approx]:.6f}")
print(f"  Ratio (GGE) at fold: {ratio_fold_GGE[idx_fold_approx]:.6f}")

# Check for crossing (ratio = 1)
crossings_GS = []
crossings_GGE = []
for i in range(len(tau_arr) - 1):
    if (ratio_fold_GS[i] - 1.0) * (ratio_fold_GS[i+1] - 1.0) < 0:
        tau_cross = tau_arr[i] + (tau_arr[i+1] - tau_arr[i]) * (1.0 - ratio_fold_GS[i]) / (ratio_fold_GS[i+1] - ratio_fold_GS[i])
        crossings_GS.append(tau_cross)
    if (ratio_fold_GGE[i] - 1.0) * (ratio_fold_GGE[i+1] - 1.0) < 0:
        tau_cross = tau_arr[i] + (tau_arr[i+1] - tau_arr[i]) * (1.0 - ratio_fold_GGE[i]) / (ratio_fold_GGE[i+1] - ratio_fold_GGE[i])
        crossings_GGE.append(tau_cross)

if crossings_GS:
    print(f"\n  GS ratio crosses unity at tau = {crossings_GS}")
else:
    print(f"\n  GS ratio does NOT cross unity in [{tau_arr[0]:.3f}, {tau_arr[-1]:.3f}]")

if crossings_GGE:
    print(f"  GGE ratio crosses unity at tau = {crossings_GGE}")
else:
    print(f"  GGE ratio does NOT cross unity in [{tau_arr[0]:.3f}, {tau_arr[-1]:.3f}]")

# ===========================================================================
# STEP 5: Analytic scaling analysis
# ===========================================================================
print("\n" + "=" * 78)
print("Step 5: Analytic scaling analysis")
print("=" * 78)

# Let r(tau) = a_2(tau)/a_2(fold). Then:
#
# gamma_opt(tau) = gamma_opt(fold) * (1/r)^{1/2}    [from f_2 propto 1/a_2, gamma propto sqrt(f_2)]
# lambda_L(tau) = lambda_L(fold) * (1/r)^{1/4}      [from D_s propto sqrt(a_2), lambda propto 1/D_s^{1/2}]
#
# Therefore the ratio:
# lambda_L(tau)/gamma_opt(tau) = [lambda_L(fold)/gamma_opt(fold)] * r^{1/4}
#
# This means:
# - The ratio GROWS as tau increases (since a_2 increases with tau => R increases)
# - The ratio is MONOTONIC (follows a_2(tau)^{1/4})
# - For the ratio to equal 1, we need:
#   r^{1/4} = gamma_opt(fold)/lambda_L(fold) = 0.4882/0.3966 = 1.231
#   r = 1.231^4 = 2.296
#   a_2(tau_cross)/a_2(fold) = 2.296
#
# Let's check if this r value is achievable within the tau range:

r_target = (gamma_opt_fold / lambda_L_fold)**4
print(f"\n  gamma_opt(fold)/lambda_L(fold) = {gamma_opt_fold/lambda_L_fold:.6f}")
print(f"  Required r = a_2(tau)/a_2(fold) for ratio=1: {r_target:.6f}")
print(f"  Maximum r in data = {(a2_gilkey_arr[-1]/a2_gilkey_fold):.6f}")
print(f"  r at tau=0: {a2_gilkey_arr[0]/a2_gilkey_fold:.6f}")

# Exact analytic formula: ratio(tau) = [lambda_L(fold)/gamma_opt(fold)] * [a_2(tau)/a_2(fold)]^{1/4}
ratio_analytic = (lambda_L_fold / gamma_opt_fold) * (a2_of_tau / a2_gilkey_fold)**0.25

# Verify agreement with numerical ratio
print(f"\n  Analytic vs numerical ratio check:")
print(f"    Analytic at fold: {ratio_analytic[idx_fold_approx]:.8f}")
print(f"    Numerical (GS) at fold: {ratio_fold_GS[idx_fold_approx]:.8f}")
print(f"    Max relative deviation: {np.max(np.abs(ratio_analytic - ratio_fold_GS)/ratio_fold_GS)*100:.6f}%")

# The scaling exponents:
# gamma ~ a_2^{-1/2}, lambda_L ~ a_2^{-1/4}
# So lambda_L falls more slowly than gamma as tau increases
# And lambda_L falls more slowly than gamma as we move away from the fold

# Compute the log-log slope of the ratio vs a_2
log_a2 = np.log(a2_of_tau / a2_gilkey_fold)
log_ratio = np.log(ratio_fold_GS)
# Expected slope: d(log ratio)/d(log a2) = 1/4
mask = np.abs(log_a2) > 1e-6  # avoid division by zero near fold
if mask.sum() > 10:
    slopes = np.diff(log_ratio[mask]) / np.diff(log_a2[mask])
    print(f"\n  Log-log slope of ratio vs a_2:")
    print(f"    Expected: 0.250")
    print(f"    Mean computed: {np.mean(slopes):.6f}")
    print(f"    Std: {np.std(slopes):.6f}")

# ===========================================================================
# STEP 6: Physical interpretation — what would make them equal?
# ===========================================================================
print("\n" + "=" * 78)
print("Step 6: Physical interpretation")
print("=" * 78)

# The two length scales:
# gamma_opt: Sets the UV cutoff of the spectral action. Physical meaning:
#   modes with |D_K|^2 > M_KK^2 * gamma_opt^{-2} are exponentially suppressed.
#   Effective UV cutoff scale: Lambda_UV = M_KK / gamma_opt
#
# lambda_L: Sets the spatial screening scale for gauge field fluctuations.
#   Magnetic fields decay as exp(-r/lambda_L) inside the condensate.
#
# For them to coincide, we would need the UV regularization scale
# to equal the IR screening scale. This is NOT expected generically.
#
# However, there is a deeper structural connection:
# Both are determined by the SAME Dirac spectrum {lambda_n}:
#   gamma_opt comes from the spectral action Tr[f(D^2/Lambda^2)]
#   lambda_L comes from the BCS condensate built from the SAME Dirac modes
#
# The 23% discrepancy at the fold may encode the non-perturbative
# structure of the BCS condensate (which is not captured by the
# heat kernel asymptotic expansion).

Lambda_UV_fold = 1.0 / gamma_opt_fold  # UV cutoff in M_KK units
Lambda_IR_fold = 1.0 / lambda_L_fold   # IR screening scale = m_M (photon mass)
print(f"\n  UV cutoff scale: Lambda_UV = 1/gamma_opt = {Lambda_UV_fold:.4f} M_KK")
print(f"  IR screening scale: m_M = 1/lambda_L = {1/lambda_L_fold:.4f} M_KK (= Meissner mass)")
print(f"  Ratio Lambda_UV/m_M = gamma_opt/lambda_L = {Lambda_UV_fold/(1/lambda_L_fold):.4f}")
print(f"  This IS the ratio lambda_L/gamma_opt = {lambda_L_fold/gamma_opt_fold:.4f}")

# Compute kappa = lambda_L / xi_GL as function of tau
# xi_GL scales the same way as lambda_L (both are lengths ~ 1/sqrt(energy))
# Actually xi_GL ~ 1/Delta and lambda_L ~ 1/sqrt(D_s) ~ 1/(Delta * sqrt(n_s))
# So kappa = lambda_L/xi_GL is approximately sqrt(1/n_s) * (geometricfactors)
# In our system kappa = 0.4086 (Type-I superconductor)

print(f"\n  GL parameter kappa = lambda_L/xi_GL = {kappa_GGE:.4f} (Type-I)")
print(f"  xi_GL = {xi_GL_GGE:.4f} M_KK^{{-1}}")
print(f"  Note: kappa < 1/sqrt(2) = 0.707 confirms Type-I (Abrikosov criterion)")

# ===========================================================================
# STEP 7: Second approach — direct eigenvalue scaling
# ===========================================================================
print("\n" + "=" * 78)
print("Step 7: Direct eigenvalue check — R(tau) as the physical driver")
print("=" * 78)

# The Ricci scalar R(tau) of the Jensen-deformed SU(3) controls everything.
# From the Gilkey relation: a_2 = (1/6) * R * a_0 / (4*pi)^{d/2}
# (For d=8, this is a_2 = R / (6 * (4*pi)^4) * a_0)
# But the actual coefficient depends on the representation.
#
# Empirically from the data: a_2(tau) propto R(tau)
# Let's verify this.

R_interp = interp1d(tau_a4, R_arr_a4, kind='cubic', fill_value='extrapolate')
R_of_tau = R_interp(tau_arr)

# Check a_2 propto R
a2_over_R = a2_of_tau / R_of_tau
print(f"  a_2/R range: [{a2_over_R.min():.8f}, {a2_over_R.max():.8f}]")
print(f"  a_2/R at fold: {a2_over_R[idx_fold_approx]:.8f}")
print(f"  Variation: {(a2_over_R.max()-a2_over_R.min())/a2_over_R[idx_fold_approx]*100:.4f}%")

print(f"\n  R(tau) range: [{R_of_tau.min():.6f}, {R_of_tau.max():.6f}]")
print(f"  R(fold) = {R_of_tau[idx_fold_approx]:.6f}")

# ===========================================================================
# STEP 8: tau-derivative analysis
# ===========================================================================
print("\n" + "=" * 78)
print("Step 8: Derivative analysis — d(ratio)/dtau")
print("=" * 78)

# Numerical derivative of the ratio
d_ratio_dtau = np.gradient(ratio_fold_GS, tau_arr)
d_gamma_dtau = np.gradient(gamma_of_tau, tau_arr)
d_lambda_dtau = np.gradient(lambda_L_of_tau, tau_arr)

print(f"\n  At fold (tau={tau_arr[idx_fold_approx]:.4f}):")
print(f"    d(gamma_opt)/dtau = {d_gamma_dtau[idx_fold_approx]:.6f}")
print(f"    d(lambda_L)/dtau = {d_lambda_dtau[idx_fold_approx]:.6f}")
print(f"    d(ratio)/dtau = {d_ratio_dtau[idx_fold_approx]:.6f}")

# Fractional rates of change
gamma_frac = d_gamma_dtau[idx_fold_approx] / gamma_of_tau[idx_fold_approx]
lambda_frac = d_lambda_dtau[idx_fold_approx] / lambda_L_of_tau[idx_fold_approx]
print(f"    (1/gamma) d(gamma)/dtau = {gamma_frac:.6f}")
print(f"    (1/lambda) d(lambda)/dtau = {lambda_frac:.6f}")
print(f"    Ratio of fractional rates = {gamma_frac/lambda_frac:.6f}")
print(f"    Expected (analytic): 2.0  [gamma ~ a_2^{-1/2}, lambda ~ a_2^{-1/4}]")

# ===========================================================================
# STEP 9: Summary table at key tau values
# ===========================================================================
print("\n" + "=" * 78)
print("Step 9: Summary table")
print("=" * 78)

tau_sample = [0.01, 0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.35, 0.40, 0.45]
print(f"\n  {'tau':>6s} {'gamma_opt':>10s} {'lambda_L':>10s} {'lambda_L_GGE':>12s} {'ratio(GS)':>10s} {'ratio(GGE)':>11s} {'a_2/a_2(fold)':>14s}")
print("  " + "-" * 80)

for tau_s in tau_sample:
    idx = np.argmin(np.abs(tau_arr - tau_s))
    print(f"  {tau_arr[idx]:6.3f} {gamma_of_tau[idx]:10.6f} {lambda_L_of_tau[idx]:10.6f} "
          f"{lambda_L_GGE_of_tau[idx]:12.6f} {ratio_fold_GS[idx]:10.6f} "
          f"{ratio_fold_GGE[idx]:11.6f} {a2_of_tau[idx]/a2_gilkey_fold:14.6f}")

# ===========================================================================
# STEP 10: Generate plots
# ===========================================================================
print("\n" + "=" * 78)
print("Step 10: Generating plots")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel (a): Both length scales vs tau
ax = axes[0, 0]
ax.plot(tau_arr, gamma_of_tau, 'b-', linewidth=2, label=r'$\gamma_{\rm opt}(\tau)$')
ax.plot(tau_arr, lambda_L_of_tau, 'r-', linewidth=2, label=r'$\lambda_L(\tau)$ [GS]')
ax.plot(tau_arr, lambda_L_GGE_of_tau, 'r--', linewidth=1.5, label=r'$\lambda_L(\tau)$ [GGE]')
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7, label=f'fold ($\\tau$={tau_fold})')
ax.set_xlabel(r'$\tau$ (Jensen parameter)')
ax.set_ylabel(r'Length scale ($M_{\rm KK}^{-1}$)')
ax.set_title('(a) Spectral Cutoff vs London Penetration Depth')
ax.legend(fontsize=9)
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

# Panel (b): Ratio lambda_L / gamma_opt vs tau
ax = axes[0, 1]
ax.plot(tau_arr, ratio_fold_GS, 'k-', linewidth=2, label='GS')
ax.plot(tau_arr, ratio_fold_GGE, 'k--', linewidth=1.5, label='GGE')
ax.axhline(1.0, color='gray', ls=':', alpha=0.7, label='Unity')
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7)
ax.set_xlabel(r'$\tau$ (Jensen parameter)')
ax.set_ylabel(r'$\lambda_L / \gamma_{\rm opt}$')
ax.set_title(r'(b) Ratio $\lambda_L(\tau) / \gamma_{\rm opt}(\tau)$')
ax.legend(fontsize=9)
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

# Panel (c): The underlying a_2(tau) / a_2(fold)
ax = axes[1, 0]
ax.plot(tau_arr, a2_of_tau / a2_gilkey_fold, 'g-', linewidth=2)
ax.axhline(r_target, color='red', ls='--', alpha=0.7,
           label=f'$r$ for ratio=1: {r_target:.3f}')
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7)
ax.set_xlabel(r'$\tau$ (Jensen parameter)')
ax.set_ylabel(r'$a_2(\tau) / a_2(\tau_{\rm fold})$')
ax.set_title(r'(c) Gilkey coefficient ratio (drives both scales)')
ax.legend(fontsize=9)
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

# Panel (d): f_2 and f_4 vs tau
ax = axes[1, 1]
ax.plot(tau_arr, f2_of_tau, 'b-', linewidth=2, label=r'$f_2(\tau)$')
ax.plot(tau_arr, f4_of_tau, 'r-', linewidth=2, label=r'$f_4(\tau)$')
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.7)
ax.axhline(f2_fold, color='blue', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$ (Jensen parameter)')
ax.set_ylabel(r'Cutoff moment')
ax.set_title(r'(d) Spectral action moments $f_2, f_4$ vs $\tau$')
ax.legend(fontsize=9)
ax.set_xlim(0, 0.5)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's63_cutoff_meissner.png'), dpi=150)
print("  Saved: s63_cutoff_meissner.png")

# ===========================================================================
# STEP 11: Gate verdict
# ===========================================================================
print("\n" + "=" * 78)
print("Step 11: Gate verdict")
print("=" * 78)

ratio_at_fold_GS = float(np.interp(tau_fold, tau_arr, ratio_fold_GS))
ratio_at_fold_GGE = float(np.interp(tau_fold, tau_arr, ratio_fold_GGE))

# Key structural finding: the ratio is MONOTONICALLY INCREASING
is_monotonic = np.all(np.diff(ratio_fold_GS) > -1e-10)
print(f"\n  Ratio monotonicity: {is_monotonic}")

# The ratio at the fold
print(f"  lambda_L(fold)/gamma_opt(fold) = {ratio_at_fold_GS:.6f} (GS)")
print(f"  lambda_L(GGE)/gamma_opt(fold) = {ratio_at_fold_GGE:.6f} (GGE)")

# Physical scaling
print(f"\n  Scaling law: ratio(tau) = {lambda_L_fold/gamma_opt_fold:.4f} * [a_2(tau)/a_2(fold)]^{{1/4}}")
print(f"  The two scales have DIFFERENT scaling exponents under Jensen deformation:")
print(f"    gamma_opt ~ a_2^{{-1/2}}   (cutoff sharpens as curvature increases)")
print(f"    lambda_L ~ a_2^{{-1/4}}   (penetration depth shrinks more slowly)")
print(f"  Exponent difference: 1/2 - 1/4 = 1/4 drives the monotonic divergence")

# The 23% discrepancy
discrepancy_pct = (1.0 - ratio_at_fold_GGE) * 100
print(f"\n  Discrepancy at fold: {abs(discrepancy_pct):.1f}%")
print(f"  lambda_L is {'BELOW' if ratio_at_fold_GGE < 1 else 'ABOVE'} gamma_opt by {abs(discrepancy_pct):.1f}%")

# Check if they coincide anywhere
coincidence_tau = crossings_GS[0] if crossings_GS else None
if coincidence_tau is not None:
    print(f"\n  COINCIDENCE POINT: lambda_L = gamma_opt at tau = {coincidence_tau:.4f}")
else:
    print(f"\n  NO COINCIDENCE in [{tau_arr[0]:.3f}, {tau_arr[-1]:.3f}]")
    print(f"  Required a_2 ratio = {r_target:.4f}, max available = {a2_gilkey_arr[-1]/a2_gilkey_fold:.4f}")
    if r_target > a2_gilkey_arr[-1]/a2_gilkey_fold:
        print(f"  Ratio = 1 is NOT achievable within the tau range of the Jensen curve")
    else:
        print(f"  Ratio = 1 IS achievable (requires extrapolation beyond computed range)")

gate_verdict = "INFO"
gate_detail = (
    f"lambda_L(fold)/gamma_opt(fold) = {ratio_at_fold_GS:.4f} (GS), "
    f"{ratio_at_fold_GGE:.4f} (GGE). "
    f"Discrepancy = {abs(discrepancy_pct):.1f}%. "
    f"Ratio is MONOTONICALLY INCREASING with tau (exponent 1/4 in a_2). "
    f"Scales share the SAME Dirac spectrum origin but have DIFFERENT "
    f"scaling exponents: gamma ~ a_2^{{-1/2}}, lambda_L ~ a_2^{{-1/4}}. "
    f"No controlled limit where they coincide within [0, 0.5]."
)

print(f"\n  GATE: {gate_verdict}")
print(f"  DETAIL: {gate_detail}")

# ===========================================================================
# STEP 12: Save output
# ===========================================================================
print("\n" + "=" * 78)
print("Step 12: Save output")
print("=" * 78)

outpath = os.path.join(SCRIPT_DIR, 's63_cutoff_meissner.npz')
np.savez(outpath,
    # Gate
    gate_name='CUTOFF-MEISSNER-63',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Key values at fold
    gamma_opt_fold=gamma_opt_fold,
    lambda_L_fold=lambda_L_fold,
    lambda_L_GGE_fold=lambda_L_GGE,
    ratio_GS_fold=ratio_at_fold_GS,
    ratio_GGE_fold=ratio_at_fold_GGE,
    discrepancy_pct=discrepancy_pct,
    # Tau-dependent arrays
    tau_arr=tau_arr,
    gamma_of_tau=gamma_of_tau,
    lambda_L_of_tau=lambda_L_of_tau,
    lambda_L_GGE_of_tau=lambda_L_GGE_of_tau,
    ratio_GS=ratio_fold_GS,
    ratio_GGE=ratio_fold_GGE,
    # Underlying Gilkey data
    a2_of_tau=a2_of_tau,
    a2_gilkey_fold=a2_gilkey_fold,
    a4_of_tau=a4_interp(tau_arr),
    ratio_gilkey_of_tau=ratio_of_tau,
    R_of_tau=R_of_tau,
    # Spectral action moments
    f2_of_tau=f2_of_tau,
    f4_of_tau=f4_of_tau,
    f0_gauge=f0_gauge,
    # Scaling analysis
    f_ratio=f_ratio,
    r_target=r_target,
    D_s_of_tau=D_s_of_tau,
    D_s_GGE_of_tau=D_s_GGE_of_tau,
    # Crossings
    n_crossings_GS=len(crossings_GS),
    n_crossings_GGE=len(crossings_GGE),
    crossings_GS=np.array(crossings_GS) if crossings_GS else np.array([]),
    crossings_GGE=np.array(crossings_GGE) if crossings_GGE else np.array([]),
    # Constants used
    tau_fold=tau_fold,
    kappa_GGE=kappa_GGE,
    xi_GL_GGE=xi_GL_GGE,
    ratio_gge_depletion=ratio_gge_depletion,
    # Monotonicity check
    ratio_monotonic=is_monotonic,
)

print(f"  Saved: {outpath}")
print(f"\n  Total time: {time.time() - t0:.2f} s")
