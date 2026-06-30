#!/usr/bin/env python3
"""
s61_alpha_crit_conformal.py — ALPHA-CRIT-CONFORMAL-61
=====================================================

Gate: ALPHA-CRIT-CONFORMAL-61
  PASS if alpha_crit has conformal invariance origin
  FAIL if accidental (no geometric explanation)
  INFO if known geometric ratio but not conformal

Physics:
  The spectral action Hessian decomposes as H_SA = alpha * H_a2 + H_a4.
  PHONON-2 found alpha_crit = 52.39 (two-step: first crossing at 52.39,
  second at 54.75). This script decomposes the curvature invariants at the
  fold into the Penrose-Rindler irreducible parts of the Riemann tensor
  on the 8-manifold SU(3), and expresses alpha_crit as a ratio of these
  geometric invariants.

  On an n-dimensional Riemannian manifold, the Riemann tensor decomposes as:
    R_{abcd} = C_{abcd} + (2/(n-2))[g_{a[c}S_{d]b} - g_{b[c}S_{d]a}]
               + (2R/(n(n-1))) g_{a[c}g_{d]b}
  where:
    C_{abcd} = Weyl tensor (trace-free part)
    S_{ab} = R_{ab} - (R/n)*g_{ab}  (traceless Ricci tensor)
    R = scalar curvature

  The curvature invariants satisfy the identity (n dimensions):
    K = |C|^2 + (4/(n-2))|S|^2 + (2/(n(n-1)))R^2

  The Gilkey a_2 and a_4 for D_K^2 on (SU(3), g_Jensen) are:
    a_2 = P * (20R/3) * Vol          [P = (4*pi)^{-4}]
    a_4 = P * (1/360)(500R^2 - 32|Ric|^2 - 28K) * Vol

  Expressing a_4 in Penrose-Rindler components:
    |Ric|^2 = |S|^2 + R^2/n  (on n-dim manifold, n=8)
    K = |C|^2 + (4/(n-2))|S|^2 + (2/(n(n-1)))R^2

    => 500R^2 - 32|Ric|^2 - 28K
       = 500R^2 - 32(|S|^2 + R^2/8) - 28(|C|^2 + (2/3)|S|^2 + R^2/28)
       = 500R^2 - 4R^2 - 32|S|^2 - 28|C|^2 - (56/3)|S|^2 - R^2
       = 495R^2 - (152/3)|S|^2 - 28|C|^2

  The Hessian of the spectral action involves derivatives of these invariants
  with respect to the moduli. The key insight: H_a2 ~ d^2R/dq^2 (scalar only),
  while H_a4 ~ d^2(495R^2 - (152/3)|S|^2 - 28|C|^2)/dq^2 (all three sectors).

  alpha_crit is the ratio where alpha * H_a2_eigenvalue + H_a4_eigenvalue = 0
  for each eigendirection. This gives alpha_crit = -H_a4_eigenvalue / H_a2_eigenvalue.

  We compute this per-eigendirection and identify the geometric content.

Author: schwarzschild-penrose-geometer (Session 61)
Date: 2026-03-28
"""

import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import numpy as np
from numpy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI,
    a0_fold, a2_fold, a4_fold,
)

print("=" * 78)
print("  ALPHA-CRIT-CONFORMAL-61: Penrose-Rindler Decomposition of alpha_crit")
print("=" * 78)

t_start = time.time()

# =============================================================================
# 1. Load Input Data
# =============================================================================
print("\n--- 1. Loading input data ---")

d60 = np.load('s60_hessian_3d.npz', allow_pickle=True)
H_a2 = d60['H_a2']
H_a4 = d60['H_a4']
H_a0 = d60['H_a0']
evals_a2_60 = d60['evals_a2']
evals_a4_60 = d60['evals_a4']
evals_a0_60 = d60['evals_a0']

d61_a4 = np.load('s61_heat_kernel_a4.npz', allow_pickle=True)
R_fold = float(d61_a4['R_fold'])
Ric2_fold = float(d61_a4['Ric2_fold'])
K_fold = float(d61_a4['K_fold'])

print(f"  H_a2 eigenvalues (S60): {evals_a2_60}")
print(f"  H_a4 eigenvalues (S60): {evals_a4_60}")
print(f"  H_a0 eigenvalues (S60): {evals_a0_60}")
print(f"  R(fold) = {R_fold:.10f}")
print(f"  |Ric|^2(fold) = {Ric2_fold:.10f}")
print(f"  K(fold) = {K_fold:.10f}")

# =============================================================================
# 2. Penrose-Rindler Decomposition of Curvature at the Fold
# =============================================================================
print("\n--- 2. Penrose-Rindler decomposition (d=8) ---")

d = 8  # dimension of SU(3) manifold (local)

# Traceless Ricci: |S|^2 = |Ric|^2 - R^2/n
S2_fold = Ric2_fold - R_fold**2 / d
print(f"  |S|^2 = |Ric|^2 - R^2/{d} = {Ric2_fold:.10f} - {R_fold**2/d:.10f} = {S2_fold:.10f}")

# Weyl: K = |C|^2 + (4/(n-2))|S|^2 + (2/(n(n-1)))R^2
#    => |C|^2 = K - (4/(n-2))|S|^2 - (2/(n(n-1)))R^2
C2_fold = K_fold - (4.0/(d-2)) * S2_fold - (2.0/(d*(d-1))) * R_fold**2
print(f"  |C|^2 = K - (4/{d-2})|S|^2 - (2/{d*d-d})R^2")
print(f"        = {K_fold:.10f} - {(4.0/(d-2))*S2_fold:.10f} - {(2.0/(d*(d-1)))*R_fold**2:.10f}")
print(f"        = {C2_fold:.10f}")

# Cross-check: reconstruct K
K_check = C2_fold + (4.0/(d-2)) * S2_fold + (2.0/(d*(d-1))) * R_fold**2
print(f"\n  Cross-check: |C|^2 + (4/6)|S|^2 + (2/56)R^2 = {K_check:.10f}")
print(f"  K(fold) = {K_fold:.10f}")
print(f"  Error: {abs(K_check - K_fold):.2e}")

# Cross-check from memory: |C|^2(0.19) = 0.3859 (S33/S49)
print(f"\n  Memory check: |C|^2(0.19) ~ 0.386 from S49 (stored in MEMORY.md)")
print(f"  Computed: |C|^2 = {C2_fold:.6f}")

# =============================================================================
# 3. Exact Analytic Curvature Functions (for derivatives)
# =============================================================================
print("\n--- 3. Exact analytic curvature functions ---")


def R_scalar(s):
    """Exact scalar curvature R(s) on Jensen-deformed SU(3)."""
    return -0.25 * np.exp(-4*s) + 2.0 * np.exp(-s) - 0.25 + 0.5 * np.exp(2*s)


def Ric2_exact(s):
    """Exact |Ric|^2(s) = Ric_{ab}Ric^{ab} on Jensen SU(3)."""
    return (
        (1.0/12) * np.exp(-8*s)
        + (-1.0/2) * np.exp(-5*s)
        + (1.0/8) * np.exp(-4*s)
        + (13.0/12) * np.exp(-2*s)
        + (-1.0/2) * np.exp(-s)
        + 1.0/8
        + (1.0/12) * np.exp(4*s)
    )


def K_exact(s):
    """Exact Kretschner scalar K(s) = R_{abcd}R^{abcd} on Jensen SU(3)."""
    return (
        (23.0/96) * np.exp(-8*s)
        + (-1.0) * np.exp(-5*s)
        + (5.0/16) * np.exp(-4*s)
        + (11.0/6) * np.exp(-2*s)
        + (-3.0/2) * np.exp(-s)
        + 17.0/32
        + (1.0/12) * np.exp(4*s)
    )


def S2_exact(s):
    """Exact traceless Ricci squared |S|^2(s)."""
    return Ric2_exact(s) - R_scalar(s)**2 / d


def C2_exact(s):
    """Exact Weyl squared |C|^2(s) = K - (4/6)|S|^2 - (2/56)R^2."""
    return K_exact(s) - (4.0/(d-2)) * S2_exact(s) - (2.0/(d*(d-1))) * R_scalar(s)**2


# Verify at fold
print(f"  R(fold): analytic = {R_scalar(tau_fold):.10f}, data = {R_fold:.10f}")
print(f"  |S|^2(fold): analytic = {S2_exact(tau_fold):.10f}, decomp = {S2_fold:.10f}")
print(f"  |C|^2(fold): analytic = {C2_exact(tau_fold):.10f}, decomp = {C2_fold:.10f}")

# Verify at round (s=0): known values
R0 = R_scalar(0)
Ric2_0 = Ric2_exact(0)
K0 = K_exact(0)
S2_0 = S2_exact(0)
C2_0 = C2_exact(0)
print(f"\n  At round (s=0):")
print(f"    R = {R0:.10f} (expected 2.0)")
print(f"    |Ric|^2 = {Ric2_0:.10f} (expected 0.5)")
print(f"    K = {K0:.10f} (expected 0.5)")
print(f"    |S|^2 = {S2_0:.10f} (expected {0.5 - 4.0/8:.10f})")
print(f"    |C|^2 = {C2_0:.10f}")
# For round SU(3): Ric = (R/d)*g => S=0 => |C|^2 = K - (2R^2)/(d(d-1))
C2_round_exact = K0 - 2.0*R0**2/(d*(d-1))
print(f"    |C|^2 check (Einstein): K - 2R^2/(d(d-1)) = {C2_round_exact:.10f}")
# Check if round SU(3) is Einstein
print(f"    Round SU(3) Einstein check: |S|^2 = {S2_0:.6e} {'(YES)' if abs(S2_0) < 1e-10 else '(NO)'}")

# =============================================================================
# 4. a_4 in Penrose-Rindler Components
# =============================================================================
print("\n--- 4. a_4 in Penrose-Rindler components ---")

# a_4 integrand (inside the 1/360 factor):
#   500*R^2 - 32*|Ric|^2 - 28*K
#
# Express |Ric|^2 = |S|^2 + R^2/d, K = |C|^2 + (4/(d-2))|S|^2 + (2/(d(d-1)))R^2
#
# 500R^2 - 32(|S|^2 + R^2/d) - 28(|C|^2 + (4/(d-2))|S|^2 + (2/(d(d-1)))R^2)
# = 500R^2 - 32R^2/d - 32|S|^2 - 28|C|^2 - 112|S|^2/(d-2) - 56R^2/(d(d-1))
# = R^2[500 - 32/d - 56/(d(d-1))] - |S|^2[32 + 112/(d-2)] - 28|C|^2

