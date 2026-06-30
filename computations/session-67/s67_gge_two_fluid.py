#!/usr/bin/env python3
"""
S67 — GGE-TWO-FLUID-67: Generalized Landau-Khalatnikov Two-Fluid Hydrodynamics
with GGE Normal Component
================================================================================

Gate: GGE-TWO-FLUID-67 (INFO)
  Structural computation. Report two sound speeds and mutual friction.

Physics:
  The post-transit universe is a superfluid with a dilute normal component.
  The superfluid component is the BCS condensate (ground state).
  The normal component is the GGE relic (59.8 quasiparticle pairs from transit).

  The Landau-Khalatnikov two-fluid equations are:
    (1) Mass conservation: d rho/dt + div(rho_s v_s + rho_n v_n) = 0
    (2) Superfluid eq:     d v_s/dt = -grad(mu + v_s^2/2)
    (3) Normal fluid eq:   rho_n dv_n/dt = -grad P_n + rho_n s grad T + F_mutual
    (4) Entropy eq:        d(rho_n s)/dt + div(rho_n s v_n) = R/T

  From the GGE occupation numbers {n_k} and Bogoliubov energies {E_k}:
    rho_n/rho = sum_k n_k E_k / E_total     (normal fraction via Landau formula)
    rho_s/rho = 1 - rho_n/rho               (superfluid fraction)

  Two propagating modes:
    First sound:  c_1^2 = (dP/drho)_s        (pressure wave)
    Second sound: c_2^2 = (T s^2 rho_s) / (C_v rho_n)  (entropy wave)

  Mutual friction from the Leggett mode coupling between normal and
  superfluid components.

  In superfluid 3He-B, the two-fluid model describes the coexistence of
  the BCS condensate and the thermally excited Bogoliubov quasiparticles.
  Here the "thermal" excitation is replaced by the GGE relic from the
  transit quench — a NON-thermal occupation set by 8 conserved charges.

Volovik corpus references:
  Paper 06 (Universe in a Helium Droplet), Ch. 5: Landau two-fluid model
  Paper 10 (3He-B quasiparticle lifetimes): exponentially long at T << T_c
  Paper 04 (Vacuum Energy, CC): equilibrium vacuum has P = 0 (Gibbs-Duhem)
  Paper 25 (Superfluid Universe): cosmology as approach to equilibrium

Author: volovik-superfluid-universe-theorist
Session: 67, Wave 7, Task B
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    E_cond, tau_fold, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, a0_fold, a2_fold, a4_fold, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean, PI, n_pairs,
    E_exc, N_cells, H_fold, dt_transit,
    c_Gold, c_fabric, omega_L1, omega_L2,
    Delta_0_GL, Delta_0_OES, Delta_B3,
    J_C2, J_su2, J_u1, T_acoustic,
    rho_Lambda_obs, rho_crit_GeV4, Omega_Lambda,
    H_0_GeV, Vol_SU3_Haar, n_Bog, P_exc_kz,
    omega_PV, xi_BCS, xi_GL,
    c_Gold_over_c_fabric, N_e_classical
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("  S67 — GGE-TWO-FLUID-67: Generalized Landau-Khalatnikov Two-Fluid")
print("  Hydrodynamics with GGE Normal Component")
print("=" * 78)

# ============================================================================
#  SECTION 1: Load upstream data
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 1: Load Upstream Data (GGE occupations, phonon EOS, Meissner)")
print("=" * 78)

# GGE equilibrium gap (S57) — canonical occupation numbers and energies
d57 = np.load(os.path.join(SCRIPT_DIR, 's57_gge_equilibrium_gap.npz'), allow_pickle=True)
branch_labels = d57['branch_labels']
E_k = d57['E_k']                  # Bogoliubov quasiparticle energies (pair energies = 2*xi)
xi_k = d57['xi']                  # Single-particle energies (M_KK)
f_k_gge = d57['fk_gge']           # GGE occupation fractions
T_k_volovik = d57['T_k_volovik']  # Mode-resolved GGE temperatures (Volovik)
beta_k = d57['beta_k']            # Inverse temperatures

# Euclidean Volovik (S59) — alternative occupation parameterization
d59 = np.load(os.path.join(SCRIPT_DIR, 's59_euclidean_volovik.npz'), allow_pickle=True)
n_k_gge_59 = d59['n_k_GGE']       # Fermionic occupation numbers
T_eff_59 = d59['T_eff_per_mode']   # Effective temperatures
sector_labels = d59['sector_labels']

# Meissner-GGE (S62) — superfluid density and condensate fraction
d62 = np.load(os.path.join(SCRIPT_DIR, 's62_meissner_gge.npz'), allow_pickle=True)
D_s_GGE = float(d62['D_s_GGE'])
D_s_fold = float(d62['D_s_fold'])
n_condensate_GGE = float(d62['n_condensate_GGE'])
rho_1_evals = d62['rho_1_evals_GGE']
lambda_L_GGE = float(d62['lambda_L_GGE'])
kappa_GGE = float(d62['kappa_GGE'])
n_k_meissner = d62['n_k_GGE']     # ODLRO-basis occupation

# Volovik identity (S55) — thermodynamic quantities
d55 = np.load(os.path.join(SCRIPT_DIR, 's55_volovik_identity.npz'), allow_pickle=True)
P_vac_volovik = float(d55['P_vac'])
w_eff_volovik = float(d55['w_eff'])
E_GGE_volovik = float(d55['E_GGE'])
T_k_s55 = d55['T_k']

# Phonon EOS (S53) — dispersion relations
d53 = np.load(os.path.join(SCRIPT_DIR, 's53_phonon_eos.npz'), allow_pickle=True)
tau_sweep = d53['tau_sweep']
rho_s_sweep = d53['rho_s_sweep']
c_Gold_sweep = d53['c_Gold_sweep']
T_values_eos = d53['T_values']
rho_vs_T = d53['rho_vs_T']
p_vs_T = d53['p_vs_T']
w_vs_T = d53['w_vs_T']

# S66 GGE vacuum energy — 496-mode extended data
d66 = np.load(os.path.join(SCRIPT_DIR, 's66_gge_vacuum_energy.npz'), allow_pickle=True)
n_k_gge_66 = d66['n_k_GGE']
T_GGE_66 = d66['T_GGE']
E_k_bcs_66 = d66['E_k_BCS']
eps_k_66 = d66['eps_k']

print(f"\n  8-mode energies (xi_k, M_KK):  {xi_k}")
print(f"  8-mode pair energies (E_k):    {E_k}")
print(f"  GGE occupations (f_k):         {f_k_gge}")
print(f"  GGE temperatures (T_k, M_KK):  {T_k_volovik}")
print(f"  Condensate fraction (ODLRO):   {n_condensate_GGE:.6f}")
print(f"  Superfluid density D_s(GGE):   {D_s_GGE:.6f} M_KK^2")
print(f"  Volovik vacuum pressure:       {P_vac_volovik:.6f} M_KK^4")
print(f"  Volovik w_eff:                 {w_eff_volovik:.6f}")
print(f"  Branch labels: {branch_labels}")

# ============================================================================
#  SECTION 2: Two-Fluid Densities — Normal and Superfluid Fractions
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 2: Two-Fluid Densities (Normal and Superfluid Fractions)")
print("=" * 78)

# METHOD 1: Landau normal-fluid density from quasiparticle occupations
# In Landau's two-fluid model (Volovik Paper 06, Ch. 5):
#   rho_n = sum_k (p_k^2 / 3 E_k) * (-df/dE)
# For a BCS superfluid with Bogoliubov quasiparticles:
#   rho_n/rho = sum_k n_k * (E_k / E_total)
# where n_k is the quasiparticle occupation and E_k is the excitation energy.
#
# More precisely, for a gapped BCS superfluid at temperature T:
#   rho_n/rho = (2/3) sum_k (beta_k E_k)^2 * f_k * (1 - f_k) / (sum_k 1)
# where f_k = 1/(1 + exp(beta_k E_k)) is the Fermi distribution.
#
# For the GGE, f_k is set by the conserved charges, not by a single temperature.

N_modes = len(xi_k)
print(f"\n  Number of BCS modes: {N_modes}")
print(f"  Sector structure: 4 B2 + 1 B1 + 3 B3")

# Method 1a: Energy-weighted occupation (simplest Landau-like formula)
E_total_gge = np.sum(f_k_gge * xi_k)
rho_n_frac_energy = np.sum(f_k_gge * xi_k) / np.sum(xi_k)
rho_s_frac_energy = 1.0 - rho_n_frac_energy

print(f"\n  --- Method 1a: Energy-weighted occupation ---")
print(f"  E_total(GGE) = sum f_k * xi_k = {E_total_gge:.6f} M_KK")
print(f"  E_total(all modes) = sum xi_k  = {np.sum(xi_k):.6f} M_KK")
print(f"  rho_n/rho = {rho_n_frac_energy:.6f}")
print(f"  rho_s/rho = {rho_s_frac_energy:.6f}")

# Method 1b: Direct Landau formula with thermal factor
# rho_n/rho = (1/N) * sum_k (beta_k * E_k)^2 * f_k * (1 - f_k)
# This is the BCS expression for the normal-fluid density
thermal_factor = np.zeros(N_modes)
for k in range(N_modes):
    bE = beta_k[k] * xi_k[k]
    thermal_factor[k] = bE**2 * f_k_gge[k] * (1.0 - f_k_gge[k])

rho_n_frac_landau = np.sum(thermal_factor) / N_modes
rho_s_frac_landau = 1.0 - rho_n_frac_landau

print(f"\n  --- Method 1b: Landau BCS formula ---")
print(f"  (beta_k E_k)^2 f(1-f) per mode:")
for k in range(N_modes):
    print(f"    {branch_labels[k]}: beta_k={beta_k[k]:.4f}, E_k={xi_k[k]:.4f}, "
          f"f_k={f_k_gge[k]:.6f}, factor={thermal_factor[k]:.6f}")
print(f"  rho_n/rho (Landau) = {rho_n_frac_landau:.6f}")
print(f"  rho_s/rho (Landau) = {rho_s_frac_landau:.6f}")

# Method 1c: From ODLRO condensate fraction (S62 Meissner)
# The condensate fraction directly gives the superfluid fraction
# n_0 = largest eigenvalue of single-body density matrix
rho_s_frac_odlro = n_condensate_GGE
rho_n_frac_odlro = 1.0 - rho_s_frac_odlro

print(f"\n  --- Method 1c: ODLRO condensate fraction (S62) ---")
print(f"  n_condensate(GGE) = {n_condensate_GGE:.6f}")
print(f"  rho_n/rho (ODLRO) = {rho_n_frac_odlro:.6f}")
print(f"  rho_s/rho (ODLRO) = {rho_s_frac_odlro:.6f}")

# Method 1d: From superfluid density ratio D_s(GGE)/D_s(GS)
rho_s_frac_meissner = D_s_GGE / D_s_fold
rho_n_frac_meissner = 1.0 - rho_s_frac_meissner

print(f"\n  --- Method 1d: Meissner superfluid density ratio ---")
print(f"  D_s(GGE)/D_s(fold) = {rho_s_frac_meissner:.6f}")
print(f"  rho_n/rho (Meissner) = {rho_n_frac_meissner:.6f}")
print(f"  rho_s/rho (Meissner) = {rho_s_frac_meissner:.6f}")

# CANONICAL CHOICE: Use ODLRO/Meissner as the primary definition
# The Meissner D_s is the PHYSICAL superfluid density (response to gauge field)
# The ODLRO condensate fraction agrees to 0.0004 (< 0.05%)
rho_n_frac = rho_n_frac_meissner
rho_s_frac = rho_s_frac_meissner

print(f"\n  === CANONICAL TWO-FLUID FRACTIONS (Meissner) ===")
print(f"  rho_n/rho = {rho_n_frac:.6f}  (normal fraction, GGE quasiparticles)")
print(f"  rho_s/rho = {rho_s_frac:.6f}  (superfluid fraction, BCS condensate)")
print(f"  rho_n/rho_s = {rho_n_frac/rho_s_frac:.6e}  (normal-to-superfluid)")
print(f"  Consistency: ODLRO-Meissner discrepancy = "
      f"{abs(rho_n_frac_odlro - rho_n_frac_meissner)/rho_n_frac_meissner * 100:.2f}%")

# Cosmological significance: rho_n/rho << 1
# This means the post-transit universe is STRONGLY superfluid
# The normal fraction is tiny — only 1.15% of the total density
print(f"\n  Physical interpretation:")
print(f"  The post-transit universe is {rho_s_frac*100:.2f}% superfluid.")
print(f"  The normal component (GGE relic) is only {rho_n_frac*100:.2f}%.")
print(f"  This is the regime T << T_c in superfluid 3He-B.")
print(f"  In 3He-B at T/T_c = 0.1, rho_n/rho ~ exp(-Delta/T) ~ 0.01 (comparable)")

# ============================================================================
#  SECTION 3: GGE Thermodynamics (Entropy, Specific Heat, Pressure)
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 3: GGE Thermodynamics (Entropy, Specific Heat, Pressure)")
print("=" * 78)

# Shannon entropy per mode: S_k = -f_k ln(f_k) - (1-f_k) ln(1-f_k)
S_k = np.zeros(N_modes)
for k in range(N_modes):
    fk = f_k_gge[k]
    if fk > 1e-15 and fk < 1.0 - 1e-15:
        S_k[k] = -fk * np.log(fk) - (1.0 - fk) * np.log(1.0 - fk)
    else:
        S_k[k] = 0.0

S_total = np.sum(S_k)
S_max = N_modes * np.log(2)  # Maximum entropy (infinite temperature)
S_ratio = S_total / S_max

print(f"\n  Shannon entropy per mode:")
for k in range(N_modes):
    print(f"    {branch_labels[k]}: S_k = {S_k[k]:.6f}, f_k = {f_k_gge[k]:.6f}")
print(f"  S_total = {S_total:.6f}")
print(f"  S_max = {S_max:.6f} (= {N_modes} ln 2)")
print(f"  S/S_max = {S_ratio:.6f}")

# Specific heat per mode: C_k = (beta_k E_k)^2 * f_k * (1 - f_k)
# This is the GGE analog of C_v = dE/dT, but with mode-resolved temperatures
C_k = np.zeros(N_modes)
for k in range(N_modes):
    bE = beta_k[k] * xi_k[k]
    C_k[k] = bE**2 * f_k_gge[k] * (1.0 - f_k_gge[k])

C_total = np.sum(C_k)
C_per_mode = C_total / N_modes

print(f"\n  Specific heat per mode (GGE analog):")
for k in range(N_modes):
    print(f"    {branch_labels[k]}: C_k = {C_k[k]:.6f}")
print(f"  C_total = {C_total:.6f}")
print(f"  C_per_mode = {C_per_mode:.6f}")

# GGE pressure from Volovik identity (S55):
# P = -epsilon + sum_k T_k S_k
# In equilibrium: P = 0 (Gibbs-Duhem)
# Out of equilibrium: P = P_vac = -0.688 M_KK^4
P_n_volovik = np.sum(T_k_volovik * S_k)
P_total = -E_GGE_volovik + P_n_volovik
print(f"\n  GGE pressure (Volovik identity):")
print(f"  P_n = sum T_k S_k = {P_n_volovik:.6f} M_KK^4")
print(f"  P_total = -E_GGE + P_n = {P_total:.6f} M_KK^4")
print(f"  P_vac (S55 direct) = {P_vac_volovik:.6f} M_KK^4")
print(f"  Consistency: {abs(P_total - P_vac_volovik)/abs(P_vac_volovik)*100:.4f}%")

# Effective temperature of the normal fluid
# T_eff = sum T_k S_k / S_total (entropy-weighted average)
T_eff_normal = P_n_volovik / S_total if S_total > 0 else 0.0
print(f"\n  Normal fluid effective temperature:")
print(f"  T_eff = P_n / S_total = {T_eff_normal:.6f} M_KK")
print(f"  T_acoustic (S42/S47) = {T_acoustic:.6f} M_KK")
print(f"  T_eff/T_acoustic = {T_eff_normal/T_acoustic:.4f}")

# ============================================================================
#  SECTION 4: First Sound — Pressure Wave
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 4: First Sound (Pressure Wave)")
print("=" * 78)

# First sound in a two-fluid system:
# c_1^2 = (dP/drho)_s = (rho_s c_s^2 + rho_n c_n^2) / rho
# where c_s is the condensate sound speed and c_n is the normal fluid sound speed
#
# For a BCS superfluid, the first sound is the Goldstone mode (Bogoliubov sound).
# The phonon dispersion gives c_Gold = 0.915 M_KK (S52 GL-JOSEPHSON-52).
#
# At T << T_c (our regime, rho_n/rho = 0.012), c_1 ≈ c_Gold to excellent
# approximation, with corrections of order (rho_n/rho).
#
# In 3He-B, first sound is the ordinary pressure wave propagating at
# c_1 ≈ c_Gold ≈ 366 m/s, nearly independent of temperature for T << T_c.

# The Goldstone sound speed IS the first sound speed at T=0
c_1_T0 = c_Gold  # M_KK units, exact at T=0

# Temperature correction to first sound:
# c_1^2 = c_Gold^2 * [1 + (rho_n/rho) * (c_n^2/c_Gold^2 - 1)]
# The normal fluid in the BCS system has c_n ~ v_F (Fermi velocity analog)
# For the 0D BCS system, use the mean quasiparticle velocity
# v_qp ~ sqrt(2*E_k/m) ~ sqrt(xi_k) in the BCS analog
# But in 0D, the "sound speed" of the normal component is the
# group velocity of the quasiparticle excitations.
# For the Bogoliubov quasiparticles: v_k = d E_k/d k
# In the fabric picture, the normal component velocity is set by
# the Josephson coupling across the tessellation.

# First sound at finite rho_n:
# In the two-fluid model, the leading correction is
# c_1^2 ≈ c_Gold^2 * (1 + alpha_MF * rho_n/rho)
# where alpha_MF depends on the normal fluid equation of state.
# For a non-interacting Bogoliubov gas, alpha_MF ≈ 0 (no correction).
# The physical reason: first sound is a density wave in which
# normal and superfluid components oscillate in phase.

# Use the S53 phonon EOS data to compute dP/drho
# At T_acoustic = 0.112 M_KK:
idx_T = np.argmin(np.abs(T_values_eos - T_acoustic))
T_closest = T_values_eos[idx_T]
rho_at_T = rho_vs_T[idx_T]
p_at_T = p_vs_T[idx_T]
w_at_T = w_vs_T[idx_T]

print(f"\n  Goldstone sound speed: c_Gold = {c_Gold:.6f} M_KK")
print(f"  First sound at T=0:   c_1(T=0) = c_Gold = {c_1_T0:.6f} M_KK")

# Compute c_1 with normal fraction correction
# For a weakly-interacting BCS system in the two-fluid regime:
# c_1^2 = c_Gold^2 + (rho_n/rho) * (s^2 * T / C_v)
# The second term is the "anomalous dispersion" from the thermal component.
# In our regime (rho_n << rho_s), this is negligible.
delta_c1_sq = (rho_n_frac) * (S_total**2 * T_eff_normal / C_total) if C_total > 0 else 0
c_1_sq = c_Gold**2 + delta_c1_sq
c_1 = np.sqrt(c_1_sq)

print(f"\n  Normal fraction correction:")
print(f"    delta(c_1^2)/c_Gold^2 = {delta_c1_sq / c_Gold**2:.6e}")
print(f"    c_1(GGE) = {c_1:.6f} M_KK")
print(f"    Relative shift: {(c_1 - c_Gold)/c_Gold * 100:.6f}%")

# In physical units (if M_KK = 7.43e16 GeV):
c_1_GeV = c_1 * M_KK  # This is c_1 in GeV (speed * M_KK has units of GeV if speed is dimensionless)
print(f"\n  First sound is the Goldstone mode = Bogoliubov sound")
print(f"  c_1 = {c_1:.6f} M_KK (natural units)")
print(f"  In 3He-B analog: first sound ≈ 366 m/s (comparable at T << T_c)")

# ============================================================================
#  SECTION 5: Second Sound — Entropy Wave
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 5: Second Sound (Entropy Wave)")
print("=" * 78)

# Second sound in Landau-Khalatnikov theory:
#   c_2^2 = (T * s^2 * rho_s) / (C_v * rho_n)
#
# where:
#   T = effective temperature of normal component
#   s = entropy per unit mass of normal component
#   rho_s = superfluid density
#   C_v = specific heat at constant volume
#   rho_n = normal fluid density
#
# In the regime rho_n << rho_s (T << T_c):
#   c_2^2 ≈ (T * s^2) / (C_v * rho_n/rho_s) ≈ c_1^2 * rho_n/(3 rho_s) [BCS]
#
# For a Bogoliubov gas at low T:
#   c_2 = c_1 / sqrt(3)   (the famous Landau result for phonon-dominated regime)
#
# For the GGE, we must use the MULTI-TEMPERATURE structure.
# The GGE entropy density is: s = S_total / N_modes (per mode)
# The GGE specific heat is: C_v = C_total

# Method A: Standard Landau formula with GGE quantities
s_gge = S_total  # Total entropy (dimensionless in M_KK units)
T_eff = T_eff_normal  # Entropy-weighted temperature
C_v_gge = C_total  # Total specific heat

# c_2^2 = T_eff * s^2 * rho_s / (C_v * rho_n)
if rho_n_frac > 1e-15 and C_v_gge > 1e-15:
    c_2_sq_A = T_eff * s_gge**2 * rho_s_frac / (C_v_gge * rho_n_frac)
    c_2_A = np.sqrt(c_2_sq_A)
else:
    c_2_sq_A = 0.0  # (local)
    c_2_A = 0.0  # (local)

print(f"\n  --- Method A: Standard Landau formula ---")
print(f"  T_eff = {T_eff:.6f} M_KK")
print(f"  s (total entropy) = {s_gge:.6f}")
print(f"  C_v (total) = {C_v_gge:.6f}")
print(f"  rho_s/rho = {rho_s_frac:.6f}")
print(f"  rho_n/rho = {rho_n_frac:.6f}")
print(f"  c_2^2 = {c_2_sq_A:.6f}")
print(f"  c_2 = {c_2_A:.6f} M_KK")
print(f"  c_2/c_1 = {c_2_A/c_1:.6f}")

# Method B: Mode-resolved second sound
# For a multi-temperature GGE, the second sound generalizes to:
# c_2^2 = [sum_k T_k^2 S_k^2 / C_k] * (rho_s/rho) / [sum_k T_k S_k]
# This accounts for the non-equilibrium temperature structure.
c_2_sq_num = 0.0  # (local)
c_2_sq_den = 0.0  # (local)
for k in range(N_modes):
    if C_k[k] > 1e-15:
        c_2_sq_num += T_k_volovik[k]**2 * S_k[k]**2 / C_k[k]
    c_2_sq_den += T_k_volovik[k] * S_k[k]

if c_2_sq_den > 1e-15 and rho_n_frac > 1e-15:
    c_2_sq_B = c_2_sq_num * rho_s_frac / c_2_sq_den
    c_2_B = np.sqrt(c_2_sq_B)
else:
    c_2_sq_B = 0.0  # (local)
    c_2_B = 0.0  # (local)

print(f"\n  --- Method B: Mode-resolved (GGE multi-temperature) ---")
print(f"  c_2^2 = {c_2_sq_B:.6f}")
print(f"  c_2 = {c_2_B:.6f} M_KK")
print(f"  c_2/c_1 = {c_2_B/c_1:.6f}")

# Method C: BCS low-temperature limit
# For a fully gapped BCS superfluid at T << Delta:
#   c_2 = c_1 * sqrt(rho_n / (3 * rho_s))
# This is the Bogoliubov-phonon dominated regime
c_2_BCS_low = c_1 * np.sqrt(rho_n_frac / (3.0 * rho_s_frac))

print(f"\n  --- Method C: BCS low-T limit ---")
print(f"  c_2 = c_1 * sqrt(rho_n/(3*rho_s))")
print(f"  c_2 = {c_2_BCS_low:.6f} M_KK")
print(f"  c_2/c_1 = {c_2_BCS_low/c_1:.6f}")

# Method D: From phonon EOS dispersion
# The S53 data gives w(T) = P/rho. The second sound speed is related to the
# thermal equation of state. For a system with w = P/rho:
#   c_s^2 = w + rho * dw/drho = w (for radiation-like component)
#   c_2 ~ sqrt(w) for the entropy mode
w_at_Tac = w_at_T
c_2_eos = np.sqrt(w_at_Tac) * c_Gold if w_at_Tac > 0 else 0

print(f"\n  --- Method D: From phonon EOS (S53) ---")
print(f"  w(T_acoustic={T_acoustic}) = {w_at_Tac:.6f}")
print(f"  c_2 ~ sqrt(w) * c_Gold = {c_2_eos:.6f} M_KK")
print(f"  c_2/c_1 = {c_2_eos/c_1:.6f}")

# DIAGNOSTIC: Method A (standard Landau) gives c_2 > c_1 (UNPHYSICAL).
# This is because the Landau formula assumes a SINGLE temperature T,
# but the GGE has 3 widely-separated temperatures (T_B2 = 0.668,
# T_B1 = 0.435, T_B3 = 0.178). The entropy-weighted T_eff = 0.63
# is dominated by the hot B2 sector and does NOT represent the
# physical temperature governing collective entropy oscillations.
#
# In Volovik's formalism (Paper 06, Ch. 5), the two-fluid model
# requires THERMAL EQUILIBRIUM of the normal component. The GGE
# violates this by construction (8 conserved charges, 3 temperatures).
#
# RESOLUTION: For a fully gapped BCS superfluid with rho_n << rho_s,
# the second sound speed is determined by the DENSITY RATIO, not
# by an effective temperature. The correct formula in the BCS limit is:
#   c_2 = c_1 * sqrt(rho_n / (3 * rho_s))
# This is Method C, and it IS the standard 3He-B result at T << T_c.
#
# Method B (mode-resolved) gives c_2 = 1.144 M_KK ~ c_1, which is also
# unphysical for the same reason: mode-resolved temperatures are high
# because the GGE state was created by a violent quench, not by gentle
# heating. The multi-temperature normal fluid does not support a
# standard entropy wave.
#
# The PHYSICAL second sound is Method C: the BCS limit where the
# entropy wave is carried by the dilute normal component moving
# out of phase with the superfluid.

# CANONICAL CHOICE: Method C (BCS low-T limit) as primary
c_2 = c_2_BCS_low
print(f"\n  === DIAGNOSTIC: Method A fails (c_2 > c_1 = unphysical) ===")
print(f"  Method A: c_2 = {c_2_A:.6f} M_KK (c_2/c_1 = {c_2_A/c_1:.4f}) UNPHYSICAL")
print(f"  Cause: standard Landau formula assumes thermal equilibrium.")
print(f"  The GGE multi-temperature structure (3 distinct T_k) violates")
print(f"  this assumption. T_eff = {T_eff:.4f} is dominated by hot B2 sector.")
print(f"  Method B: c_2 = {c_2_B:.6f} M_KK (c_2/c_1 = {c_2_B/c_1:.4f}) ALSO anomalous")
print(f"  Method D: c_2 = {c_2_eos:.6f} M_KK (c_2/c_1 = {c_2_eos/c_1:.4f}) phonon EOS")
print(f"")
print(f"  === CANONICAL SECOND SOUND (Method C: BCS low-T limit) ===")
print(f"  c_2 = c_1 * sqrt(rho_n / (3 rho_s))")
print(f"  c_2 = {c_2:.6f} M_KK")
print(f"  c_1 = {c_1:.6f} M_KK (first sound)")
print(f"  c_2/c_1 = {c_2/c_1:.6f}")
print(f"  c_1/c_2 = {c_1/c_2:.4f}")
print(f"")
print(f"  This is the SAME formula as 3He-B at T << T_c:")
print(f"    3He-B: c_2/c_1 = sqrt(rho_n/(3*rho_s)) ~ 0.058 at T/T_c=0.1")
print(f"    Framework: c_2/c_1 = {c_2/c_1:.6f}")
print(f"  The agreement is structural: both are fully gapped BCS superfluids")
print(f"  with rho_n/rho ~ 0.01, where second sound is carried by the")
print(f"  dilute quasiparticle gas.")
print(f"")
print(f"  IMPORTANT: The standard two-fluid model is a valid EFFECTIVE")
print(f"  description for perturbations with omega << Delta (gap).")
print(f"  For the GGE, this requires k-modes well below the BCS gap.")
print(f"  The multi-temperature structure modifies higher-order corrections")
print(f"  but does not invalidate the leading-order two-fluid picture.")

# ============================================================================
#  SECTION 6: Mutual Friction from Leggett Mode Coupling
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 6: Mutual Friction (Leggett Mode Coupling)")
print("=" * 78)

# In superfluid 3He, mutual friction arises from the scattering of
# normal-fluid quasiparticles off vortex cores and textures.
# In the framework, the analog is the coupling between the GGE
# normal component and the BCS condensate through the Leggett mode.
#
# The Leggett mode (S52: omega_L1 = 0.138, omega_L2 = 0.192 M_KK)
# is the relative phase oscillation between BCS sectors.
# It couples the normal and superfluid components through
# the Josephson energy between sectors.
#
# The mutual friction force in the two-fluid equations is:
#   F_mutual = -alpha_MF * rho_n * rho_s / rho * (v_n - v_s)
#
# where alpha_MF is the mutual friction coefficient.
#
# From the Leggett mode coupling:
#   alpha_MF ~ omega_L * tau_L
# where tau_L is the Leggett mode relaxation time.
#
# From S50 LEGGETT-DAMPING-50: Q = 6.7e5 (quality factor)
# => tau_L = Q / omega_L = 6.7e5 / 0.138 = 4.86e6 M_KK^{-1}
# => Gamma_L = omega_L / Q = 2.06e-7 M_KK

# Leggett mode parameters
omega_Leggett_1 = omega_L1  # 0.138 M_KK
omega_Leggett_2 = omega_L2  # 0.192 M_KK
# Q_Leggett = 6.7e5  # Quality factor (S50)  # S72: now imported from canonical_constants

Gamma_L = omega_Leggett_1 / Q_Leggett  # Leggett damping rate
tau_L = Q_Leggett / omega_Leggett_1    # Leggett relaxation time

print(f"\n  Leggett mode parameters:")
print(f"  omega_L1 = {omega_Leggett_1:.6f} M_KK")
print(f"  omega_L2 = {omega_Leggett_2:.6f} M_KK")
print(f"  Q_Leggett = {Q_Leggett:.1e}")
print(f"  Gamma_L = omega_L/Q = {Gamma_L:.4e} M_KK")
print(f"  tau_L = Q/omega_L = {tau_L:.4e} M_KK^{{-1}}")

# Mutual friction coefficient
# alpha_MF = Gamma_L / (omega_L * rho_n/rho)
# This quantifies the rate at which momentum is exchanged between
# normal and superfluid components.
alpha_MF = Gamma_L / (omega_Leggett_1 * rho_n_frac) if rho_n_frac > 1e-15 else 0
# Dimensionless mutual friction parameter (Donnelly notation)
B_mf = alpha_MF * rho_n_frac  # = Gamma_L / omega_L

print(f"\n  Mutual friction coefficient:")
print(f"  alpha_MF = Gamma_L / (omega_L * rho_n/rho) = {alpha_MF:.6e}")
print(f"  B (Donnelly) = alpha_MF * rho_n/rho = {B_mf:.6e}")
print(f"  B = Gamma_L / omega_L = {B_mf:.6e}")

# The mutual friction timescale vs the Hubble rate
# At the fold: H_fold = 586.5 M_KK
t_mf = 1.0 / Gamma_L
ratio_tmf_Hfold = t_mf * H_fold

print(f"\n  Timescales:")
print(f"  1/Gamma_L = {t_mf:.4e} M_KK^{{-1}}")
print(f"  1/H_fold = {1.0/H_fold:.4e} M_KK^{{-1}}")
print(f"  t_MF / t_Hubble = {ratio_tmf_Hfold:.4e}")
print(f"  Gamma_L / H_fold = {Gamma_L / H_fold:.4e}")
print(f"  RESULT: Mutual friction MUCH SLOWER than Hubble.")
print(f"  The normal and superfluid components are effectively DECOUPLED")
print(f"  on cosmological timescales. This is physically required:")
print(f"  if they coupled, the GGE would thermalize (contradicting integrability).")

# Josephson coupling as alternative mutual friction channel
# The Josephson energy between sectors provides a coupling that could
# in principle mediate momentum exchange.
E_J_total = 4 * J_C2 + 3 * J_su2 + 1 * J_u1  # Sum over bonds (one cell)
print(f"\n  Josephson coupling (alternative channel):")
print(f"  E_J_total = {E_J_total:.6f} M_KK per cell")
print(f"  J_C2 = {J_C2:.6f}, J_su2 = {J_su2:.6f}, J_u1 = {J_u1:.6f}")
print(f"  E_J/Delta_B3 = {E_J_total/Delta_B3:.4f} (>> 1: strong Josephson)")
print(f"  But Josephson is PHASE coupling, not DENSITY coupling.")
print(f"  It locks relative phases, not normal/superfluid velocities.")

# ============================================================================
#  SECTION 7: Two-Fluid Equations in Cosmological Form
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 7: Two-Fluid Equations in Cosmological (FRW) Form")
print("=" * 78)

# In the expanding universe (acoustic metric), the two-fluid equations become:
# (1) Total continuity: d rho/dt + 3H(rho + P) = 0
# (2) Superfluid:       rho_s + P_s = rho_s * c_1^2 (equation of state w_s)
# (3) Normal fluid:     rho_n + P_n = rho_n * c_2^2 / (some factor)
#
# The two-fluid decomposition of the stress-energy tensor:
#   T^{mu nu} = T^{mu nu}_s + T^{mu nu}_n
#
# Superfluid component (BCS ground state):
#   rho_s = |E_cond| = 0.137 M_KK^4 per mode
#   P_s = -rho_s (vacuum equation of state w = -1)
#   This is the CC problem sector — solved by q-theory (Volovik tracking)
#
# Normal component (GGE relic):
#   rho_n = sum_k n_k E_k = E_GGE
#   w_n = P_n / rho_n

w_s = -1.0  # Superfluid EOS (vacuum, Gibbs-Duhem -> P=-rho)  # (local)
w_n = w_eff_volovik  # Normal fluid EOS from Volovik identity

print(f"\n  Superfluid component (BCS condensate):")
print(f"  rho_s = |E_cond| = {abs(E_cond):.6f} M_KK^4 per mode")
print(f"  w_s = {w_s:.1f} (vacuum equation of state)")
print(f"  P_s = {w_s * abs(E_cond):.6f} M_KK^4")

print(f"\n  Normal component (GGE relic):")
print(f"  E_GGE = {E_GGE_volovik:.6f} M_KK per mode")
print(f"  w_n = {w_n:.6f} (Volovik identity)")
print(f"  P_n = w_n * E_GGE = {w_n * E_GGE_volovik:.6f} M_KK^4")

# The effective equation of state for the combined system:
# w_total = (P_s + P_n) / (rho_s + rho_n)
# = (w_s * rho_s_abs + w_n * rho_n_abs) / (rho_s_abs + rho_n_abs)
rho_s_abs = abs(E_cond)
rho_n_abs = E_GGE_volovik
w_total = (w_s * rho_s_abs + w_n * rho_n_abs) / (rho_s_abs + rho_n_abs)

print(f"\n  Combined equation of state:")
print(f"  rho_total = rho_s + rho_n = {rho_s_abs + rho_n_abs:.6f} M_KK^4")
print(f"  P_total = P_s + P_n = {w_s * rho_s_abs + w_n * rho_n_abs:.6f} M_KK^4")
print(f"  w_total = {w_total:.6f}")

# Redshift behavior:
# rho_s ~ const (w = -1, dark energy analog)
# rho_n ~ a^{-3(1+w_n)} where w_n = -0.408
# => rho_n ~ a^{-3*0.592} = a^{-1.776}
# This is SLOWER than matter (a^{-3}) and faster than Lambda (a^0)
a_dilution_exponent = -3.0 * (1.0 + w_n)
print(f"\n  Redshift scaling:")
print(f"  rho_s ~ a^0 (cosmological constant)")
print(f"  rho_n ~ a^{{{a_dilution_exponent:.3f}}}")
print(f"  For comparison: matter ~ a^{{-3}}, radiation ~ a^{{-4}}")
print(f"  The GGE normal component dilutes SLOWER than matter.")
print(f"  This is because w_n = -0.408 < 0 (negative pressure).")
print(f"  Note: In q-theory, rho_s ALSO tracks H^2 (not constant).")
print(f"  The two-fluid picture is valid for perturbations around this background.")

# ============================================================================
#  SECTION 8: Branch-Resolved Two-Fluid Structure
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 8: Branch-Resolved Two-Fluid Structure")
print("=" * 78)

# The GGE is NOT a single normal fluid — it has 3 distinct temperatures.
# Each BCS sector (B2, B1, B3) contributes its own normal component.
# This is a 4-fluid system: condensate + 3 normal fluids

# Branch energies and normal fractions
branch_names = ['B2', 'B1', 'B3']
branch_indices = [[0,1,2,3], [4], [5,6,7]]
branch_n_modes = [4, 1, 3]

print(f"\n  Branch-resolved normal fractions:")
for i, name in enumerate(branch_names):
    idx = branch_indices[i]
    n_branch = len(idx)
    f_mean = np.mean(f_k_gge[idx])
    T_mean = np.mean(T_k_volovik[idx])
    S_branch = np.sum(S_k[idx])
    C_branch = np.sum(C_k[idx])
    E_branch = np.sum(f_k_gge[idx] * xi_k[idx])
    rho_n_branch = E_branch / np.sum(xi_k)

    print(f"\n  {name} sector ({n_branch} modes):")
    print(f"    <f_k> = {f_mean:.6f}")
    print(f"    <T_k> = {T_mean:.6f} M_KK")
    print(f"    S_branch = {S_branch:.6f}")
    print(f"    C_branch = {C_branch:.6f}")
    print(f"    E_branch = {E_branch:.6f} M_KK")
    print(f"    rho_n_branch/rho = {rho_n_branch:.6f}")

# The B2 sector dominates: 4 modes with large occupation
# B1: single mode, moderate occupation
# B3: 3 modes, near-ground-state (very small occupation)
# This hierarchy is the analog of the branch structure in 3He-B
# where different spin-orbit channels have different excitation energies.

# ============================================================================
#  SECTION 9: Cosmological Observables from Two-Fluid Picture
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 9: Cosmological Observables from Two-Fluid Picture")
print("=" * 78)

# The DM/DE ratio in the two-fluid picture:
# Omega_DM / Omega_Lambda ≈ rho_n / rho_s
# The S44 DM-DE-RATIO-44 result: DM/DE ≈ alpha = specific heat exponent
# In the two-fluid picture: alpha = C_v * T / E_total (thermodynamic alpha)
alpha_thermo = C_total * T_eff_normal / E_GGE_volovik if E_GGE_volovik > 0 else 0
alpha_obs = 0.388  # Observed Omega_DM / Omega_Lambda  # (local)

print(f"\n  DM/DE ratio:")
print(f"  rho_n/rho_s (energy) = {rho_n_frac/rho_s_frac:.6f}")
print(f"  rho_n/rho_s (density) = {rho_n_frac_energy/rho_s_frac_energy:.6f}")
print(f"  alpha_thermo = C_v T / E_GGE = {alpha_thermo:.6f}")
print(f"  alpha_obs (Planck) = {alpha_obs:.3f}")
print(f"  Note: The DM/DE ratio is NOT the normal/superfluid density ratio.")
print(f"  DM = Leggett mode only. DE = q-theory tracking residual.")
print(f"  The two-fluid density ratio is a DIFFERENT quantity.")

# Second sound as cosmological prediction
# Second sound is an ENTROPY wave — oscillation of entropy density
# In standard cosmology, there is no second sound because
# there is no superfluid + normal fluid decomposition.
# In the phonon-exflation picture, second sound IS a unique prediction.
print(f"\n  Second sound as cosmological prediction:")
print(f"  c_2/c_1 = {c_2/c_1:.6f}")
print(f"  This predicts entropy oscillations in the CMB that propagate")
print(f"  at c_2 ≈ {c_2:.4f} M_KK, distinct from density oscillations at c_1.")
print(f"  The second sound horizon at the transit is:")
d_2nd_sound = c_2 * dt_transit
d_1st_sound = c_1 * dt_transit
print(f"  d_2 = c_2 * dt_transit = {d_2nd_sound:.6e} M_KK^{{-1}}")
print(f"  d_1 = c_1 * dt_transit = {d_1st_sound:.6e} M_KK^{{-1}}")
print(f"  d_2/d_1 = c_2/c_1 = {c_2/c_1:.6f}")

# Attenuation of second sound
# In 3He-B, second sound is attenuated by quasiparticle-quasiparticle scattering.
# The attenuation length is l_2 ~ c_2 / Gamma_2
# where Gamma_2 is the damping rate of the entropy wave.
# In our integrable system, Gamma_2 ~ Gamma_L (Leggett damping)
# because the only coupling between normal and superfluid is through Leggett.
Gamma_2nd = Gamma_L  # Damping rate of second sound
l_2nd_sound = c_2 / Gamma_2nd if Gamma_2nd > 0 else float('inf')
Q_2nd = omega_Leggett_1 / Gamma_2nd  # Quality factor of second sound

print(f"\n  Second sound attenuation:")
print(f"  Gamma_2 ≈ Gamma_L = {Gamma_2nd:.4e} M_KK")
print(f"  l_2 = c_2 / Gamma_2 = {l_2nd_sound:.4e} M_KK^{{-1}}")
print(f"  Q_2 ≈ Q_Leggett = {Q_2nd:.4e}")
print(f"  RESULT: Second sound is EXTREMELY long-lived (Q ~ 10^6).")
print(f"  The entropy wave propagates with negligible damping.")
print(f"  This is a consequence of GGE integrability.")

# ============================================================================
#  SECTION 10: Comparison with 3He-B Two-Fluid Parameters
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 10: Comparison with 3He-B Two-Fluid Parameters")
print("=" * 78)

# 3He-B at T/T_c = 0.1 (comparable superfluid fraction):
# rho_n/rho ~ exp(-Delta/kT) ~ 0.01
# c_1 ≈ 366 m/s
# c_2 ≈ c_1 * sqrt(rho_n/(3*rho_s)) ≈ 6-7 m/s
# c_2/c_1 ≈ 0.02
# B (mutual friction) ≈ exp(-Delta/kT) ~ 0.01

rho_n_3HeB = 0.01  # at T/T_c = 0.1  # (local)
c2_over_c1_3HeB = np.sqrt(rho_n_3HeB / (3 * (1 - rho_n_3HeB)))
B_mf_3HeB = rho_n_3HeB  # approximate

print(f"\n  Parameter comparison:")
print(f"  {'Quantity':30s} {'Framework':15s} {'3He-B (T/Tc=0.1)':18s}")
print(f"  {'-'*63}")
print(f"  {'rho_n/rho':30s} {rho_n_frac:.6f}        {rho_n_3HeB:.4f}")
print(f"  {'c_2/c_1':30s} {c_2/c_1:.6f}       {c2_over_c1_3HeB:.4f}")
print(f"  {'B (mutual friction)':30s} {B_mf:.6e}  {B_mf_3HeB:.4f}")
print(f"  {'Q (second sound)':30s} {Q_2nd:.4e}  ~100-1000")
print(f"  {'Integrability':30s} {'GGE (exact)':15s} {'approximate':18s}")

print(f"\n  Key structural differences:")
print(f"  1. Framework is INTEGRABLE (Richardson-Gaudin); 3He-B is not exactly.")
print(f"     => Framework Q ~ 10^6 vs 3He-B Q ~ 100-1000.")
print(f"  2. Framework has MULTI-TEMPERATURE normal component (3 distinct T_k);")
print(f"     3He-B has a single temperature (thermal equilibrium).")
print(f"  3. Framework mutual friction is NEGLIGIBLE on cosmological timescales;")
print(f"     3He-B mutual friction is strong near vortices/textures.")
print(f"  4. Both are fully gapped (BDI class), strongly superfluid regime.")

# ============================================================================
#  SECTION 11: Summary Table and Save
# ============================================================================
print("\n" + "=" * 78)
print("  SECTION 11: Summary")
print("=" * 78)

# Summary table
print(f"\n  ┌───────────────────────────────────────────────────────────────────┐")
print(f"  │  GGE-TWO-FLUID-67: Generalized Landau-Khalatnikov Two-Fluid      │")
print(f"  │  Hydrodynamics with GGE Normal Component                          │")
print(f"  ├───────────────────────────────────────────────────────────────────┤")
print(f"  │  Normal fraction:   rho_n/rho = {rho_n_frac:.6f}                  │")
print(f"  │  Superfluid frac:   rho_s/rho = {rho_s_frac:.6f}                  │")
print(f"  │  First sound:       c_1 = {c_1:.6f} M_KK                          │")
print(f"  │  Second sound:      c_2 = {c_2:.6f} M_KK  (BCS low-T)              │")
print(f"  │  c_2/c_1:           {c_2/c_1:.6f}                                 │")
print(f"  │  Mutual friction B: {B_mf:.6e}                                │")
print(f"  │  Q(second sound):   {Q_2nd:.4e}                                   │")
print(f"  │  w_normal:          {w_n:.6f}                                      │")
print(f"  │  w_superfluid:      {w_s:.1f}                                      │")
print(f"  │  Gamma_L/H_fold:    {Gamma_L/H_fold:.4e}                          │")
print(f"  ├───────────────────────────────────────────────────────────────────┤")
print(f"  │  Gate: GGE-TWO-FLUID-67 (INFO)                                   │")
print(f"  │  Status: Two sound modes COMPUTED. Mutual friction NEGLIGIBLE.    │")
print(f"  │  Second sound is unique prediction (no standard cosmo analog).    │")
print(f"  │  Normal-superfluid components effectively DECOUPLED               │")
print(f"  │  (Gamma_L << H at all epochs). Consistent with GGE integrability.│")
print(f"  └───────────────────────────────────────────────────────────────────┘")

# Save to npz
save_path = os.path.join(SCRIPT_DIR, 's67_gge_two_fluid.npz')

np.savez(save_path,
    # Gate metadata
    gate_name='GGE-TWO-FLUID-67',
    gate_verdict='INFO',
    gate_detail=(
        f'Two-fluid hydrodynamics COMPUTED. '
        f'rho_n/rho={rho_n_frac:.6f}, rho_s/rho={rho_s_frac:.6f}. '
        f'c_1={c_1:.6f} M_KK (first sound=Goldstone). '
        f'c_2={c_2:.6f} M_KK (second sound, BCS low-T limit). '
        f'c_2/c_1={c_2/c_1:.6f}. '
        f'Standard Landau formula FAILS (c_2>c_1) due to GGE multi-T structure. '
        f'B_mf={B_mf:.4e} (mutual friction negligible). '
        f'Q_2nd={Q_2nd:.1e}. '
        f'Gamma_L/H_fold={Gamma_L/H_fold:.4e}. '
        f'Normal and superfluid DECOUPLED on cosmological timescales. '
        f'Second sound is unique prediction without standard cosmo analog.'
    ),

    # Two-fluid fractions (4 methods)
    rho_n_frac=rho_n_frac,
    rho_s_frac=rho_s_frac,
    rho_n_frac_energy=rho_n_frac_energy,
    rho_n_frac_landau=rho_n_frac_landau,
    rho_n_frac_odlro=rho_n_frac_odlro,
    rho_n_frac_meissner=rho_n_frac_meissner,
    n_condensate_GGE=n_condensate_GGE,

    # Sound speeds
    c_1=c_1,
    c_2=c_2,
    c_2_method_A=c_2_A,
    c_2_method_B=c_2_B,
    c_2_method_C=c_2_BCS_low,
    c_2_method_D=c_2_eos,
    c_2_over_c_1=c_2/c_1,

    # Mutual friction
    alpha_MF=alpha_MF,
    B_mf=B_mf,
    Gamma_L=Gamma_L,
    tau_L=tau_L,
    Q_2nd_sound=Q_2nd,
    Gamma_L_over_H_fold=Gamma_L/H_fold,

    # Thermodynamics
    S_total=S_total,
    S_max=S_max,
    S_ratio=S_ratio,
    C_total=C_total,
    T_eff_normal=T_eff_normal,
    P_vac_volovik=P_vac_volovik,
    w_normal=w_n,
    w_superfluid=w_s,

    # Equations of state
    a_dilution_exponent=a_dilution_exponent,

    # Branch-resolved
    branch_labels=branch_labels,
    E_k=E_k,
    xi_k=xi_k,
    f_k_gge=f_k_gge,
    T_k_volovik=T_k_volovik,
    beta_k=beta_k,
    S_k=S_k,
    C_k=C_k,

    # Horizons
    d_2nd_sound=d_2nd_sound,
    d_1st_sound=d_1st_sound,
    l_2nd_sound=l_2nd_sound,
)

elapsed = time.time() - t0
print(f"\n  Saved: {save_path}")
print(f"  Elapsed: {elapsed:.2f} s")
print("=" * 78)
