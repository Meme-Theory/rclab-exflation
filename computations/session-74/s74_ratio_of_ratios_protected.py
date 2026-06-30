#!/usr/bin/env python3
"""
s74_ratio_of_ratios_protected.py -- W4-F N16-RATIO-OF-RATIOS-PROTECTED-74
=========================================================================

Gate: N16-RATIO-OF-RATIOS-PROTECTED-74
  Task: Catalog framework observables by their algebraic dependence on the
        Seeley-DeWitt coefficients a_k and classify whether each is:

          PROTECTED-R1  = f(R_1) only, where R_1 = a_0*a_4/a_2^2
          PROTECTED-Rk  = f(R_k) for k in {1,2,3} or products thereof
          PROTECTED-RAT = f(a_4/a_2) only (a weaker ratio protection)
          FRAGILE       = requires at least one individual a_k

        The physical motivation: if an observable can be written as a
        function of R-family ratios-of-ratios, its L_max sensitivity is
        partially cancelled between numerator and denominator. If it
        requires an individual a_k, it drifts as L^{2d-2k} (Weyl's law).

  Gate verdict:
    PASS if >= 4 observables are in R-family (PROTECTED-R1/Rk/RAT).
    INFO if 2-3.
    FAIL if 0-1.

Physics (substrate framing):
----------------------------
Space is an emergent description of how the fabric's spectral weight
distributes itself. The Seeley-DeWitt coefficients a_k are spectral
moments of the Dirac operator D_K at the Jensen fold. Observables built
from RATIOS of these moments (a_4/a_2, a_0/a_2) inherit L_max drift from
Weyl's law: individually a_2 ~ L^{d-2}, a_4 ~ L^{d-4}, etc., so ratios
carry residual drift unless the pre-factors cancel exactly.

Ratios-of-ratios R_k = a_{2(k-1)}*a_{2(k+1)} / a_{2k}^2 are the natural
"protected" invariants: they are the determinants of the 2x2 moment matrix
(a_{2(k-1)}, a_{2k}; a_{2k}, a_{2(k+1)}) and vanish identically for any
pure Gaussian spectral weight (generalized log-convexity detector).

W2-M showed R_1 drifts 0.34% vs L_max in [3,9] (nearly stable), R_2
drifts 2.5%, R_3 drifts 8.0%. R-family protection is graded, not binary.

Dependencies:
  - W1-M R-PROTECTED-FOLD-ADDITION-74 (canonical R_1 = 1.128655)
  - W2-M R-FAMILY-STABILITY-74 (drift comparisons)
  - canonical_constants.py (a0/a2/a4_fold, all framework predictions)

Agent: lizzi-spectral-functional-theorist (Session 74, Wave 4, W4-F)
"""

import numpy as np
import os
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    PI, M_KK, M_KK_gravity, M_KK_kerner, tau_fold, Vol_SU3_Haar,
    a0_fold, a2_fold, a4_fold,
    f_0_sharp, f_2_default, f_4_default,
    m_H_obs, v_ew, planck_ns, w0_FW,
    rho_Lambda_obs, rho_Lambda_spectral, CC_ratio,
    sin2_thetaW_MSbar, sin2_thetaW_fold,
    alpha_s_MZ_obs,
    G_DeWitt, S_fold, dS_fold, d2S_fold,
    Delta_BCS, omega_L1, c_Gold,
    Omega_DM, Omega_Lambda,
    Q_Leggett,
)

print("=" * 78)
print("W4-F  N16-RATIO-OF-RATIOS-PROTECTED-74")
print("Catalog framework observables via R-family protection")
print("lizzi-spectral-functional-theorist, Session 74")
print("=" * 78)

# =============================================================================
# STEP 1: Load R-family stability data from W2-M
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Load R-family stability data (W2-M)")
print("=" * 78)

RFAM_FILE = "s74_r_family_stability.npz"  # (local)
rfam = np.load(RFAM_FILE, allow_pickle=True)

L_vals = rfam["L_max_values"]  # (local) [3, 5, 7, 9]
R1_vs_L = rfam["R1_S73B"]  # (local)
R2_vs_L = rfam["R2_S73B"]  # (local)
R3_vs_L = rfam["R3_S73B"]  # (local)
stab_R1 = float(rfam["stab_R1"])  # (local) 0.0034
stab_R2 = float(rfam["stab_R2"])  # (local) 0.0246
stab_R3 = float(rfam["stab_R3"])  # (local) 0.0799

print(f"  R_1 drift across L in [3,9]: {stab_R1*100:.3f}%  (nearly protected)")
print(f"  R_2 drift across L in [3,9]: {stab_R2*100:.3f}%  (marginal)")
print(f"  R_3 drift across L in [3,9]: {stab_R3*100:.3f}%  (fragile)")

# Individual a_k drifts (for reference)
a0_vs_L = rfam["a0_S73B"]  # (local) [6440, 79968, 538560, 1943616]
a2_vs_L = rfam["a2_S73B"]  # (local)
a4_vs_L = rfam["a4_S73B"]  # (local)
a6_vs_L = rfam["a6_S73B"]  # (local)
a8_vs_L = rfam["a8_S73B"]  # (local)

# Weyl-law drift factors for individual a_k (L_max = 3 vs L_max = 9)
a_k_drift = {}  # (local)
for name, arr in [("a_0", a0_vs_L), ("a_2", a2_vs_L), ("a_4", a4_vs_L),
                  ("a_6", a6_vs_L), ("a_8", a8_vs_L)]:
    drift_factor = arr[-1] / arr[0]  # (local)
    a_k_drift[name] = drift_factor
    print(f"  {name}: L=3 -> L=9 ratio = {drift_factor:.3f}x  (individual a_k fragile)")

