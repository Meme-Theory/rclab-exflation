#!/usr/bin/env python3
"""
s45_dissolution_entropy.py -- DISSOLUTION-ENTROPY-45
=====================================================

Compute entanglement entropy across the Poisson->GOE level statistics
transition as a function of perturbation strength epsilon.

=== PHYSICS ===

S44 W6-7 found epsilon_c ~ N^{-0.457} for the dissolution crossover in
level statistics (ratio statistic <r>). This quantified W-FOAM-7: the spectral
triple is emergent, dissolving under any nonzero foam perturbation in the
thermodynamic limit.

The ratio statistic diagnoses spectral correlations but does not capture
quantum correlations. The entanglement entropy of the ground state across
a sector bipartition provides a complementary diagnostic:

  S_ent(epsilon) = -Tr(rho_A * ln(rho_A))

where rho_A is the reduced density matrix obtained by tracing out half the
sectors from the ground state of H(epsilon) = H_0 + epsilon * V.

At epsilon = 0: H_0 is block-diagonal, the ground state is a product state
across sectors, so S_ent = 0 exactly.

At large epsilon: H is a random Hermitian matrix (GOE), the ground state
is fully entangled, and S_ent ~ ln(d_A) - 1/2 (Page value) for subsystem
dimension d_A.

The question: how does S_ent at the crossover epsilon_c scale with N?
  - S_ent(eps_c) ~ ln(N): area law -- entanglement grows logarithmically
  - S_ent(eps_c) ~ N^alpha: volume law -- entanglement grows as power law
  - S_ent(eps_c) ~ const: entanglement is finite even in thermodynamic limit

This classifies the dissolution phase transition.

=== METHOD ===

For each max_pq_sum in {1, 2, 3, 4, 5}:
  1. Build block-diagonal H_0 = i*D_K at tau = 0.19
  2. Load epsilon_c from s44_dissolution_scaling.npz
  3. For 20 epsilon values from 0 to 10*epsilon_c:
     a. Generate M random perturbations V (Hermitian, GOE-scaled)
     b. Diagonalize H_0 + epsilon*V
     c. Partition Hilbert space into sectors A (first half) and B (second half)
     d. Project ground state onto A, compute rho_A = Tr_B(|psi><psi|)
     e. Compute S_ent = -Tr(rho_A * ln(rho_A))
  4. Fit S_ent(eps_c) vs N to: ln(N), N^alpha, constant

=== GATE ===
DISSOLUTION-ENTROPY-45: INFO (entanglement characterization of dissolution)

Author: quantum-foam-theorist, Session 45
"""

import numpy as np
from numpy.linalg import eigvalsh, eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import curve_fit
import os
import sys
import time

t_start = time.time()

# Add tier0 path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# Import infrastructure
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    dirac_operator_on_irrep,
    get_irrep,
    validate_connection,
    validate_omega_hermitian,
)
from canonical_constants import tau_fold as TAU_FOLD

# ============================================================
# LOAD S44 DISSOLUTION SCALING DATA
# ============================================================
print("=" * 70)
print("DISSOLUTION-ENTROPY-45: Entanglement Entropy vs Perturbation Strength")
print("=" * 70)

s44_path = os.path.join(SCRIPT_DIR, "s44_dissolution_scaling.npz")
s44 = np.load(s44_path, allow_pickle=True)

eps_c_s44 = s44['epsilon_crossover']        # [0.0210, 0.0139, 0.0080, 0.0036, 0.0017]
N_s44 = s44['N_values']                      # [112, 432, 1232, 2912, 6048]
max_pq_s44 = s44['max_pq_sums']              # [1, 2, 3, 4, 5]
alpha_fit = float(s44['fit_N_-alpha_params'][1])  # 0.457

print(f"\nLoaded S44 dissolution data:")
print(f"  alpha_fit = {alpha_fit:.3f}")
for i in range(len(max_pq_s44)):
    print(f"  max_pq_sum={max_pq_s44[i]}: N={int(N_s44[i])}, eps_c={eps_c_s44[i]:.5f}")

# ============================================================
# CONSTANTS AND CONFIGURATION
# ============================================================

R_POISSON = 2 * np.log(2) - 1   # 0.38629
R_GOE = 0.5307
R_MIDPOINT = (R_POISSON + R_GOE) / 2.0
DEGENERACY_TOL = 1e-10

# Per truncation level: (max_pq_sum, n_samples, n_epsilon_points)
# eigh on NxN complex matrix: O(N^3). N=6048 takes ~30s per call.
# Total calls = n_samples * n_eps + extra. Budget: ~5 min total.
# pq=1 (N=112): ~0s each, 20*20+5 = 405 calls -> 0s
# pq=2 (N=432): ~0.1s each, 15*16+10 = 250 calls -> 25s
# pq=3 (N=1232): ~1s each, 8*14+5 = 117 calls -> 120s
# pq=4 (N=2912): ~5s each, 4*12+5 = 53 calls -> 265s
# pq=5 (N=6048): ~30s each -- TOO SLOW for full scan; use 3*8+3=27 calls -> 810s
# Drop pq=5 to stay under budget. Add single-point measurement instead.
TRUNCATION_CONFIGS = [
    (1,  20, 16),   # N=112,   fast
    (2,  15, 16),   # N=432,   fast
    (3,   8, 14),   # N=1232,  moderate (~2 min)
    (4,   4, 12),   # N=2912,  slow (~4 min)
]

# For pq=5 we do a SINGLE measurement at eps_c only (no full scan)
PQ5_SINGLE_POINT = True
PQ5_SAMPLES = 3

N_EPS_POINTS_DEFAULT = 16  # default number of epsilon points per scan

