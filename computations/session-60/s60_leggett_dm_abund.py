#!/usr/bin/env python3
"""
S60 LEGGETT-DM-ABUND-60: Leggett Mode Cosmological Relic Abundance
====================================================================

Computes whether the Leggett mode (relative phase oscillation between B2 sectors)
can serve as cold dark matter. Propagates Bogoliubov-produced Leggett number density
through standard cosmological expansion to compare with Omega_DM h^2 = 0.120.

Inputs:
  - s59_epsilon_canonical.npz: Leggett mode parameters (epsilon, omega_L1)
  - s59_bogoliubov_coeff.npz: Bogoliubov coefficients beta_k for particle production
  - s59_fdm_depletion.npz: condensate depletion fraction, energy budget
  - canonical_constants.py: M_KK, cosmological constants

Gate: LEGGETT-DM-ABUND-60
  PASS: Omega_L h^2 within 10x of 0.120 AND tau_L > 10 * t_U AND lambda_fs < 0.1 Mpc
  FAIL: Omega_L h^2 off by > 10^3 OR tau_L < t_U OR lambda_fs > 10 Mpc
  INFO: intermediate

Volovik framework: The Leggett mode is the direct analog of the relative phase
oscillation between the A and B phases of superfluid 3He when they coexist.
In the 3He-B phase, Leggett's collective mode has been experimentally observed
via NMR (omega_L ~ 0.6*Delta in B-phase). Here the B2 sectors play the role
of the A and B phases, with the U(1)_7 breaking parameter epsilon setting
the mass. The cosmological abundance follows from Parker-type particle
creation during the transit (not thermal freeze-out), directly paralleling
cosmological particle creation in analog gravity (Volovik, Universe in a
Helium Droplet, Ch. 32).

Author: Volovik Superfluid Universe Theorist Agent
Session: S60
"""

import sys
import os
import numpy as np

# Ensure canonical_constants is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    M_KK, M_KK_gravity, M_Pl_reduced, M_Pl_unreduced,
    H_0_GeV, H_0_inv_s, T_CMB, T_CMB_GeV,
    rho_crit_GeV4, rho_Lambda_obs, Omega_DM,
    t_universe_s, k_B, k_B_SI, c_light, hbar_GeV_s,
    GeV_to_inv_s, GeV_inv_to_Mpc, Mpc_to_m,
    omega_L1 as omega_L1_canon, omega_L2,
    N_cells, E_cond, n_Bog, PI,
    dt_transit, omega_tau,
    Omega_m, Omega_r, Omega_Lambda,
    eV_SI, hbar_c_GeV_m,
)

print("=" * 70)
print("S60 LEGGETT-DM-ABUND-60: Leggett Mode Relic Abundance")
print("=" * 70)

# ============================================================================
# 1. Load input data
# ============================================================================

d_eps = np.load(os.path.join(os.path.dirname(__file__), 's59_epsilon_canonical.npz'),
                allow_pickle=True)
d_bog = np.load(os.path.join(os.path.dirname(__file__), 's59_bogoliubov_coeff.npz'),
                allow_pickle=True)
d_fdm = np.load(os.path.join(os.path.dirname(__file__), 's59_fdm_depletion.npz'),
                allow_pickle=True)

# Leggett mode parameters
epsilon_canon = float(d_eps['eps_canonical'])
omega_L1_eps = float(d_eps['omega_L1_canonical'])  # from S59 epsilon computation
E_L_exc = float(d_eps['E_L_exc_canon'])  # Leggett excitation energy from transit

# Bogoliubov coefficients
beta_sq_full = d_bog['beta_sq_full']  # 8 modes, full transit
beta_sq_fold = d_bog['beta_sq_fold']  # at fold only
sum_beta_sq = float(d_bog['sum_beta_sq_full'])
T_eff = float(d_bog['T_eff'])  # effective temperature

# FDM depletion
E_Leggett_0 = float(d_fdm['E_Leggett_0'])  # Leggett energy at production
E_total_0 = float(d_fdm['E_total_0'])  # total substrate energy
omega_L_gap = float(d_fdm['omega_L_gap'])  # Leggett gap frequency
f_DM_z0 = float(d_fdm['f_DM_z0'])  # dark matter fraction at z=0

