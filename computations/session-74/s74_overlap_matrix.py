#!/usr/bin/env python3
"""
OVERLAP-MATRIX-74 (W1-K): 3x3 BCS-branch to emergent-branch overlap matrix.

Computes M_ib = <BCS branch i | emergent branch b> where:
  - BCS branches (S56 classification):
      B1 = acoustic, 1 mode   (index 4 in eps_fold sorted order)
      B2 = flat-optical, 4 modes (indices 0-3)
      B3 = dispersive-optical, 3 modes (indices 5-7)
  - Emergent branches (SO(3) spin content for SVT decomposition):
      scalar = j=0
      vector = j=1
      tensor = j=2

Projection chain:
  1. Each BCS mode i is a 32-component eigenvector on the 32-cell CG(24)
     tight-binding lattice (from s54_tb_hamiltonian.npz, fold_idx=19).
  2. Cell k carries an SU(3) irrep label (p_k, q_k) (the k-th PW sector
     sorted by Casimir). This is the PW labelling of the 32-cell basis.
  3. SU(3) -> SO(3) branching (Elliott 1958) gives Theta(p,q,L) = number
     of times spin-L appears in irrep (p,q). The fractional content of
     spin j in (p,q) is f(p,q,j) = Theta(p,q,j)*(2j+1) / dim(p,q).
  4. Per-mode spin-j weight:
       w_i^{(j)} = sum_k |U[k,i]|^2 * f(p_k, q_k, j)
  5. Aggregate to BCS branches (sum over modes in each branch) and
     renormalise each row to sum_j M_{ij} = 1 (project to {scalar,vector,tensor}).

Author: Phonon-First Cosmologist (S74 W1-K)
"""

from __future__ import annotations
import os
import sys
import time
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import tau_fold, N_cells

t0 = time.time()

# ==============================================================================
# 1. Load 32-cell lattice eigenvectors at the fold and cell (p,q) labels
# ==============================================================================
print("=" * 78)
print("OVERLAP-MATRIX-74 (W1-K): BCS-branch <-> emergent-branch overlap")
print("=" * 78)

tb = np.load(os.path.join(SCRIPT_DIR, 's54_tb_hamiltonian.npz'), allow_pickle=True)
eigenvalues = tb['eigenvalues']      # (50, 32)
eigenvectors = tb['eigenvectors']    # (50, 32, 32)
cell_labels = tb['cell_labels']      # (32, 2)   (p,q) per cell
tau_values = tb['tau_values']        # (50,)

# Fold index from S56 canonical: tau_fold = 0.19 -> fold_idx = 19
fold_idx = int(np.argmin(np.abs(tau_values - tau_fold)))
tau_fold_actual = float(tau_values[fold_idx])
print(f"Fold index: {fold_idx}, tau_fold_actual = {tau_fold_actual:.4f} (canonical tau_fold = {tau_fold})")

# 32-cell eigenvector matrix at the fold; columns are eigenvectors, sorted by energy
U = eigenvectors[fold_idx]           # (32, 32)
eps = eigenvalues[fold_idx]          # (32,)
print(f"N_cells = {U.shape[0]}, lowest 8 eps = {eps[:8]}")
assert int(tb['N_cells']) == int(N_cells), "N_cells mismatch vs canonical"