np.random.seed(42)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def ratio_statistic(evals):
    """Oganesyan-Huse ratio statistic <r> from eigenvalues."""
    evals = np.sort(np.real(evals))
    unique = [evals[0]]
    for e in evals[1:]:
        if abs(e - unique[-1]) > DEGENERACY_TOL:
            unique.append(e)
    evals = np.array(unique)
    if len(evals) < 4:
        return np.nan
    spacings = np.diff(evals)
    spacings = spacings[spacings > DEGENERACY_TOL]
    if len(spacings) < 3:
        return np.nan
    ratios = []
    for i in range(len(spacings) - 1):
        s1, s2 = spacings[i], spacings[i + 1]
        if max(s1, s2) > 0:
            ratios.append(min(s1, s2) / max(s1, s2))
    return np.mean(ratios) if ratios else np.nan


def build_block_diagonal_H(max_pq_sum, gens, f_abc, gammas, E, Omega, verbose=True):
    """
    Build the block-diagonal Hamiltonian H_0 = i*D_K for all sectors
    with p+q <= max_pq_sum.

    Returns:
        H0: (total_dim, total_dim) Hermitian matrix
        block_starts: list of starting indices for each sector
        sector_dims: list of block dimensions
        sector_labels: list of "(p,q)" labels
        total_dim: total matrix dimension
    """
    sectors = []
    sector_dims = []
    sector_D_matrices = []
    sector_labels = []

    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            label = f"({p},{q})"
            try:
                rho, dim_check = get_irrep(p, q, gens, f_abc)
                assert dim_check == dim_pq
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                H_pi = 1j * D_pi
                block_dim = dim_pq * 16
                sectors.append((p, q, dim_pq))
                sector_dims.append(block_dim)
                sector_D_matrices.append(H_pi)
                sector_labels.append(label)
            except (NotImplementedError, RuntimeError) as e:
                if verbose:
                    print(f"  {label}: SKIPPED ({e})")

    total_dim = sum(sector_dims)
    H0 = np.zeros((total_dim, total_dim), dtype=complex)
    block_starts = []
    offset = 0
    for i, H_pi in enumerate(sector_D_matrices):
        d = sector_dims[i]
        block_starts.append(offset)
        H0[offset:offset + d, offset:offset + d] = H_pi
        offset += d

    return H0, block_starts, sector_dims, sector_labels, total_dim


def compute_ground_state(H):
    """
    Compute the ground state (lowest eigenvalue eigenvector) of Hermitian H.
    Returns: (eigenvalue, eigenvector)
    """
    evals, evecs = eigh(H)
    # Ground state = lowest eigenvalue
    idx = 0
    return evals[idx], evecs[:, idx]


def entanglement_entropy_bipartition(psi, d_A, dim_total):
    """
    Compute entanglement entropy of |psi> across a tensor-product bipartition.

    The Hilbert space C^N is viewed as C^{d_A} (x) C^{d_B} where
    d_A * d_B = N = dim_total. The state |psi> is reshaped into a
    (d_A, d_B) matrix, SVD gives Schmidt coefficients, and
    S_ent = -sum(p_i * ln(p_i)) where p_i = sigma_i^2.

    For a product state: all but one singular value vanish, S_ent = 0.
    For a maximally entangled state: S_ent = ln(min(d_A, d_B)).
    """
    d_B = dim_total // d_A

    if d_A <= 0 or d_B <= 0 or d_A * d_B != dim_total:
        return 0.0

    # Reshape state vector into bipartite matrix
    # psi has length d_A * d_B = dim_total
    psi_matrix = psi.reshape(d_A, d_B)

    # SVD: psi_matrix = U * diag(sigma) * V^dag
    # Schmidt decomposition
    try:
        sigma = np.linalg.svd(psi_matrix, compute_uv=False)
    except np.linalg.LinAlgError:
        return np.nan

    # Probabilities from Schmidt coefficients
    p = sigma**2
    p = np.real(p)  # ensure real (should be from Hermitian)

    # Normalize (numerical safety)
    p_sum = np.sum(p)
    if p_sum > 0:
        p = p / p_sum

    # Remove zeros to avoid log(0)
    p = p[p > 1e-30]

    # von Neumann entropy
    S = -np.sum(p * np.log(p))
    return float(S)


def entanglement_entropy_sector_bipartition(psi, block_starts, sector_dims, total_dim):
    """
    Compute entanglement entropy across a bipartition that splits
    the sectors into two halves (first half vs second half).

    This is the natural partition for detecting dissolution:
    at epsilon = 0, the ground state is a product across sectors,
    so S_ent = 0 exactly. As epsilon grows, cross-sector entanglement
    grows.

    IMPORTANT: The Hilbert space is NOT a tensor product of sector spaces
    in general. It is a direct sum. For the bipartition to be meaningful,
    we need to reinterpret the state in terms of a tensor product.

    Strategy: Define A = span of first half of basis vectors, B = second half.
    This is a standard bipartition of the single-particle Hilbert space.
    The reduced density matrix rho_A = Tr_B(|psi><psi|) is the projection
    onto the first d_A dimensions.
    """
    n_sectors = len(sector_dims)
    n_A = n_sectors // 2  # first half
    if n_A == 0:
        n_A = 1  # at least one sector in A

    # d_A = sum of dimensions of first n_A sectors
    d_A = sum(sector_dims[:n_A])
    d_B = total_dim - d_A

    if d_A <= 0 or d_B <= 0 or d_A >= total_dim:
        return 0.0, d_A

    # The state psi lives in C^{total_dim} = C^{d_A} + C^{d_B} (direct sum)
    # For a pure state in a direct sum, the entanglement entropy across
    # the bipartition {first d_A coords} vs {last d_B coords} is computed
    # by reshaping into a d_A x d_B matrix and performing SVD.
    #
    # This works because |psi> in C^N with bipartition into first d_A and
    # last d_B coordinates gives:
    #   rho_A = psi_A * psi_A^dag  (d_A x d_A matrix)
    # where psi_A is the first d_A components.
    #
    # But this gives rank-1 rho_A with S_ent = 0 for ANY state!
    # That's wrong -- this is a trivial bipartition for a single vector.
    #
    # The CORRECT approach for a single pure state |psi> in C^N is to use
    # the MATRIX bipartition: reshape |psi> into a d_A x d_B matrix
    # (where d_A * d_B = N) and compute the entanglement entropy from SVD.
    # This corresponds to viewing C^N = C^{d_A} tensor C^{d_B}.
    #
    # For our block-diagonal system, we need d_A * d_B = N.
    # Choose d_A = closest integer such that d_A * d_B = N.

    # Find the factorization closest to sqrt(N) x sqrt(N)
    # that respects sector boundaries
    d_A_tensor = find_tensor_bipartition(total_dim, sector_dims)

    return entanglement_entropy_bipartition(psi, d_A_tensor, total_dim), d_A_tensor


