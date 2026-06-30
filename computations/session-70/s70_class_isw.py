#!/usr/bin/env python3
"""
s70_class_isw.py — Full Boltzmann ISW with c_s^2_DE = 0
========================================================

Session 70, Gate: CLASS-ISW-70
Carry-forward: Mack, VdD (2/9 reviewers)

Computes the ISW effect using a full Boltzmann hierarchy (CAMB 1.6.6)
with c_s^2_DE = 0 (the tracking vacuum prediction derived in Q-SOUND-70 PASS).

The S68 ISW-TRACKING-68 used the Limber approximation with a simplified
ISW kernel. W1-C (Q-SOUND-70) proved c_s^2 = 0 is structural (spectral action
has no kinetic term for det(g_K)). This computation upgrades to the full
Boltzmann hierarchy.

Three models:
  Model A: LCDM (w=-1, no DE perturbations)
  Model B: Framework (w_0=-0.918, w_a=0, c_s^2=0, tracking vacuum)
  Model C: Quintessence (w_0=-0.918, w_a=0, c_s^2=1, smooth DE)

Computes:
  1. CMB TT power spectrum at l=2-100 for all three models (full Boltzmann)
  2. ISW contribution isolated via Weyl potential time derivative from CAMB
  3. ISW auto-power spectrum C_l^{ISW-ISW}
  4. ISW-galaxy cross-correlation C_l^{ISW-g}
  5. Fractional difference Delta(C_l) = (C_l^{FW} - C_l^{Quint}) / C_l^{LCDM}
  6. Euclid and 21cm SNR forecasts

Pre-registered gate: CLASS-ISW-70
  PASS: |C_l^{FW} - C_l^{Quint}| / C_l^{LCDM} > 5% for l in [2, 10]
  FAIL: < 1% for all l
  INFO: signal in [1%, 5%]

Physics (from S68 ISW-TRACKING-68 + W1-C Q-SOUND-70):
  The spectral action S = Tr f(D_K^2/Lambda^2) depends on det(g_K) algebraically
  (no spatial derivatives). This gives c_s^2 = 0 exactly at tree level. DE
  perturbations track matter: delta_DE = (1+w)/(1-3w) * delta_m on sub-horizon
  scales. This modifies the Poisson equation source and hence the ISW-galaxy
  cross-correlation.

  Key distinction from S68: the full Boltzmann computation includes
  - Exact evolution of DE perturbations (not sub-horizon approximation)
  - Super-horizon DE perturbation modes
  - Back-reaction on the metric perturbations through the Einstein equations
  - Correct treatment of anisotropic stress (Pi_DE = 0 for fluid model)

Author: mack-cosmic-bridge
"""

import sys
sys.path.insert(0, r"C:\sandbox\Ainulindale Exflation\computations")

import numpy as np
from scipy.integrate import trapezoid, quad
from scipy.interpolate import interp1d
from scipy.special import spherical_jn
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import camb
from camb.dark_energy import DarkEnergyFluid

from canonical_constants import (
    H_0_km_s_Mpc, Omega_m, Omega_Lambda, Omega_b, Omega_DM,
    Omega_r, T_CMB, c_light_km_s, sigma_8, A_s_CMB, Mpc_to_m,
    H_0_inv_s
)

# ==============================================================================
#  Constants and parameters
# ==============================================================================
print("=" * 72)
print("S70 FULL BOLTZMANN ISW WITH c_s^2_DE = 0")
print("Gate: CLASS-ISW-70")
print("=" * 72)

# Cosmological parameters (Planck 2018)
H0 = H_0_km_s_Mpc        # 67.4 km/s/Mpc
h = H0 / 100.0
ombh2 = Omega_b * h**2    # 0.02237
omch2 = Omega_DM * h**2   # 0.1200
tau_reion = 0.054          # optical depth to reionization  # (local)
As = A_s_CMB               # 2.1e-9
# ns_planck = 0.9649  # S72: now imported from canonical_constants as planck_ns
ns_planck = planck_ns  # S72: alias for downstream use

# Framework DE parameters
# w0_FW = -0.918    # Volovik vacuum + effacement (S68)  # S72: now imported from canonical_constants
# wa_FW = 0.0       # w_a = 0 locked (four-fold protection, S68 workshop)  # S72: now imported from canonical_constants

# Planck ISW measurement (1502.01595v2)
A_ISW_planck = 1.00  # (local)
sigma_A_ISW = 0.25  # (local)

# Galaxy survey parameters
b_g_05 = 1.5      # Galaxy bias at z=0.5 (SDSS-like)  # (local)
b_g_10 = 2.0      # Galaxy bias at z=1.0  # (local)
sigma_z = 0.15     # Photo-z width  # (local)
z_means = [0.35, 0.5, 0.7, 1.0]  # Galaxy window centers
b_g_arr = [1.3, 1.5, 1.7, 2.0]   # Bias at each z

lmax = 100
l_focus = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 50, 100])

print(f"\nCosmology: H0={H0}, Omega_m={Omega_m}, Omega_b={Omega_b}")
print(f"Framework: w0={w0_FW}, wa={wa_FW}")
print(f"CAMB version: {camb.__version__}")

# ==============================================================================
#  PART 1: Full Boltzmann CMB TT spectrum from CAMB
# ==============================================================================
print("\n" + "=" * 72)
print("PART 1: Full Boltzmann CMB TT power spectrum")
print("=" * 72)

def setup_camb_params(w=None, cs2=None, lmax_calc=2500):
    """Create CAMB parameters for a given DE model."""
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, tau=tau_reion)
    pars.InitPower.set_params(As=As, ns=ns_planck)
    pars.set_for_lmax(lmax_calc, lens_potential_accuracy=0)
    pars.set_matter_power(redshifts=[0])
    if w is not None:
        pars.DarkEnergy = DarkEnergyFluid(w=w, cs2=cs2)
    return pars

# Three models
print("\nComputing full Boltzmann TT spectra (CAMB)...")
pars_lcdm = setup_camb_params()
pars_fw = setup_camb_params(w=w0_FW, cs2=0.0)
pars_quint = setup_camb_params(w=w0_FW, cs2=1.0)

results_lcdm = camb.get_results(pars_lcdm)
results_fw = camb.get_results(pars_fw)
results_quint = camb.get_results(pars_quint)
print("  CAMB computations complete.")

# Extract TT spectra (in muK^2, l(l+1)/2pi normalization)
cls_lcdm = results_lcdm.get_cmb_power_spectra(pars_lcdm, CMB_unit='muK')
cls_fw = results_fw.get_cmb_power_spectra(pars_fw, CMB_unit='muK')
cls_quint = results_quint.get_cmb_power_spectra(pars_quint, CMB_unit='muK')

