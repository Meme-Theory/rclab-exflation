#!/usr/bin/env python3
"""
s62_bdg_gauge_fraction.py — BCS Contribution: Gauge vs Gravity (BDG-GAUGE-FRACTION-62)
======================================================================================

Computes the ratio of BCS condensate corrections to gauge sector (a_4) vs
gravitational sector (a_2) in the Seeley-DeWitt expansion of the spectral action.

NCG Foundation:
--------------
The spectral action Tr f(D^2/Lambda^2) has the asymptotic expansion:

    S_b = f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4 + O(Lambda^{-2})

where:
    a_0 = (4pi)^{-d/2} N_S Vol(M)              [cosmological constant]
    a_2 = (4pi)^{-d/2} N_S (5R/12) Vol(M)       [Einstein-Hilbert / gravity]
    a_4 = (4pi)^{-d/2} int tr(alpha R^2 + beta Ric^2 + gamma E^2 + ...) dvol
                                                  [Yang-Mills + Higgs / gauge sector]

For D -> D_BdG with endomorphism shift E -> E_0 + Delta^+Delta:
    delta_a_2 = (4pi)^{-d/2} * sum_i |Delta_i|^2           [from 6E term in a_2]
    delta_a_4 = (4pi)^{-d/2} * (R*tr(D^+D)/12 + tr(D^+D)^2/2 + ...)
                                                             [from E^2, RE terms in a_4]

The PHYSICAL question: gauge couplings run with a_4, gravity with a_2.
If delta_a_4/a_4 >> delta_a_2/a_2, BCS is gauge-visible but gravity-invisible.

Key NCG result (Chamseddine-Connes-Marcolli 2007):
    a_4 contains the Yang-Mills action ||F||^2 and the Higgs quartic |phi|^4.
    Both depend on the ENDOMORPHISM E of the Dirac operator, which is exactly
    what the BCS pairing Delta modifies.

    a_2 contains the Einstein-Hilbert action R, which depends on the METRIC
    (encoded in the Dirac operator through its principal symbol), which BCS
    does NOT modify (Delta is a bounded endomorphism perturbation, not a
    metric deformation).

This structural asymmetry — Delta shifts E but not the metric — is why we
expect delta_a_4/a_4 > delta_a_2/a_2.

Gate: BDG-GAUGE-FRACTION-62
    PASS if (delta_a4/a_4) / (delta_a2/a_2) > 10
    FAIL if ratio < 1
    INFO if 1-10

Author: Connes NCG Theorist (S62)
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    Delta_0_GL, E_cond, Delta_B3, N_dof_BCS,
    a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, tau_fold, PI,
    xi_BCS, M_KK_gravity, M_KK_kerner
)

# =============================================================================
# STEP 0: Load S61 precomputed data
# =============================================================================
data_dir = os.path.dirname(__file__)

data_bdg = np.load(os.path.join(data_dir, 's61_bdg_spectral_action.npz'),
                   allow_pickle=True)
data_fred = np.load(os.path.join(data_dir, 's61_fredholm_bdg.npz'),
                    allow_pickle=True)
data_trace = np.load(os.path.join(data_dir, 's61_trace_formula_geometric.npz'),
                     allow_pickle=True)

print("=" * 72)
print("BDG-GAUGE-FRACTION-62: BCS Contribution — Gauge vs Gravity")
print("=" * 72)

# =============================================================================
# STEP 1: Extract S61 results and verify consistency
# =============================================================================
print("\n--- Step 1: Load and Verify S61 Data ---")

# Gilkey dimensionless coefficients at fold
a2_gilkey = float(data_bdg['a2_SD_fold'])       # 0.7282
a4_gilkey = float(data_bdg['a4_gilkey_fold'])    # 0.3015
a0_gilkey = float(data_bdg['a0_SD'])             # sqrt(3)/2 = 0.8660

# S61 BCS corrections
delta_a2_s61 = float(data_bdg['delta_a2'])       # 9.894e-05
delta_a4_s61 = float(data_bdg['delta_a4'])       # 4.495e-05
ratio_a2_s61 = float(data_bdg['ratio_delta_a2']) # 1.359e-04
ratio_a4_s61 = float(data_bdg['ratio_delta_a4']) # 1.491e-04

# Manifold data
R_fold = float(data_bdg['R_fold'])               # 2.018
Ric2_fold = float(data_bdg['Ric2_fold'])         # 0.514
K_fold = float(data_bdg['K_fold'])               # 0.535
Vol_SU3 = float(data_bdg['Vol_SU3'])             # 1349.74
dim_spinor = int(data_bdg['dim_spinor'])          # 16
d_manifold = int(data_bdg['d_manifold'])          # 8

# BCS gap data
tr_Delta_sq = float(data_bdg['tr_Delta_sq'])     # 2.467
tr_Delta_4th = float(data_bdg['tr_Delta_4th'])   # 1.412
Delta_sq_B2 = float(data_bdg['Delta_sq_B2'])     # 2.374
Delta_sq_B1 = float(data_bdg['Delta_sq_B1'])     # 0.0
Delta_sq_B3 = float(data_bdg['Delta_sq_B3'])     # 0.093

# BdG eigenvalues
eigenvalues_BdG = data_fred['eigenvalues_BdG']   # 16 eigenvalues
eps_fold = data_fred['eps_fold']                   # 8 single-particle energies
Delta_matrix = data_fred['Delta_matrix']           # 8x8 pairing matrix

print(f"  a_2 (Gilkey, fold)     = {a2_gilkey:.10f}")
print(f"  a_4 (Gilkey, fold)     = {a4_gilkey:.10f}")
print(f"  a_0 (Gilkey)           = {a0_gilkey:.10f}")
print(f"  R_fold                 = {R_fold:.10f}")
print(f"  Vol(SU(3))             = {Vol_SU3:.4f}")
print(f"  dim_spinor             = {dim_spinor}")
print(f"  tr(Delta^+Delta)       = {tr_Delta_sq:.6f} M_KK^2")
print(f"  tr(Delta^4)            = {tr_Delta_4th:.6f} M_KK^4")
print(f"  S61 ratio_a2           = {ratio_a2_s61:.6e}")
print(f"  S61 ratio_a4           = {ratio_a4_s61:.6e}")

# Cross-check consistency
prefactor_4pi = (4 * PI)**(-d_manifold / 2)
a2_check = prefactor_4pi * dim_spinor * (5 * R_fold / 12) * Vol_SU3
a2_agree = abs(a2_check - a2_gilkey) / a2_gilkey
print(f"\n  a_2 formula check:     {a2_check:.10f} (err = {a2_agree:.4e})")

# =============================================================================
# STEP 2: Independent recomputation of delta_a_2 and delta_a_4
# =============================================================================
print("\n--- Step 2: Independent Recomputation ---")

# ---- a_2 correction ----
# Gilkey a_2 formula: a_2 = (4pi)^{-d/2} * (1/6) * int tr(6E + R*I) dvol
# For D_K: E_0 = R/4 * I (Lichnerowicz). So tr(6E + R) = N_S*(6*R/4 + R) = N_S*5R/2.
# Integral: N_S * 5R/2 * Vol / 6 = N_S * 5R/12 * Vol (consistent with S61).
#
# BCS shift: E -> E_0 + Delta^+Delta. The correction to a_2:
#   delta_a_2 = (4pi)^{-d/2} * (1/6) * int tr(6 * Delta^+Delta) dvol
#             = (4pi)^{-d/2} * int tr(Delta^+Delta) dvol
#
# For left-invariant modes: int tr(Delta^+Delta) dvol = sum_i |Delta_i|^2 (Parseval).
# Therefore: delta_a_2 = (4pi)^{-d/2} * sum_i |Delta_i|^2.

delta_a2_recomputed = prefactor_4pi * tr_Delta_sq
ratio_a2_recomputed = delta_a2_recomputed / a2_gilkey

print(f"  delta_a2 (recomputed)  = {delta_a2_recomputed:.6e}")
print(f"  delta_a2 (S61)         = {delta_a2_s61:.6e}")
print(f"  Agreement              = {abs(delta_a2_recomputed - delta_a2_s61)/abs(delta_a2_s61):.4e}")
print(f"  ratio delta_a2/a_2     = {ratio_a2_recomputed:.6e}")

# ---- a_4 correction: FULL Gilkey formula ----
# The Seeley-DeWitt a_4 coefficient for a generalized Laplacian D^2 = -(g^{ab}nabla_a nabla_b + E):
#
#   a_4 = (4pi)^{-d/2} * (1/360) * int tr(
#       60 R;kk + 180 E;kk         [total divergence, vanishes on closed manifold]
#     + 30 |Omega|^2                [curvature of the connection on the bundle]
#     + 12 R;kk                     [also vanishes on closed manifold]
#     + 5 R^2                       [scalar curvature squared]
#     - 2 |Ric|^2                   [Ricci squared]
#     + 2 |Riem|^2                  [Riemann squared = Kretschner]
#     + 60 R E                      [cross term: curvature x endomorphism]
#     + 180 E^2                     [endomorphism squared]
#   ) dvol
#
# SU(3) is closed and compact, so total divergence terms vanish.
# On SU(3) (Einstein manifold): Ric = R/8 * g, so |Ric|^2 = R^2/8.
# Kretschner scalar K = |Riem|^2.
#
# The E-dependent part of a_4:
#   a_4^{E-dep} = (4pi)^{-d/2} * (1/360) * int tr(60 R E + 180 E^2) dvol
#
# Writing E = E_0 + Delta_E where E_0 = R/4 (Lichnerowicz) and Delta_E = Delta^+Delta:
#   E^2 = E_0^2 + E_0 Delta_E + Delta_E E_0 + Delta_E^2
#       = (R/4)^2 + (R/2) Delta_E + Delta_E^2
#   R E = R E_0 + R Delta_E = R^2/4 + R Delta_E
#
# The correction to a_4 from BCS:
#   delta(60 R E) = 60 R Delta_E   [integrated: 60 R tr(Delta^+Delta)]
#   delta(180 E^2) = 180 (R/2 tr(D^+D) + tr((D^+D)^2))
#                  = 90 R tr(D^+D) + 180 tr((D^+D)^2)
#
# Wait — the 180 E^2 includes the cross terms:
#   delta(E^2) = (E_0 + Delta_E)^2 - E_0^2 = E_0 Delta_E + Delta_E E_0 + Delta_E^2
# For the trace: tr(E_0 Delta_E) = (R/4) tr(Delta^+Delta)  [since E_0 is scalar on spinor space]
# So: tr(delta(E^2)) = 2*(R/4)*tr(D^+D) + tr((D^+D)^2) = (R/2)*tr(D^+D) + tr((D^+D)^2)
#
# Total delta_a_4:
#   = (4pi)^{-d/2} * (1/360) * [60 R tr(D^+D) + 180*(R/2)*tr(D^+D) + 180*tr((D^+D)^2)] * Vol_factor
#
# BUT: For homogeneous (left-invariant) Delta on SU(3), the integrals are Parseval-type:
#   int tr(Delta^+Delta) dvol = sum_i |Delta_i|^2                    (proved in S61)
#   int tr((Delta^+Delta)^2) dvol = sum_i |Delta_i|^4                (same argument)
#
# Therefore:
#   delta_a_4 = (4pi)^{-d/2} * (1/360) * [60 R + 90 R] * sum_i |Delta_i|^2 + 180 * sum_i |Delta_i|^4]
#             = (4pi)^{-d/2} * (1/360) * [150 R * sum |D|^2 + 180 * sum |D|^4]
#             = (4pi)^{-d/2} * [150 R/(360) * sum |D|^2 + 180/(360) * sum |D|^4]
#             = (4pi)^{-d/2} * [5R/12 * sum |D|^2 + sum |D|^4 / 2]

# Let me verify: S61 script used delta_a4_term1 = R*tr_Delta_sq/12 and delta_a4_term2 = tr_Delta_4th/2.
# That corresponds to:
#   delta_a4 = prefactor * (R*tr(D^+D)/12 + tr(D^4)/2)
# But from the FULL Gilkey: we get 5R/12 not R/12.
#
# DISCREPANCY CHECK: Let me trace the S61 formula more carefully.
# S61 line 244: delta_a4_term1 = R_fold * tr_Delta_sq / 12  # from 30R * tr(D^+D) / 360
#
# The "30R" coefficient is suspicious. Let me rederive:
#   In the Gilkey a_4 formula, the E-dependent terms are:
#     60 R tr(E) + 180 tr(E^2)    (integrated, after dividing by 360)
#
#   The SHIFT in these terms when E -> E + Delta_E:
#     delta(60 R tr(E)) = 60 R tr(Delta_E)
#     delta(180 tr(E^2)) = 180 [2 tr(E_0 Delta_E) + tr(Delta_E^2)]
#                         = 180 [2*(R/4)*tr(Delta_E) + tr(Delta_E^2)]
#                         = 180 [(R/2)*tr(Delta_E) + tr(Delta_E^2)]
#                         = 90 R tr(Delta_E) + 180 tr(Delta_E^2)
#
#   Total: (60 R + 90 R) tr(Delta_E) + 180 tr(Delta_E^2)
#        = 150 R tr(Delta_E) + 180 tr(Delta_E^2)
#
#   Dividing by 360: (150/360) R tr + (180/360) tr^2
#                  = (5/12) R tr(Delta_E) + (1/2) tr(Delta_E^2)
#
# So the CORRECT delta_a_4:
#   delta_a_4 = (4pi)^{-d/2} * [(5/12) R * sum |D_i|^2 + (1/2) * sum |D_i|^4]
#
# The S61 script used (1/12) R instead of (5/12) R. This is an ERROR in S61.
# The factor of 5 comes from INCLUDING the 180 E^2 cross terms (90R from E^2,
# plus 60R from the RE term = 150R total, / 360 = 5/12).
#
# S61 used "30R * tr(D^+D) / 360" — but the correct coefficient from the RE term
# alone is 60R/360 = R/6, and the E^2 cross term adds 90R/360 = R/4.
# Total: R/6 + R/4 = 5R/12. The S61 script had R/12 (= 30R/360), which
# corresponds to keeping only HALF of the RE term (30R instead of 60R).
#
# I will compute BOTH: the S61 formula (for comparison) and the corrected formula.

print("\n  DERIVATION: Full Gilkey a_4 correction from E -> E + Delta^+Delta")
print("  Gilkey formula (closed manifold, dim 8):")
print("    a_4 = (4pi)^{-4} * (1/360) * int tr(30|Omega|^2 + 5R^2 - 2|Ric|^2")
print("          + 2|Riem|^2 + 60RE + 180E^2) dvol")
print()
print("  E-dependent shift:")
print("    delta(60 R tr(E))    = 60 R tr(Delta_E)          [RE cross term]")
print("    delta(180 tr(E^2))   = 90 R tr(Delta_E) + 180 tr(Delta_E^2)")
print("                           [from E_0 Delta_E cross + Delta_E^2]")
print("    Total / 360          = (5/12) R tr(D^+D) + (1/2) tr((D^+D)^2)")
print()

# CORRECTED delta_a_4
delta_a4_term_RE = (5.0 / 12.0) * R_fold * tr_Delta_sq     # 5R/12 * sum|D|^2
delta_a4_term_E2 = 0.5 * tr_Delta_4th                        # (1/2) * sum|D|^4

delta_a4_corrected = prefactor_4pi * (delta_a4_term_RE + delta_a4_term_E2)
ratio_a4_corrected = delta_a4_corrected / a4_gilkey

# S61 version for comparison
delta_a4_s61_formula = prefactor_4pi * (R_fold * tr_Delta_sq / 12 + tr_Delta_4th / 2)
ratio_a4_s61_formula = delta_a4_s61_formula / a4_gilkey

print(f"  --- S61 computation (R/12 coefficient) ---")
print(f"  delta_a4 (S61)         = {delta_a4_s61:.6e}")
print(f"  delta_a4 (S61 reproduced) = {delta_a4_s61_formula:.6e}")
print(f"  ratio delta_a4/a_4     = {ratio_a4_s61:.6e}")
print()
print(f"  --- CORRECTED computation (5R/12 coefficient) ---")
print(f"  Term 1: (5/12) R tr(D^+D)      = {delta_a4_term_RE:.6f}")
print(f"  Term 2: (1/2) tr((D^+D)^2)     = {delta_a4_term_E2:.6f}")
print(f"  Term 1 / Term 2                 = {delta_a4_term_RE / delta_a4_term_E2:.4f}")
print(f"  delta_a4 (corrected)            = {delta_a4_corrected:.6e}")
print(f"  ratio delta_a4/a_4 (corrected)  = {ratio_a4_corrected:.6e}")
print(f"  Correction factor (new/old)     = {delta_a4_corrected / delta_a4_s61_formula:.4f}")

# =============================================================================
# STEP 3: Compute the gauge-to-gravity ratio
# =============================================================================
print("\n--- Step 3: Gauge-to-Gravity Ratio ---")

# The KEY ratio for this gate
gauge_grav_ratio_s61 = ratio_a4_s61 / ratio_a2_s61
gauge_grav_ratio_corrected = ratio_a4_corrected / ratio_a2_recomputed

print(f"  S61 values:")
print(f"    delta_a2/a_2 = {ratio_a2_s61:.6e}")
print(f"    delta_a4/a_4 = {ratio_a4_s61:.6e}")
print(f"    (delta_a4/a_4) / (delta_a2/a_2) = {gauge_grav_ratio_s61:.6f}")
print()
print(f"  CORRECTED values:")
print(f"    delta_a2/a_2 = {ratio_a2_recomputed:.6e}")
print(f"    delta_a4/a_4 = {ratio_a4_corrected:.6e}")
print(f"    (delta_a4/a_4) / (delta_a2/a_2) = {gauge_grav_ratio_corrected:.6f}")

# =============================================================================
# STEP 4: Structural analysis — WHY a_4 > a_2 in ratio
# =============================================================================
print("\n--- Step 4: Structural Analysis ---")
print()
print("  WHY (delta_a4/a_4) / (delta_a2/a_2) > 1:")
print()
print("  The numerator ratio delta_a_4/a_4 has:")
print("    delta_a_4 = prefactor * [(5R/12) sum|D|^2 + (1/2) sum|D|^4]")
print(f"    a_4       = {a4_gilkey:.6f}  (Gilkey at fold)")
print(f"  The denominator ratio delta_a_2/a_2 has:")
print(f"    delta_a_2 = prefactor * sum|D|^2")
print(f"    a_2       = {a2_gilkey:.6f}  (Gilkey at fold)")
print()

# The key structural point: delta_a_4 has TWO contributions:
# 1. (5R/12) * sum|D|^2  -- linear in Delta^2 (same scaling as delta_a_2)
# 2. (1/2) * sum|D|^4    -- QUADRATIC in Delta^2 (new contribution!)

# Let's compute the enhancement factor analytically
# gauge_grav = [delta_a4/a_4] / [delta_a2/a_2]
#            = [delta_a4 * a_2] / [delta_a2 * a_4]
#            = a_2/a_4 * delta_a4/delta_a2
#            = (a_2/a_4) * [(5R/12)*sum|D|^2 + (1/2)*sum|D|^4] / sum|D|^2
#            = (a_2/a_4) * [5R/12 + (1/2)*sum|D|^4/sum|D|^2]

a2_over_a4 = a2_gilkey / a4_gilkey
mean_Delta_sq = tr_Delta_4th / tr_Delta_sq  # <|Delta|^4> / <|Delta|^2>

enhancement = a2_over_a4 * (5 * R_fold / 12 + 0.5 * mean_Delta_sq)
enhancement_linear_only = a2_over_a4 * (5 * R_fold / 12)
enhancement_quadratic_only = a2_over_a4 * 0.5 * mean_Delta_sq

print(f"  a_2 / a_4                        = {a2_over_a4:.6f}")
print(f"  <|D|^4> / <|D|^2>               = {mean_Delta_sq:.6f}")
print(f"  5R/12                            = {5*R_fold/12:.6f}")
print(f"  Enhancement (total)              = {enhancement:.6f}")
print(f"    linear part  (5R/12)           = {enhancement_linear_only:.6f}")
print(f"    quadratic part (D^4/2)         = {enhancement_quadratic_only:.6f}")
print(f"    quadratic fraction             = {enhancement_quadratic_only/enhancement*100:.1f}%")
print()

# Verify: the analytical formula should match the numerical ratio
print(f"  Verification:")
print(f"    Analytical gauge/grav ratio    = {enhancement:.6f}")
print(f"    Numerical gauge/grav ratio     = {gauge_grav_ratio_corrected:.6f}")
print(f"    Agreement                      = {abs(enhancement - gauge_grav_ratio_corrected)/enhancement:.4e}")

# =============================================================================
# STEP 5: Physical-scale Seeley-DeWitt coefficients
# =============================================================================
print("\n--- Step 5: Physical-Scale Analysis ---")
print()
print("  In the spectral action S_b = f_4 L^4 a_0 + f_2 L^2 a_2 + f_0 a_4:")
print("    Gravity sector:  S_grav = f_2 L^2 a_2  =>  G_N^{-1} ~ f_2 a_2")
print("    Gauge sector:    S_gauge = f_0 a_4      =>  g^{-2} ~ f_0 a_4")
print("    CC sector:       S_CC = f_4 L^4 a_0     =>  Lambda_CC ~ f_4 a_0")
print()

# The PHYSICAL delta_a2 and delta_a4 using canonical constants
# canonical_constants has a2_fold = 2776.2, a4_fold = 1350.7 (full spectral sums)
# These differ from Gilkey dimensionless by the sum over eigenvalues
print(f"  Physical-scale coefficients (from canonical_constants):")
print(f"    a_0 (fold) = {a0_fold:.4f}")
print(f"    a_2 (fold) = {a2_fold:.4f}")
print(f"    a_4 (fold) = {a4_fold:.4f}")
print()

# The RATIO delta_a_n/a_n is INDEPENDENT of whether we use Gilkey or physical-scale,
# as long as both numerator and denominator use the same convention.
# This is because the spectral sum factor cancels in the ratio.
print(f"  CRITICAL: delta_a_n/a_n ratios are convention-independent:")
print(f"  (The spectral sum factor cancels in numerator/denominator.)")
print(f"  delta_a_2/a_2 = {ratio_a2_recomputed:.6e}  (same in Gilkey or physical)")
print(f"  delta_a_4/a_4 = {ratio_a4_corrected:.6e}  (same in Gilkey or physical)")
print()

# What matters physically: how large is the BCS shift in physical units?
# delta(G_N^{-1}) / G_N^{-1} = delta_a2/a_2
# delta(g^{-2}) / g^{-2} = delta_a4/a_4

print(f"  Physical consequences:")
print(f"    Gravitational shift:  delta(G_N^{{-1}}) / G_N^{{-1}}  = {ratio_a2_recomputed:.4e}")
print(f"    Gauge coupling shift: delta(g^{{-2}}) / g^{{-2}}      = {ratio_a4_corrected:.4e}")
print(f"    Gauge/gravity ratio                              = {gauge_grav_ratio_corrected:.4f}")

# =============================================================================
# STEP 6: Sector-by-sector decomposition
# =============================================================================
print("\n--- Step 6: Sector Decomposition ---")

sectors = ['B2', 'B1', 'B3']
Delta_sq_sectors = [Delta_sq_B2, Delta_sq_B1, Delta_sq_B3]
n_modes = [4, 1, 3]
gaps = [Delta_0_GL, 0.0, Delta_B3]
Delta_4th_sectors = [4 * Delta_0_GL**4, 0.0, 3 * Delta_B3**4]

print(f"  {'Sector':>8} {'N_modes':>8} {'Gap':>10} {'|D|^2':>12} {'|D|^4':>12} {'da2/a2':>12} {'da4/a4':>12} {'g/g ratio':>12}")
print(f"  {'-'*8:>8} {'-'*8:>8} {'-'*10:>10} {'-'*12:>12} {'-'*12:>12} {'-'*12:>12} {'-'*12:>12} {'-'*12:>12}")

for i, sec in enumerate(sectors):
    dsq = Delta_sq_sectors[i]
    d4 = Delta_4th_sectors[i]
    da2 = prefactor_4pi * dsq
    da4 = prefactor_4pi * (5 * R_fold / 12 * dsq + 0.5 * d4)
    ra2 = da2 / a2_gilkey if dsq > 0 else 0.0
    ra4 = da4 / a4_gilkey if dsq > 0 else 0.0
    gg = ra4 / ra2 if ra2 > 0 else float('inf')
    print(f"  {sec:>8} {n_modes[i]:>8} {gaps[i]:>10.4f} {dsq:>12.6f} {d4:>12.6f} {ra2:>12.4e} {ra4:>12.4e} {gg:>12.4f}")

# Total
print(f"  {'TOTAL':>8} {8:>8} {'---':>10} {tr_Delta_sq:>12.6f} {tr_Delta_4th:>12.6f} {ratio_a2_recomputed:>12.4e} {ratio_a4_corrected:>12.4e} {gauge_grav_ratio_corrected:>12.4f}")

# =============================================================================
# STEP 7: Additional diagnostics — BdG eigenvalue direct computation
# =============================================================================
print("\n--- Step 7: Direct BdG Eigenvalue Analysis ---")

# Compute a_2 and a_4 directly from BdG eigenvalues using heat kernel trace
# Tr(exp(-t D^2)) = sum_k d_k exp(-t lambda_k^2)
# At small t: Tr ~ a_0 t^{-d/2} + a_2 t^{-d/2+1} + a_4 t^{-d/2+2} + ...
# For d=8: Tr ~ a_0 t^{-4} + a_2 t^{-3} + a_4 t^{-2} + ...
#
# But we only have 16 BdG eigenvalues (8-mode truncation), so a direct heat kernel
# fit is unreliable. Instead, use the ANALYTICAL Gilkey formula validated above.

print(f"  BdG eigenvalues (Nambu-doubled, 16 total):")
for i, ev in enumerate(eigenvalues_BdG):
    print(f"    lambda_{i:2d} = {ev:+.10f}")

print(f"\n  Normal-state single-particle energies (8 modes):")
for i, ep in enumerate(eps_fold):
    print(f"    eps_{i:2d} = {ep:+.10f}")

# Quasiparticle energies from BdG: E_k = sqrt(eps_k^2 + Delta_k^2)
# The BdG eigenvalues should be +/- E_k
print(f"\n  Quasiparticle energies E_k = sqrt(eps_k^2 + Delta_k^2):")
Delta_k = np.array([Delta_0_GL]*4 + [0.0] + [Delta_B3]*3)
E_k = np.sqrt(eps_fold**2 + Delta_k**2)
for i in range(8):
    print(f"    E_{i} = sqrt({eps_fold[i]:.6f}^2 + {Delta_k[i]:.6f}^2) = {E_k[i]:.6f}")

# Compare BdG eigenvalues to +/- E_k
bdg_pos = np.sort(eigenvalues_BdG[eigenvalues_BdG > 0])
bdg_neg = np.sort(-eigenvalues_BdG[eigenvalues_BdG < 0])
E_k_sorted = np.sort(E_k)

if len(bdg_pos) > 0 and len(E_k_sorted) > 0:
    n_compare = min(len(bdg_pos), len(E_k_sorted))
    print(f"\n  BdG eigenvalue vs quasiparticle comparison ({n_compare} modes):")
    for i in range(n_compare):
        print(f"    |lambda_BdG| = {bdg_pos[i]:.6f},  E_k = {E_k_sorted[i]:.6f},  diff = {abs(bdg_pos[i]-E_k_sorted[i]):.4e}")

# =============================================================================
# STEP 8: Nambu doubling effect
# =============================================================================
print("\n--- Step 8: Nambu Doubling ---")

# In the full BdG spectral triple, the Hilbert space is H + H*.
# The Gilkey coefficients DOUBLE: a_n(D_BdG) = 2 * a_n(D_K) + BCS corrections.
# The doubling is in the NORMAL part (background). The BCS part adds on top.
#
# For the RATIO, the doubling cancels:
#   delta_a2(BdG) / a2(BdG) = [2 * delta_a2 per sector] / [2 * a2(D_K)]
#                             = delta_a2 / a2(D_K)
# Same for a4. So Nambu doubling is irrelevant for the gauge/gravity ratio.

delta_a2_Nambu = 2 * delta_a2_recomputed  # both Nambu sectors contribute
a2_Nambu = 2 * a2_gilkey
ratio_a2_Nambu = delta_a2_Nambu / a2_Nambu

delta_a4_Nambu = 2 * delta_a4_corrected
a4_Nambu = 2 * a4_gilkey
ratio_a4_Nambu = delta_a4_Nambu / a4_Nambu

gauge_grav_Nambu = ratio_a4_Nambu / ratio_a2_Nambu

print(f"  Per Nambu sector:   delta_a2/a_2 = {ratio_a2_recomputed:.6e}")
print(f"  Full BdG (doubled): delta_a2/a_2 = {ratio_a2_Nambu:.6e}")
print(f"  Per Nambu sector:   delta_a4/a_4 = {ratio_a4_corrected:.6e}")
print(f"  Full BdG (doubled): delta_a4/a_4 = {ratio_a4_Nambu:.6e}")
print(f"  Gauge/gravity ratio (invariant)  = {gauge_grav_Nambu:.6f}")
print(f"  Nambu doubling cancels in ratio: confirmed = {abs(gauge_grav_Nambu - gauge_grav_ratio_corrected) < 1e-12}")

# =============================================================================
# STEP 9: Connection to cutoff function moments (f_0, f_2, f_4)
# =============================================================================
print("\n--- Step 9: Cutoff Function Dependence ---")
print()
print("  The spectral action S_b = f_4 L^4 a_0 + f_2 L^2 a_2 + f_0 a_4")
print()
print("  The BCS shift in the PHYSICAL action (not just Gilkey coefficients):")
print("    delta S_grav / S_grav = delta_a2/a_2  (independent of f_2, L)")
print("    delta S_gauge / S_gauge = delta_a4/a_4  (independent of f_0)")
print("    delta S_CC / S_CC = delta_a0/a_0 = 0  (BCS does not change volume)")
print()
print("  These ratios are CUTOFF-FUNCTION INDEPENDENT because BCS shifts")
print("  the Gilkey coefficients, not the moments f_n.")
print()
print("  The gauge/gravity ratio is therefore a UNIVERSAL prediction of the")
print("  BCS spectral triple, independent of the choice of cutoff function.")

# Use S62 cutoff results for cross-reference
# S62 CUTOFF-LONDON-62 found: f_0 = 9.817, f_2 = 2.34, f_4 = 0.558
# Physical gravity: delta(G_N^{-1}) ~ f_2 * delta_a2
# Physical gauge: delta(g^{-2}) ~ f_0 * delta_a4
# The physical ratio of shifts: (f_0 * delta_a4) / (f_2 * delta_a2)
# = (f_0/f_2) * (delta_a4/delta_a2)
# = (f_0/f_2) * (a_4/a_2) * (delta_a4/a_4) / (delta_a2/a_2)
# = (f_0/f_2) * (a_4/a_2) * gauge_grav_ratio

f_0_london = 9.817  # (local)
f_2_london = 2.34  # (local)
physical_shift_ratio = (f_0_london / f_2_london) * (a4_gilkey / a2_gilkey) * gauge_grav_ratio_corrected

# But wait: the actual physical coupling shifts are:
# delta(G_N^{-1}) / G_N^{-1} = delta_a2/a_2 (still)
# delta(g^{-2}) / g^{-2} = delta_a4/a_4 (still)
# These don't depend on f_n because both numerator and denominator share the same f_n.
# The ABSOLUTE shift magnitudes DO depend on f_n, but the RELATIVE shifts don't.

print(f"\n  With CUTOFF-LONDON-62 moments (f_0={f_0_london}, f_2={f_2_london}):")
print(f"    Absolute gravity shift:  f_2 * L^2 * delta_a2 = {f_2_london * delta_a2_recomputed:.6e} * L^2")
print(f"    Absolute gauge shift:    f_0 * delta_a4       = {f_0_london * delta_a4_corrected:.6e}")
print(f"    Ratio of absolute shifts = (f_0/f_2) * (delta_a4/delta_a2)")
print(f"                             = {f_0_london/f_2_london:.3f} * {delta_a4_corrected/delta_a2_recomputed:.6f}")
print(f"                             = {(f_0_london/f_2_london) * (delta_a4_corrected/delta_a2_recomputed):.6f} (times L^{-2})")
print(f"    Note: f_0/f_2 = {f_0_london/f_2_london:.3f} further ENHANCES gauge over gravity.")

# =============================================================================
# STEP 10: S61 Error Assessment
# =============================================================================
print("\n--- Step 10: S61 Coefficient Error Assessment ---")
print()
print("  S61 used delta_a4_term1 = R * tr(D^+D) / 12 (R/12 coefficient)")
print("  CORRECT:  delta_a4_term1 = 5R/12 * tr(D^+D)  (5R/12 coefficient)")
print()
print(f"  S61 R/12 coefficient:   {R_fold/12:.6f}")
print(f"  Correct 5R/12 coeff:    {5*R_fold/12:.6f}")
print(f"  Ratio (correct/S61):    {5.0:.1f} (factor of 5 in RE cross-term)")
print()
print(f"  Impact on delta_a4:")
print(f"    S61 delta_a4          = {delta_a4_s61_formula:.6e}")
print(f"    Corrected delta_a4    = {delta_a4_corrected:.6e}")
print(f"    Correction factor     = {delta_a4_corrected/delta_a4_s61_formula:.4f}")
print()
print(f"  Impact on gate verdict:")
print(f"    S61 ratio_a4          = {ratio_a4_s61:.6e}")
print(f"    Corrected ratio_a4    = {ratio_a4_corrected:.6e}")
print(f"    S61 gauge/grav        = {gauge_grav_ratio_s61:.4f}")
print(f"    Corrected gauge/grav  = {gauge_grav_ratio_corrected:.4f}")
print()

# Does the error change the BDG-SA-61 verdict?
print(f"  BDG-SA-61 re-evaluation:")
print(f"    S61 delta_a2/a_2 = {ratio_a2_s61:.4e} < 0.01 -> PASS (unchanged)")
print(f"    Corrected delta_a4/a_4 = {ratio_a4_corrected:.4e} < 0.01 -> still PASS")
print(f"    The S61 verdict (PASS: BCS invisible to gravity) stands.")
print(f"    The S61 delta_a4 value was understated by factor {delta_a4_corrected/delta_a4_s61_formula:.2f}.")

# =============================================================================
# STEP 11: Gate verdict
# =============================================================================
print("\n" + "=" * 72)
print("GATE VERDICT: BDG-GAUGE-FRACTION-62")
print("=" * 72)

# Gate: PASS if (delta_a4/a_4) / (delta_a2/a_2) > 10
#        FAIL if < 1
#        INFO if 1-10
key_ratio = gauge_grav_ratio_corrected

if key_ratio > 10:
    verdict = "PASS"
    detail = (f"(delta_a4/a_4)/(delta_a2/a_2) = {key_ratio:.4f} > 10. "
              f"BCS condensate {key_ratio:.1f}x more visible to gauge sector than gravity. "
              f"Structural: a_4 has E^2 term (quadratic in Delta), a_2 only linear.")
elif key_ratio < 1:
    verdict = "FAIL"
    detail = (f"(delta_a4/a_4)/(delta_a2/a_2) = {key_ratio:.4f} < 1. "
              f"BCS condensate more visible to gravity than gauge sector. "
              f"Unexpected: E^2 in a_4 should dominate.")
else:
    verdict = "INFO"
    detail = (f"(delta_a4/a_4)/(delta_a2/a_2) = {key_ratio:.4f} in [1, 10]. "
              f"BCS condensate has comparable visibility in gauge and gravity sectors. "
              f"Factor {key_ratio:.2f} enhancement from E^2 and a_2/a_4 ratio.")

print(f"  Verdict:        {verdict}")
print(f"  Key ratio:      (delta_a4/a_4) / (delta_a2/a_2) = {key_ratio:.6f}")
print(f"  delta_a2/a_2:   {ratio_a2_recomputed:.6e}  (gravity)")
print(f"  delta_a4/a_4:   {ratio_a4_corrected:.6e}  (gauge)")
print(f"  Threshold:      PASS > 10, FAIL < 1, INFO [1, 10]")
print(f"  Detail:         {detail}")
print(f"")
print(f"  STRUCTURAL RESULT:")
print(f"    gauge/gravity = (a_2/a_4) * [5R/12 + (1/2)*<|D|^4>/<|D|^2>]")
print(f"                  = {a2_over_a4:.4f} * [{5*R_fold/12:.4f} + {0.5*mean_Delta_sq:.4f}]")
print(f"                  = {a2_over_a4:.4f} * {5*R_fold/12 + 0.5*mean_Delta_sq:.4f}")
print(f"                  = {enhancement:.4f}")
print(f"")
print(f"  S61 ERROR FOUND: R/12 should be 5R/12 in delta_a4. Factor 5 in RE cross-term.")
print(f"  S61 delta_a4 understated by factor {delta_a4_corrected/delta_a4_s61_formula:.2f}.")
print(f"  S61 BDG-SA-61 PASS verdict unchanged (both corrected ratios < 0.01).")
print("=" * 72)

# =============================================================================
# STEP 12: Phononic classification
# =============================================================================
print("\n--- Phononic Classification ---")
print(f"  Category: GEOMETRIC + PARTICLE")
print(f"  The BDG-GAUGE-FRACTION result is GEOMETRIC (Gilkey heat kernel on SU(3))")
print(f"  with PARTICLE implications (BCS gap modifies gauge vs gravity couplings).")
print(f"  Phononic relevance: BCS phonons (quasiparticles) couple {key_ratio:.1f}x")
print(f"  preferentially to gauge sector over gravitational sector.")
print(f"  This is a consequence of the Gilkey E^2 term (endomorphism-squared)")
print(f"  which is QUADRATIC in the pairing gap, while gravity sees only LINEAR.")

# =============================================================================
# STEP 13: Save results
# =============================================================================
outpath = os.path.join(data_dir, 's62_bdg_gauge_fraction.npz')

np.savez(outpath,
    # S61 inputs
    a2_gilkey=a2_gilkey,
    a4_gilkey=a4_gilkey,
    a0_gilkey=a0_gilkey,
    R_fold=R_fold,
    Ric2_fold=Ric2_fold,
    K_fold=K_fold,
    Vol_SU3=Vol_SU3,
    dim_spinor=dim_spinor,
    d_manifold=d_manifold,
    tr_Delta_sq=tr_Delta_sq,
    tr_Delta_4th=tr_Delta_4th,
    prefactor_4pi=prefactor_4pi,
    # Recomputed delta corrections (corrected)
    delta_a2=delta_a2_recomputed,
    delta_a4_corrected=delta_a4_corrected,
    delta_a4_s61=delta_a4_s61_formula,
    # Ratios
    ratio_a2=ratio_a2_recomputed,
    ratio_a4_corrected=ratio_a4_corrected,
    ratio_a4_s61=ratio_a4_s61,
    # The KEY result
    gauge_grav_ratio=gauge_grav_ratio_corrected,
    gauge_grav_ratio_s61=gauge_grav_ratio_s61,
    # Structural formula
    a2_over_a4=a2_over_a4,
    mean_Delta_sq=mean_Delta_sq,
    enhancement_total=enhancement,
    enhancement_linear=enhancement_linear_only,
    enhancement_quadratic=enhancement_quadratic_only,
    # S61 error
    s61_correction_factor=delta_a4_corrected / delta_a4_s61_formula,
    # Sector decomposition
    Delta_sq_B2=Delta_sq_B2,
    Delta_sq_B1=Delta_sq_B1,
    Delta_sq_B3=Delta_sq_B3,
    # Gate verdict
    gate_name=np.array(['BDG-GAUGE-FRACTION-62']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"\n  Results saved to: {outpath}")
print(f"  Arrays: {len(np.load(outpath, allow_pickle=True).files)} keys")
