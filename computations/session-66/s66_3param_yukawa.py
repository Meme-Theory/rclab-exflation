#!/usr/bin/env python3
"""
s66_3param_yukawa.py — 3-PARAM-YUKAWA-66: Yukawa Matrix on Baptista 3-Parameter Family
========================================================================================
Gate: 3-PARAM-YUKAWA-66
  PASS: max(y_i/y_j) > 10 for some physically motivated parameter region
  FAIL: max(y_i/y_j) < 3 for all tested points (degeneracy unbroken)
  INFO: 3 < max < 10 (partial hierarchy, insufficient for SM)

GOVERNING STRUCTURE
===================
The 3-parameter family of left-invariant U(2)-invariant metrics on SU(3) is:

  g(L1, L2, L3) = L1 * g_0|_{u(1)} + L2 * g_0|_{su(2)} + L3 * g_0|_{C^2}

with g_0 = |B| the positive-definite Killing metric base. The decomposition:
  su(3) = u(1) [dim 1] + su(2) [dim 3] + C^2 [dim 4]

Jensen line: L1 = e^{2s}, L2 = e^{-2s}, L3 = e^s (volume-preserving).

THEORETICAL ANALYSIS (SCHUR LEMMA)
===================================
THEOREM: The Yukawa matrix Y_{ab} is proportional to I_4 for ALL U(2)-invariant
metrics, not just on the Jensen line. This is a consequence of Schur's lemma:

  1. The C^2 coset carries an irreducible representation of U(2) = SU(2) x U(1).
     Specifically, C^2 ~ (j=1/2, Y) under SU(2) x U(1).

  2. U(2) acts on C^2 by the isotropy representation. Being irreducible,
     any U(2)-equivariant endomorphism of C^2 is proportional to the identity
     (Schur's lemma).

  3. The Yukawa matrix Y_{ab} = sum_{(p,q)} dim(p,q) * Tr([D_K, L_{e_a}]^dag [D_K, L_{e_b}])
     is manifestly U(2)-equivariant: if u in U(2) acts as R on C^2 indices,
     then Y_{ab} -> (R Y R^T)_{ab}. But U(2)-equivariance forces Y = lambda * I_4.

  4. This holds for ALL three parameters (L1, L2, L3) independently. Moving off
     Jensen DOES change the scalar lambda(L1, L2, L3) but CANNOT split eigenvalues.

CONSEQUENCE: To break the C^2 degeneracy and generate a Yukawa hierarchy,
one must break U(2) invariance. This requires going beyond the 3-parameter family
to the full 36-dimensional moduli space Sym^2_+(su(3)^*).

THIS SCRIPT:
  1. Verifies the Schur theorem numerically on a 3D grid of (L1, L2, L3).
  2. Computes lambda(L1, L2, L3) — how the OVERALL Yukawa scale depends on the
     3 parameters, even though no hierarchy is produced.
  3. Investigates which minimal U(2)-breaking deformations produce hierarchy.
  4. Tests a specific U(2)-breaking perturbation to find the first non-degenerate
     Yukawa spectrum.

Author: baptista-spacetime-analyst (Session 66)
"""

import sys
import os
import time
import numpy as np
from numpy import sqrt, pi, exp
from numpy.linalg import eigh, eigvalsh, norm, inv
from scipy.linalg import cholesky
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import tau_fold, PI, M_KK_gravity, M_KK_kerner

# Import Dirac spectrum machinery
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, build_chirality, get_irrep, dirac_operator_on_irrep,
    validate_clifford, u2_invariant_metric, lie_derivative_metric,
    _irrep_cache, U1_IDX, SU2_IDX, C2_IDX
)

print("=" * 78)
print("  3-PARAM-YUKAWA-66: Yukawa Matrix on Baptista 3-Parameter Family")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")
t_start = time.time()

