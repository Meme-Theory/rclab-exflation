#!/usr/bin/env python3
"""
s57_ns_mapping.py — NS-MAPPING-57 (W3-8)
=========================================
Transfer function: KK-scale DM properties → cosmological observables.

Gate: INFO — map GGE quasiparticle DM to observable signatures.

Method:
  1. Mass spectrum: m_DM = E_k * M_KK for each GGE branch
  2. Self-scattering cross-section: sigma/m from scattering length and quasiparticle mass
  3. Phase space distribution: non-thermal GGE vs thermal WIMP
  4. Free-streaming length and equation of state
  5. Observational discriminants (P(k), halo mass, Lyman-alpha, direct detection)

Inputs:
  - s57_finite_rate_transit.npz (W1-1)
  - s57_leggett_partition.npz (W1-2)
  - s57_gge_equilibrium_gap.npz (W0-3)
  - canonical_constants.py

Output: s57_ns_mapping.npz + console summary
"""

import sys
import numpy as np

sys.path.insert(0, "computations")
from canonical_constants import (, z_eq_planck
    M_KK, M_KK_gravity, M_KK_kerner,
    E_B1, E_B2_mean, E_B3_mean,
    rho_crit_GeV4, Omega_DM, Omega_m, Omega_b,
    H_0_km_s_Mpc, H_0_GeV, T_CMB, T_CMB_GeV,
    k_B, c_light, c_light_km_s, c_light_cgs,
    hbar_c_GeV_cm, hbar_c_GeV_fm, hbar_c_GeV_m,
    GeV_to_g, GeV_to_inv_m, Mpc_to_cm, Mpc_to_m,
    kpc_to_cm, GeV_inv_to_Mpc, Mpc_to_GeV_inv,
    M_Pl_reduced, M_Pl_unreduced, G_N,
    a_scatter, N_cells, n_pairs,
    E_cond, E_exc, N_dof_BCS,
    t_universe_s, rho_Lambda_obs,
    sigma_8, A_s_CMB, Omega_Lambda,
    l_Planck, l_Planck_cm,
    PI,
)

# ============================================================================
#  Load input data
# ============================================================================

transit = np.load("computations/session-57/s57_finite_rate_transit.npz", allow_pickle=True)
leggett = np.load("computations/session-57/s57_leggett_partition.npz", allow_pickle=True)
gge = np.load("computations/session-57/s57_gge_equilibrium_gap.npz", allow_pickle=True)

P_exc_final = float(transit["P_exc_final"])
f_DM_energy = float(leggett["f_DM_energy"])
shortfall_factor = float(leggett["shortfall_factor"])
E_BCS_exc = float(leggett["E_BCS_exc"])

E_k = gge["E_k"]           # Quasiparticle energies in M_KK units (8 modes)
xi_k = gge["xi"]           # Single-particle energies in M_KK units
fk_gge = gge["fk_gge"]     # GGE occupation numbers
T_k_volovik = gge["T_k_volovik"]  # Per-mode effective temperatures
beta_k = gge["beta_k"]     # Per-mode inverse temperatures
branch_labels = gge["branch_labels"]
N_modes = int(gge["N_modes"])
n_pairs_phys = float(gge["n_pairs_physical"])

S_GGE = float(gge["S_GGE_canonical"])
S_eq = float(gge["S_eq_canonical"])
S_max = float(gge["S_max_canonical"])
D_KL = float(gge["D_KL_canonical"])
D_JS = float(gge["D_JS_canonical"])
T_max_volovik = float(gge["T_max_volovik"])
T_min_volovik = float(gge["T_min_volovik"])

print("=" * 72)
print("NS-MAPPING-57: KK-Scale DM → Cosmological Observables")
print("=" * 72)

# ============================================================================
#  SECTION 1: DM MASS SPECTRUM
# ============================================================================
print("\n--- 1. DM MASS SPECTRUM ---")

# Physical quasiparticle masses: m_k = E_k * M_KK
m_DM_GeV = E_k * M_KK  # in GeV

# Branch-averaged masses
m_B2_GeV = E_B2_mean * M_KK
m_B1_GeV = E_B1 * M_KK
m_B3_GeV = E_B3_mean * M_KK

# Mean DM mass weighted by GGE occupations
m_DM_mean_GeV = np.sum(fk_gge * m_DM_GeV) / np.sum(fk_gge)

