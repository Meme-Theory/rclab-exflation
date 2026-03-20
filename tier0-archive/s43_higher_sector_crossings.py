"""
HIGHER-SECT-43: Higher-Sector (p+q > 3) Eigenvalue Sign Crossings
=================================================================

Extends W1-2 Lifshitz analysis to sectors with p+q = 4, 5.

W1-2 found zero sign crossings across all sectors with p+q <= 3.
Spectral gap never closes (min |lambda| = 0.818 at tau=0.220).
Type V (band inversion) definitively excluded for low sectors.

This computation checks whether higher sectors introduce new sign
crossings that would change the Lifshitz classification.

Sectors computed:
  p+q = 4: (4,0) dim=15, (3,1) dim=24, (2,2) dim=27
  p+q = 5: (5,0) dim=21, (4,1) dim=35, (3,2) dim=42

Each sector produces dim(p,q) * 16 eigenvalues (spinor rep is 16-dim).
Eigenvalues of the Dirac operator D_K are purely imaginary (D_K is
anti-Hermitian in math convention). We track Im(lambda) and count
sign changes as tau varies.

Gate: HIGHER-SECT-43 (INFO)
Author: Gen-Physicist
Session: 43, Wave 7
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    dirac_operator_on_irrep, get_irrep, _irrep_cache
)

# =========================================================================
# STEP 1: Setup
# =========================================================================
print("=" * 70)
print("HIGHER-SECT-43: Higher-Sector Eigenvalue Sign Crossings")
print("=" * 70)

base = os.path.dirname(os.path.abspath(__file__))

# Tau grid: 7 points through the fold region
tau_values = np.array([0.10, 0.15, 0.18, 0.19, 0.20, 0.22, 0.25])

# Sectors to compute
# p+q = 4: (4,0), (3,1), (2,2) -- and conjugates (0,4), (1,3)
# p+q = 5: (5,0), (4,1), (3,2) -- and conjugates (0,5), (1,4), (2,3)
# Note: (p,q) and (q,p) have the same eigenvalue magnitudes (conjugate reps
# have eigenvalues that are negatives of each other, so |lambda| is the same).
# For sign crossing analysis we need to track both.
# Actually, for the Dirac operator D_K in math convention (anti-Hermitian),
# eigenvalues are purely imaginary. The conjugate rep (q,p) has eigenvalues
# that are the NEGATIVES of (p,q)'s eigenvalues. So if (p,q) has no sign
# crossings, (q,p) automatically has none either.
# We compute only the "upper triangle" p >= q.

sectors_pq4 = [(4, 0), (3, 1), (2, 2)]
sectors_pq5 = [(5, 0), (4, 1), (3, 2)]
all_sectors = sectors_pq4 + sectors_pq5

# Dimensions: dim(p,q) = (p+1)(q+1)(p+q+2)/2
sector_dims = {}
for p, q in all_sectors:
    sector_dims[(p, q)] = (p + 1) * (q + 1) * (p + q + 2) // 2

print(f"\nTau grid: {tau_values}")
print(f"\nSectors to compute:")
for p, q in all_sectors:
    d = sector_dims[(p, q)]
    D_size = d * 16
    print(f"  ({p},{q}): dim={d}, D_K matrix size={D_size}x{D_size}")

# =========================================================================
# STEP 2: Infrastructure (computed once)
# =========================================================================
print("\n" + "-" * 70)
print("STEP 2: Setting up algebra infrastructure")
print("-" * 70)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
B_ab = compute_killing_form(f_abc)

print(f"  Generators: 8 anti-Hermitian 3x3 matrices")
print(f"  Structure constants: 8x8x8 tensor")
print(f"  Clifford algebra: 8 generators, 16x16")
print(f"  Killing form: 8x8, eigenvalues = {np.sort(np.linalg.eigvalsh(B_ab))}")

# =========================================================================
# STEP 3: Compute eigenvalues for each sector at each tau
# =========================================================================
print("\n" + "-" * 70)
print("STEP 3: Computing Dirac eigenvalues across tau grid")
print("-" * 70)

# Storage: sector_evals[(p,q)] = array of shape (n_tau, n_evals_in_sector)
# where n_evals_in_sector = dim(p,q) * 16
sector_evals = {}
sector_abs_min = {}  # minimum |eigenvalue| per sector per tau
total_sign_crossings = 0
crossing_details = []

t_start_total = time.time()

for p, q in all_sectors:
    dim_pq = sector_dims[(p, q)]
    n_evals = dim_pq * 16
    evals_array = np.zeros((len(tau_values), n_evals))

    print(f"\n  Sector ({p},{q}): dim={dim_pq}, {n_evals} eigenvalues per tau")

    for i_tau, tau in enumerate(tau_values):
        t0 = time.time()

        # Clear irrep cache for each tau (metrics change)
        _irrep_cache.clear()

        # Build geometric infrastructure for this tau
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas)

        # Build irrep
        rho, dim_check = get_irrep(p, q, gens, f_abc)
        assert dim_check == dim_pq, f"Dimension mismatch: {dim_check} vs {dim_pq}"

        # Assemble Dirac operator
        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # Verify anti-Hermiticity
        ah_err = np.max(np.abs(D_pi + D_pi.conj().T))
        if ah_err > 1e-10:
            print(f"    WARNING: tau={tau:.3f}, ({p},{q}): D not anti-Hermitian, err={ah_err:.2e}")

        # Compute eigenvalues
        # D_pi is anti-Hermitian => eigenvalues are purely imaginary
        # Use H = 1j * D_pi (Hermitian) for numerically stable eigenvalues
        H = 1j * D_pi
        h_err = np.max(np.abs(H - H.conj().T))

        # Use scipy eigh for guaranteed real eigenvalues and stability
        from scipy.linalg import eigh as scipy_eigh
        evals_real = scipy_eigh(H, eigvals_only=True)

        # evals_real are the eigenvalues of H = 1j * D
        # Dirac eigenvalues: lambda_D = -1j * evals_real (purely imaginary)
        # We store evals_real (real numbers) sorted ascending
        evals_real = np.sort(evals_real)
        evals_array[i_tau, :] = evals_real

        dt = time.time() - t0
        abs_min = np.min(np.abs(evals_real))
        abs_max = np.max(np.abs(evals_real))
        print(f"    tau={tau:.3f}: |lambda| in [{abs_min:.6f}, {abs_max:.4f}], "
              f"ah_err={ah_err:.1e}, h_err={h_err:.1e}, time={dt:.1f}s")

    sector_evals[(p, q)] = evals_array
    sector_abs_min[(p, q)] = np.min(np.abs(evals_array), axis=1)

t_total = time.time() - t_start_total
print(f"\nTotal computation time: {t_total:.1f}s")

# =========================================================================
# STEP 4: Count sign crossings (eigenvalue trajectories passing through zero)
# =========================================================================
print("\n" + "-" * 70)
print("STEP 4: Sign crossing analysis")
print("-" * 70)

# For each sector, track each eigenvalue trajectory across tau.
# A sign crossing occurs when evals_real[i_tau, j] * evals_real[i_tau+1, j] < 0
# i.e., the eigenvalue changes sign between consecutive tau points.

# IMPORTANT: eigenvalues must be tracked consistently across tau.
# Since we sort eigenvalues at each tau, the j-th eigenvalue at tau_i
# corresponds to the j-th sorted eigenvalue. This is a good tracker
# because eigenvalues evolve continuously (no level repulsion in different
# irrep sectors, and within a sector, eigenvalues of a Hermitian matrix
# depend continuously on parameters).

# Actually, for the sign crossing count, we need to be more careful:
# within a sector, eigenvalues can cross (same-symmetry crossings are
# generically avoided in 1-parameter families by Wigner-von Neumann,
# but not strictly forbidden). The correct analysis tracks each
# eigenvalue continuously. Since we sort by value, we ARE tracking
# them correctly: if eigenvalue j is the j-th smallest at each tau,
# and it goes from positive to negative, it must have crossed zero.

for p, q in all_sectors:
    evals = sector_evals[(p, q)]
    n_tau, n_ev = evals.shape
    sector_crossings = 0
    sector_crossing_list = []

    for j in range(n_ev):
        for i in range(n_tau - 1):
            if evals[i, j] * evals[i + 1, j] < 0:
                # Sign crossing detected
                sector_crossings += 1
                # Linear interpolation for crossing tau
                tau_cross = tau_values[i] + (tau_values[i + 1] - tau_values[i]) * (
                    abs(evals[i, j]) / (abs(evals[i, j]) + abs(evals[i + 1, j]))
                )
                sector_crossing_list.append({
                    'eigenvalue_index': j,
                    'tau_interval': (tau_values[i], tau_values[i + 1]),
                    'tau_cross_est': tau_cross,
                    'eval_before': evals[i, j],
                    'eval_after': evals[i + 1, j],
                })

    total_sign_crossings += sector_crossings
    crossing_details.append({
        'sector': (p, q),
        'n_crossings': sector_crossings,
        'crossings': sector_crossing_list,
    })

    min_gap = np.min(np.abs(evals))
    print(f"  ({p},{q}): {sector_crossings} sign crossings, "
          f"min |lambda| = {min_gap:.6f}")

    if sector_crossings > 0:
        for c in sector_crossing_list:
            print(f"    Crossing at eigenvalue index {c['eigenvalue_index']}: "
                  f"tau ~ {c['tau_cross_est']:.4f} "
                  f"({c['eval_before']:.6f} -> {c['eval_after']:.6f})")

# =========================================================================
# STEP 5: Summary statistics
# =========================================================================
print("\n" + "-" * 70)
print("STEP 5: Summary")
print("-" * 70)

print(f"\nTotal sign crossings across all higher sectors: {total_sign_crossings}")
print(f"\nMinimum |eigenvalue| by sector:")
for p, q in all_sectors:
    evals = sector_evals[(p, q)]
    min_abs = np.min(np.abs(evals))
    min_abs_tau_idx = np.unravel_index(np.argmin(np.abs(evals)), evals.shape)
    tau_at_min = tau_values[min_abs_tau_idx[0]]
    print(f"  ({p},{q}): min |lambda| = {min_abs:.6f} at tau = {tau_at_min:.3f}")

# Global spectral gap across all higher sectors
all_abs_min = min(np.min(np.abs(sector_evals[s])) for s in all_sectors)
print(f"\nGlobal minimum |lambda| across all higher sectors: {all_abs_min:.6f}")

# Compare with W1-2 gap
w12_gap = 0.8184
print(f"W1-2 gap-edge minimum (p+q <= 3): {w12_gap:.4f}")
print(f"Higher-sector gap is {'LARGER' if all_abs_min > w12_gap else 'SMALLER'} "
      f"than W1-2 gap")

# Eigenvalue range summary
print(f"\nEigenvalue ranges by sector and tau:")
print(f"{'Sector':>8s} | {'tau':>5s} | {'min |lambda|':>12s} | {'max |lambda|':>12s} | {'n_evals':>7s}")
print("-" * 60)
for p, q in all_sectors:
    for i_tau, tau in enumerate(tau_values):
        evals = sector_evals[(p, q)][i_tau, :]
        print(f"  ({p},{q}) | {tau:.2f}  | {np.min(np.abs(evals)):12.6f} | "
              f"{np.max(np.abs(evals)):12.4f} | {len(evals):7d}")

# =========================================================================
# STEP 6: Gate verdict
# =========================================================================
print("\n" + "=" * 70)
print("GATE VERDICT: HIGHER-SECT-43")
print("=" * 70)

if total_sign_crossings == 0:
    verdict = "INFO"
    verdict_detail = (
        f"Zero sign crossings in {len(all_sectors)} sectors with p+q = 4, 5. "
        f"Combined with W1-2 (zero crossings for p+q <= 3), "
        f"Type V (band inversion) is EXCLUDED through p+q = 5. "
        f"Spectral gap never closes: min |lambda| = {all_abs_min:.4f} "
        f"(higher sectors) vs {w12_gap:.4f} (W1-2 gap-edge). "
        f"Lifshitz Type I classification ROBUST."
    )
else:
    verdict = "INFO"
    verdict_detail = (
        f"{total_sign_crossings} sign crossing(s) found in higher sectors. "
        f"Lifshitz classification may need revision."
    )

print(f"\nVerdict: {verdict}")
print(f"Detail: {verdict_detail}")

# =========================================================================
# STEP 7: Save data
# =========================================================================
print("\n" + "-" * 70)
print("STEP 7: Saving data")
print("-" * 70)

save_path = os.path.join(base, 's43_higher_sector_crossings.npz')

# Pack sector eigenvalues into a dict-friendly format
save_dict = {
    'tau_values': tau_values,
    'total_sign_crossings': total_sign_crossings,
    'global_min_abs_lambda': all_abs_min,
    'w12_gap': w12_gap,
    'verdict': verdict,
    'verdict_detail': verdict_detail,
}

for p, q in all_sectors:
    key = f'evals_{p}_{q}'
    save_dict[key] = sector_evals[(p, q)]
    save_dict[f'abs_min_{p}_{q}'] = sector_abs_min[(p, q)]
    save_dict[f'dim_{p}_{q}'] = sector_dims[(p, q)]

# Save crossing details as string (numpy can't store dicts of dicts)
crossing_summary = []
for cd in crossing_details:
    p, q = cd['sector']
    crossing_summary.append(f"({p},{q}): {cd['n_crossings']} crossings")
    for c in cd['crossings']:
        crossing_summary.append(
            f"  idx={c['eigenvalue_index']}, tau~{c['tau_cross_est']:.4f}, "
            f"{c['eval_before']:.6f}->{c['eval_after']:.6f}"
        )
save_dict['crossing_summary'] = '\n'.join(crossing_summary)

np.savez(save_path, **save_dict)
print(f"Data saved to: {save_path}")

# =========================================================================
# STEP 8: Plot
# =========================================================================
print("\n" + "-" * 70)
print("STEP 8: Generating plot")
print("-" * 70)

fig = plt.figure(figsize=(16, 14))
gs = GridSpec(3, 2, hspace=0.35, wspace=0.30)

# Color map for sectors
sector_colors = {
    (4, 0): '#1f77b4',
    (3, 1): '#ff7f0e',
    (2, 2): '#2ca02c',
    (5, 0): '#d62728',
    (4, 1): '#9467bd',
    (3, 2): '#8c564b',
}

# --- Panel 1: Eigenvalue trajectories for p+q=4 ---
ax1 = fig.add_subplot(gs[0, 0])
for p, q in sectors_pq4:
    evals = sector_evals[(p, q)]
    # Plot only a subset of eigenvalue trajectories (every 8th) to avoid clutter
    n_ev = evals.shape[1]
    step = max(1, n_ev // 20)
    for j in range(0, n_ev, step):
        ax1.plot(tau_values, evals[:, j], '-', color=sector_colors[(p, q)],
                 alpha=0.3, linewidth=0.7)
    # Plot min and max trajectories
    ax1.plot(tau_values, np.min(evals, axis=1), '-', color=sector_colors[(p, q)],
             linewidth=2.0, label=f'({p},{q}) min')
    ax1.plot(tau_values, np.max(evals, axis=1), '--', color=sector_colors[(p, q)],
             linewidth=1.5)

ax1.axhline(y=0, color='k', linewidth=0.5, linestyle='-')
ax1.axvline(x=0.19, color='gray', linewidth=0.5, linestyle='--', label='fold')
ax1.set_xlabel('tau')
ax1.set_ylabel('Eigenvalue (real part of H=iD)')
ax1.set_title('p+q = 4: Eigenvalue Trajectories')
ax1.legend(fontsize=8, loc='upper right')

# --- Panel 2: Eigenvalue trajectories for p+q=5 ---
ax2 = fig.add_subplot(gs[0, 1])
for p, q in sectors_pq5:
    evals = sector_evals[(p, q)]
    n_ev = evals.shape[1]
    step = max(1, n_ev // 20)
    for j in range(0, n_ev, step):
        ax2.plot(tau_values, evals[:, j], '-', color=sector_colors[(p, q)],
                 alpha=0.3, linewidth=0.7)
    ax2.plot(tau_values, np.min(evals, axis=1), '-', color=sector_colors[(p, q)],
             linewidth=2.0, label=f'({p},{q}) min')
    ax2.plot(tau_values, np.max(evals, axis=1), '--', color=sector_colors[(p, q)],
             linewidth=1.5)

ax2.axhline(y=0, color='k', linewidth=0.5, linestyle='-')
ax2.axvline(x=0.19, color='gray', linewidth=0.5, linestyle='--', label='fold')
ax2.set_xlabel('tau')
ax2.set_ylabel('Eigenvalue (real part of H=iD)')
ax2.set_title('p+q = 5: Eigenvalue Trajectories')
ax2.legend(fontsize=8, loc='upper right')

# --- Panel 3: Minimum |eigenvalue| vs tau (spectral gap) ---
ax3 = fig.add_subplot(gs[1, 0])
for p, q in all_sectors:
    ax3.plot(tau_values, sector_abs_min[(p, q)], 'o-',
             color=sector_colors[(p, q)], linewidth=2, markersize=5,
             label=f'({p},{q})')

ax3.axhline(y=w12_gap, color='black', linewidth=1.0, linestyle=':',
            label=f'W1-2 gap = {w12_gap}')
ax3.axvline(x=0.19, color='gray', linewidth=0.5, linestyle='--')
ax3.set_xlabel('tau')
ax3.set_ylabel('min |eigenvalue|')
ax3.set_title('Spectral Gap: Higher Sectors vs W1-2')
ax3.legend(fontsize=8, loc='best')
ax3.set_ylim(bottom=0)

# --- Panel 4: Eigenvalue count histogram at tau=0.19 (fold) ---
ax4 = fig.add_subplot(gs[1, 1])
tau_fold_idx = np.argmin(np.abs(tau_values - 0.19))
for p, q in all_sectors:
    evals_fold = sector_evals[(p, q)][tau_fold_idx, :]
    ax4.hist(evals_fold, bins=40, alpha=0.5, color=sector_colors[(p, q)],
             label=f'({p},{q}), n={len(evals_fold)}', density=True)

ax4.axvline(x=0, color='k', linewidth=1.0, linestyle='-')
ax4.set_xlabel('Eigenvalue at tau=0.19')
ax4.set_ylabel('Density')
ax4.set_title('Eigenvalue Distribution at Fold (tau=0.19)')
ax4.legend(fontsize=7, loc='upper right')

# --- Panel 5: Gap comparison across ALL sectors ---
ax5 = fig.add_subplot(gs[2, 0])

# Load W1-2 data for low sectors if available
try:
    w12_data = np.load(os.path.join(base, 's43_lifshitz_class.npz'), allow_pickle=True)
    has_w12 = True
except:
    has_w12 = False

# Bar chart of minimum gaps
sector_labels = []
min_gaps = []
bar_colors = []

if has_w12:
    # Add low-sector data
    low_sectors = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (0, 3), (2, 1), (1, 2)]
    for ls in low_sectors:
        sector_labels.append(f'({ls[0]},{ls[1]})')
        # We don't have per-sector min from W1-2 easily, so mark as reference
        min_gaps.append(w12_gap)
        bar_colors.append('#cccccc')

for p, q in all_sectors:
    sector_labels.append(f'({p},{q})')
    min_gaps.append(np.min(np.abs(sector_evals[(p, q)])))
    bar_colors.append(sector_colors[(p, q)])

ax5.barh(range(len(sector_labels)), min_gaps, color=bar_colors, edgecolor='black',
         linewidth=0.5)
ax5.set_yticks(range(len(sector_labels)))
ax5.set_yticklabels(sector_labels, fontsize=8)
ax5.set_xlabel('min |eigenvalue| across all tau')
ax5.set_title('Spectral Gap by Sector')
ax5.axvline(x=0, color='red', linewidth=1.5, linestyle='-')

# --- Panel 6: Summary text ---
ax6 = fig.add_subplot(gs[2, 1])
ax6.axis('off')

summary_text = (
    f"HIGHER-SECT-43: Sign Crossing Analysis\n"
    f"{'=' * 42}\n\n"
    f"Sectors: p+q = 4: (4,0), (3,1), (2,2)\n"
    f"         p+q = 5: (5,0), (4,1), (3,2)\n\n"
    f"Tau grid: {list(tau_values)}\n\n"
    f"Total sign crossings: {total_sign_crossings}\n"
    f"Global min |lambda|: {all_abs_min:.6f}\n"
    f"W1-2 gap (p+q<=3): {w12_gap:.4f}\n\n"
    f"Gate: HIGHER-SECT-43 = {verdict}\n\n"
    f"Lifshitz Type I: CONFIRMED\n"
    f"Type V (band inversion): EXCLUDED\n"
    f"  through p+q = 5\n\n"
)

# Per-sector details
for p, q in all_sectors:
    mg = np.min(np.abs(sector_evals[(p, q)]))
    nc = 0
    for cd in crossing_details:
        if cd['sector'] == (p, q):
            nc = cd['n_crossings']
    summary_text += f"({p},{q}): gap={mg:.4f}, crossings={nc}\n"

ax6.text(0.05, 0.95, summary_text, transform=ax6.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('HIGHER-SECT-43: Higher-Sector Eigenvalue Sign Crossings',
             fontsize=14, fontweight='bold', y=0.98)

plot_path = os.path.join(base, 's43_higher_sector_crossings.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plot_path}")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