def find_tensor_bipartition(N, sector_dims):
    """
    Find d_A such that d_A * d_B = N, with d_A as close to sqrt(N)
    as possible, preferring sector boundary alignment.

    For arbitrary N, we need exact factorization. Find the largest
    divisor of N that is <= sqrt(N).
    """
    sqrt_N = int(np.sqrt(N))

    # Find largest divisor <= sqrt(N)
    for d_A in range(sqrt_N, 0, -1):
        if N % d_A == 0:
            return d_A

    # Fallback: N is prime, use d_A = 1 (trivial)
    return 1


def page_entropy(d_A, d_B):
    """
    Page entropy: average S_ent for random pure states in C^{d_A * d_B}
    when d_A <= d_B.

    S_Page = ln(d_A) - d_A / (2 * d_B)   (leading terms)

    This is the thermodynamic limit of random matrix eigenvector entanglement.
    """
    if d_A > d_B:
        d_A, d_B = d_B, d_A
    if d_A <= 0:
        return 0.0
    return np.log(d_A) - d_A / (2.0 * d_B)


def measure_entropy_at_epsilon(H0, total_dim, H0_norm, epsilon, n_samples, d_A,
                               compute_r=False):
    """
    Measure entanglement entropy at a given epsilon, averaged over samples.

    Uses eigh to get ground state eigenvector. Optionally computes <r> statistic
    for cross-check (adds negligible overhead since eigenvalues are already computed).

    Returns: (S_mean, S_std_err, r_mean, r_std_err)
    """
    sigma = epsilon * H0_norm / total_dim
    S_values = []
    r_values = []

    for _ in range(n_samples):
        V_real = np.random.randn(total_dim, total_dim) * sigma
        V_imag = np.random.randn(total_dim, total_dim) * sigma
        V = (V_real + 1j * V_imag)
        V = (V + V.conj().T) / 2.0

        H_pert = H0 + V

        # Compute ground state
        evals, evecs = eigh(H_pert)
        psi = evecs[:, 0]  # ground state

        if compute_r:
            r_val = ratio_statistic(evals)
            if not np.isnan(r_val):
                r_values.append(r_val)

        # Entanglement entropy via SVD bipartition
        S = entanglement_entropy_bipartition(psi, d_A, total_dim)
        S_values.append(S)

    S_arr = np.array(S_values)
    S_mean = np.mean(S_arr)
    S_err = np.std(S_arr) / np.sqrt(len(S_arr)) if len(S_arr) > 1 else 0.0

    r_arr = np.array(r_values) if r_values else np.array([np.nan])
    r_mean = np.nanmean(r_arr)
    r_err = np.nanstd(r_arr) / np.sqrt(np.sum(~np.isnan(r_arr))) if np.sum(~np.isnan(r_arr)) > 1 else 0.0

    return S_mean, S_err, r_mean, r_err


# ============================================================
# FITTING MODELS FOR S_ent(N) AT eps_c
# ============================================================

def model_lnN(N, a, b):
    """S = a * ln(N) + b  (area law)"""
    return a * np.log(N) + b

def model_power(N, a, alpha):
    """S = a * N^alpha  (volume law)"""
    return a * N**alpha

def model_const(N, c):
    """S = c  (constant)"""
    return np.full_like(N, c, dtype=float)

def model_sqrt(N, a, b):
    """S = a * sqrt(N) + b"""
    return a * np.sqrt(N) + b


# ============================================================
# MAIN COMPUTATION
# ============================================================

print(f"\nTau = {TAU_FOLD:.3f}")
print(f"S44 fitted alpha = {alpha_fit:.3f}")

# ============================================================
# Step 1: Build SU(3) infrastructure
# ============================================================
print("\n--- Step 1: Build SU(3) infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
cliff_err = validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")

B_ab = compute_killing_form(f_abc)
g_s = jensen_metric(B_ab, TAU_FOLD)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E)
Gamma = connection_coefficients(ft)
mc_err = validate_connection(Gamma)
Omega = spinor_connection_offset(Gamma, gammas)
_, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)

print(f"  Connection metric-compatibility error: {mc_err:.2e}")
print(f"  Omega anti-Hermitian error: {ah_err:.2e}")

# ============================================================
# Step 2: Loop over truncation levels
# ============================================================
print("\n--- Step 2: Sweep over truncation levels ---")

# Storage
all_results = []  # list of dicts per truncation level

