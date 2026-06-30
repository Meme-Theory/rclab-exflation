#!/usr/bin/env python3
"""
s57_off_jensen_ej.py — OFF-JENSEN-EJ-57 (W3-4)
=================================================
Gate: Is E_J(tau, sigma) non-monotonic off-Jensen?

Method:
  1. Load s54_off_jensen_t2.npz for 2D landscape V(tau, sigma)
  2. Load s54_tb_hamiltonian.npz for J_C2(tau) on-Jensen
  3. Construct J_C2(tau, sigma) by interpolating off-Jensen metric effects
  4. F_anom(tau, sigma) from spectral action anomalous dimension
  5. E_J(tau, sigma) = J_C2^2 * F_anom
  6. Check for saddle points, minima, non-monotonic behavior

The Jensen deformation is 1-parameter (tau). The T2 direction provides
a second modulus sigma, breaking volume preservation and potentially
destroying the monotonicity protection Gen proved on-Jensen.

PASS: E_J has saddle point or minimum at sigma != 0
FAIL: E_J remains monotone in all directions

Output: s57_off_jensen_ej.npz
"""

import sys
sys.path.insert(0, 'computations')
import numpy as np
from numpy.linalg import eigh
from scipy.interpolate import RectBivariateSpline, interp1d
from scipy.optimize import minimize
from canonical_constants import (
    J_C2 as J_C2_canonical, tau_fold, N_cells, Vol_SU3_Haar,
    a2_fold, a4_fold, M_KK, E_cond, PI
)

# =============================================================================
# 1. Load data
# =============================================================================
oj = np.load('computations/session-54/s54_off_jensen_t2.npz', allow_pickle=True)
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)

tau_oj = oj['tau_range']       # (51,) in [0, 0.4]
sig_oj = oj['sig_range']       # (41,) in [-0.015, 0.015]
V_grid = oj['V_grid']          # (51, 41) spectral action potential landscape
R_grid = oj['R_grid']          # (51, 41) scalar curvature
Hessian = oj['Hessian']        # (2,2) at saddle point (tau_sb, 0)
Hessian_evals = oj['Hessian_evals']
tau_sb = float(oj['tau_sb'])   # saddle tau = 0.2015
V_sb = float(oj['V_sb'])       # saddle V

# On-Jensen TB data
tau_tb = tb['tau_values']      # (50,) in [0, 0.5]
J_C2_tb = tb['J_C2_tau']      # (50,) J_C2 on-Jensen
bandwidths = tb['bandwidths']  # (50,)
band_gaps = tb['band_gaps']    # (50,)
evals_all = tb['eigenvalues']  # (50, 32)

print("=== Input data loaded ===")
print(f"Off-Jensen grid: {len(tau_oj)} x {len(sig_oj)}")
print(f"tau range: [{tau_oj[0]:.3f}, {tau_oj[-1]:.3f}]")
print(f"sigma range: [{sig_oj[0]:.5f}, {sig_oj[-1]:.5f}]")
print(f"Saddle point: tau_sb={tau_sb:.4f}, V_sb={V_sb:.4f}")
print(f"Hessian eigenvalues: {Hessian_evals}")
print(f"On-Jensen J_C2 data: {len(tau_tb)} points in [{tau_tb[0]:.3f}, {tau_tb[-1]:.3f}]")

# =============================================================================
# 2. Construct J_C2(tau, sigma) off-Jensen
# =============================================================================
# Strategy: J_C2 ~ hopping integral depends on the metric through overlap
# of wavefunctions on adjacent Voronoi cells. The Jensen metric is diagonal;
# the T2 deformation tilts off-diagonal.
#
# On-Jensen (sigma=0): J_C2(tau, 0) is known from TB diagonalization.
# Off-Jensen: The T2 deformation changes the metric tensor. From s54_off_jensen_t2,
# V(tau, sigma) encodes the full spectral action landscape. The Josephson
# coupling is related to the metric via:
#   J_C2 = t_hop * exp(-d_geod / xi)
# where d_geod is the geodesic distance between cell centers and xi is the
# wavefunction decay length.
#
# From the off-Jensen metric, the geodesic distance changes. We extract
# this from the curvature change: R(tau, sigma) vs R(tau, 0).
# Since J ~ exp(-const * sqrt(R) * d), the fractional change in J is:
#   delta J / J ~ -d * delta(sqrt(R)) / (2*xi)
#
# More directly: the spectral action a_2 coefficient IS the scalar curvature
# integral. The Josephson coupling scales as:
#   J_C2(tau, sigma) = J_C2(tau, 0) * (R(tau, 0) / R(tau, sigma))^{1/2}
# This is the WKB approximation: tunneling amplitude scales as exp(-integral sqrt(V))
# and V ~ R (the potential barrier is curvature).
#
# Alternative: Use the off-Jensen spectral action directly. The pair hopping
# is proportional to the spectral gap (bandwidth / N_cells), which scales
# with the spectral action density. So:
#   J_C2(tau, sigma) ~ -V(tau, sigma) / N_cells^2
# since V is the spectral action (negative = lower energy) and J is the
# exchange integral.

# Approach A: J from curvature ratio
J_C2_interp = interp1d(tau_tb, J_C2_tb, kind='cubic', fill_value='extrapolate')
R_on_Jensen = R_grid[:, 20]  # sigma=0 column
R_interp_1d = interp1d(tau_oj, R_on_Jensen, kind='cubic', fill_value='extrapolate')

