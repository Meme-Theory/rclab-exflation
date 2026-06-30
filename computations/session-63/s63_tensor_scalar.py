#!/usr/bin/env python3
"""
TENSOR-SCALAR-63 (W2-02): Tensor-to-Scalar Ratio r
====================================================

Session 63, Wave 2, Task W2-02.
Agent: schwarzschild-penrose-geometer

EXISTENTIAL TEST: r = 16*epsilon = 0.35 single-field is 10x above BICEP/Keck
r < 0.036. Two proposed escape routes:
  (1) R^2 Starobinsky suppression from a_4
  (2) Multi-field suppression from 36-mode trajectory

Method:
  1. Decompose a_4 = a_4^{R^2} + a_4^{Ric^2} + a_4^{gauge} using Gilkey formula.
     Extract c_{R^2} and Starobinsky mass M_s^2 = M_Pl^2/(6*f_0*c_{R^2}).
  2. Compute multi-field suppression: project Jensen direction onto trace mode.
     sin^2(alpha) = |projection onto tensor-generating direction|^2.
  3. Sound speed: determine whether c_s = 0.485 from W1-04 is the adiabatic
     perturbation sound speed (DBI-type) or a modulus-space diagnostic.
  4. Starobinsky: compute m_s and compare to H(A_s). If m_s >> H, scalaron
     is frozen and provides no suppression.
  5. Report all channels and the definitive combined r.

Gate: TENSOR-SCALAR-63
  PASS if r < 0.036
  FAIL if r > 0.1
  INFO if in [0.036, 0.1]

Inputs:
  - computations/session-62/s62_hessian_oneloop.npz
  - computations/session-62/s62_kz_ns.npz
  - computations/session-62/s62_cutoff_london.npz
  - computations/session-63/s63_sound_speed.npz
  - computations/session-54/s54_starobinsky_r2.npz

Outputs:
  - computations/session-63/s63_tensor_scalar.npz
  - computations/session-63/s63_tensor_scalar.png

Author: schwarzschild-penrose-geometer (Session 63)
Date: 2026-03-30
"""

import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI,
    a0_fold, a2_fold, a4_fold,
    M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, M_Pl_unreduced,
    S_fold, dS_fold, d2S_fold,
    Z_fold, G_DeWitt, H_fold,
    A_s_CMB,
)

t_start = time.time()

print("=" * 76)
print("  TENSOR-SCALAR-63 (W2-02): Tensor-to-Scalar Ratio r")
print("=" * 76)

# =============================================================================
#  SECTION 1: Load All Input Data
# =============================================================================
print("\n[SECTION 1] Loading input data")
print("-" * 60)

d_hess = np.load('s62_hessian_oneloop.npz', allow_pickle=True)
H_eff = d_hess['H_eff']
evals_eff = d_hess['evals_eff']
evecs_eff = d_hess['evecs_eff']
g_fold = d_hess['g_fold']

d_kz = np.load('s62_kz_ns.npz', allow_pickle=True)
epsilon_H = float(d_kz['epsilon_H_SA'])
f0 = float(d_kz['f0'])
f2 = float(d_kz['f2'])
f4 = float(d_kz['f4'])
a0_gilkey = float(d_kz['a0_gilkey'])
a4_gilkey = float(d_kz['a4_gilkey'])

d_cs = np.load('s63_sound_speed.npz', allow_pickle=True)
c_s = float(d_cs['c_s'])
c_s_sq = float(d_cs['c_s_sq'])
G_tau_tau = float(d_cs['G_tau_tau'])
v_transit = float(d_cs['v_transit'])
Mach = float(d_cs['v_over_cs'])

d_s54 = np.load('s54_starobinsky_r2.npz', allow_pickle=True)
alpha_R2_s54 = float(d_s54['alpha_R2'])
N_KK = float(d_s54['N_KK'])

print(f"  epsilon_H = {epsilon_H:.6f}")
print(f"  c_s (W1-04) = {c_s:.4f}")
print(f"  G_tau_tau = {G_tau_tau:.1f}")
print(f"  Mach = {Mach:.2f}")
print(f"  f_0 = {f0:.6f}, f_2 = {f2:.6f}, f_4 = {f4:.6f}")
print(f"  alpha_R2 (S54) = {alpha_R2_s54:.4f}")
print(f"  N_KK = {N_KK:.0f}")
print(f"  Hessian evals: min={evals_eff.min():.2f}, max={evals_eff.max():.2f}, all>0={np.all(evals_eff>0)}")

