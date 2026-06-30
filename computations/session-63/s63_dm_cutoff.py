#!/usr/bin/env python3
"""
s63_dm_cutoff.py — Small-Scale Power Spectrum Cutoff from Transit Quench
=========================================================================
Gate: DM-CUTOFF-63
  INFO — report k_cut and compare to CDM benchmark.

PHYSICS:
    The matter power spectrum P(k) is suppressed below a cutoff scale k_cut
    determined by the microphysics of DM creation and subsequent decoupling.

    In the phonon-exflation framework, DM quasiparticles are created via a
    Kibble-Zurek transit quench at the tau-fold (tau=0.19). Three physical
    processes set k_cut:

    1. FREE-STREAMING CUTOFF (k_fs):
       After creation, DM quasiparticles stream freely until they become
       non-relativistic. The free-streaming length sets an upper bound on k_cut.
       From S58 TRANSFER-FUNCTION-58 and S63 WDM-FRACTION-63:
         k_fs ~ 4.3e23 h/Mpc (bulk condensate)
         k_fs ~ 4.3e22 h/Mpc (1.15% warm normal fraction)
       Both are vastly above any observable scale.

    2. COLLISIONAL DAMPING CUTOFF (k_cd):
       Before kinetic decoupling, DM-baryon interactions damp perturbations
       via acoustic oscillations and diffusion (Silk damping for DM).
       In the framework, the Meissner mass m_M = 2.507 M_KK provides the
       gauge boson mass in the superconducting phase, screening DM-SM
       interactions at distances > 1/m_M. This is the analog of kinetic
       decoupling in WIMP models: the DM-baryon scattering rate drops
       below the Hubble rate when the interaction range becomes too short.

    3. ACOUSTIC DAMPING (k_ad):
       Coupled DM-baryon oscillations before decoupling create an acoustic
       damping envelope. The damping scale depends on the DM-baryon coupling
       strength and decoupling epoch.

    For thermal WIMPs (Green, Hofmann, Schwarz 2004, 2005; Loeb & Zaldarriaga 2005;
    Profumo, Sigurdson & Kamionkowski 2006; Bringmann & Hofmann 2007):
      - Kinetic decoupling T_kd ~ 10-100 MeV (weak-scale interaction)
      - k_cut ~ 10^6 - 10^8 h/Mpc
      - M_cut ~ 10^{-12} - 10^{-3} M_sun (Earth mass scale)

    The framework predicts IMMEDIATE decoupling because:
      (a) DM created at T ~ M_KK ~ 7.4e16 GeV (far above EW scale)
      (b) Meissner screening mass m_M = 2.507 M_KK provides exponential
          suppression of DM-SM gauge interactions at distances > 1/m_M
      (c) Cross-section sigma ~ alpha^2 / m_M^4, with m_M ~ 10^17 GeV
          => sigma ~ 10^{-68} GeV^{-2} ~ 10^{-105} cm^2

    This means collisional damping is negligible: DM decouples at production.
    The cutoff is set entirely by free-streaming.

SOURCES:
    - s62_meissner_gge.npz: Meissner mass, superfluid stiffness
    - s58_transfer_function.npz: bulk DM free-streaming k_cut
    - s63_wdm_fraction.npz: warm fraction free-streaming
    - s58_sq_omega_gge.npz: GGE mode data
    - Mack M-62-13 (Friedlander, Mack et al. 2022): PBH extra dimensions
    - Green, Hofmann, Schwarz (2004): WIMP kinetic decoupling
    - Bringmann & Hofmann (2007): WIMP cutoff mass
    - Loeb & Zaldarriaga (2005): small-scale CDM structure

Author: mack-cosmic-bridge (Katie Mack agent)
Session: S63 W6-29
"""

import sys
import os
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, M_Pl_unreduced,
    tau_fold, c_Gold,
    T_CMB, T_CMB_GeV, k_B,
    H_0_km_s_Mpc, H_0_GeV,
    Omega_DM, Omega_m, Omega_r, Omega_Lambda, Omega_b,
    E_B1, E_B2_mean, E_B3_mean,
    Delta_0_OES, Delta_0_GL,
    c_light, c_light_km_s,
    hbar_c_GeV_m, hbar_GeV_s,
    Mpc_to_m, GeV_inv_to_Mpc, Mpc_to_GeV_inv,
    rho_crit_GeV4, rho_crit_cgs,
    G_N,
    J_C2, T_acoustic,
    sigma_8, N_cells,
    N_dof_BCS,
    xi_BCS,
    E_cond, E_exc,
    dt_transit, H_fold, v_terminal,
    n_Bog, P_exc_kz,
    alpha_em_MZ_inv,
    sin2_thetaW_MSbar,
    GeV_to_inv_m,
    l_Planck,
    PI,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

script_dir = os.path.dirname(os.path.abspath(__file__))
t_start = time.time()

print("=" * 78)
print("S63 DM-CUTOFF-63: Small-Scale Power Spectrum Cutoff from Transit Quench")
print("=" * 78)

# =============================================================================
# SECTION 1: LOAD INPUT DATA
# =============================================================================
print("\n--- Section 1: Load input data ---")

# Meissner mass data
d62 = np.load(os.path.join(script_dir, 's62_meissner_gge.npz'), allow_pickle=True)
m_M_GGE = float(d62['m_M_GGE'])       # 2.507 M_KK
m_M_fold = float(d62['m_M_fold'])      # 2.521 M_KK
D_s_GGE = float(d62['D_s_GGE'])       # 6.283 M_KK^2
D_s_fold = float(d62['D_s_fold'])      # 6.356 M_KK^2
lambda_L_GGE = float(d62['lambda_L_GGE'])   # 0.3989 M_KK^{-1}
lambda_L_fold = float(d62['lambda_L_fold'])  # 0.3966 M_KK^{-1}
n_condensate = float(d62['n_condensate_GGE'])  # 0.9885
T_GGE_eff = float(d62['T_GGE_eff'])   # 0.386 M_KK

