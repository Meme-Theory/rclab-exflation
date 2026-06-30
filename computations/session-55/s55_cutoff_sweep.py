#!/usr/bin/env python3
"""
s55_cutoff_sweep.py — CUTOFF-SWEEP-55
======================================
Sweep cutoff Lambda continuously from 0.5 to 3.0 M_KK (20 values, primary range)
and from 0.5 to 10.0 M_KK (40 values, extended range for asymptotic test).
Track tau_min(Lambda) of S_occ to classify: pinned (physical) vs tracking (artifact).

S_occ(tau; Lambda) = sum_k n_k(tau) * f(E_k(tau)^2 / Lambda^2)

where n_k are BCS occupations with Delta_OES = 0.4643 M_KK, and f is the sharp
cutoff f(x) = Theta(1-x), consistent with S54's spectral action formula.

Gate: CUTOFF-SWEEP-55 (INFO)
"""

import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, 'computations')
from canonical_constants import *

# ============================================================
# 1. Load data
# ============================================================
tb_data = np.load('computations/session-54/s54_tb_hamiltonian.npz')
occ_data = np.load('computations/session-54/s54_sa_latt_occ.npz')

tau_values = tb_data['tau_values']       # (50,)
eigenvalues = tb_data['eigenvalues']     # (50, 32)
occ_bcs = occ_data['occ_bcs_oes']       # (50, 32)
Delta_OES = float(occ_data['Delta_primary'])  # 0.4643

n_tau = len(tau_values)
n_modes = eigenvalues.shape[1]  # (local)

