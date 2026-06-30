#!/usr/bin/env python3
"""
S56 FABRIC-INTEG-56: Fabric-Level Integrability Diagnostic

Tests whether Josephson inter-cell coupling breaks the single-cell
Richardson-Gaudin integrability.

Physics:
    - Each isolated cell: Richardson-Gaudin integrable BCS with 8 modes,
      1 Cooper pair, 8 conserved quantities.
    - Josephson coupling: H_J = -E_J * (b_1^dag b_2 + b_2^dag b_1) / 2
      where b_i = sum_k c_{k,down} c_{k,up} is the pair annihilation operator.
    - 2-cell system: H = H_BCS(1) + H_BCS(2) + alpha * H_J(1,2)
    - Hilbert space: N_pair_total = 2 on 16 combined modes -> C(16,2) = 120 states.

Diagnostic: Mean adjacent gap ratio <r> (Atas et al. 2013).
    - Poisson (integrable): <r> = 2*ln(2) - 1 = 0.3863
    - GOE (chaotic): <r> = 0.5307

Gate: FABRIC-INTEGRABILITY-56
    PASS: <r> > 0.48 at alpha=1 (integrability broken)
    FAIL: <r> < 0.40 (Poisson persists)

Author: Volovik Superfluid Universe Theorist (S56)
"""

import numpy as np
from scipy.linalg import eigh
from itertools import combinations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    tau_fold, E_cond, N_cells, Delta_0_OES
)

# ============================================================
# 1. Load data from S54
# ============================================================
data_dir = os.path.dirname(os.path.abspath(__file__))

tb_data = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)
ed_data = np.load(os.path.join(data_dir, 's54_ed_sweep.npz'), allow_pickle=True)

tau_values_tb = tb_data['tau_values']
eigenvalues_tb = tb_data['eigenvalues']   # (50, 32)
fold_idx = int(ed_data['fold_idx'])        # = 19

E_sp = ed_data['E_sp_sweep']              # (50, 8) single-particle energies
V_bare = ed_data['V_bare_cont']           # (8, 8) pairing interaction

# Verify fold
print(f"Fold index: {fold_idx}, tau = {tau_values_tb[fold_idx]:.4f}")
print(f"Single-particle energies at fold: {E_sp[fold_idx]}")
print(f"V_bare diagonal: {np.diag(V_bare)}")
print(f"V_bare off-diagonal sample [0,1]={V_bare[0,1]:.6f}, [0,2]={V_bare[0,2]:.6f}")

N_modes = 8  # modes per cell (local)
N_pair_total = 2  # total pairs across 2 cells

# ============================================================
# 2. Build the 2-cell Hilbert space
# ============================================================
# Pair basis: each state is a set of 2 modes out of 16 (8 per cell)
# that are occupied by a Cooper pair.
# Mode indices 0-7: cell 1, modes 8-15: cell 2.

def build_pair_basis(n_modes_total, n_pairs):
    """Build basis of pair-occupied states: C(n_modes_total, n_pairs) states."""
    basis = list(combinations(range(n_modes_total), n_pairs))
    return basis

basis = build_pair_basis(2 * N_modes, N_pair_total)
dim = len(basis)
print(f"\nHilbert space dimension: C({2*N_modes},{N_pair_total}) = {dim}")
assert dim == 120, f"Expected dim=120, got {dim}"

# Create lookup for basis state -> index
basis_dict = {state: idx for idx, state in enumerate(basis)}


def classify_state(state):
    """Return (n1, n2) pair counts in cell 1 and cell 2."""
    n1 = sum(1 for k in state if k < N_modes)
    n2 = sum(1 for k in state if k >= N_modes)
    return n1, n2


# ============================================================
# 3. Build Hamiltonians
# ============================================================

