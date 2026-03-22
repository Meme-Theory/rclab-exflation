#!/usr/bin/env python3
"""
Session 39 W1-3: Schwinger Exponent from Scalar Curvature (SCHWING-GEOM-39)
============================================================================

GATE: SCHWING-GEOM-39
  PASS: |S_Schwinger(geometric) - S_inst| / S_inst < 0.02
  FAIL: discrepancy > 5%

TASK:
  Express S_Schwinger = pi * Delta_0^2 / |dtau/dt| entirely in terms of
  geometric quantities from Baptista Paper 15 (scalar curvature R(tau),
  eq 3.70) and Paper 16 (Dirac spectrum). Compare with S_inst = 0.069
  from the instanton computation.

  The Schwinger exponent measures pair creation rate in the Lorentzian
  picture. The instanton action measures tunneling rate in the Euclidean
  picture. If S_Schwinger = S_inst, the two descriptions are unified:
  the instanton gas IS the Schwinger pair creation in Euclidean time.

PHYSICAL CHAIN:
  R(tau) -> dS/dtau -> |dtau/dt| (from energy conservation)
  D_K eigenvalues -> V(B2,B2), rho(B2) -> Delta_0 (BCS gap)
  => S_Schwinger = pi * Delta_0^2 / |dtau/dt|
  => Compare with S_inst from GL instanton integral

SCALAR CURVATURE (Baptista Paper 15, eq 3.70):
  R(s) = (3/2) * [2*exp(2s) - 1 + 8*(exp(-s) - exp(-4s))]

  This is the scalar curvature of the Jensen 1-parameter family of
  left-invariant metrics on SU(3), parameterized by s = tau.
  At s = 0 (bi-invariant Einstein metric): R(0) = 3/2 * (2-1+0) = 3/2 * 9 = 27/2

  Actually: R(0) = (3/2)*(2*1 - 1 + 8*(1-1)) = (3/2)*1 = 3/2.
  Wait -- need to be careful. At s=0:
    2*exp(0) - 1 + 8*(exp(0) - exp(0)) = 2 - 1 + 8*0 = 1
  So R(0) = 3/2.

  The potential for tau dynamics is V(tau) = -R(tau) (Baptista eq 3.79).
  The modulus field tau obeys: (1/2)(dtau/dt)^2 + V(tau) = E_total.

Author: gen-physicist, Session 39
Date: 2026-03-09
"""

import os
import sys
import time
import numpy as np
from scipy.integrate import trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("Session 39 W1-3: Schwinger Exponent from Scalar Curvature")
print("GATE: SCHWING-GEOM-39")
print("=" * 78)

# ======================================================================
#  STEP 0: Load input data
# ======================================================================

print("\n--- Loading input data ---")

inst_data = np.load(os.path.join(SCRIPT_DIR, 's37_instanton_action.npz'),
                    allow_pickle=True)
dyn_data = np.load(os.path.join(SCRIPT_DIR, 's36_tau_dynamics.npz'),
                   allow_pickle=True)
susc_data = np.load(os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz'),
                    allow_pickle=True)

# Key stored values
S_inst_best = float(inst_data['S_inst_best'])          # 0.06860 (Method D, numerical)
S_inst_D = float(inst_data['S_inst_D'])                # same
Delta_0_peak = float(inst_data['Delta_0_peak'])        # 0.7704
Delta_0_num = float(inst_data['Delta_0_num'])          # 0.3646 (alpha-parameterized)
tau_fold = float(inst_data['tau_fold'])                 # 0.19016
E_cond_use = float(inst_data['E_cond_use'])            # -0.1557
E_cond_full = float(inst_data['E_cond_full'])          # -0.1369
rho_B2_per_mode = float(inst_data['rho_B2_per_mode'])  # 14.023
B2_bw = float(inst_data['B2_bw'])                      # 0.0579
E_fold = float(inst_data['E_fold'])                    # 0.8452

# GL coefficients from Method A (E_cond + Delta_0)
a_GL = float(inst_data['a_A'])                         # -0.5245
b_GL = float(inst_data['b_A'])                         #  0.4419

# BCS free energy landscape (B2 sector)
delta_scan = inst_data['delta_scan']                   # shape (10001,)
F_BCS_B2 = inst_data['F_BCS_B2']                      # shape (10001,)

# Transit velocity from S36
v_terminal_full = float(dyn_data['an_S_full_v_terminal'])       # -26.545
v_terminal_singlet = float(dyn_data['an_S_singlet_v_terminal']) # -0.1199

# Trajectory velocity at fold
v_fold_full = float(dyn_data['traj_S_full_tau00p40_v_fold'])    # -29.06
v_fold_singlet = float(dyn_data['traj_S_singlet_tau00p40_v_fold'])  # -0.133

# Pairing matrix
V_8x8 = susc_data['V_8x8']
E_8 = susc_data['E_8']
rho_8 = susc_data['rho']

# V(B2,B2) -- the Kosmann coupling within the B2 sector
V_B2 = V_8x8[np.ix_([0,1,2,3], [0,1,2,3])]
V_B2_diag = np.diag(V_B2)
V_B2_mean = np.mean(V_B2)

print(f"\n  Input data summary:")
print(f"    S_inst (best, Method D)     = {S_inst_best:.6f}")
print(f"    Delta_0 (peak, BCS gap)     = {Delta_0_peak:.6f}")
print(f"    Delta_0 (numerical, alpha)  = {Delta_0_num:.6f}")
print(f"    tau_fold                    = {tau_fold:.5f}")
print(f"    E_fold                      = {E_fold:.6f}")
print(f"    E_cond (GL)                 = {E_cond_use:.6f}")
print(f"    rho_B2 per mode             = {rho_B2_per_mode:.4f}")
print(f"    v_terminal (full S)         = {v_terminal_full:.4f}")
print(f"    v_terminal (singlet S)      = {v_terminal_singlet:.6f}")
print(f"    v_fold (trajectory, full)   = {v_fold_full:.4f}")
print(f"    V_B2 diagonal               = {V_B2_diag}")
print(f"    V_B2 mean                   = {V_B2_mean:.6f}")
print(f"    GL a                        = {a_GL:.6f}")
print(f"    GL b                        = {b_GL:.6f}")


# ======================================================================
#  STEP 1: Scalar curvature R(tau) from Baptista Paper 15, eq 3.70
# ======================================================================

print("\n" + "=" * 78)
print("STEP 1: Scalar Curvature R(tau) from Paper 15 eq 3.70")
print("=" * 78)

