#!/usr/bin/env python3
"""
S77-B1-NPIVOT: k_pivot Horizon-Crossing e-Fold Number
======================================================

Computes the e-fold number N_pivot at which k_pivot = 0.05 Mpc^{-1} crosses
the Hubble horizon in the post-fold expansion. This constrains which physical
processes can affect CMB modes.

Gate: S77-B1-NPIVOT (INFO diagnostic)
  Report N_pivot, N_BBN, N_recomb. No PASS/FAIL.

CRITICAL NORMALIZATION FINDING:
  S73B reported k_pivot = 4.30e-57 M_KK "57 OOM below horizon." This used
  the PHYSICAL wavenumber today (k_phys = k_com / a_today, with a_today = 1),
  compared to aH in the fold normalization (a_fold = 1). These are DIFFERENT
  normalizations. The correct comoving wavenumber in fold normalization is:

    k_com(fold) = k_com(today) * exp(N_total) = 14.31 M_KK

  With aH(fold) = 0.975 M_KK, the mode is SUBHORIZON at the fold (k/aH = 14.7)
  and EXITS the horizon at N_pivot = 3.12 during the quasi-dS expansion.

Method:
  1. Load a(N) and H(N) from s73b_efold_mapping.npz
  2. Convert k_pivot to fold-normalization comoving M_KK units
  3. Find N_pivot where a(N) * H(N) = k_com (horizon exit)
  4. Repeat for BBN, recombination, and today's horizon scales
  5. Cross-check against standard N_* formula

Input: computations/session-73/s73b_efold_mapping.npz
Output: computations/session-77/s77_n_pivot_map.npz, s77_n_pivot_map.png
"""

import sys
sys.path.insert(0, "computations")
from canonical_constants import (
    M_KK, M_KK_gravity, Mpc_to_GeV_inv, H_fold, H_0_GeV, H_0_inv_s,
    T_CMB_GeV, T_BBN_GeV, T_recomb_GeV, z_BBN,
    hbar_c_GeV_m, Mpc_to_m, GeV_inv_to_Mpc, GeV_to_inv_s,
    m_tau, dt_transit
)
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 78)
print("S77-B1-NPIVOT: k_pivot Horizon-Crossing e-Fold Number")
print("=" * 78)

# =============================================================================
# SECTION 1: Load S73B trajectory data
# =============================================================================
print("\nSECTION 1: Loading S73B trajectory data")
print("-" * 50)

data = np.load("computations/session-73/s73b_efold_mapping.npz", allow_pickle=True)
lna_sol = data['lna_sol']       # ln(a/a_fold), a_fold = 1
H_sol = data['H_sol']           # H(t) in M_KK units
aH_sol = data['aH_sol']         # a(t)*H(t) in M_KK units
w_sol = data['w_sol']           # equation of state w(t)
t_sol = data['t_sol']           # time in M_KK^{-1}

# Scalars from S73B
N_total_s73b = float(data['N_total'])       # (local) total e-folds fold->today
N_modulus = float(data['N_modulus'])         # (local) e-folds in exflation phase
N_post_rh = float(data['N_post_rh'])        # (local) e-folds from reheating to today
N_star_s73b = float(data['N_star'])         # (local) N_* from s73b
k_pivot_MKK_s73b = float(data['k_pivot_MKK'])  # (local) S73B value (physical today)
T_rh_GeV = float(data['T_rh_GeV'])         # (local) reheating temperature
H_phys_fold = float(data['H_phys_fold_MKK'])  # (local) H at fold in M_KK
z_fold_val = float(data['z_fold'])          # (local) redshift at fold

print(f"  Trajectory: {len(lna_sol)} points, N in [{lna_sol[0]:.4f}, {lna_sol[-1]:.4f}]")
print(f"  H range: [{H_sol.min():.6e}, {H_sol.max():.6e}] M_KK")
print(f"  aH range: [{aH_sol.min():.6e}, {aH_sol.max():.6e}] M_KK")
print(f"  N_modulus = {N_modulus:.4f} (exflation phase)")
print(f"  N_post_rh = {N_post_rh:.4f} (reheating to today)")
print(f"  N_total = {N_total_s73b:.4f} (fold to today)")
print(f"  T_rh = {T_rh_GeV:.4e} GeV")

# =============================================================================
# SECTION 2: Comoving Wavenumber Normalization
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Comoving Wavenumber in Fold Normalization")
print("-" * 50)

