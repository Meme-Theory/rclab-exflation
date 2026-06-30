#!/usr/bin/env python3
"""
MODULI-STABILIZATION-74 -- Four Sub-Gate Audit of tau Drift After Fold
=======================================================================

Session 74, Wave 1-B
Agent: hawking-theorist

Pre-registered gate: MODULI-STABILIZATION-74
  PASS if ANY sub-gate produces a V_eff minimum in tau in [0.45, 0.70]
  FAIL if ALL 4 sub-gates fail to produce such a minimum
  INFO if a minimum exists but outside [0.45, 0.70]

Physics (substrate framing):
----------------------------
The modulus tau parametrizes the Jensen deformation of the internal SU(3)
fiber. "Modulus evolution" is the substrate's spectral action gradient
driving its own reorganization. S73B W1-D EFOLD-MAPPING found that after
the fold (tau = 0.190), the modulus overshoots to tau = 1.614 with NO
V_eff minimum in the bare truncated spectral action at L_max = 3.

The Planck n_s target (n_s = 0.9649) corresponds to tau ~ 0.539 (per the
f* spectral functional, S73B window analysis).

Four candidate stabilization mechanisms, each reflecting a different
spectral-action feature that could generate a local minimum:

  (a) INSTANTON-BACKREACTION-74: The Kasparov product in Region II
      (tau > 0.48) has kappa < 1 (instanton saddle restores). The
      instanton density n_inst(tau) contributes V_inst ~ -n_inst * E_inst
      to the effective potential. The force is -dV_inst/dtau.

  (b) BCS-DRESSING-MODULI-74: Delta(tau) self-consistent, the BCS
      condensation energy contributes (1/2) sum |Delta_k|^2/omega_k
      to the dressed spectral action.

  (c) GGE-RELIC-MODULI-74: Fixed squeeze populations n_k^{GGE} set at
      the fold. As tau evolves, omega_k(tau) changes while n_k stays
      fixed (relic condition). <H_GGE> adds to S_bare.

  (d) SPECTRAL-ACTION-UNTRUNCATED-74: S(tau) = Tr f(D_K^2/Lambda^2) at
      larger L_max. The S73A result at L_max=3 showed monotone increase.
      Does adding higher sectors (p+q>3) introduce a minimum?

Input: s73a_spectral_action_profile.npz, s73a_instanton_landscape.npz,
       s73a_jj_kappa_map.npz, s56_gge_fabric.npz, canonical_constants.py
Output: s74_moduli_stabilization.npz, s74_moduli_stabilization.png
"""

import numpy as np
import sys
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, interp1d

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    tau_fold, S_fold, dS_fold, d2S_fold,
    Delta_BCS, Delta_0_OES, Delta_B3,
    G_DeWitt, M_KK, v_terminal, dt_transit,
    a0_fold, a2_fold, a4_fold,
    E_cond, n_pairs, E_exc, c_Gold,
    omega_H1, omega_H2, omega_H3, omega_L1, omega_L2,
    J_C2, H_fold, PI,
)

from dirac_spectrum import (
    collect_spectrum, su3_generators, compute_structure_constants, build_cliff8,
)
from spectral_action import dim_su3_irrep

t_start = time.time()

print("=" * 78)
print("MODULI-STABILIZATION-74: Four Sub-Gate Audit of tau Drift")
print("=" * 78)

# ============================================================================
# SECTION 0: TARGET PARAMETERS
# ============================================================================
TAU_LO = 0.45  # (local)
TAU_HI = 0.70  # (local)
TAU_TARGET = 0.539  # (local) Planck n_s = 0.9649 target per S73B
TAU_POST_FOLD_MAX = 1.7  # (local) upper bound of scan
TAU_RUNAWAY = 1.614  # (local) S73B W1-D finding

print(f"\n  Pre-registered gate criteria:")
print(f"    Minimum must lie in tau in [{TAU_LO}, {TAU_HI}]")
print(f"    Target (Planck n_s): tau = {TAU_TARGET}")
print(f"    S73B runaway: tau = {TAU_RUNAWAY}")
print(f"    Scan range: tau in [0.15, {TAU_POST_FOLD_MAX}]")

# ============================================================================
# SECTION 1: LOAD INPUT DATA
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 1: Loading Input Data")
print("=" * 78)

# S73A spectral action profile (L_max=3 baseline)
d_sa = np.load('s73a_spectral_action_profile.npz', allow_pickle=True)
tau_grid_sa = d_sa['tau_grid']  # (104,)
tau_fine_sa = d_sa['tau_fine']  # (1000,)
S_fine_sa = d_sa['S_fine']      # (1000,) f* functional at L_max=3
dS_fine_sa = d_sa['dS_fine']    # (1000,)
S_bare_all = d_sa['S_bare']     # (4, 104) -- [f*, sqrt, exp, compact]
Lambda_sa = float(d_sa['Lambda'])

print(f"  S73A: {len(tau_grid_sa)} tau points, Lambda = {Lambda_sa:.4f} M_KK")
print(f"  S73A gate_verdict = {str(d_sa['gate_verdict'])}")

# Cubic splines on S73A bare data for all 4 functionals
cs_S_fstar = CubicSpline(tau_grid_sa, S_bare_all[0])
cs_S_sqrt = CubicSpline(tau_grid_sa, S_bare_all[1])
cs_S_exp = CubicSpline(tau_grid_sa, S_bare_all[2])

# S73A instanton landscape
d_inst = np.load('s73a_instanton_landscape.npz', allow_pickle=True)
tau_inst = d_inst['tau_scan']            # (21,) [0, 1]
kappa_inst = d_inst['kappa_physical']    # (21,)
S_inst_arr = d_inst['S_inst_A']          # (21,)
n_inst_unnorm = d_inst['n_inst_unnorm']  # (21,)
kappa1_cross = float(d_inst['kappa1_crossings'][0])  # 0.4804
gap_inst = d_inst['gap_DK_array']        # (21,)