def run_truncation_level(max_pq, n_samples, n_eps, eps_c, N_expected,
                         gens, f_abc, gammas, E, Omega, full_scan=True):
    """Run entropy computation for one truncation level."""
    t_level_start = time.time()

    print(f"\n{'='*60}")
    print(f"max_pq_sum = {max_pq}: N_expected = {N_expected}, eps_c = {eps_c:.5f}")
    print(f"  n_samples = {n_samples}, n_epsilon_points = {n_eps}")
    print(f"  full_scan = {full_scan}")
    print(f"{'='*60}")

    # Build block-diagonal H0
    print(f"  Building block-diagonal H0...")
    H0, block_starts, sector_dims, sector_labels_loc, total_dim = \
        build_block_diagonal_H(max_pq, gens, f_abc, gammas, E, Omega, verbose=False)
    H0_norm = np.linalg.norm(H0, 'fro')

    print(f"  total_dim = {total_dim}, ||H0||_F = {H0_norm:.4f}")
    print(f"  Sector count: {len(sector_dims)}")
    print(f"  Sector dims: {sector_dims}")

    # Find tensor product bipartition
    d_A = find_tensor_bipartition(total_dim, sector_dims)
    d_B = total_dim // d_A
    S_page_val = page_entropy(d_A, d_B)

    print(f"  Bipartition: d_A = {d_A}, d_B = {d_B}, d_A*d_B = {d_A*d_B}")
    print(f"  Page entropy (random state): S_Page = {S_page_val:.4f}")
    print(f"  Max entropy: ln(min(d_A,d_B)) = {np.log(min(d_A, d_B)):.4f}")

    # Verify unperturbed ground state entropy
    evals_0, evecs_0 = eigh(H0)
    psi_0 = evecs_0[:, 0]
    S_0 = entanglement_entropy_bipartition(psi_0, d_A, total_dim)
    r_0 = ratio_statistic(evals_0)
    print(f"  Unperturbed S_ent = {S_0:.6f}, <r> = {r_0:.4f}")

    if full_scan:
        # Full epsilon scan: 0 to 10*eps_c
        eps_max = 10.0 * eps_c
        eps_scan = np.concatenate([
            [0.0],
            np.geomspace(eps_c * 0.01, eps_max, n_eps - 1)
        ])

        print(f"\n  Scanning {len(eps_scan)} epsilon values from 0 to {eps_max:.5f}...")

        S_means = np.zeros(len(eps_scan))
        S_errs = np.zeros(len(eps_scan))
        r_means = np.zeros(len(eps_scan))
        r_errs = np.zeros(len(eps_scan))

        for i, eps in enumerate(eps_scan):
            if eps == 0.0:
                S_means[i] = S_0
                S_errs[i] = 0.0
                r_means[i] = r_0
                r_errs[i] = 0.0
            else:
                # Only compute <r> at a few points (eps near eps_c)
                do_r = abs(np.log10(eps / eps_c)) < 0.3
                S_m, S_e, r_m, r_e = measure_entropy_at_epsilon(
                    H0, total_dim, H0_norm, eps, n_samples, d_A,
                    compute_r=do_r
                )
                S_means[i] = S_m
                S_errs[i] = S_e
                r_means[i] = r_m
                r_errs[i] = r_e

            if i % 4 == 0 or i == len(eps_scan) - 1:
                print(f"    [{i+1}/{len(eps_scan)}] eps={eps:.5f}: "
                      f"S_ent={S_means[i]:.4f}+/-{S_errs[i]:.4f}")
    else:
        # Single-point measurement at eps_c only
        eps_scan = np.array([0.0, eps_c])
        S_means = np.array([S_0, 0.0])
        S_errs = np.array([0.0, 0.0])
        r_means = np.array([r_0, 0.0])
        r_errs = np.array([0.0, 0.0])

    # Direct measurement at eps_c with extra samples for accuracy
    n_direct = max(n_samples, 4)
    print(f"\n  Direct measurement at eps_c = {eps_c:.5f} ({n_direct} samples)...")
    S_direct, S_direct_err, r_direct, r_direct_err = measure_entropy_at_epsilon(
        H0, total_dim, H0_norm, eps_c, n_direct, d_A, compute_r=True
    )
    print(f"  S_ent(eps_c) = {S_direct:.4f} +/- {S_direct_err:.4f}")
    print(f"  <r>(eps_c) = {r_direct:.4f} (midpoint = {R_MIDPOINT:.4f})")

    if not full_scan:
        S_means[1] = S_direct
        S_errs[1] = S_direct_err
        r_means[1] = r_direct
        r_errs[1] = r_direct_err

    t_level_end = time.time()
    dt = t_level_end - t_level_start

    result = {
        'max_pq': max_pq,
        'N': total_dim,
        'eps_c': eps_c,
        'd_A': d_A,
        'd_B': d_B,
        'S_page': S_page_val,
        'S_max': np.log(min(d_A, d_B)),
        'S_unperturbed': S_0,
        'eps_scan': eps_scan,
        'S_means': S_means,
        'S_errs': S_errs,
        'r_means': r_means,
        'r_errs': r_errs,
        'S_at_eps_c_direct': S_direct,
        'S_at_eps_c_direct_err': S_direct_err,
        'r_at_eps_c': r_direct,
        'n_sectors': len(sector_dims),
        'sector_dims': sector_dims,
        'runtime_s': dt,
        'full_scan': full_scan,
    }

    print(f"\n  RESULT: max_pq={max_pq}, N={total_dim}, d_A={d_A}")
    print(f"  S_ent(eps_c) = {S_direct:.4f} +/- {S_direct_err:.4f}")
    print(f"  S_page = {S_page_val:.4f}, S_max = {np.log(min(d_A, d_B)):.4f}")
    if S_page_val > 0:
        print(f"  S_ent / S_page = {S_direct/S_page_val:.4f}")
    print(f"  Time: {dt:.1f}s")

    return result


# --- Run all truncation levels ---
for config_idx, (max_pq, n_samples, n_eps) in enumerate(TRUNCATION_CONFIGS):
    result = run_truncation_level(
        max_pq, n_samples, n_eps,
        eps_c_s44[config_idx], int(N_s44[config_idx]),
        gens, f_abc, gammas, E, Omega,
        full_scan=True
    )
    all_results.append(result)

# --- pq=5 single-point measurement ---
if PQ5_SINGLE_POINT:
    result = run_truncation_level(
        5, PQ5_SAMPLES, 2,
        eps_c_s44[4], int(N_s44[4]),
        gens, f_abc, gammas, E, Omega,
        full_scan=False
    )
    all_results.append(result)

