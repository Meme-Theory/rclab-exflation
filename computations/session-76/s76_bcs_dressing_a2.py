#!/usr/bin/env python3
"""
s76_bcs_dressing_a2.py -- BCS-DRESSING-OF-A2-76: BCS Correction to a_2/a_0 Ratio
==================================================================================

Gate: S76-B4-BCS-DRESS
  PASS: A_s(BCS-corrected) in [1.8e-9, 2.4e-9]
  FAIL: |delta_a_2/a_2| < 0.001 (BCS correction negligible)
  INFO: correction has right sign but wrong magnitude

Physics
-------
The spectral scalar amplitude conversion factor f_conv depends on the
spectral moment ratio:

    f_conv = (M_KK/M_Pl)^4 * (a_2/a_0)^2                               (1)

BCS pairing modifies a_2 because the heat kernel coefficient is:

    a_2 = sum_k d_{pq}^2 * lambda_k^{-2}                                (2)

The BCS condensate reorganizes eigenvalues near the Fermi surface.
For the 16 eigenvalues in the (0,0) singlet sector, the dressed
eigenvalue is:

    E_k = sqrt(epsilon_k^2 + Delta^2)                                    (3)

For all other sectors [(p,q) != (0,0), 155968 weighted eigenvalues]:
    E_k = |lambda_k|  (unchanged)                                        (4)

The BCS correction to a_2 is:

    delta_a_2 = sum_{k in (0,0)} [E_k^{-2} - epsilon_k^{-2}]           (5)
              = sum_{k in (0,0)} [1/(eps_k^2 + Delta^2) - 1/eps_k^2]
              = -sum_{k in (0,0)} Delta^2 / [eps_k^2 * (eps_k^2 + Delta^2)]

This is NEGATIVE: BCS pushes eigenvalues apart, reducing the
inverse-square spectral weight.

For A_s:
    delta(A_s)/A_s = delta(f_conv)/f_conv = 2 * delta(a_2)/a_2          (6)

So delta_a_2 < 0 implies f_conv DECREASES, A_s DECREASES (gap widens).

For CC (HP4): chi_2 involves M_1 = sum lambda_k (first spectral moment),
not a_2 directly. But a_2 enters via R_1 = a_0*a_4/a_2^2. Track both.

Cross-checks:
  CHK1: delta_a_2 -> 0 as Delta -> 0 (normal state limit)
  CHK2: |delta_a_2/a_2| < 1 (perturbative correction)
  CHK3: Sign is NEGATIVE (BCS pushes eigenvalues apart -> reduces sum k^{-2})
  CHK4: Magnitude consistent with S72v2 mode-selective result
  CHK5: Full recomputation from D_K spectrum agrees with analytic estimate

Author: Landau Condensed Matter Theorist
Session: S76, Wave 2 (W2-D)
"""

import numpy as np
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    # BCS parameters
    Delta_BCS, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
    Delta_B3,
    # Spectral action coefficients at fold
    a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    R_protected_fold,
    # Scales
    M_KK, M_KK_gravity,
    M_Pl_reduced, M_Pl_unreduced,
    tau_fold,
    # Cosmological
    A_s_CMB,
    # Geometry
    PI,
    # Transit
    H_fold,
)

# Import spectrum computation tools
from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8, collect_spectrum,
)
from spectral_action import dim_su3_irrep

print("=" * 78)
print("S76-B4-BCS-DRESS: BCS Correction to Spectral Moment Ratio a_2/a_0")
print("=" * 78)

# =============================================================================
# STEP 0: ANALYTIC ESTIMATE FROM 8-MODE BCS SUBSYSTEM
# =============================================================================
print("\n" + "-" * 78)
print("STEP 0: Analytic estimate of BCS correction to a_2")
print("-" * 78)

print("""
  The BCS condensate pairs modes in the (0,0) singlet sector.
  8 mode energies -> 16 eigenvalues (+/- pairs), d^2 = 1 for (0,0).

  Each mode contributes to a_2 via lambda^{-2}.
  BCS dressing: lambda -> E = sqrt(lambda^2 + Delta^2).

  delta_a_2 = sum_{modes} 2 * [1/(eps^2 + Delta^2) - 1/eps^2]
            = -sum_{modes} 2 * Delta^2 / [eps^2 * (eps^2 + Delta^2)]

  Factor 2 from +/- eigenvalue pairs.
""")

# Mode energies at the fold (M_KK units)
# 1 B1 mode, 4 B2 modes, 3 B3 modes = 8 modes total
eps_modes = np.array([
    E_B1,                                          # B1 (1 mode)
    E_B2_mean, E_B2_mean, E_B2_mean, E_B2_mean,   # B2 (4 modes)
    E_B3_mean, E_B3_mean, E_B3_mean,               # B3 (3 modes)
])  # (local)
n_modes_BCS = len(eps_modes)  # (local) = 8

Delta = Delta_BCS  # (local) = 0.4643 M_KK