coeff_R2 = 500.0 - 32.0/d - 56.0/(d*(d-1))
coeff_S2 = -(32.0 + 112.0/(d-2))
coeff_C2 = -28.0  # (local)

print(f"  Dimension d = {d}")
print(f"  a_4 integrand = coeff_R2 * R^2 + coeff_S2 * |S|^2 + coeff_C2 * |C|^2")
print(f"  coeff_R2 = 500 - 32/{d} - 56/({d}*{d-1}) = {coeff_R2:.10f}")
print(f"  coeff_S2 = -(32 + 112/{d-2}) = {coeff_S2:.10f}")
print(f"  coeff_C2 = {coeff_C2:.10f}")

# Verify: 500R^2 - 32|Ric|^2 - 28K should equal the PR decomposition
s = tau_fold
direct_combo = 500*R_scalar(s)**2 - 32*Ric2_exact(s) - 28*K_exact(s)
pr_combo = coeff_R2 * R_scalar(s)**2 + coeff_S2 * S2_exact(s) + coeff_C2 * C2_exact(s)
print(f"\n  At fold: direct = {direct_combo:.10f}, PR = {pr_combo:.10f}, err = {abs(direct_combo-pr_combo):.2e}")

# Numerical values at fold
R2_val = R_fold**2
S2_val = S2_fold
C2_val = C2_fold

a4_R2_term = coeff_R2 * R2_val
a4_S2_term = coeff_S2 * S2_val
a4_C2_term = coeff_C2 * C2_val
a4_total = a4_R2_term + a4_S2_term + a4_C2_term

print(f"\n  Penrose-Rindler decomposition of a_4 integrand at fold:")
print(f"    R^2 term:   {coeff_R2:.4f} * {R2_val:.6f} = {a4_R2_term:.6f}")
print(f"    |S|^2 term: {coeff_S2:.4f} * {S2_val:.6f} = {a4_S2_term:.6f}")
print(f"    |C|^2 term: {coeff_C2:.4f} * {C2_val:.6f} = {a4_C2_term:.6f}")
print(f"    Total: {a4_total:.6f}")
print(f"    Direct: {direct_combo:.6f}")

# Fractional contributions
print(f"\n  Fractional contributions to a_4 integrand:")
print(f"    Scalar (R^2):          {a4_R2_term/a4_total*100:.2f}%")
print(f"    Traceless Ricci (|S|^2): {a4_S2_term/a4_total*100:.2f}%")
print(f"    Weyl (|C|^2):          {a4_C2_term/a4_total*100:.2f}%")

# =============================================================================
# 5. Hessian Decomposition — Analytical Approach
# =============================================================================
print("\n--- 5. Hessian decomposition in Penrose-Rindler components ---")

# The spectral action S_SA = sum_{k=0}^{infty} a_{2k} * f_{2k} * Lambda^{d-2k}
# At leading orders:
#   S_SA ~ f_0 * Lambda^8 * a_0 + f_2 * Lambda^6 * a_2 + f_4 * Lambda^4 * a_4 + ...
# (We absorb the (4pi)^{-4} into the normalization.)
#
# The Hessian H_SA = d^2 S_SA / dq_i dq_j decomposes as:
#   H_SA = f_0 * Lambda^8 * H_a0 + f_2 * Lambda^6 * H_a2 + f_4 * Lambda^4 * H_a4 + ...
#
# S60 parametrized this as H_SA = alpha * H_a2 + H_a4 where alpha = (f_2/f_4) * Lambda^2.
# Actually, S60 wrote alpha = (f_2 * Lambda^2) / f_0. Let me re-read...
#
# From S60: "H_SA = alpha * H_a2 + H_a4" where the H's are the Hessians of the
# Seeley-DeWitt coefficients. The alpha is the weight of the a_2 Hessian relative
# to the a_4 Hessian. When alpha is large, a_2 dominates.
#
# The critical alpha is where the combined Hessian changes sign.
# For each eigendirection i:
#   alpha_crit(i) = -eval_a4(i) / eval_a2(i)
# (since H_a2 eigenvalues are negative and H_a4 eigenvalues are positive)

# First: diagonalize H_a2 and H_a4 together
print("  H_a2 (from S60):")
print(f"    {H_a2}")
print(f"    eigenvalues: {evals_a2_60}")

print(f"\n  H_a4 (from S60):")
print(f"    {H_a4}")
print(f"    eigenvalues: {evals_a4_60}")

# Per-eigendirection alpha_crit
# H_a2 and H_a4 are NOT necessarily simultaneously diagonalizable.
# The ACTUAL alpha_crit is when det(alpha * H_a2 + H_a4) = 0.
# Let's find it precisely by binary search.

print("\n--- 5a. Precise alpha_crit by binary search ---")

def hessian_signature(alpha):
    """Return (n_pos, n_neg, n_zero) for alpha*H_a2 + H_a4."""
    H = alpha * H_a2 + H_a4
    ev = np.linalg.eigvalsh(H)
    n_pos = np.sum(ev > 1e-10)
    n_neg = np.sum(ev < -1e-10)
    n_zero = 3 - n_pos - n_neg  # (local)
    return n_pos, n_neg, n_zero, ev

# Binary search for first crossing (3+,0-) -> (2+,1-) or (1+,2-)
alpha_lo, alpha_hi = 0.0, 200.0

# Verify signs at boundaries
sig_lo = hessian_signature(alpha_lo)
sig_hi = hessian_signature(alpha_hi)
print(f"  At alpha=0: eigenvalues = {sig_lo[3]}, signature = ({sig_lo[0]}+,{sig_lo[1]}-)")
print(f"  At alpha=200: eigenvalues = {sig_hi[3]}, signature = ({sig_hi[0]}+,{sig_hi[1]}-)")

# Find FIRST eigenvalue zero-crossing
# The smallest eigenvalue of alpha*H_a2 + H_a4 is a decreasing function of alpha
# (since H_a2 eigenvalues are all negative).
# We want the alpha where the smallest eigenvalue of H_combined crosses zero.

def min_eigenvalue(alpha):
    H = alpha * H_a2 + H_a4
    return np.min(np.linalg.eigvalsh(H))

# Binary search for first zero crossing
a_lo, a_hi = 0.0, 200.0
for _ in range(100):
    a_mid = (a_lo + a_hi) / 2
    if min_eigenvalue(a_mid) > 0:
        a_lo = a_mid
    else:
        a_hi = a_mid

alpha_crit_1 = (a_lo + a_hi) / 2
ev_crit_1 = np.linalg.eigvalsh(alpha_crit_1 * H_a2 + H_a4)
print(f"\n  alpha_crit_1 (first zero-crossing): {alpha_crit_1:.10f}")
print(f"  eigenvalues at crossing: {ev_crit_1}")

# Find SECOND zero-crossing (middle eigenvalue)
def mid_eigenvalue(alpha):
    H = alpha * H_a2 + H_a4
    ev = np.sort(np.linalg.eigvalsh(H))
    return ev[1]  # middle eigenvalue

a_lo2, a_hi2 = alpha_crit_1, 200.0
if mid_eigenvalue(a_lo2) > 0 and mid_eigenvalue(a_hi2) < 0:
    for _ in range(100):
        a_mid = (a_lo2 + a_hi2) / 2
        if mid_eigenvalue(a_mid) > 0:
            a_lo2 = a_mid
        else:
            a_hi2 = a_mid
    alpha_crit_2 = (a_lo2 + a_hi2) / 2
    ev_crit_2 = np.linalg.eigvalsh(alpha_crit_2 * H_a2 + H_a4)
    print(f"  alpha_crit_2 (second zero-crossing): {alpha_crit_2:.10f}")
    print(f"  eigenvalues at crossing: {ev_crit_2}")
else:
    alpha_crit_2 = None
    print(f"  No second zero-crossing found in [{alpha_crit_1:.2f}, 200]")

# Third crossing (largest eigenvalue)
def max_eigenvalue(alpha):
    return np.max(np.linalg.eigvalsh(alpha * H_a2 + H_a4))

a_lo3, a_hi3 = (alpha_crit_2 if alpha_crit_2 else alpha_crit_1), 200.0
if max_eigenvalue(a_lo3) > 0 and max_eigenvalue(a_hi3) < 0:
    for _ in range(100):
        a_mid = (a_lo3 + a_hi3) / 2
        if max_eigenvalue(a_mid) > 0:
            a_lo3 = a_mid
        else:
            a_hi3 = a_mid
    alpha_crit_3 = (a_lo3 + a_hi3) / 2
    ev_crit_3 = np.linalg.eigvalsh(alpha_crit_3 * H_a2 + H_a4)
    print(f"  alpha_crit_3 (third zero-crossing): {alpha_crit_3:.10f}")
    print(f"  eigenvalues at crossing: {ev_crit_3}")
else:
    alpha_crit_3 = None
    print(f"  No third zero-crossing found")

# =============================================================================
# 6. Eigendirection Analysis at alpha_crit
# =============================================================================
print("\n--- 6. Eigendirection analysis at alpha_crit ---")

# At alpha_crit_1, find the null eigenvector
H_crit = alpha_crit_1 * H_a2 + H_a4
ev_crit, evec_crit = np.linalg.eigh(H_crit)
null_idx = np.argmin(np.abs(ev_crit))
null_vec = evec_crit[:, null_idx]
print(f"  Null eigenvector at alpha_crit_1: {null_vec}")
print(f"  Null eigenvalue: {ev_crit[null_idx]:.6e}")

# Compute the ratio along this direction:
# alpha_crit = -<v|H_a4|v> / <v|H_a2|v>
ratio_v1 = -(null_vec @ H_a4 @ null_vec) / (null_vec @ H_a2 @ null_vec)
print(f"  Rayleigh quotient: -<v|H_a4|v>/<v|H_a2|v> = {ratio_v1:.10f}")
print(f"  alpha_crit_1 = {alpha_crit_1:.10f}")
print(f"  Match: {abs(ratio_v1 - alpha_crit_1):.2e}")

# Eigendirection labels: tau, sigma, delta_1
print(f"\n  Null eigenvector components: tau={null_vec[0]:.6f}, sigma={null_vec[1]:.6f}, delta1={null_vec[2]:.6f}")
print(f"  Dominant direction: {'tau' if abs(null_vec[0]) > abs(null_vec[1]) and abs(null_vec[0]) > abs(null_vec[2]) else 'sigma' if abs(null_vec[1]) > abs(null_vec[2]) else 'delta1'}")

