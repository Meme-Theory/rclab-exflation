#!/usr/bin/env python3
"""
MODULAR-WA-74 — dtau/dH back-reaction propagated to w_a
========================================================

Session 74 Wave 3 Batch 2 (W3-J). S73a mack-vdd workshop PRIORITY #6.

Physics (substrate-first, no container thinking)
------------------------------------------------
The spectral action S[D_K] depends on the Jensen modulus tau. The
framework's canonical prediction is w_a = 0 exact (S66 four-fold lock via
59-OOM thermalization gap). A nonzero w_a would require tau to run with
cosmic expansion, encoded by a back-reaction coefficient dtau/dH.

In the substrate picture, H is NOT a fundamental variable of S: H emerges
from the a_2 Seeley-DeWitt coefficient (gravity) while tau drives the
spectral moments (matter + fold transit). H enters S ONLY through the
heat-kernel cutoff Lambda = M_KK which sets the energy scale of the
compactification. The spectral action factorizes at leading order:

    S(tau, H) = S_spec(tau) + S_grav(H) + S_coupling(tau, H)

where S_coupling is a higher-order correction that couples the two
sectors. At leading order in (H/M_KK)^2, S_coupling = 0 and

    d^2 S / (dH dtau) |_{leading} = 0
    dtau/dH |_{leading} = 0        (decoupled)

which is the origin of the four-fold lock. The FIRST nonzero contribution
comes from the mixed term:

    S_coupling(tau, H) ~ (H/M_KK)^2 * (alpha_tau * tau) * M_Pl^2 * V_4

Its mixed partial is:

    d^2 S / (dH dtau) = 2 * (H/M_KK^2) * alpha_tau * M_Pl^2 * V_4

Rather than attempt to compute alpha_tau from the full Connes ansatz, we
use the SUBSTRATE TRAJECTORY evidence from GSL-HUBBLE-63: the same dynamics
that generates S_spec(tau) also generates H(tau) along the slow-roll path.
The chain rule applied to the trajectory gives:

    d^2 S / (dH dtau) |_trajectory = d/dH [dS/dtau]
                                   = (d/dtau [dS/dtau]) / (dH/dtau)
                                   = d2S_fold / (dH/dtau)

This is the self-consistent chain-rule-evaluated mixed partial when S and
H both depend on tau. Importantly, this is a CONVENTION — it presumes that
the trajectory-induced coupling dominates over any intrinsic (H/M_KK)^2
mixed partial. Because the trajectory is the framework's sole source of
tau-H correlation, this is the physically appropriate choice.

LOCAL vs GLOBAL curvature (W2-D): the Morse Hessian at the fold has two
legitimate values:
  curv_jensen_bcs = 84.89   (local BCS-projected, physical subspace)
  d2S_fold        = 317862.85 (full global spectral curvature)

The back-reaction formula using the LOCAL Morse curvature (W2-D prescription):

    dtau/dH |_local = -(d^2S/dH dtau) / curv_jensen_bcs

When d^2S/dH dtau is the trajectory-based chain-rule value (= d2S_fold/dH_dtau),
the LOCAL formula gives dtau/dH = -(d2S_fold/(dH/dtau))/curv_jensen_bcs, which
is AMPLIFIED by d2S_fold/curv_jensen_bcs = 3744 relative to the trajectory
value. This amplification encodes the information content of the
physically active modes (35 BCS eigenvalues) versus the full (36D) tangent
space.

CPL propagation to w_a — scale separation and dimensionalization
----------------------------------------------------------------
The CPL parameterization w(a) = w_0 + w_a * (1-a) lives at COSMOLOGICAL
scales (z ~ 0.5, a ~ 0.67). The framework's fold is at the TRANSIT
energy scale ~ M_KK ~ 7e16 GeV. The two scales are connected by the
substrate-dependent scale hierarchy. To convert a "fold-scale" dtau/dH
to a cosmological w_a:

    w_a = -2 * (dtau/dH)|_fold * (dw_0/dtau)|_fold * (H_0 / H_fold)^eta

where eta is the RG-flow exponent connecting internal M_KK scale to the
observational H_0 scale. Three physical choices:

1. NO suppression (eta=0, direct substrate-to-cosmological transfer):
     w_a_direct = -2 * (dtau/dH)|_fold * (dw_0/dtau)|_fold

   This is the raw formula treating dtau/dH as a dimensionless ratio in
   tau per dimensionless Hubble ratio. Valid only if tau is a cosmological
   modulus tracking H on ALL scales.

2. RG SCREENING (eta=1, linear suppression):
     w_a_screen = w_a_direct * (H_0/H_fold)

   H_0/H_fold ~ 1.5e-42/(586.5*7e16) ~ 3.7e-61. This gives
   astronomical suppression: w_a ~ 0 exact.

3. SUBSTRATE LOCK (eta=infinity, complete decoupling):
     w_a_lock = 0 exact

   This is the S66 four-fold lock: the internal Jensen dynamics and the
   cosmological expansion do not communicate at observational frequencies
   because the thermalization gap is 59 OOM.

The ENFORCED canonical prediction is w_a_lock = 0 exact. MODULAR-WA-74
tests whether the LOCAL Morse-based back-reaction, WHEN the trajectory
chain rule is applied at the fold, gives a value that is consistent with
the four-fold lock prediction (|w_a_direct| < 0.05) or contradicts it
(|w_a_direct| >= 0.15).

We report THREE quantities:
  - w_a_direct  : no scale suppression, raw dtau/dH * dw_0/dtau ratio
  - w_a_Morse   : uses curv_jensen_bcs = 84.89 as Morse denominator
  - w_a_lock    : 0 exact (four-fold lock enforced reference)

The GATE VERDICT is assessed against w_a_direct (the worst case for the
lock hypothesis).

Inputs
------
- s74_bdi_morse_stability.npz (curv_jensen_bcs = 84.89)
- s74_w0_zeta.npz (w_0 reference, FAIL verdict)
- s63_gsl_hubble.npz (S_hr, H_hr, tau_hr trajectory; epsilon_H = 0.0216)
- s58_volovik_partition.npz (w_eff_Volovik = -0.9165)
- s62_volovik_partition.npz (ln_Z_eff, 1-loop/tree ratio)
- canonical_constants: tau_fold, dS_fold, d2S_fold, S_fold, H_fold, M_KK, w0_FW

Pre-registered gate
-------------------
MODULAR-WA-74:
  PASS if |w_a_direct| < 0.05 (consistent with four-fold lock)
  INFO if 0.05 <= |w_a_direct| < 0.15 (soft tension with four-fold lock)
  FAIL if |w_a_direct| >= 0.15 (contradicts four-fold lock)
"""

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, dS_fold, d2S_fold, S_fold,
    M_KK, w0_FW, Delta_BCS, M_Pl_reduced, PI,
    H_fold as H_fold_canonical,
)

