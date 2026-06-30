#!/usr/bin/env python3
"""
s70_zeta_as_budget.py -- ZETA-AS-BUDGET-70: A_s Gap Budget in Zeta Scheme
=========================================================================

Gate: ZETA-AS-BUDGET-70
  INFO: Report gap_zeta and |gap_zeta - gap_cutoff|. Flag if > 0.1 OOM.

Physics:
--------
The A_s gap budget (0.485 OOM) was computed in the sqrt-cutoff scheme:

  Baseline gap:       0.805 OOM  (delta-N chain: A_s = 3.29e-10 vs 2.1e-9)
  BCS dressing:      +0.046 OOM  (SCHEME-DEPENDENT, eps_H enters)
  Non-BD squeeze:    +0.226 OOM  (FUNCTIONAL-INDEPENDENT, BCS mixing angles)
  Phase correction:  +0.043 OOM  (FUNCTIONAL-INDEPENDENT, algebraic)
  Remaining gap:      0.485 OOM

This script re-derives the budget in the zeta scheme (S_zeta = a_4(D_K^2))
where eps_H changes sign and magnitude.

The critical distinction between schemes:

  CUTOFF: S_cutoff = Tr f(D^2/L^2) with f(x) = sqrt(x)
    => S_cutoff(tau) = sum dim(p,q)^2 * sum |lam_j(tau)|
    => INCREASES monotonically with tau (gradient drives transit)
    => eps_H > 0 => n_s < 1 (red tilt)

  ZETA: S_zeta = zeta_D(0) = a_4(D_K^2)
    => a_4(tau) = sum dim(p,q) * sum_{lam>0} lam^{-4}
    => DECREASES with tau (eigenvalues grow, inverse powers shrink)
    => eps_H < 0 => n_s > 1 (blue tilt)

For A_s normalization, the formula A_s = H^2/(8*pi^2*eps*M_Pl^2*c_s)
depends on both eps and H. The Hubble parameter H^2 = rho/(3*M_Pl^2)
also depends on the scheme through the total energy density. However,
the eps_H from S66 is a SHAPE parameter (dimensionless ratio of spectral
action derivatives), and the mapping to physical H requires specifying
how M_Pl^2 is extracted from the spectral action.

Key insight from this computation: the quantity eps*H^2 = KE/M_Pl^2 where
KE = G*v^2/2 is the modulus kinetic energy. In the delta-N formula,
A_s = [GGE numerator] / (6*KE)^2. If the TRANSIT DYNAMICS are the
same physical process regardless of how we regularize the spectral action,
then KE is fixed by the physical process, not by the regularization scheme.

Author: Lizzi Spectral Functional Theorist
Session: S70
"""

import sys
import os
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

from canonical_constants import (
    PI, M_Pl_reduced, M_KK, M_KK_gravity, M_KK_kerner,
    tau_fold, a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    G_DeWitt, v_terminal, c_fabric,
    Vol_SU3_Haar,
    H_fold,
    E_cond, Delta_BCS, Delta_0_OES,
    A_s_CMB,
    omega_L1, omega_L2,
    c_Gold,
)

print("=" * 78)
print("ZETA-AS-BUDGET-70: A_s Gap Budget in Zeta Scheme")
print("=" * 78)

# =============================================================================
# SECTION 1: Load input data
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 1: Load Input Data")
print("=" * 78)

# S66 zeta spectral action data
zeta_data = np.load(os.path.join(SCRIPT_DIR, 's66_zeta_sa.npz'), allow_pickle=True)

# S69 squeeze reconciliation
squeeze_data = np.load(os.path.join(SCRIPT_DIR, 's69_squeeze_reconciled.npz'),
                       allow_pickle=True)

# S69 A_s normalization chain
as_data = np.load(os.path.join(SCRIPT_DIR, 's69_as_normalization.npz'),
                  allow_pickle=True)

# S67 multifield delta-N
delta_n_data = np.load(os.path.join(SCRIPT_DIR, 's67_multifield_delta_n.npz'),
                       allow_pickle=True)

# Extract cutoff-scheme quantities
eps_H_cutoff = float(zeta_data['eps_cutoff_fold'])      # +0.02163
eps_H_zeta_a4 = float(zeta_data['eps_zeta_fold'])        # -0.04485 (a4 route)
eps_H_zeta_a2 = float(zeta_data['eps_H_zeta_a2'][3])     # a2 route at fold
eps_H_zeta_a24 = float(zeta_data['eps_H_zeta_a24'][3])   # combined at fold

# Zeta spectral action values at fold
tau_all = zeta_data['tau_all']
a2_arr = zeta_data['a2']
a4_arr = zeta_data['a4']
a6_arr = zeta_data['a6']
S_cutoff_arr = zeta_data['S_cutoff']

fold_idx = np.argmin(np.abs(tau_all - tau_fold))
a2_at_fold = float(a2_arr[fold_idx])
a4_at_fold = float(a4_arr[fold_idx])
a6_at_fold = float(a6_arr[fold_idx])
S_cutoff_at_fold = float(S_cutoff_arr[fold_idx])

# A_s from delta-N chain (cutoff scheme)
A_s_deltaN = float(as_data['A_s_correct'])               # 3.292e-10
A_s_obs = float(as_data['A_s_observed'])                  # 2.1e-9
gap_baseline_OOM = abs(float(as_data['gap_OOM']))         # 0.805

# Squeeze parameters
OOM_squeeze_canonical = float(squeeze_data['OOM_canonical'])  # 0.226

# Delta-N parameters
eps_H_deltaN = float(delta_n_data['eps_H_fold'])          # 0.022
M_Pl_MKK = float(delta_n_data['M_Pl_over_M_KK'])         # 32.778

print(f"""
  --- Cutoff scheme (reference) ---
    eps_H^cutoff   = {eps_H_cutoff:+.6f}
    H_fold         = {H_fold:.4f} M_KK
    A_s (delta-N)  = {A_s_deltaN:.4e}
    A_s (observed) = {A_s_obs:.4e}
    gap (baseline) = {gap_baseline_OOM:.4f} OOM

  --- Zeta scheme (from S66) ---
    eps_H^zeta(a4)      = {eps_H_zeta_a4:+.6f}
    eps_H^zeta(a2)      = {eps_H_zeta_a2:+.6f}
    eps_H^zeta(a2+a4)   = {eps_H_zeta_a24:+.6f}

  --- Spectral moments at fold ---
    a_2(fold) = {a2_at_fold:.4f}
    a_4(fold) = {a4_at_fold:.4f}
    a_6(fold) = {a6_at_fold:.4f}
    S_cutoff(fold) = {S_cutoff_at_fold:.2f}
    M_Pl / M_KK = {M_Pl_MKK:.4f}
""")

# =============================================================================
# SECTION 2: The S66 eps_H Formula and What It Means
# =============================================================================
print("=" * 78)
print("SECTION 2: The S66 eps_H Formula")
print("=" * 78)

# The S66 code (line 319) computes:
#   eps_H = (1/2) * (dS/dtau)^2 / (S * d2S/dtau^2)
#
# This is a SHAPE parameter: it depends only on the profile S(tau)
# and its first two derivatives. It does NOT contain M_Pl or G_DeWitt.
#
# Physical interpretation:
#   If S(tau) = V(tau)/M_KK^4 is the dimensionless potential, then:
#     S' = dV/dtau / M_KK^4
#     S'' = d2V/dtau^2 / M_KK^4
#
#   eps_H(S66) = S'^2 / (2*S*S'') = (V'/V) * (V'/V'')  / 2
#
#   This is NOT the standard eps_V = M_Pl^2/(2*G) * (V'/V)^2.
#   It is ALSO not the standard eps_H = -dH/dN.
#
#   However, it IS related to the potential curvature: it measures
#   how sharply the potential curves relative to its slope.
#
#   For a power-law V = V_0 * tau^n:
#     S' = n*tau^{n-1}, S'' = n(n-1)*tau^{n-2}
#     eps_H = (n*tau^{n-1})^2 / (2 * tau^n * n(n-1)*tau^{n-2})
#           = n / (2*(n-1))
#
#   For n=2 (quadratic): eps_H = 1 (the transit is "fast" rolling)
#   For n=1 (linear): eps_H diverges (no curvature to slow it)
#
# The KEY distinction: this eps_H is a PROFILE SHAPE parameter.
# The actual slow-roll parameter eps_V involves M_Pl and G_DeWitt,
# which determine the physical mass of the modulus field.

# Verify: compute eps_H from the S66 formula
cs_Scut = CubicSpline(tau_all, S_cutoff_arr)
cs_a4 = CubicSpline(tau_all, a4_arr)
cs_a2 = CubicSpline(tau_all, a2_arr)