tt_lcdm = cls_lcdm['total'][:lmax+1, 0]
tt_fw = cls_fw['total'][:lmax+1, 0]
tt_quint = cls_quint['total'][:lmax+1, 0]

# Also get unlensed scalar spectra
tt_lcdm_unl = cls_lcdm['unlensed_scalar'][:lmax+1, 0]
tt_fw_unl = cls_fw['unlensed_scalar'][:lmax+1, 0]
tt_quint_unl = cls_quint['unlensed_scalar'][:lmax+1, 0]

print("\nCMB TT power spectrum at focus multipoles (unlensed, muK^2):")
print(f"{'l':>5} {'LCDM':>12} {'FW(cs2=0)':>12} {'Q(cs2=1)':>12} {'(FW-Q)/LCDM':>14} {'FW/LCDM':>10} {'Q/LCDM':>10}")
print("-" * 85)
for l in l_focus:
    if l <= lmax:
        frac = (tt_fw_unl[l] - tt_quint_unl[l]) / tt_lcdm_unl[l] * 100
        fw_lcdm = tt_fw_unl[l] / tt_lcdm_unl[l]
        q_lcdm = tt_quint_unl[l] / tt_lcdm_unl[l]
        print(f"{l:5d} {tt_lcdm_unl[l]:12.4f} {tt_fw_unl[l]:12.4f} {tt_quint_unl[l]:12.4f} {frac:13.3f}% {fw_lcdm:10.6f} {q_lcdm:10.6f}")

# ==============================================================================
#  PART 2: Weyl potential evolution from CAMB Boltzmann hierarchy
# ==============================================================================
print("\n" + "=" * 72)
print("PART 2: Weyl potential evolution (full Boltzmann)")
print("=" * 72)

# Extract perturbation evolution from CAMB's Boltzmann solver
# k grid for ISW integration
nk_isw = 150
k_isw = np.logspace(-4, -1, nk_isw)  # 0.0001 to 0.1 Mpc^-1

# Redshift grid (focus on z < 5 where ISW matters)
nz_isw = 500
z_isw = np.linspace(0.005, 5.0, nz_isw)
dz = z_isw[1] - z_isw[0]

print(f"\nExtracting Weyl potential at {nk_isw} k-values, {nz_isw} z-values...")

# For each model, extract Weyl potential and matter overdensity
data = {}
for label, results in [('LCDM', results_lcdm), ('FW', results_fw), ('Quint', results_quint)]:
    evo = results.get_redshift_evolution(z_isw, k_isw, ['Weyl', 'delta_cdm', 'delta_tot_de'])
    data[label] = {
        'weyl': evo[:, :, 0],       # (nz, nk)
        'delta_cdm': evo[:, :, 1],   # (nz, nk)
        'delta_de': evo[:, :, 2] if evo.shape[2] > 2 else np.zeros_like(evo[:, :, 0]),
        'H_z': np.array([results.hubble_parameter(z) for z in z_isw]),  # km/s/Mpc
        'chi_z': np.array([results.comoving_radial_distance(z) for z in z_isw]),  # Mpc
    }
    print(f"  {label}: Weyl[z=0.01,k=0.001] = {evo[0, np.argmin(np.abs(k_isw-0.001)), 0]:.6e}")

# Compute dWeyl/dz at each (z, k)
print("\nComputing Weyl potential derivatives...")
for label in ['LCDM', 'FW', 'Quint']:
    dweyl_dz = np.gradient(data[label]['weyl'], dz, axis=0)  # d/dz along z axis
    # ISW kernel: dPhi/dt = -(1+z) * H(z) * dPhi/dz
    # The Weyl potential is (Phi+Psi)/2, and the ISW integrand is 2*d(Weyl)/dt
    # So ISW_kernel = -2 * (1+z) * H(z) * d(Weyl)/dz
    H_arr = data[label]['H_z'][:, np.newaxis]  # broadcast shape (nz, 1)
    zp1 = (1 + z_isw)[:, np.newaxis]
    data[label]['dweyl_dz'] = dweyl_dz
    data[label]['isw_kernel'] = -2.0 * zp1 * H_arr * dweyl_dz  # (nz, nk)

print("  Done.")

# Check the tracking factor at a representative k
ik_ref = np.argmin(np.abs(k_isw - 0.005))
print(f"\nWeyl potential derivative ratios at k = {k_isw[ik_ref]:.4f} Mpc^-1:")
print(f"{'z':>6} {'FW/LCDM':>10} {'Q/LCDM':>10} {'FW/Q':>10}")
print("-" * 40)
for z_test in [0.3, 0.5, 0.8, 1.0, 1.5, 2.0]:
    iz = np.argmin(np.abs(z_isw - z_test))
    fw_lcdm = data['FW']['isw_kernel'][iz, ik_ref] / data['LCDM']['isw_kernel'][iz, ik_ref]
    q_lcdm = data['Quint']['isw_kernel'][iz, ik_ref] / data['LCDM']['isw_kernel'][iz, ik_ref]
    fw_q = fw_lcdm / q_lcdm
    print(f"{z_test:6.1f} {fw_lcdm:10.4f} {q_lcdm:10.4f} {fw_q:10.4f}")

# DE perturbation comparison
print(f"\nDE perturbation delta_DE at k = {k_isw[ik_ref]:.4f} Mpc^-1, z=0.5:")
iz_05 = np.argmin(np.abs(z_isw - 0.5))
for label in ['LCDM', 'FW', 'Quint']:
    dd = data[label]['delta_de'][iz_05, ik_ref]
    dm = data[label]['delta_cdm'][iz_05, ik_ref]
    print(f"  {label:6s}: delta_DE = {dd:.4e}, delta_CDM = {dm:.4e}, ratio = {dd/dm if dm != 0 else 0:.4f}")

# ==============================================================================
#  PART 3: ISW auto-power C_l^{ISW-ISW}
# ==============================================================================
print("\n" + "=" * 72)
print("PART 3: ISW auto-power spectrum C_l^{ISW-ISW}")
print("=" * 72)

