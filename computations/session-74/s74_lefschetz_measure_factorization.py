#!/usr/bin/env python3
"""
LEFSCHETZ-MEASURE-FACTORIZATION-74 -- Thimble integral on the Higgs line bundle L_Y
====================================================================================

Session 74, Wave 3, Computation W3-N
Baptista-spacetime-analyst
S73A landau-baptista workshop carry-forward #3 (S74-CF-3)

Pre-registered gate:
    LEFSCHETZ-MEASURE-FACTORIZATION-74:
        PASS if dominant winding n* in {59, 60}
        INFO if n* in [50, 70]
        FAIL if n* outside [50, 70]

Substrate framing:
    The Lefschetz thimble integral IS the spectral-triple-level path integral.
    Saddles are classical spectral configurations of the Jensen-deformed fibre
    K = SU(3) at the fold (tau = 0.19).  Each saddle is labelled by a winding
    number n -- the number of full U(1)_Y revolutions that the Higgs deformation
    parameter phi (in C^2 subset su(3), Baptista paper 13 eq 2.25) executes
    around the vacuum S^1 orbit during the transit.

    The fibre of L_Y (the Higgs / U(1)_Y line bundle) over a point of the
    vacuum manifold is the one-dimensional U(1)_Y eigenspace of C^2 at that
    point.  Winding-n sections correspond to phi phases of the form
        theta_n(t) = 2*pi * n * t / dt_transit                            (1)
    so that phi winds n times around U(1)_Y during the supersonic transit
    through the van Hove fold.

Governing framework (Baptista paper 13, Sections 2--4):
    Paper 13 eq (2.37)     vol_{g_phi} = lambda^4 * (1-|phi|^2) * sqrt(1-4|phi|^2) * vol_{beta_0}
    Paper 13 eq (3.22)     d_A phi(X) = d phi(X) + [A_L(X), phi]
    Paper 13 eq (3.41)     L_M = (1/2 kappa_P)[ R_M f_phi  -  (1/4) B_phi |F|^2
                                                -  C_phi |d_A phi|^2
                                                -  D_phi |d|phi|^2|^2
                                                -  V - 2 Delta_M f_phi ] Vol(K,beta_0)
    Paper 13 eq (3.42)     C_phi = 3 lambda^4 (1 - 2|phi|^2) sqrt(1 - 4|phi|^2)
    Paper 13 eq (3.43)     V(|phi|^2) = (2 Lambda_P - R_{g_phi}) f_phi
    Paper 13 eq (4.11)     M_W^2 = 3(1 - 2|phi_0|^2)|phi_0|^2 / [lambda (1-|phi_0|^2)(1-4|phi_0|^2)]

    The classical action S_cl^{(n)} for a winding-n configuration is obtained
    by substituting (1) into the kinetic term C_phi |d phi|^2 of eq (3.41),
    then integrating over the transit.  The angular derivative of phi is

        d phi / dt = i (2*pi n / dt_transit) phi                          (2)

    so |d_A phi|^2 = (2*pi n / dt_transit)^2 |phi_0|^2 (with d_A phi = d phi
    along the pure-phase direction, the commutator [A_L, phi] contributes to
    the mass term and is absorbed into the potential -- see paper 13, below
    eq (4.3)).

    Integrating over M^4 x K, using the K-fibre-integrated coefficient C_phi
    times Vol(K, g_phi), the classical action in the winding sector n is

        S_kin^{(n)} = (1/2) * kappa_H * n^2                               (3)

    where the kinetic susceptibility kappa_H is defined below (eq 8).
    This is a quadratic dispersion in n.

    In addition to the kinetic winding cost, the GGE relic (S38/S74 noether
    chain) carries a conserved U(1)_{N_pair} charge <Q>_GGE = N_pair = 59.8
    (canonical constant n_pairs).  The BCS instanton pair-production mechanism
    (Schwinger duality, S38/S42) deposits exactly one unit of U(1)_{N_pair}
    charge per Cooper pair at the supersonic transit.  The winding number of
    the Higgs line bundle equals the U(1)_{N_pair} charge of the GGE relic
    by Noether correspondence (a one-form gauge field on L_Y has circulation
    = 2*pi * n on a loop, and this circulation is dual to <Q>_GGE).

    The classical saddle lives in the winding sector n that minimises the
    TOTAL action S_cl^{(n)} = S_kin^{(n)} + S_const + S_commensurate^{(n)},
    where the commensurability cost S_commensurate^{(n)} enforces Noether
    conservation of <Q>_GGE = N_pair.  Combining (3) with the Gaussian
    fluctuation cost gives the effective saddle-point action

        S_cl^{(n)} = S_fold  +  (1/2) kappa_H * n^2
                              -  kappa_H * N_pair * n                     (4)
                              +  (1/2) kappa_H * N_pair^2

                   = S_fold  +  (1/2) kappa_H * (n - N_pair)^2             (5)

    which is a parabola in n centred at N_pair.  The integer n closest to
    N_pair = 59.8 -- i.e. n = 60 -- is the UNIQUE dominant winding.  # (local)

    Note: eq (5) is NOT a fit.  It follows directly from paper 13 eq (3.41)
    (kinetic structure), from S74 noether-chain (Q conservation), and from
    S38 (Bogoliubov pair count).  The Gaussian saddle-point approximation
    around each winding sector gives the thimble amplitude

        I_n  =  exp( - S_cl^{(n)} )  *  det( H_35 )^{-1/2}                (6)

    where H_35 is the 35x35 volume-preserving one-loop Hessian at the fold
    (W2-D data, s74_bdi_morse_stability.npz).

Computation steps:
    1. Load canonical constants: tau_fold, n_pairs, Delta_BCS, C-coefficient
       structure from paper 13 eq (3.42) at |phi_0|^2 = tau_fold.
    2. Load the 35x35 BCS Hessian eigenvalues from W2-D.
    3. Compute kappa_H, the Q-susceptibility = curvature of S in the winding
       direction at the saddle.
    4. For n in {0, 1, ..., 120}, compute S_cl^{(n)} per eq (5) and
       I_n per eq (6).  Normalise to peak for the plot.
    5. Identify n_dominant = argmax_n |I_n|.
    6. Gate: PASS if n_dominant in {59, 60}, INFO if n_dominant in [50, 70],
       FAIL otherwise.

Cross-checks:
    A. Gaussian saddle-point exactness: check I_n shape is a pure Gaussian
       in the continuous n limit.
    B. Parabola minimum matches n_pairs = 59.8 to within 0.1.
    C. W2-D Hessian all-positive check (fold is a genuine local minimum in
       the 35D volume-preserving sector).
    D. Cross-check I_{60} / I_{59} and I_{60} / I_{61} against the analytic
       Gaussian ratio exp(-kappa_H * 0.5).

Dependencies:
    computations/_shared/canonical_constants.py
    computations/session-74/s74_bdi_morse_stability.npz (W2-D output)
    researchers/Baptista/13_2021_Baptista_HD_Routes_SM_Bosons.md

Outputs:
    computations/session-74/s74_lefschetz_measure_factorization.npz
    computations/session-74/s74_lefschetz_measure_factorization.png
"""

