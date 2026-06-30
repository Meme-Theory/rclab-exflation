#!/usr/bin/env python3
"""
s55_floquet.py — Floquet Analysis of Periodically Driven 1-Pair BCS Hamiltonian
================================================================================

FLOQUET-55 gate: INFO — parametric instability tongues

Physics:
    At the fold tau~0.19, the 8-mode BCS Hamiltonian in the 1-pair sector is:
        H_0 = diag(2*eps_1, ..., 2*eps_8) + V     (8x8, static)

    We modulate the kinetic hopping J(t) = J_0*(1 + A*cos(omega*t)):
        H(t) = H_0 + A*cos(omega*t) * H_1
    where H_1 = diag(2*eps_1, ..., 2*eps_8) is the kinetic part.

    The Floquet propagator U(T) = T*exp(-i integral_0^T H(t) dt) over one period T=2pi/omega
    is computed via Trotter decomposition (N_steps substeps).

    Since H(t) is Hermitian, U(T) is unitary and all Floquet multipliers lie on the unit circle.
    Parametric resonance manifests as:
    1. Quasienergy crossings/avoided crossings (resonance conditions)
    2. Large ground-state depletion: P_exc = 1 - |<psi_0|U(T)|psi_0>|^2
    3. Arnold tongues: regions in (omega, A) where P_exc exceeds threshold

    We also construct the BdG extension (16x16) where particle-hole mixing
    allows true parametric instability (|eigenvalue| != 1).

Created: Session 55
Gate: FLOQUET-55 (INFO)
"""

import sys
import os
import numpy as np
from scipy.linalg import expm, eig
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

sys.path.insert(0, 'computations')
from canonical_constants import (
    omega_PV, omega_L1, omega_L2, omega_H1, tau_fold,
    E_cond, J_C2, J_su2, J_u1
)

# =============================================================================
# Load data
# =============================================================================
d_tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
d_ed = np.load('computations/session-54/s54_ed_sweep.npz', allow_pickle=True)

fold_idx = int(d_ed['fold_idx'])
tau_f = d_tb['tau_values'][fold_idx]
print(f"Fold: tau = {tau_f:.4f} (idx {fold_idx})")

# Single-particle energies at fold (8 modes in M_KK units)
E_sp = d_ed['E_sp_sweep'][fold_idx].copy()
N_modes = len(E_sp)
print(f"N_modes = {N_modes}")
print(f"E_sp = {E_sp}")

# BCS interaction matrix (8x8)
V = d_ed['V_bare_cont'].copy()

# =============================================================================
# Construct static H_0 in 1-pair sector
# =============================================================================
# H_0 = diag(2*eps_i) + V_ij
H_kin = np.diag(2.0 * E_sp)
H_0 = H_kin + V

# Verify: eigenvalues should match all_eigenvalues_N1
evals_H0 = np.sort(np.linalg.eigvalsh(H_0))
evals_ref = np.sort(d_ed['all_eigenvalues_N1'][fold_idx])
print(f"\nH_0 eigenvalues:  {evals_H0}")
print(f"Reference (N1):   {evals_ref}")
print(f"Max discrepancy:  {np.max(np.abs(evals_H0 - evals_ref)):.2e}")

# Ground state of H_0
evals_0, evecs_0 = np.linalg.eigh(H_0)
psi_0 = evecs_0[:, 0]  # ground state

# Energy gaps from ground state
gaps = evals_0 - evals_0[0]
print(f"\nEnergy gaps from ground state (M_KK):")
for i, g in enumerate(gaps):
    print(f"  E_{i} - E_0 = {g:.6f}")

# =============================================================================
# Perturbation H_1: kinetic part (hopping modulation)
# =============================================================================
# Modulating J -> modulates single-particle energies -> H_1 = diag(2*eps_i)
# This is because eps_i are eigenvalues of the tight-binding Hamiltonian,
# which scale linearly with J. So delta_H = (delta_J/J) * H_kin = A * H_kin * cos(omega*t)
H_1 = H_kin.copy()

print(f"\n||H_0|| = {np.linalg.norm(H_0):.4f}")
print(f"||H_1|| = {np.linalg.norm(H_1):.4f}")
print(f"||V||   = {np.linalg.norm(V):.4f}")

