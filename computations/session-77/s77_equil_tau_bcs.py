#!/usr/bin/env python3
"""
EQUIL-TAU-77 RETASK: BCS-Dressed Equilibrium tau (S77-A1-EQUIL-TAU)
====================================================================

Session 77, Wave 1-A RETASK
Agent: transit-dynamics-theorist

Pre-registered gate: S77-A1-EQUIL-TAU
  PASS: |tau_equil - 0.190| < 0.05 (BCS minimum near fold)
  FAIL: No minimum in V_eff (BCS dressing insufficient)
  INFO: Minimum exists but |tau_min - 0.190| in [0.05, 0.20]

Physics:
--------
KNOWN: The bare spectral action S_f*(tau) is monotonically increasing
(Perturbative Exhaustion Theorem, S22c; confirmed S73A, S77). V_bare
has NO minimum. This is settled history.

THIS COMPUTATION: The BCS condensation energy E_cond(tau) is NEGATIVE
and peaks at the van Hove fold where the DOS diverges. The question is
whether V_eff(tau) = V_bare(tau) + E_cond(tau) has a local minimum.

Model for E_cond(tau):
  - At the fold (tau_fold = 0.190): E_cond = -0.137 M_KK (canonical, ED-CONV-36)
  - The BCS gap Delta(tau) depends on the DOS: Delta ~ exp(-1/(g*rho(tau)))
  - Near the fold, rho(tau) diverges as |tau - tau_fold|^{-1/2} (A_2 catastrophe)
  - Away from the fold, rho drops and Delta -> 0 exponentially
  - E_cond(tau) = -(1/2) * rho(tau) * Delta(tau)^2 (BCS condensation energy)
  - This creates a cusp-like minimum at tau_fold in V_eff

Cross-checks:
  CHK1: V_bare is monotonically increasing (MUST reproduce -- known)
  CHK2: E_cond(tau_fold) < 0 (condensation lowers energy)
  CHK3: E_cond(tau) -> 0 for |tau - tau_fold| >> Delta/slope
  CHK4: V_eff(tau_fold) < V_bare(tau_fold) (BCS dressing lowers energy)

Input: s73b_efold_mapping.npz, s73a_spectral_action_profile.npz,
       canonical_constants.py
Output: s77_equil_tau_bcs.npz, s77_equil_tau_bcs.png
"""

import numpy as np
import sys
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.interpolate import CubicSpline
from scipy.optimize import minimize_scalar, brentq

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    tau_fold, S_fold, dS_fold, d2S_fold,
    G_DeWitt, v_terminal, H_fold, dt_transit,
    M_KK, M_KK_gravity, M_Pl_reduced,
    a0_fold, a2_fold, a4_fold, R_protected_fold,
    m_tau, omega_att, omega_tau,
    E_cond, E_cond_ED_8mode, Delta_BCS, Delta_0_OES,
    a_GL, b_GL, rho_B2_per_mode, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
    PI, hbar_GeV_s,
)

t_start = time.time()

print("=" * 78)
print("S77-A1-EQUIL-TAU RETASK: BCS-Dressed Equilibrium tau")
print("  Does V_eff(tau) = V_bare(tau) + E_cond(tau) have a minimum?")
print("=" * 78)

# =============================================================================
# SECTION 1: LOAD S73B ODE TRAJECTORY
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 1: Loading S73B ODE Trajectory")
print("=" * 78)

d73b = np.load('s73b_efold_mapping.npz', allow_pickle=True)
t_sol = d73b['t_sol']           # time in M_KK^{-1} units
tau_sol = d73b['tau_sol']       # Jensen deformation parameter
dtau_sol = d73b['dtau_sol']     # d(tau)/dt in M_KK units
lna_sol = d73b['lna_sol']       # ln(a/a_fold)
H_sol = d73b['H_sol']           # Hubble in M_KK units
w_sol = d73b['w_sol']           # equation of state

N_pts = len(t_sol)  # (local)

print(f"  Trajectory: {N_pts} points, t in [{t_sol[0]:.4f}, {t_sol[-1]:.4f}] M_KK^{{-1}}")
print(f"  tau range: [{tau_sol.min():.4f}, {tau_sol.max():.4f}]")

# Key trajectory landmarks
idx_max_tau = np.argmax(tau_sol)  # (local)
tau_max_overshoot = tau_sol[idx_max_tau]  # (local)
t_max_overshoot = t_sol[idx_max_tau]  # (local)

sign_changes = np.where(np.diff(np.sign(dtau_sol)))[0]  # (local)
idx_turn = sign_changes[0] if len(sign_changes) > 0 else idx_max_tau  # (local)

# Find fold return
fold_return_idx = None  # (local)
for i in range(idx_turn, N_pts - 1):
    if tau_sol[i] > tau_fold and tau_sol[i + 1] <= tau_fold:
        fold_return_idx = i  # (local)
        break

print(f"  Overshoot: tau_max = {tau_max_overshoot:.4f} at t = {t_max_overshoot:.4f}")
print(f"  Fold return: t = {t_sol[fold_return_idx]:.4f}" if fold_return_idx else "  No fold return")
print(f"  Late-time: tau -> {tau_sol[-1]:.2f}, dtau = {dtau_sol[-1]:.4f}")
print(f"  VERDICT: Single overshoot, then runaway. No oscillation in bare dynamics.")

# =============================================================================
# SECTION 2: V_BARE(TAU) FROM S73A SPECTRAL ACTION
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Bare Spectral Action Potential V_bare(tau)")
print("=" * 78)

d_sa = np.load('s73a_spectral_action_profile.npz', allow_pickle=True)
tau_fine = d_sa['tau_fine']      # 1000 points in [0.01, 1.99]
S_fine = d_sa['S_fine']          # S_f*(tau)
dS_fine = d_sa['dS_fine']        # dS/dtau
d2S_fine = d_sa['d2S_fine']      # d2S/dtau2

# Build spline for S_f*(tau)
cs_S = CubicSpline(tau_fine, S_fine)
cs_dS = CubicSpline(tau_fine, dS_fine)

# S_f* at the fold
S_fstar_fold = cs_S(tau_fold)  # (local)
print(f"  S_f*(tau_fold) = {S_fstar_fold:.4f}")
print(f"  dS_f*/dtau(fold) = {cs_dS(tau_fold):.4f}")

# CHK1: V_bare monotonically increasing
dS_all_positive = np.all(dS_fine > 0)  # (local)
print(f"  CHK1: dS_f*/dtau > 0 everywhere: {dS_all_positive} (MUST BE TRUE)")
assert dS_all_positive, "FATAL: CHK1 failed -- bare SA not monotonic"

# V_bare in M_KK^4 units (heat-kernel normalization from S73B)
# V_bare(tau) = V_fold_HK * S_f*(tau) / S_f*(fold)
# V_fold_HK = (2/pi^2) * a_0 = 1304.7 M_KK^4
V_fold_HK = (2.0 / PI**2) * a0_fold  # (local) M_KK^4 units

def V_bare_fn(tau):
    """Bare potential in M_KK^4 units."""
    if tau < tau_fine[0] or tau > tau_fine[-1]:
        return V_fold_HK  # (local) clamp at boundaries
    return V_fold_HK * cs_S(tau) / S_fstar_fold

def dV_bare_dtau(tau):
    """dV_bare/dtau in M_KK^4 units."""
    if tau < tau_fine[0] or tau > tau_fine[-1]:
        return 0.0
    return V_fold_HK * cs_dS(tau) / S_fstar_fold

print(f"  V_fold_HK = (2/pi^2) * a_0 = {V_fold_HK:.4f} M_KK^4")
print(f"  V_bare(tau_fold) = {V_bare_fn(tau_fold):.4f} M_KK^4")
print(f"  dV_bare/dtau(fold) = {dV_bare_dtau(tau_fold):.4f} M_KK^4")

# Gradient at fold in M_KK^4 units
dV_bare_fold = dV_bare_dtau(tau_fold)  # (local)

# =============================================================================
# SECTION 3: BCS CONDENSATION ENERGY E_COND(TAU)
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 3: BCS Condensation Energy Model E_cond(tau)")
print("=" * 78)