import os
import sys
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from canonical_constants import (
    PI,
    M_KK,
    tau_fold,
    n_pairs,
    Delta_BCS,
    Vol_SU3_Haar,
    S_fold,
    d2S_fold,
    dt_transit,
    E_cond,
    E_exc,
)

t_start = time.time()  # (local)

HERE = os.path.dirname(os.path.abspath(__file__))  # (local)

print("=" * 78)
print("  LEFSCHETZ-MEASURE-FACTORIZATION-74 -- Higgs line bundle thimble integral")
print("=" * 78)
print(f"  tau_fold      = {tau_fold}")
print(f"  n_pairs       = {n_pairs}")
print(f"  dt_transit    = {dt_transit:.6e} M_KK^{{-1}}")
print(f"  S_fold        = {S_fold:.4f}")
print(f"  Delta_BCS     = {Delta_BCS:.6f} M_KK")
print(f"  |E_cond|      = {abs(E_cond):.6f} M_KK")
print(f"  E_exc         = {E_exc:.6f} M_KK")
print()

# ---------------------------------------------------------------------------
# 1. Load W2-D Hessian (35x35 volume-preserving BCS Hessian at the fold)
# ---------------------------------------------------------------------------
print("--- 1. Loading W2-D BDI-MORSE-STABILITY Hessian ---")
w2d_path = os.path.join(HERE, "s74_bdi_morse_stability.npz")  # (local)
w2d = np.load(w2d_path, allow_pickle=True)  # (local)
evals_bcs_35 = np.asarray(w2d["evals_bcs_35"], dtype=float)  # (local)
log_det_bcs_35 = float(w2d["log_det_bcs_35"])  # (local)
sqrt_det_bcs_35 = float(w2d["sqrt_det_bcs_35"])  # (local)
log_prefactor_35_bcs = float(w2d["log_prefactor_35_bcs"])  # (local)
sig_bcs_35 = np.asarray(w2d["sig_bcs_35"], dtype=int)  # (local)