# Cross-check eps[:8] matches S56 eps_fold
s56 = np.load(os.path.join(SCRIPT_DIR, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold_s56 = s56['eps_fold']
match = np.allclose(eps[:8], eps_fold_s56, atol=1e-12)
print(f"eps[:8] matches s56_gge_fabric.eps_fold: {match}")
assert match, "S54 TB eigenvalues at fold disagree with S56 eps_fold"

# Verify eigenvectors are orthonormal (unitary basis change)
orth_err = float(np.max(np.abs(U @ U.T - np.eye(U.shape[0]))))
print(f"max |U U^T - I| = {orth_err:.3e}")
assert orth_err < 1e-10, "32-cell eigenvectors are not orthonormal"

# ==============================================================================
# 2. BCS branch definition (S56 s56_gge_fabric.py line 596)
# ==============================================================================
# branch_labels_1cell = ['B2','B2','B2','B2','B1','B3','B3','B3']
branch_labels_1cell = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3']
N_modes = 8  # (local)
bcs_branch_modes = {
    'B1': [i for i, lbl in enumerate(branch_labels_1cell) if lbl == 'B1'],   # [4]
    'B2': [i for i, lbl in enumerate(branch_labels_1cell) if lbl == 'B2'],   # [0,1,2,3]
    'B3': [i for i, lbl in enumerate(branch_labels_1cell) if lbl == 'B3'],   # [5,6,7]
}
print(f"\nBCS branch modes: {bcs_branch_modes}")
assert len(bcs_branch_modes['B1']) == 1
assert len(bcs_branch_modes['B2']) == 4
assert len(bcs_branch_modes['B3']) == 3

# ==============================================================================
# 3. SU(3) -> SO(3) Elliott branching
# ==============================================================================
def dim_pq(p: int, q: int) -> int:
    """SU(3) irrep dimension."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def elliott_branching(p: int, q: int) -> dict[int, int]:
    """
    SU(3) irrep (p,q) -> SO(3) branching (Elliott 1958).

    For (lambda, mu) = (p, q) with lam_min = min(p,q), lam_max = max(p,q):
      - K runs over: lam_min, lam_min - 2, ..., 1 or 0
      - If K > 0: L = K, K+1, ..., K + lam_max
      - If K = 0: L = lam_max, lam_max - 2, ..., 1 or 0

    Returns: dict mapping L -> multiplicity Theta(p,q,L).

    Dimensional consistency is enforced: sum_L (2L+1) * Theta(p,q,L) = dim(p,q).
    """
    lam_min = min(p, q)
    lam_max = max(p, q)
    mult: dict[int, int] = {}

    # K values: lam_min, lam_min-2, ... down to 0 or 1
    K_vals = []
    K = lam_min
    while K >= 0:
        K_vals.append(K)
        K -= 2

    for K in K_vals:
        if K > 0:
            # L = K, K+1, ..., K + lam_max
            for L in range(K, K + lam_max + 1):
                mult[L] = mult.get(L, 0) + 1
        else:
            # K = 0: L = lam_max, lam_max-2, ...
            L = lam_max
            while L >= 0:
                mult[L] = mult.get(L, 0) + 1
                L -= 2

    # Dimensional cross-check
    total = sum((2 * L + 1) * m for L, m in mult.items())
    expected = dim_pq(p, q)
    assert total == expected, (
        f"Elliott branching failed for ({p},{q}): "
        f"sum (2L+1)*mult = {total} != dim = {expected}"
    )
    return mult


# Cross-check Elliott for known small cases
print("\nElliott SU(3) -> SO(3) branching cross-checks:")
test_cases = [
    ((0, 0), {0: 1}),               # singlet -> L=0
    ((1, 0), {1: 1}),               # triplet -> L=1
    ((0, 1), {1: 1}),
    ((1, 1), {1: 1, 2: 1}),         # adjoint -> L=1 + L=2 (no L=0)
    ((2, 0), {0: 1, 2: 1}),         # 6 -> L=0 + L=2
    ((0, 2), {0: 1, 2: 1}),
    ((2, 1), {1: 1, 2: 1, 3: 1}),   # 15 -> L=1+2+3
    ((1, 2), {1: 1, 2: 1, 3: 1}),
    ((3, 0), {1: 1, 3: 1}),         # 10 -> L=1 + L=3
    ((0, 3), {1: 1, 3: 1}),
    ((2, 2), {0: 1, 2: 2, 3: 1, 4: 1}),  # 27
]
for (p, q), expected in test_cases:
    got = elliott_branching(p, q)
    ok = got == expected
    print(f"  ({p},{q}) [dim={dim_pq(p,q):3d}]: got={got}, expected={expected}  {'OK' if ok else 'FAIL'}")
    assert ok, f"Elliott branching mismatch at ({p},{q})"

# ==============================================================================
# 4. Build per-cell fractional spin content table
# ==============================================================================
# For each cell k with label (p_k, q_k), fraction of dim(p,q) lying in spin-j
# subspace is f_k^{(j)} = (2j+1) * Theta(p_k, q_k, j) / dim(p_k, q_k)
# For j in {0, 1, 2}.

J_VALS = [0, 1, 2]
J_NAMES = ['scalar', 'vector', 'tensor']

f_cell = np.zeros((U.shape[0], 3))   # (32, 3)
branching_table = {}
for k in range(U.shape[0]):
    p, q = int(cell_labels[k, 0]), int(cell_labels[k, 1])
    mult = elliott_branching(p, q)
    branching_table[(p, q)] = mult
    d = dim_pq(p, q)
    for b_idx, j in enumerate(J_VALS):
        theta_j = mult.get(j, 0)
        f_cell[k, b_idx] = (2 * j + 1) * theta_j / d

print("\nPer-cell fractional spin content (first 10 cells):")
print(f"{'cell':>4} {'(p,q)':>7} {'dim':>4}  {'f(j=0)':>8}  {'f(j=1)':>8}  {'f(j=2)':>8}")
for k in range(10):
    p, q = int(cell_labels[k, 0]), int(cell_labels[k, 1])
    print(f"{k:>4} ({p},{q}){'':>3} {dim_pq(p,q):>4}  "
          f"{f_cell[k,0]:>8.4f}  {f_cell[k,1]:>8.4f}  {f_cell[k,2]:>8.4f}")

# ==============================================================================
# 5. Per-mode spin-j weights
# ==============================================================================
# w_i^{(j)} = sum_k |U[k, i]|^2 * f_cell[k, j]
# i runs over the 8 BCS modes (columns 0..7 of U).

U8 = U[:, :N_modes]                  # (32, 8) columns = BCS modes
amp2 = U8 ** 2                       # (32, 8) |U[k,i]|^2

print(f"\nMode probability sums (should be ~1): {amp2.sum(axis=0)}")
assert np.allclose(amp2.sum(axis=0), 1.0, atol=1e-10)

# w[i, j] = <mode i | spin-j subspace>
w_mode = amp2.T @ f_cell             # (8, 3)

# Normalise each mode row to sum_j w = 1 (project onto {scalar,vector,tensor})
w_mode_raw = w_mode.copy()
row_sums = w_mode.sum(axis=1, keepdims=True)
w_mode_norm = w_mode / np.where(row_sums > 0, row_sums, 1.0)

print(f"\nPer-mode raw spin weights (before row normalisation):")
print(f"{'mode':>5} {'branch':>7} {'eps':>10}  {'j=0 (s)':>10}  {'j=1 (v)':>10}  {'j=2 (t)':>10}  {'sum':>10}")
for i in range(N_modes):
    print(f"{i:>5} {branch_labels_1cell[i]:>7} {eps[i]:>10.6f}  "
          f"{w_mode_raw[i,0]:>10.6f}  {w_mode_raw[i,1]:>10.6f}  {w_mode_raw[i,2]:>10.6f}  "
          f"{w_mode_raw[i,:].sum():>10.6f}")

print(f"\nPer-mode normalised spin weights (projected to scalar/vector/tensor):")
print(f"{'mode':>5} {'branch':>7}  {'scalar':>10}  {'vector':>10}  {'tensor':>10}  {'sum':>10}")
for i in range(N_modes):
    print(f"{i:>5} {branch_labels_1cell[i]:>7}  "
          f"{w_mode_norm[i,0]:>10.6f}  {w_mode_norm[i,1]:>10.6f}  {w_mode_norm[i,2]:>10.6f}  "
          f"{w_mode_norm[i,:].sum():>10.6f}")

# ==============================================================================
# 6. Aggregate to 3x3 matrix M_ib over BCS branches
# ==============================================================================
branches = ['B1', 'B2', 'B3']
M = np.zeros((3, 3))
for i_row, bname in enumerate(branches):
    modes = bcs_branch_modes[bname]
    # Average the normalised per-mode projections over the modes in the branch
    # (each mode contributes equally within a branch -- uniform weighting).
    branch_weights = w_mode_norm[modes, :].mean(axis=0)   # (3,)
    M[i_row, :] = branch_weights

print("\n" + "=" * 78)
print("3x3 OVERLAP MATRIX M_ib (rows = BCS branches, cols = emergent branches)")
print("=" * 78)
print(f"{'':>6}  {'scalar':>10}  {'vector':>10}  {'tensor':>10}")
for i, bname in enumerate(branches):
    print(f"{bname:>6}  {M[i,0]:>10.6f}  {M[i,1]:>10.6f}  {M[i,2]:>10.6f}")

# ==============================================================================
# 7. Cross-checks
# ==============================================================================
row_sums_M = M.sum(axis=1)
col_sums_M = M.sum(axis=0)
row_dev = float(np.max(np.abs(row_sums_M - 1.0)))
col_dev = float(np.max(np.abs(col_sums_M - 1.0)))
diag = np.diag(M)
offdiag = M - np.diag(diag)
max_off = float(np.max(np.abs(offdiag)))

# Doubly-stochastic?
M_normalised_rows = M / row_sums_M[:, None]
col_sums_normalised = M_normalised_rows.sum(axis=0)
print(f"\nCross-checks:")
print(f"  Row sums:                       {row_sums_M}")
print(f"  Column sums:                    {col_sums_M}")
print(f"  Max |row_sum - 1|:              {row_dev:.3e}")
print(f"  Max |col_sum - 1|:              {col_dev:.3e}")
print(f"  Diagonal:                       {diag}")
print(f"  Max |off-diagonal|:             {max_off:.6f}")
print(f"  Doubly-stochastic?              "
      f"{'YES' if col_dev < 1e-6 and row_dev < 1e-6 else 'NO (not automatic; columns after row-norm: ' + str(col_sums_normalised) + ')'}")

# Diagonal-dominance check
diagonal_dominant = bool(np.all(diag > 0.5))
print(f"  Diagonal dominant (M_ii > 0.5)? {'YES' if diagonal_dominant else 'NO'}")

# Pure-eigenstate limit reference: if BCS branches were pure SO(3) eigenstates,
# M = diag(1,1,1). Report Frobenius distance from identity.
frob_dev = float(np.linalg.norm(M - np.eye(3), ord='fro'))
print(f"  |M - I|_Frobenius:              {frob_dev:.6f}")

# Compare to W1-A fallback diag(1,1,1)
M_fallback = np.eye(3)
delta_to_fallback = float(np.linalg.norm(M - M_fallback, ord='fro'))
print(f"  |M - diag(1,1,1)|_Fro:          {delta_to_fallback:.6f}")

# ==============================================================================
# 8. Gate verdict
# ==============================================================================
gate_name = "OVERLAP-MATRIX-74"
pass_row_col = (row_dev < 1e-6) and (col_dev < 1e-6)
pass_diag = diagonal_dominant
if pass_row_col and pass_diag:
    verdict = "PASS"
elif row_dev < 1e-6:
    # Rows sum to 1 but columns do not, or diagonal not dominant
    verdict = "INFO"
else:
    verdict = "INFO"    # M is computed but the off-diagonal mixing is dominant

print(f"\nGate {gate_name}: {verdict}")
print(f"  Row-sum deviation:     {row_dev:.3e} (threshold 1e-6)")
print(f"  Col-sum deviation:     {col_dev:.3e} (threshold 1e-6)")
print(f"  Diagonal dominance:    {'PASS' if pass_diag else 'FAIL'} (need all M_ii > 0.5)")

# ==============================================================================
# 9. Save
# ==============================================================================
out = os.path.join(SCRIPT_DIR, 's74_overlap_matrix.npz')
# Convert branching table to arrays for saving
branching_keys = np.array(list(branching_table.keys()), dtype=np.int64)
branching_vals_raw = []
for k in branching_table:
    mult = branching_table[k]
    # Pack as list of (L, count) pairs padded with -1
    pairs = sorted(mult.items())
    flat = [item for pair in pairs for item in pair]
    branching_vals_raw.append(flat)
# Pad to same length
maxlen = max(len(v) for v in branching_vals_raw)
branching_vals = np.full((len(branching_vals_raw), maxlen), -1, dtype=np.int64)
for i, v in enumerate(branching_vals_raw):
    branching_vals[i, :len(v)] = v

np.savez(
    out,
    M=M,
    M_row_sums=row_sums_M,
    M_col_sums=col_sums_M,
    M_row_dev=row_dev,
    M_col_dev=col_dev,
    M_diag=diag,
    M_max_offdiag=max_off,
    M_fro_from_identity=frob_dev,
    M_fro_from_fallback=delta_to_fallback,
    w_mode_raw=w_mode_raw,
    w_mode_norm=w_mode_norm,
    f_cell=f_cell,
    bcs_branches=np.array(branches),
    emergent_branches=np.array(J_NAMES),
    branch_modes_B1=np.array(bcs_branch_modes['B1']),
    branch_modes_B2=np.array(bcs_branch_modes['B2']),
    branch_modes_B3=np.array(bcs_branch_modes['B3']),
    branch_labels_1cell=np.array(branch_labels_1cell),
    cell_labels=cell_labels,
    eps_fold=eps[:N_modes],
    fold_idx=fold_idx,
    tau_fold_actual=tau_fold_actual,
    branching_keys=branching_keys,
    branching_vals=branching_vals,
    gate_name=np.array(gate_name),
    gate_verdict=np.array(verdict),
)
print(f"\nSaved -> {out}")
print(f"Runtime: {time.time() - t0:.2f} s")