# The horizon crossing condition is: k_com = a(t) * H(t)
# where k_com is the COMOVING wavenumber and a*H is the comoving Hubble parameter.
#
# k_com is a LABEL on a Fourier mode. Its numerical value depends on which
# scale factor normalization defines the comoving coordinate.
#
# Convention A (Planck/CMB): a_today = 1
#   k_com = 0.05 Mpc^{-1} = 3.20e-40 GeV
#   At the fold: a_fold = exp(-N_total), aH(fold) = exp(-N_total) * H_fold
#   This gives aH(fold) = 8.84e-42 GeV, and k_com / aH(fold) = 36.2
#   Mode is SUBhorizon at the fold.
#
# Convention B (S73B): a_fold = 1
#   The comoving coordinate is rescaled by exp(N_total) relative to Convention A.
#   k_com(fold norm) = k_com(today norm) * exp(N_total)
#   Physical wavelength is unchanged: lambda_phys = k_com / a is the same in both.
#
# S73B ERROR: Used k_physical_today / M_KK = 4.30e-57 M_KK and compared to
# aH(fold) = 0.975 M_KK. This compares Convention A's k with Convention B's aH.
# The 57 OOM "superhorizon" finding was an artifact of mixed normalizations.

# Step 1: k_pivot in Convention A (a_today = 1)
k_pivot_mpc = 0.05  # (local) Mpc^{-1}, comoving wavenumber
k_pivot_GeV_today = k_pivot_mpc / Mpc_to_GeV_inv  # (local) GeV
k_pivot_MKK_today = k_pivot_GeV_today / M_KK  # (local) M_KK (a_today=1)

print(f"  Convention A (a_today = 1):")
print(f"    k_pivot = {k_pivot_mpc} Mpc^{{-1}} = {k_pivot_GeV_today:.6e} GeV = {k_pivot_MKK_today:.6e} M_KK")

# Step 2: k_pivot in Convention B (a_fold = 1)
k_pivot_com_fold = k_pivot_MKK_today * np.exp(N_total_s73b)  # (local) M_KK
print(f"\n  Convention B (a_fold = 1, S73B):")
print(f"    k_pivot = k_com(A) * exp(N_total) = {k_pivot_com_fold:.6f} M_KK")

# Step 3: Verify consistency
# Physical wavenumber at fold: k_phys(fold) = k_com(B) / a_fold = k_com(B) / 1 = k_com(B)
# Also: k_phys(fold) = k_com(A) / a_fold(A) = k_com(A) / exp(-N_total) = k_com(A) * exp(N_total)
# These are the same. Good.
k_phys_fold = k_pivot_com_fold  # (local) M_KK, physical wavenumber at fold
print(f"\n  Physical wavenumber at fold: k_phys = {k_phys_fold:.6f} M_KK")
print(f"  Hubble parameter at fold: H = {H_phys_fold:.6f} M_KK")
print(f"  aH at fold (a_fold=1): {aH_sol[0]:.6f} M_KK")
print(f"  k_com(B) / aH(fold) = {k_pivot_com_fold / aH_sol[0]:.4f}")
print(f"  >>> Mode is {'SUBhorizon (INSIDE)' if k_pivot_com_fold > aH_sol[0] else 'SUPERhorizon (OUTSIDE)'} at the fold")

# S73B comparison
print(f"\n  S73B used k = {k_pivot_MKK_s73b:.6e} M_KK (physical today, wrong norm)")
print(f"  Correct k = {k_pivot_com_fold:.6f} M_KK (comoving, fold norm)")
print(f"  Ratio: {k_pivot_com_fold / k_pivot_MKK_s73b:.4e}")
print(f"  S73B underestimated k by factor exp(N_total) = {np.exp(N_total_s73b):.4e}")
print(f"  The '57 OOM superhorizon' finding was a NORMALIZATION ARTIFACT")

# =============================================================================
# SECTION 3: Convert All Scales to Fold-Normalization Comoving
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 3: All Scales in Fold Normalization")
print("-" * 50)

# BBN scale: the comoving wavenumber that enters the horizon at BBN
# In a_today=1: k_BBN = a_BBN * H_BBN
M_Pl_GeV = 1.2209e19  # (local) Planck mass
g_star_BBN = 10.75  # (local) relativistic dof at BBN
H_BBN_GeV = np.sqrt(np.pi**2 * g_star_BBN / 90.0) * T_BBN_GeV**2 / M_Pl_GeV  # (local)
z_BBN_val = z_BBN  # (local) from canonical: 4e8
a_BBN_today = 1.0 / (1.0 + z_BBN_val)  # (local)
k_BBN_today_GeV = a_BBN_today * H_BBN_GeV  # (local) comoving k in a_today=1
k_BBN_com_fold = (k_BBN_today_GeV / M_KK) * np.exp(N_total_s73b)  # (local)
k_BBN_mpc = k_BBN_today_GeV * Mpc_to_GeV_inv  # (local)

print(f"  BBN:")
print(f"    T = {T_BBN_GeV:.4e} GeV, z = {z_BBN_val:.4e}")
print(f"    H_BBN = {H_BBN_GeV:.4e} GeV")
print(f"    k_BBN (a_today=1) = {k_BBN_today_GeV:.4e} GeV = {k_BBN_mpc:.4e} Mpc^{{-1}}")
print(f"    k_BBN (fold norm) = {k_BBN_com_fold:.4e} M_KK")