print("\n--- Input Parameters ---")
print(f"epsilon_canonical     = {epsilon_canon:.6f}")
print(f"omega_L1 (S59)        = {omega_L1_eps:.5f} M_KK")
print(f"omega_L1 (canonical)  = {omega_L1_canon:.3f} M_KK")
print(f"omega_L_gap (FDM)     = {omega_L_gap:.3f} M_KK")
print(f"E_Leggett_0           = {E_Leggett_0:.3f} M_KK")
print(f"E_total_0             = {E_total_0:.3f} M_KK")
print(f"sum |beta_k|^2 (full) = {sum_beta_sq:.4f}")
print(f"T_eff                 = {T_eff:.4f} M_KK")
print(f"f_DM(z=0)             = {f_DM_z0:.3f}")

# ============================================================================
# 2. Leggett mode mass in physical units
# ============================================================================

# Use canonical omega_L1 = 0.138 M_KK as the Leggett mass
# This is the GL-Josephson result (S52), confirmed by damping analysis (S50)
# The S59 epsilon computation gives omega_L1 = 0.049 from bare partition,
# but the ED-constrained value omega_L1_ED = 0.070 (S50) and GL omega_L1 = 0.138 (S52)
# are the physical values. Use the gap frequency from FDM-DEPLETION which is
# the canonical 0.138.

m_L_MKK = omega_L_gap  # = 0.138 M_KK (the Leggett mass gap)
m_L_GeV = m_L_MKK * M_KK  # in GeV

print(f"\n--- Leggett Mode Mass ---")
print(f"m_L = {m_L_MKK:.4f} M_KK = {m_L_GeV:.4e} GeV")
print(f"m_L / M_Pl = {m_L_GeV / M_Pl_unreduced:.4e}")
print(f"m_L / M_KK = {m_L_MKK:.4f}")

# Cross-check: also compute with S50 Leggett damping value
m_L_S50 = 0.06955  # from LEGGETT-DAMPING-50  # (local)
m_L_S50_GeV = m_L_S50 * M_KK
print(f"\nCross-check (S50 damping): m_L = {m_L_S50:.5f} M_KK = {m_L_S50_GeV:.4e} GeV")
print(f"Ratio canonical/S50 = {m_L_MKK / m_L_S50:.2f}")

# ============================================================================
# 3. Number density from Bogoliubov production
# ============================================================================

# The system is 0-dimensional (single cell). The Bogoliubov coefficients give
# the number of particles produced per mode during transit. This is NOT a
# 3D momentum integral -- it is a discrete sum over the 8 BCS modes.
#
# In the superfluid analog: this parallels cosmological particle creation
# in a FRW universe, where the number of phonons created per mode is |beta_k|^2
# (Volovik, Universe in a Helium Droplet, eq. 32.7). The key difference:
# our system is 0D with discrete modes, not a continuous k-space.
#
# The Leggett mode is a collective mode distinct from the Bogoliubov quasiparticles.
# Its production comes from the U(1)_7 symmetry breaking during transit.
# FDM-DEPLETION-59 established that the Leggett mode carries energy
# E_Leggett_0 = 3.01 M_KK out of E_total_0 = 14.41 M_KK.
# The number of Leggett quanta is n_L = E_Leggett / omega_L.

# Method 1: From FDM energy budget
n_L_from_energy = E_Leggett_0 / omega_L_gap  # number of Leggett quanta per cell
print(f"\n--- Leggett Number Density ---")
print(f"n_L per cell (energy budget) = {n_L_from_energy:.2f}")

# Method 2: From Bogoliubov excitation of Leggett channel
# The Leggett mode is excited by the parametric variation of epsilon during transit.
# The Bogoliubov coefficient for the Leggett channel specifically can be estimated
# from the adiabaticity parameter: |beta_L|^2 ~ (omega_dot / omega^2)^2 for adiabatic,
# or ~ O(1) for sudden quench. Since omega_L * dt_transit << 1 (S50: N_osc = 1.3e-5),
# the transit is completely sudden for the Leggett mode, giving |beta_L|^2 ~ 1.
# This is consistent with sum_beta_sq = 8.12 for 8 modes (each ~1).
beta_L_sq_sudden = 1.0  # sudden quench limit  # (local)
print(f"|beta_L|^2 (sudden limit) = {beta_L_sq_sudden:.1f}")
print(f"N_osc(Leggett during transit) = {omega_L_gap * dt_transit:.2e}")

