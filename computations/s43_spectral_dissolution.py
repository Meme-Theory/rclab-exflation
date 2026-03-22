#!/usr/bin/env python3
"""
s43_spectral_dissolution.py -- DISSOLUTION-43: Spectral Triple Dissolution Threshold

Determine at what metric fluctuation amplitude the block-diagonal theorem
for D_K on Jensen-deformed SU(3) dissolves (Poisson -> GOE level statistics).

=== PHYSICS ===

The block-diagonal theorem (Session 22b) states: D_K is exactly block-diagonal
in the Peter-Weyl decomposition for ANY left-invariant metric on SU(3). This is
a structural theorem: left-invariance means the metric coefficients g_{ab} are
constants on the group manifold, so the Dirac operator D = sum_a e_a * gamma_a
commutes with the right-regular representation.

Planck-scale foam BREAKS left-invariance. The metric becomes position-dependent:
  g_{ab}(x) = g^LI_{ab} + epsilon * delta_g_{ab}(x)

where delta_g_{ab}(x) is a random symmetric tensor field on SU(3), expanded in
Peter-Weyl harmonics. The foam perturbation has representation content -- it
transforms under specific (p,q) irreps of SU(3) -- and generates inter-sector
couplings governed by Clebsch-Gordan selection rules.

At the framework's physical parameters:
  delta_g/g ~ (M_KK/M_P)^{1/2} ~ 10^{-0.75} ~ 18%

This is in the strong-perturbation regime. The question: at what epsilon does
the level statistics transition from Poisson (integrable, block-diagonal) to
GOE (chaotic, sectors mixed)?

=== METHOD ===

1. Build D_K in each Peter-Weyl sector (p,q) with p+q <= 2 at tau = 0.19 (fold)
2. Construct the combined matrix as block-diagonal (unperturbed)
3. Add random inter-sector coupling matrices with amplitude epsilon, drawn from
   GUE to model generic metric fluctuations (symmetric tensor field has no special
   structure beyond Hermiticity of the resulting operator)
4. For each epsilon in {0.001, 0.01, 0.05, 0.10, 0.20, 0.50}:
   a. Generate N_samples random perturbation matrices
   b. Diagonalize total D_K + epsilon * V_inter
   c. Compute level spacing ratio <r> (Oganesyan-Huse diagnostic)
   d. Average over samples
5. Identify epsilon_crossover where <r> transitions from Poisson to GOE

The perturbation V_inter is structured:
- WITHIN each (p,q) block: random Hermitian matrix (position-dependent metric
  changes the ON frame structure constants, modifying the block's matrix elements)
- BETWEEN (p,q) and (p',q') blocks: random matrix whose Frobenius norm is
  weighted by the Clebsch-Gordan overlap, which we approximate as uniform for
  adjacent sectors and zero for distant ones

For the inter-sector coupling, we use the selection rule: a metric perturbation
in the adjoint (1,1) representation can only couple sectors (p,q) to (p',q') if
(p',q') appears in (p,q) tensor (1,1). More general perturbations (higher harmonics)
couple further sectors.

Since we're asking for the dissolution THRESHOLD (not the exact crossover shape),
we use the simplest physical model: random couplings between ALL included sectors,
weighted by 1/sqrt(dim1 * dim2) for normalization.

=== GATE ===
DISSOLUTION-43 (INFO): Report epsilon_crossover and physical interpretation.
No pre-registered pass/fail -- this is a measurement.

Author: quantum-foam-theorist, Session 43
"""

import numpy as np
from numpy.linalg import eigvalsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
import sys
import time

t_start = time.time()

# Add tier0 path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

# Import from tier1_dirac_spectrum
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

# ============================================================
# CONSTANTS
# ============================================================
R_POISSON = 2 * np.log(2) - 1   # 0.38629
R_GOE = 0.5307                    # Atas et al. 2013
R_GUE = 0.5996
DEGENERACY_TOL = 1e-10
TAU_FOLD = 0.19                   # Jensen fold
N_SAMPLES = 20                    # Random perturbation realizations
EPSILON_VALUES = [0.001, 0.005, 0.01, 0.02, 0.03, 0.05, 0.10, 0.20, 0.50]
MAX_PQ_SUM = 2                    # Include (0,0), (1,0), (0,1), (1,1), (2,0), (0,2)