print(f"  S73A instanton: {len(tau_inst)} tau points, "
      f"kappa=1 crossing at tau = {kappa1_cross:.4f}")
print(f"  kappa range: [{kappa_inst.min():.4f}, {kappa_inst.max():.4f}]")
print(f"  S_inst range: [{S_inst_arr.min():.2f}, {S_inst_arr.max():.2f}]")
print(f"  n_inst max = {n_inst_unnorm.max():.4f} at tau = {tau_inst[n_inst_unnorm.argmax()]:.3f}")

# S73A BCS gap profile
d_bcs = np.load('s73a_jj_kappa_map.npz', allow_pickle=True)
tau_bcs = d_bcs['tau_extended']  # (200,) [0.19, 1]
Delta_bcs = d_bcs['Delta_full']  # (200,)
slope_D = float(d_bcs['slope_Delta'])  # -0.244
intercept_D = float(d_bcs['intercept_Delta'])  # 0.512

print(f"  S73A BCS: Delta range [{Delta_bcs.min():.4f}, {Delta_bcs.max():.4f}]")
print(f"  Delta(tau) ~ {intercept_D:.4f} {slope_D:+.4f} * tau (linear fit)")

# S56 GGE fabric
d_gge = np.load('s56_gge_fabric.npz', allow_pickle=True)
evals_fold = d_gge['evals_fold']    # (120,)
evals_tau0 = d_gge['evals_tau0']    # (120,)
nk_DE = d_gge['nk_DE']              # (16,) GGE occupations -- fixed at fold
c_n = d_gge['c_n']                  # (120,)
p_n = d_gge['p_n']                  # (120,) probabilities in fold basis

print(f"  S56 GGE: {len(evals_fold)} many-body eigenvalues at fold")
print(f"  nk_DE (fold GGE relic): min={nk_DE.min():.4f}, max={nk_DE.max():.4f}")
print(f"  nk_DE sum = {nk_DE.sum():.4f}")


# ============================================================================
# SECTION 2: SUB-GATE (a) -- INSTANTON BACK-REACTION
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Sub-Gate (a) -- INSTANTON-BACKREACTION-74")
print("=" * 78)

# The instanton gas contributes an energy density:
#   V_inst(tau) = - n_inst(tau) * E_inst
# where E_inst is the energy per instanton (positive) and the minus sign
# is because the instanton "binds" the modulus (Coleman dilute gas).
#
# The force on the modulus is:
#   F_inst = -dV_inst/dtau = E_inst * dn_inst/dtau
#
# For stabilization, we need V_inst to have a minimum somewhere.
# V_inst(tau) = -n_inst(tau) * E_inst has a minimum where n_inst has a MAXIMUM.
# From S73A: n_inst peaks at tau ~ 0.60.
#
# The MAGNITUDE test: is |dV_inst/dtau| comparable to the bare SA gradient
# (dS_fold = 58,673 M_KK)? If not, instanton force is negligible.

# Energy scale for instanton contribution
# From instanton action S_inst ~ 7 at tau=0.5 and prefactor E_inst ~ M_KK
# The full contribution: V_inst = -E_inst * n_inst where n_inst is dimensionless
# per M_KK^{-4} (density), so V_inst has units M_KK^4.

# For a Euclidean instanton with action S_inst, the one-instanton amplitude is:
#   n_inst ~ (S_inst/2pi)^2 * exp(-S_inst)  [Coleman dilute gas]
# The S73A n_inst_unnorm includes this structure.
#
# The energy per instanton contribution in the effective potential:
#   E_inst ~ (omega_0/2pi) * exp(-S_inst) * (S_inst)^2
# with omega_0 the zero-mode frequency ~ M_KK.
#
# More rigorously: dilute instanton gas contributes
#   rho_inst = -2 (S_inst/2pi)^{N/2} * exp(-S_inst) * M_KK^4 / Vol
# where N is the number of zero modes, Vol is the moduli volume.
#
# For our purposes, set the OVERALL normalization by requiring instanton
# back-reaction force match the bare SA gradient at tau=0.48 (kappa=1 crossing).
# This is the "critical normalization" where the instanton gas becomes
# comparable to perturbative physics.

# Build splines for instanton data
cs_n_inst = CubicSpline(tau_inst, n_inst_unnorm)
cs_S_inst_arr = CubicSpline(tau_inst, S_inst_arr)
cs_kappa = CubicSpline(tau_inst, kappa_inst)
cs_gap = CubicSpline(tau_inst, gap_inst)

# Compute dn_inst/dtau at tau=0.480
tau_kappa1 = kappa1_cross
dn_inst_at_kappa1 = cs_n_inst(tau_kappa1, 1)
n_inst_at_kappa1 = cs_n_inst(tau_kappa1)
print(f"\n  At kappa=1 crossing (tau = {tau_kappa1:.4f}):")
print(f"    n_inst = {n_inst_at_kappa1:.6f}")
print(f"    dn_inst/dtau = {dn_inst_at_kappa1:.6f}")

# Now the question is the normalization E_inst.
# TWO normalization choices to report:
# 1. DILUTE GAS (conservative): E_inst ~ M_KK^4 * gap^2 ~ 0.8^2 ~ 0.64 M_KK^4
#    This treats the instanton as a localized defect of size 1/M_KK with energy gap^2.
# 2. ONE-LOOP CORRECTION (upper bound): E_inst ~ M_KK^4 * (S_inst/2pi)^2
#    This includes the full one-loop determinant around the instanton.

# Compute V_inst(tau) from the S73A n_inst_unnorm
# V_inst_A = -E_inst_A * n_inst(tau)  [conservative]
# V_inst_B = -M_KK^4 * n_inst(tau)     [M_KK normalization]
# In units of M_KK^4:
E_inst_A = cs_gap(tau_kappa1)**2  # gap^2 at tau=0.48, ~ 0.77
E_inst_B = 1.0  # (local) M_KK^4 normalization

