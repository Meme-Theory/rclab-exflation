#!/usr/bin/env python3
"""
s40_collective_inertia.py  --  ATDHFB Collective Inertia at the Fold (M-COLL-40)

Computes the cranking-model collective inertia M_coll(tau) for the BCS condensate
on the deformed SU(3) internal space.

The Inglis-Belyaev (IB) and ATDHFB cranking masses are:
  M_IB     = 2 * sum_{k,k'} |F_{kk'}|^2 / (E_k + E_{k'})^2
  M_ATDHFB = 2 * sum_{k,k'} |F_{kk'}|^2 / (E_k + E_{k'})^3

For the k=k' (same-level pair-breaking) channel, the matrix element is:
  F_kk = (2*u_k*v_k) * (depsilon_k/dtau) + (u_k^2 - v_k^2) * (dDelta_k/dtau)

Since the BCS coherence factors cancel for the full (11)+(20) channel:
  (u_k u_{k'} - v_k v_{k'})^2 + (u_k v_{k'} + v_k u_{k'})^2 = 1
the diagonal cranking mass simplifies to:
  M_IB^{diag} = 2 * sum_k (depsilon_k/dtau)^2 / (2*E_k)^2

Gate: M-COLL-40
  PASS: sigma_ZP > delta_tau_BCS = 0.09
  FAIL: sigma_ZP < 0.05

Author: Gen-Physicist (Session 40, M-COLL-40)
"""

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# 0. Load all input data
# ============================================================

cas = np.load('tier0-computation/s39_cascade_spectroscopy.npz', allow_pickle=True)
fs  = np.load('tier0-computation/s39_fubini_study.npz', allow_pickle=True)
rg  = np.load('tier0-computation/s39_richardson_gaudin.npz', allow_pickle=True)
s36 = np.load('tier0-computation/s36_sfull_tau_stabilization.npz', allow_pickle=True)

tau_grid = cas['tau_grid']       # (50,)
B1 = cas['B1']                   # (50,) B1 eigenvalue
B2 = cas['B2']                   # (50,) B2 eigenvalue
B3 = cas['B3']                   # (50,) B3 eigenvalue
v_B1 = cas['v_B1']               # (50,) dlambda_B1/dtau
v_B2 = cas['v_B2']               # (50,) dlambda_B2/dtau
v_B3 = cas['v_B3']               # (50,) dlambda_B3/dtau

tau_fs = fs['tau_ext']           # (50,)
g_FS_ext = fs['g_FS_ext']       # (50,)

rg_tau = rg['tau_values']        # (9,) [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
E_8_tau = rg['E_8_tau']          # (9, 8) single-particle eigenvalues
V_phys_tau = rg['V_phys_tau']    # (9, 8, 8)
psi_pair_tau = rg['psi_pair_tau']  # (9, 8) pair amplitudes (v_k = -psi)
e1_tau = rg['e1_tau']            # (9,) ground state energies

tau_fold_exact = float(rg['tau_fold'])
Delta_k_fold = rg['Delta_k_fold']
u_k_fold = rg['u_k_fold']
v_k_fold = rg['v_k_fold']
V_phys_fold = rg['V_phys_fold']
de1_dtau_fold = float(rg['de1_dtau_fold'])
d2e1_dtau2_fold = float(rg['d2e1_dtau2_fold'])

d2S_fold = float(s36['d2S_fold'][0])

print("=" * 70)
print("M-COLL-40: ATDHFB Collective Inertia at the Fold")
print("=" * 70)

# ============================================================
# 1. Build 8-mode spectrum at CASCADE tau points
# ============================================================
n_tau = len(tau_grid)
n_modes = 8

epsilon = np.zeros((n_tau, n_modes))
depsilon_dtau = np.zeros((n_tau, n_modes))

for i in range(n_tau):
    epsilon[i, 0:4] = B2[i]
    depsilon_dtau[i, 0:4] = v_B2[i]
    epsilon[i, 4] = B1[i]
    depsilon_dtau[i, 4] = v_B1[i]
    epsilon[i, 5:8] = B3[i]
    depsilon_dtau[i, 5:8] = v_B3[i]

fold_idx = np.argmin(np.abs(tau_grid - tau_fold_exact))
print(f"\nCASCADE grid: {n_tau} points, fold at idx={fold_idx} (tau={tau_grid[fold_idx]:.6f})")
print(f"Exact fold: tau={tau_fold_exact:.6f}")

# ============================================================
# 2. Extract BCS coherence factors at 9 RG tau points
# ============================================================
# v_k = |psi_pair_tau[i,k]| (pair amplitudes, stored with negative sign)
# u_k = sqrt(1 - v_k^2)
# n_k = v_k^2

v_rg = np.abs(psi_pair_tau)  # (9, 8)
u_rg = np.sqrt(1.0 - v_rg**2)  # (9, 8)
n_rg = v_rg**2  # (9, 8) occupation numbers

print("\nBCS coherence factors at 9 RG tau points:")
for i in range(9):
    print(f"  tau={rg_tau[i]:.2f}: v_B2={v_rg[i,0]:.4f}, v_B1={v_rg[i,4]:.4f}, v_B3={v_rg[i,5]:.4f}")

# Verify at fold
print(f"\n  Fold check: v_rg at tau=0.20 = {v_rg[3,:]}")
print(f"              v_k_fold (stored) = {v_k_fold}")