# The physical number density requires embedding in 4D spacetime.
# Each Voronoi cell has volume ~ (1/M_KK)^3 in 3D comoving space at production.
# The cell is the elementary unit -- N_cells = 32 cells in the fabric.
# Total Leggett quanta = n_L_per_cell * N_cells

n_L_total = n_L_from_energy * N_cells  # total Leggett quanta in the fabric
print(f"n_L total (fabric) = {n_L_total:.1f}")

# The comoving volume at production is set by the Hubble radius at T ~ M_KK.
# But the framework's 0D character means the "production volume" is the
# cell volume V_cell ~ M_KK^{-3}. The number density at production:
# n_L(prod) = n_L_per_cell / V_cell = n_L_per_cell * M_KK^3

n_L_prod_GeV3 = n_L_from_energy * M_KK**3  # GeV^3 (per cell)
n_L_prod_fabric_GeV3 = n_L_total * M_KK**3 / N_cells  # same, per cell
print(f"n_L(prod) per cell = {n_L_prod_GeV3:.4e} GeV^3")

# ============================================================================
# 4. Propagate to today via cosmological expansion
# ============================================================================

# The Leggett mode is massive (gapped), so it redshifts as matter: n ~ a^{-3}.
# Production temperature T_prod ~ M_KK (transit happens at the KK scale).
# Today: T_0 = T_CMB = 2.725 K.
# Scale factor ratio: a_prod/a_0 = T_0/T_prod (for radiation-dominated early universe)

T_prod_GeV = M_KK  # production at KK scale
a_prod_over_a0 = T_CMB_GeV / T_prod_GeV

print(f"\n--- Cosmological Dilution ---")
print(f"T_prod = {T_prod_GeV:.4e} GeV (= M_KK)")
print(f"T_CMB  = {T_CMB_GeV:.4e} GeV")
print(f"a_prod/a_0 = {a_prod_over_a0:.4e}")
print(f"Dilution factor (a_prod/a_0)^3 = {a_prod_over_a0**3:.4e}")

# Number density today
n_L_today_GeV3 = n_L_prod_GeV3 * a_prod_over_a0**3
print(f"n_L(today) = {n_L_today_GeV3:.4e} GeV^3")

# ============================================================================
# 5. Relic abundance
# ============================================================================

# Energy density today: rho_L = m_L * n_L(today)
rho_L_GeV4 = m_L_GeV * n_L_today_GeV3
print(f"\n--- Relic Abundance ---")
print(f"rho_L(today) = {rho_L_GeV4:.4e} GeV^4")
print(f"rho_crit     = {rho_crit_GeV4:.4e} GeV^4")

Omega_L_h2 = rho_L_GeV4 / rho_crit_GeV4 * 0.674**2  # h = 0.674 (Planck 2018)
# More precisely: Omega_L = rho_L / rho_crit, and rho_crit already includes h^2
# rho_crit = 3*H_0^2/(8*pi*G) with H_0 in natural units
# So Omega_L = rho_L / rho_crit directly
Omega_L = rho_L_GeV4 / rho_crit_GeV4
h_Planck = 0.674  # (local)
Omega_L_h2_v2 = Omega_L * h_Planck**2

print(f"Omega_L = {Omega_L:.4e}")
print(f"Omega_L h^2 = {Omega_L_h2_v2:.4e}")
print(f"Omega_DM h^2 (observed) = {Omega_DM * h_Planck**2:.4f}")
print(f"Ratio Omega_L / Omega_DM = {Omega_L / Omega_DM:.4e}")

# Cross-check: ratio to observed DM abundance
Omega_DM_h2_obs = 0.120  # Planck 2018  # (local)
ratio_to_obs = Omega_L_h2_v2 / Omega_DM_h2_obs
print(f"Omega_L h^2 / 0.120 = {ratio_to_obs:.4e}")
print(f"|log10(ratio)| = {abs(np.log10(ratio_to_obs)):.1f} orders")

# ============================================================================
# 5b. Alternative: Energy-fraction method
# ============================================================================