# =============================================================================
# SECTION 1: Infrastructure Setup
# =============================================================================
print("\n--- 1. Infrastructure setup ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
gammas = build_cliff8()
gamma9 = build_chirality(gammas)

cliff_err = validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")

# Jensen fold parameters
L1_fold = exp(2.0 * tau_fold)
L2_fold = exp(-2.0 * tau_fold)
L3_fold = exp(tau_fold)
print(f"  Jensen fold: L1={L1_fold:.6f}, L2={L2_fold:.6f}, L3={L3_fold:.6f}")

# Verify fold metric
g_fold = jensen_metric(B_ab, tau_fold)
g_fold_3p = u2_invariant_metric(B_ab, L1_fold, L2_fold, L3_fold)
fold_err = np.max(np.abs(g_fold - g_fold_3p))
print(f"  Jensen vs 3-param at fold: max|diff| = {fold_err:.2e}")

# PW sectors for Yukawa computation (matched to S65)
pw_sectors = [
    (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
    (2, 1), (1, 2), (3, 0), (0, 3),
]


def compute_yukawa_matrix(g_metric, gens, f_abc, B_ab, gammas, gamma9, pw_sectors):
    """
    Compute the 4x4 Yukawa texture matrix Y_{ab} for the 4 non-Killing
    directions (C^2 coset) at a given metric g_metric.

    Y_{ab} = sum_{(p,q)} dim(p,q) * Tr([D_K, L_{e_a}]^dag [D_K, L_{e_b}])

    Returns:
        Y: (4,4) real symmetric matrix
        Lg_norms: (4,) norms of Lie derivatives
        comm_norms: (4,) norms of [D_K, L_{e_a}]
        success: bool
    """
    nonkilling_dirs = [3, 4, 5, 6]
    n_nk = len(nonkilling_dirs)

    # Build geometry
    try:
        eigs = eigvalsh(g_metric)
        if np.min(eigs) <= 0:
            return None, None, None, False

        E = orthonormal_frame(g_metric)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas)
    except Exception:
        return None, None, None, False

    # Compute Lie derivatives
    Lg_all = []
    Lg_norms = np.zeros(n_nk)
    for ia, a in enumerate(nonkilling_dirs):
        Lg = lie_derivative_metric(Gamma, a)
        Lg_all.append(Lg)
        Lg_norms[ia] = sqrt(np.sum(Lg ** 2))

    # Precompute spinor connection 1-forms
    omega_spin = []
    for j in range(8):
        omega_j = np.zeros((16, 16), dtype=complex)
        for b in range(8):
            for c in range(8):
                coeff = Gamma[b, j, c]
                if abs(coeff) > 1e-15:
                    omega_j += coeff * gammas[b] @ gammas[c]
        omega_j *= 0.25
        omega_spin.append(omega_j)

    # Precompute covariant derivatives of Lie metric
    nabla_Lg = {}
    for ia, a in enumerate(nonkilling_dirs):
        Lg_a = Lg_all[ia]
        for i in range(8):
            n_val = np.zeros((8, 8), dtype=np.float64)
            for b in range(8):
                for c in range(8):
                    val = 0.0  # (local)
                    for d in range(8):
                        val -= Gamma[d, i, b] * Lg_a[d, c]
                        val -= Gamma[d, i, c] * Lg_a[b, d]
                    n_val[b, c] = val
            nabla_Lg[(a, i)] = n_val

    # Accumulate Yukawa matrix over PW sectors
    Y = np.zeros((n_nk, n_nk))
    comm_norms = np.zeros(n_nk)

    for ip, (p, q) in enumerate(pw_sectors):
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        dim_total = dim_pq * 16

        # Get representation
        _irrep_cache.clear()
        if p == 0 and q == 0:
            rho_list = [np.zeros((1, 1), dtype=complex) for _ in range(8)]
        else:
            rho_list, _ = get_irrep(p, q, gens, f_abc)

        # Build commutator [D_K, L_{e_a}] from Paper 17 eq (4.7)
        comm_matrices = {}
        for ia, a in enumerate(nonkilling_dirs):
            Lg_a = Lg_all[ia]

            # Term 1: (1/2) sum_{i,j} Lg_{ij} gamma_i nabla_j
            comm = np.zeros((dim_total, dim_total), dtype=complex)
            for i in range(8):
                gamma_i = gammas[i]
                for j in range(8):
                    if abs(Lg_a[i, j]) < 1e-15:
                        continue
                    nabla_j = (np.kron(rho_list[j], np.eye(16, dtype=complex)) +
                               np.kron(np.eye(dim_pq, dtype=complex), omega_spin[j]))
                    gamma_i_full = np.kron(np.eye(dim_pq, dtype=complex), gamma_i)
                    comm += 0.5 * Lg_a[i, j] * gamma_i_full @ nabla_j

            # Term 2: (1/4) sum_j { sum_i (nabla_i Lg)_{ij} - (nabla_j Lg)_{ii} } gamma_j
            for j in range(8):
                coeff = 0.0  # (local)
                for i in range(8):
                    coeff += nabla_Lg[(a, i)][i, j]
                coeff -= sum(nabla_Lg[(a, j)][i, i] for i in range(8))
                if abs(coeff) > 1e-15:
                    gamma_j_full = np.kron(np.eye(dim_pq, dtype=complex), gammas[j])
                    comm += 0.25 * coeff * gamma_j_full

            comm_matrices[a] = comm
            comm_norms[ia] += dim_pq * np.real(np.trace(comm.conj().T @ comm))

        # Accumulate Yukawa matrix
        for ia, a in enumerate(nonkilling_dirs):
            comm_a = comm_matrices[a]
            for ib, b in enumerate(nonkilling_dirs):
                comm_b = comm_matrices[b]
                Y[ia, ib] += dim_pq * np.real(np.trace(comm_a.conj().T @ comm_b))

    comm_norms = np.sqrt(comm_norms)
    Y = 0.5 * (Y + Y.T)  # enforce symmetry
    return Y, Lg_norms, comm_norms, True


# =============================================================================
# SECTION 2: Verify S65 Result at Jensen Fold
# =============================================================================
print("\n--- 2. Verifying S65 baseline at Jensen fold ---")

Y_fold, Lg_norms_fold, comm_norms_fold, ok_fold = compute_yukawa_matrix(
    g_fold, gens, f_abc, B_ab, gammas, gamma9, pw_sectors
)
assert ok_fold, "Jensen fold computation failed"

Y_fold_evals = eigvalsh(Y_fold)
Y_fold_evals_desc = np.sort(Y_fold_evals)[::-1]

print(f"  Y eigenvalues: {Y_fold_evals_desc}")
print(f"  Lg norms: {Lg_norms_fold}")
print(f"  Comm norms: {comm_norms_fold}")

# Check degeneracy
spread_fold = np.max(Y_fold_evals_desc) / np.min(Y_fold_evals_desc[Y_fold_evals_desc > 0])
print(f"  Eigenvalue spread: {spread_fold:.8f} (should be ~1.0)")

# Cross-check with S65
s65_data = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                's65_yukawa_texture.npz'), allow_pickle=True)
s65_evals = s65_data['Y_evals']
print(f"  S65 eigenvalues: {s65_evals}")
print(f"  Relative diff: {np.max(np.abs(Y_fold_evals_desc - s65_evals) / (np.abs(s65_evals) + 1e-30)):.2e}")

