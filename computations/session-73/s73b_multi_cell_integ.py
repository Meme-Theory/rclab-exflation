#!/usr/bin/env python3
"""
MULTI-CELL-INTEG-73B: Multi-Cell Level Statistics at N_pair = 4
================================================================

Gate: MULTI-CELL-INTEG-73B
  PASS: <r> < 0.45 (Poisson, integrable)
  FAIL: <r> > 0.50 (Wigner-Dyson, chaotic)
  INFO: <r> in [0.45, 0.50] (intermediate)

Physics:
  Richardson-Gaudin integrability is PERMANENT at single-cell (S56).
  S63 found Poisson (<r> = 0.385) at N_pair = 2 on 2-cell and 4-cell
  sublattices of CG(24). S73B W2-E found <r> = 0.4625 (intermediate)
  for SINGLE-cell N_pair=4 BCS Hamiltonian.

  Test: does inter-cell Josephson coupling drive multi-cell N_pair=4
  toward Poisson (protected) or GOE (chaos)?

Method:
  Z_4 orbit-based symmetry reduction to avoid dense 35960x35960 matrices.
  For each basis state, compute its orbit under the Z_4 cyclic group.
  The orbit representative and momentum-adapted basis vectors are then
  built explicitly, keeping everything SPARSE.

  1. Load CG(24), extract C_4 ring
  2. Build pair Fock space C(32, 4) = 35960 states
  3. Compute Z_4 orbits: each orbit of size 4, 2, or 1
  4. For each momentum k in {0, pi/2, pi, 3pi/2}:
       - Build symmetry-adapted states |k, orbit>
       - Construct H_k in this basis (sparse)
       - Diagonalize (dense, per sector ~ 9000 x 9000)
  5. Compute <r> per sector

Session: S73B W3-B
Agent: landau-condensed-matter-theorist
"""

import sys
import os
import time
import numpy as np
from itertools import combinations
from math import comb as mcomb
from scipy.sparse import lil_matrix, csr_matrix
from scipy.linalg import eigh, eigvalsh
from scipy.optimize import minimize_scalar
from scipy.special import gamma as gamma_fn
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Import canonical constants ===
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, N_dof_BCS, M_KK,
    Delta_BCS, Delta_0_OES,
    E_B1, E_B2_mean, E_B3_mean,
    J_C2, J_su2, J_u1, T_acoustic,
    N_cells as N_cells_fabric,
)

data_dir = os.path.dirname(os.path.abspath(__file__))

t_start = time.time()

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

print("=" * 72)
print("MULTI-CELL-INTEG-73B: Level Statistics at N_pair = 4")
print("=" * 72)

cg24_data = np.load(os.path.join(data_dir, 's60_entangle_cg24.npz'), allow_pickle=True)
adj_cg24 = cg24_data['adj'].astype(float)
N_vertices_cg24 = int(cg24_data['N_vertices'])
degree_cg24 = int(cg24_data['degree'])

d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']
V_fold = d56['V_fold']
E_J_S56 = float(d56['E_J_fold'])  # (local)

E_J = E_J_S56  # (local)

N_modes = len(eps_fold)  # 8
N_pair = 4               # (local)
N_cells = 4              # (local)

print(f"CG(24): {N_vertices_cg24} vertices, degree {degree_cg24}")
print(f"N_modes/cell = {N_modes}, N_pair = {N_pair}, N_cells = {N_cells}")
print(f"E_J = {E_J:.6f} M_KK")
print(f"Delta_BCS = {Delta_BCS:.6f} M_KK")
print(f"E_J/Delta = {E_J/Delta_BCS:.2f}")
print(f"eps_fold = {eps_fold}")
print(f"V_fold diagonal = {np.diag(V_fold)}")
print()

# =====================================================================
#  2. EXTRACT C_4 RING SUBGRAPH FROM CG(24)
# =====================================================================

print("=" * 72)
print("C_4 RING EXTRACTION")
print("=" * 72)

def find_C4(adj, n):
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
assert c4_verts is not None
v0, v1, v2, v3 = c4_verts
assert adj_cg24[v0, v1] > 0.5
assert adj_cg24[v1, v2] > 0.5
assert adj_cg24[v2, v3] > 0.5
assert adj_cg24[v3, v0] > 0.5
assert adj_cg24[v0, v2] < 0.5
assert adj_cg24[v1, v3] < 0.5
print(f"C_4 ring in CG(24): vertices {c4_verts}")