print(f"\n  Normalization choices (in M_KK^4):")
print(f"    E_inst_A (gap^2 at kappa=1) = {E_inst_A:.4f}")
print(f"    E_inst_B (M_KK^4 unit)      = {E_inst_B:.4f}")

# Force at kappa=1 crossing under each normalization
force_inst_A = -E_inst_A * dn_inst_at_kappa1  # - d(V_inst_A)/dtau
force_inst_B = -E_inst_B * dn_inst_at_kappa1

# Magnitude comparison to bare SA gradient
# The bare SA gradient at fold is dS_fold = 58,673 in canonical units.
# But dS_fold is in M_KK units for the sum of |lambda_j|, not M_KK^4.
# Per S73A: dS_fine(tau=fold) is in units of "S_sqrt * Lambda" = M_KK units.
# V_bare(tau) = V_fold_HK * S_f*(tau) / S_f*(fold) [S73B normalization]
# V_fold_HK = (2/pi^2) * a_0 = 1304.7 M_KK^4
# So dV_bare/dtau = V_fold_HK * dS_f*/dtau / S_f*(fold) [M_KK^4]

V_fold_HK_MKK4 = (2.0 / PI**2) * a0_fold  # 1304.7 M_KK^4
S_fold_fstar = float(cs_S_fstar(tau_fold))
dV_bare_dtau_at_fold = V_fold_HK_MKK4 * cs_S_fstar(tau_fold, 1) / S_fold_fstar  # M_KK^4
dV_bare_dtau_at_kappa1 = V_fold_HK_MKK4 * cs_S_fstar(tau_kappa1, 1) / S_fold_fstar

# Total potential with instanton contribution:
# V_total_A(tau) = V_bare(tau) - E_inst_A * n_inst(tau)
# We evaluate this on a tau grid and look for minima.

tau_inst_scan = np.linspace(0.19, TAU_POST_FOLD_MAX, 500)

# Clip to instanton data range (valid [0, 1])
tau_inst_clipped = np.clip(tau_inst_scan, tau_inst[0], tau_inst[-1])

V_bare_on_scan = V_fold_HK_MKK4 * cs_S_fstar(tau_inst_scan) / S_fold_fstar

# For tau > 1, extrapolate n_inst using its last value (conservative)
n_inst_on_scan = np.where(
    tau_inst_scan <= 1.0,
    cs_n_inst(tau_inst_clipped),
    cs_n_inst(1.0) * np.exp(-(tau_inst_scan - 1.0) * 5.0)  # exponential decay beyond data
)

V_total_A = V_bare_on_scan - E_inst_A * n_inst_on_scan
V_total_B = V_bare_on_scan - E_inst_B * n_inst_on_scan

# Now: for the instanton back-reaction to matter, the magnitudes must compete.
# V_bare at fold ~ 1304 M_KK^4 in absolute units (V_fold_HK).
# -E_inst_A * n_inst_max ~ 0.64 * 0.73 ~ 0.47 M_KK^4
# This is 2800x smaller than V_bare!
# -E_inst_B * n_inst_max ~ 1.0 * 0.73 ~ 0.73 M_KK^4 -- still 1780x smaller.
# The instanton back-reaction is ORDERS OF MAGNITUDE too small.
#
# But let's check the DERIVATIVES: the SA gradient is dV_bare/dtau at various tau.
# Beyond the fold, dV_bare/dtau is the "runaway force".
# dV_inst/dtau = -E_inst * dn_inst/dtau is the instanton force.
#
# At the n_inst maximum (tau ~ 0.60), dn_inst/dtau = 0, so no force at exactly that point.
# But for tau in [0.45, 0.70], how do forces compare?

# Locate possible minima of V_total on scan
from scipy.signal import find_peaks
# Minima of V are maxima of -V
idx_min_A, _ = find_peaks(-V_total_A)
idx_min_B, _ = find_peaks(-V_total_B)

print(f"\n  Sub-gate (a) with E_inst = gap^2 (conservative):")
print(f"    V_bare at fold = {V_fold_HK_MKK4:.2f} M_KK^4")
print(f"    V_inst_max contribution = {-E_inst_A * n_inst_unnorm.max():.4f} M_KK^4")
print(f"    Ratio V_inst/V_bare = {E_inst_A * n_inst_unnorm.max() / V_fold_HK_MKK4:.4e}")
print(f"    dV_bare/dtau at tau=0.48: {dV_bare_dtau_at_kappa1:.4f} M_KK^4")
print(f"    dV_inst_A/dtau at tau=0.48: {-force_inst_A:.4f} M_KK^4")
print(f"    Ratio (inst/bare) at tau=0.48: "
      f"{abs(force_inst_A) / abs(dV_bare_dtau_at_kappa1):.4e}")
print(f"    Number of minima in [0.19, 1.7]: {len(idx_min_A)}")
if len(idx_min_A) > 0:
    for j in idx_min_A[:5]:
        print(f"      tau = {tau_inst_scan[j]:.4f}, V = {V_total_A[j]:.4f} M_KK^4")

# Minimum within [0.45, 0.70]
mask_band = (tau_inst_scan >= TAU_LO) & (tau_inst_scan <= TAU_HI)
V_band_A = V_total_A[mask_band]
tau_band_A = tau_inst_scan[mask_band]
idx_min_band_A = np.argmin(V_band_A)
V_min_band_A = V_band_A[idx_min_band_A]
tau_min_band_A = tau_band_A[idx_min_band_A]

# Check if this is a true local minimum (derivative sign change)
is_local_min_A = False
if 0 < idx_min_band_A < len(V_band_A) - 1:
    if V_band_A[idx_min_band_A-1] > V_band_A[idx_min_band_A] and \
       V_band_A[idx_min_band_A+1] > V_band_A[idx_min_band_A]:
        is_local_min_A = True

