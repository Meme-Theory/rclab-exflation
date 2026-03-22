#!/usr/bin/env python3
"""
s45_peter_weyl_censorship.py -- PETER-WEYL-CENSORSHIP-45
=========================================================

Tests whether the 17,594x EIH singlet suppression (Peter-Weyl censorship)
survives perturbations at the dissolution scale epsilon_c ~ 1/sqrt(N).

=== PHYSICS ===

The block-diagonal D_K decomposes by SU(3) representation via Peter-Weyl.
The (0,0) singlet sector contributes only S_singlet/S_fold = 5.68e-5 to the
full spectral action -- the 4D gravitational field sees only this fraction
(EIH-GRAV-44). This "Peter-Weyl censorship" hides 99.994% of internal
energy from 4D gravity.

But S44 DISSOLUTION-SCALING-44 showed that random perturbations of strength
epsilon_c ~ 0.236/sqrt(N) dissolve the block-diagonal structure (level
statistics transition from Poisson to GOE). The critical question:

  Does the singlet fraction of the spectral action survive at epsilon_c?

Three possible outcomes:
  (A) ROBUST: Singlet fraction stays ~5.7e-5 even at epsilon >> epsilon_c.
      Peter-Weyl censorship is protected by more than block-diagonality.
  (B) GRADUAL: Singlet fraction rises smoothly from 5.7e-5 toward 1/N_sectors.
      Censorship degrades but retains some suppression.
  (C) FRAGILE: Singlet fraction jumps to ~1/N_sectors at epsilon ~ epsilon_c.
      Censorship depends entirely on exact block-diagonality.

=== METHOD ===

For each truncation level (max_pq_sum = 1, 2, 3):
  1. Build block-diagonal H_0 = i*D_K
  2. For epsilon in [0, 10*epsilon_c], add random Hermitian perturbation V:
     H_perturbed = H_0 + epsilon * (||H_0||_F / N) * V_random
  3. Compute eigenvalues of H_perturbed
  4. Project back onto singlet sector:
     The singlet spectral action = sum of f(lambda^2) for eigenvalues
     that overlap with the original singlet block.
  5. Monte Carlo: M=100 realizations at each epsilon for error bars.
  6. Repeat for multiple spectral functionals (polynomial, trace-log).

The projection uses the fact that we KNOW which rows/columns belong to the
singlet block. Even after perturbation mixes blocks, we can compute
<singlet | P_0 | singlet> where P_0 projects onto the original singlet subspace.

Gate: PETER-WEYL-CENSORSHIP-45 (INFO)
  Records how singlet fraction changes with epsilon.
  No pre-registered pass/fail -- this is structural exploration.

Input: s44_eih_grav.npz, s44_dissolution_scaling.npz, canonical_constants.py
Output: s45_peter_weyl_censorship.npz, s45_peter_weyl_censorship.png

Author: schwarzschild-penrose-geometer, Session 45
Date: 2026-03-15
"""

import numpy as np
from numpy.linalg import eigvalsh, eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
import sys
import time

t_start = time.time()

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

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
# 0. LOAD PRIOR RESULTS
# ============================================================
print("=" * 72)
print("PETER-WEYL-CENSORSHIP-45")
print("Testing robustness of EIH singlet suppression under perturbation")
print("=" * 72)

eih_data = np.load('tier0-computation/s44_eih_grav.npz', allow_pickle=True)
diss_data = np.load('tier0-computation/s44_dissolution_scaling.npz', allow_pickle=True)

# EIH numbers
S_singlet_exact = float(eih_data['S_singlet'])               # 14.23
S_fold_exact = float(eih_data['S_fold'])                      # 250360.68
ratio_exact = float(eih_data['ratio_singlet_to_full'])        # 5.684e-5
suppression_exact = 1.0 / ratio_exact                         # 17,594x

# Dissolution numbers
N_values_diss = diss_data['N_values']                         # [112, 432, 1232, 2912, 6048]
eps_c_diss = diss_data['epsilon_crossover']                   # [0.021, 0.014, 0.008, 0.0036, 0.0017]
fit_a = float(diss_data['fit_1_sqrtN_params'][0])             # 0.236

print(f"\n  Exact singlet ratio:    {ratio_exact:.6e}")
print(f"  Exact suppression:      {suppression_exact:.0f}x")
print(f"  Dissolution fit:        epsilon_c = {fit_a:.4f} / sqrt(N)")
print(f"  Tau:                    {TAU_FOLD}")

# ============================================================
# 1. BUILD SU(3) INFRASTRUCTURE
# ============================================================
print("\n--- Step 1: Build SU(3) infrastructure ---")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
cliff_err = validate_clifford(gammas)
B_ab = compute_killing_form(f_abc)
g_s = jensen_metric(B_ab, TAU_FOLD)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E)
Gamma = connection_coefficients(ft)
mc_err = validate_connection(Gamma)
Omega = spinor_connection_offset(Gamma, gammas)
_, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)

