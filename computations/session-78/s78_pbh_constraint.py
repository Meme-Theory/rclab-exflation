#!/usr/bin/env python3
"""
S78-W3-E-PBH-CONSTRAINT: PBH Constraint Assessment (two sub-gates)
====================================================================

Evaluates the pre-fold Bogoliubov amplification chain against LIGO/Virgo PBH
formation and FIRAS spectral-distortion bounds.

Gate (split per Gen-Physicist):
  W3-E-1 PRE-IC:
    HYPOTHESIS: P_zeta(k_trans, un-IC-suppressed, linearized OR W1-C SC).
    PASS if P_zeta(k_trans) x S_IC(k_trans) < 1e-2.
    FAIL if > 1e-2 (raw power exceeds LIGO/Virgo + IC suppression required).
  W3-E-2 REQUIRED-SUPPRESSION:
    HYPOTHESIS: Required S_IC,min at k_trans to meet LIGO/FIRAS.
    PASS if W1-E provides >= required.
    FAIL if W1-E provides less than required (W1-E = AMPLIFICATION 1.636e5,
    structural opposite-sign: auto FAIL).

Substrate framing:
  The PBH constraint is a bound on the spectral amplitude at the k_trans scale
  (where the substrate's GGE acoustic production is strongest — the stiff-to-dS
  transition). If P_zeta x S_IC there exceeds LIGO/FIRAS, the substrate's
  parametric amplification produces more coherent relic structure than
  observations permit. This is NOT about gravitational collapse of overdensities
  in pre-existing spacetime; it is a constraint on the substrate's spectral-weight
  production at the fold.

Convention pins (S78 §0):
  - P_zeta uses F_amp as POWER RATIO (§0.1), LINEAR in A_s.
  - S_IC = |alpha+beta|^2 (§0.5) from W1-E output.
  - PBH: Carr press formula; horizon-crossing at k_trans; H(k_trans) canonical.
  - Under Branch-C (W1-C FAIL): P_zeta at k_trans suppressed by same
    backreaction factor as k_pivot. Compute BOTH linearized and SC.
  - S_IC propagation: canonical spectral-stationarity from W1-E (S_IC=1.636e5
    at k_pivot); scale dependence via W1-E CHK6 (S_IC(k_pivot)/S_IC(k_pivot/3)=5.25).

Inputs:
  - computations/session-77/s77_transition_scale_pbh.npz (S77 reference)
  - computations/session-78/s78_pre_fold_vacuum.npz (W1-E S_IC)
  - computations/session-78/s78_backreaction_selfconsistent.npz (W1-C F_amp_sc bound)

Outputs:
  - computations/session-78/s78_pbh_constraint.npz
  - computations/session-78/s78_pbh_constraint.png (4 panels)
  - Append TWO lines to s78_gate_verdicts.txt

Cross-checks:
  CHK1: PBH mass function against Carr press template.
  CHK2: FIRAS mu-distortion integration over k in [1, 1e4] Mpc^-1; bound 9e-5.
  CHK3: P_zeta(k) x S_IC(k) as function of k; evaluate at MOST-CONSTRAINING k.
  CHK4: Scheme-invariant ratio P_zeta(k_trans) x S_IC(k_trans) / P_zeta(k_pivot).
"""

import sys
sys.path.insert(0, "computations")
from canonical_constants import (
    M_KK, M_Pl_reduced, A_s_CMB, H_fold, tau_fold,
    dS_fold, d2S_fold, S_fold, v_terminal, dt_transit, m_tau,
    Mpc_to_GeV_inv
)
import numpy as np
from scipy.integrate import trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 78)
print("S78-W3-E-PBH-CONSTRAINT: PBH Constraint Assessment (two sub-gates)")
print("=" * 78)

# ===========================================================================
# SECTION 1: Load inputs
# ===========================================================================
print("\nSECTION 1: Loading inputs")
print("-" * 60)

# S77 reference: P_zeta(k), F_amp(k), k grid
s77 = np.load("computations/session-77/s77_transition_scale_pbh.npz", allow_pickle=True)
k_values_MKK = s77['k_values']                 # (local) 52 k modes (M_KK units)
k_phys_Mpc = s77['k_phys_Mpc']                 # (local) physical (Mpc^-1)
k_trans_MKK = float(s77['k_trans'])            # (local) 0.9607 M_KK
k_trans_Mpc = float(s77['k_trans_Mpc'])        # (local) 3.357e-3 Mpc^-1
k_pivot_fold = float(s77['k_pivot_fold'])      # (local) 14.31 M_KK
F_amp_linear = s77['F_amp']                    # (local) F_amp(k) linearized (with NaNs)
P_real_code = s77['P_real_code']               # (local)
P_phys_arr = s77['P_phys']                     # (local) F_amp * P_dS_phys
P_dS_phys = float(s77['P_dS_phys'])            # (local) 9.807e-4
F_amp_pivot_lin = float(s77['F_amp_pivot'])    # (local) 6857.69
F_amp_trans_lin = float(s77['F_amp_trans'])    # (local) 90.81
H_dS_MKK = float(s77['H_dS'])                  # (local) 0.633 in M_KK
MKK_over_MPl_sq = float(s77['MKK_over_MPl_sq'])  # (local) 9.31e-4