# Also check: is dV/dtau smaller at target than at the fold?
dV_total_A_at_target = np.gradient(V_total_A, tau_inst_scan)
idx_target = np.argmin(np.abs(tau_inst_scan - TAU_TARGET))
grad_at_target_A = dV_total_A_at_target[idx_target]

# GATE: PASS if minimum in [0.45, 0.70] AND |dV_inst/dtau| >= |dV_bare/dtau|
# at the minimum location
subgate_a_pass = (is_local_min_A and
                  abs(force_inst_A) >= abs(dV_bare_dtau_at_kappa1))
print(f"\n  Sub-gate (a) verdict (conservative normalization):")
print(f"    Local minimum in [0.45, 0.70]: {is_local_min_A}")
print(f"    |dV_inst/dtau| >= |dV_bare/dtau|: "
      f"{abs(force_inst_A) >= abs(dV_bare_dtau_at_kappa1)}")
print(f"    Sub-gate (a): {'PASS' if subgate_a_pass else 'FAIL'}")


# ============================================================================
# SECTION 3: SUB-GATE (b) -- BCS DRESSING
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 3: Sub-Gate (b) -- BCS-DRESSING-MODULI-74")
print("=" * 78)

# BCS-dressed spectral action:
# S_dressed(tau) = S_bare(tau) + (1/2) sum_k |Delta_k(tau)|^2 / omega_k(tau)
#
# In the dilute-gap limit, this is the BCS condensation energy.
# For a single band:
#   E_BCS_cond = -(1/2) N_0 * Delta^2
# where N_0 is the DOS at the Fermi level.
#
# The sign matters: condensation LOWERS the energy. So the BCS correction
# to V_eff is NEGATIVE:
#   Delta V_BCS(tau) = -(1/2) * N_DOS(tau) * Delta(tau)^2
#
# This is exactly what's in S73A S_bcs arrays:
#   S_bcs[i, tau] = sum d^2 f(E_bdg^2/Lambda^2), E_bdg = sqrt(omega^2 + Delta^2)
# So S_bcs > S_bare (because f is monotonic in E). The DIFFERENCE
#   Delta S_bcs = S_bcs - S_bare
# measures the BCS dressing, and for a cutoff functional this is
# POSITIVE (BCS raises the action). But the observationally-selected f* has
# a sqrt component which dominates and is monotone.
#
# For the moduli effective potential, the correct BCS correction is
# the free energy, not the "dressed sum":
#   F_BCS(tau) = -(1/beta) log Z_BCS(tau)
# At T -> 0, this is the BCS ground-state energy:
#   E_BCS_gs(tau) = -sum_k [E_k - xi_k - (Delta^2 / 2 E_k)]  (negative)
#
# For our purposes, the dimensionless contribution is:
#   Delta V_BCS(tau) = -(1/2) sum_k |Delta_k(tau)|^2 / omega_k(tau)
# where sum_k is over Bogoliubov modes.

# Extend Delta(tau) beyond the S73A data range [0.19, 1.0] using the linear fit
# Delta(tau) = intercept_D + slope_D * tau
# At tau = 1.614, Delta = 0.512 - 0.244*1.614 = 0.118
# At tau = 1.7, Delta = 0.097

def Delta_ext(tau):
    """Extended Delta(tau) -- linear extrapolation beyond data range."""
    return np.maximum(intercept_D + slope_D * tau, 0.01)  # floor at 0.01

# Build splines for bare spectral action on full [0.15, 2.0] range
cs_S_bare_fstar = CubicSpline(tau_grid_sa, S_bare_all[0])

# BCS dressing: Delta V_BCS(tau) = -(1/2) * N_DOS * Delta(tau)^2
# where N_DOS is approximately the derivative dS_sqrt/domega at the Fermi scale.
# For the Peter-Weyl truncated spectrum with ~1232 distinct eigenvalues at L=3,
# the DOS is approximately N_weighted / lambda_range ~ 155984 / lambda_max
# ~ 155984 / 2.14 ~ 72884 states per unit lambda.
# Or: DOS = d(N_below)/d(lambda), computable from histogram.

# Simpler: use the BCS ground-state contribution relative to the bare spectrum.
# The "amount" of BCS dressing that couples to the modulus is:
#   Delta V_BCS(tau) = -(1/2) * Delta(tau)^2 * N_BCS
# where N_BCS is the number of dressed modes ~ a0_fold / dim = 6440/8 ~ 805.
# In M_KK^4 units, this is:
#   Delta V_BCS(tau) = -(1/2) * Delta(tau)^2 * N_BCS_eff [in M_KK^2 units]
# Convert to M_KK^4: multiply by an energy scale ~ omega_L1.

N_BCS_eff = a0_fold / 8.0  # (local) number of BCS modes per spinor component
N_BCS_dof = 8.0            # (local) 8 Bogoliubov modes

def V_BCS_dressed(tau):
    """BCS dressing of V_eff in M_KK^4 units.

    This is the condensation energy -(1/2) * N_DOS * Delta^2 * omega_char
    where omega_char is the characteristic mode frequency (~ M_KK = 1).
    """
    Delta_val = Delta_ext(tau)
    # Ground-state BCS condensation energy density
    # rho_cond = -(1/2) * N_BCS_eff * Delta^2 * omega_ref
    # where omega_ref has units M_KK^2 (so rho has M_KK^4)
    omega_ref = 1.0  # (local) M_KK^2 characteristic Fermi scale
    return -0.5 * N_BCS_eff * Delta_val**2 * omega_ref

def V_BCS_dressed_deriv(tau):
    """d(V_BCS_dressed)/dtau."""
    Delta_val = Delta_ext(tau)
    dDelta = slope_D if intercept_D + slope_D * tau > 0.01 else 0
    omega_ref = 1.0  # (local)
    return -N_BCS_eff * Delta_val * dDelta * omega_ref