print(f"  Clifford algebra error: {cliff_err:.2e}")
print(f"  Connection metric error: {mc_err:.2e}")
print(f"  Omega anti-Hermitian error: {ah_err:.2e}")

# ============================================================
# 2. BUILD BLOCK-DIAGONAL D_K FOR EACH TRUNCATION LEVEL
# ============================================================
print("\n--- Step 2: Build block-diagonal operators ---")

# Configuration: (max_pq_sum, n_mc_samples, n_epsilon_points)
# We use truncation levels 1, 2, 3 to cover tractable matrix sizes.
# max_pq_sum=4 (N=2912) is too expensive for 100 MC samples at 20 epsilon points.
CONFIGS = [
    (1, 100, 25),   # N=112,  fast
    (2, 100, 25),   # N=432,  moderate
    (3,  50, 20),   # N=1232, slower (reduce MC to 50)
]

np.random.seed(2026_03_15)  # Session-specific seed

def build_H0_with_blocks(max_pq_sum):
    """Build block-diagonal H0 and return block metadata."""
    sectors = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq
            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
            H_pi = 1j * D_pi
            block_dim = dim_pq * 16
            sectors.append({
                'pq': (p, q),
                'dim_rep': dim_pq,
                'block_dim': block_dim,
                'H_block': H_pi,
                'is_singlet': (p == 0 and q == 0),
            })

    total_dim = sum(s['block_dim'] for s in sectors)
    H0 = np.zeros((total_dim, total_dim), dtype=complex)

    offset = 0
    singlet_indices = None
    for s in sectors:
        d = s['block_dim']
        H0[offset:offset+d, offset:offset+d] = s['H_block']
        if s['is_singlet']:
            singlet_indices = np.arange(offset, offset + d)
        s['start'] = offset
        s['end'] = offset + d
        offset += d

    return H0, sectors, singlet_indices, total_dim


def compute_singlet_fraction_eigenvalue(H_perturbed, singlet_indices, total_dim):
    """
    Compute singlet fraction of the spectral action using eigenvector overlap.

    Method: Diagonalize H_perturbed, get eigenvectors V. For each eigenvector v_k,
    compute w_k = sum_{i in singlet} |v_k[i]|^2 (weight in the singlet subspace).
    Then:
      S_singlet = sum_k f(lambda_k^2) * w_k
      S_total   = sum_k f(lambda_k^2)
      fraction  = S_singlet / S_total

    We compute for three spectral functionals:
      1. Polynomial: f(x) = x^2 (i.e., sum lambda^4 -- dominated by a_4 term)
      2. Polynomial: f(x) = x   (i.e., sum lambda^2 -- dominated by a_2 term)
      3. Trace-log:  f(x) = ln(x)  (logarithmic functional)
    """
    eigenvalues, eigenvectors = eigh(H_perturbed)

    # Weight of each eigenvector in the singlet subspace
    # w_k = sum_{i in singlet} |V[i, k]|^2
    singlet_weights = np.sum(np.abs(eigenvectors[singlet_indices, :])**2, axis=0)
    # singlet_weights[k] is the probability that eigenvector k lives in the singlet block

    abs_evals = np.abs(eigenvalues)
    pos_mask = abs_evals > 1e-12

    # Spectral action (polynomial, a_4-dominated): f(D^2) ~ sum lambda^4
    lam4 = abs_evals**4
    S_total_poly = np.sum(lam4[pos_mask])
    S_singlet_poly = np.sum(lam4[pos_mask] * singlet_weights[pos_mask])
    frac_poly = S_singlet_poly / S_total_poly if S_total_poly > 0 else 0.0

    # a_2 contribution: sum lambda^2
    lam2 = abs_evals**2
    S_total_a2 = np.sum(lam2[pos_mask])
    S_singlet_a2 = np.sum(lam2[pos_mask] * singlet_weights[pos_mask])
    frac_a2 = S_singlet_a2 / S_total_a2 if S_total_a2 > 0 else 0.0

    # Trace-log: Tr ln|D| = sum ln|lambda_k|
    ln_lam = np.log(abs_evals[pos_mask])
    S_total_log = np.sum(np.abs(ln_lam))
    S_singlet_log = np.sum(np.abs(ln_lam) * singlet_weights[pos_mask])
    frac_log = S_singlet_log / S_total_log if S_total_log > 0 else 0.0

    # Number of eigenvalues with >50% singlet weight
    n_singlet_dominant = np.sum(singlet_weights > 0.5)

    return {
        'frac_poly': frac_poly,
        'frac_a2': frac_a2,
        'frac_log': frac_log,
        'singlet_weights': singlet_weights,
        'n_singlet_dominant': n_singlet_dominant,
        'eigenvalues': eigenvalues,
    }


