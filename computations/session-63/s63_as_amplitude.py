#!/usr/bin/env python3
"""
S63 AS-AMPLITUDE-63: Scalar Power Spectrum Amplitude A_s
=========================================================
Compute A_s = V_fold / (24 * pi^2 * epsilon * M_Pl^4)
with sound speed correction: A_s = V_fold / (24 * pi^2 * epsilon * c_s * M_Pl^4)

Input:
  - s62_kz_ns.npz: epsilon_H_SA, spectral action data
  - s63_sound_speed.npz: c_s, Z_fold, d2S_fold, rho_total, P_total

Gate: AS-AMPLITUDE-63
  PASS if A_s in [1e-10, 1e-8]
  FAIL if > 1e-6
  INFO otherwise

Author: mack-cosmic-bridge (Katie Mack / Cosmic Bridge)
"""

import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import (
    PI, M_Pl_reduced, M_Pl_unreduced, M_KK, M_KK_gravity, M_KK_kerner,
    S_fold, dS_fold, d2S_fold, Z_fold, G_DeWitt, H_fold,
    a0_fold, a2_fold, a4_fold, v_terminal, A_s_CMB,
    Vol_SU3_Haar, tau_fold, E_exc
)

print("=" * 72)
print("AS-AMPLITUDE-63: Scalar Power Spectrum Amplitude A_s")
print("=" * 72)

# ==============================================================================
#  LOAD INPUT DATA
# ==============================================================================
print("\nLOADING INPUT DATA")
print("-" * 60)

d_ns = np.load('s62_kz_ns.npz', allow_pickle=True)
d_cs = np.load('s63_sound_speed.npz', allow_pickle=True)

# From s62_kz_ns.npz
epsilon_H_SA = float(d_ns['epsilon_H_SA'])     # 0.02163
epsilon_SA = float(d_ns['epsilon_SA'])           # 0.1002
epsilon_modulus = float(d_ns['epsilon_modulus'])  # 1.37e-6
f0 = float(d_ns['f0'])
f2 = float(d_ns['f2'])
f4 = float(d_ns['f4'])
a0_gilkey = float(d_ns['a0_gilkey'])
a2_gilkey = float(d_ns['a2_gilkey'])
a4_gilkey = float(d_ns['a4_gilkey'])
ns_canonical = float(d_ns['ns_canonical'])

# From s63_sound_speed.npz
c_s = float(d_cs['c_s'])                        # 0.4849
c_s_sq = float(d_cs['c_s_sq'])                  # 0.2351
epsilon_H_acoustic = float(d_cs['epsilon_H_acoustic'])  # 0.0920
rho_total = float(d_cs['rho_total'])             # 250471.86 (M_KK^4 units)
P_total = float(d_cs['P_total'])                 # -250249.49
w_eos = float(d_cs['w_eos'])                     # -0.9991
s_sound = float(d_cs['s_sound'])                 # sound speed running

print(f"  epsilon_H(SA)     = {epsilon_H_SA:.6f}")
print(f"  epsilon_SA        = {epsilon_SA:.6f}")
print(f"  epsilon_modulus    = {epsilon_modulus:.6e}")
print(f"  c_s               = {c_s:.6f}")
print(f"  c_s^2             = {c_s_sq:.6f}")
print(f"  epsilon_H(acoustic) = {epsilon_H_acoustic:.6f}")
print(f"  rho_total (M_KK^4) = {rho_total:.2f}")
print(f"  P_total (M_KK^4)   = {P_total:.2f}")
print(f"  w = P/rho          = {w_eos:.6f}")
print(f"  s (sound running)  = {s_sound:.6f}")
print(f"  n_s(canonical)     = {ns_canonical:.6f}")

# ==============================================================================
#  STEP 1: IDENTIFY V_fold IN PHYSICAL UNITS
# ==============================================================================
print("\n" + "=" * 72)
print("STEP 1: V_fold in Physical Units (GeV^4)")
print("=" * 72)