print("""
  Baptista Paper 15, eq 3.70 gives the scalar curvature of the Jensen
  1-parameter family of left-invariant metrics on SU(3):

    R(s) = (3/2) * [2*exp(2s) - 1 + 8*(exp(-s) - exp(-4s))]

  This is a TT-deformation (volume-preserving, transverse-traceless)
  of the bi-invariant Einstein metric. The parameter s = tau is the
  Jensen deformation parameter.

  Key properties:
    R(0) = (3/2) * [2 - 1 + 8*(1 - 1)] = 3/2
    R'(s) = 6*(exp(s) - exp(-2s))^2 >= 0  (monotone increasing)
    R'(0) = 0  (saddle point at Einstein metric)

  The potential for modulus dynamics: V(tau) proportional to -R(tau).
""")

def R_scalar(tau):
    """Scalar curvature of Jensen metrics on SU(3), Paper 15 eq 3.70."""
    return 1.5 * (2.0 * np.exp(2.0 * tau) - 1.0
                  + 8.0 * (np.exp(-tau) - np.exp(-4.0 * tau)))

def R_prime(tau):
    """First derivative R'(s) = 6*(exp(s) - exp(-2s))^2."""
    return 6.0 * (np.exp(tau) - np.exp(-2.0 * tau))**2

def R_double_prime(tau):
    """Second derivative of R(tau).
    R''(s) = 6*(exp(s) - exp(-2s))*(exp(s) + 2*exp(-2s))
    """
    return 6.0 * (np.exp(tau) - np.exp(-2.0*tau)) * (np.exp(tau) + 2.0*np.exp(-2.0*tau))

# Evaluate at key points
R_0 = R_scalar(0.0)
R_fold = R_scalar(tau_fold)
R_prime_fold = R_prime(tau_fold)
R_pp_fold = R_double_prime(tau_fold)

print(f"  R(0)          = {R_0:.10f}  (should be 3/2 = 1.5)")
print(f"  R(tau_fold)   = {R_fold:.10f}  (tau_fold = {tau_fold:.5f})")
print(f"  R'(tau_fold)  = {R_prime_fold:.10f}")
print(f"  R''(tau_fold) = {R_pp_fold:.10f}")

# Verify R(0) = 3/2 exactly
assert abs(R_0 - 1.5) < 1e-12, f"R(0) = {R_0} != 3/2"
print(f"\n  CHECK: R(0) = 3/2 exactly: PASS")

# Scan R(tau) for plotting
tau_scan = np.linspace(0, 0.5, 1001)
R_scan = R_scalar(tau_scan)
Rp_scan = R_prime(tau_scan)


# ======================================================================
#  STEP 2: Transit speed |dtau/dt| from energy conservation
# ======================================================================

print("\n" + "=" * 78)
print("STEP 2: Transit Speed |dtau/dt| at the Fold")
print("=" * 78)

print("""
  The modulus tau evolves under the spectral action gradient. From S36,
  the effective 1D dynamics obeys:

    G_mod * d2tau/dt2 = -dV/dtau

  where G_mod is the DeWitt metric (kinetic coefficient) and V(tau)
  is the effective potential from the spectral action.

  From S36 (stored data):
    v_terminal (full S, analytic) = -26.545  (spectral gradient units)
    v_fold (trajectory at tau=0.40 -> fold) = -29.06

  These are in units where the spectral action is dimensionless
  and the modular metric G_mod has a specific normalization.

  For the GEOMETRIC approach, we use V(tau) = -R(tau) (Baptista eq 3.79
  establishes that -R plays the role of the potential for TT deformations).

  Energy conservation (starting from rest at tau_start):
    (1/2) * G_mod * (dtau/dt)^2 = |V(tau_start) - V(tau_fold)|
                                 = R(tau_fold) - R(tau_start)

  However, the S36 dynamics already incorporated the FULL spectral action
  gradient (not just R(tau)). The spectral action includes all Seeley-
  DeWitt coefficients (a_0, a_2, a_4), not just the a_2 term proportional
  to R.

  APPROACH A: Use the stored v_terminal from S36 directly.
  APPROACH B: Compute from R(tau) alone (pure geometry).
  APPROACH C: Use the trajectory v_fold from S36 numerical integration.
""")

# APPROACH A: Stored terminal velocity
v_A = abs(v_terminal_full)  # 26.545
print(f"\n  Approach A: |v_terminal| from S36 (full spectral action)")
print(f"    |dtau/dt| = {v_A:.4f}")

# APPROACH B: From R(tau) alone
# V(tau) = -R(tau). Starting from tau_start ~ 0.40 (bi-invariant is at 0):
# KE at fold = R(tau_fold) - R(tau_start)
#
# But we need the modular metric G_mod. From S36:
# G_mod_standard = 5.0, G_mod_projected = 2.857
G_mod_std = float(dyn_data['G_mod_standard'])
G_mod_proj = float(dyn_data['G_mod_projected'])

tau_start = 0.40  # typical initial condition from S36 trajectories
R_start = R_scalar(tau_start)
Delta_R = R_fold - R_start

print(f"\n  Approach B: From R(tau) alone (pure geometry)")
print(f"    G_mod (standard) = {G_mod_std}")
print(f"    G_mod (projected) = {G_mod_proj}")
print(f"    tau_start = {tau_start}")
print(f"    R(tau_start) = {R_start:.6f}")
print(f"    R(tau_fold) = {R_fold:.6f}")
print(f"    Delta_R = R(fold) - R(start) = {Delta_R:.6f}")

# Energy conservation: (1/2)*G_mod*v^2 = |Delta_R|
# Note: tau is DECREASING (rolling from 0.40 toward 0), so
# V = -R => V decreasing means R increasing => tau rolls toward lower tau.
# Actually R is monotone increasing, so -R is monotone decreasing.
# Rolling from tau=0.40 toward tau=0 means going downhill in -R(tau).
# At the fold (tau=0.19), we are midway.
#
# KE = |V(tau_fold) - V(tau_start)| = |-R(fold) - (-R(start))| = |R(start) - R(fold)|

Delta_V = abs(R_start - R_fold)  # R(start) > R(fold) since R is monotone increasing
# This gives the wrong sign: R(0.40) > R(0.19), so V(0.40) < V(0.19).
# The modulus rolls from tau=0.40 TOWARD tau=0, i.e., down the potential hill.
# V = -R, R increasing => V decreasing. So V(0.40) < V(0.19).
# Rolling from 0.40 toward lower tau means... wait.

# Let me reconsider. R(s) is monotone increasing for s > 0.
# R(0.40) > R(0.19). So V = -R gives V(0.40) < V(0.19).
# If modulus starts at tau=0.40, it needs to roll downhill, i.e., toward
# MORE negative V, which means toward LARGER tau (AWAY from fold).
#
# But in the S36 trajectory, tau starts at 0.40 and rolls to ~0.
# This means the FULL spectral action gradient points toward tau=0,
# not away from it. The full spectral action is NOT just R(tau).
# The higher Seeley-DeWitt coefficients (a_4 etc.) dominate.
#
# From S36 data, the spectral action's effective potential has the fold at
# tau ~ 0.19 as an INFLECTION point, and the gradient pushes toward tau=0.
#
# CONCLUSION: We CANNOT use R(tau) alone for |dtau/dt|. The transit speed
# is set by the FULL spectral action gradient, which is stored in S36.
# R(tau) enters only as the geometric underpinning of the Dirac spectrum
# and hence of Delta_0.