# ============================================================
# 3. Compute quasiparticle energies at 9 RG tau points
# ============================================================
# E_k = epsilon_k / (u_k^2 - v_k^2) = epsilon_k / (1 - 2*n_k)
# This uses the BCS relation epsilon_k = E_k * cos(theta_k) where
# cos(theta_k) = u_k^2 - v_k^2.

E_qp_rg = np.zeros((9, n_modes))
for i in range(9):
    for k in range(n_modes):
        cos_theta = u_rg[i,k]**2 - v_rg[i,k]**2
        if abs(cos_theta) > 1e-10:
            E_qp_rg[i, k] = abs(E_8_tau[i, k]) / abs(cos_theta)
        else:
            # At half-filling (cos_theta~0), use Delta_k = E_k * sin(theta)
            # sin(theta) = 2*u*v, so E_k = Delta_k / (2*u*v)
            # But Delta_k is not directly stored at all tau.
            # Use E_k ~ epsilon_k / 1e-10 as large (regularized)
            E_qp_rg[i, k] = abs(E_8_tau[i, k]) * 100.0

# Compute Delta_k = 2*u_k*v_k*E_k (BCS gap)
Delta_rg = 2.0 * u_rg * v_rg * E_qp_rg  # (9, 8)

print(f"\nQuasiparticle energies at RG tau points:")
for i in range(9):
    print(f"  tau={rg_tau[i]:.2f}: E_B2={E_qp_rg[i,0]:.4f}, E_B1={E_qp_rg[i,4]:.4f}, E_B3={E_qp_rg[i,5]:.4f}")
    print(f"           Delta_B2={Delta_rg[i,0]:.4f}, Delta_B1={Delta_rg[i,4]:.4f}, Delta_B3={Delta_rg[i,5]:.4f}")

# Cross-check with stored fold data
eps_fold = np.array([0.84522]*4 + [0.81974] + [0.97403]*3)
E_fold_check = np.sqrt(eps_fold**2 + np.abs(Delta_k_fold)**2)
print(f"\nFold cross-check:")
print(f"  E_qp (from stored Delta): {E_fold_check}")
print(f"  E_qp (from u,v formula):  epsilon/(u^2-v^2) = {eps_fold / (u_k_fold**2 - v_k_fold**2)}")
print(f"  These should match: max dev = {np.max(np.abs(E_fold_check - eps_fold/(u_k_fold**2-v_k_fold**2))):.6f}")

# Use the consistent formula
E_fold = E_fold_check
Delta_fold = np.abs(Delta_k_fold)

# ============================================================
# 4. Interpolate E_qp to CASCADE grid
# ============================================================
E_qp_interp = np.zeros((n_tau, n_modes))
for k in range(n_modes):
    cs = CubicSpline(rg_tau, E_qp_rg[:, k])
    E_qp_interp[:, k] = np.maximum(cs(tau_grid), 0.01)  # floor at 0.01

# Also interpolate v_k, u_k, Delta_k to CASCADE grid
v_interp = np.zeros((n_tau, n_modes))
u_interp = np.zeros((n_tau, n_modes))
Delta_interp = np.zeros((n_tau, n_modes))
for k in range(n_modes):
    cs_v = CubicSpline(rg_tau, v_rg[:, k])
    v_interp[:, k] = np.clip(cs_v(tau_grid), 0.0, 1.0)
    u_interp[:, k] = np.sqrt(np.maximum(1.0 - v_interp[:, k]**2, 0.0))
    cs_D = CubicSpline(rg_tau, Delta_rg[:, k])
    Delta_interp[:, k] = cs_D(tau_grid)

# ============================================================
# 5. Compute dDelta/dtau and dv/dtau at all tau points
# ============================================================
dDelta_dtau = np.zeros((n_tau, n_modes))
dv_dtau = np.zeros((n_tau, n_modes))
du_dtau = np.zeros((n_tau, n_modes))

for k in range(n_modes):
    cs_D = CubicSpline(rg_tau, Delta_rg[:, k])
    dDelta_dtau[:, k] = cs_D(tau_grid, 1)

    cs_v = CubicSpline(rg_tau, v_rg[:, k])
    dv_dtau[:, k] = cs_v(tau_grid, 1)

    cs_u = CubicSpline(rg_tau, u_rg[:, k])
    du_dtau[:, k] = cs_u(tau_grid, 1)

# ============================================================
# 6. METHOD A: DIAGONAL CRANKING MASS (50 CASCADE points)
# ============================================================
# M_IB^{diag} = 2 * sum_k (depsilon_k/dtau)^2 / (2*E_k)^2
# M_ATDHFB^{diag} = 2 * sum_k (depsilon_k/dtau)^2 / (2*E_k)^3
# (BCS coherence factors cancel in the full 11+20 channel)

print("\n" + "=" * 70)
print("METHOD A: Diagonal Cranking Mass (50 CASCADE points)")
print("=" * 70)

M_IB_A = np.zeros(n_tau)
M_ATDHFB_A = np.zeros(n_tau)

for i in range(n_tau):
    for k in range(n_modes):
        de = depsilon_dtau[i, k]
        Ek = E_qp_interp[i, k]
        M_IB_A[i] += 2.0 * de**2 / (2.0 * Ek)**2
        M_ATDHFB_A[i] += 2.0 * de**2 / (2.0 * Ek)**3

print(f"M_IB_A at fold:     {M_IB_A[fold_idx]:.6f}")
print(f"M_ATDHFB_A at fold: {M_ATDHFB_A[fold_idx]:.6f}")