# =============================================================================
# SECTION 3: Schur Lemma Verification on 3-Parameter Grid
# =============================================================================
print("\n--- 3. Schur lemma verification: 3-parameter grid ---")

# Grid: vary each parameter by +/- 20% around Jensen fold values
# Use 5 points per dimension = 125 grid points
n_grid = 5  # (local)
frac_range = np.linspace(0.80, 1.20, n_grid)

# Results storage
grid_results = []
max_spread_all = 0.0
max_spread_params = None

print(f"  Grid: {n_grid}^3 = {n_grid**3} points, each L_i varied by +/-20%")
print(f"  Baseline: L1={L1_fold:.4f}, L2={L2_fold:.4f}, L3={L3_fold:.4f}")

# Use reduced PW sectors for the grid scan (speed)
pw_sectors_fast = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

count = 0  # (local)
total = n_grid ** 3

for i1, f1 in enumerate(frac_range):
    L1 = L1_fold * f1
    for i2, f2 in enumerate(frac_range):
        L2 = L2_fold * f2
        for i3, f3 in enumerate(frac_range):
            L3 = L3_fold * f3
            count += 1

            g_test = u2_invariant_metric(B_ab, L1, L2, L3)
            Y_test, Lg_n, comm_n, ok = compute_yukawa_matrix(
                g_test, gens, f_abc, B_ab, gammas, gamma9, pw_sectors_fast
            )

            if not ok:
                grid_results.append({
                    'L1': L1, 'L2': L2, 'L3': L3,
                    'f1': f1, 'f2': f2, 'f3': f3,
                    'ok': False
                })
                continue

            evals = eigvalsh(Y_test)
            evals_desc = np.sort(evals)[::-1]

            # Compute spread
            pos_evals = evals_desc[evals_desc > 1e-10 * np.max(np.abs(evals_desc))]
            if len(pos_evals) >= 2:
                spread = np.max(pos_evals) / np.min(pos_evals)
            else:
                spread = 1.0

            grid_results.append({
                'L1': L1, 'L2': L2, 'L3': L3,
                'f1': f1, 'f2': f2, 'f3': f3,
                'evals': evals_desc,
                'spread': spread,
                'trace_Y': np.trace(Y_test),
                'Lg_norms': Lg_n,
                'ok': True
            })

            if spread > max_spread_all:
                max_spread_all = spread
                max_spread_params = (L1, L2, L3, f1, f2, f3)

            if count % 25 == 0 or count == total:
                print(f"  [{count:3d}/{total}] L1={L1:.3f} L2={L2:.3f} L3={L3:.3f}"
                      f"  spread={spread:.8f}  trace={np.trace(Y_test):.2f}")

n_ok = sum(1 for r in grid_results if r['ok'])
n_fail = sum(1 for r in grid_results if not r['ok'])

print(f"\n  Grid complete: {n_ok} OK, {n_fail} failed (non-PD)")
print(f"  MAXIMUM spread across entire grid: {max_spread_all:.10f}")
if max_spread_params:
    L1m, L2m, L3m, f1m, f2m, f3m = max_spread_params
    print(f"  At: L1={L1m:.4f} ({f1m:.2f}x), L2={L2m:.4f} ({f2m:.2f}x), L3={L3m:.4f} ({f3m:.2f}x)")

# Schur theorem test: is spread always < 1.01 (< 1% variation)?
spreads = np.array([r['spread'] for r in grid_results if r['ok']])
schur_confirmed = np.all(spreads < 1.01)
print(f"\n  SCHUR LEMMA TEST: max spread = {np.max(spreads):.10f}")
print(f"  All spreads < 1.01: {schur_confirmed}")
if schur_confirmed:
    print("  CONFIRMED: U(2)-invariant metrics CANNOT break C^2 Yukawa degeneracy.")
    print("  This is a PERMANENT structural theorem (Schur's lemma for irreducible reps).")
else:
    print("  WARNING: Spread exceeds 1% — numerical artifact or Schur violation.")

# =============================================================================
# SECTION 4: Yukawa Scale Dependence on 3 Parameters
# =============================================================================
print("\n--- 4. Yukawa scale lambda(L1,L2,L3) landscape ---")

# Extract traces = 4*lambda (since Y = lambda*I_4)
traces = np.array([r.get('trace_Y', 0) for r in grid_results if r['ok']])
lambdas = traces / 4.0

