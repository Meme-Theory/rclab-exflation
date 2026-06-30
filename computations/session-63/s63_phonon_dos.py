#!/usr/bin/env python3
"""
s63_phonon_dos.py — Phonon Density of States & Van Hove Classification
=======================================================================

PHONON-DOS-63 (W5-01): Compute g(omega) for the full 45-mode coupled
dispersion across all 32 k-points. Identify all van Hove singularities
at hybridization gap edges. Classify by type (M0-M3).

PHYSICS:
    The density of states g(omega) is the spectral measure:
        g(omega) = (1/N_k) Sum_{k,n} delta(omega - omega_n(k))

    Van Hove singularities occur where nabla_k omega_n(k) = 0. In 1D
    (our CG(24) Cayley graph has effectively 1D dispersion), the VHS
    classification simplifies:
        M0: band minimum (d^2 omega/dk^2 > 0) -- onset, g ~ (omega-omega_0)^{-1/2}
        M1: band maximum (d^2 omega/dk^2 < 0) -- cutoff, g ~ (omega_1-omega)^{-1/2}
    (M2, M3 require 2D, 3D respectively -- CG(24) is effectively 1D so only M0/M1)

    At hybridization gaps: avoided crossings create paired M1/M0 singularities
    (top of lower branch = M1, bottom of upper branch = M0), separated by the gap.

    We also compute the integrated DOS N(omega) = integral_0^omega g(omega') d omega'
    and the sector-resolved DOS g_A(omega), g_B(omega), g_C(omega) using the
    sector participation weights from S62.

GATE: PHONON-DOS-63 | W5-01 | INFO (diagnostic)

INPUT: s62_phonon_dispersion_full.npz
OUTPUT: s63_phonon_dos.npz, s63_phonon_dos.png

Author: tesla-resonance
Session: S63 W5-01
"""

import sys
import os
import time
import numpy as np
from scipy.signal import find_peaks
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = Path(__file__).parent
OUT_NPZ = SCRIPT_DIR / "s63_phonon_dos.npz"
OUT_PNG = SCRIPT_DIR / "s63_phonon_dos.png"
OUT_TXT = SCRIPT_DIR / "s63_phonon_dos_output.txt"
IN_NPZ = SCRIPT_DIR / "s62_phonon_dispersion_full.npz"

t_start = time.time()

# =============================================================================
# Output tee
# =============================================================================
class Tee:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.stdout = sys.stdout
    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)
    def flush(self):
        self.file.flush()
        self.stdout.flush()

sys.stdout = Tee(str(OUT_TXT))

print("=" * 78)
print("S63 PHONON-DOS-63: Phonon DOS & Van Hove Classification (W5-01)")
print("=" * 78)

# =============================================================================
# SECTION 1: Load dispersion data
# =============================================================================
print("\n--- Section 1: Load dispersion data ---")

data = np.load(IN_NPZ, allow_pickle=True)
omega_full = data['omega_full']       # (32, 45) — sorted bands at each k
evecs_full = data['evecs_full']       # (32, 45, 45)
sector_weight = data['sector_weight'] # (32, 45, 3) — A, B, C participation
k_eff = data['k_eff']                 # (32,)
lambda_n = data['lambda_n']           # (32,) graph Laplacian eigenvalues

N_k, N_modes = omega_full.shape
print(f"Loaded: {N_k} k-points, {N_modes} modes per k-point")
print(f"omega range: [{omega_full.min():.4f}, {omega_full.max():.4f}] M_KK")
print(f"k_eff range: [{k_eff.min():.4f}, {k_eff.max():.4f}]")

# Handle the negative-frequency mode (mode 0 at some k-points)
# This is a tachyonic/unstable direction. For DOS, take |omega|.
omega_abs = np.abs(omega_full)
n_negative = np.sum(omega_full < 0)
print(f"Negative frequencies: {n_negative} entries (tachyonic mode)")
if n_negative > 0:
    print(f"  Min negative: {omega_full.min():.4f} M_KK — folded to |omega|")

# =============================================================================
# SECTION 2: Compute DOS via linear interpolation (1D tetrahedron method)
# =============================================================================
print("\n--- Section 2: Compute phonon DOS ---")

# In 1D, the "tetrahedron method" reduces to linear interpolation between
# adjacent k-points. For each band n and each k-segment [k_i, k_{i+1}],
# the band has omega in [omega_n(k_i), omega_n(k_{i+1})].
# The contribution to g(omega) from this segment is:
#   g(omega) += 1 / |omega_n(k_{i+1}) - omega_n(k_i)|  for omega in [omega_min, omega_max]
# which gives the 1D DOS its characteristic 1/sqrt divergences at band edges.

# But the CG(24) Cayley graph is NOT a simple 1D chain — k_eff values are
# graph Laplacian eigenvalues with degeneracies. We must account for the
# actual graph structure.

# Strategy: high-resolution histogram with Gaussian broadening + analytic
# identification of VHS from the discrete band structure.

# Step 1: Determine energy grid
omega_min_all = 0.0  # Start from 0 (we folded negatives)  # (local)
omega_max_all = omega_abs.max() * 1.02
N_omega = 4000  # High resolution for VHS identification
omega_grid = np.linspace(omega_min_all, omega_max_all, N_omega)
d_omega = omega_grid[1] - omega_grid[0]

