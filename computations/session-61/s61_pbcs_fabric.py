#!/usr/bin/env python3
"""
S61 — PBCS-FABRIC-61: PBCS Correction Scaling with Fabric Size
================================================================

Gate: PBCS-FABRIC-61
  PASS if delta_a2(2-cell) < delta_a2(1-cell) — correction decreases with fabric size.
  FAIL if delta_a2(2-cell) > delta_a2(1-cell) — correction increases.
  INFO if |ratio - 1| < 0.1 — less than 10% change.

Physics:
  In nuclear DFT (Papers 02, 03, 17), the PBCS/BCS correction scales as
  ~1/N_eff where N_eff is the effective number of modes participating in
  pairing. As the system grows (more cells, more modes), the relative
  particle-number fluctuation <(Delta N)^2>/N decreases, and the
  projection correction shrinks.

  For the framework: going from 1 cell (8 modes) to 2 cells (16 modes)
  with inter-cell Josephson coupling E_J, the effective pairing volume
  doubles. If the correction decreases, the thermodynamic limit restores
  number symmetry automatically — meaning PBCS corrections to the
  spectral action are irrelevant in the macroscopic fabric.

  Method:
    1. Single-cell: Use NAZ-1 results directly (s61_proj_a2.npz).
    2. Two-cell: Construct H = sum_{cell} [H_BCS(cell)] + H_J(Josephson)
       with 2 modes per cell (dim=16 for tractability), or full 8-mode
       per cell (dim ~ 65536 at N_pair=1, but we use pair-space not Fock).
    3. For each: solve BCS (HFB) and PBCS (number-projected Fomenko).
    4. Compute a_2-proxy = sum_k n_k * eps_k + pairing correction.
    5. Compare delta_a2 = |a2_PBCS - a2_BCS| / a2_BCS at each size.

  Nuclear analog:
    ^18O (8 modes, 1 major shell) -> ^36Ar (16 modes, 2 major shells)
    Projection correction drops from ~10% to ~5% (Paper 03 systematics).

Author: Nazarewicz Nuclear Structure Theorist (Session 61)
Date: 2026-03-28
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.linalg import eigh
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI,
    E_cond, N_dof_BCS,
    a0_fold, a2_fold, a4_fold,
    J_C2,
)

np.set_printoptions(precision=8, linewidth=120)

# ==============================================================================
#  SECTION 1: Load Input Data
# ==============================================================================

print("=" * 72)
print("PBCS-FABRIC-61: PBCS Correction Scaling with Fabric Size")
print("=" * 72)

# Load single-cell data from NAZ-1
naz1 = np.load('s61_proj_a2.npz', allow_pickle=True)
print(f"\nNAZ-1 single-cell results loaded.")
print(f"  Gate: {naz1['gate_name']} = {naz1['gate_verdict']}")
print(f"  a2_geom = {float(naz1['a2_geom']):.10f}")
print(f"  R_fold = {float(naz1['R_fold']):.10f}")

# Load S52 HFB data for interaction
s52 = np.load('s52_hfb_full.npz', allow_pickle=True)
E_sp_8 = s52['E_sp_bare']
V_bare_8 = s52['V_bare']
labels_8 = s52['labels']

# Load S60 2-cell data for Josephson coupling
s60 = np.load('s60_rg_integrals.npz', allow_pickle=True)
E_J_fold = float(s60['E_J_fold'])
eps_fold_8 = s60['eps_fold']

print(f"\nS52 HFB data: {len(E_sp_8)} modes, V_bare {V_bare_8.shape}")
print(f"S60 2-cell data: E_J = {E_J_fold:.4f} M_KK")
print(f"  eps_fold = {eps_fold_8}")

a2_geom = float(naz1['a2_geom'])
R_fold = float(naz1['R_fold'])
a0_geom = float(naz1['a0_geom'])


# ==============================================================================
#  SECTION 2: Extract Single-Cell NAZ-1 Results
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 2: Single-Cell Results (from NAZ-1)")
print(f"{'='*72}")

# The key quantity is delta_a2 = |a2_PROJ - a2_HFB| / a2_HFB
# This is the fractional correction from number projection.
# NAZ-1 computed this for N=1,2,3,4.

single_cell_results = {}
for N in [1, 2, 3, 4]:
    prefix = f'N{N}_'
    d = {
        'a2_ed': float(naz1[prefix + 'a2_ed']),
        'a2_hfb': float(naz1[prefix + 'a2_hfb']),
        'a2_pbcs': float(naz1[prefix + 'a2_pbcs']),
        'a2_proj': float(naz1[prefix + 'a2_proj']),
        'delta_ed': float(naz1[prefix + 'delta_ed']),
        'delta_hfb': float(naz1[prefix + 'delta_hfb']),
        'delta_proj': float(naz1[prefix + 'delta_proj']),
        'frac_proj_vs_hfb': float(naz1[prefix + 'frac_proj_vs_hfb']),
        'frac_ed_vs_hfb': float(naz1[prefix + 'frac_ed_vs_hfb']),
        'Delta_sq_ed': float(naz1[prefix + 'Delta_sq_ed']),
        'Delta_sq_hfb': float(naz1[prefix + 'Delta_sq_hfb']),
    }
    single_cell_results[N] = d

print(f"\n  Single-cell |a2_PROJ - a2_HFB|/a2_HFB (%):")
print(f"  {'N':>3s} {'PROJ vs HFB':>14s} {'ED vs HFB':>14s}")
for N in [1, 2, 3, 4]:
    d = single_cell_results[N]
    print(f"  {N:3d} {d['frac_proj_vs_hfb']:13.6f}% {d['frac_ed_vs_hfb']:13.6f}%")


# ==============================================================================
#  SECTION 3: Two-Cell Model Construction (Reduced: 2 modes/cell)
# ==============================================================================
#
# For tractability, construct a 2-mode-per-cell model:
#   Cell alpha (alpha=1,2): modes k=1,2 with energies eps_1, eps_2
#   Intra-cell pairing: V_{12}
#   Inter-cell Josephson: E_J * sum_k (c^dag_{k,1} c_{k,2} + h.c.)
#
# The 2-mode model captures B2 (low) and B1 (high) — the two sectors
# most relevant for pairing (B3 is nearly empty).
#
# Fock space: each mode has 2 states (0,1). 2 modes x 2 cells = 4 modes.
# Dim = 2^4 = 16.
#
# Also run the FULL 8-mode-per-cell model for N_pair=1 (tractable).

print(f"\n{'='*72}")
print(f"SECTION 3: Two-Cell Model (2 modes/cell, dim=16)")
print(f"{'='*72}")

# Select 2 representative modes: one B2 and one B1
# B2[0] at eps=0.845 and B1 at eps=0.819 (closest to Fermi surface)
# Use averaged B2 and B1 energies for the reduced model
eps_B2_avg = np.mean(E_sp_8[:4])
eps_B1 = E_sp_8[4]

# Average B2-B2 and B2-B1 pairing matrix elements
V_B2B2_avg = np.mean(V_bare_8[:4, :4])
V_B2B1_avg = np.mean(V_bare_8[:4, 4])
V_B1B1 = V_bare_8[4, 4]  # ~0 (B1-B1 self-interaction)

# Reduced 2-mode single-particle energies
eps_2mode = np.array([eps_B2_avg, eps_B1])
V_2mode = np.array([
    [V_B2B2_avg, V_B2B1_avg],
    [V_B2B1_avg, V_B1B1]
])

print(f"  Reduced model: eps = {eps_2mode}")
print(f"  V_2mode = \n{V_2mode}")
print(f"  E_J = {E_J_fold:.4f} M_KK")


# ==============================================================================
#  SECTION 4: Exact Diagonalization — 1-Cell (2 modes)
# ==============================================================================

def build_fock_basis(n_modes):
    """Build all Fock states for n_modes as binary tuples."""
    dim = 2**n_modes
    states = []
    for i in range(dim):
        occ = tuple((i >> j) & 1 for j in range(n_modes))
        states.append(occ)
    return states

def particle_number(state):
    """Total particle number in a Fock state."""
    return sum(state)

def build_hamiltonian_1cell(eps, V, states):
    """
    Build 1-cell Hamiltonian in Fock space.
    H = sum_k eps_k n_k + sum_{kk'} V_{kk'} c^dag_k c^dag_k' c_k' c_k
      = sum_k eps_k n_k - (1/2) sum_{kk'} V_{kk'} n_k n_k'  [for pair interaction]

    Actually for BCS pairing: H_pair = -sum_{k>k'} V_{kk'} c^dag_k c^dag_k' c_k' c_k
    = -(1/2) sum_{kk', k!=k'} V_{kk'} n_k n_{k'}

    Wait — the actual reduced BCS Hamiltonian for seniority-zero pairing is:
    H = sum_k eps_k n_k - G * P^dag P
    where P^dag = sum_k c^dag_k c^dag_{k_bar} (pair creation)

    For our 2-mode model with general V:
    H = sum_k eps_k * n_k - sum_{kk'} V_{kk'} * (c^dag_k c^dag_{k_bar}) (c_{k'_bar} c_{k'})

    But in the seniority-0 pair space, the pairing acts on PAIRS.
    For the general case with arbitrary occupations, use full Fock space.
    """
    n_modes = len(eps)
    dim = len(states)
    H = np.zeros((dim, dim))

    for i, si in enumerate(states):
        # Diagonal: single-particle energies
        H[i, i] = sum(eps[k] * si[k] for k in range(n_modes))

        # Off-diagonal: pairing scattering V_{kk'} * c^dag_k c^dag_{k'} c_l c_l'
        # For pair transfer: (k,k') -> (l,l') with V_{kl} etc.
        # Use density-density form for diagonal V terms
        for k in range(n_modes):
            for kp in range(n_modes):
                if k != kp:
                    H[i, i] -= 0.5 * V[k, kp] * si[k] * si[kp]

    return H


def build_hamiltonian_1cell_pair(eps, V, states):
    """
    Full pairing Hamiltonian in Fock space with off-diagonal pair scattering.

    H = sum_k eps_k * n_k - sum_{kk'} V_{kk'} * a^dag_k a_{k'}

    where a^dag_k = c^dag_{k,up} c^dag_{k,down} creates a pair in level k.

    For our SPINLESS model (seniority framework), the pair operator is
    between different modes: pair in mode k scatters to mode k'.

    H_pair = -sum_{k!=k'} V_{kk'} * |k><k'|  (pair hopping)
           + sum_k (2*eps_k - V_{kk}) * |k><k|  (pair on-site)

    In the FULL Fock space (not pair space), this is:
    H = sum_k eps_k n_k
      - sum_{k<k'} V_{kk'} [c^dag_k (1-n_{k'}) c_{k'} n_k + h.c.]

    Actually, let me be more careful. The interaction from S52 is derived
    from the KK reduction and acts in the pair channel. The Hamiltonian is:

    H = sum_k eps_k * n_k - sum_{kk'} V_{kk'} * c^dag_k c_{k'}

    where V_{kk'} = <k|V_pair|k'> is the pair scattering matrix element.
    This is a ONE-BODY operator in the space of pairs, but a TWO-BODY
    operator in single-particle space.

    For consistency with NAZ-1 and S52: use the same structure.
    In Fock space of individual modes, pair scattering k -> k' means:
      c^dag_k c_{k'} applied to state with k' occupied and k empty.
    """
    n_modes = len(eps)
    dim = len(states)
    H = np.zeros((dim, dim))

    for i, si in enumerate(states):
        # Diagonal: single-particle energy
        for k in range(n_modes):
            H[i, i] += eps[k] * si[k]

        # Diagonal: pairing self-energy (density-density)
        for k in range(n_modes):
            for kp in range(k+1, n_modes):
                H[i, i] -= V[k, kp] * si[k] * si[kp]

        # Off-diagonal: pair scattering
        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp:
                    continue
                # Scatter pair: destroy at kp, create at k
                # Requires: si[kp]=1, si[k]=0
                if si[kp] == 1 and si[k] == 0:
                    sj = list(si)
                    sj[kp] = 0
                    sj[k] = 1
                    sj = tuple(sj)
                    j = states.index(sj)
                    H[i, j] -= V[k, kp]

    return H


def build_hamiltonian_2cell(eps, V, E_J, states, n_modes_per_cell):
    """
    Build 2-cell Hamiltonian with Josephson coupling.

    H = H_1(cell_1) + H_2(cell_2) + H_J

    where H_J = -E_J * sum_k (c^dag_{k,1} c_{k,2} + h.c.)

    Modes: [cell_1_mode_0, cell_1_mode_1, ..., cell_2_mode_0, cell_2_mode_1, ...]

    eps: (n_modes_per_cell,) — same for both cells
    V: (n_modes_per_cell, n_modes_per_cell) — intra-cell pairing
    """
    M = n_modes_per_cell
    n_total = 2 * M
    dim = len(states)
    H = np.zeros((dim, dim))

    for i, si in enumerate(states):
        # Single-particle energies (both cells have same eps)
        for k in range(M):
            H[i, i] += eps[k] * si[k]         # cell 1
            H[i, i] += eps[k] * si[M + k]     # cell 2

        # Intra-cell pairing: density-density (cell 1)
        for k in range(M):
            for kp in range(k+1, M):
                H[i, i] -= V[k, kp] * si[k] * si[kp]

        # Intra-cell pairing: density-density (cell 2)
        for k in range(M):
            for kp in range(k+1, M):
                H[i, i] -= V[k, kp] * si[M+k] * si[M+kp]

        # Intra-cell pair scattering (cell 1)
        for k in range(M):
            for kp in range(M):
                if k == kp:
                    continue
                if si[kp] == 1 and si[k] == 0:
                    sj = list(si)
                    sj[kp] = 0
                    sj[k] = 1
                    sj = tuple(sj)
                    j = states.index(sj)
                    H[i, j] -= V[k, kp]

        # Intra-cell pair scattering (cell 2)
        for k in range(M):
            for kp in range(M):
                if k == kp:
                    continue
                k2, kp2 = M + k, M + kp
                if si[kp2] == 1 and si[k2] == 0:
                    sj = list(si)
                    sj[kp2] = 0
                    sj[k2] = 1
                    sj = tuple(sj)
                    j = states.index(sj)
                    H[i, j] -= V[k, kp]

        # Josephson coupling: -E_J * sum_k (c^dag_{k,1} c_{k,2} + h.c.)
        for k in range(M):
            k1, k2 = k, M + k
            # Hop from cell 2 to cell 1: c^dag_{k,1} c_{k,2}
            if si[k2] == 1 and si[k1] == 0:
                sj = list(si)
                sj[k2] = 0
                sj[k1] = 1
                sj = tuple(sj)
                j = states.index(sj)
                H[i, j] -= E_J
            # Hop from cell 1 to cell 2: c^dag_{k,2} c_{k,1}
            if si[k1] == 1 and si[k2] == 0:
                sj = list(si)
                sj[k1] = 0
                sj[k2] = 1
                sj = tuple(sj)
                j = states.index(sj)
                H[i, j] -= E_J

    return H


# ==============================================================================
#  SECTION 5: BCS and Fomenko Projection Functions
# ==============================================================================

def solve_bcs(eps, V, N_target, n_modes, max_iter=500, tol=1e-10):
    """
    Self-consistent BCS for n_modes levels at N_target particles.
    Returns v^2 (occupations), Delta_k, mu.
    """
    M = n_modes
    # Initial guess: fill lowest levels
    n_k = np.zeros(M)
    remaining = N_target
    for k in range(M):
        if remaining > 0:
            n_k[k] = min(1.0, remaining)
            remaining -= n_k[k]

    # Add small pairing seed
    n_k = np.clip(n_k, 0.01, 0.99)
    n_k *= N_target / np.sum(n_k)

    for iteration in range(max_iter):
        # BCS amplitudes
        v2 = np.clip(n_k, 1e-12, 1.0 - 1e-12)
        u2 = 1.0 - v2
        uv = np.sqrt(u2 * v2)

        # Gap equation
        Delta_k = -V @ uv

        # Chemical potential from particle number constraint
        mu = np.sum(n_k * eps) / N_target if N_target > 0 else np.mean(eps)

        # Quasiparticle energy
        xi_k = eps - mu
        E_k = np.sqrt(xi_k**2 + Delta_k**2)

        # New occupations
        n_k_new = 0.5 * (1.0 - xi_k / E_k)

        # Fix particle number
        n_k_new = np.clip(n_k_new, 1e-12, 1.0 - 1e-12)
        n_k_new *= N_target / np.sum(n_k_new)

        # Convergence check
        if np.max(np.abs(n_k_new - n_k)) < tol:
            return n_k_new, Delta_k, mu
        n_k = 0.5 * n_k + 0.5 * n_k_new

    return n_k, Delta_k, mu


def fomenko_projection(n_k_bcs, N_target, N_phi=128):
    """
    Exact number projection via Fomenko discretization.
    Returns projected occupations, pairing tensor, normalization, <(DN)^2>.
    """
    M = len(n_k_bcs)
    v2 = np.clip(n_k_bcs, 1e-15, 1.0 - 1e-15)
    u2 = 1.0 - v2

    phi_arr = np.linspace(0, 2*PI, N_phi, endpoint=False)
    dphi = 2*PI / N_phi

    norm = 0.0 + 0j  # (local)
    n_k_proj = np.zeros(M, dtype=complex)
    kappa_proj = np.zeros(M, dtype=complex)

    for phi in phi_arr:
        e2iphi = np.exp(2j * phi)
        zk = u2 + v2 * e2iphi
        log_overlap = np.sum(np.log(zk))
        overlap = np.exp(log_overlap)
        phase = np.exp(-1j * N_target * phi)
        w = phase * overlap * dphi / (2*PI)

        norm += w
        for k in range(M):
            n_k_proj[k] += w * v2[k] * e2iphi / zk[k]
            kappa_proj[k] += w * np.sqrt(u2[k] * v2[k]) * np.exp(1j*phi) / zk[k]

    n_k_pbcs = np.real(n_k_proj / norm)
    kappa_pbcs = np.abs(kappa_proj / norm)
    dN2 = 4.0 * np.sum(n_k_pbcs * (1.0 - n_k_pbcs))

    return n_k_pbcs, kappa_pbcs, float(np.real(norm)), dN2


def compute_a2_proxy(n_k, V, R_fold, a2_geom, a0_geom):
    """
    Compute the a_2-proxy: geometric part + pairing correction.

    a_2 = a_2^{geom} + a_0^{geom} * |Delta_eff|^2
    where |Delta_eff|^2 = mean_k(Delta_k^2) and
    Delta_k = -sum_k' V_{kk'} * sqrt(n_k'*(1-n_k'))

    Alternatively: delta = 12 * |Delta_eff|^2 / (5*R)
    a_2 = a_2^{geom} * (1 + delta)
    """
    uv = np.sqrt(np.clip(n_k * (1.0 - n_k), 0, None))
    Delta_k = -V @ uv
    Delta_sq = np.mean(Delta_k**2)
    delta = 12.0 * Delta_sq / (5.0 * R_fold)
    a2 = a2_geom * (1.0 + delta)
    return a2, delta, Delta_sq


# ==============================================================================
#  SECTION 6: 1-Cell Reduced Model (2 modes, dim=4)
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 6: 1-Cell Reduced Model (2 modes)")
print(f"{'='*72}")

states_1cell_2m = build_fock_basis(2)
print(f"  Fock space dimension: {len(states_1cell_2m)}")

H_1cell_2m = build_hamiltonian_1cell_pair(eps_2mode, V_2mode, states_1cell_2m)

# Solve for N=1
evals_1c, evecs_1c = eigh(H_1cell_2m)

# N-sector decomposition
for N_target in [1, 2]:
    N_states = [i for i, s in enumerate(states_1cell_2m) if particle_number(s) == N_target]
    if not N_states:
        continue

    # Project Hamiltonian to N sector
    P = np.zeros((len(N_states), len(states_1cell_2m)))
    for idx, i in enumerate(N_states):
        P[idx, i] = 1.0
    H_N = P @ H_1cell_2m @ P.T

    evals_N, evecs_N = eigh(H_N)
    E_gs = evals_N[0]
    psi_gs = evecs_N[:, 0]

    # Extract occupations from ground state
    n_k_ed = np.zeros(2)
    for idx, i in enumerate(N_states):
        prob = psi_gs[idx]**2
        for k in range(2):
            n_k_ed[k] += states_1cell_2m[i][k] * prob

    # BCS solution
    n_k_bcs, Delta_bcs, mu_bcs = solve_bcs(eps_2mode, V_2mode, N_target, 2)

    # Fomenko projection
    n_k_pbcs, kappa_pbcs, norm_pbcs, dN2_pbcs = fomenko_projection(n_k_bcs, N_target)

    # a_2 proxies
    a2_ed, delta_ed, Dsq_ed = compute_a2_proxy(n_k_ed, V_2mode, R_fold, a2_geom, a0_geom)
    a2_bcs, delta_bcs, Dsq_bcs = compute_a2_proxy(n_k_bcs, V_2mode, R_fold, a2_geom, a0_geom)
    a2_pbcs, delta_pbcs, Dsq_pbcs = compute_a2_proxy(n_k_pbcs, V_2mode, R_fold, a2_geom, a0_geom)

    frac_proj_bcs = abs(a2_pbcs - a2_bcs) / a2_bcs * 100
    frac_ed_bcs = abs(a2_ed - a2_bcs) / a2_bcs * 100

    print(f"\n  N={N_target} (1-cell, 2-mode):")
    print(f"    E_gs(ED) = {E_gs:.8f}")
    print(f"    n_k(ED) = {n_k_ed}")
    print(f"    n_k(BCS) = {n_k_bcs}")
    print(f"    n_k(PBCS) = {n_k_pbcs}")
    print(f"    |Delta|^2: ED={Dsq_ed:.8f}, BCS={Dsq_bcs:.8f}, PBCS={Dsq_pbcs:.8f}")
    print(f"    delta: ED={delta_ed:.8f}, BCS={delta_bcs:.8f}, PBCS={delta_pbcs:.8f}")
    print(f"    |a2_PBCS-a2_BCS|/a2_BCS = {frac_proj_bcs:.6f}%")
    print(f"    |a2_ED-a2_BCS|/a2_BCS = {frac_ed_bcs:.6f}%")
    print(f"    <(DN)^2>_PBCS = {dN2_pbcs:.6f}")


# ==============================================================================
#  SECTION 7: 2-Cell Reduced Model (2 modes/cell, 4 total, dim=16)
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 7: 2-Cell Reduced Model (2 modes/cell, dim=16)")
print(f"{'='*72}")

states_2cell_2m = build_fock_basis(4)
print(f"  Fock space dimension: {len(states_2cell_2m)}")

H_2cell_2m = build_hamiltonian_2cell(eps_2mode, V_2mode, E_J_fold, states_2cell_2m, 2)

# Symmetry check
print(f"  H symmetric: {np.allclose(H_2cell_2m, H_2cell_2m.T)}")
print(f"  ||H-H^T|| = {np.linalg.norm(H_2cell_2m - H_2cell_2m.T):.2e}")

# Solve per N-sector
fabric_2m_results = {}
for N_target in [1, 2, 3, 4]:
    N_states = [i for i, s in enumerate(states_2cell_2m) if particle_number(s) == N_target]
    if not N_states:
        continue

    P = np.zeros((len(N_states), len(states_2cell_2m)))
    for idx, i in enumerate(N_states):
        P[idx, i] = 1.0
    H_N = P @ H_2cell_2m @ P.T

    evals_N, evecs_N = eigh(H_N)
    E_gs = evals_N[0]
    gap = evals_N[1] - evals_N[0] if len(evals_N) > 1 else 0.0
    psi_gs = evecs_N[:, 0]

    # Extract occupations (4 modes: cell1_mode0, cell1_mode1, cell2_mode0, cell2_mode1)
    n_k_ed = np.zeros(4)
    for idx, i in enumerate(N_states):
        prob = psi_gs[idx]**2
        for k in range(4):
            n_k_ed[k] += states_2cell_2m[i][k] * prob

    # For a_2 proxy on the 2-cell fabric, we need the effective V for the full system.
    # The fabric V has same intra-cell V in each cell, plus the Josephson contributes
    # to delocalization but NOT to the pairing gap (it's single-particle hopping).
    # The pairing correction depends on the effective gap from intra-cell V
    # as seen by the delocalized (fabric) quasiparticles.

    # Construct fabric V (block diagonal in pairing, full in sp)
    V_fabric_4 = np.zeros((4, 4))
    V_fabric_4[0:2, 0:2] = V_2mode  # cell 1
    V_fabric_4[2:4, 2:4] = V_2mode  # cell 2

    eps_fabric_4 = np.array([eps_2mode[0], eps_2mode[1], eps_2mode[0], eps_2mode[1]])

    # BCS on the 4-mode system
    n_k_bcs, Delta_bcs, mu_bcs = solve_bcs(eps_fabric_4, V_fabric_4, N_target, 4)

    # Fomenko projection on the 4-mode BCS
    n_k_pbcs, kappa_pbcs, norm_pbcs, dN2_pbcs = fomenko_projection(n_k_bcs, N_target)

    # a_2 proxies
    a2_ed_f, delta_ed_f, Dsq_ed_f = compute_a2_proxy(n_k_ed, V_fabric_4, R_fold, a2_geom, a0_geom)
    a2_bcs_f, delta_bcs_f, Dsq_bcs_f = compute_a2_proxy(n_k_bcs, V_fabric_4, R_fold, a2_geom, a0_geom)
    a2_pbcs_f, delta_pbcs_f, Dsq_pbcs_f = compute_a2_proxy(n_k_pbcs, V_fabric_4, R_fold, a2_geom, a0_geom)

    frac_proj_bcs_f = abs(a2_pbcs_f - a2_bcs_f) / a2_bcs_f * 100
    frac_ed_bcs_f = abs(a2_ed_f - a2_bcs_f) / a2_bcs_f * 100

    fabric_2m_results[N_target] = {
        'E_gs': E_gs, 'gap': gap,
        'n_k_ed': n_k_ed, 'n_k_bcs': n_k_bcs, 'n_k_pbcs': n_k_pbcs,
        'a2_ed': a2_ed_f, 'a2_bcs': a2_bcs_f, 'a2_pbcs': a2_pbcs_f,
        'delta_ed': delta_ed_f, 'delta_bcs': delta_bcs_f, 'delta_pbcs': delta_pbcs_f,
        'Dsq_ed': Dsq_ed_f, 'Dsq_bcs': Dsq_bcs_f, 'Dsq_pbcs': Dsq_pbcs_f,
        'frac_proj_bcs': frac_proj_bcs_f, 'frac_ed_bcs': frac_ed_bcs_f,
        'dN2_pbcs': dN2_pbcs,
        'dim_N': len(N_states),
    }

    print(f"\n  N={N_target} (2-cell, 2-mode/cell):")
    print(f"    dim(N-sector) = {len(N_states)}")
    print(f"    E_gs(ED) = {E_gs:.8f}, gap = {gap:.6f}")
    print(f"    n_k(ED) = {n_k_ed}")
    print(f"    n_k(BCS) = {n_k_bcs}")
    print(f"    n_k(PBCS) = {n_k_pbcs}")
    print(f"    |Delta|^2: ED={Dsq_ed_f:.8f}, BCS={Dsq_bcs_f:.8f}, PBCS={Dsq_pbcs_f:.8f}")
    print(f"    delta: ED={delta_ed_f:.8f}, BCS={delta_bcs_f:.8f}, PBCS={delta_pbcs_f:.8f}")
    print(f"    |a2_PBCS-a2_BCS|/a2_BCS = {frac_proj_bcs_f:.6f}%")
    print(f"    |a2_ED-a2_BCS|/a2_BCS = {frac_ed_bcs_f:.6f}%")
    print(f"    <(DN)^2>_PBCS = {dN2_pbcs:.6f}")


# ==============================================================================
#  SECTION 8: Full 8-Mode Per Cell Model (N_pair=1, tractable)
# ==============================================================================
#
# For 8 modes/cell, 2 cells: 16 modes total.
# Full Fock space: 2^16 = 65536 — large but feasible.
# However, we only need the N-particle sector.
# N=1: C(16,1) = 16 states (trivial)
# N=2: C(16,2) = 120 states (same as S60 RG computation)
# N=3: C(16,3) = 560 states
# N=4: C(16,4) = 1820 states
#
# For the gate: compute N=1 and N=2 (matches NAZ-1).

print(f"\n{'='*72}")
print(f"SECTION 8: Full 8-Mode Per Cell Model (16 modes, ED)")
print(f"{'='*72}")

def build_N_sector_basis(n_total, N_target):
    """Build basis states for the N-particle sector using combinations."""
    if N_target == 0:
        return [tuple(0 for _ in range(n_total))]
    if N_target > n_total:
        return []

    basis = []
    for occupied in combinations(range(n_total), N_target):
        state = [0] * n_total
        for k in occupied:
            state[k] = 1
        basis.append(tuple(state))
    return basis


def build_hamiltonian_2cell_Nsector(eps_per_cell, V_per_cell, E_J, N_target, n_modes_per_cell):
    """
    Build 2-cell Hamiltonian directly in the N-particle sector.
    Uses combinations-based basis for memory efficiency.
    """
    M = n_modes_per_cell
    n_total = 2 * M
    basis = build_N_sector_basis(n_total, N_target)
    dim = len(basis)
    basis_dict = {s: i for i, s in enumerate(basis)}

    print(f"    Building H for N={N_target}: dim={dim}, n_modes={n_total}")

    H = np.zeros((dim, dim))

    for i, si in enumerate(basis):
        # Diagonal: sp energies
        for k in range(M):
            H[i, i] += eps_per_cell[k] * si[k]         # cell 1
            H[i, i] += eps_per_cell[k] * si[M + k]     # cell 2

        # Diagonal: intra-cell density-density (cell 1)
        for k in range(M):
            for kp in range(k+1, M):
                H[i, i] -= V_per_cell[k, kp] * si[k] * si[kp]

        # Diagonal: intra-cell density-density (cell 2)
        for k in range(M):
            for kp in range(k+1, M):
                H[i, i] -= V_per_cell[k, kp] * si[M+k] * si[M+kp]

        # Off-diagonal: intra-cell pair scattering (cell 1)
        for k in range(M):
            for kp in range(M):
                if k == kp:
                    continue
                if si[kp] == 1 and si[k] == 0:
                    sj = list(si)
                    sj[kp] = 0
                    sj[k] = 1
                    sj = tuple(sj)
                    j = basis_dict.get(sj, -1)
                    if j >= 0:
                        H[i, j] -= V_per_cell[k, kp]

        # Off-diagonal: intra-cell pair scattering (cell 2)
        for k in range(M):
            for kp in range(M):
                if k == kp:
                    continue
                k2, kp2 = M + k, M + kp
                if si[kp2] == 1 and si[k2] == 0:
                    sj = list(si)
                    sj[kp2] = 0
                    sj[k2] = 1
                    sj = tuple(sj)
                    j = basis_dict.get(sj, -1)
                    if j >= 0:
                        H[i, j] -= V_per_cell[k, kp]

        # Josephson: -E_J * sum_k (c^dag_{k,1} c_{k,2} + h.c.)
        for k in range(M):
            k1, k2 = k, M + k
            if si[k2] == 1 and si[k1] == 0:
                sj = list(si)
                sj[k2] = 0
                sj[k1] = 1
                sj = tuple(sj)
                j = basis_dict.get(sj, -1)
                if j >= 0:
                    H[i, j] -= E_J
            if si[k1] == 1 and si[k2] == 0:
                sj = list(si)
                sj[k1] = 0
                sj[k2] = 1
                sj = tuple(sj)
                j = basis_dict.get(sj, -1)
                if j >= 0:
                    H[i, j] -= E_J

    return H, basis


# Full 8-mode per cell computation
fabric_8m_results = {}
M_full = 8

# Use E_sp from S52 as the per-cell sp energies, V from S52 as intra-cell V
eps_full = E_sp_8  # 8 single-particle energies

for N_target in [1, 2, 3]:
    H_N, basis_N = build_hamiltonian_2cell_Nsector(
        eps_full, V_bare_8, E_J_fold, N_target, M_full
    )

    # Symmetry check
    sym_err = np.linalg.norm(H_N - H_N.T)
    print(f"    ||H-H^T|| = {sym_err:.2e}")

    evals_N, evecs_N = eigh(H_N)
    E_gs = evals_N[0]
    gap = evals_N[1] - evals_N[0] if len(evals_N) > 1 else 0.0
    psi_gs = evecs_N[:, 0]

    # Extract occupations (16 modes)
    n_total = 2 * M_full
    n_k_ed = np.zeros(n_total)
    for idx, si in enumerate(basis_N):
        prob = psi_gs[idx]**2
        for k in range(n_total):
            n_k_ed[k] += si[k] * prob

    # Fabric V: block diagonal
    V_fabric_16 = np.zeros((n_total, n_total))
    V_fabric_16[:M_full, :M_full] = V_bare_8
    V_fabric_16[M_full:, M_full:] = V_bare_8

    eps_fabric_16 = np.concatenate([eps_full, eps_full])

    # BCS on 16-mode system
    n_k_bcs, Delta_bcs, mu_bcs = solve_bcs(eps_fabric_16, V_fabric_16, N_target, n_total)

    # Fomenko projection on 16-mode BCS
    n_k_pbcs, kappa_pbcs, norm_pbcs, dN2_pbcs = fomenko_projection(n_k_bcs, N_target, N_phi=128)

    # a_2 proxies
    a2_ed_f, delta_ed_f, Dsq_ed_f = compute_a2_proxy(n_k_ed, V_fabric_16, R_fold, a2_geom, a0_geom)
    a2_bcs_f, delta_bcs_f, Dsq_bcs_f = compute_a2_proxy(n_k_bcs, V_fabric_16, R_fold, a2_geom, a0_geom)
    a2_pbcs_f, delta_pbcs_f, Dsq_pbcs_f = compute_a2_proxy(n_k_pbcs, V_fabric_16, R_fold, a2_geom, a0_geom)

    frac_proj_bcs_f = abs(a2_pbcs_f - a2_bcs_f) / a2_bcs_f * 100
    frac_ed_bcs_f = abs(a2_ed_f - a2_bcs_f) / a2_bcs_f * 100

    fabric_8m_results[N_target] = {
        'E_gs': E_gs, 'gap': gap,
        'n_k_ed': n_k_ed, 'n_k_bcs': n_k_bcs, 'n_k_pbcs': n_k_pbcs,
        'a2_ed': a2_ed_f, 'a2_bcs': a2_bcs_f, 'a2_pbcs': a2_pbcs_f,
        'delta_ed': delta_ed_f, 'delta_bcs': delta_bcs_f, 'delta_pbcs': delta_pbcs_f,
        'Dsq_ed': Dsq_ed_f, 'Dsq_bcs': Dsq_bcs_f, 'Dsq_pbcs': Dsq_pbcs_f,
        'frac_proj_bcs': frac_proj_bcs_f, 'frac_ed_bcs': frac_ed_bcs_f,
        'dN2_pbcs': dN2_pbcs,
        'dim_N': len(basis_N),
    }

    print(f"\n  N={N_target} (2-cell, 8-mode/cell, dim={len(basis_N)}):")
    print(f"    E_gs(ED) = {E_gs:.8f}, gap = {gap:.6f}")
    print(f"    n_k(ED, cell1) = {n_k_ed[:M_full]}")
    print(f"    n_k(ED, cell2) = {n_k_ed[M_full:]}")
    print(f"    Sum n_k = {np.sum(n_k_ed):.6f} (should be {N_target})")
    print(f"    |Delta|^2: ED={Dsq_ed_f:.8f}, BCS={Dsq_bcs_f:.8f}, PBCS={Dsq_pbcs_f:.8f}")
    print(f"    delta: ED={delta_ed_f:.8f}, BCS={delta_bcs_f:.8f}, PBCS={delta_pbcs_f:.8f}")
    print(f"    |a2_PBCS-a2_BCS|/a2_BCS = {frac_proj_bcs_f:.6f}%")
    print(f"    |a2_ED-a2_BCS|/a2_BCS   = {frac_ed_bcs_f:.6f}%")
    print(f"    <(DN)^2>_PBCS = {dN2_pbcs:.6f}")


# ==============================================================================
#  SECTION 9: Comparison — Single Cell vs Fabric
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 9: Single Cell vs Fabric Comparison")
print(f"{'='*72}")

print(f"\n  GATE COMPARISON: |a2_PBCS - a2_BCS|/a2_BCS (%)")
print(f"  {'N':>3s} {'1-cell (NAZ-1)':>16s} {'2-cell 2m':>14s} {'2-cell 8m':>14s} {'Ratio(2c8m/1c)':>16s}")

gate_ratios = {}
for N in [1, 2]:
    sc = single_cell_results[N]['frac_proj_vs_hfb']  # NAZ-1 single-cell
    fc_2m = fabric_2m_results.get(N, {}).get('frac_proj_bcs', float('nan'))
    fc_8m = fabric_8m_results.get(N, {}).get('frac_proj_bcs', float('nan'))

    ratio_2m = fc_2m / sc if sc > 0 else float('nan')
    ratio_8m = fc_8m / sc if sc > 0 else float('nan')

    gate_ratios[N] = {
        'single_cell': sc,
        'fabric_2m': fc_2m,
        'fabric_8m': fc_8m,
        'ratio_2m': ratio_2m,
        'ratio_8m': ratio_8m,
    }

    print(f"  {N:3d} {sc:15.6f}% {fc_2m:13.6f}% {fc_8m:13.6f}% {ratio_8m:15.4f}")

# Also show N=3 (fabric only)
if 3 in fabric_8m_results:
    fc_8m_3 = fabric_8m_results[3]['frac_proj_bcs']
    sc_3 = single_cell_results[3]['frac_proj_vs_hfb']
    ratio_3 = fc_8m_3 / sc_3 if sc_3 > 0 else float('nan')
    gate_ratios[3] = {
        'single_cell': sc_3,
        'fabric_8m': fc_8m_3,
        'ratio_8m': ratio_3,
    }
    print(f"  {3:3d} {sc_3:15.6f}%  {'':>13s} {fc_8m_3:13.6f}% {ratio_3:15.4f}")


# ==============================================================================
#  SECTION 10: Particle-Number Fluctuation Scaling
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 10: Particle-Number Fluctuation Scaling")
print(f"{'='*72}")

print(f"\n  <(Delta N)^2> / N  (diagnostic for finite-size projection effects)")
print(f"  {'N':>3s} {'1-cell (HFB)':>14s} {'2-cell BCS':>14s} {'Ratio':>10s}")

for N in [1, 2]:
    # Single cell
    n_hfb = s52[f'N{N}_n_k_hfb']
    dN2_1c = 4.0 * np.sum(n_hfb * (1.0 - n_hfb))

    # Fabric
    n_bcs_f = fabric_8m_results[N]['n_k_bcs']
    dN2_2c = 4.0 * np.sum(n_bcs_f * (1.0 - n_bcs_f))

    print(f"  {N:3d} {dN2_1c/N:13.6f} {dN2_2c/N:13.6f} {(dN2_2c/N)/(dN2_1c/N):9.4f}")

if 3 in fabric_8m_results:
    n_hfb_3 = s52['N3_n_k_hfb']
    dN2_1c_3 = 4.0 * np.sum(n_hfb_3 * (1.0 - n_hfb_3))
    n_bcs_f3 = fabric_8m_results[3]['n_k_bcs']
    dN2_2c_3 = 4.0 * np.sum(n_bcs_f3 * (1.0 - n_bcs_f3))
    print(f"  {3:3d} {dN2_1c_3/3:13.6f} {dN2_2c_3/3:13.6f} {(dN2_2c_3/3)/(dN2_1c_3/3):9.4f}")


# ==============================================================================
#  SECTION 11: Nuclear Physics Analysis
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 11: Nuclear Physics Analysis")
print(f"{'='*72}")

print(f"\n  Nuclear scaling of PBCS correction:")
print(f"  Papers 02, 03, 17 establish: delta_PBCS ~ 1/sqrt(N_modes) for pairing energy")
print(f"  For a_2 correction: delta ~ |Delta_eff|^2 / R, depends on pairing tensor")
print(f"")
print(f"  1-cell: N_modes = 8 (= sd-shell ^18O-^24Mg)")
print(f"  2-cell: N_modes = 16 (= sdpf-shell ^36Ar-^40Ca)")
print(f"  Expected scaling: delta(2c)/delta(1c) ~ sqrt(8/16) = 0.707")
print(f"")

if 2 in gate_ratios:
    r = gate_ratios[2]
    print(f"  Observed ratio at N=2: {r.get('ratio_8m', float('nan')):.4f}")
    print(f"  Expected 1/sqrt(N): 0.707")


# ==============================================================================
#  SECTION 12: Gate Verdict
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 12: GATE VERDICT — PBCS-FABRIC-61")
print(f"{'='*72}")

# Use N=2 as the primary comparison (physical pair sector)
# and the 8-mode-per-cell model (most realistic)
if 2 in gate_ratios:
    ratio_primary = gate_ratios[2].get('ratio_8m', float('nan'))
    sc_val = gate_ratios[2]['single_cell']
    fc_val = gate_ratios[2].get('fabric_8m', float('nan'))
else:
    ratio_primary = float('nan')
    sc_val = float('nan')
    fc_val = float('nan')

print(f"\n  Primary comparison (N=2, 8-mode/cell):")
print(f"    1-cell: |a2_PROJ - a2_BCS|/a2_BCS = {sc_val:.6f}%")
print(f"    2-cell: |a2_PBCS - a2_BCS|/a2_BCS = {fc_val:.6f}%")
print(f"    Ratio: {ratio_primary:.6f}")

if np.isnan(ratio_primary):
    verdict = "INFO"
    detail = "Unable to compute ratio (NaN)"
elif ratio_primary < 1.0:
    # Correction DECREASES with fabric size
    decrease_pct = (1.0 - ratio_primary) * 100
    if decrease_pct < 10.0:
        verdict = "INFO"
        detail = f"Ratio={ratio_primary:.4f}, decrease {decrease_pct:.1f}% (<10% change threshold)"
    else:
        verdict = "PASS"
        detail = f"Ratio={ratio_primary:.4f}, correction DECREASES by {decrease_pct:.1f}%"
elif ratio_primary > 1.0:
    increase_pct = (ratio_primary - 1.0) * 100
    if increase_pct < 10.0:
        verdict = "INFO"
        detail = f"Ratio={ratio_primary:.4f}, increase {increase_pct:.1f}% (<10% change threshold)"
    else:
        verdict = "FAIL"
        detail = f"Ratio={ratio_primary:.4f}, correction INCREASES by {increase_pct:.1f}%"
else:
    verdict = "INFO"
    detail = "Ratio exactly 1.0"

print(f"\n  *** PBCS-FABRIC-61: {verdict} ***")
print(f"  {detail}")
print(f"")

# Cross-check with other N values
print(f"  Cross-checks:")
for N in sorted(gate_ratios.keys()):
    r = gate_ratios[N]
    ratio = r.get('ratio_8m', r.get('ratio_2m', float('nan')))
    fc = r.get('fabric_8m', r.get('fabric_2m', float('nan')))
    sc = r['single_cell']
    direction = "DECREASES" if ratio < 1.0 else "INCREASES"
    print(f"    N={N}: ratio={ratio:.4f} ({direction}), 1c={sc:.6f}% -> 2c={fc:.6f}%")


# ==============================================================================
#  SECTION 13: Thermodynamic Limit Extrapolation
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 13: Thermodynamic Limit Extrapolation")
print(f"{'='*72}")

print(f"\n  If delta_a2 ~ 1/sqrt(N_cells) (nuclear scaling, Paper 03):")
print(f"  N_cells=1:  delta_a2 = {sc_val:.6f}%")
if not np.isnan(fc_val):
    # Fit power law: delta = A * N_cells^{-alpha}
    # Two points: (1, sc_val) and (2, fc_val)
    if sc_val > 0 and fc_val > 0:
        alpha_fit = -np.log(fc_val / sc_val) / np.log(2)
        A_fit = sc_val  # at N_cells=1
        print(f"  N_cells=2:  delta_a2 = {fc_val:.6f}%")
        print(f"  Fitted: delta_a2 ~ {A_fit:.4f}% * N_cells^{{-{alpha_fit:.3f}}}")
        print(f"")
        print(f"  Extrapolations:")
        for Nc in [4, 8, 16, 32]:
            delta_extrap = A_fit * Nc**(-alpha_fit)
            print(f"    N_cells={Nc:3d}: delta_a2 ~ {delta_extrap:.6f}%")
        delta_32 = A_fit * 32**(-alpha_fit)
        print(f"")
        print(f"  At physical fabric (N_cells=32): delta_a2 ~ {delta_32:.6f}%")
        print(f"  This is {'NEGLIGIBLE' if delta_32 < 0.01 else 'SMALL' if delta_32 < 0.1 else 'SIGNIFICANT'} "
              f"compared to other theoretical uncertainties (~1-5%).")
    else:
        alpha_fit = float('nan')
else:
    alpha_fit = float('nan')


# ==============================================================================
#  SECTION 14: Save Results
# ==============================================================================

print(f"\n{'='*72}")
print(f"SECTION 14: Saving Results")
print(f"{'='*72}")

save_dict = {
    'gate_name': 'PBCS-FABRIC-61',
    'gate_verdict': verdict,
    'gate_detail': detail,

    # Single-cell reference
    'single_cell_frac_N1': single_cell_results[1]['frac_proj_vs_hfb'],
    'single_cell_frac_N2': single_cell_results[2]['frac_proj_vs_hfb'],
    'single_cell_frac_N3': single_cell_results[3]['frac_proj_vs_hfb'],
    'single_cell_frac_N4': single_cell_results[4]['frac_proj_vs_hfb'],

    # 2-mode fabric results
    'fabric_2m_E_J': E_J_fold,
}
for N in fabric_2m_results:
    prefix = f'fabric_2m_N{N}_'
    r = fabric_2m_results[N]
    save_dict[prefix + 'E_gs'] = r['E_gs']
    save_dict[prefix + 'gap'] = r['gap']
    save_dict[prefix + 'frac_proj_bcs'] = r['frac_proj_bcs']
    save_dict[prefix + 'frac_ed_bcs'] = r['frac_ed_bcs']
    save_dict[prefix + 'delta_bcs'] = r['delta_bcs']
    save_dict[prefix + 'delta_pbcs'] = r['delta_pbcs']
    save_dict[prefix + 'delta_ed'] = r['delta_ed']
    save_dict[prefix + 'dN2_pbcs'] = r['dN2_pbcs']
    save_dict[prefix + 'n_k_ed'] = r['n_k_ed']
    save_dict[prefix + 'n_k_bcs'] = r['n_k_bcs']
    save_dict[prefix + 'n_k_pbcs'] = r['n_k_pbcs']

# 8-mode fabric results
for N in fabric_8m_results:
    prefix = f'fabric_8m_N{N}_'
    r = fabric_8m_results[N]
    save_dict[prefix + 'E_gs'] = r['E_gs']
    save_dict[prefix + 'gap'] = r['gap']
    save_dict[prefix + 'frac_proj_bcs'] = r['frac_proj_bcs']
    save_dict[prefix + 'frac_ed_bcs'] = r['frac_ed_bcs']
    save_dict[prefix + 'delta_bcs'] = r['delta_bcs']
    save_dict[prefix + 'delta_pbcs'] = r['delta_pbcs']
    save_dict[prefix + 'delta_ed'] = r['delta_ed']
    save_dict[prefix + 'dN2_pbcs'] = r['dN2_pbcs']
    save_dict[prefix + 'n_k_ed'] = r['n_k_ed']
    save_dict[prefix + 'n_k_bcs'] = r['n_k_bcs']
    save_dict[prefix + 'n_k_pbcs'] = r['n_k_pbcs']

# Gate ratios
for N in gate_ratios:
    prefix = f'gate_ratio_N{N}_'
    r = gate_ratios[N]
    save_dict[prefix + 'single_cell'] = r['single_cell']
    if 'fabric_8m' in r:
        save_dict[prefix + 'fabric_8m'] = r['fabric_8m']
    if 'ratio_8m' in r:
        save_dict[prefix + 'ratio_8m'] = r['ratio_8m']
    if 'fabric_2m' in r:
        save_dict[prefix + 'fabric_2m'] = r['fabric_2m']
    if 'ratio_2m' in r:
        save_dict[prefix + 'ratio_2m'] = r['ratio_2m']

# Scaling exponent
if not np.isnan(alpha_fit):
    save_dict['alpha_fit'] = alpha_fit

np.savez('s61_pbcs_fabric.npz', **save_dict)
print(f"  Saved: s61_pbcs_fabric.npz")


# ==============================================================================
#  SECTION 15: Summary Figure
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('PBCS-FABRIC-61: PBCS Correction Scaling with Fabric Size', fontsize=14)

# Panel 1: delta_a2 vs N for different models
ax1 = axes[0, 0]
N_vals = [1, 2, 3, 4]
sc_fracs = [single_cell_results[N]['frac_proj_vs_hfb'] for N in N_vals]
ax1.plot(N_vals, sc_fracs, 'bo-', label='1-cell (8 modes, NAZ-1)', markersize=8)

fc_2m_fracs = [fabric_2m_results.get(N, {}).get('frac_proj_bcs', float('nan')) for N in N_vals]
ax1.plot(N_vals, fc_2m_fracs, 'rs-', label='2-cell (2 modes/cell)', markersize=8)

fc_8m_fracs = [fabric_8m_results.get(N, {}).get('frac_proj_bcs', float('nan')) for N in [1, 2, 3]]
ax1.plot([1, 2, 3], fc_8m_fracs, 'g^-', label='2-cell (8 modes/cell)', markersize=8)

ax1.set_xlabel('N (particle number)')
ax1.set_ylabel('|a2_PBCS - a2_BCS| / a2_BCS (%)')
ax1.set_title('Projection Correction vs Particle Number')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Panel 2: Ratio (2-cell/1-cell) vs N
ax2 = axes[0, 1]
ratios_8m = []
N_rat = []
for N in [1, 2, 3]:
    if N in gate_ratios and 'ratio_8m' in gate_ratios[N]:
        ratios_8m.append(gate_ratios[N]['ratio_8m'])
        N_rat.append(N)
ax2.bar(N_rat, ratios_8m, color=['green' if r < 1 else 'red' for r in ratios_8m], alpha=0.7)
ax2.axhline(y=1.0, color='k', linestyle='--', label='No change')
ax2.axhline(y=0.707, color='gray', linestyle=':', label='1/sqrt(2) expected')
ax2.set_xlabel('N (particle number)')
ax2.set_ylabel('Ratio: delta_a2(2-cell) / delta_a2(1-cell)')
ax2.set_title('Scaling Ratio (< 1 = correction decreases)')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Panel 3: Extrapolation to N_cells=32
ax3 = axes[1, 0]
if not np.isnan(alpha_fit):
    Nc_arr = np.linspace(1, 32, 100)
    delta_arr = A_fit * Nc_arr**(-alpha_fit)
    ax3.plot(Nc_arr, delta_arr, 'b-', label=f'Fit: $\\delta \\propto N_c^{{-{alpha_fit:.2f}}}$')
    ax3.plot(1, sc_val, 'bo', markersize=10, label='1-cell (computed)')
    ax3.plot(2, fc_val, 'g^', markersize=10, label='2-cell (computed)')
    ax3.axvline(x=32, color='r', linestyle='--', alpha=0.5, label='Physical fabric (N=32)')
    ax3.set_xlabel('N_cells')
    ax3.set_ylabel('|a2_PBCS - a2_BCS| / a2_BCS (%)')
    ax3.set_title('Thermodynamic Limit Extrapolation')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
else:
    ax3.text(0.5, 0.5, 'Extrapolation not available', ha='center', va='center',
             transform=ax3.transAxes)

# Panel 4: Occupation comparison (N=2, 8-mode, ED)
ax4 = axes[1, 1]
if 2 in fabric_8m_results:
    n_ed = fabric_8m_results[2]['n_k_ed']
    n_bcs = fabric_8m_results[2]['n_k_bcs']
    n_pbcs = fabric_8m_results[2]['n_k_pbcs']
    x = np.arange(len(n_ed))
    w = 0.25  # (local)
    ax4.bar(x - w, n_ed, w, label='ED', color='blue', alpha=0.7)
    ax4.bar(x, n_bcs, w, label='BCS', color='red', alpha=0.7)
    ax4.bar(x + w, n_pbcs, w, label='PBCS', color='green', alpha=0.7)
    ax4.set_xlabel('Mode index (8+8)')
    ax4.set_ylabel('Occupation n_k')
    ax4.set_title('N=2, 2-cell (8 modes/cell)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('s61_pbcs_fabric.png', dpi=150, bbox_inches='tight')
print(f"  Saved: s61_pbcs_fabric.png")

print(f"\n{'='*72}")
print(f"COMPUTATION COMPLETE")
print(f"{'='*72}")