print(f"  BCS gap: Delta = {Delta:.4f} M_KK")
print(f"  Mode energies (M_KK units):")
mode_labels = ['B1'] + ['B2']*4 + ['B3']*3  # (local)
for i, (label, eps) in enumerate(zip(mode_labels, eps_modes)):
    E_dressed = np.sqrt(eps**2 + Delta**2)  # (local)
    ratio = Delta**2 / (eps**2 * (eps**2 + Delta**2))  # (local)
    print(f"    {label}: eps = {eps:.6f}, E = {E_dressed:.6f}, "
          f"Delta^2/(eps^2*E^2) = {ratio:.6f}")

# Analytic delta_a_2 from 8-mode subsystem
# Each mode has +/- eigenvalue pair -> factor of 2
delta_a2_analytic = 0.0  # (local)
for eps in eps_modes:
    E_sq = eps**2 + Delta**2  # (local)
    # 1/E^2 - 1/eps^2 = -Delta^2 / (eps^2 * E^2)
    delta_per_mode = 1.0/E_sq - 1.0/eps**2  # (local)
    delta_a2_analytic += 2.0 * delta_per_mode  # factor 2 for +/- pair

# Bare a_2 from 8-mode subsystem only (for comparison)
a2_8mode_bare = 2.0 * np.sum(1.0 / eps_modes**2)  # (local) factor 2 for +/-

# Relative correction to FULL a_2
delta_a2_over_a2_full = delta_a2_analytic / a2_fold  # (local)

# Relative correction within 8-mode subsystem
delta_a2_over_a2_8mode = delta_a2_analytic / a2_8mode_bare  # (local)

print(f"\n  Analytic results:")
print(f"    delta_a2 (8-mode BCS) = {delta_a2_analytic:.6f}")
print(f"    a2_8mode_bare        = {a2_8mode_bare:.6f}")
print(f"    a2_fold (full)       = {a2_fold:.6f}")
print(f"    delta_a2 / a2_fold   = {delta_a2_over_a2_full:.6e} ({delta_a2_over_a2_full*100:.4f}%)")
print(f"    delta_a2 / a2_8mode  = {delta_a2_over_a2_8mode:.6e} ({delta_a2_over_a2_8mode*100:.2f}%)")

# Sign check
print(f"\n  Sign check: delta_a2 = {delta_a2_analytic:.6f} {'< 0 (CORRECT: BCS reduces a_2)' if delta_a2_analytic < 0 else '> 0 (UNEXPECTED)'}")

# =============================================================================
# STEP 1: FULL RECOMPUTATION FROM D_K SPECTRUM AT FOLD
# =============================================================================
print("\n" + "-" * 78)
print("STEP 1: Full recomputation from D_K eigenvalue spectrum at tau_fold")
print("-" * 78)

print("""
  Compute the FULL a_2 with and without BCS dressing by summing over
  ALL eigenvalues of D_K at tau = 0.19, with d_{pq}^2 weights.

  Mode-selective: only (0,0) sector gets BCS gap.
  All other sectors: E_k = |lambda_k| (unchanged).
""")

t0 = time.time()  # (local)

# Compute D_K spectrum at fold
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

_, eval_data = collect_spectrum(tau_fold, gens, f_abc, gammas, max_pq_sum=3,
                                verbose=True)

# Accumulate a_0, a_2, a_4 for bare and BCS-dressed spectra
# TWO weighting conventions:
#   PW (Peter-Weyl): weight = d_pq. This is the heat-kernel convention
#     used by extract_seeley_dewitt and the canonical a_2_fold = 2776.
#   SQ (squared): weight = d_pq^2. Used by S72 spectral action computation.
# Both give identical delta_a_2 for (0,0) because d_{(0,0)} = 1.
# The CANONICAL f_conv uses PW-weighted a_2/a_0, so we use PW for propagation.

# PW-weighted (canonical convention)
a0_bare_pw = 0.0  # (local)
a2_bare_pw = 0.0  # (local)
a4_bare_pw = 0.0  # (local)
a0_bcs_pw = 0.0  # (local)
a2_bcs_pw = 0.0  # (local)
a4_bcs_pw = 0.0  # (local)

# SQ-weighted (S72 convention, for cross-check)
a0_bare_sq = 0.0  # (local)
a2_bare_sq = 0.0  # (local)
a4_bare_sq = 0.0  # (local)
a0_bcs_sq = 0.0  # (local)
a2_bcs_sq = 0.0  # (local)
a4_bcs_sq = 0.0  # (local)

n_eigenvalues_total = 0  # (local)
n_eigenvalues_weighted_pw = 0  # (local)
n_eigenvalues_weighted_sq = 0  # (local)
n_eigenvalues_00 = 0  # (local)

# Track (0,0) sector contribution separately
a2_00_bare = 0.0  # (local)
a2_00_bcs = 0.0  # (local)
a4_00_bare = 0.0  # (local)
a4_00_bcs = 0.0  # (local)

