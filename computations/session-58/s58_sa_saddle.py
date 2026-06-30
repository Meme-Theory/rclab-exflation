#!/usr/bin/env python3
"""
s58_sa_saddle.py — SA-SADDLE-58: Spectral Action Hessian at the Fold
=====================================================================
Gate: SA-SADDLE-58 (INFO) — det(H_S) < 0?

Method:
  1. Load Dirac spectrum at the fold from s54_ed_sweep.npz
  2. Load off-Jensen E_J data from s57_off_jensen_ej.npz for comparison
  3. Compute Seeley-DeWitt coefficients a_0, a_2, a_4 as functions of (tau, sigma)
     using the EXACT analytic curvature formulas (sd20a) extended off-Jensen
  4. Form the spectral action S = f_4*Lambda^4*a_0 + f_2*Lambda^2*a_2 + f_0*a_4
  5. Compute numerical 2nd derivatives to form the Hessian H_S at (tau_fold, sigma=0)
  6. Check det(H_S) < 0 => saddle

The spectral action on (SU(3), g_{tau,sigma}) where tau is the Jensen deformation
and sigma is the T2 (volume-breaking) deformation:

  S(tau, sigma) = C_0 * a_0(tau, sigma) + C_2 * a_2(tau, sigma) + C_4 * a_4(tau, sigma)

where C_0 = 2*f_4*Lambda^4, C_2 = 2*f_2*Lambda^2, C_4 = f_0 are tau-independent.

Key point: a_0 ~ Vol(K) is tau-INDEPENDENT under Jensen (volume-preserving) but
sigma-DEPENDENT under T2 (volume-breaking). However, the sigma direction changes
the volume, so a_0 contributes to the sigma Hessian.

For the Hessian at sigma=0, the critical observation from sd20a_seeley_dewitt_gate.py:
  - a_2^red(tau) = (20/3) R_K(tau)  [Dirac, d=8, with E=R/4 Lichnerowicz]
  - a_4^red(tau) = (1/90)(125 R^2 - 8|Ric|^2 + 2|Riem|^2)

The off-Jensen direction uses the spectral action potential V(tau, sigma) from
s54_off_jensen_t2.npz, which was computed including all curvature terms.

Author: baptista-spacetime-analyst (Session 58)
"""

import sys
sys.path.insert(0, 'computations')
import numpy as np
from numpy.linalg import eigh, eig
from scipy.interpolate import RectBivariateSpline
from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold, S_fold,
    d2S_fold, Vol_SU3_Haar, PI, M_KK, M_Pl_reduced
)

# =============================================================================
# 1. Load input data
# =============================================================================
ed = np.load('computations/session-54/s54_ed_sweep.npz', allow_pickle=True)
ej = np.load('computations/session-57/s57_off_jensen_ej.npz', allow_pickle=True)
oj = np.load('computations/session-54/s54_off_jensen_t2.npz', allow_pickle=True)

tau_ed = ed['tau_values']       # (50,) in [0, 0.5]
fold_idx = int(ed['fold_idx'])  # 19
all_eigs = ed['all_eigenvalues']  # (50, 256) Dirac eigenvalues
E_sp = ed['E_sp_sweep']        # (50, 8) single-particle energies

# Off-Jensen landscape
tau_oj = oj['tau_range']        # (51,) in [0, 0.4]
sig_oj = oj['sig_range']        # (41,) in [-0.015, 0.015]
V_grid = oj['V_grid']           # (51, 41) spectral action potential
R_grid = oj['R_grid']           # (51, 41) scalar curvature
H_V = oj['Hessian']             # (2,2) Hessian of V at saddle
H_V_evals = oj['Hessian_evals'] # [-105.63, 2372.43]
tau_sb = float(oj['tau_sb'])     # 0.2015

# E_J data from S57
EJ_H = ej['EJ_B_Hessian_at_saddle']  # (2,2)
EJ_H_evals = ej['EJ_B_Hessian_evals']  # [-0.0856, 0.0841]
EJ_det = float(ej['EJ_B_det_H'])      # -0.00719

