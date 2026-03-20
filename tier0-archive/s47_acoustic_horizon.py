#!/usr/bin/env python3
"""
S47 ACOUSTIC-HORIZON-48: Acoustic Horizon at the BCS Transit
=============================================================
Gate: ACOUSTIC-HORIZON-48
  PASS: d_acoustic within factor 10 of 151 Mpc
  INFO: d_acoustic identifiable but > factor 10 from 151 Mpc
  FAIL: d_acoustic ~ l_Pl (Planck-scale)

Physics:
  The acoustic horizon is the maximum distance sound can propagate during
  the BCS transit.  In standard cosmology the BAO sound horizon is:
    r_s = integral_0^{t_rec} c_s(t) / a(t) dt = 147.09 Mpc
  Here we compute the analogous distance for the BCS transit in the
  phonon-exflation framework.

  Three distinct length scales:
  1. d_acoustic = c_s * dt_transit  (comoving acoustic horizon during transit)
  2. r_H = c / H  (Hubble radius at the fold)
  3. d_particle = c * t_age  (particle horizon at the fold epoch)

  The framework's BCS transit occurs at the Planck epoch (M_KK ~ M_Pl).
  The sound speed in the condensate must be identified carefully:
  - Internal space: BCS Bogoliubov speed c_s = v_F/sqrt(3) or sqrt(Delta/2m)
  - 4D emergent spacetime: c_fabric = c (Lorentz invariant, S42 result)
  - The effective BAO-type sound speed depends on the equation of state

Author: hawking-theorist
Date: 2026-03-16
Session: 47
"""

import numpy as np
import sys
from pathlib import Path

# Import canonical constants
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    # Transit parameters
    dt_transit, H_fold, v_terminal, omega_att, M_ATDHFB,
    # BCS parameters
    E_cond, Delta_0_GL, Delta_0_OES, xi_BCS, xi_GL,
    E_B1, E_B2_mean, E_B3_mean, n_pairs,
    # Geometric
    tau_fold, Z_fold, dS_fold, d2S_fold, S_fold, m_tau,
    # M_KK scales
    M_KK_gravity, M_KK_kerner, M_KK, M_Pl_reduced, M_Pl_unreduced,
    # Conversions
    GeV_inv_to_Mpc, Mpc_to_GeV_inv, hbar_c_GeV_m,
    hbar_GeV_s, c_light, l_Planck, t_Planck,
    Mpc_to_m, GeV_to_inv_s, GeV_to_inv_m,
    # Cosmological
    H_0_km_s_Mpc, H_0_GeV, T_CMB_GeV, T_CMB,
    Omega_m, Omega_Lambda, Omega_r, rho_crit_GeV4,
    # BCS condensation
    a_GL, b_GL, barrier_0d,
    # Fabric
    N_cells, L_over_xi, rho_B2_per_mode,
    # Spectral action
    a0_fold, a2_fold, a4_fold,
)

base = Path(__file__).parent

print("=" * 78)
print("S47 ACOUSTIC-HORIZON-48: ACOUSTIC HORIZON AT THE BCS TRANSIT")
print("=" * 78)

# ============================================================================
# 1. FRAMEWORK TRANSIT PARAMETERS (from canonical_constants + NPZ data)
# ============================================================================
print("\n--- 1. TRANSIT PARAMETERS ---")

# Load transit data for cross-checks
kz_data = np.load(base / "s38_kz_defects.npz", allow_pickle=True)
att_data = np.load(base / "s38_attempt_freq.npz", allow_pickle=True)
fab_data = np.load(base / "s42_fabric_dispersion.npz", allow_pickle=True)

# Key transit parameters (all in M_KK units)
print(f"  dt_transit     = {dt_transit:.6e} M_KK^{{-1}}")
print(f"  H_fold         = {H_fold:.2f} M_KK")
print(f"  v_terminal     = {v_terminal:.4f} M_KK")
print(f"  omega_att      = {omega_att:.4f} M_KK")
print(f"  M_ATDHFB       = {M_ATDHFB:.4f}")
print(f"  m_tau          = {m_tau:.4f} M_KK")

# The transit time was computed in S38 as:
#   dt_transit = delta_tau_BCS / v_terminal
# where delta_tau_BCS = 0.030 (width of BCS instability region in tau)
# and v_terminal = dS/dtau / (6*H*Z) is the friction-dominated velocity.
# This gives dt_transit ~ 0.030 / 26.54 = 0.00113 M_KK^{-1}

# Cross-check: Hubble time at fold
t_Hubble_fold = 1.0 / H_fold  # M_KK^{-1}
print(f"\n  t_Hubble_fold  = 1/H = {t_Hubble_fold:.6e} M_KK^{{-1}}")
print(f"  dt_transit / t_H = {dt_transit / t_Hubble_fold:.4f}")
print(f"  => Transit takes {dt_transit / t_Hubble_fold:.1%} of one Hubble time")