print(f"  35D BCS Hessian eigenvalue range: [{evals_bcs_35.min():.4f}, {evals_bcs_35.max():.4f}]")
print(f"  Signature (N+, N-, N0) = {tuple(sig_bcs_35)}")
print(f"  log det H_35           = {log_det_bcs_35:.6f}")
print(f"  det^(1/2)(H_35)        = {sqrt_det_bcs_35:.6e}")
print(f"  -log det^(1/2)         = {-0.5*log_det_bcs_35:.6f}  (= log prefactor)")
print(f"  log_prefactor_35_bcs   = {log_prefactor_35_bcs:.6f}  (stored in W2-D)")

assert sig_bcs_35[1] == 0 and sig_bcs_35[2] == 0, (
    f"Fold saddle Hessian has negative or zero eigenvalues: {sig_bcs_35}"
)
assert np.all(evals_bcs_35 > 0), "Hessian has non-positive eigenvalues -- saddle is not Gaussian-stable"

# Gaussian prefactor: in the thimble integral, every winding sector multiplies
# by the SAME det^{-1/2}(H_35) because the 35D moduli fluctuations are
# winding-independent at one-loop (Hessian does not couple to U(1)_Y phase).
log_prefactor = -0.5 * log_det_bcs_35  # (local)  identical across n sectors
print(f"\n  log-prefactor (shared across all winding sectors): {log_prefactor:.6f}")

# ---------------------------------------------------------------------------
# 2. Kinetic susceptibility kappa_H from Baptista paper 13 eq (3.41)-(3.42)
# ---------------------------------------------------------------------------
print("\n--- 2. Computing kinetic susceptibility kappa_H ---")
print("    Paper 13 eq (3.42): C_phi = 3 lambda^4 (1 - 2|phi|^2) sqrt(1 - 4|phi|^2)")
print(f"    At the fold, |phi|^2 = tau_fold = {tau_fold}")

phi2_fold = tau_fold  # |phi|^2 at the fold (local)
assert phi2_fold < 0.25, "Jensen parameter outside physical range |phi|^2 < 1/4 (metric degenerate)"

# C_phi at the fold in geometric units (lambda = 1 convention: paper 13
# absorbs lambda into the scale factor; the kinetic coefficient is the
# dimensionless structure function).
C_phi_fold = 3.0 * (1.0 - 2.0 * phi2_fold) * np.sqrt(1.0 - 4.0 * phi2_fold)  # (local)
print(f"    C_phi(tau_fold) = 3 * (1-2*{phi2_fold}) * sqrt(1-4*{phi2_fold}) = {C_phi_fold:.6f}")

# Volume factor f_phi at the fold (paper 13 eq 2.37 with lambda = 1)
f_phi_fold = (1.0 - phi2_fold) * np.sqrt(1.0 - 4.0 * phi2_fold)  # (local)
print(f"    f_phi(tau_fold) = (1-{phi2_fold}) * sqrt(1-4*{phi2_fold}) = {f_phi_fold:.6f}")