def build_H_2cell(eps_1, eps_2, V_1, V_2, E_J_coupling, alpha):
    """
    Build the 2-cell BCS Hamiltonian in the pair basis.

    H = H_BCS(1) + H_BCS(2) + alpha * H_J(1,2)

    H_BCS(i) = sum_k 2*eps_k^(i) * n_k - sum_{k,l} V_{kl}^(i) * b_k^dag b_l

    H_J = -E_J/2 * (B_1^dag B_2 + B_2^dag B_1)
    where B_i = sum_k b_k^(i) is the total pair annihilation on cell i.

    In the pair basis |k1, k2> (two modes occupied):
    - Diagonal: 2*eps_{k1} + 2*eps_{k2}
    - Off-diagonal (BCS): if k1, k2 in same cell, V connects different pair states
    - Off-diagonal (Josephson): transfers a pair from one cell to the other

    Parameters:
        eps_1: (N_modes,) single-particle energies for cell 1
        eps_2: (N_modes,) single-particle energies for cell 2
        V_1: (N_modes, N_modes) pairing matrix for cell 1
        V_2: (N_modes, N_modes) pairing matrix for cell 2
        E_J_coupling: Josephson coupling energy
        alpha: coupling strength [0, 1]
    """
    H = np.zeros((dim, dim))

    for i, state_i in enumerate(basis):
        k1, k2 = state_i

        # --- Diagonal: kinetic energy ---
        # eps for mode k: cell 1 if k < N_modes, cell 2 if k >= N_modes
        E_kin = 0.0  # (local)
        for k in state_i:
            if k < N_modes:
                E_kin += 2.0 * eps_1[k]
            else:
                E_kin += 2.0 * eps_2[k - N_modes]
        H[i, i] += E_kin

        # --- BCS pairing within each cell ---
        # b_l^dag b_k: annihilate pair in mode k, create in mode l
        # This connects |..., k, ...> to |..., l, ...> (replacing k with l)
        # Only within same cell.

        for pos, k in enumerate(state_i):
            # Determine which cell k belongs to
            if k < N_modes:
                cell_k = 0
                k_local = k
                V_cell = V_1
                n_modes_offset = 0
            else:
                cell_k = 1
                k_local = k - N_modes
                V_cell = V_2
                n_modes_offset = N_modes

            # Try replacing k with l (same cell)
            for l_local in range(N_modes):
                l = l_local + n_modes_offset
                if l == k:
                    # Diagonal BCS: -V_{kk} * n_k contributes to diagonal
                    # Actually for a single pair in this mode, the mean-field
                    # diagonal shift is already in eps. The off-diagonal part
                    # is what matters. For BCS: H_pair = -sum_{kl} V_{kl} b_k^dag b_l
                    # Diagonal contribution: -V_{kk} when pair occupies k
                    H[i, i] -= V_cell[k_local, k_local]
                    continue
                if l in state_i:
                    continue  # mode l already occupied by the other pair

                # New state: replace k with l
                new_state = list(state_i)
                new_state[pos] = l
                new_state = tuple(sorted(new_state))

                if new_state in basis_dict:
                    j = basis_dict[new_state]
                    # -V_{l,k} connects state_i -> new_state
                    H[i, j] -= V_cell[l_local, k_local]

        # --- Josephson coupling: inter-cell pair transfer ---
        # H_J = -(E_J/2) * (B_1^dag B_2 + B_2^dag B_1)
        # B_1^dag B_2: annihilate a pair in cell 2, create in cell 1
        # In pair basis: if state has pair in mode k (cell 2),
        # replace it with mode l (cell 1)

        if alpha > 0 and E_J_coupling > 0:
            for pos, k in enumerate(state_i):
                if k >= N_modes:
                    # Pair in cell 2 at mode k_local = k - N_modes
                    k_local_2 = k - N_modes
                    # Transfer to cell 1, mode l_local
                    for l_local_1 in range(N_modes):
                        l = l_local_1  # cell 1 mode
                        if l in state_i:
                            continue  # already occupied
                        new_state = list(state_i)
                        new_state[pos] = l
                        new_state = tuple(sorted(new_state))
                        if new_state in basis_dict:
                            j = basis_dict[new_state]
                            # Josephson: -(E_J/2) * amplitude
                            # The pair transfer operator B_1^dag B_2 has matrix element 1
                            # for each (l_1, k_2) combination
                            H[i, j] -= alpha * E_J_coupling / 2.0

                elif k < N_modes:
                    # Pair in cell 1 at mode k_local
                    # Transfer to cell 2, mode l_local
                    for l_local_2 in range(N_modes):
                        l = l_local_2 + N_modes  # cell 2 mode
                        if l in state_i:
                            continue
                        new_state = list(state_i)
                        new_state[pos] = l
                        new_state = tuple(sorted(new_state))
                        if new_state in basis_dict:
                            j = basis_dict[new_state]
                            H[i, j] -= alpha * E_J_coupling / 2.0

    # Symmetrize (should already be symmetric, but ensure numerical precision)
    H = (H + H.T) / 2.0
    return H