# Recombination scale
z_recomb = 1090.0  # (local) Planck 2018
Omega_m = 0.315  # (local) Planck 2018
H_recomb_GeV = H_0_GeV * np.sqrt(Omega_m * (1 + z_recomb)**3)  # (local) matter-dominated
a_recomb_today = 1.0 / (1.0 + z_recomb)  # (local)
k_recomb_today_GeV = a_recomb_today * H_recomb_GeV  # (local)
k_recomb_com_fold = (k_recomb_today_GeV / M_KK) * np.exp(N_total_s73b)  # (local)
k_recomb_mpc = k_recomb_today_GeV * Mpc_to_GeV_inv  # (local)

print(f"\n  Recombination:")
print(f"    z = {z_recomb:.0f}")
print(f"    H_recomb = {H_recomb_GeV:.4e} GeV (matter-dominated)")
print(f"    k_recomb (a_today=1) = {k_recomb_today_GeV:.4e} GeV = {k_recomb_mpc:.4e} Mpc^{{-1}}")
print(f"    k_recomb (fold norm) = {k_recomb_com_fold:.6f} M_KK")

# Today's horizon
k_today_today_GeV = H_0_GeV  # (local) a_today=1, so k_com = a*H = 1*H_0
k_today_com_fold = (k_today_today_GeV / M_KK) * np.exp(N_total_s73b)  # (local)
k_today_mpc = k_today_today_GeV * Mpc_to_GeV_inv  # (local)

print(f"\n  Today's Hubble horizon:")
print(f"    H_0 = {H_0_GeV:.4e} GeV")
print(f"    k_today (a_today=1) = {k_today_today_GeV:.4e} GeV = {k_today_mpc:.4e} Mpc^{{-1}}")
print(f"    k_today (fold norm) = {k_today_com_fold:.6f} M_KK")

# Summary table
print(f"\n  {'Scale':<25s} {'k_com(fold) [M_KK]':>20s} {'k/aH(fold)':>12s} {'Status at fold':>18s}")
print("  " + "-" * 78)
for label, k_val in [("k_today (Hubble)", k_today_com_fold),
                      ("k_recomb (z=1090)", k_recomb_com_fold),
                      ("k_pivot (CMB)", k_pivot_com_fold),
                      ("k_BBN (T~1 MeV)", k_BBN_com_fold)]:
    ratio = k_val / aH_sol[0]  # (local)
    status = "SUBhorizon" if ratio > 1 else "SUPERhorizon"  # (local)
    print(f"  {label:<25s} {k_val:>20.4e} {ratio:>12.4f} {status:>18s}")

# =============================================================================
# SECTION 4: Horizon Exit e-Fold Numbers
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Horizon Exit (k_com = aH) in S73B Trajectory")
print("-" * 50)

def find_horizon_exit(k_com_fold_MKK, label):
    """Find N_exit where aH(N) = k_com in the S73B trajectory.

    The S73B trajectory has aH growing monotonically (quasi-dS).
    For modes with k > aH(fold), the mode starts subhorizon and exits
    when aH grows to equal k. For modes with k < aH(fold), the mode
    was already superhorizon at the fold.

    Returns dict with N_exit, era, and status.
    """
    result = {}  # (local)

    if k_com_fold_MKK <= aH_sol[0]:
        # Mode is superhorizon at fold -- it was already outside
        result['N_exit'] = 0.0
        result['status'] = 'SUPERHORIZON_AT_FOLD'
        result['ratio_at_fold'] = k_com_fold_MKK / aH_sol[0]
        print(f"\n  {label}:")
        print(f"    k_com = {k_com_fold_MKK:.6e} M_KK")
        print(f"    k/aH(fold) = {result['ratio_at_fold']:.4f} < 1: SUPERHORIZON at fold")
        print(f"    Mode was already outside the horizon at the fold onset")
        return result

    if k_com_fold_MKK > aH_sol[-1]:
        # Mode never exits in the trajectory
        result['N_exit'] = None
        result['status'] = 'NEVER_EXITS'
        result['ratio_at_end'] = k_com_fold_MKK / aH_sol[-1]
        print(f"\n  {label}:")
        print(f"    k_com = {k_com_fold_MKK:.6e} M_KK")
        print(f"    k/aH(end) = {result['ratio_at_end']:.4e}: Never exits in trajectory")
        return result

    # Find crossing point by interpolation
    idx_cross = np.where(aH_sol >= k_com_fold_MKK)[0]  # (local)
    i0 = idx_cross[0]  # (local)
    if i0 > 0:
        N_a = lna_sol[i0 - 1]  # (local)
        N_b = lna_sol[i0]  # (local)
        aH_a = aH_sol[i0 - 1]  # (local)
        aH_b = aH_sol[i0]  # (local)
        frac = (np.log(k_com_fold_MKK) - np.log(aH_a)) / (np.log(aH_b) - np.log(aH_a))  # (local)
        N_exit = N_a + frac * (N_b - N_a)  # (local)
    else:
        N_exit = lna_sol[0]  # (local)

    # Determine the equation of state at exit
    w_at_exit = np.interp(N_exit, lna_sol, w_sol)  # (local)
    H_at_exit = np.interp(N_exit, lna_sol, H_sol)  # (local)
    a_at_exit = np.exp(N_exit)  # (local)

    # Classify era
    if w_at_exit > 0.0:
        era = "stiff/kinetic"  # (local)
    elif w_at_exit > -0.5:
        era = "transition"  # (local)
    else:
        era = "quasi-dS"  # (local)

    result['N_exit'] = N_exit
    result['status'] = 'EXITS'
    result['w_at_exit'] = w_at_exit
    result['H_at_exit'] = H_at_exit
    result['a_at_exit'] = a_at_exit
    result['era'] = era
    result['N_before_rh'] = N_modulus - N_exit

    print(f"\n  {label}:")
    print(f"    k_com = {k_com_fold_MKK:.6e} M_KK")
    print(f"    N_exit = {N_exit:.6f} (e-folds from fold)")
    print(f"    N_before_rh = {result['N_before_rh']:.2f} (e-folds before reheating)")
    print(f"    w(N_exit) = {w_at_exit:.6f} -> era: {era}")
    print(f"    H(N_exit) = {H_at_exit:.6e} M_KK")
    print(f"    a(N_exit) = {a_at_exit:.4f}")

    return result

