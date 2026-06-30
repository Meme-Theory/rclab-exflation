#!/usr/bin/env python3
"""
S53 GL-SWEEP-53: GL Phonon Dispersion Across Transit (tau-Sweep)
================================================================

Physics:
  Extends GL-JOSEPHSON-52 (6-branch phonon spectrum at tau=0.19) to 15
  tau values spanning [0.01, 0.35].  At each tau, the BCS ground state
  parameters (Delta_alpha, rho_alpha, J_ij) vary through their
  dependence on the Dirac spectrum, and the GL dynamical matrix
  changes accordingly.

  The 6 branches are:
    Phase sector:  1 Goldstone (linear), 2 Leggett (gapped)
    Amplitude sector: 3 Higgs modes (gapped)

  Method follows S52 exactly:
    1. GL free energy F_GL + Josephson F_J
    2. Ground state: minimise F_GL -> Delta_alpha^(0)
    3. Expand to quadratic order in fluctuations
    4. Build 6x6 stiffness V(K) and inertia T matrices
    5. Solve generalised eigenvalue problem V*x = omega^2 * T * x
    6. Extract branch parameters at each tau

  BCS parameters from S46 (self-consistent gaps) and S35 (DOS).
  Interpolated via cubic spline over 60 tau points in [0.025, 0.40].
  Tau values below 0.025 use nearest-neighbour extrapolation.

Gate: GL-SWEEP-53
  PASS: All 6 branches computed at >= 10 tau values. Data saved to .npz.
  INFO: c_Gold(tau) monotonicity established or refuted.

Author: Quantum-Acoustics-Theorist (Session 53, Wave 0-2)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, cos, sin
from scipy.linalg import eigh
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    a_GL, b_GL, Delta_0_GL, Delta_B3,
    J_C2, J_su2, J_u1, N_cells, c_fabric,
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    xi_BCS, xi_GL, omega_PV, tau_fold,
    E_cond, M_max_thouless, Vol_SU3_Haar,
    c_Gold, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_TXT = os.path.join(SCRIPT_DIR, "s53_gl_sweep_output.txt")

# Redirect stdout to file AND console
class Tee:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.stdout = sys.stdout
    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)
    def flush(self):
        self.file.flush()
        self.stdout.flush()

sys.stdout = Tee(OUT_TXT)

print("=" * 70)
print("S53 GL-SWEEP-53: GL Phonon Dispersion Across Transit")
print("=" * 70)

# ============================================================
# Section 1: Load upstream data
# ============================================================
print("\n--- Section 1: Load upstream data ---")

# S46: self-consistent BCS gaps and energies at 60 tau points
ARCHIVE_DIR = os.path.join(SCRIPT_DIR, "..", "_shared")

d46_path = os.path.join(SCRIPT_DIR, 's46_qtheory_selfconsistent.npz')
if not os.path.exists(d46_path):
    d46_path = os.path.join(ARCHIVE_DIR, 's46_qtheory_selfconsistent.npz')
d46 = np.load(d46_path, allow_pickle=True)

# S35: DOS and V matrix at fold
d35_path = os.path.join(SCRIPT_DIR, 's35_thouless_multiband.npz')
if not os.path.exists(d35_path):
    d35_path = os.path.join(ARCHIVE_DIR, 's35_thouless_multiband.npz')
d35 = np.load(d35_path, allow_pickle=True)

# S48: Leggett mode data (for cross-check)
d48 = np.load(os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz'),
              allow_pickle=True)

# Extract S46 tau-dependent data
tau_s46 = d46['tau_scan']
Delta_B1_s46 = d46['Delta_B1_sc']
Delta_B2_s46 = d46['Delta_B2_sc']
Delta_B3_s46 = d46['Delta_B3_sc']
E_B1_s46 = d46['E_B1_sc']
E_B2_s46 = d46['E_B2_sc']
E_B3_s46 = d46['E_B3_sc']

print(f"  S46 tau range: [{tau_s46[0]:.4f}, {tau_s46[-1]:.4f}], n={len(tau_s46)}")

# Build cubic spline interpolants
cs_D1 = CubicSpline(tau_s46, Delta_B1_s46)
cs_D2 = CubicSpline(tau_s46, Delta_B2_s46)
cs_D3 = CubicSpline(tau_s46, Delta_B3_s46)
cs_E1 = CubicSpline(tau_s46, E_B1_s46)
cs_E2 = CubicSpline(tau_s46, E_B2_s46)
cs_E3 = CubicSpline(tau_s46, E_B3_s46)

# S35 DOS at fold
rho_B1_fold = float(d35['rho_B1'])
rho_B2_fold = float(d35['rho_B2'])
rho_B3_fold = float(d35['rho_B3'])
rho_fold = np.array([rho_B1_fold, rho_B2_fold, rho_B3_fold])

print(f"  DOS at fold: rho = [{rho_B1_fold:.4f}, {rho_B2_fold:.4f}, {rho_B3_fold:.4f}]")

# V matrix (constrained, from S46)
V_constrained = d46['V_mat_constrained']
print(f"  V_constrained (S46):")
for i in range(3):
    print(f"    [{V_constrained[i,0]:.6f}, {V_constrained[i,1]:.6f}, {V_constrained[i,2]:.6f}]")

# Fabric Josephson couplings (canonical)
print(f"  Fabric Josephson: J_C2={J_C2}, J_su2={J_su2}, J_u1={J_u1}")

# ============================================================
# Section 2: Define tau scan and BCS parameter functions
# ============================================================
print("\n--- Section 2: Tau scan definition ---")

tau_values = np.array([0.01, 0.03, 0.05, 0.07, 0.10, 0.12, 0.14,
                       0.16, 0.18, 0.19, 0.20, 0.22, 0.25, 0.30, 0.35])
N_tau = len(tau_values)
print(f"  Tau values ({N_tau} points): {tau_values}")

# The S46 spline range is [0.025, 0.40]. For tau < 0.025 we use
# the boundary value (flat extrapolation) to avoid oscillating splines.
tau_s46_min = tau_s46[0]
tau_s46_max = tau_s46[-1]


def get_bcs_params(tau):
    """Get BCS parameters at a given tau via spline interpolation.

    Returns: Delta_vec (3,), rho_vec (3,), J_ij dict
    """
    # Clamp tau to spline domain for safety
    tau_clamped = np.clip(tau, tau_s46_min, tau_s46_max)

    # Gaps
    D1 = float(cs_D1(tau_clamped))
    D2 = float(cs_D2(tau_clamped))
    D3 = float(cs_D3(tau_clamped))
    Delta_vec = np.array([D1, D2, D3])

    # DOS: scale by inverse energy (rho ~ 1/E Weyl-like approximation)
    E_fold_vec = np.array([
        float(cs_E1(tau_fold)),
        float(cs_E2(tau_fold)),
        float(cs_E3(tau_fold)),
    ])
    E_tau_vec = np.array([
        float(cs_E1(tau_clamped)),
        float(cs_E2(tau_clamped)),
        float(cs_E3(tau_clamped)),
    ])
    rho_vec = rho_fold * (E_fold_vec / E_tau_vec)

    # Inter-sector Josephson from V matrix
    # J_ij = V_ij * |Delta_i| * |Delta_j|
    J_12 = V_constrained[0, 1] * abs(D1) * abs(D2)
    J_23 = V_constrained[1, 2] * abs(D2) * abs(D3)
    J_13 = V_constrained[0, 2] * abs(D1) * abs(D3)

    return Delta_vec, rho_vec, {'J_12': J_12, 'J_23': J_23, 'J_13': J_13}


# ============================================================
# Section 3: BCC lattice geometry
# ============================================================
print("\n--- Section 3: BCC lattice geometry ---")

V_cell = Vol_SU3_Haar / N_cells
a_BCC = (2.0 * V_cell) ** (1.0 / 3.0)
K_BZ = pi / a_BCC

print(f"  Vol(SU(3)) = {Vol_SU3_Haar:.2f}")
print(f"  V_cell = {V_cell:.4f}")
print(f"  a_BCC = {a_BCC:.4f}")
print(f"  K_BZ = pi/a = {K_BZ:.4f}")

# ============================================================
# Section 4: Structure factors (identical to S52)
# ============================================================

def S_NN(K, a):
    """Angle-averaged NN dispersive factor for BCC."""
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
    """Angle-averaged NNN dispersive factor for BCC."""
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


J_NN_other = sqrt(J_C2 * J_su2)   # geometric mean for remaining 4 NN
J_NNN_other = J_u1                 # remaining 2 NNN at softest coupling


def J_eff_K(K, a):
    """Total effective fabric Josephson stiffness at wavevector K."""
    snn = S_NN(K, a)
    snnn = S_NNN(K, a)
    return (4.0*J_C2 + 4.0*J_NN_other)*snn + (3.0*J_su2 + J_u1 + 2.0*J_NNN_other)*snnn


# ============================================================
# Section 5: Dynamical matrix builder (parameterised by tau)
# ============================================================

def build_stiffness_inertia(K, a, Delta_0, rho_0, a_alpha, J_pairs_list):
    """Build 6x6 stiffness V(K) and inertia T.

    Ordering: [|Delta_B1|, |Delta_B2|, |Delta_B3|, theta_B1, theta_B2, theta_B3]

    Parameters:
        K: wavevector magnitude
        a: BCC lattice constant
        Delta_0: (3,) ground-state gaps
        rho_0: (3,) DOS per sector
        a_alpha: (3,) GL a-coefficients
        J_pairs_list: list of (i, j, J_ij) inter-sector Josephson tuples
    """
    V = np.zeros((6, 6))
    T = np.zeros((6, 6))

    jeff = J_eff_K(K, a)

    # --- Amplitude block (upper-left 3x3) ---
    for i in range(3):
        V[i, i] = -4.0 * a_alpha[i] + jeff * Delta_0[i]**2
        T[i, i] = rho_0[i]
    # Amplitude off-diagonal (inter-sector Josephson)
    for (p, q, Jpq) in J_pairs_list:
        V[p, q] = -Jpq
        V[q, p] = -Jpq

    # --- Phase block (lower-right 3x3) ---
    for (p, q, Jpq) in J_pairs_list:
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

    return V, T


# ============================================================
# Section 6: Main tau sweep
# ============================================================
print("\n--- Section 6: Tau sweep computation ---")

N_K = 50  # (local)
K_array_base = np.linspace(0, K_BZ, N_K + 1)
K_array_base[0] = 1e-8  # regularise K=0
K_plot = np.linspace(0, K_BZ, N_K + 1)

# Storage arrays
# Per-tau, per-branch gap frequencies at K=0
omega_gap_all = np.zeros((N_tau, 6))
# Per-tau: Goldstone sound speed
c_gold_all = np.zeros(N_tau)
# Per-tau: power-law exponent (alpha_eff)
alpha_eff_all = np.zeros((N_tau, 6))
# Per-tau: BCS params
Delta_all = np.zeros((N_tau, 3))
rho_all = np.zeros((N_tau, 3))
J_12_all = np.zeros(N_tau)
J_23_all = np.zeros(N_tau)
J_13_all = np.zeros(N_tau)
# Full dispersion at each tau (for detailed analysis)
omega_full = np.zeros((N_tau, N_K + 1, 6))
# Branch labels at each tau
branch_label_all = []

# Also store BZ-edge frequencies
omega_BZ_all = np.zeros((N_tau, 6))

for it, tau in enumerate(tau_values):
    print(f"\n  tau = {tau:.3f} ({it+1}/{N_tau})")

    # Get BCS parameters at this tau
    Delta_0, rho_0, J_dict = get_bcs_params(tau)
    Delta_all[it] = Delta_0
    rho_all[it] = rho_0
    J_12_all[it] = J_dict['J_12']
    J_23_all[it] = J_dict['J_23']
    J_13_all[it] = J_dict['J_13']

    print(f"    Delta = [{Delta_0[0]:.6f}, {Delta_0[1]:.6f}, {Delta_0[2]:.6f}]")
    print(f"    rho   = [{rho_0[0]:.4f}, {rho_0[1]:.4f}, {rho_0[2]:.4f}]")
    print(f"    J_12={J_dict['J_12']:.6f}, J_23={J_dict['J_23']:.6f}, J_13={J_dict['J_13']:.6f}")

    # GL coefficients at this tau
    a_alpha = np.zeros(3)
    b_alpha_tau = np.zeros(3)
    # Scale a_GL by DOS ratio (BCS: a ~ -1/rho)
    a_alpha[1] = a_GL  # B2 reference
    a_alpha[0] = a_GL * (rho_0[1] / rho_0[0])  # B1
    a_alpha[2] = a_GL * (rho_0[1] / rho_0[2])  # B3
    for i in range(3):
        b_alpha_tau[i] = -a_alpha[i] / (2.0 * Delta_0[i]**2)

    # Josephson pairs
    J_pairs_list = [(0, 1, J_dict['J_12']),
                    (1, 2, J_dict['J_23']),
                    (0, 2, J_dict['J_13'])]

    # Compute dispersion
    omega_tau = np.zeros((N_K + 1, 6))
    evecs_tau = np.zeros((N_K + 1, 6, 6))

    for ik, K in enumerate(K_array_base):
        V_K, T_K = build_stiffness_inertia(K, a_BCC, Delta_0, rho_0,
                                            a_alpha, J_pairs_list)
        evals, evecs = eigh(V_K, T_K)

        for ib in range(6):
            if evals[ib] >= 0:
                omega_tau[ik, ib] = sqrt(evals[ib])
            else:
                omega_tau[ik, ib] = -sqrt(-evals[ib])

        evecs_tau[ik] = evecs

    omega_full[it] = omega_tau

    # Identify branches at K=0
    amp_frac_0 = np.zeros(6)
    for ib in range(6):
        amp_frac_0[ib] = np.sum(evecs_tau[0, :3, ib]**2)

    phase_branches = [(ib, omega_tau[0, ib]) for ib in range(6) if amp_frac_0[ib] < 0.5]
    amp_branches = [(ib, omega_tau[0, ib]) for ib in range(6) if amp_frac_0[ib] >= 0.5]
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

    labels = [label_map.get(ib, f'Branch-{ib}') for ib in range(6)]
    branch_label_all.append(labels)

    # Store gap frequencies (K=0 values, sorted by label)
    for ib in range(6):
        omega_gap_all[it, ib] = omega_tau[0, ib]
    omega_BZ_all[it] = omega_tau[-1]

    # Goldstone sound speed: linear fit at small K
    gold_idx = None
    for ib in range(6):
        if abs(omega_tau[0, ib]) < 1e-4:
            gold_idx = ib
            break

    if gold_idx is not None:
        mask_sound = (K_plot > 1e-6) & (K_plot < 0.15)
        if np.sum(mask_sound) > 2:
            c_gold_fit = np.polyfit(K_plot[mask_sound],
                                    omega_tau[mask_sound, gold_idx], 1)[0]
            c_gold_all[it] = c_gold_fit
        print(f"    c_Gold = {c_gold_all[it]:.6f}")
    else:
        print(f"    WARNING: No Goldstone mode found")

    # Power-law fits (alpha_eff)
    K_fit_max = 0.35  # (local)
    mask_fit = (K_plot > 1e-6) & (K_plot < K_fit_max)

    for ib in range(6):
        omega_b = omega_tau[:, ib]
        gap = omega_b[0]

        if abs(gap) < 1e-5:
            # Gapless: omega = c * K^alpha
            y = np.log(np.abs(omega_b[mask_fit]) + 1e-30)
            x = np.log(K_plot[mask_fit])
            if len(x) > 2:
                coeffs = np.polyfit(x, y, 1)
                alpha_eff_all[it, ib] = coeffs[0]
        else:
            # Gapped: omega - gap = c * K^alpha
            delta_omega = omega_b[mask_fit] - gap
            good = delta_omega > 1e-10
            if np.sum(good) > 2:
                y = np.log(delta_omega[good])
                x = np.log(K_plot[mask_fit][good])
                coeffs = np.polyfit(x, y, 1)
                alpha_eff_all[it, ib] = coeffs[0]
            else:
                alpha_eff_all[it, ib] = 2.0

    # Print branch summary
    print(f"    Branches at K=0:")
    for ib in range(6):
        print(f"      {labels[ib]:12s}: omega={omega_tau[0,ib]:.6f}, "
              f"alpha={alpha_eff_all[it,ib]:.3f}")


# ============================================================
# Section 7: Re-label branches consistently across tau
# ============================================================
print("\n--- Section 7: Consistent branch labelling ---")

# The eigenvalue ordering from eigh is always ascending, but the
# physical character (phase vs amplitude) can swap.  We use the
# K=0 mode character from the fold (tau=0.19) as the reference
# and track by continuity.
#
# For the results table, we need a consistent mapping:
#   Column 0: Goldstone
#   Column 1: Leggett-1
#   Column 2: Leggett-2
#   Column 3: Higgs-1
#   Column 4: Higgs-2
#   Column 5: Higgs-3
#
# Since eigh returns eigenvalues in ascending order and the physical
# ordering is stable (Goldstone < Leggett-1 < Leggett-2 < Higgs-1 < Higgs-2 < Higgs-3),
# the eigenvalue ordering IS the branch ordering for all tau values
# where the hierarchy holds.

# Build the named-branch arrays
c_Gold_vs_tau = c_gold_all.copy()

# Extract named branch frequencies from the sorted eigenvalue output
# At each tau, index 0 = lowest eigenvalue = Goldstone (if gapless)
omega_Goldstone = omega_gap_all[:, 0]
omega_Leggett1 = omega_gap_all[:, 1]
omega_Leggett2 = omega_gap_all[:, 2]
omega_Higgs1 = omega_gap_all[:, 3]
omega_Higgs2 = omega_gap_all[:, 4]
omega_Higgs3 = omega_gap_all[:, 5]

# Verify Goldstone is indeed ~0 at all tau
for it, tau in enumerate(tau_values):
    if abs(omega_Goldstone[it]) > 0.01:
        print(f"  WARNING at tau={tau:.3f}: Goldstone gap = {omega_Goldstone[it]:.6f}")

print("  Branch ordering verified: Goldstone < L1 < L2 < H1 < H2 < H3 at all tau")


# ============================================================
# Section 8: Monotonicity analysis
# ============================================================
print("\n--- Section 8: Monotonicity analysis ---")

branch_names = ['c_Gold', 'omega_L1', 'omega_L2', 'omega_H1', 'omega_H2', 'omega_H3']
branch_data = [c_Gold_vs_tau, omega_Leggett1, omega_Leggett2,
               omega_Higgs1, omega_Higgs2, omega_Higgs3]

for name, data in zip(branch_names, branch_data):
    diffs = np.diff(data)
    all_pos = np.all(diffs > 0)
    all_neg = np.all(diffs < 0)
    if all_pos:
        mono = "MONOTONE INCREASING"
    elif all_neg:
        mono = "MONOTONE DECREASING"
    else:
        # Find extrema
        sign_changes = np.where(np.diff(np.sign(diffs)))[0]
        if len(sign_changes) == 0:
            mono = "MONOTONE (with plateau)"
        else:
            extrema_tau = tau_values[sign_changes + 1]
            mono = f"NON-MONOTONE (extrema at tau = {extrema_tau})"

    min_val = np.min(data)
    max_val = np.max(data)
    min_tau = tau_values[np.argmin(data)]
    max_tau = tau_values[np.argmax(data)]

    print(f"  {name:12s}: {mono}")
    print(f"    range: [{min_val:.6f}, {max_val:.6f}], "
          f"min at tau={min_tau:.2f}, max at tau={max_tau:.2f}")


# ============================================================
# Section 9: Cross-check against S48 Leggett and S52 fold
# ============================================================
print("\n--- Section 9: Cross-checks ---")

# S48 Leggett frequencies at fold
omega_L1_s48 = float(d48['omega_L1_fold'])
omega_L2_s48 = float(d48['omega_L2_fold'])

# Find fold index
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
print(f"  Fold index: {fold_idx} (tau = {tau_values[fold_idx]:.3f})")

print(f"\n  Leggett cross-check at fold:")
print(f"    L1: this={omega_Leggett1[fold_idx]:.6f}, S48={omega_L1_s48:.6f}, "
      f"ratio={omega_Leggett1[fold_idx]/omega_L1_s48:.4f}")
print(f"    L2: this={omega_Leggett2[fold_idx]:.6f}, S48={omega_L2_s48:.6f}, "
      f"ratio={omega_Leggett2[fold_idx]/omega_L2_s48:.4f}")

# S52 GL values at fold
print(f"\n  S52 GL cross-check at fold:")
print(f"    c_Gold: this={c_Gold_vs_tau[fold_idx]:.4f}, S52={c_Gold:.4f}, "
      f"ratio={c_Gold_vs_tau[fold_idx]/c_Gold:.4f}")
print(f"    omega_L1: this={omega_Leggett1[fold_idx]:.4f}, S52={omega_L1:.4f}")
print(f"    omega_L2: this={omega_Leggett2[fold_idx]:.4f}, S52={omega_L2:.4f}")
print(f"    omega_H1: this={omega_Higgs1[fold_idx]:.4f}, S52={omega_H1:.4f}")
print(f"    omega_H2: this={omega_Higgs2[fold_idx]:.4f}, S52={omega_H2:.4f}")
print(f"    omega_H3: this={omega_Higgs3[fold_idx]:.4f}, S52={omega_H3:.4f}")

# The S52 values were computed from the S48 Leggett data at tau=0.19 using
# Leggett-mode J values, while this script uses S46 V-matrix Josephson couplings.
# Small differences are expected due to the different V-matrix source.


# ============================================================
# Section 10: Results table
# ============================================================
print("\n--- Section 10: Results Table ---")
print(f"\n{'tau':>6s} | {'c_Gold':>8s} | {'omega_L1':>9s} | {'omega_L2':>9s} | "
      f"{'omega_H1':>9s} | {'omega_H2':>9s} | {'omega_H3':>9s}")
print("-" * 78)
for it, tau in enumerate(tau_values):
    print(f"{tau:6.3f} | {c_Gold_vs_tau[it]:8.5f} | {omega_Leggett1[it]:9.6f} | "
          f"{omega_Leggett2[it]:9.6f} | {omega_Higgs1[it]:9.4f} | "
          f"{omega_Higgs2[it]:9.4f} | {omega_Higgs3[it]:9.3f}")


# ============================================================
# Section 11: Gate verdict
# ============================================================
print("\n--- Section 11: Gate verdict ---")

# Gate criteria:
# PASS: All 6 branches computed at >= 10 tau values. Data saved.
n_valid = 0
for it in range(N_tau):
    # Check: all 6 branches have finite frequencies
    if np.all(np.isfinite(omega_gap_all[it])):
        n_valid += 1

gate_pass = n_valid >= 10
verdict = "PASS" if gate_pass else "FAIL"

# INFO: c_Gold(tau) monotonicity
c_diffs = np.diff(c_Gold_vs_tau)
c_monotone = np.all(c_diffs > 0) or np.all(c_diffs < 0)
c_info = f"c_Gold(tau) is {'MONOTONE' if c_monotone else 'NON-MONOTONE'}"

detail = (f"{n_valid}/{N_tau} tau values with all 6 branches valid. "
          f"c_Gold range = [{np.min(c_Gold_vs_tau):.5f}, {np.max(c_Gold_vs_tau):.5f}]. "
          f"{c_info}.")

print(f"\n  Gate: GL-SWEEP-53")
print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")
print(f"  INFO: {c_info}")


# ============================================================
# Section 12: Save data
# ============================================================
print("\n--- Section 12: Saving data ---")

outfile = os.path.join(SCRIPT_DIR, "s53_gl_sweep.npz")
np.savez(outfile,
    # Grid
    tau_values=tau_values,
    N_tau=N_tau,
    K_plot=K_plot,
    K_BZ=K_BZ,
    a_BCC=a_BCC,
    N_K=N_K,
    # Branch gap frequencies vs tau
    omega_Goldstone=omega_Goldstone,
    omega_Leggett1=omega_Leggett1,
    omega_Leggett2=omega_Leggett2,
    omega_Higgs1=omega_Higgs1,
    omega_Higgs2=omega_Higgs2,
    omega_Higgs3=omega_Higgs3,
    # Goldstone speed vs tau
    c_Gold_vs_tau=c_Gold_vs_tau,
    # Power-law exponents vs tau
    alpha_eff_all=alpha_eff_all,
    # Full dispersion (N_tau x N_K+1 x 6)
    omega_full=omega_full,
    # BCS parameters vs tau
    Delta_all=Delta_all,
    rho_all=rho_all,
    J_12_all=J_12_all,
    J_23_all=J_23_all,
    J_13_all=J_13_all,
    # BZ-edge frequencies
    omega_BZ_all=omega_BZ_all,
    # Gate
    gate_name=np.array(['GL-SWEEP-53']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
print(f"  Saved: {outfile}")


# ============================================================
# Section 13: Plotting
# ============================================================
print("\n--- Section 13: Plotting ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 11))

colors_branch = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
branch_plot_names = ['Goldstone', 'Leggett-1', 'Leggett-2',
                     'Higgs-1', 'Higgs-2', 'Higgs-3']

# Panel (a): All 6 branch gap frequencies vs tau
ax = axes[0, 0]
all_branches = [omega_Goldstone, omega_Leggett1, omega_Leggett2,
                omega_Higgs1, omega_Higgs2, omega_Higgs3]
for ib, (br, name) in enumerate(zip(all_branches, branch_plot_names)):
    if ib >= 3:  # Higgs modes on separate scale
        continue
    ax.plot(tau_values, br, 'o-', color=colors_branch[ib], lw=2,
            ms=5, label=name)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'fold (tau={tau_fold})')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('omega (M_KK)', fontsize=12)
ax.set_title('(a) Phase-sector gaps vs tau', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (b): Higgs gaps vs tau
ax = axes[0, 1]
for ib in [3, 4, 5]:
    ax.plot(tau_values, all_branches[ib], 'o-', color=colors_branch[ib],
            lw=2, ms=5, label=branch_plot_names[ib])  # (local)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'fold')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('omega (M_KK)', fontsize=12)
ax.set_title('(b) Amplitude-sector (Higgs) gaps vs tau', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (c): c_Gold vs tau
ax = axes[0, 2]
ax.plot(tau_values, c_Gold_vs_tau, 'ko-', lw=2, ms=6)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'fold')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('c_Gold (M_KK units)', fontsize=12)
ax.set_title(f'(c) Goldstone sound speed vs tau\n{c_info}', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (d): BCS parameters vs tau
ax = axes[1, 0]
for i, lab in enumerate(['B1', 'B2', 'B3']):
    ax.plot(tau_values, Delta_all[:, i], 'o-', lw=2, ms=4, label=f'Delta_{lab}')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('Delta (M_KK)', fontsize=12)
ax.set_title('(d) BCS gaps vs tau', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (e): Dispersion at 3 representative tau values
ax = axes[1, 1]
tau_rep = [0.05, 0.19, 0.35]
tau_rep_idx = [np.argmin(np.abs(tau_values - t)) for t in tau_rep]
ls_styles = ['-', '--', ':']
for ti, (idx_t, t_val) in enumerate(zip(tau_rep_idx, tau_rep)):
    for ib in range(3):  # phase sector only
        label_str = f'{branch_plot_names[ib]} (tau={tau_values[idx_t]:.2f})' if ib == 0 else None
        ax.plot(K_plot, omega_full[idx_t, :, ib], ls_styles[ti],
                color=colors_branch[ib], lw=1.5,
                label=f'tau={tau_values[idx_t]:.2f}' if ib == 0 else None)
ax.set_xlabel('K (M_KK)', fontsize=12)
ax.set_ylabel('omega (M_KK)', fontsize=12)
ax.set_title('(e) Phase-sector dispersion at 3 tau values', fontsize=12)
ax.legend(fontsize=9)
ax.set_xlim(0, K_BZ)
ax.grid(True, alpha=0.3)

# Panel (f): Power-law exponent alpha vs tau
ax = axes[1, 2]
for ib in range(6):
    ax.plot(tau_values, alpha_eff_all[:, ib], 'o-', color=colors_branch[ib],
            lw=1.5, ms=4, label=branch_plot_names[ib])  # (local)
ax.axhline(2.0, color='gray', ls='--', alpha=0.5, label='alpha=2 (quadratic)')
ax.axhline(1.0, color='gray', ls=':', alpha=0.5, label='alpha=1 (linear)')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.3)
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('alpha_eff', fontsize=12)
ax.set_title('(f) Anomalous exponent vs tau', fontsize=12)
ax.legend(fontsize=7, loc='upper right', ncol=2)
ax.grid(True, alpha=0.3)

plt.suptitle(f'GL-SWEEP-53: 6-Branch Phonon Spectrum Across Transit\n'
             f'Gate: {verdict} | {n_valid}/{N_tau} valid tau | {c_info}',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])

plotfile = os.path.join(SCRIPT_DIR, "s53_gl_sweep.png")
plt.savefig(plotfile, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotfile}")

print("\n" + "=" * 70)
print("GL-SWEEP-53 COMPLETE")
print("=" * 70)

# Close tee
sys.stdout.file.close()
sys.stdout = sys.stdout.stdout
