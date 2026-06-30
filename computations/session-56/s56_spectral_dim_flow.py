"""
s56_spectral_dim_flow.py — Spectral Dimension Flow from Collective Modes

Computes d_s(t) = -2 d(ln P)/d(ln t) on the 32-cell tight-binding graph
at the Jensen fold (tau ~ 0.194), using eigenvalues from s54_tb_hamiltonian.npz.

The heat kernel return probability is:
    P(t) = (1/N) Sum_n exp(-lambda_n * t)

where lambda_n are the TB eigenvalues (energies, not squared — the TB
Hamiltonian is already the "Laplacian" on the graph).

Energy thresholds marked:
    omega_J = 0.715 M_KK  (Josephson coupling)
    2*Delta = 0.929 M_KK  (pair-breaking threshold)

Also loads s54_graph_laplacian_ds.npz for comparison with the unweighted
graph Laplacian spectral dimension.

Gate: SPECTRAL-DIM-FLOW-56 (INFO)

Author: Spectral-Geometer
Session: S56
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, 'computations')
from canonical_constants import (
    N_cells, Delta_0_OES, E_B1, E_B2_mean, E_B3_mean,
    tau_fold, M_KK
)

# ============================================================
# 1. Load data
# ============================================================
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
tau_values = tb['tau_values']
all_eigs = tb['eigenvalues']  # (50, 32)

# Find fold index
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
tau_at_fold = tau_values[fold_idx]
print(f"Fold: tau = {tau_at_fold:.4f} (index {fold_idx})")

# Eigenvalues at fold
lambda_n = all_eigs[fold_idx]  # 32 eigenvalues
N = len(lambda_n)
print(f"N = {N} eigenvalues")
print(f"lambda_min = {lambda_n.min():.6f}, lambda_max = {lambda_n.max():.6f}")
print(f"Bandwidth = {lambda_n.max() - lambda_n.min():.6f}")

# Energy thresholds (in M_KK units = 1)
omega_J = 0.715   # Josephson coupling energy  # (local)
two_Delta = 2 * Delta_0_OES  # pair-breaking threshold = 0.929

print(f"\nEnergy thresholds:")
print(f"  omega_J   = {omega_J:.3f} M_KK")
print(f"  2*Delta   = {two_Delta:.4f} M_KK")

# ============================================================
# 2. Compute heat kernel P(t) and spectral dimension d_s(t)
# ============================================================
# Use diffusion time t from 1e-3 to 1e3 (log scale)
N_t = 5000  # (local)
t_arr = np.logspace(-3, 3, N_t)

# P(t) = (1/N) sum_n exp(-lambda_n * t)
# For numerical stability, factor out the zero mode
lambda_sorted = np.sort(lambda_n)
lambda_positive = lambda_sorted[lambda_sorted > 1e-10]  # exclude zero mode
n_zero = N - len(lambda_positive)
print(f"\nZero modes: {n_zero}")
print(f"Positive eigenvalues: {len(lambda_positive)}")

# P(t) = (1/N) * [n_zero + sum_{positive} exp(-lambda_k * t)]
P_t = np.zeros(N_t)
for i, t in enumerate(t_arr):
    P_t[i] = (n_zero + np.sum(np.exp(-lambda_positive * t))) / N

# d_s(t) = -2 * d(ln P)/d(ln t)
# Compute via finite differences on log-log scale
ln_t = np.log(t_arr)
ln_P = np.log(P_t)

# Central finite differences (4th order) for interior, forward/backward at edges
d_lnP_d_lnt = np.gradient(ln_P, ln_t)
ds_t = -2.0 * d_lnP_d_lnt

# ============================================================
# 3. Energy axis: E ~ 1/t
# ============================================================
E_arr = 1.0 / t_arr  # energy in M_KK units

# ============================================================
# 4. Identify regimes and plateaus
# ============================================================
# UV regime: t << 1/lambda_max => E >> lambda_max
# IR regime: t >> 1/lambda_1 => E << lambda_1
# Intermediate: between

# Find plateau values in different energy regimes
# Above pair-breaking: E > 2*Delta
mask_above_pair = (E_arr > two_Delta) & (E_arr < lambda_sorted[-1])
if np.any(mask_above_pair):
    ds_above_pair = np.median(ds_t[mask_above_pair])
else:
    ds_above_pair = np.nan

# Between omega_J and 2*Delta
mask_between = (E_arr > omega_J) & (E_arr < two_Delta)
if np.any(mask_between):
    ds_between = np.median(ds_t[mask_between])
else:
    ds_between = np.nan

# Below omega_J
mask_below_J = (E_arr > lambda_sorted[1]) & (E_arr < omega_J)
if np.any(mask_below_J):
    ds_below_J = np.median(ds_t[mask_below_J])
else:
    ds_below_J = np.nan

# Deep IR (E << lambda_1)
mask_deep_ir = E_arr < lambda_sorted[1] * 0.1
if np.any(mask_deep_ir):
    ds_deep_ir = np.median(ds_t[mask_deep_ir])
else:
    ds_deep_ir = np.nan

# UV limit (E >> lambda_max)
mask_uv = E_arr > lambda_sorted[-1] * 10
if np.any(mask_uv):
    ds_uv = np.median(ds_t[mask_uv])
else:
    ds_uv = np.nan

# Peak d_s
ds_max = np.max(ds_t)
t_at_max = t_arr[np.argmax(ds_t)]
E_at_max = 1.0 / t_at_max

print(f"\n{'='*60}")
print(f"SPECTRAL DIMENSION FLOW RESULTS")
print(f"{'='*60}")
print(f"Peak d_s = {ds_max:.4f} at t = {t_at_max:.4f} (E = {E_at_max:.4f} M_KK)")
print(f"\nPlateau values by energy regime:")
print(f"  UV (E >> {lambda_sorted[-1]:.2f}):                    d_s = {ds_uv:.6f}")
print(f"  Above pair-breaking (E > {two_Delta:.3f}):    d_s ~ {ds_above_pair:.4f}")
print(f"  Between thresholds ({omega_J:.3f} < E < {two_Delta:.3f}): d_s ~ {ds_between:.4f}")
print(f"  Below Josephson (E < {omega_J:.3f}):          d_s ~ {ds_below_J:.4f}")
print(f"  Deep IR (E << {lambda_sorted[1]:.3f}):               d_s = {ds_deep_ir:.6f}")

# ============================================================
# 5. More detailed plateau analysis
# ============================================================
# Find local extrema and inflection points
# Smooth d_s slightly for robust extrema detection
from scipy.ndimage import gaussian_filter1d
ds_smooth = gaussian_filter1d(ds_t, sigma=20)

# d_s at specific energy thresholds
idx_omJ = np.argmin(np.abs(E_arr - omega_J))
idx_2D = np.argmin(np.abs(E_arr - two_Delta))
ds_at_omJ = ds_t[idx_omJ]
ds_at_2D = ds_t[idx_2D]
print(f"\nd_s at energy thresholds:")
print(f"  d_s(E = omega_J = {omega_J:.3f}) = {ds_at_omJ:.4f}")
print(f"  d_s(E = 2*Delta = {two_Delta:.4f}) = {ds_at_2D:.4f}")

# Count eigenvalues below each threshold
n_below_omJ = np.sum(lambda_sorted < omega_J)
n_below_2D = np.sum(lambda_sorted < two_Delta)
print(f"\nEigenvalue counting:")
print(f"  Below omega_J ({omega_J:.3f}):  {n_below_omJ}/{N} eigenvalues")
print(f"  Below 2*Delta ({two_Delta:.4f}): {n_below_2D}/{N} eigenvalues")

# Weyl dimension from eigenvalue counting
# N(E) ~ E^{d_W/2} => d_W = 2 * d(ln N)/d(ln E)
# Use cumulative count
E_count = np.sort(lambda_positive)
N_count = np.arange(1, len(E_count) + 1)
if len(E_count) > 5:
    # Fit log N vs log E for Weyl dimension
    log_E = np.log(E_count)
    log_N = np.log(N_count)
    # Fit in middle range to avoid edge effects
    mid_start = len(E_count) // 4
    mid_end = 3 * len(E_count) // 4
    slope, intercept = np.polyfit(log_E[mid_start:mid_end], log_N[mid_start:mid_end], 1)
    d_Weyl = 2 * slope
    print(f"\nWeyl dimension (from eigenvalue counting, mid-band): d_W = {d_Weyl:.3f}")

# ============================================================
# 6. Load and compare with graph Laplacian d_s
# ============================================================
gl = np.load('computations/session-54/s54_graph_laplacian_ds.npz', allow_pickle=True)
t_gl = gl['t_range']
ds_gl_fold = gl['ds_tau0p1939']
P_gl_fold = gl['P_tau0p1939']
eigs_gl = gl['eigs_unweighted']
ds_max_gl = gl['ds_max_unweighted']

print(f"\n{'='*60}")
print(f"COMPARISON: TB vs Graph Laplacian")
print(f"{'='*60}")
print(f"Graph Laplacian max d_s = {float(ds_max_gl):.4f}")
print(f"TB Hamiltonian max d_s  = {ds_max:.4f}")
print(f"Ratio: {ds_max / float(ds_max_gl):.4f}")

# Compute d_s from graph Laplacian at fold using same method
lambda_gl = np.sort(eigs_gl)
lambda_gl_pos = lambda_gl[lambda_gl > 1e-10]
n_zero_gl = N - len(lambda_gl_pos)

P_gl_recompute = np.zeros(N_t)
for i, t in enumerate(t_arr):
    P_gl_recompute[i] = (n_zero_gl + np.sum(np.exp(-lambda_gl_pos * t))) / N
ln_P_gl = np.log(P_gl_recompute)
d_lnP_gl = np.gradient(ln_P_gl, ln_t)
ds_gl_recompute = -2.0 * d_lnP_gl

# Bandwidth comparison
print(f"\nBandwidth comparison:")
print(f"  TB:  [{lambda_sorted[1]:.4f}, {lambda_sorted[-1]:.4f}] = {lambda_sorted[-1]-lambda_sorted[1]:.4f}")
print(f"  GL:  [{lambda_gl[1]:.4f}, {lambda_gl[-1]:.4f}] = {lambda_gl[-1]-lambda_gl[1]:.4f}")
print(f"  Ratio (GL/TB bandwidth): {(lambda_gl[-1]-lambda_gl[1])/(lambda_sorted[-1]-lambda_sorted[1]):.3f}")

# ============================================================
# 7. CDT comparison dimension values
# ============================================================
# CDT in 4D: d_s flows from 4 (IR) to ~2 (UV)
# On a finite graph: d_s flows from 0 (IR, gapped) through peak ~2 (graph dim) to 0 (UV)
# The peak d_s is the effective graph dimension

print(f"\n{'='*60}")
print(f"DIMENSIONAL FLOW INTERPRETATION")
print(f"{'='*60}")
print(f"TB graph: peak d_s = {ds_max:.4f}")
print(f"  This is the effective dimension of the 32-cell Peter-Weyl graph")
print(f"  as probed by diffusion at scale t ~ {t_at_max:.3f} (E ~ {E_at_max:.3f} M_KK)")
print(f"  Hausdorff dimension (from S54): {float(gl['d_hausdorff']):.4f}")
print(f"  Weyl dimension (from S54):      {float(gl['d_weyl']):.4f}")

# Identify the flow profile: UV -> peak -> IR
# Find half-max points
ds_half = ds_max / 2
above_half = ds_t > ds_half
transitions = np.diff(above_half.astype(int))
rise_idx = np.where(transitions == 1)[0]
fall_idx = np.where(transitions == -1)[0]

if len(rise_idx) > 0 and len(fall_idx) > 0:
    t_rise = t_arr[rise_idx[0]]
    t_fall = t_arr[fall_idx[-1]]
    E_rise = 1.0 / t_rise
    E_fall = 1.0 / t_fall
    print(f"\nHalf-maximum band:")
    print(f"  E_high = {E_rise:.3f} M_KK (t = {t_rise:.4f})")
    print(f"  E_low  = {E_fall:.3f} M_KK (t = {t_fall:.4f})")
    print(f"  Width in decades: {np.log10(E_rise/E_fall):.2f}")

# ============================================================
# 8. Regime-specific d_s with finer analysis
# ============================================================
# Compute d_s at many specific energies for table
energy_points = [0.01, 0.05, 0.1, 0.177, omega_J, two_Delta, 1.0, 2.0, 3.0, 5.0, 6.77, 10.0, 50.0]
print(f"\n{'E (M_KK)':>12s} {'t':>10s} {'d_s':>10s} {'Note':>20s}")
print("-" * 55)
for E_pt in energy_points:
    t_pt = 1.0 / E_pt
    idx = np.argmin(np.abs(t_arr - t_pt))
    note = ""
    if abs(E_pt - omega_J) < 0.001:
        note = "omega_J"
    elif abs(E_pt - two_Delta) < 0.001:
        note = "2*Delta"
    elif abs(E_pt - lambda_sorted[-1]) < 0.01:
        note = "lambda_max"
    elif abs(E_pt - lambda_sorted[1]) < 0.01:
        note = "lambda_1"
    print(f"{E_pt:12.4f} {t_pt:10.4f} {ds_t[idx]:10.4f} {note:>20s}")

# ============================================================
# 9. Tau sweep: d_s at peak across all tau values
# ============================================================
ds_peak_tau = np.zeros(len(tau_values))
E_peak_tau = np.zeros(len(tau_values))
for ti in range(len(tau_values)):
    eigs_ti = np.sort(all_eigs[ti])
    eigs_pos_ti = eigs_ti[eigs_ti > 1e-10]
    n_z_ti = N - len(eigs_pos_ti)
    P_ti = np.zeros(N_t)
    for i, t in enumerate(t_arr):
        P_ti[i] = (n_z_ti + np.sum(np.exp(-eigs_pos_ti * t))) / N
    ln_P_ti = np.log(P_ti)
    d_lnP_ti = np.gradient(ln_P_ti, ln_t)
    ds_ti = -2.0 * d_lnP_ti
    ds_peak_tau[ti] = np.max(ds_ti)
    E_peak_tau[ti] = 1.0 / t_arr[np.argmax(ds_ti)]

print(f"\n{'='*60}")
print(f"PEAK d_s vs tau")
print(f"{'='*60}")
for ti in [0, 5, 10, fold_idx, 25, 30, 40, 49]:
    if ti < len(tau_values):
        print(f"  tau = {tau_values[ti]:.4f}: d_s_max = {ds_peak_tau[ti]:.4f}, E_peak = {E_peak_tau[ti]:.4f}")

# Is d_s_max at fold special?
ds_at_fold = ds_peak_tau[fold_idx]
ds_mean = np.mean(ds_peak_tau)
ds_std = np.std(ds_peak_tau)
print(f"\nFold d_s_max = {ds_at_fold:.4f}")
print(f"Mean d_s_max = {ds_mean:.4f} +/- {ds_std:.4f}")
print(f"Fold deviation: {(ds_at_fold - ds_mean)/ds_std:.2f} sigma")

# ============================================================
# 10. Save data
# ============================================================
np.savez('computations/session-56/s56_spectral_dim_flow.npz',
    # Core results
    t_arr=t_arr,
    E_arr=E_arr,
    ds_t=ds_t,
    P_t=P_t,
    lambda_fold=lambda_n,
    tau_fold_used=tau_at_fold,
    fold_idx=fold_idx,
    N_cells=N,
    # Thresholds
    omega_J=omega_J,
    two_Delta=two_Delta,
    # Plateau values
    ds_uv=ds_uv,
    ds_above_pair=ds_above_pair,
    ds_between=ds_between,
    ds_below_J=ds_below_J,
    ds_deep_ir=ds_deep_ir,
    # Peak
    ds_max=ds_max,
    t_at_max=t_at_max,
    E_at_max=E_at_max,
    # At thresholds
    ds_at_omJ=ds_at_omJ,
    ds_at_2D=ds_at_2D,
    # Eigenvalue counts
    n_below_omJ=n_below_omJ,
    n_below_2D=n_below_2D,
    # Graph Laplacian comparison
    ds_gl_recompute=ds_gl_recompute,
    lambda_gl=lambda_gl,
    ds_max_gl=float(ds_max_gl),
    # Tau sweep
    ds_peak_tau=ds_peak_tau,
    E_peak_tau=E_peak_tau,
    tau_values=tau_values,
    # Weyl dimension
    d_Weyl_mid=d_Weyl,
    d_hausdorff=float(gl['d_hausdorff']),
    # Gate
    gate_name='SPECTRAL-DIM-FLOW-56',
    gate_verdict='INFO',
)
print(f"\nData saved to computations/session-56/s56_spectral_dim_flow.npz")

# ============================================================
# 11. Plot
# ============================================================
fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.32, wspace=0.30)

# --- Panel (a): d_s vs Energy (main result) ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.semilogx(E_arr, ds_t, 'b-', linewidth=1.5, label='TB Hamiltonian')
ax1.semilogx(1.0/t_arr, ds_gl_recompute, 'r--', linewidth=1.2, label='Graph Laplacian', alpha=0.7)

# Mark thresholds
ax1.axvline(omega_J, color='green', linestyle=':', linewidth=1.5, label=f'$\\omega_J = {omega_J:.3f}$')
ax1.axvline(two_Delta, color='orange', linestyle=':', linewidth=1.5, label=f'$2\\Delta = {two_Delta:.3f}$')

# Mark peak
ax1.axhline(ds_max, color='gray', linestyle='--', alpha=0.3)
ax1.plot(E_at_max, ds_max, 'ko', markersize=8, zorder=5)
ax1.annotate(f'$d_s^{{\\mathrm{{max}}}} = {ds_max:.3f}$',
             xy=(E_at_max, ds_max), xytext=(E_at_max*3, ds_max*0.85),
             fontsize=10, arrowprops=dict(arrowstyle='->', color='black'))

# Shade regimes
ax1.axvspan(1e-3, lambda_sorted[1], alpha=0.05, color='blue', label='Deep IR')
ax1.axvspan(lambda_sorted[-1], 1e3, alpha=0.05, color='red', label='UV')

ax1.set_xlabel('Energy $E$ [$M_{KK}$]', fontsize=12)
ax1.set_ylabel('Spectral dimension $d_s$', fontsize=12)
ax1.set_title(f'(a) Spectral dimension flow at fold ($\\tau = {tau_at_fold:.4f}$)', fontsize=12)
ax1.legend(fontsize=8, loc='upper right')
ax1.set_xlim(1e-3, 1e3)
ax1.set_ylim(-0.1, ds_max * 1.15)
ax1.grid(True, alpha=0.3)

# --- Panel (b): d_s vs diffusion time t ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.semilogx(t_arr, ds_t, 'b-', linewidth=1.5, label='TB')
ax2.semilogx(t_arr, ds_gl_recompute, 'r--', linewidth=1.2, label='GL', alpha=0.7)

# Mark threshold times
ax2.axvline(1.0/omega_J, color='green', linestyle=':', linewidth=1.5, label=f'$t = 1/\\omega_J$')
ax2.axvline(1.0/two_Delta, color='orange', linestyle=':', linewidth=1.5, label=f'$t = 1/(2\\Delta)$')

ax2.set_xlabel('Diffusion time $t$ [$M_{KK}^{-1}$]', fontsize=12)
ax2.set_ylabel('Spectral dimension $d_s$', fontsize=12)
ax2.set_title('(b) Spectral dimension vs diffusion time', fontsize=12)
ax2.legend(fontsize=8)
ax2.set_xlim(1e-3, 1e3)
ax2.set_ylim(-0.1, ds_max * 1.15)
ax2.grid(True, alpha=0.3)

# --- Panel (c): P(t) return probability ---
ax3 = fig.add_subplot(gs[1, 0])
ax3.loglog(t_arr, P_t, 'b-', linewidth=1.5, label='TB')
ax3.loglog(t_arr, P_gl_recompute, 'r--', linewidth=1.2, label='GL', alpha=0.7)
ax3.axhline(1.0/N, color='gray', linestyle='--', alpha=0.5, label=f'$1/N = {1.0/N:.4f}$')

ax3.axvline(1.0/omega_J, color='green', linestyle=':', linewidth=1.5)
ax3.axvline(1.0/two_Delta, color='orange', linestyle=':', linewidth=1.5)

ax3.set_xlabel('Diffusion time $t$ [$M_{KK}^{-1}$]', fontsize=12)
ax3.set_ylabel('Return probability $P(t)$', fontsize=12)
ax3.set_title('(c) Heat kernel return probability', fontsize=12)
ax3.legend(fontsize=9)
ax3.set_xlim(1e-3, 1e3)
ax3.grid(True, alpha=0.3)

# --- Panel (d): d_s_max vs tau ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(tau_values, ds_peak_tau, 'b-', linewidth=1.5)
ax4.axvline(tau_at_fold, color='red', linestyle='--', linewidth=1.2, label=f'Fold ($\\tau = {tau_at_fold:.4f}$)')
ax4.plot(tau_at_fold, ds_peak_tau[fold_idx], 'ro', markersize=8, zorder=5)

ax4.set_xlabel('Jensen parameter $\\tau$', fontsize=12)
ax4.set_ylabel('Peak $d_s^{\\mathrm{max}}$', fontsize=12)
ax4.set_title('(d) Peak spectral dimension vs $\\tau$', fontsize=12)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

fig.suptitle('SPECTRAL-DIM-FLOW-56: Spectral Dimension on 32-Cell TB Graph', fontsize=14, fontweight='bold')
plt.savefig('computations/session-56/s56_spectral_dim_flow.png', dpi=150, bbox_inches='tight')
print("Plot saved to computations/session-56/s56_spectral_dim_flow.png")

# ============================================================
# 12. Final summary
# ============================================================
print(f"\n{'='*60}")
print(f"GATE: SPECTRAL-DIM-FLOW-56")
print(f"VERDICT: INFO")
print(f"{'='*60}")
print(f"d_s profile on 32-cell TB graph at fold (tau = {tau_at_fold:.4f}):")
print(f"  Peak d_s = {ds_max:.4f} at E = {E_at_max:.4f} M_KK")
print(f"  d_s(omega_J = {omega_J:.3f}) = {ds_at_omJ:.4f}")
print(f"  d_s(2*Delta = {two_Delta:.4f}) = {ds_at_2D:.4f}")
print(f"  UV limit: d_s -> {ds_uv:.6f}")
print(f"  IR limit: d_s -> {ds_deep_ir:.6f}")
print(f"  Weyl dimension (counting): d_W = {d_Weyl:.3f}")
print(f"  Hausdorff dimension:        d_H = {float(gl['d_hausdorff']):.3f}")
print(f"  Graph Laplacian peak d_s = {float(ds_max_gl):.4f}")
print(f"  TB/GL peak ratio = {ds_max / float(ds_max_gl):.4f}")
print(f"  Fold d_s_max deviation: {(ds_at_fold - ds_mean)/ds_std:.2f} sigma from mean")
print(f"  Eigenvalues below omega_J: {n_below_omJ}/{N}")
print(f"  Eigenvalues below 2*Delta: {n_below_2D}/{N}")
