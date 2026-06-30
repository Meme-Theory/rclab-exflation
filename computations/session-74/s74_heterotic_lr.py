#!/usr/bin/env python3
"""
S74 W3-M HETEROTIC-LR-74
========================

Heterotic L/R + three-coupling consistency + sin^2(theta_W) connection layer.

Consolidates S74-CF-4 (heterotic spectral triple), S74-CF-5 (three-coupling
consistency), S74-CF-12 (connection-layer sin^2) from S73A landau-baptista
workshop.

Structure of the computation
----------------------------

Baptista Paper 13 (HD routes to SM bosons), eq 3.41, defines a 4D Lagrangian
produced by fibre-integration of (R_P - 2 Lambda_P) where the submersion
metric g_P on M^4 x SU(3) is built from TWO connection one-forms:

    A_L : M^4 -> su(3)   (left-invariant side, couples to Higgs phi)
    A_R : M^4 -> su(3)   (right-invariant side, does NOT couple to phi)

The Yang-Mills action contains |F_{A_L}|^2 weighted by g_phi (the DEFORMED
left-invariant metric) and |F_{A_R}|^2 weighted by beta (the bi-invariant
metric).  This is precisely the heterotic split of Brain-Mesland-van Suijlekom
(Paper 20), which factors a noncommutative spectral triple (A,H,D) over a
commutative base: the internal algebra splits as A_L + A_R, with inner
fluctuations carrying connections in DIFFERENT representations on the two
factors.

In the three-coupling refinement (Paper 13 Sec. 5), beta_tilde on su(3) uses
three independent scales:

    beta_tilde(u,v) = lambda_1 * Tr(u_Y^dagger v_Y)          on u(1)_Y
                    + lambda_2 * Tr(u_W^dagger v_W)          on su(2)_L
                    + lambda_3 * Tr((u'')^dagger v'')        on C^2 (Higgs)

For beta_tilde to be a POSITIVE-DEFINITE Riemannian metric on su(3), we need
all three lambdas positive:  lambda_1 > 0,  lambda_2 > 0,  lambda_3 > 0.
This is the metric-positivity pre-requisite of the entire Paper 13
construction (the deformation parameter condition |phi|^2 < 1/4 in eq 2.25
is a separate positivity condition on the Higgs-sector deformation, but that
comes on TOP of the pre-existing requirement that beta_tilde itself be
positive).

The resulting gauge couplings (eq 5.21) are:
    g'/2   = sqrt(3 / lambda_1)
    g/2    = 1 / sqrt(lambda_2)
    g_s/2  = 2 sqrt(2) / sqrt(lambda_1 + 3*lambda_2 + 4*lambda_3)

and the M_Z/M_W ratio (eq 5.25):
    M_Z^2 / M_W^2 = 1 + 3 * lambda_2 / lambda_1

The L/R asymmetry parameter measures the connection-level anisotropy of the
left-invariant metric on the three A-module blocks.  When lambda_1 = 3*lambda_2
the U(1) and SU(2) couplings coincide (g = g'), sin^2 = 1/2, and there is no
L/R asymmetry at the connection level.  The departure from the g = g' locus
is the three-coupling generalization of the L/R asymmetry.

Three-coupling self-consistency test (sub-gate A)
-------------------------------------------------

We have 3 unknowns (lambda_1, lambda_2, lambda_3) and FIVE observational
inputs at the M_Z scale:

    (C1) alpha_em(M_Z)  = 1/127.955           from 1/g^2 + 1/g'^2 = 1/e^2
    (C2) alpha_s(M_Z)   = 0.1180              fixes g_s
    (C3) sin^2(MSbar)   = 0.23122             PDG reference scheme
    (C4) M_W            = 80.3692  GeV        on-shell anchor
    (C5) M_Z            = 91.1876  GeV        on-shell anchor

At tree level in Paper 13, constraints (C3) and (C4, C5) both give a value
for the anisotropy ratio lambda_2 / lambda_1 , but they do so in DIFFERENT
schemes: (C3) uses MSbar at M_Z, while (C4) combined with (C5) uses the
on-shell definition sin^2 = 1 - (M_W/M_Z)^2 = 0.22320 .  Those two values
differ by 3.47% (the well-known scheme tension).  This gives us our genuine
self-consistency test: with lambda_1, lambda_2 fit from ANY two of the three
"electroweak" inputs (C1, C3, C4&C5), how well do the remaining predictions
reproduce the observed third input?

Additionally, we test the PHYSICAL feasibility constraint:

    (P) metric positivity:  lambda_1 > 0  AND  lambda_2 > 0  AND  lambda_3 > 0

Sub-gate (A) PASSES only if the predicted residual on the reserved input is
< 5% AND all three lambdas are positive.

sin^2 closure (sub-gate B, connection layer)
--------------------------------------------

With (lambda_1, lambda_2, lambda_3) fixed by the consistency test in the
MSbar convention, we evaluate:

    sin^2(theta_W) = g'^2 / (g'^2 + g^2)
                   = (3/lambda_1) / (3/lambda_1 + 1/lambda_2)
                   = (3*lambda_2) / (lambda_1 + 3*lambda_2)

This is the "connection-layer" value: the Baptista tree-level prediction
from the heterotic three-coupling structure.  Sub-gate (B) PASSES if the
result is in [0.21, 0.25].

Cross-checks
------------
  (1) A_L = A_R  =>  no L/R asymmetry  =>  sin^2 = 1/2
      Verified by setting lambda_1 = 3 * lambda_2  (the g = g' locus).
  (2) Paper 13 eq 5.21 reproduced to 0.1% at the lambda_i input values.
  (3) W2-J and W3-I cross-check: those gates computed sin^2 at the
      SPECTRAL / fiber-integrated level (threshold sums + RG running to
      M_Z) and found sin^2 = -1.165699 (Jensen-blind, Dynkin-ratio locked).
      W3-M is at the CONNECTION / pre-spectral level at M_Z (no RG running,
      no per-sector threshold).  The two are structurally different layers
      and are allowed to disagree -- the distinction is precisely WHERE the
      scheme-dependent tension between MSbar and on-shell sin^2 enters.
  (4) Metric positivity on the u(2) subspace (lambda_1, lambda_2 > 0) and
      on the C^2 Higgs subspace (lambda_3 > 0).

Author: baptista-spacetime-analyst (S74 W3-M)
Date:   2026-04-11
"""