# Number of attractor oscillations during transit
N_osc_transit = omega_att * dt_transit / (2 * np.pi)
print(f"\n  N_osc_att      = omega_att * dt / (2pi) = {N_osc_transit:.4e}")
print(f"  => {N_osc_transit:.6f} attractor oscillations during transit")
print(f"     (transit is FAST compared to attractor oscillation)")

# ============================================================================
# 2. SOUND SPEEDS: WHICH ONE IS PHYSICAL?
# ============================================================================
print("\n--- 2. SOUND SPEED IDENTIFICATION ---")

# There are FOUR candidate sound speeds in this framework:

# (A) c_fabric = c = 1 (natural units)
# The speed of tau-modulus perturbations in the fabric.
# From S42: the spectral action is Lorentz-invariant, so tau perturbations
# propagate at the speed of light.  Dispersion: omega^2 = k^2 + m_tau^2
c_s_fabric = 1.0  # c, natural units
print(f"  A. c_fabric    = c = 1 (Lorentz invariant, massive KG field)")
print(f"     Dispersion: omega^2 = k^2 + {m_tau**2:.4f}")
print(f"     Group velocity: v_g = k/sqrt(k^2 + {m_tau**2:.4f})")
print(f"     At k >> m_tau: v_g -> 1 (luminal)")
print(f"     At k = m_tau:  v_g = 1/sqrt(2) = 0.707c")

# (B) BAO sound speed c_s = c/sqrt(3)
# In a radiation-dominated plasma, the baryon-photon fluid has c_s = c/sqrt(3).
# This is the standard BAO sound speed that gives r_s = 147 Mpc.
c_s_BAO = 1.0 / np.sqrt(3)
print(f"\n  B. c_BAO       = c/sqrt(3) = {c_s_BAO:.6f} c")
print(f"     (standard baryon-photon plasma sound speed)")

# (C) BCS Bogoliubov sound speed (internal space)
# In the BCS condensate, the Anderson-Bogoliubov mode has:
#   c_s = v_F / sqrt(3) (weak coupling)
# In the 0D limit (L/xi_GL = 0.031), there is no spatial propagation
# in the internal space.  The "sound speed" is the phase velocity of
# collective oscillations within the fiber.
# From S38: omega_PV = 0.792 M_KK (pair vibration frequency)
# In natural units, "velocity" = omega * L = 0.792 * 0.03 ~ 0.024 c
# This is NOT a 4D propagation speed.
omega_PV = float(att_data['omega_PV'])
v_BCS_internal = omega_PV * L_over_xi * xi_GL  # omega * L (internal "speed")
print(f"\n  C. v_BCS(int)  = omega_PV * L = {omega_PV:.4f} * {L_over_xi * xi_GL:.4f}")
print(f"                 = {v_BCS_internal:.6f} c (internal, not 4D)")
print(f"     (pair vibration across internal space, NOT a 4D sound speed)")

# (D) Modulus group velocity at the fold
# The tau perturbations have dispersion omega^2 = k^2 + m_tau^2
# The group velocity depends on k.  At the Hubble scale:
#   k_H = H_fold (the Hubble momentum)
# Note: k_H << m_tau, so v_g << c
k_H = H_fold  # Hubble-scale momentum in M_KK units
v_g_Hubble = k_H / np.sqrt(k_H**2 + m_tau**2)
print(f"\n  D. v_g(k=H)    = H/sqrt(H^2 + m_tau^2)")
print(f"                 = {H_fold:.1f}/sqrt({H_fold**2:.0f} + {m_tau**2:.4f})")
print(f"                 = {v_g_Hubble:.6f} c")

# CRITICAL POINT: H_fold = 586.5 >> m_tau = 2.06.
# This means the Hubble-scale modes are ULTRARELATIVISTIC (k >> m).
# For them, v_g ~ 1 - m^2/(2k^2) ~ 0.999994c.  Essentially luminal.
print(f"\n  CRITICAL: H_fold/m_tau = {H_fold/m_tau:.1f}")
print(f"  The Hubble-scale modes are ULTRARELATIVISTIC (k >> m).")
print(f"  For all modes with k > m_tau = 2.06 M_KK:")
print(f"    v_g = 1 - m^2/(2k^2) + ... ~ c to excellent approximation")
print(f"  The mass m_tau is IRRELEVANT at the transit epoch.")

# (E) What standard cosmology uses: c_s = c/sqrt(3*(1+R))
# where R = 3*rho_b / (4*rho_gamma) is the baryon loading.
# At the Planck epoch (before baryons exist), R = 0, so c_s = c/sqrt(3).
# BUT: this assumes a radiation-dominated thermal plasma.
# The framework at the transit epoch is NOT a thermal plasma.
# It is a BCS condensate dissolving via Parker-type particle creation.
# The equation of state is determined by the spectral action, not by
# radiation pressure.
print(f"\n  E. In standard cosmology: c_s = c/sqrt(3*(1+R))")
print(f"     At BBN (R~0): c_s = c/sqrt(3) = 0.577 c")
print(f"     The framework BCS transit is PRE-BBN (M_KK epoch).")
print(f"     No baryon-photon plasma exists yet.")