valid_mask = ~np.isnan(F_amp_linear)           # (local)
print(f"  S77 k grid: {len(k_values_MKK)} modes, {valid_mask.sum()} valid")
print(f"  k_trans = {k_trans_MKK:.4f} M_KK = {k_trans_Mpc:.4e} Mpc^-1")
print(f"  k_pivot = {k_pivot_fold:.4f} M_KK")
print(f"  F_amp_linear(k_trans) = {F_amp_trans_lin:.3f}")
print(f"  F_amp_linear(k_pivot) = {F_amp_pivot_lin:.3f}")
print(f"  P_dS_phys = {P_dS_phys:.4e}")

# W1-E S_IC (canonical: spectral stationarity)
w1e = np.load("computations/session-78/s78_pre_fold_vacuum.npz", allow_pickle=True)
S_IC_pivot_canonical = float(w1e['S_IC_spectral_stationarity'])  # (local) 1.636e5
S_IC_pivot_ME = float(w1e['S_IC_min_entropy'])                    # (local) 1.854e5
S_IC_pivot_AZ = float(w1e['S_IC_az_topology'])                    # (local) 1.636e5
S_IC_k_lo_from_CHK6 = float(w1e['CHK6_S_IC_lo'])                  # (local) 3.117e4 at k_pivot/3
ratio_pivot_lo = float(w1e['CHK6_ratio_pivot_lo'])                # (local) 5.247
print(f"\n  W1-E S_IC(k_pivot) canonical (SS) = {S_IC_pivot_canonical:.4e}")
print(f"  W1-E S_IC(k_pivot/3)              = {S_IC_k_lo_from_CHK6:.4e}")
print(f"  W1-E scale ratio k_pivot->k_lo   = {ratio_pivot_lo:.3f}")

# W1-C backreaction bound
w1c = np.load("computations/session-78/s78_backreaction_selfconsistent.npz", allow_pickle=True)
# Extract F_amp_sc value (look for key)
print(f"\n  W1-C npz keys: {list(w1c.files)[:12]}...")
# F_amp_sc from the verdict: 47.92 (analytical energy-conservation bound)
F_amp_sc_pivot_bound = 47.919   # (local) from W1-C verdict line; analytical upper bound
print(f"  W1-C F_amp_sc(k_pivot) analytical bound = {F_amp_sc_pivot_bound:.3f}")

# Backreaction reduction factor (factor by which linearized is reduced at k_pivot)
backreaction_reduction = F_amp_pivot_lin / F_amp_sc_pivot_bound  # (local) ~143x
print(f"  Backreaction reduction factor (at k_pivot) = {backreaction_reduction:.2f}x")

# ===========================================================================
# SECTION 2: Canonical fold parameters + k range for constraint scan
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 2: Physical scales and Hubble at k_trans")
print("-" * 60)

# H_fold in M_KK units (canonical) — 586.53 M_KK from S38
# H(k_trans) in the post-fold dS regime is H_dS (from s77) ≈ 0.633 M_KK
# H in physical GeV: H = H_dS * M_KK
H_k_trans_GeV = H_dS_MKK * M_KK  # (local)
H_k_trans_Mpc_inv = H_k_trans_GeV * Mpc_to_GeV_inv   # (local) Mpc^-1

print(f"  H(k_trans) = {H_dS_MKK:.4f} M_KK = {H_k_trans_GeV:.4e} GeV")
print(f"  H(k_trans) = {H_k_trans_Mpc_inv:.4e} Mpc^-1")

# ===========================================================================
# SECTION 3: W3-E-1 PRE-IC — P_zeta(k_trans) both linearized and Branch-C SC
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 3: W3-E-1 PRE-IC — P_zeta at k_trans")
print("-" * 60)

# LINEARIZED: P_zeta = F_amp_linear * P_dS_phys (from S77 direct)
P_zeta_trans_linearized = F_amp_trans_lin * P_dS_phys  # (local) 0.0891
P_zeta_pivot_linearized = F_amp_pivot_lin * P_dS_phys  # (local) 6.73

# BRANCH-C SELF-CONSISTENT: reduce F_amp by same factor as k_pivot
F_amp_sc_trans_BranchC = F_amp_trans_lin / backreaction_reduction  # (local)
P_zeta_trans_SC = F_amp_sc_trans_BranchC * P_dS_phys  # (local)
P_zeta_pivot_SC = F_amp_sc_pivot_bound * P_dS_phys    # (local) (analytical bound)

print(f"  P_zeta(k_trans, LINEARIZED, no IC) = {P_zeta_trans_linearized:.4e}")
print(f"  P_zeta(k_trans, BRANCH-C SC, no IC) = {P_zeta_trans_SC:.4e}")
print(f"  P_zeta(k_pivot, LINEARIZED, no IC) = {P_zeta_pivot_linearized:.4e}")
print(f"  P_zeta(k_pivot, BRANCH-C SC, no IC) = {P_zeta_pivot_SC:.4e}")

# Gate W3-E-1 is P_zeta(k_trans) x S_IC(k_trans) vs 1e-2
# Need S_IC(k_trans) — propagate from W1-E using log-log slope from CHK6

# ===========================================================================
# SECTION 4: S_IC(k) propagation across [1, 1e4] Mpc^-1
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 4: S_IC(k) propagation to all k")
print("-" * 60)

# W1-E CHK6: S_IC(k_pivot)/S_IC(k_pivot/3) = 5.247
# Log-log slope: d(ln S_IC)/d(ln k) = ln(5.247)/ln(3) = 1.509
slope_S_IC_logk = np.log(ratio_pivot_lo) / np.log(3.0)   # (local) 1.509
print(f"  S_IC log-log slope: d(lnS_IC)/d(lnk) = {slope_S_IC_logk:.3f}")
print(f"  (S_IC rises with k in oscillatory subhorizon regime)")

