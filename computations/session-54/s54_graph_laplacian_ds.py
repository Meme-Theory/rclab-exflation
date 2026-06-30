#!/usr/bin/env python3
"""
S54 W3-11: GRAPH-LAPLACIAN-DS-54
Spectral dimension d_s of the 32-cell Voronoi graph Laplacian.

The spectral dimension is defined via the return probability:
    P(t) = (1/N) Tr exp(-tL) = (1/N) sum_k exp(-t lambda_k)
    d_s(t) = -2 d log P(t) / d log t

For a finite graph:
  - t -> 0+: d_s approaches the graph's effective UV dimension
  - t -> infinity: d_s -> 0 (finite spectrum, gap-dominated)
  - Intermediate t: effective dimension at that scale

We compute d_s for:
  1. The unweighted graph Laplacian L = D - A (topology only)
  2. The weighted Hamiltonian H(tau) = sum_i J_i(tau) L_i (full physics)

NCG axiom 1 requires d_s = 8 for the continuum SU(3). The question is what
the 32-cell discretization gives.

Gate: GRAPH-LAPLACIAN-DS-54 (INFO)
"""

import numpy as np
from scipy.linalg import eigvalsh
import matplotlib.pyplot as plt
from pathlib import Path

# ── Load data ──────────────────────────────────────────────────────────────
data_path = Path(__file__).parent / "s54_tb_hamiltonian.npz"
data = np.load(data_path, allow_pickle=True)

adjacency = data['adjacency'].astype(float)
hamiltonians = data['hamiltonians']  # shape (50, 32, 32)
eigenvalues = data['eigenvalues']    # shape (50, 32) — pre-computed
tau_values = data['tau_values']
N_cells = int(data['N_cells'])

# ── 1. Unweighted graph Laplacian ─────────────────────────────────────────
D_unw = np.diag(adjacency.sum(axis=1))
L_unw = D_unw - adjacency
eigs_unw = np.sort(eigvalsh(L_unw))
print(f"Unweighted graph Laplacian eigenvalues (first 10):")
print(f"  {eigs_unw[:10]}")
print(f"  lambda_1 = {eigs_unw[1]:.6f} (spectral gap)")
print(f"  lambda_max = {eigs_unw[-1]:.6f}")

# ── 2. Heat trace and spectral dimension computation ──────────────────────
def compute_spectral_dimension(eigs, t_range, N):
    """
    Given eigenvalues of a Laplacian, compute the heat trace P(t) and
    spectral dimension d_s(t) = -2 d(log P)/d(log t).

    Uses the exact formula:
        P(t) = (1/N) sum_k exp(-t * lambda_k)
        d_s(t) = 2t * <lambda>_t / P(t)
    where <lambda>_t = (1/N) sum_k lambda_k exp(-t lambda_k).

    The second form avoids numerical differentiation.
    """
    t = t_range
    # Shape: (len(t), len(eigs))
    exponents = np.outer(-t, eigs)  # (n_t, n_eigs)
    exp_vals = np.exp(exponents)

    P = exp_vals.mean(axis=1)  # (1/N) Tr exp(-tL)

    # Analytic derivative: d P/dt = -(1/N) sum_k lambda_k exp(-t lambda_k)
    dPdt = -(exp_vals * eigs[np.newaxis, :]).mean(axis=1)

    # d_s = -2 * t * (dP/dt) / P = -2 * d(log P)/d(log t)
    ds = -2.0 * t * dPdt / P

    return P, ds

# Time range: logarithmic from very small to very large
t_range = np.logspace(-3, 3, 2000)

# ── 2a. Unweighted Laplacian ──────────────────────────────────────────────
P_unw, ds_unw = compute_spectral_dimension(eigs_unw, t_range, N_cells)

# Find plateau (most stable region = minimum |d(d_s)/d(log t)|)
log_t = np.log10(t_range)
dds_dlogt = np.gradient(ds_unw, log_t)
# Smooth to avoid noise
from scipy.ndimage import uniform_filter1d
dds_smooth = uniform_filter1d(np.abs(dds_dlogt), size=50)
# Find plateau in the middle range (avoid edges)
mid_mask = (log_t > -2) & (log_t < 2)
mid_indices = np.where(mid_mask)[0]
if len(mid_indices) > 0:
    plateau_idx = mid_indices[np.argmin(dds_smooth[mid_mask])]
else:
    plateau_idx = len(t_range) // 2