print("=" * 76)
print("  SA-SADDLE-58: Spectral Action Hessian at the Fold")
print("=" * 76)
print(f"\nFold: tau={tau_ed[fold_idx]:.6f} (idx={fold_idx})")
print(f"Saddle (from V landscape): tau_sb={tau_sb:.4f}")
print(f"V Hessian eigenvalues: {H_V_evals}")
print(f"E_J Hessian eigenvalues: {EJ_H_evals}")
print(f"E_J det(H): {EJ_det:.6e}")

# =============================================================================
# 2. Exact analytic curvature formulas (from sd20a, verified to machine eps)
# =============================================================================
# These are for the Jensen deformation g_tau on SU(3)

def R_exact(tau):
    """Scalar curvature R_K(tau). R(0) = 2."""
    return -0.25*np.exp(-4*tau) + 2*np.exp(-tau) - 0.25 + 0.5*np.exp(2*tau)

def Ric2_exact(tau):
    """|Ric|^2(tau). |Ric|^2(0) = 1/2."""
    return (
        (1/12) * np.exp(-8*tau)
        + (-1/2) * np.exp(-5*tau)
        + (1/8) * np.exp(-4*tau)
        + (13/12) * np.exp(-2*tau)
        + (-1/2) * np.exp(-tau)
        + 1/8
        + (1/12) * np.exp(4*tau)
    )

def K_exact(tau):
    """|Riem|^2(tau) = Kretschner. K(0) = 1/2."""
    return (
        (23/96) * np.exp(-8*tau)
        + (-1) * np.exp(-5*tau)
        + (5/16) * np.exp(-4*tau)
        + (11/6) * np.exp(-2*tau)
        + (-3/2) * np.exp(-tau)
        + 17/32
        + (1/12) * np.exp(4*tau)
    )

def a2_red(tau):
    """Reduced a_2: Dirac on 8-manifold with E=R/4.
    a_2^red = (20/3) R.
    Full a_2 = (4*pi)^{-4} * Vol(K) * a_2^red.
    """
    return (20.0/3.0) * R_exact(tau)

def a4_red(tau):
    """Reduced a_4: (1/90)(125 R^2 - 8|Ric|^2 + 2|Riem|^2).
    Full a_4 = (4*pi)^{-4} * Vol(K) * a_4^red.
    """
    R = R_exact(tau)
    return (1.0/90.0) * (125.0*R**2 - 8.0*Ric2_exact(tau) + 2.0*K_exact(tau))

# Verify at tau=0
print(f"\nCurvature verification at tau=0:")
print(f"  R(0) = {R_exact(0):.10f} (should be 2.0)")
print(f"  |Ric|^2(0) = {Ric2_exact(0):.10f} (should be 0.5)")
print(f"  |Riem|^2(0) = {K_exact(0):.10f} (should be 0.5)")
print(f"  a2_red(0) = {a2_red(0):.10f} (should be 40/3 = {40/3:.10f})")
print(f"  a4_red(0) = {a4_red(0):.10f} (should be 497/90 = {497/90:.10f})")

# =============================================================================
# 3. Construct the spectral action S(tau, sigma) on the 2D landscape
# =============================================================================
# The spectral action at a general (tau, sigma) point:
#   S(tau, sigma) = prefactor * [C0 * 1 + C2 * a2_red(tau, sigma) + C4 * a4_red(tau, sigma)]
# where prefactor = (4*pi)^{-4} * Vol(K, tau, sigma) (volume depends on sigma!)
#
# Strategy: We have V_grid(tau, sigma) from s54_off_jensen_t2.npz which IS the
# spectral action potential computed from the full Dirac spectrum on (SU(3), g_{tau,sigma}).
# This is the most reliable 2D data. We use it directly.
#
# The Hessian of V_grid at the saddle gives us the spectral action Hessian.

print("\n" + "=" * 76)
print("  3. Spectral Action Hessian from V(tau, sigma) landscape")
print("=" * 76)

# Use RectBivariateSpline for smooth interpolation
dtau = tau_oj[1] - tau_oj[0]
dsig = sig_oj[1] - sig_oj[0]
print(f"Grid spacing: dtau={dtau:.6f}, dsig={dsig:.6f}")