# =============================================================================
#  SECTION 2: Single-Field Baseline
# =============================================================================
print("\n[SECTION 2] Single-field baseline")
print("-" * 60)

r_naive = 16.0 * epsilon_H
print(f"  r_naive = 16 * epsilon_H = 16 * {epsilon_H:.6f} = {r_naive:.6f}")
print(f"  BICEP/Keck bound: r < 0.036")
print(f"  Exceeds bound by factor {r_naive / 0.036:.1f}x")

# =============================================================================
#  SECTION 3: a_4 Gilkey Decomposition
# =============================================================================
print("\n[SECTION 3] a_4 Gilkey decomposition (R^2 fraction)")
print("-" * 60)

# Curvature invariants at fold
def R_scalar(s):
    return -0.25 * np.exp(-4*s) + 2.0 * np.exp(-s) - 0.25 + 0.5 * np.exp(2*s)

def Ric2_exact(s):
    return (
        (1.0/12) * np.exp(-8*s) + (-1.0/2) * np.exp(-5*s) + (1.0/8) * np.exp(-4*s)
        + (13.0/12) * np.exp(-2*s) + (-1.0/2) * np.exp(-s) + 1.0/8
        + (1.0/12) * np.exp(4*s)
    )

def K_exact(s):
    return (
        (23.0/96) * np.exp(-8*s) + (-1.0) * np.exp(-5*s) + (5.0/16) * np.exp(-4*s)
        + (11.0/6) * np.exp(-2*s) + (-3.0/2) * np.exp(-s) + 17.0/32
        + (1.0/12) * np.exp(4*s)
    )

R_fold = R_scalar(tau_fold)
Ric2_fold = Ric2_exact(tau_fold)
K_fold = K_exact(tau_fold)

# Numerical coefficients from spectral action (verified S20a, S61):
# a_4 integrand = (500*R^2 - 32*|Ric|^2 - 28*K) / 360
c_R2_num = 500.0  # (local)
c_Ric2_num = -32.0  # (local)
c_K_num = -28.0  # (local)

term_R2 = c_R2_num * R_fold**2
term_Ric2 = c_Ric2_num * Ric2_fold
term_K = c_K_num * K_fold
total_integrand = term_R2 + term_Ric2 + term_K
frac_R2 = term_R2 / total_integrand

print(f"  R(fold) = {R_fold:.6f}, |Ric|^2 = {Ric2_fold:.6f}, K = {K_fold:.6f}")
print(f"  a_4 integrand contributions:")
print(f"    500*R^2     = {term_R2:.2f}  ({100*term_R2/total_integrand:.1f}%)")
print(f"    -32*|Ric|^2 = {term_Ric2:.2f}  ({100*term_Ric2/total_integrand:.1f}%)")
print(f"    -28*K       = {term_K:.2f}  ({100*term_K/total_integrand:.1f}%)")
print(f"    Total       = {total_integrand:.2f}")
print(f"  R^2 fraction = {frac_R2:.4f} = {100*frac_R2:.1f}%")
print(f"  NEAR-EINSTEIN: a_4 dominated by R^2 (fold is nearly Einstein)")

# =============================================================================
#  SECTION 4: Scalaron Mass from Spectral Action R^2
# =============================================================================
print("\n[SECTION 4] Starobinsky scalaron mass")
print("-" * 60)

# From spectral action on M^4 x K:
#   M_Pl^2/2 = f_2 * Lambda^2 * a_0(K) / (24*pi^2)
#   c_{R^2} = f_0 * a_0(K) * 125 / (16*pi^2*360)
#
# Scalaron mass: m_s^2 = M_Pl^2 / (12*c_{R^2})
# Using ratio (a_0(K) cancels):
#   m_s^2 = [f_2*Lambda^2/(12*pi^2)] / [12*f_0*125/(16*pi^2*360)]
#         = f_2*Lambda^2*16*360 / (12*12*f_0*125)
#         = f_2*Lambda^2*5760 / (18000*f_0)
#         = f_2*Lambda^2*0.32 / f_0