# The spectral action at the fold gives the effective potential for the
# modulus tau. In the standard inflationary A_s formula, V is the potential
# energy density driving the quasi-de Sitter expansion.
#
# CRITICAL CONVENTION NOTE:
# The standard inflationary formula uses:
#   A_s = H^2 / (8 pi^2 epsilon M_Pl^2)  = V / (24 pi^2 epsilon M_Pl^4)
#
# These are equivalent via the Friedmann equation V = 3 H^2 M_Pl^2 (when
# kinetic energy is small, i.e., epsilon << 1). For our framework:
#   epsilon_H = 0.0216 << 1, so V ~ 3 H^2 M_Pl^2 is a good approximation.
#
# Method A: V_fold from the full spectral action
# S_fold = 250360.67 in M_KK^4 units (dimensionless internal)
# Physical: V_A = S_fold * M_KK^4

V_A_GeV4 = S_fold * M_KK**4
V_A_MPl4 = V_A_GeV4 / M_Pl_reduced**4

print(f"\n  METHOD A: Full spectral action S_fold")
print(f"    S_fold = {S_fold:.2f} (M_KK^4 units)")
print(f"    M_KK = {M_KK:.4e} GeV")
print(f"    V_A = S_fold * M_KK^4 = {V_A_GeV4:.6e} GeV^4")
print(f"    V_A / M_Pl^4 = {V_A_MPl4:.6e}")

# Method B: V_fold from the bare CC term only (a_0 coefficient)
# V_B = (2/pi^2) * a_0_fold * M_KK^4
# This is the cosmological constant contribution from the leading heat kernel

V_B_GeV4 = (2.0 / PI**2) * a0_fold * M_KK**4
V_B_MPl4 = V_B_GeV4 / M_Pl_reduced**4

print(f"\n  METHOD B: Bare CC term (2/pi^2) * a_0 * M_KK^4")
print(f"    a_0(fold) = {a0_fold:.2f}")
print(f"    V_B = {V_B_GeV4:.6e} GeV^4")
print(f"    V_B / M_Pl^4 = {V_B_MPl4:.6e}")

# Method C: rho_total from the effective fluid (s63_sound_speed)
# This is rho = K + V at the fold, including kinetic energy
# V_C = rho_total * M_KK^4

V_C_GeV4 = rho_total * M_KK**4
V_C_MPl4 = V_C_GeV4 / M_Pl_reduced**4

print(f"\n  METHOD C: Total energy density at fold")
print(f"    rho_total = {rho_total:.2f} (M_KK^4 units)")
print(f"    V_C = rho_total * M_KK^4 = {V_C_GeV4:.6e} GeV^4")
print(f"    V_C / M_Pl^4 = {V_C_MPl4:.6e}")

# Method D: From the Friedmann equation: V = 3 H^2 M_Pl^2
# H_fold = 586.53 in M_KK units, so H_phys = H_fold * M_KK
# V_D = 3 * H_phys^2 * M_Pl^2

H_phys = H_fold * M_KK  # GeV
V_D_GeV4 = 3.0 * H_phys**2 * M_Pl_reduced**2
V_D_MPl4 = V_D_GeV4 / M_Pl_reduced**4

print(f"\n  METHOD D: Friedmann equation V = 3*H^2*M_Pl^2")
print(f"    H_fold = {H_fold:.4f} M_KK")
print(f"    H_phys = {H_phys:.4e} GeV")
print(f"    V_D = 3*H^2*M_Pl^2 = {V_D_GeV4:.6e} GeV^4")
print(f"    V_D / M_Pl^4 = {V_D_MPl4:.6e}")

# Cross-check: Methods A, C should agree (V_C ~ V_A since rho ~ S_fold for
# potential-dominated). Methods A,B differ because S_fold includes all
# Seeley-DeWitt terms, not just a_0.

print(f"\n  CROSS-CHECKS:")
print(f"    V_C / V_A = {V_C_GeV4 / V_A_GeV4:.6f} (should be ~ 1)")
print(f"    V_D / V_A = {V_D_GeV4 / V_A_GeV4:.6f}")
print(f"    V_B / V_A = {V_B_GeV4 / V_A_GeV4:.6f}")