# If H_a2, H_a4 were simultaneously diagonalizable, alpha_crit would be
# min_i(-eval_a4_i / eval_a2_i). Check if they approximately commute.
commutator = H_a2 @ H_a4 - H_a4 @ H_a2
comm_norm = np.linalg.norm(commutator, 'fro')
ha2_norm = np.linalg.norm(H_a2, 'fro')
ha4_norm = np.linalg.norm(H_a4, 'fro')
relative_comm = comm_norm / (ha2_norm * ha4_norm)
print(f"\n  [H_a2, H_a4] Frobenius norm: {comm_norm:.6e}")
print(f"  Relative commutator: {relative_comm:.6e}")
print(f"  Simultaneous diagonalizability: {'APPROXIMATE' if relative_comm < 0.01 else 'NO'}")

# If approximate: compute per-eigendirection ratios
# Diagonalize H_a2, project H_a4 onto those eigenvectors
ev_a2, U_a2 = np.linalg.eigh(H_a2)
H_a4_in_a2_basis = U_a2.T @ H_a4 @ U_a2
print(f"\n  H_a2 eigenvalues: {ev_a2}")
print(f"  H_a4 in H_a2 eigenbasis (diagonal elements): {np.diag(H_a4_in_a2_basis)}")
print(f"  H_a4 off-diagonal (normalized): {H_a4_in_a2_basis[0,1]/(abs(H_a4_in_a2_basis[0,0]*H_a4_in_a2_basis[1,1])**0.5):.6f}")

# Per-direction alpha_crit if they were simultaneously diagonal:
for i in range(3):
    ratio_i = -H_a4_in_a2_basis[i,i] / ev_a2[i]
    print(f"  Direction {i}: -H_a4_ii/H_a2_i = {ratio_i:.6f}")

# =============================================================================
# 7. Analytical Decomposition of Hessians
# =============================================================================
print("\n--- 7. Analytical Hessian construction from curvature invariants ---")

# The Hessians H_a2 and H_a4 are second derivatives of the Gilkey coefficients
# along the moduli directions. Since a_2 and a_4 are expressed in terms of
# R(s), |Ric|^2(s), K(s) (all exact analytic functions), we can compute their
# Hessians analytically.
#
# a_2 = P * (20R/3) * Vol  =>  H_a2 = P * (20/3) * Vol * d^2R/dq^2
# (Vol is constant on volume-preserving subspace)
#
# a_4 = P * (1/360) * (500R^2 - 32|Ric|^2 - 28K) * Vol
# = P * (1/360) * (coeff_R2 * R^2 + coeff_S2 * |S|^2 + coeff_C2 * |C|^2) * Vol
#
# The 3D moduli are (tau, sigma, delta_1) on the volume-preserving + off-Jensen surface.
# On the Jensen line (sigma=0, delta_1=0), only tau is active.
# The Hessian involves d^2/dtau^2, d^2/dsigma^2, d^2/ddelta1^2, and cross terms.

# For the on-Jensen (sigma=0, delta_1=0) restriction,
# the curvature invariants are functions of tau only.
# The Hessian along tau is just f''(tau_fold).
# The off-Jensen directions require the metric parametrization.

# Let's focus on what we CAN do analytically: the tau-tau component.
# Then compare with the numerical Hessian.

# Second derivatives of curvature invariants along tau
h = 1e-6  # step for numerical second derivative (verification)

def d2f_ds2(f, s, h=1e-6):
    """Numerical second derivative using central differences."""
    return (f(s+h) - 2*f(s) + f(s-h)) / h**2


# Exact analytic second derivatives
def dR_ds(s):
    """dR/ds."""
    return np.exp(-4*s) + (-2.0)*np.exp(-s) + np.exp(2*s)

def d2R_ds2(s):
    """d^2R/ds^2."""
    return (-4)*np.exp(-4*s) + 2.0*np.exp(-s) + 2*np.exp(2*s)

def d2R2_ds2(s):
    """d^2(R^2)/ds^2 = 2*(dR/ds)^2 + 2*R*d^2R/ds^2."""
    R = R_scalar(s)
    dR = dR_ds(s)
    d2R = d2R_ds2(s)
    return 2*dR**2 + 2*R*d2R

# For |Ric|^2 and K: use their exact formulas
def dRic2_ds(s):
    """d|Ric|^2/ds via exact derivative of the exponential sum."""
    return (
        (1.0/12)*(-8)*np.exp(-8*s)
        + (-1.0/2)*(-5)*np.exp(-5*s)
        + (1.0/8)*(-4)*np.exp(-4*s)
        + (13.0/12)*(-2)*np.exp(-2*s)
        + (-1.0/2)*(-1)*np.exp(-s)
        + (1.0/12)*(4)*np.exp(4*s)
    )

def d2Ric2_ds2(s):
    """d^2|Ric|^2/ds^2."""
    return (
        (1.0/12)*(64)*np.exp(-8*s)
        + (-1.0/2)*(25)*np.exp(-5*s)
        + (1.0/8)*(16)*np.exp(-4*s)
        + (13.0/12)*(4)*np.exp(-2*s)
        + (-1.0/2)*(1)*np.exp(-s)
        + (1.0/12)*(16)*np.exp(4*s)
    )

def dK_ds(s):
    """dK/ds via exact derivative."""
    return (
        (23.0/96)*(-8)*np.exp(-8*s)
        + (-1.0)*(- 5)*np.exp(-5*s)
        + (5.0/16)*(-4)*np.exp(-4*s)
        + (11.0/6)*(-2)*np.exp(-2*s)
        + (-3.0/2)*(-1)*np.exp(-s)
        + (1.0/12)*(4)*np.exp(4*s)
    )

def d2K_ds2(s):
    """d^2K/ds^2."""
    return (
        (23.0/96)*(64)*np.exp(-8*s)
        + (-1.0)*(25)*np.exp(-5*s)
        + (5.0/16)*(16)*np.exp(-4*s)
        + (11.0/6)*(4)*np.exp(-2*s)
        + (-3.0/2)*(1)*np.exp(-s)
        + (1.0/12)*(16)*np.exp(4*s)
    )

# Verify numerical vs analytic second derivatives at fold
print(f"  d^2R/ds^2 at fold: analytic={d2R_ds2(tau_fold):.10f}, numerical={d2f_ds2(R_scalar, tau_fold):.10f}")
print(f"  d^2|Ric|^2/ds^2:  analytic={d2Ric2_ds2(tau_fold):.10f}, numerical={d2f_ds2(Ric2_exact, tau_fold):.10f}")
print(f"  d^2K/ds^2:         analytic={d2K_ds2(tau_fold):.10f}, numerical={d2f_ds2(K_exact, tau_fold):.10f}")

# The tau-tau component of H_a4 should be proportional to:
#   d^2/ds^2 [500*R^2 - 32*|Ric|^2 - 28*K] at s=tau_fold
# times (P/360)*Vol
combo_d2 = 500*d2R2_ds2(tau_fold) - 32*d2Ric2_ds2(tau_fold) - 28*d2K_ds2(tau_fold)
print(f"\n  d^2/ds^2(500R^2 - 32|Ric|^2 - 28K) at fold = {combo_d2:.6f}")

# The tau-tau of H_a2 should be proportional to d^2R/ds^2 * (20/3)
# times P*Vol
R_d2 = d2R_ds2(tau_fold)
print(f"  d^2R/ds^2 at fold = {R_d2:.10f}")

# =============================================================================
# 8. alpha_crit Along the Jensen Line (tau-tau component)
# =============================================================================
print("\n--- 8. alpha_crit along the Jensen line (tau-tau) ---")

# If we restrict to tau deformations only (1D), the Hessian reduces to scalars.
# alpha_crit(tau) = -(d^2 a_4 / dtau^2) / (d^2 a_2 / dtau^2)
# The prefactors (P * Vol / 360 for a_4, P * Vol for a_2) ratio gives:
# alpha_crit(tau) = -(1/360) * combo_d2 / ((20/3) * R_d2)
# = -combo_d2 / (360 * (20/3) * R_d2)
# = -combo_d2 / (2400 * R_d2)

alpha_crit_tau = -combo_d2 / (2400.0 * R_d2)
print(f"  alpha_crit(tau-only, analytic) = {alpha_crit_tau:.10f}")

# Compare with numerical: -H_a4[0,0] / H_a2[0,0]
alpha_crit_tau_num = -H_a4[0,0] / H_a2[0,0]
print(f"  alpha_crit(tau-only, numerical) = -H_a4[0,0]/H_a2[0,0] = {alpha_crit_tau_num:.10f}")

# =============================================================================
# 9. Penrose-Rindler Decomposition of alpha_crit
# =============================================================================
print("\n--- 9. Penrose-Rindler decomposition of alpha_crit ---")

# Express alpha_crit in terms of the PR curvature components.
# The a_4 integrand in PR form: coeff_R2 * R^2 + coeff_S2 * |S|^2 + coeff_C2 * |C|^2
# Its second derivative at the fold:
d2_R2 = d2R2_ds2(tau_fold)
d2_S2 = d2f_ds2(S2_exact, tau_fold)
d2_C2 = d2f_ds2(C2_exact, tau_fold)

# Verify
combo_d2_PR = coeff_R2 * d2_R2 + coeff_S2 * d2_S2 + coeff_C2 * d2_C2
print(f"  d^2(a_4 integrand)/ds^2 = {combo_d2:.6f} (direct)")
print(f"  d^2(a_4 integrand)/ds^2 = {combo_d2_PR:.6f} (PR)")
print(f"  Error: {abs(combo_d2 - combo_d2_PR):.2e}")

# Components
print(f"\n  d^2(R^2)/ds^2 at fold = {d2_R2:.10f}")
print(f"  d^2(|S|^2)/ds^2 at fold = {d2_S2:.10f}")
print(f"  d^2(|C|^2)/ds^2 at fold = {d2_C2:.10f}")
print(f"  d^2R/ds^2 at fold = {R_d2:.10f}")

# PR contributions to alpha_crit (tau direction):
# alpha_crit = -(1/2400) * [coeff_R2 * d2(R^2)/ds^2 + coeff_S2 * d2(|S|^2)/ds^2 + coeff_C2 * d2(|C|^2)/ds^2]
#              / [d^2R/ds^2]
term_R2 = coeff_R2 * d2_R2 / (2400 * (-R_d2))
term_S2 = coeff_S2 * d2_S2 / (2400 * (-R_d2))
term_C2 = coeff_C2 * d2_C2 / (2400 * (-R_d2))

print(f"\n  alpha_crit = (scalar R^2 term) + (traceless Ricci term) + (Weyl term)")
print(f"  Scalar R^2 contribution:    {term_R2:.10f} ({term_R2/alpha_crit_tau*100:.2f}%)")
print(f"  Traceless Ricci contribution: {term_S2:.10f} ({term_S2/alpha_crit_tau*100:.2f}%)")
print(f"  Weyl contribution:           {term_C2:.10f} ({term_C2/alpha_crit_tau*100:.2f}%)")
print(f"  Sum:                          {term_R2+term_S2+term_C2:.10f}")
print(f"  alpha_crit(tau):              {alpha_crit_tau:.10f}")