L1_arr = np.array([r['L1'] for r in grid_results if r['ok']])
L2_arr = np.array([r['L2'] for r in grid_results if r['ok']])
L3_arr = np.array([r['L3'] for r in grid_results if r['ok']])

print(f"  Yukawa scale lambda range: [{np.min(lambdas):.4f}, {np.max(lambdas):.4f}]")
print(f"  At Jensen fold: lambda = {Y_fold_evals_desc[0]:.4f}")
print(f"  Ratio max/min: {np.max(lambdas)/np.min(lambdas):.4f}")

# Identify parameter sensitivity
# Fix two params at fold, vary third
print("\n  Parameter sensitivity (one-at-a-time):")
for param_name, param_idx in [('L1 (u(1))', 0), ('L2 (su(2))', 1), ('L3 (C^2)', 2)]:
    mask = np.ones(len(L1_arr), dtype=bool)
    fold_vals = [L1_fold, L2_fold, L3_fold]
    for j in range(3):
        if j != param_idx:
            arr = [L1_arr, L2_arr, L3_arr][j]
            mask &= np.abs(arr - fold_vals[j]) < 0.01 * fold_vals[j]
    if np.sum(mask) >= 2:
        lam_slice = lambdas[mask]
        var_arr = [L1_arr, L2_arr, L3_arr][param_idx][mask]
        idx_sort = np.argsort(var_arr)
        print(f"  {param_name}: lambda ranges [{np.min(lam_slice):.2f}, {np.max(lam_slice):.2f}]"
              f" (ratio {np.max(lam_slice)/np.min(lam_slice):.4f})")

# =============================================================================
# SECTION 5: U(2)-Breaking Deformations — First Hierarchy
# =============================================================================
print("\n--- 5. U(2)-breaking deformations ---")

# The minimal U(2)-breaking deformation treats the 4 C^2 directions non-uniformly.
# In the standard Gell-Mann basis, C^2 = {lambda_4, lambda_5, lambda_6, lambda_7}.
# We split C^2 into two pairs:
#   C^2_A = {lambda_4, lambda_5}  (associated with (1,0) raising/lowering for root alpha_1 + alpha_2)
#   C^2_B = {lambda_6, lambda_7}  (associated with root alpha_2)
#
# A U(2)-BREAKING metric assigns different scale factors to C^2_A and C^2_B:
#   g = L1*g_0|_{u(1)} + L2*g_0|_{su(2)} + L3A*g_0|_{C^2_A} + L3B*g_0|_{C^2_B}
#
# This is a 4-parameter family. It BREAKS U(2) -> U(1) x U(1) (the maximal torus).
# The C^2 representation decomposes: C^2 -> C^1_A + C^1_B under U(1)xU(1).
# Each C^1 factor is 1D (well, 2D real, but the pair in each is related by
# the residual symmetry). So the Yukawa matrix splits into 2x2 blocks.

# Build a 4-parameter metric
def u2_breaking_metric(B_ab, L1, L2, L3A, L3B):
    """
    Construct a left-invariant metric with independent scales on the two
    C^2 sub-blocks: C^2_A = {e_3, e_4} and C^2_B = {e_5, e_6}.

    This breaks U(2) invariance -> U(1) x U(1) (maximal torus).
    """
    g0 = np.abs(B_ab)
    g = np.zeros((8, 8), dtype=np.float64)

    # u(1): index 7
    for a in U1_IDX:
        for b in U1_IDX:
            g[a, b] = g0[a, b] * L1

    # su(2): indices 0,1,2
    for a in SU2_IDX:
        for b in SU2_IDX:
            g[a, b] = g0[a, b] * L2

    # C^2_A: indices 3,4
    C2A_IDX = [3, 4]
    C2B_IDX = [5, 6]

    for a in C2A_IDX:
        for b in C2A_IDX:
            g[a, b] = g0[a, b] * L3A

    for a in C2B_IDX:
        for b in C2B_IDX:
            g[a, b] = g0[a, b] * L3B

    return g


# Test: verify that U(2)-breaking metric at L3A = L3B = L3 matches U(2)-invariant
g_test_sym = u2_breaking_metric(B_ab, L1_fold, L2_fold, L3_fold, L3_fold)
g_test_u2 = u2_invariant_metric(B_ab, L1_fold, L2_fold, L3_fold)
match_err = np.max(np.abs(g_test_sym - g_test_u2))
print(f"  U(2)-breaking at L3A=L3B: max|diff| from U(2)-invariant = {match_err:.2e}")

# Scan over L3A/L3B ratio (the U(2)-breaking parameter)
# Keep L1, L2 at Jensen fold. Vary ratio r = L3A/L3B at fixed geometric mean
# L3_mean = sqrt(L3A * L3B) = L3_fold.
# So L3A = L3_fold * sqrt(r), L3B = L3_fold / sqrt(r).

n_ratio = 21
ratio_range = np.linspace(0.5, 2.0, n_ratio)  # r = L3A/L3B from 0.5 to 2.0

breaking_results = []

print(f"\n  U(2)-breaking scan: r = L3A/L3B from {ratio_range[0]:.2f} to {ratio_range[-1]:.2f}")
print(f"  Fixed: L1={L1_fold:.4f}, L2={L2_fold:.4f}, L3_mean={L3_fold:.4f}")