print(f"\n  NOTE: R(tau) alone gives the WRONG sign for the gradient.")
print(f"  R is monotone increasing, so V=-R is monotone decreasing,")
print(f"  which would roll tau AWAY from the fold, not through it.")
print(f"  The transit speed is set by the FULL spectral action (a_0, a_2, a_4).")
print(f"  Using stored S36 value for |dtau/dt|.")

# For approach B, compute what v_B WOULD be if R alone drove the dynamics
if Delta_V > 0:
    v_B_std = np.sqrt(2.0 * Delta_V / G_mod_std)
    v_B_proj = np.sqrt(2.0 * Delta_V / G_mod_proj)
else:
    v_B_std = 0.0
    v_B_proj = 0.0
print(f"    |v_B| (G_mod=5.0, R-only) = {v_B_std:.6f}  [WRONG DIRECTION]")
print(f"    |v_B| (G_mod=2.86, R-only) = {v_B_proj:.6f}  [WRONG DIRECTION]")

# APPROACH C: Trajectory velocity at fold
v_C = abs(v_fold_full)  # 29.06
print(f"\n  Approach C: |v_fold| from S36 trajectory (tau_0=0.40)")
print(f"    |dtau/dt| = {v_C:.4f}")

# Use the S38 value that produced the original S_Schwinger = 0.070
# S38 used |dtau/dt| = 26.5 (from S36 terminal velocity)
v_S38 = 26.5
print(f"\n  Approach D: S38 reference value")
print(f"    |dtau/dt| = {v_S38}")


# ======================================================================
#  STEP 3: BCS gap Delta_0 at the fold
# ======================================================================

print("\n" + "=" * 78)
print("STEP 3: BCS Gap Delta_0 at the Fold")
print("=" * 78)

print("""
  The BCS gap Delta_0 derives from the Dirac spectrum of D_K at the fold:

    Delta_0 = V_max * rho * exp(-1/(V_max * rho))   [weak coupling]

  More precisely, from the self-consistent gap equation:
    Delta_k = sum_{k'} V_{kk'} * sqrt(rho_k*rho_{k'}) * Delta_{k'} / (2*E_{k'})

  The stored values from S37:
    Delta_0_peak = 0.7704  (peak of BCS gap curve in tau)
    Delta_0_num = 0.3646   (from GL alpha-parameterization)

  The S38 Schwinger computation used Delta_0 = 0.77 (the peak value).

  GEOMETRIC CHAIN for Delta_0:
    tau_fold -> D_K eigenvalues -> V(B2,B2) Kosmann matrix elements
    tau_fold -> B2 bandwidth -> rho_B2 (van Hove DOS)
    V(B2,B2) * rho_B2 -> M_max (Thouless eigenvalue)
    M_max -> Delta_0 via gap equation

  All inputs trace to the Jensen parameter tau and the Dirac spectrum.
""")

# Reconstruct Delta_0 from BCS gap formula
# The B2 sector Kosmann coupling (spinor frame, Session 34):
V_kosmann_spinor = 0.057  # V(B2,B2) in spinor frame
V_kosmann_frame_V = 0.287  # V in frame V (RETRACTED, wrong matrix)

# From the pair susceptibility data, V_B2 diagonal:
print(f"  V_B2 (pair susceptibility data, 8x8 matrix):")
print(f"    Diagonal: {np.diag(V_B2)}")
print(f"    Mean: {np.mean(V_B2):.6f}")
print(f"    V(B2,B2) stored: {V_kosmann_spinor} (spinor frame, S34)")

# The Delta_0 that enters the instanton action is the one from the
# GL parametrization that produced S_inst_D = 0.0686:
# From the instanton file, Method D used Delta_0_num = 0.3646
# and the free energy landscape F_BCS_B2 (B2 sector only).

# But S38 used Delta_0_peak = 0.77 for the Schwinger formula.
# These are DIFFERENT Delta_0 values because:
#   Delta_0_peak = max BCS gap (physical gap)
#   Delta_0_num = alpha_min * max(Delta_SC) = GL minimum in alpha space

# The critical question: which Delta_0 enters S_Schwinger?
# The Schwinger formula S = pi * m^2 / E uses the particle MASS (gap).
# The physical gap is Delta_0_peak = 0.77.
# The instanton action uses the GL free energy landscape, which gives
# S_inst_D = integral sqrt(2*F_BCS) dDelta from 0 to Delta_0.

# Let me check: what Delta_0 gives S_inst from the GL formula?
# S_inst = sqrt(2b) * (2/3) * Delta_0^3
# With a_GL, b_GL from Method A:
Delta_0_GL = np.sqrt(-a_GL / (2.0 * b_GL))
S_inst_GL = np.sqrt(2.0 * b_GL) * (2.0/3.0) * Delta_0_GL**3

print(f"\n  GL analysis:")
print(f"    a_GL = {a_GL:.6f}")
print(f"    b_GL = {b_GL:.6f}")
print(f"    Delta_0 (GL minimum) = sqrt(-a/(2b)) = {Delta_0_GL:.6f}")
print(f"    S_inst (GL analytic) = sqrt(2b)*(2/3)*Delta_0^3 = {S_inst_GL:.6f}")
print(f"    S_inst (numerical, Method D) = {S_inst_D:.6f}")
print(f"    Ratio GL/numerical = {S_inst_GL/S_inst_D:.6f}")

print(f"\n  BCS gap values:")
print(f"    Delta_0_peak (physical gap) = {Delta_0_peak:.6f}")
print(f"    Delta_0_num (alpha-param)   = {Delta_0_num:.6f}")
print(f"    Delta_0_GL (GL minimum)     = {Delta_0_GL:.6f}")

# The self-consistent gap at fold, solving from stored Kosmann data:
# Use rho and V from pair susceptibility
# The BCS gap for B2 modes (4 degenerate at fold):
rho_B2 = rho_B2_per_mode  # 14.023 per mode
N_B2 = 4

# Effective coupling for uniform gap:
# M_max = largest eigenvalue of V_kk' * sqrt(rho_k * rho_{k'}) / (2*|xi_k|)
# At fold, xi_k ~ E_k - mu = E_fold - 0 = 0.845
# For B2 modes (4-fold degenerate at fold):
xi_fold = E_fold  # 0.845 (mu=0)

# From the Thouless eigenvalue M_max = 1.674 (authoritative)
M_max_auth = float(inst_data['M_max_AUTH'])
print(f"\n  M_max (authoritative) = {M_max_auth}")

# BCS gap from exponential formula (weak coupling limit):
# 1 = V_eff * rho_eff * integral dxi / (2*sqrt(xi^2 + Delta^2))
# For uniform gap over bandwidth W = B2_bw:
# 1 = V_eff * rho_eff * arcsinh(W/(2*Delta)) (approximately)
# => Delta = W / (2 * sinh(1/(V_eff*rho_eff)))