t_star_unw = t_range[plateau_idx]
ds_star_unw = ds_unw[plateau_idx]

print(f"\n── Unweighted Graph Laplacian ──")
print(f"d_s plateau at t* = {t_star_unw:.4f}: d_s = {ds_star_unw:.4f}")
print(f"d_s(t=0.001) = {ds_unw[0]:.4f} (UV)")
print(f"d_s(t=1000) = {ds_unw[-1]:.6f} (IR)")

# ── 2b. Weighted Hamiltonian at multiple tau ──────────────────────────────
# Key tau values: tau=0, fold (~0.19), tau=0.5
tau_indices = [0,
               np.argmin(np.abs(tau_values - 0.19)),
               np.argmin(np.abs(tau_values - 0.10)),
               np.argmin(np.abs(tau_values - 0.30)),
               -1]
tau_labels = []
ds_weighted = {}
P_weighted = {}
ds_plateau_weighted = {}

print(f"\n── Weighted Hamiltonian H(tau) = sum J_i(tau) L_i ──")
for idx in tau_indices:
    tau_val = tau_values[idx]
    eigs_w = eigenvalues[idx]  # pre-computed, already sorted
    label = f"tau={tau_val:.4f}"
    tau_labels.append(label)

    P_w, ds_w = compute_spectral_dimension(eigs_w, t_range, N_cells)
    P_weighted[label] = P_w
    ds_weighted[label] = ds_w

    # Find plateau
    dds_w = np.gradient(ds_w, log_t)
    dds_w_smooth = uniform_filter1d(np.abs(dds_w), size=50)
    if len(mid_indices) > 0:
        plat_idx = mid_indices[np.argmin(dds_w_smooth[mid_mask])]
    else:
        plat_idx = len(t_range) // 2

    t_star_w = t_range[plat_idx]
    ds_star_w = ds_w[plat_idx]
    ds_plateau_weighted[label] = (t_star_w, ds_star_w)

    print(f"  {label}: d_s(plateau) = {ds_star_w:.4f} at t* = {t_star_w:.4f}")
    print(f"    d_s(t=0.01) = {ds_w[np.argmin(np.abs(t_range-0.01))]:.4f}")
    print(f"    d_s(t=0.1)  = {ds_w[np.argmin(np.abs(t_range-0.1))]:.4f}")
    print(f"    d_s(t=1.0)  = {ds_w[np.argmin(np.abs(t_range-1.0))]:.4f}")
    print(f"    d_s(t=10)   = {ds_w[np.argmin(np.abs(t_range-10.0))]:.4f}")

# ── 2c. Sweep d_s at fixed t values across all tau ───────────────────────
t_probe_values = [0.01, 0.1, 0.5, 1.0, 5.0]
ds_sweep = {t_p: np.zeros(len(tau_values)) for t_p in t_probe_values}

for i_tau in range(len(tau_values)):
    eigs_i = eigenvalues[i_tau]
    for t_p in t_probe_values:
        exp_vals = np.exp(-t_p * eigs_i)
        P_val = exp_vals.mean()
        dPdt_val = -(eigs_i * exp_vals).mean()
        ds_sweep[t_p][i_tau] = -2.0 * t_p * dPdt_val / P_val

print(f"\n── d_s(tau) at fixed t values ──")
fold_idx = np.argmin(np.abs(tau_values - 0.19))
for t_p in t_probe_values:
    ds_at_fold = ds_sweep[t_p][fold_idx]
    ds_range = ds_sweep[t_p].max() - ds_sweep[t_p].min()
    print(f"  t={t_p:.2f}: d_s(fold) = {ds_at_fold:.4f}, "
          f"range [{ds_sweep[t_p].min():.4f}, {ds_sweep[t_p].max():.4f}], "
          f"variation = {ds_range:.4f}")

# ── 3. Weyl dimension comparison ─────────────────────────────────────────
# For a d-dimensional manifold, Weyl's law: N(lambda) ~ C * lambda^{d/2}
# On a finite graph with N nodes, the maximum eigenvalue count is N.
# The "Weyl dimension" can be estimated from the eigenvalue distribution.
# Fit log N(lambda) vs log lambda in the bulk.
eigs_fold = eigenvalues[fold_idx]
eigs_pos = eigs_fold[eigs_fold > 1e-10]
N_lambda = np.arange(1, len(eigs_pos) + 1)