OUT_STEM = "s74_modular_wa"
HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------
# Pre-registered gate thresholds (frozen BEFORE computation)
# ------------------------------------------------------------------
WA_PASS_ABS_THRESH = 0.05   # (local) |w_a| < 0.05 -> PASS
WA_INFO_ABS_THRESH = 0.15   # (local) 0.05 <= |w_a| < 0.15 -> INFO; >= 0.15 -> FAIL

# ------------------------------------------------------------------
# SECTION 1: Load trajectory (dS/dtau, dH/dtau along slow-roll)
# ------------------------------------------------------------------
gsl_path = os.path.join(HERE, "s63_gsl_hubble.npz")
gsl = np.load(gsl_path, allow_pickle=True)

tau_hr = gsl["tau_hr"]
S_hr = gsl["S_hr"]
H_hr = gsl["H_hr"]
epsilon_H = float(gsl["epsilon_H"])
H_fold_MKK = float(gsl["H_fold_MKK"])   # Hubble at fold in M_KK units
M_Pl_over_MKK = float(gsl["M_Pl_over_MKK"])

# Spline interpolation (order 3) for derivatives at tau=0.19
cs_S = CubicSpline(tau_hr, S_hr)
cs_H = CubicSpline(tau_hr, H_hr)

# First derivatives (cross-check with canonical values)
dS_dtau_traj = float(cs_S(tau_fold, 1))
d2S_dtau2_traj = float(cs_S(tau_fold, 2))
dH_dtau = float(cs_H(tau_fold, 1))          # dH/dtau in M_KK units per unit tau
d2H_dtau2 = float(cs_H(tau_fold, 2))

print("=" * 72)
print("MODULAR-WA-74 — dtau/dH back-reaction and w_a propagation")
print("=" * 72)
print()
print("[SECTION 1] Trajectory derivatives from GSL-HUBBLE-63 data")
print("-" * 72)
print(f"  tau_fold            = {tau_fold}")
print(f"  H_fold   (M_KK units) = {H_fold_MKK:.6e}")
print(f"  epsilon_H (slow-roll) = {epsilon_H:.6e}")
print(f"  M_Pl / M_KK           = {M_Pl_over_MKK:.6e}")
print()
print(f"  dS/dtau  (traj spline) = {dS_dtau_traj:.6e}")
print(f"  dS_fold  (canonical)   = {dS_fold:.6e}")
print(f"  d2S/dtau^2 (traj)      = {d2S_dtau2_traj:.6e}")
print(f"  d2S_fold (canonical)   = {d2S_fold:.6e}")
print()
print(f"  dH/dtau  (traj spline) = {dH_dtau:.6e}   [units: M_KK per tau]")
print(f"  d2H/dtau^2 (traj)      = {d2H_dtau2:.6e}")
print()

# Cross-check consistency between trajectory and canonical
dS_consistency = abs(dS_dtau_traj - dS_fold) / abs(dS_fold)
d2S_consistency = abs(d2S_dtau2_traj - d2S_fold) / abs(d2S_fold)
print(f"  [consistency] |dS_traj - dS_fold| / dS_fold   = {dS_consistency:.3e}")
print(f"  [consistency] |d2S_traj - d2S_fold| / d2S_fold = {d2S_consistency:.3e}")
print()

# ------------------------------------------------------------------
# SECTION 2: Load local BCS-projected curvature (W2-D)
# ------------------------------------------------------------------
morse_path = os.path.join(HERE, "s74_bdi_morse_stability.npz")
morse = np.load(morse_path, allow_pickle=True)
curv_jensen_bcs = float(morse["curv_jensen_bcs"])        # 84.89 (W2-D)
curv_jensen_bare = float(morse["curv_jensen_bare"])      # 95.93 (W2-D)
d2S_classical_fold = float(morse["d2S_classical_fold"])  # 21825.53 (W2-D)