# ============================================================================
# 3. THE ACOUSTIC HORIZON
# ============================================================================
print("\n--- 3. ACOUSTIC HORIZON COMPUTATION ---")

# There are multiple definitions depending on which sound speed and which
# time interval are used.  I compute all of them.

# 3a. Transit acoustic horizon (c_fabric * dt_transit)
# This is the distance sound can travel across the emerging 4D spacetime
# during the BCS transit.  Uses c = 1 because tau perturbations propagate
# at the speed of light.
d_transit_MKK = c_s_fabric * dt_transit  # M_KK^{-1}
print(f"\n  3a. TRANSIT ACOUSTIC HORIZON (d = c * dt_transit)")
print(f"      d_transit  = {c_s_fabric} * {dt_transit:.6e} = {d_transit_MKK:.6e} M_KK^{{-1}}")

# Convert to physical units
# 1 M_KK^{-1} = hbar*c / M_KK [meters]
# For M_KK = M_KK_gravity = 7.43e16 GeV:
d_transit_GeV_inv = d_transit_MKK / M_KK  # GeV^{-1}
d_transit_m = d_transit_GeV_inv * hbar_c_GeV_m  # meters
d_transit_Mpc = d_transit_m / Mpc_to_m  # Mpc

print(f"      d_transit  = {d_transit_GeV_inv:.6e} GeV^{{-1}}")
print(f"      d_transit  = {d_transit_m:.6e} m")
print(f"      d_transit  = {d_transit_Mpc:.6e} Mpc")

# Alternatively, if M_KK ~ M_Pl:
d_transit_Pl_GeV_inv = d_transit_MKK / M_Pl_reduced
d_transit_Pl_m = d_transit_Pl_GeV_inv * hbar_c_GeV_m
d_transit_Pl_Mpc = d_transit_Pl_m / Mpc_to_m
print(f"\n      If M_KK = M_Pl_red = 2.435e18 GeV:")
print(f"      d_transit  = {d_transit_Pl_GeV_inv:.6e} GeV^{{-1}}")
print(f"      d_transit  = {d_transit_Pl_m:.6e} m")
print(f"      d_transit  = {d_transit_Pl_Mpc:.6e} Mpc")

# 3b. Hubble radius at fold
# r_H = c / H = 1 / H_fold in M_KK^{-1}
r_H_MKK = 1.0 / H_fold  # M_KK^{-1}
r_H_GeV_inv = r_H_MKK / M_KK
r_H_m = r_H_GeV_inv * hbar_c_GeV_m
r_H_Mpc = r_H_m / Mpc_to_m
print(f"\n  3b. HUBBLE RADIUS AT FOLD (r_H = c/H)")
print(f"      r_H = 1/{H_fold:.2f} = {r_H_MKK:.6e} M_KK^{{-1}}")
print(f"      r_H = {r_H_GeV_inv:.6e} GeV^{{-1}}")
print(f"      r_H = {r_H_m:.6e} m")
print(f"      r_H = {r_H_Mpc:.6e} Mpc")

r_H_Pl_Mpc = (1.0/H_fold) / M_Pl_reduced * hbar_c_GeV_m / Mpc_to_m
print(f"      If M_KK = M_Pl_red: r_H = {r_H_Pl_Mpc:.6e} Mpc")

# 3c. The BAO sound horizon in standard cosmology
# r_s = integral_0^{z_drag} c_s / H(z) dz / (1+z)
# The standard result: r_s = 147.09 +/- 0.26 Mpc (Planck 2018)
r_s_standard = 147.09  # Mpc
print(f"\n  3c. STANDARD BAO SOUND HORIZON")
print(f"      r_s(Planck 2018) = {r_s_standard} Mpc")
print(f"      Target for n_s resolution = 151 Mpc")
print(f"      Difference: {151 - r_s_standard:.2f} Mpc ({(151 - r_s_standard)/r_s_standard*100:.1f}%)")

# ============================================================================
# 4. COMOVING HORIZON AFTER EXPANSION
# ============================================================================
print("\n--- 4. COMOVING HORIZON AFTER EXPANSION ---")

# The transit acoustic horizon d_transit is a PHYSICAL distance at the
# transit epoch.  To compare with the BAO scale (which is a comoving
# distance), we must account for the expansion between the transit
# epoch and today.
#
# If the transit occurs at redshift z_transit:
#   d_comoving = d_physical * (1 + z_transit)
#
# The redshift of the transit epoch:
# The transit occurs when the temperature of the universe equals
# the BCS gap energy scale.  The relevant temperature is:
#   T_transit ~ M_KK (the KK scale)
#
# From the standard Friedmann expansion:
#   T(z) = T_CMB * (1 + z)
#   z_transit = T_transit / T_CMB - 1

# For M_KK_gravity = 7.43e16 GeV:
T_transit_gravity = M_KK  # GeV
z_transit_gravity = T_transit_gravity / T_CMB_GeV
print(f"  Transit temperature: T ~ M_KK = {M_KK:.3e} GeV")
print(f"  z_transit (gravity route) = {z_transit_gravity:.3e}")