m_s_sq_MKK2 = f2 * 0.32 / f0
m_s_MKK = np.sqrt(m_s_sq_MKK2)
m_s_GeV = m_s_MKK * M_KK_gravity

print(f"  m_s^2 = f_2*Lambda^2 * 0.32 / f_0")
print(f"        = {f2:.4f} * 0.32 / {f0:.4f} * M_KK^2")
print(f"        = {m_s_sq_MKK2:.6f} M_KK^2")
print(f"  m_s   = {m_s_MKK:.4f} M_KK = {m_s_GeV:.3e} GeV")

# M_Pl from spectral action:
M_Pl_SA = np.sqrt(2.0 * f2 * M_KK_gravity**2 * a0_fold / (24.0 * PI**2))
print(f"\n  M_Pl (spectral action) = {M_Pl_SA:.3e} GeV")
print(f"  M_Pl (reduced, PDG)    = {M_Pl_reduced:.3e} GeV")
print(f"  M_Pl_SA / M_Pl_PDG    = {M_Pl_SA/M_Pl_reduced:.4f}")
print(f"  NOTE: spectral action underestimates M_Pl by 3x")
print(f"  (requires Lambda ~ 2.9x M_KK to match, or larger a_0(K))")

# Hubble rate from CMB normalization:
# P_s = H^2/(8*pi^2*eps*M_Pl^2) = A_s = 2.1e-9
# Use the PHYSICAL M_Pl for this (cosmological observation):
H_phys = np.sqrt(8.0 * PI**2 * epsilon_H * M_Pl_reduced**2 * A_s_CMB)
H_SA = np.sqrt(8.0 * PI**2 * epsilon_H * M_Pl_SA**2 * A_s_CMB)

print(f"\n  H (from A_s, physical M_Pl) = {H_phys:.3e} GeV")
print(f"  H (from A_s, SA M_Pl)       = {H_SA:.3e} GeV")
print(f"  m_s / H_phys = {m_s_GeV/H_phys:.0f}x")
print(f"  m_s / H_SA   = {m_s_GeV/H_SA:.0f}x")

# Verdict on Starobinsky:
print(f"\n  VERDICT: m_s = {m_s_GeV/H_phys:.0f}x H  (using physical M_Pl)")
print(f"           m_s = {m_s_GeV/H_SA:.0f}x H  (using SA M_Pl)")
print(f"  The scalaron is HEAVY (>> H). It is FROZEN during the expansion.")
print(f"  Quantum fluctuations: delta_sigma ~ (H/2pi)*exp(-m_s^2/(2H^2))")
print(f"  Suppression: exp(-m_s^2/(2H^2)) = exp(-{m_s_GeV**2/(2*H_phys**2):.0f}) ~ 0")
print(f"  STAROBINSKY ROUTE CLOSED: scalaron too heavy for suppression.")

staro_suppression = 1.0  # No suppression from this channel  # (local)

# =============================================================================
#  SECTION 5: Sound Speed Assessment
# =============================================================================
print("\n[SECTION 5] Sound speed assessment")
print("-" * 60)

# W1-04 found c_s = 0.485 from c_s^2 = Z_spectral / d^2S.
# CRITICAL QUESTION: Is this the adiabatic perturbation sound speed?
#
# For L = Z(tau)*X - V(tau) with X = (1/2)*tau_dot^2:
#   P_X = Z(tau), P_XX = 0
#   c_s^2 = P_X / (P_X + 2*X*P_XX) = 1  (canonical)
#
# The c_s = 0.485 is the ratio of two DIFFERENT quantities:
#   Z_spectral = spectral gradient stiffness (from eigenvalue sum)
#   d^2S = second derivative of total spectral action
# These differ because d^2S includes terms beyond the gradient stiffness.
#
# In the Mukhanov-Sasaki equation for a single canonical scalar:
#   v'' + (k^2 - z''/z)*v = 0  with z^2 = 2*eps*a^2*M_Pl^2
# The propagation speed is c_s = 1 (coefficient of k^2).
#
# The c_s < 1 would arise from a non-canonical kinetic term P(X,phi)
# where P_XX != 0 (DBI inflation, k-inflation).
# Our spectral action, after KK reduction, gives L = Z(tau)*X - V(tau).
# This IS canonical (field-dependent kinetic coefficient Z(tau) can be
# absorbed by canonical normalization sigma = integral sqrt(Z) dtau).
# After normalization: L = X_sigma - V(sigma), giving c_s = 1.
#
# HOWEVER: there is a subtlety. The spectral action is a SUM over KK modes:
#   S = sum_n f(lambda_n^2(tau)/Lambda^2) * g_n
# Each mode has tau-dependent eigenvalue lambda_n(tau).
# The effective kinetic term is:
#   T = sum_n f'(lambda_n^2/Lambda^2) * 2*lambda_n*(dlambda_n/dtau)^2/Lambda^2 * g_n
# This is NOT simply Z*X. It has a non-trivial structure that could give c_s < 1.
#
# The question is: does the KK tower produce an EFFECTIVE P(X,phi) theory
# with P_XX != 0? This requires analyzing the perturbation equation directly,
# which is beyond what W1-04 computed.
#
# CONSERVATIVE ASSESSMENT: c_s = 1 for the adiabatic perturbation.
# The c_s = 0.485 from W1-04 is an internal modulus diagnostic.
# If future computation shows the spectral action kinetic structure
# gives P_XX != 0, then c_s < 1 is physical.