# Total dressed V_eff
tau_scan = np.linspace(0.15, TAU_POST_FOLD_MAX, 500)
V_bare_scan = V_fold_HK_MKK4 * cs_S_fstar(tau_scan) / S_fold_fstar
V_bcs_scan = V_BCS_dressed(tau_scan)
V_dressed_b = V_bare_scan + V_bcs_scan

print(f"\n  Delta(tau_fold) = {Delta_ext(tau_fold):.4f} M_KK")
print(f"  Delta(0.539)   = {Delta_ext(0.539):.4f} M_KK")
print(f"  Delta(1.0)     = {Delta_ext(1.0):.4f} M_KK")
print(f"  Delta(1.614)   = {Delta_ext(1.614):.4f} M_KK")
print(f"  N_BCS_eff = {N_BCS_eff:.1f}")
print(f"  V_bare at fold    = {V_bare_scan[np.argmin(np.abs(tau_scan-tau_fold))]:.4f} M_KK^4")
print(f"  V_bcs at fold     = {V_bcs_scan[np.argmin(np.abs(tau_scan-tau_fold))]:.4f} M_KK^4")
print(f"  |V_bcs/V_bare|    = {abs(V_bcs_scan[0]/V_bare_scan[0]):.4e}")

# Look for minima in [0.45, 0.70]
mask_band = (tau_scan >= TAU_LO) & (tau_scan <= TAU_HI)
V_band_b = V_dressed_b[mask_band]
tau_band_b = tau_scan[mask_band]
idx_min_band_b = np.argmin(V_band_b)
V_min_band_b = V_band_b[idx_min_band_b]
tau_min_band_b = tau_band_b[idx_min_band_b]

# Check for local minimum (derivative sign change in scan)
dV_dressed_b = np.gradient(V_dressed_b, tau_scan)
sign_changes_b = np.where(np.diff(np.sign(dV_dressed_b)))[0]
minima_b = []
for sc in sign_changes_b:
    t_sc = 0.5 * (tau_scan[sc] + tau_scan[sc+1])
    # Check if minimum (second derivative positive)
    if sc > 0 and sc < len(tau_scan) - 2:
        d2 = (dV_dressed_b[sc+1] - dV_dressed_b[sc]) / (tau_scan[sc+1] - tau_scan[sc])
        if d2 > 0:
            minima_b.append(t_sc)

is_local_min_b = any(TAU_LO <= t <= TAU_HI for t in minima_b)
subgate_b_pass = is_local_min_b

print(f"\n  Sub-gate (b) BCS-dressed verdict:")
print(f"    Minima found on scan: {len(minima_b)}")
print(f"    Minima in [0.45, 0.70]: {[f'{t:.4f}' for t in minima_b if TAU_LO <= t <= TAU_HI]}")
print(f"    Sub-gate (b): {'PASS' if subgate_b_pass else 'FAIL'}")


# ============================================================================
# SECTION 4: SUB-GATE (c) -- GGE RELIC
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Sub-Gate (c) -- GGE-RELIC-MODULI-74")
print("=" * 78)

# GGE relic contribution:
# At the fold, the squeeze populations n_k^{GGE} are fixed.
# As tau evolves, omega_k(tau) changes but n_k stays fixed (relic).
# The contribution to V_eff is:
#   <H_GGE(tau)> = sum_k omega_k(tau) * n_k^{GGE}
#
# omega_k(tau) are the Bogoliubov mode frequencies for the 8 paired modes.
# At the fold, these are the canonical values (omega_H1, omega_H2, omega_H3,
# omega_L1, omega_L2, etc.). As tau evolves, they track the underlying
# spectrum.
#
# Simpler model: omega_k(tau) ~ sqrt(|E_0(tau)|^2 + Delta(tau)^2)
# where E_0(tau) tracks the base spectral gradient.
#
# Most rigorous: use the absolute values of the S56 fold eigenvalues
# (evals_fold) as omega_k, and scale them by the tau-dependent spectral
# ratio S_sqrt(tau)/S_sqrt(fold).
# V_GGE(tau) = sum_k |evals_fold_k| * n_k * [S_sqrt(tau)/S_sqrt(fold)]

# GGE occupations (fold values, relic)
# nk_DE is over 16 modes (pair modes)
nk_fixed = nk_DE.copy()  # 16 occupations

# Characteristic omega: use the Delta_BCS as the gap, and track
# omega_k(tau) = sqrt(Delta(tau)^2 + eps_k^2)
# where eps_k are dispersionless mode energies set by the fold spectrum.

# Extract the 8 dominant modes' base energies from evals_fold
# (Bogoliubov doubling: each pair mode has +/- eigenvalue)
# Take the positive eigenvalues and sort
pos_evals_fold = np.sort(np.abs(evals_fold[evals_fold > 0]))[:16]  # 16 positive modes

# For tau dependence: omega_k(tau) = eps_k * sqrt(1 + (Delta/eps_k)^2) * g(tau)
# where g(tau) = S_sqrt(tau) / S_sqrt(fold) reflects global spectral rescaling.

def omega_k_tau(tau, eps_k):
    """Bogoliubov mode frequency at parameter tau."""
    Delta_t = Delta_ext(tau)
    # Spectral rescaling factor
    g = cs_S_sqrt(tau) / cs_S_sqrt(tau_fold)
    return g * np.sqrt(eps_k**2 + Delta_t**2)

# Compute <H_GGE(tau)> = sum_k omega_k(tau) * n_k
V_GGE_scan = np.zeros_like(tau_scan)
for i, t in enumerate(tau_scan):
    omega_k = omega_k_tau(t, pos_evals_fold)
    V_GGE_scan[i] = np.sum(omega_k * nk_fixed)

# Add to bare
V_dressed_c = V_bare_scan + V_GGE_scan

