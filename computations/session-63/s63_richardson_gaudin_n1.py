#!/usr/bin/env python3
"""
RICHARDSON-GAUDIN-N1-63: Exact N=1 Pair Solution on CG(24)
===========================================================

Gate: RICHARDSON-GAUDIN-N1-63 | W3-04 | INFO | E_exact/E_BCS ratio

Physics:
  The Richardson equation for M=1 pair on L levels reads:
    1 + G * sum_j  Omega_j / (2*eps_j - E_alpha) = 0
  where Omega_j = pair degeneracy of level j (= 1 for time-reversed pairs).

  This is a single transcendental equation — no pair-pair interaction term
  for M=1. The exact pair energy E_alpha gives E_exact = E_seniority + E_alpha.

  We compare to BCS mean-field (gap equation + number equation) and to
  PBCS (projected BCS, exact for separable V).

Method:
  1. Build fabric Hamiltonian: 24 CG(24) cells x 8 BCS modes = 192 levels
  2. Single-particle spectrum from tight-binding on CG(24) with Josephson E_J
  3. Pairing interaction: rank-1 separable from S60 SVD (g_eff * u_i * u_j)
  4. Solve Richardson equation for E_alpha (Newton's method with pole avoidance)
  5. Solve BCS gap+number equations for comparison
  6. Compute correlation energy, occupations, pair wavefunction structure

References:
  Paper 15 (Dukelsky, Pittel, Sierra 2004): Richardson-Gaudin colloquium
  Paper 17 (von Delft, Ralph 2001): Ultrasmall BCS
  Paper 03 (Dobaczewski, Nazarewicz 2013): HFB pairing Hamiltonian

Session: S63 W3-04
"""

import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.linalg import eigh
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    tau_fold, E_B1, E_B2_mean, E_B3_mean, N_cells as N_CELLS_CANONICAL,
    E_cond, Delta_0_OES, xi_BCS, N_dof_BCS
)

# =============================================================================
# Section 1: Load CG(24) adjacency and single-cell BCS data
# =============================================================================

# CG(24) adjacency from S60
cg24_data = np.load('computations/session-60/s60_entangle_cg24.npz', allow_pickle=True)
adj_cg24 = cg24_data['adj'].astype(float)  # 24x24
N_cells = int(cg24_data['N_vertices'])      # = 24
degree = int(cg24_data['degree'])           # = 6

# Single-cell BCS data from S52 HFB
hfb_data = np.load('computations/session-52/s52_hfb_full.npz', allow_pickle=True)
eps_bare = hfb_data['E_sp_bare']       # 8 single-particle energies
V_bare = hfb_data['V_bare']            # 8x8 pairing interaction
labels = hfb_data['labels']            # mode labels

# E_J from S56 uncertainty quantification
E_J = 7.041511479282989  # M_KK, from s56_ej_uncertainty.npz  # (local)

# Rank-1 separable decomposition from S60
rg_data = np.load('computations/session-60/s60_rg_integrals.npz', allow_pickle=True)
g_eff = float(rg_data['g_eff'])        # = 0.2758 M_KK (rank-1 strength)
u_vec = rg_data['u_vec']               # 8-component (single-cell mode amplitudes)
rank1_frac = float(rg_data['svd_rank1_fraction'])  # 64.3% of V captured by rank-1

# GGE occupations from S62
gge_data = np.load('computations/session-62/s62_meissner_gge.npz', allow_pickle=True)
n_k_GGE = gge_data['n_k_GGE']         # 8 GGE occupations per cell
F_k_GGE = gge_data['F_k_GGE']         # 8 anomalous densities per cell

N_modes = len(eps_bare)  # = 8

print("="*70)
print("RICHARDSON-GAUDIN-N1-63: Exact N=1 Pair on CG(24)")
print("="*70)
print(f"CG(24): {N_cells} cells, degree {degree}, {N_cells * N_modes} total levels")
print(f"Single-cell modes: {list(labels)}")
print(f"eps_bare: {eps_bare}")
print(f"E_J = {E_J:.6f} M_KK")
print(f"g_eff = {g_eff:.6f} M_KK (rank-1 SVD, {rank1_frac*100:.1f}% of V)")
print()

# =============================================================================
# Section 2: Build fabric Hamiltonian — tight-binding on CG(24)
# =============================================================================
#
# The fabric single-particle Hamiltonian is:
#   H_0 = sum_i sum_k eps_k c^dag_{ik} c_{ik}  +  E_J * sum_{<ij>} sum_k c^dag_{ik} c_{jk}
#
# where i labels cells, k labels modes within a cell, and <ij> are CG(24) bonds.
# This gives a 192x192 matrix (24 cells x 8 modes), block-diagonal in mode index k
# because Josephson couples same-mode between cells.
#
# For each mode k, the tight-binding Hamiltonian is:
#   H_k = eps_k * I_{24} + E_J * adj_cg24
#
# The eigenvalues of adj_cg24 give the band structure.

print("--- Fabric Single-Particle Spectrum ---")

# Diagonalize CG(24) adjacency to get Bloch-like eigenvalues
evals_adj, evecs_adj = eigh(adj_cg24)
print(f"CG(24) adjacency eigenvalues: {evals_adj}")
print(f"  min = {evals_adj[0]:.4f}, max = {evals_adj[-1]:.4f}")
print(f"  Bandwidth = {E_J * (evals_adj[-1] - evals_adj[0]):.4f} M_KK")