np.random.seed(42)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def ratio_statistic(evals):
    """
    Compute Oganesyan-Huse ratio statistic from eigenvalues.
    r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1})
    where s_n = E_{n+1} - E_n are nearest-neighbor spacings.
    No unfolding needed -- scale-free by construction.
    """
    evals = np.sort(np.real(evals))
    # Remove degeneracies
    unique = [evals[0]]
    for e in evals[1:]:
        if abs(e - unique[-1]) > DEGENERACY_TOL:
            unique.append(e)
    evals = np.array(unique)

    if len(evals) < 4:
        return np.nan, np.nan, 0

    spacings = np.diff(evals)
    spacings = spacings[spacings > DEGENERACY_TOL]

    if len(spacings) < 3:
        return np.nan, np.nan, 0

    ratios = []
    for i in range(len(spacings) - 1):
        s1, s2 = spacings[i], spacings[i+1]
        if max(s1, s2) > 0:
            ratios.append(min(s1, s2) / max(s1, s2))

    ratios = np.array(ratios)
    if len(ratios) == 0:
        return np.nan, np.nan, 0

    return np.mean(ratios), np.std(ratios) / np.sqrt(len(ratios)), len(ratios)


def spacing_distribution(evals, n_bins=30):
    """
    Compute normalized nearest-neighbor spacing distribution P(s).
    Uses polynomial unfolding with outlier rejection.

    The block-diagonal spectrum has clusters of eigenvalues separated
    by sector gaps. Polynomial unfolding handles this better than
    local averaging for the Brody fit.
    """
    evals = np.sort(np.real(evals))
    unique = [evals[0]]
    for e in evals[1:]:
        if abs(e - unique[-1]) > DEGENERACY_TOL:
            unique.append(e)
    evals = np.array(unique)

    if len(evals) < 20:
        return None, None, None

    # Polynomial unfolding: fit N(E) with polynomial
    N = len(evals)
    staircase = np.arange(1, N + 1)
    degree = min(7, N // 10)
    coeffs = np.polyfit(evals, staircase, degree)
    N_smooth = np.polyval(coeffs, evals)
    spacings = np.diff(N_smooth)

    # Remove negative spacings (from poor fit at edges)
    spacings = spacings[spacings > 0]

    if len(spacings) < 20:
        return None, None, None

    # Outlier rejection: remove spacings > 5 * median
    # This handles residual cluster-gap artifacts
    med = np.median(spacings)
    spacings = spacings[spacings < 5 * med]

    if len(spacings) < 20:
        return None, None, None

    # Normalize mean to 1
    spacings = spacings / np.mean(spacings)

    hist, bin_edges = np.histogram(spacings, bins=n_bins, range=(0, 4), density=True)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    return bin_centers, hist, spacings


def wigner_goe(s):
    """Wigner surmise for GOE: P(s) = (pi/2) s exp(-pi s^2/4)."""
    return (np.pi / 2) * s * np.exp(-np.pi * s**2 / 4)


def poisson_ps(s):
    """Poisson spacing distribution: P(s) = exp(-s)."""
    return np.exp(-s)


def brody_fit(unfolded_spacings):
    """
    Fit Brody parameter beta: P(s) = (1+beta)*a*s^beta * exp(-a*s^{1+beta})
    where a = Gamma((2+beta)/(1+beta))^{1+beta}.
    beta=0 is Poisson, beta=1 is GOE.

    Uses moment method: <s^{1+beta}> = 1/a = 1/Gamma((2+beta)/(1+beta))^{1+beta}.
    This is more robust than MLE for small samples.

    Also uses a grid search + refinement approach.
    """
    from scipy.optimize import minimize_scalar
    from scipy.special import gamma as gamma_func

    s = unfolded_spacings
    s = s[s > 1e-12]  # remove zeros
    N = len(s)
    if N < 10:
        return np.nan

    # Method 1: MLE with grid initialization
    def neg_log_likelihood(beta):
        if beta < -0.01 or beta > 2.0:
            return 1e10
        bp1 = 1.0 + beta
        try:
            a = gamma_func((2.0 + beta) / bp1) ** bp1
            if a <= 0 or not np.isfinite(a):
                return 1e10
            log_P = np.log(bp1) + np.log(a) + beta * np.log(s) - a * s**bp1
            if not np.all(np.isfinite(log_P)):
                return 1e10
            return -np.sum(log_P)
        except (ValueError, OverflowError):
            return 1e10

    # Grid search for initialization
    betas_grid = np.linspace(0.01, 1.5, 50)
    nlls = [neg_log_likelihood(b) for b in betas_grid]
    best_grid_idx = np.argmin(nlls)
    best_grid_beta = betas_grid[best_grid_idx]

    # Refine
    lo = max(0.0, best_grid_beta - 0.05)
    hi = min(1.5, best_grid_beta + 0.05)
    result = minimize_scalar(neg_log_likelihood, bounds=(lo, hi), method='bounded')

    return result.x


# ============================================================
# MAIN COMPUTATION
# ============================================================

print("=" * 70)
print("DISSOLUTION-43: Spectral Triple Dissolution Threshold")
print("=" * 70)
print(f"\nTau = {TAU_FOLD:.3f} (fold), max_pq_sum = {MAX_PQ_SUM}")
print(f"Epsilon values: {EPSILON_VALUES}")
print(f"N_samples = {N_SAMPLES}")

# ============================================================
# Step 1: Build infrastructure
# ============================================================
print("\n--- Step 1: Build SU(3) Lie algebra infrastructure ---")

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
# Step 2: Build D_K in each Peter-Weyl sector
# ============================================================
print("\n--- Step 2: Build Dirac blocks per Peter-Weyl sector ---")

sectors = []
sector_dims = []
sector_D_matrices = []
sector_labels = []

for p in range(MAX_PQ_SUM + 1):
    for q in range(MAX_PQ_SUM + 1 - p):
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        label = f"({p},{q})"

        try:
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq

            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

            # The Dirac operator is anti-Hermitian in math convention
            # Work with H = i*D (Hermitian) for eigenvalue analysis
            H_pi = 1j * D_pi

            # Verify Hermiticity
            herm_err = np.max(np.abs(H_pi - H_pi.conj().T))

            block_dim = dim_pq * 16
            print(f"  {label}: dim(rep) = {dim_pq}, D size = {block_dim}x{block_dim}, "
                  f"Herm err = {herm_err:.2e}")

            sectors.append((p, q, dim_pq))
            sector_dims.append(block_dim)
            sector_D_matrices.append(H_pi)
            sector_labels.append(label)

        except (NotImplementedError, RuntimeError) as e:
            print(f"  {label}: SKIPPED ({e})")

n_sectors = len(sectors)
total_dim = sum(sector_dims)
print(f"\n  Total sectors: {n_sectors}, total Hilbert space dim: {total_dim}")

# ============================================================
# Step 3: Assemble block-diagonal matrix (unperturbed)
# ============================================================
print("\n--- Step 3: Assemble block-diagonal H_0 ---")

H0 = np.zeros((total_dim, total_dim), dtype=complex)
block_starts = []
offset = 0
for i, H_pi in enumerate(sector_D_matrices):
    d = sector_dims[i]
    block_starts.append(offset)
    H0[offset:offset+d, offset:offset+d] = H_pi
    offset += d

# Verify block-diagonal structure
off_diag_norm = 0.0
for i in range(n_sectors):
    for j in range(n_sectors):
        if i != j:
            si, di = block_starts[i], sector_dims[i]
            sj, dj = block_starts[j], sector_dims[j]
            off_diag_norm += np.linalg.norm(H0[si:si+di, sj:sj+dj])
print(f"  Off-diagonal norm (should be 0): {off_diag_norm:.2e}")

# Compute unperturbed spectrum for baseline
evals_0 = eigvalsh(H0)
r_0, r_0_err, n_ratios_0 = ratio_statistic(evals_0)
print(f"  Unperturbed <r> = {r_0:.4f} +/- {r_0_err:.4f} (N_ratios = {n_ratios_0})")
print(f"  Expected Poisson: {R_POISSON:.4f}, GOE: {R_GOE:.4f}")

# ============================================================
# Step 4: Generate non-left-invariant perturbations
# ============================================================
print("\n--- Step 4: Perturbation scan over epsilon ---")
print(f"\nPhysical motivation:")
print(f"  Foam metric fluctuation: delta_g/g ~ (M_KK/M_P)^{{1/2}}")
print(f"  For M_KK ~ 10^{{16.9}} GeV, M_P ~ 10^{{18.4}} GeV:")
print(f"  delta_g/g ~ 10^{{-0.75}} ~ 0.18")
print(f"  This epsilon is the fractional perturbation of the Dirac operator.")
print()

# The perturbation model:
# A non-left-invariant metric fluctuation delta_g_{ab}(x) has representation
# content under the right-regular representation. When expanded in Peter-Weyl
# modes, it generates:
#   1. INTRA-sector modifications (diagonal blocks change)
#   2. INTER-sector couplings (off-diagonal blocks appear)
#
# The strength scales as epsilon * ||D_K|| to set the perturbation scale
# relative to the existing spectrum.
#
# We normalize the perturbation so that epsilon = ||V||/||H_0|| in Frobenius norm.

H0_norm = np.linalg.norm(H0, 'fro')
print(f"  ||H_0||_F = {H0_norm:.4f}")

# Scale factor: we want ||V||_F ~ epsilon * ||H_0||_F
# A random Hermitian matrix of size NxN has ||M||_F ~ sqrt(N) * sigma
# where M_{ij} ~ N(0, sigma^2)
# So sigma = epsilon * ||H_0||_F / sqrt(N^2) = epsilon * ||H_0||_F / N

results = {}
results['epsilon'] = EPSILON_VALUES
results['r_mean'] = []
results['r_std'] = []
results['r_samples'] = []
results['brody_mean'] = []
results['brody_std'] = []
results['brody_samples'] = []
results['spacing_distributions'] = {}

# Also compute per-sector <r> to see intra-sector vs inter-sector dissolution
results['r_per_sector'] = {label: {'mean': [], 'std': []} for label in sector_labels}

for eps_idx, epsilon in enumerate(EPSILON_VALUES):
    print(f"\n  epsilon = {epsilon:.4f} ...")

    # Target perturbation Frobenius norm
    target_norm = epsilon * H0_norm
    # For a random Hermitian NxN, entries drawn from N(0, sigma^2),
    # ||M||_F^2 = sum |M_ij|^2 ~ N^2 * sigma^2
    # So sigma = target_norm / N
    sigma = target_norm / total_dim

    sample_r_values = []
    sample_brody_values = []
    sample_sector_r = {label: [] for label in sector_labels}
    all_spacings_this_eps = []

    for sample in range(N_SAMPLES):
        # Generate random Hermitian perturbation
        # This is a full-matrix perturbation that couples ALL sectors
        # (the generic foam perturbation has no selection rules that
        # protect the block structure)
        V_real = np.random.randn(total_dim, total_dim) * sigma
        V_imag = np.random.randn(total_dim, total_dim) * sigma
        V = (V_real + 1j * V_imag)
        V = (V + V.conj().T) / 2.0  # Hermitianize

        # Perturbed Hamiltonian
        H_pert = H0 + V

        # Verify Hermiticity
        herm_check = np.max(np.abs(H_pert - H_pert.conj().T))
        if herm_check > 1e-12:
            print(f"    WARNING: Hermiticity violation {herm_check:.2e}")

        # Diagonalize
        evals_pert = eigvalsh(H_pert)

        # Full-spectrum <r>
        r_val, r_err, n_r = ratio_statistic(evals_pert)
        sample_r_values.append(r_val)

        # Spacing distribution for Brody fit
        _, _, unfolded = spacing_distribution(evals_pert)
        if unfolded is not None and len(unfolded) > 20:
            beta = brody_fit(unfolded)
            sample_brody_values.append(beta)
            all_spacings_this_eps.extend(unfolded.tolist())

        # Per-sector <r>: project eigenvalues back to sectors using
        # the fact that at small epsilon, eigenvalues roughly stay
        # sorted within their original blocks
        # At large epsilon this is meaningless, but at small epsilon
        # it tracks when intra-sector statistics change
        for sec_idx, label in enumerate(sector_labels):
            d = sector_dims[sec_idx]
            start = block_starts[sec_idx]
            # Extract the block of the perturbed H
            H_block = H_pert[start:start+d, start:start+d]
            block_evals = eigvalsh(H_block)
            r_block, _, _ = ratio_statistic(block_evals)
            sample_sector_r[label].append(r_block)

    # Aggregate results
    r_arr = np.array(sample_r_values)
    r_arr = r_arr[~np.isnan(r_arr)]
    results['r_mean'].append(np.mean(r_arr))
    results['r_std'].append(np.std(r_arr) / np.sqrt(len(r_arr)))
    results['r_samples'].append(r_arr)

    if len(sample_brody_values) > 0:
        b_arr = np.array(sample_brody_values)
        b_arr = b_arr[~np.isnan(b_arr)]
        results['brody_mean'].append(np.mean(b_arr))
        results['brody_std'].append(np.std(b_arr) / np.sqrt(len(b_arr)))
        results['brody_samples'].append(b_arr)
    else:
        results['brody_mean'].append(np.nan)
        results['brody_std'].append(np.nan)
        results['brody_samples'].append(np.array([]))

    # Store aggregated spacing distribution
    if len(all_spacings_this_eps) > 0:
        results['spacing_distributions'][epsilon] = np.array(all_spacings_this_eps)

    # Per-sector
    for label in sector_labels:
        arr = np.array(sample_sector_r[label])
        arr = arr[~np.isnan(arr)]
        if len(arr) > 0:
            results['r_per_sector'][label]['mean'].append(np.mean(arr))
            results['r_per_sector'][label]['std'].append(np.std(arr) / np.sqrt(len(arr)))
        else:
            results['r_per_sector'][label]['mean'].append(np.nan)
            results['r_per_sector'][label]['std'].append(np.nan)

    print(f"    <r> = {results['r_mean'][-1]:.4f} +/- {results['r_std'][-1]:.4f}")
    if not np.isnan(results['brody_mean'][-1]):
        print(f"    Brody beta = {results['brody_mean'][-1]:.3f} +/- {results['brody_std'][-1]:.3f}")

# ============================================================
# Step 5: Identify crossover
# ============================================================
print("\n" + "=" * 70)
print("DISSOLUTION-43: Results Summary")
print("=" * 70)

r_midpoint = (R_POISSON + R_GOE) / 2.0  # 0.459
print(f"\nPoisson <r> = {R_POISSON:.4f}, GOE <r> = {R_GOE:.4f}")
print(f"Midpoint criterion: <r> = {r_midpoint:.4f}")

print(f"\n{'epsilon':>10s}  {'<r>':>8s}  {'err':>7s}  {'Brody':>7s}  {'err':>7s}  {'Class':>10s}")
print("-" * 60)

epsilon_crossover = None
for i, eps in enumerate(EPSILON_VALUES):
    r_val = results['r_mean'][i]
    r_err = results['r_std'][i]
    b_val = results['brody_mean'][i]
    b_err = results['brody_std'][i]

    if r_val > R_GOE - 0.01:
        cls = "GOE"
    elif r_val > r_midpoint:
        cls = "TRANS->GOE"
    elif r_val > R_POISSON + 0.01:
        cls = "TRANS"
    else:
        cls = "POISSON"

    print(f"{eps:10.4f}  {r_val:8.4f}  {r_err:7.4f}  {b_val:7.3f}  {b_err:7.3f}  {cls:>10s}")

    # Find first epsilon where <r> exceeds midpoint
    if epsilon_crossover is None and r_val > r_midpoint:
        epsilon_crossover = eps

print()
if epsilon_crossover is not None:
    print(f"  CROSSOVER: epsilon_crossover ~ {epsilon_crossover:.4f}")
    print(f"  (First epsilon where <r> exceeds {r_midpoint:.4f})")
else:
    print(f"  NO CROSSOVER DETECTED in scanned range.")
    print(f"  Maximum <r> = {max(results['r_mean']):.4f} at epsilon = "
          f"{EPSILON_VALUES[np.argmax(results['r_mean'])]:.4f}")

# Interpolate for more precise crossover estimate
r_arr = np.array(results['r_mean'])
eps_arr = np.array(EPSILON_VALUES)
# Find where <r> crosses the midpoint by linear interpolation
for i in range(len(r_arr) - 1):
    if r_arr[i] < r_midpoint <= r_arr[i+1]:
        # Linear interpolation
        frac = (r_midpoint - r_arr[i]) / (r_arr[i+1] - r_arr[i])
        eps_interp = eps_arr[i] + frac * (eps_arr[i+1] - eps_arr[i])
        print(f"  Interpolated crossover: epsilon ~ {eps_interp:.4f}")
        epsilon_crossover_interp = eps_interp
        break
else:
    epsilon_crossover_interp = None

# Per-sector results
print(f"\n--- Per-sector <r> at each epsilon ---")
print(f"{'Sector':>8s}", end="")
for eps in EPSILON_VALUES:
    print(f"  {eps:>7.3f}", end="")
print()
for label in sector_labels:
    print(f"{label:>8s}", end="")
    for i in range(len(EPSILON_VALUES)):
        val = results['r_per_sector'][label]['mean'][i]
        print(f"  {val:>7.4f}", end="")
    print()

# ============================================================
# Step 6: Physical interpretation
# ============================================================
print("\n" + "=" * 70)
print("Physical Interpretation")
print("=" * 70)

print(f"""
1. BLOCK-DIAGONAL PROTECTION:
   The Peter-Weyl block-diagonal structure is an EXACT theorem for
   left-invariant metrics. Non-left-invariant perturbations break it
   by introducing inter-sector couplings proportional to epsilon.

2. CROSSOVER PHYSICS:
   At small epsilon, inter-sector matrix elements are O(epsilon) while
   intra-sector level spacings are O(1/dim). Crossover occurs when
   V_inter ~ Delta_intra, i.e., epsilon * ||H_0|| / N ~ ||H_0|| / N,
   which gives epsilon_crossover ~ O(1/sqrt(N)) for the combined space.

3. FOAM INTERPRETATION:
   Physical foam has delta_g/g ~ (M_KK/M_P)^{{1/2}} ~ 0.18.
""")

if epsilon_crossover is not None:
    if epsilon_crossover <= 0.18:
        print(f"   epsilon_crossover ~ {epsilon_crossover:.3f} <= 0.18 (foam amplitude)")
        print(f"   => FOAM DISSOLVES THE SPECTRAL TRIPLE at Planck scale.")
        print(f"   => Block-diagonal theorem breaks. Sector mixing occurs.")
        print(f"   => The NCG spectral triple is a LOW-ENERGY effective structure,")
        print(f"      emergent when metric fluctuations are sufficiently small.")
    else:
        print(f"   epsilon_crossover ~ {epsilon_crossover:.3f} > 0.18 (foam amplitude)")
        print(f"   => SPECTRAL TRIPLE SURVIVES foam perturbations.")
        print(f"   => Block-diagonal structure is robust against Planck-scale noise.")
else:
    print(f"   No crossover found in [{EPSILON_VALUES[0]}, {EPSILON_VALUES[-1]}].")

# ============================================================
# Step 7: Save data
# ============================================================
print("\n--- Saving results ---")

save_data = {
    'tau': TAU_FOLD,
    'max_pq_sum': MAX_PQ_SUM,
    'n_sectors': n_sectors,
    'total_dim': total_dim,
    'sector_labels': np.array(sector_labels),
    'sector_dims': np.array(sector_dims),
    'epsilon_values': np.array(EPSILON_VALUES),
    'r_mean': np.array(results['r_mean']),
    'r_std': np.array(results['r_std']),
    'brody_mean': np.array(results['brody_mean']),
    'brody_std': np.array(results['brody_std']),
    'r_unperturbed': r_0,
    'r_poisson': R_POISSON,
    'r_goe': R_GOE,
    'n_samples': N_SAMPLES,
    'evals_unperturbed': evals_0,
}

# Add per-sector results
for label in sector_labels:
    safe_label = label.replace('(', '').replace(')', '').replace(',', '_')
    save_data[f'r_sector_{safe_label}_mean'] = np.array(results['r_per_sector'][label]['mean'])
    save_data[f'r_sector_{safe_label}_std'] = np.array(results['r_per_sector'][label]['std'])

# Add spacing distributions
for eps in results['spacing_distributions']:
    safe_eps = f"{eps:.4f}".replace('.', 'p')
    save_data[f'spacings_eps_{safe_eps}'] = results['spacing_distributions'][eps]

np.savez('tier0-computation/s43_spectral_dissolution.npz', **save_data)
print("  Saved: tier0-computation/s43_spectral_dissolution.npz")

# ============================================================
# Step 8: Plot
# ============================================================
print("  Generating plot...")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.35, wspace=0.3)