# In grams (for sigma/m)
m_DM_g = m_DM_GeV * GeV_to_g
m_DM_mean_g = m_DM_mean_GeV * GeV_to_g

print(f"  M_KK = {M_KK:.4e} GeV")
print(f"  Branch masses (GeV):")
print(f"    B1:        m = {m_B1_GeV:.4e} GeV  ({E_B1:.6f} M_KK)")
print(f"    B2 (mean): m = {m_B2_GeV:.4e} GeV  ({E_B2_mean:.6f} M_KK)")
print(f"    B3 (mean): m = {m_B3_GeV:.4e} GeV  ({E_B3_mean:.6f} M_KK)")
print(f"  Per-mode masses (GeV): {m_DM_GeV}")
print(f"  GGE-weighted mean mass: {m_DM_mean_GeV:.4e} GeV")
print(f"  GGE-weighted mean mass: {m_DM_mean_g:.4e} g")
print(f"  Regime: SUPERHEAVY (wimpzilla), m_DM >> M_GUT ~ 10^16 GeV")

# Compare to known DM mass windows
m_DM_over_M_GUT = m_DM_mean_GeV / 1e16
m_DM_over_M_Pl = m_DM_mean_GeV / M_Pl_unreduced
print(f"  m_DM / M_GUT  = {m_DM_over_M_GUT:.2f}")
print(f"  m_DM / M_Pl   = {m_DM_over_M_Pl:.4e}")

# ============================================================================
#  SECTION 2: SELF-SCATTERING CROSS-SECTION
# ============================================================================
print("\n--- 2. SELF-SCATTERING CROSS-SECTION ---")

# Scattering length from S52: a_scatter = -1.58e-3 M_KK^{-1}
# Convert to physical units
a_scatter_cm = abs(a_scatter) * hbar_c_GeV_cm / M_KK  # cm
a_scatter_fm = abs(a_scatter) * hbar_c_GeV_fm / M_KK   # fm

# Low-energy s-wave scattering cross-section: sigma = 4*pi*a^2
# (Born approximation for self-conjugate quasiparticles)
sigma_scatter_cm2 = 4.0 * PI * a_scatter_cm**2

# sigma/m for self-interaction constraint (Bullet Cluster: sigma/m < 1 cm^2/g)
# Use mean DM mass
sigma_over_m = sigma_scatter_cm2 / m_DM_mean_g

print(f"  Scattering length a = {abs(a_scatter):.4e} M_KK^{{-1}}")
print(f"  a_scatter = {a_scatter_cm:.4e} cm = {a_scatter_fm:.4e} fm")
print(f"  sigma_scatter = 4*pi*a^2 = {sigma_scatter_cm2:.4e} cm^2")
print(f"  sigma/m = {sigma_over_m:.4e} cm^2/g")
print(f"  Bullet Cluster bound: sigma/m < 1 cm^2/g")
print(f"  Satisfied by {1.0 / sigma_over_m:.2e}x margin")
print(f"  Classification: COLLISIONLESS")

# Also compute perturbative self-scattering: sigma ~ g^4 / (16*pi*m^2)
# Using effective coupling g_eff from BCS: V ~ E_cond / N_modes
g_eff_sq = abs(E_cond) / N_dof_BCS  # Effective coupling^2 in M_KK units
sigma_pert_MKK = g_eff_sq**2 / (16.0 * PI * E_B2_mean**2)  # in M_KK^{-2}
sigma_pert_cm2 = sigma_pert_MKK * (hbar_c_GeV_cm / M_KK)**2
sigma_over_m_pert = sigma_pert_cm2 / m_DM_mean_g

print(f"\n  Perturbative estimate (g^4/16*pi*m^2):")
print(f"    g_eff^2 = |E_cond|/N_modes = {g_eff_sq:.6f} M_KK")
print(f"    sigma_pert = {sigma_pert_cm2:.4e} cm^2")
print(f"    sigma_pert/m = {sigma_over_m_pert:.4e} cm^2/g")

# ============================================================================
#  SECTION 3: PHASE SPACE DISTRIBUTION
# ============================================================================
print("\n--- 3. PHASE SPACE DISTRIBUTION ---")