print(f"  c_s (W1-04) = {c_s:.4f} (modulus space diagnostic)")
print(f"  c_s (adiabatic perturbation, canonical) = 1.000")
print(f"  CONSERVATIVE: use c_s = 1 (canonical scalar)")
print(f"  OPTIMISTIC: use c_s = 0.485 (if spectral sum gives DBI-like kinetics)")

c_s_conservative = 1.0  # (local)
c_s_optimistic = c_s

r_conservative = 16.0 * epsilon_H * c_s_conservative  # = 0.346
r_optimistic = 16.0 * epsilon_H * c_s_optimistic      # = 0.168

print(f"\n  r (c_s=1):     {r_conservative:.4f}")
print(f"  r (c_s=0.485): {r_optimistic:.4f}")

# =============================================================================
#  SECTION 6: Multi-Field Projection
# =============================================================================
print("\n[SECTION 6] Multi-field projection")
print("-" * 60)

# Jensen direction: dg/g = (-2,-2,-2, 1,1,1,1, 2)
dg_over_g = np.array([-2.0, -2.0, -2.0, 1.0, 1.0, 1.0, 1.0, 2.0])

# Trace direction: (1,1,1,1,1,1,1,1)
trace_dir = np.ones(8)

norm_t = np.linalg.norm(dg_over_g)
norm_tr = np.linalg.norm(trace_dir)
cos_alpha = np.dot(dg_over_g, trace_dir) / (norm_t * norm_tr)
sin2_alpha = 1.0 - cos_alpha**2

print(f"  Jensen direction (dg/g): {dg_over_g}")
print(f"  Trace direction: {trace_dir}")
print(f"  cos(alpha) = {cos_alpha:.2e} (MACHINE ZERO)")
print(f"  sin^2(alpha) = {sin2_alpha:.10f}")
print(f"\n  STRUCTURAL THEOREM: Jensen (volume-preserving) EXACTLY orthogonal to trace.")
print(f"  sum(dg/g) = 3*(-2) + 4*(1) + 1*(2) = {3*(-2)+4*1+1*2} (volume preserved)")
print(f"\n  IMPORTANT: This does NOT suppress the tensor spectrum.")
print(f"  P_t = 2*H^2/(pi^2*M_Pl^2) depends on H and M_Pl alone (de Sitter vacuum).")
print(f"  The modulus merely drives the expansion; tensors are a background property.")
print(f"  sin^2(alpha)=0 means the modulus-metric MIXING vanishes,")
print(f"  but the graviton vacuum fluctuations (which produce P_t) persist.")

# Isocurvature modes:
m_iso_sq = evals_eff
# Self-consistent H in M_KK units:
H_MKK_phys = H_phys / M_KK_gravity

print(f"\n  Isocurvature masses: lightest = {np.sqrt(m_iso_sq[0]):.2f} M_KK")
print(f"  H (physical, M_KK units) = {H_MKK_phys:.6f} M_KK")
print(f"  m_lightest / H = {np.sqrt(m_iso_sq[0])/H_MKK_phys:.0f}")
print(f"  All isocurvature modes are >> H. No isocurvature enhancement.")

