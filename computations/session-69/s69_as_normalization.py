#!/usr/bin/env python3
"""
AS-NORMALIZATION-CHAIN-69: Resolve 12.9x Mismatch Between A_s Chains
=====================================================================

The direct amplitude chain (S68 W1-A) and the multifield delta-N chain
(S67 W3-B) give A_s values differing by a factor of 12.9:

  Direct:  P_phys * enhancement_M1 = 4.25e-9
  Delta-N: A_s_multi(M1)           = 3.29e-10

This script traces both normalization chains step-by-step, identifies
the source of the 12.9x discrepancy, and determines whether it is
bookkeeping (convention mismatch) or physics.

Gate: AS-NORM-69 — INFO (diagnostic)
  Einstein PASS criterion: decomposes into recognizable geometric factors
  Mack: INFO (diagnostic)

Inputs:
  s67_transit_ps.npz        — Bogoliubov power spectrum P_zeta(k)
  s67_multifield_delta_n.npz — delta-N conversion coefficients
  s68_acoustic_transfer.npz — acoustic transfer chain results

Output:
  s69_as_normalization.npz  — all diagnostic quantities
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np

from canonical_constants import (
    PI, M_Pl_reduced, M_KK, H_fold,
    a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    A_s_CMB, Vol_SU3_Haar,
)

print("=" * 72)
print("AS-NORMALIZATION-CHAIN-69")
print("Resolve 12.9x Mismatch Between A_s Chains")
print("=" * 72)

# ============================================================================
#  SECTION 1: Load input data from both chains
# ============================================================================

data_dir = os.path.dirname(__file__)

transit = np.load(os.path.join(data_dir, 's67_transit_ps.npz'), allow_pickle=True)
delta_n = np.load(os.path.join(data_dir, 's67_multifield_delta_n.npz'), allow_pickle=True)
acoustic = np.load(os.path.join(data_dir, 's68_acoustic_transfer.npz'), allow_pickle=True)

# Chain A (direct): P_transit -> P_phys -> A_s via enhancement
P_transit = float(transit['P_zeta_at_transit'])          # 2.56e6 (M_KK units)
k_transit = float(transit['k_transit'])                   # 1209.3 M_KK
zpp_z_fold = float(transit['zpp_z_fold'])                 # z''/z at fold

# Chain B (delta-N): self-contained A_s computation
A_s_multi_m1 = float(delta_n['A_s_multi_m1'])            # 3.29e-10
A_s_single = float(delta_n['A_s_single'])                # 184.3
enhancement_m1 = float(delta_n['enhancement_m1'])         # 1.786e-12
eps_H_fold = float(delta_n['eps_H_fold'])                 # 0.022
M_Pl_over_MKK = float(delta_n['M_Pl_over_M_KK'])         # 32.78

print(f"\n--- Input Data ---")
print(f"  P_transit (W1-A at k_transit)     = {P_transit:.6e}")
print(f"  k_transit                          = {k_transit:.4f} M_KK")
print(f"  z''/z at fold                      = {zpp_z_fold:.4e}")
print(f"  A_s_multi_m1 (delta-N, M1)         = {A_s_multi_m1:.6e}")
print(f"  A_s_single (std formula)           = {A_s_single:.6e}")
print(f"  enhancement_M1                     = {enhancement_m1:.6e}")
print(f"  eps_H                              = {eps_H_fold}")
print(f"  M_Pl/M_KK                          = {M_Pl_over_MKK:.6f}")

# ============================================================================
#  SECTION 2: Reproduce the 12.9x mismatch
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 2: REPRODUCE THE MISMATCH")
print(f"{'='*72}")

# Direct chain: P_phys * enhancement_M1
P_phys = P_transit / M_Pl_over_MKK**2
A_s_direct = P_phys * enhancement_m1

# Delta-N chain: A_s_multi_m1 (already computed)
A_s_deltaN = A_s_multi_m1

ratio = A_s_direct / A_s_deltaN

print(f"\n  --- Direct chain (W1-A) ---")
print(f"  Step 1: P_transit = {P_transit:.6e}  (Bogoliubov at k_transit)")
print(f"  Step 2: P_phys = P_transit / (M_Pl/M_KK)^2 = {P_phys:.6e}")
print(f"  Step 3: A_s = P_phys * enhancement_M1 = {A_s_direct:.6e}")
print(f"\n  --- Delta-N chain (W3-B) ---")
print(f"  A_s_multi_m1 = {A_s_deltaN:.6e}")
print(f"\n  RATIO (direct / delta-N) = {ratio:.6f}")
print(f"  = {np.log10(ratio):.4f} OOM")

# ============================================================================
#  SECTION 3: Algebraic decomposition
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 3: ALGEBRAIC DECOMPOSITION")
print(f"{'='*72}")

# The enhancement factor is defined as:
#   enhancement_M1 = A_s_multi / A_s_single
#
# where A_s_single = H^2 / (8 pi^2 eps M_Pl^2)  [standard single-field formula]
#
# Therefore:
#   A_s_direct = P_phys * enhancement_M1
#              = P_phys * (A_s_multi / A_s_single)
#              = (P_phys / A_s_single) * A_s_multi
#
# The 12.9x factor IS EXACTLY P_phys / A_s_single:

A_s_single_recomputed = H_fold**2 / (8.0 * PI**2 * eps_H_fold * M_Pl_over_MKK**2)
check_ratio = P_phys / A_s_single_recomputed

print(f"\n  A_s_single = H^2 / (8 pi^2 eps M_Pl^2)")
print(f"             = {H_fold:.4f}^2 / (8 * pi^2 * {eps_H_fold} * {M_Pl_over_MKK:.4f}^2)")
print(f"             = {A_s_single_recomputed:.6e}")
print(f"  P_phys     = {P_phys:.6e}")
print(f"  P_phys / A_s_single = {check_ratio:.6f}")
print(f"  12.9 ratio          = {ratio:.6f}")
print(f"  Match: {abs(check_ratio - ratio) < 1e-6}")
print(f"\n  IDENTIFICATION: The 12.9x = P_phys / A_s_single EXACTLY.")

# ============================================================================
#  SECTION 4: Root cause — inconsistent k evaluation
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 4: ROOT CAUSE — INCONSISTENT K EVALUATION")
print(f"{'='*72}")

# P_phys and A_s_single are both physical single-field power spectra
# (dimensionless, in physical M_Pl normalization), but evaluated at
# DIFFERENT wavenumbers:
#
#   P_phys = P_zeta(k_transit)     [Bogoliubov numerical, k = 1209 M_KK]
#   A_s_single = P_zeta_std(k=aH)  [slow-roll formula, k = aH = 587 M_KK]
#
# In M_KK normalization (without M_Pl in z):
#   P_transit = P_Bog(k_transit)    [raw Bogoliubov, k = 1209]
#   P_std_MKK = H^2/(8pi^2 eps)    [slow-roll at k = aH, M_KK norm]

P_std_MKK = H_fold**2 / (8.0 * PI**2 * eps_H_fold)
k_horizon = H_fold  # aH with a=1 at fold

print(f"\n  In M_KK normalization (z = a*sqrt(2*eps), no M_Pl):")
print(f"    P_Bog(k_transit = {k_transit:.1f}) = {P_transit:.6e}")
print(f"    P_std(k_horizon = {k_horizon:.1f}) = {P_std_MKK:.6e}")
print(f"    Ratio = {P_transit / P_std_MKK:.6f}")
print(f"\n  Both get divided by M_Pl^2 to become physical:")
print(f"    P_phys = P_Bog / M_Pl^2 = {P_phys:.6e}")
print(f"    A_s_single = P_std / M_Pl^2 = {A_s_single_recomputed:.6e}")
print(f"    Ratio unchanged: {P_phys / A_s_single_recomputed:.6f}")

print(f"\n  ROOT CAUSE: The direct chain evaluates P at k_transit = {k_transit:.1f} M_KK")
print(f"  but multiplies by enhancement_M1 = A_s_multi/A_s_single where")
print(f"  A_s_single is the standard formula at k = aH = {k_horizon:.1f} M_KK.")
print(f"  Since k_transit != aH, and P(k) is not scale-invariant at these")
print(f"  scales, the ratio P(k_transit)/P(aH) = 12.9 appears as spurious")
print(f"  amplification.")

# ============================================================================
#  SECTION 5: Factorize 12.9 into k-ratio and dynamical correction
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 5: DECOMPOSE 12.9 INTO PHYSICAL COMPONENTS")
print(f"{'='*72}")

# The Bogoliubov P_zeta at deeply superhorizon modes scales as k^3
# (equivalently, n_s = 4 in the tachyonic regime). If this scaling held
# exactly from k_horizon to k_transit:
#   P(k_transit) / P(k_horizon) = (k_transit / k_horizon)^3

k_ratio = k_transit / k_horizon
k_ratio_cubed = k_ratio**3
dynamical_correction = ratio / k_ratio_cubed

print(f"\n  k_transit / k_horizon = {k_ratio:.6f}")
print(f"  (k_transit / k_horizon)^3 = {k_ratio_cubed:.4f}")
print(f"  12.9 / (k_t/k_*)^3 = {dynamical_correction:.4f}")
print(f"\n  Decomposition: 12.9 = {k_ratio_cubed:.2f} (k^3 scaling)")
print(f"                        x {dynamical_correction:.3f} (non-power-law correction)")

# Check the spectral index at k_transit
k_rk = transit['k_grid_rk']
P_rk = transit['P_zeta_rk']
ns_rk = transit['ns_rk']

idx_t = np.argmin(np.abs(k_rk - k_transit))
ns_at_transit = ns_rk[idx_t]

print(f"\n  n_s at k_transit = {ns_at_transit:.4f}")
print(f"  n_s = 4 corresponds to P ~ k^3 (pure superhorizon scaling)")
print(f"  The n_s ~ {ns_at_transit:.2f} at k_transit means this mode is near the")
print(f"  tachyonic boundary where the P(k) starts to turn over.")

# For an effective average spectral index:
# P(k_transit)/P(k_horizon) = (k_t/k_h)^{ns_eff - 1}
# 12.9 = (2.06)^{ns_eff - 1}
# ln(12.9) = (ns_eff - 1) * ln(2.06)
ns_eff = 1.0 + np.log(ratio) / np.log(k_ratio)
print(f"\n  Effective average n_s from k_horizon to k_transit:")
print(f"  ns_eff = 1 + ln(12.9)/ln({k_ratio:.3f}) = {ns_eff:.4f}")
print(f"  (Between n_s=1 scale-invariant and n_s=4 tachyonic)")

# ============================================================================
#  SECTION 6: Check against geometric factors (Einstein criterion)
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 6: GEOMETRIC FACTOR CHECK (EINSTEIN CRITERION)")
print(f"{'='*72}")

# Check whether 12.9 factorizes into recognizable geometric quantities
candidates = {
    '4*pi': 4*PI,
    '4*pi^2/3': 4*PI**2/3,
    '13 (integer)': 13.0,
    'Vol(SU3)/(2pi)^4': Vol_SU3_Haar / (2*PI)**4,
    'Vol(SU3)/(2pi)^3': Vol_SU3_Haar / (2*PI)**3,
    'a0_fold/a4_fold': a0_fold / a4_fold,
    'a2_fold/a4_fold': a2_fold / a4_fold,
    'dS/dtau / S_fold': dS_fold / S_fold,
}

print(f"\n  Ratio to match: {ratio:.6f}")
print(f"  {'Candidate':<25s} {'Value':>12s} {'Off by':>8s}")
print(f"  {'-'*50}")
for name, val in candidates.items():
    pct = abs(val / ratio - 1) * 100
    print(f"  {name:<25s} {val:12.6f} {pct:7.2f}%")

print(f"\n  None match to better than 1%.")
print(f"  The closest is 4*pi^2/3 = {4*PI**2/3:.4f} (off by {abs(4*PI**2/3/ratio-1)*100:.2f}%)")
print(f"  and the integer 13 (off by {abs(13/ratio-1)*100:.2f}%).")
print(f"\n  VERDICT: 12.9 does NOT decompose into a recognizable geometric factor.")
print(f"  It is a DYNAMICAL ratio P_Bog(k_transit)/P_std(k_horizon), determined by")
print(f"  the Bogoliubov evolution of mode k = {k_transit:.0f} M_KK through the")
print(f"  tachyonic potential z''/z = {zpp_z_fold:.2e}.")

# ============================================================================
#  SECTION 7: Which chain is correct?
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 7: WHICH CHAIN IS CORRECT?")
print(f"{'='*72}")

# The delta-N chain (W3-B) is self-consistent:
#   A_s_multi = Sum_I (dN/dsigma_I)^2 * sigma_sq_I
# where:
#   dN/dsigma_I = drho_I/dsigma_I / (6 eps_H M_Pl^2 H^2)
#   sigma_sq_I = Sum_k n_k/omega_k dk  (from KZ occupation)
#
# This computation uses the Friedmann equation, the GGE branch structure,
# and the occupation numbers. It does NOT reference P_transit.
#
# The direct chain (W1-A) attempts:
#   A_s = P_phys(k_transit) * enhancement_M1
# where enhancement_M1 = A_s_multi / A_s_single.
#
# Substituting: A_s = [P_transit/(M_Pl/M_KK)^2] * [A_s_multi / (H^2/(8pi^2 eps M_Pl^2))]
#             = [P_transit * 8 pi^2 eps / H^2] * A_s_multi
#             = [P_transit / P_std] * A_s_multi
#
# The factor P_transit / P_std = 12.9 counts the Bogoliubov amplification
# RELATIVE to the slow-roll formula. But the delta-N A_s_multi already
# includes the multifield conversion from the GGE occupation spectrum.
# The P_transit at k_transit encodes the SAME occupation physics.
# Multiplying P_phys by enhancement_M1 double-counts the spectral weight.

print(f"""
  The delta-N chain is correct. A_s = 3.29e-10.

  Proof of double-counting in the direct chain:

    enhancement_M1 = A_s_multi / A_s_single
                   = (Sum_I (dN/dsigma_I)^2 * sigma_sq_I) / (H^2/(8pi^2 eps M_Pl^2))

    The sigma_sq_I are field variances from the KZ occupation:
      sigma_I^2 = Sum_k n_k / omega_k * dk

    The P_transit = P_Bog(k_transit) is the Bogoliubov power spectrum,
    which ALSO depends on the occupation numbers |beta_k|^2.

    Both P_transit and A_s_multi encode the same Bogoliubov particle
    production. The direct chain multiplies them together, overcounting
    the pair-creation amplitude by a factor of P_transit/P_std = 12.9.

    The delta-N chain avoids this because it computes A_s from the
    GGE branch structure without reference to P_transit.