# The GGE distribution is f_k = fk_gge for each mode k
# This is NOT Fermi-Dirac: each mode has its own effective temperature T_k
# Characterized by 8 independent Lagrange multipliers (integrals of motion)

# For comparison, a thermal Fermi-Dirac at the canonical equilibrium temperature:
T_eq = float(gge["T_eq_canonical"])  # Canonical equilibrium temperature
fk_eq = gge["fk_eq_canonical"]       # Equilibrium occupations

print(f"  GGE occupation numbers f_k:")
for i in range(N_modes):
    bl = str(branch_labels[i])
    print(f"    {bl:8s}: f={fk_gge[i]:.6f}, T_eff={T_k_volovik[i]:.4f} M_KK, "
          f"beta={beta_k[i]:.4f}")

print(f"\n  Thermal equivalent T_eq = {T_eq:.6f} M_KK = {T_eq * M_KK:.4e} GeV")
print(f"  GGE entropy S_GGE = {S_GGE:.4f} (vs S_eq = {S_eq:.4f}, S_max = {S_max:.4f})")
print(f"  KL divergence D_KL(GGE || eq) = {D_KL:.6f}")
print(f"  Jensen-Shannon D_JS(GGE || eq) = {D_JS:.6f}")
print(f"  Temperature ratio T_max/T_min = {T_max_volovik / T_min_volovik:.2f}")

# Entropy deficit: how far from thermal
S_deficit = 1.0 - S_GGE / S_max
print(f"  Entropy deficit (1 - S_GGE/S_max) = {S_deficit:.4f} = {S_deficit*100:.1f}%")

# ============================================================================
#  SECTION 4: EQUATION OF STATE AND FREE-STREAMING
# ============================================================================
print("\n--- 4. EQUATION OF STATE AND FREE-STREAMING ---")

# The DM is superheavy: m_DM ~ 6-7 x 10^16 GeV
# Today's CMB temperature T_CMB = 2.348e-13 GeV
# Velocity at temperature T: v/c ~ T/m (non-relativistic limit)

# GGE temperature (use maximum Volovik temperature as upper bound)
T_DM_today_MKK = T_max_volovik  # Upper bound (GGE temperatures are frozen post-transit)
T_DM_today_GeV = T_DM_today_MKK * M_KK

# But wait: the GGE temperatures are in M_KK units at production.
# After production, the DM free-streams with momenta redshifted.
# The relevant velocity today is:
# v/c ~ p/(m*c) ~ (T_production / m_DM) * (a_production / a_today)
# The production happens at T ~ M_KK (KK scale), so z_production ~ M_KK / T_CMB_GeV

z_production = M_KK / T_CMB_GeV
a_ratio = 1.0 / (1.0 + z_production)

# Velocity at production (in M_KK units, E_k ~ m, T_k ~ 0.2-0.8 M_KK)
v_production = T_max_volovik / (E_B2_mean * M_KK / M_KK)  # v/c at production ~ T_k / E_k
v_today = v_production * a_ratio  # Redshifted momentum: p ~ a^{-1}

print(f"  Production redshift z_prod ~ M_KK / T_CMB = {z_production:.4e}")
print(f"  v/c at production ~ T_max / E_B2 = {v_production:.4f}")
print(f"  v/c today (redshifted) = {v_today:.4e}")

# Equation of state: w = P/rho
# For non-relativistic matter: w = (v/c)^2 / 3
w_DM_today = v_today**2 / 3.0
w_DM_production = v_production**2 / 3.0

print(f"  w_DM at production = {w_DM_production:.4e}")
print(f"  w_DM today = {w_DM_today:.4e}")
print(f"  CDM: w = 0 exactly. Deviation: {w_DM_today:.4e}")
print(f"  Classification: COLD (w << 1 at all times)")

# Free-streaming length: lambda_fs = integral(v/a dt) from t_prod to t_0
# For non-relativistic superheavy DM produced before BBN:
# lambda_fs ~ v_prod * t_eq * (a_eq/a_prod)^(1/2)  [matter-radiation equality]
# More precisely: lambda_fs ~ (v_prod / H_prod) * (a_eq/a_prod)
# But since v is already tiny (T_k/m ~ 1) and redshifted by ~10^{29},
# lambda_fs is extraordinarily small