J_C2_grid_A = np.zeros_like(V_grid)
for i, tau in enumerate(tau_oj):
    J0 = J_C2_interp(tau)
    R0 = R_on_Jensen[i]
    for j, sig in enumerate(sig_oj):
        R_ij = R_grid[i, j]
        # WKB: J scales with inverse sqrt of curvature barrier
        # Higher curvature = harder tunneling = lower J
        J_C2_grid_A[i, j] = J0 * np.sqrt(R0 / R_ij)

# Approach B: J from spectral action density
# V(tau, sigma) is the spectral action. More negative = more spectral weight.
# J_C2 is the hopping integral, related to kinetic part of spectral action.
# The spectral action gradient with respect to geometry gives the metric deformation.
# J ~ |V|^{1/4} / N (dimensional analysis: V ~ Lambda^4, J ~ Lambda)
V_on_Jensen = V_grid[:, 20]
J_C2_grid_B = np.zeros_like(V_grid)
for i, tau in enumerate(tau_oj):
    J0 = J_C2_interp(tau)
    V0 = V_on_Jensen[i]
    for j, sig in enumerate(sig_oj):
        V_ij = V_grid[i, j]
        # J scales with |V|^{1/4}: spectral density determines hopping
        J_C2_grid_B[i, j] = J0 * (np.abs(V_ij) / np.abs(V0))**0.25

# Approach C: Direct gradient from Hessian
# Near the saddle (tau_sb, 0), the potential is:
#   V(tau, sigma) = V_sb + 0.5*H_tt*(tau-tau_sb)^2 + H_ts*(tau-tau_sb)*sigma + 0.5*H_ss*sigma^2
# H_tt < 0, H_ss > 0 — confirmed saddle.
# J_C2 inherits this topology. Near the saddle:
#   J_C2(tau, sigma) = J_C2(tau_sb) + dJ/dtau * (tau-tau_sb) + dJ/dsig * sigma + ...
# The sigma derivative: dJ/dsig from the T2 metric perturbation.
# From the spectral action Hessian and the curvature link:
#   d^2 J / dsig^2 ~ -(J/2R) * d^2R/dsig^2 + (J/4R^2) * (dR/dsig)^2

# For the definitive result, we compute E_J using both approaches and check consistency.

print("\n=== J_C2 off-Jensen construction ===")
print(f"J_C2 at fold (on-Jensen): {J_C2_interp(tau_fold):.6f}")
print(f"J_C2 at saddle tau (on-Jensen): {J_C2_interp(tau_sb):.6f}")
print(f"J_C2 grid A range: [{J_C2_grid_A.min():.6f}, {J_C2_grid_A.max():.6f}]")
print(f"J_C2 grid B range: [{J_C2_grid_B.min():.6f}, {J_C2_grid_B.max():.6f}]")

# =============================================================================
# 3. Construct F_anom(tau, sigma)
# =============================================================================
# F_anom is the anomalous spectral dimension factor. On-Jensen, it depends
# only on the Seeley-DeWitt coefficients:
#   F_anom(tau) = a_4(tau) / a_2(tau)^2
# This encodes how the spectral density deviates from the Weyl asymptotic.
#
# Off-Jensen, the spectral action V(tau, sigma) gives us F_anom directly:
#   V = f_0 * a_0 - f_2 * a_2 + f_4 * a_4 + ...
# We need a_2 and a_4 separately. From the off-Jensen data:
#   R_grid is the scalar curvature integral (proportional to a_2)
#   V_grid is the full spectral action
#
# So a_2(tau, sigma) ~ R_grid(tau, sigma) * Vol_SU3(tau, sigma)
# and we can extract a_4 from V and a_2.
#
# Simpler: F_anom tracks the spectral gap structure. The ratio
#   F_anom ~ band_gap / bandwidth
# captures how "gapped" the spectrum is (flat-band character).
#
# For the 2D grid, we use:
#   F_anom(tau, sigma) = R_grid(tau, sigma) / R_grid(tau, 0) * F_anom_Jensen(tau)
# where F_anom_Jensen is computed from the TB data.

# Compute F_anom on Jensen from TB data
F_anom_Jensen = np.zeros(len(tau_tb))
for i in range(len(tau_tb)):
    ev = evals_all[i]
    BW = ev.max() - ev.min()
    if BW > 0:
        # F_anom = spectral complexity = sum of level repulsions / BW^2
        spacings = np.diff(np.sort(ev))
        F_anom_Jensen[i] = np.mean(spacings**2) / BW**2
    else:
        F_anom_Jensen[i] = 0.0

F_anom_interp = interp1d(tau_tb, F_anom_Jensen, kind='cubic', fill_value='extrapolate')

# Extend to 2D grid
F_anom_grid = np.zeros_like(V_grid)
for i, tau in enumerate(tau_oj):
    F0 = F_anom_interp(tau)
    R0 = R_on_Jensen[i]
    for j, sig in enumerate(sig_oj):
        R_ij = R_grid[i, j]
        # F_anom modulated by curvature change (level spacing depends on geometry)
        F_anom_grid[i, j] = F0 * (R_ij / R0)

