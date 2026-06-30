#!/usr/bin/env python3
"""
VIRTUAL-PARTICLE-73B: Virtual Particle Decay on CG(24)
=======================================================

Gate: VIRTUAL-PARTICLE-73B
  PASS: Gamma_virt > Gamma_Josephson (virtual particles decay faster than
        they propagate between cells) AND the decaying component is off-shell
        (E^2 != E_qp^2 for the dominant spectral component).
  FAIL: Gamma_virt < Gamma_Josephson (perturbation propagates as a stable
        excitation).
  INFO: Decomposition into Richardson-Gaudin conserved charges is exact to
        machine epsilon (perturbation is a GGE rearrangement, not a decaying
        fluctuation).

Physics (substrate framing):
  A "virtual particle" is NOT a thing in spacetime. It is a transient
  reorganization of the fabric's spectral content — a basis state on the
  Fock space that is not an exact eigenstate of the full BCS+Josephson
  Hamiltonian. Its occupation numbers deviate from the GGE equilibrium
  distribution and must "decay" by dephasing among the true energy
  eigenstates. The timescale of this dephasing IS the virtual-particle
  lifetime.

  In the substrate picture:
    * GGE equilibrium:  exact eigenstate distribution (no dynamics, Re=0)
    * Virtual particle: localized Fock basis state (non-eigenstate, Re>0)
    * "Decay":          dephasing of the amplitude on cell 1 mode B1
    * "Propagation":    spread to cells 2, 3, 4 via Josephson hopping

  S73A W3-B confirmed Luttinger superselection: N_pair is conserved to
  machine epsilon. S73B W2-E found intermediate chaos <r>=0.4625 in
  single-cell BCS. This computation tests: can a localized perturbation
  on the 4-cell Richardson-Gaudin + Josephson Hamiltonian decay faster
  than it propagates, and does the decomposition into R-G conserved
  charges close exactly?

Method:
  1. Construct a 4-cell BCS + Josephson Hamiltonian:
       H = sum_c [sum_k 2 eps_k n_{c,k} + sum_{k,l} V_{kl} b^dag_{c,k} b_{c,l}]
         + E_J sum_{<c,c'>} sum_k [b^dag_{c,k} b_{c',k} + h.c.]
     where c = 1..4 labels cells, k = 0..7 labels B1/B2/B3 modes.
     The C_4 ring adjacency matches a 4-node cycle extracted from CG(24).
  2. Work in the fixed N_pair = 2 sector, dim = C(32, 2) = 496.
  3. Diagonalize H exactly (dense).
  4. Prepare the GGE thermal state at T_acoustic = 0.112 M_KK using the
     R-G conserved charges (level occupations), so it commutes with the
     single-cell integrable H.
  5. Define the perturbation: move +1 pair from a GGE-weighted slot to
     the (cell=1, B1) slot. The resulting state |psi_0> has
     <n_{cell=1, B1}(t=0)> = <n_{cell=1, B1}>_{GGE} + 1.
  6. Time-evolve |psi_0> under the full H:
       |psi(t)> = exp(-i H t) |psi_0>
     and compute
       delta_n_{c,k}(t) = <psi(t)|n_{c,k}|psi(t)> - <n_{c,k}>_{GGE}
     for c = 1..4, k = B1.
  7. Fit the decay envelope of delta_n_{cell=1, B1}(t) to extract
     Gamma_virt. Measure the spatial propagation to cells 2-4 and
     compare Gamma_virt to Gamma_Josephson = J_C2 / hbar.
  8. Decompose |psi_0> onto the R-G conserved charge manifold
     (cell-occupation numbers). Compute the conserved part and the
     decaying remainder. Check if the decaying component is off-shell:
     compare <E>_dec to the quasi-particle energy E_qp = Delta_BCS.
  9. Estimate the Yukawa screening length xi_virt = c_BA / Gamma_virt
     and compare to l_Planck.

Input files:
  computations/_shared/canonical_constants.py
  computations/session-64/s64_local_entangle.npz  (CG(24) adjacency)
  computations/session-56/s56_gge_fabric.npz      (eps_fold, V_fold, E_J_fold)
  computations/session-73/s73a_luttinger_supersonic.npz (sector weights)

Output files:
  computations/session-73/s73b_virtual_particle.npz
  computations/session-73/s73b_virtual_particle.png

Session: S73B W4-A
Agent: phonon-first-cosmologist
"""

import os
import sys
import time
import numpy as np
from itertools import combinations
from math import comb as mcomb
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Canonical constants ===
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, N_dof_BCS, M_KK,
    Delta_BCS, Delta_0_OES,
    E_B1, E_B2_mean, E_B3_mean,
    J_C2, J_su2, J_u1, T_acoustic,
    c_fabric, c_Gold, omega_att, omega_L1,
    l_Planck, hbar_GeV_s,
)

data_dir = os.path.dirname(os.path.abspath(__file__))

t_start = time.time()
print("=" * 72)
print("VIRTUAL-PARTICLE-73B")
print("Virtual Particle Decay on CG(24) -- Single-Mode Perturbation")
print("=" * 72)
print(f"tau_fold    = {tau_fold}")
print(f"Delta_BCS   = {Delta_BCS:.6f} M_KK")
print(f"J_C2        = {J_C2} M_KK  (Josephson coupling, dominant)")
print(f"T_acoustic  = {T_acoustic} M_KK")
print(f"c_Gold      = {c_Gold} M_KK (Goldstone sound speed)")
print(f"M_KK        = {M_KK:.4e} GeV")
print()

# ============================================================
#  1. LOAD INPUT DATA
# ============================================================

d64 = np.load(os.path.join(data_dir, 's64_local_entangle.npz'),
              allow_pickle=True)
adj_cg24 = d64['adj_cg24'].astype(float)
N_vertices_cg24 = int(d64['N_vert'])
assert adj_cg24.shape == (24, 24)
assert N_vertices_cg24 == 24

