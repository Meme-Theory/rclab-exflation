#!/usr/bin/env python3
"""
S55 PHONON-DISP-55: Phonon Dispersion Classification on 32-Cell CG Lattice
===========================================================================

Extracts phonon dispersion from S54 tight-binding Hamiltonian data.
Classifies eigenstates by Z_2 conjugation parity, identifies acoustic vs
optical branches, and extracts effective sound velocity c_eff.

Gate: PHONON-DISP-55 (INFO)
Comparison: c_eff vs c_Gold = 0.915 M_KK (canonical_constants)

Data source: computations/session-54/s54_tb_hamiltonian.npz
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, 'computations')
from canonical_constants import c_Gold, tau_fold

# =============================================================================
# 1. Load S54 data
# =============================================================================
data = np.load('computations/session-54/s54_tb_hamiltonian.npz')
tau_values = data['tau_values']         # (50,)
eigenvalues = data['eigenvalues']       # (50, 32)
eigenvectors = data['eigenvectors']     # (50, 32, 32)
cell_labels = data['cell_labels']       # (32, 2) — (p,q)
cell_casimirs = data['cell_casimirs']   # (32,)
cell_dims = data['cell_dims']           # (32,)
adjacency = data['adjacency']           # (32, 32)
hamiltonians = data['hamiltonians']     # (50, 32, 32)

N_cells = int(data['N_cells'])
diameter = int(data['diameter'])
n_tau = len(tau_values)

print(f"Loaded: {N_cells} cells, {n_tau} tau values, diameter = {diameter}")
print(f"c_Gold (canonical) = {c_Gold:.4f} M_KK")
print(f"tau_fold = {tau_fold}")

# =============================================================================
# 2. Z_2 conjugation permutation: (p,q) -> (q,p)
# =============================================================================
perm_z2 = np.zeros(N_cells, dtype=int)
for i in range(N_cells):
    pi, qi = cell_labels[i]
    for j in range(N_cells):
        if cell_labels[j][0] == qi and cell_labels[j][1] == pi:
            perm_z2[i] = j
            break

# Self-conjugate cells (p = q)
self_conj = [i for i in range(N_cells) if perm_z2[i] == i]
conj_pairs = [(i, perm_z2[i]) for i in range(N_cells)
              if perm_z2[i] > i]
n_self_conj = len(self_conj)
n_conj_pairs = len(conj_pairs)
print(f"\nZ_2 structure: {n_self_conj} self-conjugate cells, {n_conj_pairs} conjugate pairs")
print(f"Self-conjugate: {[(cell_labels[i][0], cell_labels[i][1]) for i in self_conj]}")

# =============================================================================
# 3. Classify eigenstates at each tau by Z_2 parity
# =============================================================================
# For each (tau, eigenstate): compute overlap with Z_2-conjugated eigenvector
z2_parity = np.zeros((n_tau, N_cells))  # +1 = even, -1 = odd
z2_overlap = np.zeros((n_tau, N_cells))

for t_idx in range(n_tau):
    idx_sort = np.argsort(eigenvalues[t_idx])
    for rank in range(N_cells):
        ii = idx_sort[rank]
        v = eigenvectors[t_idx, :, ii]
        v_conj = v[perm_z2]
        overlap = np.dot(v, v_conj)
        z2_overlap[t_idx, rank] = overlap
        z2_parity[t_idx, rank] = 1.0 if overlap > 0 else -1.0

# Report at fold
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
tau_at_fold = tau_values[fold_idx]
n_even_fold = np.sum(z2_parity[fold_idx] > 0)
n_odd_fold = np.sum(z2_parity[fold_idx] < 0)
print(f"\nAt fold (tau = {tau_at_fold:.4f}):")
print(f"  Z_2 even: {int(n_even_fold)}, Z_2 odd: {int(n_odd_fold)}")
print(f"  Expected: {n_self_conj + n_conj_pairs} even, {n_conj_pairs} odd")

# =============================================================================
# 4. Z_2 parity stability across tau
# =============================================================================
# Check if Z_2 assignment is stable (no crossings that swap parity)
n_even_all = np.sum(z2_parity > 0, axis=1)
n_odd_all = np.sum(z2_parity < 0, axis=1)
parity_stable = np.all(n_even_all == n_even_all[0])
print(f"\nZ_2 count stable across all tau: {parity_stable}")
if not parity_stable:
    print(f"  Even count range: [{n_even_all.min()}, {n_even_all.max()}]")
    print(f"  Odd count range: [{n_odd_all.min()}, {n_odd_all.max()}]")

# =============================================================================
# 5. Branch classification: acoustic vs optical
# =============================================================================
# Sort eigenvalues at each tau
evals_sorted = np.sort(eigenvalues, axis=1)  # (50, 32)

# Acoustic branch: E_0 = 0 (zero mode, graph Laplacian property)
# Fiedler value E_1 = lowest nonzero eigenvalue = acoustic gap
fiedler_vals = evals_sorted[:, 1]

# Bandwidth
bandwidths = evals_sorted[:, -1]

# Acoustic fraction
acoustic_fraction = fiedler_vals / bandwidths

# Identify gaps in the spectrum to classify branches
# At fold, look for large gaps between consecutive eigenvalues
evals_fold_sorted = evals_sorted[fold_idx]
gaps = np.diff(evals_fold_sorted)
rel_gaps = gaps / (evals_fold_sorted[1:] + 1e-15)

print(f"\nSpectrum at fold (tau = {tau_at_fold:.4f}):")
print(f"  E_0 = {evals_fold_sorted[0]:.2e} (zero mode)")
print(f"  E_1 = {fiedler_vals[fold_idx]:.6f} M_KK (Fiedler / acoustic gap)")
print(f"  BW = {bandwidths[fold_idx]:.4f} M_KK")
print(f"  E_1/BW = {acoustic_fraction[fold_idx]:.6f}")

# Find significant gaps (> 2x median gap)
median_gap = np.median(gaps[1:])  # exclude gap at E_0
large_gap_idx = np.where(gaps > 2.0 * median_gap)[0]
print(f"\n  Median gap: {median_gap:.4f} M_KK")
print(f"  Large gaps (> 2x median) after eigenvalue index:")
for gi in large_gap_idx:
    print(f"    After E_{gi}: gap = {gaps[gi]:.4f} M_KK "
          f"({gaps[gi]/median_gap:.1f}x median), "
          f"E = [{evals_fold_sorted[gi]:.4f}, {evals_fold_sorted[gi+1]:.4f}]")

# =============================================================================
# 6. Effective sound velocity extraction
# =============================================================================
# Method 1: c_eff = E_1 / k_min where k_min = pi / D (D = graph diameter)
k_min = np.pi / diameter
c_eff_fiedler = fiedler_vals / k_min

# Method 2: Linear fit to first N_acoustic eigenvalues
# Assign k_n = n * k_min for n = 1, 2, ..., N_fit
# Fit E_n = c_fit * k_n to get c_fit
N_fit = min(6, N_cells - 1)  # first 6 non-zero levels
k_n = np.arange(1, N_fit + 1) * k_min
E_n_fold = evals_fold_sorted[1:N_fit + 1]
# Linear fit: E = c * k (no intercept)
c_fit_fold = np.sum(E_n_fold * k_n) / np.sum(k_n**2)
residuals = E_n_fold - c_fit_fold * k_n
rms_residual = np.sqrt(np.mean(residuals**2))

# Method 3: Group velocity from dE/dk at k -> 0
# Approximate: v_g = (E_2 - E_1) / (k_2 - k_1) = (E_2 - E_1) / k_min
v_group_fold = (evals_fold_sorted[2] - evals_fold_sorted[1]) / k_min

print(f"\nEffective sound velocity at fold:")
print(f"  Method 1 (Fiedler): c_eff = E_1/k_min = {c_eff_fiedler[fold_idx]:.6f} M_KK")
print(f"  Method 2 (linear fit, {N_fit} modes): c_fit = {c_fit_fold:.6f} M_KK, "
      f"RMS residual = {rms_residual:.4f}")
print(f"  Method 3 (group velocity): v_g = {v_group_fold:.6f} M_KK")

print(f"\nComparison to continuum:")
print(f"  c_Gold = {c_Gold:.4f} M_KK (canonical, S53 GL dispersion)")
print(f"  c_eff (Fiedler) / c_Gold = {c_eff_fiedler[fold_idx] / c_Gold:.4f}")
print(f"  c_fit (linear) / c_Gold = {c_fit_fold / c_Gold:.4f}")

# c_eff across tau
c_eff_all = c_eff_fiedler
print(f"\nc_eff(tau) range: [{c_eff_all.min():.4f}, {c_eff_all.max():.4f}] M_KK")
print(f"c_eff(tau) variation: {(c_eff_all.max() - c_eff_all.min()) / c_eff_all.mean() * 100:.1f}%")

# =============================================================================
# 7. Participation analysis: localized vs extended
# =============================================================================
# IPR and participation ratio at fold
ipr_fold = np.zeros(N_cells)
pr_fold = np.zeros(N_cells)
mean_c2_fold = np.zeros(N_cells)
dom_cell_fold = np.zeros(N_cells, dtype=int)
dom_c2_fold = np.zeros(N_cells)

idx_sort_fold = np.argsort(eigenvalues[fold_idx])
for rank in range(N_cells):
    ii = idx_sort_fold[rank]
    v = eigenvectors[fold_idx, :, ii]
    ipr_fold[rank] = np.sum(v**4)
    pr_fold[rank] = 1.0 / ipr_fold[rank]
    mean_c2_fold[rank] = np.sum(v**2 * cell_casimirs)
    dom_cell_fold[rank] = np.argmax(np.abs(v))
    dom_c2_fold[rank] = cell_casimirs[dom_cell_fold[rank]]

# Classify: extended (PR > N/3 ~ 10) vs localized
extended_threshold = N_cells / 3.0
n_extended = np.sum(pr_fold > extended_threshold)
n_localized = N_cells - n_extended

print(f"\nLocalization at fold:")
print(f"  PR range: [{pr_fold.min():.2f}, {pr_fold.max():.2f}]")
print(f"  Extended (PR > {extended_threshold:.1f}): {n_extended}")
print(f"  Localized (PR <= {extended_threshold:.1f}): {n_localized}")
print(f"  Mean PR: {pr_fold.mean():.2f}")

# =============================================================================
# 8. Eigenvalue scaling test: E_n ~ n^alpha
# =============================================================================
n_indices = np.arange(1, 11)  # first 10 nonzero levels
E_first10 = evals_fold_sorted[1:11]
# Fit log(E_n) = alpha * log(n) + const
log_n = np.log(n_indices)
log_E = np.log(E_first10)
alpha_fit, log_c = np.polyfit(log_n, log_E, 1)
print(f"\nPower-law fit E_n ~ n^alpha for first 10 modes:")
print(f"  alpha = {alpha_fit:.4f} (1.0 = acoustic/linear, 2.0 = diffusive)")

# =============================================================================
# 9. DOS (density of states) from eigenvalues
# =============================================================================
# Histogram of eigenvalues at fold
dos_bins = 50
E_range = (0, bandwidths[fold_idx] * 1.05)
dos_hist, dos_edges = np.histogram(evals_fold_sorted, bins=dos_bins, range=E_range)
dos_centers = 0.5 * (dos_edges[:-1] + dos_edges[1:])
dE = dos_edges[1] - dos_edges[0]
dos_normalized = dos_hist / (N_cells * dE)

# =============================================================================
# 10. PLOTTING
# =============================================================================
fig = plt.figure(figsize=(20, 16))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.35)

# --- Panel (a): Full spectrum E_n(tau) colored by Z_2 parity ---
ax1 = fig.add_subplot(gs[0, 0:2])
for rank in range(N_cells):
    # Track eigenvalue n across tau (using sorted order)
    E_track = np.sort(eigenvalues, axis=1)[:, rank]
    # Z_2 parity at fold determines color
    color = '#2166ac' if z2_parity[fold_idx, rank] > 0 else '#b2182b'
    lw = 1.5 if rank == 0 else 0.8  # (local)
    ax1.plot(tau_values, E_track, color=color, linewidth=lw, alpha=0.7)
ax1.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax1.set_xlabel(r'$\tau$', fontsize=12)
ax1.set_ylabel(r'$E_n$ [$M_{\rm KK}$]', fontsize=12)
ax1.set_title(r'(a) Full spectrum $E_n(\tau)$: Z$_2$ even (blue) / odd (red)', fontsize=13)
ax1.legend(fontsize=10)
ax1.set_xlim(0, 0.5)

# --- Panel (b): Low-energy zoom ---
ax2 = fig.add_subplot(gs[0, 2])
for rank in range(min(8, N_cells)):
    E_track = np.sort(eigenvalues, axis=1)[:, rank]
    color = '#2166ac' if z2_parity[fold_idx, rank] > 0 else '#b2182b'
    label = f'$E_{rank}$' if rank < 5 else None
    ax2.plot(tau_values, E_track, color=color, linewidth=1.5, label=label)
ax2.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax2.set_xlabel(r'$\tau$', fontsize=12)
ax2.set_ylabel(r'$E_n$ [$M_{\rm KK}$]', fontsize=12)
ax2.set_title(r'(b) Lowest 8 modes', fontsize=13)
ax2.legend(fontsize=8, loc='upper right')
ax2.set_xlim(0, 0.5)

# --- Panel (c): Dispersion E_n vs mode index at fold ---
ax3 = fig.add_subplot(gs[1, 0])
colors_z2 = ['#2166ac' if z2_parity[fold_idx, n] > 0 else '#b2182b'
             for n in range(N_cells)]
ax3.scatter(range(N_cells), evals_fold_sorted, c=colors_z2, s=40, zorder=3)
# Linear fit line
n_plot = np.arange(N_cells)
ax3.plot(n_plot[:N_fit+1], np.concatenate([[0], c_fit_fold * k_n]),
         'k--', alpha=0.5, label=f'Linear fit: $c_{{\\rm fit}}={c_fit_fold:.3f}$')
ax3.set_xlabel('Mode index $n$', fontsize=12)
ax3.set_ylabel(r'$E_n$ [$M_{\rm KK}$]', fontsize=12)
ax3.set_title(r'(c) Dispersion at $\tau_{\rm fold}$', fontsize=13)
ax3.legend(fontsize=10)

# --- Panel (d): E_n vs mean Casimir <C_2> ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.scatter(mean_c2_fold, evals_fold_sorted, c=colors_z2, s=40, zorder=3)
ax4.set_xlabel(r'$\langle C_2 \rangle$ of eigenstate', fontsize=12)
ax4.set_ylabel(r'$E_n$ [$M_{\rm KK}$]', fontsize=12)
ax4.set_title(r'(d) Energy vs mean Casimir at fold', fontsize=13)

# --- Panel (e): c_eff(tau) vs c_Gold ---
ax5 = fig.add_subplot(gs[1, 2])
ax5.plot(tau_values, c_eff_all, 'b-', linewidth=2, label=r'$c_{\rm eff}(\tau)$ (Fiedler)')
ax5.axhline(c_Gold, color='r', linestyle='--', linewidth=1.5,
            label=f'$c_{{\\rm Gold}}={c_Gold:.3f}$')
ax5.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax5.set_xlabel(r'$\tau$', fontsize=12)
ax5.set_ylabel(r'$c_{\rm eff}$ [$M_{\rm KK}$]', fontsize=12)
ax5.set_title(r'(e) Sound velocity: lattice vs continuum', fontsize=13)
ax5.legend(fontsize=10)
ax5.set_xlim(0, 0.5)

# --- Panel (f): Participation ratio vs E_n ---
ax6 = fig.add_subplot(gs[2, 0])
ax6.scatter(evals_fold_sorted, pr_fold, c=colors_z2, s=40, zorder=3)
ax6.axhline(extended_threshold, color='gray', linestyle=':', alpha=0.5,
            label=f'Extended threshold (PR={extended_threshold:.0f})')
ax6.set_xlabel(r'$E_n$ [$M_{\rm KK}$]', fontsize=12)
ax6.set_ylabel('Participation ratio', fontsize=12)
ax6.set_title(r'(f) Localization at fold', fontsize=13)
ax6.legend(fontsize=9)

# --- Panel (g): Z_2 overlap as bar chart ---
ax7 = fig.add_subplot(gs[2, 1])
z2_ov_fold = z2_overlap[fold_idx]
# Overlaps are exactly +1 or -1 — show as sorted bar chart by eigenvalue index
z2_colors_bar = ['#2166ac' if ov > 0 else '#b2182b' for ov in z2_ov_fold]
ax7.bar(range(N_cells), z2_ov_fold, color=z2_colors_bar, alpha=0.8)
ax7.axhline(0, color='k', linewidth=0.5)
ax7.set_xlabel('Eigenstate rank (by energy)', fontsize=12)
ax7.set_ylabel(r'$\langle \psi | C | \psi \rangle$', fontsize=12)
ax7.set_title(r'(g) Z$_2$ parity by eigenstate', fontsize=13)
ax7.set_ylim(-1.3, 1.3)
# Add legend manually
from matplotlib.patches import Patch
ax7.legend(handles=[Patch(facecolor='#2166ac', label=f'Even ({int(n_even_fold)})'),
                    Patch(facecolor='#b2182b', label=f'Odd ({int(n_odd_fold)})')],
           fontsize=10)

# --- Panel (h): DOS at fold ---
ax8 = fig.add_subplot(gs[2, 2])
ax8.bar(dos_centers, dos_normalized, width=dE * 0.9, color='#4393c3', alpha=0.7)
ax8.set_xlabel(r'$E$ [$M_{\rm KK}$]', fontsize=12)
ax8.set_ylabel(r'$\rho(E)$ [1/$M_{\rm KK}$]', fontsize=12)
ax8.set_title(r'(h) DOS at fold (32 cells)', fontsize=13)

fig.suptitle('PHONON-DISP-55: Phonon Dispersion on 32-Cell CG Lattice',
             fontsize=16, fontweight='bold', y=0.98)

plt.savefig('computations/session-55/s55_phonon_disp.png', dpi=150, bbox_inches='tight')
print("\nPlot saved: computations/session-55/s55_phonon_disp.png")

# =============================================================================
# 11. Power-law linearity test
# =============================================================================
# Test: E_n ~ n for acoustic (linear dispersion) vs E_n ~ n^2 (quadratic)
# Fit only first 4 modes (lowest acoustic branch)
n_acoustic = 4
n_idx_ac = np.arange(1, n_acoustic + 1)
E_ac = evals_fold_sorted[1:n_acoustic + 1]
log_n_ac = np.log(n_idx_ac)
log_E_ac = np.log(E_ac)
alpha_acoustic, _ = np.polyfit(log_n_ac, log_E_ac, 1)
print(f"\nAcoustic power law (first {n_acoustic} modes): alpha = {alpha_acoustic:.4f}")

# =============================================================================
# 12. Summary results
# =============================================================================
print("\n" + "=" * 70)
print("PHONON-DISP-55 SUMMARY")
print("=" * 70)
print(f"Gate: PHONON-DISP-55 — INFO")
print(f"")
print(f"Z_2 conjugation classification:")
print(f"  Even (symmetric under (p,q)->(q,p)): {int(n_even_fold)}")
print(f"  Odd (antisymmetric): {int(n_odd_fold)}")
print(f"  Parity stable across all tau: {parity_stable}")
print(f"  Self-conjugate cells: {n_self_conj}, Conjugate pairs: {n_conj_pairs}")
print(f"")
print(f"Branch structure:")
print(f"  E_0 = {evals_fold_sorted[0]:.2e} M_KK (zero mode / uniform phase)")
print(f"  E_1 = {fiedler_vals[fold_idx]:.6f} M_KK (Fiedler / acoustic gap)")
print(f"  E_max = {bandwidths[fold_idx]:.4f} M_KK (bandwidth)")
print(f"  E_1/BW = {acoustic_fraction[fold_idx]:.6f} (acoustic fraction)")
print(f"  Power-law exponent (first 4 modes): alpha = {alpha_acoustic:.3f}")
print(f"  Power-law exponent (first 10 modes): alpha = {alpha_fit:.3f}")
print(f"")
print(f"Effective sound velocity:")
print(f"  c_eff (Fiedler, k_min=pi/D): {c_eff_fiedler[fold_idx]:.6f} M_KK")
print(f"  c_eff (linear fit, {N_fit} modes): {c_fit_fold:.6f} M_KK")
print(f"  v_group (E_2-E_1): {v_group_fold:.6f} M_KK")
print(f"  c_Gold (canonical): {c_Gold:.4f} M_KK")
print(f"  c_eff/c_Gold (Fiedler): {c_eff_fiedler[fold_idx] / c_Gold:.4f}")
print(f"  c_eff/c_Gold (linear fit): {c_fit_fold / c_Gold:.4f}")
print(f"")
print(f"c_eff(tau) range: [{c_eff_all.min():.4f}, {c_eff_all.max():.4f}] M_KK")
print(f"c_eff(tau) variation: {(c_eff_all.max()-c_eff_all.min())/c_eff_all.mean()*100:.1f}%")
print(f"")
print(f"Localization:")
print(f"  PR range: [{pr_fold.min():.2f}, {pr_fold.max():.2f}]")
print(f"  Extended modes (PR > {extended_threshold:.0f}): {n_extended}/{N_cells}")
print(f"  Localized modes: {n_localized}/{N_cells}")
print(f"")
print(f"Large spectral gaps at fold (> 2x median):")
for gi in large_gap_idx:
    print(f"  After E_{gi}: {gaps[gi]:.4f} M_KK "
          f"({gaps[gi]/median_gap:.1f}x median)")

# =============================================================================
# 13. Save numerical results
# =============================================================================
np.savez('computations/session-55/s55_phonon_disp.npz',
         tau_values=tau_values,
         evals_sorted=evals_sorted,
         z2_parity=z2_parity,
         z2_overlap=z2_overlap,
         fiedler_vals=fiedler_vals,
         bandwidths=bandwidths,
         c_eff_fiedler=c_eff_fiedler,
         c_fit_fold=np.array([c_fit_fold]),
         v_group_fold=np.array([v_group_fold]),
         pr_fold=pr_fold,
         mean_c2_fold=mean_c2_fold,
         dom_cell_fold=dom_cell_fold,
         alpha_acoustic=np.array([alpha_acoustic]),
         alpha_fit_10=np.array([alpha_fit]),
         n_even_fold=np.array([n_even_fold]),
         n_odd_fold=np.array([n_odd_fold]),
         perm_z2=perm_z2,
         acoustic_fraction=acoustic_fraction,
         gate_name=np.array(['PHONON-DISP-55']),
         gate_verdict=np.array(['INFO']),
         )
print("\nData saved: computations/session-55/s55_phonon_disp.npz")