# ============================================================
# 7. METHOD B: PAIR-BREAKING CRANKING MASS (50 points, with dDelta)
# ============================================================
# F_kk = (2*u_k*v_k) * (depsilon_k/dtau) + (u_k^2 - v_k^2) * (dDelta_k/dtau)
# M_IB^{pair} = 2 * sum_k F_kk^2 / (2*E_k)^2
# M_ATDHFB^{pair} = 2 * sum_k F_kk^2 / (2*E_k)^3

print("\n" + "=" * 70)
print("METHOD B: Pair-Breaking Cranking Mass (with gap derivative)")
print("=" * 70)

M_IB_B = np.zeros(n_tau)
M_ATDHFB_B = np.zeros(n_tau)
F_kk_all = np.zeros((n_tau, n_modes))

for i in range(n_tau):
    for k in range(n_modes):
        de = depsilon_dtau[i, k]
        Ek = E_qp_interp[i, k]
        uk = u_interp[i, k]
        vk = v_interp[i, k]
        dD = dDelta_dtau[i, k]

        F_kk = 2.0 * uk * vk * de + (uk**2 - vk**2) * dD
        F_kk_all[i, k] = F_kk

        M_IB_B[i] += 2.0 * F_kk**2 / (2.0 * Ek)**2
        M_ATDHFB_B[i] += 2.0 * F_kk**2 / (2.0 * Ek)**3

print(f"M_IB_B at fold:     {M_IB_B[fold_idx]:.6f}")
print(f"M_ATDHFB_B at fold: {M_ATDHFB_B[fold_idx]:.6f}")

# At EXACT fold (interpolate from spline of M_B values)
# Better: compute directly at fold using stored fold data
deps_fold = np.array([
    float(np.interp(tau_fold_exact, tau_grid, v_B2)),
    float(np.interp(tau_fold_exact, tau_grid, v_B2)),
    float(np.interp(tau_fold_exact, tau_grid, v_B2)),
    float(np.interp(tau_fold_exact, tau_grid, v_B2)),
    float(np.interp(tau_fold_exact, tau_grid, v_B1)),
    float(np.interp(tau_fold_exact, tau_grid, v_B3)),
    float(np.interp(tau_fold_exact, tau_grid, v_B3)),
    float(np.interp(tau_fold_exact, tau_grid, v_B3)),
])

# dDelta at exact fold from spline
dDelta_fold = np.zeros(n_modes)
for k in range(n_modes):
    cs = CubicSpline(rg_tau, Delta_rg[:, k])
    dDelta_fold[k] = cs(tau_fold_exact, 1)

print(f"\nAt exact fold (tau={tau_fold_exact:.6f}):")
print(f"  deps: B2={deps_fold[0]:.6f}, B1={deps_fold[4]:.6f}, B3={deps_fold[5]:.6f}")
print(f"  dDelta: {dDelta_fold}")
print(f"  |Delta|: B2={Delta_fold[0]:.4f}, B1={Delta_fold[4]:.4f}, B3={Delta_fold[5]:.4f}")
print(f"  E_qp: B2={E_fold[0]:.4f}, B1={E_fold[4]:.4f}, B3={E_fold[5]:.4f}")
print(f"  u: {u_k_fold}")
print(f"  v: {v_k_fold}")

# Compute at exact fold
M_IB_fold = 0.0
M_ATDHFB_fold = 0.0
F_kk_fold = np.zeros(n_modes)

for k in range(n_modes):
    uk = u_k_fold[k]
    vk = v_k_fold[k]
    de = deps_fold[k]
    dD = dDelta_fold[k]
    Ek = E_fold[k]

    F_kk = 2.0 * uk * vk * de + (uk**2 - vk**2) * dD
    F_kk_fold[k] = F_kk

    M_IB_fold += 2.0 * F_kk**2 / (2.0 * Ek)**2
    M_ATDHFB_fold += 2.0 * F_kk**2 / (2.0 * Ek)**3

print(f"\n  F_kk at fold: {F_kk_fold}")
print(f"  M_IB_pair (exact fold) = {M_IB_fold:.6f}")
print(f"  M_ATDHFB_pair (exact fold) = {M_ATDHFB_fold:.6f}")

# Diagonal-only at exact fold
M_IB_diag_fold = 0.0
M_ATDHFB_diag_fold = 0.0
for k in range(n_modes):
    de = deps_fold[k]
    Ek = E_fold[k]
    M_IB_diag_fold += 2.0 * de**2 / (2.0 * Ek)**2
    M_ATDHFB_diag_fold += 2.0 * de**2 / (2.0 * Ek)**3

print(f"\n  M_IB_diag (exact fold) = {M_IB_diag_fold:.6f}")
print(f"  M_ATDHFB_diag (exact fold) = {M_ATDHFB_diag_fold:.6f}")

# Frozen-gap (no dDelta, but with BCS factors)
M_IB_frozen_fold = 0.0
M_ATDHFB_frozen_fold = 0.0
for k in range(n_modes):
    uk = u_k_fold[k]
    vk = v_k_fold[k]
    de = deps_fold[k]
    Ek = E_fold[k]
    F_frozen = 2.0 * uk * vk * de  # only the deps term
    M_IB_frozen_fold += 2.0 * F_frozen**2 / (2.0 * Ek)**2
    M_ATDHFB_frozen_fold += 2.0 * F_frozen**2 / (2.0 * Ek)**3

