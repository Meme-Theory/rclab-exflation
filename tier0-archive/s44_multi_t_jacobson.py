#!/usr/bin/env python3
"""
MULTI-T-JACOBSON-44: 8-temperature Jacobson first law for GGE
=============================================================

Extends W5-1 (JACOBSON-SPEC-44) with full multi-temperature structure.

Physics: Jacobson (1995) derives Einstein equations from delta Q = T dS
on local Rindler horizons. For a GGE with 8 conserved charges (Richardson-
Gaudin integrals), the first law generalizes to:

    delta Q = sum_k T_k dS_k     (diagonal)
            + sum_{k<l} T_{kl} dC_{kl}  (cross-correlations)

where T_k = 1/beta_k are the 8 GGE temperatures, S_k = -n_k ln n_k
are per-mode entropies, and T_{kl} encodes cross-temperature correlations
from the G_kl matrix.

Each mode defines a cosmological fluid with:
    rho_k = 2 E_k n_k  (BCS pair energy)
    P_k = w_k rho_k
    w_k = T_k / (2 E_k) for relativistic gas, or 0 for dust

The 8 fluids are separately conserved (integrability-protected):
    dot{rho}_k + 3H(1 + w_k) rho_k = 0

Cross-temperature terms T_{kl} < 0 introduce effective interaction
pressure between sectors, potentially sourcing w != 0 even for dust.

Gate: INFO (8-fluid EOS diagnostic)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from pathlib import Path
import sys

# ============================================================
# 1. Load data
# ============================================================
base = Path(__file__).parent

# GGE temperatures (note: actual filename is s43_gge_temperatures.npz)
gge = np.load(base / 's43_gge_temperatures.npz', allow_pickle=True)
fl = np.load(base / 's43_first_law.npz', allow_pickle=True)
en = np.load(base / 's42_gge_energy.npz', allow_pickle=True)

# Extract key quantities
labels = gge['branch_labels']  # 8 mode labels
E_k = gge['E_8']               # quasiparticle energies [M_KK]
n_k = gge['nk_exact']          # GGE occupation numbers
T_k = gge['T_k']               # GGE temperatures [M_KK]
beta_k = gge['beta_k']         # inverse temperatures
S_GGE = float(gge['S_GGE'])    # total GGE entropy [nats]
E_GGE = float(gge['E_GGE'])    # total GGE energy [M_KK]
rho_DOS = gge['rho']           # DOS weight per mode
G_kl = gge['G_kl']             # 8x8 cross-correlation matrix
G_eig = gge['G_eigenvalues']   # eigenvalues of G_kl

# Branch temperatures
T_B2 = float(gge['T_B2'])     # 0.668
T_B1 = float(gge['T_B1'])     # 0.435
T_B3 = float(gge['T_B3'])     # 0.178

# Cross-temperatures
T_B2B1 = float(gge['T_B2B1'])  # -0.066 (negative!)
T_B2B3 = float(gge['T_B2B3'])  # 0.065
T_B1B3 = float(gge['T_B1B3'])  # 0.096

# First law quantities from S43
X_tau = float(fl['X_tau'])       # geometric drive [M_KK/dtau]
S_fold = float(fl['S_fold'])     # spectral action at fold

# Physical constants
M_KK_grav = float(en['M_KK_gravity'])   # 7.43e16 GeV
M_KK_gauge = float(en['M_KK_gauge'])    # 5.04e17 GeV

print("=" * 70)
print("MULTI-T-JACOBSON-44: 8-Temperature Jacobson First Law")
print("=" * 70)

# ============================================================
# 2. Per-mode thermodynamic quantities
# ============================================================

# Energy density per mode: rho_k = 2 * E_k * n_k (BCS pair energy)
rho_k = 2.0 * E_k * n_k  # [M_KK per cell]

# Per-mode entropy: S_k = -n_k ln(n_k) - (1-n_k) ln(1-n_k) (fermionic)
# This is the von Neumann entropy of a single-mode Fermi occupation
S_k = np.zeros(8)
for i in range(8):
    nk = n_k[i]
    if 0 < nk < 1:
        S_k[i] = -nk * np.log(nk) - (1.0 - nk) * np.log(1.0 - nk)
    else:
        S_k[i] = 0.0

# Free energy per mode: F_k = E_k - T_k * S_k (Helmholtz)
F_k = rho_k - T_k * S_k

# Verify total energy and entropy
E_total_check = np.sum(rho_k)
S_total_check = np.sum(S_k)

print(f"\n--- Per-mode decomposition ---")
print(f"{'Mode':<8} {'E_k':>8} {'n_k':>8} {'rho_k':>8} {'T_k':>8} {'S_k':>8} {'F_k':>8}")
for i in range(8):
    print(f"{labels[i]:<8} {E_k[i]:8.4f} {n_k[i]:8.5f} {rho_k[i]:8.5f} "
          f"{T_k[i]:8.4f} {S_k[i]:8.5f} {F_k[i]:8.5f}")

print(f"\nTotal rho = {E_total_check:.6f} M_KK (stored E_GGE = {E_GGE:.6f})")
print(f"Total S   = {S_total_check:.6f} nats (stored S_GGE = {S_GGE:.6f})")

# ============================================================
# 3. Equation of state per mode
# ============================================================
# For a GGE mode with temperature T_k and energy E_k:
#
# The EOS parameter w_k depends on the regime:
#
# (a) Dust (CDM-like): If quasiparticles are non-relativistic (T_k << E_k),
#     then P_k = 0, w_k = 0.
#
# (b) Radiation-like: If T_k ~ E_k, the mode is semi-relativistic.
#     For a single-mode fermionic GGE, the pressure is:
#     P_k = T_k * n_k * (1-n_k) / V_cell  (from dF/dV at fixed T)
#
#     But in the internal space, the "volume" is the cell volume of SU(3).
#     The pressure-to-energy ratio for a single bosonic mode at occupation n:
#     w_k = P_k / rho_k
#
# The key diagnostic: T_k / E_k ratio determines the regime.

ratio_TE = T_k / E_k

# For a GGE, the Euler relation gives:
#   E = sum_k T_k * S_k  (if PV = 0, no volume work)
# So the "effective temperature-weighted entropy" IS the energy:
Euler_sum = np.sum(T_k * S_k)

print(f"\n--- EOS diagnostics ---")
print(f"{'Mode':<8} {'T_k/E_k':>8} {'Regime':>12}")
for i in range(8):
    regime = "radiation" if ratio_TE[i] > 0.3 else ("warm" if ratio_TE[i] > 0.1 else "dust")
    print(f"{labels[i]:<8} {ratio_TE[i]:8.4f} {regime:>12}")

# For a massive relativistic particle with mass m and temperature T:
#   w = T/(m*c^2) * [K_1(m*c^2/T) / K_2(m*c^2/T)]  (Juttner)
# where K_n are modified Bessel functions.
# But for a SINGLE MODE GGE, the EOS is simpler.
# The occupation n_k = 1/(exp(beta_k * 2*E_k) + 1) gives:
#   P_k * V = T_k * ln(1 + exp(-beta_k * 2*E_k))  (grand potential per mode)
# and rho_k = 2*E_k*n_k, so:
#   w_k = T_k * ln(1 + exp(-2*beta_k*E_k)) / (2*E_k*n_k)

from scipy.special import kn as bessel_kn

w_k_juttner = np.zeros(8)
w_k_gge = np.zeros(8)

for i in range(8):
    # Juttner EOS: w = K_1(x)/K_2(x) * T/E where x = E/T
    x = E_k[i] / T_k[i]
    if x > 500:
        w_k_juttner[i] = 0.0  # non-relativistic limit
    else:
        w_k_juttner[i] = (T_k[i] / E_k[i]) * bessel_kn(1, x) / bessel_kn(2, x)

    # GGE single-mode EOS from grand potential
    # Omega_k = -T_k * ln(1 + exp(-beta_k * 2*E_k))
    # P_k * V = -Omega_k = T_k * ln(1 + exp(-2*beta_k*E_k))
    # w_k = P_k / rho_k = T_k * ln(1 + exp(-2*beta_k*E_k)) / (2*E_k*n_k)
    arg = -2.0 * beta_k[i] * E_k[i]
    if arg < -500:
        ln_term = 0.0
    else:
        ln_term = np.log(1.0 + np.exp(arg))

    P_k_gge = T_k[i] * ln_term
    w_k_gge[i] = P_k_gge / rho_k[i] if rho_k[i] > 0 else 0.0

# The definitive w_k: for CDM at late times (T_kinetic << m), w -> 0.
# But at PRODUCTION (the GGE state immediately post-transit), we use the
# GGE EOS which accounts for the fixed occupation numbers.

# For the 4D cosmological fluid, what matters is the 4D stress tensor.
# CDM-CONSTRUCT-43 proved T^{0i}_4D = 0 (zero 4D momentum).
# The key insight: these are INTERNAL excitations with zero external momentum.
# Their 4D EOS is w = 0 (dust) regardless of internal temperature.
#
# The multi-temperature structure matters for INTERNAL thermodynamics,
# not for the 4D Friedmann equation directly. But the cross-temperature
# terms can source effective anisotropic stress or interaction pressure.

print(f"\n--- Equation of state ---")
print(f"{'Mode':<8} {'w_Juttner':>10} {'w_GGE':>10} {'P_k':>10} {'rho_k':>10}")
for i in range(8):
    P_i = w_k_gge[i] * rho_k[i]
    print(f"{labels[i]:<8} {w_k_juttner[i]:10.5f} {w_k_gge[i]:10.5f} "
          f"{P_i:10.6f} {rho_k[i]:10.5f}")

# Energy-weighted w_eff
w_eff_juttner = np.sum(w_k_juttner * rho_k) / np.sum(rho_k)
w_eff_gge = np.sum(w_k_gge * rho_k) / np.sum(rho_k)

print(f"\nw_eff (Juttner): {w_eff_juttner:.5f}")
print(f"w_eff (GGE):     {w_eff_gge:.5f}")
print(f"w_eff (W5-1):    0.387")

# ============================================================
# 4. Multi-temperature Jacobson first law
# ============================================================
# The generalized first law for the GGE is:
#
#   delta Q = sum_k T_k dS_k  +  sum_{k<l} T_{kl} dC_{kl}
#
# where C_{kl} = <n_k n_l> - <n_k><n_l> is the connected correlator
# and T_{kl} is the cross-temperature defined from G_kl.
#
# The G_kl matrix was computed in S43:
#   G_kl = d^2 ln Z / (d beta_k d beta_l) = cov(n_k, n_l)
#
# For a non-interacting GGE, G_kl is diagonal:
#   G_kk = n_k(1-n_k) (variance of Fermi occupation)
# Off-diagonal elements arise from residual interactions.
#
# The cross-temperature T_{kl} is defined implicitly by:
#   G_kl = - d <n_k> / d beta_l
# For k != l, this gives the sensitivity of mode k's occupation to
# changing the temperature of mode l.

print(f"\n--- Cross-temperature analysis ---")

# Diagonal elements of G (variances)
G_diag = np.diag(G_kl)
G_variance_pred = n_k * (1.0 - n_k)  # non-interacting prediction

print(f"\n{'Mode':<8} {'G_kk':>10} {'n(1-n)':>10} {'ratio':>10}")
for i in range(8):
    r = G_diag[i] / G_variance_pred[i] if G_variance_pred[i] > 0 else 0
    print(f"{labels[i]:<8} {G_diag[i]:10.5f} {G_variance_pred[i]:10.5f} {r:10.4f}")

# The G_kl matrix IS the susceptibility matrix.
# For cross-temperature contributions to the first law:
#
# In the multi-temperature Jacobson formalism, the heat flux through
# a local Rindler horizon is:
#
#   delta Q = sum_k T_k dS_k + delta Q_cross
#
# where delta Q_cross = sum_{k<l} T_{kl} * d(corr_{kl})

# Branch-level cross-temperatures (already stored)
print(f"\nBranch cross-temperatures [M_KK]:")
print(f"  T(B2,B1) = {T_B2B1:+.5f}  {'NEGATIVE (time-crystalline)' if T_B2B1 < 0 else ''}")
print(f"  T(B2,B3) = {T_B2B3:+.5f}")
print(f"  T(B1,B3) = {T_B1B3:+.5f}")

# ============================================================
# 5. Cross-temperature effective pressure
# ============================================================
# The negative cross-temperature T(B2,B1) = -0.066 means that
# increasing the B1 occupation DECREASES the B2 entropy contribution.
#
# In a cosmological context, this anti-correlation creates an effective
# interaction between the B2 and B1 fluids:
#
#   P_cross = -sum_{k<l} T_{kl} * partial(S_k)/partial(V) * partial(S_l)/partial(V)
#
# For our internal-space modes (no spatial dependence in 4D), this becomes:
#
#   P_cross = 0  (no spatial gradient => no pressure contribution)
#
# The cross-temperatures are INTERNAL to the GGE and do not source
# 4D pressure. They affect the INTERNAL first law (how heat is
# redistributed among modes) but not the Friedmann equation.
#
# Physical interpretation: The negative T(B2,B1) means the B2 and B1
# sectors are ANTI-correlated: exciting B2 modes suppresses B1 modes.
# This is a consequence of the shared Fermi energy and the gap structure
# (B1 and B2 compete for the same Cooper pair spectral weight).

# Compute the cross-temperature energy contribution
E_cross = 0.0
n_cross_pairs = 0
cross_terms = []
for k in range(8):
    for l in range(k+1, 8):
        # Off-diagonal G_kl
        g_kl = G_kl[k, l]
        # Effective cross-temperature: T_kl = -g_kl / (dS_k/dn_k * dS_l/dn_l)
        # For fermionic modes: dS/dn = -ln(n/(1-n)) = beta * 2E
        # So T_kl ~ -g_kl * T_k * T_l / (something)

        # The energy contribution from cross-correlations:
        # delta_E_cross = sum_{k<l} 2*(E_k+E_l) * G_kl (if G_kl = cov)
        E_contrib = 2.0 * (E_k[k] + E_k[l]) * g_kl
        E_cross += E_contrib
        cross_terms.append((labels[k], labels[l], g_kl, E_contrib))
        n_cross_pairs += 1

print(f"\n--- Cross-correlation energy ---")
print(f"Total cross pairs: {n_cross_pairs}")
print(f"Total cross energy: {E_cross:.6f} M_KK")
print(f"Ratio cross/diagonal: {abs(E_cross)/E_GGE:.4f}")

# The most significant cross-terms
cross_terms.sort(key=lambda x: abs(x[3]), reverse=True)
print(f"\nTop 5 cross-terms:")
for lab_k, lab_l, g, e in cross_terms[:5]:
    print(f"  ({lab_k}, {lab_l}): G_kl = {g:+.5f}, E_cross = {e:+.5f} M_KK")

# ============================================================
# 6. 8-fluid Friedmann evolution
# ============================================================
# Each mode k is a separately conserved fluid:
#   dot{rho}_k + 3H(1 + w_k) rho_k = 0
#
# Solution: rho_k(a) = rho_k(a_0) * (a/a_0)^{-3(1+w_k)}
#
# The Friedmann equation:
#   H^2 = (8piG/3) sum_k rho_k(a)
#
# For dust (w=0): rho_k ~ a^{-3} (CDM behavior)
# For radiation (w=1/3): rho_k ~ a^{-4}
# For the GGE w_k values: each mode dilutes differently!

# Compute a-evolution
a_arr = np.logspace(0, 4, 500)  # a/a_0 from 1 to 10^4

# rho_k(a) for each mode
rho_k_of_a = np.zeros((8, len(a_arr)))
for i in range(8):
    rho_k_of_a[i] = rho_k[i] * a_arr**(-3.0 * (1.0 + w_k_gge[i]))

# Total rho(a)
rho_total_of_a = np.sum(rho_k_of_a, axis=0)

# Effective w(a) = -(1 + (2/3) * d ln rho / d ln a) / rho
# Numerically: w_eff(a) = sum_k w_k rho_k(a) / sum_k rho_k(a)
w_eff_of_a = np.sum(w_k_gge[:, None] * rho_k_of_a, axis=0) / rho_total_of_a

# Fraction of energy in each branch
f_B2_of_a = np.sum(rho_k_of_a[:4], axis=0) / rho_total_of_a
f_B1_of_a = rho_k_of_a[4] / rho_total_of_a
f_B3_of_a = np.sum(rho_k_of_a[5:], axis=0) / rho_total_of_a

print(f"\n--- 8-fluid Friedmann evolution ---")
print(f"{'a/a_0':<12} {'w_eff':>8} {'f_B2':>8} {'f_B1':>8} {'f_B3':>8}")
for a_val in [1.0, 10.0, 100.0, 1000.0, 10000.0]:
    idx = np.argmin(np.abs(a_arr - a_val))
    print(f"{a_arr[idx]:<12.1f} {w_eff_of_a[idx]:8.5f} "
          f"{f_B2_of_a[idx]:8.4f} {f_B1_of_a[idx]:8.4f} {f_B3_of_a[idx]:8.4f}")

# ============================================================
# 7. Effective w from cross-temperature sector
# ============================================================
# The cross-temperatures do NOT directly contribute to the 4D EOS
# (CDM-CONSTRUCT-43: T^{0i}=0 exactly). But they contribute to
# the INTERNAL first law, which affects:
#
# (a) The heat capacity: C_v = sum_k T_k^2 * d S_k / d T_k + cross terms
# (b) The response to perturbations: if a perturbation changes T_k,
#     the cross-terms T_{kl} transfer entropy between sectors
# (c) The effective sound speed for second sound in the GGE
#
# For the 4D cosmological EOS:
# - At production: w_eff = 0.387 (W5-1 confirmed)
# - This is the INTERNAL w, relevant for the thermodynamic first law
# - The 4D w for Friedmann is determined by the 4D momentum content
# - CDM-CONSTRUCT-43 proved T^{0i}=0 => w_4D = 0 (dust)
#
# Resolution: The multi-temperature structure tells us about the
# INTERNAL thermodynamics of each KZ domain cell. The cells themselves
# are CDM (w=0 in 4D). The 8-fluid structure describes the internal
# heat redistribution, not the 4D expansion dynamics.
#
# The cross-temperature T(B2,B1) < 0 means B2-B1 anti-correlation:
# a perturbation that heats B2 cools B1 (and vice versa). This is
# an internal thermostat effect.

# Compute heat capacity matrix
# C_{kl} = d E_k / d T_l = 2 E_k * d n_k / d T_l
# For non-interacting: C_{kl} = 2 E_k * n_k(1-n_k) * 2E_k/T_k^2 * delta_{kl}
# With interactions: C_{kl} = 2 E_k * G_{kl} / T_l

C_matrix = np.zeros((8, 8))
for k in range(8):
    for l in range(8):
        # d n_k / d T_l = (1/T_l^2) * G_{kl} (from definition of G)
        # Actually: d<n_k>/d beta_l = -G_{kl}
        # So d<n_k>/d T_l = G_{kl} / T_l^2
        C_matrix[k, l] = 2.0 * E_k[k] * G_kl[k, l] / T_k[l]**2

# Total heat capacity
C_total = np.sum(C_matrix)
# Diagonal heat capacity
C_diag = np.sum(np.diag(C_matrix))
# Off-diagonal heat capacity
C_off = C_total - C_diag

print(f"\n--- Heat capacity matrix ---")
print(f"C_total = {C_total:.5f}")
print(f"C_diag  = {C_diag:.5f}")
print(f"C_off   = {C_off:.5f}")
print(f"C_off/C_diag = {C_off/C_diag:.4f}")

# Eigenvalues of heat capacity matrix
C_eig = np.linalg.eigvalsh(C_matrix)
print(f"\nC eigenvalues: {np.sort(C_eig)}")
n_negative_C = np.sum(C_eig < 0)
print(f"Negative eigenvalues: {n_negative_C} / 8")

# ============================================================
# 8. Multi-temperature Euler relation verification
# ============================================================
# For a GGE: E = sum_k mu_k N_k where mu_k = 2 E_k (chemical potential
# for quasiparticle excitations). This is the Euler relation for a
# system with 8 conserved charges.
#
# Alternatively: E = sum_k T_k S_k + sum_k mu_k N_k - PV
# For PV = 0 (no volume work in internal space):
# E_GGE = sum_k T_k S_k <=> Euler identity holds

Euler_diag = np.sum(T_k * S_k)
Euler_resid = Euler_diag - E_GGE

print(f"\n--- Euler relation ---")
print(f"sum T_k S_k = {Euler_diag:.6f}")
print(f"E_GGE       = {E_GGE:.6f}")
print(f"Residual    = {Euler_resid:.6f}")
print(f"Fractional  = {abs(Euler_resid)/E_GGE:.6e}")

# If the Euler relation doesn't hold exactly (it shouldn't for a
# non-equilibrium GGE vs Gibbs), the discrepancy encodes the
# non-thermality.
Euler_Gibbs = float(gge['T_therm']) * S_GGE  # T_therm * S for comparison
print(f"\nT_therm * S_GGE = {Euler_Gibbs:.6f}")

# ============================================================
# 9. Branch-level 3-fluid decomposition
# ============================================================
# Group into B2 (4 modes), B1 (1 mode), B3 (3 modes)

branch_names = ['B2', 'B1', 'B3']
branch_slices = [slice(0, 4), slice(4, 5), slice(5, 8)]
branch_colors = ['#2196F3', '#FF9800', '#4CAF50']

rho_branch = np.array([np.sum(rho_k[s]) for s in branch_slices])
S_branch = np.array([np.sum(S_k[s]) for s in branch_slices])
T_branch = np.array([T_B2, T_B1, T_B3])
w_branch = np.array([np.sum(w_k_gge[s] * rho_k[s]) / np.sum(rho_k[s])
                      for s in branch_slices])

# Cross-temperature matrix at branch level (3x3)
T_cross_branch = np.array([
    [T_B2, T_B2B1, T_B2B3],
    [T_B2B1, T_B1, T_B1B3],
    [T_B2B3, T_B1B3, T_B3]
])

print(f"\n--- Branch-level 3-fluid ---")
print(f"{'Branch':<6} {'rho':>8} {'S':>8} {'T':>8} {'w':>8} {'frac':>8}")
for i, name in enumerate(branch_names):
    frac = rho_branch[i] / np.sum(rho_branch)
    print(f"{name:<6} {rho_branch[i]:8.5f} {S_branch[i]:8.5f} "
          f"{T_branch[i]:8.5f} {w_branch[i]:8.5f} {frac:8.4f}")

print(f"\nCross-temperature matrix [M_KK]:")
print(f"       {'B2':>8} {'B1':>8} {'B3':>8}")
for i, name in enumerate(branch_names):
    row = " ".join(f"{T_cross_branch[i,j]:+8.4f}" for j in range(3))
    print(f"  {name:<4} {row}")

# Eigenvalues of cross-temperature matrix
T_cross_eig = np.linalg.eigvalsh(T_cross_branch)
print(f"\nEigenvalues of T_cross: {T_cross_eig}")
n_neg = np.sum(T_cross_eig < 0)
print(f"Negative eigenvalues: {n_neg} / 3")

# ============================================================
# 10. Physical interpretation and w_4D assessment
# ============================================================
#
# KEY DISTINCTION:
#
# w_internal = 0.387 (internal thermodynamic EOS, from T_k / E_k)
#   This describes the internal heat content of each KZ domain cell.
#   It determines second-sound speed, heat capacity, response to perturbations.
#
# w_4D = 0 (four-dimensional cosmological EOS)
#   CDM-CONSTRUCT-43 proved T^{0i}_4D = 0 exactly. The GGE modes are
#   internal-space excitations with ZERO external momentum. They gravitate
#   as pressureless dust in 4D.
#
# The CROSS-TEMPERATURE T(B2,B1) < 0:
# - Does NOT produce 4D pressure (modes have zero 4D momentum)
# - Does produce INTERNAL anti-correlation (B2-B1 thermostat)
# - Does affect perturbation response (negative susceptibility)
# - Is a signature of the non-thermal GGE state
#
# Connection to time-crystalline behavior:
# T(B2,B1) < 0 means the B2-B1 subsystem has negative off-diagonal
# susceptibility. In condensed matter, this is associated with
# systems where increasing one order parameter suppresses another
# (competing orders). The negative cross-temperature is NOT
# time-crystalline in the Wilczek sense (no spontaneous time-translation
# breaking), but it IS a signature of the non-equilibrium GGE.

# Compute effective anisotropic stress from cross-temperatures
# Pi_{ij} = T_{ij} - (1/3) delta_{ij} T_kk for i,j = branch indices
T_trace = np.trace(T_cross_branch)
Pi_branch = T_cross_branch - (T_trace / 3.0) * np.eye(3)
Pi_norm = np.linalg.norm(Pi_branch)
Pi_frac = Pi_norm / T_trace

print(f"\n--- Anisotropic stress (internal) ---")
print(f"T_trace     = {T_trace:.5f}")
print(f"|Pi_branch| = {Pi_norm:.5f}")
print(f"|Pi|/T_tr   = {Pi_frac:.4f}")

# ============================================================
# 11. Summary table
# ============================================================

print(f"\n{'='*70}")
print(f"SUMMARY: MULTI-T-JACOBSON-44")
print(f"{'='*70}")
print(f"\n8-fluid GGE parameters:")
print(f"  Modes: 4 B2 + 1 B1 + 3 B3 = 8 total")
print(f"  E_GGE = {E_GGE:.4f} M_KK")
print(f"  S_GGE = {S_GGE:.4f} nats")
print(f"  w_eff (internal) = {w_eff_gge:.5f}")
print(f"  w_4D = 0 (CDM by construction)")
print(f"\nBranch temperatures [M_KK]:")
print(f"  T_B2 = {T_B2:.4f}, T_B1 = {T_B1:.4f}, T_B3 = {T_B3:.4f}")
print(f"  T(B2,B1) = {T_B2B1:+.5f} (NEGATIVE)")
print(f"  T(B2,B3) = {T_B2B3:+.5f}")
print(f"  T(B1,B3) = {T_B1B3:+.5f}")
print(f"\nCross-temperature matrix eigenvalues: {T_cross_eig}")
print(f"  Negative eigenvalues: {n_neg}/3")
print(f"\nHeat capacity:")
print(f"  C_total = {C_total:.5f}")
print(f"  C_off/C_diag = {C_off/C_diag:.4f} (off-diagonal fraction)")
print(f"\nEuler relation:")
print(f"  sum T_k S_k / E_GGE = {Euler_diag/E_GGE:.6f}")
print(f"\nMulti-temperature first law: delta Q = sum_k T_k dS_k")
print(f"  8 separately conserved fluids (integrability-protected)")
print(f"  Cross-terms are INTERNAL (do not source 4D pressure)")
print(f"  Negative T(B2,B1) = B2-B1 anti-correlation (competing orders)")

# ============================================================
# 12. Gate verdict
# ============================================================
gate_name = 'MULTI-T-JACOBSON-44'
gate_verdict = 'INFO'

print(f"\n{'='*70}")
print(f"GATE: {gate_name} = {gate_verdict}")
print(f"{'='*70}")
print(f"8-fluid EOS computed. w_internal = {w_eff_gge:.3f}, w_4D = 0.")
print(f"Negative T(B2,B1) = {T_B2B1:.4f} encodes B2-B1 anti-correlation.")
print(f"Cross-temps are INTERNAL; do not modify 4D Friedmann equation.")
print(f"Heat capacity has {n_negative_C} negative eigenvalue(s) => non-standard thermodynamics.")

# ============================================================
# 13. Save data
# ============================================================
np.savez(base / 's44_multi_t_jacobson.npz',
    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([gate_verdict]),

    # Per-mode quantities
    labels=labels,
    E_k=E_k,
    n_k=n_k,
    rho_k=rho_k,
    T_k=T_k,
    S_k=S_k,
    F_k=F_k,
    beta_k=beta_k,
    w_k_gge=w_k_gge,
    w_k_juttner=w_k_juttner,
    ratio_TE=ratio_TE,

    # Branch-level
    branch_names=np.array(branch_names),
    rho_branch=rho_branch,
    S_branch=S_branch,
    T_branch=T_branch,
    w_branch=w_branch,

    # Cross-temperatures
    T_cross_branch=T_cross_branch,
    T_cross_eig=T_cross_eig,
    n_negative_T_cross=n_neg,
    T_B2B1=T_B2B1,
    T_B2B3=T_B2B3,
    T_B1B3=T_B1B3,

    # Global
    E_GGE=E_GGE,
    S_GGE=S_GGE,
    w_eff_internal=w_eff_gge,
    w_4D=0.0,

    # Heat capacity
    C_matrix=C_matrix,
    C_total=C_total,
    C_diag=C_diag,
    C_off=C_off,
    C_eigenvalues=np.sort(np.linalg.eigvalsh(C_matrix)),
    n_negative_C=n_negative_C,

    # Euler relation
    Euler_sum=Euler_diag,
    Euler_residual=Euler_resid,
    Euler_frac=abs(Euler_resid)/E_GGE,

    # Anisotropic stress
    Pi_branch=Pi_branch,
    Pi_norm=Pi_norm,
    Pi_frac=Pi_frac,

    # G matrix
    G_kl=G_kl,
    G_eigenvalues=G_eig,

    # Cross energy
    E_cross=E_cross,
    E_cross_frac=abs(E_cross)/E_GGE,

    # Friedmann evolution
    a_arr=a_arr,
    rho_total_of_a=rho_total_of_a,
    w_eff_of_a=w_eff_of_a,
    f_B2_of_a=f_B2_of_a,
    f_B1_of_a=f_B1_of_a,
    f_B3_of_a=f_B3_of_a,
)

print(f"\nData saved to: {base / 's44_multi_t_jacobson.npz'}")

# ============================================================
# 14. Plots
# ============================================================
fig = plt.figure(figsize=(16, 14))
gs = GridSpec(3, 3, hspace=0.35, wspace=0.35)

# --- Panel (a): Per-mode rho, T, w bar chart ---
ax1 = fig.add_subplot(gs[0, 0])
x_pos = np.arange(8)
bars = ax1.bar(x_pos, rho_k, color=['#2196F3']*4 + ['#FF9800'] + ['#4CAF50']*3,
               alpha=0.8, edgecolor='black', linewidth=0.5)
ax1.set_xticks(x_pos)
ax1.set_xticklabels([str(l) for l in labels], fontsize=7, rotation=45)
ax1.set_ylabel(r'$\rho_k$ [$M_{\rm KK}$]', fontsize=9)
ax1.set_title('(a) Energy density per mode', fontsize=10, fontweight='bold')
ax1.axhline(y=0, color='gray', linewidth=0.5)

# Overlay w_k on secondary axis
ax1b = ax1.twinx()
ax1b.scatter(x_pos, w_k_gge, color='red', marker='D', s=30, zorder=5, label=r'$w_k$')
ax1b.set_ylabel(r'$w_k$ (GGE)', fontsize=9, color='red')
ax1b.tick_params(axis='y', labelcolor='red')
ax1b.set_ylim(-0.05, 0.6)

# --- Panel (b): Temperature hierarchy ---
ax2 = fig.add_subplot(gs[0, 1])
T_sorted_idx = np.argsort(T_k)[::-1]
colors_sorted = ['#2196F3' if i < 4 else '#FF9800' if i == 4 else '#4CAF50' for i in T_sorted_idx]
ax2.barh(np.arange(8), T_k[T_sorted_idx], color=colors_sorted, alpha=0.8,
         edgecolor='black', linewidth=0.5)
ax2.set_yticks(np.arange(8))
ax2.set_yticklabels([str(labels[i]) for i in T_sorted_idx], fontsize=7)
ax2.set_xlabel(r'$T_k$ [$M_{\rm KK}$]', fontsize=9)
ax2.set_title('(b) GGE temperature hierarchy', fontsize=10, fontweight='bold')

# --- Panel (c): Cross-temperature matrix ---
ax3 = fig.add_subplot(gs[0, 2])
im = ax3.imshow(T_cross_branch, cmap='RdBu_r', aspect='auto',
                vmin=-0.1, vmax=0.7)
ax3.set_xticks([0, 1, 2])
ax3.set_xticklabels(branch_names)
ax3.set_yticks([0, 1, 2])
ax3.set_yticklabels(branch_names)
ax3.set_title('(c) Cross-temperature matrix', fontsize=10, fontweight='bold')
for i in range(3):
    for j in range(3):
        color = 'white' if abs(T_cross_branch[i,j]) > 0.3 else 'black'
        ax3.text(j, i, f'{T_cross_branch[i,j]:+.3f}', ha='center', va='center',
                fontsize=9, color=color, fontweight='bold')
plt.colorbar(im, ax=ax3, label=r'$T_{ij}$ [$M_{\rm KK}$]', shrink=0.8)

# --- Panel (d): G_kl heatmap ---
ax4 = fig.add_subplot(gs[1, 0])
im4 = ax4.imshow(G_kl, cmap='coolwarm', aspect='auto')
ax4.set_xticks(np.arange(8))
ax4.set_xticklabels([str(l) for l in labels], fontsize=6, rotation=45)
ax4.set_yticks(np.arange(8))
ax4.set_yticklabels([str(l) for l in labels], fontsize=6)
ax4.set_title(r'(d) Susceptibility matrix $G_{kl}$', fontsize=10, fontweight='bold')
plt.colorbar(im4, ax=ax4, shrink=0.8)

# --- Panel (e): w_eff(a) evolution ---
ax5 = fig.add_subplot(gs[1, 1])
ax5.semilogx(a_arr, w_eff_of_a, 'k-', linewidth=2, label=r'$w_{\rm eff}(a)$')
ax5.axhline(y=1/3, color='red', linestyle='--', alpha=0.5, label='radiation (1/3)')
ax5.axhline(y=0, color='blue', linestyle='--', alpha=0.5, label='dust (0)')
ax5.axhline(y=w_eff_gge, color='gray', linestyle=':', alpha=0.7,
           label=f'initial ({w_eff_gge:.3f})')
ax5.set_xlabel(r'$a/a_0$', fontsize=9)
ax5.set_ylabel(r'$w_{\rm eff}$', fontsize=9)
ax5.set_title('(e) 8-fluid EOS evolution', fontsize=10, fontweight='bold')
ax5.legend(fontsize=7, loc='upper right')
ax5.set_ylim(-0.05, 0.5)

# --- Panel (f): Branch fractions vs a ---
ax6 = fig.add_subplot(gs[1, 2])
ax6.semilogx(a_arr, f_B2_of_a, color='#2196F3', linewidth=2, label='B2 (4 modes)')
ax6.semilogx(a_arr, f_B1_of_a, color='#FF9800', linewidth=2, label='B1 (1 mode)')
ax6.semilogx(a_arr, f_B3_of_a, color='#4CAF50', linewidth=2, label='B3 (3 modes)')
ax6.set_xlabel(r'$a/a_0$', fontsize=9)
ax6.set_ylabel('Energy fraction', fontsize=9)
ax6.set_title('(f) Branch energy fractions', fontsize=10, fontweight='bold')
ax6.legend(fontsize=8)
ax6.set_ylim(0, 1.05)

# --- Panel (g): Entropy per mode ---
ax7 = fig.add_subplot(gs[2, 0])
ax7.bar(x_pos, S_k, color=['#2196F3']*4 + ['#FF9800'] + ['#4CAF50']*3,
        alpha=0.8, edgecolor='black', linewidth=0.5)
ax7.set_xticks(x_pos)
ax7.set_xticklabels([str(l) for l in labels], fontsize=7, rotation=45)
ax7.set_ylabel(r'$S_k$ [nats]', fontsize=9)
ax7.set_title('(g) Per-mode entropy', fontsize=10, fontweight='bold')

# --- Panel (h): Heat capacity eigenvalues ---
ax8 = fig.add_subplot(gs[2, 1])
C_eig_sorted = np.sort(np.linalg.eigvalsh(C_matrix))
colors_C = ['red' if c < 0 else 'green' for c in C_eig_sorted]
ax8.barh(np.arange(8), C_eig_sorted, color=colors_C, alpha=0.8,
         edgecolor='black', linewidth=0.5)
ax8.axvline(x=0, color='black', linewidth=1)
ax8.set_yticks(np.arange(8))
ax8.set_yticklabels([f'mode {i}' for i in range(8)], fontsize=7)
ax8.set_xlabel(r'$C$ eigenvalue', fontsize=9)
ax8.set_title('(h) Heat capacity spectrum', fontsize=10, fontweight='bold')

# --- Panel (i): rho(a) evolution ---
ax9 = fig.add_subplot(gs[2, 2])
ax9.loglog(a_arr, rho_total_of_a, 'k-', linewidth=2, label='Total')
ax9.loglog(a_arr, np.sum(rho_k_of_a[:4], axis=0), color='#2196F3',
           linewidth=1.5, label='B2')
ax9.loglog(a_arr, rho_k_of_a[4], color='#FF9800', linewidth=1.5, label='B1')
ax9.loglog(a_arr, np.sum(rho_k_of_a[5:], axis=0), color='#4CAF50',
           linewidth=1.5, label='B3')
# Reference slopes
a_ref = np.array([1, 1e4])
ax9.loglog(a_ref, rho_total_of_a[0] * a_ref**(-3), 'k:', alpha=0.3, label=r'$a^{-3}$ (dust)')
ax9.loglog(a_ref, rho_total_of_a[0] * a_ref**(-4), 'k--', alpha=0.3, label=r'$a^{-4}$ (rad)')
ax9.set_xlabel(r'$a/a_0$', fontsize=9)
ax9.set_ylabel(r'$\rho$ [$M_{\rm KK}$]', fontsize=9)
ax9.set_title(r'(i) $\rho(a)$ evolution', fontsize=10, fontweight='bold')
ax9.legend(fontsize=7, loc='lower left')

fig.suptitle('MULTI-T-JACOBSON-44: 8-Temperature Jacobson First Law for GGE\n'
             r'$\delta Q = \sum_k T_k\,dS_k$ — 8-fluid EOS with cross-temperatures',
             fontsize=12, fontweight='bold', y=0.98)

plt.savefig(base / 's44_multi_t_jacobson.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to: {base / 's44_multi_t_jacobson.png'}")

print(f"\nDone.")