# FDM-DEPLETION-59 established that at z=0, essentially all substrate energy
# is in the Leggett channel (f_DM = 1.0). The total substrate energy at
# production is E_total = 14.41 M_KK per cell. The Leggett fraction is
# E_L/E_total = 3.01/14.41 = 0.209.
# After depletion of BA and BCS channels, the fraction becomes ~1.0.
# But the TOTAL energy density must be traced through expansion.

f_L_initial = E_Leggett_0 / E_total_0
print(f"\n--- Energy Fraction Method ---")
print(f"f_L(initial) = {f_L_initial:.4f}")
print(f"f_L(z=0) = {f_DM_z0:.3f} (from FDM-DEPLETION-59)")

# Total substrate energy density at production (per cell volume M_KK^{-3})
rho_total_prod = E_total_0 * M_KK / M_KK**(-3)  # Wait -- units.
# E_total_0 is in M_KK units, i.e. E_total = 14.41 * M_KK (in GeV)
# Per cell volume V_cell = (1/M_KK)^3 (in GeV^{-3})
# rho = E / V = E_total_0 * M_KK / (M_KK^{-3}) = E_total_0 * M_KK^4
rho_total_prod_GeV4 = E_total_0 * M_KK**4
rho_L_prod_GeV4 = E_Leggett_0 * M_KK**4

print(f"rho_total(prod) = {rho_total_prod_GeV4:.4e} GeV^4")
print(f"rho_L(prod) = {rho_L_prod_GeV4:.4e} GeV^4")

# Leggett mode is massive -> redshifts as a^{-3} in energy (matter-like)
# But energy density redshifts as rho ~ a^{-3} for matter
rho_L_today_v2 = rho_L_prod_GeV4 * (a_prod_over_a0)**3
Omega_L_v2 = rho_L_today_v2 / rho_crit_GeV4
Omega_L_h2_v2b = Omega_L_v2 * h_Planck**2

print(f"rho_L(today) [energy method] = {rho_L_today_v2:.4e} GeV^4")
print(f"Omega_L [energy method] = {Omega_L_v2:.4e}")
print(f"Omega_L h^2 [energy method] = {Omega_L_h2_v2b:.4e}")
print(f"Ratio to 0.120 = {Omega_L_h2_v2b / 0.120:.4e}")

# ============================================================================
# 6. Gravitational decay lifetime
# ============================================================================

# The Leggett mode is a neutral scalar. It can decay gravitationally via:
# (a) Leggett -> 2 gravitons (if m_L > 0): Gamma ~ m_L^3 / M_Pl^2
# (b) Leggett -> 2 photons via gravity loop: suppressed by alpha^2/M_Pl^2
# (c) Leggett -> 2 Goldstone bosons: kinematically forbidden (Beliaev, S50 PASS)
# (d) Leggett -> 2 BCS quasiparticles: kinematically forbidden (25.9x below threshold, S50)
#
# The dominant channel is (a): Gamma_grav = m_L^3 / (32 * pi * M_Pl^2)
# (Standard formula for scalar -> 2 graviton, N_channels = 1 helicity state)

# Standard gravitational decay: Gamma = m^3 / (32*pi*M_Pl^2) per channel
# For a real scalar decaying to graviton pairs:
N_grav_channels = 1  # graviton pair (2 helicities sum to 1 effective channel for scalar)

Gamma_grav_GeV = m_L_GeV**3 / (32 * PI * M_Pl_reduced**2)
tau_L_s = hbar_GeV_s / Gamma_grav_GeV  # lifetime in seconds
tau_L_over_tU = tau_L_s / t_universe_s

print(f"\n--- Gravitational Decay ---")
print(f"m_L = {m_L_GeV:.4e} GeV")
print(f"M_Pl (reduced) = {M_Pl_reduced:.4e} GeV")
print(f"Gamma_grav = {Gamma_grav_GeV:.4e} GeV")
print(f"tau_L = {tau_L_s:.4e} s")
print(f"t_universe = {t_universe_s:.4e} s")
print(f"tau_L / t_universe = {tau_L_over_tU:.4e}")

if tau_L_over_tU > 1:
    print(f"STABLE on cosmological timescales (tau_L = {tau_L_over_tU:.1e} x t_U)")