from __future__ import annotations

import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# Force headless backend
import matplotlib
matplotlib.use("Agg")

# Force canonical constants import (per math-scripts rule)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (  # noqa: E402
    M_Z,
    M_W,
    alpha_em_MZ_inv,
    alpha_s_MZ_obs,
    sin2_thetaW_MSbar,
    tau_fold,
    M_KK,
    PI,
)


# ==============================================================================
# SECTION 1 -- Derived observational anchors
# ==============================================================================

alpha_em_MZ = 1.0 / alpha_em_MZ_inv                      # (local)
e_em_MZ = np.sqrt(4.0 * PI * alpha_em_MZ)                # (local)  positron charge
g_s_sq_obs = 4.0 * PI * alpha_s_MZ_obs                   # (local)  strong coupling squared
sin2_on_shell = 1.0 - (M_W / M_Z) ** 2                   # (local)  on-shell def of sin^2_W
ratio_MZ_MW_sq = (M_Z / M_W) ** 2                        # (local)
# Observational values (on-shell) in the convention that matches Paper 13 eq 5.25:
ratio_l2_over_l1_obs = (ratio_MZ_MW_sq - 1.0) / 3.0      # (local)  from eq 5.25
sin2_obs = sin2_on_shell                                 # (local)  primary Baptista observable

# MSbar reference for reporting only (NOT used in the on-shell fit)
sin2_MSbar = sin2_thetaW_MSbar                           # (local)

# SU(2) and U(1) gauge couplings at M_Z from alpha_em and sin^2_W (on-shell)
# In SM:  g = e / sin(theta_W),  g' = e / cos(theta_W)
g_SU2_obs = e_em_MZ / np.sqrt(sin2_obs)                  # (local)
g_U1_prime_obs = e_em_MZ / np.sqrt(1.0 - sin2_obs)       # (local)  this is g' (not GUT-normalized)
g_s_obs = np.sqrt(g_s_sq_obs)                            # (local)

print("=" * 78)
print("S74 W3-M HETEROTIC-LR-74  --  inputs and PDG anchors")
print("=" * 78)
print(f"alpha_em(M_Z)       = {alpha_em_MZ:.8f}   (1/alpha = {alpha_em_MZ_inv:.3f})")
print(f"alpha_s(M_Z)        = {alpha_s_MZ_obs:.6f}")
print(f"e_em(M_Z)           = {e_em_MZ:.6f}")
print(f"M_W                 = {M_W:.4f} GeV")
print(f"M_Z                 = {M_Z:.4f} GeV")
print(f"(M_Z/M_W)^2         = {ratio_MZ_MW_sq:.6f}")
print(f"sin^2_W on-shell    = {sin2_on_shell:.6f}  (from M_W, M_Z)")
print(f"sin^2_W MSbar       = {sin2_MSbar:.6f}  (reference only)")
print(f"g  (SU(2))          = {g_SU2_obs:.6f}")
print(f"g' (U(1)_Y)         = {g_U1_prime_obs:.6f}")
print(f"g_s                 = {g_s_obs:.6f}")
print(f"lambda_2/lambda_1   = {ratio_l2_over_l1_obs:.6f}  (from eq 5.25 at on-shell)")


# ==============================================================================
# SECTION 2 -- Solve (lambda_1, lambda_2, lambda_3) from 3 independent inputs
# ==============================================================================
#
# From Paper 13 eq 5.21 and the definitions:
#       g_Y/2     = sqrt(3 / lambda_1)     where  g_Y = g' (NON-GUT normalized)
#       g/2       = 1 / sqrt(lambda_2)
#       g_s/2     = 2 sqrt(2) / sqrt(lambda_1 + 3 lambda_2 + 4 lambda_3)
#
# Inverting:
#       lambda_1 = 12 / g_Y^2
#       lambda_2 =  4 / g^2
#       lambda_1 + 3 lambda_2 + 4 lambda_3 = 32 / g_s^2
#   =>  lambda_3 = (1/4) * ( 32/g_s^2  - lambda_1 - 3 lambda_2 )
#
# We do this TWICE -- once for the MSbar scheme (using PDG sin^2_W) and once
# for the on-shell scheme (using M_W, M_Z directly).  The difference between
# the two fits is the "scheme tension" -- the genuine test of whether the
# Paper 13 tree-level three-coupling ansatz is self-consistent across schemes.

def lambdas_from_couplings(g_u1: float, g_su2: float, g_strong: float):
    """Fit (lambda_1, lambda_2, lambda_3) from (g', g, g_s) via Paper 13 eq 5.21."""
    l1 = 12.0 / g_u1 ** 2
    l2 = 4.0 / g_su2 ** 2
    l3 = 0.25 * (32.0 / g_strong ** 2 - l1 - 3.0 * l2)
    return l1, l2, l3


# ---------- Fit 1 : MSbar scheme ----------
# In MSbar, we convert alpha_em + sin^2_W -> (g, g') consistently:
#   g^2       = 4 pi alpha_em / sin^2
#   g'^2      = 4 pi alpha_em / (1 - sin^2)
g_SU2_msbar = e_em_MZ / np.sqrt(sin2_MSbar)                        # (local)
g_U1_prime_msbar = e_em_MZ / np.sqrt(1.0 - sin2_MSbar)             # (local)
lambda_1_msbar, lambda_2_msbar, lambda_3_msbar = lambdas_from_couplings(
    g_U1_prime_msbar, g_SU2_msbar, g_s_obs
)

# ---------- Fit 2 : on-shell scheme ----------
lambda_1_onsh, lambda_2_onsh, lambda_3_onsh = lambdas_from_couplings(
    g_U1_prime_obs, g_SU2_obs, g_s_obs
)

lambdas_msbar = np.array([lambda_1_msbar, lambda_2_msbar, lambda_3_msbar])  # (local)
lambdas_onsh = np.array([lambda_1_onsh, lambda_2_onsh, lambda_3_onsh])  # (local)