iso_enhancement = 1.0 + np.sum(H_MKK_phys**2 / m_iso_sq)
print(f"  Isocurvature factor: 1 + sum(H^2/m_i^2) = {iso_enhancement:.8f}")
print(f"  NEGLIGIBLE (H/m_lightest ~ {H_MKK_phys/np.sqrt(m_iso_sq[0]):.2e})")

# =============================================================================
#  SECTION 7: Definitive Combined Result
# =============================================================================
print("\n[SECTION 7] DEFINITIVE combined result")
print("-" * 60)

# Conservative (c_s = 1):
r_final_conservative = r_naive  # 16*eps, no suppression available
# Optimistic (c_s = 0.485 from spectral action kinetic structure):
r_final_optimistic = r_naive * c_s_optimistic

print(f"  SUPPRESSION CHANNEL AUDIT:")
print(f"    1. Starobinsky R^2:  CLOSED (m_s = {m_s_GeV/H_phys:.0f}x H, frozen)")
print(f"    2. Sound speed c_s:  OPEN only if spectral action gives DBI-like kinetics")
print(f"    3. Multi-field:      CLOSED (sin^2(alpha) = 1, trace orthogonal)")
print(f"    4. Isocurvature:     CLOSED (all 36 modes >> H)")
print(f"")
print(f"  CONSERVATIVE RESULT (c_s = 1):")
print(f"    r = 16 * epsilon_H = {r_final_conservative:.4f}")
print(f"    STATUS: FAIL (r = {r_final_conservative:.4f} > 0.1)")
print(f"")
print(f"  OPTIMISTIC RESULT (c_s = 0.485, DBI-like):")
print(f"    r = 16 * epsilon_H * c_s = {r_final_optimistic:.4f}")
print(f"    STATUS: FAIL (r = {r_final_optimistic:.4f} > 0.1)")
print(f"")
print(f"  In BOTH cases: r > 0.1. GATE FAILS.")

# =============================================================================
#  SECTION 8: What Would Be Needed
# =============================================================================
print("\n[SECTION 8] Sensitivity analysis: what would be needed")
print("-" * 60)

eps_needed = 0.036 / 16.0
print(f"  For r < 0.036 with c_s = 1:")
print(f"    Need epsilon < {eps_needed:.6f}")
print(f"    Current epsilon = {epsilon_H:.6f}")
print(f"    Reduction needed: {epsilon_H/eps_needed:.1f}x")

cs_needed = 0.036 / (16.0 * epsilon_H)
print(f"\n  For r < 0.036 at current epsilon:")
print(f"    Need c_s < {cs_needed:.4f}")
print(f"    This requires EXTREME non-canonical kinetics")

# 1-loop epsilon possibility:
print(f"\n  POTENTIAL RESOLUTION: 1-loop modified epsilon")
print(f"    Tree Hessian: all 36 eigenvalues NEGATIVE (S62)")
print(f"    1-loop Hessian: all 36 POSITIVE (sign reversal)")
print(f"    H_1loop / |H_tree| = 3.5")
print(f"    If 1-loop modifies dS/dtau and d^2S/dtau^2:")
print(f"      epsilon_1loop = (1/2)*(dS'/S')^2/(d2S'/S')")
print(f"      Could differ from tree epsilon by O(H_1loop/H_tree) ~ 3.5")
print(f"    Need: epsilon_1loop < {eps_needed:.6f} ({epsilon_H/eps_needed:.1f}x reduction)")

# Gauss-Bonnet / higher-curvature modification:
print(f"\n  OTHER ROUTES:")
print(f"    a) Gauss-Bonnet term in a_4 modifies consistency relation")
print(f"       Effect: r = 16*eps*(1 - 8*alpha_GB*H^2) (Nojiri-Odintsov 2005)")
print(f"       Needs: alpha_GB*H^2 ~ 0.5 for sufficient suppression")
print(f"    b) Non-Bunch-Davies vacuum state from supersonic transit")
print(f"       Mach = {Mach:.1f}: perturbations do not adiabatically evolve")
print(f"       Could modify the tensor spectrum P_t")
print(f"    c) Modified dispersion from KK tower")
print(f"       omega^2 = k^2 + sum_n lambda_n^2 modifies UV modes")
print(f"       Affects tensor spectrum at scales k > lambda_1")

# =============================================================================
#  SECTION 9: Structural Analysis
# =============================================================================
print("\n[SECTION 9] Structural analysis (Penrose perspective)")
print("-" * 60)