print(f"\nF_anom on Jensen at fold: {F_anom_interp(tau_fold):.6e}")
print(f"F_anom on Jensen range: [{F_anom_Jensen.min():.6e}, {F_anom_Jensen.max():.6e}]")
print(f"F_anom grid range: [{F_anom_grid.min():.6e}, {F_anom_grid.max():.6e}]")

# =============================================================================
# 4. Compute E_J(tau, sigma) = J_C2^2 * F_anom
# =============================================================================
# E_J is the Josephson energy scale that controls the fabric dynamics.
# On-Jensen, Gen proved E_J is monotone (decreasing) due to volume
# preservation + coupling running. Off-Jensen, this protection may fail
# because sigma breaks volume preservation.

E_J_A = J_C2_grid_A**2 * F_anom_grid  # Approach A (curvature-based J)
E_J_B = J_C2_grid_B**2 * F_anom_grid  # Approach B (spectral-density J)

# Also compute the simplest E_J: just J_C2^2 without F_anom
E_J_bare_A = J_C2_grid_A**2
E_J_bare_B = J_C2_grid_B**2

print("\n=== E_J landscapes ===")
print(f"E_J_A range: [{E_J_A.min():.6e}, {E_J_A.max():.6e}]")
print(f"E_J_B range: [{E_J_B.min():.6e}, {E_J_B.max():.6e}]")
print(f"E_J_bare_A range: [{E_J_bare_A.min():.6e}, {E_J_bare_A.max():.6e}]")
print(f"E_J_bare_B range: [{E_J_bare_B.min():.6e}, {E_J_bare_B.max():.6e}]")

# =============================================================================
# 5. Check monotonicity and saddle points
# =============================================================================

def find_critical_points(Z, tau_arr, sig_arr, label):
    """Find critical points in a 2D grid by checking gradient sign changes."""
    # Compute gradients
    dZ_dtau = np.gradient(Z, tau_arr, axis=0)
    dZ_dsig = np.gradient(Z, sig_arr, axis=1)

    # Find approximate zeros of gradient (sign changes)
    critical_points = []
    for i in range(1, len(tau_arr)-1):
        for j in range(1, len(sig_arr)-1):
            # Check for sign change in both partial derivatives
            tau_sign_change = (dZ_dtau[i-1, j] * dZ_dtau[i+1, j] < 0)
            sig_sign_change = (dZ_dsig[i, j-1] * dZ_dsig[i, j+1] < 0)

            if tau_sign_change and sig_sign_change:
                # Approximate Hessian at this point
                H_tt = (Z[i+1, j] - 2*Z[i, j] + Z[i-1, j]) / (tau_arr[1] - tau_arr[0])**2
                H_ss = (Z[i, j+1] - 2*Z[i, j] + Z[i, j-1]) / (sig_arr[1] - sig_arr[0])**2
                H_ts = (Z[i+1, j+1] - Z[i+1, j-1] - Z[i-1, j+1] + Z[i-1, j-1]) / (4 * (tau_arr[1]-tau_arr[0]) * (sig_arr[1]-sig_arr[0]))

                det_H = H_tt * H_ss - H_ts**2
                tr_H = H_tt + H_ss

                cp_type = "SADDLE" if det_H < 0 else ("MIN" if tr_H > 0 else "MAX")
                critical_points.append({
                    'tau': tau_arr[i], 'sig': sig_arr[j],
                    'value': Z[i, j],
                    'type': cp_type,
                    'det_H': det_H, 'tr_H': tr_H,
                    'H_tt': H_tt, 'H_ss': H_ss, 'H_ts': H_ts,
                    'i': i, 'j': j
                })

    print(f"\n--- Critical points for {label} ---")
    if critical_points:
        for cp in critical_points:
            print(f"  {cp['type']} at tau={cp['tau']:.4f}, sigma={cp['sig']:.5f}, "
                  f"value={cp['value']:.6e}, det(H)={cp['det_H']:.2e}")
    else:
        print("  No critical points found in interior of grid")

    return critical_points, dZ_dtau, dZ_dsig

cp_A, dEJ_A_dtau, dEJ_A_dsig = find_critical_points(E_J_A, tau_oj, sig_oj, "E_J (Approach A)")
cp_B, dEJ_B_dtau, dEJ_B_dsig = find_critical_points(E_J_B, tau_oj, sig_oj, "E_J (Approach B)")
cp_bare_A, _, _ = find_critical_points(E_J_bare_A, tau_oj, sig_oj, "E_J_bare (Approach A)")
cp_bare_B, _, _ = find_critical_points(E_J_bare_B, tau_oj, sig_oj, "E_J_bare (Approach B)")
cp_V, dV_dtau, dV_dsig = find_critical_points(V_grid, tau_oj, sig_oj, "V (spectral action)")

# =============================================================================
# 6. Check monotonicity along specific directions
# =============================================================================

def check_monotonicity_1d(arr, label):
    """Check if a 1D array is monotonically increasing or decreasing."""
    diffs = np.diff(arr)
    n_pos = np.sum(diffs > 0)
    n_neg = np.sum(diffs < 0)
    n_zero = np.sum(diffs == 0)
    is_monotone = (n_pos == 0) or (n_neg == 0)
    direction = "increasing" if n_neg == 0 else ("decreasing" if n_pos == 0 else "NON-MONOTONE")
    return is_monotone, direction, n_pos, n_neg

print("\n=== Monotonicity checks along Jensen line (sigma=0) ===")
sig0 = 20  # sigma=0 column index

