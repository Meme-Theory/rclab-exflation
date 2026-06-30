#!/usr/bin/env python3
"""
CUTOFF-FAMILY-55: One-parameter Fermi-Dirac cutoff sensitivity study.

Gate: CUTOFF-FAMILY-55 (INFO)
Pre-registered criterion: critical alpha and barrier(alpha) curve.

Method:
  S_occ(tau; alpha) = sum_k n_k(tau) * f_alpha(E_k(tau)^2 / Lambda^2)
  where f_alpha(x) = 1/(1 + exp(alpha*(x - 1)))

  alpha -> infinity: sharp step Theta(1 - x)
  alpha -> 0:        f -> 1/2 (constant, no cutoff effect)

Sweeps alpha in [0.5, 1000] to find where the barrier vanishes.

Author: Kaku-Speculative-Theorist agent
Session: S55, Wave 2, Computation W2-3
"""

import sys
sys.path.insert(0, 'computations')
from canonical_constants import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Load data ──────────────────────────────────────────────────────────
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz')
sa = np.load('computations/session-54/s54_sa_latt_occ.npz')

eigenvalues = tb['eigenvalues']   # (50, 32)
tau_values  = tb['tau_values']    # (50,)
occ_bcs     = sa['occ_bcs_oes']  # (50, 32) — BCS occupations
Delta_primary = float(sa['Delta_primary'])  # 0.4643

n_tau, n_modes = eigenvalues.shape
print(f"Loaded: {n_tau} tau points, {n_modes} modes")
print(f"Delta_primary = {Delta_primary:.4f}")
print(f"tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")

# ── Cutoff parameters ─────────────────────────────────────────────────
Lambda = 1.0  # M_KK units
alpha_values = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0, 1000.0])
n_alpha = len(alpha_values)

# Also do a fine sweep for the barrier-vs-alpha curve
alpha_fine = np.logspace(np.log10(0.3), np.log10(2000), 200)

# ── Fermi-Dirac cutoff function ───────────────────────────────────────
def f_alpha(x, alpha):
    """Fermi-Dirac cutoff: 1/(1 + exp(alpha*(x - 1)))"""
    arg = alpha * (x - 1.0)
    # Clip to avoid overflow
    arg = np.clip(arg, -500, 500)
    return 1.0 / (1.0 + np.exp(arg))

# ── Compute S_occ(tau; alpha) ─────────────────────────────────────────
def compute_S_occ(alpha_arr):
    """Compute S_occ for each alpha value."""
    n_a = len(alpha_arr)
    S_occ = np.zeros((n_a, n_tau))

    for i, alpha in enumerate(alpha_arr):
        for t in range(n_tau):
            E_k = eigenvalues[t, :]  # eigenvalues at this tau
            n_k = occ_bcs[t, :]     # BCS occupations at this tau
            x_k = E_k**2 / Lambda**2
            f_k = f_alpha(x_k, alpha)
            S_occ[i, t] = np.sum(n_k * f_k)

    return S_occ

print("\n── Computing S_occ for primary alpha values ──")
S_occ_primary = compute_S_occ(alpha_values)

print("── Computing S_occ for fine alpha sweep ──")
S_occ_fine = compute_S_occ(alpha_fine)

# ── Barrier analysis ──────────────────────────────────────────────────
def analyze_barrier(S_occ_arr, alpha_arr, tau_vals):
    """
    For each alpha: find tau_min, compute barrier height.
    Barrier = (max(S_occ at boundaries) - S_occ(tau_min)) / S_occ(tau_min)
    Only count as a real minimum if it's interior (not at endpoints).
    """
    n_a = len(alpha_arr)
    tau_min = np.zeros(n_a)
    barrier = np.zeros(n_a)
    S_min_val = np.zeros(n_a)
    S_boundary_max = np.zeros(n_a)
    has_interior_min = np.zeros(n_a, dtype=bool)

    for i in range(n_a):
        curve = S_occ_arr[i, :]
        idx_min = np.argmin(curve)
        tau_min[i] = tau_vals[idx_min]
        S_min_val[i] = curve[idx_min]

        # Boundary values
        S_left = curve[0]
        S_right = curve[-1]
        S_boundary_max[i] = max(S_left, S_right)

        # Interior minimum check (not at endpoints)
        has_interior_min[i] = (idx_min > 0) and (idx_min < len(curve) - 1)

        if has_interior_min[i] and S_min_val[i] > 0:
            barrier[i] = (S_boundary_max[i] - S_min_val[i]) / S_min_val[i]
        else:
            barrier[i] = 0.0

    return tau_min, barrier, S_min_val, S_boundary_max, has_interior_min