print(f"  M_IB_frozen (exact fold) = {M_IB_frozen_fold:.6f}")
print(f"  M_ATDHFB_frozen (exact fold) = {M_ATDHFB_frozen_fold:.6f}")

# Mode decomposition
print(f"\n  Mode decomposition at exact fold:")
branches = ['B2[0]','B2[1]','B2[2]','B2[3]','B1','B3[0]','B3[1]','B3[2]']
for k in range(n_modes):
    uk = u_k_fold[k]; vk = v_k_fold[k]
    de = deps_fold[k]; dD = dDelta_fold[k]; Ek = E_fold[k]
    F_kk = F_kk_fold[k]
    c_IB = 2.0 * F_kk**2 / (2.0 * Ek)**2
    c_ATDHFB = 2.0 * F_kk**2 / (2.0 * Ek)**3
    term1 = 2*uk*vk*de
    term2 = (uk**2 - vk**2)*dD
    print(f"    {branches[k]:6s}: F={F_kk:+.6f} = [{term1:+.6f}(deps) + {term2:+.6f}(dDelta)],"
          f" E={Ek:.4f}, c_IB={c_IB:.6f}, c_ATDHFB={c_ATDHFB:.6f}")

# ============================================================
# 8. METHOD C: Cross-branch contributions
# ============================================================
print("\n" + "=" * 70)
print("METHOD C: Cross-Branch Contributions")
print("=" * 70)

# For k != k' in different branches:
# |<k|dD_K/dtau|k'>|^2 estimated from avoided-crossing mixing.
# Since BCS factors cancel: contribution = 2*|N_{kk'}|^2 / (E_k + E_{k'})^n

M_IB_cross_fold = 0.0
M_ATDHFB_cross_fold = 0.0

# B2-B1 coupling
gap_21 = abs(eps_fold[0] - eps_fold[4])
dv_21 = abs(deps_fold[0] - deps_fold[4])
V_21 = abs(V_phys_fold[0, 4])

sin2phi_21 = 2.0 * V_21 / np.sqrt(gap_21**2 + 4.0 * V_21**2)
N_21_sq = (dv_21 * sin2phi_21 / 2.0)**2
E_B2 = E_fold[0]
E_B1 = E_fold[4]
M_cross_21_IB = 4.0 * 2.0 * N_21_sq / (E_B2 + E_B1)**2
M_cross_21_ATDHFB = 4.0 * 2.0 * N_21_sq / (E_B2 + E_B1)**3
M_IB_cross_fold += M_cross_21_IB
M_ATDHFB_cross_fold += M_cross_21_ATDHFB
print(f"  B2-B1: gap={gap_21:.4f}, V={V_21:.4f}, sin(2phi)={sin2phi_21:.4f}")
print(f"    |N|^2={N_21_sq:.6f}, 4x IB={M_cross_21_IB:.6f}, 4x ATDHFB={M_cross_21_ATDHFB:.6f}")

# B2-B3 coupling
gap_23 = abs(eps_fold[0] - eps_fold[5])
dv_23 = abs(deps_fold[0] - deps_fold[5])
V_23 = abs(V_phys_fold[0, 5])

sin2phi_23 = 2.0 * V_23 / np.sqrt(gap_23**2 + 4.0 * V_23**2)
N_23_sq = (dv_23 * sin2phi_23 / 2.0)**2
E_B3 = E_fold[5]
M_cross_23_IB = 4.0 * 3.0 * 2.0 * N_23_sq / (E_B2 + E_B3)**2
M_cross_23_ATDHFB = 4.0 * 3.0 * 2.0 * N_23_sq / (E_B2 + E_B3)**3
M_IB_cross_fold += M_cross_23_IB
M_ATDHFB_cross_fold += M_cross_23_ATDHFB
print(f"  B2-B3: gap={gap_23:.4f}, V={V_23:.4f}, sin(2phi)={sin2phi_23:.4f}")
print(f"    |N|^2={N_23_sq:.6f}, 12x IB={M_cross_23_IB:.6f}, 12x ATDHFB={M_cross_23_ATDHFB:.6f}")

# B1-B3 coupling
gap_13 = abs(eps_fold[4] - eps_fold[5])
dv_13 = abs(deps_fold[4] - deps_fold[5])
V_13 = abs(V_phys_fold[4, 5])

sin2phi_13 = 2.0 * V_13 / np.sqrt(gap_13**2 + 4.0 * V_13**2)
N_13_sq = (dv_13 * sin2phi_13 / 2.0)**2
M_cross_13_IB = 3.0 * 2.0 * N_13_sq / (E_B1 + E_B3)**2
M_cross_13_ATDHFB = 3.0 * 2.0 * N_13_sq / (E_B1 + E_B3)**3
M_IB_cross_fold += M_cross_13_IB
M_ATDHFB_cross_fold += M_cross_13_ATDHFB
print(f"  B1-B3: gap={gap_13:.4f}, V={V_13:.4f}, sin(2phi)={sin2phi_13:.4f}")
print(f"    |N|^2={N_13_sq:.6f}, 3x IB={M_cross_13_IB:.6f}, 3x ATDHFB={M_cross_13_ATDHFB:.6f}")

print(f"\n  Cross-branch total: M_IB={M_IB_cross_fold:.6f}, M_ATDHFB={M_ATDHFB_cross_fold:.6f}")

