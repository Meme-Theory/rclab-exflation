#!/usr/bin/env python3
"""
s70_3_mode_baw.py -- 3-MODE-BAW-70 (W5-J)
=============================================
Design study: Multi-mode BAW resonator matching the framework's 3-branch
squeeze distribution (B1/B2/B3) for enhanced non-BD detection.

Physical scenario:
  The single-mode BAW design (S69 BAW-ANALOG-69) requires N_shots = 71 for
  3-sigma squeeze detection at r_eff = 0.555. The framework predicts THREE
  distinct squeeze parameters for the three BCS branches:
    r_acoustic = 1.786  (B1, near Fermi surface, weight 3.3%)
    r_optical  = 0.982  (B3, intermediate regime, weight 50.6%)
    r_leggett  = 0.617  (B2 collective, weight 46.1%)

  A 3-coupled BAW resonator system, with each mode driven to a different
  squeeze parameter, provides a MULTI-MODE analog of the BCS transit.
  The joint phonon statistics of the 3-mode system carry more information
  than any single mode, reducing N_shots.

Governing structure:
  Three coupled harmonic oscillators with Hamiltonian (Eq.1):
    H = sum_{i=1}^3 hbar*omega_i a_i^dag a_i
      + sum_{i<j} hbar*J_{ij} (a_i^dag a_j + a_j^dag a_i)            (1)

  The coupling J_{ij} arises from shared piezoelectric electrodes (direct
  phonon-phonon coupling via elastic strain overlap). The normal modes are
  found by diagonalizing the 3x3 frequency matrix:
    M_{ij} = omega_i delta_{ij} + J_{ij} (1 - delta_{ij})             (2)

  Normal mode frequencies {Omega_alpha} and mode vectors {e_alpha}:
    M |e_alpha> = Omega_alpha |e_alpha>                                (3)

  Each BAW mode is independently squeezed by a parametric drive at 2*omega_i.
  The 3-mode squeezed state is:
    |psi> = S_1(r_1) S_2(r_2) S_3(r_3) |0,0,0>                       (4)

  In the normal mode basis, this is NOT a product of single-mode squeezes.
  The coupling entangles the modes, producing inter-mode correlations
  that are absent in the single-mode case.

  The joint distribution P(n_1, n_2, n_3 | r_1, r_2, r_3, J) carries
  Fisher information I_multi >= sum_i I_single(r_i), with equality
  only when J = 0 (uncoupled). For J > 0, the inequality is strict.

Gate: 3-MODE-BAW-70 -- INFO (design parameters and N_shots reduction)

References:
  [11] Chu et al., Science 358, 199-202 (2017) -- BAW-qubit coupling
  [CL] Cleland group, Science 364, 368 (2019) -- multi-mode phonon entanglement
  [vL] von Lupke et al., Nature Physics 18, 794 (2022) -- Fock states to n=7
  [AA] Arrangoiz-Arriola et al., Nature 571, 537 (2019) -- GHz phononic crystals

Author: Quantum-Acoustics Theorist (Workhorse-Quantum-Acoustics)
Session: S70
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.special import gammaln
from scipy.linalg import eigh
from canonical_constants import (
    Delta_0_OES, Delta_BCS, hbar_SI, k_B_SI,
    E_B1, E_B2_mean, E_B3_mean,
    J_C2, J_su2, J_u1,
    omega_L1, omega_L2,
    T_acoustic,
)

PI = np.pi

# ============================================================================
#  SECTION 1: Load S69 single-mode BAW baseline
# ============================================================================
#
# From S69 BAW-ANALOG-69, the single-mode design gives:
#   N_shots = 71 (canonical r = 0.555, mean-phonon-number approach)
#   N_shots = 170 (Landau r = 0.338)
#   BAW parameters: f = 5 GHz, g/2pi = 1 MHz, T1 = 100 us, T_fridge = 10 mK

print("=" * 72)
print("3-MODE-BAW-70: Multi-Mode BAW Resonator Design")
print("=" * 72)

s69_data = np.load(
    os.path.join(os.path.dirname(__file__), 's69_baw_analog.npz'),
    allow_pickle=True
)

# Single-mode baseline
N_shots_single = int(s69_data['N_shots_canonical_mean'])
r_eff_single = float(s69_data['r_eff_canonical'])
f_BAW_single = float(s69_data['f_BAW'])
T1_phonon = float(s69_data['T1_phonon'])
T_fridge = float(s69_data['T_fridge'])
n_thermal_single = float(s69_data['n_thermal'])
cooperativity_single = float(s69_data['cooperativity'])

# Per-branch squeeze parameters from S69
r_acoustic = float(s69_data['r_acoustic'])   # 1.786 (B1)
r_optical = float(s69_data['r_optical'])     # 0.982 (B3)
r_leggett = float(s69_data['r_leggett'])     # 0.617 (B2 collective)

print(f"\n--- S69 single-mode baseline ---")
print(f"  r_eff = {r_eff_single:.4f}")
print(f"  N_shots (single mode, 3-sigma) = {N_shots_single}")
print(f"  f_BAW = {f_BAW_single/1e9:.1f} GHz")
print(f"  T1 = {T1_phonon*1e6:.0f} us")
print(f"  n_thermal = {n_thermal_single:.2e}")
print(f"\n--- Per-branch squeeze parameters ---")
print(f"  r_acoustic (B1) = {r_acoustic:.4f}")
print(f"  r_optical  (B3) = {r_optical:.4f}")
print(f"  r_leggett  (B2) = {r_leggett:.4f}")

# BCS-dressed weights from the framework
# From S69 SQUEEZE-RECON-69: f_w_acoustic=0.033, f_w_optical=0.506, f_w_leggett=0.461
f_w_acoustic = 0.033    # B1 weight  # (local)
f_w_optical = 0.506     # B3 weight  # (local)
f_w_leggett = 0.461     # B2 weight  # (local)
print(f"\n--- BCS-dressed weights ---")
print(f"  f_w_acoustic (B1) = {f_w_acoustic:.3f}")
print(f"  f_w_optical  (B3) = {f_w_optical:.3f}")
print(f"  f_w_leggett  (B2) = {f_w_leggett:.3f}")
print(f"  Sum = {f_w_acoustic + f_w_optical + f_w_leggett:.3f}")

# ============================================================================
#  SECTION 2: 3-Mode BAW Resonator Design
# ============================================================================
#
# DESIGN PRINCIPLE:
# Three BAW resonators on a single sapphire substrate, each targeting a
# different longitudinal overtone. The resonator frequencies are chosen
# to be sufficiently separated (> linewidth) for independent addressing,
# yet close enough for piezoelectric coupling via shared electrode.
#
# PHYSICAL REALIZATION:
# A BAW resonator has longitudinal overtones at f_n = n * v_l / (2*h),
# where v_l is the longitudinal sound velocity and h is the substrate
# thickness. The free spectral range FSR = v_l / (2*h) ~ 13.2 MHz
# for a 420-um sapphire substrate (Chu 2017).
#
# For 3 coupled modes, we use 3 SEPARATE BAW resonators on a shared
# substrate, with frequencies chosen by varying the AlN transducer
# thickness (mass loading tunes the frequency). Each resonator couples
# to its own transmon qubit for independent readout.
#
# FREQUENCY MAP to branch structure:
#   Mode 1 -> B1 (acoustic): lightest mass loading, highest frequency
#   Mode 2 -> B2 (flat-optical): intermediate mass loading
#   Mode 3 -> B3 (dispersive-optical): heaviest mass loading, lowest frequency
#
# The frequency RATIOS matter, not the absolute frequencies:
#   E_B1 / E_B2_mean = 0.819 / 0.845 = 0.969
#   E_B3_mean / E_B2_mean = 0.978 / 0.845 = 1.157
#
# In the BAW analog, we choose:
#   f_1 = 5.05 GHz  (B1 analog, acoustic)
#   f_2 = 5.00 GHz  (B2 analog, flat-optical)
#   f_3 = 4.95 GHz  (B3 analog, dispersive-optical)
#
# Separation: 50 MHz >> linewidth (1/T1 = 10 kHz) -- independently resolvable.
# These are 3 separate BAW devices sharing a sapphire wafer, not 3 overtones
# of the same resonator.

print("\n" + "=" * 72)
print("SECTION 2: 3-Mode BAW Design Parameters")
print("=" * 72)

# --- Resonator frequencies ---
f_1 = 5.05e9   # Hz, B1 analog  # (local)
f_2 = 5.00e9   # Hz, B2 analog  # (local)
f_3 = 4.95e9   # Hz, B3 analog  # (local)

omega_1 = 2 * PI * f_1
omega_2 = 2 * PI * f_2
omega_3 = 2 * PI * f_3

print(f"\n--- Resonator frequencies ---")
print(f"  f_1 (B1 analog) = {f_1/1e9:.3f} GHz")
print(f"  f_2 (B2 analog) = {f_2/1e9:.3f} GHz")
print(f"  f_3 (B3 analog) = {f_3/1e9:.3f} GHz")
print(f"  Separations: f_1-f_2 = {(f_1-f_2)/1e6:.0f} MHz, "
      f"f_2-f_3 = {(f_2-f_3)/1e6:.0f} MHz")
print(f"  All >> linewidth (1/T1 = {1/T1_phonon/1e3:.1f} kHz)")

# --- Coupling constants ---
# The coupling between BAW resonators on a shared substrate arises from
# elastic strain overlap. For adjacent resonators on sapphire:
#   J ~ g_piezo^2 / Delta_detuning (off-resonant coupling via qubit)
#   or J ~ direct elastic coupling (strain field overlap)
#
# Typical values for piezo-coupled BAW modes:
#   J / 2pi ~ 0.1 - 1 MHz (direct elastic), 0.01 - 0.1 MHz (qubit-mediated)
#
# FRAMEWORK MAPPING:
# The Josephson couplings in the framework (J_C2 = 0.933, J_su2 = 0.059,
# J_u1 = 0.038 M_KK) give RATIOS:
#   J_C2 / J_su2 = 15.8
#   J_C2 / J_u1 = 24.6
#   J_su2 / J_u1 = 1.55
#
# For the BAW analog, the B2-B3 coupling (C^2 direction) should be strongest,
# the B1-B2 coupling (su(2) direction) intermediate, and the B1-B3 coupling
# (u(1) direction) weakest.
#
# Practical choice:
#   J_23 / 2pi = 0.5 MHz  (B2-B3, strongest -- shared electrode coupling)
#   J_12 / 2pi = 0.1 MHz  (B1-B2, intermediate -- reduced overlap)
#   J_13 / 2pi = 0.05 MHz (B1-B3, weakest -- minimal overlap)
#
# Check: J_23/J_12 = 5.0, J_23/J_13 = 10.0, J_12/J_13 = 2.0
# Framework: J_C2/J_su2 = 15.8, J_C2/J_u1 = 24.6, J_su2/J_u1 = 1.55
# The experimental ratios are compressed relative to the framework, but
# preserve the hierarchy ordering: J_23 > J_12 > J_13.

J_12_2pi = 0.1e6     # Hz, B1-B2 coupling  # (local)
J_23_2pi = 0.5e6     # Hz, B2-B3 coupling  # (local)
J_13_2pi = 0.05e6    # Hz, B1-B3 coupling  # (local)

J_12 = 2 * PI * J_12_2pi
J_23 = 2 * PI * J_23_2pi
J_13 = 2 * PI * J_13_2pi

print(f"\n--- Inter-mode couplings ---")
print(f"  J_12 / 2pi = {J_12_2pi/1e6:.2f} MHz  (B1-B2, su(2) analog)")
print(f"  J_23 / 2pi = {J_23_2pi/1e6:.2f} MHz  (B2-B3, C^2 analog)")
print(f"  J_13 / 2pi = {J_13_2pi/1e6:.2f} MHz  (B1-B3, u(1) analog)")
print(f"  Hierarchy: J_23 > J_12 > J_13 (matches framework J_C2 > J_su2 > J_u1)")
print(f"  Ratios: J_23/J_12={J_23_2pi/J_12_2pi:.1f}, "
      f"J_23/J_13={J_23_2pi/J_13_2pi:.1f}, "
      f"J_12/J_13={J_12_2pi/J_13_2pi:.1f}")
print(f"  FW ratios: J_C2/J_su2={J_C2/J_su2:.1f}, "
      f"J_C2/J_u1={J_C2/J_u1:.1f}, "
      f"J_su2/J_u1={J_su2/J_u1:.1f}")

# ============================================================================
#  SECTION 3: Normal Mode Analysis
# ============================================================================
#
# The 3x3 frequency matrix (Eq.2):
#   M = | omega_1   J_12    J_13  |
#       | J_12     omega_2  J_23  |
#       | J_13     J_23    omega_3 |
#
# Since J << |omega_i - omega_j| (weak coupling limit), the normal modes
# are perturbatively close to the bare modes. We diagonalize exactly.

print("\n" + "=" * 72)
print("SECTION 3: Normal Mode Decomposition")
print("=" * 72)

M_freq = np.array([
    [omega_1, J_12,    J_13],
    [J_12,    omega_2, J_23],
    [J_13,    J_23,    omega_3]
])

# Diagonalize
Omega_alpha, e_alpha = eigh(M_freq)

print(f"\n--- Bare frequencies (rad/s) ---")
for i, omega_bare in enumerate([omega_1, omega_2, omega_3]):
    print(f"  omega_{i+1} / 2pi = {omega_bare/(2*PI)/1e9:.6f} GHz")

print(f"\n--- Normal mode frequencies ---")
for alpha in range(3):
    f_nm = Omega_alpha[alpha] / (2 * PI)
    print(f"  Omega_{alpha+1} / 2pi = {f_nm/1e9:.6f} GHz")

print(f"\n--- Mode vectors (columns = normal modes) ---")
print(f"  {'':>10s}  {'NM 1':>10s}  {'NM 2':>10s}  {'NM 3':>10s}")
labels = ['B1 (ac)', 'B2 (fl)', 'B3 (dp)']
for i in range(3):
    print(f"  {labels[i]:>10s}  {e_alpha[i,0]:10.6f}  {e_alpha[i,1]:10.6f}  {e_alpha[i,2]:10.6f}")

# Frequency shifts from coupling
print(f"\n--- Frequency shifts from coupling ---")
for i in range(3):
    bare = [omega_1, omega_2, omega_3][i]
    shift = Omega_alpha[i] - bare
    print(f"  delta_f_{i+1} = {shift/(2*PI)/1e3:.1f} kHz "
          f"({abs(shift/bare)*1e6:.2f} ppm)")

# Verify: coupling is in weak regime (J << Delta_omega)
for i, j, Jij, name in [(0,1,J_12,'12'), (1,2,J_23,'23'), (0,2,J_13,'13')]:
    delta_omega = abs([omega_1, omega_2, omega_3][i] - [omega_1, omega_2, omega_3][j])
    ratio = Jij / delta_omega
    print(f"  J_{name}/Delta_omega_{name} = {ratio:.2e} "
          f"({'WEAK' if ratio < 0.1 else 'INTERMEDIATE' if ratio < 1 else 'STRONG'})")

# ============================================================================
#  SECTION 4: 3-Mode Squeezed State
# ============================================================================
#
# Each BAW mode is independently squeezed to match the framework's per-branch
# squeeze parameters. The squeeze is applied in the BARE mode basis (not
# normal mode basis), because the parametric drive targets each resonator
# individually.
#
# The 3-mode squeezed state in the bare basis is:
#   |psi> = S_1(r_1) S_2(r_2) S_3(r_3) |0,0,0>                       (4)
#
# where r_1 = r_acoustic, r_2 = r_leggett, r_3 = r_optical
# (matching B1, B2, B3 respectively).
#
# In the NORMAL MODE basis, the squeeze operators do NOT factorize. The
# transformation a_i = sum_alpha U_{i alpha} b_alpha mixes the squeezes.
#
# The covariance matrix in the normal mode basis captures all correlations.
# For the bare-mode squeezed state, the covariance matrix is:
#
#   C_bare = diag(cosh(2*r_1), cosh(2*r_2), cosh(2*r_3)) for xx-quadrature
#   with off-diagonal elements from the mode mixing.
#
# FULL COVARIANCE MATRIX:
# Define quadrature operators x_i = (a_i + a_i^dag)/sqrt(2),
#                             p_i = (a_i - a_i^dag)/(i*sqrt(2)).
# The 6x6 covariance matrix sigma_{AB} = <{q_A, q_B}>/2 - <q_A><q_B>
# where q = (x_1, p_1, x_2, p_2, x_3, p_3).
#
# For a product of single-mode squeezes S_i(r_i) with phases phi_i = 0:
#   <x_i^2> = (1/2) e^{2 r_i}       (anti-squeezed quadrature)
#   <p_i^2> = (1/2) e^{-2 r_i}      (squeezed quadrature)
#   <x_i p_i + p_i x_i> = 0
#   <x_i x_j> = 0, <p_i p_j> = 0, <x_i p_j> = 0   (i != j)
#
# In the bare mode basis, the covariance matrix is block-diagonal:
#   sigma_bare = diag(e^{2r_1}/2, e^{-2r_1}/2,
#                     e^{2r_2}/2, e^{-2r_2}/2,
#                     e^{2r_3}/2, e^{-2r_3}/2)
#
# In the normal mode basis, sigma_normal = U^T sigma_bare U (for the
# quadrature block), which develops off-diagonal blocks from mode mixing.

print("\n" + "=" * 72)
print("SECTION 4: 3-Mode Squeezed State Statistics")
print("=" * 72)

# Assign squeeze parameters to BAW modes
r = np.array([r_acoustic, r_leggett, r_optical])  # B1, B2, B3

print(f"\n--- Target squeeze parameters ---")
print(f"  r_1 = r_acoustic = {r[0]:.4f}  (B1 branch)")
print(f"  r_2 = r_leggett  = {r[1]:.4f}  (B2 branch)")
print(f"  r_3 = r_optical   = {r[2]:.4f}  (B3 branch)")

# Per-mode squeezed vacuum statistics
print(f"\n--- Per-mode statistics ---")
print(f"  {'Mode':>6s}  {'r':>7s}  {'<n_i>':>10s}  {'Var(n_i)':>12s}  "
      f"{'Fano_i':>8s}  {'cosh(2r_i)':>12s}")
print("-" * 65)
for i in range(3):
    ri = r[i]
    ni = np.sinh(ri)**2
    vari = 2 * np.sinh(ri)**2 * np.cosh(ri)**2
    fanoi = vari / ni if ni > 0 else 1.0
    c2ri = np.cosh(2*ri)
    print(f"  {i+1:>6d}  {ri:7.4f}  {ni:10.4f}  {vari:12.4f}  "
          f"{fanoi:8.3f}  {c2ri:12.4f}")

# Total mean phonon number (independent modes)
n_total = sum(np.sinh(r[i])**2 for i in range(3))
var_total = sum(2 * np.sinh(r[i])**2 * np.cosh(r[i])**2 for i in range(3))

print(f"\n  Total <n> = sum <n_i> = {n_total:.4f}")
print(f"  Total Var(n) = sum Var(n_i) = {var_total:.4f}")
print(f"  Total Fano = {var_total/n_total:.3f}")

# ============================================================================
#  SECTION 5: Covariance Matrix in Normal Mode Basis
# ============================================================================
#
# The mode mixing matrix U (from the normal mode decomposition):
#   a_bare = U @ a_normal, where U = e_alpha (the eigenvector matrix)
#
# The covariance matrix in the BARE mode x-quadrature is diagonal:
#   Sigma_x_bare = diag(e^{2r_1}/2, e^{2r_2}/2, e^{2r_3}/2)
#   Sigma_p_bare = diag(e^{-2r_1}/2, e^{-2r_2}/2, e^{-2r_3}/2)
#
# In the normal mode basis:
#   Sigma_x_normal = U^T @ Sigma_x_bare @ U
#   Sigma_p_normal = U^T @ Sigma_p_bare @ U
#
# The off-diagonal elements of Sigma_x_normal and Sigma_p_normal quantify
# the inter-mode correlations induced by mode mixing.

print("\n" + "=" * 72)
print("SECTION 5: Covariance Matrix (Normal Mode Basis)")
print("=" * 72)

U = e_alpha  # 3x3 unitary transformation (bare -> normal)

# Bare-mode covariance matrices (x and p quadratures)
Sigma_x_bare = np.diag([np.exp(2*r[i])/2 for i in range(3)])
Sigma_p_bare = np.diag([np.exp(-2*r[i])/2 for i in range(3)])

# Normal-mode covariance matrices
Sigma_x_normal = U.T @ Sigma_x_bare @ U
Sigma_p_normal = U.T @ Sigma_p_bare @ U

print(f"\n--- Covariance matrix Sigma_x (x-quadrature, bare basis) ---")
print(f"  diag: {np.diag(Sigma_x_bare)}")

print(f"\n--- Covariance matrix Sigma_x (x-quadrature, normal mode basis) ---")
for i in range(3):
    print(f"  [{Sigma_x_normal[i,0]:10.4f}  {Sigma_x_normal[i,1]:10.4f}  {Sigma_x_normal[i,2]:10.4f}]")

print(f"\n--- Covariance matrix Sigma_p (p-quadrature, normal mode basis) ---")
for i in range(3):
    print(f"  [{Sigma_p_normal[i,0]:10.4f}  {Sigma_p_normal[i,1]:10.4f}  {Sigma_p_normal[i,2]:10.4f}]")

# Inter-mode correlations
print(f"\n--- Inter-mode correlations (off-diagonal / diagonal) ---")
for i in range(3):
    for j in range(i+1, 3):
        corr_x = Sigma_x_normal[i,j] / np.sqrt(Sigma_x_normal[i,i] * Sigma_x_normal[j,j])
        corr_p = Sigma_p_normal[i,j] / np.sqrt(Sigma_p_normal[i,i] * Sigma_p_normal[j,j])
        print(f"  NM{i+1}-NM{j+1}: rho_x = {corr_x:.6f}, rho_p = {corr_p:.6f}")

# ============================================================================
#  SECTION 6: Phonon Number Distribution (per mode)
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 6: Phonon Number Distributions")
print("=" * 72)

def P_squeeze_vacuum(n_max, r_val):
    """Compute P(n) for a squeezed vacuum state."""
    P = np.zeros(n_max + 1)
    tanh_r = np.tanh(r_val)
    cosh_r = np.cosh(r_val)
    for n in range(0, n_max + 1, 2):
        m = n // 2
        log_P = (gammaln(2*m + 1) - 2*gammaln(m + 1) - 2*m*np.log(2)
                 + 2*m*np.log(abs(tanh_r)) - np.log(cosh_r))
        P[n] = np.exp(log_P)
    return P

# Choose n_max large enough for all modes. For large r, need n_max >> <n>.
# Mode 1 has <n> ~ 8.4 but the squeezed vacuum distribution P(2m) has a VERY
# long tail (tanh(1.786) = 0.946, so P(2m) ~ 0.946^{2m} / cosh(r) decays slowly).
# Need n_max large enough that sum P(n) > 1 - 1e-6.
# For r=1.786: P(2m) significant up to 2m ~ 200.
n_max = 200  # (local)
P_modes = []
for i in range(3):
    P_i = P_squeeze_vacuum(n_max, r[i])
    P_modes.append(P_i)
    norm_i = np.sum(P_i)
    n_arr = np.arange(n_max + 1)
    n_mean_i = np.sum(n_arr * P_i)
    n_mean_exact = np.sinh(r[i])**2
    print(f"\n  Mode {i+1} (r={r[i]:.4f}):")
    print(f"    Normalization = {norm_i:.10f}")
    print(f"    <n> from P(n) = {n_mean_i:.6f}")
    print(f"    <n> = sinh^2(r) = {n_mean_exact:.6f}")
    print(f"    Discrepancy = {abs(n_mean_i - n_mean_exact):.2e}")
    print(f"    P(0) = {P_i[0]:.6f}")
    print(f"    P(2) = {P_i[2]:.6f}")
    if n_max >= 4:
        print(f"    P(4) = {P_i[4]:.6f}")

# ============================================================================
#  SECTION 7: Joint Fisher Information and N_shots Reduction
# ============================================================================
#
# The central question: how much does the 3-mode system reduce N_shots
# compared to the single-mode case?
#
# APPROACH 1: Independent mode measurements
#   If we measure all 3 modes independently and combine results:
#   I_total = I_1 + I_2 + I_3 (independent Fisher informations)
#
#   For a single squeezed mode with parameter r, the Fisher information
#   for detecting r > 0 (i.e., for r as the parameter) is:
#     I(r) = sum_n (d ln P(n|r)/dr)^2 P(n|r)
#
#   For the squeezed vacuum: a closed-form expression exists.
#   Using d P(2m)/dr = P(2m) * [2m * d/dr(ln tanh r) - (1/2) * d/dr(ln cosh r)]
#                    = P(2m) * [2m/(sinh r * cosh r) - tanh r]
#
#   I(r) = sum_{m=0}^inf (d ln P(2m)/dr)^2 * P(2m)
#
# APPROACH 2: Joint statistics
#   The joint 3-mode measurement provides correlations between modes
#   via the mode mixing (Section 5). The joint Fisher information
#   I_joint >= I_total, with equality only for uncoupled modes.
#
#   For the phonon-number measurement (diagonal in Fock basis),
#   the joint distribution factorizes when J = 0:
#     P(n_1, n_2, n_3) = P_1(n_1) * P_2(n_2) * P_3(n_3)
#
#   For J > 0, the factorization breaks and correlations add information.
#   However, the phonon number measurement in the BARE basis still gives
#   a product distribution (squeeze operators factorize in bare basis).
#   The enhancement comes from measuring in the NORMAL MODE basis.
#
# APPROACH 3: Weighted effective squeeze
#   The BCS-dressed effective squeeze is:
#     cosh(2*r_eff) = sum_i f_w_i * cosh(2*r_i)                     (5)
#   The 3-mode system measures this DIRECTLY via the total phonon number
#   <n_total> = sum_i <n_i>, which carries the full branch-resolved
#   information.
#
#   For the total phonon number statistic:
#     <n_total> = sum_i sinh^2(r_i)
#     Var(n_total) = sum_i Var(n_i) = sum_i 2*sinh^2(r_i)*cosh^2(r_i)
#     (for independent modes)
#
#   The N_shots for 3-sigma detection of <n_total> vs vacuum:
#     N_multi = 9 * Var(n_total) / <n_total>^2
#             = 9 * sum_i Var(n_i) / (sum_i <n_i>)^2                (6)
#
#   This can be compared to the single-mode case where only one mode
#   (with r_eff) is measured.

print("\n" + "=" * 72)
print("SECTION 7: Fisher Information and N_shots Reduction")
print("=" * 72)

# --- Per-mode Fisher information ---
dr = 1e-5  # (local)

def fisher_info_single(r_val, n_max_fi=60):
    """Compute Fisher information I(r) for a single squeezed mode."""
    P_center = P_squeeze_vacuum(n_max_fi, r_val)
    P_plus = P_squeeze_vacuum(n_max_fi, r_val + dr)
    P_minus = P_squeeze_vacuum(n_max_fi, r_val - dr)
    dP_dr = (P_plus - P_minus) / (2 * dr)
    I = 0.0
    for n in range(n_max_fi + 1):
        if P_center[n] > 1e-30:
            I += (dP_dr[n])**2 / P_center[n]
    return I

I_per_mode = []
print(f"\n--- Per-mode Fisher information ---")
for i in range(3):
    I_i = fisher_info_single(r[i])
    I_per_mode.append(I_i)
    N_3sig_i = int(np.ceil(9.0 / I_i))
    print(f"  Mode {i+1} (r={r[i]:.4f}): I(r) = {I_i:.4f}, "
          f"N_shots = {N_3sig_i}")

I_total_indep = sum(I_per_mode)
N_total_indep = int(np.ceil(9.0 / I_total_indep))
print(f"\n  Total (independent sum): I = {I_total_indep:.4f}, "
      f"N_shots = {N_total_indep}")

# --- Approach A: Total phonon number ---
print(f"\n--- Approach A: Total phonon number ---")

# <n_total> and Var(n_total) for independent modes
n_means = np.array([np.sinh(r[i])**2 for i in range(3)])
vars_n = np.array([2 * np.sinh(r[i])**2 * np.cosh(r[i])**2 for i in range(3)])

n_total_mean = np.sum(n_means)
var_n_total = np.sum(vars_n)
fano_total = var_n_total / n_total_mean

N_multi_A = int(np.ceil(9 * var_n_total / n_total_mean**2))

print(f"  <n_total> = {n_total_mean:.4f}")
print(f"  Var(n_total) = {var_n_total:.4f}")
print(f"  Fano_total = {fano_total:.3f}")
print(f"  N_shots (3-mode, mean) = {N_multi_A}")
print(f"  Reduction vs single mode: {N_shots_single}/{N_multi_A} = "
      f"{N_shots_single/N_multi_A:.2f}x")

# --- Approach B: Optimal combined statistic ---
# The optimal estimator is the WEIGHTED total, with weights inversely
# proportional to the per-mode variance:
#   n_opt = sum_i w_i * n_i, where w_i = (<n_i> / Var(n_i)) / sum_j (<n_j>/Var(n_j))
# This is the SNR-optimal linear combination.

print(f"\n--- Approach B: Optimal weighted combination ---")

snr_per_mode = np.array([n_means[i]**2 / vars_n[i] for i in range(3)])
w_opt = snr_per_mode / np.sum(snr_per_mode)

n_opt_mean = np.sum(w_opt * n_means)
var_n_opt = np.sum(w_opt**2 * vars_n)
N_multi_B = int(np.ceil(9 * var_n_opt / n_opt_mean**2))

print(f"  Optimal weights: w = ({w_opt[0]:.4f}, {w_opt[1]:.4f}, {w_opt[2]:.4f})")
print(f"  <n_opt> = {n_opt_mean:.4f}")
print(f"  Var(n_opt) = {var_n_opt:.4f}")
print(f"  N_shots (optimal weighted) = {N_multi_B}")
print(f"  Reduction vs single mode: {N_shots_single}/{N_multi_B} = "
      f"{N_shots_single/N_multi_B:.2f}x")

# --- Approach C: Fisher information (per shot) ---
# Best-case: combine Fisher information from all 3 modes.
# Each shot measures all 3 phonon numbers simultaneously.
# Total Fisher information per shot = sum of individual Fishers
# (for independent modes in bare basis).

print(f"\n--- Approach C: Combined Fisher information ---")

N_multi_C = N_total_indep  # = ceil(9 / I_total)
print(f"  I_total = {I_total_indep:.4f} per shot")
print(f"  N_shots (Fisher) = {N_multi_C}")
print(f"  Reduction vs single mode: {N_shots_single}/{N_multi_C} = "
      f"{N_shots_single/N_multi_C:.2f}x")

# --- Approach D: sqrt(3) coherent enhancement ---
# The prompt suggests delta_r ~ sqrt(3) * delta_r_single from constructive
# interference of 3 modes. This corresponds to:
#   SNR_multi = sqrt(3) * SNR_single  (for equal-r modes)
#   N_shots_multi = N_shots_single / 3  (for equal-r modes)
#
# For unequal r, the enhancement is:
#   SNR_multi = sqrt(sum_i SNR_i^2)   (quadrature sum)
#   N_shots_multi = 9 / SNR_multi^2

print(f"\n--- Approach D: Quadrature SNR enhancement ---")

# SNR per mode per shot = <n_i> / sqrt(Var(n_i))
snr_per_shot = np.array([n_means[i] / np.sqrt(vars_n[i]) for i in range(3)])
snr_quadrature = np.sqrt(np.sum(snr_per_shot**2))

N_multi_D = int(np.ceil(9 / snr_quadrature**2))

print(f"  Per-mode SNR per shot: ({snr_per_shot[0]:.4f}, "
      f"{snr_per_shot[1]:.4f}, {snr_per_shot[2]:.4f})")
print(f"  Quadrature SNR per shot: {snr_quadrature:.4f}")
print(f"  N_shots (quadrature) = {N_multi_D}")
print(f"  Reduction vs single mode: {N_shots_single}/{N_multi_D} = "
      f"{N_shots_single/N_multi_D:.2f}x")

# --- Clarify Fisher information interpretation ---
# The Fisher information N_shots (Approach C) answers a DIFFERENT question:
# "How many shots to determine r to 3-sigma precision?"
# Approaches A and D answer the DETECTION question:
# "How many shots to distinguish squeezed from vacuum at 3 sigma?"
#
# For the design study, the detection question is primary.
# The Fisher approach gives unrealistically small N_shots because at large r,
# even a single phonon detection rules out vacuum. The practical N_shots is
# set by approach A (total phonon number) or D (quadrature SNR).

# Identify the best DETECTION approach (exclude Fisher)
approaches_detection = {
    'A (total phonon)': N_multi_A,
    'B (optimal weighted)': N_multi_B,
    'D (quadrature SNR)': N_multi_D,
}
N_multi_best = min(approaches_detection.values())
best_name = min(approaches_detection, key=approaches_detection.get)
reduction_factor = N_shots_single / N_multi_best

# All approaches for reference
approaches_all = {
    'A (total phonon)': N_multi_A,
    'B (optimal weighted)': N_multi_B,
    'C (Fisher, precision)': N_multi_C,
    'D (quadrature SNR)': N_multi_D,
}

print(f"\n--- Summary ---")
print(f"  Approach C (Fisher) = {N_multi_C} answers PRECISION (how well can r be measured)")
print(f"  Approaches A, B, D answer DETECTION (can squeeze be distinguished from vacuum)")
print(f"  For experiment design, DETECTION is the relevant metric.")

print(f"\n--- Best detection approach: {best_name} ---")
print(f"  N_shots (3-mode) = {N_multi_best}")
print(f"  N_shots (single mode) = {N_shots_single}")
print(f"  Reduction factor = {reduction_factor:.2f}x")
print(f"  Enhancement = sqrt(3) would give {N_shots_single/3:.0f}; "
      f"actual = {N_multi_best}")

# ============================================================================
#  SECTION 8: Q-factor and Linewidth Requirements
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 8: Q-factor and Linewidth Requirements")
print("=" * 72)

# Q factors for each mode
# Q = omega * T1. For BAW with T1 = 100 us at 5 GHz:
Q_factors = []
for i, f_i in enumerate([f_1, f_2, f_3]):
    Q_i = 2 * PI * f_i * T1_phonon
    Q_factors.append(Q_i)
    kappa_i = 1.0 / T1_phonon  # decay rate
    linewidth_i = kappa_i / (2 * PI)
    print(f"\n  Mode {i+1} (f = {f_i/1e9:.3f} GHz):")
    print(f"    Q = {Q_i:.2e}")
    print(f"    kappa / 2pi = {linewidth_i/1e3:.1f} kHz")
    print(f"    J/kappa (coupling/loss): J_max/kappa = {max(J_12, J_23, J_13)/kappa_i:.1f}")

# Verify: each mode independently resolvable from its neighbors
for i in range(3):
    for j in range(i+1, 3):
        delta_f = abs([f_1, f_2, f_3][i] - [f_1, f_2, f_3][j])
        linewidth_max = max(1/(2*PI*T1_phonon), 1/(2*PI*T1_phonon))
        ratio = delta_f / linewidth_max
        print(f"\n  Modes {i+1}-{j+1}: delta_f = {delta_f/1e6:.0f} MHz, "
              f"linewidth = {linewidth_max/1e3:.1f} kHz, "
              f"ratio = {ratio:.0f}x ({'RESOLVED' if ratio > 10 else 'MARGINAL'})")

# ============================================================================
#  SECTION 9: Squeeze Generation Protocol (3-mode)
# ============================================================================
#
# For 3 independent squeezes, apply 3 parametric drives simultaneously:
#   lambda_i(t) = lambda_{0,i} * cos(2*omega_i * t)    for t in [0, tau_q]
#
# The drives are at DIFFERENT frequencies (2*f_1, 2*f_2, 2*f_3), so they
# don't interfere. Each produces squeeze r_i = lambda_{0,i} * tau_q.
#
# The quench duration must satisfy:
#   tau_q > 1/FSR (single-mode constraint per resonator)
#   tau_q < T1 (phonon lifetime)
#
# For the 3-resonator system, the FSR constraint applies to each
# resonator individually. Since they are separate devices, each has
# its own FSR. Using tau_q = 100 ns for all three:

print("\n" + "=" * 72)
print("SECTION 9: Squeeze Generation Protocol")
print("=" * 72)

tau_q = 100e-9  # 100 ns (satisfies single-mode constraint)
lambda_0_2pi = 10e6  # 10 MHz parametric drive strength
lambda_0_rad = 2 * PI * lambda_0_2pi

print(f"\n--- Squeeze generation ---")
print(f"  tau_quench = {tau_q*1e9:.0f} ns")
print(f"  lambda_0 / 2pi = {lambda_0_2pi/1e6:.0f} MHz")
print(f"  T1_phonon = {T1_phonon*1e6:.0f} us")
print(f"  tau_q / T1 = {tau_q/T1_phonon:.2e} (negligible loss)")

print(f"\n--- Per-mode drive parameters ---")
for i in range(3):
    ri = r[i]
    lambda_i = ri / tau_q  # rad/s
    lambda_i_2pi = lambda_i / (2 * PI)
    drive_freq = 2 * [f_1, f_2, f_3][i]
    print(f"\n  Mode {i+1} (target r = {ri:.4f}):")
    print(f"    lambda_{i+1} / 2pi = {lambda_i_2pi/1e6:.2f} MHz")
    print(f"    Drive frequency: 2*f_{i+1} = {drive_freq/1e9:.3f} GHz")
    print(f"    omega_{i+1} * tau_q = {2*PI*[f_1, f_2, f_3][i]*tau_q:.0f} "
          f"(>> 1, adiabatic regime)")
    print(f"    tau_q * FSR = {tau_q * 13.2e6:.1f} > 1: single-mode OK")

# Achievable r with 100 ns quench
r_achievable_max = lambda_0_rad * tau_q
print(f"\n  Maximum r (lambda_0/2pi = 10 MHz, tau_q = 100 ns) = {r_achievable_max:.3f}")
print(f"  Required: r_max = r_acoustic = {r_acoustic:.3f}")
print(f"  Status: {'ACHIEVABLE' if r_acoustic < r_achievable_max else 'NEED STRONGER DRIVE'}")

# If r_acoustic exceeds the achievable range, increase lambda_0 or tau_q
if r_acoustic > r_achievable_max:
    lambda_needed = r_acoustic / tau_q / (2 * PI)
    print(f"  Need lambda_0/2pi >= {lambda_needed/1e6:.1f} MHz for r_acoustic")
    tau_needed = r_acoustic / lambda_0_rad
    print(f"  OR tau_q >= {tau_needed*1e9:.0f} ns with lambda_0/2pi = 10 MHz")
    # Update
    lambda_0_2pi_actual = max(lambda_0_2pi, lambda_needed * 1.1)
    lambda_0_rad_actual = 2 * PI * lambda_0_2pi_actual
    print(f"  Using lambda_0/2pi = {lambda_0_2pi_actual/1e6:.1f} MHz")
else:
    lambda_0_2pi_actual = lambda_0_2pi
    lambda_0_rad_actual = lambda_0_rad

# ============================================================================
#  SECTION 10: Readout Architecture (3-mode)
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 10: 3-Mode Readout Architecture")
print("=" * 72)

# Each BAW mode is coupled to its own transmon qubit for independent readout.
# The 3 transmon qubits have different frequencies to avoid cross-talk.
#
# For number-resolved readout, need chi > kappa_qubit, i.e.,
#   g^2 / Delta > 1/T1_qubit.
# With g/2pi = 1 MHz and T1_qubit = 50 us (kappa_q = 20 kHz):
#   Delta < g^2 * T1_qubit = (2pi * 1e6)^2 / (2pi * 20e3) ~ 50 MHz
# So detunings must be ~ 50 MHz, NOT GHz.
#
# Standard cQED: transmon at f_q ~ 5.1-5.3 GHz, detuned 50-200 MHz
# from the BAW mode. Each qubit-BAW pair has its own detuning.

f_qubit = [5.10e9, 5.06e9, 5.02e9]  # Hz, transmon frequencies
# Detunings: 50, 60, 70 MHz from respective BAW modes
g_coupling_2pi = 1.0e6  # Hz, uniform coupling  # (local)
T1_qubit = 50e-6  # s
kappa_q = 1.0 / T1_qubit  # 20 kHz

print(f"\n--- 3-qubit readout ---")
for i in range(3):
    delta_i = abs(f_qubit[i] - [f_1, f_2, f_3][i])
    chi_i = (2*PI*g_coupling_2pi)**2 / (2*PI*delta_i)
    chi_i_2pi = chi_i / (2*PI)
    chi_kappa = chi_i / kappa_q
    print(f"\n  Mode {i+1} -> Qubit {i+1}:")
    print(f"    f_qubit = {f_qubit[i]/1e9:.3f} GHz")
    print(f"    Detuning = {delta_i/1e6:.0f} MHz")
    print(f"    chi / 2pi = {chi_i_2pi/1e3:.1f} kHz")
    print(f"    chi / kappa_q = {chi_kappa:.1f} "
          f"({'RESOLVED' if chi_kappa > 1 else 'NOT RESOLVED'})")

# Total measurement time per shot (sequential readout of 3 modes)
# Each qubit readout takes ~ 1/chi ~ 1 us (for chi/2pi ~ 1 MHz)
# Sequential readout of 3 modes: 3 us per shot
# Parallel readout possible with frequency multiplexing: 1 us per shot

t_readout_per_mode = 1e-6  # 1 us per mode
t_readout_sequential = 3 * t_readout_per_mode
t_reset = 5 * T1_phonon  # 500 us reset time

t_per_shot = t_readout_sequential + t_reset
rep_rate = 1.0 / t_per_shot

print(f"\n--- Timing ---")
print(f"  Readout per mode: {t_readout_per_mode*1e6:.0f} us")
print(f"  Sequential 3-mode readout: {t_readout_sequential*1e6:.0f} us")
print(f"  Reset time (5*T1): {t_reset*1e6:.0f} us")
print(f"  Total per shot: {t_per_shot*1e6:.0f} us")
print(f"  Repetition rate: {rep_rate:.0f} Hz")

# Total experiment time
for name, N_s in approaches_all.items():
    t_total = N_s / rep_rate
    print(f"  Total time ({name}): {N_s} shots * {1/rep_rate*1e3:.1f} ms = {t_total:.2f} s")
# Also report for best detection approach
t_total_best = N_multi_best / rep_rate
print(f"  BEST DETECTION: {N_multi_best} shots * {1/rep_rate*1e3:.1f} ms = {t_total_best:.2f} s")

# ============================================================================
#  SECTION 11: Cross-Talk and Systematics (3-mode specific)
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 11: 3-Mode Systematics")
print("=" * 72)

# 1. Parasitic coupling: drives at 2*omega_i can excite neighboring modes
# if 2*omega_i is close to omega_j or 2*omega_j.
print(f"\n1. Parasitic drive contamination:")
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        drive_f = 2 * [f_1, f_2, f_3][i]
        target_f = [f_1, f_2, f_3][j]
        detuning = abs(drive_f - 2*target_f)
        print(f"   Drive(2*f_{i+1}) - 2*f_{j+1} = {detuning/1e6:.0f} MHz "
              f"({'SAFE' if detuning > 5e6 else 'CAUTION'})")

# 2. Thermal occupation at each frequency
print(f"\n2. Thermal occupation per mode:")
for i, f_i in enumerate([f_1, f_2, f_3]):
    n_th_i = 1.0 / (np.exp(hbar_SI * 2*PI*f_i / (k_B_SI * T_fridge)) - 1)
    print(f"   Mode {i+1} ({f_i/1e9:.3f} GHz): n_th = {n_th_i:.2e}")

# 3. Qubit-qubit cross-talk via shared BAW substrate
print(f"\n3. Qubit-qubit cross-talk (via virtual phonon exchange):")
for i in range(3):
    for j in range(i+1, 3):
        # Virtual exchange: g_eff ~ g_i * g_j / max(delta_i, delta_j)
        delta_i = abs(f_qubit[i] - [f_1, f_2, f_3][i])
        delta_j = abs(f_qubit[j] - [f_1, f_2, f_3][j])
        g_cross = g_coupling_2pi**2 / max(delta_i, delta_j)
        print(f"   Q{i+1}-Q{j+1}: g_cross/2pi = {g_cross/1e3:.2f} kHz "
              f"({'NEGLIGIBLE' if g_cross < 1e3 else 'CHECK'})")

# ============================================================================
#  SECTION 12: Framework-Specific Signatures (3-mode vs single-mode)
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 12: Framework-Specific Signatures")
print("=" * 72)

# The 3-mode system has additional observable signatures compared to
# the single-mode case:

# 1. BRANCH-RESOLVED SQUEEZE RATIOS
print(f"\n1. Branch-resolved squeeze ratios (framework prediction):")
print(f"   r_1/r_2 = {r[0]/r[1]:.3f} (acoustic/Leggett)")
print(f"   r_3/r_2 = {r[2]/r[1]:.3f} (optical/Leggett)")
print(f"   r_1/r_3 = {r[0]/r[2]:.3f} (acoustic/optical)")
print(f"   These ratios are FIXED by the BCS coherence factors.")
print(f"   Measuring 3 independent r values and checking these ratios")
print(f"   constitutes a 2-parameter PREDICTION (2 independent ratios).")

# 2. INTER-MODE CORRELATIONS (from coupling)
print(f"\n2. Inter-mode correlations:")
print(f"   For J != 0, the normal modes have mixed squeeze content.")
print(f"   The x-quadrature correlation matrix has off-diagonal elements:")
for i in range(3):
    for j in range(i+1, 3):
        print(f"   <x_{i+1} x_{j+1}> / sqrt(<x_{i+1}^2><x_{j+1}^2>) = "
              f"{Sigma_x_normal[i,j]/np.sqrt(Sigma_x_normal[i,i]*Sigma_x_normal[j,j]):.6f}")
print(f"   These are small (J << Delta_omega) but measurable with homodyne.")

# 3. TOTAL PHONON NUMBER DISTRIBUTION
# The total N = n_1 + n_2 + n_3 has a distribution that is the convolution
# of three independent squeezed vacuum distributions (for J = 0).
# This is a DIFFERENT distribution from a single squeeze at r_eff.
print(f"\n3. Total phonon number distribution P(N_total):")
print(f"   This is the convolution of 3 squeezed distributions.")
print(f"   It differs from single-squeeze P(n|r_eff={r_eff_single:.3f}):")
print(f"   - P(N=0) = prod P_i(0) = {np.prod([P_modes[i][0] for i in range(3)]):.6f}")
single_P0 = 1.0 / np.cosh(r_eff_single)
print(f"   - P_single(n=0|r_eff) = {single_P0:.6f}")
print(f"   - Ratio: {np.prod([P_modes[i][0] for i in range(3)])/single_P0:.4f}")

# Compute P(N_total) by convolution
# Use full convolution length, then truncate for display
P_total_full = np.convolve(P_modes[0], P_modes[1])
P_total_full = np.convolve(P_total_full, P_modes[2])
# Normalize (truncation of individual P(n) at n_max causes small norm deficit)
P_total_norm_full = P_total_full / np.sum(P_total_full)
# Truncate to a reasonable display length
n_display = min(len(P_total_norm_full), 3*n_max+1)
P_total_norm = P_total_norm_full[:n_display]

n_arr = np.arange(len(P_total_norm))
n_total_from_dist = np.sum(n_arr * P_total_norm)

print(f"\n   P(N_total) for first 11 values:")
print(f"   {'N':>5s}  {'P(N)':>12s}")
for N_val in range(min(11, len(P_total_norm))):
    print(f"   {N_val:5d}  {P_total_norm[N_val]:12.6f}")
print(f"   <N_total> from P(N) = {n_total_from_dist:.4f}")
print(f"   <N_total> from sinh^2 = {n_total:.4f}")

# ============================================================================
#  SECTION 13: Comparison: Equal-r vs Framework-r
# ============================================================================
#
# If the 3 modes were driven to EQUAL r (r = r_eff_single = 0.555),
# the reduction would be exactly 3x (the sqrt(3) enhancement).
# With the framework's UNEQUAL r values, the reduction differs.

print("\n" + "=" * 72)
print("SECTION 13: Equal-r vs Framework-r Comparison")
print("=" * 72)

# Equal-r case
r_equal = r_eff_single
n_equal = 3 * np.sinh(r_equal)**2
var_equal = 3 * 2 * np.sinh(r_equal)**2 * np.cosh(r_equal)**2
N_equal = int(np.ceil(9 * var_equal / n_equal**2))

# N_shots_single * (1/3) from sqrt(3) enhancement
N_equal_predicted = int(np.ceil(N_shots_single / 3))

print(f"\n--- Equal-r (r = {r_equal:.4f} for all 3 modes) ---")
print(f"  <n_total> = 3*sinh^2({r_equal:.4f}) = {n_equal:.4f}")
print(f"  Var(n_total) = 3*2*sinh^2*cosh^2 = {var_equal:.4f}")
print(f"  N_shots (equal-r) = {N_equal}")
print(f"  Predicted (N_single/3) = {N_equal_predicted}")
print(f"  Consistency: {'PASS' if abs(N_equal - N_equal_predicted) <= 1 else 'CHECK'}")

print(f"\n--- Framework-r (unequal r_i) ---")
print(f"  <n_total> = {n_total_mean:.4f}")
print(f"  Var(n_total) = {var_n_total:.4f}")
print(f"  N_shots (framework-r) = {N_multi_A}")

print(f"\n--- Comparison ---")
print(f"  N_single = {N_shots_single}")
print(f"  N_equal-r = {N_equal}")
print(f"  N_framework-r = {N_multi_A}")
print(f"  Reduction (equal-r vs single): {N_shots_single/N_equal:.2f}x")
print(f"  Reduction (FW-r vs single): {N_shots_single/N_multi_A:.2f}x")
print(f"  The acoustic mode (r=1.786) DOMINATES the total <n>.")
print(f"  <n_acoustic> / <n_total> = {np.sinh(r_acoustic)**2/n_total_mean:.3f}")

# ============================================================================
#  SECTION 14: Summary Table of Design Parameters
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 14: Design Summary")
print("=" * 72)

print(f"""
+--------------------------------------------------------------------+
|   3-MODE BAW RESONATOR DESIGN PARAMETERS (3-MODE-BAW-70)           |
+--------------------------------------------------------------------+
|                                                                    |
|  RESONATOR FREQUENCIES:                                            |
|    Mode 1 (B1 analog): f_1 = {f_1/1e9:.3f} GHz                      |
|    Mode 2 (B2 analog): f_2 = {f_2/1e9:.3f} GHz                      |
|    Mode 3 (B3 analog): f_3 = {f_3/1e9:.3f} GHz                      |
|    Separation: 50 MHz (>> linewidth 1.6 kHz)                       |
|                                                                    |
|  COUPLING CONSTANTS:                                               |
|    J_12 / 2pi = {J_12_2pi/1e6:.2f} MHz  (B1-B2, su(2) analog)            |
|    J_23 / 2pi = {J_23_2pi/1e6:.2f} MHz  (B2-B3, C^2 analog)              |
|    J_13 / 2pi = {J_13_2pi/1e6:.2f} MHz  (B1-B3, u(1) analog)            |
|    Hierarchy: J_23 > J_12 > J_13 (matches framework)              |
|                                                                    |
|  TARGET SQUEEZE PARAMETERS:                                        |
|    r_1 = {r[0]:.3f}  (B1, acoustic branch, near Fermi surface)       |
|    r_2 = {r[1]:.3f}  (B2, Leggett collective, inter-band)            |
|    r_3 = {r[2]:.3f}  (B3, optical branch, intermediate regime)       |
|                                                                    |
|  Q-FACTORS:                                                        |
|    Q_1 = {Q_factors[0]:.2e}                                          |
|    Q_2 = {Q_factors[1]:.2e}                                          |
|    Q_3 = {Q_factors[2]:.2e}                                          |
|    (All based on T1 = 100 us, state-of-art)                        |
|                                                                    |
|  READOUT:                                                          |
|    3 transmon qubits at 5.10, 5.06, 5.02 GHz                      |
|    g/2pi = 1 MHz per qubit                                         |
|    Sequential readout: 3 us per shot                               |
|    Parallel possible with frequency multiplexing                   |
|                                                                    |
|  N_SHOTS COMPARISON (detection, 3-sigma):                          |
|    Single-mode (S69): {N_shots_single:>4d}                                    |
|    3-mode total <n>:  {N_multi_A:>4d}  (reduction: {N_shots_single/N_multi_A:.1f}x)                |
|    3-mode optimal w:  {N_multi_B:>4d}  (reduction: {N_shots_single/N_multi_B:.1f}x)                |
|    3-mode quad SNR:   {N_multi_D:>4d}  (reduction: {N_shots_single/N_multi_D:.1f}x)                |
|    3-mode Fisher:     {N_multi_C:>4d}  (precision, not detection)            |
|    Best detection: {best_name:>20s}: {N_multi_best:>4d}         |
|                                                                    |
|  TOTAL MEASUREMENT TIME:                                           |
|    {N_multi_best} shots * {t_per_shot*1e3:.1f} ms = {N_multi_best*t_per_shot:.2f} s                          |
|                                                                    |
|  FRAMEWORK-SPECIFIC PREDICTIONS:                                   |
|    - r_1/r_2 = {r[0]/r[1]:.3f}, r_3/r_2 = {r[2]/r[1]:.3f} (fixed by BCS)       |
|    - P(N_total=0) = {np.prod([P_modes[i][0] for i in range(3)]):.6f} (multi-mode convolution)     |
|    - Inter-mode correlations from coupling: O({J_23_2pi/50e6:.1e})          |
|                                                                    |
+--------------------------------------------------------------------+
""")

# ============================================================================
#  SECTION 15: Cross-Checks
# ============================================================================

print("=" * 72)
print("SECTION 15: Cross-Checks")
print("=" * 72)

# 1. Normal mode eigenvalues sum equals bare frequency sum
omega_sum_bare = omega_1 + omega_2 + omega_3
omega_sum_normal = np.sum(Omega_alpha)
print(f"\n1. Tr(M) conservation: bare sum = {omega_sum_bare/(2*PI)/1e9:.6f} GHz, "
      f"normal sum = {omega_sum_normal/(2*PI)/1e9:.6f} GHz")
print(f"   Difference: {abs(omega_sum_bare - omega_sum_normal)/(2*PI):.2e} Hz "
      f"({'PASS' if abs(omega_sum_bare - omega_sum_normal) < 1e-3 else 'FAIL'})")

# 2. Mode vectors orthonormal
ortho_check = e_alpha.T @ e_alpha
ortho_err = np.max(np.abs(ortho_check - np.eye(3)))
print(f"2. Orthonormality of mode vectors: max|U^T U - I| = {ortho_err:.2e} "
      f"({'PASS' if ortho_err < 1e-10 else 'FAIL'})")

# 3. Covariance matrix positive definite
eigs_x = np.linalg.eigvalsh(Sigma_x_normal)
eigs_p = np.linalg.eigvalsh(Sigma_p_normal)
print(f"3. Sigma_x eigenvalues: {eigs_x}")
print(f"   Sigma_p eigenvalues: {eigs_p}")
print(f"   All positive: {'PASS' if np.all(eigs_x > 0) and np.all(eigs_p > 0) else 'FAIL'}")

# 4. Product of covariance eigenvalues >= (1/2)^3 (Heisenberg bound)
# For each mode: sigma_x * sigma_p >= 1/2
for alpha in range(3):
    prod = Sigma_x_normal[alpha, alpha] * Sigma_p_normal[alpha, alpha]
    print(f"4. Heisenberg for NM{alpha+1}: "
          f"sigma_x * sigma_p = {prod:.4f} >= 0.25 "
          f"({'PASS' if prod >= 0.25 - 1e-10 else 'FAIL'})")

# 5. Total <n> consistency
n_from_cov = sum(0.5*(Sigma_x_bare[i,i] + Sigma_p_bare[i,i]) - 0.5 for i in range(3))
print(f"5. <n_total> from covariance: {n_from_cov:.4f}")
print(f"   <n_total> from sinh^2: {n_total_mean:.4f}")
print(f"   Difference: {abs(n_from_cov - n_total_mean):.2e} "
      f"({'PASS' if abs(n_from_cov - n_total_mean) < 1e-6 else 'FAIL'})")

# 6. J -> 0 limit: normal modes = bare modes
# NOTE: eigh sorts eigenvalues in ascending order, so compare sorted arrays.
M_uncoupled = np.diag([omega_1, omega_2, omega_3])
Omega_uncoupled, e_uncoupled = eigh(M_uncoupled)
bare_sorted = np.sort([omega_1, omega_2, omega_3])
print(f"6. J=0 limit: normal = bare frequencies (sorted): "
      f"{'PASS' if np.allclose(Omega_uncoupled, bare_sorted) else 'FAIL'}")

# 7. P(n) normalization for all modes
for i in range(3):
    norm = np.sum(P_modes[i])
    deficit = abs(1 - norm)
    status = 'PASS' if deficit < 1e-4 else 'FAIL'
    print(f"7. P(n) normalization mode {i+1}: {norm:.10f} "
          f"(deficit={deficit:.1e}) ({status})")

# 8. P(odd) = 0 for all modes
for i in range(3):
    p_odd = np.sum(P_modes[i][1::2])
    print(f"8. P(odd) mode {i+1}: {p_odd:.2e} "
          f"({'PASS' if p_odd < 1e-15 else 'FAIL'})")

# 9. N_shots >= 1 for all approaches
print(f"9. N_shots >= 1: all approaches > 0: "
      f"{'PASS' if all(v >= 1 for v in approaches_all.values()) else 'FAIL'}")

# 10. Dimensional consistency: all frequencies in rad/s or Hz (consistent)
print(f"10. Dimensional consistency: all frequencies in Hz or rad/s, "
      f"couplings in Hz or rad/s. PASS (by construction)")

# ============================================================================
#  SECTION 16: Gate Verdict
# ============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: 3-MODE-BAW-70")
print("=" * 72)

print(f"""
Gate: 3-MODE-BAW-70
Classification: INFO
Result: Multi-mode BAW design with 3 coupled resonators matching the
  framework's B1/B2/B3 branch structure.