# Full fabric spectrum: for each mode k, the 24 eigenvalues are eps_k + E_J * lambda_n
# Total: 8 modes x 24 cells = 192 levels
L_total = N_cells * N_modes
eps_fabric = np.zeros(L_total)
mode_index = np.zeros(L_total, dtype=int)    # which intra-cell mode
cell_index = np.zeros(L_total, dtype=int)    # which CG(24) eigenvalue
u_fabric = np.zeros(L_total)                 # pairing amplitude for rank-1 V

for k in range(N_modes):
    for n in range(N_cells):
        idx = k * N_cells + n
        eps_fabric[idx] = eps_bare[k] + E_J * evals_adj[n]
        mode_index[idx] = k
        cell_index[idx] = n
        # Rank-1 pairing amplitude on fabric:
        # V_{(k,n),(k',n')} = g_eff * u_k * u_{k'} * delta_{n,n'}  (same-cell pairing)
        # OR for inter-cell: need Josephson-mediated pair hopping
        # For rank-1 SEPARABLE model (Richardson-solvable):
        #   V_{j,j'} = G * f_j * f_{j'}
        # where j = (k,n) composite index
        # The mode amplitude is u_k (from SVD), and the cell factor is
        # evecs_adj[cell_i, n] — the Bloch amplitude on cell i for eigenvalue n.
        # For uniform (k=0) mode of CG(24): evecs_adj[:,N-1] = 1/sqrt(24)
        # The pairing is LOCAL (same cell), so in the Bloch basis:
        #   <k,n; k',n' | V | k,m; k',m'> = g_eff * u_k * u_{k'} * (1/N) * sum_i ...
        # But for separable model, we use:
        u_fabric[idx] = u_vec[k]  # mode-dependent, cell-independent (uniform pairing)

# Sort by energy
sort_idx = np.argsort(eps_fabric)
eps_sorted = eps_fabric[sort_idx]
u_sorted = u_fabric[sort_idx]
mode_sorted = mode_index[sort_idx]
cell_sorted = cell_index[sort_idx]

print(f"\nFabric spectrum: {L_total} levels")
print(f"  E_min = {eps_sorted[0]:.6f}, E_max = {eps_sorted[-1]:.6f} M_KK")
print(f"  Bandwidth = {eps_sorted[-1] - eps_sorted[0]:.4f} M_KK")
print(f"  Mean level spacing d = {(eps_sorted[-1] - eps_sorted[0])/(L_total-1):.6f} M_KK")

# Print first and last 10 levels
print("\nLowest 10 levels:")
for i in range(min(10, L_total)):
    print(f"  [{i:3d}] eps={eps_sorted[i]:.6f}  mode={labels[mode_sorted[i]]}  "
          f"CG24_eval={evals_adj[cell_sorted[i]]:.4f}  u={u_sorted[i]:.4f}")

print("\nHighest 10 levels:")
for i in range(max(0, L_total-10), L_total):
    print(f"  [{i:3d}] eps={eps_sorted[i]:.6f}  mode={labels[mode_sorted[i]]}  "
          f"CG24_eval={evals_adj[cell_sorted[i]]:.4f}  u={u_sorted[i]:.4f}")

# =============================================================================
# Section 3: Richardson equation for M=1 pair
# =============================================================================
#
# For M=1 pair, the Richardson equation (Paper 15, Eq. 9) simplifies to:
#   1 - 4*G * sum_j  d_j / (2*eps_j - E) = 0
#
# with d_j = -Omega_j/4 for empty levels (seniority zero vacuum).
# For time-reversed pairs with Omega_j = 1 (each level holds 0 or 1 pair):
#   d_j = -1/4
#
# The SEPARABLE model has V_{jj'} = G * f_j * f_{j'}, giving:
#   1 + G * sum_j f_j^2 / (2*eps_j - E) = 0    [rational R-G model]
#
# where G = g_eff and f_j = u_fabric[j].
#
# This is a meromorphic function with poles at E = 2*eps_j.
# Between consecutive poles, it has exactly one root (if they exist).

print("\n" + "="*70)
print("RICHARDSON EQUATION: M=1 pair, L={} levels".format(L_total))
print("="*70)

# Use the sorted spectrum
eps = eps_sorted
f_sq = u_sorted**2  # f_j^2 for separable model
G = g_eff

# Richardson function: R(E) = 1 + G * sum_j f_j^2 / (2*eps_j - E)
def richardson_func(E):
    """Richardson equation for M=1: R(E) = 0"""
    return 1.0 + G * np.sum(f_sq / (2.0 * eps - E))

# The poles are at E = 2*eps_j (sorted)
poles = 2.0 * eps
# Between poles[j] and poles[j+1], there may be a root
# Also below poles[0] (the bound state region)

# Search for ALL roots between consecutive poles
roots = []
margin = 1e-12  # avoid pole singularities

# First check below all poles (bound state)
E_low = poles[0] - 100.0  # far below
try:
    R_low = richardson_func(E_low)
    R_above = richardson_func(poles[0] - margin)
    if R_low * R_above < 0:
        root = brentq(richardson_func, E_low, poles[0] - margin, xtol=1e-14)
        roots.append(root)
        print(f"  Root below poles: E = {root:.10f} M_KK")