def make_random_perturbation(total_dim, sigma):
    """Create a random Hermitian perturbation with variance sigma per element."""
    V_real = np.random.randn(total_dim, total_dim) * sigma
    V_imag = np.random.randn(total_dim, total_dim) * sigma
    V = (V_real + 1j * V_imag)
    V = (V + V.conj().T) / 2.0
    return V


# ============================================================
# 3. MAIN SWEEP: singlet fraction vs epsilon
# ============================================================
print("\n--- Step 3: Main sweep ---")

all_results = {}

for max_pq, n_mc, n_eps_pts in CONFIGS:
    t_level_start = time.time()

    # Build H0
    H0, sectors, singlet_indices, total_dim = build_H0_with_blocks(max_pq)
    H0_norm = np.linalg.norm(H0, 'fro')
    N = total_dim
    n_sectors = len(sectors)

    # Dissolution threshold for this N
    eps_c = fit_a / np.sqrt(N)

    # Exact singlet fraction (epsilon=0)
    res0 = compute_singlet_fraction_eigenvalue(H0, singlet_indices, total_dim)
    frac0_poly = res0['frac_poly']
    frac0_a2 = res0['frac_a2']
    frac0_log = res0['frac_log']
    n_singlet_block = len(singlet_indices)

    # Weyl prediction: equipartition fraction
    frac_weyl = n_singlet_block / N

    print(f"\n{'='*60}")
    print(f"max_pq_sum={max_pq}: N={N}, n_sectors={n_sectors}")
    print(f"  ||H0||_F = {H0_norm:.4f}")
    print(f"  epsilon_c = {eps_c:.6f} = {fit_a:.4f}/sqrt({N})")
    print(f"  Singlet block size: {n_singlet_block}/{N} = {frac_weyl:.6f}")
    print(f"  Exact frac(poly, eps=0): {frac0_poly:.8f}")
    print(f"  Exact frac(a2, eps=0):   {frac0_a2:.8f}")
    print(f"  Exact frac(log, eps=0):  {frac0_log:.8f}")
    print(f"{'='*60}")

    # Epsilon scan: from 0 to 10*eps_c on a logarithmic + linear scale
    # Include 0, eps_c/10, eps_c/3, eps_c, 3*eps_c, 10*eps_c
    eps_grid = np.sort(np.unique(np.concatenate([
        [0.0],
        np.geomspace(eps_c / 30, eps_c * 10, n_eps_pts - 1),
        [eps_c / 10, eps_c / 3, eps_c, 3 * eps_c, 10 * eps_c],
    ])))

    # Results storage
    frac_poly_arr = np.zeros((len(eps_grid), n_mc))
    frac_a2_arr = np.zeros((len(eps_grid), n_mc))
    frac_log_arr = np.zeros((len(eps_grid), n_mc))
    n_sing_dom_arr = np.zeros((len(eps_grid), n_mc), dtype=int)
    max_singlet_weight_arr = np.zeros((len(eps_grid), n_mc))

    for i_eps, eps in enumerate(eps_grid):
        sigma = eps * H0_norm / N

        for i_mc in range(n_mc):
            if eps == 0.0:
                # No perturbation
                H_pert = H0
            else:
                V = make_random_perturbation(N, sigma)
                H_pert = H0 + V

            res = compute_singlet_fraction_eigenvalue(H_pert, singlet_indices, N)
            frac_poly_arr[i_eps, i_mc] = res['frac_poly']
            frac_a2_arr[i_eps, i_mc] = res['frac_a2']
            frac_log_arr[i_eps, i_mc] = res['frac_log']
            n_sing_dom_arr[i_eps, i_mc] = res['n_singlet_dominant']
            max_singlet_weight_arr[i_eps, i_mc] = np.max(res['singlet_weights'])

        # Progress
        mean_poly = np.mean(frac_poly_arr[i_eps])
        std_poly = np.std(frac_poly_arr[i_eps]) / np.sqrt(n_mc)
        if i_eps % 5 == 0 or eps in [0, eps_c]:
            label = ""
            if eps == 0:
                label = " [EXACT]"
            elif abs(eps - eps_c) / eps_c < 0.05:
                label = " [eps_c]"
            print(f"  eps={eps:.6f}: frac_poly={mean_poly:.8f} +/- {std_poly:.2e}"
                  f"  n_singlet_dom={np.mean(n_sing_dom_arr[i_eps]):.1f}/{n_singlet_block}"
                  f"{label}")

    t_level_end = time.time()
    dt = t_level_end - t_level_start

    # Compute summary statistics
    mean_poly = np.mean(frac_poly_arr, axis=1)
    std_poly = np.std(frac_poly_arr, axis=1) / np.sqrt(n_mc)
    mean_a2 = np.mean(frac_a2_arr, axis=1)
    std_a2 = np.std(frac_a2_arr, axis=1) / np.sqrt(n_mc)
    mean_log = np.mean(frac_log_arr, axis=1)
    std_log = np.std(frac_log_arr, axis=1) / np.sqrt(n_mc)
    mean_n_dom = np.mean(n_sing_dom_arr, axis=1)

    # Find where suppression degrades to 100x (1% singlet fraction)
    suppression_at_grid = 1.0 / mean_poly
    threshold_100x = np.where(suppression_at_grid < 100)[0]
    eps_100x = eps_grid[threshold_100x[0]] if len(threshold_100x) > 0 else None

    # Singlet fraction at eps_c
    idx_c = np.argmin(np.abs(eps_grid - eps_c))
    frac_at_epsc = mean_poly[idx_c]
    supp_at_epsc = 1.0 / frac_at_epsc if frac_at_epsc > 0 else np.inf

    # Singlet fraction at 10*eps_c
    idx_10c = np.argmin(np.abs(eps_grid - 10 * eps_c))
    frac_at_10epsc = mean_poly[idx_10c]
    supp_at_10epsc = 1.0 / frac_at_10epsc if frac_at_10epsc > 0 else np.inf

    all_results[max_pq] = {
        'N': N,
        'n_sectors': n_sectors,
        'n_singlet_block': n_singlet_block,
        'eps_c': eps_c,
        'frac_weyl': frac_weyl,
        'eps_grid': eps_grid,
        'mean_poly': mean_poly,
        'std_poly': std_poly,
        'mean_a2': mean_a2,
        'std_a2': std_a2,
        'mean_log': mean_log,
        'std_log': std_log,
        'mean_n_dom': mean_n_dom,
        'frac0_poly': frac0_poly,
        'frac0_a2': frac0_a2,
        'frac_at_epsc': frac_at_epsc,
        'supp_at_epsc': supp_at_epsc,
        'frac_at_10epsc': frac_at_10epsc,
        'supp_at_10epsc': supp_at_10epsc,
        'eps_100x': eps_100x,
        'dt': dt,
        'max_singlet_weight': np.mean(max_singlet_weight_arr, axis=1),
    }

    print(f"\n  --- SUMMARY (max_pq={max_pq}, N={N}) ---")
    print(f"  Time: {dt:.1f}s ({dt/60:.1f}min)")
    print(f"  Exact frac (eps=0):       {frac0_poly:.8f}  (suppression: {1/frac0_poly:.0f}x)")
    print(f"  Frac at eps_c={eps_c:.5f}: {frac_at_epsc:.8f}  (suppression: {supp_at_epsc:.0f}x)")
    print(f"  Frac at 10*eps_c:         {frac_at_10epsc:.8f}  (suppression: {supp_at_10epsc:.0f}x)")
    print(f"  Weyl equipartition:       {frac_weyl:.8f}  (suppression: {1/frac_weyl:.0f}x)")
    if eps_100x is not None:
        print(f"  Suppression < 100x at:    eps = {eps_100x:.6f} = {eps_100x/eps_c:.2f} * eps_c")
    else:
        print(f"  Suppression stays > 100x for all eps tested")