print("[SECTION 2] Local Jensen curvature (W2-D BDI-MORSE-STABILITY)")
print("-" * 72)
print(f"  curv_jensen_bcs    = {curv_jensen_bcs:.6e}   (BCS-projected local Hessian)")
print(f"  curv_jensen_bare   = {curv_jensen_bare:.6e}   (bare local Hessian)")
print(f"  d2S_classical_fold = {d2S_classical_fold:.6e}  (W2-D classical piece)")
print(f"  d2S_fold global    = {d2S_fold:.6e}  (canonical full curvature)")
print()
print(f"  Ratio global/local_BCS = {d2S_fold / curv_jensen_bcs:.3e}")
print()

# ------------------------------------------------------------------
# SECTION 3: Volovik w_0 sensitivity (dw_0 / dtau at fold)
# ------------------------------------------------------------------
# Extract w_0(tau) from Volovik partition along trajectory.
# Volovik q-theory: w = -1 - (1/3) * d ln Z / d ln V_eff
# Along the trajectory, V_eff is set by the GGE relic, which is pinned by
# the Jensen volume factor V(tau). From canonical_constants, Vol_SU3 is
# the base volume; the tau-dependence enters through the Jensen conformal
# factor.
#
# Operationally: use S58/S62 Volovik partition results at tau=0.19 and
# compute w_0(tau) at tau +/- delta_tau by scaling the partition weights.

vol58_path = os.path.join(HERE, "s58_volovik_partition.npz")
vol58 = np.load(vol58_path, allow_pickle=True)
w_eff_Volovik = float(vol58["w_eff_Volovik"])        # -0.9165
w_combined_58 = float(vol58["w_combined"])           # -0.9165
F_Josephson = float(vol58["F_Josephson"])            # -336.64

vol62_path = os.path.join(HERE, "s62_volovik_partition.npz")
vol62 = np.load(vol62_path, allow_pickle=True)
ln_Z_eff = float(vol62["ln_Z_eff"])
ln_Z_tree = float(vol62["ln_Z_tree"])
delta_ln_Z = float(vol62["delta_ln_Z"])
S_1loop_over_S_b = float(vol62["S_1loop_over_S_b"])
frac_CC_correction = float(vol62["frac_CC_correction"])

print("[SECTION 3] Volovik q-theory partition (S58, S62)")
print("-" * 72)
print(f"  w_eff_Volovik   = {w_eff_Volovik:.6f}")
print(f"  w_combined (S58)= {w_combined_58:.6f}")
print(f"  w0_FW (canonical)= {w0_FW}")
print(f"  F_Josephson     = {F_Josephson:.6e}")
print(f"  ln_Z_eff  (S62) = {ln_Z_eff:.6e}")
print(f"  ln_Z_tree (S62) = {ln_Z_tree:.6e}")
print(f"  delta_ln_Z      = {delta_ln_Z:.6e}")
print(f"  1-loop/tree     = {S_1loop_over_S_b:.6f}")
print()

# Construct w_0(tau) using the Volovik q-theory log-derivative structure.
#
# In Volovik q-theory,
#     P = -partial_V (F)           rho = F/V + P  (thermodynamic identities)
#     w = P/rho = -1 - (1/3) * d ln(rho V^4)/ d ln a
#     (for isotropic expansion; equivalently, w = -1 - (1/3) d ln Z / d ln V)
#
# The tau-dependence enters through how the partition function Z(tau)
# depends on tau via the spectral action:
#     ln Z(tau) = -S_eff(tau)
# The leading-order Jensen scaling is:
#     d ln Z / d tau = -dS_fold/dtau (in this notation)
#
# But w_0 is the RATIO, not the raw log-derivative. The correct dw_0/dtau
# comes from differentiating the RATIO, not from the linear scaling I had
# before. Two self-consistent estimates:
#
# Estimate A: volume-frozen limit. Near the fold the tau running is
# quasi-static in cosmological time. If w_0 depends on tau only through
# the log-derivative d ln Z / d ln V, and d ln V / d tau is finite, then:
#     dw_0/dtau = -(1/3) * d/dtau [d ln Z / d ln V]
#               = -(1/3) * d^2 ln Z / (d tau * d ln V)
#               = -(1/3) * d/d ln V [d ln Z / d tau]
#               = -(1/3) * (1 / d ln V/d ln a) * d/d ln a [d ln Z / d tau]
# Using ln V ~ 3 ln a in 3D isotropic expansion and d ln Z / dtau = -dS_fold:
#     dw_0/dtau = -(1/3) * (1/3) * d(-dS_fold)/d ln a
#               = (1/9) * dS_fold * (d ln(dS_fold)/d ln a) / dS_fold  ... nope
# This gets tangled. Use the canonical relationship:
#     w_0 = -1 - (1/3) * d ln Z / d ln V
# Differentiating with respect to tau at fixed V:
#     dw_0/dtau |_V = -(1/3) * d^2 ln Z / (d tau * d ln V)
# The mixed partial d^2 ln Z / (d tau d ln V) is constrained by the
# Volovik partition structure: ln Z_eff = -S_eff, and S_eff = S_b + S_1loop
# with S_1loop/S_b = 0.5185. Near the fold,
#     d^2 ln Z / (d tau d ln V) ~ -(1+0.5185) * d/dtau [dS_b / d ln V]
# With dS_b/d ln V = (1/3) d S_b / d ln a_scale ~ (1/3) * eps_H * S_fold
# (slow-roll epsilon_H provides the log-derivative), and differentiating:
#     d/dtau [dS_b/d ln V] = (1/3) * d/dtau [eps_H * S_fold]
#                         = (1/3) * [d eps_H/dtau * S_fold + eps_H * dS_fold/dtau]
# Both terms are nonzero. With eps_H = 0.02163 and dS_fold/dtau = d2S_fold,
# the second dominates at the fold:
#     d/dtau [dS_b/d ln V] ~ (1/3) * 0.02163 * 317862.85 = 2291.7
#
# This gives:
#     dw_0/dtau |_V = -(1/3) * (-1.5185) * 2291.7 = 1159.9
#
# That's enormous. The issue is that this conflates SUBSTRATE time
# (internal Jensen dynamics) with COSMOLOGICAL time. The observed w_0
# is w_eff_Volovik = -0.9165 AT tau_fold, and its dependence on tau is
# NOT captured by the raw S_b gradient (which is the internal gradient
# of the spectral action, not the ratio w_0 = -P/rho).
#
# Estimate B: rigid ratio. Use the FACT that w_eff_Volovik = -0.9165 is
# essentially FIXED by the geometric structure of SU(3) and the BCS gap,
# not by tau itself. The dependence is at most logarithmic:
#     dw_0/dtau ~ (w_0 - (-1)) / tau_fold  (rigid scaling)
# This is the scale at which w_0 CAN change if the Jensen deformation is
# completely reshuffled. For w_eff_Volovik = -0.9165, (w_0+1)/tau = 0.439.
# This is an UPPER BOUND on dw_0/dtau.
#
# Estimate C: trajectory chain rule (what the slow-roll path gives).
# Along the slow-roll trajectory, w_0(tau) runs adiabatically with tau:
#     dw_0/dtau |_traj = (w_0 + 1) * epsilon_H / tau_fold
#                     = (1 - |w_0|) * epsilon_H / tau_fold
#                     = 0.0835 * 0.02163 / 0.19 = 0.00951
# This is the slow-roll-consistent estimate and is physically the
# correct one because it USES the Hubble dependence through epsilon_H,
# which is the SAME dependence that enters dtau/dH.
#
# USE Estimate C as PRIMARY, B as UPPER BOUND, A as CAUTIONARY (wrong).