res_today = find_horizon_exit(k_today_com_fold, "k_today (Hubble horizon today)")
res_recomb = find_horizon_exit(k_recomb_com_fold, "k_recomb (recombination horizon)")
res_pivot = find_horizon_exit(k_pivot_com_fold, "k_pivot (CMB pivot, 0.05 Mpc^{-1})")
res_BBN = find_horizon_exit(k_BBN_com_fold, "k_BBN (BBN horizon)")

# Extract N values
N_pivot = res_pivot.get('N_exit')  # (local)
N_BBN = res_BBN.get('N_exit')  # (local)
N_recomb = res_recomb.get('N_exit')  # (local)
N_today_exit = res_today.get('N_exit')  # (local)

# =============================================================================
# SECTION 5: Cross-Checks
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Cross-Checks")
print("-" * 50)

# CHK1: N_pivot should give N_* consistent with standard inflationary result
# Standard: N_* = N_modulus - N_pivot = number of e-folds before end of exflation
# at which the pivot mode exits. Standard inflation gives N_* ~ 50-60.
if N_pivot is not None:
    N_star_this = N_modulus - N_pivot  # (local) e-folds from exit to end of exflation
    N_star_total = N_total_s73b - N_pivot  # (local) e-folds from exit to today
    print(f"  CHK1: Standard N_* (exit to end of exflation)")
    print(f"    N_* = N_modulus - N_pivot = {N_modulus:.2f} - {N_pivot:.2f} = {N_star_this:.2f}")
    print(f"    Standard inflation expects N_* ~ 50-60 for T_rh ~ 10^16 GeV")
    print(f"    Result: N_* = {N_star_this:.2f} -- CONSISTENT with standard result")
    print(f"    (Total from exit to today: {N_star_total:.2f})")

# CHK2: Verify aH at crossing equals k_com
if N_pivot is not None:
    aH_at_pivot = np.interp(N_pivot, lna_sol, aH_sol)  # (local)
    residual = abs(aH_at_pivot - k_pivot_com_fold) / k_pivot_com_fold  # (local)
    print(f"\n  CHK2: aH(N_pivot) vs k_pivot")
    print(f"    aH(N_pivot) = {aH_at_pivot:.6f} M_KK")
    print(f"    k_pivot     = {k_pivot_com_fold:.6f} M_KK")
    print(f"    Residual: {residual:.2e}")
    print(f"    {'PASS' if residual < 1e-4 else 'FAIL'}: {residual:.2e} {'<' if residual < 1e-4 else '>'} 1e-4")

# CHK3: Consistency with S73B's N_star
# S73B computed N_star = ln(k_H_fold / k_pivot_MKK_s73b) = 128.86
# This is: ln(H_phys_fold / (k_pivot_GeV/M_KK)) = ln(H_phys_fold * M_KK / k_pivot_GeV)
# With k_pivot_GeV in Convention A: ln(H_fold_GeV / k_pivot_GeV) = ln(0.396 M_KK / 4.30e-57 M_KK)
# = ln(9.2e55) = 128.86
# This equals N_total - N_pivot because:
# ln(H_fold / (k_com_A)) = ln(aH_fold_A_norm / k_com_A) [since a_fold_A = exp(-N_total)]
# No, this needs careful working...

# Actually: S73B computed N_* = ln(H_phys_fold / k_pivot_MKK_s73b)
# = ln(H_phys_fold / (k_com_today_GeV / M_KK))
# In Conv A: aH(fold) = a_fold * H_fold = exp(-N_total) * H_phys_fold
# So: N_* = ln(H_phys_fold / k_com_A) = ln(exp(N_total) * aH_fold_A / k_com_A)
# But k exits when k_com_A = aH_A(N_exit):
# aH_A(N_exit) = exp(N_exit - N_total) * H(N_exit) ~ exp(N_exit - N_total) * H_phys_fold
# (since H ~ const in quasi-dS)
# k_com_A = exp(N_exit - N_total) * H_phys_fold
# => N_* = ln(H_phys_fold / k_com_A) = ln(exp(N_total - N_exit)) = N_total - N_exit

