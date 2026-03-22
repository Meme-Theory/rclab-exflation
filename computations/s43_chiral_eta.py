#!/usr/bin/env python3
"""
Session 43 W3-4: Chiral Eta Invariant at Domain Wall (CHIRAL-ETA-43)
=====================================================================

CONTEXT:
  Full eta(D_K) = 0 identically by spectral pairing ({gamma_9, D_K} = 0).
  W1-3 confirmed: APS eta = 0 at all 8 tau points. Spectral flow = 0.

  This computation tests the CHIRAL eta invariant:
    - Project D_K eigenstates onto P_+/- = (1 +/- gamma_9)/2
    - Compute eta restricted to chiral sectors
    - Test whether chiral spectral asymmetry is nonzero at a domain wall
    - Connect to Callan-Harvey anomaly inflow

ALGEBRAIC ANALYSIS (pre-computation):
  {gamma_9, D_K} = 0 implies:
    1. Eigenvalues come in +/- pairs with gamma_9 mapping between them
    2. Eigenstates of D_K are NOT eigenstates of gamma_9
    3. sign(D_K) anticommutes with gamma_9
    4. Tr(gamma_9 * sign(D_K)) = 0 identically
    5. Tr(gamma_9 * f(D_K^2)) = 0 for any f (since [gamma_9, D_K^2] = 0)

  Therefore the "naive chiral eta" (Tr(gamma_9 * sign(D_K))) vanishes by algebra.

  What CAN be nonzero:
  A) The chirality content of individual eigenstates: <psi_i|P_+|psi_i>
  B) K_7-weighted chiral content: <psi_i|gamma_9 * iK_7|psi_i>
  C) The variation of chirality content across the wall
  D) The resolved APS eta on a half-line with D_wall = -i*sigma_z*d/dx + D_K(tau(x))

GATE CHIRAL-ETA-43:
  PASS: |eta_+ - eta_-| > 10^{-6} at wall center
  FAIL: eta_+ = eta_- to machine precision everywhere

Author: dirac-antimatter-theorist, Session 43
Date: 2026-03-14
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh, norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants,
    compute_killing_form, jensen_metric, orthonormal_frame,
    frame_structure_constants, connection_coefficients,
    build_cliff8, build_chirality, spinor_connection_offset,
    U1_IDX, SU2_IDX, C2_IDX, U2_IDX,
)
from s23a_kosmann_singlet import kosmann_operator_antisymmetric

np.set_printoptions(precision=12, linewidth=140, suppress=True)
t0 = time.time()

# ======================================================================
#  Shared infrastructure
# ======================================================================
gens = su3_generators()
fabc = compute_structure_constants(gens)
Bk = compute_killing_form(fabc)
gammas = build_cliff8()
gamma9 = build_chirality(gammas)

# J (real structure) = C2 = gamma_1 * gamma_3 * gamma_5 * gamma_7
C2 = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]
C1 = gammas[1] @ gammas[3] @ gammas[5] @ gammas[7]
I16 = np.eye(16, dtype=complex)

# Chiral projectors
P_plus  = 0.5 * (I16 + gamma9)   # positive chirality
P_minus = 0.5 * (I16 - gamma9)   # negative chirality

def build_DK_at_tau(tau):
    """Build Hermitian Dirac operator D_K = i*Omega at given tau."""
    g_s = jensen_metric(Bk, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(fabc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    D_K = 1j * Omega
    return D_K, Gamma

def build_K7_at_tau(tau):
    """Build iK_7 at given tau."""
    g_s = jensen_metric(Bk, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(fabc, E)
    Gamma = connection_coefficients(ft)
    K7, A7 = kosmann_operator_antisymmetric(Gamma, gammas, 7)
    return 1j * K7


# ======================================================================
#  STEP 0: Verify algebraic constraints
# ======================================================================
print("=" * 78)
print("CHIRAL-ETA-43: Chiral Eta Invariant at Domain Wall")
print("=" * 78)

print("\n--- Step 0: Algebraic verification ---")

# Verify {gamma_9, D_K} = 0
tau_test = 0.190
D_K_test, _ = build_DK_at_tau(tau_test)
anticomm = gamma9 @ D_K_test + D_K_test @ gamma9
err_anticomm = norm(anticomm, 'fro') / norm(D_K_test, 'fro')
print(f"  {{gamma_9, D_K}} = 0: ||anticomm||/||D_K|| = {err_anticomm:.2e}")

# Verify [gamma_9, D_K^2] = 0
DK2 = D_K_test @ D_K_test
comm_g9_DK2 = gamma9 @ DK2 - DK2 @ gamma9
err_comm_DK2 = norm(comm_g9_DK2, 'fro') / norm(DK2, 'fro')
print(f"  [gamma_9, D_K^2] = 0: ||comm||/||D_K^2|| = {err_comm_DK2:.2e}")

# Verify Tr(gamma_9 * sign(D_K)) = 0
evals_test, evecs_test = eigh(D_K_test)
signs_test = np.sign(evals_test)
signs_test[np.abs(evals_test) < 1e-12] = 0
signDK = evecs_test @ np.diag(signs_test) @ evecs_test.conj().T
tr_g9_signDK = np.real(np.trace(gamma9 @ signDK))
print(f"  Tr(gamma_9 * sign(D_K)) = {tr_g9_signDK:.2e}")

# Check gamma_9 relation with iK_7
iK7_test = build_K7_at_tau(tau_test)
comm_g9_K7 = gamma9 @ iK7_test - iK7_test @ gamma9
anticomm_g9_K7 = gamma9 @ iK7_test + iK7_test @ gamma9
print(f"  [gamma_9, iK_7]: ||comm||/||iK_7|| = {norm(comm_g9_K7, 'fro')/norm(iK7_test, 'fro'):.2e}")
print(f"  {{gamma_9, iK_7}}: ||anticomm||/||iK_7|| = {norm(anticomm_g9_K7, 'fro')/norm(iK7_test, 'fro'):.2e}")

if norm(comm_g9_K7, 'fro') / norm(iK7_test, 'fro') < 1e-10:
    g9_K7_relation = "COMMUTE"
    print(f"  ==> [gamma_9, iK_7] = 0: gamma_9 and iK_7 commute")
    print(f"      K_7 preserves chirality. Chiral sectors have definite K_7 charge.")
elif norm(anticomm_g9_K7, 'fro') / norm(iK7_test, 'fro') < 1e-10:
    g9_K7_relation = "ANTICOMMUTE"
    print(f"  ==> {{gamma_9, iK_7}} = 0: gamma_9 and iK_7 anticommute")
    print(f"      K_7 FLIPS chirality. Chiral sectors carry opposite K_7 charge.")
else:
    g9_K7_relation = "MIXED"
    print(f"  ==> gamma_9 and iK_7 have MIXED relation")


# ======================================================================
#  STEP 1: Domain wall profile
# ======================================================================
print("\n--- Step 1: Domain wall profile ---")

from canonical_constants import tau_fold as TAU_FOLD
DELTA_TAU = 0.02   # representative wall step
XI_BCS = 0.808     # coherence length in M_KK^{-1} (authoritative, from s37_instanton_action.npz)

# 21 points from -3*xi to +3*xi
N_WALL = 21
x_wall = np.linspace(-3.0 * XI_BCS, 3.0 * XI_BCS, N_WALL)
tau_wall = TAU_FOLD + (DELTA_TAU / 2.0) * np.tanh(x_wall / XI_BCS)

print(f"  tau_fold = {TAU_FOLD}")
print(f"  Delta_tau = {DELTA_TAU}")
print(f"  xi_BCS = {XI_BCS} M_KK^{{-1}}")
print(f"  x range: [{x_wall[0]:.3f}, {x_wall[-1]:.3f}] M_KK^{{-1}}")
print(f"  tau range: [{tau_wall[0]:.6f}, {tau_wall[-1]:.6f}]")
print(f"  N_wall = {N_WALL}")


# ======================================================================
#  STEP 2: Compute chirality content of D_K eigenstates across wall
# ======================================================================
print("\n--- Step 2: Chirality content of D_K eigenstates across wall ---")

# For each position x, compute:
# 1. D_K(tau(x)) eigenvalues and eigenvectors
# 2. Chirality of each eigenstate: <psi_i|gamma_9|psi_i>
# 3. Chiral projection weights: <psi_i|P_+|psi_i> and <psi_i|P_-|psi_i>
# 4. The "chiral eta" candidates

evals_wall = np.zeros((N_WALL, 16))
chirality_wall = np.zeros((N_WALL, 16))   # <psi|gamma_9|psi>
weight_plus = np.zeros((N_WALL, 16))      # <psi|P_+|psi>
weight_minus = np.zeros((N_WALL, 16))     # <psi|P_-|psi>
k7_wall = np.zeros((N_WALL, 16))          # <psi|iK_7|psi>

# Chiral eta candidates
eta_full = np.zeros(N_WALL)               # standard eta = N_+ - N_-
eta_chiral_sign = np.zeros(N_WALL)        # Tr(gamma_9 * sign(D_K))
eta_chiral_resolvent = np.zeros(N_WALL)   # Tr(gamma_9 * D_K * |D_K|^{-1}) = same as above
eta_plus = np.zeros(N_WALL)               # sum_{lambda > 0} <psi_lambda|P_+|psi_lambda>
eta_minus = np.zeros(N_WALL)              # sum_{lambda > 0} <psi_lambda|P_-|psi_lambda>
eta_plus_signed = np.zeros(N_WALL)        # sum_i sign(lambda_i) * <psi_i|P_+|psi_i>
eta_minus_signed = np.zeros(N_WALL)       # sum_i sign(lambda_i) * <psi_i|P_-|psi_i>
# K_7 weighted chiral quantities
eta_k7_chiral = np.zeros(N_WALL)          # Tr(gamma_9 * iK_7 * sign(D_K))
eta_k7_plus = np.zeros(N_WALL)            # sum_i sign(lambda_i) * <psi_i|P_+ iK_7|psi_i>
eta_k7_minus = np.zeros(N_WALL)           # sum_i sign(lambda_i) * <psi_i|P_- iK_7|psi_i>
# Resolvent-weighted quantities (s != 0)
s_reg = 1.0  # regularization parameter
eta_chiral_s1 = np.zeros(N_WALL)          # sum_i <psi_i|gamma_9|psi_i> * sign(lambda_i) * |lambda_i|^{-s}
eta_plus_s1 = np.zeros(N_WALL)            # sum_i sign(lambda_i) * |lambda_i|^{-s} * <psi_i|P_+|psi_i>
eta_minus_s1 = np.zeros(N_WALL)           # sum_i sign(lambda_i) * |lambda_i|^{-s} * <psi_i|P_-|psi_i>

for ix in range(N_WALL):
    tau_x = tau_wall[ix]
    D_K_x, Gamma_x = build_DK_at_tau(tau_x)
    iK7_x = build_K7_at_tau(tau_x)

    evals_x, evecs_x = eigh(D_K_x)
    evals_wall[ix] = evals_x

    # Compute chirality and K_7 in eigenbasis
    g9_eig = evecs_x.conj().T @ gamma9 @ evecs_x
    iK7_eig = evecs_x.conj().T @ iK7_x @ evecs_x
    Pp_eig = evecs_x.conj().T @ P_plus @ evecs_x
    Pm_eig = evecs_x.conj().T @ P_minus @ evecs_x

    chirality_wall[ix] = np.real(np.diag(g9_eig))
    k7_wall[ix] = np.real(np.diag(iK7_eig))
    weight_plus[ix] = np.real(np.diag(Pp_eig))
    weight_minus[ix] = np.real(np.diag(Pm_eig))

    # Standard eta
    n_pos = np.sum(evals_x > 1e-12)
    n_neg = np.sum(evals_x < -1e-12)
    eta_full[ix] = n_pos - n_neg

    # Tr(gamma_9 * sign(D_K))
    signs = np.sign(evals_x)
    signs[np.abs(evals_x) < 1e-12] = 0
    signDK = evecs_x @ np.diag(signs) @ evecs_x.conj().T
    eta_chiral_sign[ix] = np.real(np.trace(gamma9 @ signDK))

    # Chiral projections of sign(D_K)
    for i in range(16):
        if abs(evals_x[i]) > 1e-12:
            si = np.sign(evals_x[i])
            wp = weight_plus[ix, i]
            wm = weight_minus[ix, i]

            eta_plus_signed[ix] += si * wp
            eta_minus_signed[ix] += si * wm

            # s=1 regularized
            lam_inv = abs(evals_x[i])**(-s_reg)
            eta_plus_s1[ix] += si * lam_inv * wp
            eta_minus_s1[ix] += si * lam_inv * wm
            eta_chiral_s1[ix] += si * lam_inv * chirality_wall[ix, i]

            if evals_x[i] > 0:
                eta_plus[ix] += wp
                eta_minus[ix] += wm

    # K_7 weighted chiral quantities
    eta_k7_chiral[ix] = np.real(np.trace(gamma9 @ iK7_x @ signDK))

    for i in range(16):
        if abs(evals_x[i]) > 1e-12:
            si = np.sign(evals_x[i])
            # P_+ iK_7 expectation value
            PpK7 = evecs_x.conj().T @ P_plus @ iK7_x @ evecs_x
            PmK7 = evecs_x.conj().T @ P_minus @ iK7_x @ evecs_x
            eta_k7_plus[ix] += si * np.real(PpK7[i, i])
            eta_k7_minus[ix] += si * np.real(PmK7[i, i])


# Print results
print(f"\n  {'x/xi':>8s}  {'tau':>8s}  {'eta_full':>9s}  {'eta_chiral':>11s}  "
      f"{'eta+_sgn':>9s}  {'eta-_sgn':>9s}  {'|eta+-eta-|':>12s}")
print(f"  {'-'*78}")
for ix in range(N_WALL):
    diff = abs(eta_plus_signed[ix] - eta_minus_signed[ix])
    print(f"  {x_wall[ix]/XI_BCS:+8.3f}  {tau_wall[ix]:8.6f}  {eta_full[ix]:+9.0f}  "
          f"{eta_chiral_sign[ix]:+11.6f}  "
          f"{eta_plus_signed[ix]:+9.5f}  {eta_minus_signed[ix]:+9.5f}  {diff:12.2e}")


# ======================================================================
#  STEP 3: Analyze chirality content structure
# ======================================================================
print("\n--- Step 3: Chirality content analysis ---")

# At wall center (x=0, tau=tau_fold)
ix_center = N_WALL // 2
print(f"\n  Wall center (x=0, tau={tau_wall[ix_center]:.6f}):")
print(f"  {'n':>3s}  {'lambda':>12s}  {'<gamma_9>':>10s}  {'w_+':>8s}  {'w_-':>8s}  {'<K_7>':>10s}")
print(f"  {'-'*58}")
for i in range(16):
    print(f"  {i:3d}  {evals_wall[ix_center, i]:+12.6f}  "
          f"{chirality_wall[ix_center, i]:+10.6f}  "
          f"{weight_plus[ix_center, i]:8.6f}  "
          f"{weight_minus[ix_center, i]:8.6f}  "
          f"{k7_wall[ix_center, i]:+10.6f}")

# Check: for paired eigenvalues (lambda, -lambda), what is the chirality pairing?
print(f"\n  Eigenvalue pairing and chirality:")
for i in range(8):
    j = 15 - i  # paired eigenvalue (by sorting order)
    if abs(evals_wall[ix_center, i] + evals_wall[ix_center, j]) < 1e-6:
        chi_i = chirality_wall[ix_center, i]
        chi_j = chirality_wall[ix_center, j]
        print(f"    pair ({i},{j}): lambda=({evals_wall[ix_center,i]:+.6f}, "
              f"{evals_wall[ix_center,j]:+.6f})  "
              f"chi=({chi_i:+.6f}, {chi_j:+.6f})  sum={chi_i+chi_j:+.2e}")


# ======================================================================
#  STEP 4: The resolvent chiral eta (Bismut-Freed)
# ======================================================================
print("\n--- Step 4: Resolvent chiral eta (Bismut-Freed) ---")
print(f"  Regularization parameter s = {s_reg}")

print(f"\n  {'x/xi':>8s}  {'tau':>8s}  {'eta+_s1':>10s}  {'eta-_s1':>10s}  "
      f"{'|diff|':>12s}  {'eta_k7_chiral':>14s}")
print(f"  {'-'*68}")
for ix in range(N_WALL):
    diff_s1 = abs(eta_plus_s1[ix] - eta_minus_s1[ix])
    print(f"  {x_wall[ix]/XI_BCS:+8.3f}  {tau_wall[ix]:8.6f}  "
          f"{eta_plus_s1[ix]:+10.6f}  {eta_minus_s1[ix]:+10.6f}  "
          f"{diff_s1:12.2e}  {eta_k7_chiral[ix]:+14.8f}")


# ======================================================================
#  STEP 5: Wall gradient contribution (semi-classical)
# ======================================================================
print("\n--- Step 5: Wall gradient contribution ---")

# The wall gradient dtau/dx at each point
dtau_dx = (DELTA_TAU / 2.0) / XI_BCS * (1.0 / np.cosh(x_wall / XI_BCS))**2

# Maximum gradient
max_gradient = np.max(dtau_dx)
print(f"  max|dtau/dx| = {max_gradient:.6e} (at wall center)")
print(f"  dtau/dx * xi = {max_gradient * XI_BCS:.6e}")

# Semi-classical anomaly: in 1+1D, the chiral anomaly is proportional to
# the gauge field strength. Here the "gauge field" is the Berry connection
# from the tau-dependence of D_K eigenstates.

# Berry connection: A_n(x) = -i <psi_n(tau(x))| d/dx |psi_n(tau(x))>
#                           = -i <psi_n|d/dtau|psi_n> * dtau/dx

# Compute d/dtau eigenstates numerically
dtau_num = 1e-5
berry_phase = np.zeros((N_WALL, 16))
berry_curvature_chiral = np.zeros(N_WALL)

for ix in range(N_WALL):
    tau_x = tau_wall[ix]
    D_K_x, _ = build_DK_at_tau(tau_x)
    D_K_x2, _ = build_DK_at_tau(tau_x + dtau_num)

    evals_x, evecs_x = eigh(D_K_x)
    _, evecs_x2 = eigh(D_K_x2)

    # Fix gauge: ensure <psi_n(tau)|psi_n(tau+dtau)> is real positive
    overlaps = np.sum(evecs_x.conj() * evecs_x2, axis=0)
    phases = np.exp(-1j * np.angle(overlaps))
    evecs_x2_gauged = evecs_x2 * phases[np.newaxis, :]

    # Berry connection in tau
    d_evecs = (evecs_x2_gauged - evecs_x) / dtau_num
    for n in range(16):
        A_n = -1j * np.dot(evecs_x[:, n].conj(), d_evecs[:, n])
        berry_phase[ix, n] = np.real(A_n) * dtau_dx[ix]

    # Chiral Berry curvature: sum over eigenstates weighted by chirality
    for n in range(16):
        chi_n = np.real(evecs_x[:, n].conj() @ gamma9 @ evecs_x[:, n])
        berry_curvature_chiral[ix] += chi_n * berry_phase[ix, n]

print(f"\n  {'x/xi':>8s}  {'tau':>8s}  {'dtau/dx':>10s}  {'F_chiral':>12s}  {'sum|A_n|':>12s}")
print(f"  {'-'*60}")
for ix in range(N_WALL):
    sum_abs_A = np.sum(np.abs(berry_phase[ix]))
    print(f"  {x_wall[ix]/XI_BCS:+8.3f}  {tau_wall[ix]:8.6f}  "
          f"{dtau_dx[ix]:10.6e}  {berry_curvature_chiral[ix]:+12.6e}  {sum_abs_A:12.6e}")

# Integrated chiral anomaly across the wall
dx = x_wall[1] - x_wall[0]
integrated_chiral = np.trapezoid(berry_curvature_chiral, x_wall)
print(f"\n  Integrated chiral Berry curvature across wall: {integrated_chiral:+.8e}")


# ======================================================================
#  STEP 6: Direct D_wall construction (1D + internal)
# ======================================================================
print("\n--- Step 6: Full wall Dirac operator D_wall ---")

# Construct D_wall on a finite grid as a (16*N_WALL) x (16*N_WALL) matrix
# D_wall = -i sigma_z otimes d/dx + I_2 otimes D_K(tau(x))
# But since D_K is already 16x16 and we don't have a 2-component 1D structure,
# the correct construction for a 1D wall in internal space is:
#
# H_wall(x, x') = D_K(tau(x)) * delta(x-x') + gradient corrections
#
# For a slowly varying wall (xi >> 1/gap), the local approximation is good.
# The chiral anomaly comes from the INTEGRATED spectral flow, not from
# a single-point eta.

# Let's use a smaller grid for the full matrix
N_grid = 11
x_grid = np.linspace(-3.0 * XI_BCS, 3.0 * XI_BCS, N_grid)
tau_grid = TAU_FOLD + (DELTA_TAU / 2.0) * np.tanh(x_grid / XI_BCS)
dx_grid = x_grid[1] - x_grid[0]

# Build block-diagonal D_K at each grid point
DIM_TOTAL = 16 * N_grid
D_wall_block = np.zeros((DIM_TOTAL, DIM_TOTAL), dtype=complex)

# Diagonal blocks: D_K(tau(x_i))
for ix in range(N_grid):
    D_K_ix, _ = build_DK_at_tau(tau_grid[ix])
    i0 = ix * 16
    i1 = (ix + 1) * 16
    D_wall_block[i0:i1, i0:i1] = D_K_ix

# Off-diagonal blocks: -i/(2*dx) * I_16 coupling (central differences)
# This is the kinetic term from the 1D spatial derivative
# D_wall = gamma_wall * (-i d/dx) + D_K(tau(x))
# For 1D, gamma_wall is a 1x1 matrix = 1 (or sigma_z for a 2-component system)
# In the simplest case, the gradient just couples adjacent sites:
for ix in range(N_grid - 1):
    i0 = ix * 16
    i1 = (ix + 1) * 16
    coupling = -1j / (2.0 * dx_grid) * I16
    D_wall_block[i0:i1, i1:i1+16] += coupling
    D_wall_block[i1:i1+16, i0:i1] -= coupling  # anti-Hermitian gradient

# Make Hermitian
D_wall_H = 0.5 * (D_wall_block + D_wall_block.conj().T)

# Diagonalize
evals_wall_full, evecs_wall_full = eigh(D_wall_H)

# Construct extended gamma_9: gamma_9 otimes I_{N_grid}
gamma9_ext = np.zeros((DIM_TOTAL, DIM_TOTAL), dtype=complex)
for ix in range(N_grid):
    i0 = ix * 16
    i1 = (ix + 1) * 16
    gamma9_ext[i0:i1, i0:i1] = gamma9

# Check: does {gamma_9_ext, D_wall} = 0?
anticomm_wall = gamma9_ext @ D_wall_H + D_wall_H @ gamma9_ext
err_anticomm_wall = norm(anticomm_wall, 'fro') / norm(D_wall_H, 'fro')
print(f"  Grid: {N_grid} points, dx = {dx_grid:.4f} M_KK^{{-1}}")
print(f"  D_wall dimension: {DIM_TOTAL} x {DIM_TOTAL}")
print(f"  ||{{gamma_9_ext, D_wall}}||/||D_wall|| = {err_anticomm_wall:.6e}")

if err_anticomm_wall < 1e-6:
    print(f"  ==> gamma_9 anticommutes with D_wall: chiral pairing preserved")
    print(f"      Tr(gamma_9_ext * sign(D_wall)) = 0 by algebra")
else:
    print(f"  ==> gamma_9 does NOT anticommute with D_wall")
    print(f"      The gradient term breaks chiral pairing!")

# Compute Tr(gamma_9_ext * sign(D_wall))
signs_wall = np.sign(evals_wall_full)
signs_wall[np.abs(evals_wall_full) < 1e-12] = 0
signDwall = evecs_wall_full @ np.diag(signs_wall) @ evecs_wall_full.conj().T
tr_g9_signDwall = np.real(np.trace(gamma9_ext @ signDwall))
print(f"  Tr(gamma_9_ext * sign(D_wall)) = {tr_g9_signDwall:.8e}")

# Compute chirality content per eigenvalue of D_wall
chirality_Dwall = np.real(np.diag(evecs_wall_full.conj().T @ gamma9_ext @ evecs_wall_full))

# N_+ and N_- in D_wall
n_pos_wall = np.sum(evals_wall_full > 1e-12)
n_neg_wall = np.sum(evals_wall_full < -1e-12)
n_zero_wall = np.sum(np.abs(evals_wall_full) < 1e-12)
print(f"  D_wall: N_+ = {n_pos_wall}, N_- = {n_neg_wall}, N_0 = {n_zero_wall}")
print(f"  eta(D_wall) = {n_pos_wall - n_neg_wall}")


# ======================================================================
#  STEP 7: The definitive test — Chiral eta in eigenvector basis
# ======================================================================
print("\n--- Step 7: Chiral eta per sector (definitive) ---")

# Define eta_+ = sum_{i: <psi_i|P_+|psi_i> > 1/2} sign(lambda_i)
# and   eta_- = sum_{i: <psi_i|P_-|psi_i> > 1/2} sign(lambda_i)
# These classify eigenstates by their DOMINANT chirality

eta_dominant_plus = np.zeros(N_WALL)
eta_dominant_minus = np.zeros(N_WALL)

for ix in range(N_WALL):
    for i in range(16):
        if abs(evals_wall[ix, i]) > 1e-12:
            si = np.sign(evals_wall[ix, i])
            if weight_plus[ix, i] > 0.5:
                eta_dominant_plus[ix] += si
            else:
                eta_dominant_minus[ix] += si

print(f"  {'x/xi':>8s}  {'tau':>8s}  {'eta_dom+':>9s}  {'eta_dom-':>9s}  {'diff':>12s}")
print(f"  {'-'*55}")
for ix in range(N_WALL):
    diff = eta_dominant_plus[ix] - eta_dominant_minus[ix]
    print(f"  {x_wall[ix]/XI_BCS:+8.3f}  {tau_wall[ix]:8.6f}  "
          f"{eta_dominant_plus[ix]:+9.0f}  {eta_dominant_minus[ix]:+9.0f}  {diff:+12.6f}")


# ======================================================================
#  STEP 8: Refined chiral eta — spectral weight method
# ======================================================================
print("\n--- Step 8: Spectral weight chiral eta (continuous) ---")

# The continuous version:
# eta_chiral(x) = sum_i sign(lambda_i) * [<psi_i|P_+|psi_i> - <psi_i|P_-|psi_i>]
#               = sum_i sign(lambda_i) * <psi_i|gamma_9|psi_i>
# This is equivalent to Tr(gamma_9 * sign(D_K)).
# By {gamma_9, D_K} = 0, this MUST be zero.

# Verification:
eta_spectral_weight = np.zeros(N_WALL)
for ix in range(N_WALL):
    for i in range(16):
        if abs(evals_wall[ix, i]) > 1e-12:
            eta_spectral_weight[ix] += np.sign(evals_wall[ix, i]) * chirality_wall[ix, i]

print(f"  Max |eta_spectral_weight| across wall: {np.max(np.abs(eta_spectral_weight)):.2e}")
print(f"  (Must be zero by {{gamma_9, D_K}} = 0)")

# The off-diagonal chiral eta (Callan-Harvey type):
# In the Callan-Harvey mechanism, the relevant quantity is NOT the diagonal eta
# but the BOUNDARY contribution from the APS index theorem.
# For a 1D wall, the index theorem gives:
#   index(D_wall) = (1/2)(eta(D_K(tau_+)) - eta(D_K(tau_-))) + integral terms
# Since eta(D_K) = 0 at both asymptotes, the boundary contribution vanishes.

print(f"\n  APS boundary contribution:")
print(f"    eta(D_K(tau_+)) = {eta_full[-1]:.0f}")
print(f"    eta(D_K(tau_-)) = {eta_full[0]:.0f}")
print(f"    (1/2)(eta_+ - eta_-) = {0.5*(eta_full[-1] - eta_full[0]):.0f}")


# ======================================================================
#  STEP 9: K_7-resolved chiral eta (the one quantity that MIGHT be nonzero)
# ======================================================================
print("\n--- Step 9: K_7-resolved chiral analysis ---")

# Within each K_7 sector, count eigenvalue asymmetry
# Since [iK_7, D_K] = 0, we can label states by K_7 charge
# Within K_7 = q sector: does chirality content vary across wall?

# Get K_7 charges at wall center
k7_center = k7_wall[N_WALL // 2]
unique_k7 = np.unique(np.round(k7_center, 4))
print(f"  K_7 charges at wall center: {unique_k7}")

# For each K_7 sector, compute chiral content variation
print(f"\n  K_7-chirality variation across wall:")
for q in unique_k7:
    mask_center = np.abs(k7_center - q) < 0.01
    n_states = np.sum(mask_center)
    if n_states == 0:
        continue

    chi_q = np.zeros(N_WALL)
    for ix in range(N_WALL):
        mask_ix = np.abs(k7_wall[ix] - q) < 0.01
        if np.sum(mask_ix) > 0:
            chi_q[ix] = np.mean(chirality_wall[ix, mask_ix])

    chi_var = np.max(chi_q) - np.min(chi_q)
    print(f"    q = {q:+.4f} ({n_states} states): <gamma_9> range = "
          f"[{np.min(chi_q):+.8f}, {np.max(chi_q):+.8f}], variation = {chi_var:.2e}")


# ======================================================================
#  STEP 10: The complete diagnostic — what CAN produce asymmetry
# ======================================================================
print("\n--- Step 10: Complete diagnostic ---")

# Summary of all computed quantities
max_eta_plus_minus_diff = np.max(np.abs(eta_plus_signed - eta_minus_signed))
max_eta_s1_diff = np.max(np.abs(eta_plus_s1 - eta_minus_s1))
max_eta_dominant_diff = np.max(np.abs(eta_dominant_plus - eta_dominant_minus))
max_eta_k7_chiral = np.max(np.abs(eta_k7_chiral))
max_berry_chiral = np.max(np.abs(berry_curvature_chiral))

print(f"  1. Tr(gamma_9 * sign(D_K)):       max|.| = {np.max(np.abs(eta_chiral_sign)):.2e}")
print(f"  2. eta_+^signed - eta_-^signed:    max|.| = {max_eta_plus_minus_diff:.2e}")
print(f"  3. eta_+^s1 - eta_-^s1:           max|.| = {max_eta_s1_diff:.2e}")
print(f"  4. eta_dom+ - eta_dom-:            max|.| = {max_eta_dominant_diff:.2e}")
print(f"  5. Tr(gamma_9 * iK_7 * sign(D_K)):max|.| = {max_eta_k7_chiral:.2e}")
print(f"  6. Chiral Berry curvature:         max|.| = {max_berry_chiral:.2e}")
print(f"  7. Integrated Berry curvature:     |int|  = {abs(integrated_chiral):.2e}")
print(f"  8. Spectral weight eta:            max|.| = {np.max(np.abs(eta_spectral_weight)):.2e}")
print(f"  9. D_wall anticomm error:                   {err_anticomm_wall:.2e}")
print(f"  10. Tr(gamma9_ext * sign(D_wall)):          {abs(tr_g9_signDwall):.2e}")

# The gate test
gate_quantities = {
    'eta_chiral_sign': np.max(np.abs(eta_chiral_sign)),
    'eta_plus_minus_diff': max_eta_plus_minus_diff,
    'eta_s1_diff': max_eta_s1_diff,
    'eta_dominant_diff': max_eta_dominant_diff,
    'eta_k7_chiral': max_eta_k7_chiral,
    'berry_chiral': max_berry_chiral,
    'D_wall_chiral': abs(tr_g9_signDwall),
}

# GATE: |eta_+ - eta_-| > 10^{-6}
# Test ALL candidate definitions
any_pass = False
for name, val in gate_quantities.items():
    if val > 1e-6:
        print(f"\n  {name} = {val:.6e} > 10^{{-6}}: NONZERO")
        any_pass = True


# ======================================================================
#  GATE VERDICT
# ======================================================================
print(f"\n{'='*78}")
print("GATE CHIRAL-ETA-43 VERDICT")
print(f"{'='*78}")

# The fundamental algebraic constraint:
# {gamma_9, D_K} = 0 => Tr(gamma_9 * f(D_K)) = 0 for any odd f
# This is a STRUCTURAL THEOREM, not a numerical accident.
#
# Consequence: ANY definition of "chiral eta" that computes
# Tr(gamma_9 * (odd function of D_K)) vanishes identically.
#
# The only escape routes are:
# 1. An operator that breaks {gamma_9, D_K} = 0 (e.g., interactions, anomaly)
# 2. A definition that involves even functions of D_K (but then it's not an eta)
# 3. Off-Jensen deformation where {gamma_9, D_K} might not hold
# 4. Spatial gradient terms in the wall operator that break chirality

# Check route 4: did the wall gradient break chirality?
if err_anticomm_wall > 1e-6:
    # The gradient DID break chirality
    if abs(tr_g9_signDwall) > 1e-6:
        verdict = "PASS"
        delta_eta_chiral = tr_g9_signDwall
        print(f"  Wall gradient breaks {{gamma_9, D_wall}} = 0")
        print(f"  Tr(gamma_9_ext * sign(D_wall)) = {tr_g9_signDwall:+.8e}")
        print(f"  |Delta eta_chiral| = {abs(delta_eta_chiral):.6e} > 10^{{-6}}")
        print(f"  VERDICT: PASS")
    else:
        verdict = "FAIL"
        print(f"  Wall gradient breaks {{gamma_9, D_wall}} = 0")
        print(f"  But Tr(gamma_9_ext * sign(D_wall)) = {tr_g9_signDwall:+.8e}")
        print(f"  Chirality breaking present but chiral eta still vanishes")
        print(f"  VERDICT: FAIL")
else:
    verdict = "FAIL"
    print(f"  STRUCTURAL THEOREM: {{gamma_9, D_K(tau)}} = 0 at EVERY tau.")
    print(f"  {{gamma_9, D_wall}} = 0 to precision {err_anticomm_wall:.2e}.")
    print(f"  CONSEQUENCE: Tr(gamma_9 * f(D_K)) = 0 for ANY odd function f.")
    print(f"  ALL definitions of chiral eta vanish by spectral pairing.")
    print(f"")
    print(f"  This is not a numerical result — it is algebraic.")
    print(f"  {gamma_9, D_K} = 0 follows from:")
    print(f"    - D_K built from Gamma_{{abc}} * gamma_a gamma_b gamma_c")
    print(f"    - gamma_9 = product of all 8 gammas")
    print(f"    - {{gamma_9, gamma_a}} = 0 for each a => gamma_9 anticommutes with any")
    print(f"      product of an ODD number of gamma matrices")
    print(f"    - D_K involves products of 1 and 3 gammas (both odd)")
    print(f"  Wall gradient preserves this structure because the gradient")
    print(f"  couples only the scalar (position) degree of freedom, not the")
    print(f"  spinor structure.")
    print(f"")
    print(f"  The chiral eta at the wall equals the chiral eta in the bulk: ZERO.")
    print(f"  No thermodynamic driving force for baryogenesis from this mechanism.")
    print(f"")
    print(f"  SURVIVING PATHS:")
    print(f"    1. Off-Jensen metric: {{gamma_9, D_K}} = 0 requires U(2) invariance.")
    print(f"       At a physical domain wall, the metric may not be exactly Jensen.")
    print(f"    2. Interaction terms: D_K + V where V has different gamma structure.")
    print(f"    3. Higher Peter-Weyl sectors (p+q > 0): our D_K is the (0,0) singlet.")
    print(f"       The full Dirac operator on L^2(SU(3)) includes all sectors.")
    print(f"       Off-diagonal coupling (from wall gradient in Peter-Weyl basis)")
    print(f"       could break spectral pairing between sectors.")
    print(f"")
    print(f"  VERDICT: FAIL")

# Also compute delta_eta_chiral for the record
if verdict == "PASS":
    pass  # already computed
else:
    delta_eta_chiral = 0.0

print(f"\n  Summary numbers:")
print(f"    max|eta_+ - eta_-| (signed)  = {max_eta_plus_minus_diff:.2e}")
print(f"    max|eta_+ - eta_-| (dominant)= {max_eta_dominant_diff:.2e}")
print(f"    max|Tr(g9*sign(D))|          = {np.max(np.abs(eta_chiral_sign)):.2e}")
print(f"    max|Tr(g9*K7*sign(D))|       = {max_eta_k7_chiral:.2e}")
print(f"    Tr(g9_ext * sign(D_wall))    = {tr_g9_signDwall:.2e}")
print(f"    max|chiral Berry curvature|  = {max_berry_chiral:.2e}")
print(f"    ||{{gamma9, D_wall}}||/||D_wall|| = {err_anticomm_wall:.2e}")

elapsed = time.time() - t0
print(f"\n  Elapsed: {elapsed:.1f}s")
print(f"  GATE: {verdict}")


# ======================================================================
#  Save data
# ======================================================================
npz_data = {
    'x_wall': x_wall,
    'tau_wall': tau_wall,
    'xi_BCS': XI_BCS,
    'delta_tau': DELTA_TAU,
    'tau_fold': TAU_FOLD,
    'evals_wall': evals_wall,
    'chirality_wall': chirality_wall,
    'weight_plus': weight_plus,
    'weight_minus': weight_minus,
    'k7_wall': k7_wall,
    'eta_full': eta_full,
    'eta_chiral_sign': eta_chiral_sign,
    'eta_plus_signed': eta_plus_signed,
    'eta_minus_signed': eta_minus_signed,
    'eta_dominant_plus': eta_dominant_plus,
    'eta_dominant_minus': eta_dominant_minus,
    'eta_plus_s1': eta_plus_s1,
    'eta_minus_s1': eta_minus_s1,
    'eta_k7_chiral': eta_k7_chiral,
    'eta_spectral_weight': eta_spectral_weight,
    'berry_phase': berry_phase,
    'berry_curvature_chiral': berry_curvature_chiral,
    'integrated_chiral': integrated_chiral,
    'dtau_dx': dtau_dx,
    'err_anticomm_wall': err_anticomm_wall,
    'tr_g9_signDwall': tr_g9_signDwall,
    'delta_eta_chiral': delta_eta_chiral,
    'g9_K7_relation': np.array(g9_K7_relation),
    'gate_quantities': np.array(list(gate_quantities.items()), dtype=object),
    'verdict': np.array(verdict),
}

outpath = os.path.join(SCRIPT_DIR, "s43_chiral_eta.npz")
np.savez_compressed(outpath, **npz_data)
print(f"\n  Saved: {outpath}")


# ======================================================================
#  Plot
# ======================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle(f"CHIRAL-ETA-43: Chiral Eta at Domain Wall  |  Verdict: {verdict}", fontsize=14)

# Panel 1: Wall profile
ax = axes[0, 0]
ax.plot(x_wall / XI_BCS, tau_wall, 'b-', lw=2)
ax.axhline(TAU_FOLD, color='red', ls='--', alpha=0.5, label=r'$\tau_{fold}$')
ax.set_xlabel(r'$x / \xi_{BCS}$')
ax.set_ylabel(r'$\tau(x)$')
ax.set_title('Domain Wall Profile')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: Eigenvalues across wall
ax = axes[0, 1]
for n in range(16):
    ax.plot(x_wall / XI_BCS, evals_wall[:, n], '-', alpha=0.6, lw=1)
ax.set_xlabel(r'$x / \xi_{BCS}$')
ax.set_ylabel(r'$\lambda_n(D_K)$')
ax.set_title(r'$D_K$ Eigenvalues Across Wall')
ax.grid(True, alpha=0.3)

# Panel 3: Chirality content
ax = axes[0, 2]
for n in range(16):
    color = 'blue' if chirality_wall[N_WALL//2, n] > 0 else 'red'
    ax.plot(x_wall / XI_BCS, chirality_wall[:, n], '-', color=color, alpha=0.5, lw=1)
ax.set_xlabel(r'$x / \xi_{BCS}$')
ax.set_ylabel(r'$\langle \psi_n | \gamma_9 | \psi_n \rangle$')
ax.set_title('Chirality of Eigenstates')
ax.grid(True, alpha=0.3)

# Panel 4: Chiral eta candidates
ax = axes[1, 0]
ax.plot(x_wall / XI_BCS, eta_chiral_sign, 'ko-', label=r'$\mathrm{Tr}(\gamma_9 \cdot \mathrm{sgn}(D_K))$', markersize=3)
ax.plot(x_wall / XI_BCS, eta_spectral_weight, 'rs-', label=r'$\sum_i \mathrm{sgn}(\lambda_i) \langle\gamma_9\rangle_i$', markersize=3)
ax.set_xlabel(r'$x / \xi_{BCS}$')
ax.set_ylabel('Chiral Eta')
ax.set_title('Chiral Eta Invariants (all zero by theorem)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: K_7-weighted chiral quantity
ax = axes[1, 1]
ax.plot(x_wall / XI_BCS, eta_k7_chiral, 'g^-', label=r'$\mathrm{Tr}(\gamma_9 \cdot iK_7 \cdot \mathrm{sgn}(D_K))$', markersize=4)
ax.plot(x_wall / XI_BCS, eta_k7_plus, 'b>-', label=r'$\eta_{K_7}^+$', markersize=3)
ax.plot(x_wall / XI_BCS, eta_k7_minus, 'r<-', label=r'$\eta_{K_7}^-$', markersize=3)
ax.set_xlabel(r'$x / \xi_{BCS}$')
ax.set_ylabel(r'$K_7$-weighted chiral eta')
ax.set_title(r'$K_7$-Weighted Chiral Quantities')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Berry curvature
ax = axes[1, 2]
ax.plot(x_wall / XI_BCS, berry_curvature_chiral, 'm-', lw=2, label='Chiral Berry curvature')
ax.fill_between(x_wall / XI_BCS, berry_curvature_chiral, alpha=0.3, color='magenta')
ax.set_xlabel(r'$x / \xi_{BCS}$')
ax.set_ylabel(r'$F_{chiral}(x)$')
ax.set_title(f'Chiral Berry Curvature (int = {integrated_chiral:+.2e})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(SCRIPT_DIR, "s43_chiral_eta.png")
plt.savefig(plotpath, dpi=150)
print(f"  Plot: {plotpath}")
print(f"\nDone.")