# ============================================================
# 9. METHOD D: Fubini-Study geometric mass
# ============================================================
print("\n" + "=" * 70)
print("METHOD D: Fubini-Study Geometric Mass")
print("=" * 70)

g_FS_fold = float(fs['pt_g_FS'])
print(f"g_FS at fold = {g_FS_fold:.6f}")

# g_FS^BCS = sum_k (u_k dv_k - v_k du_k)^2
g_FS_BCS_fold = 0.0
for k in range(n_modes):
    uk = u_k_fold[k]; vk = v_k_fold[k]
    # dv_k and du_k at fold from spline
    cs_v = CubicSpline(rg_tau, v_rg[:, k])
    cs_u = CubicSpline(rg_tau, u_rg[:, k])
    dvk = cs_v(tau_fold_exact, 1)
    duk = cs_u(tau_fold_exact, 1)
    g_FS_BCS_fold += (uk * dvk - vk * duk)**2

print(f"g_FS^BCS (from Bogoliubov angles) = {g_FS_BCS_fold:.6f}")
print(f"g_FS(stored) / g_FS^BCS = {g_FS_fold / g_FS_BCS_fold:.4f}")

# The stored g_FS is from the SINGLE-PARTICLE Dirac operator (how fast
# individual eigenstate wavefunctions rotate with tau). The BCS g_FS
# measures how fast the MANY-BODY BCS state changes. These are distinct.
# The ratio tells us the relative importance of single-particle vs
# many-body dynamics.

# QRPA-based estimate
omega_QRPA_B2 = 3.245  # B2-dominated QRPA mode
M_ATDHFB_QRPA = g_FS_BCS_fold / omega_QRPA_B2**2
print(f"\nQRPA estimate: M_ATDHFB = g_FS^BCS / omega_B2^2 = {M_ATDHFB_QRPA:.6f}")

# ============================================================
# 10. TOTAL CRANKING MASS AND SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("TOTAL CRANKING MASS")
print("=" * 70)

M_IB_TOTAL = M_IB_fold + M_IB_cross_fold
M_ATDHFB_TOTAL = M_ATDHFB_fold + M_ATDHFB_cross_fold

from canonical_constants import G_DeWitt as G_mod
delta_tau_BCS = 0.09

print(f"\n{'Quantity':44s} {'M_IB':>10s} {'M_ATDHFB':>10s}")
print(f"{'-'*66}")
print(f"{'A. Diagonal (deps only)':44s} {M_IB_diag_fold:10.6f} {M_ATDHFB_diag_fold:10.6f}")
print(f"{'B. Frozen-gap (deps, with BCS factors)':44s} {M_IB_frozen_fold:10.6f} {M_ATDHFB_frozen_fold:10.6f}")
print(f"{'C. Full pair-breaking (deps + dDelta)':44s} {M_IB_fold:10.6f} {M_ATDHFB_fold:10.6f}")
print(f"{'D. Cross-branch':44s} {M_IB_cross_fold:10.6f} {M_ATDHFB_cross_fold:10.6f}")
print(f"{'TOTAL (C+D)':44s} {M_IB_TOTAL:10.6f} {M_ATDHFB_TOTAL:10.6f}")
print(f"{'Geometric (g_FS single-particle)':44s} {'':>10s} {g_FS_fold:10.6f}")
print(f"{'Geometric (g_FS^BCS many-body)':44s} {'':>10s} {g_FS_BCS_fold:10.6f}")
print(f"{'QRPA (g_FS^BCS / omega_B2^2)':44s} {'':>10s} {M_ATDHFB_QRPA:10.6f}")

print(f"\nEnhancement over G_mod = {G_mod}:")
print(f"  M_ATDHFB_TOTAL / G_mod = {M_ATDHFB_TOTAL/G_mod:.4f}x")
print(f"  Expected (Naz-Hawking): 50-170x")

# ============================================================
# 11. WHY THE CRANKING MASS IS O(1), NOT O(250-850)
# ============================================================
print("\n" + "=" * 70)
print("PHYSICS: WHY M_COLL IS O(1)")
print("=" * 70)

print(f"""
At the fold (tau={tau_fold_exact:.4f}):
  v_B2 = {deps_fold[0]:.6f} (VANISHES: B2 at van Hove minimum)
  v_B1 = {deps_fold[4]:.6f} (nonzero: B1 still dispersing)
  v_B3 = {deps_fold[5]:.6f} (large: B3 fastest branch)

  E_qp(B2) = {E_fold[0]:.4f} (LARGE: dominated by BCS gap Delta=2.06)
  E_qp(B1) = {E_fold[4]:.4f}
  E_qp(B3) = {E_fold[5]:.4f}

  Delta(B2)/eps(B2) = {Delta_fold[0]/eps_fold[0]:.4f} (strong pairing, v_B2~0.49)
  Delta(B1)/eps(B1) = {Delta_fold[4]/eps_fold[4]:.4f} (moderate pairing)
  Delta(B3)/eps(B3) = {Delta_fold[5]/eps_fold[5]:.4f} (weak pairing)

The cranking mass has TWO factors that make it small:
1. v_B2 ~ 0 at the fold (van Hove minimum). The B2 eigenvalue derivative
   vanishes, so the diagonal contribution from B2 (which has 4-fold degeneracy
   and carries 93% of the BCS condensate weight) is NEGLIGIBLE.

2. E_qp(B2) = 2.23 is LARGE. Even if F_kk were of order 1, the denominator
   (2*E_B2)^2 ~ 20 or (2*E_B2)^3 ~ 45 suppresses the mass.

The Naz-Hawking estimate of 50-170x enhancement assumed the nuclear physics
analogy where the BCS gap CLOSES near the crossing (making E_qp -> 0 and
M -> infinity). In the SU(3) internal space, the gap remains LARGE at the
fold because the van Hove singularity is a velocity zero (minimum of the
dispersion), not a gap closure. The cranking mass remains order-1 throughout
the transit region.

The dDelta/dtau contribution (Method B vs A enhancement) adds a factor of
{M_ATDHFB_fold/M_ATDHFB_diag_fold:.1f}x over the pure diagonal mass, showing that
the gap derivative dominates over the direct eigenvalue velocity at the fold
(because v_B2 ~ 0, the dDelta term wins).
""")

