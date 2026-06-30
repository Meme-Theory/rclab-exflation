#!/usr/bin/env python3
"""
s56_strutinsky_fabric.py — Strutinsky Decomposition on Fabric Hamiltonian
=========================================================================

Gate: STRUTINSKY-FABRIC-56 (INFO)
Session: 56, Wave 2-3
Agent: nazarewicz-nuclear-structure-theorist

Purpose:
    Perform Strutinsky shell-correction decomposition on the FABRIC Hamiltonian:
      E_fabric(tau) = E_exact_TB(tau) + E_BA_ZPE(tau) + E_J_ground(tau)

    where:
      E_exact_TB = Sum_{k=0}^{15} eps_k   (16 occupied TB levels, half-filling)
      E_BA_ZPE   = (1/2) Sum_{n=1}^{31} omega_n(tau)  (Bogoliubov-Anderson ZPE)
      E_J_ground = -N_bonds * E_J * m   (Josephson ground-state energy)

    The Bogoliubov-Anderson phonon frequencies are:
      omega_n = sqrt(E_c * E_J_eff * lambda_n)
    where lambda_n = eps_n / max(eps_k) are normalized TB eigenvalues,
    E_c = (eps[16] - eps[15])/2 is the single-pair charging energy,
    and E_J_eff = max(J_C2_tau * n_bonds_C2 + ...) is the effective Josephson.

    S55 gave gradient ratio = 0.71 on the 992-mode continuum single-cell spectrum.
    This computation tests whether the fabric (inter-cell coupling + BA phonons)
    increases the ratio.

Nuclear benchmark:
    The 32-cell TB spectrum is analogous to a nuclear sd-shell problem:
    32 single-particle levels, 16 occupied (half-filling). This is a regime
    where the Strutinsky energy theorem works well — better than on the
    992-mode spectrum with massive degeneracies, because the TB levels are
    generically non-degenerate (graph Laplacian on an irregular graph).

    In nuclear physics, the shell correction delta_E_shell oscillates with
    particle number and encodes magic-number physics. Here it oscillates
    with tau and encodes the topology of the representation graph.

Method:
    1. Load s54_tb_hamiltonian.npz (50 tau x 32 eigenvalues + J_C2_tau)
    2. At each tau:
       a. Polynomial Strutinsky on 32 TB eigenvalues (order p=3-6)
       b. Compute BA phonon ZPE from graph Laplacian eigenvalues
       c. Compute Josephson ground-state energy
       d. Total fabric energy and its Strutinsky decomposition
    3. Gradient ratio: |d(delta_E_shell)/dtau| / |d(E_smooth)/dtau|
    4. Compare to S55 single-cell ratio 0.71

Provenance:
    Input: computations/session-54/s54_tb_hamiltonian.npz
    Constants: from canonical_constants import *
    S55 baseline: grad_ratio_fold = 0.71 (s55_strutinsky_992.npz)

Output:
    s56_strutinsky_fabric.npz — all numerical results
    s56_strutinsky_fabric.png — 6-panel diagnostic plot
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    J_C2, J_su2, J_u1, N_cells, tau_fold,
    E_cond, E_cond_ED_8mode,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_NPZ = os.path.join(SCRIPT_DIR, "s56_strutinsky_fabric.npz")
OUT_PNG = os.path.join(SCRIPT_DIR, "s56_strutinsky_fabric.png")
OUT_TXT = os.path.join(SCRIPT_DIR, "s56_strutinsky_fabric_output.txt")


# ============================================================
# Output tee (console + file)
# ============================================================
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

print("=" * 78)
print("S56 STRUTINSKY-FABRIC-56: Strutinsky Decomposition on Fabric Hamiltonian")
print("=" * 78)


# ==============================================================================
# SECTION 1: Load TB Hamiltonian data
# ==============================================================================
print("\n--- Section 1: Load s54_tb_hamiltonian.npz ---")

data_path = os.path.join(SCRIPT_DIR, "s54_tb_hamiltonian.npz")
data = np.load(data_path, allow_pickle=True)

tau_values = data['tau_values']   # (50,)
eigenvalues = data['eigenvalues'] # (50, 32) — sorted at each tau
J_C2_tau = data['J_C2_tau']       # (50,)
J_su2_tau = data['J_su2_tau']     # (50,)
J_u1_tau = data['J_u1_tau']       # (50,)
n_bonds_C2 = int(data['n_bonds_C2'])
n_bonds_su2 = int(data['n_bonds_su2'])
n_bonds_u1 = int(data['n_bonds_u1'])
n_bonds_total = int(data['n_bonds_total'])
N_CELLS = int(data['N_cells'])
adj_C2 = data['adj_C2']
adj_su2 = data['adj_su2']
adj_u1 = data['adj_u1']

N_tau = len(tau_values)
N_fill = N_CELLS // 2  # = 16 (half-filling)

print(f"  N_cells = {N_CELLS}, N_fill = {N_fill}")
print(f"  N_tau = {N_tau}, tau range = [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"  Bonds: C2={n_bonds_C2}, su2={n_bonds_su2}, u1={n_bonds_u1}, total={n_bonds_total}")
print(f"  Eigenvalue range at fold: [{eigenvalues[-1,0]:.6f}, {eigenvalues[-1,-1]:.6f}] M_KK")
print(f"  Gap at fold: E[{N_fill}] - E[{N_fill-1}] = {eigenvalues[-1,N_fill] - eigenvalues[-1,N_fill-1]:.6f} M_KK")


# ==============================================================================
# SECTION 2: Polynomial Strutinsky method (adapted from S55)
# ==============================================================================
print("\n--- Section 2: Polynomial Strutinsky on TB levels ---")

def polynomial_strutinsky_32(evals_sorted, N_fill, p_order):
    """
    Strutinsky shell correction via polynomial fit to the cumulative level density.

    For 32 non-degenerate levels, the staircase function N(eps) = #{k : eps_k <= eps}
    is fit by a polynomial P_p(eps) of degree p. The smooth energy is:
        E_smooth = eps_F_smooth * N_fill - integral_{eps_min}^{eps_F_smooth} P(eps) deps
    where P(eps_F_smooth) = N_fill.

    On 32 levels, p=3-6 is the appropriate range (nuclear sd-shell practice).

    Parameters:
    -----------
    evals_sorted : sorted array of eigenvalues (32 levels)
    N_fill : number of filled levels (16)
    p_order : polynomial degree

    Returns dict with E_exact, E_smooth, delta_E_shell, etc.
    """
    eps = evals_sorted
    N_total = len(eps)
    E_exact = np.sum(eps[:N_fill])
    eps_F_exact = eps[N_fill - 1]

    # Cumulative level count at each eigenvalue
    # For non-degenerate levels: N(eps_k) = k + 1
    staircase_x = eps
    staircase_y = np.arange(1, N_total + 1, dtype=float)

    # Polynomial fit P_p(eps) to the staircase
    # Equal weight since levels are non-degenerate
    coeffs = np.polyfit(staircase_x, staircase_y, p_order)

    # Smooth Fermi energy: solve P(eps_F_smooth) = N_fill
    try:
        eps_F_smooth = brentq(
            lambda x: np.polyval(coeffs, x) - N_fill,
            eps[0] - 0.01, eps[-1] + 0.01, xtol=1e-14
        )
    except ValueError:
        eps_F_smooth = eps_F_exact

    N_smooth_check = np.polyval(coeffs, eps_F_smooth)

    # Smooth density at Fermi surface: g_smooth(eps_F) = P'(eps_F)
    dP_coeffs = np.polyder(coeffs)
    g_at_fermi = np.polyval(dP_coeffs, eps_F_smooth)

    # Smooth energy via integration by parts:
    # E_smooth = integral_{eps_min}^{eps_F_smooth} eps * g_smooth(eps) deps
    #          = [eps * P(eps)]_{eps_min}^{eps_F_smooth} - integral P(eps) deps
    #          = eps_F_smooth * N_fill - integral_{eps_min}^{eps_F_smooth} P(eps) deps
    P_anti = np.polyint(coeffs)
    eps_min = eps[0] - 0.01

    integral_P = np.polyval(P_anti, eps_F_smooth) - np.polyval(P_anti, eps_min)
    E_smooth = eps_F_smooth * N_fill - integral_P

    # Correction for nonzero P at lower limit
    P_at_min = np.polyval(coeffs, eps_min)
    E_smooth -= eps_min * P_at_min

    delta_E_shell = E_exact - E_smooth

    # Fit quality: RMS residual
    fit_residuals = staircase_y - np.polyval(coeffs, staircase_x)
    rms_residual = np.sqrt(np.mean(fit_residuals**2))

    return {
        'E_exact': E_exact,
        'E_smooth': E_smooth,
        'delta_E_shell': delta_E_shell,
        'eps_F_exact': eps_F_exact,
        'eps_F_smooth': eps_F_smooth,
        'N_smooth_check': N_smooth_check,
        'g_at_fermi': g_at_fermi,
        'p_order': p_order,
        'rms_residual': rms_residual,
        'poly_coeffs': coeffs,
    }


# ==============================================================================
# SECTION 3: Run Strutinsky on TB eigenvalues at all tau
# ==============================================================================
print("\n--- Section 3: Strutinsky decomposition at all 50 tau values ---")

p_orders = [2, 3, 4, 5, 6, 7]

# Storage arrays
E_exact_TB = np.zeros(N_tau)
E_smooth_TB = np.zeros(N_tau)
dE_shell_TB = np.zeros(N_tau)
dE_shell_sigma = np.zeros(N_tau)
dE_shell_by_p = np.zeros((N_tau, len(p_orders)))
rms_by_p = np.zeros((N_tau, len(p_orders)))
g_at_fermi_arr = np.zeros(N_tau)
eps_F_exact_arr = np.zeros(N_tau)
eps_F_smooth_arr = np.zeros(N_tau)

print(f"\n{'tau':>6s} | {'E_exact':>10s} | {'p=3':>9s} {'p=4':>9s} {'p=5':>9s} {'p=6':>9s} | "
      f"{'mean(3-5)':>10s} {'sigma':>8s}")
print("-" * 90)

for t_idx in range(N_tau):
    tau = tau_values[t_idx]
    evals = eigenvalues[t_idx]
    E_exact_TB[t_idx] = np.sum(evals[:N_fill])

    # Run for each polynomial order
    results_p = {}
    for ip, p in enumerate(p_orders):
        res = polynomial_strutinsky_32(evals, N_fill, p)
        results_p[p] = res
        dE_shell_by_p[t_idx, ip] = res['delta_E_shell']
        rms_by_p[t_idx, ip] = res['rms_residual']

    # Take p=3,4,5 average (standard nuclear sd-shell practice for 32 levels)
    # In nuclear physics with ~30-40 levels, p=3-5 is the convergence window
    # (lower than p=4-6 used for 120 unique levels in S55)
    dE_p3 = results_p[3]['delta_E_shell']
    dE_p4 = results_p[4]['delta_E_shell']
    dE_p5 = results_p[5]['delta_E_shell']
    dE_mean = np.mean([dE_p3, dE_p4, dE_p5])
    dE_sigma = np.std([dE_p3, dE_p4, dE_p5])

    dE_shell_TB[t_idx] = dE_mean
    dE_shell_sigma[t_idx] = dE_sigma
    E_smooth_TB[t_idx] = E_exact_TB[t_idx] - dE_mean

    # Use p=4 for Fermi surface diagnostics
    g_at_fermi_arr[t_idx] = results_p[4]['g_at_fermi']
    eps_F_exact_arr[t_idx] = results_p[4]['eps_F_exact']
    eps_F_smooth_arr[t_idx] = results_p[4]['eps_F_smooth']

    if t_idx % 5 == 0 or t_idx == N_tau - 1:
        print(f"{tau:6.3f} | {E_exact_TB[t_idx]:10.4f} | "
              f"{dE_p3:+9.4f} {dE_p4:+9.4f} {dE_p5:+9.4f} {results_p[6]['delta_E_shell']:+9.4f} | "
              f"{dE_mean:+10.4f} {dE_sigma:8.4f}")

# Check p-convergence at key tau values
print("\n--- p-convergence check ---")
for t_idx in [0, 12, 24, 36, 49]:
    tau = tau_values[t_idx]
    vals = dE_shell_by_p[t_idx]
    print(f"  tau={tau:.3f}: " + " ".join(f"p={p}:{vals[ip]:+.4f}" for ip, p in enumerate(p_orders)))


# ==============================================================================
# SECTION 4: Bogoliubov-Anderson phonon ZPE
# ==============================================================================
print("\n\n--- Section 4: Bogoliubov-Anderson phonon zero-point energy ---")
print("""
Physics: The BA phonon spectrum arises from phase fluctuations of the BCS
condensate on the 32-cell graph. The TB Hamiltonian IS the graph Laplacian
(by construction in S54), so its eigenvalues give the phonon normal modes.