# More directly: using the stored E_cond and the BCS relation
# E_cond = -N(0) * Delta^2 / 2 (for uniform gap)
# With N_total = 4 * rho_B2 = 56.09:
N_total_B2 = N_B2 * rho_B2
Delta_from_Econd = np.sqrt(2.0 * abs(E_cond_use) / N_total_B2)

print(f"    N_total(B2) = 4 * rho_B2 = {N_total_B2:.4f}")
print(f"    Delta from E_cond: sqrt(2|E_cond|/N) = {Delta_from_Econd:.6f}")

# The Delta_0_peak = 0.77 is from the GCM self-consistent calculation
# across the tau sweep. It represents the MAXIMUM gap component among
# the 4 B2 modes at the fold.


# ======================================================================
#  STEP 4: Compute S_Schwinger from geometric inputs
# ======================================================================

print("\n" + "=" * 78)
print("STEP 4: S_Schwinger = pi * Delta_0^2 / |dtau/dt|")
print("=" * 78)

print("""
  The Schwinger pair creation exponent for quasiparticles with gap Delta_0
  in a time-dependent field with sweep rate |dtau/dt|:

    S_Schwinger = pi * Delta_0^2 / |dtau/dt|

  This formula assumes the "electric field" E ~ |dtau/dt| acts uniformly
  across the BCS gap (adiabatic Schwinger limit). The relevant Delta_0
  is the physical BCS gap at the fold.

  GEOMETRIC DECOMPOSITION:
    Delta_0 -> determined by D_K eigenvalues + Kosmann couplings
    |dtau/dt| -> determined by spectral action gradient (dS/dtau)
    R(tau) -> enters through the a_2 Seeley-DeWitt coefficient
    The a_4 term dominates the spectral action, so |dtau/dt| is NOT
    simply proportional to R'(tau).
""")

# Compute S_Schwinger with different velocity choices
results = {}

# Method 1: S38 reproduction (Delta_0_peak, v_S38=26.5)
S_schw_S38 = np.pi * Delta_0_peak**2 / v_S38
results['S38_repro'] = {
    'Delta_0': Delta_0_peak, 'v': v_S38, 'S_Schwinger': S_schw_S38
}
print(f"\n  Method 1: S38 reproduction")
print(f"    Delta_0 = {Delta_0_peak:.6f}, |v| = {v_S38}")
print(f"    S_Schwinger = pi * {Delta_0_peak:.6f}^2 / {v_S38}")
print(f"    S_Schwinger = {S_schw_S38:.6f}")

# Method 2: Terminal velocity from S36 (full spectral action)
S_schw_term = np.pi * Delta_0_peak**2 / v_A
results['terminal'] = {
    'Delta_0': Delta_0_peak, 'v': v_A, 'S_Schwinger': S_schw_term
}
print(f"\n  Method 2: S36 terminal velocity (full S)")
print(f"    Delta_0 = {Delta_0_peak:.6f}, |v| = {v_A:.4f}")
print(f"    S_Schwinger = {S_schw_term:.6f}")

# Method 3: Trajectory velocity at fold
S_schw_traj = np.pi * Delta_0_peak**2 / v_C
results['trajectory'] = {
    'Delta_0': Delta_0_peak, 'v': v_C, 'S_Schwinger': S_schw_traj
}
print(f"\n  Method 3: Trajectory velocity at fold")
print(f"    Delta_0 = {Delta_0_peak:.6f}, |v| = {v_C:.4f}")
print(f"    S_Schwinger = {S_schw_traj:.6f}")

# Method 4: With Delta_0_GL (GL-consistent gap)
S_schw_GL = np.pi * Delta_0_GL**2 / v_A
results['GL_gap'] = {
    'Delta_0': Delta_0_GL, 'v': v_A, 'S_Schwinger': S_schw_GL
}
print(f"\n  Method 4: GL-consistent Delta_0")
print(f"    Delta_0 = {Delta_0_GL:.6f}, |v| = {v_A:.4f}")
print(f"    S_Schwinger = {S_schw_GL:.6f}")

# Method 5: Singlet spectral action (much slower transit)
S_schw_singlet = np.pi * Delta_0_peak**2 / abs(v_terminal_singlet)
results['singlet'] = {
    'Delta_0': Delta_0_peak, 'v': abs(v_terminal_singlet), 'S_Schwinger': S_schw_singlet
}
print(f"\n  Method 5: Singlet spectral action velocity")
print(f"    Delta_0 = {Delta_0_peak:.6f}, |v| = {abs(v_terminal_singlet):.6f}")
print(f"    S_Schwinger = {S_schw_singlet:.4f}  (VERY LARGE -- singlet too slow)")


# ======================================================================
#  STEP 5: Compare S_Schwinger with S_inst
# ======================================================================

print("\n" + "=" * 78)
print("STEP 5: Comparison S_Schwinger vs S_inst")
print("=" * 78)

S_inst_ref = S_inst_best  # 0.06860

print(f"\n  Reference: S_inst = {S_inst_ref:.6f} (Method D, B2-only numerical)")
print(f"")
print(f"  {'Method':<25s} {'S_Schwinger':>12s} {'Discrepancy':>12s} {'Ratio':>8s}")
print(f"  {'-'*25} {'-'*12} {'-'*12} {'-'*8}")

for key, val in results.items():
    disc = abs(val['S_Schwinger'] - S_inst_ref) / S_inst_ref
    ratio = val['S_Schwinger'] / S_inst_ref
    tag = "***" if disc < 0.05 else ""
    print(f"  {key:<25s} {val['S_Schwinger']:12.6f} {disc:12.4f} {ratio:8.4f}  {tag}")

# The S38 reference: S_Schwinger = 0.070, S_inst = 0.069
# Discrepancy: (0.070 - 0.069)/0.069 = 1.4%
# This PASSES the gate at 2% threshold.

# But let me recompute more carefully with precise values:
print(f"\n  Precise comparison (S38 method):")
print(f"    S_Schwinger = pi * (0.7704)^2 / 26.5 = {np.pi * 0.7704**2 / 26.5:.6f}")
print(f"    S_inst = {S_inst_ref:.6f}")
disc_S38 = abs(np.pi * 0.7704**2 / 26.5 - S_inst_ref) / S_inst_ref
print(f"    Discrepancy = {disc_S38:.4f} = {disc_S38*100:.2f}%")

# Check with exact stored values
print(f"\n  Precise comparison (terminal velocity):")
S_schw_precise = np.pi * Delta_0_peak**2 / v_A
disc_precise = abs(S_schw_precise - S_inst_ref) / S_inst_ref
print(f"    S_Schwinger = pi * {Delta_0_peak}^2 / {v_A} = {S_schw_precise:.8f}")
print(f"    S_inst = {S_inst_ref:.8f}")
print(f"    |S_Schwinger - S_inst| = {abs(S_schw_precise - S_inst_ref):.8f}")
print(f"    Discrepancy = {disc_precise:.6f} = {disc_precise*100:.4f}%")