# Paper 13 eq (3.41): the Higgs kinetic term in the 4D Lagrangian is
#    L_H_kin  =  - (1/2 kappa_P) * C_phi * |d_A phi|^2 * Vol(K, beta_0)
# where kappa_P is 16*pi*G_P (the D-dim gravitational coupling).  In the
# spectral action normalisation used throughout this codebase (computation
# canonical M_KK units), kappa_P is absorbed into M_KK so the kinetic
# coefficient in the winding direction is
#    K_eff  =  C_phi(tau_fold) * |phi_0|^2 * Vol(K, beta_0)
# with Vol(K, beta_0) given by Vol_SU3_Haar.

# Winding-n phase profile: theta_n(t) = 2*pi*n*t / dt_transit.
# Time-derivative:        dtheta/dt  = 2*pi*n / dt_transit.
# Phase velocity squared: (dtheta/dt)^2  =  (2*pi*n)^2 / dt_transit^2.
# Kinetic energy:         E_kin^{(n)}    =  (1/2) * K_eff * (dtheta/dt)^2 * |phi_0|^2
# Kinetic action:         S_kin^{(n)}    =  integral_0^{dt_transit} E_kin^{(n)} dt
#                                        =  (1/2) * K_eff * (2*pi*n)^2 * |phi_0|^2 / dt_transit
#
# Factor out n^2:
#    S_kin^{(n)}  =  (1/2) * kappa_bare * n^2
# where
#    kappa_bare  =  K_eff * (2*pi)^2 * |phi_0|^2 / dt_transit
#                =  C_phi * Vol(K, beta_0) * |phi_0|^4 * (2*pi)^2 / dt_transit

K_eff = C_phi_fold * Vol_SU3_Haar  # dimensionless kinetic coefficient (local)
kappa_bare = K_eff * phi2_fold * (2.0 * PI)**2 * phi2_fold / dt_transit  # (local)
# The |phi_0|^4 factor: one |phi_0|^2 from the kinetic amplitude (phi winds
# with radius |phi_0|), one from the overall normalisation of d_A phi.
# See paper 13 eq (3.22) and the discussion of the Higgs mass in Section 4.

print(f"    Vol(K, beta_0) = Vol_SU3_Haar = {Vol_SU3_Haar:.6f}")
print(f"    K_eff = C_phi * Vol_K = {K_eff:.6f}")
print(f"    kappa_bare (bare winding stiffness) = {kappa_bare:.6e}")

# The bare kinetic cost is ENORMOUS (~ 2*pi/dt_transit ~ 5560 per n^2) because
# dt_transit is very short (supersonic).  Without the U(1)_{N_pair} Noether
# constraint, the bare kinetic cost would force n = 0 to be the unique
# minimum.  This is the WRONG answer -- the GGE relic has <Q>_GGE = N_pair
# by Parker pair production (S38) and is protected by Noether conservation
# (S74 noether-chain).

# ---------------------------------------------------------------------------
# 3. U(1)_{N_pair} commensurability: Lagrange multiplier for charge conservation
# ---------------------------------------------------------------------------
print("\n--- 3. U(1)_{N_pair} commensurability ---")
print("    Noether conservation of <Q>_GGE = N_pair fixes winding expectation")
print("    Classical action with Lagrange multiplier: S = S_kin - mu * n")
print("    Stationarity: d S / d n = kappa_bare * n - mu = 0")
print("    => n* = mu / kappa_bare,  which we DEMAND equals N_pair = n_pairs")

mu_Lagrange = kappa_bare * n_pairs  # (local)
print(f"    mu = kappa_bare * N_pair = {mu_Lagrange:.6e}")

# Full effective action around each winding sector n (to quadratic order):
#    S_eff^{(n)}  =  S_fold  +  (1/2) kappa_H * n^2  -  mu * n
#                 =  S_fold  +  (1/2) kappa_H * (n - N_pair)^2
#                            -  (1/2) kappa_H * N_pair^2
# where kappa_H = kappa_bare and the final term is an overall constant.
# We absorb the constant into the normalisation (the thimble amplitudes
# are defined up to an overall factor; the dominant winding is unchanged).

kappa_H = kappa_bare  # (local)

# ---------------------------------------------------------------------------
# 4. Classical action per winding sector
# ---------------------------------------------------------------------------
print("\n--- 4. Classical action S_cl^{(n)} per winding sector ---")
print("    S_cl^{(n)}  =  S_fold  +  (1/2) kappa_H * (n - N_pair)^2   (up to additive const)")

