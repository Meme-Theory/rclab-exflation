#!/usr/bin/env python3
"""
s55_euclid.py — EUCLID-55: Euclidean Free Energy at Gibbons-Hawking Temperature

Computes F(tau, T_GH(tau)) = -T_GH(tau) * ln Z_BCS(tau, T_GH(tau))
where T_GH = H(tau)/(2*pi) is the Gibbons-Hawking temperature,
and Z_BCS = Prod_k (1 + exp(-E_k/T_GH)) for 8 BCS-active modes.

Gate: EUCLID-55
  PASS: minimum in [0.10, 0.30] with barrier > 1%
  FAIL: monotone or barrier < 0.1%

Data inputs:
  s54_tb_hamiltonian.npz — tau_values (50,), eigenvalues (50, 32)
  s54_scale_factor.npz   — tau (10,), H (10,), a (10,)
  s54_ed_sweep.npz       — tau_values (50,), E_sp_sweep (50, 8)

Author: Hawking-Theorist agent, S55
"""

import sys
import os
sys.path.insert(0, 'computations')
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Load data ──────────────────────────────────────────────────────────────

tb = np.load('computations/session-54/s54_tb_hamiltonian.npz')
sf = np.load('computations/session-54/s54_scale_factor.npz', allow_pickle=True)
ed = np.load('computations/session-54/s54_ed_sweep.npz', allow_pickle=True)

tau_50 = tb['tau_values']      # (50,), range [0, 0.5]
eig_32 = tb['eigenvalues']     # (50, 32)

tau_10 = sf['tau']             # (10,)
H_10   = sf['H']              # (10,)

E_sp   = ed['E_sp_sweep']     # (50, 8) — single-particle energies for BCS-active modes

print("="*70)
print("EUCLID-55: Euclidean Free Energy at Gibbons-Hawking Temperature")
print("="*70)

# ── Step 1: Interpolate H(tau) from 10 points to 50 points ────────────────

# CubicSpline interpolation of H(tau)
cs_H = CubicSpline(tau_10, H_10, bc_type='natural')
H_50 = cs_H(tau_50)

print(f"\nH(tau) interpolation:")
print(f"  Input:  {len(tau_10)} points, tau in [{tau_10[0]:.4f}, {tau_10[-1]:.4f}]")
print(f"  Output: {len(tau_50)} points, tau in [{tau_50[0]:.4f}, {tau_50[-1]:.4f}]")
print(f"  H range: [{H_50.min():.6f}, {H_50.max():.6f}]")

# Check: tau_50 extends beyond tau_10 range. Extrapolation needed.
tau_max_interp = tau_10[-1]
n_extrap = np.sum(tau_50 > tau_max_interp)
print(f"  Points requiring extrapolation (tau > {tau_max_interp:.4f}): {n_extrap}")
if n_extrap > 0:
    print(f"  WARNING: {n_extrap} points extrapolated beyond data range.")
    print(f"  Extrapolated H values: {H_50[tau_50 > tau_max_interp]}")
    # Clamp negative H values if extrapolation goes wild
    if np.any(H_50 < 0):
        print("  CLAMPING negative H values to 0.01")
        H_50 = np.maximum(H_50, 0.01)

# ── Step 2: Compute T_GH = H/(2*pi) ──────────────────────────────────────

T_GH = H_50 / (2.0 * np.pi)

print(f"\nGibbons-Hawking temperature T_GH = H/(2*pi):")
print(f"  T_GH range: [{T_GH.min():.6f}, {T_GH.max():.6f}] M_KK")

# ── Step 3: Compute BCS partition function and free energy ─────────────────

# Use E_sp_sweep (50, 8) — single-particle energies of 8 BCS-active modes
# These are ALREADY the single-particle energies (relative to Fermi level)
# Z = Prod_k (1 + exp(-E_k/T_GH)) for each mode k

print(f"\nBCS partition function:")
print(f"  Using E_sp_sweep: shape {E_sp.shape}")
print(f"  E_sp range: [{E_sp.min():.6e}, {E_sp.max():.6f}]")