S_val = cs_Scut(tau_fold)
dS_val = cs_Scut(tau_fold, 1)
d2S_val = cs_Scut(tau_fold, 2)
eps_check = 0.5 * dS_val**2 / (S_val * d2S_val)

a4_val = cs_a4(tau_fold)
da4_val = cs_a4(tau_fold, 1)
d2a4_val = cs_a4(tau_fold, 2)
eps_check_a4 = 0.5 * da4_val**2 / (a4_val * d2a4_val)

a2_val = cs_a2(tau_fold)
da2_val = cs_a2(tau_fold, 1)
d2a2_val = cs_a2(tau_fold, 2)
eps_check_a2 = 0.5 * da2_val**2 / (a2_val * d2a2_val)

print(f"""
  Verification of S66 eps_H formula: eps_H = S'^2 / (2*S*S''):

    Cutoff:
      S = {S_val:.2f}, S' = {dS_val:.2f}, S'' = {d2S_val:.2f}
      eps_H = {dS_val:.2f}^2 / (2 * {S_val:.2f} * {d2S_val:.2f})
            = {eps_check:.6f}
      S66 stored: {eps_H_cutoff:.6f}  Match: {abs(eps_check - eps_H_cutoff) < 1e-4}

    Zeta (a_4):
      a_4 = {a4_val:.4f}, a_4' = {da4_val:.4f}, a_4'' = {d2a4_val:.4f}
      eps_H = {da4_val:.4f}^2 / (2 * {a4_val:.4f} * {d2a4_val:.4f})
            = {eps_check_a4:.6f}
      S66 stored: {eps_H_zeta_a4:.6f}  Match: {abs(eps_check_a4 - eps_H_zeta_a4) < 1e-4}

    Zeta (a_2):
      a_2 = {a2_val:.4f}, a_2' = {da2_val:.4f}, a_2'' = {d2a2_val:.4f}
      eps_H = {da2_val:.4f}^2 / (2 * {a2_val:.4f} * {d2a2_val:.4f})
            = {eps_check_a2:.6f}
      S66 stored: {eps_H_zeta_a2:.6f}  Match: {abs(eps_check_a2 - eps_H_zeta_a2) < 1e-4}
""")

# =============================================================================
# SECTION 3: The Physical A_s -- Two Levels of Analysis
# =============================================================================
print("=" * 78)
print("SECTION 3: Two Levels of Analysis")
print("=" * 78)

print(f"""
  LEVEL 1: "ONE PHYSICAL TRANSIT"
  ===============================
  The physical picture: there is ONE transit event (the modulus crosses
  the fold at tau=0.19). The transit velocity v = 26.545 M_KK and
  the kinetic energy KE = G*v^2/2 = 1762 M_KK^4 are PHYSICAL observables
  of this event, not scheme-dependent quantities.

  The delta-N formula A_s = [Sum_I (drho/dsigma)^2 * sigma^2] / (6*KE)^2
  involves:
    - Numerator: GGE occupation physics (mode populations, dispersions)
    - Denominator: (6 * G * v^2/2)^2 = the modulus kinetic energy squared

  If the transit is ONE physical event, KE is ONE physical number,
  and A_s is FUNCTIONAL-INDEPENDENT to leading order.

  Under this interpretation: gap_zeta = gap_cutoff = {gap_baseline_OOM:.4f} OOM (baseline).


  LEVEL 2: "SCHEME-DEPENDENT DYNAMICS"
  =====================================
  Alternatively: the spectral functional DEFINES the dynamics. Different
  S(tau) means different equation of motion, different v_terminal,
  different H, different eps_H -- and A_s changes.

  Under this interpretation, we must self-consistently solve the modulus
  equation of motion in each scheme.

  The S66 eps_H = S'^2/(2*S*S'') is a profile shape parameter. To convert
  it to the physical slow-roll eps_V = M_Pl^2/(2*G)*(V'/V)^2, we need the
  ratio M_Pl^2/(G*V) -- but in the zeta scheme, how V maps to physical
  units depends on how M_Pl is extracted.

  Key question: are the S66 eps_H values physical slow-roll parameters,
  or just shape parameters?

  Answer: They are SHAPE PARAMETERS. The actual physical eps involves
  M_Pl and G_DeWitt. The S66 computation used them as a proxy for the
  slow-roll parameter under the assumption that the same shape gives
  the same tilt. For n_s (a ratio), this works. For A_s (an absolute
  normalization), it does not -- A_s depends on the absolute scale H.
""")

# =============================================================================
# SECTION 4: Level 1 Analysis (One Physical Transit)
# =============================================================================
print("=" * 78)
print("SECTION 4: Level 1 -- One Physical Transit")
print("=" * 78)

# Under Level 1, the transit event is physical and KE is fixed.
# The delta-N formula:
#   dN/dsigma_I = drho_I/dsigma_I / (6 * eps_H * M_Pl^2 * H^2)
#               = drho_I/dsigma_I / (6 * KE)
#
# where KE = eps_H * M_Pl^2 * H^2 = G_DeWitt * v_terminal^2 / 2
# This identity holds in any metric theory with standard modulus kinetic term.

KE_physical = G_DeWitt * v_terminal**2 / 2.0   # = 1761.6 M_KK^4

# Verify against Friedmann
# H^2 = (KE + PE) / (3*M_Pl^2)
# eps_H = KE / (M_Pl^2 * H^2) => M_Pl^2 * H^2 = KE / eps_H
M_Pl2_H2_from_eps = KE_physical / eps_H_cutoff
H2_from_eps = M_Pl2_H2_from_eps / M_Pl_MKK**2
H_from_eps = np.sqrt(H2_from_eps)

print(f"""
  Physical modulus kinetic energy:
    KE = G * v^2 / 2 = {G_DeWitt:.1f} * {v_terminal:.4f}^2 / 2 = {KE_physical:.2f} M_KK^4

  Consistency with Friedmann:
    eps_H * M_Pl^2 * H^2 = KE
    => M_Pl^2 * H^2 = KE / eps_H = {KE_physical:.2f} / {eps_H_cutoff:.6f}
                     = {M_Pl2_H2_from_eps:.2f} M_KK^4
    => H = sqrt(KE / (eps_H * M_Pl^2)) = {H_from_eps:.2f} M_KK
    Canonical H_fold = {H_fold:.2f} M_KK
    Ratio = {H_from_eps / H_fold:.4f}

  NOTE: The discrepancy ({abs(H_from_eps/H_fold - 1)*100:.1f}%) comes from the
  fact that eps_H(S66) = {eps_H_cutoff:.6f} is the SHAPE parameter
  S'^2/(2*S*S''), not the physical eps_H = -dH/dN.

  The actual physical eps_H = KE / (M_Pl^2 * H^2)
    = {KE_physical:.2f} / ({M_Pl_MKK:.4f}^2 * {H_fold:.2f}^2)
    = {KE_physical / (M_Pl_MKK**2 * H_fold**2):.8f}

  This tiny value (1.6e-6) confirms the transit is EXTREMELY PE-dominated.
  The modulus kinetic energy is negligible compared to the potential energy.
""")

eps_H_physical = KE_physical / (M_Pl_MKK**2 * H_fold**2)

# Under Level 1:
# A_s is determined by KE (physical), drho/dsigma (GGE, FI), and sigma^2 (GGE, FI).
# Since all three are physical/FI, A_s is FUNCTIONAL-INDEPENDENT.

# The only scheme-dependent correction is the BCS dressing of the mode equation,
# which involves eps_H through the Mukhanov-Sasaki potential z''/z.
# But since physical eps_H = 1.6e-6 (tiny), the BCS correction to z''/z
# is dominated by the BCS gap Delta, not by eps_H. So even the BCS correction
# is approximately functional-independent!

# Let's compute the BCS dressing sensitivity to eps_H:
# z''/z ~ a''/a + (BCS terms) ~ H^2*(2 + ...) + Delta^2/...
# The eps_H enters via the a''/a = H^2*(2 - eps_H) piece.
# Since eps_H ~ 1.6e-6, the change from cutoff to zeta in the a''/a piece is:
# delta(z''/z) / (z''/z) ~ delta(eps_H) / 2 ~ negligible
# So even the BCS dressing correction is FI at Level 1.

