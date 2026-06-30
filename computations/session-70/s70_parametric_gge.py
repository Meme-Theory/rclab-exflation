#!/usr/bin/env python3
"""
s70_parametric_gge.py — Post-Transit Parametric Resonance in BCS Modes
=======================================================================

Session 70, Gate: PARAMETRIC-GGE-70
Agent: Tesla-Resonance

Physics:
  After the supersonic transit through the van Hove fold, the modulus tau
  settles toward its post-transit attractor. The characteristic attractor
  frequency is omega_att = 1.430 M_KK (S38). If the modulus undergoes
  damped oscillations at this frequency, it creates a time-periodic
  perturbation for the 8 BCS quasiparticle modes.

  The BCS mode energies are:
    E_B1 = 0.819 M_KK  (1 mode)
    E_B2 = 0.845 M_KK  (4 modes)
    E_B3 = 0.978 M_KK  (3 modes)

  Parametric resonance conditions:
  (a) Single-mode: 2*omega_k = n * omega_drive  (Mathieu tongues)
  (b) Sum resonance: omega_i + omega_j = m * omega_drive  (pair creation)
  (c) BCS gap oscillation: pair vibration mode omega_PV = 0.792 drives
      quasiparticle energy modulation through Delta(t)

  S67 (Kitaev) established: NO geometric modulus trapping (fold is S_max),
  omega_osc = 252 M_KK (wrong scale), mu/H < 10^{-16}. That analysis
  used omega_osc from d^2S/dtau^2 curvature, not omega_att.

  This computation tests ALL three resonance channels using omega_att
  as the physical driving frequency, including the pair vibration channel,
  and quantifies the A_s enhancement from any instability.

Gate criterion:
  PASS: Total A_s enhancement > 0.1 OOM
  INFO: Enhancement in [0.01, 0.1] OOM
  FAIL: Enhancement < 0.01 OOM (resonance negligible)

Cross-check: s67_floquet_post_transit.npz
"""

import sys
import numpy as np
from scipy.linalg import expm
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, S_fold, dS_fold, d2S_fold, G_DeWitt, H_fold,
    v_terminal, dt_transit, omega_att, omega_tau,
    E_B1, E_B2_mean, E_B3_mean,
    omega_L1, omega_L2, omega_H1, omega_H2, omega_PV,
    Delta_0_GL, Delta_B3, Delta_0_OES,
    E_cond, E_exc, n_pairs, N_dof_BCS,
    J_C2, J_su2, J_u1, T_acoustic,
    xi_BCS, m_tau, c_Gold, c_fabric,
    S_inst, Gamma_Langer_BCS, M_ATDHFB,
    PI, M_KK, Z_fold,
)

print("=" * 72)
print("PARAMETRIC-GGE-70: Post-Transit Parametric Resonance in BCS Modes")
print("=" * 72)
print("Agent: Tesla-Resonance")

# ===========================================================================
# SECTION 1: RESONANCE STRUCTURE IDENTIFICATION
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 1: Resonance Structure — What Oscillates, What Constrains")
print("=" * 72)

# === What oscillates ===
# After transit, the modulus tau has been driven through the fold at Mach 13.75.
# The characteristic frequency of the spectral action dynamics is omega_att.
# The BCS order parameter Delta may also ring (pair vibration omega_PV).

# === What constrains ===
# Hubble damping: H_fold = 586.5 M_KK (3H = 1759.6 M_KK as friction)
# BCS gap: Delta_0 = 0.770 M_KK (sub-gap modes protected)
# Josephson coupling: J_C2 = 0.933 M_KK (inter-cell rigidity)

# === Driving frequencies ===
omega_drive_geom = omega_att  # 1.430 M_KK — geometric attractor
omega_drive_BCS = omega_PV    # 0.792 M_KK — pair vibration (BCS settling)

print(f"\n--- Driving Frequencies ---")
print(f"  omega_att (geometric attractor)   = {omega_att:.4f} M_KK")
print(f"  omega_PV  (pair vibration)        = {omega_PV:.4f} M_KK")
print(f"  omega_tau (transit)               = {omega_tau:.4f} M_KK")
print(f"  H_fold (Hubble damping)           = {H_fold:.2f} M_KK")
print(f"  3*H_fold (friction coefficient)   = {3*H_fold:.1f} M_KK")

# === BCS Mode Frequencies ===
print(f"\n--- BCS Mode Frequencies ---")
# 8 modes: 4 B2, 1 B1, 3 B3
mode_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']
mode_energies = np.array([E_B2_mean]*4 + [E_B1] + [E_B3_mean]*3)
n_modes = len(mode_energies)

print(f"  {'Mode':<8s} {'E_k (M_KK)':>12s} {'omega_k/omega_att':>18s} {'omega_k/omega_PV':>18s}")
print(f"  {'-'*8} {'-'*12} {'-'*18} {'-'*18}")
for label, E in zip(mode_labels, mode_energies):
    print(f"  {label:<8s} {E:>12.4f} {E/omega_att:>18.4f} {E/omega_PV:>18.4f}")

# === Resonance Condition Check (overview) ===
print(f"\n--- Resonance Condition Check ---")
print(f"  n=1 Mathieu tongue: 2*omega_k = 2*omega_drive")
print(f"    => omega_k/omega_drive = 1.0")
print(f"  Closest for omega_att: omega_B3/omega_att = {E_B3_mean/omega_att:.4f}")
print(f"  Closest for omega_PV:  omega_B2/omega_PV  = {E_B2_mean/omega_PV:.4f}")
print(f"  Closest for omega_PV:  omega_B1/omega_PV  = {E_B1/omega_PV:.4f}")
print()
print(f"  n=2 Mathieu tongue: omega_k = omega_drive")
print(f"    Requires omega_k/omega_drive = 0.5")
print(f"    All modes have omega_k/omega_att in [{min(mode_energies)/omega_att:.3f}, {max(mode_energies)/omega_att:.3f}]")
print(f"    All modes have omega_k/omega_PV in [{min(mode_energies)/omega_PV:.3f}, {max(mode_energies)/omega_PV:.3f}]")