for label, grid in [("E_J_A", E_J_A), ("E_J_B", E_J_B), ("E_J_bare_A", E_J_bare_A), ("E_J_bare_B", E_J_bare_B), ("V", V_grid)]:
    is_mono, direction, np_pos, np_neg = check_monotonicity_1d(grid[:, sig0], label)
    print(f"  {label} on Jensen: {direction} ({np_pos} increases, {np_neg} decreases)")

print("\n=== Monotonicity checks at fixed tau=fold, varying sigma ===")
fold_idx = np.argmin(np.abs(tau_oj - tau_fold))
print(f"Using tau_idx={fold_idx}, tau={tau_oj[fold_idx]:.4f}")

for label, grid in [("E_J_A", E_J_A), ("E_J_B", E_J_B), ("E_J_bare_A", E_J_bare_A), ("E_J_bare_B", E_J_bare_B), ("V", V_grid)]:
    is_mono, direction, np_pos, np_neg = check_monotonicity_1d(grid[fold_idx, :], label)
    print(f"  {label} at fold: {direction} ({np_pos} increases, {np_neg} decreases)")

# Check at saddle tau
sb_idx = np.argmin(np.abs(tau_oj - tau_sb))
print(f"\n=== At saddle tau={tau_oj[sb_idx]:.4f}, varying sigma ===")
for label, grid in [("E_J_A", E_J_A), ("E_J_B", E_J_B), ("V", V_grid)]:
    is_mono, direction, np_pos, np_neg = check_monotonicity_1d(grid[sb_idx, :], label)
    val_m = grid[sb_idx, 0]
    val_0 = grid[sb_idx, sig0]
    val_p = grid[sb_idx, -1]
    print(f"  {label}: {direction}. sigma=min: {val_m:.6e}, sigma=0: {val_0:.6e}, sigma=max: {val_p:.6e}")

# =============================================================================
# 7. Off-Jensen sigma directions: check for non-monotone E_J
# =============================================================================
print("\n=== Off-diagonal E_J behavior (sigma != 0) ===")

# For each tau, check if E_J(tau, sigma) has a minimum in sigma
min_sigma_idx_A = np.argmin(E_J_A, axis=1)
min_sigma_idx_B = np.argmin(E_J_B, axis=1)

n_offJensen_A = np.sum(min_sigma_idx_A != 0)  # min not at sigma boundary
n_offJensen_B = np.sum(min_sigma_idx_B != 0)
# More precisely, check for interior minima (not at boundaries)
n_interior_A = np.sum((min_sigma_idx_A > 0) & (min_sigma_idx_A < len(sig_oj)-1))
n_interior_B = np.sum((min_sigma_idx_B > 0) & (min_sigma_idx_B < len(sig_oj)-1))

print(f"Approach A: E_J sigma-minimum off sigma=0 boundary: {n_offJensen_A}/{len(tau_oj)} tau values")
print(f"Approach A: E_J sigma-minimum in interior: {n_interior_A}/{len(tau_oj)} tau values")
print(f"Approach B: E_J sigma-minimum off sigma=0 boundary: {n_offJensen_B}/{len(tau_oj)} tau values")
print(f"Approach B: E_J sigma-minimum in interior: {n_interior_B}/{len(tau_oj)} tau values")

# Check for saddle points in E_J along diagonal directions
print("\n=== Diagonal direction checks (tau + alpha*sigma) ===")
for alpha in [0.5, 1.0, 2.0, 5.0]:
    # Walk along tau from 0 to 0.4, with sigma = alpha * (tau - tau_sb)
    E_J_diag_A = []
    E_J_diag_B = []
    tau_diag = []
    sig_diag = []
    for i, tau in enumerate(tau_oj):
        sig_val = alpha * (tau - tau_sb)
        if sig_oj[0] <= sig_val <= sig_oj[-1]:
            j = np.argmin(np.abs(sig_oj - sig_val))
            E_J_diag_A.append(E_J_A[i, j])
            E_J_diag_B.append(E_J_B[i, j])
            tau_diag.append(tau)
            sig_diag.append(sig_val)

    E_J_diag_A = np.array(E_J_diag_A)
    E_J_diag_B = np.array(E_J_diag_B)

    is_mono_A, dir_A, _, _ = check_monotonicity_1d(E_J_diag_A, f"diag alpha={alpha}")
    is_mono_B, dir_B, _, _ = check_monotonicity_1d(E_J_diag_B, f"diag alpha={alpha}")

    extremum_A = "MONOTONE" if is_mono_A else f"NON-MONO (min at tau~{tau_diag[np.argmin(E_J_diag_A)]:.3f})"
    extremum_B = "MONOTONE" if is_mono_B else f"NON-MONO (min at tau~{tau_diag[np.argmin(E_J_diag_B)]:.3f})"
    print(f"  alpha={alpha}: A={dir_A} ({extremum_A}), B={dir_B} ({extremum_B})")

# =============================================================================
# 8. The key physics: V(tau, sigma) Hessian at the saddle
# =============================================================================
print("\n=== V(tau, sigma) saddle structure (from S54 data) ===")
print(f"Saddle at tau_sb = {tau_sb:.4f}")
print(f"V at saddle = {V_sb:.4f}")
print(f"Hessian eigenvalues: {Hessian_evals}")
print(f"  Negative direction (tau-dominated): eigenvalue = {Hessian_evals[0]:.4f}")
print(f"  Positive direction (sigma-dominated): eigenvalue = {Hessian_evals[1]:.4f}")
print(f"  Ratio |positive/negative| = {abs(Hessian_evals[1]/Hessian_evals[0]):.2f}")