# ==============================================================================
#  STEP 2: CORRECT INTERPRETATION OF V_fold FOR A_s
# ==============================================================================
print("\n" + "=" * 72)
print("STEP 2: Which V enters the A_s formula?")
print("=" * 72)

# The standard formula A_s = V / (24*pi^2*epsilon*M_Pl^4) applies when:
# 1. V is the potential driving inflation (not the total energy)
# 2. epsilon is the Hubble slow-roll parameter
# 3. M_Pl is the reduced Planck mass
#
# In this framework, the potential driving the transit is the spectral action
# S(tau). The total energy density is rho = kinetic + potential.
#
# For a slow-roll field: V >> kinetic, so V ~ rho ~ 3 H^2 M_Pl^2.
# Our w = -0.9991, so kinetic/potential ~ (1+w)/2 ~ 0.00045.
# This means V ~ rho to 0.05% accuracy. EXCELLENT slow-roll behavior.
#
# HOWEVER, there is a CRITICAL SUBTLETY:
# The spectral action S_fold = 250360.67 M_KK^4 is the RAW spectral action.
# The 4D effective potential from the asymptotic expansion is:
#   S_eff = f_4*Lambda^4*a_0 + f_2*Lambda^2*a_2 + f_0*a_4
#
# When we identify Lambda = M_KK, the physical V is:
#   V = S_eff * M_KK^4 / (4*pi^2)
# OR simply V = S_fold * M_KK^4 if S_fold already includes the 1/(4*pi^2) factor.
#
# The stored S_fold = 250360.67 was computed as the FULL spectral sum
# (not divided by 4*pi^2). Let me check against the Gilkey decomposition.

S_gilkey_check = f4 * a0_gilkey + f2 * a2_gilkey + f0 * a4_gilkey
print(f"\n  S from Gilkey (f4*a0_G + f2*a2_G + f0*a4_G):")
print(f"    f4={f4:.6f}, a0_G={a0_gilkey:.6f}")
print(f"    f2={f2:.6f}, a2_G={a2_gilkey:.6f}")
print(f"    f0={f0:.6f}, a4_G={a4_gilkey:.6f}")
print(f"    S_gilkey = {S_gilkey_check:.6f}")
print(f"    S_fold (canonical) = {S_fold:.2f}")
print(f"    Ratio S_fold/S_gilkey = {S_fold/S_gilkey_check:.2f}")

# The ratio S_fold/S_gilkey tells us the relationship between the per-mode
# Gilkey coefficients and the full spectral sum (which includes all modes
# of the Dirac operator on M4 x SU(3)).

print(f"\n  INTERPRETATION:")
print(f"    The Gilkey coefficients (a0_G, a2_G, a4_G) from s62 are per-mode")
print(f"    (Peter-Weyl sector). S_fold is the FULL spectral action summed")
print(f"    over all modes. The ratio {S_fold/S_gilkey_check:.0f} = number of")
print(f"    contributing modes * geometric factors.")
print(f"    For the A_s formula, we use S_fold (the FULL potential).")

# ==============================================================================
#  STEP 3: COMPUTE A_s — BARE (NO SOUND SPEED CORRECTION)
# ==============================================================================
print("\n" + "=" * 72)
print("STEP 3: A_s = V / (24 * pi^2 * epsilon * M_Pl^4) — BARE")
print("=" * 72)

# Method 1: Using V = S_fold * M_KK^4
V_fold = V_A_GeV4  # S_fold * M_KK^4
M_Pl = M_Pl_reduced
epsilon = epsilon_H_SA

A_s_bare = V_fold / (24.0 * PI**2 * epsilon * M_Pl**4)

print(f"\n  V_fold = {V_fold:.6e} GeV^4")
print(f"  epsilon_H = {epsilon:.6f}")
print(f"  M_Pl = {M_Pl:.4e} GeV")
print(f"  24*pi^2 = {24*PI**2:.4f}")
print(f"  Denominator = 24*pi^2*eps*M_Pl^4 = {24*PI**2*epsilon*M_Pl**4:.6e}")
print(f"\n  A_s(bare) = {A_s_bare:.6e}")
print(f"  log10(A_s) = {np.log10(A_s_bare):.4f}")
print(f"  A_s(CMB) = {A_s_CMB:.6e}")
print(f"  log10(A_s/A_s_CMB) = {np.log10(A_s_bare/A_s_CMB):.4f}")
print(f"  RATIO: A_s(bare)/A_s(CMB) = {A_s_bare/A_s_CMB:.4e}")