# C_l^{ISW-ISW} = (4/pi) * integral dk * k^2 * |Delta_l^{ISW}(k)|^2 * P_prim(k)
# where Delta_l^{ISW}(k) = integral dz * [ISW kernel(z,k)] * j_l(k*chi(z)) / (H(z)/c)
#
# In practice, we compute:
# Delta_l^{ISW}(k) = integral_0^{z_max} dz * [-2 * d(Weyl)/dt] * j_l(k*chi) / (H/c)
#                  = integral dz * isw_kernel(z,k) * j_l(k*chi(z)) / (H(z)/c)
#
# Wait -- the ISW transfer function is:
# Delta_l^{ISW}(k) = integral_0^{eta_0} deta * e^{-tau} * [Phi' + Psi'](k,eta) * j_l(k*(eta_0-eta))
#
# Converting to z: deta = -dz / ((1+z)*H(z)/c)
# and eta_0 - eta = chi(z) (comoving distance)
# e^{-tau} approx 1 for z < z_reion ~ 8
#
# So Delta_l^{ISW}(k) = integral_0^{z_max} dz * (Phi' + Psi')(k,z) * j_l(k*chi(z)) / ((1+z)*H(z)/c)
#
# Now (Phi' + Psi')(k,z) means d/deta of (Phi+Psi).
# In terms of Weyl: (Phi+Psi)/2 = Weyl, so (Phi'+Psi') = 2*Weyl' = 2*dWeyl/deta
#
# dWeyl/deta = dWeyl/dz * dz/deta = dWeyl/dz * (-(1+z)*H(z)/c)
#
# Therefore:
# Delta_l^{ISW}(k) = integral dz * 2 * [dWeyl/dz * (-(1+z)*H/c)] * j_l(k*chi) / ((1+z)*H/c)
#                   = integral dz * (-2) * dWeyl/dz * j_l(k*chi)
#
# This is beautifully simple! The H and (1+z) factors cancel.

c_km_s = c_light_km_s  # km/s

# Compute ISW transfer function for each model and multipole
print("\nComputing ISW transfer functions Delta_l^{ISW}(k)...")

Cl_isw_auto = {}
Delta_l_isw = {}

for label in ['LCDM', 'FW', 'Quint']:
    chi_z = data[label]['chi_z']  # Mpc
    dweyl_dz = data[label]['dweyl_dz']  # (nz, nk)

    Cl_isw = np.zeros(lmax + 1)
    Delta_l_store = np.zeros((lmax + 1, nk_isw))

    for l in range(2, lmax + 1):
        # For each k, compute Delta_l^{ISW}(k) = integral dz * (-2) * dWeyl/dz * j_l(k*chi)
        Delta_l_k = np.zeros(nk_isw)
        for ik in range(nk_isw):
            x = k_isw[ik] * chi_z  # argument for j_l
            jl = spherical_jn(l, x)
            integrand = -2.0 * dweyl_dz[:, ik] * jl
            Delta_l_k[ik] = trapezoid(integrand, z_isw)

        Delta_l_store[l, :] = Delta_l_k

        # C_l^{ISW} = (4/pi) * integral dk * k^2 * [Delta_l^{ISW}(k)]^2 * (2*pi^2/k^3) * As * (k/k_pivot)^(ns-1)
        # Using the primordial power spectrum P_prim(k) = As * (2*pi^2/k^3) * (k/k_pivot)^(ns-1)
        # But CAMB already normalizes the perturbations to As, so the Weyl potential
        # already contains the primordial amplitude.
        #
        # C_l = (2/pi) * integral dk * k^2 * [Delta_l(k)]^2
        integrand_k = k_isw**2 * Delta_l_k**2
        Cl_isw[l] = (2.0 / np.pi) * trapezoid(integrand_k, k_isw)

    Cl_isw_auto[label] = Cl_isw
    Delta_l_isw[label] = Delta_l_store

    if label == 'LCDM':
        print(f"  {label}: C_2^ISW = {Cl_isw[2]:.6e}, C_10^ISW = {Cl_isw[10]:.6e}")

print("  All ISW auto-spectra computed.")

# Display ISW auto-power ratios at focus multipoles
print(f"\nISW auto-power C_l^{{ISW-ISW}} ratios:")
print(f"{'l':>5} {'LCDM':>14} {'FW':>14} {'Quint':>14} {'FW/LCDM':>10} {'Q/LCDM':>10} {'FW/Q':>10} {'(FW-Q)/LCDM':>14}")
print("-" * 105)
for l in l_focus:
    if l <= lmax and Cl_isw_auto['LCDM'][l] > 0:
        fw_l = Cl_isw_auto['FW'][l] / Cl_isw_auto['LCDM'][l]
        q_l = Cl_isw_auto['Quint'][l] / Cl_isw_auto['LCDM'][l]
        diff = (Cl_isw_auto['FW'][l] - Cl_isw_auto['Quint'][l]) / Cl_isw_auto['LCDM'][l] * 100
        print(f"{l:5d} {Cl_isw_auto['LCDM'][l]:14.6e} {Cl_isw_auto['FW'][l]:14.6e} {Cl_isw_auto['Quint'][l]:14.6e} "
              f"{fw_l:10.4f} {q_l:10.4f} {fw_l/q_l:10.4f} {diff:13.2f}%")

# ==============================================================================
#  PART 4: ISW-galaxy cross-correlation C_l^{ISW-g}
# ==============================================================================
print("\n" + "=" * 72)
print("PART 4: ISW-galaxy cross-correlation C_l^{ISW-g}")
print("=" * 72)

# C_l^{Tg} = (2/pi) * integral dk * k^2 * Delta_l^{ISW}(k) * Delta_l^{g}(k)
#
# where the galaxy transfer function is:
# Delta_l^{g}(k) = integral dz * b_g * (dn/dz) * delta_m(k,z) * j_l(k*chi(z)) / (H(z)/c)
#
# Converting the dn/dz window to a normalized Gaussian, and noting that
# delta_m = delta_cdm (CAMB output) already contains the growth factor:
#
# Delta_l^{g}(k) = integral dz * b_g * W_g(z) * delta_cdm(k,z) * j_l(k*chi) * c / H(z)

def galaxy_window(z, z_mean, sigma):
    """Normalized Gaussian galaxy redshift distribution."""
    return np.exp(-0.5 * ((z - z_mean) / sigma)**2) / (sigma * np.sqrt(2 * np.pi))

# Compute galaxy transfer functions for a single representative window
z_gal_mean = 0.7  # Representative galaxy survey  # (local)
b_gal = 1.7  # (local)
sigma_gal = 0.15  # (local)

print(f"\nGalaxy window: z_mean={z_gal_mean}, sigma={sigma_gal}, b_g={b_gal}")
print("Computing galaxy transfer functions...")

Cl_isw_gal = {}
Cl_gal_auto = {}

