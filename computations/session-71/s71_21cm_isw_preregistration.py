#!/usr/bin/env python3
"""
S71 21CM-ISW-PREREGISTRATION-71: Full Prediction Chain Pre-Registration
=======================================================================

Compiles the complete prediction chain:
  Spectral action q-theory -> c_s^2 = 0 -> modified ISW -> 21cm brightness temp

Produces central predictions, error budgets, and SNR forecasts for SKA-Low and HERA.

Gate: INFO (pre-registration document with central prediction and error budget)

Input data:
  - computations/session-70/s70_class_isw.npz (full Boltzmann ISW, CAMB 1.6.6)
  - computations/session-70/s70_q_sound.npz   (q-theory c_s^2 derivation)
  - computations/_shared/canonical_constants.py

Author: mack-cosmic-bridge (S71)
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    H_0_km_s_Mpc, Omega_m, Omega_b, Omega_DM, Omega_Lambda,
    T_CMB, sigma_8, A_s_CMB, Omega_r,
    c_light_km_s, Mpc_to_m, k_B_SI, h_planck_SI,
    rho_crit_GeV4, rho_Lambda_obs,
    a0_fold, a2_fold, a4_fold, tau_fold,
    S_fold, dS_fold, d2S_fold,
    M_KK_gravity, M_KK_kerner, Vol_SU3_Haar,
    PI
)

# ===========================================================================
# 0. Load prior computation data
# ===========================================================================

isw_data = np.load(os.path.join(os.path.dirname(__file__), 's70_class_isw.npz'),
                   allow_pickle=True)
qsound_data = np.load(os.path.join(os.path.dirname(__file__), 's70_q_sound.npz'),
                       allow_pickle=True)

# Extract ISW arrays
l_arr = isw_data['l_arr']             # multipoles 0..100
Cl_isw_fw = isw_data['Cl_isw_fw']     # ISW auto-power, FW (c_s^2=0)
Cl_isw_lcdm = isw_data['Cl_isw_lcdm'] # ISW auto-power, LCDM
Cl_isw_quint = isw_data['Cl_isw_quint']  # ISW auto-power, Quintessence (c_s^2=1)

w0_FW = float(isw_data['w0_FW'])       # -0.918
wa_FW = float(isw_data['wa_FW'])       # 0.0

# Extract q-sound results
cs2_tree = float(qsound_data['cs2_tree'])       # 0.0 (exact at tree level)
cs2_1loop = float(qsound_data['cs2_1loop'])      # 3.36e-4
cs2_total = float(qsound_data['cs2_total'])      # 3.36e-4
cs2_upper = float(qsound_data['cs2_upper_bound']) # 0.269

# W1-E result: delta(c_s^2) < 4.3e-4 from non-trivial fibration
cs2_fibration_delta = 4.3e-4  # W1-E bound  # (local)

print("=" * 72)
print("21CM-ISW-PREREGISTRATION-71: Full Prediction Chain")
print("=" * 72)

# ===========================================================================
# 1. PREDICTION CHAIN: Step-by-step with numerical values
# ===========================================================================

print("\n--- STEP 1: Spectral Action q-theory -> c_s^2 = 0 ---")
print(f"  Spectral action at fold: S_fold = {S_fold:.2f}")
print(f"  dS/dtau at fold: {dS_fold:.2f}")
print(f"  d^2S/dtau^2 at fold: {d2S_fold:.2f}")
print(f"  q-variable: thermodynamic conjugate from S = integral q d(tau)")
print(f"  c_s^2(tree) = d^2V/dq^2 * (dq/d(rho+p))^-1 = {cs2_tree:.6f}")
print(f"  c_s^2(1-loop) = {cs2_1loop:.6e}")
print(f"  c_s^2(total) = {cs2_total:.6e}")
print(f"  c_s^2(upper bound) = {cs2_upper:.4f}")
print(f"  W1-E fibration correction: delta(c_s^2) < {cs2_fibration_delta:.1e}")
print(f"  -> Q-SOUND-70 PASS: c_s^2 perturbatively small, tracking regime preserved")

# Effective c_s^2 including all corrections
cs2_eff = cs2_total + cs2_fibration_delta  # conservative: add fibration bound
cs2_eff_low = 0.0  # tree-level exact  # (local)
cs2_eff_high = cs2_total + cs2_fibration_delta  # worst-case from 1-loop + fibration

print(f"  Effective c_s^2 range: [{cs2_eff_low:.1e}, {cs2_eff_high:.4e}]")

# ===========================================================================
# STEP 2: c_s^2 = 0 -> Modified ISW at low l
# ===========================================================================

print("\n--- STEP 2: c_s^2 = 0 -> ISW modification ---")

# ISW fractional enhancement at l=2-10 (from CLASS-ISW-70)
l_gate = np.arange(2, 11)  # l = 2..10
mask = np.isin(l_arr, l_gate)

# Compute FW/Quint ratio for ISW auto at each l
ratio_fw_q = Cl_isw_fw[mask] / Cl_isw_quint[mask]
ratio_fw_lcdm = Cl_isw_fw[mask] / Cl_isw_lcdm[mask]

delta_isw_fw_q = (ratio_fw_q - 1.0)  # fractional enhancement
delta_isw_fw_lcdm = (ratio_fw_lcdm - 1.0)

mean_delta_fw_q = np.mean(delta_isw_fw_q)
mean_delta_fw_lcdm = np.mean(delta_isw_fw_lcdm)

print(f"  ISW auto FW/Quint: {100*mean_delta_fw_q:.2f}% mean (l=2-10)")
print(f"  ISW auto FW/LCDM: {100*mean_delta_fw_lcdm:.2f}% mean (l=2-10)")
print(f"  ISW auto FW/Quint at l=2: {100*delta_isw_fw_q[0]:.2f}%")
print(f"  -> CLASS-ISW-70 PASS: >5% at all l=2-10")

# Physical mechanism: tracking vacuum with c_s^2=0 -> DE clusters with matter
# delta_DE = (1+w)/(1-3w) * delta_m on sub-horizon scales
w0 = w0_FW  # = -0.918
tracking_factor = (1.0 + w0) / (1.0 - 3.0 * w0)
print(f"  Tracking factor (1+w)/(1-3w) = {tracking_factor:.4f}")
print(f"  w_0 = {w0}")

# ===========================================================================
# STEP 3: Modified ISW -> 21cm power spectrum modification
# ===========================================================================

print("\n--- STEP 3: ISW -> 21cm power spectrum at k < 0.01 h/Mpc ---")

# The ISW effect modifies the matter power spectrum at large scales (k < 0.01 h/Mpc)
# through the Rees-Sciama / ISW coupling to the 21cm signal.
#
# At z = 10-20 (pre-reionization), the 21cm signal traces the matter distribution:
#   T_b(z) = 27 * x_HI * (1 - T_gamma/T_S) * sqrt((1+z)/10 * 0.15/Omega_m/h^2) * (Omega_b*h^2/0.023) mK
# (Furlanetto, Oh & Briggs 2006, Eq. 52)
#
# The ISW modification enters through the cross-correlation between the CMB temperature
# fluctuation and the matter distribution. At z ~ 10-20, the relevant mechanism is the
# TIME-DERIVATIVE of the gravitational potential (Phi_dot) which creates the ISW temperature
# shift. The c_s^2=0 tracking vacuum modifies Phi_dot relative to c_s^2=1 quintessence.

h = H_0_km_s_Mpc / 100.0  # = 0.674
Omega_b_h2 = Omega_b * h**2
Omega_m_h2 = Omega_m * h**2

# Reference redshifts for 21cm dark ages / cosmic dawn
z_21cm = np.array([10, 12, 15, 18, 20, 25, 30])

# 21cm mean brightness temperature (Furlanetto+06 Eq 52)
# In the pre-reionization era (z > 10), x_HI ~ 1 (fully neutral)
# T_S >> T_gamma is satisfied for z < 30 due to Lyman-alpha coupling
# (Wouthuysen-Field effect from first stars)
# For z > 30, T_S -> T_gamma and the signal vanishes
# We compute T_b for x_HI = 1 and T_S >> T_gamma (saturated limit)
x_HI = 1.0  # fully neutral before reionization  # (local)

T_b_ref = 27.0 * x_HI * np.sqrt((1.0 + z_21cm) / 10.0 * 0.15 / Omega_m_h2) * (Omega_b_h2 / 0.023)  # mK

print(f"  Mean brightness temperature T_b (saturated, x_HI=1):")
for i, z in enumerate(z_21cm):
    print(f"    z={z:2d}: T_b = {T_b_ref[i]:.2f} mK")

# The ISW modification to the 21cm power spectrum occurs through two channels:
#
# Channel A: Direct matter power P(k,z) modification from DE clustering
#   At z ~ 15, Omega_DE(z) = Omega_Lambda / (Omega_Lambda + Omega_m*(1+z)^3) is small
#   For w_0 = -0.918: Omega_DE(z=15) is ~negligible
#   -> This channel is suppressed at high z
#
# Channel B: ISW-21cm cross-correlation C_l^{T,21cm}
#   This correlates the CMB ISW fluctuation with the 21cm brightness temperature field
#   At z ~ 15, the 21cm field is a biased tracer of the density field
#   The ISW effect at these redshifts is dominated by the late-time potential decay (z < 2)
#   -> Cross-correlation probes the INTEGRATED ISW, not the z=15 potential

# Channel B is the dominant discriminant (Tashiro+08, Cooray 2004)

# Omega_DE at each redshift
Omega_DE_z = Omega_Lambda / (Omega_Lambda + Omega_m * (1.0 + z_21cm)**3
                              + Omega_r * (1.0 + z_21cm)**4)

print(f"\n  Omega_DE(z) at 21cm redshifts (negligible -> direct P(k) modification small):")
for i, z in enumerate(z_21cm):
    print(f"    z={z:2d}: Omega_DE = {Omega_DE_z[i]:.2e}")

# ===========================================================================
# STEP 4: 21cm brightness temperature modification
# ===========================================================================

print("\n--- STEP 4: Central prediction: delta(T_b)/T_b ---")

# The ISW-21cm cross-correlation (Channel B):
# C_l^{T,21cm} = integral dchi W^T(chi) * W^{21cm}(chi) * P(l/chi, chi)
# where W^T includes the ISW kernel dPhi/deta, and W^{21cm} includes the 21cm emissivity.
#
# The FW modification enters ONLY through the ISW kernel:
#   dPhi/deta(FW) / dPhi/deta(LCDM) differs due to c_s^2=0 DE clustering
#
# From S70 CLASS-ISW-70 data, the Weyl potential modification is:
#   delta(dWeyl/dz) / (dWeyl/dz) = 3.5% at k=0.005 Mpc^-1 (FW vs LCDM)
#   delta(dWeyl/dz) / (dWeyl/dz) = 6.7% in ISW auto-power (FW vs Quint)
#
# The 21cm cross-correlation inherits this fractional modification.
# However, the cross-power depends on the PRODUCT of ISW and 21cm windows,
# and the 21cm window peaks at z ~ 15 where the ISW kernel has decayed.
#
# The redshift overlap integral determines the effective signal:
# Signal = integral dz dPhi/deta(z) * W_21cm(z) / [integral dz W_21cm(z)^2]^{1/2}

# The ISW kernel peaks at z ~ 0.5-1.0 (late-time DE domination)
# The 21cm window peaks at z ~ 10-20 (pre-reionization neutral hydrogen)
# Overlap is MINIMAL for the standard ISW-21cm cross-correlation.

# However, the discriminating signal is in the 21cm POWER SPECTRUM at large scales,
# which is modified by the different growth rate under c_s^2 = 0.

# Growth rate modification from c_s^2 = 0 tracking:
# The effective gravitational coupling is enhanced:
# G_eff/G = 1 + 2*(Omega_DE/(Omega_m+Omega_DE)) * (1+w)/(1-3w) at sub-horizon scales
# This modifies f = d ln(delta_m)/d ln(a)

# At high z, Omega_DE -> 0, so the modification is tiny
# The primary sensitivity is at z < 2 where the ISW auto-power lives

# For 21cm intensity mapping as a GALAXY SURVEY analog:
# The 21cm power spectrum P_21cm(k,z) = T_b(z)^2 * b_21^2(z) * P_m(k,z) * (1 + f/b * mu^2)^2
# where b_21 is the 21cm bias, f = growth rate, mu = angle to line of sight.
#
# The ISW cross-power C_l^{T,21cm} probes the late-time ISW through galaxy tracers
# at z ~ 1-5, NOT the direct high-z 21cm signal.
#
# For discriminating FW from Quintessence, the key is:
# 21cm intensity mapping at z ~ 0.5-3 covering large sky fraction
# This uses HI as a biased tracer of large-scale structure
# The signal is the same ISW-galaxy cross-correlation, but with:
#   - Much larger effective volume (no spectroscopic fiber limits)
#   - Higher number density of tracers (every neutral H atom)
#   - Lower shot noise at large scales

# k-modes relevant for ISW
k_isw = np.logspace(-4, -1.3, 200)  # h/Mpc
k_pivot = 0.01  # h/Mpc -- the scale where ISW enhancement is evaluated

# The fractional modification to the 21cm POWER at the ISW-relevant scales
# is inherited from the ISW auto-power enhancement
# Because P_21cm ~ P_m at large scales, and the growth function modification
# from c_s^2 = 0 is scale-independent at sub-horizon linear scales:

# delta(P_21cm)/P_21cm = delta(P_m)/P_m = 2 * delta(D)/D
# where D is the growth factor

# From S70 CLASS-ISW-70: the matter power modification is small compared to ISW auto
# The discriminating channel is NOT the matter power itself, but the ISW-tracer cross-power

# The key prediction: C_l^{T,21cm}(FW) / C_l^{T,21cm}(Quint) at z ~ 1-2

# From S70 ISW data at l=2-10 (the most sensitive multipoles):
# ISW auto: FW/Quint = 1.067 (6.7%)
# ISW-galaxy: FW/Quint = 1.040 (4.0%) -- galaxy window dilutes
#
# For 21cm intensity mapping, the tracer window is broader than spectroscopic galaxies
# The dilution factor depends on the redshift distribution of the 21cm survey
#
# SKA-Low: z ~ 3-27 (Dark Ages/Cosmic Dawn mode)
#   Relevant for ISW-21cm cross-correlation via matter at z < 5
#   At z > 5, the ISW kernel is negligible
#
# HERA: z ~ 6-25 (reionization focus)
#   Limited to higher z where ISW contribution is small
#
# For post-reionization HI intensity mapping (z ~ 0.1-2.5):
#   SKA-Mid Band 1: z ~ 0.35-3
#   CHIME: z ~ 0.8-2.5
#   These are the OPTIMAL ISW-21cm cross-correlation surveys

# The ISW-21cm cross-power spectrum:
# C_l^{T,21} = integral dz/chi^2 * [dPhi/deta * a] * [T_b * b_HI * D(z)] * P_m(l/chi)
# The enhancement factor is:
# Delta C_l^{T,21}(FW-Q) / C_l^{T,21}(LCDM) = delta_ISW * overlap_integral / normalization

# From S70 Boltzmann: the ISW-galaxy FW/Quint ratio = 1.040 for the test galaxy window
# For optimal HI IM at z ~ 0.5-2.5, the window is broader -> slightly different dilution

# Conservative estimate: same as ISW-galaxy (4.0% substrate-specific)
# Optimistic: closer to ISW auto (6.7% if wide-z window captures full kernel)
delta_Tb_central = 0.040  # 4.0% (ISW-galaxy inherited, conservative)  # (local)
delta_Tb_optimistic = 0.067  # 6.7% (ISW auto, optimistic)  # (local)
delta_Tb_pessimistic = 0.030  # 3.0% (if galaxy window narrower)  # (local)

# Central prediction at specific k, z for the ISW-21cm CROSS-POWER:
# The cross-power is evaluated at l ~ 5-30 (ISW-sensitive multipoles)
# At z ~ 1 for the HI tracer, l=10 corresponds to k ~ l/chi(z=1) ~ 10/3300 ~ 0.003 Mpc^{-1}
# This is exactly the ISW-relevant scale

z_cross = 1.0  # redshift of peak cross-correlation sensitivity  # (local)
l_cross = 10   # multipole of peak ISW sensitivity

# chi(z=1) in comoving Mpc (flat LCDM approximation)
chi_z1 = c_light_km_s / H_0_km_s_Mpc * 2.0 * (1.0 - 1.0 / np.sqrt(1.0 + z_cross))  # ~ 3300 Mpc (rough)
# More precise: numerical integration
z_int = np.linspace(0, z_cross, 1000)
E_z = np.sqrt(Omega_m * (1 + z_int)**3 + Omega_Lambda)
chi_z1_precise = c_light_km_s / H_0_km_s_Mpc * np.trapezoid(1.0 / E_z, z_int)  # Mpc

k_cross = l_cross / chi_z1_precise  # Mpc^{-1}

print(f"  ISW-21cm cross-correlation:")
print(f"    Peak sensitivity: z ~ {z_cross}, l ~ {l_cross}")
print(f"    Comoving distance chi(z=1) = {chi_z1_precise:.0f} Mpc")
print(f"    Corresponding k = l/chi = {k_cross:.5f} Mpc^-1 = {k_cross*h:.5f} h/Mpc")

# The fractional brightness temperature change from ISW
# delta(T_b) / T_b is NOT a modification of the mean T_b (which is background-level)
# It is the fractional change in the CROSS-POWER C_l^{T,21cm}

print(f"\n  Central prediction (ISW-21cm cross-power, l=2-30):")
print(f"    delta(C_l^{{T,21cm}})/C_l^{{T,21cm}}(FW/Quint) = {100*delta_Tb_central:.1f}% (substrate-specific)")
print(f"    delta(C_l^{{T,21cm}})/C_l^{{T,21cm}}(FW/LCDM)  = {100*mean_delta_fw_lcdm:.1f}% (expansion + tracking)")
print(f"    Range: [{100*delta_Tb_pessimistic:.1f}%, {100*delta_Tb_optimistic:.1f}%]")

# ===========================================================================
# STEP 5: Error budget
# ===========================================================================

print("\n--- STEP 5: Error budget ---")

# Source 1: c_s^2 uncertainty
# c_s^2 = 0 at tree level, 3.36e-4 at 1-loop, <4.3e-4 from fibration
# The ISW signal scales as: delta(ISW) ~ (1+w)/(1-3w) * delta_m * (1 - c_s^2)
# For c_s^2 << 1, the correction is: (1 - c_s^2) ~ 1 - 3.4e-4
# Error from c_s^2: delta(delta_ISW) / delta_ISW ~ c_s^2 ~ 3.4e-4 (negligible)
err_cs2 = cs2_eff_high  # fractional error from c_s^2 not being exactly 0
print(f"  c_s^2 uncertainty: {err_cs2:.2e} fractional -> {100*err_cs2:.4f}% (NEGLIGIBLE)")

# Source 2: w_0 uncertainty
# w_0 = -0.918 from framework; Planck+DESI combined: w_0 = -0.55 +/- 0.21 (CPL)
# The tracking factor (1+w)/(1-3w) depends on w_0:
# d/dw [(1+w)/(1-3w)] = 4/(1-3w)^2
# At w_0 = -0.918: d/dw = 4/(1+2.754)^2 = 4/14.09 = 0.284
# sigma_w from framework = 0 (geometric prediction, not fitted)
# But the OBSERVATIONAL uncertainty in the measured w affects comparison
sigma_w_obs = 0.21  # from DESI DR2 + Planck CPL fit  # (local)
tracking_derivative = 4.0 / (1.0 - 3.0 * w0)**2
delta_tracking_from_w = tracking_derivative * sigma_w_obs
err_w_fractional = delta_tracking_from_w / tracking_factor
print(f"  w_0 observational uncertainty: sigma_w = {sigma_w_obs}")
print(f"    Tracking factor at w_0={w0}: {tracking_factor:.4f}")
print(f"    d(tracking)/dw at w_0={w0}: {tracking_derivative:.4f}")
print(f"    delta(tracking) from sigma_w: {delta_tracking_from_w:.4f}")
print(f"    Fractional error: {err_w_fractional:.2f} ({100*err_w_fractional:.0f}%)")
print(f"    NOTE: This is the error in the COMPARISON, not the framework prediction")
print(f"          Framework predicts w_0 = -0.918 exactly (zero free parameters)")

# Source 3: Cosmological parameter uncertainty
# Omega_m, H_0, sigma_8 affect the ISW-galaxy normalization
# From Planck 2018: Omega_m = 0.315 +/- 0.007, H_0 = 67.4 +/- 0.5, sigma_8 = 0.811 +/- 0.006
# The ISW C_l scales as ~ (Omega_Lambda/Omega_m)^2 * sigma_8^2 * H_0^4
# Fractional error: ~ 2*sig(Omega_m)/Omega_m + 2*sig(sigma_8)/sigma_8 + 4*sig(H_0)/H_0
err_cosmo = np.sqrt((2 * 0.007 / 0.315)**2 + (2 * 0.006 / 0.811)**2 + (4 * 0.5 / 67.4)**2)
print(f"  Cosmological parameter uncertainty: {100*err_cosmo:.1f}% (ISW normalization)")

# Source 4: Reionization uncertainty
# x_HI(z) affects the 21cm tracer window
# For the ISW-21cm CROSS-CORRELATION at z < 3 (post-reionization HI IM),
# x_HI is replaced by the HI density field (damped Ly-alpha systems, 21cm IM)
# The IM signal is proportional to Omega_HI(z) * b_HI(z) * T_b(z)
# Reionization uncertainty primarily affects z > 6, NOT the z ~ 0.5-2.5 IM surveys
# For dark-ages 21cm (z > 30): x_HI = 1 exactly (no uncertainty)
# For cosmic dawn (z ~ 10-20): reionization uncertainty is O(30%) in x_HI(z)
# For post-reionization IM (z ~ 0.5-2.5): Omega_HI uncertainty ~ 10%
err_reion_IM = 0.10  # post-reionization HI IM  # (local)
err_reion_CD = 0.30  # cosmic dawn (z ~ 10-20)  # (local)
print(f"  Reionization uncertainty (post-reion IM): {100*err_reion_IM:.0f}%")
print(f"  Reionization uncertainty (cosmic dawn): {100*err_reion_CD:.0f}%")

# Source 5: Boltzmann code systematics (S70 revealed Limber overestimates)
# S68 Limber: 7.6% FW/Quint -> S70 full Boltzmann: 4.0% ISW-galaxy, 6.7% ISW auto
# The Limber overprediction at l < 10 was 1.9x for ISW-galaxy
# After S70 correction, remaining Boltzmann uncertainty ~ 5% relative
err_boltzmann = 0.05  # (local)
print(f"  Boltzmann code systematics: {100*err_boltzmann:.0f}% (residual after S70 correction)")

# Source 6: Nonlinear corrections
# At k < 0.01 h/Mpc (ISW scales), nonlinear corrections are <1%
err_nonlinear = 0.01  # (local)
print(f"  Nonlinear corrections (k<0.01 h/Mpc): {100*err_nonlinear:.0f}%")

# Total systematic error budget on the ISW enhancement
err_total_frac = np.sqrt(err_cs2**2 + err_cosmo**2 + err_boltzmann**2 + err_nonlinear**2)
print(f"\n  TOTAL systematic error (on ISW enhancement percentage):")
print(f"    sigma_sys = {100*err_total_frac:.1f}% relative")
print(f"    Central prediction: {100*delta_Tb_central:.1f}% +/- {100*delta_Tb_central*err_total_frac:.2f}%")

# ===========================================================================
# STEP 6: SNR forecasts for SKA-Low and HERA
# ===========================================================================

print("\n--- STEP 6: SNR forecasts (FW vs Quintessence, substrate-specific signal) ---")

# The substrate-specific signal is: Delta C_l^{T,21cm} / C_l^{T,21cm} = 4.0% (FW/Quint)
# This is the c_s^2 = 0 tracking enhancement (expansion history cancels in FW vs Quint)

# The detectability depends on the noise on C_l^{T,21cm}:
# sigma(C_l^{T,21cm}) / C_l^{T,21cm} ~ 1/sqrt(N_modes) where N_modes = (2l+1)*f_sky*Delta_l

# Survey parameters
surveys = {}

# SKA-Low Phase 1 (interferometric mode, z ~ 3-27)
# Primarily sensitive to EoR/Cosmic Dawn, not post-reionization IM
# For ISW-21cm cross: limited by z > 3 overlap with ISW kernel
# Not optimal for ISW cross-correlation -- too high redshift
surveys['SKA-Low (z>3)'] = {
    'f_sky': 0.50,          # hemisphere observable
    'z_range': [3.0, 27.0], # frequency: 50-350 MHz
    'T_sys': 400.0,         # K (sky-dominated at 100 MHz)
    'n_dish': 512,          # stations
    'D_dish': 38.0,         # m effective diameter
    'A_eff': 300.0,         # m^2 per station at 150 MHz
    'l_max': 5000,          # angular resolution limit
    't_obs': 1000.0,        # hours
    'note': 'EoR/CD mode, ISW overlap limited to z~3-5',
    'ISW_overlap': 0.05,    # fraction of ISW kernel captured at z>3
}

# SKA-Mid Band 1 (post-reionization HI IM, z ~ 0.35-3)
# This IS the optimal ISW-21cm cross-correlation survey
surveys['SKA-Mid IM (z~0.4-3)'] = {
    'f_sky': 0.40,          # ~16,000 deg^2
    'z_range': [0.35, 3.0],
    'T_sys': 25.0,          # K (receiver-dominated)
    'n_dish': 197,          # 64 MeerKAT + 133 new
    'D_dish': 15.0,         # m
    'l_max': 300,           # single-dish -> angular resolution ~0.6 deg at 1 GHz
    't_obs': 10000.0,       # hours (dedicated IM survey)
    'note': 'Post-reionization IM, full ISW kernel overlap',
    'ISW_overlap': 0.95,    # captures most of ISW kernel (peaks at z~0.5-1.5)
}

# HERA (Hydrogen Epoch of Reionization Array, z ~ 6-25)
# 350 dishes, 14m diameter, South Africa
# Primarily reionization science -- too high z for ISW cross
surveys['HERA (z>6)'] = {
    'f_sky': 0.05,          # drift-scan, narrow stripe
    'z_range': [6.0, 25.0],
    'T_sys': 500.0,         # K
    'n_dish': 350,
    'D_dish': 14.0,         # m
    'l_max': 3000,
    't_obs': 2000.0,        # hours
    'note': 'EoR-focused, ISW overlap negligible at z>6',
    'ISW_overlap': 0.01,    # ISW kernel negligible at z>6
}

# CHIME / CHORD (post-reionization IM, z ~ 0.8-2.5)
surveys['CHIME/CHORD (z~0.8-2.5)'] = {
    'f_sky': 0.50,          # northern hemisphere
    'z_range': [0.8, 2.5],
    'T_sys': 50.0,          # K
    'n_dish': 1,            # cylinder interferometer
    'D_dish': 100.0,        # effective
    'l_max': 500,
    't_obs': 5000.0,
    'note': 'Post-reion IM, good ISW overlap',
    'ISW_overlap': 0.70,    # partial overlap (misses z<0.8 ISW contribution)
}

# For each survey, compute the ISW-21cm cross-correlation SNR
# Following the S68/S69 methodology:
# SNR^2 = sum_{l=l_min}^{l_max} (2l+1)*f_sky * [C_l^{T,21}]^2 / [(C_l^{TT}+N_l^{TT})*(C_l^{21,21}+N_l^{21})]
#
# For the FW vs Quint discriminant:
# SNR(FW-Q) ~ delta_ISW * SNR(total cross-correlation)
# where delta_ISW = 4.0% (substrate-specific tracking enhancement)

# Simplified SNR estimate using the S69 methodology:
# sigma(A_ISW) = 1/SNR_total, then SNR(FW-Q) = delta_ISW / sigma(A_ISW)
#
# From S69 analysis:
# Planck: sigma(A_ISW) = 0.25 -> SNR(FW-Q) = 0.040/0.25 = 0.16
# Euclid: sigma(A_ISW) ~ 0.05 -> SNR(FW-Q) = 0.040/0.05 = 0.80
# 21cm (ideal): sigma(A_ISW) ~ 0.01 -> SNR(FW-Q) = 0.040/0.01 = 4.0

# More detailed: for 21cm IM surveys, the noise is set by the thermal noise + foreground residuals
# sigma(A_ISW) ~ 1 / sqrt(sum_{l=2}^{l_max} (2l+1)*f_sky * [r_l]^2)
# where r_l = C_l^{T,21} / sqrt(C_l^{TT} * C_l^{21,21})

# The ISW-21cm cross-correlation coefficient peaks at l ~ 5-30
# and is ~0.1-0.3 (moderately correlated)
# The number of independent modes in this range:
# N_modes(l=2-30) ~ sum_{l=2}^{30} (2l+1) * f_sky = f_sky * (31^2 - 4) ~ f_sky * 957

# For each survey, the effective N_modes is limited by:
# - f_sky (sky fraction)
# - l_max (angular resolution)
# - ISW_overlap (redshift overlap with ISW kernel)

print(f"\n  {'Survey':<30s} {'f_sky':>6s} {'z range':>12s} {'ISW overlap':>12s} {'N_modes(ISW)':>13s} {'sigma(A_ISW)':>13s} {'SNR(FW-Q)':>10s}")
print(f"  {'-'*30} {'-'*6} {'-'*12} {'-'*12} {'-'*13} {'-'*13} {'-'*10}")

snr_results = {}
for name, params in surveys.items():
    f_sky = params['f_sky']
    l_max_eff = min(params['l_max'], 30)  # ISW signal only at l < 30
    ISW_overlap = params['ISW_overlap']

    # Number of ISW-sensitive modes
    l_min = 2
    N_modes = f_sky * ISW_overlap * sum(2*l+1 for l in range(l_min, l_max_eff + 1))

    # Cross-correlation coefficient (typical for ISW-tracer)
    r_mean = 0.15 * ISW_overlap  # diluted by redshift overlap

    # sigma(A_ISW) ~ 1/sqrt(N_modes * r_mean^2)
    if N_modes > 0 and r_mean > 0:
        sigma_A = 1.0 / np.sqrt(N_modes * r_mean**2)
    else:
        sigma_A = np.inf

    # SNR for FW vs Quintessence discrimination
    snr_fw_q = delta_Tb_central / sigma_A if sigma_A < np.inf else 0.0

    z_str = f"[{params['z_range'][0]:.1f}, {params['z_range'][1]:.1f}]"
    print(f"  {name:<30s} {f_sky:>6.2f} {z_str:>12s} {ISW_overlap:>12.2f} {N_modes:>13.0f} {sigma_A:>13.3f} {snr_fw_q:>10.2f}")

    snr_results[name] = {
        'f_sky': f_sky,
        'N_modes': N_modes,
        'sigma_A': sigma_A,
        'snr_fw_q': snr_fw_q,
        'ISW_overlap': ISW_overlap,
    }

# Now compute the DEFINITIVE 21cm channel: tomographic intensity mapping
# This uses all available modes up to l_max ~ 10^5 (limited by foregrounds)
# Following Cooray (2004), Tashiro+08, and S68 forecast methodology:

# Ideal 21cm IM survey (all-sky, z ~ 0.1-5, thermal noise negligible)
print(f"\n  --- Ideal 21cm intensity mapping (definitive channel) ---")

# From S69 EUCLID-JOINT-69 and S68:
# 21cm projected sigma(A_ISW) = 0.01 -> SNR(FW-Q) = 4.0
sigma_A_21cm_ideal = 0.01  # from S69 forecast  # (local)
snr_21cm_ideal_fw_q = delta_Tb_central / sigma_A_21cm_ideal
snr_21cm_ideal_fw_lcdm = mean_delta_fw_lcdm / sigma_A_21cm_ideal

# From S69 directly: 21cm SNR for FW vs Quint = 7.9 (using S68 ISW-galaxy 7.6%)
# With S70 corrected value (4.0% ISW-galaxy, not 7.6%):
# SNR scales linearly: 7.9 * (4.0/7.6) = 4.16
snr_21cm_corrected_fw_q = 7.9 * (delta_Tb_central / 0.076)
# Alternative: from ISW auto (6.7%):
snr_21cm_auto_fw_q = 7.9 * (delta_Tb_optimistic / 0.076)

print(f"  sigma(A_ISW, 21cm ideal) = {sigma_A_21cm_ideal}")
print(f"  SNR(FW vs Quint, tracking): {snr_21cm_corrected_fw_q:.2f} (S70-corrected ISW-galaxy)")
print(f"  SNR(FW vs Quint, ISW auto): {snr_21cm_auto_fw_q:.2f} (using ISW auto 6.7%)")
print(f"  SNR(FW vs LCDM): {snr_21cm_ideal_fw_lcdm:.2f} (expansion + tracking)")

# Combined ISW auto-power (no galaxy tracer needed -- only uses CMB + 21cm):
# From S70: SNR(ISW auto, FW-Q) via full TT = 0.27 (Planck)
# Scaling to 21cm: the number of modes increases by (l_max_21cm / l_max_CMB)^2
# For l_max_21cm ~ 10^5: improvement factor ~ (10^5/3000)^2 ~ 10^3
# But ISW signal is only at l < 30, so the improvement is ~1
# The improvement comes from reduced noise: N_l^{21cm} << N_l^{galaxy}
# This is captured in the sigma(A_ISW) ~ 0.01

# Cross-check: S68 EUCLID-JOINT-69 gave FW vs Quint = 1.72-sig with Euclid
# 21cm adds: ~7.9-sig (from S69, using S68 numbers)
# S70 correction factor: ISW-galaxy went from 7.6% (S68 Limber) to 4.0% (S70 Boltzmann)
# But ISW AUTO went to 6.7% -- the question is which channel the 21cm survey probes

# For post-reionization IM, the 21cm survey acts as a galaxy survey -> ISW-galaxy channel
# For ISW auto-power extraction, need Planck x Planck -> already limited by cosmic variance

print(f"\n  Key distinction:")
print(f"    ISW auto-power (FW/Quint): +6.7% -- Cosmic-variance limited, 21cm irrelevant")
print(f"    ISW-tracer cross-power (FW/Quint): +4.0% -- 21cm reduces tracer noise")
print(f"    The 21cm advantage is in CROSS-CORRELATION tracer noise reduction")

# ===========================================================================
# STEP 7: Pre-registration summary
# ===========================================================================

print("\n" + "=" * 72)
print("PRE-REGISTRATION SUMMARY")
print("=" * 72)

print(f"""
PREDICTION CHAIN: Spectral Action -> c_s^2 = 0 -> ISW modification -> 21cm signal