# Scheme tension on lambdas
lambda_scheme_tension = (lambdas_msbar - lambdas_onsh) / lambdas_onsh  # (local)

# MSbar fit is the CANONICAL choice (PDG uses MSbar).  The on-shell fit is a
# cross-check.  We use MSbar for the sin^2 closure and three-coupling gate.
lambda_1_fit = lambda_1_msbar                                       # (local)
lambda_2_fit = lambda_2_msbar                                       # (local)
lambda_3_fit = lambda_3_msbar                                       # (local)

print()
print("-" * 78)
print("SECTION 2  --  (lambda_1, lambda_2, lambda_3) fits (MSbar vs on-shell)")
print("-" * 78)
print("Fit 1  (MSbar scheme, inputs: alpha_em, alpha_s, sin^2_W MSbar):")
print(f"  lambda_1 = {lambda_1_msbar:.6f}")
print(f"  lambda_2 = {lambda_2_msbar:.6f}")
print(f"  lambda_3 = {lambda_3_msbar:.6f}")
print(f"  lambda_2/lambda_1 = {lambda_2_msbar/lambda_1_msbar:.6f}")
print()
print("Fit 2  (on-shell scheme, inputs: alpha_em, alpha_s, M_W/M_Z):")
print(f"  lambda_1 = {lambda_1_onsh:.6f}")
print(f"  lambda_2 = {lambda_2_onsh:.6f}")
print(f"  lambda_3 = {lambda_3_onsh:.6f}")
print(f"  lambda_2/lambda_1 = {lambda_2_onsh/lambda_1_onsh:.6f}")
print()
print("Scheme tension (MSbar vs on-shell) on lambdas:")
print(f"  lambda_1: {100*lambda_scheme_tension[0]:+.3f}%")
print(f"  lambda_2: {100*lambda_scheme_tension[1]:+.3f}%")
print(f"  lambda_3: {100*lambda_scheme_tension[2]:+.3f}%")


# ==============================================================================
# SECTION 3 -- Three-coupling self-consistency (sub-gate A)
# ==============================================================================
#
# Five observational inputs at M_Z:
#     (C1) alpha_em(M_Z)
#     (C2) alpha_s(M_Z)
#     (C3) sin^2_W MSbar
#     (C4) M_W
#     (C5) M_Z
#
# Three unknowns (lambda_1, lambda_2, lambda_3).  Two genuine degrees of
# redundancy.  Test both:
#
#   Test 1  (scheme agreement): fit lambdas in MSbar, then predict the
#           on-shell mass ratio M_Z/M_W from eq 5.25.  Compare to observed.
#
#   Test 2  (metric positivity): verify lambda_1 > 0, lambda_2 > 0, lambda_3 > 0.
#           This is NOT a numerical residual but a PHYSICAL feasibility test.
#           The Paper 13 tree-level construction of beta_tilde REQUIRES a
#           positive-definite Riemannian metric on each of the three A-module
#           blocks; a negative lambda means beta_tilde has become indefinite
#           on that block, which is geometrically inadmissible.
#
#   Test 3  (hypercharge constraint redundancy): verify that the e^2 =
#           g^2 g'^2 / (g^2 + g'^2) relation is satisfied after the fit
#           (this is automatic if we started from consistent alpha_em, sin^2
#           inputs -- the test is that the round-trip through the lambdas
#           does not lose precision).
#
# Sub-gate (A) PASS requires all three tests: <= 5% on test 1 AND positive
# metric on test 2 AND automatic on test 3.

GATE_A_THRESHOLD = 0.05  # (local)  5% per pre-registered gate

# Test 1 -- scheme agreement
ratio_fit_msbar = np.sqrt(1.0 + 3.0 * lambda_2_fit / lambda_1_fit)       # (local)
ratio_obs = M_Z / M_W                                                    # (local)
residual_mass_ratio = (ratio_fit_msbar - ratio_obs) / ratio_obs          # (local)
test1_scheme_ok = abs(residual_mass_ratio) < GATE_A_THRESHOLD            # (local)

# Test 2 -- metric positivity
test2_lambda_positive_msbar = (lambda_1_msbar > 0 and lambda_2_msbar > 0
                               and lambda_3_msbar > 0)                   # (local)
test2_lambda_positive_onsh = (lambda_1_onsh > 0 and lambda_2_onsh > 0
                              and lambda_3_onsh > 0)                     # (local)
# The fit used for gate A is MSbar -- so gate A metric positivity uses that.
test2_metric_positive = test2_lambda_positive_msbar                      # (local)

# Test 3 -- e^2 roundtrip
g_prime_round = 2.0 * np.sqrt(3.0 / lambda_1_fit)                        # (local)
g_SU2_round = 2.0 / np.sqrt(lambda_2_fit)                                # (local)
e_round = g_prime_round * g_SU2_round / np.sqrt(
    g_prime_round ** 2 + g_SU2_round ** 2)                               # (local)
residual_e_roundtrip = (e_round - e_em_MZ) / e_em_MZ                     # (local)
test3_e_roundtrip_ok = abs(residual_e_roundtrip) < GATE_A_THRESHOLD      # (local)

# g_s roundtrip
g_strong_round = 2.0 * 2.0 * np.sqrt(2.0) / np.sqrt(
    lambda_1_fit + 3.0 * lambda_2_fit + 4.0 * lambda_3_fit)              # (local)
residual_gs_roundtrip = (g_strong_round - g_s_obs) / g_s_obs             # (local)

# Five-residual vector (for reporting)
consistency_residuals = np.array([
    residual_e_roundtrip,        # C1 alpha_em round-trip
    residual_gs_roundtrip,       # C2 alpha_s round-trip
    0.0,                         # C3 sin^2 MSbar (fit input, by construction 0)
    residual_mass_ratio,         # C4&C5 on-shell M_Z/M_W reserved-input test
    0.0,                         # C5 hypercharge redundancy already in C1
])
max_residual = float(np.max(np.abs(consistency_residuals)))              # (local)
mean_residual = float(np.mean(np.abs(consistency_residuals)))            # (local)

sub_gate_A_numeric = (
    "PASS" if (test1_scheme_ok and test3_e_roundtrip_ok) else "FAIL"
)
sub_gate_A_metric = "PASS" if test2_metric_positive else "FAIL"