# =============================================================================
# 10. Full 3D alpha_crit: Conformal Invariant Test
# =============================================================================
print("\n--- 10. Full 3D alpha_crit: geometric ratio identification ---")

# The full 3D alpha_crit (52.39) is determined by the combined Hessian problem.
# Let's express it as a ratio of curvature invariants.

# Approach 1: Direct ratio of traces
tr_H_a4 = np.trace(H_a4)
tr_H_a2 = np.trace(H_a2)
alpha_trace_ratio = -tr_H_a4 / tr_H_a2
print(f"  Trace ratio: -Tr(H_a4)/Tr(H_a2) = {alpha_trace_ratio:.10f}")

# Approach 2: Determinant ratio
det_H_a4 = np.linalg.det(H_a4)
det_H_a2 = np.linalg.det(H_a2)
alpha_det_ratio = (-det_H_a4 / det_H_a2)**(1.0/3)
print(f"  Determinant ratio: (-det(H_a4)/det(H_a2))^{1/3} = {alpha_det_ratio:.10f}")

# Approach 3: Spectral ratios (eigenvalue-by-eigenvalue)
ev_a2_sort = np.sort(evals_a2_60)  # sorted ascending (most negative first)
ev_a4_sort = np.sort(evals_a4_60)  # sorted ascending

print(f"\n  Per-eigenvalue alpha_crit ratios:")
for i in range(3):
    r = -ev_a4_sort[i] / ev_a2_sort[i]
    print(f"    Mode {i}: -eig_a4[{i}]/eig_a2[{i}] = -{ev_a4_sort[i]:.4f}/{ev_a2_sort[i]:.4f} = {r:.6f}")

# But the ACTUAL alpha_crit from binary search is different because the matrices
# are not simultaneously diagonal. The actual crossing depends on the GENERALIZED
# eigenvalue problem: H_a4 * v = -alpha * H_a2 * v
# i.e., find eigenvalues of H_a2^{-1} H_a4 (the alpha values where eigvals cross zero)

# Since H_a2 is negative definite, -H_a2 is positive definite.
# alpha_crit values are eigenvalues of (-H_a2)^{-1} H_a4 = -H_a2^{-1} H_a4
gen_ev = np.linalg.eigvalsh(np.linalg.solve(-H_a2, H_a4))
# Actually for generalized: H_a4 v = alpha (-H_a2) v
# Use scipy for proper generalized eigenvalue problem
from scipy.linalg import eigh as scipy_eigh
gen_alpha, gen_vecs = scipy_eigh(H_a4, -H_a2)

print(f"\n  Generalized eigenvalues (alpha_crit per mode):")
for i in range(3):
    print(f"    Mode {i}: alpha_crit = {gen_alpha[i]:.10f}, eigvec = {gen_vecs[:,i]}")

print(f"\n  These are the EXACT alpha values where each mode crosses zero:")
print(f"    First crossing (fold destabilizes): alpha = {gen_alpha[0]:.10f}")
print(f"    Second crossing: alpha = {gen_alpha[1]:.10f}")
print(f"    Third crossing: alpha = {gen_alpha[2]:.10f}")
print(f"  Compare PHONON-2: alpha_crit_1 = 52.39, alpha_crit_2 = 54.75")
print(f"  Compare binary search: alpha_crit_1 = {alpha_crit_1:.10f}")

# =============================================================================
# 11. Express alpha_crit as Dimensionless Geometric Ratios
# =============================================================================
print("\n--- 11. Dimensionless geometric ratio identification ---")

# The key question: is alpha_crit_1 a ratio of curvature invariants?
# On a d-dimensional manifold with known R, |S|^2, |C|^2, the dimensionless
# ratios available are:
#   R^2/K, |C|^2/K, |S|^2/K, d*(d-1)/2 (dimension), etc.

# Curvature ratios at the fold
R2_over_K = R_fold**2 / K_fold
C2_over_K = C2_fold / K_fold
S2_over_K = S2_fold / K_fold
R2_over_Ric2 = R_fold**2 / Ric2_fold
C2_over_R2 = C2_fold / R_fold**2
C2_over_Ric2 = C2_fold / Ric2_fold

print(f"  R^2/K = {R2_over_K:.10f}")
print(f"  |C|^2/K = {C2_over_K:.10f}")
print(f"  |S|^2/K = {S2_over_K:.10f}")
print(f"  R^2/|Ric|^2 = {R2_over_Ric2:.10f}")
print(f"  |C|^2/R^2 = {C2_over_R2:.10f}")
print(f"  |C|^2/|Ric|^2 = {C2_over_Ric2:.10f}")

# Dimension-dependent constants in the a_4 formula
print(f"\n  Dimension-dependent constants (d={d}):")
print(f"    coeff_R2 = {coeff_R2:.6f}")
print(f"    coeff_S2 = {coeff_S2:.6f}")
print(f"    coeff_C2 = {coeff_C2:.6f}")
print(f"    dim_spinor = 2^(d/2) = {2**(d//2)}")

# Key: alpha_crit involves SECOND DERIVATIVES, not just the curvature values.
# So we need ratios of second derivatives.

# The tau-only alpha_crit involves:
# alpha_crit = -(d^2/ds^2 [coeff_R2*R^2 + coeff_S2*|S|^2 + coeff_C2*|C|^2])
#              / (2400 * d^2R/ds^2)
# = -(coeff_R2 * d^2(R^2)/ds^2 + coeff_S2 * d^2|S|^2/ds^2 + coeff_C2 * d^2|C|^2/ds^2)
#   / (2400 * d^2R/ds^2)

# Factor out R_fold^2 from d^2(R^2)/ds^2 etc. to get dimensionless form:
# d^2(R^2)/ds^2 = 2(dR/ds)^2 + 2*R*d^2R/ds^2 at fold

dR = dR_ds(tau_fold)
d2R = d2R_ds2(tau_fold)
R_f = R_scalar(tau_fold)

print(f"\n  At fold:")
print(f"    R = {R_f:.10f}")
print(f"    dR/ds = {dR:.10f}")
print(f"    d^2R/ds^2 = {d2R:.10f}")
print(f"    (dR/ds)^2 / R^2 = {dR**2/R_f**2:.10f}")
print(f"    (d^2R/ds^2) / R = {d2R/R_f:.10f}")

# Express alpha_crit in a revealing form
# The 2400 = 360 * (20/3)
# So alpha_crit(tau) = -(1/360) * d^2(a_4_integrand)/ds^2 / ((20/3)*d^2R/ds^2)
# = -(a_4_integrand'') / (360 * (20/3) * R'')

# For an EINSTEIN manifold (|S|^2 = 0), this simplifies:
print(f"\n  Einstein manifold test:")
print(f"    |S|^2 at fold = {S2_fold:.10f}")
print(f"    |S|^2 / |Ric|^2 = {S2_fold/Ric2_fold:.6f}")
# If |S|^2 is small, the S2 contribution to alpha_crit is also small.

# =============================================================================
# 12. Conformal Invariant Structure of alpha_crit
# =============================================================================
print("\n--- 12. Conformal invariant structure ---")

# The a_4 integrand in terms of conformal invariants:
# The Weyl tensor |C|^2 is a conformal invariant (in 4D, not in 8D without weight).
# The Q-curvature would be more natural in higher dimensions.
# For the 8D Gilkey formula, the key combination is:
#   a_4 = (P/360)(500R^2 - 32|Ric|^2 - 28K) * Vol
#
# In the Penrose-Rindler decomposition:
#   = (P/360)(coeff_R2 * R^2 + coeff_S2 * |S|^2 + coeff_C2 * |C|^2) * Vol
#
# The conformal part is the |C|^2 piece.
# The NON-conformal parts are R^2 (scalar) and |S|^2 (traceless Ricci).
# In 4D, the combination 5R^2 - 2|Ric|^2 + 2K (with dim_S=4) gives
#   = conformal part + topological part (Euler density) + total derivative.
# In 8D, no such clean separation into conformal + topological exists generically.

# However, alpha_crit IS a geometric ratio. Express it purely in terms of
# curvature invariants and their flow derivatives.

# The alpha_crit from generalized eigenvalues is:
alpha_crit_full = gen_alpha[0]
print(f"  alpha_crit (full 3D, first crossing) = {alpha_crit_full:.10f}")

# Can we express this as a simple combination of d, R, |S|^2, |C|^2?
# Test various combinations:
candidates = {
    "500*R^2/(28*K)": 500*R_fold**2 / (28*K_fold),
    "|coeff_R2|*R^2/(|coeff_C2|*|C|^2)": abs(coeff_R2)*R_fold**2 / (abs(coeff_C2)*C2_fold),
    "(coeff_R2*R^2 - coeff_S2*|S|^2)/(|coeff_C2|*|C|^2)": (coeff_R2*R_fold**2 + coeff_S2*S2_fold) / (abs(coeff_C2)*C2_fold),
    "d*(d-1)*R^2/(4*K)": d*(d-1)*R_fold**2 / (4*K_fold),
    "(500R^2-32*|Ric|^2)/(28*K)": (500*R_fold**2 - 32*Ric2_fold) / (28*K_fold),
    "7*R^2/|C|^2": 7*R_fold**2/C2_fold,
    "20*R^2/(3*|C|^2)": 20*R_fold**2/(3*C2_fold),
    "a_4_integrand/(2400*R)": (500*R_fold**2 - 32*Ric2_fold - 28*K_fold) / (2400*R_fold),
}

print(f"\n  Candidate geometric ratios vs alpha_crit = {alpha_crit_full:.6f}:")
for name, val in candidates.items():
    pct_diff = (val - alpha_crit_full) / alpha_crit_full * 100
    print(f"    {name} = {val:.6f}  ({pct_diff:+.2f}%)")

# =============================================================================
# 13. Deep Analysis: Ratio of Hessian Structures
# =============================================================================
print("\n--- 13. Deep analysis: structure of the generalized eigenvalue ---")

# The generalized eigenvalue problem H_a4 v = alpha (-H_a2) v
# gives alpha_crit as eigenvalues of (-H_a2)^{-1} H_a4.
#
# Now, H_a2 = P * Vol * (20/3) * [d^2R/dq_i dq_j]
# and   H_a4 = P * Vol * (1/360) * [d^2(500R^2 - 32|Ric|^2 - 28K)/dq_i dq_j]
#
# Therefore (-H_a2)^{-1} H_a4 = -(1/360) * (3/20) * [d^2R/dq]^{-1} * [d^2 combo/dq]
# = -(1/2400) * [d^2R/dq]^{-1} * [d^2 combo/dq]
#
# alpha_crit = eigenvalue of (-1/2400) * [d^2R]^{-1} * [d^2 combo]

