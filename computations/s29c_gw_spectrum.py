#!/usr/bin/env python3
"""
29c-4: Gravitational Wave Spectrum from BCS First-Order Transition
===================================================================

Physics:
    A first-order phase transition in the early universe produces
    gravitational waves via three mechanisms:
    1. Bubble collisions (if transition proceeds via nucleation)
    2. Sound waves in the plasma (dominant for most transitions)
    3. Turbulence (subdominant)

    The key parameters are:
    - alpha: ratio of latent heat to radiation energy density
      alpha = epsilon / rho_rad, where rho_rad = (pi^2/30)*g_* T^4
    - beta/H: inverse duration of the transition in Hubble units
      Faster transitions (large beta/H) produce weaker but higher-frequency GW
    - T_*: temperature at which the transition occurs
    - v_w: bubble wall velocity (typically ~0.5-1.0 for strong transitions)

    The peak frequency today and amplitude are:
    f_peak ~ 1.65e-5 Hz * (beta/H) * (T_*/100 GeV) * (g_*/100)^{1/6}
    h^2 Omega_GW ~ 1.67e-5 * (100/beta/H)^2 * (alpha/(1+alpha))^2 * (100/g_*)^{1/3}

    For our BCS transition:
    - alpha is determined by F_BCS / rho_rad
    - beta/H ~ t_BCS * H (transition duration ~ crossing time)
    - T_* ~ T_RH(M_KK) from s29b

Method:
    For each M_KK:
    1. Compute alpha from latent heat and radiation density
    2. Estimate beta/H from modulus crossing dynamics
    3. Compute GW spectrum: f_peak, h^2*Omega_GW
    4. Plot vs LISA and LIGO sensitivity curves

Inputs:
    tier0-computation/s28b_self_consistent_tau_T.npz
    tier0-computation/s29b_free_energy_comparison.npz
    tier0-computation/s29b_modulus_eom.npz
    tier0-computation/s29b_gaussian_correction.npz

Outputs:
    tier0-computation/s29c_gw_spectrum.npz
    tier0-computation/s29c_gw_spectrum.png
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ==============================================================================
# Constants
# ==============================================================================

GeV_to_invs = 1.519e24     # 1/s per GeV
M_Pl_GeV = 2.435e18        # reduced Planck mass in GeV
h_hubble = 0.674            # Hubble parameter (Planck 2018)

# ==============================================================================
# Load data
# ==============================================================================

data_dir = os.path.join(os.path.dirname(__file__))

eom = np.load(os.path.join(data_dir, 's29b_modulus_eom.npz'), allow_pickle=True)
bcs = np.load(os.path.join(data_dir, 's29b_free_energy_comparison.npz'), allow_pickle=True)
gauss = np.load(os.path.join(data_dir, 's29b_gaussian_correction.npz'), allow_pickle=True)
sc = np.load(os.path.join(data_dir, 's28b_self_consistent_tau_T.npz'), allow_pickle=True)

M_KK_values = eom['M_KK_values']  # [1e14, ..., 1e18]
n_MKK = len(M_KK_values)

# Extract observables
t_BCS_sec = np.zeros(n_MKK)
H_phys_GeV = np.zeros(n_MKK)
T_RH_GeV = np.zeros(n_MKK)

for i in range(n_MKK):
    t_BCS_sec[i] = float(eom[f'obs_{i}_t_BCS_sec'].flat[0])
    H_phys_GeV[i] = float(eom[f'obs_{i}_H_phys_gev'].flat[0])
    T_RH_GeV[i] = float(eom[f'obs_{i}_T_RH_gev'].flat[0])

# Latent heat from BCS (in dimensionless spectral units)
# F_BCS at mu=lambda_min at tau=0.50
L_mu1 = float(eom['latent_heat_mu1'].flat[0])    # 5.63
L_mu12 = float(eom['latent_heat_mu12'].flat[0])   # 14.01
L_mu15 = float(eom['latent_heat_mu15'].flat[0])   # 38.93

# BCS gap data
Delta_BCS_050 = float(gauss['vH_0p50_Delta'])   # 0.307 at tau=0.50
Delta_BCS_035 = float(gauss['vH_0p35_Delta'])   # 0.404 at tau=0.35

# Modulus kinetic energy at crossing
KE_cross = [float(eom[f'trap_{i}_KE_at_cross'].flat[0]) for i in range(3)]
E_mults = [float(eom[f'trap_{i}_E_mult'].flat[0]) for i in range(3)]

# G_tau_tau (moduli space metric)
G_tau_tau = float(eom['G_tau_tau'].flat[0])  # 5.0

print("=" * 70)
print("29c-4: GRAVITATIONAL WAVE SPECTRUM FROM BCS TRANSITION")
print("=" * 70)

# ==============================================================================
# Compute GW parameters for each M_KK
# ==============================================================================

# The BCS transition happens when the modulus crosses the condensation threshold.
# The transition is first-order (latent heat = F_BCS jump).
#
# To convert dimensionless spectral action units to physical:
# S_spectral ~ (M_KK)^6 / (M_Pl)^2 * (dimensionless)
# => Physical energy density epsilon = L_dim * M_KK^6 / M_Pl^2
#
# Radiation density at temperature T:
# rho_rad = (pi^2/30) * g_* * T^4
#
# alpha = epsilon / rho_rad

# Relativistic DOF at BCS temperature
# For T > 100 GeV: g_* ~ 106.75 (SM)
# For T > M_KK: g_* could be larger due to KK modes
# Use g_* = 106.75 as conservative estimate
g_star = 106.75

# The energy scale of the spectral action:
# S[D^2, Lambda] = sum_n f(lambda_n/Lambda^2)
# In our units, lambda_n ~ M_KK^2 (eigenvalues of D^2 on internal space)
# The dimensionful spectral action: Tr[f(D^2/Lambda^2)] ~ N(Lambda) * M_KK^2 * ...
# For the Chamseddine-Connes spectral action:
# S_phys = (M_KK^4 / (4*pi^2)) * S_dimensionless
# (this is the standard 6D -> 4D reduction factor)

# The latent heat in physical units:
# epsilon_phys = L_dim * M_KK^4 / (4*pi^2)

alpha_per_MKK = np.zeros(n_MKK)
beta_over_H = np.zeros(n_MKK)
f_peak_Hz = np.zeros(n_MKK)
h2_Omega_peak = np.zeros(n_MKK)
f_peak_sw = np.zeros(n_MKK)
h2_Omega_sw = np.zeros(n_MKK)
f_peak_turb = np.zeros(n_MKK)
h2_Omega_turb = np.zeros(n_MKK)

# Bubble wall velocity (use v_w = 1 for detonation, common for strong transitions)
v_w = 0.95  # slightly subluminal detonation

# Efficiency factors
kappa_v = 0.5   # fraction of latent heat going to bulk fluid motion
kappa_turb = 0.05  # fraction going to turbulence

print(f"\nBubble wall velocity: v_w = {v_w}")
print(f"Efficiency kappa_v = {kappa_v}, kappa_turb = {kappa_turb}")
print(f"g_* = {g_star}")
print()

for i in range(n_MKK):
    M_KK = M_KK_values[i]
    T_star = T_RH_GeV[i]
    H_star = H_phys_GeV[i]  # Hubble at transition

    # Physical latent heat (using mu=lambda_min scenario)
    # epsilon = L_mu1 * M_KK^4 / (4*pi^2)
    epsilon_phys = L_mu1 * M_KK**4 / (4.0 * np.pi**2)

    # Radiation energy density at T_star
    rho_rad = (np.pi**2 / 30.0) * g_star * T_star**4

    # alpha = epsilon / rho_rad
    alpha = epsilon_phys / rho_rad if rho_rad > 0 else 0.0
    alpha_per_MKK[i] = alpha

    # beta/H: inverse transition duration
    # The transition completes on a timescale ~ t_BCS (modulus crossing time)
    # beta ~ 1/t_transition ~ 1/t_BCS
    # beta/H = 1/(H * t_transition) = 1/(H * t_BCS)
    # From the EOM: t_BCS_dimless ~ 0.2, physical t_BCS ~ 0.2/M_KK
    # H ~ M_KK^2 / M_Pl
    # => beta/H ~ M_Pl / (0.2 * M_KK)

    # More precisely: beta = -dS_E/dt|_nucleation evaluated at t_*
    # For our case, the BCS transition is driven by the rolling modulus,
    # so the transition duration is set by the modulus dynamics, not
    # by thermal nucleation.
    # beta ~ dtau/dt * |dDelta/dtau| / Delta_BCS
    # From s29b: dtau/dt ~ 1.12 (at crossing, in M_KK units)
    # dtau ~ 0.5 for BCS to develop fully
    # => beta ~ dtau/dt / dtau_BCS ~ 1.12 / 0.1 ~ 10 (in M_KK units)
    # beta/H = beta_dimless * M_KK / H = 10 * M_Pl / M_KK

    # Use the ODE data for more precision
    # For M_KK = 1e14, 1e16: we have ODE solutions
    # The crossing time is t_cross_dimless ~ 0.2
    # The BCS activation region is ~0.1 in tau units
    # dtau/dt at crossing ~ 1.12 M_KK
    # So tau traverses the BCS activation zone in dt ~ 0.1/1.12 ~ 0.09 in 1/M_KK
    # beta ~ 1/dt ~ 11 M_KK
    # beta/H = 11 * M_KK / (M_KK^2/M_Pl) = 11 * M_Pl / M_KK

    beta_MKK = 11.0 * M_KK  # beta in GeV
    bH = beta_MKK / H_star
    beta_over_H[i] = bH

    # ==================================================================
    # GW from sound waves (dominant contribution)
    # ==================================================================
    # From Hindmarsh et al. (2015, 2017):
    # h^2 Omega_sw = 2.65e-6 * (H/beta)^1 * (kappa_v * alpha / (1+alpha))^2
    #               * (100/g_*)^{1/3} * v_w * Gamma(f/f_sw)
    # where Gamma is the spectral shape.
    #
    # Peak frequency:
    # f_sw = 1.9e-5 Hz * (1/v_w) * (beta/H) * (T_*/100 GeV) * (g_*/100)^{1/6}

    f_sw_i = 1.9e-5 * (1.0/v_w) * bH * (T_star/100.0) * (g_star/100.0)**(1.0/6.0)
    f_peak_sw[i] = f_sw_i

    # Peak amplitude (at f = f_sw):
    h2_Omega_sw_i = 2.65e-6 * (1.0/bH) * (kappa_v * alpha / (1.0 + alpha))**2 \
                    * (100.0/g_star)**(1.0/3.0) * v_w
    h2_Omega_sw[i] = h2_Omega_sw_i

    # ==================================================================
    # GW from bubble collisions (envelope approximation)
    # ==================================================================
    # h^2 Omega_col = 1.67e-5 * (H/beta)^2 * (alpha/(1+alpha))^2
    #                * (100/g_*)^{1/3} * (0.11*v_w^3/(0.42+v_w^2))
    # Peak frequency:
    # f_col = 1.65e-5 Hz * (0.62/(1.8-0.1*v_w+v_w^2)) * (beta/H)
    #         * (T_*/100 GeV) * (g_*/100)^{1/6}

    f_col_factor = 0.62 / (1.8 - 0.1*v_w + v_w**2)
    f_col_i = 1.65e-5 * f_col_factor * bH * (T_star/100.0) * (g_star/100.0)**(1.0/6.0)
    f_peak_Hz[i] = f_col_i

    col_eff = 0.11 * v_w**3 / (0.42 + v_w**2)
    h2_Omega_col_i = 1.67e-5 * (1.0/bH)**2 * (alpha/(1.0+alpha))**2 \
                     * (100.0/g_star)**(1.0/3.0) * col_eff
    h2_Omega_peak[i] = h2_Omega_col_i

    # ==================================================================
    # GW from turbulence
    # ==================================================================
    # f_turb ~ 2.7e-5 Hz * (1/v_w) * (beta/H) * (T_*/100 GeV) * (g_*/100)^{1/6}
    # h^2 Omega_turb ~ 3.35e-4 * (H/beta) * (kappa_turb * alpha/(1+alpha))^{3/2}
    #                 * (100/g_*)^{1/3} * v_w

    f_turb_i = 2.7e-5 * (1.0/v_w) * bH * (T_star/100.0) * (g_star/100.0)**(1.0/6.0)
    f_peak_turb[i] = f_turb_i

    h2_Omega_turb_i = 3.35e-4 * (1.0/bH) * (kappa_turb * alpha/(1.0+alpha))**(1.5) \
                      * (100.0/g_star)**(1.0/3.0) * v_w
    h2_Omega_turb[i] = h2_Omega_turb_i

    print(f"M_KK = {M_KK:.0e} GeV:")
    print(f"  T_* = {T_star:.3e} GeV")
    print(f"  H_* = {H_star:.3e} GeV")
    print(f"  alpha = {alpha:.4e}")
    print(f"  beta/H = {bH:.2e}")
    print(f"  --- Sound waves ---")
    print(f"    f_peak = {f_sw_i:.3e} Hz")
    print(f"    h^2 Omega = {h2_Omega_sw_i:.3e}")
    print(f"  --- Bubble collisions ---")
    print(f"    f_peak = {f_col_i:.3e} Hz")
    print(f"    h^2 Omega = {h2_Omega_col_i:.3e}")
    print(f"  --- Turbulence ---")
    print(f"    f_peak = {f_turb_i:.3e} Hz")
    print(f"    h^2 Omega = {h2_Omega_turb_i:.3e}")
    print()

# ==============================================================================
# LISA and LIGO sensitivity curves
# ==============================================================================

# LISA power-law sensitivity (approximate)
# LISA: f_range ~ [1e-4, 0.1] Hz
# Peak sensitivity at ~3e-3 Hz: h^2 Omega ~ 1e-12
f_LISA = np.logspace(-5, -0.5, 500)
# Approximate LISA sensitivity (from Caprini et al. 2016):
# S_n(f) fit: sum of acceleration noise + optical metrology + confusion noise
# Simplified power-law-integrated:
h2_Omega_LISA = 1e-12 * ((f_LISA/3e-3)**(-4.0/3.0) + (f_LISA/3e-3)**(2.0))
h2_Omega_LISA = np.clip(h2_Omega_LISA, 1e-13, 1e-5)

# LIGO design sensitivity
# LIGO: f_range ~ [10, 3000] Hz
# Peak at ~50 Hz: h^2 Omega ~ 1e-9
f_LIGO = np.logspace(0.5, 3.5, 500)
h2_Omega_LIGO = 1e-9 * ((f_LIGO/50.0)**(-3.0) + (f_LIGO/50.0)**(2.0))
h2_Omega_LIGO = np.clip(h2_Omega_LIGO, 1e-10, 1e-3)

# BBO/DECIGO (future): f ~ [0.1, 10] Hz, sensitivity ~ 1e-16
f_BBO = np.logspace(-1.5, 1.5, 500)
h2_Omega_BBO = 1e-16 * ((f_BBO/1.0)**(-2.0) + (f_BBO/1.0)**(2.0))
h2_Omega_BBO = np.clip(h2_Omega_BBO, 1e-17, 1e-10)

# Pulsar timing arrays (NANOGrav, EPTA): f ~ [1e-9, 1e-7] Hz
f_PTA = np.logspace(-9.5, -6.5, 500)
h2_Omega_PTA = 1e-9 * ((f_PTA/1e-8)**(-2.0/3.0))
h2_Omega_PTA = np.clip(h2_Omega_PTA, 1e-11, 1e-6)

# ==============================================================================
# Spectral shape for plotting
# ==============================================================================

def gw_spectrum_sw(f, f_peak, h2_Omega_0):
    """Sound wave GW spectrum shape (broken power law)."""
    x = f / f_peak
    # From Hindmarsh et al.:
    # Omega(f) ~ Omega_peak * (f/f_peak)^3 * (7/(4+3*(f/f_peak)^2))^{7/2}
    return h2_Omega_0 * x**3 * (7.0 / (4.0 + 3.0*x**2))**3.5

# ==============================================================================
# Gate verdict
# ==============================================================================

# PASS if any M_KK produces GW signal above LISA sensitivity
# MODERATE if above BBO/DECIGO
# DIAGNOSTIC otherwise

# Check LISA detectability at sound wave peak
any_above_LISA = False
any_above_BBO = False

for i in range(n_MKK):
    # Interpolate LISA sensitivity at f_peak
    f_sw = f_peak_sw[i]
    if 1e-5 < f_sw < 0.3:
        sens_at_f = np.interp(f_sw, f_LISA, h2_Omega_LISA)
        if h2_Omega_sw[i] > sens_at_f:
            any_above_LISA = True
    if 0.03 < f_sw < 30:
        sens_at_f_bbo = np.interp(np.clip(f_sw, f_BBO[0], f_BBO[-1]), f_BBO, h2_Omega_BBO)
        if h2_Omega_sw[i] > sens_at_f_bbo:
            any_above_BBO = True

if any_above_LISA:
    verdict = "PASS"
    verdict_detail = "GW signal above LISA sensitivity for some M_KK"
elif any_above_BBO:
    verdict = "MODERATE"
    verdict_detail = "GW signal above BBO/DECIGO but below LISA"
else:
    verdict = "DIAGNOSTIC"
    verdict_detail = "GW signal below current/planned detector sensitivity"

# Check if alpha is physical
alpha_max = alpha_per_MKK.max()
alpha_min = alpha_per_MKK.min()

print("=" * 50)
print(f"alpha range: [{alpha_min:.4e}, {alpha_max:.4e}]")
print(f"beta/H range: [{beta_over_H.min():.2e}, {beta_over_H.max():.2e}]")
print(f"f_peak(SW) range: [{f_peak_sw.min():.3e}, {f_peak_sw.max():.3e}] Hz")
print(f"h^2 Omega(SW) range: [{h2_Omega_sw.min():.3e}, {h2_Omega_sw.max():.3e}]")
print(f"\nLISA detectable: {any_above_LISA}")
print(f"BBO detectable: {any_above_BBO}")
print(f"\nVerdict: {verdict}")
print(f"Detail: {verdict_detail}")

# ==============================================================================
# Save
# ==============================================================================

np.savez(
    os.path.join(data_dir, 's29c_gw_spectrum.npz'),
    M_KK_values=M_KK_values,
    T_star_GeV=T_RH_GeV,
    H_star_GeV=H_phys_GeV,
    alpha=alpha_per_MKK,
    beta_over_H=beta_over_H,
    f_peak_collision_Hz=f_peak_Hz,
    h2_Omega_collision=h2_Omega_peak,
    f_peak_sw_Hz=f_peak_sw,
    h2_Omega_sw=h2_Omega_sw,
    f_peak_turb_Hz=f_peak_turb,
    h2_Omega_turb=h2_Omega_turb,
    v_w=v_w,
    g_star=g_star,
    kappa_v=kappa_v,
    kappa_turb=kappa_turb,
    latent_heat_mu1=L_mu1,
    verdict=verdict,
    verdict_detail=verdict_detail,
)
print(f"\nSaved: s29c_gw_spectrum.npz")

# ==============================================================================
# Plot
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Panel 1: GW spectrum overview with detector sensitivity
ax = axes[0, 0]

# Detector curves
ax.fill_between(f_LISA, h2_Omega_LISA, 1e-3, alpha=0.1, color='purple', label='LISA')
ax.loglog(f_LISA, h2_Omega_LISA, 'purple', lw=1.5, alpha=0.5)
ax.fill_between(f_LIGO, h2_Omega_LIGO, 1e-3, alpha=0.1, color='blue', label='LIGO')
ax.loglog(f_LIGO, h2_Omega_LIGO, 'blue', lw=1.5, alpha=0.5)
ax.fill_between(f_BBO, h2_Omega_BBO, 1e-3, alpha=0.1, color='green', label='BBO/DECIGO')
ax.loglog(f_BBO, h2_Omega_BBO, 'green', lw=1.5, alpha=0.5)
ax.fill_between(f_PTA, h2_Omega_PTA, 1e-3, alpha=0.1, color='orange', label='PTA')
ax.loglog(f_PTA, h2_Omega_PTA, 'orange', lw=1.5, alpha=0.5)

# GW signals from sound waves at each M_KK
colors_mkk = ['red', 'darkorange', 'darkred', 'crimson', 'firebrick']
for i in range(n_MKK):
    f_range = np.logspace(np.log10(f_peak_sw[i]) - 4, np.log10(f_peak_sw[i]) + 3, 500)
    h2_spec = gw_spectrum_sw(f_range, f_peak_sw[i], h2_Omega_sw[i])
    ax.loglog(f_range, h2_spec, color=colors_mkk[i], lw=2,
              label=f'$M_{{KK}}$={M_KK_values[i]:.0e}')

ax.set_xlabel('Frequency [Hz]', fontsize=13)
ax.set_ylabel(r'$h^2 \Omega_{GW}$', fontsize=13)
ax.set_title('Gravitational Wave Spectrum from BCS Transition', fontsize=14)
ax.set_xlim(1e-10, 1e4)
ax.set_ylim(1e-22, 1e-3)
ax.legend(fontsize=8, loc='upper right', ncol=2)
ax.grid(True, alpha=0.3, which='both')

# Panel 2: alpha vs M_KK
ax = axes[0, 1]
ax.loglog(M_KK_values, alpha_per_MKK, 'ro-', ms=8, lw=2)
ax.axhline(1.0, color='k', ls='--', lw=1, alpha=0.5, label=r'$\alpha = 1$ (strong)')
ax.axhline(0.01, color='gray', ls=':', lw=1, alpha=0.5, label=r'$\alpha = 0.01$ (weak)')
ax.set_xlabel(r'$M_{KK}$ [GeV]', fontsize=13)
ax.set_ylabel(r'$\alpha$ (latent heat / radiation)', fontsize=13)
ax.set_title('Transition Strength', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, which='both')

# Panel 3: beta/H vs M_KK
ax = axes[1, 0]
ax.loglog(M_KK_values, beta_over_H, 'bs-', ms=8, lw=2)
ax.set_xlabel(r'$M_{KK}$ [GeV]', fontsize=13)
ax.set_ylabel(r'$\beta / H$', fontsize=13)
ax.set_title('Transition Duration (inverse)', fontsize=14)
ax.grid(True, alpha=0.3, which='both')

# Panel 4: f_peak and h^2*Omega for all three mechanisms
ax = axes[1, 1]
ax.loglog(f_peak_sw, h2_Omega_sw, 'ro', ms=10, label='Sound waves', zorder=5)
ax.loglog(f_peak_Hz, h2_Omega_peak, 'b^', ms=10, label='Bubble collisions', zorder=5)
ax.loglog(f_peak_turb, h2_Omega_turb, 'gs', ms=10, label='Turbulence', zorder=5)

# Annotate M_KK values
for i in range(n_MKK):
    ax.annotate(f'{M_KK_values[i]:.0e}',
                (f_peak_sw[i], h2_Omega_sw[i]),
                textcoords="offset points", xytext=(5, 5), fontsize=7)

# Detector bands
ax.axhspan(1e-12, 1e-3, xmin=0, xmax=1, alpha=0.05, color='purple')
ax.text(1e-3, 3e-12, 'LISA', fontsize=9, color='purple', alpha=0.7)

ax.set_xlabel(r'$f_{peak}$ [Hz]', fontsize=13)
ax.set_ylabel(r'$h^2 \Omega_{GW}^{peak}$', fontsize=13)
ax.set_title('Peak GW Signal by Mechanism', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, which='both')
ax.set_xlim(1e-5, 1e15)
ax.set_ylim(1e-35, 1e-3)

plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's29c_gw_spectrum.png'), dpi=150, bbox_inches='tight')
print(f"Saved: s29c_gw_spectrum.png")
print("\nDone.")