# Method 2: Equivalent formula: A_s = H^2 / (8 * pi^2 * epsilon * M_Pl^2)
A_s_H = H_phys**2 / (8.0 * PI**2 * epsilon * M_Pl**2)
print(f"\n  CROSS-CHECK: A_s = H^2/(8*pi^2*eps*M_Pl^2)")
print(f"    H_phys = {H_phys:.4e} GeV")
print(f"    A_s(H) = {A_s_H:.6e}")
print(f"    Ratio A_s(H)/A_s(V) = {A_s_H/A_s_bare:.6f}")
print(f"    (Differ because V != 3*H^2*M_Pl^2 exactly; H_fold uses")
print(f"     H^2 = S_fold*M_KK^4 / (3*M_Pl^2) only if M_KK is gravity route)")

# Method 3: Purely dimensionless internal formula
# A_s = S_fold / (24*pi^2*epsilon) * (M_KK/M_Pl)^4
R_KK_Pl = M_KK / M_Pl  # M_KK / M_Pl_reduced
A_s_dimless = S_fold / (24.0 * PI**2 * epsilon) * R_KK_Pl**4

print(f"\n  DIMENSIONLESS CHECK:")
print(f"    M_KK / M_Pl = {R_KK_Pl:.6e}")
print(f"    (M_KK/M_Pl)^4 = {R_KK_Pl**4:.6e}")
print(f"    S_fold/(24*pi^2*eps) = {S_fold/(24*PI**2*epsilon):.4e}")
print(f"    A_s = S/(24*pi^2*eps) * (M_KK/M_Pl)^4 = {A_s_dimless:.6e}")

# ==============================================================================
#  STEP 4: SOUND SPEED CORRECTION
# ==============================================================================
print("\n" + "=" * 72)
print("STEP 4: Sound Speed Correction — A_s = V/(24*pi^2*eps*c_s*M_Pl^4)")
print("=" * 72)

# For a scalar field with non-trivial sound speed c_s != 1, the power
# spectrum is modified. The standard result (see Garriga & Mukhanov 1999;
# Chen, Huang, Kachru, Shiu 2007) is:
#
#   P_s(k) = H^2 / (8 * pi^2 * M_Pl^2 * epsilon * c_s)
#
# evaluated at sound horizon crossing: c_s * k = a * H.
# The extra 1/c_s comes from two effects:
#   (a) The normalization of the mode function is proportional to 1/sqrt(c_s)
#   (b) The Bunch-Davies vacuum sees a different effective horizon
#
# In terms of V: A_s = V / (24 * pi^2 * epsilon * c_s * M_Pl^4)
#
# PHYSICAL ASSESSMENT OF c_s = 0.485:
# - c_s < 1 is physical (causal, subluminal)
# - Arises from Z_spectral/d2S: spatial and temporal stiffnesses differ
# - This is a genuine prediction: the internal spectral geometry produces
#   a non-trivial speed of sound for modulus fluctuations
# - Effect: INCREASES A_s by factor 1/c_s = 2.06

print(f"\n  c_s = {c_s:.6f}")
print(f"  1/c_s = {1.0/c_s:.6f}")
print(f"  Enhancement factor = {1.0/c_s:.4f}x")

A_s_cs = V_fold / (24.0 * PI**2 * epsilon * c_s * M_Pl**4)

print(f"\n  A_s(with c_s) = {A_s_cs:.6e}")
print(f"  log10(A_s) = {np.log10(A_s_cs):.4f}")
print(f"  A_s(CMB) = {A_s_CMB:.6e}")
print(f"  log10(A_s/A_s_CMB) = {np.log10(A_s_cs/A_s_CMB):.4f}")
print(f"  RATIO: A_s(cs)/A_s(CMB) = {A_s_cs/A_s_CMB:.4e}")