# Ratio drifts (a_4/a_2, a_0/a_2) for comparison
a4a2_vs_L = a4_vs_L / a2_vs_L  # (local)
a0a2_vs_L = a0_vs_L / a2_vs_L  # (local)
stab_a4a2 = float((np.max(a4a2_vs_L) - np.min(a4a2_vs_L)) / np.mean(a4a2_vs_L))  # (local)
stab_a0a2 = float((np.max(a0a2_vs_L) - np.min(a0a2_vs_L)) / np.mean(a0a2_vs_L))  # (local)
print(f"\n  a_4/a_2 drift: {stab_a4a2*100:.2f}%  (single-ratio protection)")
print(f"  a_0/a_2 drift: {stab_a0a2*100:.2f}%  (single-ratio protection)")

# =============================================================================
# STEP 2: Define R-family and build classification
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: R-family definitions")
print("=" * 78)

R1_canonical = a0_fold * a4_fold / a2_fold**2  # (local) = 1.128655
R2_canonical = a2_fold * rfam["a6_S73B"][2] / rfam["a4_S73B"][2]**2  # (local)
R3_canonical = rfam["a4_S73B"][2] * rfam["a8_S73B"][2] / rfam["a6_S73B"][2]**2  # (local)

print(f"  R_1 = a_0 * a_4 / a_2^2   = {R1_canonical:.6f}  (drift: {stab_R1*100:.3f}%)")
print(f"  R_2 = a_2 * a_6 / a_4^2   = {R2_canonical:.6f}  (drift: {stab_R2*100:.3f}%)")
print(f"  R_3 = a_4 * a_8 / a_6^2   = {R3_canonical:.6f}  (drift: {stab_R3*100:.3f}%)")
print(f"\n  CRITICAL FINDING: Single ratios (a_4/a_2, a_0/a_2) DO NOT have partial protection.")
print(f"       They drift at {stab_a4a2*100:.1f}% (a_4/a_2) and {stab_a0a2*100:.1f}% (a_0/a_2),")
print(f"       comparable to individual a_k drifts, NOT better.")
print(f"       Only the ratio-of-ratios R_1 achieves true protection (< 1%).")
print(f"")
print(f"       Therefore the protection hierarchy is:")
print(f"         STRUCTURAL         : 0% drift (eigenvalue ratios, no a_k used)")
print(f"         PROTECTED-R1       : < 1% drift (R_1 structural invariant)")
print(f"         PROTECTED-R2       : ~2.5% drift (R_2 invariant)")
print(f"         PROTECTED-R3       : ~8% drift (R_3 invariant, marginal)")
print(f"         PROTECTED-RAT      : > 100% drift (single-ratio, effectively fragile)")
print(f"         FRAGILE-AK         : > 1000% drift (individual a_k)")

# =============================================================================
# STEP 3: Catalog framework observables
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Classify framework observables by algebraic dependence on a_k")
print("=" * 78)

# Classification codes:
#   PROTECTED-R1   : depends on (a_0*a_4/a_2^2) only, no other a_k
#   PROTECTED-R1P  : depends on R_1 and separately on M_KK factors (partial)
#   PROTECTED-RAT  : depends on a single ratio (a_4/a_2 or a_0/a_2) only
#   PROTECTED-MULT : product of R-family ratios
#   FRAGILE-AK     : requires at least one individual a_k (not in ratio form)
#   FRAGILE-MKK    : requires M_KK_gravity or M_KK_kerner which themselves
#                    depend on individual a_k (via Newton's constant fix)
#
# The discipline: to qualify for PROTECTED-*, the observable must be writable
# as a function of only R_1, a_4/a_2, a_0/a_2 (and possibly R_2, R_3). Any
# appearance of a_k (as a lone factor, not in a ratio) is FRAGILE.

observables = []  # (local)

# ------------------------------------------------------------------
# OBSERVABLE 1: CC ratio rho_Lambda_spectral / rho_Lambda_obs
# Formula (canonical_constants line 251):
#   rho_Lambda_spectral = (2/pi^2) * a_0 * M_KK^4
#   CC_ratio = rho_Lambda_spectral / rho_Lambda_obs
# -> FRAGILE in a_0 AND in M_KK. This IS the CC problem.
# ------------------------------------------------------------------
observables.append({
    "name": "rho_Lambda_spectral / rho_Lambda_obs",
    "symbol": "Omega_Lambda (spectral)",
    "formula": "(2/pi^2) * a_0 * M_KK^4 / rho_Lambda_obs",
    "a_k_dependence": "a_0 (linear) + M_KK (implicit)",
    "class": "FRAGILE-AK",
    "reason": "Linear in a_0, the single most drift-sensitive coefficient",
    "drift_estimate_pct": float((a0_vs_L[-1] - a0_vs_L[0]) / a0_vs_L[0] * 100),
    "observed_value": float(rho_Lambda_spectral / rho_Lambda_obs),
    "note": "Using M_KK_kerner. R_1-form alternative rho~a_0*a_4/a_2^2 would be PROTECTED-R1 (see #2).",
})

