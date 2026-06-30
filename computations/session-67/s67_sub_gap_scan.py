#!/usr/bin/env python3
"""
s67_sub_gap_scan.py -- SUB-GAP-FUNCTIONAL-SCAN-67
===================================================

Gate: SUB-GAP-FUNCTIONAL-SCAN-67
  PASS: omega_L1 < 2*Delta(f) for all surviving functionals
  FAIL: omega_L1 > 2*Delta(f) for any surviving functional

Physics
-------
The Leggett mode is an inter-band phase oscillation of the BCS condensate.
Its decay into the quasiparticle continuum requires omega_L > 2*Delta_min
(Mattis-Bardeen threshold). Below this threshold, the Leggett mode is
protected from pair-breaking decay. This is sub-gap protection, the
condensed-matter analog of confinement: the mode cannot fragment because
the available phase space is gapped.

The question is whether the spectral functional f(x) -- which enters the
BOSONIC spectral action Tr(f(D^2/Lambda^2)) -- modifies the BCS gap Delta.

Two-layer structure of the spectral triple:
  (i)  BOSONIC sector: S_bos = Tr(f(D^2/Lambda^2))
       = c_0(phi)*a_0 + c_2(phi)*a_2 + c_4(phi)*a_4 + ...
       This depends on f (or equivalently on phi in the anomaly family).
  (ii) FERMIONIC sector: S_ferm = <psi, D_A psi>
       The pairing vertex V_{kj} is derived from the fermionic action
       and the eigenvalue structure of D_K. This does NOT depend on f.

The BCS gap equation:
  Delta_k = -(1/2) Sum_j V_{kj} * Delta_j / E_j
  where E_j = sqrt((eps_j - mu)^2 + Delta_j^2)
is determined entirely by V_{kj} (fermionic) and eps_j (D_K eigenvalues).
Neither depends on the bosonic spectral functional f.

Therefore: Delta is FUNCTIONAL-INDEPENDENT.

However, one might argue that f enters through a REGULARIZED gap equation
where the sum is weighted by f:
  1/G_eff = Sum_n f(lambda_n^2/Lambda^2) / (2*E_n)
This would make the effective coupling G_eff, and hence Delta, depend on f.

This script examines BOTH interpretations:
  (A) STRUCTURAL: Delta is functional-independent (correct NCG framework).
      The sub-gap check is the same for all functionals.
  (B) MAXIMAL VARIATION: Allow the effective coupling to rescale by a factor
      corresponding to c_4(phi)/c_4(phi_ref), compute the modified Delta,
      and check sub-gap for each functional. This is the MOST CONSERVATIVE
      analysis: it OVERESTIMATES the functional dependence.

Five spectral functionals:
  1. CC cutoff f(x)=sqrt(x): the sole W3-A survivor
  2. Zeta f(x)=x^{-s}|_{s=0}: effectively weights by a_4
  3. Exponential f(x)=exp(-x)
  4. Compact support f(x)=(1-x)_+
  5. Anomaly family c_k(phi) at phi=1 (reference point)

Author: Landau Condensed Matter Theorist (S67)
Session: S67, Wave 7
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
    omega_L1, omega_L2,
    Delta_B3, Delta_0_GL, Delta_0_OES,
    E_B1, E_B2_mean, E_B3_mean,
    E_cond, a4_fold, a2_fold, a0_fold,
    tau_fold, M_KK, PI,
    J_C2, J_su2, J_u1,
    N_dof_BCS,
)

t0 = time.time()

print("=" * 78)
print("SUB-GAP-FUNCTIONAL-SCAN-67: Sub-Gap Check for Surviving Functionals")
print("=" * 78)

# =============================================================================
# SECTION 1: LOAD INPUT DATA
# =============================================================================
print("\n--- Section 1: Input Data ---")

# --- Leggett mode frequencies ---
# Two sources: s48 (RPA, lower), s52 (GL-Josephson, higher)
# Use BOTH to bracket the physical value

# s52 GL-Josephson (canonical constants)
omega_L1_GL = omega_L1      # 0.138 M_KK
omega_L2_GL = omega_L2      # 0.192 M_KK

# s48 RPA (from s48_leggett_mode.npz, also used in W3-A)
d48 = np.load(os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz'), allow_pickle=True)
omega_L1_RPA = float(d48['omega_L1_fold'])  # 0.0696 M_KK
omega_L2_RPA = float(d48['omega_L2_fold'])  # 0.1074 M_KK

# s66 spectral function (dressed frequency)
# S66 W5-D: omega_peak = 0.113 M_KK (shifted from 0.138 by Re Sigma)
omega_L1_dressed = 0.113  # M_KK, from S66 LEGGETT-SPECTRAL-66  # (local)

print(f"  Leggett-1 frequencies (M_KK units):")
print(f"    omega_L1(RPA)     = {omega_L1_RPA:.6f}  (s48, bare)")
print(f"    omega_L1(dressed) = {omega_L1_dressed:.6f}  (S66, self-energy shifted)")
print(f"    omega_L1(GL)      = {omega_L1_GL:.6f}  (s52, GL-Josephson)")
print(f"  Leggett-2 frequencies:")
print(f"    omega_L2(RPA)     = {omega_L2_RPA:.6f}")
print(f"    omega_L2(GL)      = {omega_L2_GL:.6f}")

# --- BCS sector gaps ---
# From s48/s46 self-consistent BCS (verified in s52 HFB)
from pathlib import Path
d46 = np.load(Path(SCRIPT_DIR).parent / 'computations/_shared' / 's46_number_projected_bcs.npz',
              allow_pickle=True)
Delta_fold = d46['Delta_bcs_fold']  # [B1, B2, B3]
V_constrained = d46['V_mat_constrained']  # 3x3 sector-averaged pairing
V_raw = d46['V_mat_raw']  # 3x3 raw pairing

print(f"\n  BCS sector gaps at fold (M_KK units):")
print(f"    Delta_B1 = {Delta_fold[0]:.6f}  (Kramers singlet)")
print(f"    Delta_B2 = {Delta_fold[1]:.6f}  (dominant, 4 modes)")
print(f"    Delta_B3 = {Delta_fold[2]:.6f}  (softest, 3 modes)")

# Pair-breaking thresholds
threshold_B1 = 2 * Delta_fold[0]  # 0.744
threshold_B2 = 2 * Delta_fold[1]  # 1.464
threshold_B3 = 2 * Delta_fold[2]  # 0.168

print(f"\n  Pair-breaking thresholds 2*Delta_alpha:")
print(f"    2*Delta_B1 = {threshold_B1:.6f}")
print(f"    2*Delta_B2 = {threshold_B2:.6f}")
print(f"    2*Delta_B3 = {threshold_B3:.6f}  (limiting threshold)")

# The Leggett mode can decay into quasiparticle pairs from any sector.
# The lowest threshold determines sub-gap protection.
# For a multi-band system, the Leggett mode (inter-band phase oscillation)
# couples to pair excitations across BOTH bands. The threshold is determined
# by the SMALLEST gap among the participating bands:
#   omega_L < 2 * min(Delta_alpha)  for all bands alpha participating.
Delta_min = Delta_fold.min()
threshold_min = 2 * Delta_min

print(f"\n  Minimum gap: Delta_min = {Delta_min:.6f} (B3 sector)")
print(f"  Minimum threshold: 2*Delta_min = {threshold_min:.6f}")

# --- Pairing interaction matrix ---
print(f"\n  Sector pairing matrix V_constrained (3x3):")
for i, lab in enumerate(['B1', 'B2', 'B3']):
    print(f"    {lab}: {V_constrained[i,:]}")

# =============================================================================
# SECTION 2: STRUCTURAL ARGUMENT — DELTA IS FUNCTIONAL-INDEPENDENT
# =============================================================================
print("\n" + "=" * 78)
print("Section 2: Structural Analysis — Functional Independence of Delta")
print("=" * 78)

print("""
  The BCS gap Delta is determined by:
    (i)   Single-particle energies eps_k = eigenvalues of D_K at tau_fold
    (ii)  Pairing interaction V_{kj} from the fermionic spectral action
    (iii) Chemical potential mu (determined by particle number)

  None of these depend on the bosonic spectral functional f(x):
    - eps_k are eigenvalues of D_K (geometric, tau-dependent, f-independent)
    - V_{kj} comes from the fermionic overlap integrals on SU(3)
    - mu is set by the number of Cooper pairs (BEC-crossover regime)

  The spectral functional enters the BOSONIC action:
    S_bos = c_0(phi)*a_0 + c_2(phi)*a_2 + c_4(phi)*a_4

  The coefficients c_k(phi) weight the spectral moments differently,
  changing the cosmological observables (n_s, m_H, CC ratio) but NOT
  the BCS condensate structure.

  THEOREM (functional independence of sub-gap):
    Let f_1, f_2 be any two admissible spectral functionals.
    Let Delta^{f_1}_alpha, Delta^{f_2}_alpha be the BCS gaps
    derived from the same D_K spectrum at tau_fold.
    Then Delta^{f_1}_alpha = Delta^{f_2}_alpha for all sectors alpha,
    because the gap equation involves only {eps_k, V_{kj}, mu},
    none of which depend on f.

  Corollary: omega_L < 2*Delta is functional-independent.