for p, q, evals in eval_data:
    d_pq = dim_su3_irrep(p, q)  # (local)
    w_pw = d_pq      # (local) Peter-Weyl weight
    w_sq = d_pq**2   # (local) squared weight
    omega = np.abs(evals)  # (local) bare |lambda_k|
    n_ev = len(evals)  # (local)
    n_eigenvalues_total += n_ev
    n_eigenvalues_weighted_pw += w_pw * n_ev
    n_eigenvalues_weighted_sq += w_sq * n_ev

    mask = omega > 1e-12  # (local) exclude zero modes
    omega_nz = omega[mask]  # (local)

    # Bare contributions (both conventions)
    a0_bare_pw += w_pw * n_ev
    a2_bare_pw += w_pw * np.sum(1.0 / omega_nz**2)
    a4_bare_pw += w_pw * np.sum(1.0 / omega_nz**4)
    a0_bare_sq += w_sq * n_ev
    a2_bare_sq += w_sq * np.sum(1.0 / omega_nz**2)
    a4_bare_sq += w_sq * np.sum(1.0 / omega_nz**4)

    if p == 0 and q == 0:
        # (0,0) singlet sector -- apply BCS dressing
        n_eigenvalues_00 = n_ev
        E_bcs = np.sqrt(omega_nz**2 + Delta**2)  # (local)

        a2_00_bare = np.sum(1.0 / omega_nz**2)
        a2_00_bcs = np.sum(1.0 / E_bcs**2)
        a4_00_bare = np.sum(1.0 / omega_nz**4)
        a4_00_bcs = np.sum(1.0 / E_bcs**4)

        # BCS-dressed (both conventions, but d=1 so identical)
        a0_bcs_pw += w_pw * n_ev
        a2_bcs_pw += w_pw * np.sum(1.0 / E_bcs**2)
        a4_bcs_pw += w_pw * np.sum(1.0 / E_bcs**4)
        a0_bcs_sq += w_sq * n_ev
        a2_bcs_sq += w_sq * np.sum(1.0 / E_bcs**2)
        a4_bcs_sq += w_sq * np.sum(1.0 / E_bcs**4)
    else:
        # Spectator sector: no BCS gap
        a0_bcs_pw += w_pw * n_ev
        a2_bcs_pw += w_pw * np.sum(1.0 / omega_nz**2)
        a4_bcs_pw += w_pw * np.sum(1.0 / omega_nz**4)
        a0_bcs_sq += w_sq * n_ev
        a2_bcs_sq += w_sq * np.sum(1.0 / omega_nz**2)
        a4_bcs_sq += w_sq * np.sum(1.0 / omega_nz**4)

t_spectrum = time.time() - t0  # (local)

print(f"\n  Spectrum computation: {t_spectrum:.1f}s")
print(f"  Total eigenvalues: {n_eigenvalues_total}")
print(f"  PW-weighted eigenvalues: {n_eigenvalues_weighted_pw}")
print(f"  SQ-weighted eigenvalues: {n_eigenvalues_weighted_sq}")
print(f"  (0,0) sector eigenvalues: {n_eigenvalues_00}")
print(f"  Spectator eigenvalues: {n_eigenvalues_total - n_eigenvalues_00}")

# =============================================================================
# STEP 2: COMPUTE ALL CORRECTIONS AND PROPAGATE TO OBSERVABLES
# =============================================================================
print("\n" + "-" * 78)
print("STEP 2: BCS corrections to spectral moments and observables")
print("-" * 78)

print("""
  TWO weighting conventions compared:
    PW (Peter-Weyl): weight = dim(p,q). Used by heat-kernel extraction
      and canonical a_2_fold = 2776. This is the correct convention for f_conv.
    SQ (squared): weight = dim(p,q)^2. Used by S72 spectral action scripts.

  For (0,0) sector, dim = 1, so delta_a_2 is identical in both conventions.
  The denominator differs, changing the fractional correction.
""")

# Delta_a_2 from full spectrum (PW convention -- canonical)
delta_a2_pw = a2_bcs_pw - a2_bare_pw  # (local)
delta_a4_pw = a4_bcs_pw - a4_bare_pw  # (local)

# Delta_a_2 from full spectrum (SQ convention -- S72)
delta_a2_sq = a2_bcs_sq - a2_bare_sq  # (local)
delta_a4_sq = a4_bcs_sq - a4_bare_sq  # (local)

# Fractional corrections (PW -- canonical)
frac_a2 = delta_a2_pw / a2_bare_pw  # (local)
frac_a4 = delta_a4_pw / a4_bare_pw  # (local)

# Fractional corrections (SQ -- S72)
frac_a2_sq = delta_a2_sq / a2_bare_sq  # (local)
frac_a4_sq = delta_a4_sq / a4_bare_sq  # (local)

# Also compute relative to canonical a_2_fold (independent check)
frac_a2_canon = delta_a2_pw / a2_fold  # (local)

# Verify bare a_2(PW) matches canonical
a2_check_ratio = a2_bare_pw / a2_fold  # (local)
a4_check_ratio = a4_bare_pw / a4_fold  # (local)
a0_check_ratio = a0_bare_pw / a0_fold  # (local)