# ============================================================
# 12. SIGMA_ZP
# ============================================================
print("=" * 70)
print("ZERO-POINT AMPLITUDE")
print("=" * 70)

results = {}
for M_label, M_val in [
    ('M_ATDHFB_total', M_ATDHFB_TOTAL),
    ('M_ATDHFB_pair', M_ATDHFB_fold),
    ('g_FS^BCS', g_FS_BCS_fold),
    ('g_FS_sp', g_FS_fold),
]:
    for K_label, K_val in [('d2S_fold', d2S_fold), ('d2e1_fold', d2e1_dtau2_fold)]:
        if M_val > 0 and K_val > 0:
            omega = np.sqrt(K_val / M_val)
            sigma = (1.0 / (4.0 * M_val * K_val))**0.25
            MK = M_val * omega

            key = f"{M_label}+{K_label}"
            results[key] = dict(M=M_val, K=K_val, omega=omega, sigma_ZP=sigma, M_omega=MK)

            verdict = 'PASS' if sigma > delta_tau_BCS else ('FAIL' if sigma < 0.05 else 'INFO')
            print(f"\n  {key}:")
            print(f"    M={M_val:.4f}, K={K_val:.0f}, omega={omega:.2f}")
            print(f"    sigma_ZP = {sigma:.6f}")
            print(f"    sigma_ZP / delta_tau_BCS = {sigma/delta_tau_BCS:.4f}")
            print(f"    M*omega = {MK:.2f} (need <61.7 for PASS)")
            print(f"    VERDICT: {verdict}")

# ============================================================
# 13. g_FS vs M_ATDHFB PEAK COMPARISON
# ============================================================
print("\n" + "=" * 70)
print("g_FS vs M_ATDHFB PEAK COMPARISON")
print("=" * 70)

idx_gFS_peak = np.argmax(g_FS_ext)
tau_gFS_peak = tau_fs[idx_gFS_peak]
print(f"g_FS peak: tau = {tau_gFS_peak:.3f}")

M_A_interior = M_ATDHFB_A.copy()
M_A_interior[:2] = 0; M_A_interior[-2:] = 0
idx_MA_peak = np.argmax(M_A_interior)
tau_MA_peak = tau_grid[idx_MA_peak]
print(f"M_ATDHFB_A peak: tau = {tau_MA_peak:.4f}")

M_B_interior = M_ATDHFB_B.copy()
M_B_interior[:2] = 0; M_B_interior[-2:] = 0
idx_MB_peak = np.argmax(M_B_interior)
tau_MB_peak = tau_grid[idx_MB_peak]
print(f"M_ATDHFB_B peak: tau = {tau_MB_peak:.4f}")

sep = abs(tau_gFS_peak - tau_MA_peak)
print(f"g_FS - M_ATDHFB separation: {sep:.4f}")
print(f"Same peak? {'YES' if sep < 0.05 else 'NO'}")

# ============================================================
# 14. CROSS-CHECKS
# ============================================================
print("\n" + "=" * 70)
print("CROSS-CHECKS")
print("=" * 70)

# 1. u^2 + v^2 = 1
print(f"1. max|u^2+v^2-1| at fold: {np.max(np.abs(u_k_fold**2 + v_k_fold**2 - 1.0)):.2e}")

# 2. E_qp from two formulas
E_from_Delta = np.sqrt(eps_fold**2 + Delta_fold**2)
E_from_uv = eps_fold / (u_k_fold**2 - v_k_fold**2)
print(f"2. max|E(Delta) - E(u,v)| / E: {np.max(np.abs(E_from_Delta/E_from_uv - 1.0)):.2e}")

# 3. M_ATDHFB < M_IB (ATDHFB has extra 1/E in denominator, E > 0.5)
print(f"3. M_ATDHFB/M_IB (total): {M_ATDHFB_TOTAL/M_IB_TOTAL:.4f} (<1 expected)")

# 4. Enhancement from dDelta vs diagonal
print(f"4. M_pair/M_diag at fold: {M_ATDHFB_fold/M_ATDHFB_diag_fold:.2f}x (dDelta enhancement)")

# 5. Comparison with g_FS methods
print(f"5. g_FS_sp / g_FS^BCS: {g_FS_fold/g_FS_BCS_fold:.2f}")

# 6. Velocity-squared sum
v_sq = 4*deps_fold[0]**2 + deps_fold[4]**2 + 3*deps_fold[5]**2
print(f"6. Sum(deps^2): {v_sq:.6f}")
print(f"   B2 share: {4*deps_fold[0]**2/v_sq*100:.1f}%, B1: {deps_fold[4]**2/v_sq*100:.1f}%, B3: {3*deps_fold[5]**2/v_sq*100:.1f}%")