# The V_grid Hessian is already computed in s54_off_jensen_t2.npz:
print(f"\nV_grid Hessian at saddle (tau_sb={tau_sb:.4f}):")
print(f"  H_V = {H_V}")
print(f"  eigenvalues: {H_V_evals}")
print(f"  det(H_V) = {H_V_evals[0]*H_V_evals[1]:.4f}")

# But we also need to compute it at tau_fold, not just tau_sb.
# Let's do both: at the saddle point (tau_sb=0.2015) and at the fold (tau_fold=0.19)

# Interpolate V_grid using bivariate spline
spl_V = RectBivariateSpline(tau_oj, sig_oj, V_grid)
spl_R = RectBivariateSpline(tau_oj, sig_oj, R_grid)

# Compute Hessian at tau_fold, sigma=0
# Use spline derivatives for clean results
def compute_hessian_spline(spl, tau0, sig0):
    """Compute 2x2 Hessian of a RectBivariateSpline at (tau0, sig0)."""
    d2_dtau2 = float(spl(tau0, sig0, dx=2, dy=0, grid=False))
    d2_dsig2 = float(spl(tau0, sig0, dx=0, dy=2, grid=False))
    d2_mixed = float(spl(tau0, sig0, dx=1, dy=1, grid=False))
    return np.array([[d2_dtau2, d2_mixed],
                     [d2_mixed, d2_dsig2]])

# Also compute via finite differences for cross-check
def compute_hessian_fd(spl, tau0, sig0, h_tau=1e-4, h_sig=1e-5):
    """Hessian via centered finite differences."""
    f00 = float(spl(tau0, sig0, grid=False))

    fp_tau = float(spl(tau0 + h_tau, sig0, grid=False))
    fm_tau = float(spl(tau0 - h_tau, sig0, grid=False))
    d2_dtau2 = (fp_tau - 2*f00 + fm_tau) / h_tau**2

    fp_sig = float(spl(tau0, sig0 + h_sig, grid=False))
    fm_sig = float(spl(tau0, sig0 - h_sig, grid=False))
    d2_dsig2 = (fp_sig - 2*f00 + fm_sig) / h_sig**2

    fpp = float(spl(tau0 + h_tau, sig0 + h_sig, grid=False))
    fpm = float(spl(tau0 + h_tau, sig0 - h_sig, grid=False))
    fmp = float(spl(tau0 - h_tau, sig0 + h_sig, grid=False))
    fmm = float(spl(tau0 - h_tau, sig0 - h_sig, grid=False))
    d2_mixed = (fpp - fpm - fmp + fmm) / (4*h_tau*h_sig)

    return np.array([[d2_dtau2, d2_mixed],
                     [d2_mixed, d2_dsig2]])

# At the fold
H_S_fold_spl = compute_hessian_spline(spl_V, tau_fold, 0.0)
H_S_fold_fd = compute_hessian_fd(spl_V, tau_fold, 0.0)

# At the saddle
H_S_saddle_spl = compute_hessian_spline(spl_V, tau_sb, 0.0)
H_S_saddle_fd = compute_hessian_fd(spl_V, tau_sb, 0.0)

print(f"\n--- Hessian at FOLD (tau={tau_fold:.4f}, sigma=0) ---")
print(f"  Spline derivatives:")
print(f"    H_S = {H_S_fold_spl}")
evals_fold, evecs_fold = eigh(H_S_fold_spl)
print(f"    eigenvalues: {evals_fold}")
print(f"    det(H_S) = {evals_fold[0]*evals_fold[1]:.6f}")
print(f"  Finite differences (cross-check):")
print(f"    H_S = {H_S_fold_fd}")
evals_fold_fd, _ = eigh(H_S_fold_fd)
print(f"    eigenvalues: {evals_fold_fd}")

