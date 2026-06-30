#!/usr/bin/env python3
"""
S59 Refinement: Precise location of sectional curvature zero crossing
and its relationship to the domain wall E_DW=0 crossing.

The main computation found sec_min(tau_DW) = -3.3e-7, which is VERY close to zero.
This script refines the sec_min=0 crossing with higher resolution to test whether
the sec_min=0 and E_DW=0 crossings genuinely coincide.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.optimize import brentq
from scipy.interpolate import interp1d
import itertools
from canonical_constants import g0_diag

alpha = g0_diag

# Rebuild structure constants
f_abc_dict = {
    (1,2,3): 1.0, (1,4,7): 0.5, (1,6,5): 0.5, (2,4,6): 0.5,
    (2,5,7): 0.5, (3,4,5): 0.5, (3,7,6): 0.5,
    (4,5,8): np.sqrt(3)/2, (6,7,8): np.sqrt(3)/2,
}
f_full = np.zeros((9, 9, 9))
for (a, b, c), val in f_abc_dict.items():
    for perm in itertools.permutations([a, b, c]):
        inv = sum(1 for ii in range(3) for jj in range(ii+1, 3) if perm[ii] > perm[jj])
        f_full[perm[0], perm[1], perm[2]] = (-1)**inv * val

grp_map = np.array([1, 1, 1, 2, 2, 2, 2, 0])

def jensen_metric(tau):
    return alpha * np.exp(2*tau), alpha * np.exp(-2*tau), alpha * np.exp(tau)

def compute_sec_min(tau):
    x1, x2, x3 = jensen_metric(tau)
    x_vals = np.array([x1, x2, x3])
    x_per_dir = x_vals[grp_map]
    n = 8

    gamma = np.zeros((n, n, n))
    for i in range(n):
        for j in range(n):
            for c in range(n):
                fv = f_full[i+1, j+1, c+1]
                if abs(fv) > 1e-15:
                    gamma[c, i, j] = fv * np.sqrt(2.0 * x_per_dir[c] / (x_per_dir[i] * x_per_dir[j]))

    Gamma = 0.5 * (gamma - np.transpose(gamma, (1, 2, 0)) + np.transpose(gamma, (2, 0, 1)))

    sec_vals = []
    pair_info = []
    for a in range(n):
        for b in range(a+1, n):
            K = 0.0
            for m in range(n):
                K += Gamma[m, b, b] * Gamma[a, a, m]
                K -= Gamma[m, a, b] * Gamma[a, b, m]
                K -= gamma[m, a, b] * Gamma[a, m, b]
            sec_vals.append(K)
            pair_info.append((a, b))

    return np.array(sec_vals), pair_info

with open('s59_ricci_dw_refine_log.txt', 'w') as LOG:
    def log(msg):
        LOG.write(msg + '\n')
        LOG.flush()

    log("S59 REFINEMENT: Sectional curvature zero crossing vs Domain Wall")
    log("=" * 72)

    # Load the domain wall crossing
    d58 = np.load('s58_off_jensen_dw.npz', allow_pickle=True)
    tau_58 = d58['tau_scan']
    edw_geom = d58['E_DW_tau_geom']
    f_edw = interp1d(tau_58, edw_geom, kind='cubic')
    tau_dw = 0.113488  # from main computation  # (local)

    # High-resolution scan around tau_DW
    log(f"\nHigh-resolution scan: tau in [0.10, 0.15], N=200")
    tau_fine = np.linspace(0.10, 0.15, 200)
    sec_min_fine = np.zeros(200)

    for idx, tau in enumerate(tau_fine):
        sects, _ = compute_sec_min(tau)
        sec_min_fine[idx] = np.min(sects)

    # Find the exact sec_min = 0 crossing
    f_sec = interp1d(tau_fine, sec_min_fine, kind='cubic')

    tau_sec_zero = None
    for i in range(199):
        if sec_min_fine[i] >= 0 and sec_min_fine[i+1] < 0:
            tau_sec_zero = brentq(f_sec, tau_fine[i], tau_fine[i+1])
            break
        elif sec_min_fine[i] < 0 and sec_min_fine[i+1] >= 0:
            # Crossing from negative to positive
            tau_sec_zero = brentq(f_sec, tau_fine[i], tau_fine[i+1])
            break

    if tau_sec_zero is None:
        # Check if sec_min is ALWAYS zero in some range (degenerate)
        # Look at the region where sec_min is closest to zero
        idx_min_abs = np.argmin(np.abs(sec_min_fine))
        log(f"  No clean zero crossing found.")
        log(f"  Closest to zero: sec_min = {sec_min_fine[idx_min_abs]:.2e} at tau = {tau_fine[idx_min_abs]:.6f}")

        # The bi-invariant SU(3) has some sec=0 planes (flat 2-planes).
        # These may persist along the Jensen path. Let's check which pairs are zero.
        log(f"\n  Analyzing which sectional curvature pairs are zero or near-zero:")
        dir_names = ['su2_1', 'su2_2', 'su2_3', 'C2_4', 'C2_5', 'C2_6', 'C2_7', 'u1_8']

        for test_tau in [0.0, 0.05, 0.10, tau_dw, 0.15, 0.20]:
            sects, pairs = compute_sec_min(test_tau)
            log(f"\n  tau = {test_tau:.4f}:")
            min_sect = np.min(sects)
            max_sect = np.max(sects)
            log(f"    sec range: [{min_sect:.8f}, {max_sect:.8f}]")

            # Show the zero/near-zero pairs
            zero_pairs = [(sects[i], pairs[i]) for i in range(len(sects)) if abs(sects[i]) < 0.001]
            for sv, (a, b) in sorted(zero_pairs):
                log(f"    K({dir_names[a]}, {dir_names[b]}) = {sv:.10f}")

            # Show the most negative pair
            min_idx = np.argmin(sects)
            a, b = pairs[min_idx]
            log(f"    Most negative: K({dir_names[a]}, {dir_names[b]}) = {sects[min_idx]:.10f}")

            # Show all unique sectional curvature VALUES (group by type)
            # Type classification:
            # (u1, su2), (u1, C2), (su2, su2), (su2, C2), (C2, C2)
            grps = {(0,1): [], (0,2): [], (1,1): [], (1,2): [], (2,2): []}
            gmap = {0: 'u1', 1: 'su2', 2: 'C2'}
            for i, (a, b) in enumerate(pairs):
                ga = grp_map[a]
                gb = grp_map[b]
                key = (min(ga, gb), max(ga, gb))
                grps[key].append(sects[i])

            for key in sorted(grps.keys()):
                vals = grps[key]
                if vals:
                    log(f"    K({gmap[key[0]]},{gmap[key[1]]}): min={min(vals):.8f}, max={max(vals):.8f}, "
                        f"mean={np.mean(vals):.8f}, count={len(vals)}")

    else:
        log(f"\n  Sectional curvature zero crossing at tau_sec = {tau_sec_zero:.8f}")
        log(f"  Domain wall E_DW=0 crossing at tau_DW = {tau_dw:.8f}")
        log(f"  Difference: |tau_DW - tau_sec| = {abs(tau_dw - tau_sec_zero):.8f}")
        log(f"  Ratio: tau_DW / tau_sec = {tau_dw / tau_sec_zero:.8f}")

    # Detailed output near tau_DW
    log(f"\n  Fine-grained sec_min near tau_DW:")
    log(f"  {'tau':>10s} {'sec_min':>15s}")
    mask = (tau_fine > 0.108) & (tau_fine < 0.120)
    for idx in range(200):
        if mask[idx]:
            log(f"  {tau_fine[idx]:10.6f} {sec_min_fine[idx]:15.10f}")

    log(f"\n  DONE.")

print("Done. See s59_ricci_dw_refine_log.txt")