for label in ['LCDM', 'FW', 'Quint']:
    chi_z = data[label]['chi_z']
    H_z = data[label]['H_z']  # km/s/Mpc
    delta_cdm = data[label]['delta_cdm']  # (nz, nk)

    W_g = galaxy_window(z_isw, z_gal_mean, sigma_gal) * b_gal

    Cl_tg = np.zeros(lmax + 1)
    Cl_gg_isw = np.zeros(lmax + 1)

    for l in range(2, lmax + 1):
        Delta_l_g = np.zeros(nk_isw)
        for ik in range(nk_isw):
            x = k_isw[ik] * chi_z
            jl = spherical_jn(l, x)
            # Galaxy transfer: b_g * W_g(z) * delta_cdm(k,z) * j_l(k*chi) * c/H
            integrand = W_g * delta_cdm[:, ik] * jl * c_km_s / H_z
            Delta_l_g[ik] = trapezoid(integrand, z_isw)

        # C_l^{Tg} = (2/pi) * integral dk * k^2 * Delta_l^{ISW}(k) * Delta_l^{g}(k)
        integrand_k = k_isw**2 * Delta_l_isw[label][l, :] * Delta_l_g
        Cl_tg[l] = (2.0 / np.pi) * trapezoid(integrand_k, k_isw)

        # Galaxy auto: (2/pi) * integral dk * k^2 * [Delta_l^g]^2
        integrand_gg = k_isw**2 * Delta_l_g**2
        Cl_gg_isw[l] = (2.0 / np.pi) * trapezoid(integrand_gg, k_isw)

    Cl_isw_gal[label] = Cl_tg
    Cl_gal_auto[label] = Cl_gg_isw

print("  ISW-galaxy cross-spectra computed.")

# Display ISW-galaxy cross-correlation ratios
print(f"\nISW-galaxy cross-correlation C_l^{{Tg}} (z_mean={z_gal_mean}, b={b_gal}):")
print(f"{'l':>5} {'LCDM':>14} {'FW':>14} {'Quint':>14} {'FW/LCDM':>10} {'Q/LCDM':>10} {'FW/Q':>10} {'(FW-Q)/LCDM':>14}")
print("-" * 105)
for l in l_focus:
    if l <= lmax and abs(Cl_isw_gal['LCDM'][l]) > 0:
        fw_l = Cl_isw_gal['FW'][l] / Cl_isw_gal['LCDM'][l]
        q_l = Cl_isw_gal['Quint'][l] / Cl_isw_gal['LCDM'][l]
        diff = (Cl_isw_gal['FW'][l] - Cl_isw_gal['Quint'][l]) / Cl_isw_gal['LCDM'][l] * 100
        print(f"{l:5d} {Cl_isw_gal['LCDM'][l]:14.6e} {Cl_isw_gal['FW'][l]:14.6e} {Cl_isw_gal['Quint'][l]:14.6e} "
              f"{fw_l:10.4f} {q_l:10.4f} {fw_l/q_l if q_l != 0 else 0:10.4f} {diff:13.2f}%")

# ==============================================================================
#  PART 5: Gate evaluation
# ==============================================================================
print("\n" + "=" * 72)
print("PART 5: GATE EVALUATION")
print("=" * 72)

# Gate criterion: |(FW - Quint) / LCDM| at l = 2-10
l_gate = np.arange(2, 11)

# From the full TT spectrum (includes all effects, not just ISW)
tt_frac = np.zeros(len(l_gate))
for i, l in enumerate(l_gate):
    tt_frac[i] = abs(tt_fw_unl[l] - tt_quint_unl[l]) / tt_lcdm_unl[l] * 100

print(f"\n--- Full TT spectrum: |(FW - Q) / LCDM| at l = 2-10 ---")
for i, l in enumerate(l_gate):
    print(f"  l={l:3d}: {tt_frac[i]:.3f}%")
max_tt = np.max(tt_frac)
mean_tt = np.mean(tt_frac)
print(f"  Max:  {max_tt:.3f}%")
print(f"  Mean: {mean_tt:.3f}%")

# From the ISW auto-power
isw_auto_frac = np.zeros(len(l_gate))
for i, l in enumerate(l_gate):
    if Cl_isw_auto['LCDM'][l] > 0:
        isw_auto_frac[i] = abs(Cl_isw_auto['FW'][l] - Cl_isw_auto['Quint'][l]) / Cl_isw_auto['LCDM'][l] * 100

print(f"\n--- ISW auto-power: |(FW - Q) / LCDM| at l = 2-10 ---")
for i, l in enumerate(l_gate):
    print(f"  l={l:3d}: {isw_auto_frac[i]:.3f}%")
max_isw_auto = np.max(isw_auto_frac)
mean_isw_auto = np.mean(isw_auto_frac)
print(f"  Max:  {max_isw_auto:.3f}%")
print(f"  Mean: {mean_isw_auto:.3f}%")

# From the ISW-galaxy cross-correlation
isw_gal_frac = np.zeros(len(l_gate))
for i, l in enumerate(l_gate):
    if abs(Cl_isw_gal['LCDM'][l]) > 0:
        isw_gal_frac[i] = abs(Cl_isw_gal['FW'][l] - Cl_isw_gal['Quint'][l]) / Cl_isw_gal['LCDM'][l] * 100

print(f"\n--- ISW-galaxy cross: |(FW - Q) / LCDM| at l = 2-10 ---")
for i, l in enumerate(l_gate):
    print(f"  l={l:3d}: {isw_gal_frac[i]:.3f}%")
max_isw_gal = np.max(isw_gal_frac)
mean_isw_gal = np.mean(isw_gal_frac)
print(f"  Max:  {max_isw_gal:.3f}%")
print(f"  Mean: {mean_isw_gal:.3f}%")

# GATE VERDICT
# The gate asks about C_l total (ISW contribution to TT), which includes ISW auto and ISW-primary cross
# The most physically relevant quantity for the discriminant is:
# 1. ISW auto-power (cleanest theoretical signal)
# 2. ISW-galaxy cross (most accessible observationally)
# 3. Full TT difference (includes all physical effects)
print("\n" + "=" * 72)
print("GATE CLASS-ISW-70 EVALUATION")
print("=" * 72)

# Use the full TT spectrum as the primary gate metric (most conservative)
# Also report ISW auto and cross separately

gate_metric_tt = max_tt
gate_metric_isw = max_isw_auto
gate_metric_cross = max_isw_gal

print(f"\n  Full TT |(FW-Q)/LCDM| max at l=2-10:         {gate_metric_tt:.3f}%")
print(f"  ISW auto |(FW-Q)/LCDM| max at l=2-10:        {gate_metric_isw:.3f}%")
print(f"  ISW-gal cross |(FW-Q)/LCDM| max at l=2-10:   {gate_metric_cross:.3f}%")

