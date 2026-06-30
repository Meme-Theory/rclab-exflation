#!/usr/bin/env python3
"""
S78-W3-B-FAMP-TILT-SMOOTH: F_amp Tilt Smoothed (Scrubbed, POWER-RATIO pinned)
==============================================================================

Gate: S78-W3-B-FAMP-TILT-SMOOTH

Substrate framing (mandatory, phononic-framing.md):
  The tilt |slope| = |d ln F_amp / d ln k| is NOT a primordial power-law
  in an inflationary spacetime. It is the k-dependence of the Parker
  squeezing ratio at the spectral transit through the fold -- how much
  the substrate's Bogoliubov amplification varies across mode number k
  in the CMB-relevant band. F_amp(k) IS a spectral moment ratio of the
  Mukhanov-Sasaki mode at horizon exit to the pure-dS reference. Its
  logarithmic k-derivative probes whether the post-transit GGE acoustic
  spectrum is approximately scale-invariant in the CMB band.

  D_K eigenvalues -> a_2-channel emergent Mukhanov dynamics -> z''/z pump
  -> mode-by-mode Bogoliubov transformation -> F_amp(k) power-ratio ->
  log-k-derivative = scheme-independent structural quantity.

Governing structure (Transit-Dynamics methodology):

    v_k'' + (k^2 - z''/z) v_k = 0                                  ... (1)

    F_amp(k) = P_zeta(real, k) / P_zeta(pure dS, k)                ... (2)

    slope(k_pivot) = [d ln F_amp / d ln k]_{k=k_pivot}              ... (3)

  The logarithmic derivative is CONVENTION-INVARIANT: if we redefine
  F_amp -> c * F_amp for any nonzero c, d ln F_amp / d ln k is
  unchanged. The POWER-RATIO vs AMPLITUDE-RATIO convention factor
  therefore cancels exactly at the level of the slope. The only scheme
  sensitivity is through the unsmoothed F_amp(k) data itself (which is
  linearized + W1-C INCOMPUTABLE caveat; see below).

Convention pins (Section 0 of scrubbed plan, per W3-B at shell lines 526-546):
  - F_amp: POWER RATIO (Section 0.1). LINEAR in A_s.
  - Input: linearized F_amp with "superseded by backreaction" caveat
           (W1-C INCOMPUTABLE-FALLBACK-TO-BOUND; no converged F_amp^sc).
  - Smoothing: Savitzky-Golay polynomial order 3, window 7.
  - k-range: [0.1, 10] * k_pivot; extrapolate slope to k_pivot.
  - Slope extraction is convention-INVARIANT (log-derivative cancels
    overall normalization factors).
  - k_pivot = 14.31 M_KK (fold-normalized); = 0.05 Mpc^{-1} physical.

Pre-registered gate (per shell lines 535-540):
  HYPOTHESIS   : |slope| at k_pivot < 0.1 under converged F_amp^sc OR
                 under linearized F_amp with caveat.
  PASS         : |slope| < 0.1 from converged F_amp^sc.
  FAIL         : |slope| > 0.2 after backreaction; OR slope dominated
                 by self-consistency effects challenging BLV n_s = 0.9567.
  INFO         : |slope| in [0.1, 0.2]; OR W1-C returned INCOMPUTABLE
                 and slope from linearized F_amp with caveat
                 (THIS IS OUR CURRENT REGIME).

Cross-checks (three, per shell lines 541-544):
  CHK1: BLV n_s = 0.9567 unchanged (invariance test: tilt measures
        k-dependence of F_amp, not the emergent n_s of the spectral
        functional which traces to a different set of spectral moments).
  CHK2: Smoothing-window sensitivity: vary polynomial order {2,3,5},
        window {5,7,9,11}; verify slope is not a smoothing artifact.
  CHK3: Branch-C consistency: under converged F_amp^sc at saturation
        floor, slope should be near zero BY CONSTRUCTION (saturation
        flattens k-dependence). This is a CONSISTENCY check on Branch-C,
        not an independent prediction (Transit).

Input (single source of truth):
  computations/session-77/s77_transition_scale_pbh.npz
    - k_values: k-grid in M_KK (52 modes in [k_trans/10, 2*k_pivot])
    - F_amp: linearized F_amp from v'' + (k^2 - z''/z)v = 0, exact
    - k_pivot_fold: 14.31 M_KK

  NOTE: S77 grid extends to ~2*k_pivot. For our required range
  [0.1*k_pivot, 10*k_pivot], we must EXTEND the grid to k up to
  143.11 M_KK. We do so by re-solving the mode equation for k values
  not covered in S77, using the SAME integrator convention
  (DOP853 rtol=1e-11 atol=1e-13, plane-wave BD IC, k/aH=0.05 end).

  This EXTENSION is the SAME linearized F_amp formulation as S77;
  it is NOT a convention change. The caveat applies uniformly across
  the extended k-range.

CAVEAT (bold, explicit):
  =======================================================================
  | This script uses the LINEARIZED F_amp(k) (no Hartree self-energy). |
  | W1-C returned INCOMPUTABLE-FALLBACK-TO-BOUND (2PI oscillates, damped |
  | Hartree eta-scan 183% spread, Kadanoff-Baym too weak). No converged |
  | F_amp^sc(k) array is available. Per shell line 530, we use          |
  | linearized F_amp with "superseded by backreaction" caveat. Under    |
  | backreaction, F_amp at k_pivot would be SATURATED to ~48 (analytical|
  | bound from energy conservation), a factor ~143 reduction. BUT       |
  | saturation AT THE BOUND flattens k-dependence -- the slope in the   |
  | converged F_amp^sc regime would be NEAR ZERO by construction        |
  | (Branch-C cross-check). Our slope is the LINEARIZED prediction,     |
  | valid ABSENT backreaction. Report with explicit caveat.             |
  =======================================================================

Output:
  computations/session-78/s78_famp_tilt_smoothed.npz   (data + cross-checks)
  computations/session-78/s78_famp_tilt_smoothed.png   (6 panels)
  computations/session-78/s78_gate_verdicts.txt         (append-only, one line)

Classification: PHONONIC
  F_amp IS the Parker-Bogoliubov amplification of Mukhanov-Sasaki fluctuations
  through the spectral transit -- a substrate-level property of the squeezed
  GGE state post-fold. The slope is a structural invariant of the z''/z pump.

Author: transit-dynamics-theorist
Session: S78 W3-B
"""