def compute_gap_ratio(eigenvalues):
    """
    Compute mean adjacent gap ratio <r>.

    r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1})
    where s_n = E_{n+1} - E_n are the level spacings.

    Poisson: <r> = 2*ln(2) - 1 = 0.3863
    GOE: <r> = 0.5307 (4 - 2*sqrt(3)) approx

    We use the central 80% of the spectrum to avoid edge effects.
    """
    E = np.sort(eigenvalues)
    spacings = np.diff(E)

    # Filter out near-zero spacings (degeneracies)
    # Use a threshold of 1e-10 relative to mean spacing
    mean_spacing = np.mean(spacings)
    mask = spacings > 1e-10 * mean_spacing
    spacings_clean = spacings[mask]

    if len(spacings_clean) < 10:
        return np.nan, 0

    # Use central 80% to avoid edge effects
    n = len(spacings_clean)
    start = n // 10
    end = n - n // 10
    s = spacings_clean[start:end]

    # Gap ratios
    r_vals = []
    for i in range(len(s) - 1):
        r = min(s[i], s[i+1]) / max(s[i], s[i+1])
        r_vals.append(r)

    r_mean = np.mean(r_vals)
    n_ratios = len(r_vals)
    return r_mean, n_ratios


# ============================================================
# 4. Compute E_J from S54 data
# ============================================================
# E_J per bond from S55/S56: E_J = J_C2^2 * F_anom
# From W0-1: E_J(fold) = 7.042 M_KK
# But for the 2-cell system, we need E_J for a single bond.

J_C2_values = tb_data['J_C2_tau']  # (50,)
print(f"\nJ_C2 at fold: {J_C2_values[fold_idx]:.6f}")

# Compute E_J using anomalous density
# F_anom = sum_k Delta / (2 * E_qp_k^2), where E_qp_k = sqrt((eps_k - mu)^2 + Delta^2)
# mu = 0 (PH symmetric), Delta = Delta_0_OES

def compute_E_J(eps, J_C2, Delta=Delta_0_OES):
    """Compute Josephson energy per bond."""
    E_qp = np.sqrt(eps**2 + Delta**2)
    F_anom = np.sum(Delta / (2.0 * E_qp**2))
    E_J = J_C2**2 * F_anom
    return E_J, F_anom


# ============================================================
# 5. Main computation: sweep alpha at fold tau
# ============================================================

print("\n" + "="*60)
print("COMPUTATION 1: alpha sweep at fold tau")
print("="*60)

# Single-particle energies at fold (same for both cells in identical case)
eps_fold = E_sp[fold_idx].copy()
print(f"eps at fold: {eps_fold}")

# V matrix
V_fold = V_bare.copy()
print(f"V_bare shape: {V_fold.shape}")
print(f"V_bare symmetry check: max|V-V^T| = {np.max(np.abs(V_fold - V_fold.T)):.2e}")

# Symmetrize V if needed
V_fold = (V_fold + V_fold.T) / 2.0

# Compute E_J at fold
E_J_fold, F_anom_fold = compute_E_J(eps_fold, J_C2_values[fold_idx])
print(f"E_J at fold = {E_J_fold:.4f} M_KK (F_anom = {F_anom_fold:.4f})")

# Alpha sweep: 20 values from 0 to 1
n_alpha = 20  # (local)
alpha_values = np.linspace(0.0, 1.0, n_alpha)

r_means = np.zeros(n_alpha)
n_ratios_arr = np.zeros(n_alpha, dtype=int)
eigenvalue_sets = []

for i_a, alpha in enumerate(alpha_values):
    H = build_H_2cell(eps_fold, eps_fold, V_fold, V_fold, E_J_fold, alpha)

    # Check Hermiticity
    if i_a == 0:
        herm_err = np.max(np.abs(H - H.T))
        print(f"Hermiticity check: max|H-H^T| = {herm_err:.2e}")

    evals = eigh(H, eigvals_only=True)
    eigenvalue_sets.append(evals)

    r, nr = compute_gap_ratio(evals)
    r_means[i_a] = r
    n_ratios_arr[i_a] = nr

    if alpha in [0.0, 0.5, 1.0] or i_a == 0 or i_a == n_alpha - 1:
        print(f"  alpha={alpha:.3f}: <r>={r:.4f} (n_ratios={nr}), "
              f"E_min={evals[0]:.4f}, E_max={evals[-1]:.4f}")