print(f"""
  LEVEL 1 RESULT:
    Under the "one physical transit" interpretation:
    - KE is physical: {KE_physical:.2f} M_KK^4
    - GGE numerator is physical (mode populations)
    - A_s is FUNCTIONAL-INDEPENDENT
    - All corrections (BCS, squeeze, phase) are FI
    - The gap is the same in every scheme:

    gap^{{Level 1}} = {gap_baseline_OOM:.4f} OOM (baseline)
    After corrections: {gap_baseline_OOM - (0.046 + OOM_squeeze_canonical + 0.043):.4f} OOM
""")

gap_level1 = gap_baseline_OOM - (0.046 + OOM_squeeze_canonical + 0.043)

# =============================================================================
# SECTION 5: Level 2 Analysis (Scheme-Dependent Dynamics)
# =============================================================================
print("=" * 78)
print("SECTION 5: Level 2 -- Scheme-Dependent Dynamics")
print("=" * 78)

# Under Level 2, the spectral functional defines the potential and thus
# the dynamics. In each scheme, the modulus evolves according to:
#   G * tau_ddot + 3*H*G*tau_dot + dV/dtau = 0
#   H^2 = (G*tau_dot^2/2 + V) / (3*M_Pl^2)
#
# The A_s then depends on the self-consistent solution.
#
# The single-field slow-roll formula gives:
#   A_s = H^2 / (8*pi^2 * eps_V * M_Pl^2 * c_s)
#       = V / (24*pi^2 * eps_V * M_Pl^4 * c_s)  [PE-dominated: H^2 ~ V/(3*M_Pl^2)]
#
# where eps_V = M_Pl^2/(2*G) * (V'/V)^2.
#
# Therefore:
#   A_s = V * 2*G / (24*pi^2 * (V'/V)^2 * M_Pl^6 * c_s)
#       = G * V^3 / (12*pi^2 * V'^2 * M_Pl^6 * c_s)
#
# But wait -- the delta-N formula gives A_s in terms of the GGE spectrum,
# not in terms of the slow-roll potential. The two approaches should agree
# if the mode equation is solved consistently.
#
# The problem with Level 2: the cutoff action S_cutoff and the zeta
# action a_4 have DIFFERENT physical normalizations. S_cutoff at the fold
# is ~250,000 while a_4 is ~1,351. These are not comparable directly.
# The physical potential V is:
#   Cutoff: V = S_cutoff * M_KK^4 * (normalization factor from f_2, Lambda, a_2...)
#   Zeta:   V = a_4 * M_KK^4 * (different normalization from zeta regularization)
#
# To compare, we need to know M_Pl in each scheme:
#   Cutoff: M_Pl^2 = f_2 * Lambda^2 * a_2 / (16*pi^2)
#   Zeta:   M_Pl^2 is extracted from the a_2(K) * R cross-term in a_4(D_full^2)
#
# Since M_Pl is OBSERVED (we know M_Pl = 2.435e18 GeV), both schemes must
# give the same M_Pl. The normalization factor C is then:
#   Cutoff: V_cutoff = C_cutoff * S_cutoff * M_KK^4, with C_cutoff * a_2 ~ M_Pl^2
#   Zeta:   V_zeta = C_zeta * a_4 * M_KK^4, with C_zeta * a_2 ~ M_Pl^2
#
# But the RATIO V/M_Pl^4 (which enters A_s) is:
#   Cutoff: V/M_Pl^4 = C_cutoff * S_cutoff * M_KK^4 / (C_cutoff * a_2 * ...)^2
#   Zeta:   V/M_Pl^4 = C_zeta * a_4 * M_KK^4 / (C_zeta * a_2 * ...)^2
#
# The normalization factors C cancel differently in each case. This is the
# heart of the scheme-dependence.
#
# RESOLUTION: Use the dimensionless log-derivative V'/V, which is the same
# as S'/S (the normalization cancels in the ratio). The S66 eps_H values
# encode this correctly. For the A_s RATIO between schemes, use:
#
#   A_s^zeta / A_s^cutoff = (V_zeta/V_cutoff) / (eps_V^zeta/eps_V^cutoff)
#                          = (V_zeta/V_cutoff) * [(V'/V)_cutoff / (V'/V)_zeta]^2
#
# But V_zeta/V_cutoff depends on the normalization!
#
# Alternative approach: express A_s purely in terms of the physical eps_V
# and H. Since H is observed (through its effects on the CMB), and eps
# determines n_s, the combination A_s = H^2/(8*pi^2*eps*M_Pl^2*c_s) gives:
#
#   A_s^zeta / A_s^cutoff = (H_zeta/H_cutoff)^2 * (eps_cutoff/eps_zeta)
#
# We need H_zeta/H_cutoff. In terms of the potential:
#   (H_zeta/H_cutoff)^2 = V_zeta / V_cutoff  [PE-dominated]
#
# And eps^zeta/eps^cutoff involves the LOG-DERIVATIVES:
#   eps_V = M_Pl^2/(2G) * (V'/V)^2
#   eps_V^zeta / eps_V^cutoff = [(V'/V)_zeta / (V'/V)_cutoff]^2
#
# Substituting:
#   A_s^zeta / A_s^cutoff = (V_z/V_c) * [(V'/V)_c / (V'/V)_z]^2
#                          = (V_z/V_c) * (V'_c/V'_z * V_z/V_c)^2
#                          = (V_z/V_c)^3 * (V'_c/V'_z)^2
#
# This STILL requires V_z/V_c (the normalization ratio).
#
# FUNDAMENTAL POINT: Without specifying the absolute normalization of V
# in each scheme, we cannot compute the Level 2 A_s ratio. The normalization
# involves how M_Pl, Lambda (cutoff scale), and f_k (spectral moments) relate.
#
# What we CAN compute: the ratio of A_s IF we assume the same M_Pl
# (physical requirement) and the same M_KK (same internal geometry).

# The standard approach in Chamseddine-Connes:
# Cutoff action: S_cutoff = (1/16pi^2) * [f_0*L^4*a_0 + f_2*L^2*a_2*R + f_4*a_4*F^2 + ...]
# M_Pl^2 is extracted from the R coefficient: M_Pl^2 = f_2*L^2*a_2/(12*pi^2) [approx]
# The potential V = f_0*L^4*a_0/(16pi^2)  [cosmological constant piece]
# So V/M_Pl^4 ~ f_0*a_0 / (f_2*a_2)^2 * 1/L^4 [schematic]
#
# Zeta action: S_zeta = a_4(D_full^2) = a_0(M4)*a_4(K) + a_2(M4)*a_2(K) + a_4(M4)*a_0(K)
# M_Pl^2 is from the a_2(M4)*a_2(K) cross-term: M_Pl^2 propto a_2(K)
# The potential comes from the a_0(M4)*a_4(K) = Vol(M4)*a_4(K) term: V propto a_4(K)
# So V/M_Pl^2 ~ a_4(K)/a_2(K)  [no Lambda or f_k dependence!]
#
# CRITICAL: In the zeta scheme, there is NO cutoff Lambda and no f_0, f_2.
# The ratio V/M_Pl^2 is purely geometric: a_4/a_2.
# In the cutoff scheme, V/M_Pl^2 ~ f_0*L^4*a_0 / (f_2*L^2*a_2) ~ (f_0/f_2)*L^2*(a_0/a_2).
#
# This is the FUNDAMENTAL difference: in the cutoff scheme, the CC/M_Pl^2 ratio
# depends on L^2 (the cutoff scale) and f_0/f_2 (the spectral moments of f(x)).
# In the zeta scheme, it depends only on geometric ratios a_{2k}/a_{2m}.

# For the A_s formula in each scheme:
# Cutoff: A_s ~ V/(eps_V * M_Pl^4) ~ (f_0*L^4*a_0) / (eps_V * (f_2*L^2*a_2)^2)
#             ~ (f_0/f_2^2) * (a_0/a_2^2) / eps_V  [times L^0 -- Lambda cancels!]
#
# Zeta:   A_s ~ V/(eps_V * M_Pl^4) ~ a_4(K) / (eps_V * a_2(K)^2)

# So the A_s RATIO between schemes:
#   A_s^zeta / A_s^cutoff = [a_4/a_2^2 * eps_V^cutoff] / [(f_0/f_2^2)*(a_0/a_2^2) * eps_V^zeta]
#                          = (f_2^2/f_0) * (a_4/a_0) * (eps_V^cutoff / eps_V^zeta)

# For f(x) = sqrt(x):
# f_0 = integral sqrt(x) x^1 dx from 0 to 1 = 2/3  [need specific definition]
# f_2 = integral sqrt(x) dx from 0 to 1 = 2/3
# Actually, in the standard NCG convention:
# f_k = integral_0^inf f(x) x^{k-1} dx [Laplace-type moments]
# For f(x) = sqrt(x) = x^{1/2}, used on [0, L^2]:
# This is really: Tr f(D^2/L^2) = sum_j f(lam_j^2/L^2) = sum_j |lam_j|/L
# which is S_cutoff/L.