# =============================================================================
# Floquet propagator via Trotter decomposition
# =============================================================================
def floquet_propagator(H_0, H_1, omega, A, N_steps=500):
    """
    Compute U(T) for H(t) = H_0 + A*cos(omega*t)*H_1
    via first-order Trotter with N_steps substeps.
    T = 2*pi/omega.
    """
    T = 2.0 * np.pi / omega
    dt = T / N_steps
    n = H_0.shape[0]
    U = np.eye(n, dtype=complex)
    for k in range(N_steps):
        t_k = (k + 0.5) * dt  # midpoint
        H_t = H_0 + A * np.cos(omega * t_k) * H_1
        U = expm(-1j * H_t * dt) @ U
    return U


def quasienergies(U, omega):
    """
    Extract Floquet quasienergies from propagator U(T).
    eps_n = -arg(lambda_n) * omega / (2*pi), folded into [-omega/2, omega/2).
    """
    evals = np.linalg.eigvals(U)
    phases = np.angle(evals)
    eps = -phases * omega / (2.0 * np.pi)
    return np.sort(eps.real)


def ground_state_excitation(U, psi_0):
    """
    Compute probability of leaving ground state after one period.
    P_exc = 1 - |<psi_0|U|psi_0>|^2
    """
    overlap = np.conj(psi_0) @ U @ psi_0
    return 1.0 - abs(overlap)**2


# =============================================================================
# BdG Extension: 16x16 particle-hole Hamiltonian
# =============================================================================
# In BdG formalism, the Hamiltonian mixes particle (p) and hole (h) sectors:
#   H_BdG = [[H_pair, Delta], [Delta^*, -H_pair^*]]
# For the 1-pair sector with pairing field proportional to interaction V:
# Delta_ij ~ V_ij (gap matrix). The BdG propagator can have |eigenvalue| != 1.
#
# We construct: H_BdG(t) = [[H(t) - mu*I, Delta], [Delta, -(H(t)-mu*I)]]
# where Delta = alpha * V (alpha = pairing strength), mu = E_0 (Fermi level = ground state energy)

def bdg_floquet(H_0, H_1, V_pair, omega, A, alpha=1.0, N_steps=500):
    """
    Compute BdG Floquet propagator (2N x 2N).
    H_BdG(t) = [[H(t)-mu, Delta], [Delta, -(H(t)-mu)^T]]
    with mu = ground state energy, Delta = alpha * V_pair.

    Returns eigenvalues of U_BdG(T) — if any |lambda| != 1, parametric instability.
    """
    n = H_0.shape[0]
    mu = np.linalg.eigvalsh(H_0)[0]  # ground state energy as chemical potential
    Delta = alpha * V_pair

    T_period = 2.0 * np.pi / omega
    dt = T_period / N_steps
    U = np.eye(2 * n, dtype=complex)

    for k in range(N_steps):
        t_k = (k + 0.5) * dt
        H_t = H_0 + A * np.cos(omega * t_k) * H_1
        H_shifted = H_t - mu * np.eye(n)

        H_BdG = np.zeros((2*n, 2*n), dtype=complex)
        H_BdG[:n, :n] = H_shifted
        H_BdG[:n, n:] = Delta
        H_BdG[n:, :n] = Delta.conj()
        H_BdG[n:, n:] = -H_shifted.T

        U = expm(-1j * H_BdG * dt) @ U

    evals_bdg = np.linalg.eigvals(U)
    return evals_bdg


# =============================================================================
# SWEEP 1: Quasienergy spectrum vs omega at fixed A
# =============================================================================
print("\n" + "="*70)
print("SWEEP 1: Quasienergy spectrum vs omega")
print("="*70)

A_fixed = 0.3  # moderate modulation  # (local)
omega_min, omega_max = 0.02, 1.5
N_omega_fine = 300

omegas_fine = np.linspace(omega_min, omega_max, N_omega_fine)
QE = np.zeros((N_omega_fine, N_modes))

for i, om in enumerate(omegas_fine):
    U = floquet_propagator(H_0, H_1, om, A_fixed, N_steps=400)
    QE[i] = quasienergies(U, om)