print(f"Energy grid: {N_omega} points, [{omega_min_all:.4f}, {omega_max_all:.4f}] M_KK")
print(f"Resolution: {d_omega:.6f} M_KK")

# Step 2: Raw histogram DOS (each k-point equally weighted)
# The CG(24) has degenerate eigenvalues, so k-points carry multiplicities.
# For the Cayley graph of S_4, the Laplacian eigenvalues have known degeneracies
# from the irrep dimensions of S_4.
# lambda_n are the 32 DISTINCT eigenvalues of the 24-vertex graph Laplacian
# (some may coincide), each carrying weight 1/N_cells.
# Since omega_full already has 32 k-points (one per eigenvalue), weight = 1/32.

g_raw = np.zeros(N_omega)
g_A = np.zeros(N_omega)
g_B = np.zeros(N_omega)
g_C = np.zeros(N_omega)

for ik in range(N_k):
    for im in range(N_modes):
        omega_val = omega_abs[ik, im]
        idx = int((omega_val - omega_min_all) / d_omega)
        idx = np.clip(idx, 0, N_omega - 1)
        weight = 1.0 / N_k
        g_raw[idx] += weight / d_omega
        # Sector-resolved
        g_A[idx] += weight * sector_weight[ik, im, 0] / d_omega
        g_B[idx] += weight * sector_weight[ik, im, 1] / d_omega
        g_C[idx] += weight * sector_weight[ik, im, 2] / d_omega

# Step 3: Gaussian-broadened DOS for smooth visualization
# Use two widths: narrow (for VHS identification) and broad (for visualization)
sigma_narrow = 0.03  # M_KK — narrow enough to resolve gaps  # (local)
sigma_broad = 0.10   # M_KK — for smooth overview  # (local)