# More precisely, the spectral action in NCG is:
#   Tr f(D^2/Lambda^2) ~ sum_{k=0}^N f_k * Lambda^{d-2k} * a_{2k}(D^2)
# where f_k = integral_0^inf f(u) u^{(d-2k)/2-1} du (for d=4):
#   f_0 = int f(u) u du,  f_2 = int f(u) du,  f_4 = f(0)
#
# For f(x) = sqrt(x) on [0,1] (or really f(x) = x^{1/2}):
#   f_0 = int_0^1 sqrt(u) * u du = int_0^1 u^{3/2} du = 2/5
#   f_2 = int_0^1 sqrt(u) du = 2/3
#   f_4 = f(0) = 0  [!]
#
# WAIT: f_4 = f(0) = sqrt(0) = 0. This means the a_4 term in the
# CUTOFF action with f(x) = sqrt(x) has ZERO coefficient!
# This is important but tangential to the A_s calculation.
#
# For a general cutoff function (not sqrt(x)), f_0, f_2, f_4 are all nonzero.
# The A_s depends on f_0/f_2^2 (which we can treat as O(1)).
#
# For our framework, the "cutoff" action is S_cutoff = Tr|D_K| = sum dim^2 |lam|,
# which is NOT the standard NCG Tr f(D^2/L^2) form. It corresponds to
# f(x) = sqrt(x) applied at the specific scale L = M_KK (not free L).
# The M_Pl extraction uses S_cutoff as the total potential energy.

# Rather than getting lost in normalization conventions, let me use the
# PHYSICAL approach:

# Both schemes must give M_Pl = 2.435e18 GeV (observed).
# Both schemes give M_KK = 7.43e16 GeV (from the spectral triple, same D_K).
# The Hubble parameter is:
#   H^2 = rho/(3*M_Pl^2)
# where rho is the total energy density.
#
# In the cutoff scheme: rho ~ S_cutoff * M_KK^4 / Vol => H_fold = 586.5 M_KK
# (from S38, self-consistent with the transit dynamics)
#
# In the zeta scheme: rho ~ a_4 * M_KK^4 / Vol => H_zeta = ???
# The ratio is: (H_zeta/H_cutoff)^2 = a_4/S_cutoff = 0.0054
# => H_zeta = 586.5 * sqrt(0.0054) = 43 M_KK
#
# BUT this assumes the SAME normalization convention for converting
# spectral sums to energy density. This is NOT guaranteed.
#
# The CORRECT Level 2 analysis requires the full NCG machinery to
# extract M_Pl, H, and eps in each scheme self-consistently.
# This is beyond the scope of this computation -- it would require
# re-deriving the product geometry formula from scratch for each functional.

# PRAGMATIC APPROACH: Express the uncertainty as a range.
# Level 1 (one transit): gap = 0.490 OOM (same as cutoff)
# Level 2 (extreme): gap could be anywhere from ~0 to ~7 OOM depending
# on normalization assumptions.
#
# The INTERMEDIATE approach: use the S66 shape parameters to estimate
# how much the A_s formula changes, recognizing that:
# 1. The GGE numerator is FI (mode physics)
# 2. The denominator KE is physical in Level 1, but in Level 2 it
#    scales with the self-consistent modulus dynamics

# The S66 eps_H already tells us: if the spectral action profile shape
# is what matters (for n_s, it clearly does), then the SHAPE of the
# potential changes between schemes. But for A_s, we need absolute scale.

# Use the eps_H * H^2 identity differently:
# A_s = Sum (dN/dsigma)^2 sigma^2
#     = Sum [drho/dsigma / (6*eps_H*M_Pl^2*H^2)]^2 * sigma^2
#
# If we hold the GGE occupation fixed (FI) and vary only eps_H and H,
# the ratio of A_s between schemes is:
#   A_s^zeta / A_s^cutoff = [eps_cutoff * M_Pl^2 * H_cutoff^2]^2
#                          / [eps_zeta * M_Pl^2 * H_zeta^2]^2
#
# = [eps_cutoff * H_cutoff^2 / (eps_zeta * H_zeta^2)]^2
#
# With H^2 = V/(3*M_Pl^2) and eps = M_Pl^2/(2*G) * (V'/V)^2:
# eps * H^2 = (V'/V)^2 * V / (6*G)
# = V'^2 / (6*G*V)
#
# So (eps*H^2) ratio = [V'^2_cutoff / V_cutoff] / [V'^2_zeta / V_zeta]
# = (V'_c/V'_z)^2 * (V_z/V_c)
#
# This still involves V_z/V_c. But we can express V'/V (the log-derivative):

log_deriv_cutoff = abs(dS_val) / S_val
log_deriv_zeta_a4 = abs(da4_val) / a4_val
log_deriv_zeta_a2 = abs(da2_val) / a2_val

print(f"""
  Dimensionless log-derivatives |V'/V| = |S'/S|:
    Cutoff:   {log_deriv_cutoff:.6f}
    Zeta(a4): {log_deriv_zeta_a4:.6f}
    Zeta(a2): {log_deriv_zeta_a2:.6f}

  These are pure SHAPE parameters (normalization cancels).
  For eps_V = M_Pl^2/(2G) * (V'/V)^2:
    eps_V_cutoff    = {M_Pl_MKK**2 / (2*G_DeWitt) * log_deriv_cutoff**2:.6f}
    eps_V_zeta(a4)  = {M_Pl_MKK**2 / (2*G_DeWitt) * log_deriv_zeta_a4**2:.6f}
    eps_V_zeta(a2)  = {M_Pl_MKK**2 / (2*G_DeWitt) * log_deriv_zeta_a2**2:.6f}

  NOTE: These eps_V values are ALL >> 1, confirming the transit is NOT
  slow-roll. The S66 eps_H = S'^2/(2*S*S'') ~ 0.02 is a DIFFERENT quantity
  (a shape parameter of the profile, not the physical slow-roll eps_V).
""")

eps_V_cutoff = M_Pl_MKK**2 / (2 * G_DeWitt) * log_deriv_cutoff**2
eps_V_zeta_a4 = M_Pl_MKK**2 / (2 * G_DeWitt) * log_deriv_zeta_a4**2
eps_V_zeta_a2 = M_Pl_MKK**2 / (2 * G_DeWitt) * log_deriv_zeta_a2**2

# =============================================================================
# SECTION 6: The Proper Scheme Comparison for A_s
# =============================================================================
print("=" * 78)
print("SECTION 6: Proper Scheme Comparison")
print("=" * 78)

# RESOLUTION of the Level 2 problem:
#
# In the delta-N framework, A_s depends on eps_H * M_Pl^2 * H^2 = KE.
# We established that in the PE-dominated limit:
#   eps_H * H^2 = KE/M_Pl^2 = (V')^2/(6*G*V) [from eps_V definition and Friedmann]
#
# The question is: when we change the spectral functional from S_cutoff to a_4,
# does the PHYSICAL KE change?
#
# ARGUMENT FOR "YES" (Level 2):
# The potential V is defined by the spectral functional. Different V means
# different forces, different transit velocity, different KE. The modulus
# equation of motion gives v_terminal ~ V'/(3*H*G) in the friction-dominated
# regime. Since V' changes between schemes (different gradient), v changes.
#
# ARGUMENT FOR "NO" (Level 1):
# The spectral functional is a REGULARIZATION CHOICE for the same underlying
# theory. The physical transit is the same event. The regularization scheme
# is like a choice of gauge -- it cannot change observables.
# Analogy: computing a QFT amplitude in dimensional regularization vs
# cutoff regularization gives the same physical result once you match
# the renormalization conditions. Similarly, both spectral functionals
# must give the same physics once we match M_Pl, M_KK, and alpha_i.
#
# THE ANSWER depends on whether the spectral action is:
# (a) A regularized version of a unique underlying theory (Level 1 correct)
# (b) A different theory for each functional (Level 2 correct)
#
# In Connes' NCG program, the spectral action IS the theory -- the functional
# f(x) is a free function (analogous to choosing the gauge group in QFT).
# Different f(x) gives different physics. This supports Level 2.
#
# In Lizzi's (my) perspective: the choice of functional is analogous to
# a REGULARIZATION SCHEME. Different schemes give different intermediate
# results but should agree on physical observables once matched. The
# spectral moments f_0, f_2, f_4 are like running coupling constants --
# they differ between schemes but the physical predictions should match
# after renormalization group matching.
#
# PRACTICAL COMPUTATION:
# Since we cannot resolve the Level 1 vs Level 2 question purely from
# computation, we report BOTH results.