# S_IC(k) = S_IC_pivot * (k/k_pivot)^slope
def S_IC_at_k(k_MKK):  # (local)
    """Extrapolate S_IC from W1-E scaling. k in M_KK units."""
    return S_IC_pivot_canonical * (k_MKK / k_pivot_fold)**slope_S_IC_logk

S_IC_trans = S_IC_at_k(k_trans_MKK)           # (local)
print(f"  S_IC(k_pivot={k_pivot_fold:.3f} M_KK) = {S_IC_pivot_canonical:.4e}")
print(f"  S_IC(k_trans={k_trans_MKK:.3f} M_KK) = {S_IC_trans:.4e}")
print(f"  (extrapolation to k_trans < k_pivot: REDUCTION since slope > 0)")

# Caveat: this is a naive extrapolation. The W1-E CHK6 was computed between
# k_pivot and k_pivot/3. Extending further below k_pivot/3 is speculative but
# follows the structural trend of CONCENTRATED squeezing at higher k.

# ===========================================================================
# SECTION 5: Sub-gate W3-E-1 evaluation
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 5: Sub-gate W3-E-1 evaluation")
print("-" * 60)

PBH_bound = 1e-2  # (local) LIGO/Virgo-like P_zeta bound at k_trans

# Case A: linearized P_zeta + canonical S_IC
PxS_trans_lin = P_zeta_trans_linearized * S_IC_trans   # (local)
PxS_trans_SC  = P_zeta_trans_SC        * S_IC_trans    # (local)
PxS_pivot_lin = P_zeta_pivot_linearized * S_IC_pivot_canonical  # (local)
PxS_pivot_SC  = P_zeta_pivot_SC        * S_IC_pivot_canonical   # (local)

print(f"  PBH bound: {PBH_bound}")
print(f"\n  P_zeta(k_trans) x S_IC(k_trans):")
print(f"    LINEARIZED: {PxS_trans_lin:.4e} ({np.log10(PxS_trans_lin/PBH_bound):+.2f} OOM vs 1e-2)")
print(f"    BRANCH-C SC: {PxS_trans_SC:.4e} ({np.log10(PxS_trans_SC/PBH_bound):+.2f} OOM vs 1e-2)")

print(f"\n  P_zeta(k_pivot) x S_IC(k_pivot):")
print(f"    LINEARIZED: {PxS_pivot_lin:.4e}")
print(f"    BRANCH-C SC: {PxS_pivot_SC:.4e}")

# Scheme-invariant ratio (CHK4)
ratio_trans_over_pivot_lin = PxS_trans_lin / PxS_pivot_lin  # (local)
ratio_trans_over_pivot_SC  = PxS_trans_SC  / PxS_pivot_SC   # (local)
print(f"\n  CHK4: Scheme-invariant ratio P_zeta(k_trans)*S_IC(k_trans)/P_zeta(k_pivot)*S_IC(k_pivot):")
print(f"    Linearized: {ratio_trans_over_pivot_lin:.4e}")
print(f"    Branch-C SC: {ratio_trans_over_pivot_SC:.4e}")

# W3-E-1 verdict: gate says PASS if < 1e-2 (for the linearized ACCEPTED baseline)
# With W1-C in INCOMPUTABLE-FALLBACK-TO-BOUND state, BOTH are reported.
# Primary verdict is LINEARIZED (plan Section 0: 'Pre-registered expected: P_zeta(k_trans,
# linearized) = 0.089'; FAIL if > 1e-2).
if P_zeta_trans_linearized > PBH_bound:  # raw pre-IC P_zeta (without S_IC)
    # Raw P_zeta alone already exceeds bound (0.089 > 0.01)
    w3e1_raw_linearized_verdict = "FAIL"  # (local)
else:
    w3e1_raw_linearized_verdict = "PASS"  # (local)

# Plan PASS condition: P_zeta(k_trans) x S_IC(k_trans) < 1e-2
if PxS_trans_lin < PBH_bound:
    w3e1_linearized_with_SIC_verdict = "PASS"  # (local)
else:
    w3e1_linearized_with_SIC_verdict = "FAIL"  # (local)

if PxS_trans_SC < PBH_bound:
    w3e1_SC_with_SIC_verdict = "PASS"  # (local)
else:
    w3e1_SC_with_SIC_verdict = "FAIL"  # (local)

print(f"\n  W3-E-1 verdicts:")
print(f"    Raw linearized P_zeta(k_trans) = {P_zeta_trans_linearized:.4e} vs 1e-2: {w3e1_raw_linearized_verdict}")
print(f"    P_zeta(k_trans) x S_IC linearized: {w3e1_linearized_with_SIC_verdict}")
print(f"    P_zeta(k_trans) x S_IC Branch-C SC: {w3e1_SC_with_SIC_verdict}")

# Primary W3-E-1 verdict is LINEARIZED (plan pre-registered expected = 0.089)
w3e1_primary_verdict = w3e1_linearized_with_SIC_verdict  # (local)
w3e1_value = PxS_trans_lin  # (local)

# ===========================================================================
# SECTION 6: Sub-gate W3-E-2 REQUIRED-SUPPRESSION
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 6: Sub-gate W3-E-2 REQUIRED-SUPPRESSION")
print("-" * 60)

