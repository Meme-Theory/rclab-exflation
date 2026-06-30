#!/usr/bin/env python3
"""
s58_ej_3d_landscape.py — EJ-3D-LANDSCAPE-58: Full U(2)-Invariant E_J Surface
==============================================================================
Gate: EJ-3D-LANDSCAPE-58 (INFO) — Does the saddle persist or is it lifted?

Method:
  1. The U(2)-invariant metric on SU(3) has three parameters (lambda_1, lambda_2, lambda_3)
     on subspaces (u(1) [dim 1], su(2) [dim 3], C^2 [dim 4]).
     Paper 13 (Baptista) eq (5.4).

  2. The Jensen direction tau preserves volume: v_J = (2, -2, 1) in exponent space.
     The T2 direction sigma also preserves volume: v_T2 = (-11, -7, 8).
     The T1 breathing mode delta_1 BREAKS volume: it scales lambda_1 only.

  3. Parametrization in exponent space (xi_1, xi_2, xi_3):
     Jensen:    xi_1 = 2*tau,     xi_2 = -2*tau,     xi_3 = tau
     T2:        xi_1 += -11*sig,  xi_2 += -7*sig,    xi_3 += 8*sig
     T1 breath: xi_1 += delta_1   (only lambda_1 changes)

     So: lambda_1 = exp(2*tau - 11*sig + delta_1)
         lambda_2 = exp(-2*tau - 7*sig)
         lambda_3 = exp(tau + 8*sig)

  4. Volume constraint: Jensen preserves volume (n.v_J = 0 with n = (1,3,4)).
     T2 also preserves volume (n.v_T2 = 0). T1 breathing breaks it:
     n.(1,0,0) = 1 != 0. So delta_1 changes the volume.

  5. Compute E_J(tau, sigma, delta_1) from:
     - V(tau, sigma, delta_1) = spectral action (from scalar curvature + volume)
     - J_C2 from TB Hamiltonian with modified geometry
     - E_J = J_C2^2 * F_anom

  6. Compute 3x3 Hessian at (tau_fold, 0, 0) and diagonalize.

Author: baptista-spacetime-analyst (Session 58)
"""

import sys
sys.path.insert(0, 'computations')
import numpy as np
from numpy import exp, sqrt, log, pi
from numpy.linalg import eigh
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    tau_fold, J_C2 as J_C2_canonical, Vol_SU3_Haar, PI,
    a2_fold, a4_fold, M_KK, N_cells, g0_diag
)

print("=" * 76)
print("  EJ-3D-LANDSCAPE-58: Full U(2)-Invariant E_J 3D Surface")
print("=" * 76)

# =============================================================================
# 1. Load data
# =============================================================================
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
ej_data = np.load('computations/session-57/s57_off_jensen_ej.npz', allow_pickle=True)
oj = np.load('computations/session-54/s54_off_jensen_t2.npz', allow_pickle=True)

tau_tb = tb['tau_values']      # (50,)
J_C2_tb = tb['J_C2_tau']      # (50,)
evals_tb = tb['eigenvalues']   # (50, 32)
bandwidths = tb['bandwidths']  # (50,)

# S57 reference saddle data
EJ_H_2d = ej_data['EJ_B_Hessian_at_saddle']  # (2,2)
EJ_H_evals_2d = ej_data['EJ_B_Hessian_evals']  # [-0.0856, 0.0841]
tau_sb = float(ej_data['V_saddle_tau'])  # 0.2015

# T2 landscape data
V_grid_2d = oj['V_grid']        # (51, 41) spectral action
R_grid_2d = oj['R_grid']        # (51, 41) scalar curvature
tau_oj = oj['tau_range']         # (51,)
sig_oj = oj['sig_range']        # (41,)

print(f"TB data: {len(tau_tb)} tau points in [{tau_tb[0]:.3f}, {tau_tb[-1]:.3f}]")
print(f"S57 2D saddle: tau_sb={tau_sb:.4f}, EJ Hessian evals={EJ_H_evals_2d}")
print(f"Off-Jensen grid: {len(tau_oj)} x {len(sig_oj)}")

# =============================================================================
# 2. Scalar curvature of the general 3-parameter metric
# =============================================================================
# Reuse the R_K_numeric function from s54_off_jensen_t2.py
# This computes R via Milnor's formula using explicit structure constants.