d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'),
              allow_pickle=True)
eps_fold = np.asarray(d56['eps_fold'], dtype=float)
V_fold = np.asarray(d56['V_fold'], dtype=float)
E_J_fold = float(d56['E_J_fold'])

d73a = np.load(os.path.join(data_dir, 's73a_luttinger_supersonic.npz'),
               allow_pickle=True)
print(f"S73A Luttinger data: N_modes = {int(d73a['N_modes'])}")
print(f"  delta_N_full_rel = {float(d73a['delta_N_full_rel']):.2e}")
print(f"  (Luttinger superselection confirmed to machine epsilon)")
print()

N_modes = int(len(eps_fold))   # 8
N_cells = 4                    # (local) 4-cell cycle extracted from CG(24)
N_slots = N_modes * N_cells    # (local) 32
N_pair = 2                     # (local) 2 pairs total on 4 cells

print(f"System: N_modes = {N_modes}, N_cells = {N_cells}, "
      f"N_slots = {N_slots}, N_pair = {N_pair}")
print(f"Dim(Fock) = C({N_slots},{N_pair}) = {mcomb(N_slots, N_pair)}")

# ============================================================
#  2. C_4 RING FROM CG(24)
# ============================================================

def find_C4(adj, n):
    """Find a 4-cycle in adj (as induced subgraph or not)."""
    for v0 in range(n):
        nbrs0 = np.where(adj[v0] > 0.5)[0]
        for v1 in nbrs0:
            if v1 <= v0:
                continue
            nbrs1 = np.where(adj[v1] > 0.5)[0]
            for v2 in nbrs1:
                if v2 == v0:
                    continue
                if adj[v2, v0] > 0.5:
                    continue
                nbrs2 = np.where(adj[v2] > 0.5)[0]
                for v3 in nbrs2:
                    if v3 in (v0, v1):
                        continue
                    if adj[v3, v0] > 0.5 and adj[v3, v1] < 0.5:
                        return (v0, v1, v2, v3)
    return None

c4_verts = find_C4(adj_cg24, N_vertices_cg24)
assert c4_verts is not None, "No C_4 in CG(24)"
v0, v1, v2, v3 = c4_verts
assert adj_cg24[v0, v1] > 0.5
assert adj_cg24[v1, v2] > 0.5
assert adj_cg24[v2, v3] > 0.5
assert adj_cg24[v3, v0] > 0.5
print(f"\nC_4 ring in CG(24): vertices {c4_verts}")
print("Cell ordering: cell 0 = v0, cell 1 = v1, cell 2 = v2, cell 3 = v3")

# C_4 adjacency (0-1-2-3-0 cycle)
adj_C4 = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
], dtype=float)

# ============================================================
#  3. PAIR FOCK SPACE
# ============================================================

basis = list(combinations(range(N_slots), N_pair))
dim = len(basis)
basis_dict = {s: i for i, s in enumerate(basis)}
print(f"\nFock basis built: {dim} states")

# Slot <-> (cell, mode) mapping: slot = cell * N_modes + mode
def slot_to_cell_mode(slot):
    return slot // N_modes, slot % N_modes

def cell_mode_to_slot(c, m):
    return c * N_modes + m

# ============================================================
#  4. BUILD BCS + JOSEPHSON HAMILTONIAN
# ============================================================

print("\n" + "=" * 72)
print("HAMILTONIAN CONSTRUCTION")
print("=" * 72)

t_h = time.time()
H = np.zeros((dim, dim), dtype=float)
V_sym = (V_fold + V_fold.T) / 2.0  # enforce symmetry

for i, state_i in enumerate(basis):
    # --- Diagonal: kinetic energy ---
    E_kin = 0.0  # (local)
    for slot in state_i:
        c, m = slot_to_cell_mode(slot)
        E_kin += 2.0 * eps_fold[m]
    H[i, i] += E_kin

    # --- Off-diagonal: intra-cell pairing V_{kl} ---
    # Move a pair from slot (c, k) to slot (c, l) within SAME cell
    for slot_k in state_i:
        c_k, k = slot_to_cell_mode(slot_k)
        for l in range(N_modes):
            if l == k:
                continue
            slot_l = cell_mode_to_slot(c_k, l)
            if slot_l in state_i:
                continue  # already occupied
            new_state = tuple(sorted(
                [s for s in state_i if s != slot_k] + [slot_l]
            ))
            if new_state in basis_dict:
                j = basis_dict[new_state]
                H[i, j] += V_sym[k, l]

    # --- Off-diagonal: inter-cell Josephson coupling ---
    # Pair transfer: slot (c, k) -> slot (c', k) on neighboring cells
    # c-c' bond weight = adj_C4[c, c']
    for slot_from in state_i:
        c_from, k = slot_to_cell_mode(slot_from)
        for c_to in range(N_cells):
            if c_to == c_from:
                continue
            if adj_C4[c_from, c_to] < 0.5:
                continue
            slot_to = cell_mode_to_slot(c_to, k)
            if slot_to in state_i:
                continue
            new_state = tuple(sorted(
                [s for s in state_i if s != slot_from] + [slot_to]
            ))
            if new_state in basis_dict:
                j = basis_dict[new_state]
                # Symmetric coupling: count each bond once, and hermiticity
                # comes automatically because we iterate over all ordered
                # (c_from, c_to) pairs
                H[i, j] += E_J_fold

# Enforce Hermiticity to machine epsilon
H = 0.5 * (H + H.T)
herm_err = np.max(np.abs(H - H.T))
print(f"H dim = {dim}, Hermiticity error = {herm_err:.2e}")
print(f"H construction time: {time.time() - t_h:.2f} s")

# ============================================================
#  5. DIAGONALIZE
# ============================================================