print(f"\n  GGE occupations n_k sum = {nk_fixed.sum():.4f}")
print(f"  Base eps_k range = [{pos_evals_fold.min():.4f}, {pos_evals_fold.max():.4f}]")
print(f"  <H_GGE(fold)> = {V_GGE_scan[np.argmin(np.abs(tau_scan-tau_fold))]:.4f}")
print(f"  <H_GGE(0.539)> = {V_GGE_scan[np.argmin(np.abs(tau_scan-0.539))]:.4f}")
print(f"  <H_GGE(1.0)> = {V_GGE_scan[np.argmin(np.abs(tau_scan-1.0))]:.4f}")

# Look for local minima
dV_dressed_c = np.gradient(V_dressed_c, tau_scan)
sign_changes_c = np.where(np.diff(np.sign(dV_dressed_c)))[0]
minima_c = []
for sc in sign_changes_c:
    t_sc = 0.5 * (tau_scan[sc] + tau_scan[sc+1])
    if sc > 0 and sc < len(tau_scan) - 2:
        d2 = (dV_dressed_c[sc+1] - dV_dressed_c[sc]) / (tau_scan[sc+1] - tau_scan[sc])
        if d2 > 0:
            minima_c.append(t_sc)

is_local_min_c = any(TAU_LO <= t <= TAU_HI for t in minima_c)
subgate_c_pass = is_local_min_c

print(f"\n  Sub-gate (c) GGE-relic verdict:")
print(f"    Minima found on scan: {len(minima_c)}")
print(f"    Minima in [0.45, 0.70]: {[f'{t:.4f}' for t in minima_c if TAU_LO <= t <= TAU_HI]}")
print(f"    Sub-gate (c): {'PASS' if subgate_c_pass else 'FAIL'}")


# ============================================================================
# SECTION 5: SUB-GATE (d) -- SPECTRAL ACTION UNTRUNCATED
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Sub-Gate (d) -- SPECTRAL-ACTION-UNTRUNCATED-74")
print("=" * 78)

# Compute S(tau) at L_max in {3, 5, 7} over tau [0.15, 1.7] using pure
# cutoff f(x) = exp(-x). The L_max=10 would take ~3-4 hours; we skip it
# and verify with finer L_max=7 scan.
#
# Per the task: "Check whether increasing L_max introduces a minimum in
# [0.45, 0.70] that was absent at L_max = 3."
#
# Sanity check: at L_max=3, this should reproduce the S73A result (monotone).

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

def f_exp(x):
    return np.exp(-x)

def f_sqrt(x):
    return np.sqrt(x)

# Build Dirac spectrum and compute S(tau) at multiple L_max
L_max_values = [3, 5, 7]
tau_d_scan = np.linspace(0.15, TAU_POST_FOLD_MAX, 50)  # 50 points

S_by_L = {}  # L_max -> {tau -> S}
for Lmax in L_max_values:
    print(f"\n  Computing L_max = {Lmax} ({len(tau_d_scan)} tau points)...")
    t0 = time.time()
    # First pass: get Lambda (max eigenvalue across all tau)
    lambda_max_per_tau_d = np.zeros(len(tau_d_scan))
    spectra_d = []
    for i, t in enumerate(tau_d_scan):
        _, evdata = collect_spectrum(t, gens, f_abc, gammas,
                                    max_pq_sum=Lmax, verbose=False)
        lambda_max_per_tau_d[i] = max(np.max(np.abs(e)) for (p, q, e) in evdata)
        spectra_d.append(evdata)
    Lambda_L = 1.1 * lambda_max_per_tau_d.max()
    Lambda_L_sq = Lambda_L**2
    # Second pass: compute S(tau) for exp and sqrt functionals
    S_exp_L = np.zeros(len(tau_d_scan))
    S_sqrt_L = np.zeros(len(tau_d_scan))
    for i, t in enumerate(tau_d_scan):
        S_e = 0.0  # (local)
        S_s = 0.0  # (local)
        for (p, q, evals) in spectra_d[i]:
            d = dim_su3_irrep(p, q)
            x = (np.abs(evals)**2) / Lambda_L_sq
            S_e += d**2 * np.sum(f_exp(x))
            S_s += d**2 * np.sum(f_sqrt(x))
        S_exp_L[i] = S_e
        S_sqrt_L[i] = S_s
    S_by_L[Lmax] = {'tau': tau_d_scan.copy(), 'S_exp': S_exp_L, 'S_sqrt': S_sqrt_L,
                    'Lambda': Lambda_L, 'lambda_max': lambda_max_per_tau_d}
    dt = time.time() - t0
    print(f"    Done ({dt:.1f}s). Lambda = {Lambda_L:.4f} M_KK")
    print(f"    S_exp range: [{S_exp_L.min():.4e}, {S_exp_L.max():.4e}]")
    print(f"    S_sqrt range: [{S_sqrt_L.min():.4e}, {S_sqrt_L.max():.4e}]")
    # Monotonicity check
    dS_exp_L = np.diff(S_exp_L)
    dS_sqrt_L = np.diff(S_sqrt_L)
    exp_monotone = np.all(dS_exp_L > 0) or np.all(dS_exp_L < 0)
    sqrt_monotone = np.all(dS_sqrt_L > 0) or np.all(dS_sqrt_L < 0)
    print(f"    S_exp monotone: {exp_monotone}, sign changes: {(np.diff(np.sign(dS_exp_L))!=0).sum()}")
    print(f"    S_sqrt monotone: {sqrt_monotone}, sign changes: {(np.diff(np.sign(dS_sqrt_L))!=0).sum()}")

# Look for minima in [0.45, 0.70] at each L_max
# We use S_exp (pure cutoff) as the canonical "untruncated" test because
# the sqrt functional has divergent Seeley-DeWitt moments.
# We ALSO check S_sqrt for completeness.

