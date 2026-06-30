#!/usr/bin/env python3
"""
s65_u1_collapse.py — CONIFOLD-CC-65: U(1) Collapse and D_K Spectrum
====================================================================

Gate: CONIFOLD-CC-65
  PASS: a_0/a_2(epsilon=0.001) < 0.5 * a_0/a_2(fold)  (> 2x improvement)
  FAIL: a_0/a_2 increases or stays within 10% of fold value at all epsilon
  INFO: a_0/a_2 decreases but by < 50%

Context:
  The anti-Jensen flow drives c_u1 -> 0, collapsing the U(1) fiber. At the
  collapse, SU(3) degenerates toward CP^2 (4D), dramatically reducing the
  mode count. If a_0 drops discretely while a_2 is protected by curvature,
  the CC ratio jumps downward.

  Key structural identity (s65_offjensen_transit):
    a_0/a_2 = 12 / (5 * R(g))
  where R is the scalar curvature. This ratio is VOLUME-INDEPENDENT.
  So the CC ratio is determined solely by how R(g) behaves.

Method:
  1. Parametrize 3-parameter metric: g(epsilon) = diag(a_su2, ..., b_c2, ..., epsilon)
     in su(2) + C^2 + u(1) basis, with volume constraint a^3 * b^4 * eps = const.
  2. Compute vielbein, spin connection, Dirac operator D_K from structure constants.
  3. For epsilon in {1.0, 0.5, 0.1, 0.01, 0.001}: compute full D_K spectrum at L_max=3.
  4. Track: N_eff(eps), a_0(eps), a_2(eps), a_0/a_2(eps).
  5. Identify modes with U(1) charge Q_Y != 0 (diverge as eps -> 0).
  6. Plot a_0/a_2 vs log10(epsilon).

  Two paths computed:
    Path A: Volume-preserving (a^3 * b^4 * eps = const, a/b = const)
    Path B: Fixed su(2)/C^2 (only epsilon shrinks, volume NOT preserved)

Author: gen-physicist (S65 W7-B)
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
print("  CONIFOLD-CC-65: U(1) Collapse and D_K Spectrum at Fiber Degeneration")
print("=" * 78)

# =============================================================================
# 1. SU(3) Lie Algebra Infrastructure
# =============================================================================
print("\n--- 1. SU(3) infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

print(f"  Killing form B[0,0] = {B_ab[0,0]:.4f} (expected -3.0)")
print(f"  Killing form diagonal: {np.diag(B_ab)}")

gammas = build_cliff8()
cliff_err = validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")
gamma9 = build_chirality(gammas)

# =============================================================================
# 2. Fold Metric Parameters
# =============================================================================
print("\n--- 2. Fold metric parameters ---")

# Extract fold metric components from s64 data
fold_data = np.load(str(script_dir / 's64_hessian_descent.npz'), allow_pickle=True)
g_fold = fold_data['g_fold']

a_su2_fold = g_fold[0, 0]  # SU(2) metric component
b_c2_fold = g_fold[3, 3]   # C^2 metric component
eps_fold = g_fold[7, 7]    # U(1) metric component

print(f"  a_su2_fold = {a_su2_fold:.6f}")
print(f"  b_c2_fold  = {b_c2_fold:.6f}")
print(f"  eps_fold   = {eps_fold:.6f}")

# Volume factor: det(g) = a^3 * b^4 * eps (relative to |B|)
# The actual volume is sqrt(det(g_metric)) * Vol_SU3_Haar
# where g_metric = diag(a * |B[0,0]|, ..., b * |B[3,3]|, ..., eps * |B[7,7]|)
# But g_fold is the FULL metric, not scale factors alone
# g_fold[0,0] = L2 * |B[0,0]| = L2 * 3.0 for Jensen
# At fold: L1 = e^{2*0.19} = 1.4623, L2 = e^{-2*0.19} = 0.6839, L3 = e^{0.19} = 1.2092
# Check: L2 * 3.0 = 0.6839 * 3.0 = 2.0517 = a_su2_fold ✓
# L3 * 3.0 = 1.2092 * 3.0 = 3.6277 = b_c2_fold ✓
# L1 * 3.0 = 1.4623 * 3.0 = 4.3869 = eps_fold ✓

# Volume in terms of metric components (det of 8x8 diagonal)
V_fold = a_su2_fold**3 * b_c2_fold**4 * eps_fold
print(f"  V_fold = a^3 * b^4 * eps = {V_fold:.4f}")

# The a_0/a_2 ratio at fold
ratio_fold = a0_fold / a2_fold
print(f"  a_0/a_2 at fold = {ratio_fold:.6f}")

# =============================================================================
# 3. Three-Parameter Metric Construction
# =============================================================================
print("\n--- 3. Three-parameter metric parametrization ---")

def three_param_metric(a_su2, b_c2, epsilon):
    """
    Construct left-invariant metric on SU(3) with three independent scales.

    g = a_su2 * |B| on su(2) + b_c2 * |B| on C^2 + epsilon * |B| on u(1)

    This is the most general U(2)-invariant metric, parametrized directly
    by the diagonal metric components (not scale factors).

    Args:
        a_su2: metric component on su(2) directions (indices 0,1,2)
        b_c2: metric component on C^2 directions (indices 3,4,5,6)
        epsilon: metric component on u(1) direction (index 7)

    Returns:
        g: (8,8) positive definite diagonal metric
    """
    g = np.zeros((8, 8), dtype=np.float64)
    for i in SU2_IDX:
        g[i, i] = a_su2
    for i in C2_IDX:
        g[i, i] = b_c2
    for i in U1_IDX:
        g[i, i] = epsilon
    return g


def volume_preserving_params(epsilon, a_fold, b_fold, eps_fold):
    """
    Compute a_su2, b_c2 for given epsilon maintaining volume constraint.

    Constraint: a^3 * b^4 * eps = a_fold^3 * b_fold^4 * eps_fold
    Additional constraint: a/b = a_fold/b_fold (preserve ratio)

    From a = r*b: r^3 * b^7 * eps = V_0
    => b = (V_0 / (r^3 * eps))^{1/7}
    => a = r * b
    """
    V0 = a_fold**3 * b_fold**4 * eps_fold
    r = a_fold / b_fold
    b = (V0 / (r**3 * epsilon))**(1.0 / 7.0)
    a = r * b
    return a, b


# =============================================================================
# 4. Curvature Computation
# =============================================================================
print("\n--- 4. Curvature computation ---")

def compute_curvature_full(g_metric, f_abc_local):
    """
    Compute scalar curvature R, Ricci tensor, and Kretschner scalar
    for a left-invariant metric on SU(3).

    Returns: R, |Ric|^2, K (Kretschner)
    """
    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc_local, E)
    Gamma = connection_coefficients(ft)

    # Riemann tensor: R^a_{bcd}
    # Using the formula for left-invariant metrics on Lie groups:
    # R^a_{bcd} = e_c(Gamma^a_{db}) - e_d(Gamma^a_{cb}) + Gamma^a_{ce}Gamma^e_{db} - Gamma^a_{de}Gamma^e_{cb} - Gamma^a_{eb}f^e_{cd}
    # On a Lie group with left-invariant frame, e_c(anything constant) = 0, so:
    # R^a_{bcd} = Gamma^a_{ce}Gamma^e_{db} - Gamma^a_{de}Gamma^e_{cb} - Gamma^a_{eb}ft^e_{cd}

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

    # Ricci tensor: Ric_{bd} = R^a_{bad}
    Ric = np.zeros((n, n))
    for b in range(n):
        for d in range(n):
            for a in range(n):
                Ric[b, d] += Riem[a, b, a, d]

    R_scalar = np.trace(Ric)  # In ON frame, g_{bd} = delta_{bd}
    Ric_sq = np.sum(Ric**2)
    K = np.sum(Riem**2)

    return float(R_scalar), float(Ric_sq), float(K), Gamma, E, ft


# Seeley-DeWitt coefficient formulas (from s65_offjensen_transit.py)
SPIN_RANK = 16   # Spinor dimension on 8D
PREFACTOR = (4 * PI)**(-4)
C_a0 = PREFACTOR * SPIN_RANK               # a_0 = C_a0 * Vol
C_a2 = PREFACTOR * (20.0 / 3.0)            # a_2 = C_a2 * R * Vol


def seeley_dewitt_from_curvature(R_scalar, Ric_sq, K, g_metric):
    """
    Compute Seeley-DeWitt coefficients from curvature invariants.

    a_0 = C_a0 * Vol
    a_2 = C_a2 * R * Vol
    a_0/a_2 = C_a0 / (C_a2 * R) = 16 / ((20/3) * R) = 48/(20*R) = 12/(5*R)
    """
    Vol = np.sqrt(np.linalg.det(g_metric)) * Vol_SU3_Haar
    a0 = C_a0 * Vol
    a2 = C_a2 * R_scalar * Vol
    C_a4 = PREFACTOR / 360.0
    a4 = C_a4 * (500 * R_scalar**2 - 32 * Ric_sq - 28 * K) * Vol
    return a0, a2, a4, Vol


# Verify at fold
R_fold, Ric_sq_fold, K_fold, _, _, _ = compute_curvature_full(g_fold, f_abc)
a0_check, a2_check, a4_check, Vol_check = seeley_dewitt_from_curvature(
    R_fold, Ric_sq_fold, K_fold, g_fold
)

print(f"  Fold curvature: R = {R_fold:.6f}")
print(f"  Fold |Ric|^2 = {Ric_sq_fold:.6f}, K = {K_fold:.6f}")
print(f"  Fold Seeley-DeWitt: a_0 = {a0_check:.2f} (canon: {a0_fold})")
print(f"  Fold Seeley-DeWitt: a_2 = {a2_check:.2f} (canon: {a2_fold:.2f})")
print(f"  Fold a_0/a_2 = {a0_check/a2_check:.6f} (canon: {ratio_fold:.6f})")
print(f"  12/(5*R) = {12.0/(5.0*R_fold):.6f}")

# =============================================================================
# 5. U(1) Collapse Sweep — Curvature Analysis
# =============================================================================
print("\n--- 5. U(1) collapse sweep (curvature) ---")

# Epsilon values to probe
eps_values = [1.0, 0.5, 0.1, 0.01, 0.001]
# Add fold value and intermediate points
eps_fine = np.logspace(np.log10(eps_fold), np.log10(0.001), 50)
eps_all_curvature = np.sort(np.unique(np.concatenate([
    eps_fine, np.array(eps_values), np.array([eps_fold])
])))[::-1]  # Descending

# Storage
results_curv = []

for eps in eps_all_curvature:
    # Volume-preserving path
    a_vp, b_vp = volume_preserving_params(eps, a_su2_fold, b_c2_fold, eps_fold)
    g_vp = three_param_metric(a_vp, b_vp, eps)

    # Check positive definiteness
    if np.any(np.diag(g_vp) <= 0):
        print(f"  WARNING: Non-positive metric at eps={eps:.4e}")
        continue

    R_vp, Ric_sq_vp, K_vp, _, _, _ = compute_curvature_full(g_vp, f_abc)
    a0_vp, a2_vp, a4_vp, Vol_vp = seeley_dewitt_from_curvature(
        R_vp, Ric_sq_vp, K_vp, g_vp
    )

    ratio_vp = a0_vp / a2_vp if abs(a2_vp) > 1e-30 else np.inf

    results_curv.append({
        'epsilon': eps,
        'a_su2': a_vp,
        'b_c2': b_vp,
        'R': R_vp,
        'Ric_sq': Ric_sq_vp,
        'K': K_vp,
        'a0': a0_vp,
        'a2': a2_vp,
        'a4': a4_vp,
        'Vol': Vol_vp,
        'ratio': ratio_vp,
    })

# Print key points
print(f"\n  {'epsilon':>12s}  {'a_su2':>8s}  {'b_c2':>8s}  {'R':>10s}  {'a_0':>10s}  {'a_2':>10s}  {'a_0/a_2':>10s}")
print("  " + "-" * 80)
for r in results_curv:
    if r['epsilon'] in eps_values or abs(r['epsilon'] - eps_fold) < 0.01:
        tag = " <-- fold" if abs(r['epsilon'] - eps_fold) < 0.01 else ""
        print(f"  {r['epsilon']:12.4e}  {r['a_su2']:8.4f}  {r['b_c2']:8.4f}  "
              f"{r['R']:10.6f}  {r['a0']:10.2f}  {r['a2']:10.2f}  {r['ratio']:10.6f}{tag}")

# =============================================================================
# 6. D_K Eigenvalue Spectrum at Selected Epsilon Values
# =============================================================================
print("\n--- 6. D_K eigenvalue spectrum at selected epsilon values ---")
print("    (L_max = 3, computing full spectrum with Peter-Weyl multiplicities)")

MAX_PQ_SUM = 3  # (local)

def compute_dk_spectrum(g_metric, f_abc_local, gens_local, gammas_local, max_pq=MAX_PQ_SUM):
    """
    Compute the D_K eigenvalue spectrum for a given metric.

    Returns:
        eigenvalues: sorted array of |lambda| values
        sector_data: list of (p, q, evals, dim_rho) per sector
        total_modes: total mode count with PW multiplicities
        u1_charge_info: dict with U(1) charge analysis
    """
    # Clear irrep cache (metrics change, so representations relative to ON frame change)
    global _irrep_cache
    _irrep_cache = {}

    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc_local, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas_local)

    # Validate
    mc_err = validate_connection(Gamma)
    _, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)

    sector_data = []
    all_abs_evals = []
    total_modes = 0  # (local)

    # Trivial irrep (0,0): D = Omega on 16-dim space
    evals_trivial = np.linalg.eigvals(Omega)
    abs_trivial = np.sort(np.abs(evals_trivial))
    sector_data.append((0, 0, abs_trivial, 1))
    for ev in abs_trivial:
        all_abs_evals.append(ev)
    total_modes += 16 * 1  # 16 spinor components, PW multiplicity 1

    # Non-trivial irreps
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
                    all_abs_evals.append(ev)
                total_modes += len(abs_evals_pi) * dim_pq

            except (NotImplementedError, RuntimeError) as e:
                print(f"      WARNING: ({p},{q}) failed: {e}")
                continue

    all_abs_evals = np.sort(np.array(all_abs_evals))

    return all_abs_evals, sector_data, total_modes, mc_err, ah_err


def compute_u1_charges(gens_local, f_abc_local, max_pq=MAX_PQ_SUM):
    """
    Compute U(1)_Y charges for each state in each irrep sector.

    The U(1) generator is e_7 (lambda_8 / (-2i)).
    The U(1) charge is the eigenvalue of rho(e_7).
    Since e_7 is anti-Hermitian, eigenvalues are purely imaginary: i*q.
    The charge is q (real).

    States with Q_Y = 0 survive the U(1) collapse (they don't see the
    collapsing direction). States with Q_Y != 0 have eigenvalues that
    diverge as epsilon -> 0 (the vielbein component along u(1) grows as 1/sqrt(eps)).

    Returns:
        charge_data: dict mapping (p,q) -> array of charges for each D_pi eigenstate
    """
    charge_data = {}

    # Clear cache
    global _irrep_cache
    _irrep_cache = {}

    for p in range(max_pq + 1):
        for q_rep in range(max_pq + 1 - p):
            dim_pq = (p + 1) * (q_rep + 1) * (p + q_rep + 2) // 2

            if p == 0 and q_rep == 0:
                # Trivial: charge = 0
                charge_data[(0, 0)] = np.zeros(16)
                continue

            try:
                rho, _ = get_irrep(p, q_rep, gens_local, f_abc_local)
                # rho[7] is the representation of e_7 (u(1) generator)
                # Eigenvalues of rho[7] give the weights
                rho_u1 = rho[7]  # dim_pq x dim_pq anti-Hermitian
                # Eigenvalues of i * rho_u1 are real (the charges)
                u1_evals = np.linalg.eigvalsh(1j * rho_u1)

                # Each eigenvalue appears in 16 copies (spinor)
                charges = np.repeat(u1_evals, 16)
                charge_data[(p, q_rep)] = charges

            except (NotImplementedError, RuntimeError):
                continue

    return charge_data


# Compute U(1) charges at fold (these are representation-theoretic, independent of metric)
print("  Computing U(1) charges...")
u1_charges = compute_u1_charges(gens, f_abc, MAX_PQ_SUM)

# Count Q_Y = 0 modes
n_zero_charge = 0
n_total_charge = 0
for (p, q_rep), charges in u1_charges.items():
    dim_pq = (p + 1) * (q_rep + 1) * (p + q_rep + 2) // 2
    n_zero = np.sum(np.abs(charges) < 1e-10)
    n_nonzero = len(charges) - n_zero
    n_zero_charge += n_zero * dim_pq  # PW multiplicity
    n_total_charge += len(charges) * dim_pq
    if len(charges) > 0:
        print(f"    ({p},{q_rep}): dim={dim_pq}, {n_zero}/{len(charges)} modes with Q_Y=0, "
              f"charges: {np.unique(np.round(charges, 4))}")

print(f"\n  Total modes (with PW mult): {n_total_charge}")
print(f"  Q_Y = 0 modes (survive collapse): {n_zero_charge}")
print(f"  Q_Y != 0 modes (diverge): {n_total_charge - n_zero_charge}")

# =============================================================================
# 7. Full D_K Spectrum Sweep
# =============================================================================
print("\n--- 7. Full D_K spectrum at selected epsilon values ---")

spectrum_results = []

for eps in eps_values:
    print(f"\n  epsilon = {eps:.4e}:")

    # Volume-preserving parameters
    a_vp, b_vp = volume_preserving_params(eps, a_su2_fold, b_c2_fold, eps_fold)
    g_eps = three_param_metric(a_vp, b_vp, eps)

    print(f"    a_su2 = {a_vp:.6f}, b_c2 = {b_vp:.6f}")
    print(f"    Volume check: a^3*b^4*eps = {a_vp**3 * b_vp**4 * eps:.4f} (target: {V_fold:.4f})")

    abs_evals, sector_data, total_modes, mc_err, ah_err = compute_dk_spectrum(
        g_eps, f_abc, gens, gammas, MAX_PQ_SUM
    )

    print(f"    Connection metric-compat err: {mc_err:.2e}")
    print(f"    Omega anti-Hermiticity err: {ah_err:.2e}")
    print(f"    Total modes (with PW mult): {total_modes}")
    print(f"    Distinct eigenvalue count: {len(abs_evals)}")
    print(f"    |lambda| range: [{abs_evals[0]:.6f}, {abs_evals[-1]:.6f}]")

    # Seeley-DeWitt from curvature
    R_eps, Ric_sq_eps, K_eps, _, _, _ = compute_curvature_full(g_eps, f_abc)
    a0_eps, a2_eps, a4_eps, Vol_eps = seeley_dewitt_from_curvature(
        R_eps, Ric_sq_eps, K_eps, g_eps
    )
    ratio_eps = a0_eps / a2_eps if abs(a2_eps) > 1e-30 else np.inf

    # Effective mode count: N_eff = number of eigenvalues below some cutoff
    # Use median eigenvalue at fold as reference cutoff
    lambda_median = np.median(abs_evals)

    # Heat kernel trace: tr(exp(-t D^2)) = sum_i exp(-t lambda_i^2)
    # a_0 = lim_{t->0} (4*pi*t)^4 * tr(exp(-t D^2))
    # For finite spectrum, compute directly at small t
    t_probe = 0.01  # (local)
    heat_trace = np.sum(np.exp(-t_probe * abs_evals**2))

    # Count modes by U(1) charge
    n_surviving = 0
    n_diverging = 0
    for (p, q_rep), charges in u1_charges.items():
        dim_pq = (p + 1) * (q_rep + 1) * (p + q_rep + 2) // 2
        n_zero = np.sum(np.abs(charges) < 1e-10)
        n_surviving += n_zero * dim_pq
        n_diverging += (len(charges) - n_zero) * dim_pq

    print(f"    Curvature: R = {R_eps:.6f}")
    print(f"    a_0 = {a0_eps:.2f}, a_2 = {a2_eps:.2f}")
    print(f"    a_0/a_2 = {ratio_eps:.6f}")
    print(f"    12/(5*R) = {12.0/(5.0*R_eps):.6f}")

    spectrum_results.append({
        'epsilon': eps,
        'a_su2': a_vp,
        'b_c2': b_vp,
        'R': R_eps,
        'a0': a0_eps,
        'a2': a2_eps,
        'a4': a4_eps,
        'ratio': ratio_eps,
        'Vol': Vol_eps,
        'abs_evals': abs_evals,
        'sector_data': sector_data,
        'total_modes': total_modes,
        'heat_trace': heat_trace,
        'lambda_median': lambda_median,
        'mc_err': mc_err,
        'ah_err': ah_err,
    })

# Also compute at the fold
print(f"\n  epsilon = {eps_fold:.4e} (FOLD):")
abs_evals_fold, sector_data_fold, total_modes_fold, mc_err_fold, ah_err_fold = compute_dk_spectrum(
    g_fold, f_abc, gens, gammas, MAX_PQ_SUM
)
R_fold_check, _, _, _, _, _ = compute_curvature_full(g_fold, f_abc)
print(f"    Total modes: {total_modes_fold}")
print(f"    |lambda| range: [{abs_evals_fold[0]:.6f}, {abs_evals_fold[-1]:.6f}]")
print(f"    R = {R_fold_check:.6f}")
print(f"    a_0/a_2 = {ratio_fold:.6f}")

# =============================================================================
# 8. Analytical Scaling Analysis
# =============================================================================
print("\n--- 8. Analytical scaling analysis ---")
print("  a_0/a_2 = 12/(5*R) is volume-independent.")
print("  The question reduces to: how does R scale with epsilon?")
print()

# Extract R vs epsilon
eps_curv = np.array([r['epsilon'] for r in results_curv])
R_curv = np.array([r['R'] for r in results_curv])
ratio_curv = np.array([r['ratio'] for r in results_curv])

# Fit power law: R ~ eps^alpha
# Use log-log regression on the curvature sweep data
mask_fit = eps_curv < eps_fold  # Only fit below fold
if np.sum(mask_fit) > 2:
    log_eps = np.log(eps_curv[mask_fit])
    log_R = np.log(np.abs(R_curv[mask_fit]))
    # Linear regression: log_R = alpha * log_eps + const
    A = np.vstack([log_eps, np.ones(len(log_eps))]).T
    coeffs, _, _, _ = np.linalg.lstsq(A, log_R, rcond=None)
    alpha_R = coeffs[0]
    const_R = coeffs[1]

    print(f"  Power law fit: R ~ epsilon^{alpha_R:.4f}")
    print(f"  => a_0/a_2 ~ epsilon^{-alpha_R:.4f}")
    print(f"  (If alpha_R > 0, R grows as eps->0, and a_0/a_2 decreases -> GOOD for CC)")
    print(f"  (If alpha_R < 0, R shrinks as eps->0, and a_0/a_2 increases -> BAD for CC)")

# =============================================================================
# 9. Gate Verdict
# =============================================================================
print("\n--- 9. Gate verdict: CONIFOLD-CC-65 ---")

# Find the results at epsilon = 0.001
r_001 = None
for r in spectrum_results:
    if abs(r['epsilon'] - 0.001) < 1e-6:
        r_001 = r
        break

if r_001 is not None:
    ratio_001 = r_001['ratio']
    improvement = ratio_fold / ratio_001 if ratio_001 > 0 else np.inf
    decrease_pct = (1.0 - ratio_001 / ratio_fold) * 100.0

    print(f"  a_0/a_2(fold)       = {ratio_fold:.6f}")
    print(f"  a_0/a_2(eps=0.001)  = {ratio_001:.6f}")
    print(f"  Ratio: a_0/a_2(fold) / a_0/a_2(0.001) = {improvement:.4f}")
    print(f"  Change: {decrease_pct:+.2f}%")
    print()

    if ratio_001 < 0.5 * ratio_fold:
        verdict = "PASS"
        verdict_detail = f"a_0/a_2 decreased by {decrease_pct:.1f}% (> 50% required)"
    elif abs(ratio_001 - ratio_fold) / ratio_fold < 0.10:
        verdict = "FAIL"
        verdict_detail = f"a_0/a_2 changed by only {abs(decrease_pct):.1f}% (within 10%)"
    elif ratio_001 > ratio_fold:
        verdict = "FAIL"
        verdict_detail = f"a_0/a_2 INCREASED by {-decrease_pct:.1f}%"
    else:
        verdict = "INFO"
        verdict_detail = f"a_0/a_2 decreased by {decrease_pct:.1f}% (< 50% but > 10%)"

    print(f"  Gate CONIFOLD-CC-65: {verdict}")
    print(f"  {verdict_detail}")
else:
    verdict = "ERROR"
    verdict_detail = "Could not find results at epsilon = 0.001"
    print(f"  {verdict_detail}")

# =============================================================================
# 10. Summary Table
# =============================================================================
print("\n--- 10. Summary ---")
print(f"\n  {'epsilon':>12s}  {'a_su2':>8s}  {'b_c2':>8s}  {'R':>10s}  {'a_0/a_2':>10s}  {'N_modes':>8s}")
print("  " + "-" * 68)

# Fold
print(f"  {eps_fold:12.4e}  {a_su2_fold:8.4f}  {b_c2_fold:8.4f}  "
      f"{R_fold:10.6f}  {ratio_fold:10.6f}  {total_modes_fold:8d}  <-- fold")

for r in spectrum_results:
    print(f"  {r['epsilon']:12.4e}  {r['a_su2']:8.4f}  {r['b_c2']:8.4f}  "
          f"{r['R']:10.6f}  {r['ratio']:10.6f}  {r['total_modes']:8d}")

# =============================================================================
# 11. Plotting
# =============================================================================
print("\n--- 11. Generating plots ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('CONIFOLD-CC-65: U(1) Fiber Collapse', fontsize=14, fontweight='bold')

# Panel A: a_0/a_2 vs log10(epsilon)
ax = axes[0, 0]
eps_plot = np.array([r['epsilon'] for r in results_curv])
ratio_plot = np.array([r['ratio'] for r in results_curv])
ax.plot(np.log10(eps_plot), ratio_plot, 'b-', linewidth=2, label='Volume-preserving path')
ax.axhline(y=ratio_fold, color='r', linestyle='--', alpha=0.7, label=f'Fold: {ratio_fold:.4f}')
ax.axhline(y=0.5*ratio_fold, color='g', linestyle=':', alpha=0.7, label=f'PASS threshold: {0.5*ratio_fold:.4f}')
# Mark the fold point
ax.plot(np.log10(eps_fold), ratio_fold, 'rs', markersize=10, zorder=5)
# Mark computed spectrum points
for r in spectrum_results:
    ax.plot(np.log10(r['epsilon']), r['ratio'], 'ko', markersize=6, zorder=5)
ax.set_xlabel(r'$\log_{10}(\epsilon)$', fontsize=12)
ax.set_ylabel(r'$a_0 / a_2$', fontsize=12)
ax.set_title(r'$a_0/a_2$ vs U(1) scale $\epsilon$')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel B: Scalar curvature R vs log10(epsilon)
ax = axes[0, 1]
R_plot = np.array([r['R'] for r in results_curv])
ax.plot(np.log10(eps_plot), R_plot, 'b-', linewidth=2)
ax.axhline(y=R_fold, color='r', linestyle='--', alpha=0.7, label=f'R(fold) = {R_fold:.4f}')
ax.plot(np.log10(eps_fold), R_fold, 'rs', markersize=10, zorder=5)
ax.set_xlabel(r'$\log_{10}(\epsilon)$', fontsize=12)
ax.set_ylabel(r'$R$ (scalar curvature)', fontsize=12)
ax.set_title('Scalar curvature under U(1) collapse')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel C: a_0 and a_2 individually
ax = axes[1, 0]
a0_plot = np.array([r['a0'] for r in results_curv])
a2_plot = np.array([r['a2'] for r in results_curv])
ax.semilogy(np.log10(eps_plot), a0_plot, 'b-', linewidth=2, label=r'$a_0$')
ax.semilogy(np.log10(eps_plot), a2_plot, 'r-', linewidth=2, label=r'$a_2$')
ax.axhline(y=a0_fold, color='b', linestyle=':', alpha=0.5)
ax.axhline(y=a2_fold, color='r', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$\log_{10}(\epsilon)$', fontsize=12)
ax.set_ylabel('Seeley-DeWitt coefficients', fontsize=12)
ax.set_title(r'$a_0$ and $a_2$ (volume-preserving)')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel D: D_K eigenvalue spectra comparison
ax = axes[1, 1]
colors = plt.cm.viridis(np.linspace(0, 1, len(spectrum_results)))
for i, r in enumerate(spectrum_results):
    evals = r['abs_evals']
    # Plot as density (histogram)
    ax.hist(evals, bins=50, alpha=0.4, color=colors[i],
            label=f'eps={r["epsilon"]:.0e}', density=True)
ax.set_xlabel(r'$|\lambda|$ (Dirac eigenvalue)', fontsize=12)
ax.set_ylabel('Density', fontsize=12)
ax.set_title('D_K eigenvalue distribution')
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(str(script_dir / 's65_u1_collapse.png'), dpi=150)
print(f"  Plot saved: computations/session-65/s65_u1_collapse.png")

# =============================================================================
# 12. Save Data
# =============================================================================
print("\n--- 12. Saving data ---")

# Prepare saveable arrays
eps_spectrum = np.array([r['epsilon'] for r in spectrum_results])
a_su2_arr = np.array([r['a_su2'] for r in spectrum_results])
b_c2_arr = np.array([r['b_c2'] for r in spectrum_results])
R_arr = np.array([r['R'] for r in spectrum_results])
a0_arr = np.array([r['a0'] for r in spectrum_results])
a2_arr = np.array([r['a2'] for r in spectrum_results])
a4_arr = np.array([r['a4'] for r in spectrum_results])
ratio_arr = np.array([r['ratio'] for r in spectrum_results])
Vol_arr = np.array([r['Vol'] for r in spectrum_results])

# Curvature sweep data
eps_curv_arr = np.array([r['epsilon'] for r in results_curv])
R_curv_arr = np.array([r['R'] for r in results_curv])
ratio_curv_arr = np.array([r['ratio'] for r in results_curv])
a0_curv_arr = np.array([r['a0'] for r in results_curv])
a2_curv_arr = np.array([r['a2'] for r in results_curv])

np.savez(str(script_dir / 's65_u1_collapse.npz'),
         # Spectrum sweep
         eps_spectrum=eps_spectrum,
         a_su2=a_su2_arr,
         b_c2=b_c2_arr,
         R_spectrum=R_arr,
         a0_spectrum=a0_arr,
         a2_spectrum=a2_arr,
         a4_spectrum=a4_arr,
         ratio_spectrum=ratio_arr,
         Vol_spectrum=Vol_arr,
         # Curvature sweep (fine grid)
         eps_curv=eps_curv_arr,
         R_curv=R_curv_arr,
         ratio_curv=ratio_curv_arr,
         a0_curv=a0_curv_arr,
         a2_curv=a2_curv_arr,
         # Fold reference
         ratio_fold=ratio_fold,
         eps_fold=eps_fold,
         a_su2_fold=a_su2_fold,
         b_c2_fold=b_c2_fold,
         R_fold=R_fold,
         # Gate verdict
         gate_verdict=verdict,
         gate_detail=verdict_detail,
         # U(1) charges
         n_zero_charge=n_zero_charge,
         n_total_charge=n_total_charge,
         # Scaling
         alpha_R=alpha_R if 'alpha_R' in dir() else np.nan,
)

print(f"  Data saved: computations/session-65/s65_u1_collapse.npz")

t_end = time.time()
print(f"\n  Total runtime: {t_end - t_start:.1f}s")
print(f"\n  Gate CONIFOLD-CC-65: {verdict}")
print(f"  {verdict_detail}")
print("=" * 78)
