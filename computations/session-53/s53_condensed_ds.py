#!/usr/bin/env python3
"""
S53 CONDENSED-DS-53: Spectral Dimension from GL Tight-Binding Band Structure
=============================================================================

Physics:
  DS-QUANTUM-52 found d_s monotone through 8 from bare D_K^2 (Weyl asymptotics).
  The question: does the CONDENSED spectrum (GL 6-branch tight-binding bands on
  the 32-cell Voronoi tessellation) produce a different d_s flow?

  S53 reframe: N_pair=1, GL = tight-binding. The relevant spectrum is the pair
  band structure, not bare Dirac eigenvalues.

Method:
  1. Load GL 6-branch dispersion omega_i(K) from s52_gl_josephson.npz
  2. The BCC tessellation has 32 cells (graph vertices). This is a DISCRETE
     system — the spectral dimension comes from the graph Laplacian, not a
     continuum K-integral with K^2 measure.
  3. Sample the angle-averaged dispersion at 32 discrete K-points and construct
     the complete set of Laplacian eigenvalues: 6 branches x 33 K-points = 198 modes.
  4. Return probability: P(t) = (1/N) sum_n exp(-lambda_n * t)
     where lambda_n = omega_n^2 are the Laplacian eigenvalues.
  5. Spectral dimension: d_s(t) = -2 * d(log P) / d(log t)
  6. Compare: all 6 branches, Goldstone only, gapped only.
  7. Also compute with effective 3D K-multiplicity to show the effect.

  Key physical expectation:
    - UV: d_s -> d_eff (lattice dimension), but damped by the continuum of gapped modes
    - Intermediate: gapped modes freeze out at t ~ 1/gap^2, Goldstone dominates
    - IR: d_s -> 0 on finite lattice (lowest eigenvalue is the zero mode)
    - The BCS gap creates a hierarchy of freezeout scales

Gate: CONDENSED-DS-53. INFO: d_s(t) flow from GL spectrum.

Author: Quantum-Acoustics-Theorist (S53)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, log, log10
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import *

print("=" * 70)
print("S53 CONDENSED-DS-53: Spectral Dimension from GL Band Structure")
print("=" * 70)

# ============================================================
# Section 1: Load GL dispersion data
# ============================================================
print("\n--- Section 1: Load GL Josephson data ---")

data = np.load(os.path.join(os.path.dirname(__file__),
                             "s52_gl_josephson.npz"), allow_pickle=True)

K_array = data['K_array']        # (51,) K-points from 0 to K_BZ
omega_branches = data['omega_branches']  # (51, 6) frequencies omega_i(K)
omega_sq = data['omega_sq']      # (51, 6) omega^2 = Laplacian eigenvalues
branch_labels_raw = data['branch_labels']  # ['Goldstone', 'Leggett-1', ...]
branch_labels = [str(b) for b in branch_labels_raw]
K_BZ_val = float(data['K_BZ'])
a_BCC_val = float(data['a_BCC'])

# Replace K_array[0] with 0 for proper integration
K_cont = K_array.copy()
K_cont[0] = 0.0

print(f"  Loaded {omega_sq.shape[0]} K-points, {omega_sq.shape[1]} branches")
print(f"  K range: [0, {K_BZ_val:.6f}], a_BCC = {a_BCC_val:.4f}")
print(f"  Branches: {branch_labels}")

print(f"\n  omega^2 at K=0 (Laplacian eigenvalues):")
for ib in range(6):
    print(f"    {branch_labels[ib]:12s}: omega^2 = {omega_sq[0, ib]:.6e}, "
          f"omega = {omega_branches[0, ib]:.6e}")

print(f"\n  omega^2 at K=K_BZ:")
for ib in range(6):
    print(f"    {branch_labels[ib]:12s}: omega^2 = {omega_sq[-1, ib]:.6e}")

# ============================================================
# Section 2: Construct discrete eigenvalue spectrum
# ============================================================
print("\n--- Section 2: Discrete eigenvalue spectrum ---")

# The 32-cell BCC tessellation is a GRAPH with 32 vertices.
# Each vertex has 6 internal DOF (3 phase + 3 amplitude).
# The angle-averaged dispersion omega^2(K) gives eigenvalues as a function
# of the magnitude |K|.
#
# For a graph with N=32 vertices, there are 32 distinct K-points in the
# 1D Brillouin zone [0, K_BZ]. With 6 branches, total eigenvalues = 192.
# But the K=0 eigenvalues are given by the stored data at K=0,
# and K_BZ eigenvalues by the stored data at K_BZ.
# The stored data has 51 K-points — we interpolate to 32.

N_cells_graph = 32

# Discrete K-points for a 1D BZ with N sites:
# K_n = n * pi / (N * a), n = 0, 1, ..., N (folded BZ)
# But for a graph, the eigenvalues are determined by the adjacency/Laplacian
# structure, which maps to the continuous dispersion at discrete K.
# Use equally spaced K in [0, K_BZ]:
K_discrete = np.linspace(0, K_BZ_val, N_cells_graph + 1)  # 33 points including both endpoints

# Interpolate omega^2 at discrete K-points
omega_sq_discrete = np.zeros((len(K_discrete), 6))
for ib in range(6):
    f_interp = interp1d(K_cont, omega_sq[:, ib], kind='cubic', fill_value='extrapolate')
    omega_sq_discrete[:, ib] = f_interp(K_discrete)

# Enforce non-negativity
omega_sq_discrete = np.maximum(omega_sq_discrete, 0.0)

# All eigenvalues as a flat list
all_eigenvalues = omega_sq_discrete.flatten()
N_modes = len(all_eigenvalues)

# Goldstone eigenvalues only
gold_eigenvalues = omega_sq_discrete[:, 0]
N_gold = len(gold_eigenvalues)

# Gapped eigenvalues only (branches 1-5)
gapped_eigenvalues = omega_sq_discrete[:, 1:].flatten()
N_gapped = len(gapped_eigenvalues)

print(f"  N_cells = {N_cells_graph}, K-points = {len(K_discrete)}")
print(f"  Total eigenvalues: {N_modes} (= {len(K_discrete)} x 6)")
print(f"  Goldstone: {N_gold}, Gapped: {N_gapped}")
print(f"  Eigenvalue range: [{np.min(all_eigenvalues):.4e}, {np.max(all_eigenvalues):.4e}]")
print(f"  Zero modes (< 1e-10): {np.sum(all_eigenvalues < 1e-10)}")

# Sort for analysis
all_eig_sorted = np.sort(all_eigenvalues)
print(f"\n  Lowest 10 eigenvalues:")
for i in range(min(10, len(all_eig_sorted))):
    print(f"    lambda_{i} = {all_eig_sorted[i]:.6e}")

print(f"\n  Highest 5 eigenvalues:")
for i in range(5):
    idx = -(5-i)  # (local)
    print(f"    lambda_{N_modes+idx} = {all_eig_sorted[idx]:.6e}")

# ============================================================
# Section 3: Heat kernel and spectral dimension
# ============================================================
print("\n--- Section 3: Heat kernel and spectral dimension ---")

# Time range: resolve from UV (smallest eigenvalue scale) to IR
# Smallest nonzero eigenvalue determines the IR cutoff
lambda_min_nonzero = all_eig_sorted[1]  # index 0 is zero mode
lambda_max = all_eig_sorted[-1]
print(f"  lambda_min (nonzero) = {lambda_min_nonzero:.6e}")
print(f"  lambda_max = {lambda_max:.6e}")

t_min = 0.001 / lambda_max
t_max = 200.0 / lambda_min_nonzero  # (local)
N_t = 3000  # (local)
t_array = np.logspace(np.log10(t_min), np.log10(t_max), N_t)
print(f"  t range: [{t_min:.4e}, {t_max:.4e}] ({N_t} points)")


def heat_kernel_ds(eigenvalues, t_arr):
    """Compute P(t) and d_s(t) from a set of Laplacian eigenvalues.

    P(t) = (1/N) sum_n exp(-lambda_n * t)
    d_s(t) = -2 * d(log P) / d(log t)

    For a finite system with a zero mode, P(t) -> 1/N as t -> infty,
    so d_s -> 0. This is correct: the spectral dimension of a finite graph
    vanishes at large t.
    """
    N = len(eigenvalues)
    N_t_loc = len(t_arr)

    P = np.zeros(N_t_loc)
    for it, t in enumerate(t_arr):
        P[it] = np.mean(np.exp(-eigenvalues * t))

    # d_s from centered log-derivative
    log_t = np.log(t_arr)
    log_P = np.log(np.maximum(P, 1e-300))

    ds = np.zeros(N_t_loc)
    ds[1:-1] = -2.0 * (log_P[2:] - log_P[:-2]) / (log_t[2:] - log_t[:-2])
    ds[0] = ds[1]
    ds[-1] = ds[-2]

    return P, ds


# All 6 branches
print("\n  Computing: all 6 branches (discrete)...")
P_all, ds_all = heat_kernel_ds(all_eigenvalues, t_array)

# Goldstone only
print("  Computing: Goldstone branch only...")
P_gold, ds_gold = heat_kernel_ds(gold_eigenvalues, t_array)

# Gapped only (5 branches)
print("  Computing: gapped branches only...")
P_gapped, ds_gapped = heat_kernel_ds(gapped_eigenvalues, t_array)

# --- Effective 3D K-multiplicity approach ---
# On a 3D BCC lattice, each K-shell at |K| has a multiplicity proportional
# to K^2 dK (from the 3D density of states). This increases the effective
# number of modes at high K.
# Construct: for each K_n, assign multiplicity ~ K_n^2 (normalized).
# This does NOT change the eigenvalues, only their statistical weight in P(t).
print("  Computing: 3D-weighted (K^2 multiplicity)...")

K_weights_3D = K_discrete**2
K_weights_3D[0] = 0.0  # K=0 gets zero weight from K^2 --- BUT this kills the zero mode
# That's physically wrong for the return probability. Instead, give K=0 its
# proper weight from the 3D DOS: the angular integral at K=0 gives a point,
# so its weight should be treated as the lowest shell, not zero.
# In practice for a finite graph, each K-point is equally weighted.
# The K^2 weighting only applies to the CONTINUOUS limit.
#
# For a 32-vertex graph, the spectral dimension is determined by the graph
# Laplacian, not a continuum K-integral. The K^2 measure is an artifact
# of pretending the discrete graph is a section of R^3.
# We include it only for COMPARISON to show the artifact.

# With K^2 weighting (zero mode suppressed):
all_eig_3D_weighted = []
w_3D = []
for ik, K in enumerate(K_discrete):
    w = max(K**2, 1e-20)  # regularize K=0
    for ib in range(6):
        all_eig_3D_weighted.append(omega_sq_discrete[ik, ib])
        w_3D.append(w)
all_eig_3D_weighted = np.array(all_eig_3D_weighted)
w_3D = np.array(w_3D)
w_3D /= np.sum(w_3D)  # normalize

P_3Dw = np.zeros(N_t)
for it, t in enumerate(t_array):
    P_3Dw[it] = np.sum(w_3D * np.exp(-all_eig_3D_weighted * t))

log_t = np.log(t_array)
log_P_3Dw = np.log(np.maximum(P_3Dw, 1e-300))
ds_3Dw = np.zeros(N_t)
ds_3Dw[1:-1] = -2.0 * (log_P_3Dw[2:] - log_P_3Dw[:-2]) / (log_t[2:] - log_t[:-2])
ds_3Dw[0] = ds_3Dw[1]
ds_3Dw[-1] = ds_3Dw[-2]

# ============================================================
# Section 4: Key energy scales and crossovers
# ============================================================
print("\n--- Section 4: Crossover scales ---")

# Gap energies (K=0 values)
gaps = {
    'Goldstone BW': np.max(omega_sq_discrete[:, 0]),
    'Leggett-1 gap': omega_sq_discrete[0, 1],
    'Leggett-2 gap': omega_sq_discrete[0, 2],
    'Branch-3 gap': omega_sq_discrete[0, 3],
    'Branch-4 gap': omega_sq_discrete[0, 4],
    'Higgs-1 gap': omega_sq_discrete[0, 5],
}

crossover_times = {}
for name, lam in gaps.items():
    if lam > 1e-15:
        t_cross = 1.0 / lam
        crossover_times[name] = t_cross
        idx = np.argmin(np.abs(t_array - t_cross))
        print(f"  {name:20s}: lambda = {lam:.4e}, t_cross = {t_cross:.4f}, "
              f"d_s(all) = {ds_all[idx]:.4f}, d_s(gold) = {ds_gold[idx]:.4f}")

# ============================================================
# Section 5: Plateau analysis
# ============================================================
print("\n--- Section 5: Plateau analysis ---")

# Find regions where d_s is approximately constant
# Smooth d_s with a rolling window
window = 100  # (local)
if N_t > 2 * window:
    ds_smooth = np.convolve(ds_all, np.ones(window)/window, mode='valid')
    t_smooth = t_array[window//2:window//2+len(ds_smooth)]

    # Derivative |d(d_s)/d(log t)|
    dds = np.abs(np.gradient(ds_smooth, np.log(t_smooth)))
    plateaus = np.where(dds < 0.05)[0]

    if len(plateaus) > 0:
        # Find segments
        breaks = np.where(np.diff(plateaus) > 5)[0]
        segments = np.split(plateaus, breaks + 1)

        print(f"  Found {len(segments)} plateau segments:")
        for seg_i, seg in enumerate(segments[:5]):  # show first 5
            if len(seg) > 20:
                mid = seg[len(seg)//2]
                t_mid = t_smooth[mid]
                ds_mid = ds_smooth[mid]
                width = np.log10(t_smooth[seg[-1]] / t_smooth[seg[0]])
                print(f"    Plateau {seg_i}: d_s ~ {ds_mid:.3f} at t ~ {t_mid:.3e}, "
                      f"width = {width:.2f} decades")
    else:
        print("  No plateaus found (derivative always > 0.05)")

# ============================================================
# Section 6: Compare with bare D_K^2 expectations
# ============================================================
print("\n--- Section 6: Comparison with bare Dirac spectrum ---")
print(f"""
  BARE D_K^2 (DS-QUANTUM-52):
    d_s -> 8 (Weyl asymptotics on 8D SU(3))
    Monotonically approaches 8 — FAIL for d_s = 4

  CONDENSED GL spectrum (this computation):
    The BCS condensate creates a tight-binding band structure with 6 branches.
    The spectrum now lives on a 32-vertex GRAPH, not on the 8D continuum.

  Key result: on a graph, the spectral dimension at intermediate t reflects the
  graph's effective dimensionality. A 32-vertex BCC graph embedded in SU(3) has:
    - Coordination number z = 14 (8 NN + 6 NNN)
    - Effective dimension d_eff ~ ln(z)/ln(2) ~ 3.8 (heuristic)
    - But the graph spectral dimension depends on the eigenvalue distribution,
      not just coordination

  The BCS gap creates a scale separation:
    t < 1/lambda_Higgs: all modes active, d_s ~ d_graph
    1/lambda_Higgs < t < 1/lambda_Leggett: Higgs frozen, 5 active modes
    t > 1/lambda_Goldstone_BW: only Goldstone mode active, d_s -> d_Goldstone
    t >> 1/lambda_min: finite-size d_s -> 0
