#!/usr/bin/env python3
"""
s54_massey_fold.py — MASSEY-FOLD-54
====================================
Extract the Massey (Landau-Zener) adiabaticity parameter at every avoided
crossing in the 256-state Fock spectrum from ED-SWEEP-54.

Gate: MASSEY-FOLD-54  (INFO — classification only)

Physics
-------
For a two-level avoided crossing swept at velocity v = |dtau/dt|, the
standard Landau-Zener transition probability is

    P_LZ = exp(-pi * xi / 2)

where the Massey parameter is

    xi = (Delta_E_min)^2 / (v * |dE_diabatic/dtau|)        (1)

Here:
  - Delta_E_min is the minimum energy gap at the avoided crossing
  - v = omega_tau = 8.27 M_KK (attractor transit velocity, S38)
  - |dE_diabatic/dtau| is the slope difference of the diabatic levels
    at the crossing point.  We estimate this from the adiabatic spectrum
    as |d(E_{n+1} - E_n)/dtau| evaluated slightly away from the crossing
    (where the adiabatic curves approximate the diabatic ones).

Nuclear analog: Cranking through rotational band crossings in deformed
nuclei (backbending in ^158Er, ^168Hf).  There the angular velocity omega
plays the role of tau_dot, and the same Massey / Landau-Zener criterion
determines whether the yrast band follows the g-band or jumps to the
s-band.  Paper 03 (Dobaczewski-Nazarewicz) treats the analogous blocking
and pair-breaking at band crossings.

Author: nazarewicz-nuclear-structure-theorist
Session: S54, Wave 3, Computation #25
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import omega_tau, tau_fold

# ============================================================================
#  Load data
# ============================================================================
data = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),
               's54_ed_sweep.npz'), allow_pickle=True)

tau_vals   = data['tau_values']        # (50,)
all_eigs   = data['all_eigenvalues']   # (50, 256) — sorted ascending at each tau
fold_idx   = int(data['fold_idx'])     # tau index closest to fold
N_tau, N_states = all_eigs.shape

print(f"Loaded: {N_tau} tau points, {N_states} Fock states")
print(f"tau range: [{tau_vals[0]:.4f}, {tau_vals[-1]:.4f}], dtau = {tau_vals[1]-tau_vals[0]:.6f}")
print(f"Fold at index {fold_idx}, tau_fold = {tau_vals[fold_idx]:.4f}")
print(f"omega_tau = {omega_tau} M_KK (transit velocity)")
print()

dtau = tau_vals[1] - tau_vals[0]  # uniform grid spacing

# ============================================================================
#  Step 1: Compute gaps Delta_E_n(tau) = E_{n+1}(tau) - E_n(tau)
# ============================================================================
# gaps[i, n] = E_{n+1}(tau_i) - E_n(tau_i)
gaps = np.diff(all_eigs, axis=1)   # (N_tau, N_states-1)

print(f"Gap array shape: {gaps.shape}")
print(f"Min gap anywhere: {gaps.min():.6e}")
print(f"Max gap anywhere: {gaps.max():.6e}")
print()

# ============================================================================
#  Step 2: Find avoided crossings — local minima of Delta_E_n(tau)
# ============================================================================
# An avoided crossing for level pair (n, n+1) occurs at tau_i where:
#   gaps[i, n] < gaps[i-1, n]  AND  gaps[i, n] < gaps[i+1, n]
# AND the gap is "small" — we use a threshold relative to the local scale.

avoided_crossings = []  # list of (n, i_ac, DeltaE_min)

for n in range(N_states - 1):
    gap_n = gaps[:, n]  # gap for this pair across all tau

    # Find local minima (interior points only)
    for i in range(1, N_tau - 1):
        if gap_n[i] < gap_n[i-1] and gap_n[i] < gap_n[i+1]:
            # This is a local minimum — candidate avoided crossing
            # Filter: require the gap to be < 50% of the average gap for
            # this pair (otherwise it's just a fluctuation, not a crossing)
            avg_gap = np.mean(gap_n)
            if gap_n[i] < 0.5 * avg_gap and gap_n[i] > 0:
                avoided_crossings.append((n, i, gap_n[i]))

print(f"Found {len(avoided_crossings)} avoided crossings (with 50% filter)")

# Also do an unfiltered count
all_minima = []
for n in range(N_states - 1):
    gap_n = gaps[:, n]
    for i in range(1, N_tau - 1):
        if gap_n[i] < gap_n[i-1] and gap_n[i] < gap_n[i+1] and gap_n[i] > 0:
            all_minima.append((n, i, gap_n[i]))

print(f"Total local minima (unfiltered, gap>0): {len(all_minima)}")
print()

# ============================================================================
#  Step 3: Compute Massey parameter at each avoided crossing
# ============================================================================
# At an avoided crossing at tau_i for level pair (n, n+1):
#
# The ADIABATIC gap is Delta_E(tau_i) = gap_n[i].
# The DIABATIC slope |F_1 - F_2| is estimated from the adiabatic spectrum
# away from the crossing.  Near an avoided crossing:
#
#   E_+(tau) = E_bar + sqrt((alpha*delta_tau)^2 + V^2)
#   E_-(tau) = E_bar - sqrt((alpha*delta_tau)^2 + V^2)
#
# where alpha = |F_1 - F_2|/2 is half the diabatic slope difference,
# V = Delta_E_min / 2 is the coupling matrix element, and
# delta_tau = tau - tau_ac.
#
# The derivative of the gap:
#   d(Delta_E)/dtau = 2*alpha^2*delta_tau / sqrt(alpha^2*delta_tau^2 + V^2)
#
# So |d(Delta_E)/dtau| at delta_tau = +/- dtau_grid gives us alpha:
#   alpha^2 = (d_gap/2)^2 * (V^2 + alpha^2*dtau^2) / (dtau^2)
#
# Simpler approach: use second derivative of the gap at the minimum.
# d^2(Delta_E)/dtau^2 |_{tau_ac} = 2*alpha^2 / V = 2*(Delta_F/2)^2 / (Delta_E_min/2)
#                                 = Delta_F^2 / (2*Delta_E_min)
#
# So Delta_F = sqrt(2 * Delta_E_min * d^2(Delta_E)/dtau^2)
#
# The Massey parameter (standard Landau-Zener convention):
#   xi = 2*pi * V^2 / (hbar * v * |F_1 - F_2|)
#     = 2*pi * (Delta_E_min/2)^2 / (omega_tau * Delta_F)
#     = pi * Delta_E_min^2 / (2 * omega_tau * Delta_F)
#
# Alternative using the curvature directly:
#   xi = pi * Delta_E_min^2 / (2 * omega_tau * sqrt(2 * Delta_E_min * gap_curv))
#     = pi * Delta_E_min^{3/2} / (2 * omega_tau * sqrt(2 * gap_curv))

results = []

for n, i_ac, dE_min in avoided_crossings:
    gap_n = gaps[:, n]

    # Method A: finite-difference second derivative of gap at crossing
    d2gap = (gap_n[i_ac+1] - 2*gap_n[i_ac] + gap_n[i_ac-1]) / dtau**2

    if d2gap <= 0:
        # Not a proper minimum (numerical noise) — skip
        continue

    # Diabatic slope difference from curvature
    # Delta_F = sqrt(2 * dE_min * d2gap)
    Delta_F_A = np.sqrt(2.0 * dE_min * d2gap)

    # Massey parameter (Landau-Zener convention: xi = 2*pi*V^2 / (v * Delta_F))
    # V = dE_min / 2
    V = dE_min / 2.0
    xi_A = 2.0 * np.pi * V**2 / (omega_tau * Delta_F_A)

    # Method B: direct slope estimate from neighboring points
    # Use points 2 grid steps away where the adiabatic ≈ diabatic
    i_lo = max(0, i_ac - 2)
    i_hi = min(N_tau - 1, i_ac + 2)
    slope_gap = (gap_n[i_hi] - gap_n[i_lo]) / (tau_vals[i_hi] - tau_vals[i_lo])
    # Near crossing, the gap is symmetric, so the slope is ~0.
    # Use the asymmetric slope from one side instead:
    slope_right = (gap_n[i_ac+1] - gap_n[i_ac]) / dtau
    slope_left  = (gap_n[i_ac] - gap_n[i_ac-1]) / dtau
    # The diabatic slope is approximately the average of |slope_right| + |slope_left|
    # But at the minimum, slopes are opposite sign. Use the magnitude.
    avg_slope = (abs(slope_right) + abs(slope_left)) / 2.0

    # From the hyperbola model: at delta_tau = dtau, slope ≈ alpha^2*dtau / V
    # So alpha ≈ sqrt(V * avg_slope / dtau)
    # Delta_F = 2*alpha
    if avg_slope > 0:
        alpha_B = np.sqrt(V * avg_slope / dtau)
        Delta_F_B = 2.0 * alpha_B
        xi_B = 2.0 * np.pi * V**2 / (omega_tau * Delta_F_B)
    else:
        Delta_F_B = np.nan
        xi_B = np.nan

    # Landau-Zener probability
    P_LZ_A = np.exp(-np.pi * xi_A / 2.0)

    results.append({
        'n': n,
        'i_ac': i_ac,
        'tau_ac': tau_vals[i_ac],
        'dE_min': dE_min,
        'V': V,
        'd2gap': d2gap,
        'Delta_F_A': Delta_F_A,
        'Delta_F_B': Delta_F_B,
        'xi_A': xi_A,
        'xi_B': xi_B,
        'P_LZ': P_LZ_A,
        'E_low': all_eigs[i_ac, n],
        'E_high': all_eigs[i_ac, n+1],
    })

print(f"Computed Massey parameter at {len(results)} avoided crossings")
print()

# ============================================================================
#  Step 4: Analysis and classification
# ============================================================================
if len(results) == 0:
    print("WARNING: No valid avoided crossings found. Checking raw gap structure...")
    # Print some diagnostics
    for n in range(min(20, N_states-1)):
        gap_n = gaps[:, n]
        print(f"  Pair ({n},{n+1}): min_gap={gap_n.min():.6e}, "
              f"max_gap={gap_n.max():.6e}, mean={gap_n.mean():.6e}")
    sys.exit(0)

# Sort by xi_A
results.sort(key=lambda r: r['xi_A'])

xi_all = np.array([r['xi_A'] for r in results])
P_LZ_all = np.array([r['P_LZ'] for r in results])
tau_ac_all = np.array([r['tau_ac'] for r in results])
dE_all = np.array([r['dE_min'] for r in results])

print("=" * 80)
print("MASSEY PARAMETER DISTRIBUTION")
print("=" * 80)
print(f"  Total avoided crossings analyzed: {len(results)}")
print(f"  xi_min  = {xi_all.min():.6e}")
print(f"  xi_max  = {xi_all.max():.6e}")
print(f"  xi_mean = {xi_all.mean():.6e}")
print(f"  xi_med  = {np.median(xi_all):.6e}")
print()

# Classification
n_diabatic   = np.sum(xi_all < 0.1)
n_crossover  = np.sum((xi_all >= 0.1) & (xi_all <= 10))
n_adiabatic  = np.sum(xi_all > 10)

print(f"  DIABATIC   (xi < 0.1):  {n_diabatic} ({100*n_diabatic/len(results):.1f}%)")
print(f"  CROSSOVER  (0.1 < xi < 10): {n_crossover} ({100*n_crossover/len(results):.1f}%)")
print(f"  ADIABATIC  (xi > 10):   {n_adiabatic} ({100*n_adiabatic/len(results):.1f}%)")
print()

# Focus on fold region
fold_tau = tau_vals[fold_idx]
fold_window = 0.03  # +/- 0.03 around fold  # (local)
near_fold = [r for r in results
             if abs(r['tau_ac'] - fold_tau) < fold_window]

print(f"  Crossings near fold (|tau - {fold_tau:.4f}| < {fold_window}):")
print(f"  Count: {len(near_fold)}")
if near_fold:
    xi_fold = np.array([r['xi_A'] for r in near_fold])
    print(f"  xi range near fold: [{xi_fold.min():.6e}, {xi_fold.max():.6e}]")
    n_diab_fold = np.sum(xi_fold < 0.1)
    n_cross_fold = np.sum((xi_fold >= 0.1) & (xi_fold <= 10))
    n_adiab_fold = np.sum(xi_fold > 10)
    print(f"  Near-fold: {n_diab_fold} diabatic, {n_cross_fold} crossover, "
          f"{n_adiab_fold} adiabatic")
print()

# ============================================================================
#  Step 5: Detailed table of crossings sorted by xi
# ============================================================================
print("=" * 80)
print("TOP 20 MOST DIABATIC CROSSINGS (smallest xi)")
print("=" * 80)
print(f"{'Rank':>4} {'n':>4} {'tau_ac':>8} {'DeltaE':>12} "
      f"{'xi':>12} {'P_LZ':>10} {'Class':>10}")
print("-" * 70)
for rank, r in enumerate(results[:20], 1):
    if r['xi_A'] < 0.1:
        cls = "DIABATIC"
    elif r['xi_A'] > 10:
        cls = "ADIABATIC"
    else:
        cls = "CROSSOVER"
    print(f"{rank:4d} {r['n']:4d} {r['tau_ac']:8.4f} {r['dE_min']:12.6e} "
          f"{r['xi_A']:12.6e} {r['P_LZ']:10.6f} {cls:>10}")

print()
print("=" * 80)
print("TOP 10 MOST ADIABATIC CROSSINGS (largest xi)")
print("=" * 80)
print(f"{'Rank':>4} {'n':>4} {'tau_ac':>8} {'DeltaE':>12} "
      f"{'xi':>12} {'P_LZ':>10} {'Class':>10}")
print("-" * 70)
for rank, r in enumerate(sorted(results, key=lambda x: -x['xi_A'])[:10], 1):
    if r['xi_A'] < 0.1:
        cls = "DIABATIC"
    elif r['xi_A'] > 10:
        cls = "ADIABATIC"
    else:
        cls = "CROSSOVER"
    print(f"{rank:4d} {r['n']:4d} {r['tau_ac']:8.4f} {r['dE_min']:12.6e} "
          f"{r['xi_A']:12.6e} {r['P_LZ']:10.6f} {cls:>10}")

print()
print("=" * 80)
print("CROSSINGS NEAR FOLD")
print("=" * 80)
if near_fold:
    near_fold_sorted = sorted(near_fold, key=lambda r: r['xi_A'])
    print(f"{'n':>4} {'tau_ac':>8} {'DeltaE':>12} "
          f"{'xi':>12} {'P_LZ':>10} {'E_low':>10} {'E_high':>10}")
    print("-" * 75)
    for r in near_fold_sorted:
        print(f"{r['n']:4d} {r['tau_ac']:8.4f} {r['dE_min']:12.6e} "
              f"{r['xi_A']:12.6e} {r['P_LZ']:10.6f} "
              f"{r['E_low']:10.4f} {r['E_high']:10.4f}")
else:
    print("  No avoided crossings found near fold.")

# ============================================================================
#  Step 6: Volovik vs Nazarewicz assessment
# ============================================================================
print()
print("=" * 80)
print("ASSESSMENT: VOLOVIK vs NAZAREWICZ PREDICTIONS")
print("=" * 80)

# Volovik: omega_tau/delta_E ~ 800 => deeply diabatic (xi << 1)
# Estimate: if typical delta_E ~ 0.01 and omega_tau = 8.27,
# then omega_tau / delta_E ~ 827.
# xi = Delta_E^2 / (omega_tau * Delta_F).
# For xi << 1 everywhere => Volovik right.
# For any xi ~ 1 near fold => Nazarewicz crossover relevant.

median_xi = np.median(xi_all)
geomean_xi = np.exp(np.mean(np.log(xi_all[xi_all > 0])))

print(f"  Median xi:      {median_xi:.6e}")
print(f"  Geometric mean: {geomean_xi:.6e}")
print()

if median_xi < 0.01:
    verdict = "DEEPLY DIABATIC — Volovik confirmed"
    print(f"  VERDICT: {verdict}")
    print(f"  The transit is overwhelmingly diabatic. Integrability survives.")
    print(f"  P_LZ > 0.99 for most crossings: system jumps across,")
    print(f"  preserving quasiparticle character throughout transit.")
elif median_xi < 1.0:
    verdict = "MIXED — partial relaxation"
    print(f"  VERDICT: {verdict}")
    print(f"  Some crossings are in the crossover regime.")
    print(f"  Integrability is partially broken by non-adiabatic transitions.")
elif median_xi > 10:
    verdict = "DEEPLY ADIABATIC — transit follows instantaneous eigenstate"
    print(f"  VERDICT: {verdict}")
    print(f"  The transit is overwhelmingly adiabatic.")
    print(f"  System follows the ground state throughout. No pair excitation.")
else:
    verdict = "CROSSOVER REGIME"
    print(f"  VERDICT: {verdict}")

print()

# Nazarewicz crossover criterion: N_pair/Omega = 0.125
N_pair = int(data['N_pair'])
Omega = N_states  # Fock space dimension
ratio = N_pair / Omega if Omega > 0 else 0
print(f"  N_pair/Omega = {N_pair}/{Omega} = {ratio:.6f}")
print(f"  Predicted crossover at N_pair/Omega = 0.125")
print(f"  Current ratio {'<' if ratio < 0.125 else '>='} 0.125")
print()

# ============================================================================
#  Step 7: Statistics by tau region
# ============================================================================
print("=" * 80)
print("XI STATISTICS BY TAU REGION")
print("=" * 80)

regions = [
    ("Pre-fold (tau < 0.15)", 0.0, 0.15),
    ("Near-fold (0.15 < tau < 0.25)", 0.15, 0.25),
    ("Post-fold (tau > 0.25)", 0.25, 0.6),
]

for label, t_lo, t_hi in regions:
    mask = (tau_ac_all >= t_lo) & (tau_ac_all < t_hi)
    count = np.sum(mask)
    if count > 0:
        xi_region = xi_all[mask]
        print(f"  {label}:")
        print(f"    Count: {count}")
        print(f"    xi: min={xi_region.min():.4e}, med={np.median(xi_region):.4e}, "
              f"max={xi_region.max():.4e}")
        n_d = np.sum(xi_region < 0.1)
        n_c = np.sum((xi_region >= 0.1) & (xi_region <= 10))
        n_a = np.sum(xi_region > 10)
        print(f"    Diabatic/Crossover/Adiabatic: {n_d}/{n_c}/{n_a}")
    else:
        print(f"  {label}: 0 crossings")
    print()

# ============================================================================
#  Step 8: Save results
# ============================================================================
outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       's54_massey_fold.npz')

np.savez(outpath,
    # Per-crossing arrays
    xi_values=xi_all,
    P_LZ_values=P_LZ_all,
    tau_ac_values=tau_ac_all,
    dE_min_values=dE_all,
    # Summary statistics
    xi_min=xi_all.min(),
    xi_max=xi_all.max(),
    xi_median=np.median(xi_all),
    xi_geomean=geomean_xi,
    n_total=len(results),
    n_diabatic=n_diabatic,
    n_crossover=n_crossover,
    n_adiabatic=n_adiabatic,
    # Near-fold statistics
    n_near_fold=len(near_fold),
    # Parameters
    omega_tau_used=omega_tau,
    fold_tau=fold_tau,
    fold_window=fold_window,
    # Gate
    gate_name='MASSEY-FOLD-54',
    gate_verdict='INFO',
)

print(f"Results saved to {outpath}")
print()
print("=" * 80)
print(f"GATE: MASSEY-FOLD-54 = INFO")
print(f"  {len(results)} avoided crossings analyzed")
print(f"  xi range: [{xi_all.min():.4e}, {xi_all.max():.4e}]")
print(f"  Classification: {n_diabatic} diabatic / {n_crossover} crossover / "
      f"{n_adiabatic} adiabatic")
print(f"  Verdict: {verdict}")
print("=" * 80)