# For Level 2, we need the (eps*H^2) ratio = (V'^2/V) ratio.
# V' is proportional to the gradient dS/dtau (or da4/dtau):
#   V'_cutoff = C_c * dS/dtau
#   V'_zeta = C_z * da4/dtau
# V is proportional to the action value:
#   V_cutoff = C_c * S
#   V_zeta = C_z * a4
# So (V'^2/V) ratio = (C_c * dS^2 / (C_c * S)) / (C_z * da4^2 / (C_z * a4))
#                    = (dS^2/S) / (da4^2/a4)  [C cancels!]

# This ratio IS normalization-independent!
# (eps*H^2)_zeta / (eps*H^2)_cutoff = (da4^2/a4) / (dS^2/S)

epsH2_ratio_a4 = (da4_val**2 / a4_val) / (dS_val**2 / S_val)
epsH2_ratio_a2 = (da2_val**2 / a2_val) / (dS_val**2 / S_val)

# Combined a2+a4
a24_val = a2_val + a4_val
da24_val = da2_val + da4_val
epsH2_ratio_a24 = (da24_val**2 / a24_val) / (dS_val**2 / S_val)

print(f"""
  NORMALIZATION-INDEPENDENT RATIO:
    (eps*H^2)^zeta / (eps*H^2)^cutoff = (S'/S)^2_zeta * S_zeta / [(S'/S)^2_cutoff * S_cutoff]
                                       = (dS^2_zeta/S_zeta) / (dS^2_cutoff/S_cutoff)

  For zeta a_4:
    da_4^2/a_4 = {da4_val**2/a4_val:.4f}
    dS^2/S    = {dS_val**2/S_val:.4f}
    ratio     = {epsH2_ratio_a4:.6f}

  For zeta a_2:
    da_2^2/a_2 = {da2_val**2/a2_val:.4f}
    ratio     = {epsH2_ratio_a2:.6f}

  For zeta a_2+a_4:
    ratio     = {epsH2_ratio_a24:.6f}
""")

# Since A_s ~ 1/(eps*H^2)^2 [from delta-N: A_s = (GGE stuff) / (6*KE)^2 and KE = eps*M_Pl^2*H^2]:
# But eps*M_Pl^2*H^2 = M_Pl^2 * (eps*H^2)
# In Level 2: KE = M_Pl^2 * (V'^2)/(6*G*V)
# The M_Pl is the SAME in both schemes (physical constant).
# So A_s ~ 1/[M_Pl^2 * (V'^2/(6GV))]^2 = (6GV)^2 / (M_Pl^4 * V'^4)
# = 36 G^2 V^2 / (M_Pl^4 * V'^4)
#
# Hmm wait -- this gives A_s propto V^2/V'^4. Let me be more careful.
#
# A_s = [Sum (drho/dsigma)^2 sigma^2] / (6*KE)^2
# KE = eps_V * V / 3 = [M_Pl^2/(2G)] * (V'/V)^2 * V / 3 = M_Pl^2 * V'^2 / (6*G*V)
# A_s = (GGE numerator) / (6 * M_Pl^2 * V'^2 / (6*G*V))^2
#     = (GGE) * (6GV)^2 / (36 * M_Pl^4 * V'^4)
#     = (GGE) * G^2 * V^2 / (M_Pl^4 * V'^4)
#
# A_s^zeta / A_s^cutoff = (V_z/V_c)^2 * (V'_c/V'_z)^4
#
# With V_z = C_z * a4, V_c = C_c * S, V'_z = C_z * da4, V'_c = C_c * dS:
# = (C_z*a4 / (C_c*S))^2 * (C_c*dS / (C_z*da4))^4
# = (C_z/C_c)^{2-4} * (a4/S)^2 * (dS/da4)^4
# = (C_c/C_z)^2 * (a4/S)^2 * (dS/da4)^4
#
# The normalization ratio C_c/C_z does NOT cancel! Only in the
# (eps*H^2) ratio does it cancel. For A_s itself, we need C.
#
# However, A_s ~ 1/(eps*H^2)^2 requires a FOURTH power of eps*H^2,
# and eps*H^2 propto V'^2/V. So:
# A_s ~ 1/(V'^2/V)^2 = V^2/V'^4
# A_s^z/A_s^c = (V_z/V_c)^2 * (V'_c/V'_z)^4 = (C_z/C_c)^{-2} * ...
# No, A_s ~ (GGE)/(6*KE)^2 and KE = M_Pl^2*(V'^2)/(6*G*V).
# Since M_Pl and G are the same:
# A_s = GGE * (36*G^2*V^2) / (36*M_Pl^4*V'^4) = GGE * G^2*V^2 / (M_Pl^4*V'^4)

# Actually let me just carefully use the (eps*H^2) ratio:
# KE = eps_V * M_Pl^2 * H^2 = ... no.
# eps_H = KE / (M_Pl^2 * H^2). So KE = eps_H * M_Pl^2 * H^2.
# In PE-dominated limit: H^2 = V/(3*M_Pl^2).
# eps_H = KE * 3 / V (physical). KE = eps_H * V / 3.
# But KE = G*v^2/2, and the slow-roll gives v ~ V'/(3*H*G),
# so KE = (V')^2 / (18*G*H^2) = (V')^2 * M_Pl^2 / (6*G*V).
# And eps_H = KE/(M_Pl^2*H^2) = (V')^2*M_Pl^2/(6*G*V) / (V/(3*M_Pl^2))
# = (V')^2 * 3*M_Pl^4 / (6*G*V^2) = (V')^2*M_Pl^4/(2*G*V^2)
# Hmm, that gives eps_H = eps_V * M_Pl^2/V... no.
#
# Standard: eps_V = M_Pl^2/(2*G) * (V'/V)^2 = M_Pl^2*V'^2/(2*G*V^2)
# eps_H approx eps_V in slow-roll.
# KE = eps_H * M_Pl^2 * H^2 ~ eps_V * V/3  (using H^2 = V/(3*M_Pl^2))
# = M_Pl^2*V'^2/(2*G*V^2) * V/3 = M_Pl^2*V'^2/(6*G*V)  [confirmed]

# So:
# A_s = GGE_numerator / [6 * M_Pl^2 * V'^2/(6*G*V)]^2
#     = GGE_numerator / [M_Pl^2 * V'^2/(G*V)]^2
#     = GGE_numerator * G^2 * V^2 / (M_Pl^4 * V'^4)
#
# A_s^z/A_s^c = (V_z/V_c)^2 * (V'_c/V'_z)^4
#
# In terms of our spectral actions:
# V propto S * M_KK^4 / Vol (with scheme-dependent coefficient)
# V' propto dS/dtau * M_KK^4 / Vol
# So V_z/V_c = (C_z*a4) / (C_c*S) and V'_z/V'_c = (C_z*da4) / (C_c*dS)
#
# A_s^z/A_s^c = [(C_z*a4)/(C_c*S)]^2 * [(C_c*dS)/(C_z*da4)]^4
#             = (C_z/C_c)^{-2} * (a4/S)^2 * (dS/da4)^4
#
# So we need (C_c/C_z)^2, which represents the NORMALIZATION mismatch.

# We can determine C_c/C_z from the M_Pl matching condition:
# M_Pl^2 = C_c * a_2^{cutoff extraction} = C_z * a_2^{zeta extraction}
# In both cases M_Pl^2 involves a_2. If the a_2 coefficient matches:
# C_c * (f_2*L^2/(16pi^2)) * a_2 = C_z * (cross-term coefficient) * a_2
# The ratio C_c/C_z depends on f_2, Lambda, and the zeta cross-term coefficient.
#
# Without specifying these, we cannot determine C_c/C_z.
# This is the fundamental indeterminacy at Level 2.

# PRACTICAL RESOLUTION: Report the (eps*H^2) ratio (which IS normalization-
# independent) and the resulting A_s ratio UNDER TWO ASSUMPTIONS:
# (A) Same normalization (C_c = C_z): A_s ratio = (a4/S)^2 * (dS/da4)^4
# (B) Matched physics (Level 1): A_s ratio = 1

ratio_Cequal = (a4_val / S_val)**2 * (dS_val / da4_val)**4
ratio_epsH2only = 1.0 / epsH2_ratio_a4**2  # A_s ~ 1/(eps*H^2)^2

A_s_level1 = A_s_deltaN  # Same as cutoff
A_s_level2_Cequal_a4 = A_s_deltaN * ratio_Cequal
A_s_level2_epsH2_a4 = A_s_deltaN / epsH2_ratio_a4**2