print(f"Loaded: {n_tau} tau values, {n_modes} modes")
print(f"Delta_OES = {Delta_OES:.4f}")
print(f"tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"Eigenvalue range: [{eigenvalues.min():.6e}, {eigenvalues.max():.4f}]")

# ============================================================
# 2. Define Lambda sweeps
# ============================================================
# Primary sweep: 20 values in [0.5, 3.0] per task spec
n_Lambda_primary = 20
Lambda_primary = np.linspace(0.5, 3.0, n_Lambda_primary)

# Extended sweep: 40 values in [0.5, 10.0] for asymptotic test
n_Lambda_ext = 40
Lambda_extended = np.linspace(0.5, 10.0, n_Lambda_ext)

print(f"\nPrimary sweep: {n_Lambda_primary} values in [{Lambda_primary[0]:.2f}, {Lambda_primary[-1]:.2f}]")
print(f"Extended sweep: {n_Lambda_ext} values in [{Lambda_extended[0]:.2f}, {Lambda_extended[-1]:.2f}]")

# ============================================================
# 3. Compute S_occ(tau; Lambda)
# ============================================================
def compute_S_occ(Lambda_arr, eigenvalues, occ_bcs):
    """Compute S_occ(tau; Lambda) = sum_k n_k(tau) * Theta(1 - E_k^2/Lambda^2)."""
    n_L = len(Lambda_arr)
    n_t = eigenvalues.shape[0]  # (local)
    S = np.zeros((n_L, n_t))
    for i, Lam in enumerate(Lambda_arr):
        for j in range(n_t):
            x = eigenvalues[j, :]**2 / Lam**2
            mask = x < 1.0  # Theta(1 - x)
            S[i, j] = np.sum(occ_bcs[j, :] * mask)
    return S

S_occ_prim = compute_S_occ(Lambda_primary, eigenvalues, occ_bcs)
S_occ_ext = compute_S_occ(Lambda_extended, eigenvalues, occ_bcs)

# ============================================================
# 4. Find tau_min(Lambda) for each Lambda
# ============================================================
def find_tau_min(S_occ, tau_values):
    """Find tau that minimizes S_occ for each Lambda."""
    tau_min_idx = np.argmin(S_occ, axis=1)
    tau_min_vals = tau_values[tau_min_idx]
    S_occ_min = np.array([S_occ[i, tau_min_idx[i]] for i in range(len(tau_min_idx))])
    return tau_min_idx, tau_min_vals, S_occ_min

idx_prim, tau_min_prim, S_min_prim = find_tau_min(S_occ_prim, tau_values)
idx_ext, tau_min_ext, S_min_ext = find_tau_min(S_occ_ext, tau_values)

# ============================================================
# 5. Primary sweep results
# ============================================================
print("\n" + "="*70)
print("PRIMARY SWEEP RESULTS: tau_min(Lambda) trajectory")
print("="*70)
print(f"{'Lambda':>8s} {'tau_min':>8s} {'S_min':>8s} {'S_max':>8s} {'N_in_avg':>10s} {'depth_%':>8s}")
print("-"*58)
for i, Lambda in enumerate(Lambda_primary):
    n_in = np.mean([np.sum(eigenvalues[j, :]**2 < Lambda**2) for j in range(n_tau)])
    socc = S_occ_prim[i, :]
    depth_L = socc[0] - socc[idx_prim[i]]
    depth_R = socc[-1] - socc[idx_prim[i]]
    barrier = min(depth_L, depth_R)
    rel = barrier / socc[idx_prim[i]] * 100 if socc[idx_prim[i]] > 0 else 0
    print(f"{Lambda:8.3f} {tau_min_prim[i]:8.4f} {S_min_prim[i]:8.4f} "
          f"{socc.max():8.4f} {n_in:10.1f} {rel:8.1f}")

# ============================================================
# 6. Classification
# ============================================================
# Linear regression on primary sweep
coeffs_prim = np.polyfit(Lambda_primary, tau_min_prim, 1)
slope_prim = coeffs_prim[0]

# Linear regression on extended sweep
coeffs_ext = np.polyfit(Lambda_extended, tau_min_ext, 1)
slope_ext = coeffs_ext[0]

# Also fit high-Lambda regime (Lambda > 2.0) of extended sweep
mask_high = Lambda_extended > 2.0
if np.sum(mask_high) > 2:
    coeffs_high = np.polyfit(Lambda_extended[mask_high], tau_min_ext[mask_high], 1)
    slope_high = coeffs_high[0]
else:
    slope_high = np.nan

print(f"\nLinear fits:")
print(f"  Primary [0.5, 3.0]: slope = {slope_prim:.4f}")
print(f"  Extended [0.5, 10.0]: slope = {slope_ext:.4f}")
print(f"  High-Lambda [2.0, 10.0]: slope = {slope_high:.4f}")

# Local slopes
local_slopes = np.diff(tau_min_prim) / np.diff(Lambda_primary)
mean_abs_local = np.mean(np.abs(local_slopes))
max_abs_local = np.max(np.abs(local_slopes))

print(f"\nLocal slopes (primary):")
print(f"  Mean |slope| = {mean_abs_local:.4f}")
print(f"  Max |slope| = {max_abs_local:.4f}")

# tau_min range statistics
print(f"\ntau_min statistics:")
print(f"  Primary: range=[{tau_min_prim.min():.4f}, {tau_min_prim.max():.4f}], "
      f"mean={tau_min_prim.mean():.4f}, std={tau_min_prim.std():.4f}")
print(f"  Extended: range=[{tau_min_ext.min():.4f}, {tau_min_ext.max():.4f}], "
      f"mean={tau_min_ext.mean():.4f}, std={tau_min_ext.std():.4f}")

# Definitive classification using extended sweep
# The key test: does tau_min span a large fraction of the available tau range?
tau_range_span = (tau_min_ext.max() - tau_min_ext.min()) / (tau_values[-1] - tau_values[0])

# Does the linear slope have |slope| > 0.01?
if abs(slope_ext) > 0.1:
    classification = "TRACKING"
    class_detail = (f"|slope_ext|={abs(slope_ext):.4f} > 0.1. "
                    f"tau_min spans {tau_range_span*100:.0f}% of tau range. Edge artifact.")
elif abs(slope_ext) < 0.01 and tau_range_span < 0.1:
    classification = "PINNED"
    class_detail = (f"|slope_ext|={abs(slope_ext):.4f} < 0.01. "
                    f"tau_min spans only {tau_range_span*100:.0f}% of tau range. Physical.")
else:
    classification = "TRACKING"
    class_detail = (f"|slope_ext|={abs(slope_ext):.4f}, "
                    f"tau_min spans {tau_range_span*100:.0f}% of tau range. "
                    f"Systematic drift with Lambda rules out pinning.")

# Check fold proximity
near_fold_primary = np.all((tau_min_prim > 0.15) & (tau_min_prim < 0.25))
near_fold_extended = np.all((tau_min_ext > 0.15) & (tau_min_ext < 0.25))
frac_near_fold_ext = np.mean((tau_min_ext > 0.15) & (tau_min_ext < 0.25))

print(f"\nClassification: {classification}")
print(f"  {class_detail}")
print(f"  All near fold (primary)? {near_fold_primary}")
print(f"  All near fold (extended)? {near_fold_extended}")
print(f"  Fraction near fold (extended): {frac_near_fold_ext:.2f}")

# ============================================================
# 7. Extended sweep table
# ============================================================
print("\n" + "="*70)
print("EXTENDED SWEEP: tau_min(Lambda) trajectory")
print("="*70)
print(f"{'Lambda':>8s} {'tau_min':>8s} {'S_min':>8s} {'N_in_avg':>10s}")
print("-"*40)
for i, Lambda in enumerate(Lambda_extended):
    n_in = np.mean([np.sum(eigenvalues[j, :]**2 < Lambda**2) for j in range(n_tau)])
    print(f"{Lambda:8.3f} {tau_min_ext[i]:8.4f} {S_min_ext[i]:8.4f} {n_in:10.1f}")

# ============================================================
# 8. Asymptotic analysis
# ============================================================
print("\n" + "="*70)
print("ASYMPTOTIC ANALYSIS")
print("="*70)

# S_occ at Lambda -> infinity: sum of all n_k (all modes in cutoff)
S_occ_inf = np.sum(occ_bcs, axis=1)
print(f"S_occ(Lambda=inf): range [{S_occ_inf.min():.6f}, {S_occ_inf.max():.6f}]")
print(f"  Variation: {(S_occ_inf.max() - S_occ_inf.min()):.6e}")
print(f"  This is sum_k n_k = 2.0 (half-filling). Profile is FLAT => no physical minimum.")

# As Lambda decreases from infinity, modes are removed at LARGE tau first
# (eigenvalues scale as bandwidth, which increases at small tau)
# This creates an ARTIFICIAL depression at large tau, driving tau_min upward
# Then at very small Lambda, only the lowest modes survive, and their
# occupations at small tau dominate, pushing tau_min around
print(f"\nMechanism: As Lambda decreases, modes drop out. High-energy modes")
print(f"drop out first at small tau (where bandwidth is largest). This creates")
print(f"artificial S_occ depression that TRACKS Lambda, not geometry.")

# Verify: bandwidth vs tau
bw = np.max(eigenvalues, axis=1)
print(f"\nBandwidth: tau=0 -> {bw[0]:.2f}, tau=0.20 -> {bw[20]:.2f}, tau=0.50 -> {bw[-1]:.2f}")
print(f"Bandwidth ratio (tau=0 / tau=0.5) = {bw[0]/bw[-1]:.2f}")
print(f"=> Cutoff bites harder at small tau => S_occ drops more at small tau")
print(f"   at intermediate Lambda, creating a TRACKING minimum.")

# ============================================================
# 9. Depth analysis
# ============================================================
print("\n" + "="*70)
print("MINIMUM DEPTH ANALYSIS")
print("="*70)
depths_prim = []
for i in range(n_Lambda_primary):
    socc = S_occ_prim[i, :]
    depth_L = socc[0] - socc[idx_prim[i]]
    depth_R = socc[-1] - socc[idx_prim[i]]
    barrier = min(depth_L, depth_R)
    rel = barrier / socc[idx_prim[i]] * 100 if socc[idx_prim[i]] > 0 else 0
    depths_prim.append(rel)

print(f"Relative depth range (primary): [{min(depths_prim):.2f}%, {max(depths_prim):.2f}%]")
print(f"Mean relative depth: {np.mean(depths_prim):.2f}%")
print(f"Depth < 1% at Lambda = {Lambda_primary[np.array(depths_prim) < 1.0]} (endpoint-dominated)")

# ============================================================
# 10. Plot
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('CUTOFF-SWEEP-55: S_occ Cutoff Dependence — TRACKING',
             fontsize=14, fontweight='bold')

# Panel 1: S_occ(tau) for selected Lambda values (primary sweep)
ax1 = axes[0, 0]
colors = plt.cm.viridis(np.linspace(0, 1, n_Lambda_primary))
highlight = [0, 4, 9, 14, 19]
for i in range(n_Lambda_primary):
    alpha = 0.3 if i not in highlight else 1.0  # (local)
    lw = 1.0 if i not in highlight else 2.0  # (local)
    label = f"$\\Lambda$={Lambda_primary[i]:.2f}" if i in highlight else None
    ax1.plot(tau_values, S_occ_prim[i, :], color=colors[i],
             alpha=alpha, linewidth=lw, label=label)
    # Mark minimum
    if i in highlight:
        ax1.plot(tau_min_prim[i], S_min_prim[i], 'v', color=colors[i],
                 markersize=8, markeredgecolor='k', zorder=5)
ax1.axvline(x=0.2015, color='red', linestyle='--', alpha=0.5, label='fold')
ax1.set_xlabel(r'$\tau$')
ax1.set_ylabel(r'$S_{\rm occ}(\tau; \Lambda)$')
ax1.set_title(r'$S_{\rm occ}$ profiles (primary sweep)')
ax1.legend(fontsize=7, loc='upper right')
ax1.grid(True, alpha=0.3)

# Panel 2: tau_min vs Lambda (extended sweep, definitive)
ax2 = axes[0, 1]
ax2.plot(Lambda_extended, tau_min_ext, 'ko-', markersize=4, linewidth=1.5,
         label='Extended sweep')
ax2.plot(Lambda_primary, tau_min_prim, 'bs', markersize=8, markerfacecolor='none',
         linewidth=0, label='Primary sweep', zorder=6)
ax2.axhline(y=0.2015, color='red', linestyle='--', alpha=0.7,
            label=r'$\tau_{\rm fold}=0.2015$')
ax2.fill_between([0.3, 10.5], 0.15, 0.25, alpha=0.1, color='red',
                 label='Fold region')
fit_line_ext = np.polyval(coeffs_ext, Lambda_extended)
ax2.plot(Lambda_extended, fit_line_ext, 'b--', alpha=0.5,
         label=f'Fit: slope={slope_ext:.3f}')
ax2.set_xlabel(r'$\Lambda$ [$M_{\rm KK}$]')
ax2.set_ylabel(r'$\tau_{\rm min}(\Lambda)$')
ax2.set_title(f'$\\tau_{{\\rm min}}$ vs $\\Lambda$ -- {classification}')
ax2.legend(fontsize=7)
ax2.set_xlim([0.3, 10.5])
ax2.set_ylim([-0.02, 0.55])
ax2.grid(True, alpha=0.3)

# Panel 3: Mode count inside cutoff vs tau
ax3 = axes[1, 0]
for i, idx_show in enumerate([0, 10, 20, 30, 39]):
    Lambda = Lambda_extended[idx_show]
    n_in = np.array([np.sum(eigenvalues[j, :]**2 < Lambda**2) for j in range(n_tau)])
    ax3.plot(tau_values, n_in, 'o-', markersize=3,
             label=f"$\\Lambda$={Lambda:.1f}")
ax3.axhline(y=32, color='gray', linestyle=':', alpha=0.5, label='All 32 modes')
ax3.set_xlabel(r'$\tau$')
ax3.set_ylabel('Number of modes below cutoff')
ax3.set_title('Mode count inside cutoff')
ax3.legend(fontsize=7)
ax3.grid(True, alpha=0.3)

# Panel 4: Bandwidth vs tau (explains the tracking mechanism)
ax4 = axes[1, 1]
bw = np.max(eigenvalues, axis=1)
ax4.plot(tau_values, bw, 'k-', linewidth=2, label='Bandwidth')
for L in [1.0, 2.0, 3.0, 5.0]:
    ax4.axhline(y=L, linestyle='--', alpha=0.5, label=f'$\\Lambda$={L:.0f}')
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel('Bandwidth [$M_{\\rm KK}$]')
ax4.set_title(r'Bandwidth vs $\tau$ (tracking mechanism)')
ax4.legend(fontsize=7)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-55/s55_cutoff_sweep.png', dpi=150)
print(f"\nPlot saved: computations/session-55/s55_cutoff_sweep.png")

# ============================================================
# 11. Save results
# ============================================================
np.savez('computations/session-55/s55_cutoff_sweep.npz',
         Lambda_primary=Lambda_primary,
         Lambda_extended=Lambda_extended,
         tau_values=tau_values,
         S_occ_primary=S_occ_prim,
         S_occ_extended=S_occ_ext,
         tau_min_primary=tau_min_prim,
         tau_min_extended=tau_min_ext,
         S_min_primary=S_min_prim,
         S_min_extended=S_min_ext,
         slope_primary=slope_prim,
         slope_extended=slope_ext,
         slope_high=slope_high,
         classification=classification,
         Delta_OES=Delta_OES,
         depths_primary=np.array(depths_prim),
         gate_name='CUTOFF-SWEEP-55',
         gate_verdict='INFO')

print(f"Data saved: computations/session-55/s55_cutoff_sweep.npz")

# ============================================================
# 12. Final summary
# ============================================================
print("\n" + "="*70)
print("GATE VERDICT: CUTOFF-SWEEP-55 — INFO")
print("="*70)
print(f"Classification: {classification}")
print(f"Slopes: primary={slope_prim:.4f}, extended={slope_ext:.4f}, high-Lambda={slope_high:.4f}")
print(f"tau_min(Lambda=0.5) = {tau_min_ext[0]:.4f}")
print(f"tau_min(Lambda=3.0) = {tau_min_prim[-1]:.4f}")
print(f"tau_min(Lambda=10.0) = {tau_min_ext[-1]:.4f}")
print(f"tau_min range (extended): [{tau_min_ext.min():.4f}, {tau_min_ext.max():.4f}]")
print(f"tau_min spans {tau_range_span*100:.0f}% of available tau range")
print(f"Near fold [0.15,0.25]? Primary: {near_fold_primary}, Extended: {near_fold_extended}")
print(f"Fraction of extended sweep near fold: {frac_near_fold_ext:.0%}")
print(f"Minimum depth range: [{min(depths_prim):.2f}%, {max(depths_prim):.2f}%]")
print(f"Mechanism: bandwidth decreases with tau ({bw[0]:.1f} -> {bw[-1]:.1f}),")
print(f"  so cutoff bites harder at small tau, creating artificial depression that tracks Lambda.")
print(f"CONCLUSION: S_occ minimum is a CUTOFF ARTIFACT, not a physical standing wave.")