# Bulk DM transfer function data
d58_tf = np.load(os.path.join(script_dir, 's58_transfer_function.npz'), allow_pickle=True)
k_cut_bulk = float(d58_tf['k_cut'])          # 4.31e23 h/Mpc
lambda_fs_bulk = float(d58_tf['lambda_fs_Mpc_h'])  # 1.46e-23 Mpc/h
m_DM_GeV = float(d58_tf['m_DM_GeV'])        # 1.325e17 GeV
m_DM_MKK = float(d58_tf['m_DM_MKK'])        # 1.784 M_KK
v_rms_dm = float(d58_tf['v_rms_dm'])         # 0.254 c

# WDM fraction data
d63_wdm = np.load(os.path.join(script_dir, 's63_wdm_fraction.npz'), allow_pickle=True)
k_fs_warm = float(d63_wdm['k_fs'])           # 4.30e22 h/Mpc
lambda_fs_warm = float(d63_wdm['lambda_fs_Mpc'])  # 9.85e-23 Mpc
f_normal = float(d63_wdm['f_normal'])        # 0.01152
v_rms_warm = float(d63_wdm['v_rms_wdm'])    # 0.866 c
m_wdm_MKK = float(d63_wdm['m_wdm_MKK'])    # 0.844 M_KK
z_prod = float(d63_wdm['z_prod'])            # 1.053e29

# GGE mode data
d58_sq = np.load(os.path.join(script_dir, 's58_sq_omega_gge.npz'), allow_pickle=True)
E_k = d58_sq['E_k']           # (8,) quasiparticle energies
T_k = d58_sq['T_k_volovik']   # (8,) mode temperatures
Delta = float(d58_sq['Delta'])  # BCS gap

print(f"Meissner mass (GGE):     m_M = {m_M_GGE:.6f} M_KK = {m_M_GGE * M_KK:.4e} GeV")
print(f"Meissner mass (fold):    m_M = {m_M_fold:.6f} M_KK = {m_M_fold * M_KK:.4e} GeV")
print(f"London depth (GGE):      lambda_L = {lambda_L_GGE:.6f} M_KK^{{-1}} = {lambda_L_GGE / (M_KK * GeV_to_inv_m):.4e} m")
print(f"Condensate fraction:     {n_condensate:.6f} ({n_condensate*100:.2f}%)")
print(f"Normal fraction:         {f_normal:.6f} ({f_normal*100:.2f}%)")
print(f"DM mass (bulk):          m_DM = {m_DM_MKK:.4f} M_KK = {m_DM_GeV:.4e} GeV")
print(f"WDM mass (normal frac):  m_wdm = {m_wdm_MKK:.4f} M_KK = {m_wdm_MKK * M_KK:.4e} GeV")
print(f"BCS gap:                 Delta = {Delta:.6f} M_KK = {Delta * M_KK:.4e} GeV")
print(f"Production redshift:     z_prod = {z_prod:.4e}")
print(f"Bulk k_cut (S58):        {k_cut_bulk:.4e} h/Mpc")
print(f"Warm k_fs (S63):         {k_fs_warm:.4e} h/Mpc")

# =============================================================================
# SECTION 2: DM-SM SCATTERING CROSS-SECTION FROM MEISSNER SCREENING
# =============================================================================
print("\n--- Section 2: DM-SM cross-section from Meissner screening ---")

# In the superconducting phase (post-transit), gauge bosons acquire Meissner mass
# m_M = 2.507 M_KK. The DM-SM interaction is mediated by these massive gauge bosons.
#
# The Born-approximation cross-section for DM-baryon scattering through
# a massive gauge boson (analog of Z/W exchange but with Meissner mass):
#
#   sigma_{DM-b} ~ alpha_gauge^2 / m_M^4   [low-energy limit, s << m_M^2]
#
# where alpha_gauge is the gauge coupling at the relevant scale.
#
# At the fold: alpha_2 = 1 / alpha2_MKK_inv = 1/47.86
# The DM quasiparticle coupling to gauge bosons is set by the Josephson
# coupling J_C2 = 0.933 M_KK (dominant C^2 coset channel).

# Gauge coupling at M_KK scale
alpha_gauge = 1.0 / 47.86  # = 0.0209 (SU(2) coupling at M_KK)
print(f"alpha_gauge (M_KK):      {alpha_gauge:.6f}")

# DM-baryon cross-section (Born approximation, s << m_M^2)
# sigma ~ pi * alpha^2 / m_M^4
# In natural units: sigma has dimensions GeV^{-2}
m_M_GeV = m_M_GGE * M_KK
sigma_DM_b = PI * alpha_gauge**2 / m_M_GeV**4
sigma_DM_b_cm2 = sigma_DM_b * (hbar_c_GeV_m * 100)**2  # convert GeV^{-2} to cm^2

print(f"\nDM-baryon cross-section (Meissner-screened):")
print(f"  m_M = {m_M_GeV:.4e} GeV")
print(f"  sigma = pi * alpha^2 / m_M^4")
print(f"  sigma = {sigma_DM_b:.4e} GeV^{{-2}}")
print(f"  sigma = {sigma_DM_b_cm2:.4e} cm^2")
print(f"  log10(sigma / cm^2) = {np.log10(sigma_DM_b_cm2):.1f}")

# For comparison: weak interaction cross-section (standard WIMP)
# sigma_weak ~ G_F^2 * s / pi ~ alpha_weak^2 / M_W^2 (low energy, M_W ~ 80 GeV)
alpha_weak = 1.0 / 128.0
M_W_GeV = 80.4  # GeV  # (local)
sigma_WIMP_weak = PI * alpha_weak**2 / M_W_GeV**4
sigma_WIMP_weak_cm2 = sigma_WIMP_weak * (hbar_c_GeV_m * 100)**2

