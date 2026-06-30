#!/usr/bin/env python3
"""
s58_off_jensen_dw.py — OFF-JENSEN-DW-58 (W3-9)
================================================
Gate: E_DW(delta_sigma) > 0?   (INFO)

Physics:
  The 32-cell Voronoi tessellation of SU(3) has cells connected by Josephson
  bonds. S57 computed E_J(tau, sigma) where sigma parametrizes the T^2
  deformation breaking the Jensen line. When ALL cells share the same sigma,
  the fabric is uniform — no domain walls.

  A domain wall forms when adjacent cells sit at different sigma values:
  cell 1 at sigma_1 = 0 (Jensen), cell 2 at sigma_2 = delta_sigma.

  The inter-cell Josephson coupling depends on BOTH cells' geometries.
  For WKB tunneling between two regions with curvatures R_1 and R_2,
  the hopping integral goes through the geometric mean:
    J(sigma_1, sigma_2) = sqrt( J(sigma_1) * J(sigma_2) )
  This is the standard WKB result: the transmission amplitude through
  a double barrier is the geometric mean of the individual amplitudes.

  Domain wall energy per bond:
    E_DW(delta_sigma) = E_J(0, delta_sigma) - E_J(0, 0)
  where E_J(sigma_1, sigma_2) = J_eff(sigma_1, sigma_2)^2 * F_anom_eff(sigma_1, sigma_2)

  Sign convention: E_DW > 0 means walls COST energy (stable uniform state).
                   E_DW < 0 means walls are FAVORABLE (spontaneous differentiation).

Method:
  1. Load E_J(tau, sigma) landscape from S57 (both approaches A and B).
  2. Load bond structure from S54 TB Hamiltonian.
  3. At the fold (tau ~ 0.19), construct inter-cell E_J for mismatched sigma.
  4. Compute E_DW(delta_sigma) for 20 values of delta_sigma in [1e-4, 0.1].
  5. For the full 32-cell fabric, compute total domain wall energy for one
     wall separating two domains.

Output: s58_off_jensen_dw.npz
"""

import sys
sys.path.insert(0, 'computations')
import numpy as np
from scipy.interpolate import RectBivariateSpline, interp1d
from canonical_constants import (
    tau_fold, N_cells, J_C2, PI, E_cond, M_KK,
    a2_fold, a4_fold
)

# =============================================================================
# 1. Load data
# =============================================================================
oj = np.load('computations/session-57/s57_off_jensen_ej.npz', allow_pickle=True)
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)

tau_range = oj['tau_range']       # (51,) in [0, 0.4]
sig_range = oj['sig_range']       # (41,) in [-0.015, 0.015]
E_J_A = oj['E_J_A']              # (51, 41) approach A (curvature-ratio J)
E_J_B = oj['E_J_B']              # (51, 41) approach B (spectral-density J)
J_C2_grid_A = oj['J_C2_grid_A']  # (51, 41)
J_C2_grid_B = oj['J_C2_grid_B']  # (51, 41)
F_anom_grid = oj['F_anom_grid']   # (51, 41)
V_grid = oj['V_grid']            # (51, 41) spectral action potential
R_grid = oj['R_grid']            # (51, 41) scalar curvature

# Bond structure
adj_C2 = tb['adj_C2']            # (32, 32) C2 adjacency
adj_su2 = tb['adj_su2']          # (32, 32) su2 adjacency
adj_u1 = tb['adj_u1']            # (32, 32) u1 adjacency
adjacency = tb['adjacency']      # (32, 32) total adjacency
n_bonds_C2 = int(tb['n_bonds_C2'])    # 50
n_bonds_su2 = int(tb['n_bonds_su2'])  # 24
n_bonds_u1 = int(tb['n_bonds_u1'])    # 19
n_bonds_total = int(tb['n_bonds_total'])  # 93

# TB couplings on-Jensen
tau_tb = tb['tau_values']         # (50,) in [0, 0.5]
J_C2_tb = tb['J_C2_tau']         # (50,) on-Jensen
J_su2_tb = tb['J_su2_tau']       # (50,)
J_u1_tb = tb['J_u1_tau']         # (50,)