# --- Panel 1: <r> vs epsilon ---
ax1 = fig.add_subplot(gs[0, 0])
eps_plot = np.array(EPSILON_VALUES)
r_plot = np.array(results['r_mean'])
r_err_plot = np.array(results['r_std'])

ax1.errorbar(eps_plot, r_plot, yerr=r_err_plot, fmt='ko-', capsize=4,
             linewidth=2, markersize=8, label='Full spectrum <r>')
ax1.axhline(R_POISSON, color='blue', linestyle='--', linewidth=1.5,
            label=f'Poisson ({R_POISSON:.3f})')
ax1.axhline(R_GOE, color='red', linestyle='--', linewidth=1.5,
            label=f'GOE ({R_GOE:.3f})')
ax1.axhline(r_midpoint, color='gray', linestyle=':', linewidth=1,
            label=f'Midpoint ({r_midpoint:.3f})')
# Mark foam amplitude
ax1.axvline(0.18, color='green', linestyle='-', linewidth=2, alpha=0.5,
            label=r'$\delta g/g \sim 0.18$ (foam)')
ax1.set_xlabel(r'$\epsilon$ (perturbation amplitude)', fontsize=12)
ax1.set_ylabel(r'$\langle r \rangle$', fontsize=14)
ax1.set_title('Level Spacing Ratio vs Perturbation Amplitude', fontsize=13)
ax1.set_xscale('log')
ax1.legend(fontsize=9, loc='lower right')
ax1.set_xlim(5e-4, 1)
ax1.set_ylim(0.30, 0.60)
ax1.grid(True, alpha=0.3)