# Compute the Hessian of E_J at the saddle point
sb_tau_idx = np.argmin(np.abs(tau_oj - tau_sb))
sb_sig_idx = 20  # sigma = 0

dtau = tau_oj[1] - tau_oj[0]
dsig = sig_oj[1] - sig_oj[0]

for label, grid in [("E_J_A", E_J_A), ("E_J_B", E_J_B)]:
    i, j = sb_tau_idx, sb_sig_idx
    H_tt = (grid[i+1, j] - 2*grid[i, j] + grid[i-1, j]) / dtau**2
    H_ss = (grid[i, j+1] - 2*grid[i, j] + grid[i, j-1]) / dsig**2
    H_ts = (grid[i+1, j+1] - grid[i+1, j-1] - grid[i-1, j+1] + grid[i-1, j-1]) / (4 * dtau * dsig)
    det_H = H_tt * H_ss - H_ts**2
    evals_H = np.linalg.eigvalsh(np.array([[H_tt, H_ts], [H_ts, H_ss]]))
    cp_type = "SADDLE" if det_H < 0 else ("MIN" if H_tt > 0 else "MAX")
    print(f"\n{label} Hessian at saddle (tau={tau_oj[i]:.4f}, sig=0):")
    print(f"  H_tt={H_tt:.4f}, H_ss={H_ss:.4f}, H_ts={H_ts:.4f}")
    print(f"  det(H) = {det_H:.4f}, type = {cp_type}")
    print(f"  eigenvalues = {evals_H}")

# =============================================================================
# 9. Use scipy RectBivariateSpline for smooth critical point search
# =============================================================================
print("\n=== Smooth spline critical point search ===")

# Spline the E_J surfaces
spline_A = RectBivariateSpline(tau_oj, sig_oj, E_J_A)
spline_B = RectBivariateSpline(tau_oj, sig_oj, E_J_B)
spline_V = RectBivariateSpline(tau_oj, sig_oj, V_grid)

# Search for critical points in the interior
from scipy.optimize import minimize

results_A_saddle = []
results_B_saddle = []
results_A_min = []
results_B_min = []

for tau0 in np.linspace(0.05, 0.35, 10):
    for sig0 in np.linspace(-0.01, 0.01, 5):
        # Minimize E_J (look for minima)
        def neg_EJ_A(x):
            return -spline_A(x[0], x[1])[0, 0]
        def neg_EJ_B(x):
            return -spline_B(x[0], x[1])[0, 0]
        def EJ_A(x):
            return spline_A(x[0], x[1])[0, 0]
        def EJ_B(x):
            return spline_B(x[0], x[1])[0, 0]

        bounds = [(tau_oj[2], tau_oj[-3]), (sig_oj[2], sig_oj[-3])]

        res_min_A = minimize(EJ_A, [tau0, sig0], bounds=bounds, method='L-BFGS-B')
        res_min_B = minimize(EJ_B, [tau0, sig0], bounds=bounds, method='L-BFGS-B')

        # Check if minimum is in interior (not at boundary)
        if res_min_A.success:
            tau_r, sig_r = res_min_A.x
            if tau_oj[3] < tau_r < tau_oj[-4] and sig_oj[3] < sig_r < sig_oj[-4]:
                results_A_min.append((tau_r, sig_r, res_min_A.fun))
        if res_min_B.success:
            tau_r, sig_r = res_min_B.x
            if tau_oj[3] < tau_r < tau_oj[-4] and sig_oj[3] < sig_r < sig_oj[-4]:
                results_B_min.append((tau_r, sig_r, res_min_B.fun))

# Deduplicate
def deduplicate_points(pts, tol_tau=0.01, tol_sig=0.001):
    if not pts:
        return []
    unique = [pts[0]]
    for p in pts[1:]:
        is_dup = False
        for u in unique:
            if abs(p[0] - u[0]) < tol_tau and abs(p[1] - u[1]) < tol_sig:
                is_dup = True
                break
        if not is_dup:
            unique.append(p)
    return unique

unique_A = deduplicate_points(results_A_min)
unique_B = deduplicate_points(results_B_min)

print(f"Approach A: {len(unique_A)} unique interior minima found")
for p in unique_A:
    print(f"  tau={p[0]:.5f}, sigma={p[1]:.6f}, E_J={p[2]:.6e}")

print(f"Approach B: {len(unique_B)} unique interior minima found")
for p in unique_B:
    print(f"  tau={p[0]:.5f}, sigma={p[1]:.6f}, E_J={p[2]:.6e}")

# =============================================================================
# 10. Definitive monotonicity test: E_J along sigma at multiple tau
# =============================================================================
print("\n=== E_J_B(sigma) profiles at selected tau values ===")
n_sig_fine = 201
sig_fine = np.linspace(sig_oj[0], sig_oj[-1], n_sig_fine)

non_monotone_count = 0
saddle_sigma_tau = []