# Fit in log-log
log_eigs = np.log(eigs_pos)
log_N = np.log(N_lambda)
# Use middle 60% to avoid edge effects
n_fit = len(eigs_pos)
i_lo = n_fit // 5
i_hi = 4 * n_fit // 5
if i_hi > i_lo + 2:
    coeffs = np.polyfit(log_eigs[i_lo:i_hi], log_N[i_lo:i_hi], 1)
    d_weyl_half = coeffs[0]  # slope = d/2
    d_weyl = 2 * d_weyl_half
else:
    d_weyl = np.nan

print(f"\n── Weyl Dimension Estimate ──")
print(f"d_Weyl/2 (slope) = {d_weyl_half:.4f}")
print(f"d_Weyl = {d_weyl:.4f}")

# ── 4. Maximum spectral dimension as UV proxy ────────────────────────────
# The true UV spectral dimension of a finite graph is limited.
# For random regular graphs, d_s -> infinity as t -> 0. For lattice
# graphs in d dimensions, d_s -> d. Our graph is neither.
# Report the maximum d_s achieved.
ds_max_unw = ds_unw.max()
t_max_unw = t_range[np.argmax(ds_unw)]
print(f"\n── Maximum Spectral Dimension ──")
print(f"Unweighted: max d_s = {ds_max_unw:.4f} at t = {t_max_unw:.4f}")

for label in tau_labels:
    ds_w = ds_weighted[label]
    ds_max_w = ds_w.max()
    t_max_w = t_range[np.argmax(ds_w)]
    print(f"{label}: max d_s = {ds_max_w:.4f} at t = {t_max_w:.4f}")

# ── 5. Graph-theoretic dimension estimates ────────────────────────────────
# Hausdorff dimension from shortest-path scaling
# d_H ~ log(N) / log(diameter)
diameter = int(data['diameter'])
d_hausdorff = np.log(N_cells) / np.log(diameter)
print(f"\n── Graph-Theoretic Dimensions ──")
print(f"N = {N_cells}, diameter = {diameter}")
print(f"d_Hausdorff (graph) = log({N_cells})/log({diameter}) = {d_hausdorff:.4f}")

# Average degree
avg_degree = adjacency.sum() / N_cells
print(f"Average degree = {avg_degree:.2f}")

# ── 6. Comparison summary ────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"COMPARISON SUMMARY")
print(f"{'='*60}")
print(f"Continuum SU(3):           d_s = 8")
print(f"S53 W3-10 GL bands:        d_s = 1.652")
print(f"Graph Hausdorff:           d_H = {d_hausdorff:.3f}")
print(f"Weyl fit (fold):           d_W = {d_weyl:.3f}")
print(f"Unweighted Laplacian:      max d_s = {ds_max_unw:.3f}")
fold_label = [l for l in tau_labels if '0.19' in l][0]
ds_fold = ds_weighted[fold_label]
print(f"Weighted H (fold):         max d_s = {ds_fold.max():.3f}")
print(f"Weighted H (fold):         d_s(plateau) = {ds_plateau_weighted[fold_label][1]:.3f}")
print(f"{'='*60}")

# ── PLOTTING ──────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("GRAPH-LAPLACIAN-DS-54: Spectral Dimension of 32-Cell Voronoi Graph",
             fontsize=13, fontweight='bold')

# Panel (a): d_s(t) for unweighted and weighted at key tau
ax = axes[0, 0]
ax.semilogx(t_range, ds_unw, 'k-', linewidth=2, label='Unweighted L', alpha=0.7)
colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(tau_labels)))
for i, label in enumerate(tau_labels):
    ax.semilogx(t_range, ds_weighted[label], '-', color=colors[i],
                linewidth=1.5, label=f'H({label})')
ax.axhline(y=8, color='red', linestyle='--', linewidth=1, alpha=0.5, label='d=8 (SU(3))')
ax.axhline(y=d_hausdorff, color='blue', linestyle=':', linewidth=1, alpha=0.5,
           label=f'd_H={d_hausdorff:.2f}')
ax.set_xlabel('t (diffusion time)', fontsize=11)
ax.set_ylabel('d_s(t)', fontsize=11)
ax.set_title('(a) Spectral Dimension vs Diffusion Time', fontsize=11)
ax.legend(fontsize=7, loc='upper right')
ax.set_ylim(-0.5, 10)
ax.set_xlim(1e-3, 1e3)
ax.grid(True, alpha=0.3)