print("\n" + "=" * 72)
print("DIAGONALIZATION")
print("=" * 72)
t_d = time.time()
evals, evecs = eigh(H)
print(f"Diagonalization: {time.time() - t_d:.2f} s")
print(f"E_min = {evals[0]:.6f}, E_max = {evals[-1]:.6f}")
print(f"Spectrum spread = {evals[-1] - evals[0]:.4f} M_KK")
print(f"Gap to first excited = {evals[1] - evals[0]:.6f}")
print(f"Level spacing at center = "
      f"{np.median(np.diff(evals)):.6f} M_KK")

# ============================================================
#  6. GGE REFERENCE STATE
# ============================================================
#
# The GGE is a product state in the Richardson-Gaudin conserved-charge
# basis. For the single-cell integrable sector, the R-G charges are the
# pair occupations on each mode. For a 4-cell system with finite E_J,
# the Josephson term breaks single-cell integrability but preserves the
# total N_pair and the total pair occupation per mode summed over cells
# (since the hopping conserves mode-k and transfers only between cells).
#
# Canonical GGE: thermal in H at T = T_acoustic, restricted to N_pair=2.
# This is the working definition used by S56 GGE-FABRIC and S62 GGE
# computations. At T_acoustic = 0.112 M_KK << Delta_BCS, the GGE is
# ground-state-dominated but has small thermal population in excited
# states.

beta = 1.0 / T_acoustic  # (local) inverse temperature
# Thermal weights
w_unnorm = np.exp(-beta * (evals - evals[0]))  # (local)
Z = np.sum(w_unnorm)  # (local)
w_therm = w_unnorm / Z  # (local)
print(f"\nbeta = 1/T_acoustic = {beta:.4f} M_KK^{{-1}}")
print(f"Ground-state thermal weight: {w_therm[0]:.6f}")
print(f"Effective thermal dim: "
      f"{1.0/np.sum(w_therm**2):.3f}")

# <n_{c,m}>_GGE: expectation value in the thermal state
# = sum_alpha w_therm[alpha] * <alpha| n_{c,m} |alpha>
# In the pair basis, n_{slot} = 1 if slot is in state_i, else 0.

n_gge = np.zeros(N_slots)
for alpha in range(dim):
    # Skip extremely small weights
    if w_therm[alpha] < 1e-15:
        continue
    psi_alpha = evecs[:, alpha]
    # For each slot, compute |<i|psi_alpha>|^2 for all i containing slot
    for i, state_i in enumerate(basis):
        p_i = np.abs(psi_alpha[i])**2
        if p_i < 1e-20:
            continue
        for slot in state_i:
            n_gge[slot] += w_therm[alpha] * p_i

# Sanity check: sum over all slots should equal N_pair
print(f"\nGGE occupation (should sum to {N_pair}): "
      f"sum = {np.sum(n_gge):.6f}")

# Reshape to (cells, modes)
n_gge_cm = n_gge.reshape(N_cells, N_modes)
print("\nGGE <n_{c,m}> by cell:")
for c in range(N_cells):
    print(f"  cell {c}: {np.round(n_gge_cm[c], 4)}")

# ============================================================
#  7. PREPARE PERTURBED STATE
# ============================================================
#
# The perturbation is delta_n_{c=1, m=B1} = +1 on cell 1.
# We pick the B1 mode as mode index 0 (lowest-energy mode of the B
# sector at the fold -- eps_fold[0] = 0, closest to the Fermi surface).
#
# We prepare a pure state |psi_0> which is a simultaneous eigenstate of
# n_{c=1, B1} with eigenvalue 1. Specifically: start from the BCS ground
# state (alpha=0), then apply P_{c=1, B1} (pair creation at that slot)
# and re-normalize. This gives a state with one pair pinned at
# (cell=1, B1) and the second pair distributed as in the ground state,
# but conditioned on cell=1 mode=B1 being occupied.
#
# Concretely: |psi_0> = P_{slot=8} |GS> / ||P_{slot=8} |GS>||
# where slot = cell*N_modes + mode = 1*8 + 0 = 8.
#
# This state IS a legitimate N_pair=2 state (both pairs present) and
# the perturbation is <n_{cell=1, B1}> = 1 - <n_{cell=1, B1}>_{GS,
# conditional} -- guaranteed to be an O(1) excess over the GGE value
# because the GGE has <n_{cell=1, B1}> ~ 1/4 (one pair delocalized) +
# thermal corrections.

print("\n" + "=" * 72)
print("PERTURBATION: localize one pair at (cell=1, B1)")
print("=" * 72)

PERT_CELL = 1  # (local)
PERT_MODE = 0  # (local) B1 is mode index 0 (eps_fold[0]=0)
PERT_SLOT = cell_mode_to_slot(PERT_CELL, PERT_MODE)
print(f"Perturbation slot = {PERT_SLOT} (cell={PERT_CELL}, mode={PERT_MODE})")
print(f"eps_fold[{PERT_MODE}] = {eps_fold[PERT_MODE]:.6e}")
print(f"GGE <n_slot={PERT_SLOT}> = {n_gge[PERT_SLOT]:.6f}")

# Projector P_{PERT_SLOT} in the N_pair=2 basis:
# state_i -> state_i if slot in state_i, else 0
psi_gs = evecs[:, 0]
psi_pert_raw = np.zeros(dim)
for i, state_i in enumerate(basis):
    if PERT_SLOT in state_i:
        psi_pert_raw[i] = psi_gs[i]

norm_raw = np.linalg.norm(psi_pert_raw)
print(f"||P_slot |GS>|| = {norm_raw:.6f}")
assert norm_raw > 1e-8, "GS has zero weight on perturbed slot"
psi_0 = psi_pert_raw / norm_raw

# Verify: <psi_0 | n_{PERT_SLOT} | psi_0> = 1 (pinned)
n_slot_psi0 = 0.0
for i, state_i in enumerate(basis):
    if PERT_SLOT in state_i:
        n_slot_psi0 += np.abs(psi_0[i])**2