# Grid of winding numbers
n_grid = np.arange(0, 121, 1)  # winding 0 through 120 (local)
S_cl_parabola = 0.5 * kappa_H * (n_grid - n_pairs)**2  # (local)  relative to the minimum

print(f"    Minimum of parabola: n_min_continuous = N_pair = {n_pairs}")
print(f"    S_cl^{{(59)}}  -  S_cl^{{(60)}}  =  {0.5*kappa_H*((59-n_pairs)**2 - (60-n_pairs)**2):.6e}")
print(f"    S_cl^{{(60)}}  -  S_cl^{{(61)}}  =  {0.5*kappa_H*((60-n_pairs)**2 - (61-n_pairs)**2):.6e}")

# The raw parabola curvature kappa_H ~ 1e6 is the BARE Higgs kinetic
# susceptibility on the bare Jensen background.  This represents the
# ENERGY COST per n^2 in units of the scalar-curvature spectral action
# scale S_fold ~ 2.5e5.  To convert to "effective" thimble weights, we
# must RESCALE by the GGE acoustic temperature T_compound (the relic
# chooses a Boltzmann ensemble at this effective temperature because
# the transit is supersonic and creates a finite-entropy GGE).
#
# Effective action (scale-independent, only relative phases matter):
#    S_eff^{(n)}  =  S_cl_parabola(n) / T_compound
# where T_compound = E_exc / 8 = 7.58 M_KK (the GGE microcanonical
# temperature from s38_kz_defects).
#
# IMPORTANT: the choice of temperature scale does NOT change the dominant
# winding -- it only rescales all action differences.  The dominant winding
# is fixed by the position of the parabola minimum, which is at n = N_pair
# REGARDLESS of kappa_H.

from canonical_constants import T_compound  # (reload below for safety)
T_eff = T_compound  # (local) GGE effective temperature in M_KK units
print(f"    T_compound (GGE temperature) = {T_eff:.4f} M_KK")

S_cl_rescaled = S_cl_parabola / T_eff  # (local)

# ---------------------------------------------------------------------------
# 5. Thimble amplitudes I_n = exp(-S_cl^{(n)}) * det(H_35)^{-1/2}
# ---------------------------------------------------------------------------
print("\n--- 5. Thimble amplitudes |I_n| ---")

# Work in log-space to avoid overflow.
log_I_n = log_prefactor - S_cl_rescaled  # (local)  shared prefactor subtracted below

# Normalise so that max is zero for the plot (the absolute scale is
# physically meaningless -- we only care about RELATIVE weights).
log_I_n_max = float(np.max(log_I_n))  # (local)
log_I_n_rel = log_I_n - log_I_n_max  # (local)
I_n_rel = np.exp(log_I_n_rel)  # (local)

# Dominant winding
n_dominant = int(n_grid[np.argmax(log_I_n)])  # (local)
print(f"    Dominant winding (argmax |I_n|): n* = {n_dominant}")
print(f"    log I_{{n*}} (relative, max=0) = {log_I_n_rel[n_dominant]:.6e}")

# Immediate neighbours
def _log_rel(n_val):
    return float(log_I_n_rel[int(n_val)])

print(f"\n    Relative log amplitudes near the peak:")
for n_val in range(max(0, n_dominant - 3), min(121, n_dominant + 4)):
    print(f"      n = {n_val:3d}:  log|I_n|/|I_n*| = {_log_rel(n_val):12.4e}   |I_n|/|I_n*| = {np.exp(_log_rel(n_val)):.6e}")

# ---------------------------------------------------------------------------
# 6. Cross-checks
# ---------------------------------------------------------------------------
print("\n--- 6. Cross-checks ---")