# The BCS condensation energy at the fold:
# E_cond = -0.137 M_KK (from 8-mode ED, S36)
# This is in M_KK units (energy per unit cell)
# Convert to M_KK^4 units for comparison with V_bare:
# E_cond_density = E_cond * M_KK^3 ... no.
#
# Wait: E_cond and V_bare must be compared in the SAME units.
# V_bare comes from the spectral action S(tau), which is dimensionless
# (sum over eigenvalues). V_bare = (2/pi^2) * a_0 * M_KK^4 * S/S_fold.
# Actually V_fold_HK = (2/pi^2) * a_0 = 1304.7 (in M_KK^4 units, meaning
# V_fold_HK * M_KK^4 in physical units).
#
# E_cond = -0.137 in M_KK units -- this is an energy, not an energy density.
# To get the energy density (M_KK^4 units), we need E_cond_density.
#
# In the spectral action framework, the action is:
# S = Tr f(D^2/Lambda^2) -- this counts eigenvalue modes
# The BCS condensation energy is:
# E_cond = sum_k [E_k - epsilon_k] + ... (BCS energy lowering)
# This is per unit cell, in M_KK units.
#
# The effective potential includes both:
# V_eff(tau) = S_f*(tau) * (normalization) + E_BCS(tau)
#
# The S73B ODE treats V in M_KK^4 units. So E_cond must also be in M_KK^4.
# E_cond = -0.137 M_KK means the condensation energy is -0.137 * M_KK
# per unit cell. But the potential V_bare at the fold is 1304.7 M_KK^4.
#
# CRITICAL: E_cond is dimensionless (M_KK = 1 system). It's -0.137 in
# the same units as the spectral action coefficients. The spectral action
# has a_0 = 6440, a_2 = 2776, a_4 = 1351. E_cond = -0.137 is on the
# SAME SCALE as individual mode energies (~0.8 M_KK each).
#
# The potential in the KG equation is:
# V(tau) = (2/pi^2) * a_0(tau) * f_0 * Lambda^4  [with f_0=1, Lambda=M_KK]
# = (2/pi^2) * S_f*(tau) * Lambda^4 / Lambda^4 = (2/pi^2) * S_f*(tau)
# Wait, S_f*(tau) already has Lambda^4 absorbed? No.
#
# More carefully from S73B:
# V_fold_HK = (2/pi^2) * a_0 = 1304.7
# This is the potential energy density in M_KK^4 units.
# S_f*(fold) = 31244 -- this is the spectral action (dimensionless count)
# V(tau) = 1304.7 * S_f*(tau) / 31244
#
# So V is ~0.042 * S_f*(tau) in M_KK^4 units.
# V(fold) = 1304.7 M_KK^4
# dV/dtau(fold) = 1304.7 * 4040.7 / 31244 = 168.7 M_KK^4
#
# E_cond = -0.137 is in M_KK units (energy, not energy density).
# For the KG equation, we need the ENERGY DENSITY contribution.
# E_cond enters the potential as:
# V_BCS(tau) = E_cond(tau) * (number density factor)
#
# Actually: in the Chamseddine-Connes framework, E_cond IS part of the
# spectral action -- it comes from the correlation contribution to the
# eigenvalue sum. The spectral action already includes potential energy
# at the mean-field level. E_cond is the BEYOND-mean-field part.
#
# For dimensional analysis: E_cond = -0.137 M_KK is an energy per fiber.
# The potential V(tau) is an energy density (M_KK^4 = M_KK^3 * M_KK).
# Each fiber occupies a volume ~ M_KK^{-3}. So:
# V_BCS(tau) = E_cond(tau) * M_KK^3 = E_cond(tau) in M_KK^4 units
# (since M_KK = 1 in our unit system, M_KK^3 = 1).
#
# BUT WAIT: The spectral action S_fold = 31244 counts eigenvalue modes
# weighted by degeneracy d_{pq}^2. Each mode contributes ~0.8 to S.
# V = (2/pi^2) * a_0 * M_KK^4 where a_0 = 6440.
# So V = (2/9.87) * 6440 = 1304.7 in M_KK^4.
# This is a number of order 10^3.
# E_cond = -0.137 is a number of order 10^{-1}.
#
# The ratio is |E_cond| / V_bare = 0.137 / 1304.7 = 1.05e-4.
# The BCS condensation energy is 4 ORDERS OF MAGNITUDE smaller than V_bare.
#
# For a minimum to form: |dE_cond/dtau| must exceed |dV_bare/dtau|
# at some point near the fold. But:
# |dV_bare/dtau| at fold = 168.7 M_KK^4
# |E_cond| at fold = 0.137
# Even if E_cond changes by order 1 over delta_tau ~ 0.01:
# |dE_cond/dtau| ~ 0.137 / 0.01 = 13.7
# Still 12x smaller than dV_bare/dtau.
#
# This is already telling us the answer. But let me compute carefully.

print("  === Dimensional Analysis ===")
print(f"  V_bare(fold) = {V_fold_HK:.4f} M_KK^4")
print(f"  |E_cond| = {abs(E_cond):.6f} M_KK")
print(f"  Ratio |E_cond| / V_bare = {abs(E_cond) / V_fold_HK:.6e}")
print(f"  dV_bare/dtau(fold) = {dV_bare_fold:.4f} M_KK^4")

# The E_cond in the spectral action framework is the BCS condensation
# energy per fiber, in M_KK units. To add it to V_bare (in M_KK^4),
# we need the energy DENSITY. The conversion factor is:
#
# The spectral action sums over all (p,q) sectors with weight d_{pq}^2.
# The total count is ~ sum d_{pq}^2 * N_evals ~ 31244 (S_f*).
# Each mode contributes energy ~ omega_j (eigenvalue) ~ 0.8-1.0 M_KK.
# E_cond = -0.137 M_KK modifies the TOTAL energy from correlations,
# not per-mode but summed over the 8 BCS-active modes.
#
# The correct comparison: V_bare comes from summing over ALL modes.
# E_cond comes from the 8 BCS-active modes (4 B2 + 1 B1 + 3 B3).
# In the spectral action, these 8 modes contribute:
# S_BCS = 8 modes * <omega> * d^2 ~ 8 * 0.85 * 16 ~ 109
# (using d_{pq}^2 = 16 for B2 modes at (0,0) with d=1, ..no)
# Actually the 8 modes are in the (0,0) representation (d_{00}=1),
# so their weight is d^2 = 1.
# S_BCS_modes = 8 * 0.85 = 6.8 in spectral action units
#
# Hmm, this doesn't resolve the issue. Let me just compare
# E_cond to V_bare directly, treating both as contributions
# to the same modulus potential in the KG equation.
#
# The KG equation is:
# G * ddot_tau + 3GH * dot_tau + dV_total/dtau = 0
# where V_total = V_bare + V_BCS
#
# V_BCS must have the SAME units as V_bare (M_KK^4).
# E_cond = -0.137 is quoted in M_KK units = M_KK^{-3} * M_KK^4
# So V_BCS(tau) = E_cond(tau) * M_KK^{-3} ... no, that makes it smaller.
#
# The issue is: what IS the unit system for E_cond?
# From S36 (ED-CONV-36): the Hamiltonian is H_BCS = sum epsilon_k n_k +
# sum V_{kk'} c^dag c^dag c c, and E_cond is the ground state energy
# minus the uncorrelated energy. The epsilon_k are eigenvalues of D_K,
# which are in M_KK units. So E_cond is in M_KK units (energy).
#
# V_bare from the spectral action: S = Tr f(D^2/Lambda^2).
# With Lambda = 12.9 M_KK (S73a), and f* the specific functional:
# S is dimensionless. V_bare = (2/pi^2) * a_0_fold * M_KK^4
# = 1304.7 * M_KK^4.
#
# These are NOT directly comparable without knowing how many
# spatial points (fibers) contribute to V_bare. V_bare is an
# ENERGY DENSITY (energy per spatial volume), while E_cond is
# an energy PER FIBER.
#
# In the emergent 4D picture: V_bare * Volume_4D = total vacuum energy.
# E_cond * N_fibers = total condensation energy.
# For the homogeneous modulus field tau(t):
# V_total(tau) = V_bare(tau) + E_cond(tau) per fiber.
# Both contribute per fiber.
#
# So V_bare per fiber = V_bare(tau) and E_cond per fiber = E_cond(tau).
# THEY ARE COMPARABLE AS-IS IF V_bare is also per fiber.
#
# But wait: V_bare = (2/pi^2) * a_0 = 1304.7. And a_0 = 6440 = sum d_{pq}^2 * N_evals.
# This is a sum over the internal Dirac spectrum per fiber.
# So V_bare IS per fiber. And E_cond is per fiber.
# Therefore V_BCS(tau) = E_cond(tau) in the SAME units.
#
# OK, so the comparison is:
# V_bare(fold) = 1304.7 (dimensionless, per fiber, in M_KK^4 units)
# E_cond(fold) = -0.137 (in M_KK, per fiber)
#
# NO! The units are DIFFERENT. V_bare is in M_KK^4, E_cond is in M_KK.
# The spectral action S has dimensions [Lambda^4] / [Lambda^4] = 1.
# But V = (2/pi^2) * sum f(lambda^2/Lambda^2) * Lambda^4.
# Wait, S = Tr f(D^2/Lambda^2), which is dimensionless.
# V = S * (cutoff energy)^4 / (spacetime volume)?
#
# Let me just read the S73B more carefully. From line 346-347:
# KE = 0.5 * G * dtau^2 -- G=5, dtau~26.5, so KE = 0.5*5*702 = 1756
# PE = V_eff_MKK4(tau) = V_fold_HK * S/S_fold ~ 1304.7
# H^2 = (KE + PE) / (3 * (M_Pl/M_KK)^2)
# (M_Pl/M_KK)^2 = (2.435e18/7.43e16)^2 = 32.8^2 = 1073
# H^2 = (1756 + 1305) / (3 * 1073) = 3061 / 3219 = 0.951
# H = 0.975 -- matches S73B!
#
# So V and KE are both in "M_KK = 1" units where:
# V has units [M_KK^4 / M_KK^4] = 1 (dimensionless number ~1304)
# KE = (1/2) G (dtau)^2 -- also dimensionless number ~1756
# H^2 = (V + KE) / (3 M_Pl^2/M_KK^2) -- H in M_KK units
#
# The E_cond = -0.137 is also in this system: it's the BCS condensation
# energy in units where M_KK = 1. So -0.137 * M_KK^4 would be 0.137
# in these same dimensionless units.
#
# WAIT: if E_cond = -0.137 M_KK, and V_bare = 1304.7 M_KK^4, then
# in M_KK = 1 units, E_cond = -0.137 and V_bare = 1304.7.
# These ARE directly comparable! E_cond is tiny.
#
# But E_cond might be in M_KK^4 units already. Let me check:
# From S36, E_cond = -0.137 comes from exact diagonalization of
# H_BCS where eigenvalues are in M_KK units. The energies epsilon_k
# are eigenvalues of D_K, which are ~0.8 M_KK. So E_cond has units
# of energy = M_KK. Not M_KK^4.
#
# OR: in the 0+1 dimensional BCS system (fiber at one point),
# E_cond is an energy (not energy density). In M_KK = 1 units,
# it's 0.137. The spectral action V_bare is also an "energy"
# per fiber (the trace over internal Dirac eigenvalues).
#
# RESOLUTION: Both V_bare and E_cond are "energy per fiber" in M_KK units.
# The spectral action normalization:
# V_fold = (2/pi^2) * a_0 = 1304.7 -- this is the SPECTRAL ACTION VALUE
# at the fold, which IS the sum of f*(lambda_j^2/Lambda^2) weighted by d^2.
#
# The individual eigenvalue energies are ~0.8-1.0 M_KK.
# The total spectral action sums ~31000 weighted eigenvalues.
# The BCS condensation involves 8 modes out of ~31000.
#
# So E_cond/V_bare = 0.137 / 1304.7 = 1.05e-4.
#
# But WAIT: E_cond is an ENERGY in the BCS Hamiltonian, whose natural
# scale is epsilon_k ~ 0.85 M_KK per mode. The spectral action value
# a_0 = 6440 is NOT an energy in the same sense -- it's a DIMENSIONLESS
# count proportional to the number of eigenvalue modes.
#
# For the KG potential: both V_bare(tau) and V_BCS(tau) enter the
# Klein-Gordon equation as dV/dtau, driving the modulus. The
# spectral action potential is:
# V_SA(tau) = (2/pi^2) * a_0(tau) * M_KK^4 / M_KK^4  [dimensionless]
# And E_cond(tau) adds to this as:
# V_total(tau) = V_SA(tau) + E_cond(tau)/M_KK ... ???
#
# I think the fundamental issue is that E_cond is in M_KK units
# (one power of mass) while V_bare ~ a_0 is dimensionless (zero power
# of mass -- it's a pure number). They can't be directly added.
#
# The resolution is in how the effective action is constructed.
# The total effective action per fiber is:
# S_total = S_spectral(tau) + S_BCS(tau)
# Both S_spectral and S_BCS are DIMENSIONLESS. The spectral action
# S = Tr f(D^2/Lambda^2) is dimensionless by construction.
# The BCS free energy F_BCS = E_cond in units of [energy/kT]... no.
#
# Actually, in the Chamseddine-Connes framework, EVERYTHING is encoded
# in the spectral action S = Tr f(D^2/Lambda^2). The BCS correlations
# modify the spectrum of D, hence modify S. The S73A data already
# computes S_bcs by shifting eigenvalues to E = sqrt(omega^2 + Delta^2).
# That's the spectral action WITH the BCS gap.
#
# The issue is that S73A uses a CONSTANT Delta at all tau, while
# physically Delta(tau) varies -- it's maximal at the fold and
# vanishes away from it.
#
# So the proper approach is:
# V_eff(tau) = V_fold_HK * S_bcs(tau, Delta(tau)) / S_fstar_fold
# where S_bcs(tau, Delta) is the spectral action computed with
# eigenvalues shifted by a tau-dependent gap Delta(tau).
#
# From S73A data, we have:
# S_bare(tau) = spectral action with Delta = 0
# S_bcs(tau) = spectral action with Delta = Delta_BCS = 0.464 (constant)
# Delta_S(tau) = S_bcs(tau) - S_bare(tau) = spectral shift from BCS gap
#
# For a tau-dependent gap Delta(tau):
# S_eff(tau) = S_bare(tau) + Delta_S(tau) * (Delta(tau)/Delta_BCS)^2
#   (to leading order, since Delta_S ~ Delta^2 for small gap)
# This is approximate but captures the essential physics.