The BA dispersion for a Josephson junction array in the Mott regime is:
  omega_n = sqrt(E_c * E_J_eff * lambda_n)

where:
  E_c = charging energy = (eps[16] - eps[15])/2  (half the single-pair gap)
  E_J_eff = effective Josephson energy (mean coupling * connectivity)
  lambda_n = eps_n / max(eps_k)  (normalized TB eigenvalue, n=1..31)

The n=0 mode is the zero mode (global phase, Goldstone). It carries no ZPE.

Nuclear analog: this is the QRPA phonon vacuum with 31 modes, each
contributing hbar*omega/2 to the ground-state energy.
""")

# Compute BA phonon ZPE at each tau
E_BA_ZPE = np.zeros(N_tau)
omega_BA = np.zeros((N_tau, N_CELLS - 1))  # 31 non-zero modes
E_c_arr = np.zeros(N_tau)
E_J_eff_arr = np.zeros(N_tau)

# F_anomalous: the anomalous pair-transfer enhancement
# From S50: F_transfer = 2.13 (xi/d = 5.3 drives enhancement)
# From S49: m ~ 0.99 (Josephson order parameter at half-filling)
F_anomalous = 2.13  # S50 JPAIR-CALIBRATE-50  # (local)
m_order = 0.99      # S49, near-unity for deep BCS  # (local)

for t_idx in range(N_tau):
    evals = eigenvalues[t_idx]

    # Charging energy: half the single-particle gap at Fermi surface
    E_c = (evals[N_fill] - evals[N_fill - 1]) / 2.0
    E_c_arr[t_idx] = E_c

    # Effective Josephson energy
    # E_J_eff = total Josephson energy per bond
    # Use the mean coupling weighted by bond count
    E_J_eff = (n_bonds_C2 * J_C2_tau[t_idx]
               + n_bonds_su2 * J_su2_tau[t_idx]
               + n_bonds_u1 * J_u1_tau[t_idx]) / n_bonds_total
    E_J_eff *= F_anomalous  # anomalous enhancement
    E_J_eff_arr[t_idx] = E_J_eff

    # Normalized TB eigenvalues (skip zero mode at index 0)
    evals_nonzero = evals[1:]  # 31 modes
    lambda_n = evals_nonzero / evals[-1]  # normalize by bandwidth

    # BA phonon frequencies
    omega_n = np.sqrt(E_c * E_J_eff * lambda_n)
    omega_BA[t_idx] = omega_n

    # Zero-point energy
    E_BA_ZPE[t_idx] = 0.5 * np.sum(omega_n)

print(f"\nBA phonon ZPE summary:")
print(f"{'tau':>6s} | {'E_c':>8s} | {'E_J_eff':>8s} | {'omega_min':>10s} {'omega_max':>10s} | {'E_BA_ZPE':>10s}")
print("-" * 70)
for t_idx in [0, 12, 24, 36, 49]:
    tau = tau_values[t_idx]
    print(f"{tau:6.3f} | {E_c_arr[t_idx]:8.4f} | {E_J_eff_arr[t_idx]:8.4f} | "
          f"{omega_BA[t_idx].min():10.4f} {omega_BA[t_idx].max():10.4f} | "
          f"{E_BA_ZPE[t_idx]:10.4f}")


# ==============================================================================
# SECTION 5: Josephson ground-state energy
# ==============================================================================
print("\n\n--- Section 5: Josephson ground-state energy ---")
print("""
The Josephson energy for a junction array with all phases aligned is:
  E_J_ground = -N_bonds * <E_J> * m