except:
    pass

# Between consecutive poles
n_between = 0
for j in range(L_total - 1):
    try:
        R_left = richardson_func(poles[j] + margin)
        R_right = richardson_func(poles[j+1] - margin)
        if R_left * R_right < 0:
            root = brentq(richardson_func, poles[j] + margin, poles[j+1] - margin, xtol=1e-14)
            roots.append(root)
            n_between += 1
    except:
        pass

# Above all poles
E_high = poles[-1] + 100.0
try:
    R_below = richardson_func(poles[-1] + margin)
    R_high = richardson_func(E_high)
    if R_below * R_high < 0:
        root = brentq(richardson_func, poles[-1] + margin, E_high, xtol=1e-14)
        roots.append(root)
        print(f"  Root above poles: E = {root:.10f} M_KK")
except:
    pass

roots = np.array(sorted(roots))
print(f"\nFound {len(roots)} Richardson roots ({n_between} between poles)")
print(f"Ground state pair energy: E_alpha = {roots[0]:.10f} M_KK")

# The exact ground state energy for M=1 pair is just E_alpha
# (no seniority contribution since vacuum has E_seniority = 0)
E_exact = roots[0]

# Pair wavefunction: psi_j = f_j / (2*eps_j - E_alpha)
psi_raw = u_sorted / (2.0 * eps - E_exact)
psi_norm = psi_raw / np.sqrt(np.sum(psi_raw**2))

# Occupation numbers from exact solution
# n_j = |psi_j|^2 (probability of pair occupying level j)
n_exact = psi_norm**2

print(f"\nExact pair wavefunction analysis:")
print(f"  Participation ratio PR = 1/sum(n_j^2) = {1.0/np.sum(n_exact**2):.2f}")
print(f"  Pair energy E_alpha = {E_exact:.10f} M_KK")

# Analyze by mode type
for k in range(N_modes):
    mask = (mode_sorted == k)
    print(f"  {labels[k]:>6s}: sum(n_j) = {np.sum(n_exact[mask]):.6f}, "
          f"max(n_j) = {np.max(n_exact[mask]):.6f}")

# =============================================================================
# Section 4: BCS Mean-Field Solution
# =============================================================================
#
# For the separable interaction V_{jj'} = G * f_j * f_{j'}, the BCS gap equation
# (Paper 15, Eq. 51 in discrete form) gives:
#   Delta_j = Delta * f_j  (separable gap)
#   1 = G * sum_j f_j^2 / (2 * E_qp_j)
# where E_qp_j = sqrt((eps_j - mu)^2 + Delta^2 * f_j^2)
#
# Number equation: sum_j v_j^2 = N_pair (= 1 here)
# where v_j^2 = (1/2)(1 - (eps_j - mu)/E_qp_j)

print("\n" + "="*70)
print("BCS MEAN-FIELD SOLUTION")
print("="*70)

def bcs_equations(params):
    """BCS gap + number equations for separable V, N_pair=1"""
    Delta, mu = params
    if Delta <= 0:
        return [1e10, 1e10]
    E_qp = np.sqrt((eps - mu)**2 + (Delta * np.abs(u_sorted))**2)
    # Gap equation: 1 = G * sum f_j^2 / (2*E_qp_j)
    gap_eq = 1.0 - G * np.sum(f_sq / (2.0 * E_qp))
    # Number equation: sum v_j^2 = N_pair
    v_sq = 0.5 * (1.0 - (eps - mu) / E_qp)
    num_eq = np.sum(v_sq) - 1.0
    return [gap_eq, num_eq]

# Solve BCS by iteration
# Initial guess: mu near lowest levels, small Delta
from scipy.optimize import fsolve

# Try multiple initial conditions
best_E_bcs = np.inf
best_Delta = 0
best_mu = 0
best_converged = False

for mu_init in np.linspace(eps[0] - 0.1, eps[10], 20):
    for Delta_init in [0.001, 0.01, 0.05, 0.1, 0.5]:
        try:
            sol = fsolve(bcs_equations, [Delta_init, mu_init], full_output=True)
            x, info, ier, msg = sol
            if ier == 1 and x[0] > 1e-10:
                Delta_bcs, mu_bcs = x
                E_qp = np.sqrt((eps - mu_bcs)**2 + (Delta_bcs * np.abs(u_sorted))**2)
                v_sq = 0.5 * (1.0 - (eps - mu_bcs) / E_qp)
                # BCS energy: E_BCS = 2*sum_j eps_j * v_j^2 - Delta^2/G
                E_bcs = 2.0 * np.sum(eps * v_sq) - Delta_bcs**2 / G
                # For M=1 pair: E_BCS = sum_j eps_j * 2*v_j^2 - Delta^2/G
                # But with separable V: E_BCS = 2*sum eps_j v_j^2 + G*(sum f_j u_j v_j)^2
                # Simpler: use standard BCS GS energy
                if E_bcs < best_E_bcs:
                    best_E_bcs = E_bcs
                    best_Delta = Delta_bcs
                    best_mu = mu_bcs
                    best_converged = True
        except:
            pass

# If BCS collapses (Delta -> 0), use number-projected BCS (PBCS)
bcs_collapsed = not best_converged or best_Delta < 1e-8

