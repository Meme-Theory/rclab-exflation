#!/usr/bin/env python3
"""
S52 QM-DISPERSION-52: Quantum Metric K^4 Correction to Goldstone Dispersion
============================================================================

PHYSICS:
  The BCS condensate on the 32-cell Voronoi tessellation has 3 sectors
  (B1, B2, B3). Each cell hosts a 3-component order parameter:
      (Delta_1 e^{i phi_1}, Delta_2 e^{i phi_2}, Delta_3 e^{i phi_3})

  The phase dynamics are governed by:
    - INTER-CELL hopping: each sector's phase phi_{i,alpha} couples to
      neighbors via directional Josephson stiffness (J_C2, J_su2, J_u1)
    - INTER-SECTOR Leggett coupling: within each cell, V_{alpha,beta}
      couples the relative phases phi_alpha - phi_beta

  The Bloch Hamiltonian at crystal momentum K is a 3x3 matrix:
      H_{alpha,beta}(K) = [lambda_alpha(K) + sum_{gamma} J^L_{alpha,gamma}]
                          * delta_{alpha,beta} - J^L_{alpha,beta}
  where:
      lambda_alpha(K) = sector-alpha lattice dispersion
      J^L_{alpha,beta} = V_{alpha,beta} |Delta_alpha| |Delta_beta|  (Leggett)

  The 3 eigenvalues give: 1 Goldstone (acoustic, omega -> 0 as K -> 0)
                           2 Leggett modes (gapped)

  QUANTUM METRIC:
  The quantum geometric tensor of the Goldstone Bloch state is:
      Q_{ij}(K) = <d_i u_K | d_j u_K> - <d_i u_K | u_K><u_K | d_j u_K>
  where |u_K> is the Goldstone eigenvector of H(K), and d_i = d/dK_i.

  The quantum metric g_{ij}(K) = Re Q_{ij}(K) measures how fast the
  Goldstone eigenvector rotates in the 3-component space as K varies.
  The Berry curvature F_{ij}(K) = -2 Im Q_{ij}(K) measures the phase twist.

  For a time-reversal symmetric system (H(K) = H(-K)*, real), Berry curvature
  vanishes but quantum metric can be nonzero.

  The K^4 correction to the Goldstone dispersion:
      omega(K) = c_eff * |K| * sqrt(1 + alpha_QM * K^2 + ...)
  where alpha_QM comes from the band curvature (deviation from linearity)
  induced by hybridization with Leggett modes.

  alpha_QM is controlled by:
  - The sector stiffness anisotropy (rho_B1 vs rho_B2 vs rho_B3)
  - The Leggett gap (mass of the relative-phase modes)
  - The lattice dispersion (cosine vs linear)

  Geometric interpretation (Berry Paper 01, eq BP-4):
      g_{ij}(K) = sum_{n != 0} Re[<0|d_i H|n><n|d_j H|0>] / (E_n - E_0)^2
  The quantum metric is concentrated where the Goldstone-Leggett gap is small.

GATE: QM-DISPERSION-52
  PASS: K^4 correction modifies effective power-law index by > 0.01 at K_pivot
  FAIL: K^4 correction < 0.001 at K_pivot

Author: berry-geometric-phase-theorist (Session 52, Wave 1-G)
Date: 2026-03-20
"""

import os
import sys
import time
import numpy as np
from scipy.linalg import eigh

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t0 = time.time()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import *  # noqa: F401,F403 (canonical star-import, S81 T3 compliance)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

print("=" * 78)
print("QM-DISPERSION-52: Quantum Metric K^4 Correction to Goldstone Dispersion")
print("=" * 78)

# ===========================================================================
# STEP 1: Load upstream data and define parameters
# ===========================================================================
print("\n--- Step 1: Parameters ---")

# Lattice geometry: 4x4x2 with PBC
nx, ny, nz = 4, 4, 2      # (local) Voronoi 4x4x2 tiling (4*4*2=32=N_cells)
N = nx * ny * nz          # (local) total cell count for assertion
assert N == N_cells, f"Lattice cells {N} != N_cells {N_cells}"

# Sector DOS (proportional to mode count * per-mode DOS)
# From S35/S48: n_B1=1, n_B2=4, n_B3=3 modes
# DOS-weighted stiffness: rho_alpha = n_alpha * rho_per_mode
# We use the rho values from the Leggett mode computation (S48)
# Load if available, otherwise use canonical
try:
    d35 = np.load(os.path.join(SCRIPT_DIR, 's35_thouless_multiband.npz'), allow_pickle=True)
    rho_B1 = float(d35['rho_B1'])
    rho_B2 = float(d35['rho_B2'])
    rho_B3 = float(d35['rho_B3'])
    print(f"  Loaded DOS from s35_thouless_multiband.npz")
except FileNotFoundError:
    # Fallback: use mode counting * per-mode DOS
    rho_B1 = 1 * rho_B2_per_mode * 0.5   # (local) B1 has ~half the DOS per mode
    rho_B2 = 4 * rho_B2_per_mode          # (local) B2 dominant (S35 mode count)
    rho_B3 = 3 * rho_B2_per_mode * 0.7    # (local) B3 reduced (S35 mode count)
    print(f"  Using estimated DOS (fallback)")

print(f"  rho_B1 = {rho_B1:.6f}")
print(f"  rho_B2 = {rho_B2:.6f}")
print(f"  rho_B3 = {rho_B3:.6f}")