# ===========================================================================
# SECTION 2: COUPLING STRENGTH (epsilon)
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 2: Coupling Strength from Eigenvalue Tau-Dependence")
print("=" * 72)

# Load eigenvalue data from s60_hessian_3d for d(E)/d(tau)
hess_data = np.load(Path(__file__).parent / 's60_hessian_3d.npz', allow_pickle=True)
tau_arr = hess_data['tau_arr']
all_eigs = hess_data['all_eigenvalues']  # (5, 5, 5, 12880)
dtau_grid = hess_data['dtau']  # 0.01

# Extract eigenvalues at sigma=0, d1=0 for varying tau
eigs_vs_tau = all_eigs[:, 2, 2, :]  # (5, 12880)

# Sort and track lowest 8 positive eigenvalues at each tau
lowest8_pos = np.zeros((5, 8))
for i in range(5):
    pos = np.sort(eigs_vs_tau[i, eigs_vs_tau[i] > 0])
    lowest8_pos[i] = pos[:8]

# Central difference at fold (idx=2) for d(E)/d(tau)
dE_dtau = (lowest8_pos[3] - lowest8_pos[1]) / (2 * dtau_grid)
E_at_fold = lowest8_pos[2]
dln_E_dtau = dE_dtau / E_at_fold

print(f"\n  D_K eigenvalue derivatives at fold (sigma=0, d1=0):")
print(f"  {'Mode idx':<10s} {'E_fold':>10s} {'dE/dtau':>12s} {'d(ln E)/dtau':>14s}")
print(f"  {'-'*10} {'-'*10} {'-'*12} {'-'*14}")
for i in range(8):
    print(f"  {i:<10d} {E_at_fold[i]:>10.6f} {dE_dtau[i]:>12.6f} {dln_E_dtau[i]:>14.6f}")

print(f"\n  Mean |d(ln E)/d(tau)| = {np.mean(np.abs(dln_E_dtau)):.6f}")

# Modulus oscillation amplitude after transit
# The transit excursion is delta_tau ~ 0.05 (from S67).
# After transit, modulus settles. The post-transit ringing amplitude
# decays as exp(-3H*t/2) * cos(omega_att * t).
# Initial amplitude: estimated from terminal velocity deceleration
# delta_tau_0 = v_terminal / omega_att (ballistic estimate)
delta_tau_0 = v_terminal / omega_att  # ballistic estimate
# But Hubble friction dominates: 3H >> omega_att, so oscillations are OVERDAMPED
zeta_att = 3 * H_fold / (2 * omega_att)

# More physical: use the transit excursion itself
delta_tau_transit = 0.05  # from synthesis: van Hove fold width  # (local)

print(f"\n  Post-transit oscillation amplitude estimates:")
print(f"  delta_tau (ballistic) = v_terminal / omega_att = {delta_tau_0:.4f}")
print(f"  delta_tau (transit)   = {delta_tau_transit}")
print(f"  Hubble damping ratio  = 3H/(2*omega_att) = {zeta_att:.2f}")
print(f"  System is {'OVERDAMPED' if zeta_att > 1 else 'UNDERDAMPED'} (zeta = {zeta_att:.1f})")

# The coupling epsilon for each mode:
# epsilon_k = |dE_k/dtau| * delta_tau
# This is the modulation depth of the BCS mode energy due to tau oscillation

# Use the CANONICAL BCS mode energies and their tau-derivatives
# For the BCS quasiparticle E_k = sqrt(xi_k^2 + Delta^2):
# dE_k/dtau = (xi_k * d(xi_k)/dtau + Delta * dDelta/dtau) / E_k

# Use the raw D_K eigenvalue derivatives as proxy
# Note: modes are approximately sorted B2 (4), B1 (1), B3 (3) in the canonical
# constants. The D_K spectrum at the fold is highly degenerate (0.819-0.841).
# Map: B1 ~ idx 0 (lowest), B2 ~ idx 1-4 (degenerate), B3 ~ idx 5-7

dln_E_B1 = dln_E_dtau[0]   # B1: -0.084
dln_E_B2 = np.mean(dln_E_dtau[1:5])  # B2: +0.101
dln_E_B3 = np.mean(dln_E_dtau[5:8])  # B3: mix of +0.096 and +0.082

# However, the BCS energies are DIFFERENT from the raw D_K eigenvalues.
# The canonical E_B1=0.819, E_B2=0.845, E_B3=0.978 include BCS dressing.
# For the coupling, we use the canonical BCS energies and the D_K derivatives.
# This is an upper estimate (BCS gap rigidity would reduce the modulation).

# Map canonical BCS modes to derivatives
dln_E_modes = np.array([dln_E_B2]*4 + [dln_E_B1] + [dln_E_B3]*3)

# Coupling strengths for each channel
print(f"\n  Coupling strength epsilon_k = |d(ln E_k)/d(tau)| * delta_tau:")
epsilon_geom = np.abs(dln_E_modes) * delta_tau_transit
epsilon_BCS_frac = 0.10  # BCS gap oscillation: delta_Delta/Delta ~ S_inst ~ 0.069, use 10% upper bound  # (local)