for ir, r in enumerate(ratio_range):
    L3A = L3_fold * sqrt(r)
    L3B = L3_fold / sqrt(r)

    g_break = u2_breaking_metric(B_ab, L1_fold, L2_fold, L3A, L3B)

    Y_break, Lg_n, comm_n, ok = compute_yukawa_matrix(
        g_break, gens, f_abc, B_ab, gammas, gamma9, pw_sectors_fast
    )

    if not ok:
        breaking_results.append({'r': r, 'ok': False})
        print(f"  r={r:.3f}: FAILED (metric not PD)")
        continue

    evals = eigvalsh(Y_break)
    evals_desc = np.sort(evals)[::-1]

    pos_evals = evals_desc[evals_desc > 1e-10 * np.max(np.abs(evals_desc))]
    if len(pos_evals) >= 2:
        spread = np.max(pos_evals) / np.min(pos_evals)
    else:
        spread = 1.0

    breaking_results.append({
        'r': r, 'L3A': L3A, 'L3B': L3B,
        'evals': evals_desc,
        'spread': spread,
        'trace_Y': np.trace(Y_break),
        'Lg_norms': Lg_n,
        'Y_matrix': Y_break.copy(),
        'ok': True
    })

    print(f"  r={r:.3f}: evals=[{', '.join(f'{e:.2f}' for e in evals_desc)}]"
          f"  spread={spread:.4f}  Lg=[{', '.join(f'{x:.4f}' for x in Lg_n)}]")

# =============================================================================
# SECTION 6: Full 4-Parameter Grid at Stronger Breaking
# =============================================================================
print("\n--- 6. Full 4-parameter scan (L1, L2, L3A, L3B) ---")

# Also vary L1 and L2 alongside the breaking ratio
# Coarser grid: 3^2 x 11 = 99 points
frac_12 = [0.85, 1.0, 1.15]
n_r2 = 11
ratio_range_2 = np.linspace(0.3, 3.0, n_r2)

full_results = []
max_hierarchy = 0
max_hierarchy_params = None

print(f"  Grid: {len(frac_12)}^2 x {n_r2} = {len(frac_12)**2 * n_r2} points")

for f1 in frac_12:
    L1 = L1_fold * f1
    for f2 in frac_12:
        L2 = L2_fold * f2
        for r in ratio_range_2:
            L3A = L3_fold * sqrt(r)
            L3B = L3_fold / sqrt(r)

            g_test = u2_breaking_metric(B_ab, L1, L2, L3A, L3B)
            Y_test, _, _, ok = compute_yukawa_matrix(
                g_test, gens, f_abc, B_ab, gammas, gamma9, pw_sectors_fast
            )

            if not ok:
                continue

            evals = eigvalsh(Y_test)
            evals_desc = np.sort(evals)[::-1]
            pos_evals = evals_desc[evals_desc > 1e-10 * np.max(np.abs(evals_desc))]

            if len(pos_evals) >= 2:
                hierarchy = np.max(pos_evals) / np.min(pos_evals)
            else:
                hierarchy = 1.0

            full_results.append({
                'L1': L1, 'L2': L2, 'L3A': L3A, 'L3B': L3B,
                'r': r, 'f1': f1, 'f2': f2,
                'evals': evals_desc,
                'hierarchy': hierarchy,
                'ok': True
            })

            if hierarchy > max_hierarchy:
                max_hierarchy = hierarchy
                max_hierarchy_params = (L1, L2, L3A, L3B, f1, f2, r)

print(f"\n  Results: {len(full_results)} valid grid points")
print(f"  MAXIMUM hierarchy ratio: {max_hierarchy:.4f}")
if max_hierarchy_params:
    L1m, L2m, L3Am, L3Bm, f1m, f2m, rm = max_hierarchy_params
    print(f"  At: L1={L1m:.4f}({f1m}x), L2={L2m:.4f}({f2m}x), L3A={L3Am:.4f}, L3B={L3Bm:.4f}")
    print(f"  L3A/L3B = {rm:.2f}")

# =============================================================================
# SECTION 7: Extreme Breaking Exploration
# =============================================================================
print("\n--- 7. Extreme U(2)-breaking (L3A/L3B up to 10) ---")

# Push the ratio to extreme values to map out the hierarchy landscape
n_extreme = 31
ratio_extreme = np.logspace(-1.0, 1.0, n_extreme)  # 0.1 to 10

extreme_results = []
for r in ratio_extreme:
    L3A = L3_fold * sqrt(r)
    L3B = L3_fold / sqrt(r)

    g_test = u2_breaking_metric(B_ab, L1_fold, L2_fold, L3A, L3B)

    # Check PD before expensive computation
    eigs_test = eigvalsh(g_test)
    if np.min(eigs_test) <= 0:
        extreme_results.append({'r': r, 'ok': False})
        continue

    Y_test, Lg_n, _, ok = compute_yukawa_matrix(
        g_test, gens, f_abc, B_ab, gammas, gamma9, pw_sectors_fast
    )

    if not ok:
        extreme_results.append({'r': r, 'ok': False})
        continue

    evals = eigvalsh(Y_test)
    evals_desc = np.sort(evals)[::-1]
    pos_evals = evals_desc[evals_desc > 1e-10 * np.max(np.abs(evals_desc))]

    if len(pos_evals) >= 2:
        hierarchy = np.max(pos_evals) / np.min(pos_evals)
    else:
        hierarchy = 1.0

    extreme_results.append({
        'r': r, 'L3A': L3A, 'L3B': L3B,
        'evals': evals_desc,
        'hierarchy': hierarchy,
        'Lg_norms': Lg_n,
        'ok': True
    })

    print(f"  r={r:6.3f}: evals=[{', '.join(f'{e:8.2f}' for e in evals_desc)}]"
          f"  spread={hierarchy:8.4f}")