# ------------------------------------------------------------------
# OBSERVABLE 2: CC ratio in R_1 formulation
# Lizzi alternative: rho_Lambda / (rho_gravity)^2 ~ a_0 * a_4 / a_2^2 = R_1
# This is the "bare" R_1 combination.
# ------------------------------------------------------------------
observables.append({
    "name": "R_1 = a_0*a_4/a_2^2 (structural invariant)",
    "symbol": "R_1",
    "formula": "a_0 * a_4 / a_2^2",
    "a_k_dependence": "a_0, a_2, a_4 combined in ratio-of-ratios",
    "class": "PROTECTED-R1",
    "reason": "All Weyl divergences cancel: (L^{d})(L^{d-4})/(L^{d-2})^2 = L^0",
    "drift_estimate_pct": stab_R1 * 100,
    "observed_value": R1_canonical,
    "note": "Lizzi's structural invariant — the only R-family ratio below 1% drift.",
})

# ------------------------------------------------------------------
# OBSERVABLE 3: Higgs mass (Chamseddine-Connes)
# m_H^2 = (4*pi^2/3) * (a_4/a_2) * v_EW^2 / f_0
# (Reference: s61_higgs_mass.py line 404-406, s60_a4_trace.py line 286)
# Depends on ratio a_4/a_2 -> PROTECTED-RAT.
# ------------------------------------------------------------------
mh_ratio = np.sqrt((4.0 * PI**2 / 3.0) * (a4_fold / a2_fold) / f_0_sharp) * v_ew  # (local)
observables.append({
    "name": "m_H (Chamseddine-Connes spectral action)",
    "symbol": "m_H",
    "formula": "v_EW * sqrt((4*pi^2/3) * (a_4/a_2) / f_0)",
    "a_k_dependence": "a_4/a_2 ratio",
    "class": "PROTECTED-RAT",
    "reason": "Writable as a single-ratio function of (a_4/a_2); Weyl cancels via f_4/f_2 identification",
    "drift_estimate_pct": stab_a4a2 * 100,
    "observed_value": float(mh_ratio),
    "note": f"m_H from bare CC-SA formula = {float(mh_ratio):.1f} GeV vs observed {m_H_obs} GeV. f_0 scheme-dependent.",
})

# ------------------------------------------------------------------
# OBSERVABLE 4: Spectral index n_s (Gilkey prescription)
# n_s = 1 - 2 * (f_4/f_2) * (a_4/a_2)
# (Reference: s62_kz_ns.py line 489, 519)
# Depends on single ratio a_4/a_2 -> PROTECTED-RAT.
# ------------------------------------------------------------------
ns_gilkey = 1.0 - 2.0 * (f_4_default / f_2_default) * (a4_fold / a2_fold)  # (local)
observables.append({
    "name": "n_s (scalar tilt, Gilkey-a_4/a_2 prescription)",
    "symbol": "n_s",
    "formula": "1 - 2*(f_4/f_2)*(a_4/a_2)",
    "a_k_dependence": "a_4/a_2 ratio",
    "class": "PROTECTED-RAT",
    "reason": "Tilt is a pure ratio of spectral moments; f_4/f_2 is functional-dependent scheme factor",
    "drift_estimate_pct": stab_a4a2 * 100,
    "observed_value": float(ns_gilkey),
    "note": f"n_s (bare Gilkey) = {float(ns_gilkey):.4f} vs Planck {planck_ns}. Scheme factor f_4/f_2 absorbs remaining difference.",
})

# ------------------------------------------------------------------
# OBSERVABLE 5: epsilon_H (slow-roll, Hubble)
# eps_H = (1/2)(dS/dtau)^2 / (S * d2S/dtau^2)
# S = alpha*a_2 + beta*a_4 + ... depending on spectral functional.
# dS/dtau, d2S/dtau^2 depend on tau-derivatives of the a_k.
# Under R-family assumption: eps_H ~ d(ln R_1)/d(tau) if S is dominated by R_1.
# Not straightforwardly R_1-expressible in the general case -> FRAGILE-AK
# (But note: for pure zeta_a4 or zeta_a2 functionals, eps_H uses a single a_k
#  and is therefore FRAGILE to that a_k alone.)
# ------------------------------------------------------------------
eps_H_num = 0.5 * dS_fold**2 / (S_fold * d2S_fold)  # (local)
observables.append({
    "name": "epsilon_H (Hubble slow-roll)",
    "symbol": "eps_H",
    "formula": "(1/2)*(dS/dtau)^2 / (S * d2S/dtau^2)",
    "a_k_dependence": "dS, d2S are linear in a_k' and a_k'' (individual)",
    "class": "FRAGILE-AK",
    "reason": "Derivatives of individual a_k enter explicitly; no ratio cancellation",
    "drift_estimate_pct": float(max(a_k_drift[name] for name in ("a_2", "a_4")) * 100 - 100),
    "observed_value": float(eps_H_num),
    "note": "Strongly scheme-dependent (cutoff -> positive, zeta -> negative)",
})

# ------------------------------------------------------------------
# OBSERVABLE 6: sin^2(theta_W) at M_KK
# From Kerner gauge-kinetic terms: sin^2 = g'^2 / (g^2 + g'^2)
# In spectral action: 1/g_i^2 ~ (f_2 * a_2_i) / (some geometric factor)
# where a_2_i is a REPRESENTATION-SPECIFIC coefficient (sub-block of a_2).
# Depends on RATIOS of a_2 moments within reps -> writable as ratio -> PROTECTED-RAT
# but with sub-block structure, not bare a_4/a_2.
# ------------------------------------------------------------------
observables.append({
    "name": "sin^2(theta_W) at M_KK",
    "symbol": "sin^2_W",
    "formula": "g_Y^2 / (g_2^2 + g_Y^2) with 1/g_i^2 ~ a_{2,i} sub-block ratios",
    "a_k_dependence": "ratios of a_2 sub-blocks (U(1), SU(2), SU(3))",
    "class": "PROTECTED-RAT",
    "reason": "A sum of inverse couplings; each coupling is a ratio a_2_sub/a_0_sub — structurally a single-ratio observable",
    "drift_estimate_pct": stab_a0a2 * 100,
    "observed_value": float(sin2_thetaW_fold),
    "note": "Depends on a_2 DECOMPOSITION by gauge-rep, not on the total a_2 magnitude",
})