else:
    print(f"UNSTABLE: decays in {tau_L_s:.2e} s ({tau_L_s / (365.25*86400):.2e} yr)")

# Cross-check with M_Pl unreduced
Gamma_grav_unreduced = m_L_GeV**3 / (32 * PI * M_Pl_unreduced**2)
tau_L_unreduced_s = hbar_GeV_s / Gamma_grav_unreduced
print(f"\nCross-check (unreduced M_Pl):")
print(f"Gamma = {Gamma_grav_unreduced:.4e} GeV, tau = {tau_L_unreduced_s:.4e} s")
print(f"tau/t_U = {tau_L_unreduced_s / t_universe_s:.4e}")

# Also: the S50 gravitational decay rate was Gamma_grav = 5.2e-8 M_KK
Gamma_grav_S50 = 5.2e-8 * M_KK  # GeV
tau_L_S50_s = hbar_GeV_s / Gamma_grav_S50
print(f"\nCross-check (S50 Gamma_grav = 5.2e-8 M_KK):")
print(f"tau_L(S50) = {tau_L_S50_s:.4e} s")
print(f"tau_L(S50)/t_U = {tau_L_S50_s / t_universe_s:.4e}")

# ============================================================================
# 7. Free-streaming length
# ============================================================================

# The Leggett mode is produced at rest in the cell frame (it is a collective
# oscillation, not a relativistic particle). Its "velocity" comes from the
# Heisenberg uncertainty: v ~ p/m ~ T_eff/m for thermal production, or
# from the Bogoliubov boost for parametric production.
#
# In the superfluid analog: the Leggett mode in 3He-B has zero group velocity
# at k=0 (it is a gapped mode at the zone center). The framework Leggett is
# similarly k=0 in the 0D cell. On the fabric, it could propagate via
# Josephson coupling between cells, but the 0D production is at k=0.
#
# For the free-streaming estimate:
# v_L = p/E, where p ~ T_prod for thermal, or p ~ omega_tau for parametric.
# Since the mode is produced at T_prod ~ M_KK with mass m_L = 0.138 M_KK,
# it is initially relativistic: E ~ T >> m, v ~ 1.
# It becomes non-relativistic when T ~ m_L = 0.138 M_KK.
# The non-relativistic transition happens at T_NR = m_L.

T_NR_GeV = m_L_GeV  # non-relativistic transition
z_NR = T_NR_GeV / T_CMB_GeV - 1  # redshift at NR transition
a_NR = T_CMB_GeV / T_NR_GeV

print(f"\n--- Free-Streaming ---")
print(f"m_L = {m_L_GeV:.4e} GeV")
print(f"T_NR = {T_NR_GeV:.4e} GeV")
print(f"z_NR = {z_NR:.4e}")
print(f"a_NR = {a_NR:.4e}")

# BUT: the Leggett mode is NOT produced thermally. It is a coherent
# collective oscillation with no momentum. The 0D character means
# it has NO spatial momentum. The free-streaming length is therefore
# set by the Josephson coupling between cells on the fabric.
#
# Velocity from Josephson hopping: v_J ~ J * a_lattice, where
# J is the Josephson coupling and a_lattice is the cell spacing.
# From S47: J_C2 = 0.933 M_KK (dominant coupling).
# In the tight-binding limit: v_max = 2 * J * a / hbar.
# But a ~ 1/M_KK (cell size), so v_max ~ J / M_KK (dimensionless, in c=1 units).

from canonical_constants import J_C2
v_hopping = J_C2  # in M_KK units, dimensionless (c=1)
# This gives v ~ 0.93c -- nearly relativistic! But this is the GROUP velocity
# of the Leggett band, not the Leggett particle velocity.
# The Leggett dispersion is omega(k) = sqrt(omega_L^2 + v_J^2 * k^2)
# Group velocity at k=0: v_g(k=0) = 0 (gapped mode)
# At typical k (thermal): v_g ~ v_J * k / omega(k) ~ v_J * T / omega_L for T << omega_L