where m is the order parameter (m ~ 0.99) and <E_J> is the mean
Josephson coupling per bond. The negative sign reflects the energy
gain from phase coherence across the fabric.

This is the single largest energy scale in the fabric.
""")

E_J_ground = np.zeros(N_tau)
for t_idx in range(N_tau):
    E_J_mean = (n_bonds_C2 * J_C2_tau[t_idx]
                + n_bonds_su2 * J_su2_tau[t_idx]
                + n_bonds_u1 * J_u1_tau[t_idx]) / n_bonds_total
    E_J_ground[t_idx] = -n_bonds_total * E_J_mean * m_order

print(f"{'tau':>6s} | {'E_J_ground':>12s} | {'E_J_mean':>10s}")
print("-" * 40)
for t_idx in [0, 12, 24, 36, 49]:
    tau = tau_values[t_idx]
    E_J_mean = (n_bonds_C2 * J_C2_tau[t_idx]
                + n_bonds_su2 * J_su2_tau[t_idx]
                + n_bonds_u1 * J_u1_tau[t_idx]) / n_bonds_total
    print(f"{tau:6.3f} | {E_J_ground[t_idx]:12.4f} | {E_J_mean:10.4f}")


# ==============================================================================
# SECTION 6: Total fabric energy and its Strutinsky decomposition
# ==============================================================================
print("\n\n--- Section 6: Total fabric energy ---")

E_fabric = E_exact_TB + E_BA_ZPE + E_J_ground
E_fabric_smooth = E_smooth_TB + E_BA_ZPE + E_J_ground
# Shell correction is the same — BA and Josephson are smooth functions of tau
# (they depend on the eigenvalues collectively, not on individual shell occupations)
# This is the EXACT nuclear Strutinsky argument: the smooth energy contains
# the LDM (liquid drop) contributions, and the shell correction is purely
# from the discrete occupation effects.

dE_shell_fabric = dE_shell_TB.copy()  # Shell correction unchanged

print(f"\n{'tau':>6s} | {'E_TB':>10s} {'E_BA_ZP':>10s} {'E_J_gnd':>12s} | "
      f"{'E_fabric':>12s} {'dE_shell':>10s}")
print("-" * 78)
for t_idx in [0, 6, 12, 18, 24, 30, 36, 42, 49]:
    tau = tau_values[t_idx]
    print(f"{tau:6.3f} | {E_exact_TB[t_idx]:10.4f} {E_BA_ZPE[t_idx]:10.4f} "
          f"{E_J_ground[t_idx]:12.4f} | {E_fabric[t_idx]:12.4f} {dE_shell_fabric[t_idx]:+10.4f}")


# ==============================================================================
# SECTION 7: Gradient analysis — the decisive test
# ==============================================================================
print("\n\n--- Section 7: Gradient analysis (DECISIVE) ---")
print("""
The gradient ratio measures whether shell corrections can drive a minimum:
  R_grad = |d(delta_E_shell)/dtau| / |d(E_smooth_fabric)/dtau|