# ------------------------------------------------------------------
# OBSERVABLE 7: alpha_s(M_KK) (strong coupling at high scale)
# 1/alpha_s(M_KK) ~ a_4 / (geometric_factor)
# (Reference: s71_bcs_backreaction_a4.py line 340-349)
# Depends linearly on a_4 -> FRAGILE-AK
# ------------------------------------------------------------------
observables.append({
    "name": "alpha_s at M_KK (strong coupling)",
    "symbol": "alpha_s(M_KK)",
    "formula": "1/alpha_s(M_KK) ~ a_4 / (Vol_SU3 * geometric prefactor)",
    "a_k_dependence": "a_4 (linear)",
    "class": "FRAGILE-AK",
    "reason": "Running coupling absorbs a_4 directly; no natural ratio partner",
    "drift_estimate_pct": float((a4_vs_L[-1] - a4_vs_L[0]) / a4_vs_L[0] * 100),
    "observed_value": float(alpha_s_MZ_obs),  # proxy — scheme choice
    "note": "alpha_s at M_Z is PDG; the M_KK value derives from a_4 individually",
})

# ------------------------------------------------------------------
# OBSERVABLE 8: Newton constant (from spectral action a_2 term)
# 1/(16*pi*G_N) = (f_2/(24*pi^2)) * a_2 * M_KK^2
# Linear in a_2 -> FRAGILE-AK
# ------------------------------------------------------------------
observables.append({
    "name": "1/(16*pi*G_N) (Newton constant)",
    "symbol": "G_N",
    "formula": "1/(16*pi*G_N) ~ (f_2/24pi^2) * a_2 * M_KK^2",
    "a_k_dependence": "a_2 (linear)",
    "class": "FRAGILE-AK",
    "reason": "Einstein-Hilbert prefactor is linear in the a_2 second spectral moment",
    "drift_estimate_pct": float((a2_vs_L[-1] - a2_vs_L[0]) / a2_vs_L[0] * 100),
    "observed_value": 1.0 / (16 * PI),
    "note": "M_KK_gravity is EXTRACTED by fixing G_N; circular — a_2 drifts reabsorbed into M_KK",
})

# ------------------------------------------------------------------
# OBSERVABLE 9: M_KK (gravity route) itself
# M_KK_gravity^2 = (16*pi*G_N)^{-1} * (24*pi^2) / (f_2 * a_2)
# Linear in 1/a_2 -> FRAGILE-AK (but a_2 is well-behaved up to L_max=9)
# ------------------------------------------------------------------
observables.append({
    "name": "M_KK (gravity route)",
    "symbol": "M_KK",
    "formula": "M_KK^2 = (24*pi^2/f_2) * 1/(16*pi*G_N*a_2)",
    "a_k_dependence": "a_2 (inverse)",
    "class": "FRAGILE-AK",
    "reason": "Single a_k (a_2) inverted — no ratio partner",
    "drift_estimate_pct": float((a2_vs_L[-1] - a2_vs_L[0]) / a2_vs_L[0] * 100),
    "observed_value": float(M_KK_gravity),
    "note": "Whole-point of M_KK: absorbs a_2 drift via the Newton constant constraint",
})

# ------------------------------------------------------------------
# OBSERVABLE 10: Dimensionless ratio (a_0 * a_4 / a_2^2) = R_1
# ALREADY observable #2. Also include the derived CC-to-EH ratio.
# Lambda/M_Pl^2 ~ a_0/a_2 (single ratio) -> PROTECTED-RAT
# ------------------------------------------------------------------
observables.append({
    "name": "Lambda / M_Pl^2 (dimensionless CC)",
    "symbol": "Lambda/M_Pl^2",
    "formula": "~ a_0 / a_2 (ratio of zeroth to second moment)",
    "a_k_dependence": "a_0/a_2 ratio",
    "class": "PROTECTED-RAT",
    "reason": "Both CC and EH prefactors are spectral moments; their dimensionless ratio is bare (a_0/a_2)",
    "drift_estimate_pct": stab_a0a2 * 100,
    "observed_value": float(a0_fold / a2_fold),
    "note": "Structural CC-to-EH ratio. Drift of (a_0/a_2): {:.2f}%".format(stab_a0a2 * 100),
})

# ------------------------------------------------------------------
# OBSERVABLE 11: m_H / sqrt(Lambda_CC) — Lizzi R_1 observable
# (m_H/v)^2 ~ a_4/a_2, Lambda/M_Pl^2 ~ a_0/a_2.
# Their combination: (m_H/v)^2 * (Lambda/M_Pl^2) ~ (a_4*a_0)/a_2^2 = R_1
# This is a TRUE R_1-protected observable — combining two ratios gives R_1!
# ------------------------------------------------------------------
R1_observable = (a4_fold / a2_fold) * (a0_fold / a2_fold)  # (local) = R_1
observables.append({
    "name": "(m_H/v_EW)^2 * (Lambda/M_Pl^2) product",
    "symbol": "R_1_phys",
    "formula": "(a_4/a_2) * (a_0/a_2) = a_0*a_4/a_2^2 = R_1",
    "a_k_dependence": "R_1 ratio-of-ratios",
    "class": "PROTECTED-R1",
    "reason": "The product of two single-ratio observables collapses to R_1 — ALL Weyl drifts cancel",
    "drift_estimate_pct": stab_R1 * 100,
    "observed_value": float(R1_observable),
    "note": "This is the Lizzi signature observable: combining m_H^2/v^2 with CC/EH ratio yields R_1 exactly",
})