# Inter-sector Josephson coupling (Leggett mass matrix)
# From S48 Leggett mode: J^L_{alpha,beta} = V_{alpha,beta} |Delta_alpha||Delta_beta|
# Load V matrix from S35 or use the Leggett mode data
try:
    d48 = np.load(os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz'), allow_pickle=True)
    # Try to extract Josephson couplings
    if 'J_12' in d48:
        J_12 = float(d48['J_12'])
        J_13 = float(d48['J_13'])
        J_23 = float(d48['J_23'])
    elif 'J_matrix' in d48:
        J_mat = d48['J_matrix']
        J_12 = J_mat[0, 1]
        J_13 = J_mat[0, 2]
        J_23 = J_mat[1, 2]
    else:
        raise KeyError("J values not found in s48 data")
    print(f"  Loaded Josephson couplings from s48_leggett_mode.npz")
except (FileNotFoundError, KeyError) as e:
    print(f"  s48 data issue: {e}")
    # Construct from V matrix (S35) and BCS gaps
    try:
        V_branch = d35['V_branch_3x3']
        V_sym = 0.5 * (V_branch + V_branch.T)
        Delta_vec = np.array([Delta_0_GL * 0.3, Delta_0_GL, Delta_B3])  # approximate
        J_12 = abs(V_sym[0, 1]) * Delta_vec[0] * Delta_vec[1]
        J_13 = abs(V_sym[0, 2]) * Delta_vec[0] * Delta_vec[2]
        J_23 = abs(V_sym[1, 2]) * Delta_vec[1] * Delta_vec[2]
        print(f"  Constructed J from V_branch_3x3 and BCS gaps")
    except (NameError, KeyError):
        # Use Leggett mode frequencies to back-extract Josephson couplings
        # From S48: omega_L1 ~ 0.28, omega_L2 ~ 0.40 M_KK
        # omega_L^2 = J_eff / rho_eff
        # Use approximate values from Leggett mode analysis
        J_12 = 0.10   # B1-B2 coupling  # (local)
        J_13 = 0.02   # B1-B3 coupling  # (local)
        J_23 = 0.15   # B2-B3 coupling (dominant, V(B2,B3) ~ Feshbach)  # (local)
        print(f"  Using approximate Josephson couplings")

print(f"  J_12 (B1-B2 Leggett) = {J_12:.6f}")
print(f"  J_13 (B1-B3 Leggett) = {J_13:.6f}")
print(f"  J_23 (B2-B3 Leggett) = {J_23:.6f}")

# Inter-cell hopping: directional
# J_C2 = 0.933 (x,y), J_su2 = 0.059 (z)
J_xy = J_C2    # In-plane Josephson (C^2 coset)
J_z = J_su2    # Inter-plane Josephson (su(2) stabilizer)
print(f"\n  Inter-cell Josephson:")
print(f"    J_xy (C^2)  = {J_xy:.6f} M_KK")
print(f"    J_z  (su2)  = {J_z:.6f} M_KK")
print(f"    Anisotropy  = {J_xy / J_z:.1f}x")

# ===========================================================================
# STEP 2: Build Bloch Hamiltonian H(K) and diagonalize across BZ
# ===========================================================================
print("\n--- Step 2: Bloch Hamiltonian ---")

def lattice_dispersion(kx, ky, kz, J_xy_val, J_z_val):
    """
    Lattice eigenvalue for mode K = (kx, ky, kz):
        lambda(K) = 2*J_xy*(2 - cos(kx) - cos(ky)) + 2*J_z*(1 - cos(kz))
    """
    return (2 * J_xy_val * (2.0 - np.cos(kx) - np.cos(ky))
            + 2 * J_z_val * (1.0 - np.cos(kz)))


def build_H_K(kx, ky, kz, rho_vec, J_Leggett, J_xy_val, J_z_val):
    """
    Build the 3x3 Bloch Hamiltonian at momentum K = (kx, ky, kz).

    The dynamical equation for sector phases is:
        rho_alpha * omega^2 * phi_alpha = lambda_alpha(K) * phi_alpha
                                          + sum_beta M^L_{alpha,beta} phi_beta
    where M^L is the Leggett mass matrix.

    Rewrite as a standard eigenvalue problem by dividing by rho:
        omega^2 * phi = [diag(lambda/rho) + diag(1/rho) M^L] phi

    BUT different sectors may have different phase stiffnesses (different
    effective J for hopping). In the simplest model, all sectors share the
    same lattice hopping (the BCS condensate couples to the same geometry):

        H(K) = diag(lambda(K)/rho_alpha) + diag(1/rho_alpha) @ M_Leggett

    This is a real symmetric matrix (since M_Leggett is symmetric and
    all diagonal elements are real).

    Parameters:
        kx, ky, kz: momentum components
        rho_vec: (3,) sector DOS [rho_B1, rho_B2, rho_B3]
        J_Leggett: (3,3) inter-sector Josephson coupling matrix
        J_xy_val: in-plane hopping J
        J_z_val: inter-plane hopping J

    Returns:
        H: (3,3) real symmetric Bloch Hamiltonian (eigenvalues = omega^2)
    """
    lam_K = lattice_dispersion(kx, ky, kz, J_xy_val, J_z_val)

    # Leggett mass matrix (graph Laplacian structure)
    n = len(rho_vec)
    M_L = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                M_L[i, j] = -J_Leggett[i, j]
                M_L[i, i] += J_Leggett[i, j]

    # Full dynamical matrix: H(K) = diag(1/rho) @ [lambda(K)*I + M_L]
    inv_rho = np.diag(1.0 / rho_vec)
    H = inv_rho @ (lam_K * np.eye(n) + M_L)

    # Symmetrize (should be symmetric by construction for uniform lattice)
    # Actually, diag(1/rho) @ M is NOT symmetric unless rho_i are all equal.
    # The correct symmetric form uses the generalized eigenvalue:
    #     M_L phi = omega^2 diag(rho) phi
    # or equivalently, transform: H_sym = diag(rho)^{-1/2} (lambda*I + M_L) diag(rho)^{-1/2}
    # This IS symmetric and has the same eigenvalues.
    sqrt_inv_rho = np.diag(1.0 / np.sqrt(rho_vec))
    H_sym = sqrt_inv_rho @ (lam_K * np.eye(n) + M_L) @ sqrt_inv_rho

    return H_sym


def eigensystem_at_K(kx, ky, kz, rho_vec, J_Leggett, J_xy_val, J_z_val):
    """
    Diagonalize H(K) and return sorted eigenvalues and eigenvectors.

    Returns:
        evals: (3,) sorted eigenvalues (omega^2), ascending
        evecs: (3,3) columns are eigenvectors in sqrt(rho)-weighted basis
        evecs_phys: (3,3) columns are physical eigenvectors (phi basis)
    """
    H = build_H_K(kx, ky, kz, rho_vec, J_Leggett, J_xy_val, J_z_val)
    evals, evecs = eigh(H)  # eigh gives sorted ascending, real eigenvalues

    # Transform back to physical (phi) basis:
    # if psi = diag(rho)^{1/2} phi, then phi = diag(rho)^{-1/2} psi
    sqrt_inv_rho = np.diag(1.0 / np.sqrt(rho_vec))
    evecs_phys = sqrt_inv_rho @ evecs

    # Normalize physical eigenvectors
    for i in range(evecs_phys.shape[1]):
        evecs_phys[:, i] /= np.linalg.norm(evecs_phys[:, i])

    return evals, evecs, evecs_phys


# Build Josephson coupling matrix
J_Leggett = np.array([
    [0.0,  J_12, J_13],
    [J_12, 0.0,  J_23],
    [J_13, J_23, 0.0 ]
])

rho_vec = np.array([rho_B1, rho_B2, rho_B3])

# Verify at K=0: should have one zero eigenvalue (Goldstone)
evals_0, evecs_0, evecs_phys_0 = eigensystem_at_K(0, 0, 0, rho_vec, J_Leggett, J_xy, J_z)
print(f"  K=0 eigenvalues (omega^2): {evals_0}")
print(f"  Goldstone eigenvalue: {evals_0[0]:.4e} (should be ~0)")
print(f"  Leggett gap 1: omega_L1 = {np.sqrt(max(0, evals_0[1])):.6f} M_KK")
print(f"  Leggett gap 2: omega_L2 = {np.sqrt(max(0, evals_0[2])):.6f} M_KK")

# K=0 Goldstone eigenvector should be proportional to (sqrt(rho_1), sqrt(rho_2), sqrt(rho_3))
gold_0 = evecs_0[:, 0]
gold_expected = np.sqrt(rho_vec) / np.linalg.norm(np.sqrt(rho_vec))
print(f"\n  K=0 Goldstone eigvec (sqrt-rho basis): {gold_0}")
print(f"  Expected (uniform phase):               {gold_expected}")
print(f"  Overlap: {abs(np.dot(gold_0, gold_expected)):.10f}")

# ===========================================================================
# STEP 3: Dispersion relation omega(K) along high-symmetry directions
# ===========================================================================
print("\n--- Step 3: Dispersion along high-symmetry lines ---")

# High-symmetry points on 4x4x2 lattice
# Gamma = (0,0,0), X = (pi,0,0), M = (pi,pi,0), Z = (0,0,pi)
# R = (pi,pi,pi), A = (pi,0,pi)

Nk = 200  # (local) K-points per BZ segment

def dispersion_along_path(k_path, rho_vec, J_Leggett, J_xy_val, J_z_val):
    """Compute omega(K) along a path in the BZ."""
    n_pts = len(k_path)
    n_bands = len(rho_vec)
    omega_sq = np.zeros((n_pts, n_bands))
    evecs_all = np.zeros((n_pts, n_bands, n_bands))

    for i, (kx, ky, kz) in enumerate(k_path):
        evals, evecs, _ = eigensystem_at_K(kx, ky, kz, rho_vec, J_Leggett, J_xy_val, J_z_val)
        omega_sq[i] = evals
        evecs_all[i] = evecs

    omega = np.sqrt(np.maximum(omega_sq, 0))
    return omega_sq, omega, evecs_all


# Path: Gamma -> X -> M -> Gamma -> Z -> R
def make_path(p1, p2, N_pts):
    """Linear interpolation between two k-points."""
    return [p1 + t * (p2 - p1) for t in np.linspace(0, 1, N_pts, endpoint=False)]

G = np.array([0, 0, 0], dtype=float)
X = np.array([PI, 0, 0])
M = np.array([PI, PI, 0])
Z = np.array([0, 0, PI])
R = np.array([PI, PI, PI])

path_labels = ['Gamma', 'X', 'M', 'Gamma', 'Z', 'R']
segments = [
    make_path(G, X, Nk),
    make_path(X, M, Nk),
    make_path(M, G, Nk),
    make_path(G, Z, Nk),
    make_path(Z, R, Nk),
]
k_path = []
for seg in segments:
    k_path.extend(seg)
k_path = np.array(k_path)

# Also add the final point
k_path = np.vstack([k_path, R])

# Compute dispersion
omega_sq_path, omega_path, evecs_path = dispersion_along_path(
    k_path, rho_vec, J_Leggett, J_xy, J_z
)

# K-distance for plotting
k_dist = np.zeros(len(k_path))
for i in range(1, len(k_path)):
    k_dist[i] = k_dist[i-1] + np.linalg.norm(k_path[i] - k_path[i-1])

# Mark high-symmetry points
hs_indices = [0, Nk, 2*Nk, 3*Nk, 4*Nk, 5*Nk]
hs_distances = [k_dist[i] for i in hs_indices]

print(f"  Path length: {len(k_path)} points")
print(f"  Goldstone band: omega(X) = {omega_path[Nk, 0]:.6f}")
print(f"  Goldstone band: omega(M) = {omega_path[2*Nk, 0]:.6f}")
print(f"  Goldstone band: omega(Z) = {omega_path[4*Nk, 0]:.6f}")

# ===========================================================================
# STEP 4: Quantum Geometric Tensor (QGT) across the BZ
# ===========================================================================
print("\n--- Step 4: Quantum Geometric Tensor ---")

dk = 1e-5  # (local) finite-difference step for dH/dK

def compute_QGT_at_K(kx, ky, kz, rho_vec, J_Leggett, J_xy_val, J_z_val, dk=1e-5):
    """
    Compute the quantum geometric tensor Q_{ij}(K) for the Goldstone band.

    Uses the formula (Berry Paper 01, BP-4 for real part):
        g_{ij} = Re sum_{n!=0} <0|d_i H|n><n|d_j H|0> / (E_n - E_0)^2
        F_{ij} = -2 Im sum_{n!=0} <0|d_i H|n><n|d_j H|0> / (E_n - E_0)^2

    We compute d_i H by finite differences on the Hamiltonian.

    Returns:
        g: (3,3) quantum metric (real, symmetric)
        F: (3,3) Berry curvature (real, antisymmetric)
        tr_g: trace of quantum metric
    """
    K0 = np.array([kx, ky, kz])

    # Reference eigensystem
    H0 = build_H_K(kx, ky, kz, rho_vec, J_Leggett, J_xy_val, J_z_val)
    evals0, evecs0 = eigh(H0)

    # Goldstone = band 0 (lowest)
    psi_0 = evecs0[:, 0]
    E_0 = evals0[0]

    # Compute dH/dK_i by finite differences
    dH = np.zeros((3, 3, 3), dtype=float)  # dH[i] = dH/dK_i, shape (3,3)
    for i in range(3):
        K_plus = K0.copy()
        K_minus = K0.copy()
        K_plus[i] += dk
        K_minus[i] -= dk

        H_plus = build_H_K(*K_plus, rho_vec, J_Leggett, J_xy_val, J_z_val)
        H_minus = build_H_K(*K_minus, rho_vec, J_Leggett, J_xy_val, J_z_val)

        dH[i] = (H_plus - H_minus) / (2 * dk)

    # Compute QGT using sum over excited states
    n_bands = len(evals0)
    g = np.zeros((3, 3))
    F_berry = np.zeros((3, 3))

    for n in range(1, n_bands):
        psi_n = evecs0[:, n]
        E_n = evals0[n]
        gap_sq = (E_n - E_0)**2

        if gap_sq < 1e-30:
            continue

        for i in range(3):
            for j in range(3):
                matrix_elem = np.dot(psi_0, dH[i] @ psi_n) * np.dot(psi_n, dH[j] @ psi_0)
                # For real H: matrix elements are real
                # g_{ij} = Re[...] / gap^2 = real / gap^2
                # F_{ij} = -2 Im[...] / gap^2 = 0 for real H
                g[i, j] += np.real(matrix_elem) / gap_sq
                F_berry[i, j] += -2 * np.imag(matrix_elem) / gap_sq

    # Symmetrize g (should be symmetric), antisymmetrize F
    g = 0.5 * (g + g.T)
    F_berry = 0.5 * (F_berry - F_berry.T)

    return g, F_berry, np.trace(g)


# Compute QGT on a grid in the BZ
Ng = 16  # (local) QGT grid points per direction
kx_grid = 2 * PI * np.arange(Ng) / Ng  # [0, 2pi) with period matching lattice
ky_grid = 2 * PI * np.arange(Ng) / Ng
kz_grid = 2 * PI * np.arange(Ng) / Ng

# Store results
g_trace_grid = np.zeros((Ng, Ng, Ng))
g_tensor_grid = np.zeros((Ng, Ng, Ng, 3, 3))
F_tensor_grid = np.zeros((Ng, Ng, Ng, 3, 3))
omega_grid = np.zeros((Ng, Ng, Ng, 3))
K_mag_grid = np.zeros((Ng, Ng, Ng))

print(f"  Computing QGT on {Ng}^3 = {Ng**3} grid...")
t_qgt = time.time()

for ix in range(Ng):
    for iy in range(Ng):
        for iz in range(Ng):
            kx = kx_grid[ix]
            ky = ky_grid[iy]
            kz = kz_grid[iz]

            # Compute eigensystem
            evals, evecs, _ = eigensystem_at_K(kx, ky, kz, rho_vec, J_Leggett, J_xy, J_z)
            omega_grid[ix, iy, iz] = np.sqrt(np.maximum(evals, 0))

            # K magnitude (use lattice-appropriate |K|)
            # For BZ centered at Gamma: use sin(k/2) for lattice momentum
            K_eff_sq = (4 * J_xy * (np.sin(kx/2)**2 + np.sin(ky/2)**2)
                       + 4 * J_z * np.sin(kz/2)**2) / (J_xy + J_xy + J_z) * 3
            K_mag_grid[ix, iy, iz] = np.sqrt(K_eff_sq) if K_eff_sq > 0 else 0

            # Compute QGT (skip K=0 to avoid zero-mode issue)
            if abs(kx) + abs(ky) + abs(kz) > 1e-10:
                g, F, tr_g = compute_QGT_at_K(kx, ky, kz, rho_vec, J_Leggett, J_xy, J_z)
                g_trace_grid[ix, iy, iz] = tr_g
                g_tensor_grid[ix, iy, iz] = g
                F_tensor_grid[ix, iy, iz] = F

dt_qgt = time.time() - t_qgt
print(f"  QGT computation: {dt_qgt:.1f}s")

# QGT statistics
mask_nonzero = g_trace_grid > 1e-20
print(f"\n  QGT Statistics (nonzero points: {np.sum(mask_nonzero)} / {Ng**3}):")
print(f"    tr(g) max  = {np.max(g_trace_grid):.6e}")
print(f"    tr(g) mean = {np.mean(g_trace_grid[mask_nonzero]):.6e}")
print(f"    tr(g) min  = {np.min(g_trace_grid[mask_nonzero]):.6e}" if np.any(mask_nonzero) else "    No nonzero points")
print(f"    max|F_ij|  = {np.max(np.abs(F_tensor_grid)):.6e} (should be ~0 for real H)")

# BZ-averaged quantum metric
g_BZ_avg = np.mean(g_tensor_grid, axis=(0, 1, 2))
tr_g_BZ_avg = np.trace(g_BZ_avg)
print(f"\n  BZ-averaged quantum metric:")
print(f"    <g_xx> = {g_BZ_avg[0,0]:.6e}")
print(f"    <g_yy> = {g_BZ_avg[1,1]:.6e}")
print(f"    <g_zz> = {g_BZ_avg[2,2]:.6e}")
print(f"    <tr(g)> = {tr_g_BZ_avg:.6e}")

# ===========================================================================
# STEP 5: Extract K^4 coefficient from dispersion fitting
# ===========================================================================
print("\n--- Step 5: K^4 coefficient from dispersion ---")

# Along Gamma->X direction (kx only, ky=kz=0)
# This is the in-plane direction with strongest coupling
Nfit = 100                             # (local) fit-sample count along G->X
kx_fit = np.linspace(0.01, PI, Nfit)  # (local) avoid K=0 singular

omega_fit_GX = np.zeros((Nfit, 3))
for i, kx in enumerate(kx_fit):
    evals, _, _ = eigensystem_at_K(kx, 0, 0, rho_vec, J_Leggett, J_xy, J_z)
    omega_fit_GX[i] = np.sqrt(np.maximum(evals, 0))

# Goldstone dispersion
omega_gold_GX = omega_fit_GX[:, 0]

# For small K, the lattice dispersion is:
#   lambda(K) = J_xy * kx^2 + O(kx^4)   (Taylor of 2*J_xy*(1-cos(kx)))
# So omega ~ c * kx near Gamma.
# The effective sound speed c_eff = sqrt(lambda'(0)/rho_eff) for the Goldstone mode.

# Fit omega(kx) = a1*kx + a2*kx^2 + a3*kx^3 + a4*kx^4 (odd + even terms)
# Actually, by symmetry omega(K) = omega(-K), so omega(kx) should be even in kx
# when plotted as omega vs |kx|. But omega = sqrt(omega^2) and omega^2 is even.
# omega^2(kx) = c^2 kx^2 + alpha_2 kx^4 + alpha_3 kx^6 + ...

# Fit omega^2 as function of kx^2
kx_small_K_cut = 0.5              # (local) small-K regime upper bound (half of pi/2)
kx_small = kx_fit[kx_fit < kx_small_K_cut]  # (local) small-K regime
omega_sq_small = omega_gold_GX[kx_fit < kx_small_K_cut]**2
kx2_small = kx_small**2

# Polynomial fit: omega^2 = c0 + c2*kx^2 + c4*kx^4
# c0 should be ~0 (Goldstone), c2 = c_s^2, c4 = K^4 coefficient
from numpy.polynomial import polynomial as P
coeffs = P.polyfit(kx2_small, omega_sq_small, 3)  # fit omega^2 vs kx^2 up to (kx^2)^3
# coeffs[0] = constant, coeffs[1] = linear in kx^2, coeffs[2] = quadratic in kx^2, etc.
# omega^2 = coeffs[0] + coeffs[1]*kx^2 + coeffs[2]*kx^4 + coeffs[3]*kx^6

c_sq_eff = coeffs[1]  # effective c_s^2 in lattice units
c_eff = np.sqrt(c_sq_eff) if c_sq_eff > 0 else 0
alpha_4_raw = coeffs[2]  # K^4 coefficient in omega^2

print(f"  Fit: omega^2 = {coeffs[0]:.6e} + {coeffs[1]:.6e}*K^2 + {coeffs[2]:.6e}*K^4 + {coeffs[3]:.6e}*K^6")
print(f"  c_eff (lattice units) = {c_eff:.6f}")
print(f"  K^4 coefficient (omega^2) = {alpha_4_raw:.6e}")

# The correction to the dispersion:
# omega = c_eff * |K| * sqrt(1 + (alpha_4/c_sq) * K^2 + ...)
# => omega ~ c_eff * |K| * (1 + (alpha_4/(2*c_sq)) * K^2 + ...)
# alpha_QM = alpha_4 / (2 * c_sq_eff) if viewed as correction to omega
# or alpha_QM = alpha_4 / c_sq_eff if viewed as correction to omega^2

alpha_QM_omega = alpha_4_raw / (2 * c_sq_eff) if abs(c_sq_eff) > 1e-30 else 0
alpha_QM_omega_sq = alpha_4_raw / c_sq_eff if abs(c_sq_eff) > 1e-30 else 0

print(f"\n  alpha_QM (correction to omega):    {alpha_QM_omega:.6e}")
print(f"  alpha_QM (correction to omega^2):  {alpha_QM_omega_sq:.6e}")

# Repeat for Gamma->Z direction (inter-plane, kz only)
kz_fit = np.linspace(0.01, PI, Nfit)
omega_fit_GZ = np.zeros((Nfit, 3))
for i, kz in enumerate(kz_fit):
    evals, _, _ = eigensystem_at_K(0, 0, kz, rho_vec, J_Leggett, J_xy, J_z)
    omega_fit_GZ[i] = np.sqrt(np.maximum(evals, 0))

omega_gold_GZ = omega_fit_GZ[:, 0]

kz_small = kz_fit[kz_fit < kx_small_K_cut]             # (local) reuse small-K cut
omega_sq_small_z = omega_gold_GZ[kz_fit < kx_small_K_cut]**2  # (local)
kz2_small = kz_small**2

coeffs_z = P.polyfit(kz2_small, omega_sq_small_z, 3)
c_sq_z = coeffs_z[1]
c_z = np.sqrt(c_sq_z) if c_sq_z > 0 else 0
alpha_4_z = coeffs_z[2]
alpha_QM_z = alpha_4_z / (2 * c_sq_z) if abs(c_sq_z) > 1e-30 else 0

print(f"\n  Gamma->Z direction:")
print(f"    c_z (lattice) = {c_z:.6f}")
print(f"    K^4 coeff     = {alpha_4_z:.6e}")
print(f"    alpha_QM_z    = {alpha_QM_z:.6e}")

# Speed of sound anisotropy
if c_z > 0 and c_eff > 0:
    print(f"\n  Sound speed anisotropy: c_xy / c_z = {c_eff / c_z:.4f}")

# ===========================================================================
# STEP 6: Effective power-law index n_eff(K)
# ===========================================================================
print("\n--- Step 6: Effective power-law index ---")

# n_eff(K) = d log(omega) / d log(K)
# For omega = c*K: n_eff = 1 (acoustic)
# For omega = c*K*(1 + alpha*K^2): n_eff = 1 + 2*alpha*K^2/(1+alpha*K^2)

# Compute n_eff along Gamma->X
# Use log-derivative: n_eff = K * (domega/dK) / omega
K_eval = kx_fit[2:-2]  # avoid edges
omega_eval = omega_gold_GX[2:-2]
domega = np.gradient(omega_gold_GX, kx_fit)[2:-2]
n_eff_GX = K_eval * domega / omega_eval

# n_eff along Gamma->Z
K_eval_z = kz_fit[2:-2]
omega_eval_z = omega_gold_GZ[2:-2]
domega_z = np.gradient(omega_gold_GZ, kz_fit)[2:-2]
n_eff_GZ = K_eval_z * domega_z / omega_eval_z

print(f"  n_eff at K=0.1 (G->X): {np.interp(0.1, K_eval, n_eff_GX):.6f}")
print(f"  n_eff at K=0.5 (G->X): {np.interp(0.5, K_eval, n_eff_GX):.6f}")
print(f"  n_eff at K=1.0 (G->X): {np.interp(1.0, K_eval, n_eff_GX):.6f}")
print(f"  n_eff at K=pi  (G->X): {n_eff_GX[-1]:.6f}")

print(f"\n  n_eff at K=0.1 (G->Z): {np.interp(0.1, K_eval_z, n_eff_GZ):.6f}")
print(f"  n_eff at K=0.5 (G->Z): {np.interp(0.5, K_eval_z, n_eff_GZ):.6f}")
print(f"  n_eff at K=1.0 (G->Z): {np.interp(1.0, K_eval_z, n_eff_GZ):.6f}")

# What K_pivot would give delta_n = 0.035 (Planck's n_s - 1)?
# We want n_eff(K_pivot) = 1 - 0.035 = 0.965
# From the fit: n_eff ~ 1 + 2*alpha_QM*K^2 for small alpha*K^2
# If alpha_QM > 0: n_eff > 1 (blue tilt), need negative alpha for red tilt
# Lattice effects ALWAYS give n_eff < 1 at large K (cosine flattens)

# The K where n_eff = Planck's n_s (canonical planck_ns; preserve legacy rounding)
target = 0.965  # (local) tilted spectrum reference (legacy rounding of planck_ns)
idx_target_GX = np.argmin(np.abs(n_eff_GX - target))
K_target_GX = K_eval[idx_target_GX]
print(f"\n  K where n_eff = {target} (G->X): K = {K_target_GX:.4f}")
print(f"    (K/K_BZ = {K_target_GX / PI:.4f})")

idx_target_GZ = np.argmin(np.abs(n_eff_GZ - target))
K_target_GZ = K_eval_z[idx_target_GZ]
print(f"  K where n_eff = {target} (G->Z): K = {K_target_GZ:.4f}")

# ===========================================================================
# STEP 7: Quantum metric contribution vs lattice contribution
# ===========================================================================
print("\n--- Step 7: Decomposition of K^4 correction ---")

# The K^4 correction has TWO sources:
# 1. LATTICE: cosine dispersion -> omega^2 = 2J(1-cos(k)) = Jk^2 - Jk^4/12 + ...
#    This gives alpha_lattice = -1/12 in omega^2 = c^2 k^2 (1 - k^2/12 + ...)
# 2. QUANTUM METRIC: hybridization with Leggett modes changes the Goldstone eigenvector
#    composition, contributing an additional K^4 term proportional to <g_ii>.

# For a single-band model: alpha_4 = -c^2/12 (pure lattice)
# For multi-band: alpha_4 = -c^2/12 + delta_alpha (quantum metric correction)

# Compute single-band reference (all rho equal -> no hybridization)
rho_uniform = np.array([1.0, 1.0, 1.0]) * np.mean(rho_vec)
omega_gold_ref = np.zeros(Nfit)
for i, kx in enumerate(kx_fit):
    evals, _, _ = eigensystem_at_K(kx, 0, 0, rho_uniform, J_Leggett, J_xy, J_z)
    omega_gold_ref[i] = np.sqrt(max(evals[0], 0))

omega_sq_ref_small = omega_gold_ref[kx_fit < kx_small_K_cut]**2  # (local)
coeffs_ref = P.polyfit(kx2_small, omega_sq_ref_small, 3)
alpha_4_ref = coeffs_ref[2]
c_sq_ref = coeffs_ref[1]

alpha_QM_ref = alpha_4_ref / (2 * c_sq_ref) if abs(c_sq_ref) > 1e-30 else 0

# Also compute the "no Leggett" case (J_Leggett = 0)
omega_gold_nolg = np.zeros(Nfit)
J_zero = np.zeros((3, 3))
for i, kx in enumerate(kx_fit):
    evals, _, _ = eigensystem_at_K(kx, 0, 0, rho_vec, J_zero, J_xy, J_z)
    omega_gold_nolg[i] = np.sqrt(max(evals[0], 0))

omega_sq_nolg_small = omega_gold_nolg[kx_fit < kx_small_K_cut]**2  # (local)
coeffs_nolg = P.polyfit(kx2_small, omega_sq_nolg_small, 3)
alpha_4_nolg = coeffs_nolg[2]
c_sq_nolg = coeffs_nolg[1]

alpha_QM_nolg = alpha_4_nolg / (2 * c_sq_nolg) if abs(c_sq_nolg) > 1e-30 else 0

print(f"  Single-band reference (uniform rho):")
print(f"    alpha_4 (omega^2)     = {alpha_4_ref:.6e}")
print(f"    alpha_QM (omega)      = {alpha_QM_ref:.6e}")
print(f"\n  No-Leggett reference (J_Leggett=0):")
print(f"    alpha_4 (omega^2)     = {alpha_4_nolg:.6e}")
print(f"    alpha_QM (omega)      = {alpha_QM_nolg:.6e}")
print(f"\n  Full multi-band:")
print(f"    alpha_4 (omega^2)     = {alpha_4_raw:.6e}")
print(f"    alpha_QM (omega)      = {alpha_QM_omega:.6e}")

delta_alpha_QM = alpha_QM_omega - alpha_QM_nolg
print(f"\n  QUANTUM METRIC CONTRIBUTION:")
print(f"    delta_alpha = alpha_full - alpha_no_Leggett = {delta_alpha_QM:.6e}")
print(f"    Fractional: delta_alpha / alpha_lattice = {abs(delta_alpha_QM / alpha_QM_nolg):.4f}" if abs(alpha_QM_nolg) > 1e-30 else "    (no lattice reference)")

# ===========================================================================
# STEP 8: Gate Verdict
# ===========================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: QM-DISPERSION-52")
print("=" * 78)

# The gate criterion:
# PASS if K^4 correction modifies effective power-law index by > 0.01 at K_pivot
# FAIL if K^4 correction < 0.001 at K_pivot

# K_pivot is not yet determined (depends on W2-A). Evaluate at several K values.
K_pivots = [0.05, 0.1, 0.2, 0.5, 1.0]   # (local) candidate pivot K (lattice units)
print(f"\n  Power-law modification |n_eff - 1| at candidate K_pivot values:")
print(f"  {'K_pivot':>8s}  {'n_eff(G->X)':>12s}  {'|dn_QM|':>12s}  {'verdict':>10s}")
print(f"  {'-'*8}  {'-'*12}  {'-'*12}  {'-'*10}")

gate_pass = False
for K_p in K_pivots:
    if K_p < K_eval[0] or K_p > K_eval[-1]:
        continue
    n_at_Kp = np.interp(K_p, K_eval, n_eff_GX)
    # Quantum metric contribution: difference from single-band
    # Compute n_eff for no-Leggett case
    domega_nolg = np.gradient(omega_gold_nolg, kx_fit)
    n_eff_nolg = kx_fit * domega_nolg / np.where(omega_gold_nolg > 1e-30, omega_gold_nolg, 1)
    n_nolg = np.interp(K_p, kx_fit[2:-2], n_eff_nolg[2:-2])

    dn_QM = abs(n_at_Kp - n_nolg)

    qm_pass_thresh = 0.01    # (local) gate PASS threshold (n_eff modification > 0.01)
    qm_fail_thresh = 0.001   # (local) gate FAIL threshold (n_eff modification < 0.001)
    if dn_QM > qm_pass_thresh:
        verdict = "PASS"
        gate_pass = True
    elif dn_QM < qm_fail_thresh:
        verdict = "FAIL"
    else:
        verdict = "MARGINAL"

    print(f"  {K_p:>8.3f}  {n_at_Kp:>12.6f}  {dn_QM:>12.6e}  {verdict:>10s}")

# Overall gate verdict
# Since the full alpha_QM and delta_alpha are the primary numbers:
print(f"\n  Primary numbers:")
print(f"    alpha_QM (full, omega correction) = {alpha_QM_omega:.6e}")
print(f"    delta_alpha_QM (quantum metric)   = {delta_alpha_QM:.6e}")
print(f"    BZ-averaged tr(g)                 = {tr_g_BZ_avg:.6e}")
print(f"    max Berry curvature |F|           = {np.max(np.abs(F_tensor_grid)):.6e}")

# The K^4 correction at K~0.1 (physical pivot scale):
delta_n_01 = abs(np.interp(0.1, K_eval, n_eff_GX) - 1.0) if 0.1 >= K_eval[0] and 0.1 <= K_eval[-1] else 0

if gate_pass:
    gate_status = "PASS"
    gate_msg = f"Quantum metric K^4 correction modifies n_eff by > {qm_pass_thresh} at some K_pivot"
elif delta_n_01 > qm_fail_thresh:
    gate_status = "INFO"
    gate_msg = f"K^4 correction is {delta_n_01:.4e} at K=0.1 (between PASS and FAIL thresholds)"
else:
    gate_status = "FAIL"
    gate_msg = f"K^4 correction < {qm_fail_thresh} at K=0.1"

print(f"\n  GATE STATUS: {gate_status}")
print(f"  {gate_msg}")

# ===========================================================================
# STEP 9: Save data
# ===========================================================================
print("\n--- Step 9: Save results ---")

save_path = os.path.join(SCRIPT_DIR, 's52_qm_dispersion.npz')
np.savez_compressed(
    save_path,
    # Grid data
    kx_grid=kx_grid, ky_grid=ky_grid, kz_grid=kz_grid,
    g_trace_grid=g_trace_grid,
    g_tensor_grid=g_tensor_grid,
    F_tensor_grid=F_tensor_grid,
    omega_grid=omega_grid,
    K_mag_grid=K_mag_grid,
    # Path data
    k_path=k_path,
    k_dist=k_dist,
    omega_path=omega_path,
    hs_distances=np.array(hs_distances),
    hs_labels=np.array(path_labels),
    # Fit data
    kx_fit=kx_fit,
    omega_gold_GX=omega_gold_GX,
    omega_gold_GZ=omega_gold_GZ,
    kz_fit=kz_fit,
    n_eff_GX=n_eff_GX,
    K_eval_GX=K_eval,
    n_eff_GZ=n_eff_GZ,
    K_eval_GZ=K_eval_z,
    # Coefficients
    coeffs_GX=coeffs,
    coeffs_GZ=coeffs_z,
    alpha_QM_omega=alpha_QM_omega,
    alpha_QM_omega_sq=alpha_QM_omega_sq,
    alpha_QM_z=alpha_QM_z,
    delta_alpha_QM=delta_alpha_QM,
    tr_g_BZ_avg=tr_g_BZ_avg,
    c_eff_xy=c_eff,
    c_eff_z=c_z,
    # Parameters
    J_xy=J_xy, J_z=J_z,
    J_12=J_12, J_13=J_13, J_23=J_23,
    rho_vec=rho_vec,
    gate_status=gate_status,
)
print(f"  Saved to {save_path}")

# ===========================================================================
# STEP 10: Plot
# ===========================================================================
print("\n--- Step 10: Plotting ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# (a) Band structure along high-symmetry path
ax = axes[0, 0]
for band in range(3):
    label = ['Goldstone', 'Leggett 1', 'Leggett 2'][band]
    ax.plot(k_dist, omega_path[:, band], label=label)
for d, l in zip(hs_distances, path_labels):
    ax.axvline(d, color='gray', lw=0.5, ls='--')
ax.set_xticks(hs_distances)
ax.set_xticklabels([r'$\Gamma$', 'X', 'M', r'$\Gamma$', 'Z', 'R'])
ax.set_ylabel(r'$\omega$ [M_KK]')
ax.set_title('Band Structure')
ax.legend(fontsize=8)
ax.set_ylim(bottom=0)

# (b) Goldstone dispersion along G->X with fit
ax = axes[0, 1]
ax.plot(kx_fit, omega_gold_GX, 'b-', label='Goldstone (G->X)')
ax.plot(kx_fit, omega_gold_GZ, 'r--', label='Goldstone (G->Z)')
# Plot the linear approximation
kx_lin = np.linspace(0, 0.5, 50)
ax.plot(kx_lin, c_eff * kx_lin, 'b:', alpha=0.5, label=f'Linear: c={c_eff:.3f}')
ax.plot(kx_lin, c_z * kx_lin, 'r:', alpha=0.5, label=f'Linear: c_z={c_z:.3f}')
ax.set_xlabel('K')
ax.set_ylabel(r'$\omega$ [M_KK]')
ax.set_title('Goldstone Dispersion')
ax.legend(fontsize=8)
ax.set_xlim(0, PI)

# (c) Effective power-law index
ax = axes[0, 2]
ax.plot(K_eval, n_eff_GX, 'b-', label='G->X')
ax.plot(K_eval_z, n_eff_GZ, 'r--', label='G->Z')
ax.axhline(1.0, color='k', lw=0.5, ls=':')
ax.axhline(0.965, color='green', lw=1, ls='--', label='n_s = 0.965 (Planck)')
ax.set_xlabel('K')
ax.set_ylabel(r'$n_{eff}(K)$')
ax.set_title('Effective Power-Law Index')
ax.legend(fontsize=8)
ax.set_ylim(0.5, 1.2)

# (d) Quantum metric trace across BZ (kz=0 slice)
ax = axes[1, 0]
g_slice = g_trace_grid[:, :, 0]
im = ax.imshow(g_slice.T, origin='lower', aspect='equal',
               extent=[0, 2*PI, 0, 2*PI], cmap='hot')
plt.colorbar(im, ax=ax, label='tr(g)')
ax.set_xlabel(r'$k_x$')
ax.set_ylabel(r'$k_y$')
ax.set_title(r'Quantum Metric tr($g$), $k_z=0$')

# (e) Quantum metric vs K along G->X
ax = axes[1, 1]
# Extract g along kx axis (ky=kz=0)
g_along_GX = g_trace_grid[:, 0, 0]
kx_plot = kx_grid
ax.plot(kx_plot, g_along_GX, 'b-o', markersize=3, label=r'tr(g) along $\Gamma\to X$')
ax.set_xlabel(r'$k_x$')
ax.set_ylabel(r'tr($g$)')
ax.set_title('Quantum Metric Along G->X')
ax.legend(fontsize=8)

# (f) K^4 decomposition
ax = axes[1, 2]
# Plot omega^2 / K^2 vs K^2 — deviations from constant = K^4 correction
kx_plot2 = kx_fit[1:]  # skip K=0
ratio_full = omega_gold_GX[1:]**2 / kx_plot2**2
ratio_nolg = omega_gold_nolg[1:]**2 / kx_plot2**2
ax.plot(kx_plot2**2, ratio_full, 'b-', label='Full (multi-band)')
ax.plot(kx_plot2**2, ratio_nolg, 'r--', label='No Leggett')
ax.plot(kx_plot2**2, ratio_full[0] * np.ones_like(kx_plot2), 'k:', alpha=0.3, label='Pure acoustic')
ax.set_xlabel(r'$K^2$')
ax.set_ylabel(r'$\omega^2 / K^2$')
ax.set_title(r'$\omega^2/K^2$ vs $K^2$ (K$^4$ deviation)')
ax.legend(fontsize=8)
ax.set_xlim(0, PI**2)

plt.suptitle(f'QM-DISPERSION-52: Quantum Metric K$^4$ Correction\n'
             f'Gate: {gate_status} | alpha_QM = {alpha_QM_omega:.3e} | '
             f'delta_alpha(QM) = {delta_alpha_QM:.3e} | '
             f'<tr(g)> = {tr_g_BZ_avg:.3e}',
             fontsize=12, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])

plot_path = os.path.join(SCRIPT_DIR, 's52_qm_dispersion.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Plot saved to {plot_path}")

dt_total = time.time() - t0
print(f"\n  Total runtime: {dt_total:.1f}s")
print("  DONE.")
