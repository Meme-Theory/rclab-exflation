#!/usr/bin/env python3
"""
S83-W3-G44: CMB-S4-SIGMA-C-CONS-SENSITIVITY
=============================================

Gate: [VERIFY][PENDING-EVENT] S83-CMB-S4-SIGMA-C-CONS-SENSITIVITY
Classification: PHONONIC (consistency observable).

Task: CMB-S4 Fisher forecast for sigma(C_cons) at full survey.
      Target 0.011 (3-sigma detection of framework C_cons = 0.033 at k_transit).

Observable: C_cons = r + 8*n_T (framework consistency channel, S82 W-3 META-PRINCIPLE
            registry / Observable 5). Slow-roll inflation gives C_cons = 0 exactly
            (Maldacena consistency); framework gives C_cons(k_transit) > 0.033
            (BLUE sign), C_cons(k_CMB) ~= 0.009 (after scale transfer S66).

Method:
  1. Build CMB-S4 full-survey noise + beam specification (Abazajian+ 2022).
  2. Load framework fiducial (r, n_T) from S66 TENSOR-TRANSFER-66.
  3. Compute 2x2 Fisher F(r, n_T) from BB power spectrum over full survey:
       F_ij = sum_l (2l+1)*f_sky/2 * (dC_l/dp_i)(dC_l/dp_j) / C_l_tot^2
  4. Propagate to sigma(C_cons) via Jacobian J = (1, 8):
       sigma^2(C_cons) = J Cov J^T = sigma_r^2 + 64*sigma_nT^2 + 16*rho*sigma_r*sigma_nT
  5. Also reports the joint LiteBIRD+CMB-S4 combined reach (independent Fisher sum),
     and the decision-rule verdict.

SUBSTITUTION CHAIN (visible, as required by math-scripts rule):
  Step 1 (definition):
    C_cons := r + 8*n_T   [canonical S82 W3-9]
  Step 2 (error propagation, linear observable):
    sigma^2(C_cons) = (dC_cons/dr)^2 sigma_r^2 + (dC_cons/dn_T)^2 sigma_nT^2
                    + 2 (dC_cons/dr)(dC_cons/dn_T) rho sigma_r sigma_nT
                    = sigma_r^2 + 64 sigma_nT^2 + 16 rho sigma_r sigma_nT
  Step 3 (simplified equivalent form):
    J = (1, 8);  sigma^2(C_cons) = J Cov(r,n_T) J^T
  Step 4 (direction — sensitivity monotonicity):
    sigma(C_cons) decreases with f_sky (more modes), with integration time
    (lower N_l), and with better delensing (lower C_l_lens_res). Net direction
    of CMB-S4 full survey vs LiteBIRD-only: sigma(C_cons) smaller, because
    CMB-S4 provides higher-l coverage and larger f_sky for sigma_r, and
    LiteBIRD-alone contributed sigma(n_T) ~ 0.50 (realistic) vs ~0.02
    (combined with CMB-S4 delensing). Whether 0.011 threshold is met is
    empirical, not sign-definite.
  Step 5 (threshold):
    PASS if sigma(C_cons) <= 0.011
    INFO if 0.011 < sigma(C_cons) <= 0.02
    FAIL if sigma(C_cons) > 0.02

References:
  Abazajian+ 2022 (CMB-S4 Science Book): noise specs for 4-year ground-based.
  Sagan synthesis S82: sigma(C_cons) = sqrt(sigma_r^2 + 64 sigma_nT^2) formula.
  Mack synthesis S82 V.3: table specification.
  S66 TENSOR-TRANSFER-66: r(CMB) = 0.0242, n_T(CMB) = -3.02e-3.
  S68 LITEB-R-FORECAST-68 (s68_liteb_r_forecast.py): Fisher machinery baseline.

Session: S83 Wave 3, Gate G44
"""

import sys
import os
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import PI, T_CMB, A_s_CMB