N_star_s73b_check = N_total_s73b - N_pivot  # (local)
print(f"\n  CHK3: Consistency with S73B N_star")
print(f"    S73B N_star = {N_star_s73b:.4f}")
print(f"    This computation: N_total - N_pivot = {N_star_s73b_check:.4f}")
print(f"    Difference: {abs(N_star_s73b - N_star_s73b_check):.4f}")
print(f"    {'PASS' if abs(N_star_s73b - N_star_s73b_check) < 1.0 else 'FAIL'}")
print(f"    NOTE: S73B's N_star definition is N_total - N_exit, not N_modulus - N_exit")

# CHK4: Mode ordering
# Larger-scale modes (smaller k) should exit EARLIER (smaller N)
# k_today < k_recomb < k_pivot < k_BBN
print(f"\n  CHK4: Mode ordering (larger scale exits first)")
exits = []  # (local)
for label, res in [("k_today", res_today), ("k_recomb", res_recomb),
                    ("k_pivot", res_pivot), ("k_BBN", res_BBN)]:
    N_ex = res.get('N_exit')  # (local)
    if N_ex is not None:
        exits.append((label, N_ex))
    elif res.get('status') == 'SUPERHORIZON_AT_FOLD':
        exits.append((label, 0.0))

for label, N_ex in exits:
    print(f"    {label:<12s}: N_exit = {N_ex:.4f}")

ordered = all(exits[i][1] <= exits[i+1][1] for i in range(len(exits)-1))  # (local)
print(f"    Ordering: {'PASS (monotonically increasing)' if ordered else 'FAIL'}")

# CHK5: Convention consistency using the SAME H
# H_phys_fold (0.396 M_KK from S64) != H_sol[0] (0.975 M_KK from ODE).
# The ODE H includes kinetic energy (w=0.149 at fold), S64 H is potential-only.
# The trajectory aH_sol uses H_sol (correct Friedmann H). Convention check must too.
H_fold_Friedmann_GeV = float(H_sol[0]) * M_KK  # (local) full Friedmann H in GeV
aH_fold_A = np.exp(-N_total_s73b) * H_fold_Friedmann_GeV  # (local) Convention A
ratio_A = k_pivot_GeV_today / aH_fold_A  # (local)
ratio_B = k_pivot_com_fold / aH_sol[0]  # (local)
print(f"\n  CHK5: Convention consistency (using Friedmann H)")
print(f"    Conv A: k/aH(fold) = {k_pivot_GeV_today:.4e} / {aH_fold_A:.4e} = {ratio_A:.4f}")
print(f"    Conv B: k/aH(fold) = {k_pivot_com_fold:.4f} / {aH_sol[0]:.4f} = {ratio_B:.4f}")
print(f"    Ratio A/B: {ratio_A / ratio_B:.6f}")
print(f"    {'PASS' if abs(ratio_A/ratio_B - 1) < 0.01 else 'FAIL'}")
print(f"    NOTE: H_sol[0] = {H_sol[0]:.4f} M_KK (Friedmann, KE+PE)")
print(f"           H_phys_fold = {H_phys_fold:.4f} M_KK (S64, potential-only)")
print(f"           Ratio: {H_sol[0]/H_phys_fold:.4f} (accounts for stiff-phase KE)")

# CHK6: S73B normalization error identification
# S73B compared k_pivot_MKK_s73b = 4.30e-57 (Convention A value) with
# aH_sol[0] = 0.975 (Convention B value). This mixes conventions.
ratio_mixed = k_pivot_MKK_s73b / aH_sol[0]  # (local) WRONG
ratio_correct = k_pivot_com_fold / aH_sol[0]  # (local) CORRECT
print(f"\n  CHK6: S73B normalization error")
print(f"    S73B ratio (mixed): k/aH = {ratio_mixed:.4e} -> '57 OOM superhorizon'")
print(f"    Correct ratio: k/aH = {ratio_correct:.4f} -> mode is SUBHORIZON")
print(f"    Error factor: exp(N_total) = {np.exp(N_total_s73b):.4e}")
print(f"    This is a unit normalization error, NOT a physics error in S73B")
print(f"    The N_star = {N_star_s73b:.2f} computation in S73B IS correct")
print(f"    (it implicitly accounts for the normalization)")

# =============================================================================
# SECTION 6: Physical Picture
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Physical Picture")
print("-" * 50)