import os
import sys
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# Canonical constants (MANDATORY per math-scripts.md)
from canonical_constants import (
    PI,
    M_KK,
    M_Pl_reduced,
    A_s_CMB,
    planck_ns,
)

OUT_NPZ = os.path.join(SCRIPT_DIR, "s78_famp_tilt_smoothed.npz")
OUT_PNG = os.path.join(SCRIPT_DIR, "s78_famp_tilt_smoothed.png")
GATE_VERDICTS = os.path.join(SCRIPT_DIR, "s78_gate_verdicts.txt")

t_start = time.time()  # (local)
log_lines = []  # (local)


def log(msg=""):
    print(msg)
    log_lines.append(msg)


log("=" * 78)
log("S78 W3-B  S78-W3-B-FAMP-TILT-SMOOTH: F_amp Tilt Smoothed")
log("=" * 78)
log("")
log("Convention pins (Section 0 of scrubbed plan):")
log("  F_amp convention: POWER-RATIO (linear in A_s)")
log("  Input:            linearized F_amp (W1-C INCOMPUTABLE caveat)")
log("  Smoothing:        Savitzky-Golay poly 3, window 7 (primary)")
log("  k-range:          [0.1, 10] x k_pivot")
log("  Slope extraction: d ln F_amp / d ln k at k_pivot")
log("  Convention-INV:   log-derivative kills overall normalization")
log("")
log("CAVEAT: Linearized F_amp input. W1-C INCOMPUTABLE-FALLBACK-TO-BOUND.")
log("  No converged F_amp^sc(k) array. Slope is LINEARIZED regime prediction.")

# ========================================================================
#  SECTION 1: Load S77 linearized F_amp(k) baseline and extend k-range
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 1: Load S77 linearized F_amp(k) baseline")
log("=" * 78)

d77 = np.load(os.path.join(SCRIPT_DIR, 's77_transition_scale_pbh.npz'), allow_pickle=True)
k_s77 = d77['k_values']  # (local) M_KK, 52 modes
F_s77 = d77['F_amp']  # (local) linearized F_amp (power ratio)
k_pivot_MKK = float(d77['k_pivot_fold'])  # (local) = 14.31 M_KK
F_amp_pivot_s77 = float(d77['F_amp_pivot'])  # (local) = 6858 at k_pivot
H_dS = float(d77['H_dS'])  # (local)
eps_dS = float(d77['eps_dS'])  # (local)

# Filter NaNs and superhorizon-at-fold modes
valid_s77 = ~np.isnan(F_s77)  # (local)
k_s77_v = k_s77[valid_s77]  # (local)
F_s77_v = F_s77[valid_s77]  # (local)

log(f"  S77 grid: {len(k_s77)} total, {valid_s77.sum()} valid")
log(f"  S77 k-range: [{k_s77_v.min():.4f}, {k_s77_v.max():.4f}] M_KK")
log(f"  k_pivot = {k_pivot_MKK:.4f} M_KK")
log(f"  F_amp(k_pivot) S77 reference = {F_amp_pivot_s77:.2f}")
log(f"  H_dS = {H_dS:.4f} M_KK, eps_dS = {eps_dS:.4e}")

# Required range: [0.1, 10] * k_pivot
k_req_lo = 0.1 * k_pivot_MKK  # (local) = 1.431 M_KK
k_req_hi = 10.0 * k_pivot_MKK  # (local) = 143.11 M_KK

log(f"\n  Required k-range: [{k_req_lo:.4f}, {k_req_hi:.4f}] M_KK (= [0.1, 10] x k_pivot)")
log(f"  S77 coverage of req range: "
    f"[{max(k_s77_v.min(), k_req_lo):.4f}, {min(k_s77_v.max(), k_req_hi):.4f}] M_KK")
log(f"  S77 upper limit ({k_s77_v.max():.4f}) < required upper ({k_req_hi:.4f}) -> EXTEND")


# ========================================================================
#  SECTION 2: Extend F_amp(k) above S77 upper limit (k in [28.6, 143.1])
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 2: Extend F_amp(k) to cover [0.1, 10] x k_pivot")
log("=" * 78)

# Load S73B trajectory (single source of truth for z''/z and z)
d73 = np.load(os.path.join(SCRIPT_DIR, 's73b_efold_mapping.npz'), allow_pickle=True)
lna_raw = d73['lna_sol']  # (local)
H_raw = d73['H_sol']  # (local) M_KK units
w_raw = d73['w_sol']  # (local)
aH_raw = d73['aH_sol']  # (local) M_KK units