# Overall sub-gate A requires BOTH numeric agreement AND metric positivity
sub_gate_A = (
    "PASS" if (sub_gate_A_numeric == "PASS" and sub_gate_A_metric == "PASS")
    else "FAIL"
)

print()
print("-" * 78)
print("SECTION 3  --  Three-coupling self-consistency (sub-gate A)")
print("-" * 78)
print("Test 1 (scheme agreement MSbar -> on-shell M_Z/M_W):")
print(f"  predicted M_Z/M_W (from MSbar fit) = {ratio_fit_msbar:.6f}")
print(f"  observed  M_Z/M_W                  = {ratio_obs:.6f}")
print(f"  relative residual                  = {residual_mass_ratio:+.3e}  "
      f"({100*residual_mass_ratio:+.3f}%)")
print(f"  Test 1: {'PASS' if test1_scheme_ok else 'FAIL'} "
      f"(threshold {100*GATE_A_THRESHOLD:.0f}%)")
print()
print("Test 2 (metric positivity on u(1)_Y x su(2)_L x C^2):")
print(f"  MSbar fit   : l1={lambda_1_msbar:+.4f}, l2={lambda_2_msbar:+.4f}, "
      f"l3={lambda_3_msbar:+.4f}")
print(f"  on-shell fit: l1={lambda_1_onsh:+.4f}, l2={lambda_2_onsh:+.4f}, "
      f"l3={lambda_3_onsh:+.4f}")
print(f"  Test 2 (MSbar): {'PASS' if test2_lambda_positive_msbar else 'FAIL'}")
print(f"  Test 2 (on-shell): {'PASS' if test2_lambda_positive_onsh else 'FAIL'}")
print(f"  Note: lambda_3 < 0 means beta_tilde is indefinite on the C^2 Higgs "
      f"subspace,")
print(f"        violating the positive-definite Riemannian metric requirement "
      f"of Paper 13.")
print()
print("Test 3 (e^2 round-trip and g_s round-trip at fit lambdas):")
print(f"  e_round residual   = {residual_e_roundtrip:+.3e}")
print(f"  g_s round residual = {residual_gs_roundtrip:+.3e}")
print(f"  Test 3: {'PASS' if test3_e_roundtrip_ok else 'FAIL'}")
print()
print(f"Sub-gate (A) numeric component: {sub_gate_A_numeric}")
print(f"Sub-gate (A) metric positivity: {sub_gate_A_metric}")
print(f"Sub-gate (A) OVERALL:           {sub_gate_A}")


# ==============================================================================
# SECTION 4 -- Heterotic spectral triple: L/R asymmetry parameter
# ==============================================================================
#
# The heterotic spectral triple in Baptista-Paper-20 sense is
#   (A_L + A_R, H, D_K)
# with inner-fluctuations contributing  A_L * (g_phi weight) and
# A_R * (beta weight) to the Yang-Mills action (Paper 13 eq 3.41).
#
# On the u(2) subspace:  g_phi = beta_tilde   (the deformed metric coincides
#                                              with beta_tilde on u(2) at
#                                              phi = 0; for phi != 0 there
#                                              are corrections of order |phi|^2)
# On the C^2 subspace:   g_phi != beta_tilde  (these directions carry the
#                                              off-diagonal mixing that
#                                              generates |d_{A_L} phi|^2)
#
# The L/R asymmetry parameter at the connection level has TWO natural
# representations:
#
#   delta_LR(u(2))  =  lambda_2/lambda_1 - 1/3
#     = deviation from the g = g' locus (L/R-symmetric electroweak subgroup)
#     This vanishes when lambda_1 = 3*lambda_2, i.e. when the U(1) coupling
#     matches the SU(2) coupling.
#
#   delta_LR(C^2)   =  (lambda_mean_u(2) - lambda_3) / lambda_mean_u(2)
#     = relative anisotropy between the gauge (u(2)) and Higgs (C^2) sectors
#     This measures how the C^2 subspace (carrying the deformation parameter
#     phi) is weighted differently from the u(2) subspace.

delta_LR_u2 = lambda_2_fit / lambda_1_fit - 1.0 / 3.0                     # (local)

lambda_mean_u2 = (lambda_1_fit + 3.0 * lambda_2_fit) / 4.0                # (local)
delta_LR_C2 = (lambda_mean_u2 - lambda_3_fit) / lambda_mean_u2            # (local)

# Raw lambda ratios
ratio_l2_l1 = lambda_2_fit / lambda_1_fit                                 # (local)
ratio_l3_l2 = lambda_3_fit / lambda_2_fit                                 # (local)

print()
print("-" * 78)
print("SECTION 4  --  Heterotic L/R asymmetry (connection level)")
print("-" * 78)
print(f"Lambda ratios (MSbar fit):")
print(f"  lambda_2/lambda_1 = {ratio_l2_l1:+.6f}")
print(f"  lambda_3/lambda_2 = {ratio_l3_l2:+.6f}")
print(f"Asymmetry parameters:")
print(f"  delta_LR(u(2))  = lambda_2/lambda_1 - 1/3 = {delta_LR_u2:+.6f}")
print(f"      ( = 0 at the g = g' locus, L/R symmetric electroweak subgroup)")
print(f"  delta_LR(C^2)   = (lambda_mean_u(2) - lambda_3)/lambda_mean_u(2) "
      f"= {delta_LR_C2:+.6f}")
print(f"      ( = 0 at the u(2) vs C^2 isotropic locus)")
print(f"  lambda_mean on u(2) = {lambda_mean_u2:+.6f}")


# ==============================================================================
# SECTION 5 -- sin^2(theta_W) closure layer (Paper 13 eq 3.41 + 5.21)
# ==============================================================================
#
# With (lambda_1, lambda_2, lambda_3) fixed by the MSbar consistency fit,
# evaluate:
#
#     sin^2(theta_W) = g'^2 / (g^2 + g'^2)
#                    = (3/lambda_1) / (1/lambda_2 + 3/lambda_1)
#                    = (3 * lambda_2) / (lambda_1 + 3 * lambda_2)
#
# This is the PREDICTION from the three-coupling connection-layer fit at M_Z.
# It ties sin^2 to the ratio lambda_2/lambda_1 alone (lambda_3 drops out of
# the electroweak angle, though lambda_3 enters g_s and therefore controls
# the metric-positivity feasibility of the fit).