if not bcs_collapsed:
    Delta_bcs = best_Delta
    mu_bcs = best_mu
    E_qp_bcs = np.sqrt((eps - mu_bcs)**2 + (Delta_bcs * np.abs(u_sorted))**2)
    v_sq_bcs = 0.5 * (1.0 - (eps - mu_bcs) / E_qp_bcs)
    u_sq_bcs = 1.0 - v_sq_bcs
    n_bcs = v_sq_bcs  # per level (pair occupation)

    # BCS energy for N_pair pairs
    # E_BCS = 2*sum eps_j v_j^2 - Delta^2/G
    E_bcs_raw = 2.0 * np.sum(eps * v_sq_bcs) - Delta_bcs**2 / G

    # But this is the grand-canonical energy. For comparison with Richardson at
    # fixed N_pair=1, we should use the canonical BCS energy.
    # In practice, for large L, grand-canonical ~ canonical.
    # The pair condensation energy relative to Fermi sea is what matters.

    print(f"BCS converged: Delta = {Delta_bcs:.8f}, mu = {mu_bcs:.8f}")
    print(f"  N_pair (check) = {np.sum(v_sq_bcs):.6f}")
    print(f"  E_BCS (grand canonical) = {E_bcs_raw:.10f} M_KK")
else:
    print("BCS COLLAPSED (Delta -> 0)")
    print("  This is expected for N_pair=1 on 192 levels — ultrasmall limit")
    print("  d/Delta >> 1 (Paper 17 regime)")

# =============================================================================
# Section 4b: Number-Projected BCS (PBCS) — exact for separable V at M=1
# =============================================================================
#
# For M=1 pair with separable V, PBCS gives the EXACT answer (Paper 15, Sec. IV).
# The PBCS wavefunction is |PBCS> = sum_j c_j A^dag_j |0>
# with c_j proportional to u_j*v_j from BCS (or directly from variational principle).
#
# For separable V_{jj'} = G * f_j * f_{j'}, the M=1 ground state is:
#   |psi> = sum_j (f_j / (2*eps_j - E)) A^dag_j |0>
# which is EXACTLY the Richardson solution. So PBCS = Richardson for M=1.
# This provides the self-consistency check.

print("\n" + "="*70)
print("PROJECTED BCS (M=1 equivalent)")
print("="*70)

# PBCS for M=1: minimize <psi|H|psi>/<psi|psi> over |psi> = sum c_j A^dag_j |0>
# H|psi> = sum_j 2*eps_j c_j A^dag_j |0> + G * (sum_j f_j c_j) * sum_k f_k A^dag_k |0>
# <psi|H|psi> = 2*sum_j eps_j |c_j|^2 + G * |sum_j f_j c_j|^2
# <psi|psi> = sum_j |c_j|^2
#
# This is a generalized eigenvalue problem in 1D:
# (2*diag(eps) + G * f*f^T) * c = E * c

H_pbcs = 2.0 * np.diag(eps) + G * np.outer(u_sorted, u_sorted)
# Lowest eigenvalue = exact M=1 pair energy
evals_pbcs, evecs_pbcs = eigh(H_pbcs)
E_pbcs = evals_pbcs[0]
c_pbcs = evecs_pbcs[:, 0]

print(f"PBCS (= exact for separable V at M=1):")
print(f"  E_PBCS = {E_pbcs:.10f} M_KK")
print(f"  Richardson E_alpha = {E_exact:.10f} M_KK")
print(f"  |E_PBCS - E_Richardson| = {abs(E_pbcs - E_exact):.2e} M_KK")

# Verify Richardson solution matches PBCS
pbcs_richardson_match = abs(E_pbcs - E_exact) < 1e-8
print(f"  PBCS-Richardson match: {'YES' if pbcs_richardson_match else 'NO'} "
      f"(tolerance 1e-8)")

# =============================================================================
# Section 5: BCS comparison — proper treatment for ultrasmall limit
# =============================================================================
#
# In the ultrasmall limit (d/Delta >> 1, Paper 17), BCS collapses but the
# exact solution does NOT. The proper comparison is:
#
# 1. Fermi sea energy: place 1 pair in the lowest level
#    E_FS = 2 * eps[0] (lowest single-particle energy, 2 particles)
#
# 2. First-order perturbation theory (PT1):
#    E_PT1 = 2*eps[0] + G*f[0]^2 (self-energy of pair in lowest level)
#
# 3. Second-order perturbation theory (PT2):
#    E_PT2 = E_PT1 + G^2 * sum_{j>0} f[0]^2 * f[j]^2 / (2*eps[0] - 2*eps[j])
#
# 4. Richardson exact: E_alpha from Section 3
#
# 5. BCS (if converged): from Section 4

print("\n" + "="*70)
print("ENERGY COMPARISON: Perturbative -> Exact")
print("="*70)

# Fermi sea: 1 pair in lowest level
E_FS = 2.0 * eps[0]
print(f"Fermi sea (1 pair in lowest level):")
print(f"  E_FS = 2 * eps[0] = {E_FS:.10f} M_KK")

# First-order PT
E_PT1 = E_FS + G * f_sq[0]
print(f"\nFirst-order perturbation theory:")
print(f"  E_PT1 = E_FS + G*f_0^2 = {E_PT1:.10f} M_KK")
print(f"  Shift = {E_PT1 - E_FS:.8f} M_KK")