print("=== Input data loaded ===")
print(f"Off-Jensen grid: {len(tau_range)} x {len(sig_range)}")
print(f"tau range: [{tau_range[0]:.3f}, {tau_range[-1]:.3f}]")
print(f"sigma range: [{sig_range[0]:.5f}, {sig_range[-1]:.5f}]")
print(f"Bond structure: {n_bonds_C2} C2 + {n_bonds_su2} su2 + {n_bonds_u1} u1 = {n_bonds_total} total")
print(f"N_cells = {N_cells}")

# =============================================================================
# 2. Build interpolators for J and F_anom as functions of (tau, sigma)
# =============================================================================
# We need J(tau, sigma) and F_anom(tau, sigma) as smooth functions.
# Use the Approach B data (spectral-density based) as primary — it has
# the saddle structure found in S57.

J_C2_spline = RectBivariateSpline(tau_range, sig_range, J_C2_grid_B, kx=3, ky=3)
F_anom_spline = RectBivariateSpline(tau_range, sig_range, F_anom_grid, kx=3, ky=3)

# Also build splines for approach A for cross-check
J_C2_spline_A = RectBivariateSpline(tau_range, sig_range, J_C2_grid_A, kx=3, ky=3)

# On-Jensen 1D interpolators for reference
J_C2_1d = interp1d(tau_tb, J_C2_tb, kind='cubic', fill_value='extrapolate')

print(f"\nJ_C2 at fold (on-Jensen, TB): {J_C2_1d(tau_fold):.6f}")
print(f"J_C2 at fold (grid B, sigma=0): {J_C2_spline(tau_fold, 0.0)[0,0]:.6f}")
print(f"F_anom at fold (sigma=0): {F_anom_spline(tau_fold, 0.0)[0,0]:.6e}")

# =============================================================================
# 3. Domain wall energy: WKB geometric-mean construction
# =============================================================================
# The Josephson coupling between cell i (at sigma_i) and cell j (at sigma_j)
# depends on the tunneling amplitude through the shared boundary.
#
# WKB tunneling: T ~ exp(-integral_path sqrt(2m(V-E)) dx)
# For two cells at different sigma, the barrier is the average:
#   T(sigma_i, sigma_j) ~ sqrt(T(sigma_i, sigma_i) * T(sigma_j, sigma_j))
#
# This gives:
#   J_eff(sigma_i, sigma_j) = sqrt(J(sigma_i) * J(sigma_j))
#   where J(sigma) = J_C2(tau, sigma) from the homogeneous calculation
#
# The Josephson ENERGY for a bond between cells at sigma_i, sigma_j:
#   E_J(sigma_i, sigma_j) = J_eff^2 * F_anom_eff
#                         = J(sigma_i)*J(sigma_j) * sqrt(F_anom(sigma_i)*F_anom(sigma_j))
#
# Actually, E_J = J_C2^2 * F_anom from S57. The inter-cell E_J for mismatched
# cells uses the geometric mean of J (WKB) and arithmetic mean of F_anom
# (spectral density averages). But the most conservative approach is:
#   E_J_bond(sigma_i, sigma_j) = sqrt(E_J(sigma_i) * E_J(sigma_j))
# i.e., geometric mean of the full Josephson energy.
#
# Alternative: arithmetic mean
#   E_J_bond(sigma_i, sigma_j) = 0.5*(E_J(sigma_i) + E_J(sigma_j))
#
# We compute BOTH for robustness.

def E_J_homogeneous(tau, sigma, approach='B'):
    """E_J for a bond where both cells are at the same sigma."""
    if approach == 'B':
        J = J_C2_spline(tau, sigma)[0, 0]
        F = F_anom_spline(tau, sigma)[0, 0]
    else:
        J = J_C2_spline_A(tau, sigma)[0, 0]
        F = F_anom_spline(tau, sigma)[0, 0]
    return J**2 * F