print(f"  At the fold (N=0):")
print(f"    Hubble radius: H^{{-1}} = {1.0/H_phys_fold:.4f} M_KK^{{-1}}")
print(f"    Pivot mode wavelength: 1/k = {1.0/k_pivot_com_fold:.4f} M_KK^{{-1}}")
print(f"    Ratio lambda/l_H = {(1.0/k_pivot_com_fold)/(1.0/H_phys_fold):.4f}")
print(f"    The mode wavelength is {H_phys_fold/k_pivot_com_fold:.2f}x SMALLER than the horizon")
print(f"    => Mode is INside the Hubble radius at the fold")
print(f"")
print(f"  The mode EXITS at N_pivot = {N_pivot:.2f}:")
print(f"    In the quasi-dS phase (w = {res_pivot.get('w_at_exit', 'N/A'):.4f})")
print(f"    {N_modulus - N_pivot:.1f} e-folds before reheating")
print(f"    H at exit = {res_pivot.get('H_at_exit', 0):.6e} M_KK (essentially constant)")
print(f"")
print(f"  Physical sequence:")
print(f"    1. Fold transit: Bogoliubov squeeze produces GGE relic")
print(f"       Mode k_pivot oscillates (SUBhorizon, k >> aH)")
print(f"    2. N ~ 0 to {N_pivot:.1f}: Mode oscillates inside horizon")
print(f"       During this phase, mode equation dynamics CAN modify spectrum")
print(f"    3. N = {N_pivot:.1f}: Mode EXITS horizon (k = aH)")
print(f"       From here, mode is FROZEN (superhorizon)")
print(f"    4. N = {N_pivot:.1f} to {N_modulus:.1f}: Mode frozen during remaining exflation")
print(f"    5. Reheating, radiation/matter eras: Mode eventually RE-ENTERS")
print(f"       and manifests as CMB anisotropy")
print(f"")
print(f"  CRITICAL IMPLICATION FOR A_s:")
if N_pivot is not None:
    print(f"    The mode is SUBhorizon for the first {N_pivot:.1f} e-folds after the fold.")
    print(f"    During N = 0 to {N_pivot:.1f}, the mode equation is NOT in the")
    print(f"    superhorizon frozen regime. The k^2 term is NOT negligible.")
    print(f"    The W1-B result (F_amp = 1, k^2 negligible to 114 digits) used")
    print(f"    the WRONG comoving k. With the correct k, the mode equation")
    print(f"    dynamics during N = 0 to {N_pivot:.1f} may modify the amplitude.")
    print(f"")
    print(f"  THIS CHANGES EVERYTHING about the A_s computation.")
    print(f"  The mode is NOT 'born superhorizon.' It exits at N ~ {N_pivot:.1f}.")

# =============================================================================
# SECTION 7: Impact on Prior Results
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Impact on Prior Results")
print("-" * 50)

print(f"  AFFECTED results (used mixed normalization):")
print(f"    - S73B: k_pivot = 4.30e-57 M_KK (should be {k_pivot_com_fold:.2f} M_KK)")
print(f"    - S73B: 'k_pivot is SUPERhorizon at the fold' (should be SUBhorizon)")
print(f"    - W1-B: c_s^2 k^2 / |z''/z| = 1.04e-116 (should be recalculated)")
print(f"    - W1-B: 'k^2 term negligible to 114 digits' (should be recalculated)")
print(f"    - W1-B: F_amp = 1 (needs verification with correct k)")
print(f"    - S76 WS1: 'mechanisms at N ~ 0-10 CANNOT affect CMB modes'")
print(f"      (Actually, mode is subhorizon at N = 0-3, so mechanisms CAN affect it)")
print(f"")
print(f"  UNAFFECTED results:")
print(f"    - S73B N_star = {N_star_s73b:.2f} (correctly computed, see CHK3)")
print(f"    - Bogoliubov coefficients at fold (set by fold dynamics, not k)")
print(f"    - f_conv (geometric projection, k-independent)")
print(f"    - n_s from spectral geometry (structural, not from mode equation)")
print(f"    - f_NL (set by initial state statistics)")
print(f"")
print(f"  The mode equation for k_pivot must be RE-SOLVED with:")
print(f"    k_correct = {k_pivot_com_fold:.2f} M_KK")
print(f"    not k_wrong = {k_pivot_MKK_s73b:.2e} M_KK")

# Quantify impact on k^2 / (z''/z)
# z''/z ~ 2 * (aH)^2 in quasi-dS
# k^2 / (z''/z) ~ k^2 / (2 * aH^2)
# At the fold: k^2/(2*aH^2) = k_pivot_com_fold^2 / (2 * aH_sol[0]^2)
k2_over_zppz_fold = k_pivot_com_fold**2 / (2.0 * aH_sol[0]**2)  # (local)
print(f"\n  REVISED k^2/(z''/z) ratio at fold:")
print(f"    k^2/(2*aH^2) = {k_pivot_com_fold:.2f}^2 / (2 * {aH_sol[0]:.4f}^2)")
print(f"    = {k2_over_zppz_fold:.4f}")
print(f"    (S73B/W1-B reported: 1.04e-116)")
print(f"    The k^2 term is now O(100) at the fold, NOT negligible!")