# =============================================================================
# SWEEP 2: Arnold tongue map — P_exc(omega, A)
# =============================================================================
print("\n" + "="*70)
print("SWEEP 2: Arnold tongue map P_exc(omega, A)")
print("="*70)

# Fine grid around resonance frequencies
# Resonances occur at omega = Delta_E / n for integer n (n-photon absorption)
N_omega = 200  # (local)
N_A = 80  # (local)
omegas = np.linspace(0.02, 1.5, N_omega)
amplitudes = np.linspace(0.01, 1.0, N_A)

P_exc_map = np.zeros((N_A, N_omega))

total = N_omega * N_A
done = 0
for j, A_val in enumerate(amplitudes):
    for i, om in enumerate(omegas):
        U = floquet_propagator(H_0, H_1, om, A_val, N_steps=300)
        P_exc_map[j, i] = ground_state_excitation(U, psi_0)
        done += 1
    if (j+1) % 10 == 0:
        print(f"  A sweep: {j+1}/{N_A} done ({done}/{total} total)")

# =============================================================================
# SWEEP 3: BdG instability check
# =============================================================================
print("\n" + "="*70)
print("SWEEP 3: BdG instability (|Floquet multiplier| != 1)")
print("="*70)

N_omega_bdg = 100
N_A_bdg = 50
omegas_bdg = np.linspace(0.02, 1.5, N_omega_bdg)
amplitudes_bdg = np.linspace(0.01, 1.0, N_A_bdg)

# Max deviation from unit circle
max_dev_map = np.zeros((N_A_bdg, N_omega_bdg))

for j, A_val in enumerate(amplitudes_bdg):
    for i, om in enumerate(omegas_bdg):
        evals_bdg = bdg_floquet(H_0, H_1, V, om, A_val, alpha=1.0, N_steps=300)
        mods = np.abs(evals_bdg)
        max_dev_map[j, i] = np.max(np.abs(mods - 1.0))
    if (j+1) % 10 == 0:
        print(f"  BdG sweep: {j+1}/{N_A_bdg} done")

# =============================================================================
# ANALYSIS: Find resonance tongues
# =============================================================================
print("\n" + "="*70)
print("ANALYSIS")
print("="*70)

# Find omega values with strongest excitation at each A
resonance_omegas = []
resonance_As = []
resonance_Pexc = []

P_exc_threshold = 0.5  # significant excitation  # (local)

for j, A_val in enumerate(amplitudes):
    # Find peaks in P_exc vs omega
    P_row = P_exc_map[j]
    # Simple peak finding: local maxima above threshold
    for i in range(1, N_omega - 1):
        if P_row[i] > P_exc_threshold and P_row[i] > P_row[i-1] and P_row[i] > P_row[i+1]:
            resonance_omegas.append(omegas[i])
            resonance_As.append(A_val)
            resonance_Pexc.append(P_row[i])

print(f"Found {len(resonance_omegas)} resonance points above P_exc > {P_exc_threshold}")

# Identify principal tongues by clustering near expected resonance frequencies
# Expected: omega = gap_n, gap_n/2, gap_n/3, ... (n-photon resonances)
print(f"\nExpected resonance frequencies (1-photon):")
for i, g in enumerate(gaps[1:], 1):
    print(f"  omega = gap_{i} = {g:.4f}")
    print(f"  omega = gap_{i}/2 = {g/2:.4f} (2-photon)")

# BdG instability summary
max_bdg_deviation = np.max(max_dev_map)
print(f"\nBdG max |eigenvalue| deviation from 1: {max_bdg_deviation:.6e}")
if max_bdg_deviation > 0.01:
    print("  --> TRUE PARAMETRIC INSTABILITY DETECTED in BdG sector")
    # Find the tongue locations
    bdg_threshold = 0.01  # (local)
    bdg_unstable = max_dev_map > bdg_threshold
    if np.any(bdg_unstable):
        bdg_j, bdg_i = np.where(bdg_unstable)
        print(f"  Unstable region: omega in [{omegas_bdg[bdg_i.min()]:.3f}, {omegas_bdg[bdg_i.max()]:.3f}]")
        print(f"                   A in [{amplitudes_bdg[bdg_j.min()]:.3f}, {amplitudes_bdg[bdg_j.max()]:.3f}]")