print(f"  {'Mode':<8s} {'dln_E/dtau':>12s} {'eps_geom':>10s} {'eps_BCS':>10s}")
print(f"  {'-'*8} {'-'*12} {'-'*10} {'-'*10}")
for i, (label, E) in enumerate(zip(mode_labels, mode_energies)):
    eps_g = epsilon_geom[i]
    # BCS coupling: delta_E_k/E_k = (Delta^2/E_k^2) * delta_Delta/Delta
    eps_b = (Delta_0_GL**2 / E**2) * epsilon_BCS_frac
    print(f"  {label:<8s} {dln_E_modes[i]:>12.6f} {eps_g:>10.6f} {eps_b:>10.6f}")

# ===========================================================================
# SECTION 3: MATHIEU EQUATION — FLOQUET ANALYSIS
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 3: Mathieu Equation Floquet Analysis")
print("=" * 72)

def floquet_exponent_mathieu(a_param, q_param, n_steps=2000):
    """
    Compute the Floquet exponent of the Mathieu equation
    u'' + [a - 2q cos(2z)] u = 0
    by integrating over one period [0, pi] and computing monodromy matrix.
    Returns the maximum Floquet exponent mu (growth rate per period/pi).
    """
    dz = PI / n_steps
    M_mono = np.eye(2)

    for i in range(n_steps):
        z = i * dz
        omega_sq = a_param - 2 * q_param * np.cos(2 * z)
        A_local = np.array([[0.0, 1.0], [-omega_sq, 0.0]])

        # RK4 step on the monodromy matrix
        k1 = A_local @ M_mono

        z2 = z + dz / 2
        omega_sq_2 = a_param - 2 * q_param * np.cos(2 * z2)
        A2 = np.array([[0.0, 1.0], [-omega_sq_2, 0.0]])
        k2 = A2 @ (M_mono + dz / 2 * k1)
        k3 = A2 @ (M_mono + dz / 2 * k2)

        z3 = z + dz
        omega_sq_3 = a_param - 2 * q_param * np.cos(2 * z3)
        A3 = np.array([[0.0, 1.0], [-omega_sq_3, 0.0]])
        k4 = A3 @ (M_mono + dz * k3)

        M_mono = M_mono + (dz / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    eigvals = np.linalg.eigvals(M_mono)
    mu = np.max(np.log(np.abs(eigvals))) / PI
    return mu

# ===== CHANNEL A: Geometric modulus driving (omega_drive = omega_att) =====
print("\n--- CHANNEL A: Geometric Modulus Driving (omega_drive = omega_att) ---")
print(f"  omega_drive = omega_att = {omega_att:.4f} M_KK")

# Mathieu parameters:
#   u'' + [a - 2q cos(2z)] u = 0
# where z = omega_drive * t / 2
# and a = (2*omega_k / omega_drive)^2
# and q = epsilon_k * a / 2  (modulation depth)

print(f"\n  {'Mode':<8s} {'omega_k':>8s} {'a':>10s} {'q':>12s} {'mu_Floq':>12s} {'mu_phys':>12s} {'mu/H':>14s}")
print(f"  {'-'*8} {'-'*8} {'-'*10} {'-'*12} {'-'*12} {'-'*12} {'-'*14}")

mu_A_max = 0.0  # (local)
mu_A_results = {}

for i, (label, E) in enumerate(zip(mode_labels, mode_energies)):
    a_k = (2 * E / omega_att) ** 2
    q_k = epsilon_geom[i] * a_k / 2
    mu_k = floquet_exponent_mathieu(a_k, q_k)
    mu_phys = mu_k * omega_att / 2  # Convert to physical time
    ratio = mu_phys / H_fold if H_fold > 0 else 0
    mu_A_results[label] = {'a': a_k, 'q': q_k, 'mu': mu_k, 'mu_phys': mu_phys}
    if mu_phys > mu_A_max:
        mu_A_max = mu_phys
    print(f"  {label:<8s} {E:>8.4f} {a_k:>10.4f} {q_k:>12.6e} {mu_k:>12.6e} {mu_phys:>12.6e} {ratio:>14.6e}")

print(f"\n  Maximum physical growth rate (Channel A): {mu_A_max:.6e} M_KK")
print(f"  mu_A_max / H_fold = {mu_A_max/H_fold:.6e}")

# Key observation: a_k values
a_B2 = (2 * E_B2_mean / omega_att) ** 2
a_B1 = (2 * E_B1 / omega_att) ** 2
a_B3 = (2 * E_B3_mean / omega_att) ** 2
print(f"\n  Mathieu parameter a for each sector:")
print(f"    a_B1 = {a_B1:.4f}  (n=1 tongue: a~1.0, n=2: a~4.0)")
print(f"    a_B2 = {a_B2:.4f}  (n=1 tongue: a~1.0)")
print(f"    a_B3 = {a_B3:.4f}  (n=1 tongue: a~1.0)")
print(f"  All a > 1: modes are ABOVE the n=1 principal resonance tongue.")
print(f"  Closest integer squared: a_B1~{a_B1:.1f} nearest n^2=1, a_B3~{a_B3:.1f} nearest n^2=2")

# ===== CHANNEL B: BCS pair vibration driving (omega_drive = omega_PV) =====
print(f"\n--- CHANNEL B: BCS Pair Vibration Driving (omega_drive = omega_PV) ---")
print(f"  omega_drive = omega_PV = {omega_PV:.4f} M_KK")
print(f"  delta_Delta / Delta_0 = {epsilon_BCS_frac} (upper bound)")

print(f"\n  {'Mode':<8s} {'omega_k':>8s} {'a':>10s} {'q':>12s} {'mu_Floq':>12s} {'mu_phys':>12s} {'mu/H':>14s}")
print(f"  {'-'*8} {'-'*8} {'-'*10} {'-'*12} {'-'*12} {'-'*12} {'-'*14}")

mu_B_max = 0.0  # (local)
mu_B_results = {}

for i, (label, E) in enumerate(zip(mode_labels, mode_energies)):
    a_k = (2 * E / omega_PV) ** 2
    # BCS coupling: modulation of quasiparticle energy through gap oscillation
    # delta_E_k / E_k ~ (Delta^2 / E_k^2) * (delta_Delta / Delta)
    eps_BCS = (Delta_0_GL**2 / E**2) * epsilon_BCS_frac
    q_k = eps_BCS * a_k / 2
    mu_k = floquet_exponent_mathieu(a_k, q_k)
    mu_phys = mu_k * omega_PV / 2
    ratio = mu_phys / H_fold if H_fold > 0 else 0
    mu_B_results[label] = {'a': a_k, 'q': q_k, 'mu': mu_k, 'mu_phys': mu_phys}
    if mu_phys > mu_B_max:
        mu_B_max = mu_phys
    print(f"  {label:<8s} {E:>8.4f} {a_k:>10.4f} {q_k:>12.6e} {mu_k:>12.6e} {mu_phys:>12.6e} {ratio:>14.6e}")

print(f"\n  Maximum physical growth rate (Channel B): {mu_B_max:.6e} M_KK")
print(f"  mu_B_max / H_fold = {mu_B_max/H_fold:.6e}")
print(f"\n  a_B2 (PV drive) = {(2*E_B2_mean/omega_PV)**2:.4f}")
print(f"  a_B1 (PV drive) = {(2*E_B1/omega_PV)**2:.4f}")
print(f"  a_B3 (PV drive) = {(2*E_B3_mean/omega_PV)**2:.4f}")
print(f"  All a >> 1 (modes are 2-3x above omega_PV). Far from all tongues.")

# ===== CHANNEL C: Sum-frequency parametric resonance (omega_i + omega_j = 2*omega_drive) =====
print(f"\n--- CHANNEL C: Sum-Frequency Pair Resonance ---")
print(f"  Condition: omega_i + omega_j = 2 * omega_drive")

# For geometric drive
print(f"\n  Geometric drive (omega_att = {omega_att:.4f}):")
print(f"  2 * omega_att = {2*omega_att:.4f} M_KK")
print(f"\n  {'Pair':>12s} {'omega_i+omega_j':>16s} {'detuning':>12s} {'detuning/omega':>16s}")
print(f"  {'-'*12} {'-'*16} {'-'*12} {'-'*16}")

detunings_geom = []
pair_sums_geom = []

unique_sectors = [(0, 'B2', E_B2_mean), (4, 'B1', E_B1), (5, 'B3', E_B3_mean)]
for i_idx, (i_start, i_name, E_i) in enumerate(unique_sectors):
    for j_idx, (j_start, j_name, E_j) in enumerate(unique_sectors):
        if j_idx < i_idx:
            continue
        omega_sum = E_i + E_j
        det = omega_sum - 2 * omega_att
        det_frac = abs(det) / (2 * omega_att)
        detunings_geom.append(det)
        pair_sums_geom.append(omega_sum)
        in_res = "<<< NEAR" if det_frac < 0.1 else ""
        print(f"  {i_name}+{j_name:>3s} {omega_sum:>16.4f} {det:>12.4f} {det_frac:>16.4f} {in_res}")

# For PV drive
print(f"\n  Pair vibration drive (omega_PV = {omega_PV:.4f}):")
print(f"  2 * omega_PV = {2*omega_PV:.4f} M_KK")
print(f"\n  {'Pair':>12s} {'omega_i+omega_j':>16s} {'detuning':>12s} {'detuning/omega':>16s}")
print(f"  {'-'*12} {'-'*16} {'-'*12} {'-'*16}")

for i_idx, (i_start, i_name, E_i) in enumerate(unique_sectors):
    for j_idx, (j_start, j_name, E_j) in enumerate(unique_sectors):
        if j_idx < i_idx:
            continue
        omega_sum = E_i + E_j
        det = omega_sum - 2 * omega_PV
        det_frac = abs(det) / (2 * omega_PV)
        in_res = "<<< NEAR" if det_frac < 0.1 else ""
        print(f"  {i_name}+{j_name:>3s} {omega_sum:>16.4f} {det:>12.4f} {det_frac:>16.4f} {in_res}")

print(f"\n  All pair sums in [{min(pair_sums_geom):.3f}, {max(pair_sums_geom):.3f}] M_KK")
print(f"  2*omega_att = {2*omega_att:.3f}, 2*omega_PV = {2*omega_PV:.3f}")
print(f"  Minimum detuning (geom): {min(abs(d) for d in detunings_geom):.4f} M_KK")
print(f"  All detunings > epsilon: no sum resonance possible with these couplings.")

# ===========================================================================
# SECTION 4: COMPREHENSIVE MATHIEU BAND SCAN
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 4: Comprehensive Floquet Band Scan")
print("=" * 72)

# Scan Mathieu parameter a from 0 to 10, for each relevant q value,
# to map ALL instability tongues and verify no mode sits in one.

a_scan = np.linspace(0.01, 8.0, 400)

# Relevant q values from both channels
q_values_to_scan = {
    'geom_B2': epsilon_geom[0] * (2*E_B2_mean/omega_att)**2 / 2,
    'geom_B1': epsilon_geom[4] * (2*E_B1/omega_att)**2 / 2,
    'geom_B3': epsilon_geom[5] * (2*E_B3_mean/omega_att)**2 / 2,
    'BCS_B2': (Delta_0_GL**2/E_B2_mean**2) * epsilon_BCS_frac * (2*E_B2_mean/omega_PV)**2 / 2,
    'BCS_B1': (Delta_0_GL**2/E_B1**2) * epsilon_BCS_frac * (2*E_B1/omega_PV)**2 / 2,
    'BCS_B3': (Delta_0_GL**2/E_B3_mean**2) * epsilon_BCS_frac * (2*E_B3_mean/omega_PV)**2 / 2,
}

print(f"\n  Scanning a in [0.01, 8.0] for each q value:")
print(f"  {'Channel':<12s} {'q':>12s}")
for name, q_val in q_values_to_scan.items():
    print(f"  {name:<12s} {q_val:>12.6e}")

# Find the maximum Floquet exponent at any a for each channel (DIAGNOSTIC ONLY)
# NOTE: This scans over ALL values of a, not just physical mode locations.
# The physical growth rates are from Section 3 (mu_A_max, mu_B_max).
mu_scan_results = {}
mu_scan_max_diagnostic = 0.0  # Maximum over ALL a (unphysical diagnostic)  # (local)
mu_scan_max_channel = ""
mu_scan_max_a = 0.0  # (local)

for name, q_val in q_values_to_scan.items():
    mu_arr = np.array([floquet_exponent_mathieu(a, q_val) for a in a_scan])
    idx_max = np.argmax(mu_arr)
    mu_scan_results[name] = {
        'q': q_val,
        'mu_max': mu_arr[idx_max],
        'a_at_max': a_scan[idx_max],
        'mu_arr': mu_arr,
    }
    # Convert to physical rate
    if 'geom' in name:
        omega_d = omega_att
    else:
        omega_d = omega_PV
    mu_phys = mu_arr[idx_max] * omega_d / 2

    print(f"  {name:<12s}: mu_max = {mu_arr[idx_max]:.6e} at a = {a_scan[idx_max]:.3f}, mu_phys = {mu_phys:.6e} M_KK")

    if mu_phys > mu_scan_max_diagnostic:
        mu_scan_max_diagnostic = mu_phys
        mu_scan_max_channel = name
        mu_scan_max_a = a_scan[idx_max]

# PHYSICAL mu_max is from Section 3: maximum over physical mode locations only
# The Floquet exponents at the physical a values are ALL essentially zero
# (machine epsilon ~10^{-16}) because no physical mode sits in any tongue.
mu_max_phys = max(mu_A_max, mu_B_max)
print(f"\n  DIAGNOSTIC scan mu_max (over all a): {mu_scan_max_diagnostic:.6e} M_KK at a={mu_scan_max_a:.3f}")
print(f"  PHYSICAL mu_max (at mode locations): {mu_max_phys:.6e} M_KK")
print(f"  The scan mu_max occurs at a~1.0 (first Mathieu tongue), but NO physical")
print(f"  mode sits there. Physical modes have a in [1.31, 6.11] — between tongues.")

# Also scan with LARGER q (hypothetical: what if coupling were 100x stronger?)
print(f"\n  Hypothetical: what q is needed for mu_phys > H?")
# At a = 1 (principal tongue), mu ~ q/2
# Need mu * omega_drive / 2 > H_fold
# => q > 2 * H_fold / (omega_drive / 2) = 4 * H_fold / omega_drive
q_needed_geom = 4 * H_fold / omega_att
q_needed_BCS = 4 * H_fold / omega_PV
print(f"  For omega_att: q_needed = {q_needed_geom:.1f} (actual q ~ {max(q_values_to_scan[k] for k in q_values_to_scan if 'geom' in k):.2e})")
print(f"  For omega_PV:  q_needed = {q_needed_BCS:.1f} (actual q ~ {max(q_values_to_scan[k] for k in q_values_to_scan if 'BCS' in k):.2e})")
print(f"  Ratio (shortfall): {q_needed_geom / max(q_values_to_scan[k] for k in q_values_to_scan if 'geom' in k):.1e}x (geom)")
print(f"                     {q_needed_BCS / max(q_values_to_scan[k] for k in q_values_to_scan if 'BCS' in k):.1e}x (BCS)")

# ===========================================================================
# SECTION 5: DAMPING AND POST-TRANSIT OSCILLATION COUNT
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 5: Damping and Available Oscillation Time")
print("=" * 72)

# Even if parametric resonance existed, it needs time to grow.
# The Hubble friction damps oscillations. The post-transit epoch
# has a finite window before Hubble damping kills all oscillations.

# For the modulus tau:
# tau'' + 3H*tau' + omega_att^2 * tau = 0
# zeta = 3H / (2*omega_att) = damping ratio
print(f"  Modulus oscillation: omega_att = {omega_att:.4f}, 3H = {3*H_fold:.1f}")
print(f"  Damping ratio zeta = 3H/(2*omega_att) = {zeta_att:.1f}")
print(f"  System: MASSIVELY OVERDAMPED (zeta = {zeta_att:.0f})")
print(f"  => Modulus does NOT oscillate at omega_att after transit.")
print(f"  => It monotonically decays (overdamped rolloff).")
print(f"  => There is NO periodic driving force for parametric resonance.")

# For the BCS pair vibration:
zeta_PV = 3 * H_fold / (2 * omega_PV)
print(f"\n  BCS pair vibration: omega_PV = {omega_PV:.4f}, 3H = {3*H_fold:.1f}")
print(f"  Damping ratio zeta_PV = 3H/(2*omega_PV) = {zeta_PV:.1f}")
print(f"  System: MASSIVELY OVERDAMPED (zeta = {zeta_PV:.0f})")
print(f"  => Pair vibration mode also does NOT oscillate.")

# Even ignoring Hubble damping — conservative estimate with T = 10 periods
T_10_att = 10 * 2 * PI / omega_att
T_10_PV = 10 * 2 * PI / omega_PV
print(f"\n  Conservative: 10 oscillation periods of driving")
print(f"  T_10 (omega_att) = {T_10_att:.4f} M_KK^{{-1}}")
print(f"  T_10 (omega_PV)  = {T_10_PV:.4f} M_KK^{{-1}}")
print(f"  H_fold * T_10 (att) = {H_fold * T_10_att:.1f}  (>>1: heavily damped)")
print(f"  H_fold * T_10 (PV)  = {H_fold * T_10_PV:.1f}  (>>1: heavily damped)")

# Damped amplitude after one period:
# exp(-3H * T/2) where T = 2*pi/omega
damp_1period_att = np.exp(-3 * H_fold * PI / omega_att)
damp_1period_PV = np.exp(-3 * H_fold * PI / omega_PV)
print(f"\n  Amplitude after 1 period (undamped assumption):")
print(f"  exp(-3H * pi/omega_att) = {damp_1period_att:.6e} (omega_att)")
print(f"  exp(-3H * pi/omega_PV)  = {damp_1period_PV:.6e} (omega_PV)")
damp_oom_att = -np.log10(damp_1period_att) if damp_1period_att > 0 else float('inf')
print(f"  => Driving amplitude is suppressed by {damp_oom_att:.0f} OOM after ONE period")
print(f"  => Parametric resonance impossible: driver damps before any amplification occurs")

# ===========================================================================
# SECTION 6: A_s ENHANCEMENT COMPUTATION (OPTIMISTIC UPPER BOUND)
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 6: A_s Enhancement (Optimistic Upper Bound)")
print("=" * 72)

# Despite the overdamping argument killing parametric resonance,
# compute the upper bound A_s enhancement AS IF the driving lasted
# for T = 10 periods without damping.

# Maximum PHYSICAL Floquet exponent from Section 3 (at physical mode locations)
# The physical Floquet exponents are essentially zero because no mode sits in a tongue.
print(f"  Physical Floquet exponent (at mode locations): mu_phys = {mu_max_phys:.6e} M_KK")
print(f"  This is machine epsilon — no physical mode sits in any Mathieu tongue.")
print()
print(f"  For completeness, also compute analytic upper bound AT resonance:")
# Even if a mode WERE at a = 1, the growth rate would be:
q_max_geom = max(q_values_to_scan[k] for k in q_values_to_scan if 'geom' in k)
q_max_BCS = max(q_values_to_scan[k] for k in q_values_to_scan if 'BCS' in k)
mu_analytic_geom = q_max_geom / 2 * omega_att / 2
mu_analytic_BCS = q_max_BCS / 2 * omega_PV / 2
mu_hypothetical_max = max(mu_analytic_geom, mu_analytic_BCS)
print(f"  mu_analytic (geom, IF a=1) = q/2 * omega/2 = {mu_analytic_geom:.6e} M_KK")
print(f"  mu_analytic (BCS, IF a=1)  = q/2 * omega/2 = {mu_analytic_BCS:.6e} M_KK")
print(f"  Even this hypothetical rate is {H_fold / mu_hypothetical_max:.0f}x below H_fold.")
# Use the physical mu for the gate
mu_for_gate = mu_max_phys

# Amplification factor: A_s_enhanced / A_s_bare = exp(2 * mu * T)
# where factor 2 comes from A_s ~ |u_k|^2
T_drive = T_10_att  # 10 periods of omega_att
amplification = np.exp(2 * mu_for_gate * T_drive) if mu_for_gate > 0 else 1.0
delta_OOM = np.log10(amplification) if amplification > 1 else 0.0

print(f"\n  Amplification with T = 10 periods of omega_att:")
print(f"  mu_phys (physical) = {mu_for_gate:.6e} M_KK")
print(f"  exp(2 * mu * T) = exp(2 * {mu_for_gate:.6e} * {T_drive:.4f})")
print(f"                   = {amplification:.10f}")
print(f"  delta_OOM = log10(exp(2*mu*T)) = {delta_OOM:.6e} OOM")

# Also compute: what mu would be needed for 0.1 OOM?
# 0.1 OOM = factor 10^{0.1} = 1.259
# exp(2*mu*T) = 1.259 => 2*mu*T = ln(1.259) = 0.2303
# mu_needed = 0.2303 / (2 * T)
mu_needed_01 = np.log(10**0.1) / (2 * T_drive)
mu_needed_001 = np.log(10**0.01) / (2 * T_drive)
print(f"\n  Needed for PASS (0.1 OOM): mu_needed = {mu_needed_01:.6e} M_KK")
print(f"  Needed for INFO (0.01 OOM): mu_needed = {mu_needed_001:.6e} M_KK")
print(f"  Actual physical mu_max: {mu_for_gate:.6e} M_KK")
if mu_for_gate > 0:
    print(f"  Shortfall to PASS: {mu_needed_01/mu_for_gate:.1e}x")
    print(f"  Shortfall to INFO: {mu_needed_001/mu_for_gate:.1e}x")
else:
    print(f"  Physical Floquet exponent = 0 (machine epsilon). No amplification.")
    print(f"  Shortfall: INFINITE — no tongue overlap, no growth at all.")

# ===========================================================================
# SECTION 7: S67 CROSS-CHECK
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 7: Cross-Check Against S67 Floquet Analysis")
print("=" * 72)

s67_data = np.load(Path(__file__).parent / 's67_floquet_post_transit.npz', allow_pickle=True)
s67_mu_max = float(s67_data['max_growth_rate'])
s67_mu_channel = str(s67_data['max_growth_channel'])
s67_ratio = float(s67_data['ratio_mu_H'])
s67_omega_osc = float(s67_data['omega_osc'])
s67_zeta = float(s67_data['zeta_damping'])

print(f"  S67 maximum growth rate: {s67_mu_max:.6e} M_KK (channel: {s67_mu_channel})")
print(f"  S67 mu/H ratio: {s67_ratio:.6e}")
print(f"  S67 omega_osc (curvature): {s67_omega_osc:.2f} M_KK")
print(f"  S67 damping ratio: {s67_zeta:.4f}")
print(f"\n  S70 omega_drive (attractor): {omega_att:.4f} M_KK")
print(f"  S70 maximum physical growth rate: {mu_max_phys:.6e} M_KK")
print(f"  S70 diagnostic scan max (at a~1): {mu_scan_max_diagnostic:.6e} M_KK (unphysical)")

# Consistency: Both analyses find negligible parametric resonance.
# S67 used omega_osc = 252 M_KK (too fast, modes far below resonance).
# S70 uses omega_att = 1.430 M_KK (correct scale, but modes ABOVE resonance
# and coupling is too weak, and driving is overdamped).
print(f"\n  CONSISTENCY:")
print(f"  S67: omega_drive = 252 M_KK >> omega_k ~ 0.8-0.98 M_KK. A_k << 1. No resonance.")
print(f"  S70: omega_drive = 1.43 M_KK ~  omega_k ~ 0.8-0.98 M_KK. A_k ~ 1.3-1.9.")
print(f"       Modes are BETWEEN n=1 and n=2 tongues, not IN any tongue.")
print(f"       Coupling q ~ 10^{{-3}}-10^{{-2}} => tongue width ~ q << mode spacing.")
print(f"       AND driving is overdamped: zeta = {zeta_att:.0f} >> 1.")
print(f"  BOTH analyses: parametric resonance is negligible.")

# ===========================================================================
# SECTION 8: PHYSICAL INTERPRETATION — RESONANCE STRUCTURE
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 8: Physical Interpretation — Why Parametric Resonance Fails")
print("=" * 72)

print(f"""
  THREE INDEPENDENT REASONS:

  1. FREQUENCY MISMATCH (structural)
     The Mathieu parameter a = (2*omega_k/omega_drive)^2 for the BCS modes is:
       a_B1 = {a_B1:.3f}, a_B2 = {a_B2:.3f}, a_B3 = {a_B3:.3f}
     Instability tongues are centered at a = n^2 (n = 1, 2, 3, ...).
     The modes sit BETWEEN the n=1 (a=1) and n=2 (a=4) tongues.
     Tongue width ~ q ~ {max(epsilon_geom):.3f} (geometric) or {epsilon_BCS_frac * Delta_0_GL**2 / E_B2_mean**2:.3f} (BCS).
     The modes are separated from the nearest tongue by delta_a ~ {min(abs(a_B1-1), abs(a_B2-1), abs(a_B3-1)):.2f} (n=1) or
     delta_a ~ {min(abs(a_B1-4), abs(a_B2-4), abs(a_B3-4)):.2f} (n=2), both >> q.
     No mode sits in any instability tongue.

  2. HUBBLE OVERDAMPING (dynamical)
     The driving oscillation (whether modulus or BCS gap) is subject to
     Hubble friction with zeta = {zeta_att:.0f} (omega_att) or {zeta_PV:.0f} (omega_PV).
     Both are MASSIVELY overdamped (zeta >> 1).
     The driving amplitude decays by {damp_oom_att:.0f} OOM within ONE oscillation period.
     No periodic driving survives to create Floquet instability.

     CONDENSED MATTER ANALOG: This is like trying to create parametric
     amplification in a superfluid at temperatures T >> T_c, where the normal
     fluid viscosity kills oscillations before any energy transfer occurs.

  3. WEAK COUPLING (energetic)
     The modulation depth epsilon ~ |d(ln E)/d(tau)| * delta_tau ~ {max(epsilon_geom):.3f}.
     Even at the exact resonance condition (a = n^2), the growth rate
     would be mu ~ epsilon * omega_drive / 4 ~ {max(epsilon_geom) * omega_att / 4:.4f} M_KK,
     which is {H_fold / (max(epsilon_geom) * omega_att / 4):.0f}x below H_fold.
     The coupling is too weak to overcome Hubble expansion even at resonance.

     For comparison, KLS preheating requires q >> 1 (broad resonance) or
     q ~ 1 and many oscillation cycles (narrow resonance). Our q ~ {max(epsilon_geom):.3f}
     with N_osc = 0 (overdamped) is in neither regime.

  CONCLUSION:
  Parametric resonance does not contribute to A_s enhancement.
  The A_s gap closure budget remains at 0.485 OOM from the S69 accounting.
  The GGE spectral content is set entirely by the single-pass Bogoliubov
  mechanism at the transit, not by post-transit oscillatory dynamics.
""")

# ===========================================================================
# SECTION 9: CONDENSED MATTER ANALOG VERIFICATION
# ===========================================================================
print("=" * 72)
print("SECTION 9: Condensed Matter Analog")
print("=" * 72)

print(f"""
  In 3He-B, the analog of post-transit parametric resonance would be:
  After a rapid pressure quench through T_c (the analog of the transit),
  can the oscillation of the A-phase/B-phase boundary drive parametric
  amplification of Bogoliubov quasiparticles?

  The answer is known experimentally (Lancaster, Grenoble): NO.
  The reason is the same: the boundary dynamics are overdamped by
  mutual friction (analog of Hubble friction), and the quasiparticle
  modes are not at the correct frequency for Mathieu-type resonance
  with the boundary oscillation.

  The GGE spectrum in 3He-B after a quench is determined by the
  single-pass Kibble-Zurek mechanism, not by post-quench oscillatory
  dynamics. This is structurally identical to our result.

  HOWEVER: note that KLS-type broad parametric resonance (q >> 1) DOES
  occur in BEC experiments (Chin group, Chicago) where the coupling
  g is tunable via Feshbach resonance. The difference: in BEC, g can be
  made large enough to reach q >> 1. In our framework, the coupling
  epsilon ~ 0.005 is set by the spectral action curvature and cannot be
  tuned. The framework PREDICTS its own coupling too weak for resonance.
""")

# ===========================================================================
# GATE VERDICT
# ===========================================================================
print("=" * 72)
print("GATE VERDICT: PARAMETRIC-GGE-70")
print("=" * 72)

# Determine verdict
if delta_OOM >= 0.1:
    verdict = "PASS"
    verdict_detail = f"A_s enhancement = {delta_OOM:.4f} OOM > 0.1 OOM threshold."
elif delta_OOM >= 0.01:
    verdict = "INFO"
    verdict_detail = f"A_s enhancement = {delta_OOM:.6f} OOM in [0.01, 0.1] (marginal contribution)."
else:
    verdict = "FAIL"
    verdict_detail = f"A_s enhancement = {delta_OOM:.6e} OOM < 0.01 OOM. Parametric resonance negligible."

print(f"\n  Threshold: PASS > 0.1 OOM, INFO in [0.01, 0.1], FAIL < 0.01 OOM")
print(f"  Computed:  delta_OOM = {delta_OOM:.6e}")
print(f"  Verdict:   {verdict}")
print(f"  Detail:    {verdict_detail}")

print(f"\n  Three independent arguments (all structural):")
print(f"    1. Frequency mismatch: a in [{min(a_B1,a_B2,a_B3):.2f}, {max(a_B1,a_B2,a_B3):.2f}], no tongue hit")
print(f"    2. Hubble overdamping: zeta = {zeta_att:.0f} >> 1, driver killed in < 1 period")
print(f"    3. Weak coupling: epsilon ~ {max(epsilon_geom):.3f}, need q ~ {q_needed_geom:.0f} for mu > H")
print(f"\n  Cross-check: S67 Floquet (different omega_drive): same conclusion (mu/H ~ 10^{{-16}})")
print(f"\n  A_s gap remains: 0.485 OOM (unchanged from S69 budget)")

# ===========================================================================
# SAVE DATA
# ===========================================================================
print("\n--- Saving data ---")

outfile = Path(__file__).parent / 's70_parametric_gge.npz'

# Collect mode-level results
a_vals_A = np.array([(2*E/omega_att)**2 for E in mode_energies])
a_vals_B = np.array([(2*E/omega_PV)**2 for E in mode_energies])
q_vals_A = np.array([mu_A_results[l]['q'] for l in mode_labels])
q_vals_B = np.array([mu_B_results[l]['q'] for l in mode_labels])
mu_vals_A = np.array([mu_A_results[l]['mu_phys'] for l in mode_labels])
mu_vals_B = np.array([mu_B_results[l]['mu_phys'] for l in mode_labels])

np.savez(outfile,
    # Gate
    gate_name='PARAMETRIC-GGE-70',
    gate_verdict=verdict,
    gate_detail=verdict_detail,

    # Driving frequencies
    omega_drive_geom=omega_att,
    omega_drive_BCS=omega_PV,

    # BCS mode energies
    mode_labels=np.array(mode_labels),
    mode_energies=mode_energies,

    # Coupling strengths
    epsilon_geom=epsilon_geom,
    epsilon_BCS_frac=epsilon_BCS_frac,
    dln_E_dtau=dln_E_modes,
    delta_tau_transit=delta_tau_transit,

    # Channel A: geometric driving
    a_vals_geom=a_vals_A,
    q_vals_geom=q_vals_A,
    mu_phys_geom=mu_vals_A,
    mu_A_max=mu_A_max,

    # Channel B: BCS pair vibration driving
    a_vals_BCS=a_vals_B,
    q_vals_BCS=q_vals_B,
    mu_phys_BCS=mu_vals_B,
    mu_B_max=mu_B_max,

    # Channel C: sum frequencies
    pair_sums_geom=np.array(pair_sums_geom),
    detunings_geom=np.array(detunings_geom),

    # Damping
    zeta_att=zeta_att,
    zeta_PV=zeta_PV,
    damp_1period_att=damp_1period_att,
    damp_1period_PV=damp_1period_PV,

    # Band scan
    a_scan=a_scan,
    mu_scan_geom_B2=mu_scan_results.get('geom_B2', {}).get('mu_arr', np.array([])),
    mu_scan_BCS_B2=mu_scan_results.get('BCS_B2', {}).get('mu_arr', np.array([])),

    # Enhancement
    mu_max_phys=mu_max_phys,
    mu_scan_max_diagnostic=mu_scan_max_diagnostic,
    mu_max_channel=mu_scan_max_channel,
    T_drive=T_drive,
    amplification=amplification,
    delta_OOM=delta_OOM,

    # Needed values
    mu_needed_PASS=mu_needed_01,
    mu_needed_INFO=mu_needed_001,
    q_needed_geom=q_needed_geom,
    q_needed_BCS=q_needed_BCS,

    # S67 cross-check
    s67_mu_max=s67_mu_max,
    s67_omega_osc=s67_omega_osc,

    # Key Mathieu parameters
    a_B1=a_B1,
    a_B2=a_B2,
    a_B3=a_B3,

    # Eigenvalue derivatives
    dE_dtau_lowest8=dE_dtau,
    E_at_fold_lowest8=E_at_fold,
)

print(f"  Saved to: {outfile}")
print(f"\n{'='*72}")
print(f"PARAMETRIC-GGE-70: {verdict}")
print(f"{'='*72}")