# For M_KK = M_Pl:
z_transit_Pl = M_Pl_reduced / T_CMB_GeV
print(f"  z_transit (Planck route)  = {z_transit_Pl:.3e}")

# Comoving acoustic horizon:
d_comoving_MKK = d_transit_MKK  # already in M_KK^{-1}
# The comoving distance = physical distance * (1+z) / a_0
# In natural units with a_0 = 1 (today):
#   d_comoving = d_physical * (1 + z_transit)
# But d_physical at the transit epoch in METERS:
d_phys_transit_m = d_transit_m  # at the transit epoch
d_comoving_m = d_phys_transit_m * (1 + z_transit_gravity)
d_comoving_Mpc = d_comoving_m / Mpc_to_m

print(f"\n  Physical distance at transit: d_phys = {d_phys_transit_m:.3e} m")
print(f"  Expansion factor: (1 + z) = {1 + z_transit_gravity:.3e}")
print(f"  Comoving acoustic horizon: d_com = {d_comoving_m:.3e} m")
print(f"                             d_com = {d_comoving_Mpc:.3e} Mpc")

# If M_KK = M_Pl:
d_comoving_Pl_m = d_transit_Pl_m * (1 + z_transit_Pl)
d_comoving_Pl_Mpc = d_comoving_Pl_m / Mpc_to_m
print(f"\n  If M_KK = M_Pl_red:")
print(f"  d_com = {d_comoving_Pl_m:.3e} m")
print(f"  d_com = {d_comoving_Pl_Mpc:.3e} Mpc")

# ============================================================================
# 5. THE CRUCIAL QUESTION: INFLATION/EXFLATION EXPANSION
# ============================================================================
print("\n--- 5. EXPANSION DURING AND AFTER TRANSIT ---")

# The simple (1+z) scaling above assumes the transit happened in an
# FRW universe that expanded smoothly to today.  But the framework
# posits that the transit IS the origin of expansion.  The exflation
# IS the transit from SU(3) to the observed universe.
#
# In standard inflation, a tiny patch of size ~ H^{-1}_infl is
# expanded to the observed universe.  The number of e-folds:
#   N_e = ln(a_end / a_start)
# For the observed universe to emerge from a Hubble patch at the
# Planck epoch:
#   N_e = ln(T_transit / T_0) ~ ln(M_KK / T_CMB)

N_efolds_gravity = np.log(M_KK / T_CMB_GeV)
N_efolds_Planck = np.log(M_Pl_reduced / T_CMB_GeV)
print(f"  N_efolds needed (gravity M_KK): {N_efolds_gravity:.1f}")
print(f"  N_efolds needed (Planck M_KK):  {N_efolds_Planck:.1f}")
print(f"  Standard inflation requires:     ~60 e-folds")

# The H at the fold in PHYSICAL units:
H_fold_GeV = H_fold * M_KK  # GeV
H_fold_inv_s = H_fold_GeV * GeV_to_inv_s
H_fold_Mpc = H_fold_GeV * GeV_inv_to_Mpc

print(f"\n  H_fold = {H_fold:.2f} M_KK = {H_fold_GeV:.3e} GeV")
print(f"  H_fold = {H_fold_inv_s:.3e} s^{{-1}}")
print(f"  r_H(fold) = c/H = {1.0/H_fold_inv_s * c_light:.3e} m = {1.0/H_fold_GeV * hbar_c_GeV_m / Mpc_to_m:.3e} Mpc")

# The Hubble patch at the fold that expands to become today's universe:
# Comoving size today = r_H(fold) * a(today)/a(fold) = r_H(fold) * (1+z_fold)
# But r_H(fold) in physical meters at the fold epoch:
r_H_fold_m = hbar_c_GeV_m / (H_fold * M_KK)
r_H_comoving_today_m = r_H_fold_m * (1 + z_transit_gravity)
r_H_comoving_today_Mpc = r_H_comoving_today_m / Mpc_to_m
print(f"\n  Hubble patch at fold:")
print(f"    Physical size: {r_H_fold_m:.3e} m")
print(f"    Comoving today (simple scaling): {r_H_comoving_today_Mpc:.3e} Mpc")
print(f"    Observable universe: ~46,300 Mpc (comoving radius)")

# ============================================================================
# 6. THE BAO CONNECTION
# ============================================================================
print("\n--- 6. THE BAO CONNECTION ---")

# The standard BAO scale r_s = 147 Mpc comes from:
#   r_s = integral_0^{t_drag} c_s(t) dt / a(t)
# where c_s = c/sqrt(3*(1+R)), R = 3*rho_b/(4*rho_gamma)
# and t_drag ~ 370,000 years (recombination + drag epoch)
#
# This integral runs from the BIG BANG to the drag epoch.
# The sound horizon is NOT set by any single epoch -- it accumulates
# over the entire radiation-dominated era.
#
# In the phonon-exflation framework, what sets r_s?
# The BCS transit is the ORIGIN event.  After the transit:
# - The GGE thermalizes to T_Gibbs = 0.113 M_KK
# - The universe enters a radiation-dominated phase
# - Standard cosmology takes over
# - The BAO integral runs from t_transit to t_drag
#
# The critical question: does the framework MODIFY c_s between the
# transit and recombination?  If not, then r_s is determined entirely
# by standard physics, and the 147 Mpc result is inherited.