# C_4 ring adjacency: 0-1, 1-2, 2-3, 3-0
adj_C4 = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
], dtype=float)

# =====================================================================
#  3. PAIR FOCK SPACE AND Z_4 ORBITS
# =====================================================================

print("\n" + "=" * 72)
print("PAIR FOCK SPACE AND Z_4 ORBITS")
print("=" * 72)

N_slots = N_modes * N_cells  # 32   # (local)
dim_total = mcomb(N_slots, N_pair)  # 35960  # (local)
print(f"N_slots = {N_slots}, dim_total = {dim_total}")

t_basis = time.time()
# Build basis efficiently using numpy-indexed tuples
basis = list(combinations(range(N_slots), N_pair))
state_index = {s: i for i, s in enumerate(basis)}
print(f"Basis built in {time.time() - t_basis:.1f} s")

def translate_state(slots, n_modes, n_cells):
    """Apply Z_4 translation cell j -> cell (j+1) mod N_cells."""
    new_slots = []
    for s in slots:
        m = s % n_modes
        c = s // n_modes
        c_new = (c + 1) % n_cells
        new_slots.append(c_new * n_modes + m)
    return tuple(sorted(new_slots))


# Compute orbits: for each state, find its Z_4 orbit
# Each orbit has period p where p | 4, so p in {1, 2, 4}.
# p = 4: generic orbit (4 states)
# p = 2: states invariant under T^2 (2 states in orbit)
# p = 1: states invariant under T (1 state in orbit)
print("Computing Z_4 orbits...")
t_orbit = time.time()

orbit_reps = []          # List of orbit representatives (tuples)
orbit_rep_index = {}     # orbit_id -> index in orbit_reps
orbit_of_state = np.full(dim_total, -1, dtype=np.int64)  # state -> orbit id
orbit_phase = np.zeros(dim_total, dtype=np.int8)  # n such that T^n |rep> = |state>
orbit_periods = []       # Period of each orbit (1, 2, or 4)

visited = np.zeros(dim_total, dtype=bool)

for i in range(dim_total):
    if visited[i]:
        continue
    state = basis[i]
    orbit_id = len(orbit_reps)
    orbit_reps.append(state)
    orbit_rep_index[state] = orbit_id

    # Apply T repeatedly
    cur_state = state
    orbit_indices = [i]
    for n in range(1, 4):
        cur_state = translate_state(cur_state, N_modes, N_cells)
        if cur_state == state:
            # Orbit closes at period n
            break
        idx = state_index[cur_state]
        orbit_indices.append(idx)

    period = len(orbit_indices)
    orbit_periods.append(period)

    for n, idx in enumerate(orbit_indices):
        visited[idx] = True
        orbit_of_state[idx] = orbit_id
        orbit_phase[idx] = n

orbit_periods = np.array(orbit_periods, dtype=np.int8)
n_orbits = len(orbit_reps)

p1 = np.sum(orbit_periods == 1)
p2 = np.sum(orbit_periods == 2)
p4 = np.sum(orbit_periods == 4)
print(f"Orbit counts: p=1: {p1}, p=2: {p2}, p=4: {p4}")
print(f"Total orbits: {n_orbits}")
print(f"Sanity check: 1*{p1} + 2*{p2} + 4*{p4} = {p1 + 2*p2 + 4*p4} "
      f"(should be {dim_total})")
assert p1 + 2*p2 + 4*p4 == dim_total
print(f"Orbit computation: {time.time() - t_orbit:.1f} s")

# =====================================================================
#  4. SECTOR DIMENSIONS
# =====================================================================
#
# A momentum sector k = 2*pi*n/N_cells contains an orbit of period p iff
# the symmetry sum Sum_{m=0}^{p-1} exp(-i*k*m) is nonzero.
# Equivalently: n*p must be a multiple of N_cells = 4.
#
#   period 1 (p=1): only n=0 (T|rep> = |rep> ≡ sector k=0)
#   period 2 (p=2): n*2 ≡ 0 mod 4 => n in {0, 2}, i.e., k=0 and k=pi
#   period 4 (p=4): n*4 ≡ 0 mod 4 for all n => all 4 sectors
#
# Each compatible orbit contributes exactly ONE state to that sector.
# Sector dimensions:
#   n=0 (k=0):      p1 + p2 + p4
#   n=1 (k=pi/2):   0  + 0  + p4
#   n=2 (k=pi):     0  + p2 + p4
#   n=3 (k=3pi/2):  0  + 0  + p4
#
# For a real Hamiltonian, n=1 and n=3 sectors give identical spectra
# (complex conjugate pair). We diagonalize each as a complex Hermitian.