# The first mode at each tau is ~0 (Fermi level). This is the BCS condensate mode.
# For partition function: Z_k = 1 + exp(-E_k/T)
# F = -T * sum_k ln(1 + exp(-E_k/T))

# Compute ln Z = sum_k ln(1 + exp(-E_k/T_GH))
# Use log1p for numerical stability when E_k/T is large

ln_Z = np.zeros(50)
F_euclid = np.zeros(50)
S_BCS = np.zeros(50)   # entropy as cross-check
n_occ = np.zeros((50, 8))  # Fermi-Dirac occupations

for i in range(50):
    T = T_GH[i]
    if T < 1e-15:
        ln_Z[i] = 0.0
        F_euclid[i] = 0.0
        continue

    for k in range(8):
        E = E_sp[i, k]  # (local)
        ratio = E / T
        if ratio > 500:
            # exp(-ratio) ~ 0, ln(1 + exp(-ratio)) ~ exp(-ratio)
            ln_Z[i] += np.exp(-ratio)
            n_occ[i, k] = np.exp(-ratio)
        else:
            ln_Z[i] += np.log1p(np.exp(-ratio))
            n_occ[i, k] = 1.0 / (1.0 + np.exp(ratio))

    F_euclid[i] = -T * ln_Z[i]

    # Entropy: S = -sum_k [n_k ln n_k + (1-n_k) ln(1-n_k)]
    for k in range(8):
        nk = n_occ[i, k]
        if 0 < nk < 1:
            S_BCS[i] -= nk * np.log(nk) + (1 - nk) * np.log(1 - nk)

print(f"\n  ln Z range: [{ln_Z.min():.6f}, {ln_Z.max():.6f}]")
print(f"  F range: [{F_euclid.min():.6f}, {F_euclid.max():.6f}] M_KK")
print(f"  S_BCS range: [{S_BCS.min():.6f}, {S_BCS.max():.6f}]")

# ── Step 4: Analyze structure — search for extrema ────────────────────────

# Compute dF/dtau via finite differences
dF = np.gradient(F_euclid, tau_50)
d2F = np.gradient(dF, tau_50)

print(f"\n{'='*70}")
print(f"EXTREMUM ANALYSIS")
print(f"{'='*70}")

# Find sign changes of dF/dtau (zero crossings)
extrema = []
for i in range(len(dF) - 1):
    if dF[i] * dF[i+1] < 0:
        # Linear interpolation for zero crossing
        tau_cross = tau_50[i] - dF[i] * (tau_50[i+1] - tau_50[i]) / (dF[i+1] - dF[i])
        F_cross = np.interp(tau_cross, tau_50, F_euclid)
        d2F_cross = np.interp(tau_cross, tau_50, d2F)
        etype = "MINIMUM" if d2F_cross > 0 else "MAXIMUM"
        extrema.append({
            'tau': tau_cross,
            'F': F_cross,
            'd2F': d2F_cross,
            'type': etype,
            'idx': i
        })
        print(f"  {etype} at tau = {tau_cross:.6f}, F = {F_cross:.6f}, d2F = {d2F_cross:.4f}")

if len(extrema) == 0:
    print("  NO EXTREMA FOUND — F(tau) is monotone")

# Monotonicity check
is_monotone_increasing = np.all(dF > 0)
is_monotone_decreasing = np.all(dF < 0)
is_monotone = is_monotone_increasing or is_monotone_decreasing

print(f"\n  F monotonically increasing: {is_monotone_increasing}")
print(f"  F monotonically decreasing: {is_monotone_decreasing}")
print(f"  F is monotone: {is_monotone}")

# ── Step 5: Gate evaluation ───────────────────────────────────────────────

print(f"\n{'='*70}")
print(f"GATE EVALUATION: EUCLID-55")
print(f"{'='*70}")
print(f"  Criterion: PASS if minimum in [0.10, 0.30] with barrier > 1%")
print(f"             FAIL if monotone or barrier < 0.1%")

gate_pass = False
tau_min = None
barrier_height = None
barrier_frac = None

# Check for minimum in the target range
minima_in_range = [e for e in extrema if e['type'] == 'MINIMUM' and 0.10 <= e['tau'] <= 0.30]