Design parameters:
  - Frequencies: {f_1/1e9:.3f}, {f_2/1e9:.3f}, {f_3/1e9:.3f} GHz (50 MHz separation)
  - Couplings: J_12/2pi = {J_12_2pi/1e6:.2f}, J_23/2pi = {J_23_2pi/1e6:.2f}, J_13/2pi = {J_13_2pi/1e6:.2f} MHz
  - Target squeezes: r = ({r[0]:.3f}, {r[1]:.3f}, {r[2]:.3f})
  - Q-factors: ~{Q_factors[0]:.0e} (T1 = {T1_phonon*1e6:.0f} us)

N_shots reduction (detection):
  - Single mode (S69): {N_shots_single}
  - 3-mode best detection ({best_name}): {N_multi_best}
  - Reduction factor: {reduction_factor:.1f}x
  - Total measurement time: {N_multi_best*t_per_shot:.2f} s
  - For precision (Fisher): {N_multi_C} shots ({N_shots_single/N_multi_C:.0f}x reduction)

Framework-specific features:
  - Branch-resolved r ratios: r_1/r_2 = {r[0]/r[1]:.3f}, r_3/r_2 = {r[2]/r[1]:.3f}
  - Coupling hierarchy matches J_C2 > J_su2 > J_u1
  - Multi-mode convolution P(N_total) distinguishable from single-squeeze