# Weyl decomposition:
C_sq_fold = 0.3859  # (local)
S_sq_fold = 0.00476  # (local)
R_sq_fold = R_fold**2

# a_4 in Weyl basis: 495*R^2 - (152/3)*|S|^2 - 28*|C|^2
c_R2_weyl = 495.0  # (local)
c_S2_weyl = -152.0 / 3.0
c_C2_weyl = -28.0  # (local)

a4_R2_weyl = c_R2_weyl * R_sq_fold
a4_S2_weyl = c_S2_weyl * S_sq_fold
a4_C2_weyl = c_C2_weyl * C_sq_fold

print(f"  a_4 in Weyl decomposition:")
print(f"    495*R^2     = {a4_R2_weyl:.2f}  ({100*a4_R2_weyl/total_integrand:.1f}%)")
print(f"    -50.7*|S|^2 = {a4_S2_weyl:.2f}  ({100*a4_S2_weyl/total_integrand:.2f}%)")
print(f"    -28*|C|^2   = {a4_C2_weyl:.2f}  ({100*a4_C2_weyl/total_integrand:.2f}%)")
print(f"  R^2 DOMINATES by factor {abs(a4_R2_weyl)/(abs(a4_S2_weyl)+abs(a4_C2_weyl)):.0f}x")

print(f"\n  WEYL CURVATURE HYPOTHESIS CONNECTION:")
print(f"    |C|^2(fold) = {C_sq_fold:.4f} (low Weyl at fold, consistent with WCH)")
print(f"    Weyl enters a_4 NEGATIVELY: more Weyl -> smaller a_4 -> heavier scalaron")
print(f"    WCH (low Weyl at start) ensures LIGHTEST possible scalaron")
print(f"    Even so, m_s = {m_s_MKK:.4f} M_KK >> H_inflation")
print(f"    STRUCTURAL: the KK scale M_KK determines m_s ~ O(M_KK),")
print(f"    while H is set by A_s ~ 10^{{-9}}. The hierarchy H << M_KK is fundamental.")

# Conformal diagram perspective:
print(f"\n  PENROSE DIAGRAM PERSPECTIVE:")
print(f"    The tensor-to-scalar ratio r is an observable at future null infinity I^+.")
print(f"    It measures the ratio of tensor to scalar perturbation amplitudes")
print(f"    as they cross the Hubble horizon and freeze.")
print(f"    The transit (tau: 0 -> 0.19) occurs in the causal past.")
print(f"    The expansion history determines how perturbations map from transit to I^+.")
print(f"    With N_e = 0.17 classical e-folds, the causal past is very narrow —")
print(f"    the transit is ALMOST a point event in the conformal diagram.")
print(f"    This is a STRUCTURAL obstacle: insufficient expansion to amplify")
print(f"    perturbations while diluting the initial epsilon.")

# =============================================================================
#  SECTION 10: Gate Verdict
# =============================================================================
print("\n" + "=" * 60)
print("  GATE VERDICT: TENSOR-SCALAR-63")
print("=" * 60)

# The definitive result:
r_definitive = r_naive  # 16*eps = 0.346, conservative (c_s = 1)
verdict = "FAIL"
detail = (f"r = 16*eps = {r_definitive:.4f} > 0.1. "
          f"All three suppression routes CLOSED: "
          f"Starobinsky (m_s/H={m_s_GeV/H_phys:.0f}x, frozen), "
          f"multi-field (sin^2(alpha)=1, volume-preserving), "
          f"isocurvature (m_min/H={np.sqrt(m_iso_sq[0])*M_KK_gravity/H_phys:.0f}x). "
          f"c_s=0.485 is modulus diagnostic, not DBI sound speed (c_s=1 canonical). "
          f"Need epsilon < 0.00225 or non-standard tensor spectrum.")

print(f"\n  r = {r_definitive:.6f}")
print(f"  Verdict: {verdict}")
print(f"  {detail}")

# Non-Gaussianity prediction (if c_s were physical):
f_NL_if_cs = 1.0 / c_s_sq  # = 4.25 (equilateral)

