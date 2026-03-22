#!/usr/bin/env python3
"""
Session 33a Step 1: LANDAU-SECTOR -- B2-analog minimum in non-singlet sectors.

Check whether the B2 eigenvalue minimum at tau ~ 0.19 exists in sectors (1,0)
and (0,1). Gate SECT-33a: UNIVERSAL if delta_tau < 0.02, SINGLET-SPECIFIC if
delta_tau > 0.05.

Mathematical background:
    In the singlet sector (0,0), the 8-fold degenerate eigenvalue at tau=0
    (lambda = sqrt(3)/2 = 0.866025) splits into B1(1) + B2(4) + B3(3).
    B2 minimum at tau = 0.190, the organizing center.

    In non-singlet sectors, the eigenvalue structure differs because
    different SU(3) irreps have different Casimirs. We search for ANY
    eigenvalue minimum near tau ~ 0.19 in each sector.

Refined method:
    Track individual eigenvalue trajectories (not group centroids).
    For each track, find all interior minima via cubic spline interpolation.
    Report ALL minima in range [0.10, 0.35] and identify the one closest
    to tau = 0.190 as the "B2-analog" for that sector.

Author: sim (phonon-exflation-sim)
Date: 2026-03-06
"""

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────
# 1. Load data
# ─────────────────────────────────────────────────────────────

d_bcs = np.load('tier0-computation/s27_multisector_bcs.npz', allow_pickle=True)
d_conv = np.load('tier0-computation/s28c_sector_convergence.npz', allow_pickle=True)
tau_vals = d_bcs['tau_values']
n_tau = len(tau_vals)
tau_fine = np.linspace(0.05, 0.45, 5000)

print(f"Tau grid: {tau_vals}")


def get_positive_tracks(p, q, n_max=16):
    """Get sorted positive eigenvalue tracks for sector (p,q)."""
    tracks = []
    for ti in range(n_tau):
        key = f'evals_{p}_{q}_{ti}'
        if key in d_bcs.files:
            e = d_bcs[key]
        elif key in d_conv.files:
            e = d_conv[key]
        else:
            raise KeyError(f"Missing {key}")
        pos = np.sort(e[e > 1e-10])
        tracks.append(pos)
    n_pos = min(n_max, min(len(t) for t in tracks))
    arr = np.zeros((n_tau, n_pos))
    for ti in range(n_tau):
        arr[ti, :] = tracks[ti][:n_pos]
    return arr


def find_minima_in_range(traj, tau_range=(0.10, 0.35)):
    """Find all interior minima of trajectory in given tau range."""
    # Use tau points starting from index 1 to avoid tau=0 degeneracy issues
    # For the singlet B2, we need to use tau > 0 only
    cs = CubicSpline(tau_vals, traj)
    tf_range = tau_fine[(tau_fine >= tau_range[0]) & (tau_fine <= tau_range[1])]
    if len(tf_range) < 3:
        return []
    deriv = cs(tf_range, 1)
    scs = np.where(np.diff(np.sign(deriv)))[0]
    minima = []
    for sc in scs:
        try:
            tm = brentq(lambda t: cs(t, 1), tf_range[sc], tf_range[sc + 1])
            d2 = cs(tm, 2)
            if d2 > 0:
                minima.append({
                    'tau_min': tm,
                    'lambda_min': float(cs(tm)),
                    'd2': float(d2),
                })
        except Exception:
            pass
    return minima


# ─────────────────────────────────────────────────────────────
# 2. Singlet (0,0): B2 minimum (reference)
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("REFERENCE: (0,0) SINGLET B2 MINIMUM")
print("=" * 70)

tracks_00 = get_positive_tracks(0, 0, n_max=8)
# At tau > 0: index 0 = B1, indices 1-4 = B2 (4-fold), indices 5-7 = B3 (3-fold)
# B2 centroid
b2_centroid_00 = tracks_00[:, 1:5].mean(axis=1)
b2_spread_00 = tracks_00[:, 1:5].max(axis=1) - tracks_00[:, 1:5].min(axis=1)
print(f"  B2 4-fold spread: {b2_spread_00[1:].max():.2e} (should be ~0 = exact degeneracy)")

b2_min_00 = find_minima_in_range(b2_centroid_00)
if b2_min_00:
    ref = b2_min_00[0]
    tau_ref = ref['tau_min']
    print(f"  B2 minimum: tau = {tau_ref:.5f}, lambda = {ref['lambda_min']:.7f}, "
          f"d2 = {ref['d2']:.4f}")
