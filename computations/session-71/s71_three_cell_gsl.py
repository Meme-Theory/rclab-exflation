#!/usr/bin/env python3
"""
THREE-CELL-GSL-71 — Generalized Second Law on 3-Cell Ring
==========================================================

Gate: THREE-CELL-GSL-71
Pre-registered criterion: PASS if S_gen monotonically non-decreasing at
    ALL 4 stages. FAIL if S_gen decreases at any stage. INFO if S_gen
    monotone for 3/4 stages.

Physics:
    The GSL states S_gen = S_a2 + S_matter is non-decreasing.
    S_a2: spectral entropy from the a_2 Seeley-DeWitt coefficient.
    S_matter: BCS condensate entropy from quasiparticle excitations.

    The 3-cell ring introduces FRUSTRATION: the BCS phases at 120-degree
    separation on an odd ring cannot simultaneously minimize all
    junction energies.

    KEY PHYSICAL INSIGHT (from S64): The transit is a UNITARY Bogoliubov
    transformation. The total state is PURE at all times. The physical
    entropy trajectory tracks the PHYSICAL entropy — which is zero for
    the pure state and only becomes nonzero after decoherence/relaxation.

    Stage 1: S_matter = 0. Pure BCS ground state. Frustration determines
             the phase pattern (120-degree separation) but does NOT break
             pairs or create entropy. The BCS ground state with frustrated
             phases is still a definite quantum state — pure, zero entropy.
    Stage 2: S_matter = 0. Pure Bogoliubov-transformed state. The transit
             creates EPR-correlated pairs but the TOTAL state is pure.
    Stage 3: S_matter = S_GGE. Off-diagonal coherences decohere. The GGE
             diagonal ensemble has nonzero entropy from the 8 conserved
             charges. Frustration shifts the Lagrange multipliers.
    Stage 4: S_matter = S_Gibbs. Conservation laws relax. The system
             approaches thermal equilibrium at T_compound = E_exc/8.

    The non-trivial test: does the 3-cell ring frustration modify S_GGE
    or S_Gibbs enough to affect GSL monotonicity? And does the a_2
    spectral entropy component behave monotonically?

    Frustration regime: J_C2/Delta_BCS = 0.933/0.464 = 2.01.
    This is STRONG coupling — the Josephson coupling exceeds the gap.
    Non-perturbative treatment required for ground state energy.
    However, the entropy of the ground state is still zero (pure state)
    because frustration selects a phase configuration, not a mixed state.

    For the GGE stage, frustration's effect on the Lagrange multipliers
    is through the mean-field energy shift. Since the GGE is defined by
    the conserved charges of the post-transit state, and the transit
    is local in tau (not in the cell-cell coupling), the primary effect
    of frustration is through the junction contribution to the total
    Hamiltonian, which modifies the energy landscape but not the
    number of conserved charges.

Author: Hawking-Theorist (S71)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import time

t_start = time.time()

# Import canonical constants
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, n_Bog, N_dof_BCS, n_pairs,
    E_B1, E_B2_mean, E_B3_mean, T_acoustic,
    J_C2, Delta_BCS, a2_fold, a0_fold, a4_fold,
    E_cond, PI, dt_transit, T_compound, E_exc
)

print("=" * 72)
print("THREE-CELL-GSL-71 — Generalized Second Law on 3-Cell Ring")
print("=" * 72)

# ==========================================================================
# Section 1: Physical Parameters
# ==========================================================================

N_cells = 3
N_junc = 3
N_modes = N_dof_BCS  # 8 modes per cell

N_B2, N_B1, N_B3 = 4, 1, 3

E_B2 = E_B2_mean    # 0.8453 M_KK
E_B1_val = E_B1     # 0.8191 M_KK
E_B3_val = E_B3_mean  # 0.9782 M_KK
E_modes = np.array([E_B2]*N_B2 + [E_B1_val]*N_B1 + [E_B3_val]*N_B3)

# GGE Lagrange multipliers (S39, S52, S64)
lambda_B2 = 1.459  # (local)
lambda_B1 = 2.771  # (local)
lambda_B3 = 6.007  # (local)

# Bogoliubov |beta_k|^2 (S61, bosonic convention)
beta_sq = 1.015  # (local)

# tau stages
tau_stages = np.array([0.22, 0.19, 0.16, 0.10])
stage_names = [
    "Pre-transit BCS (pure)",
    "Transit fold (pure)",
    "Post-transit GGE",
    "Late-time Gibbs"
]

print("\n--- Physical Parameters ---")
print(f"  N_cells       = {N_cells} (ring)")
print(f"  N_junctions   = {N_junc}")
print(f"  N_modes/cell  = {N_modes} (B2:{N_B2}, B1:{N_B1}, B3:{N_B3})")
print(f"  J_C2          = {J_C2} M_KK")
print(f"  Delta_BCS     = {Delta_BCS:.4f} M_KK")
print(f"  J_C2/Delta    = {J_C2/Delta_BCS:.4f} (STRONG coupling regime)")
print(f"  |beta_k|^2    = {beta_sq}")
print(f"  T_compound    = {T_compound:.4f} M_KK (= E_exc/8)")
print(f"  E_exc         = {E_exc:.4f} M_KK")

# ==========================================================================
# Section 2: Utility Functions
# ==========================================================================

def binary_entropy(p):
    """Fermionic binary entropy s(p) = -p*ln(p) - (1-p)*ln(1-p)."""
    p = np.clip(p, 1e-15, 1.0 - 1e-15)
    return -(p * np.log(p) + (1.0 - p) * np.log(1.0 - p))


def p_GGE(lam):
    """GGE occupation: p = 1/(1 + exp(lambda))."""
    return 1.0 / (1.0 + np.exp(lam))


def p_Fermi(E, T):
    """Fermi-Dirac distribution."""
    if T < 1e-15:
        return 0.0
    x = E / T
    return 1.0 / (1.0 + np.exp(x)) if x < 500 else 0.0


def exact_gibbs_entropy(T, E_modes):
    """Exact canonical entropy from 2^N partition function."""
    N = len(E_modes)
    log_boltz = np.zeros(2**N)
    energies = np.zeros(2**N)
    for state in range(2**N):
        E_state = sum(E_modes[k] for k in range(N) if state & (1 << k))
        energies[state] = E_state
        log_boltz[state] = -E_state / T
    max_lb = np.max(log_boltz)
    log_Z = max_lb + np.log(np.sum(np.exp(log_boltz - max_lb)))
    Z = np.exp(log_Z)
    E_avg = np.sum(energies * np.exp(log_boltz - log_Z))
    S = log_Z + E_avg / T
    return S, Z, E_avg


# ==========================================================================
# Section 3: Frustration Analysis
# ==========================================================================

print("\n" + "=" * 72)
print("FRUSTRATION ANALYSIS: 3-Cell Ring")
print("=" * 72)

# Ground state phase configuration: 120-degree separation
phi_ring = np.array([0.0, 2*PI/3, 4*PI/3])

E_J_bonds = []
I_J_bonds = []
for i in range(N_cells):
    j = (i + 1) % N_cells
    dphi = phi_ring[i] - phi_ring[j]
    E_J_bonds.append(-J_C2 * np.cos(dphi))
    I_J_bonds.append(J_C2 * np.sin(dphi))

E_J_total = sum(E_J_bonds)
E_J_aligned = -N_junc * J_C2

print(f"\n  Phases: [0, 2pi/3, 4pi/3]")
for i in range(N_cells):
    j = (i + 1) % N_cells
    print(f"  Bond {i+1}-{j+1}: E_J={E_J_bonds[i]:+.4f}, I_J={I_J_bonds[i]:+.6f} M_KK")
print(f"\n  E_J(frustrated) = {E_J_total:.4f} M_KK")
print(f"  E_J(aligned)    = {E_J_aligned:.4f} M_KK")
print(f"  Frustration gap = {E_J_total - E_J_aligned:.4f} M_KK")
print(f"  J/Delta         = {J_C2/Delta_BCS:.4f} (strong coupling)")

# Kirchhoff check: circulating current, all bonds equal by symmetry
I_circ = I_J_bonds[0]
kirchhoff = all(abs(I_J_bonds[i] - I_J_bonds[0]) < 1e-10 for i in range(N_cells))
print(f"\n  Circulating current: {I_circ:.6f} M_KK")
print(f"  Kirchhoff (all bonds equal): {kirchhoff}")

# ==========================================================================
# Section 4: 3-Cell Ring BCS Hamiltonian — Exact Diagonalization
# ==========================================================================
#
# Each cell has N_modes=8 fermionic modes. The full 3-cell Fock space
# has 256^3 = 16,777,216 states — too large for full diagonalization.
#
# TRUNCATION: Restrict to a manageable sector. The BCS physics is
# dominated by the N_pair=1 sector (S40: N_pair=1 exact).
# For each cell, use the 2-mode (1 B2 representative + pair) subspace:
# dim = 4 per cell, total = 4^3 = 64 states.
#
# Actually, the physical content is simpler. The frustration selects
# the phase pattern but does NOT change the BCS gap or the mode
# occupations. The BCS Hamiltonian is diagonal in the quasiparticle
# basis; the Josephson coupling enters as a phase constraint, not
# a mode-mixing term. The ground state is PURE for any phase
# configuration — frustration changes WHICH pure state, not WHETHER
# it's pure.
#
# We compute the frustration's effect on energetics explicitly.

print("\n" + "=" * 72)
print("3-CELL EXACT DIAGONALIZATION (truncated sector)")
print("=" * 72)

# Construct minimal 2-mode-per-cell Hamiltonian for the ring
# Each cell: BCS part H_BCS = -Delta * (c_up^dagger c_down^dagger + h.c.)
#            + epsilon * (n_up + n_down)
# Using representative B2 mode with epsilon = E_B2, Delta = Delta_BCS.
# Between cells: H_J = -J_C2 * cos(phi_i - phi_j) * (pair transfer)

# For 2-mode per cell (spin up/down pairing):
# States: |0,0>, |up>, |down>, |up,down> = |vac>, |1>, |1>, |pair>
# dim = 4 per cell, 4^3 = 64 total

dim_cell = 4  # |vac>, |up>, |down>, |pair>
dim_total = dim_cell**3

# Single-cell BCS Hamiltonian matrix
def H_BCS_cell(eps, Delta):
    """4x4 BCS Hamiltonian for 2-mode cell."""
    H = np.zeros((4, 4))
    # |vac>=0, |up>=1, |down>=2, |pair>=3
    H[1, 1] = eps       # single up
    H[2, 2] = eps       # single down
    H[3, 3] = 2*eps     # pair (2 particles)
    H[0, 3] = -Delta    # pair creation
    H[3, 0] = -Delta    # pair annihilation
    return H

# Construct the full 64x64 Hamiltonian
H_full = np.zeros((dim_total, dim_total))

# Helper: state index = i3 * 16 + i2 * 4 + i1 (cell 1, 2, 3)
def state_idx(i1, i2, i3):
    return i3 * 16 + i2 * 4 + i1

# Single-cell BCS terms (3 cells)
H_cell = H_BCS_cell(E_B2, Delta_BCS)

for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            idx = state_idx(i1, i2, i3)
            # Cell 1 BCS
            for i1p in range(4):
                if H_cell[i1, i1p] != 0:
                    jdx = state_idx(i1p, i2, i3)
                    H_full[idx, jdx] += H_cell[i1, i1p]
            # Cell 2 BCS
            for i2p in range(4):
                if H_cell[i2, i2p] != 0:
                    jdx = state_idx(i1, i2p, i3)
                    H_full[idx, jdx] += H_cell[i2, i2p]
            # Cell 3 BCS
            for i3p in range(4):
                if H_cell[i3, i3p] != 0:
                    jdx = state_idx(i1, i2, i3p)
                    H_full[idx, jdx] += H_cell[i3, i3p]

# Josephson coupling: pair transfer between cells
# H_J(i,j) = -J_C2 * cos(phi_i - phi_j) * (c_pair_i^dagger c_pair_j + h.c.)
# In our 4-state basis: pair transfer is |pair_i, vac_j> <-> |vac_i, pair_j>

# Junction 1-2
cos_12 = np.cos(phi_ring[0] - phi_ring[1])
# Junction 2-3
cos_23 = np.cos(phi_ring[1] - phi_ring[2])
# Junction 3-1
cos_31 = np.cos(phi_ring[2] - phi_ring[0])

def add_josephson(H, cell_a, cell_b, cos_phi):
    """Add Josephson pair-transfer coupling between two cells."""
    for other_cells in range(4**(N_cells - 2)):
        # Generate all states of the third cell
        for state_a_vac in [0]:   # cell a in |vac>
            for state_b_pair in [3]:  # cell b in |pair>
                for state_a_pair in [3]:  # cell a in |pair>
                    for state_b_vac in [0]:  # cell b in |vac>
                        # Build full state indices
                        if N_cells == 3:
                            cells = [0, 0, 0]
                            other_idx = 3 - cell_a - cell_b  # the third cell
                            for c_state in range(4):
                                cells_fwd = list(cells)
                                cells_fwd[cell_a] = state_a_vac
                                cells_fwd[cell_b] = state_b_pair
                                cells_fwd[other_idx] = c_state
                                idx_fwd = state_idx(*cells_fwd)

                                cells_rev = list(cells)
                                cells_rev[cell_a] = state_a_pair
                                cells_rev[cell_b] = state_b_vac
                                cells_rev[other_idx] = c_state
                                idx_rev = state_idx(*cells_rev)

                                H[idx_fwd, idx_rev] += -J_C2 * cos_phi
                                H[idx_rev, idx_fwd] += -J_C2 * cos_phi

add_josephson(H_full, 0, 1, cos_12)
add_josephson(H_full, 1, 2, cos_23)
add_josephson(H_full, 2, 0, cos_31)

# Verify Hermiticity
assert np.allclose(H_full, H_full.T), "Hamiltonian not Hermitian!"

# Diagonalize
evals, evecs = np.linalg.eigh(H_full)

E_GS = evals[0]
psi_GS = evecs[:, 0]

print(f"\n  Hilbert space: {dim_total} states (4^3, truncated 2-mode/cell)")
print(f"  E_GS = {E_GS:.6f} M_KK")
print(f"  E_1st = {evals[1]:.6f} M_KK (gap = {evals[1]-evals[0]:.6f})")

# Ground state density matrix
rho_GS = np.outer(psi_GS, psi_GS.conj())

# Per-cell reduced density matrix (trace over other 2 cells)
def trace_over_others(rho_full, keep_cell, N_cells=3, dim_cell=4):
    """Trace over all cells except keep_cell to get reduced rho."""
    rho_reduced = np.zeros((dim_cell, dim_cell), dtype=complex)
    for i_keep in range(dim_cell):
        for j_keep in range(dim_cell):
            for other_states in range(dim_cell**(N_cells - 1)):
                # Build full state indices
                cells_i = [0]*N_cells
                cells_j = [0]*N_cells
                cells_i[keep_cell] = i_keep
                cells_j[keep_cell] = j_keep
                # Decode other_states into cell indices
                temp = other_states
                for c in range(N_cells):
                    if c != keep_cell:
                        cells_i[c] = temp % dim_cell
                        cells_j[c] = temp % dim_cell  # trace = same index
                        temp //= dim_cell
                idx_i = state_idx(*cells_i)
                idx_j = state_idx(*cells_j)
                rho_reduced[i_keep, j_keep] += rho_full[idx_i, idx_j]
    return rho_reduced

# Compute per-cell reduced density matrices
S_cell_GS = np.zeros(N_cells)
for c in range(N_cells):
    rho_c = trace_over_others(rho_GS, c)
    eigs_c = np.linalg.eigvalsh(rho_c)
    eigs_c = eigs_c[eigs_c > 1e-15]
    S_cell_GS[c] = -np.sum(eigs_c * np.log(eigs_c))

print(f"\n  Per-cell entanglement entropy (ground state):")
for c in range(N_cells):
    print(f"    Cell {c+1}: S = {S_cell_GS[c]:.6f} nats")
print(f"  Mean per-cell S: {np.mean(S_cell_GS):.6f} nats")
print(f"  Note: nonzero from Josephson entanglement between cells")

# Total ground state entropy (should be 0 for pure state)
rho_eigs = np.linalg.eigvalsh(rho_GS)
rho_eigs = rho_eigs[rho_eigs > 1e-15]
S_total_GS = -np.sum(rho_eigs * np.log(rho_eigs))
print(f"  Total S (pure state check): {S_total_GS:.2e} nats (should be ~0)")

# Compare with unfrustrated ring
H_unfrust = np.zeros_like(H_full)
# Same BCS terms
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            idx = state_idx(i1, i2, i3)
            for i1p in range(4):
                if H_cell[i1, i1p] != 0:
                    jdx = state_idx(i1p, i2, i3)
                    H_unfrust[idx, jdx] += H_cell[i1, i1p]
            for i2p in range(4):
                if H_cell[i2, i2p] != 0:
                    jdx = state_idx(i1, i2p, i3)
                    H_unfrust[idx, jdx] += H_cell[i2, i2p]
            for i3p in range(4):
                if H_cell[i3, i3p] != 0:
                    jdx = state_idx(i1, i2, i3p)
                    H_unfrust[idx, jdx] += H_cell[i3, i3p]

# Unfrustrated: all cos=1
add_josephson(H_unfrust, 0, 1, 1.0)
add_josephson(H_unfrust, 1, 2, 1.0)
add_josephson(H_unfrust, 2, 0, 1.0)

evals_uf, evecs_uf = np.linalg.eigh(H_unfrust)
E_GS_uf = evals_uf[0]
psi_GS_uf = evecs_uf[:, 0]

rho_GS_uf = np.outer(psi_GS_uf, psi_GS_uf.conj())
S_cell_uf = np.zeros(N_cells)
for c in range(N_cells):
    rho_c = trace_over_others(rho_GS_uf, c)
    eigs_c = np.linalg.eigvalsh(rho_c)
    eigs_c = eigs_c[eigs_c > 1e-15]
    S_cell_uf[c] = -np.sum(eigs_c * np.log(eigs_c))

print(f"\n  Unfrustrated ring comparison:")
print(f"  E_GS(frustrated) = {E_GS:.6f} M_KK")
print(f"  E_GS(aligned)    = {E_GS_uf:.6f} M_KK")
print(f"  Frustration lift = {E_GS - E_GS_uf:.6f} M_KK")
print(f"  Per-cell S (aligned): {np.mean(S_cell_uf):.6f} nats")
print(f"  Per-cell S (frust):   {np.mean(S_cell_GS):.6f} nats")
print(f"  Frustration enhances entanglement: "
      f"{np.mean(S_cell_GS)/np.mean(S_cell_uf):.4f}x")

# ==========================================================================
# Section 5: Spectral Entropy S_a2(tau)
# ==========================================================================

print("\n" + "=" * 72)
print("SPECTRAL ENTROPY S_a2(tau)")
print("=" * 72)

# Load S70 BCS curvature data
try:
    d70 = np.load(str(Path(__file__).parent / 's70_kretschner_bcs.npz'),
                  allow_pickle=True)
    tau_arr_70 = d70['tau_values']
    R_scalar_BCS_70 = d70['R_scalar_BCS']
    delta_a2_ratio_fold = float(d70['delta_a2_ratio'])
    print(f"  Loaded S70 data: {len(tau_arr_70)} tau values")
except Exception as e:
    print(f"  WARNING: Could not load S70 data: {e}")
    delta_a2_ratio_fold = 0.116  # (local)

from scipy.interpolate import interp1d

R_interp = interp1d(tau_arr_70, R_scalar_BCS_70, kind='cubic',
                    fill_value='extrapolate')
R_fold = R_interp(tau_fold)

# BCS pair number at each stage (determines backreaction)
n_pairs_stages = np.array([0.0, n_pairs/2, n_pairs, n_pairs])

# BCS correction to a_2: proportional to excited pairs
delta_a2_per_pair = delta_a2_ratio_fold * a2_fold / n_pairs
a2_BCS_corr = n_pairs_stages * delta_a2_per_pair

# Bare a_2 at each tau
R_stages = R_interp(tau_stages)
a2_bare = a2_fold * R_stages / R_fold
a2_total = a2_bare + a2_BCS_corr

# S_a2 per cell: normalized by 4*a2_fold (Bekenstein analog)
S_a2_per_cell = a2_total / (4.0 * a2_fold)
S_a2_3cell = N_cells * S_a2_per_cell

print(f"\n  {'Stage':>6} | {'tau':>5} | {'n_pair':>7} | {'a2_bare':>10} | "
      f"{'a2_BCS':>10} | {'a2_tot':>10} | {'S_a2/cell':>10}")
for i in range(4):
    print(f"  {i+1:>6} | {tau_stages[i]:>5.2f} | {n_pairs_stages[i]:>7.1f} | "
          f"{a2_bare[i]:>10.2f} | {a2_BCS_corr[i]:>10.2f} | "
          f"{a2_total[i]:>10.2f} | {S_a2_per_cell[i]:>10.6f}")

S_a2_monotone = all(S_a2_3cell[i+1] >= S_a2_3cell[i] for i in range(3))
print(f"\n  S_a2 (3-cell) monotone: {S_a2_monotone}")

# ==========================================================================
# Section 6: Physical Entropy Trajectory (S_matter)
# ==========================================================================
#
# The PHYSICAL entropy follows S64's analysis:
#   Stage 1: S_matter = 0 (pure BCS, frustrated but pure)
#   Stage 2: S_matter = 0 (pure Bogoliubov-transformed state)
#   Stage 3: S_matter = S_GGE (decoherence of off-diagonal terms)
#   Stage 4: S_matter = S_Gibbs (conservation laws relaxed)
#
# The per-cell ENTANGLEMENT entropy (from tracing over other cells and
# partner modes) is a different quantity. It is nonzero at Stages 1-2
# but reflects correlations, not ignorance.
#
# For the GSL, we track the TOTAL physical entropy. The total state is
# pure at Stages 1-2, so S_matter = 0. At Stage 3, decoherence converts
# the pure state to the GGE mixed state. At Stage 4, relaxation of
# conservation laws converts GGE to Gibbs.
#
# For the 3-cell ring, we additionally track the JUNCTION entropy:
# the Shannon entropy of the phase fluctuations across each bond.
# This is zero in the ground state (definite phase), grows during
# transit, and saturates at ln(2) per bond at thermalization.

print("\n" + "=" * 72)
print("PHYSICAL ENTROPY S_matter: Stage-by-Stage")
print("=" * 72)

# --- Stage 1: Pure BCS (frustrated) ---
# Total entropy = 0 (pure state). Per-cell entanglement from ED above.
# Junction contribution: zero (phase is definite, just frustrated).
S_matter_1 = 0.0  # (local)
S_ent_per_cell_1 = np.mean(S_cell_GS)  # from ED, for reference

print(f"\n--- Stage 1 (tau=0.22): Pure BCS ground state ---")
print(f"  S_matter (total)  = {S_matter_1:.6f} nats (PURE STATE)")
print(f"  S_ent per cell    = {S_ent_per_cell_1:.6f} nats (Josephson entanglement)")
print(f"  Note: entanglement entropy is NOT physical entropy for GSL")

# --- Stage 2: Pure Bogoliubov-transformed state ---
# Total entropy = 0. Transit creates correlated pairs but state is pure.
p_transit = beta_sq / (1.0 + beta_sq)
S_ent_transit_per_mode = binary_entropy(p_transit)
S_ent_transit_per_cell = N_modes * S_ent_transit_per_mode

S_matter_2 = 0.0  # (local)

print(f"\n--- Stage 2 (tau=0.19): Transit (pure state) ---")
print(f"  p_transit         = {p_transit:.6f}")
print(f"  S_matter (total)  = {S_matter_2:.6f} nats (PURE STATE)")
print(f"  S_ent per cell    = {S_ent_transit_per_cell:.4f} nats (if traced)")

# --- Stage 3: GGE after decoherence ---
# The GGE diagonal ensemble. Frustration modifies the energy landscape.
# The Lagrange multipliers lambda_k are determined by the conserved
# charges of the SPECIFIC post-transit state.
#
# For the frustrated ring, the junction coupling adds an energy offset
# but does NOT change the number of conserved charges (the Richardson-
# Gaudin integrals are properties of each cell's BCS Hamiltonian).
# The frustration enters through the BOUNDARY CONDITIONS on the
# Bogoliubov transformation — the transit at each cell sees the
# mean field of its neighbors.
#
# Net effect: lambda_k shift by a small amount proportional to J_C2/E_mode.
# Since J_C2/E_B2 ~ 1.1, this is a significant correction.

# Frustration correction to GGE multipliers (mean-field)
# delta_lambda_k = -2 * J_C2 * cos(2pi/3) / E_k
# (factor 2 from 2 neighbors on the ring)
# cos(2pi/3) = -1/2, so delta_lambda_k = +J_C2 / E_k
delta_lam_B2 = J_C2 / E_B2  # ~ 1.10
delta_lam_B1 = J_C2 / E_B1_val  # ~ 1.14
delta_lam_B3 = J_C2 / E_B3_val  # ~ 0.95

# The frustration INCREASES lambda (pushes occupations DOWN, LESS entropy)
# compared to unfrustrated. This is physically correct: frustration
# constrains the system, reducing the accessible phase space.
lambda_B2_f = lambda_B2 + delta_lam_B2
lambda_B1_f = lambda_B1 + delta_lam_B1
lambda_B3_f = lambda_B3 + delta_lam_B3

p_B2_f = p_GGE(lambda_B2_f)
p_B1_f = p_GGE(lambda_B1_f)
p_B3_f = p_GGE(lambda_B3_f)

# Unfrustrated GGE (reference)
p_B2_0 = p_GGE(lambda_B2)
p_B1_0 = p_GGE(lambda_B1)
p_B3_0 = p_GGE(lambda_B3)

S_GGE_cell_0 = (N_B2 * binary_entropy(p_B2_0) +
                N_B1 * binary_entropy(p_B1_0) +
                N_B3 * binary_entropy(p_B3_0))

S_GGE_cell_f = (N_B2 * binary_entropy(p_B2_f) +
                N_B1 * binary_entropy(p_B1_f) +
                N_B3 * binary_entropy(p_B3_f))

# Junction entropy at GGE stage: partially disordered
# The junction phase fluctuations grow as the condensate weakens.
# S_junc ~ 3 * binary_entropy(1 - n_cond_GGE)
# From S70: n_cond_GGE = 0.9997
n_cond_GGE = 0.9997
S_junc_GGE = N_junc * binary_entropy(1 - n_cond_GGE)

S_matter_3 = N_cells * S_GGE_cell_f + S_junc_GGE

print(f"\n--- Stage 3 (tau=0.16): Post-transit GGE ---")
print(f"  Frustration shifts (delta_lambda):")
print(f"    B2: +{delta_lam_B2:.4f} -> lambda = {lambda_B2_f:.4f}")
print(f"    B1: +{delta_lam_B1:.4f} -> lambda = {lambda_B1_f:.4f}")
print(f"    B3: +{delta_lam_B3:.4f} -> lambda = {lambda_B3_f:.4f}")
print(f"  Occupations (frustrated / bare):")
print(f"    p_B2 = {p_B2_f:.6f} / {p_B2_0:.6f}")
print(f"    p_B1 = {p_B1_f:.6f} / {p_B1_0:.6f}")
print(f"    p_B3 = {p_B3_f:.6f} / {p_B3_0:.6f}")
print(f"  S_GGE/cell: frustrated={S_GGE_cell_f:.4f}, bare={S_GGE_cell_0:.4f}")
print(f"  S_junc (3 bonds):  {S_junc_GGE:.6f} nats")
print(f"  S_matter (total):  {S_matter_3:.6f} nats")
print(f"  Enhancement: {S_GGE_cell_f/S_GGE_cell_0:.4f}x per cell")

# --- Stage 4: Gibbs thermalization ---
# At T_compound, the exact Gibbs entropy per cell from 256-state
# partition function. Frustration at this stage is subdominant:
# T_compound >> J_C2, so all junction phases thermalize.
S_Gibbs_cell, Z_G, E_avg_G = exact_gibbs_entropy(T_compound, E_modes)

# Junction entropy: saturated (T >> J)
S_junc_Gibbs = N_junc * np.log(2)
S_matter_4 = N_cells * S_Gibbs_cell + S_junc_Gibbs

print(f"\n--- Stage 4 (tau=0.10): Gibbs relaxation ---")
print(f"  T = T_compound = {T_compound:.4f} M_KK")
print(f"  S_Gibbs/cell (256-state): {S_Gibbs_cell:.6f} nats")
print(f"  Z = {Z_G:.4f}, <E> = {E_avg_G:.4f} M_KK")
print(f"  S_junc (saturated): {S_junc_Gibbs:.6f} nats")
print(f"  S_matter (total):   {S_matter_4:.6f} nats")

# Cross-check with S64
print(f"\n  Cross-check:")
print(f"    S_GGE/cell: S64=2.2125, this(bare)={S_GGE_cell_0:.4f}")
print(f"    S_Gibbs/cell: S64=4.6448, this={S_Gibbs_cell:.4f}")
# NOTE: S_Gibbs at T_compound may differ from S64 because S64 found
# the T that gives exactly 4.6448 nats. Let me check.
S_Gibbs_at_T113, _, _ = exact_gibbs_entropy(0.113, E_modes)
S_Gibbs_at_Tacoustic, _, _ = exact_gibbs_entropy(T_acoustic, E_modes)
print(f"    S_Gibbs at T=0.113: {S_Gibbs_at_T113:.4f} nats")
print(f"    S_Gibbs at T_acoustic={T_acoustic}: {S_Gibbs_at_Tacoustic:.4f} nats")

# ==========================================================================
# Section 7: Generalized Entropy S_gen = S_a2 + S_matter
# ==========================================================================

print("\n" + "=" * 72)
print("GENERALIZED SECOND LAW: S_gen at 4 Stages")
print("=" * 72)

S_matter = np.array([S_matter_1, S_matter_2, S_matter_3, S_matter_4])
S_gen = S_a2_3cell + S_matter

print(f"\n  {'Stage':>6} | {'tau':>5} | {'S_a2':>10} | {'S_matter':>10} | "
      f"{'S_gen':>10} | {'Delta':>10}")
print(f"  {'-'*6} | {'-'*5} | {'-'*10} | {'-'*10} | {'-'*10} | {'-'*10}")

for i in range(4):
    delta = S_gen[i] - S_gen[i-1] if i > 0 else 0.0
    delta_str = '---' if i == 0 else f'{delta:+.6f}'
    print(f"  {i+1:>6} | {tau_stages[i]:>5.2f} | {S_a2_3cell[i]:>10.6f} | "
          f"{S_matter[i]:>10.6f} | {S_gen[i]:>10.6f} | {delta_str:>10}")

# Monotonicity
all_nondec = all(S_gen[i+1] >= S_gen[i] for i in range(3))
n_nondec = sum(1 for i in range(3) if S_gen[i+1] >= S_gen[i])

print(f"\n  S_gen monotone: {all_nondec}")
print(f"  Transitions:    {n_nondec}/3 non-decreasing")

# Component analysis
for i in range(3):
    dS_a2 = S_a2_3cell[i+1] - S_a2_3cell[i]
    dS_mat = S_matter[i+1] - S_matter[i]
    dS_gen = S_gen[i+1] - S_gen[i]
    driver = "S_a2" if abs(dS_a2) > abs(dS_mat) else "S_matter"
    print(f"  {i+1}->{i+2}: dS_a2={dS_a2:+.4f}, dS_mat={dS_mat:+.4f}, "
          f"dS_gen={dS_gen:+.4f} [{driver}]")

# ==========================================================================
# Section 8: Frustration Enhancement Analysis
# ==========================================================================

print("\n" + "=" * 72)
print("FRUSTRATION ENHANCEMENT")
print("=" * 72)

# Per-cell entropy comparison
print(f"\n  Per-cell S_GGE:")
print(f"    Unfrustrated: {S_GGE_cell_0:.4f} nats")
print(f"    Frustrated:   {S_GGE_cell_f:.4f} nats")
print(f"    Ratio:        {S_GGE_cell_f/S_GGE_cell_0:.4f}")
delta_S_frust = S_GGE_cell_f - S_GGE_cell_0
print(f"    Delta (frust): {delta_S_frust:+.4f} nats ({delta_S_frust/S_GGE_cell_0*100:+.1f}%)")

# Ground state entanglement comparison
print(f"\n  Ground state entanglement (per cell):")
print(f"    Frustrated:   {np.mean(S_cell_GS):.6f} nats")
print(f"    Unfrustrated: {np.mean(S_cell_uf):.6f} nats")
if np.mean(S_cell_uf) > 1e-10:
    print(f"    Ratio:        {np.mean(S_cell_GS)/np.mean(S_cell_uf):.4f}")
else:
    print(f"    Ratio:        inf (unfrustrated has ~0 entanglement)")

print(f"\n  Junction physics:")
print(f"    Circulating current:  {abs(I_circ):.4f} M_KK")
print(f"    Frustration energy:   {E_GS - E_GS_uf:.4f} M_KK")
print(f"    Bond energy (frust):  {E_J_bonds[0]:+.4f} M_KK (each, by symmetry)")
print(f"    Bond energy (align):  {-J_C2:+.4f} M_KK")

# ==========================================================================
# Section 9: Cross-Checks
# ==========================================================================

print("\n" + "=" * 72)
print("CROSS-CHECKS")
print("=" * 72)

chk1 = all(S_gen[i] >= 0 for i in range(4))
print(f"  [1] S_gen >= 0 at all stages: {chk1}")

S_max = N_cells * N_modes * np.log(2) + N_junc * np.log(2)
chk2 = all(S_matter[i] <= S_max * 1.001 for i in range(4))
print(f"  [2] S_matter <= S_max ({S_max:.4f}): {chk2}")

u_sq = 1.0 / (1.0 + beta_sq)
v_sq = beta_sq / (1.0 + beta_sq)
chk3 = abs(u_sq + v_sq - 1.0) < 1e-10
print(f"  [3] |u|^2 + |v|^2 = {u_sq + v_sq:.10f}: {chk3}")

chk4 = abs(S_GGE_cell_0 - 2.2125) < 0.01
print(f"  [4] S_GGE/cell matches S64: {S_GGE_cell_0:.4f} vs 2.2125: {chk4}")

print(f"  [5] Kirchhoff on ring: {kirchhoff}")

# Phase single-valuedness
dphi_sum = sum(phi_ring[(i+1)%N_cells] - phi_ring[i] for i in range(N_cells))
chk6 = abs(dphi_sum % (2*PI)) < 1e-10 or abs(dphi_sum % (2*PI) - 2*PI) < 1e-10
print(f"  [6] Phase single-valued: sum(dphi) = {dphi_sum:.4f} = "
      f"{dphi_sum/(2*PI):.4f} * 2pi: {chk6}")

chk7 = abs(S_total_GS) < 1e-10
print(f"  [7] GS purity: S_total = {S_total_GS:.2e}: {chk7}")

# Hermiticity of Hamiltonian
chk8 = np.allclose(H_full, H_full.T)
print(f"  [8] Hamiltonian Hermitian: {chk8}")

# ==========================================================================
# Section 10: Gate Verdict
# ==========================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: THREE-CELL-GSL-71")
print("=" * 72)

if all_nondec:
    verdict = "PASS"
    detail = (f"S_gen monotonically non-decreasing at all 4 stages. "
              f"GSL extends to frustrated 3-cell ring topology on CG(24).")
elif n_nondec >= 2:
    verdict = "INFO"
    fail_trans = [f"stage {i+1}->{i+2}" for i in range(3)
                  if S_gen[i+1] < S_gen[i]]
    detail = (f"S_gen non-decreasing at {n_nondec+1}/4 stages. "
              f"Non-monotone at: {', '.join(fail_trans)}.")
else:
    verdict = "FAIL"
    detail = f"S_gen non-decreasing at only {n_nondec+1}/4 stages."

print(f"\n  Gate: THREE-CELL-GSL-71")
print(f"  Verdict: {verdict}")
print(f"  Criterion: S_gen non-decreasing at all 4 stages")
print(f"  Detail: {detail}")

print(f"\n  S_gen trajectory (nats):")
for i in range(4):
    print(f"    Stage {i+1} ({stage_names[i]}): {S_gen[i]:.6f}")

print(f"\n  Key quantitative results:")
print(f"    1. Frustration energy:      {E_GS - E_GS_uf:.4f} M_KK")
print(f"    2. GS entanglement (frust): {np.mean(S_cell_GS):.6f} nats/cell")
print(f"    3. S_GGE/cell (frust/bare): {S_GGE_cell_f:.4f}/{S_GGE_cell_0:.4f} = {S_GGE_cell_f/S_GGE_cell_0:.4f}")
print(f"    4. S_gen increase (1->4):   {S_gen[3]-S_gen[0]:+.4f} nats")
print(f"    5. Circulating current:     {abs(I_circ):.4f} M_KK")

# ==========================================================================
# Section 11: Save Data
# ==========================================================================

elapsed = time.time() - t_start

outpath = Path(__file__).parent / 's71_three_cell_gsl.npz'
np.savez(
    str(outpath),
    # Gate
    gate_name='THREE-CELL-GSL-71',
    gate_verdict=verdict,
    gate_detail=detail,
    # Topology
    N_cells=N_cells,
    N_junctions=N_junc,
    N_modes_per_cell=N_modes,
    # Stages
    tau_stages=tau_stages,
    stage_names=np.array(stage_names),
    # Entropy components
    S_a2_3cell=S_a2_3cell,
    S_matter=S_matter,
    S_gen=S_gen,
    # Frustration
    phi_ring=phi_ring,
    E_J_total=E_J_total,
    E_J_aligned=E_J_aligned,
    E_GS_frust=E_GS,
    E_GS_aligned=E_GS_uf,
    I_circ=I_circ,
    S_cell_GS_frust=S_cell_GS,
    S_cell_GS_aligned=S_cell_uf,
    # GGE
    lambda_B2_frust=lambda_B2_f,
    lambda_B1_frust=lambda_B1_f,
    lambda_B3_frust=lambda_B3_f,
    S_GGE_cell_frust=S_GGE_cell_f,
    S_GGE_cell_bare=S_GGE_cell_0,
    # Gibbs
    S_Gibbs_cell=S_Gibbs_cell,
    T_Gibbs_phys=T_compound,
    # Cross-checks
    S_a2_monotone=S_a2_monotone,
    all_nondecreasing=all_nondec,
    n_nondecreasing_transitions=n_nondec,
    Bogoliubov_norm=u_sq + v_sq,
    kirchhoff=kirchhoff,
    GS_purity=S_total_GS,
    # Timing
    elapsed_s=elapsed
)

print(f"\n  Data saved: {outpath}")
print(f"  Elapsed: {elapsed:.2f} s")

# ==========================================================================
# Section 12: Plot
# ==========================================================================

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot 1: S_gen trajectory
ax = axes[0]
ax.plot(range(1, 5), S_gen, 'ko-', lw=2.5, ms=9, label=r'$S_{\rm gen}$', zorder=5)
ax.plot(range(1, 5), S_a2_3cell, 's--', color='blue', ms=6, label=r'$S_{a_2}$')
ax.plot(range(1, 5), S_matter, '^--', color='red', ms=6, label=r'$S_{\rm matter}$')
ax.set_ylabel('Entropy (nats)', fontsize=12)
ax.set_title(f'THREE-CELL-GSL-71: {verdict}', fontsize=11, fontweight='bold')
ax.legend(fontsize=9)
ax.set_xticks(range(1, 5))
ax.set_xticklabels([f'{tau_stages[i]:.2f}' for i in range(4)], fontsize=9)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.grid(True, alpha=0.3)

# Plot 2: Component stacked bar
ax = axes[1]
x = np.arange(4)
ax.bar(x, S_a2_3cell, 0.6, label=r'$S_{a_2}$', color='steelblue')
ax.bar(x, S_matter, 0.6, bottom=S_a2_3cell, label=r'$S_{\rm matter}$', color='coral')
ax.set_ylabel('Entropy (nats)', fontsize=12)
ax.set_title('Entropy Components', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels([f'S{i+1}' for i in range(4)])
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# Plot 3: Phase diagram
ax = axes[2]
theta_c = np.linspace(0, 2*PI, 100)
ax.plot(np.cos(theta_c), np.sin(theta_c), 'k-', lw=0.5, alpha=0.3)
colors = ['C0', 'C1', 'C2']
for i in range(N_cells):
    ax.plot(np.cos(phi_ring[i]), np.sin(phi_ring[i]), 'o', ms=15, color=colors[i],
            label=f'Cell {i+1}')
    j = (i + 1) % N_cells
    ax.annotate('', xy=(np.cos(phi_ring[j]), np.sin(phi_ring[j])),
                xytext=(np.cos(phi_ring[i]), np.sin(phi_ring[i])),
                arrowprops=dict(arrowstyle='->', color=colors[i], lw=2, alpha=0.6))
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_title('Frustrated 3-Cell Ring', fontsize=11)
ax.legend(fontsize=8, loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
figpath = Path(__file__).parent / 's71_three_cell_gsl.png'
plt.savefig(str(figpath), dpi=150, bbox_inches='tight')
print(f"  Plot saved: {figpath}")

print("\n" + "=" * 72)
print("DONE: THREE-CELL-GSL-71")
print("=" * 72)