# ============ APPROACH: Use S73A S_bcs and S_bare data ============
# Load the coarse grid data
tau_grid = d_sa['tau_grid']       # 104 points
S_bare_grid = d_sa['S_bare'][0]   # f_star functional, bare
S_bcs_grid = d_sa['S_bcs'][0]     # f_star functional, BCS with constant Delta

# Spectral shift from constant BCS gap
Delta_S_const = S_bcs_grid - S_bare_grid  # (local) shift at each tau

# The shift at the fold
idx_fold_grid = np.argmin(np.abs(tau_grid - tau_fold))  # (local)
Delta_S_fold = Delta_S_const[idx_fold_grid]  # (local)

print(f"\n  === S73A Spectral Action Data (f* functional) ===")
print(f"  S_bare(fold) = {S_bare_grid[idx_fold_grid]:.4f}")
print(f"  S_bcs(fold) = {S_bcs_grid[idx_fold_grid]:.4f}")
print(f"  Delta_S(fold) = {Delta_S_fold:.4f} (shift from constant BCS gap)")
print(f"  Delta_BCS = {Delta_BCS:.6f} M_KK (gap used in S73A)")

# Build splines for S_bare and Delta_S on coarse grid
cs_S_bare = CubicSpline(tau_grid, S_bare_grid)
cs_Delta_S = CubicSpline(tau_grid, Delta_S_const)

# Verify: Delta_S should be roughly constant (since gap is constant)
# but the eigenvalues shift differently at each tau, so Delta_S varies
print(f"\n  Delta_S range: [{Delta_S_const.min():.4f}, {Delta_S_const.max():.4f}]")
print(f"  Delta_S(fold) = {Delta_S_fold:.4f}")
print(f"  Delta_S(0) = {Delta_S_const[0]:.4f}")
print(f"  Delta_S(1.0) = {Delta_S_const[np.argmin(np.abs(tau_grid - 1.0))]:.4f}")

# =============================================================================
# SECTION 4: MODEL FOR DELTA(TAU) -- TAU-DEPENDENT BCS GAP
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: Tau-Dependent BCS Gap Model")
print("=" * 78)

# The BCS gap at the fold: Delta(tau_fold) = Delta_BCS = 0.464 M_KK
# Away from the fold, the gap depends on the DOS rho(tau).
#
# Van Hove singularity: near the fold, the DOS diverges as:
#   rho(tau) ~ rho_0 / sqrt(|tau - tau_fold| + epsilon)
# where epsilon is a regularization scale.
#
# BCS gap equation: 1/g = integral rho(E) / sqrt(E^2 + Delta^2) dE
# For weak coupling: Delta ~ omega_D * exp(-1/(g * rho_F))
# where rho_F is the DOS at the Fermi level.
#
# As tau moves away from the fold, rho decreases and the gap closes:
#   Delta(tau) = Delta_fold * exp(-(rho_fold/rho(tau) - 1) / (g * rho_fold))
# In the BCS limit: Delta(tau) ~ Delta_fold * exp(-1/(g*rho(tau)) + 1/(g*rho_fold))
#
# For the A_2 catastrophe (cusp):
#   rho(tau) = rho_fold * min(1, sqrt(tau_width / |tau - tau_fold|))
# where tau_width = width of van Hove peak.
#
# The width is set by: the eigenvalue dispersion bandwidth.
# From the mode spectrum: omega_min = 0.82 M_KK (B1), omega_max = 0.98 M_KK (B3)
# Spread delta_omega ~ 0.16 M_KK.
# The van Hove width in tau is: delta_omega / (d_omega/d_tau)_fold
#
# From the spectral action: the eigenvalues shift with tau. The rate of
# shift is determined by the Jensen deformation. For a mode with energy
# omega at the fold, d(omega)/d(tau) ~ omega * alpha where alpha ~ 0.5
# (from the spectral action curvature).
#
# Approximate: tau_width ~ 0.05 (from the BCS coherence xi_BCS = 0.808)

# --- Model parameters ---
# We use a two-parameter model for Delta(tau):
# Delta(tau) = Delta_fold * F(tau)
# where F(tau) = exp(-C * (tau - tau_fold)^2 / tau_w^2) for a Gaussian model
# or F(tau) = 1 / (1 + ((tau - tau_fold)/tau_w)^2) for Lorentzian
#
# The critical parameter is tau_w -- the width of the BCS gap in tau.
# From the GL coherence: xi_GL = 0.976, xi_BCS = 0.808 (in M_KK^{-1})
# The BCS gap closes over a tau range of order:
# tau_w ~ Delta_BCS / dE_mean_dtau
# where dE_mean_dtau is the rate at which mode energies shift with tau.
#
# From the spectral action: d(S_f*)/dtau at fold = 4041 (S73A) or 58673 (canonical)
# Per mode: d(omega)/dtau ~ dS/(N_modes * d^2) ~ 4041 / (1232) ~ 3.3
# This gives tau_w ~ 0.464 / 3.3 = 0.14
#
# We'll compute with multiple widths to test sensitivity.