# ======================================================================
#  STEP 6: S_inst from first principles (BCS free energy integral)
# ======================================================================

print("\n" + "=" * 78)
print("STEP 6: S_inst from First Principles")
print("=" * 78)

print("""
  The instanton action from the GL potential:

    S_inst = integral_0^{Delta_0} sqrt(2 * F_BCS(Delta)) dDelta

  where F_BCS(Delta) is the BCS free energy measured from the broken minimum
  (so F_BCS >= 0 everywhere on [0, Delta_0]).

  For the quartic GL potential F = a*Delta^2 + b*Delta^4:
    Barrier = |a|^2/(4b) = E_cond
    F(Delta) - F_min = b*(Delta^2 - Delta_0^2)^2   (Mexican hat)
    S_inst = sqrt(2b) * (2/3) * Delta_0^3

  GEOMETRIC CHAIN:
    D_K eigenvalues -> V_kk' (Kosmann matrix) -> BCS gap equation
    -> GL coefficients a, b -> F_BCS landscape -> S_inst integral.

  All inputs trace to {tau, D_K eigenvalues, Kosmann matrix elements}.
""")

# Re-derive from the stored F_BCS_B2 landscape
F_min_B2 = np.min(F_BCS_B2)
idx_min_B2 = np.argmin(F_BCS_B2)
Delta_min_B2 = delta_scan[idx_min_B2]
barrier_B2 = F_BCS_B2[0] - F_min_B2  # F(0) - F(Delta_0) = barrier

print(f"  BCS free energy landscape (B2 sector, stored):")
print(f"    Delta range: [{delta_scan[0]:.6f}, {delta_scan[-1]:.6f}]")
print(f"    F_min = {F_min_B2:.8f} at Delta = {Delta_min_B2:.6f}")
print(f"    F(0) = {F_BCS_B2[0]:.8f}")
print(f"    Barrier = F(0) - F_min = {barrier_B2:.8f}")

# Compute instanton integral from the stored landscape
# Shift so F(Delta_0) = 0:
F_shifted = F_BCS_B2[:idx_min_B2+1] - F_min_B2
delta_inst = delta_scan[:idx_min_B2+1]
integrand = np.sqrt(2.0 * np.maximum(0, F_shifted))
S_inst_recomputed = trapezoid(integrand, delta_inst)

print(f"\n  Recomputed instanton action from stored landscape:")
print(f"    S_inst = integral sqrt(2*F_BCS) dDelta = {S_inst_recomputed:.8f}")
print(f"    Stored S_inst (D) = {S_inst_D:.8f}")
print(f"    Agreement: {abs(S_inst_recomputed - S_inst_D)/S_inst_D*100:.4f}%")

# GL analytic check:
# From a_GL, b_GL:
# S_inst = sqrt(2b) * (2/3) * Delta_0^3
# where Delta_0 = sqrt(-a/(2b))
Delta_0_check = np.sqrt(-a_GL / (2.0 * b_GL))
S_inst_analytic = np.sqrt(2.0 * b_GL) * (2.0/3.0) * Delta_0_check**3
barrier_analytic = a_GL**2 / (4.0 * b_GL)

print(f"\n  GL analytic instanton action:")
print(f"    Delta_0 = sqrt(-a/(2b)) = {Delta_0_check:.6f}")
print(f"    Barrier = a^2/(4b) = {barrier_analytic:.8f}")
print(f"    S_inst = sqrt(2b)*(2/3)*Delta_0^3 = {S_inst_analytic:.8f}")
print(f"    vs numerical: {S_inst_recomputed:.8f}")
print(f"    GL/numerical ratio: {S_inst_analytic/S_inst_recomputed:.6f}")

# Express S_inst in terms of GL coefficients explicitly:
# S_inst = sqrt(2b) * (2/3) * [-a/(2b)]^{3/2}
#        = sqrt(2b) * (2/3) * (-a)^{3/2} / (2b)^{3/2}
#        = (2/3) * (-a)^{3/2} / (2b)
#        = (2/3) * |a|^{3/2} / (2b)   [since a < 0]
#        = |a|^{3/2} / (3b)

S_inst_formula = abs(a_GL)**(1.5) / (3.0 * b_GL)
print(f"\n  S_inst = |a|^(3/2) / (3b) = {S_inst_formula:.8f}")
print(f"  Cross-check: {S_inst_analytic:.8f}")
assert abs(S_inst_formula - S_inst_analytic) < 1e-10, "Formula mismatch"
print(f"  Formula VERIFIED to machine precision.")


# ======================================================================
#  STEP 7: The Geometric Identity
# ======================================================================

print("\n" + "=" * 78)
print("STEP 7: Testing S_Schwinger = S_inst as a Geometric Relation")
print("=" * 78)

print("""
  The question: can we reduce S_Schwinger = S_inst to a relation
  involving ONLY {tau, D_K eigenvalues, scalar curvature R(tau)}?

  S_Schwinger = pi * Delta_0^2 / |v|
  S_inst = |a|^{3/2} / (3b)

  Setting them equal:
    pi * Delta_0^2 / |v| = |a|^{3/2} / (3b)

  From GL: a = 2*E_cond / Delta_0^2,  b = -E_cond / Delta_0^4
  So: |a| = 2|E_cond|/Delta_0^2,  b = |E_cond|/Delta_0^4

  S_inst = (2|E_cond|/Delta_0^2)^{3/2} / (3 * |E_cond|/Delta_0^4)
         = (2^{3/2} * |E_cond|^{3/2} / Delta_0^3) / (3|E_cond|/Delta_0^4)
         = 2^{3/2} * |E_cond|^{3/2} * Delta_0^4 / (3 * Delta_0^3 * |E_cond|)
         = 2^{3/2} * |E_cond|^{1/2} * Delta_0 / 3
         = (2*sqrt(2)/3) * sqrt(|E_cond|) * Delta_0

  S_Schwinger = pi * Delta_0^2 / |v|

  Setting equal:
    pi * Delta_0^2 / |v| = (2*sqrt(2)/3) * sqrt(|E_cond|) * Delta_0
    => pi * Delta_0 / |v| = (2*sqrt(2)/3) * sqrt(|E_cond|)
    => |v| = 3*pi*Delta_0 / (2*sqrt(2) * sqrt(|E_cond|))

  With |E_cond| = N(0)*Delta_0^2/2 (BCS relation):
    |v| = 3*pi*Delta_0 / (2*sqrt(2) * sqrt(N(0)*Delta_0^2/2))
        = 3*pi*Delta_0 / (2*sqrt(2) * Delta_0 * sqrt(N(0)/2))
        = 3*pi / (2*sqrt(2) * sqrt(N(0)/2))
        = 3*pi / (2 * sqrt(N(0)))

  So the identity S_Schwinger = S_inst requires:
    |v_fold| = 3*pi / (2 * sqrt(N(0)))

  where N(0) is the total DOS at the fold (4 * rho_B2 = 56.09).
""")