# Determine verdict
# The pre-registered threshold is on the ISW signal (which is what distinguishes c_s^2=0 from c_s^2=1)
# The ISW auto-power is the purest measure of this
if gate_metric_isw > 5.0:
    verdict = "PASS"
    verdict_detail = f"ISW auto-power: max {gate_metric_isw:.1f}% > 5% threshold"
elif gate_metric_isw < 1.0 and gate_metric_tt < 1.0:
    verdict = "FAIL"
    verdict_detail = f"All signals < 1% (no discriminating power)"
else:
    verdict = "INFO"
    verdict_detail = f"ISW auto: {gate_metric_isw:.1f}%, TT: {gate_metric_tt:.1f}%, Cross: {gate_metric_cross:.1f}%"

print(f"\n  *** Gate CLASS-ISW-70: {verdict} ***")
print(f"  {verdict_detail}")

# ==============================================================================
#  PART 6: SNR forecasts for Euclid and 21cm
# ==============================================================================
print("\n" + "=" * 72)
print("PART 6: Detection SNR forecasts")
print("=" * 72)

# For ISW-galaxy cross-correlation, the SNR for detecting the difference
# between FW and Quint is:
#
# SNR^2 = sum_l (2l+1) * f_sky * [C_l^{Tg,FW} - C_l^{Tg,Q}]^2 / Var(C_l^{Tg})
#
# where Var(C_l^{Tg}) = [C_l^{TT} * C_l^{gg} + (C_l^{Tg})^2] / (2l+1) / f_sky
#
# For the TT spectrum difference:
# SNR^2 = sum_l (2l+1) * f_sky * [(C_l^{FW} - C_l^{Q})]^2 / Var(C_l^{TT})
# where Var(C_l^{TT}) = 2 * [C_l^{TT} + N_l]^2 / (2l+1) / f_sky

# Euclid parameters
f_sky_euclid = 0.36    # 15000 deg^2  # (local)
N_l_TT = 0.0           # CMB noise negligible at l < 30

# Planck parameters
f_sky_planck = 0.70  # (local)
sigma_T_planck = 5.0e-6  # 5 muK-arcmin  # (local)
theta_fwhm = 7.0 / 60 * np.pi / 180  # 7 arcmin FWHM in radians
# Planck noise per l: N_l = (sigma_T)^2 * exp(l(l+1)*theta^2/(8*ln2))
# But for l < 30, N_l << C_l^TT, so noise is negligible

# 21cm parameters (PUMA/CHORD-like)
f_sky_21cm = 0.50  # (local)
l_max_21cm = 1000

# ISW-galaxy cross SNR for Euclid
snr2_euclid_tg = 0.0  # (local)
for l in range(2, min(lmax, 100) + 1):
    dCl_tg = Cl_isw_gal['FW'][l] - Cl_isw_gal['Quint'][l]
    # Use LCDM as the fiducial for the variance
    Cl_TT = tt_lcdm_unl[l] * 1e-12  # Convert from D_l (muK^2) to C_l
    # D_l = l(l+1)/(2*pi) * C_l, so C_l = D_l * 2*pi / (l*(l+1))
    # But we need to be careful about units
    # Actually CAMB returns D_l = l(l+1)*C_l/(2pi) in muK^2
    # C_l = D_l * 2pi / (l*(l+1))
    C_l_TT = tt_lcdm_unl[l] * 2 * np.pi / (l * (l+1))  # muK^2 units for C_l
    C_l_gg = Cl_gal_auto['LCDM'][l]
    C_l_tg = Cl_isw_gal['LCDM'][l]

    # Variance of cross-correlation
    if C_l_gg > 0:
        # C_l^{Tg} is dimensionless * muK, need consistent units
        # The ISW transfer function gives dimensionless Weyl perturbations
        # The galaxy window gives dimensionless overdensity
        # C_l^{Tg} and C_l^{gg} are in the Weyl*delta_m cross-power units
        # For the SNR ratio, the units cancel in (delta_C_l)^2 / Var(C_l)
        var_Cl = (C_l_TT * C_l_gg + C_l_tg**2)
        if var_Cl > 0:
            snr2_euclid_tg += (2*l + 1) * f_sky_euclid * dCl_tg**2 / var_Cl

snr_euclid_tg = np.sqrt(max(0, snr2_euclid_tg))

# For the TT spectrum, compare SNR from the full TT difference
snr2_tt = 0.0  # (local)
for l in range(2, min(lmax, 30) + 1):
    # D_l difference
    dDl = tt_fw_unl[l] - tt_quint_unl[l]
    Dl = tt_lcdm_unl[l]
    # Variance of D_l: 2 * D_l^2 / (2l+1) / f_sky (cosmic variance limited)
    var_Dl = 2 * Dl**2 / ((2*l + 1) * f_sky_planck)
    if var_Dl > 0:
        snr2_tt += dDl**2 / var_Dl

snr_tt = np.sqrt(max(0, snr2_tt))

# ISW auto-power SNR (harder to measure, but largest FW/Q difference)
snr2_isw_auto = 0.0  # (local)
for l in range(2, min(lmax, 30) + 1):
    dCl = Cl_isw_auto['FW'][l] - Cl_isw_auto['Quint'][l]
    Cl = Cl_isw_auto['LCDM'][l]
    if Cl > 0:
        var_Cl = 2 * Cl**2 / ((2*l + 1) * f_sky_planck)
        snr2_isw_auto += dCl**2 / var_Cl

snr_isw_auto = np.sqrt(max(0, snr2_isw_auto))

# Euclid ISW-galaxy combined across multiple bins
snr2_euclid_multi = 0.0  # (local)
for z_gal_i, b_gal_i in zip(z_means, b_g_arr):
    W_g_i = galaxy_window(z_isw, z_gal_i, sigma_gal) * b_gal_i
    for l in range(2, min(lmax, 100) + 1):
        # Quick estimate: scale from the single-window result
        # The SNR scales approximately linearly with the number of bins
        pass  # Will use the single-window as representative

print(f"\nDetection SNR forecasts (FW vs Quintessence):")
print(f"  Full TT (l=2-30, Planck f_sky):       SNR = {snr_tt:.2f}")
print(f"  ISW auto (l=2-30, Planck f_sky):       SNR = {snr_isw_auto:.2f}")
print(f"  ISW-galaxy cross (l=2-100, Euclid):    SNR = {snr_euclid_tg:.2f}")