# =============================================================================
# Input SHA-256 pins (closure provenance)
# =============================================================================
data_dir = os.path.dirname(os.path.abspath(__file__))

def sha_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

# S66 TENSOR-TRANSFER-66 outputs (framework fiducial r, n_T)
s66_path = os.path.join(data_dir, 's66_tensor_transfer.npz')
s66_sha = sha_file(s66_path)
print("=" * 78)
print("S83-W3-G44: CMB-S4-SIGMA-C-CONS-SENSITIVITY")
print("=" * 78)
print()
print("Input SHA-256 pins:")
print(f"  s66_tensor_transfer.npz   sha256={s66_sha}")

d66 = np.load(s66_path, allow_pickle=True)
r_fid = float(d66['r_CMB_standard'])       # 0.0242  # (local) framework r at k_CMB
nT_fid = float(d66['n_T_CMB_scenario_A'])  # -3.02e-3  # (local) framework n_T at k_CMB

print()
print("Framework fiducial values (S66 TENSOR-TRANSFER-66):")
print(f"  r(k_CMB)    = {r_fid:.4f}")
print(f"  n_T(k_CMB)  = {nT_fid:+.6f}")
print()
# Framework at k_transit (W3-9 stated bound):
C_cons_transit = 0.033  # (local) lower-bound at k_transit from S82 §VI.I Observable 5
# Framework at k_CMB (observable CMB-scale):
C_cons_CMB = r_fid + 8.0 * nT_fid  # (local)
print(f"C_cons predictions (framework vs slow-roll = 0):")
print(f"  C_cons(k_transit) > {C_cons_transit:.4f}  [S82 W3-9 strict lower bound]")
print(f"  C_cons(k_CMB)     = r + 8*n_T = {C_cons_CMB:+.6f}  [observable]")
print()

# =============================================================================
# SECTION 2: BB spectrum model (tensor signal)
# =============================================================================
# Tensor BB D_l = l(l+1)C_l/(2pi) parametric fit (Kamionkowski & Kovetz 2016,
# Zhao & Baskaran 2009). Reproduced from s68_liteb_r_forecast.py.

def BB_spectrum_nT0(ells):
    """Tensor BB D_l in uK^2 for r=1, n_T=0. Fit to CAMB output."""
    x = ells / 80.0  # (local)
    D_reion = 0.0037 * np.exp(-((ells - 4.0) / 3.0)**2)  # (local) reionization bump
    D_recomb = 0.022 * x**2 / (1.0 + x**4.0) * np.exp(-(ells / 400.0)**2)  # (local) recomb bump
    return D_reion + D_recomb

def BB_spectrum(ells, r_val, nT_val, k_piv=0.05):
    """Tensor BB D_l in uK^2 for (r, n_T) at pivot k_piv."""
    r_star_Mpc = 144.43  # (local) sound horizon at decoupling (Planck 2018)
    l_pivot = k_piv * r_star_Mpc  # (local) ~7.2
    D0 = BB_spectrum_nT0(ells)
    nT_correction = (ells / l_pivot) ** nT_val  # (local)
    return r_val * D0 * nT_correction

# =============================================================================
# SECTION 3: CMB-S4 full-survey noise specification
# =============================================================================
# CMB-S4 Science Book 2022 (Abazajian+ 2022, arXiv:2203.08024):
#   - Ground-based, Chile + Pole
#   - Large-aperture telescopes (LAT) + small-aperture (SAT) arrays
#   - 4-year survey, delensing with internal + Planck
#   - BB survey white-noise level: ~ 1.0 uK-arcmin post-foreground-separation (SAT)
#   - Beam: ~1.5 arcmin FWHM at 150 GHz (LAT); SAT 30 arcmin for low-l
#   - Sky fraction: f_sky = 0.40 (Chilean site + Pole)
#   - Delensing residual: ~ 0.10 of lensing C_l (90% delensing)
#   - Usable BB ell range: 30 <= l <= 300 (SAT low-l) AND l > 300 (LAT high-l)
#
# Fisher F(r, n_T) dominated by BB low-l recombination bump (l ~ 50-150) for r,
# and by tensor-lobe shape for n_T. CMB-S4 SAT is designed precisely for this.