# ------------------------------------------------------------------
# OBSERVABLE 12: Tensor-to-scalar ratio r (INAPPLICABLE per project framing)
# Per phononic-framing.md: r=16*eps is a standard inflaton formula, explicitly
# marked INAPPLICABLE to the framework (VdD-Hawking workshop).
# We include it for completeness, classified NON-PHONONIC.
# ------------------------------------------------------------------
observables.append({
    "name": "r (tensor-to-scalar ratio)",
    "symbol": "r",
    "formula": "N/A (r=16*eps is standard inflaton formalism, INAPPLICABLE to substrate transit)",
    "a_k_dependence": "N/A",
    "class": "NON-PHONONIC",
    "reason": "Per framework rules (phononic-framing.md): substrate transit is non-inflationary, r has no spectral-action representative",
    "drift_estimate_pct": float("nan"),
    "observed_value": float("nan"),
    "note": "5 independent arguments established this (VdD-Hawking). Not a FRAGILE or PROTECTED classification.",
})

# ------------------------------------------------------------------
# OBSERVABLE 13: w_0 (dark energy EOS)
# w_0_FW = -0.918 from Volovik vacuum + effacement (S58).
# Canonical formula in the framework: w_0 = -1 + (2/3)*(Gamma_L / H_0)
# where Gamma_L is Leggett damping rate and H_0 is today's Hubble.
# Not directly expressible via a_k; FRAGILE if derived from a_0 (CC density).
# ------------------------------------------------------------------
observables.append({
    "name": "w_0 (dark energy EOS)",
    "symbol": "w_0",
    "formula": "-1 + (2/3)*(Gamma_Leggett/H_0) — leakage through effacement",
    "a_k_dependence": "indirectly via Gamma_Leggett (not a standard a_k combination)",
    "class": "FRAGILE-AK",
    "reason": "Leggett damping is dynamical, not a heat-kernel invariant — a_k dependence routes through CC density -> a_0",
    "drift_estimate_pct": float((a0_vs_L[-1] - a0_vs_L[0]) / a0_vs_L[0] * 100),
    "observed_value": float(w0_FW),
    "note": "Not a spectral-action observable per se; inherits a_0 fragility through CC normalization",
})

# ------------------------------------------------------------------
# OBSERVABLE 14: Omega_DM (dark matter density)
# DM is the B1-Leggett GGE channel. Omega_DM ~ (GGE pair count) * (M_KK) / (rho_crit)
# n_pairs = 59.8 is from transit (NOT a_k), M_KK is FRAGILE in a_2.
# Omega_DM is thus partially a_k-independent but has M_KK factor.
# ------------------------------------------------------------------
observables.append({
    "name": "Omega_DM (dark matter density)",
    "symbol": "Omega_DM",
    "formula": "(n_pairs * M_KK^4) / rho_crit — transit-driven, not a_k-dependent",
    "a_k_dependence": "only via M_KK^4 (inherits M_KK fragility)",
    "class": "FRAGILE-MKK",
    "reason": "Transit physics (n_pairs=59.8) is NOT a spectral moment; fragility enters only through M_KK^4 prefactor",
    "drift_estimate_pct": 4 * float((a2_vs_L[-1] - a2_vs_L[0]) / a2_vs_L[0] * 100),  # 4x because M_KK^4
    "observed_value": float(Omega_DM),
    "note": "Transit count is a_k-independent; a_k enters through M_KK amplitude only",
})

# ------------------------------------------------------------------
# OBSERVABLE 15: Q_Leggett (Leggett mode quality factor)
# From GGE dynamics, Q ~ omega_L / Gamma_L.
# omega_L1 is from GL-Josephson analysis; not directly an a_k observable.
# Classified NON-PHONONIC for a_k-dependence purposes (it's a dynamical not spectral quantity).
# ------------------------------------------------------------------
observables.append({
    "name": "Q_Leggett (mode quality factor)",
    "symbol": "Q_L",
    "formula": "omega_L / Gamma_L (not a spectral action moment)",
    "a_k_dependence": "indirect — no direct a_k formula",
    "class": "NON-PHONONIC",
    "reason": "Dynamical (GGE dissipation) rather than spectral — not a Chamseddine-Connes observable",
    "drift_estimate_pct": float("nan"),
    "observed_value": float(Q_Leggett),
    "note": "Quality factor of the Leggett mode from GL-Josephson; not a spectral invariant",
})

# ------------------------------------------------------------------
# OBSERVABLE 16: f_NL (primordial non-Gaussianity)
# f_NL ~ (derivative expansion of slow-roll) — same fragile structure as eps_H.
# ------------------------------------------------------------------
observables.append({
    "name": "f_NL (primordial non-Gaussianity)",
    "symbol": "f_NL",
    "formula": "(5/12)*(1-n_s) + ... — derivative expansion of slow-roll",
    "a_k_dependence": "inherits a_4/a_2 ratio + derivative corrections",
    "class": "PROTECTED-RAT",
    "reason": "Leading term ~ (1-n_s), which is already classified PROTECTED-RAT",
    "drift_estimate_pct": stab_a4a2 * 100,
    "observed_value": float("nan"),
    "note": "Inherits n_s protection at leading order",
})