# --- Panel 2: Brody parameter vs epsilon ---
ax2 = fig.add_subplot(gs[0, 1])
b_plot = np.array(results['brody_mean'])
b_err_plot = np.array(results['brody_std'])
valid = ~np.isnan(b_plot)
if np.any(valid):
    ax2.errorbar(eps_plot[valid], b_plot[valid], yerr=b_err_plot[valid],
                 fmt='s-', color='purple', capsize=4, linewidth=2, markersize=8)
    ax2.axhline(0, color='blue', linestyle='--', linewidth=1.5, label='Poisson (beta=0)')
    ax2.axhline(1, color='red', linestyle='--', linewidth=1.5, label='GOE (beta=1)')
    ax2.axvline(0.18, color='green', linestyle='-', linewidth=2, alpha=0.5,
                label=r'$\delta g/g \sim 0.18$')
    ax2.set_xlabel(r'$\epsilon$', fontsize=12)
    ax2.set_ylabel(r'Brody $\beta$', fontsize=14)
    ax2.set_title('Brody Parameter (0=Poisson, 1=GOE)', fontsize=13)
    ax2.set_xscale('log')
    ax2.legend(fontsize=9)
    ax2.set_xlim(5e-4, 1)
    ax2.set_ylim(-0.1, 1.2)
    ax2.grid(True, alpha=0.3)