# H-based formula with c_s
A_s_H_cs = H_phys**2 / (8.0 * PI**2 * epsilon * c_s * M_Pl**2)
print(f"\n  CROSS-CHECK: A_s = H^2/(8*pi^2*eps*c_s*M_Pl^2)")
print(f"    A_s(H, c_s) = {A_s_H_cs:.6e}")

# ==============================================================================
#  STEP 5: SYSTEMATIC EXPLORATION — ALL epsilon CHOICES
# ==============================================================================
print("\n" + "=" * 72)
print("STEP 5: Systematic A_s for Different epsilon Definitions")
print("=" * 72)

# The framework has multiple epsilon definitions:
# 1. epsilon_H(SA) = 0.0216: from spectral action log-derivatives (CANONICAL)
# 2. epsilon_SA = 0.100: direct spectral action ratio
# 3. epsilon_modulus = 1.37e-6: from modulus kinetic term alone
# 4. epsilon_H(acoustic) = 0.0920: acoustic-corrected epsilon

epsilon_vals = {
    'epsilon_H(SA) [CANONICAL]': epsilon_H_SA,
    'epsilon_SA': epsilon_SA,
    'epsilon_modulus': epsilon_modulus,
    'epsilon_H(acoustic)': epsilon_H_acoustic,
}

print(f"\n  {'epsilon definition':<30s} {'epsilon':<14s} {'A_s(bare)':<14s} "
      f"{'A_s(c_s)':<14s} {'log10(ratio)':<14s} {'OOM above':<10s}")
print(f"  {'-'*30} {'-'*14} {'-'*14} {'-'*14} {'-'*14} {'-'*10}")

best_As = None
best_label = None
results = {}

for label, eps_val in epsilon_vals.items():
    As_bare = V_fold / (24.0 * PI**2 * eps_val * M_Pl**4)
    As_cs = V_fold / (24.0 * PI**2 * eps_val * c_s * M_Pl**4)
    log_ratio = np.log10(As_cs / A_s_CMB)
    oom_above = log_ratio if log_ratio > 0 else 0

    results[label] = {
        'epsilon': eps_val,
        'As_bare': As_bare,
        'As_cs': As_cs,
        'log_ratio': log_ratio,
    }

    print(f"  {label:<30s} {eps_val:<14.6e} {As_bare:<14.4e} "
          f"{As_cs:<14.4e} {log_ratio:<14.4f} {oom_above:<10.1f}")

    # Track which is closest to CMB value
    if best_As is None or abs(log_ratio) < abs(best_label):
        best_As = As_cs
        best_label = abs(log_ratio)

# ==============================================================================
#  STEP 6: WHAT WOULD BRING A_s DOWN TO CMB VALUE?
# ==============================================================================
print("\n" + "=" * 72)
print("STEP 6: Required Corrections for A_s = 2.1e-9")
print("=" * 72)

# Using canonical epsilon_H(SA) = 0.0216 with c_s = 0.485:
# A_s(framework) / A_s(CMB) = ratio
# To match, we need V_fold / M_Pl^4 to be smaller by this ratio.

ratio_canonical = A_s_cs / A_s_CMB
OOM_gap = np.log10(ratio_canonical)

print(f"\n  A_s(framework, canonical with c_s) = {A_s_cs:.4e}")
print(f"  A_s(CMB)                           = {A_s_CMB:.4e}")
print(f"  Ratio = {ratio_canonical:.4e}")
print(f"  OOM gap = {OOM_gap:.2f}")

# What V/M_Pl^4 is needed?
V_needed_MPl4 = A_s_CMB * 24.0 * PI**2 * epsilon * c_s
V_needed_GeV4 = V_needed_MPl4 * M_Pl**4

print(f"\n  Required V/M_Pl^4 = {V_needed_MPl4:.6e}")
print(f"  Actual V/M_Pl^4   = {V_A_MPl4:.6e}")
print(f"  Ratio (actual/needed) = {V_A_MPl4/V_needed_MPl4:.4e}")