# Since the Leggett mode is produced as a k=0 condensate (coherent oscillation),
# its free-streaming velocity is effectively ZERO. The free-streaming comes only
# from quantum uncertainty: delta_v ~ 1/(m_L * L_cell) where L_cell ~ 1/M_KK.
v_quantum = 1.0 / (m_L_MKK * 1.0)  # in M_KK^{-1} * M_KK = dimensionless
# = 1/0.138 = 7.25 -- this is >c, meaning the uncertainty principle gives
# a "velocity" larger than c. This just means the mode is confined to the cell.
# Physical interpretation: the Leggett mode at k=0 has ZERO free-streaming.

# For the most conservative estimate (assuming thermal-like production):
# v_fs at matter-radiation equality z_eq ~ 3400
z_eq = 3400
T_eq_GeV = T_CMB_GeV * (1 + z_eq)  # ~ 0.8 eV
p_eq = T_eq_GeV if T_eq_GeV < m_L_GeV else m_L_GeV  # momentum at equality
v_eq = p_eq / np.sqrt(p_eq**2 + m_L_GeV**2)  # velocity at equality

print(f"\nT_eq = {T_eq_GeV:.4e} GeV")
print(f"m_L / T_eq = {m_L_GeV / T_eq_GeV:.4e} (deeply non-relativistic at eq)")
print(f"v_eq (if thermal) = {v_eq:.4e} c")
print(f"v_quantum (0D) = {v_quantum:.2f} (unphysical, >c means confined)")

# Free-streaming length (thermal approximation):
# lambda_fs ~ v_NR * t_eq / a_eq, where t_eq ~ 5.1e4 yr = 1.6e12 s
# For a massive particle that became NR at T_NR >> T_eq:
# lambda_fs ~ (T_NR / m_L) * (t_eq / a_eq) * (a_NR / a_eq)
# More precisely: integral from a_NR to a_eq of v(a) da / (a^2 H(a))
# For m_L >> T_eq: lambda_fs << 1 Mpc (cold DM)

# Standard formula for thermal relic free-streaming:
# lambda_fs = 0.2 * (m/1 keV)^{-1} Mpc  (for warm DM)
# This applies to thermal relics. For our m_L = 0.138 * 7.43e16 GeV = 1.03e16 GeV:
lambda_fs_thermal_Mpc = 0.2 * (m_L_GeV / 1e-6)**(-1)  # keV = 1e-6 GeV
print(f"\nlambda_fs (thermal formula) = {lambda_fs_thermal_Mpc:.4e} Mpc")

# For non-thermal production at k=0 (our case):
# The Leggett mode has ZERO momentum at production, so lambda_fs = 0 exactly.
# But quantum uncertainty gives delta_x ~ 1/m_L in natural units:
lambda_fs_quantum_GeVinv = 1.0 / m_L_GeV
lambda_fs_quantum_Mpc = lambda_fs_quantum_GeVinv * GeV_inv_to_Mpc
print(f"lambda_fs (Compton) = {lambda_fs_quantum_Mpc:.4e} Mpc")
print(f"lambda_fs (Compton) = {lambda_fs_quantum_GeVinv:.4e} GeV^-1")
print(f"                    = {lambda_fs_quantum_GeVinv * hbar_c_GeV_m:.4e} m")

# ============================================================================
# 8. Summary and gate assessment
# ============================================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

# Key numbers
print(f"\nm_L = {m_L_GeV:.4e} GeV ({m_L_MKK:.3f} M_KK)")
print(f"n_L per cell = {n_L_from_energy:.2f}")
print(f"Omega_L h^2 = {Omega_L_h2_v2:.4e}  (Method 1: n*m/rho_crit)")
print(f"Omega_L h^2 = {Omega_L_h2_v2b:.4e} (Method 2: energy fraction)")
print(f"Omega_DM h^2 = {Omega_DM_h2_obs:.3f} (observed)")
print(f"Ratio to observed = {Omega_L_h2_v2b / Omega_DM_h2_obs:.4e} (energy method)")

# The FUNDAMENTAL issue: overclosure
# rho_L(prod) = 3.01 * M_KK^4 ~ 10^67 GeV^4
# rho_crit = 4.08e-47 GeV^4
# Dilution (a_prod/a_0)^3 = (T_CMB/M_KK)^3 ~ (3e-13 / 7e16)^3 ~ 10^{-87}
# rho_L(today) ~ 10^67 * 10^{-87} = 10^{-20} GeV^4
# Omega_L ~ 10^{-20} / 10^{-47} = 10^{27}
# This is MASSIVE overclosure.