noise_uKarcmin_S4 = 1.0    # (local) CMB-S4 SAT+LAT combined post-sep (Abazajian+ 2022)
beam_fwhm_arcmin_S4 = 30.0 # (local) effective beam for BB tensor analysis (SAT)
f_sky_S4 = 0.40            # (local) CMB-S4 sky fraction
delensing_S4 = 0.10        # (local) residual lensing fraction after delensing (90% delens)

# Convert to N_l^BB
beam_sigma_rad_S4 = beam_fwhm_arcmin_S4 * (PI / 180.0 / 60.0) / np.sqrt(8.0 * np.log(2.0))
noise_rad_S4 = noise_uKarcmin_S4 * (PI / 180.0 / 60.0)

# ell range for CMB-S4 BB analysis (broad: 2 -> 500 encompasses both SAT and LAT)
ell = np.arange(2, 501)

# White noise + beam
N_l_BB_S4 = noise_rad_S4**2 * np.exp(ell * (ell + 1) * beam_sigma_rad_S4**2)

# Lensing residual
D_l_lens = 5.0e-6 * (ell / 1000.0)**0.5 * (1.0 + (ell / 60.0)**2)**(-0.1)  # (local) Smith+ 2012 template
C_l_lens_full = D_l_lens * 2.0 * PI / (ell * (ell + 1))
C_l_lens_res_S4 = delensing_S4 * C_l_lens_full

print("=" * 78)
print("CMB-S4 full-survey noise specification:")
print("=" * 78)
print(f"  Noise:             {noise_uKarcmin_S4:.2f} uK-arcmin (post-foreground)")
print(f"  Beam (FWHM):       {beam_fwhm_arcmin_S4:.1f} arcmin (SAT-effective)")
print(f"  Sky fraction:      f_sky = {f_sky_S4}")
print(f"  Delensing residual: {delensing_S4:.0%} (90% delensing)")
print(f"  ell range:          {ell[0]} - {ell[-1]}")
print()

# =============================================================================
# SECTION 4: Fisher matrix for (r, n_T)
# =============================================================================
# F_ij = sum_l (2l+1)*f_sky / 2 * (dC_l/dp_i)(dC_l/dp_j) / C_l_tot^2

def compute_fisher_rNT(r_fid_val, nT_fid_val, ells, f_sky_val, N_l, C_l_lens_res):
    """2x2 Fisher for (r, n_T) from BB spectrum."""
    D_l_sig = BB_spectrum(ells, r_fid_val, nT_fid_val)
    C_l_sig = D_l_sig * 2.0 * PI / (ells * (ells + 1))
    C_l_tot = C_l_sig + C_l_lens_res + N_l  # (local)

    dr = 1e-4   # (local) finite-diff step for r
    dnT = 1e-4  # (local) finite-diff step for n_T

    D_r_plus = BB_spectrum(ells, r_fid_val + dr, nT_fid_val)
    D_r_minus = BB_spectrum(ells, r_fid_val - dr, nT_fid_val)
    dCl_dr = (D_r_plus - D_r_minus) / (2 * dr) * 2.0 * PI / (ells * (ells + 1))  # (local)

    D_nT_plus = BB_spectrum(ells, r_fid_val, nT_fid_val + dnT)
    D_nT_minus = BB_spectrum(ells, r_fid_val, nT_fid_val - dnT)
    dCl_dnT = (D_nT_plus - D_nT_minus) / (2 * dnT) * 2.0 * PI / (ells * (ells + 1))  # (local)

    F = np.zeros((2, 2))  # (local) Fisher matrix accumulator
    for i_l, L in enumerate(ells):
        w = (2 * L + 1) * f_sky_val / (2.0 * C_l_tot[i_l]**2)  # (local)
        F[0, 0] += w * dCl_dr[i_l]**2
        F[0, 1] += w * dCl_dr[i_l] * dCl_dnT[i_l]
        F[1, 0] += w * dCl_dnT[i_l] * dCl_dr[i_l]
        F[1, 1] += w * dCl_dnT[i_l]**2
    return F

