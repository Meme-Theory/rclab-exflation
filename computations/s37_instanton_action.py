#!/usr/bin/env python3
"""
Session 37: F.1 Instanton Action from ED Spectrum (ZERO-COST)
=============================================================

GATE: INST-37a
  S_inst < 0.5  -> Dense instanton gas, Z_2 restored, virtual particle regime
  0.5 < S_inst < 5 -> Crossover regime
  S_inst > 5    -> Dilute instantons, standard mean-field BCS

CONTEXT:
  The BCS condensate on the B2 sector breaks Z_2 (sign of Delta).
  GL-CUBIC-36 confirmed: second-order transition, Z_2 universality class.
  No cubic term (U(1)_7 forbids it). The GL potential is:

    F_GL[Delta] = a |Delta|^2 + b |Delta|^4

  with a < 0 (below T_c / above the Thouless threshold) and b > 0.

  The instanton connects the false vacuum (Delta=0) to the true vacuum
  (Delta=Delta_0) through a kink solution. The action determines the
  tunneling rate: Gamma ~ exp(-S_inst).

PHYSICAL PARAMETERS (from Session 35-36):
  M_max = 1.674 (8x8 authoritative, MMAX-AUTH-36)
  M_max(B2-only) = 1.351 (conservative)
  rho_smooth = 14.02 per B2 mode (van Hove DOS)
  E_cond = -0.137 (8-mode ED, ED-CONV-36)
  v_F = 0.01174 (Fermi velocity at physical fold)
  N_B2 = 4 (B2 flat-band modes)
  B2 bandwidth = 0.0579
  E_fold = 0.845

METHODOLOGY:
  1. Derive GL coefficients a, b from BCS gap equation near T_c
  2. Compute instanton action in 1D (kink solution)
  3. Compute coherence length xi_BCS
  4. Cross-check against ED condensation energy

Author: nazarewicz-nuclear-structure-theorist, Session 37
Date: 2026-03-08
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigvals, eigh
from scipy.integrate import trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("Session 37: F.1 Instanton Action from ED Spectrum")
print("=" * 78)

# ======================================================================
#  Load data from Session 35-36 computations
# ======================================================================

print("\n--- Loading data ---")

# Load Kosmann singlet data
kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                  allow_pickle=True)
dphys_kosmann = np.load(os.path.join(SCRIPT_DIR, 's34a_dphys_kosmann.npz'),
                        allow_pickle=True)
vh_arbiter = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                     allow_pickle=True)
ed_data = np.load(os.path.join(SCRIPT_DIR, 's36_multisector_ed.npz'),
                  allow_pickle=True)
gl_data = np.load(os.path.join(SCRIPT_DIR, 's36_gl_cubic_check.npz'),
                  allow_pickle=True)
gcm_data = np.load(os.path.join(SCRIPT_DIR, 's36_gcm_self_consistent.npz'),
                   allow_pickle=True)

# Key physical parameters
E_8 = ed_data['E_8_full']      # 8 positive eigenvalues
V_8 = ed_data['V_8x8_full']    # 8x8 pairing matrix
E_cond_full = float(ed_data['E_cond_full'])   # -0.137

rho_B2_per_mode = float(vh_arbiter['rho_at_physical'])   # 14.02
v_F = float(vh_arbiter['v_phys'])              # 0.01174
E_fold = float(vh_arbiter['E_fold'])           # 0.845
B2_bw = float(vh_arbiter['B2_bw'])             # 0.0579
d2E_fold = float(vh_arbiter['d2E_fold'])       # 1.176 (dispersion curvature)
tau_fold = float(vh_arbiter['tau_fold'])        # 0.190

# B2 eigenvalues at tau=0.20 (near fold)
ti = 3  # tau index for 0.20
evals_raw = kosmann[f'eigenvalues_{ti}']
si = np.argsort(evals_raw)
evals_s = evals_raw[si]
pos_idx = np.where(evals_s > 0)[0]
B2_idx = pos_idx[1:5]
B1_idx = pos_idx[0:1]
B3_idx = pos_idx[5:8]
E_B2 = evals_s[B2_idx]
E_B1 = evals_s[B1_idx]
E_B3 = evals_s[B3_idx]

# M_max values
M_max_8x8 = float(ed_data['config_4_M_max_mf'])   # 1.396
M_max_B2only = float(ed_data['config_0_M_max_mf']) # 1.292
M_max_AUTH = 1.674   # Authoritative from MMAX-AUTH-36

# GCM fine-resolution BCS gap at fold
tau_fine = gcm_data['tau_fine']
Delta_fine = gcm_data['Delta_max_fine']
E_BCS_fine = gcm_data['E_BCS_fine']
Mmax_8x8_fine = gcm_data['Mmax_8x8_fine']

# Find peak BCS gap
idx_peak = np.argmax(Delta_fine)
Delta_0_peak = Delta_fine[idx_peak]
tau_peak = tau_fine[idx_peak]

# At tau=0.20
idx_020 = np.argmin(np.abs(tau_fine - 0.20))
Delta_0_020 = Delta_fine[idx_020]

print(f"\n  Physical parameters:")
print(f"    E_B2 = {E_B2}")
print(f"    E_B1 = {E_B1}")
print(f"    E_B3 = {E_B3}")
print(f"    E_fold = {E_fold}")
print(f"    B2 bandwidth = {B2_bw}")
print(f"    v_F = {v_F}")
print(f"    d2E/dk2 at fold = {d2E_fold}")
print(f"    rho_B2 per mode = {rho_B2_per_mode}")
print(f"    M_max (8x8 ED) = {M_max_8x8}")
print(f"    M_max (B2-only ED) = {M_max_B2only}")
print(f"    M_max (authoritative) = {M_max_AUTH}")
print(f"    E_cond (8-mode ED) = {E_cond_full}")
print(f"    Delta_0 at peak (tau={tau_peak:.4f}) = {Delta_0_peak:.6f}")
print(f"    Delta_0 at tau=0.20 = {Delta_0_020:.6f}")


# ======================================================================
#  STEP 1: GL coefficients from BCS microscopic theory
# ======================================================================

print("\n" + "=" * 78)
print("STEP 1: GL Coefficients from BCS Theory")
print("=" * 78)

print("""
  The Ginzburg-Landau free energy density for a BCS superconductor is:

    F_GL[Delta] = a |Delta|^2 + b |Delta|^4                           (1)

  where (standard BCS derivation, see e.g. Abrikosov-Gorkov-Dzyaloshinski):

    a = N(0) * (1 - g*N(0))  /  (g*N(0))                             (2)
      = N(0) * (1 - M_max) / M_max

  Here M_max = g*N(0) is the Thouless eigenvalue. For M_max > 1:
    a < 0 (broken symmetry phase, below T_c).

    b = 7*zeta(3) * N(0) / (8 * pi^2 * T_c^2)                        (3)

  In the nuclear/condensed-matter BCS at T=0, the GL coefficients relate
  to the gap Delta_0 and condensation energy E_cond through:

    Delta_0^2 = -a / (2b)                                             (4)
    E_cond = -a^2 / (4b) = -N(0) * Delta_0^2 / 2                     (5)

  The last equality is the standard BCS result at T=0.

  HOWEVER: our system has N_pair = 1 exactly (from ED). This is NOT
  the thermodynamic BCS limit. The GL expansion is still valid as a
  PARAMETRIZATION of the energy landscape, but the coefficients must
  be extracted from the ED data directly, not from asymptotic formulas.