print(f"<psi_0| n_{PERT_SLOT} |psi_0> = {n_slot_psi0:.10f} "
      f"(should be 1.0000000000)")
assert abs(n_slot_psi0 - 1.0) < 1e-10

# Energy of the perturbed state
E_psi0 = psi_0 @ H @ psi_0
E_gs = evals[0]
print(f"<psi_0|H|psi_0> = {E_psi0:.6f} M_KK")
print(f"E_gs           = {E_gs:.6f} M_KK")
print(f"Excess energy  = {E_psi0 - E_gs:.6f} M_KK")
print(f"(Compare Delta_BCS = {Delta_BCS:.6f} M_KK)")

# ============================================================
#  8. SPECTRAL DECOMPOSITION OF THE PERTURBATION
# ============================================================

print("\n" + "=" * 72)
print("SPECTRAL DECOMPOSITION")
print("=" * 72)

# c_alpha = <alpha | psi_0>
c_alpha = evecs.T @ psi_0
p_alpha = np.abs(c_alpha)**2
assert abs(np.sum(p_alpha) - 1.0) < 1e-10

# Effective number of eigenstates in the superposition
IPR = np.sum(p_alpha**2)  # (local) inverse participation ratio
N_eff = 1.0 / IPR  # (local)
print(f"IPR(psi_0) = {IPR:.6e}")
print(f"N_eff eigenstates in psi_0 = {N_eff:.3f}")
print(f"Total Fock dim = {dim}")

# Energy statistics of the perturbation
E_mean = np.sum(p_alpha * evals)
E_var = np.sum(p_alpha * (evals - E_mean)**2)
E_std = np.sqrt(E_var)
print(f"<E>_{{psi_0}} = {E_mean:.6f} M_KK")
print(f"sigma_E      = {E_std:.6f} M_KK  (energy spread)")
print(f"sigma_E / Delta_BCS = {E_std/Delta_BCS:.4f}")

# Quasi-particle energy reference
E_qp = Delta_BCS  # (local) BCS excitation gap
print(f"\nE_qp (reference) = Delta_BCS = {E_qp:.6f} M_KK")
print(f"(E_mean^2 - E_gs^2 - E_qp^2) / E_qp^2 = "
      f"{((E_mean - E_gs)**2 - E_qp**2) / E_qp**2:.4f}")
off_shell_ratio = abs((E_mean - E_gs)**2 - E_qp**2) / E_qp**2
off_shell = off_shell_ratio > 0.1  # (local) more than 10% off-shell
print(f"Off-shell flag (|ratio| > 0.1): {off_shell}")

# ============================================================
#  9. TIME EVOLUTION AND DECAY RATE
# ============================================================

print("\n" + "=" * 72)
print("TIME EVOLUTION")
print("=" * 72)

# Time grid: resolve the fastest mode and capture multi-bounce recurrence
# Fastest frequency: omega_max ~ max |E_alpha - E_beta| ~ spectrum width
omega_max = evals[-1] - evals[0]
dt_min = 0.1 / omega_max  # (local) Nyquist-ish
# Total time: target 20 Josephson hops
tau_J = 1.0 / (2 * np.pi * J_C2)  # (local) single-hop time (M_KK^{-1})
t_max = 40.0 * tau_J  # (local)
n_t = 2000  # (local)
dt = t_max / n_t
print(f"omega_max    = {omega_max:.4f} M_KK")
print(f"tau_Josephson= {tau_J:.4f} M_KK^{{-1}} (single-hop time)")
print(f"t_max        = {t_max:.4f} M_KK^{{-1}}")
print(f"dt           = {dt:.4e}  (n_t = {n_t})")

t_grid = np.linspace(0.0, t_max, n_t)

# Evolve in spectral basis: psi(t) = sum_alpha c_alpha e^{-i E_alpha t} |alpha>
# For each t, compute <psi(t)| n_{c,k} |psi(t)> for cells 0..3, mode B1
# Instead of rebuilding psi(t) at each t (expensive), compute the occupation
# matrix elements M_alpha_beta^{(slot)} = <alpha|n_slot|beta> once, then
# <n_slot>(t) = sum_{alpha, beta} c_alpha* c_beta e^{i(E_alpha - E_beta)t}
#                 M_{alpha beta}^{(slot)}
# which is a stationary-phase sum we evaluate by FFT.

# But for 4 slots (one per cell) x 2000 time points, direct construction
# of the occupation matrix per slot (dim^2 = 246016 entries) is cheap.
# Do it.

slots_monitor = [cell_mode_to_slot(c, PERT_MODE) for c in range(N_cells)]
print(f"Monitor slots (cell, B1): {slots_monitor}")

# Build n_slot matrices in the pair-basis Fock space (diagonal in basis)
# then rotate to eigenbasis: M = evecs.T @ diag(n) @ evecs
t_occ = time.time()
n_traces = np.zeros((N_cells, n_t))  # (local)
n_op = {}  # slot -> N x N eigen-basis matrix