def build_structure_constants():
    """Build structure constants of su(3) in gamma_0-orthonormal basis,
    reordered to (u(1), su(2), C^2)."""
    lam = np.zeros((9, 3, 3), dtype=complex)
    lam[1] = np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex)
    lam[2] = np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex)
    lam[3] = np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex)
    lam[4] = np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex)
    lam[5] = np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex)
    lam[6] = np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex)
    lam[7] = np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex)
    lam[8] = np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex) / sqrt(3.0)

    T = np.zeros((9, 3, 3), dtype=complex)
    for a in range(1, 9):
        T[a] = 1j * lam[a] / 2.0

    reorder = [8, 1, 2, 3, 4, 5, 6, 7]
    f = np.zeros((8, 3, 3), dtype=complex)
    for i in range(8):
        f[i] = T[reorder[i]] * sqrt(2.0)

    c_abc = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            bracket = f[a] @ f[b] - f[b] @ f[a]
            for cc in range(8):
                c_abc[a, b, cc] = -np.trace(bracket @ f[cc]).real

    return c_abc

# Build once
C_ABC = build_structure_constants()

def R_K_from_alphas(a1, a2, a3):
    """Scalar curvature R of (SU(3), hat-g) with metric eigenvalues
    (a1, a2, a3) on (u(1), su(2), C^2) subspaces.
    Uses Milnor's formula with precomputed structure constants."""
    alpha = np.zeros(8)
    alpha[0] = a1
    alpha[1:4] = a2
    alpha[4:8] = a3

    # T1 = sum_{a,b} g([ea,eb],[ea,eb])
    T1 = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            for cc in range(8):
                T1 += C_ABC[a, b, cc]**2 * alpha[cc] / (alpha[a] * alpha[b])

    # T2 = sum_{a,b} g([ea,[ea,eb]], eb)
    T2 = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            gamma_ab = np.zeros(8)
            for cc in range(8):
                gamma_ab[cc] = C_ABC[a, b, cc] * sqrt(alpha[cc]) / (sqrt(alpha[a]) * sqrt(alpha[b]))
            inner = 0.0
            for cc in range(8):
                gamma_ac = np.zeros(8)
                for d in range(8):
                    gamma_ac[d] = C_ABC[a, cc, d] * sqrt(alpha[d]) / (sqrt(alpha[a]) * sqrt(alpha[cc]))
                inner += gamma_ab[cc] * gamma_ac[b]
            T2 += inner

    R = -0.25 * T1 - 0.5 * T2
    return R

# Verify at bi-invariant point
R_bi = R_K_from_alphas(1.0, 1.0, 1.0)
print(f"\nCurvature verification: R(1,1,1) = {R_bi:.6f} (expect 12.0)")

# Verify at fold on Jensen
a1_f = exp(2*tau_fold)
a2_f = exp(-2*tau_fold)
a3_f = exp(tau_fold)
R_fold = R_K_from_alphas(a1_f, a2_f, a3_f)
print(f"R at Jensen fold (tau={tau_fold}): {R_fold:.6f}")
# Compare to analytic: R(tau) = -0.25*exp(-4*tau) + 2*exp(-tau) - 0.25 + 0.5*exp(2*tau)
# But that uses the normalized convention. Our R_K_numeric gives unnormalized.
# Actually, sd20a uses yet another normalization. Let me check what R_K_from_alphas gives.
# For the Jensen metric with alpha=1 base scale:
#   R = (3/2) * (2*e^{2s} - 1 + 8*e^{-s} - e^{-4s})
R_fold_formula = 1.5 * (2*exp(2*tau_fold) - 1 + 8*exp(-tau_fold) - exp(-4*tau_fold))
print(f"R at fold (Paper 15 eq 3.70, alpha=1): {R_fold_formula:.6f}")
print(f"Ratio: {R_fold / R_fold_formula:.10f}")

# =============================================================================
# 3. Spectral action V(tau, sigma, delta_1)
# =============================================================================
# The spectral action in the heat-kernel expansion:
#   S = f_4*Lambda^4 * a_0 + f_2*Lambda^2 * a_2 + f_0 * a_4 + ...
# where:
#   a_0 = (4*pi)^{-4} * dim_spinor * Vol(K)
#   a_2 = (4*pi)^{-4} * dim_spinor * Vol(K) * a_2^red(R)
#   a_4 = (4*pi)^{-4} * dim_spinor * Vol(K) * a_4^red(R, |Ric|^2, |Riem|^2)
#
# Vol(K) = sqrt(a1) * a2^{3/2} * a3^2 * Vol_0
# where Vol_0 = Vol(SU(3), gamma_0) is the base volume.
#
# For the Hessian, we only need the spectral action POTENTIAL:
#   V = spectral action density (intensive, per unit 4D volume)
#   V(a1, a2, a3) = R(a1, a2, a3) * Vol(a1, a2, a3)^{2/8} + ...
# Actually, V_grid from s54 IS the spectral action landscape including
# curvature and volume effects. For the 3D extension, we need to compute
# V from first principles.
#
# STRATEGY: Use V ~ R * sqrt_vol_factor as the dominant contribution.
# The spectral action potential is dominated by the scalar curvature term
# (a_2 ~ R * Vol). We compute:
#   V_eff(tau, sig, d1) = R(a1,a2,a3) * Vol(a1,a2,a3) / Vol_0