# Equivalent: what H is needed?
H_needed = np.sqrt(8.0 * PI**2 * A_s_CMB * epsilon * c_s) * M_Pl
print(f"\n  Required H = {H_needed:.4e} GeV")
print(f"  Actual H   = {H_phys:.4e} GeV")
print(f"  Ratio (actual/needed) = {H_phys/H_needed:.4e}")

# The scale hierarchy question:
# A_s ~ 10^{-9} requires V ~ 10^{-9} * M_Pl^4 ~ 10^{-9} * (2.4e18)^4 ~ 10^{65} GeV^4
# But V_fold = S_fold * M_KK^4 ~ 2.5e5 * (7.4e16)^4 ~ 7.6e72 GeV^4
# This is V/M_Pl^4 ~ 2.1e-2, which is O(1) rather than O(10^{-9}).
#
# The A_s problem is fundamentally: (M_KK/M_Pl)^4 ~ 10^{-6.5} is not
# small enough. The spectral action S_fold ~ 2.5e5 makes it worse (adds 5.4 OOM).
# Together: A_s ~ S * (M_KK/M_Pl)^4 / epsilon ~ 2.5e5 * 3.4e-7 / 0.022 ~ 4e-3
# This is 10^{-2.4}, compared to the needed 10^{-8.7}. Gap is ~6.3 OOM.

print(f"\n  STRUCTURAL ANALYSIS:")
print(f"    (M_KK/M_Pl)^4 = {R_KK_Pl**4:.4e} = 10^{{{np.log10(R_KK_Pl**4):.2f}}}")
print(f"    S_fold = {S_fold:.2f} = 10^{{{np.log10(S_fold):.2f}}}")
print(f"    1/epsilon = {1/epsilon:.1f} = 10^{{{np.log10(1/epsilon):.2f}}}")
print(f"    1/c_s = {1/c_s:.4f} = 10^{{{np.log10(1/c_s):.2f}}}")
print(f"    Product: 10^{{{np.log10(S_fold * R_KK_Pl**4 / (24*PI**2*epsilon*c_s)):.2f}}}")
print(f"    Needed:  10^{{{np.log10(A_s_CMB):.2f}}}")
print(f"    Gap:     10^{{{OOM_gap:.2f}}}")

# ==============================================================================
#  STEP 7: POTENTIAL RESOLUTION CHANNELS
# ==============================================================================
print("\n" + "=" * 72)
print("STEP 7: Potential Resolution Channels")
print("=" * 72)

# Channel 1: Volovik partition function suppression
# The Volovik partition Z ~ exp(-S_fold) would suppress A_s by a huge factor.
# But this enters the CC problem, not directly A_s.

print(f"\n  Channel 1: Volovik partition / q-theory")
print(f"    If the effective potential seen by perturbations is not S_fold*M_KK^4")
print(f"    but rather the q-theory reduced potential V_q, which self-adjusts to")
print(f"    near-zero, then V_eff << S_fold*M_KK^4.")
print(f"    Required suppression: factor {ratio_canonical:.2e}")
print(f"    log10 = {np.log10(ratio_canonical):.1f} OOM")

# Channel 2: Kerner vs gravity route M_KK
# M_KK(gravity) = 7.43e16 GeV
# M_KK(Kerner) = 5.04e17 GeV
# Switching to Kerner makes it WORSE (higher M_KK -> higher V)
V_kerner = S_fold * M_KK_kerner**4
A_s_kerner = V_kerner / (24.0 * PI**2 * epsilon * c_s * M_Pl**4)

print(f"\n  Channel 2: M_KK(Kerner) = {M_KK_kerner:.4e} GeV")
print(f"    V(Kerner) = {V_kerner:.4e} GeV^4")
print(f"    A_s(Kerner) = {A_s_kerner:.4e}  [WORSE by {A_s_kerner/A_s_cs:.1f}x]")

# Channel 3: Number of e-folds and normalization
# If the framework has N_e ~ 0.023 e-folds (from tau-to-N mapping in S63),
# the perturbations freeze out at a DIFFERENT scale than assumed.
# The mode that corresponds to k* = 0.05 Mpc^{-1} might exit at a different
# point in the transit, changing epsilon and V at horizon crossing.