# ============================================================
# 4. CROSS-TRUNCATION COMPARISON
# ============================================================
print("\n" + "=" * 72)
print("Step 4: Cross-Truncation Comparison")
print("=" * 72)

print(f"\n  {'max_pq':>7s} {'N':>7s} {'eps_c':>10s} {'frac(0)':>12s} "
      f"{'frac(eps_c)':>14s} {'supp(eps_c)':>12s} {'frac(10c)':>12s} {'supp(10c)':>12s}")
print(f"  {'-'*94}")
for max_pq in sorted(all_results.keys()):
    r = all_results[max_pq]
    print(f"  {max_pq:>7d} {r['N']:>7d} {r['eps_c']:>10.6f} {r['frac0_poly']:>12.8f} "
          f"{r['frac_at_epsc']:>14.8f} {r['supp_at_epsc']:>12.0f}x "
          f"{r['frac_at_10epsc']:>12.8f} {r['supp_at_10epsc']:>12.0f}x")

# Determine regime: robust, gradual, or fragile
print(f"\n  REGIME CLASSIFICATION:")
for max_pq in sorted(all_results.keys()):
    r = all_results[max_pq]
    ratio_change = r['frac_at_epsc'] / r['frac0_poly']
    ratio_change_10 = r['frac_at_10epsc'] / r['frac0_poly']

    if ratio_change < 1.1:
        regime = "ROBUST at eps_c"
    elif ratio_change < 2.0:
        regime = "SLIGHTLY DEGRADED at eps_c"
    elif ratio_change < 10.0:
        regime = "MODERATELY DEGRADED at eps_c"
    else:
        regime = "FRAGILE at eps_c"

    if ratio_change_10 < 2.0:
        regime_10 = "ROBUST at 10*eps_c"
    elif ratio_change_10 < 10.0:
        regime_10 = "MODERATELY DEGRADED at 10*eps_c"
    else:
        regime_10 = "FRAGILE at 10*eps_c"

    print(f"  pq={max_pq}: {regime} (ratio change: {ratio_change:.2f}x); "
          f"{regime_10} (ratio change: {ratio_change_10:.2f}x)")