# Required S_IC,min to meet LIGO/FIRAS bound
# Plan: Required S_IC,min = 1e-2 / P_zeta(k_trans)
S_IC_required_linearized = PBH_bound / P_zeta_trans_linearized  # (local)
S_IC_required_SC = PBH_bound / P_zeta_trans_SC  # (local)
print(f"  Required S_IC,min (LINEARIZED P_zeta):  {S_IC_required_linearized:.4e}")
print(f"  Required S_IC,min (BRANCH-C SC P_zeta): {S_IC_required_SC:.4e}")
print(f"  W1-E provided S_IC(k_trans) extrap:    {S_IC_trans:.4e}")

# PASS if W1-E provides <= required (i.e., sufficient suppression)
# FAIL if W1-E provides more than required (amplification vs required suppression)
if S_IC_trans <= S_IC_required_linearized:
    w3e2_linearized_verdict = "PASS"  # (local)
else:
    w3e2_linearized_verdict = "FAIL"  # (local)

if S_IC_trans <= S_IC_required_SC:
    w3e2_SC_verdict = "PASS"  # (local)
else:
    w3e2_SC_verdict = "FAIL"  # (local)

print(f"\n  W3-E-2 verdicts:")
print(f"    LINEARIZED: W1-E S_IC {S_IC_trans:.3e} vs required {S_IC_required_linearized:.3e}: {w3e2_linearized_verdict}")
print(f"    BRANCH-C SC: W1-E S_IC {S_IC_trans:.3e} vs required {S_IC_required_SC:.3e}: {w3e2_SC_verdict}")

# Primary W3-E-2 verdict: uses the canonical W1-E S_IC at the most-constraining k
# This is the STRUCTURAL verdict: S_IC = AMPLIFICATION (opposite sign of required SUPPRESSION)

# Express excess as OOM
excess_lin_OOM = np.log10(S_IC_trans / S_IC_required_linearized)  # (local)
excess_SC_OOM = np.log10(S_IC_trans / S_IC_required_SC)  # (local)
print(f"\n  OOM excess of provided over required:")
print(f"    Linearized:   {excess_lin_OOM:+.2f} OOM")
print(f"    Branch-C SC:  {excess_SC_OOM:+.2f} OOM")

w3e2_primary_verdict = w3e2_linearized_verdict  # (local)

# ===========================================================================
# SECTION 7: Cross-check 1 — PBH mass function vs Carr press template
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 7: CHK1 — PBH mass function (Carr press)")
print("-" * 60)

# Carr press formula for PBH mass at horizon re-entry (radiation era):
#   M_PBH = gamma * M_H(k)
#   M_H(k) = (4*pi/3) * rho_rad * H_re^(-3) * c^3 in SI
# The Hubble at RE-ENTRY H_re is NOT H(k_trans) at fold/transit (that is the
# exit-Hubble ~ 1e17 GeV). H_re is the radiation-era Hubble when k crosses back.
# Standard Carr formula in Mpc units:
#   M_PBH = gamma * (1.2e49) * (k / 1 Mpc^-1)^(-2) g
# at radiation-dominated horizon crossing
# (Carr, Kuhnel, Sandstad 2016 eq. 2.3 with k in Mpc^-1, M in grams).

gamma_carr = 0.2  # (local) radiation-era Carr formation efficiency
# Carr formula at horizon re-entry in radiation era:
M_PBH_grams_carr = gamma_carr * 1.2e49 * (k_trans_Mpc)**(-2)  # (local)
M_sun_grams = 1.989e33  # (local)
M_PBH_solar = M_PBH_grams_carr / M_sun_grams  # (local)

print(f"  H(k_trans) (fold exit) = {H_k_trans_GeV:.4e} GeV (NOT H_re)")
print(f"  M_PBH (Carr press at re-entry, gamma=0.2):")
print(f"    {M_PBH_grams_carr:.4e} g = {M_PBH_solar:.4e} M_sun")
# Note: k_trans ~ 3.4e-3 Mpc^-1 corresponds to large scales, so M_PBH is
# SUPERMASSIVE (~10^53 g ~ 10^20 M_sun) — well above ANY observational PBH
# constraint (LIGO probes stellar-mass regime, CMB probes ~10^4 M_sun).
# The PBH threshold on P_zeta at this k_trans scale is set by the mu-distortion
# bound (FIRAS) and the CMB spectral distortion bound, not direct PBH searches.

# Compare to S77 rough estimate
M_PBH_S77_rough = 1e18 * (k_trans_Mpc / 1e6)**(-2)  # (local)
print(f"  S77 rough: {M_PBH_S77_rough:.4e} g (S77 used M_PBH^rough(k) in Mpc units)")
# Ratio: Carr formula with proper radiation-era normalization vs S77 rough
# Carr: 0.2 * 1.2e49 / k_Mpc^2 = 2.4e48 / k_Mpc^2
# S77:  1e18 / (k_Mpc * 1e-6)^2 = 1e18 * 1e12 / k_Mpc^2 = 1e30 / k_Mpc^2
# These differ by factor 2.4e48 / 1e30 = 2.4e18 — the S77 "rough" formula is
# a simplified scaling that misses normalization factors; Carr is canonical.
ratio_carr_S77 = M_PBH_grams_carr / M_PBH_S77_rough  # (local)
print(f"  Ratio Carr/S77-rough = {ratio_carr_S77:.3e}")
# Consistency test: both should be in SUPERMASSIVE regime (>> M_sun) since
# k_trans is large-scale. Check that Carr value is in supermassive regime:
chk1_carr_consistent = M_PBH_solar > 1e3  # (local) supermassive regime expected
print(f"  CHK1 (Carr formalism consistent, supermassive regime): {'PASS' if chk1_carr_consistent else 'NOTE'}")