If R_grad > 1 at some tau, the shell correction slope exceeds the smooth
background slope, and a minimum is POSSIBLE (necessary but not sufficient).
If R_grad < 1 everywhere, the smooth background dominates and shell
corrections CANNOT produce a minimum by themselves.

S55 single-cell result: R_grad = 0.71 at fold.

Nuclear context: In nuclei, R_grad is typically 0.1-0.3 for medium-mass
nuclei (shell corrections are a small perturbation on the LDM). R_grad > 1
occurs only at doubly-magic nuclei (^208Pb, ^132Sn) where deep shell gaps
create large shell corrections. The question is whether the fabric
connectivity pushes the framework into the doubly-magic regime.
""")

# Gradients using finite differences (50 points, smooth enough)
d_dE_shell_dtau = np.gradient(dE_shell_fabric, tau_values)
d_E_smooth_fabric_dtau = np.gradient(E_fabric_smooth, tau_values)
d_E_fabric_dtau = np.gradient(E_fabric, tau_values)
d_E_exact_TB_dtau = np.gradient(E_exact_TB, tau_values)
d_E_BA_ZPE_dtau = np.gradient(E_BA_ZPE, tau_values)
d_E_J_ground_dtau = np.gradient(E_J_ground, tau_values)

# Gradient ratio
grad_ratio_fabric = np.zeros(N_tau)
for t_idx in range(N_tau):
    denom = abs(d_E_smooth_fabric_dtau[t_idx])
    if denom > 1e-12:
        grad_ratio_fabric[t_idx] = abs(d_dE_shell_dtau[t_idx]) / denom
    else:
        grad_ratio_fabric[t_idx] = 0.0

# Also compute on TB alone (for comparison with S55)
d_E_smooth_TB_dtau = np.gradient(E_smooth_TB, tau_values)
grad_ratio_TB = np.zeros(N_tau)
for t_idx in range(N_tau):
    denom = abs(d_E_smooth_TB_dtau[t_idx])
    if denom > 1e-12:
        grad_ratio_TB[t_idx] = abs(d_dE_shell_dtau[t_idx]) / denom
    else:
        grad_ratio_TB[t_idx] = 0.0

# Find fold index (tau closest to 0.50)
fold_idx = N_tau - 1
fold_tau = tau_values[fold_idx]

# Also check at tau ~ 0.19 (same as S55 fold reference)
idx_019 = np.argmin(np.abs(tau_values - 0.19))

# Print gradient decomposition
print(f"\nGradient decomposition (units: M_KK per unit tau):")
print(f"{'tau':>6s} | {'dE_TB/dt':>10s} {'dE_BA/dt':>10s} {'dE_J/dt':>10s} | "
      f"{'dE_sm/dt':>10s} {'d(dEsh)/dt':>10s} | {'R_TB':>6s} {'R_fab':>6s}")
print("-" * 95)
for t_idx in [0, 6, 12, 18, 24, 30, 36, 42, 49]:
    tau = tau_values[t_idx]
    print(f"{tau:6.3f} | {d_E_exact_TB_dtau[t_idx]:10.3f} {d_E_BA_ZPE_dtau[t_idx]:10.4f} "
          f"{d_E_J_ground_dtau[t_idx]:10.3f} | {d_E_smooth_fabric_dtau[t_idx]:10.3f} "
          f"{d_dE_shell_dtau[t_idx]:+10.4f} | {grad_ratio_TB[t_idx]:6.3f} {grad_ratio_fabric[t_idx]:6.3f}")

# Key results
print(f"\n{'=' * 78}")
print(f"KEY GRADIENT RATIOS:")
print(f"{'=' * 78}")
print(f"  At fold (tau={fold_tau:.3f}):")
print(f"    TB-only gradient ratio:  {grad_ratio_TB[fold_idx]:.4f}")
print(f"    Fabric gradient ratio:   {grad_ratio_fabric[fold_idx]:.4f}")
print(f"  At tau=0.19 (S55 reference):")
print(f"    TB-only gradient ratio:  {grad_ratio_TB[idx_019]:.4f}")
print(f"    Fabric gradient ratio:   {grad_ratio_fabric[idx_019]:.4f}")
print(f"  S55 single-cell (992-mode): 0.711")
print(f"  Maximum grad ratio (fabric): {np.max(grad_ratio_fabric):.4f} at tau={tau_values[np.argmax(grad_ratio_fabric)]:.3f}")
print(f"  Maximum grad ratio (TB-only): {np.max(grad_ratio_TB):.4f} at tau={tau_values[np.argmax(grad_ratio_TB)]:.3f}")

# Mean in the physically relevant range [0.15, 0.50]
mask_phys = tau_values >= 0.15
mean_R_fabric = np.mean(grad_ratio_fabric[mask_phys])
mean_R_TB = np.mean(grad_ratio_TB[mask_phys])
print(f"\n  Mean gradient ratio for tau >= 0.15:")
print(f"    TB-only:  {mean_R_TB:.4f}")
print(f"    Fabric:   {mean_R_fabric:.4f}")

# Check for sign changes in delta_E_shell (potential minimum signature)
sign_changes = np.sum(np.diff(np.sign(dE_shell_fabric)) != 0)
print(f"\n  Shell correction sign changes: {sign_changes}")

# Check if E_fabric has a minimum
dE_fabric_dtau = np.gradient(E_fabric, tau_values)
sign_changes_E = np.sum(np.diff(np.sign(dE_fabric_dtau)) != 0)
print(f"  E_fabric gradient sign changes: {sign_changes_E}")
if sign_changes_E > 0:
    for i in range(len(dE_fabric_dtau) - 1):
        if dE_fabric_dtau[i] * dE_fabric_dtau[i+1] < 0:
            tau_cross = tau_values[i] + (tau_values[i+1] - tau_values[i]) * abs(dE_fabric_dtau[i]) / (abs(dE_fabric_dtau[i]) + abs(dE_fabric_dtau[i+1]))
            E_cross = 0.5 * (E_fabric[i] + E_fabric[i+1])
            kind = "minimum" if dE_fabric_dtau[i] < 0 else "maximum"
            print(f"    {kind} near tau={tau_cross:.3f}, E_fabric={E_cross:.4f}")


# ==============================================================================
# SECTION 8: Energy scale comparison
# ==============================================================================
print("\n\n--- Section 8: Energy scale comparison ---")

print(f"\nEnergy scales at fold (tau={fold_tau:.3f}):")
print(f"  E_exact_TB:    {E_exact_TB[fold_idx]:12.4f} M_KK")
print(f"  E_BA_ZPE:      {E_BA_ZPE[fold_idx]:12.4f} M_KK")
print(f"  E_J_ground:    {E_J_ground[fold_idx]:12.4f} M_KK")
print(f"  E_fabric:      {E_fabric[fold_idx]:12.4f} M_KK")
print(f"  delta_E_shell: {dE_shell_fabric[fold_idx]:+12.4f} M_KK")
print(f"  E_smooth_fab:  {E_fabric_smooth[fold_idx]:12.4f} M_KK")
print(f"  |dE_shell|/|E_fabric|: {abs(dE_shell_fabric[fold_idx])/abs(E_fabric[fold_idx]):.4e}")

# Dominant energy gradient
print(f"\nGradient magnitudes at fold:")
print(f"  |dE_TB/dtau|:       {abs(d_E_exact_TB_dtau[fold_idx]):.4f}")
print(f"  |dE_BA_ZPE/dtau|:   {abs(d_E_BA_ZPE_dtau[fold_idx]):.4f}")
print(f"  |dE_J_ground/dtau|: {abs(d_E_J_ground_dtau[fold_idx]):.4f}")
print(f"  |d(dE_shell)/dtau|: {abs(d_dE_shell_dtau[fold_idx]):.4f}")
print(f"  |dE_smooth/dtau|:   {abs(d_E_smooth_fabric_dtau[fold_idx]):.4f}")

# Which term dominates the gradient?
gradient_magnitudes = {
    'TB_exact': abs(d_E_exact_TB_dtau[fold_idx]),
    'BA_ZPE': abs(d_E_BA_ZPE_dtau[fold_idx]),
    'J_ground': abs(d_E_J_ground_dtau[fold_idx]),
}
dominant = max(gradient_magnitudes, key=gradient_magnitudes.get)
print(f"\n  Dominant gradient term: {dominant} ({gradient_magnitudes[dominant]:.4f})")


# ==============================================================================
# SECTION 9: Comparison with S55 single-cell
# ==============================================================================
print("\n\n--- Section 9: Comparison with S55 single-cell ---")

# S55 had 5 tau points; we have 50. Compare at common points.
s55_tau = [0.00, 0.05, 0.10, 0.15, 0.19]
s55_grad_ratios = [1.110, 0.986, 0.419, 0.502, 0.711]
s55_dE_shell = [15.656, 10.355, 7.974, 8.366, 9.398]

print(f"\n{'tau':>6s} | {'S55 R_grad':>10s} {'S56 R_TB':>10s} {'S56 R_fab':>10s} | "
      f"{'S55 dE_sh':>10s} {'S56 dE_sh':>10s}")
print("-" * 65)
for i, s55_t in enumerate(s55_tau):
    idx = np.argmin(np.abs(tau_values - s55_t))
    print(f"{s55_t:6.2f} | {s55_grad_ratios[i]:10.3f} {grad_ratio_TB[idx]:10.3f} "
          f"{grad_ratio_fabric[idx]:10.3f} | {s55_dE_shell[i]:10.3f} {dE_shell_fabric[idx]:10.4f}")


# ==============================================================================
# SECTION 10: Gate verdict
# ==============================================================================
print("\n\n" + "=" * 78)
print("GATE VERDICT: STRUTINSKY-FABRIC-56")
print("=" * 78)

R_fold_fabric = grad_ratio_fabric[fold_idx]
R_fold_TB = grad_ratio_TB[fold_idx]
R_max_fabric = np.max(grad_ratio_fabric)
R_max_TB = np.max(grad_ratio_TB)

verdict = "INFO"  # pre-registered as INFO
verdict_detail = (
    f"Fabric Strutinsky on 32-cell TB Hamiltonian. "
    f"R_grad(fold) = {R_fold_fabric:.3f} (fabric), {R_fold_TB:.3f} (TB-only). "
    f"R_max = {R_max_fabric:.3f} at tau={tau_values[np.argmax(grad_ratio_fabric)]:.3f}. "
    f"S55 single-cell: 0.71. "
    f"{'Fabric INCREASES gradient ratio.' if R_fold_fabric > 0.711 else 'Fabric DECREASES gradient ratio.'} "
    f"Shell corrections {'SUFFICIENT' if R_max_fabric > 1.0 else 'INSUFFICIENT'} for minimum."
)

print(f"\n  Verdict: {verdict}")
print(f"  Detail: {verdict_detail}")
print(f"\n  Key constraint: gradient ratio {'>' if R_max_fabric > 1.0 else '<'} 1.0")
if R_max_fabric > 1.0:
    print(f"  Shell correction can DRIVE a minimum at tau ~ {tau_values[np.argmax(grad_ratio_fabric)]:.3f}")
else:
    print(f"  Shell correction INSUFFICIENT alone. Maximum R = {R_max_fabric:.3f}")
    print(f"  Shortfall factor: {1.0 / R_max_fabric:.2f}x")


# ==============================================================================
# SECTION 11: Save results
# ==============================================================================
print("\n\n--- Section 11: Saving results ---")

save_dict = {
    # Tau grid
    'tau_values': tau_values,
    'N_fill': np.array(N_fill),
    'N_cells': np.array(N_CELLS),
    'n_bonds_total': np.array(n_bonds_total),

    # TB Strutinsky
    'E_exact_TB': E_exact_TB,
    'E_smooth_TB': E_smooth_TB,
    'dE_shell_TB': dE_shell_TB,
    'dE_shell_sigma': dE_shell_sigma,
    'dE_shell_by_p': dE_shell_by_p,
    'rms_by_p': rms_by_p,
    'p_orders': np.array(p_orders),
    'g_at_fermi': g_at_fermi_arr,
    'eps_F_exact': eps_F_exact_arr,
    'eps_F_smooth': eps_F_smooth_arr,

    # BA phonon ZPE
    'E_BA_ZPE': E_BA_ZPE,
    'omega_BA': omega_BA,
    'E_c_arr': E_c_arr,
    'E_J_eff_arr': E_J_eff_arr,

    # Josephson ground state
    'E_J_ground': E_J_ground,
    'F_anomalous': np.array(F_anomalous),
    'm_order': np.array(m_order),

    # Total fabric
    'E_fabric': E_fabric,
    'E_fabric_smooth': E_fabric_smooth,
    'dE_shell_fabric': dE_shell_fabric,

    # Gradients
    'd_dE_shell_dtau': d_dE_shell_dtau,
    'd_E_smooth_fabric_dtau': d_E_smooth_fabric_dtau,
    'd_E_fabric_dtau': d_E_fabric_dtau,
    'd_E_exact_TB_dtau': d_E_exact_TB_dtau,
    'd_E_BA_ZPE_dtau': d_E_BA_ZPE_dtau,
    'd_E_J_ground_dtau': d_E_J_ground_dtau,
    'd_E_smooth_TB_dtau': d_E_smooth_TB_dtau,

    # Gradient ratios
    'grad_ratio_fabric': grad_ratio_fabric,
    'grad_ratio_TB': grad_ratio_TB,
    'R_fold_fabric': np.array(R_fold_fabric),
    'R_fold_TB': np.array(R_fold_TB),
    'R_max_fabric': np.array(R_max_fabric),
    'R_max_TB': np.array(R_max_TB),

    # S55 comparison
    's55_grad_ratio_fold': np.array(0.711),

    # Gate
    'gate_name': np.array(['STRUTINSKY-FABRIC-56']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([verdict_detail]),
}

np.savez(OUT_NPZ, **save_dict)
print(f"  Saved: {OUT_NPZ}")


# ==============================================================================
# SECTION 12: 6-panel diagnostic plot
# ==============================================================================
print("\n--- Section 12: Generating plot ---")

fig = plt.figure(figsize=(18, 14))
fig.suptitle('STRUTINSKY-FABRIC-56: Strutinsky Decomposition on 32-Cell Fabric',
             fontsize=14, fontweight='bold')
gs = GridSpec(3, 2, hspace=0.45, wspace=0.35)

# --- Panel 1: TB eigenvalue spectrum vs tau ---
ax1 = fig.add_subplot(gs[0, 0])
for k in range(N_CELLS):
    color = 'blue' if k < N_fill else 'red'
    alpha = 0.6 if k < N_fill else 0.3  # (local)
    ax1.plot(tau_values, eigenvalues[:, k], '-', color=color, alpha=alpha, linewidth=0.7)
ax1.axhline(0, color='gray', linestyle=':', alpha=0.3)
ax1.set_xlabel('tau', fontsize=11)
ax1.set_ylabel('epsilon_k [M_KK]', fontsize=11)
ax1.set_title('TB eigenvalue spectrum (blue=occupied, red=empty)', fontsize=11)
ax1.grid(True, alpha=0.2)

# --- Panel 2: p-convergence of shell correction ---
ax2 = fig.add_subplot(gs[0, 1])
tau_show = [0, 12, 24, 36, 49]
colors_show = plt.cm.viridis(np.linspace(0.1, 0.9, len(tau_show)))
for ic, t_idx in enumerate(tau_show):
    ax2.plot(p_orders, dE_shell_by_p[t_idx], 'o-', color=colors_show[ic],
             markersize=5, linewidth=1.2, label=f'tau={tau_values[t_idx]:.2f}')
ax2.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax2.axvspan(2.5, 5.5, alpha=0.08, color='green')
ax2.set_xlabel('Polynomial order p', fontsize=11)
ax2.set_ylabel('delta_E_shell [M_KK]', fontsize=11)
ax2.set_title('Polynomial Strutinsky: p-convergence', fontsize=11)
ax2.legend(fontsize=8, loc='best')
ax2.grid(True, alpha=0.2)

# --- Panel 3: Energy components vs tau ---
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(tau_values, E_exact_TB, 'b-', linewidth=1.5, label='E_TB (exact)')
ax3.plot(tau_values, E_BA_ZPE, 'g-', linewidth=1.5, label='E_BA_ZPE')
ax3.plot(tau_values, -E_J_ground, 'r--', linewidth=1.5, label='-E_J_ground')
ax3.plot(tau_values, E_fabric, 'k-', linewidth=2.5, label='E_fabric (total)')
ax3.set_xlabel('tau', fontsize=11)
ax3.set_ylabel('Energy [M_KK]', fontsize=11)
ax3.set_title('Energy components vs tau', fontsize=11)
ax3.legend(fontsize=9, loc='best')
ax3.grid(True, alpha=0.2)

# --- Panel 4: Shell correction and smooth energy ---
ax4 = fig.add_subplot(gs[1, 1])
ax4.errorbar(tau_values, dE_shell_fabric, yerr=dE_shell_sigma,
             fmt='ko-', markersize=3, linewidth=1.2, capsize=2,
             label='delta_E_shell (p=3-5 avg)')
ax4.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax4.set_xlabel('tau', fontsize=11)
ax4.set_ylabel('delta_E_shell [M_KK]', fontsize=11)
ax4.set_title('Shell correction vs tau', fontsize=11)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.2)

ax4b = ax4.twinx()
ax4b.plot(tau_values, E_fabric_smooth, 'r--', linewidth=1.2, alpha=0.6, label='E_smooth_fab')
ax4b.set_ylabel('E_smooth_fabric [M_KK]', fontsize=10, color='red')
ax4b.tick_params(axis='y', labelcolor='red')

# --- Panel 5: Gradient ratio comparison ---
ax5 = fig.add_subplot(gs[2, 0])
ax5.plot(tau_values, grad_ratio_TB, 'b-', linewidth=1.5, label='R_grad (TB only)')
ax5.plot(tau_values, grad_ratio_fabric, 'r-', linewidth=2.0, label='R_grad (fabric)')
ax5.axhline(1.0, color='green', linestyle='--', linewidth=1.5, alpha=0.6, label='R = 1.0 threshold')
ax5.axhline(0.711, color='orange', linestyle=':', linewidth=1.5, alpha=0.6, label='S55 single-cell (0.71)')
# Mark S55 data points
s55_tau_pts = [0.00, 0.05, 0.10, 0.15, 0.19]
s55_R_pts = [1.110, 0.986, 0.419, 0.502, 0.711]
ax5.scatter(s55_tau_pts, s55_R_pts, marker='D', color='orange', s=50, zorder=5, label='S55 data points')
ax5.set_xlabel('tau', fontsize=11)
ax5.set_ylabel('Gradient ratio R', fontsize=11)
ax5.set_title('Gradient ratio: shell vs smooth (DECISIVE)', fontsize=11)
ax5.legend(fontsize=8, loc='best')
ax5.grid(True, alpha=0.2)
ax5.set_ylim(bottom=0)

# --- Panel 6: BA phonon spectrum at fold ---
ax6 = fig.add_subplot(gs[2, 1])
mode_indices = np.arange(1, N_CELLS)  # 1..31
ax6.bar(mode_indices, omega_BA[fold_idx], color='steelblue', alpha=0.7, width=0.7)
ax6.set_xlabel('Mode index n', fontsize=11)
ax6.set_ylabel('omega_n [M_KK]', fontsize=11)
ax6.set_title(f'BA phonon spectrum at fold (tau={fold_tau:.2f})', fontsize=11)
ax6.grid(True, alpha=0.2, axis='y')

# Summary text box
textstr = (f'STRUTINSKY-FABRIC-56: {verdict}\n'
           f'R_grad(fold) = {R_fold_fabric:.3f} (fabric)\n'
           f'R_grad(fold) = {R_fold_TB:.3f} (TB-only)\n'
           f'S55 single-cell = 0.711\n'
           f'R_max(fabric) = {R_max_fabric:.3f}')
props = dict(boxstyle='round', facecolor='lightyellow', alpha=0.8)
fig.text(0.5, 0.01, textstr, fontsize=10, ha='center', va='bottom', bbox=props,
         fontfamily='monospace')

plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
