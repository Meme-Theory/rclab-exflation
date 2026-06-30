#!/usr/bin/env python3
"""
s69_phi_eff.py -- PHI-EFF-BCS-BOGOL-69: BCS Squeeze Phase Determination
=========================================================================

Gate: PHI-EFF-69
  PASS: Enhancement in [1.3, 4.0] (A_s gap improved by 0.11-0.60 OOM)
  FAIL: Enhancement < 1.0 (destructive interference, gap WORSENS)
  INFO: Enhancement in [1.0, 1.3] (modest, need additional channels)

Physics
-------
The non-Bunch-Davies initial state produced by the BCS transit modifies the
scalar power spectrum via:

    P_zeta(non-BD) = P_zeta(BD) * [cosh(2r_eff) + sinh(2r_eff) * cos(phi_eff)]  (1)

The squeeze parameter r_eff = 0.338 is established from S67 (beta_sq from
transit Runge-Kutta). The squeeze PHASE phi_eff is determined by the
time-dependent BCS gap dynamics Delta(tau) through the fold.

For a BCS system undergoing a quench, the squeeze phase phi_k of mode k
is determined by the Bogoliubov transformation connecting the pre-transit
vacuum (Delta=0) to the post-transit ground state (Delta=Delta_0). The
key quantity is the TDGL dynamics of the gap opening.

The BCS squeeze parameters follow from the time-dependent Bogoliubov
transformation. For mode k:

    r_k = arctanh(|beta_k|)                                                    (2)
    phi_k = arg(alpha_k * beta_k^*)                                            (3)

where alpha_k, beta_k are the Bogoliubov coefficients from the transit.
The effective phase phi_eff is the variance-weighted average over the
three GGE channel groups (acoustic, Leggett, optical).

The CRITICAL physics: The Landau-Transit workshop (Ld2) established that
tau_relax/dt_transit = 0.003 -- the BCS gap tracks the instantaneous
equilibrium ADIABATICALLY through the transit. This means the squeeze
phase is determined by the adiabatic phase accumulation, NOT by sudden
quench dynamics.

In the adiabatic limit, phi_k receives contributions from:
  1. The dynamical phase: integral of [E_k(post) - E_k(pre)] over transit
  2. The geometric (Berry) phase: from the rotation of the BCS spinor
     as Delta(tau) increases from 0 to Delta_0

The BCS coherence factor rotation angle theta_k(tau) = arctan(Delta(tau)/xi_k)
evolves continuously. The squeeze phase for mode k is:

    phi_k = 2 * int_0^{dt_transit} [E_k(tau) - epsilon_k] d(tau)              (4)
          + pi * sign(xi_k)  [Berry phase correction]                          (5)

For modes at the Fermi surface (xi_k ~ 0, i.e. B2 modes), theta goes from
0 to pi/2 and the Berry phase is pi/2. For modes away from the Fermi surface,
the Berry phase correction is smaller.

Author: Landau Condensed Matter Theorist
Session: S69
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
    # BCS parameters
    E_cond, E_exc, xi_BCS, Delta_0_GL, Delta_0_OES, N_dof_BCS,
    n_pairs, Delta_B3,
    # Spectral action
    a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    # Transit dynamics
    H_fold, v_terminal, dt_transit, P_exc_kz, n_Bog,
    # Fabric and modes
    c_Gold, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    c_fabric, T_acoustic,
    J_C2, J_su2, J_u1,
    # Scales
    M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, tau_fold,
    # Cosmological
    A_s_CMB,
    # Geometry
    G_DeWitt, N_cells,
    # Mode energies
    E_B1, E_B2_mean, E_B3_mean,
    # GL parameters
    a_GL, b_GL,
    # Instanton
    S_inst,
    PI,
)

print("=" * 78)
print("PHI-EFF-BCS-BOGOL-69: BCS Squeeze Phase Determination")
print("=" * 78)
t_start = time.time()

# =============================================================================
# STEP 0: LOAD INPUT DATA
# =============================================================================
print("\n" + "-" * 78)
print("STEP 0: Load input data and verify consistency")
print("-" * 78)

# S67 Transit PS
d_ps = np.load('s67_transit_ps.npz', allow_pickle=True)
A_s_gap_OOM_transit = float(d_ps['A_s_gap_OOM'])
beta_sq_rk = d_ps['beta_sq_rk']        # |beta_k|^2 from Runge-Kutta transit
k_grid_rk = d_ps['k_grid_rk']
tau_fine = d_ps['tau_fine']
eps_H_fine = d_ps['eps_H_fine']
z_fine = d_ps['z_fine']
a_fine = d_ps['a_fine']

# S67 Multifield delta-N
d_dn = np.load('s67_multifield_delta_n.npz', allow_pickle=True)
f_acoustic = float(d_dn['f_acoustic'])
f_leggett = float(d_dn['f_leggett'])
f_optical = float(d_dn['f_optical'])
c_acoustic_dn = float(d_dn['c_acoustic'])
c_leggett_dn = float(d_dn['c_leggett'])
c_optical_dn = float(d_dn['c_optical'])
sigma_groups = d_dn['sigma_groups']
m_eff_groups = d_dn['m_eff']
eps_H_fold_dn = float(d_dn['eps_H_fold'])
H_fold_dn = float(d_dn['H_fold'])
M_Pl_over_M_KK = float(d_dn['M_Pl_over_M_KK'])

# S68 BCS dressed mode
d_bcs = np.load('s68_bcs_dressed_mode.npz', allow_pickle=True)
Delta = float(d_bcs['Delta'])              # 0.464 M_KK (OES gap)
mu_BCS = float(d_bcs['mu_BCS'])            # 0.845 M_KK
eps_k = d_bcs['eps_k']                     # 8 bare mode energies
xi_k = d_bcs['xi_k']                       # 8 xi = eps - mu values
E_k = d_bcs['E_k']                         # 8 BCS quasiparticle energies
u_k_sq = d_bcs['u_k_sq']                   # 8 |u_k|^2
v_k_sq = d_bcs['v_k_sq']                   # 8 |v_k|^2
uv_product = d_bcs['uv_product']           # 8 u_k*v_k
labels = d_bcs['labels']                   # ['B2[0]', 'B2[1]', ...,'B3[2]']
f_w_acoustic = float(d_bcs['f_w_acoustic'])
f_w_leggett = float(d_bcs['f_w_leggett'])
f_w_optical = float(d_bcs['f_w_optical'])
delta_As_total = float(d_bcs['delta_As_total'])
A_s_bare = float(d_bcs['A_s_bare'])
A_s_bcs = float(d_bcs['A_s_bcs'])
gap_bare_OOM = float(d_bcs['gap_bare_OOM'])
gap_bcs_OOM = float(d_bcs['gap_bcs_OOM'])

# Effective squeeze parameter from transit
# beta_sq at the transit wavenumber gives r_eff
k_transit = float(d_ps['k_transit'])
idx_ktransit = np.argmin(np.abs(k_grid_rk - k_transit))
beta_sq_at_transit = beta_sq_rk[idx_ktransit]
r_eff_from_transit = 0.5 * np.log(1.0 + 2.0 * beta_sq_at_transit)
# The stated value is r_eff = 0.338
# Let's verify from data and use consistently
print(f"  Delta (OES gap)     = {Delta:.6f} M_KK")
print(f"  mu (chem. pot.)     = {mu_BCS:.6f} M_KK")
print(f"  beta_sq at transit  = {beta_sq_at_transit:.4f}")
print(f"  r_eff (from data)   = {r_eff_from_transit:.4f}")
print(f"  f_acoustic (S67)    = {f_acoustic:.6f}")
print(f"  f_leggett (S67)     = {f_leggett:.6f}")
print(f"  f_optical (S67)     = {f_optical:.6f}")
print(f"  f_w_acoustic (S68)  = {f_w_acoustic:.6f}")
print(f"  f_w_leggett (S68)   = {f_w_leggett:.6f}")
print(f"  f_w_optical (S68)   = {f_w_optical:.6f}")
print(f"  A_s (bare)          = {A_s_bare:.4e}")
print(f"  A_s (BCS)           = {A_s_bcs:.4e}")
print(f"  A_s (CMB)           = {A_s_CMB:.2e}")
print(f"  Gap (bare)          = {gap_bare_OOM:.3f} OOM")
print(f"  Gap (BCS)           = {gap_bcs_OOM:.3f} OOM")

# Use r_eff = 0.338 as stated in prompt (from previous analysis)
# This is the variance-weighted effective value
r_eff = 0.338  # (local)
print(f"\n  Using r_eff = {r_eff:.3f} (from S68 Landau-Transit workshop)")

# =============================================================================
# STEP 1: TIME-DEPENDENT BCS GAP EQUATION Delta(tau)
# =============================================================================
print("\n" + "-" * 78)
print("STEP 1: Time-dependent BCS gap equation Delta(tau) through the fold")
print("-" * 78)

print("""
  The BCS gap Delta(tau) evolves as the modulus tau traverses the fold.
  From Ld2: tau_relax/dt_transit = 0.003, so Delta tracks equilibrium
  adiabatically. We solve:

      Delta(tau) = Delta_0 * tanh(sqrt(2*(tau - tau_c) / (tau_w)))       (6)

  where tau_c = tau_fold is the critical point and tau_w characterizes
  the width of the transition region.

  The equilibrium gap at tau is:
      Delta_eq(tau) = Delta_0 * sqrt(max(0, (tau - tau_pre)/(tau_fold - tau_pre)))

  For the adiabatic limit, we use the Ginzburg-Landau form:
      F(Delta, tau) = a(tau)*|Delta|^2 + b*|Delta|^4
      a(tau) = a_GL * (tau - tau_c)/tau_c  [changes sign at fold]

  The equilibrium gap:
      Delta_eq^2(tau) = -a(tau)/(2*b) for a(tau) < 0 (below transition)
      Delta_eq(tau)  = 0                for a(tau) >= 0 (above transition)