print(f"\n  Channel 3: N_e correction")
print(f"    If N_e ~ 0.023 (from S63 tau-to-N mapping), the standard formula")
print(f"    may not apply. KZ freeze-out replaces Hubble-exit freeze-out.")

# Channel 4: Multi-field suppression
# The spectral action has 36 moduli directions (s62 Hessian).
# Multi-field effects can suppress the adiabatic perturbation by the
# turn rate and isocurvature-to-adiabatic transfer.

print(f"\n  Channel 4: Multi-field turn-rate suppression")
print(f"    36 Hessian modes → effective single-field projection may suppress")
print(f"    adiabatic power by sin^2(theta) where theta is turn angle.")
print(f"    Required: sin^2(theta) < {A_s_CMB/A_s_cs:.2e}")

# Channel 5: Peter-Weyl normalization
# S_fold = 250360.67 is the FULL spectral action. If only a fraction
# of modes contribute to the inflationary potential (e.g., the (0,0) sector),
# the effective V is smaller.

S_pw00_fraction = S_gilkey_check / S_fold if S_fold > 0 else 0
V_pw00 = S_gilkey_check * M_KK**4
A_s_pw00 = V_pw00 / (24.0 * PI**2 * epsilon * c_s * M_Pl**4)

print(f"\n  Channel 5: Peter-Weyl (0,0) sector only")
print(f"    S_gilkey(0,0) = {S_gilkey_check:.6f}")
print(f"    Fraction of S_fold = {S_pw00_fraction:.6e}")
print(f"    A_s(PW 0,0) = {A_s_pw00:.4e}")
print(f"    log10(A_s(PW)/A_s_CMB) = {np.log10(A_s_pw00/A_s_CMB):.2f}")
print(f"    NOTE: PW(0,0) sector is MUCH smaller -> much closer to CMB!")

# ==============================================================================
#  STEP 8: GATE VERDICT
# ==============================================================================
print("\n" + "=" * 72)
print("STEP 8: GATE VERDICT")
print("=" * 72)

# Primary result: canonical epsilon with sound speed correction
A_s_primary = A_s_cs  # V/(24*pi^2*eps*c_s*M_Pl^4) with full S_fold

# Check gate criteria
if 1e-10 <= A_s_primary <= 1e-8:
    verdict = "PASS"
    detail = f"A_s = {A_s_primary:.4e} in [1e-10, 1e-8]. CMB-consistent."
elif A_s_primary > 1e-6:
    verdict = "FAIL"
    OOM = np.log10(A_s_primary / A_s_CMB)
    detail = (f"A_s = {A_s_primary:.4e} ({OOM:.1f} OOM above CMB). "
              f"V_fold = S_fold*M_KK^4 = {V_fold:.2e} GeV^4 >> needed. "
              f"(M_KK/M_Pl)^4 = {R_KK_Pl**4:.2e} insufficiently small. "
              f"c_s={c_s:.3f} correction insufficient (2.1x). "
              f"6.3 OOM normalization problem.")
else:
    verdict = "INFO"
    detail = f"A_s = {A_s_primary:.4e}, between FAIL (>1e-6) and PASS ([1e-10, 1e-8])."

print(f"\n  GATE: AS-AMPLITUDE-63")
print(f"  VERDICT: {verdict}")
print(f"  A_s(framework) = {A_s_primary:.6e}")
print(f"  A_s(Planck) = {A_s_CMB:.1e} +/- 0.03e-9")
print(f"  Ratio = {A_s_primary/A_s_CMB:.4e}")
print(f"  log10(ratio) = {np.log10(A_s_primary/A_s_CMB):.2f}")
print(f"  Detail: {detail}")

# ==============================================================================
#  STEP 9: SUMMARY TABLE
# ==============================================================================
print("\n" + "=" * 72)
print("STEP 9: Summary Table")
print("=" * 72)