print(f"\n<r> at alpha=0: {r_means[0]:.4f} (Poisson target: 0.3863)")
print(f"<r> at alpha=1: {r_means[-1]:.4f} (GOE target: 0.5307)")

# ============================================================
# 6. Non-identical cells: break cell-exchange symmetry
# ============================================================
# The identical-cell system has an additional Z_2 symmetry (cell exchange).
# This can produce spurious Poisson statistics if sectors are not resolved.
# Test with slightly different cells to break this symmetry.

print("\n" + "="*60)
print("COMPUTATION 2: Non-identical cells (symmetry-broken)")
print("="*60)

# Perturb cell 2 energies by 5%
eps_fold_2 = eps_fold * 1.05
print(f"Cell 2 eps (5% shifted): {eps_fold_2}")

E_J_fold_2, _ = compute_E_J(eps_fold_2, J_C2_values[fold_idx])
# Use average E_J for the bond
E_J_avg = (E_J_fold + E_J_fold_2) / 2.0
print(f"E_J (cell 1) = {E_J_fold:.4f}, E_J (cell 2) = {E_J_fold_2:.4f}, avg = {E_J_avg:.4f}")

r_means_asym = np.zeros(n_alpha)
n_ratios_asym = np.zeros(n_alpha, dtype=int)
eigenvalue_sets_asym = []

for i_a, alpha in enumerate(alpha_values):
    H = build_H_2cell(eps_fold, eps_fold_2, V_fold, V_fold, E_J_avg, alpha)
    evals = eigh(H, eigvals_only=True)
    eigenvalue_sets_asym.append(evals)

    r, nr = compute_gap_ratio(evals)
    r_means_asym[i_a] = r
    n_ratios_asym[i_a] = nr

    if alpha in [0.0, 0.5, 1.0] or i_a == 0 or i_a == n_alpha - 1:
        print(f"  alpha={alpha:.3f}: <r>={r:.4f} (n_ratios={nr})")

print(f"\nAsymmetric: <r> at alpha=0: {r_means_asym[0]:.4f}")
print(f"Asymmetric: <r> at alpha=1: {r_means_asym[-1]:.4f}")

# ============================================================
# 7. Tau sweep at alpha=1 (5 tau values near fold)
# ============================================================

print("\n" + "="*60)
print("COMPUTATION 3: Tau sweep at fixed alpha=1")
print("="*60)

# 5 tau values: well below fold, approaching, at fold, past fold, well past
tau_indices = [5, 12, fold_idx, 25, 35]  # tau ~ 0.05, 0.12, 0.19, 0.26, 0.36

r_tau_sym = np.zeros(len(tau_indices))
r_tau_asym = np.zeros(len(tau_indices))
tau_sweep = np.zeros(len(tau_indices))
EJ_sweep = np.zeros(len(tau_indices))

for i_t, tidx in enumerate(tau_indices):
    eps_t = E_sp[tidx]
    tau_t = tau_values_tb[tidx]
    tau_sweep[i_t] = tau_t

    E_J_t, _ = compute_E_J(eps_t, J_C2_values[tidx])
    EJ_sweep[i_t] = E_J_t

    # Symmetric
    H_sym = build_H_2cell(eps_t, eps_t, V_fold, V_fold, E_J_t, 1.0)
    evals_sym = eigh(H_sym, eigvals_only=True)
    r_s, _ = compute_gap_ratio(evals_sym)
    r_tau_sym[i_t] = r_s

    # Asymmetric (5% perturbation on cell 2)
    eps_t2 = eps_t * 1.05
    E_J_t2, _ = compute_E_J(eps_t2, J_C2_values[tidx])
    E_J_tavg = (E_J_t + E_J_t2) / 2.0

    H_asym = build_H_2cell(eps_t, eps_t2, V_fold, V_fold, E_J_tavg, 1.0)
    evals_asym = eigh(H_asym, eigvals_only=True)
    r_a, _ = compute_gap_ratio(evals_asym)
    r_tau_asym[i_t] = r_a

    print(f"  tau={tau_t:.4f}: E_J={E_J_t:.4f}, <r>_sym={r_s:.4f}, <r>_asym={r_a:.4f}")


# ============================================================
# 8. Sector-resolved analysis
# ============================================================
# The 2-cell system at alpha=0 has conserved N_1 (pairs in cell 1).
# States split into sectors: (N_1=0, N_2=2), (N_1=1, N_2=1), (N_1=2, N_2=0).
# The Josephson coupling mixes (N_1, N_2) sectors with |Delta N_1| = 1.
# We should check <r> within the (1,1) sector at alpha=0 and then
# after mixing at alpha=1.