""")

# Method A: Extract GL coefficients from E_cond and Delta_0
# Using E_cond = -a^2/(4b) and Delta_0^2 = -a/(2b)
# => a = -2 E_cond / Delta_0^2
# => b = E_cond / Delta_0^4

# Use the peak values (tau = 0.1902, closest to fold)
Delta_0 = Delta_0_peak
E_cond_use = float(gcm_data['E_BCS_fine'][idx_peak])

print(f"\n  Method A: Extract from BCS gap equation solution")
print(f"    Using peak values at tau = {tau_peak:.4f}:")
print(f"    Delta_0 = {Delta_0:.6f}")
print(f"    E_BCS = {E_cond_use:.6f}")

if abs(Delta_0) > 1e-8 and E_cond_use < 0:
    a_A = 2.0 * E_cond_use / Delta_0**2     # should be negative
    b_A = -E_cond_use / Delta_0**4           # should be positive

    print(f"    a = 2*E_BCS/Delta_0^2 = {a_A:.6f}")
    print(f"    b = -E_BCS/Delta_0^4 = {b_A:.6f}")
    print(f"    Check: Delta_0^2 = -a/(2b) = {-a_A/(2*b_A):.6f} vs {Delta_0**2:.6f}")
    print(f"    Check: E_cond = -a^2/(4b) = {-a_A**2/(4*b_A):.6f} vs {E_cond_use:.6f}")
else:
    print(f"    Cannot extract: Delta_0 or E_BCS invalid")
    a_A = -1.0
    b_A = 1.0

# Method B: From Thouless criterion directly
# The linearized gap equation gives M_max = sum_k V_kk' * rho_k / (2|xi_k|)
# Near the critical point: a = N_total(0) * (1 - M_max) / M_max
# where N_total(0) = sum of DOS for all modes

N_total_B2 = 4 * rho_B2_per_mode  # Total B2 DOS
M_max_use = M_max_AUTH  # 1.674

# For the GL coefficient a from Thouless:
# a = -N_total(0) * (M_max - 1) / M_max
a_B = -N_total_B2 * (M_max_use - 1.0) / M_max_use

# b from Delta_0: b = -a/(2*Delta_0^2)
b_B = -a_B / (2.0 * Delta_0**2)

print(f"\n  Method B: From Thouless criterion (M_max = {M_max_use})")
print(f"    N_total(0) = 4 * rho_B2 = {N_total_B2:.4f}")
print(f"    a = -N(0)*(M_max-1)/M_max = {a_B:.6f}")
print(f"    b = -a/(2*Delta_0^2) = {b_B:.6f}")
print(f"    Check: E_cond_GL = -a^2/(4b) = {-a_B**2/(4*b_B):.6f}")

# Method C: BCS free energy along instanton path (scaling parametrization)
# The correct approach for a multi-mode system: parametrize
# Delta_k(alpha) = alpha * Delta_k^{SC}, where Delta_k^{SC} is the
# self-consistent gap solution. Then F(alpha) gives the GL potential
# along the instanton path.

print(f"\n  Method C: BCS free energy along instanton path")
print(f"    (multi-mode gap, scaling parametrization)")

# Build the V matrix for B2 sector
V_B2 = V_8[np.ix_([0,1,2,3], [0,1,2,3])]
rho_B2_vec = np.array([rho_B2_per_mode]*4)
xi_B2 = E_B2 - 0.0  # mu = 0

# First solve the gap equation to get the self-consistent Delta_k
def solve_gap_equation(V_mat, xi, rho, n_iter=5000, tol=1e-14):
    """Solve multi-mode BCS gap equation:
    Delta_k = sum_{k'} V_{kk'} * rho_{k'} * Delta_{k'} / (2 * E_{k'})
    E_{k'} = sqrt(xi_{k'}^2 + Delta_{k'}^2)
    """
    n = len(xi)
    Delta = np.ones(n) * 0.1  # initial guess
    for it in range(n_iter):
        E_qp = np.sqrt(xi**2 + Delta**2)
        Delta_new = np.zeros(n)
        for k in range(n):
            for kp in range(n):
                Delta_new[k] += V_mat[k, kp] * np.sqrt(rho[k] * rho[kp]) * Delta[kp] / (2.0 * E_qp[kp])
        diff = np.max(np.abs(Delta_new - Delta))
        Delta = Delta_new.copy()
        if diff < tol:
            return Delta, True, it
    return Delta, False, n_iter

Delta_SC, conv_SC, nit_SC = solve_gap_equation(V_B2, xi_B2, rho_B2_vec)
print(f"    Gap equation converged: {conv_SC} ({nit_SC} iterations)")
print(f"    Delta_SC = {Delta_SC}")
print(f"    max(Delta_SC) = {np.max(Delta_SC):.8f}")
Delta_max_SC = np.max(Delta_SC)

# Now compute the BCS free energy F(alpha) along the path
# Delta_k(alpha) = alpha * Delta_k^{SC}
#
# F[{Delta_k}] = sum_k rho_k * [sqrt(xi_k^2 + Delta_k^2) - |xi_k|]
#              - sum_{k,k'} V_{kk'} * sqrt(rho_k*rho_k') * Delta_k*Delta_{k'} / (4*E_k*E_{k'})
#
# The first term is the kinetic energy cost of pairing.
# The second term is the pairing interaction energy gain.

def bcs_free_energy_path(alpha, Delta_SC, V_mat, xi, rho):
    """BCS variational energy at Delta_k = alpha * Delta_SC_k.

    The BCS variational state gives:
      E = sum_k 2*xi_k * v_k^2 - sum_{k,k'} V_{kk'} * sqrt(rho_k*rho_{k'}) * u_k*v_k * u_{k'}*v_{k'}

    where v_k^2 = (1 - xi_k/E_k)/2, u_k*v_k = Delta_k/(2*E_k).

    Measured relative to the normal state (all v_k = 0):
      F = sum_k [E_k - |xi_k|] - sum_{k,k'} V_{kk'} * sqrt(rho_k*rho_{k'}) * Delta_k*Delta_{k'} / (4*E_k*E_{k'})

    NOTE: The kinetic term sum_k [E_k - |xi_k|] does NOT carry the DOS
    prefactor because this is a DISCRETE-mode Hamiltonian where the DOS
    is already absorbed into the off-diagonal coupling sqrt(rho_k*rho_{k'}).
    """
    n = len(xi)
    Delta = alpha * Delta_SC
    E_qp = np.sqrt(xi**2 + Delta**2)

    # Kinetic: no DOS factor (discrete-mode BCS)
    F_kin = np.sum(E_qp - np.abs(xi))

    # Interaction: V * sqrt(rho_k * rho_{k'}) * uv_k * uv_{k'}
    F_pair = 0.0
    for k in range(n):
        for kp in range(n):
            F_pair -= V_mat[k, kp] * np.sqrt(rho[k] * rho[kp]) * Delta[k] * Delta[kp] / (4.0 * E_qp[k] * E_qp[kp])

    return F_kin + F_pair

alpha_scan = np.linspace(0, 3.0, 10001)
F_alpha = np.array([bcs_free_energy_path(a, Delta_SC, V_B2, xi_B2, rho_B2_vec)
                     for a in alpha_scan])

# Find minimum
idx_min = np.argmin(F_alpha)
alpha_min = alpha_scan[idx_min]
F_min = F_alpha[idx_min]
Delta_0_num = alpha_min * Delta_max_SC

print(f"\n    Free energy landscape along instanton path:")
print(f"    alpha_min = {alpha_min:.6f}")
print(f"    Delta_0 = alpha_min * max(Delta_SC) = {Delta_0_num:.8f}")
print(f"    F_min = {F_min:.8f}")
print(f"    F(0) = {F_alpha[0]:.8f}")
print(f"    E_cond = F_min - F(0) = {F_min - F_alpha[0]:.8f}")

# GL fit: F(alpha) ~ a_eff * alpha^2 + b_eff * alpha^4
# (The alpha=0 and alpha=alpha_min define the instanton endpoints)
mask_fit = (alpha_scan > 0.01) & (alpha_scan < 2.5)
x_fit = alpha_scan[mask_fit]
y_fit = F_alpha[mask_fit]
A_design = np.column_stack([x_fit**2, x_fit**4])
coeffs_C, _, _, _ = np.linalg.lstsq(A_design, y_fit, rcond=None)
a_C_alpha, b_C_alpha = coeffs_C

print(f"\n    GL fit in alpha: F(alpha) = a_eff * alpha^2 + b_eff * alpha^4")
print(f"    a_eff = {a_C_alpha:.8f}")
print(f"    b_eff = {b_C_alpha:.8f}")

if b_C_alpha > 0 and a_C_alpha < 0:
    alpha_0_GL = np.sqrt(-a_C_alpha / (2*b_C_alpha))
    F_min_GL = -a_C_alpha**2 / (4*b_C_alpha)
    print(f"    alpha_0(GL) = {alpha_0_GL:.6f} vs {alpha_min:.6f}")
    print(f"    E_cond(GL) = {F_min_GL:.8f} vs {F_min:.8f}")

    # Convert to Delta-space GL coefficients
    # F(Delta) = a_eff/D_SC^2 * Delta^2 + b_eff/D_SC^4 * Delta^4
    # where Delta = alpha * D_SC (max component)
    a_C = a_C_alpha / Delta_max_SC**2
    b_C = b_C_alpha / Delta_max_SC**4
else:
    # Use Method A values as fallback
    a_C = a_A
    b_C = b_A
    print(f"    GL fit failed (a_eff >= 0 or b_eff <= 0). Using Method A values.")

print(f"    a_GL (Delta-space) = {a_C:.8f}")
print(f"    b_GL (Delta-space) = {b_C:.8f}")
if b_C > 0 and a_C < 0:
    Delta_0_C = np.sqrt(-a_C / (2*b_C))
    print(f"    Delta_0(GL) = {Delta_0_C:.6f}")
else:
    Delta_0_C = Delta_0_num

# Store for later use
delta_scan = alpha_scan * Delta_max_SC
F_BCS = F_alpha


# ======================================================================
#  STEP 2: Instanton Action Computation
# ======================================================================

print("\n" + "=" * 78)
print("STEP 2: Instanton Action")
print("=" * 78)

print("""
  The GL potential (measured from the broken minimum) is:

    V(Delta) = F_GL(Delta) - F_GL(Delta_0)
             = a*(Delta^2 - Delta_0^2) + b*(Delta^4 - Delta_0^4)        (6)

  At Delta = 0: V(0) = -a*Delta_0^2 - b*Delta_0^4 = |a|^2/(4b)
  This is the barrier height separating the false vacuum (Delta=0)
  from the true vacuum (Delta=Delta_0).

  The 1D instanton (kink) action is (Landau & Lifshitz notation):

    S_inst = integral_0^{Delta_0} sqrt(2 * V(Delta)) dDelta             (7)

  For V(Delta) = a*Delta^2 + b*Delta^4 - E_cond (shifted so V(Delta_0)=0):

    V(Delta) - V(Delta_0) = a*(Delta^2 - Delta_0^2) + b*(Delta^4 - Delta_0^4)
                          = (Delta^2 - Delta_0^2) * (a + b*(Delta^2 + Delta_0^2))

  With a = -2*b*Delta_0^2 (from the minimum condition):
    V = (Delta^2 - Delta_0^2) * (-2b*Delta_0^2 + b*(Delta^2 + Delta_0^2))
      = b * (Delta^2 - Delta_0^2) * (Delta^2 - Delta_0^2)
      = b * (Delta^2 - Delta_0^2)^2

  So V(Delta) = b * (Delta^2 - Delta_0^2)^2 (the "Mexican hat" profile).

  The instanton action becomes:

    S_inst = integral_0^{Delta_0} sqrt(2b) * |Delta^2 - Delta_0^2| dDelta
           = sqrt(2b) * integral_0^{Delta_0} (Delta_0^2 - Delta^2) dDelta
           = sqrt(2b) * [Delta_0^2 * Delta - Delta^3/3]_0^{Delta_0}
           = sqrt(2b) * (2/3) * Delta_0^3                               (8)

  This is the EXACT result for the quartic GL potential.
""")

# Compute S_inst using three different sets of GL coefficients

print(f"\n  Computing S_inst = sqrt(2b) * (2/3) * Delta_0^3:")

# Method A: From E_cond and Delta_0 at peak
if abs(Delta_0_peak) > 1e-8:
    S_inst_A = np.sqrt(2*b_A) * (2.0/3.0) * Delta_0_peak**3
    barrier_A = a_A**2 / (4*b_A)
    print(f"\n  Method A (E_cond + Delta_0 at peak):")
    print(f"    a = {a_A:.6f}, b = {b_A:.6f}")
    print(f"    Delta_0 = {Delta_0_peak:.6f}")
    print(f"    Barrier height |a|^2/(4b) = {barrier_A:.8f}")
    print(f"    S_inst = {S_inst_A:.6f}")
else:
    S_inst_A = 0.0
    barrier_A = 0.0

# Method B: From Thouless + Delta_0
S_inst_B = np.sqrt(2*b_B) * (2.0/3.0) * Delta_0_peak**3
barrier_B = a_B**2 / (4*b_B)
print(f"\n  Method B (Thouless M_max = {M_max_AUTH}):")
print(f"    a = {a_B:.6f}, b = {b_B:.6f}")
print(f"    Delta_0 = {Delta_0_peak:.6f}")
print(f"    Barrier height |a|^2/(4b) = {barrier_B:.8f}")
print(f"    S_inst = {S_inst_B:.6f}")

# Method C: Numerical GL fit
if b_C > 0:
    Delta_0_C = np.sqrt(-a_C / (2*b_C))
    S_inst_C = np.sqrt(2*b_C) * (2.0/3.0) * Delta_0_C**3
    barrier_C = a_C**2 / (4*b_C)
    print(f"\n  Method C (Numerical GL fit):")
    print(f"    a = {a_C:.8f}, b = {b_C:.8f}")
    print(f"    Delta_0 = {Delta_0_C:.6f}")
    print(f"    Barrier height |a|^2/(4b) = {barrier_C:.8f}")
    print(f"    S_inst = {S_inst_C:.6f}")
else:
    S_inst_C = 0.0
    barrier_C = 0.0
    Delta_0_C = 0.0
    print(f"\n  Method C: b = {b_C:.8f} <= 0, GL quartic unbound")

# Method D: Direct numerical integration of the instanton
# S_inst = integral_0^{Delta_0_num} sqrt(2 * max(0, F_BCS(Delta_0_num) - F_BCS(Delta))) dDelta
# This is the most rigorous — uses the full BCS free energy, not GL truncation

F_BCS_shifted = F_BCS - F_min  # Shift so minimum is at zero
# The barrier is at Delta=0: V(0) = -F_min = |F_min|

# Numerical integration using trapezoidal rule
delta_inst = delta_scan[:idx_min+1]
V_inst = np.maximum(0, F_BCS_shifted[:idx_min+1])
integrand_inst = np.sqrt(2.0 * V_inst)
S_inst_D = trapezoid(integrand_inst, delta_inst)
barrier_D = F_BCS_shifted[0]

print(f"\n  Method D (Direct numerical from full BCS free energy):")
print(f"    Delta_0 = {Delta_0_num:.6f}")
print(f"    Barrier height F(0) - F(Delta_0) = {barrier_D:.8f}")
print(f"    S_inst (numerical integral) = {S_inst_D:.6f}")

# Method E: 6th-order GL fit along alpha path
mask_6 = (alpha_scan > 0.01) & (alpha_scan < 2.5)
x6 = alpha_scan[mask_6]
y6 = F_alpha[mask_6]
A6 = np.column_stack([x6**2, x6**4, x6**6])
coeffs_6, _, _, _ = np.linalg.lstsq(A6, y6, rcond=None)
a_6, b_6, c_6 = coeffs_6

print(f"\n  Method E (6th-order GL along alpha path):")
print(f"    F(alpha) = {a_6:.6f}*a^2 + {b_6:.6f}*a^4 + {c_6:.6f}*a^6")

# Find minimum of 6th-order: dF/dalpha = 2*a_6*alpha + 4*b_6*alpha^3 + 6*c_6*alpha^5 = 0
# alpha*(a_6 + 2*b_6*alpha^2 + 3*c_6*alpha^4) = 0
# Solve quadratic in alpha^2: 3*c_6*z^2 + 2*b_6*z + a_6 = 0
disc_6 = (2*b_6)**2 - 4*3*c_6*a_6
if disc_6 > 0 and abs(c_6) > 1e-15:
    z_roots = [(-2*b_6 + np.sqrt(disc_6))/(2*3*c_6),
               (-2*b_6 - np.sqrt(disc_6))/(2*3*c_6)]
    z_phys = [z for z in z_roots if z > 0]
    if z_phys:
        alpha_0_6 = np.sqrt(min(z_phys))
        F_6 = a_6*alpha_0_6**2 + b_6*alpha_0_6**4 + c_6*alpha_0_6**6

        # Numerical integration of instanton along alpha path
        al_inst = np.linspace(0, alpha_0_6, 10001)
        V_6 = a_6*al_inst**2 + b_6*al_inst**4 + c_6*al_inst**6
        V_6_shifted = V_6 - V_6[-1]
        integrand_6 = np.sqrt(2.0 * np.maximum(0, V_6_shifted))
        # Convert from alpha to Delta: dDelta = Delta_max_SC * dalpha
        S_inst_E = trapezoid(integrand_6, al_inst) * Delta_max_SC
        barrier_E = V_6_shifted[0]
        print(f"    alpha_0 = {alpha_0_6:.6f}")
        print(f"    Delta_0 = {alpha_0_6 * Delta_max_SC:.6f}")
        print(f"    Barrier = {barrier_E:.8f}")
        print(f"    S_inst = {S_inst_E:.6f}")
    else:
        S_inst_E = 0.0
        barrier_E = 0.0
        print(f"    No physical root")
else:
    S_inst_E = 0.0
    barrier_E = 0.0
    print(f"    Discriminant < 0 or c_6 = 0")


# ======================================================================
#  STEP 3: Conservative and aggressive estimates using M_max range
# ======================================================================

print("\n" + "=" * 78)
print("STEP 3: S_inst across M_max range [1.351, 1.674]")
print("=" * 78)

print("""
  From MMAX-AUTH-36: the authoritative range is [1.351, 1.674].
  For each M_max, we need the corresponding Delta_0 from the gap equation.

  At the BCS level (uniform s-wave gap), the gap equation gives:
    1 = M_max * Delta_0^2 / (sum_k rho_k * Delta_0^2 / E_k^2)

  For uniform Delta, this simplifies to:
    1 = sum_k V_{kk}^{eff} * rho_k / (2 * E_k)
  where E_k = sqrt(xi_k^2 + Delta^2).

  We solve the self-consistent gap equation numerically.
""")

def solve_bcs_gap(V_mat, E_vec, rho_vec, mu=0.0, n_iter=2000, tol=1e-12):
    """Solve the multi-mode BCS gap equation self-consistently.

    Delta_k = sum_{k'} V_{kk'} * rho_{k'} * Delta_{k'} / (2 * E_{k'})
    E_{k'} = sqrt(xi_{k'}^2 + Delta_{k'}^2)

    Returns: Delta_k vector, converged flag
    """
    n = len(E_vec)
    xi = E_vec - mu

    # Initialize with small uniform gap
    Delta = np.ones(n) * 0.01

    for iteration in range(n_iter):
        E_qp = np.sqrt(xi**2 + Delta**2)
        Delta_new = np.zeros(n)
        for k in range(n):
            for kp in range(n):
                Delta_new[k] += V_mat[k, kp] * np.sqrt(rho_vec[k] * rho_vec[kp]) * Delta[kp] / (2.0 * E_qp[kp])
        diff = np.max(np.abs(Delta_new - Delta))
        Delta = Delta_new
        if diff < tol:
            return Delta, True, iteration
    return Delta, False, n_iter

def bcs_econd(Delta, E_vec, V_mat, rho_vec, mu=0.0):
    """BCS condensation energy from the gap solution (discrete-mode)."""
    xi = E_vec - mu
    E_qp = np.sqrt(xi**2 + Delta**2)
    n = len(E_vec)

    # Kinetic: NO DOS factor for discrete-mode BCS
    F_kin = np.sum(E_qp - np.abs(xi))

    # Interaction: V * sqrt(rho) already weighted
    uv = Delta / (2.0 * E_qp)
    F_pair = 0.0
    for k in range(n):
        for kp in range(n):
            F_pair -= V_mat[k, kp] * np.sqrt(rho_vec[k] * rho_vec[kp]) * uv[k] * uv[kp]

    return F_kin + F_pair


# Solve gap equation for B2-only sector
Delta_B2, conv_B2, niter_B2 = solve_bcs_gap(V_B2, E_B2, rho_B2_vec, mu=0.0)
E_cond_B2_gap = bcs_econd(Delta_B2, E_B2, V_B2, rho_B2_vec)

print(f"  B2-only gap equation:")
print(f"    Converged: {conv_B2} ({niter_B2} iterations)")
print(f"    Delta_k = {Delta_B2}")
print(f"    Max Delta = {np.max(Delta_B2):.6f}")
print(f"    E_cond = {E_cond_B2_gap:.8f}")

# Also with 5-mode (B2+B1) and 8-mode
V_5 = V_8[np.ix_([0,1,2,3,4], [0,1,2,3,4])]
E_5 = E_8[[0,1,2,3,4]]
rho_5 = np.array([rho_B2_per_mode]*4 + [1.0])
Delta_5, conv_5, niter_5 = solve_bcs_gap(V_5, E_5, rho_5, mu=0.0)
E_cond_5_gap = bcs_econd(Delta_5, E_5, V_5, rho_5)

print(f"\n  5-mode (B2+B1) gap equation:")
print(f"    Converged: {conv_5} ({niter_5} iterations)")
print(f"    Delta_k = {Delta_5}")
print(f"    Max Delta = {np.max(Delta_5):.6f}")
print(f"    E_cond = {E_cond_5_gap:.8f}")

rho_8 = np.array([rho_B2_per_mode]*4 + [1.0, 1.0, 1.0, 1.0])
Delta_8, conv_8, niter_8 = solve_bcs_gap(V_8, E_8, rho_8, mu=0.0)
E_cond_8_gap = bcs_econd(Delta_8, E_8, V_8, rho_8)

print(f"\n  8-mode (full) gap equation:")
print(f"    Converged: {conv_8} ({niter_8} iterations)")
print(f"    Delta_k = {Delta_8}")
print(f"    Max Delta = {np.max(Delta_8):.6f}")
print(f"    E_cond = {E_cond_8_gap:.8f}")

# Now compute S_inst for each case
# For each: construct the BCS free energy landscape, find minimum, integrate

def compute_instanton(V_mat, E_vec, rho_vec, label, mu=0.0, n_alpha=10001, alpha_max=3.0):
    """Compute S_inst via alpha-parametrization of multi-mode BCS gap.

    Solves the self-consistent gap equation for Delta_k, then computes
    F(alpha) where Delta_k(alpha) = alpha * Delta_k^{SC}.
    The instanton action is integral_0^{alpha_0} sqrt(2*V(alpha)) dalpha * Delta_max.
    """
    xi = E_vec - mu
    n = len(E_vec)

    # Solve gap equation
    Delta_gap = np.ones(n) * 0.1
    for it in range(5000):
        E_qp = np.sqrt(xi**2 + Delta_gap**2)
        Delta_new = np.zeros(n)
        for k in range(n):
            for kp in range(n):
                Delta_new[k] += V_mat[k, kp] * np.sqrt(rho_vec[k] * rho_vec[kp]) * Delta_gap[kp] / (2.0 * E_qp[kp])
        diff = np.max(np.abs(Delta_new - Delta_gap))
        Delta_gap = Delta_new.copy()
        if diff < 1e-14:
            break

    D_max = np.max(Delta_gap)
    if D_max < 1e-10:
        return {
            'label': label, 'Delta_0': 0.0, 'F_min': 0.0,
            'barrier': 0.0, 'S_inst': 0.0,
            'alpha_arr': np.linspace(0, alpha_max, n_alpha),
            'F_arr': np.zeros(n_alpha), 'status': 'NO_GAP',
            'Delta_gap': Delta_gap,
        }

    # Compute F(alpha) along the instanton path
    alpha_arr = np.linspace(0, alpha_max, n_alpha)
    F_arr = np.zeros(n_alpha)

    for i, alpha in enumerate(alpha_arr):
        Delta = alpha * Delta_gap
        E_qp = np.sqrt(xi**2 + Delta**2)
        # Kinetic: NO DOS factor (discrete-mode)
        F_kin = np.sum(E_qp - np.abs(xi))
        F_pair = 0.0
        for k in range(n):
            for kp in range(n):
                F_pair -= V_mat[k, kp] * np.sqrt(rho_vec[k] * rho_vec[kp]) * Delta[k] * Delta[kp] / (4.0 * E_qp[k] * E_qp[kp])
        F_arr[i] = F_kin + F_pair

    idx_min = np.argmin(F_arr)
    if idx_min == 0:
        return {
            'label': label, 'Delta_0': 0.0, 'F_min': 0.0,
            'barrier': 0.0, 'S_inst': 0.0,
            'alpha_arr': alpha_arr, 'F_arr': F_arr, 'status': 'NO_MIN',
            'Delta_gap': Delta_gap,
        }

    alpha_0 = alpha_arr[idx_min]
    F_min = F_arr[idx_min]
    Delta_0 = alpha_0 * D_max
    barrier = -F_min

    # Numerical instanton action: S = integral sqrt(2*(F-F_min)) * D_max * dalpha
    F_shifted = F_arr[:idx_min+1] - F_min
    integrand = np.sqrt(2.0 * np.maximum(0, F_shifted))
    S_inst = trapezoid(integrand, alpha_arr[:idx_min+1]) * D_max

    # GL fit in alpha space
    mask = (alpha_arr > 0.01) & (alpha_arr < alpha_max * 0.9)
    x = alpha_arr[mask]
    y = F_arr[mask]
    A_fit = np.column_stack([x**2, x**4])
    c, _, _, _ = np.linalg.lstsq(A_fit, y, rcond=None)
    a_gl, b_gl = c

    if b_gl > 0 and a_gl < 0:
        alpha_0_gl = np.sqrt(-a_gl / (2*b_gl))
        D0_gl = alpha_0_gl * D_max
        S_gl = np.sqrt(2*b_gl) * (2.0/3.0) * alpha_0_gl**3 * D_max
        barrier_gl = a_gl**2 / (4*b_gl)
    else:
        D0_gl = Delta_0
        S_gl = S_inst
        barrier_gl = barrier

    return {
        'label': label, 'Delta_0': Delta_0, 'F_min': F_min,
        'barrier': barrier, 'S_inst': S_inst,
        'a_gl': a_gl, 'b_gl': b_gl, 'D0_gl': D0_gl,
        'S_gl': S_gl, 'barrier_gl': barrier_gl,
        'alpha_arr': alpha_arr, 'F_arr': F_arr, 'status': 'OK',
        'Delta_gap': Delta_gap, 'alpha_0': alpha_0,
    }

configs = [
    ("B2-only (4 modes, conservative)", V_B2, E_B2, rho_B2_vec),
    ("B2+B1 (5 modes)", V_5, E_5, rho_5),
    ("Full (8 modes)", V_8, E_8, rho_8),
]

inst_results = {}
for label, V_mat, E_vec, rho_vec in configs:
    res = compute_instanton(V_mat, E_vec, rho_vec, label, alpha_max=3.0)
    inst_results[label] = res
    print(f"\n  {label}:")
    print(f"    Status: {res['status']}")
    if res['status'] == 'OK':
        print(f"    Delta_0 = {res['Delta_0']:.6f}")
        print(f"    Barrier = {res['barrier']:.8f}")
        print(f"    S_inst (numerical) = {res['S_inst']:.6f}")
        print(f"    S_inst (GL) = {res['S_gl']:.6f}")
        print(f"    a_GL = {res['a_gl']:.8f}, b_GL = {res['b_gl']:.8f}")
    else:
        print(f"    No BCS condensation (Delta_0 = 0)")


# ======================================================================
#  STEP 4: Coherence Length
# ======================================================================

print("\n" + "=" * 78)
print("STEP 4: BCS Coherence Length")
print("=" * 78)

print("""
  The BCS coherence length is:

    xi_BCS = v_F / (pi * Delta_0)                                     (9)

  In nuclear physics (Nazarewicz papers 02, 03), the coherence length
  determines whether the system is in the BCS regime (xi >> d, where d
  is the inter-particle spacing) or the BEC regime (xi << d).

  For the B2 flat-band system:
  - v_F = 0.01174 (Fermi velocity at physical fold, from VH-IMP-35a)
  - The "inter-particle spacing" is set by the mode spacing in the
    B2 quartet: delta_E ~ B2_bandwidth / N_B2 = 0.0579 / 4 = 0.0145.

  BUT: the B2 band is nearly flat (v -> 0 at the fold).
  The relevant velocity is NOT v_F = dE/dk at a generic k-point,
  but the velocity at the Fermi surface (which is AT the fold,
  where v = 0 by definition of the van Hove singularity).

  This is the key subtlety: at a van Hove singularity, v_F -> 0
  and xi_BCS -> 0. The system is driven toward the BCS-BEC crossover
  precisely because the coherence length shrinks.

  For a 1D van Hove: E(k) ~ E_fold + (1/2)*d2E*k^2
  => v(k) = dE/dk = d2E * k
  At the Fermi energy E_F: k_F = sqrt(2*(E_F - E_fold)/d2E)
  Since mu = 0 and E_B2 = 0.845:
  For the van Hove peak: the relevant velocity scale is
    v_eff = sqrt(2 * B2_bw * d2E) (geometric mean)
  or better: v_eff from the inverse DOS:
    rho ~ 1/v => v_eff = 1/rho
""")

# Fermi velocity estimates
# 1. From VH arbiter directly
v_F_arbiter = v_F

# 2. From inverse DOS: v_eff = 1/(rho_per_mode) in the van Hove region
# rho = dn/dE. For the flat band: rho ~ 1/v. So v ~ 1/rho.
v_F_invdos = 1.0 / rho_B2_per_mode

# 3. From dispersion curvature at fold
# E(k) = E_fold + d2E * k^2 / 2. The velocity at distance delta_k from fold:
# v(delta_k) = d2E * delta_k
# At the edge of the pairing window (delta_E ~ Delta_0):
# delta_k ~ sqrt(2*Delta_0 / d2E)
# v_eff ~ d2E * sqrt(2*Delta_0 / d2E) = sqrt(2 * Delta_0 * d2E)

# Use the numerical Delta_0 from Method D
Delta_0_best = Delta_0_num if abs(Delta_0_num) > 1e-8 else Delta_0_peak
v_F_fold = np.sqrt(2.0 * Delta_0_best * d2E_fold)

# 4. From B2 bandwidth / N_B2 (crude estimate)
v_F_bw = B2_bw / 4.0

print(f"  Fermi velocity estimates:")
print(f"    v_F (VH arbiter) = {v_F_arbiter:.6f}")
print(f"    v_F (1/rho)      = {v_F_invdos:.6f}")
print(f"    v_F (fold, sqrt(2*Delta*d2E)) = {v_F_fold:.6f}")
print(f"    v_F (bandwidth/N) = {v_F_bw:.6f}")

# Coherence lengths
for label, vf in [("VH arbiter", v_F_arbiter),
                   ("1/rho", v_F_invdos),
                   ("fold", v_F_fold),
                   ("BW/N", v_F_bw)]:
    xi_bcs = vf / (np.pi * Delta_0_best) if abs(Delta_0_best) > 1e-8 else float('inf')
    print(f"    xi_BCS ({label:>12s}) = {xi_bcs:.6f}")

# "Inter-particle spacing" for BCS vs BEC comparison
# In the B2 sector with 4 modes, the effective mode spacing is:
d_eff = 1.0 / (4 * rho_B2_per_mode)  # 1 / (total DOS)
print(f"\n  Effective inter-particle spacing: d_eff = 1/(N_B2*rho) = {d_eff:.6f}")
xi_bcs_best = v_F_fold / (np.pi * Delta_0_best)
print(f"  xi_BCS / d_eff = {xi_bcs_best / d_eff:.4f}")
print(f"  (BCS regime: ratio >> 1; BEC regime: ratio << 1)")

# BCS-BEC crossover parameter: g * N(0)
gN0 = M_max_AUTH
print(f"\n  BCS-BEC crossover parameter: g*N(0) = M_max = {gN0:.4f}")
print(f"  (Weak coupling: g*N(0) << 1; Crossover: g*N(0) ~ 1; BEC: g*N(0) >> 1)")
print(f"  This system is in the BCS-BEC CROSSOVER regime (g*N(0) = 1.674)")


# ======================================================================
#  STEP 5: Instanton in the tau (deformation) direction
# ======================================================================

print("\n" + "=" * 78)
print("STEP 5: Instanton in the tau direction")
print("=" * 78)

print("""
  The instanton computed above is for Delta fluctuations at FIXED tau.
  But in the framework, tau itself is a dynamical variable (the modulus
  field). There is a SECOND instanton problem: can the system tunnel
  from the BCS minimum at tau_fold to the normal phase at tau >> tau_fold?

  This tau-direction instanton is controlled by the spectral action
  landscape S(tau), which from SC-HFB-36 is MONOTONICALLY INCREASING.
  There is no second minimum in tau-space to tunnel TO, so this
  instanton is not relevant.

  The ONLY instanton that matters is the Delta-direction one computed
  above: tunneling between +Delta_0 and -Delta_0 at fixed tau.
  (Or equivalently, between Delta_0 and the false vacuum at Delta=0.)

  Nuclear analogy: In nuclear DFT (Nazarewicz paper 13, GCM),
  the collective coordinate is the deformation parameter beta.
  The GCM wavefunction can tunnel between prolate and oblate minima
  through a spherical saddle point. The instanton action for this
  shape tunneling is S ~ (barrier height) * (mass parameter) * width.
  For shape coexistence in Hg isotopes, S ~ 5-10, giving significant
  but not overwhelming tunneling.

  Here, the B2 Delta-space instanton plays the same role:
  it determines whether the two Z_2 vacua (Delta and -Delta)
  are well-separated (dilute instantons) or strongly mixed
  (dense instanton gas).
""")


# ======================================================================
#  STEP 6: Summary and Gate Verdict
# ======================================================================

print("\n" + "=" * 78)
print("STEP 6: Summary and Gate Verdict")
print("=" * 78)

# Collect all S_inst values
print(f"\n  Instanton action summary:")
print(f"  {'Method':<45s}  {'S_inst':>8s}  {'Delta_0':>8s}  {'Barrier':>10s}")
print(f"  {'-'*45}  {'-'*8}  {'-'*8}  {'-'*10}")

methods = [
    ("A: E_cond + Delta_0 (peak)", S_inst_A, Delta_0_peak, barrier_A),
    ("B: Thouless (M_max=1.674)", S_inst_B, Delta_0_peak, barrier_B),
    ("C: Numerical GL fit (B2)", S_inst_C, Delta_0_C, barrier_C),
    ("D: Direct numerical (B2)", S_inst_D, Delta_0_num, barrier_D),
]

# Add multi-sector results
for label, res in inst_results.items():
    if res['status'] == 'OK':
        methods.append((f"MS: {label}", res['S_inst'], res['Delta_0'], res['barrier']))

for label, s, d0, bar in methods:
    if s > 0:
        print(f"  {label:<45s}  {s:8.4f}  {d0:8.4f}  {bar:10.6f}")
    else:
        print(f"  {label:<45s}  {'N/A':>8s}  {'N/A':>8s}  {'N/A':>10s}")

# Best estimate with uncertainty
S_inst_values = [s for _, s, _, _ in methods if s > 0]
if S_inst_values:
    S_inst_mean = np.mean(S_inst_values)
    S_inst_min = np.min(S_inst_values)
    S_inst_max = np.max(S_inst_values)
    S_inst_best = S_inst_D  # Most rigorous (full numerical)
else:
    S_inst_mean = 0.0
    S_inst_min = 0.0
    S_inst_max = 0.0
    S_inst_best = 0.0

print(f"\n  Best estimate (Method D, full numerical): S_inst = {S_inst_best:.6f}")
print(f"  Range across methods: [{S_inst_min:.4f}, {S_inst_max:.4f}]")
print(f"  Mean: {S_inst_mean:.4f}")

# Gate verdict
print(f"\n  PRE-REGISTERED CRITERIA:")
print(f"    S_inst < 0.5  -> Dense instanton gas, Z_2 restored")
print(f"    0.5 < S_inst < 5 -> Crossover regime")
print(f"    S_inst > 5    -> Dilute instantons, mean-field BCS")

if S_inst_best < 0.5:
    verdict = "DENSE GAS"
    verdict_detail = (f"S_inst = {S_inst_best:.4f} < 0.5. Dense instanton gas. "
                     f"Z_2 symmetry is restored by tunneling. "
                     f"The BCS ground state is a superposition of +Delta and -Delta. "
                     f"Virtual particle picture applies.")
elif S_inst_best < 5.0:
    verdict = "CROSSOVER"
    verdict_detail = (f"S_inst = {S_inst_best:.4f} in [0.5, 5]. Crossover regime. "
                     f"Tunneling is neither negligible nor dominant. "
                     f"Both Z_2 vacua contribute significantly.")
else:
    verdict = "DILUTE"
    verdict_detail = (f"S_inst = {S_inst_best:.4f} > 5. Dilute instantons. "
                     f"Standard mean-field BCS applies. Z_2 is well-broken.")

print(f"\n  *** GATE INST-37a: {verdict} ***")
print(f"  {verdict_detail}")

# Physical interpretation
print(f"\n  PHYSICAL INTERPRETATION:")
print(f"    Tunnel splitting / attempt frequency ~ exp(-S_inst) = {np.exp(-S_inst_best):.4e}")
print(f"    For S_inst = {S_inst_best:.4f}:")
if S_inst_best < 0.5:
    print(f"    exp(-S) = {np.exp(-S_inst_best):.4f} ~ O(1)")
    print(f"    Tunneling rate is comparable to the BCS pairing frequency.")
    print(f"    The system samples both Z_2 vacua on the pairing timescale.")
    print(f"    This confirms the 'virtual particle' picture from Session 36:")
    print(f"    pair fluctuations (instantons) are the dominant excitations.")
elif S_inst_best < 5.0:
    print(f"    exp(-S) = {np.exp(-S_inst_best):.4f}")
    print(f"    Tunneling is suppressed but not negligible.")
    print(f"    The system has long-lived Z_2 domains with occasional tunneling.")
else:
    print(f"    exp(-S) = {np.exp(-S_inst_best):.4e}")
    print(f"    Tunneling is exponentially suppressed.")
    print(f"    The mean-field BCS vacuum is stable against Z_2 fluctuations.")

# Nuclear benchmark
print(f"\n  NUCLEAR BENCHMARK:")
print(f"    In ^{208}Pb (doubly magic, zero pairing gap): S_inst = 0 (no condensate)")
print(f"    In ^{120}Sn (mid-shell, Delta ~ 1.3 MeV): S_inst >> 5 (deep BCS)")
print(f"    In ^{18}O (2 valence neutrons, Delta/xi ~ 0.1): S_inst ~ 1-3")
print(f"    The framework system (N_pair=1, Delta/xi ~ {Delta_0_best/E_B2[0]:.3f}) most resembles")
print(f"    the ^{18}O case: a few-body system near the BCS-BEC crossover.")

# Coherence length summary
print(f"\n  COHERENCE LENGTH SUMMARY:")
xi_bcs_final = v_F_fold / (np.pi * Delta_0_best)
print(f"    xi_BCS = v_F / (pi * Delta_0) = {xi_bcs_final:.6f}")
print(f"    (using v_F at fold = {v_F_fold:.6f})")
print(f"    xi_BCS / system_size ~ {xi_bcs_final:.4f}")
print(f"    For comparison: B2 bandwidth = {B2_bw:.4f}")
print(f"    xi_BCS / BW = {xi_bcs_final / B2_bw:.4f}")


# ======================================================================
#  PLOT
# ======================================================================

fig, axes = plt.subplots(2, 3, figsize=(20, 12))

# Panel 1: BCS free energy landscape (alpha parametrization)
ax = axes[0, 0]
ax.plot(alpha_scan, F_alpha, 'b-', lw=2, label='F(alpha) along gap path')
ax.axhline(0, color='gray', ls='--', lw=1)
ax.axvline(alpha_min, color='red', ls='--', lw=1.5, label=f'alpha_0 = {alpha_min:.3f}')
ax.axhline(F_min, color='green', ls=':', lw=1.5, label=f'E_cond = {F_min:.4f}')
# GL fit
F_GL_plot = a_C_alpha * alpha_scan**2 + b_C_alpha * alpha_scan**4
ax.plot(alpha_scan, F_GL_plot, 'r:', lw=1.5, alpha=0.7, label='GL fit')
ax.set_xlabel('alpha (scaling factor)')
ax.set_ylabel('F_BCS')
ax.set_title(f'BCS Free Energy (Delta_max = {Delta_max_SC:.4f})')
ax.set_xlim(0, 3.0)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Instanton integrand
ax = axes[0, 1]
d_inst_plot = delta_scan[:idx_min+1]
V_inst_plot = np.maximum(0, F_BCS[:idx_min+1] - F_min)
integrand_plot = np.sqrt(2.0 * V_inst_plot)
ax.fill_between(d_inst_plot, integrand_plot, alpha=0.3, color='steelblue',
                label=f'S_inst = {S_inst_D:.4f}')
ax.plot(d_inst_plot, integrand_plot, 'b-', lw=2)
ax.axvline(Delta_0_num, color='red', ls='--', lw=1.5)
ax.set_xlabel('Delta = alpha * Delta_max_SC')
ax.set_ylabel('sqrt(2V(Delta))')
ax.set_title(f'Instanton Integrand (S_inst = {S_inst_D:.4f})')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 3: Instanton action vs method
ax = axes[0, 2]
valid_methods = [(l, s) for l, s, _, _ in methods if s > 0]
if valid_methods:
    names = [m[0].split(':')[1].strip()[:25] for m in valid_methods]
    vals = [m[1] for m in valid_methods]
    colors = ['green' if v < 0.5 else ('orange' if v < 5 else 'red') for v in vals]
    bars = ax.barh(range(len(vals)), vals, color=colors, alpha=0.7, edgecolor='black')
    ax.set_yticks(range(len(vals)))
    ax.set_yticklabels(names, fontsize=8)
    ax.axvline(0.5, color='green', ls='--', lw=2, label='Dense gas boundary')
    ax.axvline(5.0, color='red', ls='--', lw=2, label='Dilute boundary')
    for i, v in enumerate(vals):
        ax.text(v + 0.02, i, f'{v:.3f}', va='center', fontsize=8)
    ax.set_xlabel('S_inst')
    ax.set_title('Instanton Action by Method')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, axis='x')

# Panel 4: Multi-sector F_BCS landscapes (alpha parametrization)
ax = axes[1, 0]
for label, res in inst_results.items():
    if res['status'] == 'OK':
        short_label = label.split('(')[0].strip()
        ax.plot(res['alpha_arr'], res['F_arr'], lw=2, label=short_label)
ax.axhline(0, color='gray', ls='--', lw=1)
ax.set_xlabel('alpha (scaling factor)')
ax.set_ylabel('F_BCS')
ax.set_title('BCS Free Energy: Multi-Sector Comparison')
ax.set_xlim(0, 3.0)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: GL potential (shifted, along alpha path)
ax = axes[1, 1]
F_shifted_plot = F_alpha - F_min
ax.plot(alpha_scan, F_shifted_plot, 'b-', lw=2, label='V(alpha) (numerical)')
# GL version
if b_C_alpha > 0:
    alpha_0_gl_plot = np.sqrt(-a_C_alpha / (2*b_C_alpha)) if a_C_alpha < 0 else alpha_min
    V_GL_plot = b_C_alpha * (alpha_scan**2 - alpha_0_gl_plot**2)**2
else:
    V_GL_plot = np.zeros_like(alpha_scan)
ax.plot(alpha_scan, V_GL_plot, 'r:', lw=1.5, alpha=0.7, label='V(alpha) (GL)')
ax.axhline(0, color='gray', ls='--', lw=1)
ax.axvline(alpha_min, color='red', ls='--', lw=1.5, alpha=0.5)
ax.set_xlabel('alpha')
ax.set_ylabel('V(alpha) - V(alpha_0)')
ax.set_title('GL Potential (Z_2 Double Well)')
ax.set_xlim(-0.1, 3.0)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Regime classification
ax = axes[1, 2]
S_range = np.linspace(0, 8, 1000)
tunneling = np.exp(-S_range)
ax.plot(S_range, tunneling, 'k-', lw=2)
ax.axvspan(0, 0.5, alpha=0.15, color='green', label='Dense gas (Z_2 restored)')
ax.axvspan(0.5, 5.0, alpha=0.15, color='yellow', label='Crossover')
ax.axvspan(5.0, 8.0, alpha=0.15, color='red', label='Dilute (mean-field BCS)')

# Mark our values
for label, s, _, _ in methods:
    if s > 0 and s < 8:
        short = label.split(':')[0]
        ax.axvline(s, color='blue', ls='--', lw=1, alpha=0.5)

ax.axvline(S_inst_best, color='blue', ls='-', lw=3, alpha=0.8,
           label=f'Best: S = {S_inst_best:.3f}')
ax.set_xlabel('S_inst')
ax.set_ylabel('exp(-S_inst)')
ax.set_title('Instanton Regime Classification')
ax.set_yscale('log')
ax.set_ylim(1e-4, 2)
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3)

fig.suptitle(f'F.1 Instanton Action: INST-37a = {verdict} | '
             f'S_inst = {S_inst_best:.4f} | '
             f'Delta_0 = {Delta_0_best:.4f} | '
             f'Barrier = {barrier_D:.6f}',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.96])
out_png = os.path.join(SCRIPT_DIR, 's37_instanton_action.png')
plt.savefig(out_png, dpi=150)
plt.close()
print(f"\nPlot saved: {out_png}")


# ======================================================================
#  SAVE
# ======================================================================

save_dict = {
    # Gate verdict
    'verdict': np.array([verdict]),
    'S_inst_best': S_inst_best,
    'S_inst_min': S_inst_min,
    'S_inst_max': S_inst_max,
    'S_inst_mean': S_inst_mean,
    'tunneling_rate': np.exp(-S_inst_best),

    # GL coefficients (Method A)
    'a_A': a_A,
    'b_A': b_A,
    'barrier_A': barrier_A,
    'S_inst_A': S_inst_A,

    # GL coefficients (Method B: Thouless)
    'a_B': a_B,
    'b_B': b_B,
    'barrier_B': barrier_B,
    'S_inst_B': S_inst_B,

    # GL coefficients (Method C: numerical fit)
    'a_C': a_C,
    'b_C': b_C,
    'barrier_C': barrier_C,
    'S_inst_C': S_inst_C,

    # Method D: direct numerical
    'Delta_0_num': Delta_0_num,
    'barrier_D': barrier_D,
    'S_inst_D': S_inst_D,

    # Physical parameters
    'Delta_0_peak': Delta_0_peak,
    'Delta_0_020': Delta_0_020,
    'E_cond_full': E_cond_full,
    'E_cond_use': E_cond_use,
    'rho_B2_per_mode': rho_B2_per_mode,
    'v_F_arbiter': v_F_arbiter,
    'v_F_fold': v_F_fold,
    'v_F_invdos': v_F_invdos,
    'M_max_AUTH': M_max_AUTH,
    'M_max_8x8_ED': M_max_8x8,
    'M_max_B2only': M_max_B2only,
    'tau_fold': tau_fold,
    'tau_peak': tau_peak,
    'E_fold': E_fold,
    'B2_bw': B2_bw,
    'd2E_fold': d2E_fold,

    # Coherence length
    'xi_BCS': xi_bcs_final,
    'xi_BCS_over_BW': xi_bcs_final / B2_bw if B2_bw > 0 else 0.0,

    # Gap equation solutions
    'Delta_B2_gap': Delta_B2,
    'Delta_5_gap': Delta_5,
    'Delta_8_gap': Delta_8,
    'E_cond_B2_gap': E_cond_B2_gap,
    'E_cond_5_gap': E_cond_5_gap,
    'E_cond_8_gap': E_cond_8_gap,

    # Free energy landscape (B2)
    'delta_scan': delta_scan,
    'F_BCS_B2': F_BCS,

    # Multi-sector instanton results
    'S_inst_B2only': inst_results.get("B2-only (4 modes, conservative)", {}).get('S_inst', 0.0),
    'S_inst_B2B1': inst_results.get("B2+B1 (5 modes)", {}).get('S_inst', 0.0),
    'S_inst_full': inst_results.get("Full (8 modes)", {}).get('S_inst', 0.0),
}

out_npz = os.path.join(SCRIPT_DIR, 's37_instanton_action.npz')
np.savez_compressed(out_npz, **save_dict)
print(f"\nSaved: {out_npz}")
print(f"File size: {os.path.getsize(out_npz) / 1024:.1f} KB")


# ======================================================================
#  FINAL SUMMARY
# ======================================================================

elapsed = time.time() - t0
print(f"\n{'='*78}")
print(f"F.1 INSTANTON ACTION FINAL: {verdict}")
print(f"{'='*78}")
print(f"\n  S_inst (best, direct numerical) = {S_inst_best:.6f}")
print(f"  S_inst range = [{S_inst_min:.4f}, {S_inst_max:.4f}]")
print(f"  Delta_0 = {Delta_0_best:.6f}")
print(f"  Barrier = {barrier_D:.8f}")
print(f"  Tunneling rate ~ exp(-S) = {np.exp(-S_inst_best):.4e}")
print(f"  xi_BCS = {xi_bcs_final:.6f}")
print(f"  g*N(0) = {M_max_AUTH:.4f} (BCS-BEC crossover regime)")
print(f"\n  N_pair = 1 (ED). This is a FEW-BODY system, not thermodynamic BCS.")
print(f"  The instanton gas picture is the correct physical description.")
print(f"\n  Runtime: {elapsed:.1f}s")
print(f"{'='*78}")