# ============================================================
# 5. PHYSICAL INTERPRETATION
# ============================================================
print("\n" + "=" * 72)
print("Step 5: Physical Interpretation")
print("=" * 72)

# Average across truncations at eps_c
avg_degradation_at_c = np.mean([all_results[k]['frac_at_epsc'] / all_results[k]['frac0_poly']
                                 for k in all_results])
avg_degradation_at_10c = np.mean([all_results[k]['frac_at_10epsc'] / all_results[k]['frac0_poly']
                                   for k in all_results])

print(f"\n  Average singlet fraction change:")
print(f"    At eps_c:     {avg_degradation_at_c:.2f}x exact value")
print(f"    At 10*eps_c:  {avg_degradation_at_10c:.2f}x exact value")
print(f"\n  Note: level statistics undergo Poisson -> GOE transition at eps_c.")
print(f"  The question is whether the SPECTRAL ACTION (an integrated quantity)")
print(f"  is as sensitive as the LEVEL STATISTICS (a local quantity).")
print(f"\n  If the fraction changes by <2x at eps_c, the spectral action is more")
print(f"  robust than level statistics -- the integrated quantity is protected")
print(f"  by a sum rule (total spectral action is approximately conserved).")
print(f"  This would be analogous to the ADM mass being robust against")
print(f"  local perturbations: the 1/r monopole term is an integral quantity")
print(f"  that doesn't care about local multipole structure.")

# ============================================================
# 6. PENROSE DIAGRAM ANALYSIS
# ============================================================
print("\n" + "=" * 72)
print("Step 6: Causal Structure (Schwarzschild-Penrose Analysis)")
print("=" * 72)

print("""
  The Peter-Weyl censorship is the spectral analog of the event horizon:

  SPACETIME:   Interior mass-energy HIDDEN from I+ by the event horizon
  SPECTRAL:    Non-singlet energy HIDDEN from 4D gravity by Peter-Weyl

  The dissolution threshold epsilon_c is the spectral analog of the
  Cauchy horizon stability problem:

  SPACETIME:   Cauchy horizon is an inner boundary; perturbations may
               destabilize it (mass inflation instability)
  SPECTRAL:    Block-diagonality is an inner boundary of the spectral
               triple structure; perturbations at epsilon_c dissolve it

  The KEY QUESTION is whether the EIH singlet fraction (analogous to
  ADM mass seen at I+) is affected when the block structure (analogous
  to the inner causal structure) is perturbed.

  In GR, the ADM mass is ROBUST: perturbations of the interior (even
  violent ones that change the Cauchy horizon) do not change the total
  mass measured at spatial infinity. This is Bondi mass loss = radiation
  emitted to I+, which is bounded.

  The spectral analog: does the singlet projection of the spectral
  action (analogous to ADM mass) change when block-diagonality
  (analogous to causal structure) is perturbed?
""")

# Report analogy status
print(f"  RESULT:")
if avg_degradation_at_c < 2.0 and avg_degradation_at_10c < 10.0:
    analogy_status = "ADM-LIKE ROBUSTNESS CONFIRMED"
    print(f"  {analogy_status}")
    print(f"  The singlet fraction is MORE ROBUST than level statistics.")
    print(f"  Peter-Weyl censorship is protected by a sum-rule mechanism")
    print(f"  analogous to ADM mass conservation: the spectral action is")
    print(f"  an integrated (global) quantity that averages over local")
    print(f"  perturbative mixing.")
elif avg_degradation_at_c < 10.0:
    analogy_status = "PARTIAL CENSORSHIP SURVIVAL"
    print(f"  {analogy_status}")
    print(f"  The singlet fraction degrades but retains significant suppression.")
    print(f"  Analogous to Bondi mass loss: some energy 'leaks' through the")
    print(f"  censorship boundary, but the bulk remains hidden.")