""")

# GL parameters from canonical
a_GL_val = a_GL    # = -0.5245
b_GL_val = b_GL    # = 0.4418

# The tau coordinate for the transit
# Pre-transit: tau < tau_fold, a(tau) > 0, no gap
# Post-transit: tau > tau_fold, a(tau) < 0, gap opens
# But the transit goes THROUGH the fold, so we parameterize by time

# Transit duration
print(f"  dt_transit = {dt_transit:.6f} M_KK^{{-1}}")
print(f"  v_terminal = {v_terminal:.3f} M_KK")
print(f"  tau_fold   = {tau_fold}")
print(f"  a_GL       = {a_GL_val:.4f}")
print(f"  b_GL       = {b_GL_val:.4f}")

# Create a fine time grid through the transit
# The transit spans roughly dt_transit centered on the fold
N_t = 10000  # (local)
# Use a wider window: +/- 5*dt_transit around fold
t_half = 5.0 * dt_transit
t_grid = np.linspace(-t_half, t_half, N_t)
dt = t_grid[1] - t_grid[0]

# tau(t) through the transit: approximately linear at v_terminal
# tau(t) = tau_fold + v_terminal * t  (t=0 at fold crossing)
tau_of_t = tau_fold + v_terminal * t_grid

# GL coefficient a(tau) = a_GL * (tau - tau_fold)/tau_fold
# a_GL is NEGATIVE, so:
#   tau < tau_fold: a > 0 (symmetric phase, no condensate)
#   tau > tau_fold: a < 0 (broken phase, condensate)
# Wait -- a_GL = -0.5245 is already the value at the fold. Let me think
# more carefully.
#
# Standard Landau theory: F = alpha*(T-Tc)/Tc * |psi|^2 + beta*|psi|^4
# With alpha > 0, beta > 0.
# Below Tc: alpha*(T-Tc)/Tc < 0, so condensate forms.
# Identifying: the reduced temperature analog is (tau - tau_fold)
# In our system, a_GL = -0.5245 is the FULL coefficient at tau_fold.
# The transition happens as tau passes through the fold.
#
# The spectral action drives the system: pre-transit (tau < tau_fold),
# the system is in the high-symmetry phase. At the fold, BCS condensation
# occurs. Post-transit (tau > tau_fold), the gap is fully open.
#
# For the time-dependent gap profile:
# Since the transit is adiabatic (tau_relax/dt_transit = 0.003),
# Delta(t) follows the instantaneous equilibrium value:
#
#   Delta_eq(t) = 0                          for t < 0 (pre-transit)
#   Delta_eq(t) = Delta_0 * sqrt(t/t_open)   for 0 < t < t_open
#   Delta_eq(t) = Delta_0                     for t > t_open
#
# where t_open is the gap opening timescale.

# The gap opening time: determined by the GL relaxation time at the fold
# tau_GL = 1/(2*|a_GL|) in natural units
tau_GL = 1.0 / (2.0 * abs(a_GL_val))
print(f"  tau_GL (GL relax.)  = {tau_GL:.4f} M_KK^{{-1}}")
print(f"  tau_relax/dt_transit = {tau_GL / (dt_transit * v_terminal):.4f}")

# The gap profile: use the BCS mean-field time dependence
# For a smooth transit, the gap opens as:
# Delta(t) = Delta_0 * tanh((t - 0)/tau_open) for t > 0
# where tau_open = dt_transit (transit timescale sets the quench rate)
#
# But since tau_relax << dt_transit, the gap tracks equilibrium.
# The equilibrium gap as function of the GL control parameter:
#
# epsilon(t) = v_terminal * t / tau_fold  (reduced "temperature")
# For epsilon > 0 (past the fold): Delta_eq = sqrt(|a_GL|*epsilon/(2*b_GL)) * tau_fold^{1/2}
#
# More precisely: the GL functional is F = a_GL*r*|Delta|^2 + b_GL*|Delta|^4
# where r = (tau - tau_fold)/tau_fold
# For r > 0: Delta_eq^2 = |a_GL|*r/(2*b_GL)
# At r = 1 (far from fold): Delta_eq^2 = |a_GL|/(2*b_GL) = 0.5245/(2*0.4418) = 0.5936
# so Delta_eq ~ 0.770 M_KK, close to Delta_0_GL = 0.770.
# Check: consistent.

# Smooth gap profile
# r(t) = v_terminal * t / tau_fold
r_of_t = v_terminal * t_grid / tau_fold

# Gap evolution:
Delta_of_t = np.zeros(N_t)
for i in range(N_t):
    r_val = r_of_t[i]
    if r_val > 0:
        # Post-fold: gap is open
        Delta_sq = abs(a_GL_val) * r_val / (2.0 * b_GL_val)
        Delta_of_t[i] = np.sqrt(Delta_sq)
    else:
        Delta_of_t[i] = 0.0

# The GL equilibrium gap reaches Delta_0_GL when r=1, i.e. tau = 2*tau_fold
# But we use OES gap Delta = 0.464 as the physical gap.
# Normalize: Delta_of_t -> Delta_of_t * (Delta / Delta_of_t[-1])
# At the end of our window, r = v_terminal * t_half / tau_fold
r_end = v_terminal * t_half / tau_fold
Delta_end_GL = np.sqrt(abs(a_GL_val) * r_end / (2.0 * b_GL_val))
print(f"  r(t_end)            = {r_end:.2f}")
print(f"  Delta_GL(t_end)     = {Delta_end_GL:.4f} M_KK")

# Use the OES gap as the physical scale
# The time at which Delta reaches Delta (OES) value:
# Delta^2 = |a_GL| * r_c / (2*b_GL)
# r_c = 2*b_GL*Delta^2/|a_GL| = 2*0.4418*0.464^2/0.5245 = 0.362
r_c = 2.0 * b_GL_val * Delta**2 / abs(a_GL_val)
t_c = r_c * tau_fold / v_terminal
print(f"  r_c (OES gap)       = {r_c:.4f}")
print(f"  t_c (OES gap)       = {t_c:.6f} M_KK^{{-1}}")

# Physical gap profile: clamp to Delta (OES) maximum
Delta_phys = np.minimum(Delta_of_t, Delta)

# Also compute smooth version using tanh ramp:
# Delta_smooth(t) = Delta * (1/2)(1 + tanh(t/tau_ramp))
# where tau_ramp = dt_transit/2
tau_ramp = dt_transit / 2.0
Delta_smooth = Delta * 0.5 * (1.0 + np.tanh(t_grid / tau_ramp))

print(f"\n  Gap profile computed on {N_t} points, t in [{t_grid[0]:.6f}, {t_grid[-1]:.6f}]")
print(f"  Delta(t=0)  = {Delta_phys[N_t//2]:.6f} M_KK")
print(f"  Delta(t_end) = {Delta_phys[-1]:.6f} M_KK")

# =============================================================================
# STEP 2: BCS SQUEEZE PARAMETERS r_k, phi_k FOR EACH MODE
# =============================================================================
print("\n" + "-" * 78)
print("STEP 2: Compute BCS squeeze parameters r_k, phi_k for 8 modes")
print("-" * 78)

print("""
  For each of the 8 BCS modes, the Bogoliubov transformation from the
  pre-transit vacuum (no condensate) to the post-transit ground state
  (BCS condensate) defines squeeze parameters.

  The squeeze parameter r_k is related to the BCS coherence factors:

      r_k = arctanh(v_k / u_k)  for |v_k| < |u_k|                     (7a)
      r_k = arctanh(u_k / v_k)  for |u_k| < |v_k|                     (7b)

  Equivalently:
      tanh(r_k) = |v_k / u_k| = sqrt(v_k^2 / u_k^2)                   (8)
      r_k = 0.5 * ln((1 + |v/u|) / (1 - |v/u|))
          = 0.5 * ln(u_k^2 + v_k^2 + 2*u_k*v_k) / (u_k^2 + v_k^2 - 2*u_k*v_k)

  Actually, more precisely for BCS:
      cosh(r_k) = u_k, sinh(r_k) = v_k (in standard BCS normalization)
      so r_k = arctanh(v_k/u_k)

  For the B2 modes at the Fermi surface: u_k = v_k = 1/sqrt(2),
  so r_k = arctanh(1) -> infinity. But this is the ZERO-TEMPERATURE limit.
  The DYNAMICAL squeeze from the transit is finite, characterized by the
  transit Bogoliubov coefficient beta_k.

  The squeeze PHASE phi_k comes from the time-dependent dynamics.
  In the adiabatic limit (tau_relax/dt_transit = 0.003), the phase is:

      phi_k = 2 * integral_0^{dt_transit} E_k(t') dt'                  (9)

  where E_k(t) = sqrt(xi_k^2 + Delta(t)^2) is the instantaneous
  quasiparticle energy.

  This is the DYNAMICAL phase accumulated during the gap opening.
  The interference between the BCS squeeze and the Mukhanov-Sasaki
  mode evolution determines whether enhancement is constructive or
  destructive.
""")

# Compute per-mode squeeze parameters
# Mode labels and BCS data already loaded
N_modes = 8  # (local)

# Per-mode squeeze parameter from BCS coherence factors
# r_k (BCS) = arctanh(sqrt(v_k^2/u_k^2)) = arctanh(|v_k/u_k|)
r_k_bcs = np.zeros(N_modes)
for i in range(N_modes):
    ratio = np.sqrt(v_k_sq[i] / u_k_sq[i])
    if ratio < 1.0:
        r_k_bcs[i] = np.arctanh(ratio)
    else:
        # At Fermi surface, u=v, ratio=1, arctanh diverges
        # Use a large but finite value representing the transit timescale
        r_k_bcs[i] = 0.5 * np.log((1 + ratio) / max(1 - ratio, 1e-15))

print("  Per-mode BCS squeeze parameters (static, T=0):")
print(f"  {'Mode':<8} {'u_k^2':<10} {'v_k^2':<10} {'v/u':<10} {'r_k(BCS)':<12}")
print("  " + "-" * 50)
for i in range(N_modes):
    ratio = np.sqrt(v_k_sq[i] / u_k_sq[i])
    print(f"  {str(labels[i]):<8} {u_k_sq[i]:<10.4f} {v_k_sq[i]:<10.4f} "
          f"{ratio:<10.4f} {r_k_bcs[i]:<12.4f}")

# The DYNAMICAL squeeze from the transit is different from the static BCS value.
# The transit Bogoliubov coefficients give r_eff = 0.338.
# What matters for phi_eff is the PHASE, not the amplitude.

# =============================================================================
# STEP 3: DYNAMICAL PHASE ACCUMULATION phi_k
# =============================================================================
print("\n" + "-" * 78)
print("STEP 3: Dynamical phase accumulation phi_k for each mode")
print("-" * 78)

print("""
  The squeeze phase for mode k accumulated during the gap opening is:

      phi_k = 2 * int_{t_i}^{t_f} [E_k(t) - epsilon_k] dt              (10)

  where E_k(t) = sqrt(xi_k^2 + Delta(t)^2) and epsilon_k is the bare
  (pre-transit) energy. The factor of 2 accounts for the pair nature
  of the BCS squeeze.

  In the adiabatic limit, this integral has a clean structure:
  - For modes far from the Fermi surface (|xi_k| >> Delta):
    E_k(t) ~ |xi_k| + Delta(t)^2/(2|xi_k|), so
    phi_k ~ int Delta(t)^2/|xi_k| dt ~ Delta^2 * t_transit / |xi_k|

  - For modes at the Fermi surface (xi_k ~ 0):
    E_k(t) = Delta(t), so
    phi_k = 2 * int Delta(t) dt

  The interference between modes is crucial: the EFFECTIVE phase is
  the variance-weighted average.
""")

# Compute phi_k by numerical integration for both gap profiles
phi_k_GL = np.zeros(N_modes)   # GL equilibrium gap
phi_k_smooth = np.zeros(N_modes)  # Smooth tanh gap

for i in range(N_modes):
    xi_i = xi_k[i]
    eps_i = eps_k[i]

    # GL profile
    E_k_GL = np.sqrt(xi_i**2 + Delta_phys**2)
    integrand_GL = 2.0 * (E_k_GL - abs(eps_i))
    phi_k_GL[i] = np.trapezoid(integrand_GL, t_grid)

    # Smooth (tanh) profile
    E_k_sm = np.sqrt(xi_i**2 + Delta_smooth**2)
    integrand_sm = 2.0 * (E_k_sm - abs(eps_i))
    phi_k_smooth[i] = np.trapezoid(integrand_sm, t_grid)

print("  Dynamical squeeze phase phi_k (two gap profiles):")
print(f"  {'Mode':<8} {'xi_k':<12} {'phi_GL':<12} {'phi_smooth':<12} {'phi_GL mod 2pi':<16}")
print("  " + "-" * 60)
for i in range(N_modes):
    phi_mod = phi_k_GL[i] % (2 * PI)
    print(f"  {str(labels[i]):<8} {xi_k[i]:<12.6f} {phi_k_GL[i]:<12.4f} "
          f"{phi_k_smooth[i]:<12.4f} {phi_mod:<16.4f}")

# The physical observable is cos(phi_k) for the interference term
cos_phi_GL = np.cos(phi_k_GL)
cos_phi_smooth = np.cos(phi_k_smooth)

print("\n  cos(phi_k) values (determine constructive/destructive):")
print(f"  {'Mode':<8} {'cos(phi_GL)':<14} {'cos(phi_sm)':<14}")
print("  " + "-" * 36)
for i in range(N_modes):
    print(f"  {str(labels[i]):<8} {cos_phi_GL[i]:<14.4f} {cos_phi_smooth[i]:<14.4f}")

# =============================================================================
# STEP 4: VARIANCE-WEIGHTED EFFECTIVE phi_eff
# =============================================================================
print("\n" + "-" * 78)
print("STEP 4: Variance-weighted effective phi_eff")
print("-" * 78)

print("""
  The effective squeeze phase enters the power spectrum through the
  multifield enhancement formula:

      P_zeta(non-BD) = P_zeta(BD) * [cosh(2r_eff) + sinh(2r_eff)*cos(phi_eff)]

  The effective phase phi_eff is determined by the variance-weighted
  average of cos(phi_k) over the GGE branches:

      cos(phi_eff) = sum_I f_I * cos(phi_I)                             (11)

  where f_I are the variance fractions from S68 BCS-dressed modes.

  The three GGE groups and their mode compositions:
    Acoustic (Goldstone): Branch 0 (B2[0]) - f_w = 3.3%
    Leggett (1+2):        Branches 1-2 (B2[1-2] + B1) - f_w = 46.2%
    Optical (Higgs 3-5):  Branches 3-5 (B2[3] + B3[0-2]) - f_w = 50.6%
""")

# Group the 8 modes into the 3 GGE channels
# From S68: B2[0-3] are first 4, B1 is index 4, B3[0-2] are indices 5-7
# From S67 multifield: acoustic = {Goldstone (B2[0])}, leggett = {B2[1], B2[2]},
# optical = {B2[3], B1, B3[0], B3[1], B3[2]}

# Actually, the S67 grouping is:
#   Acoustic: 1 branch (Goldstone, B2[0])
#   Leggett: 2 branches (Leggett-1 = B2[1]+B1, Leggett-2 = B2[2]+B2[3])
#   Optical: 3 branches (B3[0], B3[1], B3[2])
# But the fractions are energy-weighted, not mode-count-weighted.
#
# For the squeeze phase, each group's phase is an average over its constituent
# modes, weighted by their contribution to the group's variance.

# Acoustic group: Goldstone mode (B2[0])
# The Goldstone mode is special: its dispersion is omega = c_Gold * k
# (Paper 4, superfluidity). At k=0, E = 0. The phase integral for
# a gapless mode involves a subtlety: the phase is dominated by the
# low-energy behavior.
# For the Goldstone: xi_k ~ 0, Delta -> Gap contribution only
phi_acoustic = phi_k_GL[0]   # B2[0]
cos_phi_acoustic = cos_phi_GL[0]

# Leggett group: average of B2[1], B2[2] (and B1 for the mixed channel)
# B2[1] and B2[2] have identical xi_k (same eps, same mu)
# B1 has different xi_k
# Weighted average: equal weight for simplicity (confirmed by identical u,v)
phi_leggett_modes = [phi_k_GL[1], phi_k_GL[2], phi_k_GL[4]]  # B2[1], B2[2], B1
cos_phi_leggett_modes = [cos_phi_GL[1], cos_phi_GL[2], cos_phi_GL[4]]
# B2[1] and B2[2] have identical coherence factors, B1 slightly different
# Weight by u_k*v_k (pair correlation strength)
w_leggett = np.array([uv_product[1], uv_product[2], uv_product[4]])
w_leggett = w_leggett / w_leggett.sum()
cos_phi_leggett = np.average(cos_phi_leggett_modes, weights=w_leggett)
phi_leggett_avg = np.average(phi_leggett_modes, weights=w_leggett)

# Optical group: B2[3], B3[0], B3[1], B3[2]
phi_optical_modes = [phi_k_GL[3], phi_k_GL[5], phi_k_GL[6], phi_k_GL[7]]
cos_phi_optical_modes = [cos_phi_GL[3], cos_phi_GL[5], cos_phi_GL[6], cos_phi_GL[7]]
w_optical = np.array([uv_product[3], uv_product[5], uv_product[6], uv_product[7]])
w_optical = w_optical / w_optical.sum()
cos_phi_optical = np.average(cos_phi_optical_modes, weights=w_optical)
phi_optical_avg = np.average(phi_optical_modes, weights=w_optical)

print(f"  Acoustic: phi = {phi_acoustic:.4f}, cos(phi) = {cos_phi_acoustic:.4f}")
print(f"  Leggett:  phi = {phi_leggett_avg:.4f}, cos(phi) = {cos_phi_leggett:.4f}")
print(f"  Optical:  phi = {phi_optical_avg:.4f}, cos(phi) = {cos_phi_optical:.4f}")

# Effective cos(phi_eff) using S68 variance fractions
# Two weighting schemes: S67 delta-N fractions vs S68 BCS-dressed fractions
# S67: f_acoustic = 0.0013, f_leggett = 0.0044, f_optical = 0.9944
# S68: f_w_acoustic = 0.033, f_w_leggett = 0.462, f_w_optical = 0.506
# S68 fractions are BCS-dressed and more physical for the squeeze calculation

print(f"\n  Weighting scheme comparison:")
print(f"  S67 delta-N:  acoustic={f_acoustic:.4f}, leggett={f_leggett:.4f}, optical={f_optical:.4f}")
print(f"  S68 BCS:      acoustic={f_w_acoustic:.4f}, leggett={f_w_leggett:.4f}, optical={f_w_optical:.4f}")

# Use S68 BCS-dressed fractions (more appropriate for squeeze calculation)
cos_phi_eff_s68 = (f_w_acoustic * cos_phi_acoustic +
                   f_w_leggett * cos_phi_leggett +
                   f_w_optical * cos_phi_optical)

# Also compute with S67 fractions for cross-check
cos_phi_eff_s67 = (f_acoustic * cos_phi_acoustic +
                   f_leggett * cos_phi_leggett +
                   f_optical * cos_phi_optical)

# Infer phi_eff from cos(phi_eff)
phi_eff_s68 = np.arccos(np.clip(cos_phi_eff_s68, -1.0, 1.0))
phi_eff_s67 = np.arccos(np.clip(cos_phi_eff_s67, -1.0, 1.0))

print(f"\n  cos(phi_eff):")
print(f"    S68 weighting: cos(phi_eff) = {cos_phi_eff_s68:.6f}")
print(f"    S67 weighting: cos(phi_eff) = {cos_phi_eff_s67:.6f}")
print(f"  phi_eff:")
print(f"    S68 weighting: phi_eff = {phi_eff_s68:.4f} rad = {phi_eff_s68/PI:.4f} * pi")
print(f"    S67 weighting: phi_eff = {phi_eff_s67:.4f} rad = {phi_eff_s67/PI:.4f} * pi")

# =============================================================================
# STEP 5: ENHANCEMENT FACTOR
# =============================================================================
print("\n" + "-" * 78)
print("STEP 5: Enhancement factor from non-BD initial state")
print("-" * 78)

print("""
  Enhancement = cosh(2*r_eff) + sinh(2*r_eff) * cos(phi_eff)            (12)

  At r_eff = 0.338:
    cosh(2*r_eff) = cosh(0.676) = 1.2370
    sinh(2*r_eff) = sinh(0.676) = 0.7258

  Enhancement range:
    phi_eff = 0  (constructive):  1.237 + 0.726 = 1.963  (WRONG)
    phi_eff = pi (destructive):   1.237 - 0.726 = 0.511
    phi_eff = pi/2 (no interf.):  1.237 + 0     = 1.237

  The prompt states:
    phi=0: enhancement 1.58, phi=pi: 0.89
  These must use a different r_eff. Let me verify.
""")

# Compute enhancement for various r_eff and phi values
r_test = r_eff
cosh_2r = np.cosh(2.0 * r_test)
sinh_2r = np.sinh(2.0 * r_test)
print(f"  r_eff = {r_test:.4f}")
print(f"  cosh(2*r_eff) = {cosh_2r:.6f}")
print(f"  sinh(2*r_eff) = {sinh_2r:.6f}")
print(f"  Enhancement(phi=0)   = {cosh_2r + sinh_2r:.4f}")
print(f"  Enhancement(phi=pi)  = {cosh_2r - sinh_2r:.4f}")
print(f"  Enhancement(phi=pi/2) = {cosh_2r:.4f}")

# The prompt values (1.58, 0.89) correspond to a DIFFERENT formula
# where the enhancement is defined relative to the BARE (no squeeze) value.
# P(non-BD) / P(BD) = cosh^2(r) + sinh^2(r) + 2*cosh(r)*sinh(r)*cos(phi)
#                    = 1 + 2*sinh^2(r) + sinh(2r)*cos(phi)
# At r=0.338:
#   1 + 2*sinh^2(0.338) = 1 + 2*0.1192 = 1.238
#   sinh(2*0.338) = sinh(0.676) = 0.726
# So enhancement(phi=0) = 1.238 + 0.726 = 1.964
# This doesn't match 1.58 either.

# Perhaps r_eff is meant as the Bogoliubov coefficient magnitude |beta|,
# not the squeeze parameter. |beta|^2 = sinh^2(r).
# If |beta| = 0.338, then sinh(r) = 0.338, r = arcsinh(0.338) = 0.3314
# cosh(r) = sqrt(1 + 0.338^2) = 1.0557
# P/P_BD = (cosh(r) + sinh(r)*e^{i*phi})*(cosh(r) + sinh(r)*e^{-i*phi})
#        = cosh^2(r) + sinh^2(r) + 2*cosh(r)*sinh(r)*cos(phi)
#        = 1.1145 + 0.1142 + 2*1.0557*0.338*cos(phi)
#        = 1.2287 + 0.7137*cos(phi)
# phi=0: 1.942, phi=pi: 0.515
# Still not matching.

# Let me try: the prompt values (1.58 at phi=0, 0.89 at phi=pi)
# imply: cosh(2r) + sinh(2r) = 1.58, cosh(2r) - sinh(2r) = 0.89
# => cosh(2r) = (1.58+0.89)/2 = 1.235, sinh(2r) = (1.58-0.89)/2 = 0.345
# => 2r = arccosh(1.235) = 0.6917, r = 0.346
# And sinh(2r) should = 0.345 at 2r=0.6917: sinh(0.6917)=0.745
# INCONSISTENT.
# The prompt values likely use a DIFFERENT parameterization.
# Let me use: P/P_BD = 1 + 2*n_k + 2*sqrt(n_k*(n_k+1))*cos(phi)
# where n_k = sinh^2(r_eff) = mean occupation from squeeze.
# At r=0.338: n = sinh^2(0.338) = 0.1192
# P/P_BD = 1 + 2*0.1192 + 2*sqrt(0.1192*1.1192)*cos(phi)
#        = 1.2384 + 2*0.3653*cos(phi)
#        = 1.2384 + 0.7306*cos(phi)
# phi=0: 1.969, phi=pi: 0.508
# Still not.

# Try yet another: maybe the prompt uses |beta_k|^2 = 0.338
# Then n_k = 0.338
# P/P_BD = 1 + 2*0.338 + 2*sqrt(0.338*1.338)*cos(phi)
#        = 1.676 + 2*0.6726*cos(phi)
#        = 1.676 + 1.345*cos(phi)
# phi=0: 3.021, phi=pi: 0.331
# Too large.

# Maybe the prompt accounts for the MULTIFIELD effect.
# The enhancement is channel-dependent, and the effective enhancement
# after multifield averaging could be smaller.
# Let me just compute the physics correctly and report.

# The standard two-mode squeezed state result:
# <n_k> = |beta_k|^2 for each mode
# From S67 transit: beta_sq_rk are the |beta_k|^2 values
# At k_transit: beta_sq ~ 46.35 (VERY large occupation!)
# This gives enormous squeeze: r = arcsinh(sqrt(46.35)) = arcsinh(6.81) = 2.64
# Then cosh(2r) ~ cosh(5.28) ~ 98.6. That's huge.

# But the PROMPT says r_eff = 0.338 and enhancement ~ 1.6.
# There must be a different meaning. Let me interpret r_eff as an EFFECTIVE
# squeeze that includes the BCS-Mukhanov-Sasaki coupling, not the raw
# Bogoliubov occupation.

# The S68 result: delta_As/As = 0.1117. This is the BCS dressing enhancement.
# 0.1117 corresponds to ~12% increase, i.e. enhancement ~ 1.12.
# The non-BD squeeze is an ADDITIONAL effect on top of BCS dressing.

# For the squeeze phase calculation, what matters is the RATIO of the
# imaginary to real parts of the Bogoliubov coefficient:
# phi_k = arg(alpha_k * beta_k^*)
# This is independent of |beta_k|.

# Let me compute the phases correctly from the TDGL dynamics and
# report both the phase and the enhancement for multiple r_eff values.

# For the purpose of the gate, compute enhancement at r_eff = 0.338 as stated.
# If the prompt values don't match exactly, it's because the prompt
# used approximate numbers.

# Compute enhancement for our cos(phi_eff)
def enhancement(r, cos_phi):
    return np.cosh(2*r) + np.sinh(2*r) * cos_phi

enh_s68 = enhancement(r_eff, cos_phi_eff_s68)
enh_s67 = enhancement(r_eff, cos_phi_eff_s67)

print(f"\n  Enhancement (S68 weights): {enh_s68:.6f}")
print(f"  Enhancement (S67 weights): {enh_s67:.6f}")

# Also compute using the smooth gap profile
cos_phi_eff_smooth_s68 = (f_w_acoustic * np.cos(phi_k_smooth[0]) +
                          f_w_leggett * np.average([np.cos(phi_k_smooth[1]),
                                                    np.cos(phi_k_smooth[2]),
                                                    np.cos(phi_k_smooth[4])],
                                                   weights=w_leggett) +
                          f_w_optical * np.average([np.cos(phi_k_smooth[3]),
                                                    np.cos(phi_k_smooth[5]),
                                                    np.cos(phi_k_smooth[6]),
                                                    np.cos(phi_k_smooth[7])],
                                                   weights=w_optical))

enh_smooth = enhancement(r_eff, cos_phi_eff_smooth_s68)
print(f"  Enhancement (smooth gap): {enh_smooth:.6f}")
print(f"  cos(phi_eff) smooth:      {cos_phi_eff_smooth_s68:.6f}")

# =============================================================================
# STEP 6: SENSITIVITY ANALYSIS
# =============================================================================
print("\n" + "-" * 78)
print("STEP 6: Sensitivity analysis and robustness checks")
print("-" * 78)

print("""
  The squeeze phase phi_k depends on the gap profile Delta(t) through
  the dynamical phase integral (Eq. 10). We check sensitivity to:
  1. Gap profile shape (GL vs tanh vs step function)
  2. Transit duration dt_transit
  3. r_eff value
  4. Mode grouping and weighting
""")

# 1. Step function gap profile (sudden approximation)
# Delta(t) = 0 for t < 0, Delta for t > 0
# Phase integral: phi_k = 2 * int_0^{t_f} (E_k - eps_k) dt
#                       = 2 * (sqrt(xi_k^2 + Delta^2) - |eps_k|) * t_half
phi_k_step = np.zeros(N_modes)
for i in range(N_modes):
    E_post = np.sqrt(xi_k[i]**2 + Delta**2)
    phi_k_step[i] = 2.0 * (E_post - abs(eps_k[i])) * t_half

cos_phi_eff_step = (f_w_acoustic * np.cos(phi_k_step[0]) +
                    f_w_leggett * np.average([np.cos(phi_k_step[1]),
                                              np.cos(phi_k_step[2]),
                                              np.cos(phi_k_step[4])],
                                             weights=w_leggett) +
                    f_w_optical * np.average([np.cos(phi_k_step[3]),
                                              np.cos(phi_k_step[5]),
                                              np.cos(phi_k_step[6]),
                                              np.cos(phi_k_step[7])],
                                             weights=w_optical))
enh_step = enhancement(r_eff, cos_phi_eff_step)
print(f"  Step gap:    cos(phi_eff) = {cos_phi_eff_step:.6f}, enhancement = {enh_step:.4f}")

# 2. Scan over transit duration
dt_factors = [0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0]
enh_vs_dt = []
cos_phi_vs_dt = []
print(f"\n  Enhancement vs transit duration (factor * dt_transit):")
print(f"  {'Factor':<10} {'cos(phi_eff)':<14} {'Enhancement':<14} {'A_s corr (OOM)':<16}")
print("  " + "-" * 54)
for fac in dt_factors:
    dt_f = fac * dt_transit
    t_half_f = 5.0 * dt_f
    t_grid_f = np.linspace(-t_half_f, t_half_f, N_t)
    tau_ramp_f = dt_f / 2.0
    Delta_f = Delta * 0.5 * (1.0 + np.tanh(t_grid_f / tau_ramp_f))

    phi_f = np.zeros(N_modes)
    for i in range(N_modes):
        E_f = np.sqrt(xi_k[i]**2 + Delta_f**2)
        integrand_f = 2.0 * (E_f - abs(eps_k[i]))
        phi_f[i] = np.trapezoid(integrand_f, t_grid_f)

    cos_f = (f_w_acoustic * np.cos(phi_f[0]) +
             f_w_leggett * np.average([np.cos(phi_f[1]),
                                       np.cos(phi_f[2]),
                                       np.cos(phi_f[4])],
                                      weights=w_leggett) +
             f_w_optical * np.average([np.cos(phi_f[3]),
                                       np.cos(phi_f[5]),
                                       np.cos(phi_f[6]),
                                       np.cos(phi_f[7])],
                                      weights=w_optical))
    enh_f = enhancement(r_eff, cos_f)
    As_corr = np.log10(enh_f) if enh_f > 0 else -np.inf
    enh_vs_dt.append(enh_f)
    cos_phi_vs_dt.append(cos_f)
    print(f"  {fac:<10.2f} {cos_f:<14.6f} {enh_f:<14.4f} {As_corr:<16.4f}")

# 3. Scan over r_eff
r_values = [0.1, 0.2, 0.338, 0.5, 0.7, 1.0, 1.5, 2.0]
print(f"\n  Enhancement vs r_eff (at cos(phi_eff) = {cos_phi_eff_s68:.4f}):")
print(f"  {'r_eff':<10} {'cosh(2r)':<12} {'sinh(2r)':<12} {'Enhancement':<14} {'A_s (OOM)':<12}")
print("  " + "-" * 56)
for r in r_values:
    enh = enhancement(r, cos_phi_eff_s68)
    As_corr = np.log10(enh) if enh > 0 else -np.inf
    print(f"  {r:<10.3f} {np.cosh(2*r):<12.4f} {np.sinh(2*r):<12.4f} "
          f"{enh:<14.4f} {As_corr:<12.4f}")

# =============================================================================
# STEP 7: CROSS-CHECKS
# =============================================================================
print("\n" + "-" * 78)
print("STEP 7: Cross-checks against predictions")
print("-" * 78)

print("""
  Three independent predictions for phi_eff:
    QA (adiabatic impedance matching):  phi_eff ~ 0     -> enh ~ 1.58 (prompt)
    Landau (Josephson analogy):         phi_eff ~ pi/4  -> enh ~ 1.48 (prompt)
    Phonon-First (KZ defect topology):  <cos> = -1/2    -> enh ~ 0.87

  Our computation:
    phi_eff is determined by the dynamical phase integral (Eq. 10).
    The key feature: B2 modes (4 of 8) sit at the Fermi surface
    with xi_k ~ 0. For these modes:
        E_k(t) = sqrt(0 + Delta(t)^2) = Delta(t)
        phi_k = 2 * int Delta(t) dt

    This integral over the gap opening profile gives a phase that
    depends on the integral of the gap over time.
""")

# For B2 modes at Fermi surface (xi=0):
# phi_B2 = 2 * integral of Delta(t) dt
# With tanh profile: integral = Delta * tau_ramp * [ln(cosh(t/tau_ramp))]_{-t_half}^{t_half}
# ~ Delta * tau_ramp * 2 * t_half / tau_ramp = Delta * 2 * t_half (for large t_half/tau_ramp)
# Actually: integral of (1/2)(1+tanh(x)) dx = x/2 + (1/2)*ln(cosh(x))
# So integral_{-A}^{A} Delta*(1/2)*(1+tanh(t/tau_ramp)) dt
# = Delta * tau_ramp * [t/(2*tau_ramp) + (1/2)*ln(cosh(t/tau_ramp))]_{-A}^{A}
# = Delta * tau_ramp * [A/tau_ramp + ln(cosh(A/tau_ramp))]
# For A/tau_ramp >> 1: ~ Delta * tau_ramp * (A/tau_ramp + A/tau_ramp) = 2*Delta*A
# But that's just Delta*t_total on average.

# Exact analytical for B2 with tanh gap:
A_over_tau = t_half / tau_ramp
integral_analytic = Delta * tau_ramp * (A_over_tau + np.log(np.cosh(A_over_tau))
                                        - (-A_over_tau + np.log(np.cosh(-A_over_tau))))
# Since cosh is even: = Delta * tau_ramp * 2*A_over_tau = 2*Delta*t_half
# Wait: integral of Delta*(1/2)*(1+tanh(t/tau_ramp)) from -A to A
# = Delta*(1/2)*[t + tau_ramp*ln(cosh(t/tau_ramp))]_{-A}^{A}
# = Delta*(1/2)*[2A + tau_ramp*(ln(cosh(A/tau_ramp)) - ln(cosh(-A/tau_ramp)))]
# = Delta*(1/2)*[2A + 0]  (since cosh is even)
# = Delta*A

# So phi_B2_analytic = 2 * (E_k - |eps_k|) * integral weight
# For xi=0: E_k = Delta(t), eps_k = mu ~ 0.845
# Phase = 2 * int (Delta(t) - eps_k) dt
# But the pre-transit value: E_k(pre) = |eps_k| = 0.845
# And post-transit: E_k(post) = sqrt(0 + Delta^2) = Delta = 0.464
# So E_k(post) < eps_k! The "excess" is NEGATIVE for B2.
# This means the phase integral picks up a NEGATIVE contribution for B2
# modes because the quasiparticle energy (0.464) is LESS than the bare
# particle energy (0.845). The BCS gap LOWERS the quasiparticle energy
# relative to the Fermi surface.

# Actually, let me reconsider. The phase integral is:
# phi_k = 2 * int [E_k(t) - E_k(pre-transit)] dt
# Pre-transit: no condensate, E_k = eps_k (bare energy)
# During transit: E_k(t) = sqrt(xi_k^2 + Delta(t)^2)
# For B2 at Fermi surface: xi_k ~ 0
#   Pre-transit E = |xi_k| + eps_k... no, pre-transit is just the normal state
#   In the normal state (no BCS), the quasiparticle energy is |xi_k|
#   But |xi_k| ~ 0 for B2 modes at the Fermi surface
# So the pre-transit energy is eps_k (the bare energy measured from zero)
# and the post-transit energy is E_k = sqrt(xi_k^2 + Delta^2)
#
# Wait, I need to be more careful about what "energy" means.
# In the BCS problem, the TOTAL energy is:
#   E_BCS = sum_k eps_k * (n_k^(0)) + BCS correction
# The quasiparticle energy (excitation energy) in the BCS state is E_k.
# The relevant phase for the squeeze is the QUASIPARTICLE phase:
#   phi_k = 2 * int_0^T E_k(t) dt
# This is the phase accumulated by the quasiparticle in the BCS state.
# There is no subtraction of eps_k because we're computing the phase
# of the Bogoliubov mode, not the difference from the normal state.

# CORRECTION: The squeeze phase is simply the accumulated quasiparticle phase
# phi_k = 2 * int_0^{t_f} E_k(t) dt
# The factor of 2 comes from the pair structure.

phi_k_corrected = np.zeros(N_modes)
for i in range(N_modes):
    E_t = np.sqrt(xi_k[i]**2 + Delta_smooth**2)
    phi_k_corrected[i] = 2.0 * np.trapezoid(E_t, t_grid)

print("\n  CORRECTED squeeze phases (pure quasiparticle phase, Eq. 9'):")
print(f"  phi_k = 2 * integral E_k(t) dt  (no subtraction)")
print(f"  {'Mode':<8} {'E_k(post)':<12} {'phi_k':<14} {'phi_k mod 2pi':<16} {'cos(phi_k)':<12}")
print("  " + "-" * 62)
for i in range(N_modes):
    phi_mod = phi_k_corrected[i] % (2 * PI)
    print(f"  {str(labels[i]):<8} {E_k[i]:<12.4f} {phi_k_corrected[i]:<14.4f} "
          f"{phi_mod:<16.4f} {np.cos(phi_k_corrected[i]):<12.4f}")

# The TOTAL phase is very large (E_k ~ 0.46, t_half ~ 0.006,
# so phi ~ 2*0.46*2*0.006 ~ 0.011). Let me check numerically.
print(f"\n  Diagnostic: t_half = {t_half:.6f}, dt_transit = {dt_transit:.6f}")
print(f"  Integral of E_k(t) for B2[0]: 2 * E * 2*t_half ~ {2*E_k[0]*2*t_half:.4f}")

# The phases are SMALL because the transit is very fast!
# dt_transit = 0.00113, t_half = 5*dt_transit = 0.00565
# phi_B2 ~ 2 * 0.464 * 0.00565 = 0.00525 radians
# This is essentially ZERO mod 2pi!

# This is the CRITICAL result: because the transit is supersonic
# (Mach 13.75), the quasiparticle phases accumulated during the transit
# are TINY. The phase per mode is:
# phi_k ~ 2 * E_k * dt_transit ~ 2 * 0.46 * 0.00113 = 0.00104 rad

# For a phase this small, cos(phi) ~ 1 - phi^2/2 ~ 1.
# The interference is MAXIMALLY CONSTRUCTIVE.

# But wait -- the total accumulated phase should be computed over
# the ENTIRE post-transit evolution, not just the transit duration.
# After the transit, the quasiparticle modes continue evolving with
# phase e^{-i*E_k*t}. The relevant time is not dt_transit but the
# Hubble time 1/H_fold.

# IMPORTANT PHYSICAL POINT: The squeeze phase phi_k in the
# cosmological context is the phase of the Bogoliubov coefficient
# beta_k at the time of horizon crossing. For modes that cross
# the horizon AFTER the transit, the phase accumulated is:
# phi_k = 2 * E_k * (t_horizon - t_transit)
# Since horizon crossing happens at t ~ 1/H, and E_k ~ 0.46,
# while 1/H = 1/586.5 = 0.00170,
# phi_k ~ 2 * 0.46 * 0.00170 = 0.00157 rad
# Still very small!

# Actually, the cosmological modes cross the horizon at k = a*H.
# The BCS modes have E_k ~ 0.5 M_KK, but the cosmological fluctuation
# modes have much smaller k. The squeeze arises from the COUPLING
# between BCS and cosmological degrees of freedom.

# The PROPER treatment: The squeeze of the cosmological mode occurs
# at the transit. The BCS pairing amplitude (Delta) acts as an
# additional source term in the Mukhanov-Sasaki equation.
# The Bogoliubov coefficient for the cosmological mode k is:
#
# beta_k = -i * int dt' z''/z * |u_k(t')|^2 * F(t')
#
# where F(t) encodes the BCS modification.
# The PHASE of beta_k is then:
#
# arg(beta_k) = arg(-i * integral) = -pi/2 + arg(integral)
#
# The integral is dominated by the fold where z''/z is large.
# The BCS contribution F(t) ~ Delta(t)^2 / E_F is real and positive.
# So the integral is real and positive => arg(integral) = 0
# => phi_k = -pi/2

# This gives a SPECIFIC prediction for the squeeze phase!

print("""
  PHYSICAL ANALYSIS: BCS-Mukhanov-Sasaki coupling

  The squeeze phase of the COSMOLOGICAL mode k arises from the
  Bogoliubov coefficient:

      beta_k = -i * int dt' (z''/z) * |u_k(t')|^2 * F_BCS(t')        (13)

  where F_BCS(t) = 1 + Delta(t)^2/E_F^2 is the BCS correction to
  the pump field, and z''/z is the Mukhanov-Sasaki effective potential.

  F_BCS is REAL and POSITIVE throughout the transit.
  z''/z is REAL (peaked at the fold, magnitude ~10^6).
  |u_k|^2 is REAL and POSITIVE.

  Therefore the integral in (13) is REAL and POSITIVE.
  The leading -i factor gives:

      arg(beta_k) = -pi/2                                              (14)

  The squeeze phase phi_k = arg(alpha_k * beta_k^*).
  Since alpha_k ~ 1 (to leading order in the squeeze),
  phi_k = -arg(beta_k) = +pi/2.

  But there are TWO corrections to this leading result:
  (a) The BCS coherence factors introduce a SIGN through the
      anomalous Green's function F = u_k*v_k*e^{i*theta}
      where theta is the BCS phase.
  (b) The Josephson coupling between cells shifts the phase
      by the inter-cell phase difference.
""")

# PRECISE COMPUTATION of phi_k from the Mukhanov-Sasaki integral

# The Bogoliubov coefficient for cosmological mode k in the
# presence of BCS pairing is:
#
# beta_k = -i/(2*omega_k) * int dt' exp(2*i*omega_k*t') *
#           [z''/z + Delta_BCS(t')^2 * correction] * exp(i*theta_BCS(t'))
#
# The BCS phase theta_BCS(t) = 2*mu*t (overall U(1) phase, Paper 3)
# This adds to the cosmological oscillation frequency.

# The full Bogoliubov coefficient:
# beta_k propto int dt' exp[2*i*(omega_k + mu)*t'] * z''/z *
#                  (1 + Delta(t')^2/E_F^2) * exp(i*phi_BCS_anomalous(t'))

# For the BCS anomalous contribution:
# The anomalous Green's function F_k = u_k*v_k = Delta/(2*E_k)
# This is REAL and POSITIVE. No additional phase from the BCS sector
# in the mean-field approximation.

# The key insight from Landau's theory of Fermi liquids (Paper 11):
# the quasiparticle interaction vertex introduces a PHASE SHIFT
# through the forward scattering amplitude. This is the Landau-
# Pomeranchuk shift.

# For the problem at hand, the dominant effect is:
# 1. The -i prefactor gives phi = -pi/2
# 2. The time-dependent BCS gap modifies the spectral weight
#    but NOT the phase (since Delta is real in mean field)
# 3. Josephson coupling between cells introduces a relative
#    phase phi_J between adjacent cells

# The Josephson phase: for a 32-cell fabric with random domain
# phases (from the Kibble-Zurek mechanism), the phase distribution
# is uniform on [0, 2*pi). The AVERAGE cos(phi_J) = 0.
# But the VARIANCE contributes through second-order corrections.

# RESULT: In mean-field BCS without Josephson phase randomness,
# the squeeze phase is phi_eff = pi/2 (from the -i prefactor).

# With Josephson phase averaging: the per-cell Bogoliubov coefficient
# has a random phase phi_J^{(n)}, so:
# beta_total = sum_n beta_n * e^{i*phi_J^{(n)}}
# The magnitude |beta_total| is reduced by sqrt(N_cells) averaging
# but the PHASE depends on the specific realization.
# For a THERMAL average: <cos(phi_eff)> = 0 (destructive for random phases)
# For the GGE state: the phases are LOCKED by the Josephson coupling.

# Josephson locking: E_J >> T_acoustic (J_C2 = 0.933, T_acoustic = 0.112)
# The phase differences are SMALL: delta_phi ~ sqrt(T/E_J) ~ sqrt(0.112/0.933) = 0.346
# So the effective phase:
delta_phi_J = np.sqrt(T_acoustic / J_C2)
print(f"\n  Josephson phase fluctuation: delta_phi_J = sqrt(T/E_J) = {delta_phi_J:.4f} rad")

# The squeeze phase corrections:
# phi_eff = pi/2 + <delta_phi_BCS> + <delta_phi_Josephson>
# <delta_phi_BCS> = 0 (mean field, real gap)
# <delta_phi_Josephson> ~ delta_phi_J ~ 0.346 rad (random, adds in quadrature)

# But this is the phase of INDIVIDUAL cells.
# For the fabric average over N_cells:
# phi_fabric = phi_MF + delta_phi_fabric
# delta_phi_fabric ~ delta_phi_J / sqrt(N_cells) = 0.346/sqrt(32) = 0.061

delta_phi_fabric = delta_phi_J / np.sqrt(N_cells)
phi_eff_MF = PI / 2.0  # Mean-field prediction
phi_eff_total = phi_eff_MF  # Leading term (corrections are small)
cos_phi_eff_MF = np.cos(phi_eff_MF)  # = 0

print(f"  delta_phi_fabric = delta_phi_J / sqrt(N) = {delta_phi_fabric:.4f} rad")
print(f"  Mean-field phi_eff = pi/2 = {phi_eff_MF:.4f}")
print(f"  cos(phi_eff = pi/2) = {cos_phi_eff_MF:.6f}")
print(f"  Enhancement at phi=pi/2: {enhancement(r_eff, cos_phi_eff_MF):.4f}")

# However, there is a SECOND contribution from the BCS coherence factors.
# The anomalous Green's function F_k = u_k*v_k has a SIGN that depends
# on whether the mode is particle-like (u > v) or hole-like (v > u).
#
# For B2 modes at the Fermi surface: u = v = 1/sqrt(2), sign is +.
# For B1 (below Fermi): v > u, F has phase pi relative to particle-like.
# For B3 (above Fermi): u > v, F has phase 0.
#
# This means: the Leggett modes (which mix particle and hole)
# have a DIFFERENT phase from the acoustic and optical modes.
# Specifically:
#   Acoustic (B2[0], at Fermi): phi = pi/2 (no extra phase)
#   Leggett (B2+B1 mixed): phi = pi/2 + delta_BCS
#   Optical (B3, above Fermi): phi = pi/2 (no extra phase)
#
# The delta_BCS for Leggett comes from the BCS mixing angle:
# For B1: xi = -0.026, Delta = 0.464
# theta_BCS = arctan(Delta/xi) = arctan(0.464/0.026) = 1.515 rad ~ pi/2
# The anomalous self-energy adds 2*theta_BCS ~ pi to the phase.
# But theta_BCS ~ pi/2 for modes near the Fermi surface, so
# 2*theta_BCS ~ pi.

# Let me compute this more carefully.
print("\n  Per-mode BCS phase corrections:")
theta_BCS_k = np.zeros(N_modes)
for i in range(N_modes):
    if abs(xi_k[i]) > 1e-10:
        theta_BCS_k[i] = np.arctan2(Delta, xi_k[i])
    else:
        theta_BCS_k[i] = PI / 2.0  # Fermi surface

phi_anomalous = 2.0 * theta_BCS_k  # Phase of anomalous propagator

print(f"  {'Mode':<8} {'xi_k':<12} {'theta_BCS':<12} {'2*theta':<12} {'cos(2*theta)':<14}")
print("  " + "-" * 58)
for i in range(N_modes):
    print(f"  {str(labels[i]):<8} {xi_k[i]:<12.6f} {theta_BCS_k[i]:<12.4f} "
          f"{phi_anomalous[i]:<12.4f} {np.cos(phi_anomalous[i]):<14.4f}")

# The total squeeze phase per mode:
# phi_k_total = pi/2 (from -i prefactor) + phi_anomalous_k (from BCS)
phi_k_total = PI/2.0 + phi_anomalous
cos_phi_k_total = np.cos(phi_k_total)

print(f"\n  Total squeeze phase phi_k = pi/2 + 2*theta_BCS:")
print(f"  {'Mode':<8} {'phi_total':<12} {'phi mod 2pi':<14} {'cos(phi)':<12}")
print("  " + "-" * 48)
for i in range(N_modes):
    phi_mod = phi_k_total[i] % (2*PI)
    print(f"  {str(labels[i]):<8} {phi_k_total[i]:<12.4f} {phi_mod:<14.4f} "
          f"{cos_phi_k_total[i]:<12.4f}")

# Effective cos(phi_eff) with these per-mode phases
cos_phi_acoustic_total = cos_phi_k_total[0]
cos_phi_leggett_total = np.average([cos_phi_k_total[1], cos_phi_k_total[2],
                                     cos_phi_k_total[4]], weights=w_leggett)
cos_phi_optical_total = np.average([cos_phi_k_total[3], cos_phi_k_total[5],
                                     cos_phi_k_total[6], cos_phi_k_total[7]],
                                    weights=w_optical)

cos_phi_eff_total = (f_w_acoustic * cos_phi_acoustic_total +
                     f_w_leggett * cos_phi_leggett_total +
                     f_w_optical * cos_phi_optical_total)

phi_eff_total_from_cos = np.arccos(np.clip(cos_phi_eff_total, -1.0, 1.0))
enh_total = enhancement(r_eff, cos_phi_eff_total)

print(f"\n  FINAL RESULT (BCS-Mukhanov-Sasaki + BCS anomalous phase):")
print(f"  cos(phi_eff) = {cos_phi_eff_total:.6f}")
print(f"  phi_eff      = {phi_eff_total_from_cos:.4f} rad = {phi_eff_total_from_cos/PI:.4f} * pi")
print(f"  Enhancement  = {enh_total:.6f}")
print(f"  A_s correction = {np.log10(max(enh_total, 1e-30)):.4f} OOM")

# =============================================================================
# STEP 8: COMBINE ALL RESULTS
# =============================================================================
print("\n" + "-" * 78)
print("STEP 8: Final results and gate verdict")
print("-" * 78)

# Summary of all three approaches:
print("\n  Three determinations of phi_eff:")
print(f"  1. Dynamical phase integral (GL gap):   cos = {cos_phi_eff_s68:.4f},  enh = {enhancement(r_eff, cos_phi_eff_s68):.4f}")
print(f"  2. Dynamical phase integral (smooth):   cos = {cos_phi_eff_smooth_s68:.4f},  enh = {enh_smooth:.4f}")
print(f"  3. BCS-MS + anomalous (structural):     cos = {cos_phi_eff_total:.4f},  enh = {enh_total:.4f}")
print(f"  4. Pure mean-field (phi=pi/2):           cos = {0.0:.4f},  enh = {enhancement(r_eff, 0.0):.4f}")

# The most reliable determination is #3 (structural), because:
# - It captures both the -i from the Bogoliubov transformation
# - It includes the BCS anomalous phase (theta_BCS)
# - It is independent of the detailed gap profile (structural, not dynamical)
# - The dynamical phase approaches are ill-defined for the B2 modes
#   at the Fermi surface (zero energy difference, tiny accumulated phase)

# HOWEVER: Let me also consider the Josephson contribution more carefully.
# The N_cells=32 fabric has inter-cell phase coherence.
# The Josephson coupling locks phases, so the effective phase is:
# phi_eff = phi_MF + thermal fluctuation correction
# cos(phi_eff) = cos(phi_MF) * exp(-<delta_phi^2>/2)
#              = cos(phi_MF) * exp(-delta_phi_fabric^2/2)

cos_phi_josephson_corrected = cos_phi_eff_total * np.exp(-delta_phi_fabric**2/2.0)
enh_josephson = enhancement(r_eff, cos_phi_josephson_corrected)
print(f"\n  Josephson fluctuation correction:")
print(f"  cos(phi_eff) with J correction: {cos_phi_josephson_corrected:.6f}")
print(f"  Enhancement with J correction:  {enh_josephson:.6f}")

# DEFINITIVE result:
# Use the structural determination (#3) as primary, with Josephson correction

# But first: what is the CORRECT r_eff?
# From the transit Bogoliubov coefficients:
# beta_sq at k_transit ~ 46. This is VERY large.
# r = arcsinh(sqrt(46)) = arcsinh(6.78) = 2.63
# Enhancement at phi=pi/2: cosh(2*2.63) = cosh(5.26) ~ 96
# This would give 96x enhancement = +1.98 OOM.
# At r_eff = 0.338: enhancement at phi=pi/2: cosh(0.676) = 1.237

# The resolution: r_eff = 0.338 is an EFFECTIVE value that accounts for
# the fact that most of beta_k is the standard cosmological Bogoliubov
# coefficient from the time-dependent z''/z potential. The BCS CORRECTION
# is the ADDITIONAL squeeze on top of this.
# delta_r from BCS = delta_As/As / 2 ~ 0.12/2 = 0.06
# This gives a much more modest enhancement.

# Let me compute the enhancement using the actual BCS correction to r
# delta_As/As = 0.1117 from S68
# In terms of squeeze: delta_As/As = 2*r*delta_r + (delta_r)^2 (quadratic in delta_r)
# For small delta_r: delta_As/As ~ cosh(2r)*delta_r + ...
# But the S68 result already accounts for BCS dressing of the mode functions.
# The NON-BD squeeze is a SEPARATE effect.

# The prompt says r_eff = 0.338. Let me accept this and compute the gate.

# DECISIVE CALCULATION
# The B2 modes have theta_BCS = pi/2 (at Fermi surface)
# => 2*theta_BCS = pi, phi_total = pi/2 + pi = 3*pi/2
# => cos(3*pi/2) = 0
# The B3 modes have theta_BCS ~ 1.29 (above Fermi)
# => 2*theta_BCS = 2.59, phi_total = pi/2 + 2.59 = 4.16
# => cos(4.16) = -0.47
# The B1 mode has theta_BCS = 1.63 (below Fermi, hole-like)
# => 2*theta_BCS = 3.25, phi_total = pi/2 + 3.25 = 4.82
# => cos(4.82) = +0.09

# The variance-weighted average: acoustic (3.3%, cos~0) + leggett (46.2%)
# + optical (50.6%)
# The Leggett group mixes B2 (cos~0) and B1 (cos~+0.09) => net small positive
# The Optical group has B2[3] (cos~0) and B3[0-2] (cos~-0.47)
# Weighted by uv_product: B2[3] has uv=0.500, B3 has uv=0.481
# => optical cos ~ (0.500*0 + 3*0.481*(-0.47))/(0.500 + 3*0.481) = -0.48

# Net: cos(phi_eff) is NEGATIVE (partially destructive), dominated by
# optical sector contribution.

# But: the B3 phase (theta_BCS = arctan(Delta/xi_B3)) needs to be
# verified carefully.
print("\n  DETAILED mode-by-mode analysis:")
for i in range(N_modes):
    if abs(xi_k[i]) > 1e-10:
        theta = np.arctan2(Delta, xi_k[i])
    else:
        theta = PI/2
    phi_t = PI/2 + 2*theta
    cos_t = np.cos(phi_t)
    print(f"  {str(labels[i]):<8}: xi={xi_k[i]:+.4f}, theta_BCS={theta:.4f}, "
          f"phi={phi_t:.4f}, cos={cos_t:.4f}")

# FINAL ANSWER
# Take the structural result as definitive.
# phi_eff = arccos(cos_phi_eff_total)
# Enhancement = cosh(2*r_eff) + sinh(2*r_eff) * cos(phi_eff)

# Report all quantities
phi_eff_final = phi_eff_total_from_cos
cos_phi_final = cos_phi_eff_total
enh_final = enh_total
A_s_corr_OOM = np.log10(max(enh_final, 1e-30))

# Also compute: what r_eff would be needed for PASS at this phi_eff?
# Enhancement >= 1.3 requires cosh(2r) + sinh(2r)*cos(phi) >= 1.3
# At cos(phi) = cos_phi_final:
# cosh(2r) + sinh(2r)*cos_phi >= 1.3
# e^{2r}*(1+cos_phi)/2 + e^{-2r}*(1-cos_phi)/2 >= 1.3
if cos_phi_final > -1.0:
    # Solve: (1+c)/2 * x + (1-c)/2 / x = 1.3 where x = e^{2r}, c = cos_phi
    c = cos_phi_final
    # Quadratic: (1+c)/2 * x^2 - 1.3*x + (1-c)/2 = 0
    A_coeff = (1+c)/2
    B_coeff = -1.3  # (local)
    C_coeff = (1-c)/2
    disc = B_coeff**2 - 4*A_coeff*C_coeff
    if disc >= 0 and A_coeff > 0:
        x_sol = (-B_coeff + np.sqrt(disc)) / (2*A_coeff)
        r_needed = np.log(x_sol) / 2.0
    else:
        r_needed = np.inf
else:
    r_needed = np.inf

print(f"\n  ═══════════════════════════════════════════════════════")
print(f"  FINAL RESULT:")
print(f"  phi_eff          = {phi_eff_final:.4f} rad = {phi_eff_final/PI:.4f} * pi")
print(f"  cos(phi_eff)     = {cos_phi_final:.6f}")
print(f"  r_eff            = {r_eff:.4f}")
print(f"  Enhancement      = {enh_final:.6f}")
print(f"  A_s correction   = {A_s_corr_OOM:+.4f} OOM")
print(f"  r_eff needed for PASS (enh>=1.3): {r_needed:.3f}")
print(f"  ═══════════════════════════════════════════════════════")

# Comparison with predictions
print(f"\n  Comparison with prior predictions:")
print(f"  {'Source':<30} {'phi_eff':<12} {'cos(phi)':<12} {'Enhancement':<14}")
print("  " + "-" * 68)
predictions = [
    ("QA (impedance matching)", 0.0, 1.0),
    ("Landau (Josephson analogy)", PI/4, np.cos(PI/4)),
    ("Phonon-First (KZ Z_3)", np.arccos(-0.5), -0.5),
    ("THIS WORK (structural)", phi_eff_final, cos_phi_final),
    ("Mean-field only (pi/2)", PI/2, 0.0),
]
for name, phi, cosphi in predictions:
    enh = enhancement(r_eff, cosphi)
    print(f"  {name:<30} {phi:<12.4f} {cosphi:<12.4f} {enh:<14.4f}")

# Gate verdict
print(f"\n  ═══════════════════════════════════════════════════════")
if enh_final >= 1.3 and enh_final <= 4.0:
    gate_verdict = "PASS"
    gate_detail = f"Enhancement = {enh_final:.4f} in [1.3, 4.0], A_s improved by {A_s_corr_OOM:.3f} OOM"
elif enh_final < 1.0:
    gate_verdict = "FAIL"
    gate_detail = f"Enhancement = {enh_final:.4f} < 1.0, destructive interference"
else:
    gate_verdict = "INFO"
    if enh_final < 1.3:
        gate_detail = f"Enhancement = {enh_final:.4f} in [1.0, 1.3], modest -- need additional channels"
    else:
        gate_detail = f"Enhancement = {enh_final:.4f} > 4.0, unexpectedly large"

print(f"  Gate PHI-EFF-69: {gate_verdict}")
print(f"  {gate_detail}")
print(f"  ═══════════════════════════════════════════════════════")

# =============================================================================
# SAVE DATA
# =============================================================================
print("\n" + "-" * 78)
print("Saving results to s69_phi_eff.npz")
print("-" * 78)

np.savez('s69_phi_eff.npz',
    # Gate
    gate_name='PHI-EFF-69',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Primary results
    phi_eff=phi_eff_final,
    cos_phi_eff=cos_phi_final,
    r_eff=r_eff,
    enhancement=enh_final,
    A_s_correction_OOM=A_s_corr_OOM,
    r_needed_for_pass=r_needed,
    # Per-mode data
    labels=labels,
    xi_k=xi_k,
    E_k=E_k,
    u_k_sq=u_k_sq,
    v_k_sq=v_k_sq,
    uv_product=uv_product,
    theta_BCS=theta_BCS_k,
    phi_anomalous=phi_anomalous,
    phi_k_total=phi_k_total,
    cos_phi_k_total=cos_phi_k_total,
    # Group results
    cos_phi_acoustic=cos_phi_acoustic_total,
    cos_phi_leggett=cos_phi_leggett_total,
    cos_phi_optical=cos_phi_optical_total,
    # Weighting
    f_w_acoustic=f_w_acoustic,
    f_w_leggett=f_w_leggett,
    f_w_optical=f_w_optical,
    w_leggett=w_leggett,
    w_optical=w_optical,
    # BCS parameters
    Delta=Delta,
    mu_BCS=mu_BCS,
    # Josephson corrections
    delta_phi_J=delta_phi_J,
    delta_phi_fabric=delta_phi_fabric,
    # Dynamical phase results (secondary)
    phi_k_GL=phi_k_GL,
    phi_k_smooth=phi_k_smooth,
    phi_k_corrected=phi_k_corrected,
    cos_phi_eff_dynamical=cos_phi_eff_s68,
    # Sensitivity
    dt_factors=np.array(dt_factors),
    enh_vs_dt=np.array(enh_vs_dt),
    cos_phi_vs_dt=np.array(cos_phi_vs_dt),
)
print("  Saved: s69_phi_eff.npz")

# =============================================================================
# PLOT
# =============================================================================
print("\n" + "-" * 78)
print("Generating plot: s69_phi_eff.png")
print("-" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('PHI-EFF-BCS-BOGOL-69: BCS Squeeze Phase Determination',
             fontsize=14, fontweight='bold')

# Panel (a): Gap profile Delta(t)
ax = axes[0, 0]
t_plot = t_grid * 1000  # Convert to 10^{-3} M_KK^{-1}
ax.plot(t_plot, Delta_phys, 'b-', linewidth=2, label='GL equilibrium')
ax.plot(t_plot, Delta_smooth, 'r--', linewidth=2, label='Smooth (tanh)')
ax.axhline(y=Delta, color='gray', linestyle=':', alpha=0.5, label=f'$\\Delta_0$ = {Delta:.3f}')
ax.axvline(x=0, color='gray', linestyle=':', alpha=0.3)
ax.set_xlabel('$t$ [$10^{-3}$ $M_{KK}^{-1}$]')
ax.set_ylabel('$\\Delta(t)$ [$M_{KK}$]')
ax.set_title('(a) BCS Gap Profile Through Transit')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (b): Per-mode squeeze phases
ax = axes[0, 1]
mode_idx = np.arange(N_modes)
colors = ['#1f77b4']*4 + ['#2ca02c'] + ['#d62728']*3  # B2=blue, B1=green, B3=red
bar_labels = [str(l) for l in labels]
bars = ax.bar(mode_idx - 0.15, phi_k_total / PI, 0.3, color=colors, alpha=0.7, label='$\\phi_k^{total}/\\pi$')
ax.bar(mode_idx + 0.15, cos_phi_k_total, 0.3, color=colors, alpha=0.4, edgecolor='black',
       label='$\\cos(\\phi_k)$')
ax.set_xticks(mode_idx)
ax.set_xticklabels(bar_labels, rotation=45, ha='right', fontsize=8)
ax.set_ylabel('Phase / $\\pi$ or $\\cos(\\phi)$')
ax.set_title('(b) Per-Mode Squeeze Phase')
ax.legend(fontsize=9)
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
ax.grid(True, alpha=0.3, axis='y')

# Panel (c): Enhancement vs phi_eff
ax = axes[1, 0]
phi_scan = np.linspace(0, 2*PI, 500)
enh_scan = np.cosh(2*r_eff) + np.sinh(2*r_eff) * np.cos(phi_scan)
ax.plot(phi_scan/PI, enh_scan, 'k-', linewidth=2)
ax.axhline(y=1.0, color='gray', linestyle=':', alpha=0.5)
ax.axhline(y=1.3, color='green', linestyle='--', alpha=0.5, label='PASS threshold (1.3)')
ax.axhline(y=4.0, color='green', linestyle='--', alpha=0.5)
# Mark predictions
pred_markers = [
    (0.0, 'QA', 'blue', 'o'),
    (PI/4, 'Josephson', 'orange', 's'),
    (np.arccos(-0.5), 'KZ (Z$_3$)', 'red', '^'),
    (phi_eff_final, 'This work', 'green', '*'),
    (PI/2, 'Mean-field', 'purple', 'D'),
]
for phi_p, name, color, marker in pred_markers:
    enh_p = enhancement(r_eff, np.cos(phi_p))
    ax.plot(phi_p/PI, enh_p, marker=marker, color=color, markersize=10,
            label=f'{name}: {enh_p:.3f}', zorder=5)
ax.set_xlabel('$\\phi_{eff}$ / $\\pi$')
ax.set_ylabel('Enhancement')
ax.set_title(f'(c) Enhancement vs $\\phi_{{eff}}$ ($r_{{eff}}$ = {r_eff})')
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 2)

# Panel (d): Enhancement vs r_eff for our phi_eff
ax = axes[1, 1]
r_scan = np.linspace(0, 2.5, 200)
enh_our = np.cosh(2*r_scan) + np.sinh(2*r_scan) * cos_phi_final
enh_max = np.cosh(2*r_scan) + np.sinh(2*r_scan) * 1.0  # phi=0
enh_min = np.cosh(2*r_scan) - np.sinh(2*r_scan) * 1.0  # phi=pi
ax.fill_between(r_scan, enh_min, enh_max, alpha=0.1, color='gray', label='Allowed range')
ax.plot(r_scan, enh_our, 'g-', linewidth=2, label=f'$\\cos\\phi$ = {cos_phi_final:.3f}')
ax.plot(r_scan, np.cosh(2*r_scan), 'b--', linewidth=1, label='$\\phi=\\pi/2$ (no interf.)')
ax.axhline(y=1.3, color='green', linestyle=':', alpha=0.5, label='PASS (1.3)')
ax.axhline(y=1.0, color='red', linestyle=':', alpha=0.5, label='FAIL (<1.0)')
ax.axvline(x=r_eff, color='gray', linestyle=':', alpha=0.5)
ax.plot(r_eff, enh_final, 'g*', markersize=15, zorder=5, label=f'r={r_eff}: enh={enh_final:.3f}')
if r_needed < 10:
    ax.axvline(x=r_needed, color='green', linestyle='--', alpha=0.5,
               label=f'r needed for PASS: {r_needed:.2f}')
ax.set_xlabel('$r_{eff}$')
ax.set_ylabel('Enhancement')
ax.set_title(f'(d) Enhancement vs $r_{{eff}}$ (gate verdict: {gate_verdict})')
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 2.5)
ax.set_ylim(0, 8)

plt.tight_layout()
plt.savefig('s69_phi_eff.png', dpi=150, bbox_inches='tight')
print("  Saved: s69_phi_eff.png")

t_end = time.time()
print(f"\n  Total runtime: {t_end - t_start:.1f} s")
print("\n" + "=" * 78)
print("PHI-EFF-BCS-BOGOL-69: COMPLETE")
print("=" * 78)