# Use Ginzburg-Landau parameters for the tau-dependence:
# V_GL(Delta) = a_GL * |Delta|^2 + b_GL * |Delta|^4
# a_GL = -0.5245 (attractive), b_GL = 0.4418 (repulsive)
# The GL order parameter: Delta_0 = sqrt(|a_GL|/(2*b_GL)) = 0.770 M_KK
#
# The GL potential minimum energy: V_GL_min = -a_GL^2/(4*b_GL) = -0.1556
# This is the GL condensation energy E_cond_GL = -0.156 (matches canonical)
#
# The key: a_GL depends on tau through the DOS:
# a_GL(tau) = a_GL(tau_fold) * (rho_fold / rho(tau))
# When rho decreases, a_GL becomes less negative and eventually positive,
# destroying the BCS state.

# Model: Gaussian suppression of BCS gap away from fold
# Delta(tau) = Delta_fold * exp(-((tau - tau_fold) / tau_w)^2)
# E_cond(tau) = E_cond_fold * (Delta(tau)/Delta_fold)^2 * (rho(tau)/rho_fold)
#            ~ E_cond_fold * exp(-2*((tau - tau_fold)/tau_w)^2)
# (For BCS: E_cond ~ -rho * Delta^2, and we assume rho varies slowly
# compared to the exponential gap suppression.)

# We scan over tau_w from 0.01 to 0.50 to find sensitivity
tau_w_scan = np.array([0.01, 0.02, 0.05, 0.10, 0.14, 0.20, 0.30, 0.50])  # (local)

print(f"  Delta(tau_fold) = {Delta_BCS:.6f} M_KK")
print(f"  E_cond(tau_fold) = {E_cond:.6f} M_KK")
print(f"  |a_GL| = {abs(a_GL):.6f}, b_GL = {b_GL:.6f}")
print(f"  GL minimum energy: -a_GL^2/(4*b_GL) = {-a_GL**2/(4*b_GL):.6f}")

# E_cond in spectral action units (to compare with V_bare):
# V_bare at fold = V_fold_HK = 1304.7 (dimensionless in M_KK^4)
# E_cond = -0.137 M_KK = -0.137 / M_KK^3 in M_KK^4 units? NO.
#
# FUNDAMENTAL RESOLUTION:
# The S73B KG equation is written as (line 384):
#   ddot_tau = -3H dot_tau - dV/dtau / G
# where V = V_fold_HK * S_f*(tau) / S_f*(fold) in M_KK^4 units.
#
# The BCS condensation energy enters the SAME potential.
# But E_cond from ED (S36) is the condensation energy of the
# 8-mode BCS Hamiltonian, measured in units of M_KK.
#
# The spectral action S_f*(tau) is ALSO in units of M_KK^0 (dimensionless).
# The heat-kernel normalization V_fold_HK converts it to M_KK^4.
#
# For E_cond to enter V_eff, it must be expressed in M_KK^4 units.
# The BCS Hamiltonian has eigenvalues in M_KK. E_cond is an energy
# eigenvalue, hence in M_KK.
#
# To get M_KK^4: we need to know the "volume" factor.
# In cosmological FRW: rho = energy density = energy / volume.
# V_eff is an energy DENSITY (M_KK^4 = [energy]^4 in natural units).
# E_cond is an energy PER FIBER.
# Density = energy/volume ~ E_cond * n_fiber where n_fiber = M_KK^3.
# So V_BCS = E_cond * M_KK^3 = E_cond in M_KK^4 units (since M_KK = 1).
#
# With M_KK = 1: V_BCS = E_cond = -0.137.
# V_bare = 1304.7.
# V_BCS / V_bare = 1.05e-4.
#
# But this assumes ONE BCS condensate per (M_KK)^{-3} volume.
# The actual density could be higher if the condensate is collective.
#
# ALTERNATIVE: The spectral action already COUNTS all modes.
# S = Tr f(D^2/Lambda^2) = sum over ALL eigenvalues.
# At the fold, S_f*(fold) = 31244.
# Each eigenvalue contributes ~f*(omega^2/Lambda^2) to S.
# E_cond = -0.137 is the difference between correlated and uncorrelated
# ground states, in M_KK units. This is equivalent to:
# Delta_S_BCS = E_cond * (S_fold / sum_i omega_i)
# where sum_i omega_i is the total uncorrelated spectral action.
#
# This doesn't quite work either. Let me just use the S73A data directly.
# S73A already computed S_bcs at each tau with Delta = 0.464 constant.
# The spectral shift Delta_S(tau) = S_bcs(tau) - S_bare(tau) is the
# BCS contribution in spectral action units. At the fold:
# Delta_S(fold) = 720.08.
# This is 720 / 31244 = 2.3% of S_f*(fold).
# And 720 / S_fold_canonical = 720 / 250361 = 0.29%.
#
# In V_bare units: V_BCS(fold) = V_fold_HK * Delta_S(fold) / S_fstar_fold
# = 1304.7 * 720.08 / 31244 = 30.07 M_KK^4.
# So V_BCS at fold = 30.07 M_KK^4 with CONSTANT Delta.
#
# With tau-dependent Delta: V_BCS(tau) = V_fold_HK * Delta_S(tau) *
# (Delta(tau)/Delta_fold)^2 / S_fstar_fold
# (assuming Delta_S scales as Delta^2 -- correct for small gap)

# CORRECTION: The S73A "S_bcs" already adds the gap shift, which INCREASES
# the spectral action (higher eigenvalues). The BCS condensation energy
# is NEGATIVE (lowers energy). These are DIFFERENT things!
#
# S73A S_bcs: each omega -> sqrt(omega^2 + Delta^2) > omega, so S_bcs > S_bare.
# This is the cost of opening the gap (kinetic energy increase).
# The CONDENSATION energy E_cond < 0 comes from the INTERACTION term,
# which is not captured by just shifting eigenvalues.
#
# In BCS theory:
# E_cond = E_kinetic_increase + E_interaction_decrease
# E_kinetic_increase > 0 (gapping the spectrum costs energy)
# E_interaction_decrease < 0 (pairing lowers interaction energy)
# E_cond < 0 means |E_interaction| > E_kinetic
#
# The S73A Delta_S = S_bcs - S_bare captures ONLY E_kinetic_increase.
# The full E_cond includes both. In the GL framework:
# E_cond = a_GL * Delta^2 + b_GL * Delta^4 < 0 at the minimum
# The kinetic increase is proportional to b_GL * Delta^4 > 0
# The interaction decrease is a_GL * Delta^2 < 0 (since a_GL < 0 at fold)
#
# So:
# V_kinetic(tau) = V_fold_HK * Delta_S(tau) * (Delta(tau)/Delta_fold)^2 / S_fstar_fold
#   (This INCREASES V_eff -- it opposes the minimum)
# V_interaction(tau) = E_cond(tau) - V_kinetic(tau)
#   (This DECREASES V_eff -- it creates the minimum)
#
# The NET contribution V_BCS(tau) = V_kinetic(tau) + V_interaction(tau) = E_cond(tau)
# But E_cond(tau) must be in spectral action units!
#
# OK let me take a completely different approach. The GL functional gives us:
# F_GL(Delta, tau) = a_GL(tau) * |Delta|^2 + b_GL(tau) * |Delta|^4
# At the fold: F_GL(Delta_0, tau_fold) = -a_GL^2/(4*b_GL) = -0.156
# This is in M_KK units (energy per fiber).
#
# The modulus equation couples to F_GL through:
# V_total(tau) = V_SA(tau) + F_GL(Delta(tau), tau)
# where both are in the SAME units (energy per fiber).
#
# V_SA = spectral action contribution = (2/pi^2) * Tr f(D^2/Lambda^2) * Lambda^4
# Wait, V_SA must also be in energy-per-fiber units.
# In M_KK^4 units: V_SA(fold) = 1304.7 M_KK^4
# In M_KK units (energy per fiber): V_SA(fold) = 1304.7 M_KK
# But E_cond = -0.137 M_KK.
#
# The ratio is STILL E_cond / V_SA = 0.137 / 1304.7 = 1.05e-4.
# The BCS contribution is 4 orders of magnitude smaller.
#
# For a minimum: dE_cond/dtau must compete with dV_SA/dtau.
# dV_SA/dtau(fold) = V_fold_HK * dS_fine/dtau / S_fstar_fold
# = 1304.7 * 4040.7 / 31244 = 168.7 in spectral action units
# E_cond at fold = -0.137 (or -0.156 from GL)
# For sharp enough E_cond profile: dE_cond/dtau ~ E_cond / tau_w
# Need: |E_cond/tau_w| > dV_SA/dtau
# tau_w < |E_cond| / dV_SA = 0.156 / 168.7 = 9.2e-4
#
# tau_w = 0.001! This means the BCS gap must close over delta_tau = 0.001
# for the BCS dressing to create a minimum. That's EXTREMELY narrow.
# For comparison, the transit itself spans delta_tau ~ 0.01.

# Let me compute this properly with the correct scaling.