for slot_idx, slot in enumerate(slots_monitor):
    # Diagonal operator n_slot in pair basis
    diag_n = np.zeros(dim)
    for i, state_i in enumerate(basis):
        if slot in state_i:
            diag_n[i] = 1.0
    # Rotate to eigenbasis
    M_eig = (evecs.T * diag_n) @ evecs  # (local) N x N matrix
    n_op[slot] = M_eig

    # <n_slot(t)> = c^dag M_eig(t) c
    # where M_eig(t) = D^dag M_eig D with D = diag(exp(-i E_alpha t))
    # Equivalently: sum_{ab} c_alpha^* c_beta e^{i(E_a - E_b)t} M_{ab}
    # For real H, c_alpha is real, so the trace is:
    # <n(t)> = sum_a c_a^2 M_{aa} + 2 sum_{a<b} c_a c_b M_{ab} cos((E_a-E_b)t)

    # Diagonal (static) part
    stat_part = np.sum(c_alpha**2 * np.diag(M_eig))

    # Off-diagonal (oscillating) part
    # For speed, only keep pairs where |c_a c_b M_{ab}| is not negligible
    c_outer = np.outer(c_alpha, c_alpha)
    AMP = c_outer * M_eig  # (local)
    # Mask upper triangle only
    iu = np.triu_indices(dim, k=1)
    w_ab = 2.0 * AMP[iu]  # (local) factor 2 for symmetric sum
    dE_ab = evals[iu[0]] - evals[iu[1]]  # (local)
    # Time series: static + sum_{a<b} w_ab * cos(dE_ab * t)
    # Vectorize over t_grid
    phase = np.outer(dE_ab, t_grid)  # (local) (N_pair, n_t)
    # Only keep terms with nontrivial amplitude
    mask = np.abs(w_ab) > 1e-14  # (local)
    w_ab_k = w_ab[mask]  # (local)
    phase_k = phase[mask]  # (local)
    osc_part = np.einsum('i,it->t', w_ab_k, np.cos(phase_k))  # (local)
    n_traces[slot_idx, :] = stat_part + osc_part

print(f"Time traces computed: {time.time()-t_occ:.2f} s")

# Subtract GGE equilibrium
delta_n_traces = np.zeros_like(n_traces)
for slot_idx, slot in enumerate(slots_monitor):
    delta_n_traces[slot_idx, :] = n_traces[slot_idx, :] - n_gge[slot]

# Record initial values
print("\nInitial values (should match the imposed perturbation at t=0):")
for c in range(N_cells):
    slot = slots_monitor[c]
    n0 = n_traces[c, 0]
    dn0 = delta_n_traces[c, 0]
    print(f"  cell {c}, slot {slot}: n(0) = {n0:.4f}, "
          f"delta_n(0) = {dn0:.4f}  (GGE = {n_gge[slot]:.4f})")

# ============================================================
# 10. EXTRACT DECAY RATE
# ============================================================

print("\n" + "=" * 72)
print("DECAY RATE EXTRACTION")
print("=" * 72)

# Envelope of delta_n on cell 1 (the perturbed cell)
signal_1 = delta_n_traces[PERT_CELL, :]
envelope_1 = np.abs(signal_1)

# Fit exponential to the initial decay:
# envelope(t) ~ A * exp(-Gamma_virt * t) + offset
# Use first ~half of t_grid to avoid recurrence
t_fit_end = n_t // 3
t_fit = t_grid[:t_fit_end]
env_fit = envelope_1[:t_fit_end]

# Log-linear fit where envelope is nonzero
mask_pos = env_fit > 1e-10
if np.sum(mask_pos) > 50:
    log_env = np.log(env_fit[mask_pos])
    slope, intercept = np.polyfit(t_fit[mask_pos], log_env, 1)
    Gamma_virt = -slope  # (local) decay rate (M_KK)
    A_fit = np.exp(intercept)  # (local)
    print(f"Log-linear fit on [0, {t_fit[-1]:.3f}]:")
    print(f"  A = {A_fit:.4f}")
    print(f"  Gamma_virt = {Gamma_virt:.6f} M_KK")
else:
    Gamma_virt = np.nan
    print("WARNING: envelope too close to zero for fit")

# Alternative: use the energy spread as a theoretical decay rate
Gamma_dephasing = E_std  # (local) natural dephasing rate
print(f"Gamma_dephasing (= sigma_E) = {Gamma_dephasing:.6f} M_KK")

# Josephson propagation rate
Gamma_J = 2 * np.pi * J_C2  # (local) angular frequency of hopping
Gamma_J_scalar = J_C2       # (local) raw coupling
print(f"Gamma_Josephson = {Gamma_J:.4f} M_KK  (= 2*pi*J_C2)")
print(f"J_C2 (raw)      = {J_C2:.4f} M_KK")

# Gate criterion: Gamma_virt vs J_C2 (use raw coupling for fair comparison)
ratio_virt_J = Gamma_virt / J_C2 if Gamma_virt > 0 else np.nan
print(f"\nGamma_virt / J_C2 = {ratio_virt_J:.4f}")
print(f"Gamma_dephasing / J_C2 = {Gamma_dephasing/J_C2:.4f}")

# === Long-time average and permanent component ===
# DC component: time-average of <n_{cell=1, B1}(t)> over the second half
# of the trajectory. If this is substantially above the GGE value, there
# is a permanent (conserved) component that does NOT decay.
half = n_t // 2
dc_signal = np.mean(delta_n_traces[PERT_CELL, half:])
dc_envelope = np.mean(envelope_1[half:])
print(f"\nLong-time mean <delta_n_{{cell=1, B1}}> (second half) = "
      f"{dc_signal:.6f}")
print(f"Long-time mean |delta_n_{{cell=1, B1}}|              = "
      f"{dc_envelope:.6f}")
# Initial excess
initial_excess = abs(delta_n_traces[PERT_CELL, 0])
dc_fraction = abs(dc_signal) / initial_excess if initial_excess > 0 else 0.0
print(f"DC fraction (permanent / initial): {dc_fraction:.6f}")

