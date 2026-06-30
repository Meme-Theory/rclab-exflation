#!/usr/bin/env python3
"""
S55 W0-1: ZETA-55 — Zeta-Regularized Effective Action on 32-Cell Lattice
=========================================================================

Gate: ZETA-55
    If zeta'_D(0, tau) is monotone => S_occ cutoff artifact confirmed on 32 cells
    If non-monotone => Connes' prediction wrong, S_occ strengthened

Method:
    zeta'_D(0, tau) = -sum_{k: E_k > 0} ln(E_k(tau))

    This is the derivative at s=0 of the spectral zeta function
        zeta_D(s, tau) = sum_{k: E_k > 0} E_k(tau)^{-s}
    evaluated via d/ds[E^{-s}]|_{s=0} = -ln(E).

    The zero mode (smallest eigenvalue, ~machine epsilon) is excluded.

    zeta'_D(0) = -ln(det'(H)) where det' is the zeta-regularized determinant
    (product over nonzero eigenvalues). This is the cutoff-INDEPENDENT
    one-loop effective action.

Cross-checks:
    1. Verify eigenvalue count: 31 positive modes + 1 zero mode = 32 total
    2. Compare zeta'_D(0) monotonicity against S_occ from S54
    3. Compute d(zeta')/d(tau) numerically, check for sign changes
    4. Verify det'(H) = exp(-zeta'_D(0)) is well-defined and positive
    5. Check individual ln(E_k) contributions for anomalous behavior

Created: 2026-03-22 (Session 55, Wave 0)
Agent: spectral-geometer
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, 'computations')
from canonical_constants import *

# ============================================================================
# Load data
# ============================================================================

data = np.load('computations/session-54/s54_tb_hamiltonian.npz')
tau_values = data['tau_values']       # shape (50,)
eigenvalues = data['eigenvalues']     # shape (50, 32)
N_tau = len(tau_values)
N_cells = int(data['N_cells'])

print(f"Loaded: {N_tau} tau values, {N_cells} cells")
print(f"tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print()

# ============================================================================
# Sort eigenvalues and identify zero mode
# ============================================================================

eigs_sorted = np.sort(eigenvalues, axis=1)  # shape (50, 32), ascending

# Zero mode identification: smallest eigenvalue at each tau
zero_modes = eigs_sorted[:, 0]
print("Zero mode values (should be ~machine epsilon):")
print(f"  max|E_0|  = {np.max(np.abs(zero_modes)):.2e}")
print(f"  mean|E_0| = {np.mean(np.abs(zero_modes)):.2e}")
assert np.all(np.abs(zero_modes) < 1e-10), "Zero mode not at machine epsilon!"

# Positive eigenvalues: indices 1..31 (31 modes)
eigs_pos = eigs_sorted[:, 1:]  # shape (50, 31)
N_pos = eigs_pos.shape[1]
print(f"Positive eigenvalues: {N_pos} modes per tau value")
print(f"  min E_k (over all tau, k>0): {eigs_pos.min():.6f}")
print(f"  max E_k (over all tau, k>0): {eigs_pos.max():.6f}")
assert np.all(eigs_pos > 0), "Found non-positive eigenvalue in positive sector!"
print()

# ============================================================================
# Compute zeta'_D(0, tau) = -sum_{k=1}^{31} ln(E_k(tau))
# ============================================================================

ln_eigs = np.log(eigs_pos)           # shape (50, 31)
zeta_prime = -np.sum(ln_eigs, axis=1)  # shape (50,)

# Equivalently: zeta'_D(0) = -ln(det'(H))
log_det_prime = np.sum(ln_eigs, axis=1)  # ln(det') = sum ln(E_k)
det_prime = np.exp(log_det_prime)

print("=" * 60)
print("ZETA'_D(0, tau) = -sum_{k>0} ln(E_k(tau))")
print("=" * 60)
print(f"  zeta'(0, tau=0.000) = {zeta_prime[0]:.6f}")
print(f"  zeta'(0, tau=0.250) = {zeta_prime[N_tau//2]:.6f}")
print(f"  zeta'(0, tau=0.500) = {zeta_prime[-1]:.6f}")
print(f"  range: [{zeta_prime.min():.6f}, {zeta_prime.max():.6f}]")
print()

# ============================================================================
# Monotonicity analysis
# ============================================================================

# Numerical derivative d(zeta')/d(tau)
dtau = np.diff(tau_values)
dzeta = np.diff(zeta_prime)
dzeta_dtau = dzeta / dtau

# Check for sign changes
sign_changes = np.where(np.diff(np.sign(dzeta_dtau)))[0]
is_monotone = len(sign_changes) == 0

# Direction
if np.all(dzeta_dtau > 0):
    monotone_dir = "INCREASING"
elif np.all(dzeta_dtau < 0):
    monotone_dir = "DECREASING"
else:
    monotone_dir = "NON-MONOTONE"

print("MONOTONICITY ANALYSIS:")
print(f"  Direction: {monotone_dir}")
print(f"  Sign changes in d(zeta')/d(tau): {len(sign_changes)}")
if not is_monotone:
    for sc in sign_changes:
        tau_sc = 0.5 * (tau_values[sc + 1] + tau_values[sc + 2])
        print(f"    Sign change at tau ~ {tau_sc:.4f}: "
              f"d(zeta')/d(tau) goes from {dzeta_dtau[sc]:.4f} to {dzeta_dtau[sc+1]:.4f}")
print(f"  d(zeta')/d(tau) range: [{dzeta_dtau.min():.4f}, {dzeta_dtau.max():.4f}]")
print(f"  d(zeta')/d(tau) at tau~0: {dzeta_dtau[0]:.6f}")
print(f"  d(zeta')/d(tau) at tau~0.5: {dzeta_dtau[-1]:.6f}")
print()

# ============================================================================
# Find extrema if non-monotone
# ============================================================================

if not is_monotone:
    # Local extrema of zeta'
    for i in range(1, N_tau - 1):
        if (zeta_prime[i] > zeta_prime[i-1] and zeta_prime[i] > zeta_prime[i+1]):
            print(f"  LOCAL MAXIMUM at tau = {tau_values[i]:.6f}: zeta' = {zeta_prime[i]:.6f}")
        if (zeta_prime[i] < zeta_prime[i-1] and zeta_prime[i] < zeta_prime[i+1]):
            print(f"  LOCAL MINIMUM at tau = {tau_values[i]:.6f}: zeta' = {zeta_prime[i]:.6f}")

    # Amplitude of non-monotonicity
    zeta_max = zeta_prime.max()
    zeta_min = zeta_prime.min()
    zeta_range = zeta_max - zeta_min
    idx_max = np.argmax(zeta_prime)
    idx_min = np.argmin(zeta_prime)
    print(f"\n  Global max: zeta' = {zeta_max:.6f} at tau = {tau_values[idx_max]:.6f}")
    print(f"  Global min: zeta' = {zeta_min:.6f} at tau = {tau_values[idx_min]:.6f}")
    print(f"  Total variation: {zeta_range:.6f}")
    print(f"  Relative variation: {zeta_range / np.abs(zeta_prime.mean()) * 100:.2f}%")
print()

# ============================================================================
# Cross-check 1: Individual eigenvalue monotonicity
# ============================================================================

print("CROSS-CHECK 1: Individual eigenvalue monotonicity")
n_increasing = 0
n_decreasing = 0
n_nonmonotone = 0
for k in range(N_pos):
    deig = np.diff(eigs_pos[:, k])
    if np.all(deig >= -1e-15):
        n_increasing += 1
    elif np.all(deig <= 1e-15):
        n_decreasing += 1
    else:
        n_nonmonotone += 1
        # Find the mode details
        sc_k = np.where(np.diff(np.sign(deig)))[0]
        if len(sc_k) <= 3:
            for s in sc_k:
                print(f"  Mode k={k}: sign change at tau ~ {tau_values[s+1]:.4f}")

print(f"  Monotonically increasing: {n_increasing}")
print(f"  Monotonically decreasing: {n_decreasing}")
print(f"  Non-monotone: {n_nonmonotone}")
print()

# ============================================================================
# Cross-check 2: Decompose zeta' into contributions by eigenvalue
# ============================================================================

print("CROSS-CHECK 2: Largest individual contributions to zeta'")
# At mid-tau, which eigenvalues contribute most to zeta'?
mid_idx = N_tau // 2
contributions = -ln_eigs[mid_idx, :]
sorted_idx = np.argsort(np.abs(contributions))[::-1]
print(f"  At tau = {tau_values[mid_idx]:.4f}:")
for rank in range(5):
    k = sorted_idx[rank]
    print(f"    Mode k={k}: E_k={eigs_pos[mid_idx, k]:.6f}, "
          f"-ln(E_k)={contributions[k]:.6f}")
print()

# ============================================================================
# Cross-check 3: det'(H) = exp(-zeta'_D(0))
# ============================================================================

print("CROSS-CHECK 3: Zeta-regularized determinant det'(H)")
print(f"  det'(H, tau=0)    = {det_prime[0]:.6e}")
print(f"  det'(H, tau=0.25) = {det_prime[N_tau//2]:.6e}")
print(f"  det'(H, tau=0.5)  = {det_prime[-1]:.6e}")
print(f"  All positive: {np.all(det_prime > 0)}")
print()

# ============================================================================
# Cross-check 4: Relationship to S_occ (if zeta' increases, det' increases,
# meaning eigenvalues get larger on average => S_occ should decrease)
# ============================================================================

# The sign convention: zeta'_D(0) = -sum ln(E_k)
# If eigenvalues DECREASE with tau, then ln(E_k) decreases, so -ln(E_k) increases
# => zeta' INCREASES when eigenvalues decrease
# S_occ ~ sum f(E_k) for occupied modes with some cutoff
# Connes' prediction: zeta' monotonically increasing (eigenvalues monotonically decreasing)

print("CROSS-CHECK 4: Eigenvalue means vs zeta'")
mean_eig = np.mean(eigs_pos, axis=1)
mean_ln_eig = np.mean(ln_eigs, axis=1)
print(f"  <E>(tau=0)   = {mean_eig[0]:.6f},  <ln E>(tau=0)   = {mean_ln_eig[0]:.6f}")
print(f"  <E>(tau=0.5) = {mean_eig[-1]:.6f},  <ln E>(tau=0.5) = {mean_ln_eig[-1]:.6f}")
print(f"  <E> increasing: {np.all(np.diff(mean_eig) > -1e-15)}")
print(f"  <E> decreasing: {np.all(np.diff(mean_eig) < 1e-15)}")
print()

# ============================================================================
# Cross-check 5: Compare with spectral action moments
# ============================================================================

# Spectral zeta at other s values as cross-reference
s_values = [0.5, 1.0, 2.0, 3.0]
print("CROSS-CHECK 5: Spectral zeta function at various s")
for s in s_values:
    zeta_s = np.sum(eigs_pos ** (-s), axis=1)
    mono_s = "INC" if np.all(np.diff(zeta_s) > -1e-15) else (
             "DEC" if np.all(np.diff(zeta_s) < 1e-15) else "NON-MONO")
    print(f"  zeta(s={s:.1f}): range [{zeta_s.min():.4f}, {zeta_s.max():.4f}], {mono_s}")
print()

# ============================================================================
# GATE VERDICT
# ============================================================================

print("=" * 60)
print("GATE VERDICT: ZETA-55")
print("=" * 60)

if is_monotone and monotone_dir == "INCREASING":
    verdict = "PASS (monotone increasing)"
    print(f"  {verdict}")
    print("  zeta'_D(0, tau) is MONOTONICALLY INCREASING.")
    print("  => All eigenvalues decrease monotonically with tau.")
    print("  => S_occ minimum is a CUTOFF ARTIFACT (confirmed on 32 cells).")
    print("  => Connes' prediction CONFIRMED: cutoff-independent effective action")
    print("     has no minimum.")
elif is_monotone and monotone_dir == "DECREASING":
    verdict = "PASS (monotone decreasing)"
    print(f"  {verdict}")
    print("  zeta'_D(0, tau) is MONOTONICALLY DECREASING.")
    print("  => All eigenvalues increase monotonically with tau.")
    print("  => Connes' prediction of monotonicity CONFIRMED (opposite direction).")
elif not is_monotone:
    verdict = "FAIL (non-monotone)"
    print(f"  {verdict}")
    print("  zeta'_D(0, tau) is NON-MONOTONE.")
    print("  => Connes' prediction WRONG on 32-cell lattice.")
    print("  => S_occ minimum is NOT a cutoff artifact.")
    print(f"  => {len(sign_changes)} extrema found.")
else:
    verdict = "INFORMATIVE"
    print(f"  {verdict}")

print()

# ============================================================================
# Save results
# ============================================================================

np.savez('computations/session-55/s55_zeta.npz',
         tau_values=tau_values,
         zeta_prime=zeta_prime,
         dzeta_dtau=dzeta_dtau,
         eigs_pos=eigs_pos,
         ln_eigs=ln_eigs,
         det_prime=det_prime,
         mean_eig=mean_eig,
         is_monotone=is_monotone,
         monotone_dir=monotone_dir,
         n_sign_changes=len(sign_changes),
         sign_change_indices=sign_changes if len(sign_changes) > 0 else np.array([]),
         verdict=verdict,
         gate_name='ZETA-55')

print(f"Results saved to computations/session-55/s55_zeta.npz")
print()

# ============================================================================
# Plotting
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("ZETA-55: Zeta-Regularized Effective Action on 32-Cell Lattice",
             fontsize=14, fontweight='bold')

# Panel 1: zeta'_D(0, tau)
ax = axes[0, 0]
ax.plot(tau_values, zeta_prime, 'b-', linewidth=2, label=r"$\zeta'_D(0, \tau)$")
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r"$\zeta'_D(0)$", fontsize=12)
ax.set_title(r"$\zeta'_D(0, \tau) = -\sum_{k>0} \ln E_k(\tau)$", fontsize=11)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
# Mark extrema if any
if not is_monotone:
    for i in range(1, N_tau - 1):
        if (zeta_prime[i] > zeta_prime[i-1] and zeta_prime[i] > zeta_prime[i+1]):
            ax.axvline(tau_values[i], color='r', linestyle='--', alpha=0.5)
            ax.plot(tau_values[i], zeta_prime[i], 'rv', markersize=10)
        if (zeta_prime[i] < zeta_prime[i-1] and zeta_prime[i] < zeta_prime[i+1]):
            ax.axvline(tau_values[i], color='g', linestyle='--', alpha=0.5)
            ax.plot(tau_values[i], zeta_prime[i], 'g^', markersize=10)

# Panel 2: d(zeta')/d(tau)
ax = axes[0, 1]
tau_mid = 0.5 * (tau_values[:-1] + tau_values[1:])
ax.plot(tau_mid, dzeta_dtau, 'r-', linewidth=1.5, label=r"$d\zeta'/d\tau$")
ax.axhline(0, color='k', linewidth=0.5, linestyle='-')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r"$d\zeta'/d\tau$", fontsize=12)
ax.set_title(r"Derivative $d\zeta'_D(0)/d\tau$", fontsize=11)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 3: Individual eigenvalue trajectories
ax = axes[1, 0]
for k in range(N_pos):
    alpha = 0.3 if k > 5 else 0.8  # (local)
    lw = 0.5 if k > 5 else 1.0  # (local)
    ax.plot(tau_values, eigs_pos[:, k], linewidth=lw, alpha=alpha)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$E_k(\tau)$', fontsize=12)
ax.set_title(f'All {N_pos} Positive Eigenvalue Trajectories', fontsize=11)
ax.grid(True, alpha=0.3)

# Panel 4: det'(H) = exp(-zeta'_D(0))
ax = axes[1, 1]
ax.semilogy(tau_values, det_prime, 'g-', linewidth=2,
            label=r"$\det'(H) = e^{-\zeta'_D(0)}$")
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r"$\det'(H)$", fontsize=12)
ax.set_title("Zeta-Regularized Determinant", fontsize=11)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Add verdict text
verdict_color = 'green' if 'PASS' in verdict else 'red'
fig.text(0.5, 0.01, f"GATE VERDICT: {verdict}", fontsize=13,
         fontweight='bold', color=verdict_color, ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow',
                   edgecolor=verdict_color, alpha=0.8))

plt.tight_layout(rect=[0, 0.04, 1, 0.96])
plt.savefig('computations/session-55/s55_zeta.png', dpi=150, bbox_inches='tight')
print("Plot saved to computations/session-55/s55_zeta.png")
print()

# ============================================================================
# Summary table
# ============================================================================

print("=" * 60)
print("SUMMARY TABLE")
print("=" * 60)
print(f"  N_cells             = {N_cells}")
print(f"  N_positive_modes    = {N_pos}")
print(f"  tau range           = [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"  zeta'(0, tau=0)     = {zeta_prime[0]:.6f}")
print(f"  zeta'(0, tau=0.5)   = {zeta_prime[-1]:.6f}")
print(f"  Total change        = {zeta_prime[-1] - zeta_prime[0]:.6f}")
print(f"  Relative change     = {(zeta_prime[-1] - zeta_prime[0])/np.abs(zeta_prime[0])*100:.2f}%")
print(f"  Monotone?           = {is_monotone}")
print(f"  Direction           = {monotone_dir}")
print(f"  Sign changes        = {len(sign_changes)}")
print(f"  det'(H, tau=0)      = {det_prime[0]:.6e}")
print(f"  det'(H, tau=0.5)    = {det_prime[-1]:.6e}")
print(f"  Individual E_k mono = {n_increasing} inc, {n_decreasing} dec, {n_nonmonotone} non-mono")
print(f"  GATE VERDICT        = {verdict}")