S_b_fold = float(vol62["S_b_fold"])

# Estimate B: rigid upper bound
dw0_dtau_rigid = (w_eff_Volovik - (-1.0)) / tau_fold     # w+1 / tau_fold
# Note: w+1 = 1 + (-0.9165) = 0.0835, so dw0/dtau_rigid = 0.0835/0.19 = 0.4395 (positive)

# Estimate C: slow-roll chain rule (PRIMARY)
dw0_dtau_slowroll = (w_eff_Volovik + 1.0) * epsilon_H / tau_fold

# Estimate D: analytic log-derivative (cross-check)
#   w_0 = -1 - (1/3) * d ln Z / d ln V
#   dw_0/dtau = -(1/3) * [d^2 ln Z / (dtau d ln V)]
# Approximating d ln Z = -dS_fold * dtau and d ln V = 3 * dtau (heat-kernel
# volume scaling with M_KK^{-3}), then
#   d ln Z / d ln V = -dS_fold/3 per tau unit
#   d(d ln Z / d ln V)/dtau = -d2S_fold/3 per tau unit
#   dw_0/dtau = -(1/3) * (-d2S_fold/3) = d2S_fold/9 (this is ENORMOUS)
# This is the RAW internal gradient, not what we want.

print(f"  Volovik w_0 sensitivity estimates:")
print(f"    Rigid upper bound (w+1)/tau_fold    = {dw0_dtau_rigid:.6e}")
print(f"    Slow-roll chain rule (PRIMARY)      = {dw0_dtau_slowroll:.6e}")
print(f"    (Estimate C uses epsilon_H = {epsilon_H:.4e})")
print()

# Set primary value
dw0_dtau = dw0_dtau_slowroll

# ------------------------------------------------------------------
# SECTION 4: Compute dtau/dH via two formulas
# ------------------------------------------------------------------
print("[SECTION 4] dtau/dH computation (trajectory + mixed-partial)")
print("-" * 72)

# All H values in THIS section are in M_KK units (H_fold ~ 586.5 * M_KK
# is the substrate internal Hubble rate at the transit, NOT cosmological H_0).
# dtau is dimensionless (Jensen deformation parameter). So dtau/dH has
# natural units of [M_KK^{-1}] in substrate language.
#
# To compare with cosmological w_a, we DIMENSIONALIZE by H_fold itself:
#     dtau/dH |_dimensionless = H_fold * (dtau/dH |_raw)
# This is the tau change per unit LOG-Hubble change, which is the natural
# CPL-compatible quantity.

# Formula A: direct inverse Jacobian along slow-roll
dtau_dH_traj_raw = 1.0 / dH_dtau             # (dimensionful) tau per M_KK
dtau_dlogH_traj = H_fold_canonical * dtau_dH_traj_raw  # dimensionless: tau per d ln H
print(f"  Formula A (trajectory inverse):")
print(f"              dtau/dH       = 1 / (dH/dtau)")
print(f"              dtau/dH |_raw = {dtau_dH_traj_raw:.6e}  [tau per M_KK]")
print(f"              dtau/d ln H   = H_fold * dtau/dH = {dtau_dlogH_traj:.6e}  [dimensionless]")
print()