else:
    print("  --> No BdG instability (all multipliers on unit circle to 1e-2)")

# Tongue widths at specific A values
print(f"\nArnold tongue widths (P_exc > 0.5) at selected amplitudes:")
for A_check in [0.1, 0.3, 0.5, 0.8]:
    j_A = np.argmin(np.abs(amplitudes - A_check))
    unstable_mask = P_exc_map[j_A] > 0.5
    if np.any(unstable_mask):
        unstable_omegas = omegas[unstable_mask]
        # Find connected regions
        regions = []
        start = unstable_omegas[0]
        prev = start
        for om in unstable_omegas[1:]:
            if om - prev > 2 * (omegas[1] - omegas[0]):
                regions.append((start, prev))
                start = om
            prev = om
        regions.append((start, prev))
        print(f"  A={A_check:.1f}: {len(regions)} tongue(s)")
        for r_start, r_end in regions:
            center = (r_start + r_end) / 2
            width = r_end - r_start
            # Find nearest gap
            nearest_gap_idx = np.argmin(np.abs(gaps[1:] - center)) + 1
            print(f"    [{r_start:.4f}, {r_end:.4f}] center={center:.4f} width={width:.4f} "
                  f"(near gap_{nearest_gap_idx}={gaps[nearest_gap_idx]:.4f})")
    else:
        print(f"  A={A_check:.1f}: no tongues above threshold")

# Multi-period P_exc accumulation
print(f"\nMulti-period excitation (A=0.3, selected omegas):")
test_omegas = [gaps[1]/2, gaps[1], omega_L1, omega_PV, gaps[2]/2, gaps[2]]
for om_test in test_omegas:
    if om_test < 0.02:
        continue
    U1 = floquet_propagator(H_0, H_1, om_test, 0.3, N_steps=400)
    # Multi-period: U^n
    psi = psi_0.astype(complex).copy()
    P_vs_n = []
    for n_period in range(1, 21):
        psi = U1 @ psi
        P_vs_n.append(1.0 - abs(np.conj(psi_0) @ psi)**2)
    print(f"  omega={om_test:.4f}: P_exc after 1,5,10,20 periods = "
          f"{P_vs_n[0]:.4f}, {P_vs_n[4]:.4f}, {P_vs_n[9]:.4f}, {P_vs_n[19]:.4f}")

# =============================================================================
# PLOT
# =============================================================================
fig = plt.figure(figsize=(18, 14))

# --- Panel 1: Quasienergy spectrum ---
ax1 = fig.add_subplot(2, 2, 1)
for m in range(N_modes):
    ax1.scatter(omegas_fine, QE[:, m], s=0.3, c='steelblue', alpha=0.5)
# Mark resonance frequencies
for i, g in enumerate(gaps[1:], 1):
    ax1.axvline(g, color='red', ls='--', alpha=0.5, lw=0.8, label=f'gap_{i}={g:.3f}' if i <= 3 else None)
    ax1.axvline(g/2, color='orange', ls=':', alpha=0.4, lw=0.8)
ax1.axvline(omega_L1, color='green', ls='-', alpha=0.7, lw=1.2, label=f'omega_L1={omega_L1:.3f}')
ax1.axvline(omega_PV, color='purple', ls='-', alpha=0.7, lw=1.2, label=f'omega_PV={omega_PV:.3f}')
ax1.set_xlabel('omega (M_KK)')
ax1.set_ylabel('Quasienergy (M_KK)')
ax1.set_title(f'Floquet Quasienergies (A={A_fixed})')
ax1.legend(fontsize=7, loc='upper left')

# --- Panel 2: Arnold tongue map (P_exc) ---
ax2 = fig.add_subplot(2, 2, 2)
im = ax2.pcolormesh(omegas, amplitudes, P_exc_map,
                     cmap='hot', vmin=0, vmax=1, shading='auto')
