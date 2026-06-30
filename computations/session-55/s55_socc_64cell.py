#!/usr/bin/env python3
"""
S55 SOCC-64CELL-55: S_occ on 64-Cell CG Lattice
=================================================

Physics:
  Extends the S54 32-cell tight-binding Hamiltonian to 64 cells to test
  lattice-size scaling of the occupation-weighted spectral action S_occ(tau).

  On the 32-cell lattice (SA-LATT-OCC-54), S_occ had a minimum at tau~0.194
  with a 5.35% barrier (sharp cutoff Lambda=1.0). However, W0-1 (zeta monotone),
  W0-4 (ZPF unstable), and W0-5 (minimum tracks Lambda) all identified this
  as a cutoff artifact. This computation tests whether doubling the lattice
  size changes the conclusion.

  The 64 cells are the first 64 SU(3) irreducible representations (p,q)
  ordered by Casimir eigenvalue C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3.

  Adjacency follows from Clebsch-Gordan decomposition (same as S54):
    - (p,q) bonded to (p',q') if (p',q') in (p,q) x (1,0) or (p,q) x (0,1)
    - Bonds classified: C^2 coset, su(2) stabilizer, u(1) hypercharge

  S_occ(tau) = sum_k n_k(tau) * Theta(1 - E_k^2/Lambda^2)
  with BCS occupation numbers n_k = v_k^2 and sharp cutoff Lambda=1.0.

Gate: SOCC-64CELL-55
  PASS: minimum persists with barrier >= 3%
  FAIL: barrier < 1% or vanishes

Author: Quantum-Acoustics-Theorist (Session 55, Wave 2-2)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, exp
from scipy.linalg import eigh
from scipy.optimize import brentq
from scipy.sparse.csgraph import connected_components, shortest_path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from canonical_constants import (
    J_C2, J_su2, J_u1, tau_fold,
    Delta_0_OES, Delta_0_GL,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_NPZ = os.path.join(SCRIPT_DIR, "s55_socc_64cell.npz")
OUT_PNG = os.path.join(SCRIPT_DIR, "s55_socc_64cell.png")
OUT_TXT = os.path.join(SCRIPT_DIR, "s55_socc_64cell_output.txt")

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

print("=" * 72)
print("S55 SOCC-64CELL-55: S_occ on 64-Cell CG Lattice")
print("=" * 72)

# ============================================================
# Section 1: Construct the 64-cell representation graph
# ============================================================
print("\n--- Section 1: 64-cell representation graph ---")

def casimir_su3(p, q):
    """SU(3) quadratic Casimir: C_2(p,q) = (p^2+q^2+pq+3p+3q)/3."""
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Enumerate all representations up to a generous cutoff, sort by Casimir
all_reps = []
for p in range(30):
    for q in range(30):
        all_reps.append((casimir_su3(p, q), p, q))
all_reps.sort()

# Take first 64 by Casimir ordering
N_CELLS = 64  # (local)

cell_labels = np.array([(p, q) for (_, p, q) in all_reps[:N_CELLS]])
cell_casimirs = np.array([casimir_su3(p, q) for (p, q) in cell_labels])
cell_dims = np.array([dim_su3(p, q) for (p, q) in cell_labels])
rep_set = set(map(tuple, cell_labels))
rep_to_idx = {tuple(cell_labels[i]): i for i in range(N_CELLS)}

print(f"  Number of cells: {N_CELLS}")
print(f"  Casimir range: [{cell_casimirs[0]:.3f}, {cell_casimirs[-1]:.3f}]")
print(f"  Dimension range: [{cell_dims.min()}, {cell_dims.max()}]")
print(f"  Total Hilbert space dimension (sum of dims): {cell_dims.sum()}")

# Print all representations
print(f"\n  Representations (Casimir order):")
for i, (p, q) in enumerate(cell_labels):
    print(f"    {i:2d}: ({p},{q})  C2={casimir_su3(p,q):.3f}  dim={dim_su3(p,q)}")

# ============================================================
# Section 2: Build adjacency matrices by bond type
# ============================================================
print("\n--- Section 2: Adjacency from Clebsch-Gordan rules ---")

# Bond types and their Dynkin label steps (same as S54):
COSET_STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1)]     # C^2 coset
SU2_STEPS   = [(-1, 1), (1, -1)]                       # su(2) stabilizer
U1_STEPS    = [(1, 1), (-1, -1)]                        # u(1) hypercharge

adj_C2  = np.zeros((N_CELLS, N_CELLS), dtype=int)
adj_su2 = np.zeros((N_CELLS, N_CELLS), dtype=int)
adj_u1  = np.zeros((N_CELLS, N_CELLS), dtype=int)

for i, (p1, q1) in enumerate(cell_labels):
    for (dp, dq) in COSET_STEPS:
        p2, q2 = int(p1) + dp, int(q1) + dq
        if p2 >= 0 and q2 >= 0 and (p2, q2) in rep_set:
            adj_C2[i, rep_to_idx[(p2, q2)]] = 1
    for (dp, dq) in SU2_STEPS:
        p2, q2 = int(p1) + dp, int(q1) + dq
        if p2 >= 0 and q2 >= 0 and (p2, q2) in rep_set:
            adj_su2[i, rep_to_idx[(p2, q2)]] = 1
    for (dp, dq) in U1_STEPS:
        p2, q2 = int(p1) + dp, int(q1) + dq
        if p2 >= 0 and q2 >= 0 and (p2, q2) in rep_set:
            adj_u1[i, rep_to_idx[(p2, q2)]] = 1

# Full adjacency
adj_full = adj_C2 | adj_su2 | adj_u1

# Bond counts
n_bonds_C2 = np.sum(adj_C2) // 2
n_bonds_su2 = np.sum(adj_su2) // 2
n_bonds_u1 = np.sum(adj_u1) // 2
n_bonds_total = np.sum(adj_full) // 2

bonds_per_cell = np.sum(adj_full, axis=1)
bonds_C2_per = np.sum(adj_C2, axis=1)
bonds_su2_per = np.sum(adj_su2, axis=1)
bonds_u1_per = np.sum(adj_u1, axis=1)

print(f"  Bond counts (undirected):")
print(f"    C^2 coset:       {n_bonds_C2}")
print(f"    su(2) stabilizer: {n_bonds_su2}")
print(f"    u(1) hypercharge: {n_bonds_u1}")
print(f"    Total:           {n_bonds_total}")
print(f"  Bonds per cell: min={bonds_per_cell.min()}, max={bonds_per_cell.max()}, "
      f"mean={bonds_per_cell.mean():.2f}")

# Verify symmetry, no self-loops, no overlap
assert np.allclose(adj_C2, adj_C2.T), "C2 adjacency not symmetric"
assert np.allclose(adj_su2, adj_su2.T), "su2 adjacency not symmetric"
assert np.allclose(adj_u1, adj_u1.T), "u1 adjacency not symmetric"
assert np.trace(adj_full) == 0, "Self-loops detected"
assert not np.any(adj_C2 & adj_su2), "C2/su2 overlap"
assert not np.any(adj_C2 & adj_u1), "C2/u1 overlap"
assert not np.any(adj_su2 & adj_u1), "su2/u1 overlap"
print(f"  Symmetry: PASS | Self-loops: NONE | Overlap: NONE")

# Connectivity check
n_comp, comp_labels = connected_components(adj_full)
print(f"  Connected components: {n_comp}")
assert n_comp == 1, f"Graph is disconnected ({n_comp} components)!"

# Graph diameter
dists = shortest_path(adj_full, method='D', unweighted=True)
diameter = int(np.max(dists[dists < np.inf]))
print(f"  Graph diameter: {diameter}")

# ============================================================
# Section 3: Compare to 32-cell graph
# ============================================================
print("\n--- Section 3: Comparison to 32-cell graph ---")

# Load 32-cell data for comparison
data_32 = np.load(os.path.join(SCRIPT_DIR, 's54_tb_hamiltonian.npz'), allow_pickle=True)
N_cells_32 = int(data_32['N_cells'])
n_bonds_32 = int(data_32['n_bonds_total'])
diameter_32 = int(data_32['diameter'])
cell_labels_32 = data_32['cell_labels']

print(f"  32-cell: {N_cells_32} cells, {n_bonds_32} bonds, diameter {diameter_32}")
print(f"  64-cell: {N_CELLS} cells, {n_bonds_total} bonds, diameter {diameter}")
print(f"  Scaling: cells 2.0x, bonds {n_bonds_total/n_bonds_32:.2f}x, "
      f"diameter {diameter/diameter_32:.2f}x")

# Verify first 32 cells match
match_32 = True
for i in range(min(N_cells_32, N_CELLS)):
    if i < N_cells_32:
        p32, q32 = cell_labels_32[i]
        p64, q64 = cell_labels[i]
        if p32 != p64 or q32 != q64:
            match_32 = False
            print(f"  MISMATCH at cell {i}: 32-cell ({p32},{q32}) vs 64-cell ({p64},{q64})")
            break

if match_32:
    print(f"  First 32 cells: MATCH (32-cell subset preserved)")

# ============================================================
# Section 4: Jensen metric tau-dependent Josephson couplings
# ============================================================
print("\n--- Section 4: tau-dependent Josephson couplings ---")

# Identical to S54 -- Jensen metric scaling:
#   J_C2(tau)  = J_C2(fold)  * exp(4*(tau_fold - tau))
#   J_su2(tau) = J_su2(fold) * exp(-6*(tau_fold - tau))
#   J_u1(tau)  = J_u1(fold)  * exp(2*(tau_fold - tau))

def J_C2_of_tau(tau):
    return J_C2 * exp(4.0 * (tau_fold - tau))

def J_su2_of_tau(tau):
    return J_su2 * exp(-6.0 * (tau_fold - tau))

def J_u1_of_tau(tau):
    return J_u1 * exp(2.0 * (tau_fold - tau))

print(f"  At fold (tau={tau_fold}): J_C2={J_C2:.3f}, J_su2={J_su2:.3f}, J_u1={J_u1:.3f}")

# ============================================================
# Section 5: Build H_TB(tau) and diagonalize
# ============================================================
print("\n--- Section 5: Hamiltonian construction and diagonalization ---")

tau_values = np.linspace(0.00, 0.50, 50)
N_tau = len(tau_values)
print(f"  Tau grid: {N_tau} values in [{tau_values[0]:.2f}, {tau_values[-1]:.2f}]")

# Storage
eigenvalues = np.zeros((N_tau, N_CELLS))
eigenvectors = np.zeros((N_tau, N_CELLS, N_CELLS))
bandwidths = np.zeros(N_tau)
J_C2_arr = np.zeros(N_tau)
J_su2_arr = np.zeros(N_tau)
J_u1_arr = np.zeros(N_tau)

def build_H_TB(tau):
    """Build 64x64 tight-binding Hamiltonian at given tau.
    H_TB is the weighted graph Laplacian:
      H_TB(i,j) = -J(i,j) for bonded i,j
      H_TB(i,i) = sum_j J(i,j)
    """
    jc2 = J_C2_of_tau(tau)
    jsu2 = J_su2_of_tau(tau)
    ju1 = J_u1_of_tau(tau)

    # Off-diagonal: weighted adjacency
    H = -(jc2 * adj_C2 + jsu2 * adj_su2 + ju1 * adj_u1).astype(float)

    # Diagonal: sum of outgoing bond strengths
    for i in range(N_CELLS):
        H[i, i] = (jc2 * bonds_C2_per[i]
                    + jsu2 * bonds_su2_per[i]
                    + ju1 * bonds_u1_per[i])

    return H, jc2, jsu2, ju1

# Diagonalize at each tau
for t_idx, tau in enumerate(tau_values):
    H, jc2, jsu2, ju1 = build_H_TB(tau)

    J_C2_arr[t_idx] = jc2
    J_su2_arr[t_idx] = jsu2
    J_u1_arr[t_idx] = ju1

    # Hermitian eigenvalue decomposition
    evals, evecs = eigh(H)
    eigenvalues[t_idx] = evals
    eigenvectors[t_idx] = evecs
    bandwidths[t_idx] = evals[-1] - evals[0]

print(f"  Diagonalization complete: {N_tau} tau values")

# Cross-checks
t_fold_idx = np.argmin(np.abs(tau_values - tau_fold))
zero_evals = eigenvalues[:, 0]
print(f"  Lowest eigenvalue (should be ~0):")
print(f"    min={zero_evals.min():.2e}, max={zero_evals.max():.2e}")
evals_fold = eigenvalues[t_fold_idx]
print(f"  Bandwidth at fold: {bandwidths[t_fold_idx]:.4f} M_KK")
print(f"  Fiedler eigenvalue at fold: {evals_fold[1]:.6f} M_KK")
print(f"  Eigenvalue range at fold: [{evals_fold[0]:.6f}, {evals_fold[-1]:.6f}]")

# Degeneracy pattern at fold
degeneracy_tol = 1e-8
unique_evals_fold = []
degeneracies_fold = []
i = 0
while i < N_CELLS:
    e = evals_fold[i]
    deg = 1  # (local)
    while i + deg < N_CELLS and abs(evals_fold[i + deg] - e) < degeneracy_tol:
        deg += 1
    unique_evals_fold.append(e)
    degeneracies_fold.append(deg)
    i += deg
n_distinct_fold = len(unique_evals_fold)
print(f"  Distinct eigenvalues at fold: {n_distinct_fold}")

# Z_2 conjugation check
conj_perm = np.zeros((N_CELLS, N_CELLS), dtype=int)
for i, (p, q) in enumerate(cell_labels):
    if (int(q), int(p)) in rep_to_idx:
        j = rep_to_idx[(int(q), int(p))]
        conj_perm[i, j] = 1
    else:
        conj_perm[i, i] = 1

H_fold, _, _, _ = build_H_TB(tau_fold)
comm_err = np.max(np.abs(conj_perm @ H_fold - H_fold @ conj_perm))
print(f"  [C, H] at fold: {comm_err:.2e}")

n_selfconj = sum(1 for (p, q) in cell_labels if p == q)
n_pairs = (N_CELLS - n_selfconj) // 2
print(f"  Self-conjugate reps: {n_selfconj}, conjugate pairs: {n_pairs}")

# ============================================================
# Section 6: BCS occupation numbers
# ============================================================
print("\n--- Section 6: BCS occupation numbers ---")

def bcs_occupation(energies, delta, n_target=2.0):
    """BCS occupation n_k = v_k^2 with mu set by particle number constraint."""
    N = len(energies)
    e_min, e_max = energies.min(), energies.max()

    def occupation_sum(mu):
        eps = energies - mu
        Ek = np.sqrt(eps**2 + delta**2)
        vk2 = 0.5 * (1.0 - eps / Ek)
        return np.sum(vk2) - n_target

    mu_lo = e_min - 10.0 * abs(delta) - 10.0 * (e_max - e_min)
    mu_hi = e_max + 10.0 * abs(delta) + 10.0 * (e_max - e_min)

    try:
        mu = brentq(occupation_sum, mu_lo, mu_hi, xtol=1e-14, maxiter=200)
    except ValueError:
        mu_lo = e_min - 100.0
        mu_hi = e_max + 100.0
        mu = brentq(occupation_sum, mu_lo, mu_hi, xtol=1e-14, maxiter=200)

    eps = energies - mu
    Ek = np.sqrt(eps**2 + delta**2)
    n_k = 0.5 * (1.0 - eps / Ek)
    return n_k, mu

# Compute BCS occupations at each tau using Delta_OES (primary) and Delta_GL (cross-check)
Delta_primary = Delta_0_OES
Delta_secondary = Delta_0_GL

occ_bcs_oes = np.zeros((N_tau, N_CELLS))
occ_bcs_gl = np.zeros((N_tau, N_CELLS))
mu_bcs_oes_arr = np.zeros(N_tau)
mu_bcs_gl_arr = np.zeros(N_tau)

for t_idx in range(N_tau):
    eps = eigenvalues[t_idx]
    occ_bcs_oes[t_idx], mu_bcs_oes_arr[t_idx] = bcs_occupation(eps, Delta_primary, n_target=2.0)
    occ_bcs_gl[t_idx], mu_bcs_gl_arr[t_idx] = bcs_occupation(eps, Delta_secondary, n_target=2.0)

print(f"  Delta_OES = {Delta_primary:.4f} M_KK, Delta_GL = {Delta_secondary:.4f} M_KK")
print(f"  BCS(OES) occupation sum check: {occ_bcs_oes[t_fold_idx].sum():.6f} (target: 2.0)")
print(f"  mu_BCS(OES) at fold: {mu_bcs_oes_arr[t_fold_idx]:.6f}")

# ============================================================
# Section 7: Compute S_occ and S_vac with sharp cutoff
# ============================================================
print("\n--- Section 7: S_occ and S_vac computation ---")

# Primary cutoff: sharp Theta(1 - E^2/Lambda^2) with Lambda = 1.0
# Also scan Lambda = [0.5, 1.0, 2.0, 5.0] for cutoff sensitivity
Lambda_values = np.array([0.5, 1.0, 2.0, 5.0])
n_lambdas = len(Lambda_values)

def f_sharp(x):
    """Sharp cutoff: f(x) = Theta(1 - x)"""
    return np.where(x <= 1.0, 1.0, 0.0)

# Also compute with exponential cutoff for comparison
def f_exp(x):
    return np.exp(-x)

# Storage: [Lambda_idx, tau_idx]
S_occ_sharp = np.zeros((n_lambdas, N_tau))
S_vac_sharp = np.zeros((n_lambdas, N_tau))
S_occ_gl_sharp = np.zeros((n_lambdas, N_tau))
S_occ_exp = np.zeros((n_lambdas, N_tau))
S_vac_exp = np.zeros((n_lambdas, N_tau))

for il, Lam in enumerate(Lambda_values):
    for it in range(N_tau):
        eps = eigenvalues[it]
        x = eps**2 / Lam**2

        fvals_sharp = f_sharp(x)
        fvals_exp = f_exp(x)

        S_vac_sharp[il, it] = np.sum(fvals_sharp)
        S_occ_sharp[il, it] = np.sum(occ_bcs_oes[it] * fvals_sharp)
        S_occ_gl_sharp[il, it] = np.sum(occ_bcs_gl[it] * fvals_sharp)

        S_vac_exp[il, it] = np.sum(fvals_exp)
        S_occ_exp[il, it] = np.sum(occ_bcs_oes[it] * fvals_exp)

# Primary result: sharp cutoff, Lambda=1.0
il_primary = 1  # Lambda=1.0
S_occ_primary = S_occ_sharp[il_primary]
S_vac_primary = S_vac_sharp[il_primary]

print(f"  Cutoff: sharp, Lambda = {Lambda_values[il_primary]:.1f} M_KK")
print(f"  S_occ at tau=0:    {S_occ_primary[0]:.6f}")
print(f"  S_occ at fold:     {S_occ_primary[t_fold_idx]:.6f}")
print(f"  S_occ at tau=0.50: {S_occ_primary[-1]:.6f}")
print(f"  S_vac at tau=0:    {S_vac_primary[0]:.6f}")
print(f"  S_vac at fold:     {S_vac_primary[t_fold_idx]:.6f}")
print(f"  S_vac at tau=0.50: {S_vac_primary[-1]:.6f}")

# Count modes within cutoff at fold
n_within_fold = np.sum(eigenvalues[t_fold_idx]**2 <= Lambda_values[il_primary]**2)
print(f"  Modes within cutoff at fold: {n_within_fold}/{N_CELLS}")

# ============================================================
# Section 8: Search for S_occ minima
# ============================================================
print("\n--- Section 8: Minima search ---")

tau_lo_idx = np.argmin(np.abs(tau_values - 0.10))
tau_hi_idx = np.argmin(np.abs(tau_values - 0.30))

def find_minima_in_range(S_arr, tau_arr, idx_lo, idx_hi):
    """Find local minima of S_arr in index range [idx_lo, idx_hi]."""
    minima = []
    for j in range(idx_lo + 1, idx_hi):
        if S_arr[j] < S_arr[j-1] and S_arr[j] < S_arr[j+1]:
            S_min = S_arr[j]
            tau_min = tau_arr[j]
            # Barrier: smaller of (left max - min, right max - min)
            S_left_max = S_arr[idx_lo:j].max()
            S_right_max = S_arr[j+1:idx_hi+1].max()
            barrier_abs = min(S_left_max - S_min, S_right_max - S_min)
            barrier_rel = barrier_abs / abs(S_min) if abs(S_min) > 1e-15 else barrier_abs
            minima.append((tau_min, S_min, barrier_rel, barrier_abs))
    return minima

def find_minima_derivative(S_arr, tau_arr, idx_lo, idx_hi):
    """Find minima using centered finite differences."""
    dtau = tau_arr[1] - tau_arr[0]
    dS = np.gradient(S_arr, dtau)
    d2S = np.gradient(dS, dtau)

    minima = []
    for j in range(idx_lo + 1, idx_hi):
        if dS[j-1] < 0 and dS[j+1] > 0 and d2S[j] > 0:
            tau_min = tau_arr[j]
            S_min = S_arr[j]
            S_left = S_arr[idx_lo:j].max() if j > idx_lo else S_arr[idx_lo]
            S_right = S_arr[j+1:idx_hi+1].max() if j < idx_hi else S_arr[idx_hi]
            barrier = min(S_left - S_min, S_right - S_min)
            barrier_rel = barrier / abs(S_min) if abs(S_min) > 1e-15 else barrier
            minima.append((tau_min, S_min, barrier_rel, barrier))
    return minima

print(f"  Search range: tau in [{tau_values[tau_lo_idx]:.3f}, {tau_values[tau_hi_idx]:.3f}]")
print()

# Table header
print(f"  {'Lambda':>6s}  {'Cutoff':>8s}  {'Occ':>10s}  {'Min tau':>8s}  {'S_min':>10s}  "
      f"{'Barrier%':>10s}  {'Barrier_abs':>12s}  {'Verdict':>8s}")
print(f"  {'-'*6}  {'-'*8}  {'-'*10}  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*8}")

# Track the primary result
primary_min_tau = None
primary_barrier_rel = None
primary_barrier_abs = None
primary_S_min = None

for il, Lam in enumerate(Lambda_values):
    for occ_label, S_arr in [('BCS(OES)', S_occ_sharp[il]),
                              ('BCS(GL)', S_occ_gl_sharp[il]),
                              ('Vacuum', S_vac_sharp[il])]:
        mins_direct = find_minima_in_range(S_arr, tau_values, tau_lo_idx, tau_hi_idx)
        mins_deriv = find_minima_derivative(S_arr, tau_values, tau_lo_idx, tau_hi_idx)
        # Use derivative method as primary, direct as cross-check
        mins = mins_deriv if mins_deriv else mins_direct

        if mins:
            best = max(mins, key=lambda x: x[2])
            tau_min, S_min, barrier_rel, barrier_abs = best
            verdict = "MIN"

            if Lam == 1.0 and occ_label == 'BCS(OES)':
                primary_min_tau = tau_min
                primary_barrier_rel = barrier_rel
                primary_barrier_abs = barrier_abs
                primary_S_min = S_min
                verdict = "PRIMARY"

            print(f"  {Lam:6.1f}  {'sharp':>8s}  {occ_label:>10s}  {tau_min:8.3f}  "
                  f"{S_min:10.4f}  {barrier_rel*100:10.4f}  {barrier_abs:12.6f}  {verdict:>8s}")
        else:
            verdict = "MONO"
            if Lam == 1.0 and occ_label == 'BCS(OES)':
                verdict = "PRIMARY"
            print(f"  {Lam:6.1f}  {'sharp':>8s}  {occ_label:>10s}  {'---':>8s}  "
                  f"{'---':>10s}  {'monotone':>10s}  {'---':>12s}  {verdict:>8s}")

# Also check exponential cutoff
print()
for il, Lam in enumerate(Lambda_values):
    S_arr = S_occ_exp[il]
    mins = find_minima_derivative(S_arr, tau_values, tau_lo_idx, tau_hi_idx)
    if mins:
        best = max(mins, key=lambda x: x[2])
        print(f"  {Lam:6.1f}  {'exp':>8s}  {'BCS(OES)':>10s}  {best[0]:8.3f}  "
              f"{best[1]:10.4f}  {best[2]*100:10.4f}  {best[3]:12.6f}  {'MIN':>8s}")
    else:
        print(f"  {Lam:6.1f}  {'exp':>8s}  {'BCS(OES)':>10s}  {'---':>8s}  "
              f"{'---':>10s}  {'monotone':>10s}  {'---':>12s}  {'MONO':>8s}")

# ============================================================
# Section 9: Compare S_occ(64) to S_occ(32) side by side
# ============================================================
print("\n--- Section 9: 64-cell vs 32-cell comparison ---")

# Load 32-cell S_occ data
try:
    data_32_socc = np.load(os.path.join(SCRIPT_DIR, 's54_sa_latt_occ.npz'), allow_pickle=True)
    has_32 = True
except FileNotFoundError:
    has_32 = False
    print("  WARNING: 32-cell S_occ data not found (s54_sa_latt_occ.npz)")

if has_32:
    # The 32-cell data stores S_occ with indices [cutoff, Lambda, tau]
    # Sharp cutoff = index 1, Lambda=1.0 = index 0
    # Let me check what's in the file
    print(f"  32-cell npz keys: {list(data_32_socc.keys())}")

    tau_32 = data_32_socc['tau_values']
    evals_32 = data_32['eigenvalues']  # From the TB hamiltonian file

    # Reconstruct S_occ(32) with sharp cutoff Lambda=1.0 to ensure apples-to-apples
    n_bcs_32, mu_32 = np.zeros((len(tau_32), N_cells_32)), np.zeros(len(tau_32))
    for t_idx in range(len(tau_32)):
        n_bcs_32[t_idx], mu_32[t_idx] = bcs_occupation(evals_32[t_idx], Delta_primary, n_target=2.0)

    S_occ_32_recomp = np.zeros(len(tau_32))
    S_vac_32_recomp = np.zeros(len(tau_32))
    Lam_compare = 1.0  # (local)
    for it in range(len(tau_32)):
        x32 = evals_32[it]**2 / Lam_compare**2
        fvals = f_sharp(x32)
        S_vac_32_recomp[it] = np.sum(fvals)
        S_occ_32_recomp[it] = np.sum(n_bcs_32[it] * fvals)

    # Find minimum for 32-cell (recomputed)
    mins_32 = find_minima_derivative(S_occ_32_recomp, tau_32,
                                      np.argmin(np.abs(tau_32 - 0.10)),
                                      np.argmin(np.abs(tau_32 - 0.30)))

    if mins_32:
        best_32 = max(mins_32, key=lambda x: x[2])
        print(f"  32-cell S_occ minimum: tau={best_32[0]:.3f}, "
              f"barrier={best_32[2]*100:.4f}%, S_min={best_32[1]:.4f}")
    else:
        print(f"  32-cell S_occ: monotone (no minimum)")

    # 64-cell result
    if primary_min_tau is not None:
        print(f"  64-cell S_occ minimum: tau={primary_min_tau:.3f}, "
              f"barrier={primary_barrier_rel*100:.4f}%, S_min={primary_S_min:.4f}")
    else:
        print(f"  64-cell S_occ: monotone (no minimum)")

    # Normalized comparison
    print(f"\n  Per-cell S_occ at fold:")
    print(f"    32-cell: S_occ/N = {S_occ_32_recomp[np.argmin(np.abs(tau_32-tau_fold))]/N_cells_32:.6f}")
    print(f"    64-cell: S_occ/N = {S_occ_primary[t_fold_idx]/N_CELLS:.6f}")

    print(f"\n  S_vac at fold:")
    print(f"    32-cell: {S_vac_32_recomp[np.argmin(np.abs(tau_32-tau_fold))]:.4f} ({N_cells_32} cells)")
    print(f"    64-cell: {S_vac_primary[t_fold_idx]:.4f} ({N_CELLS} cells)")

# ============================================================
# Section 10: Cutoff sensitivity analysis
# ============================================================
print("\n--- Section 10: Cutoff sensitivity ---")

# For the sharp cutoff, the minimum should track Lambda if it's an artifact
# The S54 W0-5 finding was that the minimum tracks Lambda
print(f"  Minimum location vs Lambda (sharp cutoff, BCS(OES)):")
for il, Lam in enumerate(Lambda_values):
    mins = find_minima_derivative(S_occ_sharp[il], tau_values, tau_lo_idx, tau_hi_idx)
    if mins:
        best = max(mins, key=lambda x: x[2])
        n_within = np.sum(eigenvalues[t_fold_idx]**2 <= Lam**2)
        print(f"    Lambda={Lam:.1f}: tau_min={best[0]:.3f}, barrier={best[2]*100:.4f}%, "
              f"modes_in_cutoff={n_within}/{N_CELLS}")
    else:
        n_within = np.sum(eigenvalues[t_fold_idx]**2 <= Lam**2)
        print(f"    Lambda={Lam:.1f}: MONOTONE, modes_in_cutoff={n_within}/{N_CELLS}")

# ============================================================
# Section 11: Monotonicity analysis
# ============================================================
print("\n--- Section 11: Monotonicity analysis ---")

# Check if S_occ is monotone
S_diff = np.diff(S_occ_primary)
n_increasing = np.sum(S_diff > 0)
n_decreasing = np.sum(S_diff < 0)
print(f"  S_occ(Lambda=1.0): {n_increasing} increasing, {n_decreasing} decreasing "
      f"out of {len(S_diff)} intervals")

# Check where S_occ increases/decreases
if n_decreasing > 0 and n_increasing > 0:
    # Find the turning point
    turning_points = []
    for j in range(1, len(S_diff)):
        if S_diff[j-1] * S_diff[j] < 0:
            turning_points.append(tau_values[j])
    print(f"  Turning points: {turning_points}")

# Relative change from tau=0 to fold
S_change = (S_occ_primary[t_fold_idx] - S_occ_primary[0]) / abs(S_occ_primary[0]) * 100
print(f"  S_occ change from tau=0 to fold: {S_change:+.2f}%")

# ============================================================
# Section 12: Save data
# ============================================================
print("\n--- Section 12: Save data ---")

np.savez(OUT_NPZ,
         # Primary outputs
         tau_values=tau_values,
         eigenvalues=eigenvalues,
         eigenvectors=eigenvectors,
         # Graph structure
         adjacency=adj_full.astype(np.int8),
         adj_C2=adj_C2.astype(np.int8),
         adj_su2=adj_su2.astype(np.int8),
         adj_u1=adj_u1.astype(np.int8),
         cell_labels=cell_labels,
         cell_casimirs=cell_casimirs,
         cell_dims=cell_dims,
         # Spectrum
         bandwidths=bandwidths,
         J_C2_tau=J_C2_arr,
         J_su2_tau=J_su2_arr,
         J_u1_tau=J_u1_arr,
         # S_occ results
         S_occ_sharp=S_occ_sharp,         # [n_lambdas, N_tau]
         S_vac_sharp=S_vac_sharp,
         S_occ_gl_sharp=S_occ_gl_sharp,
         S_occ_exp=S_occ_exp,
         S_vac_exp=S_vac_exp,
         Lambda_values=Lambda_values,
         occ_bcs_oes=occ_bcs_oes,         # [N_tau, N_CELLS]
         occ_bcs_gl=occ_bcs_gl,
         mu_bcs_oes=mu_bcs_oes_arr,
         mu_bcs_gl=mu_bcs_gl_arr,
         # Metadata
         N_cells=np.int64(N_CELLS),
         n_bonds_C2=np.int64(n_bonds_C2),
         n_bonds_su2=np.int64(n_bonds_su2),
         n_bonds_u1=np.int64(n_bonds_u1),
         n_bonds_total=np.int64(n_bonds_total),
         diameter=np.int64(diameter),
         Delta_primary=Delta_primary,
         Delta_secondary=Delta_secondary,
         )

print(f"  Saved: {OUT_NPZ}")

# ============================================================
# Section 13: Plot
# ============================================================
print("\n--- Section 13: Plotting ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(3, 2, figure=fig, hspace=0.35, wspace=0.30)

fig.suptitle("SOCC-64CELL-55: S$_{occ}$ on 64-Cell CG Lattice",
             fontsize=14, fontweight='bold')

# Panel (a): Eigenvalue spectrum vs tau (64-cell)
ax = fig.add_subplot(gs[0, 0])
for n in range(N_CELLS):
    alpha = 0.15 if n > 16 else (0.4 if n > 4 else 0.8)  # (local)
    lw = 1.2 if n <= 4 else 0.3  # (local)
    color = 'C0' if n == 0 else ('C1' if n <= 4 else ('C2' if n <= 16 else 'C3'))
    ax.plot(tau_values, eigenvalues[:, n], color=color, alpha=alpha, linewidth=lw)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$E_n(\tau)$ [M$_{KK}$]')
ax.set_title(f'(a) 64-cell eigenvalue spectrum')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{fold}$')
ax.legend(fontsize=8)

# Panel (b): S_occ vs tau for different Lambda (sharp cutoff)
ax = fig.add_subplot(gs[0, 1])
colors_lam = ['C0', 'C1', 'C2', 'C3']
for il, Lam in enumerate(Lambda_values):
    ax.plot(tau_values, S_occ_sharp[il], color=colors_lam[il],
            linewidth=1.5, label=rf'$\Lambda = {Lam:.1f}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S_{occ}(\tau)$')
ax.set_title('(b) S$_{occ}$(64-cell, sharp cutoff)')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.legend(fontsize=8)

# Panel (c): S_occ(64) vs S_occ(32) comparison at Lambda=1.0
ax = fig.add_subplot(gs[1, 0])
# Normalize to compare shape
S64_norm = S_occ_primary / S_occ_primary[0] if abs(S_occ_primary[0]) > 1e-15 else S_occ_primary
ax.plot(tau_values, S64_norm, 'C0-', linewidth=2, label=f'64-cell (N={N_CELLS})')
if has_32:
    S32_norm = S_occ_32_recomp / S_occ_32_recomp[0] if abs(S_occ_32_recomp[0]) > 1e-15 else S_occ_32_recomp
    ax.plot(tau_32, S32_norm, 'C1--', linewidth=2, label=f'32-cell (N={N_cells_32})')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S_{occ}(\tau) / S_{occ}(0)$')
ax.set_title(r'(c) Normalized S$_{occ}$ comparison ($\Lambda = 1.0$)')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.legend(fontsize=9)

# Panel (d): S_vac vs tau (vacuum spectral action)
ax = fig.add_subplot(gs[1, 1])
ax.plot(tau_values, S_vac_primary, 'C0-', linewidth=2, label='64-cell S$_{vac}$')
if has_32:
    ax.plot(tau_32, S_vac_32_recomp, 'C1--', linewidth=2, label='32-cell S$_{vac}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S_{vac}(\tau)$')
ax.set_title(r'(d) Vacuum spectral action ($\Lambda = 1.0$)')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.legend(fontsize=9)

# Panel (e): BCS(OES) vs BCS(GL) comparison
ax = fig.add_subplot(gs[2, 0])
ax.plot(tau_values, S_occ_sharp[il_primary], 'C0-', linewidth=2,
        label=f'BCS(OES), $\\Delta$={Delta_primary:.3f}')
ax.plot(tau_values, S_occ_gl_sharp[il_primary], 'C1--', linewidth=2,
        label=f'BCS(GL), $\\Delta$={Delta_secondary:.3f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S_{occ}(\tau)$')
ax.set_title(r'(e) BCS gap comparison ($\Lambda = 1.0$, sharp)')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.legend(fontsize=9)

# Panel (f): Modes within cutoff vs tau
ax = fig.add_subplot(gs[2, 1])
for il, Lam in enumerate(Lambda_values):
    n_within = np.array([np.sum(eigenvalues[it]**2 <= Lam**2) for it in range(N_tau)])
    ax.plot(tau_values, n_within, color=colors_lam[il],
            linewidth=1.5, label=rf'$\Lambda = {Lam:.1f}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Modes within cutoff')
ax.set_title('(f) Number of modes within cutoff')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_ylim(0, N_CELLS + 2)
ax.legend(fontsize=8)

plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

# ============================================================
# Section 14: Gate verdict
# ============================================================
print("\n" + "=" * 72)
print("GATE VERDICT: SOCC-64CELL-55")
print("=" * 72)

print(f"\n  Pre-registered criterion:")
print(f"    PASS: minimum persists with barrier >= 3%")
print(f"    FAIL: barrier < 1% or vanishes")
print(f"    INFO: barrier in [1%, 3%)")

print(f"\n  Results (64-cell, sharp cutoff, Lambda=1.0, BCS(OES)):")
if primary_min_tau is not None:
    print(f"    Minimum at tau = {primary_min_tau:.3f}")
    print(f"    S_occ(min) = {primary_S_min:.6f}")
    print(f"    Barrier (relative): {primary_barrier_rel*100:.4f}%")
    print(f"    Barrier (absolute): {primary_barrier_abs:.6f}")

    if primary_barrier_rel >= 0.03:
        verdict = "PASS"
        detail = f"Minimum at tau={primary_min_tau:.3f}, barrier={primary_barrier_rel*100:.2f}% >= 3%"
    elif primary_barrier_rel >= 0.01:
        verdict = "INFO"
        detail = f"Minimum at tau={primary_min_tau:.3f}, barrier={primary_barrier_rel*100:.2f}% in [1%,3%)"
    else:
        verdict = "FAIL"
        detail = f"Minimum at tau={primary_min_tau:.3f}, barrier={primary_barrier_rel*100:.2f}% < 1%"
else:
    verdict = "FAIL"
    detail = "No minimum found in [0.10, 0.30] -- S_occ is monotone"
    print(f"    No minimum found in [0.10, 0.30]")
    print(f"    S_occ is monotone")

print(f"\n  VERDICT: {verdict}")
print(f"  Detail: {detail}")

# Summary comparison
print(f"\n  Summary comparison (sharp, Lambda=1.0):")
if has_32 and mins_32:
    print(f"    32-cell: tau_min={best_32[0]:.3f}, barrier={best_32[2]*100:.4f}%")
else:
    print(f"    32-cell: {'monotone' if has_32 else 'data not available'}")
if primary_min_tau is not None:
    print(f"    64-cell: tau_min={primary_min_tau:.3f}, barrier={primary_barrier_rel*100:.4f}%")
else:
    print(f"    64-cell: monotone")

# Cutoff sensitivity summary
print(f"\n  Cutoff sensitivity (BCS(OES), sharp):")
for il, Lam in enumerate(Lambda_values):
    mins = find_minima_derivative(S_occ_sharp[il], tau_values, tau_lo_idx, tau_hi_idx)
    if mins:
        best = max(mins, key=lambda x: x[2])
        print(f"    Lambda={Lam:.1f}: tau_min={best[0]:.3f}, barrier={best[2]*100:.4f}%")
    else:
        print(f"    Lambda={Lam:.1f}: monotone")

print(f"\n{'='*72}")
print(f"  64-cell lattice: {N_CELLS} cells, {n_bonds_total} bonds, diameter {diameter}")
print(f"  Casimir range: [{cell_casimirs[0]:.3f}, {cell_casimirs[-1]:.3f}]")
print(f"  Bandwidth at fold: {bandwidths[t_fold_idx]:.4f} M_KK")
print(f"{'='*72}")