# Construct the analytic ratio matrix for the tau-tau component
# For the full 3D, we need the off-Jensen metric parametrization.
# But we can check: is the (0,0) entry of [d^2R]^{-1}*[d^2 combo] = alpha_crit_tau * 2400?

# We have H_a2 and H_a4 from S60. Compute the ratio matrix.
# H_a2 = P*Vol*(20/3) * H_R   where H_R = d^2R/dq_i dq_j
# H_a4 = P*Vol*(1/360) * H_combo where H_combo = d^2(500R^2-32|Ric|^2-28K)/dq

# Therefore: H_a4 / H_a2 (as a matrix equation) involves:
# (-H_a2)^{-1} H_a4 = -(3/(20*360)) * H_R^{-1} * H_combo = -(1/2400) * H_R^{-1} * H_combo

# H_R = H_a2 / (P*Vol*(20/3))
# H_combo = H_a4 / (P*Vol*(1/360))

# So ratio matrix = -(1/2400) * [H_a2/(P*Vol*20/3)]^{-1} * [H_a4/(P*Vol/360)]
# = -(1/2400) * (20/3)(P*Vol) * H_a2^{-1} * (1/360)(P*Vol)^{-1} H_a4  -- this is circular
# Actually:  let A = H_a2, B = H_a4. Then:
#   A = P*Vol*(20/3)*H_R,  B = P*Vol*(1/360)*H_combo
#   (-A)^{-1} B = -(P*Vol*20/3)^{-1} H_R^{-1} * P*Vol*(1/360)*H_combo
#              = -(1/2400) H_R^{-1} H_combo
# eigenvalues of (-A)^{-1}B = eigenvalues of -(1/2400) H_R^{-1} H_combo
# So alpha_crit = -(1/2400) * eigenvalue of (H_R^{-1} H_combo)

ratio_matrix = np.linalg.solve(-H_a2, H_a4)  # = (-H_a2)^{-1} H_a4
ev_ratio = np.linalg.eigvals(ratio_matrix)
print(f"  Eigenvalues of (-H_a2)^{{-1}} H_a4: {np.sort(np.real(ev_ratio))}")
print(f"  Compare generalized eigenvalues: {gen_alpha}")

# The ratio matrix eigenvalues should equal gen_alpha
print(f"  Match: {np.allclose(np.sort(np.real(ev_ratio)), np.sort(gen_alpha), rtol=1e-6)}")

# =============================================================================
# 14. Tau-sweep of alpha_crit(tau)
# =============================================================================
print("\n--- 14. Tau-sweep of generalized alpha_crit ---")

# Along the Jensen line, the Hessians are functions of tau.
# H_a2(tau) = P*Vol*(20/3)*d^2R/ds^2(tau) [tau-tau component]
# H_a4(tau) = P*Vol*(1/360)*d^2(combo)/ds^2(tau)
# alpha_crit(tau) = -H_a4(tau)/H_a2(tau) = -d^2(combo)/ds^2 / (2400*d^2R/ds^2)

tau_sweep = np.linspace(0.0, 0.5, 200)
alpha_crit_vs_tau = np.zeros_like(tau_sweep)

for i, s in enumerate(tau_sweep):
    d2R_s = d2R_ds2(s)
    d2_combo = (500*d2R2_ds2(s) - 32*d2Ric2_ds2(s) - 28*d2K_ds2(s))
    if abs(d2R_s) > 1e-15:
        alpha_crit_vs_tau[i] = -d2_combo / (2400.0 * d2R_s)
    else:
        alpha_crit_vs_tau[i] = np.nan

print(f"  alpha_crit(tau=0) = {alpha_crit_vs_tau[0]:.10f}")
print(f"  alpha_crit(tau=fold) = {alpha_crit_vs_tau[np.argmin(np.abs(tau_sweep-tau_fold))]:.10f}")

# Check at round: all curvature invariants are determined by the Einstein condition
print(f"\n  At round (s=0):")
R0 = R_scalar(0)
Ric2_0 = Ric2_exact(0)
K0 = K_exact(0)
S2_0_check = Ric2_0 - R0**2/d
C2_0_check = K0 - (4.0/(d-2))*S2_0_check - (2.0/(d*(d-1)))*R0**2
combo_0 = 500*R0**2 - 32*Ric2_0 - 28*K0
print(f"    R={R0}, |Ric|^2={Ric2_0}, K={K0}, |S|^2={S2_0_check:.6e}, |C|^2={C2_0_check:.10f}")
print(f"    a_4 integrand = {combo_0:.6f}")
print(f"    a_4 integrand / (2400 * R) = {combo_0/(2400*R0):.10f}")

# The round SU(3) is Einstein: R_{ab} = (R/d)*g_{ab}, so |S|^2 = 0
# and K = |C|^2 + 2R^2/(d(d-1))
# Check what alpha_crit becomes on an Einstein space:
# a_4_integrand = coeff_R2*R^2 + 0 + coeff_C2*|C|^2
# = coeff_R2*R^2 + coeff_C2*(K - 2R^2/(d(d-1)))
# = coeff_R2*R^2 + coeff_C2*K - coeff_C2*2R^2/(d(d-1))
# = [coeff_R2 - 28*2/(d(d-1))]*R^2 + coeff_C2*K
# = [coeff_R2 - R^2/d(d-1)]*R^2 + coeff_C2*K
# For round SU(3): this is all constant, so d^2/ds^2 at s=0 is meaningful
# only through the FLOW of the deformation away from Einstein.

# =============================================================================
# 15. Structural Formula for alpha_crit
# =============================================================================
print("\n--- 15. Structural formula identification ---")

# Let's define normalized curvature responses:
# rho_R = (d^2R/ds^2) / R  (scalar curvature response)
# rho_K = (d^2K/ds^2) / K  (Kretschner response)
# rho_Ric = (d^2|Ric|^2/ds^2) / |Ric|^2  (Ricci-squared response)
# Then alpha_crit(tau) = -(500*(2*eta^2 + rho_R)*R - 32*rho_Ric*|Ric|^2 - 28*rho_K*K)
#                        / (2400 * rho_R * R)
# where eta = (dR/ds)/(d^2R/ds^2)^{1/2} * something...

# Simpler: just express alpha_crit directly.
# alpha_crit = -[500*d^2(R^2) - 32*d^2|Ric|^2 - 28*d^2K] / (2400*d^2R)

# At the fold:
num = -(500*d2R2_ds2(tau_fold) - 32*d2Ric2_ds2(tau_fold) - 28*d2K_ds2(tau_fold))
den = 2400*d2R_ds2(tau_fold)
print(f"  Numerator: {num:.10f}")
print(f"  Denominator: {den:.10f}")
print(f"  alpha_crit(tau) = {num/den:.10f}")

# Break numerator into pieces
piece_R2 = 500*d2R2_ds2(tau_fold)
piece_Ric2 = -32*d2Ric2_ds2(tau_fold)
piece_K = -28*d2K_ds2(tau_fold)
total_num = piece_R2 + piece_Ric2 + piece_K

print(f"\n  Numerator decomposition:")
print(f"    500*d^2(R^2)/ds^2 = {piece_R2:.6f} ({piece_R2/total_num*100:.2f}%)")
print(f"    -32*d^2|Ric|^2/ds^2 = {piece_Ric2:.6f} ({piece_Ric2/total_num*100:.2f}%)")
print(f"    -28*d^2K/ds^2 = {piece_K:.6f} ({piece_K/total_num*100:.2f}%)")
print(f"    Total: {total_num:.6f}")

# Now express d^2(R^2)/ds^2 = 2(dR/ds)^2 + 2R*d^2R/ds^2
term_dR2 = 2*dR_ds(tau_fold)**2
term_Rd2R = 2*R_fold*d2R_ds2(tau_fold)
print(f"\n  d^2(R^2)/ds^2 = 2(dR/ds)^2 + 2R*d^2R/ds^2")
print(f"    = 2*{dR_ds(tau_fold):.6f}^2 + 2*{R_fold:.6f}*{d2R_ds2(tau_fold):.6f}")
print(f"    = {term_dR2:.6f} + {term_Rd2R:.6f} = {term_dR2+term_Rd2R:.6f}")

# =============================================================================
# 16. Compare 1D vs 3D alpha_crit
# =============================================================================
print("\n--- 16. 1D (tau-only) vs 3D alpha_crit ---")

print(f"  1D alpha_crit (tau-only, analytic): {alpha_crit_tau:.10f}")
print(f"  3D alpha_crit (first crossing, generalized eigenvalue): {gen_alpha[0]:.10f}")
print(f"  3D alpha_crit (binary search): {alpha_crit_1:.10f}")
print(f"  PHONON-2 value: 52.39")
print(f"  S60 text value: ~55")

# The ratio alpha_crit_3D / alpha_crit_1D tells us about the off-Jensen directions
if abs(alpha_crit_tau) > 1e-10:
    ratio_3d_1d = gen_alpha[0] / alpha_crit_tau
    print(f"\n  alpha_crit(3D) / alpha_crit(1D) = {ratio_3d_1d:.10f}")

# =============================================================================
# 17. Conformal Invariance Test
# =============================================================================
print("\n--- 17. Conformal invariance test ---")

# Question: Is alpha_crit a conformally invariant quantity?
# Under conformal transformation g -> Omega^2 g on an n-manifold:
#   C_{abcd} -> Omega^2 C_{abcd} (conformal invariance of Weyl, n>=4)
#   |C|^2 -> Omega^{-4} |C|^2 (in n>4)
#   R -> Omega^{-2}[R - 2(n-1)*nabla^2(ln Omega) - (n-1)(n-2)|d(ln Omega)|^2]
#   |Ric|^2 -> (not simply conformal)
#
# alpha_crit is NOT conformally invariant because:
# 1. It involves R and its derivatives (not conformal)
# 2. |Ric|^2 mixes under conformal transformations
# 3. Only |C|^2 is conformal (in the appropriate sense)
#
# However, alpha_crit may be a TOPOLOGICAL or DIMENSIONAL invariant.

# Test: is alpha_crit related to the Euler density coefficients?
# In d=8, the Euler density (Lovelock) involves:
# E_8 = sum of products of 4 Riemann tensors, contracted with epsilon tensors.
# The Gauss-Bonnet term in d=4 is |C|^2 - 2|S|^2 + R^2/(d(d-1)).
# In d=8, the generalized Gauss-Bonnet involves 4th-order Lovelock.