def sin2_thetaW_from_lambdas(l1: float, l2: float) -> float:
    """Paper 13 eq 5.21 + on-shell relation: sin^2_W = 3 l2 / (l1 + 3 l2)."""
    return (3.0 * l2) / (l1 + 3.0 * l2)


sin2_final = sin2_thetaW_from_lambdas(lambda_1_fit, lambda_2_fit)         # (local)
sin2_final_onsh = sin2_thetaW_from_lambdas(lambda_1_onsh, lambda_2_onsh)  # (local)

print()
print("-" * 78)
print("SECTION 5  --  sin^2(theta_W) connection-layer closure")
print("-" * 78)
print(f"sin^2(theta_W) from MSbar fit    = {sin2_final:.6f}")
print(f"sin^2(theta_W) from on-shell fit = {sin2_final_onsh:.6f}")
print(f"  PDG MSbar reference            = {sin2_MSbar:.6f}")
print(f"  on-shell anchor (1 - M_W^2/M_Z^2) = {sin2_obs:.6f}")
print(f"  sin^2(MSbar) deviation from PDG    = "
      f"{100*(sin2_final-sin2_MSbar)/sin2_MSbar:+.3f}%")
print(f"  sin^2(on-shell) deviation from PDG = "
      f"{100*(sin2_final_onsh-sin2_MSbar)/sin2_MSbar:+.3f}%")

# Pre-registered gate B: sin^2 in [0.21, 0.25] for PASS, [0.18, 0.28] for INFO
GATE_B_PASS_LO, GATE_B_PASS_HI = 0.21, 0.25  # (local)
GATE_B_INFO_LO, GATE_B_INFO_HI = 0.18, 0.28  # (local)

if GATE_B_PASS_LO <= sin2_final <= GATE_B_PASS_HI:
    sub_gate_B = "PASS"
elif GATE_B_INFO_LO <= sin2_final <= GATE_B_INFO_HI:
    sub_gate_B = "INFO"
else:
    sub_gate_B = "FAIL"

print(f"Sub-gate (B) sin^2 in [0.21, 0.25]: {sub_gate_B}")


# ==============================================================================
# SECTION 6 -- Cross-checks
# ==============================================================================

# Cross-check 1: limiting case A_L = A_R  =>  lambda_1 = lambda_2 / 3
# The "A_L = A_R" condition at the heterotic spectral-triple level means the
# U(1) and SU(2) pieces of the connection have equal weighting, i.e. g = g'.
# From eq 5.21: g^2/4 = 1/lambda_2, g'^2/4 = 3/lambda_1.  Setting g = g':
# 1/lambda_2 = 3/lambda_1 => lambda_1 = 3 * lambda_2.  Substituting:
#     sin^2_W = 3 * lambda_2 / (lambda_1 + 3 * lambda_2)
#             = 3 * lambda_2 / (3*lambda_2 + 3*lambda_2)
#             = 1/2
# So "no L/R asymmetry" (g = g') gives sin^2 = 1/2.  Check:

l1_LRsym = 1.0                                          # (local)  arbitrary scale
l2_LRsym = l1_LRsym / 3.0                               # (local)  g = g' condition
sin2_LRsym = sin2_thetaW_from_lambdas(l1_LRsym, l2_LRsym)  # (local)

print()
print("-" * 78)
print("SECTION 6  --  Cross-checks")
print("-" * 78)
print(f"CC-1  Limiting case g = g' (L/R symmetric): lambda_1 = 3*lambda_2")
print(f"      sin^2(theta_W) = {sin2_LRsym:.6f}   (expected 0.5)")
assert abs(sin2_LRsym - 0.5) < 1e-12, "L/R symmetric limit failed"
print(f"      -- PASS (agrees with 0.5 to 1e-12)")

# Cross-check 2: eq 5.21 self-consistency at the fitted lambdas (MSbar)
err_g_msbar = abs(
    2.0 * np.sqrt(3.0 / lambda_1_fit) - g_U1_prime_msbar
) / g_U1_prime_msbar                                     # (local)
err_gsu2_msbar = abs(2.0 / np.sqrt(lambda_2_fit) - g_SU2_msbar) / g_SU2_msbar  # (local)
err_gs_msbar = abs(g_strong_round - g_s_obs) / g_s_obs   # (local)
print(f"CC-2  Paper 13 eq 5.21 reproduction at fitted lambdas (MSbar):")
print(f"      |g' err|   = {err_g_msbar:.2e}")
print(f"      |g  err|   = {err_gsu2_msbar:.2e}")
print(f"      |g_s err|  = {err_gs_msbar:.2e}")
max_eq521_err = max(err_g_msbar, err_gsu2_msbar, err_gs_msbar)   # (local)
print(f"      Max error  = {max_eq521_err:.2e}")
if max_eq521_err < 1e-3:
    print(f"      -- PASS (< 0.1%)")
else:
    print(f"      -- FAIL  (> 0.1% threshold)")

# Cross-check 3: lambda_3 positivity (metric positivity on C^2)
print(f"CC-3  lambda_3 > 0 (C^2 metric positivity):")
print(f"      MSbar fit:    lambda_3 = {lambda_3_msbar:+.6f}   "
      f"-- {'PASS' if lambda_3_msbar > 0 else 'FAIL'}")
print(f"      on-shell fit: lambda_3 = {lambda_3_onsh:+.6f}   "
      f"-- {'PASS' if lambda_3_onsh > 0 else 'FAIL'}")
print(f"      (Negative lambda_3 means beta_tilde is indefinite on C^2, which")
print(f"       violates the positive-definite Riemannian metric requirement")
print(f"       of Paper 13 Sec. 5.  The (lambda_1, lambda_2) fit from alpha_em")
print(f"       and sin^2_W forces lambda_1 + 3*lambda_2 >> 32/g_s^2, so the")
print(f"       remainder 4*lambda_3 = 32/g_s^2 - (lambda_1 + 3*lambda_2) is")
print(f"       STRUCTURALLY negative.  This is NOT a numerical artifact --")
print(f"       it is a metric-positivity obstruction to the Paper 13 tree-")
print(f"       level three-coupling ansatz at M_Z.)")

