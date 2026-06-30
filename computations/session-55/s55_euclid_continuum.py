#!/usr/bin/env python3
"""
s55_euclid_continuum.py — EUCLID-CONTINUUM-55: Euclidean Free Energy on 992-Mode Continuum

Repeats the EUCLID-55 computation (which PASSED on the 32-cell lattice with tau_min=0.220,
30% barrier) on the full 992-mode continuum spectrum from the Dirac operator on SU(3).

Physical content:
  F(tau, T_GH) = -T_GH(tau) * ln Z(tau, T_GH(tau))
  where T_GH = H(tau)/(2*pi) is the Gibbons-Hawking temperature,
  and ln Z = sum_{i=1}^{992} dim(p_i,q_i)^2 * ln(1 + exp(-omega_i/T_GH))

The dim^2 factor accounts for the SU(3) representation multiplicity:
each distinct Dirac eigenvalue in sector (p,q) has dim(p,q)^2 physical degrees of freedom.
Total physical modes: sum dim^2 = 101,984 (vs 32 on the lattice).

Data sources:
  s44_dos_tau.npz      — 992-mode spectrum at tau = [0.00, 0.05, 0.10, 0.15, 0.19]
  s27_multisector_bcs.npz — per-sector eigenvalues at tau = [0.00, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]
  s54_scale_factor.npz — H(tau) from the lattice scale factor
  s55_euclid.npz       — lattice EUCLID-55 results for comparison

Gate: EUCLID-CONTINUUM-55
  PASS: barrier on continuum exceeds barrier on 32-cell lattice
  FAIL: barrier weaker or no minimum

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
from canonical_constants import *

print("=" * 70)
print("EUCLID-CONTINUUM-55: Euclidean Free Energy on 992-Mode Continuum")
print("=" * 70)

# ── Load data ──────────────────────────────────────────────────────────────

d44 = np.load('computations/session-44/s44_dos_tau.npz')
d27 = np.load('computations/session-27/s27_multisector_bcs.npz')
sf  = np.load('computations/session-54/s54_scale_factor.npz', allow_pickle=True)
d55 = np.load('computations/session-55/s55_euclid.npz', allow_pickle=True)

# Scale factor data
tau_sf = sf['tau']   # (10,)
H_sf   = sf['H']    # (10,)

# Lattice results for comparison
tau_lattice = d55['tau_values']    # (50,)
F_lattice_8 = d55['F_euclid']     # (50,) — 8 BCS modes
F_lattice_32 = d55['F_32mode']    # (50,) — all 32 modes
T_GH_lattice = d55['T_GH']       # (50,)
tau_min_lattice = float(d55['tau_min'])
barrier_frac_lattice = float(d55['barrier_frac'])

print(f"\nLattice EUCLID-55 reference:")
print(f"  tau_min = {tau_min_lattice:.4f}")
print(f"  barrier_frac = {barrier_frac_lattice:.4f} ({barrier_frac_lattice*100:.1f}%)")
print(f"  F_lattice_32 range: [{F_lattice_32.min():.4f}, {F_lattice_32.max():.4f}]")

# ── Step 1: Assemble continuum spectrum at available tau points ────────────

sectors = [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(3,0),(0,3),(2,1)]

def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p+1)*(q+1)*(p+q+2)//2

# Source A: s44 at tau = [0.00, 0.05, 0.10, 0.15, 0.19]
s44_taus = [0.00, 0.05, 0.10, 0.15, 0.19]
s44_data = {}
for tv in s44_taus:
    key = f'tau{tv:.2f}'
    omega = d44[f'{key}_all_omega']   # (992,) — absolute eigenvalues
    dim2  = d44[f'{key}_all_dim2']    # (992,) — degeneracy weights
    s44_data[tv] = {'omega': omega, 'dim2': dim2}
    print(f"  s44 tau={tv:.2f}: {len(omega)} modes, "
          f"omega=[{omega.min():.4f}, {omega.max():.4f}], "
          f"sum(dim2)={dim2.sum():.0f}")

# Source B: s27 at tau = [0.00, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]
s27_taus = list(d27['tau_values'])
s27_data = {}
for ti, tv in enumerate(s27_taus):
    omega_list = []
    dim2_list = []
    for p, q in sectors:
        key = f'evals_{p}_{q}_{ti}'
        evals = np.abs(d27[key])  # absolute eigenvalues
        d = dim_pq(p, q)
        omega_list.extend(evals)
        dim2_list.extend([d**2] * len(evals))
    omega = np.array(omega_list)
    dim2 = np.array(dim2_list)
    s27_data[tv] = {'omega': omega, 'dim2': dim2}
    if tv not in [0.0, 0.1, 0.15]:  # avoid duplicating s44 output
        print(f"  s27 tau={tv:.2f}: {len(omega)} modes, "
              f"omega=[{omega.min():.4f}, {omega.max():.4f}], "
              f"sum(dim2)={dim2.sum():.0f}")

# ── Step 2: Merge into unified tau grid ────────────────────────────────────

# Combine all available tau points, preferring s44 where both exist
# s44: [0.00, 0.05, 0.10, 0.15, 0.19]
# s27: [0.00, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]
# Combined unique: [0.00, 0.05, 0.10, 0.15, 0.19, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]

all_tau_set = sorted(set(s44_taus + s27_taus))
print(f"\nMerged tau grid: {all_tau_set}")
print(f"  {len(all_tau_set)} distinct points")

# Build spectrum at each tau (prefer s44 data where available)
spectrum_data = {}
for tv in all_tau_set:
    if tv in s44_data:
        spectrum_data[tv] = s44_data[tv]
    elif tv in s27_data:
        spectrum_data[tv] = s27_data[tv]
    else:
        raise ValueError(f"No data at tau={tv}")

tau_grid = np.array(all_tau_set)

# ── Step 3: Interpolate H(tau) to the continuum tau grid ──────────────────

cs_H = CubicSpline(tau_sf, H_sf, bc_type='natural')
H_grid = cs_H(tau_grid)

# Clamp if extrapolation goes negative
if np.any(H_grid < 0):
    print(f"  WARNING: Clamping {(H_grid < 0).sum()} negative H values")
    H_grid = np.maximum(H_grid, 0.01)

T_GH_grid = H_grid / (2.0 * np.pi)

print(f"\nH(tau) interpolation to continuum grid:")
for i, tv in enumerate(tau_grid):
    print(f"  tau={tv:.2f}: H={H_grid[i]:.4f}, T_GH={T_GH_grid[i]:.6f}")

# ── Step 4: Compute free energy on continuum ──────────────────────────────

print(f"\n{'='*70}")
print(f"COMPUTING FREE ENERGY ON 992-MODE CONTINUUM")
print(f"{'='*70}")

F_continuum = np.zeros(len(tau_grid))
ln_Z_continuum = np.zeros(len(tau_grid))
S_continuum = np.zeros(len(tau_grid))  # entropy cross-check
E_avg_continuum = np.zeros(len(tau_grid))

# Also compute WITHOUT degeneracy weights (992 modes, unit weight)
F_992_unweighted = np.zeros(len(tau_grid))

for i, tv in enumerate(tau_grid):
    T = T_GH_grid[i]
    omega = spectrum_data[tv]['omega']
    dim2 = spectrum_data[tv]['dim2']

    if T < 1e-15:
        continue

    # Weighted partition function: ln Z = sum_k dim2_k * ln(1 + exp(-omega_k/T))
    ratios = omega / T

    # Numerical stability
    ln_terms = np.where(ratios > 500, np.exp(-ratios), np.log1p(np.exp(-ratios)))

    # Weighted
    ln_Z_continuum[i] = np.sum(dim2 * ln_terms)
    F_continuum[i] = -T * ln_Z_continuum[i]

    # Unweighted (992 modes, each weight=1)
    ln_Z_uw = np.sum(ln_terms)
    F_992_unweighted[i] = -T * ln_Z_uw

    # Entropy and average energy (weighted)
    n_k = np.where(ratios > 500, np.exp(-ratios), 1.0 / (1.0 + np.exp(ratios)))

    # S = -sum dim2 * [n ln n + (1-n) ln(1-n)]
    safe_mask = (n_k > 1e-15) & (n_k < 1 - 1e-15)
    s_terms = np.zeros_like(n_k)
    s_terms[safe_mask] = -(n_k[safe_mask] * np.log(n_k[safe_mask]) +
                           (1 - n_k[safe_mask]) * np.log(1 - n_k[safe_mask]))
    S_continuum[i] = np.sum(dim2 * s_terms)

    # E = sum dim2 * omega * n_k
    E_avg_continuum[i] = np.sum(dim2 * omega * n_k)

    # Thermodynamic consistency check: F = E - TS
    F_check = E_avg_continuum[i] - T * S_continuum[i]
    discrepancy = abs(F_continuum[i] - F_check)

    print(f"  tau={tv:.2f}: T_GH={T:.4f}, ln_Z={ln_Z_continuum[i]:.2f}, "
          f"F={F_continuum[i]:.4f}, S={S_continuum[i]:.2f}, "
          f"|F-(E-TS)|={discrepancy:.2e}")

# ── Step 5: Interpolate to fine grid for extremum analysis ────────────────

print(f"\n{'='*70}")
print(f"FINE-GRID INTERPOLATION AND EXTREMUM ANALYSIS")
print(f"{'='*70}")

# Interpolate F_continuum onto a fine 200-point grid
tau_fine = np.linspace(tau_grid[0], tau_grid[-1], 200)
cs_F = CubicSpline(tau_grid, F_continuum)
F_fine = cs_F(tau_fine)
dF_fine = cs_F(tau_fine, 1)  # first derivative
d2F_fine = cs_F(tau_fine, 2)  # second derivative

# Also interpolate T_GH for reporting
cs_T = CubicSpline(tau_grid, T_GH_grid)
T_fine = cs_T(tau_fine)

# Find extrema via zero crossings of dF
extrema = []
for i in range(len(dF_fine) - 1):
    if dF_fine[i] * dF_fine[i+1] < 0:
        # Linear interpolation for zero crossing
        tau_cross = tau_fine[i] - dF_fine[i] * (tau_fine[i+1] - tau_fine[i]) / (dF_fine[i+1] - dF_fine[i])
        F_cross = float(cs_F(tau_cross))
        d2F_cross = float(cs_F(tau_cross, 2))
        etype = "MINIMUM" if d2F_cross > 0 else "MAXIMUM"
        extrema.append({
            'tau': float(tau_cross),
            'F': F_cross,
            'd2F': d2F_cross,
            'type': etype
        })
        print(f"  {etype} at tau = {tau_cross:.6f}, F = {F_cross:.4f}, d2F = {d2F_cross:.2f}")

if len(extrema) == 0:
    print("  NO EXTREMA FOUND — F(tau) is monotone on fine grid")

# ── Step 6: Gate evaluation ───────────────────────────────────────────────

print(f"\n{'='*70}")
print(f"GATE EVALUATION: EUCLID-CONTINUUM-55")
print(f"{'='*70}")
print(f"  Criterion: PASS if barrier on continuum exceeds barrier on 32-cell lattice")
print(f"             FAIL if barrier weaker or no minimum")
print(f"  Lattice barrier: {barrier_frac_lattice*100:.1f}%")

gate_pass = False
tau_min_cont = None
barrier_height_cont = None
barrier_frac_cont = None
barrier_left = None
barrier_right = None

# Check for minimum in the range [0.10, 0.30]
minima_in_range = [e for e in extrema if e['type'] == 'MINIMUM' and 0.10 <= e['tau'] <= 0.30]

if len(minima_in_range) > 0:
    best_min = min(minima_in_range, key=lambda e: e['F'])
    tau_min_cont = best_min['tau']
    F_min_cont = best_min['F']

    # Barrier heights from left and right
    F_left = float(cs_F(tau_grid[0]))     # F at tau=0
    F_right = float(cs_F(tau_grid[-1]))   # F at tau=0.5

    barrier_left = F_left - F_min_cont
    barrier_right = F_right - F_min_cont

    # Overall barrier
    barrier_height_cont = max(barrier_left, barrier_right)
    barrier_frac_cont = abs(barrier_height_cont / F_min_cont) if abs(F_min_cont) > 1e-15 else float('inf')

    # Fractional barriers from each side
    barrier_frac_left = abs(barrier_left / F_min_cont)
    barrier_frac_right = abs(barrier_right / F_min_cont)

    print(f"\n  MINIMUM FOUND at tau = {tau_min_cont:.6f}")
    print(f"    F_min = {F_min_cont:.4f} M_KK")
    print(f"    F(tau=0) = {F_left:.4f}")
    print(f"    F(tau=0.5) = {F_right:.4f}")
    print(f"    Barrier (left)  = {barrier_left:.4f} ({barrier_frac_left*100:.1f}%)")
    print(f"    Barrier (right) = {barrier_right:.4f} ({barrier_frac_right*100:.1f}%)")
    print(f"    Barrier (max)   = {barrier_height_cont:.4f} ({barrier_frac_cont*100:.1f}%)")
    print(f"    d2F/dtau2 at min = {best_min['d2F']:.2f} (curvature)")

    # Gate comparison
    print(f"\n  COMPARISON WITH LATTICE:")
    print(f"    Lattice barrier: {barrier_frac_lattice*100:.1f}%")
    print(f"    Continuum barrier: {barrier_frac_cont*100:.1f}%")
    print(f"    Ratio (continuum/lattice): {barrier_frac_cont/barrier_frac_lattice:.3f}")
    print(f"    Lattice tau_min: {tau_min_lattice:.4f}")
    print(f"    Continuum tau_min: {tau_min_cont:.4f}")

    if barrier_frac_cont > barrier_frac_lattice:
        gate_pass = True
        verdict = "PASS"
        print(f"\n  VERDICT: PASS — continuum barrier ({barrier_frac_cont*100:.1f}%) "
              f"exceeds lattice ({barrier_frac_lattice*100:.1f}%)")
    else:
        verdict = "FAIL"
        print(f"\n  VERDICT: FAIL — continuum barrier ({barrier_frac_cont*100:.1f}%) "
              f"weaker than lattice ({barrier_frac_lattice*100:.1f}%)")
else:
    if len(extrema) == 0:
        verdict = "FAIL (monotone)"
        print(f"\n  VERDICT: FAIL — F(tau) is monotone, no minimum found")
    else:
        verdict = "FAIL (no minimum in [0.10, 0.30])"
        print(f"\n  VERDICT: FAIL — no minimum in target range [0.10, 0.30]")
        for e in extrema:
            print(f"    Found {e['type']} at tau={e['tau']:.4f} (outside range)")

# ── Step 7: Physical interpretation ──────────────────────────────────────

print(f"\n{'='*70}")
print(f"PHYSICAL ANALYSIS")
print(f"{'='*70}")

# Decompose F into T and lnZ contributions
print(f"\n  F = -T * ln Z decomposition at data points:")
print(f"  {'tau':>5s} {'T_GH':>8s} {'ln_Z':>12s} {'-T*lnZ':>12s} {'F_unw':>10s}")
for i, tv in enumerate(tau_grid):
    print(f"  {tv:5.2f} {T_GH_grid[i]:8.4f} {ln_Z_continuum[i]:12.2f} {F_continuum[i]:12.4f} {F_992_unweighted[i]:10.4f}")

# Ratio of continuum to lattice free energy
print(f"\n  Scale comparison at overlapping tau points:")
# Find closest lattice points for each continuum tau
for i, tv in enumerate(tau_grid):
    idx_lat = np.argmin(np.abs(tau_lattice - tv))
    if abs(tau_lattice[idx_lat] - tv) < 0.015:
        ratio = F_continuum[i] / F_lattice_32[idx_lat] if abs(F_lattice_32[idx_lat]) > 1e-10 else float('inf')
        print(f"  tau={tv:.2f}: F_cont={F_continuum[i]:.2f}, F_lat32={F_lattice_32[idx_lat]:.2f}, ratio={ratio:.1f}")

# ── Step 8: Save data ────────────────────────────────────────────────────

np.savez('computations/session-55/s55_euclid_continuum.npz',
    # Raw data at available tau points
    tau_grid=tau_grid,
    H_grid=H_grid,
    T_GH_grid=T_GH_grid,
    F_continuum=F_continuum,
    F_992_unweighted=F_992_unweighted,
    ln_Z_continuum=ln_Z_continuum,
    S_continuum=S_continuum,
    E_avg_continuum=E_avg_continuum,
    # Fine grid interpolation
    tau_fine=tau_fine,
    F_fine=F_fine,
    dF_fine=dF_fine,
    d2F_fine=d2F_fine,
    T_fine=T_fine,
    # Gate results
    gate_verdict=verdict,
    tau_min_continuum=tau_min_cont if tau_min_cont is not None else np.nan,
    barrier_height_continuum=barrier_height_cont if barrier_height_cont is not None else np.nan,
    barrier_frac_continuum=barrier_frac_cont if barrier_frac_cont is not None else np.nan,
    barrier_frac_left=barrier_left / abs(F_min_cont) if (tau_min_cont is not None and abs(F_min_cont) > 1e-15) else np.nan,
    barrier_frac_right=barrier_right / abs(F_min_cont) if (tau_min_cont is not None and abs(F_min_cont) > 1e-15) else np.nan,
    # Lattice comparison
    tau_min_lattice=tau_min_lattice,
    barrier_frac_lattice=barrier_frac_lattice,
    # Metadata
    n_modes=992,  # (local)
    n_physical_modes=101984,
)
print(f"\nData saved: computations/session-55/s55_euclid_continuum.npz")

# ── Step 9: Plot ─────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle(f'EUCLID-CONTINUUM-55: 992-Mode Continuum vs 32-Cell Lattice\nVerdict: {verdict}',
             fontsize=14, fontweight='bold')

# Panel 1: F(tau) — main comparison
ax = axes[0, 0]
ax.plot(tau_fine, F_fine, 'b-', linewidth=2.5, label=f'Continuum (992 modes, weighted)')
ax.plot(tau_grid, F_continuum, 'bo', markersize=8, zorder=5)
ax.plot(tau_lattice, F_lattice_32, 'r--', linewidth=1.5, alpha=0.7, label='Lattice (32 modes)')
ax.plot(tau_lattice, F_lattice_8, 'g:', linewidth=1.5, alpha=0.5, label='Lattice (8 BCS modes)')
if tau_min_cont is not None:
    ax.axvline(tau_min_cont, color='blue', linestyle=':', alpha=0.7,
               label=f'tau_min={tau_min_cont:.3f} (cont)')
ax.axvline(tau_min_lattice, color='red', linestyle=':', alpha=0.5,
           label=f'tau_min={tau_min_lattice:.3f} (lat)')
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
ax.set_xlabel('tau')
ax.set_ylabel('F(tau) [M_KK]')
ax.set_title('Free Energy Comparison')
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3)

# Panel 2: Normalized comparison F/F_min
ax = axes[0, 1]
if tau_min_cont is not None:
    F_norm_cont = F_fine / F_min_cont
    F_norm_lat = F_lattice_32 / F_lattice_32.min()
    F_norm_lat8 = F_lattice_8 / F_lattice_8.min()
    ax.plot(tau_fine, F_norm_cont, 'b-', linewidth=2.5, label='Continuum')
    ax.plot(tau_lattice, F_norm_lat, 'r--', linewidth=1.5, alpha=0.7, label='Lattice 32')
    ax.plot(tau_lattice, F_norm_lat8, 'g:', linewidth=1.5, alpha=0.5, label='Lattice 8')
    ax.axhline(1.0, color='k', linestyle='-', alpha=0.3)
    ax.set_xlabel('tau')
    ax.set_ylabel('F / F_min')
    ax.set_title('Normalized Free Energy (barrier shape)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
else:
    ax.text(0.5, 0.5, 'No minimum found', ha='center', va='center', transform=ax.transAxes)
    ax.set_title('Normalized Free Energy')

# Panel 3: dF/dtau
ax = axes[0, 2]
ax.plot(tau_fine, dF_fine, 'b-', linewidth=2)
ax.axhline(0, color='k', linestyle='-', alpha=0.3)
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
for e in extrema:
    color = 'red' if e['type'] == 'MINIMUM' else 'magenta'
    marker = 'v' if e['type'] == 'MINIMUM' else '^'
    ax.axvline(e['tau'], color=color, linestyle=':', alpha=0.7,
               label=f"{e['type']} tau={e['tau']:.3f}")
ax.set_xlabel('tau')
ax.set_ylabel('dF/dtau')
ax.set_title('Free Energy Gradient (continuum)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: T_GH(tau) and H(tau)
ax = axes[1, 0]
ax.plot(tau_grid, T_GH_grid, 'ro-', linewidth=2, label='T_GH (continuum grid)')
ax.plot(tau_lattice, T_GH_lattice, 'r--', alpha=0.5, label='T_GH (lattice)')
ax2 = ax.twinx()
ax2.plot(tau_grid, H_grid, 'b^-', linewidth=1.5, alpha=0.7, label='H(tau)')
ax.set_xlabel('tau')
ax.set_ylabel('T_GH [M_KK]', color='r')
ax2.set_ylabel('H(tau)', color='b')
ax.set_title('Gibbons-Hawking Temperature')
ax.legend(loc='upper left', fontsize=8)
ax2.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: ln Z decomposition
ax = axes[1, 1]
ax.plot(tau_grid, ln_Z_continuum, 'b-o', linewidth=2, label='ln Z (weighted, 101984 modes)')
ax.plot(tau_grid, -F_continuum / T_GH_grid, 'r--', linewidth=1.5, alpha=0.7, label='F/(-T_GH) check')
ax.set_xlabel('tau')
ax.set_ylabel('ln Z')
ax.set_title('Partition Function (continuum)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Entropy
ax = axes[1, 2]
ax.plot(tau_grid, S_continuum, 'm-o', linewidth=2, label='S_continuum')
ax.set_xlabel('tau')
ax.set_ylabel('S [nats]')
ax.set_title('Entropy at T_GH (continuum)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-55/s55_euclid_continuum.png', dpi=150, bbox_inches='tight')
print(f"Plot saved: computations/session-55/s55_euclid_continuum.png")

# ── Final summary ────────────────────────────────────────────────────────

print(f"\n{'='*70}")
print(f"FINAL SUMMARY")
print(f"{'='*70}")
print(f"  Gate: EUCLID-CONTINUUM-55")
print(f"  Verdict: {verdict}")
print(f"  N_modes (distinct): 992")
print(f"  N_modes (physical, weighted): 101,984")
print(f"  F(tau) range: [{F_continuum.min():.4f}, {F_continuum.max():.4f}]")
if tau_min_cont is not None:
    print(f"  tau_min (continuum): {tau_min_cont:.6f}")
    print(f"  tau_min (lattice): {tau_min_lattice:.6f}")
    print(f"  F_min (continuum): {F_min_cont:.4f}")
    print(f"  Barrier (left): {barrier_frac_left*100:.1f}%")
    print(f"  Barrier (right): {barrier_frac_right*100:.1f}%")
    print(f"  Barrier (max): {barrier_frac_cont*100:.1f}%")
    print(f"  Lattice barrier: {barrier_frac_lattice*100:.1f}%")
    print(f"  Continuum/Lattice ratio: {barrier_frac_cont/barrier_frac_lattice:.3f}")
else:
    print(f"  No minimum found")
print(f"  Number of extrema: {len(extrema)}")
for e in extrema:
    print(f"    {e['type']} at tau={e['tau']:.4f}, F={e['F']:.4f}")