else:
    print("  WARNING: no B2 minimum found in (0,0)!")
    tau_ref = 0.190

# ─────────────────────────────────────────────────────────────
# 3. Non-singlet sectors: search for eigenvalue minima near dump
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("NON-SINGLET SECTOR ANALYSIS")
print("=" * 70)

# All sectors available in s27
all_sectors = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
               (3, 0), (0, 3), (2, 1)]

sector_summary = {}

for (p, q) in all_sectors:
    try:
        tracks = get_positive_tracks(p, q, n_max=16)
    except KeyError:
        continue

    n_tracks = tracks.shape[1]
    print(f"\n--- Sector ({p},{q}): {n_tracks} positive tracks ---")

    # Degeneracy groups at tau=0
    e0 = tracks[0, :]
    groups = []
    i = 0
    while i < len(e0):
        val = e0[i]
        cnt = 1
        while i + cnt < len(e0) and abs(e0[i + cnt] - val) < 1e-4:
            cnt += 1
        groups.append((i, cnt, val))
        i += cnt
    print(f"  Degeneracy groups at tau=0: {[(g[1], round(g[2], 6)) for g in groups]}")

    # For each track, find all minima near the dump point
    all_mins = []
    for j in range(n_tracks):
        mins = find_minima_in_range(tracks[:, j], tau_range=(0.10, 0.35))
        for m in mins:
            m['track'] = j
            all_mins.append(m)

    # Sort by proximity to tau_ref
    all_mins.sort(key=lambda m: abs(m['tau_min'] - tau_ref))

    # Identify degenerate cluster (minima at the same tau within tolerance)
    if all_mins:
        best = all_mins[0]
        cluster = [best]
        for m in all_mins[1:]:
            if abs(m['tau_min'] - best['tau_min']) < 0.005:
                cluster.append(m)

        cluster_deg = len(cluster)
        cluster_tau = np.mean([m['tau_min'] for m in cluster])
        cluster_lam = np.mean([m['lambda_min'] for m in cluster])
        cluster_d2 = np.mean([m['d2'] for m in cluster])

        print(f"  Closest minimum cluster to tau={tau_ref:.3f}:")
        print(f"    Tracks: {[m['track'] for m in cluster]}")
        print(f"    Mean tau_min: {cluster_tau:.5f}")
        print(f"    Mean lambda_min: {cluster_lam:.7f}")
        print(f"    Mean d2: {cluster_d2:.4f}")
        print(f"    Cluster degeneracy: {cluster_deg}")
        print(f"    delta_tau from ref: {abs(cluster_tau - tau_ref):.5f}")

        # Which degeneracy group do these tracks belong to?
        for m in cluster:
            for (start, cnt, val0) in groups:
                if start <= m['track'] < start + cnt:
                    m['group_deg'] = cnt
                    m['group_val0'] = val0
                    break

        sector_summary[(p, q)] = {
            'cluster_tau': cluster_tau,
            'cluster_lambda': cluster_lam,
            'cluster_d2': cluster_d2,
            'cluster_deg': cluster_deg,
            'cluster_tracks': [m['track'] for m in cluster],
            'group_info': [(m.get('group_deg'), m.get('group_val0')) for m in cluster],
            'all_mins': all_mins,
        }
    else:
        print(f"  NO minima found in [0.10, 0.35]")

# ─────────────────────────────────────────────────────────────
# 4. Gate evaluation
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("GATE EVALUATION: SECT-33a")
print("=" * 70)

# Target sectors for gate
target_sectors = [(0, 0), (1, 0), (0, 1)]
tau_mins = {}

# (0,0) reference
tau_mins[(0, 0)] = tau_ref

for (p, q) in [(1, 0), (0, 1)]:
    if (p, q) in sector_summary:
        s = sector_summary[(p, q)]
        tau_mins[(p, q)] = s['cluster_tau']

print("\nSector-by-sector B2-analog minima:")
for (p, q), tm in sorted(tau_mins.items()):
    if (p, q) == (0, 0):
        label = "B2 (4-fold, reference)"
    elif (p, q) in sector_summary:
        s = sector_summary[(p, q)]
        label = f"cluster deg={s['cluster_deg']}, tracks={s['cluster_tracks']}"
    else:
        label = "???"
    print(f"  ({p},{q}): tau_min = {tm:.5f}  [{label}]")