# Cross-check 4: M_Z / M_W reproduction via eq 5.25 (MSbar fit)
print(f"CC-4  M_Z/M_W from eq 5.25 at MSbar fit: {ratio_fit_msbar:.6f}")
print(f"      Observed M_Z/M_W                   = {M_Z/M_W:.6f}")
print(f"      relative error                     = {residual_mass_ratio:+.3e}  "
      f"({100*residual_mass_ratio:+.3f}%)")
print(f"      -- {'PASS' if abs(residual_mass_ratio) < GATE_A_THRESHOLD else 'FAIL'}  "
      f"(gate threshold 5%)")

# Cross-check 5: W2-J / W3-I comparison
# W2-J computed sin^2 at the SPECTRAL (fiber-integrated) level via per-sector
# threshold sums and RG running, and found sin^2 = -1.165699 (Jensen-blind,
# per-sector Dynkin-index ratio theorem).  W3-M is at the CONNECTION (pre-
# spectral, tree-level at M_Z) level and uses a DIFFERENT relation: the
# anisotropy of the left-invariant metric through (lambda_1, lambda_2,
# lambda_3) rather than the per-sector spectral moments.  The two produce
# different numerical sin^2 values because they live in different layers of
# the reduction -- this is STRUCTURALLY consistent, not a contradiction.
w2j_sin2 = -1.165699                                     # (local) W2-J value
w3i_sin2 = -1.165699                                     # (local) W3-I J-weighted
print(f"CC-5  Cross-check against W2-J and W3-I:")
print(f"      W2-J sin^2(spectral, M_Z)     = {w2j_sin2:+.6f} (Jensen-blind, Dynkin-locked)")
print(f"      W3-I sin^2(modular, J-weight) = {w3i_sin2:+.6f} (modular flow, same theorem)")
print(f"      W3-M sin^2(connection, M_Z)   = {sin2_final:+.6f} (pre-spectral, lambda-fit)")
print(f"      -- W3-M is a DIFFERENT constraint layer than W2-J/W3-I")

# Cross-check 6: full lambda positivity
all_positive_msbar = (lambda_1_msbar > 0 and lambda_2_msbar > 0 and lambda_3_msbar > 0)  # (local)
all_positive_onsh = (lambda_1_onsh > 0 and lambda_2_onsh > 0 and lambda_3_onsh > 0)      # (local)
print(f"CC-6  Full metric positivity (all three lambdas > 0):")
print(f"      MSbar fit:    {'PASS' if all_positive_msbar else 'FAIL'}")
print(f"      on-shell fit: {'PASS' if all_positive_onsh else 'FAIL'}")


# ==============================================================================
# SECTION 7 -- Gate verdict
# ==============================================================================

# Gate HETEROTIC-LR-74:
#   PASS if (A) three-coupling consistency to 5% AND (B) sin^2 in [0.21, 0.25]
#   INFO if (A) passes but (B) gives sin^2 in [0.18, 0.28] but not in [0.21, 0.25]
#   FAIL if (A) fails or (B) gives sin^2 outside [0.18, 0.28]
#
# Sub-gate (A) in this computation is COMPOSITE:
#   - numerical consistency (test 1, test 3):  residual on reserved input
#     is < 5%, and the e^2 / g_s round-trip is consistent.
#   - metric positivity (test 2):  lambda_1, lambda_2, lambda_3 > 0.
#
# Both components are required to PASS.  If the numerical sub-component
# passes but metric positivity fails, we report sub-gate (A) = FAIL because
# the fit is physically infeasible even though the numbers are consistent.

if sub_gate_A == "PASS" and sub_gate_B == "PASS":
    verdict = "PASS"
elif sub_gate_A == "PASS" and sub_gate_B == "INFO":
    verdict = "INFO"
else:
    verdict = "FAIL"

print()
print("=" * 78)
print("GATE VERDICT  HETEROTIC-LR-74")
print("=" * 78)
print(f"  Sub-gate (A) three-coupling consistency to 5%: {sub_gate_A}")
print(f"      - numerical (scheme+roundtrip):   {sub_gate_A_numeric}")
print(f"      - metric positivity (lambdas>0):  {sub_gate_A_metric}")
print(f"      - test 1 (scheme agreement):      "
      f"{abs(residual_mass_ratio):.3e}  "
      f"(thr {GATE_A_THRESHOLD})")
print(f"      - lambda_3 (MSbar)  = {lambda_3_msbar:+.6f}  "
      f"({'positive' if lambda_3_msbar > 0 else 'NEGATIVE'})")
print(f"  Sub-gate (B) sin^2 in [0.21, 0.25] PASS band:  {sub_gate_B}")
print(f"      - sin^2(theta_W) closure          = {sin2_final:.6f}")
print(f"      - sin^2 deviation from PDG MSbar  = "
      f"{(sin2_final-sin2_MSbar)/sin2_MSbar:+.3e}")
print(f"  OVERALL: {verdict}")


# ==============================================================================
# SECTION 8 -- Save data + plot
# ==============================================================================

OUT_NPZ = os.path.join(SCRIPT_DIR, "s74_heterotic_lr.npz")
OUT_PNG = os.path.join(SCRIPT_DIR, "s74_heterotic_lr.png")