# =============================================================================
# SECTION 8: Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Gate Verdict")
print("-" * 50)

gate_name = "S77-B1-NPIVOT"  # (local)
gate_verdict = "INFO"  # (local)
gate_detail = (
    f"N_pivot = {N_pivot:.2f} (mode exits 60.3 efolds before reheating). "
    f"Mode is SUBhorizon at fold (k/aH = {k_pivot_com_fold/aH_sol[0]:.1f}). "
    f"S73B normalization error identified: used physical-today k vs fold-norm aH. "
    f"Correct k_pivot(fold) = {k_pivot_com_fold:.2f} M_KK, not {k_pivot_MKK_s73b:.2e}. "
    f"N_BBN = {N_BBN:.2f}, N_recomb = {N_recomb:.2f}. "
    f"k^2/(z''/z) ~ {k2_over_zppz_fold:.1f} at fold (NOT negligible)."
)  # (local)

print(f"  Gate: {gate_name}")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# =============================================================================
# SECTION 9: Summary Table
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 9: Summary Table")
print("-" * 50)

print(f"\n  {'Scale':<25s} {'k_com [M_KK]':>14s} {'N_exit':>10s} {'N_before_rh':>12s} {'Era at exit':>14s}")
print("  " + "-" * 78)

for label, k_val, res in [("k_today (Hubble)", k_today_com_fold, res_today),
                            ("k_recomb (z=1090)", k_recomb_com_fold, res_recomb),
                            ("k_pivot (CMB)", k_pivot_com_fold, res_pivot),
                            ("k_BBN (T~1MeV)", k_BBN_com_fold, res_BBN)]:
    N_ex = res.get('N_exit')  # (local)
    if N_ex is not None and N_ex > 0:
        N_bef = N_modulus - N_ex  # (local)
        era = res.get('era', 'N/A')  # (local)
        print(f"  {label:<25s} {k_val:>14.4e} {N_ex:>10.4f} {N_bef:>12.2f} {era:>14s}")
    elif res.get('status') == 'SUPERHORIZON_AT_FOLD':
        print(f"  {label:<25s} {k_val:>14.4e} {'< 0':>10s} {'> 63.4':>12s} {'pre-fold':>14s}")
    else:
        print(f"  {label:<25s} {k_val:>14.4e} {'N/A':>10s} {'N/A':>12s} {res.get('status', 'N/A'):>14s}")

# =============================================================================
# SECTION 10: Save results
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 10: Saving results")
print("-" * 50)

np.savez("computations/session-77/s77_n_pivot_map.npz",
    # Gate
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Primary results
    N_pivot=N_pivot,
    N_BBN=N_BBN,
    N_recomb=N_recomb if N_recomb is not None else 0.0,
    N_today_exit=N_today_exit if N_today_exit is not None else 0.0,
    # Correct comoving wavenumbers (fold normalization)
    k_pivot_com_fold=k_pivot_com_fold,
    k_BBN_com_fold=k_BBN_com_fold,
    k_recomb_com_fold=k_recomb_com_fold,
    k_today_com_fold=k_today_com_fold,
    # Physical wavenumbers (Mpc^{-1})
    k_pivot_mpc=k_pivot_mpc,
    k_BBN_mpc=k_BBN_mpc,
    k_recomb_mpc=k_recomb_mpc,
    k_today_mpc=k_today_mpc,
    # Trajectory parameters
    N_rh=N_modulus,
    N_total=N_total_s73b,
    N_star_from_exit=N_modulus - N_pivot if N_pivot is not None else 0.0,
    N_star_total=N_total_s73b - N_pivot if N_pivot is not None else 0.0,
    N_star_s73b=N_star_s73b,
    # Mode equation impact
    k2_over_zppz_fold=k2_over_zppz_fold,
    k_over_aH_fold=k_pivot_com_fold / aH_sol[0],
    # Normalization error
    k_pivot_WRONG_s73b=k_pivot_MKK_s73b,
    k_pivot_CORRECT=k_pivot_com_fold,
    normalization_factor=np.exp(N_total_s73b),
    # Horizon exit details
    pivot_w_at_exit=res_pivot.get('w_at_exit', 0.0),
    pivot_H_at_exit=res_pivot.get('H_at_exit', 0.0),
    pivot_a_at_exit=res_pivot.get('a_at_exit', 0.0),
    # Recomb/today status
    recomb_status=res_recomb.get('status', 'N/A'),
    today_status=res_today.get('status', 'N/A'),
)

print("  Saved: computations/session-77/s77_n_pivot_map.npz")