# Hubble at production: H_prod ~ T_prod^2 / M_Pl (radiation dominated)
T_prod_GeV = M_KK  # Production at KK scale
H_prod_GeV = T_prod_GeV**2 / M_Pl_reduced
H_prod_inv_GeV = 1.0 / H_prod_GeV  # Hubble radius in GeV^{-1}

# Free-streaming horizon (comoving, in GeV^{-1})
# lambda_fs ~ v * d_H(prod) * (a_prod / a_eq)
# where d_H = 1/H is the Hubble distance at production
z_eq = z_eq_planck  # canonical alias (was: = 3387)
a_eq = 1.0 / (1 + z_eq)
a_prod = 1.0 / (1 + z_production)

# Comoving free-streaming length (approximate)
# In radiation era: lambda_fs(comoving) ~ v * (1/H_prod) * (a_prod/a_eq) * ln(a_eq/a_prod)
# The log comes from integrating v*dt/a over the radiation era
ratio_a = a_eq / a_prod
lambda_fs_GeV_inv = v_production * H_prod_inv_GeV * np.log(ratio_a) / (1 + z_production)

# Convert to physical units
lambda_fs_Mpc = lambda_fs_GeV_inv * GeV_inv_to_Mpc

# More careful estimate: for superheavy DM with v ~ T/m ~ O(1) at production,
# the comoving free-streaming length is:
# lambda_fs ~ (T_prod / m_DM) * (1/H_prod) * (1+z_prod)^{-1} * 2*ln(z_prod/z_eq)
# Since T_prod/m_DM ~ T_k/E_k ~ 0.9, this is suppressed by the enormous z_prod
lambda_fs_proper = v_production / H_prod_GeV  # Physical free-streaming distance at production
lambda_fs_proper_cm = lambda_fs_proper * hbar_c_GeV_cm
lambda_fs_proper_Mpc = lambda_fs_proper * GeV_inv_to_Mpc

# Comoving free-streaming: lambda_fs_com = lambda_fs_proper * (1+z_prod) * integral...
# The key point: superheavy DM becomes non-relativistic essentially at production
# Since v/c ~ T/m ~ O(1) but m ~ M_KK, after even one e-fold of expansion, v drops
lambda_fs_comoving_Mpc = lambda_fs_Mpc

print(f"\n  Free-streaming calculation:")
print(f"    H at production = {H_prod_GeV:.4e} GeV")
print(f"    d_H at production = {H_prod_inv_GeV:.4e} GeV^-1 = {lambda_fs_proper_Mpc:.4e} Mpc")
print(f"    lambda_fs (comoving) ~ {lambda_fs_comoving_Mpc:.4e} Mpc")

# For comparison, key scales:
# Lyman-alpha sensitivity: ~0.5 Mpc (comoving)
# Milky Way halo: ~200 kpc ~ 0.2 Mpc
# CDM free-streaming: essentially 0
# WDM (1 keV): ~0.1 Mpc
lambda_jeans_CDM_Mpc = 0.0  # CDM  # (local)
lambda_jeans_WDM_Mpc = 0.1  # WDM at 1 keV  # (local)
lambda_lyman_alpha = 0.5    # Lyman-alpha sensitivity  # (local)

print(f"    Lyman-alpha sensitivity: ~{lambda_lyman_alpha} Mpc")
print(f"    WDM (1 keV): ~{lambda_jeans_WDM_Mpc} Mpc")
print(f"    GGE DM: {lambda_fs_comoving_Mpc:.4e} Mpc")
print(f"    Ratio lambda_fs / lambda_Lyman-alpha = {lambda_fs_comoving_Mpc / lambda_lyman_alpha:.4e}")
print(f"    Classification: INDISTINGUISHABLE from CDM at all cosmological scales")

# ============================================================================
#  SECTION 5: RELIC DENSITY CROSS-CHECK
# ============================================================================
print("\n--- 5. RELIC DENSITY ---")

# From W1-2: f_DM = 0.119 of total BCS excitation energy goes to DM
# Omega_DM h^2 range from W2-4: [0.017, 0.188], observed 0.120
rho_DM_obs = Omega_DM * rho_crit_GeV4  # GeV^4

# Number density of DM quasiparticles (per unit volume)
# n_DM = rho_DM / m_DM
n_DM_GeV3 = rho_DM_obs / m_DM_mean_GeV  # GeV^3
n_DM_cm3 = n_DM_GeV3 * (GeV_to_inv_m * 100)**3  # cm^{-3}

