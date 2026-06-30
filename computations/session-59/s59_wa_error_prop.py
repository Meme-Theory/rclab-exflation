#!/usr/bin/env python3
"""
s59_wa_error_prop.py — WA-ERROR-PROP-59: w_a Error Propagation for DESI DR3
============================================================================
Gate: WA-ERROR-PROP-59
  PASS: Framework contour overlaps DESI DR3 projected contour at > 5% area
  FAIL: Overlap < 1% (framework excluded at > 3 sigma by projected DR3)
  INFO: Overlap in [1%, 5%]

Physics: The framework predicts w_a ~ 0 (|w_a| < 0.03) because the GGE state
is integrability-protected and the w(tau) trajectory is nearly flat across
the observable redshift range (z ~ 0 to 1.5). DESI DR2 reports w_a = -0.73
+/- 0.25, a 2.9-sigma deviation from w_a = 0.

This script:
  1. Loads w(tau) trajectory from s58_w_desi.npz (Interp A: w_0 = -0.918, w_a = -0.0006)
  2. Propagates framework parameter uncertainties into the w_0-w_a plane:
     - epsilon: +/- 39% (from s58_epsilon_direct.npz)
     - tau_fold: +/- 5% (canonical uncertainty)
     - N_cells: discrete [24, 32, 48] (tessellation uncertainty)
  3. Generates framework 68% and 95% confidence contours
  4. Overlays DESI DR2 and projected DR3 contours
  5. Computes overlap fraction and exclusion significance

Author: Katie Mack (Cosmic Bridge)
Session: 59, Wave 1, Task W1-3
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.colors import to_rgba
from scipy import stats

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import *

# =============================================================================
# 1. Load upstream data
# =============================================================================
d_w = np.load(os.path.join(SCRIPT_DIR, 's58_w_desi.npz'), allow_pickle=True)
d_eps = np.load(os.path.join(SCRIPT_DIR, 's58_epsilon_direct.npz'), allow_pickle=True)

print("=" * 72)
print("WA-ERROR-PROP-59: w_a Error Propagation for DESI DR3")
print("=" * 72)

# Extract S58 central values (Interpretation A: combined Josephson+GGE)
w0_A_central = float(d_w['w_0_A'])          # -0.918
wa_A_central = float(d_w['w_a_A'])          # -0.000575
w0_A_fit = float(d_w['w0_A_fit'])           # -0.918 (CPL fit)
wa_A_fit = float(d_w['wa_A_fit'])           # -0.000575 (CPL fit)

# Framework uncertainty parameters
epsilon_central = float(d_eps['epsilon_direct'])   # 0.001431
sigma_eps_frac = float(d_eps['sigma_eps_frac'])    # 0.3923 (~39%)

# DESI DR2 values
desi_dr2_w0 = float(d_w['desi_dr2_w0'])     # -0.752
desi_dr2_w0_e = float(d_w['desi_dr2_w0_e']) # 0.057
desi_dr2_wa = float(d_w['desi_dr2_wa'])     # -0.73
desi_dr2_wa_e = float(d_w['desi_dr2_wa_e']) # 0.25

# GGE state parameters
rho_J_cell = float(d_w['rho_J_cell'])       # 10.52
rho_GGE = float(d_w['rho_GGE'])             # 1.709
P_GGE = float(d_w['P_GGE'])                 # -0.688
F_Josephson = float(d_w['F_Josephson'])      # -336.64

print(f"\n=== S58 Central Values (Interpretation A) ===")
print(f"  w_0 = {w0_A_central:.6f}")
print(f"  w_a = {wa_A_central:.6f}")
print(f"  epsilon = {epsilon_central:.6f} +/- {sigma_eps_frac*100:.1f}%")
print(f"  rho_J/cell = {rho_J_cell:.4f} M_KK")
print(f"  rho_GGE = {rho_GGE:.6f} M_KK")
print(f"  P_GGE = {P_GGE:.6f} M_KK")

# =============================================================================
# 2. Parameter uncertainty propagation
# =============================================================================
# Three sources of uncertainty, propagated through the w_0, w_a formulas:
#
# w_0 = (P_J + P_GGE) / (rho_J + rho_GGE)
# where rho_J = |F_J| / N_cells, P_J = -rho_J (CC-like, w_J = -1)
#
# The w_a dependence is through the tau-derivative of w:
# w_a = dw/da|_{a=1} = (dw/dtau) * (dtau/da)|_{a=1}
# Since w(tau) is nearly flat (RMS of A-fit = 2.99e-5), w_a is tiny.
#
# Parameter dependencies:
# 1. epsilon: affects E_GGE and P_GGE through pairing strength
#    w_GGE = P_GGE / rho_GGE. The GGE equation of state depends on epsilon
#    via the integrability-breaking channel. Variation: P_GGE ~ P_0 * (1 + alpha * delta_eps)
#
# 2. tau_fold: shifts which point in the w(tau) trajectory maps to z=0
#    tau_fold = 0.19 +/- 0.0095. This shifts w_0 by (dw/dtau)|_{fold} * delta_tau
#
# 3. N_cells: changes rho_J/cell = |F_J| / N_cells
#    N_cells in {24, 32, 48}: rho_J/cell = {14.03, 10.52, 7.01}

print(f"\n=== Parameter Uncertainty Propagation ===")

# --- 2a. N_cells variation ---
N_cells_values = np.array([24, 32, 48])
w0_Ncells = np.zeros(len(N_cells_values))
wa_Ncells = np.zeros(len(N_cells_values))

for i, N in enumerate(N_cells_values):
    rho_J_N = abs(F_Josephson) / N
    rho_DE = rho_J_N + rho_GGE
    P_DE = -rho_J_N + P_GGE
    w0_Ncells[i] = P_DE / rho_DE
    # w_a remains ~0 because the tau-dependence is in rho_GGE(tau) and P_GGE(tau),
    # not N_cells. N_cells shifts the z=0 anchor point's w_0, not the slope.
    wa_Ncells[i] = wa_A_central  # unchanged by N_cells to leading order

print(f"\n  N_cells variation:")
for i, N in enumerate(N_cells_values):
    print(f"    N={N}: w_0 = {w0_Ncells[i]:.6f}, rho_J/cell = {abs(F_Josephson)/N:.4f}")

# --- 2b. tau_fold variation ---
sigma_tau = 0.05 * tau_fold  # = 0.0095
# From the w_sweep_A array, compute dw/dtau at the fold
tau_vals = d_w['tau_values']
w_sweep_A = d_w['w_sweep_A']

# Find the index closest to tau_fold
fold_idx = np.argmin(np.abs(tau_vals - tau_fold))
# Numerical derivative at the fold
if fold_idx > 0 and fold_idx < len(tau_vals) - 1:
    dtau = tau_vals[fold_idx + 1] - tau_vals[fold_idx - 1]
    dw_dtau_A = (w_sweep_A[fold_idx + 1] - w_sweep_A[fold_idx - 1]) / dtau
else:
    dw_dtau_A = 0.0  # (local)

# w_0 shift from tau_fold uncertainty
delta_w0_tau = abs(dw_dtau_A) * sigma_tau

# w_a: the slope changes slightly with tau_fold shift, but the dominant effect
# is the reanchoring of z=0. From the S58 CPL fit, w_a = -5.75e-4 with RMS = 3e-5.
# The tau variation adds an uncertainty of order dw_a/dtau ~ second derivative * sigma_tau
if fold_idx > 1 and fold_idx < len(tau_vals) - 2:
    d2w_dtau2 = (w_sweep_A[fold_idx + 1] - 2*w_sweep_A[fold_idx] + w_sweep_A[fold_idx - 1]) / \
                ((tau_vals[fold_idx + 1] - tau_vals[fold_idx])**2)
    delta_wa_tau = abs(d2w_dtau2) * sigma_tau
else:
    delta_wa_tau = 0.001  # fallback  # (local)

print(f"\n  tau_fold variation:")
print(f"    tau_fold = {tau_fold} +/- {sigma_tau:.4f}")
print(f"    dw/dtau at fold = {dw_dtau_A:.6e}")
print(f"    delta_w0 from tau = {delta_w0_tau:.6e}")
print(f"    delta_wa from tau = {delta_wa_tau:.6e}")

# --- 2c. epsilon variation ---
# epsilon affects the integrability-breaking coupling and hence the GGE partition.
# From the Volovik partition: rho_GGE = E_GGE and P_GGE = w_GGE * rho_GGE
# The BCS pairing gap scales as Delta ~ exp(-1/(g*N(E_F))), where g ~ epsilon.
# For small epsilon variations around the central value:
#   delta(rho_GGE)/rho_GGE ~ delta(epsilon)/epsilon (linear to leading order)
# But the ratio P_GGE/rho_GGE (= w_GGE) is set by the GGE distribution,
# which is integrability-protected. So epsilon mainly rescales the MAGNITUDE
# of the GGE contribution, not its equation of state.
#
# This changes w_0 through the weighting of Josephson vs GGE:
#   w_0 = (-rho_J + P_GGE) / (rho_J + rho_GGE)
# Differentiating w.r.t. rho_GGE (with P_GGE = w_GGE * rho_GGE, w_GGE fixed):

w_GGE = P_GGE / rho_GGE   # -0.403
rho_J = abs(F_Josephson) / N_cells  # canonical

# dw_0/d(rho_GGE) = [rho_J * (1 + w_GGE)] / (rho_J + rho_GGE)**2
dw0_drhoGGE = (rho_J * (1 + w_GGE)) / (rho_J + rho_GGE)**2

# delta(rho_GGE) = rho_GGE * sigma_eps_frac (linear scaling)
delta_rhoGGE = rho_GGE * sigma_eps_frac
delta_w0_eps = abs(dw0_drhoGGE) * delta_rhoGGE

# epsilon doesn't change w_a significantly (GGE is integrability-locked)
delta_wa_eps = abs(wa_A_central) * sigma_eps_frac  # fractional scaling

print(f"\n  epsilon variation:")
print(f"    epsilon = {epsilon_central:.6f} +/- {sigma_eps_frac*100:.1f}%")
print(f"    w_GGE = {w_GGE:.6f}")
print(f"    dw_0/d(rho_GGE) = {dw0_drhoGGE:.6e}")
print(f"    delta_w0 from epsilon = {delta_w0_eps:.6e}")
print(f"    delta_wa from epsilon = {delta_wa_eps:.6e}")

# =============================================================================
# 3. Combined uncertainty and contour generation
# =============================================================================
# Total 1-sigma uncertainties (add in quadrature for continuous params,
# envelope for discrete N_cells)

# Continuous uncertainties (tau + epsilon) in quadrature
sigma_w0_cont = np.sqrt(delta_w0_tau**2 + delta_w0_eps**2)
sigma_wa_cont = np.sqrt(delta_wa_tau**2 + delta_wa_eps**2)

# Discrete N_cells shifts w_0 but not w_a
w0_Ncells_spread = (w0_Ncells.max() - w0_Ncells.min()) / 2.0  # half-range
# Use the max of continuous and discrete as the effective sigma
sigma_w0_total = np.sqrt(sigma_w0_cont**2 + w0_Ncells_spread**2)
sigma_wa_total = sigma_wa_cont  # N_cells doesn't affect w_a

# Framework central prediction
w0_fw = w0_A_central   # -0.918
wa_fw = wa_A_central   # -0.000575

print(f"\n=== Framework Prediction ===")
print(f"  w_0 = {w0_fw:.4f} +/- {sigma_w0_total:.4f}")
print(f"    (continuous: +/- {sigma_w0_cont:.4e})")
print(f"    (N_cells spread: +/- {w0_Ncells_spread:.4f})")
print(f"  w_a = {wa_fw:.6f} +/- {sigma_wa_total:.6f}")
print(f"  |w_a| < {abs(wa_fw) + 2*sigma_wa_total:.4f} (2-sigma upper bound)")

# =============================================================================
# 4. Monte Carlo contour generation
# =============================================================================
# Generate samples from the framework's parameter space
N_mc = 100000
rng = np.random.default_rng(42)

# Sample N_cells discretely
N_cells_samples = rng.choice(N_cells_values, size=N_mc)

# Sample tau_fold and epsilon as Gaussians
tau_fold_samples = rng.normal(tau_fold, sigma_tau, size=N_mc)
eps_samples = rng.normal(epsilon_central, epsilon_central * sigma_eps_frac, size=N_mc)
eps_samples = np.clip(eps_samples, 1e-6, None)  # epsilon must be positive

# Compute w_0 for each sample
# rho_J depends on N_cells, rho_GGE scales linearly with epsilon
rho_J_samples = abs(F_Josephson) / N_cells_samples
rho_GGE_samples = rho_GGE * (eps_samples / epsilon_central)
P_GGE_samples = w_GGE * rho_GGE_samples  # w_GGE fixed by integrability

rho_DE_samples = rho_J_samples + rho_GGE_samples
P_DE_samples = -rho_J_samples + P_GGE_samples
w0_samples = P_DE_samples / rho_DE_samples

# w_a: near-zero with tiny variation from tau_fold shift
# w_a(tau) ~ w_a_central + d2w/dtau2 * (tau - tau_fold)
# But the dominant physics is that w(z) is flat, so w_a stays near zero
wa_samples = wa_A_central + rng.normal(0, sigma_wa_total, size=N_mc)

print(f"\n=== Monte Carlo Results ({N_mc} samples) ===")
print(f"  w_0: mean = {np.mean(w0_samples):.4f}, std = {np.std(w0_samples):.4f}")
print(f"  w_0: [2.5%, 97.5%] = [{np.percentile(w0_samples, 2.5):.4f}, {np.percentile(w0_samples, 97.5):.4f}]")
print(f"  w_a: mean = {np.mean(wa_samples):.6f}, std = {np.std(wa_samples):.6f}")
print(f"  w_a: [2.5%, 97.5%] = [{np.percentile(wa_samples, 2.5):.6f}, {np.percentile(wa_samples, 97.5):.6f}]")

# Framework 68% and 95% contour ellipse parameters
w0_mean_mc = np.mean(w0_samples)
wa_mean_mc = np.mean(wa_samples)
cov_fw = np.cov(w0_samples, wa_samples)
sigma_w0_mc = np.sqrt(cov_fw[0, 0])
sigma_wa_mc = np.sqrt(cov_fw[1, 1])
rho_corr = cov_fw[0, 1] / (sigma_w0_mc * sigma_wa_mc) if sigma_w0_mc > 0 and sigma_wa_mc > 0 else 0

print(f"\n  Covariance matrix:")
print(f"    sigma(w_0) = {sigma_w0_mc:.4f}")
print(f"    sigma(w_a) = {sigma_wa_mc:.6f}")
print(f"    correlation = {rho_corr:.4f}")

# =============================================================================
# 5. DESI DR2 and projected DR3 contours
# =============================================================================
# DR2 values (from data)
dr2_w0 = desi_dr2_w0         # -0.752
dr2_w0_e = desi_dr2_w0_e     # 0.057
dr2_wa = desi_dr2_wa          # -0.73
dr2_wa_e = desi_dr2_wa_e     # 0.25

# DR3 projection: sqrt(2) improvement in errors (doubled statistics)
# Central values assumed equal to DR2 (conservative for exclusion estimate)
dr3_w0 = dr2_w0               # -0.752 (assumed)
dr3_w0_e = dr2_w0_e / np.sqrt(2)   # ~0.040
dr3_wa = dr2_wa                # -0.73 (assumed)
dr3_wa_e = dr2_wa_e / np.sqrt(2)   # ~0.177

# DESI w_0-w_a correlation coefficient
# From DESI DR2 public results, the w_0-w_a correlation is approximately -0.85
# (strong negative correlation: more negative w_0 implies less negative w_a)
rho_desi = -0.85  # (local)

print(f"\n=== DESI Contours ===")
print(f"  DR2: w_0 = {dr2_w0:.3f} +/- {dr2_w0_e:.3f}, w_a = {dr2_wa:.2f} +/- {dr2_wa_e:.2f}")
print(f"  DR3 (projected): w_0 = {dr3_w0:.3f} +/- {dr3_w0_e:.3f}, w_a = {dr3_wa:.2f} +/- {dr3_wa_e:.2f}")
print(f"  w_0-w_a correlation (assumed): {rho_desi:.2f}")

# =============================================================================
# 6. Overlap computation (grid-based)
# =============================================================================
# Compute overlap between framework and DESI DR3 2D Gaussians on a fine grid

# Grid in w_0-w_a plane
w0_grid = np.linspace(-1.3, -0.3, 500)
wa_grid = np.linspace(-2.0, 1.0, 500)
W0, WA = np.meshgrid(w0_grid, wa_grid)
dw0 = w0_grid[1] - w0_grid[0]
dwa = wa_grid[1] - wa_grid[0]

# Framework PDF (from MC histogram, smoothed to 2D Gaussian)
# Use the MC-derived covariance
cov_fw_2d = cov_fw  # from MC above
mean_fw = np.array([w0_mean_mc, wa_mean_mc])

# Since framework's w_a variance is tiny, the 2D Gaussian is extremely elongated
# along w_0 and nearly a delta function in w_a. We need to handle this carefully.
# Use scipy multivariate normal
try:
    rv_fw = stats.multivariate_normal(mean_fw, cov_fw_2d)
    pdf_fw = rv_fw.pdf(np.dstack([W0, WA]))
except np.linalg.LinAlgError:
    # If covariance is singular (wa variance too small), use product of marginals
    print("  WARNING: Framework covariance nearly singular, using product of marginals")
    pdf_w0_fw = stats.norm.pdf(W0, loc=w0_mean_mc, scale=max(sigma_w0_mc, 1e-6))
    pdf_wa_fw = stats.norm.pdf(WA, loc=wa_mean_mc, scale=max(sigma_wa_mc, 1e-8))
    pdf_fw = pdf_w0_fw * pdf_wa_fw

# Normalize
pdf_fw = pdf_fw / (np.sum(pdf_fw) * dw0 * dwa)

# DESI DR3 PDF (2D Gaussian with correlation)
cov_dr3 = np.array([
    [dr3_w0_e**2, rho_desi * dr3_w0_e * dr3_wa_e],
    [rho_desi * dr3_w0_e * dr3_wa_e, dr3_wa_e**2]
])
mean_dr3 = np.array([dr3_w0, dr3_wa])
rv_dr3 = stats.multivariate_normal(mean_dr3, cov_dr3)
pdf_dr3 = rv_dr3.pdf(np.dstack([W0, WA]))
pdf_dr3 = pdf_dr3 / (np.sum(pdf_dr3) * dw0 * dwa)

# DESI DR2 PDF
cov_dr2 = np.array([
    [dr2_w0_e**2, rho_desi * dr2_w0_e * dr2_wa_e],
    [rho_desi * dr2_w0_e * dr2_wa_e, dr2_wa_e**2]
])
mean_dr2 = np.array([dr2_w0, dr2_wa])
rv_dr2 = stats.multivariate_normal(mean_dr2, cov_dr2)
pdf_dr2 = rv_dr2.pdf(np.dstack([W0, WA]))
pdf_dr2 = pdf_dr2 / (np.sum(pdf_dr2) * dw0 * dwa)

# Overlap integral: integral of min(p_fw, p_desi) dw0 dwa
# This is the Bhattacharyya-like overlap (probability of confusion)
overlap_dr3 = np.sum(np.minimum(pdf_fw, pdf_dr3)) * dw0 * dwa
overlap_dr2 = np.sum(np.minimum(pdf_fw, pdf_dr2)) * dw0 * dwa

# Alternative: area overlap of 95% contour regions
# For 2D Gaussian, 95% contour encloses chi2 < 5.991 (2 dof)
chi2_95 = 5.991  # (local)
chi2_68 = 2.30  # (local)

# Framework 95% region (as MC percentile)
# The framework contour is dominated by N_cells discreteness
# Compute chi2 for each grid point under framework distribution
fw_chi2 = np.zeros_like(W0)
try:
    inv_cov_fw = np.linalg.inv(cov_fw_2d)
    dw = np.dstack([W0 - mean_fw[0], WA - mean_fw[1]])
    fw_chi2 = np.einsum('...i,ij,...j->...', dw, inv_cov_fw, dw)
except np.linalg.LinAlgError:
    # Fallback: use marginal chi2
    fw_chi2 = ((W0 - mean_fw[0])/max(sigma_w0_mc, 1e-6))**2 + \
              ((WA - mean_fw[1])/max(sigma_wa_mc, 1e-8))**2

# DR3 chi2
inv_cov_dr3 = np.linalg.inv(cov_dr3)
dw_dr3 = np.dstack([W0 - mean_dr3[0], WA - mean_dr3[1]])
dr3_chi2 = np.einsum('...i,ij,...j->...', dw_dr3, inv_cov_dr3, dw_dr3)

# DR2 chi2
inv_cov_dr2 = np.linalg.inv(cov_dr2)
dw_dr2 = np.dstack([W0 - mean_dr2[0], WA - mean_dr2[1]])
dr2_chi2 = np.einsum('...i,ij,...j->...', dw_dr2, inv_cov_dr2, dw_dr2)

# 95% contour overlap: fraction of grid points inside BOTH 95% regions
mask_fw_95 = fw_chi2 < chi2_95
mask_dr3_95 = dr3_chi2 < chi2_95
mask_dr2_95 = dr2_chi2 < chi2_95

# Overlap area as fraction of DESI DR3 95% area (the relevant denominator)
area_fw_95 = np.sum(mask_fw_95) * dw0 * dwa
area_dr3_95 = np.sum(mask_dr3_95) * dw0 * dwa
area_dr2_95 = np.sum(mask_dr2_95) * dw0 * dwa
area_overlap_dr3 = np.sum(mask_fw_95 & mask_dr3_95) * dw0 * dwa
area_overlap_dr2 = np.sum(mask_fw_95 & mask_dr2_95) * dw0 * dwa

# Overlap as fraction of DR3 area (how much of DESI DR3 space the framework occupies)
frac_overlap_dr3 = area_overlap_dr3 / area_dr3_95 if area_dr3_95 > 0 else 0
frac_overlap_dr2 = area_overlap_dr2 / area_dr2_95 if area_dr2_95 > 0 else 0

# Also compute overlap as fraction of union (Jaccard-like)
area_union_dr3 = np.sum(mask_fw_95 | mask_dr3_95) * dw0 * dwa
frac_jaccard_dr3 = area_overlap_dr3 / area_union_dr3 if area_union_dr3 > 0 else 0

print(f"\n=== Contour Overlap ===")
print(f"  Framework 95% area:    {area_fw_95:.4f}")
print(f"  DESI DR3 95% area:     {area_dr3_95:.4f}")
print(f"  DESI DR2 95% area:     {area_dr2_95:.4f}")
print(f"  Overlap (FW & DR3 95%): {area_overlap_dr3:.6f}")
print(f"  Overlap (FW & DR2 95%): {area_overlap_dr2:.6f}")
print(f"  Overlap / DR3_area:    {frac_overlap_dr3*100:.2f}%")
print(f"  Overlap / DR2_area:    {frac_overlap_dr2*100:.2f}%")
print(f"  Jaccard (DR3):         {frac_jaccard_dr3*100:.2f}%")
print(f"  PDF overlap integral (DR3): {overlap_dr3:.6e}")
print(f"  PDF overlap integral (DR2): {overlap_dr2:.6e}")

# =============================================================================
# 7. Significance calculations
# =============================================================================

# 7a. At what significance does DR3 exclude w_a = 0?
# w_a = 0 vs DR3 central w_a = -0.73 with sigma = 0.177
sigma_wa0_dr3 = abs(dr3_wa - 0) / dr3_wa_e
sigma_wa0_dr2 = abs(dr2_wa - 0) / dr2_wa_e

print(f"\n=== Significance of w_a = 0 Exclusion ===")
print(f"  DR2: w_a = 0 excluded at {sigma_wa0_dr2:.2f} sigma")
print(f"  DR3 (projected): w_a = 0 excluded at {sigma_wa0_dr3:.2f} sigma")

# 7b. 2D significance: framework point (w0_fw, wa_fw) vs DESI DR3
delta_fw_dr3 = np.array([w0_fw - dr3_w0, wa_fw - dr3_wa])
chi2_fw_dr3 = delta_fw_dr3 @ inv_cov_dr3 @ delta_fw_dr3
sigma_2d_fw_dr3 = np.sqrt(chi2_fw_dr3)

delta_fw_dr2 = np.array([w0_fw - dr2_w0, wa_fw - dr2_wa])
chi2_fw_dr2 = delta_fw_dr2 @ inv_cov_dr2 @ delta_fw_dr2
sigma_2d_fw_dr2 = np.sqrt(chi2_fw_dr2)

print(f"\n=== 2D Tension (Framework vs DESI) ===")
print(f"  Framework: (w_0, w_a) = ({w0_fw:.4f}, {wa_fw:.6f})")
print(f"  DR2: chi2 = {chi2_fw_dr2:.2f}, sigma_2D = {sigma_2d_fw_dr2:.2f}")
print(f"  DR3 (projected): chi2 = {chi2_fw_dr3:.2f}, sigma_2D = {sigma_2d_fw_dr3:.2f}")

# 7c. What DR3 measurement would definitively exclude the framework?
# Framework predicts w_a = -0.0006 +/- ~0.001.
# The framework is excluded if DESI DR3 measures w_a < -X at Y sigma,
# where X is distant enough from ~0 that even the framework's 2-sigma region is excluded.
# With DR3 sigma(w_a) ~ 0.177:
#   Framework excluded at 3-sigma if: |w_a(DR3) - wa_fw| > 3 * sqrt(dr3_wa_e^2 + sigma_wa_mc^2)
# Since sigma_wa_mc << dr3_wa_e, the threshold is dominated by DR3 error.
wa_critical_3sig = wa_fw - 3 * np.sqrt(dr3_wa_e**2 + sigma_wa_mc**2)
wa_critical_5sig = wa_fw - 5 * np.sqrt(dr3_wa_e**2 + sigma_wa_mc**2)

# More precisely: if DR3 measures w_a = X, the framework (at w_a ~ 0) is excluded at
# significance = |X - 0| / sqrt(dr3_wa_e^2 + sigma_wa_mc^2)
# For 3-sigma exclusion, need X < -3 * dr3_wa_e ~ -0.53
# For 5-sigma exclusion, need X < -5 * dr3_wa_e ~ -0.88

wa_excl_3sig = -3 * dr3_wa_e  # -0.530
wa_excl_5sig = -5 * dr3_wa_e  # -0.884

# Current DR2 measurement gives:
sigma_current = abs(dr2_wa) / dr3_wa_e  # using DR3 errors

print(f"\n=== Critical DR3 Measurements ===")
print(f"  Framework prediction: w_a = {wa_fw:.6f} +/- {sigma_wa_mc:.6f}")
print(f"  DR3 sigma(w_a): {dr3_wa_e:.3f}")
print(f"  For 3-sigma exclusion of framework: DR3 needs w_a < {wa_excl_3sig:.3f}")
print(f"  For 5-sigma exclusion of framework: DR3 needs w_a < {wa_excl_5sig:.3f}")
print(f"  DR2 central value w_a = {dr2_wa:.2f} would give: {abs(dr2_wa)/dr3_wa_e:.1f}-sigma exclusion (with DR3 errors)")

# 7d. Probability that DR3 excludes framework at 3-sigma, given DR2 posterior
# If DR3 central ~ N(dr2_wa, dr3_wa_e), what is P(|w_a_DR3| / dr3_wa_e > 3)?
# This is P(w_a_DR3 < -3*dr3_wa_e) since we expect w_a < 0
p_exclude_3sig = stats.norm.cdf(wa_excl_3sig, loc=dr2_wa, scale=dr3_wa_e)
p_exclude_5sig = stats.norm.cdf(wa_excl_5sig, loc=dr2_wa, scale=dr3_wa_e)

# Actually we want P(framework excluded), i.e., P(w_a_DR3 < wa_excl_3sig)
# where wa_excl_3sig = -0.53 and DR3 ~ N(-0.73, 0.177)
# P = Phi((-0.53 - (-0.73)) / 0.177) = Phi(0.20/0.177) = Phi(1.13) = 87%
p_fw_excl_3sig_from_dr2 = 1.0 - stats.norm.cdf(wa_excl_3sig, loc=dr2_wa, scale=dr3_wa_e)
p_fw_excl_5sig_from_dr2 = 1.0 - stats.norm.cdf(wa_excl_5sig, loc=dr2_wa, scale=dr3_wa_e)

# Wait — we need to be careful with the sign. Framework at ~0, DESI at -0.73.
# Framework excluded if DR3 measures w_a sufficiently negative (far from 0).
# So we want P(w_a_DR3 < wa_excl_3sig) where wa_excl_3sig is the THRESHOLD
# below which w_a=0 is excluded.
# Actually: framework (w_a=0) is excluded at 3-sigma if w_a_measured < -3*sigma_DR3 = -0.53
# We want P(w_a_DR3 < -0.53 | w_a_true = -0.73, sigma = 0.177)
# = Phi((-0.53 + 0.73)/0.177) = Phi(1.13) = 87%
p_fw_excl_3sig_correct = stats.norm.cdf(wa_excl_3sig, loc=dr2_wa, scale=dr3_wa_e)

print(f"\n=== Probability of Framework Exclusion by DR3 ===")
print(f"  (Assuming DR3 central ~ DR2 central)")
print(f"  P(DR3 excludes w_a=0 at 3-sigma): {p_fw_excl_3sig_correct*100:.1f}%")
print(f"  P(DR3 excludes w_a=0 at 5-sigma): {p_fw_excl_5sig_from_dr2*100:.1f}%")

# =============================================================================
# 8. LCDM comparison point
# =============================================================================
# LCDM: w_0 = -1, w_a = 0
lcdm_w0, lcdm_wa = -1.0, 0.0
delta_lcdm_dr3 = np.array([lcdm_w0 - dr3_w0, lcdm_wa - dr3_wa])
chi2_lcdm_dr3 = delta_lcdm_dr3 @ inv_cov_dr3 @ delta_lcdm_dr3
sigma_lcdm_dr3 = np.sqrt(chi2_lcdm_dr3)

delta_lcdm_dr2 = np.array([lcdm_w0 - dr2_w0, lcdm_wa - dr2_wa])
chi2_lcdm_dr2 = delta_lcdm_dr2 @ inv_cov_dr2 @ delta_lcdm_dr2
sigma_lcdm_dr2 = np.sqrt(chi2_lcdm_dr2)

print(f"\n=== LCDM Comparison ===")
print(f"  LCDM: (w_0, w_a) = ({lcdm_w0:.1f}, {lcdm_wa:.1f})")
print(f"  DR2 tension: {sigma_lcdm_dr2:.2f} sigma")
print(f"  DR3 projected tension: {sigma_lcdm_dr3:.2f} sigma")

# Framework vs LCDM distance in the w_0-w_a plane
delta_fw_lcdm = np.sqrt((w0_fw - lcdm_w0)**2 + (wa_fw - lcdm_wa)**2)
print(f"  Framework-LCDM distance in w_0-w_a: {delta_fw_lcdm:.4f}")
print(f"  Framework sits {abs(w0_fw - lcdm_w0)/dr3_w0_e:.1f} sigma from LCDM in w_0")

# =============================================================================
# 9. Gate verdict
# =============================================================================
print(f"\n{'='*72}")
print(f"GATE: WA-ERROR-PROP-59")
print(f"{'='*72}")

# The gate uses the 95% contour overlap fraction (FW 95% & DR3 95%) / DR3 95% area
# PASS: > 5%
# FAIL: < 1%
# INFO: 1-5%

gate_metric = frac_overlap_dr3 * 100  # percentage

if gate_metric > 5.0:
    gate_verdict = "PASS"
    gate_detail = f"overlap = {gate_metric:.2f}% > 5% threshold"
elif gate_metric < 1.0:
    gate_verdict = "FAIL"
    gate_detail = f"overlap = {gate_metric:.2f}% < 1% threshold (framework excluded at > 3 sigma by projected DR3)"
else:
    gate_verdict = "INFO"
    gate_detail = f"overlap = {gate_metric:.2f}% in [1%, 5%] range"

print(f"  Overlap (FW 95% & DR3 95%)/DR3 = {gate_metric:.2f}%")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# =============================================================================
# 10. Save results
# =============================================================================
np.savez(
    os.path.join(SCRIPT_DIR, 's59_wa_error_prop.npz'),
    # Framework prediction
    w0_fw=w0_fw,
    wa_fw=wa_fw,
    sigma_w0_fw=sigma_w0_mc,
    sigma_wa_fw=sigma_wa_mc,
    cov_fw=cov_fw,
    w0_mean_mc=w0_mean_mc,
    wa_mean_mc=wa_mean_mc,
    # Uncertainty components
    delta_w0_tau=delta_w0_tau,
    delta_w0_eps=delta_w0_eps,
    w0_Ncells_spread=w0_Ncells_spread,
    delta_wa_tau=delta_wa_tau,
    delta_wa_eps=delta_wa_eps,
    sigma_w0_total=sigma_w0_total,
    sigma_wa_total=sigma_wa_total,
    # N_cells variation
    N_cells_values=N_cells_values,
    w0_Ncells=w0_Ncells,
    # DESI values
    dr2_w0=dr2_w0, dr2_w0_e=dr2_w0_e,
    dr2_wa=dr2_wa, dr2_wa_e=dr2_wa_e,
    dr3_w0=dr3_w0, dr3_w0_e=dr3_w0_e,
    dr3_wa=dr3_wa, dr3_wa_e=dr3_wa_e,
    rho_desi=rho_desi,
    # Overlap
    overlap_pdf_dr3=overlap_dr3,
    overlap_pdf_dr2=overlap_dr2,
    area_fw_95=area_fw_95,
    area_dr3_95=area_dr3_95,
    area_dr2_95=area_dr2_95,
    area_overlap_dr3=area_overlap_dr3,
    area_overlap_dr2=area_overlap_dr2,
    frac_overlap_dr3=frac_overlap_dr3,
    frac_overlap_dr2=frac_overlap_dr2,
    frac_jaccard_dr3=frac_jaccard_dr3,
    # Significance
    sigma_wa0_dr2=sigma_wa0_dr2,
    sigma_wa0_dr3=sigma_wa0_dr3,
    sigma_2d_fw_dr2=sigma_2d_fw_dr2,
    sigma_2d_fw_dr3=sigma_2d_fw_dr3,
    sigma_lcdm_dr2=sigma_lcdm_dr2,
    sigma_lcdm_dr3=sigma_lcdm_dr3,
    # Critical thresholds
    wa_excl_3sig=wa_excl_3sig,
    wa_excl_5sig=wa_excl_5sig,
    p_fw_excl_3sig=p_fw_excl_3sig_correct,
    p_fw_excl_5sig=p_fw_excl_5sig_from_dr2,
    # LCDM comparison
    delta_fw_lcdm=delta_fw_lcdm,
    # Gate
    gate_name=np.array(['WA-ERROR-PROP-59']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)

print(f"\n  Saved: s59_wa_error_prop.npz")

# =============================================================================
# 11. Plot
# =============================================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# --- Contour levels for 68% and 95% in 2D (chi2 values) ---
levels_68 = [chi2_68]
levels_95 = [chi2_95]

# Framework contours
if np.linalg.det(cov_fw_2d) > 0:
    ax.contour(W0, WA, fw_chi2, levels=levels_68, colors='#2166ac', linewidths=1.5, linestyles='-')
    cs_fw95 = ax.contour(W0, WA, fw_chi2, levels=levels_95, colors='#2166ac', linewidths=2.0, linestyles='--')
    ax.contourf(W0, WA, fw_chi2, levels=[0, chi2_95], colors=[to_rgba('#2166ac', 0.15)])
    ax.contourf(W0, WA, fw_chi2, levels=[0, chi2_68], colors=[to_rgba('#2166ac', 0.25)])

# DESI DR2 contours
ax.contour(W0, WA, dr2_chi2, levels=levels_68, colors='#b2182b', linewidths=1.2, linestyles='-')
ax.contour(W0, WA, dr2_chi2, levels=levels_95, colors='#b2182b', linewidths=1.5, linestyles='--')
ax.contourf(W0, WA, dr2_chi2, levels=[0, chi2_95], colors=[to_rgba('#b2182b', 0.08)])
ax.contourf(W0, WA, dr2_chi2, levels=[0, chi2_68], colors=[to_rgba('#b2182b', 0.15)])

# DESI DR3 projected contours
ax.contour(W0, WA, dr3_chi2, levels=levels_68, colors='#d6604d', linewidths=1.2, linestyles='-')
ax.contour(W0, WA, dr3_chi2, levels=levels_95, colors='#d6604d', linewidths=2.5, linestyles='--')
ax.contourf(W0, WA, dr3_chi2, levels=[0, chi2_95], colors=[to_rgba('#d6604d', 0.08)])

# Mark central points
ax.plot(w0_fw, wa_fw, 'o', color='#2166ac', ms=10, zorder=10, label=f'Framework ({w0_fw:.3f}, {wa_fw:.4f})')
ax.plot(dr2_w0, dr2_wa, 's', color='#b2182b', ms=8, zorder=10, label=f'DESI DR2 ({dr2_w0:.3f}, {dr2_wa:.2f})')
ax.plot(dr3_w0, dr3_wa, 'D', color='#d6604d', ms=8, zorder=10, label=f'DESI DR3 proj. ({dr3_w0:.3f}, {dr3_wa:.2f})')
ax.plot(lcdm_w0, lcdm_wa, '*', color='black', ms=14, zorder=10, label=r'$\Lambda$CDM ($-1, 0$)')

# Mark N_cells variation
for i, N in enumerate(N_cells_values):
    marker = 'v' if N == 24 else ('^' if N == 48 else 'o')
    ax.plot(w0_Ncells[i], wa_fw, marker, color='#4393c3', ms=7, zorder=9,
            alpha=0.7, label=f'N={N}: w_0={w0_Ncells[i]:.3f}' if i == 0 or i == 2 else None)  # (local)

# Reference lines
ax.axhline(0, color='gray', ls=':', lw=0.8, alpha=0.5)
ax.axvline(-1, color='gray', ls=':', lw=0.8, alpha=0.5)

# Annotations
ax.annotate(f'2D tension:\n  DR2: {sigma_2d_fw_dr2:.1f}$\\sigma$\n  DR3: {sigma_2d_fw_dr3:.1f}$\\sigma$',
            xy=(0.03, 0.97), xycoords='axes fraction', va='top', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

ax.annotate(f'w_a=0 exclusion:\n  DR2: {sigma_wa0_dr2:.1f}$\\sigma$\n  DR3: {sigma_wa0_dr3:.1f}$\\sigma$',
            xy=(0.03, 0.78), xycoords='axes fraction', va='top', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

ax.annotate(f'95% contour overlap:\n  DR3: {frac_overlap_dr3*100:.1f}%',
            xy=(0.03, 0.62), xycoords='axes fraction', va='top', fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='wheat', alpha=0.8))

# Labels
ax.set_xlabel(r'$w_0$', fontsize=14)
ax.set_ylabel(r'$w_a$', fontsize=14)
ax.set_title('WA-ERROR-PROP-59: Framework vs DESI in the $w_0$-$w_a$ Plane', fontsize=13)
ax.legend(loc='lower right', fontsize=8)
ax.set_xlim(-1.3, -0.3)
ax.set_ylim(-2.0, 1.0)
ax.tick_params(labelsize=11)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's59_wa_error_prop.png'), dpi=150, bbox_inches='tight')
print(f"  Saved: s59_wa_error_prop.png")

print(f"\n{'='*72}")
print(f"DONE: WA-ERROR-PROP-59")
print(f"{'='*72}")