print("\n" + "="*60)
print("COMPUTATION 4: Sector-resolved statistics")
print("="*60)

# Classify basis states by (n1, n2)
sector_02 = [i for i, s in enumerate(basis) if classify_state(s) == (0, 2)]
sector_11 = [i for i, s in enumerate(basis) if classify_state(s) == (1, 1)]
sector_20 = [i for i, s in enumerate(basis) if classify_state(s) == (2, 0)]

print(f"Sector sizes: (0,2)={len(sector_02)}, (1,1)={len(sector_11)}, (2,0)={len(sector_20)}")
print(f"Total: {len(sector_02)+len(sector_11)+len(sector_20)} (should be {dim})")

# At alpha=0, compute <r> within the (1,1) sector (largest, C(8,1)*C(8,1)=64)
H_0 = build_H_2cell(eps_fold, eps_fold, V_fold, V_fold, E_J_fold, 0.0)
evals_0 = eigh(H_0, eigvals_only=True)

# Extract (1,1) sector eigenvalues at alpha=0
# For identical cells, the (0,2) and (2,0) sectors are degenerate
# The (1,1) sector is the largest
H_11 = H_0[np.ix_(sector_11, sector_11)]
evals_11 = np.sort(np.linalg.eigvalsh(H_11))
r_11_a0, nr_11 = compute_gap_ratio(evals_11)
print(f"\n(1,1) sector at alpha=0: dim={len(sector_11)}, <r>={r_11_a0:.4f} (n_ratios={nr_11})")

H_02 = H_0[np.ix_(sector_02, sector_02)]
evals_02 = np.sort(np.linalg.eigvalsh(H_02))
r_02_a0, nr_02 = compute_gap_ratio(evals_02)
print(f"(0,2) sector at alpha=0: dim={len(sector_02)}, <r>={r_02_a0:.4f} (n_ratios={nr_02})")

# At alpha=1, full spectrum mixing
H_1 = build_H_2cell(eps_fold, eps_fold, V_fold, V_fold, E_J_fold, 1.0)
evals_1 = eigh(H_1, eigvals_only=True)
r_full_a1, nr_full = compute_gap_ratio(evals_1)
print(f"\nFull spectrum at alpha=1: <r>={r_full_a1:.4f} (n_ratios={nr_full})")

# Check sector mixing at alpha=1
_, evecs_1 = eigh(H_1)
# Compute participation in each sector
sector_weights = np.zeros((dim, 3))
for i in range(dim):
    v = evecs_1[:, i]
    sector_weights[i, 0] = np.sum(v[sector_02]**2)
    sector_weights[i, 1] = np.sum(v[sector_11]**2)
    sector_weights[i, 2] = np.sum(v[sector_20]**2)

mixing = 1.0 - np.max(sector_weights, axis=1)
print(f"Mean sector mixing at alpha=1: {np.mean(mixing):.4f}")
print(f"Max sector mixing: {np.max(mixing):.4f}")
print(f"Min sector mixing: {np.min(mixing):.4f}")
print(f"States with >10% mixing: {np.sum(mixing > 0.1)}/{dim}")

# ============================================================
# 9. E_J strength analysis
# ============================================================
# How does the Josephson coupling compare to level spacing?
# If E_J >> mean spacing, coupling is strong and should break integrability.

print("\n" + "="*60)
print("KEY RATIOS")
print("="*60)

mean_spacing_0 = np.mean(np.diff(np.sort(evals_0)))
mean_spacing_1 = np.mean(np.diff(np.sort(evals_1)))
bandwidth_0 = evals_0[-1] - evals_0[0]
bandwidth_1 = evals_1[-1] - evals_1[0]

print(f"E_J(fold) = {E_J_fold:.4f} M_KK")
print(f"Mean level spacing (alpha=0): {mean_spacing_0:.6f}")
print(f"Mean level spacing (alpha=1): {mean_spacing_1:.6f}")
print(f"E_J / mean_spacing: {E_J_fold / mean_spacing_0:.1f}")
print(f"Bandwidth (alpha=0): {bandwidth_0:.4f}")
print(f"Bandwidth (alpha=1): {bandwidth_1:.4f}")
print(f"|E_cond| per cell = {abs(E_cond):.4f}")