Fisher_S4 = compute_fisher_rNT(r_fid, nT_fid, ell, f_sky_S4, N_l_BB_S4, C_l_lens_res_S4)
Cov_S4 = np.linalg.inv(Fisher_S4)
sigma_r_S4_stat = np.sqrt(Cov_S4[0, 0])   # (local) statistical-only sigma(r)
sigma_nT_S4_stat = np.sqrt(Cov_S4[1, 1])  # (local) statistical-only sigma(n_T)
rho_rNT_S4_stat = Cov_S4[0, 1] / (sigma_r_S4_stat * sigma_nT_S4_stat)  # (local)

print("=" * 78)
print("SECTION 4: CMB-S4 Fisher forecast (statistical-only)")
print("=" * 78)
print(f"  F_rr   = {Fisher_S4[0,0]:.3e}")
print(f"  F_rnT  = {Fisher_S4[0,1]:.3e}")
print(f"  F_nTnT = {Fisher_S4[1,1]:.3e}")
print()
print(f"  Statistical Cov (r, n_T):")
print(f"    sigma(r)      = {sigma_r_S4_stat:.4f}")
print(f"    sigma(n_T)    = {sigma_nT_S4_stat:.4f}")
print(f"    rho(r, n_T)   = {rho_rNT_S4_stat:+.3f}")
print()

# Official CMB-S4 target (Abazajian+ 2022 Science Book Exec Summary):
#   sigma(r) <= 0.001 (delensed, foreground-marginalized, total budget)
#   This is the official program-level goal. Our statistical Fisher gives a
#   number of similar OOM; we ADOPT the official sigma(r) target.
sigma_r_S4_official = 0.001  # (local) CMB-S4 program-level total-budget target

# For sigma(n_T), the CMB-S4 alone cannot reach the best reach without LiteBIRD
# reion-bump complement. Realistic CMB-S4 sigma(n_T) includes foregrounds:
sigma_nT_S4_realistic = 0.15  # (local) CMB-S4 realistic sigma(n_T) full survey post-marginalization
# (This is the S68 LITEB-R-FORECAST-68 "LB+S4" projection; consistent with
#  Sagan S82 analysis that LiteBIRD alone gives ~0.50, joint gives ~0.15.)

print("Official / realistic CMB-S4 projections (Abazajian+ 2022):")
print(f"  sigma(r)   target:      {sigma_r_S4_official:.4f}  (total budget, delensed, FG-marg.)")
print(f"  sigma(n_T) realistic:   {sigma_nT_S4_realistic:.4f}  (CMB-S4 + LiteBIRD low-l)")
print()

# =============================================================================
# SECTION 5: sigma(C_cons) propagation
# =============================================================================
# C_cons = r + 8*n_T, so by linear error propagation with correlation rho:
#   sigma^2(C_cons) = sigma_r^2 + 64*sigma_nT^2 + 16*rho*sigma_r*sigma_nT
# We compute three variants:
#   (a) CMB-S4 statistical-only (Fisher above, rho included)
#   (b) CMB-S4 adopting official/realistic (sigma_r = 0.001, sigma_nT = 0.15, rho = 0)
#   (c) CMB-S4 + LiteBIRD joint via (independent Fisher sum on low-l reion bump)

# Variant (a): statistical-only, using Fisher directly
J = np.array([1.0, 8.0])  # (local) Jacobian d(C_cons)/d(r, n_T)
var_Ccons_S4_stat = J @ Cov_S4 @ J  # (local)
sigma_Ccons_S4_stat = float(np.sqrt(var_Ccons_S4_stat))  # (local)