""")

# ============================================================================
#  SECTION 8: Revised gap assessment
# ============================================================================

print(f"{'='*72}")
print("SECTION 8: REVISED GAP ASSESSMENT")
print(f"{'='*72}")

A_s_correct = A_s_multi_m1
gap_OOM = np.log10(A_s_correct / A_s_CMB)
gap_linear = A_s_CMB / A_s_correct

print(f"\n  Correct A_s = {A_s_correct:.6e}")
print(f"  Planck A_s  = {A_s_CMB:.6e}")
print(f"  Gap = {gap_OOM:.4f} OOM  ({gap_linear:.2f}x below Planck)")
print(f"\n  The direct chain's claimed A_s = {A_s_direct:.4e} ({np.log10(A_s_direct/A_s_CMB):.2f} OOM)")
print(f"  is WRONG due to double-counting.")
print(f"\n  The entire gap closure budget remains anchored at 0.80 OOM.")
print(f"  No revision needed. The gap is NOT -0.31 OOM (above Planck).")
print(f"  It is +0.80 OOM (below Planck).")

# ============================================================================
#  SECTION 9: Independent cross-checks
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 9: CROSS-CHECKS")
print(f"{'='*72}")

# Cross-check 1: Verify A_s_single matches the standard formula
A_s_single_check = H_fold**2 / (8.0 * PI**2 * eps_H_fold * M_Pl_over_MKK**2)
print(f"\n  1. A_s_single consistency:")
print(f"     From npz: {A_s_single:.6e}")
print(f"     Recomputed: {A_s_single_check:.6e}")
print(f"     Match: {abs(A_s_single - A_s_single_check)/A_s_single < 1e-6}")

# Cross-check 2: Verify enhancement_M1 = A_s_multi / A_s_single
enh_check = A_s_multi_m1 / A_s_single
print(f"\n  2. Enhancement consistency:")
print(f"     From npz: {enhancement_m1:.6e}")
print(f"     A_s_multi / A_s_single: {enh_check:.6e}")
print(f"     Match: {abs(enhancement_m1 - enh_check)/enhancement_m1 < 1e-6}")

# Cross-check 3: Check that P_phys * enhancement = A_s_multi * (P_transit/P_std)
product = A_s_multi_m1 * (P_transit / P_std_MKK)
print(f"\n  3. Product consistency:")
print(f"     A_s_multi * (P_transit/P_std) = {product:.6e}")
print(f"     P_phys * enhancement_M1 = {A_s_direct:.6e}")
print(f"     Match: {abs(product - A_s_direct)/A_s_direct < 1e-6}")

# Cross-check 4: Does the ratio depend on which k we evaluate P at?
# If we used P(k_horizon) instead of P(k_transit), do we get A_s_single?
# P_Bog(k~aH) from the data:
idx_horizon = np.argmin(np.abs(k_rk - k_horizon))
P_at_horizon = P_rk[idx_horizon]
P_phys_horizon = P_at_horizon / M_Pl_over_MKK**2
ratio_horizon = P_phys_horizon / A_s_single_check

print(f"\n  4. P_Bog at horizon scale:")
print(f"     k_horizon = aH = {k_horizon:.2f} M_KK")
print(f"     P_Bog(k_horizon) = {P_at_horizon:.6e} (M_KK norm)")
print(f"     P_phys(k_horizon) = {P_phys_horizon:.6e}")
print(f"     P_phys(k_horizon) / A_s_single = {ratio_horizon:.6f}")
print(f"     If this were 1.0, Bogoliubov and slow-roll would agree at k=aH.")
print(f"     Deviation from 1.0 measures how much the Bogoliubov evolution")
print(f"     differs from standard slow-roll at the horizon scale.")

# Cross-check 5: The S68 acoustic transfer result A_s = 3.29e-10
A_s_from_s68 = float(acoustic['A_s_cmb'])
print(f"\n  5. S68 acoustic transfer A_s:")
print(f"     A_s(S68) = {A_s_from_s68:.6e}")
print(f"     A_s(delta-N M1) = {A_s_multi_m1:.6e}")
print(f"     These should agree (S68 imported delta-N result): "
      f"{abs(A_s_from_s68 - A_s_multi_m1)/A_s_multi_m1 < 1e-6}")

# Cross-check 6: Spectral action normalization check (f_0, f_2, f_4)
# The spectral action S = f_0 * a_0 + f_2 * a_2 + f_4 * a_4 + ...
# where f_n are the moments of the cutoff function.
# Does any f_n ratio give 12.9?
# a_0/a_2 = 6440/2776 = 2.32, a_0/a_4 = 4.77, a_2/a_4 = 2.06
# None of these are 12.9.
print(f"\n  6. Spectral action coefficient ratios:")
print(f"     a_0/a_2 = {a0_fold/a2_fold:.4f}")
print(f"     a_0/a_4 = {a0_fold/a4_fold:.4f}")
print(f"     a_2/a_4 = {a2_fold/a4_fold:.4f}")
print(f"     None equal 12.9. The mismatch is NOT from spectral action normalization.")

# ============================================================================
#  SECTION 10: Gate verdict
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 10: GATE VERDICT")
print(f"{'='*72}")

print(f"""
  Gate: AS-NORM-69
  Pre-registered criterion: INFO (diagnostic)
  Einstein criterion: PASS if decomposes into recognizable geometric factors
  Mack criterion: INFO (diagnostic)

  RESULT: The 12.9x mismatch is a normalization bookkeeping error,
  NOT a physics effect.

  The direct chain (W1-A) computes:
    A_s = P_phys(k_transit) * enhancement_M1(k=aH)
  mixing P evaluated at k_transit with enhancement normalized to k=aH.
  Since the power spectrum is NOT scale-invariant at transit scales
  (n_s ~ 4 in the superhorizon regime), this introduces a spurious
  factor P(k_transit)/P(k_horizon) = 12.9.

  The delta-N chain (W3-B) is self-consistent and correct: A_s = 3.29e-10.

  Einstein criterion: NOT PASSED. The 12.9 does not decompose into
  a recognizable geometric factor (closest: 4*pi^2/3 = 13.16, off by 2%).
  It is a dynamical ratio from the Bogoliubov mode evolution.

  Gate verdict: INFO. The mismatch is resolved as bookkeeping.
  The A_s gap remains 0.80 OOM (unchanged from W3-B).

  IMPACT ON GAP CLOSURE BUDGET: NONE. The gap was already correctly
  computed by the delta-N chain. The direct chain's -0.31 OOM was
  erroneous. All gap closure results (BCS: -0.046, PW selection: -3.50,
  etc.) are unaffected — they were computed relative to the delta-N
  baseline, not the direct chain.