else:
    analogy_status = "CAUCHY INSTABILITY ANALOG"
    print(f"  {analogy_status}")
    print(f"  The singlet fraction degrades severely at eps_c.")
    print(f"  Analogous to mass inflation: the inner causal structure")
    print(f"  is destroyed, and the censorship fails.")

# ============================================================
# 7. GATE VERDICT
# ============================================================
print("\n" + "=" * 72)
print("GATE: PETER-WEYL-CENSORSHIP-45 (INFO)")
print("=" * 72)

# Key numbers at the largest truncation
best_pq = max(all_results.keys())
r_best = all_results[best_pq]
verdict = "INFO"

print(f"\n  Reference truncation: max_pq_sum={best_pq}, N={r_best['N']}")
print(f"  Exact singlet fraction (eps=0):  {r_best['frac0_poly']:.8f}")
print(f"  At eps_c = {r_best['eps_c']:.6f}:           {r_best['frac_at_epsc']:.8f} "
      f"({r_best['frac_at_epsc']/r_best['frac0_poly']:.2f}x exact)")
print(f"  At 10*eps_c:                     {r_best['frac_at_10epsc']:.8f} "
      f"({r_best['frac_at_10epsc']/r_best['frac0_poly']:.2f}x exact)")
print(f"  Weyl equipartition limit:        {r_best['frac_weyl']:.8f}")
print(f"\n  Suppression factors:")
print(f"    eps=0:      {1/r_best['frac0_poly']:.0f}x")
print(f"    eps=eps_c:  {r_best['supp_at_epsc']:.0f}x")
print(f"    eps=10*c:   {r_best['supp_at_10epsc']:.0f}x")
print(f"    Weyl limit: {1/r_best['frac_weyl']:.0f}x")
print(f"\n  Analogy: {analogy_status}")
print(f"\n  VERDICT: {verdict}")

# ============================================================
# 8. SAVE DATA
# ============================================================
print("\n--- Saving results ---")

save_dict = {
    'gate_verdict': np.array([verdict]),
    'gate_name': np.array(['PETER-WEYL-CENSORSHIP-45']),
    'tau': TAU_FOLD,
    'S_singlet_exact': S_singlet_exact,
    'S_fold_exact': S_fold_exact,
    'ratio_exact': ratio_exact,
    'suppression_exact': suppression_exact,
    'fit_a_dissolution': fit_a,
    'analogy_status': np.array([analogy_status]),
    'avg_degradation_at_c': avg_degradation_at_c,
    'avg_degradation_at_10c': avg_degradation_at_10c,
}

for max_pq, r in all_results.items():
    prefix = f'pq{max_pq}'
    save_dict[f'{prefix}_N'] = np.array([r['N']])
    save_dict[f'{prefix}_n_sectors'] = np.array([r['n_sectors']])
    save_dict[f'{prefix}_n_singlet_block'] = np.array([r['n_singlet_block']])
    save_dict[f'{prefix}_eps_c'] = np.array([r['eps_c']])
    save_dict[f'{prefix}_frac_weyl'] = np.array([r['frac_weyl']])
    save_dict[f'{prefix}_eps_grid'] = r['eps_grid']
    save_dict[f'{prefix}_mean_poly'] = r['mean_poly']
    save_dict[f'{prefix}_std_poly'] = r['std_poly']
    save_dict[f'{prefix}_mean_a2'] = r['mean_a2']
    save_dict[f'{prefix}_std_a2'] = r['std_a2']
    save_dict[f'{prefix}_mean_log'] = r['mean_log']
    save_dict[f'{prefix}_std_log'] = r['std_log']
    save_dict[f'{prefix}_mean_n_dom'] = r['mean_n_dom']
    save_dict[f'{prefix}_frac0_poly'] = np.array([r['frac0_poly']])
    save_dict[f'{prefix}_frac0_a2'] = np.array([r['frac0_a2']])
    save_dict[f'{prefix}_frac_at_epsc'] = np.array([r['frac_at_epsc']])
    save_dict[f'{prefix}_supp_at_epsc'] = np.array([r['supp_at_epsc']])
    save_dict[f'{prefix}_frac_at_10epsc'] = np.array([r['frac_at_10epsc']])
    save_dict[f'{prefix}_supp_at_10epsc'] = np.array([r['supp_at_10epsc']])
    save_dict[f'{prefix}_max_singlet_weight'] = r['max_singlet_weight']
    save_dict[f'{prefix}_dt'] = np.array([r['dt']])

np.savez('tier0-computation/s45_peter_weyl_censorship.npz', **save_dict)
print("  Saved: tier0-computation/s45_peter_weyl_censorship.npz")

# ============================================================
# 9. PLOT
# ============================================================
print("  Generating plot...")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 2, hspace=0.40, wspace=0.30)