print(f"\n  SECONDARY PREDICTIONS:")
print(f"    If c_s = 0.485 is physical: f_NL_equil ~ {f_NL_if_cs:.1f}")
print(f"    Scalaron mass: m_s = {m_s_GeV:.3e} GeV = {m_s_GeV/M_Pl_reduced:.4f} M_Pl")
print(f"    a_4 is {100*frac_R2:.0f}% R^2 (near-Einstein at fold)")

# PHONONIC CLASSIFICATION
print(f"\n  PHONONIC CLASSIFICATION: GEOMETRIC")
print(f"  The r = 0.346 FAIL is a purely geometric statement.")
print(f"  epsilon_H = 0.0216 comes from the spectral action on SU(3).")
print(f"  No phononic/BCS mechanism enters. The FAIL is structural.")

# =============================================================================
#  SECTION 11: Save Results
# =============================================================================
print("\n[SECTION 11] Saving results")
print("-" * 60)

results = {
    'gate_name': 'TENSOR-SCALAR-63',
    'gate_verdict': verdict,
    'gate_detail': detail,

    # Single-field
    'r_naive': r_naive,
    'r_definitive': r_definitive,
    'epsilon_H': epsilon_H,

    # Sound speed
    'c_s_modulus': c_s,
    'c_s_adiabatic': c_s_conservative,
    'c_s_sq_modulus': c_s_sq,
    'r_if_cs_physical': r_optimistic,

    # Starobinsky
    'alpha_R2': alpha_R2_s54,
    'm_s_MKK': m_s_MKK,
    'm_s_GeV': m_s_GeV,
    'm_s_over_H_phys': m_s_GeV / H_phys,
    'm_s_over_H_SA': m_s_GeV / H_SA,
    'staro_channel': 'CLOSED',

    # Multi-field
    'cos_alpha_jensen_trace': cos_alpha,
    'sin2_alpha': sin2_alpha,
    'multifield_channel': 'CLOSED (volume-preserving)',

    # Isocurvature
    'iso_enhancement': iso_enhancement,
    'lightest_iso_mass_MKK': np.sqrt(m_iso_sq[0]),
    'lightest_iso_over_H': np.sqrt(m_iso_sq[0]) * M_KK_gravity / H_phys,
    'iso_channel': 'CLOSED',

    # a_4 decomposition
    'frac_R2_a4': frac_R2,
    'frac_Ric2_a4': term_Ric2 / total_integrand,
    'frac_K_a4': term_K / total_integrand,

    # Hubble
    'H_phys_GeV': H_phys,
    'H_SA_GeV': H_SA,
    'H_MKK_phys': H_MKK_phys,
    'M_Pl_SA_GeV': M_Pl_SA,

    # Sensitivity
    'eps_needed_for_pass': eps_needed,
    'cs_needed_for_pass': cs_needed,
    'shortfall_factor': r_definitive / 0.036,

    # Secondary predictions
    'f_NL_equil_if_cs': f_NL_if_cs,
    'Mach': Mach,
}

outfile = 's63_tensor_scalar.npz'
np.savez(outfile, **results)
print(f"  Saved: {outfile}")

# =============================================================================
#  SECTION 12: Plots
# =============================================================================
print("\n[SECTION 12] Generating plots")
print("-" * 60)

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3)

# Plot 1: Suppression channels
ax1 = fig.add_subplot(gs[0, 0])
channels = ['Naive\n16*eps', 'Staro\nR^2', 'Multi-\nfield', 'Iso-\ncurv.', 'All\n(c_s=1)']
r_vals = [r_naive, r_naive, r_naive, r_naive, r_definitive]
suppression_notes = ['None', 'CLOSED\nm_s>>H', 'CLOSED\nvol-pres', 'CLOSED\nm>>H', 'r=16*eps']
colors_bar = ['#d32f2f', '#d32f2f', '#d32f2f', '#d32f2f', '#d32f2f']

bars = ax1.bar(channels, r_vals, color=colors_bar, edgecolor='black', alpha=0.7)
ax1.axhline(y=0.036, color='blue', linestyle='--', linewidth=2, label='BICEP/Keck r<0.036')
ax1.axhline(y=0.1, color='darkred', linestyle='--', linewidth=1.5, label='FAIL threshold r>0.1')
ax1.set_ylabel('r (tensor-to-scalar ratio)')
ax1.set_title('Suppression Channels: ALL CLOSED')
ax1.legend(loc='upper right', fontsize=9)
for i, (v, note) in enumerate(zip(r_vals, suppression_notes)):
    ax1.text(i, v + 0.01, note, ha='center', va='bottom', fontsize=7, style='italic')