if len(minima_in_range) > 0:
    best_min = min(minima_in_range, key=lambda e: e['F'])
    tau_min = best_min['tau']
    F_min = best_min['F']

    # Barrier height: max of F at boundaries minus F_min
    F_at_0 = F_euclid[0]
    F_at_05 = F_euclid[-1]
    F_boundary = max(F_at_0, F_at_05)

    # Also check for local maximum on either side
    maxima = [e for e in extrema if e['type'] == 'MAXIMUM']
    F_barrier_candidates = [F_boundary]
    for m in maxima:
        if m['tau'] < tau_min or m['tau'] > tau_min:
            F_barrier_candidates.append(m['F'])

    barrier_height = max(F_barrier_candidates) - F_min
    barrier_frac = abs(barrier_height / F_min) if abs(F_min) > 1e-15 else float('inf')

    print(f"\n  MINIMUM FOUND in [0.10, 0.30]:")
    print(f"    tau_min = {tau_min:.6f}")
    print(f"    F_min = {F_min:.6f} M_KK")
    print(f"    F(tau=0) = {F_at_0:.6f} M_KK")
    print(f"    F(tau=0.5) = {F_at_05:.6f} M_KK")
    print(f"    Barrier height = {barrier_height:.6f} M_KK")
    print(f"    Barrier/|F_min| = {barrier_frac:.4f} = {barrier_frac*100:.2f}%")

    if barrier_frac > 0.01:
        gate_pass = True
        verdict = "PASS"
    elif barrier_frac > 0.001:
        verdict = "FAIL (barrier < 1%, > 0.1%)"
    else:
        verdict = "FAIL (barrier < 0.1%)"
else:
    if is_monotone:
        verdict = "FAIL (monotone)"
    else:
        verdict = "FAIL (no minimum in [0.10, 0.30])"
        # Report what was found
        for e in extrema:
            print(f"    Found {e['type']} at tau={e['tau']:.4f} (outside target range)")

print(f"\n  VERDICT: {verdict}")

# ── Step 6: Cross-checks ──────────────────────────────────────────────────

print(f"\n{'='*70}")
print(f"CROSS-CHECKS")
print(f"{'='*70}")

# Cross-check 1: Thermodynamic consistency — F = E - TS
# At T_GH, the average energy is E = sum_k E_k * n_k
E_avg = np.sum(E_sp * n_occ, axis=1)
F_check = E_avg - T_GH * S_BCS
F_discrepancy = np.max(np.abs(F_euclid - F_check))
print(f"  1. Thermodynamic consistency |F - (E - TS)|_max = {F_discrepancy:.2e}")

# Cross-check 2: Limiting behavior at tau=0
print(f"  2. F(tau=0) = {F_euclid[0]:.6f} M_KK")
print(f"     T_GH(tau=0) = {T_GH[0]:.6f} M_KK")
print(f"     E_sp(tau=0) = {E_sp[0]}")

# Cross-check 3: T_GH at fold (tau ~ 0.19)
idx_fold = np.argmin(np.abs(tau_50 - 0.19))
print(f"  3. At fold (tau={tau_50[idx_fold]:.4f}):")
print(f"     T_GH = {T_GH[idx_fold]:.6f} M_KK")
print(f"     H = {H_50[idx_fold]:.6f} M_KK")
print(f"     F = {F_euclid[idx_fold]:.6f} M_KK")
print(f"     S_BCS = {S_BCS[idx_fold]:.6f}")

# Cross-check 4: Compare with canonical H_fold
from canonical_constants import H_fold, tau_fold
print(f"  4. Canonical H_fold = {H_fold:.4f} (from canonical_constants)")
print(f"     s54 H at fold = {H_50[idx_fold]:.4f}")
print(f"     Ratio s54/canonical = {H_50[idx_fold]/H_fold:.4e}")
print(f"     NOTE: s54 H is in LATTICE units (O(1)), canonical H_fold is in M_KK units (586.5)")
print(f"     These are different quantities — s54 is a lattice-scale Hubble-like parameter")