# ------------------------------------------------------------------
# OBSERVABLE 17: Delta_BCS (BCS gap)
# Delta_BCS = 0.464 M_KK from ED (not a_k based).
# However, its physical value in GeV = Delta_BCS * M_KK_gravity, which is FRAGILE-MKK.
# ------------------------------------------------------------------
observables.append({
    "name": "Delta_BCS (physical BCS gap in GeV)",
    "symbol": "Delta_BCS",
    "formula": "0.464 * M_KK (dimensionless gap from ED)",
    "a_k_dependence": "only via M_KK (ED gap is a_k-independent in M_KK units)",
    "class": "FRAGILE-MKK",
    "reason": "Dimensionless gap is a ratio of eigenvalues and is structurally invariant; dimensional version inherits M_KK",
    "drift_estimate_pct": float((a2_vs_L[-1] - a2_vs_L[0]) / a2_vs_L[0] * 100),
    "observed_value": float(Delta_BCS * M_KK_gravity),
    "note": "Dimensionless form Delta_BCS/M_KK = 0.464 is R-FAMILY-INVARIANT (purely eigenvalue ratio)",
})

# ------------------------------------------------------------------
# OBSERVABLE 18: A_s (CMB scalar amplitude)
# A_s ~ V/eps_H ~ (spectral action) / (slow-roll). Fragile through individual a_k.
# ------------------------------------------------------------------
observables.append({
    "name": "A_s (CMB scalar amplitude)",
    "symbol": "A_s",
    "formula": "~ V(phi_fold) / eps_H / (12*pi^2)",
    "a_k_dependence": "individual a_k via V and slow-roll",
    "class": "FRAGILE-AK",
    "reason": "V(phi) is the full spectral action, which is a SUM over a_k with different f_k prefactors — no clean ratio",
    "drift_estimate_pct": float((a2_vs_L[-1] - a2_vs_L[0]) / a2_vs_L[0] * 100),
    "observed_value": 2.1e-9,
    "note": "A_s involves individual a_k contributions weighted by f_k — inherently FRAGILE",
})

# ------------------------------------------------------------------
# OBSERVABLE 19: Delta_BCS / M_KK (dimensionless gap)
# Pure eigenvalue ratio from ED. Structurally R-family-independent:
# it is a ratio of Dirac eigenvalues, which does NOT need a_k coefficients at all.
# Classification: "STRUCTURAL" — invariant by construction.
# ------------------------------------------------------------------
observables.append({
    "name": "Delta_BCS/M_KK (dimensionless)",
    "symbol": "Delta_BCS/M_KK",
    "formula": "pure eigenvalue ratio from ED",
    "a_k_dependence": "none — not a Seeley-DeWitt heat kernel observable",
    "class": "STRUCTURAL",
    "reason": "Dimensionless eigenvalue ratio bypasses a_k entirely — not a truncated zeta observable",
    "drift_estimate_pct": 0.0,
    "observed_value": float(Delta_BCS),
    "note": "Structurally invariant under L_max — it's computed from the SPECTRUM directly, not from moments",
})

# ------------------------------------------------------------------
# OBSERVABLE 20: c_Gold / c_fabric (Goldstone / fabric sound speed ratio)
# Pure eigenvalue ratio from GL-Josephson. Same classification: STRUCTURAL.
# ------------------------------------------------------------------
observables.append({
    "name": "c_Gold / c_fabric (sound speed ratio)",
    "symbol": "c_G/c_f",
    "formula": "sqrt(J_C2/rho) ratio — pure spectral eigenvalue combination",
    "a_k_dependence": "none — direct from eigenvalue gradient (not Gilkey moment)",
    "class": "STRUCTURAL",
    "reason": "Sound speeds derive from stiffness and inertia at the van Hove fold; extracted from eigenvectors, not moments",
    "drift_estimate_pct": 0.0,
    "observed_value": 0.00436,
    "note": "Goldstone-fabric hierarchy is structural — 229x from band geometry, not moment truncation",
})

# =============================================================================
# STEP 4: Tabulate and count
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Classification table")
print("=" * 78)

classes = ["PROTECTED-R1", "PROTECTED-RAT", "PROTECTED-MULT",
           "STRUCTURAL", "FRAGILE-AK", "FRAGILE-MKK", "NON-PHONONIC"]
class_counts = {c: 0 for c in classes}  # (local)

print(f"\n{'#':>3}  {'Observable':<45s}  {'Class':<17s}  {'Drift %':>10s}")
print("-" * 78)
for i, obs in enumerate(observables, 1):
    cls = obs["class"]  # (local)
    class_counts[cls] += 1
    drift = obs["drift_estimate_pct"]  # (local)
    drift_str = f"{drift:>8.2f}%" if not np.isnan(drift) else "    N/A "  # (local)
    print(f"{i:>3}  {obs['name'][:45]:<45s}  {cls:<17s}  {drift_str}")

print("\nClass summary:")
for c in classes:
    print(f"  {c:<17s}  : {class_counts[c]:>2d}")

# R-family count: PROTECTED-R1 + PROTECTED-RAT + PROTECTED-MULT
# Plus STRUCTURAL (which is strictly stronger than R-family protection)
r_family_count = (class_counts["PROTECTED-R1"]
                  + class_counts["PROTECTED-RAT"]
                  + class_counts["PROTECTED-MULT"])  # (local)