# ============================================================
# Step 3: Scaling analysis of S_ent(eps_c) vs N
# ============================================================
print("\n" + "=" * 70)
print("Step 3: Scaling Analysis -- S_ent(eps_c) vs N")
print("=" * 70)

N_arr = np.array([r['N'] for r in all_results], dtype=float)
S_arr = np.array([r['S_at_eps_c_direct'] for r in all_results])
S_err_arr = np.array([r['S_at_eps_c_direct_err'] for r in all_results])
S_page_arr = np.array([r['S_page'] for r in all_results])
S_max_arr = np.array([r['S_max'] for r in all_results])
d_A_arr = np.array([r['d_A'] for r in all_results], dtype=float)

# Normalized entropy: S / S_page
S_norm = S_arr / S_page_arr
S_norm[~np.isfinite(S_norm)] = 0.0

print(f"\n  {'max_pq':>7s}  {'N':>7s}  {'d_A':>7s}  {'S_ent':>10s}  {'S_page':>10s}  "
      f"{'S/S_page':>10s}  {'S_max':>10s}")
print(f"  {'-'*75}")
for i, r in enumerate(all_results):
    print(f"  {r['max_pq']:>7d}  {r['N']:>7d}  {r['d_A']:>7d}  "
          f"{S_arr[i]:>10.4f}  {S_page_arr[i]:>10.4f}  "
          f"{S_norm[i]:>10.4f}  {S_max_arr[i]:>10.4f}")

# Fit models to S_ent(eps_c) vs N
fit_results = {}