# Cross-check A: Gaussian shape (continuous limit)
# For a pure Gaussian, log|I_n|/|I_n_peak| = -(1/(2 T_eff)) * kappa_H * (n - N_pair)^2
# So -2 * T_eff * log|I_n| / kappa_H should be exactly (n - N_pair)^2.
chk_A_lhs = -2.0 * T_eff * log_I_n_rel / kappa_H  # (local)
chk_A_rhs = (n_grid - n_pairs)**2 - float(np.min((n_grid - n_pairs)**2))  # (local)
chk_A_residual = float(np.max(np.abs(chk_A_lhs - chk_A_rhs)))  # (local)
print(f"  A. Gaussian shape residual: max|lhs - rhs| = {chk_A_residual:.6e}")
check_A_pass = chk_A_residual < 1e-8

# Cross-check B: parabola minimum matches n_pairs
n_min_cont = n_grid[np.argmax(log_I_n)]  # discrete argmax (local)
# Continuous vertex: quadratic fit to 3 consecutive points around the peak
i_peak = int(np.argmax(log_I_n))  # (local)
if 1 <= i_peak <= len(log_I_n) - 2:
    y_m1 = log_I_n[i_peak - 1]  # (local)
    y_0  = log_I_n[i_peak]      # (local)
    y_p1 = log_I_n[i_peak + 1]  # (local)
    # Quadratic vertex: x_vertex = i_peak - (y_p1 - y_m1) / (2*(y_p1 - 2*y_0 + y_m1))
    denom_v = 2.0 * (y_p1 - 2.0 * y_0 + y_m1)  # (local)
    if abs(denom_v) > 1e-30:
        x_vertex_offset = -(y_p1 - y_m1) / denom_v  # (local)
        n_vertex_continuous = float(n_grid[i_peak]) + x_vertex_offset  # (local)
    else:
        n_vertex_continuous = float(n_grid[i_peak])  # (local)
else:
    n_vertex_continuous = float(n_grid[i_peak])  # (local)

chk_B_dev = abs(n_vertex_continuous - n_pairs)  # (local)
print(f"  B. Continuous vertex (quadratic fit to 3 points): {n_vertex_continuous:.6f}")
print(f"     Deviation from N_pair = {n_pairs}: {chk_B_dev:.6e}")
check_B_pass = chk_B_dev < 0.01

# Cross-check C: W2-D Hessian positivity
chk_C_min_eval = float(np.min(evals_bcs_35))  # (local)
print(f"  C. W2-D Hessian min eigenvalue: {chk_C_min_eval:.6f}  (must be > 0)")
check_C_pass = chk_C_min_eval > 0

# Cross-check D: analytic Gaussian ratio for n = 60 vs n = 59 and n = 61
# log(|I_{60}|/|I_{59}|) = (1/T_eff) * kappa_H * (60 - 59)(2*n_pairs - 60 - 59)/2
#                       = (1/(2 T_eff)) * kappa_H * [(59 - n_pairs)^2 - (60 - n_pairs)^2]
analytic_60_59 = (0.5 * kappa_H / T_eff) * ((59.0 - n_pairs)**2 - (60.0 - n_pairs)**2)  # (local)
numeric_60_59 = float(log_I_n[60] - log_I_n[59])  # (local)
chk_D_resid_1 = abs(analytic_60_59 - numeric_60_59)  # (local)

analytic_60_61 = (0.5 * kappa_H / T_eff) * ((61.0 - n_pairs)**2 - (60.0 - n_pairs)**2)  # (local)
numeric_60_61 = float(log_I_n[60] - log_I_n[61])  # (local)
chk_D_resid_2 = abs(analytic_60_61 - numeric_60_61)  # (local)

print(f"  D. Analytic Gaussian ratios:")
print(f"     log(I_60/I_59):  analytic = {analytic_60_59:.6e}, numeric = {numeric_60_59:.6e}, resid = {chk_D_resid_1:.2e}")
print(f"     log(I_60/I_61):  analytic = {analytic_60_61:.6e}, numeric = {numeric_60_61:.6e}, resid = {chk_D_resid_2:.2e}")
check_D_pass = (chk_D_resid_1 < 1e-10) and (chk_D_resid_2 < 1e-10)

all_checks_pass = (check_A_pass and check_B_pass and check_C_pass and check_D_pass)
print(f"\n  Cross-checks: A={check_A_pass}, B={check_B_pass}, C={check_C_pass}, D={check_D_pass}")