print("\n── Barrier analysis (primary) ──")
tau_min_p, barrier_p, S_min_p, S_bdy_p, has_min_p = analyze_barrier(
    S_occ_primary, alpha_values, tau_values)

print(f"\n{'alpha':>8s} {'tau_min':>8s} {'S_min':>10s} {'S_bdy_max':>10s} "
      f"{'barrier%':>10s} {'interior':>8s}")
print("-" * 60)
for i in range(n_alpha):
    print(f"{alpha_values[i]:8.1f} {tau_min_p[i]:8.4f} {S_min_p[i]:10.6f} "
          f"{S_bdy_p[i]:10.6f} {barrier_p[i]*100:10.4f} {'YES' if has_min_p[i] else 'NO':>8s}")

print("\n── Barrier analysis (fine sweep) ──")
tau_min_f, barrier_f, S_min_f, S_bdy_f, has_min_f = analyze_barrier(
    S_occ_fine, alpha_fine, tau_values)

# Find critical alpha where barrier first exceeds 0.1%
threshold = 0.001  # 0.1% (local)
above_threshold = np.where(barrier_f > threshold)[0]
if len(above_threshold) > 0:
    alpha_c_idx = above_threshold[0]
    alpha_c = alpha_fine[alpha_c_idx]
    print(f"\nCritical alpha_c (barrier > 0.1%): {alpha_c:.3f}")
    print(f"  barrier at alpha_c: {barrier_f[alpha_c_idx]*100:.4f}%")
    print(f"  tau_min at alpha_c: {tau_min_f[alpha_c_idx]:.4f}")
else:
    alpha_c = None
    print("\nNo alpha found with barrier > 0.1%")

# Find where barrier first exceeds 1%
threshold_1pct = 0.01  # (local)
above_1pct = np.where(barrier_f > threshold_1pct)[0]
if len(above_1pct) > 0:
    alpha_1pct = alpha_fine[above_1pct[0]]
    print(f"Critical alpha (barrier > 1%): {alpha_1pct:.3f}")
    print(f"  barrier: {barrier_f[above_1pct[0]]*100:.4f}%")
else:
    alpha_1pct = None
    print("No alpha found with barrier > 1%")

# Max barrier
max_barrier_idx = np.argmax(barrier_f)
print(f"\nMax barrier: {barrier_f[max_barrier_idx]*100:.4f}% at alpha={alpha_fine[max_barrier_idx]:.2f}")
print(f"  tau_min at max barrier: {tau_min_f[max_barrier_idx]:.4f}")

# ── Verify sharp-cutoff limit ────────────────────────────────────────
# At alpha=1000, should approximate Theta function
print("\n── Sharp cutoff verification ──")
# Compare alpha=1000 with actual sharp cutoff
S_sharp = np.zeros(n_tau)
for t in range(n_tau):
    E_k = eigenvalues[t, :]
    n_k = occ_bcs[t, :]
    mask = (E_k**2 / Lambda**2) < 1.0  # sharp step
    S_sharp[t] = np.sum(n_k[mask])

diff_sharp = np.max(np.abs(S_occ_primary[-1, :] - S_sharp))
print(f"Max |S_occ(alpha=1000) - S_occ(sharp)| = {diff_sharp:.2e}")

# ── Smooth limit analysis ────────────────────────────────────────────
print("\n── Smooth limit (small alpha) ──")
# At alpha=0.5, f_alpha ≈ 1/(1+exp(0.5*(x-1))) ≈ smooth
# Check if curve is monotonic
for i, alpha in enumerate(alpha_values):
    curve = S_occ_primary[i, :]
    diffs = np.diff(curve)
    n_sign_changes = np.sum(np.abs(np.diff(np.sign(diffs[diffs != 0]))) > 0)
    is_mono = (np.all(diffs >= 0) or np.all(diffs <= 0))
    print(f"  alpha={alpha:7.1f}: monotonic={is_mono}, sign_changes={n_sign_changes}, "
          f"range=[{curve.min():.6f}, {curve.max():.6f}]")

# ── Detailed look at minimum formation ───────────────────────────────
print("\n── Minimum formation analysis ──")
for i, alpha in enumerate(alpha_values):
    curve = S_occ_primary[i, :]
    idx_min = np.argmin(curve)
    idx_max = np.argmax(curve)
    # Check for interior local minima
    interior_mins = []
    for j in range(1, n_tau - 1):
        if curve[j] < curve[j-1] and curve[j] < curve[j+1]:
            interior_mins.append((j, tau_values[j], curve[j]))
    if interior_mins:
        for (j, tau_j, s_j) in interior_mins:
            depth = (max(curve[0], curve[-1]) - s_j) / s_j * 100
            print(f"  alpha={alpha:7.1f}: LOCAL MIN at tau={tau_j:.4f}, "
                  f"S={s_j:.6f}, depth={depth:.3f}%")
    else:
        trend = "decreasing" if curve[-1] < curve[0] else "increasing"
        print(f"  alpha={alpha:7.1f}: no interior minimum ({trend})")