dim_k0 = p1 + p2 + p4   # (local)
dim_k1 = p4             # (local)
dim_k2 = p2 + p4        # (local)
dim_k3 = p4             # (local)
print(f"\nSector dimensions:")
print(f"  k=0:     {dim_k0}")
print(f"  k=pi/2:  {dim_k1}")
print(f"  k=pi:    {dim_k2}")
print(f"  k=3pi/2: {dim_k3}")
print(f"  Sum:     {dim_k0 + dim_k1 + dim_k2 + dim_k3} (should be {dim_total})")
assert dim_k0 + dim_k1 + dim_k2 + dim_k3 == dim_total

# Build orbit index list per sector
# For each sector, list the orbit IDs that contribute
orbit_in_sector = {0: [], 1: [], 2: [], 3: []}  # (local)
for oid, p in enumerate(orbit_periods):
    if p == 1:
        # period-1 orbits: only k=0
        orbit_in_sector[0].append(oid)
    elif p == 2:
        # period-2 orbits: k=0 and k=pi
        orbit_in_sector[0].append(oid)
        orbit_in_sector[2].append(oid)
    elif p == 4:
        # period-4 orbits: all 4 sectors
        for k in range(4):
            orbit_in_sector[k].append(oid)

# Inverse: orbit -> index within sector
orbit_to_sector_idx = {0: {}, 1: {}, 2: {}, 3: {}}  # (local)
for k in range(4):
    for idx, oid in enumerate(orbit_in_sector[k]):
        orbit_to_sector_idx[k][oid] = idx

# =====================================================================
#  5. HAMILTONIAN MATRIX ELEMENTS IN ORBIT BASIS
# =====================================================================
#
# The symmetry-adapted basis vector in sector k for orbit o is:
#   |k, o> = (1/sqrt(N_o)) * Sum_{n=0}^{period-1} exp(-2*pi*i*k*n/4) * T^n|rep_o>
# where N_o = period (normalization).
#
# We need a bit more care: the phase factor for state m = T^n |rep> in sector k is
# exp(-2*pi*i*k*n/4) / sqrt(period).
#
# The matrix element <k, o' | H | k, o> is then computed by:
#   1. For each state in orbit o with its phase factor,
#   2. Apply H to generate off-diagonal terms (intra-cell + Josephson),
#   3. Find which orbit each new state belongs to,
#   4. Accumulate with the conjugate phase of the target.
#
# Because H commutes with T, the result is independent of which state in orbit o
# we start from -- but we need to sum over ALL states in the orbit to get the
# correctly normalized matrix element. Equivalently, we start from the rep and
# the accumulated factor picks up the phase of the target orbit element.

def hamiltonian_action(slots, eps, V, E_J_val, adj, n_cells, n_modes, n_pair):
    """
    Apply H to state |slots> and return list of (new_state, amplitude).
    Includes diagonal kinetic and off-diagonal scattering terms.
    Off-diagonal comes from intra-cell pair scattering (V) and
    inter-cell Josephson tunneling (E_J).
    """
    contributions = []  # (local)

    # Diagonal
    E_diag = 0.0  # (local)
    for s in slots:
        m = s % n_modes
        E_diag += 2.0 * eps[m]
        E_diag -= V[m, m]

    for a_idx in range(n_pair):
        for b_idx in range(a_idx + 1, n_pair):
            s_a = slots[a_idx]
            s_b = slots[b_idx]
            m_a, c_a = s_a % n_modes, s_a // n_modes
            m_b, c_b = s_b % n_modes, s_b // n_modes
            if c_a == c_b:
                E_diag += V[m_a, m_b]

    contributions.append((tuple(sorted(slots)), E_diag))

    # Off-diagonal
    for p_idx in range(n_pair):
        s_p = slots[p_idx]
        m_p = s_p % n_modes
        c_p = s_p // n_modes

        other_slots = list(slots[:p_idx]) + list(slots[p_idx+1:])
        other_set_p = set(other_slots)

        # Intra-cell scattering: scatter pair m_p -> k in same cell
        for k in range(n_modes):
            if k == m_p:
                continue
            new_slot = c_p * n_modes + k
            if new_slot in other_set_p:
                continue
            new_state = tuple(sorted(other_slots + [new_slot]))
            contributions.append((new_state, -V[k, m_p]))

        # Josephson tunneling: pair -> any mode in adjacent cell
        for c_target in range(n_cells):
            if adj[c_p, c_target] < 0.5:
                continue
            for l in range(n_modes):
                new_slot = c_target * n_modes + l
                if new_slot == s_p:
                    continue
                if new_slot in other_set_p:
                    continue
                new_state = tuple(sorted(other_slots + [new_slot]))
                contributions.append((new_state, -E_J_val / 2.0))

    return contributions