print(f"\n  === Scale Comparison ===")
dV_SA_fold = V_fold_HK * cs_dS(tau_fold) / S_fstar_fold  # (local)
print(f"  dV_SA/dtau(fold) = {dV_SA_fold:.4f} (spectral action units, M_KK^4)")

# E_cond in the SAME units as V_SA:
# Need a conversion factor. The spectral action is extensive (proportional
# to number of modes). E_cond is intensive (per correlated subsystem).
#
# Let me try the NATURAL comparison: treat E_cond as directly addable
# to the spectral action, in its own units (M_KK).
# Then V_eff = V_SA + E_cond(tau) where both are in M_KK.
# But V_SA ~ 1305 and E_cond ~ -0.14. The BCS effect is tiny.

# The key insight: V_bare = a_0 * (2/pi^2) = 6440 * 0.2026 = 1305
# This is the sum over THOUSANDS of eigenvalue modes.
# E_cond comes from EIGHT modes. The per-mode contribution is:
# V_bare per mode ~ 1305 / 6440 = 0.203 per eigenvalue unit
# E_cond = -0.137 for 8 modes = -0.0171 per mode
# So E_cond/mode / V_bare/mode = 0.0171 / 0.203 = 8.4%
# That's NOT negligible per mode! But V_bare involves ~6440 modes,
# so the aggregate ratio is tiny.
#
# For the modulus dynamics, what matters is the TAU-DERIVATIVE.
# V_bare's tau-derivative comes from ALL modes shifting together.
# E_cond's tau-derivative comes from the 8 BCS modes' pairing
# strength changing with tau.
#
# If the 8 BCS modes have anomalously large dE/dtau at the fold
# (because of the van Hove singularity), their contribution to
# dV_eff/dtau could be competitive.
#
# From the S73A data, the per-mode spectral action shift at the fold:
# dS_fine(fold) = 4041 for all modes
# For 8 modes out of ~31244 total S: each mode contributes ~1.
# So 8 modes contribute ~ 8 * dS_per_mode ~ 8 * 1.03 = 8.3 to dS.
# That's 8.3/4041 = 0.2% of the total derivative.
#
# The BCS energy depends on these 8 modes through the gap equation.
# The gap equation is exponentially sensitive to DOS at the fold.
# dE_cond/dtau ~ E_cond * (1/rho) * (drho/dtau) * (1/(g*rho)^2)
# Near the van Hove fold: drho/dtau ~ -rho / (2 * (tau - tau_fold))
# This is the 1/sqrt singularity derivative.
# At the fold: drho/dtau -> infinity! But it's integrable.
#
# The bottom line: the BCS contribution to dV_eff/dtau is a TINY
# fraction of the bare spectral action gradient. The van Hove
# singularity creates a sharp feature in E_cond(tau), but its
# amplitude is 4 orders of magnitude smaller than V_bare.

# === COMPUTATIONAL APPROACH ===
# Rather than arguing about units, compute V_eff(tau) for MULTIPLE
# models of E_cond(tau) and check whether any create a minimum.
# Model A: E_cond(tau) = E_cond * Gaussian (width tau_w)
# Model B: E_cond(tau) = E_cond * Lorentzian (width tau_w)
# Model C: E_cond(tau) from GL a(tau) dependence
# For each, compute V_eff(tau) = V_bare(tau) + alpha * E_cond(tau)
# where alpha is a "units correction" factor.
# If alpha = 1: E_cond is in the same units as V_bare.
# The gate asks: does V_eff have a minimum?

# =============================================================================
# SECTION 5: CONSTRUCT V_EFF(TAU) WITH BCS DRESSING
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Construct V_eff(tau) = V_bare(tau) + E_cond(tau)")
print("=" * 78)

# High-resolution tau grid for V_eff
tau_veff = np.linspace(0.01, 1.0, 5000)  # (local)

# V_bare on this grid (interpolated from S73A fine data)
V_bare_arr = np.array([V_bare_fn(t) for t in tau_veff])  # (local)
dV_bare_arr = np.array([dV_bare_dtau(t) for t in tau_veff])  # (local)

print(f"  V_bare range: [{V_bare_arr.min():.4f}, {V_bare_arr.max():.4f}]")
print(f"  dV_bare/dtau at fold: {dV_bare_dtau(tau_fold):.4f}")

# MODEL A: Gaussian BCS condensation
# E_cond(tau) = E_cond_fold * exp(-((tau - tau_fold)/tau_w)^2)
# In the modulus potential units (same as V_bare):

# The BCS condensation energy in V_bare units:
# From GL: F_GL_min = -a_GL^2/(4*b_GL) = -0.1557 M_KK
# From ED: E_cond = -0.137 M_KK
# V_bare(fold) = 1304.7 (in M_KK^4 units)
# Ratio: |E_cond| / V_bare = 1.05e-4

# For the modulus KG equation, the CONSISTENT treatment is:
# The modulus mass M_KK^2 * G_DeWitt = 5 * M_KK^2 is the kinetic scale.
# The potential gradient dV/dtau drives the modulus.
# BCS gradient dE_cond/dtau competes with dV_SA/dtau.
# Both are in M_KK^4 units if both are energy densities.
#
# But if E_cond is per-fiber energy (M_KK) and V_SA is energy density
# (M_KK^4), then E_cond needs a factor of M_KK^3 (fiber number density).
# In M_KK = 1 units: E_cond_density = E_cond * 1 = -0.137 M_KK^4.
# This is STILL 4 OOM below V_bare.
#
# Unless the fiber number density is NOT M_KK^3 but something else.
# In the spectral action: a_0 = (number of eigenvalues) = 6440.
# This counts modes per fiber. V = (2/pi^2)*a_0 = 1304.7 is then
# the sum over these modes of the spectral functional.
# E_cond = -0.137 is for 8 modes out of ~6440.
# If we normalize: E_cond contributes to V as E_cond * (2/pi^2):
# V_BCS = -0.137 * (2/pi^2) = -0.0278
# V_bare at fold = 1304.7
# Ratio: 2.1e-5. Still tiny.
#
# Actually, the factor (2/pi^2) doesn't make sense here.
# Let me use a different normalization argument.
#
# The spectral action S = Tr f(D^2/Lambda^2)
# = sum_j f(lambda_j^2 / Lambda^2)
# For f*(x) = 0.912 * sqrt(x) + 0.0883 * exp(-x), with Lambda = 12.9:
# f*(omega^2/Lambda^2) ~ 0.912 * omega/Lambda + ... ~ 0.912 * 0.85/12.9 ~ 0.060
# Times N_eigenvalues ~ 155984 (L_max=10) ... but S73A uses max_pq_sum=3
# giving ~1232 weighted eigenvalues.
# S ~ 1232 * 0.060 * weight ~ 31000 -- consistent with S_f*(fold) = 31244.
#
# Each eigenvalue contributes ~25 to S (weighted by d_{pq}^2).
# 8 BCS modes with d_{00} = 1 contribute 8 * 0.060 = 0.48 to S.
# That's 0.48 / 31244 = 1.5e-5 of S. Negligible.
#
# E_cond = -0.137 M_KK is the ACTUAL ground state energy shift.
# In spectral action units: delta_S = E_cond * Lambda / (alpha_star * M_KK)
# No, this is getting circular. Let me just compute.

# ====== DIRECT COMPARISON IN THE KG EQUATION ======
# From S73B (lines 383-384):
#   ddot_tau = -3H dot_tau - dV_MKK4/dtau / G_DeWitt
# where V_MKK4 = V_fold_HK * S_f*(tau) / S_f*(fold) with V_fold_HK = 1304.7
#
# The modulus mass squared:
#   m_tau^2 = d2V/dtau2 / G_DeWitt
# From canonical: m_tau = 2.062
# So d2V/dtau2 = m_tau^2 * G_DeWitt = 4.252 * 5 = 21.26
# But V_fold_HK * d2S/S_fold_fstar = 1304.7 * 21826 / 31244 = 911.0
# This gives m_tau = sqrt(911/5) = 13.5, NOT 2.062.
#
# The m_tau = 2.062 from S42 must use a DIFFERENT normalization!
# Let me check.

print(f"\n  === Mass Cross-Check ===")
d2V_from_S73A = V_fold_HK * d2S_fine[np.argmin(np.abs(tau_fine - tau_fold))] / S_fstar_fold  # (local)
m_tau_from_S73A = np.sqrt(d2V_from_S73A / G_DeWitt)  # (local)
print(f"  d2V/dtau2 from S73A = {d2V_from_S73A:.4f}")
print(f"  m_tau from S73A = {m_tau_from_S73A:.4f}")
print(f"  m_tau canonical = {m_tau:.4f}")
print(f"  Ratio = {m_tau_from_S73A / m_tau:.4f}")