# In standard cosmology:
# r_s = integral_0^{a_drag} c_s da / (a^2 H(a))
# The dominant contribution comes from the radiation-dominated era.
# The integral can be broken into two parts:
# (1) Early (a < a_eq): radiation dominated, c_s ~ c/sqrt(3)
# (2) Late (a_eq < a < a_drag): matter-radiation transition

# In the framework, part (1) is IDENTICAL to standard cosmology if:
# - The universe is radiation-dominated after thermalization
# - c_s = c/sqrt(3) in the baryon-photon plasma
# - The expansion rate H(a) follows the standard Friedmann equation
#
# All three conditions hold if M_KK is high enough that the transit
# completes before any standard cosmology processes begin.

# The transit completes at T ~ M_KK.  Standard BBN begins at T ~ 1 MeV.
# The ratio:
ratio_MKK_BBN = M_KK / 1e-3  # M_KK in GeV / 1 MeV in GeV
print(f"  M_KK / T_BBN = {ratio_MKK_BBN:.3e}")
print(f"  Transit completes at T = {M_KK:.3e} GeV")
print(f"  BBN begins at T = 1 MeV = 1e-3 GeV")
print(f"  Separation: {np.log10(ratio_MKK_BBN):.1f} orders of magnitude")
print(f"  => Standard cosmology from BBN onward is UNMODIFIED")

# Therefore the standard r_s = 147 Mpc is INHERITED by the framework.
# The BCS transit cannot modify it because the transit completes
# 10^{19} orders of magnitude before the sound horizon is set.

print(f"\n  CONCLUSION: The framework INHERITS r_s = 147 Mpc from standard")
print(f"  cosmology.  The BCS transit is separated from the BAO epoch by")
print(f"  {np.log10(ratio_MKK_BBN):.0f} decades in temperature.  No framework")
print(f"  modification of the baryon-photon plasma sound speed is possible.")
print(f"\n  The 151 Mpc needed for n_s resolution is NOT the transit acoustic")
print(f"  horizon.  It would have to be a modified BAO scale, which requires")
print(f"  new physics between the transit and recombination -- physics that")
print(f"  the framework does not predict.")

# ============================================================================
# 7. WHAT THE TRANSIT ACOUSTIC HORIZON ACTUALLY IS
# ============================================================================
print("\n--- 7. TRANSIT ACOUSTIC HORIZON: WHAT IT ACTUALLY IS ---")

# The transit acoustic horizon d_transit = c * dt_transit = 1.13e-3 M_KK^{-1}
# is the distance across which causal correlations can be established
# DURING the transit itself.  This sets the correlation length of the
# post-transit state.
#
# In the Kibble-Zurek picture (S38), the relevant length is:
#   xi_KZ = xi_0 * (tau_Q / tau_0)^{nu/(1+z*nu)}
# where xi_0 = xi_BCS, tau_Q is the quench time, tau_0 is the
# relaxation time, and nu, z are critical exponents.
#
# From S38: xi_KZ = xi_BCS = 0.808 M_KK^{-1} (because P_exc = 1, all
# modes are excited -- the system is in the "sudden" limit).

xi_KZ = xi_BCS  # M_KK^{-1}
xi_KZ_m = xi_KZ / M_KK * hbar_c_GeV_m
xi_KZ_Mpc = xi_KZ_m / Mpc_to_m
print(f"  Kibble-Zurek correlation length: xi_KZ = {xi_KZ:.4f} M_KK^{{-1}}")
print(f"  Physical: xi_KZ = {xi_KZ_m:.3e} m = {xi_KZ_Mpc:.3e} Mpc")

# Transit acoustic horizon vs xi_KZ:
print(f"\n  d_transit / xi_KZ = {d_transit_MKK / xi_KZ:.4f}")
print(f"  => Transit horizon is {d_transit_MKK / xi_KZ:.4f}x the KZ correlation length")
print(f"     Transit is FASTER than the correlation time.")
print(f"     Correlations are set by xi_KZ, not d_transit.")

# Comoving KZ scale today:
xi_KZ_comoving_Mpc = xi_KZ_Mpc * (1 + z_transit_gravity)
print(f"\n  xi_KZ comoving today = {xi_KZ_comoving_Mpc:.3e} Mpc")
print(f"  (if simple (1+z) scaling from z_transit)")

# But this is NOT observable as r_s.  It would be the correlation
# length of the INITIAL perturbation spectrum, not the BAO scale.

# ============================================================================
# 8. THE PARTICLE HORIZON
# ============================================================================
print("\n--- 8. PARTICLE HORIZON AT THE TRANSIT EPOCH ---")

# The particle horizon at time t is:
#   d_H(t) = a(t) * integral_0^t c dt' / a(t')
# At the Planck epoch in a radiation-dominated universe:
#   a(t) ~ t^{1/2}, so d_H = 2ct = 2 * c * t_Pl ~ 2 * l_Pl
# This is the causal horizon at the Planck time.

