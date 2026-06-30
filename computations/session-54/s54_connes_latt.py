#!/usr/bin/env python3
"""
S54 CONNES-LATT-54: Connes distance on 32-cell Voronoi graph.

Computes d_D(i,j) = sup{|f_i - f_j| : ||[D, pi(f)]||_op <= 1}
for all 496 cell pairs at 10 tau values in [0.00, 0.35].

FINITE SPECTRAL TRIPLE:
  A = C(V) = C^32  (functions on 32 vertices)
  H = C^32
  D = H_TB(tau) - diag(H_TB)  (off-diagonal part; diagonal is invisible to [D, .])

MATHEMATICAL STRUCTURE:
  For f: V -> R, [D, diag(f)]_{kl} = (f_k - f_l) D_{kl}.
  Since D is symmetric, this commutator is ANTISYMMETRIC.
  The spectral norm constraint ||[D,f]||_op <= 1 is a semidefinite constraint:
    [[I, M], [-M, I]] >> 0   (Schur complement for sigma_max(M) <= 1)
  where M(f) = sum_k f_k E_k, E_k = e_k e_k^T D - D e_k e_k^T.

SOLVER: cvxpy with CLARABEL backend, parametric SDP (compile once per tau).

Gate: CONNES-LATT-54
  PASS: mean d_Connes/d_continuum in [0.5, 2.0] at all tau AND <d_D> varies with tau
  FAIL: distances degenerate or ratio outside [0.1, 10]

Author: Connes-NCG-Theorist (Session 54)
"""

import numpy as np
import cvxpy as cp
from scipy.interpolate import interp1d
import time
import os
import sys
import warnings
warnings.filterwarnings('ignore')

# ─── paths ───────────────────────────────────────────────────────────────
PROJ = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(PROJ, "s54_tb_hamiltonian.npz")
OUTPUT_NPZ = os.path.join(PROJ, "s54_connes_latt.npz")
OUTPUT_PNG = os.path.join(PROJ, "s54_connes_latt.png")
S46_FILE = os.path.join(PROJ, "..", "_shared", "s46_connes_distance.npz")


def build_basis_matrices(D_off):
    """Build the E_k basis for the commutator [D_off, diag(f)].

    E_k = e_k e_k^T @ D_off - D_off @ e_k e_k^T

    So that [D_off, diag(f)] = sum_k f_k E_k.

    Mathematical verification:
      [diag(f), D]_{ab} = f_a D_{ab} - D_{ab} f_b = (f_a - f_b) D_{ab}
      (sum_k f_k E_k)_{ab} = sum_k f_k (delta_{ak} D_{kb} - D_{ak} delta_{kb})
                            = f_a D_{ab} - D_{ab} f_b.  Correct.
    """
    N = D_off.shape[0]
    E_list = []
    for k in range(N):
        ek = np.zeros(N)
        ek[k] = 1.0
        Ek = np.outer(ek, ek) @ D_off - D_off @ np.outer(ek, ek)
        E_list.append(Ek)
    return E_list


def compute_all_connes_distances(D_off, label=""):
    """Compute all 496 Connes distances for a 32-node graph via parametric SDP.

    The SDP for each pair (i,j):
      maximize   f_i - f_j
      subject to [[I, M(f)], [-M(f), I]] >> 0

    where M(f) = sum_k f_k E_k is the commutator [D_off, diag(f)].
    The Schur complement ensures sigma_max(M) <= 1.
    """
    N = D_off.shape[0]
    n_pairs = N * (N - 1) // 2

    # Build basis
    E_list = build_basis_matrices(D_off)

    # Set up parametric SDP
    f_var = cp.Variable(N)
    c_param = cp.Parameter(N)

    M = sum(f_var[k] * E_list[k] for k in range(N))
    I_n = np.eye(N)
    top = cp.hstack([I_n, M])
    bot = cp.hstack([-M, I_n])
    big = cp.vstack([top, bot])

    objective = cp.Maximize(c_param @ f_var)
    constraints = [big >> 0]
    prob = cp.Problem(objective, constraints)

    # Warm compile
    c_val = np.zeros(N)
    c_val[0] = 1.0
    c_val[1] = -1.0
    c_param.value = c_val
    prob.solve(solver=cp.CLARABEL, verbose=False)

    # Solve all pairs
    pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    dist_matrix = np.zeros((N, N))
    distances_flat = np.zeros(n_pairs)

    for idx, (i, j) in enumerate(pairs):
        c_val = np.zeros(N)
        c_val[i] = 1.0
        c_val[j] = -1.0
        c_param.value = c_val

        try:
            prob.solve(solver=cp.CLARABEL, verbose=False, warm_start=True)
            if prob.status not in ['infeasible', 'unbounded', None] and prob.value is not None:
                d = max(prob.value, 0.0)
            else:
                d = np.nan
        except Exception:
            d = np.nan

        dist_matrix[i, j] = d
        dist_matrix[j, i] = d
        distances_flat[idx] = d

        if (idx + 1) % 100 == 0:
            print(f"    {label} pair {idx+1}/{n_pairs}")

    return dist_matrix, distances_flat