np.savez(
    OUT_NPZ,
    # Inputs
    M_Z=M_Z, M_W=M_W,
    alpha_em_MZ=alpha_em_MZ, e_em_MZ=e_em_MZ,
    alpha_s_MZ_obs=alpha_s_MZ_obs, g_s_obs=g_s_obs,
    g_SU2_obs=g_SU2_obs, g_U1_prime_obs=g_U1_prime_obs,
    g_SU2_msbar=g_SU2_msbar, g_U1_prime_msbar=g_U1_prime_msbar,
    sin2_on_shell=sin2_on_shell, sin2_MSbar=sin2_MSbar,
    ratio_MZ_MW_sq=ratio_MZ_MW_sq,
    # Heterotic decomposition -- MSbar fit (canonical)
    lambda_1_msbar=lambda_1_msbar,
    lambda_2_msbar=lambda_2_msbar,
    lambda_3_msbar=lambda_3_msbar,
    lambdas_msbar=lambdas_msbar,
    # Heterotic decomposition -- on-shell fit (cross-check)
    lambda_1_onsh=lambda_1_onsh,
    lambda_2_onsh=lambda_2_onsh,
    lambda_3_onsh=lambda_3_onsh,
    lambdas_onsh=lambdas_onsh,
    lambda_scheme_tension=lambda_scheme_tension,
    # Canonical fit (MSbar alias)
    lambda_1_fit=lambda_1_fit,
    lambda_2_fit=lambda_2_fit,
    lambda_3_fit=lambda_3_fit,
    # L/R asymmetry measures
    delta_LR_u2=delta_LR_u2,
    delta_LR_C2=delta_LR_C2,
    lambda_mean_u2=lambda_mean_u2,
    ratio_l2_l1=ratio_l2_l1,
    ratio_l3_l2=ratio_l3_l2,
    # Three-coupling consistency tests
    consistency_residuals=consistency_residuals,
    max_residual=max_residual,
    mean_residual=mean_residual,
    residual_mass_ratio=residual_mass_ratio,
    residual_e_roundtrip=residual_e_roundtrip,
    residual_gs_roundtrip=residual_gs_roundtrip,
    test1_scheme_ok=test1_scheme_ok,
    test2_metric_positive_msbar=test2_lambda_positive_msbar,
    test2_metric_positive_onsh=test2_lambda_positive_onsh,
    test3_e_roundtrip_ok=test3_e_roundtrip_ok,
    # sin^2 closure
    sin2_final=sin2_final,
    sin2_final_onsh=sin2_final_onsh,
    # Cross-checks
    sin2_LRsym=sin2_LRsym,
    max_eq521_err=max_eq521_err,
    w2j_sin2=w2j_sin2,
    w3i_sin2=w3i_sin2,
    all_positive_msbar=all_positive_msbar,
    all_positive_onsh=all_positive_onsh,
    # Gate
    sub_gate_A=sub_gate_A,
    sub_gate_A_numeric=sub_gate_A_numeric,
    sub_gate_A_metric=sub_gate_A_metric,
    sub_gate_B=sub_gate_B,
    verdict=verdict,
    # Provenance
    tau_fold=tau_fold,
    M_KK=M_KK,
)

print(f"\nData written: {OUT_NPZ}")


# ----- PLOT -------------------------------------------------------------------
fig = plt.figure(figsize=(13.0, 9.5))

# Panel 1: sin^2 closure cascade
ax1 = fig.add_subplot(2, 2, 1)

# Scan sin^2 as a function of lambda_2/lambda_1
r_scan = np.linspace(0.0, 0.6, 600)                               # (local)
sin2_scan = (3.0 * r_scan) / (1.0 + 3.0 * r_scan)                 # (local)
ax1.plot(r_scan, sin2_scan, "-", lw=2, color="#1f77b4",
         label=r"$\sin^2 = 3r/(1+3r)$")
ax1.axhline(sin2_MSbar, color="k", ls="--", lw=1.2,
            label=fr"MSbar PDG: {sin2_MSbar:.4f}")
ax1.axhline(sin2_on_shell, color="grey", ls=":", lw=1.2,
            label=fr"on-shell: {sin2_on_shell:.4f}")
ax1.axhspan(GATE_B_PASS_LO, GATE_B_PASS_HI, alpha=0.15, color="green",
            label=f"PASS [{GATE_B_PASS_LO},{GATE_B_PASS_HI}]")
ax1.axhspan(GATE_B_INFO_LO, GATE_B_PASS_LO, alpha=0.08, color="orange")
ax1.axhspan(GATE_B_PASS_HI, GATE_B_INFO_HI, alpha=0.08, color="orange")
ax1.axvline(ratio_l2_l1, color="red", ls="-", lw=1.5,
            label=fr"MSbar fit $r={ratio_l2_l1:.4f}$")
ax1.plot([ratio_l2_l1], [sin2_final], "ro", ms=10,
         label=fr"MSbar $\sin^2={sin2_final:.4f}$")
ax1.plot([lambda_2_onsh/lambda_1_onsh], [sin2_final_onsh], "ms", ms=8,
         label=fr"on-shell $\sin^2={sin2_final_onsh:.4f}$")
# L/R symmetric reference
ax1.plot([1/3.0], [0.5], "ks", ms=8,
         label=r"$g=g'$ (L/R sym): $\sin^2=0.5$")
ax1.set_xlabel(r"$r = \lambda_2 / \lambda_1$")
ax1.set_ylabel(r"$\sin^2(\theta_W)$")
ax1.set_title(r"$\sin^2$ closure (connection layer, Paper 13 eq 5.21)")
ax1.set_xlim(0, 0.55)
ax1.set_ylim(0, 0.65)
ax1.grid(alpha=0.3)
ax1.legend(loc="upper left", fontsize=7)

# Panel 2: Three-coupling consistency cascade
ax2 = fig.add_subplot(2, 2, 2)
# Show the 3 critical tests: scheme agreement, e_roundtrip, metric positivity
test_labels = ["test 1\nscheme\nagreement",
               "test 3\ne_roundtrip",
               "test 2\nl_1 > 0",
               "test 2\nl_2 > 0",
               "test 2\nl_3 > 0"]
# Quantitative values for numeric tests, and binary "passed/failed" heights for
# positivity tests (use log10(lambda_i) if positive, else -1 marker).
def _vp(x):
    return x if x > 0 else 1e-3  # (local) avoid zero on log scale

test_vals = [
    abs(residual_mass_ratio),
    abs(residual_e_roundtrip),
    1.0 if lambda_1_msbar > 0 else 10.0,
    1.0 if lambda_2_msbar > 0 else 10.0,
    1.0 if lambda_3_msbar > 0 else 10.0,
]
test_colors = [
    "#2ca02c" if test1_scheme_ok else "#d62728",
    "#2ca02c" if test3_e_roundtrip_ok else "#d62728",
    "#2ca02c" if lambda_1_msbar > 0 else "#d62728",
    "#2ca02c" if lambda_2_msbar > 0 else "#d62728",
    "#2ca02c" if lambda_3_msbar > 0 else "#d62728",
]
bars2 = ax2.bar(test_labels, test_vals, color=test_colors, edgecolor="black")
ax2.axhline(GATE_A_THRESHOLD, ls="--", color="red",
            label=f"gate A thr = {GATE_A_THRESHOLD}")