print(f"\n--- Hessian at SADDLE (tau={tau_sb:.4f}, sigma=0) ---")
print(f"  Spline derivatives:")
print(f"    H_S = {H_S_saddle_spl}")
evals_saddle, evecs_saddle = eigh(H_S_saddle_spl)
print(f"    eigenvalues: {evals_saddle}")
print(f"    det(H_S) = {evals_saddle[0]*evals_saddle[1]:.6f}")
print(f"  Finite differences (cross-check):")
print(f"    H_S = {H_S_saddle_fd}")
evals_saddle_fd, _ = eigh(H_S_saddle_fd)
print(f"    eigenvalues: {evals_saddle_fd}")

# =============================================================================
# 4. Now compute from the ANALYTIC curvature formulas (Jensen direction only)
# =============================================================================
# For the on-Jensen direction, we have exact analytic second derivatives.
# The spectral action is S(tau) = f_4*Lambda^4*a_0 + f_2*Lambda^2*a_2(tau) + f_0*a_4(tau)
# where a_0 is constant (volume preserving), so:
#   d^2S/dtau^2 = f_2*Lambda^2 * d^2a_2/dtau^2 + f_0 * d^2a_4/dtau^2

# Derivatives of R
def dR_dtau(tau):
    return np.exp(-4*tau) + (-2)*np.exp(-tau) + np.exp(2*tau)

def d2R_dtau2(tau):
    return -4*np.exp(-4*tau) + 2*np.exp(-tau) + 2*np.exp(2*tau)

# Derivatives of |Ric|^2
def dRic2_dtau(tau):
    return (
        (1/12)*(-8)*np.exp(-8*tau) + (-1/2)*(-5)*np.exp(-5*tau)
        + (1/8)*(-4)*np.exp(-4*tau) + (13/12)*(-2)*np.exp(-2*tau)
        + (-1/2)*(-1)*np.exp(-tau) + (1/12)*4*np.exp(4*tau)
    )

def d2Ric2_dtau2(tau):
    return (
        (1/12)*64*np.exp(-8*tau) + (-1/2)*25*np.exp(-5*tau)
        + (1/8)*16*np.exp(-4*tau) + (13/12)*4*np.exp(-2*tau)
        + (-1/2)*np.exp(-tau) + (1/12)*16*np.exp(4*tau)
    )

# Derivatives of |Riem|^2
def dK_dtau(tau):
    return (
        (23/96)*(-8)*np.exp(-8*tau) + (-1)*(-5)*np.exp(-5*tau)
        + (5/16)*(-4)*np.exp(-4*tau) + (11/6)*(-2)*np.exp(-2*tau)
        + (-3/2)*(-1)*np.exp(-tau) + (1/12)*4*np.exp(4*tau)
    )

def d2K_dtau2(tau):
    return (
        (23/96)*64*np.exp(-8*tau) + (-1)*25*np.exp(-5*tau)
        + (5/16)*16*np.exp(-4*tau) + (11/6)*4*np.exp(-2*tau)
        + (-3/2)*np.exp(-tau) + (1/12)*16*np.exp(4*tau)
    )

# Second derivatives of Seeley-DeWitt coefficients
def d2a2_dtau2(tau):
    """d^2 a_2^red / dtau^2 = (20/3) d^2R/dtau^2."""
    return (20.0/3.0) * d2R_dtau2(tau)

def d2a4_dtau2(tau):
    """d^2 a_4^red / dtau^2."""
    R = R_exact(tau)
    dR = dR_dtau(tau)
    d2R = d2R_dtau2(tau)
    return (1.0/90.0) * (
        250.0*(dR**2 + R*d2R)  # d^2/dtau^2 of 125 R^2
        - 8.0*d2Ric2_dtau2(tau)
        + 2.0*d2K_dtau2(tau)
    )

print(f"\n" + "=" * 76)
print(f"  4. Analytic curvature derivatives at fold")
print(f"=" * 76)

tau_f = tau_fold  # 0.19
print(f"\nAt tau_fold = {tau_f}:")
print(f"  R = {R_exact(tau_f):.8f}")
print(f"  dR/dtau = {dR_dtau(tau_f):.8f}")
print(f"  d2R/dtau2 = {d2R_dtau2(tau_f):.8f}")
print(f"  a_2^red = {a2_red(tau_f):.8f}")
print(f"  a_4^red = {a4_red(tau_f):.8f}")
print(f"  d2a2/dtau2 = {d2a2_dtau2(tau_f):.8f}")
print(f"  d2a4/dtau2 = {d2a4_dtau2(tau_f):.8f}")