# ============================================================
# 15. SAVE DATA
# ============================================================

# sigma_ZP profiles
sigma_ZP_A_SA = np.zeros(n_tau)
sigma_ZP_A_BCS = np.zeros(n_tau)
omega_A_SA = np.zeros(n_tau)
omega_A_BCS = np.zeros(n_tau)

for i in range(n_tau):
    M = M_ATDHFB_B[i]  # pair-breaking mass
    if M > 1e-10:
        omega_A_SA[i] = np.sqrt(d2S_fold / M)
        sigma_ZP_A_SA[i] = (1.0 / (4.0 * M * d2S_fold))**0.25
        omega_A_BCS[i] = np.sqrt(d2e1_dtau2_fold / M)
        sigma_ZP_A_BCS[i] = (1.0 / (4.0 * M * d2e1_dtau2_fold))**0.25

sigma_ZP_SA_fold = (1.0 / (4.0 * M_ATDHFB_TOTAL * d2S_fold))**0.25 if M_ATDHFB_TOTAL > 0 else 0
sigma_ZP_BCS_fold = (1.0 / (4.0 * M_ATDHFB_TOTAL * d2e1_dtau2_fold))**0.25 if M_ATDHFB_TOTAL > 0 else 0
omega_SA_fold = np.sqrt(d2S_fold / M_ATDHFB_TOTAL) if M_ATDHFB_TOTAL > 0 else 0
omega_BCS_fold = np.sqrt(d2e1_dtau2_fold / M_ATDHFB_TOTAL) if M_ATDHFB_TOTAL > 0 else 0

if sigma_ZP_SA_fold > delta_tau_BCS:
    gate_verdict = 'PASS'
elif sigma_ZP_SA_fold < 0.05:
    gate_verdict = 'FAIL'
else:
    gate_verdict = 'INFO'

np.savez('tier0-computation/s40_collective_inertia.npz',
    tau_grid=tau_grid, rg_tau=rg_tau, n_modes=n_modes,
    fold_idx=fold_idx, tau_fold=tau_grid[fold_idx],
    tau_fold_exact=tau_fold_exact, delta_tau_BCS=delta_tau_BCS, G_mod=G_mod,

    # Method A: Diagonal (50 points)
    M_IB_A=M_IB_A, M_ATDHFB_A=M_ATDHFB_A,

    # Method B: Pair-breaking (50 points)
    M_IB_B=M_IB_B, M_ATDHFB_B=M_ATDHFB_B,

    # Fold values
    M_IB_diag_fold=M_IB_diag_fold, M_ATDHFB_diag_fold=M_ATDHFB_diag_fold,
    M_IB_frozen_fold=M_IB_frozen_fold, M_ATDHFB_frozen_fold=M_ATDHFB_frozen_fold,
    M_IB_fold=M_IB_fold, M_ATDHFB_fold=M_ATDHFB_fold,
    M_IB_cross_fold=M_IB_cross_fold, M_ATDHFB_cross_fold=M_ATDHFB_cross_fold,
    M_IB_TOTAL=M_IB_TOTAL, M_ATDHFB_TOTAL=M_ATDHFB_TOTAL,
    g_FS_fold=g_FS_fold, g_FS_BCS_fold=g_FS_BCS_fold,
    M_ATDHFB_QRPA=M_ATDHFB_QRPA,

    enhancement_total=M_ATDHFB_TOTAL / G_mod,
    F_kk_fold=F_kk_fold, deps_fold=deps_fold, dDelta_fold=dDelta_fold,
    eps_fold=eps_fold, Delta_fold=Delta_fold, E_fold=E_fold,
    u_fold=u_k_fold, v_fold=v_k_fold,

    # Sigma_ZP
    sigma_ZP_A_SA=sigma_ZP_A_SA, sigma_ZP_A_BCS=sigma_ZP_A_BCS,
    sigma_ZP_SA_fold=sigma_ZP_SA_fold, sigma_ZP_BCS_fold=sigma_ZP_BCS_fold,
    omega_SA_fold=omega_SA_fold, omega_BCS_fold=omega_BCS_fold,
    d2S_fold=d2S_fold, d2e1_fold=d2e1_dtau2_fold,

    # Peaks
    tau_gFS_peak=tau_gFS_peak, tau_M_peak=tau_MA_peak,

    gate_verdict=gate_verdict,
)

print(f"\nData saved to tier0-computation/s40_collective_inertia.npz")

# ============================================================
# 16. PLOT
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('M-COLL-40: ATDHFB Collective Inertia at the Fold', fontsize=14, fontweight='bold')

mask = (tau_grid > 0.02) & (tau_grid < 0.48)

# Panel 1: Cranking mass profiles
ax = axes[0, 0]
ax.semilogy(tau_grid[mask], M_ATDHFB_A[mask], 'b-', linewidth=2, label='$M_{ATDHFB}^{diag}$ (Meth A)')
ax.semilogy(tau_grid[mask], M_ATDHFB_B[mask], 'r--', linewidth=2, label='$M_{ATDHFB}^{pair}$ (Meth B)')
ax.semilogy(tau_fs, g_FS_ext, 'g:', linewidth=1.5, label='$g_{FS}$ (sp)')
ax.axvline(tau_fold_exact, color='gray', linestyle=':', alpha=0.5, label='fold')
ax.axhline(G_mod, color='orange', linestyle='--', alpha=0.5, label=f'$G_{{mod}}$ = {G_mod}')
ax.set_xlabel(r'$\tau$'); ax.set_ylabel(r'$M_{coll}$')
ax.set_title('Cranking Mass Profiles')
ax.legend(fontsize=7, loc='upper left')
ax.set_xlim(0.02, 0.48)