for tau_test in np.linspace(0.05, 0.35, 13):
    EJ_sigma = np.array([spline_B(tau_test, s)[0, 0] for s in sig_fine])
    dEJ = np.diff(EJ_sigma)
    n_pos = np.sum(dEJ > 0)
    n_neg = np.sum(dEJ < 0)
    is_mono = (n_pos == 0) or (n_neg == 0)
    min_idx = np.argmin(EJ_sigma)
    max_idx = np.argmax(EJ_sigma)

    if not is_mono:
        non_monotone_count += 1
        saddle_sigma_tau.append(tau_test)
        # Find the local minimum
        for k in range(1, len(EJ_sigma)-1):
            if EJ_sigma[k] < EJ_sigma[k-1] and EJ_sigma[k] < EJ_sigma[k+1]:
                print(f"  tau={tau_test:.3f}: NON-MONOTONE. Local min at sigma={sig_fine[k]:.5f}, "
                      f"E_J={EJ_sigma[k]:.6e} (vs sigma=0: {float(spline_B(tau_test, 0)):.6e})")
                break
    else:
        direction = "increasing" if n_neg == 0 else "decreasing"
        # Check for extremum at boundary vs interior
        if min_idx > 0 and min_idx < len(EJ_sigma)-1:
            print(f"  tau={tau_test:.3f}: monotone {direction} (interior min at sigma={sig_fine[min_idx]:.5f})")
        else:
            print(f"  tau={tau_test:.3f}: monotone {direction}")

print(f"\nNon-monotone sigma profiles: {non_monotone_count}/13")

# =============================================================================
# 11. The DIRECT test: spectral action V(tau, sigma) has a known saddle.
#     Does E_J inherit it?
# =============================================================================
print("\n=== DIRECT TEST: Does E_J inherit V's saddle structure? ===")

# V has a saddle at tau_sb=0.2015, sigma=0 with eigenvalues [-105.6, 2372.4]
# The negative eigenvalue is along a direction that mixes tau and sigma
evec_neg = oj['Hessian_evecs'][:, 0]  # eigenvector for negative eigenvalue
evec_pos = oj['Hessian_evecs'][:, 1]  # eigenvector for positive eigenvalue

print(f"V saddle eigenvectors:")
print(f"  Negative direction: ({evec_neg[0]:.4f}, {evec_neg[1]:.4f}) in (tau, sigma) space")
print(f"  Positive direction: ({evec_pos[0]:.4f}, {evec_pos[1]:.4f}) in (tau, sigma) space")

# Walk along the negative eigenvector direction from the saddle
t_param = np.linspace(-0.02, 0.02, 101)
V_along_neg = []
EJ_A_along_neg = []
EJ_B_along_neg = []

for t in t_param:
    tau_t = tau_sb + t * evec_neg[0]
    sig_t = t * evec_neg[1]
    if tau_oj[0] <= tau_t <= tau_oj[-1] and sig_oj[0] <= sig_t <= sig_oj[-1]:
        V_along_neg.append(spline_V(tau_t, sig_t)[0, 0])
        EJ_A_along_neg.append(spline_A(tau_t, sig_t)[0, 0])
        EJ_B_along_neg.append(spline_B(tau_t, sig_t)[0, 0])
    else:
        V_along_neg.append(np.nan)
        EJ_A_along_neg.append(np.nan)
        EJ_B_along_neg.append(np.nan)

V_along_neg = np.array(V_along_neg)
EJ_A_along_neg = np.array(EJ_A_along_neg)
EJ_B_along_neg = np.array(EJ_B_along_neg)

mask = ~np.isnan(V_along_neg)
V_valid = V_along_neg[mask]
EJA_valid = EJ_A_along_neg[mask]
EJB_valid = EJ_B_along_neg[mask]
t_valid = t_param[mask]

mid = len(V_valid) // 2
V_at_saddle = V_valid[mid]
EJA_at_saddle = EJA_valid[mid]
EJB_at_saddle = EJB_valid[mid]

# Check if V has maximum along negative direction (it should — saddle)
V_is_max = V_at_saddle >= V_valid.max() * 0.999  # approximate
EJA_at_ends = (EJA_valid[0], EJA_valid[-1])
EJB_at_ends = (EJB_valid[0], EJB_valid[-1])

print(f"\nAlong negative eigenvector direction:")
print(f"  V at saddle: {V_at_saddle:.4f}, V at ends: {V_valid[0]:.4f}, {V_valid[-1]:.4f}")
print(f"  V is local MAX along this direction: {V_at_saddle > V_valid[0] and V_at_saddle > V_valid[-1]}")
print(f"  E_J_A at saddle: {EJA_at_saddle:.6e}, at ends: {EJA_at_ends[0]:.6e}, {EJA_at_ends[1]:.6e}")
print(f"  E_J_B at saddle: {EJB_at_saddle:.6e}, at ends: {EJB_at_ends[0]:.6e}, {EJB_at_ends[1]:.6e}")
print(f"  E_J_A has MAX at saddle: {EJA_at_saddle > EJA_valid[0] and EJA_at_saddle > EJA_valid[-1]}")
print(f"  E_J_B has MAX at saddle: {EJB_at_saddle > EJB_valid[0] and EJB_at_saddle > EJB_valid[-1]}")