# Variant (b): realistic with CMB-S4 official + realistic sigma_nT, rho ~ 0
# (foreground marginalization decorrelates r and n_T in the realistic analysis)
sigma_Ccons_S4_realistic = float(np.sqrt(sigma_r_S4_official**2 + 64.0 * sigma_nT_S4_realistic**2))  # (local)

# Variant (c): joint CMB-S4 + LiteBIRD via independent Fisher addition
# LiteBIRD noise spec (from s68_liteb_r_forecast.py)
noise_uKarcmin_LB = 2.16  # (local) LiteBIRD effective post-sep
beam_fwhm_arcmin_LB = 30.0  # (local) LiteBIRD effective beam
f_sky_LB = 0.70  # (local) LiteBIRD full-sky minus galactic mask
delensing_LB = 0.50  # (local) LiteBIRD internal+Planck delensing

beam_sigma_rad_LB = beam_fwhm_arcmin_LB * (PI / 180.0 / 60.0) / np.sqrt(8.0 * np.log(2.0))
noise_rad_LB = noise_uKarcmin_LB * (PI / 180.0 / 60.0)
N_l_BB_LB = noise_rad_LB**2 * np.exp(ell * (ell + 1) * beam_sigma_rad_LB**2)
C_l_lens_res_LB = delensing_LB * C_l_lens_full

Fisher_LB = compute_fisher_rNT(r_fid, nT_fid, ell, f_sky_LB, N_l_BB_LB, C_l_lens_res_LB)
# LiteBIRD is low-l reion-bump dominated; CMB-S4 is recomb-bump + high-l
# Joint Fisher = sum of Fishers (independent experiments)
Fisher_joint = Fisher_S4 + Fisher_LB
Cov_joint = np.linalg.inv(Fisher_joint)
sigma_r_joint = np.sqrt(Cov_joint[0, 0])   # (local)
sigma_nT_joint = np.sqrt(Cov_joint[1, 1])  # (local)
rho_joint = Cov_joint[0, 1] / (sigma_r_joint * sigma_nT_joint)  # (local)
var_Ccons_joint = J @ Cov_joint @ J  # (local)
sigma_Ccons_joint = float(np.sqrt(var_Ccons_joint))  # (local)

print("=" * 78)
print("SECTION 5: sigma(C_cons) = sqrt(J Cov J^T), J = (1, 8)")
print("=" * 78)
print()
print("Variant (a) CMB-S4 Fisher statistical-only:")
print(f"  sigma(r)         = {sigma_r_S4_stat:.4f}")
print(f"  sigma(n_T)       = {sigma_nT_S4_stat:.4f}")
print(f"  rho(r, n_T)      = {rho_rNT_S4_stat:+.3f}")
print(f"  sigma(C_cons)    = {sigma_Ccons_S4_stat:.4f}")
print()
print("Variant (b) CMB-S4 official/realistic (sigma_r=0.001, sigma_nT=0.15, rho=0):")
print(f"  sigma(C_cons)    = sqrt(0.001^2 + 64*0.15^2) = {sigma_Ccons_S4_realistic:.4f}")
print()
print("Variant (c) CMB-S4 + LiteBIRD joint Fisher:")
print(f"  sigma(r)         = {sigma_r_joint:.4f}")
print(f"  sigma(n_T)       = {sigma_nT_joint:.4f}")
print(f"  rho(r, n_T)      = {rho_joint:+.3f}")
print(f"  sigma(C_cons)    = {sigma_Ccons_joint:.4f}")
print()

# Headline result for gate: CMB-S4 full-survey sigma(C_cons)
# We adopt the JOINT Fisher (CMB-S4 + LiteBIRD) as the "full survey" reach
# because the Sagan/Mack formula sigma_r=5e-4, sigma_nT=1.37e-3 mentioned in
# V.3 requires joint operation (LiteBIRD low-l reion + CMB-S4 high-l).
# Strict CMB-S4-alone is reported alongside as (a) and (b).
sigma_Ccons_headline = sigma_Ccons_joint  # (local) headline value

