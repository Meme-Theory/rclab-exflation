#!/usr/bin/env python3
"""
s66_u1_collapse_spectrum.py — U1-COLLAPSE-SPECTRUM-66
=====================================================

Gate: U1-COLLAPSE-SPECTRUM-66
  PASS: a_0/a_2 has minimum at c_u1 != 1 with value < 0.5 * Jensen
  FAIL: a_0/a_2 monotone in c_u1 or always > Jensen
  INFO: Non-monotone but min > 0.5 * Jensen

Context:
  S65 found U(1) collapse (c_u1 -> 0) INCREASES a_0/a_2 by 195% at eps=0.001
  (wrong direction for CC). This script scans BOTH directions:
  c_u1 < 1 (collapse) and c_u1 > 1 (expansion), checking whether there
  exists ANY c_u1 that decreases the ratio.

  The fiber metric is parametrized as:
    g_u1 = c_u1 * g_fold_u1
  with volume preservation: a^3 * b^4 * (c_u1 * eps_fold) = V_fold
  maintaining a/b = a_fold/b_fold.

  Also checks T-dual inversion symmetry: c_u1 <-> 1/c_u1.

Method:
  1. Curvature-based Seeley-DeWitt sweep (dense, 200 points in log space)
  2. Full D_K eigenvalue spectrum at 11 selected c_u1 values (L_max=3)
  3. Extract a_0, a_2, a_4 from both methods
  4. Plot a_0/a_2 and a_4/a_2 vs c_u1
  5. Test T-duality: compare spectra at c and 1/c

Author: gen-physicist (S66 W7-C)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import time
from scipy.linalg import eigh

t_start = time.time()

script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))
archive_dir = script_dir.parent / 'computations/_shared'
sys.path.insert(0, str(archive_dir))

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI,
    a0_fold, a2_fold, a4_fold,
    g0_diag,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    orthonormal_frame, frame_structure_constants,
    connection_coefficients, validate_connection,
    build_cliff8, validate_clifford, build_chirality,
    spinor_connection_offset, validate_omega_hermitian,
    dirac_operator_on_irrep, get_irrep, validate_irrep,
    U1_IDX, SU2_IDX, C2_IDX,
    _irrep_cache,
)

print("=" * 78)
print("  U1-COLLAPSE-SPECTRUM-66: D_K Spectrum vs U(1) Scale Factor c_u1")
print("=" * 78)

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure
# =============================================================================
print("\n--- 1. SU(3) infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

print(f"  Killing form B[0,0] = {B_ab[0,0]:.4f} (expected -3.0)")
gammas = build_cliff8()
cliff_err = validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")
gamma9 = build_chirality(gammas)

# =============================================================================
# 2. Fold Metric Parameters
# =============================================================================
print("\n--- 2. Fold metric parameters ---")

fold_data = np.load(str(script_dir / 's64_hessian_descent.npz'), allow_pickle=True)
g_fold = fold_data['g_fold']

a_su2_fold = g_fold[0, 0]   # SU(2) metric component
b_c2_fold = g_fold[3, 3]    # C^2 metric component
eps_fold = g_fold[7, 7]     # U(1) metric component

print(f"  a_su2_fold = {a_su2_fold:.6f}")
print(f"  b_c2_fold  = {b_c2_fold:.6f}")
print(f"  eps_fold   = {eps_fold:.6f}")

V_fold = a_su2_fold**3 * b_c2_fold**4 * eps_fold
print(f"  V_fold = a^3 * b^4 * eps = {V_fold:.4f}")

ratio_fold_canonical = a0_fold / a2_fold
print(f"  a_0/a_2 at fold (canonical) = {ratio_fold_canonical:.6f}")

# =============================================================================
# 3. Metric Construction Utilities
# =============================================================================
print("\n--- 3. Metric construction ---")

def three_param_metric(a_su2, b_c2, epsilon):
    """Diagonal left-invariant metric on SU(3) with three independent scales."""
    g = np.zeros((8, 8), dtype=np.float64)
    for i in SU2_IDX:
        g[i, i] = a_su2
    for i in C2_IDX:
        g[i, i] = b_c2
    for i in U1_IDX:
        g[i, i] = epsilon
    return g


def volume_preserving_params(c_u1, a_fold, b_fold, eps_fold_val):
    """
    Compute a_su2, b_c2 for given c_u1 maintaining volume constraint.

    The U(1) metric component is c_u1 * eps_fold.
    Constraint: a^3 * b^4 * (c_u1 * eps_fold) = a_fold^3 * b_fold^4 * eps_fold
    Additional constraint: a/b = a_fold/b_fold (preserve ratio)

    From a = r*b: r^3 * b^7 * c_u1 * eps_fold = V_0
    => b = (V_0 / (r^3 * c_u1 * eps_fold))^{1/7}
    => a = r * b
    """
    V0 = a_fold**3 * b_fold**4 * eps_fold_val
    r = a_fold / b_fold
    eps_new = c_u1 * eps_fold_val
    b = (V0 / (r**3 * eps_new))**(1.0 / 7.0)
    a = r * b
    return a, b, eps_new


# Verify at fold: c_u1 = 1.0
a_test, b_test, eps_test = volume_preserving_params(1.0, a_su2_fold, b_c2_fold, eps_fold)
print(f"  c_u1=1.0: a={a_test:.6f} (fold: {a_su2_fold:.6f}), b={b_test:.6f} (fold: {b_c2_fold:.6f})")
print(f"  eps={eps_test:.6f} (fold: {eps_fold:.6f})")
assert abs(a_test - a_su2_fold) < 1e-10, f"Volume preservation failed: a mismatch"
assert abs(b_test - b_c2_fold) < 1e-10, f"Volume preservation failed: b mismatch"
print("  Volume preservation verified at c_u1=1.0 ✓")

# =============================================================================
# 4. Curvature Computation
# =============================================================================
print("\n--- 4. Curvature engine ---")

def compute_curvature_full(g_metric, f_abc_local):
    """Compute R, |Ric|^2, Kretschner for left-invariant metric on SU(3)."""
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc_local, E)
    Gamma = connection_coefficients(ft)

    n = 8
    Riem = np.zeros((n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    val = 0.0  # (local)
                    for e in range(n):
                        val += Gamma[a, c, e] * Gamma[e, d, b]
                        val -= Gamma[a, d, e] * Gamma[e, c, b]
                        val -= Gamma[a, e, b] * ft[c, d, e]
                    Riem[a, b, c, d] = val

    Ric = np.zeros((n, n))
    for b in range(n):
        for d in range(n):
            for a in range(n):
                Ric[b, d] += Riem[a, b, a, d]

    R_scalar = np.trace(Ric)
    Ric_sq = np.sum(Ric**2)
    K = np.sum(Riem**2)

    return float(R_scalar), float(Ric_sq), float(K)


SPIN_RANK = 16  # (local)
PREFACTOR = (4 * PI)**(-4)
C_a0 = PREFACTOR * SPIN_RANK
C_a2 = PREFACTOR * (20.0 / 3.0)


def seeley_dewitt_from_curvature(R_scalar, Ric_sq, K, g_metric):
    """Compute Seeley-DeWitt coefficients from curvature invariants."""
    Vol = np.sqrt(np.linalg.det(g_metric)) * Vol_SU3_Haar
    a0 = C_a0 * Vol
    a2 = C_a2 * R_scalar * Vol
    C_a4 = PREFACTOR / 360.0
    a4 = C_a4 * (500 * R_scalar**2 - 32 * Ric_sq - 28 * K) * Vol
    return a0, a2, a4, Vol


# Verify at fold
R_fold_val, Ric_sq_fold, K_fold = compute_curvature_full(g_fold, f_abc)
a0_curv_fold, a2_curv_fold, a4_curv_fold, Vol_fold_check = seeley_dewitt_from_curvature(
    R_fold_val, Ric_sq_fold, K_fold, g_fold
)
ratio_curv_fold = a0_curv_fold / a2_curv_fold

print(f"  R(fold) = {R_fold_val:.6f}")
print(f"  a_0(curv, fold) = {a0_curv_fold:.4f}")
print(f"  a_2(curv, fold) = {a2_curv_fold:.4f}")
print(f"  a_0/a_2(curv, fold) = {ratio_curv_fold:.6f}")
print(f"  12/(5*R) = {12.0/(5.0*R_fold_val):.6f}")
print(f"  a_0/a_2(canonical, fold) = {ratio_fold_canonical:.6f}")

# The curvature-based ratio 12/(5R) and the canonical ratio differ because
# canonical a0, a2 are computed from the FULL spectral action (all modes
# with Peter-Weyl multiplicities), not just from the heat kernel asymptotic.
# For this computation, we use a CONSISTENT ratio throughout:
# ratio = a0/a2 from the curvature formula, normalized so that at the fold
# it matches the canonical value.
# Normalization factor:
norm_ratio = ratio_fold_canonical / ratio_curv_fold
print(f"  Normalization factor (canonical/curvature): {norm_ratio:.6f}")

# =============================================================================
# 5. Dense Curvature Sweep: c_u1 from 0.001 to 10.0
# =============================================================================
print("\n--- 5. Dense curvature sweep ---")

# c_u1 values: log-spaced from 0.001 to 10.0
c_u1_values = np.sort(np.unique(np.concatenate([
    np.logspace(-3, 1, 200),       # Dense log grid
    np.array([0.001, 0.01, 0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 5.0, 10.0]),  # Task-specified
    np.array([1.0]),               # Fold reference
])))

results_curv = []

for c_u1 in c_u1_values:
    a_vp, b_vp, eps_new = volume_preserving_params(c_u1, a_su2_fold, b_c2_fold, eps_fold)
    g_cu1 = three_param_metric(a_vp, b_vp, eps_new)

    if np.any(np.diag(g_cu1) <= 0):
        continue

    R_val, Ric_sq_val, K_val = compute_curvature_full(g_cu1, f_abc)
    a0_val, a2_val, a4_val, Vol_val = seeley_dewitt_from_curvature(
        R_val, Ric_sq_val, K_val, g_cu1
    )

    ratio_raw = a0_val / a2_val if abs(a2_val) > 1e-30 else np.inf
    ratio_norm = ratio_raw * norm_ratio  # Normalized to canonical scale

    results_curv.append({
        'c_u1': c_u1,
        'a_su2': a_vp,
        'b_c2': b_vp,
        'eps': eps_new,
        'R': R_val,
        'Ric_sq': Ric_sq_val,
        'K': K_val,
        'a0': a0_val,
        'a2': a2_val,
        'a4': a4_val,
        'Vol': Vol_val,
        'ratio_raw': ratio_raw,
        'ratio_norm': ratio_norm,
    })

# Extract arrays
c_u1_arr = np.array([r['c_u1'] for r in results_curv])
R_arr = np.array([r['R'] for r in results_curv])
ratio_raw_arr = np.array([r['ratio_raw'] for r in results_curv])
ratio_norm_arr = np.array([r['ratio_norm'] for r in results_curv])
a0_arr = np.array([r['a0'] for r in results_curv])
a2_arr = np.array([r['a2'] for r in results_curv])
a4_arr = np.array([r['a4'] for r in results_curv])
Vol_arr_curv = np.array([r['Vol'] for r in results_curv])

# Print key points
print(f"\n  {'c_u1':>10s}  {'a_su2':>8s}  {'b_c2':>8s}  {'eps':>8s}  {'R':>10s}  "
      f"{'a0/a2(raw)':>12s}  {'a0/a2(norm)':>12s}")
print("  " + "-" * 90)
target_cu1 = [0.001, 0.01, 0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 5.0, 10.0]
for r in results_curv:
    if any(abs(r['c_u1'] - t) / max(t, 1e-10) < 0.02 for t in target_cu1):
        tag = " <-- fold" if abs(r['c_u1'] - 1.0) < 0.01 else ""
        print(f"  {r['c_u1']:10.4f}  {r['a_su2']:8.4f}  {r['b_c2']:8.4f}  {r['eps']:8.4f}  "
              f"{r['R']:10.6f}  {r['ratio_raw']:12.6f}  {r['ratio_norm']:12.6f}{tag}")

# =============================================================================
# 6. Find Extrema (PHYSICAL: R > 0 regime only)
# =============================================================================
print("\n--- 6. Extrema analysis ---")

# CRITICAL: a_0/a_2 = 12/(5R). When R passes through zero and goes negative,
# a_2 changes sign (gravity inverts). Negative a_0/a_2 is NOT a physical
# reduction in the CC ratio -- it means the Einstein-Hilbert term flips sign.
# The gate must be evaluated in the R > 0 regime only.

mask_physical = R_arr > 0.0
c_u1_phys = c_u1_arr[mask_physical]
ratio_phys = ratio_raw_arr[mask_physical]
R_phys = R_arr[mask_physical]

print(f"  Total points: {len(c_u1_arr)}")
print(f"  Physical (R > 0) points: {len(c_u1_phys)}")
print(f"  R > 0 range: c_u1 in [{c_u1_phys[0]:.6f}, {c_u1_phys[-1]:.6f}]")

# Find R=0 crossing
R_sign_changes = np.where(np.diff(np.sign(R_arr)))[0]
if len(R_sign_changes) > 0:
    idx_cross = R_sign_changes[0]
    c_u1_Rzero = c_u1_arr[idx_cross] + (c_u1_arr[idx_cross+1] - c_u1_arr[idx_cross]) * \
                 (-R_arr[idx_cross]) / (R_arr[idx_cross+1] - R_arr[idx_cross])
    print(f"  R = 0 crossing at c_u1 ~ {c_u1_Rzero:.4f}")
    print(f"    Above this: R < 0 (gravity inverts, unphysical for CC)")
else:
    c_u1_Rzero = np.inf
    print("  No R = 0 crossing found in scan range")

# Minimum of a_0/a_2 in physical regime
idx_min_phys = np.argmin(ratio_phys)
c_u1_min = c_u1_phys[idx_min_phys]
ratio_min_raw = ratio_phys[idx_min_phys]

print(f"\n  Minimum a_0/a_2 (R>0 regime):")
print(f"    c_u1 = {c_u1_min:.6f}")
print(f"    a_0/a_2 = {ratio_min_raw:.6f}")
print(f"    R at min = {R_phys[idx_min_phys]:.6f}")
print(f"  Fold a_0/a_2: {ratio_curv_fold:.6f}")

# Maximum of R gives minimum of a_0/a_2
idx_Rmax = np.argmax(R_phys)
print(f"\n  Maximum R in physical regime:")
print(f"    c_u1 = {c_u1_phys[idx_Rmax]:.6f}")
print(f"    R_max = {R_phys[idx_Rmax]:.6f}")
print(f"    => min(a_0/a_2) = 12/(5*R_max) = {12.0/(5.0*R_phys[idx_Rmax]):.6f}")

# Check if minimum is at interior or boundary
if 1 < idx_min_phys < len(ratio_phys) - 1:
    print(f"  Interior minimum in R>0 regime at c_u1 = {c_u1_min:.6f}")
    is_interior_min = True
else:
    print(f"  Minimum at boundary of R>0 regime")
    is_interior_min = False

# Monotonicity in R>0 regime
ratio_at_0_001 = ratio_raw_arr[np.argmin(np.abs(c_u1_arr - 0.001))]
ratio_at_1 = ratio_raw_arr[np.argmin(np.abs(c_u1_arr - 1.0))]
# For the upper end, use the largest c_u1 still in R>0
c_u1_upper = c_u1_phys[-1]
ratio_at_upper = ratio_phys[-1]

print(f"\n  a_0/a_2(c_u1=0.001) = {ratio_at_0_001:.6f}")
print(f"  a_0/a_2(c_u1=1.0)   = {ratio_at_1:.6f}")
print(f"  a_0/a_2(c_u1={c_u1_upper:.3f})  = {ratio_at_upper:.6f}")

# The fold (c_u1=1) sits at R_max, so ratio has a minimum there.
# Moving in EITHER direction (collapse or expansion), R decreases, ratio increases.
# This is a U-shaped curve with minimum at c_u1 ~ 1.
if ratio_at_0_001 > ratio_at_1 and ratio_at_upper > ratio_at_1:
    print("  U-SHAPED: minimum near fold (c_u1 ~ 1)")
    monotone_dir = "U-shaped"
elif ratio_at_0_001 > ratio_at_1 > ratio_at_upper:
    print("  Monotone DECREASING with c_u1 (in R>0)")
    monotone_dir = "decreasing"
elif ratio_at_0_001 < ratio_at_1 < ratio_at_upper:
    print("  Monotone INCREASING with c_u1 (in R>0)")
    monotone_dir = "increasing"
else:
    print("  NON-MONOTONE (complex structure)")
    monotone_dir = "non-monotone"

# =============================================================================
# 7. T-Duality Check: c_u1 vs 1/c_u1
# =============================================================================
print("\n--- 7. T-duality check ---")
print("  Testing R(c_u1) vs R(1/c_u1):")

tdual_pairs = [0.1, 0.2, 0.5, 2.0, 5.0, 10.0]
for c in tdual_pairs:
    c_inv = 1.0 / c
    R_c = R_arr[np.argmin(np.abs(c_u1_arr - c))]
    R_cinv = R_arr[np.argmin(np.abs(c_u1_arr - c_inv))]
    ratio_c = ratio_raw_arr[np.argmin(np.abs(c_u1_arr - c))]
    ratio_cinv = ratio_raw_arr[np.argmin(np.abs(c_u1_arr - c_inv))]
    print(f"  c_u1={c:8.4f}: R={R_c:10.6f}, ratio={ratio_c:.6f}  |  "
          f"c_u1={c_inv:8.4f}: R={R_cinv:10.6f}, ratio={ratio_cinv:.6f}  |  "
          f"R_ratio={R_c/R_cinv:.6f}")

# Also check if R(c) * c^alpha = R(1/c) * (1/c)^alpha for some alpha
# i.e., if there's a power-law T-duality
print("\n  Testing power-law T-duality R(c) * c^p = R(1/c) * (1/c)^p:")
for c in [0.1, 0.2, 0.5]:
    c_inv = 1.0 / c
    R_c = R_arr[np.argmin(np.abs(c_u1_arr - c))]
    R_cinv = R_arr[np.argmin(np.abs(c_u1_arr - c_inv))]
    if R_c > 0 and R_cinv > 0:
        # R(c)/R(1/c) = (1/c)^p / c^p = c^{-2p}
        # log(R(c)/R(1/c)) = -2p * log(c)
        p_eff = -np.log(R_c / R_cinv) / (2.0 * np.log(c))
        print(f"  c={c:.2f}: R(c)/R(1/c) = {R_c/R_cinv:.6f}, effective p = {p_eff:.4f}")

# =============================================================================
# 8. Scaling Analysis
# =============================================================================
print("\n--- 8. Scaling analysis ---")

# Fit R vs c_u1 power law in different regimes
# Small c_u1 (collapse)
mask_small = c_u1_arr < 0.5
if np.sum(mask_small) > 5:
    log_c = np.log(c_u1_arr[mask_small])
    log_R = np.log(np.abs(R_arr[mask_small]))
    A = np.vstack([log_c, np.ones(len(log_c))]).T
    coeffs, _, _, _ = np.linalg.lstsq(A, log_R, rcond=None)
    alpha_collapse = coeffs[0]
    print(f"  Collapse regime (c_u1 < 0.5): R ~ c_u1^{alpha_collapse:.4f}")
    print(f"    => a_0/a_2 ~ c_u1^{-alpha_collapse:.4f}")

# Large c_u1 (expansion)
mask_large = c_u1_arr > 2.0
if np.sum(mask_large) > 5:
    log_c = np.log(c_u1_arr[mask_large])
    log_R = np.log(np.abs(R_arr[mask_large]))
    A = np.vstack([log_c, np.ones(len(log_c))]).T
    coeffs, _, _, _ = np.linalg.lstsq(A, log_R, rcond=None)
    alpha_expand = coeffs[0]
    print(f"  Expansion regime (c_u1 > 2.0): R ~ c_u1^{alpha_expand:.4f}")
    print(f"    => a_0/a_2 ~ c_u1^{-alpha_expand:.4f}")

# a_4/a_2 ratio analysis
a4_over_a2_arr = a4_arr / a2_arr
idx_min_42 = np.argmin(a4_over_a2_arr)
print(f"\n  a_4/a_2 minimum at c_u1 = {c_u1_arr[idx_min_42]:.6f}: {a4_over_a2_arr[idx_min_42]:.6f}")
print(f"  a_4/a_2 at fold: {a4_curv_fold / a2_curv_fold:.6f}")

# =============================================================================
# 9. Full D_K Spectrum at Selected c_u1 Values
# =============================================================================
print("\n--- 9. Full D_K spectrum sweep ---")
print("    (L_max = 3, 9 irrep sectors)")

MAX_PQ_SUM = 3  # (local)

def compute_dk_spectrum(g_metric, f_abc_local, gens_local, gammas_local, max_pq=MAX_PQ_SUM):
    """Compute D_K eigenvalue spectrum for a given metric."""
    import dirac_spectrum as t1
    t1._irrep_cache = {}

    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc_local, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas_local)

    mc_err = validate_connection(Gamma)
    _, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)

    sector_data = []
    all_evals_squared = []
    total_modes = 0  # (local)

    # Trivial irrep
    evals_trivial = np.linalg.eigvals(Omega)
    abs_trivial = np.sort(np.abs(evals_trivial))
    sector_data.append((0, 0, abs_trivial, 1))
    for ev in abs_trivial:
        all_evals_squared.append(ev**2)
    total_modes += 16

    for p in range(max_pq + 1):
        for q in range(max_pq + 1 - p):
            if p == 0 and q == 0:
                continue
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2

            try:
                rho, dim_check = get_irrep(p, q, gens_local, f_abc_local)
                assert dim_check == dim_pq
                D_pi = dirac_operator_on_irrep(rho, E, gammas_local, Omega)
                evals_pi = np.linalg.eigvals(D_pi)
                abs_evals_pi = np.sort(np.abs(evals_pi))
                sector_data.append((p, q, abs_evals_pi, dim_pq))
                for ev in abs_evals_pi:
                    # Each eigenvalue has PW multiplicity dim_pq
                    for _ in range(dim_pq):
                        all_evals_squared.append(ev**2)
                total_modes += len(abs_evals_pi) * dim_pq

            except (NotImplementedError, RuntimeError) as e:
                print(f"      WARNING: ({p},{q}) failed: {e}")
                continue

    all_evals_squared = np.sort(np.array(all_evals_squared))

    return all_evals_squared, sector_data, total_modes, mc_err, ah_err


def extract_spectral_moments(evals_sq, Vol):
    """
    Extract effective Seeley-DeWitt coefficients from finite spectrum.

    For a truncated spectrum, the heat kernel expansion is:
      tr(e^{-t D^2}) = sum_k exp(-t * lambda_k^2)

    The asymptotic expansion for t -> 0:
      tr(e^{-t D^2}) ~ (4*pi*t)^{-d/2} * sum_{n=0} a_{2n} * t^n

    For d=8: ~ (4*pi*t)^{-4} * (a_0 + a_2*t + a_4*t^2 + ...)

    From the spectrum: at large cutoff Lambda,
      a_0 = N_modes (total mode count, proportional to Vol)
      a_2 proportional to sum_k 1/lambda_k^2 (zeta function at s=1)
      a_4 proportional to sum_k 1/lambda_k^4 (zeta function at s=2)

    But these spectral sums diverge for zero modes. We compute:
      F_n = sum_k |lambda_k|^{2n} (positive power spectral moments)
    which are what the spectral action actually uses:
      S = Tr(f(D/Lambda)) = sum_k f(lambda_k/Lambda)
      a_0 ~ N_modes (= F_0 = len(evals))
      a_2 ~ sum lambda_k^2 * f'(lambda_k^2/Lambda^2) / Lambda^2

    For a sharp cutoff f = chi_{[0,1]}: S_Lambda = #{|lambda_k| < Lambda}

    We define effective a_n from the heat kernel fit.
    """
    N_modes = len(evals_sq)

    # Remove zero eigenvalues for zeta sums
    mask_nz = evals_sq > 1e-20
    evals_sq_nz = evals_sq[mask_nz]

    # Spectral zeta function: zeta(s) = sum lambda_k^{-2s}
    if len(evals_sq_nz) > 0:
        zeta_1 = np.sum(1.0 / evals_sq_nz)      # sum 1/lambda^2
        zeta_2 = np.sum(1.0 / evals_sq_nz**2)    # sum 1/lambda^4
    else:
        zeta_1 = 0.0  # (local)
        zeta_2 = 0.0

    # Heat kernel fit: tr(exp(-t D^2)) at multiple t values
    # to extract a_0, a_2, a_4 from the asymptotic expansion
    t_vals = np.logspace(-3, -1, 50)
    heat_trace = np.array([np.sum(np.exp(-t * evals_sq)) for t in t_vals])

    # In the small-t limit: K(t) ~ (4*pi*t)^{-4} * (a0 + a2*t + a4*t^2)
    # So: K(t) * (4*pi*t)^4 ~ a0 + a2*t + a4*t^2
    scaled_heat = heat_trace * (4 * PI * t_vals)**4

    # Polynomial fit to extract coefficients
    # Use the smallest t values for the best asymptotic approximation
    mask_fit = t_vals < 0.01
    t_fit = t_vals[mask_fit]
    sh_fit = scaled_heat[mask_fit]

    if len(t_fit) >= 3:
        # Fit: sh = a0 + a2*t + a4*t^2
        A_mat = np.vstack([np.ones(len(t_fit)), t_fit, t_fit**2]).T
        coeffs, _, _, _ = np.linalg.lstsq(A_mat, sh_fit, rcond=None)
        a0_eff = coeffs[0]
        a2_eff = coeffs[1]
        a4_eff = coeffs[2]
    else:
        a0_eff = scaled_heat[0]
        a2_eff = 0.0  # (local)
        a4_eff = 0.0  # (local)

    return {
        'N_modes': N_modes,
        'zeta_1': zeta_1,
        'zeta_2': zeta_2,
        'a0_eff': a0_eff,
        'a2_eff': a2_eff,
        'a4_eff': a4_eff,
        'n_zero': int(np.sum(~mask_nz)),
    }


# Selected c_u1 values for full spectrum computation
c_u1_spectrum = np.array([0.001, 0.01, 0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 5.0, 10.0])

spectrum_results = []

for c_u1 in c_u1_spectrum:
    print(f"\n  c_u1 = {c_u1:.4f}:")

    a_vp, b_vp, eps_new = volume_preserving_params(c_u1, a_su2_fold, b_c2_fold, eps_fold)
    g_cu1 = three_param_metric(a_vp, b_vp, eps_new)

    print(f"    a_su2 = {a_vp:.6f}, b_c2 = {b_vp:.6f}, eps = {eps_new:.6f}")
    V_check = a_vp**3 * b_vp**4 * eps_new
    print(f"    Volume check: {V_check:.4f} (target: {V_fold:.4f})")

    evals_sq, sector_data, total_modes, mc_err, ah_err = compute_dk_spectrum(
        g_cu1, f_abc, gens, gammas, MAX_PQ_SUM
    )

    print(f"    MC error: {mc_err:.2e}, AH error: {ah_err:.2e}")
    print(f"    Total modes (with PW): {total_modes}")
    print(f"    lambda^2 range: [{evals_sq[0]:.6f}, {evals_sq[-1]:.6f}]")

    # Curvature-based
    R_val, Ric_sq_val, K_val = compute_curvature_full(g_cu1, f_abc)
    a0_curv, a2_curv, a4_curv, Vol_check2 = seeley_dewitt_from_curvature(
        R_val, Ric_sq_val, K_val, g_cu1
    )
    ratio_curv = a0_curv / a2_curv

    # Spectral moments from eigenvalues
    moments = extract_spectral_moments(evals_sq, Vol_check2)

    ratio_spec = moments['a0_eff'] / moments['a2_eff'] if abs(moments['a2_eff']) > 1e-30 else np.inf

    print(f"    Curvature: R = {R_val:.6f}, a0/a2(curv) = {ratio_curv:.6f}")
    print(f"    Spectral: a0_eff = {moments['a0_eff']:.2f}, a2_eff = {moments['a2_eff']:.2f}")
    print(f"    Spectral: a0/a2(spec) = {ratio_spec:.6f}")
    print(f"    Zero modes: {moments['n_zero']}")

    spectrum_results.append({
        'c_u1': c_u1,
        'a_su2': a_vp,
        'b_c2': b_vp,
        'eps': eps_new,
        'R': R_val,
        'Ric_sq': Ric_sq_val,
        'K': K_val,
        'a0_curv': a0_curv,
        'a2_curv': a2_curv,
        'a4_curv': a4_curv,
        'Vol': Vol_check2,
        'ratio_curv': ratio_curv,
        'total_modes': total_modes,
        'evals_sq': evals_sq,
        'moments': moments,
        'ratio_spec': ratio_spec,
        'mc_err': mc_err,
        'ah_err': ah_err,
    })

# =============================================================================
# 10. Also compute Jensen (round SU(3)) reference
# =============================================================================
print("\n--- 10. Jensen (round SU(3)) reference ---")

g_jensen = np.diag([g0_diag] * 8)
R_jensen, Ric_sq_jensen, K_jensen = compute_curvature_full(g_jensen, f_abc)
a0_jensen, a2_jensen, a4_jensen, Vol_jensen = seeley_dewitt_from_curvature(
    R_jensen, Ric_sq_jensen, K_jensen, g_jensen
)
ratio_jensen = a0_jensen / a2_jensen

print(f"  R(Jensen) = {R_jensen:.6f}")
print(f"  a_0(Jensen) = {a0_jensen:.4f}")
print(f"  a_2(Jensen) = {a2_jensen:.4f}")
print(f"  a_0/a_2(Jensen) = {ratio_jensen:.6f}")
print(f"  12/(5*R_jensen) = {12.0/(5.0*R_jensen):.6f}")

# NOTE: For the gate, "Jensen" means the round SU(3) metric.
# The S64 theorem proved R(tau) is monotone on the Jensen deformation,
# so a_0/a_2 = 12/(5R) is MINIMIZED at the round metric (tau=0, max curvature)
# and maximized as tau -> infinity.
# The question is whether BREAKING the Jensen path (via U(1) anisotropy)
# can reach a LOWER a_0/a_2 than the round metric.

ratio_gate_ref = ratio_jensen  # Gate reference: Jensen = round SU(3)
print(f"\n  Gate reference (Jensen): a_0/a_2 = {ratio_gate_ref:.6f}")
print(f"  PASS threshold (< 0.5 * Jensen): {0.5 * ratio_gate_ref:.6f}")

# =============================================================================
# 11. Summary Table
# =============================================================================
print("\n--- 11. Summary table ---")

print(f"\n  {'c_u1':>10s}  {'R':>10s}  {'a0/a2(curv)':>12s}  {'a0/a2(spec)':>12s}  "
      f"{'modes':>6s}  {'vs Jensen':>10s}")
print("  " + "-" * 72)

# Jensen reference row
print(f"  {'JENSEN':>10s}  {R_jensen:10.6f}  {ratio_jensen:12.6f}  {'---':>12s}  "
      f"{'---':>6s}  {'1.000':>10s}")

for r in spectrum_results:
    vs_jensen = r['ratio_curv'] / ratio_jensen
    tag = " <-- fold" if abs(r['c_u1'] - 1.0) < 0.01 else ""
    print(f"  {r['c_u1']:10.4f}  {r['R']:10.6f}  {r['ratio_curv']:12.6f}  "
          f"{r['ratio_spec']:12.6f}  {r['total_modes']:6d}  {vs_jensen:10.4f}{tag}")

# =============================================================================
# 12. Gate Verdict
# =============================================================================
print("\n--- 12. Gate verdict: U1-COLLAPSE-SPECTRUM-66 ---")

# IMPORTANT: Use ONLY the R > 0 (physical gravity) regime.
# When R < 0, a_2 < 0, meaning the Einstein-Hilbert term has wrong sign.
# A negative a_0/a_2 does NOT solve the CC problem -- it destroys gravity.

# Use curvature-based ratio in R > 0 regime (most reliable, not truncation-dependent)
phys_spectrum = [r for r in spectrum_results if r['R'] > 0]
min_ratio_curv_phys = min(r['ratio_curv'] for r in phys_spectrum)
min_c_u1_curv_phys = [r['c_u1'] for r in phys_spectrum if r['ratio_curv'] == min_ratio_curv_phys][0]

# Dense sweep in R > 0 regime
min_ratio_dense = np.min(ratio_phys)
min_c_u1_dense = c_u1_phys[np.argmin(ratio_phys)]

print(f"  Reference (Jensen round SU(3)):")
print(f"    a_0/a_2 = {ratio_jensen:.6f}")
print(f"  PASS threshold:")
print(f"    a_0/a_2 < {0.5 * ratio_jensen:.6f}")
print(f"\n  Dense sweep minimum (R > 0 only):")
print(f"    c_u1 = {min_c_u1_dense:.6f}")
print(f"    a_0/a_2 = {min_ratio_dense:.6f}")
print(f"    vs Jensen: {min_ratio_dense / ratio_jensen:.4f}x")
print(f"\n  Spectrum points minimum (R > 0 only):")
print(f"    c_u1 = {min_c_u1_curv_phys:.6f}")
print(f"    a_0/a_2 = {min_ratio_curv_phys:.6f}")
print(f"    vs Jensen: {min_ratio_curv_phys / ratio_jensen:.4f}x")
print(f"\n  R = 0 crossing at c_u1 ~ {c_u1_Rzero:.4f}")
print(f"    Above c_u1 = {c_u1_Rzero:.4f}: gravity inverts, unphysical")

# Key physical finding: the fold metric MAXIMIZES R on the volume-preserving
# U(1)-deformation path. Therefore the fold MINIMIZES a_0/a_2.
# U(1) anisotropy in EITHER direction makes the CC ratio WORSE.
fold_is_min = abs(min_c_u1_dense - 1.0) < 0.15
has_min_below_half = min_ratio_dense < 0.5 * ratio_jensen
has_min_not_at_one = abs(min_c_u1_dense - 1.0) > 0.05

if has_min_below_half and has_min_not_at_one:
    verdict = "PASS"
    verdict_detail = (f"a_0/a_2 has minimum {min_ratio_dense:.6f} at c_u1={min_c_u1_dense:.4f}, "
                     f"which is {min_ratio_dense/ratio_jensen:.2%} of Jensen (< 50% required)")
elif fold_is_min:
    verdict = "FAIL"
    verdict_detail = (f"a_0/a_2 has minimum at c_u1 ~ 1 (fold). "
                     f"U-shaped: increases in BOTH directions. "
                     f"min = {min_ratio_dense:.6f} = {min_ratio_dense/ratio_jensen:.4f}x Jensen. "
                     f"R goes negative at c_u1 > {c_u1_Rzero:.2f} (gravity inverts). "
                     f"U(1) anisotropy cannot reduce CC ratio below fold value.")
elif monotone_dir in ["increasing", "decreasing"]:
    verdict = "FAIL"
    verdict_detail = (f"a_0/a_2 is monotone {monotone_dir} in c_u1 (R>0 regime). "
                     f"Range: [{min_ratio_dense:.6f}, {np.max(ratio_phys):.6f}]")
else:
    # Non-monotone but min > 0.5 * Jensen
    verdict = "INFO"
    verdict_detail = (f"Non-monotone, min at c_u1={min_c_u1_dense:.4f} "
                     f"ratio={min_ratio_dense:.6f} "
                     f"= {min_ratio_dense/ratio_jensen:.4f}x Jensen (> 0.5x)")

print(f"\n  Gate U1-COLLAPSE-SPECTRUM-66: {verdict}")
print(f"  {verdict_detail}")

# =============================================================================
# 13. Analytical Understanding
# =============================================================================
print("\n--- 13. Analytical understanding ---")
print("  The key identity is a_0/a_2 = 12/(5*R) where R is the scalar curvature")
print("  of the left-invariant metric on SU(3).")
print()
print("  For the volume-preserving U(1) deformation (a/b ratio fixed):")
print(f"    R(fold, c_u1=1) = {R_fold_val:.6f}")
print(f"    R(Jensen, round) = {R_jensen:.6f}")
print()

# Compute R at the boundaries
R_at_min_cu1 = R_arr[np.argmin(ratio_raw_arr)]
R_at_max_cu1 = R_arr[np.argmax(ratio_raw_arr)]
print(f"    R at min(a0/a2) [c_u1={min_c_u1_dense:.4f}] = {R_at_min_cu1:.6f} (max R)")
print(f"    R at max(a0/a2) [c_u1={c_u1_arr[np.argmax(ratio_raw_arr)]:.4f}] = {R_at_max_cu1:.6f} (min R)")
print()
print("  The scalar curvature R(c_u1) on the volume-preserving path")
print(f"  has its maximum at c_u1 = {c_u1_arr[np.argmax(R_arr)]:.4f}")
print(f"  R_max = {np.max(R_arr):.6f}")
print(f"  corresponding to a_0/a_2 = 12/(5*R_max) = {12.0/(5.0*np.max(R_arr)):.6f}")

# =============================================================================
# 14. Plotting
# =============================================================================
print("\n--- 14. Generating plots ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('U1-COLLAPSE-SPECTRUM-66: D_K Spectrum vs U(1) Scale Factor',
             fontsize=14, fontweight='bold')

# Panel A: a_0/a_2 vs log10(c_u1) — curvature-based
ax = axes[0, 0]
ax.plot(np.log10(c_u1_arr), ratio_raw_arr, 'b-', linewidth=2, label='Volume-preserving')
ax.axhline(y=ratio_curv_fold, color='r', linestyle='--', alpha=0.7,
           label=f'Fold: {ratio_curv_fold:.4f}')
ax.axhline(y=ratio_jensen, color='g', linestyle=':', alpha=0.7,
           label=f'Jensen: {ratio_jensen:.4f}')
ax.axhline(y=0.5*ratio_jensen, color='orange', linestyle='-.', alpha=0.7,
           label=f'PASS: {0.5*ratio_jensen:.4f}')
ax.axvline(x=0, color='gray', linestyle=':', alpha=0.3)
# Mark spectrum computation points
for r in spectrum_results:
    ax.plot(np.log10(r['c_u1']), r['ratio_curv'], 'ko', markersize=5, zorder=5)
# Mark minimum
ax.plot(np.log10(min_c_u1_dense), min_ratio_dense, 'r*', markersize=12, zorder=6,
        label=f'Min: {min_ratio_dense:.4f} @ {min_c_u1_dense:.3f}')
ax.set_xlabel(r'$\log_{10}(c_{U(1)})$', fontsize=12)
ax.set_ylabel(r'$a_0 / a_2$', fontsize=12)
ax.set_title(r'$a_0/a_2$ vs U(1) scale (curvature)')
ax.legend(fontsize=8, loc='best')
ax.grid(True, alpha=0.3)

# Panel B: R vs log10(c_u1)
ax = axes[0, 1]
ax.plot(np.log10(c_u1_arr), R_arr, 'b-', linewidth=2)
ax.axhline(y=R_fold_val, color='r', linestyle='--', alpha=0.7, label=f'R(fold)={R_fold_val:.4f}')
ax.axhline(y=R_jensen, color='g', linestyle=':', alpha=0.7, label=f'R(Jensen)={R_jensen:.4f}')
ax.axvline(x=0, color='gray', linestyle=':', alpha=0.3)
ax.set_xlabel(r'$\log_{10}(c_{U(1)})$', fontsize=12)
ax.set_ylabel(r'$R$ (scalar curvature)', fontsize=12)
ax.set_title('Scalar curvature vs U(1) scale')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel C: a_4/a_2 vs log10(c_u1)
ax = axes[0, 2]
a4a2_fold_curv = a4_curv_fold / a2_curv_fold
a4a2_jensen = a4_jensen / a2_jensen
ax.plot(np.log10(c_u1_arr), a4_arr / a2_arr, 'b-', linewidth=2)
ax.axhline(y=a4a2_fold_curv, color='r', linestyle='--', alpha=0.7,
           label=f'Fold: {a4a2_fold_curv:.4f}')
ax.axhline(y=a4a2_jensen, color='g', linestyle=':', alpha=0.7,
           label=f'Jensen: {a4a2_jensen:.4f}')
ax.axvline(x=0, color='gray', linestyle=':', alpha=0.3)
ax.set_xlabel(r'$\log_{10}(c_{U(1)})$', fontsize=12)
ax.set_ylabel(r'$a_4 / a_2$', fontsize=12)
ax.set_title(r'$a_4/a_2$ vs U(1) scale (zeta action)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel D: T-duality comparison
ax = axes[1, 0]
# Plot R(c) and R(1/c) on same axes
mask_below = c_u1_arr <= 1.0
mask_above = c_u1_arr >= 1.0
ax.plot(np.log10(c_u1_arr[mask_above]), R_arr[mask_above], 'b-', linewidth=2,
        label=r'$R(c_{U(1)})$, $c \geq 1$')
# For 1/c mapping: at c>1, map to 1/c<1
c_inv_plot = 1.0 / c_u1_arr[mask_above]
R_inv_plot = []
for c_inv in c_inv_plot:
    idx = np.argmin(np.abs(c_u1_arr - c_inv))
    R_inv_plot.append(R_arr[idx])
R_inv_plot = np.array(R_inv_plot)
ax.plot(np.log10(c_u1_arr[mask_above]), R_inv_plot, 'r--', linewidth=2,
        label=r'$R(1/c_{U(1)})$')
ax.set_xlabel(r'$\log_{10}(c_{U(1)})$', fontsize=12)
ax.set_ylabel(r'$R$', fontsize=12)
ax.set_title('T-duality test: R(c) vs R(1/c)')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel E: Individual a_0, a_2 vs c_u1
ax = axes[1, 1]
ax.semilogy(np.log10(c_u1_arr), a0_arr, 'b-', linewidth=2, label=r'$a_0$')
ax.semilogy(np.log10(c_u1_arr), np.abs(a2_arr), 'r-', linewidth=2, label=r'$|a_2|$')
ax.semilogy(np.log10(c_u1_arr), np.abs(a4_arr), 'g-', linewidth=2, label=r'$|a_4|$')
ax.axvline(x=0, color='gray', linestyle=':', alpha=0.3)
ax.set_xlabel(r'$\log_{10}(c_{U(1)})$', fontsize=12)
ax.set_ylabel('Seeley-DeWitt coefficients', fontsize=12)
ax.set_title(r'$a_0, a_2, a_4$ vs U(1) scale')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel F: Spectral density comparison at selected c_u1
ax = axes[1, 2]
colors_spec = plt.cm.viridis(np.linspace(0, 1, len(spectrum_results)))
for i, r in enumerate(spectrum_results):
    if r['c_u1'] in [0.01, 0.1, 1.0, 2.0, 10.0]:
        evals = np.sqrt(np.maximum(r['evals_sq'], 0))
        ax.hist(evals, bins=50, alpha=0.4, color=colors_spec[i],
                label=f'c={r["c_u1"]:.2f}', density=True)
ax.set_xlabel(r'$|\lambda|$ (Dirac eigenvalue)', fontsize=12)
ax.set_ylabel('Density', fontsize=12)
ax.set_title('Spectral density at selected c_u1')
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(str(script_dir / 's66_u1_collapse_spectrum.png'), dpi=150)
print(f"  Plot saved: computations/session-66/s66_u1_collapse_spectrum.png")

# =============================================================================
# 15. Save Data
# =============================================================================
print("\n--- 15. Saving data ---")

# Curvature sweep arrays
np.savez(str(script_dir / 's66_u1_collapse_spectrum.npz'),
         # Dense curvature sweep
         c_u1_dense=c_u1_arr,
         R_dense=R_arr,
         ratio_raw_dense=ratio_raw_arr,
         ratio_norm_dense=ratio_norm_arr,
         a0_dense=a0_arr,
         a2_dense=a2_arr,
         a4_dense=a4_arr,
         Vol_dense=Vol_arr_curv,
         # Spectrum sweep
         c_u1_spectrum=np.array([r['c_u1'] for r in spectrum_results]),
         R_spectrum=np.array([r['R'] for r in spectrum_results]),
         ratio_curv_spectrum=np.array([r['ratio_curv'] for r in spectrum_results]),
         ratio_spec_spectrum=np.array([r['ratio_spec'] for r in spectrum_results]),
         total_modes_spectrum=np.array([r['total_modes'] for r in spectrum_results]),
         a0_curv_spectrum=np.array([r['a0_curv'] for r in spectrum_results]),
         a2_curv_spectrum=np.array([r['a2_curv'] for r in spectrum_results]),
         a4_curv_spectrum=np.array([r['a4_curv'] for r in spectrum_results]),
         # Jensen reference
         R_jensen=R_jensen,
         ratio_jensen=ratio_jensen,
         a0_jensen=a0_jensen,
         a2_jensen=a2_jensen,
         a4_jensen=a4_jensen,
         # Fold reference
         R_fold=R_fold_val,
         ratio_fold_curv=ratio_curv_fold,
         ratio_fold_canonical=ratio_fold_canonical,
         # Extrema (R > 0 physical regime only)
         c_u1_min_phys=min_c_u1_dense,
         ratio_min_phys=min_ratio_dense,
         c_u1_Rzero=c_u1_Rzero,
         # Scaling exponents
         alpha_collapse=alpha_collapse if 'alpha_collapse' in dir() else np.nan,
         alpha_expand=alpha_expand if 'alpha_expand' in dir() else np.nan,
         # Gate
         gate_verdict=verdict,
         gate_detail=verdict_detail,
)

print(f"  Data saved: computations/session-66/s66_u1_collapse_spectrum.npz")

t_end = time.time()
print(f"\n  Total runtime: {t_end - t_start:.1f}s")
print(f"\n  Gate U1-COLLAPSE-SPECTRUM-66: {verdict}")
print(f"  {verdict_detail}")
print("=" * 78)