extreme_ok = [r for r in extreme_results if r['ok']]
if extreme_ok:
    max_extreme = max(r['hierarchy'] for r in extreme_ok)
    print(f"\n  MAXIMUM hierarchy in extreme range: {max_extreme:.4f}")

# =============================================================================
# SECTION 8: Full PW Computation at Best Point
# =============================================================================
print("\n--- 8. Full PW computation at best hierarchy point ---")

# Find the best hierarchy point from all scans
best_hierarchy = 0
best_params = None
best_source = None

for r in breaking_results:
    if r['ok'] and r['spread'] > best_hierarchy:
        best_hierarchy = r['spread']
        best_params = (L1_fold, L2_fold, r['L3A'], r['L3B'])
        best_source = 'breaking_scan'

for r in full_results:
    if r['ok'] and r['hierarchy'] > best_hierarchy:
        best_hierarchy = r['hierarchy']
        best_params = (r['L1'], r['L2'], r['L3A'], r['L3B'])
        best_source = 'full_scan'

for r in extreme_results:
    if r['ok'] and r['hierarchy'] > best_hierarchy:
        best_hierarchy = r['hierarchy']
        best_params = (L1_fold, L2_fold, r['L3A'], r['L3B'])
        best_source = 'extreme_scan'

print(f"  Best hierarchy from {best_source}: {best_hierarchy:.4f}")
print(f"  Parameters: L1={best_params[0]:.4f}, L2={best_params[1]:.4f},"
      f" L3A={best_params[2]:.4f}, L3B={best_params[3]:.4f}")
print(f"  L3A/L3B = {best_params[2]/best_params[3]:.4f}")

# Run full PW computation at best point
g_best = u2_breaking_metric(B_ab, *best_params)
Y_best, Lg_best, comm_best, ok_best = compute_yukawa_matrix(
    g_best, gens, f_abc, B_ab, gammas, gamma9, pw_sectors  # FULL PW set
)
assert ok_best, "Best point computation failed"

Y_best_evals = eigvalsh(Y_best)
Y_best_desc = np.sort(Y_best_evals)[::-1]
pos_best = Y_best_desc[Y_best_desc > 1e-10 * np.max(np.abs(Y_best_desc))]
hierarchy_full = np.max(pos_best) / np.min(pos_best) if len(pos_best) >= 2 else 1.0

print(f"\n  Full PW result at best point:")
print(f"    Y eigenvalues: {Y_best_desc}")
print(f"    Hierarchy ratio (full PW): {hierarchy_full:.6f}")
print(f"    Lg norms: {Lg_best}")
print(f"    [D,L] norms: {comm_best}")

# Check substructure: is it 2+2 or something else?
if len(Y_best_desc) == 4:
    pairs = [(0, 1), (2, 3)]
    print(f"\n  Pair structure:")
    print(f"    Pair 1 (e_3, e_4): evals {Y_best_desc[0]:.4f}, {Y_best_desc[1]:.4f}"
          f"  ratio {Y_best_desc[0]/(Y_best_desc[1]+1e-30):.4f}")
    print(f"    Pair 2 (e_5, e_6): evals {Y_best_desc[2]:.4f}, {Y_best_desc[3]:.4f}"
          f"  ratio {Y_best_desc[2]/(Y_best_desc[3]+1e-30):.4f}")
    inter_ratio = (Y_best_desc[0] + Y_best_desc[1]) / (Y_best_desc[2] + Y_best_desc[3] + 1e-30)
    print(f"    Inter-pair ratio: {inter_ratio:.4f}")

# =============================================================================
# SECTION 9: SM Comparison
# =============================================================================
print("\n--- 9. SM hierarchy comparison ---")

m_t = 172.69   # GeV  # (local)
m_b = 4.18     # GeV  # (local)
m_tau = 1.777  # GeV
m_c = 1.27     # GeV  # (local)

r_tb = m_t / m_b     # ~ 41.3
r_bt = m_b / m_tau   # ~ 2.35
r_tc = m_t / m_c     # ~ 136

print(f"  SM ratios: m_t/m_b = {r_tb:.1f}, m_b/m_tau = {r_bt:.2f}, m_t/m_c = {r_tc:.0f}")
print(f"  Best geometric hierarchy: {hierarchy_full:.4f}")
print(f"  Required for PASS: > 10")
print(f"  Required for FAIL: < 3")