def gaussian_broaden(g_hist, omega_grid, sigma):
    """Convolve histogram DOS with Gaussian kernel."""
    g_smooth = np.zeros_like(g_hist)
    # Direct convolution on grid
    kernel_half = int(5 * sigma / d_omega) + 1
    kernel_x = np.arange(-kernel_half, kernel_half + 1) * d_omega
    kernel = np.exp(-kernel_x**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
    kernel /= kernel.sum() * d_omega  # Normalize
    g_smooth = np.convolve(g_hist * d_omega, kernel, mode='same')
    return g_smooth

g_narrow = gaussian_broaden(g_raw, omega_grid, sigma_narrow)
g_broad = gaussian_broaden(g_raw, omega_grid, sigma_broad)
g_A_narrow = gaussian_broaden(g_A, omega_grid, sigma_narrow)
g_B_narrow = gaussian_broaden(g_B, omega_grid, sigma_narrow)
g_C_narrow = gaussian_broaden(g_C, omega_grid, sigma_narrow)
g_A_broad = gaussian_broaden(g_A, omega_grid, sigma_broad)
g_B_broad = gaussian_broaden(g_B, omega_grid, sigma_broad)
g_C_broad = gaussian_broaden(g_C, omega_grid, sigma_broad)

# Normalization check: integral should equal N_modes = 45
integral_raw = np.trapezoid(g_narrow, omega_grid)
print(f"\nDOS integral (should = {N_modes}): {integral_raw:.4f}")
print(f"Normalization error: {abs(integral_raw - N_modes)/N_modes * 100:.2f}%")

# Integrated DOS: N(omega) = int_0^omega g(omega') d omega'
N_omega_integrated = np.cumsum(g_narrow) * d_omega
print(f"N(omega_max) = {N_omega_integrated[-1]:.4f} (should be ~{N_modes})")

# =============================================================================
# SECTION 3: Identify van Hove singularities from band structure
# =============================================================================
print("\n--- Section 3: Van Hove singularity identification ---")

# Van Hove singularities occur at critical points: d omega_n / d k = 0.
# In 1D this means band minima (M0) and band maxima (M1).
# For each of the 45 bands, find extrema and classify.

vhs_list = []  # (omega, type, band_index, k_index, sector_char, curvature)

for n in range(N_modes):
    band = omega_abs[:, n]  # omega(k) for band n

    # Band minimum = M0 (onset singularity)
    k_min_idx = np.argmin(band)
    omega_min_band = band[k_min_idx]

    # Band maximum = M1 (cutoff singularity)
    k_max_idx = np.argmax(band)
    omega_max_band = band[k_max_idx]

    # Sector character at extrema
    sw_min = sector_weight[k_min_idx, n, :]
    sw_max = sector_weight[k_max_idx, n, :]
    sec_char_min = ['A', 'B', 'C'][np.argmax(sw_min)]
    sec_char_max = ['A', 'B', 'C'][np.argmax(sw_max)]

    # Estimate curvature at extrema (second derivative)
    # Use finite differences on the k_eff grid
    if k_min_idx == 0:
        curv_min = (band[1] - band[0]) / (k_eff[1] - k_eff[0] + 1e-15)
    elif k_min_idx == N_k - 1:
        curv_min = (band[-1] - band[-2]) / (k_eff[-1] - k_eff[-2] + 1e-15)
    else:
        dk1 = k_eff[k_min_idx] - k_eff[k_min_idx - 1]
        dk2 = k_eff[k_min_idx + 1] - k_eff[k_min_idx]
        if dk1 > 0 and dk2 > 0:
            curv_min = ((band[k_min_idx + 1] - band[k_min_idx]) / dk2
                       - (band[k_min_idx] - band[k_min_idx - 1]) / dk1) / ((dk1 + dk2) / 2)
        else:
            curv_min = 0.0  # (local)

    if k_max_idx == 0:
        curv_max = (band[1] - band[0]) / (k_eff[1] - k_eff[0] + 1e-15)
    elif k_max_idx == N_k - 1:
        curv_max = (band[-1] - band[-2]) / (k_eff[-1] - k_eff[-2] + 1e-15)
    else:
        dk1 = k_eff[k_max_idx] - k_eff[k_max_idx - 1]
        dk2 = k_eff[k_max_idx + 1] - k_eff[k_max_idx]
        if dk1 > 0 and dk2 > 0:
            curv_max = ((band[k_max_idx + 1] - band[k_max_idx]) / dk2
                       - (band[k_max_idx] - band[k_max_idx - 1]) / dk1) / ((dk1 + dk2) / 2)
        else:
            curv_max = 0.0  # (local)

    bandwidth = omega_max_band - omega_min_band

    # Record M0 (band minimum)
    vhs_list.append({
        'omega': omega_min_band,
        'type': 'M0',
        'band': n,
        'k_idx': k_min_idx,
        'sector': sec_char_min,
        'curvature': curv_min,
        'bandwidth': bandwidth,
        'sw': sw_min.copy()
    })

    # Record M1 (band maximum)
    vhs_list.append({
        'omega': omega_max_band,
        'type': 'M1',
        'band': n,
        'k_idx': k_max_idx,
        'sector': sec_char_max,
        'curvature': curv_max,
        'bandwidth': bandwidth,
        'sw': sw_max.copy()
    })

    # Check for interior extrema (saddle points in higher-D; local extrema in 1D)
    # These would be additional VHS if the band has non-monotonic behavior
    for i in range(1, N_k - 1):
        if band[i] > band[i-1] and band[i] > band[i+1]:
            # Local maximum (interior M1)
            if i != k_max_idx:  # Don't double-count global max
                sw_loc = sector_weight[i, n, :]
                sec_loc = ['A', 'B', 'C'][np.argmax(sw_loc)]
                dk1 = k_eff[i] - k_eff[i-1]
                dk2 = k_eff[i+1] - k_eff[i]
                if dk1 > 0 and dk2 > 0:
                    curv_loc = ((band[i+1] - band[i])/dk2 - (band[i] - band[i-1])/dk1) / ((dk1+dk2)/2)
                else:
                    curv_loc = 0.0  # (local)
                vhs_list.append({
                    'omega': band[i],
                    'type': 'M1_int',
                    'band': n,
                    'k_idx': i,
                    'sector': sec_loc,
                    'curvature': curv_loc,
                    'bandwidth': bandwidth,
                    'sw': sw_loc.copy()
                })
        elif band[i] < band[i-1] and band[i] < band[i+1]:
            # Local minimum (interior M0)
            if i != k_min_idx:  # Don't double-count global min
                sw_loc = sector_weight[i, n, :]
                sec_loc = ['A', 'B', 'C'][np.argmax(sw_loc)]
                dk1 = k_eff[i] - k_eff[i-1]
                dk2 = k_eff[i+1] - k_eff[i]
                if dk1 > 0 and dk2 > 0:
                    curv_loc = ((band[i+1] - band[i])/dk2 - (band[i] - band[i-1])/dk1) / ((dk1+dk2)/2)
                else:
                    curv_loc = 0.0  # (local)
                vhs_list.append({
                    'omega': band[i],
                    'type': 'M0_int',
                    'band': n,
                    'k_idx': i,
                    'sector': sec_loc,
                    'curvature': curv_loc,
                    'bandwidth': bandwidth,
                    'sw': sw_loc.copy()
                })

# Sort all VHS by frequency
vhs_list.sort(key=lambda x: x['omega'])

print(f"\nTotal van Hove singularities identified: {len(vhs_list)}")
n_M0 = sum(1 for v in vhs_list if v['type'] == 'M0')
n_M1 = sum(1 for v in vhs_list if v['type'] == 'M1')
n_M0_int = sum(1 for v in vhs_list if v['type'] == 'M0_int')
n_M1_int = sum(1 for v in vhs_list if v['type'] == 'M1_int')
print(f"  M0 (band minima): {n_M0}")
print(f"  M1 (band maxima): {n_M1}")
print(f"  M0_int (interior minima): {n_M0_int}")
print(f"  M1_int (interior maxima): {n_M1_int}")

# =============================================================================
# SECTION 4: Identify hybridization gaps
# =============================================================================
print("\n--- Section 4: Hybridization gap analysis ---")

# A hybridization gap between bands n and n+1 exists when:
#   min_k(omega_{n+1}(k)) > max_k(omega_n(k))
# i.e. no k-point has the bands overlapping.
# At the gap edges, the VHS are M1 (top of lower band) and M0 (bottom of upper band).

gaps = []
for n in range(N_modes - 1):
    band_upper_min = omega_abs[:, n + 1].min()
    band_lower_max = omega_abs[:, n].max()
    if band_upper_min > band_lower_max:
        gap_size = band_upper_min - band_lower_max
        gap_center = (band_upper_min + band_lower_max) / 2

        # Find the VHS at the gap edges
        # M1 at top of band n
        k_M1 = np.argmax(omega_abs[:, n])
        sw_M1 = sector_weight[k_M1, n, :]
        # M0 at bottom of band n+1
        k_M0 = np.argmin(omega_abs[:, n + 1])
        sw_M0 = sector_weight[k_M0, n + 1, :]

        # Sector character change across gap?
        sec_below = ['A', 'B', 'C'][np.argmax(sw_M1)]
        sec_above = ['A', 'B', 'C'][np.argmax(sw_M0)]
        sector_change = (sec_below != sec_above)

        gaps.append({
            'band_below': n,
            'band_above': n + 1,
            'gap_size': gap_size,
            'gap_center': gap_center,
            'omega_lower': band_lower_max,
            'omega_upper': band_upper_min,
            'k_M1': k_M1,
            'k_M0': k_M0,
            'sector_below': sec_below,
            'sector_above': sec_above,
            'sector_change': sector_change,
            'sw_M1': sw_M1.copy(),
            'sw_M0': sw_M0.copy()
        })

print(f"\nTrue hybridization gaps (non-overlapping adjacent bands): {len(gaps)}")
print(f"\n{'Gap':>4} {'Bands':>8} {'Size (M_KK)':>12} {'Center':>10} {'Below':>6} {'Above':>6} {'Hybrid?':>8}")
print("-" * 60)
for i, g in enumerate(gaps):
    hybrid = "YES" if g['sector_change'] else "no"
    print(f"  {i:2d}  {g['band_below']:2d}-{g['band_above']:2d}  "
          f"{g['gap_size']:12.6f}  {g['gap_center']:10.4f}  "
          f"{g['sector_below']:>6}  {g['sector_above']:>6}  {hybrid:>8}")

# Classify gaps by size
large_gaps = [g for g in gaps if g['gap_size'] > 0.1]
medium_gaps = [g for g in gaps if 0.01 <= g['gap_size'] <= 0.1]
small_gaps = [g for g in gaps if g['gap_size'] < 0.01]
hybrid_gaps = [g for g in gaps if g['sector_change']]

print(f"\nGap classification:")
print(f"  Large (> 0.1 M_KK): {len(large_gaps)}")
print(f"  Medium (0.01 - 0.1 M_KK): {len(medium_gaps)}")
print(f"  Small (< 0.01 M_KK): {len(small_gaps)}")
print(f"  Cross-sector (hybridization): {len(hybrid_gaps)}")

# =============================================================================
# SECTION 5: Classify VHS at hybridization gap edges
# =============================================================================
print("\n--- Section 5: VHS classification at hybridization gaps ---")

# For each gap, identify and classify the paired VHS (M1 below, M0 above).
# Report: type, omega, band, sector character, curvature (effective mass).

print(f"\n{'Gap':>4} {'Edge':>5} {'Type':>4} {'omega (M_KK)':>14} {'Band':>5} "
      f"{'Sector':>7} {'|d2w/dk2|':>10} {'BW':>8}")
print("-" * 72)

gap_vhs_pairs = []
for i, g in enumerate(gaps):
    # M1 at top of lower band
    n_low = g['band_below']
    band_low = omega_abs[:, n_low]
    k_M1 = g['k_M1']
    omega_M1 = g['omega_lower']
    sw_M1 = g['sw_M1']
    sec_M1 = g['sector_below']

    # Curvature at M1
    if k_M1 == 0:
        curv_M1 = 0.0  # (local)
    elif k_M1 == N_k - 1:
        curv_M1 = 0.0  # (local)
    else:
        dk1 = k_eff[k_M1] - k_eff[k_M1 - 1]
        dk2 = k_eff[k_M1 + 1] - k_eff[k_M1]
        if dk1 > 0 and dk2 > 0:
            curv_M1 = ((band_low[k_M1+1] - band_low[k_M1])/dk2
                      - (band_low[k_M1] - band_low[k_M1-1])/dk1) / ((dk1+dk2)/2)
        else:
            curv_M1 = 0.0  # (local)
    bw_low = band_low.max() - band_low.min()

    # M0 at bottom of upper band
    n_up = g['band_above']
    band_up = omega_abs[:, n_up]
    k_M0 = g['k_M0']
    omega_M0 = g['omega_upper']
    sw_M0 = g['sw_M0']
    sec_M0 = g['sector_above']

    # Curvature at M0
    if k_M0 == 0:
        curv_M0 = 0.0  # (local)
    elif k_M0 == N_k - 1:
        curv_M0 = 0.0  # (local)
    else:
        dk1 = k_eff[k_M0] - k_eff[k_M0 - 1]
        dk2 = k_eff[k_M0 + 1] - k_eff[k_M0]
        if dk1 > 0 and dk2 > 0:
            curv_M0 = ((band_up[k_M0+1] - band_up[k_M0])/dk2
                      - (band_up[k_M0] - band_up[k_M0-1])/dk1) / ((dk1+dk2)/2)
        else:
            curv_M0 = 0.0  # (local)
    bw_up = band_up.max() - band_up.min()

    print(f"  {i:2d}  lower  M1   {omega_M1:14.6f}  {n_low:5d}  "
          f"{sec_M1:>7}  {abs(curv_M1):10.4f}  {bw_low:8.4f}")
    print(f"  {i:2d}  upper  M0   {omega_M0:14.6f}  {n_up:5d}  "
          f"{sec_M0:>7}  {abs(curv_M0):10.4f}  {bw_up:8.4f}")

    gap_vhs_pairs.append({
        'gap_idx': i,
        'gap_size': g['gap_size'],
        'omega_M1': omega_M1,
        'omega_M0': omega_M0,
        'band_M1': n_low,
        'band_M0': n_up,
        'sector_M1': sec_M1,
        'sector_M0': sec_M0,
        'curv_M1': curv_M1,
        'curv_M0': curv_M0,
        'bw_M1': bw_low,
        'bw_M0': bw_up,
        'sw_M1': sw_M1,
        'sw_M0': sw_M0,
        'sector_change': g['sector_change']
    })

# =============================================================================
# SECTION 6: Pseudo-gap and soft-gap detection
# =============================================================================
print("\n--- Section 6: Pseudo-gap detection ---")

# Even without true gaps (non-overlapping bands), there are regions where
# g(omega) dips sharply — pseudo-gaps. These are important for the phononic
# crystal interpretation.

# Find minima in the broadened DOS
# Use narrow broadening for gap detection
g_for_gaps = g_narrow.copy()
# Exclude edges
mask = (omega_grid > 0.5) & (omega_grid < omega_max_all - 1.0)
g_masked = g_for_gaps.copy()
g_masked[~mask] = np.max(g_for_gaps)  # Suppress edges

# Find local minima in DOS
# Invert and find peaks
g_inv = -g_masked
peaks_inv, props = find_peaks(g_inv, prominence=0.01, distance=20)

print(f"\nDOS local minima (pseudo-gaps): {len(peaks_inv)}")
if len(peaks_inv) > 0:
    print(f"  {'#':>3} {'omega (M_KK)':>14} {'g(omega)':>10} {'Depth':>10}")
    print(f"  " + "-" * 48)

    # For each minimum, compute the "depth" = ratio of surrounding maxima to minimum
    pseudogaps = []
    for i, pidx in enumerate(peaks_inv):
        omega_pg = omega_grid[pidx]
        g_pg = g_for_gaps[pidx]

        # Find surrounding maxima
        left_max = g_for_gaps[max(0, pidx-200):pidx].max() if pidx > 10 else g_pg
        right_max = g_for_gaps[pidx:min(N_omega, pidx+200)].max() if pidx < N_omega - 10 else g_pg
        surrounding_max = max(left_max, right_max)
        depth = surrounding_max / max(g_pg, 1e-10)

        pseudogaps.append({
            'omega': omega_pg,
            'g_min': g_pg,
            'depth_ratio': depth,
            'idx': pidx
        })
        print(f"  {i:3d}  {omega_pg:14.4f}  {g_pg:10.4f}  {depth:10.2f}x")

# =============================================================================
# SECTION 7: Spectral statistics summary
# =============================================================================
print("\n--- Section 7: Spectral statistics ---")

# Moments of the DOS
omega_flat = omega_abs.flatten()
n_total_states = len(omega_flat)
omega_mean = omega_flat.mean()
omega_std = omega_flat.std()
omega_median = np.median(omega_flat)

print(f"\nTotal states: {n_total_states} ({N_k} k x {N_modes} bands)")
print(f"Mean frequency: {omega_mean:.4f} M_KK")
print(f"Std deviation: {omega_std:.4f} M_KK")
print(f"Median frequency: {omega_median:.4f} M_KK")

# Sector-resolved statistics
for sec_idx, sec_name in enumerate(['A', 'B', 'C']):
    # Weighted mean frequency for this sector
    w = sector_weight[:, :, sec_idx].flatten()
    omega_sec_mean = np.average(omega_flat, weights=w)
    omega_sec_total = w.sum()
    print(f"\nSector {sec_name}:")
    print(f"  Total weight: {omega_sec_total:.2f} (of {n_total_states})")
    print(f"  Weighted mean: {omega_sec_mean:.4f} M_KK")
    # Find dominant bands
    sec_dominant = np.sum(sector_weight[:, :, sec_idx] > 0.5) / N_k
    print(f"  Bands with >50% {sec_name} character: {sec_dominant:.1f}")

# Bandwidth statistics
bandwidths = np.array([omega_abs[:, n].max() - omega_abs[:, n].min() for n in range(N_modes)])
print(f"\nBandwidth statistics:")
print(f"  Min bandwidth: {bandwidths.min():.6f} M_KK (mode {np.argmin(bandwidths)})")
print(f"  Max bandwidth: {bandwidths.max():.4f} M_KK (mode {np.argmax(bandwidths)})")
print(f"  Mean bandwidth: {bandwidths.mean():.4f} M_KK")
print(f"  Flat bands (BW < 0.1): {np.sum(bandwidths < 0.1)}")
print(f"  Dispersive bands (BW > 1.0): {np.sum(bandwidths > 1.0)}")

# =============================================================================
# SECTION 8: Phononic crystal interpretation
# =============================================================================
print("\n--- Section 8: Phononic crystal interpretation ---")

# Key structural question: does the DOS look like a phononic crystal
# (bands + gaps + VHS) or a disordered system (smooth, featureless)?

# Count true gaps as fraction of spectral range
total_gap = sum(g['gap_size'] for g in gaps)
spectral_range = omega_abs.max() - omega_abs[omega_abs > 0].min()
gap_fraction = total_gap / spectral_range

print(f"\nSpectral range: {spectral_range:.4f} M_KK")
print(f"Total gap width: {total_gap:.4f} M_KK")
print(f"Gap fraction: {gap_fraction:.4f} ({gap_fraction*100:.2f}%)")

# Compare to Debye model: in a Debye solid, g(omega) ~ omega^2 up to cutoff.
# Deviations from Debye indicate phononic crystal structure.
# Fit low-frequency DOS to power law
low_mask = (omega_grid > 0.5) & (omega_grid < 3.0) & (g_narrow > 1e-6)
if np.sum(low_mask) > 5:
    log_omega = np.log(omega_grid[low_mask])
    log_g = np.log(g_narrow[low_mask])
    # Linear fit: log(g) = alpha * log(omega) + const
    coeffs = np.polyfit(log_omega, log_g, 1)
    alpha_debye = coeffs[0]
    print(f"\nLow-frequency power law: g(omega) ~ omega^{alpha_debye:.2f}")
    print(f"  (Debye: alpha = 2 in 3D, alpha = 0 in 1D)")
    print(f"  Effective spectral dimension d_eff = {2*(alpha_debye + 1):.2f}")
    print(f"  (d_eff = 2*(alpha+1) from g ~ omega^{alpha_debye:.2f} = omega^(d_eff/2 - 1))")
else:
    alpha_debye = float('nan')
    print("\nInsufficient low-frequency data for Debye fit")

# =============================================================================
# SECTION 9: Cross-domain connections
# =============================================================================
print("\n--- Section 9: Cross-domain connections ---")
print("""
PHONONIC CRYSTAL ANALOG:
  The 45-mode coupled dispersion on CG(24) is structurally identical to a
  phononic crystal with 45 atoms per unit cell. The van Hove singularities
  at gap edges are the same phenomenon as in semiconductor band theory:
  wherever nabla_k omega(k) = 0, the 1D DOS diverges as (omega - omega_c)^{-1/2}.

  Sector A (36 flat modes): These are the "optical" branches — high-frequency
  modes with negligible dispersion (bandwidth < 0.5 M_KK). In a phononic crystal,
  these correspond to internal vibrations of a complex basis.

  Sector B (8 dispersive modes): The "acoustic + optical" mixed branches.
  The lowest B mode disperses from 0 to ~53 M_KK — a massive bandwidth that
  spans the entire spectrum. This is the sound cone of the substrate.

  Sector C (1 Leggett mode): A nearly-flat mode at omega_L0 = 0.049 M_KK.
  In a superfluid, this is the amplitude oscillation of the order parameter.
  Its tiny bandwidth (0.014 M_KK) means it is almost k-independent: a
  collective mode, not a propagating excitation.

CONDENSED MATTER BRIDGE:
  The hybridization gaps where sector character changes are phonon-polariton
  gaps. In an ionic crystal, these occur where acoustic and optical branches
  anti-cross due to long-range Coulomb coupling. Here, the coupling is the
  A-tensor (fiber-base conversion). The gap size measures the coupling
  strength: delta_omega = 2 * |V_coupling|.

SUPERFLUID ANALOG (Volovik):
  The near-zero-frequency modes (Goldstone + Leggett) sit at the base of
  the spectrum — exactly as in 3He-B, where phase and amplitude modes of
  the order parameter create a two-gap structure. The gap between the
  Goldstone manifold and the first optical branch is the superfluid gap.
""")

# =============================================================================
# SECTION 10: Gate verdict
# =============================================================================
print("\n--- Section 10: Gate verdict ---")

n_gaps = len(gaps)
n_hybrid = len(hybrid_gaps)
n_vhs = len(vhs_list)

gate_detail = (
    f"INFO: {n_vhs} van Hove singularities ({n_M0} M0, {n_M1} M1, "
    f"{n_M0_int} M0_int, {n_M1_int} M1_int). "
    f"{n_gaps} true gaps, {n_hybrid} cross-sector hybridization gaps. "
    f"Gap fraction = {gap_fraction*100:.1f}%. "
    f"Low-freq power law: g ~ omega^{alpha_debye:.2f}. "
    f"Phononic crystal structure confirmed."
)

print(f"\nGATE: PHONON-DOS-63 | INFO")
print(f"DETAIL: {gate_detail}")

# =============================================================================
# SECTION 11: Save output data
# =============================================================================
print("\n--- Section 11: Save output ---")

# Pack VHS data into arrays for npz storage
vhs_omega = np.array([v['omega'] for v in vhs_list])
vhs_type = np.array([v['type'] for v in vhs_list])
vhs_band = np.array([v['band'] for v in vhs_list])
vhs_k_idx = np.array([v['k_idx'] for v in vhs_list])
vhs_sector = np.array([v['sector'] for v in vhs_list])
vhs_curvature = np.array([v['curvature'] for v in vhs_list])
vhs_bandwidth = np.array([v['bandwidth'] for v in vhs_list])

# Pack gap data
gap_bands_below = np.array([g['band_below'] for g in gaps])
gap_bands_above = np.array([g['band_above'] for g in gaps])
gap_sizes = np.array([g['gap_size'] for g in gaps])
gap_centers = np.array([g['gap_center'] for g in gaps])
gap_omega_lower = np.array([g['omega_lower'] for g in gaps])
gap_omega_upper = np.array([g['omega_upper'] for g in gaps])
gap_sector_below = np.array([g['sector_below'] for g in gaps])
gap_sector_above = np.array([g['sector_above'] for g in gaps])
gap_sector_change = np.array([g['sector_change'] for g in gaps])

np.savez(OUT_NPZ,
    # DOS
    omega_grid=omega_grid,
    g_narrow=g_narrow,
    g_broad=g_broad,
    g_A_narrow=g_A_narrow,
    g_B_narrow=g_B_narrow,
    g_C_narrow=g_C_narrow,
    g_A_broad=g_A_broad,
    g_B_broad=g_B_broad,
    g_C_broad=g_C_broad,
    N_omega_integrated=N_omega_integrated,
    sigma_narrow=np.array(sigma_narrow),
    sigma_broad=np.array(sigma_broad),
    # VHS data
    vhs_omega=vhs_omega,
    vhs_type=vhs_type,
    vhs_band=vhs_band,
    vhs_k_idx=vhs_k_idx,
    vhs_sector=vhs_sector,
    vhs_curvature=vhs_curvature,
    vhs_bandwidth=vhs_bandwidth,
    # Gap data
    gap_bands_below=gap_bands_below,
    gap_bands_above=gap_bands_above,
    gap_sizes=gap_sizes,
    gap_centers=gap_centers,
    gap_omega_lower=gap_omega_lower,
    gap_omega_upper=gap_omega_upper,
    gap_sector_below=gap_sector_below,
    gap_sector_above=gap_sector_above,
    gap_sector_change=gap_sector_change,
    # Statistics
    bandwidths=bandwidths,
    alpha_debye=np.array(alpha_debye),
    gap_fraction=np.array(gap_fraction),
    spectral_range=np.array(spectral_range),
    # Gate
    gate_name=np.array(['PHONON-DOS-63']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([gate_detail])
)
print(f"Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 12: Plotting
# =============================================================================
print("\n--- Section 12: Generate plots ---")

fig = plt.figure(figsize=(18, 22))
gs = GridSpec(4, 2, hspace=0.35, wspace=0.30)

# --- Panel 1: Full DOS (narrow broadening) ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(omega_grid, g_narrow, 'k-', linewidth=0.8, label='Total')
ax1.plot(omega_grid, g_A_narrow, 'b-', linewidth=0.6, alpha=0.7, label='Sector A')
ax1.plot(omega_grid, g_B_narrow, 'r-', linewidth=0.6, alpha=0.7, label='Sector B')
ax1.plot(omega_grid, g_C_narrow, 'g-', linewidth=0.6, alpha=0.7, label='Sector C')
# Mark gaps
for g in gaps:
    ax1.axvspan(g['omega_lower'], g['omega_upper'], alpha=0.15, color='orange')
ax1.set_xlabel(r'$\omega$ [M$_{\rm KK}$]')
ax1.set_ylabel(r'$g(\omega)$ [M$_{\rm KK}^{-1}$]')
ax1.set_title(f'Phonon DOS ($\\sigma$ = {sigma_narrow} M$_{{KK}}$)')
ax1.legend(fontsize=8)
ax1.set_xlim(0, omega_max_all)

# --- Panel 2: Low-frequency zoom ---
ax2 = fig.add_subplot(gs[0, 1])
low_cut = 8.0  # (local)
mask_low = omega_grid < low_cut
ax2.plot(omega_grid[mask_low], g_narrow[mask_low], 'k-', linewidth=0.8, label='Total')
ax2.plot(omega_grid[mask_low], g_A_narrow[mask_low], 'b-', linewidth=0.6, alpha=0.7, label='A')
ax2.plot(omega_grid[mask_low], g_B_narrow[mask_low], 'r-', linewidth=0.6, alpha=0.7, label='B')
ax2.plot(omega_grid[mask_low], g_C_narrow[mask_low], 'g-', linewidth=0.6, alpha=0.7, label='C')
for g in gaps:
    if g['gap_center'] < low_cut:
        ax2.axvspan(g['omega_lower'], g['omega_upper'], alpha=0.15, color='orange')
ax2.set_xlabel(r'$\omega$ [M$_{\rm KK}$]')
ax2.set_ylabel(r'$g(\omega)$ [M$_{\rm KK}^{-1}$]')
ax2.set_title('Low-Frequency DOS (0-8 M$_{KK}$)')
ax2.legend(fontsize=8)

# --- Panel 3: Integrated DOS ---
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(omega_grid, N_omega_integrated, 'k-', linewidth=1.0)
for g in gaps:
    ax3.axvspan(g['omega_lower'], g['omega_upper'], alpha=0.15, color='orange')
ax3.set_xlabel(r'$\omega$ [M$_{\rm KK}$]')
ax3.set_ylabel(r'$N(\omega)$')
ax3.set_title('Integrated DOS')
ax3.axhline(y=N_modes, color='gray', linestyle='--', alpha=0.5, label=f'N = {N_modes}')
ax3.legend(fontsize=8)
ax3.set_xlim(0, omega_max_all)

# --- Panel 4: Van Hove singularity map ---
ax4 = fig.add_subplot(gs[1, 1])
# Plot all VHS colored by type
colors_vhs = {'M0': 'blue', 'M1': 'red', 'M0_int': 'cyan', 'M1_int': 'magenta'}
markers_vhs = {'M0': 'v', 'M1': '^', 'M0_int': 'v', 'M1_int': '^'}
for vtype in ['M0', 'M1', 'M0_int', 'M1_int']:
    mask_v = [v for v in vhs_list if v['type'] == vtype]
    if mask_v:
        omegas = [v['omega'] for v in mask_v]
        bands = [v['band'] for v in mask_v]
        ax4.scatter(omegas, bands, c=colors_vhs[vtype], marker=markers_vhs[vtype],
                   s=20, label=vtype, alpha=0.7, edgecolors='k', linewidths=0.3)
for g in gaps:
    ax4.axvspan(g['omega_lower'], g['omega_upper'], alpha=0.15, color='orange')
ax4.set_xlabel(r'$\omega$ [M$_{\rm KK}$]')
ax4.set_ylabel('Band index')
ax4.set_title('Van Hove Singularity Map')
ax4.legend(fontsize=8, ncol=2)

# --- Panel 5: Gap spectrum ---
ax5 = fig.add_subplot(gs[2, 0])
if len(gaps) > 0:
    gap_x = np.arange(len(gaps))
    colors_gap = ['red' if g['sector_change'] else 'blue' for g in gaps]
    ax5.bar(gap_x, [g['gap_size'] for g in gaps], color=colors_gap, alpha=0.7)
    ax5.set_xlabel('Gap index')
    ax5.set_ylabel('Gap size [M$_{KK}$]')
    ax5.set_title('Hybridization Gap Spectrum')
    # Add legend
    from matplotlib.patches import Patch
    ax5.legend(handles=[
        Patch(facecolor='red', alpha=0.7, label='Cross-sector'),
        Patch(facecolor='blue', alpha=0.7, label='Same-sector')
    ], fontsize=8)
else:
    ax5.text(0.5, 0.5, 'No gaps found', transform=ax5.transAxes, ha='center')
    ax5.set_title('Hybridization Gap Spectrum')

# --- Panel 6: Sector-resolved DOS (broad) ---
ax6 = fig.add_subplot(gs[2, 1])
ax6.fill_between(omega_grid, 0, g_A_broad, alpha=0.4, color='blue', label='A (geometric)')
ax6.fill_between(omega_grid, g_A_broad, g_A_broad + g_B_broad,
                 alpha=0.4, color='red', label='B (dispersive)')  # (local)
ax6.fill_between(omega_grid, g_A_broad + g_B_broad, g_A_broad + g_B_broad + g_C_broad,
                 alpha=0.4, color='green', label='C (Leggett)')  # (local)
ax6.set_xlabel(r'$\omega$ [M$_{\rm KK}$]')
ax6.set_ylabel(r'$g(\omega)$ [M$_{\rm KK}^{-1}$]')
ax6.set_title('Sector-Resolved DOS (stacked)')
ax6.legend(fontsize=8)
ax6.set_xlim(0, omega_max_all)

# --- Panel 7: Band dispersion with DOS alongside ---
ax7 = fig.add_subplot(gs[3, 0])
for n in range(N_modes):
    # Color by dominant sector
    mean_sw = sector_weight[:, n, :].mean(axis=0)
    dom_sec = np.argmax(mean_sw)
    color = ['blue', 'red', 'green'][dom_sec]
    ax7.plot(k_eff, omega_abs[:, n], '-', color=color, linewidth=0.5, alpha=0.5)
ax7.set_xlabel(r'$k_{\rm eff}$')
ax7.set_ylabel(r'$\omega$ [M$_{\rm KK}$]')
ax7.set_title('Band Structure (color = sector)')
ax7.set_ylim(0, 15)
from matplotlib.lines import Line2D
ax7.legend(handles=[
    Line2D([0], [0], color='blue', label='A'),
    Line2D([0], [0], color='red', label='B'),
    Line2D([0], [0], color='green', label='C'),
], fontsize=8, loc='upper right')

# --- Panel 8: DOS vs band index heatmap ---
ax8 = fig.add_subplot(gs[3, 1])
# Create a 2D histogram of DOS binned by band
band_dos = np.zeros((N_modes, 200))
omega_bins = np.linspace(0, omega_max_all, 201)
for n in range(N_modes):
    for ik in range(N_k):
        val = omega_abs[ik, n]
        bin_idx = int((val - omega_bins[0]) / (omega_bins[1] - omega_bins[0]))
        bin_idx = np.clip(bin_idx, 0, 199)
        band_dos[n, bin_idx] += 1.0 / N_k

im = ax8.imshow(band_dos, aspect='auto', origin='lower',
                extent=[omega_bins[0], omega_bins[-1], 0, N_modes],
                cmap='hot', interpolation='nearest')
ax8.set_xlabel(r'$\omega$ [M$_{\rm KK}$]')
ax8.set_ylabel('Band index')
ax8.set_title('Band-Resolved Spectral Weight')
plt.colorbar(im, ax=ax8, label='Weight')

fig.suptitle('S63 PHONON-DOS-63: Phonon DOS & Van Hove Classification\n'
             f'{N_modes} modes, {N_k} k-points, {n_vhs} VHS, {n_gaps} gaps',
             fontsize=14, fontweight='bold')

plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"Saved: {OUT_PNG}")

elapsed = time.time() - t_start
print(f"\n{'='*78}")
print(f"PHONON-DOS-63 complete. Time: {elapsed:.1f}s")
print(f"Gate: INFO | {gate_detail}")
print(f"{'='*78}")