def E_J_bond_geom(tau, sigma_1, sigma_2, approach='B'):
    """E_J for a bond between cells at sigma_1 and sigma_2 (geometric mean)."""
    EJ1 = E_J_homogeneous(tau, sigma_1, approach)
    EJ2 = E_J_homogeneous(tau, sigma_2, approach)
    return np.sqrt(EJ1 * EJ2)

def E_J_bond_arith(tau, sigma_1, sigma_2, approach='B'):
    """E_J for a bond between cells at sigma_1 and sigma_2 (arithmetic mean)."""
    EJ1 = E_J_homogeneous(tau, sigma_1, approach)
    EJ2 = E_J_homogeneous(tau, sigma_2, approach)
    return 0.5 * (EJ1 + EJ2)

def E_J_bond_product(tau, sigma_1, sigma_2, approach='B'):
    """E_J for a bond using product of J values and geometric mean of F_anom."""
    if approach == 'B':
        J1 = J_C2_spline(tau, sigma_1)[0, 0]
        J2 = J_C2_spline(tau, sigma_2)[0, 0]
        F1 = F_anom_spline(tau, sigma_1)[0, 0]
        F2 = F_anom_spline(tau, sigma_2)[0, 0]
    else:
        J1 = J_C2_spline_A(tau, sigma_1)[0, 0]
        J2 = J_C2_spline_A(tau, sigma_2)[0, 0]
        F1 = F_anom_spline(tau, sigma_1)[0, 0]
        F2 = F_anom_spline(tau, sigma_2)[0, 0]
    return J1 * J2 * np.sqrt(F1 * F2)

# =============================================================================
# 4. Scan domain wall energy at the fold
# =============================================================================
# delta_sigma range: 1e-4 to 0.1 in 20 log-spaced steps
# But sigma range is only [-0.015, 0.015], so clamp to available range
sig_max_data = sig_range[-1]  # 0.015
delta_sigma_scan = np.logspace(-4, np.log10(sig_max_data), 20)
# Also add linear steps for better resolution at small delta_sigma
delta_sigma_linear = np.linspace(1e-4, sig_max_data, 20)
delta_sigma_all = np.sort(np.unique(np.concatenate([delta_sigma_scan, delta_sigma_linear])))

print(f"\n=== Domain wall scan at tau_fold = {tau_fold} ===")
print(f"delta_sigma range: [{delta_sigma_all[0]:.2e}, {delta_sigma_all[-1]:.4f}]")
print(f"N_steps: {len(delta_sigma_all)}")

# Reference: E_J at (tau_fold, sigma=0, sigma=0)
EJ_ref_B = E_J_homogeneous(tau_fold, 0.0, 'B')
EJ_ref_A = E_J_homogeneous(tau_fold, 0.0, 'A')
print(f"\nE_J(fold, 0, 0) approach B: {EJ_ref_B:.6e}")
print(f"E_J(fold, 0, 0) approach A: {EJ_ref_A:.6e}")

# Compute E_DW for each delta_sigma, three mixing rules, two approaches
results = {
    'delta_sigma': delta_sigma_all,
    'E_DW_geom_B': np.zeros(len(delta_sigma_all)),
    'E_DW_arith_B': np.zeros(len(delta_sigma_all)),
    'E_DW_prod_B': np.zeros(len(delta_sigma_all)),
    'E_DW_geom_A': np.zeros(len(delta_sigma_all)),
    'E_DW_arith_A': np.zeros(len(delta_sigma_all)),
    'E_DW_prod_A': np.zeros(len(delta_sigma_all)),
    'EJ_bond_geom_B': np.zeros(len(delta_sigma_all)),
    'EJ_bond_arith_B': np.zeros(len(delta_sigma_all)),
    'EJ_bond_prod_B': np.zeros(len(delta_sigma_all)),
    'EJ_homo_0_B': np.zeros(len(delta_sigma_all)),
    'EJ_homo_ds_B': np.zeros(len(delta_sigma_all)),
}