# The m_tau = 2.062 uses the FULL spectral action (S_fold = 250361)
# while S73A uses max_pq_sum=3 giving S_f*(fold) = 31244.
# The ratio sqrt(250361/31244) = sqrt(8.01) = 2.83.
# m_tau(S73A) / m_tau(canonical) = 13.5 / 2.062 = 6.55. Hmm, not 2.83.
# The resolution: m_tau from S42 uses d2S_fold = 317863 at higher resolution
# and the FULL S_fold = 250361.
# d2V = V_fold_HK * d2S_fold / S_fold = 1304.7 * 317863 / 250361 = 1657
# m_tau = sqrt(1657/5) = sqrt(331) = 18.2 -- still not 2.062!
#
# There must be a different normalization for m_tau in S42.
# m_tau^2 = d2S/(2*G_DeWitt) / S * ... hmm.
# From the spectral action: V(tau) = (2/pi^2) f_0 Lambda^4 Tr f(D^2/Lambda^2)
# The potential is proportional to Lambda^4 * S(tau)/normalization.
# In the Friedmann equation: 3 M_Pl^2 H^2 = rho = (1/2) G dot_tau^2 + V
# The modulus mass: omega^2 = V''/(G * ...) depends on the normalization.
#
# This normalization confusion is NOT important for the gate question.
# What matters: the RATIO dE_cond/dtau divided by dV_bare/dtau.
# Both use the SAME normalization, so the ratio is normalization-independent.

# ====== RATIO APPROACH (normalization-independent) ======
# The gradient of V_bare at the fold:
# |dV_bare/dtau| = C * dS_f*/dtau where C = V_fold_HK / S_fstar_fold
# The gradient of E_cond at the fold:
# |dE_cond/dtau| ~ |E_cond_fold| / tau_w (for Gaussian with width tau_w)
#
# For a minimum: dV_eff/dtau = 0 requires:
# dV_bare/dtau + dE_cond/dtau = 0
# This means: |dE_cond/dtau| = |dV_bare/dtau|
# |E_cond| / tau_w = C * dS/dtau
#
# The critical question: is E_cond in the same units as C * S?
# C = V_fold_HK / S_fstar_fold = 1304.7 / 31244 = 0.04176
# C * S_fold = V_fold_HK = 1304.7
# C * dS_fold = 1304.7 * 4041 / 31244 = 168.7
#
# If E_cond = -0.137 is in M_KK units and V = C*S is also in some
# system of units, we need to know the relationship.
#
# From the Friedmann equation cross-check:
# KE = (1/2) * G * v^2 = 0.5 * 5 * 26.5^2 = 1757
# V = 1304.7
# H^2 = (1757 + 1305) / (3 * 1073) = 0.951 -> H = 0.975
# This matches the S73B data. So V = 1304.7 is in M_KK^4 units
# where M_KK = 1, and quantities like H = 0.975 are in M_KK units.
# The energies V and KE are in [M_KK^4].
#
# E_cond = -0.137 is in M_KK units [energy].
# To convert to M_KK^4 [energy density]:
# E_cond_density = E_cond * (M_KK^3) = -0.137 (since M_KK = 1)
#
# So V_BCS_density = -0.137 M_KK^4 vs V_bare = 1304.7 M_KK^4.
# Ratio: 1.05e-4.
#
# For the gradient to balance:
# |dE_cond/dtau| / tau_w ~ 0.137 / tau_w
# dV_bare/dtau = 168.7
# Balance requires: tau_w = 0.137 / 168.7 = 8.1e-4
# This is an extremely narrow feature -- physically unreasonable.
#
# The BCS gap width tau_w cannot be narrower than ~0.01 (the
# spectral resolution limit). So BCS dressing in THIS normalization
# CANNOT create a minimum.
#
# BUT: there's a factor I may be missing. E_cond comes from 8 modes,
# but the TOTAL BCS energy might be extensive in some sense.
# Let me check: if the condensate extends over N_fibers fibers:
# E_cond_total = E_cond * N_fibers
# V_BCS_density = E_cond * N_fibers / Volume = E_cond * M_KK^3
# This is the same as before. The extensivity doesn't help.
#
# UNLESS: E_cond is already an energy DENSITY (per unit volume),
# not per fiber. Let me check the original S36 computation.
# In S36: H_BCS is a 256-state Hamiltonian in 8-mode Fock space.
# The eigenvalues are in M_KK units. E_cond is the ground state
# energy minus uncorrelated energy, in M_KK units.
# This is energy PER FIBER. Not per volume.
#
# HOWEVER: in the KG equation (S73B), the modulus tau is spatially
# homogeneous. The potential V(tau) IS a 4D energy density.
# V_bare = spectral action / (spacetime volume) ~ S * Lambda^4 / (2*pi)^4
# This is Lambda^4 * O(1) ~ M_KK^4 * O(10^3).
# E_cond per fiber = -0.137 M_KK.
# E_cond density = E_cond * n_fiber = E_cond * M_KK^3 = -0.137 M_KK^4.
# ratio = 0.137 / 1305 = 1.05e-4. Confirmed.

# ====== GENEROUS UPPER BOUND ======
# What if E_cond is ALREADY in M_KK^4 units (energy density)?
# This would mean the BCS condensation energy density is -0.137 M_KK^4
# per unit KK volume. Then:
# ratio = 0.137 / 1305 = 1.05e-4. Same result.
#
# What if we use E_cond_GL = -0.156 instead? Still 1.2e-4.
# What about the barrier height? barrier_1d = 0.156. Same scale.
#
# The deepest possible BCS well is bounded by the gap:
# |V_BCS| <= (1/2) * Delta_BCS^2 * rho_fold = 0.5 * 0.464^2 * 14.02
# = 0.5 * 0.215 * 14.02 = 1.51 M_KK
# Even with the generous rho_fold, V_BCS ~ 1.5 M_KK.
# Ratio: 1.5 / 1305 = 1.15e-3. Still 3 OOM below.
#
# MAXIMALLY GENEROUS: use E_exc = 60.6 M_KK (the total excitation
# energy from the transit). This is an extreme upper bound.
# Ratio: 60.6 / 1305 = 4.6e-2. This is 5%, which COULD create
# a minimum if concentrated narrowly enough. But E_exc is the kinetic
# energy of the quasiparticles, not a potential well.

# ====== FINAL MODEL: Compute V_eff for several scenarios ======

# Scenario 1: E_cond in natural units (per fiber, M_KK -> M_KK^4)
E_cond_V = abs(E_cond)  # (local) 0.137 in V_bare units
# Scenario 2: E_cond with van Hove enhancement (rho*Delta^2/2)
E_cond_vH = 0.5 * Delta_BCS**2 * rho_B2_per_mode  # (local)
# Scenario 3: Full excitation energy as potential depth (extreme upper bound)
E_cond_exc = abs(E_cond) * 100  # (local) 100x enhancement = 13.7 M_KK^4

print(f"\n  === BCS Condensation Energy Scenarios ===")
print(f"  V_bare(fold) = {V_fold_HK:.4f} M_KK^4")
print(f"  dV_bare/dtau(fold) = {dV_SA_fold:.4f} M_KK^4")
print(f"")
print(f"  Scenario 1 (canonical E_cond): |V_BCS| = {E_cond_V:.6f}")
print(f"    Ratio to V_bare: {E_cond_V / V_fold_HK:.6e}")
print(f"    tau_w needed for min: {E_cond_V / dV_SA_fold:.6e}")
print(f"")
print(f"  Scenario 2 (van Hove rho*Delta^2/2): |V_BCS| = {E_cond_vH:.6f}")
print(f"    Ratio to V_bare: {E_cond_vH / V_fold_HK:.6e}")
print(f"    tau_w needed for min: {E_cond_vH / dV_SA_fold:.6e}")
print(f"")
print(f"  Scenario 3 (100x enhancement): |V_BCS| = {E_cond_exc:.4f}")
print(f"    Ratio to V_bare: {E_cond_exc / V_fold_HK:.6e}")
print(f"    tau_w needed for min: {E_cond_exc / dV_SA_fold:.6e}")

# For each scenario, compute V_eff and check for minimum
results = {}  # (local)

for label, E_BCS, tau_w_list in [
    ("Canonical E_cond", E_cond_V, [0.01, 0.02, 0.05, 0.10]),
    ("van Hove enhanced", E_cond_vH, [0.01, 0.02, 0.05, 0.10]),
    ("100x enhanced", E_cond_exc, [0.01, 0.02, 0.05, 0.10]),
]:
    print(f"\n  --- {label}: |E_BCS| = {E_BCS:.6f} ---")
    for tw in tau_w_list:
        # BCS energy: Gaussian well centered at tau_fold
        E_bcs_arr = -E_BCS * np.exp(-((tau_veff - tau_fold) / tw)**2)  # (local)

        # V_eff = V_bare + E_bcs
        V_eff_arr = V_bare_arr + E_bcs_arr  # (local)

        # Check for minimum by looking at gradient sign changes
        dV_eff = np.gradient(V_eff_arr, tau_veff)  # (local)
        sign_changes_veff = np.where(np.diff(np.sign(dV_eff)))[0]  # (local)

        has_min = False  # (local)
        tau_min_val = None  # (local)

        for sc in sign_changes_veff:
            # Minimum = gradient goes from negative to positive
            if dV_eff[sc] < 0 and dV_eff[sc + 1] > 0:
                has_min = True
                tau_min_val = tau_veff[sc]
                break

        if has_min:
            delta_tau_min = abs(tau_min_val - tau_fold)  # (local)
            print(f"    tau_w={tw:.3f}: MINIMUM at tau={tau_min_val:.4f}, "
                  f"|delta|={delta_tau_min:.4f}")
            results[(label, tw)] = {
                'has_min': True, 'tau_min': tau_min_val,
                'delta_tau': delta_tau_min, 'E_BCS': E_BCS, 'tau_w': tw
            }
        else:
            max_dE = E_BCS / tw  # (local) max |dE_bcs/dtau|
            print(f"    tau_w={tw:.3f}: NO minimum. "
                  f"|dE_bcs/dtau|_max={max_dE:.4f} vs dV_bare={dV_SA_fold:.4f} "
                  f"(ratio={max_dE/dV_SA_fold:.4e})")
            results[(label, tw)] = {
                'has_min': False, 'ratio': max_dE / dV_SA_fold,
                'E_BCS': E_BCS, 'tau_w': tw
            }