print(f"  BARE spectral moments (PW convention) at fold:")
print(f"    a_0(PW)  = {a0_bare_pw:.4f}   (canonical: {a0_fold:.1f}, ratio: {a0_check_ratio:.6f})")
print(f"    a_2(PW)  = {a2_bare_pw:.4f}  (canonical: {a2_fold:.4f}, ratio: {a2_check_ratio:.6f})")
print(f"    a_4(PW)  = {a4_bare_pw:.4f}  (canonical: {a4_fold:.4f}, ratio: {a4_check_ratio:.6f})")

print(f"\n  BARE spectral moments (SQ convention) at fold:")
print(f"    a_0(SQ)  = {a0_bare_sq:.4f}")
print(f"    a_2(SQ)  = {a2_bare_sq:.4f}")
print(f"    a_4(SQ)  = {a4_bare_sq:.4f}")

print(f"\n  BCS-DRESSED spectral moments (PW convention):")
print(f"    a_0(BCS) = {a0_bcs_pw:.4f}   (unchanged)")
print(f"    a_2(BCS) = {a2_bcs_pw:.4f}")
print(f"    a_4(BCS) = {a4_bcs_pw:.4f}")

print(f"\n  CORRECTIONS (PW -- canonical for f_conv):")
print(f"    delta_a_2         = {delta_a2_pw:.6f}")
print(f"    delta_a_4         = {delta_a4_pw:.6f}")
print(f"    delta_a_2 / a_2   = {frac_a2:.6e} ({frac_a2*100:.6f}%)")
print(f"    delta_a_4 / a_4   = {frac_a4:.6e} ({frac_a4*100:.6f}%)")
print(f"    delta_a_2 / a_2(canon) = {frac_a2_canon:.6e} ({frac_a2_canon*100:.6f}%)")

print(f"\n  CORRECTIONS (SQ -- S72 convention, for cross-check):")
print(f"    delta_a_2 / a_2   = {frac_a2_sq:.6e} ({frac_a2_sq*100:.6f}%)")
print(f"    delta_a_4 / a_4   = {frac_a4_sq:.6e} ({frac_a4_sq*100:.6f}%)")

print(f"\n  Note: delta_a_2(PW) = {delta_a2_pw:.6f}, delta_a_2(SQ) = {delta_a2_sq:.6f}")
print(f"  These are identical (d_(0,0)=1) confirming only the denominator differs.")

# Sign verification
sign_a2_ok = delta_a2_pw < 0  # (local) BCS should REDUCE a_2
print(f"\n  Sign check (delta_a_2 < 0): {'PASS' if sign_a2_ok else 'FAIL'} (delta_a_2 = {delta_a2_pw:.6e})")

# (0,0) sector detailed breakdown
delta_a2_00 = a2_00_bcs - a2_00_bare  # (local)
delta_a4_00 = a4_00_bcs - a4_00_bare  # (local)
print(f"\n  (0,0) sector breakdown:")
print(f"    a_2(0,0) bare = {a2_00_bare:.6f}")
print(f"    a_2(0,0) BCS  = {a2_00_bcs:.6f}")
print(f"    delta_a_2(0,0) = {delta_a2_00:.6f}")
print(f"    Fraction of total a_2(PW) from (0,0): {a2_00_bare/a2_bare_pw*100:.4f}%")

# =============================================================================
# STEP 3: PROPAGATE TO A_s AND CC
# =============================================================================
print("\n" + "-" * 78)
print("STEP 3: Propagation to A_s and Cosmological Constant predictions")
print("-" * 78)

# --- A_s via f_conv ---
print("\n  === A_s prediction ===")
print(f"  f_conv = (M_KK/M_Pl)^4 * (a_2/a_0)^2")
print(f"  Using CANONICAL a_2_fold/a_0_fold (PW/heat-kernel convention)")

# W1-F uses M_Pl_unreduced (= 1.221e19 GeV), NOT M_Pl_reduced (= 2.435e18 GeV).
# f_KK = (M_KK/M_Pl)^4 = (6.085e-3)^4 = 1.371e-9 per W1-F.
f_KK = (M_KK / M_Pl_unreduced)**4  # (local) KK hierarchy factor, using M_Pl (unreduced)

# Bare f_conv: use canonical values (matches W1-F exactly)
f_spec_bare = (a2_fold / a0_fold)**2  # (local) spectral projection (bare)
f_conv_bare = f_KK * f_spec_bare  # (local)

# BCS-corrected: shift a_2 by delta_a_2 from (0,0) sector
# The delta_a_2 is an ABSOLUTE shift, same in both PW and SQ conventions
# because d_(0,0) = 1. We apply it to the canonical a_2_fold.
a2_bcs_canon = a2_fold + delta_a2_pw  # (local) = a2_fold + delta
a4_bcs_canon = a4_fold + delta_a4_pw  # (local) = a4_fold + delta
f_spec_bcs = (a2_bcs_canon / a0_fold)**2  # (local) BCS-corrected
f_conv_bcs = f_KK * f_spec_bcs  # (local)