plt.colorbar(im, ax=ax2, label='P_exc')
# Mark canonical frequencies
for i, g in enumerate(gaps[1:4], 1):
    ax2.axvline(g, color='cyan', ls='--', alpha=0.7, lw=0.8)
    ax2.axvline(g/2, color='cyan', ls=':', alpha=0.5, lw=0.6)
ax2.axvline(omega_L1, color='lime', ls='-', alpha=0.8, lw=1.0)
ax2.axvline(omega_PV, color='magenta', ls='-', alpha=0.8, lw=1.0)
ax2.set_xlabel('omega (M_KK)')
ax2.set_ylabel('Amplitude A')
ax2.set_title('Arnold Tongue Map: Ground-State Excitation')

# --- Panel 3: BdG instability map ---
ax3 = fig.add_subplot(2, 2, 3)
im3 = ax3.pcolormesh(omegas_bdg, amplitudes_bdg, max_dev_map,
                      cmap='inferno', shading='auto',
                      norm=LogNorm(vmin=max(1e-15, max_dev_map[max_dev_map > 0].min() if np.any(max_dev_map > 0) else 1e-15),
                                   vmax=max(1e-10, max_dev_map.max())))
plt.colorbar(im3, ax=ax3, label='max(||lambda| - 1|)')
ax3.axvline(omega_L1, color='lime', ls='-', alpha=0.8, lw=1.0, label=f'omega_L1')
ax3.axvline(omega_PV, color='magenta', ls='-', alpha=0.8, lw=1.0, label=f'omega_PV')
ax3.set_xlabel('omega (M_KK)')
ax3.set_ylabel('Amplitude A')
ax3.set_title('BdG Floquet: |multiplier| deviation from 1')
ax3.legend(fontsize=7)

# --- Panel 4: P_exc slices at fixed A ---
ax4 = fig.add_subplot(2, 2, 4)
for A_slice in [0.1, 0.3, 0.5, 0.8]:
    j_A = np.argmin(np.abs(amplitudes - A_slice))
    ax4.plot(omegas, P_exc_map[j_A], label=f'A={A_slice:.1f}', alpha=0.8)
ax4.axvline(omega_L1, color='green', ls='--', alpha=0.5, label=f'omega_L1={omega_L1:.3f}')
ax4.axvline(omega_PV, color='purple', ls='--', alpha=0.5, label=f'omega_PV={omega_PV:.3f}')
for i, g in enumerate(gaps[1:4], 1):
    ax4.axvline(g, color='red', ls=':', alpha=0.3)
ax4.set_xlabel('omega (M_KK)')
ax4.set_ylabel('P_exc')
ax4.set_title('Ground-State Depletion vs Frequency')
ax4.legend(fontsize=7)
ax4.set_ylim(-0.05, 1.05)

fig.suptitle(f'FLOQUET-55: Parametric Instability of 1-Pair BCS Walker (tau={tau_f:.4f})',
             fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('computations/session-55/s55_floquet.png', dpi=150, bbox_inches='tight')
print(f"\nPlot saved: computations/session-55/s55_floquet.png")

# =============================================================================
# SAVE DATA
# =============================================================================
np.savez('computations/session-55/s55_floquet.npz',
         # Sweep parameters
         omegas_qe=omegas_fine,
         omegas_arnold=omegas,
         amplitudes=amplitudes,
         omegas_bdg=omegas_bdg,
         amplitudes_bdg=amplitudes_bdg,
         # Results
         quasienergies=QE,
         P_exc_map=P_exc_map,
         max_dev_bdg=max_dev_map,
         # Static Hamiltonian info
         H_0=H_0,
         H_1=H_1,
         V_pair=V,
         evals_H0=evals_0,
         evecs_H0=evecs_0,
         gaps=gaps,
         E_sp=E_sp,
         tau_fold=tau_f,
         fold_idx=fold_idx,
         A_fixed=A_fixed,
         # Canonical frequencies
         omega_L1=omega_L1,
         omega_PV=omega_PV,
         # Gate
         gate_name='FLOQUET-55',
         gate_verdict='INFO')
print("Data saved: computations/session-55/s55_floquet.npz")

print("\n" + "="*70)
print("FLOQUET-55 COMPLETE")
print("="*70)