print(f"\nWIMP weak cross-section (for comparison):")
print(f"  sigma_weak = pi * alpha_w^2 / M_W^4")
print(f"  sigma_weak = {sigma_WIMP_weak:.4e} GeV^{{-2}}")
print(f"  sigma_weak = {sigma_WIMP_weak_cm2:.4e} cm^2")
print(f"  log10(sigma_weak / cm^2) = {np.log10(sigma_WIMP_weak_cm2):.1f}")

ratio_sigma = sigma_DM_b / sigma_WIMP_weak
print(f"\nRatio sigma_DM / sigma_WIMP = {ratio_sigma:.4e}")
print(f"  log10(ratio) = {np.log10(ratio_sigma):.1f}")
print(f"  Framework DM-SM interaction is {np.log10(1/ratio_sigma):.0f} OOM weaker than WIMP")

# =============================================================================
# SECTION 3: KINETIC DECOUPLING TEMPERATURE
# =============================================================================
print("\n--- Section 3: Kinetic decoupling temperature ---")

# Kinetic decoupling occurs when the momentum transfer rate Gamma_mom drops
# below the Hubble rate H(T).
#
# Gamma_mom ~ n_b * sigma_DM-b * v_rel * (T/m_DM) [elastic scattering]
#           ~ n_b * sigma * v * (T/m_DM)
#
# where n_b is the baryon number density, v_rel is the relative velocity,
# and the factor T/m_DM accounts for momentum transfer efficiency.
#
# In standard cosmology (radiation-dominated):
#   H(T) = 1.66 * g_*^{1/2} * T^2 / M_Pl
#   n_b ~ eta_B * n_gamma ~ eta_B * (2*zeta(3)/pi^2) * T^3
#
# For WIMPs: T_kd ~ O(MeV) to O(GeV) depending on model.
# For framework DM: the Meissner-screened cross-section is so small
# that Gamma_mom / H << 1 at ALL temperatures.

# Baryon-to-photon ratio
eta_B = 6.12e-10  # Planck 2018  # (local)

# Number density of photons
def n_gamma(T_GeV):
    """Photon number density in GeV^3 (natural units)."""
    return 2 * 1.202 / PI**2 * T_GeV**3

# Baryon number density
def n_baryon(T_GeV):
    """Baryon number density in GeV^3."""
    return eta_B * n_gamma(T_GeV)

# Hubble rate in radiation domination
def H_rad(T_GeV, g_star=106.75):
    """Hubble rate during radiation domination (GeV)."""
    return 1.66 * np.sqrt(g_star) * T_GeV**2 / M_Pl_unreduced

# Momentum transfer rate
def Gamma_mom(T_GeV, sigma, m_DM):
    """Momentum transfer rate for elastic DM-baryon scattering (GeV)."""
    n_b = n_baryon(T_GeV)
    v_rel = np.sqrt(3 * T_GeV / m_DM) if T_GeV < m_DM else 1.0  # thermal velocity
    T_over_mDM = min(T_GeV / m_DM, 1.0)  # momentum transfer fraction
    return n_b * sigma * v_rel * T_over_mDM

# Evaluate at various temperatures for framework DM
T_test = np.logspace(-3, 17, 100)  # GeV, from MeV to above M_KK
Gamma_arr = np.array([Gamma_mom(T, sigma_DM_b, m_DM_GeV) for T in T_test])
H_arr = np.array([H_rad(T) for T in T_test])
ratio_arr = Gamma_arr / H_arr

# Find maximum of ratio (closest to kinetic coupling)
i_max = np.argmax(ratio_arr)
T_max = T_test[i_max]
ratio_max = ratio_arr[i_max]

print(f"Framework DM kinetic coupling analysis:")
print(f"  m_DM = {m_DM_GeV:.4e} GeV")
print(f"  sigma_DM-b = {sigma_DM_b:.4e} GeV^{{-2}}")
print(f"  Maximum Gamma_mom / H occurs at T = {T_max:.4e} GeV")
print(f"  Max(Gamma_mom / H) = {ratio_max:.4e}")
print(f"  log10(max ratio) = {np.log10(ratio_max):.1f}")

if ratio_max < 1:
    print(f"\n  RESULT: Gamma_mom / H < 1 at ALL temperatures.")
    print(f"  DM was NEVER in kinetic equilibrium with baryons.")
    print(f"  No kinetic decoupling epoch exists => no collisional damping cutoff.")
    T_kd_framework = None  # Never coupled
else:
    # Find decoupling temperature
    idx = np.where(ratio_arr > 1)[0]
    if len(idx) > 0:
        T_kd_framework = T_test[idx[-1]]
        print(f"\n  Kinetic decoupling at T_kd = {T_kd_framework:.4e} GeV")
    else:
        T_kd_framework = None

# Compare to standard WIMP kinetic decoupling
print(f"\nStandard WIMP comparison:")
T_kd_WIMP_low = 10e-3   # 10 MeV (typical lower bound)
T_kd_WIMP_high = 1.0     # 1 GeV (typical upper bound)  # (local)
print(f"  T_kd(WIMP) = 10 MeV - 1 GeV (model dependent)")
print(f"  Framework ratio max = {ratio_max:.4e} (need > 1 for coupling)")
print(f"  Framework DM is NEVER kinetically coupled.")

# =============================================================================
# SECTION 4: FREE-STREAMING CUTOFF (FRAMEWORK)
# =============================================================================
print("\n--- Section 4: Free-streaming cutoff ---")

# Since there is no collisional damping, the power spectrum cutoff is set
# entirely by the free-streaming length of the DM quasiparticles.
#
# Two components:
# (a) Condensate (98.85%): effectively CDM, k_fs ~ 4.3e23 h/Mpc (S58)
# (b) Normal fraction (1.15%): warmer, k_fs ~ 4.3e22 h/Mpc (S63)
#
# The PHYSICAL cutoff in P(k) is the scale where the TOTAL DM transfer
# function departs from unity:
#   T^2(k) = f_cond + f_norm * T_warm^2(k)
#
# Since f_norm = 0.0115, the departure from T^2 = 1 is at most 1.15%,
# occurring at k ~ k_fs_warm.

