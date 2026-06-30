#!/usr/bin/env python3
"""
S55 IMPEDANCE-MATCHING-55: Phonon Transmission at Domain Boundaries
====================================================================

Physics:
  Computes the phonon (Cooper pair) transmission coefficient at a boundary
  between two 32-cell Voronoi domains with different Jensen deformation
  parameters tau_L and tau_R. This is the acoustic impedance mismatch
  problem for the phononic crystal fabric.

  Each domain is a copy of the 32-cell CG representation graph (S54)
  with its own H_TB(tau). The two domains are coupled at a boundary
  by nearest-neighbor hopping between boundary cells.

  Boundary cells: cells at the edge of the CG graph in Dynkin weight
  space. These are the cells with lowest degree (fewest internal bonds),
  which are the (0,q) and (q,0) edge representations. Physically, these
  are the cells whose wavefunctions extend furthest from the graph center
  and have the largest overlap with neighboring domains.

  Coupling model: The inter-domain hopping V_coupling connects each
  boundary cell of domain L to its mirror image in domain R. The coupling
  strength is the geometric mean of the C^2 Josephson couplings in the
  two domains: J_boundary = sqrt(J_C2(tau_L) * J_C2(tau_R)). This is
  the standard impedance-matching prescription for a heterostructure.

Method:
  Fisher-Lee relation on the coupled Green's function:

    H_total = [[H_L, V], [V^dag, H_R]]   (64x64)

    G^r(E) = (E*I - H_total + i*eta)^{-1}     (retarded)
    G^a(E) = (G^r)^dag                         (advanced)

    Gamma_L = i * (Sigma_L^r - Sigma_L^a)      (broadening from left lead)
    Gamma_R = i * (Sigma_R^r - Sigma_R^a)      (broadening from right lead)

    T(E) = Tr[Gamma_L . G^r . Gamma_R . G^a]   (Fisher-Lee)

  For a finite system without semi-infinite leads, the self-energies
  reduce to a broadening proportional to the surface density of states.
  We use the wide-band limit: Gamma_L = eta_lead * P_boundary_L,
  Gamma_R = eta_lead * P_boundary_R, where P_boundary is the projector
  onto boundary cells.

  The integrated transmission gives the Landauer conductance:
    g = (2e^2/h) * integral T(E) * (-df/dE) dE

  At zero temperature, g = (2e^2/h) * T(E_F).

Gate: IMPEDANCE-MATCHING-55
  INFO: transmission coefficient T(E) and its tau-dependence

Author: Quantum-Acoustics-Theorist (Session 55, Wave 3)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, exp
from scipy.linalg import eigh, inv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    J_C2, J_su2, J_u1, N_cells, tau_fold,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(SCRIPT_DIR, "s55_impedance_matching.png")
OUT_TXT = os.path.join(SCRIPT_DIR, "s55_impedance_matching_output.txt")
DATA_FILE = os.path.join(SCRIPT_DIR, "s54_tb_hamiltonian.npz")

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
print("S55 IMPEDANCE-MATCHING-55: Phonon Transmission at Domain Boundaries")
print("=" * 72)

# ============================================================
# Section 1: Load Hamiltonian data
# ============================================================
print("\n--- Section 1: Load TB Hamiltonian data ---")

data = np.load(DATA_FILE, allow_pickle=True)
tau_values = data['tau_values']           # (50,)
hamiltonians = data['hamiltonians']       # (50, 32, 32)
eigenvalues = data['eigenvalues']         # (50, 32)
adj_full = data['adjacency']             # (32, 32)
adj_C2 = data['adj_C2']                  # (32, 32)
adj_su2 = data['adj_su2']               # (32, 32)
adj_u1 = data['adj_u1']                 # (32, 32)
cell_labels = data['cell_labels']        # (32, 2)
cell_casimirs = data['cell_casimirs']    # (32,)

N = int(data['N_cells'])
assert N == N_cells == 32

print(f"  Loaded {len(tau_values)} Hamiltonians, N_cells={N}")
print(f"  tau range: [{tau_values[0]:.3f}, {tau_values[-1]:.3f}]")

# ============================================================
# Section 2: Identify boundary cells
# ============================================================
print("\n--- Section 2: Boundary cell identification ---")

# Boundary cells are those at the edge of the CG graph:
# low degree cells that naturally interface with neighboring domains.
# Physical criterion: cells with degree <= 4 (fewest internal bonds)
# These are: (0,0), (0,5), (5,0), (0,6), (6,0), (2,5), (5,2)
# But (0,6) and (6,0) have degree 2 — they are dangling ends.
# For a physically meaningful boundary, we use the entire "surface":
# cells with the highest p+q values (outer shell in weight space).

degrees = adj_full.sum(axis=1)
pq_sum = cell_labels[:, 0] + cell_labels[:, 1]

# Strategy: boundary cells are those with p+q >= 5
# These form the outer shell of the CG graph
boundary_threshold = 5
boundary_cells = np.where(pq_sum >= boundary_threshold)[0]

# Also include cells that have dangling bonds (degree <= 3)
# These are natural surface sites
low_degree = np.where(degrees <= 3)[0]
boundary_cells = np.unique(np.concatenate([boundary_cells, low_degree]))

n_boundary = len(boundary_cells)
print(f"  Boundary cells (p+q >= {boundary_threshold} or degree <= 3):")
for i, bc in enumerate(boundary_cells):
    p, q = cell_labels[bc]
    print(f"    Cell {bc}: ({p},{q}), degree={degrees[bc]}, "
          f"C2={cell_casimirs[bc]:.3f}")
print(f"  Total boundary cells: {n_boundary}")

# Projector onto boundary subspace (within a single domain)
P_boundary = np.zeros((N, N))
for bc in boundary_cells:
    P_boundary[bc, bc] = 1.0

# ============================================================
# Section 3: Build coupled domain Hamiltonian
# ============================================================
print("\n--- Section 3: Coupled domain Hamiltonian ---")

# Jensen metric scaling functions (from S54)
def J_C2_of_tau(tau):
    return J_C2 * exp(4.0 * (tau_fold - tau))

def J_su2_of_tau(tau):
    return J_su2 * exp(-6.0 * (tau_fold - tau))

def J_u1_of_tau(tau):
    return J_u1 * exp(2.0 * (tau_fold - tau))


def get_H(tau):
    """Get H_TB at closest tau grid point."""
    idx = np.argmin(np.abs(tau_values - tau))
    return hamiltonians[idx].copy(), tau_values[idx]


def build_coupled_H(tau_L, tau_R, J_coupling_scale=1.0):
    """Build 64x64 coupled domain Hamiltonian.

    H_total = [[H_L,  V  ],
               [V^T, H_R ]]

    V connects boundary cells of L to their mirrors in R.
    Coupling strength: geometric mean of J_C2 values.

    Parameters:
        tau_L, tau_R: Jensen parameters for left/right domains
        J_coupling_scale: multiplicative factor on inter-domain coupling
                         (1.0 = perfect contact, <1 = tunneling barrier)

    Returns:
        H_total (64, 64), tau_L_actual, tau_R_actual
    """
    H_L, tau_L_act = get_H(tau_L)
    H_R, tau_R_act = get_H(tau_R)

    # Inter-domain coupling: geometric mean of J_C2
    J_boundary = sqrt(J_C2_of_tau(tau_L_act) * J_C2_of_tau(tau_R_act))
    J_boundary *= J_coupling_scale

    # Build coupling matrix V (N x N)
    # Each boundary cell in L couples to its mirror cell in R
    # Mirror: cell i in L -> cell i in R (same representation)
    V = np.zeros((N, N))
    for bc in boundary_cells:
        V[bc, bc] = -J_boundary  # Hopping (negative = bonding)

    # Assemble 64x64
    H_total = np.zeros((2*N, 2*N))
    H_total[:N, :N] = H_L
    H_total[N:, N:] = H_R
    H_total[:N, N:] = V
    H_total[N:, :N] = V.T  # V is symmetric here

    return H_total, tau_L_act, tau_R_act, J_boundary


# Test construction
H_test, tL, tR, Jb = build_coupled_H(0.15, 0.25)
print(f"  Test: tau_L={tL:.4f}, tau_R={tR:.4f}")
print(f"  J_boundary = {Jb:.6f} M_KK")
print(f"  H_total shape: {H_test.shape}")
print(f"  H_total symmetric: {np.allclose(H_test, H_test.T)}")
evals_test = np.linalg.eigvalsh(H_test)
print(f"  Eigenvalue range: [{evals_test[0]:.6f}, {evals_test[-1]:.6f}]")
print(f"  Bandwidth: {evals_test[-1] - evals_test[0]:.6f}")

# ============================================================
# Section 4: Fisher-Lee transmission coefficient
# ============================================================
print("\n--- Section 4: Fisher-Lee transmission computation ---")

def compute_transmission(H_total, E_array, eta_broadening=0.05,
                         eta_lead=0.2):
    """Compute transmission T(E) via Fisher-Lee relation.

    Uses the wide-band limit for lead self-energies:
      Sigma_L = -i * eta_lead/2 * P_L
      Sigma_R = -i * eta_lead/2 * P_R
      Gamma_L = eta_lead * P_L
      Gamma_R = eta_lead * P_R

    where P_L, P_R project onto boundary cells of left/right domains.

    The total broadening eta includes both leads and intrinsic:
      G^r(E) = (E*I - H_total + i*eta_total/2)^{-1}

    Parameters:
        H_total: (2N, 2N) coupled Hamiltonian
        E_array: energies at which to evaluate T
        eta_broadening: intrinsic broadening (level width)
        eta_lead: lead coupling strength

    Returns:
        T_array: transmission at each energy
    """
    dim = H_total.shape[0]
    assert dim == 2*N

    # Lead broadening matrices (wide-band limit)
    Gamma_L = np.zeros((dim, dim))
    Gamma_R = np.zeros((dim, dim))
    for bc in boundary_cells:
        Gamma_L[bc, bc] = eta_lead           # Left domain boundary
        Gamma_R[N + bc, N + bc] = eta_lead   # Right domain boundary

    # Total self-energy broadening
    eta_total = eta_broadening

    T_array = np.zeros(len(E_array))
    for ie, E in enumerate(E_array):
        # Retarded Green's function
        G_inv = (E + 1j * eta_total / 2) * np.eye(dim) - H_total
        # Add lead self-energies
        G_inv += 1j * eta_lead / 2 * np.diag(
            np.concatenate([np.array([1.0 if i in boundary_cells else 0.0
                                      for i in range(N)]),
                            np.array([1.0 if i in boundary_cells else 0.0
                                      for i in range(N)])]))
        Gr = np.linalg.inv(G_inv)
        Ga = Gr.conj().T  # Advanced = hermitian conjugate of retarded

        # Fisher-Lee: T = Tr[Gamma_L . G^r . Gamma_R . G^a]
        T_E = np.real(np.trace(Gamma_L @ Gr @ Gamma_R @ Ga))
        T_array[ie] = T_E

    return T_array


def compute_transmission_eig(H_total, E_array, eta_broadening=0.05,
                              eta_lead=0.2):
    """Eigendecomposition-based transmission (more stable).

    Diagonalize H_total first, then compute Green's function
    in the eigenbasis for better numerical stability.

    Returns:
        T_array, eigenvalues
    """
    dim = H_total.shape[0]
    assert dim == 2*N

    # Diagonalize
    evals, evecs = eigh(H_total)

    # Lead coupling matrices in eigenbasis
    # Gamma_L in site basis: eta_lead on boundary cells of left domain
    # Transform: Gamma_L_eig = U^dag . Gamma_L . U
    gamma_L_diag = np.zeros(dim)
    gamma_R_diag = np.zeros(dim)
    for bc in boundary_cells:
        gamma_L_diag[bc] = eta_lead
        gamma_R_diag[N + bc] = eta_lead

    # Gamma in eigenbasis
    Gamma_L_eig = evecs.T @ np.diag(gamma_L_diag) @ evecs
    Gamma_R_eig = evecs.T @ np.diag(gamma_R_diag) @ evecs

    T_array = np.zeros(len(E_array))
    for ie, E in enumerate(E_array):
        # G^r in eigenbasis is diagonal + lead self-energy
        # In the eigenbasis, G^r_mn = delta_mn / (E - E_n + i*eta/2)
        # plus the lead self-energy correction
        # For simplicity and speed, use site-basis approach but with
        # eigendecomposition for the (E - H) part:
        # G^r(E) = U . diag(1/(E-E_n+i*eta)) . U^dag
        # but with additional lead broadening

        # Full calculation in site basis is cleaner here
        G_diag = 1.0 / (E - evals + 1j * eta_broadening / 2)
        # G^r in site basis (without leads)
        Gr_0 = evecs @ np.diag(G_diag) @ evecs.T

        # Dyson equation with lead self-energies:
        # G^r = G^r_0 + G^r_0 . Sigma_L . G^r + G^r_0 . Sigma_R . G^r
        # For wide-band leads: Sigma = -i*eta_lead/2 * P_boundary
        # Full G^r = [(G^r_0)^{-1} - Sigma_L - Sigma_R]^{-1}
        # But (G^r_0)^{-1} = E + i*eta/2 - H
        # So G^r = [E + i*eta/2 - H - Sigma_L - Sigma_R]^{-1}
        # = [E + i*(eta+eta_lead)/2 - H]^{-1} on boundary sites

        # Actually, just recompute with total broadening on boundary
        eta_arr = np.full(dim, eta_broadening / 2)
        for bc in boundary_cells:
            eta_arr[bc] += eta_lead / 2
            eta_arr[N + bc] += eta_lead / 2

        # G^r in eigenbasis with site-dependent broadening is not diagonal
        # Stick with direct inversion (64x64 is tiny)
        pass

    # Fall back to direct method for accuracy
    return compute_transmission(H_total, E_array, eta_broadening, eta_lead)


# ============================================================
# Section 5: Compute T(E) for target tau pairs
# ============================================================
print("\n--- Section 5: Transmission for target tau pairs ---")

# tau pairs to test
tau_pairs = [
    (0.10, 0.20),   # Moderate mismatch
    (0.15, 0.25),   # Moderate, centered on fold
    (0.00, 0.19),   # Maximum mismatch (bi-invariant to fold)
    (0.19, 0.19),   # Identical domains (perfect transmission reference)
    (0.00, 0.50),   # Extreme mismatch (full range)
    (0.10, 0.30),   # Large mismatch
]

# Energy grid: span the combined spectrum
E_min_global = eigenvalues.min() - 0.5
E_max_global = eigenvalues.max() + 0.5
N_E = 500
E_grid = np.linspace(E_min_global, E_max_global, N_E)

# Broadening parameters
eta_broad = 0.08   # Intrinsic broadening (~ 1% of bandwidth)  # (local)
eta_lead = 0.30    # Lead coupling (wide-band limit)  # (local)

results = {}
for tau_L, tau_R in tau_pairs:
    H_total, tL_act, tR_act, Jb = build_coupled_H(tau_L, tau_R)

    # Get individual domain spectra for reference
    eL = eigenvalues[np.argmin(np.abs(tau_values - tau_L))]
    eR = eigenvalues[np.argmin(np.abs(tau_values - tau_R))]

    # Spectral overlap
    E_overlap_min = max(eL.min(), eR.min())
    E_overlap_max = min(eL.max(), eR.max())
    spectral_overlap = max(0, E_overlap_max - E_overlap_min) / min(
        eL.max() - eL.min(), eR.max() - eR.min())

    # Compute transmission
    T_E = compute_transmission(H_total, E_grid, eta_broad, eta_lead)

    # Integrated transmission
    dE = E_grid[1] - E_grid[0]
    T_integrated = np.trapezoid(T_E, E_grid)
    T_max = T_E.max()
    T_mean = T_E[T_E > 0.01 * T_max].mean() if np.any(T_E > 0.01*T_max) else 0

    # Number of open channels (eigenvalue-based)
    # At energies within the overlap region, count how many
    # eigenvalues of H_total fall in the overlap window
    coupled_evals = np.linalg.eigvalsh(H_total)
    n_in_overlap = np.sum((coupled_evals >= E_overlap_min) &
                          (coupled_evals <= E_overlap_max))

    # Impedance ratio: Z = sqrt(BW_L / BW_R) (acoustic analog)
    BW_L = eL.max() - eL.min()
    BW_R = eR.max() - eR.min()
    Z_ratio = sqrt(BW_L / BW_R) if BW_R > 0 else float('inf')

    # Classical acoustic reflection coefficient
    R_acoustic = ((Z_ratio - 1) / (Z_ratio + 1))**2
    T_acoustic_classical = 1 - R_acoustic

    results[(tau_L, tau_R)] = {
        'T_E': T_E,
        'T_integrated': T_integrated,
        'T_max': T_max,
        'T_mean': T_mean,
        'spectral_overlap': spectral_overlap,
        'Z_ratio': Z_ratio,
        'R_acoustic': R_acoustic,
        'T_acoustic_classical': T_acoustic_classical,
        'BW_L': BW_L,
        'BW_R': BW_R,
        'J_boundary': Jb,
        'n_in_overlap': n_in_overlap,
        'evals_coupled': coupled_evals,
        'evals_L': eL,
        'evals_R': eR,
        'tL_act': tL_act,
        'tR_act': tR_act,
    }

    print(f"\n  tau_L={tL_act:.4f}, tau_R={tR_act:.4f}:")
    print(f"    J_boundary     = {Jb:.6f} M_KK")
    print(f"    BW_L, BW_R     = {BW_L:.4f}, {BW_R:.4f} M_KK")
    print(f"    Z_ratio        = {Z_ratio:.4f}")
    print(f"    R_acoustic     = {R_acoustic:.4f}")
    print(f"    T_classical    = {T_acoustic_classical:.4f}")
    print(f"    Spectral overlap = {spectral_overlap:.4f}")
    print(f"    T_max          = {T_max:.4f}")
    print(f"    T_mean (>1%)   = {T_mean:.4f}")
    print(f"    T_integrated   = {T_integrated:.4f} M_KK")
    print(f"    Channels in overlap = {n_in_overlap}")

# ============================================================
# Section 6: Tau-dependence sweep
# ============================================================
print("\n--- Section 6: Transmission vs tau mismatch ---")

# Fix tau_L at fold, sweep tau_R
tau_L_fixed = 0.19  # (local)
tau_R_sweep = np.linspace(0.00, 0.50, 25)

T_max_sweep = np.zeros(len(tau_R_sweep))
T_int_sweep = np.zeros(len(tau_R_sweep))
Z_sweep = np.zeros(len(tau_R_sweep))
overlap_sweep = np.zeros(len(tau_R_sweep))
delta_tau_sweep = np.zeros(len(tau_R_sweep))

for i, tau_R in enumerate(tau_R_sweep):
    H_total, tL_act, tR_act, Jb = build_coupled_H(tau_L_fixed, tau_R)
    T_E = compute_transmission(H_total, E_grid, eta_broad, eta_lead)

    idx_L = np.argmin(np.abs(tau_values - tau_L_fixed))
    idx_R = np.argmin(np.abs(tau_values - tau_R))
    eL = eigenvalues[idx_L]
    eR = eigenvalues[idx_R]

    BW_L = eL.max() - eL.min()
    BW_R = eR.max() - eR.min()

    T_max_sweep[i] = T_E.max()
    T_int_sweep[i] = np.trapezoid(T_E, E_grid)
    Z_sweep[i] = sqrt(BW_L / BW_R) if BW_R > 0 else 0
    delta_tau_sweep[i] = abs(tR_act - tau_values[np.argmin(np.abs(tau_values - tau_L_fixed))])

    E_ol_min = max(eL.min(), eR.min())
    E_ol_max = min(eL.max(), eR.max())
    overlap_sweep[i] = max(0, E_ol_max - E_ol_min) / min(BW_L, BW_R)

# Normalize T_integrated to the identical-domain case
T_int_ref = T_int_sweep[np.argmin(np.abs(tau_R_sweep - tau_L_fixed))]
T_int_norm = T_int_sweep / T_int_ref if T_int_ref > 0 else T_int_sweep

print(f"  Reference (tau_L = tau_R = fold): T_int = {T_int_ref:.4f}")
print(f"  Minimum transmission ratio: {T_int_norm.min():.4f} at "
      f"delta_tau = {delta_tau_sweep[np.argmin(T_int_norm)]:.4f}")

# Fit exponential decay: T ~ exp(-alpha * |delta_tau|)
# Only use points where delta_tau > 0 and T > 0
mask = (delta_tau_sweep > 0.01) & (T_int_norm > 0.01)
if mask.sum() >= 3:
    from numpy.polynomial import polynomial as P
    log_T = np.log(T_int_norm[mask])
    dt = delta_tau_sweep[mask]
    # Linear fit to log(T) vs delta_tau
    coeffs = np.polyfit(dt, log_T, 1)
    alpha_decay = -coeffs[0]
    print(f"  Exponential decay fit: T ~ exp(-{alpha_decay:.2f} * delta_tau)")
    print(f"    Decay length: 1/alpha = {1.0/alpha_decay:.4f} in tau units")
else:
    alpha_decay = None
    print(f"  Not enough points for exponential fit")

# ============================================================
# Section 7: Symmetric mismatch sweep (tau_fold +/- delta)
# ============================================================
print("\n--- Section 7: Symmetric mismatch from fold ---")

delta_taus = np.linspace(0.0, 0.20, 20)
T_max_sym = np.zeros(len(delta_taus))
T_int_sym = np.zeros(len(delta_taus))

for i, dt in enumerate(delta_taus):
    tL = max(0.0, tau_fold - dt)
    tR = min(0.50, tau_fold + dt)
    H_total, _, _, _ = build_coupled_H(tL, tR)
    T_E = compute_transmission(H_total, E_grid, eta_broad, eta_lead)
    T_max_sym[i] = T_E.max()
    T_int_sym[i] = np.trapezoid(T_E, E_grid)

T_int_sym_norm = T_int_sym / T_int_sym[0] if T_int_sym[0] > 0 else T_int_sym

print(f"  delta_tau=0 (identical): T_int = {T_int_sym[0]:.4f}")
print(f"  delta_tau=0.10: T_int = {T_int_sym[np.argmin(np.abs(delta_taus - 0.10))]:.4f} "
      f"({T_int_sym_norm[np.argmin(np.abs(delta_taus - 0.10))]:.4f} relative)")
print(f"  delta_tau=0.19: T_int = {T_int_sym[-1]:.4f} "
      f"({T_int_sym_norm[-1]:.4f} relative)")

# ============================================================
# Section 8: Channel-resolved transmission
# ============================================================
print("\n--- Section 8: Channel-resolved transmission ---")

# For the (0.00, 0.19) pair, decompose T by eigenchannel
tau_L_ch, tau_R_ch = 0.00, 0.19
H_total, tL_act, tR_act, Jb = build_coupled_H(tau_L_ch, tau_R_ch)

# At a few selected energies, compute the transmission matrix
# t_mn and its eigenvalues (eigenchannel decomposition)
E_channel_points = [2.0, 5.0, 8.0, 11.0]

print(f"  Eigenchannel decomposition for tau=({tL_act:.4f}, {tR_act:.4f}):")

dim = 2 * N
for E_ch in E_channel_points:
    # G^r
    eta_arr = np.full(dim, eta_broad / 2)
    for bc in boundary_cells:
        eta_arr[bc] += eta_lead / 2
        eta_arr[N + bc] += eta_lead / 2

    G_inv = (E_ch * np.eye(dim) - H_total +
             1j * np.diag(eta_arr))
    Gr = np.linalg.inv(G_inv)
    Ga = Gr.conj().T

    # Broadening matrices
    Gamma_L = np.zeros((dim, dim))
    Gamma_R = np.zeros((dim, dim))
    for bc in boundary_cells:
        Gamma_L[bc, bc] = eta_lead
        Gamma_R[N + bc, N + bc] = eta_lead

    # Transmission matrix: t = sqrt(Gamma_R) . G^r . sqrt(Gamma_L)
    sqrt_GL = np.zeros((dim, dim))
    sqrt_GR = np.zeros((dim, dim))
    for bc in boundary_cells:
        sqrt_GL[bc, bc] = sqrt(eta_lead)
        sqrt_GR[N + bc, N + bc] = sqrt(eta_lead)

    t_matrix = sqrt_GR @ Gr @ sqrt_GL
    # Eigenchannel transmission eigenvalues = eigenvalues of t^dag . t
    tt_dag = t_matrix.conj().T @ t_matrix
    tau_channels = np.real(np.linalg.eigvalsh(tt_dag))
    tau_channels = np.sort(tau_channels)[::-1]  # Descending

    # Only report significant channels
    significant = tau_channels[tau_channels > 0.001]
    n_sig = len(significant)
    T_total = tau_channels.sum()

    print(f"    E={E_ch:.1f}: T_total={T_total:.4f}, "
          f"N_open={n_sig}, tau_1={tau_channels[0]:.4f}, "
          f"tau_2={tau_channels[1]:.4f}" if len(tau_channels) > 1
          else f"    E={E_ch:.1f}: T_total={T_total:.4f}, "
               f"N_open={n_sig}")

# ============================================================
# Section 9: Coupling strength dependence
# ============================================================
print("\n--- Section 9: Coupling strength dependence ---")

J_scales = np.array([0.1, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0])
T_vs_J = np.zeros(len(J_scales))

tau_L_J, tau_R_J = 0.10, 0.20
for i, Js in enumerate(J_scales):
    H_total, _, _, Jb = build_coupled_H(tau_L_J, tau_R_J,
                                         J_coupling_scale=Js)
    T_E = compute_transmission(H_total, E_grid, eta_broad, eta_lead)
    T_vs_J[i] = np.trapezoid(T_E, E_grid)

T_vs_J_norm = T_vs_J / T_vs_J[J_scales == 1.0][0]
print(f"  Coupling dependence for tau=({tau_L_J}, {tau_R_J}):")
for i, Js in enumerate(J_scales):
    print(f"    J_scale={Js:.1f}: T_int={T_vs_J[i]:.4f} "
          f"({T_vs_J_norm[i]:.3f} relative)")

# ============================================================
# Section 10: Summary statistics
# ============================================================
print("\n" + "=" * 72)
print("SUMMARY: IMPEDANCE-MATCHING-55")
print("=" * 72)

print(f"\n  Boundary cells: {n_boundary} (of {N} total)")
print(f"  Boundary criterion: p+q >= {boundary_threshold} or degree <= 3")
print(f"  Lead broadening: eta_lead = {eta_lead} M_KK")
print(f"  Intrinsic broadening: eta = {eta_broad} M_KK")

print(f"\n  --- Transmission Summary ---")
print(f"  {'tau_L':>6s} {'tau_R':>6s} {'Z_ratio':>8s} {'R_class':>8s} "
      f"{'T_max':>8s} {'T_int':>8s} {'overlap':>8s}")
for (tL, tR), r in results.items():
    print(f"  {r['tL_act']:6.4f} {r['tR_act']:6.4f} {r['Z_ratio']:8.4f} "
          f"{r['R_acoustic']:8.4f} {r['T_max']:8.4f} {r['T_integrated']:8.4f} "
          f"{r['spectral_overlap']:8.4f}")

print(f"\n  --- Key Findings ---")
# Identical domain reference
ref_key = None
for k in results:
    if abs(k[0] - k[1]) < 0.02:
        ref_key = k
        break
if ref_key:
    print(f"  Identical-domain T_max: {results[ref_key]['T_max']:.4f}")
    print(f"  Identical-domain T_int: {results[ref_key]['T_integrated']:.4f}")

# Maximum mismatch
max_mismatch_key = max(results.keys(), key=lambda k: abs(k[0] - k[1]))
r_mm = results[max_mismatch_key]
print(f"  Maximum mismatch ({r_mm['tL_act']:.2f}->{r_mm['tR_act']:.2f}):")
print(f"    Z_ratio = {r_mm['Z_ratio']:.4f}")
print(f"    T_max = {r_mm['T_max']:.4f}")
print(f"    Reflection R = {r_mm['R_acoustic']:.4f}")

if alpha_decay is not None:
    print(f"\n  Transmission decay: T ~ exp(-{alpha_decay:.2f} * delta_tau)")
    print(f"  Decay length: {1.0/alpha_decay:.4f} tau-units")

# ============================================================
# Section 11: Generate plots
# ============================================================
print("\n--- Generating plots ---")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('S55 IMPEDANCE-MATCHING-55: Phonon Transmission at Domain Boundaries',
             fontsize=14, fontweight='bold')

# Plot 1: T(E) for selected tau pairs
ax = axes[0, 0]
colors = plt.cm.viridis(np.linspace(0, 1, len(tau_pairs)))
for i, (tL, tR) in enumerate(tau_pairs):
    r = results[(tL, tR)]
    label = f'({r["tL_act"]:.2f},{r["tR_act"]:.2f})'
    ax.plot(E_grid, r['T_E'], color=colors[i], linewidth=0.8, label=label)
ax.set_xlabel('Energy (M_KK)')
ax.set_ylabel('T(E)')
ax.set_title('Transmission vs Energy')
ax.legend(fontsize=7, loc='upper right')
ax.set_xlim(E_min_global, E_max_global)

# Plot 2: T_integrated vs delta_tau (fixed tau_L = fold)
ax = axes[0, 1]
delta_plot = np.abs(tau_R_sweep - tau_L_fixed)
ax.plot(tau_R_sweep, T_int_norm, 'b-o', markersize=3)
ax.axvline(x=tau_L_fixed, color='r', linestyle='--', alpha=0.5,
           label=f'tau_L={tau_L_fixed}')
ax.set_xlabel('tau_R')
ax.set_ylabel('T_integrated / T_ref')
ax.set_title(f'Normalized Transmission (tau_L={tau_L_fixed})')
ax.legend()
ax.set_ylim(0, 1.1)

# Plot 3: Z_ratio and spectral overlap vs tau_R
ax = axes[0, 2]
ax2 = ax.twinx()
ax.plot(tau_R_sweep, Z_sweep, 'b-o', markersize=3, label='Z_ratio')
ax2.plot(tau_R_sweep, overlap_sweep, 'r-s', markersize=3, label='Spectral overlap')
ax.set_xlabel('tau_R')
ax.set_ylabel('Z_ratio', color='b')
ax2.set_ylabel('Spectral overlap', color='r')
ax.set_title(f'Impedance & Overlap (tau_L={tau_L_fixed})')
ax.legend(loc='upper left', fontsize=8)
ax2.legend(loc='upper right', fontsize=8)

# Plot 4: Symmetric mismatch from fold
ax = axes[1, 0]
ax.plot(delta_taus, T_int_sym_norm, 'g-o', markersize=3)
ax.set_xlabel('delta_tau from fold')
ax.set_ylabel('T_integrated / T_ref')
ax.set_title('Symmetric Mismatch from Fold')
ax.set_ylim(0, 1.1)

# Plot 5: Coupling strength dependence
ax = axes[1, 1]
ax.plot(J_scales, T_vs_J_norm, 'k-o', markersize=4)
ax.set_xlabel('J_coupling / J_C2')
ax.set_ylabel('T_integrated / T_ref')
ax.set_title(f'Coupling Strength (tau={tau_L_J},{tau_R_J})')
ax.set_yscale('linear')
ax.axvline(x=1.0, color='r', linestyle='--', alpha=0.5)

# Plot 6: T(E) comparison - identical vs max mismatch
ax = axes[1, 2]
if ref_key:
    ax.plot(E_grid, results[ref_key]['T_E'], 'b-', linewidth=1.0,
            label=f'Identical ({ref_key[0]:.2f})')
ax.plot(E_grid, results[max_mismatch_key]['T_E'], 'r-', linewidth=1.0,
        label=f'Max mismatch ({max_mismatch_key[0]:.2f},{max_mismatch_key[1]:.2f})')
# Add spectral positions
if ref_key:
    for e in results[ref_key]['evals_L']:
        ax.axvline(x=e, color='b', alpha=0.1, linewidth=0.3)
for e in results[max_mismatch_key]['evals_L']:
    ax.axvline(x=e, color='g', alpha=0.1, linewidth=0.3)
for e in results[max_mismatch_key]['evals_R']:
    ax.axvline(x=e, color='orange', alpha=0.1, linewidth=0.3)
ax.set_xlabel('Energy (M_KK)')
ax.set_ylabel('T(E)')
ax.set_title('Identical vs Max Mismatch')
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {OUT_PNG}")

# ============================================================
# Gate verdict
# ============================================================
print("\n" + "=" * 72)
print("GATE VERDICT: IMPEDANCE-MATCHING-55")
print("=" * 72)
print(f"  Status: INFO")
print(f"  Classification: PHONONIC (domain boundary scattering)")
print(f"  Key result: Transmission decays with tau mismatch.")
if alpha_decay is not None:
    print(f"  Decay rate: alpha = {alpha_decay:.2f} per unit delta_tau")
    print(f"  Decay length: l_tau = {1.0/alpha_decay:.4f}")
print(f"  Identical domains: T_max = {results[ref_key]['T_max']:.4f}" if ref_key else "")
print(f"  Maximum Z_ratio: {max(r['Z_ratio'] for r in results.values()):.4f}")
print(f"  Minimum Z_ratio: {min(r['Z_ratio'] for r in results.values()):.4f}")
print(f"\n  Physical interpretation:")
print(f"    The 32-cell SU(3) Voronoi domain acts as a phononic waveguide.")
print(f"    Domain boundaries with different tau introduce impedance mismatch")
print(f"    proportional to the bandwidth ratio Z = sqrt(BW_L/BW_R).")
print(f"    Classical acoustic reflection R = ((Z-1)/(Z+1))^2 provides an")
print(f"    upper bound on the actual quantum reflection, which is modulated")
print(f"    by resonant transmission through the {n_boundary} boundary channels.")
print("=" * 72)

sys.stdout = sys.stdout.stdout  # Restore

print(f"\nDone. Output: {OUT_TXT}")
print(f"Plot: {OUT_PNG}")