# Cross-check 5: Energy scale comparison
print(f"  5. Energy scales:")
print(f"     T_GH range: [{T_GH.min():.6f}, {T_GH.max():.6f}] (lattice units)")
print(f"     E_sp(k=1) range: [{E_sp[:,1].min():.4f}, {E_sp[:,1].max():.4f}]")
print(f"     Ratio T_GH/E_sp(k=1): [{(T_GH/E_sp[:,1]).min():.4f}, {(T_GH/E_sp[:,1]).max():.4f}]")
print(f"     ==> T_GH >> E_sp means high-T regime (all modes thermally populated)")

# Cross-check 6: Alternative — use 8 lowest eigenvalues from 32-cell spectrum
# (instead of E_sp_sweep) as consistency check
eig_8lowest = np.sort(eig_32, axis=1)[:, :8]
F_alt = np.zeros(50)
for i in range(50):
    T = T_GH[i]
    if T < 1e-15:
        continue
    for k in range(8):
        E = eig_8lowest[i, k]  # (local)
        ratio = E / T
        if ratio > 500:
            F_alt[i] -= T * np.exp(-ratio)
        else:
            F_alt[i] -= T * np.log1p(np.exp(-ratio))

F_diff_alt = np.max(np.abs(F_euclid - F_alt))
print(f"  6. Alternative (8 lowest of 32 eigenvalues):")
print(f"     |F_Esp - F_8lowest|_max = {F_diff_alt:.4e}")
print(f"     F_alt range: [{F_alt.min():.6f}, {F_alt.max():.6f}]")

# Cross-check 7: All 32 modes partition function
F_32 = np.zeros(50)
for i in range(50):
    T = T_GH[i]
    if T < 1e-15:
        continue
    for k in range(32):
        E = eig_32[i, k]  # (local)
        ratio = E / T
        if ratio > 500:
            F_32[i] -= T * np.exp(-ratio)
        else:
            F_32[i] -= T * np.log1p(np.exp(-ratio))

print(f"  7. Full 32-mode partition function:")
print(f"     F_32 range: [{F_32.min():.6f}, {F_32.max():.6f}]")

# ── Step 7: Detailed tabulation ───────────────────────────────────────────

print(f"\n{'='*70}")
print(f"TABULATION: F(tau) at selected points")
print(f"{'='*70}")
print(f"{'tau':>8s} {'H(tau)':>10s} {'T_GH':>10s} {'F(tau)':>12s} {'dF/dtau':>12s} {'S_BCS':>10s}")
print("-"*70)
for i in range(0, 50, 2):
    print(f"{tau_50[i]:8.4f} {H_50[i]:10.4f} {T_GH[i]:10.6f} {F_euclid[i]:12.6f} {dF[i]:12.6f} {S_BCS[i]:10.6f}")

# ── Step 8: Save data ────────────────────────────────────────────────────

np.savez('computations/session-55/s55_euclid.npz',
    tau_values=tau_50,
    H_interp=H_50,
    T_GH=T_GH,
    E_sp=E_sp,
    F_euclid=F_euclid,
    F_32mode=F_32,
    dF_dtau=dF,
    d2F_dtau2=d2F,
    ln_Z=ln_Z,
    S_BCS=S_BCS,
    n_occ=n_occ,
    E_avg=E_avg,
    gate_verdict=verdict,
    tau_min=tau_min if tau_min is not None else np.nan,
    barrier_height=barrier_height if barrier_height is not None else np.nan,
    barrier_frac=barrier_frac if barrier_frac is not None else np.nan,
)
print(f"\nData saved: computations/session-55/s55_euclid.npz")

# ── Step 9: Plot ─────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle(f'EUCLID-55: Euclidean Free Energy at Gibbons-Hawking Temperature\nVerdict: {verdict}',
             fontsize=14, fontweight='bold')

# Panel 1: F(tau) — the main result
ax = axes[0, 0]
ax.plot(tau_50, F_euclid, 'b-', linewidth=2, label='F(tau) [8 BCS modes]')
ax.plot(tau_50, F_32, 'r--', linewidth=1.5, alpha=0.7, label='F(tau) [all 32 modes]')
if tau_min is not None:
    ax.axvline(tau_min, color='green', linestyle=':', alpha=0.7, label=f'tau_min={tau_min:.3f}')