def build_sector_hamiltonian(k_idx, eps, V, E_J_val, adj,
                             orbit_reps, orbit_periods, orbit_of_state,
                             orbit_phase, state_index, basis,
                             orbit_in_sector, orbit_to_sector_idx,
                             n_cells, n_modes, n_pair):
    """
    Build the Hamiltonian matrix in the sector k_idx (n=0,1,2,3).
    k_actual = 2*pi*k_idx/4.
    Returns a complex Hermitian dense matrix of size dim_k x dim_k.
    """
    omega = np.exp(-2j * np.pi * k_idx / 4)  # phase per translation step  # (local)

    sector_orbits = orbit_in_sector[k_idx]
    dim_k = len(sector_orbits)  # (local)

    H_k = np.zeros((dim_k, dim_k), dtype=np.complex128)

    for sec_idx, oid in enumerate(sector_orbits):
        rep = orbit_reps[oid]
        period_o = orbit_periods[oid]

        # Apply H to the representative
        contribs = hamiltonian_action(rep, eps, V, E_J_val, adj,
                                       n_cells, n_modes, n_pair)

        # For each resulting state, determine its orbit and phase within that orbit
        for new_state, amp in contribs:
            if amp == 0.0:
                continue
            new_idx = state_index[new_state]
            new_oid = orbit_of_state[new_idx]
            new_phase = orbit_phase[new_idx]
            new_period = orbit_periods[new_oid]

            # Check if this orbit belongs to sector k
            # An orbit of period p contributes to sector k iff k_idx*p ≡ 0 mod 4
            # period 1: only k=0; period 2: k in {0, 2}; period 4: all k
            if new_period == 1 and k_idx != 0:
                continue
            if new_period == 2 and k_idx not in (0, 2):
                continue
            # (period 4 always included)

            # Matrix element: <k, new_o | H | k, o>
            # |k, o> = (1/sqrt(period_o)) * Sum_n omega^n * T^n|rep_o>
            # When we apply H to |rep_o>, we get states in various orbits.
            # The projection onto |k, new_o> extracts the coefficient of
            # the representative of new_o, with appropriate phase.
            #
            # The amplitude becomes:
            #   H_k[new_sec_idx, sec_idx] += (1/sqrt(period_o * new_period))
            #                                * sum over orbit members of source
            #                                * amp * omega^{-new_phase}
            #
            # Since H commutes with T, applying H to any state in orbit o gives
            # a "shifted" version of what applying H to the rep gives. Summing
            # over orbit members produces a factor of period_o.
            # The normalization (1/sqrt(period_o * new_period)) * period_o
            # = sqrt(period_o / new_period).

            new_sec_idx = orbit_to_sector_idx[k_idx][new_oid]

            norm = np.sqrt(period_o / new_period)  # (local)
            phase_factor = omega**(-int(new_phase))  # conjugate phase  # (local)

            H_k[new_sec_idx, sec_idx] += amp * norm * phase_factor

    # Symmetrize (ensure Hermitian)
    H_k = 0.5 * (H_k + H_k.conj().T)

    return H_k


# =====================================================================
#  6. BUILD AND DIAGONALIZE EACH SECTOR
# =====================================================================

print("\n" + "=" * 72)
print("BUILDING AND DIAGONALIZING SECTOR HAMILTONIANS")
print("=" * 72)

results = {}  # (local)
sector_names = {0: "k=0", 1: "k=pi/2", 2: "k=pi", 3: "k=3pi/2"}  # (local)

