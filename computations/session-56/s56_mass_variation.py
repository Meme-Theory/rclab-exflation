#!/usr/bin/env python3
"""
S56 MASS-VARIATION-56 -- Paper 16 Eq 7.1 Mass Variation Integral
================================================================

Compute dm_k/dtau for each eigenvalue along the Jensen transit,
using central finite differences. This is a purely geometric
expansion diagnostic: mass change from the Jensen deformation alone.

Paper 16 (Baptista 2025), Eq 7.1:
    c^2 d(m^2)/ds = - (d_A g_K)_{\dot{M}} (p_V, p_V)

In the tight-binding discretization, E_k(tau) plays the role of
the k-th KK mass eigenvalue. The Jensen deformation parameter tau
replaces the geodesic parameter s (the internal geometry changes
along tau, producing mass variation via the second fundamental
form of the fibres).

Computation:
    1. Load eigenvalues E_k(tau) from s54_tb_hamiltonian.npz
    2. Central differences: dE_k/dtau = (E_k(tau+dtau) - E_k(tau-dtau))/(2*dtau)
    3. Total: M_total(tau) = Sum_k E_k(tau), dM_total/dtau
    4. Spectral weight: W(tau) = Sum_k E_k^2(tau), dW/dtau
    5. Mode-by-mode sign analysis at the fold

Gate: MASS-VARIATION-56 (INFO)
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, 'computations')
from canonical_constants import tau_fold, M_KK, N_cells

# ============================================================
#  1. Load data
# ============================================================
data = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
tau_values = data['tau_values']       # (50,)
eigenvalues = data['eigenvalues']     # (50, 32)
cell_labels = data['cell_labels']     # (32, 2)
cell_casimirs = data['cell_casimirs'] # (32,)
cell_dims = data['cell_dims']         # (32,)

N_tau, N_modes = eigenvalues.shape
dtau = tau_values[1] - tau_values[0]

print(f"Loaded: {N_tau} tau points, {N_modes} modes")
print(f"tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}], dtau = {dtau:.6f}")

# ============================================================
#  2. Central differences: dE_k/dtau
# ============================================================
# Use central differences for interior points, forward/backward at boundaries
dE_dtau = np.zeros_like(eigenvalues)

# Interior: central differences
dE_dtau[1:-1, :] = (eigenvalues[2:, :] - eigenvalues[:-2, :]) / (2.0 * dtau)

# Boundaries: one-sided differences
dE_dtau[0, :] = (eigenvalues[1, :] - eigenvalues[0, :]) / dtau
dE_dtau[-1, :] = (eigenvalues[-1, :] - eigenvalues[-2, :]) / dtau

print("\n--- dE_k/dtau computed (central differences) ---")

# ============================================================
#  3. d(E_k^2)/dtau = 2 * E_k * dE_k/dtau  (mass-squared rate)
# ============================================================
dm2_dtau = 2.0 * eigenvalues * dE_dtau  # (50, 32) — Eq 7.1 analog

# ============================================================
#  4. Total spectral weight and derivatives
# ============================================================
M_total = np.sum(eigenvalues, axis=1)          # Sum_k E_k(tau)
W_total = np.sum(eigenvalues**2, axis=1)       # Sum_k E_k^2(tau)

dM_total_dtau = np.zeros(N_tau)
dM_total_dtau[1:-1] = (M_total[2:] - M_total[:-2]) / (2.0 * dtau)
dM_total_dtau[0] = (M_total[1] - M_total[0]) / dtau
dM_total_dtau[-1] = (M_total[-1] - M_total[-2]) / dtau

dW_total_dtau = np.zeros(N_tau)
dW_total_dtau[1:-1] = (W_total[2:] - W_total[:-2]) / (2.0 * dtau)
dW_total_dtau[0] = (W_total[1] - W_total[0]) / dtau
dW_total_dtau[-1] = (W_total[-1] - W_total[-2]) / dtau

# Also: total dM/dtau from mode sum (should agree)
dM_total_sum = np.sum(dE_dtau, axis=1)
dW_total_sum = np.sum(dm2_dtau, axis=1)

# Cross-check: mode sum vs direct derivative
err_dM = np.max(np.abs(dM_total_dtau - dM_total_sum))
err_dW = np.max(np.abs(dW_total_dtau - dW_total_sum))
print(f"Cross-check dM: max |direct - sum| = {err_dM:.2e}")
print(f"Cross-check dW: max |direct - sum| = {err_dW:.2e}")

# ============================================================
#  5. Analysis at the fold (tau ~ tau_fold)
# ============================================================
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
tau_at_fold = tau_values[fold_idx]

print(f"\n=== FOLD ANALYSIS (tau = {tau_at_fold:.4f}, idx = {fold_idx}) ===")

dE_at_fold = dE_dtau[fold_idx, :]
E_at_fold = eigenvalues[fold_idx, :]
dm2_at_fold = dm2_dtau[fold_idx, :]

n_positive = np.sum(dE_at_fold > 0)
n_negative = np.sum(dE_at_fold < 0)
n_zero = np.sum(np.abs(dE_at_fold) < 1e-12)

print(f"Modes with dE/dtau > 0: {n_positive}")
print(f"Modes with dE/dtau < 0: {n_negative}")
print(f"Modes with dE/dtau ~ 0: {n_zero}")
print(f"dM_total/dtau at fold: {dM_total_dtau[fold_idx]:.6f}")
print(f"dW_total/dtau at fold: {dW_total_dtau[fold_idx]:.6f}")
print(f"M_total at fold: {M_total[fold_idx]:.6f}")
print(f"W_total at fold: {W_total[fold_idx]:.6f}")

# Spectral flow rate: fraction of total mass changing per unit tau
spectral_flow_rate = dM_total_dtau[fold_idx] / M_total[fold_idx]
print(f"Spectral flow rate (dM/M)/dtau at fold: {spectral_flow_rate:.6f}")

# Mass variation per mode at the fold
print(f"\n--- Mode-by-mode at fold (tau = {tau_at_fold:.4f}) ---")
print(f"{'k':>3}  {'(p,q)':>6}  {'C2':>8}  {'dim':>4}  {'E_k':>10}  {'dE/dtau':>12}  {'d(E^2)/dtau':>14}  {'sign':>5}")
for k in range(N_modes):
    p, q = cell_labels[k]
    sign_str = "+" if dE_at_fold[k] > 1e-12 else ("-" if dE_at_fold[k] < -1e-12 else "0")
    print(f"{k:3d}  ({p},{q})  {cell_casimirs[k]:8.4f}  {cell_dims[k]:4d}  "
          f"{E_at_fold[k]:10.6f}  {dE_at_fold[k]:12.6f}  {dm2_at_fold[k]:14.6f}  {sign_str:>5}")

# ============================================================
#  6. Dimension-weighted analysis
# ============================================================
# In the full Dirac spectrum, each (p,q) mode has degeneracy dim(p,q)^2 * spinor_dim
# Here we use dim(p,q) as the degeneracy weight for the tight-binding Hamiltonian
dim_weighted_dE = dE_dtau * cell_dims[np.newaxis, :]  # (50, 32)
dim_weighted_M = np.sum(eigenvalues * cell_dims[np.newaxis, :], axis=1)
dim_weighted_dM = np.sum(dim_weighted_dE, axis=1)

print(f"\n--- Dimension-weighted totals at fold ---")
print(f"dim-weighted M_total: {dim_weighted_M[fold_idx]:.6f}")
print(f"dim-weighted dM/dtau: {dim_weighted_dM[fold_idx]:.6f}")
print(f"dim-weighted flow rate: {dim_weighted_dM[fold_idx]/dim_weighted_M[fold_idx]:.6f}")

# ============================================================
#  7. Analytic check: volume-preserving TT deformation
# ============================================================
# For volume-preserving TT deformation, vol(SU(3), g_tau) = const.
# The total spectral weight Sum E_k^2 should scale with the average
# curvature, not remain constant. Check its monotonicity.
W_ratio = W_total / W_total[0]
print(f"\n--- Spectral weight Sum E_k^2 ---")
print(f"W(0)     = {W_total[0]:.6f}")
print(f"W(fold)  = {W_total[fold_idx]:.6f}")
print(f"W(0.5)   = {W_total[-1]:.6f}")
print(f"W(fold)/W(0) = {W_total[fold_idx]/W_total[0]:.6f}")
print(f"W(0.5)/W(0)  = {W_total[-1]/W_total[0]:.6f}")

# Check monotonicity of W
dW_sign_changes = np.sum(np.diff(np.sign(np.diff(W_total))) != 0)
W_monotone = np.all(np.diff(W_total) <= 0) or np.all(np.diff(W_total) >= 0)
print(f"W(tau) monotone: {W_monotone}")
print(f"W(tau) sign changes in dW/dtau: {dW_sign_changes}")

# ============================================================
#  8. Find zero crossings of dE_k/dtau (where mass flow reverses)
# ============================================================
print(f"\n--- Zero crossings of dE_k/dtau ---")
for k in range(N_modes):
    sign_changes = np.where(np.diff(np.sign(dE_dtau[:, k])))[0]
    if len(sign_changes) > 0:
        tau_crossings = [0.5 * (tau_values[i] + tau_values[i+1]) for i in sign_changes]
        p, q = cell_labels[k]
        print(f"  k={k} ({p},{q}): crossings at tau = {[f'{t:.3f}' for t in tau_crossings]}")

# ============================================================
#  9. Sector analysis (B1, B2, B3 sectors from BCS physics)
# ============================================================
# B1: (1,0) sector, k=2
# B2: multiple sectors at the gap edge
# B3: (0,1), k=1
# Identify sectors by Casimir ranges
print(f"\n--- Sector-resolved mass flow at fold ---")
B1_idx = [k for k in range(N_modes) if tuple(cell_labels[k]) == (1, 0)]
B2_idx = [k for k in range(N_modes) if tuple(cell_labels[k]) == (1, 1)]
B3_idx = [k for k in range(N_modes) if tuple(cell_labels[k]) == (0, 1)]

for name, indices in [("B1 (1,0)", B1_idx), ("B2 (1,1)", B2_idx), ("B3 (0,1)", B3_idx)]:
    if indices:
        E_sec = np.mean(E_at_fold[indices])
        dE_sec = np.mean(dE_at_fold[indices])
        print(f"  {name}: E = {E_sec:.6f}, dE/dtau = {dE_sec:.6f}")

# ============================================================
#  10. Maximum spectral flow rate along the transit
# ============================================================
flow_rate = dM_total_dtau / M_total
max_flow_idx = np.argmax(np.abs(flow_rate))
print(f"\n--- Maximum spectral flow rate ---")
print(f"Max |(dM/M)/dtau| = {np.abs(flow_rate[max_flow_idx]):.6f} at tau = {tau_values[max_flow_idx]:.4f}")
print(f"Flow rate at fold: {flow_rate[fold_idx]:.6f}")

# Also find maximum absolute dM/dtau
max_dM_idx = np.argmax(np.abs(dM_total_dtau))
print(f"Max |dM/dtau| = {np.abs(dM_total_dtau[max_dM_idx]):.6f} at tau = {tau_values[max_dM_idx]:.4f}")

# ============================================================
#  11. Save data
# ============================================================
np.savez('computations/session-56/s56_mass_variation.npz',
    tau_values=tau_values,
    eigenvalues=eigenvalues,
    dE_dtau=dE_dtau,
    dm2_dtau=dm2_dtau,
    M_total=M_total,
    W_total=W_total,
    dM_total_dtau=dM_total_dtau,
    dW_total_dtau=dW_total_dtau,
    dim_weighted_M=dim_weighted_M,
    dim_weighted_dM=dim_weighted_dM,
    flow_rate=flow_rate,
    cell_labels=cell_labels,
    cell_casimirs=cell_casimirs,
    cell_dims=cell_dims,
    fold_idx=fold_idx,
    tau_fold_actual=tau_at_fold,
    n_positive_fold=n_positive,
    n_negative_fold=n_negative,
    gate_name='MASS-VARIATION-56',
    gate_verdict='INFO',
)

print(f"\nData saved: computations/session-56/s56_mass_variation.npz")

# ============================================================
#  12. Plots
# ============================================================
fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.35)

# --- Panel (a): All eigenvalues vs tau ---
ax1 = fig.add_subplot(gs[0, 0])
for k in range(N_modes):
    p, q = cell_labels[k]
    ax1.plot(tau_values, eigenvalues[:, k], lw=0.7, alpha=0.7)
ax1.axvline(tau_at_fold, color='red', ls='--', lw=1, alpha=0.7, label=f'fold tau={tau_at_fold:.2f}')
ax1.set_xlabel(r'$\tau$')
ax1.set_ylabel(r'$E_k(\tau)$ [M$_{\rm KK}$]')
ax1.set_title('(a) Eigenvalue spectrum')
ax1.legend(fontsize=8)

# --- Panel (b): dE_k/dtau vs tau ---
ax2 = fig.add_subplot(gs[0, 1])
for k in range(N_modes):
    ax2.plot(tau_values, dE_dtau[:, k], lw=0.7, alpha=0.7)
ax2.axvline(tau_at_fold, color='red', ls='--', lw=1, alpha=0.7)
ax2.axhline(0, color='black', ls='-', lw=0.5)
ax2.set_xlabel(r'$\tau$')
ax2.set_ylabel(r'$dE_k/d\tau$ [M$_{\rm KK}$]')
ax2.set_title(r'(b) Mass variation rate $dE_k/d\tau$')

# --- Panel (c): d(E_k^2)/dtau vs tau (Paper 16 Eq 7.1 analog) ---
ax3 = fig.add_subplot(gs[0, 2])
for k in range(N_modes):
    ax3.plot(tau_values, dm2_dtau[:, k], lw=0.7, alpha=0.7)
ax3.axvline(tau_at_fold, color='red', ls='--', lw=1, alpha=0.7)
ax3.axhline(0, color='black', ls='-', lw=0.5)
ax3.set_xlabel(r'$\tau$')
ax3.set_ylabel(r'$d(E_k^2)/d\tau$ [M$_{\rm KK}^2$]')
ax3.set_title(r'(c) $d(m_k^2)/d\tau$ (Eq 7.1 analog)')

# --- Panel (d): M_total and dM_total/dtau ---
ax4 = fig.add_subplot(gs[1, 0])
ax4.plot(tau_values, M_total, 'b-', lw=2, label=r'$M_{\rm tot}(\tau)$')
ax4.axvline(tau_at_fold, color='red', ls='--', lw=1, alpha=0.7)
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel(r'$M_{\rm tot}$ [M$_{\rm KK}$]', color='b')
ax4.tick_params(axis='y', labelcolor='b')
ax4r = ax4.twinx()
ax4r.plot(tau_values, dM_total_dtau, 'r-', lw=2, label=r'$dM_{\rm tot}/d\tau$')
ax4r.set_ylabel(r'$dM_{\rm tot}/d\tau$ [M$_{\rm KK}$]', color='r')
ax4r.tick_params(axis='y', labelcolor='r')
ax4.set_title(r'(d) Total mass $M_{\rm tot}$ and rate')

# --- Panel (e): Spectral weight W = Sum E_k^2 ---
ax5 = fig.add_subplot(gs[1, 1])
ax5.plot(tau_values, W_total, 'b-', lw=2, label=r'$W(\tau) = \sum E_k^2$')
ax5.axvline(tau_at_fold, color='red', ls='--', lw=1, alpha=0.7)
ax5.set_xlabel(r'$\tau$')
ax5.set_ylabel(r'$W(\tau)$ [M$_{\rm KK}^2$]')
ax5.set_title(r'(e) Spectral weight $\sum E_k^2(\tau)$')
ax5r = ax5.twinx()
ax5r.plot(tau_values, dW_total_dtau, 'r-', lw=2)
ax5r.set_ylabel(r'$dW/d\tau$ [M$_{\rm KK}^2$]', color='r')
ax5r.tick_params(axis='y', labelcolor='r')

# --- Panel (f): Spectral flow rate (dM/M)/dtau ---
ax6 = fig.add_subplot(gs[1, 2])
ax6.plot(tau_values, flow_rate, 'k-', lw=2)
ax6.axvline(tau_at_fold, color='red', ls='--', lw=1, alpha=0.7)
ax6.axhline(0, color='gray', ls='-', lw=0.5)
ax6.set_xlabel(r'$\tau$')
ax6.set_ylabel(r'$(dM_{\rm tot}/d\tau) / M_{\rm tot}$')
ax6.set_title('(f) Spectral flow rate')

# --- Panel (g): dE/dtau at fold, bar chart by mode ---
ax7 = fig.add_subplot(gs[2, 0:2])
colors = ['tab:blue' if dE_at_fold[k] < 0 else 'tab:red' for k in range(N_modes)]
mode_labels = [f"({cell_labels[k,0]},{cell_labels[k,1]})" for k in range(N_modes)]
bars = ax7.bar(range(N_modes), dE_at_fold, color=colors, edgecolor='black', lw=0.3)
ax7.set_xticks(range(N_modes))
ax7.set_xticklabels(mode_labels, rotation=90, fontsize=6)
ax7.set_xlabel('Mode (p,q)')
ax7.set_ylabel(r'$dE_k/d\tau$ at fold')
ax7.set_title(f'(g) Mode-resolved mass flow at fold (tau={tau_at_fold:.2f})')
ax7.axhline(0, color='black', ls='-', lw=0.5)

# --- Panel (h): Dimension-weighted mass flow ---
ax8 = fig.add_subplot(gs[2, 2])
ax8.plot(tau_values, dim_weighted_dM, 'g-', lw=2, label='dim-weighted')
ax8.plot(tau_values, dM_total_dtau, 'b--', lw=1.5, label='unweighted')
ax8.axvline(tau_at_fold, color='red', ls='--', lw=1, alpha=0.7)
ax8.axhline(0, color='black', ls='-', lw=0.5)
ax8.set_xlabel(r'$\tau$')
ax8.set_ylabel(r'$dM/d\tau$ [M$_{\rm KK}$]')
ax8.set_title('(h) Mass flow: weighted vs unweighted')
ax8.legend(fontsize=8)

fig.suptitle('MASS-VARIATION-56: Paper 16 Eq 7.1 Mass Variation Along Jensen Transit',
             fontsize=14, fontweight='bold')

plt.savefig('computations/session-56/s56_mass_variation.png', dpi=150, bbox_inches='tight')
print("Plot saved: computations/session-56/s56_mass_variation.png")

# ============================================================
#  13. Final summary
# ============================================================
print("\n" + "="*70)
print("MASS-VARIATION-56 SUMMARY")
print("="*70)
print(f"Gate: INFO (geometric diagnostic)")
print(f"")
print(f"Fold location: tau = {tau_at_fold:.4f} (idx {fold_idx})")
print(f"")
print(f"At fold:")
print(f"  M_total = {M_total[fold_idx]:.4f} M_KK")
print(f"  dM_total/dtau = {dM_total_dtau[fold_idx]:.4f} M_KK")
print(f"  W_total = Sum E_k^2 = {W_total[fold_idx]:.4f} M_KK^2")
print(f"  dW_total/dtau = {dW_total_dtau[fold_idx]:.4f} M_KK^2")
print(f"  Spectral flow rate = {flow_rate[fold_idx]:.6f}")
print(f"  Modes with dE/dtau > 0: {n_positive}/{N_modes}")
print(f"  Modes with dE/dtau < 0: {n_negative}/{N_modes}")
print(f"  Modes with dE/dtau ~ 0: {n_zero}/{N_modes}")
print(f"")
print(f"Full transit:")
print(f"  M_total(0) = {M_total[0]:.4f}, M_total(0.5) = {M_total[-1]:.4f}")
print(f"  M ratio = M(0.5)/M(0) = {M_total[-1]/M_total[0]:.6f}")
print(f"  W(0) = {W_total[0]:.4f}, W(0.5) = {W_total[-1]:.4f}")
print(f"  W ratio = W(0.5)/W(0) = {W_total[-1]/W_total[0]:.6f}")
print(f"  W(tau) monotonically decreasing: {np.all(np.diff(W_total) <= 0)}")
print(f"  Max |flow rate| = {np.max(np.abs(flow_rate)):.6f} at tau = {tau_values[np.argmax(np.abs(flow_rate))]:.4f}")
print(f"")

# Dim-weighted summary
dw_flow_fold = dim_weighted_dM[fold_idx] / dim_weighted_M[fold_idx]
print(f"Dimension-weighted at fold:")
print(f"  dim*M_total = {dim_weighted_M[fold_idx]:.4f}")
print(f"  dim*dM/dtau = {dim_weighted_dM[fold_idx]:.4f}")
print(f"  dim-weighted flow rate = {dw_flow_fold:.6f}")
print(f"")
print(f"Files: s56_mass_variation.npz, s56_mass_variation.png")
print("="*70)