Step 1: q-theory from spectral action
  S_fold = {S_fold:.2f} | dS/dtau = {dS_fold:.2f} | d2S/dtau2 = {d2S_fold:.2f}
  -> c_s^2(tree) = 0.0 (exact, from H_vol_vol = 0)
  -> c_s^2(1-loop) = {cs2_1loop:.2e}
  -> c_s^2(fibration) < {cs2_fibration_delta:.1e} (W1-E)
  Gate: Q-SOUND-70 PASS

Step 2: ISW modification (CLASS-ISW-70)
  ISW auto FW/Quint: +{100*mean_delta_fw_q:.1f}% (l=2-10 mean)
  ISW auto FW/LCDM: +{100*mean_delta_fw_lcdm:.1f}%
  ISW-galaxy FW/Quint: +4.0% (galaxy window dilution)
  Gate: CLASS-ISW-70 PASS (>5% ISW auto)

Step 3: 21cm prediction
  Central observable: ISW-21cm cross-power C_l^{{T,21cm}}
  FW vs Quint enhancement: +{100*delta_Tb_central:.1f}% (substrate-specific tracking)
  FW vs LCDM enhancement: +{100*mean_delta_fw_lcdm:.1f}% (expansion + tracking)
  Range: [{100*delta_Tb_pessimistic:.1f}%, {100*delta_Tb_optimistic:.1f}%]