# ── tau_min tracking Lambda check ────────────────────────────────────
print("\n── tau_min(alpha) tracking analysis ──")
# The question: does the minimum location shift with alpha?
# If barrier is a cutoff artifact, tau_min should shift systematically
interior_alphas = alpha_fine[has_min_f]
interior_taus = tau_min_f[has_min_f]
if len(interior_alphas) > 1:
    print(f"  Interior minima found for {len(interior_alphas)} of {len(alpha_fine)} alpha values")
    print(f"  alpha range with minima: [{interior_alphas[0]:.2f}, {interior_alphas[-1]:.2f}]")
    print(f"  tau_min range: [{interior_taus.min():.4f}, {interior_taus.max():.4f}]")
    # Correlation
    if len(interior_alphas) > 2:
        log_alpha = np.log(interior_alphas)
        corr = np.corrcoef(log_alpha, interior_taus)[0, 1]
        print(f"  Correlation(ln(alpha), tau_min) = {corr:.4f}")
else:
    print("  Too few interior minima for tracking analysis")

# ── Save results ──────────────────────────────────────────────────────
np.savez('computations/session-55/s55_cutoff_family.npz',
    alpha_primary=alpha_values,
    alpha_fine=alpha_fine,
    tau_values=tau_values,
    S_occ_primary=S_occ_primary,
    S_occ_fine=S_occ_fine,
    barrier_primary=barrier_p,
    barrier_fine=barrier_f,
    tau_min_primary=tau_min_p,
    tau_min_fine=tau_min_f,
    has_interior_min_primary=has_min_p,
    has_interior_min_fine=has_min_f,
    S_min_primary=S_min_p,
    S_boundary_max_primary=S_bdy_p,
    alpha_c_01pct=alpha_c if alpha_c else 0.0,
    alpha_c_1pct=alpha_1pct if alpha_1pct else 0.0,
    max_barrier_pct=barrier_f[max_barrier_idx]*100,
    max_barrier_alpha=alpha_fine[max_barrier_idx],
    Lambda=Lambda,
    Delta_primary=Delta_primary,
    gate_name='CUTOFF-FAMILY-55',
    gate_verdict='INFO',
    gate_detail='Fermi-Dirac cutoff family sensitivity study'
)
print("\nSaved: computations/session-55/s55_cutoff_family.npz")

# ── Plotting ──────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('CUTOFF-FAMILY-55: Fermi-Dirac Cutoff Sensitivity\n'
             r'$f_\alpha(x) = 1/(1 + e^{\alpha(x-1)})$, $\Lambda = 1.0\,M_{KK}$',
             fontsize=13, fontweight='bold')

# Panel (a): S_occ(tau) for representative alpha values
ax = axes[0, 0]
# Pick representative subset
repr_indices = [0, 2, 4, 6, 8, 10]  # alpha = 0.5, 2, 10, 50, 200, 1000
cmap = plt.cm.viridis(np.linspace(0, 0.9, len(repr_indices)))
for ci, i in enumerate(repr_indices):
    label = rf'$\alpha = {alpha_values[i]:.0f}$' if alpha_values[i] >= 1 else rf'$\alpha = {alpha_values[i]:.1f}$'
    ax.plot(tau_values, S_occ_primary[i, :], color=cmap[ci], label=label, linewidth=1.5)
# Also plot sharp cutoff for reference
ax.plot(tau_values, S_sharp, 'k--', linewidth=1.0, alpha=0.5, label='Sharp (exact)')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S_{\mathrm{occ}}(\tau;\alpha)$')
ax.set_title('(a) S_occ curves')
ax.legend(fontsize=8, loc='best')
ax.grid(True, alpha=0.3)

# Panel (b): Barrier height vs alpha
ax = axes[0, 1]
# Fine sweep
ax.semilogx(alpha_fine, barrier_f * 100, 'b-', linewidth=1.0, alpha=0.7, label='Fine sweep')
# Primary points
ax.semilogx(alpha_values, barrier_p * 100, 'ro', markersize=6, zorder=5, label='Primary points')
# Threshold lines
ax.axhline(0.1, color='orange', linestyle='--', alpha=0.5, label='0.1% threshold')
ax.axhline(1.0, color='red', linestyle='--', alpha=0.5, label='1% threshold')
if alpha_c is not None:
    ax.axvline(alpha_c, color='green', linestyle=':', alpha=0.7,
               label=rf'$\alpha_c = {alpha_c:.1f}$ (0.1%)')