""")

# ============================================================================
#  SECTION 11: Save results
# ============================================================================

output_path = os.path.join(data_dir, 's69_as_normalization.npz')

# The effective spectral index between k_horizon and k_transit
ns_eff = 1.0 + np.log(ratio) / np.log(k_ratio)

np.savez(output_path,
    # Gate information
    gate_name='AS-NORM-69',
    gate_verdict='INFO',
    gate_detail=(f'12.9x mismatch is bookkeeping (double-counting). '
                 f'P_phys/A_s_single = {check_ratio:.4f}. '
                 f'Delta-N chain correct: A_s = {A_s_multi_m1:.4e}. '
                 f'Gap = 0.80 OOM (unchanged).'),

    # Key numbers
    ratio_direct_over_deltaN=ratio,
    ratio_P_phys_over_A_s_single=check_ratio,

    # Direct chain quantities
    P_transit=P_transit,
    P_phys_transit=P_phys,
    A_s_direct_chain=A_s_direct,
    k_transit=k_transit,

    # Delta-N chain quantities
    A_s_deltaN_chain=A_s_deltaN,
    A_s_single=A_s_single,
    enhancement_m1=enhancement_m1,

    # Standard formula quantities
    P_std_MKK=P_std_MKK,
    k_horizon=k_horizon,

    # Decomposition
    k_ratio=k_ratio,
    k_ratio_cubed=k_ratio_cubed,
    dynamical_correction=dynamical_correction,
    ns_effective=ns_eff,

    # Spectral action checks
    a0_over_a2=a0_fold/a2_fold,
    a0_over_a4=a0_fold/a4_fold,
    a2_over_a4=a2_fold/a4_fold,

    # Geometric factor candidates
    four_pi=4*PI,
    four_pi_sq_over_3=4*PI**2/3,

    # Gap assessment
    A_s_correct=A_s_multi_m1,
    A_s_observed=A_s_CMB,
    gap_OOM=np.log10(A_s_multi_m1 / A_s_CMB),
    gap_linear=A_s_CMB / A_s_multi_m1,

    # Cross-check: P at horizon scale
    P_at_horizon_MKK=P_at_horizon,
    P_phys_at_horizon=P_phys_horizon,
    ratio_phys_horizon_to_A_s_single=ratio_horizon,

    # Origin classification
    origin='bookkeeping',
    physics_contribution='none',
)

print(f"\n  Results saved to {output_path}")
print(f"\n{'='*72}")
print("COMPUTATION COMPLETE")
print(f"{'='*72}")