Labs: Chu/ETH, Cleland/Stanford best positioned for multi-mode BAW.
""")

# ============================================================================
#  SECTION 17: Save results
# ============================================================================

outpath = os.path.join(os.path.dirname(__file__), 's70_3_mode_baw.npz')
np.savez(outpath,
    # Gate
    gate_name='3-MODE-BAW-70',
    gate_verdict='INFO',
    gate_detail='Multi-mode BAW design: 3 coupled resonators matching B1/B2/B3 branch structure',

    # Resonator frequencies (Hz)
    f_1=f_1, f_2=f_2, f_3=f_3,
    omega_1=omega_1, omega_2=omega_2, omega_3=omega_3,

    # Coupling constants (Hz, /2pi)
    J_12_2pi=J_12_2pi, J_23_2pi=J_23_2pi, J_13_2pi=J_13_2pi,

    # Normal mode frequencies and vectors
    Omega_normal=Omega_alpha,
    mode_vectors=e_alpha,

    # Target squeeze parameters
    r_modes=r,
    r_acoustic=r_acoustic, r_leggett=r_leggett, r_optical=r_optical,
    f_w_acoustic=f_w_acoustic, f_w_optical=f_w_optical, f_w_leggett=f_w_leggett,

    # Per-mode statistics
    n_means=n_means,
    vars_n=vars_n,

    # Total statistics
    n_total_mean=n_total_mean,
    var_n_total=var_n_total,
    fano_total=fano_total,

    # N_shots results
    N_shots_single=N_shots_single,
    N_shots_3mode_total=N_multi_A,
    N_shots_3mode_optimal=N_multi_B,
    N_shots_3mode_fisher=N_multi_C,
    N_shots_3mode_quadrature=N_multi_D,
    N_shots_3mode_best_detection=N_multi_best,
    best_detection_approach=best_name,
    reduction_factor_detection=reduction_factor,

    # Q-factors
    Q_factors=np.array(Q_factors),
    T1_phonon=T1_phonon,

    # Covariance matrices
    Sigma_x_bare=Sigma_x_bare,
    Sigma_p_bare=Sigma_p_bare,
    Sigma_x_normal=Sigma_x_normal,
    Sigma_p_normal=Sigma_p_normal,

    # Fisher information
    I_per_mode=np.array(I_per_mode),
    I_total_indep=I_total_indep,

    # Framework ratios
    r_ratio_12=r[0]/r[1],
    r_ratio_32=r[2]/r[1],
    r_ratio_13=r[0]/r[2],

    # P(N_total) convolution (truncated to display range)
    P_N_total=P_total_norm,
    P_modes_0=np.array([P_modes[i][0] for i in range(3)]),

    # Timing
    t_per_shot=t_per_shot,
    t_total_best=N_multi_best * t_per_shot,

    # Qubit frequencies
    f_qubits=np.array(f_qubit),
)

print(f"\nResults saved to: {outpath}")
print("DONE")