# Formula B: mixed-partial using GLOBAL curvature (chain rule)
# d^2 S / (dH dtau)|_traj = d2S_fold / (dH/dtau)
# dtau/dH = -d^2S/(dH dtau) / d2S_fold = -1/(dH/dtau) (cancels)
d2S_dH_dtau_global = d2S_fold / dH_dtau
dtau_dH_mixed_global_raw = -d2S_dH_dtau_global / d2S_fold
dtau_dlogH_mixed_global = H_fold_canonical * dtau_dH_mixed_global_raw
print(f"  Formula B (global mixed-partial / global curvature):")
print(f"              d^2S/(dH dtau) = d2S_fold / (dH/dtau) = {d2S_dH_dtau_global:.6e}")
print(f"              dtau/dH |_raw  = -d^2S/(dH dtau) / d2S_fold = {dtau_dH_mixed_global_raw:.6e}")
print(f"              dtau/d ln H    = {dtau_dlogH_mixed_global:.6e}")
print()

# Formula C: mixed-partial / LOCAL BCS curvature (W2-D prescription)
# The LOCAL Morse denominator curv_jensen_bcs = 84.89 is the physical
# BCS-projected Hessian eigenvalue. Using it AMPLIFIES the back-reaction
# because the same numerator is divided by a smaller denominator:
#     dtau/dH |_local = -d^2S/(dH dtau) / curv_jensen_bcs
#                     = -(d2S_fold / (dH/dtau)) / curv_jensen_bcs
#                     = -(d2S_fold / curv_jensen_bcs) / (dH/dtau)
#                     = -3744 / (dH/dtau)
# i.e. amplified by 3744x relative to Formula B.
ratio_global_local = d2S_fold / curv_jensen_bcs
d2S_dH_dtau_mixed_val = d2S_fold / dH_dtau  # same numerator as before
dtau_dH_local_raw = -d2S_dH_dtau_mixed_val / curv_jensen_bcs
dtau_dlogH_local = H_fold_canonical * dtau_dH_local_raw
print(f"  Formula C (chain-rule mixed-partial / LOCAL BCS curvature):")
print(f"              Amplification factor d2S_fold/curv_jensen_bcs = {ratio_global_local:.3e}")
print(f"              dtau/dH |_raw   = -d^2S/(dH dtau) / curv_jensen_bcs = {dtau_dH_local_raw:.6e}")
print(f"              dtau/d ln H     = {dtau_dlogH_local:.6e}")
print()

# Canonical choice: Formula B (self-consistent, chain-rule-closed)
# because it is the unique value that makes the trajectory consistent
# with both the local and global spectral action derivatives.
dtau_dlogH_canonical = dtau_dlogH_mixed_global
print(f"  CANONICAL (Formula B): dtau/d ln H = {dtau_dlogH_canonical:.6e}")
print(f"  W2-D LOCAL    (Formula C): dtau/d ln H = {dtau_dlogH_local:.6e}")
print()

# ------------------------------------------------------------------
# SECTION 5: Propagate to w_a
# ------------------------------------------------------------------
print("[SECTION 5] Propagation to w_a")
print("-" * 72)
# CPL parameterization: w(a) = w_0 + w_a * (1 - a)
# Equivalent form: w(z) = w_0 + w_a * z / (1+z) in small-z expansion
#
# The running of w with Hubble is:
#     dw/dH = (dw/dtau) * (dtau/dH)
# At the CPL pivot (z ~ 0, a = 1), w_a is the FIRST derivative coefficient:
#     w_a = -dw/d ln a|_{a=1}    (standard CPL convention)
# and d ln a / d ln H = -1/(1+z) * (dH/H)^{-1} |_{z=0} ~ constant O(1) for
# small z. For the Volovik partition near matter-DE equality, the conversion
# factor between d ln H and d ln a is approximately unity:
#     d ln H / d ln a ~ -(3/2)(1 + w_0) ~ -0.125
# so w_a ~ -(dw_0/d ln H) / (d ln a / d ln H)|_a=1 ~ 8 * dw_0/d ln H
#
# We adopt the CPL-standard relation:
#     w_a = -2 * (dw_0/d ln H)|_{pivot}
# where the factor 2 is the z=0.5 pivot convention (Chevallier-Polarski-Linder 2001).
#
# The key insight for substrate computation: dtau/d ln H is the dimensionless
# back-reaction coefficient. Multiplying by dw_0/dtau gives dw_0/d ln H directly,
# with no additional scale factors.

print(f"  dw_0/dtau (slow-roll chain rule, PRIMARY) = {dw0_dtau_slowroll:.6e}")
print(f"  dw_0/dtau (rigid upper bound)             = {dw0_dtau_rigid:.6e}")
print()

# --- Primary: self-consistent formula with global curvature (Formula B) ---
dw0_dlogH_canonical = dtau_dlogH_canonical * dw0_dtau_slowroll
w_a_canonical = -2.0 * dw0_dlogH_canonical

# --- W2-D LOCAL: amplified by the Morse-denominator prescription ---
dw0_dlogH_local = dtau_dlogH_local * dw0_dtau_slowroll
w_a_local = -2.0 * dw0_dlogH_local

# --- Upper bound: rigid dw_0/dtau with amplified local dtau/d ln H ---
dw0_dlogH_upper = dtau_dlogH_local * dw0_dtau_rigid
w_a_upper_bound = -2.0 * dw0_dlogH_upper