for idx, ds in enumerate(delta_sigma_all):
    # Clamp to data range
    sig2 = min(ds, sig_max_data)

    # Approach B
    EJ_00_B = EJ_ref_B
    EJ_geom_B = E_J_bond_geom(tau_fold, 0.0, sig2, 'B')
    EJ_arith_B = E_J_bond_arith(tau_fold, 0.0, sig2, 'B')
    EJ_prod_B = E_J_bond_product(tau_fold, 0.0, sig2, 'B')

    results['E_DW_geom_B'][idx] = EJ_geom_B - EJ_00_B
    results['E_DW_arith_B'][idx] = EJ_arith_B - EJ_00_B
    results['E_DW_prod_B'][idx] = EJ_prod_B - EJ_00_B
    results['EJ_bond_geom_B'][idx] = EJ_geom_B
    results['EJ_bond_arith_B'][idx] = EJ_arith_B
    results['EJ_bond_prod_B'][idx] = EJ_prod_B
    results['EJ_homo_0_B'][idx] = EJ_00_B
    results['EJ_homo_ds_B'][idx] = E_J_homogeneous(tau_fold, sig2, 'B')

    # Approach A
    EJ_00_A = EJ_ref_A
    EJ_geom_A = E_J_bond_geom(tau_fold, 0.0, sig2, 'A')
    EJ_arith_A = E_J_bond_arith(tau_fold, 0.0, sig2, 'A')
    EJ_prod_A = E_J_bond_product(tau_fold, 0.0, sig2, 'A')

    results['E_DW_geom_A'][idx] = EJ_geom_A - EJ_00_A
    results['E_DW_arith_A'][idx] = EJ_arith_A - EJ_00_A
    results['E_DW_prod_A'][idx] = EJ_prod_A - EJ_00_A

print("\n=== Domain wall energy E_DW (approach B, geometric mean) ===")
print(f"{'delta_sigma':>12s} {'E_DW':>14s} {'E_DW/E_J(0)':>14s} {'sign':>6s}")
for idx, ds in enumerate(delta_sigma_all):
    edw = results['E_DW_geom_B'][idx]
    frac = edw / EJ_ref_B if EJ_ref_B != 0 else 0
    sign = '+' if edw > 0 else ('-' if edw < 0 else '0')
    print(f"{ds:12.6f} {edw:14.6e} {frac:14.6e} {sign:>6s}")

# =============================================================================
# 5. Analytic check: AM-GM inequality
# =============================================================================
# For geometric mean: sqrt(a*b) <= (a+b)/2 always, with equality iff a=b.
# So E_J_geom(0, ds) = sqrt(E_J(0)*E_J(ds)) <= E_J(0) iff E_J(ds) <= E_J(0)
# And E_J_arith(0, ds) = 0.5*(E_J(0)+E_J(ds))
#   E_DW_arith = 0.5*(E_J(ds) - E_J(0))
#   sign(E_DW_arith) = sign(E_J(ds) - E_J(0))
#
# Key question: does E_J increase or decrease with sigma at the fold?
# From S57: E_J_B at fold varies with sigma. Let's check the gradient.

EJ_fold_B = np.array([E_J_homogeneous(tau_fold, s, 'B') for s in sig_range])
dEJ_dsig = np.gradient(EJ_fold_B, sig_range)
mid_idx = len(sig_range) // 2

print(f"\n=== E_J(fold, sigma) profile (approach B) ===")
print(f"E_J at sigma=0: {EJ_fold_B[mid_idx]:.6e}")
print(f"dE_J/dsigma at sigma=0: {dEJ_dsig[mid_idx]:.6e}")
print(f"E_J at sigma=+0.015: {EJ_fold_B[-1]:.6e}")
print(f"E_J at sigma=-0.015: {EJ_fold_B[0]:.6e}")
print(f"E_J(+0.015)/E_J(0): {EJ_fold_B[-1]/EJ_fold_B[mid_idx]:.6f}")
print(f"E_J(-0.015)/E_J(0): {EJ_fold_B[0]/EJ_fold_B[mid_idx]:.6f}")