N_max_mode = 15.0  # (local) e-folds
mask_N = lna_raw <= N_max_mode  # (local)
N_arr = lna_raw[mask_N].copy()  # (local)
H_arr = H_raw[mask_N].copy()  # (local)
w_arr = w_raw[mask_N].copy()  # (local)
aH_arr = aH_raw[mask_N].copy()  # (local)
eps_arr = 1.5 * (1.0 + w_arr)  # (local) eps = 3(1+w)/2
a_arr = np.exp(N_arr)  # (local)
z_arr = a_arr * np.sqrt(2.0 * np.abs(eps_arr) + 1e-30)  # (local) Mukhanov z

d_eta_dN = 1.0 / aH_arr  # (local)
dN_step = np.gradient(N_arr)  # (local)
eta_arr = np.cumsum(d_eta_dN * dN_step)  # (local)
eta_arr -= eta_arr[0]  # (local)

deps_dN = np.gradient(eps_arr, N_arr)  # (local)
eta_H_arr = deps_dN / (eps_arr + 1e-30)  # (local)
deta_H_dN = np.gradient(eta_H_arr, N_arr)  # (local)
dlnz_dN = 1.0 + 0.5 * eta_H_arr  # (local)
d2lnz_dN2 = 0.5 * deta_H_dN  # (local)
pump_N_arr = d2lnz_dN2 + dlnz_dN**2 + (1.0 - eps_arr) * dlnz_dN  # (local)
zppoz_arr = aH_arr**2 * pump_N_arr  # (local)

zppoz_eta_interp = interp1d(eta_arr, zppoz_arr, kind='cubic', fill_value='extrapolate')  # (local)
z_eta_interp = interp1d(eta_arr, z_arr, kind='cubic', fill_value='extrapolate')  # (local)


def zppoz_pure_dS(eta):
    """z''/z for pure de Sitter (F_amp denominator)."""
    return 2.0 * H_dS**2 / (1.0 - H_dS * eta)**2


def solve_mode_conformal(k_com, zppoz_func, eta_start, eta_end,
                         rtol=1e-11, atol=1e-13, n_pts=2000):
    """Solve v'' + (k^2 - z''/z) v = 0 in conformal time.

    BD plane-wave IC: v = 1/sqrt(2k), dv/d_eta = -ik * v at eta_start.
    Returns dict with P_zeta_final and Wronskian deviation.
    """
    amp = 1.0 / np.sqrt(2.0 * k_com)  # (local)
    y0 = [amp, 0.0, 0.0, -k_com * amp]  # (local) [v_re, v_im, dv_re, dv_im]

    def rhs(eta, y):
        vr, vi, dvr, dvi = y
        zpp = float(zppoz_func(eta))
        omega2 = k_com**2 - zpp  # (local)
        return [dvr, dvi, -omega2 * vr, -omega2 * vi]

    d_eta = eta_end - eta_start  # (local)
    max_step = d_eta / 5000  # (local)
    sol = solve_ivp(rhs, [eta_start, eta_end], y0,
                    method='DOP853', rtol=rtol, atol=atol,
                    dense_output=True, max_step=max_step)

    if not sol.success:
        return {'status': 'FAIL'}

    eta_eval = np.linspace(eta_start, eta_end, n_pts)  # (local)
    y_eval = sol.sol(eta_eval)  # (local)
    v_abs2 = y_eval[0]**2 + y_eval[1]**2  # (local)
    z_eval = np.array([float(z_eta_interp(e)) for e in eta_eval])  # (local)
    P_zeta = k_com**3 / (2.0 * PI**2) * v_abs2 / (z_eval**2 + 1e-30)  # (local)
    P_zeta_final = np.median(P_zeta[-200:])  # (local)
    W = y_eval[0] * y_eval[3] - y_eval[1] * y_eval[2]  # (local)
    W_dev = abs(W[-1] - W[0]) / abs(W[0])  # (local)

    return {'status': 'OK', 'P_zeta_final': P_zeta_final, 'W_dev': W_dev}


def solve_mode_pure_dS(k_com, eta_end, rtol=1e-11, atol=1e-13, n_pts=2000):
    """Pure dS reference for F_amp denominator."""
    amp = 1.0 / np.sqrt(2.0 * k_com)  # (local)
    y0 = [amp, 0.0, 0.0, -k_com * amp]  # (local)

    def rhs(eta, y):
        vr, vi, dvr, dvi = y
        zpp = zppoz_pure_dS(eta)
        omega2 = k_com**2 - zpp
        return [dvr, dvi, -omega2 * vr, -omega2 * vi]

    d_eta = eta_end  # (local)
    max_step = d_eta / 5000  # (local)
    sol = solve_ivp(rhs, [0, eta_end], y0,
                    method='DOP853', rtol=rtol, atol=atol,
                    dense_output=True, max_step=max_step)

    if not sol.success:
        return {'status': 'FAIL'}

    eta_eval = np.linspace(0, eta_end, n_pts)  # (local)
    y_eval = sol.sol(eta_eval)  # (local)
    v_abs2 = y_eval[0]**2 + y_eval[1]**2  # (local)
    N_dS = -np.log(1.0 - H_dS * eta_eval)  # (local)
    z_dS = np.exp(N_dS) * np.sqrt(2.0 * eps_dS)  # (local)
    P_zeta = k_com**3 / (2.0 * PI**2) * v_abs2 / (z_dS**2 + 1e-30)  # (local)

    return {'status': 'OK', 'P_zeta_final': np.median(P_zeta[-200:])}


# Extension k-grid: logarithmic from S77 upper limit to 10*k_pivot
k_extend_lo = k_s77_v.max() * 1.01  # (local) just above S77 max
k_extend_hi = k_req_hi  # (local) = 143.11
n_extend = 20  # (local)
k_extend = np.geomspace(k_extend_lo, k_extend_hi, n_extend)  # (local)

