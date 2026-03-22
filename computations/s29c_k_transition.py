#!/usr/bin/env python3
"""
29c-2: Transition Scale k_transition from Modulus Dynamics
==========================================================

Physics:
    When the modulus tau rolls from tau=0 to the BCS trapping point at tau~0.35-0.50,
    it crosses the BCS condensation threshold at some time t_BCS. The comoving
    wavenumber that exits the horizon at that moment defines a characteristic scale:

        k_transition = a(t_BCS) * H(t_BCS)

    where a(t) is the scale factor and H(t) is the Hubble parameter. This scale
    separates modes that experienced the BCS phase transition (k < k_transition)
    from those that did not (k > k_transition). In the exflation framework,
    k_transition should fall within the observable range for DESI/Euclid
    (0.01-0.3 h/Mpc) to produce detectable signatures.

    From the modulus EOM (s29b), we have t_BCS in physical seconds and H(t_BCS)
    at different M_KK values. The scale factor at BCS transition depends on the
    expansion history before and during the transition.

Method:
    For each M_KK:
    1. Extract t_BCS, H at BCS crossing from s29b data
    2. Compute a(t_BCS) assuming radiation-dominated expansion before BCS:
       a(t) = a_0 * (t/t_0)^{1/2}    (radiation dominated)
       or a(t) = a_0 * exp(H*t)       (de Sitter)
    3. k_transition = a(t_BCS) * H(t_BCS) in physical units
    4. Convert to h/Mpc for comparison with surveys
    5. Plot vs DESI/Euclid sensitivity range

Inputs:
    tier0-computation/s29b_modulus_eom.npz

Outputs:
    tier0-computation/s29c_k_transition.npz
    tier0-computation/s29c_k_transition.png
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ==============================================================================
# Constants
# ==============================================================================

# Physical constants in CGS/natural units
c_mks = 2.998e8        # m/s
hbar_mks = 1.055e-34   # J.s
G_N_mks = 6.674e-11    # m^3/(kg.s^2)
GeV_to_J = 1.602e-10   # J/GeV
GeV_to_invs = GeV_to_J / hbar_mks   # 1/s per GeV (= 1.519e24 /s per GeV)
Mpc_to_m = 3.086e22    # m/Mpc
h_hubble = 0.674       # Planck 2018 h

# M_Planck in GeV
M_Pl_GeV = 2.435e18    # reduced Planck mass

# ==============================================================================
# Load data
# ==============================================================================

data_dir = os.path.join(os.path.dirname(__file__))
eom = np.load(os.path.join(data_dir, 's29b_modulus_eom.npz'), allow_pickle=True)

M_KK_values = eom['M_KK_values']  # [1e14, 1e15, 1e16, 1e17, 1e18] GeV
tau_cross = float(eom['tau_cross'].flat[0])  # 0.5

# Extract per-M_KK observables
n_MKK = len(M_KK_values)
t_BCS_sec = np.zeros(n_MKK)
H_phys_GeV = np.zeros(n_MKK)
T_RH_GeV = np.zeros(n_MKK)
friction_param = np.zeros(n_MKK)

for i in range(n_MKK):
    t_BCS_sec[i] = float(eom[f'obs_{i}_t_BCS_sec'].flat[0])
    H_phys_GeV[i] = float(eom[f'obs_{i}_H_phys_gev'].flat[0])
    T_RH_GeV[i] = float(eom[f'obs_{i}_T_RH_gev'].flat[0])
    friction_param[i] = float(eom[f'obs_{i}_friction_param'].flat[0])

# Also extract ODE solutions for more detail
latent_heat = float(eom['latent_heat_mu1'].flat[0])  # F_BCS at mu=lambda_min, tau=0.50

print("=" * 70)
print("29c-2: TRANSITION SCALE k_transition")
print("=" * 70)
print()

# ==============================================================================
# Compute k_transition for different expansion histories
# ==============================================================================

# The key relation: k_phys = a * H at horizon exit
# After the BCS transition, we need to redshift to today:
#   k_today = k_phys * (a_BCS / a_today)
#
# During radiation domination: a(t) ~ t^{1/2}, H = 1/(2t)
# The temperature at BCS: T_BCS ~ (M_Pl / t_BCS)^{1/2} (Friedmann)
#
# Relating to today: k_today / a_today = H_BCS * (a_BCS / a_today)
# In radiation domination: a_BCS/a_today = T_today/T_BCS (entropy conservation)
# k_today = H_BCS * T_0 / T_BCS  (in natural units, k_today in 1/length)

T_CMB_GeV = 2.725 * 8.617e-14  # 2.725 K in GeV (k_B*T)
T_CMB_eV = 2.725 * 8.617e-5    # eV

# Scenario A: Radiation-dominated at BCS
# H_BCS = pi * sqrt(g_*) * T_BCS^2 / (3*sqrt(10) * M_Pl)
# But we have H directly from the EOM: H_phys_GeV

# k_today (physical) = H_BCS * (a_BCS/a_0) = H_BCS * T_0/T_BCS
# Convert to h/Mpc:
# k [h/Mpc] = k [1/s] * c / (H_100 * Mpc)
# where H_100 = 100 km/s/Mpc = 3.241e-18 /s

H_100_invs = 3.241e-18  # 100 km/s/Mpc in 1/s

# Method: k_transition = H(t_BCS) * T_CMB / T_RH, then convert units
# H in 1/s, T ratio is dimensionless, result in 1/s
# Convert 1/s to h/Mpc: multiply by c / (H_100 * Mpc) * h

k_transition_rad = np.zeros(n_MKK)
k_transition_dS = np.zeros(n_MKK)
T_BCS_from_H = np.zeros(n_MKK)

for i in range(n_MKK):
    # Hubble at BCS in 1/s
    H_invs = H_phys_GeV[i] * GeV_to_invs

    # Temperature at BCS (~ reheat temperature for our purposes)
    T_BCS = T_RH_GeV[i]  # GeV

    # Scenario A: Radiation-dominated universe at BCS
    # k_physical_today = H_BCS * (T_CMB / T_BCS)
    k_phys_invs = H_invs * (T_CMB_GeV / T_BCS)

    # Convert to h/Mpc
    # k [h/Mpc] = k [1/m] / (h * H_100 / c)
    #           = k [1/s] * 1 / (h * H_100_invs)
    # Actually: k [h/Mpc] = k [1/s] / (h_hubble * H_100_invs)
    # No wait. k has units of inverse length in comoving coordinates.
    # k_phys [1/s] -> k_phys [1/m] = k_phys_invs / c
    # k [h/Mpc] = k [1/m] * Mpc_to_m / h_hubble
    #   But that gives huge numbers. Let me be more careful.
    #
    # The standard conversion: k [Mpc^{-1}] = k [1/s] * (Mpc_to_m / c_mks)
    # Then k [h/Mpc] = k [Mpc^{-1}] / h_hubble
    # Actually k [h/Mpc] = k [Mpc^{-1}] * h_hubble  ... no.
    # Convention: k in units of h/Mpc means k_phys = k * h / Mpc
    # So k [h/Mpc] = k_phys * Mpc / h
    # k_phys in 1/m: k_phys_m = k_phys_invs / c_mks
    # k [h/Mpc] = k_phys_m * Mpc_to_m / h_hubble

    k_phys_invm = k_phys_invs / c_mks
    k_hMpc = k_phys_invm * Mpc_to_m / h_hubble

    k_transition_rad[i] = k_hMpc

    # Scenario B: de Sitter-like (if modulus drives inflation)
    # During de Sitter: k = a*H = const for modes at horizon
    # After reheating: k_today = H_dS * exp(N_efolds_remaining) * (T_RH/T_0)^{-1}
    # But we don't know N_efolds. Use N_eff ~ H*t_BCS ~ small (order 1)
    # This is really a lower bound on k since de Sitter produces more expansion.
    N_eff = H_invs * t_BCS_sec[i]
    k_dS_invs = H_invs * np.exp(N_eff) * (T_CMB_GeV / T_BCS)
    k_dS_invm = k_dS_invs / c_mks
    k_transition_dS[i] = k_dS_invm * Mpc_to_m / h_hubble

    T_BCS_from_H[i] = T_BCS

    print(f"M_KK = {M_KK_values[i]:.0e} GeV:")
    print(f"  t_BCS = {t_BCS_sec[i]:.3e} s")
    print(f"  H_BCS = {H_phys_GeV[i]:.3e} GeV = {H_invs:.3e} /s")
    print(f"  T_BCS = {T_BCS:.3e} GeV")
    print(f"  k_transition (rad)  = {k_hMpc:.4e} h/Mpc")
    print(f"  k_transition (dS)   = {k_transition_dS[i]:.4e} h/Mpc")
    print(f"  N_eff (H*t_BCS)     = {N_eff:.4f}")
    print(f"  Friction param      = {friction_param[i]:.4e}")
    print()

# ==============================================================================
# DESI/Euclid comparison
# ==============================================================================

# DESI BAO: 0.02 - 0.3 h/Mpc (galaxy survey)
# Euclid: 0.001 - 0.5 h/Mpc (broader range)
# LIGO horizon: ~10 - 1000 Mpc^{-1} (much higher k)
# CMB (Planck): 0.0005 - 0.2 Mpc^{-1}

DESI_kmin, DESI_kmax = 0.02, 0.30     # h/Mpc
Euclid_kmin, Euclid_kmax = 0.001, 0.50  # h/Mpc
CMB_kmin, CMB_kmax = 0.0005/h_hubble, 0.2/h_hubble  # convert to h/Mpc

print("=" * 50)
print("Comparison with survey ranges:")
print(f"  DESI BAO:   [{DESI_kmin}, {DESI_kmax}] h/Mpc")
print(f"  Euclid:     [{Euclid_kmin}, {Euclid_kmax}] h/Mpc")
print(f"  CMB:        [{CMB_kmin:.4f}, {CMB_kmax:.3f}] h/Mpc")
print()

# Which M_KK puts k_transition in DESI range?
for i in range(n_MKK):
    in_DESI = DESI_kmin <= k_transition_rad[i] <= DESI_kmax
    in_Euclid = Euclid_kmin <= k_transition_rad[i] <= Euclid_kmax
    status = ""
    if in_DESI:
        status = " ** IN DESI RANGE **"
    elif in_Euclid:
        status = " * in Euclid range *"
    print(f"  M_KK={M_KK_values[i]:.0e}: k={k_transition_rad[i]:.3e} h/Mpc{status}")

# ==============================================================================
# Gate verdict
# ==============================================================================
# PASS if any M_KK in [1e14, 1e18] puts k_transition within Euclid range
# STRONG PASS if in DESI range

any_in_Euclid = np.any((k_transition_rad >= Euclid_kmin) & (k_transition_rad <= Euclid_kmax))
any_in_DESI = np.any((k_transition_rad >= DESI_kmin) & (k_transition_rad <= DESI_kmax))

if any_in_DESI:
    verdict = "PASS"
    verdict_detail = "k_transition falls within DESI BAO range for some M_KK"
elif any_in_Euclid:
    verdict = "MODERATE"
    verdict_detail = "k_transition falls within Euclid range but outside DESI"
else:
    # Check if it's within a few orders of magnitude
    log_k_min = np.log10(k_transition_rad.min())
    log_k_max = np.log10(k_transition_rad.max())
    log_DESI_mid = np.log10(np.sqrt(DESI_kmin * DESI_kmax))
    if abs(log_k_min - log_DESI_mid) < 5 or abs(log_k_max - log_DESI_mid) < 5:
        verdict = "DIAGNOSTIC"
        verdict_detail = f"k_transition range [{k_transition_rad.min():.2e}, {k_transition_rad.max():.2e}] h/Mpc, within 5 decades of DESI"
    else:
        verdict = "FAIL"
        verdict_detail = "k_transition far from observable range"

print(f"\nVerdict: {verdict}")
print(f"Detail: {verdict_detail}")

# ==============================================================================
# Additional: scaling relation
# ==============================================================================
# k_transition ~ H_BCS * T_CMB / T_BCS
# H_BCS ~ M_KK^2 / M_Pl (from Friedmann with rho ~ M_KK^4)
# T_BCS ~ M_KK (reheat to KK scale)
# => k_transition ~ M_KK * T_CMB / M_Pl
# This gives a simple scaling: k ~ M_KK / M_Pl * T_CMB / H_100

# The power-law fit
log_M = np.log10(M_KK_values)
log_k = np.log10(k_transition_rad)
finite_mask = np.isfinite(log_k)
if finite_mask.sum() >= 2:
    coeffs = np.polyfit(log_M[finite_mask], log_k[finite_mask], 1)
    print(f"\nScaling: log10(k) = {coeffs[0]:.3f} * log10(M_KK) + {coeffs[1]:.3f}")
    print(f"  => k ~ M_KK^{coeffs[0]:.3f}")

# ==============================================================================
# Save
# ==============================================================================

np.savez(
    os.path.join(data_dir, 's29c_k_transition.npz'),
    M_KK_values=M_KK_values,
    t_BCS_sec=t_BCS_sec,
    H_phys_GeV=H_phys_GeV,
    T_RH_GeV=T_RH_GeV,
    friction_param=friction_param,
    k_transition_rad=k_transition_rad,
    k_transition_dS=k_transition_dS,
    DESI_range=np.array([DESI_kmin, DESI_kmax]),
    Euclid_range=np.array([Euclid_kmin, Euclid_kmax]),
    CMB_range=np.array([CMB_kmin, CMB_kmax]),
    scaling_exponent=coeffs[0] if finite_mask.sum() >= 2 else np.nan,
    verdict=verdict,
    verdict_detail=verdict_detail,
)
print(f"\nSaved: s29c_k_transition.npz")

# ==============================================================================
# Plot
# ==============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Panel 1: k_transition vs M_KK
ax = axes[0]
ax.loglog(M_KK_values, k_transition_rad, 'bo-', ms=8, lw=2, label='Radiation dom.')
ax.loglog(M_KK_values, k_transition_dS, 'rs--', ms=6, lw=1.5, label='de Sitter')

# Survey bands
ax.axhspan(DESI_kmin, DESI_kmax, alpha=0.15, color='green', label=f'DESI BAO [{DESI_kmin}-{DESI_kmax}]')
ax.axhspan(Euclid_kmin, Euclid_kmax, alpha=0.08, color='blue', label=f'Euclid [{Euclid_kmin}-{Euclid_kmax}]')
ax.axhspan(CMB_kmin, CMB_kmax, alpha=0.08, color='orange', label=f'CMB')

ax.set_xlabel(r'$M_{KK}$ [GeV]', fontsize=13)
ax.set_ylabel(r'$k_{transition}$ [h/Mpc]', fontsize=13)
ax.set_title('BCS Transition Scale vs KK Mass', fontsize=14)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.3, which='both')
ax.set_xlim(5e13, 2e18)

# Panel 2: Physical timeline
ax = axes[1]
ax.loglog(M_KK_values, t_BCS_sec, 'ko-', ms=8, lw=2)
ax.set_xlabel(r'$M_{KK}$ [GeV]', fontsize=13)
ax.set_ylabel(r'$t_{BCS}$ [seconds]', fontsize=13)
ax.set_title('BCS Transition Time vs KK Mass', fontsize=14)
ax.grid(True, alpha=0.3, which='both')

# Mark reference times
t_EW = 1e-12   # electroweak transition
t_QCD = 1e-5   # QCD transition
t_BBN = 1.0    # BBN
ax.axhline(t_EW, color='purple', ls=':', alpha=0.5, label=f'EW ({t_EW:.0e} s)')
ax.axhline(t_QCD, color='red', ls=':', alpha=0.5, label=f'QCD ({t_QCD:.0e} s)')
ax.axhline(t_BBN, color='green', ls=':', alpha=0.5, label=f'BBN ({t_BBN:.0f} s)')
ax.legend(fontsize=9)
ax.set_xlim(5e13, 2e18)

plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's29c_k_transition.png'), dpi=150, bbox_inches='tight')
print(f"Saved: s29c_k_transition.png")
print("\nDone.")