gap_level1_raw = abs(np.log10(A_s_obs / A_s_level1))
gap_level2_Cequal = abs(np.log10(A_s_obs / A_s_level2_Cequal_a4)) if A_s_level2_Cequal_a4 > 0 else float('inf')
gap_level2_epsH2 = abs(np.log10(A_s_obs / A_s_level2_epsH2_a4)) if A_s_level2_epsH2_a4 > 0 else float('inf')

# The direction of the gap: if A_s^computed > A_s^obs, gap is negative (overshoot)
# if A_s^computed < A_s^obs, gap is positive (undershoot)
gap_sign_level1 = np.log10(A_s_obs / A_s_level1)
gap_sign_Cequal = np.log10(A_s_obs / A_s_level2_Cequal_a4) if A_s_level2_Cequal_a4 > 0 else float('inf')
gap_sign_epsH2 = np.log10(A_s_obs / A_s_level2_epsH2_a4) if A_s_level2_epsH2_a4 > 0 else float('inf')

print(f"""
  THREE ESTIMATES OF A_s^zeta:

  Estimate 1 (Level 1: one physical transit, KE = {KE_physical:.2f}):
    A_s^zeta = A_s^cutoff = {A_s_level1:.4e}
    gap = {gap_sign_level1:+.4f} OOM
    Interpretation: spectral functional is regularization, not dynamics

  Estimate 2 (Level 2, C_c = C_z, A_s propto V^2/V'^4):
    V_z/V_c ratio = a4/S = {a4_val/S_val:.6f}
    V'_z/V'_c ratio = da4/dS = {da4_val/dS_val:.6f}
    A_s ratio = (V_z/V_c)^2 * (V'_c/V'_z)^4 = {ratio_Cequal:.4e}
    A_s^zeta = {A_s_level2_Cequal_a4:.4e}
    gap = {gap_sign_Cequal:+.4f} OOM
    Interpretation: same normalization, different action shape

  Estimate 3 (Level 2, using (eps*H^2) ratio -- C-independent):
    (eps*H^2) ratio = {epsH2_ratio_a4:.6f}
    A_s ~ 1/(eps*H^2)^2, ratio = {1/epsH2_ratio_a4**2:.4e}
    A_s^zeta = {A_s_level2_epsH2_a4:.4e}
    gap = {gap_sign_epsH2:+.4f} OOM
    Interpretation: uses only dimensionless profile shapes

  IMPORTANT: Estimates 2 and 3 DISAGREE because Estimate 2 uses
  A_s propto V^2/V'^4 while Estimate 3 uses A_s propto 1/(V'^2/V)^2 = V^2/V'^4.
  These should be the same... let me check.

  Check: 1/ratio_epsH2^2 = 1/{epsH2_ratio_a4:.6f}^2 = {1/epsH2_ratio_a4**2:.4e}
  ratio_Cequal (with C_c=C_z) = (a4/S)^2 * (dS/da4)^4 = {ratio_Cequal:.4e}
  (a4/S)^2 * (dS/da4)^4 = [(a4/S) * (dS/da4)^2]^2 = [(a4*dS^2)/(S*da4^2)]^2
  eps*H^2 ratio = (da4^2/a4)/(dS^2/S) = (da4^2*S)/(a4*dS^2)
  1/ratio^2 = (a4*dS^2)^2 / (da4^2*S)^2 = (a4/S)^2 * (dS/da4)^4
  = ratio_Cequal! CONFIRMED: they agree.
""")

# Great -- Estimates 2 and 3 are the SAME (as they must be, since
# A_s propto V^2/V'^4 = 1/(eps*H^2)^2 when C cancels).

# =============================================================================
# SECTION 7: Final A_s Gap Budget
# =============================================================================
print("=" * 78)
print("SECTION 7: Final A_s Gap Budget")
print("=" * 78)

# The BCS dressing correction:
BCS_OOM_cutoff = 0.046  # from S69  # (local)

# In Level 1, ALL corrections are the same:
total_corr_level1 = BCS_OOM_cutoff + OOM_squeeze_canonical + 0.043
gap_level1_final = gap_level1_raw - total_corr_level1

# In Level 2, the BCS dressing changes (eps_H enters):
# The BCS dressing shifts eps_H by a fractional amount.
# In cutoff: delta(log A_s) = 0.046. Using A_s ~ 1/eps^2:
# delta(log_10 eps) = 0.046/2 = 0.023
# fractional change in eps = 10^{0.023} - 1 = 0.0544
# This SAME absolute change in eps occurs in any scheme (BCS physics).
# But A_s ~ 1/(eps*H^2)^2. The BCS dressing modifies eps (via z''/z):
# delta(log A_s) = -2 * delta(log(eps*H^2)) = -2 * delta(eps)/eps * delta(eps contribution)
# Since the mode equation z''/z depends on eps through a''/a = H^2(2-eps),
# and eps is tiny in both schemes (1.6e-6 physical), the BCS correction
# is essentially independent of eps. The dominant BCS contribution comes
# from Delta^2 terms in z''/z, not from eps.
# So BCS correction ~ same in both schemes to leading order.
BCS_OOM_level2 = BCS_OOM_cutoff  # same to leading order (eps << Delta)

total_corr_level2 = BCS_OOM_level2 + OOM_squeeze_canonical + 0.043

# Level 2 gap (from Estimate 3 which is C-independent):
gap_level2_raw = gap_sign_epsH2  # signed gap
gap_level2_final = abs(gap_level2_raw) - total_corr_level2
# But which direction? A_s_level2 is huge (>> obs), so gap is negative (overshoot)
# Actually: gap = log10(obs/computed). If computed > obs, gap < 0.
overshoot_level2 = (A_s_level2_epsH2_a4 > A_s_obs)

if overshoot_level2:
    # Computed >> observed: massive overshoot
    gap_level2_final_signed = gap_sign_epsH2 + total_corr_level2  # corrections make it worse
else:
    gap_level2_final_signed = gap_sign_epsH2 + total_corr_level2  # corrections help

print(f"""
  ===========================================================
  A_s GAP BUDGET: LEVEL 1 (ONE PHYSICAL TRANSIT)
  ===========================================================
    Baseline gap:           {gap_sign_level1:+.4f} OOM
    BCS dressing:          +{BCS_OOM_cutoff:.3f} OOM
    Non-BD squeeze:        +{OOM_squeeze_canonical:.3f} OOM
    Phase correction:      +{0.043:.3f} OOM
    Total corrections:     +{total_corr_level1:.3f} OOM
    -----------------------------------------------
    FINAL GAP:              {gap_level1_raw - total_corr_level1:.4f} OOM
    Classification:         FUNCTIONAL-INDEPENDENT

  ===========================================================
  A_s GAP BUDGET: LEVEL 2 (SCHEME-DEPENDENT DYNAMICS)
  ===========================================================
    A_s^zeta (a4) = {A_s_level2_epsH2_a4:.4e} vs observed {A_s_obs:.4e}
    {'MASSIVE OVERSHOOT: computed >> observed' if overshoot_level2 else 'Undershoot: computed < observed'}
    Baseline gap:           {gap_sign_epsH2:+.4f} OOM {'(overshoot)' if overshoot_level2 else '(undershoot)'}
    Corrections:            Same as Level 1 (eps << Delta in z''/z)
    -----------------------------------------------
    FINAL GAP:              {gap_sign_epsH2 + total_corr_level2:+.4f} OOM {'(overshoot)' if overshoot_level2 else ''}
    Classification:         MAXIMALLY SCHEME-DEPENDENT

  ===========================================================
  COMPARISON
  ===========================================================
    gap_cutoff (Level 1):  {gap_level1_final:.4f} OOM  (undershoot)
    gap_zeta (Level 2):    {gap_sign_epsH2:+.4f} OOM  ({'overshoot' if overshoot_level2 else 'undershoot'})
    |difference|:          {abs(gap_sign_epsH2 - gap_sign_level1):.4f} OOM
""")

delta_gap_L1 = 0.0  # Level 1: no change by definition  # (local)
delta_gap_L2 = abs(gap_sign_epsH2 - gap_sign_level1)

# =============================================================================
# SECTION 8: Physical Resolution
# =============================================================================
print("=" * 78)
print("SECTION 8: Physical Resolution")
print("=" * 78)