# --- Panel 3: P(s) at selected epsilon values ---
ax3 = fig.add_subplot(gs[1, 0])
s_theory = np.linspace(0, 4, 200)
ax3.plot(s_theory, poisson_ps(s_theory), 'b--', linewidth=2, label='Poisson')
ax3.plot(s_theory, wigner_goe(s_theory), 'r--', linewidth=2, label='GOE')

colors_ps = plt.cm.viridis(np.linspace(0.1, 0.9, len(EPSILON_VALUES)))
for i, eps in enumerate(EPSILON_VALUES):
    if eps in results['spacing_distributions']:
        spacings = results['spacing_distributions'][eps]
        if len(spacings) > 20:
            hist, bin_edges = np.histogram(spacings, bins=25, range=(0, 4), density=True)
            bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
            ax3.step(bin_centers, hist, color=colors_ps[i], linewidth=1.5,
                     label=f'eps={eps:.3f}', alpha=0.8)

ax3.set_xlabel('s (unfolded spacing)', fontsize=12)
ax3.set_ylabel('P(s)', fontsize=12)
ax3.set_title('Spacing Distribution', fontsize=13)
ax3.legend(fontsize=8, ncol=2)
ax3.set_xlim(0, 4)
ax3.set_ylim(0, 1.2)
ax3.grid(True, alpha=0.3)