# Second-order PT
E_PT2_shift = G**2 * np.sum(f_sq[0] * f_sq[1:] / (2*eps[0] - 2*eps[1:]))
E_PT2 = E_PT1 + E_PT2_shift
print(f"\nSecond-order perturbation theory:")
print(f"  E_PT2 = E_PT1 + sum G^2|<j|V|0>|^2/(E_0-E_j) = {E_PT2:.10f} M_KK")
print(f"  PT2 shift = {E_PT2_shift:.8f} M_KK")

# Exact Richardson
print(f"\nExact Richardson (M=1):")
print(f"  E_exact = {E_exact:.10f} M_KK")

# Condensation energy relative to Fermi sea
E_cond_exact = E_exact - E_FS
E_cond_PT1 = E_PT1 - E_FS
E_cond_PT2 = E_PT2 - E_FS
print(f"\nCondensation energies (E - E_FS):")
print(f"  PT1:   {E_cond_PT1:.10f} M_KK ({E_cond_PT1/E_cond_exact*100:.2f}% of exact)")
print(f"  PT2:   {E_cond_PT2:.10f} M_KK ({E_cond_PT2/E_cond_exact*100:.2f}% of exact)")
print(f"  Exact: {E_cond_exact:.10f} M_KK")

# Correlation energy: E_exact - E_PT1 (beyond mean-field)
E_corr = E_exact - E_PT1
print(f"\nCorrelation energy (E_exact - E_PT1):")
print(f"  E_corr = {E_corr:.10f} M_KK")
print(f"  E_corr/E_cond = {E_corr/E_cond_exact:.4f}")

# =============================================================================
# Section 5b: Full-V exact diagonalization at M=1 for comparison
# =============================================================================
#
# The above uses the rank-1 separable approximation. For the FULL V_bare
# (non-separable), ED at M=1 is trivial: just diagonalize the 192x192
# pair Hamiltonian h_pair = 2*diag(eps) + V_fabric.
#
# V_fabric in the Bloch basis: for local (same-cell) pairing,
# V_{(k,n),(k',n')} = V_bare[k,k'] * (1/N_cells) * sum_i evecs[i,n]*evecs[i,n']
# where the sum over cells gives delta_{n,n'} for orthonormal evecs.
# So V_fabric = V_bare (x) I_{N_cells} / N_cells ... wait, that's not right.
#
# Actually: in the Bloch basis, local pairing gives
# V_{(k,n),(k',n')} = (1/N_cells) * V_bare[k,k'] for ALL n,n'
# because the pair operator sum_i A^dag_{ik} A_{ik'} in momentum space
# gives (1/N) * sum_{n,n'} ... No, let me be careful.
#
# A^dag_{ik} creates a pair on cell i, mode k. In Bloch basis:
# c_{kn} = (1/sqrt(N)) * sum_i evecs[i,n] * c_{ik}
# A^dag_{kn} = c^dag_{kn,up} c^dag_{kn,down} = (1/N) sum_{ij} evecs[i,n]*evecs[j,n] c^dag_{ik,up} c^dag_{jk,down}
#
# For LOCAL pairing (same-cell only):
# H_pair = sum_i sum_{kk'} V[k,k'] A^dag_{ik} A_{ik'}
#        = sum_{kk'} V[k,k'] sum_i A^dag_{ik} A_{ik'}
#
# In Bloch basis, sum_i A^dag_{ik} A_{ik'} = sum_{nn'} (1/N) * A^dag_{kn} A_{k'n'}
# ... no, this overcounts.
#
# Correctly: c_{ik} = (1/sqrt(N)) sum_n evecs[i,n] c_{kn}
# A^dag_{ik} = (1/N) sum_{nn'} evecs[i,n] evecs[i,n'] c^dag_{kn} c^dag_{kn'}  ... no.
# A^dag_{ik} creates a PAIR (up,down) at (cell i, mode k).
# A^dag_{ik} = c^dag_{ik,up} c^dag_{ik,down}
#
# Transform: c^dag_{ik,s} = (1/sqrt(N)) sum_n evecs[i,n] c^dag_{kn,s}
# A^dag_{ik} = (1/N) sum_{nn'} evecs[i,n] evecs[i,n'] c^dag_{kn,up} c^dag_{kn',down}
#
# H_pair = sum_i sum_{kk'} V[k,k'] * (1/N^2) sum_{n1 n2 m1 m2} evecs[i,n1]*evecs[i,n2]*evecs[i,m1]*evecs[i,m2]
#          * c^dag_{kn1,up} c^dag_{kn2,down} c_{k'm2,down} c_{k'm1,up}
#
# This is getting complicated. For the M=1 sector, we can simplify:
# State = sum_{k,n} psi_{kn} A^dag_{kn} |0>, where A^dag_{kn} = c^dag_{kn,up} c^dag_{kn,down}
# BUT: the pair can be (kn,up; k'n',down) with k!=k' or n!=n'. This is the general case.
#
# For SEPARABLE V (rank-1), the Bloch transform is clean and gives exactly
# what we computed above. For the full V, we need the matrix element:
# <kn, k'n' | H | k''m, k'''m'> which is the full 2-particle matrix.
#
# SIMPLIFICATION: Since the pairing interaction is LOCAL (same-cell),
# and Josephson is SINGLE-PARTICLE, the M=1 pair Hamiltonian in the
# (k,n) basis where n labels CG(24) eigenvalues is:
#
# H_pair_{(kn),(k'n')} = (eps_k + E_J*lambda_n + eps_k' + E_J*lambda_n') * delta_{kn,k'n'}
#                        + V_eff[k,k';n,n']
#
# where V_eff encodes the local pairing projected onto Bloch states.
#
# For the PAIR sector (paired fermions, both in same (k,n)):
# The pair lives on level j = (k,n) with energy 2*eps_j.
# The pairing scatters pair from level j to level j'.
# For local pairing in real space -> uniform scattering in momentum space:
# V_{(k,n),(k',n')} = V_bare[k,k'] / N_cells   (momentum conservation relaxed by locality)
#
# This is the correct formula for s-wave pairing projected onto Bloch states
# of a finite system where the interaction is on-site.