# A_s(fiber) from W1-F
A_s_fiber = 6.221  # (local) from S76 W1-F spectral perturbation theory

A_s_bare = A_s_fiber * f_conv_bare  # (local)
A_s_bcs = A_s_fiber * f_conv_bcs  # (local)

delta_As_rel = (A_s_bcs - A_s_bare) / A_s_bare  # (local)
delta_As_rel_from_a2 = 2.0 * frac_a2_canon  # (local) linearized: 2*delta(a_2)/a_2

# Gap in OOM
gap_bare_OOM = np.log10(A_s_bare / A_s_CMB)  # (local)
gap_bcs_OOM = np.log10(A_s_bcs / A_s_CMB)  # (local)

print(f"\n  f_KK = (M_KK/M_Pl)^4 = {f_KK:.6e}")
print(f"  a_2(bare) = {a2_fold:.4f} (canonical)")
print(f"  a_2(BCS)  = {a2_bcs_canon:.4f} (= a2_fold + delta_a2)")
print(f"  a_4(bare) = {a4_fold:.4f} (canonical)")
print(f"  a_4(BCS)  = {a4_bcs_canon:.4f}")
print(f"  f_spec(bare) = (a_2/a_0)^2 = {f_spec_bare:.6e}")
print(f"  f_spec(BCS)  = (a_2^BCS/a_0)^2 = {f_spec_bcs:.6e}")
print(f"\n  f_conv(bare) = {f_conv_bare:.6e}")
print(f"  f_conv(BCS)  = {f_conv_bcs:.6e}")
print(f"\n  A_s(fiber)  = {A_s_fiber:.3f}")
print(f"  A_s(bare)   = {A_s_bare:.4e}")
print(f"  A_s(BCS)    = {A_s_bcs:.4e}")
print(f"  A_s(Planck) = {A_s_CMB:.2e}")
print(f"\n  delta(A_s)/A_s = {delta_As_rel:.6e} ({delta_As_rel*100:.6f}%)")
print(f"  Linearized:     2 * delta(a_2)/a_2 = {delta_As_rel_from_a2:.6e}")
print(f"\n  Gap (bare):  log10(A_s/A_s_CMB) = {gap_bare_OOM:.4f} OOM")
print(f"  Gap (BCS):   log10(A_s/A_s_CMB) = {gap_bcs_OOM:.4f} OOM")
print(f"  Gap change:  {gap_bcs_OOM - gap_bare_OOM:.6f} OOM")

# --- CC via R_protected ---
print("\n  === Cosmological Constant impact ===")
R1_bare = a0_fold * a4_fold / a2_fold**2  # (local) = R_protected_fold
R1_bcs = a0_fold * a4_bcs_canon / a2_bcs_canon**2  # (local)
delta_R1_rel = (R1_bcs - R1_bare) / R1_bare  # (local)

print(f"  R_1(bare)  = a_0*a_4/a_2^2 = {R1_bare:.6f}")
print(f"  R_1(BCS)   = a_0*a_4^BCS/(a_2^BCS)^2 = {R1_bcs:.6f}")
print(f"  R_1(canon) = {R_protected_fold:.6f}")
print(f"  delta_R_1/R_1 = {delta_R1_rel:.6e} ({delta_R1_rel*100:.6f}%)")

# chi_2 from HP4: M_1/(N_modes * lam_max)
# chi_2 does NOT depend on a_2 directly -- it is a ratio of first spectral
# moments. But the CC prediction rho_HP4 = chi_2 * H_0^2 * M_Pl^2 does
# not involve a_2. So BCS dressing of a_2 does NOT affect chi_2 or rho_HP4.
# It DOES affect R_1 = a_0*a_4/a_2^2 (the L_max-protected ratio).
print(f"\n  chi_2 (HP4): does NOT depend on a_2 directly.")
print(f"    -> BCS dressing does NOT change the CC prediction via HP4 route.")
print(f"    -> But R_1 = a_0*a_4/a_2^2 IS affected (above).")

# =============================================================================
# STEP 4: CROSS-CHECKS
# =============================================================================
print("\n" + "-" * 78)
print("STEP 4: Cross-checks")
print("-" * 78)

# CHK1: Delta -> 0 limit
Delta_test = 1e-10  # (local) vanishing gap
delta_a2_zero = 0.0  # (local)
for eps in eps_modes:
    E_sq_test = eps**2 + Delta_test**2  # (local)
    delta_a2_zero += 2.0 * (1.0/E_sq_test - 1.0/eps**2)
chk1_pass = abs(delta_a2_zero) < 1e-15  # (local)
print(f"\n  CHK1 (Delta->0 limit): delta_a_2(Delta=1e-10) = {delta_a2_zero:.2e}")
print(f"    {'PASS' if chk1_pass else 'FAIL'}: {'vanishes' if chk1_pass else 'nonzero'}")