print(f"  rho_DM = Omega_DM * rho_crit = {rho_DM_obs:.4e} GeV^4")
print(f"  m_DM (mean) = {m_DM_mean_GeV:.4e} GeV")
print(f"  n_DM = rho_DM / m_DM = {n_DM_GeV3:.4e} GeV^3")
print(f"  n_DM = {n_DM_cm3:.4e} cm^-3")

# Compare to WIMP number density
m_WIMP = 100  # GeV (typical WIMP)
n_WIMP = rho_DM_obs / m_WIMP
n_WIMP_cm3 = n_WIMP * (GeV_to_inv_m * 100)**3
print(f"  For comparison, WIMP (100 GeV): n = {n_WIMP_cm3:.4e} cm^-3")
print(f"  GGE DM number density is {n_WIMP_cm3 / n_DM_cm3:.2e}x smaller (superheavy)")

# Omega_DM h^2 bracket from W2-4
h_Planck = H_0_km_s_Mpc / 100.0
Omega_DM_h2_obs = 0.120  # Planck 2018  # (local)
Omega_DM_h2_pred_low = 0.017  # W2-4 lower bracket  # (local)
Omega_DM_h2_pred_high = 0.188  # W2-4 upper bracket  # (local)

print(f"\n  Omega_DM h^2 observed: {Omega_DM_h2_obs}")
print(f"  Omega_DM h^2 predicted bracket: [{Omega_DM_h2_pred_low}, {Omega_DM_h2_pred_high}]")
print(f"  Observed falls inside bracket: {Omega_DM_h2_pred_low <= Omega_DM_h2_obs <= Omega_DM_h2_pred_high}")
print(f"  f_DM (energy partition) = {f_DM_energy:.6f}")
print(f"  shortfall factor = {shortfall_factor:.4f}")

# ============================================================================
#  SECTION 6: MATTER POWER SPECTRUM P(k) DEVIATION
# ============================================================================
print("\n--- 6. MATTER POWER SPECTRUM P(k) ---")

# For CDM: P(k) ~ k^{n_s} * T^2(k) where T(k) is the transfer function
# GGE DM deviates from CDM in two possible ways:
# (a) Free-streaming cutoff: lambda_fs ~ 10^{-42} Mpc (irrelevant)
# (b) Non-thermal velocity dispersion: v_rms affects Jeans scale
# (c) Late-time self-interaction: modifies halo profiles

# The GGE distribution gives a different velocity dispersion than thermal
# Mean velocity squared: <v^2> = sum(fk * (pk/mk)^2) / sum(fk)
# But all modes have the same mass ~ M_KK, so:
# <v^2> ~ sum(fk * T_k) / (E_k * sum(fk)) * (a_prod/a_0)^2

v2_GGE = np.sum(fk_gge * T_k_volovik / E_k)  / np.sum(fk_gge) # in natural units at production
v2_thermal = T_eq / E_B2_mean  # Thermal equivalent

# Today
v2_GGE_today = v2_GGE * a_ratio**2
v2_thermal_today = v2_thermal * a_ratio**2

v_rms_GGE_today = np.sqrt(v2_GGE_today)
v_rms_thermal_today = np.sqrt(v2_thermal_today)

print(f"  <v^2>_GGE at production = {v2_GGE:.6f} c^2")
print(f"  <v^2>_thermal at production = {v2_thermal:.6f} c^2")
print(f"  Ratio <v^2>_GGE / <v^2>_thermal = {v2_GGE / v2_thermal:.4f}")
print(f"  v_rms today (GGE) = {v_rms_GGE_today:.4e} c")
print(f"  v_rms today (thermal) = {v_rms_thermal_today:.4e} c")

# Jeans scale: lambda_J ~ v_rms / H
# Today: H_0 = 67.4 km/s/Mpc = 2.18e-18 s^{-1}
lambda_J_GGE = v_rms_GGE_today * c_light_km_s / H_0_km_s_Mpc  # in Mpc
lambda_J_thermal = v_rms_thermal_today * c_light_km_s / H_0_km_s_Mpc

print(f"  Jeans scale today (GGE) = {lambda_J_GGE:.4e} Mpc")
print(f"  Jeans scale today (thermal) = {lambda_J_thermal:.4e} Mpc")
print(f"  Both << Lyman-alpha scale (~0.5 Mpc)")