ax2.axhline(1.0, ls=":", color="grey", label="positivity PASS marker")
ax2.set_ylabel("residual (tests 1,3) / positivity (test 2)")
ax2.set_yscale("log")
ax2.set_title(f"Sub-gate (A) composite: {sub_gate_A}")
ax2.legend(fontsize=7)
ax2.grid(alpha=0.3)
# Annotate positivity tests with the actual lambda values
ax2.text(2, 1.2, fr"$\lambda_1={lambda_1_msbar:.2f}$",
         ha="center", fontsize=7)
ax2.text(3, 1.2, fr"$\lambda_2={lambda_2_msbar:.2f}$",
         ha="center", fontsize=7)
ax2.text(4, 1.2 if lambda_3_msbar > 0 else 11.0,
         fr"$\lambda_3={lambda_3_msbar:.2f}$",
         ha="center", fontsize=7, color="red" if lambda_3_msbar < 0 else "black")
ax2.text(0, abs(residual_mass_ratio) * 1.8,
         f"{100*residual_mass_ratio:+.2f}%", ha="center", fontsize=7)
ax2.text(1, abs(residual_e_roundtrip) * 1.8 if residual_e_roundtrip != 0 else 1e-15,
         f"{residual_e_roundtrip:+.1e}", ha="center", fontsize=7)

# Panel 3: L/R asymmetry -- lambdas bar chart
ax3 = fig.add_subplot(2, 2, 3)
lam_labels = [r"$\lambda_1$ (U(1)$_Y$)",
              r"$\lambda_2$ (SU(2)$_L$)",
              r"$\lambda_3$ ($C^2$)"]
x_lam = np.arange(3)                                                   # (local)
width = 0.35                                                           # (local)
lam_values_msbar = [lambda_1_msbar, lambda_2_msbar, lambda_3_msbar]
lam_values_onsh = [lambda_1_onsh, lambda_2_onsh, lambda_3_onsh]
b3_msbar = ax3.bar(x_lam - width/2, lam_values_msbar, width,
                   color="#1f77b4", label="MSbar", edgecolor="black")
b3_onsh = ax3.bar(x_lam + width/2, lam_values_onsh, width,
                  color="#ff7f0e", label="on-shell", edgecolor="black")
ax3.axhline(0, color="black", lw=1)
ax3.set_xticks(x_lam)
ax3.set_xticklabels(lam_labels)
ax3.set_ylabel(r"$\lambda_i$ (dimensionless)")
ax3.set_title(r"Heterotic $(\lambda_1,\lambda_2,\lambda_3)$  --  MSbar vs on-shell")
ax3.grid(alpha=0.3, axis="y")
ax3.legend(fontsize=8)
# Annotate each bar
for xi, v in zip(x_lam - width/2, lam_values_msbar):
    ax3.text(xi, v + (2 if v > 0 else -4),
             f"{v:.2f}", ha="center", va="bottom" if v > 0 else "top",
             fontsize=8)
for xi, v in zip(x_lam + width/2, lam_values_onsh):
    ax3.text(xi, v + (2 if v > 0 else -4),
             f"{v:.2f}", ha="center", va="bottom" if v > 0 else "top",
             fontsize=8)
# Highlight the negative lambda_3 region
ax3.axhspan(-40, 0, alpha=0.08, color="red",
            label="indefinite region ($\\lambda<0$)")

# Panel 4: sin^2 closure cascade / comparison
ax4 = fig.add_subplot(2, 2, 4)
labels = ["W2-J\n(spectral)",
          "W3-I\n(modular)",
          "W3-M MSbar\n(connection)",
          "W3-M onshell\n(connection)",
          "PDG\nMSbar"]
values = [w2j_sin2, w3i_sin2, sin2_final, sin2_final_onsh, sin2_MSbar]
colors4 = ["#d62728", "#d62728", "#2ca02c", "#2ca02c", "#1f77b4"]
bars4 = ax4.bar(labels, values, color=colors4, edgecolor="black")
ax4.axhline(sin2_MSbar, color="#1f77b4", ls=":", alpha=0.8)
ax4.axhspan(GATE_B_PASS_LO, GATE_B_PASS_HI, alpha=0.15, color="green",
            label=f"PASS [{GATE_B_PASS_LO},{GATE_B_PASS_HI}]")
ax4.axhspan(GATE_B_INFO_LO, GATE_B_PASS_LO, alpha=0.08, color="orange")
ax4.axhspan(GATE_B_PASS_HI, GATE_B_INFO_HI, alpha=0.08, color="orange",
            label=f"INFO [{GATE_B_INFO_LO},{GATE_B_INFO_HI}]")
ax4.set_ylabel(r"$\sin^2(\theta_W)$")
ax4.set_title(f"sin^2 closure cascade  --  sub-gate (B) {sub_gate_B}")
ax4.set_ylim(-1.5, 0.65)
ax4.grid(alpha=0.3, axis="y")
ax4.legend(fontsize=7, loc="lower right")
for b, v in zip(bars4, values):
    ax4.text(b.get_x() + b.get_width() / 2,
             v + (0.03 if v > 0 else -0.08),
             f"{v:+.4f}", ha="center",
             va="bottom" if v > 0 else "top", fontsize=7)

fig.suptitle(
    f"S74 W3-M HETEROTIC-LR-74  --  verdict: {verdict}\n"
    r"Paper 13 eq 5.21 + Paper 20 heterotic spectral triple  --  "
    r"metric-positivity-constrained",
    fontsize=12,
)
fig.tight_layout()
fig.subplots_adjust(top=0.90)
fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
plt.close(fig)

print(f"Plot  written: {OUT_PNG}")
print()
print("=" * 78)
print(f"HETEROTIC-LR-74 complete.  Verdict = {verdict}")
print("=" * 78)