# Compute gate quantity
target_taus = [tau_mins.get(s) for s in target_sectors if s in tau_mins]
delta_tau = max(target_taus) - min(target_taus)
print(f"\ndelta_tau (max spread across targets): {delta_tau:.5f}")

if delta_tau < 0.02:
    verdict = "UNIVERSAL"
elif delta_tau > 0.05:
    verdict = "SINGLET-SPECIFIC"
else:
    verdict = "INTERMEDIATE"

print(f"Threshold: UNIVERSAL < 0.02, SINGLET-SPECIFIC > 0.05")
print(f"\n>>> SECT-33a verdict: {verdict} <<<")

# ─────────────────────────────────────────────────────────────
# 5. Extended analysis: all sectors
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("EXTENDED: ALL SECTORS WITH MINIMA NEAR DUMP POINT")
print("=" * 70)

all_sector_taus = {}
for (p, q), s in sector_summary.items():
    if abs(s['cluster_tau'] - tau_ref) < 0.05:
        all_sector_taus[(p, q)] = s['cluster_tau']
        print(f"  ({p},{q}): tau_min = {s['cluster_tau']:.5f}, "
              f"deg = {s['cluster_deg']}, d2 = {s['cluster_d2']:.3f}")

if all_sector_taus:
    taus = list(all_sector_taus.values())
    print(f"\n  Sectors with minima within 0.05 of dump: "
          f"{len(all_sector_taus)}/{len(sector_summary)}")
    print(f"  Overall spread: {max(taus) - min(taus):.5f}")
    print(f"  Mean: {np.mean(taus):.5f}, Std: {np.std(taus):.5f}")

# ─────────────────────────────────────────────────────────────
# 6. Plot
# ─────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: (0,0) singlet eigenvalue flow with branch labels
ax = axes[0, 0]
for j in range(8):
    if j == 0:
        ax.plot(tau_vals, tracks_00[:, j], 'o-', color='C0', markersize=3, label='B1')
    elif j <= 4:
        lbl = 'B2 (4-fold)' if j == 1 else None
        ax.plot(tau_vals, tracks_00[:, j], 'o-', color='C1', markersize=3, label=lbl)
    else:
        lbl = 'B3 (3-fold)' if j == 5 else None
        ax.plot(tau_vals, tracks_00[:, j], 'o-', color='C2', markersize=3, label=lbl)
ax.axvline(x=tau_ref, color='red', linestyle='--', alpha=0.7,
           label=f'B2 min: tau={tau_ref:.3f}')
ax.set_xlabel('tau')
ax.set_ylabel('lambda')
ax.set_title('(0,0) Singlet: B1+B2+B3 Branches')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: (1,0) sector eigenvalue flow
ax = axes[0, 1]
tracks_10 = get_positive_tracks(1, 0, n_max=12)
cmap = plt.cm.tab20
for j in range(12):
    ax.plot(tau_vals, tracks_10[:, j], 'o-', color=cmap(j / 12), markersize=3,
            label=f'track {j}' if j < 6 else None)
if (1, 0) in sector_summary:
    s = sector_summary[(1, 0)]
    for t in s['cluster_tracks']:
        ax.plot(tau_vals, tracks_10[:, t], 'o-', color='red', markersize=5, linewidth=2)
ax.axvline(x=tau_ref, color='red', linestyle='--', alpha=0.7)
if (1, 0) in tau_mins:
    ax.axvline(x=tau_mins[(1, 0)], color='blue', linestyle=':', alpha=0.7,
               label=f'(1,0) min: tau={tau_mins[(1,0)]:.3f}')
ax.set_xlabel('tau')
ax.set_ylabel('lambda')
ax.set_title('(1,0) Sector: Eigenvalue Flow (red = B2-analog cluster)')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 3: B2-analog minimum comparison across sectors
ax = axes[1, 0]
sectors_to_plot = [(p, q) for (p, q) in sector_summary if sector_summary[(p, q)]['cluster_tau'] is not None]
sectors_to_plot.sort()
y_labels = []
y_vals = []
for i, (p, q) in enumerate(sectors_to_plot):
    s = sector_summary[(p, q)]
    y_labels.append(f'({p},{q})')
    y_vals.append(s['cluster_tau'])
    ax.barh(i, s['cluster_tau'], height=0.6, alpha=0.7,
            color='green' if abs(s['cluster_tau'] - tau_ref) < 0.02 else
            ('orange' if abs(s['cluster_tau'] - tau_ref) < 0.05 else 'gray'))
    ax.text(s['cluster_tau'] + 0.005, i, f"d={s['cluster_deg']}, d2={s['cluster_d2']:.1f}",
            fontsize=7, va='center')