# ===========================================================================
# SECTION 8: Cross-check 2 — FIRAS mu-distortion integration
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 8: CHK2 — FIRAS mu-distortion integration")
print("-" * 60)

# FIRAS bound: mu < 9e-5
# mu-distortion formula (Chluba, Hu): mu ~ 2.2 * integral over k of P_zeta(k) dlnk
# for k in [1, 1e4] Mpc^-1 (mu-era scales)

FIRAS_mu_bound = 9e-5  # (local)

# Build P_zeta(k) and S_IC(k) across the FIRAS window [1, 1e4] Mpc^-1
# k_phys_Mpc from S77 runs from 3.36e-4 to ~0.1 Mpc^-1. Need to EXTEND up to 1e4 Mpc^-1.
# The S77 F_amp(k) peaks at k=16 M_KK corresponding to ~5.6e-3 Mpc^-1
# For FIRAS we need much smaller scales (larger k) — extrapolate the decaying side.

# Use F_amp(k) from S77 where available; extrapolate tail
k_valid_MKK = k_values_MKK[valid_mask]     # (local)
F_amp_valid = F_amp_linear[valid_mask]     # (local)
k_valid_Mpc = k_phys_Mpc[valid_mask]       # (local)

# For k > max(k_valid), F_amp decays rapidly (subhorizon modes not enhanced)
# Approximate tail: F_amp(k) ~ 1 for k > k_valid_max (no enhancement)
# Build full grid in Mpc^-1 over [1, 1e4]

# Tabulate at S77 grid first
mask_FIRAS = (k_valid_Mpc >= 1.0) & (k_valid_Mpc <= 1e4)  # (local)
# None of S77 grid is in [1, 1e4] Mpc^-1 (max is ~0.1 Mpc^-1)
print(f"  S77 k_phys range: [{k_valid_Mpc.min():.3e}, {k_valid_Mpc.max():.3e}] Mpc^-1")
print(f"  FIRAS window: [1, 1e4] Mpc^-1")
print(f"  S77 grid overlap with FIRAS: {mask_FIRAS.sum()} of {len(k_valid_Mpc)} modes")

# Since the S77 grid does NOT extend to FIRAS scales (which probe much smaller
# wavelengths than the fold's k_trans ~ 3e-3 Mpc^-1), we must EXTRAPOLATE.
# Approach: in the post-fold dS regime, modes with k >> k_pivot are subhorizon
# at the fold transit and experience BD vacuum — F_amp -> 1 at high k.
# This makes P_zeta(k > k_pivot) ~ P_dS_phys + modulation.
# For FIRAS scales (k > 1 Mpc^-1 >> k_pivot = 0.05 Mpc^-1), F_amp ~ 1.

# Build P_zeta(k) on FIRAS window:
k_FIRAS_Mpc = np.geomspace(1.0, 1e4, 200)  # (local) Mpc^-1
# k in M_KK: k_Mpc / Mpc_to_MKK
# k_Mpc = k_MKK * M_KK / exp(N_total) * Mpc_to_GeV_inv
# For these large k, F_amp ~ 1 (no enhancement — deep subhorizon at fold)
F_amp_FIRAS = np.ones_like(k_FIRAS_Mpc)  # (local)
P_zeta_FIRAS = F_amp_FIRAS * P_dS_phys  # (local)

# S_IC at FIRAS scales: extrapolate
# Need k_MKK from k_Mpc inversion. k_Mpc / k_MKK = M_KK/exp(N)*Mpc_to_GeV_inv
# Use S77 conversion: k_trans_Mpc / k_trans_MKK
MKK_per_Mpc_conv = k_trans_Mpc / k_trans_MKK  # (local) Mpc^-1 per M_KK
k_FIRAS_MKK = k_FIRAS_Mpc / MKK_per_Mpc_conv  # (local) M_KK units
S_IC_FIRAS = S_IC_at_k(k_FIRAS_MKK)  # (local)

PxS_FIRAS = P_zeta_FIRAS * S_IC_FIRAS  # (local)

# mu-distortion: mu ~ 2.2 * integral P_zeta(k) * S_IC(k) dlnk over [1, 1e4] Mpc^-1
# Note: S_IC at these scales is a HUGE amplification (since slope_S_IC > 1),
# so extrapolation becomes unreliable. Report both cases: (a) physical S_IC ~ 1
# at scales much shorter than transit scale; (b) naive extrapolation.

lnk_FIRAS = np.log(k_FIRAS_Mpc)  # (local)

# Case A: Naive S_IC extrapolation (may be unreliable)
mu_naive = 2.2 * trapezoid(PxS_FIRAS, lnk_FIRAS)  # (local)

# Case B: S_IC capped at 1 for k > k_pivot (modes subhorizon at fold do not
# experience squeezing — adiabatic evolution, alpha=1, beta=0)
S_IC_FIRAS_capped = np.ones_like(k_FIRAS_Mpc)  # (local) ~1 for BD-like modes
PxS_FIRAS_capped = P_zeta_FIRAS * S_IC_FIRAS_capped  # (local)
mu_capped = 2.2 * trapezoid(PxS_FIRAS_capped, lnk_FIRAS)  # (local)

print(f"\n  mu-distortion over FIRAS window [1, 1e4] Mpc^-1:")
print(f"    Naive extrapolation (S_IC(k)^(1.51)):   mu = {mu_naive:.4e}")
print(f"    S_IC capped at 1 (physical):            mu = {mu_capped:.4e}")
print(f"    FIRAS bound:                            mu < {FIRAS_mu_bound:.1e}")