print("\n" + "="*70)
print("FULL-V EXACT DIAGONALIZATION (M=1)")
print("="*70)

# Build the L x L pair Hamiltonian (L = 192)
# H_{jj'} = 2*eps_j * delta_{jj'} + V_pair_{jj'}
# where V_pair_{jj'} = V_bare[mode_j, mode_j'] / N_cells

H_full = np.zeros((L_total, L_total))
for j in range(L_total):
    H_full[j, j] = 2.0 * eps_sorted[j]
    for jp in range(L_total):
        kj = mode_sorted[j]
        kjp = mode_sorted[jp]
        H_full[j, jp] += V_bare[kj, kjp] / N_cells

evals_full, evecs_full = eigh(H_full)
E_full_exact = evals_full[0]
psi_full = evecs_full[:, 0]

print(f"Full-V ED (M=1 on CG(24)):")
print(f"  E_full = {E_full_exact:.10f} M_KK")
print(f"  E_separable (Richardson) = {E_exact:.10f} M_KK")
print(f"  Difference = {E_full_exact - E_exact:.8f} M_KK")
print(f"  Relative = {abs(E_full_exact - E_exact)/abs(E_full_exact)*100:.4f}%")

# Participation ratio for full solution
n_full = psi_full**2
PR_full = 1.0 / np.sum(n_full**2)
print(f"  PR (full) = {PR_full:.2f}")
print(f"  PR (separable) = {1.0/np.sum(n_exact**2):.2f}")

# Mode decomposition of full solution
print(f"\nMode decomposition of pair wavefunction:")
for k in range(N_modes):
    mask = (mode_sorted == k)
    w_sep = np.sum(n_exact[mask])
    w_full = np.sum(n_full[mask])
    print(f"  {labels[k]:>6s}: separable={w_sep:.6f}  full-V={w_full:.6f}")

# =============================================================================
# Section 6: Comparison to single-cell Richardson (S52 benchmark)
# =============================================================================

print("\n" + "="*70)
print("SINGLE-CELL vs FABRIC COMPARISON")
print("="*70)

# S52 had N=1 on single cell (8 modes):
# E_ed = 1.4398, E_pbcs = 1.4539, E_hfb = 1.4264
E_1cell_ed = float(hfb_data['N1_E_ed'])   # 1.440 (8-mode ED)
E_1cell_pbcs = float(hfb_data['N1_E_pbcs'])

print(f"Single cell (S52):")
print(f"  E_ED = {E_1cell_ed:.6f} M_KK (8-mode full ED)")
print(f"  E_PBCS = {E_1cell_pbcs:.6f} M_KK")
print(f"\nFabric CG(24) (this computation):")
print(f"  E_Richardson (separable, 192 levels) = {E_exact:.6f} M_KK")
print(f"  E_full_ED (full V, 192 levels) = {E_full_exact:.6f} M_KK")
print(f"  E_Fermi_sea = {E_FS:.6f} M_KK")

# The fabric pair energy should be LOWER than single-cell because the pair
# can delocalize across cells via Josephson coupling
print(f"\nPair delocalization:")
print(f"  E_fabric - E_1cell = {E_full_exact - E_1cell_ed:.6f} M_KK")
print(f"  This is {'LOWER (delocalized)' if E_full_exact < E_1cell_ed else 'HIGHER (localized)'}")

# Mean level spacing
d_fabric = (eps_sorted[-1] - eps_sorted[0]) / (L_total - 1)
d_1cell = (eps_bare[-1] - eps_bare[0]) / (N_modes - 1)
print(f"\nLevel spacings:")
print(f"  d (fabric) = {d_fabric:.6f} M_KK")
print(f"  d (single cell) = {d_1cell:.6f} M_KK")
print(f"  d/Delta_OES (fabric) = {d_fabric/Delta_0_OES:.2f}")
print(f"  d/Delta_OES (single cell) = {d_1cell/Delta_0_OES:.2f}")

# =============================================================================
# Section 7: GGE occupation comparison
# =============================================================================

print("\n" + "="*70)
print("GGE OCCUPATION COMPARISON")
print("="*70)

# The GGE occupations (from S62) are per-mode averages.
# The Richardson exact solution gives n_j for the pair.
# For M=1 pair on 192 levels, the occupation of level j is |c_j|^2.
# Summed over CG(24) cells, this gives the mode-resolved occupation.