# ============================================================
# 10. Full E_J sweep (stronger coupling test)
# ============================================================
# The physical E_J might be too weak relative to the discrete spectrum.
# Sweep E_J from 0 to 10x physical value.

print("\n" + "="*60)
print("COMPUTATION 5: E_J strength sweep at fold")
print("="*60)

EJ_multipliers = np.array([0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0])
r_EJ_sweep = np.zeros(len(EJ_multipliers))

for i_e, mult in enumerate(EJ_multipliers):
    H = build_H_2cell(eps_fold, eps_fold_2, V_fold, V_fold,
                       E_J_fold * mult, 1.0)
    evals = eigh(H, eigvals_only=True)
    r, _ = compute_gap_ratio(evals)
    r_EJ_sweep[i_e] = r
    print(f"  E_J_mult={mult:.2f}: E_J_eff={E_J_fold*mult:.4f}, <r>={r:.4f}")


# ============================================================
# 11. Unfolding test: use unfolded spectrum
# ============================================================
# Standard RMT diagnostic uses the unfolded spectrum.
# Fit a smooth N(E) and compute unfolded levels.

print("\n" + "="*60)
print("COMPUTATION 6: Unfolded spectrum analysis")
print("="*60)

def unfold_spectrum(evals, n_poly=6):
    """Unfold spectrum using polynomial fit to integrated density of states."""
    E = np.sort(evals)
    n = len(E)
    # Integrated density of states: N(E_i) = (i + 0.5) / n
    N_raw = (np.arange(n) + 0.5) / n

    # Fit polynomial to N(E) vs E
    coeffs = np.polyfit(E, N_raw, n_poly)
    N_smooth = np.polyval(coeffs, E)

    # Unfolded levels: xi_i = n * N_smooth(E_i)
    xi = n * N_smooth
    return xi

def compute_gap_ratio_unfolded(evals, n_poly=6):
    """Compute <r> on unfolded spectrum."""
    xi = unfold_spectrum(evals, n_poly)
    spacings = np.diff(xi)

    # Filter
    mask = spacings > 1e-10
    s = spacings[mask]

    if len(s) < 10:
        return np.nan

    # Central 80%
    n = len(s)
    start = n // 10
    end = n - n // 10
    s = s[start:end]

    r_vals = [min(s[i], s[i+1]) / max(s[i], s[i+1]) for i in range(len(s)-1)]
    return np.mean(r_vals)

# Unfolded analysis at alpha=0 and alpha=1 (asymmetric)
for alpha_test in [0.0, 0.5, 1.0]:
    H = build_H_2cell(eps_fold, eps_fold_2, V_fold, V_fold, E_J_avg, alpha_test)
    evals = eigh(H, eigvals_only=True)
    r_raw, _ = compute_gap_ratio(evals)
    r_unf = compute_gap_ratio_unfolded(evals)
    print(f"  alpha={alpha_test:.1f}: <r>_raw={r_raw:.4f}, <r>_unfolded={r_unf:.4f}")


# ============================================================
# 12. Save results
# ============================================================

save_path = os.path.join(data_dir, 's56_fabric_integ.npz')

np.savez(save_path,
    # Alpha sweep (symmetric)
    alpha_values=alpha_values,
    r_means_sym=r_means,
    n_ratios_sym=n_ratios_arr,
    # Alpha sweep (asymmetric)
    r_means_asym=r_means_asym,
    n_ratios_asym=n_ratios_asym,
    # Tau sweep
    tau_sweep=tau_sweep,
    r_tau_sym=r_tau_sym,
    r_tau_asym=r_tau_asym,
    EJ_sweep=EJ_sweep,
    # Sector analysis
    sector_sizes=np.array([len(sector_02), len(sector_11), len(sector_20)]),
    r_11_a0=r_11_a0,
    r_02_a0=r_02_a0,
    r_full_a1=r_full_a1,
    mean_mixing=np.mean(mixing),
    # E_J sweep
    EJ_multipliers=EJ_multipliers,
    r_EJ_sweep=r_EJ_sweep,
    # Key parameters
    E_J_fold=E_J_fold,
    eps_fold=eps_fold,
    dim=dim,
    fold_idx=fold_idx,
    tau_fold_actual=tau_values_tb[fold_idx],
    # Eigenvalue sets for plotting
    eigenvalues_a0=eigenvalue_sets[0],
    eigenvalues_a1=eigenvalue_sets[-1],
    eigenvalues_a0_asym=eigenvalue_sets_asym[0],
    eigenvalues_a1_asym=eigenvalue_sets_asym[-1],
)
print(f"\nData saved to {save_path}")