# === Power-law vs exponential comparison ===
# If the decay is dispersive (power-law), envelope(t) ~ t^{-alpha}.
# If exponential, envelope(t) ~ exp(-Gamma t).
# Fit both on the range where envelope is decreasing and above noise.
mask_fit = (t_grid > 0.1 * tau_J) & (envelope_1 > 0.01 * initial_excess)
n_fit_pts = int(np.sum(mask_fit))
if n_fit_pts > 20:
    t_fit2 = t_grid[mask_fit]
    env_fit2 = envelope_1[mask_fit]
    # Power law: log(env) = -alpha * log(t) + const
    log_t = np.log(t_fit2)
    log_env2 = np.log(env_fit2)
    alpha_pow, beta_pow = np.polyfit(log_t, log_env2, 1)
    alpha_pow = -alpha_pow
    pred_pow = np.exp(beta_pow) * t_fit2**(-alpha_pow)
    resid_pow = np.sum((log_env2 - np.log(pred_pow))**2)

    # Exponential: log(env) = -Gamma * t + const
    slope_e, int_e = np.polyfit(t_fit2, log_env2, 1)
    Gamma_exp = -slope_e
    pred_exp = np.exp(int_e) * np.exp(-Gamma_exp * t_fit2)
    resid_exp = np.sum((log_env2 - np.log(pred_exp))**2)

    print(f"\nPower-law fit: alpha = {alpha_pow:.4f}, resid = {resid_pow:.4f}")
    print(f"Exp      fit: Gamma = {Gamma_exp:.4f}, resid = {resid_exp:.4f}")
    if resid_pow < resid_exp:
        print("==> Power-law (dispersive) fits better")
        dispersive_dominant = True  # (local)
    else:
        print("==> Exponential (decohering) fits better")
        dispersive_dominant = False  # (local)
else:
    alpha_pow = np.nan
    Gamma_exp = Gamma_virt
    dispersive_dominant = False
    print("\nNot enough points for power-law vs exp comparison")

# ============================================================
# 11. SPATIAL PROPAGATION
# ============================================================

print("\n" + "=" * 72)
print("SPATIAL PROPAGATION")
print("=" * 72)

# For each cell 2, 3 (nearest/next-nearest neighbors of cell 1), measure
# the time at which delta_n reaches its peak, and the peak value.
print("Peak arrival times and amplitudes (cells 0..3):")
peak_times = np.zeros(N_cells)  # (local)
peak_amps = np.zeros(N_cells)  # (local)
for c in range(N_cells):
    sig = delta_n_traces[c, :]
    i_peak = int(np.argmax(np.abs(sig)))
    peak_times[c] = t_grid[i_peak]
    peak_amps[c] = sig[i_peak]
    print(f"  cell {c}: peak at t = {peak_times[c]:.4f} M_KK^{{-1}}, "
          f"delta_n_peak = {peak_amps[c]:+.4f}")

# Propagation velocity: distance = 1 bond (1 cell) / time-of-arrival
# Nearest neighbor of cell 1 on C_4 is cells 0 and 2 (adjacent).
# Next-nearest is cell 3 (opposite).
nn_cells = [0, 2]  # (local)
nnn_cells = [3]  # (local)

# Arrival time = first time at which |delta_n| exceeds 10% of cell 1's
# initial value
threshold = 0.10 * abs(delta_n_traces[PERT_CELL, 0])  # (local)
print(f"\nArrival threshold = {threshold:.4f}")
arrival_times = np.full(N_cells, np.nan)
for c in range(N_cells):
    sig_abs = np.abs(delta_n_traces[c, :])
    # Skip the source cell
    if c == PERT_CELL:
        arrival_times[c] = 0.0
        continue
    above = np.where(sig_abs > threshold)[0]
    if len(above) > 0:
        arrival_times[c] = t_grid[above[0]]
    print(f"  cell {c}: arrival time = {arrival_times[c]:.4f} M_KK^{{-1}}")

# Effective propagation speed (1 cell hop per arrival)
if not np.isnan(arrival_times[0]) and arrival_times[0] > 0:
    v_prop = 1.0 / arrival_times[0]  # (local) M_KK (cells per time)
    print(f"v_propagation (cell 0) = {v_prop:.4f} M_KK (cells/M_KK^{{-1}})")
else:
    v_prop = np.nan

# ============================================================
# 12. DECOMPOSITION INTO R-G CONSERVED CHARGES
# ============================================================

print("\n" + "=" * 72)
print("R-G CONSERVED CHARGE DECOMPOSITION")
print("=" * 72)
#
# The R-G conserved charges on the single-cell integrable sector are
# the pair-occupation numbers n_k = sum_c n_{c,k} (for each mode k,
# summed over cells -- this is preserved by inter-cell Josephson
# hopping because hopping transfers slot (c,k) <-> (c',k)).
#
# We test: is psi_0 a simultaneous eigenstate of the {N_k} operators?
# If yes, then psi_0 lives on a single R-G charge sector and its decay
# is pure intra-sector dephasing (INFO verdict).
#
# N_k = sum_c n_{c,k}. Each pair basis state |i> has N_k = (number of
# slots (c, k) in state_i).

print("Mode-occupation profile of psi_0:")
N_k_expect = np.zeros(N_modes)
for k in range(N_modes):
    slots_k = [cell_mode_to_slot(c, k) for c in range(N_cells)]
    n_k_val = 0.0
    for i, state_i in enumerate(basis):
        count_k = sum(1 for s in state_i if s in slots_k)
        n_k_val += np.abs(psi_0[i])**2 * count_k
    N_k_expect[k] = n_k_val
    print(f"  <N_k={k}> = {n_k_val:.6f}")

print(f"sum_k <N_k> = {np.sum(N_k_expect):.6f} (should be {N_pair})")

# Variance of N_k: if psi_0 is an eigenstate of N_k, variance = 0
print("\nN_k variance (should be 0 if R-G eigenstate):")
N_k_var = np.zeros(N_modes)
for k in range(N_modes):
    slots_k = [cell_mode_to_slot(c, k) for c in range(N_cells)]
    n_k_sq = 0.0
    for i, state_i in enumerate(basis):
        count_k = sum(1 for s in state_i if s in slots_k)
        n_k_sq += np.abs(psi_0[i])**2 * count_k**2
    N_k_var[k] = n_k_sq - N_k_expect[k]**2
    print(f"  Var(N_k={k}) = {N_k_var[k]:.6e}")

max_Nk_var = np.max(N_k_var)
print(f"\nMax R-G charge variance = {max_Nk_var:.6e}")
rg_exact = max_Nk_var < 1e-12  # (local)
print(f"R-G decomposition exact to machine epsilon: {rg_exact}")