# Let's test pure dimensional formulas
dim_formulas = {
    "d*(d+1)/2": d*(d+1)/2,                        # 36
    "d^2/2 + d": d**2/2 + d,                       # 40
    "(d-1)*(d+2)/2": (d-1)*(d+2)/2,                # 35
    "d*(d-1)/2 + d": d*(d-1)/2 + d,                # 36
    "coeff_R2/coeff_C2_ratio": -coeff_R2/coeff_C2, # ~17.6
    "2400/coeff_R2": 2400/coeff_R2,                 # ~4.85
    "2400/(20/3)": 2400/(20.0/3),                   # 360
    "(5R^2 - 2Ric^2)/(2K)": (5*R_fold**2-2*Ric2_fold)/(2*K_fold),  # ~18.2
    "coeff_R2*R^2/(20*R/3)": coeff_R2*R_fold**2/((20.0/3)*R_fold), # ~52.5 !
}

print(f"  Testing dimensional/structural formulas vs alpha_crit = {gen_alpha[0]:.6f}:")
for name, val in dim_formulas.items():
    if val != 0:
        pct = (val - gen_alpha[0])/gen_alpha[0]*100
        print(f"    {name} = {val:.6f}  ({pct:+.2f}%)")

# The candidate "coeff_R2*R^2/(20*R/3)" is very close!
# Let's check: coeff_R2*R / (20/3) = (495 + residual)*R / (20/3)
# = (3/20) * coeff_R2 * R  [at the fold]
val_candidate = (3.0/20) * coeff_R2 * R_fold
print(f"\n  CANDIDATE: (3/20) * coeff_R2 * R(fold) = (3/20) * {coeff_R2:.6f} * {R_fold:.6f} = {val_candidate:.10f}")
print(f"  alpha_crit(1D) = {alpha_crit_tau:.10f}")
print(f"  alpha_crit(3D) = {gen_alpha[0]:.10f}")
pct_1d = (val_candidate - alpha_crit_tau)/alpha_crit_tau*100
pct_3d = (val_candidate - gen_alpha[0])/gen_alpha[0]*100
print(f"  Match to 1D: {pct_1d:+.2f}%")
print(f"  Match to 3D: {pct_3d:+.2f}%")

# =============================================================================
# 18. The Key Formula: alpha_crit from a_4 Coefficient Ratios
# =============================================================================
print("\n--- 18. Key formula derivation ---")

# From the a_4 Gilkey formula:
# a_4_integrand = 500R^2 - 32|Ric|^2 - 28K
#
# At the fold, this evaluates to:
a4_int_fold = 500*R_fold**2 - 32*Ric2_fold - 28*K_fold
print(f"  a_4 integrand at fold = {a4_int_fold:.10f}")

# The a_2 integrand is: 20R/3
a2_int_fold = 20*R_fold/3
print(f"  a_2 integrand at fold = {a2_int_fold:.10f}")

# Their ratio:
ratio_integrands = a4_int_fold / a2_int_fold
print(f"  a_4_integrand / a_2_integrand = {ratio_integrands:.10f}")

# This is NOT alpha_crit directly. alpha_crit involves the HESSIAN ratio,
# not the value ratio. But let's see if it's related.

# The ratio a_4_int/a_2_int = (500R^2 - 32|Ric|^2 - 28K) / (20R/3)
# = (3/20) * (500R^2 - 32|Ric|^2 - 28K) / R
# = (3/20) * (500R - 32|Ric|^2/R - 28K/R)

ratio_explicit = (3.0/20) * (500*R_fold - 32*Ric2_fold/R_fold - 28*K_fold/R_fold)
print(f"  (3/20)*(500R - 32|Ric|^2/R - 28K/R) = {ratio_explicit:.10f}")

# Now the key observation: on a HOMOGENEOUS space, the curvature invariants
# are CONSTANT (no spatial derivatives). The Hessian is d^2/ds^2 of the
# DEFORMATION-DEPENDENT curvature. BUT the ratio alpha_crit should be
# related to the ratio of the a_4 to a_2 integrands themselves, scaled by
# the curvature stiffness.

# Actually, let's think about it differently.
# The spectral action is S = alpha * a_2 + a_4 (dropping Lambda dependences).
# The Hessian is H = alpha * H_a2 + H_a4.
# For an ISOTROPIC deformation (all directions scale the same), the Hessian
# eigenvalue is alpha * d^2(a_2)/ds^2 + d^2(a_4)/ds^2.
# This is zero when alpha = -d^2(a_4)/d^2(a_2).
# The value of this ratio depends on the specific point on the moduli space.

# Let's compute the GILKEY values and their second derivatives
P_norm = (4*PI)**(-4)
a2_SD = P_norm * (20.0/3) * R_fold * Vol_SU3_Haar
a4_SD = P_norm * (1.0/360) * a4_int_fold * Vol_SU3_Haar
ratio_SD = a4_SD / a2_SD
print(f"\n  Gilkey normalized:")
print(f"    a_2^SD = {a2_SD:.10f}")
print(f"    a_4^SD = {a4_SD:.10f}")
print(f"    a_4/a_2 = {ratio_SD:.10f}")

# This ratio is the a_4/a_2 ratio from Gilkey, which was computed in s61_heat_kernel_a4.
# It's 0.414, confirmed there.

# alpha_crit(1D) is NOT the same as a_4/a_2 because alpha_crit involves
# the ratio of SECOND DERIVATIVES, not values.

# =============================================================================
# 19. Exact Numerical Formula
# =============================================================================
print("\n--- 19. Exact numerical verification ---")

# Let's compute alpha_crit along tau analytically and see if it can be
# written as a SIMPLE function of the curvature invariants at that point.

# For each tau, define:
#   A(s) = a_4_integrand = 500R(s)^2 - 32|Ric|^2(s) - 28K(s)
#   B(s) = a_2_integrand = (20/3)*R(s)
# alpha_crit(s) = -A''(s) / (360 * B''(s)) [the 360 comes from the 1/360 in a_4]
# Wait: let's be careful.
# H_a4 = P*Vol*(1/360)*A''(s), H_a2 = P*Vol*B''(s)
# alpha_crit = -H_a4/H_a2 = -(1/360)*A''/B''

# Let's verify with the actual Hessians
H_a2_00 = H_a2[0,0]
H_a4_00 = H_a4[0,0]
ratio_numerical = -H_a4_00 / H_a2_00
a2_dd = (20.0/3) * d2R_ds2(tau_fold)
a4_dd = (1.0/360) * (500*d2R2_ds2(tau_fold) - 32*d2Ric2_ds2(tau_fold) - 28*d2K_ds2(tau_fold))
ratio_analytic = -a4_dd / a2_dd
print(f"  alpha_crit(tau-only, from H matrices) = {ratio_numerical:.10f}")
print(f"  alpha_crit(tau-only, from curvature) = {ratio_analytic:.10f}")

# These should match if the S60 computation is consistent with the analytic curvature.
# Any discrepancy comes from:
# 1. S60 used finite differences on Dirac eigenvalues (not analytic curvature)
# 2. S60 truncated the Dirac spectrum at max(p+q)=3
# 3. The Gilkey expansion is an asymptotic series (converges slowly)
print(f"  Discrepancy: {abs(ratio_numerical - ratio_analytic)/ratio_analytic*100:.4f}%")

# =============================================================================
# 20. The Answer: What IS alpha_crit?
# =============================================================================
print("\n" + "=" * 78)
print("  SECTION 20: THE GEOMETRIC ORIGIN OF alpha_crit")
print("=" * 78)

# alpha_crit(tau, fold) = -[d^2(a4_int)/ds^2] / [360 * d^2(a2_int)/ds^2]
# where a4_int = 500R^2 - 32|Ric|^2 - 28K  and  a2_int = (20/3)*R
# at s = tau_fold = 0.19.

# Compute all pieces at the fold precisely
A_dd = 500*d2R2_ds2(tau_fold) - 32*d2Ric2_ds2(tau_fold) - 28*d2K_ds2(tau_fold)
B_dd = (20.0/3) * d2R_ds2(tau_fold)
alpha_analytic = -A_dd / (360.0 * B_dd)

# Using d^2(R^2)/ds^2 = 2(R')^2 + 2R*R''
Rp = dR_ds(tau_fold)
Rpp = d2R_ds2(tau_fold)
R_val = R_fold
Ric2pp = d2Ric2_ds2(tau_fold)
Kpp = d2K_ds2(tau_fold)

print(f"\n  R = {R_val:.10f}")
print(f"  R' = {Rp:.10f}")
print(f"  R'' = {Rpp:.10f}")
print(f"  |Ric|^2'' = {Ric2pp:.10f}")
print(f"  K'' = {Kpp:.10f}")

# alpha_crit = -(500*(2Rp^2 + 2R*Rpp) - 32*Ric2pp - 28*Kpp) / (360*(20/3)*Rpp)
# = -(1000*Rp^2 + 1000*R*Rpp - 32*Ric2pp - 28*Kpp) / (2400*Rpp)
# = -(1000*Rp^2/Rpp + 1000*R - 32*Ric2pp/Rpp - 28*Kpp/Rpp) / 2400

# Separate into a "static" part and a "flow" part:
static_part = -1000*R_val / 2400  # = -(5/12)*R
flow_part_R = -1000*Rp**2 / (2400*Rpp)
flow_part_Ric = 32*Ric2pp / (2400*Rpp)
flow_part_K = 28*Kpp / (2400*Rpp)

print(f"\n  alpha_crit decomposition:")
print(f"    Static (-(5/12)*R):   {static_part:.10f}")
print(f"    Flow (R'^2/R''):      {flow_part_R:.10f}")
print(f"    Flow (|Ric|^2''/R''): {flow_part_Ric:.10f}")
print(f"    Flow (K''/R''):       {flow_part_K:.10f}")
print(f"    Sum: {static_part + flow_part_R + flow_part_Ric + flow_part_K:.10f}")
print(f"    alpha_crit: {alpha_analytic:.10f}")

# The dominant contribution:
total_static = abs(static_part)
total_flow = abs(flow_part_R) + abs(flow_part_Ric) + abs(flow_part_K)
print(f"\n  |Static| = {total_static:.6f}, |Flow| = {total_flow:.6f}")
print(f"  Static fraction: {total_static/(total_static+total_flow)*100:.1f}%")

# Check: the static part is -(5/12)*R = -(5/12)*2.018 = -0.841
# The total alpha_crit ~ 52, so the flow parts dominate massively.
# This means alpha_crit is NOT simply a ratio of curvature invariants
# at the fold — it also encodes the curvature FLOW (how invariants change
# with the modulus).

# =============================================================================
# 21. Curvature Stiffness Ratios
# =============================================================================
print("\n--- 21. Curvature stiffness ratios ---")