for k_idx in range(4):
    name = sector_names[k_idx]
    dim_k = len(orbit_in_sector[k_idx])  # (local)
    print(f"\n--- Sector {name}: dim = {dim_k} ---")

    t_sec = time.time()

    # Physical Hamiltonian
    H_k = build_sector_hamiltonian(
        k_idx, eps_fold, V_fold, E_J, adj_C4,
        orbit_reps, orbit_periods, orbit_of_state,
        orbit_phase, state_index, basis,
        orbit_in_sector, orbit_to_sector_idx,
        N_cells, N_modes, N_pair
    )
    t_build_k = time.time() - t_sec
    print(f"  H_k built in {t_build_k:.1f} s")

    # Hermiticity check
    herm_err = np.max(np.abs(H_k - H_k.conj().T))
    print(f"  Hermiticity: max|H - H^dag| = {herm_err:.2e}")

    # Diagonalize
    t_diag = time.time()
    evals_phys = eigvalsh(H_k)
    print(f"  Diagonalized in {time.time() - t_diag:.1f} s")
    print(f"  E range: [{evals_phys[0]:.4f}, {evals_phys[-1]:.4f}]")

    # Control: E_J = 0
    t_ctrl = time.time()
    H_k_ctrl = build_sector_hamiltonian(
        k_idx, eps_fold, V_fold, 0.0, adj_C4,
        orbit_reps, orbit_periods, orbit_of_state,
        orbit_phase, state_index, basis,
        orbit_in_sector, orbit_to_sector_idx,
        N_cells, N_modes, N_pair
    )
    evals_ctrl = eigvalsh(H_k_ctrl)
    print(f"  Control built+diagonalized in {time.time() - t_ctrl:.1f} s")

    del H_k, H_k_ctrl

    results[name] = {
        'evals': evals_phys,
        'evals_ctrl': evals_ctrl,
        'dim': dim_k,
        'k_idx': k_idx,
    }

# =====================================================================
#  7. LEVEL SPACING STATISTICS
# =====================================================================

print("\n" + "=" * 72)
print("LEVEL SPACING STATISTICS")
print("=" * 72)

def compute_r_statistic(eigenvalues, unfold_degree=5):
    E = np.sort(eigenvalues)
    N_E = len(E)  # (local)

    if N_E < 10:
        return np.nan, np.array([]), np.array([])

    # Polynomial unfolding
    N_stair = np.arange(1, N_E + 1)  # (local)
    deg = min(unfold_degree, N_E - 2)  # (local)
    if deg < 1:
        deg = 1  # (local)
    poly = np.polyfit(E, N_stair, deg=deg)  # (local)
    E_unf = np.polyval(poly, E)  # (local)

    s = np.diff(E_unf)  # (local)
    s = s[s > 1e-14]

    if len(s) < 3:
        return np.nan, np.array([]), s

    r_n = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])  # (local)

    return np.mean(r_n), r_n, s


def brody_nll(eta, spacings):
    if eta < 0 or eta > 2:
        return 1e10
    s = spacings / np.mean(spacings)
    s = s[s > 1e-14]
    a = (gamma_fn((eta + 2) / (eta + 1)))**(1 + eta)  # (local)
    ll = np.sum(np.log(1 + eta) + np.log(a) + eta * np.log(s + 1e-30)
                 - a * s**(1 + eta))  # (local)
    return -ll


print("\n--- Physical Hamiltonian ---")
r_values = {}  # (local)
all_r_n = []   # (local)
all_spacings = []  # (local)

for name, data in results.items():
    r_mean, r_n, spacings = compute_r_statistic(data['evals'])
    data['r_mean'] = r_mean
    data['r_n'] = r_n
    data['spacings'] = spacings
    r_values[name] = r_mean

    if len(spacings) > 10:
        res_b = minimize_scalar(lambda eta: brody_nll(eta, spacings),
                                bounds=(0.0, 1.5), method='bounded')
        data['brody_eta'] = res_b.x
    else:
        data['brody_eta'] = np.nan

    print(f"  {name}: <r> = {r_mean:.4f}, dim = {data['dim']}, "
          f"eta = {data['brody_eta']:.3f}")

    if len(r_n) > 0:
        all_r_n.extend(r_n)
    if len(spacings) > 0:
        all_spacings.extend(spacings)

all_r_n = np.array(all_r_n)
r_overall = np.mean(all_r_n)  # (local)
r_std = np.std(all_r_n) / np.sqrt(len(all_r_n))  # (local)
print(f"\n  OVERALL: <r> = {r_overall:.4f} +/- {r_std:.4f}")

all_spacings = np.array(all_spacings)
if len(all_spacings) > 10:
    res_bo = minimize_scalar(lambda eta: brody_nll(eta, all_spacings),
                              bounds=(0.0, 1.5), method='bounded')
    eta_overall = res_bo.x  # (local)