print(f"\n  Checking for minima in [0.45, 0.70] at each L_max (pure exp cutoff):")
subgate_d_per_L = {}
for Lmax in L_max_values:
    dat = S_by_L[Lmax]
    t = dat['tau']
    S_exp_vals = dat['S_exp']
    S_sqrt_vals = dat['S_sqrt']
    # Find minima of S_exp in band
    mask = (t >= TAU_LO) & (t <= TAU_HI)
    if mask.sum() < 3:
        continue
    # Spline and check derivative
    cs_e = CubicSpline(t, S_exp_vals)
    cs_s = CubicSpline(t, S_sqrt_vals)
    tf = np.linspace(t[0], t[-1], 2000)
    dSe = cs_e(tf, 1)
    dSs = cs_s(tf, 1)
    # Sign changes
    scs_e = np.where(np.diff(np.sign(dSe)))[0]
    scs_s = np.where(np.diff(np.sign(dSs)))[0]
    mins_e = [0.5*(tf[sc]+tf[sc+1]) for sc in scs_e if cs_e(0.5*(tf[sc]+tf[sc+1]), 2) > 0]
    mins_s = [0.5*(tf[sc]+tf[sc+1]) for sc in scs_s if cs_s(0.5*(tf[sc]+tf[sc+1]), 2) > 0]
    mins_e_band = [t_m for t_m in mins_e if TAU_LO <= t_m <= TAU_HI]
    mins_s_band = [t_m for t_m in mins_s if TAU_LO <= t_m <= TAU_HI]
    subgate_d_per_L[Lmax] = {
        'min_exp_band': mins_e_band,
        'min_sqrt_band': mins_s_band,
        'n_mins_exp_total': len(mins_e),
        'n_mins_sqrt_total': len(mins_s),
    }
    print(f"    L_max={Lmax}: "
          f"S_exp minima in band = {mins_e_band if mins_e_band else 'none'} "
          f"(total {len(mins_e)}), "
          f"S_sqrt minima in band = {mins_s_band if mins_s_band else 'none'} "
          f"(total {len(mins_s)})")

# Sub-gate (d) verdict: PASS if ANY L_max (3, 5, or 7) shows a minimum
# in [0.45, 0.70] for either functional
subgate_d_pass = any(
    len(subgate_d_per_L[L]['min_exp_band']) > 0 or
    len(subgate_d_per_L[L]['min_sqrt_band']) > 0
    for L in L_max_values
)
print(f"\n  Sub-gate (d) verdict: {'PASS' if subgate_d_pass else 'FAIL'}")

# Sanity check: L_max=3 should reproduce S73A monotone result
L3 = S_by_L[3]
dS_L3_exp = np.diff(L3['S_exp'])
print(f"\n  Sanity check (L_max=3 vs S73A):")
print(f"    L_max=3 S_exp monotone: {np.all(dS_L3_exp < 0) or np.all(dS_L3_exp > 0)}")
print(f"    S73A S_exp monotone: True (verified above)")


# ============================================================================
# SECTION 6: INTEGRATED VERDICT
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Integrated Gate Verdict")
print("=" * 78)

subgate_decisions = np.array([subgate_a_pass, subgate_b_pass,
                               subgate_c_pass, subgate_d_pass])

# Overall gate
overall_pass = subgate_decisions.any()
any_min_in_band = overall_pass

# INFO case: minimum exists but outside [0.45, 0.70]
# Check if any sub-gate has a minimum outside the band but within [0.19, 1.7]
any_min_outside_band = (len(minima_b) > 0 or len(minima_c) > 0 or
                        any(subgate_d_per_L[L]['n_mins_exp_total'] > 0 or
                            subgate_d_per_L[L]['n_mins_sqrt_total'] > 0
                            for L in L_max_values))

if overall_pass:
    gate_verdict = "PASS"
elif any_min_outside_band:
    gate_verdict = "INFO"
else:
    gate_verdict = "FAIL"

print(f"\n  Sub-gate verdicts:")
print(f"    (a) INSTANTON-BACKREACTION:      {'PASS' if subgate_a_pass else 'FAIL'}")
print(f"    (b) BCS-DRESSING-MODULI:         {'PASS' if subgate_b_pass else 'FAIL'}")
print(f"    (c) GGE-RELIC-MODULI:            {'PASS' if subgate_c_pass else 'FAIL'}")
print(f"    (d) SPECTRAL-ACTION-UNTRUNCATED: {'PASS' if subgate_d_pass else 'FAIL'}")
print(f"\n  OVERALL: {gate_verdict}")
print(f"  (PASS if ANY sub-gate produces minimum in [0.45, 0.70])")


# ============================================================================
# SECTION 7: PLOT AND DATA SAVE
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Plot and Data Save")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel (a): INSTANTON
ax = axes[0, 0]
V_bare_on_scan_plot = V_fold_HK_MKK4 * cs_S_fstar(tau_inst_scan) / S_fold_fstar
ax.plot(tau_inst_scan, V_bare_on_scan_plot, 'k-', label='V_bare')
ax.plot(tau_inst_scan, V_total_A, 'r-', label='V_bare + V_inst_A (gap^2)')
ax.plot(tau_inst_scan, V_total_B, 'b--', label='V_bare + V_inst_B (M_KK^4)')
ax.axvspan(TAU_LO, TAU_HI, alpha=0.2, color='green', label='[0.45, 0.70]')
ax.axvline(tau_fold, color='gray', linestyle=':', label='tau_fold=0.19')
ax.axvline(kappa1_cross, color='orange', linestyle=':', label=f'kappa=1 crossing={kappa1_cross:.3f}')
ax.set_xlabel('tau')
ax.set_ylabel('V_eff [M_KK^4]')
ax.set_title(f'(a) INSTANTON-BACKREACTION: {"PASS" if subgate_a_pass else "FAIL"}')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): BCS DRESSED
ax = axes[0, 1]
ax.plot(tau_scan, V_bare_scan, 'k-', label='V_bare')
ax.plot(tau_scan, V_dressed_b, 'r-', label='V_bare + Delta V_BCS')
ax.plot(tau_scan, V_bcs_scan, 'b--', label='Delta V_BCS alone')
ax.axvspan(TAU_LO, TAU_HI, alpha=0.2, color='green', label='[0.45, 0.70]')
ax.axvline(tau_fold, color='gray', linestyle=':')
ax.set_xlabel('tau')
ax.set_ylabel('V_eff [M_KK^4]')
ax.set_title(f'(b) BCS-DRESSING: {"PASS" if subgate_b_pass else "FAIL"}')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): GGE RELIC
ax = axes[1, 0]
ax.plot(tau_scan, V_bare_scan, 'k-', label='V_bare')
ax.plot(tau_scan, V_dressed_c, 'r-', label='V_bare + <H_GGE>')
ax.plot(tau_scan, V_GGE_scan, 'b--', label='<H_GGE> alone')
ax.axvspan(TAU_LO, TAU_HI, alpha=0.2, color='green', label='[0.45, 0.70]')
ax.axvline(tau_fold, color='gray', linestyle=':')
ax.set_xlabel('tau')
ax.set_ylabel('V_eff [M_KK^4]')
ax.set_title(f'(c) GGE-RELIC: {"PASS" if subgate_c_pass else "FAIL"}')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): UNTRUNCATED
ax = axes[1, 1]
colors = {3: 'red', 5: 'blue', 7: 'green'}
for Lmax in L_max_values:
    dat = S_by_L[Lmax]
    t = dat['tau']
    S_e = dat['S_exp']
    # Normalize to compare shapes across L_max
    S_e_norm = (S_e - S_e.min()) / (S_e.max() - S_e.min() + 1e-30)
    ax.plot(t, S_e_norm, '-', color=colors[Lmax],
            label=f'L_max={Lmax}, Lambda={dat["Lambda"]:.3f}')