# Decompose psi_0 into (1) part conserved by {N_k} and (2) the rest
# The "conserved part" is the component that IS a simultaneous eigenstate
# of the dominant N_k charges. Since psi_0 has fixed total N_pair, and
# may not have fixed individual N_k, the conserved-charge projection
# onto the (N_0, ..., N_7) sector containing the largest weight gives
# the "stable" component.
#
# Find the dominant (N_0, ..., N_7) pattern by computing, for each basis
# state, its signature (c_0, ..., c_7) where c_k = count of (c,k) in state.
# Weighted histogram over basis states.

sig_weights = {}
for i, state_i in enumerate(basis):
    sig = tuple(sum(1 for s in state_i if s % N_modes == k)
                for k in range(N_modes))
    w = np.abs(psi_0[i])**2
    sig_weights[sig] = sig_weights.get(sig, 0.0) + w

sigs_sorted = sorted(sig_weights.items(), key=lambda x: -x[1])
print("\nTop R-G charge-sector weights of psi_0:")
for sig, w in sigs_sorted[:10]:
    print(f"  {sig}: weight = {w:.6f}")
top_sig_weight = sigs_sorted[0][1]
print(f"\nTop sector weight (stable fraction): {top_sig_weight:.6f}")

# "Decaying" fraction = 1 - top sector weight
decay_frac = 1.0 - top_sig_weight  # (local)
print(f"Decaying fraction (non-dominant sectors) = {decay_frac:.6f}")

# ============================================================
# 13. YUKAWA SCREENING LENGTH
# ============================================================

print("\n" + "=" * 72)
print("YUKAWA SCREENING LENGTH")
print("=" * 72)
# xi_virt = c_{BA} / Gamma_virt
# where c_{BA} is the Bogoliubov acoustic sound speed (Goldstone mode)
# and Gamma_virt is the decay rate extracted above. Compare to l_Planck.

c_BA = c_Gold  # (local) Goldstone sound speed (M_KK units)
if Gamma_virt > 0 and not np.isnan(Gamma_virt):
    xi_virt_MKK = c_BA / Gamma_virt  # (local) in M_KK^{-1}
    xi_virt_GeV = xi_virt_MKK / M_KK  # (local) in GeV^{-1}
    xi_virt_m = xi_virt_GeV * 1.973269804e-16  # (local) GeV^{-1} to m
    print(f"c_BA (Goldstone)  = {c_BA} M_KK")
    print(f"Gamma_virt        = {Gamma_virt:.6f} M_KK")
    print(f"xi_virt = c_BA/Gamma_virt = {xi_virt_MKK:.4f} M_KK^{{-1}}")
    print(f"xi_virt (SI)      = {xi_virt_m:.4e} m")
    print(f"l_Planck          = {l_Planck:.4e} m")
    ratio_xi = xi_virt_m / l_Planck  # (local)
    print(f"xi_virt / l_Planck= {ratio_xi:.4e}")
else:
    xi_virt_MKK = np.nan
    xi_virt_m = np.nan
    ratio_xi = np.nan
    print("xi_virt undefined (Gamma_virt not extracted)")

# ============================================================
# 14. GATE VERDICT
# ============================================================

print("\n" + "=" * 72)
print("GATE VERDICT: VIRTUAL-PARTICLE-73B")
print("=" * 72)

# Criteria:
# PASS: Gamma_virt > J_C2 AND off_shell
# FAIL: Gamma_virt < J_C2
# INFO: R-G decomposition exact (max_Nk_var < 1e-12)

if rg_exact:
    verdict = "INFO"
    reason = ("R-G conserved charge decomposition exact to machine "
              "epsilon: perturbation is a GGE rearrangement, not a "
              "decaying fluctuation.")
elif not np.isnan(Gamma_virt) and Gamma_virt > J_C2 and off_shell:
    verdict = "PASS"
    reason = (f"Gamma_virt = {Gamma_virt:.4f} > J_C2 = {J_C2:.4f} "
              f"and off-shell ratio {off_shell_ratio:.3f} > 0.1")
elif not np.isnan(Gamma_virt) and Gamma_virt < J_C2:
    verdict = "FAIL"
    reason = (f"Gamma_virt = {Gamma_virt:.4f} < J_C2 = {J_C2:.4f}: "
              f"perturbation propagates as a stable excitation.")
else:
    verdict = "INFO"
    reason = "Intermediate/ambiguous regime; further decomposition required."

print(f"Verdict: {verdict}")
print(f"Reason:  {reason}")

# ============================================================
# 15. PLOT
# ============================================================

print("\n" + "=" * 72)
print("PLOTTING")
print("=" * 72)

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Panel 1: delta_n traces for all 4 cells
ax = axes[0, 0]
colors = ['C3', 'C0', 'C2', 'C1']
labels = [f'cell {c}' + (' (source)' if c == PERT_CELL else '')
          for c in range(N_cells)]
for c in range(N_cells):
    ax.plot(t_grid, delta_n_traces[c, :], color=colors[c],
            label=labels[c], lw=1.5, alpha=0.9)
ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel(r'$t \; [M_{KK}^{-1}]$')
ax.set_ylabel(r'$\delta n_{c, B_1}(t)$')
ax.set_title('Single-Mode Perturbation Decay (cell=1, mode B1)')
ax.legend(fontsize=9, loc='upper right')
ax.grid(True, alpha=0.3)

# Panel 2: Envelope + fit
ax = axes[0, 1]
ax.semilogy(t_grid, envelope_1, color='C3', lw=1.3,
            label=r'$|\delta n_{1,B_1}|$')
if not np.isnan(Gamma_virt):
    t_model = t_grid[:t_fit_end]
    model = A_fit * np.exp(-Gamma_virt * t_model)
    ax.semilogy(t_model, model, 'k--', lw=1.5,
                label=rf'$\Gamma_{{virt}} = {Gamma_virt:.3f}$')