colors_pq = {1: '#1f77b4', 2: '#ff7f0e', 3: '#2ca02c'}
linestyles_func = {'poly': '-', 'a2': '--', 'log': ':'}

# --- Panel 1: Singlet fraction (polynomial) vs epsilon ---
ax1 = fig.add_subplot(gs[0, 0])
for max_pq in sorted(all_results.keys()):
    r = all_results[max_pq]
    eps = r['eps_grid']
    mask = eps > 0
    ax1.errorbar(eps[mask], r['mean_poly'][mask], yerr=r['std_poly'][mask],
                 fmt='o-', color=colors_pq[max_pq], markersize=3, linewidth=1.2,
                 capsize=2, label=f'pq={max_pq} (N={r["N"]})')
    # Mark eps_c
    ax1.axvline(r['eps_c'], color=colors_pq[max_pq], linestyle=':', alpha=0.5)
    # Mark exact value
    ax1.axhline(r['frac0_poly'], color=colors_pq[max_pq], linestyle='--', alpha=0.3)
    # Mark Weyl limit
    ax1.axhline(r['frac_weyl'], color=colors_pq[max_pq], linestyle='-.', alpha=0.2)

ax1.set_xlabel(r'$\epsilon$ (perturbation strength)', fontsize=11)
ax1.set_ylabel(r'Singlet fraction of $\mathrm{Tr}\, f(D_K^2)$', fontsize=11)
ax1.set_title(r'Peter-Weyl Censorship: Singlet Fraction vs $\epsilon$ (polynomial)', fontsize=12)
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# --- Panel 2: Suppression factor vs epsilon ---
ax2 = fig.add_subplot(gs[0, 1])
for max_pq in sorted(all_results.keys()):
    r = all_results[max_pq]
    eps = r['eps_grid']
    mask = eps > 0
    supp = 1.0 / r['mean_poly'][mask]
    ax2.plot(eps[mask], supp, 'o-', color=colors_pq[max_pq], markersize=3,
             linewidth=1.2, label=f'pq={max_pq} (N={r["N"]})')
    ax2.axvline(r['eps_c'], color=colors_pq[max_pq], linestyle=':', alpha=0.5)

ax2.axhline(suppression_exact, color='red', linestyle='--', alpha=0.5,
            label=f'Exact (S44): {suppression_exact:.0f}x')
ax2.axhline(100, color='gray', linestyle=':', alpha=0.5, label='100x threshold')
ax2.set_xlabel(r'$\epsilon$', fontsize=11)
ax2.set_ylabel('Suppression factor', fontsize=11)
ax2.set_title('EIH Suppression Factor vs Perturbation Strength', fontsize=12)
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)

# --- Panel 3: Singlet fraction ratio (frac/frac0) vs eps/eps_c ---
ax3 = fig.add_subplot(gs[1, 0])
for max_pq in sorted(all_results.keys()):
    r = all_results[max_pq]
    eps = r['eps_grid']
    mask = eps > 0
    x = eps[mask] / r['eps_c']  # Normalized epsilon
    y = r['mean_poly'][mask] / r['frac0_poly']  # Normalized singlet fraction
    ax3.plot(x, y, 'o-', color=colors_pq[max_pq], markersize=3, linewidth=1.2,
             label=f'pq={max_pq} (N={r["N"]})')

ax3.axhline(1.0, color='black', linestyle='-', alpha=0.3, label='Exact (no perturbation)')
ax3.axhline(2.0, color='red', linestyle='--', alpha=0.3, label='2x degradation')
ax3.axvline(1.0, color='gray', linestyle=':', alpha=0.5, label=r'$\epsilon = \epsilon_c$')
ax3.set_xlabel(r'$\epsilon / \epsilon_c$', fontsize=11)
ax3.set_ylabel(r'$f_{\mathrm{singlet}}(\epsilon) / f_{\mathrm{singlet}}(0)$', fontsize=11)
ax3.set_title(r'Relative Degradation of Censorship (normalized to $\epsilon_c$)', fontsize=12)
ax3.set_xscale('log')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# --- Panel 4: Three spectral functionals compared (best truncation) ---
ax4 = fig.add_subplot(gs[1, 1])
r = all_results[best_pq]
eps = r['eps_grid']
mask = eps > 0
for name, mean_key, std_key, ls, clr in [
    ('Polynomial (a4)', 'mean_poly', 'std_poly', '-', '#1f77b4'),
    ('Curvature (a2)', 'mean_a2', 'std_a2', '--', '#ff7f0e'),
    ('Trace-log', 'mean_log', 'std_log', ':', '#2ca02c'),
]:
    ax4.errorbar(eps[mask], r[mean_key][mask], yerr=r[std_key][mask],
                 fmt='o', markersize=2, linewidth=1.2, linestyle=ls, color=clr,
                 capsize=2, label=name)

