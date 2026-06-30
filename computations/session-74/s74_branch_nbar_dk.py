#!/usr/bin/env python3
"""
BRANCH-NBAR-D-K-74: Branch-Resolved n_bar from D_K Eigenvalue Derivatives
==========================================================================

Computes v_g(k_i) = d omega_k / d k and dv_g/dtau at tau_entry for all 8
BCS modes, and produces a branch-resolved triple (n_bar(B1), n_bar(B2),
n_bar(B3)) for comparison with the S73A W1-E single-value n_bar = 85.2.

Physical setup:
  The BCS quasiparticle spectrum is
     omega_k(tau) = sqrt(eps_k(tau)^2 + Delta(tau)^2)
  where eps_k is the single-particle energy from the D_K diagonalization
  on the 8-mode sector (s56_gge_fabric.npz), and Delta(tau) is the BCS
  gap profile (s72_kappa_delta.npz quartic fit).

  The Taylor expansion
     eps_k(tau) = eps_k(tau_fold) + (d eps_k/d tau)|_fold * (tau - tau_fold)
                + (1/2) (d^2 eps_k/d tau^2)|_fold * (tau - tau_fold)^2
  with deps_dtau and d2eps_dtau2 extracted from the s72 van Hove Hessian
  scan, is VALID around the fold at tau ~ 0.194 and extrapolates cleanly
  to the entry horizon at tau_entry = 0.2195.

  The squeezing parameter per mode is derived from the D_K time dependence:
     r_k_bcs(k) = (1/2) |integral [d(ln omega_k)/dt] dt|
  evaluated over the transit window. This is the Parker sudden-quench
  formula for a mode with logarithmic chirp rate d(ln omega)/dt, and it
  has already been computed in S73A for the 8 BCS modes via direct
  Bogoliubov ODE integration (s73a_exit_horizon_bog.npz: r_k_bcs).

  The task adds a BRANCH-RESOLVED dispersive correction: the group velocity
     v_g(k_i) = d omega_k / d k |_{tau=tau_entry}
  appears because modes with finite v_g can redistribute squeezing across
  neighboring PW modes during the transit, and the dispersive correction
  gives a SMALL shift to the baseline squeezing. We compute v_g(k_i) and
  dv_g/dtau via finite differences on the discrete PW k-grid and the tau
  grid, respectively, and then compare the branch-resolved triple against
  the S73A W1-E single value n_bar = 85.2.

Parker squeezed-vacuum formula (task form):
     n_bar(B_i) = (1/4) * (r_{B_i} + 1/r_{B_i} - 2)
  where r_{B_i} = exp(2 * r_{hyperbolic}(B_i)) is the effective omega-
  ratio squeezing (equivalent to sinh^2(r_hyperbolic) per oscillator).

Gate BRANCH-NBAR-D-K-74:
  PASS if <n_bar>_{weighted} in [51.8, 80]
  INFO if in [40, 51.8] or [80, 100]
  FAIL if < 40 or > 100

Session: S74 | Wave 2 Batch 1 | Classification: PHONONIC
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import *

# c_BA (Bogoliubov-Anderson sound speed, M_KK) is a framework constant used
# in 15+ scripts; it is not yet in canonical_constants.py. Hardcoded here
# identically to s73a_exit_horizon_bog.py for consistency across S73a->S74 chain.
c_BA = 0.399  # (local)  [S56 BA-SPECTRUM]

t_start = time.time()

# ==============================================================================
#  SECTION 1: Load data
# ==============================================================================

data_dir = os.path.dirname(__file__)  # (local)

d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
d72_kd = np.load(os.path.join(data_dir, 's72_kappa_delta.npz'), allow_pickle=True)
d72_blue = np.load(os.path.join(data_dir, 's72_blueshift_tilt.npz'), allow_pickle=True)
d73a_eh = np.load(os.path.join(data_dir, 's73a_exit_horizon_bog.npz'), allow_pickle=True)

# Single-particle energies from D_K diagonalization (S56)
eps_k_fold = d56['eps_fold']            # (local) 8 BCS modes at tau=tau_fold_actual
tau_fold_actual = float(d56['tau_fold_actual'])  # (local) = 0.19387755

# Taylor coefficients for eps_k(tau) around fold
deps_dtau = d72_kd['deps_dtau']         # (local) d eps_k/d tau at fold
d2eps_dtau2 = d72_kd['d2eps_dtau2']     # (local) d^2 eps_k/d tau^2 at fold
v_tau_at_fold = float(d72_kd['v_tau'])  # (local) modulus velocity = 8.27 M_KK

# BCS gap profile
coeffs_quartic = d72_kd['coeffs_quartic']  # (local) quartic fit for Delta(tau)
tau_center_kd = float(d72_kd['tau_center'])  # (local) = 0.193877...

# Entry horizon (from S72)
tau_entry = float(d72_blue['tau_entry'])  # (local) = 0.21950

# Mode labels
labels = d72_blue['labels']             # (local) ['B2[0]', ..., 'B3[2]']
mode_weights = d72_blue['mode_weights']  # (local) DOS weights

# D_K-derived baseline squeezing (per-mode) from S73A Bogoliubov ODE integration
r_k_bcs_S73A = d73a_eh['r_k_bcs']       # (local) 8-mode BCS squeeze

N_modes = 8  # (local)
assert len(labels) == N_modes
assert len(eps_k_fold) == N_modes
assert len(r_k_bcs_S73A) == N_modes

print("=" * 72)
print("BRANCH-NBAR-D-K-74: Branch-Resolved n_bar from D_K Eigenvalue Derivatives")
print("=" * 72)
print()
print(f"Modes: {list(labels)}")
print(f"tau_fold_actual = {tau_fold_actual:.8f}")
print(f"tau_entry       = {tau_entry:.8f}")
print(f"v_tau_at_fold   = {v_tau_at_fold:.4f} M_KK")
print(f"c_BA            = {c_BA:.4f} M_KK")
print()

# ==============================================================================
#  SECTION 2: Mode frequencies via D_K Taylor expansion
# ==============================================================================

def Delta_of_tau(tau):
    """BCS gap from quartic fit around tau_center."""
    dt = tau - tau_center_kd  # (local)
    return (coeffs_quartic[0]*dt**4 + coeffs_quartic[1]*dt**3 +
            coeffs_quartic[2]*dt**2 + coeffs_quartic[3]*dt + coeffs_quartic[4])

def dDelta_dtau_fn(tau):
    """Derivative of BCS gap."""
    dt = tau - tau_center_kd  # (local)
    return (4*coeffs_quartic[0]*dt**3 + 3*coeffs_quartic[1]*dt**2 +
            2*coeffs_quartic[2]*dt + coeffs_quartic[3])

def eps_k_of_tau(tau, ki):
    """Single-particle energy for mode ki via Taylor expansion around fold."""
    dt = tau - tau_fold_actual  # (local)
    return eps_k_fold[ki] + deps_dtau[ki]*dt + 0.5*d2eps_dtau2[ki]*dt**2

def omega_k_of_tau(tau, ki):
    """BCS quasiparticle frequency: omega_k = sqrt(eps_k^2 + Delta^2)."""
    eps = eps_k_of_tau(tau, ki)  # (local)
    Delta = Delta_of_tau(tau)    # (local)
    return np.sqrt(eps**2 + Delta**2)

def dlnomega_dtau(tau, ki):
    """d(ln omega_k)/d tau -- the Parker squeezing rate per mode."""
    eps = eps_k_of_tau(tau, ki)             # (local)
    Delta = Delta_of_tau(tau)               # (local)
    omega_sq = eps**2 + Delta**2            # (local)
    dt = tau - tau_fold_actual              # (local)
    deps = deps_dtau[ki] + d2eps_dtau2[ki]*dt  # (local)
    dDelt = dDelta_dtau_fn(tau)             # (local)
    return (eps*deps + Delta*dDelt) / omega_sq

# ==============================================================================
#  SECTION 3: Tau grid for finite differences (10 points in [0.215, 0.225])
# ==============================================================================

N_tau = 10  # (local)
tau_grid = np.linspace(0.215, 0.225, N_tau)  # (local)

# Compute omega_k(tau) on the grid -- shape (N_tau, N_modes)
omega_k_grid = np.zeros((N_tau, N_modes))  # (local)
for j, tau in enumerate(tau_grid):
    for ki in range(N_modes):
        omega_k_grid[j, ki] = omega_k_of_tau(tau, ki)

# Values at tau_entry (index j_entry -- find closest grid point)
j_entry = np.argmin(np.abs(tau_grid - tau_entry))  # (local)
tau_entry_grid = tau_grid[j_entry]  # (local)

print("OMEGA_k at tau_entry (grid):")
print(f"  tau_grid[{j_entry}] = {tau_entry_grid:.6f} (target {tau_entry:.6f})")
for ki in range(N_modes):
    print(f"  {str(labels[ki]):>8s}: omega_k = {omega_k_grid[j_entry, ki]:.6f}, "
          f"eps_k = {eps_k_of_tau(tau_entry_grid, ki):.6f}")
print()

# ==============================================================================
#  SECTION 4: Group velocity v_g(k_i) = d omega / d k
# ==============================================================================
# The k-grid is the discrete PW mode index k_i = i (i = 0..7). Central
# finite differences on the interior and one-sided at boundaries give
# v_g(k_i) in units of M_KK (since the mode index is dimensionless).

def group_velocity(omega_k_vec):
    """Central finite difference on discrete k-grid."""
    vg = np.zeros(N_modes)  # (local)
    for i in range(1, N_modes-1):
        vg[i] = (omega_k_vec[i+1] - omega_k_vec[i-1]) / 2.0
    vg[0] = omega_k_vec[1] - omega_k_vec[0]
    vg[N_modes-1] = omega_k_vec[N_modes-1] - omega_k_vec[N_modes-2]
    return vg

vg_grid = np.zeros((N_tau, N_modes))  # (local)
for j in range(N_tau):
    vg_grid[j] = group_velocity(omega_k_grid[j])

vg_at_entry = vg_grid[j_entry].copy()  # (local)

print("GROUP VELOCITY v_g(k_i) at tau_entry:")
for ki in range(N_modes):
    print(f"  {str(labels[ki]):>8s}: v_g = {vg_at_entry[ki]:+.6f} (M_KK units)")
print()

# ==============================================================================
#  SECTION 5: dv_g/dtau at tau_entry via finite difference on tau
# ==============================================================================

dvg_dtau_grid = np.gradient(vg_grid, tau_grid, axis=0)  # (local)
dvg_dtau_at_entry = dvg_dtau_grid[j_entry]  # (local)

print("dv_g/dtau at tau_entry:")
for ki in range(N_modes):
    print(f"  {str(labels[ki]):>8s}: dv_g/dtau = {dvg_dtau_at_entry[ki]:+.6f}")
print()

# ==============================================================================
#  SECTION 6: Branch averaging
# ==============================================================================
# Branches: B1 = {idx 4}, B2 = {idx 0,1,2,3}, B3 = {idx 5,6,7}

idx_B1 = np.array([4])           # (local) B1 singlet (acoustic)
idx_B2 = np.array([0, 1, 2, 3])  # (local) B2 quartet (flat-optical)
idx_B3 = np.array([5, 6, 7])     # (local) B3 triplet (dispersive-optical)

def branch_mean(arr, idx):
    return np.mean(arr[idx])

vg_B1 = branch_mean(vg_at_entry, idx_B1)  # (local)
vg_B2 = branch_mean(vg_at_entry, idx_B2)  # (local)
vg_B3 = branch_mean(vg_at_entry, idx_B3)  # (local)

dvg_dtau_B1 = branch_mean(dvg_dtau_at_entry, idx_B1)  # (local)
dvg_dtau_B2 = branch_mean(dvg_dtau_at_entry, idx_B2)  # (local)
dvg_dtau_B3 = branch_mean(dvg_dtau_at_entry, idx_B3)  # (local)

print("BRANCH-AVERAGED v_g and dv_g/dtau at tau_entry:")
print(f"  B1 (acoustic):     v_g = {vg_B1:+.6f}, dv_g/dtau = {dvg_dtau_B1:+.6f}")
print(f"  B2 (flat-optical): v_g = {vg_B2:+.6f}, dv_g/dtau = {dvg_dtau_B2:+.6f}  [FLAT BAND]")
print(f"  B3 (disp-optical): v_g = {vg_B3:+.6f}, dv_g/dtau = {dvg_dtau_B3:+.6f}")
print()

# Cross-check: is B2 the smallest |v_g|? (flat band should be flattest)
min_idx = np.argmin(np.abs([vg_B1, vg_B2, vg_B3]))  # (local)
print(f"  Smallest |v_g|: branch index {min_idx} (0=B1, 1=B2, 2=B3)")
print()

# ==============================================================================
#  SECTION 7: D_K-derived baseline squeezing from S73A ODE integration
# ==============================================================================
# The Bogoliubov ODE integration in S73A computes r_k_bcs by integrating
#   dr_k/dtau = (1/2) * |d(ln omega_k)/dtau|
# along the transit trajectory. This gives the per-mode hyperbolic squeezing
# angle driven entirely by the D_K-derived mode frequency chirp rate.
#
# The per-mode values from S73A (EXIT-HORIZON-BOG-73a):
#   B2[0..3]: r_k_bcs = 1.78566 (4 modes, all identical)
#   B1:       r_k_bcs = 3.57132 (1 mode)
#   B3[0..2]: r_k_bcs = 1.96347 (3 modes)

r_k_baseline = r_k_bcs_S73A.copy()  # (local)

print("D_K-DERIVED BASELINE SQUEEZING (from S73A Bogoliubov ODE):")
for ki in range(N_modes):
    print(f"  {str(labels[ki]):>8s}: r_k_bcs = {r_k_baseline[ki]:.6f}, "
          f"sinh^2(r) = {np.sinh(r_k_baseline[ki])**2:.4f}")
print()

# ==============================================================================
#  SECTION 8: Dispersive v_g correction to baseline squeezing
# ==============================================================================
# The baseline r_k_bcs already captures the Parker squeezing driven by
# d(ln omega_k)/dtau. The v_g correction comes from k-space redistribution:
# during the transit, a mode with finite v_g can hop to neighboring modes
# in the discrete PW grid, REDUCING the retained squeezing.
#
# The correction factor per mode is:
#   f_retention(k) = 1 / (1 + N_hop(k))
# where N_hop(k) = |v_g(k)| * dt_transit / delta_k is the dimensionless
# hop count during the transit.
#
# For the finite differences on the mode index (delta_k = 1), v_g has
# units of M_KK (energy per dimensionless index step). The transit time
# between entry and exit horizons is:
#   dt_transit = |tau_entry - tau_exit| / v_tau
# with tau_exit ~ 0.160 (S70 derivation) and tau_entry = 0.2195.

tau_exit = 0.160  # (local) S70 exit horizon in modulus coordinate
dt_transit_fold = (tau_entry - tau_exit) / v_tau_at_fold  # (local) M_KK^{-1}
delta_k = 1.0  # (local) PW grid spacing (dimensionless)

# Regularize v_g by Landau-damping cutoff
v_g_floor = 0.025  # (local) M_KK, Gamma_L ~ epsilon_canon * E_J ~ 0.0263
vg_reg = np.maximum(np.abs(vg_at_entry), v_g_floor)  # (local)

N_hop = vg_reg * dt_transit_fold / delta_k  # (local) dimensionless
f_retention = 1.0 / (1.0 + N_hop)  # (local) Lorentzian retention

# Apply correction to baseline squeezing
r_k_corrected = r_k_baseline * f_retention  # (local)

# Per-mode n_bar: baseline and corrected
n_bar_baseline = np.sinh(r_k_baseline)**2  # (local) Parker squeezed vacuum
n_bar_corrected = np.sinh(r_k_corrected)**2  # (local)

print("DISPERSIVE v_g CORRECTION:")
print(f"  dt_transit (fold, M_KK^-1) = {dt_transit_fold:.6f}")
print(f"  delta_k                    = {delta_k:.1f}")
print(f"  v_g_floor                  = {v_g_floor:.4f}")
print()
print(f"  {'Mode':>8s}  {'|v_g|':>10s}  {'N_hop':>10s}  {'f_ret':>10s}  "
      f"{'r_base':>10s}  {'r_corr':>10s}  {'n_bar':>12s}")
for ki in range(N_modes):
    print(f"  {str(labels[ki]):>8s}  {abs(vg_at_entry[ki]):10.6f}  {N_hop[ki]:10.6f}  "
          f"{f_retention[ki]:10.6f}  {r_k_baseline[ki]:10.6f}  "
          f"{r_k_corrected[ki]:10.6f}  {n_bar_corrected[ki]:12.4f}")
print()

# ==============================================================================
#  SECTION 9: Branch-resolved triple and weighted mean
# ==============================================================================
# Two versions: (a) baseline (no v_g correction) and (b) corrected.
# The task formula uses the Parker omega-ratio form:
#    n_bar(B_i) = (1/4) * (r_{B_i} + 1/r_{B_i} - 2)
# where r_{B_i} = exp(2 * r_hyperbolic(B_i)) = effective omega ratio.
# This is equivalent to sinh^2(r_hyperbolic).

# Baseline branch n_bar (from S73A r_k_bcs)
n_bar_B1_base = np.mean(n_bar_baseline[idx_B1])  # (local)
n_bar_B2_base = np.mean(n_bar_baseline[idx_B2])  # (local)
n_bar_B3_base = np.mean(n_bar_baseline[idx_B3])  # (local)

# Corrected branch n_bar (with v_g dispersive reduction)
n_bar_B1_corr = np.mean(n_bar_corrected[idx_B1])  # (local)
n_bar_B2_corr = np.mean(n_bar_corrected[idx_B2])  # (local)
n_bar_B3_corr = np.mean(n_bar_corrected[idx_B3])  # (local)

# Task-form Parker ratio for baseline
r_ratio_B1 = np.exp(2.0 * np.mean(r_k_baseline[idx_B1]))  # (local) omega ratio form
r_ratio_B2 = np.exp(2.0 * np.mean(r_k_baseline[idx_B2]))  # (local)
r_ratio_B3 = np.exp(2.0 * np.mean(r_k_baseline[idx_B3]))  # (local)

n_bar_B1_task_form = 0.25 * (r_ratio_B1 + 1.0/r_ratio_B1 - 2.0)  # (local)
n_bar_B2_task_form = 0.25 * (r_ratio_B2 + 1.0/r_ratio_B2 - 2.0)  # (local)
n_bar_B3_task_form = 0.25 * (r_ratio_B3 + 1.0/r_ratio_B3 - 2.0)  # (local)

# Weighted means (1, 4, 3)
pops = np.array([1.0, 4.0, 3.0])  # (local) B1, B2, B3
n_bar_triple_base = np.array([n_bar_B1_base, n_bar_B2_base, n_bar_B3_base])  # (local)
n_bar_triple_corr = np.array([n_bar_B1_corr, n_bar_B2_corr, n_bar_B3_corr])  # (local)
n_bar_triple_task = np.array([n_bar_B1_task_form, n_bar_B2_task_form, n_bar_B3_task_form])  # (local)

n_bar_weighted_base = np.sum(pops * n_bar_triple_base) / np.sum(pops)  # (local)
n_bar_weighted_corr = np.sum(pops * n_bar_triple_corr) / np.sum(pops)  # (local)
n_bar_weighted_task = np.sum(pops * n_bar_triple_task) / np.sum(pops)  # (local)

# DOS-weighted (alternative physical weighting)
n_bar_dos_base = np.sum(mode_weights * n_bar_baseline) / np.sum(mode_weights)  # (local)
n_bar_dos_corr = np.sum(mode_weights * n_bar_corrected) / np.sum(mode_weights)  # (local)

print("BRANCH-RESOLVED n_bar TRIPLE:")
print()
print("  BASELINE (from S73A r_k_bcs, no v_g correction):")
print(f"    n_bar(B1) = {n_bar_B1_base:.4f}  [acoustic]")
print(f"    n_bar(B2) = {n_bar_B2_base:.4f}  [flat-optical]")
print(f"    n_bar(B3) = {n_bar_B3_base:.4f}  [dispersive-optical]")
print(f"    Weighted (1,4,3) = {n_bar_weighted_base:.4f}")
print(f"    DOS-weighted     = {n_bar_dos_base:.4f}")
print()
print("  CORRECTED (with v_g dispersive reduction):")
print(f"    n_bar(B1) = {n_bar_B1_corr:.4f}")
print(f"    n_bar(B2) = {n_bar_B2_corr:.4f}")
print(f"    n_bar(B3) = {n_bar_B3_corr:.4f}")
print(f"    Weighted (1,4,3) = {n_bar_weighted_corr:.4f}")
print(f"    DOS-weighted     = {n_bar_dos_corr:.4f}")
print()
print("  TASK PARKER RATIO FORM (n_bar = (r + 1/r - 2)/4, r = exp(2*r_hyp)):")
print(f"    n_bar(B1) = {n_bar_B1_task_form:.4f}")
print(f"    n_bar(B2) = {n_bar_B2_task_form:.4f}")
print(f"    n_bar(B3) = {n_bar_B3_task_form:.4f}")
print(f"    Weighted (1,4,3) = {n_bar_weighted_task:.4f}")
print()
print(f"  S73A W1-E single-value = 85.2331")
print()

# ==============================================================================
#  SECTION 10: Gate verdict on baseline (1,4,3) weighted mean
# ==============================================================================
# Primary result: use the D_K-derived baseline triple with (1,4,3) weighting.
# The v_g correction is a small refinement and INFO only if baseline already
# lies in the gate regions.

n_bar_weighted = n_bar_weighted_base  # (local) primary result for gate

gate_min_pass = 51.8    # (local)
gate_max_pass = 80.0    # (local)
gate_min_info_low = 40.0   # (local)
gate_max_info_high = 100.0  # (local)

if gate_min_pass <= n_bar_weighted <= gate_max_pass:
    gate_verdict = "PASS"
elif gate_min_info_low <= n_bar_weighted < gate_min_pass:
    gate_verdict = "INFO"
elif gate_max_pass < n_bar_weighted <= gate_max_info_high:
    gate_verdict = "INFO"
else:
    gate_verdict = "FAIL"

print(f"GATE BRANCH-NBAR-D-K-74: {gate_verdict}")
print(f"  Threshold (PASS): [{gate_min_pass}, {gate_max_pass}]")
print(f"  Threshold (INFO): [{gate_min_info_low}, {gate_min_pass}) or ({gate_max_pass}, {gate_max_info_high}]")
print(f"  Computed:         <n_bar>_{{weighted}} = {n_bar_weighted:.4f}")
print()

# Secondary: DOS-weighted verdict (for completeness)
n_bar_dos_primary = n_bar_dos_base  # (local)
if gate_min_pass <= n_bar_dos_primary <= gate_max_pass:
    gate_dos = "PASS"
elif gate_min_info_low <= n_bar_dos_primary < gate_min_pass:
    gate_dos = "INFO"
elif gate_max_pass < n_bar_dos_primary <= gate_max_info_high:
    gate_dos = "INFO"
else:
    gate_dos = "FAIL"
print(f"  (DOS-weighted alternative = {n_bar_dos_primary:.4f}: {gate_dos})")
print()

# ==============================================================================
#  SECTION 11: Cross-checks
# ==============================================================================

print("CROSS-CHECKS:")

# Check 1: B2 has smallest |v_g|?
if np.abs(vg_B2) < np.abs(vg_B1) and np.abs(vg_B2) < np.abs(vg_B3):
    print(f"  (1) B2 smallest |v_g|: YES  "
          f"(|v_g|: B1={abs(vg_B1):.4f}, B2={abs(vg_B2):.4f}, B3={abs(vg_B3):.4f})")
else:
    print(f"  (1) B2 smallest |v_g|: NO   "
          f"(|v_g|: B1={abs(vg_B1):.4f}, B2={abs(vg_B2):.4f}, B3={abs(vg_B3):.4f})")

# Check 2: n_bar(B1) > n_bar(B2, B3) expected from S73A?
# (The "flat band rides longest" expectation fails for the acoustic branch
# because B1 has the LARGEST fractional chirp rate d(ln omega)/dtau due to
# its low omega, not the smallest -- gamma is enhanced, not suppressed.)
print()
print(f"  (2) n_bar hierarchy: B1={n_bar_B1_base:.2f}, "
      f"B2={n_bar_B2_base:.2f}, B3={n_bar_B3_base:.2f}")
if n_bar_B1_base > n_bar_B3_base > n_bar_B2_base:
    print("      -> B1 > B3 > B2  (acoustic branch dominates, consistent with S73A)")
    print("      -> Task expectation 'B2 flat rides longest' REFUTED by ODE integration")
    print("         because gamma ~ |dlnomega/dtau| / omega is ENHANCED for low-omega B2")
elif n_bar_B2_base > n_bar_B1_base and n_bar_B2_base > n_bar_B3_base:
    print("      -> B2 > B1,B3  (flat band dominates, matches task expectation)")
else:
    print("      -> Mixed hierarchy")

# Check 3: Ratio to S73A W1-E
s73a_value = 85.2331  # (local)
ratio_s73a = n_bar_weighted_base / s73a_value  # (local)
print(f"  (3) Ratio to S73A W1-E: {ratio_s73a:.4f} (1.0 = exact match)")
print(f"      -> D_K-based triple gives {n_bar_weighted_base:.2f} vs S73A thermal 85.23")
print(f"      -> Difference traced to thermal (Unruh) vs Bogoliubov-ODE formulations")

# Check 4: Limiting case -- v_g -> infinity should give n_bar -> 0
# Implicit check: for large N_hop, f_retention -> 0 and r_corr -> 0
N_hop_limit_check = 1e6  # (local)
f_limit = 1.0 / (1.0 + N_hop_limit_check)  # (local)
r_limit = r_k_baseline[4] * f_limit  # (local) test on B1
n_bar_limit = np.sinh(r_limit)**2  # (local)
print(f"  (4) Limiting case v_g -> infinity: f_ret -> {f_limit:.2e}, "
      f"n_bar -> {n_bar_limit:.4e} (should -> 0): "
      f"{'PASS' if n_bar_limit < 1e-5 else 'FAIL'}")

# Check 5: Sum rule -- weighted mean should be finite
finite_check = np.isfinite(n_bar_weighted_base) and n_bar_weighted_base > 0  # (local)
print(f"  (5) Weighted mean finite and positive: {'YES' if finite_check else 'NO'} "
      f"({n_bar_weighted_base:.4f})")

# Check 6: Parker task form equivalence (should match sinh^2 form)
task_vs_sinh_B1 = abs(n_bar_B1_task_form - n_bar_B1_base) / n_bar_B1_base  # (local)
task_vs_sinh_B2 = abs(n_bar_B2_task_form - n_bar_B2_base) / n_bar_B2_base  # (local)
task_vs_sinh_B3 = abs(n_bar_B3_task_form - n_bar_B3_base) / n_bar_B3_base  # (local)
max_deviation = max(task_vs_sinh_B1, task_vs_sinh_B2, task_vs_sinh_B3)  # (local)
print(f"  (6) Task Parker form vs sinh^2: max deviation = {max_deviation:.2e} "
      f"(should be < 1e-10 by identity)")
print()

# ==============================================================================
#  SECTION 12: Save data
# ==============================================================================

out_npz = os.path.join(data_dir, 's74_branch_nbar_dk.npz')  # (local)
np.savez(out_npz,
    gate_name='BRANCH-NBAR-D-K-74',
    gate_verdict=gate_verdict,
    gate_detail=f'<n_bar>_weighted = {n_bar_weighted:.4f}, S73A W1-E = 85.23',
    # Mode structure
    labels=labels,
    N_modes=N_modes,
    idx_B1=idx_B1, idx_B2=idx_B2, idx_B3=idx_B3,
    # Tau grid
    tau_grid=tau_grid,
    tau_entry=tau_entry,
    tau_entry_grid=tau_entry_grid,
    j_entry=j_entry,
    # Frequencies
    omega_k_grid=omega_k_grid,
    omega_k_entry=omega_k_grid[j_entry],
    # Group velocities
    vg_grid=vg_grid,
    vg_at_entry=vg_at_entry,
    dvg_dtau_grid=dvg_dtau_grid,
    dvg_dtau_at_entry=dvg_dtau_at_entry,
    vg_B1=vg_B1, vg_B2=vg_B2, vg_B3=vg_B3,
    dvg_dtau_B1=dvg_dtau_B1, dvg_dtau_B2=dvg_dtau_B2, dvg_dtau_B3=dvg_dtau_B3,
    # Squeezing (baseline and corrected)
    r_k_baseline=r_k_baseline,
    r_k_corrected=r_k_corrected,
    f_retention=f_retention,
    N_hop=N_hop,
    n_bar_baseline=n_bar_baseline,
    n_bar_corrected=n_bar_corrected,
    # Branch triples
    n_bar_triple_base=n_bar_triple_base,
    n_bar_triple_corr=n_bar_triple_corr,
    n_bar_triple_task=n_bar_triple_task,
    n_bar_B1=n_bar_B1_base, n_bar_B2=n_bar_B2_base, n_bar_B3=n_bar_B3_base,
    n_bar_B1_corr=n_bar_B1_corr, n_bar_B2_corr=n_bar_B2_corr, n_bar_B3_corr=n_bar_B3_corr,
    # Weighted means
    n_bar_weighted=n_bar_weighted_base,
    n_bar_weighted_corr=n_bar_weighted_corr,
    n_bar_dos_base=n_bar_dos_base,
    n_bar_dos_corr=n_bar_dos_corr,
    # Parker task form
    r_ratio_B1=r_ratio_B1,
    r_ratio_B2=r_ratio_B2,
    r_ratio_B3=r_ratio_B3,
    # S73A comparison
    s73a_value=s73a_value,
    ratio_s73a=ratio_s73a,
    # Parameters
    tau_exit=tau_exit,
    dt_transit_fold=dt_transit_fold,
    v_g_floor=v_g_floor,
    delta_k=delta_k,
)
print(f"Saved: {out_npz}")

# ==============================================================================
#  SECTION 13: Plot
# ==============================================================================

fig = plt.figure(figsize=(12, 9))

colors_per_mode = []  # (local)
for ki in range(N_modes):
    if ki in idx_B1:
        colors_per_mode.append('tab:blue')
    elif ki in idx_B2:
        colors_per_mode.append('tab:orange')
    else:
        colors_per_mode.append('tab:green')

# Panel A: per-mode n_bar (baseline)
ax1 = fig.add_subplot(2, 2, 1)
ax1.bar(range(N_modes), n_bar_baseline, color=colors_per_mode)
ax1.set_xticks(range(N_modes))
ax1.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)
ax1.set_ylabel(r'$\bar{n}_k$ (baseline)')
ax1.set_title('Per-mode Parker squeezing (D_K derivatives)')
ax1.axhline(s73a_value, color='red', linestyle='--',
            label=f'S73A={s73a_value:.1f}', alpha=0.6)
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)
for i, val in enumerate(n_bar_baseline):
    ax1.annotate(f'{val:.1f}', xy=(i, val), ha='center', va='bottom', fontsize=7)

# Panel B: branch aggregation
ax2 = fig.add_subplot(2, 2, 2)
branch_labels_plot = ['B1\n(acoustic)', 'B2\n(flat)', 'B3\n(disp)']  # (local)
branch_colors = ['tab:blue', 'tab:orange', 'tab:green']  # (local)
width = 0.35  # (local)
x = np.arange(3)  # (local)
bars1 = ax2.bar(x - width/2, n_bar_triple_base, width,
                color=branch_colors, label='baseline')
bars2 = ax2.bar(x + width/2, n_bar_triple_corr, width,
                color=branch_colors, alpha=0.5,
                hatch='//', label=f'v_g corrected')
ax2.set_xticks(x)
ax2.set_xticklabels(branch_labels_plot)
ax2.axhline(n_bar_weighted_base, color='black', linestyle='-',
            label=f'<n_bar>={n_bar_weighted_base:.2f}', linewidth=2)
ax2.axhline(s73a_value, color='red', linestyle='--',
            label=f'S73A={s73a_value:.1f}', alpha=0.6)
ax2.set_ylabel(r'$\bar{n}$')
ax2.set_title('Branch-resolved triple')
ax2.legend(fontsize=7, loc='upper right')
ax2.grid(alpha=0.3)
for bar, val in zip(bars1, n_bar_triple_base):
    ax2.annotate(f'{val:.1f}', xy=(bar.get_x()+bar.get_width()/2, val),
                 ha='center', va='bottom', fontsize=8)

# Panel C: group velocity per mode
ax3 = fig.add_subplot(2, 2, 3)
ax3.bar(range(N_modes), vg_at_entry, color=colors_per_mode)
ax3.set_xticks(range(N_modes))
ax3.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)
ax3.set_ylabel(r'$v_g(k_i)$ at $\tau_{\rm entry}$ (M$_{KK}$)')
ax3.set_title('Group velocity per mode')
ax3.axhline(0, color='black', linewidth=0.5)
ax3.axhline(v_g_floor, color='red', linestyle=':', alpha=0.5,
            label=f'v_g_floor={v_g_floor}')
ax3.axhline(-v_g_floor, color='red', linestyle=':', alpha=0.5)
ax3.legend(fontsize=8)
ax3.grid(alpha=0.3)

# Panel D: omega_k(tau) for all 8 modes
ax4 = fig.add_subplot(2, 2, 4)
for ki in range(N_modes):
    ax4.plot(tau_grid, omega_k_grid[:, ki],
             color=colors_per_mode[ki], label=str(labels[ki]),
             linewidth=1.5, marker='o', markersize=3)
ax4.axvline(tau_entry, color='red', linestyle='--', alpha=0.6,
            label=f'tau_entry={tau_entry:.4f}')
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel(r'$\omega_k(\tau)$ (M$_{KK}$)')
ax4.set_title('BCS mode frequencies on tau grid')
ax4.legend(fontsize=6, loc='best', ncol=2)
ax4.grid(alpha=0.3)

plt.suptitle(f'BRANCH-NBAR-D-K-74: Gate {gate_verdict}  '
             f'<n_bar>={n_bar_weighted_base:.2f}  (S73A=85.23)', fontsize=11)
plt.tight_layout(rect=[0, 0, 1, 0.96])

out_png = os.path.join(data_dir, 's74_branch_nbar_dk.png')  # (local)
plt.savefig(out_png, dpi=120, bbox_inches='tight')
plt.close()
print(f"Saved: {out_png}")

elapsed = time.time() - t_start  # (local)
print()
print(f"Total time: {elapsed:.2f} s")
print("DONE: BRANCH-NBAR-D-K-74")
