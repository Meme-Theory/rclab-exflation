#!/usr/bin/env python3
"""
SA-LATT-OCC-54: Occupied Lattice Spectral Action
=================================================

Computes the occupation-weighted spectral action S_occ(tau) = sum_k n_k(tau) f(lambda_k^2/Lambda^2)
on the 32-cell Voronoi lattice of SU(3), and compares to the vacuum sum S_vac(tau) = sum_k f(lambda_k^2/Lambda^2).

Physics: On the continuum (992 modes), Weyl's law forces monotonicity of both S_vac and S_occ
(S45 OCC-SPEC-45 FAIL). On the 32-cell lattice, Weyl's law does not apply. The Strutinsky-NCG
decomposition predicts the occupied-only sum can go OPPOSITE to the vacuum sum if the occupation
weights reshape the spectral measure enough.

Method:
  - Load lattice eigenvalues lambda_k(tau) from W0-1 (s54_tb_hamiltonian.npz)
  - Compute BCS occupation n_k(tau) using the BdG approach:
      n_k = v_k^2 = (1/2)(1 - epsilon_k / sqrt(epsilon_k^2 + Delta^2))
    where epsilon_k = lambda_k - mu, and mu is set by half-filling of the lowest N_fill levels.
  - Also compute exact Richardson N_pair=1 occupation for comparison.
  - Evaluate S_occ and S_vac for 3 cutoff functions x 3 Lambda values.
  - Extract Strutinsky shell correction: delta_E_shell = S_occ - S_smooth.

Gate: SA-LATT-OCC-54: PASS if S_occ(tau) has a local minimum in [0.10, 0.30] with barrier > 1%
      for ANY cutoff/Lambda combination. FAIL if monotone for ALL.

Author: Spectral-Geometer (S54 W1-3)
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import brentq
from scipy.ndimage import gaussian_filter1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from canonical_constants import (
    tau_fold, Delta_0_GL, Delta_0_OES, E_cond, E_B1, E_B2_mean, E_B3_mean
)

# =============================================================================
# 0. Load lattice data from W0-1
# =============================================================================
data = np.load(os.path.join(os.path.dirname(__file__), 's54_tb_hamiltonian.npz'), allow_pickle=True)
tau_values = data['tau_values']       # (50,)
eigenvalues = data['eigenvalues']     # (50, 32)
eigenvectors = data['eigenvectors']   # (50, 32, 32)
hamiltonians = data['hamiltonians']   # (50, 32, 32)
cell_dims = data['cell_dims']         # (32,) degeneracies
cell_labels = data['cell_labels']     # (32, 2)
N_tau = len(tau_values)
N_cells = int(data['N_cells'])

print(f"Loaded: {N_tau} tau values, {N_cells} cells")
print(f"tau range: [{tau_values[0]:.3f}, {tau_values[-1]:.3f}]")
print(f"Eigenvalue range: [{eigenvalues.min():.4f}, {eigenvalues.max():.4f}]")

# =============================================================================
# 1. BCS occupation numbers
# =============================================================================
# The lattice has 32 single-particle levels. In the phonon-exflation framework,
# the relevant pairing is in the B2 sector (4-fold, U(2) fundamental).
# For N_pair=1 (one Cooper pair = 2 particles), we need occupation numbers.
#
# Approach 1: BCS mean-field with chemical potential set to accommodate 2 particles.
#   n_k = v_k^2 = (1/2)(1 - (eps_k - mu)/sqrt((eps_k - mu)^2 + Delta^2))
#   sum_k n_k = N_pair * 2 = 2 determines mu.
#
# Approach 2: Exact Richardson for N_pair=1 (simplest case -- one pair).
#   For a single Cooper pair, the ground state is |psi> = sum_k alpha_k c_k^+ c_{-k}^+ |0>
#   where the amplitudes solve the Richardson equation. For N_pair=1, it reduces to:
#   alpha_k propto 1/(2*eps_k - E) where E is the pair energy.
#   Gap equation: 1/g = sum_k 1/(2*eps_k - E)
#
# We implement BOTH and compare.

def bcs_occupation(energies, delta, n_target=2.0):
    """
    Compute BCS occupation numbers n_k = v_k^2 for given single-particle energies.
    Chemical potential mu adjusted so sum_k n_k = n_target.

    Parameters:
        energies: (N,) single-particle energies
        delta: BCS gap parameter
        n_target: target total occupation (= 2 * N_pair)

    Returns:
        n_k: (N,) occupation numbers
        mu: chemical potential
    """
    N = len(energies)
    e_min, e_max = energies.min(), energies.max()

    def occupation_sum(mu):
        eps = energies - mu
        Ek = np.sqrt(eps**2 + delta**2)
        vk2 = 0.5 * (1.0 - eps / Ek)
        return np.sum(vk2) - n_target

    # Bracket mu: at mu -> -inf, all n_k -> 0; at mu -> +inf, all n_k -> 1
    mu_lo = e_min - 10.0 * abs(delta) - 10.0 * (e_max - e_min)
    mu_hi = e_max + 10.0 * abs(delta) + 10.0 * (e_max - e_min)

    try:
        mu = brentq(occupation_sum, mu_lo, mu_hi, xtol=1e-14, maxiter=200)
    except ValueError:
        # If bracketing fails, try wider range
        mu_lo = e_min - 100.0
        mu_hi = e_max + 100.0
        mu = brentq(occupation_sum, mu_lo, mu_hi, xtol=1e-14, maxiter=200)

    eps = energies - mu
    Ek = np.sqrt(eps**2 + delta**2)
    n_k = 0.5 * (1.0 - eps / Ek)
    return n_k, mu


def richardson_occupation_Npair1(energies, g):
    """
    Exact Richardson solution for N_pair=1.

    The pair wavefunction: |psi> = sum_k alpha_k c_{k,up}^+ c_{k,down}^+ |0>
    Normalization: sum_k |alpha_k|^2 = 1
    The pair energy E satisfies: 1/g = sum_k 1/(2*eps_k - E)
    Occupation: n_k = |alpha_k|^2 = [1/(2*eps_k - E)]^2 / sum_j [1/(2*eps_j - E)]^2

    Parameters:
        energies: (N,) single-particle energies (doubly degenerate levels)
        g: pairing strength (positive = attractive)

    Returns:
        n_k: (N,) occupation per level (sum = 1, so 2*n_k particles per level)
        E_pair: pair energy
    """
    N = len(energies)
    eps = energies  # single-particle energies

    # Gap equation: 1/g = sum_k 1/(2*eps_k - E)
    # For attractive pairing (g > 0), E < 2*eps_0 (bound state below lowest pair energy)

    def gap_eq(E):
        return 1.0/g - np.sum(1.0 / (2.0*eps - E))

    # E must be below 2*eps_min for bound state
    E_max = 2.0 * eps.min() - 1e-10
    E_min = E_max - 100.0 * g  # Search well below

    try:
        E_pair = brentq(gap_eq, E_min, E_max, xtol=1e-14, maxiter=500)
    except ValueError:
        # No bound state found -- weak coupling limit
        # Use perturbative estimate
        E_pair = 2.0 * eps.min() - 2.0 * np.exp(-1.0 / (g * N))

    alpha_k = 1.0 / (2.0 * eps - E_pair)
    n_k = alpha_k**2 / np.sum(alpha_k**2)

    return n_k, E_pair


def fermi_occupation(energies, n_target=2.0, beta=1000.0):
    """
    Fermi-Dirac occupation at inverse temperature beta.
    n_k = 1/(exp(beta*(eps_k - mu)) + 1), sum n_k = n_target.
    """
    def occ_sum(mu):
        return np.sum(1.0 / (np.exp(beta * (energies - mu)) + 1.0)) - n_target

    e_min, e_max = energies.min(), energies.max()
    mu = brentq(occ_sum, e_min - 100.0/beta, e_max + 100.0/beta, xtol=1e-14)
    n_k = 1.0 / (np.exp(beta * (energies - mu)) + 1.0)
    return n_k, mu


# =============================================================================
# 2. Cutoff functions
# =============================================================================
def f_exp(x):
    """Exponential cutoff: f(x) = exp(-x)"""
    return np.exp(-x)

def f_sharp(x):
    """Sharp cutoff: f(x) = Theta(1 - x)"""
    return np.where(x <= 1.0, 1.0, 0.0)

def f_poly(x):
    """Polynomial cutoff: f(x) = (1-x)^2 * Theta(1-x)"""
    return np.where(x <= 1.0, (1.0 - x)**2, 0.0)

cutoff_funcs = [f_exp, f_sharp, f_poly]
cutoff_names = ['Exponential', 'Sharp', 'Polynomial']

# Lambda values in units of the bandwidth (use eigenvalue scale, not M_KK)
# The lattice eigenvalues range from ~0 to ~15 (at tau=0) to ~0 to ~6.8 (at fold)
# Lambda should be chosen relative to the eigenvalue scale
Lambda_values = np.array([1.0, 2.0, 5.0])  # in M_KK units
Lambda_labels = ['1.0', '2.0', '5.0']

# =============================================================================
# 3. Determine pairing parameters
# =============================================================================
# For the 32-cell lattice, we need a pairing strength g.
# From the continuum BCS (S35-S37), the relevant gap is Delta_0_GL = 0.77 M_KK.
# The pairing interaction V = g/N where g is extracted from the BCS gap equation.
# On the lattice: Delta = g * sum_k Delta / (2 * E_k) where E_k = sqrt(eps_k^2 + Delta^2).
# This gives: 1 = g * sum_k 1/(2*E_k).
#
# We use two approaches:
# (A) BCS with Delta_0 from canonical constants
# (B) Richardson exact with g extracted from the BCS gap equation at the fold

# First, estimate g from BCS gap equation at fold
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
eps_fold = eigenvalues[fold_idx]
mu_fold_est = (eps_fold[0] + eps_fold[1]) / 2.0  # mu near bottom of band for N=2

# For BCS at fold with Delta = Delta_0_GL:
Delta_BCS = Delta_0_GL  # 0.77 M_KK

# Also consider the OES gap (more physical for N_pair=1)
Delta_OES = Delta_0_OES  # 0.46 M_KK

# We'll scan over a range of Delta values to be thorough
# Use Delta_OES as primary (more appropriate for N_pair=1), Delta_BCS as cross-check
Delta_primary = Delta_OES

print(f"\nPairing parameters:")
print(f"  Delta_BCS (GL) = {Delta_BCS:.4f} M_KK")
print(f"  Delta_OES = {Delta_OES:.4f} M_KK")
print(f"  Using Delta = {Delta_primary:.4f} for primary BCS occupation")

# Extract g from BCS self-consistency at fold
n_bcs_fold, mu_bcs_fold = bcs_occupation(eps_fold, Delta_primary, n_target=2.0)
eps_shifted = eps_fold - mu_bcs_fold
Ek_fold = np.sqrt(eps_shifted**2 + Delta_primary**2)
g_extracted = 1.0 / np.sum(1.0 / (2.0 * Ek_fold))
print(f"  Extracted g = {g_extracted:.6f} (from BCS self-consistency at fold)")
print(f"  mu_BCS(fold) = {mu_bcs_fold:.4f}")
print(f"  n_BCS(fold) sum = {np.sum(n_bcs_fold):.6f}")

# =============================================================================
# 4. Compute occupation numbers at all tau
# =============================================================================
# We compute 3 occupation schemes:
# (A) BCS with Delta_OES
# (B) BCS with Delta_GL
# (C) Richardson exact with extracted g
# (D) Fermi step (T=0 limit, for reference)

occ_bcs_oes = np.zeros((N_tau, N_cells))
occ_bcs_gl = np.zeros((N_tau, N_cells))
occ_richardson = np.zeros((N_tau, N_cells))
occ_fermi = np.zeros((N_tau, N_cells))
mu_bcs_oes_arr = np.zeros(N_tau)
mu_bcs_gl_arr = np.zeros(N_tau)
E_pair_arr = np.zeros(N_tau)

for i in range(N_tau):
    eps_i = eigenvalues[i]

    # (A) BCS with Delta_OES
    occ_bcs_oes[i], mu_bcs_oes_arr[i] = bcs_occupation(eps_i, Delta_OES, n_target=2.0)

    # (B) BCS with Delta_GL
    occ_bcs_gl[i], mu_bcs_gl_arr[i] = bcs_occupation(eps_i, Delta_BCS, n_target=2.0)

    # (C) Richardson exact with N_pair=1
    occ_richardson[i], E_pair_arr[i] = richardson_occupation_Npair1(eps_i, g_extracted)
    # Richardson gives sum = 1 (one pair), so n_k is the pair wavefunction weight
    # For the spectral action, this means the pair occupies levels with weight n_k
    # Total "particle number" = 2 * sum n_k = 2 (one pair)

    # (D) Fermi step (zero T, sharp Fermi surface at n=2)
    occ_fermi[i], _ = fermi_occupation(eps_i, n_target=2.0, beta=10000.0)

# Use BCS with Delta_OES as primary occupation
occupations = occ_bcs_oes

print(f"\nOccupation numbers at fold (tau={tau_values[fold_idx]:.3f}):")
print(f"  BCS(OES) : {occ_bcs_oes[fold_idx, :6]}")
print(f"  BCS(GL)  : {occ_bcs_gl[fold_idx, :6]}")
print(f"  Richardson: {occ_richardson[fold_idx, :6]}")
print(f"  Fermi    : {occ_fermi[fold_idx, :6]}")
print(f"  Sums: BCS(OES)={occ_bcs_oes[fold_idx].sum():.4f}, "
      f"BCS(GL)={occ_bcs_gl[fold_idx].sum():.4f}, "
      f"Rich={occ_richardson[fold_idx].sum():.4f}, "
      f"Fermi={occ_fermi[fold_idx].sum():.4f}")

# =============================================================================
# 5. Compute spectral actions S_occ and S_vac
# =============================================================================
n_cutoffs = len(cutoff_funcs)
n_lambdas = len(Lambda_values)

S_occ = np.zeros((n_cutoffs, n_lambdas, N_tau))     # BCS(OES) primary
S_occ_gl = np.zeros((n_cutoffs, n_lambdas, N_tau))   # BCS(GL) cross-check
S_occ_rich = np.zeros((n_cutoffs, n_lambdas, N_tau))  # Richardson exact
S_occ_fermi = np.zeros((n_cutoffs, n_lambdas, N_tau)) # Fermi step
S_vac = np.zeros((n_cutoffs, n_lambdas, N_tau))

for ic, f_cut in enumerate(cutoff_funcs):
    for il, Lam in enumerate(Lambda_values):
        for it in range(N_tau):
            eps = eigenvalues[it]
            x = eps**2 / Lam**2  # argument of cutoff function: lambda_k^2 / Lambda^2
            fvals = f_cut(x)

            S_vac[ic, il, it] = np.sum(fvals)
            S_occ[ic, il, it] = np.sum(occ_bcs_oes[it] * fvals)
            S_occ_gl[ic, il, it] = np.sum(occ_bcs_gl[it] * fvals)
            S_occ_rich[ic, il, it] = np.sum(2.0 * occ_richardson[it] * fvals)  # factor 2 for pair
            S_occ_fermi[ic, il, it] = np.sum(occ_fermi[it] * fvals)

print(f"\n{'='*70}")
print(f"Spectral Action Results")
print(f"{'='*70}")

# =============================================================================
# 6. Search for minima
# =============================================================================
# Search in [0.10, 0.30] for local minima of S_occ
tau_lo_idx = np.argmin(np.abs(tau_values - 0.10))
tau_hi_idx = np.argmin(np.abs(tau_values - 0.30))
search_slice = slice(tau_lo_idx, tau_hi_idx + 1)

has_minimum = np.zeros((n_cutoffs, n_lambdas), dtype=bool)
minimum_locations = np.full((n_cutoffs, n_lambdas), np.nan)
minimum_values = np.full((n_cutoffs, n_lambdas), np.nan)
barrier_heights = np.full((n_cutoffs, n_lambdas), np.nan)

# Also check other occupation schemes
has_min_gl = np.zeros((n_cutoffs, n_lambdas), dtype=bool)
has_min_rich = np.zeros((n_cutoffs, n_lambdas), dtype=bool)
has_min_fermi = np.zeros((n_cutoffs, n_lambdas), dtype=bool)

def find_minima_in_range(S_arr, tau_arr, idx_lo, idx_hi):
    """
    Find local minima of S_arr in the index range [idx_lo, idx_hi].
    Returns list of (tau_min, S_min, barrier_relative) tuples.
    """
    minima = []
    S_range = S_arr[idx_lo:idx_hi+1]
    tau_range = tau_arr[idx_lo:idx_hi+1]

    for j in range(1, len(S_range) - 1):
        if S_range[j] < S_range[j-1] and S_range[j] < S_range[j+1]:
            # Local minimum found
            S_min = S_range[j]
            tau_min = tau_range[j]
            # Barrier = max of neighbors minus minimum, relative to S_min
            S_left_max = S_range[:j].max() if j > 0 else S_range[0]
            S_right_max = S_range[j+1:].max() if j < len(S_range)-1 else S_range[-1]
            barrier = min(S_left_max - S_min, S_right_max - S_min)
            if abs(S_min) > 1e-15:
                barrier_rel = barrier / abs(S_min)
            else:
                barrier_rel = barrier
            minima.append((tau_min, S_min, barrier_rel, barrier))

    return minima

# Also use numerical derivative to find sign changes
def find_minima_derivative(S_arr, tau_arr, idx_lo, idx_hi):
    """Find minima using centered finite differences."""
    dtau = tau_arr[1] - tau_arr[0]
    dS = np.gradient(S_arr, dtau)
    d2S = np.gradient(dS, dtau)

    minima = []
    for j in range(idx_lo + 1, idx_hi):
        # Zero crossing of dS with positive d2S
        if dS[j-1] < 0 and dS[j+1] > 0 and d2S[j] > 0:
            tau_min = tau_arr[j]
            S_min = S_arr[j]
            # Barrier: max of S to the left minus S_min, similarly right
            S_left = S_arr[idx_lo:j].max() if j > idx_lo else S_arr[idx_lo]
            S_right = S_arr[j+1:idx_hi+1].max() if j < idx_hi else S_arr[idx_hi]
            barrier = min(S_left - S_min, S_right - S_min)
            barrier_rel = barrier / abs(S_min) if abs(S_min) > 1e-15 else barrier
            minima.append((tau_min, S_min, barrier_rel, barrier))

    return minima

print(f"\nMinima search in tau ∈ [{tau_values[tau_lo_idx]:.3f}, {tau_values[tau_hi_idx]:.3f}]:")
print(f"{'Cutoff':<15} {'Lambda':<8} {'BCS(OES)':<25} {'BCS(GL)':<25} {'Richardson':<25} {'Fermi':<25}")
print("-" * 120)

all_occ_arrays = {
    'BCS(OES)': (S_occ, has_minimum),
    'BCS(GL)': (S_occ_gl, has_min_gl),
    'Richardson': (S_occ_rich, has_min_rich),
    'Fermi': (S_occ_fermi, has_min_fermi),
}

for ic in range(n_cutoffs):
    for il in range(n_lambdas):
        results_str = []
        for label, (S_arr, has_arr) in all_occ_arrays.items():
            mins = find_minima_derivative(S_arr[ic, il], tau_values, tau_lo_idx, tau_hi_idx)
            if mins:
                has_arr[ic, il] = True
                best = max(mins, key=lambda x: x[2])  # largest relative barrier
                if label == 'BCS(OES)':
                    minimum_locations[ic, il] = best[0]
                    minimum_values[ic, il] = best[1]
                    barrier_heights[ic, il] = best[2]
                results_str.append(f"tau={best[0]:.3f} b={best[2]:.4f}")
            else:
                results_str.append("monotone")

        print(f"{cutoff_names[ic]:<15} {Lambda_labels[il]:<8} "
              f"{results_str[0]:<25} {results_str[1]:<25} {results_str[2]:<25} {results_str[3]:<25}")

# =============================================================================
# 7. Strutinsky shell correction
# =============================================================================
# delta_E_shell = S_occ - S_smooth
# S_smooth uses Strutinsky-smoothed occupation: convolve n_k with Gaussian of width gamma
# Physically: gamma should be comparable to the level spacing near the Fermi surface

# Compute mean level spacing near Fermi surface
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
spacings = np.diff(eigenvalues[fold_idx])
mean_spacing_low = spacings[:4].mean()
print(f"\nStrutinsky smoothing:")
print(f"  Mean level spacing (lowest 4): {mean_spacing_low:.4f}")
print(f"  Using gamma = {mean_spacing_low:.4f} (1x mean spacing)")

# For Strutinsky: smooth the occupation as a function of energy, not level index
# Standard Strutinsky: n_smooth(eps) = integral of n_k * gaussian(eps - eps_k, gamma)
# But on discrete lattice with fixed levels, we smooth n_k in index space
gamma_strut = 2.0  # smooth over ~2 levels (standard Strutinsky width)  # (local)

shell_corr = np.zeros((n_cutoffs, n_lambdas, N_tau))
S_smooth = np.zeros((n_cutoffs, n_lambdas, N_tau))
has_shell_min = np.zeros((n_cutoffs, n_lambdas), dtype=bool)
shell_min_locations = np.full((n_cutoffs, n_lambdas), np.nan)

for ic in range(n_cutoffs):
    for il in range(n_lambdas):
        for it in range(N_tau):
            eps = eigenvalues[it]
            x = eps**2 / Lambda_values[il]**2
            fvals = cutoff_funcs[ic](x)

            # Strutinsky-smooth the occupation in level space
            n_smooth = gaussian_filter1d(occupations[it], sigma=gamma_strut)
            S_smooth[ic, il, it] = np.sum(n_smooth * fvals)

        shell_corr[ic, il] = S_occ[ic, il] - S_smooth[ic, il]

        # Check if shell correction has a minimum
        mins = find_minima_derivative(shell_corr[ic, il], tau_values, tau_lo_idx, tau_hi_idx)
        if mins:
            has_shell_min[ic, il] = True
            best = max(mins, key=lambda x: abs(x[3]))
            shell_min_locations[ic, il] = best[0]

print(f"\nShell correction minima:")
for ic in range(n_cutoffs):
    for il in range(n_lambdas):
        if has_shell_min[ic, il]:
            print(f"  {cutoff_names[ic]} Lambda={Lambda_labels[il]}: min at tau={shell_min_locations[ic,il]:.3f}")
        else:
            print(f"  {cutoff_names[ic]} Lambda={Lambda_labels[il]}: monotone")

# =============================================================================
# 8. Additional diagnostics
# =============================================================================
print(f"\n{'='*70}")
print(f"Diagnostic Summary")
print(f"{'='*70}")

# Check monotonicity of S_vac
for ic in range(n_cutoffs):
    for il in range(n_lambdas):
        dS = np.diff(S_vac[ic, il])
        mono_dec = np.all(dS <= 1e-10)
        mono_inc = np.all(dS >= -1e-10)
        status = "decreasing" if mono_dec else ("increasing" if mono_inc else "NON-MONOTONE")
        print(f"  S_vac {cutoff_names[ic]:<12} Lambda={Lambda_labels[il]}: {status}")

print()
# Check monotonicity of S_occ
for ic in range(n_cutoffs):
    for il in range(n_lambdas):
        dS = np.diff(S_occ[ic, il])
        mono_dec = np.all(dS <= 1e-10)
        mono_inc = np.all(dS >= -1e-10)
        status = "decreasing" if mono_dec else ("increasing" if mono_inc else "NON-MONOTONE")
        print(f"  S_occ {cutoff_names[ic]:<12} Lambda={Lambda_labels[il]}: {status}")

# Occupation evolution
print(f"\nOccupation of lowest 4 levels vs tau:")
for it in [0, fold_idx, N_tau-1]:
    n = occupations[it, :4]
    print(f"  tau={tau_values[it]:.3f}: n = {n}")

# =============================================================================
# 9. Gate Verdict
# =============================================================================
any_minimum = np.any(has_minimum)
any_minimum_any_scheme = np.any(has_minimum) or np.any(has_min_gl) or np.any(has_min_rich) or np.any(has_min_fermi)

# Check barrier threshold: 1% relative
pass_threshold = 0.01  # (local)
any_pass = False
pass_details = []

for ic in range(n_cutoffs):
    for il in range(n_lambdas):
        if has_minimum[ic, il] and barrier_heights[ic, il] >= pass_threshold:
            any_pass = True
            pass_details.append(
                f"{cutoff_names[ic]} Lambda={Lambda_labels[il]}: "
                f"tau_min={minimum_locations[ic,il]:.3f}, "
                f"barrier={barrier_heights[ic,il]:.4f} ({barrier_heights[ic,il]*100:.2f}%)"
            )

if any_pass:
    gate_verdict = "PASS"
    gate_detail = f"S_occ has minimum with barrier >= 1% in {len(pass_details)} combination(s)"
else:
    gate_verdict = "FAIL"
    if any_minimum:
        max_barrier = np.nanmax(barrier_heights)
        gate_detail = f"S_occ has minima but max barrier = {max_barrier:.4f} ({max_barrier*100:.2f}%) < 1% threshold"
    elif any_minimum_any_scheme:
        gate_detail = "S_occ(BCS-OES) monotone; other schemes show minima (see cross-check)"
    else:
        gate_detail = "S_occ monotone for ALL cutoffs, ALL Lambda, ALL occupation schemes"

print(f"\n{'='*70}")
print(f"GATE: SA-LATT-OCC-54")
print(f"Verdict: {gate_verdict}")
print(f"Detail: {gate_detail}")
if pass_details:
    for d in pass_details:
        print(f"  {d}")
print(f"{'='*70}")

# =============================================================================
# 10. Save results
# =============================================================================
outpath = os.path.join(os.path.dirname(__file__), 's54_sa_latt_occ.npz')
np.savez(outpath,
    # Core results
    tau_values=tau_values,
    S_occ=S_occ,                          # (3, 3, 50)
    S_vac=S_vac,                          # (3, 3, 50)
    occupations=occupations,               # (50, 32)
    has_minimum=has_minimum,               # (3, 3)
    minimum_locations=minimum_locations,   # (3, 3)

    # Extended results
    S_occ_gl=S_occ_gl,
    S_occ_rich=S_occ_rich,
    S_occ_fermi=S_occ_fermi,
    occ_bcs_oes=occ_bcs_oes,
    occ_bcs_gl=occ_bcs_gl,
    occ_richardson=occ_richardson,
    occ_fermi=occ_fermi,

    # Strutinsky
    shell_correction=shell_corr,
    S_smooth=S_smooth,

    # Parameters
    Lambda_values=Lambda_values,
    cutoff_names=np.array(cutoff_names),
    Delta_primary=Delta_primary,
    Delta_BCS=Delta_BCS,
    g_extracted=g_extracted,
    gamma_strutinsky=gamma_strut,

    # Diagnostic
    minimum_values=minimum_values,
    barrier_heights=barrier_heights,
    mu_bcs_oes=mu_bcs_oes_arr,
    mu_bcs_gl=mu_bcs_gl_arr,
    E_pair_richardson=E_pair_arr,

    # Gate
    gate_name=np.array(['SA-LATT-OCC-54']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
print(f"\nData saved: {outpath}")

# =============================================================================
# 11. Plot
# =============================================================================
fig = plt.figure(figsize=(20, 24))
gs = GridSpec(5, 3, figure=fig, hspace=0.35, wspace=0.30)

# --- Row 1: S_vac and S_occ for each cutoff (Lambda=2.0, middle value) ---
il_plot = 1  # Lambda = 2.0

for ic in range(3):
    ax = fig.add_subplot(gs[0, ic])

    # Normalize for comparison
    S_v = S_vac[ic, il_plot]
    S_o = S_occ[ic, il_plot]

    ax.plot(tau_values, S_v, 'b-', linewidth=2, label='$S_{\\mathrm{vac}}$')
    ax.plot(tau_values, S_o, 'r-', linewidth=2, label='$S_{\\mathrm{occ}}$ (BCS)')
    ax.plot(tau_values, S_occ_rich[ic, il_plot], 'g--', linewidth=1.5, label='$S_{\\mathrm{occ}}$ (Rich.)')
    ax.plot(tau_values, S_occ_fermi[ic, il_plot], 'k:', linewidth=1.5, label='$S_{\\mathrm{occ}}$ (Fermi)')

    ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label='fold')

    if has_minimum[ic, il_plot]:
        ax.axvline(minimum_locations[ic, il_plot], color='red', linestyle=':', alpha=0.7)

    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$S(\\tau)$')
    ax.set_title(f'{cutoff_names[ic]}, $\\Lambda = {Lambda_values[il_plot]:.1f}$')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

# --- Row 2: S_occ for all Lambda at each cutoff ---
for ic in range(3):
    ax = fig.add_subplot(gs[1, ic])
    colors = ['tab:blue', 'tab:orange', 'tab:green']
    for il in range(3):
        ax.plot(tau_values, S_occ[ic, il], color=colors[il], linewidth=2,
                label=f'$\\Lambda = {Lambda_values[il]:.1f}$')
        if has_minimum[ic, il]:
            idx = np.argmin(np.abs(tau_values - minimum_locations[ic, il]))
            ax.plot(minimum_locations[ic, il], S_occ[ic, il, idx], 'v',
                    color=colors[il], markersize=10)

    ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$S_{\\mathrm{occ}}(\\tau)$')
    ax.set_title(f'{cutoff_names[ic]}: $S_{{\\mathrm{{occ}}}}$ vs $\\Lambda$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

# --- Row 3: Occupation numbers vs tau ---
ax = fig.add_subplot(gs[2, 0])
for k in range(min(8, N_cells)):
    ax.plot(tau_values, occ_bcs_oes[:, k], label=f'$n_{{{k}}}$ ({cell_labels[k,0]},{cell_labels[k,1]})')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$n_k(\\tau)$ (BCS)')
ax.set_title('BCS Occupation Numbers (lowest 8 levels)')
ax.legend(fontsize=6, ncol=2)
ax.grid(True, alpha=0.3)

ax = fig.add_subplot(gs[2, 1])
for k in range(min(8, N_cells)):
    ax.plot(tau_values, occ_richardson[:, k], label=f'$n_{{{k}}}$ ({cell_labels[k,0]},{cell_labels[k,1]})')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$n_k(\\tau)$ (Richardson)')
ax.set_title('Richardson Occupation (lowest 8 levels)')
ax.legend(fontsize=6, ncol=2)
ax.grid(True, alpha=0.3)

# Chemical potential and pair energy
ax = fig.add_subplot(gs[2, 2])
ax.plot(tau_values, mu_bcs_oes_arr, 'b-', linewidth=2, label='$\\mu$ BCS(OES)')
ax.plot(tau_values, mu_bcs_gl_arr, 'r--', linewidth=1.5, label='$\\mu$ BCS(GL)')
ax.plot(tau_values, E_pair_arr, 'g:', linewidth=2, label='$E_{\\mathrm{pair}}$ (Rich.)')
ax.plot(tau_values, eigenvalues[:, 0], 'k-', alpha=0.5, label='$\\epsilon_0$')
ax.plot(tau_values, eigenvalues[:, 1], 'k--', alpha=0.5, label='$\\epsilon_1$')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Energy (M$_{\\mathrm{KK}}$)')
ax.set_title('Chemical Potential / Pair Energy')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# --- Row 4: Shell correction ---
for ic in range(3):
    ax = fig.add_subplot(gs[3, ic])
    colors = ['tab:blue', 'tab:orange', 'tab:green']
    for il in range(3):
        ax.plot(tau_values, shell_corr[ic, il], color=colors[il], linewidth=2,
                label=f'$\\Lambda = {Lambda_values[il]:.1f}$')
        if has_shell_min[ic, il]:
            idx = np.argmin(np.abs(tau_values - shell_min_locations[ic, il]))
            ax.plot(shell_min_locations[ic, il], shell_corr[ic, il, idx], 'v',
                    color=colors[il], markersize=10)

    ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
    ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$\\delta E_{\\mathrm{shell}}$')
    ax.set_title(f'{cutoff_names[ic]}: Strutinsky Shell Correction')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

# --- Row 5: Normalized ratio S_occ/S_vac ---
for ic in range(3):
    ax = fig.add_subplot(gs[4, ic])
    colors = ['tab:blue', 'tab:orange', 'tab:green']
    for il in range(3):
        with np.errstate(divide='ignore', invalid='ignore'):
            ratio = np.where(S_vac[ic, il] > 1e-15, S_occ[ic, il] / S_vac[ic, il], np.nan)
        ax.plot(tau_values, ratio, color=colors[il], linewidth=2,
                label=f'$\\Lambda = {Lambda_values[il]:.1f}$')

    ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('$S_{\\mathrm{occ}} / S_{\\mathrm{vac}}$')
    ax.set_title(f'{cutoff_names[ic]}: Occupation Ratio')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

fig.suptitle('SA-LATT-OCC-54: Occupied Lattice Spectral Action\n'
             f'32-cell Voronoi lattice, $\\Delta = {Delta_primary:.3f}$ M$_{{\\mathrm{{KK}}}}$, '
             f'Gate: {gate_verdict}', fontsize=14, fontweight='bold', y=0.995)

plotpath = os.path.join(os.path.dirname(__file__), 's54_sa_latt_occ.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
plt.close()
print(f"Plot saved: {plotpath}")

# =============================================================================
# 12. Final summary for working paper
# =============================================================================
print(f"\n{'='*70}")
print(f"RESULTS FOR WORKING PAPER (W1-3)")
print(f"{'='*70}")
print(f"Gate: SA-LATT-OCC-54 — {gate_verdict}")
print(f"Detail: {gate_detail}")
print(f"")
print(f"Key numbers:")
print(f"  32-cell lattice, 50 tau values in [0.00, 0.50]")
print(f"  Cutoffs: Exponential, Sharp, Polynomial")
print(f"  Lambda: 1.0, 2.0, 5.0 M_KK")
print(f"  BCS gap: Delta_OES = {Delta_OES:.4f}, Delta_GL = {Delta_BCS:.4f}")
print(f"  Pairing strength: g = {g_extracted:.6f}")
print(f"  Occupation: BCS(OES) primary, BCS(GL)/Richardson/Fermi cross-checks")
print(f"")
print(f"S_vac monotonicity:")
for ic in range(3):
    for il in range(3):
        dS = np.diff(S_vac[ic, il])
        if np.all(dS >= -1e-10):
            direction = "increasing"
        elif np.all(dS <= 1e-10):
            direction = "decreasing"
        else:
            direction = "NON-MONOTONE"
        print(f"  {cutoff_names[ic]:<12} Lambda={Lambda_labels[il]}: {direction}")

print(f"")
print(f"S_occ(BCS-OES) minima (in [0.10, 0.30]):")
n_min_total = 0
for ic in range(3):
    for il in range(3):
        if has_minimum[ic, il]:
            n_min_total += 1
            print(f"  {cutoff_names[ic]:<12} Lambda={Lambda_labels[il]}: "
                  f"tau_min={minimum_locations[ic,il]:.3f}, "
                  f"barrier={barrier_heights[ic,il]*100:.2f}%")
        else:
            print(f"  {cutoff_names[ic]:<12} Lambda={Lambda_labels[il]}: monotone")

if n_min_total == 0:
    print(f"  => NO minima found in primary BCS(OES)")

# Check across all schemes
print(f"\nCross-check across occupation schemes:")
for label, has_arr in [('BCS(OES)', has_minimum), ('BCS(GL)', has_min_gl),
                       ('Richardson', has_min_rich), ('Fermi', has_min_fermi)]:
    n = np.sum(has_arr)
    print(f"  {label}: {n}/9 combinations show minima")

print(f"\nS_occ/S_vac ratio evolution (Exp, Lambda=2.0):")
for it in [0, fold_idx, N_tau-1]:
    r = S_occ[0, 1, it] / S_vac[0, 1, it] if S_vac[0, 1, it] > 1e-15 else 0
    print(f"  tau={tau_values[it]:.3f}: ratio = {r:.6f}")

print(f"\nStrutinsky shell correction:")
for ic in range(3):
    for il in range(3):
        sc = shell_corr[ic, il]
        print(f"  {cutoff_names[ic]:<12} Lambda={Lambda_labels[il]}: "
              f"range [{sc.min():.6f}, {sc.max():.6f}]")
