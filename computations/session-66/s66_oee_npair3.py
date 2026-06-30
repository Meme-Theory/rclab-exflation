#!/usr/bin/env python3
"""
S66 OEE-NPAIR3-66: Operator Entanglement Entropy Growth for N_pair=3
=====================================================================

Gate: OEE-NPAIR3-66
  PASS: alpha < 0.1 (log growth, integrable)
  FAIL: alpha > 1.0 (linear growth dominates, chaotic)
  INFO: 0.1 < alpha < 1.0 (intermediate)

Physics: The operator entanglement entropy (OEE) S_OEE(t) of a local operator
O(t) = e^{iHt} O e^{-iHt} measures how quickly operator "information" spreads
across subsystem boundaries. For:
  - Integrable systems: S_OEE(t) ~ alpha * ln(t) + const  [Prosen & Pizorn 2007]
  - Chaotic systems:    S_OEE(t) ~ v * t + const           [Zanardi 2001, Hosur+ 2016]

The diagnostic is:
  - Fit both ln(t) and linear forms to S_OEE(t) in the growth regime
  - Compare R^2 values to determine which fit dominates
  - Extract alpha (log coefficient) and v (linear rate)

Method:
  1. Load N_pair=3 Hamiltonian from S64 data (eps_bare, V_bare)
  2. Full diagonalization: H = U diag(E) U^dag
  3. Choose local operator O = n_1 = c_1^dag c_1 (number on mode 1)
  4. Evolve: O(t) = U e^{iEt} U^dag O U e^{-iEt} U^dag
  5. Vectorize O(t) via Choi-Jamiolkowski: |O(t)>> in H_A tensor H_B
  6. Bipartition: modes {0,1,2,3} (B2) vs {4,5,6,7} (B1+B3)
  7. Compute S_OEE(t) = -Tr(rho_A ln rho_A) where rho_A = Tr_B(|O>><<O|)
  8. Fit to ln(t) and linear forms, classify

Input: computations/session-64/s64_npair3_rg.npz
Output: computations/session-66/s66_oee_npair3.npz, s66_oee_npair3.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import curve_fit
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

# ============================================================================
# Section 1: Load S64 Data and Build Hamiltonian
# ============================================================================

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's64_npair3_rg.npz')
d = np.load(data_path, allow_pickle=True)

eps_bare = d['eps_bare']       # (8,) single-particle energies
V_bare = d['V_bare']           # (8,8) pairing interaction matrix
N_modes_val = len(eps_bare)    # 8
N_pair_val = 3                 # number of pairs

print(f"=== OEE-NPAIR3-66: Operator Entanglement Entropy ===")
print(f"N_modes = {N_modes_val}, N_pair = {N_pair_val}")
print(f"eps_bare = {eps_bare}")
print()

# Build Fock basis
def build_fock_basis(n_modes, n_pair):
    """Build all n_pair-subset configurations of n_modes levels."""
    return list(combinations(range(n_modes), n_pair))

basis = build_fock_basis(N_modes_val, N_pair_val)
dim = len(basis)
print(f"Fock space dimension: {dim}")
print(f"Operator Hilbert space dim: {dim}^2 = {dim**2}")

# Build full pairing Hamiltonian (matches S64/S65 construction EXACTLY)
def build_hamiltonian_full(eps, V, fock_basis):
    """Build full pairing Hamiltonian H = sum_k 2*eps_k n_k - sum_{kl} V_{kl} P_k^+ P_l."""
    d = len(fock_basis)
    H = np.zeros((d, d))
    for i, si in enumerate(fock_basis):
        H[i, i] = 2.0 * sum(eps[k] for k in si)
        H[i, i] -= sum(V[k, k] for k in si)
        for j in range(i + 1, d):
            sj = fock_basis[j]
            si_set = set(si)
            sj_set = set(sj)
            diff_i = si_set - sj_set
            diff_j = sj_set - si_set
            if len(diff_i) == 1 and len(diff_j) == 1:
                k = diff_i.pop()
                l = diff_j.pop()
                H[i, j] = -V[k, l]
                H[j, i] = -V[l, k]
    return H

H_full = build_hamiltonian_full(eps_bare, V_bare, basis)

# Verify against S64 eigenvalues
evals_s64 = np.sort(d['N3_evals_full'])
evals_check, evecs = eigh(H_full)
max_diff = np.max(np.abs(np.sort(evals_check) - evals_s64))
print(f"Hamiltonian verification: max|E - E_s64| = {max_diff:.2e}")
assert max_diff < 1e-8, f"Hamiltonian mismatch: {max_diff}"
print("VERIFIED: Hamiltonian matches S64 to machine epsilon")
print(f"Eigenvalue range: [{evals_check[0]:.6f}, {evals_check[-1]:.6f}]")
print(f"Bandwidth: {evals_check[-1] - evals_check[0]:.6f} M_KK")
print()

# ============================================================================
# Section 2: Build Bipartition Structure
# ============================================================================
# Bipartition: modes A = {0,1,2,3} (B2 sector), B = {4,5,6,7} (B1 + B3)
# A Fock state |S> = (k1,k2,k3) decomposes as |S> = |n_A, config_A> x |n_B, config_B>
# where n_A pairs are in A-modes and n_B = N_pair - n_A pairs are in B-modes.
#
# For the operator vectorization (Choi map):
#   |O(t)>> = sum_{i,j} O(t)_{ij} |i> tensor |j>
# in the doubled Fock space (dim x dim). The bipartition of modes induces a
# bipartition of the Fock basis. We need the tensor product structure
# H = H_A tensor H_B where H_A = span of A-sector states, H_B = span of B-sector.
#
# For the OPERATOR entanglement, the bipartition is in the doubled space:
# H_op = H tensor H* = (H_A tensor H_B) tensor (H_A* tensor H_B*)
#       = (H_A tensor H_A*) tensor (H_B tensor H_B*)
# So rho_A = Tr_{H_B tensor H_B*}(|O>><<O|)
#
# Implementation: reshape O(t) as a tensor and partial-trace over B.

modes_A = {0, 1, 2, 3}  # B2 modes
modes_B = {4, 5, 6, 7}  # B1 + B3 modes

# Classify each Fock basis state by (n_A, config_A, config_B)
# where n_A = number of pairs in A-modes
def classify_basis(fock_basis, modes_A, modes_B, n_pair):
    """For each basis state, compute (modes_in_A, modes_in_B).

    Returns: list of (tuple_A, tuple_B) for each basis state.
    """
    decomp = []
    for state in fock_basis:
        in_A = tuple(sorted(k for k in state if k in modes_A))
        in_B = tuple(sorted(k for k in state if k in modes_B))
        decomp.append((in_A, in_B))
    return decomp

decomp = classify_basis(basis, modes_A, modes_B, N_pair_val)

# Build the tensor product structure
# Get unique A-configs and B-configs
A_configs = sorted(set(d[0] for d in decomp))
B_configs = sorted(set(d[1] for d in decomp))
A_idx = {cfg: i for i, cfg in enumerate(A_configs)}
B_idx = {cfg: i for i, cfg in enumerate(B_configs)}
dim_A = len(A_configs)
dim_B = len(B_configs)

print(f"Bipartition: modes A = {sorted(modes_A)}, modes B = {sorted(modes_B)}")
print(f"dim_A = {dim_A} (A-sector configs)")
print(f"dim_B = {dim_B} (B-sector configs)")
print(f"dim_A * dim_B = {dim_A * dim_B}, dim_Fock = {dim}")

# Build the permutation matrix P: |Fock_i> -> |A_a> tensor |B_b>
# where Fock state i maps to A-config a and B-config b
# P has shape (dim, dim_A * dim_B) -- it's an isometry from dim into dim_A * dim_B
# Since every Fock state decomposes uniquely, P is an isometric embedding.

# Map: for each Fock state i, find its (a,b) indices in the A x B product
fock_to_AB = []
for i, (cfg_A, cfg_B) in enumerate(decomp):
    a = A_idx[cfg_A]
    b = B_idx[cfg_B]
    fock_to_AB.append((a, b))

# Check: is dim = dim_A * dim_B? (it will be if every (A,B) combo appears)
valid_pairs = set(fock_to_AB)
print(f"Number of valid (A,B) pairs: {len(valid_pairs)} (out of {dim_A * dim_B} possible)")

# Build the embedding: Fock index i <-> (a,b) in A x B space
# If dim < dim_A * dim_B, we need to handle the embedding carefully.
# The Fock space is a SUBSPACE of H_A tensor H_B (only particle-number-conserving states).
# For OEE, we work in the full Fock space and use the map directly.

# The operator O(t) is a dim x dim matrix.
# For OEE with bipartition A|B, we can compute:
#   |O(t)>> = sum_{i,j} O(t)_{ij} |i>|j> in H tensor H*
# where |i> = |a_i, b_i> and |j> = |a_j, b_j>.
# So |O(t)>> = sum_{i,j} O_{ij} |a_i>|b_i>|a_j>|b_j>
#            = sum_{i,j} O_{ij} |a_i, a_j> tensor |b_i, b_j>
#
# Reshape into matrix M_{(a_i,a_j), (b_i,b_j)} = O_{ij}
# Then OEE = entanglement entropy of M (via SVD).
#
# This is equivalent to: reshape O(t) from (dim, dim) into (dim_A, dim_B, dim_A, dim_B)
# then contract to (dim_A^2, dim_B^2) and compute SVD.
#
# Since Fock states don't fill the full A x B product space, we embed.

def compute_oee(O_t, fock_to_AB, dim_A, dim_B):
    """Compute operator entanglement entropy of O_t under bipartition A|B.

    O_t: (dim, dim) matrix in Fock basis
    fock_to_AB: list of (a, b) for each Fock state
    dim_A, dim_B: dimensions of A and B subsystems

    Returns: S_OEE = von Neumann entropy of the reduced operator state
    """
    dim_fock = O_t.shape[0]

    # Build the reshaped matrix M_{(a_i, a_j), (b_i, b_j)} = O_t_{i,j}
    # Row index: (a_i, a_j) -> a_i * dim_A + a_j  (dim_A^2 rows)
    # Col index: (b_i, b_j) -> b_i * dim_B + b_j  (dim_B^2 cols)
    M = np.zeros((dim_A * dim_A, dim_B * dim_B), dtype=complex)

    for i in range(dim_fock):
        a_i, b_i = fock_to_AB[i]
        for j in range(dim_fock):
            a_j, b_j = fock_to_AB[j]
            if abs(O_t[i, j]) > 1e-16:
                row = a_i * dim_A + a_j
                col = b_i * dim_B + b_j
                M[row, col] += O_t[i, j]

    # SVD of M gives Schmidt decomposition of |O>>
    # OEE = -sum_k (sigma_k^2 / sum) * ln(sigma_k^2 / sum)
    # where sigma_k are singular values
    s = np.linalg.svd(M, compute_uv=False)
    s = s[s > 1e-15]  # remove numerical zeros
    p = s**2
    p = p / p.sum()  # normalize

    # Von Neumann entropy
    S = -np.sum(p * np.log(p))  # (local)
    return S


def compute_oee_fast(O_t, fock_to_AB, dim_A, dim_B):
    """Vectorized OEE computation -- builds M via advanced indexing."""
    dim_fock = O_t.shape[0]

    # Pre-compute row and column indices for all (i,j) pairs
    ab_array = np.array(fock_to_AB)  # (dim_fock, 2)
    a_vals = ab_array[:, 0]
    b_vals = ab_array[:, 1]

    # For each (i,j), row = a_i * dim_A + a_j, col = b_i * dim_B + b_j
    row_idx = np.outer(a_vals, np.ones(dim_fock, dtype=int)) * dim_A + \
              np.outer(np.ones(dim_fock, dtype=int), a_vals)
    col_idx = np.outer(b_vals, np.ones(dim_fock, dtype=int)) * dim_B + \
              np.outer(np.ones(dim_fock, dtype=int), b_vals)

    M = np.zeros((dim_A * dim_A, dim_B * dim_B), dtype=complex)
    np.add.at(M, (row_idx.ravel(), col_idx.ravel()), O_t.ravel())

    s = np.linalg.svd(M, compute_uv=False)
    s = s[s > 1e-15]
    p = s**2
    p = p / p.sum()
    S = -np.sum(p * np.log(p))  # (local)
    return S


# ============================================================================
# Section 3: Define Local Operator O = n_1 (number on mode 1)
# ============================================================================
# The number operator n_k counts whether mode k is occupied in a Fock state.
# In the Fock basis, n_k is diagonal: <S|n_k|S> = 1 if k in S, 0 otherwise.

def build_number_op(mode_k, fock_basis):
    """Build the number operator n_k in the Fock basis."""
    d = len(fock_basis)
    n_op = np.zeros((d, d))
    for i, state in enumerate(fock_basis):
        if mode_k in state:
            n_op[i, i] = 1.0
    return n_op

# Primary operator: n_0 (mode 0 = B2[0])
O0_n0 = build_number_op(0, basis)
print(f"\nOperator O = n_0 (B2[0]): Tr = {np.trace(O0_n0):.1f}, "
      f"rank = {np.linalg.matrix_rank(O0_n0)}")

# Secondary operator: n_4 (mode 4 = B1, cross-sector probe)
O0_n4 = build_number_op(4, basis)
print(f"Operator O = n_4 (B1):   Tr = {np.trace(O0_n4):.1f}, "
      f"rank = {np.linalg.matrix_rank(O0_n4)}")

# ============================================================================
# Section 4: Time Evolution and OEE Computation
# ============================================================================

# O(t) = U diag(e^{iEt}) U^dag O U diag(e^{-iEt}) U^dag
# where H = U diag(E) U^dag

# evals_check and evecs from Section 1
# evecs[:,n] is the n-th eigenvector
E = evals_check  # eigenvalues
U = evecs         # eigenvector matrix

# Verify: U^dag H U = diag(E)
H_diag = U.T @ H_full @ U
diag_err = np.max(np.abs(H_diag - np.diag(E)))
print(f"\nDiagonalization check: max|U^T H U - diag(E)| = {diag_err:.2e}")

# Time grid
t_max = 100.0  # M_KK^{-1} (local)
n_steps = 1000  # (local)
t_values = np.linspace(0, t_max, n_steps + 1)

# Pre-compute U^dag O U for both operators
UdagO0U_n0 = U.T @ O0_n0 @ U  # (dim, dim) in energy basis
UdagO0U_n4 = U.T @ O0_n4 @ U

print(f"\nTime evolution: t in [0, {t_max}] M_KK^-1, {n_steps+1} steps")
print(f"Heisenberg time t_H = 2*pi*dim/bandwidth = "
      f"{2*np.pi*dim/(E[-1]-E[0]):.2f} M_KK^-1")
t_H = 2 * np.pi * dim / (E[-1] - E[0])

# Pre-compute A_ij = (U^dag O U)_{ij} -- the matrix elements in energy basis
# O(t)_{ab} = sum_{i,j} U_{a,i} A_{ij} U_{b,j} exp(i*(E_i - E_j)*t)
# This is just U @ (A * exp_matrix(t)) @ U^T

def evolve_operator(A_energy, E_vals, U_mat, t):
    """Compute O(t) = U exp(iEt) A exp(-iEt) U^T in Fock basis.

    A_energy: (dim,dim) = U^T O U (operator in energy basis)
    E_vals: (dim,) eigenvalues
    U_mat: (dim,dim) eigenvectors
    t: time

    Returns: O(t) in Fock basis, shape (dim,dim)
    """
    # Phase factors: exp(i*(E_i - E_j)*t)
    phases = np.exp(1j * np.subtract.outer(E_vals, E_vals) * t)
    # O(t) in energy basis = A .* phases
    O_energy = A_energy * phases
    # Transform back to Fock basis
    O_fock = U_mat @ O_energy @ U_mat.T
    return O_fock

# Compute OEE(t) for both operators
print("\nComputing OEE(t) for O = n_0 (B2[0])...")
t_start = time.time()

# Pre-compute row/col indices for fast OEE
ab_array = np.array(fock_to_AB, dtype=int)
a_vals = ab_array[:, 0]
b_vals = ab_array[:, 1]
row_idx_flat = (np.outer(a_vals, np.ones(dim, dtype=int)) * dim_A +
                np.outer(np.ones(dim, dtype=int), a_vals)).ravel()
col_idx_flat = (np.outer(b_vals, np.ones(dim, dtype=int)) * dim_B +
                np.outer(np.ones(dim, dtype=int), b_vals)).ravel()

def compute_oee_precomputed(O_t, row_idx, col_idx, dim_A_sq, dim_B_sq):
    """OEE with pre-computed indices."""
    M = np.zeros((dim_A_sq, dim_B_sq), dtype=complex)
    np.add.at(M, (row_idx, col_idx), O_t.ravel())
    s = np.linalg.svd(M, compute_uv=False)
    s = s[s > 1e-15]
    p = s**2
    p = p / p.sum()
    return -np.sum(p * np.log(p))

dim_A_sq = dim_A * dim_A
dim_B_sq = dim_B * dim_B

# Energy difference matrix (precompute)
dE = np.subtract.outer(E, E)  # (dim, dim)

S_oee_n0 = np.zeros(n_steps + 1)
S_oee_n4 = np.zeros(n_steps + 1)

for step_i, t in enumerate(t_values):
    if step_i % 200 == 0:
        print(f"  step {step_i}/{n_steps}, t = {t:.1f}")

    # Compute O(t) for n_0
    phases = np.exp(1j * dE * t)
    O_t_energy_n0 = UdagO0U_n0 * phases
    O_t_fock_n0 = U @ O_t_energy_n0 @ U.T
    S_oee_n0[step_i] = compute_oee_precomputed(
        O_t_fock_n0, row_idx_flat, col_idx_flat, dim_A_sq, dim_B_sq)

    # Compute O(t) for n_4
    O_t_energy_n4 = UdagO0U_n4 * phases
    O_t_fock_n4 = U @ O_t_energy_n4 @ U.T
    S_oee_n4[step_i] = compute_oee_precomputed(
        O_t_fock_n4, row_idx_flat, col_idx_flat, dim_A_sq, dim_B_sq)

elapsed = time.time() - t_start
print(f"Time evolution complete: {elapsed:.1f}s")

# ============================================================================
# Section 5: Initial Values and Sanity Checks
# ============================================================================

print(f"\n=== OEE Results ===")
print(f"S_OEE(t=0) for n_0: {S_oee_n0[0]:.6f}")
print(f"S_OEE(t=0) for n_4: {S_oee_n4[0]:.6f}")
print(f"S_OEE max for n_0:  {np.max(S_oee_n0):.6f}")
print(f"S_OEE max for n_4:  {np.max(S_oee_n4):.6f}")

# Maximum possible OEE: log(min(dim_A^2, dim_B^2))
S_max = np.log(min(dim_A_sq, dim_B_sq))
print(f"S_OEE max possible: log(min({dim_A_sq},{dim_B_sq})) = {S_max:.4f}")
print(f"S_OEE(n_0) / S_max = {np.max(S_oee_n0)/S_max:.4f}")
print(f"S_OEE(n_4) / S_max = {np.max(S_oee_n4)/S_max:.4f}")

# ============================================================================
# Section 6: Fitting — Log vs Linear Growth
# ============================================================================

# For fitting, use t > t_min to skip the trivial early-time regime (t^2 from BCH)
# and t < t_sat where the entropy saturates.
# Choose t_min = 1.0 (several oscillation periods) and t_sat from saturation detection.

t_min_fit = 1.0  # (local)
t_max_fit = t_max  # use full range initially

# Helper: detect saturation time (where S_OEE reaches 90% of its max and stays)
def find_saturation(S, t_arr, frac=0.90):
    """Find earliest time where S(t) >= frac * max(S) for the rest of the array."""
    S_thresh = frac * np.max(S)
    for i in range(len(S)):
        if np.all(S[i:] >= 0.8 * S_thresh):  # roughly stays above
            return t_arr[i]
    return t_arr[-1]

t_sat_n0 = find_saturation(S_oee_n0, t_values)
t_sat_n4 = find_saturation(S_oee_n4, t_values)
print(f"\nSaturation time (90% of max): n_0: {t_sat_n0:.1f}, n_4: {t_sat_n4:.1f}")

# Fit in the growth regime: t_min_fit < t < t_sat
def fit_growth(S, t_arr, t_min, t_max_f, label=""):
    """Fit S(t) to both log(t) and linear forms in [t_min, t_max_f]."""
    mask = (t_arr > t_min) & (t_arr < t_max_f) & (S > 0) & np.isfinite(S)
    t_fit = t_arr[mask]
    S_fit = S[mask]

    if len(t_fit) < 10:
        print(f"  {label}: insufficient points for fitting ({len(t_fit)})")
        return None

    # Log fit: S = alpha * ln(t) + c_log
    def log_model(t, alpha, c):
        return alpha * np.log(t) + c

    # Linear fit: S = v * t + c_lin
    def lin_model(t, v, c):
        return v * t + c

    try:
        popt_log, _ = curve_fit(log_model, t_fit, S_fit, p0=[0.1, S_fit[0]])
        alpha = popt_log[0]
        S_pred_log = log_model(t_fit, *popt_log)
        SS_res_log = np.sum((S_fit - S_pred_log)**2)
        SS_tot = np.sum((S_fit - np.mean(S_fit))**2)
        R2_log = 1 - SS_res_log / SS_tot if SS_tot > 0 else 0
    except Exception as e:
        print(f"  {label}: log fit failed: {e}")
        alpha, R2_log = np.nan, 0
        popt_log = [np.nan, np.nan]

    try:
        popt_lin, _ = curve_fit(lin_model, t_fit, S_fit, p0=[0.01, S_fit[0]])
        v_lin = popt_lin[0]
        S_pred_lin = lin_model(t_fit, *popt_lin)
        SS_res_lin = np.sum((S_fit - S_pred_lin)**2)
        SS_tot = np.sum((S_fit - np.mean(S_fit))**2)
        R2_lin = 1 - SS_res_lin / SS_tot if SS_tot > 0 else 0
    except Exception as e:
        print(f"  {label}: linear fit failed: {e}")
        v_lin, R2_lin = np.nan, 0
        popt_lin = [np.nan, np.nan]

    # Power law: S = A * t^beta + c (general form to identify growth exponent)
    def power_model(t, A, beta, c):
        return A * np.power(t, beta) + c

    try:
        popt_pow, _ = curve_fit(power_model, t_fit, S_fit,
                                 p0=[0.1, 0.3, S_fit[0]], maxfev=5000,
                                 bounds=([0, 0, -np.inf], [np.inf, 2.0, np.inf]))
        beta_pow = popt_pow[1]
        S_pred_pow = power_model(t_fit, *popt_pow)
        SS_res_pow = np.sum((S_fit - S_pred_pow)**2)
        SS_tot = np.sum((S_fit - np.mean(S_fit))**2)
        R2_pow = 1 - SS_res_pow / SS_tot if SS_tot > 0 else 0
    except Exception as e:
        print(f"  {label}: power fit failed: {e}")
        beta_pow, R2_pow = np.nan, 0
        popt_pow = [np.nan, np.nan, np.nan]

    result = {
        'alpha': alpha, 'R2_log': R2_log, 'popt_log': popt_log,
        'v_lin': v_lin, 'R2_lin': R2_lin, 'popt_lin': popt_lin,
        'beta_pow': beta_pow, 'R2_pow': R2_pow, 'popt_pow': popt_pow,
        't_fit': t_fit, 'S_fit': S_fit,
    }

    print(f"\n  {label} fits (t in [{t_min:.1f}, {t_max_f:.1f}], {len(t_fit)} points):")
    print(f"    Log:    S = {alpha:.4f} * ln(t) + {popt_log[1]:.4f}  "
          f"(R^2 = {R2_log:.4f})")
    print(f"    Linear: S = {v_lin:.6f} * t + {popt_lin[1]:.4f}  "
          f"(R^2 = {R2_lin:.4f})")
    print(f"    Power:  S = {popt_pow[0]:.4f} * t^{beta_pow:.3f} + {popt_pow[2]:.4f}  "
          f"(R^2 = {R2_pow:.4f})")
    print(f"    Best fit: {'LOG' if R2_log > R2_lin else 'LINEAR'} "
          f"(R2_log/R2_lin = {R2_log/R2_lin if R2_lin > 0 else np.inf:.3f})")

    return result

# Fit both operators
print(f"\n=== Fitting Growth Forms ===")

# For n_0 (intra-A operator)
result_n0 = fit_growth(S_oee_n0, t_values, t_min_fit, min(t_sat_n0, t_max), "n_0 (B2[0])")

# For n_4 (cross-sector operator, in B-sector)
result_n4 = fit_growth(S_oee_n4, t_values, t_min_fit, min(t_sat_n4, t_max), "n_4 (B1)")

# Also fit in a more restricted window to check robustness
print(f"\n=== Robustness Check: Restricted Window [2, 50] ===")
result_n0_r = fit_growth(S_oee_n0, t_values, 2.0, 50.0, "n_0 restricted")
result_n4_r = fit_growth(S_oee_n4, t_values, 2.0, 50.0, "n_4 restricted")

# ============================================================================
# Section 7: Gate Verdict
# ============================================================================

# Use the primary operator n_0 for the gate
alpha_gate = result_n0['alpha'] if result_n0 is not None else np.nan
R2_log_gate = result_n0['R2_log'] if result_n0 is not None else 0
R2_lin_gate = result_n0['R2_lin'] if result_n0 is not None else 0
v_lin_gate = result_n0['v_lin'] if result_n0 is not None else np.nan
beta_gate = result_n0['beta_pow'] if result_n0 is not None else np.nan

print(f"\n{'='*60}")
print(f"=== GATE VERDICT: OEE-NPAIR3-66 ===")
print(f"{'='*60}")
print(f"Primary operator: n_0 (B2[0])")
print(f"alpha (log coefficient): {alpha_gate:.4f}")
print(f"v (linear rate):         {v_lin_gate:.6f}")
print(f"beta (power exponent):   {beta_gate:.4f}")
print(f"R^2(log):                {R2_log_gate:.4f}")
print(f"R^2(linear):             {R2_lin_gate:.4f}")
print(f"R^2(power):              {result_n0['R2_pow']:.4f}")
print(f"Best fit form:           {'LOG' if R2_log_gate > R2_lin_gate else 'LINEAR'}")

if alpha_gate < 0.1:
    verdict = "PASS"
    reason = f"alpha = {alpha_gate:.4f} < 0.1 (log growth, INTEGRABLE)"
elif alpha_gate > 1.0:
    verdict = "FAIL"
    reason = f"alpha = {alpha_gate:.4f} > 1.0 (linear growth dominates, CHAOTIC)"
else:
    verdict = "INFO"
    reason = f"alpha = {alpha_gate:.4f} in [0.1, 1.0] (intermediate)"

# Additional: if log fits much better, the system is integrable regardless
if R2_log_gate > 0.9 and R2_log_gate > R2_lin_gate and v_lin_gate < 0.01:
    verdict_note = "LOG FIT DOMINATES: integrable operator spreading"
elif R2_lin_gate > 0.9 and R2_lin_gate > R2_log_gate:
    verdict_note = "LINEAR FIT DOMINATES: chaotic operator spreading"
else:
    verdict_note = f"Neither fit dominant (R2_log={R2_log_gate:.3f}, R2_lin={R2_lin_gate:.3f})"

print(f"\nVerdict: {verdict}")
print(f"Reason:  {reason}")
print(f"Note:    {verdict_note}")

# Cross-check with n_4 (cross-sector)
if result_n4 is not None:
    alpha_n4 = result_n4['alpha']
    print(f"\nCross-check (n_4 B1): alpha = {alpha_n4:.4f}, "
          f"R2_log = {result_n4['R2_log']:.4f}, R2_lin = {result_n4['R2_lin']:.4f}")
    print(f"  beta_pow = {result_n4['beta_pow']:.4f}, R2_pow = {result_n4['R2_pow']:.4f}")

# ============================================================================
# Section 8: Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'OEE-NPAIR3-66: Operator Entanglement Entropy\n'
             f'N_pair=3, 8 modes, dim={dim}. Gate: {verdict}',
             fontsize=13, fontweight='bold')

# Panel (a): S_OEE(t) for both operators -- linear scale
ax = axes[0, 0]
ax.plot(t_values, S_oee_n0, 'b-', lw=0.8, label=f'n_0 (B2[0])')
ax.plot(t_values, S_oee_n4, 'r-', lw=0.8, label=f'n_4 (B1)')
ax.axhline(S_max, color='gray', ls='--', lw=0.5, label=f'S_max = {S_max:.2f}')
ax.axvline(t_H, color='green', ls=':', lw=0.5, label=f't_H = {t_H:.1f}')
ax.set_xlabel(r't  [$M_{KK}^{-1}$]')
ax.set_ylabel(r'$S_{OEE}(t)$')
ax.set_title('(a) OEE vs time')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): S_OEE(t) vs ln(t) -- test for log growth
ax = axes[0, 1]
mask_pos = t_values > 0.1
ax.plot(np.log(t_values[mask_pos]), S_oee_n0[mask_pos], 'b-', lw=0.8, label='n_0 data')
ax.plot(np.log(t_values[mask_pos]), S_oee_n4[mask_pos], 'r-', lw=0.8, label='n_4 data')
if result_n0 is not None:
    t_f = result_n0['t_fit']
    ax.plot(np.log(t_f), result_n0['popt_log'][0]*np.log(t_f) + result_n0['popt_log'][1],
            'b--', lw=1.5, label=f'n_0 log fit: a={result_n0["alpha"]:.3f}, R2={result_n0["R2_log"]:.3f}')
if result_n4 is not None:
    t_f = result_n4['t_fit']
    ax.plot(np.log(t_f), result_n4['popt_log'][0]*np.log(t_f) + result_n4['popt_log'][1],
            'r--', lw=1.5, label=f'n_4 log fit: a={result_n4["alpha"]:.3f}, R2={result_n4["R2_log"]:.3f}')
ax.set_xlabel(r'$\ln(t)$')
ax.set_ylabel(r'$S_{OEE}$')
ax.set_title(r'(b) OEE vs $\ln(t)$ — log growth test')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel (c): S_OEE(t) vs t -- test for linear growth
ax = axes[1, 0]
ax.plot(t_values, S_oee_n0, 'b-', lw=0.8, label='n_0 data')
ax.plot(t_values, S_oee_n4, 'r-', lw=0.8, label='n_4 data')
if result_n0 is not None:
    t_f = result_n0['t_fit']
    ax.plot(t_f, result_n0['popt_lin'][0]*t_f + result_n0['popt_lin'][1],
            'b--', lw=1.5, label=f'n_0 lin: v={result_n0["v_lin"]:.5f}, R2={result_n0["R2_lin"]:.3f}')
if result_n4 is not None:
    t_f = result_n4['t_fit']
    ax.plot(t_f, result_n4['popt_lin'][0]*t_f + result_n4['popt_lin'][1],
            'r--', lw=1.5, label=f'n_4 lin: v={result_n4["v_lin"]:.5f}, R2={result_n4["R2_lin"]:.3f}')
ax.set_xlabel(r't  [$M_{KK}^{-1}$]')
ax.set_ylabel(r'$S_{OEE}(t)$')
ax.set_title('(c) OEE vs t — linear growth test')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel (d): Power-law fit on log-log scale
ax = axes[1, 1]
mask_pos2 = t_values > 0.5
ax.plot(np.log10(t_values[mask_pos2]), np.log10(np.maximum(S_oee_n0[mask_pos2], 1e-10)),
        'b-', lw=0.8, label='n_0 data')
ax.plot(np.log10(t_values[mask_pos2]), np.log10(np.maximum(S_oee_n4[mask_pos2], 1e-10)),
        'r-', lw=0.8, label='n_4 data')
if result_n0 is not None and not np.isnan(result_n0['beta_pow']):
    ax.axhline(np.log10(np.max(S_oee_n0)), color='b', ls=':', lw=0.5)
    ax.text(0.05, 0.95, f'n_0: beta={result_n0["beta_pow"]:.3f} (R2={result_n0["R2_pow"]:.3f})',
            transform=ax.transAxes, fontsize=9, va='top', color='b')
if result_n4 is not None and not np.isnan(result_n4['beta_pow']):
    ax.text(0.05, 0.88, f'n_4: beta={result_n4["beta_pow"]:.3f} (R2={result_n4["R2_pow"]:.3f})',
            transform=ax.transAxes, fontsize=9, va='top', color='r')
ax.set_xlabel(r'$\log_{10}(t)$')
ax.set_ylabel(r'$\log_{10}(S_{OEE})$')
ax.set_title('(d) Log-log — power law exponent')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's66_oee_npair3.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"\nPlot saved: {plot_path}")

# ============================================================================
# Section 9: Save Data
# ============================================================================

save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         's66_oee_npair3.npz')

save_dict = {
    # Time grid
    't_values': t_values,
    't_max': t_max,
    'n_steps': n_steps,
    't_H': t_H,

    # OEE curves
    'S_oee_n0': S_oee_n0,
    'S_oee_n4': S_oee_n4,
    'S_max': S_max,

    # Hamiltonian info
    'N_modes': N_modes_val,
    'N_pair': N_pair_val,
    'dim': dim,
    'dim_A': dim_A,
    'dim_B': dim_B,
    'eigenvalues': E,

    # Bipartition
    'modes_A': np.array(sorted(modes_A)),
    'modes_B': np.array(sorted(modes_B)),

    # Fit results (n_0)
    'alpha_n0': result_n0['alpha'] if result_n0 else np.nan,
    'R2_log_n0': result_n0['R2_log'] if result_n0 else np.nan,
    'v_lin_n0': result_n0['v_lin'] if result_n0 else np.nan,
    'R2_lin_n0': result_n0['R2_lin'] if result_n0 else np.nan,
    'beta_pow_n0': result_n0['beta_pow'] if result_n0 else np.nan,
    'R2_pow_n0': result_n0['R2_pow'] if result_n0 else np.nan,

    # Fit results (n_4)
    'alpha_n4': result_n4['alpha'] if result_n4 else np.nan,
    'R2_log_n4': result_n4['R2_log'] if result_n4 else np.nan,
    'v_lin_n4': result_n4['v_lin'] if result_n4 else np.nan,
    'R2_lin_n4': result_n4['R2_lin'] if result_n4 else np.nan,
    'beta_pow_n4': result_n4['beta_pow'] if result_n4 else np.nan,
    'R2_pow_n4': result_n4['R2_pow'] if result_n4 else np.nan,

    # Gate
    'gate_name': 'OEE-NPAIR3-66',
    'gate_verdict': verdict,
    'gate_reason': reason,
    'gate_note': verdict_note,
}

np.savez(save_path, **save_dict)
print(f"Data saved: {save_path}")

print(f"\n{'='*60}")
print(f"FINAL: OEE-NPAIR3-66 = {verdict}")
print(f"  alpha = {alpha_gate:.4f}")
print(f"  R2_log = {R2_log_gate:.4f}, R2_lin = {R2_lin_gate:.4f}")
print(f"  Best fit: {'LOG (integrable)' if R2_log_gate > R2_lin_gate else 'LINEAR (chaotic)'}")
print(f"{'='*60}")