# CHK2: |delta_a_2/a_2| < 1
chk2_pass = abs(frac_a2) < 1.0  # (local)
print(f"\n  CHK2 (perturbative): |delta_a_2/a_2| = {abs(frac_a2):.6e}")
print(f"    {'PASS' if chk2_pass else 'FAIL'}: {'< 1 (perturbative)' if chk2_pass else '>= 1 (non-perturbative!)'}")

# CHK3: Sign (negative = BCS pushes eigenvalues apart)
chk3_pass = delta_a2_pw < 0  # (local)
print(f"\n  CHK3 (sign): delta_a_2 = {delta_a2_pw:.6e}")
print(f"    {'PASS' if chk3_pass else 'FAIL'}: {'negative (correct)' if chk3_pass else 'positive (wrong!)'}")

# CHK4: Analytic vs full spectrum consistency
analytic_vs_full = delta_a2_analytic / delta_a2_pw  # (local)
chk4_pass = abs(analytic_vs_full - 1.0) < 0.05  # (local) within 5%
print(f"\n  CHK4 (analytic vs full): ratio = {analytic_vs_full:.6f}")
print(f"    delta_a2(analytic) = {delta_a2_analytic:.6f}")
print(f"    delta_a2(full)     = {delta_a2_pw:.6f}")
print(f"    {'PASS' if chk4_pass else 'FAIL'}: {'agree within 5%' if chk4_pass else 'disagree > 5%'}")
if not chk4_pass:
    print(f"    NOTE: Discrepancy likely from using mean energies in analytic vs exact eigenvalues.")

# CHK5: Consistency with S72v2 delta_a2 (if available)
print(f"\n  CHK5 (S72v2 consistency):")
try:
    d_s72 = np.load('s72_bcs_dressed_sa_v2.npz', allow_pickle=True)
    a2_bare_s72 = float(d_s72.get('a2_bare_fold', 0))
    a2_bcs_s72 = float(d_s72.get('a2_BCS_selective_fold', 0))
    if a2_bare_s72 > 0 and a2_bcs_s72 > 0:
        delta_a2_s72 = a2_bcs_s72 - a2_bare_s72  # (local)
        frac_s72 = delta_a2_s72 / a2_bare_s72  # (local)
        print(f"    S72v2: delta_a2/a2 = {frac_s72:.6e}")
        print(f"    This:  delta_a2/a2 = {frac_a2:.6e}")
        s72_ratio = frac_a2 / frac_s72 if abs(frac_s72) > 1e-20 else float('inf')  # (local)
        chk5_pass = abs(s72_ratio - 1.0) < 0.1  # (local)
        print(f"    Ratio: {s72_ratio:.4f}")
        print(f"    {'PASS' if chk5_pass else 'INFO'}: {'consistent' if chk5_pass else 'differs (check S72 methodology)'}")
    else:
        print(f"    Keys not found in S72v2 data. SKIP.")
except Exception as e:
    print(f"    Could not load S72v2 data: {e}. SKIP.")

# CHK6: Delta scan -- verify monotonic dependence
print(f"\n  CHK6 (Delta scan -- monotonicity):")
Delta_scan = np.linspace(0, 1.0, 21)  # (local)
frac_a2_scan = np.zeros_like(Delta_scan)  # (local)
for j, D in enumerate(Delta_scan):
    da2 = 0.0  # (local)
    for eps in eps_modes:
        E_sq_j = eps**2 + D**2  # (local)
        da2 += 2.0 * (1.0/E_sq_j - 1.0/eps**2)
    frac_a2_scan[j] = da2 / a2_fold
diffs = np.diff(frac_a2_scan)  # (local) should all be <= 0 (monotonically decreasing)
monotonic = np.all(diffs <= 0)  # (local)
print(f"    Delta range: [0, 1.0] M_KK, 21 points")
print(f"    frac_a2 range: [{frac_a2_scan.min():.6e}, {frac_a2_scan.max():.6e}]")
print(f"    Monotonically decreasing: {'PASS' if monotonic else 'FAIL'}")
print(f"    At Delta_BCS = {Delta:.4f}: frac = {frac_a2_scan[int(round(Delta/1.0*20))]:.6e}")

# =============================================================================
# STEP 5: GATE VERDICT
# =============================================================================
print("\n" + "-" * 78)
print("STEP 5: Gate verdict")
print("-" * 78)

# Gate: S76-B4-BCS-DRESS
#   PASS: A_s(BCS-corrected) in [1.8e-9, 2.4e-9]
#   FAIL: |delta_a_2/a_2| < 0.001 (BCS correction negligible)
#   INFO: correction has right sign but wrong magnitude
#
# Use canonical frac_a2_canon = delta_a2/a2_fold for the gate test.

gate_pass = 1.8e-9 <= A_s_bcs <= 2.4e-9  # (local)
gate_fail = abs(frac_a2_canon) < 0.001  # (local)
gate_info = not gate_pass and not gate_fail  # (local)

if gate_fail:
    verdict = "FAIL"
    explanation = f"|delta_a_2/a_2| = {abs(frac_a2_canon):.6e} < 0.001. BCS correction NEGLIGIBLE."