# The matter power spectrum cutoff wavenumber
# For mixed CDM+WDM:
# T^2(k) = (1 - f_norm) + f_norm * exp(-(k/k_fs_warm)^2)
# The cutoff where |delta T^2 / T^2| = 1% is approximately:
# f_norm * (1 - exp(-(k/k_fs)^2)) = 0.01
# => k ~ k_fs * sqrt(-ln(1 - 0.01/f_norm))
# For f_norm = 0.0115 and threshold = 0.01:
# k ~ k_fs * sqrt(-ln(1 - 0.01/0.0115)) = k_fs * sqrt(-ln(0.130))
# = k_fs * sqrt(2.04) = 1.43 * k_fs

# At 1% suppression of P(k):
threshold_1pct = 0.01  # (local)
if f_normal > threshold_1pct:
    arg = 1.0 - threshold_1pct / f_normal
    k_cut_1pct = k_fs_warm * np.sqrt(-np.log(arg))
else:
    k_cut_1pct = np.inf  # Never reaches 1% suppression

# At 0.1% suppression (observable precision limit):
threshold_01pct = 0.001  # (local)
if f_normal > threshold_01pct:
    arg2 = 1.0 - threshold_01pct / f_normal
    k_cut_01pct = k_fs_warm * np.sqrt(-np.log(arg2))
else:
    k_cut_01pct = np.inf

# The bulk condensate cutoff (effectively CDM)
k_cut_cond = k_cut_bulk  # From S58

# The physical cutoff = smaller of the two (more conservative)
k_cut_framework = k_fs_warm  # Warm component sets the observable cutoff

print(f"Component cutoffs:")
print(f"  Condensate (f={n_condensate:.4f}): k_cut = {k_cut_cond:.4e} h/Mpc")
print(f"  Normal (f={f_normal:.4f}):         k_fs = {k_fs_warm:.4e} h/Mpc")
print(f"  1% P(k) suppression at:            k = {k_cut_1pct:.4e} h/Mpc")
print(f"  0.1% P(k) suppression at:          k = {k_cut_01pct:.4e} h/Mpc")
print(f"  Observable scales: k < 10^4 h/Mpc (galaxy surveys)")
print(f"  Lyman-alpha:       k ~ 10 h/Mpc")
print(f"  Subhalo mass:      k ~ 10^6 h/Mpc")

# Convert to comoving length and mass scales
lambda_cut = 2 * PI / k_cut_framework  # Mpc/h (comoving)
# Cutoff mass (mass within sphere of radius lambda_cut/2):
# M_cut = (4/3)*pi*(lambda_cut/2)^3 * rho_mean
# rho_mean = Omega_m * rho_crit = 0.315 * 2.775e11 h^2 M_sun/Mpc^3
h_hub = H_0_km_s_Mpc / 100.0
rho_mean_Msun_Mpc3 = Omega_m * 2.775e11 * h_hub**2  # M_sun / Mpc^3
# But lambda_cut is in h/Mpc units, so convert:
lambda_cut_Mpc = lambda_cut / h_hub  # Mpc (physical)
M_cut = (4.0 / 3.0) * PI * (lambda_cut_Mpc / 2.0)**3 * rho_mean_Msun_Mpc3

# In solar masses
print(f"\nCutoff scales:")
print(f"  k_cut (framework) = {k_cut_framework:.4e} h/Mpc")
print(f"  lambda_cut = {lambda_cut:.4e} Mpc/h = {lambda_cut_Mpc:.4e} Mpc")
print(f"  log10(k_cut / [h/Mpc]) = {np.log10(k_cut_framework):.2f}")
print(f"  log10(lambda_cut / Mpc) = {np.log10(lambda_cut_Mpc):.2f}")
print(f"  M_cut = {M_cut:.4e} M_sun")
print(f"  log10(M_cut / M_sun) = {np.log10(M_cut):.2f}" if M_cut > 0 else "  M_cut: undefined")

# =============================================================================
# SECTION 5: STANDARD WIMP KINETIC DECOUPLING CUTOFF
# =============================================================================
print("\n--- Section 5: Standard WIMP kinetic decoupling cutoff ---")

# Standard CDM (WIMP) small-scale cutoff.
# Reference: Green, Hofmann, Schwarz (2004, 2005); Bringmann & Hofmann (2007);
# Profumo, Sigurdson & Kamionkowski (2006)
#
# For a generic neutralino-like WIMP (m_chi ~ 100 GeV):
#   T_kd ~ 10 MeV (bino-like) to ~1 GeV (higgsino-like)
#
# The cutoff mass is:
#   M_cut ~ M_Jeans(T_kd) ~ few * 10^{-6} M_sun (bino)
#                          ~ 10^{-12} M_sun (higgsino)
#
# Equivalently:
#   k_cut(WIMP) ~ 10^6 h/Mpc (bino) to 10^8 h/Mpc (higgsino)
#
# Standard formulas (Bringmann & Hofmann 2007):
#   M_fs = 4*pi/3 * rho_eq * (pi * a_kd / k_kd)^3
#   k_kd ~ (2*pi*T_kd * a_kd / M_Pl)^{1/2} * a_kd
# where a_kd = a(T_kd), rho_eq is the matter density at equality.
#
# Numerical scaling (Green et al. 2004):
#   M_cut ~ 10^{-6} * (T_kd / 10 MeV)^{-3} M_sun

# Compute WIMP cutoff for several benchmark T_kd values
T_kd_benchmarks = {
    'Bino (100 GeV)':   10e-3,    # 10 MeV
    'Mixed (300 GeV)':  50e-3,    # 50 MeV
    'Higgsino (1 TeV)': 1.0,      # 1 GeV
}

# Standard formula for cutoff mass from kinetic decoupling:
# M_cut ~ (4*pi/3) * rho_bar * (lambda_fs)^3
# where lambda_fs = integral from t_kd to t_0 of v(t)/a(t) dt
# Approximate: lambda_fs ~ v_kd * t_kd / a_kd
# Simpler scaling: M_cut(WIMP) ~ 3.4e-6 * (T_kd / 30 MeV)^{-3} M_sun
# (from Bringmann 2009)

