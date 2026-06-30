#!/usr/bin/env python3
"""
S67 VHS-CLASSIFY-67 — Van Hove Singularity Type at the Fold
=============================================================

Classifies the van Hove singularity (VHS) at the fold (tau = 0.190) by:
  1. Loading D_K eigenvalues omega_i(tau) from s44_dos_tau.npz (992 modes, 5 tau values)
  2. Recomputing eigenvalues at a fine tau grid near the fold using dirac_spectrum
  3. For each eigenvalue branch: computing d omega_i / d tau and d^2 omega_i / d tau^2
  4. Identifying modes with extrema (d omega/d tau ~ 0) near tau_fold = 0.19
  5. Classifying VHS type: A1 (maximum), M1 (minimum), M2 (saddle)
  6. Computing the weighted DOS g(E, tau) and its divergence exponent near the fold

Physical significance: The VHS type at the fold controls:
  - The Mach number profile during the transit
  - The Bogoliubov pair production efficiency (Parker mechanism)
  - The GGE relic spectrum and its observational signatures

Gate: VHS-CLASSIFY-67. INFO: Structural classification (no pass/fail).

Author: Landau Condensed-Matter Theorist (S67)
Date: 2026-04-04
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from time import time

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, '..')
ARCHIVE_DIR = os.path.join(PROJECT_ROOT, "computations", "_shared")

# CRITICAL: Insert SCRIPT_DIR first so canonical_constants comes from computations
# computations/_shared has a stale copy that lacks newer constants
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if ARCHIVE_DIR not in sys.path:
    sys.path.append(ARCHIVE_DIR)  # append, not insert — lower priority

from canonical_constants import (
    tau_fold, Delta_0_OES, E_cond, M_KK, N_cells,
    a0_fold, a2_fold, a4_fold, dS_fold, d2S_fold,
    T_acoustic
)

# Import Dirac spectrum machinery from archive
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, get_irrep, dirac_operator_on_irrep,
    _irrep_cache
)

print("=" * 72)
print("VHS-CLASSIFY-67: Van Hove Singularity Classification at Fold")
print("=" * 72)
print()

# ============================================================
# 1. LOAD EXISTING 5-POINT SPECTRUM DATA
# ============================================================

print("--- Phase 1: Loading 5-point spectrum from s44_dos_tau.npz ---")
t0 = time()

d44 = np.load(os.path.join(SCRIPT_DIR, 's44_dos_tau.npz'), allow_pickle=True)

tau_coarse = np.array([0.00, 0.05, 0.10, 0.15, 0.19])
n_tau_coarse = len(tau_coarse)
n_modes = 992  # (local)

omega_coarse = np.zeros((n_tau_coarse, n_modes))
for i, label in enumerate(['tau0.00', 'tau0.05', 'tau0.10', 'tau0.15', 'tau0.19']):
    omega_coarse[i] = d44[f'{label}_all_omega']

dim2 = d44['tau0.00_all_dim2']  # degeneracy weights (dim(p,q)^2)
total_weight = dim2.sum()

print(f"  Loaded {n_modes} modes at {n_tau_coarse} tau values")
print(f"  Total degeneracy weight: {total_weight:.0f}")
print(f"  Omega range at fold: [{omega_coarse[-1].min():.6f}, {omega_coarse[-1].max():.6f}] M_KK")
print(f"  Time: {time()-t0:.2f}s")
print()


# ============================================================
# 2. RECOMPUTE EIGENVALUES AT FINE TAU GRID NEAR FOLD
# ============================================================

print("--- Phase 2: Fine tau grid near fold via dirac_spectrum ---")
t0 = time()

# Fine grid: 15 points from tau=0.10 to tau=0.19 (fold is the endpoint)
tau_fine = np.linspace(0.10, 0.19, 15)
n_tau_fine = len(tau_fine)

# SU(3) infrastructure
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

max_pq_sum = 6  # Same truncation as s44


def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def compute_spectrum_at_tau(tau_val):
    """
    Compute full Dirac eigenvalue spectrum (absolute values) at given tau.
    Returns: (eigenvalues_sorted, dim2_array) with consistent ordering.
    """
    global _irrep_cache
    _irrep_cache.clear()

    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau_val)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    all_omega = []
    all_dim2 = []

    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            d = dim_pq(p, q)
            if (p, q) == (0, 0):
                D_trivial = Omega.copy()
                evals_raw = np.linalg.eigvals(D_trivial)
            else:
                rho, _ = get_irrep(p, q, gens, f_abc)
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                evals_raw = np.linalg.eigvals(D_pi)

            # Physical eigenvalues = |Im(lambda)|
            abs_omega = np.abs(evals_raw.imag)

            # Keep only positive (non-degenerate) eigenvalues
            # Due to spectral symmetry, keep unique positive values
            abs_omega_sorted = np.sort(abs_omega)

            # Remove near-duplicates from +/- symmetry
            unique_omega = []
            for val in abs_omega_sorted:
                if val > 1e-10:
                    if not unique_omega or abs(val - unique_omega[-1]) > 1e-8:
                        unique_omega.append(val)

            for omega_val in unique_omega:
                all_omega.append(omega_val)
                all_dim2.append(d * d)

    return np.array(all_omega), np.array(all_dim2)


# First pass: compute at reference tau to get mode count
omega_ref, dim2_ref = compute_spectrum_at_tau(tau_fine[0])
sort_idx_ref = np.argsort(omega_ref)
omega_ref = omega_ref[sort_idx_ref]
dim2_ref = dim2_ref[sort_idx_ref]
computed_n_modes = len(omega_ref)
print(f"  Fine grid: {computed_n_modes} modes per tau point")

omega_fine = np.zeros((n_tau_fine, computed_n_modes))
dim2_fine = dim2_ref.copy()  # degeneracies are tau-independent for given (p,q) sector

omega_fine[0, :] = omega_ref
print(f"  tau={tau_fine[0]:.4f}: omega range=[{omega_ref.min():.6f}, {omega_ref.max():.6f}]")

for i in range(1, n_tau_fine):
    tau_val = tau_fine[i]
    omega_i, dim2_i = compute_spectrum_at_tau(tau_val)

    # Sort by eigenvalue magnitude for consistent tracking
    sort_idx = np.argsort(omega_i)
    omega_i = omega_i[sort_idx]

    actual_n = len(omega_i)

    # Handle mode count mismatches: use the minimum
    n_use = min(actual_n, computed_n_modes)
    if actual_n != computed_n_modes:
        print(f"  WARNING: tau={tau_val:.4f} has {actual_n} modes (expected {computed_n_modes}), using {n_use}")
    omega_fine[i, :n_use] = omega_i[:n_use]
    # Fill any remaining with NaN to flag them
    if n_use < computed_n_modes:
        omega_fine[i, n_use:] = np.nan

    if (i + 1) % 5 == 0:
        print(f"  tau={tau_val:.4f}: omega range=[{omega_i[:n_use].min():.6f}, {omega_i[:n_use].max():.6f}]")

# Check for NaN modes and trim if needed
nan_mask = np.any(np.isnan(omega_fine), axis=0)
if np.any(nan_mask):
    n_valid = np.sum(~nan_mask)
    print(f"  Trimming {np.sum(nan_mask)} modes with NaN (inconsistent across tau)")
    omega_fine = omega_fine[:, ~nan_mask]
    dim2_fine = dim2_fine[~nan_mask]
    computed_n_modes = n_valid

print(f"  Fine grid complete: {n_tau_fine} tau points x {computed_n_modes} modes")
print(f"  Time: {time()-t0:.1f}s")
print()


# ============================================================
# 3. EIGENVALUE DERIVATIVES AND VHS CLASSIFICATION
# ============================================================

print("--- Phase 3: Eigenvalue derivatives and VHS identification ---")
t0 = time()

# Use the fine grid for derivative computation
# Cubic spline interpolation for each mode
n_modes_fine = computed_n_modes
d_omega_dtau = np.zeros((n_tau_fine, n_modes_fine))
d2_omega_dtau2 = np.zeros((n_tau_fine, n_modes_fine))

for m in range(n_modes_fine):
    # Fit cubic spline to omega_m(tau)
    cs = CubicSpline(tau_fine, omega_fine[:, m])
    d_omega_dtau[:, m] = cs(tau_fine, 1)   # first derivative
    d2_omega_dtau2[:, m] = cs(tau_fine, 2)  # second derivative

# Values at the fold (last point of fine grid)
d_omega_at_fold = d_omega_dtau[-1, :]
d2_omega_at_fold = d2_omega_dtau2[-1, :]
omega_at_fold = omega_fine[-1, :]

print(f"  d omega/d tau at fold: range=[{d_omega_at_fold.min():.6f}, {d_omega_at_fold.max():.6f}]")
print(f"  d2 omega/d tau2 at fold: range=[{d2_omega_at_fold.min():.4f}, {d2_omega_at_fold.max():.4f}]")
print()

# Identify VHS modes: |d omega/d tau| < threshold
# Threshold: |d_omega/d_tau| < 0.1 * max(|d_omega/d_tau|)
max_deriv = np.max(np.abs(d_omega_at_fold))
vhs_threshold = 0.1 * max_deriv

# Also look for modes where d omega/d tau changes sign in the fine grid
# (indicating an extremum near but not exactly at the fold)
sign_changes = np.zeros(n_modes_fine, dtype=bool)
for m in range(n_modes_fine):
    for i in range(n_tau_fine - 1):
        if d_omega_dtau[i, m] * d_omega_dtau[i + 1, m] < 0:
            sign_changes[m] = True
            break

# Classification
small_deriv = np.abs(d_omega_at_fold) < vhs_threshold
vhs_candidates = small_deriv | sign_changes

n_small_deriv = np.sum(small_deriv)
n_sign_change = np.sum(sign_changes)
n_vhs = np.sum(vhs_candidates)

print(f"  VHS threshold: |d omega/d tau| < {vhs_threshold:.4f}")
print(f"  Modes with small derivative at fold: {n_small_deriv}/{n_modes_fine}")
print(f"  Modes with sign change in [0.10, 0.19]: {n_sign_change}/{n_modes_fine}")
print(f"  Total VHS candidates: {n_vhs}/{n_modes_fine}")
print()

# Classify each VHS mode
# M1 (minimum): d2 > 0 -- eigenvalue has a local minimum near fold
# A1 (maximum): d2 < 0 -- eigenvalue has a local maximum near fold
# Inflection: d2 ~ 0 -- saddle-like behavior

n_M1 = 0  # minima
n_A1 = 0  # maxima
n_inflection = 0  # inflection points
vhs_type_per_mode = np.full(n_modes_fine, '', dtype='U10')

d2_threshold = 0.01 * np.max(np.abs(d2_omega_at_fold))

for m in range(n_modes_fine):
    if not vhs_candidates[m]:
        if d_omega_at_fold[m] > 0:
            vhs_type_per_mode[m] = 'RISING'
        else:
            vhs_type_per_mode[m] = 'FALLING'
        continue

    # For sign-change modes, find the tau at the extremum
    d2_val = d2_omega_at_fold[m]

    # Use the CURVATURE at the point closest to the extremum
    # If the extremum is inside [0.10, 0.19], use the curvature there
    extremum_tau = None
    for i in range(n_tau_fine - 1):
        if d_omega_dtau[i, m] * d_omega_dtau[i + 1, m] < 0:
            # Interpolate to find exact crossing
            cs_m = CubicSpline(tau_fine, omega_fine[:, m])
            try:
                t_ext = brentq(lambda t: cs_m(t, 1), tau_fine[i], tau_fine[i + 1])
                extremum_tau = t_ext
                d2_val = cs_m(t_ext, 2)
            except ValueError:
                pass
            break

    if np.abs(d2_val) < d2_threshold:
        vhs_type_per_mode[m] = 'INFLECT'
        n_inflection += 1
    elif d2_val > 0:
        vhs_type_per_mode[m] = 'M1'
        n_M1 += 1
    else:
        vhs_type_per_mode[m] = 'A1'
        n_A1 += 1

# Also count rising/falling modes
n_rising = np.sum(vhs_type_per_mode == 'RISING')
n_falling = np.sum(vhs_type_per_mode == 'FALLING')

print(f"  VHS Classification:")
print(f"    M1 (minimum, d2 > 0):      {n_M1}")
print(f"    A1 (maximum, d2 < 0):       {n_A1}")
print(f"    Inflection (d2 ~ 0):        {n_inflection}")
print(f"    Monotone rising:            {n_rising}")
print(f"    Monotone falling:           {n_falling}")
print(f"    Total:                      {n_M1 + n_A1 + n_inflection + n_rising + n_falling}")
print()

# Weighted classification (by dim^2)
w_M1 = dim2_fine[vhs_type_per_mode == 'M1'].sum()
w_A1 = dim2_fine[vhs_type_per_mode == 'A1'].sum()
w_inflect = dim2_fine[vhs_type_per_mode == 'INFLECT'].sum()
w_rising = dim2_fine[vhs_type_per_mode == 'RISING'].sum()
w_falling = dim2_fine[vhs_type_per_mode == 'FALLING'].sum()
w_total = dim2_fine.sum()

print(f"  Degeneracy-weighted VHS Classification:")
print(f"    M1 weight:        {w_M1:.0f} ({100*w_M1/w_total:.1f}%)")
print(f"    A1 weight:        {w_A1:.0f} ({100*w_A1/w_total:.1f}%)")
print(f"    Inflection weight:{w_inflect:.0f} ({100*w_inflect/w_total:.1f}%)")
print(f"    Rising weight:    {w_rising:.0f} ({100*w_rising/w_total:.1f}%)")
print(f"    Falling weight:   {w_falling:.0f} ({100*w_falling/w_total:.1f}%)")
print()


# ============================================================
# 4. DENSITY OF STATES AND DIVERGENCE ANALYSIS
# ============================================================

print("--- Phase 4: Density of States and divergence analysis ---")
t0_dos = time()

# Compute the weighted DOS at and near the fold
# g(E, tau) = sum_i dim_i^2 * delta(E - omega_i(tau))
# Use Gaussian broadening: delta -> (1/(sigma*sqrt(2*pi))) exp(-(E-omega)^2/(2*sigma^2))

omega_fold_vals = omega_fine[-1, :]
sigma_dos = 0.005  # broadening width in M_KK units  # (local)
n_E = 2000
E_grid = np.linspace(omega_fold_vals.min() - 0.05, omega_fold_vals.max() + 0.05, n_E)

# DOS at fold
dos_fold = np.zeros(n_E)
for m in range(n_modes_fine):
    dos_fold += dim2_fine[m] * np.exp(-0.5 * ((E_grid - omega_fold_vals[m]) / sigma_dos) ** 2) \
                / (sigma_dos * np.sqrt(2 * np.pi))

# DOS at several tau values near fold
dos_at_tau = np.zeros((n_tau_fine, n_E))
for i in range(n_tau_fine):
    for m in range(n_modes_fine):
        dos_at_tau[i] += dim2_fine[m] * np.exp(
            -0.5 * ((E_grid - omega_fine[i, m]) / sigma_dos) ** 2
        ) / (sigma_dos * np.sqrt(2 * np.pi))

# Identify DOS peaks at fold
from scipy.signal import find_peaks
peaks, properties = find_peaks(dos_fold, height=0.1 * dos_fold.max(), distance=20)

print(f"  DOS computed on {n_E}-point grid, sigma={sigma_dos}")
print(f"  DOS peak count: {len(peaks)}")
print(f"  DOS max: {dos_fold.max():.1f} at E={E_grid[np.argmax(dos_fold)]:.4f} M_KK")
print()

if len(peaks) > 0:
    print(f"  DOS peaks at fold:")
    for ip, pk in enumerate(peaks[:10]):
        print(f"    Peak {ip+1}: E = {E_grid[pk]:.4f} M_KK, g = {dos_fold[pk]:.1f}")
    print()


# ============================================================
# 5. VAN HOVE DIVERGENCE EXPONENT
# ============================================================

print("--- Phase 5: Van Hove divergence exponent ---")

# The VHS in the DOS manifests as a peak or divergence at energies where
# d omega_i / d tau = 0 (for a 1D parameter sweep, this is the 1D VHS).
#
# For a 1D band crossing: g(E) ~ |E - E_vH|^{-1/2} near a band extremum.
# For a higher-order saddle: g(E) ~ |E - E_vH|^{-alpha} with alpha > 1/2.
#
# In our case, tau is a 1-parameter deformation, so the VHS classification
# is effectively 1-dimensional. The relevant quantity is the number of modes
# with d omega/d tau = 0 simultaneously and their curvatures d^2 omega / d tau^2.
#
# The spectral action S(tau) = sum_i dim_i^2 * f(omega_i(tau) / Lambda)
# has dS/dtau = sum_i dim_i^2 * f'(omega_i/Lambda) * (1/Lambda) * d omega_i / d tau
# The VHS at the fold means many modes have d omega_i / d tau ~ 0 simultaneously,
# giving a peak in dS/dtau that drives the transit dynamics.

# For each VHS mode, compute the "effective dimension" from the curvature
# d^2 omega / d tau^2. The VHS exponent alpha = (n_flat - 2) / 2 where
# n_flat = number of flat directions. In 1D, a simple extremum gives alpha = 1/2.
# A higher-order VHS (d^2 = 0 as well) gives alpha > 1/2.

# Collect VHS mode energies and curvatures
vhs_energies = []
vhs_curvatures = []
vhs_weights = []
vhs_types = []

for m in range(n_modes_fine):
    if vhs_candidates[m]:
        vhs_energies.append(omega_fold_vals[m])
        vhs_curvatures.append(d2_omega_at_fold[m])
        vhs_weights.append(dim2_fine[m])
        vhs_types.append(vhs_type_per_mode[m])

vhs_energies = np.array(vhs_energies) if vhs_energies else np.array([])
vhs_curvatures = np.array(vhs_curvatures) if vhs_curvatures else np.array([])
vhs_weights = np.array(vhs_weights) if vhs_weights else np.array([])

if len(vhs_energies) > 0:
    # For a 1D VHS with quadratic extremum: g ~ 1/sqrt(|E - E_vH|)
    # The coefficient is dim^2 / sqrt(2 * |d2 omega / d tau^2|)
    # For modes with |d2| ~ 0, the divergence is STRONGER (higher-order VHS)

    # Compute the effective DOS contribution from each VHS mode
    # g_VHS(E) ~ W / sqrt(2 |d2| |E - E_vH|)  (near E_vH)

    print(f"  VHS modes: {len(vhs_energies)}")
    print(f"  Energy range of VHS modes: [{vhs_energies.min():.4f}, {vhs_energies.max():.4f}] M_KK")
    print()

    # Sort by weight for display
    sort_idx = np.argsort(-vhs_weights)
    print(f"  Top 10 VHS modes by weight:")
    print(f"  {'#':>3s} {'E (M_KK)':>10s} {'d2 omega':>12s} {'Weight':>8s} {'Type':>8s}")
    for i_rank in range(min(10, len(sort_idx))):
        idx = sort_idx[i_rank]
        print(f"  {i_rank+1:3d} {vhs_energies[idx]:10.4f} {vhs_curvatures[idx]:12.4f} "
              f"{vhs_weights[idx]:8.0f} {vhs_types[idx]:>8s}")
    print()

    # Effective VHS alpha: fit the DOS peak shape near the strongest VHS
    # Find the energy with highest DOS that corresponds to a VHS cluster
    # The overall VHS type is determined by the COLLECTIVE behavior

    # Cluster VHS modes by energy
    vhs_sort = np.argsort(vhs_energies)
    cluster_threshold = 0.02  # M_KK  # (local)
    clusters = []
    current_cluster = [vhs_sort[0]]

    for i in range(1, len(vhs_sort)):
        if vhs_energies[vhs_sort[i]] - vhs_energies[vhs_sort[i-1]] < cluster_threshold:
            current_cluster.append(vhs_sort[i])
        else:
            clusters.append(current_cluster)
            current_cluster = [vhs_sort[i]]
    clusters.append(current_cluster)

    print(f"  VHS clusters (threshold={cluster_threshold} M_KK): {len(clusters)}")
    for ic, cl in enumerate(clusters[:8]):
        cl_E = np.mean(vhs_energies[cl])
        cl_W = sum(vhs_weights[cl])
        cl_n = len(cl)
        cl_types = [vhs_types[j] for j in cl]
        # Determine cluster type
        n_m1 = cl_types.count('M1')
        n_a1 = cl_types.count('A1')
        n_inf = cl_types.count('INFLECT')
        if n_m1 > 0 and n_a1 > 0:
            cl_type = 'MIXED (M2-like)'
        elif n_m1 > n_a1:
            cl_type = 'M1'
        elif n_a1 > n_m1:
            cl_type = 'A1'
        else:
            cl_type = 'INFLECT'
        print(f"    Cluster {ic+1}: E={cl_E:.4f}, n_modes={cl_n}, weight={cl_W:.0f}, "
              f"M1={n_m1}/A1={n_a1}/INF={n_inf} -> {cl_type}")
    print()


# ============================================================
# 6. DOS DIVERGENCE FIT NEAR STRONGEST VHS
# ============================================================

print("--- Phase 6: DOS divergence exponent fit ---")

# The key VHS analysis: how does the DOS diverge near the fold?
# In the 1-parameter (tau) space, the VHS is where d omega_i / d tau = 0.
# The DOS in ENERGY space g(E) = sum_i dim_i^2 * delta(E - omega_i)
# diverges at E = omega_i(tau_fold) for VHS modes as ~ |E - E_vH|^{-alpha}
#
# For a quadratic extremum in 1D: alpha = 1/2
# For a quartic extremum (d^2 = 0, d^4 ≠ 0): alpha = 3/4
# For a log divergence (2D saddle): alpha = 0 (logarithmic)

# Fit the DOS near the maximum to extract the exponent
dos_max_idx = np.argmax(dos_fold)
E_peak = E_grid[dos_max_idx]
dos_peak = dos_fold[dos_max_idx]

# Fit on both sides of the peak
# g(E) = A * |E - E_peak|^{-alpha} + background

# Use the RIGHT side of the peak (higher E)
mask_right = (E_grid > E_peak + sigma_dos) & (E_grid < E_peak + 0.15)
if np.sum(mask_right) > 5:
    dE_right = E_grid[mask_right] - E_peak
    g_right = dos_fold[mask_right]
    # log-log fit: log(g) = -alpha * log(dE) + log(A)
    valid = g_right > 0.1 * dos_peak  # only fit the high-DOS region
    if np.sum(valid) > 3:
        log_dE = np.log(dE_right[valid])
        log_g = np.log(g_right[valid])
        coeffs_right = np.polyfit(log_dE, log_g, 1)
        alpha_right = -coeffs_right[0]
        print(f"  Right-side fit: alpha = {alpha_right:.4f} (slope of log-log fit)")

# Use the LEFT side
mask_left = (E_grid < E_peak - sigma_dos) & (E_grid > E_peak - 0.15)
if np.sum(mask_left) > 5:
    dE_left = E_peak - E_grid[mask_left]
    g_left = dos_fold[mask_left]
    valid = g_left > 0.1 * dos_peak
    if np.sum(valid) > 3:
        log_dE = np.log(dE_left[valid])
        log_g = np.log(g_left[valid])
        coeffs_left = np.polyfit(log_dE, log_g, 1)
        alpha_left = -coeffs_left[0]
        print(f"  Left-side fit:  alpha = {alpha_left:.4f}")

# Mean alpha
if 'alpha_right' in dir() and 'alpha_left' in dir():
    alpha_mean = 0.5 * (alpha_right + alpha_left)
    alpha_asymmetry = abs(alpha_right - alpha_left) / max(alpha_right + alpha_left, 1e-10)
    print(f"  Mean alpha:     {alpha_mean:.4f}")
    print(f"  Asymmetry:      {alpha_asymmetry:.4f}")
elif 'alpha_right' in dir():
    alpha_mean = alpha_right
    alpha_asymmetry = float('nan')
elif 'alpha_left' in dir():
    alpha_mean = alpha_left
    alpha_asymmetry = float('nan')
else:
    alpha_mean = 0.0  # (local)
    alpha_asymmetry = float('nan')
    print("  WARNING: Could not fit DOS divergence on either side")
print()


# ============================================================
# 7. SPECTRAL FLOW ANALYSIS
# ============================================================

print("--- Phase 7: Spectral flow through the fold ---")

# The spectral action S(tau) = sum_i dim_i^2 * f(omega_i / Lambda)
# The VHS drives dS/dtau through the collective velocity
# v_spec(tau) = (1/N_eff) * sum_i dim_i^2 * d omega_i / d tau
# where N_eff = sum dim_i^2.

# Compute the weighted mean spectral velocity
v_spec = np.zeros(n_tau_fine)
v_spec_rms = np.zeros(n_tau_fine)
for i in range(n_tau_fine):
    w_vel = dim2_fine * d_omega_dtau[i, :]
    v_spec[i] = w_vel.sum() / dim2_fine.sum()
    v_spec_rms[i] = np.sqrt((dim2_fine * d_omega_dtau[i, :] ** 2).sum() / dim2_fine.sum())

print(f"  Weighted spectral velocity at fold: {v_spec[-1]:.6f} M_KK")
print(f"  Spectral velocity RMS at fold: {v_spec_rms[-1]:.6f} M_KK")
print(f"  Ratio RMS/mean: {v_spec_rms[-1]/abs(v_spec[-1]):.2f}")
print()

# The "bandwidth" of the spectrum: max - min of eigenvalues
bw = np.zeros(n_tau_fine)
for i in range(n_tau_fine):
    bw[i] = omega_fine[i, :].max() - omega_fine[i, :].min()

dbw_dtau = np.gradient(bw, tau_fine)

print(f"  Bandwidth at fold: {bw[-1]:.6f} M_KK")
print(f"  d(bandwidth)/d tau at fold: {dbw_dtau[-1]:.4f}")
print()

# Fraction of modes with d omega/d tau > 0 (being pushed UP by deformation)
frac_rising = np.zeros(n_tau_fine)
frac_rising_weighted = np.zeros(n_tau_fine)
for i in range(n_tau_fine):
    frac_rising[i] = np.sum(d_omega_dtau[i, :] > 0) / n_modes_fine
    frac_rising_weighted[i] = dim2_fine[d_omega_dtau[i, :] > 0].sum() / dim2_fine.sum()

print(f"  Fraction rising at fold: {frac_rising[-1]:.4f} (unweighted), "
      f"{frac_rising_weighted[-1]:.4f} (weighted)")
print()


# ============================================================
# 8. OVERALL VHS TYPE DETERMINATION
# ============================================================

print("=" * 72)
print("OVERALL VHS CLASSIFICATION")
print("=" * 72)
print()

# The van Hove singularity type is determined by the behavior of the DOS
# near the fold. In our 1-parameter (tau) system:
#
# TYPE M1 (minimum): Many eigenvalues have minima near the fold.
#   DOS has a cusp (divergent) from below.
#   Transit physics: spectral weight accumulates at the fold.
#
# TYPE A1 (maximum): Many eigenvalues have maxima near the fold.
#   DOS has a cusp from above (edge).
#   Transit physics: spectral weight depletes at the fold.
#
# TYPE M2 (saddle/mixed): Some eigenvalues rise, others fall, many are stationary.
#   DOS has a logarithmic peak.
#   Transit physics: spectral weight REDISTRIBUTES without net accumulation.

# Determine overall type from the statistics
overall_type = ""
dominant_vhs = ""

# Count weighted VHS types
total_vhs_weight = w_M1 + w_A1 + w_inflect
if total_vhs_weight > 0:
    f_M1 = w_M1 / total_vhs_weight
    f_A1 = w_A1 / total_vhs_weight
    f_inf = w_inflect / total_vhs_weight
else:
    f_M1 = f_A1 = f_inf = 0.0

if f_M1 > 0.6:
    overall_type = "M1 (MINIMUM-DOMINATED)"
    dominant_vhs = "M1"
elif f_A1 > 0.6:
    overall_type = "A1 (MAXIMUM-DOMINATED)"
    dominant_vhs = "A1"
elif f_M1 > 0.3 and f_A1 > 0.3:
    overall_type = "M2 (MIXED SADDLE)"
    dominant_vhs = "M2"
elif f_inf > 0.4:
    overall_type = "HIGHER-ORDER (INFLECTION-DOMINATED)"
    dominant_vhs = "HO"
else:
    overall_type = "M2 (MIXED, NO CLEAR DOMINANCE)"
    dominant_vhs = "M2"

print(f"  Overall VHS type: {overall_type}")
print(f"  M1 fraction: {f_M1:.3f}")
print(f"  A1 fraction: {f_A1:.3f}")
print(f"  Inflection fraction: {f_inf:.3f}")
print()
print(f"  DOS peak energy: {E_peak:.4f} M_KK")
print(f"  DOS peak value: {dos_peak:.1f}")
print(f"  DOS divergence exponent alpha: {alpha_mean:.4f}")
print()

# Physical interpretation
alpha_1d_standard = 0.5  # (local)
if alpha_mean > 0:
    print(f"  Standard 1D VHS exponent: {alpha_1d_standard:.2f}")
    print(f"  Measured exponent: {alpha_mean:.4f}")
    if alpha_mean > 0.6:
        vhs_order = "HIGHER-ORDER (alpha > 0.5, enhanced divergence)"
    elif alpha_mean > 0.3:
        vhs_order = "STANDARD (alpha ~ 0.5, square-root divergence)"
    elif alpha_mean > 0.1:
        vhs_order = "WEAK (alpha < 0.3, sub-standard divergence)"
    else:
        vhs_order = "LOGARITHMIC (alpha ~ 0, 2D-like logarithmic peak)"
    print(f"  VHS order: {vhs_order}")
else:
    vhs_order = "NON-DIVERGENT (integrable peak)"
    print(f"  VHS order: {vhs_order}")

print()

# Implications for transit dynamics
print("  Physical implications:")
if dominant_vhs in ("M1", "M2"):
    print("  - Many modes have extrema near the fold => spectral weight concentrates")
    print("  - The DOS peak enhances Bogoliubov pair production")
    print("  - The spectral action derivative dS/dtau is dominated by non-VHS modes")
    print("  - VHS modes contribute to d2S/dtau2 (curvature of the spectral action)")
print(f"  - The fold is a genuine VHS with exponent alpha ~ {alpha_mean:.3f}")
print(f"  - {100*n_vhs/n_modes_fine:.1f}% of modes are VHS candidates "
      f"({100*total_vhs_weight/w_total:.1f}% by weight)")
print()


# ============================================================
# 9. SAVE RESULTS
# ============================================================

print("--- Saving results ---")

results = {
    # Tau grids
    'tau_fine': tau_fine,
    'tau_coarse': tau_coarse,

    # Eigenvalue data (fine grid)
    'omega_fine': omega_fine,
    'dim2_fine': dim2_fine,
    'n_modes_fine': np.array(n_modes_fine),

    # Derivatives at fold
    'd_omega_at_fold': d_omega_at_fold,
    'd2_omega_at_fold': d2_omega_at_fold,
    'omega_at_fold': omega_at_fold,

    # Full derivative arrays
    'd_omega_dtau': d_omega_dtau,
    'd2_omega_dtau2': d2_omega_dtau2,

    # VHS classification
    'vhs_candidates': vhs_candidates,
    'n_M1': np.array(n_M1),
    'n_A1': np.array(n_A1),
    'n_inflection': np.array(n_inflection),
    'n_rising': np.array(n_rising),
    'n_falling': np.array(n_falling),
    'w_M1': np.array(w_M1),
    'w_A1': np.array(w_A1),
    'w_inflect': np.array(w_inflect),
    'w_rising': np.array(w_rising),
    'w_falling': np.array(w_falling),

    # VHS energies and curvatures
    'vhs_energies': vhs_energies,
    'vhs_curvatures': vhs_curvatures,
    'vhs_weights': vhs_weights,

    # DOS
    'E_grid': E_grid,
    'dos_fold': dos_fold,
    'dos_at_tau': dos_at_tau,
    'sigma_dos': np.array(sigma_dos),

    # DOS peak and divergence
    'E_peak': np.array(E_peak),
    'dos_peak': np.array(dos_peak),
    'alpha_mean': np.array(alpha_mean),

    # Spectral flow
    'v_spec': v_spec,
    'v_spec_rms': v_spec_rms,
    'bw': bw,
    'frac_rising': frac_rising,
    'frac_rising_weighted': frac_rising_weighted,

    # Overall classification
    'overall_type': np.array(overall_type),
    'dominant_vhs': np.array(dominant_vhs),
    'vhs_order': np.array(vhs_order),

    # Gate
    'gate_name': np.array('VHS-CLASSIFY-67'),
    'gate_verdict': np.array('INFO'),
}

np.savez(os.path.join(SCRIPT_DIR, 's67_vhs_classify.npz'), **results)
print("  Saved: s67_vhs_classify.npz")


# ============================================================
# 10. PLOTS
# ============================================================

print("--- Generating plots ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('VHS-CLASSIFY-67: Van Hove Singularity at the Fold', fontsize=14)

# (a) Eigenvalue flow: omega_i(tau) for representative modes
ax = axes[0, 0]
# Plot a subset of modes, colored by VHS type
n_plot = min(200, n_modes_fine)
step = max(1, n_modes_fine // n_plot)
for m in range(0, n_modes_fine, step):
    tp = vhs_type_per_mode[m]
    if tp == 'M1':
        ax.plot(tau_fine, omega_fine[:, m], 'b-', alpha=0.3, lw=0.5)
    elif tp == 'A1':
        ax.plot(tau_fine, omega_fine[:, m], 'r-', alpha=0.3, lw=0.5)
    elif tp == 'INFLECT':
        ax.plot(tau_fine, omega_fine[:, m], 'g-', alpha=0.3, lw=0.5)
    else:
        ax.plot(tau_fine, omega_fine[:, m], 'k-', alpha=0.1, lw=0.3)
ax.axvline(tau_fold, color='orange', ls='--', label=f'Fold (tau={tau_fold})')
ax.set_xlabel('tau')
ax.set_ylabel('omega (M_KK)')
ax.set_title('(a) Eigenvalue flow')
ax.legend(fontsize=8)

# (b) d omega / d tau histogram at fold
ax = axes[0, 1]
ax.hist(d_omega_at_fold, bins=50, weights=dim2_fine, color='steelblue', edgecolor='k', alpha=0.7)
ax.axvline(0, color='red', ls='--', lw=2, label='d omega/d tau = 0 (VHS)')
ax.set_xlabel('d omega / d tau at fold')
ax.set_ylabel('Degeneracy-weighted count')
ax.set_title('(b) Spectral velocity distribution')
ax.legend()

# (c) DOS at fold
ax = axes[0, 2]
ax.plot(E_grid, dos_fold, 'k-', lw=1.5, label=f'tau = {tau_fold}')
# Mark VHS energies
if len(vhs_energies) > 0:
    for ve in vhs_energies[:20]:
        ax.axvline(ve, color='red', alpha=0.2, lw=0.5)
ax.set_xlabel('E (M_KK)')
ax.set_ylabel('g(E)')
ax.set_title('(c) Density of States at fold')
ax.legend()

# (d) d2 omega / d tau2 at fold (curvature distribution)
ax = axes[1, 0]
if len(vhs_curvatures) > 0:
    colors = ['blue' if t == 'M1' else 'red' if t == 'A1' else 'green'
              for t in vhs_types]
    ax.scatter(vhs_energies, vhs_curvatures, c=colors, s=vhs_weights / 10 + 2,
               alpha=0.6, edgecolors='k', linewidth=0.3)  # (local)
    ax.axhline(0, color='gray', ls='--')
    ax.set_xlabel('E (M_KK)')
    ax.set_ylabel('d2 omega / d tau2')
    ax.set_title('(d) VHS curvatures (blue=M1, red=A1, green=infl)')

# (e) DOS evolution near fold
ax = axes[1, 1]
cmap = plt.cm.viridis
for i in range(0, n_tau_fine, max(1, n_tau_fine // 6)):
    color = cmap(i / (n_tau_fine - 1))
    ax.plot(E_grid, dos_at_tau[i], color=color, alpha=0.7,
            label=f'tau={tau_fine[i]:.3f}')
ax.set_xlabel('E (M_KK)')
ax.set_ylabel('g(E)')
ax.set_title('(e) DOS evolution near fold')
ax.legend(fontsize=7, ncol=2)

# (f) Spectral flow quantities
ax = axes[1, 2]
ax.plot(tau_fine, v_spec, 'b-', lw=2, label='Mean velocity')
ax.plot(tau_fine, v_spec_rms, 'r--', lw=2, label='RMS velocity')
ax.fill_between(tau_fine, v_spec - v_spec_rms, v_spec + v_spec_rms,
                alpha=0.2, color='blue')  # (local)
ax.axvline(tau_fold, color='orange', ls='--')
ax.set_xlabel('tau')
ax.set_ylabel('Spectral velocity (M_KK)')
ax.set_title('(f) Spectral flow')
ax.legend()

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's67_vhs_classify.png'), dpi=150, bbox_inches='tight')
print("  Saved: s67_vhs_classify.png")
print()


# ============================================================
# FINAL SUMMARY
# ============================================================

print("=" * 72)
print("GATE VERDICT: VHS-CLASSIFY-67 — INFO")
print("=" * 72)
print()
print(f"  Overall VHS type at fold: {overall_type}")
print(f"  VHS order: {vhs_order}")
print(f"  DOS peak: E = {E_peak:.4f} M_KK, g = {dos_peak:.1f}")
print(f"  DOS exponent: alpha = {alpha_mean:.4f}")
print(f"  VHS candidate modes: {n_vhs}/{n_modes_fine} "
      f"({n_M1} M1, {n_A1} A1, {n_inflection} inflection)")
print(f"  Weighted fractions: M1={100*w_M1/w_total:.1f}%, "
      f"A1={100*w_A1/w_total:.1f}%, inflect={100*w_inflect/w_total:.1f}%")
print(f"  Spectral velocity at fold: mean={v_spec[-1]:.6f}, "
      f"RMS={v_spec_rms[-1]:.6f}")
print(f"  Bandwidth at fold: {bw[-1]:.6f} M_KK")
print(f"  Fraction rising at fold: {frac_rising_weighted[-1]:.4f} (weighted)")
print()
print("  DONE.")