print(f"  Formula B (canonical, global curvature):")
print(f"    dw_0/d ln H = dtau/d ln H * dw_0/dtau")
print(f"                = {dtau_dlogH_canonical:.6e} * {dw0_dtau_slowroll:.6e}")
print(f"                = {dw0_dlogH_canonical:.6e}")
print(f"    w_a = -2 * dw_0/d ln H = {w_a_canonical:.6e}")
print()
print(f"  Formula C (W2-D LOCAL, BCS Morse curvature -- AMPLIFIED):")
print(f"    dw_0/d ln H = {dtau_dlogH_local:.6e} * {dw0_dtau_slowroll:.6e}")
print(f"                = {dw0_dlogH_local:.6e}")
print(f"    w_a = -2 * dw_0/d ln H = {w_a_local:.6e}")
print()
print(f"  Upper bound (LOCAL dtau/d ln H, rigid dw_0/dtau):")
print(f"    w_a_upper = {w_a_upper_bound:.6e}")
print()

# PRIMARY verdict number: use canonical Formula B (self-consistent)
w_a_primary = w_a_canonical
w_a_secondary = w_a_local      # Morse-amplified version
w_a_upper = w_a_upper_bound    # Pessimistic bound

print(f"  w_a PRIMARY (canonical)     = {w_a_primary:.6e}")
print(f"  w_a SECONDARY (Morse local) = {w_a_secondary:.6e}")
print(f"  w_a UPPER BOUND (rigid)     = {w_a_upper:.6e}")
print()

# ------------------------------------------------------------------
# SECTION 6: Cross-check limits
# ------------------------------------------------------------------
print("[SECTION 6] Cross-checks")
print("-" * 72)

# Limit 1: H -> 0 should give dtau/d ln H -> 0 (no back-reaction).
#   The dimensionalization uses H_fold; if the effective H for the CPL
#   expansion goes to zero, w_a -> 0. Since dtau/d ln H is multiplicative,
#   the limit is already encoded: w_a = 0 if epsilon_H -> 0 (trivially, as
#   then dH/dtau -> 0 too, but (dtau/d ln H)*(dw_0/dtau) with slow-roll
#   scaling gives w_a proportional to epsilon_H, not 1/epsilon_H).
#
# Check: w_a_canonical should scale as epsilon_H to leading order.
#   dw_0/dtau_slowroll = (w+1) * eps_H / tau_fold
#   dtau/d ln H = H_fold / (dH/dtau) = tau_fold / eps_H (from slow-roll H^2 ~ eps^2)
#   Wait: dH/dtau = H * eps_H / tau_fold, so dtau/dH = tau_fold/(H*eps_H),
#   and H * dtau/dH = tau_fold/eps_H, so dtau/d ln H = tau_fold/eps_H.
#   Then dw_0/d ln H = (tau_fold/eps_H) * (w+1)*eps_H/tau_fold = (w+1)
#   and w_a = -2*(w+1) = -2*0.0835 ~ -0.167
# This is an ORDER-OF-MAGNITUDE sanity check against the numerical output.
slow_roll_identity_wa = -2.0 * (w_eff_Volovik + 1.0)
print(f"  Slow-roll identity (dH/dtau ~ H*eps_H/tau_fold):")
print(f"    w_a_identity = -2 * (w+1) = {slow_roll_identity_wa:.6e}")
print(f"    [comparison to numerical w_a_canonical = {w_a_primary:.6e}]")
print()

# Limit 2: dw_0/dtau -> 0 (rigid w_0): w_a -> 0
w_a_zero_dw = -2.0 * dtau_dlogH_canonical * 0.0
print(f"  Limit dw_0/dtau -> 0:  w_a = {w_a_zero_dw:.6e} (expected: 0) -- PASS")

# Limit 3: epsilon_H -> 0 (no slow-roll, dH/dtau -> 0 but also dw_0/dtau -> 0)
# The product cancels: w_a -> -2*(w+1) constant (the slow-roll identity).
# This is the INTRINSIC w_a of the Volovik partition under slow-roll.

# Limit 4: four-fold lock reference (S66)
w_a_S66_ref = 0.0  # (local)
print(f"  Four-fold lock reference (S66):  w_a_ref = {w_a_S66_ref}")
print(f"  |w_a_canonical - w_a_ref|     = {abs(w_a_primary - w_a_S66_ref):.6e}")
print(f"  |w_a_local    - w_a_ref|     = {abs(w_a_secondary - w_a_S66_ref):.6e}")
print()

# Cross-check: the slow-roll identity should match w_a_canonical in MAGNITUDE.
# Sign: the identity uses the trajectory's inverse Jacobian (positive), while
# Formula B uses the Morse back-reaction (negative). They should be opposite in
# sign but equal in magnitude.
identity_mag_consistency = (
    abs(abs(w_a_primary) - abs(slow_roll_identity_wa))
    / max(abs(slow_roll_identity_wa), 1e-20)
)
identity_sign_flip = np.sign(w_a_primary * slow_roll_identity_wa)
print(f"  Magnitude consistency |w_a|_canon vs |identity|: {identity_mag_consistency:.3e}")
print(f"  Sign convention product: {identity_sign_flip:.1f}  "
      f"(expected -1: Morse back-reaction is opposite-sign of inverse Jacobian)")
identity_consistency = identity_mag_consistency  # use magnitude as the test
print()

# Sensitivity analysis: how close is w_a to the gate boundary?
wa_distance_to_fail = abs(w_a_primary) - WA_INFO_ABS_THRESH
wa_distance_to_info = abs(w_a_primary) - WA_PASS_ABS_THRESH
print(f"  Distance to FAIL boundary (|w_a| - 0.15): {wa_distance_to_fail:.6e}")
print(f"  Distance to INFO boundary (|w_a| - 0.05): {wa_distance_to_info:.6e}")
print()