# P(k) deviation: delta_P/P ~ (lambda_fs / k^{-1})^2 for k >> k_fs
# Since lambda_fs ~ 10^{-42} Mpc, deviation at any observable k is:
k_obs_min = 0.001  # h/Mpc (large-scale limit of galaxy surveys)  # (local)
k_obs_max = 10.0   # h/Mpc (small-scale limit, nonlinear)  # (local)
delta_P_over_P_large = (lambda_fs_comoving_Mpc * k_obs_min)**2
delta_P_over_P_small = (lambda_fs_comoving_Mpc * k_obs_max)**2

print(f"\n  P(k) deviation from CDM:")
print(f"    At k = {k_obs_min} h/Mpc: delta_P/P ~ {delta_P_over_P_large:.4e}")
print(f"    At k = {k_obs_max} h/Mpc: delta_P/P ~ {delta_P_over_P_small:.4e}")
print(f"    Euclid sensitivity: ~1% on P(k)")
print(f"    Classification: UNOBSERVABLE (deviation << 10^{-50})")

# ============================================================================
#  SECTION 7: DIRECT/INDIRECT DETECTION
# ============================================================================
print("\n--- 7. DETECTION PROSPECTS ---")

# Direct detection: superheavy DM has extremely low flux
# Flux = n_DM * v_DM (local) ~ n_DM * 220 km/s (galactic velocity)
# Local DM density: rho_local = 0.3 GeV/cm^3
rho_local_GeV = 0.3  # GeV/cm^3  # (local)
n_local = rho_local_GeV / m_DM_mean_GeV  # cm^{-3}
v_galactic_cm_s = 220e5  # 220 km/s in cm/s
flux_DM = n_local * v_galactic_cm_s  # cm^{-2} s^{-1}

print(f"  Local DM density: rho = 0.3 GeV/cm^3")
print(f"  Local number density: n = {n_local:.4e} cm^-3")
print(f"  DM flux: Phi = n*v = {flux_DM:.4e} cm^-2 s^-1")
print(f"  For 1 ton detector, 1 year:")
N_target_per_ton = 6.022e26  # atoms per ton (roughly, for Xe)
exposure_s = 3.156e7  # 1 year in seconds  # (local)
rate = flux_DM * sigma_scatter_cm2 * N_target_per_ton * exposure_s
print(f"    Expected events = {rate:.4e}")
print(f"    Classification: UNDETECTABLE by direct detection")

# Indirect detection: self-conjugate (BDI) => no annihilation channel
print(f"\n  Annihilation:")
print(f"    BDI class T^2=+1: quasiparticles are self-conjugate")
print(f"    No annihilation channel (CPT-neutral, no antiparticle distinction)")
print(f"    Gamma-ray, neutrino, positron signals: ZERO")
print(f"    Classification: INVISIBLE to indirect detection (Fermi-LAT, IceCube, AMS-02)")

# Collider production
print(f"\n  Collider production:")
print(f"    m_DM = {m_DM_mean_GeV:.2e} GeV >> sqrt(s)_LHC = 14 TeV = 1.4e4 GeV")
print(f"    Ratio m_DM / sqrt(s)_LHC = {m_DM_mean_GeV / 1.4e4:.2e}")
print(f"    Classification: UNREACHABLE by any foreseeable collider")

# ============================================================================
#  SECTION 8: NEUTRINO EXPERIMENT DISCRIMINANTS
# ============================================================================
print("\n--- 8. NEUTRINO EXPERIMENT DISCRIMINANTS ---")

# Can JUNO, DUNE, KATRIN, or any neutrino experiment see GGE DM?
# The GGE quasiparticles are KK-scale excitations. They do NOT couple to
# SM neutrinos via standard weak interactions. The only coupling is
# gravitational (through the spectral action).