elif gate_pass:
    verdict = "PASS"
    explanation = f"A_s(BCS) = {A_s_bcs:.4e} in [1.8e-9, 2.4e-9]."
else:
    verdict = "INFO"
    # Determine if sign is right for closing A_s gap
    # Bare A_s = 1.585e-9 < Planck 2.1e-9, so we need A_s to INCREASE
    # delta_a_2 < 0 -> a_2 decreases -> (a_2/a_0)^2 decreases -> f_conv decreases -> A_s decreases
    # This is the WRONG sign for closing the gap.
    if delta_a2_pw < 0:
        explanation = (f"BCS correction has WRONG sign for closing A_s gap. "
                      f"delta_a_2 = {delta_a2_pw:.4f} < 0 -> A_s DECREASES "
                      f"(gap widens from {abs(gap_bare_OOM):.4f} to {abs(gap_bcs_OOM):.4f} OOM). "
                      f"|delta_a_2/a_2| = {abs(frac_a2_canon):.6e} (exceeds 0.001 threshold).")
    else:
        explanation = (f"BCS correction has RIGHT sign. "
                      f"A_s increases but not enough: {A_s_bcs:.4e} vs target [1.8e-9, 2.4e-9]. "
                      f"|delta_a_2/a_2| = {abs(frac_a2_canon):.6e}.")

print(f"\n  Gate S76-B4-BCS-DRESS: {verdict}")
print(f"  Threshold (PASS): A_s(BCS) in [1.8e-9, 2.4e-9]")
print(f"  Threshold (FAIL): |delta_a_2/a_2| < 0.001")
print(f"  Computed:  A_s(bare) = {A_s_bare:.4e}, A_s(BCS) = {A_s_bcs:.4e}")
print(f"  Computed:  |delta_a_2/a_2(canon)| = {abs(frac_a2_canon):.6e}")
print(f"  Verdict:   {explanation}")

# Cross-check summary
print(f"\n  Cross-check summary:")
chk_labels = ['CHK1 (Delta->0)', 'CHK2 (perturbative)', 'CHK3 (sign)',
              'CHK4 (analytic vs full)', 'CHK6 (monotonicity)']
chk_results = [chk1_pass, chk2_pass, chk3_pass, chk4_pass, monotonic]
for label, result in zip(chk_labels, chk_results):
    print(f"    {label}: {'PASS' if result else 'FAIL'}")

# =============================================================================
# STEP 6: PHYSICAL INTERPRETATION
# =============================================================================
print("\n" + "-" * 78)
print("STEP 6: Physical interpretation")
print("-" * 78)

needed_frac = 0.12 / (2 * np.log10(np.e))  # (local) fraction needed to close 0.12 OOM
print(f"""
  STRUCTURAL RESULT:

  The mode-selective BCS correction involves only 16 eigenvalues in the
  (0,0) singlet sector. The correction is:

    delta_a_2 / a_2(canon) = {frac_a2_canon:.6e} ({frac_a2_canon*100:.4f}%)

  This is {abs(frac_a2_canon)/0.001:.1f}x the FAIL threshold of 0.001, so it
  is NOT negligible by the gate criterion. But:

    1. SIGN IS WRONG: delta_a_2 < 0, so A_s DECREASES (gap WIDENS).
       The framework needs A_s to INCREASE to close the 0.12 OOM gap.

    2. MAGNITUDE IS INSUFFICIENT: To close 0.12 OOM by a_2 alone requires
       delta(a_2)/a_2 = {needed_frac:.4f} ({needed_frac*100:.2f}%).
       Actual: {abs(frac_a2_canon):.4e}, which is {abs(frac_a2_canon)/needed_frac:.4f}x
       of what is needed ({abs(frac_a2_canon)/needed_frac*100:.2f}% of required magnitude).

  CONCLUSION: BCS dressing of a_2 shifts A_s by {delta_As_rel*100:.4f}%
  in the WRONG direction (decreasing). f_conv is effectively BCS-immune
  for the purpose of closing the A_s gap.

  The 0.12 OOM residual (A_s_pred = 1.585e-9 vs Planck 2.1e-9) must come from:
    - A_s(fiber) correction (Bogoliubov squeezing enhancement)
    - Observational uncertainty (Planck A_s has ~2% error, ~0.009 OOM)
    - Or it is the final structural precision of the framework

  For CC: R_1 = a_0*a_4/a_2^2 shifts by delta_R1/R1 = {delta_R1_rel:.4e}.
  The HP4 route (chi_2 * H_0^2 * M_Pl^2) does not involve a_2 at all.
  BCS dressing does NOT affect the CC prediction.
""")

# =============================================================================
# STEP 7: SAVE DATA AND PLOT
# =============================================================================
print("\n" + "-" * 78)
print("STEP 7: Save data and generate plot")
print("-" * 78)