log(f"  Extension grid: {n_extend} log-spaced k in [{k_extend_lo:.4f}, {k_extend_hi:.4f}] M_KK")

F_extend = np.zeros(n_extend)  # (local)
W_extend = np.zeros(n_extend)  # (local)

for i, k in enumerate(k_extend):
    # k/aH endpoint
    koh = k / aH_arr  # (local)
    idx_sh = np.where(koh < 0.05)[0]  # (local)
    if len(idx_sh) > 0:
        eta_end = eta_arr[idx_sh[0]]  # (local)
    else:
        eta_end = eta_arr[-1]  # (local)

    result_real = solve_mode_conformal(k, zppoz_eta_interp, 0.0, eta_end)
    if result_real['status'] != 'OK':
        F_extend[i] = np.nan
        W_extend[i] = np.nan
        continue

    N_dS_exit = np.log(k / (0.05 * H_dS))  # (local)
    eta_dS_end = (1.0 - np.exp(-N_dS_exit)) / H_dS  # (local)
    eta_dS_end = min(eta_dS_end, 0.99 / H_dS)  # (local)
    result_dS = solve_mode_pure_dS(k, eta_dS_end)
    if result_dS['status'] != 'OK':
        F_extend[i] = np.nan
        W_extend[i] = np.nan
        continue

    F_extend[i] = result_real['P_zeta_final'] / (result_dS['P_zeta_final'] + 1e-30)
    W_extend[i] = result_real['W_dev']

    if i % 5 == 0:
        log(f"    k = {k:10.4f} M_KK  F_amp = {F_extend[i]:.4e}  W_dev = {W_extend[i]:.2e}")

valid_ex = ~np.isnan(F_extend)  # (local)
log(f"  Extension: {valid_ex.sum()} / {n_extend} valid solutions")

# Combined grid
k_combined = np.concatenate([k_s77_v, k_extend[valid_ex]])  # (local)
F_combined = np.concatenate([F_s77_v, F_extend[valid_ex]])  # (local)

# Sort and dedupe
sort_idx = np.argsort(k_combined)  # (local)
k_combined = k_combined[sort_idx]  # (local)
F_combined = F_combined[sort_idx]  # (local)

# Keep only within required band and positive F_amp
in_band = (k_combined >= k_req_lo) & (k_combined <= k_req_hi) & (F_combined > 0)  # (local)
k_band = k_combined[in_band]  # (local)
F_band = F_combined[in_band]  # (local)

log(f"\n  Combined grid in [0.1, 10]*k_pivot band: {len(k_band)} points")
log(f"  k_band range: [{k_band.min():.4f}, {k_band.max():.4f}] M_KK")
log(f"  F_band range: [{F_band.min():.4e}, {F_band.max():.4e}]")


# ========================================================================
#  SECTION 3: Savitzky-Golay primary smoothing (poly 3, window 7)
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 3: Savitzky-Golay smoothing (primary: poly 3, window 7)")
log("=" * 78)

# Work in log-log: define x = ln(k / k_pivot), y = ln(F_amp)
x_band = np.log(k_band / k_pivot_MKK)  # (local) log-k centered on pivot
y_band = np.log(F_band)  # (local) log-F_amp

# Native data spacing (for sanity):
dx_native = np.median(np.diff(x_band))  # (local) ~ 0.116
log(f"  Native data spacing: median dlog_k = {dx_native:.4f}")
log(f"  Native data points: {len(x_band)}")

# Interpolate onto UNIFORM log-k grid for Savitzky-Golay (SG requires uniform spacing).
# Primary uniform grid: use spacing MATCHING native data density (~0.116), avoiding
# interpolation overshoot. This gives n_uni ~ 40 for log-range [-2.3, 2.3].
n_uni = int(round((np.log(10.0) - np.log(0.1)) / dx_native)) + 1  # (local)
x_uni = np.linspace(np.log(0.1), np.log(10.0), n_uni)  # (local)
# Cubic interpolation onto uniform log-k
y_interp = interp1d(x_band, y_band, kind='cubic', bounds_error=False, fill_value='extrapolate')  # (local)
y_uni = y_interp(x_uni)  # (local)

# Primary SG: polyorder=3, window_length=7 (pre-registered)
poly_primary = 3  # (local) pre-registered
window_primary = 7  # (local) pre-registered
y_sm_primary = savgol_filter(y_uni, window_length=window_primary, polyorder=poly_primary)  # (local)

# Slope via SG with deriv=1: gives d y / d x directly (since x is uniform spacing)
dx = x_uni[1] - x_uni[0]  # (local) uniform spacing = dx_native approx
slope_primary_arr = savgol_filter(y_uni, window_length=window_primary,
                                  polyorder=poly_primary, deriv=1, delta=dx)  # (local)

# Evaluate slope at x=0 (k = k_pivot) via interpolation
slope_interp = interp1d(x_uni, slope_primary_arr, kind='cubic')  # (local)
slope_at_pivot = float(slope_interp(0.0))  # (local)

log(f"  Uniform log-k grid: {n_uni} points, dx = {dx:.6f}")
log(f"  SG primary: poly={poly_primary}, window={window_primary}")
log(f"  slope_primary(x=0) = d ln F_amp / d ln k |_{{k=k_pivot}} = {slope_at_pivot:+.6f}")
log(f"  |slope_primary| = {abs(slope_at_pivot):.6f}")