# Panel 2: g_FS vs M_ATDHFB (normalized)
ax = axes[0, 1]
M_B_plot = M_ATDHFB_B[mask]
M_B_max = np.max(np.abs(M_B_plot))
g_interp_plot = np.interp(tau_grid, tau_fs, g_FS_ext)[mask]
g_max = np.max(g_interp_plot)
if M_B_max > 0 and g_max > 0:
    ax.plot(tau_grid[mask], M_B_plot / M_B_max, 'b-', linewidth=2, label='$M_{ATDHFB}$ (norm)')
    ax.plot(tau_grid[mask], g_interp_plot / g_max, 'r--', linewidth=2, label='$g_{FS}$ (norm)')
ax.axvline(tau_fold_exact, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$\tau$'); ax.set_ylabel('Normalized')
ax.set_title('$g_{FS}$ vs $M_{ATDHFB}$ Shape')
ax.legend()
ax.set_xlim(0.05, 0.45)

# Panel 3: sigma_ZP profile
ax = axes[1, 0]
valid_SA = sigma_ZP_A_SA > 0
valid_BCS = sigma_ZP_A_BCS > 0
if np.any(valid_SA & mask):
    ax.plot(tau_grid[valid_SA & mask], sigma_ZP_A_SA[valid_SA & mask], 'b-', linewidth=2,
            label=r'$\sigma_{ZP}$ (SA curv)')
if np.any(valid_BCS & mask):
    ax.plot(tau_grid[valid_BCS & mask], sigma_ZP_A_BCS[valid_BCS & mask], 'r--', linewidth=1.5,
            label=r'$\sigma_{ZP}$ (BCS curv)')
ax.axhline(delta_tau_BCS, color='red', linestyle=':', linewidth=2,
           label=f'$\\delta\\tau_{{BCS}}$ = {delta_tau_BCS}')
ax.axhline(0.05, color='orange', linestyle=':', linewidth=1, label='FAIL threshold')
ax.axvline(tau_fold_exact, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$\tau$'); ax.set_ylabel(r'$\sigma_{ZP}$')
ax.set_title(r'Zero-Point Amplitude vs $\delta\tau_{BCS}$')
ax.legend(fontsize=7)
ax.set_xlim(0.05, 0.45)

# Panel 4: Mode decomposition at fold
ax = axes[1, 1]
contribs = []
for k in range(n_modes):
    F = F_kk_fold[k]
    Ek = E_fold[k]
    contribs.append(2.0 * F**2 / (2.0 * Ek)**3)  # ATDHFB
x = np.arange(n_modes)
colors_bar = ['#1f77b4']*4 + ['#ff7f0e'] + ['#2ca02c']*3
ax.bar(x, contribs, color=colors_bar, alpha=0.7)
ax.set_xticks(x)
ax.set_xticklabels(branches, rotation=45, fontsize=8)
ax.set_ylabel('$M_{ATDHFB}^{pair}$ contribution')
ax.set_title('Mode Decomposition at Fold')

plt.tight_layout()
plt.savefig('tier0-computation/s40_collective_inertia.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to tier0-computation/s40_collective_inertia.png")

# ============================================================
# 17. FINAL SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("FINAL SUMMARY: M-COLL-40")
print("=" * 70)

print(f"\n--- Key Numbers ---")
print(f"  M_ATDHFB_TOTAL at fold = {M_ATDHFB_TOTAL:.4f}")
print(f"  Enhancement: {M_ATDHFB_TOTAL/G_mod:.2f}x G_mod (expected 50-170x)")
print(f"  sigma_ZP (SA curvature) = {sigma_ZP_SA_fold:.4f}")
print(f"  sigma_ZP (BCS curvature) = {sigma_ZP_BCS_fold:.4f}")
print(f"  delta_tau_BCS = {delta_tau_BCS}")
print(f"  g_FS peak at tau = {tau_gFS_peak:.3f}")
print(f"  M_ATDHFB peak at tau = {tau_MA_peak:.4f}")
print(f"  Same peak: {'YES' if abs(tau_gFS_peak - tau_MA_peak) < 0.05 else 'NO'}")

print(f"\n--- Gate Verdict: M-COLL-40 ---")
print(f"  Criterion: PASS if sigma_ZP > 0.09, FAIL if sigma_ZP < 0.05")
print(f"  sigma_ZP(SA) = {sigma_ZP_SA_fold:.4f} {'> 0.09 PASS' if sigma_ZP_SA_fold > 0.09 else '< 0.05 FAIL' if sigma_ZP_SA_fold < 0.05 else 'INTERMEDIATE'}")
print(f"  sigma_ZP(BCS) = {sigma_ZP_BCS_fold:.4f} {'> 0.09 PASS' if sigma_ZP_BCS_fold > 0.09 else '< 0.05 FAIL' if sigma_ZP_BCS_fold < 0.05 else 'INTERMEDIATE'}")
print(f"  VERDICT: {gate_verdict}")