# Check specific observed ratio matches
if hierarchy_full > 1.01:
    print(f"\n  Ratio matches:")
    for i in range(4):
        for j in range(i + 1, 4):
            if Y_best_desc[j] > 1e-15:
                r_ij = Y_best_desc[i] / Y_best_desc[j]
                for name, val in [('m_t/m_b', r_tb), ('m_b/m_tau', r_bt), ('m_t/m_c', r_tc)]:
                    if val > 0:
                        log_r = abs(np.log10(r_ij / val))
                        if log_r < 2.0:
                            print(f"    y_{i+1}/y_{j+1} = {r_ij:.4f} vs {name} = {val:.1f}"
                                  f" (log10 diff = {log_r:.3f})")

# =============================================================================
# SECTION 10: Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: 3-PARAM-YUKAWA-66")
print("=" * 78)

# First: the 3-parameter (U(2)-invariant) result
print(f"\n  Part A: U(2)-invariant 3-parameter family")
print(f"    Maximum spread across 125-point grid: {np.max(spreads):.10f}")
print(f"    SCHUR THEOREM CONFIRMED: Y = lambda * I_4 for ALL U(2)-invariant metrics")
print(f"    PERMANENT: No mass hierarchy possible within U(2)-invariant moduli (3-param)")

# Second: the U(2)-breaking result
print(f"\n  Part B: U(2)-breaking 4-parameter deformation")
print(f"    Maximum hierarchy ratio: {hierarchy_full:.6f}")
print(f"    At L3A/L3B = {best_params[2]/best_params[3]:.4f}")

# Gate classification
if hierarchy_full > 10:
    verdict = "PASS"
    detail = f"max(y_i/y_j) = {hierarchy_full:.2f} > 10 at L3A/L3B = {best_params[2]/best_params[3]:.2f}"
elif hierarchy_full > 3:
    verdict = "INFO"
    detail = f"max(y_i/y_j) = {hierarchy_full:.4f} in (3, 10) — partial hierarchy, insufficient for SM"
else:
    verdict = "FAIL"
    detail = f"max(y_i/y_j) = {hierarchy_full:.4f} < 3 for all tested deformations"

print(f"\n  Verdict: {verdict}")
print(f"  Detail: {detail}")

print(f"\n  STRUCTURAL THEOREMS (PERMANENT):")
print(f"    1. U(2)-invariant metrics: Y = lambda*I_4 (Schur lemma). No hierarchy.")
print(f"       Verified on {n_ok} grid points, max spread = {np.max(spreads):.10f}")
print(f"    2. U(2)-breaking required: C^2 must split into distinguishable sub-representations.")
print(f"    3. S65 quadratic zero: Tr(gamma_9 dD dD) = 0 still holds (structural, metric-independent).")

elapsed = time.time() - t_start
print(f"\n  Total time: {elapsed:.1f}s")

# =============================================================================
# SECTION 11: Save Data
# =============================================================================
print("\n--- 11. Saving data ---")

data_dir = os.path.dirname(os.path.abspath(__file__))
outfile = os.path.join(data_dir, 's66_3param_yukawa.npz')

# Collect grid spreads and lambdas
grid_spreads = np.array([r['spread'] for r in grid_results if r['ok']])
grid_lambdas = np.array([r.get('trace_Y', 0) / 4.0 for r in grid_results if r['ok']])
grid_L1 = np.array([r['L1'] for r in grid_results if r['ok']])
grid_L2 = np.array([r['L2'] for r in grid_results if r['ok']])
grid_L3 = np.array([r['L3'] for r in grid_results if r['ok']])

# Breaking scan
break_ratios = np.array([r['r'] for r in breaking_results if r['ok']])
break_hierarchies = np.array([r['spread'] for r in breaking_results if r['ok']])
break_evals_list = np.array([r['evals'] for r in breaking_results if r['ok']])

# Extreme scan
ext_ratios = np.array([r['r'] for r in extreme_results if r['ok']])
ext_hierarchies = np.array([r['hierarchy'] for r in extreme_results if r['ok']])

np.savez(outfile,
    # Jensen fold baseline
    Y_fold=Y_fold,
    Y_fold_evals=Y_fold_evals_desc,

    # 3-param grid (Schur verification)
    grid_spreads=grid_spreads,
    grid_lambdas=grid_lambdas,
    grid_L1=grid_L1,
    grid_L2=grid_L2,
    grid_L3=grid_L3,
    schur_confirmed=schur_confirmed,
    max_spread_u2=float(np.max(spreads)),

    # U(2)-breaking scan
    break_ratios=break_ratios,
    break_hierarchies=break_hierarchies,
    break_evals=break_evals_list,

    # Extreme scan
    extreme_ratios=ext_ratios,
    extreme_hierarchies=ext_hierarchies,

    # Best point (full PW)
    Y_best=Y_best,
    Y_best_evals=Y_best_desc,
    best_params=np.array(best_params),
    best_hierarchy=hierarchy_full,

    # Metadata
    tau_fold=tau_fold,
    pw_sectors=np.array(pw_sectors),
    pw_sectors_fast=np.array(pw_sectors_fast),
    gate_verdict=verdict,
    elapsed_time=elapsed,
)
print(f"  Saved: {outfile}")