# Compute the predicted velocity from the identity
N_total = N_B2 * rho_B2  # 56.09
v_predicted = 3.0 * np.pi / (2.0 * np.sqrt(N_total))
print(f"  Predicted |v| from identity = 3*pi / (2*sqrt(N(0)))")
print(f"    N(0) = {N_total:.4f}")
print(f"    |v|_predicted = {v_predicted:.6f}")
print(f"    |v|_actual (terminal) = {v_A:.6f}")
print(f"    |v|_actual (trajectory) = {v_C:.6f}")
print(f"    Ratio predicted/actual = {v_predicted/v_A:.6f}")

# The predicted velocity is ~0.63, while actual is ~26.5.
# This is a 42x discrepancy. The identity DOES NOT HOLD in the
# strong-coupling, DOS-dependent regime unless we use a different
# normalization.

# However, the S38 near-agreement (1.4%) was achieved with SPECIFIC
# numerical values. Let me check what makes it work.

print(f"\n  Checking the S38 near-agreement numerically:")

# S_Schwinger(S38) = pi * Delta_0_peak^2 / 26.5 = 0.0703
S_schw_S38_val = np.pi * Delta_0_peak**2 / 26.5
print(f"    S_Schwinger = {S_schw_S38_val:.6f}")
print(f"    S_inst = {S_inst_ref:.6f}")
print(f"    Discrepancy = {abs(S_schw_S38_val - S_inst_ref)/S_inst_ref*100:.2f}%")

# S_inst uses Delta_0_num = 0.3646 (from GL alpha parametrization)
# while S_Schwinger uses Delta_0_peak = 0.7704.
# These are DIFFERENT Delta_0 values.

# The Delta_0 in S_inst is the GL order parameter amplitude,
# while Delta_0 in S_Schwinger is the physical BCS gap.

# This suggests the near-agreement is a NUMERICAL COINCIDENCE
# arising from the specific ratio of these different Delta_0 values
# and the velocity.

# Let me quantify this precisely:
print(f"\n  CRITICAL ANALYSIS: Different Delta_0 in S_inst vs S_Schwinger")
print(f"    S_inst uses GL landscape with Delta_min = {Delta_min_B2:.6f}")
print(f"    S_Schwinger uses physical gap Delta_0 = {Delta_0_peak:.6f}")
print(f"    Ratio = {Delta_0_peak / Delta_min_B2:.4f}")

# For the GL instanton, S_inst = |a|^{3/2}/(3b).
# Let's see what S_Schwinger would be with the GL-consistent Delta_0:
S_schw_GL_v = np.pi * Delta_min_B2**2 / v_A
print(f"\n  S_Schwinger with GL-consistent Delta_0:")
print(f"    S_Schwinger(GL) = pi * {Delta_min_B2:.6f}^2 / {v_A:.4f} = {S_schw_GL_v:.6f}")
print(f"    S_inst = {S_inst_ref:.6f}")
disc_GL = abs(S_schw_GL_v - S_inst_ref) / S_inst_ref
print(f"    Discrepancy = {disc_GL*100:.2f}%")

# And with Delta_0_num (the numerical GL minimum):
S_schw_num_v = np.pi * Delta_0_num**2 / v_A
print(f"\n  S_Schwinger with Delta_0_num:")
print(f"    S_Schwinger(num) = pi * {Delta_0_num:.6f}^2 / {v_A:.4f} = {S_schw_num_v:.6f}")
disc_num = abs(S_schw_num_v - S_inst_ref) / S_inst_ref
print(f"    Discrepancy = {disc_num*100:.2f}%")


# ======================================================================
#  STEP 8: Decompose the near-agreement
# ======================================================================

print("\n" + "=" * 78)
print("STEP 8: Decomposing the Near-Agreement")
print("=" * 78)

print("""
  The S38 near-agreement S_Schwinger ~ S_inst at the 1-2% level arises
  from using Delta_0_peak (physical gap) in S_Schwinger but the GL
  landscape (which depends on the GL coefficients a, b) for S_inst.

  Let me trace all quantities to geometric inputs and check where
  the discrepancy enters.

  GEOMETRIC INPUT TABLE:
    tau_fold = 0.19016      (Jensen parameter at fold)
    R(tau_fold)             (scalar curvature from Paper 15)
    D_K eigenvalues at fold (8 positive: 4 B2 + 1 B1 + 3 B3)
    V(B2,B2) Kosmann matrix (from inner fluctuations on D_K)
    rho_B2 = 14.023         (van Hove DOS at fold)

  DERIVED QUANTITIES:
    Delta_0 = self-consistent BCS gap (from gap equation)
    E_cond = condensation energy (from gap equation)
    a, b = GL coefficients (from E_cond, Delta_0)
    |dtau/dt| = transit speed (from spectral action gradient)
""")

# Express the ratio S_Schwinger / S_inst
# S_Schwinger = pi * Delta_0_peak^2 / |v|
# S_inst = (2*sqrt(2)/3) * sqrt(|E_cond|) * Delta_0_GL
#
# Let's work with E_cond_use = -0.1557 and the stored GL parameters

S_inst_from_Econd = (2.0*np.sqrt(2.0)/3.0) * np.sqrt(abs(E_cond_use)) * Delta_0_check
print(f"  S_inst (from E_cond formula):")
print(f"    S_inst = (2*sqrt(2)/3) * sqrt(|E_cond|) * Delta_0")
print(f"    = (2*sqrt(2)/3) * sqrt({abs(E_cond_use):.6f}) * {Delta_0_check:.6f}")
print(f"    = {S_inst_from_Econd:.8f}")
print(f"    (Should match S_inst_analytic = {S_inst_analytic:.8f})")

# Now the ratio:
ratio_SvSi = S_schw_S38_val / S_inst_ref
print(f"\n  Ratio S_Schwinger/S_inst = {ratio_SvSi:.6f}")
print(f"  log(ratio) = {np.log(ratio_SvSi):.6f}")

# The ratio close to 1 means:
# pi * Delta_peak^2 / |v| ~ |a|^{3/2} / (3b)
#
# Both are O(0.07) because:
# - pi * (0.77)^2 / 26.5 = 0.0703
# - instanton integral through shallow barrier = 0.0686
#
# Let me check the dimensional/parametric structure:
# S_Schwinger = pi * Delta_peak^2 / v  (one factor of Delta from gap, one from gap/v)
# S_inst ~ b^{1/2} * Delta_GL^3 ~ (E_cond/Delta_GL^4)^{1/2} * Delta_GL^3
#        ~ sqrt(E_cond) * Delta_GL ~ sqrt(rho*Delta_GL^2/2) * Delta_GL
#        ~ Delta_GL^2 * sqrt(rho/2)