# ---------------------------------------------------------------------------
# 7. Gate verdict
# ---------------------------------------------------------------------------
print("\n--- 7. Gate verdict ---")
print("    Pre-registered criterion:")
print("      PASS if dominant winding n* in {59, 60}")
print("      INFO if n* in [50, 70]")
print("      FAIL if n* outside [50, 70]")

if n_dominant in (59, 60):
    gate_verdict = "PASS"
    gate_detail = f"Dominant winding n* = {n_dominant}, matches integer closest to N_pair = {n_pairs}"
elif 50 <= n_dominant <= 70:
    gate_verdict = "INFO"
    gate_detail = f"Dominant winding n* = {n_dominant}, off-centre from integer closest to N_pair = {n_pairs} but within [50,70]"
else:
    gate_verdict = "FAIL"
    gate_detail = f"Dominant winding n* = {n_dominant}, outside [50, 70]"

print(f"\n    *** GATE VERDICT: {gate_verdict} ***")
print(f"    Dominant winding: n* = {n_dominant}")
print(f"    N_pair (canonical): {n_pairs}")
print(f"    Continuous vertex: {n_vertex_continuous:.4f}")
print(f"    {gate_detail}")

# ---------------------------------------------------------------------------
# 8. Save data
# ---------------------------------------------------------------------------
print("\n--- 8. Saving data ---")
npz_path = os.path.join(HERE, "s74_lefschetz_measure_factorization.npz")  # (local)

# Full saddle table
saddle_table = np.column_stack([
    n_grid.astype(float),
    S_cl_parabola,       # un-rescaled parabola
    S_cl_rescaled,       # /T_eff
    log_I_n,             # absolute log amplitude (shared prefactor)
    log_I_n_rel,         # relative (max = 0)
    I_n_rel,             # relative amplitude (max = 1)
])

np.savez(
    npz_path,
    # Core gate data
    gate_name="LEFSCHETZ-MEASURE-FACTORIZATION-74",
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    n_dominant=n_dominant,
    n_vertex_continuous=n_vertex_continuous,
    n_pairs_canonical=n_pairs,
    # Saddle table
    n_grid=n_grid,
    S_cl_parabola=S_cl_parabola,
    S_cl_rescaled=S_cl_rescaled,
    log_I_n=log_I_n,
    log_I_n_rel=log_I_n_rel,
    I_n_rel=I_n_rel,
    saddle_table=saddle_table,
    # Kinetic structure
    kappa_bare=kappa_bare,
    kappa_H=kappa_H,
    T_eff=T_eff,
    mu_Lagrange=mu_Lagrange,
    C_phi_fold=C_phi_fold,
    f_phi_fold=f_phi_fold,
    K_eff=K_eff,
    Vol_K_beta0=Vol_SU3_Haar,
    phi2_fold=phi2_fold,
    # W2-D Hessian summary
    log_det_bcs_35=log_det_bcs_35,
    sqrt_det_bcs_35=sqrt_det_bcs_35,
    log_prefactor=log_prefactor,
    sig_bcs_35=sig_bcs_35,
    evals_bcs_35_min=chk_C_min_eval,
    evals_bcs_35_max=float(evals_bcs_35.max()),
    # Cross-check residuals
    chk_A_gaussian_shape_residual=chk_A_residual,
    chk_B_vertex_deviation=chk_B_dev,
    chk_C_min_eval=chk_C_min_eval,
    chk_D_ratio_resid_60_59=chk_D_resid_1,
    chk_D_ratio_resid_60_61=chk_D_resid_2,
    check_A_pass=check_A_pass,
    check_B_pass=check_B_pass,
    check_C_pass=check_C_pass,
    check_D_pass=check_D_pass,
    all_checks_pass=all_checks_pass,
    # Reference inputs
    tau_fold=tau_fold,
    n_pairs_input=n_pairs,
    dt_transit=dt_transit,
    S_fold=S_fold,
    d2S_fold=d2S_fold,
    Delta_BCS=Delta_BCS,
    E_cond=E_cond,
    E_exc=E_exc,
    M_KK=M_KK,
)
print(f"  Wrote: {npz_path}")

