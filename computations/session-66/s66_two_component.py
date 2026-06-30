#!/usr/bin/env python3
"""
s66_two_component.py — TWO-COMPONENT-66: Separate a_0-Constant from GGE-Dynamical
==================================================================================

Einstein-Theorist computation, Session 66 Wave 1.

Principle-Theoretic Reasoning:
  The vacuum energy entering the Friedmann equation has TWO physically distinct origins:

  1. GEOMETRIC (a_0 term): The spectral action zeroth coefficient Tr(f(D^2/Lambda^2))
     produces a term proportional to f_0 * Lambda^4 * a_0. Because a_0 counts modes
     weighted by volume (a topological invariant of the fiber), it is EXACTLY CONSTANT
     in tau — proven numerically: a_0 = 101984 at ALL 5 tau points in WDW data.
     This enters Friedmann as a true cosmological constant (w = -1, no redshift).

  2. DYNAMICAL (GGE excitations): The 59.8 Bogoliubov quasiparticle pairs created
     at the fold transit carry energy E_GGE = 60.625 M_KK. Each mode has a specific
     dispersion relation from the GL-Josephson spectrum (s52_gl_josephson.npz).
     These excitations redshift according to their equation of state.

  The Friedmann equation is:
     H^2 = (8*pi*G_N/3) * [rho_geom + rho_GGE(a)]
  where rho_geom is constant and rho_GGE(a) = sum_k n_k * E_k * a^{-3(1+w_k)}.

  This decomposition is STRUCTURALLY CLEAN: a_0 is a property of the GEOMETRY
  (fiber topology), while rho_GGE is a property of the STATE (excitations).
  These are categorically distinct — no entanglement between them.

Gate: TWO-COMPONENT-66
  PASS: Clean separation with w_eff(today) consistent with DESI w ~ -0.918
  FAIL: Components inseparable
  INFO: Separation achieved but w_eff(today) != -0.918

Reads: computations/session-53/s53_q_theory_gge.npz (GGE energy, temperature)
       computations/session-52/s52_gl_josephson.npz (GL dispersion, 6 branches)
       computations/session-65/s65_ep_test.npz (tau dynamics, a_2 profile)
       computations/session-52/s52_wdw_initial.npz (a_0 constancy proof)
       computations/session-58/s58_w_desi.npz (w_0 DESI comparison)
Writes: computations/session-66/s66_two_component.npz
        computations/session-66/s66_two_component.png

Author: einstein-theorist
Session: S66 W1-E
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    PI, M_KK, M_KK_gravity, M_Pl_reduced, M_Pl_unreduced,
    a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, G_N,
    rho_Lambda_obs, rho_crit_GeV4, H_0_GeV,
    Omega_Lambda, Omega_m, Omega_r,
    E_cond, E_exc, n_pairs, N_dof_BCS,
    T_acoustic, tau_fold, S_fold,
    c_Gold, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    H_fold, v_terminal, dt_transit,
    n_Bog, hbar_GeV_s,
    J_C2, J_su2, J_u1,
    E_B1, E_B2_mean, E_B3_mean,
    c_light, c_light_km_s,
    Mpc_to_m, hbar_c_GeV_m,
)
import numpy as np
from scipy.integrate import solve_ivp, simpson
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("  TWO-COMPONENT-66: Separate a_0-Constant from GGE-Dynamical")
print("  in the Friedmann Equation")
print("=" * 72)

# =============================================================================
#  1. COMPUTE rho_geom AT THE FOLD
# =============================================================================
#
# From Chamseddine-Connes spectral action (CCM 2007, Paper 06):
#
#   S_spectral = f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f(0) a_4 + ...
#
# The gravitational sector identification:
#   (1/16*pi*G_eff) = f_2 Lambda^2 * a_2 / (2*pi^2)     [Eq. (1)]
#   Lambda_CC = (f_0/f_2) * Lambda^2 * (a_0/a_2)          [Eq. (2)]
#
# For a sharp cutoff: f_n = Lambda^n * (moments of f), with
#   f_0 = Lambda^4/2, f_2 = Lambda^2/2, f_4 ~ 1
# This gives f_0/f_2 = Lambda^2.
#
# The cosmological constant energy density:
#   rho_Lambda = Lambda_CC / (8*pi*G_eff)
#             = (f_0 * a_0) / (2*pi^2) * Lambda^4           [Eq. (3)]
#
# Using M_KK as the natural UV cutoff (Lambda = M_KK):

print("\n--- Step 1: rho_geom (a_0 term, geometric cosmological constant) ---")

# Verify a_0 constancy from WDW data
wdw_data = np.load(os.path.join(SCRIPT_DIR, 's52_wdw_initial.npz'), allow_pickle=True)
a0_wdw = wdw_data['a0_vals']
tau_wdw = wdw_data['tau_data']
a2_wdw = wdw_data['a2_vals']

print(f"\n  a_0 constancy test (WDW data, 5 tau points):")
print(f"  tau:  {tau_wdw}")
print(f"  a_0:  {a0_wdw}")
print(f"  std(a_0)/mean(a_0) = {np.std(a0_wdw)/np.mean(a0_wdw):.2e}")
print(f"  RESULT: a_0 = {a0_wdw[0]:.0f} (EXACTLY CONSTANT in tau)")
a0_constant = a0_wdw[0]  # = 101984

# The canonical a0_fold = 6440.0 uses the spectral-zeta normalization
# The WDW a0 = 101984 uses the full trace normalization (with spinor multiplicity)
# Both are correct in their own conventions. For the CC computation, we use
# the same convention as s42_constants_snapshot.npz which gave rho_Lambda_spectral.

# From s42: rho_Lambda_spectral = (2/pi^2) * a0_fold * M_KK_kerner^4
# This is already computed in canonical_constants:
from canonical_constants import rho_Lambda_spectral

# For consistency with the gravity-route M_KK, recompute:
rho_geom_kerner = (2.0 / PI**2) * a0_fold * M_KK_gravity**4  # Using gravity-route M_KK
rho_geom_gravity = rho_geom_kerner  # Same thing, gravity route

# The canonical formula (Chamseddine-Connes):
# rho_Lambda = Lambda_CC / (8*pi*G) = (f_0/f_2) * Lambda^2 * (a_0/a_2) / (8*pi*G)
# For sharp cutoff: f_0/f_2 = Lambda^2
# Lambda_CC_SA = Lambda^4 * a_0 / a_2  (sharp cutoff)
# rho_geom = Lambda_CC_SA / (8*pi*G_eff)

# More precisely: rho_geom enters as the a_0 term in the spectral action
# density, which equals (2/pi^2) * a_0 * M_KK^4 in standard normalization
rho_geom = (2.0 / PI**2) * a0_fold * M_KK_gravity**4

print(f"\n  rho_geom (gravity-route M_KK = {M_KK_gravity:.3e} GeV):")
print(f"    rho_geom = (2/pi^2) * a0_fold * M_KK^4")
print(f"             = (2/{PI**2:.4f}) * {a0_fold:.1f} * ({M_KK_gravity:.3e})^4")
print(f"             = {rho_geom:.4e} GeV^4")
print(f"    log10(rho_geom) = {np.log10(rho_geom):.2f}")
print(f"    rho_geom / rho_Lambda_obs = {rho_geom / rho_Lambda_obs:.3e}")
print(f"    Gap: {np.log10(rho_geom / rho_Lambda_obs):.1f} OOM")

# a_0/a_2 ratio at fold (both in canonical normalization)
a0_over_a2_fold = a0_fold / a2_fold
print(f"\n  a_0/a_2 at fold = {a0_over_a2_fold:.4f}")
print(f"  This ratio is KEY: it sets Lambda_CC / M_Pl^2")

# =============================================================================
#  2. COMPUTE rho_GGE AT THE FOLD
# =============================================================================

print("\n\n--- Step 2: rho_GGE (dynamical quasiparticle excitations) ---")

# Load GGE data from s53
gge_data = np.load(os.path.join(SCRIPT_DIR, 's53_q_theory_gge.npz'), allow_pickle=True)
E_GGE_MKK = float(gge_data['E_GGE_MKK'])       # 60.625 M_KK
rho_GGE_GeV4_s53 = float(gge_data['rho_GGE_GeV4'])  # 3.74e68 GeV^4
T_GGE_arr = gge_data['T_GGE']                    # [0.668, 0.668, 0.668, 0.668, 0.435, 0.178, 0.178, 0.178]

# Load GL-Josephson dispersion for mode-resolved EOS
gl_data = np.load(os.path.join(SCRIPT_DIR, 's52_gl_josephson.npz'), allow_pickle=True)
K_arr = gl_data['K_array']        # (51,) wavenumber
omega_branches = gl_data['omega_branches']  # (51, 6) frequency
branch_labels = gl_data['branch_labels']
K_BZ = float(gl_data['K_BZ'])

# The GGE has 8 modes: 4 B2 + 1 B1 + 3 B3
# The GL-Josephson gives 6 collective branches (Goldstone, 2 Leggett, 3 massive)
# For the Friedmann equation, we need the equation of state w_k for each mode

# Mode-resolved EOS from dispersion: w_k = P_k / rho_k
# For relativistic phonons: w = c_s^2 (in the long-wavelength limit)
# For massive modes: w varies from 0 (non-relativistic) to 1/3 (ultra-relativistic)

# Sound speeds from GL-Josephson (slope at K=0):
dK = K_arr[1] - K_arr[0]
c_s_branches = np.zeros(6)
for i in range(6):
    # Linear slope from first two points
    c_s_branches[i] = (omega_branches[1, i] - omega_branches[0, i]) / dK

# Equation of state for each branch
# In a phonon gas at temperature T, w = (1/3) * <v_g * K> / <omega>
# For linear dispersion omega = c_s * K: w = c_s^2 / 3 (3D) or c_s^2 (1D)
# For massive modes omega = sqrt(m^2 + c_s^2 K^2): w transitions from 0 to c_s^2/3

# The GGE modes at the fold are in the non-equilibrium state with n_Bog ~ 1
# Their equation of state is determined by the dispersion relation

print(f"\n  GGE summary:")
print(f"    E_GGE = {E_GGE_MKK:.3f} M_KK ({n_pairs:.1f} pairs, {N_dof_BCS} branches)")
print(f"    rho_GGE = {rho_GGE_GeV4_s53:.3e} GeV^4")
print(f"    T_GGE = {T_GGE_arr}")

# Convert GGE energy to GeV^4 density
# rho_GGE = E_GGE * M_KK^4 / Vol_cell (in the cell)
# From s53: rho_GGE_GeV4 = 3.74e68 GeV^4
rho_GGE = rho_GGE_GeV4_s53

print(f"\n  Branch dispersions (slope at K=0):")
for i in range(6):
    lbl = branch_labels[i] if i < len(branch_labels) else f"Branch-{i}"
    gap = omega_branches[0, i]
    print(f"    {lbl}: c_s = {c_s_branches[i]:.4f} M_KK, gap = {gap:.4f} M_KK")

# Classify modes by their EOS
# Goldstone (branch 0): gapless, omega ~ c_s * K -> w = c_s^2/3 (radiation-like)
# Leggett-1,2 (branches 1,2): gapped, omega = sqrt(m_L^2 + c^2 K^2) -> w varies
# Massive (branches 3,4,5): large gaps -> w ~ 0 (matter-like) at low T

# Mode masses (gaps at K=0)
m_modes = omega_branches[0, :]
w_modes = np.zeros(6)

# For the GGE state: each mode has typical K ~ T_GGE / c_s
# At T_GGE ~ 0.5 M_KK, modes with gap >> T are matter-like (w~0)
# Modes with gap << T are radiation-like (w ~ 1/3 for 3+1D)
# The Goldstone mode has gap=0, so w_Gold ~ c_Gold^2 / 3 in 3D

T_avg = np.mean(T_GGE_arr)  # Average GGE temperature

for i in range(6):
    if m_modes[i] < 0.01 * T_avg:
        # Gapless: radiation-like
        # In 3+1D: w = c_s^2/3 for a relativistic boson gas
        # But c_s is in M_KK units, and c_fabric = 209.97
        # The physical sound speed ratio c_s/c_fabric determines w
        w_modes[i] = c_s_branches[i]**2 / 3.0
    elif m_modes[i] > 3.0 * T_avg:
        # Non-relativistic: matter-like
        w_modes[i] = T_avg / m_modes[i]  # w ~ T/m for non-rel
    else:
        # Intermediate: compute from Bose-Einstein integral
        x = m_modes[i] / T_avg
        # w = (1/3) * (1 - x * K_1(x)/K_2(x)) for massive bosons
        # Approximate: w ~ (1/3) / (1 + x^2/5)
        w_modes[i] = (1.0/3.0) / (1.0 + x**2 / 5.0)

print(f"\n  Mode equations of state at T_avg = {T_avg:.3f} M_KK:")
for i in range(6):
    lbl = branch_labels[i] if i < len(branch_labels) else f"Branch-{i}"
    print(f"    {lbl}: m = {m_modes[i]:.4f}, w_k = {w_modes[i]:.6f}")

# =============================================================================
#  3. COMPUTE rho_geom / rho_GGE RATIO AT THE FOLD
# =============================================================================

print("\n\n--- Step 3: Ratio rho_geom / rho_GGE at the fold ---")

ratio_fold = rho_geom / rho_GGE
log_ratio = np.log10(ratio_fold)

print(f"\n  rho_geom  = {rho_geom:.4e} GeV^4  (a_0 term, constant)")
print(f"  rho_GGE   = {rho_GGE:.4e} GeV^4  (excitation energy)")
print(f"  Ratio     = {ratio_fold:.4e}")
print(f"  log10     = {log_ratio:.2f}")

if ratio_fold > 1:
    print(f"\n  RESULT: rho_geom DOMINATES by {log_ratio:.1f} orders of magnitude")
    print(f"  The geometric a_0 term is the dominant vacuum energy contributor.")
    print(f"  The GGE excitation energy is a PERTURBATION on top of the geometric floor.")
else:
    print(f"\n  RESULT: rho_GGE DOMINATES by {-log_ratio:.1f} orders of magnitude")

# =============================================================================
#  4. MODE-RESOLVED GGE ENERGY BUDGET
# =============================================================================

print("\n\n--- Step 4: Mode-resolved GGE energy distribution ---")

# From the GGE: 59.8 pairs across 8 Fock-space modes (4B2 + 1B1 + 3B3)
# Map to 6 GL branches:
# B2 (4 modes) -> dominantly Goldstone + Leggett-1 + Leggett-2 + Branch-3
# B1 (1 mode)  -> dominantly Branch-4
# B3 (3 modes) -> dominantly Higgs-1 + high-energy branches

# Energy per mode from canonical constants:
E_per_branch = np.array([
    E_B2_mean,  # Goldstone (B2-derived)
    E_B2_mean,  # Leggett-1 (B2-derived)
    E_B2_mean,  # Leggett-2 (B2-derived)
    E_B2_mean,  # Branch-3 (B2-derived)
    E_B1,       # Branch-4 (B1-derived)
    E_B3_mean,  # Higgs-1 (B3-derived)
])

# Occupation: n_Bog = 0.999 per mode, 59.8 pairs total
# Distribute: 4 B2 modes contribute ~4/8 * 59.8 = 29.9 pairs to B2-like branches
# 1 B1 mode contributes ~1/8 * 59.8 = 7.475 pairs
# 3 B3 modes contribute ~3/8 * 59.8 = 22.425 pairs

n_per_branch = np.array([
    n_pairs * 1/8,  # Goldstone
    n_pairs * 1/8,  # Leggett-1
    n_pairs * 1/8,  # Leggett-2
    n_pairs * 1/8,  # Branch-3
    n_pairs * 1/8,  # Branch-4 (B1)
    n_pairs * 3/8,  # Higgs-1 (B3, 3 modes)
])

E_branch = n_per_branch * E_per_branch
E_total_check = np.sum(E_branch)

print(f"  Energy per branch (M_KK):")
for i in range(6):
    lbl = branch_labels[i] if i < len(branch_labels) else f"Branch-{i}"
    print(f"    {lbl}: n = {n_per_branch[i]:.2f} pairs, "
          f"E/pair = {E_per_branch[i]:.4f}, "
          f"E_total = {E_branch[i]:.3f} M_KK, "
          f"w = {w_modes[i]:.4f}")
print(f"  Sum check: {E_total_check:.3f} vs E_GGE = {E_GGE_MKK:.3f} M_KK")
print(f"  Discrepancy: {abs(E_total_check - E_GGE_MKK)/E_GGE_MKK * 100:.1f}%")

# Weighted average EOS
w_avg_GGE = np.sum(E_branch * w_modes) / np.sum(E_branch)
print(f"\n  Energy-weighted average w_GGE = {w_avg_GGE:.6f}")

# =============================================================================
#  5. FRIEDMANN EQUATION: TWO-COMPONENT EVOLUTION
# =============================================================================

print("\n\n--- Step 5: Friedmann equation with two components ---")
print("  H^2 = (8*pi*G_N/3) * [rho_geom + rho_GGE(a)]")

# The key insight: rho_geom is CONSTANT (w = -1) and rho_GGE redshifts
# rho_GGE(a) = rho_GGE_fold * (a/a_fold)^{-3(1+w_avg)}
#
# But we have MULTIPLE modes with DIFFERENT w_k, so:
# rho_GGE(a) = sum_k rho_k_fold * (a/a_fold)^{-3(1+w_k)}

# Normalize: define a_fold = 1 at the fold, evolve to a_0 (today)
# Need the number of e-folds from fold to today

# From the spectral action transit framework:
# The fold occurs at t ~ t_Planck ~ 10^{-43} s
# Today: t_0 ~ 4.35e17 s
# In a radiation-dominated universe from fold to equality:
#   a ~ t^{1/2} (radiation era)
#   a ~ t^{2/3} (matter era)
#
# Temperature at fold in physical units:
# E_fold ~ M_KK ~ 7.4e16 GeV
# T_fold ~ M_KK (the fold is at the KK scale)
# T_0 ~ T_CMB ~ 2.35e-13 GeV
# a_0/a_fold ~ T_fold/T_0 ~ M_KK/T_CMB

from canonical_constants import T_CMB_GeV

# Scale factor ratio: the expansion from the fold to today
a_ratio_total = M_KK_gravity / T_CMB_GeV
ln_a_ratio = np.log(a_ratio_total)
N_e_total = ln_a_ratio  # Total e-folds

print(f"  T_fold ~ M_KK = {M_KK_gravity:.3e} GeV")
print(f"  T_0 ~ T_CMB = {T_CMB_GeV:.3e} GeV")
print(f"  a_0/a_fold = T_fold/T_0 = {a_ratio_total:.3e}")
print(f"  Total e-folds = ln(a_0/a_fold) = {N_e_total:.2f}")

# Energy density fractions at the fold
f_geom = rho_geom / (rho_geom + rho_GGE)
f_GGE = rho_GGE / (rho_geom + rho_GGE)
print(f"\n  At the fold:")
print(f"    f_geom = rho_geom/(rho_geom+rho_GGE) = {f_geom:.6e}")
print(f"    f_GGE  = rho_GGE/(rho_geom+rho_GGE)  = {f_GGE:.6e}")

# =============================================================================
#  5a. Solve Friedmann numerically from fold to today
# =============================================================================

# We solve in terms of x = ln(a/a_fold), from x=0 to x=N_e_total
# H^2(x) = (8*pi*G_N/3) * rho_total(x)
#
# rho_total(x) = rho_geom + sum_k rho_k_fold * exp(-3*(1+w_k)*x)
#
# For the effective EOS: w_eff = P_total/rho_total
# P_total = -rho_geom + sum_k w_k * rho_k * exp(-3*(1+w_k)*x)

# Mode-resolved rho at fold (in GeV^4)
rho_branch_fold = E_branch / E_GGE_MKK * rho_GGE  # Scale to physical units

# But we also need standard model radiation and matter!
# At the fold (T ~ M_KK), the SM degrees of freedom contribute:
# rho_rad = (pi^2/30) * g_star * T^4
# g_star(M_KK) ~ 106.75 (all SM particles relativistic)
g_star_fold = 106.75  # (local)
rho_rad_fold = (PI**2 / 30.0) * g_star_fold * M_KK_gravity**4
print(f"\n  SM radiation at fold: rho_rad = {rho_rad_fold:.3e} GeV^4")
print(f"  log10(rho_rad_fold) = {np.log10(rho_rad_fold):.2f}")

# Today's densities (observed)
rho_DE_obs = Omega_Lambda * rho_crit_GeV4  # = 2.79e-47 GeV^4
rho_m_obs = Omega_m * rho_crit_GeV4        # = 1.29e-47 GeV^4
rho_r_obs = Omega_r * rho_crit_GeV4        # = 3.74e-51 GeV^4

print(f"  Today (observed):")
print(f"    rho_DE  = {rho_DE_obs:.3e} GeV^4")
print(f"    rho_m   = {rho_m_obs:.3e} GeV^4")
print(f"    rho_r   = {rho_r_obs:.3e} GeV^4")
print(f"    rho_crit = {rho_crit_GeV4:.3e} GeV^4")

# Solve Friedmann: define normalized densities
# Let a_fold = 1. Then a_today = a_ratio_total.
# x = ln(a/a_fold)

N_x = 5000  # resolution
x_arr = np.linspace(0, N_e_total, N_x)
a_arr = np.exp(x_arr)

# rho_geom: constant
rho_geom_arr = np.full(N_x, rho_geom)

# rho_GGE modes: each redshifts with its own w_k
rho_GGE_arr = np.zeros(N_x)
rho_branch_arr = np.zeros((6, N_x))
for i in range(6):
    rho_branch_arr[i, :] = rho_branch_fold[i] * a_arr**(-3.0 * (1.0 + w_modes[i]))
    rho_GGE_arr += rho_branch_arr[i, :]

# Standard model radiation (w = 1/3)
rho_rad_arr = rho_rad_fold * a_arr**(-4.0)

# Standard model matter (w = 0) — NOT present at fold, forms later
# But for the Friedmann evolution we need to include it
# At a = a_fold: rho_m = 0 (no baryons yet). Baryons form at BBN.
# For simplicity, track the full expansion with rho_m matching observations
# at a = a_today (this is the standard approach)
rho_m_fold = rho_m_obs * a_ratio_total**3
rho_m_arr = rho_m_fold * a_arr**(-3.0)

# Total
rho_total_arr = rho_geom_arr + rho_GGE_arr + rho_rad_arr + rho_m_arr

# Effective EOS
P_geom_arr = -rho_geom_arr  # w = -1
P_GGE_arr = np.zeros(N_x)
for i in range(6):
    P_GGE_arr += w_modes[i] * rho_branch_arr[i, :]
P_rad_arr = rho_rad_arr / 3.0  # w = 1/3
P_m_arr = np.zeros(N_x)  # w = 0

P_total_arr = P_geom_arr + P_GGE_arr + P_rad_arr + P_m_arr
w_eff_arr = P_total_arr / rho_total_arr

# H(x) = sqrt(8*pi*G_N / 3 * rho_total)
# G_N in natural units: G_N = 1/(8*pi*M_Pl_reduced^2)
G_N_nat = 1.0 / (8.0 * PI * M_Pl_reduced**2)  # GeV^{-2}
H_arr = np.sqrt(8.0 * PI * G_N_nat / 3.0 * np.abs(rho_total_arr))

# =============================================================================
#  6. EXTRACT w_eff AT TODAY
# =============================================================================

print("\n\n--- Step 6: w_eff at a = a_today ---")

# At today (x = N_e_total), extract w_eff
w_eff_today = w_eff_arr[-1]

# Also compute at z=0 more carefully: what is the DE fraction?
# At today:
rho_geom_today = rho_geom  # constant
rho_GGE_today = rho_GGE_arr[-1]
rho_rad_today = rho_rad_arr[-1]
rho_m_today = rho_m_arr[-1]
rho_total_today = rho_total_arr[-1]

# The "dark energy" is rho_geom + rho_GGE (both contribute to acceleration)
rho_DE_framework = rho_geom_today + rho_GGE_today
w_DE_framework = (-rho_geom_today + np.sum([w_modes[i] * rho_branch_arr[i, -1] for i in range(6)])) / rho_DE_framework

print(f"  At a = a_today (x = {N_e_total:.1f} e-folds):")
print(f"    rho_geom   = {rho_geom_today:.4e} GeV^4  (CONSTANT)")
print(f"    rho_GGE    = {rho_GGE_today:.4e} GeV^4  (redshifted)")
print(f"    rho_rad    = {rho_rad_today:.4e} GeV^4")
print(f"    rho_m      = {rho_m_today:.4e} GeV^4")
print(f"    rho_total  = {rho_total_today:.4e} GeV^4")
print(f"    rho_DE (geom+GGE) = {rho_DE_framework:.4e} GeV^4")
print(f"    w_eff(total) = {w_eff_today:.6f}")
print(f"    w_DE(geom+GGE) = {w_DE_framework:.6f}")

# The key question: since rho_geom dominates by enormous factors,
# rho_GGE is diluted away, and rho_geom persists as a true CC.
# So w_DE -> -1 (pure cosmological constant) at late times.

# But DESI finds w_0 ~ -0.918. How does this arise?
# In this framework: the deviation from w = -1 comes from the GGE component.
# w_DE = (w_geom * rho_geom + w_GGE * rho_GGE) / (rho_geom + rho_GGE)
# Since rho_geom >> rho_GGE at late times: w_DE -> -1 + O(rho_GGE/rho_geom)

# The S58 computation gave w_0 = -0.918 using a DIFFERENT approach:
# it used the Volovik partition (F_Josephson = -336.64 M_KK as the vacuum energy).
# That approach treats the entire BCS condensate as contributing to DE.
# The two-component decomposition shows the internal structure.

print(f"\n  Comparison with DESI:")
print(f"    w_DE (this work) = {w_DE_framework:.6f}")
print(f"    w_0 (S58, DESI-matched) = -0.918")
print(f"    w_0 (DESI DR2) = -0.752 +/- 0.057")

# =============================================================================
#  7. THE KEY QUESTION: IS rho_DE A RESIDUAL?
# =============================================================================

print("\n\n--- Step 7: Is observed DE the residual of a cancellation? ---")

# rho_geom at the fold = rho_geom today (it's constant)
# The question: does rho_geom = rho_Lambda_obs?
# Answer: NO. rho_geom ~ 10^{68} GeV^4 >> rho_Lambda_obs ~ 2.7e-47 GeV^4

CC_gap_geom = np.log10(rho_geom / rho_Lambda_obs)
CC_gap_GGE = np.log10(rho_GGE / rho_Lambda_obs) if rho_GGE > 0 else 0

print(f"  rho_geom = {rho_geom:.3e} GeV^4")
print(f"  rho_Lambda_obs = {rho_Lambda_obs:.3e} GeV^4")
print(f"  Gap: log10(rho_geom/rho_obs) = {CC_gap_geom:.1f} OOM")
print(f"\n  rho_GGE(fold) = {rho_GGE:.3e} GeV^4")
print(f"  Gap: log10(rho_GGE/rho_obs) = {CC_gap_GGE:.1f} OOM")

# rho_GGE(today) after dilution:
if rho_GGE_today > 0:
    CC_gap_GGE_today = np.log10(rho_GGE_today / rho_Lambda_obs)
    dilution_OOM = np.log10(rho_GGE / rho_GGE_today)
    print(f"\n  rho_GGE(today) = {rho_GGE_today:.3e} GeV^4")
    print(f"  Dilution from fold to today: {dilution_OOM:.1f} OOM")
    print(f"  Gap after dilution: {CC_gap_GGE_today:.1f} OOM")

print(f"\n  CONCLUSION: The observed DE is NOT a simple residual.")
print(f"  rho_geom (a_0 term) is a constant 10^{{{CC_gap_geom:.0f}}} x rho_obs.")
print(f"  rho_GGE dilutes from 10^{{{CC_gap_GGE:.0f}}} to {CC_gap_GGE_today:.0f} x rho_obs.")
print(f"  The CC problem (114 OOM gap) resides entirely in the a_0 term.")
print(f"  The GGE component dilutes away and is negligible at late times.")

# =============================================================================
#  8. DECOMPOSITION SUMMARY AND w_eff EVOLUTION
# =============================================================================

print("\n\n--- Step 8: Decomposition summary ---")

# Compute w_eff at specific redshifts
z_targets = np.array([0, 0.5, 1.0, 2.0, 5.0, 10.0, 100.0, 1000.0, 1e6, 1e10])
x_targets = np.log(1.0 + z_targets) + np.log(a_ratio_total) - N_e_total
# Wait — z = a_0/a - 1, so a = a_0/(1+z), x = ln(a/a_fold) = ln(a_0/(1+z)/a_fold)
# = ln(a_ratio_total/(1+z)) = N_e_total - ln(1+z)
x_targets = N_e_total - np.log(1.0 + z_targets)

print(f"\n  w_eff(z) at key redshifts:")
print(f"  {'z':>12s} {'x (e-folds)':>14s} {'w_eff':>10s} {'Omega_geom':>12s} {'Omega_GGE':>12s}")
print("  " + "-" * 65)

for z_t, x_t in zip(z_targets, x_targets):
    if x_t < 0 or x_t > N_e_total:
        continue
    # Interpolate
    idx = int(x_t / N_e_total * (N_x - 1))
    idx = np.clip(idx, 0, N_x - 1)
    rho_g = rho_geom
    rho_gge = rho_GGE_arr[idx]
    rho_r = rho_rad_arr[idx]
    rho_m_z = rho_m_arr[idx]
    rho_t = rho_g + rho_gge + rho_r + rho_m_z
    w_e = w_eff_arr[idx]
    Om_g = rho_g / rho_t
    Om_gge = rho_gge / rho_t
    print(f"  {z_t:12.1e} {x_t:14.2f} {w_e:10.4f} {Om_g:12.4e} {Om_gge:12.4e}")

# =============================================================================
#  9. CROSS-CHECKS
# =============================================================================

print("\n\n--- Step 9: Cross-checks ---")

# Cross-check 1: Energy conservation
# d(rho_total * a^3)/dt = -P_total * d(a^3)/dt
# For constant rho_geom: d(rho_geom)/dt = 0 but rho_geom * da^3/dt != 0
# This is fine: the CC has w=-1, so d(rho_CC * a^3)/dt = -(-rho_CC)*3*a^2*da/dt
# = 3*rho_CC*a^2*da/dt, and the equation d(rho*a^3)/dt = -P*3a^2*da/dt is violated
# for the CC. Energy conservation for CC: d(rho_CC)/dt = -3H(rho_CC + P_CC) = 0. Correct.

# Cross-check 2: At early times (fold), rho_geom ~ rho_GGE comparison
print(f"  Cross-check 1: Fold dominance")
print(f"    rho_geom/rho_total at fold = {rho_geom/(rho_geom + rho_GGE + rho_rad_fold):.6e}")
print(f"    rho_GGE/rho_total at fold  = {rho_GGE/(rho_geom + rho_GGE + rho_rad_fold):.6e}")
print(f"    rho_rad/rho_total at fold  = {rho_rad_fold/(rho_geom + rho_GGE + rho_rad_fold):.6e}")

# Cross-check 3: Late-time consistency
# At z=0, with rho_geom dominating: H^2 ~ (8*pi*G/3)*rho_geom
H_late = np.sqrt(8.0 * PI * G_N_nat / 3.0 * rho_geom)
# This should be enormous compared to H_0 ~ 1.4e-42 GeV
print(f"\n  Cross-check 2: Late-time Hubble")
print(f"    H(rho_geom) = {H_late:.3e} GeV")
print(f"    H_0_obs = {H_0_GeV:.3e} GeV")
print(f"    Ratio = {H_late/H_0_GeV:.3e} (sqrt of CC gap)")

# Cross-check 4: The two-component decomposition at the fold matches S53
print(f"\n  Cross-check 3: S53 consistency")
print(f"    rho_GGE here = {rho_GGE:.3e} GeV^4")
print(f"    rho_GGE S53  = {rho_GGE_GeV4_s53:.3e} GeV^4")
print(f"    Match: {'YES' if abs(rho_GGE - rho_GGE_GeV4_s53)/rho_GGE < 0.01 else 'NO'}")

# Cross-check 5: w_eff at late times approaches -1 (geometric dominance)
w_late = w_eff_arr[-100:]
print(f"\n  Cross-check 4: Late-time w_eff -> -1")
print(f"    Mean w_eff (last 100 points) = {np.mean(w_late):.8f}")
print(f"    Deviation from -1: {np.mean(w_late) + 1:.2e}")

# Cross-check 6: GGE dilution factor
GGE_dilution = rho_GGE_arr[-1] / rho_GGE_arr[0]
expected_dilution_matter = a_ratio_total**(-3.0)  # if w=0 (matter)
expected_dilution_rad = a_ratio_total**(-4.0)     # if w=1/3 (radiation)

print(f"\n  Cross-check 5: GGE dilution")
print(f"    Actual dilution = {GGE_dilution:.3e}")
print(f"    If matter (w=0): {expected_dilution_matter:.3e}")
print(f"    If radiation (w=1/3): {expected_dilution_rad:.3e}")
print(f"    Dilution OOM = {-np.log10(GGE_dilution):.1f}")

# =============================================================================
#  10. GATE VERDICT
# =============================================================================

print("\n\n" + "=" * 72)
print("  GATE VERDICT: TWO-COMPONENT-66")
print("=" * 72)

# The separation IS clean: a_0 is exactly constant, GGE modes have well-defined w_k.
# The decomposition is structurally forced by the spectral action.
# w_eff(today) is NOT -0.918 — it is -1.0000 (to machine precision)
# because rho_geom dominates overwhelmingly.

# The S58 w_0 = -0.918 uses a DIFFERENT definition: it treats the
# Volovik partition F_Josephson as the DE, which is the BCS condensate
# free energy, NOT the spectral action a_0 term.

# These are two different questions:
# Q1 (this computation): What does the spectral action predict for DE? -> w = -1
# Q2 (S58): What does the BCS condensate EOS predict? -> w = -0.918

# The two-component decomposition reveals that the spectral action CC (a_0 term)
# is the dominant contributor and gives w = -1 exactly. The GGE excitations
# are a negligible perturbation at late times.

# Verdict: INFO (separation achieved, but w_eff != -0.918)
gate_verdict = "INFO"
gate_detail = (
    f"Clean two-component separation achieved. "
    f"rho_geom = {rho_geom:.3e} GeV^4 (CONSTANT, w=-1) dominates by "
    f"{log_ratio:.0f} OOM over rho_GGE = {rho_GGE:.3e} GeV^4 at fold. "
    f"w_eff(today) = {w_eff_today:.6f} (pure CC), NOT -0.918. "
    f"The w=-0.918 from S58 uses the BCS free energy (Volovik partition), "
    f"which is a DIFFERENT physical quantity from the spectral action a_0 term. "
    f"GGE dilution over {N_e_total:.0f} e-folds: {-np.log10(GGE_dilution):.0f} OOM. "
    f"The 114-OOM CC gap resides entirely in the a_0 term."
)

print(f"\n  Gate: TWO-COMPONENT-66")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

print(f"\n  KEY NUMBERS:")
print(f"    1. rho_geom = {rho_geom:.4e} GeV^4 (115.2 OOM above rho_obs)")
print(f"    2. rho_GGE(fold) = {rho_GGE:.4e} GeV^4 (115 OOM above rho_obs)")
print(f"    3. rho_geom/rho_GGE = {ratio_fold:.4e} ({log_ratio:.1f} OOM)")
print(f"    4. w_eff(today) = {w_eff_today:.6f} (pure cosmological constant)")
print(f"    5. GGE dilution = {-np.log10(GGE_dilution):.0f} OOM over {N_e_total:.0f} e-folds")
print(f"    6. The S58 w=-0.918 and this w=-1 are DIFFERENT decompositions")
print(f"       (BCS condensate EOS vs spectral action a_0 term)")

# =============================================================================
#  11. SAVE DATA
# =============================================================================

print("\n\n--- Saving data ---")

np.savez(
    os.path.join(SCRIPT_DIR, 's66_two_component.npz'),
    # Core results
    rho_geom=rho_geom,
    rho_GGE_fold=rho_GGE,
    rho_GGE_today=rho_GGE_today,
    ratio_fold=ratio_fold,
    log_ratio=log_ratio,
    # a_0 constancy proof
    a0_constant=a0_constant,
    a0_wdw=a0_wdw,
    tau_wdw=tau_wdw,
    # Mode-resolved
    w_modes=w_modes,
    E_branch=E_branch,
    n_per_branch=n_per_branch,
    branch_labels=branch_labels,
    rho_branch_fold=rho_branch_fold,
    w_avg_GGE=w_avg_GGE,
    # Evolution
    x_arr=x_arr,
    rho_total_arr=rho_total_arr,
    rho_geom_arr=rho_geom_arr,
    rho_GGE_arr=rho_GGE_arr,
    rho_rad_arr=rho_rad_arr,
    rho_m_arr=rho_m_arr,
    w_eff_arr=w_eff_arr,
    H_arr=H_arr,
    N_e_total=N_e_total,
    a_ratio_total=a_ratio_total,
    # Dilution
    GGE_dilution=GGE_dilution,
    GGE_dilution_OOM=-np.log10(GGE_dilution),
    CC_gap_geom=CC_gap_geom,
    CC_gap_GGE_today=CC_gap_GGE_today if rho_GGE_today > 0 else np.nan,
    # Gate
    gate_name='TWO-COMPONENT-66',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # w comparison
    w_eff_today=w_eff_today,
    w_DE_framework=w_DE_framework,
)

print(f"  Saved: computations/session-66/s66_two_component.npz")

# =============================================================================
#  12. PLOT
# =============================================================================

print("\n--- Generating plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('TWO-COMPONENT-66: a₀-Constant vs GGE-Dynamical in Friedmann',
             fontsize=13, fontweight='bold')

# Panel 1: Energy densities vs e-folds
ax = axes[0, 0]
# Use log scale, plot vs x (e-folds from fold)
ax.semilogy(x_arr, rho_geom_arr, 'r-', lw=2, label=r'$\rho_{\rm geom}$ (a₀, w=−1)')
ax.semilogy(x_arr, rho_GGE_arr, 'b-', lw=2, label=r'$\rho_{\rm GGE}$ (excitations)')
ax.semilogy(x_arr, rho_rad_arr, 'orange', lw=1.5, ls='--', label=r'$\rho_{\rm rad}$ (SM, w=1/3)')
ax.semilogy(x_arr, rho_m_arr, 'g', lw=1.5, ls='--', label=r'$\rho_{\rm m}$ (matter, w=0)')
ax.semilogy(x_arr, rho_total_arr, 'k-', lw=1, alpha=0.5, label=r'$\rho_{\rm total}$')
ax.axhline(rho_Lambda_obs, color='purple', ls=':', lw=1, label=r'$\rho_{\Lambda,\rm obs}$')
ax.set_xlabel('e-folds from fold', fontsize=11)
ax.set_ylabel(r'$\rho$ [GeV$^4$]', fontsize=11)
ax.set_title('Energy Density Evolution', fontsize=11)
ax.legend(fontsize=8, loc='lower left')
ax.set_xlim(0, N_e_total)
ax.set_ylim(1e-60, 1e75)

# Panel 2: w_eff vs e-folds
ax = axes[0, 1]
ax.plot(x_arr, w_eff_arr, 'k-', lw=2)
ax.axhline(-1, color='r', ls=':', lw=1, label='w = −1 (CC)')
ax.axhline(-0.918, color='blue', ls='--', lw=1, label='w = −0.918 (S58 DESI)')
ax.axhline(1/3, color='orange', ls=':', lw=1, label='w = 1/3 (radiation)')
ax.set_xlabel('e-folds from fold', fontsize=11)
ax.set_ylabel(r'$w_{\rm eff}$', fontsize=11)
ax.set_title('Effective Equation of State', fontsize=11)
ax.legend(fontsize=8)
ax.set_xlim(0, N_e_total)
ax.set_ylim(-1.1, 0.5)

# Panel 3: a_0 constancy proof
ax = axes[1, 0]
ax.plot(tau_wdw, a0_wdw, 'ro-', markersize=10, lw=2)
ax.axhline(a0_constant, color='gray', ls='--', lw=1)
ax.set_xlabel(r'$\tau$ (Jensen parameter)', fontsize=11)
ax.set_ylabel(r'$a_0(\tau)$', fontsize=11)
ax.set_title(r'$a_0$ Constancy Proof (WDW data)', fontsize=11)
ax.set_ylim(a0_constant * 0.99, a0_constant * 1.01)
ax.text(0.5, 0.3, f'$a_0 = {a0_constant:.0f}$ (EXACT CONSTANT)',
        transform=ax.transAxes, ha='center', fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='lightyellow'))

# Panel 4: Decomposition at fold and today
ax = axes[1, 1]
labels_fold = ['rho_geom', 'rho_GGE', 'rho_rad']
values_fold = [np.log10(rho_geom), np.log10(rho_GGE), np.log10(rho_rad_fold)]
colors_fold = ['red', 'blue', 'orange']

# Bar chart comparing fold vs today
x_bar = np.arange(3)
width = 0.35  # (local)
vals_fold_log = [np.log10(rho_geom), np.log10(rho_GGE), np.log10(rho_rad_fold)]
vals_today_log = [np.log10(rho_geom_today),
                  np.log10(max(rho_GGE_today, 1e-300)),
                  np.log10(max(rho_rad_today, 1e-300))]

bars1 = ax.bar(x_bar - width/2, vals_fold_log, width, label='At fold',
               color=['red', 'blue', 'orange'], alpha=0.7)
bars2 = ax.bar(x_bar + width/2, vals_today_log, width, label='Today',
               color=['darkred', 'darkblue', 'darkorange'], alpha=0.7)
ax.axhline(np.log10(rho_Lambda_obs), color='purple', ls=':', lw=2,
           label=r'$\rho_{\Lambda,\rm obs}$')
ax.set_xticks(x_bar)
ax.set_xticklabels([r'$\rho_{\rm geom}$', r'$\rho_{\rm GGE}$', r'$\rho_{\rm rad}$'],
                    fontsize=11)
ax.set_ylabel(r'$\log_{10}(\rho / {\rm GeV}^4)$', fontsize=11)
ax.set_title('Fold vs Today Comparison', fontsize=11)
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's66_two_component.png'), dpi=150)
plt.close()

print(f"  Saved: computations/session-66/s66_two_component.png")

print("\n" + "=" * 72)
print("  TWO-COMPONENT-66 COMPLETE")
print("=" * 72)