else:
    eta_overall = np.nan
print(f"  OVERALL Brody eta = {eta_overall:.3f}")

print("\n--- Control (E_J = 0) ---")
all_r_n_ctrl = []   # (local)
for name, data in results.items():
    r_mean_c, r_n_c, spacings_c = compute_r_statistic(data['evals_ctrl'])
    data['r_ctrl'] = r_mean_c

    if len(spacings_c) > 10:
        res_bc = minimize_scalar(lambda eta: brody_nll(eta, spacings_c),
                                 bounds=(0.0, 1.5), method='bounded')
        data['brody_ctrl'] = res_bc.x
    else:
        data['brody_ctrl'] = np.nan

    print(f"  {name}: <r> = {r_mean_c:.4f}, eta = {data['brody_ctrl']:.3f}")
    if len(r_n_c) > 0:
        all_r_n_ctrl.extend(r_n_c)

all_r_n_ctrl = np.array(all_r_n_ctrl)
r_ctrl_overall = np.mean(all_r_n_ctrl)  # (local)
r_ctrl_std = np.std(all_r_n_ctrl) / np.sqrt(len(all_r_n_ctrl))  # (local)
print(f"\n  CONTROL OVERALL: <r> = {r_ctrl_overall:.4f} +/- {r_ctrl_std:.4f}")

# =====================================================================
#  8. GATE VERDICT
# =====================================================================

print("\n" + "=" * 72)
print("GATE VERDICT")
print("=" * 72)

r_Poisson = 0.386  # (local)
r_GOE = 0.536      # (local)
r_GUE = 0.603      # (local)

print(f"References: Poisson = {r_Poisson}, GOE = {r_GOE}, GUE = {r_GUE}")
print(f"Physical:   <r> = {r_overall:.4f} +/- {r_std:.4f}")
print(f"Control:    <r> = {r_ctrl_overall:.4f} +/- {r_ctrl_std:.4f}")

alpha_interp = (r_overall - r_Poisson) / (r_GOE - r_Poisson)  # (local)
alpha_ctrl = (r_ctrl_overall - r_Poisson) / (r_GOE - r_Poisson)  # (local)
print(f"\nInterpolation alpha (0=Poisson, 1=GOE):")
print(f"  Physical: alpha = {alpha_interp:.3f}")
print(f"  Control:  alpha = {alpha_ctrl:.3f}")

if r_overall < 0.45:
    gate_verdict = "PASS"
    gate_detail = (f"<r> = {r_overall:.4f} < 0.45. "
                   f"Multi-cell R-G integrability survives at N_pair=4.")
elif r_overall > 0.50:
    gate_verdict = "FAIL"
    gate_detail = (f"<r> = {r_overall:.4f} > 0.50. "
                   f"Josephson coupling breaks R-G integrability at N_pair=4.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"<r> = {r_overall:.4f} in [0.45, 0.50]. "
                   f"Intermediate: inconclusive at this system size.")

print(f"\nGate MULTI-CELL-INTEG-73B: {gate_verdict}")
print(f"  {gate_detail}")

# =====================================================================
#  9. SAVE
# =====================================================================

print("\n" + "=" * 72)
print("SAVING")
print("=" * 72)

t_total = time.time() - t_start

save_dict = {
    'gate_name': 'MULTI-CELL-INTEG-73B',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,
    'N_modes': N_modes,
    'N_cells': N_cells,
    'N_pair': N_pair,
    'N_slots': N_slots,
    'dim_total': dim_total,
    'E_J': E_J,
    'Delta_BCS': Delta_BCS,
    'EJ_over_Delta': E_J / Delta_BCS,
    'c4_verts': np.array(c4_verts),
    'n_orbits': n_orbits,
    'orbit_periods': orbit_periods,
    'r_overall': r_overall,
    'r_overall_std': r_std,
    'r_ctrl_overall': r_ctrl_overall,
    'r_ctrl_std': r_ctrl_std,
    'eta_overall': eta_overall,
    'alpha_interp': alpha_interp,
    'r_Poisson': r_Poisson,
    'r_GOE': r_GOE,
    'r_GUE': r_GUE,
    'elapsed_s': t_total,
}