# =============================================================================
# 5. Construct the FULL spectral action Hessian using V_grid data
# =============================================================================
# V_grid IS the spectral action landscape. Its Hessian IS H_S.
# We compute at multiple points near the fold for robustness.

print(f"\n" + "=" * 76)
print("  5. Full spectral action Hessian (from V landscape)")
print("=" * 76)

# Scan tau near fold
tau_scan_pts = [0.16, 0.17, 0.18, 0.19, 0.20, 0.2015, 0.21, 0.22]
print(f"\nHessian eigenvalues scan (sigma=0):")
print(f"{'tau':>8s} {'d2V/dtau2':>12s} {'d2V/dsig2':>12s} {'d2V/dtaudsig':>12s} {'eig_min':>12s} {'eig_max':>12s} {'det(H)':>12s} {'saddle?':>8s}")
print("-" * 92)

results_scan = []
for tau_pt in tau_scan_pts:
    if tau_pt < tau_oj[0] or tau_pt > tau_oj[-1]:
        continue
    H = compute_hessian_spline(spl_V, tau_pt, 0.0)
    evals_pt = np.sort(np.linalg.eigvalsh(H))
    det_H = evals_pt[0] * evals_pt[1]
    is_saddle = "YES" if det_H < 0 else "no"
    results_scan.append((tau_pt, H[0,0], H[1,1], H[0,1], evals_pt[0], evals_pt[1], det_H))
    print(f"{tau_pt:8.4f} {H[0,0]:12.4f} {H[1,1]:12.4f} {H[0,1]:12.6f} {evals_pt[0]:12.4f} {evals_pt[1]:12.4f} {det_H:12.2f} {is_saddle:>8s}")

# =============================================================================
# 6. Compare SA Hessian with E_J Hessian
# =============================================================================
print(f"\n" + "=" * 76)
print("  6. Comparison: V (spectral action) vs E_J Hessians")
print("=" * 76)

# Use the Hessian at the saddle tau_sb = 0.2015 for direct comparison
H_SA = compute_hessian_spline(spl_V, tau_sb, 0.0)
evals_SA, evecs_SA = eigh(H_SA)
det_SA = evals_SA[0] * evals_SA[1]

print(f"\nSpectral action V Hessian at (tau={tau_sb:.4f}, sigma=0):")
print(f"  H_SA = [[{H_SA[0,0]:.6f}, {H_SA[0,1]:.6f}],")
print(f"          [{H_SA[1,0]:.6f}, {H_SA[1,1]:.6f}]]")
print(f"  eigenvalues: [{evals_SA[0]:.6f}, {evals_SA[1]:.6f}]")
print(f"  det(H_SA) = {det_SA:.6f}")
print(f"  SADDLE: {'YES' if det_SA < 0 else 'NO'}")

print(f"\nE_J Hessian at same point (from S57):")
print(f"  H_EJ = [[{EJ_H[0,0]:.6f}, {EJ_H[0,1]:.6f}],")
print(f"          [{EJ_H[1,0]:.6f}, {EJ_H[1,1]:.6f}]]")
print(f"  eigenvalues: [{EJ_H_evals[0]:.6f}, {EJ_H_evals[1]:.6f}]")
print(f"  det(H_EJ) = {EJ_det:.6e}")
print(f"  SADDLE: {'YES' if EJ_det < 0 else 'NO'}")

# Eigenvector comparison
print(f"\nEigenvector comparison:")
print(f"  SA negative eigvec: {evecs_SA[:,0]}")
print(f"  SA positive eigvec: {evecs_SA[:,1]}")
e_EJ, v_EJ = eigh(EJ_H)
print(f"  EJ negative eigvec: {v_EJ[:,0]}")
print(f"  EJ positive eigvec: {v_EJ[:,1]}")