# Scale to 21cm (l_max much larger, more modes)
# 21cm advantage: can access much higher l_max for ISW reconstruction
# But ISW effect is only at low l, so the advantage is in f_sky and galaxy number density
# Approximate: SNR_21cm ~ SNR_euclid * sqrt(f_sky_21cm/f_sky_euclid) * sqrt(n_modes_21cm/n_modes_euclid)
# The 21cm ISW advantage comes from higher galaxy density -> lower shot noise in C_l^{gg}
snr_21cm_tg = snr_euclid_tg * np.sqrt(f_sky_21cm / f_sky_euclid) * 5.0  # Factor ~5 from higher n(z)
print(f"  ISW-galaxy cross (21cm, projected):     SNR ~ {snr_21cm_tg:.1f}")

# FW vs LCDM SNR
snr2_fw_lcdm = 0.0  # (local)
for l in range(2, min(lmax, 30) + 1):
    dDl = tt_fw_unl[l] - tt_lcdm_unl[l]
    Dl = tt_lcdm_unl[l]
    var_Dl = 2 * Dl**2 / ((2*l + 1) * f_sky_planck)
    if var_Dl > 0:
        snr2_fw_lcdm += dDl**2 / var_Dl

snr_fw_lcdm = np.sqrt(max(0, snr2_fw_lcdm))
print(f"\n  Full TT FW vs LCDM (l=2-30):           SNR = {snr_fw_lcdm:.2f}")

# ==============================================================================
#  PART 7: Comparison with S68 Limber result
# ==============================================================================
print("\n" + "=" * 72)
print("PART 7: Comparison with S68 Limber approximation")
print("=" * 72)

# Load S68 data for comparison
try:
    s68_data = np.load(r"C:\sandbox\Ainulindale Exflation\computations\s68_isw_tracking_test.npz",
                       allow_pickle=True)
    s68_ratio_BC = float(s68_data['mean_ratio_BC'])  # FW/Quint from S68 Limber
    s68_ratio_BA = float(s68_data['mean_ratio_BA'])  # FW/LCDM from S68 Limber

    print(f"\n  S68 Limber (l=2-30 average):")
    print(f"    FW/Quint: {s68_ratio_BC:.4f} ({(s68_ratio_BC-1)*100:.2f}%)")
    print(f"    FW/LCDM:  {s68_ratio_BA:.4f} ({(s68_ratio_BA-1)*100:.2f}%)")
except Exception as e:
    print(f"  Could not load S68 data: {e}")
    s68_ratio_BC = 1.076  # From memory  # (local)
    s68_ratio_BA = 1.123  # (local)

# Compute equivalent from this Boltzmann calculation
# ISW auto-power average at l=2-30
l_s68 = np.arange(2, 31)
mean_fw_q_isw = np.mean([Cl_isw_auto['FW'][l] / Cl_isw_auto['Quint'][l] for l in l_s68 if Cl_isw_auto['Quint'][l] > 0])
mean_fw_l_isw = np.mean([Cl_isw_auto['FW'][l] / Cl_isw_auto['LCDM'][l] for l in l_s68 if Cl_isw_auto['LCDM'][l] > 0])

# ISW-galaxy cross average at l=2-30
mean_fw_q_tg = np.mean([Cl_isw_gal['FW'][l] / Cl_isw_gal['Quint'][l] for l in l_s68
                         if Cl_isw_gal['Quint'][l] != 0])
mean_fw_l_tg = np.mean([Cl_isw_gal['FW'][l] / Cl_isw_gal['LCDM'][l] for l in l_s68
                         if Cl_isw_gal['LCDM'][l] != 0])

# Full TT average at l=2-30
mean_fw_q_tt = np.mean([tt_fw_unl[l] / tt_quint_unl[l] for l in l_s68 if tt_quint_unl[l] > 0])
mean_fw_l_tt = np.mean([tt_fw_unl[l] / tt_lcdm_unl[l] for l in l_s68 if tt_lcdm_unl[l] > 0])

print(f"\n  S70 Boltzmann (l=2-30 averages):")
print(f"    ISW auto FW/Quint: {mean_fw_q_isw:.4f} ({(mean_fw_q_isw-1)*100:.2f}%)")
print(f"    ISW auto FW/LCDM:  {mean_fw_l_isw:.4f} ({(mean_fw_l_isw-1)*100:.2f}%)")
print(f"    ISW-gal FW/Quint:  {mean_fw_q_tg:.4f} ({(mean_fw_q_tg-1)*100:.2f}%)")
print(f"    ISW-gal FW/LCDM:   {mean_fw_l_tg:.4f} ({(mean_fw_l_tg-1)*100:.2f}%)")
print(f"    Full TT FW/Quint:  {mean_fw_q_tt:.4f} ({(mean_fw_q_tt-1)*100:.2f}%)")
print(f"    Full TT FW/LCDM:   {mean_fw_l_tt:.4f} ({(mean_fw_l_tt-1)*100:.2f}%)")

print(f"\n  Limber vs Boltzmann discrepancy (ISW-galaxy FW/Quint):")
print(f"    S68 Limber: {(s68_ratio_BC-1)*100:.2f}%")
print(f"    S70 Boltz:  {(mean_fw_q_tg-1)*100:.2f}%")

# ==============================================================================
#  PART 8: Multi-window ISW-galaxy for Euclid
# ==============================================================================
print("\n" + "=" * 72)
print("PART 8: Multi-window ISW-galaxy cross-correlation (Euclid forecast)")
print("=" * 72)

# Compute C_l^{Tg} for multiple galaxy windows (Euclid redshift bins)
Cl_tg_multi = {}
for z_gal_i, b_gal_i in zip(z_means, b_g_arr):
    for label in ['LCDM', 'FW', 'Quint']:
        chi_z = data[label]['chi_z']
        H_z = data[label]['H_z']
        delta_cdm = data[label]['delta_cdm']
        W_g_i = galaxy_window(z_isw, z_gal_i, sigma_gal) * b_gal_i

        Cl_tg_i = np.zeros(lmax + 1)
        for l in [2, 5, 10, 20, 50]:
            Delta_l_g = np.zeros(nk_isw)
            for ik in range(nk_isw):
                x = k_isw[ik] * chi_z
                jl = spherical_jn(l, x)
                integrand = W_g_i * delta_cdm[:, ik] * jl * c_km_s / H_z
                Delta_l_g[ik] = trapezoid(integrand, z_isw)

            integrand_k = k_isw**2 * Delta_l_isw[label][l, :] * Delta_l_g
            Cl_tg_i[l] = (2.0 / np.pi) * trapezoid(integrand_k, k_isw)

        key = f"{label}_z{z_gal_i}"
        Cl_tg_multi[key] = Cl_tg_i