# Check concavity
d2EJ_dsig2 = np.gradient(dEJ_dsig, sig_range)
print(f"d^2 E_J/dsigma^2 at sigma=0: {d2EJ_dsig2[mid_idx]:.6e}")
curvature_sign = "CONCAVE (max at 0)" if d2EJ_dsig2[mid_idx] < 0 else "CONVEX (min at 0)"
print(f"Curvature: {curvature_sign}")

# Repeat for approach A
EJ_fold_A = np.array([E_J_homogeneous(tau_fold, s, 'A') for s in sig_range])
dEJ_dsig_A = np.gradient(EJ_fold_A, sig_range)
d2EJ_dsig2_A = np.gradient(dEJ_dsig_A, sig_range)
print(f"\nApproach A at sigma=0: E_J={EJ_fold_A[mid_idx]:.6e}, d2E_J/ds2={d2EJ_dsig2_A[mid_idx]:.6e}")
curvature_A = "CONCAVE" if d2EJ_dsig2_A[mid_idx] < 0 else "CONVEX"
print(f"Curvature A: {curvature_A}")

# =============================================================================
# 6. Full fabric domain wall: energy cost for one planar wall
# =============================================================================
# A domain wall cuts the 32-cell graph into two halves.
# Find a minimal cut (fewest bonds crossing the wall).
# Each crossing bond has E_DW per bond.
# Total E_DW_wall = n_cut_bonds * E_DW_per_bond

# For simplicity, estimate the cut size from the graph structure.
# The 32-cell graph has 93 bonds. A bisection into 16+16 cells
# has approximately 93 * 2 * 16/32 * 16/32 ~ 46.5 crossing bonds
# for a random cut. The minimum bisection cut is smaller.

# Use spectral bisection from the adjacency Laplacian
adj_full = adjacency.astype(float)
degree = adj_full.sum(axis=1)
Laplacian = np.diag(degree) - adj_full
eigvals_L, eigvecs_L = np.linalg.eigh(Laplacian)

# Fiedler vector (2nd smallest eigenvalue)
fiedler = eigvecs_L[:, 1]
partition = fiedler > 0
n_plus = partition.sum()
n_minus = (~partition).sum()
print(f"\n=== Spectral bisection of 32-cell graph ===")
print(f"Fiedler eigenvalue (algebraic connectivity): {eigvals_L[1]:.4f}")
print(f"Partition: {n_plus} + {n_minus} cells")

# Count bonds crossing the cut
n_cut = 0
cut_types = {'C2': 0, 'su2': 0, 'u1': 0}
for i in range(N_cells):
    for j in range(i+1, N_cells):
        if partition[i] != partition[j]:
            if adj_C2[i, j]:
                cut_types['C2'] += 1
                n_cut += 1
            if adj_su2[i, j]:
                cut_types['su2'] += 1
                n_cut += 1
            if adj_u1[i, j]:
                cut_types['u1'] += 1
                n_cut += 1

print(f"Bonds crossing cut: {n_cut} total ({cut_types})")
print(f"Cut fraction: {n_cut}/{n_bonds_total} = {n_cut/n_bonds_total:.3f}")

# Total domain wall energy for the bisection
# Use delta_sigma values at a few representative points
ds_representatives = [0.001, 0.005, 0.010, 0.015]
print(f"\n=== Total fabric domain wall energy ===")
print(f"{'delta_sigma':>12s} {'E_DW/bond':>14s} {'E_DW_total':>14s} {'E_DW_total/|E_cond|':>20s}")

E_DW_fabric = {}
for ds in ds_representatives:
    sig2 = min(ds, sig_max_data)
    # Per-bond domain wall energy (geometric mean)
    edw_per_bond = E_J_bond_geom(tau_fold, 0.0, sig2, 'B') - EJ_ref_B
    # Total across cut
    # C2 bonds dominate; weight by coupling strength
    # For simplicity, assume all cut bonds have the C2 E_DW
    edw_total = n_cut * edw_per_bond
    edw_ratio = edw_total / abs(E_cond)
    E_DW_fabric[ds] = edw_total
    print(f"{ds:12.6f} {edw_per_bond:14.6e} {edw_total:14.6e} {edw_ratio:20.6e}")