np.savez('s76_bcs_dressing_a2.npz',
         # Gate
         gate_id='S76-B4-BCS-DRESS',
         verdict=verdict,
         # Bare moments (canonical)
         a0_bare=a0_fold,
         a2_bare=a2_fold,
         a4_bare=a4_fold,
         # BCS-dressed moments (canonical + delta)
         a2_bcs_canon=a2_bcs_canon,
         a4_bcs_canon=a4_bcs_canon,
         # Corrections (absolute)
         delta_a2=delta_a2_pw,
         delta_a4=delta_a4_pw,
         # Fractional corrections (canonical denominator)
         frac_a2_canon=frac_a2_canon,
         frac_a4=frac_a4,
         # Full-spectrum PW moments (for verification)
         a0_bare_pw=a0_bare_pw,
         a2_bare_pw=a2_bare_pw,
         a4_bare_pw=a4_bare_pw,
         a2_bcs_pw=a2_bcs_pw,
         a4_bcs_pw=a4_bcs_pw,
         # (0,0) sector
         a2_00_bare=a2_00_bare,
         a2_00_bcs=a2_00_bcs,
         delta_a2_00=delta_a2_00,
         n_eigenvalues_total=n_eigenvalues_total,
         n_eigenvalues_weighted_pw=n_eigenvalues_weighted_pw,
         n_eigenvalues_weighted_sq=n_eigenvalues_weighted_sq,
         n_eigenvalues_00=n_eigenvalues_00,
         # Analytic estimate
         delta_a2_analytic=delta_a2_analytic,
         # A_s
         f_conv_bare=f_conv_bare,
         f_conv_bcs=f_conv_bcs,
         A_s_bare=A_s_bare,
         A_s_bcs=A_s_bcs,
         A_s_CMB=A_s_CMB,
         gap_OOM_bare=gap_bare_OOM,
         gap_OOM_bcs=gap_bcs_OOM,
         delta_As_rel=delta_As_rel,
         # R_1 (CC)
         R1_bare=R1_bare,
         R1_bcs=R1_bcs,
         delta_R1_rel=delta_R1_rel,
         # Delta scan
         Delta_scan=Delta_scan,
         frac_a2_scan=frac_a2_scan,
         # Cross-checks
         chk1_pass=chk1_pass,
         chk2_pass=chk2_pass,
         chk3_pass=chk3_pass,
         chk4_pass=chk4_pass,
         chk6_monotonic=monotonic,
         )

print("  Saved: s76_bcs_dressing_a2.npz")

# Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: Delta scan of delta_a_2/a_2
ax = axes[0]
ax.plot(Delta_scan, frac_a2_scan * 100, 'b-', linewidth=2)
ax.axvline(Delta, color='r', linestyle='--', linewidth=1.5,
           label=f'$\\Delta_{{BCS}} = {Delta:.4f}$')
ax.axhline(0, color='k', linestyle='-', linewidth=0.5)
ax.axhline(-0.1, color='gray', linestyle=':', linewidth=1,
           label='FAIL threshold (0.1%)')
ax.set_xlabel('$\\Delta$ (M$_{KK}$ units)', fontsize=12)
ax.set_ylabel('$\\delta a_2 / a_2$ (%)', fontsize=12)
ax.set_title('BCS Correction to $a_2$ vs Gap Magnitude', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Right panel: A_s comparison
ax = axes[1]
labels_bar = ['Planck 2018', 'A$_s$(bare)', 'A$_s$(BCS)']
values_bar = [A_s_CMB, A_s_bare, A_s_bcs]
colors_bar = ['green', 'blue', 'red']
bars = ax.bar(labels_bar, [v * 1e9 for v in values_bar], color=colors_bar, alpha=0.7)
ax.set_ylabel('A$_s$ ($\\times 10^{-9}$)', fontsize=12)
ax.set_title('Scalar Amplitude: BCS Dressing Effect', fontsize=13)
# Add value labels
for bar_item, val in zip(bars, values_bar):
    ax.text(bar_item.get_x() + bar_item.get_width()/2., bar_item.get_height() + 0.02,
            f'{val:.3e}', ha='center', va='bottom', fontsize=9)
ax.axhline(1.8, color='gray', linestyle=':', linewidth=1, label='PASS range')
ax.axhline(2.4, color='gray', linestyle=':', linewidth=1)
ax.fill_between([-0.5, 2.5], 1.8, 2.4, alpha=0.1, color='green')
ax.set_xlim(-0.5, 2.5)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('s76_bcs_dressing_a2.png', dpi=150, bbox_inches='tight')
print("  Saved: s76_bcs_dressing_a2.png")

print("\n" + "=" * 78)
print("COMPLETE: S76-B4-BCS-DRESS")
print(f"  Verdict: {verdict}")
print(f"  delta_a_2/a_2(canon) = {frac_a2_canon:.6e}")
print(f"  A_s(bare) = {A_s_bare:.4e}, A_s(BCS) = {A_s_bcs:.4e}")
print(f"  Gap: {gap_bare_OOM:.4f} OOM (bare) -> {gap_bcs_OOM:.4f} OOM (BCS)")
print("=" * 78)
