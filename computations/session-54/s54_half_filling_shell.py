#!/usr/bin/env python3
"""
s54_half_filling_shell.py — Shell Correction Scaling with N_pair
================================================================
Session 54, W3-9: HALF-FILLING-SHELL-54

Tests the Connes x Nazarewicz prediction (S53 workshop) that Strutinsky
shell correction amplitude grows as ~sqrt(N_pair) toward half-filling.

Method:
  1. Load lattice single-particle energies E_k(tau) from W0-1
  2. Load continuum V_bare from S48 (Strutinsky approach B: lattice E_sp + continuum V)
  3. At N_pair = 1, 2, 3, 4 (half-filling of 8 modes):
     - Build canonical BCS Hamiltonian in C(8, N_pair) Fock space
     - Exact diagonalization -> E_0(tau)
     - Strutinsky smoothing -> E_smooth(tau)
     - Shell correction: delta_E_shell = E_0 - E_smooth
     - Also: pure single-particle shell correction (no pairing)
  4. Extract |delta_E_shell| amplitude at 10 tau values near fold
  5. Fit scaling: |delta_E| vs sqrt(N_pair)
  6. Compare to nuclear benchmark: ^18O (1 pair) -> ^28Si (6 pairs), 2.7x enhancement

Physics (Paper 02, Dobaczewski; Paper 03, Bogoliubov; Paper 08, pairing collapse):
  - Shell corrections arise from non-uniform single-particle level density
  - In nuclei, |delta_E_shell| ~ sqrt(A) ~ sqrt(N) for closed-shell regions
  - Pairing REDUCES shell effects (odd-even staggering, Paper 03 eq. 2.17)
  - At half-filling, pairing is maximal (all u_k ~ v_k ~ 1/sqrt(2))
  - The competition between shell structure and pairing is the core nuclear DFT problem

Gate: HALF-FILLING-SHELL-54 (INFO)
  Reports gradient ratio at each N_pair.

Author: nazarewicz-nuclear-structure-theorist, Session 54
Date: 2026-03-21
"""

import numpy as np
from scipy.integrate import trapezoid
from scipy.optimize import curve_fit
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import tau_fold

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data_dir = Path(__file__).parent
archive_dir = Path(__file__).parent.parent / 'computations/_shared'
t_start = time.time()

N_MODES = 8  # (local)
N_PAIR_VALUES = [1, 2, 3, 4]  # Up to half-filling

# Tau grid: 10 values near the fold [0.10, 0.30]
TAU_MIN, TAU_MAX = 0.10, 0.30
STRUTINSKY_GAMMA = 0.4  # Primary smoothing width (matches W1-1)  # (local)
GAMMA_TEST = [0.2, 0.3, 0.4, 0.5, 0.6]  # For plateau check

print("=" * 78)
print("HALF-FILLING-SHELL-54: Shell Correction Scaling with N_pair")
print("=" * 78)

# ============================================================================
# Section 1: Load Data
# ============================================================================

print("\n--- Section 1: Loading Data ---")

d_tb = np.load(data_dir / 's54_tb_hamiltonian.npz', allow_pickle=True)
tau_all = d_tb['tau_values']       # (50,)
eigenvalues = d_tb['eigenvalues']  # (50, 32)
N_tau_full = len(tau_all)

# Load W1-1 reference for cross-check
d_w1 = np.load(data_dir / 's54_ed_sweep.npz', allow_pickle=True)
fold_idx_full = int(d_w1['fold_idx'])
V_bare_cont = d_w1['V_bare_cont'].copy()  # 8x8 continuum sector pairing

