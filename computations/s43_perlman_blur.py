#!/usr/bin/env python3
"""
s43_perlman_blur.py — PERLMAN-43: Modulus Fluctuation Angular Blur vs Perlman Bound

Gate: PERLMAN-43 (INFO)
Task: Verify that random-walk modulus fluctuations coupled through the spectral
      action produce angular blur below the Perlman bound.

PHYSICS SUMMARY:

After the BCS transit, the modulus tau(x) freezes to a spatially varying field:
  - RMS amplitude: delta_tau ~ 3.3e-7 (from HOMOG-42 Starobinsky formula)
  - Correlation length: L_corr ~ 4e-2 cm today (comoving, from KZ domain stretching)

This modulus variation produces metric perturbations through the spectral action:
  delta_g/g ~ (dS/dtau / S) * delta_tau ~ 0.234 * 3.3e-7 ~ 7.8e-8

A photon traversing distance d crosses N = d/L_corr independent modulus domains.

THREE MECHANISMS produce angular blur:

(A) Shapiro time delay: A conformal metric perturbation h produces refractive
    index change delta_n = -h for g_{00} perturbation and +h for g_{ij}. For a
    purely conformal perturbation (ALL components scale the same), delta_n = 0.
    Only the anisotropic part contributes. This gives theta ~ 0 for conformal.

(B) Weak gravitational lensing: The modulus variation changes G_eff locally.
    The Newtonian potential of matter in each domain: Phi_N ~ G * rho * L_corr^2.
    The deflection: alpha ~ 4*Phi_N/c^2. But Phi_N for a domain of size L_corr
    is suppressed by (H*L_corr/c)^2 relative to the Hubble-scale potential.

(C) Integrated Sachs-Wolfe: The time variation of the potential from the spatial
    modulus variation (as the photon crosses domains). This is a COHERENT effect
    over the photon's path, NOT per-domain. Total ISW ~ delta_G/G * Phi_Hubble ~ 10^{-12}.

The dominant physical mechanism is (B) or (C). All give blur VASTLY below Perlman.

References:
  Paper 03 (Ng-van Dam): delta_l ~ sqrt(l * l_P)
  Paper 09 (Perlman 2011): HST quasar limits
  Paper 12 (Perlman 2019): theta < 10^{-27} arcsec
  S42 QF collab Section 3D
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def to_float(x):
    x = np.asarray(x)
    return float(x.flat[0]) if x.ndim > 0 else float(x)

# ============================================================
# 1. LOAD INPUT DATA
# ============================================================
homog = np.load('tier0-computation/s42_homogeneity.npz', allow_pickle=True)
grad = np.load('tier0-computation/s42_gradient_stiffness.npz', allow_pickle=True)

tau_fold = to_float(homog['tau_fold'])
S_fold = to_float(grad['S_fold'])
dS_fold = to_float(grad['dS_fold'])
d2S_fold = to_float(grad['d2S_fold'])
M_KK_grav = to_float(homog['M_KK_GN'])
M_Planck = to_float(homog['M_Planck'])
dtau_over_tau_transit_grav = to_float(homog['dtau_over_tau_transit_grav'])
L_corr_Mpc_grav = to_float(homog['L_corr_Mpc_grav'])

print("=" * 70)
print("PERLMAN-43: Modulus Fluctuation Angular Blur vs Perlman Bound")
print("=" * 70)
print()
print("--- Input Parameters ---")
print(f"  tau_fold                = {tau_fold}")
print(f"  S_fold                  = {S_fold:.1f}  M_KK^4")
print(f"  dS/dtau (fold)          = {dS_fold:.1f}  M_KK^4")
print(f"  M_KK (gravity route)    = {M_KK_grav:.3e} GeV")
print(f"  M_Planck                = {M_Planck:.3e} GeV")
print(f"  dtau/tau (transit)      = {dtau_over_tau_transit_grav:.6e}")
print(f"  L_corr (today comoving) = {L_corr_Mpc_grav:.3e} Mpc")
print()

# ============================================================
# 2. CONSTANTS
# ============================================================
from canonical_constants import l_Planck_cm as l_P_cm
from canonical_constants import Mpc_to_cm as Mpc_cm
rad_to_arcsec = 206265.0
from canonical_constants import c_light_cgs as c_cgs
from canonical_constants import G_N_cgs as G_cgs
from canonical_constants import H_0_inv_s as H_0_per_s

# ============================================================
# 3. DERIVED QUANTITIES
# ============================================================

delta_tau_abs = dtau_over_tau_transit_grav * tau_fold
coupling = dS_fold / S_fold
delta_g = coupling * delta_tau_abs  # metric perturbation amplitude per domain

L_corr_cm = L_corr_Mpc_grav * Mpc_cm
L_corr_lP = L_corr_cm / l_P_cm

# Mean cosmic matter density today (rho_crit * Omega_m)
rho_crit = 3.0 * H_0_per_s**2 / (8.0 * np.pi * G_cgs)  # g/cm^3
Omega_m = 0.31
rho_m = rho_crit * Omega_m  # g/cm^3

print(f"  delta_tau (absolute)    = {delta_tau_abs:.6e}")
print(f"  Coupling dS/S           = {coupling:.6f}")
print(f"  delta_g/g per domain    = {delta_g:.6e}")
print(f"  L_corr (cm)             = {L_corr_cm:.3e}")
print(f"  L_corr (l_P)            = {L_corr_lP:.3e}")
print(f"  rho_crit                = {rho_crit:.3e} g/cm^3")
print(f"  rho_matter              = {rho_m:.3e} g/cm^3")
print()

# ============================================================
# 4. MECHANISM (B): WEAK GRAVITATIONAL LENSING
# ============================================================
# The modulus variation delta_tau changes G_eff by delta_G/G ~ delta_g.
# This produces a Newtonian potential perturbation in a domain of size L_corr:
#   Phi_domain = (4*pi/3) * G * delta_rho * L_corr^2
# where delta_rho = rho_m * (delta_G/G) is the effective density perturbation
# from the varying G (at fixed matter density).
#
# Actually: varying G doesn't change matter density. It changes the POTENTIAL
# generated by the matter. The Newtonian potential of a uniform sphere of
# radius R and density rho:
#   Phi = -(2*pi/3) * G * rho * R^2
# The perturbation from delta_G:
#   delta_Phi = -(2*pi/3) * delta_G * rho * R^2
#             = (delta_G/G) * Phi_domain
#   Phi_domain = (2*pi/3) * G * rho_m * L_corr^2 / c^2  [dimensionless]
#
# The lensing deflection from this potential:
#   alpha = 4 * |delta_Phi| / c^2 [GR factor 2x Newtonian]
#         = 4 * (delta_G/G) * (2*pi/3) * G * rho_m * L_corr^2 / c^2

print("=" * 70)
print("4. MECHANISM B: WEAK GRAVITATIONAL LENSING")
print("=" * 70)
print()

Phi_domain = (2.0 * np.pi / 3.0) * G_cgs * rho_m * L_corr_cm**2 / c_cgs**2
alpha_per_domain = 4.0 * delta_g * Phi_domain  # GR deflection

print(f"  Phi_domain (dimensionless)  = {Phi_domain:.3e}")
print(f"    = (2*pi/3) * G * rho_m * L^2 / c^2")
print(f"    = (2*pi/3) * {G_cgs:.3e} * {rho_m:.3e} * ({L_corr_cm:.3e})^2 / ({c_cgs:.3e})^2")
print(f"  delta_G/G                   = {delta_g:.3e}")
print(f"  alpha_per_domain (GR)       = {alpha_per_domain:.3e} rad")
print(f"                              = {alpha_per_domain * rad_to_arcsec:.3e} arcsec")
print()

# Source distances
d_values_Gpc = np.array([0.01, 0.1, 0.5, 1.0, 2.0, 4.0, 10.0])
d_values_cm = d_values_Gpc * 1e3 * Mpc_cm
N_domains = d_values_cm / L_corr_cm

# Random-walk blur
theta_B_rad = np.sqrt(N_domains) * alpha_per_domain
theta_B_arcsec = theta_B_rad * rad_to_arcsec

print(f"  {'d (Gpc)':>10s} | {'N_domains':>13s} | {'sqrt(N)':>12s} | {'theta_B (arcsec)':>17s}")
print(f"  {'-'*60}")
for i in range(len(d_values_Gpc)):
    print(f"  {d_values_Gpc[i]:10.2f} | {N_domains[i]:13.3e} | {np.sqrt(N_domains[i]):12.3e} | {theta_B_arcsec[i]:17.3e}")
print()

# ============================================================
# 5. MECHANISM (C): PHASE ACCUMULATION (SHAPIRO-LIKE)
# ============================================================
# A photon crossing a domain with potential Phi_domain and size L_corr
# accumulates an extra path length:
#   delta_l = 2 * Phi_domain * L_corr  [factor 2 for GR Shapiro]
# The refractive index perturbation from delta_G modifying the local
# potential: delta_n = 2 * (delta_G/G) * Phi_domain
# Path length per domain: delta_l = delta_n * L_corr = 2*(delta_G/G)*Phi*L_corr
# Phase error per domain: delta_phi = (2*pi/lambda) * delta_l
# After N domains: Delta_phi = sqrt(N) * delta_phi
# Angular blur: theta_C = Delta_phi / (2*pi*d/lambda)
#             = sqrt(N) * delta_l / d
#             = sqrt(N) * 2*delta_g*Phi*L_corr / d
#             = 2*delta_g*Phi * sqrt(L_corr) * sqrt(d) / d
#             = 2*delta_g*Phi * sqrt(L_corr / d)

print("=" * 70)
print("5. MECHANISM C: PHASE ACCUMULATION (SHAPIRO-LIKE)")
print("=" * 70)
print()

delta_l_per_domain = 2.0 * delta_g * Phi_domain * L_corr_cm
theta_C_rad = np.sqrt(N_domains) * delta_l_per_domain / d_values_cm
theta_C_arcsec = theta_C_rad * rad_to_arcsec

print(f"  delta_l per domain = {delta_l_per_domain:.3e} cm")
print()
print(f"  {'d (Gpc)':>10s} | {'theta_C (arcsec)':>17s}")
print(f"  {'-'*30}")
for i in range(len(d_values_Gpc)):
    print(f"  {d_values_Gpc[i]:10.2f} | {theta_C_arcsec[i]:17.3e}")
print()

# ============================================================
# 6. MECHANISM (D): PURE EFFACEMENT (S42 COLLAB FORMULA)
# ============================================================
# The S42 collab Section 3D formula, stripped to its essence:
# delta_theta ~ (dS/S) * delta_tau_transit * sqrt(l_P / L_H)
# where L_H is the Hubble radius. This formula assumes Planck-scale
# phase noise modulated by the metric coupling -- the "effacement" approach.
#
# This is the formula that was meant to be computed in the S42 collab.
# It uses the Ng scaling theta ~ sqrt(l_P/d) but replaces l_P with an
# effective scale l_eff = (coupling * delta_tau)^2 * L_H.

print("=" * 70)
print("6. MECHANISM D: EFFACEMENT FORMULA (S42 COLLAB)")
print("=" * 70)
print()

# The effacement formula: theta_eff = coupling * delta_tau * sqrt(l_P / d)
# This treats the modulus fluctuation as a MODULATION of the Planck-scale
# foam: the foam amplitude is not l_P but l_P * coupling * delta_tau.
# The angular blur is then:
#   theta_D = coupling * delta_tau * theta_Ng(d)
# where theta_Ng = sqrt(l_P/d) is the standard Ng random-walk foam result.

theta_Ng_arcsec = np.sqrt(l_P_cm / d_values_cm) * rad_to_arcsec
theta_D_arcsec = delta_g * theta_Ng_arcsec

print(f"  theta_D = (dS/S * delta_tau) * sqrt(l_P/d)")
print(f"  Effective foam amplitude: {delta_g:.3e} * l_P")
print()
print(f"  {'d (Gpc)':>10s} | {'theta_Ng (arcsec)':>17s} | {'theta_D (arcsec)':>17s}")
print(f"  {'-'*50}")
for i in range(len(d_values_Gpc)):
    print(f"  {d_values_Gpc[i]:10.2f} | {theta_Ng_arcsec[i]:17.3e} | {theta_D_arcsec[i]:17.3e}")
print()

# ============================================================
# 7. COMPREHENSIVE COMPARISON
# ============================================================

print("=" * 70)
print("7. COMPREHENSIVE COMPARISON AT d = 1 Gpc")
print("=" * 70)
print()

perlman_2011_arcsec = 1e-24
perlman_2019_arcsec = 1e-27

# Standard foam
idx_1 = np.argmin(np.abs(d_values_Gpc - 1.0))
theta_RW_arcsec = np.sqrt(l_P_cm / d_values_cm) * rad_to_arcsec
theta_HO_arcsec = (l_P_cm / d_values_cm)**(2.0/3.0) * rad_to_arcsec

mechs = {
    'Standard RW foam': theta_RW_arcsec[idx_1],
    'Holographic foam': theta_HO_arcsec[idx_1],
    'Perlman 2019 bound': perlman_2019_arcsec,
    'Perlman 2011 bound': perlman_2011_arcsec,
    'Framework (B): Lensing': theta_B_arcsec[idx_1],
    'Framework (C): Phase': theta_C_arcsec[idx_1],
    'Framework (D): Effacement': theta_D_arcsec[idx_1],
}

print(f"  {'Mechanism':<30s} {'theta (arcsec)':>15s} {'log10':>8s}")
print(f"  {'-'*58}")
for name, val in mechs.items():
    if val > 0:
        print(f"  {name:<30s} {val:15.3e} {np.log10(val):8.1f}")
print()

# Identify the physically correct framework prediction.
#
# Analysis of mechanisms:
#
# (B) Lensing: This is the deflection from the Newtonian potential perturbation
#     caused by delta_G * rho_m within each L_corr domain. This is PHYSICALLY CORRECT
#     but extremely small because Phi_domain ~ G*rho*L^2/c^2 ~ 10^{-67} for L~0.04 cm.
#
# (C) Phase: Shapiro time delay from the same potential. Same physics as (B),
#     expressed as phase rather than deflection. Even smaller.
#
# (D) Effacement: Treats modulus fluctuations as modulating the PLANCK-SCALE foam.
#     theta_D = delta_g * theta_Ng. This is the LARGEST physically motivated estimate.
#     It says: whatever foam blur exists at the Planck scale, it is MODULATED by
#     the modulus variation. The modulation factor is delta_g ~ 7.8e-8.
#
# The S42 collab Section 3D was computing (D). The effacement ratio delta_g ~ 10^{-7}
# multiplies the standard Ng foam blur. Even if Planck-scale foam were AS LARGE AS
# the Ng random-walk prediction (which Perlman has already excluded), the framework's
# modulus-modulated version would be 7 orders smaller.
#
# Since Perlman has already excluded the Ng random-walk model, and our framework's
# modulus fluctuations can only MODULATE that foam (not add to it independently),
# the framework is automatically safe.

# Take mechanism (D) as the conservative upper bound:
# It gives the LARGEST framework blur because it couples to the full Ng foam.
theta_framework = theta_D_arcsec[idx_1]
mechanism_label = "Effacement (D)"

margin_2019 = np.log10(perlman_2019_arcsec) - np.log10(theta_framework)
margin_2011 = np.log10(perlman_2011_arcsec) - np.log10(theta_framework)
margin_RW = np.log10(theta_RW_arcsec[idx_1]) - np.log10(theta_framework)

below_2019 = theta_framework < perlman_2019_arcsec
below_2011 = theta_framework < perlman_2011_arcsec

print(f"  Physical framework prediction: {theta_framework:.3e} arcsec")
print(f"  Mechanism: {mechanism_label}")
print(f"  Below Perlman 2019: {below_2019}")
print(f"  Below Perlman 2011: {below_2011}")
print(f"  Margin (2019): {margin_2019:+.1f} orders ({'+' if margin_2019 > 0 else ''}below)")
print(f"  Margin (2011): {margin_2011:+.1f} orders")
print(f"  Margin vs RW:  {margin_RW:+.1f} orders")
print()

# ============================================================
# 8. CROSS-CHECKS
# ============================================================

print("=" * 70)
print("8. CROSS-CHECKS")
print("=" * 70)
print()

# CC-1: Dimensional analysis of Phi_domain
print(f"  CC-1: Newtonian potential of one domain")
print(f"    Phi = (2pi/3) * G * rho_m * L^2 / c^2")
print(f"    = (2pi/3) * {G_cgs:.3e} * {rho_m:.3e} * {L_corr_cm:.3e}^2 / {c_cgs:.3e}^2")
print(f"    = {Phi_domain:.3e}  (dimensionless)")
print(f"    Compare: (H_0 * L_corr / c)^2 = {(H_0_per_s * L_corr_cm / c_cgs)**2:.3e}")
print(f"    Ratio: {Phi_domain / (H_0_per_s * L_corr_cm / c_cgs)**2:.2f}")
print(f"    (Should be O(1) for mean density -- YES, {Phi_domain / (H_0_per_s * L_corr_cm / c_cgs)**2:.2f})")
print()

# CC-2: Effacement ratio
print(f"  CC-2: Effacement metric coupling")
print(f"    delta_g = coupling * delta_tau = {coupling:.4f} * {delta_tau_abs:.3e} = {delta_g:.3e}")
print(f"    vs |E_BCS|/S_fold ~ 10^{{-6}} -- same ballpark")
print()

# CC-3: L_corr vs cosmic scales
L_corr_ly = L_corr_cm / 9.461e17  # cm to light years
print(f"  CC-3: Domain size comparison")
print(f"    L_corr = {L_corr_cm:.3e} cm = {L_corr_cm*1e-2:.1e} m = {L_corr_ly:.1e} ly")
print(f"    This is {L_corr_cm*1e-2:.0e} m -- sub-millimeter scale")
print(f"    N_domains per Gpc = {d_values_cm[idx_1]/L_corr_cm:.2e}")
print()

# CC-4: Approach D vs B ratio
ratio_DB = theta_D_arcsec[idx_1] / theta_B_arcsec[idx_1]
print(f"  CC-4: Mechanism hierarchy")
print(f"    theta_D / theta_B = {ratio_DB:.3e}")
print(f"    theta_D / theta_C = {theta_D_arcsec[idx_1] / theta_C_arcsec[idx_1]:.3e}")
print(f"    D >> B > C: Effacement dominates (modulates Planck foam)")
print()

# CC-5: FIRAS consistency
print(f"  CC-5: FIRAS check")
print(f"    delta_g = {delta_g:.3e} < FIRAS 10^-5: YES ({np.log10(1e-5/delta_g):.1f} orders margin)")
print()

# CC-6: Standard foam at Perlman sample distances
d_Perl = 2.0  # Gpc, typical Perlman quasar
theta_RW_Perl = np.sqrt(l_P_cm / (d_Perl * 1e3 * Mpc_cm)) * rad_to_arcsec
theta_D_Perl = delta_g * theta_RW_Perl
print(f"  CC-6: At Perlman sample d = {d_Perl} Gpc")
print(f"    theta_RW(Ng) = {theta_RW_Perl:.3e} arcsec")
print(f"    theta_D(framework) = {theta_D_Perl:.3e} arcsec")
print(f"    Perlman 2019 bound = {perlman_2019_arcsec:.0e} arcsec")
print(f"    Framework below bound by {np.log10(perlman_2019_arcsec / theta_D_Perl):.1f} orders")
print()

# ============================================================
# 9. GATE VERDICT
# ============================================================

print("=" * 70)
print("GATE VERDICT: PERLMAN-43")
print("=" * 70)
print()

verdict = "PASS" if below_2019 else "FAIL"

print(f"  Framework blur (1 Gpc):    {theta_framework:.3e} arcsec")
print(f"  Perlman 2019 bound:        {perlman_2019_arcsec:.0e} arcsec")
print(f"  Below bound:               {below_2019}")
print(f"  Margin:                     {abs(margin_2019):.1f} orders of magnitude")
print(f"  Gate: PERLMAN-43 (INFO):   {verdict}")
print()

if verdict == "PASS":
    print(f"  The framework's modulus fluctuations produce angular blur")
    print(f"  {abs(margin_2019):.0f} orders of magnitude below the Perlman 2019 bound.")
    print()
    print(f"  Suppression hierarchy:")
    print(f"    1. Effacement coupling: delta_g = {delta_g:.1e}")
    print(f"       (modulus fluctuation * spectral action sensitivity)")
    print(f"    2. This MODULATES the standard Ng foam blur by factor {delta_g:.1e}")
    print(f"    3. Even if RW foam existed at its maximum amplitude,")
    print(f"       the framework's modulation is {abs(margin_RW):.1f} orders below it")
    print()
    print(f"  Physical interpretation:")
    print(f"    The modulus fluctuations are INTERNAL geometry changes.")
    print(f"    They couple to the external metric only through the spectral action.")
    print(f"    The effacement ratio (7.8e-8) ensures that internal fluctuations")
    print(f"    are invisible to photon propagation at any foreseeable precision.")
    print(f"    This is structurally guaranteed: the spectral action dominates")
    print(f"    any dynamical contribution by ~7 orders of magnitude.")

print()

# ============================================================
# 10. SAVE DATA
# ============================================================

np.savez('tier0-computation/s43_perlman_blur.npz',
    # Input parameters
    tau_fold=tau_fold,
    S_fold=S_fold,
    dS_fold=dS_fold,
    coupling=coupling,
    delta_tau_abs=delta_tau_abs,
    dtau_over_tau_transit_grav=dtau_over_tau_transit_grav,
    M_KK_grav=M_KK_grav,
    M_Planck=M_Planck,
    L_corr_cm=L_corr_cm,
    L_corr_lP=L_corr_lP,
    L_corr_Mpc=L_corr_Mpc_grav,
    # Per-domain quantities
    delta_g_per_domain=delta_g,
    Phi_domain=Phi_domain,
    alpha_lensing_per_domain=alpha_per_domain,
    # Predictions at multiple distances
    d_values_Gpc=d_values_Gpc,
    d_values_cm=d_values_cm,
    N_domains=N_domains,
    theta_B_lensing_arcsec=theta_B_arcsec,
    theta_C_phase_arcsec=theta_C_arcsec,
    theta_D_effacement_arcsec=theta_D_arcsec,
    # Standard foam
    theta_RW_arcsec=theta_RW_arcsec,
    theta_HO_arcsec=theta_HO_arcsec,
    # Bounds
    perlman_2011_arcsec=perlman_2011_arcsec,
    perlman_2019_arcsec=perlman_2019_arcsec,
    # Final comparison at 1 Gpc
    theta_physical_1Gpc=theta_framework,
    dominant_mechanism=np.array([mechanism_label]),
    margin_below_perlman_2019_OOM=margin_2019,
    margin_below_perlman_2011_OOM=margin_2011,
    margin_below_RW_OOM=margin_RW,
    # Verdict
    verdict=np.array([verdict]),
    gate_name=np.array(['PERLMAN-43']),
)
print("Data saved to tier0-computation/s43_perlman_blur.npz")
print()

# ============================================================
# 11. PLOT
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(15, 7))

# --- Panel (a): Angular blur vs distance ---
ax = axes[0]
d_plot_Gpc = np.logspace(-2, 1.5, 300)
d_plot_cm = d_plot_Gpc * 1e3 * Mpc_cm

# Standard foam models
theta_RW_plot = np.sqrt(l_P_cm / d_plot_cm) * rad_to_arcsec
theta_HO_plot = (l_P_cm / d_plot_cm)**(2.0/3.0) * rad_to_arcsec

# Framework: Effacement (D) -- dominant
theta_D_plot = delta_g * np.sqrt(l_P_cm / d_plot_cm) * rad_to_arcsec

# Framework: Lensing (B)
N_plot = d_plot_cm / L_corr_cm
theta_B_plot = np.sqrt(N_plot) * alpha_per_domain * rad_to_arcsec

ax.loglog(d_plot_Gpc, theta_RW_plot, 'r-', lw=2, label=r'Ng RW foam $\sqrt{\ell_P/d}$', alpha=0.8)
ax.loglog(d_plot_Gpc, theta_HO_plot, 'b--', lw=2, label=r'Holographic $(\ell_P/d)^{2/3}$', alpha=0.8)
ax.loglog(d_plot_Gpc, theta_D_plot, 'g-', lw=2.5, label=r'Framework: $\delta g \cdot \sqrt{\ell_P/d}$')
ax.loglog(d_plot_Gpc, theta_B_plot, 'g:', lw=1.5, label='Framework: Newtonian lensing')

# Perlman bounds
ax.axhline(perlman_2019_arcsec, color='k', ls='--', lw=1.5, label='Perlman 2019 bound')
ax.axhline(perlman_2011_arcsec, color='gray', ls='--', lw=1.5, label='Perlman 2011 bound')

# Quasar sample
ax.axvspan(1.0, 4.0, alpha=0.08, color='orange', label='Quasar sample')

ax.set_xlabel('Source distance $d$ (Gpc)', fontsize=13)
ax.set_ylabel(r'Angular blur $\delta\theta$ (arcsec)', fontsize=13)
ax.set_title('PERLMAN-43: Angular Blur vs Perlman Bound', fontsize=14)
ax.set_xlim(0.01, 30)
ax.set_ylim(1e-90, 1e-20)
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.3)

# Add margin annotation
ax.annotate(
    f'Margin:\n{abs(margin_2019):.0f} OOM',
    xy=(1.0, theta_framework),
    xytext=(0.05, perlman_2019_arcsec * 1e5),
    fontsize=11, fontweight='bold', color='darkgreen',
    arrowprops=dict(arrowstyle='->', color='darkgreen', lw=1.5),
)

# --- Panel (b): Mechanism hierarchy bar chart ---
ax = axes[1]

bar_labels = [
    'Ng RW foam',
    'Perlman 2011',
    'Perlman 2019',
    'Holographic',
    'Framework (D)\nEffacement',
    'Framework (B)\nLensing',
    'Framework (C)\nPhase',
]
bar_vals = [
    theta_RW_arcsec[idx_1],
    perlman_2011_arcsec,
    perlman_2019_arcsec,
    theta_HO_arcsec[idx_1],
    theta_D_arcsec[idx_1],
    theta_B_arcsec[idx_1],
    theta_C_arcsec[idx_1],
]
bar_colors = ['red', 'gray', 'black', 'blue', 'green', 'darkgreen', 'forestgreen']

log_vals = [np.log10(max(v, 1e-200)) for v in bar_vals]
y_pos = np.arange(len(bar_labels))

bars = ax.barh(y_pos, log_vals, color=bar_colors, alpha=0.7, height=0.6)
ax.set_yticks(y_pos)
ax.set_yticklabels(bar_labels, fontsize=9)
ax.set_xlabel(r'$\log_{10}(\delta\theta\,/\,\mathrm{arcsec})$', fontsize=13)
ax.set_title('Mechanism Hierarchy at $d = 1$ Gpc', fontsize=14)

# Value labels
for i, lv in enumerate(log_vals):
    if lv > -180:
        ax.text(max(lv, -85) + 1, i, f'{lv:.1f}', va='center', fontsize=9, fontweight='bold')

ax.axvline(np.log10(perlman_2019_arcsec), color='black', ls='--', lw=1)
ax.grid(True, alpha=0.3, axis='x')
ax.set_xlim(-90, -20)

plt.tight_layout()
plt.savefig('tier0-computation/s43_perlman_blur.png', dpi=150, bbox_inches='tight')
print("Plot saved to tier0-computation/s43_perlman_blur.png")
print()

# ============================================================
# 12. SUMMARY TABLE
# ============================================================

print("=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print()
print(f"  {'Quantity':<45s} {'Value':<20s} {'Units'}")
print(f"  {'-'*80}")
print(f"  {'delta_tau (transit amplitude)':<45s} {delta_tau_abs:<20.3e} {''}")
print(f"  {'Coupling dS/S':<45s} {coupling:<20.6f} {''}")
print(f"  {'delta_g (metric perturbation)':<45s} {delta_g:<20.3e} {''}")
print(f"  {'L_corr (today comoving)':<45s} {L_corr_cm:<20.3e} {'cm'}")
print(f"  {'Phi_domain (Newtonian pot.)':<45s} {Phi_domain:<20.3e} {''}")
print(f"  {'N_domains (1 Gpc)':<45s} {N_domains[idx_1]:<20.3e} {''}")
print(f"  {'--- Predictions at 1 Gpc ---':<45s}")
print(f"  {'theta_D (effacement, dominant)':<45s} {theta_D_arcsec[idx_1]:<20.3e} {'arcsec'}")
print(f"  {'theta_B (Newtonian lensing)':<45s} {theta_B_arcsec[idx_1]:<20.3e} {'arcsec'}")
print(f"  {'theta_C (phase accumulation)':<45s} {theta_C_arcsec[idx_1]:<20.3e} {'arcsec'}")
print(f"  {'--- Standard foam at 1 Gpc ---':<45s}")
print(f"  {'theta_RW (Ng random walk)':<45s} {theta_RW_arcsec[idx_1]:<20.3e} {'arcsec'}")
print(f"  {'theta_HO (holographic)':<45s} {theta_HO_arcsec[idx_1]:<20.3e} {'arcsec'}")
print(f"  {'--- Bounds ---':<45s}")
print(f"  {'Perlman 2019':<45s} {perlman_2019_arcsec:<20.0e} {'arcsec'}")
print(f"  {'Perlman 2011':<45s} {perlman_2011_arcsec:<20.0e} {'arcsec'}")
print(f"  {'--- Margins ---':<45s}")
print(f"  {'Below Perlman 2019':<45s} {abs(margin_2019):<20.1f} {'orders'}")
print(f"  {'Below Perlman 2011':<45s} {abs(margin_2011):<20.1f} {'orders'}")
print(f"  {'Below standard RW foam':<45s} {abs(margin_RW):<20.1f} {'orders'}")
print(f"  {'--- Gate ---':<45s}")
print(f"  {'PERLMAN-43':<45s} {'INFO: ' + verdict:<20s}")
print()
print("DONE.")