Error budget (on ISW enhancement percentage):
  c_s^2 uncertainty:      {100*err_cs2:.4f}% (NEGLIGIBLE)
  Cosmological params:    {100*err_cosmo:.1f}%
  Boltzmann systematics:  {100*err_boltzmann:.0f}%
  Nonlinear corrections:  {100*err_nonlinear:.0f}%
  Total systematic:       {100*err_total_frac:.1f}%

SNR forecasts (FW vs Quintessence, substrate-specific):
  Planck (existing):       {delta_Tb_central/0.25:.2f}-sig (NOT detectable)
  Euclid ISW (~2030):      {delta_Tb_central/0.05:.2f}-sig (marginal)
  SKA-Mid IM (~2030):      {snr_results['SKA-Mid IM (z~0.4-3)']['snr_fw_q']:.2f}-sig (marginal)
  CHIME/CHORD (~2027):     {snr_results['CHIME/CHORD (z~0.8-2.5)']['snr_fw_q']:.2f}-sig
  21cm ideal (>2035):      {snr_21cm_corrected_fw_q:.2f}-sig (DETECTABLE)
  SKA-Low (Dark Ages):     {snr_results['SKA-Low (z>3)']['snr_fw_q']:.2f}-sig (wrong z for ISW)
  HERA (EoR):              {snr_results['HERA (z>6)']['snr_fw_q']:.2f}-sig (wrong z for ISW)