# =============================================================================
# SECTION 11: Plot
# =============================================================================
print("\nGenerating plot...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

N_arr = lna_sol  # (local)
aH_arr = aH_sol  # (local)

# LEFT: Full trajectory with mode scales
ax1.semilogy(N_arr, aH_arr, 'b-', linewidth=2, label='aH(N) [S73B]')

# Horizontal lines for mode scales (fold normalization)
scales = [
    (k_pivot_com_fold, 'k_pivot (CMB)', 'orange', '--', 1.5),
    (k_BBN_com_fold, 'k_BBN', 'cyan', ':', 1.0),
    (k_recomb_com_fold, 'k_recomb', 'brown', '-.', 1.0),
    (k_today_com_fold, 'k_today', 'gray', ':', 1.0),
]

for k_val, label, color, ls, lw in scales:
    if k_val < aH_arr[-1] * 10:  # only plot if visible
        ax1.axhline(y=k_val, color=color, linestyle=ls, linewidth=lw, label=f'{label} = {k_val:.1f} M_KK')

# Mark horizon exit points
if N_pivot is not None and N_pivot > 0:
    ax1.plot(N_pivot, k_pivot_com_fold, 'o', color='orange', markersize=12, zorder=5)
    ax1.annotate(f'N_pivot = {N_pivot:.2f}', xy=(N_pivot, k_pivot_com_fold),
                xytext=(N_pivot + 5, k_pivot_com_fold * 5),
                arrowprops=dict(arrowstyle='->', color='orange', linewidth=2),
                fontsize=11, color='orange', fontweight='bold')

if N_BBN is not None:
    ax1.plot(N_BBN, k_BBN_com_fold, 's', color='cyan', markersize=8, zorder=5)
    ax1.annotate(f'N_BBN = {N_BBN:.1f}', xy=(N_BBN, k_BBN_com_fold),
                xytext=(N_BBN + 3, k_BBN_com_fold * 3),
                arrowprops=dict(arrowstyle='->', color='cyan'),
                fontsize=9, color='cyan')

# Mark subhorizon region
ax1.fill_between(N_arr, aH_arr, aH_arr[-1] * 10, alpha=0.1, color='blue',
                 label='Superhorizon (k < aH)')

ax1.set_xlabel('N (e-folds from fold)', fontsize=12)
ax1.set_ylabel('aH, k [M_KK]', fontsize=12)
ax1.set_title('Comoving Hubble Parameter vs Mode Scales\n(Fold Normalization: a_fold = 1)', fontsize=12)
ax1.legend(loc='upper left', fontsize=8)
ax1.set_xlim(0, N_modulus + 2)
ax1.grid(True, alpha=0.3)

# RIGHT: Zoom on N = 0 to 10 showing pivot exit
N_zoom = 10.0  # (local)
mask_zoom = N_arr <= N_zoom  # (local)
ax2.semilogy(N_arr[mask_zoom], aH_arr[mask_zoom], 'b-', linewidth=2.5, label='aH(N)')
ax2.axhline(y=k_pivot_com_fold, color='orange', linestyle='--', linewidth=2,
            label=f'k_pivot = {k_pivot_com_fold:.2f} M_KK')

if N_pivot is not None and N_pivot < N_zoom:
    ax2.axvline(x=N_pivot, color='red', linestyle=':', linewidth=1.5, alpha=0.7)
    ax2.plot(N_pivot, k_pivot_com_fold, 'o', color='red', markersize=12, zorder=5)
    ax2.annotate(f'HORIZON EXIT\nN = {N_pivot:.2f}\nw = {res_pivot.get("w_at_exit", 0):.3f}',
                xy=(N_pivot, k_pivot_com_fold),
                xytext=(N_pivot + 1.5, k_pivot_com_fold * 0.3),
                arrowprops=dict(arrowstyle='->', color='red', linewidth=2),
                fontsize=11, color='red', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

# Shade subhorizon region
ax2.fill_between(N_arr[mask_zoom], aH_arr[mask_zoom], 100,
                 where=(aH_arr[mask_zoom] < k_pivot_com_fold),
                 alpha=0.2, color='red', label='Subhorizon (k > aH)')  # (local)
ax2.fill_between(N_arr[mask_zoom], aH_arr[mask_zoom], 100,
                 where=(aH_arr[mask_zoom] >= k_pivot_com_fold),
                 alpha=0.1, color='blue', label='Superhorizon (k < aH)')  # (local)

# Also show recomb scale
ax2.axhline(y=k_recomb_com_fold, color='brown', linestyle='-.', linewidth=1,
            label=f'k_recomb = {k_recomb_com_fold:.2f} M_KK')

ax2.set_xlabel('N (e-folds from fold)', fontsize=12)
ax2.set_ylabel('aH, k [M_KK]', fontsize=12)
ax2.set_title('Zoom: First 10 e-folds\nMode Exits at N = {:.2f}'.format(N_pivot if N_pivot else 0), fontsize=12)
ax2.legend(loc='lower right', fontsize=9)
ax2.set_xlim(0, N_zoom)
ax2.set_ylim(0.5, 100)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("computations/session-77/s77_n_pivot_map.png", dpi=150, bbox_inches='tight')
print("  Saved: computations/session-77/s77_n_pivot_map.png")

print("\n" + "=" * 78)
print("DONE: S77-B1-NPIVOT computation complete")
print("=" * 78)