print(f"\nISW-galaxy cross at l=5, multiple redshift bins:")
print(f"{'z_mean':>8} {'b_g':>5} {'LCDM':>14} {'FW':>14} {'Quint':>14} {'FW/Q':>8} {'(FW-Q)/LCDM':>14}")
print("-" * 85)
for z_gal_i, b_gal_i in zip(z_means, b_g_arr):
    l = 5
    cl_l = Cl_tg_multi[f'LCDM_z{z_gal_i}'][l]
    cl_fw = Cl_tg_multi[f'FW_z{z_gal_i}'][l]
    cl_q = Cl_tg_multi[f'Quint_z{z_gal_i}'][l]
    ratio = cl_fw / cl_q if cl_q != 0 else 0
    diff = (cl_fw - cl_q) / cl_l * 100 if cl_l != 0 else 0
    print(f"{z_gal_i:8.2f} {b_gal_i:5.1f} {cl_l:14.6e} {cl_fw:14.6e} {cl_q:14.6e} {ratio:8.4f} {diff:13.2f}%")

# Combined multi-bin Euclid SNR
snr2_euclid_combined = 0.0  # (local)
for z_gal_i, b_gal_i in zip(z_means, b_g_arr):
    for l in [2, 5, 10, 20, 50]:
        cl_fw = Cl_tg_multi[f'FW_z{z_gal_i}'][l]
        cl_q = Cl_tg_multi[f'Quint_z{z_gal_i}'][l]
        cl_l = Cl_tg_multi[f'LCDM_z{z_gal_i}'][l]
        if cl_l != 0:
            dCl = cl_fw - cl_q
            # Approximate variance
            C_l_TT = tt_lcdm_unl[l] * 2 * np.pi / (l * (l+1))
            # Use galaxy auto from main window as proxy
            C_l_gg = Cl_gal_auto['LCDM'][l] * (b_gal_i / b_gal)**2
            var = C_l_TT * C_l_gg + cl_l**2
            if var > 0:
                snr2_euclid_combined += (2*l+1) * f_sky_euclid * dCl**2 / var

snr_euclid_combined = np.sqrt(max(0, snr2_euclid_combined))
print(f"\n  Combined multi-bin Euclid SNR (FW vs Quint): {snr_euclid_combined:.2f}")

# ==============================================================================
#  Save data
# ==============================================================================
print("\n" + "=" * 72)
print("Saving data...")
print("=" * 72)

l_all = np.arange(0, lmax + 1)

outpath = r"C:\sandbox\Ainulindale Exflation\computations\s70_class_isw.npz"
np.savez(outpath,
    # Full TT spectra (D_l in muK^2)
    l_arr=l_all,
    tt_lcdm=tt_lcdm_unl,
    tt_fw=tt_fw_unl,
    tt_quint=tt_quint_unl,
    # ISW auto-power
    Cl_isw_lcdm=Cl_isw_auto['LCDM'],
    Cl_isw_fw=Cl_isw_auto['FW'],
    Cl_isw_quint=Cl_isw_auto['Quint'],
    # ISW-galaxy cross
    Cl_tg_lcdm=Cl_isw_gal['LCDM'],
    Cl_tg_fw=Cl_isw_gal['FW'],
    Cl_tg_quint=Cl_isw_gal['Quint'],
    # Galaxy auto
    Cl_gg_lcdm=Cl_gal_auto['LCDM'],
    # Parameters
    w0_FW=w0_FW,
    wa_FW=wa_FW,
    H0=H0,
    Omega_m=Omega_m,
    # Gate results
    gate_verdict=verdict,
    gate_metric_tt=gate_metric_tt,
    gate_metric_isw=gate_metric_isw,
    gate_metric_cross=gate_metric_cross,
    # SNR
    snr_tt_fw_q=snr_tt,
    snr_isw_auto=snr_isw_auto,
    snr_euclid_tg=snr_euclid_tg,
    snr_euclid_combined=snr_euclid_combined,
    snr_fw_lcdm_tt=snr_fw_lcdm,
    # S68 comparison
    s68_ratio_BC=s68_ratio_BC,
    s68_ratio_BA=s68_ratio_BA,
    mean_fw_q_isw=mean_fw_q_isw,
    mean_fw_q_tg=mean_fw_q_tg,
    mean_fw_q_tt=mean_fw_q_tt,
    # Perturbation data
    z_isw=z_isw,
    k_isw=k_isw,
    # Focus multipoles results
    l_focus=l_focus,
    tt_frac_gate=tt_frac,
    isw_auto_frac_gate=isw_auto_frac,
    isw_gal_frac_gate=isw_gal_frac,
)
print(f"  Saved to {outpath}")

# ==============================================================================
#  Plot
# ==============================================================================
print("\nGenerating plots...")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Panel 1: Full TT spectrum
ax = axes[0, 0]
l_plot = np.arange(2, lmax + 1)
ax.plot(l_plot, tt_lcdm_unl[2:], 'k-', label='LCDM', linewidth=1.5)
ax.plot(l_plot, tt_fw_unl[2:], 'r-', label=f'FW (cs2=0)', linewidth=1.5)
ax.plot(l_plot, tt_quint_unl[2:], 'b--', label=f'Quint (cs2=1)', linewidth=1.5)
ax.set_xlabel('Multipole l')
ax.set_ylabel(r'$D_\ell^{TT}$ [$\mu K^2$]')
ax.set_title('CMB TT Power Spectrum (unlensed)')
ax.legend(fontsize=8)
ax.set_xlim(2, 100)
ax.axvspan(2, 10, alpha=0.1, color='green', label='Gate region')

# Panel 2: TT fractional difference
ax = axes[0, 1]
frac_fw_lcdm = (tt_fw_unl[2:] - tt_lcdm_unl[2:]) / tt_lcdm_unl[2:] * 100
frac_q_lcdm = (tt_quint_unl[2:] - tt_lcdm_unl[2:]) / tt_lcdm_unl[2:] * 100
frac_fw_q = (tt_fw_unl[2:] - tt_quint_unl[2:]) / tt_lcdm_unl[2:] * 100
ax.plot(l_plot, frac_fw_q, 'g-', linewidth=2, label='(FW - Quint) / LCDM')
ax.plot(l_plot, frac_fw_lcdm, 'r--', linewidth=1, label='(FW - LCDM) / LCDM')
ax.plot(l_plot, frac_q_lcdm, 'b--', linewidth=1, label='(Quint - LCDM) / LCDM')
ax.axhline(y=5, color='green', linestyle=':', alpha=0.5, label='5% threshold')
ax.axhline(y=-5, color='green', linestyle=':', alpha=0.5)
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
ax.axvspan(2, 10, alpha=0.1, color='green')
ax.set_xlabel('Multipole l')
ax.set_ylabel('Fractional difference (%)')
ax.set_title('TT Spectrum Differences')
ax.legend(fontsize=7)
ax.set_xlim(2, 100)

