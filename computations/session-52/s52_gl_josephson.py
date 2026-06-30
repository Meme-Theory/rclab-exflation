#!/usr/bin/env python3
"""
S52 GL-JOSEPHSON-52: Ginzburg-Landau Fabric Dynamical Matrix
=============================================================

Physics:
  The BCS condensate on M^4 x SU(3) has 3 sectors (B1, B2, B3), each with
  a complex order parameter Delta_alpha = |Delta_alpha| * exp(i*theta_alpha).
  On the 32-cell Voronoi tessellation, cells are Josephson-coupled through
  directional stiffnesses (J_C2, J_su2, J_u1).

  Small fluctuations around the BCS ground state yield 6 DOF per cell:
    3 amplitudes (Higgs-like) + 3 phases (1 Goldstone + 2 Leggett)

  The equation of motion is T * d^2 q / dt^2 = -V * q, so
  the eigenfrequencies satisfy det(V - omega^2 T) = 0.
  This is a GENERALIZED eigenvalue problem: V*x = omega^2 * T * x.

  T is the inertia matrix:
    - Phase sector: T_theta = diag(rho_alpha * Delta_alpha^2)
      (number susceptibility -- the Anderson-Bogoliubov mass)
    - Amplitude sector: T_rho = diag(rho_alpha)
      (compressibility -- DOS at Fermi level)

  V is the stiffness matrix (from second derivatives of F_GL + F_J).

Method:
  1. GL free energy: F_GL = sum_alpha [a_alpha |Delta_alpha|^2 + b_alpha |Delta_alpha|^4]
     plus inter-sector Josephson: F_J = -J_ij |Delta_i||Delta_j| cos(theta_i - theta_j)
  2. Ground state: minimize F_GL to get Delta_alpha^(0)
  3. Expand to quadratic order in fluctuations
  4. Build stiffness V(K) and inertia T(K) on BCC lattice
  5. Solve generalized eigenvalue problem at each K

Gate: GL-JOSEPHSON-52
  PASS: |alpha_eff - 2| > 0.05 at K < 0.2 M_KK for at least one branch
  FAIL: All modes K^2

Author: Landau-Condensed-Matter-Theorist (S52)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, cos, sin
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# Import canonical constants
# ============================================================
from canonical_constants import (
    a_GL, b_GL, Delta_0_GL, Delta_B3,
    J_C2, J_su2, J_u1, N_cells, c_fabric,
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    xi_BCS, xi_GL, omega_PV, tau_fold,
    E_cond, M_max_thouless, Vol_SU3_Haar
)

print("=" * 70)
print("S52 GL-JOSEPHSON-52: Ginzburg-Landau Fabric Dynamical Matrix")
print("=" * 70)

# ============================================================
# Section 1: Ground state from S48 data
# ============================================================
print("\n--- Section 1: Ground state from S48 Leggett mode data ---")

leggett_data = np.load(os.path.join(os.path.dirname(__file__),
                        "s48_leggett_mode.npz"), allow_pickle=True)

# Ground state at tau_fold
Delta_0 = leggett_data['Delta_fold']   # [Delta_B1, Delta_B2, Delta_B3]
rho_0 = leggett_data['rho_fold']        # [rho_B1, rho_B2, rho_B3]

# Inter-sector Josephson (same cell, different sectors)
J_12_micro = float(leggett_data['J_12_fold'])
J_23_micro = float(leggett_data['J_23_fold'])
J_13_micro = float(leggett_data['J_13_fold'])

# S48 Leggett frequencies for validation
omega_L1_s48 = float(leggett_data['omega_L1_fold'])
omega_L2_s48 = float(leggett_data['omega_L2_fold'])
evals_s48 = leggett_data['evals_fold']  # [0, eval_L1, eval_L2]

print(f"  Delta_0 = [{Delta_0[0]:.6f}, {Delta_0[1]:.6f}, {Delta_0[2]:.6f}] M_KK")
print(f"  rho_0   = [{rho_0[0]:.4f}, {rho_0[1]:.4f}, {rho_0[2]:.4f}]")
print(f"  J_12 = {J_12_micro:.6f}, J_23 = {J_23_micro:.6f}, J_13 = {J_13_micro:.6f}")
print(f"  omega_L1(S48) = {omega_L1_s48:.6f}, omega_L2(S48) = {omega_L2_s48:.6f}")
print(f"  S48 evals (phase sector) = {evals_s48}")

# ============================================================
# Section 2: GL coefficients per sector
# ============================================================
print("\n--- Section 2: GL free energy functional ---")

# GL coefficients: a_GL, b_GL are B2 reference values.
# For each sector: a_alpha ~ -1/rho_alpha (BCS), b from ground state.
a_alpha = np.zeros(3)
b_alpha = np.zeros(3)

a_alpha[1] = a_GL   # B2 reference
a_alpha[0] = a_GL * (rho_0[1] / rho_0[0])  # B1
a_alpha[2] = a_GL * (rho_0[1] / rho_0[2])  # B3

for i in range(3):
    b_alpha[i] = -a_alpha[i] / (2.0 * Delta_0[i]**2)

print(f"  GL coefficients:")
for i, lab in enumerate(['B1', 'B2', 'B3']):
    delta_check = sqrt(-a_alpha[i] / (2.0 * b_alpha[i]))
    print(f"    {lab}: a = {a_alpha[i]:.6f}, b = {b_alpha[i]:.6f}, "
          f"Delta_0 = {Delta_0[i]:.6f} (check: {delta_check:.6f})")

# Condensation energy per sector
F_0_sector = a_alpha * Delta_0**2 + b_alpha * Delta_0**4
print(f"\n  Condensation energy: {F_0_sector}")
print(f"  Total: {np.sum(F_0_sector):.6f}")

# ============================================================
# Section 3: Inertia (mass) matrices
# ============================================================
print("\n--- Section 3: Inertia matrices ---")

# Phase inertia: T_theta_alpha = rho_alpha * Delta_0_alpha^2
# This is the Anderson-Bogoliubov result: the phase dynamics
# involves the number susceptibility chi = dn/dmu = rho * Delta^2 / Delta^2 = rho
# More precisely: the EOM for theta is
#   rho_alpha * Delta_alpha^2 * d^2 theta_alpha / dt^2 = -dF/dtheta_alpha
# So T_theta_alpha = rho_alpha * Delta_alpha^2

T_phase = np.diag(rho_0 * Delta_0**2)

# Amplitude inertia: T_rho_alpha = rho_alpha
# The EOM for |Delta| involves the compressibility:
#   rho_alpha * d^2 |Delta_alpha| / dt^2 = -dF/d|Delta_alpha|
T_amp = np.diag(rho_0)

print(f"  Phase inertia (rho * Delta^2):")
for i, lab in enumerate(['B1', 'B2', 'B3']):
    val = rho_0[i] * Delta_0[i]**2
    print(f"    {lab}: {val:.6f}")

print(f"  Amplitude inertia (rho):")
for i, lab in enumerate(['B1', 'B2', 'B3']):
    print(f"    {lab}: {rho_0[i]:.6f}")

# ============================================================
# Section 4: Stiffness matrices at K=0
# ============================================================
print("\n--- Section 4: Stiffness (mass) matrices at K=0 ---")

# Amplitude stiffness: V_rho[i,i] = d^2F/d|Delta_i|^2 = -4*a_i (at minimum)
V_amp_0 = np.diag(-4.0 * a_alpha)  # = 2*a + 12*b*Delta^2 = -4*a at minimum
# Off-diagonal: inter-sector Josephson coupling to amplitudes
# d^2 F_J / d|Delta_i| d|Delta_j| = -J_ij cos(0) = -J_ij
V_amp_0[0, 1] = V_amp_0[1, 0] = -J_12_micro
V_amp_0[1, 2] = V_amp_0[2, 1] = -J_23_micro
V_amp_0[0, 2] = V_amp_0[2, 0] = -J_13_micro

print(f"  Amplitude stiffness V_amp(K=0):")
for i in range(3):
    print(f"    [{V_amp_0[i,0]:+.6f}  {V_amp_0[i,1]:+.6f}  {V_amp_0[i,2]:+.6f}]")

# Phase stiffness: standard Josephson coupling matrix
V_phase_0 = np.zeros((3, 3))
J_pairs = [(0, 1, J_12_micro), (1, 2, J_23_micro), (0, 2, J_13_micro)]
for (p, q, Jpq) in J_pairs:
    coupling = Jpq * Delta_0[p] * Delta_0[q]
    V_phase_0[p, p] += coupling
    V_phase_0[q, q] += coupling
    V_phase_0[p, q] = -coupling
    V_phase_0[q, p] = -coupling

print(f"\n  Phase stiffness V_phase(K=0):")
for i in range(3):
    print(f"    [{V_phase_0[i,0]:+.8f}  {V_phase_0[i,1]:+.8f}  {V_phase_0[i,2]:+.8f}]")

# ============================================================
# Section 5: Cross-check Leggett modes at K=0
# ============================================================
print("\n--- Section 5: Cross-check Leggett modes at K=0 ---")

# Solve generalized eigenvalue problem: V_phase * x = omega^2 * T_phase * x
evals_gen, evecs_gen = eigh(V_phase_0, T_phase)
print(f"  Generalized eigenvalues (omega^2): {evals_gen}")
print(f"  Frequencies:")
for i, ev in enumerate(evals_gen):
    if ev > 1e-15:
        print(f"    Mode {i}: omega = {sqrt(ev):.6f}")
    else:
        print(f"    Mode {i}: omega = 0 (Goldstone, eval = {ev:.2e})")

# Compare with S48
pos_evals = sorted([ev for ev in evals_gen if ev > 1e-15])
if len(pos_evals) >= 2:
    oL1 = sqrt(pos_evals[0])
    oL2 = sqrt(pos_evals[1])
    print(f"\n  Leggett cross-check:")
    print(f"    L1: here = {oL1:.6f}, S48 = {omega_L1_s48:.6f}, ratio = {oL1/omega_L1_s48:.4f}")
    print(f"    L2: here = {oL2:.6f}, S48 = {omega_L2_s48:.6f}, ratio = {oL2/omega_L2_s48:.4f}")

# Also check: amplitude sector generalized eigenvalues
evals_amp_gen, _ = eigh(V_amp_0, T_amp)
print(f"\n  Amplitude sector generalized eigenvalues (omega^2): {evals_amp_gen}")
print(f"  Amplitude frequencies: {np.sqrt(np.abs(evals_amp_gen))}")

# ============================================================
# Section 6: BCC lattice geometry
# ============================================================
print("\n--- Section 6: BCC lattice geometry ---")

V_cell = Vol_SU3_Haar / N_cells
a_BCC = (2.0 * V_cell) ** (1.0/3.0)  # BCC: 2 atoms per conventional cell
K_BZ = pi / a_BCC

print(f"  Vol(SU(3)) = {Vol_SU3_Haar:.2f}")
print(f"  V_cell = {V_cell:.4f}")
print(f"  a_BCC = {a_BCC:.4f}")
print(f"  K_BZ = pi/a = {K_BZ:.4f}")

# ============================================================
# Section 7: Structure factors
# ============================================================

def S_NN(K, a):
    """Angle-averaged NN dispersive factor for BCC.

    NN shell: 8 vectors a/2*(pm1,pm1,pm1).
    gamma_NN = cos(K_x a/2)*cos(K_y a/2)*cos(K_z a/2)
    <gamma_NN> = sinc^3(Ka/(2*pi)) where sinc(x)=sin(pi*x)/(pi*x)
    Actually: <gamma(K)> = [sin(Ka/2)/(Ka/2)]^3
    S = 1 - <gamma>.  # (local)
    """
    x = K * a / 2.0
    if np.isscalar(K):
        if abs(x) < 1e-12:
            return 0.0
        return 1.0 - (np.sin(x) / x)**3
    result = np.zeros_like(K, dtype=float)
    mask = np.abs(x) > 1e-12
    sx = np.where(mask, x, 1.0)
    result = np.where(mask, 1.0 - (np.sin(sx) / sx)**3, 0.0)
    return result


def S_NNN(K, a):
    """Angle-averaged NNN dispersive factor for BCC.

    NNN: 6 vectors a*(pm1,0,0) etc.
    <gamma_NNN> = sin(Ka)/(Ka)
    S = 1 - <gamma>.  # (local)
    """
    x = K * a
    if np.isscalar(K):
        if abs(x) < 1e-12:
            return 0.0
        return 1.0 - np.sin(x) / x
    result = np.zeros_like(K, dtype=float)
    mask = np.abs(x) > 1e-12
    sx = np.where(mask, x, 1.0)
    result = np.where(mask, 1.0 - np.sin(sx) / sx, 0.0)
    return result


# ============================================================
# Section 8: Build full 6x6 stiffness and inertia matrices
# ============================================================
print("\n--- Section 8: Dynamical matrix construction ---")

# The fabric Josephson couplings (J_C2, J_su2, J_u1) are the INTER-CELL
# phase stiffnesses. They produce K-dependent terms in the stiffness matrix.
#
# Bond structure on BCC-derived tessellation:
#   8 NN bonds: 4 along C^2 coset (J_C2) + 4 along other NN
#   6 NNN bonds: 3 along su(2) (J_su2) + 1 along u(1) (J_u1) + 2 others
#
# For each sector alpha, the inter-cell Josephson energy is:
#   F_fabric = -sum_<ij> J_bond * |Delta_alpha^(i)|^2 * cos(theta_alpha^(i) - theta_alpha^(j))
#
# This gives K-dependent additions to both phase and amplitude stiffnesses.
# Phase: V_phase += Delta_0^2 * J_eff(K) where J_eff(K) = sum of bond J * S(K)
# Amplitude: V_amp += J_eff(K) (gradient stiffness for |Delta|)

# Effective fabric Josephson coupling vs K:
# J_eff(K) = 4*J_C2*S_NN(K) + (3*J_su2 + J_u1)*S_NNN(K) + remaining bonds
# The remaining 4 NN bonds and 2 NNN bonds have intermediate couplings.
# Conservative: assign remaining NN at geometric mean of J_C2 and J_su2,
# remaining NNN at J_u1.

# Weighted average for remaining bonds
J_NN_other = sqrt(J_C2 * J_su2)  # geometric mean for remaining 4 NN
J_NNN_other = J_u1               # remaining 2 NNN at softest coupling

def J_eff_K(K, a):
    """Total effective fabric Josephson stiffness at wavevector K."""
    snn = S_NN(K, a)
    snnn = S_NNN(K, a)
    # 4 C2-bonds (NN) + 4 other NN + 3 su2-bonds (NNN) + 1 u1-bond + 2 other NNN
    return (4.0*J_C2 + 4.0*J_NN_other)*snn + (3.0*J_su2 + J_u1 + 2.0*J_NNN_other)*snnn


def build_stiffness_inertia(K, a):
    """Build 6x6 stiffness V(K) and inertia T (K-independent).

    Ordering: [|Delta_B1|, |Delta_B2|, |Delta_B3|, theta_B1, theta_B2, theta_B3]
    """
    V = np.zeros((6, 6))
    T = np.zeros((6, 6))

    jeff = J_eff_K(K, a)

    # --- Amplitude block (upper-left 3x3) ---
    for i in range(3):
        V[i, i] = -4.0 * a_alpha[i] + jeff * Delta_0[i]**2
        T[i, i] = rho_0[i]
    # Amplitude off-diagonal (inter-sector Josephson)
    V[0, 1] = V[1, 0] = -J_12_micro
    V[1, 2] = V[2, 1] = -J_23_micro
    V[0, 2] = V[2, 0] = -J_13_micro

    # --- Phase block (lower-right 3x3) ---
    # Inter-sector Josephson (K=0 contribution)
    for (p, q, Jpq) in J_pairs:
        coupling = Jpq * Delta_0[p] * Delta_0[q]
        V[3+p, 3+p] += coupling
        V[3+q, 3+q] += coupling
        V[3+p, 3+q] -= coupling
        V[3+q, 3+p] -= coupling

    # Fabric gradient contribution to phase stiffness
    for i in range(3):
        V[3+i, 3+i] += jeff * Delta_0[i]**2

    # Phase inertia
    for i in range(3):
        T[3+i, 3+i] = rho_0[i] * Delta_0[i]**2

    # --- Cross-coupling ---
    # At the aligned ground state (all theta=0, real Delta_0),
    # d^2F/(d|Delta_i| dtheta_j) = 0 by U(1) symmetry.
    # No amplitude-phase cross terms.

    return V, T


# ============================================================
# Section 9: Dispersion calculation
# ============================================================
print("\n--- Section 9: Dispersion omega(K) ---")

N_K = 50  # (local)
K_array = np.linspace(0, K_BZ, N_K + 1)
K_array[0] = 1e-8  # Regularize K=0

omega_sq_all = np.zeros((N_K + 1, 6))
omega_all = np.zeros((N_K + 1, 6))
evecs_all = np.zeros((N_K + 1, 6, 6))

for ik, K in enumerate(K_array):
    V_K, T_K = build_stiffness_inertia(K, a_BCC)

    # Generalized eigenvalue problem: V*x = omega^2 * T * x
    # scipy.linalg.eigh(V, T) returns eigenvalues in ascending order
    evals, evecs = eigh(V_K, T_K)

    omega_sq_all[ik] = evals
    evecs_all[ik] = evecs

    # Convert to frequencies
    for ib in range(6):
        if evals[ib] >= 0:
            omega_all[ik, ib] = sqrt(evals[ib])
        else:
            omega_all[ik, ib] = -sqrt(-evals[ib])

# Restore K=0 for plotting
K_plot = np.linspace(0, K_BZ, N_K + 1)

print(f"  K range: [0, {K_BZ:.4f}] ({N_K+1} points)")
print(f"\n  Dispersion at K=0:")
for ib in range(6):
    print(f"    Branch {ib}: omega(0) = {omega_all[0,ib]:.6f}, "
          f"omega^2 = {omega_sq_all[0,ib]:.6e}")

print(f"\n  Dispersion at K=K_BZ:")
for ib in range(6):
    print(f"    Branch {ib}: omega(K_BZ) = {omega_all[-1,ib]:.6f}")

# Assign branch labels based on K=0 character
# Determine amplitude vs phase content
amp_frac_0 = np.zeros(6)
for ib in range(6):
    amp_frac_0[ib] = np.sum(evecs_all[0, :3, ib]**2)

print(f"\n  Mode character at K=0 (amplitude fraction):")
for ib in range(6):
    char = "amplitude" if amp_frac_0[ib] > 0.5 else "phase"
    print(f"    Branch {ib}: amp_frac = {amp_frac_0[ib]:.4f} ({char})")

# Label assignment
branch_labels = []
phase_branches = [(ib, omega_all[0, ib]) for ib in range(6) if amp_frac_0[ib] < 0.5]
amp_branches = [(ib, omega_all[0, ib]) for ib in range(6) if amp_frac_0[ib] >= 0.5]
phase_branches.sort(key=lambda x: x[1])
amp_branches.sort(key=lambda x: x[1])

label_map = {}
phase_names = ['Goldstone', 'Leggett-1', 'Leggett-2']
amp_names = ['Higgs-1', 'Higgs-2', 'Higgs-3']
for idx, (ib, _) in enumerate(phase_branches):
    if idx < len(phase_names):
        label_map[ib] = phase_names[idx]
for idx, (ib, _) in enumerate(amp_branches):
    if idx < len(amp_names):
        label_map[ib] = amp_names[idx]

branch_labels = [label_map.get(ib, f'Branch-{ib}') for ib in range(6)]
print(f"\n  Branch labels: {branch_labels}")

# ============================================================
# Section 10: Power-law fit
# ============================================================
print("\n--- Section 10: Power-law fit omega ~ K^alpha ---")

# Fit in the region K < 0.2 (gate criterion region)
K_gate_max = 0.2  # (local)
mask_gate = (K_plot > 1e-6) & (K_plot < K_gate_max)

# Also fit in a wider region for robustness
K_fit_max = 0.35  # (local)
mask_fit = (K_plot > 1e-6) & (K_plot < K_fit_max)

alpha_eff = np.zeros(6)
alpha_gate = np.zeros(6)
alpha_err = np.zeros(6)
c_eff = np.zeros(6)

for ib in range(6):
    omega_b = omega_all[:, ib]
    gap = omega_b[0]

    if abs(gap) < 1e-5:
        # Gapless (Goldstone): omega = c * K^alpha
        for mask_use, label_fit, store_idx in [
            (mask_gate, "gate", None), (mask_fit, "wide", None)
        ]:
            pass

        # Gate region fit
        y = np.log(np.abs(omega_b[mask_gate]) + 1e-30)
        x = np.log(K_plot[mask_gate])
        if len(x) > 2:
            coeffs, cov = np.polyfit(x, y, 1, cov=True)
            alpha_gate[ib] = coeffs[0]

        # Wide region fit (for reporting)
        y = np.log(np.abs(omega_b[mask_fit]) + 1e-30)
        x = np.log(K_plot[mask_fit])
        if len(x) > 2:
            coeffs, cov = np.polyfit(x, y, 1, cov=True)
            alpha_eff[ib] = coeffs[0]
            alpha_err[ib] = sqrt(cov[0, 0])
            c_eff[ib] = np.exp(coeffs[1])
    else:
        # Gapped: omega - gap = c * K^alpha
        delta_omega = omega_b[mask_fit] - gap
        good = delta_omega > 1e-10
        if np.sum(good) > 2:
            y = np.log(delta_omega[good])
            x = np.log(K_plot[mask_fit][good])
            coeffs, cov = np.polyfit(x, y, 1, cov=True)
            alpha_eff[ib] = coeffs[0]
            alpha_err[ib] = sqrt(cov[0, 0])
            c_eff[ib] = np.exp(coeffs[1])
        else:
            alpha_eff[ib] = 2.0

        # Gate region
        delta_omega_g = omega_b[mask_gate] - gap
        good_g = delta_omega_g > 1e-10
        if np.sum(good_g) > 2:
            y_g = np.log(delta_omega_g[good_g])
            x_g = np.log(K_plot[mask_gate][good_g])
            coeffs_g = np.polyfit(x_g, y_g, 1)
            alpha_gate[ib] = coeffs_g[0]
        else:
            alpha_gate[ib] = alpha_eff[ib]

print(f"  Power-law fits:")
print(f"  {'Branch':15s} {'gap':>8s} {'alpha(wide)':>12s} {'alpha(gate)':>12s} {'|a-2|':>8s} {'Verdict':>10s}")
for ib in range(6):
    gap = omega_all[0, ib]
    gap_str = f"{gap:.4f}" if abs(gap) > 1e-5 else "0"
    dev = abs(alpha_gate[ib] - 2.0)
    verdict_str = "ANOMALOUS" if dev > 0.05 else "K^2"
    print(f"  {branch_labels[ib]:15s} {gap_str:>8s} "
          f"{alpha_eff[ib]:>10.4f}+-{alpha_err[ib]:.4f} "
          f"{alpha_gate[ib]:>10.4f}   {dev:>6.4f}   {verdict_str:>10s}")

# ============================================================
# Section 11: Feshbach diagnostic
# ============================================================
print("\n--- Section 11: Feshbach / level crossing diagnostic ---")

# Check crossings
crossings = []
for ib1 in range(6):
    for ib2 in range(ib1+1, 6):
        for ik in range(1, N_K+1):
            d1 = omega_all[ik-1, ib1] - omega_all[ik-1, ib2]
            d2 = omega_all[ik, ib1] - omega_all[ik, ib2]
            if d1 * d2 < 0:
                K_c = K_plot[ik-1] + (K_plot[ik] - K_plot[ik-1]) * abs(d1)/(abs(d1)+abs(d2))
                w_c = 0.5*(omega_all[ik, ib1] + omega_all[ik, ib2])
                crossings.append((ib1, ib2, K_c, w_c))

# Anti-crossings
anticrossings = []
for ib1 in range(6):
    for ib2 in range(ib1+1, 6):
        gaps = np.abs(omega_all[:, ib1] - omega_all[:, ib2])
        ik_min = np.argmin(gaps)
        if gaps[ik_min] < 0.15 and ik_min > 0:
            anticrossings.append((ib1, ib2, K_plot[ik_min], gaps[ik_min]))

if crossings:
    print(f"  {len(crossings)} branch crossing(s):")
    for (b1, b2, Kc, wc) in crossings:
        print(f"    {branch_labels[b1]}/{branch_labels[b2]} at K={Kc:.4f}, omega={wc:.4f}")
else:
    print(f"  No exact branch crossings")

if anticrossings:
    print(f"  Anti-crossings:")
    for (b1, b2, K_ac, gap_ac) in anticrossings:
        print(f"    {branch_labels[b1]}/{branch_labels[b2]}: "
              f"min gap = {gap_ac:.6f} at K = {K_ac:.4f}")

# Pair-breaking threshold
threshold_B3 = 2.0 * Delta_0[2]
print(f"\n  Pair-breaking threshold 2*Delta_B3 = {threshold_B3:.6f}")
for ib in range(6):
    for ik in range(N_K):
        if omega_all[ik, ib] < threshold_B3 and omega_all[ik+1, ib] > threshold_B3:
            K_thr = K_plot[ik] + (K_plot[ik+1]-K_plot[ik]) * \
                    (threshold_B3 - omega_all[ik,ib])/(omega_all[ik+1,ib]-omega_all[ik,ib])
            print(f"    {branch_labels[ib]}: enters continuum at K = {K_thr:.4f}")
            break
    else:
        if omega_all[0, ib] < threshold_B3 and omega_all[-1, ib] < threshold_B3:
            print(f"    {branch_labels[ib]}: always below threshold (sharp)")
        elif omega_all[0, ib] > threshold_B3:
            print(f"    {branch_labels[ib]}: always above threshold")

# ============================================================
# Section 12: Gate verdict
# ============================================================
print("\n--- Section 12: Gate GL-JOSEPHSON-52 ---")

gate_pass = False
anomalous = []
for ib in range(6):
    dev = abs(alpha_gate[ib] - 2.0)
    if dev > 0.05:
        anomalous.append((ib, branch_labels[ib], alpha_gate[ib], dev))
        gate_pass = True

if gate_pass:
    verdict = "PASS"
    detail = f"{len(anomalous)} branch(es) anomalous at K<0.2: "
    detail += ", ".join([f"{lab} (alpha={a:.3f}, |a-2|={d:.3f})"
                         for (_, lab, a, d) in anomalous])
else:
    verdict = "FAIL"
    max_dev = max(abs(alpha_gate[ib] - 2.0) for ib in range(6))
    detail = f"All branches K^2 (max |alpha-2| = {max_dev:.4f} < 0.05)"

print(f"\n  Gate: GL-JOSEPHSON-52")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")

# ============================================================
# Section 13: Band structure summary
# ============================================================
print("\n--- Section 13: Band structure summary ---")

for ib in range(6):
    bw = omega_all[-1, ib] - omega_all[0, ib]
    print(f"  {branch_labels[ib]:15s}: omega=[{omega_all[0,ib]:.6f}, {omega_all[-1,ib]:.6f}], "
          f"BW={bw:.6f}")

# Group velocities
print(f"\n  Group velocities at small K:")
for ib in range(6):
    dw = omega_all[2, ib] - omega_all[1, ib]
    dk = K_plot[2] - K_plot[1]
    print(f"    {branch_labels[ib]:15s}: v_g = {dw/dk:.6f}")

# Effective masses
print(f"\n  Effective masses at small K:")
for ib in range(6):
    dk = K_plot[2] - K_plot[1]
    d2w = (omega_all[3,ib] - 2*omega_all[2,ib] + omega_all[1,ib]) / dk**2
    if abs(d2w) > 1e-12:
        m_star = 0.5 / d2w
        print(f"    {branch_labels[ib]:15s}: d^2w/dK^2 = {d2w:.6f}, m* = {m_star:.4f}")
    else:
        print(f"    {branch_labels[ib]:15s}: flat")

# ============================================================
# Section 14: Sound speed and comparison with c_fabric
# ============================================================
print("\n--- Section 14: Sound speed analysis ---")

# The Goldstone sound speed from the dispersion
gold_idx = None
for ib in range(6):
    if abs(omega_all[0, ib]) < 1e-4:
        gold_idx = ib
        break

if gold_idx is not None:
    # Linear fit omega = c*K at small K
    mask_sound = (K_plot > 1e-6) & (K_plot < 0.15)
    c_gold_fit = np.polyfit(K_plot[mask_sound], omega_all[mask_sound, gold_idx], 1)[0]
    print(f"  Goldstone sound speed (fit): c = {c_gold_fit:.4f}")
    print(f"  c_fabric (canonical): {c_fabric:.4f}")
    print(f"  Ratio: {c_gold_fit / c_fabric:.6f}")

    # The Goldstone speed is the fabric sound speed divided by the lattice factor
    # c_Gold^2 = (total phase stiffness) / (total phase inertia)
    # At small K: omega^2 ~ J_eff * K^2 * sum(Delta_i^2) / sum(rho_i * Delta_i^2)
    # This gives c^2 = J_eff_coeff * sum(Delta_i^2) / sum(rho_i * Delta_i^2)

    # The canonical c_fabric = 209.97 comes from the spectral action gradient
    # stiffness Z_fold, not from the BCS Josephson coupling. The ratio tells us
    # how much of the fabric stiffness is captured by the GL Josephson model.

    # Expected: c_GL << c_fabric because GL captures only the BCS component,
    # not the full spectral action stiffness.
    print(f"\n  NOTE: c_fabric >> c_Gold because c_fabric comes from spectral action")
    print(f"  gradient stiffness (Z_fold = 74730), while c_Gold comes from")
    print(f"  BCS Josephson coupling (J_C2 = {J_C2}). The ratio measures")
    print(f"  the BCS fraction of the total fabric stiffness.")

    # What c_Gold SHOULD be from BCS parameters:
    # c_Gold^2 = 8*J_eff_small_K * (sum Delta^2) / (sum rho*Delta^2)
    # where J_eff_small_K ~ (3/4)*(4*J_C2 + 4*J_NN_other)*(a/2)^2 + ...
    # (from Taylor expansion of S_NN at small K)
    sum_D2 = np.sum(Delta_0**2)
    sum_rD2 = np.sum(rho_0 * Delta_0**2)
    print(f"  sum(Delta^2) = {sum_D2:.6f}")
    print(f"  sum(rho*Delta^2) = {sum_rD2:.6f}")

# ============================================================
# Section 15: Save data
# ============================================================
print("\n--- Section 15: Saving data ---")

outfile = os.path.join(os.path.dirname(__file__), "s52_gl_josephson.npz")
np.savez(outfile,
    # Grid
    K_array=K_plot,
    K_BZ=K_BZ,
    a_BCC=a_BCC,
    N_K=N_K,
    # Dispersion
    omega_branches=omega_all,
    omega_sq=omega_sq_all,
    eigvecs_all=evecs_all,
    branch_labels=np.array(branch_labels),
    # Ground state
    Delta_0=Delta_0,
    rho_0=rho_0,
    a_alpha=a_alpha,
    b_alpha=b_alpha,
    # Josephson couplings
    J_12=J_12_micro,
    J_23=J_23_micro,
    J_13=J_13_micro,
    J_C2_fab=J_C2,
    J_su2_fab=J_su2,
    J_u1_fab=J_u1,
    # Matrices at K=0
    V_amp_0=V_amp_0,
    V_phase_0=V_phase_0,
    T_phase=T_phase,
    T_amp=T_amp,
    # Power-law fits
    alpha_eff=alpha_eff,
    alpha_gate=alpha_gate,
    alpha_err=alpha_err,
    c_eff=c_eff,
    # Mode character
    amp_frac_K0=amp_frac_0,
    # Cross-checks
    omega_L1_s48=omega_L1_s48,
    omega_L2_s48=omega_L2_s48,
    # Gate
    gate_name=np.array(['GL-JOSEPHSON-52']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
    n_crossings=len(crossings),
    n_anticrossings=len(anticrossings),
)
print(f"  Saved: {outfile}")

# ============================================================
# Section 16: Plot
# ============================================================
print("\n--- Section 16: Plotting ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# Panel (a): Full dispersion
ax = axes[0, 0]
for ib in range(6):
    ax.plot(K_plot, omega_all[:, ib], '-', color=colors[ib],
            linewidth=2, label=branch_labels[ib])
ax.axhline(threshold_B3, color='gray', ls='--', alpha=0.5,
           label=f'2*Delta_B3={threshold_B3:.3f}')
ax.set_xlabel('K (M_KK units)', fontsize=12)
ax.set_ylabel('omega (M_KK)', fontsize=12)
ax.set_title('(a) GL Dispersion: 6 Branches on 32-Cell BCC', fontsize=12)
ax.legend(fontsize=8, loc='upper left')
ax.set_xlim(0, K_BZ)
ax.grid(True, alpha=0.3)

# Panel (b): Low-K zoom
ax = axes[0, 1]
mask_zoom = K_plot < 0.4
for ib in range(6):
    if omega_all[0, ib] < 0.5:  # Only plot low-energy branches
        ax.plot(K_plot[mask_zoom], omega_all[mask_zoom, ib], '-o',
                color=colors[ib], linewidth=2, markersize=3,
                label=f'{branch_labels[ib]} (alpha={alpha_gate[ib]:.2f})')

# K^1 and K^2 reference
K_ref = np.linspace(0.01, 0.4, 50)
ax.plot(K_ref, c_gold_fit * K_ref, 'k--', alpha=0.3, label='K^1 ref')
ax.plot(K_ref, 5.0 * K_ref**2, 'k:', alpha=0.3, label='K^2 ref')
ax.axhline(threshold_B3, color='gray', ls='--', alpha=0.5)
ax.axvline(0.2, color='red', ls=':', alpha=0.3, label='K=0.2 (gate)')
ax.set_xlabel('K (M_KK)', fontsize=12)
ax.set_ylabel('omega (M_KK)', fontsize=12)
ax.set_title('(b) Low-K: Phase Sector (Gate Region)', fontsize=12)
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3)

# Panel (c): log-log power-law
ax = axes[1, 0]
for ib in range(6):
    om = omega_all[:, ib]
    gap = om[0]
    if abs(gap) < 1e-4:
        y = np.abs(om[1:])
    else:
        y = np.abs(om[1:] - gap)
    valid = y > 1e-10
    if np.any(valid):
        ax.plot(K_plot[1:][valid], y[valid], '-', color=colors[ib], lw=2,
                label=f'{branch_labels[ib]} (a={alpha_eff[ib]:.2f})')

K_ref_log = np.logspace(np.log10(K_plot[1]), np.log10(K_BZ), 50)
ax.plot(K_ref_log, 0.1*K_ref_log**1, 'k-', alpha=0.2, label='~K^1')
ax.plot(K_ref_log, 0.5*K_ref_log**2, 'k--', alpha=0.2, label='~K^2')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('K (M_KK)', fontsize=12)
ax.set_ylabel('omega - gap (M_KK)', fontsize=12)
ax.set_title('(c) Log-Log Power Law Identification', fontsize=12)
ax.legend(fontsize=7, loc='upper left')
ax.grid(True, alpha=0.3, which='both')

# Panel (d): Mode character
ax = axes[1, 1]
amp_frac = np.zeros((N_K + 1, 6))
for ik in range(N_K + 1):
    for ib in range(6):
        amp_frac[ik, ib] = np.sum(evecs_all[ik, :3, ib]**2)
for ib in range(6):
    ax.plot(K_plot, amp_frac[:, ib], '-', color=colors[ib], lw=2,
            label=branch_labels[ib])
ax.axhline(0.5, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('K (M_KK)', fontsize=12)
ax.set_ylabel('Amplitude fraction', fontsize=12)
ax.set_title('(d) Mode Character: Amplitude vs Phase', fontsize=12)
ax.legend(fontsize=8, loc='center right')
ax.set_ylim(-0.05, 1.05)
ax.grid(True, alpha=0.3)

plt.suptitle(f'GL-JOSEPHSON-52: Generalized Eigenvalue Dispersion\n'
             f'Gate: {verdict} | {detail[:80]}',
             fontsize=12, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])

plotfile = os.path.join(os.path.dirname(__file__), "s52_gl_josephson.png")
plt.savefig(plotfile, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotfile}")

# ============================================================
# Final summary
# ============================================================
print("\n" + "=" * 70)
print("SUMMARY: GL-JOSEPHSON-52")
print("=" * 70)
print(f"  Lattice: BCC-derived, a = {a_BCC:.4f}, K_BZ = {K_BZ:.4f}")
print(f"  Ground state: Delta = [{Delta_0[0]:.4f}, {Delta_0[1]:.4f}, {Delta_0[2]:.4f}]")
print(f"  Inertia (generalized eigenvalue): T_phase = rho*Delta^2, T_amp = rho")
print(f"\n  6 dispersion branches (K=0 -> K_BZ):")
for ib in range(6):
    print(f"    {ib}. {branch_labels[ib]:15s}: omega = [{omega_all[0,ib]:.6f}, {omega_all[-1,ib]:.6f}], "
          f"alpha_gate = {alpha_gate[ib]:.4f}")
if gold_idx is not None:
    print(f"\n  Goldstone sound speed: {c_gold_fit:.4f} (cf. c_fabric = {c_fabric:.2f})")
    print(f"  BCS/fabric stiffness ratio: {(c_gold_fit/c_fabric)**2:.6f}")
print(f"\n  Leggett cross-check:")
if len(pos_evals) >= 2:
    print(f"    L1: {oL1:.6f} vs S48 {omega_L1_s48:.6f} (ratio {oL1/omega_L1_s48:.3f})")
    print(f"    L2: {oL2:.6f} vs S48 {omega_L2_s48:.6f} (ratio {oL2/omega_L2_s48:.3f})")
print(f"\n  Gate: {verdict}")
print(f"  Detail: {detail}")
print("=" * 70)