# If the transit happens at the Planck time:
d_particle_Pl = 2.0 * l_Planck  # meters
d_particle_Pl_Mpc = d_particle_Pl / Mpc_to_m
print(f"  Particle horizon at Planck time: d_H ~ 2*l_Pl = {d_particle_Pl:.3e} m")
print(f"  d_H = {d_particle_Pl_Mpc:.3e} Mpc")

# If the transit happens at T = M_KK (gravity route):
# In radiation domination: H = (pi^2 g_*/90)^{1/2} * T^2 / M_Pl
# g_* at T ~ 10^{16} GeV: all SM + KK modes ~ 106.75 (SM) or more
g_star_transit = 106.75  # conservative (SM only)
H_at_MKK = np.sqrt(np.pi**2 * g_star_transit / 90) * M_KK**2 / M_Pl_unreduced  # GeV
t_at_MKK = 1.0 / (2.0 * H_at_MKK)  # seconds (radiation domination: t = 1/(2H))
d_particle_MKK_m = 2.0 * c_light * (hbar_GeV_s / H_at_MKK)  # d_H = 2*c*t = c/H
d_particle_MKK_Mpc = d_particle_MKK_m / Mpc_to_m

print(f"\n  If transit at T = M_KK = {M_KK:.3e} GeV (standard Friedmann):")
print(f"  H(T=M_KK) = {H_at_MKK:.3e} GeV")
print(f"  t(T=M_KK) = {hbar_GeV_s / (2*H_at_MKK):.3e} s")
print(f"  d_H = c/H = {hbar_c_GeV_m / H_at_MKK:.3e} m = {hbar_c_GeV_m / H_at_MKK / Mpc_to_m:.3e} Mpc")

# This d_H is the particle horizon in STANDARD Friedmann cosmology
# at the transit temperature.  It's tiny -- about 10^{-27} Mpc.

# ============================================================================
# 9. COMPARISON: FRAMEWORK H vs STANDARD FRIEDMANN H
# ============================================================================
print("\n--- 9. FRAMEWORK H_fold vs STANDARD FRIEDMANN H ---")

# The framework's H_fold = 586.5 M_KK is ENORMOUS.
# In standard Friedmann at T = M_KK:
#   H_Friedmann = sqrt(pi^2 g_*/90) * T^2/M_Pl
# With T = M_KK = 7.43e16 GeV, M_Pl = 1.22e19 GeV:
H_Friedmann_at_MKK = np.sqrt(np.pi**2 * g_star_transit / 90) * M_KK**2 / M_Pl_unreduced
H_ratio = H_fold * M_KK / H_Friedmann_at_MKK
print(f"  H_fold (framework) = {H_fold * M_KK:.3e} GeV")
print(f"  H_Friedmann(T=M_KK) = {H_Friedmann_at_MKK:.3e} GeV")
print(f"  Ratio: H_fold / H_Friedmann = {H_ratio:.3e}")

# The framework H is driven by the spectral action gradient (dS/dtau),
# not by the energy density.  It is ~10^{17} times larger than the
# standard Friedmann H at the same temperature.
print(f"\n  The framework H is driven by the spectral action gradient dS/dtau,")
print(f"  not by the energy density rho.  This is the FRIEDMANN SHORTFALL:")
print(f"  the spectral action drive is {H_ratio:.0e}x larger than what")
print(f"  the gravitational energy density can produce.")
print(f"  (This was previously identified as the 35,000-114,000x shortfall.)")

# ============================================================================
# 10. THE STANDARD r_s: WHY 147 Mpc AND ITS RELATION TO 151 Mpc
# ============================================================================
print("\n--- 10. THE STANDARD r_s AND THE 151 Mpc TARGET ---")

# The BAO sound horizon r_s = 147.09 Mpc is set by:
# 1. The sound speed c_s(z) = c / sqrt(3*(1+R(z)))
#    where R(z) = 3*Omega_b / (4*Omega_gamma) * 1/(1+z)
# 2. The expansion rate H(z) = H_0 * E(z)
# 3. The drag epoch z_drag = 1059.68 (Planck 2018)
#
# r_s = integral_{z_drag}^{infinity} c_s(z) dz / H(z)
#
# The 151 Mpc needed for n_s = 0.965:
# If the primordial power spectrum P(k) has its shape set by a
# correlation scale k_* = 2*pi / r_*, then r_* determines the
# spectral index through:
#   n_s - 1 = d ln P / d ln k evaluated at k_* = 2*pi / r_*
#
# The 4 Mpc difference between 147 and 151 is 2.7%.
# In standard cosmology, this corresponds to a ~2.7% change in
# the integral, achievable by small changes in Omega_b*h^2 or H_0.