# Select 10 tau values near the fold
tau_mask = (tau_all >= TAU_MIN) & (tau_all <= TAU_MAX)
tau_indices = np.where(tau_mask)[0]
# Subsample to ~10 evenly spaced
if len(tau_indices) > 10:
    step = max(1, len(tau_indices) // 10)
    tau_indices = tau_indices[::step][:10]
N_tau = len(tau_indices)
tau_values = tau_all[tau_indices]

print(f"Loaded {N_tau_full} total tau values")
print(f"Selected {N_tau} tau near fold: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"Fold at tau={tau_all[fold_idx_full]:.4f} (index {fold_idx_full})")
print(f"V_bare_cont norm: {np.linalg.norm(V_bare_cont):.6f}")
print(f"V(B1,B1) = {V_bare_cont[4,4]:.2e} (Trap 1: zero)")

# Single-particle energies: lowest 8 lattice eigenvalues at selected tau
E_sp_all = eigenvalues[tau_indices, :N_MODES]  # (N_tau, 8)

print(f"E_sp at fold: {E_sp_all[np.argmin(np.abs(tau_values - tau_fold))]}")

# ============================================================================
# Section 2: Canonical BCS Hamiltonian
# ============================================================================

print("\n--- Section 2: Building Canonical BCS Hamiltonians ---")


def build_canonical_states(n_modes, n_pair):
    """Generate all states with exactly n_pair occupied modes.

    Each state is a tuple of occupied mode indices.
    Fock space dimension = C(n_modes, n_pair).
    """
    states = list(combinations(range(n_modes), n_pair))
    return states


def build_canonical_H(E_sp, V, n_pair):
    """Build BCS Hamiltonian in the N-pair canonical subspace.

    H = sum_k 2*eps_k * n_k - sum_{k!=k'} V_{kk'} P+_k P_{k'}

    where P+_k creates a pair in mode k, P_{k'} annihilates a pair in mode k'.
    In the canonical basis, P+_k P_{k'} scatters a pair from level k' to level k.

    Parameters
    ----------
    E_sp : array (n_modes,) — single-particle energies
    V : array (n_modes, n_modes) — pairing interaction matrix
    n_pair : int — number of pairs

    Returns
    -------
    H : array (dim, dim) — Hamiltonian matrix
    states : list of tuples — basis states (occupied mode indices)
    """
    states = build_canonical_states(len(E_sp), n_pair)
    dim = len(states)
    state_to_idx = {s: i for i, s in enumerate(states)}
    H = np.zeros((dim, dim))

    for i, state in enumerate(states):
        # Diagonal: kinetic energy of all occupied pairs
        for k in state:
            H[i, i] += 2.0 * E_sp[k]

        # Off-diagonal: pair scattering k' -> k
        # |new_state> = P+_k P_{k'} |state>
        # This requires k' IN state and k NOT IN state
        occ_set = set(state)
        for kp in state:
            for k in range(len(E_sp)):
                if k in occ_set or k == kp:
                    continue
                if abs(V[k, kp]) < 1e-30:
                    continue
                # Scatter pair from kp to k
                new_occ = tuple(sorted((occ_set - {kp}) | {k}))
                j = state_to_idx.get(new_occ)
                if j is not None:
                    H[j, i] -= V[k, kp]

    # Symmetrize (should be Hermitian by construction, but enforce)
    H = 0.5 * (H + H.T)
    return H, states


# Verify against W1-1 at N_pair=1
fold_local = np.argmin(np.abs(tau_values - tau_fold))
E_sp_fold = E_sp_all[fold_local]
H_test, states_test = build_canonical_H(E_sp_fold, V_bare_cont, 1)
evals_test = np.linalg.eigh(H_test)[0]
E0_w1_ref = float(d_w1['E0'][fold_idx_full])
print(f"Cross-check N_pair=1 at fold:")
print(f"  This script: E_0 = {evals_test[0]:.10f}")
print(f"  W1-1 ref:    E_0 = {E0_w1_ref:.10f}")
print(f"  Delta: {abs(evals_test[0] - E0_w1_ref):.2e}")
# Note: might differ slightly because tau grid is subsampled

# ============================================================================
# Section 3: ED Sweep at Multiple N_pair
# ============================================================================

print("\n--- Section 3: ED Sweep at N_pair = 1, 2, 3, 4 ---")

# Storage
results = {}
for np_val in N_PAIR_VALUES:
    dim = comb(N_MODES, np_val)
    results[np_val] = {
        'dim': dim,
        'E0': np.zeros(N_tau),
        'E0_all_evals': np.zeros((N_tau, dim)),
        'E_discrete': np.zeros(N_tau),  # Sum of lowest n_pair SP energies (no pairing)
        'E_pair': np.zeros(N_tau),       # Pairing correlation: E_0 - E_discrete
        'gap': np.zeros(N_tau),          # Excitation gap E_1 - E_0
        'occupations': np.zeros((N_tau, N_MODES)),
    }

for np_val in N_PAIR_VALUES:
    dim = results[np_val]['dim']
    print(f"\nN_pair = {np_val}: Fock dim = C(8,{np_val}) = {dim}")

    for t in range(N_tau):
        E_sp = E_sp_all[t]

        # Discrete (no pairing) ground state: fill lowest n_pair levels
        E_discrete = 2.0 * np.sum(np.sort(E_sp)[:np_val])
        results[np_val]['E_discrete'][t] = E_discrete

        # ED with pairing
        H, states = build_canonical_H(E_sp, V_bare_cont, np_val)
        evals, evecs = np.linalg.eigh(H)
        results[np_val]['E0'][t] = evals[0]
        results[np_val]['E0_all_evals'][t] = evals
        results[np_val]['E_pair'][t] = evals[0] - E_discrete
        results[np_val]['gap'][t] = evals[1] - evals[0] if dim > 1 else 0.0

        # Extract occupations from ground state
        psi = evecs[:, 0]
        n_k = np.zeros(N_MODES)
        for si, state in enumerate(states):
            for k in state:
                n_k[k] += psi[si]**2
        results[np_val]['occupations'][t] = n_k

    # Report at fold
    f = fold_local
    print(f"  At fold (tau={tau_values[f]:.4f}):")
    print(f"    E_0 = {results[np_val]['E0'][f]:.8f}")
    print(f"    E_discrete = {results[np_val]['E_discrete'][f]:.8f}")
    print(f"    E_pair = {results[np_val]['E_pair'][f]:.8f}")
    print(f"    Gap = {results[np_val]['gap'][f]:.6f}")
    print(f"    Occupations: {results[np_val]['occupations'][f]}")

# ============================================================================
# Section 4: Strutinsky Shell Corrections at Multiple N_pair
# ============================================================================

print("\n--- Section 4: Strutinsky Shell Corrections ---")


def strutinsky_smooth_energy(E_sp_arr, gamma, n_pair):
    """Strutinsky-smoothed total energy for n_pair pairs.

    Standard Strutinsky prescription (Paper 08):
    1. Smooth the level density with Gaussian of width gamma
    2. Find smoothed Fermi energy for 2*n_pair particles
    3. Integrate E * rho_smooth(E) up to lambda_tilde

    Returns E_smooth(tau) for each tau point.
    """
    N_t = E_sp_arr.shape[0]  # (local)
    n_modes = E_sp_arr.shape[1]  # (local)
    E_smooth = np.zeros(N_t)

    for t in range(N_t):
        E_k = E_sp_arr[t]
        E_min = np.min(E_k) - 5 * gamma
        E_max = np.max(E_k) + 5 * gamma
        n_grid = 2000  # Fine grid for accuracy
        E_grid = np.linspace(E_min, E_max, n_grid)
        dE = E_grid[1] - E_grid[0]

        # Smoothed level density (each level holds 1 pair = 2 particles)
        rho = np.zeros(n_grid)
        for ek in E_k:
            rho += np.exp(-(E_grid - ek)**2 / (2 * gamma**2)) / (gamma * np.sqrt(2 * np.pi))

        # Cumulative pair count
        N_cumul = np.cumsum(rho) * dE

        # Find smoothed Fermi energy for n_pair pairs
        idx_F = np.searchsorted(N_cumul, n_pair)
        idx_F = min(idx_F, n_grid - 1)

        # Smoothed energy sum (factor 2 for Kramers degeneracy: pair energy = 2 * epsilon)
        if idx_F > 0:
            integrand = 2.0 * E_grid[:idx_F+1] * rho[:idx_F+1]
            E_smooth[t] = trapezoid(integrand, E_grid[:idx_F+1])
        else:
            E_smooth[t] = 2.0 * E_grid[0] * n_pair

    return E_smooth


# Compute Strutinsky shell corrections for all N_pair and gamma values
shell_corrections = {}  # [n_pair][gamma] -> dict with arrays

for np_val in N_PAIR_VALUES:
    shell_corrections[np_val] = {}

    for gamma in GAMMA_TEST:
        E_smooth = strutinsky_smooth_energy(E_sp_all, gamma, np_val)

        # Pure single-particle shell correction (no pairing)
        delta_SP = results[np_val]['E_discrete'] - E_smooth

        # Full shell correction (with pairing)
        delta_full = results[np_val]['E0'] - E_smooth

        # Pairing contribution to shell correction
        delta_pair = results[np_val]['E_pair']  # = E_0 - E_discrete

        shell_corrections[np_val][gamma] = {
            'E_smooth': E_smooth,
            'delta_SP': delta_SP,
            'delta_full': delta_full,
            'delta_pair': delta_pair,
        }

    # Report at primary gamma
    g = STRUTINSKY_GAMMA
    f = fold_local
    print(f"\nN_pair = {np_val} (gamma={g}):")
    print(f"  E_discrete_fold = {results[np_val]['E_discrete'][f]:.8f}")
    print(f"  E_smooth_fold   = {shell_corrections[np_val][g]['E_smooth'][f]:.8f}")
    print(f"  E_0_fold        = {results[np_val]['E0'][f]:.8f}")
    print(f"  delta_SP_fold   = {shell_corrections[np_val][g]['delta_SP'][f]:.8f}")
    print(f"  delta_full_fold = {shell_corrections[np_val][g]['delta_full'][f]:.8f}")
    print(f"  delta_pair_fold = {shell_corrections[np_val][g]['delta_pair'][f]:.8f}")

# ============================================================================
# Section 5: Plateau Test for Strutinsky Smoothing
# ============================================================================

print("\n--- Section 5: Strutinsky Plateau Test ---")

# Standard test: shell correction should be insensitive to gamma
# within a plateau region. Check at fold for each N_pair.
print(f"\nShell correction delta_SP at fold (tau={tau_values[fold_local]:.4f}):")
print(f"  {'gamma':<8}", end="")
for np_val in N_PAIR_VALUES:
    print(f"  N={np_val:<8}", end="")
print()

plateau_data = {}
for gamma in GAMMA_TEST:
    print(f"  {gamma:<8.2f}", end="")
    for np_val in N_PAIR_VALUES:
        val = shell_corrections[np_val][gamma]['delta_SP'][fold_local]
        print(f"  {val:<8.6f}", end="")
    print()

# Compute plateau width (fractional variation across gamma test range)
print(f"\nPlateau quality (fractional variation across gamma):")
for np_val in N_PAIR_VALUES:
    vals = [shell_corrections[np_val][g]['delta_SP'][fold_local] for g in GAMMA_TEST]
    mean_val = np.mean(vals)
    spread = (np.max(vals) - np.min(vals)) / (abs(mean_val) + 1e-30)
    print(f"  N_pair={np_val}: mean={mean_val:.6f}, spread={spread:.4f} "
          f"({'GOOD' if spread < 0.3 else 'MARGINAL' if spread < 0.5 else 'POOR'})")

# ============================================================================
# Section 6: Scaling Analysis — |delta_E| vs N_pair
# ============================================================================

print("\n--- Section 6: Scaling Analysis ---")

# Extract amplitude of shell correction oscillation across tau
# Use RMS of delta_SP across the tau sweep as the amplitude measure
g = STRUTINSKY_GAMMA

# Method 1: RMS of delta_SP
rms_SP = np.zeros(len(N_PAIR_VALUES))
# Method 2: Peak-to-peak of delta_SP
pp_SP = np.zeros(len(N_PAIR_VALUES))
# Method 3: |delta_SP| at fold
fold_SP = np.zeros(len(N_PAIR_VALUES))
# Method 4: Same but for delta_full (with pairing)
rms_full = np.zeros(len(N_PAIR_VALUES))
fold_full = np.zeros(len(N_PAIR_VALUES))
# Method 5: |E_pair| at fold
fold_pair = np.zeros(len(N_PAIR_VALUES))

for i, np_val in enumerate(N_PAIR_VALUES):
    d_sp = shell_corrections[np_val][g]['delta_SP']
    d_full = shell_corrections[np_val][g]['delta_full']
    d_pair = shell_corrections[np_val][g]['delta_pair']

    rms_SP[i] = np.sqrt(np.mean(d_sp**2))
    pp_SP[i] = np.max(d_sp) - np.min(d_sp)
    fold_SP[i] = abs(d_sp[fold_local])
    rms_full[i] = np.sqrt(np.mean(d_full**2))
    fold_full[i] = abs(d_full[fold_local])
    fold_pair[i] = abs(d_pair[fold_local])

N_arr = np.array(N_PAIR_VALUES, dtype=float)

# Fit to power law: |delta| = A * N^alpha
def power_law(N, A, alpha):
    return A * N**alpha

def sqrt_law(N, A):
    return A * np.sqrt(N)

print(f"\nAmplitude measures at gamma={g}:")
print(f"  {'N_pair':<8} {'RMS_SP':<12} {'PP_SP':<12} {'|d_SP|_fold':<12} "
      f"{'|d_full|_fold':<14} {'|E_pair|_fold':<14} {'gap':<10}")
for i, np_val in enumerate(N_PAIR_VALUES):
    print(f"  {np_val:<8} {rms_SP[i]:<12.8f} {pp_SP[i]:<12.8f} {fold_SP[i]:<12.8f} "
          f"{fold_full[i]:<14.8f} {fold_pair[i]:<14.8f} "
          f"{results[np_val]['gap'][fold_local]:<10.6f}")

# Gradient ratios (key metric for the gate)
print(f"\nGradient ratios (normalized to N_pair=1):")
for measure_name, measure_arr in [("RMS_SP", rms_SP), ("fold_SP", fold_SP),
                                    ("fold_full", fold_full), ("fold_pair", fold_pair)]:
    if measure_arr[0] > 1e-30:
        ratios = measure_arr / measure_arr[0]
        sqrt_predicted = np.sqrt(N_arr / N_arr[0])
        print(f"  {measure_name}:")
        for i, np_val in enumerate(N_PAIR_VALUES):
            print(f"    N={np_val}: ratio={ratios[i]:.4f}, sqrt pred={sqrt_predicted[i]:.4f}, "
                  f"actual/sqrt={ratios[i]/sqrt_predicted[i]:.4f}")

# Power law fits
print(f"\nPower law fits (|delta| = A * N^alpha):")
fit_results = {}
for measure_name, measure_arr in [("RMS_SP", rms_SP), ("fold_SP", fold_SP),
                                    ("fold_full", fold_full), ("fold_pair", fold_pair)]:
    if np.all(measure_arr > 1e-30):
        try:
            popt, pcov = curve_fit(power_law, N_arr, measure_arr, p0=[measure_arr[0], 0.5])
            perr = np.sqrt(np.diag(pcov))
            print(f"  {measure_name}: A={popt[0]:.6f}+/-{perr[0]:.6f}, "
                  f"alpha={popt[1]:.4f}+/-{perr[1]:.4f}")
            fit_results[measure_name] = {'A': popt[0], 'alpha': popt[1],
                                          'A_err': perr[0], 'alpha_err': perr[1]}

            # Also fit sqrt specifically
            popt_sq, pcov_sq = curve_fit(sqrt_law, N_arr, measure_arr, p0=[measure_arr[0]])
            resid_sq = measure_arr - sqrt_law(N_arr, popt_sq[0])
            resid_pow = measure_arr - power_law(N_arr, *popt)
            chi2_sq = np.sum(resid_sq**2) / (len(N_arr) - 1)
            chi2_pow = np.sum(resid_pow**2) / (len(N_arr) - 2)
            print(f"    sqrt fit: A={popt_sq[0]:.6f}, chi2_red={chi2_sq:.2e}")
            print(f"    power fit: chi2_red={chi2_pow:.2e}")
        except Exception as e:
            print(f"  {measure_name}: fit failed ({e})")
            fit_results[measure_name] = {'A': 0, 'alpha': 0, 'A_err': 0, 'alpha_err': 0}

# ============================================================================
# Section 7: Tau-Resolved Shell Correction Profiles
# ============================================================================

print("\n--- Section 7: Tau-Resolved Shell Correction Profiles ---")

g = STRUTINSKY_GAMMA
print(f"\ndelta_SP(tau) at gamma={g}:")
print(f"  {'tau':<10}", end="")
for np_val in N_PAIR_VALUES:
    print(f"  N={np_val:<10}", end="")
print(f"  {'ratio(4/1)':<12}")

for t in range(N_tau):
    tau = tau_values[t]
    print(f"  {tau:<10.4f}", end="")
    vals = []
    for np_val in N_PAIR_VALUES:
        val = shell_corrections[np_val][g]['delta_SP'][t]
        print(f"  {val:<10.6f}", end="")
        vals.append(val)
    if abs(vals[0]) > 1e-30:
        print(f"  {vals[-1]/vals[0]:<12.4f}")
    else:
        print(f"  {'inf':<12}")

# Also show pairing correlation energy
print(f"\nE_pair(tau) = E_0 - E_discrete:")
print(f"  {'tau':<10}", end="")
for np_val in N_PAIR_VALUES:
    print(f"  N={np_val:<10}", end="")
print()

for t in range(N_tau):
    tau = tau_values[t]
    print(f"  {tau:<10.4f}", end="")
    for np_val in N_PAIR_VALUES:
        val = results[np_val]['E_pair'][t]
        print(f"  {val:<10.6f}", end="")
    print()

# ============================================================================
# Section 8: Nuclear Benchmark Comparison
# ============================================================================

print("\n--- Section 8: Nuclear Benchmark ---")

# Nuclear reference: sd-shell nuclei
# ^18O: 1 neutron pair beyond ^16O core. delta_E_shell ~ 3.2 MeV (from exp masses)
# ^20Ne: 2 neutron pairs. delta_E_shell ~ 3.8 MeV
# ^24Mg: 4 neutron pairs (sd-shell half-filling). delta_E_shell ~ 6.0 MeV
# ^28Si: 6 neutron pairs. delta_E_shell ~ 8.6 MeV (sd-shell closure)
# Enhancement ^28Si/^18O ~ 2.7x for 6x pairs, which is ~6^0.52
# Enhancement ^24Mg/^18O ~ 1.9x for 4x pairs, which is ~4^0.45

# These are rough estimates from mass table (Paper 06 systematics)
nuc_Npair = np.array([1, 2, 4, 6])
nuc_delta = np.array([3.2, 3.8, 6.0, 8.6])  # MeV, approximate
nuc_ratio = nuc_delta / nuc_delta[0]

print("Nuclear sd-shell shell corrections (approximate, from mass table):")
print(f"  ^18O  (N_pair=1): ~{nuc_delta[0]:.1f} MeV (reference)")
print(f"  ^20Ne (N_pair=2): ~{nuc_delta[1]:.1f} MeV (ratio {nuc_ratio[1]:.2f}, "
      f"sqrt pred {np.sqrt(2):.2f})")
print(f"  ^24Mg (N_pair=4): ~{nuc_delta[2]:.1f} MeV (ratio {nuc_ratio[2]:.2f}, "
      f"sqrt pred {np.sqrt(4):.2f})")
print(f"  ^28Si (N_pair=6): ~{nuc_delta[3]:.1f} MeV (ratio {nuc_ratio[3]:.2f}, "
      f"sqrt pred {np.sqrt(6):.2f})")

# Nuclear power law fit
try:
    popt_nuc, pcov_nuc = curve_fit(power_law, nuc_Npair.astype(float), nuc_delta, p0=[3.0, 0.5])
    perr_nuc = np.sqrt(np.diag(pcov_nuc))
    print(f"\nNuclear power law: alpha = {popt_nuc[1]:.3f} +/- {perr_nuc[1]:.3f}")
    print(f"  (sqrt would give alpha = 0.500)")
except:
    pass

# Framework comparison
print(f"\nFramework scaling comparison:")
for measure_name in ["fold_SP", "fold_full", "fold_pair"]:
    if measure_name in fit_results and fit_results[measure_name]['A'] > 0:
        alpha = fit_results[measure_name]['alpha']
        alpha_err = fit_results[measure_name]['alpha_err']
        print(f"  {measure_name}: alpha = {alpha:.3f} +/- {alpha_err:.3f} "
              f"(nuclear: ~0.5)")

# ============================================================================
# Section 9: Occupation Analysis at Half-Filling
# ============================================================================

print("\n--- Section 9: Occupation Analysis ---")

print(f"\nOccupations n_k at fold (tau={tau_values[fold_local]:.4f}):")
print(f"  {'mode':<6} {'E_sp':<12}", end="")
for np_val in N_PAIR_VALUES:
    print(f"  n(N={np_val})", end="")
print()

for k in range(N_MODES):
    print(f"  {k:<6} {E_sp_all[fold_local, k]:<12.6f}", end="")
    for np_val in N_PAIR_VALUES:
        print(f"  {results[np_val]['occupations'][fold_local, k]:<10.6f}", end="")
    print()

# BCS-like check: at half-filling (N=4), do we get u^2 ~ v^2 ~ 0.5?
if 4 in N_PAIR_VALUES:
    occ_half = results[4]['occupations'][fold_local]
    n_half_filled = np.sum(np.abs(occ_half - 0.5) < 0.1)
    print(f"\nHalf-filling BCS check:")
    print(f"  N_pair=4: {n_half_filled}/{N_MODES} modes within 10% of n=0.5")
    print(f"  Mean n_k: {np.mean(occ_half):.4f} (expected: 0.5)")
    print(f"  Max |n_k - 0.5|: {np.max(np.abs(occ_half - 0.5)):.4f}")

# ============================================================================
# Section 10: Plots
# ============================================================================

print("\n--- Section 10: Generating Plots ---")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('HALF-FILLING-SHELL-54: Shell Correction Scaling with N_pair',
             fontsize=14, fontweight='bold')

# Panel (a): delta_SP(tau) for each N_pair
ax = axes[0, 0]
for np_val in N_PAIR_VALUES:
    d_sp = shell_corrections[np_val][STRUTINSKY_GAMMA]['delta_SP']
    ax.plot(tau_values, d_sp, 'o-', label=f'N={np_val}', markersize=4)
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\delta E_{\rm shell}^{\rm SP}$ [M$_{\rm KK}$]')
ax.set_title('(a) SP Shell Correction')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): E_pair(tau) for each N_pair
ax = axes[0, 1]
for np_val in N_PAIR_VALUES:
    ax.plot(tau_values, results[np_val]['E_pair'], 'o-', label=f'N={np_val}', markersize=4)
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$E_{\rm pair}$ [M$_{\rm KK}$]')
ax.set_title('(b) Pairing Correlation Energy')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Scaling — |delta_SP|_fold vs N_pair
ax = axes[0, 2]
N_fine = np.linspace(1, 4, 100)
ax.plot(N_arr, fold_SP, 'ko', markersize=8, label='|$\\delta E^{SP}$| at fold')
ax.plot(N_arr, fold_full, 's', color='red', markersize=7, label='|$\\delta E^{full}$| at fold')
if 'fold_SP' in fit_results and fit_results['fold_SP']['A'] > 0:
    A_sp = fit_results['fold_SP']['A']
    alpha_sp = fit_results['fold_SP']['alpha']
    ax.plot(N_fine, power_law(N_fine, A_sp, alpha_sp), 'k--',
            label=f'$\\propto N^{{{alpha_sp:.2f}}}$')
ax.plot(N_fine, fold_SP[0] * np.sqrt(N_fine), ':', color='blue', alpha=0.5,
        label='$\\propto \\sqrt{N}$')
ax.set_xlabel('$N_{\\rm pair}$')
ax.set_ylabel('|$\\delta E_{\\rm shell}$| [$M_{\\rm KK}$]')
ax.set_title('(c) Shell Correction Scaling')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Excitation gap vs N_pair
ax = axes[1, 0]
gaps = np.array([results[np_val]['gap'][fold_local] for np_val in N_PAIR_VALUES])
ax.bar(N_arr, gaps, width=0.6, color='steelblue', alpha=0.8)
ax.set_xlabel('$N_{\\rm pair}$')
ax.set_ylabel('Gap $E_1 - E_0$ [M$_{\\rm KK}$]')
ax.set_title('(d) Excitation Gap at Fold')
ax.set_xticks(N_PAIR_VALUES)
ax.grid(True, alpha=0.3, axis='y')

# Panel (e): Occupations at half-filling
ax = axes[1, 1]
mode_indices = np.arange(N_MODES)
for np_val in N_PAIR_VALUES:
    ax.plot(mode_indices, results[np_val]['occupations'][fold_local], 'o-',
            label=f'N={np_val}', markersize=6)
ax.axhline(0.5, color='gray', linestyle='--', alpha=0.5, label='half-filled')
ax.set_xlabel('Mode index $k$')
ax.set_ylabel('$n_k$')
ax.set_title('(e) Mode Occupations at Fold')
ax.legend(fontsize=7)
ax.set_xticks(mode_indices)
ax.grid(True, alpha=0.3)

# Panel (f): Plateau test
ax = axes[1, 2]
for np_val in N_PAIR_VALUES:
    vals = [abs(shell_corrections[np_val][g]['delta_SP'][fold_local]) for g in GAMMA_TEST]
    ax.plot(GAMMA_TEST, vals, 'o-', label=f'N={np_val}', markersize=5)
ax.set_xlabel('$\\gamma$ (Strutinsky width)')
ax.set_ylabel('|$\\delta E_{\\rm shell}^{\\rm SP}$|')
ax.set_title('(f) Strutinsky Plateau Test')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(data_dir / 's54_half_filling_shell.png', dpi=150, bbox_inches='tight')
print("  Saved s54_half_filling_shell.png")

# ============================================================================
# Section 11: Save Results
# ============================================================================

print("\n--- Section 11: Saving Results ---")

# Compile into arrays
E0_all = np.array([results[n]['E0'] for n in N_PAIR_VALUES])          # (4, N_tau)
E_disc_all = np.array([results[n]['E_discrete'] for n in N_PAIR_VALUES])
E_pair_all = np.array([results[n]['E_pair'] for n in N_PAIR_VALUES])
gap_all = np.array([results[n]['gap'] for n in N_PAIR_VALUES])
occ_all = np.array([results[n]['occupations'] for n in N_PAIR_VALUES])  # (4, N_tau, 8)
delta_SP_all = np.array([shell_corrections[n][STRUTINSKY_GAMMA]['delta_SP']
                          for n in N_PAIR_VALUES])
delta_full_all = np.array([shell_corrections[n][STRUTINSKY_GAMMA]['delta_full']
                            for n in N_PAIR_VALUES])
E_smooth_all = np.array([shell_corrections[n][STRUTINSKY_GAMMA]['E_smooth']
                           for n in N_PAIR_VALUES])

# Fit results
alpha_SP = fit_results.get('fold_SP', {}).get('alpha', np.nan)
alpha_SP_err = fit_results.get('fold_SP', {}).get('alpha_err', np.nan)
alpha_full = fit_results.get('fold_full', {}).get('alpha', np.nan)
alpha_full_err = fit_results.get('fold_full', {}).get('alpha_err', np.nan)
alpha_pair = fit_results.get('fold_pair', {}).get('alpha', np.nan)
alpha_pair_err = fit_results.get('fold_pair', {}).get('alpha_err', np.nan)

out_path = data_dir / 's54_half_filling_shell.npz'
np.savez(out_path,
         # Grid
         tau_values=tau_values,
         tau_indices=tau_indices,
         N_pair_values=np.array(N_PAIR_VALUES),
         fold_local=fold_local,
         fold_idx_full=fold_idx_full,
         # Energies (4 x N_tau)
         E0=E0_all,
         E_discrete=E_disc_all,
         E_pair=E_pair_all,
         E_smooth=E_smooth_all,
         delta_SP=delta_SP_all,
         delta_full=delta_full_all,
         gap=gap_all,
         occupations=occ_all,
         # Single-particle energies
         E_sp=E_sp_all,
         V_bare_cont=V_bare_cont,
         # Scaling fits
         alpha_SP=alpha_SP,
         alpha_SP_err=alpha_SP_err,
         alpha_full=alpha_full,
         alpha_full_err=alpha_full_err,
         alpha_pair=alpha_pair,
         alpha_pair_err=alpha_pair_err,
         rms_SP=rms_SP,
         fold_SP=fold_SP,
         fold_full=fold_full,
         fold_pair=fold_pair,
         # Strutinsky parameters
         strutinsky_gamma=STRUTINSKY_GAMMA,
         # Gate
         gate_name=np.array(['HALF-FILLING-SHELL-54']),
         gate_verdict=np.array(['INFO']),
         )

print(f"  Saved {out_path}")

# ============================================================================
# Section 12: Gate Verdict
# ============================================================================

print("\n" + "=" * 78)
print("HALF-FILLING-SHELL-54 — GATE VERDICT: INFO")
print("=" * 78)

print(f"\nShell correction scaling exponents:")
print(f"  delta_SP at fold:   alpha = {alpha_SP:.4f} +/- {alpha_SP_err:.4f}")
print(f"  delta_full at fold: alpha = {alpha_full:.4f} +/- {alpha_full_err:.4f}")
print(f"  E_pair at fold:     alpha = {alpha_pair:.4f} +/- {alpha_pair_err:.4f}")
print(f"  Prediction (sqrt): alpha = 0.500")

# Gradient ratios at each N_pair
print(f"\nGradient ratios (key observable for gate):")
for i, np_val in enumerate(N_PAIR_VALUES):
    r_sp = fold_SP[i] / fold_SP[0] if fold_SP[0] > 0 else 0
    r_full = fold_full[i] / fold_full[0] if fold_full[0] > 0 else 0
    r_pair = fold_pair[i] / fold_pair[0] if fold_pair[0] > 0 else 0
    sq = np.sqrt(np_val)
    print(f"  N_pair={np_val}: SP_ratio={r_sp:.4f}, full_ratio={r_full:.4f}, "
          f"pair_ratio={r_pair:.4f}, sqrt_pred={sq:.4f}")

# Nuclear benchmark
print(f"\nNuclear benchmark comparison:")
print(f"  Nuclear sd-shell: alpha ~ 0.5 (^18O -> ^28Si)")
print(f"  Framework SP:     alpha = {alpha_SP:.3f}")
print(f"  Framework full:   alpha = {alpha_full:.3f}")

elapsed = time.time() - t_start
print(f"\nTotal elapsed: {elapsed:.1f}s")
print("DONE.")