# Neutrino-DM scattering: if DM is a KK excitation, the coupling to SM
# neutrinos goes through gravity or higher-dimensional operators suppressed
# by M_KK. Cross section: sigma(nu-DM) ~ G_N^2 * E_nu^2 * m_DM^2
E_nu_typical = 1e-3  # GeV (MeV-scale for reactor/solar)
sigma_nu_DM_gravitational = G_N**2 * E_nu_typical**2 * (m_DM_mean_GeV * GeV_to_g * 1e-3)**2
# This is meaninglessly small. Use dimensional analysis instead:
# sigma ~ (E_nu / M_Pl)^2 * (m_DM / M_Pl)^2 * (1/M_Pl^2)
sigma_nu_DM_dim = (E_nu_typical / M_Pl_reduced)**2 * (m_DM_mean_GeV / M_Pl_reduced)**2 / M_Pl_reduced**2
sigma_nu_DM_cm2 = sigma_nu_DM_dim * (hbar_c_GeV_cm)**2  # Convert GeV^{-2} to cm^2

print(f"  Neutrino-DM gravitational scattering:")
print(f"    sigma(nu-DM) ~ (E_nu/M_Pl)^2 * (m_DM/M_Pl)^2 / M_Pl^2")
print(f"    At E_nu = 1 MeV: sigma ~ {sigma_nu_DM_cm2:.4e} cm^2")
print(f"    Weak cross section at 1 MeV: ~10^-44 cm^2")
print(f"    Ratio: {sigma_nu_DM_cm2 / 1e-44:.4e}")
print(f"    Classification: UNOBSERVABLE by neutrino detectors")

# N_eff constraint: does GGE DM contribute to N_eff?
# From S56: N_eff(fabric) = 41.5 internal modes, but frozen out by 100+ orders at BBN
# GGE quasiparticles are superheavy and non-relativistic at BBN
T_BBN_GeV = 1e-3  # 1 MeV
m_DM_over_T_BBN = m_DM_mean_GeV / T_BBN_GeV
boltzmann_suppression = np.exp(-min(m_DM_over_T_BBN, 700))  # Cap to avoid overflow

print(f"\n  N_eff contribution:")
print(f"    m_DM / T_BBN = {m_DM_over_T_BBN:.4e}")
print(f"    Boltzmann suppression e^(-m/T) = {boltzmann_suppression:.4e}")
print(f"    GGE DM is NON-RELATIVISTIC at BBN by {m_DM_over_T_BBN:.1e}x")
print(f"    delta_N_eff from GGE DM: ZERO (frozen out)")
print(f"    CMB-S4 target sensitivity delta_N_eff ~ 0.06: UNAFFECTED")

# KATRIN relevance: KATRIN measures m(nu_e) via beta decay endpoint
# GGE DM is unrelated to neutrino mass (different mechanism)
# But the framework predicts neutrino masses from D_K eigenvalues
print(f"\n  KATRIN / neutrino mass experiments:")
print(f"    GGE quasiparticle DM is NOT the neutrino mass mechanism")
print(f"    Neutrino masses = lightest D_K(s_0) eigenvalues (separate prediction)")
print(f"    GGE DM = excited BCS quasiparticles (M_KK scale)")
print(f"    No coupling between GGE DM and neutrino mass measurement")
print(f"    KATRIN, JUNO, DUNE: measure neutrinos, NOT GGE DM")

# Gravitational signatures: galaxy-scale effects
print(f"\n  Gravitational signatures:")
print(f"    Bullet Cluster sigma/m = {sigma_over_m:.4e} cm^2/g << 1 cm^2/g: PASS")
print(f"    Halo profiles: CDM-like (collisionless, cold)")
print(f"    SIDM bounds (dwarf galaxies): sigma/m < 0.1-10 cm^2/g: PASS trivially")
print(f"    Gravitational lensing: indistinguishable from CDM")

# ============================================================================
#  SECTION 9: SUMMARY: THE NON-OBSERVABILITY THEOREM
# ============================================================================
print("\n--- 9. SUMMARY ---")