ax.axvline(0.19, color='gray', linestyle='--', alpha=0.5, label='fold (tau=0.19)')
ax.axvspan(0.10, 0.30, alpha=0.1, color='green', label='target [0.10, 0.30]')
ax.set_xlabel('tau')
ax.set_ylabel('F(tau) [M_KK]')
ax.set_title('Euclidean Free Energy')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: T_GH(tau) and H(tau)
ax = axes[0, 1]
ax.plot(tau_50, T_GH, 'r-', linewidth=2, label='T_GH = H/(2pi)')
ax.plot(tau_10, H_10/(2*np.pi), 'ko', markersize=6, label='T_GH (data points)')
ax2 = ax.twinx()
ax2.plot(tau_50, H_50, 'b--', linewidth=1.5, alpha=0.7, label='H(tau)')
ax.set_xlabel('tau')
ax.set_ylabel('T_GH [M_KK]', color='r')
ax2.set_ylabel('H(tau) [M_KK]', color='b')
ax.set_title('Gibbons-Hawking Temperature')
ax.legend(loc='upper left', fontsize=8)
ax2.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: dF/dtau
ax = axes[0, 2]
ax.plot(tau_50, dF, 'g-', linewidth=2)
ax.axhline(0, color='k', linestyle='-', alpha=0.3)
ax.axvspan(0.10, 0.30, alpha=0.1, color='green')
for e in extrema:
    color = 'red' if e['type'] == 'MINIMUM' else 'blue'
    ax.axvline(e['tau'], color=color, linestyle=':', alpha=0.7,
               label=f"{e['type']} tau={e['tau']:.3f}")
ax.set_xlabel('tau')
ax.set_ylabel('dF/dtau')
ax.set_title('Derivative of Free Energy')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: E_sp(tau) — single-particle energies
ax = axes[1, 0]
for k in range(8):
    ax.plot(tau_50, E_sp[:, k], linewidth=1.5, label=f'k={k}')
ax.axhline(T_GH[0], color='gray', linestyle='--', alpha=0.5, label=f'T_GH(0)={T_GH[0]:.3f}')
ax.set_xlabel('tau')
ax.set_ylabel('E_sp [M_KK]')
ax.set_title('Single-Particle Energies (8 BCS modes)')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 5: Occupation numbers
ax = axes[1, 1]
for k in range(8):
    ax.plot(tau_50, n_occ[:, k], linewidth=1.5, label=f'k={k}')
ax.set_xlabel('tau')
ax.set_ylabel('n_k (Fermi-Dirac)')
ax.set_title('Mode Occupations at T_GH')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 6: Entropy
ax = axes[1, 2]
ax.plot(tau_50, S_BCS, 'm-', linewidth=2, label='S_BCS')
ax.set_xlabel('tau')
ax.set_ylabel('S_BCS [nats]')
ax.set_title('BCS Entropy at T_GH')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-55/s55_euclid.png', dpi=150, bbox_inches='tight')
print(f"Plot saved: computations/session-55/s55_euclid.png")

# ── Final summary ────────────────────────────────────────────────────────

print(f"\n{'='*70}")
print(f"FINAL SUMMARY")
print(f"{'='*70}")
print(f"  Gate: EUCLID-55")
print(f"  Verdict: {verdict}")
print(f"  F(tau) range: [{F_euclid.min():.6f}, {F_euclid.max():.6f}]")
print(f"  T_GH range: [{T_GH.min():.6f}, {T_GH.max():.6f}]")
if tau_min is not None:
    print(f"  tau_min = {tau_min:.6f}")
    print(f"  Barrier height = {barrier_height:.6f}")
    print(f"  Barrier fraction = {barrier_frac:.4f} ({barrier_frac*100:.2f}%)")
else:
    print(f"  No minimum found in [0.10, 0.30]")
print(f"  Monotone: {is_monotone}")
print(f"  Number of extrema: {len(extrema)}")
for e in extrema:
    print(f"    {e['type']} at tau={e['tau']:.4f}, F={e['F']:.6f}")