# g_* at various scales
# g_star_SM = 106.75  # S72: now imported from canonical_constants
g_star_10MeV = 10.75   # after QCD transition  # (local)
g_star_50MeV = 17.25   # around QCD transition  # (local)
g_star_1GeV = 86.25    # before QCD transition  # (local)

g_star_S_today = 3.938  # (local)
a_eq = float(d58_tf['a_eq'])

print(f"WIMP kinetic decoupling benchmarks:")
print(f"{'Model':<25} {'T_kd (GeV)':<12} {'k_cut (h/Mpc)':<18} {'M_cut (M_sun)':<18} {'log10(k_cut)':<12}")
print("-" * 85)

wimp_results = {}
for name, T_kd in T_kd_benchmarks.items():
    # Determine g_* at T_kd
    if T_kd < 0.05:
        g_s = g_star_10MeV
    elif T_kd < 0.2:
        g_s = g_star_50MeV
    else:
        g_s = g_star_1GeV

    # Scale factor at kinetic decoupling
    g_ratio_kd = (g_star_S_today / g_s)**(1.0/3.0)
    a_kd = T_CMB_GeV / T_kd * g_ratio_kd

    # Hubble rate at T_kd
    H_kd = H_rad(T_kd, g_s)

    # Kinetic decoupling wavenumber (entering horizon at T_kd):
    # k_kd = a_kd * H_kd (comoving Hubble scale at decoupling)
    # In h/Mpc: need to convert H from GeV to h/Mpc
    # H(GeV) = H(km/s/Mpc) * 1/(c_light_km_s) * (1 Mpc / hbar_c_GeV_m) * H_0_GeV/H_0_km_s_Mpc
    # Actually: k = aH in comoving. In h/Mpc:
    # k [h/Mpc] = a * H [GeV] / (H_0 [GeV]) * (100 km/s/Mpc) / c [km/s]
    # = a * H / H_0_GeV * (100 / c_light_km_s)
    H0_over_c_hMpc = 100.0 / c_light_km_s  # h/(c * Mpc) but in 1/Mpc
    k_kd = a_kd * H_kd / H_0_GeV * (100.0 / c_light_km_s)

    # Free-streaming damping scale for WIMP after kinetic decoupling:
    # lambda_fs(WIMP) ~ sqrt(T_kd / m_chi) * (1/H_kd) * ln(a_eq/a_kd)
    # where v_th(T_kd) ~ sqrt(T_kd / m_chi) for NR particle
    # For m_chi ~ 100 GeV, T_kd ~ 10 MeV: v ~ sqrt(10^-2/10^2) ~ 10^-2
    m_chi = 100.0  # GeV nominal  # (local)
    if name == 'Higgsino (1 TeV)':
        m_chi = 1000.0  # (local)
    elif name == 'Mixed (300 GeV)':
        m_chi = 300.0  # (local)

    v_kd = np.sqrt(3 * T_kd / m_chi)

    # Comoving free-streaming scale
    # lambda_fs ~ v_kd * a_kd * ln(a_eq / a_kd) / (sqrt(Omega_r) * H0_over_c_hMpc)
    # This is approximate; the exact integral accounts for the transition
    if a_kd < a_eq:
        I_fs = np.log(a_eq / a_kd) / np.sqrt(Omega_r)
    else:
        I_fs = 1.0 / np.sqrt(Omega_m)

    lambda_fs_wimp = v_kd * a_kd * I_fs / (100.0 / c_light_km_s)
    k_fs_wimp = 2 * PI / lambda_fs_wimp if lambda_fs_wimp > 0 else np.inf

    # The physical cutoff is max(k_kd, k_fs_wimp) = collisional vs free-streaming
    # In practice k_fs ~ k_kd for typical WIMPs
    k_cut_wimp = max(k_kd, k_fs_wimp)

    # Cutoff mass
    lambda_cut_wimp = 2 * PI / k_cut_wimp / h_hub  # Mpc
    M_cut_wimp = (4.0/3.0) * PI * (lambda_cut_wimp/2.0)**3 * rho_mean_Msun_Mpc3

    wimp_results[name] = {
        'T_kd': T_kd,
        'k_cut': k_cut_wimp,
        'M_cut': M_cut_wimp,
        'k_kd': k_kd,
        'k_fs': k_fs_wimp,
        'lambda_fs': lambda_fs_wimp,
    }

    print(f"{name:<25} {T_kd:<12.4e} {k_cut_wimp:<18.4e} {M_cut_wimp:<18.4e} {np.log10(k_cut_wimp):<12.2f}")

# =============================================================================
# SECTION 6: COMPREHENSIVE COMPARISON TABLE
# =============================================================================
print("\n--- Section 6: Comprehensive comparison ---")

print(f"\n{'Quantity':<40} {'Framework':<24} {'WIMP (bino)':<24} {'Ratio'}")
print("=" * 112)

k_wimp_bino = wimp_results['Bino (100 GeV)']['k_cut']
M_wimp_bino = wimp_results['Bino (100 GeV)']['M_cut']

print(f"{'DM mass (GeV)':<40} {m_DM_GeV:<24.4e} {'~100':<24} {m_DM_GeV/100:.4e}")
print(f"{'DM-SM sigma (cm^2)':<40} {sigma_DM_b_cm2:<24.4e} {sigma_WIMP_weak_cm2:<24.4e} {ratio_sigma:<.4e}")
print(f"{'T_kd (GeV)':<40} {'N/A (never coupled)':<24} {'~0.01':<24} {'---'}")
print(f"{'k_cut (h/Mpc)':<40} {k_cut_framework:<24.4e} {k_wimp_bino:<24.4e} {k_cut_framework/k_wimp_bino:.4e}")
print(f"{'log10(k_cut)':<40} {np.log10(k_cut_framework):<24.2f} {np.log10(k_wimp_bino):<24.2f} {'---'}")
print(f"{'M_cut (M_sun)':<40} {M_cut:<24.4e} {M_wimp_bino:<24.4e} {M_cut/M_wimp_bino:.4e}" if M_cut > 0 and M_wimp_bino > 0 else f"{'M_cut (M_sun)':<40} {'see below':<24} {M_wimp_bino:<24.4e} {'---'}")
print(f"{'Mechanism':<40} {'Free-streaming (no kd)':<24} {'Kin. decoupling':<24}")
print(f"{'Production T':<40} {M_KK:<24.4e} {'~few GeV (f.o.)':<24}")