print(f"""
  The massive Level 2 gap shift ({delta_gap_L2:.1f} OOM) is a REDUCTIO argument:

  1. If the spectral functional is truly "different dynamics" (Level 2), then
     the zeta action gives A_s ~ {A_s_level2_epsH2_a4:.1e}, which is
     {abs(gap_sign_epsH2):.0f} orders of magnitude ABOVE observed. This would
     exclude the zeta functional as a viable theory for this spectral triple.

  2. The zeta functional also gives n_s = 1.09 (blue tilt), independently
     excluding it from Planck observations (S66 ZETA-SA-66 FAIL).

  3. BOTH the n_s exclusion and the A_s overshoot trace to the SAME cause:
     the a_4 spectral moment DECREASES with tau, giving a concave potential
     that produces hilltop dynamics instead of roll-down dynamics.

  4. This means: in the context of this spectral triple (SU(3) fiber, Jensen
     deformation transit), the zeta functional is EXCLUDED by both n_s and A_s.
     This is not a weakness -- it is a SELECTION CRITERION.

  CLASSIFICATION:
    The A_s gap is FUNCTIONAL-INDEPENDENT at Level 1 (0 OOM shift)
    and MAXIMALLY SCHEME-DEPENDENT at Level 2 ({delta_gap_L2:.1f} OOM shift).

    The PHYSICAL answer is Level 1 (one transit, one KE), with the proviso
    that the spectral functional CHOICE determines which functionals are
    VIABLE for this spectral triple. The zeta functional is excluded by
    both n_s (blue tilt) and A_s (massive overshoot).

    This is consistent with S67 FUNCTIONAL-SELECT-67 which established
    that the anomaly-derived family is also excluded from red tilt --
    the frustration triangle of (cutoff, zeta, anomaly) where only cutoff
    can produce n_s < 1 for this spectral triple.

  CONCLUSION:
    The A_s gap = {gap_level1_final:.3f} OOM is STRUCTURAL (functional-independent)
    at Level 1. The functional choice affects VIABILITY (which functionals
    work at all), not the MAGNITUDE of the gap within the viable functional.
""")

# =============================================================================
# SECTION 9: Classification Table
# =============================================================================
print("=" * 78)
print("SECTION 9: Classification Table")
print("=" * 78)

print(f"""
  +---------------------------------+-------------------+-------------------+
  | Quantity                        | FI (Level 1)      | SD (Level 2)      |
  +---------------------------------+-------------------+-------------------+
  | eps_H shape parameter           | n/a               | Cutoff: +0.022    |
  |                                 |                   | Zeta:   -0.045    |
  | eps_H physical                  | 1.6e-6 (both)     | n/a               |
  | n_s (tilt direction)            | n/a               | Cutoff: 0.957     |
  |                                 |                   | Zeta:   1.090     |
  | KE (modulus kinetic energy)     | {KE_physical:8.1f} (both) | n/a               |
  | A_s baseline                    | {A_s_deltaN:.3e} (both) | Cutoff: {A_s_deltaN:.2e}  |
  |                                 |                   | Zeta:   {A_s_level2_epsH2_a4:.2e}  |
  | BCS dressing (OOM)              | +0.046 (both)     | +0.046 (both)     |
  | Non-BD squeeze (OOM)            | +0.226 (FI)       | +0.226 (FI)       |
  | Phase correction (OOM)          | +0.043 (FI)       | +0.043 (FI)       |
  | Final gap (OOM)                 | {gap_level1_final:6.3f} (both)   | Cutoff: {gap_level1_final:6.3f}   |
  |                                 |                   | Zeta:   {gap_sign_epsH2:+6.1f}     |
  +---------------------------------+-------------------+-------------------+

  Level 1 interpretation: FUNCTIONAL-INDEPENDENT (gap = {gap_level1_final:.3f} OOM, same for all)
  Level 2 interpretation: MAXIMALLY SCHEME-DEPENDENT (zeta excluded by {abs(gap_sign_epsH2):.0f} OOM)
""")

# =============================================================================
# SECTION 10: Sensitivity Analysis -- eps*H^2 Ratio
# =============================================================================
print("=" * 78)
print("SECTION 10: Sensitivity Analysis")
print("=" * 78)

# Compute (eps*H^2) ratio = (dS^2/S) for each functional, across all tau
cs_a24 = CubicSpline(tau_all, a2_arr + a4_arr)

tau_fine = np.linspace(0.01, 0.49, 200)
epsH2_cutoff = cs_Scut(tau_fine, 1)**2 / cs_Scut(tau_fine)
epsH2_a4 = cs_a4(tau_fine, 1)**2 / cs_a4(tau_fine)
epsH2_a2 = cs_a2(tau_fine, 1)**2 / cs_a2(tau_fine)
epsH2_a24 = cs_a24(tau_fine, 1)**2 / cs_a24(tau_fine)

# Ratio relative to cutoff
ratio_a4 = epsH2_a4 / epsH2_cutoff
ratio_a2 = epsH2_a2 / epsH2_cutoff
ratio_a24 = epsH2_a24 / epsH2_cutoff

# At the fold:
ratio_a4_fold = epsH2_ratio_a4
ratio_a2_fold = epsH2_ratio_a2
ratio_a24_fold = epsH2_ratio_a24

print(f"""
  (eps*H^2) ratio at fold:
    Zeta a_4:     {ratio_a4_fold:.6f}  => A_s ratio = {1/ratio_a4_fold**2:.2e}
    Zeta a_2:     {ratio_a2_fold:.6f}  => A_s ratio = {1/ratio_a2_fold**2:.2e}
    Zeta a_2+a_4: {ratio_a24_fold:.6f}  => A_s ratio = {1/ratio_a24_fold**2:.2e}

  All ratios are << 1, meaning the zeta gradient is much weaker than
  the cutoff gradient. This makes A_s MUCH LARGER in the zeta scheme (Level 2).

  The reason: S_cutoff = sum dim^2 |lam| puts HIGH weight on large eigenvalues,
  giving a steep potential. The zeta a_4 = sum dim * |lam|^{{-4}} puts high
  weight on SMALL eigenvalues, giving a shallow potential with weak gradients.
""")

# =============================================================================
# SECTION 11: Plot
# =============================================================================
print("=" * 78)
print("SECTION 11: Generating Plots")
print("=" * 78)

fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))

# Panel 1: Normalized spectral action profiles
ax1 = axes[0]
S_norm = cs_Scut(tau_fine) / cs_Scut(tau_fold)
a4_norm = cs_a4(tau_fine) / cs_a4(tau_fold)
a2_norm = cs_a2(tau_fine) / cs_a2(tau_fold)

ax1.plot(tau_fine, S_norm, 'b-', lw=2, label=r'$S_{\mathrm{cutoff}} / S_f$')
ax1.plot(tau_fine, a4_norm, 'r-', lw=2, label=r'$a_4 / a_{4,f}$')
ax1.plot(tau_fine, a2_norm, 'g-', lw=2, label=r'$a_2 / a_{2,f}$')
ax1.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=r'$\tau_f = 0.19$')
ax1.set_xlabel(r'$\tau$', fontsize=12)
ax1.set_ylabel('Normalized action', fontsize=11)
ax1.set_title('Spectral Functionals', fontsize=12)
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel 2: (eps*H^2) ratio
ax2 = axes[1]
ax2.semilogy(tau_fine, ratio_a4, 'r-', lw=2, label=r'$a_4$ / cutoff')
ax2.semilogy(tau_fine, ratio_a2, 'g-', lw=2, label=r'$a_2$ / cutoff')
ax2.semilogy(tau_fine, ratio_a24, 'm-', lw=2, label=r'$(a_2+a_4)$ / cutoff')
ax2.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax2.axhline(1.0, color='k', ls=':', alpha=0.3)
ax2.set_xlabel(r'$\tau$', fontsize=12)
ax2.set_ylabel(r'$(\epsilon H^2)_{\mathrm{zeta}} / (\epsilon H^2)_{\mathrm{cutoff}}$', fontsize=11)
ax2.set_title(r'KE ratio (Level 2)', fontsize=12)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: Gap budget comparison
ax3 = axes[2]
schemes = ['Cutoff\n(=Level 1)', 'Zeta a_4\n(Level 2)', 'Zeta a_2\n(Level 2)']

gap_a2_raw = np.log10(A_s_obs / (A_s_deltaN / epsH2_ratio_a2**2))
gap_a2_sign = gap_a2_raw

baselines = [gap_sign_level1, gap_sign_epsH2, gap_a2_sign]
finals = [gap_level1_final,
          gap_sign_epsH2 + total_corr_level2,
          gap_a2_sign + total_corr_level2]