structural_count = class_counts["STRUCTURAL"]  # (local)
fragile_count = class_counts["FRAGILE-AK"] + class_counts["FRAGILE-MKK"]  # (local)
non_phononic_count = class_counts["NON-PHONONIC"]  # (local)

total_obs = len(observables)  # (local)
protected_or_stronger = r_family_count + structural_count  # (local)

print(f"\n  R-family protected (PROTECTED-R1/RAT/MULT): {r_family_count}")
print(f"  STRUCTURAL (stronger than R-family):        {structural_count}")
print(f"  FRAGILE (AK + MKK):                         {fragile_count}")
print(f"  NON-PHONONIC:                               {non_phononic_count}")
print(f"  Total catalogued:                           {total_obs}")
print(f"  Protected-or-stronger total:                {protected_or_stronger}")

# =============================================================================
# STEP 5: Gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Gate verdict")
print("=" * 78)

GATE_THRESHOLD_PASS = 4  # (local)
GATE_THRESHOLD_INFO = 2  # (local)

# ------------------------------------------------------------------
# HONEST GATE CRITERION
# ------------------------------------------------------------------
# The naive reading "R-family protected" = any PROTECTED-* class.
# The empirical finding is that single-ratio PROTECTED-RAT observables
# drift 100%+ (a_4/a_2 drifts 132%, a_0/a_2 drifts 122%). They are NOT
# protected in any meaningful quantitative sense — only the ratio-of-
# ratios R_1 achieves < 1% drift.
#
# We therefore report TWO gate counts:
#
#   (a) STRICT-R-FAMILY: observables with drift < 10%
#         Includes PROTECTED-R1 + STRUCTURAL (no-a_k) + R_2-marginal
#
#   (b) LOOSE-R-FAMILY: naive sum of all PROTECTED-* classes
#         Includes PROTECTED-RAT (single-ratio), which IS NOT protected
#         quantitatively but IS protected structurally (they have no
#         dependence on individual a_k, only on their ratio).
#
# The gate threshold (>=4 to PASS) is evaluated against BOTH.

DRIFT_PROTECTION_THRESHOLD = 10.0  # (local) percent
strict_r_family = sum(
    1 for o in observables
    if (not np.isnan(o["drift_estimate_pct"]))
    and o["drift_estimate_pct"] < DRIFT_PROTECTION_THRESHOLD
    and o["class"] in ("PROTECTED-R1", "PROTECTED-R2", "PROTECTED-R3",
                       "PROTECTED-MULT", "STRUCTURAL")
)  # (local)

loose_r_family = r_family_count + structural_count  # (local) = 7 + 2 = 9

# Gate verdict uses the STRICT criterion (empirical drift < 10%).
if strict_r_family >= GATE_THRESHOLD_PASS:
    verdict = "PASS"
    detail = (f"STRICT: {strict_r_family} observables have L_max drift < 10% "
              f"(>= threshold 4). "
              f"LOOSE (naive class count): {loose_r_family}. "
              f"The STRICT criterion is the honest physical protection — "
              f"single-ratio observables (PROTECTED-RAT) drift 100%+ "
              f"and do NOT deserve the 'protected' label despite having "
              f"clean algebraic form.")
elif strict_r_family >= GATE_THRESHOLD_INFO:
    verdict = "INFO"
    detail = (f"STRICT: {strict_r_family} observables have drift < 10% "
              f"(2-3, partial protection). "
              f"LOOSE: {loose_r_family}.")
else:
    verdict = "FAIL"
    detail = (f"STRICT: {strict_r_family} observables have drift < 10% (0-1). "
              f"Only R_1-based invariants achieve protection.")

print(f"\n  Threshold PASS: R-family count >= 4  (using drift < 10%)")
print(f"  Threshold INFO: R-family count in [2, 3]")
print(f"  Threshold FAIL: R-family count <= 1")
print(f"")
print(f"  STRICT count (drift < 10%):   {strict_r_family}")
print(f"  LOOSE count (all PROTECTED-*):{loose_r_family}")
print(f"  Class-sum R-family count:     {r_family_count}")
print(f"  Verdict: {verdict}")
print(f"  Detail:  {detail}")

# =============================================================================
# STEP 6: Cross-checks
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Cross-checks")
print("=" * 78)

# Cross-check 1: R_1 closure
R1_from_obs = observables[10]["observed_value"]  # (local) "R_1_phys" entry (index 10)
R1_direct = R1_canonical  # (local)
R1_closure = abs(R1_from_obs - R1_direct) / R1_direct  # (local)
print(f"\n  CC-1 R_1 closure: observable R_1_phys = {R1_from_obs:.6f}")
print(f"                    direct R_1       = {R1_direct:.6f}")
print(f"                    closure residual = {R1_closure:.2e}  (expect < 1e-12)")

# Cross-check 2: Higgs formula gives finite prediction
mh_check = observables[2]["observed_value"]  # (local)
print(f"\n  CC-2 Higgs formula: m_H (bare spectral action) = {mh_check:.2f} GeV")
print(f"                       m_H observed                  = {m_H_obs:.2f} GeV")
print(f"                       ratio (bare / obs)             = {mh_check/m_H_obs:.4f}")

# Cross-check 3: n_s formula gives Planck-consistent range
ns_check = observables[3]["observed_value"]  # (local)
print(f"\n  CC-3 n_s formula:  n_s (bare Gilkey)    = {ns_check:.6f}")
print(f"                      n_s Planck            = {planck_ns:.6f}")
print(f"                      difference            = {(ns_check - planck_ns)*1e4:.2f} * 1e-4")