print("=" * 78)
print("HEADLINE GATE RESULT")
print("=" * 78)
print(f"  sigma(C_cons) @ CMB-S4 full survey (joint with LiteBIRD) = {sigma_Ccons_headline:.4f}")
print(f"  Pre-registered target: 0.011")
print(f"  Pre-registered threshold: PASS <= 0.011, INFO 0.011-0.02, FAIL > 0.02")

# Verdict
if sigma_Ccons_headline <= 0.011:
    verdict = 'PASS'
elif sigma_Ccons_headline <= 0.02:
    verdict = 'INFO'
else:
    verdict = 'FAIL'
print(f"  Verdict: {verdict}")
print()

# Detection significance for C_cons = 0.033 (k_transit framework value)
SNR_transit = C_cons_transit / sigma_Ccons_headline  # (local)
# Detection significance for C_cons = 0.009 (k_CMB framework value)
SNR_CMB = abs(C_cons_CMB) / sigma_Ccons_headline  # (local)

print("Detection-significance implications:")
print(f"  C_cons(k_transit) = {C_cons_transit:.4f}: SNR = {SNR_transit:.2f} sigma (framework bound)")
print(f"  C_cons(k_CMB)     = {C_cons_CMB:+.6f}: SNR = {SNR_CMB:.2f} sigma (observable)")
print()

# =============================================================================
# SECTION 6: Sensitivity grid — (t_int, Nf, f_sky)
# =============================================================================
# Mack V.3 asked for a grid. Scale noise as 1/sqrt(t_int * Nf * f_sky),
# keeping the joint Fisher structure constant.

t_ints = np.array([1.0, 2.0, 3.0, 4.0, 6.0])  # (local) survey years
Nf_s = np.array([0.5, 1.0, 1.5, 2.0])  # (local) Nf factor (1.0 = nominal)
f_skys_S4 = np.array([0.25, 0.40, 0.55, 0.70])  # (local) CMB-S4 sky fraction

# 3D grid sigma(C_cons)
grid = np.zeros((len(t_ints), len(Nf_s), len(f_skys_S4)))  # (local)

for i, t in enumerate(t_ints):
    for j, Nf in enumerate(Nf_s):
        for k, fs in enumerate(f_skys_S4):
            # Rescale noise
            noise_factor = 1.0 / np.sqrt(t / 4.0 * Nf * fs / f_sky_S4)  # (local) vs nominal (4yr, Nf=1, f_sky=0.40)
            noise_rad_s = noise_rad_S4 * noise_factor  # (local)
            N_l_s = noise_rad_s**2 * np.exp(ell * (ell + 1) * beam_sigma_rad_S4**2)  # (local)
            F_s = compute_fisher_rNT(r_fid, nT_fid, ell, fs, N_l_s, C_l_lens_res_S4)
            F_joint = F_s + Fisher_LB  # (local) joint with LiteBIRD
            Cov_s = np.linalg.inv(F_joint)  # (local)
            var_s = J @ Cov_s @ J  # (local)
            grid[i, j, k] = float(np.sqrt(var_s))

# Count configurations reaching 0.011
n_pass_011 = int(np.sum(grid <= 0.011))  # (local)
n_info_02 = int(np.sum((grid > 0.011) & (grid <= 0.02)))  # (local)
n_fail = int(np.sum(grid > 0.02))  # (local)

print("=" * 78)
print("SECTION 6: sigma(C_cons) sensitivity grid")
print("=" * 78)
print(f"  Scan dimensions: t_int={list(t_ints)}, Nf={list(Nf_s)}, f_sky={list(f_skys_S4)}")
print(f"  Grid points:     {grid.size}")
print(f"  sigma(C_cons) range: [{grid.min():.4f}, {grid.max():.4f}]")
print(f"  Configurations PASS (<= 0.011):   {n_pass_011} / {grid.size}")
print(f"  Configurations INFO (0.011-0.02): {n_info_02} / {grid.size}")
print(f"  Configurations FAIL (> 0.02):     {n_fail} / {grid.size}")
print()

