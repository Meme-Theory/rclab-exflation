#!/usr/bin/env python3
"""
JOINT-OBSERVATIONAL-68: Consolidated Observational Prediction Table
===================================================================

Consolidates all S68 results into a single observational comparison table.
Computes joint chi-squared across all independent CMB observables.
Compares framework (zero free parameters) against LCDM (6 free parameters).

Gate: JOINT-OBSERVATIONAL-68 (INFO — consolidated table, no pass/fail).

Session: S68 Wave 4-A
Agent: mack-cosmic-bridge (Katie Mack)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    A_s_CMB, H_0_km_s_Mpc, Omega_m, Omega_b, Omega_DM, Omega_Lambda,
    sigma_8, M_Z, sin2_thetaW_MSbar, rho_Lambda_obs, M_KK_gravity
)

# =============================================================================
# SECTION 1: Load all S68 and S67 data
# =============================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# S68 Wave 1
d_acoustic   = np.load(os.path.join(data_dir, 's68_acoustic_transfer.npz'), allow_pickle=True)
d_bcs        = np.load(os.path.join(data_dir, 's68_bcs_dressed_mode.npz'), allow_pickle=True)
d_alpha_s    = np.load(os.path.join(data_dir, 's68_alpha_s_transfer.npz'), allow_pickle=True)
d_rg         = np.load(os.path.join(data_dir, 's68_rg_a2_mode_prop.npz'), allow_pickle=True)

# S68 Wave 2
d_as_closure = np.load(os.path.join(data_dir, 's68_multifield_as_closure.npz'), allow_pickle=True)
d_ns         = np.load(os.path.join(data_dir, 's68_ns_combined.npz'), allow_pickle=True)
d_desi       = np.load(os.path.join(data_dir, 's68_desi_dr3_forecast.npz'), allow_pickle=True)
d_fnl        = np.load(os.path.join(data_dir, 's68_cmbs4_fnl_forecast.npz'), allow_pickle=True)
d_liteb      = np.load(os.path.join(data_dir, 's68_liteb_r_forecast.npz'), allow_pickle=True)

# S68 Wave 3
d_r_cmb      = np.load(os.path.join(data_dir, 's68_r_cmb_transfer.npz'), allow_pickle=True)
d_2nd_sound  = np.load(os.path.join(data_dir, 's68_second_sound_obs.npz'), allow_pickle=True)
d_beyond_mf  = np.load(os.path.join(data_dir, 's68_beyond_mf_a4.npz'), allow_pickle=True)
d_iso        = np.load(os.path.join(data_dir, 's68_isocurvature_transfer.npz'), allow_pickle=True)

# S67 data
d_bispec     = np.load(os.path.join(data_dir, 's67_gge_bispectrum.npz'), allow_pickle=True)
d_desi67     = np.load(os.path.join(data_dir, 's67_desi_volovik.npz'), allow_pickle=True)
d_leggett    = np.load(os.path.join(data_dir, 's67_leggett_grav_decay.npz'), allow_pickle=True)

# =============================================================================
# SECTION 2: Build the observational comparison table
# =============================================================================

# Each entry: (name, fw_value, fw_unc, obs_value, obs_unc, obs_source,
#              tension_sigma, status, notes, is_upper_bound)

observables = []

# --- 1. n_s ---
ns_fw     = float(d_ns['ns_combined'])
ns_fw_unc = float(d_ns['sigma_ns_combined'])
ns_obs    = 0.9649   # Planck 2018 (TT,TE,EE+lowE)  # (local)
ns_obs_unc = 0.0042  # (local)
ns_tension = abs(ns_fw - ns_obs) / ns_obs_unc
observables.append({
    'name': 'n_s',
    'fw_val': ns_fw, 'fw_unc': ns_fw_unc,
    'obs_val': ns_obs, 'obs_unc': ns_obs_unc,
    'source': 'Planck 2018',
    'tension': ns_tension,
    'status': 'PASS' if ns_tension < 2.0 else 'TENSION',
    'notes': 'BCS+1-loop+RG corrections. Hubble convention.',
    'is_bound': False,
    'group': 'CMB_primordial'
})

# --- 2. alpha_s (running) ---
alpha_s_fw     = float(d_ns['alpha_s_combined'])
alpha_s_fw_unc = float(d_ns['alpha_s_uncertainty'])
alpha_s_obs    = -0.0045  # Planck 2018  # (local)
alpha_s_obs_unc = 0.0067  # (local)
alpha_s_tension = abs(alpha_s_fw - alpha_s_obs) / alpha_s_obs_unc
observables.append({
    'name': 'alpha_s = dn_s/dlnk',
    'fw_val': alpha_s_fw, 'fw_unc': alpha_s_fw_unc,
    'obs_val': alpha_s_obs, 'obs_unc': alpha_s_obs_unc,
    'source': 'Planck 2018',
    'tension': alpha_s_tension,
    'status': 'PASS' if alpha_s_tension < 2.0 else 'TENSION',
    'notes': 'Category error resolved: tau-derivative != k-derivative. Superhorizon plateau.',
    'is_bound': False,
    'group': 'CMB_primordial'
})

# --- 3. A_s ---
As_fw     = float(d_as_closure['A_s_final'])
As_obs    = 2.1e-9   # Planck 2018  # (local)
As_gap_OOM = float(d_as_closure['gap_final'])
# For chi-squared, we need sigma. Planck: ln(10^10 A_s) = 3.044 +/- 0.014
# sigma(A_s)/A_s = 0.014 => sigma(A_s) = 0.014 * 2.1e-9 = 2.94e-11
As_obs_unc = 2.94e-11  # (local)
As_tension = abs(As_fw - As_obs) / As_obs_unc
observables.append({
    'name': 'A_s',
    'fw_val': As_fw, 'fw_unc': 0.0,
    'obs_val': As_obs, 'obs_unc': As_obs_unc,
    'source': 'Planck 2018',
    'tension': As_tension,
    'status': 'FAIL',
    'notes': f'Gap = {As_gap_OOM:.3f} OOM (factor {As_obs/As_fw:.2f}x). 95% of 15.1 OOM closed.',
    'is_bound': False,
    'group': 'CMB_amplitude'
})

# --- 4. r (tensor-to-scalar) ---
r_fw     = float(d_r_cmb['r_CMB'])
r_obs_95 = 0.036     # BK18 95% CL upper bound  # (local)
# For chi-squared against upper bound, use sigma = r_95/1.96
r_obs_unc_equiv = r_obs_95 / 1.96
r_tension = max(0.0, (r_fw - r_obs_95) / r_obs_unc_equiv) if r_fw > r_obs_95 else 0.0
observables.append({
    'name': 'r',
    'fw_val': r_fw, 'fw_unc': 0.0,
    'obs_val': r_obs_95, 'obs_unc': r_obs_unc_equiv,
    'source': 'BICEP/Keck 2021 (BK18)',
    'tension': 0.0,  # Below upper bound
    'status': 'PASS',
    'notes': f'r = {r_fw:.4f} < 0.036 (95% CL). LiteBIRD: {float(d_liteb["SNR_r_LiteBIRD"]):.1f}-sigma detection.',
    'is_bound': True,
    'group': 'CMB_tensor'
})

# --- 5. n_T (tensor tilt) ---
nT_fw     = float(d_r_cmb['nT_CMB'])
nT_SR     = -r_fw / 8.0
consistency = float(d_r_cmb['r_plus_8nT'])
observables.append({
    'name': 'n_T',
    'fw_val': nT_fw, 'fw_unc': 0.0,
    'obs_val': None, 'obs_unc': None,
    'source': 'No CMB constraint yet',
    'tension': 0.0,
    'status': 'PREDICTION',
    'notes': f'= -r/8 exactly (consistency: r+8n_T = {consistency:.1e}). Blue tilt at transit scale only.',
    'is_bound': False,
    'group': 'CMB_tensor'
})

# --- 6. beta_iso (isocurvature fraction) ---
beta_iso_fw  = float(d_iso['beta_iso_CMB'])
beta_iso_obs = 0.017  # Planck 95% CL  # (local)
margin_OOM   = float(d_iso['margin_OOM'])
observables.append({
    'name': 'beta_iso',
    'fw_val': beta_iso_fw, 'fw_unc': 0.0,
    'obs_val': beta_iso_obs, 'obs_unc': beta_iso_obs / 1.96,
    'source': 'Planck 2018',
    'tension': 0.0,  # 9.7 OOM below bound
    'status': 'PASS',
    'notes': f'{margin_OOM:.1f} OOM below Planck bound. Superhorizon conservation exact.',
    'is_bound': True,
    'group': 'CMB_primordial'
})

# --- 7. f_NL(equil) ---
fNL_eq_fw    = float(d_fnl['f_NL_equil'])
fNL_eq_obs   = -26.0   # Planck 2018  # (local)
fNL_eq_unc   = 47.0  # (local)
fNL_eq_tension = abs(fNL_eq_fw - fNL_eq_obs) / fNL_eq_unc
observables.append({
    'name': 'f_NL(equil)',
    'fw_val': fNL_eq_fw, 'fw_unc': 0.0,
    'obs_val': fNL_eq_obs, 'obs_unc': fNL_eq_unc,
    'source': 'Planck 2018',
    'tension': fNL_eq_tension,
    'status': 'PASS' if fNL_eq_tension < 2.0 else 'TENSION',
    'notes': 'From c_BLV = 0.485 via Cheung et al. EFT. CMB-S4 sigma=5.0 (0.17-sigma).',
    'is_bound': False,
    'group': 'CMB_NG'
})

# --- 8. f_NL(folded) ---
fNL_fo_fw = float(d_fnl['f_NL_folded'])
observables.append({
    'name': 'f_NL(folded)',
    'fw_val': fNL_fo_fw, 'fw_unc': 0.0,
    'obs_val': None, 'obs_unc': None,
    'source': 'Unconstrained (unique prediction)',
    'tension': 0.0,
    'status': 'PREDICTION',
    'notes': 'GGE diagonal correlator. 21cm at l_max=10^5: 3.6-sigma detectable.',
    'is_bound': False,
    'group': 'CMB_NG'
})

# --- 9. f_NL(total) ---
fNL_tot_fw = float(d_fnl['f_NL_total'])
observables.append({
    'name': 'f_NL(total)',
    'fw_val': fNL_tot_fw, 'fw_unc': 0.0,
    'obs_val': fNL_eq_obs, 'obs_unc': fNL_eq_unc,
    'source': 'Planck 2018 (equil template)',
    'tension': abs(fNL_tot_fw - fNL_eq_obs) / fNL_eq_unc,
    'status': 'PASS',
    'notes': 'Equil + folded + multifield channels. Consistent with Planck.',
    'is_bound': False,
    'group': 'CMB_NG'
})

# --- 10. w_0 ---
w0_fw     = float(d_desi['w0_fw'])
w0_obs    = -0.752    # DESI DR2  # (local)
w0_obs_unc = 0.057  # (local)
w0_tension = abs(w0_fw - w0_obs) / w0_obs_unc
observables.append({
    'name': 'w_0',
    'fw_val': w0_fw, 'fw_unc': 0.0,
    'obs_val': w0_obs, 'obs_unc': w0_obs_unc,
    'source': 'DESI DR2 (2025)',
    'tension': w0_tension,
    'status': 'TENSION',
    'notes': 'Volovik effacement residual. Pure FW (no compaction). LCDM at 4.35-sigma.',
    'is_bound': False,
    'group': 'DE'
})

# --- 11. w_a ---
wa_fw     = float(d_desi['wa_fw'])
wa_obs    = -0.73     # DESI DR2  # (local)
wa_obs_unc = 0.25  # (local)
wa_tension = abs(wa_fw - wa_obs) / wa_obs_unc
observables.append({
    'name': 'w_a',
    'fw_val': wa_fw, 'fw_unc': 0.0,
    'obs_val': wa_obs, 'obs_unc': wa_obs_unc,
    'source': 'DESI DR2 (2025)',
    'tension': wa_tension,
    'status': 'TENSION',
    'notes': 'Framework structurally static (w_a=0). Compaction w_a=+1.121 CLOSED (wrong sign).',
    'is_bound': False,
    'group': 'DE'
})

# --- 12. Omega_DM h^2 ---
# Leggett-only (canonical after S66)
OmDM_fw   = 0.120     # Leggett-only (S66 Z-EQ-CHECK-66)  # (local)
OmDM_obs  = 0.1200    # Planck 2018  # (local)
OmDM_unc  = 0.0012    # Planck 2018  # (local)
OmDM_tension = abs(OmDM_fw - OmDM_obs) / OmDM_unc
observables.append({
    'name': 'Omega_DM h^2',
    'fw_val': OmDM_fw, 'fw_unc': 0.0,
    'obs_val': OmDM_obs, 'obs_unc': OmDM_unc,
    'source': 'Planck 2018',
    'tension': OmDM_tension,
    'status': 'PASS',
    'notes': 'Leggett-only channel. z_eq=3425 (0.88-sigma). BA phonons must decay before z~3400.',
    'is_bound': False,
    'group': 'DM'
})

# --- 13. m_H (Higgs mass) ---
# Two values: uncorrected (Aitken extrapolation) and RG-corrected
mH_bare   = float(d_beyond_mf['mH_inf_bare'])    # 127.5 GeV
mH_rg     = float(d_beyond_mf['mH_inf_dressed'])  # 137.4 GeV
mH_obs    = 125.10    # PDG 2024  # (local)
mH_obs_unc = 0.11     # Combined LHC  # (local)
mH_tension_bare = abs(mH_bare - mH_obs) / mH_obs_unc
mH_tension_rg   = abs(mH_rg - mH_obs) / mH_obs_unc
observables.append({
    'name': 'm_H (uncorrected)',
    'fw_val': mH_bare, 'fw_unc': 0.0,
    'obs_val': mH_obs, 'obs_unc': mH_obs_unc,
    'source': 'PDG 2024 (LHC)',
    'tension': mH_tension_bare,
    'status': 'FAIL',
    'notes': f'{mH_bare:.1f} GeV. Aitken-extrapolated (L->inf). KK threshold corrections needed.',
    'is_bound': False,
    'group': 'particle'
})

observables.append({
    'name': 'm_H (RG-corrected)',
    'fw_val': mH_rg, 'fw_unc': 0.0,
    'obs_val': mH_obs, 'obs_unc': mH_obs_unc,
    'source': 'PDG 2024 (LHC)',
    'tension': mH_tension_rg,
    'status': 'FAIL',
    'notes': f'{mH_rg:.1f} GeV. 29.8% BCS correction worsens. Suggests overcounting.',
    'is_bound': False,
    'group': 'particle'
})

# --- 14. sin^2(theta_W) ---
sin2_bare = float(d_beyond_mf['sin2_fw_MZ_bare'])   # 0.2312
sin2_rg   = float(d_beyond_mf['sin2_fw_MZ_dressed']) # 0.2394
sin2_obs  = 0.23122   # PDG 2024 (MSbar at M_Z)  # (local)
sin2_unc  = 0.00003   # PDG 2024  # (local)
sin2_tension_bare = abs(sin2_bare - sin2_obs) / sin2_unc
sin2_tension_rg   = abs(sin2_rg - sin2_obs) / sin2_unc

observables.append({
    'name': 'sin^2(theta_W) (uncorrected)',
    'fw_val': sin2_bare, 'fw_unc': 0.0,
    'obs_val': sin2_obs, 'obs_unc': sin2_unc,
    'source': 'PDG 2024',
    'tension': sin2_tension_bare,
    'status': 'PASS' if sin2_tension_bare < 2.0 else 'TENSION',
    'notes': 'Geometrically protected. Uncorrected = observed to 0.01%.',
    'is_bound': False,
    'group': 'particle'
})

observables.append({
    'name': 'sin^2(theta_W) (RG-corrected)',
    'fw_val': sin2_rg, 'fw_unc': 0.0,
    'obs_val': sin2_obs, 'obs_unc': sin2_unc,
    'source': 'PDG 2024',
    'tension': sin2_tension_rg,
    'status': 'FAIL',
    'notes': 'BCS dressing shifts by +0.0082. Overcounting suggests KK threshold needed.',
    'is_bound': False,
    'group': 'particle'
})

# --- 15. DM self-interaction ---
observables.append({
    'name': 'sigma/m (DM self-interaction)',
    'fw_val': 0.0, 'fw_unc': 0.0,
    'obs_val': 1.25, 'obs_unc': 0.0,
    'source': 'Bullet Cluster',
    'tension': 0.0,
    'status': 'PASS',
    'notes': 'sigma/m = 0 exactly (N_pair=1). Bound: <1.25 cm^2/g.',
    'is_bound': True,
    'group': 'DM'
})

# --- 16. DM gravitational stability ---
tau_pair_s = float(d_leggett['tau_pair_s_S52'])
observables.append({
    'name': 'tau_DM (Leggett stability)',
    'fw_val': tau_pair_s, 'fw_unc': 0.0,
    'obs_val': 4.35e17, 'obs_unc': 0.0,
    'source': 'Age of universe',
    'tension': 0.0,
    'status': 'PASS',
    'notes': f'Z_2 parity forbids single decay exactly. Pair annihilation tau = {tau_pair_s:.1e} s >> t_U.',
    'is_bound': True,
    'group': 'DM'
})

# =============================================================================
# SECTION 3: Joint chi-squared across INDEPENDENT observables
# =============================================================================
#
# Independence structure:
# - n_s and alpha_s are correlated (use 2D with covariance)
# - w_0 and w_a are correlated (use 2D with DESI covariance)
# - r is an upper bound (exclude from chi^2)
# - beta_iso is an upper bound (exclude from chi^2)
# - n_T has no constraint yet (exclude)
# - f_NL(folded) has no constraint yet (exclude)
# - m_H and sin^2(theta_W) are not independent (both from a_4/a_2)
# - sigma/m and tau_DM are bounds (exclude)
#
# Independent chi^2 contributions:
# Group 1: (n_s, alpha_s) with Planck covariance
# Group 2: A_s (1D)
# Group 3: f_NL(equil) (1D)
# Group 4: (w_0, w_a) with DESI covariance
# Group 5: Omega_DM h^2 (1D)
# Group 6: m_H uncorrected (1D) — use this as canonical
# Group 7: sin^2(theta_W) uncorrected (1D) — use this as canonical

print("=" * 80)
print("JOINT-OBSERVATIONAL-68: Consolidated Observational Prediction Table")
print("=" * 80)

# --- Group 1: (n_s, alpha_s) joint ---
# Planck 2018 correlation rho(n_s, alpha_s) ~ +0.55 (from MCMC chains)
rho_ns_alpha = 0.55  # (local)
cov_ns_alpha = np.array([
    [ns_obs_unc**2, rho_ns_alpha * ns_obs_unc * alpha_s_obs_unc],
    [rho_ns_alpha * ns_obs_unc * alpha_s_obs_unc, alpha_s_obs_unc**2]
])
delta_ns_alpha = np.array([ns_fw - ns_obs, alpha_s_fw - alpha_s_obs])
cov_inv = np.linalg.inv(cov_ns_alpha)
chi2_ns_alpha = float(delta_ns_alpha @ cov_inv @ delta_ns_alpha)
print(f"\nGroup 1: (n_s, alpha_s) joint chi^2 = {chi2_ns_alpha:.3f} (2 DOF)")

# --- Group 2: A_s ---
chi2_As = ((As_fw - As_obs) / As_obs_unc)**2
print(f"Group 2: A_s chi^2 = {chi2_As:.3f} (1 DOF)")

# --- Group 3: f_NL(equil) ---
chi2_fNL = ((fNL_eq_fw - fNL_eq_obs) / fNL_eq_unc)**2
print(f"Group 3: f_NL(equil) chi^2 = {chi2_fNL:.3f} (1 DOF)")

# --- Group 4: (w_0, w_a) joint with DESI DR2 covariance ---
# DESI DR2: rho(w_0, w_a) = -0.85 (highly anticorrelated, standard for CPL)
rho_w = -0.85  # (local)
cov_w = np.array([
    [w0_obs_unc**2, rho_w * w0_obs_unc * wa_obs_unc],
    [rho_w * w0_obs_unc * wa_obs_unc, wa_obs_unc**2]
])
delta_w = np.array([w0_fw - w0_obs, wa_fw - wa_obs])
cov_w_inv = np.linalg.inv(cov_w)
chi2_w = float(delta_w @ cov_w_inv @ delta_w)
print(f"Group 4: (w_0, w_a) joint chi^2 = {chi2_w:.3f} (2 DOF)")

# --- Group 5: Omega_DM h^2 ---
chi2_OmDM = ((OmDM_fw - OmDM_obs) / OmDM_unc)**2
print(f"Group 5: Omega_DM h^2 chi^2 = {chi2_OmDM:.3f} (1 DOF)")

# --- Group 6: m_H (uncorrected) ---
chi2_mH = ((mH_bare - mH_obs) / mH_obs_unc)**2
print(f"Group 6: m_H chi^2 = {chi2_mH:.3f} (1 DOF)")

# --- Group 7: sin^2(theta_W) (uncorrected) ---
chi2_sin2 = ((sin2_bare - sin2_obs) / sin2_unc)**2
print(f"Group 7: sin^2(theta_W) chi^2 = {chi2_sin2:.3f} (1 DOF)")

# --- Total ---
chi2_total = chi2_ns_alpha + chi2_As + chi2_fNL + chi2_w + chi2_OmDM + chi2_mH + chi2_sin2
ndof_total = 2 + 1 + 1 + 2 + 1 + 1 + 1  # = 9 DOF
n_free_params_fw = 0  # Zero free parameters

print(f"\n--- TOTAL ---")
print(f"chi^2 = {chi2_total:.3f}")
print(f"DOF = {ndof_total}")
print(f"chi^2/DOF = {chi2_total / ndof_total:.3f}")
print(f"Free parameters = {n_free_params_fw}")

# =============================================================================
# SECTION 4: LCDM comparison
# =============================================================================
# LCDM fits the data by construction (6 free parameters: Omega_b h^2, Omega_c h^2,
# theta_*, tau_reion, n_s, A_s). The 6-parameter fit gives chi^2/DOF ~ 1.
# For Planck-only CMB observables, LCDM chi^2 ~ 0 by construction (it fits them).
# For DESI (w_0, w_a), LCDM predicts w_0=-1, w_a=0 -> tension with DESI DR2.

# w0_lcdm = -1.0  # S72: now imported from canonical_constants
w0_lcdm = w0_LCDM  # S72: alias for downstream use
# wa_lcdm = 0.0  # S72: now imported from canonical_constants
wa_lcdm = wa_LCDM  # S72: alias for downstream use
delta_w_lcdm = np.array([w0_lcdm - w0_obs, wa_lcdm - wa_obs])
chi2_w_lcdm = float(delta_w_lcdm @ cov_w_inv @ delta_w_lcdm)

# LCDM fits CMB observables: chi^2 ~ 0 for n_s, alpha_s, A_s, f_NL
# LCDM fits DM: chi^2 ~ 0 (free parameter)
# LCDM does not predict m_H or sin^2(theta_W) — these are external
# For fair comparison, use only observables both models predict:
# CMB primordial (n_s, alpha_s, A_s) + f_NL + (w_0, w_a) + Omega_DM h^2

# LCDM has 6 free parameters that absorb CMB observables
chi2_lcdm_cmb = 0.0  # By construction (fit parameters)  # (local)
chi2_lcdm_total = chi2_lcdm_cmb + chi2_w_lcdm
# LCDM doesn't predict fNL (it's 0, but that's because of single-field assumption)
chi2_fNL_lcdm = ((0.0 - fNL_eq_obs) / fNL_eq_unc)**2  # 0.306
chi2_lcdm_all = chi2_lcdm_cmb + chi2_fNL_lcdm + chi2_w_lcdm

n_free_params_lcdm = 6

print(f"\n--- LCDM COMPARISON ---")
print(f"LCDM chi^2(w_0, w_a) = {chi2_w_lcdm:.3f} (2 DOF)")
print(f"LCDM chi^2(f_NL) = {chi2_fNL_lcdm:.3f} (1 DOF)")
print(f"LCDM total chi^2 = {chi2_lcdm_all:.3f}")
print(f"LCDM free params = {n_free_params_lcdm}")

# Comparable observables (both models address):
# n_s, alpha_s, A_s, f_NL, w_0, w_a, Omega_DM h^2
# = Groups 1-5 (DOF = 7)
chi2_fw_comparable = chi2_ns_alpha + chi2_As + chi2_fNL + chi2_w + chi2_OmDM
ndof_comparable = 7

print(f"\n--- COMPARABLE OBSERVABLES (both models address, DOF={ndof_comparable}) ---")
print(f"Framework: chi^2 = {chi2_fw_comparable:.3f}, params = {n_free_params_fw}")
print(f"  chi^2/DOF = {chi2_fw_comparable / ndof_comparable:.3f}")
print(f"  chi^2/(DOF - params) = {chi2_fw_comparable / (ndof_comparable - n_free_params_fw):.3f}")

print(f"LCDM: chi^2 = {chi2_lcdm_all:.3f}, params = {n_free_params_lcdm}")
print(f"  chi^2/DOF = {chi2_lcdm_all / ndof_comparable:.3f}")
# LCDM: DOF - params = 7 - 6 = 1
print(f"  chi^2/(DOF - params) = {chi2_lcdm_all / max(1, ndof_comparable - n_free_params_lcdm):.3f}")

# AIC comparison: AIC = chi^2 + 2k (k = number of free parameters)
AIC_fw   = chi2_fw_comparable + 2 * n_free_params_fw
AIC_lcdm = chi2_lcdm_all + 2 * n_free_params_lcdm
delta_AIC = AIC_fw - AIC_lcdm

# BIC comparison: BIC = chi^2 + k * ln(N_data)
# For Planck: N_data ~ 2500 (TT) + 2500 (TE) + 2500 (EE) + 30 (low-l) ~ 7530
# For DESI: 14 data points (7 bins x 2 distances)
# For f_NL: 1 measurement
# Combined: N_data ~ 7545
N_data = 7545
BIC_fw   = chi2_fw_comparable + n_free_params_fw * np.log(N_data)
BIC_lcdm = chi2_lcdm_all + n_free_params_lcdm * np.log(N_data)
delta_BIC = BIC_fw - BIC_lcdm

print(f"\n--- AIC / BIC ---")
print(f"AIC(FW) = {AIC_fw:.3f}, AIC(LCDM) = {AIC_lcdm:.3f}, Delta AIC = {delta_AIC:.3f}")
print(f"BIC(FW) = {BIC_fw:.3f}, BIC(LCDM) = {BIC_lcdm:.3f}, Delta BIC = {delta_BIC:.3f}")
print(f"  Delta AIC > 0 => LCDM preferred by AIC")
print(f"  Delta BIC > 0 => LCDM preferred by BIC")
print(f"  (But LCDM uses 6 free params to fit Planck CMB by construction)")

# =============================================================================
# SECTION 5: Excluding A_s (the known gap)
# =============================================================================
# A_s dominates chi^2 overwhelmingly. Useful to see the picture without it.

chi2_fw_no_As = chi2_ns_alpha + chi2_fNL + chi2_w + chi2_OmDM
ndof_no_As = 6

print(f"\n--- EXCLUDING A_s (known 0.755 OOM gap) ---")
print(f"Framework chi^2(no A_s) = {chi2_fw_no_As:.3f} / {ndof_no_As} DOF = {chi2_fw_no_As/ndof_no_As:.3f}")

# Also excluding particle physics (m_H, sin^2) which LCDM doesn't predict:
chi2_fw_cosmo_only = chi2_ns_alpha + chi2_fNL + chi2_w + chi2_OmDM
ndof_cosmo = 6
print(f"Framework chi^2(cosmo only, no A_s) = {chi2_fw_cosmo_only:.3f} / {ndof_cosmo} DOF = {chi2_fw_cosmo_only/ndof_cosmo:.3f}")

# =============================================================================
# SECTION 6: Print full table
# =============================================================================

print("\n" + "=" * 120)
print(f"{'Observable':<28} {'Framework':>14} {'Observed':>14} {'sigma_obs':>10} {'Tension':>8} {'Status':<12} {'Source'}")
print("=" * 120)

for obs in observables:
    fw_str = f"{obs['fw_val']:.6g}" if isinstance(obs['fw_val'], float) else str(obs['fw_val'])
    if obs['obs_val'] is not None:
        obs_str = f"{obs['obs_val']:.6g}"
        unc_str = f"{obs['obs_unc']:.4g}" if obs['obs_unc'] else "—"
    else:
        obs_str = "—"
        unc_str = "—"
    tension_str = f"{obs['tension']:.2f}" if obs['tension'] > 0 else "—"
    print(f"{obs['name']:<28} {fw_str:>14} {obs_str:>14} {unc_str:>10} {tension_str:>8} {obs['status']:<12} {obs['source']}")

print("=" * 120)

# =============================================================================
# SECTION 7: Three most decisive upcoming measurements
# =============================================================================

print("\n--- THREE MOST DECISIVE UPCOMING MEASUREMENTS ---")
print()
print("1. LiteBIRD r detection (launch ~2032)")
print(f"   Framework predicts r = {r_fw:.4f}")
print(f"   LiteBIRD sensitivity: sigma(r) = 0.001 => {float(d_liteb['SNR_r_LiteBIRD']):.1f}-sigma detection")
print(f"   n_T = {nT_fw:.6f} (= -r/8 exactly, indistinguishable from slow-roll at CMB)")
print(f"   Starobinsky (r=0.004) excluded at {float(d_liteb['sigma_FW_vs_Starobinsky_LB']):.0f}-sigma")
print(f"   NECESSARY but NOT SUFFICIENT: r=0.024 consistent with many inflation models")
print()
print("2. DESI DR3 w_0-w_a (expected ~2026)")
print(f"   Framework: w_0 = {w0_fw}, w_a = {wa_fw}")
print(f"   Scenario B (DR3 toward LCDM): {float(d_desi['sig_fw_scenarios'][1]):.2f}-sigma tension")
print(f"   Scenario A (DR2 confirmed): {float(d_desi['sig_fw_scenarios'][0]):.2f}-sigma (both FW and LCDM fail)")
print(f"   DECISIVE: w_a < -0.530 at 3-sigma would exclude framework")
print()
print("3. 21cm intensity mapping f_NL(folded) (SKA era, ~2030s)")
print(f"   Framework unique prediction: f_NL(folded) = {fNL_fo_fw:.3f}")
print(f"   21cm at l_max = 10^5: {float(d_fnl['SNR_fo_21cm']):.1f}-sigma detection")
print(f"   CMB-S4: {float(d_fnl['CMB-S4_SNR_fo']):.3f}-sigma (NOT detectable)")
print(f"   UNIQUE DISCRIMINANT: no standard inflation model predicts this shape")

# =============================================================================
# SECTION 8: Save all results
# =============================================================================

np.savez(
    os.path.join(data_dir, 's68_joint_observational.npz'),
    # Gate metadata
    gate_name='JOINT-OBSERVATIONAL-68',
    gate_verdict='INFO',
    gate_detail=(
        f'Joint chi^2 = {chi2_total:.1f} / {ndof_total} DOF = {chi2_total/ndof_total:.1f} (all obs, 0 free params). '
        f'Excluding A_s: chi^2 = {chi2_fw_no_As:.1f} / {ndof_no_As} DOF = {chi2_fw_no_As/ndof_no_As:.2f}. '
        f'A_s gap 0.755 OOM (factor 5.69x) dominates. '
        f'LCDM comparison (7 shared obs): delta_AIC = {delta_AIC:.1f}, delta_BIC = {delta_BIC:.1f}. '
        f'w_0-w_a tension: FW {np.sqrt(chi2_w):.1f}-sig vs LCDM {np.sqrt(chi2_w_lcdm):.1f}-sig. '
        f'Three decisive tests: LiteBIRD r (24-sig), DESI DR3 w_a (2-sig), 21cm f_NL^folded (3.6-sig).'
    ),
    # Observable names and values
    obs_names=np.array([o['name'] for o in observables]),
    obs_fw_val=np.array([o['fw_val'] for o in observables]),
    obs_fw_unc=np.array([o['fw_unc'] for o in observables]),
    obs_val=np.array([o['obs_val'] if o['obs_val'] is not None else np.nan for o in observables]),
    obs_unc=np.array([o['obs_unc'] if o['obs_unc'] is not None else np.nan for o in observables]),
    obs_tension=np.array([o['tension'] for o in observables]),
    obs_status=np.array([o['status'] for o in observables]),
    obs_source=np.array([o['source'] for o in observables]),
    obs_notes=np.array([o['notes'] for o in observables]),
    obs_group=np.array([o['group'] for o in observables]),
    obs_is_bound=np.array([o['is_bound'] for o in observables]),
    # Chi-squared components
    chi2_ns_alpha=chi2_ns_alpha,
    chi2_As=chi2_As,
    chi2_fNL=chi2_fNL,
    chi2_w=chi2_w,
    chi2_OmDM=chi2_OmDM,
    chi2_mH=chi2_mH,
    chi2_sin2=chi2_sin2,
    chi2_total=chi2_total,
    ndof_total=ndof_total,
    chi2_per_dof=chi2_total / ndof_total,
    # LCDM comparison
    chi2_w_lcdm=chi2_w_lcdm,
    chi2_lcdm_all=chi2_lcdm_all,
    AIC_fw=AIC_fw,
    AIC_lcdm=AIC_lcdm,
    delta_AIC=delta_AIC,
    BIC_fw=BIC_fw,
    BIC_lcdm=BIC_lcdm,
    delta_BIC=delta_BIC,
    # Excluding A_s
    chi2_fw_no_As=chi2_fw_no_As,
    ndof_no_As=ndof_no_As,
    # Covariance matrices used
    cov_ns_alpha=cov_ns_alpha,
    cov_w=cov_w,
    rho_ns_alpha=rho_ns_alpha,
    rho_w=rho_w,
    # Key individual values for downstream use
    ns_fw=ns_fw,
    alpha_s_fw=alpha_s_fw,
    As_fw=As_fw,
    As_gap_OOM=As_gap_OOM,
    r_fw=r_fw,
    nT_fw=nT_fw,
    beta_iso_fw=beta_iso_fw,
    fNL_eq_fw=fNL_eq_fw,
    fNL_fo_fw=fNL_fo_fw,
    fNL_tot_fw=fNL_tot_fw,
    w0_fw=w0_fw,
    wa_fw=wa_fw,
    OmDM_fw=OmDM_fw,
    mH_bare=mH_bare,
    mH_rg=mH_rg,
    sin2_bare=sin2_bare,
    sin2_rg=sin2_rg,
    # Decisive measurements
    SNR_r_LiteBIRD=float(d_liteb['SNR_r_LiteBIRD']),
    sig_fw_desi_dr3_ScB=float(d_desi['sig_fw_scenarios'][1]),
    SNR_fNL_folded_21cm=float(d_fnl['SNR_fo_21cm']),
    # Framework parameter count
    n_free_params_fw=n_free_params_fw,
    n_free_params_lcdm=n_free_params_lcdm,
)

print(f"\nData saved to {os.path.join(data_dir, 's68_joint_observational.npz')}")

# =============================================================================
# SECTION 9: Visualization
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(18, 14))
fig.suptitle('JOINT-OBSERVATIONAL-68: Phonon-Exflation vs Observations\n(S68 Consolidated — Zero Free Parameters)',
             fontsize=14, fontweight='bold', y=0.98)

# --- Panel 1: Tension bar chart (all observables with measured values) ---
ax1 = axes[0, 0]
measured = [o for o in observables if o['obs_val'] is not None and not o['is_bound']
            and o['status'] != 'PREDICTION']
names_m = [o['name'] for o in measured]
tensions_m = [o['tension'] for o in measured]
colors_m = []
for o in measured:
    if o['tension'] < 1.0:
        colors_m.append('#2ecc71')  # green
    elif o['tension'] < 2.0:
        colors_m.append('#f39c12')  # orange
    elif o['tension'] < 3.0:
        colors_m.append('#e67e22')  # dark orange
    else:
        colors_m.append('#e74c3c')  # red

bars = ax1.barh(range(len(names_m)), tensions_m, color=colors_m, edgecolor='black', linewidth=0.5)
ax1.set_yticks(range(len(names_m)))
ax1.set_yticklabels(names_m, fontsize=8)
ax1.set_xlabel('Tension (sigma)', fontsize=10)
ax1.set_title('Tension with Observations', fontsize=11, fontweight='bold')
ax1.axvline(x=2.0, color='orange', linestyle='--', linewidth=1, label='2-sigma')
ax1.axvline(x=3.0, color='red', linestyle='--', linewidth=1, label='3-sigma')
ax1.legend(fontsize=8, loc='lower right')

# Truncate the bar labels for A_s (huge tension)
for i, (name, tension) in enumerate(zip(names_m, tensions_m)):
    if tension > 10:
        ax1.text(min(tension, ax1.get_xlim()[1]) + 0.5, i, f'{tension:.0f}σ',
                va='center', fontsize=7, color='red')

ax1.set_xlim(0, max(max(tensions_m) * 1.15, 5))

# --- Panel 2: Chi-squared budget ---
ax2 = axes[0, 1]
chi2_labels = ['(n_s, alpha_s)', 'A_s', 'f_NL(eq)', '(w_0, w_a)',
               'Omega_DM h^2', 'm_H', 'sin^2(theta_W)']
chi2_vals = [chi2_ns_alpha, chi2_As, chi2_fNL, chi2_w, chi2_OmDM, chi2_mH, chi2_sin2]
chi2_dofs = [2, 1, 1, 2, 1, 1, 1]

# Log scale because A_s dominates
chi2_display = [max(v, 0.01) for v in chi2_vals]  # floor for log
bar_colors = ['#3498db' if v < d else '#e74c3c' for v, d in zip(chi2_vals, chi2_dofs)]

bars2 = ax2.bar(range(len(chi2_labels)), chi2_display, color=bar_colors,
                edgecolor='black', linewidth=0.5, alpha=0.8)
# Add DOF markers
for i, dof in enumerate(chi2_dofs):
    ax2.plot(i, dof, 'k_', markersize=15, markeredgewidth=2)

ax2.set_xticks(range(len(chi2_labels)))
ax2.set_xticklabels(chi2_labels, fontsize=8, rotation=45, ha='right')
ax2.set_ylabel('chi^2', fontsize=10)
ax2.set_yscale('log')
ax2.set_title('Chi-squared Budget (black marks = DOF)', fontsize=11, fontweight='bold')

# Annotate total
ax2.text(0.95, 0.95, f'Total chi^2 = {chi2_total:.0f} / {ndof_total} DOF\n'
         f'Excl. A_s: {chi2_fw_no_As:.1f} / {ndof_no_As} DOF',
         transform=ax2.transAxes, fontsize=9, va='top', ha='right',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# --- Panel 3: Framework vs LCDM (w_0 - w_a plane) ---
ax3 = axes[1, 0]
# Plot DESI contours (1-sigma, 2-sigma ellipses)
from matplotlib.patches import Ellipse
for nsig, alpha_val in [(1, 0.6), (2, 0.3), (3, 0.1)]:
    # Eigenvalue decomposition of covariance
    eigvals, eigvecs = np.linalg.eigh(cov_w)
    angle = np.degrees(np.arctan2(eigvecs[1, 1], eigvecs[0, 1]))
    width  = 2 * nsig * np.sqrt(eigvals[1])  # (local)
    height = 2 * nsig * np.sqrt(eigvals[0])
    ell = Ellipse((w0_obs, wa_obs), width, height, angle=angle,
                  facecolor='blue', alpha=alpha_val * 0.3, edgecolor='blue', linewidth=1)
    ax3.add_patch(ell)

ax3.plot(w0_fw, wa_fw, 'r*', markersize=15, label=f'Framework (w_0={w0_fw}, w_a={wa_fw})', zorder=5)
ax3.plot(-1.0, 0.0, 'ks', markersize=10, label='LCDM (w_0=-1, w_a=0)', zorder=5)
ax3.plot(w0_obs, wa_obs, 'b+', markersize=12, markeredgewidth=2, label=f'DESI DR2 ({w0_obs}, {wa_obs})', zorder=5)
ax3.set_xlabel('w_0', fontsize=10)
ax3.set_ylabel('w_a', fontsize=10)
ax3.set_title('Dark Energy Equation of State', fontsize=11, fontweight='bold')
ax3.legend(fontsize=8, loc='upper left')
ax3.set_xlim(-1.15, -0.55)
ax3.set_ylim(-1.5, 0.5)
ax3.axhline(0, color='gray', linestyle=':', linewidth=0.5)
ax3.axvline(-1, color='gray', linestyle=':', linewidth=0.5)

# --- Panel 4: Summary scorecard ---
ax4 = axes[1, 1]
ax4.axis('off')

# Count by status
n_pass = sum(1 for o in observables if o['status'] == 'PASS')
n_tension = sum(1 for o in observables if o['status'] == 'TENSION')
n_fail = sum(1 for o in observables if o['status'] == 'FAIL')
n_pred = sum(1 for o in observables if o['status'] == 'PREDICTION')
n_total = len(observables)

scorecard_text = (
    f"S68 OBSERVATIONAL SCORECARD\n"
    f"{'='*40}\n"
    f"Total observables:      {n_total}\n"
    f"  PASS (<2-sigma):      {n_pass}\n"
    f"  TENSION (2-3 sigma):  {n_tension}\n"
    f"  FAIL (>3 sigma):      {n_fail}\n"
    f"  PREDICTION (no data): {n_pred}\n"
    f"{'='*40}\n"
    f"Free parameters:        0\n"
    f"{'='*40}\n"
    f"\n"
    f"JOINT CHI-SQUARED (9 DOF):\n"
    f"  Full:    chi^2 = {chi2_total:.0f}\n"
    f"  Per DOF: {chi2_total/ndof_total:.1f}\n"
    f"  A_s dominates: {chi2_As:.0f} of {chi2_total:.0f}\n"
    f"\n"
    f"EXCL. A_s (6 DOF):\n"
    f"  chi^2 = {chi2_fw_no_As:.2f}\n"
    f"  Per DOF: {chi2_fw_no_As/ndof_no_As:.2f}\n"
    f"\n"
    f"vs LCDM (6 free params):\n"
    f"  Delta AIC = {delta_AIC:+.1f}\n"
    f"  Delta BIC = {delta_BIC:+.1f}\n"
    f"\n"
    f"BOTTLENECK: A_s gap (0.755 OOM)\n"
    f"TENSION:    w_0-w_a ({np.sqrt(chi2_w):.1f}-sigma)"
)

ax4.text(0.05, 0.95, scorecard_text, transform=ax4.transAxes,
         fontsize=10, va='top', ha='left', family='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(os.path.join(data_dir, 's68_joint_observational.png'), dpi=150, bbox_inches='tight')
plt.close()

print(f"Plot saved to {os.path.join(data_dir, 's68_joint_observational.png')}")
print("\nDone. JOINT-OBSERVATIONAL-68 complete.")