# For S_Schwinger ~ S_inst:
# pi * Delta_peak^2 / v ~ Delta_GL^2 * sqrt(rho/2)
# => v ~ pi * (Delta_peak/Delta_GL)^2 / sqrt(rho/2)

v_from_identity = np.pi * (Delta_0_peak/Delta_0_check)**2 / np.sqrt(rho_B2/2.0)
print(f"\n  If identity exact, required |v|:")
print(f"    |v| = pi * (Delta_peak/Delta_GL)^2 / sqrt(rho/2)")
print(f"    = pi * ({Delta_0_peak:.4f}/{Delta_0_check:.4f})^2 / sqrt({rho_B2:.2f}/2)")
print(f"    = {v_from_identity:.4f}")
print(f"    Actual |v| = {v_A:.4f}")
print(f"    Ratio = {v_from_identity/v_A:.4f}")

# But this uses single-mode rho, not total. With N_total = 56.09:
v_from_identity_total = np.pi * (Delta_0_peak/Delta_0_check)**2 / np.sqrt(N_total/2.0)
print(f"\n    With N_total = {N_total:.2f}:")
print(f"    |v| = {v_from_identity_total:.4f}")
print(f"    Ratio = {v_from_identity_total/v_A:.4f}")


# ======================================================================
#  STEP 9: Final Assessment and Gate Verdict
# ======================================================================

print("\n" + "=" * 78)
print("STEP 9: GATE VERDICT")
print("=" * 78)

# The gate asks: |S_Schwinger(geometric) - S_inst| / S_inst < 0.02?
# "Geometric" means expressed in terms of {R(tau), D_K eigenvalues, Kosmann}

# The S_Schwinger = pi * Delta_0^2 / |v| uses:
#   Delta_0 = physical BCS gap (from D_K eigenvalues + Kosmann)  -> GEOMETRIC
#   |v| = transit speed (from spectral action gradient) -> GEOMETRIC
#     (but involves full spectral action, not just R(tau))

# The precise numbers:
# Using S38 parameters: Delta_0 = 0.7704, |v| = 26.5
S_schwinger_best = np.pi * Delta_0_peak**2 / v_A
S_inst_final = S_inst_ref

disc_final = abs(S_schwinger_best - S_inst_final) / S_inst_final

print(f"\n  S_Schwinger (geometric) = pi * Delta_0^2 / |v|")
print(f"    Delta_0 = {Delta_0_peak:.8f}  (peak BCS gap at fold)")
print(f"    |v| = {v_A:.8f}  (terminal velocity from S36)")
print(f"    S_Schwinger = {S_schwinger_best:.8f}")
print(f"")
print(f"  S_inst = {S_inst_final:.8f}  (Method D, B2-only numerical)")
print(f"")
print(f"  |S_Schwinger - S_inst| / S_inst = {disc_final:.6f} = {disc_final*100:.4f}%")

# Also check with trajectory velocity
S_schwinger_traj = np.pi * Delta_0_peak**2 / v_C
disc_traj = abs(S_schwinger_traj - S_inst_final) / S_inst_final
print(f"\n  With trajectory velocity |v| = {v_C:.4f}:")
print(f"    S_Schwinger = {S_schwinger_traj:.8f}")
print(f"    Discrepancy = {disc_traj*100:.4f}%")

# GATE CLASSIFICATION
print(f"\n  {'='*60}")
if disc_final < 0.02:
    gate_verdict = "PASS"
    print(f"  GATE SCHWING-GEOM-39: PASS")
    print(f"  Discrepancy {disc_final*100:.2f}% < 2% threshold")
elif disc_final < 0.05:
    gate_verdict = "INTERMEDIATE"
    print(f"  GATE SCHWING-GEOM-39: INTERMEDIATE")
    print(f"  Discrepancy {disc_final*100:.2f}% between 2% and 5%")
else:
    gate_verdict = "FAIL"
    print(f"  GATE SCHWING-GEOM-39: FAIL")
    print(f"  Discrepancy {disc_final*100:.2f}% > 5%")
print(f"  {'='*60}")

# Identify which BCS parameters prevent exact equality
print(f"\n  STRUCTURAL ANALYSIS:")
print(f"  The near-agreement arises from using DIFFERENT Delta_0 values:")
print(f"    S_Schwinger uses Delta_0_peak = {Delta_0_peak:.6f} (physical gap)")
print(f"    S_inst uses the GL landscape (GL Delta_0 = {Delta_0_check:.6f})")
print(f"    Ratio: {Delta_0_peak/Delta_0_check:.4f}")
print(f"")
print(f"  Parameters preventing exact geometric reduction:")
print(f"    1. Transit speed |v| = {v_A:.4f} depends on FULL spectral action")
print(f"       (a_0 + a_2 + a_4 terms), not just R(tau).")
print(f"    2. The physical gap Delta_0_peak comes from the self-consistent")
print(f"       gap equation on the B2 sector, while the GL instanton action")
print(f"       depends on the GL coefficients a, b extracted from the free")
print(f"       energy landscape.")
print(f"    3. The identity S_Schwinger = S_inst is NOT an algebraic identity")
print(f"       in D_K eigenvalues alone. It involves the transit speed |v|,")
print(f"       which requires the FULL spectral action potential, not just the")
print(f"       Dirac spectrum at the fold.")
print(f"")
print(f"  The {disc_final*100:.1f}% near-agreement is a NUMERICAL near-coincidence")
print(f"  for the specific SU(3) Jensen deformation, NOT a theorem.")
print(f"  The parameters that break exact equality:")
print(f"    - The GL approximation (quartic truncation of F_BCS)")
print(f"    - The ratio Delta_0_peak / Delta_0_GL = {Delta_0_peak/Delta_0_check:.4f}")
print(f"    - The dependence of |v| on non-R(tau) spectral action terms")

# R(tau) role summary
print(f"\n  ROLE OF R(tau) (Paper 15 eq 3.70):")
print(f"    R(tau_fold) = {R_fold:.6f}")
print(f"    R contributes to the a_2 Seeley-DeWitt coefficient in the")
print(f"    spectral action. However, the tau dynamics are dominated by")
print(f"    the a_4 term (which involves |Riemann|^2, Ric^2). The a_2")
print(f"    contribution to the gradient is order R'(tau_fold) = {R_prime_fold:.4f},")
print(f"    while the full gradient gives |v| ~ {v_A:.1f}.")
print(f"    R(tau) alone cannot reproduce the transit speed.")


# ======================================================================
#  PLOTS
# ======================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: R(tau) and its derivative
ax = axes[0, 0]
ax.plot(tau_scan, R_scan, 'b-', linewidth=2, label=r'$R(\tau)$')
ax.axvline(tau_fold, color='r', linestyle='--', alpha=0.7, label=f'fold ({tau_fold:.3f})')
ax.axhline(R_fold, color='r', linestyle=':', alpha=0.3)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R(\tau)$')
ax.set_title('Scalar Curvature (Paper 15 eq 3.70)')
ax.legend()
ax.grid(True, alpha=0.3)