# Define stiffness = d^2f/ds^2 / f for each curvature invariant
stiff_R = Rpp / R_val
stiff_Ric2 = Ric2pp / Ric2_fold
stiff_K = Kpp / K_fold
stiff_R2 = d2R2_ds2(tau_fold) / R_val**2

print(f"  R''/R = {stiff_R:.10f}")
print(f"  |Ric|^2''/|Ric|^2 = {stiff_Ric2:.10f}")
print(f"  K''/K = {stiff_K:.10f}")
print(f"  (R^2)''/(R^2) = {stiff_R2:.10f}")

# If all stiffnesses were equal (sigma), then:
# alpha_crit = -(500*sigma*R^2 - 32*sigma*|Ric|^2 - 28*sigma*K) / (2400*sigma*R)
# = -a_4_integrand / (2400*R)  [independent of sigma!]
# This is the "integrand ratio" formula.

alpha_ratio_formula = -a4_int_fold / (2400*R_fold)
print(f"\n  'Equal stiffness' formula: -a_4_int/(2400*R) = {alpha_ratio_formula:.10f}")
print(f"  Actual alpha_crit(1D): {alpha_analytic:.10f}")
print(f"  Discrepancy: {(alpha_ratio_formula - alpha_analytic)/alpha_analytic*100:.2f}%")

# The equal-stiffness approximation is off because the stiffnesses are NOT equal.
# The Kretschner K stiffens faster than R.
# This is the "differential" origin of alpha_crit: it measures the RELATIVE
# curvature stiffness of the a_4 and a_2 sectors.

# =============================================================================
# 22. The Definitive Formula
# =============================================================================
print("\n--- 22. Definitive formula ---")

# alpha_crit (1D Jensen, tau-direction) =
#   -(500[2(R'/R)^2 + 2R''/R]*R^2 - 32|Ric|^2''  - 28K'')
#   / (2400 * R'')
#
# = [500R(R + (R'/R'')^2*2R) + 32|Ric|^2''/R'' + 28K''/R''] / 2400
#
# Define dimensionless flow parameters:
#   xi = (R')^2 / (R*R'')  (normalized scalar curvature kinetic term)
#   rho_Ric = |Ric|^2'' / (R*R'')  (Ricci-squared flow / scalar flow)
#   rho_K = K'' / (R*R'')  (Kretschner flow / scalar flow)
#
# Then:
#   alpha_crit = -[500R(2xi+2) - 32*rho_Ric*R*R'' - 28*rho_K*R*R''] / (2400*R'')
#   ... this is getting complicated. Let's just state the clean version.

# The cleanest form:
# alpha_crit = (1/2400) * [1000R + 1000(R')^2/R'' - 32|Ric|^2''/R'' - 28K''/R'']
# The R'' cancels between numerator and denominator except for the ratio terms.

# At the fold:
term1 = 1000*R_val / 2400
term2 = 1000*Rp**2 / (2400*Rpp)
term3 = -32*Ric2pp / (2400*Rpp)
term4 = -28*Kpp / (2400*Rpp)
print(f"  alpha_crit = (5/12)*R + (5/12)*(R')^2/R'' - (2/150)|Ric|^2''/R'' - (7/600)K''/R''")
print(f"  Term 1: (5/12)*R = {term1:.10f}")
print(f"  Term 2: (5/12)*(R')^2/R'' = {term2:.10f}")
print(f"  Term 3: -(2/150)|Ric|^2''/R'' = {term3:.10f}")
print(f"  Term 4: -(7/600)K''/R'' = {term4:.10f}")
print(f"  Sum: {term1+term2+term3+term4:.10f}")
print(f"  Check sign convention: actual = {alpha_analytic:.10f}")

# Wait -- sign. Let me recompute from scratch carefully.
# H_a2 has eigenvalues ALL NEGATIVE. H_a4 has eigenvalues ALL POSITIVE.
# H_SA = alpha * H_a2 + H_a4
# At alpha = 0: H_SA = H_a4 > 0 (all positive eigenvalues)
# As alpha grows: H_a2 (negative) dominates.
# alpha_crit is where first eigenvalue crosses zero.
# So alpha_crit > 0 (it's a positive number).
# alpha_crit = min eigenvalue of (-H_a2)^{-1} H_a4 = gen_alpha[0] > 0.

# For the 1D tau case:
# H_a2_00 < 0 (confirmed from data)
# H_a4_00 > 0 (confirmed from data)
# alpha_crit_tau = -H_a4_00 / H_a2_00 > 0 ✓
print(f"\n  Sign check: H_a2[0,0] = {H_a2[0,0]:.6f} (should be negative)")
print(f"  Sign check: H_a4[0,0] = {H_a4[0,0]:.6f} (should be positive)")
print(f"  Sign check: alpha_crit_tau = {alpha_crit_tau:.6f} (should be positive)")

# =============================================================================
# 23. Test Known 4D Result
# =============================================================================
print("\n--- 23. Test: 4D Chamseddine-Connes alpha_crit ---")

# In 4D, for a Dirac operator on a 4-manifold:
# a_2 = (4pi)^{-2} * int (R/6 - E) = (4pi)^{-2} * int (5R/12) for Lichnerowicz
# Wait, dim_S = 4 in 4D. E = -R/4*I_4.
# a_2 = (4pi)^{-2} * 4 * (R/6 + R/4) = (4pi)^{-2} * 4*(5R/12) = (4pi)^{-2}*(5R/3)
#
# a_4 = (4pi)^{-2} * (1/360) * [60R*E + 180E^2 + 30*Omega^2 + (5R^2-2|Ric|^2+2K)*dim_S]
# For dim_S=4, E=-R/4*I:
# = (4pi)^{-2} * (1/360) * [-60R^2 + 180R^2/16 + 30*Omega^2 + 4(5R^2-2|Ric|^2+2K)]
# = (4pi)^{-2} * (1/360) * [-60R^2 + 11.25R^2 + 30*Omega^2 + 20R^2 - 8|Ric|^2 + 8K]
#
# For D_K^2 on a 4-manifold, Omega is the spin curvature, tr(Omega^2) = -K/2 * dim_S = -2K
# So 30*Omega^2 -> 30*(-2K) = -60K
# Total: -60R^2 + 11.25R^2 - 60K + 20R^2 - 8|Ric|^2 + 8K
#       = -28.75R^2 - 8|Ric|^2 - 52K
# Hmm, that doesn't look right. Let me use standard 4D Lichnerowicz formula directly.

# Standard Gilkey-Branson-Orsted for spin-Dirac on 4-manifold (see e.g., Vassilevich):
# a_4(D^2) = (4pi)^{-2} * (1/360) * int [-60*R*R/4 + 180*(R/4)^2 - 60K
#            + (5R^2 - 2|Ric|^2 + 2K)*4] * vol   (using tr(I)=4, E=-R/4)
# = (4pi)^{-2} * (1/360) * int [-15R^2 + 45R^2/4 - 60K + 20R^2 - 8|Ric|^2 + 8K]
# = (4pi)^{-2} * (1/360) * int [(-15+11.25+20)R^2 - 8|Ric|^2 + (-60+8)K]
# = (4pi)^{-2} * (1/360) * int [16.25R^2 - 8|Ric|^2 - 52K]

# For 4D round S^4 (Einstein, all curvature determined by R):
# alpha_crit_4D ~ a_4_int / (360 * a_2_int / a_2) ...
# This is getting complicated. Let me just compute the 4D analog numerically.

# For S^4 with radius r: R = 12/r^2, |Ric|^2 = 36/r^4, K = 24/r^4
# All in unit radius (r=1): R=12, |Ric|^2=36, K=24
d4 = 4
R_S4 = 12.0  # (local)
Ric2_S4 = 36.0  # (local)
K_S4 = 24.0  # (local)
dim_S_4D = 4  # spinor dimension in 4D

# 4D Gilkey: 60*R*E + 180*E^2 + 30*Omega^2 + (5R^2-2|Ric|^2+2K)*dim_S
# E = -R/4, Omega^2 trace = -2K (for dim_S=4)
a4_int_4D = (-60*R_S4*R_S4/4 + 180*(R_S4/4)**2 + 30*(-2*K_S4)
             + dim_S_4D*(5*R_S4**2 - 2*Ric2_S4 + 2*K_S4))
a2_int_4D = dim_S_4D * (R_S4/6 + R_S4/4)  # = 4*(5R/12)
print(f"  4D S^4: a_4_int = {a4_int_4D:.6f}, a_2_int = {a2_int_4D:.6f}")
print(f"  Ratio: {a4_int_4D/a2_int_4D:.6f}")
# This ratio is NOT alpha_crit, but is related to it.

# =============================================================================
# 24. Summary: Geometric Classification of alpha_crit
# =============================================================================
print("\n" + "=" * 78)
print("  SUMMARY: GEOMETRIC ORIGIN OF alpha_crit")
print("=" * 78)

print(f"""
  RESULT: alpha_crit IS a geometric quantity but is NOT a conformal invariant.

  The spectral action Hessian H_SA = alpha * H_a2 + H_a4 changes sign when
  the Einstein-Hilbert sector (a_2, proportional to scalar curvature R)
  overcomes the Yang-Mills/Gauss-Bonnet sector (a_4, involving R^2, |Ric|^2, K).

  DECOMPOSITION (Penrose-Rindler, d=8):
    a_2 integrand = (20/3) * R   [pure scalar curvature]
    a_4 integrand = (1/360) * ({coeff_R2:.2f}*R^2 + {coeff_S2:.2f}*|S|^2 + {coeff_C2:.2f}*|C|^2)

  At the fold (tau={tau_fold}):
    R = {R_fold:.6f}
    |S|^2 = {S2_fold:.6f}  (traceless Ricci)
    |C|^2 = {C2_fold:.6f}  (Weyl)

  Penrose-Rindler fractions of a_4 integrand:
    Scalar (R^2):    {a4_R2_term/a4_total*100:.1f}%
    Traceless Ricci: {a4_S2_term/a4_total*100:.1f}%
    Weyl:            {a4_C2_term/a4_total*100:.1f}%

  alpha_crit is determined by the GENERALIZED EIGENVALUE PROBLEM:
    H_a4 * v = alpha * (-H_a2) * v
  where both Hessians are 3x3 matrices on the volume-preserving moduli space.

  GENERALIZED EIGENVALUES (exact alpha_crit per mode):
    Mode 0: alpha = {gen_alpha[0]:.6f}  (first destabilization)
    Mode 1: alpha = {gen_alpha[1]:.6f}
    Mode 2: alpha = {gen_alpha[2]:.6f}

  GEOMETRIC INTERPRETATION:
    alpha_crit = ratio of (a_4 curvature stiffness) to (a_2 curvature stiffness)
    along each modulus direction.

    It involves NOT just the curvature invariants at the fold, but their
    SECOND DERIVATIVES with respect to the moduli (curvature flow).

    Key flow parameters at fold:
      R''/R = {stiff_R:.6f}
      |Ric|^2''/|Ric|^2 = {stiff_Ric2:.6f}
      K''/K = {stiff_K:.6f}

    These stiffnesses are NOT equal (K stiffens {stiff_K/stiff_R:.1f}x faster than R),
    which is why alpha_crit differs from the naive integrand ratio
    ({alpha_ratio_formula:.2f} vs {alpha_analytic:.2f}).

  CONFORMAL INVARIANCE: NO.
    alpha_crit mixes all three Penrose-Rindler sectors (R^2, |S|^2, |C|^2).
    Only |C|^2 is conformally invariant. The scalar R and traceless Ricci |S|^2
    transform non-trivially under conformal rescaling.
    The Weyl contribution ({a4_C2_term/a4_total*100:.1f}% of a_4 integrand)
    is the SMALLEST sector — the scalar R^2 sector ({a4_R2_term/a4_total*100:.1f}%)
    dominates.

  CLASSIFICATION: The value alpha_crit = {gen_alpha[0]:.2f} is a GEOMETRIC (not conformal,
    not topological) invariant of the Jensen deformation on SU(3) at the fold.
    It encodes the competition between scalar curvature stiffness (how fast R changes)
    and full curvature stiffness (how fast the a_4 combination changes).
""")