ax.set_xlabel(r'$\alpha$ (Fermi-Dirac steepness)')
ax.set_ylabel('Barrier height (%)')
ax.set_title(r'(b) Barrier height vs $\alpha$')
ax.legend(fontsize=8, loc='best')
ax.grid(True, alpha=0.3)
ax.set_xlim(0.3, 2500)

# Panel (c): tau_min vs alpha
ax = axes[1, 0]
# Fine sweep - only where interior min exists
mask_interior = has_min_f
if np.any(mask_interior):
    ax.semilogx(alpha_fine[mask_interior], tau_min_f[mask_interior], 'b.',
                markersize=2, alpha=0.5, label='Interior minima')
# Primary points
for i in range(n_alpha):
    color = 'red' if has_min_p[i] else 'gray'
    marker = 'o' if has_min_p[i] else 'x'
    label = 'Interior min' if (i == 0 and has_min_p[i]) else ('Endpoint min' if (i == 0 and not has_min_p[i]) else '')
    ax.semilogx(alpha_values[i], tau_min_p[i], marker, color=color, markersize=6,
                label=label if label else None)
ax.set_xlabel(r'$\alpha$ (Fermi-Dirac steepness)')
ax.set_ylabel(r'$\tau_{\min}$')
ax.set_title(r'(c) Location of minimum vs $\alpha$')
ax.legend(fontsize=8, loc='best')
ax.grid(True, alpha=0.3)
ax.set_xlim(0.3, 2500)

# Panel (d): The cutoff function f_alpha for several alpha values
ax = axes[1, 1]
x = np.linspace(0, 3, 500)
alphas_show = [0.5, 2, 10, 50, 200, 1000]
cmap2 = plt.cm.viridis(np.linspace(0, 0.9, len(alphas_show)))
for ci, alpha in enumerate(alphas_show):
    label = rf'$\alpha = {alpha:.0f}$' if alpha >= 1 else rf'$\alpha = {alpha:.1f}$'
    ax.plot(x, f_alpha(x, alpha), color=cmap2[ci], label=label, linewidth=1.5)
ax.axvline(1.0, color='k', linestyle=':', alpha=0.3)
ax.set_xlabel(r'$x = E_k^2 / \Lambda^2$')
ax.set_ylabel(r'$f_\alpha(x)$')
ax.set_title(r'(d) Cutoff functions $f_\alpha$')
ax.legend(fontsize=8, loc='best')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-55/s55_cutoff_family.png', dpi=150, bbox_inches='tight')
print("Saved: computations/session-55/s55_cutoff_family.png")

# ── Final summary ─────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("CUTOFF-FAMILY-55 SUMMARY")
print("=" * 70)
print(f"Cutoff function: f_alpha(x) = 1/(1 + exp(alpha*(x-1)))")
print(f"Lambda = {Lambda:.1f} M_KK, Delta_primary = {Delta_primary:.4f}")
print(f"Alpha range: [{alpha_fine[0]:.2f}, {alpha_fine[-1]:.2f}] ({len(alpha_fine)} fine values)")
print(f"")
print(f"Max barrier: {barrier_f[max_barrier_idx]*100:.3f}% at alpha = {alpha_fine[max_barrier_idx]:.1f}")
if alpha_c is not None:
    print(f"alpha_c (barrier > 0.1%): {alpha_c:.2f}")
else:
    print(f"alpha_c (barrier > 0.1%): NONE (barrier never exceeds 0.1%)")
if alpha_1pct is not None:
    print(f"alpha (barrier > 1%): {alpha_1pct:.2f}")
else:
    print(f"alpha (barrier > 1%): NONE")

# Interior minimum existence
n_with_min = np.sum(has_min_f)
n_total = len(alpha_fine)
print(f"\nInterior minima: {n_with_min}/{n_total} alpha values ({n_with_min/n_total*100:.1f}%)")
if n_with_min > 0:
    alpha_first_min = alpha_fine[has_min_f][0]
    alpha_last_min = alpha_fine[has_min_f][-1]
    print(f"  Alpha range with interior min: [{alpha_first_min:.2f}, {alpha_last_min:.2f}]")

print(f"\nSharp cutoff verification: |S(alpha=1000) - S(sharp)| = {diff_sharp:.2e}")
print("=" * 70)