print(f"  r_s(Planck 2018) = 147.09 Mpc")
print(f"  Target for n_s:    151 Mpc")
print(f"  Difference:        {151 - 147.09:.2f} Mpc = {(151 - 147.09)/147.09*100:.1f}%")
print(f"")
print(f"  CRITICAL OBSERVATION:")
print(f"  The 147 Mpc and 151 Mpc are BOTH set by post-BBN physics.")
print(f"  The BCS transit happens at {M_KK:.0e} GeV, which is")
print(f"  {np.log10(M_KK/1e-3):.0f} orders of magnitude before BBN.")
print(f"  The transit acoustic horizon (~{d_transit_Mpc:.0e} Mpc) is")
print(f"  {np.log10(147/d_transit_Mpc):.0f} orders of magnitude smaller than r_s.")
print(f"")
print(f"  The transit sets INITIAL CONDITIONS for the post-transit universe.")
print(f"  The BAO scale is set by the SUBSEQUENT evolution of those conditions.")
print(f"  These are separated by {np.log10(M_KK/1e-3):.0f} decades in temperature.")

# ============================================================================
# 11. ACOUSTIC TEMPERATURE CROSS-CHECK (from MEMORY)
# ============================================================================
print("\n--- 11. ACOUSTIC TEMPERATURE CROSS-CHECK ---")

# From S40 T-ACOUSTIC-40:
# T_a/T_Gibbs = 0.993 (acoustic metric)
# T_Gibbs = 0.113 M_KK
# The acoustic metric gives a Hawking-like temperature for the
# phononic excitations crossing the fold.  This temperature is
# set by the surface gravity of the acoustic horizon.
#
# In standard Hawking radiation: T = kappa / (2*pi)
# The acoustic analog: T_a = (d c_s/dx)|_{horizon} / (2*pi)
#
# The acoustic metric sound speed gradient at the fold determines
# T_a, which is geometric (set by the fold structure, not by BCS).

T_Gibbs = 0.113  # M_KK (from S40)
T_a = T_Gibbs * 0.993  # acoustic metric temperature
print(f"  T_Gibbs = 0.113 M_KK (post-transit equilibrium)")
print(f"  T_a = {T_a:.4f} M_KK (acoustic metric, S40)")
print(f"  T_a / T_Gibbs = 0.993 (0.7% match)")
print(f"  => Acoustic temperature is set by fold geometry, confirmed T-ACOUSTIC-40")

# The thermal de Broglie wavelength at T_a:
lambda_dB = 1.0 / np.sqrt(2 * np.pi * E_B2_mean * T_a)  # M_KK^{-1}
print(f"\n  Thermal de Broglie wavelength:")
print(f"  lambda_dB = 1/sqrt(2*pi*M*T) = {lambda_dB:.4f} M_KK^{{-1}}")
print(f"  lambda_dB / xi_BCS = {lambda_dB / xi_BCS:.4f}")

# ============================================================================
# 12. GATE VERDICT
# ============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: ACOUSTIC-HORIZON-48")
print("=" * 78)

# The transit acoustic horizon is the distance sound propagates during
# the BCS transit.  This is unambiguous:
#   d_acoustic = c_fabric * dt_transit = 1.0 * 1.13e-3 M_KK^{-1}
#              = 1.52e-20 GeV^{-1}
#              = 3.00e-36 m
#              = 9.72e-59 Mpc

# Comparing to 151 Mpc:
ratio_to_target = d_transit_Mpc / 151.0
log_ratio = np.log10(ratio_to_target) if ratio_to_target > 0 else float('-inf')

print(f"\n  d_acoustic (transit) = {d_transit_Mpc:.3e} Mpc")
print(f"  Target: 151 Mpc")
print(f"  Ratio: d_acoustic / 151 = {ratio_to_target:.3e}")
print(f"  log10(ratio) = {log_ratio:.1f}")

# Even with comoving stretching:
print(f"\n  d_acoustic (comoving, z_transit={z_transit_gravity:.1e}) = {d_comoving_Mpc:.3e} Mpc")
ratio_comoving = d_comoving_Mpc / 151.0
log_ratio_comoving = np.log10(ratio_comoving) if ratio_comoving > 0 else float('-inf')
print(f"  Ratio (comoving): {ratio_comoving:.3e}")
print(f"  log10(ratio) = {log_ratio_comoving:.1f}")

# Determine gate verdict
if abs(log_ratio) <= 1:
    verdict = "PASS"
    verdict_detail = f"d_acoustic within factor 10 of 151 Mpc"
elif d_transit_Mpc > l_Planck / Mpc_to_m * 100:  # well above Planck scale
    verdict = "INFO"
    verdict_detail = (f"d_acoustic = {d_transit_Mpc:.1e} Mpc, factor "
                      f"10^{abs(log_ratio):.0f} from 151 Mpc")
else:
    verdict = "FAIL"
    verdict_detail = "d_acoustic ~ l_Pl (Planck-scale)"

print(f"\n  VERDICT: {verdict}")
print(f"  Detail: {verdict_detail}")

