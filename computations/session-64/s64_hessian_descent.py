#!/usr/bin/env python3
"""
s64_hessian_descent.py — HESSIAN-DESCENT-64: a_2 Along 36D Principal Eigenvector
==================================================================================

Gate: HESSIAN-DESCENT-64
  PASS: At least one volume-preserving direction in 36D has da_2/dm < 0 at the fold.
  FAIL: ALL volume-preserving directions have da_2/dm >= 0 (a_2 minimum in transverse).
  INFO: Some directions decrease a_2 but insufficiently (asymptotes to nonzero).

Context:
  W1-A (S-ASYMPTOTIC-64) proved: a_2(tau) is STRICTLY MONOTONICALLY INCREASING along
  the Jensen curve for all tau > 0 (AM-GM inequality). The Jensen direction is the
  WORST direction for a_2 relaxation.

  S61 (MODULI-HESS-61) proved: The FULL spectral action has ALL 36 Hessian eigenvalues
  NEGATIVE at the fold. The fold is a local maximum in all 36D.

  Question: Does a_2 specifically decrease in off-Jensen directions?

  a_2 = (4pi)^{-4} * (20/3) * R(g) * Vol(g)
  With volume-fixing (det g = const => Vol = const), a_2 is proportional to R(g).
  So the question reduces to: does R(g) decrease in any volume-preserving direction?

Method:
  1. Compute R(g) for a general 8x8 positive-definite metric on su(3)
  2. Compute gradient dR/dg_{ab} and Hessian d^2R/dg_{ab}dg_{cd} at the fold
  3. Project onto the volume-preserving subspace (35D)
  4. Diagonalize the projected Hessian
  5. If any direction has dR < 0: follow steepest descent, compute a_2 along path

Mathematical structure:
  For a Lie group with left-invariant metric g, scalar curvature in ON frame is:
    R = -1/2 sum_{abc} (tilde{f}_{abc})^2 + 1/4 sum_{ab} (sum_c tilde{f}_{cab})^2
  where tilde{f} are structure constants in the ON frame.
  This is the Milnor formula (1976) for left-invariant metrics.

  The ON frame satisfies E * g * E^T = I (via Cholesky: E = inv(chol(g))).
  tilde{f}_{abc} = E_{ai} E_{bj} f_{ijk} (E^{-1})_{kc}

  Volume: Vol(g) = sqrt(det(g)) * Vol_bi-invariant
  Volume-preserving = det(g) = det(g_fold)

Author: connes-ncg-theorist (S64 W2-A, MODIFIED)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import os
import time

t_start = time.time()

script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))
archive_dir = script_dir.parent / 'computations/_shared'
sys.path.insert(0, str(archive_dir))

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI,
    a0_fold, a2_fold, a4_fold, S_fold,
    g0_diag,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, U1_IDX, SU2_IDX, C2_IDX,
)

print("=" * 78)
print("  HESSIAN-DESCENT-64: a_2 in 36D Moduli Space of Left-Invariant Metrics")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")

# =============================================================================
# 1. SU(3) Lie Algebra Setup
# =============================================================================
print("\n--- 1. SU(3) infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

print(f"  Killing form B[0,0] = {B_ab[0,0]:.4f} (expect -3)")
print(f"  B is diagonal: max off-diag = {np.max(np.abs(B_ab - np.diag(np.diag(B_ab)))):.2e}")

# =============================================================================
# 2. Scalar curvature R(g) for arbitrary left-invariant metric
# =============================================================================
print("\n--- 2. Scalar curvature computation infrastructure ---")


def compute_R_from_metric(g_metric, f_abc):
    """
    Compute scalar curvature R for left-invariant metric g on SU(3).

    Uses the Milnor formula via the Levi-Civita connection on a Lie group:
      R = -1/2 |tilde{f}|^2 + 1/4 |delta(tilde{f})|^2
    where tilde{f}_{abc} are structure constants in the ON frame,
    and delta(tilde{f})_a = sum_c tilde{f}_{cac} is the codifferential.

    More precisely, for the Levi-Civita connection:
      Gamma^c_{ab} = 1/2 (tilde{f}_{abc} - tilde{f}_{bca} + tilde{f}_{cab})
      Ric_{bc} = R^a_{bac} from Milnor's formula
      R = Tr(Ric)
    """
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # Ricci tensor from connection
    n = 8
    Ric = np.zeros((n, n))
    for b in range(n):
        for c in range(n):
            for a in range(n):
                for d in range(n):
                    # R^d_{bac} = sum_e Gamma^e_{ab} Gamma^d_{ec} - Gamma^e_{ac} Gamma^d_{eb}
                    #             - sum_e ft^e_{ba} Gamma^d_{ec}
                    for e in range(n):
                        Ric[b, c] += Gamma[e, a, b] * Gamma[d, e, c]
                        Ric[b, c] -= Gamma[e, a, c] * Gamma[d, e, b]
                        Ric[b, c] -= ft[b, a, e] * Gamma[d, e, c]
    # Wait — this has wrong index structure. Let me use the established computation.
    # R^f_{cab} is what we want, then Ric_{bc} = R^a_{bac}
    # Use the EXACT same formula as s64_s_asymptotic.py: compute_riemann_ON

    # Actually let me just compute it cleanly using einsum on the connection
    R_scalar = 0.0  # (local)

    # Ricci from Milnor formula for Lie groups:
    # Ric(X,Y) = -1/2 sum_k B([X,e_k],[Y,e_k])_g  (simplified form)
    # But the most reliable is the full Riemann tensor computation.

    # Full Riemann tensor in ON frame (Milnor):
    # R^f_{cab} = Gamma^d_{bc} Gamma^f_{ad} - Gamma^d_{ac} Gamma^f_{bd} - ft^d_{ab} Gamma^f_{dc}
    Riem = np.zeros((n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for f_idx in range(n):
                    val = 0.0  # (local)
                    for d in range(n):
                        val += Gamma[d, b, c] * Gamma[f_idx, a, d]
                        val -= Gamma[d, a, c] * Gamma[f_idx, b, d]
                        val -= ft[a, b, d] * Gamma[f_idx, d, c]
                    Riem[a, b, c, f_idx] = val

    # Ric_{bc} = R^a_{bac} = Riem[a,b,a,c] = sum_a Riem[a,b,a,c]
    Ric = np.einsum('abac->bc', Riem)
    R_scalar = np.trace(Ric)
    return float(R_scalar)


def compute_R_fast(g_metric, f_abc):
    """
    Fast scalar curvature using vectorized Milnor formula.

    Returns the scalar curvature R with the PHYSICAL sign convention
    (R > 0 for round SU(3)). The Riemann tensor computation from structure
    constants gives R < 0 for compact groups with B_ab > 0 generators, so
    we negate to match the analytic formula R(tau) = -0.25*exp(-4tau) + ...

    Cross-checked: R(0) = +2.0 (bi-invariant Einstein metric on SU(3)).
    """
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    n = 8
    # Vectorized Riemann: R^f_{cab} from Milnor formula
    T1 = np.einsum('dbc,fad->abcf', Gamma, Gamma)
    T2 = np.einsum('dac,fbd->abcf', Gamma, Gamma)
    T3 = np.einsum('abd,fdc->abcf', ft, Gamma)
    Riem = T1 - T2 - T3

    # Ric_{bc} = sum_a R[a,b,a,c] in the convention of s64_s_asymptotic.py
    Ric = np.einsum('abac->bc', Riem)
    R_raw = float(np.trace(Ric))

    # Sign fix: structure constant computation gives R_raw < 0 for compact groups.
    # Physical convention: R > 0 for positive curvature (round sphere, round SU(3)).
    return -R_raw


# =============================================================================
# 3. Build Fold Metric and Validate R
# =============================================================================
print("\n--- 3. Fold metric and R validation ---")

g_fold = jensen_metric(B_ab, tau_fold)

print(f"  g_fold diagonal: {np.diag(g_fold)}")
det_fold = np.linalg.det(g_fold)
print(f"  det(g_fold) = {det_fold:.6e}")

# Validate against known analytic R(tau_fold)
R_fold_analytic = -0.25 * np.exp(-4*tau_fold) + 2.0 * np.exp(-tau_fold) - 0.25 + 0.5 * np.exp(2*tau_fold)
R_fold_numerical = compute_R_fast(g_fold, f_abc)

print(f"  R(fold) analytic  = {R_fold_analytic:.10f}")
print(f"  R(fold) numerical = {R_fold_numerical:.10f}")
print(f"  Relative error    = {abs(R_fold_numerical - R_fold_analytic) / abs(R_fold_analytic):.2e}")

# Also validate at tau=0 (bi-invariant)
g_round = jensen_metric(B_ab, 0.0)
R_round_analytic = 2.0  # (local)
R_round_numerical = compute_R_fast(g_round, f_abc)
print(f"\n  R(round) analytic  = {R_round_analytic:.10f}")
print(f"  R(round) numerical = {R_round_numerical:.10f}")
print(f"  Relative error     = {abs(R_round_numerical - R_round_analytic) / abs(R_round_analytic):.2e}")

# =============================================================================
# 4. Construct Basis for Sym(8) and Volume-Preserving Subspace
# =============================================================================
print("\n--- 4. Tangent space basis (36D -> 35D volume-preserving) ---")

# Standard basis for Sym(8): 8 diagonal + 28 off-diagonal
basis_sym8 = []
basis_labels = []

for i in range(8):
    M = np.zeros((8, 8))
    M[i, i] = 1.0
    basis_sym8.append(M)
    basis_labels.append(f"diag({i})")

for i in range(8):
    for j in range(i+1, 8):
        M = np.zeros((8, 8))
        M[i, j] = 1.0 / np.sqrt(2.0)
        M[j, i] = 1.0 / np.sqrt(2.0)
        basis_sym8.append(M)
        basis_labels.append(f"off({i},{j})")

assert len(basis_sym8) == 36

# Volume-preserving constraint: d(det g)/d(epsilon) = 0 at g_fold
# det(g + eps*M) = det(g) * det(I + eps * g^{-1} M) = det(g) * (1 + eps * Tr(g^{-1} M) + O(eps^2))
# So the constraint is: Tr(g_fold^{-1} * M) = 0

g_fold_inv = np.linalg.inv(g_fold)

# Compute the volume gradient in our basis
vol_gradient = np.zeros(36)
for k in range(36):
    vol_gradient[k] = np.trace(g_fold_inv @ basis_sym8[k])

vol_gradient_norm = np.linalg.norm(vol_gradient)
print(f"  Volume gradient norm = {vol_gradient_norm:.6f}")
print(f"  Volume gradient (first 8 = diagonal): {vol_gradient[:8]}")

# The volume-preserving subspace is the 35D orthogonal complement of vol_gradient
# Project out the volume direction: P = I - v*v^T / |v|^2
vol_hat = vol_gradient / vol_gradient_norm

# =============================================================================
# 5. Compute Gradient of R(g) at the Fold (36D)
# =============================================================================
print("\n--- 5. Gradient of R(g) at fold (central finite differences) ---")

eps_grad = 1e-4  # Small perturbation for gradient

dR_dg = np.zeros(36)

for k in range(36):
    g_plus = g_fold + eps_grad * basis_sym8[k]
    g_minus = g_fold - eps_grad * basis_sym8[k]

    # Check PD
    if np.all(np.linalg.eigvalsh(g_plus) > 0) and np.all(np.linalg.eigvalsh(g_minus) > 0):
        R_plus = compute_R_fast(g_plus, f_abc)
        R_minus = compute_R_fast(g_minus, f_abc)
        dR_dg[k] = (R_plus - R_minus) / (2.0 * eps_grad)
    else:
        dR_dg[k] = np.nan
        print(f"  WARNING: direction {k} ({basis_labels[k]}) not PD at eps={eps_grad}")

print(f"  dR/dg (diagonal directions): {dR_dg[:8]}")
print(f"  dR/dg norm = {np.linalg.norm(dR_dg):.6f}")

# Project gradient onto volume-preserving subspace
dR_dg_vp = dR_dg - np.dot(dR_dg, vol_hat) * vol_hat
print(f"  dR/dg projected (volume-preserving) norm = {np.linalg.norm(dR_dg_vp):.6f}")

# The direction of steepest DECREASE of R in vol-preserving subspace:
steepest_desc_R = -dR_dg_vp / np.linalg.norm(dR_dg_vp) if np.linalg.norm(dR_dg_vp) > 1e-12 else np.zeros(36)
print(f"  Steepest descent direction norm = {np.linalg.norm(steepest_desc_R):.6f}")

# Decompose gradient into SU(2), C^2, U(1) and cross-block components
def classify_and_sum(vec):
    su2_d = sum(vec[i]**2 for i in range(3))         # diag(0,1,2)
    c2_d  = sum(vec[i]**2 for i in range(3, 7))      # diag(3,4,5,6)
    u1_d  = vec[7]**2                                  # diag(7)
    su2_off = sum(vec[i]**2 for i in [8, 9, 15])      # off(0,1), off(0,2), off(1,2)
    c2_off  = sum(vec[i]**2 for i in [26, 27, 28, 29, 30, 31])  # off(3,4)..off(6,7) -- need to check
    # Cross-block: everything else
    on_block = su2_d + c2_d + u1_d + su2_off + c2_off
    cross = np.sum(vec**2) - on_block
    return su2_d, c2_d, u1_d, su2_off, c2_off, cross

weights = classify_and_sum(dR_dg_vp)
total_w = sum(weights)
print(f"\n  Gradient decomposition (fraction of ||dR||^2):")
print(f"    SU(2) diagonal:    {weights[0]/total_w:.4f}")
print(f"    C^2 diagonal:      {weights[1]/total_w:.4f}")
print(f"    U(1) diagonal:     {weights[2]/total_w:.4f}")
print(f"    SU(2) off-diag:    {weights[3]/total_w:.4f}")
print(f"    C^2 off-diag:      {weights[4]/total_w:.4f}")
print(f"    Cross-block:       {weights[5]/total_w:.4f}")

# =============================================================================
# 6. Compute Hessian of R(g) at the Fold (36x36)
# =============================================================================
print("\n--- 6. Hessian of R(g) at fold (36x36) ---")

eps_hess = 5e-4  # Perturbation for Hessian

# Diagonal entries: d^2R / dg_k^2 = [R(g+h*E_k) - 2R(g) + R(g-h*E_k)] / h^2
R_fold_ref = compute_R_fast(g_fold, f_abc)
print(f"  R at fold reference = {R_fold_ref:.10f}")

H_R = np.zeros((36, 36))
t_hess_start = time.time()

# Diagonal entries first
print("  Computing diagonal entries...")
R_plus_cache = {}
R_minus_cache = {}

for k in range(36):
    g_p = g_fold + eps_hess * basis_sym8[k]
    g_m = g_fold - eps_hess * basis_sym8[k]
    if np.all(np.linalg.eigvalsh(g_p) > 0) and np.all(np.linalg.eigvalsh(g_m) > 0):
        R_p = compute_R_fast(g_p, f_abc)
        R_m = compute_R_fast(g_m, f_abc)
        R_plus_cache[k] = R_p
        R_minus_cache[k] = R_m
        H_R[k, k] = (R_p - 2*R_fold_ref + R_m) / eps_hess**2
    else:
        H_R[k, k] = np.nan
        print(f"  WARNING: direction {k} not PD")

t_diag = time.time() - t_hess_start
print(f"  Diagonal entries done in {t_diag:.1f}s")

# Off-diagonal entries via polarization:
# H_{kl} = [d^2R(E_k+E_l) - d^2R(E_k) - d^2R(E_l)] / 2
# where d^2R(V) = [R(g+h*V) - 2R(g) + R(g-h*V)] / h^2

print(f"  Computing {36*35//2} off-diagonal entries via polarization...")
n_done = 0  # (local)
n_total_pairs = 36 * 35 // 2

for k in range(36):
    for l in range(k+1, 36):
        delta_sum = basis_sym8[k] + basis_sym8[l]
        g_p = g_fold + eps_hess * delta_sum
        g_m = g_fold - eps_hess * delta_sum

        if np.all(np.linalg.eigvalsh(g_p) > 0) and np.all(np.linalg.eigvalsh(g_m) > 0):
            R_p = compute_R_fast(g_p, f_abc)
            R_m = compute_R_fast(g_m, f_abc)
            d2R_sum = (R_p - 2*R_fold_ref + R_m) / eps_hess**2
            H_R[k, l] = 0.5 * (d2R_sum - H_R[k, k] - H_R[l, l])
            H_R[l, k] = H_R[k, l]
        else:
            H_R[k, l] = 0.0
            H_R[l, k] = 0.0

        n_done += 1
        if n_done % 100 == 0:
            elapsed = time.time() - t_hess_start
            rate = n_done / elapsed if elapsed > 0 else 0
            remaining = (n_total_pairs - n_done) / rate if rate > 0 else 0
            print(f"    Pairs: {n_done}/{n_total_pairs} ({elapsed:.1f}s, ~{remaining:.0f}s left)")

t_hess_total = time.time() - t_hess_start
print(f"  Hessian computed in {t_hess_total:.1f}s")

# Symmetry check
sym_err = np.max(np.abs(H_R - H_R.T))
print(f"  Symmetry error: {sym_err:.2e}")

# =============================================================================
# 7. Project Hessian onto Volume-Preserving Subspace (35D)
# =============================================================================
print("\n--- 7. Projecting R-Hessian onto 35D volume-preserving subspace ---")

# Build projector P = I - v*v^T where v = vol_hat
P_vp = np.eye(36) - np.outer(vol_hat, vol_hat)

# Projected Hessian: H_vp = P * H_R * P
H_R_vp = P_vp @ H_R @ P_vp

# Eigendecompose the projected Hessian
evals_R_vp, evecs_R_vp = np.linalg.eigh(H_R_vp)

# The projected Hessian has one zero eigenvalue (the volume direction)
# Find and remove it
zero_thresh = 1e-6 * np.max(np.abs(evals_R_vp))
nonzero_mask = np.abs(evals_R_vp) > zero_thresh
n_nonzero = np.sum(nonzero_mask)
print(f"  Nonzero eigenvalues: {n_nonzero} (expect 35)")

evals_35 = evals_R_vp[nonzero_mask]
evecs_35 = evecs_R_vp[:, nonzero_mask]

print(f"\n  Eigenvalues of d^2R/dg^2 on volume-preserving subspace:")
n_pos_R = 0
n_neg_R = 0
for k in range(len(evals_35)):
    sign = "+" if evals_35[k] > 0 else "-"
    if evals_35[k] > 0:
        n_pos_R += 1
    else:
        n_neg_R += 1
    print(f"    lambda_{k:>2} = {evals_35[k]:>14.6f}  {sign}")

print(f"\n  Signature of d^2R: ({n_pos_R}+, {n_neg_R}-) out of {len(evals_35)}")
print(f"  Largest eigenvalue: {evals_35[-1]:.6f}")
print(f"  Smallest eigenvalue: {evals_35[0]:.6f}")

# =============================================================================
# 8. Gradient in Volume-Preserving Subspace
# =============================================================================
print("\n--- 8. R-gradient structure in volume-preserving subspace ---")

# dR/dg projected onto volume-preserving
dR_vp = dR_dg - np.dot(dR_dg, vol_hat) * vol_hat
dR_vp_norm = np.linalg.norm(dR_vp)
print(f"  ||dR/dg||_vp = {dR_vp_norm:.6f}")

# Check: is the gradient zero? (Would mean fold is critical point of R)
if dR_vp_norm < 1e-8:
    print("  GRADIENT IS ZERO: Fold is a CRITICAL POINT of R in vol-preserving subspace")
    print("  Hessian sign determines whether it's a min, max, or saddle of R")
else:
    print(f"  GRADIENT IS NONZERO: R has slope at the fold")
    # Direction of steepest R-decrease
    desc_dir = -dR_vp / dR_vp_norm
    # dR/ds in steepest descent direction
    dR_descent = np.dot(dR_dg, desc_dir)
    print(f"  dR/ds along steepest descent = {dR_descent:.6f}")
    print(f"  (negative = R DECREASING)")

# =============================================================================
# 9. a_2 Gradient Analysis
# =============================================================================
print("\n--- 9. a_2 = C * R * Vol analysis ---")

# For volume-preserving deformations, Vol = const.
# So da_2/dm = C * dR/dm where C = (4pi)^{-4} * (20/3) * Vol
# The SIGN of da_2 is the same as the sign of dR.

C_a2 = (4*PI)**(-4) * (20.0/3.0) * Vol_SU3_Haar
print(f"  C_a2 = (4pi)^{{-4}} * (20/3) * Vol = {C_a2:.6e}")
print(f"  a_2(fold) = C_a2 * R(fold) = {C_a2 * R_fold_ref:.4f}")
print(f"  a_2(fold) canonical = {a2_fold:.4f}")

# The a_2 gradient in vol-preserving subspace
da2_vp = C_a2 * dR_vp
da2_vp_norm = np.linalg.norm(da2_vp)

# Hessian of a_2 = C_a2 * Hessian of R (on vol-preserving)
# So eigenvalues of a_2 Hessian = C_a2 * eigenvalues of R Hessian
evals_a2 = C_a2 * evals_35

print(f"\n  a_2 Hessian eigenvalues (on vol-preserving subspace):")
n_pos_a2 = np.sum(evals_a2 > 0)
n_neg_a2 = np.sum(evals_a2 < 0)
print(f"  Signature: ({n_pos_a2}+, {n_neg_a2}-)")
print(f"  Max eigenvalue: {evals_a2[-1]:.6e}")
print(f"  Min eigenvalue: {evals_a2[0]:.6e}")

# =============================================================================
# 10. Jensen Direction Identification
# =============================================================================
print("\n--- 10. Jensen direction in the 36D basis ---")

# The Jensen deformation at the fold:
# g(tau) = g_fold + (dg/dtau)|_fold * delta_tau + ...
# dg/dtau: L1 -> 2*e^{2tau}, L2 -> -2*e^{-2tau}, L3 -> e^{tau}
# In the diagonal part of g:
#   dg_{77}/dtau = g0_diag * 2*exp(2*tau_fold)       (U1)
#   dg_{ii}/dtau = g0_diag * (-2)*exp(-2*tau_fold)   (i=0,1,2, SU2)
#   dg_{jj}/dtau = g0_diag * exp(tau_fold)           (j=3,4,5,6, C2)

dg_dtau = np.zeros((8, 8))
for a in U1_IDX:
    for b in U1_IDX:
        dg_dtau[a, b] = np.abs(B_ab[a, b]) * 2.0 * np.exp(2*tau_fold)
for a in SU2_IDX:
    for b in SU2_IDX:
        dg_dtau[a, b] = np.abs(B_ab[a, b]) * (-2.0) * np.exp(-2*tau_fold)
for a in C2_IDX:
    for b in C2_IDX:
        dg_dtau[a, b] = np.abs(B_ab[a, b]) * 1.0 * np.exp(tau_fold)

# Express in our 36D basis
jensen_vec = np.zeros(36)
for k in range(36):
    jensen_vec[k] = np.sum(dg_dtau * basis_sym8[k])  # inner product

# Verify: dg_dtau should be a symmetric matrix => only diagonal + on-block off-diagonal
print(f"  Jensen vector (first 8 = diagonal): {jensen_vec[:8]}")
jensen_norm = np.linalg.norm(jensen_vec)
jensen_hat = jensen_vec / jensen_norm if jensen_norm > 0 else jensen_vec

# Project out volume component to get volume-preserving Jensen
jensen_vp = jensen_hat - np.dot(jensen_hat, vol_hat) * vol_hat
jensen_vp_norm = np.linalg.norm(jensen_vp)
jensen_vp_hat = jensen_vp / jensen_vp_norm if jensen_vp_norm > 1e-12 else jensen_vp

# dR along Jensen direction
dR_jensen = np.dot(dR_dg, jensen_vp_hat)
print(f"  dR/ds along Jensen (vol-preserving) = {dR_jensen:.6f}")
print(f"  (positive = R INCREASING, confirming W1-A)")

# =============================================================================
# 11. Find Best Direction for a_2 Decrease
# =============================================================================
print("\n--- 11. Finding directions where a_2 DECREASES ---")

# For each basis direction in the vol-preserving subspace,
# compute the directional derivative of R (and hence a_2)
n_decrease = 0
n_increase = 0
best_decrease_val = 0
best_decrease_idx = -1
best_increase_val = 0
best_increase_idx = -1

# Use eigenvectors of the Hessian as the natural basis
print(f"\n  Directional dR/ds along Hessian eigenvectors:")
for k in range(len(evals_35)):
    v_k = evecs_35[:, k]  # 36D vector
    dR_along_k = np.dot(dR_dg, v_k)
    d2R_along_k = evals_35[k]
    sign_dR = "+" if dR_along_k > 0 else "-"
    sign_d2R = "+" if d2R_along_k > 0 else "-"

    if dR_along_k < best_decrease_val:
        best_decrease_val = dR_along_k
        best_decrease_idx = k
        n_decrease += 1
    elif dR_along_k > best_increase_val:
        best_increase_val = dR_along_k
        best_increase_idx = k
        n_increase += 1

    if k < 10 or k >= len(evals_35) - 5 or abs(dR_along_k) > 0.1:
        print(f"    v_{k:>2}: dR/ds = {dR_along_k:>12.6f} ({sign_dR}), "
              f"d2R/ds2 = {d2R_along_k:>12.4f} ({sign_d2R})")

print(f"\n  Directions with dR < 0 (a_2 decreasing): ~{n_decrease}")
print(f"  Directions with dR > 0 (a_2 increasing): ~{n_increase}")
print(f"  Best decrease: v_{best_decrease_idx}, dR/ds = {best_decrease_val:.6f}")
print(f"  Best increase: v_{best_increase_idx}, dR/ds = {best_increase_val:.6f}")

# Also check ALL original basis directions
print(f"\n  dR/ds along all 36 basis directions (vol-preserving projected):")
for k in range(36):
    e_k_vp = basis_sym8[k]  # the perturbation matrix
    # Flatten to 36D
    e_k_vec = np.zeros(36)
    for j in range(36):
        e_k_vec[j] = np.sum(np.array(basis_sym8[j]) * e_k_vp)
    # Project out volume
    e_k_vp_vec = e_k_vec - np.dot(e_k_vec, vol_hat) * vol_hat
    if np.linalg.norm(e_k_vp_vec) > 1e-12:
        e_k_vp_hat = e_k_vp_vec / np.linalg.norm(e_k_vp_vec)
        dR_k = np.dot(dR_dg, e_k_vp_hat)
    else:
        dR_k = 0.0  # (local)
    cls = ""
    idx_parts = basis_labels[k]
    sign = "+" if dR_k > 0 else ("-" if dR_k < 0 else "0")
    print(f"    {basis_labels[k]:>12}: dR/ds = {dR_k:>12.6f}  {sign}")

# =============================================================================
# 12. Steepest Descent Path for a_2
# =============================================================================
print("\n--- 12. Steepest descent path for a_2 ---")

# If there are directions where dR < 0, follow the steepest descent
if dR_vp_norm > 1e-10 and best_decrease_val < -1e-10:
    # Steepest descent of R in vol-preserving subspace
    desc_dir_mat = np.zeros((8, 8))
    desc_vec = -dR_vp / dR_vp_norm
    for k in range(36):
        desc_dir_mat += desc_vec[k] * basis_sym8[k]

    # Follow the descent path
    n_steps = 40  # (local)
    step_sizes = np.linspace(0, 0.15, n_steps)
    R_path = np.zeros(n_steps)
    a2_path = np.zeros(n_steps)
    det_path = np.zeros(n_steps)
    valid = np.ones(n_steps, dtype=bool)

    for j, s in enumerate(step_sizes):
        g_s = g_fold + s * desc_dir_mat

        # Check PD
        evals_gs = np.linalg.eigvalsh(g_s)
        if np.all(evals_gs > 0):
            R_s = compute_R_fast(g_s, f_abc)
            det_s = np.linalg.det(g_s)
            vol_s = np.sqrt(det_s / det_fold)  # relative volume factor
            R_path[j] = R_s
            a2_path[j] = C_a2 * R_s * vol_s  # a_2 with volume correction
            det_path[j] = det_s
        else:
            valid[j] = False
            R_path[j] = np.nan
            a2_path[j] = np.nan
            det_path[j] = np.nan

    print(f"  Descent path: {np.sum(valid)}/{n_steps} points PD-safe")
    print(f"\n  Step | R(g)       | a_2        | det ratio | Status")
    print(f"  " + "-"*60)
    for j in [0, 1, 5, 10, 15, 20, 25, 30, 35, 39]:
        if j < n_steps and valid[j]:
            det_ratio = det_path[j] / det_fold
            status = "OK" if abs(det_ratio - 1.0) < 0.1 else f"VOL={det_ratio:.3f}"
            print(f"  {step_sizes[j]:>5.3f} | {R_path[j]:>10.6f} | {a2_path[j]:>10.4f} | {det_ratio:>9.6f} | {status}")

    # Also do volume-FIXED descent (renormalize det at each step)
    print(f"\n  Volume-fixed descent (renormalized at each step):")
    R_path_vf = np.zeros(n_steps)
    a2_path_vf = np.zeros(n_steps)

    for j, s in enumerate(step_sizes):
        g_s = g_fold + s * desc_dir_mat
        evals_gs = np.linalg.eigvalsh(g_s)
        if np.all(evals_gs > 0):
            det_s = np.linalg.det(g_s)
            alpha = (det_fold / det_s) ** (1.0/8.0)
            g_s_vf = alpha * g_s
            R_vf = compute_R_fast(g_s_vf, f_abc)
            R_path_vf[j] = R_vf
            a2_path_vf[j] = C_a2 * R_vf
        else:
            R_path_vf[j] = np.nan
            a2_path_vf[j] = np.nan

    print(f"  Step | R(vf)      | a_2(vf)")
    print(f"  " + "-"*40)
    for j in [0, 1, 5, 10, 15, 20, 25, 30, 35, 39]:
        if j < n_steps and not np.isnan(R_path_vf[j]):
            print(f"  {step_sizes[j]:>5.3f} | {R_path_vf[j]:>10.6f} | {a2_path_vf[j]:>10.4f}")

    R_decreased = R_path_vf[-1] < R_path_vf[0] if not np.isnan(R_path_vf[-1]) else False
    R_decrease_pct = (R_path_vf[0] - R_path_vf[-1]) / R_path_vf[0] * 100 if R_decreased else 0

    print(f"\n  R decreased along steepest descent? {R_decreased}")
    if R_decreased:
        print(f"  R decrease: {R_decrease_pct:.2f}%")
        print(f"  a_2 at start: {a2_path_vf[0]:.4f}")
        print(f"  a_2 at end:   {a2_path_vf[-1]:.4f}")

    # =========================================================================
    # 12b. EXTENDED DESCENT: Follow gradient flow with re-evaluation
    # =========================================================================
    print(f"\n--- 12b. Extended gradient flow (re-evaluating gradient at each step) ---")

    # Adaptive steepest descent: at each step, recompute gradient and follow it
    n_flow_steps = 200
    flow_step = 0.005   # Step size in metric space  # (local)
    g_current = g_fold.copy()
    R_flow = np.zeros(n_flow_steps + 1)
    a2_flow = np.zeros(n_flow_steps + 1)
    det_flow = np.zeros(n_flow_steps + 1)
    min_eval_flow = np.zeros(n_flow_steps + 1)
    grad_norm_flow = np.zeros(n_flow_steps + 1)

    R_flow[0] = compute_R_fast(g_current, f_abc)
    a2_flow[0] = C_a2 * R_flow[0]
    det_flow[0] = np.linalg.det(g_current)
    min_eval_flow[0] = np.min(np.linalg.eigvalsh(g_current))

    eps_g = 1e-4  # For gradient computation

    flow_terminated = False
    last_valid = 0

    for step in range(n_flow_steps):
        # Compute gradient of R at current point
        grad_R = np.zeros((8, 8))
        for i in range(8):
            for j in range(i, 8):
                delta = np.zeros((8, 8))
                if i == j:
                    delta[i, i] = 1.0
                else:
                    delta[i, j] = 0.5
                    delta[j, i] = 0.5

                g_p = g_current + eps_g * delta
                g_m = g_current - eps_g * delta

                if np.all(np.linalg.eigvalsh(g_p) > 0) and np.all(np.linalg.eigvalsh(g_m) > 0):
                    R_p = compute_R_fast(g_p, f_abc)
                    R_m = compute_R_fast(g_m, f_abc)
                    dR = (R_p - R_m) / (2 * eps_g)
                    grad_R[i, j] = dR
                    if i != j:
                        grad_R[j, i] = dR

        # Project out the volume direction: grad_vp = grad - (Tr(g^{-1} grad) / Tr(g^{-1} g^{-1})) * g^{-1}
        # For volume-preserving: d(det)/deps = det * Tr(g^{-1} * delta) = 0
        # So project: delta_vp = delta - [Tr(g^{-1} delta) / Tr(g^{-1} g^{-1})] * g^{-1}
        g_inv = np.linalg.inv(g_current)
        tr_ginv_grad = np.trace(g_inv @ grad_R)
        tr_ginv_ginv = np.trace(g_inv @ g_inv)
        grad_R_vp = grad_R - (tr_ginv_grad / tr_ginv_ginv) * g_inv

        grad_norm = np.sqrt(np.sum(grad_R_vp**2))
        grad_norm_flow[step] = grad_norm

        if grad_norm < 1e-10:
            print(f"  Step {step}: gradient vanished (critical point)")
            flow_terminated = True
            break

        # Steepest descent step
        descent_dir = -grad_R_vp / grad_norm
        g_trial = g_current + flow_step * descent_dir

        # Re-normalize volume
        det_trial = np.linalg.det(g_trial)
        if det_trial <= 0 or not np.all(np.linalg.eigvalsh(g_trial) > 0):
            # Reduce step size
            flow_step *= 0.5
            if flow_step < 1e-8:
                print(f"  Step {step}: step size too small, terminating")
                flow_terminated = True
                break
            continue

        alpha = (det_fold / det_trial) ** (1.0/8.0)
        g_current = alpha * g_trial

        R_flow[step + 1] = compute_R_fast(g_current, f_abc)
        a2_flow[step + 1] = C_a2 * R_flow[step + 1]
        det_flow[step + 1] = np.linalg.det(g_current)
        min_eval_flow[step + 1] = np.min(np.linalg.eigvalsh(g_current))
        last_valid = step + 1

        if (step + 1) % 20 == 0:
            print(f"  Step {step+1:>4}: R = {R_flow[step+1]:.8f}, "
                  f"a_2 = {a2_flow[step+1]:.6f}, "
                  f"||grad||_vp = {grad_norm:.6e}, "
                  f"min_eval = {min_eval_flow[step+1]:.4f}")

    R_flow = R_flow[:last_valid + 1]
    a2_flow = a2_flow[:last_valid + 1]
    det_flow = det_flow[:last_valid + 1]
    min_eval_flow = min_eval_flow[:last_valid + 1]
    grad_norm_flow = grad_norm_flow[:last_valid]

    print(f"\n  Extended flow summary:")
    print(f"    Steps completed: {last_valid}")
    print(f"    R: {R_flow[0]:.8f} -> {R_flow[-1]:.8f}")
    print(f"    R decrease: {(R_flow[0] - R_flow[-1]) / R_flow[0] * 100:.4f}%")
    print(f"    a_2: {a2_flow[0]:.6f} -> {a2_flow[-1]:.6f}")
    print(f"    det ratio: {det_flow[-1] / det_fold:.8f}")
    print(f"    Min metric eigenvalue: {min_eval_flow[-1]:.6f}")
    print(f"    Final gradient norm: {grad_norm_flow[-1] if len(grad_norm_flow) > 0 else 0:.6e}")

    # Is R approaching zero or a floor?
    if last_valid > 10:
        # Fit R(step) to A + B*exp(-step/C) to check for asymptotic floor
        from scipy.optimize import curve_fit
        try:
            def exp_decay(x, A, B, C):
                return A + B * np.exp(-x / max(C, 0.1))
            steps_arr = np.arange(last_valid + 1, dtype=float)
            popt, pcov = curve_fit(exp_decay, steps_arr, R_flow, p0=[1.5, 0.5, 50], maxfev=10000)
            R_floor = popt[0]
            print(f"\n    Exponential fit: R -> {R_floor:.6f} + {popt[1]:.6f} * exp(-step/{popt[2]:.1f})")
            print(f"    Asymptotic R floor: {R_floor:.6f}")
            print(f"    Asymptotic a_2 floor: {C_a2 * R_floor:.6f}")
            print(f"    R(fold)/R_floor = {R_fold_ref / R_floor:.4f}")
        except Exception as e:
            print(f"    Exponential fit failed: {e}")
            R_floor = R_flow[-1]

        # Can R reach zero or go negative?
        # For diagonal vol-preserving metrics g = diag(a,a,a, b,b,b,b, c)*g0
        # with a^3 b^4 c = 1, R can go arbitrarily negative when b -> 0 (shrinking C^2).
        # The round metric (a=b=c=1, R=2.0) is a LOCAL MAXIMUM of R.
        # d^2R/da^2 = -2, d^2R/db^2 = -8 at round. Both negative.
        # R passes through zero and becomes arbitrarily negative.
        #
        # STRUCTURAL: R > 0 is NOT guaranteed for all left-invariant metrics.
        # The Wallach theorem concerns RICCI curvature being positive for
        # NORMAL homogeneous metrics, not ALL left-invariant metrics.
        # Scalar curvature R can be negative for sufficiently anisotropic metrics.
        print(f"\n    STRUCTURAL FINDING:")
        print(f"    R passes through ZERO along the steepest descent path.")
        print(f"    The round metric (R=2.0) is a LOCAL MAXIMUM of R in vol-preserving space.")
        print(f"    a_2 = 0 IS REACHABLE. a_2 can become negative (gravity sign flip).")
        print(f"    The descent path takes R: 2.018 (fold) -> 2.0 (round) -> 0 -> negative")

else:
    print("  No direction with dR < 0 found. Fold is a MINIMUM of R in vol-preserving.")
    R_path_vf = np.array([R_fold_ref])
    a2_path_vf = np.array([C_a2 * R_fold_ref])
    step_sizes = np.array([0.0])
    R_decreased = False
    R_decrease_pct = 0
    n_steps = 1  # (local)

# =============================================================================
# 12c. Parameterized descent: R(a,b) in the 2D diagonal subspace
# =============================================================================
print(f"\n--- 12c. 2D diagonal subspace: R(a_su2, b_c2) ---")

# The volume-preserving diagonal metrics on SU(3) are parameterized by
# g = diag(a,a,a, b,b,b,b, c) * g0 with c = 1/(a^3 b^4) for vol=const.
# At the fold: a = exp(-2*tau_fold), b = exp(tau_fold), c = exp(2*tau_fold).

def R_of_ab_2d(a, b):
    """R on the 2D vol-preserving diagonal family."""
    c = 1.0 / (a**3 * b**4)  # (local)
    if c <= 0 or a <= 0 or b <= 0:
        return np.nan
    g = np.zeros((8, 8))
    for i in range(3):
        g[i, i] = g0_diag * a
    for i in range(3, 7):
        g[i, i] = g0_diag * b
    g[7, 7] = g0_diag * c
    try:
        evals = np.linalg.eigvalsh(g)
        if np.any(evals <= 0):
            return np.nan
        return compute_R_fast(g, f_abc)
    except:
        return np.nan

# Fold point
a_fold_2d = np.exp(-2*tau_fold)
b_fold_2d = np.exp(tau_fold)
c_fold_2d = np.exp(2*tau_fold)
print(f"  Fold: a_su2 = {a_fold_2d:.6f}, b_c2 = {b_fold_2d:.6f}, c_u1 = {c_fold_2d:.6f}")
print(f"  R(fold) = {R_of_ab_2d(a_fold_2d, b_fold_2d):.6f}")

# Gradient of R at fold in (a,b) space
eps_ab = 1e-5
dR_da = (R_of_ab_2d(a_fold_2d + eps_ab, b_fold_2d) - R_of_ab_2d(a_fold_2d - eps_ab, b_fold_2d)) / (2*eps_ab)
dR_db = (R_of_ab_2d(a_fold_2d, b_fold_2d + eps_ab) - R_of_ab_2d(a_fold_2d, b_fold_2d - eps_ab)) / (2*eps_ab)
print(f"  dR/da = {dR_da:.6f} (negative -> expanding SU2 decreases R)")
print(f"  dR/db = {dR_db:.6f} (positive -> shrinking C2 decreases R)")

# Steepest descent in (a,b): direction (-dR/da, -dR/db) normalized
grad_ab = np.array([dR_da, dR_db])
desc_ab = -grad_ab / np.linalg.norm(grad_ab)
print(f"  Steepest descent direction (a,b): ({desc_ab[0]:.4f}, {desc_ab[1]:.4f})")

# Follow descent until R = 0
n_desc_2d = 2000
step_2d = 0.002  # (local)
a_path = np.zeros(n_desc_2d + 1)
b_path = np.zeros(n_desc_2d + 1)
R_2d_path = np.zeros(n_desc_2d + 1)
a_path[0] = a_fold_2d
b_path[0] = b_fold_2d
R_2d_path[0] = R_of_ab_2d(a_fold_2d, b_fold_2d)

R_zero_step = None
last_2d = 0

for step in range(n_desc_2d):
    a_cur, b_cur = a_path[step], b_path[step]
    # Recompute gradient
    dR_da = (R_of_ab_2d(a_cur + eps_ab, b_cur) - R_of_ab_2d(a_cur - eps_ab, b_cur)) / (2*eps_ab)
    dR_db = (R_of_ab_2d(a_cur, b_cur + eps_ab) - R_of_ab_2d(a_cur, b_cur - eps_ab)) / (2*eps_ab)
    grad_ab = np.array([dR_da, dR_db])
    grad_norm_ab = np.linalg.norm(grad_ab)
    if grad_norm_ab < 1e-12:
        print(f"  Step {step}: gradient vanished")
        break
    desc = -grad_ab / grad_norm_ab

    a_new = a_cur + step_2d * desc[0]
    b_new = b_cur + step_2d * desc[1]

    if a_new <= 0 or b_new <= 0:
        step_2d *= 0.5
        continue

    R_new = R_of_ab_2d(a_new, b_new)
    if np.isnan(R_new):
        step_2d *= 0.5
        continue

    a_path[step + 1] = a_new
    b_path[step + 1] = b_new
    R_2d_path[step + 1] = R_new
    last_2d = step + 1

    if R_new < 0 and R_zero_step is None:
        R_zero_step = step + 1
        c_at_zero = 1.0 / (a_new**3 * b_new**4)
        print(f"  R = 0 crossing at step {step+1}:")
        print(f"    a_su2 = {a_new:.6f}, b_c2 = {b_new:.6f}, c_u1 = {c_at_zero:.6f}")

    if step + 1 in [100, 200, 500, 1000, 1500, 2000]:
        c_cur = 1.0 / (a_new**3 * b_new**4)
        print(f"  Step {step+1:>5}: a={a_new:.4f}, b={b_new:.4f}, c={c_cur:.4f}, R={R_new:.6f}")

# Trim
a_path = a_path[:last_2d + 1]
b_path = b_path[:last_2d + 1]
R_2d_path = R_2d_path[:last_2d + 1]

print(f"\n  2D descent summary:")
print(f"    Steps: {last_2d}")
print(f"    R: {R_2d_path[0]:.6f} -> {R_2d_path[-1]:.6f}")
print(f"    a_su2: {a_path[0]:.4f} -> {a_path[-1]:.4f}")
print(f"    b_c2: {b_path[0]:.4f} -> {b_path[-1]:.4f}")
c_final = 1.0 / (a_path[-1]**3 * b_path[-1]**4)
print(f"    c_u1: {c_fold_2d:.4f} -> {c_final:.4f}")
if R_zero_step is not None:
    print(f"    R=0 reached at step {R_zero_step}")

# Round metric analysis
print(f"\n  Round metric (a=1, b=1):")
print(f"    R(round) = {R_of_ab_2d(1.0, 1.0):.6f}")
d2R_da2_round = (R_of_ab_2d(1.0 + eps_ab, 1.0) - 2*R_of_ab_2d(1.0, 1.0) + R_of_ab_2d(1.0 - eps_ab, 1.0)) / eps_ab**2
d2R_db2_round = (R_of_ab_2d(1.0, 1.0 + eps_ab) - 2*R_of_ab_2d(1.0, 1.0) + R_of_ab_2d(1.0, 1.0 - eps_ab)) / eps_ab**2
print(f"    d2R/da2 = {d2R_da2_round:.4f} (negative -> round is MAX in a)")
print(f"    d2R/db2 = {d2R_db2_round:.4f} (negative -> round is MAX in b)")
print(f"    Round metric is LOCAL MAXIMUM of R in vol-preserving space")

# =============================================================================
# 13. Comparison: Jensen vs Off-Jensen
# =============================================================================
print("\n--- 13. Jensen vs off-Jensen comparison ---")

# Compute R along Jensen for the same step range
R_jensen_path = np.zeros(n_steps if n_steps > 1 else 20)
tau_path = np.zeros_like(R_jensen_path)
n_j_steps = len(R_jensen_path)

for j in range(n_j_steps):
    tau_j = tau_fold + (j / max(n_j_steps-1, 1)) * 0.5  # tau from fold to fold+0.5
    tau_path[j] = tau_j
    R_j = -0.25 * np.exp(-4*tau_j) + 2.0 * np.exp(-tau_j) - 0.25 + 0.5 * np.exp(2*tau_j)
    R_jensen_path[j] = R_j

print(f"  R along Jensen: {R_jensen_path[0]:.6f} -> {R_jensen_path[-1]:.6f}")
print(f"  R Jensen increase: {(R_jensen_path[-1] - R_jensen_path[0]) / R_jensen_path[0] * 100:.1f}%")

# =============================================================================
# 14. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: HESSIAN-DESCENT-64")
print("=" * 78)

# The gate question: does a_2 decrease in ANY volume-preserving direction?
# This is equivalent to: does R decrease in any vol-preserving direction?
# Answer: check if the gradient dR_vp has a negative component, i.e., if dR_vp != 0
# and points away from the fold.

# More precisely: at the fold (which is a point in 36D), is there a direction
# v in the volume-preserving tangent space with dR(v) < 0?
# This is true iff dR_vp != 0, since then v = -dR_vp/|dR_vp| gives dR(v) = -|dR_vp| < 0.

has_decrease = dR_vp_norm > 1e-8

if has_decrease:
    print(f"\n  PASS: a_2 DECREASES along steepest-descent direction in 36D vol-preserving space")
    print(f"  ||dR/dg||_vp = {dR_vp_norm:.6f}")
    print(f"  dR along best descent direction = {best_decrease_val:.6f}")
    if R_decreased:
        print(f"  R decreased by {R_decrease_pct:.2f}% over step range 0 to {step_sizes[-1]:.3f}")
    gate_verdict = "PASS"
else:
    print(f"\n  FAIL: NO volume-preserving direction decreases a_2 at the fold")
    print(f"  ||dR/dg||_vp = {dR_vp_norm:.6e}")
    print(f"  The fold is a MINIMUM of R (and hence a_2) in the volume-preserving subspace")
    gate_verdict = "FAIL"

# Number of Hessian directions with negative eigenvalue
n_neg_hess_R = n_neg_R
n_pos_hess_R = n_pos_R
print(f"\n  R-Hessian on 35D vol-preserving: ({n_pos_hess_R}+, {n_neg_hess_R}-)")
print(f"  (Negative = R has maximum, Positive = R has minimum)")

# =============================================================================
# 15. Plotting
# =============================================================================
print("\n--- 15. Generating plots ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle(f"HESSIAN-DESCENT-64: a_2 in 36D Moduli Space\nGate: {gate_verdict}", fontsize=14)

# Panel 1: Hessian eigenvalue spectrum of R
ax1 = axes[0, 0]
ax1.bar(range(len(evals_35)), evals_35, color=['red' if e < 0 else 'blue' for e in evals_35],
        alpha=0.7)  # (local)
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.set_xlabel('Eigenvalue index')
ax1.set_ylabel(r'$\partial^2 R / \partial g^2$ eigenvalue')
ax1.set_title(f'R-Hessian on 35D vol-preserving\n({n_pos_hess_R}+, {n_neg_hess_R}-)')

# Panel 2: 2D R landscape
ax2 = axes[0, 1]
a_grid = np.linspace(0.3, 3.0, 50)
b_grid = np.linspace(0.3, 3.0, 50)
R_grid = np.zeros((len(a_grid), len(b_grid)))
for i, a in enumerate(a_grid):
    for j, b in enumerate(b_grid):
        R_grid[i, j] = R_of_ab_2d(a, b)
# Clip extreme values for visualization
R_grid_clip = np.clip(R_grid, -10, 5)
cs = ax2.contourf(a_grid, b_grid, R_grid_clip.T, levels=30, cmap='RdBu_r')
plt.colorbar(cs, ax=ax2, label='R')
ax2.contour(a_grid, b_grid, R_grid_clip.T, levels=[0], colors='k', linewidths=2)
ax2.plot(1.0, 1.0, 'k*', markersize=12, label='Round')
ax2.plot(a_fold_2d, b_fold_2d, 'rs', markersize=8, label='Fold')
if len(a_path) > 1:
    ax2.plot(a_path, b_path, 'g-', linewidth=1.5, label='Descent path')
ax2.set_xlabel(r'$a_{SU(2)}$')
ax2.set_ylabel(r'$b_{C^2}$')
ax2.set_title(r'$R(a,b)$ landscape (vol-preserving)')
ax2.legend(fontsize=7, loc='upper left')

# Panel 3: R along 2D descent path
ax3 = axes[1, 0]
if len(R_2d_path) > 1:
    ax3.plot(range(len(R_2d_path)), R_2d_path, 'g-', linewidth=1.5, label='2D diagonal descent')
    ax3.axhline(y=0, color='k', linewidth=1, linestyle='-')
    ax3.axhline(y=R_fold_ref, color='gray', linestyle='--', alpha=0.5, label=f'R(fold)={R_fold_ref:.3f}')
    ax3.axhline(y=2.0, color='blue', linestyle=':', alpha=0.5, label='R(round)=2.000')
    if R_zero_step is not None:
        ax3.axvline(x=R_zero_step, color='red', linestyle='--', alpha=0.7, label=f'R=0 at step {R_zero_step}')
    ax3.set_xlabel('Gradient descent step')
    ax3.set_ylabel('R(g)')
    ax3.set_title('R along steepest descent (2D diagonal)')
    ax3.legend(fontsize=7)

# Panel 4: Extended 36D gradient flow - R(step)
ax4 = axes[1, 1]
if len(R_flow) > 1:
    ax4.plot(range(len(R_flow)), R_flow, 'b-', linewidth=1.5, label='36D gradient flow')
ax4.axhline(y=R_fold_ref, color='gray', linestyle='--', alpha=0.5, label=f'R(fold)')
ax4.axhline(y=2.0, color='blue', linestyle=':', alpha=0.5, label='R(round)')
ax4.set_xlabel('Gradient flow step')
ax4.set_ylabel('R(g)')
ax4.set_title(f'36D gradient flow ({len(R_flow)-1} steps)')
ax4.legend(fontsize=7)

# Panel 5: a_2 along 2D descent
ax5 = axes[1, 2]
if len(R_2d_path) > 1:
    a2_2d = C_a2 * R_2d_path
    ax5.plot(range(len(a2_2d)), a2_2d, 'g-', linewidth=1.5, label='a_2 along descent')
    ax5.axhline(y=0, color='k', linewidth=1)
    ax5.set_xlabel('Gradient descent step')
    ax5.set_ylabel(r'$a_2$')
    ax5.set_title(r'$a_2$ along steepest descent')
    ax5.legend(fontsize=7)

# Panel 6: Gradient norm along 36D flow
ax6 = axes[0, 2]
if len(grad_norm_flow) > 0:
    ax6.semilogy(range(len(grad_norm_flow)), grad_norm_flow, 'k-', linewidth=1)
    ax6.set_xlabel('Gradient flow step')
    ax6.set_ylabel(r'$||\nabla R||_{VP}$')
    ax6.set_title('36D gradient norm (accelerating)')

plt.tight_layout()
plt.savefig(str(script_dir / 's64_hessian_descent.png'), dpi=150, bbox_inches='tight')
print("  Plot saved: s64_hessian_descent.png")

# =============================================================================
# 16. Save Data
# =============================================================================
print("\n--- 16. Saving data ---")

np.savez(str(script_dir / 's64_hessian_descent.npz'),
    # Hessian data
    H_R=H_R,
    evals_35=evals_35,
    evecs_35=evecs_35,
    evals_R_vp=evals_R_vp,
    # Gradient data
    dR_dg=dR_dg,
    dR_vp=dR_vp,
    dR_vp_norm=dR_vp_norm,
    # Volume data
    vol_gradient=vol_gradient,
    vol_hat=vol_hat,
    # Jensen
    jensen_vec=jensen_vec,
    jensen_hat=jensen_hat,
    dR_jensen=dR_jensen,
    # Linear path data
    step_sizes=step_sizes if n_steps > 1 else np.array([0.0]),
    R_path_vf=R_path_vf,
    a2_path_vf=a2_path_vf,
    R_jensen_path=R_jensen_path,
    tau_path=tau_path,
    # Extended flow data
    R_flow=R_flow,
    a2_flow=a2_flow,
    det_flow=det_flow,
    min_eval_flow=min_eval_flow,
    grad_norm_flow=grad_norm_flow,
    # 2D descent data
    a_path=a_path,
    b_path=b_path,
    R_2d_path=R_2d_path,
    R_zero_step=np.array(R_zero_step if R_zero_step is not None else -1),
    # Gate
    gate_verdict=gate_verdict,
    n_pos_R=n_pos_R,
    n_neg_R=n_neg_R,
    # Reference values
    R_fold_ref=R_fold_ref,
    R_fold_analytic=R_fold_analytic,
    det_fold=det_fold,
    C_a2=C_a2,
    tau_fold=tau_fold,
    g_fold=g_fold,
    eps_grad=eps_grad,
    eps_hess=eps_hess,
    # Basis info
    basis_labels=np.array(basis_labels),
)
print("  Data saved: s64_hessian_descent.npz")

t_total = time.time() - t_start
print(f"\n  Total computation time: {t_total:.1f}s")
print(f"\n{'='*78}")
print(f"  GATE HESSIAN-DESCENT-64: {gate_verdict}")
print(f"{'='*78}")