# --- Panel 4: Per-sector <r> ---
ax4 = fig.add_subplot(gs[1, 1])
colors_sec = plt.cm.tab10(np.linspace(0, 1, len(sector_labels)))
for idx, label in enumerate(sector_labels):
    r_sec = np.array(results['r_per_sector'][label]['mean'])
    valid_sec = ~np.isnan(r_sec)
    if np.any(valid_sec):
        ax4.plot(eps_plot[valid_sec], r_sec[valid_sec], 'o-',
                 color=colors_sec[idx], linewidth=1.5, markersize=6,
                 label=f'Sector {label}')

ax4.axhline(R_POISSON, color='blue', linestyle='--', linewidth=1, alpha=0.5)
ax4.axhline(R_GOE, color='red', linestyle='--', linewidth=1, alpha=0.5)
ax4.axvline(0.18, color='green', linestyle='-', linewidth=2, alpha=0.3)
ax4.set_xlabel(r'$\epsilon$', fontsize=12)
ax4.set_ylabel(r'$\langle r \rangle$ (sector block)', fontsize=12)
ax4.set_title('Per-Sector Statistics (Diagonal Blocks Only)', fontsize=13)
ax4.set_xscale('log')
ax4.legend(fontsize=8, ncol=2, loc='lower right')
ax4.set_xlim(5e-4, 1)
ax4.set_ylim(0.25, 0.60)
ax4.grid(True, alpha=0.3)

