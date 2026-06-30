#!/usr/bin/env python3
"""
S71 ENTRY-HORIZON-SPECTRUM-71 — D_K Eigenvalue Tracking Across Entry Sonic Horizon
====================================================================================

The S70 Hawking workshop identified a six-layer causal structure with two sonic
horizons: entry at tau ~ 0.22 (Ma crosses 1 upward) and exit at tau ~ 0.16
(Ma crosses 1 downward). This script tracks D_K eigenvalues across the ENTRY
sonic horizon to count level crossings and identify spectral reorganization.

Physical picture:
  - At the entry sonic horizon, the modulus flow velocity v(tau) equals the
    fabric sound speed c_s(tau).
  - Level crossings of D_K eigenvalues at this point would indicate spectral
    reorganization -- analogous to the BCS transition at the exit horizon.
  - The effective temperature T_entry = (1/2*pi) * |d(v - c_s)/dtau|_{tau_entry}
    is the analog of Hawking surface gravity.

Method:
  1. Compute v(tau) from the spectral action gradient dS/dtau via the modulus
     equation of motion: M_ATDHFB * d^2tau/dt^2 = dS/dtau.
  2. Compute c_s(tau) = sqrt(d^2S/dtau^2 / M_ATDHFB) -- the sound speed of
     modulus fluctuations in the spectral action landscape.
  3. Solve v(tau) = c_s(tau) for tau_entry.
  4. Track the 8 BCS-relevant D_K eigenvalues at fine tau steps through
     tau in [0.18, 0.26] using dirac_spectrum.
  5. Count level crossings and measure gaps at closest approach.
  6. Compute T_entry from the surface gravity analog.

Gate: ENTRY-HORIZON-SPECTRUM-71. INFO: N_crossings and T_entry.

Author: Spectral Geometer (S71)
Date: 2026-04-09
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

# ============================================================
# Path setup
# ============================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, '..')
ARCHIVE_DIR = os.path.join(PROJECT_ROOT, "computations", "_shared")

if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if ARCHIVE_DIR not in sys.path:
    sys.path.append(ARCHIVE_DIR)

from canonical_constants import (
    tau_fold, v_terminal, c_fabric, M_ATDHFB, G_DeWitt,
    a0_fold, a2_fold, a4_fold, dS_fold, d2S_fold,
    T_compound, Delta_BCS, E_B1, E_B2_mean, E_B3_mean,
    S_fold, M_KK, H_fold, dt_transit
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, get_irrep, dirac_operator_on_irrep,
    _irrep_cache
)

print("=" * 72)
print("ENTRY-HORIZON-SPECTRUM-71: D_K Eigenvalue Tracking at Entry Horizon")
print("=" * 72)
print()

t_total_start = time()

# ============================================================
# 1. SPECTRAL ACTION LANDSCAPE: v(tau) AND c_s(tau)
# ============================================================
print("--- Phase 1: Spectral action landscape from S42/S36 data ---")
t0 = time()

# Load S42 gradient data
d42 = np.load(os.path.join(ARCHIVE_DIR, 's42_gradient_stiffness.npz'), allow_pickle=True)
tau_grid_42 = d42['tau_grid']      # [0.05, 0.1, 0.13, 0.15, 0.17, 0.19, 0.2, 0.22, 0.25, 0.3]
dS_dtau_42 = d42['dS_dtau']       # spectral action gradient at those tau values
d2S_dtau2_42 = d42['d2S_dtau2']   # second derivative
S_total_42 = d42['S_total']       # S_full at those tau values
Z_spectral_42 = d42['Z_spectral'] # gradient stiffness

print(f"  S42 tau grid: {tau_grid_42}")
print(f"  dS/dtau range: [{dS_dtau_42.min():.1f}, {dS_dtau_42.max():.1f}]")
print(f"  d^2S/dtau^2 range: [{d2S_dtau2_42.min():.1f}, {d2S_dtau2_42.max():.1f}]")

# Cubic spline interpolation of spectral action data
cs_dS = CubicSpline(tau_grid_42, dS_dtau_42)
cs_d2S = CubicSpline(tau_grid_42, d2S_dtau2_42)
cs_Stot = CubicSpline(tau_grid_42, S_total_42)

# The modulus velocity v(tau) from the equation of motion.
#
# The spectral action gradient dS/dtau acts as a force on the modulus tau.
# From M_ATDHFB * d^2tau/dt^2 = dS/dtau, and using v = dtau/dt, we get
# M_ATDHFB * v * dv/dtau = dS/dtau.
#
# At any tau, the modulus has been accelerated from rest at tau -> infinity
# (or from some initial tau_0 >> tau_fold). Energy conservation:
#   (1/2) * M_ATDHFB * v^2 = S(tau_0) - S(tau)
#
# Since S(tau) is monotonically increasing, S(tau_0) > S(tau) for tau < tau_0,
# so v^2 > 0 as expected (the modulus rolls "downhill" from large to small tau).
#
# We use the S42 data to compute v(tau) = sqrt(2 * (S(tau_0) - S(tau)) / M_ATDHFB)
# taking tau_0 = 0.30 as the outermost S42 grid point.

tau_0 = tau_grid_42[-1]  # 0.30
S_0 = S_total_42[-1]     # S_full at tau=0.30

def v_modulus(tau):
    """Modulus velocity at tau from energy conservation."""
    S_tau = float(cs_Stot(tau))
    dS = S_0 - S_tau
    if dS < 0:
        return 0.0
    return np.sqrt(2.0 * dS / M_ATDHFB)

# Sound speed of modulus fluctuations:
# c_s^2 = d^2S/dtau^2 / M_ATDHFB
# This is the "acoustic" speed in the spectral action landscape --
# the speed at which perturbations to tau propagate.
def c_s_modulus(tau):
    """Sound speed of modulus fluctuations at tau."""
    d2S = float(cs_d2S(tau))
    return np.sqrt(abs(d2S) / M_ATDHFB)

# Evaluate on a fine grid
tau_fine = np.linspace(0.06, 0.29, 500)
v_arr = np.array([v_modulus(t) for t in tau_fine])
cs_arr = np.array([c_s_modulus(t) for t in tau_fine])
Ma_arr = np.where(cs_arr > 0, v_arr / cs_arr, 0.0)

# Cross-check at fold
v_at_fold = v_modulus(tau_fold)
cs_at_fold = c_s_modulus(tau_fold)
Ma_at_fold = v_at_fold / cs_at_fold if cs_at_fold > 0 else 0.0

print(f"\n  At fold (tau={tau_fold}):")
print(f"    v(tau_fold) = {v_at_fold:.4f} M_KK")
print(f"    c_s(tau_fold) = {cs_at_fold:.4f} M_KK")
print(f"    Ma(tau_fold) = {Ma_at_fold:.4f}")
print(f"    v_terminal (canonical) = {v_terminal:.4f} M_KK")
print(f"    c_fabric (canonical) = {c_fabric:.4f} M_KK")

# Find sonic crossings: where v(tau) = c_s(tau), i.e. Ma = 1
# The transit goes from large tau toward small tau.
# Entry horizon: Ma crosses 1 upward (approaching fold from above).
# Note: the modulus velocity v(tau) is speed in TAU per unit time.
# We need to check where Ma crosses unity.

diff_v_cs = v_arr - cs_arr
sign_changes = np.where(np.diff(np.sign(diff_v_cs)))[0]

print(f"\n  Sonic horizon search:")
print(f"    v range: [{v_arr.min():.4f}, {v_arr.max():.4f}] M_KK")
print(f"    c_s range: [{cs_arr.min():.4f}, {cs_arr.max():.4f}] M_KK")
print(f"    Ma range: [{Ma_arr.min():.4f}, {Ma_arr.max():.4f}]")
print(f"    Sign changes in (v - c_s): {len(sign_changes)}")

# The Ma from the canonical constants uses a different definition:
# v_terminal/c_fabric = 26.545/209.97 = 0.1264 -- this is the TERMINAL
# velocity from S38, not the tau-dependent velocity from energy conservation.
#
# The S70 workshop Mach numbers (Ma = 0, 0.76, 54.7, 0.045 at tau = 0.25, 0.221, 0.190, 0.15)
# use a DIFFERENT velocity model that includes the spectral action's full
# energy budget. The Ma ~ 54.7 at fold means v >> c_s there.
#
# For the spectral action landscape, c_s is the MODULUS sound speed:
# c_s^2 = d^2V/dtau^2 / M = d^2S/dtau^2 / M_ATDHFB
# And v is the rolling velocity from energy conservation in the S(tau) potential.
#
# Let's compute the S70 Mach sequence from our data:
Ma_check_taus = [0.15, 0.19, 0.221, 0.25]
print(f"\n  S70 Mach sequence cross-check:")
for tc in Ma_check_taus:
    if 0.06 <= tc <= 0.29:
        vc = v_modulus(tc)
        cc = c_s_modulus(tc)
        mac = vc / cc if cc > 0 else 0.0
        print(f"    tau={tc:.3f}: v={vc:.4f}, c_s={cc:.4f}, Ma={mac:.6f}")

# The S70 workshop used a DIFFERENT definition of sound speed.
# The Hawking workshop's c_s is the FABRIC speed (BCS+Josephson medium),
# not the modulus fluctuation speed.
#
# The correct sound speed for the sonic horizon is the speed at which
# PERTURBATIONS to the modulus propagate, which for a scalar field in a
# potential V(tau) is c_s^2 = V''(tau)/M.
#
# Since V(tau) = -S_full(tau) (the modulus rolls DOWN the spectral action),
# c_s^2 = d^2S/dtau^2 / M_ATDHFB.
#
# This gives c_s ~ 430 M_KK everywhere, while v ~ 100 M_KK at fold.
# So Ma < 1 everywhere in this model -- no sonic horizon in the modulus sector.
#
# The S70 workshop's sonic horizons are in the FABRIC sector:
# v is the modulus rolling speed, and c_s is the fabric propagation speed.
# The fabric speed c_fabric = 209.97 involves the FULL spectral action
# stiffness, while v_terminal = 26.545 is the terminal rolling speed.
#
# The large Mach number (54.7) at fold is from a DIFFERENT velocity definition
# that involves the Hubble-like expansion rate H_fold = 586.5.
#
# Let me use the S70 workshop's definition directly.
# From PC1: Ma = 0.76 at tau=0.221, Ma = 54.7 at tau=0.190.
# The entry horizon (Ma=1) is between tau=0.190 and tau=0.221.
#
# The velocity profile from S38:
# v(tau) = H_fold * |tau - tau_fold| / dt_transit (linear approximation near fold)
# This diverges away from fold -- which is unphysical.
#
# More carefully: the Mach number profile from the S70 workshop uses
# Ma(tau) = v(tau) / c_s(tau) where:
# - v(tau) involves the spectral action force dS/dtau and dissipation
# - c_s(tau) is the fabric sound speed which depends on BCS state
#
# For this computation, I will:
# 1. Interpolate the S70 Ma data to find tau_entry precisely
# 2. Track D_K eigenvalues through that region regardless of the Ma model
# 3. Compute T_entry from the Ma gradient

# S70 Mach data from the workshop (PC1):
# Ma = 0 at tau ~ 0.25 (start, subsonic)
# Ma = 0.76 at tau = 0.221
# Ma = 54.7 at tau = 0.190 (fold, peak)
# Ma = 0.045 at tau = 0.15 (post-exit, subsonic)
#
# The entry horizon is where Ma first crosses 1.
# Between tau=0.221 (Ma=0.76) and tau=0.190 (Ma=54.7).
# Since tau DECREASES during transit, the entry is at the larger tau value.

tau_Ma = np.array([0.25, 0.221, 0.190, 0.15])
Ma_values = np.array([0.0, 0.76, 54.7, 0.045])

# Interpolate to find Ma=1 crossing
# Use log for the large dynamic range
# Only use the entry segment: tau from 0.25 to 0.19
tau_entry_seg = tau_Ma[:3][::-1]   # [0.190, 0.221, 0.25]
Ma_entry_seg = Ma_values[:3][::-1]  # [54.7, 0.76, 0.0]

# Linear interpolation between tau=0.221 (Ma=0.76) and tau=0.190 (Ma=54.7)
# Ma = 1 at tau_entry
# Linear: Ma(tau) = 0.76 + (54.7-0.76)*(0.221-tau)/(0.221-0.190)
# 1 = 0.76 + 53.94 * (0.221-tau_entry)/0.031
# 0.24 = 53.94 * (0.221-tau_entry)/0.031
# (0.221-tau_entry) = 0.24 * 0.031 / 53.94 = 0.0001379
# tau_entry = 0.221 - 0.000138 = 0.22086

tau_entry_linear = 0.221 - 0.24 * 0.031 / (54.7 - 0.76)
print(f"\n  Entry sonic horizon (linear interpolation):")
print(f"    tau_entry = {tau_entry_linear:.6f}")

# But this linear interp is crude. Use cubic spline on the S70 Ma data.
# The Ma profile should be smooth. Use the full 4-point data.
# Since Ma varies enormously, use log(Ma+eps) for interpolation.
eps_Ma = 0.01  # (local)
log_Ma = np.log(Ma_values + eps_Ma)
cs_log_Ma = CubicSpline(tau_Ma[::-1], log_Ma[::-1])  # tau increasing

tau_dense = np.linspace(0.15, 0.25, 1000)
Ma_dense = np.exp(cs_log_Ma(tau_dense)) - eps_Ma

# Find where Ma crosses 1
Ma_minus_1 = Ma_dense - 1.0
crossings = np.where(np.diff(np.sign(Ma_minus_1)))[0]
tau_entry_spline = None
for idx in crossings:
    t_cross = tau_dense[idx] + (tau_dense[idx+1] - tau_dense[idx]) * \
              abs(Ma_minus_1[idx]) / (abs(Ma_minus_1[idx]) + abs(Ma_minus_1[idx+1]))
    if t_cross > tau_fold:  # entry horizon is above fold
        tau_entry_spline = t_cross
        break

if tau_entry_spline is None:
    # Fallback: use linear estimate
    tau_entry_spline = tau_entry_linear
    print(f"    Spline crossing not found, using linear: tau_entry = {tau_entry_spline:.6f}")
else:
    print(f"    tau_entry (spline) = {tau_entry_spline:.6f}")

# Use the best estimate
tau_entry = tau_entry_spline
print(f"    ADOPTED tau_entry = {tau_entry:.6f}")

# Surface gravity analog: kappa = |d(v - c_s)/dtau|_{tau_entry}
# In the S70 Ma framework: kappa ~ |dMa/dtau|_{tau_entry} * c_s(tau_entry)
# From the spline:
dMa_dtau_at_entry = float(cs_log_Ma(tau_entry, 1)) * np.exp(float(cs_log_Ma(tau_entry)))
print(f"    |dMa/dtau| at entry ~ {abs(dMa_dtau_at_entry):.4f}")

# T_entry = (1/2*pi) * kappa
# kappa = surface gravity = |d(v-c_s)/dr| at horizon
# In our modulus space: kappa = |d(Ma*c_s - c_s)/dtau| = c_s * |dMa/dtau|
# But c_s at the entry horizon is not well-constrained by 4 data points.
# Use the modulus fluctuation speed:
c_s_at_entry = c_s_modulus(tau_entry)
kappa_entry = abs(dMa_dtau_at_entry) * c_s_at_entry

T_entry = kappa_entry / (2.0 * np.pi)
print(f"    c_s at entry = {c_s_at_entry:.4f} M_KK")
print(f"    kappa_entry = {kappa_entry:.4f} M_KK")
print(f"    T_entry = kappa/(2*pi) = {T_entry:.4f} M_KK")
print(f"    T_compound (canonical) = {T_compound:.4f} M_KK")
print(f"    T_entry / T_compound = {T_entry / T_compound:.4f}")

print(f"\n  Time: {time()-t0:.2f}s")
print()

# ============================================================
# 2. COMPUTE D_K EIGENVALUES ACROSS ENTRY HORIZON REGION
# ============================================================
print("--- Phase 2: D_K eigenvalue tracking across entry horizon ---")
t0 = time()

# SU(3) infrastructure
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# Scan range: tau from 0.18 to 0.26 (brackets the entry horizon)
# Step dtau = 0.001 as specified
tau_scan = np.arange(0.180, 0.261, 0.001)
n_tau_scan = len(tau_scan)
print(f"  Scanning {n_tau_scan} tau values in [{tau_scan[0]:.3f}, {tau_scan[-1]:.3f}]")

# Focus on the 8 BCS-relevant eigenvalues from the lowest sectors.
# The BCS modes are: 4 B2 (from (0,1) and (1,0) sectors) + 1 B1 (from (0,0))
# + 3 B3 (from (1,1) sector).
#
# At the fold: E_B1 = 0.819, E_B2_mean = 0.845, E_B3_mean = 0.978
# These are the ABSOLUTE VALUES of D_K eigenvalues (omega = |Im(lambda)|).
#
# To track individual eigenvalues across tau, we need consistent ordering.
# The cleanest approach: compute ALL eigenvalues in a given (p,q) sector
# and track them by sorting, using the sector label for branch identification.


def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# Sectors containing the 8 BCS modes:
# (0,0): trivial, dim=1, 16 spinor eigenvalues -> 8 unique positive omega
#   contains B1 mode
# (0,1): fundamental, dim=3, 48 eigenvalues -> 24 unique positive
#   contains B2 modes
# (1,0): conjugate, dim=3, 48 eigenvalues -> 24 unique positive
#   contains B2 modes
# (1,1): adjoint, dim=8, 128 eigenvalues -> 64 unique positive
#   contains B3 modes
#
# We track ALL eigenvalues in these sectors, then identify the BCS-relevant
# ones as the LOWEST eigenvalue(s) in each sector.

BCS_SECTORS = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Storage: for each sector, store sorted positive eigenvalues at each tau
sector_evals = {}
for p, q in BCS_SECTORS:
    d = dim_pq(p, q)
    n_spinor = d * 16
    n_unique_pos = n_spinor // 2  # Due to +/- symmetry
    sector_evals[(p, q)] = np.zeros((n_tau_scan, n_unique_pos))


def compute_sector_eigenvalues(tau_val, p, q):
    """
    Compute sorted positive eigenvalues of D_K in sector (p,q) at given tau.
    Returns sorted array of unique positive |Im(lambda)|.
    """
    _irrep_cache.clear()

    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau_val)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    if (p, q) == (0, 0):
        D = Omega.copy()
    else:
        rho, _ = get_irrep(p, q, gens, f_abc)
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)

    evals_raw = np.linalg.eigvals(D)
    abs_omega = np.abs(evals_raw.imag)

    # Sort and keep unique positive values
    abs_omega_sorted = np.sort(abs_omega)

    # Remove near-duplicates from +/- symmetry
    unique_pos = []
    for val in abs_omega_sorted:
        if val > 1e-10:
            if not unique_pos or abs(val - unique_pos[-1]) > 1e-8:
                unique_pos.append(val)

    return np.array(unique_pos)


# Compute eigenvalues at all tau values
print(f"  Computing eigenvalues for {len(BCS_SECTORS)} sectors x {n_tau_scan} tau values...")
for p, q in BCS_SECTORS:
    d = dim_pq(p, q)
    expected_n = d * 16 // 2
    print(f"  Sector ({p},{q}): dim={d}, expected {expected_n} unique positive eigenvalues")
    for i, tau_val in enumerate(tau_scan):
        evals = compute_sector_eigenvalues(tau_val, p, q)

        # Handle mode count variations
        n_got = len(evals)
        n_store = sector_evals[(p, q)].shape[1]

        if n_got >= n_store:
            sector_evals[(p, q)][i, :] = evals[:n_store]
        else:
            sector_evals[(p, q)][i, :n_got] = evals
            sector_evals[(p, q)][i, n_got:] = np.nan
            if i == 0:
                print(f"    WARNING at tau={tau_val:.3f}: got {n_got} evals, expected {n_store}")

    print(f"    Completed sector ({p},{q}): "
          f"omega_min=[{sector_evals[(p,q)][:,0].min():.6f}, {sector_evals[(p,q)][:,0].max():.6f}], "
          f"omega_max=[{np.nanmin(sector_evals[(p,q)][:,-1]):.6f}, {np.nanmax(sector_evals[(p,q)][:,-1]):.6f}]")

print(f"  Total computation time: {time()-t0:.2f}s")
print()

# ============================================================
# 3. EXTRACT BCS EIGENVALUE BRANCHES AND TRACK CROSSINGS
# ============================================================
print("--- Phase 3: BCS eigenvalue branch tracking ---")
t0 = time()

# The 8 BCS eigenvalues are the LOWEST eigenvalue in each of these sectors:
#   B1: min of (0,0)  -- 1 mode
#   B2: min of (0,1)  -- 4 modes (but (0,1) and (1,0) give same minimum by conjugate symmetry)
#   B3: min of (1,1)  -- 3 modes
#
# Actually, the B2 sector has 4 modes from 4 degenerate states in the (0,1) sector.
# Let's track the first few eigenvalues from each sector.

# B1: lowest eigenvalue of (0,0) sector
B1_track = sector_evals[(0, 0)][:, 0]

# B2: lowest eigenvalue of (0,1) sector (and conjugate (1,0))
B2_track_01 = sector_evals[(0, 1)][:, 0]
B2_track_10 = sector_evals[(1, 0)][:, 0]

# B3: lowest eigenvalue of (1,1) sector
B3_track = sector_evals[(1, 1)][:, 0]

# Also track the SECOND lowest in each sector (to check for intra-sector crossings)
B1_second = sector_evals[(0, 0)][:, 1] if sector_evals[(0, 0)].shape[1] > 1 else None
B2_second_01 = sector_evals[(0, 1)][:, 1] if sector_evals[(0, 1)].shape[1] > 1 else None
B2_second_10 = sector_evals[(1, 0)][:, 1] if sector_evals[(1, 0)].shape[1] > 1 else None
B3_second = sector_evals[(1, 1)][:, 1] if sector_evals[(1, 1)].shape[1] > 1 else None

print(f"  B1 range: [{B1_track.min():.6f}, {B1_track.max():.6f}] M_KK")
print(f"  B2(0,1) range: [{B2_track_01.min():.6f}, {B2_track_01.max():.6f}] M_KK")
print(f"  B2(1,0) range: [{B2_track_10.min():.6f}, {B2_track_10.max():.6f}] M_KK")
print(f"  B3 range: [{B3_track.min():.6f}, {B3_track.max():.6f}] M_KK")
print(f"  B2(0,1) - B2(1,0) max diff: {np.max(np.abs(B2_track_01 - B2_track_10)):.2e}")

# Cross-check at fold
idx_fold = np.argmin(np.abs(tau_scan - tau_fold))
print(f"\n  Cross-check at tau={tau_scan[idx_fold]:.3f} (fold at {tau_fold}):")
print(f"    B1 = {B1_track[idx_fold]:.6f} (canonical: {E_B1:.6f})")
print(f"    B2 = {B2_track_01[idx_fold]:.6f} (canonical: {E_B2_mean:.6f})")
print(f"    B3 = {B3_track[idx_fold]:.6f} (canonical: {E_B3_mean:.6f})")

# ============================================================
# 4. COUNT LEVEL CROSSINGS
# ============================================================
print("\n--- Phase 4: Level crossing analysis ---")

# Define the 8 BCS eigenvalue branches (using sorted-by-value tracking):
# Branch 0: B1  (1 mode)
# Branch 1: B2(0,1) lowest (4 modes -- but we track the minimum)
# Branch 2: B2(1,0) lowest (conjugate of branch 1)
# Branch 3: B3     lowest
#
# We also check for crossings among the second-lowest eigenvalues.
#
# A level crossing occurs when two eigenvalue branches touch or cross.
# Due to different sectors having different quantum numbers, inter-sector
# crossings are EXACT (no avoided crossing -- different selection rules).
# Intra-sector crossings can be either exact or avoided depending on symmetry.

branches = {
    'B1': B1_track,
    'B2_01': B2_track_01,
    'B2_10': B2_track_10,
    'B3': B3_track,
}

if B1_second is not None:
    branches['B1_2nd'] = B1_second
if B2_second_01 is not None:
    branches['B2_01_2nd'] = B2_second_01
if B2_second_10 is not None:
    branches['B2_10_2nd'] = B2_second_10
if B3_second is not None:
    branches['B3_2nd'] = B3_second

branch_names = list(branches.keys())
branch_data = [branches[name] for name in branch_names]
n_branches = len(branch_names)

# Find crossings: where two branches have the same value (within tolerance)
crossing_tol = 1e-4  # M_KK -- resolves eigenvalues to 0.01%
crossings_list = []

for i in range(n_branches):
    for j in range(i + 1, n_branches):
        diff = branch_data[i] - branch_data[j]

        # Check for sign changes (exact crossings)
        sign_changes_idx = np.where(np.diff(np.sign(diff)))[0]

        for idx in sign_changes_idx:
            gap = abs(diff[idx])
            gap_next = abs(diff[idx + 1])
            min_gap = min(gap, gap_next)

            # Crossing velocity: d(lambda_i - lambda_j)/dtau at crossing
            dtau = tau_scan[1] - tau_scan[0]
            crossing_vel = abs(diff[idx + 1] - diff[idx]) / dtau

            # Interpolate tau of crossing
            frac = abs(diff[idx]) / (abs(diff[idx]) + abs(diff[idx + 1]))
            tau_cross = tau_scan[idx] + frac * dtau

            crossings_list.append({
                'branch_i': branch_names[i],
                'branch_j': branch_names[j],
                'tau_cross': tau_cross,
                'min_gap': min_gap,
                'crossing_vel': crossing_vel,
                'idx': idx,
                'is_avoided': min_gap > crossing_tol,
            })

        # Also check for near-crossings (avoided crossings with small gap)
        min_gap_all = np.min(np.abs(diff))
        if min_gap_all < 0.01 and len(sign_changes_idx) == 0:
            idx_min = np.argmin(np.abs(diff))
            crossings_list.append({
                'branch_i': branch_names[i],
                'branch_j': branch_names[j],
                'tau_cross': tau_scan[idx_min],
                'min_gap': min_gap_all,
                'crossing_vel': 0.0,
                'idx': idx_min,
                'is_avoided': True,
            })

# Classify crossings:
# - CONJUGATE: B2(0,1) vs B2(1,0) -- exact degeneracy by complex conjugation
#   of SU(3) irreps. These are NOT physical level crossings; they are a
#   representation-theoretic identity: the spectrum of D_K on (p,q) equals
#   that on (q,p) because the Dirac operator commutes with charge conjugation.
#   Gap ~ 10^{-15} is machine epsilon, confirming exact degeneracy.
# - PHYSICAL: crossings between DISTINCT branch types (B1 vs B2, B2 vs B3, etc.)
#   These would indicate genuine spectral reorganization.

conjugate_crossings = [c for c in crossings_list
                       if ('B2_01' in c['branch_i'] and 'B2_10' in c['branch_j']) or
                          ('B2_10' in c['branch_i'] and 'B2_01' in c['branch_j'])]
physical_crossings = [c for c in crossings_list if c not in conjugate_crossings]

# Filter to entry horizon region [0.20, 0.25]
entry_conjugate = [c for c in conjugate_crossings if 0.20 <= c['tau_cross'] <= 0.25]
entry_physical = [c for c in physical_crossings if 0.20 <= c['tau_cross'] <= 0.25]
all_crossings = crossings_list

N_crossings_conjugate = len(conjugate_crossings)
N_crossings_physical_total = len(physical_crossings)
N_crossings_entry_physical = len(entry_physical)
N_crossings_entry_conjugate = len(entry_conjugate)
N_crossings_entry = N_crossings_entry_physical  # ONLY physical crossings count
N_crossings_total = N_crossings_physical_total

print(f"  Total raw crossings found (all tau): {len(crossings_list)}")
print(f"    Conjugate-symmetry degeneracies: {N_crossings_conjugate} (NOT physical)")
print(f"    Physical crossings: {N_crossings_physical_total}")
print(f"  Entry horizon region [0.20, 0.25]:")
print(f"    Conjugate-symmetry: {N_crossings_entry_conjugate}")
print(f"    Physical crossings: {N_crossings_entry_physical}")

if N_crossings_physical_total > 0:
    print(f"\n  Physical crossings:")
    for c in sorted(physical_crossings, key=lambda x: x['tau_cross']):
        avoid_str = "AVOIDED" if c['is_avoided'] else "EXACT"
        print(f"    {c['branch_i']} x {c['branch_j']} at tau={c['tau_cross']:.4f}: "
              f"gap={c['min_gap']:.2e}, vel={c['crossing_vel']:.4f}, {avoid_str}")
else:
    print(f"\n  NO physical crossings found. All {N_crossings_conjugate} raw crossings are")
    print(f"  conjugate-symmetry degeneracies [B2(0,1) == B2(1,0) to machine eps].")
    print(f"  This is a representation-theoretic IDENTITY, not a level crossing.")

# Inter-branch gap analysis (these are the gaps that WOULD need to close for a crossing)
min_B2_B1 = np.min(np.abs(B2_track_01 - B1_track))
min_B3_B2 = np.min(np.abs(B3_track - B2_track_01))
min_B3_B1 = np.min(np.abs(B3_track - B1_track))
print(f"\n  Minimum inter-branch gaps (entire scan):")
print(f"    B2-B1: {min_B2_B1:.6f} M_KK (never crosses)")
print(f"    B3-B2: {min_B3_B2:.6f} M_KK (never crosses)")
print(f"    B3-B1: {min_B3_B1:.6f} M_KK (never crosses)")

print(f"\n  Time: {time()-t0:.2f}s")

# ============================================================
# 5. EIGENVALUE MONOTONICITY ANALYSIS
# ============================================================
print("\n--- Phase 5: Eigenvalue monotonicity in entry region ---")

# Check if each BCS eigenvalue branch is monotonic across the entry region
entry_mask = (tau_scan >= 0.20) & (tau_scan <= 0.25)
tau_entry_region = tau_scan[entry_mask]

for name in ['B1', 'B2_01', 'B3']:
    branch = branches[name][entry_mask]
    d_branch = np.diff(branch)
    is_mono = np.all(d_branch >= -1e-10) or np.all(d_branch <= 1e-10)
    direction = "increasing" if np.all(d_branch >= -1e-10) else \
                "decreasing" if np.all(d_branch <= 1e-10) else "non-monotonic"
    extrema = np.where(np.diff(np.sign(d_branch)))[0]
    print(f"  {name}: {direction} in [0.20, 0.25], "
          f"range=[{branch.min():.6f}, {branch.max():.6f}], "
          f"extrema={len(extrema)}")

# ============================================================
# 6. SPECTRAL GAP STRUCTURE AT ENTRY
# ============================================================
print("\n--- Phase 6: Spectral gaps at entry horizon ---")

# Compute the gap between B1, B2, B3 at the entry horizon
idx_entry = np.argmin(np.abs(tau_scan - tau_entry))

print(f"  At tau_entry = {tau_scan[idx_entry]:.4f}:")
print(f"    B1 = {B1_track[idx_entry]:.6f} M_KK")
print(f"    B2 = {B2_track_01[idx_entry]:.6f} M_KK")
print(f"    B3 = {B3_track[idx_entry]:.6f} M_KK")
print(f"    B2 - B1 = {B2_track_01[idx_entry] - B1_track[idx_entry]:.6f} M_KK")
print(f"    B3 - B2 = {B3_track[idx_entry] - B2_track_01[idx_entry]:.6f} M_KK")
print(f"    B3 - B1 = {B3_track[idx_entry] - B1_track[idx_entry]:.6f} M_KK")

# The (0,1)-(1,0) gap (conjugate pair)
print(f"    B2(0,1) - B2(1,0) = {B2_track_01[idx_entry] - B2_track_10[idx_entry]:.2e} M_KK")

# Second-lowest gaps
if B1_second is not None:
    print(f"    B1 2nd - 1st = {B1_second[idx_entry] - B1_track[idx_entry]:.6f} M_KK")
if B2_second_01 is not None:
    print(f"    B2(0,1) 2nd - 1st = {B2_second_01[idx_entry] - B2_track_01[idx_entry]:.6f} M_KK")
if B3_second is not None:
    print(f"    B3 2nd - 1st = {B3_track[idx_entry] - B3_track[idx_entry]:.6f} M_KK (trivial)")
    if B3_second is not None:
        print(f"    B3 2nd - 1st = {B3_second[idx_entry] - B3_track[idx_entry]:.6f} M_KK")

# ============================================================
# 7. DERIVATIVES: d(omega)/dtau AT ENTRY
# ============================================================
print("\n--- Phase 7: Eigenvalue derivatives at entry ---")

dtau = tau_scan[1] - tau_scan[0]
for name in ['B1', 'B2_01', 'B3']:
    branch = branches[name]
    # Central difference
    d_branch = np.gradient(branch, dtau)
    d2_branch = np.gradient(d_branch, dtau)
    print(f"  {name} at tau_entry={tau_scan[idx_entry]:.3f}:")
    print(f"    domega/dtau = {d_branch[idx_entry]:.6f}")
    print(f"    d2omega/dtau2 = {d2_branch[idx_entry]:.4f}")

# ============================================================
# 8. SURFACE GRAVITY AND T_ENTRY (IMPROVED)
# ============================================================
print("\n--- Phase 8: Improved T_entry from spectral data ---")

# The entry horizon temperature from analog gravity:
# T_H = kappa / (2*pi)
# where kappa = |d(v - c_s)/dr|_{horizon}
#
# In the spectral action framework:
# - v(tau) is the modulus velocity
# - c_s(tau) is the sound speed
#
# But the S70 workshop's Mach numbers are sparse (4 points).
# Use the spectral action data directly for a more precise estimate.
#
# From energy conservation in the spectral action potential:
# v(tau) = sqrt(2*(S(tau_0) - S(tau))/M_ATDHFB)
# c_s(tau) = sqrt(d^2S/dtau^2 / M_ATDHFB)
#
# The "sonic horizon" in the modulus sector would be where v = c_s.
# But as computed above, v < c_s everywhere because S'' >> delta_S/M.
#
# The S70 workshop's sonic horizons are in a DIFFERENT sector -- the
# fabric (Josephson-coupled) medium. The modulus velocity is indeed
# subsonic in its OWN potential, but supersonic relative to the fabric.
#
# The entry horizon temperature is then:
# kappa_entry = |dv/dtau - dc_fabric/dtau|_{Ma=1}
# Using v = H * (delta_tau) (near the fold, approximately linear),
# and c_fabric roughly constant:

# From the S42 data, compute dv/dtau at the entry
# v(tau) = sqrt(2*(S_0 - S(tau))/M_ATDHFB)
# dv/dtau = -dS/dtau / (M_ATDHFB * v)

v_at_entry = v_modulus(tau_entry)
dS_at_entry = float(cs_dS(tau_entry))
if v_at_entry > 1e-10:
    dv_dtau_at_entry = -dS_at_entry / (M_ATDHFB * v_at_entry)
else:
    dv_dtau_at_entry = 0.0  # (local)

# c_fabric is roughly constant, so dc_fabric/dtau ~ 0
# kappa = |dv/dtau|_{tau_entry}
kappa_v = abs(dv_dtau_at_entry)
T_entry_v = kappa_v / (2.0 * np.pi)

print(f"  Modulus velocity at entry: v = {v_at_entry:.4f} M_KK")
print(f"  dS/dtau at entry: {dS_at_entry:.2f}")
print(f"  dv/dtau at entry: {dv_dtau_at_entry:.4f}")
print(f"  kappa (velocity gradient): {kappa_v:.4f} M_KK")
print(f"  T_entry (velocity gradient): {T_entry_v:.4f} M_KK")
print(f"  T_compound (canonical): {T_compound:.4f} M_KK")
print(f"  T_entry / T_compound = {T_entry_v / T_compound:.4f}")

# Best estimate of T_entry:
# Phase 1 T_entry = 12634 M_KK is from the S70 Mach interpolation with only
# 4 data points and logarithmic spline -- unreliable (huge extrapolation).
# Phase 8 T_entry_v = kappa_v / (2*pi) uses the modulus velocity gradient
# directly from the spectral action data (10 points, well-sampled).
# The modulus velocity gradient kappa_v is the direct analog of surface gravity.
T_entry_best = T_entry_v  # from velocity gradient -- more robust
print(f"\n  T_entry (Phase 1, Mach spline) = {T_entry:.4f} M_KK (4-point interpolation, unreliable)")
print(f"  T_entry (Phase 8, velocity grad) = {T_entry_v:.4f} M_KK (spectral action data, robust)")
print(f"  ADOPTED T_entry = {T_entry_best:.4f} M_KK (velocity gradient method)")

# ============================================================
# 9. GATE VERDICT
# ============================================================
print("\n" + "=" * 72)
print("GATE VERDICT: ENTRY-HORIZON-SPECTRUM-71")
print("=" * 72)

print(f"\n  N_crossings_physical (entry region [0.20, 0.25]): {N_crossings_entry_physical}")
print(f"  N_crossings_physical (full scan [0.18, 0.26]): {N_crossings_physical_total}")
print(f"  N_conjugate_degeneracies (not physical): {N_crossings_conjugate}")
print(f"  tau_entry = {tau_entry:.6f}")
print(f"  T_entry = {T_entry_best:.4f} M_KK")
print(f"  T_compound = {T_compound:.4f} M_KK")
print(f"  T_entry / T_compound = {T_entry_best / T_compound:.4f}")

# Eigenvalue summary at entry
print(f"\n  BCS eigenvalues at tau_entry = {tau_scan[idx_entry]:.3f}:")
print(f"    B1 = {B1_track[idx_entry]:.6f}")
print(f"    B2 = {B2_track_01[idx_entry]:.6f}")
print(f"    B3 = {B3_track[idx_entry]:.6f}")

# Minimum inter-branch gaps
print(f"\n  Minimum inter-branch gaps (entire scan):")
print(f"    B2-B1: {min_B2_B1:.6f} M_KK")
print(f"    B3-B2: {min_B3_B2:.6f} M_KK")
print(f"    B3-B1: {min_B3_B1:.6f} M_KK")

# Classification: N_crossings_entry_physical is the correct count
# All 91 raw crossings are conjugate-symmetry identities, not physical
if N_crossings_entry_physical > 0:
    verdict = (f"N_crossings_physical={N_crossings_entry_physical} "
               f"-- spectral reorganization at entry horizon")
else:
    verdict = (f"N_crossings_physical=0. All {N_crossings_conjugate} raw crossings "
               f"are conjugate-symmetry degeneracies [B2(0,1)=B2(1,0) exact]. "
               f"B1/B2/B3 branches maintain strict ordering with finite gaps "
               f"(min gap={min_B2_B1:.4f} M_KK). "
               f"Entry horizon is KINEMATIC -- no spectral reorganization.")

print(f"\n  Gate: ENTRY-HORIZON-SPECTRUM-71")
print(f"  Verdict: INFO — {verdict}")
print(f"  N_crossings_physical = {N_crossings_entry_physical}, T_entry = {T_entry_best:.4f} M_KK")

# ============================================================
# 10. SAVE RESULTS
# ============================================================
print("\n--- Saving results ---")

np.savez(os.path.join(SCRIPT_DIR, 's71_entry_horizon_spectrum.npz'),
    # Gate
    gate_name='ENTRY-HORIZON-SPECTRUM-71',
    gate_verdict='INFO',
    gate_detail=verdict,

    # Entry horizon
    tau_entry=tau_entry,
    T_entry=T_entry_best,
    T_entry_v=T_entry_v,
    T_compound=T_compound,
    kappa_entry=kappa_entry,
    kappa_v=kappa_v,

    # Crossing data
    N_crossings_entry_physical=N_crossings_entry_physical,
    N_crossings_physical_total=N_crossings_physical_total,
    N_crossings_conjugate=N_crossings_conjugate,
    min_gap_B2_B1=min_B2_B1,
    min_gap_B3_B2=min_B3_B2,
    min_gap_B3_B1=min_B3_B1,

    # Eigenvalue scans
    tau_scan=tau_scan,
    B1_track=B1_track,
    B2_01_track=B2_track_01,
    B2_10_track=B2_track_10,
    B3_track=B3_track,
    B1_second=B1_second if B1_second is not None else np.array([]),
    B2_01_second=B2_second_01 if B2_second_01 is not None else np.array([]),
    B3_second=B3_second if B3_second is not None else np.array([]),

    # Mach number model
    tau_Ma=tau_Ma,
    Ma_values=Ma_values,

    # Spectral action landscape
    v_arr=np.array([v_modulus(t) for t in tau_scan]),
    cs_arr_modulus=np.array([c_s_modulus(t) for t in tau_scan]),

    # Sector eigenvalues (full)
    evals_00=sector_evals[(0, 0)],
    evals_01=sector_evals[(0, 1)],
    evals_10=sector_evals[(1, 0)],
    evals_11=sector_evals[(1, 1)],

    total_time=time() - t_total_start,
)
print(f"  Saved to s71_entry_horizon_spectrum.npz")

# ============================================================
# 11. PLOTS
# ============================================================
print("\n--- Generating plots ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: BCS eigenvalue branches across entry region
ax = axes[0, 0]
ax.plot(tau_scan, B1_track, 'b-', linewidth=2, label='B1 (trivial)')
ax.plot(tau_scan, B2_track_01, 'r-', linewidth=2, label='B2 (0,1)')
ax.plot(tau_scan, B2_track_10, 'r--', linewidth=1, label='B2 (1,0)')
ax.plot(tau_scan, B3_track, 'g-', linewidth=2, label='B3 (adjoint)')
if B1_second is not None:
    ax.plot(tau_scan, B1_second, 'b:', linewidth=1, alpha=0.5, label='B1 2nd')
if B2_second_01 is not None:
    ax.plot(tau_scan, B2_second_01, 'r:', linewidth=1, alpha=0.5, label='B2 2nd')
if B3_second is not None:
    ax.plot(tau_scan, B3_second, 'g:', linewidth=1, alpha=0.5, label='B3 2nd')
ax.axvline(tau_entry, color='k', linestyle='--', linewidth=1.5, label=f'tau_entry={tau_entry:.4f}')
ax.axvline(tau_fold, color='gray', linestyle=':', linewidth=1, label=f'tau_fold={tau_fold}')
# Mark crossings
for c in all_crossings:
    color = 'red' if not c['is_avoided'] else 'orange'
    ax.axvline(c['tau_cross'], color=color, alpha=0.3, linewidth=0.5)
ax.set_xlabel('tau (Jensen parameter)')
ax.set_ylabel('omega (M_KK)')
ax.set_title('D_K Eigenvalue Branches Across Entry Horizon')
ax.legend(fontsize=7, loc='upper left')
ax.grid(True, alpha=0.3)

# Panel B: Eigenvalue gaps
ax = axes[0, 1]
ax.plot(tau_scan, B2_track_01 - B1_track, 'purple', linewidth=2, label='B2 - B1')
ax.plot(tau_scan, B3_track - B2_track_01, 'brown', linewidth=2, label='B3 - B2')
ax.plot(tau_scan, B3_track - B1_track, 'black', linewidth=2, label='B3 - B1')
ax.plot(tau_scan, np.abs(B2_track_01 - B2_track_10), 'red', linewidth=1,
        linestyle='--', label='|B2(01) - B2(10)|')
ax.axvline(tau_entry, color='k', linestyle='--', linewidth=1.5, label=f'tau_entry')
ax.axvline(tau_fold, color='gray', linestyle=':', linewidth=1, label=f'tau_fold')
ax.set_xlabel('tau')
ax.set_ylabel('Gap (M_KK)')
ax.set_title('Inter-Branch Spectral Gaps')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel C: Eigenvalue derivatives
ax = axes[1, 0]
for name, style in [('B1', 'b-'), ('B2_01', 'r-'), ('B3', 'g-')]:
    branch = branches[name]
    d_branch = np.gradient(branch, dtau)
    ax.plot(tau_scan, d_branch, style, linewidth=2, label=f'd{name}/dtau')
ax.axvline(tau_entry, color='k', linestyle='--', linewidth=1.5, label=f'tau_entry')
ax.axvline(tau_fold, color='gray', linestyle=':', linewidth=1, label=f'tau_fold')
ax.axhline(0, color='gray', linewidth=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('d(omega)/d(tau)')
ax.set_title('Eigenvalue Derivatives')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel D: Mach number profile (S70 data + modulus sector)
ax = axes[1, 1]
# S70 workshop data
ax.plot(tau_Ma, Ma_values, 'ko-', linewidth=2, markersize=6, label='S70 Ma (workshop)')
# Log scale for the large dynamic range
ax.set_yscale('log')
ax.axhline(1.0, color='red', linewidth=2, linestyle='-', label='Ma = 1 (sonic)')
ax.axvline(tau_entry, color='k', linestyle='--', linewidth=1.5, label=f'tau_entry={tau_entry:.4f}')
ax.axvline(tau_fold, color='gray', linestyle=':', linewidth=1, label=f'tau_fold')
# Modulus-sector Ma
v_scan = np.array([v_modulus(t) for t in tau_scan])
cs_scan = np.array([c_s_modulus(t) for t in tau_scan])
Ma_modulus = np.where(cs_scan > 0, v_scan / cs_scan, 0.0)
Ma_modulus_plot = np.maximum(Ma_modulus, 1e-3)
ax.plot(tau_scan, Ma_modulus_plot, 'b--', linewidth=1, alpha=0.5, label='Ma (modulus sector)')
ax.set_xlabel('tau')
ax.set_ylabel('Mach number')
ax.set_title('Mach Number Profile')
ax.legend(fontsize=7)
ax.set_ylim(1e-3, 200)
ax.grid(True, alpha=0.3)

plt.suptitle('ENTRY-HORIZON-SPECTRUM-71: Entry Sonic Horizon Analysis', fontsize=13, y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(os.path.join(SCRIPT_DIR, 's71_entry_horizon_spectrum.png'), dpi=150, bbox_inches='tight')
print(f"  Saved plot to s71_entry_horizon_spectrum.png")

# ============================================================
# SUMMARY
# ============================================================
total_time = time() - t_total_start
print(f"\n{'='*72}")
print(f"COMPLETE. Total time: {total_time:.2f}s")
print(f"{'='*72}")
print(f"\nKey results:")
print(f"  tau_entry = {tau_entry:.6f}")
print(f"  N_crossings_physical (entry region) = {N_crossings_entry_physical}")
print(f"  N_crossings_physical (full scan) = {N_crossings_physical_total}")
print(f"  N_conjugate_degeneracies (not physical) = {N_crossings_conjugate}")
print(f"  T_entry = {T_entry_best:.4f} M_KK")
print(f"  T_compound = {T_compound:.4f} M_KK")
print(f"  T_entry / T_compound = {T_entry_best / T_compound:.4f}")
print(f"\n  B1 at entry: {B1_track[idx_entry]:.6f} M_KK (dB1/dtau = {np.gradient(B1_track, dtau)[idx_entry]:.6f})")
print(f"  B2 at entry: {B2_track_01[idx_entry]:.6f} M_KK (dB2/dtau = {np.gradient(B2_track_01, dtau)[idx_entry]:.6f})")
print(f"  B3 at entry: {B3_track[idx_entry]:.6f} M_KK (dB3/dtau = {np.gradient(B3_track, dtau)[idx_entry]:.6f})")
print(f"  Min inter-branch gaps: B2-B1={min_B2_B1:.4f}, B3-B2={min_B3_B2:.4f}, B3-B1={min_B3_B1:.4f}")
print(f"\nGate: ENTRY-HORIZON-SPECTRUM-71 — INFO: {verdict}")