# =============================================================================
# 7. Tau dependence: scan E_DW at fixed delta_sigma across tau
# =============================================================================
ds_fixed = 0.010  # Representative delta_sigma  # (local)
tau_scan = tau_range[tau_range <= 0.35]  # Focus on physical range

E_DW_tau_geom = np.zeros(len(tau_scan))
E_DW_tau_arith = np.zeros(len(tau_scan))
EJ_homo_tau = np.zeros(len(tau_scan))

for i, tau in enumerate(tau_scan):
    EJ_00 = E_J_homogeneous(tau, 0.0, 'B')
    EJ_geom = E_J_bond_geom(tau, 0.0, ds_fixed, 'B')
    EJ_arith = E_J_bond_arith(tau, 0.0, ds_fixed, 'B')
    E_DW_tau_geom[i] = EJ_geom - EJ_00
    E_DW_tau_arith[i] = EJ_arith - EJ_00
    EJ_homo_tau[i] = EJ_00

print(f"\n=== E_DW(tau) at delta_sigma={ds_fixed} (approach B, geometric mean) ===")
print(f"{'tau':>8s} {'E_DW_geom':>14s} {'E_DW_arith':>14s} {'E_J(0)':>14s}")
for i, tau in enumerate(tau_scan):
    print(f"{tau:8.3f} {E_DW_tau_geom[i]:14.6e} {E_DW_tau_arith[i]:14.6e} {EJ_homo_tau[i]:14.6e}")

# Sign summary
all_positive_geom = np.all(results['E_DW_geom_B'] >= 0)
all_positive_arith = np.all(results['E_DW_arith_B'] >= 0)
all_negative_geom = np.all(results['E_DW_geom_B'] <= 0)
all_negative_arith = np.all(results['E_DW_arith_B'] <= 0)

print(f"\n=== SIGN ANALYSIS ===")
print(f"Geometric mean:  all >= 0: {all_positive_geom}, all <= 0: {all_negative_geom}")
print(f"  min E_DW = {results['E_DW_geom_B'].min():.6e}")
print(f"  max E_DW = {results['E_DW_geom_B'].max():.6e}")
print(f"Arithmetic mean: all >= 0: {all_positive_arith}, all <= 0: {all_negative_arith}")
print(f"  min E_DW = {results['E_DW_arith_B'].min():.6e}")
print(f"  max E_DW = {results['E_DW_arith_B'].max():.6e}")

# =============================================================================
# 8. Structural theorem: AM-GM guarantee
# =============================================================================
# For GEOMETRIC mean mixing:
#   E_DW_geom = sqrt(E_J(0)*E_J(ds)) - E_J(0)
#             = E_J(0) * (sqrt(E_J(ds)/E_J(0)) - 1)
# If E_J(ds) > E_J(0): E_DW_geom > 0 BUT less than arithmetic (AM-GM)
# If E_J(ds) < E_J(0): E_DW_geom < 0
# If E_J(ds) = E_J(0): E_DW_geom = 0
#
# For ARITHMETIC mean mixing:
#   E_DW_arith = 0.5*(E_J(0) + E_J(ds)) - E_J(0) = 0.5*(E_J(ds) - E_J(0))
#   sign = sign(E_J(ds) - E_J(0))
#
# KEY: The sign depends ONLY on whether E_J increases or decreases with sigma.
# From S57 data: E_J_B INCREASES with sigma at the fold (convex in sigma).
# Therefore E_DW > 0 for BOTH mixing rules.
#
# STRUCTURAL RESULT: Domain walls cost energy. The uniform state is stable.
# This is a consequence of E_J being CONVEX in sigma at the fold.