# Plot 2: a_4 decomposition
ax2 = fig.add_subplot(gs[0, 1])
labels_pie = [f'500*R^2\n({100*frac_R2:.1f}%)',
              f'-32*|Ric|^2\n({100*term_Ric2/total_integrand:.1f}%)',
              f'-28*K\n({100*term_K/total_integrand:.1f}%)']
sizes = [abs(term_R2), abs(term_Ric2), abs(term_K)]
colors_pie = ['#1976d2', '#e53935', '#43a047']
ax2.pie(sizes, labels=labels_pie, colors=colors_pie, explode=(0.05,0,0),
        autopct='', startangle=90, textprops={'fontsize': 10})
ax2.set_title(f'a_4 Gilkey Decomposition at Fold\n(Near-Einstein: {100*frac_R2:.0f}% is R^2)')

# Plot 3: Mass hierarchy
ax3 = fig.add_subplot(gs[1, 0])
masses = [H_phys, m_s_GeV, M_KK_gravity, M_Pl_SA, M_Pl_reduced]
labels_m = ['H (CMB)', r'$m_s$ (scalaron)', r'$M_{KK}$', r'$M_{Pl}$ (SA)', r'$M_{Pl}$ (PDG)']
colors_m = ['#ff9800', '#4caf50', '#2196f3', '#9c27b0', '#f44336']
y_pos = np.arange(len(masses))
ax3.barh(y_pos, np.log10(np.array(masses)), color=colors_m, edgecolor='black', alpha=0.7)
ax3.set_yticks(y_pos)
ax3.set_yticklabels(labels_m)
ax3.set_xlabel('log10(Mass / GeV)')
ax3.set_title('Mass Hierarchy: m_s >> H')
for i, (m, label) in enumerate(zip(masses, labels_m)):
    ax3.text(np.log10(m) + 0.1, i, f'{m:.1e}', va='center', fontsize=8)
ax3.axvline(x=np.log10(H_phys), color='orange', linestyle=':', alpha=0.5)

# Plot 4: r vs epsilon
ax4 = fig.add_subplot(gs[1, 1])
eps_range = np.logspace(-4, -0.5, 100)
r_vs_eps = 16.0 * eps_range
ax4.fill_between(eps_range, 0, 0.036, alpha=0.15, color='green', label='PASS')
ax4.fill_between(eps_range, 0.036, 0.1, alpha=0.15, color='orange', label='INFO')
ax4.fill_between(eps_range, 0.1, 10, alpha=0.15, color='red', label='FAIL')
ax4.loglog(eps_range, r_vs_eps, 'k-', linewidth=2, label=r'$r = 16\epsilon$')
ax4.loglog(eps_range, r_vs_eps*c_s, 'b--', linewidth=1.5, label=r'$r = 16\epsilon c_s$ (if DBI)')
ax4.plot(epsilon_H, r_definitive, 'rs', markersize=12, zorder=5,
         label=f'This work: eps={epsilon_H:.4f}')
ax4.axhline(y=0.036, color='green', linestyle=':', alpha=0.5)
ax4.axhline(y=0.1, color='red', linestyle=':', alpha=0.5)
ax4.set_xlabel(r'$\epsilon_H$')
ax4.set_ylabel(r'$r$')
ax4.set_title(r'$r$ vs $\epsilon_H$ Parameter Space')
ax4.legend(loc='upper left', fontsize=8)
ax4.set_xlim(1e-4, 0.3)
ax4.set_ylim(1e-3, 10)
ax4.grid(True, alpha=0.2, which='both')

plt.suptitle('TENSOR-SCALAR-63: r = 0.346 [FAIL]\n'
             'All three suppression routes CLOSED',
             fontsize=14, fontweight='bold', color='darkred')

plt.savefig('s63_tensor_scalar.png', dpi=150, bbox_inches='tight')
print(f"  Saved: s63_tensor_scalar.png")

elapsed = time.time() - t_start
print(f"\n  Total runtime: {elapsed:.1f}s")
print(f"\n{'='*76}")
print(f"  TENSOR-SCALAR-63 COMPLETE: r = {r_definitive:.4f} [{verdict}]")
print(f"{'='*76}")