ax4.axvline(r['eps_c'], color='gray', linestyle=':', alpha=0.5, label=r'$\epsilon_c$')
ax4.set_xlabel(r'$\epsilon$', fontsize=11)
ax4.set_ylabel('Singlet fraction', fontsize=11)
ax4.set_title(f'Three Spectral Functionals (pq={best_pq}, N={r["N"]})', fontsize=12)
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

# --- Panel 5: Number of singlet-dominant eigenvectors ---
ax5 = fig.add_subplot(gs[2, 0])
for max_pq in sorted(all_results.keys()):
    r = all_results[max_pq]
    eps = r['eps_grid']
    mask = eps > 0
    ax5.plot(eps[mask], r['mean_n_dom'][mask], 'o-', color=colors_pq[max_pq],
             markersize=3, linewidth=1.2, label=f'pq={max_pq} (n_block={r["n_singlet_block"]})')
    ax5.axhline(r['n_singlet_block'], color=colors_pq[max_pq], linestyle='--', alpha=0.3)
    ax5.axvline(r['eps_c'], color=colors_pq[max_pq], linestyle=':', alpha=0.5)

ax5.set_xlabel(r'$\epsilon$', fontsize=11)
ax5.set_ylabel('Eigenvectors with >50% singlet weight', fontsize=11)
ax5.set_title('Singlet-Dominant Eigenvector Count', fontsize=12)
ax5.set_xscale('log')
ax5.legend(fontsize=9)
ax5.grid(True, alpha=0.3)

# --- Panel 6: Max singlet weight of any eigenvector ---
ax6 = fig.add_subplot(gs[2, 1])
for max_pq in sorted(all_results.keys()):
    r = all_results[max_pq]
    eps = r['eps_grid']
    mask = eps > 0
    ax6.plot(eps[mask], r['max_singlet_weight'][mask], 'o-', color=colors_pq[max_pq],
             markersize=3, linewidth=1.2, label=f'pq={max_pq} (N={r["N"]})')
    ax6.axvline(r['eps_c'], color=colors_pq[max_pq], linestyle=':', alpha=0.5)

ax6.axhline(1.0, color='black', linestyle='-', alpha=0.3)
ax6.set_xlabel(r'$\epsilon$', fontsize=11)
ax6.set_ylabel('Max singlet weight of any eigenvector', fontsize=11)
ax6.set_title('Eigenvector Localization in Singlet Block', fontsize=12)
ax6.set_xscale('log')
ax6.legend(fontsize=9)
ax6.grid(True, alpha=0.3)

fig.suptitle('PETER-WEYL-CENSORSHIP-45: Robustness of EIH Singlet Suppression\n'
             f'Tau={TAU_FOLD} | Exact suppression: {suppression_exact:.0f}x | '
             f'Dissolution: eps_c = {fit_a:.3f}/sqrt(N)',
             fontsize=13, fontweight='bold')

plt.savefig('tier0-computation/s45_peter_weyl_censorship.png', dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s45_peter_weyl_censorship.png")

# ============================================================
# 10. FINAL SUMMARY
# ============================================================
t_end = time.time()
total_time = t_end - t_start

print(f"\n{'='*72}")
print(f"PETER-WEYL-CENSORSHIP-45: FINAL SUMMARY")
print(f"{'='*72}")

print(f"\n  Total runtime: {total_time:.1f}s ({total_time/60:.1f}min)")
print(f"\n  QUESTION: Does the 17,594x EIH suppression survive at epsilon_c?")
print(f"\n  ANSWER:")

for max_pq in sorted(all_results.keys()):
    r = all_results[max_pq]
    print(f"    pq={max_pq} (N={r['N']}): {r['supp_at_epsc']:.0f}x at eps_c "
          f"(was {1/r['frac0_poly']:.0f}x at eps=0). "
          f"Degradation: {r['frac_at_epsc']/r['frac0_poly']:.2f}x")

print(f"\n  REGIME: {analogy_status}")

print(f"\n  CONSTRAINT ON SOLUTION SPACE:")
print(f"  The Peter-Weyl singlet projection (EIH censorship) is an")
print(f"  INTEGRATED quantity (spectral action = sum over eigenvalues).")
print(f"  Its robustness/fragility under dissolution-scale perturbations")
print(f"  determines whether the 4.25-order CC suppression from S44 is:")
print(f"    - STRUCTURAL (survives any reasonable perturbation)")
print(f"    - CONDITIONAL (requires block-diagonality to hold)")

print(f"\n  Verdict: {verdict}")
print(f"  Status: {analogy_status}")
print(f"\n{'='*72}")