# Verify convexity numerically
EJ_B_at_fold = E_J_B[24, :]  # tau_fold ~ 0.192, index 24
EJ_B_mid = EJ_B_at_fold[20]  # sigma=0
EJ_B_pm = 0.5 * (EJ_B_at_fold[0] + EJ_B_at_fold[-1])  # average of endpoints
convex = EJ_B_pm >= EJ_B_mid
print(f"\nConvexity check: 0.5*(E_J(-0.015)+E_J(+0.015)) = {EJ_B_pm:.6e}")
print(f"                 E_J(0) = {EJ_B_mid:.6e}")
print(f"                 Convex: {convex} (endpoint avg >= midpoint)")

# Quadratic fit to get wall tension
# E_J(sigma) ~ E_J(0) + 0.5 * kappa * sigma^2 (even function at sigma=0)
# Then E_DW_geom(ds) ~ E_J(0) * (sqrt(1 + 0.5*kappa*ds^2/E_J(0)) - 1)
#                     ~ 0.25 * kappa * ds^2 for small ds
from numpy.polynomial import polynomial as P
# Fit even polynomial E_J(sigma) = a0 + a2*sigma^2 + a4*sigma^4
sig2_vals = sig_range**2
coeffs = np.polyfit(sig2_vals, EJ_B_at_fold, 2)
kappa_fit = coeffs[1]  # coefficient of sigma^2 (but polyfit gives highest degree first)
# polyfit: coeffs[0]*x^2 + coeffs[1]*x + coeffs[2] where x = sigma^2
# So E_J ~ coeffs[2] + coeffs[1]*sigma^2 + coeffs[0]*sigma^4
a0_fit = coeffs[2]
a2_fit = coeffs[1]  # This is kappa/2 effectively
a4_fit = coeffs[0]

print(f"\nQuadratic fit: E_J(sigma) = {a0_fit:.6e} + {a2_fit:.4e}*sigma^2 + {a4_fit:.4e}*sigma^4")
print(f"Wall stiffness kappa = 2*a2 = {2*a2_fit:.4e} M_KK per sigma^2")

# Surface tension: E_DW / (domain wall area)
# The domain wall area in the graph is n_cut bonds.
# Tension = E_DW_per_bond (dimensionless in M_KK units)
sigma_tension_001 = E_J_bond_geom(tau_fold, 0.0, 0.01, 'B') - EJ_ref_B
print(f"\nDomain wall tension at delta_sigma=0.01: {sigma_tension_001:.6e} M_KK per bond")

# =============================================================================
# 9. Connection to BCS: E_DW vs condensation energy
# =============================================================================
print(f"\n=== Domain wall vs BCS ===")
print(f"|E_cond| = {abs(E_cond):.6e} M_KK (per cell)")
print(f"E_DW/bond at ds=0.015: {results['E_DW_geom_B'][-1]:.6e} M_KK")
print(f"Ratio E_DW/|E_cond| at ds=0.015: {results['E_DW_geom_B'][-1]/abs(E_cond):.4e}")
print(f"Ratio E_DW/|E_cond| at ds=0.001: {results['E_DW_geom_B'][0]/abs(E_cond):.4e}")
print(f"Total wall E_DW / |E_cond| at ds=0.015: {n_cut * results['E_DW_geom_B'][-1] / abs(E_cond):.4e}")

# =============================================================================
# 10. Gate verdict
# =============================================================================
# Check if E_DW > 0 at all scanned delta_sigma values
E_DW_primary = results['E_DW_geom_B']
all_positive = np.all(E_DW_primary >= -1e-15)  # numerical zero tolerance
max_frac = np.max(np.abs(E_DW_primary)) / EJ_ref_B

gate_name = "OFF-JENSEN-DW-58"
if all_positive:
    gate_verdict = "INFO"
    gate_detail = (
        f"E_DW > 0 at all {len(delta_sigma_all)} scanned delta_sigma values "
        f"(range [{delta_sigma_all[0]:.1e}, {delta_sigma_all[-1]:.4f}]). "
        f"Walls COST energy. E_J convex in sigma at fold (d2E_J/ds2={2*a2_fit:.2e}). "
        f"max E_DW/E_J(0) = {max_frac:.4e}. "
        f"max E_DW/|E_cond| = {np.max(E_DW_primary)/abs(E_cond):.4e}. "
        f"Uniform state stable. Spectral bisection: {n_cut} bonds across cut."
    )
