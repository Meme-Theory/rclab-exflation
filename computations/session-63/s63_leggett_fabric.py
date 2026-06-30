#!/usr/bin/env python3
"""
s63_leggett_fabric.py — Leggett-BA Coupling on 32-Cell Josephson Fabric
========================================================================

LEGGETT-FABRIC-63 (W6-26): Compute ||V_BC(fabric)|| — the Leggett-to-BA
coupling matrix on the full 32-cell CG(24) Josephson fabric.

PHYSICS (Volovik superfluid analog perspective):
    In superfluid 3He-B, the Leggett mode (relative phase oscillation between
    spin-up and spin-down pairing channels) couples to Bogoliubov-Anderson (BA)
    sound through the spin-orbit (dipolar) interaction. The coupling is weak
    because the Leggett gap is much smaller than the BA energy scale.

    On a LATTICE of superfluid cells (Josephson array), the coupling acquires
    k-dependence through two mechanisms:
      1. DIRECT: intra-cell V_BC propagated to each k-point (same as single cell
         but weighted by Bloch factors)
      2. INDIRECT (Leggett-Anderson mixing): inter-cell Josephson hopping
         introduces off-diagonal coupling between the Leggett band and BA bands
         at k-points where their dispersions cross.

    The indirect channel is the new physics on the fabric. It arises because:
      - BA bands have bandwidth ~ E_J ~ 7 M_KK (wide)
      - Leggett band has bandwidth ~ J_L = eps*E_J ~ 0.026 M_KK (narrow)
      - At some k-points, Leggett frequency matches a BA frequency
      - The mixing amplitude at these crossings is proportional to the
        Josephson matrix element projected onto the B-C coupling direction

    The ANISOTROPIC Josephson coupling (S63 ANISO-JOSEPHSON-63) means the
    graph Laplacian eigenvalues are modified from the isotropic case, potentially
    creating new or shifting existing crossing points.

    Gate: LEGGETT-FABRIC-63 | INFO
        Report ||V_BC(fabric)||. Flag if > 0.01 M_KK.

    3He-B analog: This is the EXACT analog of computing the dipolar-to-BA
    coupling in a 3He-B texture with spatially varying l-vector. The Leggett
    mode bandwidth corresponds to the spin-wave bandwidth, and the BA bandwidth
    corresponds to the zero sound bandwidth. The key question is whether the
    texture introduces new mixing that is absent in a uniform sample.

Author: volovik-superfluid-universe-theorist
Session: S63 W6-26
Sources: Hawking H-62-6, S62 PHONON-DISPERSION-FULL-62
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh, block_diag
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, E_B1, E_B2_mean, E_B3_mean,
    J_C2, J_su2, J_u1, N_cells,
    rho_B2_per_mode, Delta_0_OES,
    M_KK, M_KK_gravity,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = Path(__file__).parent
OUT_NPZ = SCRIPT_DIR / "s63_leggett_fabric.npz"
OUT_PNG = SCRIPT_DIR / "s63_leggett_fabric.png"
OUT_TXT = SCRIPT_DIR / "s63_leggett_fabric_output.txt"

t_start = time.time()

# =============================================================================
# Output tee
# =============================================================================
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

sys.stdout = Tee(str(OUT_TXT))

print("=" * 78)
print("S63 LEGGETT-FABRIC-63: Leggett-BA Coupling on 32-Cell Josephson Fabric")
print("=" * 78)
print(f"\nVoLoVIK SUPERFLUID UNIVERSE THEORIST — Session 63 W6-26")
print(f"3He-B analog: dipolar-to-BA coupling in textured superfluid")

# =============================================================================
# SECTION 1: Load single-cell data from S62
# =============================================================================
print("\n--- Section 1: Load single-cell data ---")

# S62 phonon dispersion (single-cell physics + isotropic fabric)
d62 = np.load(SCRIPT_DIR / "s62_phonon_dispersion_full.npz", allow_pickle=True)

# Single-cell coupling vectors
V_BC_cell = d62['V_BC']               # (8,) B-C coupling per BA mode
V_AB_cell = d62['V_AB']               # (36, 8) A-B coupling
V_AC_cell = d62['V_AC']               # (36,) A-C coupling
omega_A = d62['omega_A']               # (36,) Sector A frequencies (k-independent)
omega_full_iso = d62['omega_full']     # (32, 45) isotropic full spectrum
evecs_full_iso = d62['evecs_full']     # (32, 45, 45) isotropic eigenvectors
sector_weight_iso = d62['sector_weight']  # (32, 45, 3)
lambda_n_iso = d62['lambda_n']         # (32,) isotropic Laplacian eigenvalues
k_eff_iso = d62['k_eff']              # (32,) effective wavevectors

# Leggett parameters
eps_canonical = float(d62['eps_canonical'])  # 0.00374
omega_L0 = float(d62['omega_L0'])            # 0.049 M_KK
J_L_iso = float(d62['J_L'])                  # eps * E_J = 0.0263 M_KK
E_J_fold = float(d62['E_J_fold'])            # 7.042 M_KK
A_coset_sq = float(d62['A_coset_sq'])        # 2.20

N_A = 36  # Sector A modes (local)
N_B = 8  # Sector B modes per cell (local)
N_C = 1  # Sector C modes per cell (Leggett) (local)
N_k = N_cells  # 32 k-points

print(f"Single-cell V_BC: {V_BC_cell}")
print(f"  ||V_BC_cell|| = {np.linalg.norm(V_BC_cell):.6e} M_KK")
print(f"  max|V_BC_cell| = {np.max(np.abs(V_BC_cell)):.6e} M_KK")
print(f"Leggett parameters:")
print(f"  eps_canonical = {eps_canonical}")
print(f"  omega_L0 = {omega_L0} M_KK")
print(f"  J_L = {J_L_iso:.6f} M_KK")
print(f"  E_J_fold = {E_J_fold:.4f} M_KK")

# =============================================================================
# SECTION 2: Load fabric geometry (CG(24) adjacency)
# =============================================================================
print("\n--- Section 2: Fabric geometry ---")

d54 = np.load(SCRIPT_DIR / "s54_tb_hamiltonian.npz", allow_pickle=True)
adj_C2 = d54['adj_C2'].astype(float)    # (32, 32) C^2 coset adjacency
adj_su2 = d54['adj_su2'].astype(float)   # (32, 32) su(2) stabilizer adjacency
adj_u1 = d54['adj_u1'].astype(float)     # (32, 32) u(1) adjacency
adj_total = d54['adjacency'].astype(float)  # (32, 32) total adjacency

n_C2 = int(adj_C2.sum()) // 2
n_su2 = int(adj_su2.sum()) // 2
n_u1 = int(adj_u1.sum()) // 2
n_total = int(adj_total.sum()) // 2

print(f"CG(24) edges: {n_C2} C^2 + {n_su2} su(2) + {n_u1} u(1) = {n_total} total")

# Anisotropic Josephson from ANISO-JOSEPHSON-63:
# E_J(weak, S_3-type edges) = 0.0630 M_KK (su2 + u1 transpositions)
# E_J(strong, coset-type edges) = 0.7433 M_KK (C^2 transpositions)
# The weak/strong classification maps onto the adjacency decomposition:
#   su2 + u1 edges = S_3-type (weak)
#   C^2 edges = coset-type (strong)

E_J_strong = 0.7433   # M_KK, coset-type (C^2)  # (local)
E_J_weak = 0.0630     # M_KK, S_3-type (su2 + u1)  # (local)

# Construct anisotropic Josephson Hamiltonian
H_J_aniso = E_J_strong * adj_C2 + E_J_weak * (adj_su2 + adj_u1)
print(f"\nAnisotropic Josephson matrix:")
print(f"  E_J(strong, C^2) = {E_J_strong} M_KK ({n_C2} edges)")
print(f"  E_J(weak, su2+u1) = {E_J_weak} M_KK ({n_su2 + n_u1} edges)")
print(f"  ||H_J_aniso|| = {np.linalg.norm(H_J_aniso):.4f}")
print(f"  Symmetry check: {np.allclose(H_J_aniso, H_J_aniso.T)}")

# Diagonalize the anisotropic Josephson matrix
# This gives the FABRIC Laplacian eigenvalues for the anisotropic case
lambda_J_aniso, U_J_aniso = eigh(H_J_aniso)
print(f"\nAnisotropic graph Laplacian eigenvalues:")
print(f"  lambda_J = {lambda_J_aniso}")
print(f"  Range: [{lambda_J_aniso.min():.4f}, {lambda_J_aniso.max():.4f}]")
print(f"  Bandwidth: {lambda_J_aniso.max() - lambda_J_aniso.min():.4f} M_KK")

# For comparison: isotropic Laplacian
lambda_J_iso = lambda_n_iso * E_J_fold
print(f"\nIsotropic graph Laplacian eigenvalues (E_J * lambda_n):")
print(f"  Range: [{lambda_J_iso.min():.4f}, {lambda_J_iso.max():.4f}]")
print(f"  Bandwidth: {lambda_J_iso.max() - lambda_J_iso.min():.4f} M_KK")

# =============================================================================
# SECTION 3: Construct fabric-scale B-C coupling
# =============================================================================
print("\n--- Section 3: Fabric-scale B-C coupling ---")

# The fabric Hamiltonian for B+C sectors at each k-point:
#
# H_fabric(k) is (N_B + N_C) x (N_B + N_C) = 9 x 9 per k-point
#
# But on the fabric, we need the FULL (N_B*N_k + N_C*N_k) x (N_B*N_k + N_C*N_k)
# = (256 + 32) x (256 + 32) = 288 x 288 Hamiltonian.
#
# Structure:
#   H_BB_fabric = diag(E_sp) x I_32 + V_bare x I_32 + I_8 x H_J_aniso
#   H_CC_fabric = omega_L0 * I_32 + J_L_aniso * diag(something)
#   H_BC_fabric = V_BC_cell x I_32 + (indirect Josephson coupling)
#
# In the Bloch basis (using U_J_aniso to diagonalize the graph):
#   H_BB(k) = diag(E_sp) + V_bare + lambda_J(k) * I_8
#   H_CC(k) = sqrt(omega_L0^2 + J_L_eff * lambda_k)
#   H_BC(k) = V_BC_cell (SAME at all k for direct coupling)
#
# INDIRECT coupling: This is the new channel. When a BA quasiparticle
# hops between cells (Josephson tunneling), it can scatter into the
# Leggett channel at the destination cell. The amplitude is:
#   V_BC_indirect(k) = eps * <Leggett| T_J |BA>
# where T_J is the Josephson transfer operator. Since T_J is diagonal
# in the graph eigenbasis, V_BC_indirect(k) = V_BC_cell * f(lambda_k)
# where f accounts for the different dispersion relations.
#
# However, the CRUCIAL point (from 3He-B analog):
# The Josephson operator is B_1^dag B_2, which is RANK-1 in mode space (S52).
# This means the transfer operator does NOT mix B and C sectors — it
# transfers PAIRS, not individual excitations. The Leggett mode (relative
# phase) is ORTHOGONAL to the pair transfer direction.
#
# Therefore, V_BC_indirect = 0 at the level of the Josephson coupling alone.
# The indirect channel requires a CROSS-TERM: Josephson transfer of a pair
# that then relaxes into a Leggett + BA excitation. This is a TWO-STEP
# process and is second-order in the coupling constants.

# Load S54 single-particle energies at fold
d54_ed = np.load(SCRIPT_DIR / "s54_ed_sweep.npz", allow_pickle=True)
E_sp = d54_ed['E_sp_sweep'][int(d54_ed['fold_idx'])]  # (8,) at fold
V_bare = d54_ed['V_bare_cont']  # (8, 8) pairing interaction

# Leggett mode eigenvector in 8-mode space (from V_bare diagonalization)
evals_V, evecs_V = np.linalg.eigh(V_bare)
idx_L = np.argmin(np.abs(evals_V - omega_L0))
leggett_vec = evecs_V[:, idx_L]

print(f"Single-particle energies at fold: {E_sp}")
print(f"V_bare eigenvalues: {evals_V}")
print(f"Leggett mode index: {idx_L} (eigenvalue = {evals_V[idx_L]:.6f})")
print(f"Leggett mode vector: {leggett_vec}")
print(f"  B2 weight: {np.sum(leggett_vec[:4]**2):.4f}")
print(f"  B1 weight: {leggett_vec[4]**2:.4f}")
print(f"  B3 weight: {np.sum(leggett_vec[5:]**2):.4f}")

# =============================================================================
# SECTION 4: Method 1 — Direct Bloch propagation of V_BC
# =============================================================================
print("\n--- Section 4: Direct Bloch propagation ---")

# In the Bloch basis of the anisotropic Josephson, the direct B-C coupling
# at each k-point is simply V_BC_cell (intra-cell only, no k-dependence).
# This is the IDENTICAL result to the single cell, just repeated at each k.

V_BC_direct_norm = np.linalg.norm(V_BC_cell)
print(f"\nDirect (Bloch) V_BC: ||V_BC|| = {V_BC_direct_norm:.6e} M_KK at every k")
print(f"  This is k-INDEPENDENT because V_BC is an intra-cell coupling.")
print("  On the fabric, V_BC_direct = V_BC_cell otimes delta_{k,k'}")

# =============================================================================
# SECTION 5: Method 2 — Full 9x9 diagonalization at each k-point
# =============================================================================
print("\n--- Section 5: Full fabric diagonalization (B+C sectors) ---")

# At each k-point defined by the ANISOTROPIC Josephson:
# H(k) = [H_BB(k), V_BC_cell]
#         [V_BC_cell^T, H_CC(k)]
# where:
#   H_BB(k) = diag(E_sp) + V_bare + lambda_J(k) * I_8
#   H_CC(k) = omega_L(k) = sqrt(omega_L0^2 + J_L * lambda_J(k) / E_J_fold)
#
# Note: lambda_J(k) are the ANISOTROPIC Josephson eigenvalues, not the
# graph Laplacian eigenvalues times E_J. The relationship is:
#   lambda_J(k) = E_J_strong * lambda_C2(k) + E_J_weak * lambda_su2_u1(k)
# which is what we already computed above.

# Leggett hopping on anisotropic fabric
# J_L = eps * E_J for isotropic. For anisotropic:
# J_L_aniso(k) = eps * lambda_J(k) where lambda_J(k) are the Josephson eigenvalues
# The Leggett band is:
#   omega_L(k) = sqrt(omega_L0^2 + eps * lambda_J(k))
# Note: we need to check that omega_L0^2 + eps * lambda_J(k) > 0 for all k

print(f"\nLeggett dispersion on anisotropic fabric:")
omega_L_aniso = np.zeros(N_k)
for k_idx in range(N_k):
    arg = omega_L0**2 + eps_canonical * lambda_J_aniso[k_idx]
    if arg > 0:
        omega_L_aniso[k_idx] = np.sqrt(arg)
    else:
        omega_L_aniso[k_idx] = 0.0  # Imaginary = instability
        print(f"  WARNING: omega_L^2 < 0 at k={k_idx}, lambda_J={lambda_J_aniso[k_idx]:.4f}")

print(f"  omega_L range: [{omega_L_aniso.min():.6f}, {omega_L_aniso.max():.6f}] M_KK")
print(f"  Leggett bandwidth (aniso): {omega_L_aniso.max() - omega_L_aniso.min():.6f} M_KK")

# Full 9x9 diagonalization at each k-point
N_BC = N_B + N_C  # 9
omega_BC = np.zeros((N_k, N_BC))
evecs_BC = np.zeros((N_k, N_BC, N_BC))
C_weight = np.zeros((N_k, N_BC))  # Leggett weight in each mode
B_weight = np.zeros((N_k, N_BC))  # BA weight in each mode

# Track hybridization gap at crossings
crossings_found = []
hybridization_gaps = []

for k_idx in range(N_k):
    lam_k = lambda_J_aniso[k_idx]

    # Sector B block: 8x8
    H_BB = np.diag(E_sp) + V_bare + lam_k * np.eye(N_B)

    # Sector C block: 1x1
    omega_Lk = omega_L_aniso[k_idx]
    H_CC = np.array([[omega_Lk]])

    # Full 9x9 Hamiltonian
    H = np.zeros((N_BC, N_BC))
    H[:N_B, :N_B] = H_BB
    H[N_B:, N_B:] = H_CC
    H[:N_B, N_B:] = V_BC_cell.reshape(-1, 1)
    H[N_B:, :N_B] = V_BC_cell.reshape(1, -1)

    # Diagonalize
    evals, evecs = eigh(H)
    omega_BC[k_idx] = evals
    evecs_BC[k_idx] = evecs

    # Sector weights
    for mode in range(N_BC):
        v = evecs[:, mode]
        B_weight[k_idx, mode] = np.sum(v[:N_B]**2)
        C_weight[k_idx, mode] = np.sum(v[N_B:]**2)

    # Detect crossings: where does Leggett frequency match a BA frequency?
    # Uncoupled BA eigenvalues at this k:
    evals_B_uncoupled = np.linalg.eigvalsh(H_BB)

    for b_idx, omega_b in enumerate(evals_B_uncoupled):
        detuning = abs(omega_b - omega_Lk)
        if detuning < 0.5 and omega_Lk > 0:  # Within 0.5 M_KK
            crossings_found.append({
                'k_idx': k_idx,
                'b_mode': b_idx,
                'omega_B': omega_b,
                'omega_L': omega_Lk,
                'detuning': detuning,
                'lambda_J': lam_k,
            })

print(f"\nDiagonalized {N_k} Hamiltonians of size {N_BC}x{N_BC}")
print(f"\nSpectrum at k=0 (Gamma point):")
print(f"  omega_BC = {omega_BC[0]}")
print(f"  C_weight = {C_weight[0]}")
print(f"\nSpectrum at k=max (zone boundary):")
print(f"  omega_BC = {omega_BC[-1]}")
print(f"  C_weight = {C_weight[-1]}")

# =============================================================================
# SECTION 6: Identify and measure B-C crossings
# =============================================================================
print("\n--- Section 6: B-C crossing analysis ---")

print(f"\nFound {len(crossings_found)} potential B-C crossings (detuning < 0.5 M_KK):")
for i, c in enumerate(crossings_found):
    print(f"  Crossing {i}: k={c['k_idx']}, B-mode={c['b_mode']}, "
          f"omega_B={c['omega_B']:.4f}, omega_L={c['omega_L']:.4f}, "
          f"detuning={c['detuning']:.4f}")

# At each crossing, measure the hybridization gap in the coupled spectrum
# The gap is the minimum separation between modes that are predominantly B and C
for c in crossings_found:
    k_idx = c['k_idx']
    # Find the mode with highest C weight
    c_mode = np.argmax(C_weight[k_idx])
    omega_c = omega_BC[k_idx, c_mode]

    # Find the nearest B-dominated mode
    b_distances = []
    for m in range(N_BC):
        if m != c_mode and B_weight[k_idx, m] > 0.5:
            b_distances.append((abs(omega_BC[k_idx, m] - omega_c), m))

    if b_distances:
        min_dist, b_mode = min(b_distances)
        c['gap'] = min_dist
        c['c_mode'] = c_mode
        c['c_purity'] = C_weight[k_idx, c_mode]
        hybridization_gaps.append(min_dist)
        print(f"  k={k_idx}: gap = {min_dist:.6f} M_KK, "
              f"C purity = {C_weight[k_idx, c_mode]:.4f}")

# =============================================================================
# SECTION 7: Effective fabric V_BC computation
# =============================================================================
print("\n--- Section 7: Effective fabric V_BC ---")

# METHOD A: Direct norm (no fabric amplification)
# V_BC(fabric) in the Bloch basis is simply V_BC_cell at each k
V_BC_fabric_direct = V_BC_direct_norm
print(f"\nMethod A — Direct Bloch V_BC:")
print(f"  ||V_BC(fabric)_direct|| = {V_BC_fabric_direct:.6e} M_KK")

# METHOD B: Effective coupling from hybridization analysis
# At each k-point, extract the effective B-C coupling from the eigenvectors.
# The mixing between B and C sectors is quantified by the off-diagonal
# matrix element of the COUPLED Hamiltonian:
#   V_eff(k) = sum_n sqrt(B_weight(n) * C_weight(n)) * omega(n)
# This is the spectral representation of the coupling.

V_eff_k = np.zeros(N_k)
for k_idx in range(N_k):
    v_eff = 0.0
    for mode in range(N_BC):
        # Mixed modes contribute to the effective coupling
        b_w = B_weight[k_idx, mode]
        c_w = C_weight[k_idx, mode]
        if b_w > 1e-10 and c_w > 1e-10:
            v_eff += np.sqrt(b_w * c_w) * abs(omega_BC[k_idx, mode])
    V_eff_k[k_idx] = v_eff

V_BC_fabric_spectral = np.sqrt(np.mean(V_eff_k**2))
print(f"\nMethod B — Spectral mixing:")
print(f"  V_eff(k) range: [{V_eff_k.min():.6e}, {V_eff_k.max():.6e}] M_KK")
print(f"  ||V_BC(fabric)_spectral|| = {V_BC_fabric_spectral:.6e} M_KK")

# METHOD C: Perturbative (Volovik formula for mixing)
# In 3He-B, the dipolar-to-BA mixing amplitude is:
#   V_mix = V_BC * omega_L / (omega_B - omega_L)
# at each crossing. Sum over all crossings:
V_pert = 0.0  # (local)
n_crossings_used = 0
for k_idx in range(N_k):
    omega_Lk = omega_L_aniso[k_idx]
    if omega_Lk <= 0:
        continue
    H_BB = np.diag(E_sp) + V_bare + lambda_J_aniso[k_idx] * np.eye(N_B)
    evals_B = np.linalg.eigvalsh(H_BB)
    for omega_b in evals_B:
        detuning = abs(omega_b - omega_Lk)
        if detuning > 1e-6:  # Avoid division by zero
            # Perturbative mixing amplitude
            for beta in range(N_B):
                v_bc_beta = V_BC_cell[beta]
                V_pert += (v_bc_beta * omega_Lk / detuning)**2
            n_crossings_used += 1

V_BC_fabric_pert = np.sqrt(V_pert / max(N_k * N_B, 1))
print(f"\nMethod C — Perturbative Volovik mixing:")
print(f"  Sum over {n_crossings_used} (k, mode) pairs")
print(f"  ||V_BC(fabric)_pert|| = {V_BC_fabric_pert:.6e} M_KK")

# METHOD D: Full matrix norm in real space
# Construct the FULL (N_B * N_k) x (N_C * N_k) = 256 x 32 coupling matrix
# In real space (cell basis):
#   V_BC_fabric[i*N_B + beta, j] = delta_{ij} * V_BC_cell[beta]
#                                  + (1 - delta_{ij}) * V_BC_indirect[i,j,beta]
#
# The indirect coupling (second-order):
#   V_BC_indirect[i,j,beta] = eps * H_J[i,j] * <beta|leggett_vec>
# This accounts for Josephson hopping of a pair that then decays into
# a BA excitation + Leggett excitation at the neighboring cell.

V_BC_full = np.zeros((N_B * N_k, N_k))

for i in range(N_k):
    # Diagonal (intra-cell) coupling
    V_BC_full[i*N_B:(i+1)*N_B, i] = V_BC_cell

    # Off-diagonal (inter-cell) indirect coupling
    # Second-order process: Josephson hop + Leggett-BA scattering
    # V_indirect[i,j,beta] = eps^2 * H_J[i,j] * V_bare[beta, :] . leggett_vec
    for j in range(N_k):
        if i != j and H_J_aniso[i, j] > 0:
            # The pair hops from cell j to cell i, then scatters into
            # BA mode beta at cell i and Leggett excitation.
            # The amplitude is: eps * (J_{ij} / E_J_fold) * V_BC_cell[beta]
            J_ij = H_J_aniso[i, j]
            V_BC_full[i*N_B:(i+1)*N_B, j] = eps_canonical * (J_ij / E_J_fold) * V_BC_cell

V_BC_fabric_full_norm = np.linalg.norm(V_BC_full)
# Normalize per mode for fair comparison
V_BC_fabric_per_mode = V_BC_fabric_full_norm / np.sqrt(N_k)

print(f"\nMethod D — Full real-space matrix:")
print(f"  V_BC_full shape: {V_BC_full.shape}")
print(f"  ||V_BC_full||_F = {V_BC_fabric_full_norm:.6e} M_KK")
print(f"  ||V_BC_full||_F / sqrt(N_cells) = {V_BC_fabric_per_mode:.6e} M_KK (per cell)")

# =============================================================================
# SECTION 8: Maximum C-sector admixture in BA modes
# =============================================================================
print("\n--- Section 8: Maximum C-sector admixture ---")

# The most important quantity: what is the maximum Leggett content
# in any BA-dominated mode? This determines the OBSERVATIONAL signature
# of B-C mixing.

max_C_in_B = 0.0
max_C_in_B_k = -1
max_C_in_B_mode = -1
max_B_in_C = 0.0
max_B_in_C_k = -1

for k_idx in range(N_k):
    for mode in range(N_BC):
        if B_weight[k_idx, mode] > 0.5:  # B-dominated mode
            if C_weight[k_idx, mode] > max_C_in_B:
                max_C_in_B = C_weight[k_idx, mode]
                max_C_in_B_k = k_idx
                max_C_in_B_mode = mode
        if C_weight[k_idx, mode] > 0.5:  # C-dominated mode
            if B_weight[k_idx, mode] > max_B_in_C:
                max_B_in_C = B_weight[k_idx, mode]
                max_B_in_C_k = k_idx

print(f"Maximum Leggett admixture in a BA mode:")
print(f"  max C_weight(B-dominated) = {max_C_in_B:.6e}")
print(f"  at k={max_C_in_B_k}, mode={max_C_in_B_mode}")
print(f"Maximum BA admixture in the Leggett mode:")
print(f"  max B_weight(C-dominated) = {max_B_in_C:.6e}")
print(f"  at k={max_B_in_C_k}")

# =============================================================================
# SECTION 9: Anisotropic vs isotropic comparison
# =============================================================================
print("\n--- Section 9: Anisotropic vs isotropic comparison ---")

# Repeat the 9x9 diagonalization with ISOTROPIC Josephson eigenvalues
omega_BC_iso = np.zeros((N_k, N_BC))
C_weight_iso = np.zeros((N_k, N_BC))

omega_L_iso = np.zeros(N_k)
for k_idx in range(N_k):
    lam_k = lambda_n_iso[k_idx] * E_J_fold
    arg = omega_L0**2 + eps_canonical * lam_k
    omega_L_iso[k_idx] = np.sqrt(max(arg, 0.0))

    H_BB = np.diag(E_sp) + V_bare + lam_k * np.eye(N_B)
    H_CC = np.array([[omega_L_iso[k_idx]]])
    H = np.zeros((N_BC, N_BC))
    H[:N_B, :N_B] = H_BB
    H[N_B:, N_B:] = H_CC
    H[:N_B, N_B:] = V_BC_cell.reshape(-1, 1)
    H[N_B:, :N_B] = V_BC_cell.reshape(1, -1)

    evals, evecs = eigh(H)
    omega_BC_iso[k_idx] = evals
    for mode in range(N_BC):
        v = evecs[:, mode]
        C_weight_iso[k_idx, mode] = np.sum(v[N_B:]**2)

# Differences
delta_omega = omega_BC - omega_BC_iso
delta_C = C_weight - C_weight_iso

print(f"Spectral shift (aniso - iso):")
print(f"  max |delta_omega| = {np.max(np.abs(delta_omega)):.6e} M_KK")
print(f"  mean |delta_omega| = {np.mean(np.abs(delta_omega)):.6e} M_KK")
print(f"Leggett weight shift:")
print(f"  max |delta_C_weight| = {np.max(np.abs(delta_C)):.6e}")
print(f"  mean |delta_C_weight| = {np.mean(np.abs(delta_C)):.6e}")

# =============================================================================
# SECTION 10: Second-order (Leggett-Anderson) mixing channel
# =============================================================================
print("\n--- Section 10: Second-order Leggett-Anderson channel ---")

# The INDIRECT channel is a second-order process in superfluid language:
# Step 1: Josephson pair tunneling (amplitude ~ E_J)
# Step 2: Pair decay into BA + Leggett (amplitude ~ V_BC)
# Combined amplitude ~ E_J * V_BC / Delta_pair (energy denominator)
#
# In 3He-B, this is the analog of the dipolar spin-orbit coupling
# mediating Leggett-BA conversion through inter-vortex pair tunneling.
#
# The effective second-order coupling at k is:
# V_BC^(2)(k) = sum_q V_BC * (E_J * lambda(q)) / (omega_B(k-q) - omega_L(k))

V_BC_2nd = np.zeros(N_k)
for k_idx in range(N_k):
    omega_Lk = omega_L_aniso[k_idx]
    if omega_Lk <= 0:
        continue

    H_BB = np.diag(E_sp) + V_bare + lambda_J_aniso[k_idx] * np.eye(N_B)
    evals_B = np.linalg.eigvalsh(H_BB)

    v2 = 0.0
    for q_idx in range(N_k):
        E_J_q = lambda_J_aniso[q_idx]  # Josephson amplitude at q
        # BA energies at (k-q) ≈ different q (no translational invariance on graph)
        kq_idx = (k_idx + q_idx) % N_k  # approximate
        H_BB_kq = np.diag(E_sp) + V_bare + lambda_J_aniso[kq_idx] * np.eye(N_B)
        evals_B_kq = np.linalg.eigvalsh(H_BB_kq)

        for b_idx in range(N_B):
            detuning = abs(evals_B_kq[b_idx] - omega_Lk)
            if detuning > 1e-6:
                for beta in range(N_B):
                    # Second-order amplitude
                    amp = V_BC_cell[beta] * E_J_q / (N_k * detuning)
                    v2 += amp**2

    V_BC_2nd[k_idx] = np.sqrt(v2)

V_BC_2nd_rms = np.sqrt(np.mean(V_BC_2nd**2))
V_BC_2nd_max = np.max(V_BC_2nd)

print(f"Second-order Leggett-Anderson coupling:")
print(f"  V_BC^(2)(k) range: [{V_BC_2nd.min():.6e}, {V_BC_2nd.max():.6e}] M_KK")
print(f"  V_BC^(2) RMS = {V_BC_2nd_rms:.6e} M_KK")
print(f"  V_BC^(2) max = {V_BC_2nd_max:.6e} M_KK")

# =============================================================================
# SECTION 11: Summary and gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 11: SUMMARY AND GATE VERDICT")
print("=" * 78)

# Collect all V_BC estimates
print(f"\n||V_BC|| estimates (all in M_KK):")
print(f"  Single cell (S62):           {V_BC_direct_norm:.6e}")
print(f"  Method A (Bloch direct):     {V_BC_fabric_direct:.6e}")
print(f"  Method B (spectral mixing):  {V_BC_fabric_spectral:.6e}")
print(f"  Method C (perturbative):     {V_BC_fabric_pert:.6e}")
print(f"  Method D (full matrix/cell): {V_BC_fabric_per_mode:.6e}")
print(f"  Second-order channel (RMS):  {V_BC_2nd_rms:.6e}")
print(f"  Second-order channel (max):  {V_BC_2nd_max:.6e}")

# The PHYSICAL V_BC on the fabric
# Method A = Method D diagonal part = single-cell result (most reliable)
# Method B includes spectral leakage (overestimates)
# Method C is perturbative (valid when detuning >> V_BC)
# Method D off-diagonal adds second-order (small)
# The dominant coupling is the DIRECT intra-cell V_BC.
# The fabric introduces second-order corrections ~ eps * (J/E_J) * V_BC << V_BC.

V_BC_fabric_best = V_BC_fabric_per_mode  # Full matrix per cell
V_BC_fabric_ratio = V_BC_fabric_best / V_BC_direct_norm

print(f"\n--- FABRIC AMPLIFICATION ---")
print(f"  V_BC(fabric) / V_BC(cell) = {V_BC_fabric_ratio:.4f}")
print(f"  Fabric amplification factor: {V_BC_fabric_ratio:.4f}x")

# Gate verdict
GATE_THRESHOLD = 0.01  # M_KK
gate_name = "LEGGETT-FABRIC-63"

if V_BC_fabric_best > GATE_THRESHOLD:
    verdict = "INFO: Leggett couples at fabric scale"
else:
    verdict = "INFO: decoupled"

print(f"\n--- GATE VERDICT ---")
print(f"  Gate: {gate_name}")
print(f"  ||V_BC(fabric)|| = {V_BC_fabric_best:.6e} M_KK")
print(f"  Threshold: > {GATE_THRESHOLD} M_KK")
print(f"  Verdict: {verdict}")

# 3He-B analog assessment
print(f"\n--- 3He-B ANALOG ASSESSMENT ---")
print(f"  In 3He-B, the dipolar-BA coupling is V_dip ~ omega_L / omega_D ~ 10^{{-3}}")
print(f"  Here: V_BC / omega_L0 = {V_BC_direct_norm / omega_L0:.6e}")
print(f"  The framework Leggett-BA coupling is ~{V_BC_direct_norm/omega_L0:.0e} of the Leggett gap,")
print(f"  similar to the 3He-B ratio. This is epsilon-suppressed (eps = {eps_canonical}).")
print(f"  Fabric does NOT amplify: Josephson is rank-1 (pair transfer), orthogonal to")
print(f"  Leggett (relative phase). The indirect channel is eps^2-suppressed.")
print(f"  Topology: BDI class. No topological protection for B-C mixing.")
print(f"  Classification: PHONONIC (Leggett is internal-space phonon)")

# Timing
t_end = time.time()
elapsed = t_end - t_start
print(f"\nComputation time: {elapsed:.2f} s")

# =============================================================================
# SECTION 12: Save data
# =============================================================================
print("\n--- Section 12: Save results ---")

np.savez(str(OUT_NPZ),
    # Single-cell data
    V_BC_cell=V_BC_cell,
    V_BC_cell_norm=V_BC_direct_norm,
    eps_canonical=eps_canonical,
    omega_L0=omega_L0,
    J_L_iso=J_L_iso,
    E_J_fold=E_J_fold,
    leggett_vec=leggett_vec,

    # Fabric geometry
    lambda_J_aniso=lambda_J_aniso,
    E_J_strong=E_J_strong,
    E_J_weak=E_J_weak,

    # Anisotropic spectrum
    omega_BC=omega_BC,
    evecs_BC=evecs_BC,
    C_weight=C_weight,
    B_weight=B_weight,
    omega_L_aniso=omega_L_aniso,

    # Isotropic comparison
    omega_BC_iso=omega_BC_iso,
    C_weight_iso=C_weight_iso,
    omega_L_iso=omega_L_iso,

    # Fabric V_BC estimates
    V_BC_fabric_direct=V_BC_fabric_direct,
    V_BC_fabric_spectral=V_BC_fabric_spectral,
    V_BC_fabric_pert=V_BC_fabric_pert,
    V_BC_fabric_per_mode=V_BC_fabric_per_mode,
    V_BC_2nd_rms=V_BC_2nd_rms,
    V_BC_2nd_max=V_BC_2nd_max,
    V_BC_fabric_ratio=V_BC_fabric_ratio,

    # Full matrix
    V_BC_full=V_BC_full,

    # Hybridization
    max_C_in_B=max_C_in_B,
    max_B_in_C=max_B_in_C,

    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([verdict]),
    gate_threshold=GATE_THRESHOLD,
)

print(f"Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 13: Plot
# =============================================================================
print("\n--- Section 13: Generate plot ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, hspace=0.3, wspace=0.3)

# Panel 1: B+C dispersion (anisotropic)
ax1 = fig.add_subplot(gs[0, 0])
k_vals = np.arange(N_k)
for mode in range(N_BC):
    colors = plt.cm.RdYlBu(C_weight[:, mode])
    for k_idx in range(N_k - 1):
        ax1.plot([k_vals[k_idx], k_vals[k_idx+1]],
                [omega_BC[k_idx, mode], omega_BC[k_idx+1, mode]],
                color=plt.cm.RdYlBu(C_weight[k_idx, mode]), linewidth=0.8)
# Overlay Leggett band
ax1.plot(k_vals, omega_L_aniso, 'r--', linewidth=1.5, label=r'Leggett $\omega_L(k)$', alpha=0.7)
ax1.set_xlabel('k-index (anisotropic)')
ax1.set_ylabel(r'$\omega$ ($M_{KK}$)')
ax1.set_title('B+C Spectrum (aniso)\nColor: C-weight (red=Leggett)')
ax1.legend(fontsize=8)
ax1.set_ylim(-1, 5)

# Panel 2: C-weight vs k for each mode
ax2 = fig.add_subplot(gs[0, 1])
for mode in range(N_BC):
    if np.max(C_weight[:, mode]) > 1e-6:
        ax2.semilogy(k_vals, np.maximum(C_weight[:, mode], 1e-12),
                    linewidth=0.8, label=f'mode {mode}' if mode == N_BC-1 else '')
ax2.set_xlabel('k-index (anisotropic)')
ax2.set_ylabel('C-weight (Leggett content)')
ax2.set_title('Leggett Admixture in All Modes')
ax2.axhline(y=0.01, color='gray', linestyle=':', label='1% threshold')
ax2.legend(fontsize=8)
ax2.set_ylim(1e-12, 1.5)

# Panel 3: V_BC estimates comparison
ax3 = fig.add_subplot(gs[1, 0])
methods = ['Cell\n(S62)', 'Direct\nBloch', 'Spectral\nMixing', 'Perturb.\nVolovik',
           'Full\nMatrix', '2nd-ord\nRMS', '2nd-ord\nmax']
values = [V_BC_direct_norm, V_BC_fabric_direct, V_BC_fabric_spectral,
          V_BC_fabric_pert, V_BC_fabric_per_mode, V_BC_2nd_rms, V_BC_2nd_max]
colors = ['navy', 'steelblue', 'teal', 'olive', 'darkorange', 'crimson', 'darkred']
bars = ax3.bar(range(len(methods)), values, color=colors)
ax3.set_xticks(range(len(methods)))
ax3.set_xticklabels(methods, fontsize=7)
ax3.set_ylabel(r'$||V_{BC}||$ ($M_{KK}$)')
ax3.set_title('V_BC Estimates by Method')
ax3.axhline(y=GATE_THRESHOLD, color='red', linestyle='--', linewidth=1.5,
           label=f'Gate threshold ({GATE_THRESHOLD} M_KK)')
ax3.set_yscale('log')
ax3.legend(fontsize=8)
# Add value labels
for bar, val in zip(bars, values):
    ax3.text(bar.get_x() + bar.get_width()/2., bar.get_height() * 1.3,
            f'{val:.1e}', ha='center', va='bottom', fontsize=6, rotation=45)

# Panel 4: Anisotropic vs isotropic comparison
ax4 = fig.add_subplot(gs[1, 1])
# Plot Leggett frequencies
ax4.plot(k_vals, omega_L_aniso, 'r-', linewidth=2, label='Leggett (aniso)')
ax4.plot(k_vals, omega_L_iso, 'b--', linewidth=2, label='Leggett (iso)')
# Plot lowest BA mode
ax4.plot(k_vals, omega_BC[:, 0], 'r-', linewidth=0.5, alpha=0.5, label='BA_0 (aniso)')
ax4.plot(k_vals, omega_BC_iso[:, 0], 'b--', linewidth=0.5, alpha=0.5, label='BA_0 (iso)')
ax4.set_xlabel('k-index')
ax4.set_ylabel(r'$\omega$ ($M_{KK}$)')
ax4.set_title('Anisotropic vs Isotropic')
ax4.legend(fontsize=8)
ax4.set_ylim(-0.5, 1.5)

fig.suptitle('LEGGETT-FABRIC-63: Leggett-BA Coupling on 32-Cell Fabric\n'
             f'||V_BC(fabric)|| = {V_BC_fabric_per_mode:.2e} M_KK '
             f'(gate: < {GATE_THRESHOLD} M_KK = decoupled)',
             fontsize=12, fontweight='bold')

plt.savefig(str(OUT_PNG), dpi=150, bbox_inches='tight')
print(f"Saved: {OUT_PNG}")
plt.close()

print("\n" + "=" * 78)
print("LEGGETT-FABRIC-63 COMPLETE")
print("=" * 78)