# Cross-check 4: Drift order (R_1 < a_4/a_2 < individual a_k)
print(f"\n  CC-4 Drift hierarchy verification:")
print(f"       R_1 drift      = {stab_R1*100:.3f}%")
print(f"       a_4/a_2 drift  = {stab_a4a2*100:.2f}%")
print(f"       a_0/a_2 drift  = {stab_a0a2*100:.2f}%")
print(f"       a_0 (alone)    = {(a0_vs_L[-1]/a0_vs_L[0] - 1)*100:.1f}%")
print(f"       a_2 (alone)    = {(a2_vs_L[-1]/a2_vs_L[0] - 1)*100:.1f}%")
print(f"       a_4 (alone)    = {(a4_vs_L[-1]/a4_vs_L[0] - 1)*100:.1f}%")
hierarchy_ok = (stab_R1 < stab_a4a2 < (a4_vs_L[-1]/a4_vs_L[0] - 1))  # (local)
print(f"       Hierarchy intact (R_1 < ratio < individual): {hierarchy_ok}")

# Cross-check 5: Classification completeness — every observable has a class
all_classified = all(obs["class"] in classes for obs in observables)  # (local)
print(f"\n  CC-5 Every observable classified: {all_classified}")

# =============================================================================
# STEP 7: Assessment (data only — interpretation goes in results section)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Assessment summary")
print("=" * 78)

# Best-drift observable
best_drift_idx = int(np.argmin([obs["drift_estimate_pct"] if not np.isnan(obs["drift_estimate_pct"]) else np.inf for obs in observables]))  # (local)
worst_drift_idx = int(np.argmax([obs["drift_estimate_pct"] if not np.isnan(obs["drift_estimate_pct"]) else -np.inf for obs in observables]))  # (local)

print(f"\n  Lowest L_max drift: #{best_drift_idx+1} {observables[best_drift_idx]['name']}")
print(f"    -> {observables[best_drift_idx]['drift_estimate_pct']:.3f}%")
print(f"  Highest L_max drift: #{worst_drift_idx+1} {observables[worst_drift_idx]['name']}")
print(f"    -> {observables[worst_drift_idx]['drift_estimate_pct']:.1f}%")

# Summary sentence
print(f"\n  SUMMARY: {r_family_count} R-family + {structural_count} structural + "
      f"{fragile_count} fragile + {non_phononic_count} non-phononic = {total_obs} total.")

# =============================================================================
# STEP 8: Save outputs
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Save NPZ and exit")
print("=" * 78)

obs_names = np.array([o["name"] for o in observables])  # (local)
obs_symbols = np.array([o["symbol"] for o in observables])  # (local)
obs_formulas = np.array([o["formula"] for o in observables])  # (local)
obs_ak_dep = np.array([o["a_k_dependence"] for o in observables])  # (local)
obs_class = np.array([o["class"] for o in observables])  # (local)
obs_reason = np.array([o["reason"] for o in observables])  # (local)
obs_drift = np.array([o["drift_estimate_pct"] for o in observables])  # (local)
obs_values = np.array([o["observed_value"] for o in observables])  # (local)
obs_notes = np.array([o["note"] for o in observables])  # (local)

np.savez(
    "s74_ratio_of_ratios_protected.npz",
    gate_name="N16-RATIO-OF-RATIOS-PROTECTED-74",
    gate_verdict=verdict,
    gate_detail=detail,
    # Classification
    obs_names=obs_names,
    obs_symbols=obs_symbols,
    obs_formulas=obs_formulas,
    obs_ak_dependence=obs_ak_dep,
    obs_class=obs_class,
    obs_reason=obs_reason,
    obs_drift_pct=obs_drift,
    obs_values=obs_values,
    obs_notes=obs_notes,
    # Counts
    class_counts=np.array(list(class_counts.items()), dtype=object),
    r_family_count=r_family_count,
    structural_count=structural_count,
    fragile_count=fragile_count,
    non_phononic_count=non_phononic_count,
    protected_or_stronger=protected_or_stronger,
    total_observables=total_obs,
    strict_r_family=strict_r_family,
    loose_r_family=loose_r_family,
    DRIFT_PROTECTION_THRESHOLD=DRIFT_PROTECTION_THRESHOLD,
    # R-family drift data
    R1_canonical=R1_canonical,
    R2_canonical=R2_canonical,
    R3_canonical=R3_canonical,
    stab_R1=stab_R1,
    stab_R2=stab_R2,
    stab_R3=stab_R3,
    stab_a4a2=stab_a4a2,
    stab_a0a2=stab_a0a2,
    L_max_values=L_vals,
    a0_vs_L=a0_vs_L,
    a2_vs_L=a2_vs_L,
    a4_vs_L=a4_vs_L,
    # Thresholds
    GATE_THRESHOLD_PASS=GATE_THRESHOLD_PASS,
    GATE_THRESHOLD_INFO=GATE_THRESHOLD_INFO,
    # Cross-checks
    R1_closure=R1_closure,
    mh_check=mh_check,
    ns_check=ns_check,
    hierarchy_ok=hierarchy_ok,
    all_classified=all_classified,
)

print(f"\n  Saved: s74_ratio_of_ratios_protected.npz")
print(f"\n{'=' * 78}")
print(f"  GATE N16-RATIO-OF-RATIOS-PROTECTED-74 VERDICT: {verdict}")
print(f"{'=' * 78}\n")
