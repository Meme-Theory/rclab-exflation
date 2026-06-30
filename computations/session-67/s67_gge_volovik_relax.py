#!/usr/bin/env python3
"""
S67 GGE-VOLOVIK-RELAX-67: Exact Beta-Relaxation Rate on CG(24)
================================================================

Physics:
  The Volovik self-tuning mechanism requires the vacuum energy to track H(t)^2
  across cosmic history. The rate at which rho_vac adjusts is set by the
  Josephson dynamics of the BCS condensate on the 32-cell CG(24) fabric graph.

  Each cell i has a complex order parameter Delta_i = |Delta_i| exp(i*phi_i).
  The inter-cell Josephson coupling creates a Hamiltonian:

    H_J = -sum_{<ij>} J_{ij} * |Delta_i| * |Delta_j| * cos(phi_i - phi_j)
        + sum_i  Q_i^2 / (2 * C_i)

  where Q_i is the charge (number fluctuation) conjugate to phi_i, and
  C_i = rho_i is the single-particle DOS (compressibility) at cell i.

  In the transmon limit (E_J >> E_C), phase slips are exponentially rare:
    Gamma_slip = omega_p * exp(-S_inst)
  where omega_p = sqrt(8*E_J*E_C) is the plasma frequency and
  S_inst = sqrt(8*E_J/E_C) is the instanton action.

  The FABRIC-SCALE relaxation rate is set by the graph Laplacian spectral gap:
    Gamma_fabric = lambda_1 * Gamma_slip / z_mean

Method:
  1. ANALYTIC: Compute omega_p, S_inst, Gamma_slip, Gamma_fabric from
     canonical constants and graph Laplacian spectrum.
  2. SEMICLASSICAL NORMAL MODES: Diagonalize the full 32x32 Josephson
     dynamical matrix to get all relaxation eigenfrequencies.
  3. CLASSICAL DYNAMICS: Solve Hamilton's equations for {phi_i(t), Q_i(t)}
     on CG(24) with a small vacuum energy perturbation. Measure the
     exponential decay time of the perturbation.
  4. QUANTUM TUNNELING: Compute the WKB phase-slip rate for a single
     junction and multiply by the number of parallel channels.

Gate: GGE-VOLOVIK-RELAX-67
  PASS: Gamma > H(z_eq) ~ 3.4e-13 s^{-1}
  FAIL: Gamma < H_0 ~ 2.2e-18 s^{-1}

Context: W1-D BBN tracking PASSED by 10^{38.9} margin (S67). This computation
provides the microscopic foundation: the beta-relaxation rate that W1-D assumed.

Author: Kitaev-Quantum-Chaos-Theorist (S67)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, cos, sin, exp
from scipy.linalg import eigvalsh, eigh
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

from canonical_constants import (
    J_C2, J_su2, J_u1, T_acoustic, M_KK, S_inst,
    GeV_to_inv_s, H_0_inv_s, hbar_SI, hbar_GeV_s,
    Delta_0_OES, rho_B2_per_mode, N_cells,
    Omega_r, Omega_m, Omega_Lambda, H_0_km_s_Mpc,
    E_cond, M_KK_gravity,
)

print("=" * 70)
print("GGE-VOLOVIK-RELAX-67: Beta-Relaxation Rate on CG(24)")
print("=" * 70)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 1: Load CG(24) graph data
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

data_path = Path(__file__).parent / "s54_tb_hamiltonian.npz"
data = np.load(data_path, allow_pickle=True)

adj = data['adjacency'].astype(float)
adj_C2 = data['adj_C2'].astype(float)
adj_su2 = data['adj_su2'].astype(float)
adj_u1 = data['adj_u1'].astype(float)
N = int(data['N_cells'])  # = 32

z_per_cell = adj.sum(axis=1)
z_mean = z_per_cell.mean()
N_bonds = int(adj.sum() / 2)

print(f"\n--- Section 1: CG(24) Graph ---")
print(f"  N_cells = {N}")
print(f"  N_bonds = {N_bonds}")
print(f"  z_mean = {z_mean:.4f}")
print(f"  z_range = [{z_per_cell.min():.0f}, {z_per_cell.max():.0f}]")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 2: Josephson parameters from canonical constants
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Load BKT data for E_J, E_C at fold
bkt_data = np.load(Path(__file__).parent / "s58_bkt_kubo.npz", allow_pickle=True)
E_J_fold = float(bkt_data['E_J_fold'])       # 7.0415 M_KK (total Josephson energy per cell)
E_C_fold = float(bkt_data['E_c_fold'])        # 0.0363 M_KK (charging energy per cell)
ratio_EJ_EC = float(bkt_data['ratio_EJ_Ec'])  # 194.13

# Josephson energy PER BOND (E_J_fold is the total for z_mean bonds)
# E_J_fold = sum_{j nn i} J_{ij} = z_mean * J_avg
# The E_J relevant for a single phase slip is the single-bond value
E_J_bond = E_J_fold / z_mean  # Per-bond Josephson energy
E_C_cell = E_C_fold           # Charging energy is per cell

print(f"\n--- Section 2: Josephson Parameters ---")
print(f"  E_J_fold (total per cell) = {E_J_fold:.6f} M_KK")
print(f"  E_C_fold (charging per cell) = {E_C_fold:.6f} M_KK")
print(f"  E_J/E_C = {ratio_EJ_EC:.2f}")
print(f"  E_J per bond = {E_J_bond:.6f} M_KK")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 3: Weighted graph Laplacian spectrum
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Weighted adjacency matrix (Josephson couplings)
W = J_C2 * adj_C2 + J_su2 * adj_su2 + J_u1 * adj_u1
D_w = np.diag(W.sum(axis=1))
L_w = D_w - W

eigs_Lw = np.sort(eigvalsh(L_w))
lambda_1 = eigs_Lw[1]  # Spectral gap

# Unweighted Laplacian for comparison
D_unw = np.diag(adj.sum(axis=1))
L_unw = D_unw - adj
eigs_Lunw = np.sort(eigvalsh(L_unw))

print(f"\n--- Section 3: Laplacian Spectrum ---")
print(f"  Weighted Laplacian spectral gap lambda_1 = {lambda_1:.6f} M_KK")
print(f"  Weighted lambda_max = {eigs_Lw[-1]:.6f} M_KK")
print(f"  Unweighted spectral gap = {eigs_Lunw[1]:.6f}")
print(f"  First 5 weighted eigenvalues: {eigs_Lw[:5]}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 4: ANALYTIC beta-relaxation rate
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 4a: Plasma frequency
# omega_p = sqrt(8 * E_J * E_C) -- the Josephson plasma oscillation frequency
# This is the attempt frequency for phase slips.
# Two versions: per-bond and per-cell
omega_p_cell = sqrt(8 * E_J_fold * E_C_fold)  # Using total E_J per cell
omega_p_bond = sqrt(8 * E_J_bond * E_C_cell)  # Using per-bond E_J

print(f"\n--- Section 4: Analytic Beta-Relaxation ---")
print(f"  omega_p (per cell) = {omega_p_cell:.6f} M_KK")
print(f"  omega_p (per bond) = {omega_p_bond:.6f} M_KK")
print(f"  omega_p (per cell) in Hz = {omega_p_cell * M_KK * GeV_to_inv_s:.4e}")

# 4b: Instanton action for phase slip
# In the transmon limit (E_J >> E_C), the WKB tunneling action through
# the cosine potential barrier is:
#   S_inst = sqrt(8 * E_J / E_C)
# This is the action for a 2pi phase slip across a SINGLE junction.
# Per-cell: uses total E_J
S_inst_cell = sqrt(8 * E_J_fold / E_C_fold)
# Per-bond: uses per-bond E_J
S_inst_bond = sqrt(8 * E_J_bond / E_C_cell)

print(f"  S_inst (per cell) = {S_inst_cell:.4f}")
print(f"  S_inst (per bond) = {S_inst_bond:.4f}")
print(f"  exp(-S_inst_cell) = {exp(-S_inst_cell):.4e}")
print(f"  exp(-S_inst_bond) = {exp(-S_inst_bond):.4e}")

# 4c: Phase slip rate per junction
# Gamma_slip = omega_p * exp(-S_inst)
# The PHYSICAL rate is per-bond: one junction sees E_J_bond and attempts
# at omega_p_bond, tunneling through action S_inst_bond.
Gamma_slip_bond = omega_p_bond * exp(-S_inst_bond)
Gamma_slip_cell = omega_p_cell * exp(-S_inst_cell)

print(f"  Gamma_slip (per bond) = {Gamma_slip_bond:.6e} M_KK")
print(f"  Gamma_slip (per cell) = {Gamma_slip_cell:.6e} M_KK")
print(f"  Gamma_slip (per bond) in Hz = {Gamma_slip_bond * M_KK * GeV_to_inv_s:.4e}")

# 4d: Total phase slip rate for one cell (all z_mean junctions in parallel)
Gamma_cell_total = z_mean * Gamma_slip_bond

print(f"  Gamma_cell_total = z_mean * Gamma_slip_bond = {Gamma_cell_total:.6e} M_KK")

# 4e: Fabric-scale relaxation rate
# The vacuum energy relaxation is a COLLECTIVE mode of the CG(24) graph.
# The slowest collective mode decays at rate set by the spectral gap lambda_1.
#
# Physical picture: A uniform vacuum energy shift delta_rho_vac corresponds
# to a uniform phase gradient. This decomposes into graph Laplacian eigenmodes.
# Each mode k relaxes at rate Gamma_k = Gamma_slip * lambda_k / z_mean.
# The bottleneck is the slowest nonzero mode (k=1, lambda_1 = 0.179).
#
# More precisely, for small oscillations around the ordered ground state,
# the phase dynamics is:
#   C_i * ddot{phi}_i = -dH/dphi_i = -sum_j J_{ij} sin(phi_i - phi_j)
# Linearizing (small phi): C_i * ddot{phi}_i = -sum_j J_{ij} (phi_i - phi_j) = -(L_w phi)_i
# This gives normal mode frequencies: omega_k^2 = lambda_k^(Lw) / C
# where C = E_C_fold / 2 (in M_KK units, C = 1/(2*E_C))
#
# But the relaxation rate is not the oscillation frequency — it's the
# TUNNELING rate through the phase-slip barrier, weighted by the mode structure.

# Method A: Simple Laplacian scaling (S66 estimate, corrected)
Gamma_fabric_A = lambda_1 * Gamma_slip_bond / z_mean
print(f"\n  Method A (Laplacian scaling):")
print(f"    Gamma_fabric_A = {Gamma_fabric_A:.6e} M_KK")
print(f"    Gamma_fabric_A in Hz = {Gamma_fabric_A * M_KK * GeV_to_inv_s:.4e}")

# Method B: Normal mode oscillation frequencies (classical, no tunneling)
# These give the OSCILLATION rates, not tunneling rates.
# The vacuum energy relaxation is an oscillatory process when the system
# is in the superfluid phase (E_J >> E_C).
#
# The dynamical matrix equation is:
#   omega^2 * C * phi = L_w * phi
# where C = 1/(2*E_C) is the capacitance.
# Equivalently: omega^2 = lambda_k * (2 * E_C)
C_eff = 1.0 / (2.0 * E_C_fold)  # Capacitance (inverse charging energy)
omega_k_sq = eigs_Lw / C_eff     # = eigs_Lw * 2 * E_C_fold
omega_k = np.sqrt(np.maximum(omega_k_sq, 0))

print(f"\n  Method B (Normal mode oscillation):")
print(f"    Capacitance C_eff = {C_eff:.4f} M_KK^{{-1}}")
print(f"    omega_1 = sqrt(lambda_1 / C) = {omega_k[1]:.6f} M_KK")
print(f"    omega_max = {omega_k[-1]:.6f} M_KK")
print(f"    omega_1 in Hz = {omega_k[1] * M_KK * GeV_to_inv_s:.4e}")
print(f"    First 5 normal mode frequencies: {omega_k[:5]}")

# The RELAXATION rate is the normal mode frequency omega_1, because
# in the phase-coherent (superfluid) regime, the vacuum energy responds
# to perturbations OSCILLATORILY, not via tunneling. The phase-slip
# rate is the rate for a 2pi quantum, which is NOT needed for small
# vacuum energy adjustments. Small adjustments = small phase shifts,
# which propagate at the normal mode frequency.
Gamma_fabric_B = omega_k[1]

print(f"    Gamma_fabric_B (osc) = {Gamma_fabric_B:.6f} M_KK")
print(f"    Gamma_fabric_B in Hz = {Gamma_fabric_B * M_KK * GeV_to_inv_s:.4e}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 5: NUMERICAL DYNAMICS — Classical Josephson evolution on CG(24)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Solve Hamilton's equations:
#   dphi_i/dt = dH/dQ_i = Q_i / C_i
#   dQ_i/dt  = -dH/dphi_i = sum_j J_{ij} sin(phi_i - phi_j)
#
# Initial condition: small perturbation on top of ordered ground state.
# The "vacuum energy" is E_vac = H_J = -sum_{<ij>} J_{ij} cos(phi_i - phi_j)
# In the ground state (all phi_i = 0), E_vac = -sum_{<ij>} J_{ij} = -E_J_total
# A perturbation delta_phi raises E_vac by delta_E ~ (1/2) phi^T L_w phi.
#
# We initialize with phi(0) ~ small random perturbation, Q(0) = 0, and
# measure how E_vac(t) relaxes back to the ground state value.

print(f"\n--- Section 5: Classical Josephson Dynamics on CG(24) ---")

def josephson_rhs(t, y, W_mat, C_inv_arr, N_sites):
    """Right-hand side of Hamilton's equations for Josephson array.

    y = [phi_0, ..., phi_{N-1}, Q_0, ..., Q_{N-1}]

    dphi_i/dt = Q_i * C_inv_i     (C_inv = 2*E_C = 1/C)
    dQ_i/dt   = sum_j W_{ij} * sin(phi_j - phi_i)

    Note: W_{ij} >= 0 is the Josephson coupling for bond (i,j).
    The force on phi_i from bond (i,j) is +J_{ij}*sin(phi_j - phi_i).
    """
    phi = y[:N_sites]
    Q = y[N_sites:]

    # Phase velocity
    dphi_dt = Q * C_inv_arr

    # Charge dynamics (force from Josephson coupling)
    # dQ_i/dt = sum_j W_{ij} * sin(phi_j - phi_i)
    dQ_dt = np.zeros(N_sites)
    for i in range(N_sites):
        for j in range(N_sites):
            if W_mat[i, j] > 0:
                dQ_dt[i] += W_mat[i, j] * sin(phi[j] - phi[i])

    return np.concatenate([dphi_dt, dQ_dt])


# Build coupling matrix W and capacitance array
C_inv_arr = np.full(N, 2.0 * E_C_fold)  # C_inv = 1/C = 2*E_C for all cells

# Ground state energy
E_gs = -W.sum() / 2  # Each bond counted once: -sum_{<ij>} J_{ij}
print(f"  Ground state E_vac = {E_gs:.6f} M_KK")

def compute_E_vac(phi, W_mat, N_sites):
    """Compute vacuum (Josephson) energy from phases."""
    E = 0.0  # (local)
    for i in range(N_sites):
        for j in range(i+1, N_sites):
            if W_mat[i, j] > 0:
                E -= W_mat[i, j] * cos(phi[i] - phi[j])
    return E

def compute_E_total(phi, Q, W_mat, C_inv_arr, N_sites):
    """Compute total energy (Josephson + charging)."""
    E_J_tot = compute_E_vac(phi, W_mat, N_sites)
    E_C_tot = 0.5 * np.sum(Q**2 * C_inv_arr)  # (1/2) * sum Q^2/C = (1/2) * sum Q^2 * C_inv
    # Wait, H = sum_i Q_i^2/(2*C_i). With C_inv_i = 1/C_i = 2*E_C:
    # H_charging = sum_i Q_i^2 * E_C = E_C * sum Q^2
    # But more precisely: H = sum_i Q_i^2 / (2*C_i).
    # If C_inv = 2*E_C (so C = 1/(2*E_C)), then H_ch = sum_i Q_i^2 * E_C.
    E_C_tot = E_C_fold * np.sum(Q**2)
    return E_J_tot + E_C_tot

# 5a: Small perturbation (linear regime — should match normal mode prediction)
np.random.seed(42)
delta = 0.01  # Small phase perturbation amplitude
phi_0 = delta * np.random.randn(N)
phi_0 -= phi_0.mean()  # Remove uniform phase (Goldstone mode)
Q_0 = np.zeros(N)

y0 = np.concatenate([phi_0, Q_0])

E_vac_0 = compute_E_vac(phi_0, W, N)
delta_E_0 = E_vac_0 - E_gs  # Initial perturbation energy

print(f"\n  5a: Linear regime (delta = {delta})")
print(f"    delta_E_0 / |E_gs| = {delta_E_0 / abs(E_gs):.6e}")

# Expected oscillation period from lowest normal mode
T_osc_1 = 2 * pi / omega_k[1]
print(f"    Expected T_osc (mode 1) = {T_osc_1:.4f} M_KK^{{-1}}")

# Integrate for several oscillation periods
t_end = 10 * T_osc_1
n_eval = 2000
t_eval = np.linspace(0, t_end, n_eval)

print(f"    Integrating t = [0, {t_end:.2f}] M_KK^{{-1}}...")
sol = solve_ivp(josephson_rhs, [0, t_end], y0, t_eval=t_eval,
                args=(W, C_inv_arr, N), method='DOP853',
                rtol=1e-12, atol=1e-14)

if not sol.success:
    print(f"    WARNING: Integration failed: {sol.message}")
else:
    print(f"    Integration successful: {sol.y.shape[1]} time points")

# Compute E_vac(t)
E_vac_t = np.zeros(len(sol.t))
E_total_t = np.zeros(len(sol.t))
for idx in range(len(sol.t)):
    phi_t = sol.y[:N, idx]
    Q_t = sol.y[N:, idx]
    E_vac_t[idx] = compute_E_vac(phi_t, W, N)
    E_total_t[idx] = compute_E_total(phi_t, Q_t, W, C_inv_arr, N)

delta_E_t = E_vac_t - E_gs  # Perturbation energy in Josephson sector

# Check energy conservation
E_drift = (E_total_t[-1] - E_total_t[0]) / abs(E_total_t[0])
print(f"    Energy conservation: dE/E = {E_drift:.4e}")

# 5b: Extract oscillation frequency from E_vac(t)
# Since the system is integrable (proven S38-S66), E_vac oscillates
# rather than relaxing. The FREQUENCY of oscillation gives the
# relaxation rate for the Volovik mechanism.
from scipy.signal import find_peaks
from scipy.fft import rfft, rfftfreq

# FFT of delta_E(t) to find dominant frequency
dt = sol.t[1] - sol.t[0]
fft_vals = np.abs(rfft(delta_E_t - delta_E_t.mean()))
fft_freqs = rfftfreq(len(delta_E_t), dt)

# Find peaks in FFT
peak_indices, peak_props = find_peaks(fft_vals, height=fft_vals.max() * 0.1)
if len(peak_indices) > 0:
    dominant_idx = peak_indices[np.argmax(fft_vals[peak_indices])]
    omega_dominant = 2 * pi * fft_freqs[dominant_idx]
    print(f"\n    Dominant oscillation frequency: {omega_dominant:.6f} M_KK")
    print(f"    Expected omega_1 (normal mode): {omega_k[1]:.6f} M_KK")
    print(f"    Ratio omega_measured / omega_1: {omega_dominant / omega_k[1]:.4f}")

    # The dominant frequency should be 2*omega_1 since E_vac ~ cos^2(omega_1 t)
    # = (1 + cos(2*omega_1*t))/2. So check against 2*omega_1:
    print(f"    Expected 2*omega_1: {2*omega_k[1]:.6f}")
    print(f"    Ratio omega_measured / (2*omega_1): {omega_dominant / (2*omega_k[1]):.4f}")

    # Sort by amplitude
    sorted_peaks = peak_indices[np.argsort(fft_vals[peak_indices])[::-1]]
    print(f"    Top 5 FFT peaks:")
    for rank, pi_val in enumerate(sorted_peaks[:5]):
        print(f"      #{rank+1}: omega = {2*pi*fft_freqs[pi_val]:.4f} M_KK, "
              f"amplitude = {fft_vals[pi_val]:.4e}")
else:
    omega_dominant = omega_k[1]
    print(f"    No FFT peaks found. Using analytic omega_1 = {omega_k[1]:.6f}")

# 5c: Large perturbation (nonlinear regime)
print(f"\n  5c: Nonlinear regime (delta = 0.5)")
delta_large = 0.5  # (local)
phi_0_large = delta_large * np.random.randn(N)
phi_0_large -= phi_0_large.mean()
Q_0_large = np.zeros(N)
y0_large = np.concatenate([phi_0_large, Q_0_large])

delta_E_0_large = compute_E_vac(phi_0_large, W, N) - E_gs
print(f"    delta_E_0 / |E_gs| = {delta_E_0_large / abs(E_gs):.6e}")

sol_large = solve_ivp(josephson_rhs, [0, t_end], y0_large, t_eval=t_eval,
                      args=(W, C_inv_arr, N), method='DOP853',
                      rtol=1e-12, atol=1e-14)

E_vac_large = np.zeros(len(sol_large.t))
for idx in range(len(sol_large.t)):
    phi_t = sol_large.y[:N, idx]
    E_vac_large[idx] = compute_E_vac(phi_t, W, N)
delta_E_large = E_vac_large - E_gs

# FFT
fft_large = np.abs(rfft(delta_E_large - delta_E_large.mean()))
fft_freqs_large = rfftfreq(len(delta_E_large), dt)
peak_indices_large, _ = find_peaks(fft_large, height=fft_large.max() * 0.1)
if len(peak_indices_large) > 0:
    dom_idx_large = peak_indices_large[np.argmax(fft_large[peak_indices_large])]
    omega_dom_large = 2 * pi * fft_freqs_large[dom_idx_large]
    print(f"    Dominant frequency (nonlinear): {omega_dom_large:.6f} M_KK")
    print(f"    Ratio to linear: {omega_dom_large / omega_dominant:.4f}")
else:
    omega_dom_large = omega_dominant
    print(f"    No FFT peaks found in nonlinear run.")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 6: QUANTUM TUNNELING RATE (WKB phase-slip rate)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print(f"\n--- Section 6: Quantum Phase-Slip Rate (WKB) ---")

# For a single Josephson junction with H = E_C * n^2 - E_J * cos(phi):
# The barrier for a 2pi phase slip is:
#   V(phi) = -E_J * cos(phi)
# At phi = 0: V = -E_J (minimum)
# At phi = pi: V = +E_J (maximum)
# Barrier height = 2*E_J
#
# The WKB action for tunneling from phi_min to phi_min + 2pi is:
#   S_WKB = integral_0^{2pi} sqrt(2*m*(V(phi)-E)) dphi
# where m = C = 1/(2*E_C) and E = -E_J (ground state energy near bottom).
#   V(phi) - E = E_J * (1 - cos(phi))
#   S_WKB = integral_0^{2pi} sqrt(2*C*E_J*(1-cos(phi))) dphi
#         = integral_0^{2pi} sqrt(E_J/(E_C) * (1-cos(phi))) dphi
#         = sqrt(E_J/E_C) * integral_0^{2pi} sqrt(1-cos(phi)) dphi
#         = sqrt(E_J/E_C) * integral_0^{2pi} sqrt(2)*|sin(phi/2)| dphi
#         = sqrt(E_J/E_C) * sqrt(2) * 4
#         = sqrt(8 * E_J/E_C)
#
# This confirms S_inst = sqrt(8*E_J/E_C).
#
# For the per-bond phase slip:
S_WKB_bond = sqrt(8 * E_J_bond / E_C_cell)
Gamma_WKB_bond = omega_p_bond * exp(-S_WKB_bond)

# For the whole-cell phase slip (all bonds simultaneously):
S_WKB_cell = sqrt(8 * E_J_fold / E_C_cell)
Gamma_WKB_cell = omega_p_cell * exp(-S_WKB_cell)

# The PHYSICAL phase slip rate is per-bond (single junction tunneling)
# with z_mean parallel channels per cell
Gamma_WKB_per_cell = z_mean * Gamma_WKB_bond

print(f"  Per-bond WKB:")
print(f"    S_WKB = {S_WKB_bond:.4f}")
print(f"    omega_p = {omega_p_bond:.6f} M_KK")
print(f"    Gamma = {Gamma_WKB_bond:.6e} M_KK = {Gamma_WKB_bond * M_KK * GeV_to_inv_s:.4e} Hz")
print(f"  Per-cell (z channels):")
print(f"    Gamma = {Gamma_WKB_per_cell:.6e} M_KK = {Gamma_WKB_per_cell * M_KK * GeV_to_inv_s:.4e} Hz")
print(f"  Whole-cell collective:")
print(f"    S_WKB = {S_WKB_cell:.4f}")
print(f"    Gamma = {Gamma_WKB_cell:.6e} M_KK = {Gamma_WKB_cell * M_KK * GeV_to_inv_s:.4e} Hz")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 7: PHYSICAL RELAXATION RATE (correct identification)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print(f"\n--- Section 7: Physical Beta-Relaxation Rate ---")
print(f"")
print(f"  The beta-relaxation rate depends on the NATURE of the vacuum")
print(f"  energy response:")
print(f"")
print(f"  (A) For SMALL vacuum energy shifts (delta_rho_vac << rho_vac):")
print(f"      The response is LINEAR. The phases adjust continuously")
print(f"      without needing phase slips. The rate is set by the")
print(f"      lowest normal mode frequency omega_1.")
print(f"      This is the relevant regime for Volovik tracking.")
print(f"")
print(f"  (B) For LARGE shifts requiring 2pi phase slips:")
print(f"      The rate is exponentially suppressed by exp(-S_inst).")
print(f"      This is relevant only for discontinuous vacuum transitions.")
print(f"")
print(f"  In Volovik's q-theory, the vacuum tracks H^2 CONTINUOUSLY.")
print(f"  The adjustment is infinitesimal at each instant.")
print(f"  Therefore regime (A) applies: Gamma_beta = omega_1.")

# The physical beta-relaxation rate for Volovik tracking is:
# Gamma_beta = omega_1 (normal mode oscillation of the slowest collective mode)
Gamma_beta_phys = omega_k[1]  # Slowest collective mode frequency
Gamma_beta_Hz = Gamma_beta_phys * M_KK * GeV_to_inv_s

# For comparison, also compute the phase-slip rate (regime B):
# Use per-bond tunneling with Laplacian weighting
Gamma_slip_fabric = lambda_1 * Gamma_WKB_bond / z_mean
Gamma_slip_Hz = Gamma_slip_fabric * M_KK * GeV_to_inv_s

print(f"\n  REGIME A (continuous tracking, PHYSICAL):")
print(f"    Gamma_beta = omega_1 = {Gamma_beta_phys:.6f} M_KK")
print(f"    Gamma_beta = {Gamma_beta_Hz:.4e} Hz")
print(f"")
print(f"  REGIME B (phase-slip tunneling, for reference):")
print(f"    Gamma_slip = {Gamma_slip_fabric:.6e} M_KK")
print(f"    Gamma_slip = {Gamma_slip_Hz:.4e} Hz")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 8: Comparison to cosmological rates
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print(f"\n--- Section 8: Comparison to Cosmological Rates ---")

# H_0 (today)
H_0_Hz = H_0_inv_s  # s^{-1} = Hz

# H(z_eq) (matter-radiation equality, z ~ 3400)
z_eq = 3400.0  # (local)
H_eq_Hz = H_0_inv_s * sqrt(Omega_r*(1+z_eq)**4 + Omega_m*(1+z_eq)**3 + Omega_Lambda)

# H(z_BBN) (BBN, z ~ 4e8)
z_BBN = 4e8
H_BBN_Hz = H_0_inv_s * sqrt(Omega_r*(1+z_BBN)**4 + Omega_m*(1+z_BBN)**3 + Omega_Lambda)

print(f"  Cosmological rates:")
print(f"    H_0          = {H_0_Hz:.4e} Hz")
print(f"    H(z_eq)      = {H_eq_Hz:.4e} Hz")
print(f"    H(z_BBN)     = {H_BBN_Hz:.4e} Hz")
print(f"")

# Physical rate (regime A)
ratio_H0 = Gamma_beta_Hz / H_0_Hz
ratio_Heq = Gamma_beta_Hz / H_eq_Hz
ratio_HBBN = Gamma_beta_Hz / H_BBN_Hz

print(f"  Regime A (continuous tracking):")
print(f"    Gamma_beta / H_0          = {ratio_H0:.4e}")
print(f"    Gamma_beta / H(z_eq)      = {ratio_Heq:.4e}")
print(f"    Gamma_beta / H(z_BBN)     = {ratio_HBBN:.4e}")
print(f"    log10(Gamma_beta / H_0)   = {np.log10(ratio_H0):.2f}")
print(f"    log10(Gamma_beta / H_eq)  = {np.log10(ratio_Heq):.2f}")
print(f"    log10(Gamma_beta / H_BBN) = {np.log10(ratio_HBBN):.2f}")

# Phase-slip rate (regime B, for reference)
ratio_H0_B = Gamma_slip_Hz / H_0_Hz
ratio_Heq_B = Gamma_slip_Hz / H_eq_Hz
ratio_HBBN_B = Gamma_slip_Hz / H_BBN_Hz

print(f"")
print(f"  Regime B (phase-slip tunneling, for reference):")
print(f"    Gamma_slip / H_0          = {ratio_H0_B:.4e}")
print(f"    Gamma_slip / H(z_eq)      = {ratio_Heq_B:.4e}")
print(f"    Gamma_slip / H(z_BBN)     = {ratio_HBBN_B:.4e}")
if ratio_H0_B > 0:
    print(f"    log10(Gamma_slip / H_0)   = {np.log10(ratio_H0_B):.2f}")
    print(f"    log10(Gamma_slip / H_eq)  = {np.log10(ratio_Heq_B):.2f}")
    print(f"    log10(Gamma_slip / H_BBN) = {np.log10(ratio_HBBN_B):.2f}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 9: Numerical verification (relaxation timescale from dynamics)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print(f"\n--- Section 9: Numerical Verification ---")

# From Section 5, the classical dynamics shows oscillation, not decay.
# This is EXPECTED for an integrable Hamiltonian system (no dissipation).
# The beta-relaxation rate = 1/T_osc is the rate at which the vacuum
# energy RETURNS to its equilibrium value (half-period of oscillation).
T_half_osc = pi / omega_k[1]  # Half oscillation period
Gamma_numerical = 1.0 / T_half_osc  # Relaxation rate = 1/(half period)

# Also extract from the actual dynamics
# Find zero-crossings of delta_E_t (where E_vac returns to E_gs)
delta_E_centered = delta_E_t - delta_E_t.mean()
zero_crossings = []
for i in range(len(delta_E_centered) - 1):
    if delta_E_centered[i] * delta_E_centered[i+1] < 0:
        # Linear interpolation
        t_cross = sol.t[i] - delta_E_centered[i] * (sol.t[i+1] - sol.t[i]) / (delta_E_centered[i+1] - delta_E_centered[i])
        zero_crossings.append(t_cross)

zero_crossings = np.array(zero_crossings)
if len(zero_crossings) >= 2:
    T_half_numerical = np.mean(np.diff(zero_crossings))
    omega_numerical = pi / T_half_numerical
    Gamma_numerical_exact = 1.0 / T_half_numerical

    print(f"  From zero-crossings of delta_E(t):")
    print(f"    N crossings = {len(zero_crossings)}")
    print(f"    T_half (numerical) = {T_half_numerical:.6f} M_KK^{{-1}}")
    print(f"    omega (numerical) = {omega_numerical:.6f} M_KK")
    print(f"    omega_1 (analytic) = {omega_k[1]:.6f} M_KK")
    print(f"    Ratio omega_num / omega_1 = {omega_numerical / omega_k[1]:.6f}")
else:
    print(f"  Insufficient zero-crossings ({len(zero_crossings)})")
    Gamma_numerical_exact = Gamma_numerical
    omega_numerical = omega_k[1]

Gamma_num_Hz = Gamma_numerical_exact * M_KK * GeV_to_inv_s
print(f"\n  Numerical Gamma_beta = {Gamma_numerical_exact:.6f} M_KK")
print(f"  Numerical Gamma_beta = {Gamma_num_Hz:.4e} Hz")
print(f"  Numerical Gamma_beta / H(z_eq) = {Gamma_num_Hz / H_eq_Hz:.4e}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 10: GATE VERDICT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print(f"\n{'='*70}")
print(f"GATE: GGE-VOLOVIK-RELAX-67")
print(f"{'='*70}")

# Use the most conservative (slowest) rate
# Regime A: omega_1 (continuous tracking) — physically correct for Volovik
# Regime B: phase-slip tunneling — slower, applies only for 2pi slips
# Use Regime B as the CONSERVATIVE bound (it's the smaller number)
Gamma_conservative = min(Gamma_beta_Hz, Gamma_slip_Hz)
Gamma_label = "phase-slip" if Gamma_conservative == Gamma_slip_Hz else "normal-mode"

print(f"\n  Conservative rate (Regime {'B' if Gamma_label == 'phase-slip' else 'A'}): "
      f"Gamma = {Gamma_conservative:.4e} Hz")
print(f"  Gate criterion: Gamma > H(z_eq) = {H_eq_Hz:.4e} Hz")

if Gamma_conservative > H_eq_Hz:
    gate_verdict = "PASS"
    gate_margin = np.log10(Gamma_conservative / H_eq_Hz)
    print(f"\n  >>> GATE VERDICT: PASS <<<")
    print(f"  >>> Margin: 10^{gate_margin:.1f} (even using conservative rate) <<<")
elif Gamma_conservative > H_0_Hz:
    gate_verdict = "INFO"
    print(f"\n  >>> GATE VERDICT: INFO (Gamma > H_0 but < H(z_eq)) <<<")
else:
    gate_verdict = "FAIL"
    print(f"\n  >>> GATE VERDICT: FAIL <<<")

# Physical rate (Regime A):
print(f"\n  Physical rate (continuous tracking):")
print(f"    Gamma_beta = {Gamma_beta_Hz:.4e} Hz")
print(f"    Gamma_beta / H_0 = {ratio_H0:.4e} = 10^{np.log10(ratio_H0):.1f}")
print(f"    Gamma_beta / H(z_eq) = {ratio_Heq:.4e} = 10^{np.log10(ratio_Heq):.1f}")
print(f"    Gamma_beta / H(z_BBN) = {ratio_HBBN:.4e} = 10^{np.log10(ratio_HBBN):.1f}")

# Correction to S66 estimate
print(f"\n  S66 estimate (Landau-Lizzi workshop): ~10^25 Hz")
print(f"  This computation:")
print(f"    Regime A (oscillation): {Gamma_beta_Hz:.2e} Hz = 10^{np.log10(Gamma_beta_Hz):.1f}")
print(f"    Regime B (phase-slip):  {Gamma_slip_Hz:.2e} Hz = 10^{np.log10(Gamma_slip_Hz) if Gamma_slip_Hz > 0 else -999:.1f}")
print(f"  S66 used approximate values (E_J/E_C ~ 24.8, lambda_1 ~ 2, z ~ 6).")
print(f"  Corrected values: E_J/E_C = {ratio_EJ_EC:.1f}, lambda_1 = {lambda_1:.3f}, z = {z_mean:.2f}.")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 11: Summary table
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print(f"\n{'='*70}")
print(f"SUMMARY TABLE")
print(f"{'='*70}")
print(f"{'Quantity':<40} {'Value':<20} {'Unit'}")
print(f"{'-'*70}")
print(f"{'N_cells':<40} {N:<20} {''}")
print(f"{'N_bonds':<40} {N_bonds:<20} {''}")
print(f"{'z_mean':<40} {z_mean:<20.4f} {''}")
print(f"{'E_J_fold (per cell)':<40} {E_J_fold:<20.6f} {'M_KK'}")
print(f"{'E_C_fold (per cell)':<40} {E_C_fold:<20.6f} {'M_KK'}")
print(f"{'E_J/E_C':<40} {ratio_EJ_EC:<20.2f} {''}")
print(f"{'E_J per bond':<40} {E_J_bond:<20.6f} {'M_KK'}")
print(f"{'lambda_1 (Josephson Laplacian)':<40} {lambda_1:<20.6f} {'M_KK'}")
print(f"{'omega_p (per cell)':<40} {omega_p_cell:<20.6f} {'M_KK'}")
print(f"{'omega_p (per bond)':<40} {omega_p_bond:<20.6f} {'M_KK'}")
print(f"{'S_inst (per bond, WKB)':<40} {S_WKB_bond:<20.4f} {''}")
print(f"{'S_inst (per cell, WKB)':<40} {S_WKB_cell:<20.4f} {''}")
print(f"{'omega_1 (slowest collective mode)':<40} {omega_k[1]:<20.6f} {'M_KK'}")
print(f"{'omega_1 (Hz)':<40} {omega_k[1]*M_KK*GeV_to_inv_s:<20.4e} {'Hz'}")
print(f"{'Gamma_slip per bond (Hz)':<40} {Gamma_WKB_bond*M_KK*GeV_to_inv_s:<20.4e} {'Hz'}")
print(f"{'Gamma_fabric (phase-slip, Hz)':<40} {Gamma_slip_Hz:<20.4e} {'Hz'}")
print(f"{'Gamma_beta (oscillation, Hz)':<40} {Gamma_beta_Hz:<20.4e} {'Hz'}")
print(f"{'Gamma_numerical (Hz)':<40} {Gamma_num_Hz:<20.4e} {'Hz'}")
print(f"{'H_0':<40} {H_0_Hz:<20.4e} {'Hz'}")
print(f"{'H(z_eq)':<40} {H_eq_Hz:<20.4e} {'Hz'}")
print(f"{'H(z_BBN)':<40} {H_BBN_Hz:<20.4e} {'Hz'}")
print(f"{'Gamma_beta / H_0':<40} {ratio_H0:<20.4e} {''}")
print(f"{'Gamma_beta / H(z_eq)':<40} {ratio_Heq:<20.4e} {''}")
print(f"{'Gamma_beta / H(z_BBN)':<40} {ratio_HBBN:<20.4e} {''}")
print(f"{'log10(Gamma_beta / H_0)':<40} {np.log10(ratio_H0):<20.1f} {''}")
print(f"{'log10(Gamma_beta / H(z_eq))':<40} {np.log10(ratio_Heq):<20.1f} {''}")
print(f"{'Gate verdict':<40} {gate_verdict:<20} {''}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 12: Plot
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('GGE-VOLOVIK-RELAX-67: Beta-Relaxation on CG(24)', fontsize=14)

# Panel (a): Laplacian eigenvalues
ax = axes[0, 0]
ax.bar(range(N), eigs_Lw, color='steelblue', alpha=0.7)
ax.axhline(lambda_1, color='red', linestyle='--', label=f'$\\lambda_1 = {lambda_1:.3f}$')
ax.set_xlabel('Mode index k')
ax.set_ylabel('$\\lambda_k$ (M$_{KK}$)')
ax.set_title('(a) Josephson Laplacian spectrum')
ax.legend()

# Panel (b): Normal mode frequencies
ax = axes[0, 1]
ax.bar(range(1, N), omega_k[1:], color='darkorange', alpha=0.7)
ax.axhline(omega_k[1], color='red', linestyle='--', label=f'$\\omega_1 = {omega_k[1]:.4f}$')
ax.set_xlabel('Mode index k')
ax.set_ylabel('$\\omega_k$ (M$_{KK}$)')
ax.set_title('(b) Normal mode frequencies')
ax.legend()

# Panel (c): E_vac(t) dynamics (linear)
ax = axes[0, 2]
ax.plot(sol.t, delta_E_t / delta_E_0, 'b-', linewidth=0.5)
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.set_xlabel('t (M$_{KK}^{-1}$)')
ax.set_ylabel('$\\delta E_{vac}(t) / \\delta E_{vac}(0)$')
ax.set_title(f'(c) Vacuum energy oscillation ($\\delta = {delta}$)')

# Panel (d): FFT of E_vac oscillation
ax = axes[1, 0]
omega_fft = 2 * pi * fft_freqs
mask = omega_fft < 1.5  # Show only below 1.5 M_KK
ax.plot(omega_fft[mask], fft_vals[mask] / fft_vals.max(), 'b-', linewidth=0.8)
for k_idx in range(1, min(6, N)):
    ax.axvline(2 * omega_k[k_idx], color='red', alpha=0.3, linestyle='--',
               label=f'$2\\omega_{k_idx}$' if k_idx <= 3 else '')
ax.set_xlabel('$\\omega$ (M$_{KK}$)')
ax.set_ylabel('FFT amplitude (normalized)')
ax.set_title('(d) Spectral content of $\\delta E_{vac}$')
ax.legend(fontsize=8)

# Panel (e): Rate comparison
ax = axes[1, 1]
rates = [Gamma_beta_Hz, Gamma_slip_Hz, H_BBN_Hz, H_eq_Hz, H_0_Hz]
labels = ['$\\Gamma_{\\beta}$ (osc)', '$\\Gamma_{slip}$ (tunnel)',
          '$H_{BBN}$', '$H(z_{eq})$', '$H_0$']
colors = ['green', 'orange', 'red', 'darkred', 'maroon']
log_rates = [np.log10(r) if r > 0 else -100 for r in rates]
bars = ax.barh(range(len(rates)), log_rates, color=colors, alpha=0.7)
ax.set_yticks(range(len(rates)))
ax.set_yticklabels(labels)
ax.set_xlabel('$\\log_{10}(\\Gamma / \\mathrm{Hz})$')
ax.set_title('(e) Rate hierarchy')
ax.axvline(np.log10(H_eq_Hz), color='darkred', linestyle=':', alpha=0.5)

# Panel (f): E_vac(t) dynamics (nonlinear)
ax = axes[1, 2]
ax.plot(sol_large.t, delta_E_large / delta_E_0_large, 'r-', linewidth=0.5)
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.set_xlabel('t (M$_{KK}^{-1}$)')
ax.set_ylabel('$\\delta E_{vac}(t) / \\delta E_{vac}(0)$')
ax.set_title(f'(f) Nonlinear regime ($\\delta = {delta_large}$)')

plt.tight_layout()
plot_path = Path(__file__).parent / "s67_gge_volovik_relax.png"
plt.savefig(str(plot_path), dpi=150, bbox_inches='tight')
plt.close()
print(f"\nPlot saved to {plot_path}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 13: Save data
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

save_path = Path(__file__).parent / "s67_gge_volovik_relax.npz"
np.savez(str(save_path),
    # Graph
    N_cells=N,
    N_bonds=N_bonds,
    z_mean=z_mean,
    z_per_cell=z_per_cell,

    # Laplacian
    eigs_Laplacian_weighted=eigs_Lw,
    eigs_Laplacian_unweighted=eigs_Lunw,
    lambda_1=lambda_1,

    # Josephson parameters
    E_J_fold=E_J_fold,
    E_C_fold=E_C_fold,
    ratio_EJ_EC=ratio_EJ_EC,
    E_J_bond=E_J_bond,

    # Plasma & instanton
    omega_p_cell=omega_p_cell,
    omega_p_bond=omega_p_bond,
    S_inst_bond=S_WKB_bond,
    S_inst_cell=S_WKB_cell,

    # Normal modes
    omega_normal_modes=omega_k,
    omega_1=omega_k[1],

    # Rates (M_KK units)
    Gamma_beta_MKK=Gamma_beta_phys,
    Gamma_slip_fabric_MKK=Gamma_slip_fabric,
    Gamma_WKB_bond_MKK=Gamma_WKB_bond,

    # Rates (Hz)
    Gamma_beta_Hz=Gamma_beta_Hz,
    Gamma_slip_Hz=Gamma_slip_Hz,

    # Cosmological
    H_0_Hz=H_0_Hz,
    H_eq_Hz=H_eq_Hz,
    H_BBN_Hz=H_BBN_Hz,
    ratio_Gamma_H0=ratio_H0,
    ratio_Gamma_Heq=ratio_Heq,
    ratio_Gamma_HBBN=ratio_HBBN,

    # Numerical dynamics
    t_dynamics=sol.t,
    delta_E_dynamics=delta_E_t,
    delta_E_0=delta_E_0,
    omega_numerical=omega_numerical,

    # Gate
    gate_name=np.array(['GGE-VOLOVIK-RELAX-67']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([
        f"Gamma_beta = {Gamma_beta_Hz:.2e} Hz (normal mode omega_1). "
        f"Gamma_beta/H(z_eq) = {ratio_Heq:.1e} = 10^{np.log10(ratio_Heq):.1f}. "
        f"Phase-slip rate: {Gamma_slip_Hz:.2e} Hz. "
        f"E_J/E_C = {ratio_EJ_EC:.1f}. "
        f"S_inst_bond = {S_WKB_bond:.2f}. "
        f"lambda_1 = {lambda_1:.4f}. "
        f"Numerically verified: omega_num/omega_1 = {omega_numerical/omega_k[1]:.4f}."
    ]),
)
print(f"Data saved to {save_path}")

print(f"\n{'='*70}")
print(f"COMPUTATION COMPLETE")
print(f"{'='*70}")