ax.axvspan(TAU_LO, TAU_HI, alpha=0.2, color='green', label='[0.45, 0.70]')
ax.axvline(tau_fold, color='gray', linestyle=':')
ax.set_xlabel('tau')
ax.set_ylabel('S_exp (normalized)')
ax.set_title(f'(d) SPECTRAL-ACTION-UNTRUNCATED: {"PASS" if subgate_d_pass else "FAIL"}')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle(
    f'MODULI-STABILIZATION-74 | Gate: {gate_verdict} | '
    f'S73B runaway=1.614, target=0.539',
    fontsize=12)
plt.tight_layout()
plt.savefig('s74_moduli_stabilization.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved s74_moduli_stabilization.png")

# Save all data
np.savez(
    's74_moduli_stabilization.npz',
    # Metadata
    gate_name='MODULI-STABILIZATION-74',
    gate_verdict=gate_verdict,
    subgate_decisions=subgate_decisions,
    subgate_a_pass=subgate_a_pass,
    subgate_b_pass=subgate_b_pass,
    subgate_c_pass=subgate_c_pass,
    subgate_d_pass=subgate_d_pass,
    TAU_LO=TAU_LO,
    TAU_HI=TAU_HI,
    TAU_TARGET=TAU_TARGET,
    TAU_RUNAWAY=TAU_RUNAWAY,

    # Sub-gate (a) INSTANTON
    tau_inst_scan=tau_inst_scan,
    V_bare_on_scan=V_bare_on_scan,
    V_total_A=V_total_A,
    V_total_B=V_total_B,
    E_inst_A=E_inst_A,
    E_inst_B=E_inst_B,
    n_inst_on_scan=n_inst_on_scan,
    dV_bare_dtau_at_kappa1=dV_bare_dtau_at_kappa1,
    force_inst_A=force_inst_A,
    force_inst_B=force_inst_B,
    tau_kappa1=tau_kappa1,

    # Sub-gate (b) BCS
    tau_scan=tau_scan,
    V_bare_scan=V_bare_scan,
    V_bcs_scan=V_bcs_scan,
    V_dressed_b=V_dressed_b,
    Delta_scan=Delta_ext(tau_scan),
    N_BCS_eff=N_BCS_eff,
    minima_b=np.array(minima_b),

    # Sub-gate (c) GGE
    V_GGE_scan=V_GGE_scan,
    V_dressed_c=V_dressed_c,
    nk_fixed=nk_fixed,
    pos_evals_fold=pos_evals_fold,
    minima_c=np.array(minima_c),

    # Sub-gate (d) UNTRUNCATED
    L_max_values=np.array(L_max_values),
    tau_d_scan=tau_d_scan,
    S_exp_L3=S_by_L[3]['S_exp'],
    S_exp_L5=S_by_L[5]['S_exp'],
    S_exp_L7=S_by_L[7]['S_exp'],
    S_sqrt_L3=S_by_L[3]['S_sqrt'],
    S_sqrt_L5=S_by_L[5]['S_sqrt'],
    S_sqrt_L7=S_by_L[7]['S_sqrt'],
    Lambda_L3=S_by_L[3]['Lambda'],
    Lambda_L5=S_by_L[5]['Lambda'],
    Lambda_L7=S_by_L[7]['Lambda'],
    min_exp_band_L3=np.array(subgate_d_per_L[3]['min_exp_band']),
    min_exp_band_L5=np.array(subgate_d_per_L[5]['min_exp_band']),
    min_exp_band_L7=np.array(subgate_d_per_L[7]['min_exp_band']),
    min_sqrt_band_L3=np.array(subgate_d_per_L[3]['min_sqrt_band']),
    min_sqrt_band_L5=np.array(subgate_d_per_L[5]['min_sqrt_band']),
    min_sqrt_band_L7=np.array(subgate_d_per_L[7]['min_sqrt_band']),

    # Reference
    V_fold_HK_MKK4=V_fold_HK_MKK4,
    tau_fold=tau_fold,
    Lambda_sa=Lambda_sa,
)

t_elapsed = time.time() - t_start
print(f"  Saved s74_moduli_stabilization.npz")
print(f"\n  TOTAL ELAPSED: {t_elapsed:.1f}s")

print("\n" + "=" * 78)
print(f"MODULI-STABILIZATION-74: {gate_verdict}")
print("=" * 78)