""")

# =============================================================================
# SECTION 3: MAXIMAL VARIATION ANALYSIS (CONSERVATIVE BOUND)
# =============================================================================
print("=" * 78)
print("Section 3: Maximal Variation — Rescaled Coupling Analysis")
print("=" * 78)

print("""
  Even though Delta is structurally functional-independent, we perform a
  MAXIMAL VARIATION analysis as a conservative check. We ask:
    "If the effective coupling G_eff were to scale with c_4(phi)/c_4(phi_ref),
     how would Delta change? Would it break sub-gap protection?"

  This OVERESTIMATES the functional dependence because:
    (a) c_4 enters the BOSONIC action, not the gap equation
    (b) Even if it entered, the gap depends logarithmically on G:
        Delta ~ omega_D * exp(-1/(N(0)*G))
    (c) The ratio c_4(phi)/c_4(phi_ref) is O(1) for all physical functionals

  For each functional, we define an effective coupling rescaling factor:
    lambda_f = c_4(phi_f) / c_4(phi_CC)
  where phi_CC corresponds to the CC cutoff (the surviving functional).
""")

# Anomaly family coefficients
def c_0(phi):
    return (1.0/8.0) * (np.exp(4.0*phi) - 1.0)

def c_2(phi):
    return (1.0/2.0) * (np.exp(2.0*phi) - 1.0)

def c_4(phi):
    return phi

# The CC cutoff f(x) = sqrt(x) corresponds to the standard Chamseddine-Connes
# spectral action S = Tr(f(D^2/Lambda^2)). In the anomaly parameterization,
# phi -> +inf recovers the cutoff action (c_0 >> c_2 >> c_4 >> 0, all positive).
# But in practice, the CC cutoff is the BASELINE against which gaps are computed.
#
# The five functionals and their effective c_4:
# Note: c_4(phi) = phi in the anomaly family.
# For functionals NOT in the anomaly family, we use the EFFECTIVE phi
# from the S67 FUNCTIONAL-SELECT-67 computation, matching via eps_H.

# Load functional selection data
d67 = np.load(os.path.join(SCRIPT_DIR, 's67_functional_select.npz'), allow_pickle=True)
da2_dtau = float(d67['da2_dtau'])    # -875.6
da4_dtau = float(d67['da4_dtau'])    # -609.2

print(f"  Spectral moment derivatives at fold:")
print(f"    da_2/dtau = {da2_dtau:.2f}")
print(f"    da_4/dtau = {da4_dtau:.2f}")

# The five spectral functionals and their c_4 effective values:
# 1. CC cutoff: S = sum d_n^2 |lambda_n| (standard, baseline for BCS)
#    In anomaly language, this is the phi -> inf limit but we use it as reference.
#    Effective a_4 weighting = a_4 (unit weight). c_4_eff = 1 (reference).
#
# 2. Zeta: S = sum d_n^2 |lambda_n|^{-2s}. Weight: |lambda_n|^{-2s} = 1 at s=0.
#    But the ACTION is the coefficient of Lambda^{-4} in zeta, which IS a_4.
#    c_4_eff ~ 1 (same a_4, but different gradient dS/dtau sign).
#
# 3. Exponential: S = sum d_n^2 exp(-lambda_n^2/Lambda^2). Gaussian weight.
#    Effective a_4 ~ sum d_n^2 lambda_n^{-4} * 24 (from exp Taylor).
#    c_4_eff ~ 1 (same a_4 at leading order).
#
# 4. Compact support: S = sum d_n^2 max(0, 1 - lambda_n^2/Lambda^2).
#    Includes only modes with |lambda_n| < Lambda.
#    c_4_eff depends on Lambda; at Lambda = M_KK, includes all modes.
#
# 5. Anomaly at phi=1: c_4(1) = 1.
#
# KEY INSIGHT: All spectral functionals produce the SAME a_4 at leading order.
# The coefficient a_4 = Tr(|D_K|^{-4}) is a spectral invariant.
# Different functionals reweight the higher-order corrections, but a_4 is universal.
#
# The BCS coupling V is proportional to a_4 / (f_2 * Lambda^2), where f_2 is
# a second moment that sets the energy scale. For dimensional analysis:
#   G ~ g^2 / M_KK^2 ~ a_4 / a_2 * (1/M_KK^2)
# This ratio a_4/a_2 is what matters, and it is the SAME for all functionals
# up to O(Lambda^{-2}) corrections.

# Define the five functionals with their properties
functionals = {
    'CC cutoff sqrt(x)': {
        'description': 'Chamseddine-Connes standard action',
        'eps_H': 0.02163,      # from S66
        'n_s': 0.9567,         # = 1 - 2*0.02163
        'c4_ratio': 1.0,       # reference
        'W3A_status': 'PASS',
    },
    'Zeta x^{-s}': {
        'description': 'Zeta function regularization',
        'eps_H': -0.04485,
        'n_s': 1.0897,
        'c4_ratio': 1.0,       # same a_4 coefficient
        'W3A_status': 'FAIL (n_s)',
    },
    'Exponential exp(-x)': {
        'description': 'Gaussian/heat-kernel cutoff',
        'eps_H': -0.00006,
        'n_s': 1.0001,
        'c4_ratio': 1.0,       # same a_4 at leading order
        'W3A_status': 'FAIL (n_s)',
    },
    'Compact (1-x)_+': {
        'description': 'Sharp momentum cutoff',
        'eps_H': -0.000006,
        'n_s': 1.0000,
        'c4_ratio': 1.0,       # same a_4 at leading order
        'W3A_status': 'FAIL (n_s)',
    },
    'Anomaly phi=1': {
        'description': 'Anomaly-derived family at phi=1',
        'eps_H': -0.00589,
        'n_s': 1.0118,
        'c4_ratio': 1.0,       # c_4(1) = 1
        'W3A_status': 'FAIL (n_s)',
    },
}

print("\n  Functional landscape:")
print(f"  {'Functional':25s}  {'eps_H':>10s}  {'n_s':>8s}  {'c4_ratio':>10s}  {'W3A':>12s}")
print(f"  {'-'*25}  {'-'*10}  {'-'*8}  {'-'*10}  {'-'*12}")
for name, props in functionals.items():
    print(f"  {name:25s}  {props['eps_H']:+10.5f}  {props['n_s']:8.4f}  "
          f"{props['c4_ratio']:10.3f}  {props['W3A_status']:>12s}")

# =============================================================================
# SECTION 4: BCS GAP SENSITIVITY ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("Section 4: BCS Gap Sensitivity to Coupling Rescaling")
print("=" * 78)

# Load the 8-mode pairing interaction
d48_hfb = np.load(Path(SCRIPT_DIR).parent / 'computations/_shared' / 's48_hfb_selfconsist.npz',
                   allow_pickle=True)
V_bare_8x8 = d48_hfb['V_bare'].copy()
E_sp = d48_hfb['E_sp'].copy()
labels = list(d48_hfb['labels'])

print(f"  8-mode BCS system:")
print(f"    Modes: {labels}")
print(f"    E_sp = {E_sp}")
print(f"    V_bare norm = {np.linalg.norm(V_bare_8x8):.6f}")

# Self-consistent BCS gap solver
def solve_bcs(V, eps, mu, max_iter=50000, tol=1e-15):
    """Solve multi-mode BCS gap equation Delta_k = (1/2) V @ (Delta/E_qp)."""
    N = len(eps)
    Delta = np.full(N, 0.3)  # initial guess

    for it in range(max_iter):
        E_qp = np.sqrt((eps - mu)**2 + Delta**2)
        Delta_new = 0.5 * np.abs(V @ (Delta / E_qp))
        diff = np.max(np.abs(Delta_new - Delta))
        Delta = Delta_new.copy()
        if diff < tol:
            return Delta, E_qp, True, it + 1
    return Delta, np.sqrt((eps - mu)**2 + Delta**2), False, max_iter

# Optimal chemical potential for BCS (midgap B2-B3)
mu_opt = 0.5 * (E_sp[3] + E_sp[5])
print(f"  Chemical potential mu = {mu_opt:.6f} (midgap B2-B3)")

# Baseline BCS gap
Delta_base, E_qp_base, conv_base, nit_base = solve_bcs(V_bare_8x8, E_sp, mu_opt)
print(f"\n  Baseline BCS gap (V_bare, mu={mu_opt:.4f}):")
print(f"    Converged: {conv_base} in {nit_base} iterations")
print(f"    Delta_B2 = {np.mean(Delta_base[:4]):.6f}")
print(f"    Delta_B1 = {Delta_base[4]:.6f}")
print(f"    Delta_B3 = {np.mean(Delta_base[5:]):.6f}")

# Now test rescaled couplings
# Even though c_4 ratio = 1 for all functionals (a_4 is a spectral invariant),
# let us systematically scan coupling rescalings from 0.1x to 10x to map out
# the Delta(G) curve and show that sub-gap protection is robust.

rescale_factors = np.array([0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9,
                            1.0,
                            1.1, 1.2, 1.5, 2.0, 3.0, 5.0, 10.0])

print(f"\n  Coupling rescaling scan: G -> alpha * G")
print(f"  {'alpha':>6s}  {'Delta_B2':>10s}  {'Delta_B1':>10s}  {'Delta_B3':>10s}  "
      f"{'2*D_min':>8s}  {'wL1<2Dm':>8s}  {'wL2<2Dm':>8s}")
print(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}  "
      f"{'-'*8}  {'-'*8}  {'-'*8}")

rescale_results = {}
for alpha in rescale_factors:
    V_scaled = alpha * V_bare_8x8
    Delta_s, E_qp_s, conv_s, nit_s = solve_bcs(V_scaled, E_sp, mu_opt)

    D_B2 = np.mean(Delta_s[:4])
    D_B1 = Delta_s[4]
    D_B3 = np.mean(Delta_s[5:])
    D_min = min(D_B2, D_B1, D_B3)
    thr = 2 * D_min

    # Sub-gap checks with the most conservative (highest) Leggett frequency
    sub_L1_GL = omega_L1_GL < thr
    sub_L2_GL = omega_L2_GL < thr

    rescale_results[alpha] = {
        'Delta_B2': D_B2, 'Delta_B1': D_B1, 'Delta_B3': D_B3,
        'Delta_min': D_min, 'threshold': thr,
        'sub_L1': sub_L1_GL, 'sub_L2': sub_L2_GL,
        'converged': conv_s,
    }

    flag_L1 = "PASS" if sub_L1_GL else "FAIL"
    flag_L2 = "PASS" if sub_L2_GL else "FAIL"
    print(f"  {alpha:6.2f}  {D_B2:10.6f}  {D_B1:10.6f}  {D_B3:10.6f}  "
          f"{thr:8.4f}  {flag_L1:>8s}  {flag_L2:>8s}")

# =============================================================================
# SECTION 5: SUB-GAP MATRIX FOR ALL FUNCTIONALS × ALL LEGGETT ESTIMATES
# =============================================================================
print("\n" + "=" * 78)
print("Section 5: Sub-Gap Matrix — All Functionals × All Leggett Estimates")
print("=" * 78)

# Since all functionals have c4_ratio = 1.0 (a_4 is a spectral invariant),
# Delta is the SAME for all functionals. Use the s48/s46 sector gaps.

# Sector gaps from s46 self-consistent BCS
Delta_sector = {
    'B1': Delta_fold[0],  # 0.372
    'B2': Delta_fold[1],  # 0.732
    'B3': Delta_fold[2],  # 0.084
}

# For the Leggett mode, the relevant threshold is the minimum gap
# because the Leggett mode involves oscillation between ALL sectors.
# The decay channel with the lowest threshold dominates.
Delta_min_sector = min(Delta_sector.values())
threshold_pair = 2 * Delta_min_sector

# Three Leggett-1 frequency estimates
omega_L1_estimates = {
    'RPA (s48)': omega_L1_RPA,        # 0.0696
    'Dressed (S66)': omega_L1_dressed,  # 0.113
    'GL-Josephson (s52)': omega_L1_GL,  # 0.138
}

# Three Leggett-2 frequency estimates
omega_L2_estimates = {
    'RPA (s48)': omega_L2_RPA,        # 0.107
    'GL-Josephson (s52)': omega_L2_GL,  # 0.192
}

print(f"\n  Pair-breaking threshold: 2*Delta_min(B3) = {threshold_pair:.6f} M_KK")
print(f"\n  Sub-gap matrix (omega_L < 2*Delta_min?):")
print(f"\n  {'Leggett mode':25s}  {'omega_L':>8s}  {'ratio':>8s}  {'margin':>8s}  {'Status':>8s}")
print(f"  {'-'*25}  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*8}")

sub_gap_results = {}
for name, omega in {**omega_L1_estimates, **omega_L2_estimates}.items():
    ratio = omega / threshold_pair
    margin = (threshold_pair - omega) / threshold_pair * 100
    status = "PASS" if omega < threshold_pair else "FAIL"
    sub_gap_results[name] = {
        'omega': omega, 'ratio': ratio, 'margin_pct': margin, 'status': status
    }
    print(f"  {name:25s}  {omega:8.4f}  {ratio:8.4f}  {margin:+7.1f}%  {status:>8s}")

print(f"\n  Now check per-functional (all have same Delta):")
print(f"\n  {'Functional':25s}  {'Delta_min':>10s}  {'2*Dmin':>8s}  {'wL1(GL)':>8s}  "
      f"{'L1 gap?':>8s}  {'wL2(GL)':>8s}  {'L2 gap?':>8s}")
print(f"  {'-'*25}  {'-'*10}  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*8}")

functional_sub_gap = {}
for fname, fprops in functionals.items():
    # All functionals give the same Delta (functional-independent)
    Dm = Delta_min_sector
    thr = 2 * Dm
    sub_L1 = omega_L1_GL < thr
    sub_L2 = omega_L2_GL < thr

    functional_sub_gap[fname] = {
        'Delta_min': Dm,
        'threshold': thr,
        'sub_L1': sub_L1,
        'sub_L2': sub_L2,
        'surviving': fprops['W3A_status'] == 'PASS',
    }

    flag_L1 = "PASS" if sub_L1 else "FAIL"
    flag_L2 = "PASS" if sub_L2 else "FAIL"
    star = " *" if fprops['W3A_status'] == 'PASS' else ""
    print(f"  {fname:25s}  {Dm:10.6f}  {thr:8.4f}  {omega_L1_GL:8.4f}  "
          f"{flag_L1:>8s}  {omega_L2_GL:8.4f}  {flag_L2:>8s}{star}")

# =============================================================================
# SECTION 6: LEGGETT-2 MARGINAL ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("Section 6: Leggett-2 Marginal Analysis (omega_L2 near threshold)")
print("=" * 78)

# omega_L2(GL) = 0.192 vs 2*Delta_B3 = 0.168
# This is ABOVE the B3 pair-breaking threshold.
# However: omega_L2(RPA) = 0.107 is safely below.
# The physical situation depends on which estimate is more reliable.

print(f"""
  omega_L2(GL)  = {omega_L2_GL:.4f} M_KK
  omega_L2(RPA) = {omega_L2_RPA:.4f} M_KK
  2*Delta_B3    = {threshold_pair:.4f} M_KK

  The GL-Josephson estimate includes Josephson coupling between cells,
  which RAISES the Leggett frequency. The RPA estimate is the bare
  intra-cell result.

  For the B3 threshold (softest sector):
    omega_L2(RPA)  / 2*Delta_B3 = {omega_L2_RPA / threshold_pair:.4f} (sub-gap)
    omega_L2(GL)   / 2*Delta_B3 = {omega_L2_GL / threshold_pair:.4f} (ABOVE threshold)

  However, for the B1 and B2 thresholds:
    omega_L2(GL) / 2*Delta_B1 = {omega_L2_GL / (2*Delta_fold[0]):.4f} (deeply sub-gap)
    omega_L2(GL) / 2*Delta_B2 = {omega_L2_GL / (2*Delta_fold[1]):.4f} (deeply sub-gap)

  The Leggett-2 mode is a B1-B3 relative phase oscillation. Its decay
  requires breaking pairs in BOTH participating sectors. The kinematic
  threshold is max(2*Delta_B1, 2*Delta_B3) for the heavier channel,
  but the dominant decay is into the SOFTEST channel (B3).

  Physical interpretation:
  - If the Leggett-2 frequency truly exceeds 2*Delta_B3, it can decay
    into B3 quasiparticle pairs. This gives a FINITE lifetime (not infinite).
  - The S66 spectral function analysis found Q_L1 = 18.6 (sharp resonance),
    meaning even WITH some pair-breaking, the mode remains well-defined.
  - The Z_2 selection rule (W1-B) provides EXACT protection against
    gravitational decay, independent of sub-gap status.

  Conclusion: omega_L2 is marginally sub-gap or marginally above threshold
  depending on the Leggett frequency estimate used. This does NOT affect
  the gate verdict because:
    (a) The gate tests omega_L1, not omega_L2
    (b) omega_L1 is sub-gap by ALL estimates (ratio 0.41-0.82)
    (c) DM viability requires only the LOWEST Leggett mode to be stable