fig.suptitle(f'DISSOLUTION-43: Spectral Triple Dissolution at tau={TAU_FOLD}\n'
             f'Block-diagonal theorem vs non-left-invariant metric perturbations',
             fontsize=14, fontweight='bold')

plt.savefig('tier0-computation/s43_spectral_dissolution.png', dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s43_spectral_dissolution.png")

# ============================================================
# Final timing
# ============================================================
t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s")

# ============================================================
# Dimensional analysis cross-check
# ============================================================
print("\n" + "=" * 70)
print("Dimensional Analysis and Foam Parameter Mapping")
print("=" * 70)
print(f"""
Physical parameters:
  l_P = 1.616e-35 m
  M_P = 1.221e19 GeV
  M_KK ~ 10^{{16.9-17.7}} GeV (CONST-FREEZE-42)

Foam metric fluctuation at KK scale:
  delta_g/g ~ (l_P / R_KK)^{{1/2}} ~ (M_KK / M_P)^{{1/2}}
  For M_KK = 10^{{17.0}} GeV: delta_g/g = 10^{{-0.70}} = 0.200
  For M_KK = 10^{{16.5}} GeV: delta_g/g = 10^{{-0.95}} = 0.112
  For M_KK = 10^{{17.5}} GeV: delta_g/g = 10^{{-0.45}} = 0.355

The epsilon parameter maps directly to delta_g/g since the perturbation
V acts on D_K which is O(1/R_KK) and the perturbation is epsilon * D_K.
""")

if epsilon_crossover is not None:
    print(f"epsilon_crossover = {epsilon_crossover:.4f}")
    print(f"=> For M_KK/M_P = epsilon_crossover^2:")
    print(f"   M_KK_threshold / M_P = {epsilon_crossover**2:.4e}")
    print(f"   M_KK_threshold = {epsilon_crossover**2 * 1.221e19:.3e} GeV")
    print(f"\n=> M_KK < M_KK_threshold: spectral triple dissolved by foam")
    print(f"   M_KK > M_KK_threshold: spectral triple survives")