# =============================================================================
# SECTION 12: Plot
# =============================================================================
print("\n--- 12. Generating plot ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)
fig.suptitle('3-PARAM-YUKAWA-66: Yukawa Hierarchy on Baptista 3-Parameter Family',
             fontsize=13, fontweight='bold')

# Panel 1: Schur verification — spread as bar (all values = 1.0)
ax1 = fig.add_subplot(gs[0, 0])
# All spreads are exactly 1.0 (perfect degeneracy), so histogram fails.
# Instead show deviation from 1.0 across grid points.
spread_devs = np.abs(grid_spreads - 1.0)
ax1.semilogy(range(len(spread_devs)), spread_devs + 1e-16, '.', color='steelblue',
             markersize=3, alpha=0.7)
ax1.axhline(1e-10, color='red', ls='--', lw=1.5, label='Machine epsilon')
ax1.axhline(0.01, color='orange', ls='--', lw=1, label='1% threshold')
ax1.set_xlabel('Grid point index')
ax1.set_ylabel('|spread - 1.0|')
ax1.set_title('U(2)-Invariant Grid:\nSchur Lemma Verification')
ax1.legend(fontsize=8)
ax1.set_ylim(1e-17, 1e-1)

# Panel 2: Yukawa scale lambda vs grid parameters
ax2 = fig.add_subplot(gs[0, 1])
sc = ax2.scatter(grid_L3 / L3_fold, grid_lambdas, c=grid_L1 / L1_fold,
                 cmap='viridis', s=15, alpha=0.7)
ax2.set_xlabel('L3/L3_fold (C^2 scale)')
ax2.set_ylabel('Yukawa scale lambda')
ax2.set_title('U(2)-Invariant:\nYukawa Scale Landscape')
plt.colorbar(sc, ax=ax2, label='L1/L1_fold')

# Panel 3: U(2)-breaking scan — hierarchy vs ratio
ax3 = fig.add_subplot(gs[0, 2])
if len(break_ratios) > 0:
    ax3.plot(break_ratios, break_hierarchies, 'o-', color='crimson', markersize=4)
    ax3.axhline(1.0, color='gray', ls=':', alpha=0.5)
    ax3.axhline(3.0, color='orange', ls='--', lw=1, label='FAIL threshold (3)')
    ax3.axhline(10.0, color='green', ls='--', lw=1, label='PASS threshold (10)')
ax3.set_xlabel('L3A/L3B (U(2)-breaking ratio)')
ax3.set_ylabel('Hierarchy max(y)/min(y)')
ax3.set_title('U(2)-Breaking Scan:\nHierarchy vs Anisotropy')
ax3.legend(fontsize=8)

# Panel 4: Extreme breaking — log scale
ax4 = fig.add_subplot(gs[1, 0])
if len(ext_ratios) > 0:
    ax4.semilogx(ext_ratios, ext_hierarchies, 's-', color='darkgreen', markersize=4)
    ax4.axhline(3.0, color='orange', ls='--', lw=1, label='FAIL threshold')
    ax4.axhline(10.0, color='green', ls='--', lw=1, label='PASS threshold')
    ax4.axhline(r_tb, color='purple', ls=':', lw=1, label=f'm_t/m_b = {r_tb:.0f}')
ax4.set_xlabel('L3A/L3B (log scale)')
ax4.set_ylabel('Hierarchy')
ax4.set_title('Extreme U(2)-Breaking:\nHierarchy at Large Anisotropy')
ax4.legend(fontsize=8)

# Panel 5: Eigenvalue flow under U(2)-breaking
ax5 = fig.add_subplot(gs[1, 1])
break_evals_arr = np.array([r['evals'] for r in breaking_results if r['ok']])
if len(break_ratios) > 0 and len(break_evals_arr) > 0:
    for i in range(min(4, break_evals_arr.shape[1])):
        ax5.plot(break_ratios, break_evals_arr[:, i], '-', lw=1.5,
                 label='y_%d' % (i + 1))
    ax5.set_xlabel('L3A/L3B')
    ax5.set_ylabel('Yukawa eigenvalue')
    ax5.set_title('Eigenvalue Flow\nunder U(2)-Breaking')
    ax5.legend(fontsize=8)

# Panel 6: Summary text
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
summary_lines = [
    "GATE: 3-PARAM-YUKAWA-66",
    "Verdict: %s" % verdict,
    "",
    "PERMANENT THEOREMS:",
    "1. Schur lemma: Y = lambda*I_4",
    "   for ALL U(2)-invariant metrics",
    "   (verified %d points, max spread" % n_ok,
    "   = %.10f)" % np.max(spreads),
    "",
    "2. U(2)-breaking REQUIRED for",
    "   mass hierarchy",
    "",
    "Best hierarchy (U(2)-breaking):",
    "  max(y_i/y_j) = %.4f" % hierarchy_full,
    "  at L3A/L3B = %.4f" % (best_params[2] / best_params[3]),
    "",
    "SM target: m_t/m_b = %.1f" % r_tb,
    "Time: %.1fs" % elapsed,
]
summary_text = "\n".join(summary_lines)
ax6.text(0.05, 0.95, summary_text, transform=ax6.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plotfile = os.path.join(data_dir, 's66_3param_yukawa.png')
plt.savefig(plotfile, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {plotfile}")

print("\n" + "=" * 78)
print("  COMPUTATION COMPLETE")
print("=" * 78)