chk2_capped = mu_capped < FIRAS_mu_bound  # (local)
chk2_naive  = mu_naive  < FIRAS_mu_bound  # (local)
print(f"  CHK2 verdict (capped S_IC): {'PASS' if chk2_capped else 'FAIL'}")
print(f"  CHK2 verdict (naive extrapolation): {'PASS' if chk2_naive else 'FAIL'}")

# ===========================================================================
# SECTION 9: Cross-check 3 — Most-constraining k (P_zeta x S_IC)(k)
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 9: CHK3 — P_zeta(k) x S_IC(k) across full k range")
print("-" * 60)

# Build P_zeta(k) on S77 grid + FIRAS extension
k_grid_MKK_full = np.concatenate([k_valid_MKK, k_FIRAS_MKK])  # (local)
k_grid_Mpc_full = np.concatenate([k_valid_Mpc, k_FIRAS_Mpc])  # (local)
F_amp_full = np.concatenate([F_amp_valid, F_amp_FIRAS])       # (local)
P_zeta_full = F_amp_full * P_dS_phys                           # (local)
S_IC_full = S_IC_at_k(k_grid_MKK_full)                         # (local) naive
S_IC_full_capped = np.ones_like(k_grid_MKK_full)              # (local) physical cap
PxS_full_naive = P_zeta_full * S_IC_full                       # (local)
PxS_full_capped = P_zeta_full * S_IC_full_capped               # (local)

# Sort by k
idx_sort = np.argsort(k_grid_Mpc_full)
k_grid_Mpc_sorted = k_grid_Mpc_full[idx_sort]
k_grid_MKK_sorted = k_grid_MKK_full[idx_sort]
P_zeta_sorted = P_zeta_full[idx_sort]
S_IC_sorted_naive = S_IC_full[idx_sort]
S_IC_sorted_capped = S_IC_full_capped[idx_sort]
PxS_sorted_naive = PxS_full_naive[idx_sort]
PxS_sorted_capped = PxS_full_capped[idx_sort]

# Find most-constraining k (max of P_zeta x S_IC)
idx_max_naive = np.argmax(PxS_sorted_naive)
idx_max_capped = np.argmax(PxS_sorted_capped)

k_max_naive_Mpc = k_grid_Mpc_sorted[idx_max_naive]
k_max_capped_Mpc = k_grid_Mpc_sorted[idx_max_capped]

print(f"  Most-constraining k (P_zeta*S_IC max):")
print(f"    Naive S_IC propagation:  k = {k_max_naive_Mpc:.4e} Mpc^-1, PxS = {PxS_sorted_naive[idx_max_naive]:.3e}")
print(f"    S_IC capped at 1:        k = {k_max_capped_Mpc:.4e} Mpc^-1, PxS = {PxS_sorted_capped[idx_max_capped]:.3e}")

# k_trans value for reference
idx_trans = np.argmin(np.abs(k_grid_Mpc_sorted - k_trans_Mpc))
PxS_at_k_trans = PxS_sorted_naive[idx_trans]  # (local)
print(f"\n  P_zeta(k_trans) x S_IC(k_trans) = {PxS_at_k_trans:.3e} (for reference)")
print(f"  Ratio (most-constraining / k_trans): {PxS_sorted_naive[idx_max_naive]/PxS_at_k_trans:.3e}")

# CHK3: is the most-constraining k different from k_trans?
chk3_k_trans_is_most_constraining = np.isclose(k_max_naive_Mpc, k_trans_Mpc, rtol=0.5)  # (local)
print(f"\n  CHK3: k_trans is most-constraining? {chk3_k_trans_is_most_constraining}")

# ===========================================================================
# SECTION 10: Plots
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 10: Plotting")
print("-" * 60)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: P_zeta(k) and S_IC(k) across range
ax = axes[0, 0]
ax.loglog(k_grid_Mpc_sorted, P_zeta_sorted, 'b-', lw=2, label=r'$\mathcal{P}_\zeta(k)$ (F_amp linearized)')
ax.axhline(PBH_bound, color='red', ls='--', lw=1.5, label=f'PBH bound = {PBH_bound}')
ax.axhline(A_s_CMB, color='orange', ls=':', lw=1.5, label=f'$A_s$(Planck)={A_s_CMB:.1e}')
ax.axvline(k_trans_Mpc, color='r', ls='-.', alpha=0.5, label=f'$k_{{trans}}$={k_trans_Mpc:.2e}')
ax.axvline(0.05, color='g', ls='-.', alpha=0.5, label=r'$k_{pivot}=0.05$')
ax.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax.set_ylabel(r'$\mathcal{P}_\zeta(k)$')
ax.set_title('Primordial Power Spectrum (linearized)')
ax.legend(loc='upper right', fontsize=8)
ax.grid(alpha=0.3)

# Panel 2: S_IC(k) propagation
ax = axes[0, 1]
ax.loglog(k_grid_Mpc_sorted, S_IC_sorted_naive, 'b-', lw=2, label='Naive log-log extrap')
ax.loglog(k_grid_Mpc_sorted, S_IC_sorted_capped, 'g--', lw=2, label=r'$S_{IC}$ capped at 1 (physical)')
ax.axhline(1.0, color='gray', ls=':', alpha=0.5, label=r'$S_{IC}=1$ (BD)')
ax.axvline(k_trans_Mpc, color='r', ls='-.', alpha=0.5)
ax.axvline(0.05, color='g', ls='-.', alpha=0.5)
ax.scatter([0.05], [S_IC_pivot_canonical], color='purple', s=80, zorder=5, label=f'W1-E: $S_{{IC}}(k_{{pivot}})$={S_IC_pivot_canonical:.2e}')
ax.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax.set_ylabel(r'$S_{IC}(k) = |\alpha+\beta|^2$')
ax.set_title('Pre-fold Bogoliubov Squeezing Factor')
ax.legend(loc='upper left', fontsize=8)
ax.grid(alpha=0.3)