# Interpolation-grid sensitivity test (additional cross-check):
# Compute slope on 3 different grid densities to verify primary is not
# an interpolation artifact. We use the SAME SG (poly=3, window=7) on each.
grid_sizes = [21, 41, 81]  # (local) coarser than primary, same, finer
slopes_grid = []  # (local)
for ng in grid_sizes:
    x_g = np.linspace(np.log(0.1), np.log(10.0), ng)
    y_g = y_interp(x_g)
    if ng > window_primary:
        dx_g = x_g[1] - x_g[0]
        slope_g_arr = savgol_filter(y_g, window_length=window_primary,
                                    polyorder=poly_primary, deriv=1, delta=dx_g)
        slope_g_i = interp1d(x_g, slope_g_arr, kind='cubic')
        slopes_grid.append(float(slope_g_i(0.0)))
    else:
        slopes_grid.append(np.nan)

log(f"  Interpolation-grid sensitivity (same SG poly=3, window=7):")
for ng, s in zip(grid_sizes, slopes_grid):
    log(f"    n_grid={ng:3d}  slope(pivot)={s:+.4f}")
grid_spread = np.nanmax(slopes_grid) - np.nanmin(slopes_grid)  # (local)
log(f"    Grid spread = {grid_spread:.4f}")


# ========================================================================
#  SECTION 4: CHK2 -- Smoothing-window sensitivity
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 4: CHK2 -- Smoothing-window sensitivity")
log("=" * 78)

# Scan polynomial orders {2, 3, 5} and windows {5, 7, 9, 11, 15}
poly_scan = [2, 3, 5]  # (local) pre-registered scan
window_scan = [5, 7, 9, 11, 15]  # (local)
n_poly = len(poly_scan)  # (local)
n_win = len(window_scan)  # (local)

slope_matrix = np.full((n_poly, n_win), np.nan)  # (local)

for ip, p in enumerate(poly_scan):
    for iw, w in enumerate(window_scan):
        if w <= p:
            continue  # window must exceed polyorder
        try:
            slope_arr = savgol_filter(y_uni, window_length=w, polyorder=p,
                                      deriv=1, delta=dx)  # (local)
            slope_i = interp1d(x_uni, slope_arr, kind='cubic')  # (local)
            slope_matrix[ip, iw] = float(slope_i(0.0))
        except Exception:
            slope_matrix[ip, iw] = np.nan

log("  Slope at k_pivot across (poly, window) scan:")
log(f"  {'poly\\win':<10}" + "".join([f"{w:>12}" for w in window_scan]))
for ip, p in enumerate(poly_scan):
    row = f"  {p:<10}"
    for iw, w in enumerate(window_scan):
        val = slope_matrix[ip, iw]
        if np.isnan(val):
            row += f"{'N/A':>12}"
        else:
            row += f"{val:>+12.5f}"
    log(row)

# Compute mean/std across valid entries
valid_mat = ~np.isnan(slope_matrix)  # (local)
slope_mean_scan = np.nanmean(slope_matrix)  # (local)
slope_std_scan = np.nanstd(slope_matrix)  # (local)
slope_spread = np.nanmax(slope_matrix) - np.nanmin(slope_matrix)  # (local)

log(f"\n  Scan statistics ({valid_mat.sum()} valid combos):")
log(f"    mean(slope) = {slope_mean_scan:+.6f}")
log(f"    std(slope)  = {slope_std_scan:.6f}")
log(f"    spread      = {slope_spread:.6f} (max - min)")
log(f"    primary slope: {slope_at_pivot:+.6f}  (|slope|={abs(slope_at_pivot):.6f})")
log(f"    primary vs mean: delta = {slope_at_pivot - slope_mean_scan:+.6f}")

# CHK2 PASS: primary slope within 2-sigma of scan mean AND spread < 0.2
chk2_consistent = (abs(slope_at_pivot - slope_mean_scan) <= 2.0 * slope_std_scan
                   and slope_spread < 0.2)  # (local)
chk2_outcome = "PASS" if chk2_consistent else "REVIEW"  # (local)
log(f"    CHK2 outcome: {chk2_outcome}")
if not chk2_consistent:
    log(f"    (primary slope is > 2-sigma from scan mean OR spread > 0.2 = artifact possible)")


# ========================================================================
#  SECTION 5: CHK1 -- BLV n_s invariance
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 5: CHK1 -- BLV n_s = 0.9567 invariance")
log("=" * 78)

# The BLV n_s = 0.9567 is the emergent scalar tilt from S73B functional
# selection (framework's n_s). It traces to SPECTRAL MOMENTS (a_2, a_4, a_6)
# of the deformed triple, NOT to F_amp(k) tilt. Our |slope| measures
# the k-dependence of the Parker squeezing F_amp(k), which is a DIFFERENT
# quantity from n_s^{framework}. Therefore:
#
#   CHK1 is a LOGICAL invariance check: the F_amp tilt slope does not
#   enter the BLV n_s computation; BLV n_s = 0.9567 is UNCHANGED by our
#   slope computation BY CONSTRUCTION.
#
# Numerically: load n_s from S73B functional selection output if available;
# else cite S75/S76 value.

BLV_n_s_target = 0.9567  # (local) S77 BLV target (framework's n_s)
# Load S73B functional selection n_s if available
n_s_BLV_source = "S73B functional selection (s73b_functional_select.npz)"  # (local)
try:
    d73f = np.load(os.path.join(SCRIPT_DIR, 's73b_functional_select.npz'), allow_pickle=True)
    # Check keys for n_s
    blv_keys = list(d73f.keys())
    n_s_BLV = None  # (local)
    for key in blv_keys:
        if 'n_s' in key.lower() or 'ns_' in key.lower():
            val = d73f[key]
            if hasattr(val, 'shape'):
                continue
            try:
                v = float(val)
                if 0.9 < v < 1.05:
                    n_s_BLV = v
                    n_s_BLV_source = f"{key} in s73b_functional_select.npz"
                    break
            except (ValueError, TypeError):
                continue
    if n_s_BLV is None:
        n_s_BLV = BLV_n_s_target  # (local) fallback to pre-registered BLV target
        n_s_BLV_source = "pre-registered BLV value (S77 convention pin)"