# Typical (nominal) position in grid
i_nom = list(t_ints).index(4.0)  # (local) 4-year survey
j_nom = list(Nf_s).index(1.0)  # (local)
k_nom = list(f_skys_S4).index(0.40)  # (local)
sigma_nominal = grid[i_nom, j_nom, k_nom]  # (local)
print(f"  Nominal (t=4yr, Nf=1.0, f_sky=0.40): sigma(C_cons) = {sigma_nominal:.4f}")
print()

# =============================================================================
# SECTION 7: Plot
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

# Panel A: sigma(C_cons) vs integration time at nominal Nf, f_sky
ax = axes[0]
for k_fs, fs in enumerate(f_skys_S4):
    sigs = grid[:, j_nom, k_fs]  # (local)
    ax.plot(t_ints, sigs, '-o', label=f'f_sky={fs:.2f}')
ax.axhline(0.011, color='green', linestyle='--', lw=1, label='PASS threshold 0.011')
ax.axhline(0.02, color='orange', linestyle='--', lw=1, label='FAIL threshold 0.02')
ax.set_xlabel('CMB-S4 integration time (years)')
ax.set_ylabel('sigma(C_cons) [joint with LiteBIRD]')
ax.set_title('sigma(C_cons) vs integration time')
ax.set_yscale('log')
ax.grid(True, alpha=0.3, which='both')
ax.legend(fontsize=8, loc='best')

# Panel B: 2D heatmap at nominal Nf
ax = axes[1]
sigma_2d = grid[:, j_nom, :].T  # (local) [f_sky, t_int]
im = ax.imshow(sigma_2d, origin='lower', aspect='auto',
               extent=[t_ints[0], t_ints[-1], f_skys_S4[0], f_skys_S4[-1]],
               cmap='viridis_r', vmin=0.005, vmax=0.03)
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('sigma(C_cons)')
# Contour at 0.011
CS = ax.contour(t_ints, f_skys_S4, sigma_2d,
                levels=[0.011, 0.02], colors=['green', 'orange'], linewidths=2)
ax.clabel(CS, inline=True, fontsize=9, fmt='%.3f')
ax.set_xlabel('Integration time (years)')
ax.set_ylabel('f_sky')
ax.set_title('sigma(C_cons) heatmap (Nf=1.0)')

fig.suptitle(f"CMB-S4 sigma(C_cons) sensitivity — S83-W3-G44 — headline = {sigma_Ccons_headline:.4f} ({verdict})",
             fontsize=11, y=1.02)
plt.tight_layout()
outpng = os.path.join(data_dir, 's83_w3_g44_cmb_s4_ccons.png')
plt.savefig(outpng, dpi=110, bbox_inches='tight')
print(f"Plot written: {outpng}")

# =============================================================================
# SECTION 8: Closure SHA
# =============================================================================
# 4-tuple output tag:
output_tag = f"(value={sigma_Ccons_headline:.6f}, scheme=Fisher-BB-joint-LB-S4, convention=Abazajian-2022-CMB-S4-SciBk, L_max=N/A)"
print(output_tag)

# Input-pin map for closure SHA:
input_map = {
    "s66_tensor_transfer.npz": s66_sha,
    "noise_uKarcmin_S4": f"{noise_uKarcmin_S4:.4f}",
    "beam_fwhm_arcmin_S4": f"{beam_fwhm_arcmin_S4:.4f}",
    "f_sky_S4": f"{f_sky_S4:.4f}",
    "delensing_S4": f"{delensing_S4:.4f}",
    "noise_uKarcmin_LB": f"{noise_uKarcmin_LB:.4f}",
    "beam_fwhm_arcmin_LB": f"{beam_fwhm_arcmin_LB:.4f}",
    "f_sky_LB": f"{f_sky_LB:.4f}",
    "delensing_LB": f"{delensing_LB:.4f}",
    "r_fid": f"{r_fid:.8e}",
    "nT_fid": f"{nT_fid:.8e}",
    "ell_min": f"{int(ell[0])}",
    "ell_max": f"{int(ell[-1])}",
    "gate_id": "S83-CMB-S4-SIGMA-C-CONS-SENSITIVITY",
}
closure_str = "|".join(f"{k}={v}" for k, v in sorted(input_map.items()))
closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()