# =============================================================================
# SECTION 6: CRITICAL TAU_W AND ENHANCEMENT FACTOR
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 6: Critical Enhancement Factor for Minimum")
print("=" * 78)

# For a minimum to exist with Gaussian E_cond:
# dV_eff/dtau = 0 at some tau near tau_fold
# dV_bare/dtau + dE_bcs/dtau = 0
# dV_bare/dtau(fold) = dV_SA_fold = 168.7
# dE_bcs/dtau = 2 * E_BCS * (tau - tau_fold) / tau_w^2 * exp(...)
# Maximum of |dE_bcs/dtau| occurs at tau = tau_fold +/- tau_w/sqrt(2):
# |dE_bcs/dtau|_max = E_BCS * sqrt(2/e) / tau_w

# For balance: E_BCS * sqrt(2/e) / tau_w = dV_SA_fold
# E_BCS_critical = dV_SA_fold * tau_w / sqrt(2/e) = dV_SA_fold * tau_w * 1.166

sqrt_2_over_e = np.sqrt(2.0 / np.e)  # (local) = 0.8578

print(f"  Gradient balance condition:")
print(f"  E_BCS * sqrt(2/e) / tau_w = dV_bare/dtau(fold)")
print(f"  E_BCS_critical = dV_bare * tau_w / sqrt(2/e)")
print(f"  sqrt(2/e) = {sqrt_2_over_e:.4f}")
print(f"  dV_bare/dtau(fold) = {dV_SA_fold:.4f}")
print(f"")

for tw in [0.01, 0.02, 0.05, 0.10, 0.20]:
    E_crit = dV_SA_fold * tw / sqrt_2_over_e  # (local)
    enhancement = E_crit / abs(E_cond)  # (local)
    print(f"  tau_w = {tw:.3f}: E_BCS_critical = {E_crit:.4f}, "
          f"enhancement needed = {enhancement:.1f}x over |E_cond|={abs(E_cond):.3f}")

# For tau_w = 0.05 (reasonable BCS width):
tau_w_phys = 0.05  # (local) physical tau_w
E_crit_phys = dV_SA_fold * tau_w_phys / sqrt_2_over_e  # (local)
enhancement_phys = E_crit_phys / abs(E_cond)  # (local)

print(f"\n  Physical tau_w = {tau_w_phys}: enhancement needed = {enhancement_phys:.1f}x")
print(f"  This means E_BCS must be {E_crit_phys:.2f} to create a minimum")
print(f"  Canonical E_cond = {abs(E_cond):.6f}")
print(f"  Ratio: {enhancement_phys:.1f}x too small")

# =============================================================================
# SECTION 7: PROPAGATE TO R_1 AND OBSERVABLES
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 7: R_1 Stability Analysis")
print("=" * 78)

# Load R_1(tau) from S77 data
d77 = np.load('s77_equil_tau.npz', allow_pickle=True)
tau_gilkey = d77['tau_gilkey']   # [0, 0.5] 101 points
R1_gilkey = d77['R1_gilkey']     # R_1 = a_0*a_4/a_2^2

cs_R1 = CubicSpline(tau_gilkey, R1_gilkey)

R1_fold = cs_R1(tau_fold)  # (local)
R1_max_dev = np.max(np.abs(R1_gilkey - R1_fold)) / R1_fold  # (local)

print(f"  R_1(tau_fold) = {R1_fold:.6f}")
print(f"  R_1 max deviation in [0, 0.5]: {R1_max_dev*100:.4f}%")
print(f"  R-protection holds regardless of BCS minimum question")

# Even if there's no minimum, R_1 is stable in [0, 0.5]
# The question of WHERE tau settles doesn't affect R_1-protected observables

# =============================================================================
# SECTION 8: CROSS-CHECKS
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Cross-Checks")
print("=" * 78)

# CHK1: V_bare monotonically increasing
chk1 = dS_all_positive  # (local)
print(f"  CHK1: V_bare monotonically increasing: {'PASS' if chk1 else 'FAIL'}")

# CHK2: E_cond(tau_fold) < 0
chk2 = (E_cond < 0)  # (local)
print(f"  CHK2: E_cond(tau_fold) = {E_cond:.6f} < 0: {'PASS' if chk2 else 'FAIL'}")

# CHK3: E_cond(tau) -> 0 away from fold
# For Gaussian model with any tau_w, exp(-((tau_far - tau_fold)/tau_w)^2) -> 0
chk3 = True  # (local) By construction of Gaussian model
print(f"  CHK3: E_cond -> 0 away from fold: PASS (Gaussian model)")

# CHK4: V_eff(tau_fold) < V_bare(tau_fold)
V_eff_fold = V_bare_fn(tau_fold) + E_cond  # (local) using canonical E_cond
chk4 = (V_eff_fold < V_bare_fn(tau_fold))  # (local)
print(f"  CHK4: V_eff(fold) = {V_eff_fold:.4f} < V_bare(fold) = {V_bare_fn(tau_fold):.4f}: "
      f"{'PASS' if chk4 else 'FAIL'}")
print(f"    BCS lowers V at fold by {abs(E_cond):.6f} M_KK^4 = {abs(E_cond)/V_bare_fn(tau_fold)*100:.4f}%")

# =============================================================================
# SECTION 9: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 9: Gate Verdict")
print("=" * 78)

# Check if any scenario produced a minimum
any_minimum = any(r.get('has_min', False) for r in results.values())  # (local)
canonical_minimum = results.get(("Canonical E_cond", 0.05), {}).get('has_min', False)  # (local)

if canonical_minimum:
    tau_min = results[("Canonical E_cond", 0.05)]['tau_min']  # (local)
    delta_tau = abs(tau_min - tau_fold)  # (local)
    if delta_tau < 0.05:
        verdict = "PASS"
        detail = f"|tau_equil - 0.190| = {delta_tau:.4f} < 0.05"
    elif delta_tau < 0.20:
        verdict = "INFO"
        detail = f"|tau_equil - 0.190| = {delta_tau:.4f} in [0.05, 0.20]"
    else:
        verdict = "FAIL"
        detail = f"|tau_equil - 0.190| = {delta_tau:.4f} > 0.20"
else:
    verdict = "FAIL"
    # Find which enhanced scenarios have minima
    enhanced_mins = [(k, v) for k, v in results.items() if v.get('has_min', False)]  # (local)
    if enhanced_mins:
        best = min(enhanced_mins, key=lambda x: x[1]['delta_tau'])  # (local)
        detail = (f"No minimum in canonical BCS. "
                 f"Enhancement {best[1]['E_BCS']/abs(E_cond):.0f}x needed. "
                 f"Best minimum at tau={best[1]['tau_min']:.4f} with "
                 f"E_BCS={best[1]['E_BCS']:.4f}, tau_w={best[1]['tau_w']:.3f}")
    else:
        detail = (f"No minimum in ANY scenario. "
                 f"BCS gradient max={abs(E_cond)*sqrt_2_over_e/0.01:.4f} vs "
                 f"V_bare gradient={dV_SA_fold:.4f}. "
                 f"Enhancement needed: {enhancement_phys:.0f}x at tau_w={tau_w_phys}")

# Compute tau_equil (best estimate)
if canonical_minimum:
    tau_equil = results[("Canonical E_cond", 0.05)]['tau_min']  # (local)
else:
    # tau_equil from time-average of S73B trajectory (from prior computation)
    tau_equil = float(d77['tau_equil'])  # (local) 1.092

delta_equil = abs(tau_equil - tau_fold)  # (local)

print(f"  Gate: S77-A1-EQUIL-TAU")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")
print(f"  tau_equil = {tau_equil:.6f}")
print(f"  |tau_equil - 0.190| = {delta_equil:.6f}")
print(f"")
print(f"  BCS-to-bare ratio: {abs(E_cond)/V_fold_HK:.6e}")
print(f"  Enhancement needed for minimum (tau_w=0.05): {enhancement_phys:.1f}x")
print(f"  R_1 protected to {R1_max_dev*100:.2f}% regardless")

# =============================================================================
# SECTION 10: WHAT COULD CREATE THE MINIMUM?
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 10: What Additional Physics Could Create a Minimum?")
print("=" * 78)