def metric_params(tau, sig, d1):
    """Compute (a1, a2, a3) from (tau, sigma, delta_1)."""
    a1 = exp(2*tau - 11*sig + d1)
    a2 = exp(-2*tau - 7*sig)  # (local)
    a3 = exp(tau + 8*sig)
    return a1, a2, a3

def volume_factor(a1, a2, a3):
    """Volume factor: Vol(hat-g) / Vol(gamma_0) = sqrt(a1) * a2^{3/2} * a3^2."""
    return sqrt(a1) * a2**1.5 * a3**2

def V_eff_3d(tau, sig, d1):
    """Spectral action potential V = R * Vol_factor.
    This is the dominant (a_2) contribution to the spectral action."""
    a1, a2, a3 = metric_params(tau, sig, d1)
    R = R_K_from_alphas(a1, a2, a3)
    Vf = volume_factor(a1, a2, a3)
    return R * Vf

# Verify at Jensen fold
V_fold_check = V_eff_3d(tau_fold, 0.0, 0.0)
print(f"\nV_eff at (tau_fold, 0, 0) = {V_fold_check:.6f}")

# =============================================================================
# 4. Construct E_J(tau, sigma, delta_1) on a 3D grid
# =============================================================================
print(f"\n" + "=" * 76)
print("  4. Computing E_J on 3D grid near the fold")
print("=" * 76)

# Grid definition
n_tau = 21
n_sig = 21
n_d1 = 21

tau_center = tau_sb  # Use saddle point as center (near fold)
tau_range_3d = np.linspace(tau_center - 0.05, tau_center + 0.05, n_tau)
sig_range_3d = np.linspace(-0.01, 0.01, n_sig)
d1_range_3d = np.linspace(-0.1, 0.1, n_d1)

# Build J_C2 interpolator (on-Jensen)
J_C2_interp = interp1d(tau_tb, J_C2_tb, kind='cubic', fill_value='extrapolate')

# F_anom interpolator (from TB eigenvalues)
F_anom_Jensen = np.zeros(len(tau_tb))
for i in range(len(tau_tb)):
    ev = evals_tb[i]
    BW = ev.max() - ev.min()
    if BW > 0:
        spacings = np.diff(np.sort(ev))
        F_anom_Jensen[i] = np.mean(spacings**2) / BW**2
    else:
        F_anom_Jensen[i] = 0.0
F_anom_interp = interp1d(tau_tb, F_anom_Jensen, kind='cubic', fill_value='extrapolate')

# Compute V and R on the 3D grid
V_3d = np.zeros((n_tau, n_sig, n_d1))
R_3d = np.zeros((n_tau, n_sig, n_d1))
Vol_3d = np.zeros((n_tau, n_sig, n_d1))

print("Computing R and V on 3D grid...")
for i, tau in enumerate(tau_range_3d):
    for j, sig in enumerate(sig_range_3d):
        for k, d1 in enumerate(d1_range_3d):
            a1, a2, a3 = metric_params(tau, sig, d1)
            R_3d[i, j, k] = R_K_from_alphas(a1, a2, a3)
            Vol_3d[i, j, k] = volume_factor(a1, a2, a3)
            V_3d[i, j, k] = R_3d[i, j, k] * Vol_3d[i, j, k]
    if (i+1) % 5 == 0:
        print(f"  tau {i+1}/{n_tau} done")

# Compute E_J on the 3D grid
# E_J(tau, sig, d1) = J_C2^2(tau, sig, d1) * F_anom(tau, sig, d1)
# Off-Jensen J_C2: use Approach B (spectral density scaling)
#   J_C2(tau, sig, d1) = J_C2(tau, 0, 0) * (|V(tau, sig, d1)| / |V(tau, 0, 0)|)^{1/4}
# Off-Jensen F_anom: modulated by curvature
#   F_anom(tau, sig, d1) = F_anom(tau, 0, 0) * R(tau, sig, d1) / R(tau, 0, 0)