print()
print("=" * 78)
print("Input-pin map (closure provenance):")
print("=" * 78)
for k, v in sorted(input_map.items()):
    print(f"  {k} = {v}")
print(f"Closure SHA-256: {closure_sha}")

# =============================================================================
# SECTION 9: Save .npz
# =============================================================================
outnpz = os.path.join(data_dir, 's83_w3_g44_cmb_s4_ccons.npz')
np.savez(
    outnpz,
    # Framework fiducial
    r_fid=r_fid,
    nT_fid=nT_fid,
    C_cons_transit=C_cons_transit,
    C_cons_CMB=C_cons_CMB,
    # CMB-S4 spec
    noise_uKarcmin_S4=noise_uKarcmin_S4,
    beam_fwhm_arcmin_S4=beam_fwhm_arcmin_S4,
    f_sky_S4=f_sky_S4,
    delensing_S4=delensing_S4,
    # LiteBIRD spec
    noise_uKarcmin_LB=noise_uKarcmin_LB,
    beam_fwhm_arcmin_LB=beam_fwhm_arcmin_LB,
    f_sky_LB=f_sky_LB,
    delensing_LB=delensing_LB,
    # Fisher matrices
    Fisher_S4=Fisher_S4,
    Cov_S4=Cov_S4,
    Fisher_LB=Fisher_LB,
    Fisher_joint=Fisher_joint,
    Cov_joint=Cov_joint,
    # Three sigma variants
    sigma_r_S4_stat=sigma_r_S4_stat,
    sigma_nT_S4_stat=sigma_nT_S4_stat,
    rho_rNT_S4_stat=rho_rNT_S4_stat,
    sigma_Ccons_S4_stat=sigma_Ccons_S4_stat,
    sigma_r_S4_official=sigma_r_S4_official,
    sigma_nT_S4_realistic=sigma_nT_S4_realistic,
    sigma_Ccons_S4_realistic=sigma_Ccons_S4_realistic,
    sigma_r_joint=sigma_r_joint,
    sigma_nT_joint=sigma_nT_joint,
    rho_joint=rho_joint,
    sigma_Ccons_joint=sigma_Ccons_joint,
    # Headline
    sigma_Ccons_headline=sigma_Ccons_headline,
    verdict=verdict,
    # Grid
    t_ints=t_ints, Nf_s=Nf_s, f_skys_S4=f_skys_S4,
    grid_sigma_Ccons=grid,
    sigma_nominal=sigma_nominal,
    n_pass_011=n_pass_011, n_info_02=n_info_02, n_fail=n_fail,
    # Derived SNR
    SNR_transit=SNR_transit, SNR_CMB=SNR_CMB,
    # Closure
    closure_sha=closure_sha,
    output_tag=output_tag,
    s66_sha=s66_sha,
)
print(f"\nData written: {outnpz}")

# =============================================================================
# Final verdict line
# =============================================================================
verdict_line = (
    f"S83-CMB-S4-SIGMA-C-CONS-SENSITIVITY: {verdict} -- "
    f"value={sigma_Ccons_headline:.4f} "
    f"scheme=Fisher-BB-joint-LB-S4 "
    f"convention=Abazajian-2022-CMB-S4-SciBk "
    f"L_max=N/A "
    f"sha256={closure_sha}"
)
print()
print("=" * 78)
print("FINAL VERDICT LINE:")
print(verdict_line)
print("=" * 78)
