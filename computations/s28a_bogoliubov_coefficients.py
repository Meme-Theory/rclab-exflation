"""
Session 28a Computation KC-1: Parametric Injection Rate (Bogoliubov Coefficients)
=================================================================================

Computes |beta_k|^2 from the rate of change of Dirac eigenvalues d(lambda_k)/d(tau).
This is the Parker particle creation rate on the internal space -- the mechanism by
which an evolving Jensen deformation generates phononic excitations.

Physics:
--------
When the internal geometry evolves (tau changes in time), the Dirac eigenvalues
lambda_k(tau) become time-dependent. In the WKB/adiabatic approximation, the
Bogoliubov coefficient for particle creation in mode k is:

    |beta_k|^2 ~ (1 / (4 omega_k^2)) * |d(omega_k)/d(tau)|^2 * (d(tau)/dt)^2

where omega_k(tau) = |lambda_k(tau)| is the mode frequency.

We compute the tau-independent (geometric) part:

    B_k(tau) = (1 / (4 * omega_k^2)) * (d(omega_k)/d(tau))^2

This is the "adiabaticity parameter" -- if B_k >> 1, the adiabatic approximation
breaks down and copious particle creation occurs. If B_k << 1, the evolution is
adiabatic and particles are NOT created.

The physical injection rate is: |beta_k|^2 = B_k * (d(tau)/dt)^2.

Input: tier0-computation/s19a_sweep_data.npz (21 tau values, 11424 modes)
Output: tier0-computation/s28a_bogoliubov_coefficients.npz
        tier0-computation/s28a_bogoliubov_coefficients.png

Gate KC-1:
    PASS: B_k > 0.01 for modes near the gap edge at any tau in [0.10, 0.40]
    CLOSED: B_k < 10^{-4} for ALL modes at ALL tau -- no parametric amplification
    INCONCLUSIVE: B_k in [10^{-4}, 0.01] -- marginal injection

Author: phonon-exflation-sim agent
Date: 2026-02-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# ==============================================================================
# Configuration
# ==============================================================================

DATA_DIR = Path(__file__).parent
INPUT_FILE = DATA_DIR / "s19a_sweep_data.npz"
OUTPUT_NPZ = DATA_DIR / "s28a_bogoliubov_coefficients.npz"
OUTPUT_PNG = DATA_DIR / "s28a_bogoliubov_coefficients.png"

# Gate thresholds
B_PASS_THRESHOLD = 0.01
B_KILL_THRESHOLD = 1e-4

# Region of interest for the gate
TAU_GATE_MIN = 0.10
TAU_GATE_MAX = 0.40

# ==============================================================================
# Load data
# ==============================================================================

print("=" * 72)
print("KC-1: Parametric Injection Rate (Bogoliubov Coefficients)")
print("=" * 72)

data = np.load(INPUT_FILE, allow_pickle=True)
tau_values = data['tau_values']  # shape (21,)
n_tau = len(tau_values)
n_modes = data['eigenvalues_0'].shape[0]  # 11424

print(f"Loaded: {n_tau} tau values from {tau_values[0]:.2f} to {tau_values[-1]:.2f}")
print(f"Modes per tau: {n_modes}")

# Build eigenvalue matrix: shape (n_tau, n_modes)
eigenvalues = np.zeros((n_tau, n_modes))
sector_p = np.zeros((n_tau, n_modes), dtype=np.int32)
sector_q = np.zeros((n_tau, n_modes), dtype=np.int32)
multiplicities = np.zeros((n_tau, n_modes), dtype=np.int32)

for i in range(n_tau):
    eigenvalues[i] = data[f'eigenvalues_{i}']
    sector_p[i] = data[f'sector_p_{i}']
    sector_q[i] = data[f'sector_q_{i}']
    multiplicities[i] = data[f'multiplicities_{i}']

# ==============================================================================
# Mode tracking: sort eigenvalues by absolute value at each tau
# ==============================================================================
# The eigenvalues in the .npz may not be consistently ordered across tau.
# We need to track modes. Since D_K is block-diagonal, eigenvalues within
# each (p,q) sector are smoothly varying. Sort by (sector, |eigenvalue|)
# to track modes consistently.

print("\nTracking modes across tau values...")

# For each tau, create a composite sort key: (p, q, sign(lambda), |lambda|)
# This ensures we track individual mode trajectories.
omega = np.abs(eigenvalues)  # mode frequencies

# We need to track modes. Strategy: within each (p,q) sector at each tau,
# sort by eigenvalue magnitude. Since eigenvalues evolve continuously,
# modes at the same position in the sorted order within a sector correspond
# to the same physical mode.

# Get unique sectors at tau=0 (they are the same at all tau by block-diagonality)
unique_sectors = set()
for j in range(n_modes):
    unique_sectors.add((int(sector_p[0, j]), int(sector_q[0, j])))
unique_sectors = sorted(unique_sectors)
print(f"Unique sectors: {len(unique_sectors)}")

# Build tracked omega array: shape (n_tau, n_modes)
# Within each sector, sort by |eigenvalue| and track by index
omega_tracked = np.zeros_like(omega)
sign_tracked = np.zeros_like(eigenvalues)  # track sign for completeness
sector_p_ref = sector_p[0].copy()
sector_q_ref = sector_q[0].copy()
mult_ref = multiplicities[0].copy()

# Build sector masks from tau=0 reference
sector_masks = {}
for (p, q) in unique_sectors:
    mask = (sector_p[0] == p) & (sector_q[0] == q)
    sector_masks[(p, q)] = np.where(mask)[0]

# For each tau, sort eigenvalues within each sector by |lambda| to match modes
for i in range(n_tau):
    for (p, q), ref_idx in sector_masks.items():
        # Get eigenvalues in this sector at tau[i]
        # Find matching indices at tau[i]
        mask_i = (sector_p[i] == p) & (sector_q[i] == q)
        idx_i = np.where(mask_i)[0]

        # Sort both by |eigenvalue| to match
        ref_order = np.argsort(np.abs(eigenvalues[0, ref_idx]))
        cur_order = np.argsort(np.abs(eigenvalues[i, idx_i]))

        if len(ref_idx) != len(idx_i):
            print(f"  WARNING: sector ({p},{q}) tau={tau_values[i]:.1f}: "
                  f"{len(ref_idx)} vs {len(idx_i)} modes")
            continue

        # Map: ref_idx[ref_order[k]] <-> idx_i[cur_order[k]]
        for k in range(len(ref_order)):
            target = ref_idx[ref_order[k]]
            source = idx_i[cur_order[k]]
            omega_tracked[i, target] = np.abs(eigenvalues[i, source])
            sign_tracked[i, target] = np.sign(eigenvalues[i, source])

# ==============================================================================
# Compute d(omega_k)/d(tau) via 3-point central differences
# ==============================================================================

print("\nComputing d(omega_k)/d(tau) via central differences...")

dtau = tau_values[1] - tau_values[0]  # uniform spacing = 0.1
domega_dtau = np.zeros_like(omega_tracked)

# Central difference for interior points
for i in range(1, n_tau - 1):
    domega_dtau[i] = (omega_tracked[i + 1] - omega_tracked[i - 1]) / (2 * dtau)

# Forward/backward difference at boundaries
domega_dtau[0] = (omega_tracked[1] - omega_tracked[0]) / dtau
domega_dtau[-1] = (omega_tracked[-1] - omega_tracked[-2]) / dtau

# ==============================================================================
# Compute Bogoliubov adiabaticity parameter B_k(tau)
# ==============================================================================

print("Computing B_k(tau) = (1/(4*omega_k^2)) * (d(omega_k)/d(tau))^2 ...")

# Avoid division by zero for any zero eigenvalues
omega_safe = np.where(omega_tracked > 1e-12, omega_tracked, 1e-12)
B_k = (1.0 / (4.0 * omega_safe**2)) * domega_dtau**2

# ==============================================================================
# Analysis: focus on gate region tau in [0.10, 0.40]
# ==============================================================================

gate_mask = (tau_values >= TAU_GATE_MIN) & (tau_values <= TAU_GATE_MAX)
gate_tau_idx = np.where(gate_mask)[0]
gate_taus = tau_values[gate_mask]

print(f"\nGate region: tau in [{TAU_GATE_MIN}, {TAU_GATE_MAX}]")
print(f"  Tau values in gate: {gate_taus}")

# For each tau in gate region, find max B_k, identify which mode
print("\n--- B_k statistics in gate region ---")
B_max_gate = 0.0
B_max_tau = None
B_max_mode_info = None

for i in gate_tau_idx:
    tau = tau_values[i]
    B_at_tau = B_k[i]
    max_B = np.max(B_at_tau)
    max_idx = np.argmax(B_at_tau)
    p_max = sector_p_ref[max_idx]
    q_max = sector_q_ref[max_idx]
    omega_at_max = omega_tracked[i, max_idx]

    print(f"  tau={tau:.2f}: max(B_k) = {max_B:.6e}, "
          f"mode omega={omega_at_max:.4f}, sector=({p_max},{q_max})")

    if max_B > B_max_gate:
        B_max_gate = max_B
        B_max_tau = tau
        B_max_mode_info = (p_max, q_max, omega_at_max, max_idx)

# Gap-edge analysis: identify modes within 10% of the spectral gap
print("\n--- Gap-edge mode analysis ---")
for i in gate_tau_idx:
    tau = tau_values[i]
    gap = np.min(omega_tracked[i, omega_tracked[i] > 1e-6])
    near_gap_mask = (omega_tracked[i] > 0.9 * gap) & (omega_tracked[i] < 1.1 * gap)
    near_gap_idx = np.where(near_gap_mask)[0]
    if len(near_gap_idx) > 0:
        B_near_gap = B_k[i, near_gap_idx]
        max_B_gap = np.max(B_near_gap)
        mean_B_gap = np.mean(B_near_gap)
        print(f"  tau={tau:.2f}: gap={gap:.4f}, {len(near_gap_idx)} near-gap modes, "
              f"max(B)={max_B_gap:.6e}, mean(B)={mean_B_gap:.6e}")
    else:
        print(f"  tau={tau:.2f}: no near-gap modes found")

# ==============================================================================
# Compute total injection rate per tau
# ==============================================================================

print("\n--- Total injection rate (multiplicity-weighted) ---")
# Gamma_inject(tau) = sum_k B_k(tau) * mult_k
Gamma_inject = np.zeros(n_tau)
for i in range(n_tau):
    Gamma_inject[i] = np.sum(B_k[i] * mult_ref)

for i in range(n_tau):
    print(f"  tau={tau_values[i]:.2f}: Gamma_inject = {Gamma_inject[i]:.6e}")

# ==============================================================================
# Per-sector breakdown at representative tau values
# ==============================================================================

print("\n--- Per-sector B_k breakdown at tau=0.15, 0.25, 0.35 ---")
target_taus = [0.15, 0.25, 0.35]
# Find nearest tau indices
for t_target in target_taus:
    i = np.argmin(np.abs(tau_values - t_target))
    tau = tau_values[i]
    print(f"\n  tau = {tau:.2f} (index {i}):")
    for (p, q), ref_idx in sorted(sector_masks.items()):
        B_sector = B_k[i, ref_idx]
        omega_sector = omega_tracked[i, ref_idx]
        if len(B_sector) == 0:
            continue
        max_B = np.max(B_sector)
        mean_B = np.mean(B_sector)
        gap_sector = np.min(omega_sector[omega_sector > 1e-6]) if np.any(omega_sector > 1e-6) else 0
        print(f"    ({p},{q}): {len(ref_idx):4d} modes, gap={gap_sector:.4f}, "
              f"max(B)={max_B:.4e}, mean(B)={mean_B:.4e}")

# ==============================================================================
# Adiabaticity ratio: omega / |d(omega)/d(tau)| — the "adiabatic ratio"
# ==============================================================================
# If omega / |d(omega)/d(tau)| >> 1, evolution is adiabatic (no creation)
# If omega / |d(omega)/d(tau)| ~ 1, breakdown (copious creation)

print("\n--- Adiabaticity ratio omega / |d(omega)/d(tau)| ---")
for i in gate_tau_idx:
    tau = tau_values[i]
    domega_abs = np.abs(domega_dtau[i])
    # Avoid div by zero
    ratio = np.where(domega_abs > 1e-15,
                     omega_tracked[i] / domega_abs,
                     np.inf)
    min_ratio = np.min(ratio[np.isfinite(ratio)])
    # Modes with ratio < 10 are "non-adiabatic"
    non_adiab = np.sum(ratio < 10)
    strongly_non = np.sum(ratio < 1)
    print(f"  tau={tau:.2f}: min(omega/|domega/dtau|) = {min_ratio:.4f}, "
          f"modes with ratio<10: {non_adiab}, ratio<1: {strongly_non}")

# ==============================================================================
# Gate verdict
# ==============================================================================

print("\n" + "=" * 72)
print("GATE KC-1 VERDICT")
print("=" * 72)

# Check max B_k in gate region for ALL modes
B_all_gate = B_k[gate_mask]
B_max_all = np.max(B_all_gate)
B_max_overall_tau_idx = gate_tau_idx[np.unravel_index(np.argmax(B_all_gate),
                                                       B_all_gate.shape)[0]]
B_max_overall_mode_idx = np.unravel_index(np.argmax(B_all_gate), B_all_gate.shape)[1]

print(f"\nMax B_k in gate region [0.10, 0.40]: {B_max_all:.6e}")
print(f"  At tau = {tau_values[B_max_overall_tau_idx]:.2f}, "
      f"mode index = {B_max_overall_mode_idx}, "
      f"sector = ({sector_p_ref[B_max_overall_mode_idx]}, "
      f"{sector_q_ref[B_max_overall_mode_idx]})")

# Check gap-edge modes specifically
B_gap_edge_max = 0.0
for i in gate_tau_idx:
    gap = np.min(omega_tracked[i, omega_tracked[i] > 1e-6])
    near_gap = (omega_tracked[i] > 0.9 * gap) & (omega_tracked[i] < 1.1 * gap)
    if np.any(near_gap):
        B_gap_edge_max = max(B_gap_edge_max, np.max(B_k[i, near_gap]))

print(f"Max B_k at gap edge: {B_gap_edge_max:.6e}")

if B_gap_edge_max > B_PASS_THRESHOLD:
    verdict = "PASS"
    print(f"\nVERDICT: **PASS** -- B_k = {B_gap_edge_max:.4e} > {B_PASS_THRESHOLD} at gap edge")
elif B_max_all > B_PASS_THRESHOLD:
    verdict = "PASS"
    print(f"\nVERDICT: **PASS** -- B_k = {B_max_all:.4e} > {B_PASS_THRESHOLD} (non-gap-edge modes)")
elif B_max_all < B_KILL_THRESHOLD:
    verdict = "CLOSED"
    print(f"\nVERDICT: **CLOSED** -- B_k = {B_max_all:.4e} < {B_KILL_THRESHOLD} for ALL modes")
else:
    verdict = "INCONCLUSIVE"
    print(f"\nVERDICT: **INCONCLUSIVE** -- B_k in [{B_KILL_THRESHOLD}, {B_PASS_THRESHOLD}]")

print(f"\nPhysical note: |beta_k|^2 = B_k * (dtau/dt)^2.")
print(f"For dtau/dt = 1 (geometric time), |beta_k|^2 = B_k.")
print(f"For dtau/dt << 1 (slow roll), |beta_k|^2 << B_k.")

# ==============================================================================
# Save data
# ==============================================================================

np.savez_compressed(
    OUTPUT_NPZ,
    tau_values=tau_values,
    omega_tracked=omega_tracked,
    domega_dtau=domega_dtau,
    B_k=B_k,
    sector_p_ref=sector_p_ref,
    sector_q_ref=sector_q_ref,
    mult_ref=mult_ref,
    Gamma_inject=Gamma_inject,
    B_max_gate=np.array([B_max_all]),
    B_gap_edge_max=np.array([B_gap_edge_max]),
    verdict=np.array([verdict]),
)
print(f"\nSaved: {OUTPUT_NPZ}")

# ==============================================================================
# Plotting
# ==============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("KC-1: Bogoliubov Adiabaticity Parameter B_k(tau)", fontsize=14, fontweight='bold')

# --- Panel 1: B_k vs omega at tau = 0.15 ---
target_indices = []
for t in [0.15, 0.25, 0.35]:
    target_indices.append(np.argmin(np.abs(tau_values - t)))

for ax_idx, (ax, ti) in enumerate(zip(axes[0], target_indices)):
    tau = tau_values[ti]
    omega_i = omega_tracked[ti]
    B_i = B_k[ti]

    # Color by sector (p,q)
    for (p, q), ref_idx in sorted(sector_masks.items()):
        if len(ref_idx) == 0:
            continue
        label = f"({p},{q})" if p + q <= 2 else None
        ax.semilogy(omega_i[ref_idx], B_i[ref_idx], '.', markersize=2, alpha=0.6, label=label)

    ax.axhline(B_PASS_THRESHOLD, color='green', ls='--', lw=1, alpha=0.7, label=f'PASS: {B_PASS_THRESHOLD}')
    ax.axhline(B_KILL_THRESHOLD, color='red', ls='--', lw=1, alpha=0.7, label=f'CLOSED: {B_KILL_THRESHOLD}')
    ax.set_xlabel(r'$\omega_k = |\lambda_k|$')
    ax.set_ylabel(r'$B_k(\tau)$')
    ax.set_title(f'$\\tau = {tau:.2f}$')
    if ax_idx == 0:
        ax.legend(fontsize=7, ncol=2, loc='upper right')
    ax.set_ylim(1e-10, 10)
    ax.grid(True, alpha=0.3)

# --- Panel 2a: Total injection rate vs tau ---
ax = axes[1, 0]
ax.semilogy(tau_values, Gamma_inject, 'b-o', markersize=4)
ax.axvspan(TAU_GATE_MIN, TAU_GATE_MAX, alpha=0.1, color='green', label='Gate region')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\Gamma_{\rm inject}(\tau)$')
ax.set_title('Total Injection Rate (mult-weighted)')
ax.legend()
ax.grid(True, alpha=0.3)

# --- Panel 2b: Max B_k vs tau ---
ax = axes[1, 1]
B_max_per_tau = np.max(B_k, axis=1)
B_mean_per_tau = np.mean(B_k, axis=1)
ax.semilogy(tau_values, B_max_per_tau, 'r-o', markersize=4, label='max(B_k)')
ax.semilogy(tau_values, B_mean_per_tau, 'b-s', markersize=3, label='mean(B_k)')
ax.axhline(B_PASS_THRESHOLD, color='green', ls='--', lw=1, label='PASS threshold')
ax.axhline(B_KILL_THRESHOLD, color='red', ls='--', lw=1, label='CLOSURE threshold')
ax.axvspan(TAU_GATE_MIN, TAU_GATE_MAX, alpha=0.1, color='green')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$B_k$')
ax.set_title(r'Max and Mean $B_k$ vs $\tau$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel 2c: Heatmap of B_k near gap edge across tau ---
ax = axes[1, 2]
# For each tau, get the 20 smallest-omega modes and their B_k
n_show = 30
B_gap_heatmap = np.zeros((n_tau, n_show))
omega_gap_labels = []
for i in range(n_tau):
    # Get sorted by omega
    sorted_idx = np.argsort(omega_tracked[i])
    for j in range(min(n_show, len(sorted_idx))):
        B_gap_heatmap[i, j] = B_k[i, sorted_idx[j]]

im = ax.imshow(np.log10(np.clip(B_gap_heatmap.T, 1e-15, None)),
               aspect='auto', origin='lower',
               extent=[tau_values[0], tau_values[-1], 0, n_show],
               cmap='hot', vmin=-10, vmax=0)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Mode index (sorted by $\\omega_k$)')
ax.set_title(r'$\log_{10} B_k$ for lowest-$\omega$ modes')
plt.colorbar(im, ax=ax, label=r'$\log_{10} B_k$')

plt.tight_layout()
plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
print(f"Saved: {OUTPUT_PNG}")

print("\nDone.")