# Panel (b): d_s(tau) at fixed probe times
ax = axes[0, 1]
probe_colors = plt.cm.plasma(np.linspace(0.1, 0.9, len(t_probe_values)))
for i, t_p in enumerate(t_probe_values):
    ax.plot(tau_values, ds_sweep[t_p], '-', color=probe_colors[i],
            linewidth=1.5, label=f't={t_p}')
ax.axhline(y=8, color='red', linestyle='--', linewidth=1, alpha=0.5)
ax.axvline(x=0.19, color='gray', linestyle=':', linewidth=1, alpha=0.5, label='fold')
ax.set_xlabel('tau (Jensen parameter)', fontsize=11)
ax.set_ylabel('d_s(tau; t_probe)', fontsize=11)
ax.set_title('(b) Spectral Dimension vs tau at Fixed t', fontsize=11)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Heat trace P(t) comparison
ax = axes[1, 0]
ax.loglog(t_range, P_unw, 'k-', linewidth=2, label='Unweighted', alpha=0.7)
for i, label in enumerate(tau_labels):
    ax.loglog(t_range, P_weighted[label], '-', color=colors[i], linewidth=1.5,
              label=f'H({label})')
# Reference: P ~ t^{-d/2} for d=8
t_ref = t_range[(t_range > 0.01) & (t_range < 0.3)]
P_ref = 0.5 * t_ref**(-4)  # d/2 = 4
ax.loglog(t_ref, P_ref, 'r--', linewidth=1, alpha=0.5, label='t^{-4} (d=8)')
ax.set_xlabel('t', fontsize=11)
ax.set_ylabel('P(t) = (1/N) Tr exp(-tL)', fontsize=11)
ax.set_title('(c) Heat Trace (Return Probability)', fontsize=11)
ax.legend(fontsize=7, loc='lower left')
ax.grid(True, alpha=0.3)

# Panel (d): Weyl counting function
ax = axes[1, 1]
for idx_w in [0, fold_idx, -1]:
    tau_w = tau_values[idx_w]
    eigs_w = eigenvalues[idx_w]
    eigs_pos_w = eigs_w[eigs_w > 1e-10]
    N_w = np.arange(1, len(eigs_pos_w) + 1)
    ax.loglog(eigs_pos_w, N_w, 'o-', markersize=3, linewidth=1.5,
              label=f'tau={tau_w:.3f}')

# Reference slopes
lam_ref = np.logspace(-0.5, 1.2, 50)
ax.loglog(lam_ref, 0.5 * lam_ref**(d_weyl/2), 'r--', linewidth=1, alpha=0.5,
          label=f'd_W={d_weyl:.1f} fit')
ax.loglog(lam_ref, 0.02 * lam_ref**4, 'b:', linewidth=1, alpha=0.5,
          label='d=8 ref')
ax.set_xlabel('lambda (eigenvalue)', fontsize=11)
ax.set_ylabel('N(lambda) (counting function)', fontsize=11)
ax.set_title('(d) Eigenvalue Counting Function', fontsize=11)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(str(Path(__file__).parent / "s54_graph_laplacian_ds.png"), dpi=150,
            bbox_inches='tight')
plt.close()
print(f"\nPlot saved to s54_graph_laplacian_ds.png")

# ── Save results ──────────────────────────────────────────────────────────
results = {
    'tau_values': tau_values,
    't_range': t_range,
    'ds_unweighted': ds_unw,
    'P_unweighted': P_unw,
    'eigs_unweighted': eigs_unw,
    'ds_max_unweighted': ds_max_unw,
    't_max_unweighted': t_max_unw,
    'ds_plateau_unweighted': ds_star_unw,
    't_plateau_unweighted': t_star_unw,
    'd_hausdorff': d_hausdorff,
    'd_weyl': d_weyl,
    'diameter': diameter,
    'N_cells': N_cells,
}

# Add weighted results
for label in tau_labels:
    safe = label.replace('=', '').replace('.', 'p')
    results[f'ds_{safe}'] = ds_weighted[label]
    results[f'P_{safe}'] = P_weighted[label]
    t_s, ds_s = ds_plateau_weighted[label]
    results[f'ds_plateau_{safe}'] = ds_s
    results[f't_plateau_{safe}'] = t_s

# Add sweep data
for t_p in t_probe_values:
    key = f'ds_sweep_t{str(t_p).replace(".", "p")}'
    results[key] = ds_sweep[t_p]

np.savez(str(Path(__file__).parent / "s54_graph_laplacian_ds.npz"), **results)
print("Results saved to s54_graph_laplacian_ds.npz")