# ============================================================
# 13. Plot
# ============================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))

# Panel 1: <r> vs alpha (symmetric + asymmetric)
ax = axes[0, 0]
ax.plot(alpha_values, r_means, 'b-o', ms=4, label='Identical cells')
ax.plot(alpha_values, r_means_asym, 'r-s', ms=4, label='5% asymmetry')
ax.axhline(y=0.3863, color='green', ls='--', lw=1.5, label='Poisson (0.386)')
ax.axhline(y=0.5307, color='orange', ls='--', lw=1.5, label='GOE (0.531)')
ax.axhline(y=0.48, color='red', ls=':', lw=1.5, label='PASS threshold')
ax.set_xlabel(r'$\alpha$ (Josephson coupling)', fontsize=12)
ax.set_ylabel(r'$\langle r \rangle$', fontsize=12)
ax.set_title(f'Level Statistics vs Coupling (fold, dim={dim})', fontsize=12)
ax.legend(fontsize=9, loc='upper left')
ax.set_ylim(0.25, 0.65)
ax.grid(True, alpha=0.3)

# Panel 2: Tau sweep
ax = axes[0, 1]
ax.plot(tau_sweep, r_tau_sym, 'b-o', ms=6, label='Identical cells')
ax.plot(tau_sweep, r_tau_asym, 'r-s', ms=6, label='5% asymmetry')
ax.axhline(y=0.3863, color='green', ls='--', lw=1.5, label='Poisson')
ax.axhline(y=0.5307, color='orange', ls='--', lw=1.5, label='GOE')
ax.axhline(y=0.48, color='red', ls=':', lw=1.5)
ax.axvline(x=tau_values_tb[fold_idx], color='gray', ls=':', lw=1.5, label='fold')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$\langle r \rangle$ at $\alpha=1$', fontsize=12)
ax.set_title('Level Statistics vs Modulus', fontsize=12)
ax.legend(fontsize=9)
ax.set_ylim(0.25, 0.65)
ax.grid(True, alpha=0.3)

# Panel 3: E_J strength sweep
ax = axes[0, 2]
ax.semilogx(EJ_multipliers, r_EJ_sweep, 'k-o', ms=5)
ax.axhline(y=0.3863, color='green', ls='--', lw=1.5, label='Poisson')
ax.axhline(y=0.5307, color='orange', ls='--', lw=1.5, label='GOE')
ax.axhline(y=0.48, color='red', ls=':', lw=1.5, label='PASS')
ax.axvline(x=1.0, color='gray', ls=':', label='Physical E_J')
ax.set_xlabel(r'$E_J / E_J^{\rm phys}$', fontsize=12)
ax.set_ylabel(r'$\langle r \rangle$', fontsize=12)
ax.set_title('E_J Strength Sweep (asymmetric)', fontsize=12)
ax.legend(fontsize=9)
ax.set_ylim(0.25, 0.65)
ax.grid(True, alpha=0.3)

# Panel 4: Level spacing distribution at alpha=0
ax = axes[1, 0]
evals_0_clean = eigenvalue_sets_asym[0]
s0 = np.diff(np.sort(evals_0_clean))
s0 = s0[s0 > 1e-10 * np.mean(s0)]
s0_norm = s0 / np.mean(s0)
ax.hist(s0_norm, bins=20, density=True, alpha=0.7, color='blue', label=r'$\alpha=0$')
x = np.linspace(0, 4, 100)
ax.plot(x, np.exp(-x), 'g--', lw=2, label='Poisson')
ax.plot(x, (np.pi/2)*x*np.exp(-np.pi*x**2/4), 'r--', lw=2, label='GOE')
ax.set_xlabel(r'$s / \langle s \rangle$', fontsize=12)
ax.set_ylabel('P(s)', fontsize=12)
ax.set_title(r'Spacing Distribution ($\alpha=0$, asym)', fontsize=12)
ax.legend(fontsize=10)
ax.set_xlim(0, 4)