print("Mode occupations (pair fraction by mode type):")
print(f"{'Mode':>8s} {'Richardson':>12s} {'Full-ED':>12s} {'GGE':>12s} {'GS(S62)':>12s}")

n_k_rich = np.zeros(N_modes)
n_k_full = np.zeros(N_modes)

for k in range(N_modes):
    mask = (mode_sorted == k)
    n_k_rich[k] = np.sum(n_exact[mask])
    n_k_full[k] = np.sum(n_full[mask])
    print(f"{labels[k]:>8s} {n_k_rich[k]:12.6f} {n_k_full[k]:12.6f} "
          f"{n_k_GGE[k]:12.6f} {float(gge_data['n_k_GS'][k]):12.6f}")

# =============================================================================
# Section 8: Electrostatic mapping (Paper 15, Sec. III)
# =============================================================================

print("\n" + "="*70)
print("ELECTROSTATIC MAPPING")
print("="*70)

# For M=1, the pair energy E_alpha is a single charge on the real line
# (since M=1, no pair-pair repulsion forces complex E).
# The "orbitons" are at positions 2*eps_j with charges f_j^2.
# The external field is e = 1/G.
# Equilibrium condition: e = sum_j q_j / (z_alpha - z_j)
#   i.e. 1/G = sum_j f_j^2 / (E_alpha - 2*eps_j)

# Check electrostatic equilibrium
es_lhs = 1.0 / G
es_rhs = np.sum(f_sq / (E_exact - 2.0 * eps))
print(f"Electrostatic check: 1/G = {es_lhs:.10f}")
print(f"  sum f_j^2/(E - 2*eps_j) = {es_rhs:.10f}")
print(f"  Residual = {abs(es_lhs - es_rhs):.2e}")

# Position of pair energy relative to orbitons
print(f"\nPair energy E_alpha = {E_exact:.6f} sits {'below' if E_exact < 2*eps[0] else 'between'} "
      f"the orbiton spectrum [{2*eps[0]:.4f}, {2*eps[-1]:.4f}]")

# =============================================================================
# Section 9: BCS accuracy assessment and d/Delta diagnostic
# =============================================================================

print("\n" + "="*70)
print("BCS ACCURACY AND ULTRASMALL DIAGNOSTICS")
print("="*70)

# Key diagnostic: d/Delta ratio (Paper 17)
# d = mean level spacing near Fermi surface
# Delta = pairing gap

# Compute effective d near the Fermi surface (where the pair lives)
# Use levels within 1 Delta of the pair energy
Delta_eff = abs(E_cond_exact)  # use condensation energy as scale
levels_near_FS = eps[eps < eps[0] + 2*Delta_eff]
if len(levels_near_FS) > 1:
    d_near_FS = np.mean(np.diff(levels_near_FS))
else:
    d_near_FS = d_fabric

print(f"Ultrasmall diagnostics (Paper 17, von Delft-Ralph):")
print(f"  Mean level spacing d = {d_fabric:.6f} M_KK")
print(f"  d near Fermi surface = {d_near_FS:.6f} M_KK")
print(f"  BCS gap Delta_OES = {Delta_0_OES:.6f} M_KK")
print(f"  Condensation energy |E_cond| = {abs(E_cond_exact):.6f} M_KK")
print(f"  d/Delta_OES = {d_fabric/Delta_0_OES:.2f}")
print(f"  d_FS/Delta_OES = {d_near_FS/Delta_0_OES:.2f}")

# Anderson criterion: BCS valid when d/Delta < 1
if d_fabric / Delta_0_OES > 1:
    print(f"  => ULTRASMALL regime: d/Delta = {d_fabric/Delta_0_OES:.1f} > 1")
    print(f"     BCS mean-field NOT reliable (Paper 17)")
    print(f"     Richardson exact solution IS the correct benchmark")
else:
    print(f"  => BCS regime: d/Delta = {d_fabric/Delta_0_OES:.2f} < 1")
    print(f"     BCS mean-field should be accurate")

# BCS vs exact ratio
if not bcs_collapsed:
    ratio_bcs = E_exact / best_E_bcs
    print(f"\n  E_exact/E_BCS = {ratio_bcs:.6f}")
    print(f"  Correlation energy (E_exact - E_BCS)/E_exact = "
          f"{(E_exact - best_E_bcs)/abs(E_exact)*100:.2f}%")
else:
    print(f"\n  BCS collapsed: using perturbative comparison instead")
    ratio_pt2 = E_exact / E_PT2
    print(f"  E_exact/E_PT2 = {ratio_pt2:.6f}")
    accuracy_pt2 = abs(E_exact - E_PT2) / abs(E_exact) * 100
    print(f"  PT2 accuracy = {accuracy_pt2:.4f}%")

# Richardson vs single-cell accuracy
ratio_rich_1cell = E_exact / E_1cell_ed
print(f"\n  E_Richardson(fabric)/E_ED(1cell) = {ratio_rich_1cell:.6f}")

# =============================================================================
# Section 10: Save results
# =============================================================================

print("\n" + "="*70)
print("SAVING RESULTS")
print("="*70)

output_file = 'computations/session-63/s63_richardson_gaudin_n1.npz'