# =============================================================================
# 25. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: ALPHA-CRIT-CONFORMAL-61")
print("=" * 78)

# PASS: conformal invariance origin identified
# FAIL: accidental (no geometric explanation)
# INFO: known geometric ratio but not conformal

verdict = "INFO"
detail = (f"alpha_crit = {gen_alpha[0]:.4f} is a geometric ratio of curvature stiffnesses "
          f"(a_4 vs a_2 Hessians), NOT conformal. R^2 sector dominates ({a4_R2_term/a4_total*100:.0f}%), "
          f"Weyl only {a4_C2_term/a4_total*100:.0f}%. "
          f"Origin: generalized eigenvalue of H_a4 vs -H_a2 on 3D volume-preserving moduli space.")

print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")

# =============================================================================
# 26. Save Data
# =============================================================================
print("\n--- Saving results ---")

save_path = 's61_alpha_crit_conformal.npz'
np.savez(save_path,
    # Gate
    gate_name=np.array(['ALPHA-CRIT-CONFORMAL-61']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),

    # Penrose-Rindler decomposition at fold
    R_fold=R_fold,
    Ric2_fold=Ric2_fold,
    K_fold=K_fold,
    S2_fold=S2_fold,
    C2_fold=C2_fold,
    d_manifold=d,

    # PR coefficients in a_4
    coeff_R2=coeff_R2,
    coeff_S2=coeff_S2,
    coeff_C2=coeff_C2,

    # PR fractions
    frac_R2=a4_R2_term/a4_total,
    frac_S2=a4_S2_term/a4_total,
    frac_C2=a4_C2_term/a4_total,

    # Generalized eigenvalues (exact alpha_crit per mode)
    gen_alpha=gen_alpha,
    gen_vecs=gen_vecs,

    # Binary search alpha_crit
    alpha_crit_1=alpha_crit_1,
    alpha_crit_2=alpha_crit_2 if alpha_crit_2 else np.nan,
    alpha_crit_3=alpha_crit_3 if alpha_crit_3 else np.nan,

    # 1D analytic alpha_crit
    alpha_crit_tau_1D=alpha_analytic,

    # Curvature stiffnesses
    stiff_R=stiff_R,
    stiff_Ric2=stiff_Ric2,
    stiff_K=stiff_K,

    # Second derivatives at fold
    R_fold_pp=Rpp,
    Ric2_fold_pp=Ric2pp,
    K_fold_pp=Kpp,
    R_fold_p=Rp,

    # Tau sweep
    tau_sweep=tau_sweep,
    alpha_crit_vs_tau=alpha_crit_vs_tau,

    # Hessians from S60
    H_a2=H_a2,
    H_a4=H_a4,
    H_a0=H_a0,

    # Round SU(3) values
    R_round=R0,
    S2_round=S2_0,
    C2_round=C2_0,
)
print(f"  Saved: {save_path}")

# =============================================================================
# 27. Plot
# =============================================================================
print("\n--- Generating plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(r'$\alpha_{\rm crit}$ Conformal Analysis — ALPHA-CRIT-CONFORMAL-61', fontsize=14, fontweight='bold')

# Panel 1: alpha_crit vs tau
ax1 = axes[0,0]
valid = ~np.isnan(alpha_crit_vs_tau) & (alpha_crit_vs_tau > 0) & (alpha_crit_vs_tau < 500)
ax1.plot(tau_sweep[valid], alpha_crit_vs_tau[valid], 'b-', linewidth=2)
ax1.axvline(tau_fold, color='r', linestyle='--', alpha=0.7, label=f'fold ($\\tau$={tau_fold})')
ax1.axhline(gen_alpha[0], color='g', linestyle=':', alpha=0.7, label=f'$\\alpha_{{crit,3D}}$ = {gen_alpha[0]:.2f}')
ax1.set_xlabel(r'$\tau$', fontsize=12)
ax1.set_ylabel(r'$\alpha_{\rm crit}(\tau)$ [1D Jensen]', fontsize=12)
ax1.set_title(r'$\alpha_{\rm crit}$ along Jensen line')
ax1.legend(fontsize=9)
ax1.set_ylim([0, 300])
ax1.grid(True, alpha=0.3)

# Panel 2: Penrose-Rindler decomposition pie chart at fold
ax2 = axes[0,1]
sizes = [abs(a4_R2_term), abs(a4_S2_term), abs(a4_C2_term)]
labels = [f'Scalar $R^2$\n({abs(a4_R2_term)/a4_total*100:.1f}%)',
          f'Traceless Ricci $|S|^2$\n({abs(a4_S2_term)/a4_total*100:.1f}%)',
          f'Weyl $|C|^2$\n({abs(a4_C2_term)/a4_total*100:.1f}%)']
colors = ['#ff6b6b', '#4ecdc4', '#45b7d1']
# Use signs: R^2 positive, S^2 negative, C^2 negative in a_4 integrand
wedges, texts, autotexts = ax2.pie(sizes, labels=labels, colors=colors, autopct='',
                                    startangle=90, textprops={'fontsize':9})
ax2.set_title(f'Penrose-Rindler sectors in $a_4$\n(fold, $\\tau$={tau_fold})', fontsize=11)

# Panel 3: Eigenvalue scan
ax3 = axes[1,0]
alpha_scan_fine = np.linspace(0, 100, 500)
ev_scan = np.zeros((len(alpha_scan_fine), 3))
for i, alpha in enumerate(alpha_scan_fine):
    ev_scan[i] = np.sort(np.linalg.eigvalsh(alpha * H_a2 + H_a4))

for j in range(3):
    ax3.plot(alpha_scan_fine, ev_scan[:,j], linewidth=2, label=f'Mode {j}')
ax3.axhline(0, color='k', linewidth=0.5)
for j, ac in enumerate(gen_alpha):
    ax3.axvline(ac, color=['red','orange','green'][j], linestyle='--', alpha=0.7,
               label=f'$\\alpha_{{crit,{j}}}$ = {ac:.2f}')
ax3.set_xlabel(r'$\alpha = f_2 \Lambda^2 / f_0$', fontsize=12)
ax3.set_ylabel('Hessian eigenvalue', fontsize=12)
ax3.set_title(r'$H_{SA}$ eigenvalues vs $\alpha$')
ax3.legend(fontsize=8, loc='lower left')
ax3.set_ylim([-5e6, 5e6])
ax3.grid(True, alpha=0.3)

# Panel 4: Curvature stiffness comparison
ax4 = axes[1,1]
tau_stiff = np.linspace(0.01, 0.4, 200)
stiff_R_arr = np.array([d2R_ds2(s)/R_scalar(s) for s in tau_stiff])
stiff_Ric2_arr = np.array([d2Ric2_ds2(s)/Ric2_exact(s) for s in tau_stiff])
stiff_K_arr = np.array([d2K_ds2(s)/K_exact(s) for s in tau_stiff])

ax4.plot(tau_stiff, stiff_R_arr, 'b-', linewidth=2, label=r"$R''/R$")
ax4.plot(tau_stiff, stiff_Ric2_arr, 'r-', linewidth=2, label=r"$|{\rm Ric}|^{2\prime\prime}/|{\rm Ric}|^2$")
ax4.plot(tau_stiff, stiff_K_arr, 'g-', linewidth=2, label=r"$K''/K$")
ax4.axvline(tau_fold, color='k', linestyle='--', alpha=0.5, label='fold')
ax4.set_xlabel(r'$\tau$', fontsize=12)
ax4.set_ylabel('Curvature stiffness', fontsize=12)
ax4.set_title('Curvature stiffness = $f\'\'/f$')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('s61_alpha_crit_conformal.png', dpi=150, bbox_inches='tight')
print(f"  Saved: s61_alpha_crit_conformal.png")

# =============================================================================
# 28. Final Summary
# =============================================================================
elapsed = time.time() - t_start
print(f"\n  Elapsed: {elapsed:.1f}s")
print("\n" + "=" * 78)
print("  FINAL RESULT")
print("=" * 78)
print(f"""
  alpha_crit (3D, first crossing) = {gen_alpha[0]:.6f}
  alpha_crit (3D, second crossing) = {gen_alpha[1]:.6f}
  alpha_crit (3D, third crossing) = {gen_alpha[2]:.6f}
  alpha_crit (1D Jensen, analytic) = {alpha_analytic:.6f}

  CONFORMAL: NO (scalar R^2 dominates at {a4_R2_term/a4_total*100:.0f}%, Weyl only {a4_C2_term/a4_total*100:.0f}%)
  TOPOLOGICAL: NO (involves curvature flow derivatives, not just topology)
  DIMENSIONAL: PARTIAL (the coefficients {coeff_R2:.1f}, {coeff_S2:.1f}, {coeff_C2:.1f} depend on d=8,
    but the RATIOS of second derivatives are metric-dependent)

  GEOMETRIC ORIGIN: alpha_crit measures the ratio of curvature stiffness
    in the Yang-Mills sector (a_4) to the Einstein-Hilbert sector (a_2).
    The K stiffness is {stiff_K/stiff_R:.1f}x the R stiffness at the fold,
    which is why alpha_crit deviates from the naive integrand ratio.

  Gate: {verdict}
""")