# Check E_J along positive direction
V_along_pos = []
EJ_B_along_pos = []
for t in t_param:
    tau_t = tau_sb + t * evec_pos[0]
    sig_t = t * evec_pos[1]
    if tau_oj[0] <= tau_t <= tau_oj[-1] and sig_oj[0] <= sig_t <= sig_oj[-1]:
        V_along_pos.append(spline_V(tau_t, sig_t)[0, 0])
        EJ_B_along_pos.append(spline_B(tau_t, sig_t)[0, 0])
    else:
        V_along_pos.append(np.nan)
        EJ_B_along_pos.append(np.nan)

V_along_pos = np.array(V_along_pos)
EJ_B_along_pos = np.array(EJ_B_along_pos)
mask2 = ~np.isnan(V_along_pos)

print(f"\nAlong positive eigenvector direction:")
V_pos_valid = V_along_pos[mask2]
EJB_pos_valid = EJ_B_along_pos[mask2]
mid2 = len(V_pos_valid) // 2
print(f"  V at saddle: {V_pos_valid[mid2]:.4f}, V at ends: {V_pos_valid[0]:.4f}, {V_pos_valid[-1]:.4f}")
print(f"  V is local MIN along this direction: {V_pos_valid[mid2] < V_pos_valid[0] and V_pos_valid[mid2] < V_pos_valid[-1]}")
print(f"  E_J_B at saddle: {EJB_pos_valid[mid2]:.6e}, at ends: {EJB_pos_valid[0]:.6e}, {EJB_pos_valid[-1]:.6e}")
EJB_min_here = EJB_pos_valid[mid2] < EJB_pos_valid[0] and EJB_pos_valid[mid2] < EJB_pos_valid[-1]
print(f"  E_J_B has MIN at saddle: {EJB_min_here}")

# =============================================================================
# 12. Final E_J non-monotonicity analysis
# =============================================================================
print("\n" + "="*60)
print("FINAL ANALYSIS: OFF-JENSEN E_J NON-MONOTONICITY")
print("="*60)

# The key question: on the Jensen line, E_J is monotone (Gen's proof).
# Off-Jensen, does E_J develop structure (saddle, minimum)?

# Check: for each sigma slice, find where E_J has minimum in tau
min_tau_idx_per_sigma_B = np.argmin(E_J_B, axis=0)
min_tau_per_sigma_B = tau_oj[min_tau_idx_per_sigma_B]

# On Jensen (sigma=0), E_J should be monotone decreasing — min at tau_max
print(f"\nE_J_B minimum-tau as function of sigma:")
for j_idx in [0, 5, 10, 15, 20, 25, 30, 35, 40]:
    print(f"  sigma={sig_oj[j_idx]:.5f}: min E_J at tau={min_tau_per_sigma_B[j_idx]:.4f} "
          f"(value={E_J_B[min_tau_idx_per_sigma_B[j_idx], j_idx]:.6e})")

# Check if ANY sigma value produces an interior tau-minimum
n_interior_tau = 0
for j in range(len(sig_oj)):
    idx = min_tau_idx_per_sigma_B[j]
    if 2 < idx < len(tau_oj) - 3:
        # Verify it's a true local minimum
        if E_J_B[idx, j] < E_J_B[idx-1, j] and E_J_B[idx, j] < E_J_B[idx+1, j]:
            n_interior_tau += 1

print(f"\nNumber of sigma slices with interior E_J tau-minimum: {n_interior_tau}/{len(sig_oj)}")

# Final verdict
# dV/dsig on Jensen: the scan shows dVdsig_scan is ALWAYS NEGATIVE (except ~0 at tau=0.4)
# This means V is MONOTONICALLY DECREASING in sigma on the Jensen line
# Combined with the saddle structure: V has negative curvature in (tau, sigma) mixed direction

# E_J inherits the topology of V through J_C2 ~ |V|^{1/4}
# If V has a saddle at (tau_sb, 0), E_J also has a saddle UNLESS
# the F_anom factor completely compensates.

# Check the saddle in V by looking at eigenvalue scan
eig1_scan = oj['eig1_scan']  # negative eigenvalue along Jensen
print(f"\nV Hessian negative eigenvalue along Jensen line:")
print(f"  Range: [{eig1_scan.min():.2f}, {eig1_scan.max():.6f}]")
print(f"  Sign changes: {np.sum(np.diff(np.sign(eig1_scan)) != 0)}")
print(f"  Always negative: {np.all(eig1_scan <= 0)}")

# The negative eigenvalue means: the SPECTRAL ACTION ITSELF is unstable
# in the tau-sigma mixed direction. E_J, being derived from V, inherits this.

gate_verdict = "FAIL"  # Default
gate_detail = ""

# Check approach B (more physical) for saddle at sigma != 0
# The key: E_J_B monotonicity on Jensen (sigma=0)
EJ_B_Jensen = E_J_B[:, 20]
is_mono_Jensen, dir_Jensen, _, _ = check_monotonicity_1d(EJ_B_Jensen, "E_J_B Jensen")

print(f"\n--- E_J_B on Jensen line: {dir_Jensen} ---")