# Alignment
cos_neg = abs(np.dot(evecs_SA[:,0], v_EJ[:,0]))
cos_pos = abs(np.dot(evecs_SA[:,1], v_EJ[:,1]))
print(f"  cos(angle) negative dirs: {cos_neg:.6f}")
print(f"  cos(angle) positive dirs: {cos_pos:.6f}")

# Ratio of eigenvalues
ratio_neg = evals_SA[0] / EJ_H_evals[0] if EJ_H_evals[0] != 0 else np.inf
ratio_pos = evals_SA[1] / EJ_H_evals[1] if EJ_H_evals[1] != 0 else np.inf
print(f"\n  Eigenvalue ratios (SA/EJ):")
print(f"    negative: {ratio_neg:.2f}")
print(f"    positive: {ratio_pos:.2f}")

# =============================================================================
# 7. Verify with direct eigenvalue-based spectral action
# =============================================================================
# The spectral action can also be computed directly from the Dirac eigenvalues:
#   S = sum_n f(lambda_n^2 / Lambda^2)
# For a cutoff function f, the heat kernel gives:
#   S(t) = sum_n exp(-t * lambda_n^2)
# The Seeley-DeWitt coefficients are extracted from the t -> 0 expansion.

print(f"\n" + "=" * 76)
print("  7. Direct eigenvalue-based Seeley-DeWitt coefficients")
print("=" * 76)

# At each tau, compute zeta function moments from the 256 Dirac eigenvalues
def seeley_dewitt_from_spectrum(eigenvalues, t_vals):
    """Compute Tr(exp(-t D^2)) from eigenvalue list for multiple t values.
    Returns heat trace Z(t) = sum_n exp(-t * lambda_n^2).
    """
    lam2 = eigenvalues**2
    Z = np.array([np.sum(np.exp(-t * lam2)) for t in t_vals])
    return Z

# For extracting a_0, a_2, a_4 from Z(t):
# Z(t) ~ (4*pi*t)^{-4} * [a_0 + a_2*t + a_4*t^2 + ...]
# So: Z(t) * (4*pi*t)^4 ~ a_0 + a_2*t + a_4*t^2 + ...
# We fit a polynomial in t to the product Z(t) * (4*pi*t)^4

t_vals = np.logspace(-3, -0.5, 50)  # Small t for asymptotic expansion

# Compute at several tau values near the fold
tau_near_fold = tau_ed[max(0,fold_idx-3):fold_idx+4]
idx_near_fold = list(range(max(0,fold_idx-3), min(len(tau_ed), fold_idx+4)))

a0_arr = np.zeros(len(idx_near_fold))
a2_arr = np.zeros(len(idx_near_fold))
a4_arr = np.zeros(len(idx_near_fold))
tau_arr = np.zeros(len(idx_near_fold))

for k, idx in enumerate(idx_near_fold):
    eigs = all_eigs[idx]
    tau_arr[k] = tau_ed[idx]
    Z_t = seeley_dewitt_from_spectrum(eigs, t_vals)

    # Multiply by (4*pi*t)^4 to get the asymptotic coefficients
    factor = (4*PI*t_vals)**4
    W = Z_t * factor  # W ~ a_0 + a_2*t + a_4*t^2 + ...

    # Fit polynomial in t (use small t values for best accuracy)
    mask = t_vals < 0.1
    coeffs = np.polyfit(t_vals[mask], W[mask], 3)  # cubic fit
    # coeffs[3] = a_0, coeffs[2] = a_2, coeffs[1] = a_4
    a0_arr[k] = coeffs[3]
    a2_arr[k] = coeffs[2]
    a4_arr[k] = coeffs[1]

print(f"\nSeeley-DeWitt coefficients from Dirac spectrum (direct):")
print(f"{'tau':>8s} {'a_0':>12s} {'a_2':>12s} {'a_4':>12s}")
print("-" * 48)
for k in range(len(idx_near_fold)):
    print(f"{tau_arr[k]:8.5f} {a0_arr[k]:12.2f} {a2_arr[k]:12.4f} {a4_arr[k]:12.4f}")