# However: this assumes ONE cell's worth of Leggett modes fills the
# Hubble volume. The correct counting is: the cell volume at production is
# V_cell ~ M_KK^{-3}, and the Hubble volume at production is
# V_H ~ H_prod^{-3} where H_prod ~ T_prod^2/M_Pl ~ M_KK^2/M_Pl.
# So V_H/V_cell ~ (M_Pl/M_KK)^3.

H_prod_GeV = M_KK**2 / M_Pl_reduced  # Hubble rate at T ~ M_KK (radiation dominated)
V_H_over_V_cell = (M_KK / H_prod_GeV)**3  # number of cell-volumes in Hubble volume

print(f"\n--- Volume Counting ---")
print(f"H(T=M_KK) = {H_prod_GeV:.4e} GeV")
print(f"V_H / V_cell = {V_H_over_V_cell:.4e}")
print(f"This is (M_Pl/M_KK)^3 = {(M_Pl_reduced/M_KK)**3:.4e}")

# The energy density is an INTENSIVE quantity: rho = E/V is the same
# regardless of how many cells we consider. So the energy density method
# (Method 2) is correct: rho_L = E_L_per_cell / V_cell = E_L * M_KK^4.
# The dilution a^{-3} is also correct for non-relativistic matter.

# Let's be very explicit about the overclosure:
log10_overclosure = np.log10(Omega_L_h2_v2b / Omega_DM_h2_obs)
print(f"\nOverclosure: {log10_overclosure:.1f} orders of magnitude")

# This is the standard GUT-scale moduli problem! Any particle with
# mass m ~ 10^{16} GeV produced at T ~ 10^{16} GeV with O(1) occupation
# per Hubble volume WILL overclose the universe unless diluted by inflation.
# This is precisely the cosmological moduli problem (Coughlan et al. 1983).

print(f"\n--- Decay Lifetime ---")
print(f"tau_L = {tau_L_s:.4e} s")
print(f"tau_L / t_U = {tau_L_over_tU:.4e}")
if tau_L_over_tU > 1:
    stability = "STABLE"
else:
    stability = "UNSTABLE"
print(f"Stability: {stability}")

print(f"\n--- Free Streaming ---")
print(f"lambda_fs (thermal) = {lambda_fs_thermal_Mpc:.4e} Mpc")
print(f"lambda_fs (Compton) = {lambda_fs_quantum_Mpc:.4e} Mpc")
if lambda_fs_thermal_Mpc < 0.01:
    fs_class = "COLD DM"
elif lambda_fs_thermal_Mpc < 0.1:
    fs_class = "COLD/WARM DM"
elif lambda_fs_thermal_Mpc < 10:
    fs_class = "WARM DM"
else:
    fs_class = "HOT DM (excluded)"
print(f"Classification: {fs_class}")

# ============================================================================
# 9. Gate verdict
# ============================================================================

# Pre-registered gate (from task prompt):
# PASS: Omega_L h^2 within 10x of 0.120 AND tau_L > 10*t_U AND lambda_fs < 0.1 Mpc
# FAIL: Omega_L h^2 off by >10^3 OR tau_L < t_U OR lambda_fs > 10 Mpc
# INFO: intermediate

abundance_ratio = abs(Omega_L_h2_v2b / Omega_DM_h2_obs)
abundance_offset = max(abundance_ratio, 1.0/abundance_ratio)

if abundance_offset <= 10 and tau_L_over_tU > 10 and lambda_fs_thermal_Mpc < 0.1:
    verdict = "PASS"
elif abundance_offset > 1e3 or tau_L_over_tU < 1 or lambda_fs_thermal_Mpc > 10:
    verdict = "FAIL"
else:
    verdict = "INFO"

# Construct reason
reasons = []
if abundance_offset > 1e3:
    reasons.append(f"Omega_L h^2 = {Omega_L_h2_v2b:.2e} ({log10_overclosure:.0f} OOM overclosure)")
if tau_L_over_tU < 1:
    reasons.append(f"tau_L < t_U (decays)")
if lambda_fs_thermal_Mpc > 10:
    reasons.append(f"lambda_fs > 10 Mpc (hot DM)")