ax.axvline(x=tau_ref, color='red', linestyle='--', linewidth=2, label=f'(0,0) ref: {tau_ref:.3f}')
ax.axvspan(tau_ref - 0.02, tau_ref + 0.02, alpha=0.15, color='green', label='UNIVERSAL zone')
ax.set_yticks(range(len(y_labels)))
ax.set_yticklabels(y_labels)
ax.set_xlabel('tau_min of closest eigenvalue cluster')
ax.set_title('Eigenvalue Minima Near Dump Point by Sector')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: d(lambda)/d(tau) for B2 and non-singlet analogs
ax = axes[1, 1]
# (0,0) B2
cs_00 = CubicSpline(tau_vals, b2_centroid_00)
ax.plot(tau_fine, cs_00(tau_fine, 1), '-', color='blue', linewidth=2, label='(0,0) B2')

# (1,0) closest cluster
if (1, 0) in sector_summary:
    s = sector_summary[(1, 0)]
    # Average trajectory of cluster tracks
    cluster_traj = tracks_10[:, s['cluster_tracks']].mean(axis=1)
    cs_10 = CubicSpline(tau_vals, cluster_traj)
    ax.plot(tau_fine, cs_10(tau_fine, 1), '-', color='orange', linewidth=2,
            label=f'(1,0) tracks {s["cluster_tracks"]}')

ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=tau_ref, color='red', linestyle='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('d(lambda)/d(tau)')
ax.set_title('Group Velocity: (0,0) B2 vs (1,0) Analog')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(-1.5, 1.5)

plt.suptitle(f'Session 33a: LANDAU-SECTOR Diagnostic -- SECT-33a: {verdict}',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('tier0-computation/s33a_landau_sector.png', dpi=150, bbox_inches='tight')
print("\nPlot saved: tier0-computation/s33a_landau_sector.png")

# ─────────────────────────────────────────────────────────────
# 7. Save results
# ─────────────────────────────────────────────────────────────

save_data = {
    'tau_values': tau_vals,
    'verdict': np.array([verdict]),
    'tau_ref_00': np.array([tau_ref]),
    'b2_centroid_00': b2_centroid_00,
}

for (p, q), s in sector_summary.items():
    prefix = f'sector_{p}_{q}'
    save_data[f'{prefix}_cluster_tau'] = np.array([s['cluster_tau']])
    save_data[f'{prefix}_cluster_lambda'] = np.array([s['cluster_lambda']])
    save_data[f'{prefix}_cluster_d2'] = np.array([s['cluster_d2']])
    save_data[f'{prefix}_cluster_deg'] = np.array([s['cluster_deg']])
    save_data[f'{prefix}_cluster_tracks'] = np.array(s['cluster_tracks'])

for (p, q), tm in tau_mins.items():
    save_data[f'tau_min_{p}_{q}'] = np.array([tm])

save_data['delta_tau'] = np.array([delta_tau])

np.savez('tier0-computation/s33a_landau_sector.npz', **save_data)
print("Data saved: tier0-computation/s33a_landau_sector.npz")

# ─────────────────────────────────────────────────────────────
# 8. Final summary
# ─────────────────────────────────────────────────────────────

print("\n" + "=" * 70)
print("FINAL SUMMARY: SECT-33a")
print("=" * 70)

print(f"\nReference: (0,0) B2 minimum at tau = {tau_ref:.5f}")
print(f"  4-fold degeneracy, lambda_min = {b2_min_00[0]['lambda_min']:.7f}, "
      f"d2 = {b2_min_00[0]['d2']:.4f}")

for (p, q) in [(1, 0), (0, 1)]:
    if (p, q) in sector_summary:
        s = sector_summary[(p, q)]
        dt = abs(s['cluster_tau'] - tau_ref)
        print(f"\n({p},{q}): closest cluster at tau = {s['cluster_tau']:.5f}")
        print(f"  {s['cluster_deg']}-fold cluster, tracks = {s['cluster_tracks']}")
        print(f"  lambda_min = {s['cluster_lambda']:.7f}, d2 = {s['cluster_d2']:.3f}")
        print(f"  delta_tau from (0,0) B2 = {dt:.5f}")

print(f"\n  delta_tau (gate quantity) = {delta_tau:.5f}")
print(f"  Verdict: {verdict}")
print(f"  (UNIVERSAL < 0.02, SINGLET-SPECIFIC > 0.05)")