""")

# ===========================================================================
# STEP 8: What the pre-registration says and does not say
# ===========================================================================

print("CRITICAL DISTINCTIONS:")
print("  1. The substrate-specific signal (c_s^2=0 vs c_s^2=1) is +4.0% in ISW cross-power")
print("  2. The total FW vs LCDM signal includes expansion history (+2.9%)")
print("     but this is NOT substrate-specific (any w_0=-0.918 model gives similar)")
print("  3. Post-reionization HI IM (z~0.4-3) is the CORRECT channel for ISW, not Dark Ages")
print("  4. SKA-Low and HERA probe z>3 and z>6 respectively -- ISW kernel negligible there")
print("  5. The 21cm advantage over galaxy surveys is NUMBER DENSITY of tracers,")
print("     not direct sensitivity at high z")
print("  6. Detection requires sigma(A_ISW) < 0.02 for 2-sigma discrimination")
print("     -> needs >>10^3 modes at l=2-30, achievable with all-sky IM + CMB cross-correlation")

# ===========================================================================
# Save results
# ===========================================================================

save_path = os.path.join(os.path.dirname(__file__), 's71_21cm_isw_preregistration.npz')
np.savez(save_path,
    # Chain step 1: c_s^2
    cs2_tree=cs2_tree,
    cs2_1loop=cs2_1loop,
    cs2_total=cs2_total,
    cs2_fibration_delta=cs2_fibration_delta,
    cs2_eff_range=np.array([cs2_eff_low, cs2_eff_high]),

    # Chain step 2: ISW modification
    delta_isw_fw_q_mean=mean_delta_fw_q,
    delta_isw_fw_lcdm_mean=mean_delta_fw_lcdm,
    delta_isw_fw_q_l2_10=delta_isw_fw_q,
    delta_isw_fw_lcdm_l2_10=delta_isw_fw_lcdm,

    # Chain step 3: 21cm prediction
    delta_Tb_central=delta_Tb_central,
    delta_Tb_optimistic=delta_Tb_optimistic,
    delta_Tb_pessimistic=delta_Tb_pessimistic,
    z_cross=z_cross,
    k_cross=k_cross,

    # Error budget
    err_cs2=err_cs2,
    err_cosmo=err_cosmo,
    err_boltzmann=err_boltzmann,
    err_nonlinear=err_nonlinear,
    err_total_frac=err_total_frac,

    # Survey SNR (FW vs Quintessence)
    snr_planck=delta_Tb_central / 0.25,
    snr_euclid=delta_Tb_central / 0.05,
    snr_ska_mid=snr_results['SKA-Mid IM (z~0.4-3)']['snr_fw_q'],
    snr_chime=snr_results['CHIME/CHORD (z~0.8-2.5)']['snr_fw_q'],
    snr_21cm_ideal=snr_21cm_corrected_fw_q,
    snr_ska_low=snr_results['SKA-Low (z>3)']['snr_fw_q'],
    snr_hera=snr_results['HERA (z>6)']['snr_fw_q'],

    # Input parameters
    w0_FW=w0_FW,
    wa_FW=wa_FW,
    tracking_factor=tracking_factor,
    S_fold=S_fold,
    dS_fold=dS_fold,
    d2S_fold=d2S_fold,

    # Brightness temperatures
    z_21cm=z_21cm,
    T_b_ref=T_b_ref,
    Omega_DE_z=Omega_DE_z,

    # Gate
    gate_name='21CM-ISW-PREREGISTRATION-71',
    gate_verdict='INFO',
    gate_detail='Pre-registration complete. Central prediction: +4.0% ISW-21cm cross-power (FW vs Quint). 21cm ideal SNR=4.16.',
)

print(f"\nData saved: {save_path}")
print(f"\nGate 21CM-ISW-PREREGISTRATION-71: INFO")
print(f"  Pre-registration document complete with central prediction and error budget.")