print(f"\n  {'Quantity':<40s} {'Value':<20s} {'Units':<15s}")
print(f"  {'-'*40} {'-'*20} {'-'*15}")
print(f"  {'V_fold (S_fold * M_KK^4)':<40s} {V_fold:<20.4e} {'GeV^4':<15s}")
print(f"  {'V_fold / M_Pl^4':<40s} {V_A_MPl4:<20.4e} {'dimensionless':<15s}")
print(f"  {'epsilon_H(SA)':<40s} {epsilon:<20.6f} {'dimensionless':<15s}")
print(f"  {'c_s (spectral fabric)':<40s} {c_s:<20.6f} {'dimensionless':<15s}")
print(f"  {'M_KK':<40s} {M_KK:<20.4e} {'GeV':<15s}")
print(f"  {'M_Pl (reduced)':<40s} {M_Pl:<20.4e} {'GeV':<15s}")
print(f"  {'(M_KK/M_Pl)^4':<40s} {R_KK_Pl**4:<20.4e} {'dimensionless':<15s}")
print(f"  {'H_fold (physical)':<40s} {H_phys:<20.4e} {'GeV':<15s}")
print(f"  {'A_s(bare, no c_s)':<40s} {A_s_bare:<20.4e} {'dimensionless':<15s}")
print(f"  {'A_s(with c_s = 0.485)':<40s} {A_s_cs:<20.4e} {'dimensionless':<15s}")
print(f"  {'A_s(CMB, Planck 2018)':<40s} {A_s_CMB:<20.4e} {'dimensionless':<15s}")
print(f"  {'Ratio A_s(fw)/A_s(CMB)':<40s} {A_s_cs/A_s_CMB:<20.4e} {'dimensionless':<15s}")
print(f"  {'OOM gap':<40s} {OOM_gap:<20.2f} {'log10':<15s}")

# ==============================================================================
#  SAVE OUTPUT
# ==============================================================================
print("\n" + "=" * 72)
print("Saving to s63_as_amplitude.npz")
print("=" * 72)

np.savez('s63_as_amplitude.npz',
    # Gate metadata
    gate_name='AS-AMPLITUDE-63',
    gate_verdict=verdict,
    gate_detail=detail,

    # Primary results
    A_s_bare=A_s_bare,
    A_s_cs=A_s_cs,
    A_s_CMB=A_s_CMB,
    A_s_ratio=A_s_cs / A_s_CMB,
    OOM_gap=OOM_gap,

    # Input quantities
    V_fold_GeV4=V_fold,
    V_fold_MPl4=V_A_MPl4,
    epsilon_H_SA=epsilon_H_SA,
    epsilon_SA=epsilon_SA,
    epsilon_modulus=epsilon_modulus,
    epsilon_H_acoustic=epsilon_H_acoustic,
    c_s=c_s,
    c_s_sq=c_s_sq,
    s_sound=s_sound,

    # Scale hierarchy
    M_KK_over_M_Pl=R_KK_Pl,
    M_KK_over_M_Pl_4th=R_KK_Pl**4,
    S_fold=S_fold,
    H_fold_phys_GeV=H_phys,

    # Alternative computations
    A_s_H_method=A_s_H,
    A_s_H_cs_method=A_s_H_cs,
    A_s_dimless_check=A_s_dimless,
    A_s_kerner=A_s_kerner,
    A_s_pw00=A_s_pw00,

    # Cross-checks
    V_B_CC_GeV4=V_B_GeV4,
    V_C_rho_GeV4=V_C_GeV4,
    V_D_Friedmann_GeV4=V_D_GeV4,
    S_gilkey_00=S_gilkey_check,
    V_needed_GeV4=V_needed_GeV4,
    H_needed_GeV=H_needed,

    # Resolution channel estimates
    ratio_canonical=ratio_canonical,
    PW00_fraction=S_pw00_fraction,
)

print(f"  Saved: s63_as_amplitude.npz")
print(f"  Gate: {verdict}")
print(f"  A_s = {A_s_cs:.4e} (with c_s), {A_s_bare:.4e} (bare)")
print(f"  A_s(CMB) = {A_s_CMB:.1e}")
print(f"  Gap: {OOM_gap:.2f} OOM")
print(f"\nDone.")