else:
    # Check if mixed sign
    has_neg = np.any(E_DW_primary < -1e-15)
    has_pos = np.any(E_DW_primary > 1e-15)
    if has_neg and has_pos:
        gate_verdict = "INFO"
        gate_detail = (
            f"E_DW has MIXED sign: min={E_DW_primary.min():.4e}, max={E_DW_primary.max():.4e}. "
            f"Domain walls favorable at some delta_sigma, costly at others."
        )
    else:
        gate_verdict = "INFO"
        gate_detail = (
            f"E_DW <= 0 at all delta_sigma: min={E_DW_primary.min():.4e}. "
            f"Domain walls energetically FAVORABLE — spontaneous differentiation. "
            f"Uniform state UNSTABLE to off-Jensen perturbations."
        )

print(f"\n=== GATE VERDICT ===")
print(f"Gate: {gate_name}")
print(f"Verdict: {gate_verdict}")
print(f"Detail: {gate_detail}")

# =============================================================================
# 11. Save output
# =============================================================================
np.savez('computations/session-58/s58_off_jensen_dw.npz',
    # Scan parameters
    delta_sigma_scan=delta_sigma_all,
    tau_fold_used=tau_fold,

    # Per-delta_sigma results (at fold)
    E_DW_geom_B=results['E_DW_geom_B'],
    E_DW_arith_B=results['E_DW_arith_B'],
    E_DW_prod_B=results['E_DW_prod_B'],
    E_DW_geom_A=results['E_DW_geom_A'],
    E_DW_arith_A=results['E_DW_arith_A'],
    E_DW_prod_A=results['E_DW_prod_A'],
    EJ_bond_geom_B=results['EJ_bond_geom_B'],
    EJ_bond_arith_B=results['EJ_bond_arith_B'],
    EJ_bond_prod_B=results['EJ_bond_prod_B'],
    EJ_homo_0_B=results['EJ_homo_0_B'],
    EJ_homo_ds_B=results['EJ_homo_ds_B'],
    EJ_ref_B=EJ_ref_B,
    EJ_ref_A=EJ_ref_A,

    # E_J(sigma) profile at fold
    sig_range=sig_range,
    EJ_fold_profile_B=EJ_fold_B,
    EJ_fold_profile_A=EJ_fold_A,
    d2EJ_dsig2_B=d2EJ_dsig2[mid_idx],
    d2EJ_dsig2_A=d2EJ_dsig2_A[mid_idx],

    # Quadratic fit
    fit_a0=a0_fit,
    fit_a2=a2_fit,
    fit_a4=a4_fit,
    kappa_wall=2*a2_fit,

    # Tau dependence
    tau_scan=tau_scan,
    E_DW_tau_geom=E_DW_tau_geom,
    E_DW_tau_arith=E_DW_tau_arith,
    EJ_homo_tau=EJ_homo_tau,
    ds_fixed=ds_fixed,

    # Graph bisection
    partition=partition,
    n_cut=n_cut,
    cut_types_C2=cut_types['C2'],
    cut_types_su2=cut_types['su2'],
    cut_types_u1=cut_types['u1'],
    fiedler_eigenvalue=eigvals_L[1],
    fiedler_vector=fiedler,

    # Fabric domain wall totals
    E_DW_fabric_0p001=E_DW_fabric.get(0.001, 0.0),
    E_DW_fabric_0p005=E_DW_fabric.get(0.005, 0.0),
    E_DW_fabric_0p010=E_DW_fabric.get(0.010, 0.0),
    E_DW_fabric_0p015=E_DW_fabric.get(0.015, 0.0),

    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)

print(f"\nSaved: computations/session-58/s58_off_jensen_dw.npz")
print("DONE.")
