#!/usr/bin/env python3
"""
s63_local_entangle.py — Local Entanglement Entropy of GGE State Across Rindler Cut
===================================================================================

Session 63, Gate: LOCAL-ENTANGLE-63
  INFO: Report S_ent magnitude.
        S_ent > 0 opens Jacobson CC path (Jacobson 1995: dQ = T dS => Einstein eqs).
        S_ent = 0 confirms 9th closure of Jacobson route.  # (local)

Physics:
  The GGE state is a product state in the QUASIPARTICLE (Bogoliubov mode) basis:
    rho_GGE = prod_k [n_k |1_k><1_k| + (1-n_k) |0_k><0_k|]

  In the global Fock space, S_ent = 0 (no mode-mode entanglement). This was
  confirmed in S59.

  BUT: Jacobson's thermodynamic derivation of Einstein equations uses LOCAL
  entanglement entropy across a Rindler horizon. On the discrete graph (32-cell
  BCC tessellation), we bipartition into two spatial hemispheres of 16 vertices.

  Even though the GGE is a product state in mode basis, the Bogoliubov modes are
  DELOCALIZED across the graph. Spatial bipartition generically generates nonzero
  entanglement entropy because:
    - Mode k has weight |V[i,k]|^2 at site i
    - Tracing over sites in B projects out the B-components of each mode
    - This creates entanglement between A and B in the SITE basis

  For Gaussian states, S_ent is determined entirely by the eigenvalues of the
  restricted correlation matrix C_A (Peschel 2003, Peschel-Eisler 2009).

Method:
  1. Load 32x32 TB eigenvectors V[i,k] and GGE occupations n_k
  2. Build normal correlation matrix: C_ij = sum_k n_k * V[i,k] * V[j,k]
  3. Build anomalous correlation matrix: F_ij = sum_k f_k * V[i,k] * V[j,k]
  4. Find maximal balanced bipartition (16+16) via spectral + greedy optimization
  5. Restrict C,F to region A -> C_A, F_A (16x16 each)
  6. Compute entanglement entropy via Peschel formula:
     S = -sum_alpha [nu_alpha * ln(nu_alpha) + (1-nu_alpha) * ln(1-nu_alpha)]  # (local)
     where nu_alpha are eigenvalues of C_A (for normal correlations only)
  7. For full BCS with anomalous: use 2Nx2N covariance matrix method
  8. Compute mutual information I(A:B) = S(A) + S(B) - S(AB) = 2*S(A) - 0 = 2*S(A)
  9. If S_ent > 0: compute Lambda_Jacobson = T_ent * S_ent / V_cell
  10. Multiple bipartitions for robustness: spectral, random-max, min-cut

Inputs:
  computations/session-54/s54_tb_hamiltonian.npz
  computations/session-56/s56_gge_fabric.npz
  computations/session-62/s62_meissner_gge.npz
  computations/session-62/s62_cc_qtheory_gge.npz

Outputs:
  computations/session-63/s63_local_entangle.npz
  computations/session-63/s63_local_entangle.png

Author: Hawking-Theorist Agent (S63)
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh, svd, logm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    N_cells, a2_fold, tau_fold, J_C2, PI,
    M_KK, M_KK_gravity, rho_Lambda_obs, M_Pl_unreduced,
    a0_fold, G_N, hbar_SI, c_light, k_B
)

data_dir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("S63 W3-01: Local Entanglement Entropy of GGE Across Rindler Cut")
print("Gate: LOCAL-ENTANGLE-63")
print("=" * 72)

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================
print("\n--- Section 1: Loading input data ---")

# TB Hamiltonian: graph structure and eigenstates
d54 = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)
adj = d54['adjacency'].astype(int)                # (32, 32)
tau_arr = d54['tau_values']
fold_idx = np.argmin(np.abs(tau_arr - tau_fold))
H_fold = d54['hamiltonians'][fold_idx]             # (32, 32) TB Hamiltonian at fold
eigs_tb = d54['eigenvalues'][fold_idx]             # 32 eigenvalues
V_tb = d54['eigenvectors'][fold_idx]               # (32, 32) eigenvectors: V[site, mode]
cell_labels = d54['cell_labels']                   # (32, 2) SU(3) irrep labels (p,q)
cell_dims = d54['cell_dims']                       # (32,) irrep dimensions

N = adj.shape[0]
N_edges = int(np.sum(adj)) // 2
N_modes = 8  # BCS modes (first 8 TB eigenstates) (local)

print(f"  Graph: {N} vertices, {N_edges} edges")
print(f"  Fold: tau = {tau_arr[fold_idx]:.4f} (idx {fold_idx})")
print(f"  TB eigenvalues (first 8): {eigs_tb[:8]}")

# GGE occupation data
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']      # 8 single-particle energies
V_pair = d56['V_fold']          # 8x8 pairing matrix

d62m = np.load(os.path.join(data_dir, 's62_meissner_gge.npz'), allow_pickle=True)
n_k_GGE = d62m['n_k_GGE']     # 8 GGE occupation numbers
n_k_GS = d62m['n_k_GS']       # 8 ground state occupation numbers
F_k_GGE = d62m['F_k_GGE']     # 8 anomalous pairing amplitudes (GGE)
F_k_GS = d62m['F_k_GS']       # 8 anomalous pairing amplitudes (GS)

# CC data for comparison
d62c = np.load(os.path.join(data_dir, 's62_cc_qtheory_gge.npz'), allow_pickle=True)
CC_gap_OOM = float(d62c['CC_gap_OOM'])

print(f"\n  GGE occupations n_k: {n_k_GGE}")
print(f"  GGE pairing F_k:    {F_k_GGE}")
print(f"  Sum(n_k) = {n_k_GGE.sum():.6f}")

# Verify mode-eigenvalue correspondence
assert np.allclose(eigs_tb[:N_modes], eps_fold), \
    "BCS modes don't match first 8 TB eigenvalues!"
print("  VERIFIED: eps_fold matches first 8 TB eigenvalues")

# =====================================================================
#  2. VERIFY EIGENVECTOR ORTHOGONALITY AND COMPLETENESS
# =====================================================================
print("\n--- Section 2: Verify eigenvector properties ---")

orth_check = V_tb.T @ V_tb
max_orth_err = np.max(np.abs(orth_check - np.eye(N)))
print(f"  Orthonormality: max|V^T V - I| = {max_orth_err:.2e}")
assert max_orth_err < 1e-12, f"Eigenvectors not orthonormal: {max_orth_err}"

# Check eigendecomposition
H_recon = V_tb @ np.diag(eigs_tb) @ V_tb.T
recon_err = np.max(np.abs(H_recon - H_fold))
print(f"  Eigendecomposition: max|V D V^T - H| = {recon_err:.2e}")
assert recon_err < 1e-10, f"Eigendecomposition failed: {recon_err}"

# Weight of each BCS mode at each site
print("\n  Mode weights |V[i,k]|^2 (first 4 modes, first 8 sites):")
for k in range(min(4, N_modes)):
    weights = V_tb[:8, k]**2
    print(f"    k={k}: {weights}")

# Localization measure: inverse participation ratio
print("\n  Inverse participation ratio (IPR) for BCS modes:")
for k in range(N_modes):
    ipr = np.sum(V_tb[:, k]**4)
    print(f"    k={k}: IPR = {ipr:.4f}, participation = {1.0/ipr:.2f} sites")

# =====================================================================
#  3. BUILD CORRELATION MATRICES IN SITE BASIS
# =====================================================================
print("\n--- Section 3: Correlation matrices ---")

# Normal correlation matrix: C_ij = sum_k n_k * V[i,k] * V[j,k]
# For the GGE state with 8 occupied modes:
C_GGE = np.zeros((N, N))
for k in range(N_modes):
    C_GGE += n_k_GGE[k] * np.outer(V_tb[:, k], V_tb[:, k])

# Verify: Tr(C) = sum(n_k)
tr_C = np.trace(C_GGE)
sum_nk = n_k_GGE.sum()
print(f"  Tr(C_GGE) = {tr_C:.8f}")
print(f"  Sum(n_k)  = {sum_nk:.8f}")
print(f"  Match: {np.isclose(tr_C, sum_nk)}")

# Also build the ground state correlation matrix for comparison
C_GS = np.zeros((N, N))
for k in range(N_modes):
    C_GS += n_k_GS[k] * np.outer(V_tb[:, k], V_tb[:, k])

print(f"  Tr(C_GS) = {np.trace(C_GS):.8f}, Sum(n_k_GS) = {n_k_GS.sum():.8f}")

# Anomalous correlation matrix: F_ij = sum_k f_k * V[i,k] * V[j,k]
# This captures BCS pairing correlations
F_GGE_mat = np.zeros((N, N))
for k in range(N_modes):
    F_GGE_mat += F_k_GGE[k] * np.outer(V_tb[:, k], V_tb[:, k])

F_GS_mat = np.zeros((N, N))
for k in range(N_modes):
    F_GS_mat += F_k_GS[k] * np.outer(V_tb[:, k], V_tb[:, k])

# Eigenvalues of C_GGE should all be in [0, 1] for a valid correlation matrix
eigs_C = np.linalg.eigvalsh(C_GGE)
print(f"\n  C_GGE eigenvalues: min = {eigs_C.min():.6e}, max = {eigs_C.max():.6e}")
print(f"  All in [0,1]: {np.all(eigs_C >= -1e-14) and np.all(eigs_C <= 1+1e-14)}")

# =====================================================================
#  4. FIND MAXIMAL BALANCED BIPARTITION
# =====================================================================
print("\n--- Section 4: Maximal balanced bipartition (16+16) ---")

# Method: spectral (Fiedler vector) + greedy refinement

# Graph Laplacian
D_diag = np.diag(adj.sum(axis=1).astype(float))
L = D_diag - adj.astype(float)
evals_L, evecs_L = np.linalg.eigh(L)
fiedler = evecs_L[:, 1]

# Initial partition from Fiedler: top 16 by Fiedler value
sorted_idx = np.argsort(fiedler)
A_spectral = set(sorted_idx[16:].tolist())
B_spectral = set(sorted_idx[:16].tolist())

def cut_size(A_set, adj_matrix):
    r"""Number of edges crossing from A to B = V\A."""
    cut = 0
    for i in A_set:
        for j in range(adj_matrix.shape[0]):
            if j not in A_set and adj_matrix[i, j]:
                cut += 1
    return cut

cut_spectral = cut_size(A_spectral, adj)
print(f"  Spectral partition cut: {cut_spectral} edges")

# Greedy swap optimization from spectral partition
A_greedy = set(A_spectral)
best_cut_greedy = cut_spectral
for _ in range(1000):
    improved = False
    for i in list(A_greedy):
        for j in range(N):
            if j in A_greedy:
                continue
            new_A = (A_greedy - {i}) | {j}
            new_cut = cut_size(new_A, adj)
            if new_cut > best_cut_greedy:
                best_cut_greedy = new_cut
                A_greedy = new_A
                improved = True
                break
        if improved:
            break
    if not improved:
        break

print(f"  Greedy-optimized cut: {best_cut_greedy} edges")
print(f"  A_max = {sorted(A_greedy)}")

# Also try random search for max cut
np.random.seed(42)
A_random_best = set(A_greedy)
cut_random_best = best_cut_greedy
for _ in range(200000):
    perm = np.random.permutation(N)
    A_try = set(perm[:16].tolist())
    c = cut_size(A_try, adj)
    if c > cut_random_best:
        cut_random_best = c
        A_random_best = set(A_try)

print(f"  Random search best cut: {cut_random_best} edges")
if cut_random_best > best_cut_greedy:
    A_max = A_random_best
    cut_max = cut_random_best
    # Greedy refine from random best
    for _ in range(1000):
        improved = False
        for i in list(A_max):
            for j in range(N):
                if j in A_max:
                    continue
                new_A = (A_max - {i}) | {j}
                new_cut = cut_size(new_A, adj)
                if new_cut > cut_max:
                    cut_max = new_cut
                    A_max = new_A
                    improved = True
                    break
            if improved:
                break
        if not improved:
            break
    print(f"  After greedy from random: {cut_max} edges")
else:
    A_max = A_greedy
    cut_max = best_cut_greedy

A_max_sorted = sorted(A_max)
B_max_sorted = sorted(set(range(N)) - A_max)
print(f"\n  FINAL max-cut partition:")
print(f"    A = {A_max_sorted}")
print(f"    B = {B_max_sorted}")
print(f"    Cut edges: {cut_max} / {N_edges} total ({100*cut_max/N_edges:.1f}%)")

# Also find the MIN-cut balanced partition for comparison (Fiedler-based)
A_min = set(sorted_idx[:16].tolist())
cut_min_init = cut_size(A_min, adj)
# Greedy minimize
A_min_greedy = set(A_min)
best_cut_min = cut_min_init
for _ in range(1000):
    improved = False
    for i in list(A_min_greedy):
        for j in range(N):
            if j in A_min_greedy:
                continue
            new_A = (A_min_greedy - {i}) | {j}
            new_cut = cut_size(new_A, adj)
            if new_cut < best_cut_min:
                best_cut_min = new_cut
                A_min_greedy = new_A
                improved = True
                break
        if improved:
            break
    if not improved:
        break

print(f"  Min-cut balanced partition: {best_cut_min} edges")

# =====================================================================
#  5. COMPUTE ENTANGLEMENT ENTROPY VIA PESCHEL METHOD
# =====================================================================
print("\n--- Section 5: Entanglement entropy (Peschel method) ---")

def entanglement_entropy_gaussian(C_full, A_indices):
    """
    Compute von Neumann entanglement entropy of a Gaussian (free-fermion)
    state across a spatial bipartition.

    For a Gaussian state defined by correlation matrix C_ij = <c_i^dag c_j>,
    the entanglement entropy of subsystem A is:

    S_A = -sum_alpha [nu_alpha * ln(nu_alpha) + (1-nu_alpha) * ln(1-nu_alpha)]

    where nu_alpha are eigenvalues of C_A = C[A,A].

    Reference: Peschel, J. Phys. A 36 (2003) L205.
    """
    A_idx = np.array(sorted(A_indices))
    C_A = C_full[np.ix_(A_idx, A_idx)]

    # Eigenvalues of restricted correlation matrix
    nu = np.linalg.eigvalsh(C_A)

    # Compute entropy only from eigenvalues strictly between 0 and 1
    # (eigenvalues at 0 or 1 contribute zero entropy)
    tol = 1e-14  # (local)
    mask = (nu > tol) & (nu < 1.0 - tol)
    nu_active = nu[mask]

    S = -np.sum(nu_active * np.log(nu_active) +  # (local)
                (1.0 - nu_active) * np.log(1.0 - nu_active))

    # Number of effective entangled modes
    n_eff = np.sum((nu > 1e-10) & (nu < 1.0 - 1e-10))

    return S, nu, n_eff, C_A


def entanglement_entropy_bcs(C_full, F_full, A_indices):
    """
    Compute entanglement entropy for a BCS-type Gaussian state including
    anomalous (pairing) correlations.

    The generalized covariance matrix is:
    Gamma = [[C_A, F_A], [-F_A^*, I - C_A^*]]

    (Peschel-Eisler 2009, Eq. 11)

    The entanglement entropy is:
    S = -sum_alpha [lambda_alpha * ln(lambda_alpha) + (1-lambda_alpha) * ln(1-lambda_alpha)]  # (local)

    where lambda_alpha are eigenvalues of the 2N_A x 2N_A matrix Gamma_A.
    """
    A_idx = np.array(sorted(A_indices))
    N_A = len(A_idx)

    C_A = C_full[np.ix_(A_idx, A_idx)]
    F_A = F_full[np.ix_(A_idx, A_idx)]

    # Build generalized covariance matrix
    # For real-valued matrices (time-reversal symmetric BCS):
    # Gamma = [[C_A, F_A], [F_A, I - C_A]]
    Gamma = np.zeros((2 * N_A, 2 * N_A))
    Gamma[:N_A, :N_A] = C_A
    Gamma[:N_A, N_A:] = F_A
    Gamma[N_A:, :N_A] = F_A   # F^T = F for symmetric pairing
    Gamma[N_A:, N_A:] = np.eye(N_A) - C_A

    # Eigenvalues
    lam = np.linalg.eigvalsh(Gamma)

    # Clip to [eps, 1-eps]
    eps = 1e-30
    lam_clipped = np.clip(lam, eps, 1.0 - eps)

    # von Neumann entropy
    S = -np.sum(lam_clipped * np.log(lam_clipped) +  # (local)
                (1.0 - lam_clipped) * np.log(1.0 - lam_clipped))

    # Need to divide by 2 because we're double-counting particle-hole
    # Actually, the eigenvalues come in pairs (lambda, 1-lambda) by construction.
    # The entropy from each pair is the same. So S from 2N eigenvalues
    # double-counts. Use only eigenvalues > 0.5 (or the N_A independent ones).
    #
    # Actually, for the generalized covariance matrix, the eigenvalues
    # nu_alpha of the REDUCED matrix come from diagonalizing:
    #   C_A - F_A * (I - C_A)^{-1} * F_A^T  (Schur complement)
    # or equivalently from the single-particle entanglement spectrum.
    #
    # The correct approach: eigenvalues of Gamma come in pairs (lambda, 1-lambda).
    # S = sum over DISTINCT pairs of h(lambda) where h(x) = -x*ln(x) - (1-x)*ln(1-x).

    # Sort eigenvalues
    lam_sorted = np.sort(lam)

    # Take the N_A eigenvalues >= 0.5 (each paired with one <= 0.5)
    lam_upper = lam_sorted[N_A:]  # should be >= 0.5
    lam_lower = lam_sorted[:N_A]  # should be <= 0.5

    # Verify pairing
    pair_check = np.sort(lam_upper) + np.sort(1.0 - lam_lower[::-1])
    pair_err = np.max(np.abs(pair_check - 1.0))

    # Entropy from distinct eigenvalues
    # Only count eigenvalues strictly between 0 and 1 (0 and 1 contribute zero entropy)
    S_distinct = 0.0  # (local)
    tol = 1e-12  # (local)
    for l in lam_upper:
        if l > tol and l < 1.0 - tol:
            S_distinct += -l * np.log(l) - (1.0 - l) * np.log(1.0 - l)
        # l = 0 or l = 1 contributes 0 (pure eigenstate, no entanglement)

    return S_distinct, lam, pair_err, C_A, F_A, Gamma


# --- 5a. Normal-only entropy (max-cut partition) ---
print("\n  5a. Normal correlations only (Peschel 2003)")
S_normal, nu_normal, n_eff_normal, C_A_max = entanglement_entropy_gaussian(C_GGE, A_max)
print(f"  S_ent(normal, max-cut) = {S_normal:.6f} nats")
print(f"  Eigenvalues of C_A: {nu_normal}")
print(f"  Number of entangled modes: {n_eff_normal}")

# --- 5b. Full BCS entropy with anomalous correlations ---
print("\n  5b. Full BCS with anomalous correlations (Peschel-Eisler 2009)")
S_bcs, lam_bcs, pair_err, C_A_bcs, F_A_bcs, Gamma_A = \
    entanglement_entropy_bcs(C_GGE, F_GGE_mat, A_max)
print(f"  S_ent(BCS, max-cut) = {S_bcs:.6f} nats")
print(f"  Eigenvalue pairing error: {pair_err:.2e}")
print(f"  Generalized eigenvalues: {np.sort(lam_bcs)}")

# --- 5c. Ground state entanglement for comparison ---
print("\n  5c. Ground state comparison")
S_GS_normal, nu_GS, _, _ = entanglement_entropy_gaussian(C_GS, A_max)
S_GS_bcs, lam_GS, pair_err_GS, _, _, _ = \
    entanglement_entropy_bcs(C_GS, F_GS_mat, A_max)
print(f"  S_ent(GS, normal) = {S_GS_normal:.6f} nats")
print(f"  S_ent(GS, BCS)    = {S_GS_bcs:.6f} nats")

# --- 5d. Entropy across min-cut partition ---
print("\n  5d. Min-cut partition comparison")
S_min_normal, nu_min, n_eff_min, _ = entanglement_entropy_gaussian(C_GGE, A_min_greedy)
S_min_bcs, lam_min, _, _, _, _ = entanglement_entropy_bcs(C_GGE, F_GGE_mat, A_min_greedy)
print(f"  S_ent(normal, min-cut) = {S_min_normal:.6f} nats")
print(f"  S_ent(BCS, min-cut)    = {S_min_bcs:.6f} nats")

# =====================================================================
#  6. SWEEP OVER ALL BALANCED BIPARTITIONS (SAMPLING)
# =====================================================================
print("\n--- Section 6: Bipartition sweep (1000 random samples) ---")

np.random.seed(137)
S_samples_normal = []
S_samples_bcs = []
cut_samples = []

N_sample = 1000
for trial in range(N_sample):
    perm = np.random.permutation(N)
    A_try = set(perm[:16].tolist())

    # Normal entropy
    S_try, _, _, _ = entanglement_entropy_gaussian(C_GGE, A_try)
    S_samples_normal.append(S_try)

    # BCS entropy
    S_bcs_try, _, _, _, _, _ = entanglement_entropy_bcs(C_GGE, F_GGE_mat, A_try)
    S_samples_bcs.append(S_bcs_try if np.isfinite(S_bcs_try) else 0.0)

    # Cut size
    cut_samples.append(cut_size(A_try, adj))

S_samples_normal = np.array(S_samples_normal)
S_samples_bcs = np.array(S_samples_bcs)
cut_samples = np.array(cut_samples)

print(f"  Normal S_ent: mean = {S_samples_normal.mean():.6f}, "
      f"std = {S_samples_normal.std():.6f}, "
      f"min = {S_samples_normal.min():.6f}, max = {S_samples_normal.max():.6f}")
print(f"  BCS S_ent:    mean = {S_samples_bcs.mean():.6f}, "
      f"std = {S_samples_bcs.std():.6f}, "
      f"min = {S_samples_bcs.min():.6f}, max = {S_samples_bcs.max():.6f}")
print(f"  Cut sizes:    mean = {cut_samples.mean():.1f}, "
      f"min = {cut_samples.min()}, max = {cut_samples.max()}")

# Correlation between cut size and entropy
corr_normal = np.corrcoef(cut_samples, S_samples_normal)[0, 1]
corr_bcs = np.corrcoef(cut_samples, S_samples_bcs)[0, 1]
print(f"  Correlation(cut, S_normal) = {corr_normal:.4f}")
print(f"  Correlation(cut, S_bcs) = {corr_bcs:.4f}")

# =====================================================================
#  7. AREA LAW ANALYSIS
# =====================================================================
print("\n--- Section 7: Area law analysis ---")

# Fit S_ent vs cut_size to area law: S = s_0 * n_cut + gamma
from numpy.polynomial import polynomial as P

# Normal entropy
coeffs_normal = np.polyfit(cut_samples, S_samples_normal, 1)
s0_normal = coeffs_normal[0]
gamma_normal = coeffs_normal[1]
print(f"  Normal: S = {s0_normal:.6f} * n_cut + {gamma_normal:.6f}")
print(f"    s_0 (entropy per cut edge) = {s0_normal:.6f} nats/edge")

# BCS entropy
coeffs_bcs = np.polyfit(cut_samples, S_samples_bcs, 1)
s0_bcs = coeffs_bcs[0]
gamma_bcs = coeffs_bcs[1]
print(f"  BCS:    S = {s0_bcs:.6f} * n_cut + {gamma_bcs:.6f}")
print(f"    s_0 (entropy per cut edge) = {s0_bcs:.6f} nats/edge")

# R-squared
SS_res_normal = np.sum((S_samples_normal - np.polyval(coeffs_normal, cut_samples))**2)
SS_tot_normal = np.sum((S_samples_normal - S_samples_normal.mean())**2)
R2_normal = 1 - SS_res_normal / SS_tot_normal

SS_res_bcs = np.sum((S_samples_bcs - np.polyval(coeffs_bcs, cut_samples))**2)
SS_tot_bcs = np.sum((S_samples_bcs - S_samples_bcs.mean())**2)
R2_bcs = 1 - SS_res_bcs / SS_tot_bcs

print(f"  R^2 (normal) = {R2_normal:.6f}")
print(f"  R^2 (BCS) = {R2_bcs:.6f}")

# =====================================================================
#  8. MUTUAL INFORMATION
# =====================================================================
print("\n--- Section 8: Mutual information ---")

# For a pure global state: I(A:B) = 2 * S(A)
# For the GGE (mixed state): S(AB) > 0, so I(A:B) = S(A) + S(B) - S(AB)
#
# S(AB) = total von Neumann entropy of the GGE state
# For a product state over modes: S_total = -sum_k [n_k ln(n_k) + (1-n_k) ln(1-n_k)]

S_total_GGE = 0.0  # (local)
for k in range(N_modes):
    nk = n_k_GGE[k]
    if nk > 1e-30 and nk < 1 - 1e-30:
        S_total_GGE += -nk * np.log(nk) - (1 - nk) * np.log(1 - nk)

print(f"  S_total(GGE) = {S_total_GGE:.6f} nats")

# For balanced partition: S(A) = S(B) by symmetry arguments?
# Not exactly — the graph is not vertex-transitive.
# But we can compute S(B) separately.
B_max = set(range(N)) - A_max
S_B_normal, _, _, _ = entanglement_entropy_gaussian(C_GGE, B_max)
S_B_bcs, _, _, _, _, _ = entanglement_entropy_bcs(C_GGE, F_GGE_mat, B_max)

print(f"\n  S(A, normal) = {S_normal:.6f}")
print(f"  S(B, normal) = {S_B_normal:.6f}")
print(f"  S(AB, normal) = {S_total_GGE:.6f}")

I_AB_normal = S_normal + S_B_normal - S_total_GGE
print(f"  I(A:B, normal) = {I_AB_normal:.6f} nats")

print(f"\n  S(A, BCS) = {S_bcs:.6f}")
print(f"  S(B, BCS) = {S_B_bcs:.6f}")
I_AB_bcs = S_bcs + S_B_bcs - S_total_GGE
print(f"  I(A:B, BCS) = {I_AB_bcs:.6f} nats")

# =====================================================================
#  9. JACOBSON THERMODYNAMIC ANALYSIS
# =====================================================================
print("\n--- Section 9: Jacobson thermodynamic analysis ---")

# Jacobson 1995: Einstein equations emerge from dQ = T * dS
# where S is the LOCAL entanglement entropy across a Rindler horizon.
#
# For the GGE on the fabric, the relevant entropy density is:
#   s_ent = S_ent / A_cut
# where A_cut is the "area" of the cut in Planck units.
#
# In the framework, the cut area is n_cut * (area per bond).
# The area per bond is related to the spectral action coefficient a_2:
#   G_eff = 1 / (16 * pi * a_2)
#   Area per bond in Planck units = a_2 (roughly)

G_eff = 1.0 / (16.0 * PI * a2_fold)
A_bond = 1.0  # In graph units, each bond has unit area  # (local)

print(f"  G_eff = {G_eff:.6e} (= 1/(16*pi*a_2))")
print(f"  a_2 = {a2_fold:.4f}")

# The entanglement entropy per unit area:
s_per_bond_normal = S_normal / cut_max if cut_max > 0 else 0.0
s_per_bond_bcs = S_bcs / cut_max if cut_max > 0 else 0.0

print(f"\n  Max-cut partition ({cut_max} edges):")
print(f"    S_ent(normal) / n_cut = {s_per_bond_normal:.6f} nats/bond")
print(f"    S_ent(BCS) / n_cut = {s_per_bond_bcs:.6f} nats/bond")

# Bekenstein-Hawking: S_BH = A / (4 * G)
# In our units: S_BH_per_bond = 1 / (4 * G_eff) = 4 * pi * a_2
S_BH_per_bond = 4.0 * PI * a2_fold
print(f"\n  Bekenstein-Hawking per bond: S_BH/bond = 4*pi*a_2 = {S_BH_per_bond:.4f}")
print(f"  Ratio S_ent/S_BH per bond = {s_per_bond_normal / S_BH_per_bond:.6e}")

# If S_ent > 0 (even though small), what cosmological constant would
# Jacobson's derivation predict?
#
# Jacobson: T_Unruh * dS_ent = dE_matter
# For vacuum: Lambda_Jacobson ~ (S_ent/A) * (4*pi*G) * ...
# Actually, the CC from entanglement is:
#   rho_Lambda ~ (S_ent / V) * T_ent
# where T_ent is the entanglement temperature.
#
# A cleaner estimate: the entanglement entropy contributes to the
# effective cosmological constant as:
#   Lambda_ent = 8*pi*G * rho_ent
# where rho_ent ~ S_ent * T_ent / V_cell
# T_ent ~ 1/(2*pi * R_cut) in Planck units

# For the graph, R_cut ~ diameter/2 in graph units
R_cut = 3.0  # half the diameter (diameter = 6)  # (local)
T_ent = 1.0 / (2.0 * PI * R_cut) if S_normal > 1e-20 else 0.0

# Energy density from entanglement
V_cell = 1.0  # normalize per cell  # (local)
rho_ent = S_normal * T_ent / V_cell if S_normal > 1e-20 else 0.0

print(f"\n  Jacobson analysis (if S_ent > 0):")
print(f"    R_cut ~ {R_cut:.1f} (graph units)")
print(f"    T_ent ~ {T_ent:.6f} (graph units)")
print(f"    rho_ent ~ {rho_ent:.6e} (graph units)")

# Compare to CC gap
if rho_ent > 1e-30:
    # In M_KK^4 units
    rho_ent_MKK4 = rho_ent  # already in dimensionless graph units
    rho_ent_GeV4 = rho_ent_MKK4 * M_KK**4
    log_ratio = np.log10(rho_ent_GeV4 / rho_Lambda_obs) if rho_ent_GeV4 > 0 else 0
    print(f"    rho_ent (GeV^4) ~ {rho_ent_GeV4:.4e}")
    print(f"    rho_Lambda_obs  = {rho_Lambda_obs:.4e} GeV^4")
    print(f"    log10(rho_ent/rho_obs) ~ {log_ratio:.1f}")
    CC_reduction_from_entangle = CC_gap_OOM - log_ratio if log_ratio > 0 else 0
    print(f"    CC gap reduction: {CC_reduction_from_entangle:.1f} OOM")
else:
    print(f"    S_ent effectively zero — no Jacobson CC contribution")
    CC_reduction_from_entangle = 0.0  # (local)

# =====================================================================
#  10. STRUCTURAL ANALYSIS: WHY S_ent > 0 OR = 0
# =====================================================================
print("\n--- Section 10: Structural analysis ---")

# The GGE state is a product over modes in quasiparticle basis.
# When transformed to site basis and spatially traced, the entanglement
# depends on how much of each mode lives in A vs B.
#
# If mode k is entirely in A or entirely in B: no contribution to entanglement
# If mode k straddles the cut: contributes to entanglement
#
# Weight of mode k in region A:
A_list = sorted(A_max)
B_list = sorted(set(range(N)) - A_max)

print("  Mode weights in region A (max-cut):")
w_A = np.zeros(N_modes)
w_B = np.zeros(N_modes)
for k in range(N_modes):
    w_A[k] = np.sum(V_tb[A_list, k]**2)
    w_B[k] = np.sum(V_tb[B_list, k]**2)
    print(f"    k={k}: w_A = {w_A[k]:.6f}, w_B = {w_B[k]:.6f}, "
          f"w_A+w_B = {w_A[k]+w_B[k]:.8f}, "
          f"n_k = {n_k_GGE[k]:.6e}")

# Mode-resolved entanglement entropy contribution
# For a single mode with occupation n in a two-region system with weight w_A in A:
# The single-mode correlation matrix contribution to C_A is: n * w_A
# This mode contributes entanglement only if 0 < n*w_A < 1
print("\n  Single-mode C_A eigenvalue contributions (n_k * w_A_k):")
for k in range(N_modes):
    contrib = n_k_GGE[k] * w_A[k]
    print(f"    k={k}: n_k * w_A = {contrib:.8f}")

# For exactly 8 modes on 32 sites with a 16-site partition,
# C_A is a 16x16 matrix of rank 8 (at most).
# Its eigenvalues are at most 8 nonzero values.
print(f"\n  Rank of C_A: 8 (from 8 occupied BCS modes)")
print(f"  C_A eigenvalue spectrum:")
print(f"    {nu_normal}")

# Check if any eigenvalue is exactly 0 or 1 (no entanglement contribution)
n_entangled = 0
S_per_mode = np.zeros(16)
for i, nu_val in enumerate(nu_normal):
    if nu_val > 1e-15 and nu_val < 1.0 - 1e-15:
        S_i = -nu_val * np.log(nu_val) - (1 - nu_val) * np.log(1 - nu_val)
        S_per_mode[i] = S_i
        n_entangled += 1
        print(f"    nu_{i} = {nu_val:.8f} -> S_i = {S_i:.8f} nats")
    elif nu_val > 1e-15:
        print(f"    nu_{i} = {nu_val:.8f} -> S_i = 0 (saturated)")
    else:
        pass  # zero eigenvalue, no contribution

print(f"\n  Total entangled modes: {n_entangled}")
print(f"  Total S_ent = {np.sum(S_per_mode):.8f} nats (cross-check: {S_normal:.8f})")

# =====================================================================
#  11. GATE VERDICT
# =====================================================================
print("\n" + "=" * 72)
print("GATE VERDICT: LOCAL-ENTANGLE-63")
print("=" * 72)

# Determine verdict
if S_normal > 1e-10:
    S_ent_status = "NONZERO"
    jacobson_open = True
    verdict = "INFO"
    S_bcs_str = f"{S_bcs:.4f}" if np.isfinite(S_bcs) else "N/A"
    detail = (f"S_ent = {S_normal:.4f} nats (normal), {S_bcs_str} nats (BCS) "
              f"across max-cut partition ({cut_max} edges). "
              f"GGE has NONZERO local entanglement despite being a global product state. "
              f"Delocalized Bogoliubov modes straddle the cut. "
              f"I(A:B) = {I_AB_normal:.4f} nats. "
              f"Area-law: s_0 = {s0_normal:.4f} nats/edge (R^2 = {R2_normal:.4f}). "
              f"Jacobson path: OPEN (S_ent > 0).")
    if CC_reduction_from_entangle > 0:
        detail += f" CC reduction: {CC_reduction_from_entangle:.0f} OOM."
else:
    S_ent_status = "ZERO"
    jacobson_open = False
    verdict = "INFO"
    detail = (f"S_ent = {S_normal:.2e} nats (effectively zero). "
              f"GGE product state has no local entanglement across spatial cut. "
              f"Jacobson CC path: 9th closure confirmed.")

print(f"\n  S_ent (normal, max-cut) = {S_normal:.6f} nats")
print(f"  S_ent (BCS, max-cut)    = {S_bcs:.6f} nats")
print(f"  S_ent status: {S_ent_status}")
print(f"  Jacobson CC path: {'OPEN' if jacobson_open else 'CLOSED (9th closure)'}")
print(f"\n  Verdict: {verdict}")
print(f"  Detail: {detail}")

# =====================================================================
#  12. SAVE RESULTS
# =====================================================================
print("\n--- Section 12: Saving results ---")

out_path = os.path.join(data_dir, 's63_local_entangle.npz')

np.savez(out_path,
    # Gate
    gate_name='LOCAL-ENTANGLE-63',
    gate_verdict=verdict,
    gate_detail=detail,

    # Graph
    N_vertices=N,
    N_edges=N_edges,
    adj=adj,

    # Partition
    A_max=np.array(A_max_sorted),
    B_max=np.array(B_max_sorted),
    cut_max=cut_max,
    cut_min=best_cut_min,

    # GGE occupations
    n_k_GGE=n_k_GGE,
    F_k_GGE=F_k_GGE,

    # Entanglement entropy
    S_ent_normal_max=S_normal,
    S_ent_bcs_max=S_bcs,
    S_ent_normal_min=S_min_normal,
    S_ent_bcs_min=S_min_bcs,
    S_ent_GS_normal=S_GS_normal,
    S_ent_GS_bcs=S_GS_bcs,
    S_total_GGE=S_total_GGE,

    # Eigenvalue spectra
    nu_normal_max=nu_normal,
    nu_GS=nu_GS,
    lam_bcs_max=lam_bcs,

    # Mutual information
    I_AB_normal=I_AB_normal,
    I_AB_bcs=I_AB_bcs,

    # Area law
    s0_normal=s0_normal,
    s0_bcs=s0_bcs,
    gamma_normal=gamma_normal,
    gamma_bcs=gamma_bcs,
    R2_normal=R2_normal,
    R2_bcs=R2_bcs,

    # Mode weights
    w_A_modes=w_A,
    w_B_modes=w_B,

    # Sweep data
    S_samples_normal=S_samples_normal,
    S_samples_bcs=S_samples_bcs,
    cut_samples=cut_samples,

    # Jacobson analysis
    jacobson_open=jacobson_open,
    CC_reduction_OOM=CC_reduction_from_entangle,
    rho_ent=rho_ent,
    T_ent=T_ent,

    # BCS correlation matrices
    C_A_max=C_A_max,

    # S_ent per mode
    S_per_mode=S_per_mode,
    n_entangled_modes=n_entangled,
)

print(f"  Saved: {out_path}")

# =====================================================================
#  13. PLOT
# =====================================================================
print("\n--- Section 13: Generating plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: C_A eigenvalue spectrum
ax = axes[0, 0]
idx_sorted = np.argsort(nu_normal)[::-1]
ax.bar(range(16), nu_normal[idx_sorted], color='steelblue', alpha=0.8, label='GGE')
ax.bar(range(16), nu_GS[np.argsort(nu_GS)[::-1]], color='coral', alpha=0.4, label='GS')
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel(r'$\nu_\alpha$')
ax.set_title(r'$C_A$ eigenvalue spectrum')
ax.legend()
ax.set_xlim(-0.5, 15.5)

# Panel 2: S_ent vs cut size (area law)
ax = axes[0, 1]
ax.scatter(cut_samples, S_samples_normal, s=3, alpha=0.3, c='steelblue', label='Normal')
ax.scatter(cut_samples, S_samples_bcs, s=3, alpha=0.3, c='coral', label='BCS')
x_fit = np.linspace(cut_samples.min(), cut_samples.max(), 100)
ax.plot(x_fit, np.polyval(coeffs_normal, x_fit), 'b-', lw=2,
        label=f'Fit: {s0_normal:.4f}*n + {gamma_normal:.4f}')
ax.plot(x_fit, np.polyval(coeffs_bcs, x_fit), 'r-', lw=2,
        label=f'Fit: {s0_bcs:.4f}*n + {gamma_bcs:.4f}')
ax.set_xlabel('Cut edges')
ax.set_ylabel(r'$S_\mathrm{ent}$ (nats)')
ax.set_title('Area law: $S$ vs cut size')
ax.legend(fontsize=8)

# Panel 3: Mode weight distribution in A
ax = axes[1, 0]
x_pos = np.arange(N_modes)
width = 0.35  # (local)
ax.bar(x_pos - width/2, w_A, width, label='w(A)', color='steelblue', alpha=0.8)
ax.bar(x_pos + width/2, w_B, width, label='w(B)', color='coral', alpha=0.8)
ax.axhline(0.5, color='gray', ls='--', lw=1, label='50%')
ax.set_xlabel('BCS mode k')
ax.set_ylabel('Weight in region')
ax.set_title('Mode delocalization across cut')
ax.legend()
ax.set_xticks(x_pos)

# Panel 4: Histogram of S_ent over random partitions
ax = axes[1, 1]
ax.hist(S_samples_normal, bins=40, alpha=0.6, color='steelblue', label='Normal', density=True)
bcs_valid = S_samples_bcs[np.isfinite(S_samples_bcs)]
if len(bcs_valid) > 0:
    ax.hist(bcs_valid, bins=40, alpha=0.4, color='coral', label='BCS', density=True)
ax.axvline(S_normal, color='blue', ls='--', lw=2, label=f'Max-cut: {S_normal:.4f}')
ax.axvline(S_min_normal, color='green', ls='--', lw=2, label=f'Min-cut: {S_min_normal:.4f}')
ax.set_xlabel(r'$S_\mathrm{ent}$ (nats)')
ax.set_ylabel('Density')
ax.set_title('Distribution of $S_{ent}$ over random bipartitions')
ax.legend(fontsize=8)

fig.suptitle('LOCAL-ENTANGLE-63: GGE Local Entanglement Across Rindler Cut\n'
             f'$S_{{ent}}$ = {S_normal:.4f} nats (normal), {S_bcs:.4f} nats (BCS) | '
             f'Cut = {cut_max}/{N_edges} edges',
             fontsize=12, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])

plot_path = os.path.join(data_dir, 's63_local_entangle.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

print("\n" + "=" * 72)
print("LOCAL-ENTANGLE-63 COMPLETE")
print("=" * 72)