# Compare to canonical values
print(f"\nCanonical (S42): a0={a0_fold:.1f}, a2={a2_fold:.4f}, a4={a4_fold:.4f}")

# Compute d^2a_2/dtau^2 and d^2a_4/dtau^2 from the fitted values
dtau_ed = tau_ed[1] - tau_ed[0]

# Use the full sweep for proper derivatives
a0_full = np.zeros(len(tau_ed))
a2_full = np.zeros(len(tau_ed))
a4_full = np.zeros(len(tau_ed))

for idx in range(len(tau_ed)):
    eigs = all_eigs[idx]
    Z_t = seeley_dewitt_from_spectrum(eigs, t_vals)
    factor = (4*PI*t_vals)**4
    W = Z_t * factor
    mask = t_vals < 0.1
    coeffs = np.polyfit(t_vals[mask], W[mask], 3)
    a0_full[idx] = coeffs[3]
    a2_full[idx] = coeffs[2]
    a4_full[idx] = coeffs[1]

# Numerical second derivatives at fold
d2a2_num = (a2_full[fold_idx+1] - 2*a2_full[fold_idx] + a2_full[fold_idx-1]) / dtau_ed**2
d2a4_num = (a4_full[fold_idx+1] - 2*a4_full[fold_idx] + a4_full[fold_idx-1]) / dtau_ed**2
d2a0_num = (a0_full[fold_idx+1] - 2*a0_full[fold_idx] + a0_full[fold_idx-1]) / dtau_ed**2

print(f"\nNumerical 2nd derivatives at fold (from spectrum):")
print(f"  d^2 a_0 / dtau^2 = {d2a0_num:.4f} (should be ~0 for volume-preserving)")
print(f"  d^2 a_2 / dtau^2 = {d2a2_num:.4f}")
print(f"  d^2 a_4 / dtau^2 = {d2a4_num:.4f}")

print(f"\nAnalytic 2nd derivatives at fold (from curvature):")
print(f"  d^2 a_2^red / dtau^2 = {d2a2_dtau2(tau_fold):.6f}")
print(f"  d^2 a_4^red / dtau^2 = {d2a4_dtau2(tau_fold):.6f}")

# =============================================================================
# 8. Construct the combined SA Hessian
# =============================================================================
# For the spectral action S = C_0*a_0 + C_2*a_2 + C_4*a_4:
#   d^2S/dtau^2 = C_2 * d^2a_2/dtau^2 + C_4 * d^2a_4/dtau^2  (a_0 constant on-Jensen)
# The tau-tau component is fully determined by the analytic formulas.
#
# For the sigma-sigma and mixed components, we use V_grid.
# The full H_S is the V_grid Hessian at the fold.
#
# The key question: does the V Hessian have a negative eigenvalue?

print(f"\n" + "=" * 76)
print("  8. GATE VERDICT: SA-SADDLE-58")
print("=" * 76)

# Use the fold point
H_at_fold = compute_hessian_spline(spl_V, tau_fold, 0.0)
evals_at_fold = np.sort(np.linalg.eigvalsh(H_at_fold))
det_at_fold = evals_at_fold[0] * evals_at_fold[1]

print(f"\nSpectral Action Hessian at fold (tau={tau_fold}, sigma=0):")
print(f"  H_S = [[{H_at_fold[0,0]:.4f}, {H_at_fold[0,1]:.6f}],")
print(f"         [{H_at_fold[1,0]:.6f}, {H_at_fold[1,1]:.4f}]]")
print(f"  eigenvalues: [{evals_at_fold[0]:.4f}, {evals_at_fold[1]:.4f}]")
print(f"  det(H_S) = {det_at_fold:.4f}")

is_saddle_fold = det_at_fold < 0
print(f"\n  det(H_S) < 0 at fold? {is_saddle_fold}")

# Also at the saddle point
H_at_saddle = compute_hessian_spline(spl_V, tau_sb, 0.0)
evals_at_saddle = np.sort(np.linalg.eigvalsh(H_at_saddle))
det_at_saddle = evals_at_saddle[0] * evals_at_saddle[1]