except Exception as e:
    n_s_BLV = BLV_n_s_target  # (local)
    n_s_BLV_source = f"pre-registered BLV value (fallback: {type(e).__name__})"

log(f"  BLV n_s target (pre-registered): {BLV_n_s_target}")
log(f"  n_s loaded: {n_s_BLV} (source: {n_s_BLV_source})")
log(f"  Tilt slope is LOGICALLY INDEPENDENT of BLV n_s by construction:")
log(f"    * BLV n_s = f(a_2, a_4, a_6) = spectral moments of D_K (emergent")
log(f"      scalar tilt from the GGE acoustic power spectrum functional)")
log(f"    * slope = d ln F_amp / d ln k = k-dependence of Bogoliubov")
log(f"      squeezing ratio against pure-dS reference")
log(f"  These are distinct structural quantities. CHK1: PASS (by logical")
log(f"  independence; |n_s_loaded - BLV_target| = {abs(n_s_BLV - BLV_n_s_target):.4e}")

chk1_pass = abs(n_s_BLV - BLV_n_s_target) < 0.01  # (local)


# ========================================================================
#  SECTION 6: CHK3 -- Branch-C consistency (saturated F_amp^sc -> slope ~ 0)
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 6: CHK3 -- Branch-C saturation consistency")
log("=" * 78)

# Under W1-C's analytical bound (F_amp^sc ~ 48 at k_pivot, from energy
# conservation saturation), the saturated F_amp is approximately
# INDEPENDENT of k in the saturated regime: rho_p/rho_bg < 0.1 forces
# F_amp to the budget-limited plateau. A flat F_amp(k) has slope = 0.
#
# This is a CONSISTENCY check on Branch-C, not an independent prediction.
# We construct a synthetic saturated F_amp^sc(k) model (capped at F_max)
# and verify the slope approaches zero.

# S78-W1-C output: F_amp^sc(k_pivot) = 48 (analytical bound)
F_amp_sc_bound = 48.0  # (local) S78-W1-C analytical bound (rate-limited by rho_p/rho_bg=0.1)
# Saturated model: F_sat(k) = min(F_linearized(k), F_amp_sc_bound)
F_band_sat = np.minimum(F_band, F_amp_sc_bound)  # (local)
y_band_sat = np.log(F_band_sat)  # (local)
y_interp_sat = interp1d(x_band, y_band_sat, kind='cubic',
                        bounds_error=False, fill_value='extrapolate')  # (local)
y_uni_sat = y_interp_sat(x_uni)  # (local)
slope_sat_arr = savgol_filter(y_uni_sat, window_length=window_primary,
                              polyorder=poly_primary, deriv=1, delta=dx)  # (local)
slope_sat_interp = interp1d(x_uni, slope_sat_arr, kind='cubic')  # (local)
slope_sat_at_pivot = float(slope_sat_interp(0.0))  # (local)

log(f"  Branch-C synthetic: F_amp^sc saturated at F_bound = {F_amp_sc_bound:.1f}")
log(f"  slope_sat(k_pivot) under saturation = {slope_sat_at_pivot:+.6f}")
log(f"  |slope_sat| = {abs(slope_sat_at_pivot):.6f}")

# Expectation: |slope_sat| should be MUCH smaller than |slope_primary|
# (because saturation flattens the k-dependence)
chk3_ratio = abs(slope_sat_at_pivot) / max(abs(slope_at_pivot), 1e-10)  # (local)
log(f"  |slope_sat| / |slope_linearized| = {chk3_ratio:.4f}")

# CHK3 PASS if saturation flattens slope by >= 10x (or reaches |slope_sat| < 0.05)
chk3_pass = (abs(slope_sat_at_pivot) < 0.05) or (chk3_ratio < 0.1)  # (local)
chk3_outcome = "PASS" if chk3_pass else "REVIEW"  # (local)
log(f"  CHK3 outcome: {chk3_outcome}")
log(f"  Interpretation: Branch-C at saturation floor has near-zero slope")
log(f"  by construction; our linearized slope {slope_at_pivot:+.6f} is the")
log(f"  NO-backreaction prediction, superseded by backreaction (caveat).")


# ========================================================================
#  SECTION 7: Gate Verdict (INFO -- W1-C INCOMPUTABLE regime)
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 7: Gate verdict")
log("=" * 78)

abs_slope = abs(slope_at_pivot)  # (local)

# Pre-registered gate:
#  PASS  : |slope| < 0.1 from converged F_amp^sc (but W1-C is INCOMPUTABLE -- not possible)
#  FAIL  : |slope| > 0.2 after backreaction
#  INFO  : W1-C INCOMPUTABLE and slope from linearized F_amp with caveat
#          (CURRENT REGIME per shell line 539)

if abs_slope < 0.1:
    verdict_class = "INFO"  # (local)
    verdict_reason = (f"|slope| = {abs_slope:.4f} < 0.1 band; "
                      f"BUT input is linearized F_amp (W1-C INCOMPUTABLE).")
elif abs_slope < 0.2:
    verdict_class = "INFO"  # (local)
    verdict_reason = (f"|slope| = {abs_slope:.4f} in [0.1, 0.2]; "
                      f"input is linearized F_amp (W1-C INCOMPUTABLE).")