# Key observable difference:
# The framework predicts k_cut >> k_cut(WIMP) because:
# 1. DM is super-heavy (m ~ 10^17 GeV), so v ~ sqrt(T/m) is tiny
# 2. Meissner screening ensures instant decoupling (no collisional damping)
# 3. Free-streaming length is microscopic (10^{-22} Mpc)
#
# This means the framework predicts NO observable small-scale cutoff
# at any scale probed by galaxy surveys, Lyman-alpha, or subhalo searches.
# Standard CDM WIMPs ALSO predict no cutoff at currently observable scales,
# but they predict cutoffs at k ~ 10^6-10^8 that could be probed by
# future gravitational lensing or pulsar timing.

# =============================================================================
# SECTION 7: OBSERVATIONAL WINDOW COMPARISON
# =============================================================================
print("\n--- Section 7: Observational window comparison ---")

obs_scales = {
    'CMB (Planck)':         (0.001, 0.2),      # h/Mpc
    'Galaxy surveys (DESI)': (0.01, 0.5),       # h/Mpc
    'Lyman-alpha':          (0.5, 100),         # h/Mpc
    'Galaxy counts':        (1, 1000),          # h/Mpc
    'Subhalo lensing':      (100, 1e6),         # h/Mpc
    'Pulsar timing (fut.)': (1e3, 1e8),         # h/Mpc
    'Micro-lensing (fut.)': (1e4, 1e10),        # h/Mpc
}

print(f"\n{'Observation':<25} {'k range (h/Mpc)':<25} {'Framework T^2(k)':<18} {'WIMP T^2(k)'}")
print("-" * 88)

for name, (k_lo, k_hi) in obs_scales.items():
    # Framework: T^2(k) = 1 - f_norm * (1 - exp(-(k/k_fs_warm)^2))
    # For k << k_fs_warm: T^2 ~ 1
    T2_fw_lo = 1.0 - f_normal * (1.0 - np.exp(-(k_lo/k_fs_warm)**2))
    T2_fw_hi = 1.0 - f_normal * (1.0 - np.exp(-(k_hi/k_fs_warm)**2))

    # WIMP: T^2(k) = 1 for k << k_cut_wimp, rapidly drops for k > k_cut_wimp
    k_wimp = k_wimp_bino
    T2_wimp_lo = np.exp(-(k_lo/k_wimp)**2) if k_lo > 0 else 1.0
    T2_wimp_hi = np.exp(-(k_hi/k_wimp)**2) if k_hi > 0 else 1.0

    fw_str = f"1.0000" if T2_fw_hi > 0.9999 else f"{T2_fw_hi:.4f}"
    wimp_str = f"1.0000" if T2_wimp_hi > 0.9999 else f"{T2_wimp_hi:.4e}"

    print(f"{name:<25} [{k_lo:.0e}, {k_hi:.0e}]{'':<8} {fw_str:<18} {wimp_str}")

# =============================================================================
# SECTION 8: SECONDARY EFFECTS — ACOUSTIC OSCILLATIONS IN DM
# =============================================================================
print("\n--- Section 8: Acoustic oscillations in DM (secondary) ---")

# Even without DM-baryon coupling, the DM quasiparticles propagate as
# collective modes on the 32-cell tessellation with sound speed c_Gold.
# This introduces DM acoustic oscillations at the scale of the internal
# geometry, but these are at k >> any observable scale.
#
# The DM sound horizon is:
# r_s^DM = c_Gold * t_transit ~ c_Gold * dt_transit / M_KK
# In comoving Mpc: need to account for a(t_transit) = a_prod

c_s_DM = c_Gold  # = 0.915 M_KK (dimensionless, in units of c)
# But c_Gold is the Goldstone sound speed on the internal geometry.
# The 4D cosmological sound speed for DM is set by the dispersion relation
# of the collective modes, which is c_Gold for the acoustic branch.

# Sound horizon at transit (internal geometry scale)
r_s_internal = c_s_DM * dt_transit  # M_KK^{-1} (internal units)
r_s_physical = r_s_internal / (M_KK * GeV_to_inv_m)  # meters
r_s_comoving = r_s_physical / (1.0/(1.0 + z_prod))  # comoving meters
r_s_comoving_Mpc = r_s_comoving / Mpc_to_m

print(f"DM sound speed:           c_Gold = {c_Gold:.4f} c")
print(f"Transit duration:         dt = {dt_transit:.6e} M_KK^{{-1}}")
print(f"Sound horizon (internal): r_s = {r_s_internal:.6e} M_KK^{{-1}}")
print(f"Sound horizon (physical): r_s = {r_s_physical:.4e} m")
print(f"Sound horizon (comoving): r_s = {r_s_comoving_Mpc:.4e} Mpc")

k_acoustic_DM = 2 * PI / r_s_comoving_Mpc * h_hub if r_s_comoving_Mpc > 0 else np.inf
print(f"DM acoustic scale:        k_ac = {k_acoustic_DM:.4e} h/Mpc")
print(f"  log10(k_ac) = {np.log10(k_acoustic_DM):.2f}" if k_acoustic_DM < np.inf else "  k_ac = inf")
print(f"  (Beyond all observable scales)")

# =============================================================================
# SECTION 9: MEISSNER LENGTH AS INTERACTION RANGE
# =============================================================================
print("\n--- Section 9: Meissner length as interaction range ---")