results = {
    # Gate
    'gate_name': 'RICHARDSON-GAUDIN-N1-63',
    'gate_verdict': 'INFO',

    # System parameters
    'N_cells': N_cells,
    'N_modes': N_modes,
    'L_total': L_total,
    'N_pair': 1,
    'E_J': E_J,
    'g_eff': g_eff,
    'rank1_frac': rank1_frac,

    # Spectrum
    'eps_sorted': eps_sorted,
    'mode_sorted': mode_sorted,
    'cell_sorted': cell_sorted,
    'evals_adj': evals_adj,
    'd_fabric': d_fabric,
    'd_1cell': d_1cell,

    # Richardson exact
    'E_exact_richardson': E_exact,
    'E_exact_full_ED': E_full_exact,
    'n_exact_richardson': n_exact,
    'n_exact_full': n_full,
    'PR_richardson': 1.0 / np.sum(n_exact**2),
    'PR_full': PR_full,
    'all_richardson_roots': roots,

    # Perturbative
    'E_FS': E_FS,
    'E_PT1': E_PT1,
    'E_PT2': E_PT2,

    # BCS
    'bcs_collapsed': bcs_collapsed,
    'Delta_bcs': best_Delta if not bcs_collapsed else 0.0,
    'mu_bcs': best_mu if not bcs_collapsed else 0.0,
    'E_bcs': best_E_bcs if not bcs_collapsed else np.inf,

    # PBCS verification
    'E_pbcs': E_pbcs,
    'pbcs_richardson_match': pbcs_richardson_match,

    # Condensation
    'E_cond_exact': E_cond_exact,
    'E_cond_PT1': E_cond_PT1,
    'E_cond_PT2': E_cond_PT2,
    'E_corr': E_corr,

    # Diagnostics
    'd_over_Delta': d_fabric / Delta_0_OES,

    # Mode decomposition
    'n_k_richardson': n_k_rich,
    'n_k_full': n_k_full,
    'n_k_GGE': n_k_GGE,
    'labels': labels,

    # Single-cell comparison
    'E_1cell_ed': E_1cell_ed,
    'E_1cell_pbcs': E_1cell_pbcs,

    # Electrostatic
    'es_residual': abs(es_lhs - es_rhs),
}

# Build gate detail string
if not bcs_collapsed:
    detail = (f"E_rich={E_exact:.6f}, E_full={E_full_exact:.6f}, "
              f"E_BCS={best_E_bcs:.6f}, ratio={E_exact/best_E_bcs:.6f}, "
              f"E_corr={E_corr:.6f}, d/Delta={d_fabric/Delta_0_OES:.2f}")
else:
    detail = (f"E_rich={E_exact:.6f}, E_full={E_full_exact:.6f}, "
              f"BCS_collapsed, E_corr={E_corr:.6f}, "
              f"d/Delta={d_fabric/Delta_0_OES:.2f}, "
              f"PT2_accuracy={abs(E_exact-E_PT2)/abs(E_exact)*100:.4f}%")

results['gate_detail'] = detail
np.savez(output_file, **results)
print(f"Saved to {output_file}")
print(f"Gate detail: {detail}")

# =============================================================================
# Section 11: Summary
# =============================================================================

print("\n" + "="*70)
print("SUMMARY: RICHARDSON-GAUDIN-N1-63")
print("="*70)
print(f"System: {N_cells} cells (CG(24)) x {N_modes} modes = {L_total} levels")
print(f"N_pair = 1, E_J = {E_J:.4f} M_KK, G = {g_eff:.4f} M_KK")
print(f"")
print(f"Exact pair energy (Richardson): {E_exact:.8f} M_KK")
print(f"Exact pair energy (full-V ED):  {E_full_exact:.8f} M_KK")
print(f"Separable vs full: {abs(E_exact-E_full_exact)/abs(E_full_exact)*100:.4f}%")
print(f"Fermi sea energy:               {E_FS:.8f} M_KK")
print(f"Condensation energy:            {E_cond_exact:.8f} M_KK")
print(f"d/Delta = {d_fabric/Delta_0_OES:.2f} ({'ultrasmall' if d_fabric/Delta_0_OES > 1 else 'BCS regime'})")
print(f"")
print(f"PBCS = Richardson match: {pbcs_richardson_match} (residual {abs(E_pbcs-E_exact):.2e})")
print(f"Electrostatic residual: {abs(es_lhs - es_rhs):.2e}")
print(f"Richardson roots: {len(roots)} found ({n_between} between poles)")
print(f"PR (separable) = {1.0/np.sum(n_exact**2):.2f}")
print(f"PR (full) = {PR_full:.2f}")
print(f"")
if not bcs_collapsed:
    print(f"BCS: Delta = {best_Delta:.6f}, E = {best_E_bcs:.6f}")
    print(f"E_exact/E_BCS = {E_exact/best_E_bcs:.6f}")
    print(f"BCS accuracy = {abs(E_exact-best_E_bcs)/abs(E_exact)*100:.4f}%")
else:
    print(f"BCS COLLAPSED (Delta -> 0, ultrasmall limit)")
    print(f"PT2 accuracy = {abs(E_exact-E_PT2)/abs(E_exact)*100:.4f}%")
print(f"")
print(f"GATE: RICHARDSON-GAUDIN-N1-63 = INFO")