ax2 = ax.twinx()
ax2.plot(tau_scan, Rp_scan, 'g--', linewidth=1.5, alpha=0.6, label=r"$R'(\tau)$")
ax2.set_ylabel(r"$R'(\tau)$", color='g')
ax2.tick_params(axis='y', labelcolor='g')

# Plot 2: BCS free energy landscape
ax = axes[0, 1]
ax.plot(delta_scan, F_BCS_B2, 'b-', linewidth=2)
ax.axhline(0, color='k', linestyle='-', alpha=0.3)
ax.axvline(Delta_min_B2, color='r', linestyle='--', alpha=0.7,
           label=f'$\\Delta_0$ = {Delta_min_B2:.3f}')
ax.set_xlabel(r'$\Delta$')
ax.set_ylabel(r'$F_{BCS}(\Delta)$')
ax.set_title('BCS Free Energy (B2 sector)')
ax.set_xlim(0, 1.5)
ax.legend()
ax.grid(True, alpha=0.3)

# Plot 3: S_Schwinger vs S_inst comparison
ax = axes[1, 0]
methods = ['S38 repro', 'Terminal v', 'Traj v', 'GL gap', 'Singlet v']
S_vals = [S_schw_S38_val, S_schw_precise, S_schw_traj, S_schw_GL_v, min(S_schw_singlet, 2.0)]
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
x_pos = np.arange(len(methods))

bars = ax.bar(x_pos, S_vals, color=colors, alpha=0.7)
ax.axhline(S_inst_ref, color='k', linestyle='--', linewidth=2, label=f'S_inst = {S_inst_ref:.4f}')
ax.axhline(S_inst_ref * 1.02, color='gray', linestyle=':', alpha=0.5, label='2% band')
ax.axhline(S_inst_ref * 0.98, color='gray', linestyle=':', alpha=0.5)
ax.set_xticks(x_pos)
ax.set_xticklabels(methods, rotation=30, ha='right')
ax.set_ylabel(r'$S_{Schwinger}$')
ax.set_title(r'$S_{Schwinger}$ vs $S_{inst}$ (various methods)')
ax.set_ylim(0, max(0.15, S_inst_ref * 1.5))
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# Plot 4: Discrepancy analysis
ax = axes[1, 1]
v_range = np.linspace(20, 35, 200)
S_schw_v = np.pi * Delta_0_peak**2 / v_range
ax.plot(v_range, S_schw_v, 'b-', linewidth=2,
        label=r'$\pi \Delta_0^2 / |v|$')
ax.axhline(S_inst_ref, color='r', linestyle='--', linewidth=2,
           label=f'$S_{{inst}}$ = {S_inst_ref:.4f}')
ax.fill_between(v_range, S_inst_ref*0.98, S_inst_ref*1.02,
                color='green', alpha=0.2, label='2% pass band')
ax.fill_between(v_range, S_inst_ref*0.95, S_inst_ref*1.05,
                color='yellow', alpha=0.15, label='5% fail band')
ax.axvline(v_A, color='tab:orange', linestyle=':', linewidth=1.5,
           label=f'$|v_{{term}}|$ = {v_A:.1f}')
ax.axvline(v_C, color='tab:green', linestyle=':', linewidth=1.5,
           label=f'$|v_{{traj}}|$ = {v_C:.1f}')
ax.set_xlabel(r'$|d\tau/dt|$')
ax.set_ylabel(r'$S_{Schwinger}$')
ax.set_title('Schwinger Exponent vs Transit Speed')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's39_schwinger_geometric.png'), dpi=150)
print(f"\n  Plot saved: tier0-computation/s39_schwinger_geometric.png")

# Find the |v| that gives exact equality
v_exact = np.pi * Delta_0_peak**2 / S_inst_ref
print(f"\n  For EXACT equality S_Schwinger = S_inst:")
print(f"    Required |v| = pi * Delta_0^2 / S_inst = {v_exact:.4f}")
print(f"    Actual |v| (terminal) = {v_A:.4f}")
print(f"    Actual |v| (trajectory) = {v_C:.4f}")
print(f"    Required/actual ratio = {v_exact/v_A:.4f}")


# ======================================================================
#  SAVE DATA
# ======================================================================

print("\n--- Saving data ---")

output_path = os.path.join(SCRIPT_DIR, 's39_schwinger_geometric.npz')
np.savez(output_path,
    # Gate
    gate_id='SCHWING-GEOM-39',
    gate_verdict=gate_verdict,
    gate_criterion='|S_Schwinger - S_inst| / S_inst < 0.02',
    gate_discrepancy=disc_final,

    # Scalar curvature
    R_at_fold=R_fold,
    R_prime_at_fold=R_prime_fold,
    R_double_prime_at_fold=R_pp_fold,
    R_at_zero=R_0,
    tau_fold=tau_fold,

    # BCS gap
    Delta_0_peak=Delta_0_peak,
    Delta_0_GL=Delta_0_check,
    Delta_0_num=Delta_0_num,
    Delta_min_B2=Delta_min_B2,

    # Transit speed
    v_terminal_full=v_A,
    v_fold_trajectory=v_C,
    v_for_exact_equality=v_exact,

    # S_Schwinger (various)
    S_Schwinger_terminal=S_schwinger_best,
    S_Schwinger_trajectory=S_schwinger_traj,
    S_Schwinger_S38=S_schw_S38_val,
    S_Schwinger_GL_gap=S_schw_GL_v,

    # S_inst
    S_inst_best=S_inst_ref,
    S_inst_recomputed=S_inst_recomputed,
    S_inst_analytic=S_inst_analytic,

    # GL coefficients
    a_GL=a_GL,
    b_GL=b_GL,

    # Geometric data
    E_cond_use=E_cond_use,
    rho_B2_per_mode=rho_B2_per_mode,
    N_total_B2=N_total,

    # Discrepancies
    disc_terminal=disc_final,
    disc_trajectory=disc_traj,
    disc_GL_gap=disc_GL,
    disc_S38=disc_S38,

    # Scan data
    tau_scan=tau_scan,
    R_scan=R_scan,
    R_prime_scan=Rp_scan,
)

print(f"  Saved: {output_path}")

elapsed = time.time() - t0
print(f"\n  Elapsed time: {elapsed:.2f}s")
print(f"\n{'='*78}")
print(f"  FINAL: SCHWING-GEOM-39 = {gate_verdict}")
print(f"  Discrepancy = {disc_final*100:.2f}%")
print(f"  S_Schwinger = {S_schwinger_best:.6f}")
print(f"  S_inst = {S_inst_final:.6f}")
print(f"{'='*78}")