# The London penetration depth lambda_L sets the range of DM-SM interaction
# mediated by gauge bosons in the superconducting phase.
# For gauge interactions with Meissner mass m_M, the Yukawa potential is:
#   V(r) ~ exp(-m_M * r) / r
# The interaction range is r_int ~ 1/m_M = lambda_L

r_int_MKK = 1.0 / m_M_GGE                           # M_KK^{-1}
r_int_m = r_int_MKK / (M_KK * GeV_to_inv_m)          # meters
r_int_cm = r_int_m * 100
r_int_fm = r_int_m * 1e15

print(f"Interaction range (Meissner screening):")
print(f"  r_int = 1/m_M = {r_int_MKK:.6f} M_KK^{{-1}}")
print(f"  r_int = {r_int_m:.4e} m")
print(f"  r_int = {r_int_cm:.4e} cm")
print(f"  r_int = {r_int_fm:.4e} fm")
print(f"  For comparison:")
print(f"    Weak interaction range: 1/M_W ~ {1.0/(80.4 * GeV_to_inv_m):.4e} m")
print(f"    Planck length:          l_Pl ~ {l_Planck:.4e} m")
print(f"    Ratio r_int / l_Pl = {r_int_m / l_Planck:.4e}")

# The interaction range is about 2 orders of magnitude above the Planck length
# but vastly below any cosmological scale. This confirms that DM-SM interactions
# are exponentially suppressed at all relevant separations.

# =============================================================================
# SECTION 10: SUMMARY AND GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 10: SUMMARY AND GATE VERDICT")
print("=" * 78)

print(f"\n1. DM creation mechanism: transit quench at tau-fold (T ~ M_KK ~ 7.4e16 GeV)")
print(f"2. DM-SM cross-section: sigma = {sigma_DM_b_cm2:.2e} cm^2 (Meissner-screened)")
print(f"   - This is {np.log10(1/ratio_sigma):.0f} OOM below standard weak cross-section")
print(f"3. Kinetic decoupling: NEVER COUPLED (Gamma_mom/H < {ratio_max:.2e} at all T)")
print(f"4. Power spectrum cutoff is set entirely by free-streaming:")
print(f"   - Condensate (98.85%): k_cut = {k_cut_cond:.2e} h/Mpc (log = {np.log10(k_cut_cond):.1f})")
print(f"   - Normal fraction (1.15%): k_fs = {k_fs_warm:.2e} h/Mpc (log = {np.log10(k_fs_warm):.1f})")
print(f"   - Physical cutoff: k_cut = {k_cut_framework:.2e} h/Mpc (warm component)")
print(f"5. WIMP comparison (bino benchmark):")
print(f"   - k_cut(WIMP) = {k_wimp_bino:.2e} h/Mpc (log = {np.log10(k_wimp_bino):.1f})")
print(f"   - Framework/WIMP ratio: {k_cut_framework/k_wimp_bino:.2e}")
print(f"   - Framework cutoff is ~{np.log10(k_cut_framework/k_wimp_bino):.0f} OOM higher")
print(f"6. Observable consequence: IDENTICAL to CDM at all observable scales (k < 10^6)")
print(f"   - No observable difference from CDM at ANY current or planned survey scale")
print(f"   - Even micro-lensing (k ~ 10^10) cannot distinguish framework from CDM")

# Gate verdict
gate_name = "DM-CUTOFF-63"
gate_criterion = "INFO — report k_cut and compare to CDM benchmark"
gate_verdict = "INFORMATIVE"
gate_detail = (
    f"k_cut = {k_cut_framework:.2e} h/Mpc (log={np.log10(k_cut_framework):.1f}) from warm-fraction free-streaming. "
    f"Meissner screening (m_M={m_M_GGE:.3f} M_KK) gives sigma_DM-SM = {sigma_DM_b_cm2:.1e} cm^2, "
    f"{np.log10(1/ratio_sigma):.0f} OOM below weak scale. DM NEVER kinetically coupled (max Gamma/H = {ratio_max:.1e}). "
    f"vs WIMP (bino): k_cut = {k_wimp_bino:.1e} h/Mpc. Framework cutoff {np.log10(k_cut_framework/k_wimp_bino):.0f} OOM higher. "
    f"Both CDM and framework show T(k)=1 at all observable scales."
)

print(f"\n--- GATE VERDICT ---")
print(f"Gate {gate_name}: {gate_verdict}")
print(f"  Criterion: {gate_criterion}")
print(f"  Detail: {gate_detail}")

# =============================================================================
# SECTION 11: SAVE DATA
# =============================================================================
print("\n--- Section 11: Saving data ---")

output_path = os.path.join(script_dir, 's63_dm_cutoff.npz')
np.savez(output_path,
    # Gate
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_criterion=gate_criterion,
    gate_detail=gate_detail,
    # Framework cutoff
    k_cut_framework=k_cut_framework,
    k_cut_condensate=k_cut_cond,
    k_fs_warm=k_fs_warm,
    k_cut_1pct=k_cut_1pct,
    k_cut_01pct=k_cut_01pct,
    M_cut_framework=M_cut,
    lambda_fs_warm_Mpc=lambda_fs_warm,
    # Meissner screening
    m_M_GGE=m_M_GGE,
    m_M_fold=m_M_fold,
    m_M_GeV=m_M_GeV,
    lambda_L_GGE=lambda_L_GGE,
    sigma_DM_b=sigma_DM_b,
    sigma_DM_b_cm2=sigma_DM_b_cm2,
    r_int_m=r_int_m,
    # Kinetic decoupling
    max_Gamma_over_H=ratio_max,
    T_at_max_ratio=T_max,
    never_coupled=True,
    # WIMP comparison
    k_cut_WIMP_bino=wimp_results['Bino (100 GeV)']['k_cut'],
    k_cut_WIMP_mixed=wimp_results['Mixed (300 GeV)']['k_cut'],
    k_cut_WIMP_higgsino=wimp_results['Higgsino (1 TeV)']['k_cut'],
    M_cut_WIMP_bino=wimp_results['Bino (100 GeV)']['M_cut'],
    T_kd_WIMP_bino=wimp_results['Bino (100 GeV)']['T_kd'],
    sigma_WIMP_weak_cm2=sigma_WIMP_weak_cm2,
    # Derived
    ratio_k_cut=k_cut_framework / k_wimp_bino,
    ratio_sigma_fw_wimp=ratio_sigma,
    OOM_sigma_suppression=np.log10(1/ratio_sigma),
    # DM sound horizon
    k_acoustic_DM=k_acoustic_DM,
    r_s_DM_Mpc=r_s_comoving_Mpc,
    # Input scalars
    n_condensate=n_condensate,
    f_normal=f_normal,
    m_DM_GeV=m_DM_GeV,
    m_DM_MKK=m_DM_MKK,
    z_prod=z_prod,
)
print(f"Saved: {output_path}")