if verdict == "PASS":
    detail = f"All three criteria met. Omega_L h^2 = {Omega_L_h2_v2b:.3f}, tau_L/t_U = {tau_L_over_tU:.1e}, lambda_fs = {lambda_fs_thermal_Mpc:.2e} Mpc"
elif verdict == "FAIL":
    detail = "; ".join(reasons)
else:
    detail = f"Intermediate: Omega_L h^2 = {Omega_L_h2_v2b:.2e}, tau_L/t_U = {tau_L_over_tU:.1e}, lambda_fs = {lambda_fs_thermal_Mpc:.2e} Mpc"

print(f"\n{'='*70}")
print(f"GATE VERDICT: {verdict}")
print(f"{'='*70}")
print(f"Detail: {detail}")

# ============================================================================
# 10. 3He analog assessment
# ============================================================================

print(f"\n--- 3He Superfluid Analog ---")
print("The Leggett mode overclosure is the EXACT analog of the cosmological")
print("moduli problem in string theory. In the superfluid framework:")
print("  - Leggett mass ~ 0.138 * M_KK ~ 10^16 GeV (GUT scale)")
print("  - Produced with O(1) quanta per cell during phase transition (KZ)")
print("  - Non-relativistic almost immediately (m >> T_eq)")
print("  - Gravitationally stable (tau >> t_U)")
print("  - Overclosure by ~27 orders")
print("")
print("In 3He-B: the Leggett mode exists but its energy is tiny compared to")
print("the thermal energy. It does not contribute to the 'cosmological constant'")
print("of the superfluid (the Gibbs-Duhem pressure). The overclosure problem")
print("does not arise because the Leggett energy is re-absorbed into the")
print("normal component via Raman scattering (available in 3D but forbidden in 0D).")
print("")
print("DIAGNOSIS: The overclosure is the cosmological moduli problem. Standard")
print("resolution requires late-time entropy production (inflation, late decay,")
print("thermal inflation). The framework currently lacks such a mechanism.")
print("This is STRUCTURAL: any GUT-scale relic with O(1) production needs dilution.")

# ============================================================================
# 11. Save results
# ============================================================================

results = {
    # Leggett mass
    'm_L_MKK': m_L_MKK,
    'm_L_GeV': m_L_GeV,
    'm_L_S50_MKK': m_L_S50,
    'm_L_S50_GeV': m_L_S50_GeV,

    # Number density
    'n_L_per_cell': n_L_from_energy,
    'n_L_total_fabric': n_L_total,
    'n_L_prod_GeV3': n_L_prod_GeV3,
    'n_L_today_GeV3': n_L_today_GeV3,

    # Cosmological
    'T_prod_GeV': T_prod_GeV,
    'a_prod_over_a0': a_prod_over_a0,
    'dilution_factor': a_prod_over_a0**3,

    # Abundance
    'rho_L_prod_GeV4': rho_L_prod_GeV4,
    'rho_L_today_GeV4': rho_L_today_v2,
    'Omega_L': Omega_L_v2,
    'Omega_L_h2': Omega_L_h2_v2b,
    'Omega_DM_h2_obs': Omega_DM_h2_obs,
    'ratio_to_obs': Omega_L_h2_v2b / Omega_DM_h2_obs,
    'log10_overclosure': log10_overclosure,

    # Decay
    'Gamma_grav_GeV': Gamma_grav_GeV,
    'tau_L_s': tau_L_s,
    'tau_L_over_tU': tau_L_over_tU,
    'stability': stability,

    # Free streaming
    'lambda_fs_thermal_Mpc': lambda_fs_thermal_Mpc,
    'lambda_fs_Compton_Mpc': lambda_fs_quantum_Mpc,
    'v_eq': v_eq,
    'z_NR': z_NR,
    'fs_class': fs_class,

    # Volume counting
    'H_prod_GeV': H_prod_GeV,
    'V_H_over_V_cell': V_H_over_V_cell,

    # Gate
    'gate_name': 'LEGGETT-DM-ABUND-60',
    'gate_verdict': verdict,
    'gate_detail': detail,
}

outpath = os.path.join(os.path.dirname(__file__), 's60_leggett_dm_abund.npz')
np.savez(outpath, **results)
print(f"\nSaved: {outpath}")
print("DONE.")