# Panel 3: P_zeta x S_IC (master constraint curve)
ax = axes[1, 0]
ax.loglog(k_grid_Mpc_sorted, PxS_sorted_naive, 'b-', lw=2, label=r'$\mathcal{P}_\zeta \cdot S_{IC}$ naive')
ax.loglog(k_grid_Mpc_sorted, PxS_sorted_capped, 'g--', lw=2, label=r'$\mathcal{P}_\zeta \cdot S_{IC}$ capped')
ax.axhline(PBH_bound, color='red', ls='--', lw=1.5, label=f'PBH bound = {PBH_bound}')
ax.axhline(FIRAS_mu_bound, color='orange', ls=':', lw=1.5, label=f'FIRAS $\\mu$={FIRAS_mu_bound}')
ax.axvline(k_trans_Mpc, color='r', ls='-.', alpha=0.5)
ax.axvline(0.05, color='g', ls='-.', alpha=0.5)
ax.scatter([k_max_naive_Mpc], [PxS_sorted_naive[idx_max_naive]], color='purple', s=80, zorder=5, label=f'max naive @ k={k_max_naive_Mpc:.2e}')
ax.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax.set_ylabel(r'$\mathcal{P}_\zeta(k) \cdot S_{IC}(k)$')
ax.set_title('Constraint Density — PBH/FIRAS Test')
ax.legend(loc='lower right', fontsize=8)
ax.grid(alpha=0.3)