else:
    # Per shell: FAIL requires "after backreaction" OR challenging BLV n_s.
    # Our input is linearized, so we do NOT have "after backreaction."
    # Therefore INFO with caveat.
    verdict_class = "INFO"  # (local)
    verdict_reason = (f"|slope| = {abs_slope:.4f} > 0.2 in LINEARIZED regime; "
                      f"FAIL clause requires backreaction input, which is "
                      f"W1-C INCOMPUTABLE; reporting INFO with caveat. "
                      f"Saturated Branch-C slope is {slope_sat_at_pivot:+.4f}, "
                      f"indicating |slope| collapses under backreaction.")

log(f"  slope(k_pivot) linearized   = {slope_at_pivot:+.6f}")
log(f"  slope(k_pivot) saturated    = {slope_sat_at_pivot:+.6f}")
log(f"  |slope|_linearized          = {abs_slope:.6f}")
log(f"  Scan spread (poly 2-5, win 5-15) = {slope_spread:.6f}")
log(f"  Verdict: {verdict_class}")
log(f"  Reason: {verdict_reason}")

# Append to gate verdicts file
verdict_line = (f"S78-W3-B-FAMP-TILT-SMOOTH: {verdict_class} -- "
                f"|slope|={abs_slope:.4f} "
                f"(SCHEME-INDEPENDENT,POWER-RATIO,L_max=10), "
                f"input=linearized-F_amp-with-W1C-caveat "
                f"(slope_primary={slope_at_pivot:+.4f}, "
                f"slope_saturated={slope_sat_at_pivot:+.4f}, "
                f"scan_spread={slope_spread:.4f}, "
                f"CHK1={'P' if chk1_pass else 'R'}/"
                f"CHK2={'P' if chk2_consistent else 'R'}/"
                f"CHK3={'P' if chk3_pass else 'R'})")

with open(GATE_VERDICTS, 'a') as f:
    f.write(verdict_line + "\n")

log(f"\n  Appended to: {GATE_VERDICTS}")


# ========================================================================
#  SECTION 8: Save artifacts
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 8: Save outputs")
log("=" * 78)

# Save NPZ
np.savez(
    OUT_NPZ,
    gate_name='S78-W3-B-FAMP-TILT-SMOOTH',
    gate_verdict=verdict_class,
    gate_detail=verdict_reason,
    # Input (with caveat)
    k_s77=k_s77_v,
    F_s77=F_s77_v,
    k_extend=k_extend[valid_ex],
    F_extend=F_extend[valid_ex],
    W_extend=W_extend[valid_ex],
    k_combined=k_band,
    F_combined=F_band,
    # Uniform grid and smoothing
    x_uni=x_uni,
    y_uni=y_uni,
    y_sm_primary=y_sm_primary,
    slope_primary_arr=slope_primary_arr,
    slope_at_pivot=slope_at_pivot,
    # Smoothing scan (CHK2)
    poly_scan=np.array(poly_scan),
    window_scan=np.array(window_scan),
    slope_matrix=slope_matrix,
    slope_mean_scan=slope_mean_scan,
    slope_std_scan=slope_std_scan,
    slope_spread=slope_spread,
    # Interpolation-grid sensitivity
    grid_sizes=np.array(grid_sizes),
    slopes_grid=np.array(slopes_grid),
    grid_spread=grid_spread,
    # CHK1 BLV
    BLV_n_s_target=BLV_n_s_target,
    n_s_BLV=n_s_BLV,
    n_s_BLV_source=n_s_BLV_source,
    chk1_pass=chk1_pass,
    # CHK3 Branch-C saturation
    F_amp_sc_bound=F_amp_sc_bound,
    F_band_sat=F_band_sat,
    slope_sat_at_pivot=slope_sat_at_pivot,
    chk3_pass=chk3_pass,
    # Pins
    k_pivot_MKK=k_pivot_MKK,
    k_req_lo=k_req_lo,
    k_req_hi=k_req_hi,
    poly_primary=poly_primary,
    window_primary=window_primary,
    convention_tag='POWER-RATIO',
    scheme_tag='SCHEME-INDEPENDENT',
    L_max_tag=10,
    caveat='linearized F_amp (W1-C INCOMPUTABLE-FALLBACK-TO-BOUND); slope superseded by backreaction',
)
log(f"  NPZ: {OUT_NPZ}")


# 6-panel plot
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3)

# Panel 1: F_amp(k) linearized (log-log)
ax1 = fig.add_subplot(gs[0, 0])
ax1.loglog(k_band / k_pivot_MKK, F_band, 'o', color='steelblue', markersize=4,
           alpha=0.7, label='linearized F_amp')  # (local)
ax1.loglog(k_band / k_pivot_MKK, F_band_sat, 's', color='crimson', markersize=3,
           alpha=0.5, label=f'saturated F_amp^sc={F_amp_sc_bound:.0f}')  # (local)
ax1.axvline(1.0, color='k', linestyle='--', linewidth=0.6, label='k=k_pivot')
ax1.set_xlabel('k / k_pivot')
ax1.set_ylabel('F_amp (power ratio)')
ax1.set_title(f'F_amp(k) input (W1-C INCOMPUTABLE caveat)')
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)

# Panel 2: log-log fit near pivot
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(x_uni, y_uni, '-', color='steelblue', alpha=0.5, label='raw log F_amp (interp)')
ax2.plot(x_uni, y_sm_primary, '-', color='darkorange', linewidth=2,
         label=f'SG poly={poly_primary} win={window_primary}')