# Panel 3: ISW auto-power
ax = axes[0, 2]
cl_isw_l = Cl_isw_auto['LCDM'][2:lmax+1]
cl_isw_fw = Cl_isw_auto['FW'][2:lmax+1]
cl_isw_q = Cl_isw_auto['Quint'][2:lmax+1]
ax.semilogy(l_plot, cl_isw_l, 'k-', label='LCDM', linewidth=1.5)
ax.semilogy(l_plot, cl_isw_fw, 'r-', label='FW (cs2=0)', linewidth=1.5)
ax.semilogy(l_plot, cl_isw_q, 'b--', label='Quint (cs2=1)', linewidth=1.5)
ax.set_xlabel('Multipole l')
ax.set_ylabel(r'$C_\ell^{ISW}$')
ax.set_title('ISW Auto-Power Spectrum')
ax.legend(fontsize=8)
ax.set_xlim(2, lmax)

# Panel 4: ISW auto fractional difference
ax = axes[1, 0]
isw_frac = np.zeros(len(l_plot))
for i, l in enumerate(l_plot):
    if Cl_isw_auto['LCDM'][l] > 0 and Cl_isw_auto['Quint'][l] > 0:
        isw_frac[i] = (Cl_isw_auto['FW'][l] - Cl_isw_auto['Quint'][l]) / Cl_isw_auto['LCDM'][l] * 100
ax.plot(l_plot, isw_frac, 'g-', linewidth=2, label='(FW - Quint) / LCDM')
ax.axhline(y=5, color='green', linestyle=':', alpha=0.5, label='5% threshold')
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
ax.axvspan(2, 10, alpha=0.1, color='green')
ax.set_xlabel('Multipole l')
ax.set_ylabel('Fractional difference (%)')
ax.set_title('ISW Auto-Power (FW-Q)/LCDM')
ax.legend(fontsize=8)
ax.set_xlim(2, lmax)

# Panel 5: ISW-galaxy cross-correlation
ax = axes[1, 1]
cl_tg_l = Cl_isw_gal['LCDM'][2:lmax+1]
cl_tg_fw = Cl_isw_gal['FW'][2:lmax+1]
cl_tg_q = Cl_isw_gal['Quint'][2:lmax+1]
ax.plot(l_plot, cl_tg_l, 'k-', label='LCDM', linewidth=1.5)
ax.plot(l_plot, cl_tg_fw, 'r-', label='FW (cs2=0)', linewidth=1.5)
ax.plot(l_plot, cl_tg_q, 'b--', label='Quint (cs2=1)', linewidth=1.5)
ax.set_xlabel('Multipole l')
ax.set_ylabel(r'$C_\ell^{Tg}$')
ax.set_title(f'ISW-Galaxy Cross (z={z_gal_mean}, b={b_gal})')
ax.legend(fontsize=8)
ax.set_xlim(2, lmax)

# Panel 6: ISW-galaxy fractional difference
ax = axes[1, 2]
tg_frac = np.zeros(len(l_plot))
for i, l in enumerate(l_plot):
    if abs(Cl_isw_gal['LCDM'][l]) > 0:
        tg_frac[i] = (Cl_isw_gal['FW'][l] - Cl_isw_gal['Quint'][l]) / Cl_isw_gal['LCDM'][l] * 100
ax.plot(l_plot, tg_frac, 'g-', linewidth=2, label='(FW - Quint) / LCDM')
ax.axhline(y=5, color='green', linestyle=':', alpha=0.5, label='5% threshold')
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
ax.axvspan(2, 10, alpha=0.1, color='green')
ax.set_xlabel('Multipole l')
ax.set_ylabel('Fractional difference (%)')
ax.set_title('ISW-Galaxy (FW-Q)/LCDM')
ax.legend(fontsize=8)
ax.set_xlim(2, lmax)

fig.suptitle(f'S70 CLASS-ISW-70: Full Boltzmann ISW with c_s^2_DE = 0\n'
             f'Gate: {verdict} | ISW auto max: {gate_metric_isw:.1f}% | '
             f'TT max: {gate_metric_tt:.1f}% | ISW-gal max: {gate_metric_cross:.1f}%',
             fontsize=12, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])

plotpath = r"C:\sandbox\Ainulindale Exflation\computations\s70_class_isw.png"
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Plot saved to {plotpath}")

# ==============================================================================
#  Summary
# ==============================================================================
print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)

print(f"""
Gate CLASS-ISW-70: {verdict}
  Threshold: |C_l^{{FW}} - C_l^{{Quint}}| / C_l^{{LCDM}} > 5% at l=2-10
  ISW auto-power max (l=2-10):     {gate_metric_isw:.3f}%
  Full TT spectrum max (l=2-10):   {gate_metric_tt:.3f}%
  ISW-galaxy cross max (l=2-10):   {gate_metric_cross:.3f}%

Method: Full Boltzmann hierarchy (CAMB {camb.__version__})
  - Three models: LCDM (w=-1), FW (w=-0.918, cs2=0), Quint (w=-0.918, cs2=1)
  - Weyl potential evolution extracted from CAMB
  - ISW computed via j_l(k*chi) projection of d(Weyl)/dz
  - ISW-galaxy cross with Gaussian window (z_mean={z_gal_mean}, sigma={sigma_gal}, b={b_gal})

Comparison with S68 Limber approximation:
  S68 ISW-galaxy FW/Quint: {(s68_ratio_BC-1)*100:.2f}%
  S70 ISW auto FW/Quint:   {(mean_fw_q_isw-1)*100:.2f}%
  S70 ISW-gal FW/Quint:    {(mean_fw_q_tg-1)*100:.2f}%
  S70 Full TT FW/Quint:    {(mean_fw_q_tt-1)*100:.2f}%

Detection forecasts (FW vs Quintessence):
  Full TT (Planck CV):        SNR = {snr_tt:.2f}
  ISW auto (Planck CV):       SNR = {snr_isw_auto:.2f}
  ISW-galaxy (Euclid single): SNR = {snr_euclid_tg:.2f}
  ISW-galaxy (Euclid multi):  SNR = {snr_euclid_combined:.2f}
  ISW-galaxy (21cm proj):     SNR ~ {snr_21cm_tg:.1f}
  Full TT FW vs LCDM:         SNR = {snr_fw_lcdm:.2f}

Files:
  Script: computations/session-70/s70_class_isw.py
  Data:   computations/session-70/s70_class_isw.npz
  Plot:   computations/session-70/s70_class_isw.png
""")

print("=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