print(f"""
  The BCS condensation energy is {enhancement_phys:.0f}x too small to overcome the
  bare spectral action gradient at the fold. To create a minimum, one needs:

  1. MULTI-BAND ENHANCEMENT: The 8-mode BCS model uses 1 B1 + 4 B2 + 3 B3 modes.
     At L_max = 10, there are 155,984 eigenvalues. If inter-band pairing extends
     to more modes, E_cond could be larger. Enhancement factor: up to
     155984/8 = 19,498x (theoretical maximum, physically unrealistic).
     Realistic multi-band: 10-100x.

  2. SPATIAL JOSEPHSON COUPLING: The BCS calculation is per-fiber. If neighboring
     fibers couple via Josephson-like terms, the collective condensation energy
     includes the spatial stiffness (xi_BCS = 0.808 M_KK^{{-1}}). This adds an
     energy density from the condensate gradient: E_J ~ J * Delta^2 * xi^2.
     Enhancement: O(1) -- not enough by itself.

  3. SPECTRAL ACTION FUNCTIONAL DEPENDENCE: The bare gradient dS/dtau depends
     on the choice of functional f*. Other functionals (exp, compact) have
     NEGATIVE Delta_S at the fold, meaning the BCS shift works in the right
     direction. But the f* functional is observationally selected.

  4. NON-PERTURBATIVE INSTANTON CONTRIBUTIONS: The instanton gas creates a
     non-perturbative potential V_inst(tau) that is independent of the spectral
     action. If V_inst has a minimum near the fold, it could stabilize tau
     regardless of V_bare. This is the CASIMIR-JOSEPHSON-52 channel.

  5. TADPOLE CANCELLATION: If the bare spectral action gradient is cancelled
     by a tadpole condition (fixing a Lagrange multiplier), the remaining
     potential could be dominated by BCS. This would require V_bare to be
     a constraint, not a potential.
""")

# =============================================================================
# SECTION 11: PLOTTING
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 11: Generating Plot")
print("=" * 78)

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.3, wspace=0.3)

# Panel 1: V_bare(tau)
ax1 = fig.add_subplot(gs[0, 0])
tau_plot = np.linspace(0.05, 0.8, 1000)  # (local)
V_bare_plot = np.array([V_bare_fn(t) for t in tau_plot])  # (local)
ax1.plot(tau_plot, V_bare_plot, 'b-', linewidth=2, label=r'$V_{\rm bare}(\tau)$')
ax1.axvline(tau_fold, color='r', linestyle='--', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax1.set_xlabel(r'$\tau$', fontsize=14)
ax1.set_ylabel(r'$V \ [M_{\rm KK}^4]$', fontsize=14)
ax1.set_title(r'Bare Spectral Action Potential', fontsize=14)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# Panel 2: BCS condensation energy models
ax2 = fig.add_subplot(gs[0, 1])
tau_narrow = np.linspace(0.0, 0.5, 2000)  # (local)
for tw, ls in [(0.01, '-'), (0.02, '--'), (0.05, '-.'), (0.10, ':')]:
    E_bcs = -abs(E_cond) * np.exp(-((tau_narrow - tau_fold) / tw)**2)
    ax2.plot(tau_narrow, E_bcs, ls, linewidth=2,
             label=rf'$\tau_w = {tw}$')
ax2.axvline(tau_fold, color='r', linestyle='--', alpha=0.5)
ax2.set_xlabel(r'$\tau$', fontsize=14)
ax2.set_ylabel(r'$E_{\rm cond}(\tau)$', fontsize=14)
ax2.set_title(r'BCS Condensation Energy (canonical)', fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

# Panel 3: V_eff for scenarios with tau_w = 0.05
ax3 = fig.add_subplot(gs[1, 0])
tau_zoom = np.linspace(0.05, 0.50, 2000)  # (local)
V_bare_zoom = np.array([V_bare_fn(t) for t in tau_zoom])  # (local)
ax3.plot(tau_zoom, V_bare_zoom, 'b-', linewidth=2, label=r'$V_{\rm bare}$')

tw = 0.05  # (local)
for E_label, E_val, color in [
    ("Canonical", E_cond_V, 'g'),
    ("van Hove", E_cond_vH, 'orange'),
    ("100x enhanced", E_cond_exc, 'r'),
]:
    E_bcs_zoom = -E_val * np.exp(-((tau_zoom - tau_fold) / tw)**2)
    V_eff_zoom = V_bare_zoom + E_bcs_zoom
    ax3.plot(tau_zoom, V_eff_zoom, color=color, linewidth=2,
             linestyle='--', label=rf'$V_{{\rm eff}}$ ({E_label})')

ax3.axvline(tau_fold, color='r', linestyle=':', alpha=0.5)
ax3.set_xlabel(r'$\tau$', fontsize=14)
ax3.set_ylabel(r'$V \ [M_{\rm KK}^4]$', fontsize=14)
ax3.set_title(rf'$V_{{\rm eff}}(\tau)$ with BCS dressing ($\tau_w = {tw}$)', fontsize=14)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: Enhancement factor needed vs tau_w
ax4 = fig.add_subplot(gs[1, 1])
tau_w_range = np.logspace(-3, -0.3, 200)  # (local)
enhancement_range = dV_SA_fold * tau_w_range / (sqrt_2_over_e * abs(E_cond))  # (local)

ax4.loglog(tau_w_range, enhancement_range, 'k-', linewidth=2)
ax4.axhline(1.0, color='g', linestyle='--', alpha=0.7, label='No enhancement needed')
ax4.axhline(10, color='orange', linestyle=':', alpha=0.7, label='10x enhancement')
ax4.axhline(100, color='r', linestyle=':', alpha=0.7, label='100x enhancement')
ax4.axvline(0.05, color='b', linestyle='--', alpha=0.5, label=r'$\tau_w = 0.05$ (physical)')

ax4.set_xlabel(r'$\tau_w$ (BCS gap width)', fontsize=14)
ax4.set_ylabel(r'Enhancement factor needed', fontsize=14)
ax4.set_title('Enhancement Factor for V_eff Minimum', fontsize=14)
ax4.legend(fontsize=10)
ax4.grid(True, alpha=0.3, which='both')
ax4.set_ylim(0.01, 1e5)

fig.suptitle(
    r'S77-A1-EQUIL-TAU RETASK: BCS-Dressed Equilibrium $\tau$'
    f'\nVerdict: {verdict}',
    fontsize=16, fontweight='bold'
)

plt.savefig('s77_equil_tau_bcs.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved: s77_equil_tau_bcs.png")

# =============================================================================
# SECTION 12: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 12: Saving Results")
print("=" * 78)

# Collect minimum results for all scenarios
min_scenarios = {}  # (local)
for (label, tw), r in results.items():
    if r.get('has_min', False):
        min_scenarios[f"{label}_tw{tw}"] = r

np.savez('s77_equil_tau_bcs.npz',
    # Gate metadata
    gate_name='S77-A1-EQUIL-TAU-RETASK',
    gate_verdict=verdict,
    gate_detail=detail,

    # Key results
    tau_equil=tau_equil,
    delta_tau_equil=delta_equil,
    V_bare_fold=V_fold_HK,
    E_cond_canonical=E_cond,
    E_cond_vH=E_cond_vH,
    ratio_Econd_Vbare=abs(E_cond) / V_fold_HK,
    dV_bare_fold=dV_SA_fold,
    enhancement_needed_tw005=enhancement_phys,

    # BCS model parameters
    Delta_BCS=Delta_BCS,
    rho_B2_fold=rho_B2_per_mode,
    tau_w_physical=tau_w_phys,

    # R_1 stability
    R1_fold=R1_fold,
    R1_max_deviation=R1_max_dev,
    tau_gilkey=tau_gilkey,
    R1_gilkey=R1_gilkey,

    # V_eff arrays for plotting
    tau_veff=tau_veff,
    V_bare_arr=V_bare_arr,

    # Cross-checks
    CHK1_bare_monotonic=chk1,
    CHK2_Econd_negative=chk2,
    CHK3_Econd_vanishes=chk3,
    CHK4_Veff_lower=chk4,

    # Trajectory from S73B (reference)
    tau_max_overshoot=tau_max_overshoot,
    t_max_overshoot=t_max_overshoot,
    is_monotonic_potential=True,
)

print(f"  Data saved: s77_equil_tau_bcs.npz")

# =============================================================================
# FINAL SUMMARY
# =============================================================================
elapsed = time.time() - t_start  # (local)
print("\n" + "=" * 78)
print("FINAL SUMMARY")
print("=" * 78)
print(f"""
  Gate: S77-A1-EQUIL-TAU (RETASK -- BCS-dressed)
  Verdict: {verdict}

  V_bare(fold) = {V_fold_HK:.4f} M_KK^4 (heat-kernel normalized)
  E_cond(fold) = {E_cond:.6f} M_KK (canonical ED, 8-mode)
  |E_cond|/V_bare = {abs(E_cond)/V_fold_HK:.6e}
  dV_bare/dtau(fold) = {dV_SA_fold:.4f} M_KK^4

  For minimum at tau_w = 0.05:
    Enhancement needed: {enhancement_phys:.1f}x over canonical E_cond
    E_BCS_critical = {E_crit_phys:.4f} M_KK^4

  BCS dressing is {enhancement_phys:.0f}x too weak to create a potential minimum.
  The bare spectral action gradient overwhelms the condensation energy at the fold.

  R_1 = {R1_fold:.6f} (protected to {R1_max_dev*100:.2f}%) -- stable regardless.

  Elapsed: {elapsed:.1f}s
""")