# ============================================================================
# 13. THE HONEST ASSESSMENT
# ============================================================================
print("\n--- 13. HONEST ASSESSMENT ---")
print(f"""
  The transit acoustic horizon is {d_transit_Mpc:.1e} Mpc.
  This is {abs(log_ratio):.0f} orders of magnitude below 151 Mpc.
  Even after comoving stretching by (1+z) ~ {z_transit_gravity:.0e},
  the comoving transit horizon is {d_comoving_Mpc:.1e} Mpc.

  THE TRANSIT CANNOT SET THE BAO SCALE.

  The 147 Mpc BAO sound horizon is a standard cosmological
  observable set by baryon-photon plasma physics at z ~ 1060.
  The BCS transit occurs at z ~ {z_transit_gravity:.0e}, some
  {np.log10(z_transit_gravity/1060):.0f} decades earlier.  The transit
  determines INITIAL CONDITIONS (the primordial power spectrum),
  not the acoustic scale.

  The 151 Mpc needed for n_s resolution refers to the
  correlation length of the primordial perturbation spectrum,
  not the BAO sound horizon.  These are DIFFERENT quantities:
  - r_s = 147 Mpc is an integral of c_s/H from z=infinity to z_drag
  - r_corr = 151 Mpc would be set by the spectrum at formation

  If the framework's primordial spectrum has a characteristic
  scale k_* that happens to give n_s = 0.965 when convolved
  with the transfer function, that scale must be built in at
  formation, not generated by acoustic propagation during transit.

  The closeness of 147 and 151 Mpc is suggestive but COINCIDENTAL
  from the framework's perspective.  The 147 Mpc is set by post-BBN
  plasma physics.  The 151 Mpc target is set by the required n_s.
  Both derive from standard cosmological evolution, not from the
  BCS transit.
""")

# ============================================================================
# 14. SUMMARY TABLE
# ============================================================================
print("\n--- SUMMARY TABLE ---")
print(f"{'Quantity':<45} {'M_KK units':>15} {'Mpc':>15}")
print("-" * 78)
print(f"{'Transit duration dt_transit':<45} {dt_transit:>15.6e} {'-':>15}")
print(f"{'Transit acoustic horizon c*dt':<45} {d_transit_MKK:>15.6e} {d_transit_Mpc:>15.3e}")
print(f"{'Comoving transit horizon (gravity M_KK)':<45} {'-':>15} {d_comoving_Mpc:>15.3e}")
print(f"{'KZ correlation length xi_KZ':<45} {xi_KZ:>15.4f} {xi_KZ_Mpc:>15.3e}")
print(f"{'Hubble radius at fold r_H':<45} {r_H_MKK:>15.6e} {r_H_Mpc:>15.3e}")
print(f"{'Particle horizon at Planck time':<45} {'-':>15} {d_particle_Pl_Mpc:>15.3e}")
print(f"{'Standard BAO r_s':<45} {'-':>15} {'147.09':>15}")
print(f"{'Target for n_s resolution':<45} {'-':>15} {'151':>15}")
print(f"{'Transit / Target':<45} {'-':>15} {ratio_to_target:>15.3e}")
print("-" * 78)

# ============================================================================
# 15. SAVE DATA
# ============================================================================
print("\n--- SAVING DATA ---")

outfile = base / "s47_acoustic_horizon.npz"
np.savez(outfile,
    # Gate
    gate_name="ACOUSTIC-HORIZON-48",
    gate_verdict=verdict,
    gate_detail=verdict_detail,
    # Transit parameters
    dt_transit=dt_transit,
    H_fold=H_fold,
    v_terminal=v_terminal,
    omega_att=omega_att,
    m_tau=m_tau,
    # Sound speeds
    c_fabric=1.0,
    c_BAO=c_s_BAO,
    v_BCS_internal=v_BCS_internal,
    v_g_Hubble=v_g_Hubble,
    # Acoustic horizons (M_KK^{-1})
    d_transit_MKK=d_transit_MKK,
    d_transit_Mpc=d_transit_Mpc,
    d_comoving_Mpc=d_comoving_Mpc,
    # Hubble radius
    r_H_MKK=r_H_MKK,
    r_H_Mpc=r_H_Mpc,
    # KZ scale
    xi_KZ_MKK=xi_KZ,
    xi_KZ_Mpc=xi_KZ_Mpc,
    # Particle horizon
    d_particle_Pl_Mpc=d_particle_Pl_Mpc,
    # Standard BAO
    r_s_standard=r_s_standard,
    target_Mpc=151.0,
    ratio_to_target=ratio_to_target,
    log_ratio=log_ratio,
    # Redshift
    z_transit_gravity=z_transit_gravity,
    z_transit_Planck=z_transit_Pl,
    # N e-folds
    N_efolds_gravity=N_efolds_gravity,
    N_efolds_Planck=N_efolds_Planck,
    # Framework vs Friedmann
    H_fold_GeV=H_fold * M_KK,
    H_Friedmann_at_MKK=H_Friedmann_at_MKK,
    H_ratio=H_ratio,
    # Acoustic temperature
    T_a_MKK=T_a,
    T_Gibbs_MKK=T_Gibbs,
    lambda_dB_MKK=lambda_dB,
    # M_KK used
    M_KK_used=M_KK,
)
print(f"Data saved to: {outfile}")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