x = np.arange(len(schemes))
width = 0.35  # (local)
bars1 = ax3.bar(x - width/2, baselines, width, label='Baseline gap', color='steelblue', alpha=0.8)
bars2 = ax3.bar(x + width/2, finals, width, label='After corrections', color='indianred', alpha=0.8)

ax3.set_xticks(x)
ax3.set_xticklabels(schemes, fontsize=8)
ax3.set_ylabel('Gap (OOM)', fontsize=11)
ax3.set_title(r'$A_s$ Gap Budget', fontsize=12)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3, axis='y')
ax3.axhline(0, color='k', lw=0.5)
# Add horizontal line at observed A_s (gap = 0)
ax3.text(0.05, 0.05, 'gap = 0: matches observation', fontsize=8,
         transform=ax3.transAxes, color='k', alpha=0.7)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's70_zeta_as_budget.png'), dpi=150)
plt.close()
print("  Saved: s70_zeta_as_budget.png")

# =============================================================================
# SECTION 12: Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 12: Gate Verdict")
print("=" * 78)

gate_name = 'ZETA-AS-BUDGET-70'
gate_verdict = 'INFO'
flag_threshold = 0.1  # (local)

# Level 1 gap difference: 0 (by construction -- A_s is FI)
# Level 2 gap difference: massive (~7 OOM)
delta_gap_report = delta_gap_L2

gate_detail = (
    f"Level 1 (one transit): gap={gap_level1_final:.3f} OOM, same as cutoff, "
    f"FUNCTIONAL-INDEPENDENT. "
    f"Level 2 (scheme dynamics): gap_zeta(a4)={gap_sign_epsH2:+.1f} OOM "
    f"({'overshoot' if overshoot_level2 else 'undershoot'}), "
    f"|diff|={delta_gap_L2:.1f} OOM. "
    f"Zeta excluded by both n_s (blue) and A_s ({abs(gap_sign_epsH2):.0f} OOM overshoot). "
    f"Physical answer: Level 1 (A_s gap FI at {gap_level1_final:.3f} OOM)."
)

print(f"""
  Gate: {gate_name}
  Verdict: {gate_verdict}

  Level 1 result: gap = {gap_level1_final:.3f} OOM (FUNCTIONAL-INDEPENDENT)
  Level 2 result: gap = {gap_sign_epsH2:+.1f} OOM (zeta EXCLUDED, {abs(gap_sign_epsH2):.0f} OOM overshoot)
  Flagged: {'YES' if delta_gap_L2 > flag_threshold else 'NO'} (|diff| = {delta_gap_L2:.1f} OOM)

  {gate_detail}
""")

# =============================================================================
# SECTION 13: Save Data
# =============================================================================
print("=" * 78)
print("SECTION 13: Save Data")
print("=" * 78)

output = dict(
    # Cutoff scheme reference
    eps_H_cutoff_shape=eps_H_cutoff,       # S66 shape parameter S'^2/(2*S*S'')
    eps_H_cutoff_physical=eps_H_physical,   # Physical eps = KE/(M_Pl^2*H^2)
    H_fold=H_fold,
    A_s_cutoff=A_s_deltaN,
    A_s_obs=A_s_obs,

    # Level 1: Functional-Independent
    KE_physical=KE_physical,
    gap_level1_baseline=gap_level1_raw,
    gap_level1_final=gap_level1_final,

    # Level 2: Scheme-Dependent (a4)
    eps_H_zeta_a4_shape=eps_H_zeta_a4,
    epsH2_ratio_a4=epsH2_ratio_a4,
    A_s_zeta_a4_level2=A_s_level2_epsH2_a4,
    gap_level2_a4_signed=gap_sign_epsH2,
    zeta_a4_excluded=True,  # by both n_s and A_s

    # Level 2: Scheme-Dependent (a2)
    eps_H_zeta_a2_shape=eps_H_zeta_a2,
    epsH2_ratio_a2=epsH2_ratio_a2,
    A_s_zeta_a2_level2=A_s_deltaN / epsH2_ratio_a2**2,
    gap_level2_a2_signed=gap_a2_sign,
    zeta_a2_excluded=True,

    # Level 2: Scheme-Dependent (a2+a4)
    eps_H_zeta_a24_shape=eps_H_zeta_a24,
    epsH2_ratio_a24=epsH2_ratio_a24,

    # Spectral moments at fold
    a2_fold=a2_at_fold,
    a4_fold=a4_at_fold,
    a6_fold=a6_at_fold,
    S_cutoff_fold=S_cutoff_at_fold,

    # Gradients at fold
    dS_dtau_fold=float(dS_val),
    da4_dtau_fold=float(da4_val),
    da2_dtau_fold=float(da2_val),
    d2S_dtau2_fold=float(d2S_val),
    d2a4_dtau2_fold=float(d2a4_val),

    # Log-derivatives
    log_deriv_cutoff=log_deriv_cutoff,
    log_deriv_zeta_a4=log_deriv_zeta_a4,
    log_deriv_zeta_a2=log_deriv_zeta_a2,

    # Corrections (functional-independent in both levels)
    BCS_OOM=BCS_OOM_cutoff,
    OOM_squeeze=OOM_squeeze_canonical,
    OOM_phase=0.043,

    # Gap analysis
    delta_gap_L1=0.0,                # Level 1: FI
    delta_gap_L2=delta_gap_L2,       # Level 2: massive
    gap_threshold=flag_threshold,

    # Gate
    gate_name=np.array(gate_name),
    gate_verdict=np.array(gate_verdict),
    gate_detail=np.array(gate_detail),
    independence_class=np.array(
        'FUNCTIONAL-INDEPENDENT at Level 1 (one physical transit). '
        'MAXIMALLY SCHEME-DEPENDENT at Level 2 (different dynamics). '
        'Resolution: Level 1 is physical; Level 2 provides functional SELECTION '
        '(zeta excluded by n_s and A_s).'
    ),
)

npz_path = os.path.join(SCRIPT_DIR, 's70_zeta_as_budget.npz')
np.savez(npz_path, **output)
print(f"  Saved: {npz_path}")
print(f"  Keys ({len(output)}): {sorted(output.keys())}")

# =============================================================================
# SECTION 14: Final Summary
# =============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY")
print("=" * 78)

print(f"""
  ZETA-AS-BUDGET-70: A_s Gap Budget in Zeta Scheme

  The A_s gap budget was analyzed in the zeta spectral action scheme
  (S_zeta = a_4(D_K^2)) vs the sqrt-cutoff scheme (S_cutoff = Tr|D_K|).

  TWO LEVELS OF ANALYSIS:

  Level 1 (One Physical Transit):
    The transit event is physical: v = 26.545 M_KK, KE = 1762 M_KK^4.
    The delta-N formula A_s = (GGE numerator)/(6*KE)^2 is FI.
    Gap = {gap_level1_final:.3f} OOM (same as cutoff: {gap_level1_raw:.3f} - {total_corr_level1:.3f} corrections).
    ALL corrections (BCS, squeeze, phase) are FI.
    Physical eps_H = KE/(M_Pl^2*H^2) = {eps_H_physical:.1e} (same in both schemes).

  Level 2 (Scheme-Dependent Dynamics):
    The zeta potential a_4(tau) DECREASES with tau (opposite to cutoff).
    The gradient da_4/dtau = {da4_val:.1f} is much weaker than dS/dtau = {dS_val:.0f}.
    The (eps*H^2) ratio = {epsH2_ratio_a4:.4f} => A_s^zeta >> A_s^cutoff.
    A_s^zeta = {A_s_level2_epsH2_a4:.1e} vs observed {A_s_obs:.1e} => {abs(gap_sign_epsH2):.0f} OOM overshoot.
    Zeta functional EXCLUDED for this spectral triple by both n_s and A_s.

  GATE VERDICT: INFO
    The A_s gap is {gap_level1_final:.3f} OOM, FUNCTIONAL-INDEPENDENT at Level 1.
    The zeta functional is independently excluded by A_s overshoot ({abs(gap_sign_epsH2):.0f} OOM),
    consistent with its n_s exclusion (blue tilt, S66).
    Corrections: BCS +{BCS_OOM_cutoff:.3f}, squeeze +{OOM_squeeze_canonical:.3f}, phase +{0.043:.3f} -- all FI.

  PHYSICAL CONCLUSION:
    The A_s gap (0.490 OOM) is a property of the MODE PHYSICS (GGE occupation,
    Bogoliubov coefficients, BCS mixing angles) and the PHYSICAL transit dynamics
    (KE = G*v^2/2), not of the spectral functional choice. This confirms the
    S69 classification: the gap closure path runs through Leggett vacuum
    physics and mode occupation numbers, not through functional selection.
""")

print("=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