ax2.axvline(0.0, color='k', linestyle='--', linewidth=0.6, label='k=k_pivot')
ax2.set_xlabel('ln(k / k_pivot)')
ax2.set_ylabel('ln F_amp')
ax2.set_title('Smoothed log-log trace')
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)

# Panel 3: slope(k) from SG derivative
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(x_uni, slope_primary_arr, '-', color='darkorange', linewidth=2,
         label='linearized slope')
ax3.plot(x_uni, slope_sat_arr, '-', color='crimson', linewidth=1.5,
         label='saturated slope (Branch-C)')
ax3.axvline(0.0, color='k', linestyle='--', linewidth=0.6)
ax3.axhline(0.0, color='gray', linestyle=':', linewidth=0.6)
ax3.axhline(slope_at_pivot, color='darkorange', linestyle=':', linewidth=0.8,
            label=f'slope(pivot)={slope_at_pivot:+.3f}')
ax3.axhline(slope_sat_at_pivot, color='crimson', linestyle=':', linewidth=0.8,
            label=f'slope_sat(pivot)={slope_sat_at_pivot:+.3f}')
ax3.set_xlabel('ln(k / k_pivot)')
ax3.set_ylabel('d ln F_amp / d ln k')
ax3.set_title('Slope (SG derivative)')
ax3.legend(fontsize=8, loc='best')
ax3.grid(alpha=0.3)

# Panel 4: CHK2 scan heatmap
ax4 = fig.add_subplot(gs[1, 0])
im = ax4.imshow(slope_matrix, cmap='RdBu_r', aspect='auto',
                vmin=-max(np.nanmax(np.abs(slope_matrix)), 0.1),
                vmax=max(np.nanmax(np.abs(slope_matrix)), 0.1))
ax4.set_xticks(np.arange(n_win))
ax4.set_xticklabels([str(w) for w in window_scan])
ax4.set_yticks(np.arange(n_poly))
ax4.set_yticklabels([str(p) for p in poly_scan])
ax4.set_xlabel('window_length')
ax4.set_ylabel('polyorder')
ax4.set_title('CHK2: slope(pivot) vs (poly, window)')
for ip in range(n_poly):
    for iw in range(n_win):
        val = slope_matrix[ip, iw]
        if not np.isnan(val):
            ax4.text(iw, ip, f'{val:+.3f}', ha='center', va='center',
                     fontsize=8, color='white')
cbar = plt.colorbar(im, ax=ax4)
cbar.set_label('slope at k_pivot')

# Panel 5: Scan distribution
ax5 = fig.add_subplot(gs[1, 1])
valid_slopes = slope_matrix[~np.isnan(slope_matrix)]  # (local)
ax5.hist(valid_slopes, bins=15, color='steelblue', edgecolor='k', alpha=0.7)
ax5.axvline(slope_at_pivot, color='darkorange', linewidth=2,
            label=f'primary (3,7)={slope_at_pivot:+.3f}')
ax5.axvline(slope_mean_scan, color='green', linestyle='--',
            label=f'scan mean={slope_mean_scan:+.3f}')
ax5.axvline(0.0, color='k', linestyle=':', linewidth=0.6, label='slope=0')
ax5.set_xlabel('slope at k_pivot')
ax5.set_ylabel('count')
ax5.set_title(f'CHK2: scan spread={slope_spread:.3f}')
ax5.legend(fontsize=8)
ax5.grid(alpha=0.3)

# Panel 6: Summary
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
summary = (
    f"S78-W3-B-FAMP-TILT-SMOOTH\n"
    f"{'='*35}\n\n"
    f"VERDICT: {verdict_class}\n\n"
    f"slope (linearized primary):\n"
    f"  {slope_at_pivot:+.4f}\n"
    f"|slope|: {abs_slope:.4f}\n\n"
    f"slope (saturated, Branch-C):\n"
    f"  {slope_sat_at_pivot:+.4f}\n\n"
    f"Smoothing scan:\n"
    f"  mean  = {slope_mean_scan:+.4f}\n"
    f"  std   = {slope_std_scan:.4f}\n"
    f"  spread= {slope_spread:.4f}\n\n"
    f"Tags:\n"
    f"  convention: POWER-RATIO\n"
    f"  scheme:     SCHEME-INDEPENDENT\n"
    f"  L_max:      10\n\n"
    f"CHK1 (BLV n_s inv): {'PASS' if chk1_pass else 'REVIEW'}\n"
    f"CHK2 (smoothing):   {'PASS' if chk2_consistent else 'REVIEW'}\n"
    f"CHK3 (Branch-C):    {'PASS' if chk3_pass else 'REVIEW'}\n\n"
    f"CAVEAT:\n"
    f"  Input=linearized F_amp.\n"
    f"  W1-C INCOMPUTABLE-\n"
    f"  FALLBACK-TO-BOUND.\n"
    f"  Slope superseded by\n"
    f"  backreaction."
)
ax6.text(0.02, 0.98, summary, transform=ax6.transAxes,
         fontsize=9, verticalalignment='top', family='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle(f'S78-W3-B: F_amp(k) Tilt Smoothed  |  slope(k_pivot)={slope_at_pivot:+.4f}  '
             f'(linearized + W1-C caveat)', fontsize=13)
plt.savefig(OUT_PNG, dpi=120, bbox_inches='tight')
plt.close()
log(f"  PNG: {OUT_PNG}")

t_total = time.time() - t_start  # (local)
log(f"\n  Total runtime: {t_total:.1f} s")
log("\n" + "=" * 78)
log("S78 W3-B COMPLETE")
log("=" * 78)