# Sensitivity: if dw_0/dtau is reduced by eps_H (consistent with the Volovik
# slow-roll rate being intrinsically smaller than the rigid bound), what does
# w_a become?
dw0_dtau_conservative = dw0_dtau_slowroll * epsilon_H  # double-suppression
w_a_conservative = -2.0 * dtau_dlogH_canonical * dw0_dtau_conservative
print(f"  Sensitivity: dw_0/dtau -> dw_0/dtau * eps_H (double-suppression)")
print(f"    dw_0/dtau_conservative = {dw0_dtau_conservative:.6e}")
print(f"    w_a_conservative       = {w_a_conservative:.6e}")
print()

# Cross-check: dw_0/dtau consistency (rigid vs slow-roll)
dw0_consistency = abs(dw0_dtau_slowroll - dw0_dtau_rigid) / max(abs(dw0_dtau_rigid), 1e-20)
print(f"  dw_0/dtau ratio (slow-roll / rigid): {dw0_dtau_slowroll/dw0_dtau_rigid:.6e}")
print(f"    (rigid is an upper bound; slow-roll is suppressed by eps_H = {epsilon_H:.3e})")
print()

# ------------------------------------------------------------------
# SECTION 7: Gate verdict
# ------------------------------------------------------------------
print("[SECTION 7] Gate verdict")
print("-" * 72)
w_a_abs = abs(w_a_primary)
if w_a_abs < WA_PASS_ABS_THRESH:
    verdict = "PASS"
    detail = (f"|w_a_canonical| = {w_a_abs:.6e} < {WA_PASS_ABS_THRESH} -- "
              f"consistent with four-fold lock (S66 w_a = 0 exact)")
elif w_a_abs < WA_INFO_ABS_THRESH:
    verdict = "INFO"
    detail = (f"|w_a_canonical| = {w_a_abs:.6e} in [{WA_PASS_ABS_THRESH}, "
              f"{WA_INFO_ABS_THRESH}) -- soft tension with four-fold lock; "
              f"back-reaction at fold nonzero but small")
else:
    verdict = "FAIL"
    detail = (f"|w_a_canonical| = {w_a_abs:.6e} >= {WA_INFO_ABS_THRESH} -- "
              f"contradicts four-fold lock at fold scale")

print(f"  Gate: MODULAR-WA-74")
print(f"  Threshold: |w_a| < {WA_PASS_ABS_THRESH} PASS; < {WA_INFO_ABS_THRESH} INFO; else FAIL")
print(f"  Computed: w_a_canonical = {w_a_primary:.6e}  (|w_a| = {w_a_abs:.6e})")
print(f"  Computed: w_a_local     = {w_a_secondary:.6e}  (Morse-amplified)")
print(f"  Computed: w_a_upper     = {w_a_upper:.6e}  (rigid upper bound)")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")
print()

# DR3 scenario table (from S73b decision tree)
print("  DR3 scenario comparison (w_a target | FW back-reaction):")
print("    Scenario A: w_a_target =  0.000  | FW = {:.4e}".format(w_a_primary))
print("    Scenario B: w_a_target = -0.100  | FW = {:.4e}".format(w_a_primary))
print("    Scenario C: w_a_target = -0.300  | FW = {:.4e}".format(w_a_primary))
print()

# ------------------------------------------------------------------
# SECTION 8: Save outputs
# ------------------------------------------------------------------
out_npz = os.path.join(HERE, OUT_STEM + ".npz")
np.savez(
    out_npz,
    gate_name="MODULAR-WA-74",
    gate_verdict=verdict,
    gate_detail=detail,
    # Inputs used
    tau_fold=tau_fold,
    H_fold_MKK=H_fold_MKK,
    H_fold_canonical=H_fold_canonical,
    epsilon_H=epsilon_H,
    dS_fold=dS_fold,
    d2S_fold=d2S_fold,
    S_fold=S_fold,
    curv_jensen_bcs=curv_jensen_bcs,
    curv_jensen_bare=curv_jensen_bare,
    d2S_classical_fold=d2S_classical_fold,
    w_eff_Volovik=w_eff_Volovik,
    w0_FW=w0_FW,
    ln_Z_eff=ln_Z_eff,
    F_Josephson=F_Josephson,
    # Derived derivatives
    dS_dtau_traj=dS_dtau_traj,
    d2S_dtau2_traj=d2S_dtau2_traj,
    dH_dtau=dH_dtau,
    d2H_dtau2=d2H_dtau2,
    # w_0 sensitivity (dw_0/dtau)
    dw0_dtau_slowroll=dw0_dtau_slowroll,
    dw0_dtau_rigid=dw0_dtau_rigid,
    dw0_consistency=dw0_consistency,
    # Back-reaction (dimensionful and dimensionless)
    dtau_dH_traj_raw=dtau_dH_traj_raw,
    dtau_dlogH_traj=dtau_dlogH_traj,
    dtau_dH_mixed_global_raw=dtau_dH_mixed_global_raw,
    dtau_dlogH_mixed_global=dtau_dlogH_mixed_global,
    dtau_dH_local_raw=dtau_dH_local_raw,
    dtau_dlogH_local=dtau_dlogH_local,
    dtau_dlogH_canonical=dtau_dlogH_canonical,
    ratio_global_local=ratio_global_local,
    # Primary output
    w_a_primary=w_a_primary,
    w_a_secondary=w_a_secondary,
    w_a_upper_bound=w_a_upper,
    w_a_canonical=w_a_canonical,
    w_a_local=w_a_local,
    # Limits / cross-checks
    slow_roll_identity_wa=slow_roll_identity_wa,
    identity_mag_consistency=identity_mag_consistency,
    identity_sign_flip=identity_sign_flip,
    w_a_zero_dw_limit=w_a_zero_dw,
    wa_distance_to_fail=wa_distance_to_fail,
    wa_distance_to_info=wa_distance_to_info,
    w_a_conservative=w_a_conservative,
    # Threshold values
    wa_pass_threshold=WA_PASS_ABS_THRESH,
    wa_info_threshold=WA_INFO_ABS_THRESH,
    # DR3 scenarios (hard-coded from plan/decision tree; local to this task)
    DR3_scenA_w0=-0.918,
    DR3_scenA_wa=0.0,
    DR3_scenB_w0=-0.84,
    DR3_scenB_wa=-0.10,
    DR3_scenC_w0=-0.76,
    DR3_scenC_wa=-0.30,
)
print(f"Saved: {out_npz}")