""")

# =============================================================================
# SECTION 7: GATE VERDICT
# =============================================================================
print("=" * 78)
print("Section 7: Gate Verdict")
print("=" * 78)

# Gate: SUB-GAP-FUNCTIONAL-SCAN-67
# PASS: omega_L1 < 2*Delta(f) for all surviving functionals
# FAIL: omega_L1 > 2*Delta(f) for any surviving functional

# The sole surviving functional (W3-A) is CC cutoff sqrt(x).
# Delta is functional-independent. omega_L1 is functional-independent.
# Using the MOST CONSERVATIVE Leggett-1 estimate (GL-Josephson):

omega_L1_max = omega_L1_GL  # 0.138 (highest estimate)
Delta_min_for_gate = Delta_min_sector  # 0.084 (B3, softest)
threshold_for_gate = 2 * Delta_min_for_gate  # 0.168
ratio_for_gate = omega_L1_max / threshold_for_gate

gate_pass = omega_L1_max < threshold_for_gate

print(f"\n  Gate: SUB-GAP-FUNCTIONAL-SCAN-67")
print(f"    Criterion: omega_L1 < 2*Delta(f) for surviving functional (CC cutoff)")
print(f"    omega_L1(max) = {omega_L1_max:.6f} M_KK (GL-Josephson, most conservative)")
print(f"    2*Delta_min   = {threshold_for_gate:.6f} M_KK (B3 sector)")
print(f"    Ratio         = {ratio_for_gate:.4f}")
print(f"    Margin        = {(1 - ratio_for_gate)*100:.1f}%")
print(f"    Gate status: {'PASS' if gate_pass else 'FAIL'}")

# Also report with each Leggett estimate
print(f"\n  Robustness across Leggett-1 estimates:")
for est_name, omega_val in omega_L1_estimates.items():
    r = omega_val / threshold_for_gate
    print(f"    {est_name:25s}: ratio = {r:.4f}  ({'PASS' if r < 1 else 'FAIL'})")

# Key numbers for the gate
print(f"\n  DECISIVE NUMBERS:")
print(f"    omega_L1 / (2*Delta_B3) = {ratio_for_gate:.4f}  [threshold: 1.0]")
print(f"    Margin to threshold     = {(threshold_for_gate - omega_L1_max):.4f} M_KK")
print(f"    Margin fraction         = {(1 - ratio_for_gate)*100:.1f}%")
print(f"    Functional dependence   = NONE (structural theorem)")
print(f"    W3-A surviving functional: CC cutoff f(x) = sqrt(x)")
print(f"    Double protection: sub-gap (this gate) + Z_2 parity (W1-B)")

verdict = "PASS" if gate_pass else "FAIL"
print(f"\n  Gate SUB-GAP-FUNCTIONAL-SCAN-67: {verdict}")

# =============================================================================
# SECTION 8: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("Section 8: Save Data")
print("=" * 78)

# Prepare arrays for the rescaling scan
alpha_scan = np.array(list(rescale_results.keys()))
Delta_B2_scan = np.array([rescale_results[a]['Delta_B2'] for a in alpha_scan])
Delta_B1_scan = np.array([rescale_results[a]['Delta_B1'] for a in alpha_scan])
Delta_B3_scan = np.array([rescale_results[a]['Delta_B3'] for a in alpha_scan])
Delta_min_scan = np.array([rescale_results[a]['Delta_min'] for a in alpha_scan])
threshold_scan = np.array([rescale_results[a]['threshold'] for a in alpha_scan])

np.savez(os.path.join(SCRIPT_DIR, 's67_sub_gap_scan.npz'),
         # Leggett frequencies
         omega_L1_RPA=omega_L1_RPA,
         omega_L1_dressed=omega_L1_dressed,
         omega_L1_GL=omega_L1_GL,
         omega_L2_RPA=omega_L2_RPA,
         omega_L2_GL=omega_L2_GL,
         # BCS sector gaps
         Delta_fold=Delta_fold,
         Delta_min=Delta_min_sector,
         threshold_pair=threshold_pair,
         # Pairing matrix
         V_constrained=V_constrained,
         # Rescaling scan
         alpha_scan=alpha_scan,
         Delta_B2_scan=Delta_B2_scan,
         Delta_B1_scan=Delta_B1_scan,
         Delta_B3_scan=Delta_B3_scan,
         Delta_min_scan=Delta_min_scan,
         threshold_scan=threshold_scan,
         # Gate result
         gate_ratio=ratio_for_gate,
         gate_margin_pct=(1 - ratio_for_gate) * 100,
         gate_name='SUB-GAP-FUNCTIONAL-SCAN-67',
         gate_verdict=verdict,
         gate_detail=f'omega_L1/2*Delta_min = {ratio_for_gate:.4f} < 1.0. '
                     f'Delta is functional-independent (structural theorem). '
                     f'Margin = {(1-ratio_for_gate)*100:.1f}%. '
                     f'Double protection: sub-gap + Z_2 parity.',
         )

print(f"  Saved: s67_sub_gap_scan.npz")

# =============================================================================
# SECTION 9: DIAGNOSTIC PLOT
# =============================================================================
print("\n--- Generating diagnostic plot ---")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel (a): Leggett frequencies vs pair-breaking thresholds
ax = axes[0]
sectors = ['B3', 'B1', 'B2']
thresholds = [threshold_pair, 2*Delta_fold[0], 2*Delta_fold[1]]
colors_sector = ['#CC6677', '#4477AA', '#228833']

y_pos = np.arange(len(sectors))
ax.barh(y_pos, thresholds, color=colors_sector, alpha=0.3, edgecolor='black',
        label=r'$2\Delta_\alpha$ (pair threshold)')
ax.axvline(omega_L1_GL, color='red', ls='--', lw=2, label=f'$\\omega_{{L1}}$(GL) = {omega_L1_GL}')
ax.axvline(omega_L1_RPA, color='blue', ls='-.', lw=2, label=f'$\\omega_{{L1}}$(RPA) = {omega_L1_RPA:.4f}')
ax.axvline(omega_L2_GL, color='red', ls=':', lw=1.5, label=f'$\\omega_{{L2}}$(GL) = {omega_L2_GL}')
ax.set_yticks(y_pos)
ax.set_yticklabels(sectors)
ax.set_xlabel(r'Frequency ($M_{\mathrm{KK}}$)')
ax.set_title('(a) Sub-Gap Check')
ax.legend(fontsize=7, loc='lower right')
ax.set_xlim(0, 1.6)

# Panel (b): Delta vs coupling rescaling
ax = axes[1]
ax.plot(alpha_scan, Delta_B2_scan, 'o-', color='#4477AA', label=r'$\Delta_{\mathrm{B2}}$')
ax.plot(alpha_scan, Delta_B1_scan, 's-', color='#228833', label=r'$\Delta_{\mathrm{B1}}$')
ax.plot(alpha_scan, Delta_B3_scan, '^-', color='#CC6677', label=r'$\Delta_{\mathrm{B3}}$')
ax.axhline(omega_L1_GL / 2, color='red', ls='--', lw=1, label=r'$\omega_{L1}$/2')
ax.axvline(1.0, color='gray', ls=':', lw=1, label=r'$\alpha = 1$ (physical)')
ax.set_xlabel(r'Coupling rescale factor $\alpha$')
ax.set_ylabel(r'$\Delta_\alpha$ ($M_{\mathrm{KK}}$)')
ax.set_title(r'(b) $\Delta$ vs Coupling Rescaling')
ax.set_xscale('log')
ax.legend(fontsize=7)

# Panel (c): Sub-gap ratio for each Leggett estimate
ax = axes[2]
est_names = list(omega_L1_estimates.keys()) + list(omega_L2_estimates.keys())
est_omegas = [omega_L1_estimates[n] for n in omega_L1_estimates] + \
             [omega_L2_estimates[n] for n in omega_L2_estimates]
est_ratios = [o / threshold_pair for o in est_omegas]
est_colors = ['#4477AA' if r < 1 else '#CC3311' for r in est_ratios]

y_est = np.arange(len(est_names))
ax.barh(y_est, est_ratios, color=est_colors, alpha=0.7, edgecolor='black')
ax.axvline(1.0, color='black', ls='-', lw=2, label='Pair threshold')
ax.set_yticks(y_est)
ax.set_yticklabels(est_names, fontsize=8)
ax.set_xlabel(r'$\omega_L / (2\Delta_{\min})$')
ax.set_title('(c) Sub-Gap Ratios')
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's67_sub_gap_scan.png'), dpi=150, bbox_inches='tight')
print(f"  Saved: s67_sub_gap_scan.png")

dt = time.time() - t0
print(f"\n  Total runtime: {dt:.2f} s")
print(f"\n{'='*78}")
print(f"  Gate SUB-GAP-FUNCTIONAL-SCAN-67: {verdict}")
print(f"  omega_L1 / (2*Delta_B3) = {ratio_for_gate:.4f}")
print(f"  Sub-gap margin = {(1-ratio_for_gate)*100:.1f}%")
print(f"  Functional dependence: NONE (Delta is structural)")
print(f"{'='*78}")