# Panel 5: Level spacing distribution at alpha=1
ax = axes[1, 1]
evals_1_clean = eigenvalue_sets_asym[-1]
s1 = np.diff(np.sort(evals_1_clean))
s1 = s1[s1 > 1e-10 * np.mean(s1)]
s1_norm = s1 / np.mean(s1)
ax.hist(s1_norm, bins=20, density=True, alpha=0.7, color='red', label=r'$\alpha=1$')
ax.plot(x, np.exp(-x), 'g--', lw=2, label='Poisson')
ax.plot(x, (np.pi/2)*x*np.exp(-np.pi*x**2/4), 'r--', lw=2, label='GOE')
ax.set_xlabel(r'$s / \langle s \rangle$', fontsize=12)
ax.set_ylabel('P(s)', fontsize=12)
ax.set_title(r'Spacing Distribution ($\alpha=1$, asym)', fontsize=12)
ax.legend(fontsize=10)
ax.set_xlim(0, 4)

# Panel 6: Eigenvalue spectrum comparison
ax = axes[1, 2]
evals_a0 = np.sort(eigenvalue_sets_asym[0])
evals_a1 = np.sort(eigenvalue_sets_asym[-1])
ax.plot(range(dim), evals_a0, 'b.', ms=3, alpha=0.6, label=r'$\alpha=0$')
ax.plot(range(dim), evals_a1, 'r.', ms=3, alpha=0.6, label=r'$\alpha=1$')
ax.set_xlabel('Level index', fontsize=12)
ax.set_ylabel('Energy (M_KK)', fontsize=12)
ax.set_title('Eigenvalue Spectrum', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.suptitle('FABRIC-INTEG-56: Josephson Coupling vs Integrability\n'
             f'2-cell BCS, dim={dim}, fold tau={tau_values_tb[fold_idx]:.3f}, '
             f'E_J={E_J_fold:.3f} M_KK', fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.94])

plot_path = os.path.join(data_dir, 's56_fabric_integ.png')
plt.savefig(plot_path, dpi=150)
print(f"Plot saved to {plot_path}")

# ============================================================
# 14. Summary
# ============================================================
print("\n" + "="*60)
print("SUMMARY: FABRIC-INTEG-56")
print("="*60)
print(f"Hilbert space: C(16,2) = {dim} states, 2 cells x 8 modes x 1 pair each")
print(f"Fold: tau = {tau_values_tb[fold_idx]:.4f}, E_J = {E_J_fold:.4f} M_KK")
print(f"")
print(f"--- Alpha sweep at fold ---")
print(f"<r>(alpha=0, symmetric):  {r_means[0]:.4f}  (Poisson=0.386)")
print(f"<r>(alpha=1, symmetric):  {r_means[-1]:.4f}")
print(f"<r>(alpha=0, asymmetric): {r_means_asym[0]:.4f}")
print(f"<r>(alpha=1, asymmetric): {r_means_asym[-1]:.4f}")
print(f"")
print(f"--- Sector analysis ---")
print(f"(1,1) sector <r> at alpha=0: {r_11_a0:.4f} (dim={len(sector_11)})")
print(f"(0,2) sector <r> at alpha=0: {r_02_a0:.4f} (dim={len(sector_02)})")
print(f"Full spectrum <r> at alpha=1: {r_full_a1:.4f}")
print(f"Mean sector mixing at alpha=1: {np.mean(mixing):.4f}")
print(f"")
print(f"--- Tau sweep at alpha=1 ---")
for i_t in range(len(tau_sweep)):
    print(f"  tau={tau_sweep[i_t]:.3f}: <r>_sym={r_tau_sym[i_t]:.4f}, <r>_asym={r_tau_asym[i_t]:.4f}")
print(f"")
print(f"--- E_J strength sweep ---")
for i_e in range(len(EJ_multipliers)):
    print(f"  E_J/E_J_phys={EJ_multipliers[i_e]:.2f}: <r>={r_EJ_sweep[i_e]:.4f}")
print(f"")

# Gate verdict
r_gate = r_means_asym[-1]  # Use asymmetric case (broken Z_2)
if r_gate > 0.48:
    verdict = "PASS"
    msg = f"<r>={r_gate:.4f} > 0.48: integrability broken by Josephson coupling"
elif r_gate < 0.40:
    verdict = "FAIL"
    msg = f"<r>={r_gate:.4f} < 0.40: Poisson statistics persist"
else:
    verdict = "INFO"
    msg = f"<r>={r_gate:.4f} in [0.40, 0.48]: transition regime, inconclusive"

print(f"GATE VERDICT: FABRIC-INTEGRABILITY-56 = {verdict}")
print(f"  {msg}")
print(f"  Reference: Poisson <r>=0.386, GOE <r>=0.531")