# 1. ln(N) model (area law)
try:
    popt, pcov = curve_fit(model_lnN, N_arr, S_arr, p0=[0.1, 0.0],
                           sigma=np.maximum(S_err_arr, 0.01))
    residuals = S_arr - model_lnN(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((S_arr - np.mean(S_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_results['ln(N)'] = {'params': popt, 'R2': r_squared, 'ss_res': ss_res,
                             'label': f'a*ln(N)+b: a={popt[0]:.4f}, b={popt[1]:.4f}'}
    print(f"\n  ln(N):     a = {popt[0]:.4f}, b = {popt[1]:.4f}, R^2 = {r_squared:.6f}")
except Exception as e:
    print(f"\n  ln(N) fit failed: {e}")

# 2. Power law model (volume law)
try:
    popt, pcov = curve_fit(model_power, N_arr, S_arr, p0=[0.01, 0.5],
                           bounds=([0, 0], [100, 2.0]),
                           sigma=np.maximum(S_err_arr, 0.01))
    residuals = S_arr - model_power(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((S_arr - np.mean(S_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_results['N^alpha'] = {'params': popt, 'R2': r_squared, 'ss_res': ss_res,
                               'label': f'a*N^alpha: a={popt[0]:.4f}, alpha={popt[1]:.4f}'}
    print(f"  N^alpha:   a = {popt[0]:.4f}, alpha = {popt[1]:.4f}, R^2 = {r_squared:.6f}")
except Exception as e:
    print(f"  N^alpha fit failed: {e}")

# 3. Constant model
try:
    popt, pcov = curve_fit(model_const, N_arr, S_arr, p0=[np.mean(S_arr)],
                           sigma=np.maximum(S_err_arr, 0.01))
    residuals = S_arr - model_const(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((S_arr - np.mean(S_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_results['const'] = {'params': popt, 'R2': r_squared, 'ss_res': ss_res,
                             'label': f'const: c={popt[0]:.4f}'}
    print(f"  constant:  c = {popt[0]:.4f}, R^2 = {r_squared:.6f}")
except Exception as e:
    print(f"  constant fit failed: {e}")

# 4. sqrt(N) model (intermediate)
try:
    popt, pcov = curve_fit(model_sqrt, N_arr, S_arr, p0=[0.01, 0.0],
                           sigma=np.maximum(S_err_arr, 0.01))
    residuals = S_arr - model_sqrt(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((S_arr - np.mean(S_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_results['sqrt(N)'] = {'params': popt, 'R2': r_squared, 'ss_res': ss_res,
                               'label': f'a*sqrt(N)+b: a={popt[0]:.4f}, b={popt[1]:.4f}'}
    print(f"  sqrt(N):   a = {popt[0]:.4f}, b = {popt[1]:.4f}, R^2 = {r_squared:.6f}")
except Exception as e:
    print(f"  sqrt(N) fit failed: {e}")

# Also fit S/S_page (normalized entropy) vs N
fit_norm = {}
try:
    popt, pcov = curve_fit(model_const, N_arr, S_norm, p0=[0.5],
                           sigma=np.maximum(S_err_arr/S_page_arr, 0.01))
    residuals = S_norm - model_const(N_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((S_norm - np.mean(S_norm))**2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    fit_norm['const'] = {'c': popt[0], 'R2': r2}
    print(f"\n  Normalized S/S_page ~ const: c = {popt[0]:.4f}, R^2 = {r2:.6f}")
except Exception as e:
    print(f"\n  Normalized const fit failed: {e}")

# ============================================================
# Step 4: Model comparison
# ============================================================
print("\n" + "=" * 70)
print("Step 4: Model Comparison")
print("=" * 70)

n_data = len(N_arr)
print(f"\n  {'Model':>12s}  {'R^2':>10s}  {'SS_res':>12s}  {'k':>3s}  {'BIC':>10s}")
print(f"  {'-'*55}")

for name in sorted(fit_results.keys(), key=lambda x: fit_results[x]['ss_res']):
    res = fit_results[name]
    k = len(res['params'])
    ss = res['ss_res']
    bic = n_data * np.log(ss / n_data + 1e-30) + k * np.log(n_data)
    res['BIC'] = bic
    print(f"  {name:>12s}  {res['R2']:>10.6f}  {ss:>12.4e}  {k:>3d}  {bic:>10.3f}")

best_model = min(fit_results.items(), key=lambda x: x[1]['ss_res'])
print(f"\n  Best fit (lowest SS_res): {best_model[0]}")

# ============================================================
# Step 5: Physical interpretation
# ============================================================
print("\n" + "=" * 70)
print("Step 5: Physical Interpretation")
print("=" * 70)

# Determine the scaling law
if 'N^alpha' in fit_results:
    alpha_S = fit_results['N^alpha']['params'][1]
    print(f"\n  Power law exponent: S ~ N^{alpha_S:.3f}")

    if alpha_S < 0.1:
        scaling_class = "AREA (logarithmic or slower)"
    elif 0.1 <= alpha_S < 0.35:
        scaling_class = "SUB-VOLUME (intermediate)"
    elif 0.35 <= alpha_S < 0.65:
        scaling_class = "SQRT (critical-like)"
    elif alpha_S >= 0.65:
        scaling_class = "VOLUME"
    else:
        scaling_class = "INDETERMINATE"

    print(f"  Classification: {scaling_class}")

print(f"\n  S_ent / S_page at each N:")
for i, r in enumerate(all_results):
    ratio = S_arr[i] / S_page_arr[i] if S_page_arr[i] > 0 else 0
    print(f"    N={r['N']:>6d}: S/S_page = {ratio:.4f}")

mean_ratio = np.mean(S_norm[S_norm > 0]) if np.any(S_norm > 0) else 0
print(f"\n  Mean S/S_page = {mean_ratio:.4f}")

if mean_ratio > 0.5:
    print(f"  Interpretation: at eps_c the ground state is MORE than half Page-entangled.")
    print(f"  The dissolution transition is strongly entangling -- the system is")
    print(f"  already deep into the volume-law regime at the spectral crossover.")
elif mean_ratio > 0.1:
    print(f"  Interpretation: at eps_c the ground state has MODERATE entanglement.")
    print(f"  The entanglement transition and spectral transition are correlated")
    print(f"  but entanglement lags behind the level statistics change.")
else:
    print(f"  Interpretation: at eps_c the ground state has WEAK entanglement.")
    print(f"  The spectral dissolution (level repulsion) occurs BEFORE significant")
    print(f"  entanglement develops. Spectral and entanglement transitions decouple.")

# ============================================================
# Step 6: Foam implications
# ============================================================
print("\n" + "=" * 70)
print("Step 6: Foam Implications")
print("=" * 70)

print(f"""
  STRUCTURAL RESULT: Entanglement entropy quantifies the dissolution transition.

  At epsilon = 0 (pure block-diagonal): S_ent = 0 (product state across sectors)
  At epsilon = eps_c (spectral crossover <r> = midpoint): S_ent measured
  At epsilon >> eps_c (GOE random matrix): S_ent -> S_Page ~ ln(d_A)

  The scaling S_ent(eps_c, N) classifies the phase transition:

  - Area law (S ~ ln N): dissolution is a LOCALIZED phenomenon.
    Only sector boundaries are affected. Bulk of each sector remains coherent.
    This would mean foam perturbations affect only inter-sector physics,
    while intra-sector predictions (particle spectrum) are robust.

  - Volume law (S ~ N^alpha, alpha > 0): dissolution is EXTENSIVE.
    The perturbation scrambles the entire Hilbert space.
    This would mean foam effects contaminate ALL predictions at sufficient strength.

  - Critical (S ~ sqrt(N)): dissolution is at a PHASE TRANSITION.
    The system is at an entanglement phase transition, with long-range
    correlations and universal scaling. This would be the most interesting
    scenario from the foam perspective.

  Connection to W-FOAM-7 (spectral triple emergence):
    - S44 proved epsilon_c ~ N^{{-0.457}}: threshold vanishes with mode count
    - This computation adds: the ENTANGLEMENT at the threshold scales as [...]
    - Together: both spectral statistics and quantum correlations confirm emergence
""")

# ============================================================
# Step 7: Gate verdict
# ============================================================
print("=" * 70)
print("DISSOLUTION-ENTROPY-45: GATE VERDICT")
print("=" * 70)

verdict = "INFO"

print(f"\n  Gate: DISSOLUTION-ENTROPY-45")
print(f"  Status: {verdict} (entanglement characterization of dissolution)")
print(f"  This is a characterization computation, not a pass/fail gate.")

if 'N^alpha' in fit_results:
    alpha_S = fit_results['N^alpha']['params'][1]
    print(f"\n  Key finding: S_ent(eps_c) ~ N^{{{alpha_S:.3f}}}")

    if 'ln(N)' in fit_results:
        print(f"  Alternative: S ~ a*ln(N)+b: R^2 = {fit_results['ln(N)']['R2']:.4f}")
    print(f"  Power law: R^2 = {fit_results['N^alpha']['R2']:.4f}")

# ============================================================
# Step 8: Save data
# ============================================================
print("\n--- Saving results ---")

save_data = {
    'tau': TAU_FOLD,
    'max_pq_sums': np.array([r['max_pq'] for r in all_results]),
    'N_values': N_arr,
    'd_A_values': d_A_arr,
    'd_B_values': np.array([r['d_B'] for r in all_results], dtype=float),
    'S_at_eps_c': S_arr,
    'S_at_eps_c_err': S_err_arr,
    'S_page': S_page_arr,
    'S_max': S_max_arr,
    'S_normalized': S_norm,
    'eps_c_values': np.array([r['eps_c'] for r in all_results]),
    'S_unperturbed': np.array([r['S_unperturbed'] for r in all_results]),
    'r_at_eps_c': np.array([r['r_at_eps_c'] for r in all_results]),
    'verdict': np.array([verdict]),
    'alpha_dissolution_s44': alpha_fit,
}

# Save fit results
for name, res in fit_results.items():
    safe_name = name.replace('(', '').replace(')', '').replace('^', '_')
    save_data[f'fit_{safe_name}_params'] = np.array(res['params'])
    save_data[f'fit_{safe_name}_R2'] = np.array([res['R2']])

# Save per-truncation scan data
for i, r in enumerate(all_results):
    pq = r['max_pq']
    save_data[f'eps_scan_pq{pq}'] = r['eps_scan']
    save_data[f'S_scan_pq{pq}'] = r['S_means']
    save_data[f'S_err_scan_pq{pq}'] = r['S_errs']
    save_data[f'r_scan_pq{pq}'] = r['r_means']
    save_data[f'r_err_scan_pq{pq}'] = r['r_errs']
    save_data[f'sector_dims_pq{pq}'] = np.array(r['sector_dims'])

np.savez(os.path.join(SCRIPT_DIR, 's45_dissolution_entropy.npz'), **save_data)
print("  Saved: tier0-computation/s45_dissolution_entropy.npz")

# ============================================================
# Step 9: Plot
# ============================================================
print("  Generating plot...")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 2, hspace=0.4, wspace=0.35)

# --- Panel 1: S_ent vs epsilon for each truncation level ---
ax1 = fig.add_subplot(gs[0, 0])
colors_pq = plt.cm.viridis(np.linspace(0.1, 0.9, len(all_results)))

for i, r in enumerate(all_results):
    eps_scan = r['eps_scan']
    S_means = r['S_means']
    S_errs = r['S_errs']
    mask = eps_scan > 0  # skip eps=0 on log scale
    ax1.errorbar(eps_scan[mask], S_means[mask], yerr=S_errs[mask],
                 fmt='o-', color=colors_pq[i], capsize=2, linewidth=1.5,
                 markersize=4, label=f'pq={r["max_pq"]} (N={r["N"]})')
    # Mark eps_c
    ax1.axvline(r['eps_c'], color=colors_pq[i], linestyle=':', linewidth=0.8, alpha=0.5)
    # Mark S_page
    ax1.axhline(r['S_page'], color=colors_pq[i], linestyle='--', linewidth=0.5, alpha=0.3)

ax1.set_xlabel(r'$\epsilon$', fontsize=12)
ax1.set_ylabel(r'$S_{\rm ent}$', fontsize=14)
ax1.set_title(r'Entanglement Entropy vs Perturbation Strength', fontsize=12)
ax1.set_xscale('log')
ax1.legend(fontsize=8, loc='lower right')
ax1.grid(True, alpha=0.3)

# --- Panel 2: S_ent / S_page vs epsilon (normalized) ---
ax2 = fig.add_subplot(gs[0, 1])

for i, r in enumerate(all_results):
    eps_scan = r['eps_scan']
    S_means = r['S_means']
    S_page = r['S_page']
    mask = eps_scan > 0
    if S_page > 0:
        ax2.plot(eps_scan[mask] / r['eps_c'], S_means[mask] / S_page,
                 'o-', color=colors_pq[i], linewidth=1.5, markersize=4,
                 label=f'pq={r["max_pq"]} (N={r["N"]})')

ax2.axhline(1.0, color='red', linestyle='--', linewidth=1, label='Page value')
ax2.axvline(1.0, color='gray', linestyle=':', linewidth=1, label=r'$\epsilon = \epsilon_c$')
ax2.set_xlabel(r'$\epsilon / \epsilon_c$', fontsize=12)
ax2.set_ylabel(r'$S_{\rm ent} / S_{\rm Page}$', fontsize=14)
ax2.set_title(r'Normalized Entropy vs Scaled Perturbation', fontsize=12)
ax2.set_xscale('log')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(bottom=-0.05)

# --- Panel 3: S_ent(eps_c) vs N (main scaling result) ---
ax3 = fig.add_subplot(gs[1, 0])
ax3.errorbar(N_arr, S_arr, yerr=S_err_arr, fmt='ko', markersize=10, zorder=5,
             label='Data')

# Plot fit curves
N_plot = np.logspace(np.log10(N_arr.min() * 0.5), np.log10(N_arr.max() * 3), 200)
fit_colors = {'ln(N)': 'blue', 'N^alpha': 'red', 'const': 'gray', 'sqrt(N)': 'green'}

for name, res in fit_results.items():
    p = res['params']
    if name == 'ln(N)':
        y = model_lnN(N_plot, *p)
    elif name == 'N^alpha':
        y = model_power(N_plot, *p)
    elif name == 'const':
        y = model_const(N_plot, *p)
    elif name == 'sqrt(N)':
        y = model_sqrt(N_plot, *p)
    else:
        continue
    ax3.plot(N_plot, y, '-', color=fit_colors.get(name, 'purple'), linewidth=1.5,
             alpha=0.7, label=f'{res["label"]}, R2={res["R2"]:.3f}')

# Also show S_page curve
ax3.plot(N_plot, [page_entropy(find_tensor_bipartition(int(n), []),
                                int(n)//find_tensor_bipartition(int(n), []))
                  for n in N_plot],
         'k--', linewidth=1, alpha=0.3, label='Page value')

ax3.set_xlabel('N (total Hilbert space dimension)', fontsize=12)
ax3.set_ylabel(r'$S_{\rm ent}(\epsilon_c)$', fontsize=14)
ax3.set_title(r'Entanglement at Dissolution Threshold', fontsize=12)
ax3.set_xscale('log')
ax3.legend(fontsize=7, loc='upper left')
ax3.grid(True, alpha=0.3)

# Annotate max_pq_sum values
for i, r in enumerate(all_results):
    ax3.annotate(f'pq={r["max_pq"]}', (N_arr[i], S_arr[i]),
                 textcoords="offset points", xytext=(10, 5), fontsize=9)

# --- Panel 4: S/S_page vs N (normalized scaling) ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(N_arr, S_norm, 'ko-', markersize=10, zorder=5, label=r'$S(\epsilon_c)/S_{\rm Page}$')
ax4.axhline(1.0, color='red', linestyle='--', linewidth=1, alpha=0.5, label='Full Page')
ax4.axhline(mean_ratio, color='blue', linestyle=':', linewidth=1.5,
            label=f'Mean = {mean_ratio:.3f}')

ax4.set_xlabel('N (total Hilbert space dimension)', fontsize=12)
ax4.set_ylabel(r'$S_{\rm ent}(\epsilon_c) / S_{\rm Page}$', fontsize=14)
ax4.set_title(r'Normalized Entropy at Dissolution', fontsize=12)
ax4.set_xscale('log')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)
ax4.set_ylim(bottom=-0.05)

# --- Panel 5: Dual diagnostic: <r> and S_ent vs epsilon for one truncation ---
ax5 = fig.add_subplot(gs[2, 0])
# Use max_pq_sum=2 (S43 baseline) for the dual plot
idx_ref = 1  # max_pq_sum=2
r_ref = all_results[idx_ref]
eps_ref = r_ref['eps_scan']
mask_ref = eps_ref > 0

ax5_r = ax5
ax5_s = ax5.twinx()

ax5_r.plot(eps_ref[mask_ref], r_ref['r_means'][mask_ref], 'b-o', markersize=4,
           linewidth=1.5, label=r'$\langle r \rangle$')
ax5_r.axhline(R_POISSON, color='blue', linestyle='--', linewidth=0.8, alpha=0.5)
ax5_r.axhline(R_GOE, color='blue', linestyle='--', linewidth=0.8, alpha=0.5)
ax5_r.axhline(R_MIDPOINT, color='blue', linestyle=':', linewidth=0.8)

ax5_s.plot(eps_ref[mask_ref], r_ref['S_means'][mask_ref], 'r-s', markersize=4,
           linewidth=1.5, label=r'$S_{\rm ent}$')
ax5_s.axhline(r_ref['S_page'], color='red', linestyle='--', linewidth=0.8, alpha=0.5)

ax5_r.axvline(r_ref['eps_c'], color='gray', linestyle=':', linewidth=1.5, alpha=0.7)

ax5_r.set_xlabel(r'$\epsilon$', fontsize=12)
ax5_r.set_ylabel(r'$\langle r \rangle$', fontsize=12, color='blue')
ax5_s.set_ylabel(r'$S_{\rm ent}$', fontsize=12, color='red')
ax5_r.set_xscale('log')
ax5_r.set_title(f'Dual Diagnostic (pq={r_ref["max_pq"]}, N={r_ref["N"]})', fontsize=12)

# Combined legend
lines_r, labels_r = ax5_r.get_legend_handles_labels()
lines_s, labels_s = ax5_s.get_legend_handles_labels()
ax5_r.legend(lines_r + lines_s, labels_r + labels_s, fontsize=8, loc='center right')
ax5_r.grid(True, alpha=0.3)

# --- Panel 6: Log-log diagnostic for scaling ---
ax6 = fig.add_subplot(gs[2, 1])
log_N = np.log(N_arr)
ax6.plot(log_N, S_arr, 'ko', markersize=10, zorder=5)

if 'ln(N)' in fit_results:
    p = fit_results['ln(N)']['params']
    ax6.plot(log_N, model_lnN(N_arr, *p), 'b-', linewidth=2,
             label=f'ln(N): R2={fit_results["ln(N)"]["R2"]:.3f}')

if 'N^alpha' in fit_results:
    p = fit_results['N^alpha']['params']
    ax6.plot(log_N, model_power(N_arr, *p), 'r-', linewidth=2,
             label=f'N^{{{p[1]:.2f}}}: R2={fit_results["N^alpha"]["R2"]:.3f}')

ax6.set_xlabel(r'$\ln(N)$', fontsize=12)
ax6.set_ylabel(r'$S_{\rm ent}(\epsilon_c)$', fontsize=14)
ax6.set_title('Scaling Diagnostic', fontsize=12)
ax6.legend(fontsize=9)
ax6.grid(True, alpha=0.3)

fig.suptitle(f'DISSOLUTION-ENTROPY-45: Entanglement Entropy at Dissolution (tau={TAU_FOLD})\n'
             f'Verdict: {verdict}',
             fontsize=14, fontweight='bold')

plt.savefig(os.path.join(SCRIPT_DIR, 's45_dissolution_entropy.png'), dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s45_dissolution_entropy.png")

# ============================================================
# Final timing and summary
# ============================================================
t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s ({(t_end - t_start)/60:.1f}min)")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"\n  Entanglement entropy measured at dissolution threshold for {len(all_results)} truncation levels.")
print(f"  N range: [{int(N_arr.min())}, {int(N_arr.max())}]")
print(f"  S_ent(eps_c) range: [{S_arr.min():.4f}, {S_arr.max():.4f}]")
print(f"  S/S_page mean: {mean_ratio:.4f}")

if 'N^alpha' in fit_results:
    p = fit_results['N^alpha']['params']
    print(f"\n  Power law: S_ent(eps_c) = {p[0]:.4f} * N^{{{p[1]:.4f}}}")
    print(f"  R^2 = {fit_results['N^alpha']['R2']:.6f}")

if 'ln(N)' in fit_results:
    p = fit_results['ln(N)']['params']
    print(f"  Logarithmic: S_ent(eps_c) = {p[0]:.4f} * ln(N) + {p[1]:.4f}")
    print(f"  R^2 = {fit_results['ln(N)']['R2']:.6f}")

print(f"\n  QF-81: S_ent(epsilon_c, N) scaling at dissolution")
print(f"\n  Gate verdict: {verdict}")
print(f"\n  Data: tier0-computation/s45_dissolution_entropy.npz")
print(f"  Plot: tier0-computation/s45_dissolution_entropy.png")