ax.axhline(abs(delta_n_traces[PERT_CELL, 0]) * np.exp(-1),
           color='gray', ls=':', label='1/e level')
ax.set_xlabel(r'$t \; [M_{KK}^{-1}]$')
ax.set_ylabel(r'$|\delta n_{1, B_1}(t)|$')
ax.set_title('Decay Envelope (semi-log)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which='both')

# Panel 3: Spectral decomposition
ax = axes[1, 0]
ax.stem(evals - evals[0], p_alpha, basefmt=' ',
        linefmt='C0-', markerfmt='C0o')
ax.axvline(Delta_BCS, color='r', ls='--', alpha=0.7,
           label=rf'$\Delta_{{BCS}} = {Delta_BCS:.3f}$')
ax.axvline(E_mean - E_gs, color='k', ls=':', alpha=0.7,
           label=rf'$\langle E - E_{{gs}}\rangle = '
                 rf'{E_mean - E_gs:.3f}$')
ax.set_xlabel(r'$E_\alpha - E_{gs} \; [M_{KK}]$')
ax.set_ylabel(r'$|c_\alpha|^2$')
ax.set_title(rf'Spectral decomposition of $|\psi_0\rangle$ '
             rf'($N_{{eff}} = {N_eff:.1f}$)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 4: R-G charge histogram
ax = axes[1, 1]
top_sigs = sigs_sorted[:8]
labels_sig = [''.join(str(x) for x in s[0]) for s in top_sigs]
weights_sig = [s[1] for s in top_sigs]
ax.bar(range(len(top_sigs)), weights_sig, color='C2',
       edgecolor='k')
ax.set_xticks(range(len(top_sigs)))
ax.set_xticklabels(labels_sig, rotation=45, ha='right', fontsize=8)
ax.set_xlabel('R-G charge sector $(N_0, ..., N_7)$')
ax.set_ylabel('Weight in $|\\psi_0\\rangle$')
ax.set_title(f'Conserved-charge decomposition (top weight '
             f'{top_sig_weight:.3f})')
ax.grid(True, alpha=0.3, axis='y')

plt.suptitle(f'VIRTUAL-PARTICLE-73B: verdict = {verdict}',
             fontsize=13, fontweight='bold')
plt.tight_layout()

png_path = os.path.join(data_dir, 's73b_virtual_particle.png')
plt.savefig(png_path, dpi=120, bbox_inches='tight')
plt.close(fig)
print(f"Figure saved: {png_path}")

# ============================================================
# 16. SAVE RESULTS
# ============================================================

print("\n" + "=" * 72)
print("SAVING RESULTS")
print("=" * 72)

npz_path = os.path.join(data_dir, 's73b_virtual_particle.npz')
np.savez(
    npz_path,
    gate_name='VIRTUAL-PARTICLE-73B',
    gate_verdict=verdict,
    gate_reason=reason,
    # System parameters
    N_modes=N_modes, N_cells=N_cells, N_slots=N_slots, N_pair=N_pair,
    dim=dim,
    c4_vertices=np.array(c4_verts, dtype=int),
    # Spectrum
    evals=evals,
    E_gs=evals[0],
    E_psi0=E_psi0,
    spectrum_spread=evals[-1] - evals[0],
    # Hamiltonian parameters (reference)
    eps_fold=eps_fold,
    V_fold=V_fold,
    E_J_fold=E_J_fold,
    Delta_BCS=Delta_BCS,
    J_C2=J_C2,
    T_acoustic=T_acoustic,
    # GGE reference
    n_gge_slot=n_gge,
    n_gge_cell_mode=n_gge_cm,
    beta_GGE=beta,
    w_therm=w_therm,
    # Perturbation
    pert_cell=PERT_CELL,
    pert_mode=PERT_MODE,
    pert_slot=PERT_SLOT,
    n_slot_psi0=n_slot_psi0,
    # Spectral decomposition
    c_alpha=c_alpha,
    p_alpha=p_alpha,
    IPR=IPR,
    N_eff=N_eff,
    E_mean=E_mean,
    E_std=E_std,
    off_shell_ratio=off_shell_ratio,
    off_shell=off_shell,
    # Time evolution
    t_grid=t_grid,
    n_traces=n_traces,
    delta_n_traces=delta_n_traces,
    envelope_1=envelope_1,
    # Decay rate
    Gamma_virt=Gamma_virt,
    Gamma_dephasing=Gamma_dephasing,
    Gamma_J=Gamma_J,
    Gamma_J_scalar=J_C2,
    ratio_virt_J=ratio_virt_J,
    # Long-time / DC component
    dc_signal=dc_signal,
    dc_envelope=dc_envelope,
    dc_fraction=dc_fraction,
    initial_excess=initial_excess,
    # Power-law vs exponential
    alpha_pow=alpha_pow,
    Gamma_exp=Gamma_exp,
    dispersive_dominant=dispersive_dominant,
    # Propagation
    peak_times=peak_times,
    peak_amps=peak_amps,
    arrival_times=arrival_times,
    v_prop=v_prop,
    # R-G decomposition
    N_k_expect=N_k_expect,
    N_k_var=N_k_var,
    max_Nk_var=max_Nk_var,
    rg_exact=rg_exact,
    top_sig_weight=top_sig_weight,
    decay_frac=decay_frac,
    # Yukawa length
    c_BA=c_BA,
    xi_virt_MKK=xi_virt_MKK,
    xi_virt_m=xi_virt_m,
    l_Planck=l_Planck,
    ratio_xi_Planck=ratio_xi,
    # Timing
    elapsed_s=time.time() - t_start,
)
print(f"Data saved: {npz_path}")

print(f"\nTotal runtime: {time.time() - t_start:.2f} s")
print("=" * 72)
print(f"GATE VERDICT: VIRTUAL-PARTICLE-73B = {verdict}")
print("=" * 72)