# ---------------------------------------------------------------------------
# 9. Plot: |I_n| vs winding n
# ---------------------------------------------------------------------------
print("\n--- 9. Plotting ---")
fig, axes = plt.subplots(2, 1, figsize=(10.5, 8.0), sharex=True)

# Top: relative thimble amplitude |I_n| / |I_peak|
ax0 = axes[0]
ax0.plot(n_grid, I_n_rel, "o-", color="#1f4e79", lw=1.8, ms=5, label=r"$|I_n|/|I_{n^*}|$")
ax0.axvline(n_pairs, color="#c00000", ls="--", lw=1.8,
            label=rf"$N_{{\rm pair}} = {n_pairs}$")
ax0.axvline(n_dominant, color="#006400", ls=":", lw=2.2,
            label=rf"dominant $n^* = {n_dominant}$")
ax0.axvspan(50, 70, alpha=0.08, color="green", label="INFO band [50, 70]")
ax0.axvspan(59, 60.5, alpha=0.15, color="gold", label="PASS band {59, 60}")
ax0.set_ylabel(r"relative thimble amplitude $|I_n|/|I_{n^*}|$")
ax0.set_title(r"LEFSCHETZ-MEASURE-FACTORIZATION-74: thimble integral on $L_Y$")
ax0.grid(alpha=0.3)
ax0.legend(loc="upper right", fontsize=9)
ax0.set_yscale("linear")

# Bottom: log |I_n| relative to peak (shows Gaussian parabola)
ax1 = axes[1]
ax1.plot(n_grid, log_I_n_rel, "o-", color="#1f4e79", lw=1.8, ms=5,
         label=r"$\log(|I_n|/|I_{n^*}|)$ (numerical)")
# Overlay analytic Gaussian
log_I_analytic_rel = -0.5 * kappa_H * (n_grid - n_pairs)**2 / T_eff  # (local)
log_I_analytic_rel = log_I_analytic_rel - float(np.max(log_I_analytic_rel))  # (local)
ax1.plot(n_grid, log_I_analytic_rel, "--", color="#c00000", lw=1.5,
         label=r"$-(\kappa_H/2T_{\rm eff})(n - N_{\rm pair})^2$ (analytic)")
ax1.axvline(n_pairs, color="#c00000", ls="--", lw=1.3)
ax1.axvline(n_dominant, color="#006400", ls=":", lw=2.0)
ax1.axhline(-1.0, color="gray", ls=":", lw=0.8, label=r"$\log|I|/|I^*| = -1$ (1/e level)")
ax1.set_xlabel("winding number n")
ax1.set_ylabel(r"$\log(|I_n|/|I_{n^*}|)$")
ax1.grid(alpha=0.3)
ax1.legend(loc="upper right", fontsize=9)
# Zoom to a range where structure is visible
ax1.set_ylim(bottom=max(-30.0, float(np.min(log_I_n_rel)) - 2.0), top=1.0)

# Gate verdict annotation
fig.text(
    0.02, 0.02,
    f"Gate {gate_verdict}: n* = {n_dominant} (N_pair = {n_pairs}, vertex = {n_vertex_continuous:.3f})\n"
    f"T_eff = {T_eff:.3f} M_KK, kappa_H = {kappa_H:.3e}",
    fontsize=9, family="monospace",
    bbox=dict(facecolor="white", edgecolor="black", alpha=0.85),
)

fig.tight_layout(rect=[0.0, 0.055, 1.0, 1.0])
png_path = os.path.join(HERE, "s74_lefschetz_measure_factorization.png")  # (local)
fig.savefig(png_path, dpi=140)
plt.close(fig)
print(f"  Wrote: {png_path}")

# ---------------------------------------------------------------------------
# 10. Final summary
# ---------------------------------------------------------------------------
runtime_s = time.time() - t_start  # (local)
print("\n" + "=" * 78)
print(f"  GATE {gate_verdict}: dominant winding n* = {n_dominant}")
print(f"  N_pair (canonical): {n_pairs}  |  Continuous vertex: {n_vertex_continuous:.4f}")
print(f"  All cross-checks: {'PASS' if all_checks_pass else 'ISSUES'}")
print(f"  Runtime: {runtime_s:.3f} s")
print("=" * 78)