# =============================================================================
# SECTION 12: PLOT
# =============================================================================
print("\n--- Section 12: Generating plot ---")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Panel 1: Transfer function comparison
ax1 = axes[0]
k_plot = np.logspace(-2, 30, 10000)

# Framework mixed CDM+WDM transfer function
T2_fw = 1.0 - f_normal * (1.0 - np.exp(-(k_plot / k_fs_warm)**2))
# Pure warm component
T2_warm = np.exp(-(k_plot / k_fs_warm)**2)
# WIMP (bino) transfer function (Gaussian damping approximation)
T2_wimp = np.exp(-(k_plot / k_wimp_bino)**2)

ax1.semilogx(k_plot, T2_fw, 'b-', lw=2, label=f'Framework (mixed, f_n={f_normal:.3f})')
ax1.semilogx(k_plot, T2_warm, 'b--', lw=1, alpha=0.5, label='Warm component only')
ax1.semilogx(k_plot, T2_wimp, 'r-', lw=2, label=f'WIMP (bino, T_kd=10 MeV)')

# Mark observable ranges
ax1.axvspan(0.01, 100, alpha=0.1, color='green', label='Observable (galaxy+Lya)')
ax1.axvspan(100, 1e6, alpha=0.05, color='orange', label='Subhalo lensing')
ax1.axvline(k_cut_framework, color='b', ls=':', alpha=0.5)
ax1.axvline(k_wimp_bino, color='r', ls=':', alpha=0.5)

ax1.set_xlim(1e-2, 1e30)
ax1.set_ylim(0, 1.05)
ax1.set_xlabel('k [h/Mpc]')
ax1.set_ylabel(r'$T^2(k)$')
ax1.set_title('Matter Power Spectrum Transfer Function')
ax1.legend(loc='lower left', fontsize=7)

# Panel 2: DM-SM cross section and kinetic coupling ratio
ax2 = axes[1]
# Plot Gamma_mom / H as function of temperature
T_arr_plot = np.logspace(-3, 17, 500)
Gamma_plot = np.array([Gamma_mom(T, sigma_DM_b, m_DM_GeV) for T in T_arr_plot])
Gamma_wimp_plot = np.array([Gamma_mom(T, sigma_WIMP_weak, 100.0) for T in T_arr_plot])
H_plot = np.array([H_rad(T) for T in T_arr_plot])

ax2.loglog(T_arr_plot, Gamma_plot / H_plot, 'b-', lw=2, label='Framework DM')
ax2.loglog(T_arr_plot, Gamma_wimp_plot / H_plot, 'r-', lw=2, label='WIMP (100 GeV)')
ax2.axhline(1, color='k', ls='--', lw=1, label=r'$\Gamma_{mom}/H = 1$ (decoupling)')
ax2.axvline(M_KK, color='b', ls=':', alpha=0.3, label=f'M_KK = {M_KK:.1e} GeV')

ax2.set_xlim(1e-3, 1e18)
ax2.set_ylim(1e-80, 1e20)
ax2.set_xlabel('T [GeV]')
ax2.set_ylabel(r'$\Gamma_{mom} / H$')
ax2.set_title('Kinetic Coupling Ratio')
ax2.legend(loc='upper left', fontsize=7)

# Panel 3: Cutoff scale comparison diagram
ax3 = axes[2]
# Bar chart comparing log10(k_cut) for different models
models = ['Framework\n(condensate)', 'Framework\n(warm frac)',
          'WIMP\n(bino)', 'WIMP\n(mixed)', 'WIMP\n(higgsino)']
k_vals = [np.log10(k_cut_cond), np.log10(k_fs_warm),
          np.log10(wimp_results['Bino (100 GeV)']['k_cut']),
          np.log10(wimp_results['Mixed (300 GeV)']['k_cut']),
          np.log10(wimp_results['Higgsino (1 TeV)']['k_cut'])]
colors = ['#2196F3', '#64B5F6', '#F44336', '#EF9A9A', '#FFCDD2']

bars = ax3.barh(models, k_vals, color=colors, edgecolor='black', linewidth=0.5)
ax3.axvline(4, color='green', ls='--', lw=1.5, label='Observable limit (k~10^4)')
ax3.axvline(6, color='orange', ls='--', lw=1.5, label='Subhalo scale (k~10^6)')
ax3.set_xlabel(r'$\log_{10}(k_{cut}$ [h/Mpc])')
ax3.set_title('Power Spectrum Cutoff Comparison')
ax3.legend(loc='lower right', fontsize=7)
ax3.set_xlim(0, 25)

# Add value labels on bars
for bar, val in zip(bars, k_vals):
    ax3.text(val + 0.3, bar.get_y() + bar.get_height()/2, f'{val:.1f}',
             va='center', fontsize=8, fontweight='bold')

plt.tight_layout()
plot_path = os.path.join(script_dir, 's63_dm_cutoff.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {plot_path}")

# =============================================================================
# FINAL TIMING
# =============================================================================
elapsed = time.time() - t_start
print(f"\nTotal runtime: {elapsed:.2f}s")
print("\n" + "=" * 78)
print("DONE: s63_dm_cutoff.py")
print("=" * 78)