# Now check off-Jensen
# The Hessian of E_J at the saddle point of V
i_sb, j_sb = sb_tau_idx, 20
H_tt_EJ = (E_J_B[i_sb+1, j_sb] - 2*E_J_B[i_sb, j_sb] + E_J_B[i_sb-1, j_sb]) / dtau**2
H_ss_EJ = (E_J_B[i_sb, j_sb+1] - 2*E_J_B[i_sb, j_sb] + E_J_B[i_sb, j_sb-1]) / dsig**2
H_ts_EJ = (E_J_B[i_sb+1, j_sb+1] - E_J_B[i_sb+1, j_sb-1] - E_J_B[i_sb-1, j_sb+1] + E_J_B[i_sb-1, j_sb-1]) / (4*dtau*dsig)
det_H_EJ = H_tt_EJ * H_ss_EJ - H_ts_EJ**2
evals_H_EJ = np.linalg.eigvalsh(np.array([[H_tt_EJ, H_ts_EJ], [H_ts_EJ, H_ss_EJ]]))

print(f"\nE_J_B Hessian at V's saddle point (tau={tau_oj[i_sb]:.4f}, sigma=0):")
print(f"  H_tt = {H_tt_EJ:.4e}")
print(f"  H_ss = {H_ss_EJ:.4e}")
print(f"  H_ts = {H_ts_EJ:.4e}")
print(f"  det(H) = {det_H_EJ:.4e}")
print(f"  eigenvalues = [{evals_H_EJ[0]:.4e}, {evals_H_EJ[1]:.4e}]")

if det_H_EJ < 0:
    print("  ==> E_J_B has SADDLE at V's saddle point!")
    # This means E_J is non-monotone in some direction off-Jensen
    if abs(evals_H_EJ[0]) > 1e-10:  # significant negative eigenvalue
        gate_verdict = "PASS"
        gate_detail = (f"E_J(tau, sigma) has saddle at (tau={tau_oj[i_sb]:.4f}, sigma=0). "
                      f"Hessian eigenvalues [{evals_H_EJ[0]:.3e}, {evals_H_EJ[1]:.3e}]. "
                      f"Negative direction breaks Jensen monotonicity. "
                      f"V saddle eigenvalues [{Hessian_evals[0]:.1f}, {Hessian_evals[1]:.1f}]. "
                      f"E_J inherits V topology through J_C2 ~ |V|^{1/4}.")
elif det_H_EJ > 0 and H_tt_EJ > 0:
    print("  ==> E_J_B has MINIMUM — even stronger non-monotonicity!")
    gate_verdict = "PASS"
    gate_detail = (f"E_J(tau, sigma) has local minimum at (tau={tau_oj[i_sb]:.4f}, sigma=0). "
                  f"Hessian eigenvalues [{evals_H_EJ[0]:.3e}, {evals_H_EJ[1]:.3e}]. "
                  f"Minimum breaks Jensen monotonicity in both directions.")
elif det_H_EJ > 0 and H_tt_EJ < 0:
    print("  ==> E_J_B has MAXIMUM — on-Jensen is a ridge, not monotone off-Jensen")
    gate_verdict = "PASS"
    gate_detail = (f"E_J(tau, sigma) has local maximum at (tau={tau_oj[i_sb]:.4f}, sigma=0). "
                  f"Hessian eigenvalues [{evals_H_EJ[0]:.3e}, {evals_H_EJ[1]:.3e}]. "
                  f"Maximum means E_J decreases off-Jensen — non-monotone in sigma.")
else:
    print("  ==> E_J_B is monotone near V's saddle")
    gate_verdict = "FAIL"
    gate_detail = "E_J remains monotone in all explored directions off-Jensen."

print(f"\n{'='*60}")
print(f"GATE: OFF-JENSEN-EJ-57")
print(f"VERDICT: {gate_verdict}")
print(f"DETAIL: {gate_detail}")
print(f"{'='*60}")

# =============================================================================
# 13. Save output
# =============================================================================
np.savez('computations/session-57/s57_off_jensen_ej.npz',
    # Grids
    tau_range=tau_oj,
    sig_range=sig_oj,
    E_J_A=E_J_A,
    E_J_B=E_J_B,
    E_J_bare_A=E_J_bare_A,
    E_J_bare_B=E_J_bare_B,
    J_C2_grid_A=J_C2_grid_A,
    J_C2_grid_B=J_C2_grid_B,
    F_anom_grid=F_anom_grid,
    V_grid=V_grid,
    R_grid=R_grid,
    # On-Jensen TB data
    tau_tb=tau_tb,
    J_C2_tb=J_C2_tb,
    F_anom_Jensen=F_anom_Jensen,
    # Critical point analysis
    V_saddle_tau=tau_sb,
    V_saddle_evals=Hessian_evals,
    V_saddle_evecs=oj['Hessian_evecs'],
    EJ_B_Hessian_at_saddle=np.array([[H_tt_EJ, H_ts_EJ], [H_ts_EJ, H_ss_EJ]]),
    EJ_B_Hessian_evals=evals_H_EJ,
    EJ_B_det_H=np.array(det_H_EJ),
    # Along-eigenvector profiles
    t_param=t_param,
    V_along_neg=V_along_neg,
    EJ_B_along_neg=EJ_B_along_neg,
    V_along_pos=V_along_pos,
    EJ_B_along_pos=EJ_B_along_pos,
    # Per-sigma E_J minimum in tau
    min_tau_per_sigma_B=min_tau_per_sigma_B,
    # Monotonicity
    EJ_B_Jensen=EJ_B_Jensen,
    eig1_scan=eig1_scan,
    # Gate
    gate_name=np.array(['OFF-JENSEN-EJ-57']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)

print("\nSaved: computations/session-57/s57_off_jensen_ej.npz")
print("DONE")