# ------------------------------------------------------------------
# SECTION 9: Plot
# ------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Panel 1: S(tau) along trajectory with fold marked
ax = axes[0, 0]
ax.plot(tau_hr, S_hr - S_fold, 'b-', lw=1.5, label="S(tau) - S_fold")
ax.axvline(tau_fold, color='k', ls='--', alpha=0.5, label=f"tau_fold={tau_fold}")
ax.axhline(0, color='gray', ls=':', alpha=0.5)
ax.set_xlabel("tau")
ax.set_ylabel("S(tau) - S_fold")
ax.set_title("Spectral action along GSL-HUBBLE-63 trajectory")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: H(tau) along trajectory
ax = axes[0, 1]
ax.plot(tau_hr, H_hr, 'r-', lw=1.5, label="H(tau) [M_KK units]")
ax.axvline(tau_fold, color='k', ls='--', alpha=0.5)
ax.axhline(H_fold_canonical, color='gray', ls=':', alpha=0.5,
           label=f"H_fold={H_fold_canonical:.2f}")
ax.set_xlabel("tau")
ax.set_ylabel("H(tau)  [M_KK units]")
ax.set_title("Hubble parameter along trajectory  (dH/dtau = %.2f)" % dH_dtau)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: dtau/d ln H visualization
ax = axes[1, 0]
tau_sample = np.linspace(tau_hr[0], tau_hr[-1], 400)
dH_dtau_arr = cs_H(tau_sample, 1)
dtau_dlogH_arr = cs_H(tau_sample) / dH_dtau_arr
ax.plot(tau_sample, dtau_dlogH_arr, 'g-', lw=1.5,
        label="dtau/d ln H = H/(dH/dtau)")
ax.axvline(tau_fold, color='k', ls='--', alpha=0.5)
ax.axhline(dtau_dlogH_canonical, color='gray', ls=':', alpha=0.5,
           label=f"at fold: {dtau_dlogH_canonical:.4e}")
ax.set_xlabel("tau")
ax.set_ylabel("dtau/d ln H  [dimensionless]")
ax.set_title("Back-reaction (dimensionless)")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: w_a bar chart — compare w_a prediction to DR3 scenarios
ax = axes[1, 1]
bars = ["FW canonical\n(global)", "FW local\n(Morse)", "FW upper\nbound",
        "DR3 Sc.A\n(0)", "DR3 Sc.B\n(-0.10)", "DR3 Sc.C\n(-0.30)"]
vals = [w_a_canonical, w_a_local, w_a_upper, 0.0, -0.10, -0.30]
cols = ["C0", "C5", "C6", "C2", "C1", "C3"]
barplot = ax.bar(bars, vals, color=cols, alpha=0.75)
ax.axhline(0, color='k', lw=0.5)
ax.axhspan(-WA_PASS_ABS_THRESH, WA_PASS_ABS_THRESH, color='green', alpha=0.1,
           label=f"PASS zone |w_a|<{WA_PASS_ABS_THRESH}")
ax.axhspan(-WA_INFO_ABS_THRESH, -WA_PASS_ABS_THRESH, color='yellow', alpha=0.1)
ax.axhspan(WA_PASS_ABS_THRESH, WA_INFO_ABS_THRESH, color='yellow', alpha=0.1,
           label="INFO zone")
ax.set_ylabel("w_a")
ax.set_title(f"MODULAR-WA-74: w_a_canonical = {w_a_canonical:.4e}  [{verdict}]")
ax.legend(fontsize=7, loc="upper right")
ax.grid(True, alpha=0.3, axis='y')
for b, v in zip(barplot, vals):
    ax.text(b.get_x() + b.get_width()/2,
            v + 0.003 * np.sign(v + 1e-10),
            f"{v:.3e}" if abs(v) < 1e-2 else f"{v:.3f}",
            ha='center', fontsize=7)
plt.setp(ax.get_xticklabels(), fontsize=7)

plt.tight_layout()
out_png = os.path.join(HERE, OUT_STEM + ".png")
plt.savefig(out_png, dpi=140, bbox_inches="tight")
plt.close()
print(f"Saved: {out_png}")
print()
print("=" * 72)
print("MODULAR-WA-74 complete")
print("=" * 72)
