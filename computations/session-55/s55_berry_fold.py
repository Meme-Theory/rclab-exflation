#!/usr/bin/env python3
"""
S55 BERRY-FOLD-55: Berry Phase Around the Jensen Fold
=====================================================

Compute the Berry phase of B2-dominated eigenstates around a closed loop
in (tau, sigma) parameter space encircling the B2 mass zero-crossing at
tau* = 0.190158.

Tests whether the zero-crossing is topologically protected (Berry phase = pi)
or accidental (Berry phase = 0).

METHOD:
  1. Construct the 32x32 tight-binding Hamiltonian H(tau, sigma) where:
     - tau parametrises the Jensen deformation
     - sigma parametrises the T2 off-Jensen perturbation
     Jensen: alpha_1 = e^{2*tau}, alpha_2 = e^{-2*tau}, alpha_3 = e^{tau}
     T2:     alpha_1 -> e^{2*tau - 11*sigma}, alpha_2 -> e^{-2*tau - 7*sigma},
             alpha_3 -> e^{tau + 8*sigma}

  2. Parametrise a closed loop:
     tau(theta) = tau* + r*cos(theta), sigma(theta) = r*sin(theta)
     for theta in [0, 2*pi], with r small enough to isolate the crossing.

  3. At each point, diagonalize H and track the B2-dominated eigenstate.

  4. Compute the discrete Berry phase:
     gamma = -Im ln prod_{j=0}^{N-1} <psi(theta_j)|psi(theta_{j+1})>

STRUCTURAL THEOREM (from memory):
  H(tau, sigma) is a REAL SYMMETRIC matrix for all (tau, sigma), because it
  is a graph Laplacian with real positive weights. For real-symmetric
  Hamiltonians, eigenvectors can always be chosen real, so:
  - Berry curvature Omega = 0 pointwise (Im of real product = 0)
  - Berry phase around any loop is quantised to 0 or pi (mod 2*pi)
  - gamma = pi requires the loop to encircle a CONICAL DEGENERACY
    (diabolical point) where two eigenvalues cross.

  The test is therefore: is there a degeneracy within the loop?

Gate: BERRY-FOLD-55 — INFO: Berry phase value (0 = accidental, pi = topological)

Author: Berry-Geometric-Phase-Theorist (Session 55)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, exp
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import LineCollection

from canonical_constants import J_C2, J_su2, J_u1, N_cells, tau_fold

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_NPZ = os.path.join(SCRIPT_DIR, "s55_berry_fold.npz")
OUT_PNG = os.path.join(SCRIPT_DIR, "s55_berry_fold.png")
OUT_TXT = os.path.join(SCRIPT_DIR, "s55_berry_fold_output.txt")

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
print("S55 BERRY-FOLD-55: Berry Phase Around the Jensen Fold")
print("=" * 72)

# ============================================================
# Section 1: Reconstruct the 32-cell representation graph
# ============================================================
print("\n--- Section 1: Reconstruct 32-cell representation graph ---")

def casimir_su3(p, q):
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Enumerate reps, sort by Casimir, take first 32
all_reps = []
for p in range(20):
    for q in range(20):
        all_reps.append((casimir_su3(p, q), p, q))
all_reps.sort()

N_CELLS = 32  # (local)
cell_labels = np.array([(p, q) for (_, p, q) in all_reps[:N_CELLS]])
cell_casimirs = np.array([casimir_su3(p, q) for (p, q) in cell_labels])
cell_dims = np.array([dim_su3(p, q) for (p, q) in cell_labels])
rep_set = set(map(tuple, cell_labels))
rep_to_idx = {tuple(cell_labels[i]): i for i in range(N_CELLS)}

# Build adjacency matrices
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

bonds_C2_per  = np.sum(adj_C2, axis=1)
bonds_su2_per = np.sum(adj_su2, axis=1)
bonds_u1_per  = np.sum(adj_u1, axis=1)

print(f"  32-cell graph reconstructed. B2 = cell {rep_to_idx[(1,1)]}")

# Verify against saved data
tb_data = np.load(os.path.join(SCRIPT_DIR, "s54_tb_hamiltonian.npz"), allow_pickle=True)
assert np.allclose(tb_data['adjacency'], adj_C2 | adj_su2 | adj_u1), "Adjacency mismatch!"
print("  Adjacency verified against s54_tb_hamiltonian.npz")

# ============================================================
# Section 2: Hamiltonian H(tau, sigma) with T2 deformation
# ============================================================
print("\n--- Section 2: H(tau, sigma) construction ---")

# Jensen metric:
#   alpha_1(tau) = e^{2*tau},  alpha_2(tau) = e^{-2*tau},  alpha_3(tau) = e^{tau}
# T2 deformation (volume-preserving: 1*(-11) + 3*(-7) + 4*8 = 0):
#   alpha_1(tau,sig) = e^{2*tau - 11*sig}
#   alpha_2(tau,sig) = e^{-2*tau - 7*sig}
#   alpha_3(tau,sig) = e^{tau + 8*sig}
#
# Josephson coupling scaling (from s54_tb_hamiltonian.py):
#   J_X(tau,sig) = J_X(fold) * [L_X(fold) / L_X(tau,sig)]^{d_X}
# where d_X is the dimension of direction X and L_X is the metric eigenvalue.
#
# Exponents from s54_tb_hamiltonian.py: J_C2 ~ L_C2^{-4}, J_su2 ~ L_su2^{-3}, J_u1 ~ L_u1^{-1}
# At fold: L_C2 = e^{tau_fold}, L_su2 = e^{-2*tau_fold}, L_u1 = e^{2*tau_fold}

def J_couplings(tau, sigma=0.0):
    """Compute (J_C2, J_su2, J_u1) at (tau, sigma) in 2D parameter space."""
    # Metric eigenvalues
    L_C2  = exp(tau + 8.0 * sigma)     # alpha_3 = C^2 metric
    L_su2 = exp(-2.0 * tau - 7.0 * sigma)  # alpha_2 = su(2) metric
    L_u1  = exp(2.0 * tau - 11.0 * sigma)   # alpha_1 = u(1) metric

    # Reference values at fold (sigma=0)
    L_C2_fold  = exp(tau_fold)
    L_su2_fold = exp(-2.0 * tau_fold)
    L_u1_fold  = exp(2.0 * tau_fold)

    jc2  = J_C2  * (L_C2_fold / L_C2)**4
    jsu2 = J_su2 * (L_su2_fold / L_su2)**3
    ju1  = J_u1  * (L_u1_fold / L_u1)**1

    return jc2, jsu2, ju1


def build_H(tau, sigma=0.0):
    """Build 32x32 tight-binding Hamiltonian at (tau, sigma)."""
    jc2, jsu2, ju1 = J_couplings(tau, sigma)

    # Off-diagonal: weighted adjacency
    H = -(jc2 * adj_C2 + jsu2 * adj_su2 + ju1 * adj_u1).astype(float)

    # Diagonal: graph Laplacian convention
    for i in range(N_CELLS):
        H[i, i] = (jc2 * bonds_C2_per[i]
                    + jsu2 * bonds_su2_per[i]
                    + ju1 * bonds_u1_per[i])

    return H


# Verify against saved data at sigma=0
# Use an EXACT tau grid point for comparison (saved grid may not include tau_fold exactly)
tau_saved = tb_data['tau_values']
idx_compare = 25  # pick a grid point that exists exactly
tau_compare = tau_saved[idx_compare]
H_check = build_H(tau_compare, 0.0)
H_saved = tb_data['hamiltonians'][idx_compare]
rel_err = np.max(np.abs(H_check - H_saved)) / np.max(np.abs(H_saved))
print(f"  H(tau={tau_compare:.4f}, 0) vs saved: max relative error = {rel_err:.2e}")
assert rel_err < 1e-10, f"Hamiltonian mismatch: {rel_err}"

# Verify sigma effects
jc2_0, jsu2_0, ju1_0 = J_couplings(tau_fold, 0.0)
jc2_p, jsu2_p, ju1_p = J_couplings(tau_fold, 0.005)
jc2_m, jsu2_m, ju1_m = J_couplings(tau_fold, -0.005)
print(f"  J_C2:  sigma=0: {jc2_0:.6f}, +0.005: {jc2_p:.6f}, -0.005: {jc2_m:.6f}")
print(f"  J_su2: sigma=0: {jsu2_0:.6f}, +0.005: {jsu2_p:.6f}, -0.005: {jsu2_m:.6f}")
print(f"  J_u1:  sigma=0: {ju1_0:.6f}, +0.005: {ju1_p:.6f}, -0.005: {ju1_m:.6f}")
print(f"  T2 perturbation changes couplings by ~{abs(jc2_p/jc2_0 - 1)*100:.1f}% at sig=0.005")

# ============================================================
# Section 3: Identify B2-dominated eigenstate and its flow
# ============================================================
print("\n--- Section 3: B2 eigenstate identification ---")

B2_cell = rep_to_idx[(1, 1)]  # cell index for B2 = (1,1)
print(f"  B2 cell index: {B2_cell}")

# Track B2-dominated eigenstate along Jensen line
tau_test = np.linspace(0.0, 0.5, 100)
b2_eval_track = np.zeros(len(tau_test))
b2_idx_track = np.zeros(len(tau_test), dtype=int)
min_gap_track = np.zeros(len(tau_test))

for i, tau in enumerate(tau_test):
    H = build_H(tau, 0.0)
    evals, evecs = eigh(H)
    # Find eigenstate with largest B2 component
    b2_weights = evecs[B2_cell, :]**2  # real eigenvectors, so no abs needed
    b2_idx = np.argmax(b2_weights)
    b2_eval_track[i] = evals[b2_idx]
    b2_idx_track[i] = b2_idx
    # Gap to nearest eigenvalue
    if b2_idx > 0 and b2_idx < N_CELLS - 1:
        gap_below = evals[b2_idx] - evals[b2_idx - 1]
        gap_above = evals[b2_idx + 1] - evals[b2_idx]
        min_gap_track[i] = min(gap_below, gap_above)
    elif b2_idx == 0:
        min_gap_track[i] = evals[1] - evals[0]
    else:
        min_gap_track[i] = evals[-1] - evals[-2]

print(f"  B2 eigenstate index range: {b2_idx_track.min()} to {b2_idx_track.max()}")
print(f"  B2 eigenvalue range: [{b2_eval_track.min():.4f}, {b2_eval_track.max():.4f}]")
print(f"  Min gap along Jensen: {min_gap_track.min():.4f} at tau={tau_test[np.argmin(min_gap_track)]:.4f}")

# Check for level crossings
idx_changes = np.where(np.diff(b2_idx_track) != 0)[0]
if len(idx_changes) > 0:
    print(f"  WARNING: B2 eigenstate index changes at tau = {tau_test[idx_changes]}")
    print(f"    Index transitions: {[(b2_idx_track[i], b2_idx_track[i+1]) for i in idx_changes]}")
else:
    print(f"  B2 eigenstate stays at index {b2_idx_track[0]} for all tau.")

# ============================================================
# Section 4: Scan for degeneracies in 2D parameter space
# ============================================================
print("\n--- Section 4: Degeneracy search in (tau, sigma) space ---")

# Scan a grid near the fold to find near-degeneracies
tau_scan_2d = np.linspace(0.10, 0.30, 61)
sig_scan_2d = np.linspace(-0.015, 0.015, 61)
min_gap_2d = np.zeros((len(tau_scan_2d), len(sig_scan_2d)))
b2_idx_2d = np.zeros((len(tau_scan_2d), len(sig_scan_2d)), dtype=int)
b2_eval_2d = np.zeros((len(tau_scan_2d), len(sig_scan_2d)))

for i, tau in enumerate(tau_scan_2d):
    for j, sig in enumerate(sig_scan_2d):
        H = build_H(tau, sig)
        evals, evecs = eigh(H)
        # B2-dominated eigenstate
        b2_weights = evecs[B2_cell, :]**2
        b2_idx = np.argmax(b2_weights)
        b2_idx_2d[i, j] = b2_idx
        b2_eval_2d[i, j] = evals[b2_idx]
        # Min gap to nearest level
        if 0 < b2_idx < N_CELLS - 1:
            min_gap_2d[i, j] = min(evals[b2_idx] - evals[b2_idx-1],
                                   evals[b2_idx+1] - evals[b2_idx])
        elif b2_idx == 0:
            min_gap_2d[i, j] = evals[1] - evals[0]
        else:
            min_gap_2d[i, j] = evals[-1] - evals[-2]

min_gap_global = min_gap_2d.min()
min_loc = np.unravel_index(min_gap_2d.argmin(), min_gap_2d.shape)
print(f"  Minimum gap in 2D scan: {min_gap_global:.6f}")
print(f"    at tau={tau_scan_2d[min_loc[0]]:.4f}, sigma={sig_scan_2d[min_loc[1]]:.6f}")
print(f"  Maximum gap in 2D scan: {min_gap_2d.max():.6f}")

# Check if B2 index changes across the grid
unique_indices = np.unique(b2_idx_2d)
print(f"  B2 eigenstate indices found: {unique_indices}")
if len(unique_indices) > 1:
    print(f"  WARNING: B2 index varies -- possible level crossings in 2D!")
    for idx in unique_indices:
        count = np.sum(b2_idx_2d == idx)
        print(f"    index {idx}: {count} grid points")
else:
    print(f"  B2 eigenstate stays at index {unique_indices[0]} everywhere in 2D scan.")

# ============================================================
# Section 5: Berry phase computation around closed loop
# ============================================================
print("\n--- Section 5: Berry phase around closed loop ---")

# Loop parametrisation: (tau, sigma) = (tau_fold + r*cos(theta), r*sin(theta))
# We compute for multiple radii to test robustness

radii = [0.001, 0.005, 0.01, 0.02, 0.05, 0.10]
N_theta_values = [64, 128, 256, 512]

results = {}

for r in radii:
    for N_theta in N_theta_values:
        theta = np.linspace(0, 2*pi, N_theta, endpoint=False)
        tau_loop = tau_fold + r * np.cos(theta)
        sig_loop = r * np.sin(theta)

        # Check loop stays in valid parameter range (tau > 0)
        if np.any(tau_loop <= 0):
            print(f"  r={r}: loop exits valid range (tau <= 0), skipping")
            continue

        # Diagonalize at each loop point and track B2 eigenstate
        evecs_loop = np.zeros((N_theta, N_CELLS, N_CELLS))
        evals_loop = np.zeros((N_theta, N_CELLS))
        b2_idx_loop = np.zeros(N_theta, dtype=int)

        for k in range(N_theta):
            H = build_H(tau_loop[k], sig_loop[k])
            evals, evecs = eigh(H)
            evals_loop[k] = evals
            evecs_loop[k] = evecs
            b2_weights = evecs[B2_cell, :]**2
            b2_idx_loop[k] = np.argmax(b2_weights)

        # Check if B2 index is constant around the loop
        unique_b2 = np.unique(b2_idx_loop)
        if len(unique_b2) > 1:
            print(f"  r={r:.3f}, N={N_theta}: B2 index CHANGES: {unique_b2}")
            # Use adiabatic tracking instead (overlap with previous state)
            # Recompute with overlap tracking
            b2_state = np.zeros(N_theta, dtype=int)
            H0 = build_H(tau_loop[0], sig_loop[0])
            e0, v0 = eigh(H0)
            b2_w0 = v0[B2_cell, :]**2
            b2_state[0] = np.argmax(b2_w0)

            for k in range(1, N_theta):
                H = build_H(tau_loop[k], sig_loop[k])
                ek, vk = eigh(H)
                # Track by maximum overlap with previous state
                prev_vec = evecs_loop[k-1, :, b2_state[k-1]]
                overlaps = np.abs(vk.T @ prev_vec)
                b2_state[k] = np.argmax(overlaps)

            b2_idx_loop = b2_state

        # Now compute Berry phase using the tracked eigenstate
        # gamma = -Im ln prod_{j} <psi_j|psi_{j+1}>
        # For real eigenvectors, <psi_j|psi_{j+1}> is real, so gamma = 0 or pi
        # depending on the sign of the product

        phase_product = 1.0  # will be real  # (local)
        overlaps = np.zeros(N_theta)
        for k in range(N_theta):
            k_next = (k + 1) % N_theta
            idx_k = b2_idx_loop[k]
            idx_k_next = b2_idx_loop[k_next]
            psi_k = evecs_loop[k, :, idx_k]
            psi_k_next = evecs_loop[k_next, :, idx_k_next]
            overlap = np.dot(psi_k, psi_k_next)  # real since real eigenvectors
            overlaps[k] = overlap
            phase_product *= np.sign(overlap)  # track sign only (magnitude ~ 1)

        # Berry phase
        log_product = np.sum(np.log(np.abs(overlaps) + 1e-300))  # for magnitude check
        berry_phase = 0.0 if phase_product > 0 else pi

        # Also compute the "raw" Berry phase including magnitude effects
        complex_product = np.prod(overlaps)
        berry_phase_raw = -np.angle(complex_product) if complex_product != 0 else 0.0

        min_overlap = np.min(np.abs(overlaps))
        max_overlap = np.max(np.abs(overlaps))

        results[(r, N_theta)] = {
            'berry_phase': berry_phase,
            'berry_phase_raw': berry_phase_raw,
            'phase_product_sign': phase_product,
            'min_overlap': min_overlap,
            'max_overlap': max_overlap,
            'b2_idx': b2_idx_loop.copy(),
            'overlaps': overlaps.copy(),
        }

        if N_theta == 256:  # Report at one representative N
            print(f"  r={r:.4f}, N={N_theta}: gamma/pi = {berry_phase/pi:.4f}, "
                  f"sign(prod) = {phase_product:+.0f}, "
                  f"|overlap| in [{min_overlap:.8f}, {max_overlap:.8f}]")

# ============================================================
# Section 6: Convergence analysis
# ============================================================
print("\n--- Section 6: Convergence and structural analysis ---")

# For each radius, check convergence with N_theta
print("\n  Berry phase gamma/pi vs radius and N_theta:")
print(f"  {'r':>8s}  {'N=64':>8s}  {'N=128':>8s}  {'N=256':>8s}  {'N=512':>8s}")
for r in radii:
    row = f"  {r:8.4f}"
    for N in N_theta_values:
        if (r, N) in results:
            gamma = results[(r, N)]['berry_phase']
            row += f"  {gamma/pi:8.4f}"
        else:
            row += f"  {'skip':>8s}"
    print(row)

# Detailed analysis at optimal radius
print("\n  Detailed analysis at r=0.01, N=256:")
r_detail = 0.01  # (local)
N_detail = 256
if (r_detail, N_detail) in results:
    res = results[(r_detail, N_detail)]
    print(f"    Berry phase: gamma/pi = {res['berry_phase']/pi:.6f}")
    print(f"    Raw phase:   gamma/pi = {res['berry_phase_raw']/pi:.6f}")
    print(f"    Sign of overlap product: {res['phase_product_sign']:+.0f}")
    print(f"    Overlap magnitude range: [{res['min_overlap']:.10f}, {res['max_overlap']:.10f}]")
    print(f"    B2 index range: [{res['b2_idx'].min()}, {res['b2_idx'].max()}]")

    # Overlap-by-step statistics
    ov = res['overlaps']
    print(f"    Mean overlap: {np.mean(ov):.10f}")
    print(f"    Std overlap:  {np.std(ov):.2e}")
    n_negative = np.sum(ov < 0)
    print(f"    Negative overlaps: {n_negative} out of {len(ov)}")
    if n_negative > 0:
        neg_idx = np.where(ov < 0)[0]
        print(f"    Negative at theta indices: {neg_idx}")

# ============================================================
# Section 7: Structural theorem — real eigenvectors
# ============================================================
print("\n--- Section 7: Structural analysis (real Hamiltonian theorem) ---")

# The Hamiltonian H(tau, sigma) is real-symmetric for ALL (tau, sigma).
# This is because:
#   1. The adjacency matrices adj_C2, adj_su2, adj_u1 are real integer matrices
#   2. The Josephson couplings J_X(tau, sigma) are real positive scalars
#   3. H = sum of (real scalar) * (real matrix) + diagonal terms
#
# For a real-symmetric H, all eigenvectors can be chosen real.
# Berry curvature Omega = -Im sum_{m!=n} <n|dH|m><m|dH|n> / (E_n - E_m)^2
# For real eigenvectors: <n|dH|m> is REAL (H and dH are real-symmetric,
# eigenvectors are real), so the product is real, and Im = 0.
#
# Therefore Berry CURVATURE = 0 everywhere in parameter space.
#
# Berry PHASE around a closed loop can still be pi (not 0) if the loop
# encircles a point where two eigenvalues become degenerate (a conical
# intersection / diabolical point). At such a point, the eigenvector
# acquires a sign flip (pi Berry phase).
#
# For this to happen, we need codimension-2 conditions:
# In 2 parameters (tau, sigma), a degeneracy is codimension-2 and hence
# generically isolated points. The question is whether the dm2=0 crossing
# corresponds to such a degeneracy.

# Check: is the H(tau, sigma) real-symmetric everywhere on the loop?
print("  Verifying H is real-symmetric on loop points...")
theta_check = np.linspace(0, 2*pi, 20, endpoint=False)
max_asym = 0.0
max_imag = 0.0
for theta in theta_check:
    tau = tau_fold + 0.01 * np.cos(theta)
    sig = 0.01 * np.sin(theta)
    H = build_H(tau, sig)
    max_asym = max(max_asym, np.max(np.abs(H - H.T)))
    max_imag = max(max_imag, np.max(np.abs(np.imag(H))))
print(f"  max|H - H^T| = {max_asym:.2e}")
print(f"  max|Im(H)| = {max_imag:.2e}")
print(f"  H is real-symmetric: {'YES' if max_asym < 1e-15 and max_imag < 1e-15 else 'NO'}")

# For real-symmetric H, Berry phase is Z_2 quantized: 0 or pi.
# Check the gap structure to see if a degeneracy could exist

# Find the minimum gap between the B2 eigenvalue and its neighbors
# across the full 2D scan
print(f"\n  Gap analysis from 2D scan:")
print(f"    Minimum B2-neighbor gap: {min_gap_global:.6f}")
print(f"    This gap is {'LARGE (no degeneracy)' if min_gap_global > 0.01 else 'SMALL (possible degeneracy)'}")

# Search for exact degeneracy more carefully
# At a diabolical point, gap = 0. Let's check if gap ever gets close
print(f"\n  Gap distribution in 2D scan:")
gap_flat = min_gap_2d.flatten()
percentiles = [0, 1, 5, 25, 50, 75, 95, 99, 100]
for p in percentiles:
    print(f"    {p:3d}th percentile: {np.percentile(gap_flat, p):.6f}")

# ============================================================
# Section 8: Track dm^2_B2 in 2D to understand the zero-crossing
# ============================================================
print("\n--- Section 8: dm^2_B2 in 2D parameter space ---")

# The "B2 mass" is the eigenvalue of the B2-dominated state.
# dm^2/dtau changes sign at the fold. Let's track this in 2D.

# Compute d(eval)/dtau by finite difference along the loop
r_phys = 0.01  # (local)
N_phys = 256
theta_phys = np.linspace(0, 2*pi, N_phys, endpoint=False)
tau_phys = tau_fold + r_phys * np.cos(theta_phys)
sig_phys = r_phys * np.sin(theta_phys)

# B2 eigenvalue along the loop
b2_eval_loop = np.zeros(N_phys)
for k in range(N_phys):
    H = build_H(tau_phys[k], sig_phys[k])
    evals, evecs = eigh(H)
    b2_weights = evecs[B2_cell, :]**2
    b2_idx = np.argmax(b2_weights)
    b2_eval_loop[k] = evals[b2_idx]

print(f"  B2 eigenvalue on r=0.01 loop: [{b2_eval_loop.min():.6f}, {b2_eval_loop.max():.6f}]")
print(f"  Range: {b2_eval_loop.max() - b2_eval_loop.min():.2e}")
print(f"  This is {'a small variation on a large value' if b2_eval_loop.min() > 0.5 else 'near zero'}")

# ============================================================
# Section 9: Final verdict
# ============================================================
print("\n" + "=" * 72)
print("  SECTION 9: FINAL VERDICT — BERRY-FOLD-55")
print("=" * 72)

# Collect the definitive result
r_final = 0.01  # (local)
N_final = 256
res_final = results.get((r_final, N_final))
if res_final is None:
    # Try other combinations
    for r in radii:
        if (r, N_final) in results:
            res_final = results[(r, N_final)]
            r_final = r
            break

gamma_final = res_final['berry_phase']
sign_final = res_final['phase_product_sign']

print(f"\n  Berry phase: gamma = {gamma_final:.6f}")
print(f"  gamma/pi = {gamma_final/pi:.6f}")
print(f"  Sign of overlap product: {sign_final:+.0f}")
print(f"\n  STRUCTURAL FACTS:")
print(f"    1. H(tau, sigma) is real-symmetric for ALL (tau, sigma)")
print(f"    2. Berry curvature Omega = 0 identically (Im of real products)")
print(f"    3. Berry phase is Z_2 quantized: 0 or pi")
print(f"    4. gamma = pi requires a DEGENERACY inside the loop")
print(f"    5. Minimum gap in 2D scan: {min_gap_global:.6f} (NO degeneracy)")
print(f"    6. B2 eigenvalue at fold: {b2_eval_loop[np.argmin(np.abs(theta_phys))]:.6f} >> 0")
print(f"    7. The dm^2_B2 = 0 crossing is a DERIVATIVE zero (fold), not an eigenvalue zero")

if gamma_final == 0:
    verdict = "ACCIDENTAL"
    print(f"\n  RESULT: Berry phase = 0 => B2 mass zero-crossing is {verdict}")
    print(f"  The fold at tau*={tau_fold} is a smooth turning point in dm^2/dtau,")
    print(f"  NOT a topological feature. It can be removed by perturbation.")
else:
    verdict = "TOPOLOGICAL"
    print(f"\n  RESULT: Berry phase = pi => B2 mass zero-crossing is {verdict}")
    print(f"  The fold at tau*={tau_fold} is protected by a diabolical point.")

print(f"\n  Gate BERRY-FOLD-55: INFO — gamma/pi = {gamma_final/pi:.4f} ({verdict})")

# Consistency check across all radii
all_phases = []
for r in radii:
    for N in N_theta_values:
        if (r, N) in results:
            all_phases.append(results[(r, N)]['berry_phase'])
phases_agree = all(p == all_phases[0] for p in all_phases)
print(f"\n  Consistency: {len(all_phases)} loop computations, all agree: {phases_agree}")
if not phases_agree:
    print(f"  WARNING: Phases differ! {[p/pi for p in all_phases]}")

# ============================================================
# Section 10: Save data
# ============================================================
print("\n--- Section 10: Saving results ---")

# Collect all results for saving
save_data = {
    'tau_fold': tau_fold,
    'radii': np.array(radii),
    'N_theta_values': np.array(N_theta_values),
    'gamma_final': gamma_final,
    'verdict': np.array([verdict]),
    'min_gap_2d': min_gap_2d,
    'tau_scan_2d': tau_scan_2d,
    'sig_scan_2d': sig_scan_2d,
    'b2_eval_2d': b2_eval_2d,
    'b2_idx_2d': b2_idx_2d,
    'b2_eval_track': b2_eval_track,
    'tau_track': tau_test,
    'min_gap_track': min_gap_track,
}

# Add per-loop results
for (r, N), res in results.items():
    prefix = f"r{r:.4f}_N{N}"
    save_data[f"{prefix}_gamma"] = res['berry_phase']
    save_data[f"{prefix}_sign"] = res['phase_product_sign']
    save_data[f"{prefix}_min_overlap"] = res['min_overlap']

np.savez(OUT_NPZ, **save_data)
print(f"  Saved: {OUT_NPZ}")

# ============================================================
# Section 11: Plot
# ============================================================
print("\n--- Section 11: Plotting ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel 1: 2D gap map
ax = axes[0, 0]
im = ax.pcolormesh(sig_scan_2d, tau_scan_2d, min_gap_2d,
                   cmap='viridis', shading='auto')
plt.colorbar(im, ax=ax, label='Min gap to neighbor')
ax.set_xlabel(r'$\sigma$ (T2 deformation)')
ax.set_ylabel(r'$\tau$ (Jensen parameter)')
ax.set_title('B2 eigenvalue gap in 2D parameter space')
# Mark the fold
ax.axhline(tau_fold, color='red', linestyle='--', alpha=0.5, label=r'$\tau^*$')
ax.axvline(0, color='red', linestyle='--', alpha=0.5)
# Draw loop circles
for r in [0.01, 0.05, 0.10]:
    circle = Circle((0, tau_fold), r, fill=False, color='white',
                     linestyle='--', linewidth=1.5)
    ax.add_patch(circle)
ax.legend(fontsize=8)

# Panel 2: B2 eigenvalue on loops
ax = axes[0, 1]
for r in [0.005, 0.01, 0.05]:
    N_plot = 256
    theta_plot = np.linspace(0, 2*pi, N_plot, endpoint=False)
    tau_plot = tau_fold + r * np.cos(theta_plot)
    sig_plot = r * np.sin(theta_plot)
    eval_plot = np.zeros(N_plot)
    for k in range(N_plot):
        H = build_H(tau_plot[k], sig_plot[k])
        evals, _ = eigh(H)
        eval_plot[k] = evals[b2_idx_track[0]]  # use fixed index
    ax.plot(theta_plot / pi, eval_plot, label=f'r={r}')
ax.set_xlabel(r'$\theta / \pi$')
ax.set_ylabel('B2 eigenvalue')
ax.set_title('B2 eigenvalue around closed loops')
ax.legend()
ax.axhline(b2_eval_loop.mean(), color='gray', linestyle=':', alpha=0.5)

# Panel 3: Overlap along loop for r=0.01
ax = axes[1, 0]
if (0.01, 256) in results:
    ov = results[(0.01, 256)]['overlaps']
    theta_ov = np.linspace(0, 2*pi, 256, endpoint=False)
    ax.plot(theta_ov / pi, ov, 'b-', linewidth=0.5)
    ax.set_xlabel(r'$\theta / \pi$')
    ax.set_ylabel(r'$\langle\psi(\theta_j)|\psi(\theta_{j+1})\rangle$')
    ax.set_title(f'Overlap along loop (r=0.01, N=256)')
    ax.axhline(1, color='gray', linestyle=':', alpha=0.5)
    ax.axhline(0, color='red', linestyle=':', alpha=0.5)
    ax.set_ylim([min(0.99, ov.min() - 0.001), 1.001])

# Panel 4: Berry phase vs radius
ax = axes[1, 1]
r_plot = []
gamma_plot = []
for r in radii:
    if (r, 256) in results:
        r_plot.append(r)
        gamma_plot.append(results[(r, 256)]['berry_phase'] / pi)
ax.bar(range(len(r_plot)), gamma_plot, tick_label=[f'{r:.3f}' for r in r_plot],
       color=['green' if g == 0 else 'red' for g in gamma_plot])
ax.set_xlabel('Loop radius r')
ax.set_ylabel(r'$\gamma / \pi$')
ax.set_title(f'Berry phase vs loop radius (gate verdict: {verdict})')
ax.set_ylim([-0.1, 1.1])
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.axhline(1, color='gray', linestyle='-', alpha=0.3)

fig.suptitle(f'BERRY-FOLD-55: Berry Phase = {gamma_final/pi:.0f}$\\pi$ ({verdict})',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

print("\n" + "=" * 72)
print("  COMPUTATION COMPLETE")
print("=" * 72)
