"""
Session 43 W1-4: Phonon Density of States at the Fold (DOS-43)

Computes the multiplicity-weighted phonon density of states rho(omega) from
all 992 D_K eigenvalues at the Jensen fold (tau=0.20), identifies van Hove
singularities, cumulative distribution, and per-sector decomposition.

Physical setup:
    - D_K eigenvalues from the restricted Dirac operator on M4 x SU(3)
      with Jensen TT-deformation at tau = 0.20 (closest grid point to fold 0.190)
    - 9 sectors: (p,q) = (0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1)
    - 992 stored eigenvalues (spinor-level, distinct within each sector)
    - Physical multiplicity: each eigenvalue in sector (p,q) appears dim(p,q)^2
      times in the full Peter-Weyl expansion on SU(3)
    - Total physical modes (with Peter-Weyl multiplicity): 101,984

Phononic interpretation:
    |eigenvalue| = omega = phonon frequency (in M_KK units)
    rho(omega) = density of phonon modes per unit frequency
    Each sector (p,q) = Brillouin zone of the internal-space phononic crystal
    Van Hove singularities = band edges where grad_k(omega) = 0

Gate: DOS-43 (INFO -- diagnostic, feeds W1-2 Lifshitz classification)

Author: quantum-acoustics-theorist (Session 43)
Date: 2026-03-14
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ================================================================
# 1. LOAD EIGENVALUE DATA
# ================================================================

print("=" * 70)
print("Session 43 W1-4: Phonon DOS at the Fold")
print("=" * 70)

# Primary source: s27_multisector_bcs.npz has per-sector eigenvalues
bcs_path = os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz")
bcs_data = np.load(bcs_path, allow_pickle=True)

sectors = bcs_data['sectors']
tau_values = bcs_data['tau_values']
idx_fold = 3  # tau = 0.20
tau_fold = tau_values[idx_fold]

print(f"\nUsing tau = {tau_fold:.2f} (closest grid point to fold tau=0.190)")
print(f"Sectors: {len(sectors)}")

# ================================================================
# 2. EXTRACT ALL EIGENVALUES WITH SECTOR LABELS AND MULTIPLICITIES
# ================================================================

# Build arrays: omega[i], dim2[i], sector_p[i], sector_q[i]
all_omega = []       # |eigenvalue| = phonon frequency
all_dim2 = []        # Peter-Weyl multiplicity dim(p,q)^2
all_sector_p = []    # p label
all_sector_q = []    # q label

sector_data = {}     # (p,q) -> array of |eigenvalues|

for row in sectors:
    p, q, dim, dim2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
    key = f'evals_{p}_{q}_{idx_fold}'
    evals = bcs_data[key]
    abs_evals = np.abs(evals)

    sector_data[(p, q)] = abs_evals

    for ev in abs_evals:
        all_omega.append(ev)
        all_dim2.append(dim2)
        all_sector_p.append(p)
        all_sector_q.append(q)

all_omega = np.array(all_omega)
all_dim2 = np.array(all_dim2)
all_sector_p = np.array(all_sector_p)
all_sector_q = np.array(all_sector_q)

n_stored = len(all_omega)
n_physical = np.sum(all_dim2)

print(f"\nEigenvalue census:")
print(f"  Stored eigenvalues (spinor-level): {n_stored}")
print(f"  Physical modes (with dim^2 weighting): {n_physical}")
print(f"  Frequency range: [{all_omega.min():.4f}, {all_omega.max():.4f}] M_KK")
print(f"  Spectral gap (from zero): {all_omega.min():.4f} M_KK")

# ================================================================
# 3. CONSTRUCT MULTIPLICITY-WEIGHTED HISTOGRAM rho(omega)
# ================================================================

# Bin width 0.02 M_KK across [0.8, 2.1] M_KK
bin_width = 0.02
omega_min, omega_max = 0.80, 2.10
bins = np.arange(omega_min, omega_max + bin_width, bin_width)
bin_centers = 0.5 * (bins[:-1] + bins[1:])
n_bins = len(bin_centers)

# Histogram A: unweighted (992 eigenvalues, each weight 1)
hist_unweighted, _ = np.histogram(all_omega, bins=bins)

# Histogram B: dim^2-weighted (each eigenvalue weighted by its sector's dim^2)
hist_weighted, _ = np.histogram(all_omega, bins=bins, weights=all_dim2.astype(float))

# Normalize to density of states (modes per M_KK per bin)
rho_unweighted = hist_unweighted / bin_width  # modes / M_KK (stored)
rho_weighted = hist_weighted / bin_width       # modes / M_KK (physical)

print(f"\nHistogram parameters:")
print(f"  Bin width: {bin_width} M_KK")
print(f"  Range: [{omega_min}, {omega_max}] M_KK")
print(f"  Number of bins: {n_bins}")
print(f"  Total unweighted count: {hist_unweighted.sum()} (expect {n_stored})")
print(f"  Total weighted count: {hist_weighted.sum():.0f} (expect {n_physical})")

# ================================================================
# 4. CUMULATIVE DISTRIBUTION N(omega)
# ================================================================

# N(omega) = integral from 0 to omega of rho(omega') domega'
# = cumulative sum of histogram

N_cumulative_unweighted = np.cumsum(hist_unweighted)
N_cumulative_weighted = np.cumsum(hist_weighted)

print(f"\nCumulative distribution:")
print(f"  N(omega_max) unweighted: {N_cumulative_unweighted[-1]}")
print(f"  N(omega_max) weighted: {N_cumulative_weighted[-1]:.0f}")

# Fractional cumulative (for identifying quartiles etc.)
N_frac_unweighted = N_cumulative_unweighted / N_cumulative_unweighted[-1]
N_frac_weighted = N_cumulative_weighted / N_cumulative_weighted[-1]

# Find median, quartiles
for label, N_frac in [("unweighted", N_frac_unweighted), ("weighted", N_frac_weighted)]:
    q25_idx = np.searchsorted(N_frac, 0.25)
    q50_idx = np.searchsorted(N_frac, 0.50)
    q75_idx = np.searchsorted(N_frac, 0.75)
    print(f"  {label}: Q25={bin_centers[min(q25_idx,n_bins-1)]:.3f}, "
          f"Q50={bin_centers[min(q50_idx,n_bins-1)]:.3f}, "
          f"Q75={bin_centers[min(q75_idx,n_bins-1)]:.3f} M_KK")

# ================================================================
# 5. PER-SECTOR DECOMPOSITION
# ================================================================

# Group sectors as specified:
# Group 1: (0,0) -- singlet
# Group 2: (1,0) + (0,1) -- fundamental + antifundamental
# Group 3: (1,1) -- adjoint
# Group 4: (2,0) + (0,2) -- symmetric + antisymmetric
# Group 5: (3,0) + (0,3) -- decuplet + anti-decuplet
# Group 6: (2,1) + (1,2) -- but we only have (2,1), no (1,2) in data

sector_groups = {
    '(0,0)': [(0, 0)],
    '(1,0)+(0,1)': [(1, 0), (0, 1)],
    '(1,1)': [(1, 1)],
    '(2,0)+(0,2)': [(2, 0), (0, 2)],
    '(3,0)+(0,3)': [(3, 0), (0, 3)],
    '(2,1)': [(2, 1)],
}

# Branch labels (B1, B2, B3 classification from S31Ca)
branch_map = {
    (0, 0): 'B1',
    (1, 0): 'B1', (0, 1): 'B1',
    (1, 1): 'B2',
    (2, 0): 'B3', (0, 2): 'B3',
    (3, 0): 'B3', (0, 3): 'B3',
    (2, 1): 'B3',
}

print(f"\n{'='*70}")
print(f"PER-SECTOR DECOMPOSITION")
print(f"{'='*70}")
print(f"\n{'Group':>18s} {'Branch':>6s} {'dim^2':>6s} {'N_ev':>5s} {'N_phys':>8s} "
      f"{'omega_min':>9s} {'omega_max':>9s} {'BW':>7s} {'BW<0.05?':>9s}")
print("-" * 90)

group_histograms_uw = {}   # unweighted
group_histograms_w = {}    # dim^2-weighted
group_stats = {}

for gname, sector_list in sector_groups.items():
    # Collect eigenvalues for this group
    mask = np.zeros(n_stored, dtype=bool)
    total_dim2 = 0
    for (p, q) in sector_list:
        sector_mask = (all_sector_p == p) & (all_sector_q == q)
        mask |= sector_mask
        if np.any(sector_mask):
            total_dim2 = all_dim2[sector_mask][0]  # dim^2 for this sector

    group_omega = all_omega[mask]
    group_dim2 = all_dim2[mask]
    n_ev = len(group_omega)
    n_phys = int(np.sum(group_dim2))

    # Histograms
    h_uw, _ = np.histogram(group_omega, bins=bins)
    h_w, _ = np.histogram(group_omega, bins=bins, weights=group_dim2.astype(float))
    group_histograms_uw[gname] = h_uw
    group_histograms_w[gname] = h_w

    # Stats
    if n_ev > 0:
        om_min = group_omega.min()
        om_max = group_omega.max()
        bw = om_max - om_min
        flat = bw < 0.05
    else:
        om_min = om_max = bw = 0.0
        flat = True

    branch = branch_map.get(sector_list[0], '?')
    group_stats[gname] = {
        'branch': branch,
        'dim2': total_dim2,
        'n_ev': n_ev,
        'n_phys': n_phys,
        'omega_min': om_min,
        'omega_max': om_max,
        'bandwidth': bw,
        'flat_band': flat,
    }

    flat_str = "YES" if flat else "no"
    print(f"{gname:>18s} {branch:>6s} {total_dim2:>6d} {n_ev:>5d} {n_phys:>8d} "
          f"{om_min:>9.4f} {om_max:>9.4f} {bw:>7.4f} {flat_str:>9s}")

# Branch-level aggregation
print(f"\n{'--- Branch-level aggregation ---':>40s}")
branch_stats = defaultdict(lambda: {'n_ev': 0, 'n_phys': 0, 'omega_min': np.inf,
                                      'omega_max': -np.inf})
for gname, stats in group_stats.items():
    b = stats['branch']
    branch_stats[b]['n_ev'] += stats['n_ev']
    branch_stats[b]['n_phys'] += stats['n_phys']
    branch_stats[b]['omega_min'] = min(branch_stats[b]['omega_min'], stats['omega_min'])
    branch_stats[b]['omega_max'] = max(branch_stats[b]['omega_max'], stats['omega_max'])

for b in ['B1', 'B2', 'B3']:
    bs = branch_stats[b]
    bw = bs['omega_max'] - bs['omega_min']
    print(f"  {b}: N_ev={bs['n_ev']:>4d}, N_phys={bs['n_phys']:>6d}, "
          f"range=[{bs['omega_min']:.4f}, {bs['omega_max']:.4f}], BW={bw:.4f} M_KK")

# ================================================================
# 6. VAN HOVE SINGULARITY IDENTIFICATION
# ================================================================

print(f"\n{'='*70}")
print(f"VAN HOVE SINGULARITY ANALYSIS")
print(f"{'='*70}")

# Van Hove singularities occur at critical points of the dispersion
# relation: omega(k) where grad_k omega = 0.
# In a histogram, they manifest as:
#   M_0 (band minimum): step onset in rho(omega) -- rising edge
#   M_1 (saddle point): logarithmic peak in rho (2D) or kink (3D)
#   M_2 (band maximum): step cutoff in rho(omega) -- falling edge
#   M_3 (flat band): delta-function peak -- extremely high rho in narrow bin range

# Since we have a discrete spectrum (not continuous dispersion), we identify
# VH singularities as:
# 1. Sharp peaks in rho(omega) (more than 2x the local average)
# 2. Band edges of each sector (onset and cutoff)
# 3. Flat bands (bandwidth < 0.05 M_KK)

# Method: find peaks in the weighted DOS histogram
# Smooth first to avoid noise

from scipy.signal import find_peaks, savgol_filter

# Smooth the weighted DOS with Savitzky-Golay filter
# Window must be odd and >= 5
window = min(11, n_bins if n_bins % 2 == 1 else n_bins - 1)
if window < 5:
    window = 5
rho_smooth = savgol_filter(rho_weighted, window, 3)

# Find peaks in the smoothed DOS
# Prominence > 20% of max height
peak_height_threshold = 0.20 * rho_smooth.max()
peaks, peak_props = find_peaks(rho_smooth, prominence=peak_height_threshold * 0.5,
                                height=peak_height_threshold * 0.3)

print(f"\nSmoothed DOS analysis (Savitzky-Golay, window={window}):")
print(f"  Max rho(omega) [weighted]: {rho_weighted.max():.1f} modes/M_KK")
print(f"  Max rho(omega) [smoothed]: {rho_smooth.max():.1f} modes/M_KK")
print(f"  Peak detection threshold: {peak_height_threshold:.1f} modes/M_KK")
print(f"  Number of peaks found: {len(peaks)}")

# Classify each peak
vh_singularities = []
for i, pk in enumerate(peaks):
    omega_pk = bin_centers[pk]
    rho_pk = rho_smooth[pk]
    prom = peak_props['prominences'][i]

    # Classify by checking if it corresponds to a band edge
    # Check which sectors have eigenvalues near this peak
    contributing_sectors = []
    for gname, stats in group_stats.items():
        if stats['omega_min'] - 0.03 <= omega_pk <= stats['omega_max'] + 0.03:
            contributing_sectors.append(gname)

    # Check if it's at a band edge
    is_band_min = False
    is_band_max = False
    for gname, stats in group_stats.items():
        if abs(omega_pk - stats['omega_min']) < 0.04:
            is_band_min = True
        if abs(omega_pk - stats['omega_max']) < 0.04:
            is_band_max = True

    # Classify
    if is_band_min and is_band_max:
        vh_type = "M_0/M_2"  # coincident minimum and maximum (narrow band)
    elif is_band_min:
        vh_type = "M_0"  # band minimum
    elif is_band_max:
        vh_type = "M_2"  # band maximum
    else:
        # Interior peak -> saddle point (M_1) or flat band accumulation (M_3)
        # Check local flatness: if many eigenvalues cluster in narrow range
        nearby_count = np.sum(np.abs(all_omega - omega_pk) < 0.03)
        if nearby_count > 30:  # significant clustering
            vh_type = "M_3"  # flat band accumulation
        else:
            vh_type = "M_1"  # saddle point

    vh_singularities.append({
        'omega': omega_pk,
        'rho': rho_pk,
        'prominence': prom,
        'type': vh_type,
        'sectors': contributing_sectors,
    })

    print(f"  Peak {i+1}: omega={omega_pk:.3f} M_KK, rho={rho_pk:.0f}, "
          f"prom={prom:.0f}, type={vh_type}, sectors={contributing_sectors}")

# Also identify band edges directly
print(f"\nBand edges (sector-level):")
band_edges = []
for gname, stats in group_stats.items():
    if stats['n_ev'] > 0:
        band_edges.append({
            'omega': stats['omega_min'],
            'type': 'M_0 (onset)',
            'sector': gname,
        })
        band_edges.append({
            'omega': stats['omega_max'],
            'type': 'M_2 (cutoff)',
            'sector': gname,
        })

band_edges.sort(key=lambda x: x['omega'])
for be in band_edges:
    print(f"  omega={be['omega']:.4f}: {be['type']} from {be['sector']}")

# Count distinct VH singularities (merge nearby ones)
vh_omega_list = [v['omega'] for v in vh_singularities]
for be in band_edges:
    # Check if this band edge is already captured by a peak
    already_found = False
    for vo in vh_omega_list:
        if abs(vo - be['omega']) < 0.04:
            already_found = True
            break
    if not already_found:
        vh_singularities.append({
            'omega': be['omega'],
            'rho': 0,  # edge, not peak
            'prominence': 0,
            'type': be['type'].split()[0],
            'sectors': [be['sector']],
        })

n_vh = len(vh_singularities)
print(f"\nTotal van Hove singularities (peaks + distinct edges): {n_vh}")

# Flat-band fraction
n_flat = sum(1 for stats in group_stats.values() if stats['flat_band'])
n_groups = len(group_stats)
flat_frac = n_flat / n_groups
print(f"Flat-band fraction: {n_flat}/{n_groups} = {flat_frac:.2f}")

# ================================================================
# 7. GLOBAL SPECTRAL STATISTICS
# ================================================================

print(f"\n{'='*70}")
print(f"GLOBAL SPECTRAL STATISTICS")
print(f"{'='*70}")

omega_gap = all_omega.min()
omega_max_val = all_omega.max()
total_bandwidth = omega_max_val - omega_gap
mean_omega = np.average(all_omega, weights=all_dim2)
std_omega = np.sqrt(np.average((all_omega - mean_omega)**2, weights=all_dim2))

# Mean level spacing (unweighted)
sorted_omega = np.sort(all_omega)
spacings = np.diff(sorted_omega)
mean_spacing = np.mean(spacings)
min_spacing = np.min(spacings)

# Weighted mean level spacing
sorted_unique = np.unique(np.round(all_omega, 6))
unique_spacings = np.diff(sorted_unique)
mean_unique_spacing = np.mean(unique_spacings) if len(unique_spacings) > 0 else 0

print(f"  Spectral gap (from zero): {omega_gap:.4f} M_KK")
print(f"  Maximum frequency: {omega_max_val:.4f} M_KK")
print(f"  Total bandwidth: {total_bandwidth:.4f} M_KK")
print(f"  Weighted mean frequency: {mean_omega:.4f} M_KK")
print(f"  Weighted std deviation: {std_omega:.4f} M_KK")
print(f"  Mean spacing (992 eigenvalues): {mean_spacing:.6f} M_KK")
print(f"  Min spacing: {min_spacing:.6e} M_KK")
print(f"  Number of unique mass values: {len(sorted_unique)}")
print(f"  Mean unique spacing: {mean_unique_spacing:.6f} M_KK")

# First and second moments (phonon thermodynamics)
# <omega> = mean phonon frequency
# <omega^2> = mean square frequency (related to Debye temperature)
omega_1 = np.average(all_omega, weights=all_dim2)
omega_2 = np.average(all_omega**2, weights=all_dim2)
omega_rms = np.sqrt(omega_2)
omega_log = np.exp(np.average(np.log(all_omega), weights=all_dim2))

print(f"\n  Phonon frequency moments (dim^2-weighted):")
print(f"    <omega>     = {omega_1:.4f} M_KK")
print(f"    <omega^2>   = {omega_2:.4f} M_KK^2")
print(f"    omega_rms   = {omega_rms:.4f} M_KK")
print(f"    omega_log   = {omega_log:.4f} M_KK (logarithmic average)")

# Debye-like temperature
# In standard phonon theory: Theta_D ~ hbar * omega_max / k_B
# Here omega_max = 2.0767 M_KK
print(f"    Theta_D analogue = omega_max = {omega_max_val:.4f} M_KK")

# Einstein-like temperature
# Theta_E ~ hbar * <omega> / k_B
print(f"    Theta_E analogue = <omega> = {omega_1:.4f} M_KK")

# ================================================================
# 8. CROSS-CHECKS
# ================================================================

print(f"\n{'='*70}")
print(f"CROSS-CHECKS")
print(f"{'='*70}")

# Cross-check 1: total eigenvalue count
assert n_stored == 992, f"Expected 992 stored eigenvalues, got {n_stored}"
print(f"  [PASS] Total stored eigenvalues: {n_stored} == 992")

# Cross-check 2: histogram sums
uw_sum = hist_unweighted.sum()
w_sum = hist_weighted.sum()
# Some eigenvalues may fall outside the bin range
outside_range = np.sum((all_omega < omega_min) | (all_omega > omega_max))
print(f"  [INFO] Eigenvalues outside histogram range: {outside_range}")
assert abs(uw_sum + outside_range - n_stored) == 0, \
    f"Unweighted sum {uw_sum} + outside {outside_range} != {n_stored}"
print(f"  [PASS] Unweighted histogram sum: {uw_sum} + {outside_range} outside = {n_stored}")

# Cross-check 3: conjugate sectors have identical spectra
for (p1, q1), (p2, q2) in [((1,0),(0,1)), ((2,0),(0,2)), ((3,0),(0,3))]:
    s1 = np.sort(sector_data[(p1, q1)])
    s2 = np.sort(sector_data[(p2, q2)])
    if len(s1) == len(s2) and np.allclose(s1, s2, atol=1e-10):
        print(f"  [PASS] Conjugate pair ({p1},{q1}) and ({p2},{q2}): identical spectra")
    else:
        print(f"  [WARN] ({p1},{q1}) and ({p2},{q2}): spectra differ (max diff: {np.max(np.abs(s1-s2)):.2e})")

# Cross-check 4: spectral gap matches S42 HF data
hf_data = np.load(os.path.join(SCRIPT_DIR, "s42_hauser_feshbach.npz"), allow_pickle=True)
m_lightest_hf = float(hf_data['m_lightest'])
print(f"  [INFO] m_lightest (this): {omega_gap:.4f}, m_lightest (HF-42): {m_lightest_hf:.4f}")
assert abs(omega_gap - m_lightest_hf) < 0.001, "Spectral gap mismatch with HF-42"
print(f"  [PASS] Spectral gap consistent with HF-42")

# Cross-check 5: per-sector eigenvalue count matches dim^2 relationship
for row in sectors:
    p, q, dim, dim2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
    n_ev = len(sector_data[(p, q)])
    # The number of Dirac eigenvalues in sector (p,q) should be
    # related to the spinor structure: 16 for singlet, scaled by sector content
    expected_ratio = n_ev / 16  # ratio to singlet count
    print(f"  [INFO] ({p},{q}): n_ev={n_ev}, n_ev/16={expected_ratio:.2f}, dim^2={dim2}")

# ================================================================
# 9. SAVE RESULTS
# ================================================================

print(f"\n{'='*70}")
print(f"SAVING RESULTS")
print(f"{'='*70}")

# Compile van Hove data
vh_omega_arr = np.array([v['omega'] for v in vh_singularities])
vh_rho_arr = np.array([v['rho'] for v in vh_singularities])
vh_types = np.array([v['type'] for v in vh_singularities])

output_data = {
    # Metadata
    'tau_fold': tau_fold,
    'n_stored': n_stored,
    'n_physical': n_physical,

    # Raw eigenvalues with labels
    'all_omega': all_omega,
    'all_dim2': all_dim2,
    'all_sector_p': all_sector_p,
    'all_sector_q': all_sector_q,

    # Histogram
    'bins': bins,
    'bin_centers': bin_centers,
    'bin_width': bin_width,
    'hist_unweighted': hist_unweighted,
    'hist_weighted': hist_weighted,
    'rho_unweighted': rho_unweighted,
    'rho_weighted': rho_weighted,
    'rho_smooth': rho_smooth,

    # Cumulative distribution
    'N_cumulative_unweighted': N_cumulative_unweighted,
    'N_cumulative_weighted': N_cumulative_weighted,

    # Per-sector histograms (unweighted)
    **{f'hist_uw_{gname}': group_histograms_uw[gname] for gname in group_histograms_uw},
    **{f'hist_w_{gname}': group_histograms_w[gname] for gname in group_histograms_w},

    # Global statistics
    'omega_gap': omega_gap,
    'omega_max': omega_max_val,
    'total_bandwidth': total_bandwidth,
    'mean_omega': mean_omega,
    'std_omega': std_omega,
    'omega_rms': omega_rms,
    'omega_log': omega_log,
    'mean_spacing': mean_spacing,
    'min_spacing': min_spacing,

    # Van Hove singularities
    'vh_omega': vh_omega_arr,
    'vh_rho': vh_rho_arr,
    'vh_types': vh_types,
    'n_vh_singularities': n_vh,

    # Flat band info
    'n_flat_bands': n_flat,
    'n_groups': n_groups,
    'flat_band_fraction': flat_frac,

    # Per-sector statistics
    'group_names': np.array(list(group_stats.keys())),
    'group_branches': np.array([group_stats[g]['branch'] for g in group_stats]),
    'group_n_ev': np.array([group_stats[g]['n_ev'] for g in group_stats]),
    'group_n_phys': np.array([group_stats[g]['n_phys'] for g in group_stats]),
    'group_omega_min': np.array([group_stats[g]['omega_min'] for g in group_stats]),
    'group_omega_max': np.array([group_stats[g]['omega_max'] for g in group_stats]),
    'group_bandwidth': np.array([group_stats[g]['bandwidth'] for g in group_stats]),
    'group_flat': np.array([group_stats[g]['flat_band'] for g in group_stats]),
}

output_path = os.path.join(SCRIPT_DIR, "s43_phonon_dos.npz")
np.savez_compressed(output_path, **output_data)
print(f"Saved: {output_path}")

# ================================================================
# 10. PLOTS
# ================================================================

fig = plt.figure(figsize=(16, 14))
fig.suptitle(f"Phonon DOS at the Fold (DOS-43, $\\tau={tau_fold:.2f}$)",
             fontsize=14, fontweight='bold')

# Layout: 3x2 grid
# Panel A: Full DOS (weighted + unweighted)
ax1 = fig.add_subplot(3, 2, 1)
ax1.bar(bin_centers, rho_weighted, width=bin_width*0.9, alpha=0.6,
        color='steelblue', label=f'Weighted (N={n_physical})')
ax1.plot(bin_centers, rho_smooth, 'r-', lw=2, label='Smoothed')
# Mark van Hove peaks
for vh in vh_singularities:
    if vh['rho'] > 0:
        marker = {'M_0': 'v', 'M_1': 's', 'M_2': '^', 'M_3': 'D',
                  'M_0/M_2': 'o'}.get(vh['type'], 'o')
        ax1.plot(vh['omega'], vh['rho'], marker, color='red', markersize=8,
                 label=f"{vh['type']} ({vh['omega']:.2f})" if vh == vh_singularities[0] else '')
ax1.set_xlabel('$\\omega$ ($M_{KK}$)')
ax1.set_ylabel('$\\rho(\\omega)$ (modes / $M_{KK}$)')
ax1.set_title('Density of States (dim$^2$-weighted)')
ax1.legend(fontsize=7, loc='upper right')
ax1.axvline(omega_gap, color='green', ls=':', lw=1, alpha=0.7)
ax1.set_xlim(omega_min, omega_max)

# Panel B: Unweighted DOS
ax2 = fig.add_subplot(3, 2, 2)
ax2.bar(bin_centers, rho_unweighted, width=bin_width*0.9, alpha=0.6,
        color='coral', label=f'Unweighted (N={n_stored})')
ax2.set_xlabel('$\\omega$ ($M_{KK}$)')
ax2.set_ylabel('$\\rho(\\omega)$ (modes / $M_{KK}$)')
ax2.set_title('Density of States (unweighted, 992 eigenvalues)')
ax2.legend(fontsize=8)
ax2.axvline(omega_gap, color='green', ls=':', lw=1, alpha=0.7)
ax2.set_xlim(omega_min, omega_max)

# Panel C: Cumulative distribution
ax3 = fig.add_subplot(3, 2, 3)
ax3.plot(bin_centers, N_frac_weighted, 'b-', lw=2, label='Weighted')
ax3.plot(bin_centers, N_frac_unweighted, 'r--', lw=1.5, label='Unweighted')
ax3.axhline(0.5, color='gray', ls=':', lw=1, alpha=0.5)
ax3.set_xlabel('$\\omega$ ($M_{KK}$)')
ax3.set_ylabel('$N(\\omega) / N_{total}$')
ax3.set_title('Cumulative Distribution')
ax3.legend(fontsize=8)
ax3.set_xlim(omega_min, omega_max)
ax3.set_ylim(0, 1.05)

# Panel D: Per-sector decomposition (stacked, weighted)
ax4 = fig.add_subplot(3, 2, 4)
colors_groups = {
    '(0,0)': '#1f77b4',
    '(1,0)+(0,1)': '#ff7f0e',
    '(1,1)': '#2ca02c',
    '(2,0)+(0,2)': '#d62728',
    '(3,0)+(0,3)': '#9467bd',
    '(2,1)': '#8c564b',
}
bottom = np.zeros(n_bins)
for gname in sector_groups:
    h = group_histograms_w[gname] / bin_width  # convert to density
    ax4.bar(bin_centers, h, width=bin_width*0.9, bottom=bottom,
            alpha=0.7, color=colors_groups[gname], label=gname)
    bottom += h
ax4.set_xlabel('$\\omega$ ($M_{KK}$)')
ax4.set_ylabel('$\\rho(\\omega)$ (modes / $M_{KK}$)')
ax4.set_title('Per-Sector Decomposition (stacked, weighted)')
ax4.legend(fontsize=7, loc='upper right')
ax4.set_xlim(omega_min, omega_max)

# Panel E: Per-sector DOS individually (log scale for comparison)
ax5 = fig.add_subplot(3, 2, 5)
for gname in sector_groups:
    h = group_histograms_w[gname] / bin_width
    nonzero = h > 0
    if np.any(nonzero):
        ax5.semilogy(bin_centers[nonzero], h[nonzero], 'o-', markersize=3,
                     color=colors_groups[gname], label=gname, lw=1)
ax5.set_xlabel('$\\omega$ ($M_{KK}$)')
ax5.set_ylabel('$\\rho(\\omega)$ (modes / $M_{KK}$)')
ax5.set_title('Per-Sector DOS (log scale, weighted)')
ax5.legend(fontsize=7, loc='upper left')
ax5.set_xlim(omega_min, omega_max)

# Panel F: Branch-level comparison (B1, B2, B3)
ax6 = fig.add_subplot(3, 2, 6)
branch_colors = {'B1': '#1f77b4', 'B2': '#2ca02c', 'B3': '#d62728'}
branch_labels_plot = {'B1': 'B1 (acoustic)', 'B2': 'B2 (flat-optical)',
                      'B3': 'B3 (dispersive-optical)'}

# Aggregate histograms by branch
for b_label in ['B1', 'B2', 'B3']:
    h_branch = np.zeros(n_bins)
    for gname, stats in group_stats.items():
        if stats['branch'] == b_label:
            h_branch += group_histograms_w[gname] / bin_width
    nonzero = h_branch > 0
    if np.any(nonzero):
        ax6.bar(bin_centers[nonzero], h_branch[nonzero], width=bin_width*0.85,
                alpha=0.5, color=branch_colors[b_label],
                label=branch_labels_plot[b_label])
ax6.set_xlabel('$\\omega$ ($M_{KK}$)')
ax6.set_ylabel('$\\rho(\\omega)$ (modes / $M_{KK}$)')
ax6.set_title('Branch-Level DOS (B1, B2, B3)')
ax6.legend(fontsize=8)
ax6.set_xlim(omega_min, omega_max)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "s43_phonon_dos.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved: {plot_path}")
plt.close()

# ================================================================
# 11. FINAL SUMMARY
# ================================================================

print(f"\n{'='*70}")
print(f"DOS-43 FINAL SUMMARY")
print(f"{'='*70}")
print(f"")
print(f"  SPECTRAL GAP: {omega_gap:.4f} M_KK (hard gap, ALL modes massive)")
print(f"  TOTAL BANDWIDTH: {total_bandwidth:.4f} M_KK")
print(f"  FREQUENCY RANGE: [{omega_gap:.4f}, {omega_max_val:.4f}] M_KK")
print(f"  STORED EIGENVALUES: {n_stored}")
print(f"  PHYSICAL MODES (dim^2-weighted): {n_physical}")
print(f"  WEIGHTED MEAN: {mean_omega:.4f} +/- {std_omega:.4f} M_KK")
print(f"  LOGARITHMIC MEAN: {omega_log:.4f} M_KK")
print(f"")
print(f"  VAN HOVE SINGULARITIES: {n_vh}")
for vh in sorted(vh_singularities, key=lambda x: x['omega']):
    if vh['rho'] > 0:
        print(f"    omega={vh['omega']:.3f}: {vh['type']}, rho={vh['rho']:.0f}, sectors={vh['sectors']}")
print(f"")
print(f"  FLAT-BAND FRACTION: {n_flat}/{n_groups} = {flat_frac:.2f}")
for gname, stats in group_stats.items():
    if stats['flat_band']:
        print(f"    {gname}: BW={stats['bandwidth']:.4f} M_KK (< 0.05 threshold)")
print(f"")
print(f"  PER-SECTOR TABLE:")
print(f"    {'Group':>18s} {'Branch':>6s} {'N_ev':>5s} {'N_phys':>8s} {'BW':>7s} {'omega_min':>9s} {'omega_max':>9s}")
for gname, stats in group_stats.items():
    print(f"    {gname:>18s} {stats['branch']:>6s} {stats['n_ev']:>5d} "
          f"{stats['n_phys']:>8d} {stats['bandwidth']:>7.4f} "
          f"{stats['omega_min']:>9.4f} {stats['omega_max']:>9.4f}")
print(f"")
print(f"  PHONONIC INTERPRETATION:")
print(f"    Theta_D analogue = {omega_max_val:.4f} M_KK (Debye cutoff)")
print(f"    Theta_E analogue = {omega_1:.4f} M_KK (Einstein frequency)")
print(f"    All modes optical (no acoustic branch at fold -- NG mode absent)")
print(f"    Crystal is GAPPED: purely optical phonon spectrum")
print(f"")
print(f"  Gate: DOS-43 (INFO -- diagnostic, no PASS/FAIL)")
print(f"  Data: tier0-computation/s43_phonon_dos.npz")
print(f"  Plot: tier0-computation/s43_phonon_dos.png")