for name, data in results.items():
    key = name.replace('=', '').replace('/', '_')
    save_dict[f'r_{key}'] = data['r_mean']
    save_dict[f'r_ctrl_{key}'] = data['r_ctrl']
    save_dict[f'dim_{key}'] = data['dim']
    save_dict[f'eta_{key}'] = data['brody_eta']
    save_dict[f'eta_ctrl_{key}'] = data['brody_ctrl']
    save_dict[f'evals_{key}'] = data['evals']
    save_dict[f'evals_ctrl_{key}'] = data['evals_ctrl']

outpath = os.path.join(data_dir, 's73b_multi_cell_integ.npz')
np.savez(outpath, **save_dict)
print(f"Saved: {outpath}")

# =====================================================================
#  10. PLOT
# =====================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

ax = axes[0, 0]
s_ref = np.linspace(0.01, 4.0, 200)
ax.plot(s_ref, np.exp(-s_ref), 'k--', lw=1.5, label='Poisson', alpha=0.7)
ax.plot(s_ref, (np.pi/2)*s_ref*np.exp(-np.pi*s_ref**2/4), 'r--',
        lw=1.5, label='GOE', alpha=0.7)  # (local)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for (name, data), color in zip(results.items(), colors):
    if len(data['spacings']) > 5:
        s_norm = data['spacings'] / np.mean(data['spacings'])
        ax.hist(s_norm, bins=30, density=True, alpha=0.25, color=color,
                label=f'{name} (<r>={data["r_mean"]:.3f})')

ax.set_xlabel('s (unfolded)')
ax.set_ylabel('P(s)')
ax.set_title('Level Spacing Distribution')
ax.legend(fontsize=8)
ax.set_xlim(0, 4)

ax = axes[0, 1]
sec_list = list(results.keys()) + ['Overall']
r_phys = [results[k]['r_mean'] for k in results.keys()] + [r_overall]
r_ctrl_list = [results[k]['r_ctrl'] for k in results.keys()] + [r_ctrl_overall]

x = np.arange(len(sec_list))
width = 0.35  # (local)
ax.bar(x - width/2, r_phys, width, label=f'E_J={E_J:.2f}', color='#1f77b4')
ax.bar(x + width/2, r_ctrl_list, width, label='E_J=0 (ctrl)', color='#ff7f0e')
ax.axhline(y=r_Poisson, color='g', ls='--', lw=1, label='Poisson (0.386)')
ax.axhline(y=r_GOE, color='r', ls='--', lw=1, label='GOE (0.536)')
ax.axhline(y=0.45, color='gray', ls=':', lw=1)
ax.axhline(y=0.50, color='gray', ls='-.', lw=1)
ax.set_xticks(x)
ax.set_xticklabels(sec_list, fontsize=8, rotation=15)
ax.set_ylabel('<r>')
ax.set_title('Gap Ratio by Sector')
ax.legend(fontsize=7)

ax = axes[1, 0]
evals_k0 = results['k=0']['evals']
ax.plot(np.arange(len(evals_k0)), evals_k0, '.', ms=1, color='#1f77b4')
ax.set_xlabel('Level index')
ax.set_ylabel('Energy (M_KK)')
ax.set_title(f'k=0 sector spectrum (dim={len(evals_k0)})')

ax = axes[1, 1]
ax.hist(all_r_n, bins=40, density=True, alpha=0.5, color='#1f77b4',
        label=f'Physical <r>={r_overall:.4f}')
ax.hist(all_r_n_ctrl, bins=40, density=True, alpha=0.5, color='#ff7f0e',
        label=f'Control <r>={r_ctrl_overall:.4f}')
ax.axvline(x=r_Poisson, color='g', ls='--', lw=1.5, label='Poisson')
ax.axvline(x=r_GOE, color='r', ls='--', lw=1.5, label='GOE')
ax.set_xlabel('r_n')
ax.set_ylabel('P(r_n)')
ax.set_title('Gap ratio distribution')
ax.legend(fontsize=8)

fig.suptitle(f'MULTI-CELL-INTEG-73B: 4-cell C_4, N_pair=4\n'
             f'<r> = {r_overall:.4f} | Gate: {gate_verdict}',
             fontsize=13, fontweight='bold')
fig.tight_layout(rect=[0, 0, 1, 0.93])

plotpath = os.path.join(data_dir, 's73b_multi_cell_integ.png')
fig.savefig(plotpath, dpi=150)
print(f"Plot saved: {plotpath}")

print(f"\nTotal elapsed: {t_total:.1f} s")
print("Done.")
