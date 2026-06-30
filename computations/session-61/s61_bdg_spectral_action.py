#!/usr/bin/env python3
"""
s61_bdg_spectral_action.py — BdG Spectral Action (BDG-SA-61)
=============================================================

FIRST NCG spectral action computation on a BCS system.

Computes Seeley-DeWitt coefficients a_n(D_K^{BdG}) for the Bogoliubov-de Gennes
Dirac operator and compares to a_n(D_K).

Physics:
--------
The BdG Dirac operator acts on the Nambu-doubled Hilbert space H + H*:

    D_K^{BdG} = ( D_K      Delta  )
                ( Delta^+  -C D_K C^{-1} )

For (D_K^{BdG})^2, the diagonal blocks:
    D_K^2 + Delta Delta^+  (particle sector)
    C D_K^2 C^{-1} + Delta^+ Delta  (hole sector)

The endomorphism E -> E_0 + Delta^+ Delta in each Nambu sector.

NORMALIZATION KEY POINT:
  The Gilkey a_2 formula is:
    a_2 = (4pi)^{-d/2} * (1/6) * integral tr(6E + R) dvol

  where the integral and trace are over the manifold and the vector bundle
  (spinor bundle of rank N_S = 16 at each point).

  For the Dirac operator D_K, E_0 = R/4 (Lichnerowicz), giving:
    a_2(D_K) = (4pi)^{-d/2} * N_S * (5R/12) * Vol(SU(3))

  The BCS pairing Delta(x) is a section of End(S). For a HOMOGENEOUS
  (left-invariant) condensate on SU(3), Delta is constant as an endomorphism.

  SUBTLETY: In the spectral (eigenvalue) basis:
    Delta = sum_i Delta_i |psi_i><psi_i| (diagonal in the BCS eigenmode basis)
  But eigenspinors psi_i are L^2-normalized:
    <psi_i|psi_i> = integral |psi_i(x)|^2 dvol = 1
  The POINTWISE value of |psi_i(x)|^2 varies, but for left-invariant modes
  on SU(3), |psi_i(x)|^2 = 1/Vol(SU(3)) (constant on the group).

  Therefore the POINTWISE endomorphism trace:
    tr_x(Delta^+ Delta) = sum_i |Delta_i|^2 * |psi_i(x)|^2
                         = sum_i |Delta_i|^2 / Vol(SU(3))

  And the Gilkey integral:
    integral tr(Delta^+ Delta) dvol = Vol * sum_i |Delta_i|^2 / Vol
                                     = sum_i |Delta_i|^2
    i.e., just the mode sum (no extra Vol factor).

  The correction to a_2 (per Nambu sector):
    delta_a_2 = (4pi)^{-d/2} * sum_i |Delta_i|^2

  This must be compared to:
    a_2(D_K) = (4pi)^{-d/2} * N_S * (5R/12) * Vol(SU(3))

  So the ratio:
    delta_a_2 / a_2 = sum_i |Delta_i|^2 / (N_S * 5R/12 * Vol(SU(3)))

  Since Vol(SU(3)) = 1349.74 and N_S = 16, 5R/12 = 0.841, the denominator
  is ~ 18156, making the ratio very small (~ 10^{-4}).

Gate: BDG-SA-61
  PASS if delta_a_2/a_2 < 0.01
  FAIL if delta_a_2/a_2 > 1
  INFO if 0.01 <= delta_a_2/a_2 <= 1

Author: Van den Dungen Bridge Theorist (S61)
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    Delta_0_GL, E_cond, Delta_B3, N_dof_BCS,
    a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, tau_fold, PI, g0_diag,
    xi_BCS, M_KK_gravity, M_KK_kerner
)

# =============================================================================
# STEP 0: Load precomputed heat kernel data
# =============================================================================
data_a2 = np.load(os.path.join(os.path.dirname(__file__), 's61_heat_kernel_a2.npz'),
                   allow_pickle=True)
data_a4 = np.load(os.path.join(os.path.dirname(__file__), 's61_heat_kernel_a4.npz'),
                   allow_pickle=True)
data_rg = np.load(os.path.join(os.path.dirname(__file__), 's60_rg_integrals.npz'),
                   allow_pickle=True)

# Gilkey a_2 and a_4 at the fold
a2_SD_fold = float(data_a2['a2_SD_fold'])        # = 0.7282 (dimensionless Gilkey)
a4_gilkey_fold = float(data_a4['a4_gilkey_fold']) # = 0.3015
a0_SD = float(data_a2['a0_SD'])                   # = sqrt(3)/2

# Manifold data
dim_spinor = 16  # rank of spinor bundle on SU(3) (2^{8/2} = 16)
d_manifold = 8  # dim(SU(3)) = 8 (local)

# Curvature invariants at fold
R_fold = float(data_a2['R_fold'])          # = 2.018
Ric2_fold = float(data_a4['Ric2_fold'])    # = 0.514
K_fold = float(data_a4['K_fold'])          # = 0.535
Vol_SU3 = float(data_a2['Vol_SU3_Haar'])   # = 1349.74

# BCS data
eps_fold = data_rg['eps_fold']  # 8 single-particle energies
V_fold = data_rg['V_fold']     # 8x8 pairing matrix

print("=" * 72)
print("BDG-SA-61: BdG Spectral Action on BCS System")
print("=" * 72)

# =============================================================================
# STEP 1: BCS pairing potential sector-by-sector
# =============================================================================
# 8-mode model: B2 (4 modes, gap Delta_0), B1 (1 Goldstone, gap 0), B3 (3 modes, gap Delta_B3)

print("\n--- Step 1: BCS Pairing Potential ---")
print(f"  Delta_0 (GL)       = {Delta_0_GL:.6f} M_KK")
print(f"  Delta_B3           = {Delta_B3:.6f} M_KK")
print(f"  E_cond             = {E_cond:.6f} M_KK")
print(f"  N_dof_BCS          = {N_dof_BCS}")

Delta_sq_B2 = 4 * Delta_0_GL**2
Delta_sq_B1 = 0.0  # Goldstone mode  # (local)
Delta_sq_B3 = 3 * Delta_B3**2

# MODE SUM: sum_i |Delta_i|^2 over the 8 BCS modes
tr_Delta_sq = Delta_sq_B2 + Delta_sq_B1 + Delta_sq_B3
tr_Delta_sq_uniform = N_dof_BCS * Delta_0_GL**2  # upper bound

print(f"\n  Mode sum: sum_i |Delta_i|^2")
print(f"    B2 (4 modes):   4 x {Delta_0_GL**2:.6f} = {Delta_sq_B2:.6f}")
print(f"    B1 (1 mode):    1 x 0.000000           = {Delta_sq_B1:.6f}")
print(f"    B3 (3 modes):   3 x {Delta_B3**2:.6f} = {Delta_sq_B3:.6f}")
print(f"  sum_i |Delta_i|^2 = {tr_Delta_sq:.6f} M_KK^2")
print(f"  Upper bound        = {tr_Delta_sq_uniform:.6f} (all 8 modes at Delta_0)")

# =============================================================================
# STEP 2: Gilkey correction to a_2 — CORRECT NORMALIZATION
# =============================================================================
# See docstring for the full normalization argument.
#
# KEY: For left-invariant eigenspinors on SU(3), |psi_i(x)|^2 = 1/Vol(SU(3)).
# The Gilkey integral of the endomorphism correction:
#   integral tr(Delta^+ Delta) dvol = sum_i |Delta_i|^2
# (the Vol factor from integration CANCELS the 1/Vol from the eigenfunction
# normalization — this is just Parseval's theorem).
#
# Therefore:
#   delta_a_2 = (4pi)^{-d/2} * sum_i |Delta_i|^2
#   a_2(D_K) = (4pi)^{-d/2} * N_S * (5R/12) * Vol(SU(3))
#
#   delta_a_2 / a_2 = sum_i |Delta_i|^2 / (N_S * 5R/12 * Vol)

print("\n--- Step 2: Gilkey Correction to a_2 ---")

d = d_manifold  # = 8
prefactor_4pi = (4 * PI)**(-d / 2)

# Verify the a_2 formula
a2_check = prefactor_4pi * dim_spinor * (5 * R_fold / 12) * Vol_SU3
print(f"  (4pi)^{{-d/2}}          = {prefactor_4pi:.6e}")
print(f"  a_2 check (formula)    = {a2_check:.10f}")
print(f"  a_2 from data          = {a2_SD_fold:.10f}")
print(f"  Agreement              = {abs(a2_check - a2_SD_fold)/a2_SD_fold:.4e}")

# Pairing correction (per Nambu sector — using Parseval normalization)
delta_a2 = prefactor_4pi * tr_Delta_sq
# NOTE: NO Vol(SU(3)) factor! See docstring for the proof.

# The full a_2 (for comparison) DOES include Vol:
# a_2 = prefactor * N_S * 5R/12 * Vol = a2_SD_fold

# KEY RATIO
ratio_delta_a2 = delta_a2 / a2_SD_fold

# Equivalent form: direct mode-to-curvature comparison
denominator = dim_spinor * (5 * R_fold / 12) * Vol_SU3
ratio_check = tr_Delta_sq / denominator

print(f"\n  Mode sum sum_i |Delta_i|^2   = {tr_Delta_sq:.6f}")
print(f"  delta_a2 (one Nambu sector)  = {delta_a2:.6e}")
print(f"  a_2(D_K)                     = {a2_SD_fold:.6f}")
print(f"  N_S * (5R/12) * Vol          = {denominator:.4f}")
print(f"  delta_a2 / a_2               = {ratio_delta_a2:.6e}")
print(f"  Cross-check (direct ratio)   = {ratio_check:.6e}")
print(f"  Agreement                    = {abs(ratio_delta_a2 - ratio_check):.2e}")

# =============================================================================
# STEP 3: Energy scale analysis — WHY the ratio is tiny
# =============================================================================
print("\n--- Step 3: Energy Scale Analysis ---")

# The ratio breaks down as:
#   delta_a2/a_2 = [sum |Delta_i|^2] / [N_S * (5R/12) * Vol]
#
# Numerator: 8 BCS modes, sum |Delta_i|^2 ~ 2.467 M_KK^2
# Denominator: 16 spinor components * 0.841 curvature * 1349.74 volume = 18156
#
# The denominator is huge because it includes the ENTIRE spinor spectrum
# integrated over the FULL volume of SU(3). The 8 BCS modes are an infinitesimal
# fraction of the total spectral weight.

curvature_weight = 5 * R_fold / 12
total_curvature_spectral_weight = dim_spinor * curvature_weight * Vol_SU3

print(f"  Curvature weight per spinor (5R/12)          = {curvature_weight:.6f}")
print(f"  N_S                                          = {dim_spinor}")
print(f"  Vol(SU(3))                                   = {Vol_SU3:.4f}")
print(f"  Total curvature spectral weight              = {total_curvature_spectral_weight:.4f}")
print(f"  Mode sum |Delta|^2                           = {tr_Delta_sq:.6f}")
print(f"  Ratio (modes / total)                        = {tr_Delta_sq/total_curvature_spectral_weight:.6e}")
print(f"")
print(f"  Physical reason: 8 BCS modes carry gap energy ~ 2.47 M_KK^2,")
print(f"  but the FULL spinor bundle on SU(3) has curvature weight ~ 18156 M_KK^2.")
print(f"  The condensate is a {tr_Delta_sq/total_curvature_spectral_weight*100:.4f}% perturbation.")
print(f"")
print(f"  Individual scale comparisons:")
print(f"    Delta_0^2 / R_fold                         = {Delta_0_GL**2 / R_fold:.6f}")
print(f"    |E_cond| / R_fold                          = {abs(E_cond)/R_fold:.6f}")
print(f"    Delta_0 / M_KK                             = {Delta_0_GL:.6f}")
print(f"    8 modes / (N_S * Vol)                      = {8/(dim_spinor*Vol_SU3):.6e}")

# =============================================================================
# STEP 4: Corrections to a_0 and a_4
# =============================================================================
print("\n--- Step 4: Corrections to a_0 and a_4 ---")

# a_0: No change from pairing (depends only on rank * Vol)
delta_a0_over_a0 = 0.0  # (local)

# a_4: The Gilkey a_4 has E^2 and R*E terms.
# delta_a4 ~ (4pi)^{-d/2} * [R * sum|Delta_i|^2/12 + sum|Delta_i|^4/2]
# Again using Parseval normalization (no extra Vol factor on the mode sums).

tr_Delta_4th = 4 * Delta_0_GL**4 + 0.0 + 3 * Delta_B3**4

delta_a4_term1 = R_fold * tr_Delta_sq / 12  # from 30R * tr(D^+D) / 360
delta_a4_term2 = tr_Delta_4th / 2            # from 180 E^2 / 360

delta_a4 = prefactor_4pi * (delta_a4_term1 + delta_a4_term2)
ratio_delta_a4 = delta_a4 / a4_gilkey_fold

print(f"  sum_i |Delta_i|^4  = {tr_Delta_4th:.6f}")
print(f"  R * sum|D|^2 / 12 = {delta_a4_term1:.6f}")
print(f"  sum|D|^4 / 2      = {delta_a4_term2:.6f}")
print(f"  delta_a4           = {delta_a4:.6e}")
print(f"  a_4(D_K)           = {a4_gilkey_fold:.6f}")
print(f"  delta_a4 / a_4     = {ratio_delta_a4:.6e}")

# =============================================================================
# STEP 5: Summary
# =============================================================================
print("\n--- Step 5: Summary of All Corrections ---")
print(f"  delta_a0/a_0 = {delta_a0_over_a0:.6e}  (pairing does not change volume term)")
print(f"  delta_a2/a_2 = {ratio_delta_a2:.6e}  <-- KEY RATIO for gravity")
print(f"  delta_a4/a_4 = {ratio_delta_a4:.6e}")
print(f"")
print(f"  Physical interpretation:")
print(f"    a_2 gives Einstein-Hilbert (M_Pl^2 R). delta_a2/a_2 ~ {ratio_delta_a2:.2e}")
print(f"    means condensate shifts Planck mass by {abs(ratio_delta_a2)*100:.6f}%.")
if abs(ratio_delta_a2) < 0.01:
    print(f"    BCS condensate is INVISIBLE to gravity at spectral action level.")
elif abs(ratio_delta_a2) < 1:
    print(f"    BCS condensate is PERTURBATIVE but not invisible to gravity.")
else:
    print(f"    BCS condensate DOMINATES the spectral action.")
print(f"")
print(f"  NCG interpretation (van den Dungen Paper 01, Thm 3.7):")
print(f"    Delta is bounded (||Delta|| = {Delta_0_GL:.3f} M_KK).")
print(f"    K-homology class preserved (SPECTRAL-FLOW-61: sf=0, gap open).")
print(f"    Kasparov product [pi!] (x) [D_base] unchanged by bounded perturbation.")
print(f"    Spectral ACTION shifts by {abs(ratio_delta_a2)*100:.4f}%,")
print(f"    but TOPOLOGICAL content (index, spectral flow, K-theory class) exact.")

# =============================================================================
# STEP 6: Sensitivity analysis — what if ALL modes paired at max gap?
# =============================================================================
print("\n--- Step 6: Sensitivity / Upper Bound ---")

# Upper bound: all 8 modes at Delta_0 (ignoring B1 Goldstone, B3 suppression)
delta_a2_upper = prefactor_4pi * tr_Delta_sq_uniform
ratio_upper = delta_a2_upper / a2_SD_fold

# Even more extreme: all N_S = 16 spinor components at Delta_0
delta_a2_max = prefactor_4pi * dim_spinor * Delta_0_GL**2
ratio_max = delta_a2_max / a2_SD_fold

# What if delta acted on the full Hilbert space (all modes at all points)?
# Then integral tr(D^+D) dvol = dim_spinor * Delta_0^2 * Vol
delta_a2_fullspace = prefactor_4pi * dim_spinor * Delta_0_GL**2 * Vol_SU3
ratio_fullspace = delta_a2_fullspace / a2_SD_fold

print(f"  ACTUAL:    8 modes, sector gaps:    delta_a2/a_2 = {ratio_delta_a2:.6e}")
print(f"  UPPER:     8 modes, all at Delta_0: delta_a2/a_2 = {ratio_upper:.6e}")
print(f"  EXTREME:  16 spinors, no Vol:       delta_a2/a_2 = {ratio_max:.6e}")
print(f"  GLOBAL:   16 spinors x Vol:         delta_a2/a_2 = {ratio_fullspace:.6e}")
print(f"")
print(f"  The ACTUAL result is suppressed relative to GLOBAL by a factor of")
print(f"  {ratio_delta_a2/ratio_fullspace:.6e} = (sum_modes |D|^2) / (N_S * D_0^2 * Vol)")
print(f"  This suppression factor = {tr_Delta_sq / (dim_spinor * Delta_0_GL**2 * Vol_SU3):.6e}")

# =============================================================================
# STEP 7: Gate verdict
# =============================================================================
print("\n" + "=" * 72)
print("GATE VERDICT: BDG-SA-61")
print("=" * 72)

threshold_pass = 0.01
threshold_fail = 1.0
key_ratio = abs(ratio_delta_a2)

if key_ratio < threshold_pass:
    verdict = "PASS"
    detail = (f"delta_a2/a_2 = {ratio_delta_a2:.4e} < 0.01. "
              f"BCS condensate invisible to gravity. "
              f"8-mode sum |Delta|^2 = {tr_Delta_sq:.4f}, "
              f"curvature spectral weight = {total_curvature_spectral_weight:.1f}.")
elif key_ratio > threshold_fail:
    verdict = "FAIL"
    detail = (f"delta_a2/a_2 = {ratio_delta_a2:.4e} > 1. "
              f"BCS condensate DOMINATES spectral action.")
else:
    verdict = "INFO"
    detail = (f"delta_a2/a_2 = {ratio_delta_a2:.4e} in [0.01, 1]. "
              f"Condensate perturbative but visible.")

print(f"  Verdict:     {verdict}")
print(f"  delta_a2/a_2 = {ratio_delta_a2:.6e}")
print(f"  delta_a4/a_4 = {ratio_delta_a4:.6e}")
print(f"  Threshold:   PASS < {threshold_pass}, FAIL > {threshold_fail}")
print(f"  Detail:      {detail}")
print("=" * 72)

# =============================================================================
# STEP 8: Save results
# =============================================================================
outpath = os.path.join(os.path.dirname(__file__), 's61_bdg_spectral_action.npz')

np.savez(outpath,
    # BCS pairing data
    Delta_0_GL=Delta_0_GL,
    Delta_B3=Delta_B3,
    tr_Delta_sq=tr_Delta_sq,
    tr_Delta_sq_uniform=tr_Delta_sq_uniform,
    tr_Delta_4th=tr_Delta_4th,
    Delta_sq_B2=Delta_sq_B2,
    Delta_sq_B1=Delta_sq_B1,
    Delta_sq_B3=Delta_sq_B3,
    # Gilkey corrections
    prefactor_4pi=prefactor_4pi,
    delta_a2=delta_a2,
    delta_a2_Nambu=2*delta_a2,
    delta_a4=delta_a4,
    # Reference values
    a2_SD_fold=a2_SD_fold,
    a4_gilkey_fold=a4_gilkey_fold,
    a0_SD=a0_SD,
    R_fold=R_fold,
    Ric2_fold=Ric2_fold,
    K_fold=K_fold,
    Vol_SU3=Vol_SU3,
    dim_spinor=dim_spinor,
    d_manifold=d_manifold,
    # Key ratios
    ratio_delta_a2=ratio_delta_a2,
    ratio_delta_a4=ratio_delta_a4,
    delta_a0_over_a0=delta_a0_over_a0,
    # Energy scale comparisons
    E_cond_over_R=abs(E_cond)/R_fold,
    Delta0_sq_over_R=Delta_0_GL**2/R_fold,
    total_curvature_spectral_weight=total_curvature_spectral_weight,
    # Verification
    a2_check=a2_check,
    a2_formula_agreement=abs(a2_check - a2_SD_fold)/a2_SD_fold,
    # Sensitivity
    ratio_upper=ratio_upper,
    ratio_max=ratio_max,
    ratio_fullspace=ratio_fullspace,
    # Gate
    gate_name=np.array(['BDG-SA-61']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"\nSaved: {outpath}")
print("Done.")