E_J_3d = np.zeros((n_tau, n_sig, n_d1))
J_C2_3d = np.zeros((n_tau, n_sig, n_d1))
F_anom_3d = np.zeros((n_tau, n_sig, n_d1))

for i, tau in enumerate(tau_range_3d):
    J0 = J_C2_interp(tau)
    F0 = F_anom_interp(tau)
    V0 = V_3d[i, n_sig//2, n_d1//2]  # (tau, 0, 0) -- center of sig and d1
    R0 = R_3d[i, n_sig//2, n_d1//2]

    for j, sig in enumerate(sig_range_3d):
        for k, d1 in enumerate(d1_range_3d):
            V_ijk = V_3d[i, j, k]
            R_ijk = R_3d[i, j, k]

            # J from spectral density
            if abs(V0) > 1e-10 and abs(V_ijk) > 1e-10:
                J_C2_3d[i, j, k] = J0 * (abs(V_ijk) / abs(V0))**0.25
            else:
                J_C2_3d[i, j, k] = J0

            # F_anom modulated by curvature
            if abs(R0) > 1e-10:
                F_anom_3d[i, j, k] = F0 * (R_ijk / R0)
            else:
                F_anom_3d[i, j, k] = F0

            E_J_3d[i, j, k] = J_C2_3d[i, j, k]**2 * F_anom_3d[i, j, k]

print(f"\nE_J 3D grid shape: {E_J_3d.shape}")
print(f"E_J range: [{E_J_3d.min():.6e}, {E_J_3d.max():.6e}]")

# =============================================================================
# 5. Compute 3x3 Hessian at the center point
# =============================================================================
print(f"\n" + "=" * 76)
print("  5. 3x3 Hessian of E_J at saddle center")
print("=" * 76)

# Central point indices
ic = n_tau // 2
jc = n_sig // 2
kc = n_d1 // 2

print(f"Center: tau={tau_range_3d[ic]:.4f}, sig={sig_range_3d[jc]:.4f}, d1={d1_range_3d[kc]:.4f}")
print(f"E_J at center: {E_J_3d[ic, jc, kc]:.8e}")

dtau_3d = tau_range_3d[1] - tau_range_3d[0]
dsig_3d = sig_range_3d[1] - sig_range_3d[0]
dd1_3d = d1_range_3d[1] - d1_range_3d[0]

print(f"Grid steps: dtau={dtau_3d:.6f}, dsig={dsig_3d:.6f}, dd1={dd1_3d:.6f}")

# Second derivatives via centered finite differences
E = E_J_3d  # (local)

# Diagonal elements
d2E_dtau2 = (E[ic+1, jc, kc] - 2*E[ic, jc, kc] + E[ic-1, jc, kc]) / dtau_3d**2
d2E_dsig2 = (E[ic, jc+1, kc] - 2*E[ic, jc, kc] + E[ic, jc-1, kc]) / dsig_3d**2
d2E_dd12 = (E[ic, jc, kc+1] - 2*E[ic, jc, kc] + E[ic, jc, kc-1]) / dd1_3d**2

# Off-diagonal elements
d2E_dtau_dsig = (E[ic+1, jc+1, kc] - E[ic+1, jc-1, kc]
                  - E[ic-1, jc+1, kc] + E[ic-1, jc-1, kc]) / (4*dtau_3d*dsig_3d)
d2E_dtau_dd1 = (E[ic+1, jc, kc+1] - E[ic+1, jc, kc-1]
                 - E[ic-1, jc, kc+1] + E[ic-1, jc, kc-1]) / (4*dtau_3d*dd1_3d)
d2E_dsig_dd1 = (E[ic, jc+1, kc+1] - E[ic, jc+1, kc-1]
                 - E[ic, jc-1, kc+1] + E[ic, jc-1, kc-1]) / (4*dsig_3d*dd1_3d)

H_3d = np.array([
    [d2E_dtau2,     d2E_dtau_dsig, d2E_dtau_dd1],
    [d2E_dtau_dsig, d2E_dsig2,     d2E_dsig_dd1],
    [d2E_dtau_dd1,  d2E_dsig_dd1,  d2E_dd12]
])

print(f"\n3x3 Hessian H_EJ at center:")
print(f"  [[{H_3d[0,0]:.6e}, {H_3d[0,1]:.6e}, {H_3d[0,2]:.6e}],")
print(f"   [{H_3d[1,0]:.6e}, {H_3d[1,1]:.6e}, {H_3d[1,2]:.6e}],")
print(f"   [{H_3d[2,0]:.6e}, {H_3d[2,1]:.6e}, {H_3d[2,2]:.6e}]]")

evals_3d, evecs_3d = eigh(H_3d)
print(f"\n  Eigenvalues: {evals_3d}")
print(f"  Eigenvectors:")
for i_ev in range(3):
    print(f"    e_{i_ev}: {evecs_3d[:, i_ev]}  (eval = {evals_3d[i_ev]:.6e})")

n_negative = np.sum(evals_3d < 0)
n_positive = np.sum(evals_3d > 0)
n_zero = np.sum(np.abs(evals_3d) < 1e-10 * max(abs(evals_3d)))

det_3d = np.prod(evals_3d)
print(f"\n  det(H_3d) = {det_3d:.6e}")
print(f"  Signature: ({n_positive}+, {n_negative}-) (Morse index = {n_negative})")

# =============================================================================
# 6. Robustness: multiple step sizes for finite differences
# =============================================================================
print(f"\n" + "=" * 76)
print("  6. Robustness check: multiple finite difference stencils")
print("=" * 76)

# Recompute using different grid positions (wider stencils)
for stride in [1, 2, 3]:
    if ic + stride >= n_tau or ic - stride < 0:
        continue
    if jc + stride >= n_sig or jc - stride < 0:
        continue
    if kc + stride >= n_d1 or kc - stride < 0:
        continue

    h_tau = stride * dtau_3d
    h_sig = stride * dsig_3d
    h_d1 = stride * dd1_3d

    d2_tt = (E[ic+stride, jc, kc] - 2*E[ic, jc, kc] + E[ic-stride, jc, kc]) / h_tau**2
    d2_ss = (E[ic, jc+stride, kc] - 2*E[ic, jc, kc] + E[ic, jc-stride, kc]) / h_sig**2
    d2_dd = (E[ic, jc, kc+stride] - 2*E[ic, jc, kc] + E[ic, jc, kc-stride]) / h_d1**2

    d2_ts = (E[ic+stride, jc+stride, kc] - E[ic+stride, jc-stride, kc]
             - E[ic-stride, jc+stride, kc] + E[ic-stride, jc-stride, kc]) / (4*h_tau*h_sig)
    d2_td = (E[ic+stride, jc, kc+stride] - E[ic+stride, jc, kc-stride]
             - E[ic-stride, jc, kc+stride] + E[ic-stride, jc, kc-stride]) / (4*h_tau*h_d1)
    d2_sd = (E[ic, jc+stride, kc+stride] - E[ic, jc+stride, kc-stride]
             - E[ic, jc-stride, kc+stride] + E[ic, jc-stride, kc-stride]) / (4*h_sig*h_d1)

    H_s = np.array([[d2_tt, d2_ts, d2_td],
                     [d2_ts, d2_ss, d2_sd],
                     [d2_td, d2_sd, d2_dd]])
    evals_s = np.sort(np.linalg.eigvalsh(H_s))
    print(f"  stride={stride} (h_tau={h_tau:.5f}, h_sig={h_sig:.5f}, h_d1={h_d1:.5f}):")
    print(f"    evals = {evals_s}")
    print(f"    n_neg = {np.sum(evals_s < 0)}")

# =============================================================================
# 7. Also compute the 3x3 Hessian of V_eff (spectral action) for comparison
# =============================================================================
print(f"\n" + "=" * 76)
print("  7. Spectral action V Hessian (3D) for comparison")
print("=" * 76)

V = V_3d

d2V_dtau2 = (V[ic+1, jc, kc] - 2*V[ic, jc, kc] + V[ic-1, jc, kc]) / dtau_3d**2
d2V_dsig2 = (V[ic, jc+1, kc] - 2*V[ic, jc, kc] + V[ic, jc-1, kc]) / dsig_3d**2
d2V_dd12 = (V[ic, jc, kc+1] - 2*V[ic, jc, kc] + V[ic, jc, kc-1]) / dd1_3d**2

d2V_dtau_dsig = (V[ic+1, jc+1, kc] - V[ic+1, jc-1, kc]
                  - V[ic-1, jc+1, kc] + V[ic-1, jc-1, kc]) / (4*dtau_3d*dsig_3d)
d2V_dtau_dd1 = (V[ic+1, jc, kc+1] - V[ic+1, jc, kc-1]
                 - V[ic-1, jc, kc+1] + V[ic-1, jc, kc-1]) / (4*dtau_3d*dd1_3d)
d2V_dsig_dd1 = (V[ic, jc+1, kc+1] - V[ic, jc+1, kc-1]
                 - V[ic, jc-1, kc+1] + V[ic, jc-1, kc-1]) / (4*dsig_3d*dd1_3d)

H_V_3d = np.array([
    [d2V_dtau2,     d2V_dtau_dsig, d2V_dtau_dd1],
    [d2V_dtau_dsig, d2V_dsig2,     d2V_dsig_dd1],
    [d2V_dtau_dd1,  d2V_dsig_dd1,  d2V_dd12]
])

print(f"3x3 V Hessian at center:")
print(f"  [[{H_V_3d[0,0]:.4f}, {H_V_3d[0,1]:.4f}, {H_V_3d[0,2]:.4f}],")
print(f"   [{H_V_3d[1,0]:.4f}, {H_V_3d[1,1]:.4f}, {H_V_3d[1,2]:.4f}],")
print(f"   [{H_V_3d[2,0]:.4f}, {H_V_3d[2,1]:.4f}, {H_V_3d[2,2]:.4f}]]")

evals_V_3d, evecs_V_3d = eigh(H_V_3d)
print(f"\n  V Hessian eigenvalues: {evals_V_3d}")
n_neg_V = np.sum(evals_V_3d < 0)
print(f"  Signature: ({np.sum(evals_V_3d > 0)}+, {n_neg_V}-)")

# =============================================================================
# 8. Check: 2x2 sub-block vs S57 result
# =============================================================================
print(f"\n" + "=" * 76)
print("  8. Consistency check: 2x2 (tau, sigma) sub-block vs S57")
print("=" * 76)

H_2d_subblock = H_3d[:2, :2]
evals_2d_sub = np.sort(np.linalg.eigvalsh(H_2d_subblock))
print(f"  E_J 2x2 sub-block (tau, sigma) eigenvalues: {evals_2d_sub}")
print(f"  S57 2x2 E_J Hessian eigenvalues: {EJ_H_evals_2d}")
print(f"  Ratio sub/S57: {evals_2d_sub / EJ_H_evals_2d}")

# The delta_1 direction
print(f"\n  delta_1 diagonal element: d^2 E_J / d(delta_1)^2 = {H_3d[2,2]:.6e}")
print(f"  tau-delta_1 coupling: {H_3d[0,2]:.6e}")
print(f"  sigma-delta_1 coupling: {H_3d[1,2]:.6e}")

# =============================================================================
# 9. GATE VERDICT
# =============================================================================
print(f"\n" + "=" * 76)
print("  9. GATE: EJ-3D-LANDSCAPE-58")
print("=" * 76)

saddle_persists = n_negative > 0
if n_negative == 1:
    verdict_desc = "SADDLE persists (Morse index 1)"
elif n_negative == 2:
    verdict_desc = "SADDLE persists (Morse index 2 — stronger instability)"
elif n_negative == 0:
    verdict_desc = "LIFTED — no negative eigenvalues (minimum or flat)"
else:
    verdict_desc = f"Morse index {n_negative}"

print(f"\n  3D Hessian eigenvalues: {evals_3d}")
print(f"  Morse index (negative eigenvalues): {n_negative}")
print(f"  Verdict: {verdict_desc}")
print(f"\n  S57 2D saddle eigenvalues for reference: {EJ_H_evals_2d}")
print(f"  Third direction (delta_1): eigenvalue = {evals_3d[2] if n_negative < 3 else evals_3d[0]:.6e}")
print(f"\n  Physical interpretation:")
if saddle_persists:
    neg_idx = np.argmin(evals_3d)
    neg_evec = evecs_3d[:, neg_idx]
    print(f"    Unstable direction: ({neg_evec[0]:.4f})*tau + ({neg_evec[1]:.4f})*sigma + ({neg_evec[2]:.4f})*delta_1")
    print(f"    The T1 breathing mode does NOT lift the saddle.")
    print(f"    Transit along the negative eigenvector remains possible.")
else:
    print(f"    The T1 breathing mode LIFTS the saddle to a minimum or maximum.")
    print(f"    The 2D instability was an artifact of missing delta_1.")

# =============================================================================
# 10. Plotting
# =============================================================================
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('EJ-3D-LANDSCAPE-58: E_J(tau, sigma, delta_1) near the fold', fontsize=14)

# Plot 1: E_J in (tau, sigma) plane at delta_1 = 0
ax = axes[0, 0]
extent = [sig_range_3d[0], sig_range_3d[-1], tau_range_3d[0], tau_range_3d[-1]]
im = ax.imshow(E_J_3d[:, :, n_d1//2], origin='lower', aspect='auto',
               extent=extent, cmap='RdBu_r')
plt.colorbar(im, ax=ax, label='E_J')
ax.set_xlabel('sigma')
ax.set_ylabel('tau')
ax.set_title('E_J(tau, sigma, d1=0)')
ax.axhline(tau_center, color='k', ls=':', alpha=0.5)
ax.axvline(0, color='k', ls=':', alpha=0.5)

# Plot 2: E_J in (tau, delta_1) plane at sigma = 0
ax = axes[0, 1]
extent = [d1_range_3d[0], d1_range_3d[-1], tau_range_3d[0], tau_range_3d[-1]]
im = ax.imshow(E_J_3d[:, n_sig//2, :], origin='lower', aspect='auto',
               extent=extent, cmap='RdBu_r')
plt.colorbar(im, ax=ax, label='E_J')
ax.set_xlabel('delta_1')
ax.set_ylabel('tau')
ax.set_title('E_J(tau, sig=0, d1)')
ax.axhline(tau_center, color='k', ls=':', alpha=0.5)
ax.axvline(0, color='k', ls=':', alpha=0.5)

# Plot 3: E_J in (sigma, delta_1) plane at tau = center
ax = axes[0, 2]
extent = [d1_range_3d[0], d1_range_3d[-1], sig_range_3d[0], sig_range_3d[-1]]
im = ax.imshow(E_J_3d[n_tau//2, :, :], origin='lower', aspect='auto',
               extent=extent, cmap='RdBu_r')
plt.colorbar(im, ax=ax, label='E_J')
ax.set_xlabel('delta_1')
ax.set_ylabel('sigma')
ax.set_title(f'E_J(tau={tau_center:.3f}, sig, d1)')
ax.axhline(0, color='k', ls=':', alpha=0.5)
ax.axvline(0, color='k', ls=':', alpha=0.5)

# Plot 4: V (spectral action) in (tau, sigma) plane at delta_1 = 0
ax = axes[1, 0]
extent = [sig_range_3d[0], sig_range_3d[-1], tau_range_3d[0], tau_range_3d[-1]]
im = ax.imshow(V_3d[:, :, n_d1//2], origin='lower', aspect='auto',
               extent=extent, cmap='viridis')
plt.colorbar(im, ax=ax, label='V')
ax.set_xlabel('sigma')
ax.set_ylabel('tau')
ax.set_title('V(tau, sigma, d1=0)')

# Plot 5: Eigenvalue evolution along delta_1 at (tau_center, 0)
ax = axes[1, 1]
evals_vs_d1 = []
for k in range(n_d1):
    if ic+1 < n_tau and ic-1 >= 0 and jc+1 < n_sig and jc-1 >= 0 and k+1 < n_d1 and k-1 >= 0:
        h_t = dtau_3d
        h_s = dsig_3d
        h_d = dd1_3d
        d2tt = (E[ic+1,jc,k] - 2*E[ic,jc,k] + E[ic-1,jc,k]) / h_t**2
        d2ss = (E[ic,jc+1,k] - 2*E[ic,jc,k] + E[ic,jc-1,k]) / h_s**2
        d2dd = (E[ic,jc,k+1] - 2*E[ic,jc,k] + E[ic,jc,k-1]) / h_d**2
        d2ts = (E[ic+1,jc+1,k] - E[ic+1,jc-1,k] - E[ic-1,jc+1,k] + E[ic-1,jc-1,k]) / (4*h_t*h_s)
        d2td = (E[ic+1,jc,k+1] - E[ic+1,jc,k-1] - E[ic-1,jc,k+1] + E[ic-1,jc,k-1]) / (4*h_t*h_d)
        d2sd = (E[ic,jc+1,k+1] - E[ic,jc+1,k-1] - E[ic,jc-1,k+1] + E[ic,jc-1,k-1]) / (4*h_s*h_d)
        H_k = np.array([[d2tt, d2ts, d2td], [d2ts, d2ss, d2sd], [d2td, d2sd, d2dd]])
        ev_k = np.sort(np.linalg.eigvalsh(H_k))
        evals_vs_d1.append((d1_range_3d[k], ev_k))

d1_plot = [x[0] for x in evals_vs_d1]
ev0_plot = [x[1][0] for x in evals_vs_d1]
ev1_plot = [x[1][1] for x in evals_vs_d1]
ev2_plot = [x[1][2] for x in evals_vs_d1]

ax.plot(d1_plot, ev0_plot, 'r-', label='eval 0 (min)')
ax.plot(d1_plot, ev1_plot, 'b-', label='eval 1')
ax.plot(d1_plot, ev2_plot, 'g-', label='eval 2 (max)')
ax.axhline(0, color='k', ls=':', alpha=0.5)
ax.axvline(0, color='k', ls=':', alpha=0.5)
ax.set_xlabel('delta_1')
ax.set_ylabel('Hessian eigenvalue')
ax.set_title('Hessian eigenvalues vs delta_1')
ax.legend(fontsize=8)

# Plot 6: 1D slice along the negative eigenvector
ax = axes[1, 2]
neg_dir = evecs_3d[:, np.argmin(evals_3d)]
t_line = np.linspace(-0.05, 0.05, 101)
EJ_line = np.zeros_like(t_line)
for l, t in enumerate(t_line):
    tau_l = tau_center + t * neg_dir[0]
    sig_l = 0.0 + t * neg_dir[1]
    d1_l = 0.0 + t * neg_dir[2]
    a1, a2, a3 = metric_params(tau_l, sig_l, d1_l)
    if a1 > 0 and a2 > 0 and a3 > 0:
        R_l = R_K_from_alphas(a1, a2, a3)
        Vf_l = volume_factor(a1, a2, a3)
        V_l = R_l * Vf_l
        J_l = J_C2_interp(tau_l) * (abs(V_l) / max(abs(V_fold_check), 1e-10))**0.25
        F_l = F_anom_interp(tau_l) * R_l / max(R_fold, 1e-10)
        EJ_line[l] = J_l**2 * F_l
    else:
        EJ_line[l] = np.nan

ax.plot(t_line, EJ_line, 'k-', lw=2)
ax.axvline(0, color='r', ls=':', alpha=0.5, label='center')
ax.set_xlabel('t (along negative eigvec)')
ax.set_ylabel('E_J')
ax.set_title(f'E_J along negative direction\n(Morse index {n_negative})')
ax.legend()

plt.tight_layout()
plt.savefig('computations/session-58/s58_ej_3d_landscape.png', dpi=150, bbox_inches='tight')
print(f"\nPlot saved: computations/session-58/s58_ej_3d_landscape.png")

# =============================================================================
# 11. Save results
# =============================================================================
gate_verdict = "PASS" if saddle_persists else "FAIL"
detail = (
    f"3D Hessian evals=[{evals_3d[0]:.4e},{evals_3d[1]:.4e},{evals_3d[2]:.4e}], "
    f"Morse_idx={n_negative}. "
    f"2D sub-block evals=[{evals_2d_sub[0]:.4e},{evals_2d_sub[1]:.4e}]. "
    f"S57 2D ref: [{EJ_H_evals_2d[0]:.4e},{EJ_H_evals_2d[1]:.4e}]. "
    f"delta_1 direction: d2E/dd1^2={H_3d[2,2]:.4e}. "
    f"{verdict_desc}."
)

np.savez('computations/session-58/s58_ej_3d_landscape.npz',
    # Grid
    tau_range=tau_range_3d,
    sig_range=sig_range_3d,
    d1_range=d1_range_3d,
    # 3D fields
    E_J_3d=E_J_3d,
    V_3d=V_3d,
    R_3d=R_3d,
    Vol_3d=Vol_3d,
    J_C2_3d=J_C2_3d,
    F_anom_3d=F_anom_3d,
    # Hessians
    H_EJ_3d=H_3d,
    evals_EJ_3d=evals_3d,
    evecs_EJ_3d=evecs_3d,
    H_V_3d=H_V_3d,
    evals_V_3d=evals_V_3d,
    # 2D sub-block
    H_EJ_2d_sub=H_2d_subblock,
    evals_EJ_2d_sub=evals_2d_sub,
    # Reference
    EJ_H_2d_S57=EJ_H_2d,
    EJ_evals_2d_S57=EJ_H_evals_2d,
    # Morse index
    morse_index=np.array([n_negative]),
    # Gate
    gate_name=np.array(['EJ-3D-LANDSCAPE-58']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([detail]),
)

print(f"\nSaved: computations/session-58/s58_ej_3d_landscape.npz")
print(f"\nGATE: EJ-3D-LANDSCAPE-58 — Saddle persist or lifted?")
print(f"Verdict: {gate_verdict} — {verdict_desc}")
print("DONE.")