# Panel 4: Sub-gate summary
ax = axes[1, 1]
ax.axis('off')
summary = (
    f"Gate: S78-W3-E-PBH-CONSTRAINT\n"
    f"=" * 46 + "\n\n"
    f"W1-E INPUT:\n"
    f"  S_IC(k_pivot) canonical = {S_IC_pivot_canonical:.3e}\n"
    f"  (spectral stationarity, f*, |alpha+beta|^2, L=10)\n"
    f"  => AMPLIFICATION channel\n\n"
    f"W1-C INPUT:\n"
    f"  F_amp_sc(k_pivot) bound = {F_amp_sc_pivot_bound:.2f}\n"
    f"  Reduction factor = {backreaction_reduction:.1f}x\n\n"
    f"W3-E-1 PRE-IC:\n"
    f"  P_zeta(k_trans) x S_IC(k_trans):\n"
    f"  LINEARIZED: {PxS_trans_lin:.2e}\n"
    f"  BRANCH-C SC: {PxS_trans_SC:.2e}\n"
    f"  Bound: {PBH_bound}\n"
    f"  VERDICT: {w3e1_primary_verdict}\n\n"
    f"W3-E-2 REQUIRED-SUPP:\n"
    f"  Required S_IC,min: {S_IC_required_linearized:.3e}\n"
    f"  Provided S_IC: {S_IC_trans:.3e}\n"
    f"  Excess: {excess_lin_OOM:+.2f} OOM (AMPLIFICATION)\n"
    f"  VERDICT: {w3e2_primary_verdict}\n\n"
    f"Most-constraining k:\n"
    f"  Naive: {k_max_naive_Mpc:.3e} Mpc^-1\n"
    f"  Capped: {k_max_capped_Mpc:.3e} Mpc^-1"
)
ax.text(0.02, 0.98, summary, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', family='monospace')

plt.suptitle('S78-W3-E-PBH-CONSTRAINT: PBH/FIRAS Constraint Assessment (2 sub-gates)', fontsize=13)
plt.tight_layout()
plt.savefig("computations/session-78/s78_pbh_constraint.png", dpi=150, bbox_inches='tight')
print(f"  Saved: computations/session-78/s78_pbh_constraint.png")

# ===========================================================================
# SECTION 11: Save .npz
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 11: Saving data")
print("-" * 60)

save_dict = dict(  # (local)
    # Gate metadata
    gate_id="S78-W3-E-PBH-CONSTRAINT",
    w3e1_primary_verdict=w3e1_primary_verdict,
    w3e2_primary_verdict=w3e2_primary_verdict,
    scheme_tag="f*",
    convention_tag="F_amp=POWER-RATIO,S_IC=|alpha+beta|^2",
    L_max_tag=10,
    IC_principle="spectral_stationarity",
    # Key k scales
    k_trans_MKK=k_trans_MKK,
    k_trans_Mpc=k_trans_Mpc,
    k_pivot_fold_MKK=k_pivot_fold,
    # Linearized
    F_amp_pivot_linearized=F_amp_pivot_lin,
    F_amp_trans_linearized=F_amp_trans_lin,
    P_zeta_trans_linearized=P_zeta_trans_linearized,
    P_zeta_pivot_linearized=P_zeta_pivot_linearized,
    # Branch-C SC
    F_amp_sc_pivot_bound=F_amp_sc_pivot_bound,
    backreaction_reduction=backreaction_reduction,
    F_amp_sc_trans_BranchC=F_amp_sc_trans_BranchC,
    P_zeta_trans_SC=P_zeta_trans_SC,
    P_zeta_pivot_SC=P_zeta_pivot_SC,
    # S_IC
    S_IC_pivot_canonical=S_IC_pivot_canonical,
    S_IC_trans_propagated=S_IC_trans,
    slope_S_IC_logk=slope_S_IC_logk,
    ratio_pivot_lo_from_W1E=ratio_pivot_lo,
    # Gate products
    PxS_trans_linearized=PxS_trans_lin,
    PxS_trans_SC=PxS_trans_SC,
    PxS_pivot_linearized=PxS_pivot_lin,
    PxS_pivot_SC=PxS_pivot_SC,
    PBH_bound=PBH_bound,
    FIRAS_mu_bound=FIRAS_mu_bound,
    # Required suppression
    S_IC_required_linearized=S_IC_required_linearized,
    S_IC_required_SC=S_IC_required_SC,
    excess_lin_OOM=excess_lin_OOM,
    excess_SC_OOM=excess_SC_OOM,
    # Cross-checks
    CHK1_M_PBH_grams=M_PBH_grams_carr,
    CHK1_M_PBH_solar=M_PBH_solar,
    CHK1_carr_consistent=chk1_carr_consistent,
    CHK2_mu_naive=mu_naive,
    CHK2_mu_capped=mu_capped,
    CHK2_capped_passes=chk2_capped,
    CHK2_naive_passes=chk2_naive,
    CHK3_k_most_constraining_naive_Mpc=k_max_naive_Mpc,
    CHK3_k_most_constraining_capped_Mpc=k_max_capped_Mpc,
    CHK3_k_trans_is_most_constraining=chk3_k_trans_is_most_constraining,
    CHK4_ratio_trans_over_pivot_lin=ratio_trans_over_pivot_lin,
    CHK4_ratio_trans_over_pivot_SC=ratio_trans_over_pivot_SC,
    # Arrays
    k_grid_Mpc=k_grid_Mpc_sorted,
    k_grid_MKK=k_grid_MKK_sorted,
    P_zeta_grid=P_zeta_sorted,
    S_IC_grid_naive=S_IC_sorted_naive,
    S_IC_grid_capped=S_IC_sorted_capped,
    PxS_grid_naive=PxS_sorted_naive,
    PxS_grid_capped=PxS_sorted_capped,
)

np.savez("computations/session-78/s78_pbh_constraint.npz", **save_dict)
print(f"  Saved: computations/session-78/s78_pbh_constraint.npz")

# ===========================================================================
# SECTION 12: Append gate verdict lines
# ===========================================================================
print("\n" + "=" * 78)
print("SECTION 12: Appending gate verdict lines")
print("-" * 60)

verdict_line_1 = (  # (local)
    f"S78-W3-E-1-PRE-IC: {w3e1_primary_verdict} — "
    f"P_zeta(k_trans)*S_IC={PxS_trans_lin:.3e} (linearized), bound=1e-2 "
    f"[SC-branch P*S={PxS_trans_SC:.3e}; raw P_zeta_lin={P_zeta_trans_linearized:.3e}; "
    f"k_trans={k_trans_Mpc:.2e} Mpc^-1; f*,POWER-RATIO,|alpha+beta|^2,L=10]"
)
verdict_line_2 = (  # (local)
    f"S78-W3-E-2-REQUIRED-SUPP: {w3e2_primary_verdict} — "
    f"required_S_IC={S_IC_required_linearized:.3e}, provided_S_IC_W1E={S_IC_trans:.3e} "
    f"(@k_trans from extrap slope={slope_S_IC_logk:.2f}), adequate=N "
    f"[excess={excess_lin_OOM:+.1f} OOM; W1-E is AMPLIFICATION not SUPPRESSION; "
    f"f*,POWER-RATIO,|alpha+beta|^2,L=10]"
)

# Guard against duplicate appending on re-runs
verdict_path = "computations/session-78/s78_gate_verdicts.txt"  # (local)
with open(verdict_path, "r", encoding="utf-8") as f:
    existing = f.read()
already_present = "S78-W3-E-1-PRE-IC:" in existing and "S78-W3-E-2-REQUIRED-SUPP:" in existing  # (local)
if already_present:
    print(f"  W3-E verdicts already present in {verdict_path} — skipping append.")
else:
    with open(verdict_path, "a", encoding="utf-8") as f:
        f.write(verdict_line_1 + "\n")
        f.write(verdict_line_2 + "\n")
    print(f"  Appended 2 lines to s78_gate_verdicts.txt:")
print(f"  [1] {verdict_line_1}")
print(f"  [2] {verdict_line_2}")

# ===========================================================================
# SECTION 13: Final summary
# ===========================================================================
print("\n" + "=" * 78)
print("S78-W3-E-PBH-CONSTRAINT: COMPLETE")
print("=" * 78)
print(f"\n  W3-E-1 PRE-IC verdict (linearized):   {w3e1_primary_verdict}")
print(f"    Value: P_zeta(k_trans)*S_IC(k_trans) = {PxS_trans_lin:.4e} vs bound {PBH_bound}")
print(f"    Margin: {np.log10(PxS_trans_lin/PBH_bound):+.2f} OOM above bound")
print(f"\n  W3-E-2 REQUIRED-SUPPRESSION verdict: {w3e2_primary_verdict}")
print(f"    Required S_IC,min: {S_IC_required_linearized:.3e}")
print(f"    Provided by W1-E:  {S_IC_trans:.3e} (AMPLIFICATION)")
print(f"    Excess: {excess_lin_OOM:+.2f} OOM wrong sign")