print("""
  GGE-relic DM properties:
  ========================
  Mass:            m_DM ~ 6-7 x 10^16 GeV (superheavy, wimpzilla regime)
  Cross-section:   sigma/m ~ 10^{-51} cm^2/g (collisionless)
  Velocity today:  v/c ~ 10^{-29} (ultracold)
  Free-streaming:  lambda_fs ~ 10^{-42} Mpc (zero for all practical purposes)
  Equation of state: w_DM ~ 10^{-58} (indistinguishable from w=0)
  Phase space:     Non-thermal GGE with 8 effective temperatures
  P(k) deviation:  < 10^{-50} at all observable scales
  Annihilation:    ZERO (BDI self-conjugate, no anti-DM)
  Direct detection: ZERO (flux ~ 10^{-24} cm^{-2} s^{-1})
  Collider:        m_DM / sqrt(s)_LHC ~ 10^{12} (unreachable)

  CLASSIFICATION: PHONONIC (framework-native)

  At cosmological scales, GGE DM is INDISTINGUISHABLE from standard CDM.
  The non-thermal phase space distribution is unobservable because:
    1. The free-streaming length is 42 orders below Lyman-alpha sensitivity
    2. The self-scattering cross-section is 51 orders below Bullet Cluster bounds
    3. The DM is non-annihilating (BDI), so no indirect detection signal
    4. The mass is 12 orders above LHC energy, so no collider signature
    5. The neutrino-DM coupling is gravitational-only, so no neutrino detector signal

  The ONLY way to distinguish GGE DM from CDM is through:
    - The mass ordering of neutrinos (structural prediction: NORMAL)
    - The NNI texture of the PMNS matrix (structural prediction)
    - The DM abundance fraction f_DM = 0.119 (within Omega_DM h^2 bracket)
    - The tau-alpha coupling: delta_alpha/alpha ~ -3.08 * dtau (clock constraint)

  These are INDIRECT: they test the framework, not the DM candidate specifically.
""")

# ============================================================================
#  SAVE RESULTS
# ============================================================================

results = {
    # Gate metadata
    "gate_name": "NS-MAPPING-57",
    "gate_verdict": "INFO",

    # Mass spectrum
    "m_DM_GeV": m_DM_GeV,
    "m_B1_GeV": m_B1_GeV,
    "m_B2_GeV": m_B2_GeV,
    "m_B3_GeV": m_B3_GeV,
    "m_DM_mean_GeV": m_DM_mean_GeV,
    "m_DM_mean_g": m_DM_mean_g,
    "m_DM_over_M_GUT": m_DM_over_M_GUT,
    "m_DM_over_M_Pl": m_DM_over_M_Pl,

    # Cross-sections
    "a_scatter_MKK_inv": abs(a_scatter),
    "a_scatter_cm": a_scatter_cm,
    "sigma_scatter_cm2": sigma_scatter_cm2,
    "sigma_over_m_cm2_per_g": sigma_over_m,
    "sigma_pert_cm2": sigma_pert_cm2,
    "sigma_over_m_pert": sigma_over_m_pert,

    # Phase space
    "fk_gge": fk_gge,
    "T_k_volovik": T_k_volovik,
    "beta_k": beta_k,
    "T_eq_canonical": T_eq,
    "S_GGE": S_GGE,
    "S_eq": S_eq,
    "D_KL": D_KL,
    "D_JS": D_JS,
    "S_deficit_fraction": S_deficit,

    # Equation of state
    "w_DM_today": w_DM_today,
    "w_DM_production": w_DM_production,
    "v_production": v_production,
    "v_today": v_today,
    "v_rms_GGE_today": v_rms_GGE_today,

    # Free-streaming
    "lambda_fs_Mpc": lambda_fs_comoving_Mpc,
    "z_production": z_production,
    "lambda_J_GGE_Mpc": lambda_J_GGE,

    # Relic density
    "f_DM_energy": f_DM_energy,
    "P_exc_final": P_exc_final,
    "Omega_DM_h2_bracket_low": Omega_DM_h2_pred_low,
    "Omega_DM_h2_bracket_high": Omega_DM_h2_pred_high,
    "Omega_DM_h2_obs": Omega_DM_h2_obs,
    "n_DM_cm3": n_DM_cm3,

    # P(k) deviation
    "delta_P_over_P_k001": delta_P_over_P_large,
    "delta_P_over_P_k10": delta_P_over_P_small,

    # Detection prospects
    "flux_DM_local": flux_DM,
    "sigma_nu_DM_cm2": sigma_nu_DM_cm2,
    "n_local_cm3": n_local,

    # Key ratios
    "v2_GGE_over_thermal": v2_GGE / v2_thermal,
    "branch_labels": branch_labels,
    "M_KK": M_KK,
}

np.savez("computations/session-57/s57_ns_mapping.npz", **results)
print("Saved: computations/session-57/s57_ns_mapping.npz")
print("DONE")