def main():
    print("=" * 70)
    print("S54 CONNES-LATT-54: Connes Distance on 32-Cell Voronoi Graph")
    print("=" * 70)

    # ─── Load ────────────────────────────────────────────────────────────
    data = np.load(INPUT, allow_pickle=True)
    all_tau = data['tau_values']
    hamiltonians = data['hamiltonians']
    adjacency = data['adjacency']
    cell_labels = data['cell_labels']
    cell_dims = data['cell_dims']

    N = hamiltonians.shape[1]
    n_pairs = N * (N - 1) // 2
    print(f"\nGraph: {N} nodes, {adjacency.sum() // 2} edges, diameter {int(data['diameter'])}")

    # Select 10 tau values
    tau_target = np.linspace(0.0, 0.35, 10)
    tau_indices = [int(np.argmin(np.abs(all_tau - t))) for t in tau_target]
    tau_values = all_tau[np.array(tau_indices)]
    print(f"Tau values: {[f'{t:.4f}' for t in tau_values]}")

    # ─── Validation ──────────────────────────────────────────────────────
    print("\n--- Validation ---")
    D_test = hamiltonians[0]
    D_off_test = D_test - np.diag(D_test.diagonal())

    # Antisymmetry check
    f_rnd = np.random.randn(N)
    M_comm = (f_rnd[:, None] - f_rnd[None, :]) * D_off_test
    assert np.allclose(M_comm, -M_comm.T, atol=1e-14)
    print("  Commutator antisymmetry: VERIFIED")

    # Self-adjointness of D
    assert np.allclose(D_test, D_test.T, atol=1e-12)
    print("  D = D^T (self-adjoint): VERIFIED")

    # Compact resolvent (finite-dimensional, automatic)
    print("  Compact resolvent: AUTOMATIC (finite N=32)")

    # Bounded commutator (finite-dimensional, automatic for continuous functions)
    print("  [D, a] bounded: AUTOMATIC (A = C^32 finite)")

    # ─── Full computation ────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("FULL COMPUTATION")
    print(f"{'='*70}")

    all_dists_mat = np.zeros((len(tau_values), N, N))
    all_dists_flat = np.zeros((len(tau_values), n_pairs))
    mean_d = np.zeros(len(tau_values))
    max_d = np.zeros(len(tau_values))
    min_d = np.zeros(len(tau_values))
    med_d = np.zeros(len(tau_values))
    std_d = np.zeros(len(tau_values))

    t_total = time.time()

    for t_idx, (tau_idx, tau) in enumerate(zip(tau_indices, tau_values)):
        print(f"\n--- tau = {tau:.4f} ({t_idx+1}/{len(tau_values)}) ---")
        D = hamiltonians[tau_idx].copy()
        D_off = D - np.diag(D.diagonal())

        assert np.allclose(D, D.T, atol=1e-12)

        t0 = time.time()
        dist_mat, dist_flat = compute_all_connes_distances(D_off, label=f"tau={tau:.3f}")
        elapsed = time.time() - t0

        all_dists_mat[t_idx] = dist_mat
        all_dists_flat[t_idx] = dist_flat

        nz = dist_flat[dist_flat > 1e-15]
        n_nan = np.isnan(dist_flat).sum()
        n_zero = (dist_flat < 1e-15).sum()

        mean_d[t_idx] = np.nanmean(nz) if len(nz) > 0 else 0
        max_d[t_idx] = np.nanmax(nz) if len(nz) > 0 else 0
        min_d[t_idx] = np.nanmin(nz) if len(nz) > 0 else 0
        med_d[t_idx] = np.nanmedian(nz) if len(nz) > 0 else 0
        std_d[t_idx] = np.nanstd(nz) if len(nz) > 0 else 0

        print(f"  Mean = {mean_d[t_idx]:.6f}, Median = {med_d[t_idx]:.6f}")
        print(f"  Min  = {min_d[t_idx]:.6f}, Max = {max_d[t_idx]:.6f}")
        print(f"  Std  = {std_d[t_idx]:.6f}")
        print(f"  NaN={n_nan}, Zero={n_zero}, Time={elapsed:.1f}s")

    t_total = time.time() - t_total
    print(f"\nTotal: {t_total:.1f}s ({t_total/60:.1f} min)")

    # ─── Continuum comparison ────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("CONTINUUM COMPARISON (S46)")
    print(f"{'='*70}")

    ratios = None
    ratios_max = None
    d_cont = None

    if os.path.exists(S46_FILE):
        s46 = np.load(S46_FILE, allow_pickle=True)
        tau_c = s46['tau_sweep']
        diam_c = s46['diameter_sweep']

        # S46: continuum Connes diameter in M_KK^{-1}
        interp_fn = interp1d(tau_c, diam_c, kind='linear', fill_value='extrapolate')
        d_cont = interp_fn(tau_values)

        # Also get mean of the 3 directional distances as a "mean" continuum measure
        d_su2 = interp1d(tau_c, s46['d_su2_sweep'], fill_value='extrapolate')(tau_values)
        d_c2 = interp1d(tau_c, s46['d_c2_sweep'], fill_value='extrapolate')(tau_values)
        d_u1 = interp1d(tau_c, s46['d_u1_sweep'], fill_value='extrapolate')(tau_values)
        d_cont_mean = (d_su2 + d_c2 + d_u1) / 3.0

        ratios = mean_d / d_cont_mean
        ratios_max = max_d / d_cont

        print(f"\n{'tau':>8s} | {'<d_latt>':>10s} | {'d_cont_mean':>12s} | {'d_cont_diam':>12s} | "
              f"{'mean/mean':>10s} | {'max/diam':>10s}")
        print("-" * 80)
        for t_idx in range(len(tau_values)):
            print(f"{tau_values[t_idx]:8.4f} | {mean_d[t_idx]:10.6f} | "
                  f"{d_cont_mean[t_idx]:12.6f} | {d_cont[t_idx]:12.6f} | "
                  f"{ratios[t_idx]:10.4f} | {ratios_max[t_idx]:10.4f}")

        print(f"\nRatio (mean/mean): mean={ratios.mean():.4f}, "
              f"range=[{ratios.min():.4f}, {ratios.max():.4f}]")
        print(f"Ratio (max/diam):  mean={ratios_max.mean():.4f}, "
              f"range=[{ratios_max.min():.4f}, {ratios_max.max():.4f}]")
    else:
        print("S46 data not found.")

    # ─── Variation analysis ──────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("VARIATION ANALYSIS")
    print(f"{'='*70}")

    mean_range = mean_d.max() - mean_d.min()
    rel_var = mean_range / mean_d.mean() if mean_d.mean() > 0 else 0

    print(f"<d_D> range: [{mean_d.min():.6f}, {mean_d.max():.6f}]")
    print(f"Absolute variation: {mean_range:.6f}")
    print(f"Relative variation: {rel_var:.4f} ({rel_var*100:.2f}%)")

    degenerate = rel_var < 0.001

    diffs = np.diff(mean_d)
    mono_inc = np.all(diffs > 0)
    mono_dec = np.all(diffs < 0)
    print(f"Monotone increasing: {mono_inc}")
    print(f"Monotone decreasing: {mono_dec}")
    if not mono_inc and not mono_dec:
        turns = np.where(np.diff(np.sign(diffs)))[0]
        print(f"Sign changes at tau indices: {turns}")

    fold_idx = int(np.argmin(np.abs(tau_values - 0.19)))
    print(f"\n<d_D>(tau=0.00)         = {mean_d[0]:.6f}")
    print(f"<d_D>(tau~{tau_values[fold_idx]:.2f}, fold) = {mean_d[fold_idx]:.6f}")
    print(f"<d_D>(tau=0.35)         = {mean_d[-1]:.6f}")
    print(f"fold/origin ratio       = {mean_d[fold_idx]/mean_d[0]:.6f}")
    print(f"end/origin ratio        = {mean_d[-1]/mean_d[0]:.6f}")

    # Per-pair variation
    pair_std = np.std(all_dists_flat, axis=0)
    pair_mean = np.mean(all_dists_flat, axis=0)
    pair_cv = pair_std / (pair_mean + 1e-30)
    valid = pair_mean > 1e-10
    print(f"\nPer-pair CV: mean={pair_cv[valid].mean():.4f}, max={pair_cv[valid].max():.4f}")

    # Topology of distance: check triangle inequality
    print(f"\n--- Triangle inequality check at fold ---")
    D_fold = all_dists_mat[fold_idx]
    violations = 0
    max_violation = 0.0  # (local)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                # Check all 3 permutations
                for a, b, c in [(i,j,k), (i,k,j), (j,k,i)]:
                    excess = D_fold[a,b] - D_fold[a,c] - D_fold[c,b]
                    if excess > 1e-10:
                        violations += 1
                        max_violation = max(max_violation, excess)
    print(f"Triangle inequality violations: {violations}")
    print(f"Max violation: {max_violation:.2e}")
    if violations == 0:
        print("  -> VERIFIED: Connes distances form a METRIC on the 32-cell graph.")

    # ─── Gate verdict ────────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("GATE VERDICT: CONNES-LATT-54")
    print(f"{'='*70}")

    varies = not degenerate

    if ratios is not None:
        in_pass = np.all((ratios >= 0.5) & (ratios <= 2.0))
        in_outer = np.all((ratios >= 0.1) & (ratios <= 10.0))
    else:
        in_pass = True
        in_outer = True

    if varies and in_pass and ratios is not None:
        verdict = "PASS"
        detail = (f"<d>/d_cont in [{ratios.min():.3f}, {ratios.max():.3f}] (within [0.5,2.0]). "
                  f"Rel var {rel_var*100:.1f}%. "
                  f"<d>(0)={mean_d[0]:.4f}, <d>(fold)={mean_d[fold_idx]:.4f}, "
                  f"<d>(0.35)={mean_d[-1]:.4f}. "
                  f"Triangle ineq: {violations} violations.")
    elif not varies:
        verdict = "FAIL"
        detail = f"Degenerate: rel var {rel_var*100:.4f}%."
    elif ratios is not None and not in_outer:
        verdict = "FAIL"
        detail = f"Ratio outside [0.1,10]: [{ratios.min():.3f}, {ratios.max():.3f}]."
    elif ratios is not None and not in_pass:
        verdict = "INFO"
        detail = (f"Ratio [{ratios.min():.3f}, {ratios.max():.3f}] in [0.1,10] "
                  f"but outside [0.5,2.0]. Rel var {rel_var*100:.1f}%.")
    else:
        verdict = "INFO"
        detail = f"No continuum data. Rel var {rel_var*100:.1f}%."

    print(f"Verdict: {verdict}")
    print(f"Detail:  {detail}")

    # ─── Save ────────────────────────────────────────────────────────────
    print("\n--- Saving ---")
    save = {
        'tau_values': tau_values,
        'tau_indices': np.array(tau_indices),
        'distances': all_dists_flat,
        'distance_matrix': all_dists_mat,
        'mean_distance': mean_d,
        'max_distance': max_d,
        'min_distance': min_d,
        'median_distance': med_d,
        'std_distance': std_d,
        'cell_labels': cell_labels,
        'cell_dims': cell_dims,
        'adjacency': adjacency,
        'N_cells': np.array(N),
        'n_pairs': np.array(n_pairs),
        'gate_name': np.array(['CONNES-LATT-54']),
        'gate_verdict': np.array([verdict]),
        'gate_detail': np.array([detail]),
    }
    if ratios is not None:
        save['ratios'] = ratios
        save['ratios_max'] = ratios_max
        save['d_continuum'] = d_cont
        save['d_continuum_mean'] = d_cont_mean

    np.savez(OUTPUT_NPZ, **save)
    print(f"Saved: {OUTPUT_NPZ}")

    # ─── Plot ────────────────────────────────────────────────────────────
    print("\n--- Plotting ---")
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'CONNES-LATT-54: Connes Distance on 32-Cell Graph  [{verdict}]',
                 fontsize=14, fontweight='bold')

    # Panel 1: Mean distance vs tau
    ax = axes[0, 0]
    ax.fill_between(tau_values, min_d, max_d, alpha=0.15, color='blue')
    ax.plot(tau_values, mean_d, 'b-o', lw=2, ms=6, label=r'$\langle d_D \rangle$')
    ax.plot(tau_values, med_d, 'b--', lw=1.5, alpha=0.7, label='median')
    if d_cont is not None:
        ax.plot(tau_values, d_cont_mean, 'r-s', lw=1.5, ms=5, alpha=0.8,
                label=r'$\bar{d}_{\rm cont}$ (S46 mean)')
        ax.plot(tau_values, d_cont, 'r--^', lw=1, ms=4, alpha=0.5,
                label=r'$d_{\rm cont}$ (S46 diam)')
    ax.axvline(0.19, color='gray', ls=':', alpha=0.7, label='fold')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Distance')
    ax.set_title(r'Connes Distance vs $\tau$')
    ax.legend(fontsize=7, loc='best')
    ax.grid(True, alpha=0.3)

    # Panel 2: Ratio
    ax = axes[0, 1]
    if ratios is not None:
        ax.plot(tau_values, ratios, 'g-o', lw=2, ms=6, label=r'$\langle d \rangle / \bar{d}_{\rm cont}$')
        ax.plot(tau_values, ratios_max, 'g--^', lw=1.5, ms=5, alpha=0.7,
                label=r'$d_{\rm max} / d_{\rm diam}$')
        ax.axhline(1.0, color='k', ls='-', alpha=0.3)
        ax.axhspan(0.5, 2.0, alpha=0.1, color='green', label='PASS range')
        ax.axvline(0.19, color='gray', ls=':', alpha=0.7)
        ax.legend(fontsize=8)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Ratio')
    ax.set_title('Lattice / Continuum Ratio')
    ax.grid(True, alpha=0.3)

    # Panel 3: Histograms
    ax = axes[1, 0]
    d0_flat = all_dists_flat[0]
    df_flat = all_dists_flat[fold_idx]
    de_flat = all_dists_flat[-1]
    d0_nz = d0_flat[d0_flat > 1e-15]
    df_nz = df_flat[df_flat > 1e-15]
    de_nz = de_flat[de_flat > 1e-15]
    bins = np.linspace(0, max(d0_nz.max(), df_nz.max(), de_nz.max()) * 1.05, 30)
    ax.hist(d0_nz, bins=bins, alpha=0.5, label=r'$\tau=0$', density=True, color='blue')
    ax.hist(df_nz, bins=bins, alpha=0.5,
            label=rf'$\tau={tau_values[fold_idx]:.2f}$', density=True, color='red')
    ax.hist(de_nz, bins=bins, alpha=0.5,
            label=rf'$\tau={tau_values[-1]:.2f}$', density=True, color='green')
    ax.set_xlabel('Connes distance')
    ax.set_ylabel('Density')
    ax.set_title('Distance Distribution')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: Distance matrix at fold
    ax = axes[1, 1]
    im = ax.imshow(all_dists_mat[fold_idx], cmap='viridis', aspect='equal')
    plt.colorbar(im, ax=ax, label='Connes distance')
    ax.set_xlabel('Cell index')
    ax.set_ylabel('Cell index')
    ax.set_title(rf'$d_D$ Matrix at fold ($\tau={tau_values[fold_idx]:.2f}$)')

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
    print(f"Saved: {OUTPUT_PNG}")

    # ─── Final summary ───────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"Gate: CONNES-LATT-54 -> {verdict}")
    print(f"<d_D>(tau=0.00)         = {mean_d[0]:.6f}")
    print(f"<d_D>(tau~{tau_values[fold_idx]:.2f}, fold) = {mean_d[fold_idx]:.6f}")
    print(f"<d_D>(tau=0.35)         = {mean_d[-1]:.6f}")
    print(f"Relative variation:       {rel_var*100:.2f}%")
    print(f"Monotone increasing:      {mono_inc}")
    print(f"Triangle inequality:      {'SATISFIED' if violations == 0 else f'{violations} violations'}")
    if ratios is not None:
        print(f"Ratio <d>/d_cont:         [{ratios.min():.4f}, {ratios.max():.4f}]")
    print(f"Total time:               {t_total:.1f}s")
    print(f"\nOutputs: {OUTPUT_NPZ}, {OUTPUT_PNG}")


if __name__ == '__main__':
    main()