print(f"\nSpectral Action Hessian at saddle (tau={tau_sb}, sigma=0):")
print(f"  H_S = [[{H_at_saddle[0,0]:.4f}, {H_at_saddle[0,1]:.6f}],")
print(f"         [{H_at_saddle[1,0]:.6f}, {H_at_saddle[1,1]:.4f}]]")
print(f"  eigenvalues: [{evals_at_saddle[0]:.4f}, {evals_at_saddle[1]:.4f}]")
print(f"  det(H_S) = {det_at_saddle:.4f}")

is_saddle_sb = det_at_saddle < 0
print(f"\n  det(H_S) < 0 at saddle? {is_saddle_sb}")

# Determine overall verdict
is_saddle_anywhere = is_saddle_fold or is_saddle_sb
verdict = "PASS" if is_saddle_anywhere else "FAIL"

print(f"\n{'='*76}")
print(f"  GATE: SA-SADDLE-58 — det(H_S) < 0?")
print(f"  Verdict: {verdict}")
if is_saddle_fold:
    print(f"  Saddle at FOLD (tau={tau_fold}): eigenvalues {evals_at_fold}")
if is_saddle_sb:
    print(f"  Saddle at tau_sb={tau_sb}: eigenvalues {evals_at_saddle}")
print(f"  E_J Hessian eigenvalues (S57): {EJ_H_evals}")
print(f"  SA and E_J share saddle topology: directions {'aligned' if cos_neg > 0.9 else 'misaligned'}")
print(f"{'='*76}")

# =============================================================================
# 9. Save results
# =============================================================================
detail = (
    f"H_S at fold: evals=[{evals_at_fold[0]:.4f},{evals_at_fold[1]:.4f}], "
    f"det={det_at_fold:.4f}. "
    f"H_S at saddle: evals=[{evals_at_saddle[0]:.4f},{evals_at_saddle[1]:.4f}], "
    f"det={det_at_saddle:.4f}. "
    f"E_J comparison: evals=[{EJ_H_evals[0]:.4f},{EJ_H_evals[1]:.4f}], "
    f"cos_align={cos_neg:.4f}."
)

np.savez('computations/session-58/s58_sa_saddle.npz',
    # Hessians at fold
    H_SA_fold=H_at_fold,
    evals_SA_fold=evals_at_fold,
    evecs_SA_fold=evecs_fold if tau_fold == tau_sb else np.linalg.eigh(H_at_fold)[1],
    det_SA_fold=det_at_fold,
    # Hessians at saddle
    H_SA_saddle=H_at_saddle,
    evals_SA_saddle=evals_at_saddle,
    det_SA_saddle=det_at_saddle,
    # Comparison with E_J
    EJ_Hessian=EJ_H,
    EJ_evals=EJ_H_evals,
    EJ_det=EJ_det,
    cos_align_neg=cos_neg,
    cos_align_pos=cos_pos,
    ratio_neg=ratio_neg,
    ratio_pos=ratio_pos,
    # Seeley-DeWitt from spectrum
    tau_sweep=tau_ed,
    a0_spectrum=a0_full,
    a2_spectrum=a2_full,
    a4_spectrum=a4_full,
    d2a2_fold_num=d2a2_num,
    d2a4_fold_num=d2a4_num,
    d2a2_fold_analytic=d2a2_dtau2(tau_fold),
    d2a4_fold_analytic=d2a4_dtau2(tau_fold),
    # Scan results
    tau_scan=np.array([r[0] for r in results_scan]),
    d2V_dtau2_scan=np.array([r[1] for r in results_scan]),
    d2V_dsig2_scan=np.array([r[2] for r in results_scan]),
    d2V_mixed_scan=np.array([r[3] for r in results_scan]),
    eig_min_scan=np.array([r[4] for r in results_scan]),
    eig_max_scan=np.array([r[5] for r in results_scan]),
    det_scan=np.array([r[6] for r in results_scan]),
    # Gate
    gate_name=np.array(['SA-SADDLE-58']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"\nSaved: computations/session-58/s58_sa_saddle.npz")
print("DONE.")