""")

# ============================================================
# Section 7: Maximum d_s and the d_s = 4 question
# ============================================================
print("\n--- Section 7: d_s = 4 question ---")

# Find maximum d_s for each method
margin = 50  # skip endpoints
ds_max_all = np.max(ds_all[margin:-margin])
ds_max_gold = np.max(ds_gold[margin:-margin])
ds_max_gapped = np.max(ds_gapped[margin:-margin])
ds_max_3Dw = np.max(ds_3Dw[margin:-margin])

idx_max_all = np.argmax(ds_all[margin:-margin]) + margin
idx_max_gold = np.argmax(ds_gold[margin:-margin]) + margin

print(f"  Maximum d_s:")
print(f"    All branches (discrete):    {ds_max_all:.4f} at t = {t_array[idx_max_all]:.4e}")
print(f"    Goldstone only:             {ds_max_gold:.4f} at t = {t_array[idx_max_gold]:.4e}")
print(f"    Gapped only:                {ds_max_gapped:.4f}")
print(f"    3D-weighted (K^2, artifact): {ds_max_3Dw:.4f}")

# Check d_s = 4 crossing
for thr in [0.5, 0.3, 0.1]:
    near_4 = np.where(np.abs(ds_all[margin:-margin] - 4.0) < thr)[0]
    if len(near_4) > 0:
        print(f"\n  d_s within {thr} of 4: YES ({len(near_4)} points)")
        print(f"    Range: t in [{t_array[near_4[0]+margin]:.3e}, {t_array[near_4[-1]+margin]:.3e}]")
    else:
        print(f"\n  d_s within {thr} of 4: NO")

# IR limit
print(f"\n  IR behavior:")
print(f"    d_s(all, t_max) = {ds_all[-margin]:.4f}")
print(f"    d_s(gold, t_max) = {ds_gold[-margin]:.4f}")
print(f"    P(all, t_max) = {P_all[-margin]:.6e}")
print(f"    Expected P(t->inf) = 1/N = {1.0/N_modes:.6e} (zero mode saturation)")

# ============================================================
# Section 8: Analytic cross-check via Weyl counting
# ============================================================
print("\n--- Section 8: Weyl counting cross-check ---")

# For a set of N eigenvalues {lambda_n}, the integrated density of states is:
# N(lambda) = #{n : lambda_n < lambda}
# If N(lambda) ~ lambda^{d/2}, then d_s ~ d at the scale t ~ 1/lambda.
# This is the Weyl law.

# Compute the eigenvalue counting function
lam_sorted = np.sort(all_eigenvalues)
N_cumul = np.arange(1, len(lam_sorted) + 1)

# Fit power law N(lambda) = A * lambda^{alpha} in different ranges
# d_s = 2 * alpha
from numpy.polynomial import polynomial as P_fit

# Use log-log regression on nonzero eigenvalues
mask_nz = lam_sorted > 1e-10
if np.sum(mask_nz) > 10:
    log_lam = np.log(lam_sorted[mask_nz])
    log_N = np.log(N_cumul[mask_nz])

    # Full range
    coeffs = np.polyfit(log_lam, log_N, 1)
    alpha_full = coeffs[0]
    print(f"  Weyl exponent (full range): alpha = {alpha_full:.4f}, d_s(Weyl) = {2*alpha_full:.4f}")

    # Low-eigenvalue range (first half of nonzero)
    n_half = np.sum(mask_nz) // 2
    if n_half > 5:
        coeffs_low = np.polyfit(log_lam[:n_half], log_N[:n_half], 1)
        alpha_low = coeffs_low[0]
        print(f"  Weyl exponent (low-lambda): alpha = {alpha_low:.4f}, d_s(Weyl) = {2*alpha_low:.4f}")

    # High-eigenvalue range (second half)
    if n_half > 5:
        coeffs_hi = np.polyfit(log_lam[n_half:], log_N[n_half:], 1)
        alpha_hi = coeffs_hi[0]
        print(f"  Weyl exponent (high-lambda): alpha = {alpha_hi:.4f}, d_s(Weyl) = {2*alpha_hi:.4f}")

    # Goldstone branch only
    gold_sorted = np.sort(gold_eigenvalues)
    mask_g = gold_sorted > 1e-10
    if np.sum(mask_g) > 5:
        log_lam_g = np.log(gold_sorted[mask_g])
        log_N_g = np.log(np.arange(1, np.sum(mask_g) + 1))
        coeffs_g = np.polyfit(log_lam_g, log_N_g, 1)
        alpha_g = coeffs_g[0]
        print(f"  Goldstone Weyl exponent: alpha = {alpha_g:.4f}, d_s(Weyl) = {2*alpha_g:.4f}")

# ============================================================
# Section 9: Gate Verdict
# ============================================================
print("\n--- Section 9: Gate Verdict ---")

print(f"\n  GATE: CONDENSED-DS-53")
print(f"  VERDICT: INFO")
print(f"  DETAIL:")
print(f"    d_s flow computed from GL 6-branch tight-binding spectrum")
print(f"    on 32-cell BCC Voronoi tessellation of SU(3).")
print(f"")
print(f"    Discrete graph (CORRECT method):")
print(f"      d_s_max = {ds_max_all:.3f} at t = {t_array[idx_max_all]:.3e}")
print(f"      d_s at Leggett-2 gap scale: {ds_all[np.argmin(np.abs(t_array - 1.0/omega_sq_discrete[0,2]))]:.3f}")
print(f"      d_s -> {ds_all[-margin]:.3f} (IR, finite-size saturation)")
print(f"")
print(f"    Goldstone-only:")
print(f"      d_s_max = {ds_max_gold:.3f}")
print(f"")
print(f"    3D K^2 weighting (ARTIFACT for finite graph):")
print(f"      d_s_max = {ds_max_3Dw:.3f} (divergent at large t, K=0 weight -> 0)")
print(f"")
print(f"    KEY FINDING: The condensed spectrum reduces d_s from 8 (bare Dirac)")
print(f"    to ~ {ds_max_all:.1f} (tight-binding graph). The BCS condensation projects")
print(f"    the 8D SU(3) manifold onto the low-dimensional BCC graph.")
if ds_max_all > 3.5 and ds_max_all < 4.5:
    print(f"    d_s passes through 4 --- DIMENSIONAL REDUCTION from 8 to 4 achieved.")
elif ds_max_all < 3.5:
    print(f"    d_s does NOT reach 4 --- BCC graph is too low-dimensional.")
    print(f"    The graph spectral dimension ~ {ds_max_all:.1f} reflects the BCC")
    print(f"    coordination structure, not the embedding dimension.")
else:
    print(f"    d_s exceeds 4 --- intermediate between graph and continuum.")

# ============================================================
# Section 10: Plotting
# ============================================================
print("\n--- Section 10: Generating plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('CONDENSED-DS-53: Spectral Dimension from GL Band Structure',
             fontsize=13, fontweight='bold')

# Color scheme
c_all = '#1f77b4'
c_gold = '#d62728'
c_gapped = '#2ca02c'
c_3Dw = '#ff7f0e'

# --- Panel A: d_s(t) main result ---
ax = axes[0, 0]
ax.semilogx(t_array, ds_all, color=c_all, lw=2.0, label='All 6 branches (discrete)')
ax.semilogx(t_array, ds_gold, color=c_gold, lw=1.5, ls='--', label='Goldstone only')
# Clip gapped d_s to avoid divergence artifact (no zero mode -> P->0 -> d_s->inf)
ds_gapped_panel = np.clip(ds_gapped, -1, 10)
ax.semilogx(t_array, ds_gapped_panel, color=c_gapped, lw=1.5, ls='-.', label='Gapped only (5 branches)')
ax.axhline(y=4, color='k', ls='--', alpha=0.5, lw=1, label='$d_s = 4$ (M$^4$ target)')
ax.axhline(y=8, color='gray', ls=':', alpha=0.4, lw=0.8, label='$d_s = 8$ (bare SU(3))')
ax.axhline(y=3, color='gray', ls=':', alpha=0.3, lw=0.8)
ax.axhline(y=1, color='gray', ls=':', alpha=0.2, lw=0.8)

# Mark crossover scales
vline_data = [
    ('$t_H$', 1.0/omega_sq_discrete[0, 5], 'purple'),
    ('$t_{L2}$', 1.0/omega_sq_discrete[0, 2], 'orange'),
    ('$t_{L1}$', 1.0/omega_sq_discrete[0, 1], 'brown'),
    ('$t_{BW}$', 1.0/np.max(omega_sq_discrete[:, 0]), 'green'),
]
for name, t_val, col in vline_data:
    if t_min < t_val < t_max:
        ax.axvline(x=t_val, color=col, ls=':', alpha=0.5, lw=0.8)
        ax.text(t_val*1.1, ds_max_all * 0.92, name, fontsize=7, color=col, va='top')

ax.set_xlabel('$t$ (diffusion time, $M_{KK}^{-2}$)', fontsize=10)
ax.set_ylabel('$d_s(t)$', fontsize=11)
ax.set_title('(A) Spectral Dimension Flow', fontsize=11)
ax.legend(fontsize=7, loc='upper right')
y_top = min(max(8.5, ds_max_all * 1.3), 12)
ax.set_ylim(-0.3, y_top)
ax.grid(True, alpha=0.3)

# --- Panel B: d_s zoomed into intermediate t ---
ax = axes[0, 1]
# Focus on t range where d_s is interesting
t_zoom_min = 0.01  # (local)
t_zoom_max = 1000.0  # (local)
mask_zoom = (t_array > t_zoom_min) & (t_array < t_zoom_max)
ax.semilogx(t_array[mask_zoom], ds_all[mask_zoom], color=c_all, lw=2.0, label='All 6 branches')
ax.semilogx(t_array[mask_zoom], ds_gold[mask_zoom], color=c_gold, lw=1.5, ls='--', label='Goldstone only')
ds_gapped_clipped = np.clip(ds_gapped, -1, 10)
ax.semilogx(t_array[mask_zoom], ds_gapped_clipped[mask_zoom], color=c_gapped, lw=1.5, ls='-.', label='Gapped only')
ax.axhline(y=4, color='k', ls='--', alpha=0.5, lw=1)
ax.axhline(y=3, color='gray', ls=':', alpha=0.4, lw=0.8)
for name, t_val, col in vline_data:
    if t_zoom_min < t_val < t_zoom_max:
        ax.axvline(x=t_val, color=col, ls=':', alpha=0.6, lw=1.0)
        ax.text(t_val*1.15, 0.3, name, fontsize=8, color=col)

ax.set_xlabel('$t$ (diffusion time)', fontsize=10)
ax.set_ylabel('$d_s(t)$', fontsize=11)
ax.set_title('(B) Intermediate-Scale Zoom', fontsize=11)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel C: Return probability P(t) ---
ax = axes[1, 0]
ax.loglog(t_array, P_all, color=c_all, lw=2.0, label='$P(t)$ all branches')
ax.loglog(t_array, P_gold, color=c_gold, lw=1.5, ls='--', label='$P(t)$ Goldstone')
ax.loglog(t_array, P_gapped, color=c_gapped, lw=1.5, ls='-.', label='$P(t)$ gapped')
# Reference slopes
t_ref = t_array[N_t//3:2*N_t//3]
P_ref_start = P_all[N_t//3]
P_ref_2 = P_ref_start * (t_ref / t_ref[0])**(-2.0)  # d_s = 4
P_ref_15 = P_ref_start * (t_ref / t_ref[0])**(-1.5)  # d_s = 3
P_ref_05 = P_ref_start * (t_ref / t_ref[0])**(-0.5)  # d_s = 1
ax.loglog(t_ref, P_ref_2, 'k--', alpha=0.25, lw=0.8, label='$t^{-2}$ ($d_s=4$)')
ax.loglog(t_ref, P_ref_15, 'k:', alpha=0.25, lw=0.8, label='$t^{-3/2}$ ($d_s=3$)')
# Saturation level
ax.axhline(y=1.0/N_modes, color='gray', ls='--', alpha=0.3, lw=0.8)
ax.text(t_array[10], 1.0/N_modes * 1.5, f'$1/N = {1.0/N_modes:.4f}$',
        fontsize=7, color='gray')
ax.set_xlabel('$t$', fontsize=10)
ax.set_ylabel('$P(t)$', fontsize=11)
ax.set_title('(C) Return Probability (Heat Kernel Trace)', fontsize=11)
ax.legend(fontsize=7, loc='best')
ax.grid(True, alpha=0.3)

# --- Panel D: Eigenvalue counting function (Weyl law) ---
ax = axes[1, 1]
# Plot N(lambda) = #{eigenvalues < lambda}
lam_plot = np.sort(all_eigenvalues)
N_count = np.arange(1, len(lam_plot) + 1)
ax.loglog(lam_plot[1:], N_count[1:], color=c_all, lw=1.5, label='All branches')

gold_plot = np.sort(gold_eigenvalues)
N_gold_count = np.arange(1, len(gold_plot) + 1)
ax.loglog(gold_plot[1:], N_gold_count[1:], color=c_gold, lw=1.5, ls='--', label='Goldstone')

# Reference Weyl slopes
lam_ref = np.logspace(np.log10(lam_plot[2]), np.log10(lam_plot[-1]), 100)
ax.loglog(lam_ref, 2.0 * lam_ref**0.5, 'k:', alpha=0.3, label='$\\lambda^{0.5}$ ($d_s=1$)')
ax.loglog(lam_ref, 0.5 * lam_ref**1.0, 'k--', alpha=0.3, label='$\\lambda^{1.0}$ ($d_s=2$)')
ax.loglog(lam_ref, 0.2 * lam_ref**1.5, 'k-.', alpha=0.3, label='$\\lambda^{1.5}$ ($d_s=3$)')
ax.loglog(lam_ref, 0.1 * lam_ref**2.0, color='gray', ls='--', alpha=0.3, label='$\\lambda^{2.0}$ ($d_s=4$)')

ax.set_xlabel('$\\lambda$ (eigenvalue)', fontsize=10)
ax.set_ylabel('$N(\\lambda)$', fontsize=11)
ax.set_title('(D) Eigenvalue Counting (Weyl Law)', fontsize=11)
ax.legend(fontsize=7, loc='best')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(__file__), "s53_condensed_ds.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plot_path}")

# ============================================================
# Section 11: Summary table
# ============================================================
print("\n--- Section 11: Summary Table ---")
print(f"\n  =============== CONDENSED-DS-53 SUMMARY ===============")
print(f"  {'Quantity':35s} {'Value':>12s}")
print(f"  {'-'*35} {'-'*12}")
print(f"  {'d_s(bare D_K^2, S52)':35s} {'8.0':>12s}")
print(f"  {'d_s_max(GL, all 6 branches)':35s} {ds_max_all:12.3f}")
print(f"  {'d_s_max(Goldstone only)':35s} {ds_max_gold:12.3f}")
print(f"  {'d_s_max(gapped only)':35s} {ds_max_gapped:12.3f}")
print(f"  {'d_s at Leggett-2 scale':35s} {ds_all[np.argmin(np.abs(t_array - 1.0/omega_sq_discrete[0,2]))]:12.3f}")
print(f"  {'d_s at Goldstone BW scale':35s} {ds_all[np.argmin(np.abs(t_array - 1.0/np.max(omega_sq_discrete[:,0])))]:12.3f}")
print(f"  {'d_s(IR, t -> inf)':35s} {ds_all[-margin]:12.3f}")
print(f"  {'P(t -> inf)':35s} {P_all[-margin]:12.6e}")
print(f"  {'1/N_modes (zero-mode floor)':35s} {1.0/N_modes:12.6e}")
print(f"  {'N_modes total':35s} {N_modes:>12d}")
print(f"  {'Spectral gap (lambda_min)':35s} {lambda_min_nonzero:12.6e}")
print(f"  ========================================================")

# ============================================================
# Section 12: Save data
# ============================================================
save_path = os.path.join(os.path.dirname(__file__), "s53_condensed_ds.npz")
np.savez(save_path,
    t_array=t_array,
    P_all=P_all, ds_all=ds_all,
    P_gold=P_gold, ds_gold=ds_gold,
    P_gapped=P_gapped, ds_gapped=ds_gapped,
    P_3Dw=P_3Dw, ds_3Dw=ds_3Dw,
    omega_sq_discrete=omega_sq_discrete,
    K_discrete=K_discrete,
    all_eigenvalues=all_eigenvalues,
    gold_eigenvalues=gold_eigenvalues,
    gapped_eigenvalues=gapped_eigenvalues,
    branch_labels=np.array(branch_labels),
    ds_max_all=np.array(ds_max_all),
    ds_max_gold=np.array(ds_max_gold),
    ds_max_gapped=np.array(ds_max_gapped),
    lambda_min_nonzero=np.array(lambda_min_nonzero),
    N_modes=np.array(N_modes),
    gate_name=np.array(['CONDENSED-DS-53']),
    gate_verdict=np.array(['INFO']),
)
print(f"\n  Data saved: {save_path}")

print("\n" + "=" * 70)
print("CONDENSED-DS-53 COMPLETE")
print("=" * 70)
