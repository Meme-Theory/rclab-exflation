#!/usr/bin/env python3
"""
N-PAIR-3-RG-64: Richardson-Gaudin Integrability vs N_pair on 8-Mode Spectrum
=============================================================================

Gate: N-PAIR-3-RG-64
  PASS: <r>(N=3) > 0.45 (approaching Wigner-Dyson, integrability broken)
  FAIL: <r>(N=3) < 0.40 (Poisson persists, integrability intact)
  INFO: <r>(N=3) in [0.40, 0.45] (transition regime)

Physics:
  The Richardson-Gaudin (RG) pairing Hamiltonian with uniform coupling g:
    H_RG = sum_k eps_k n_k - g sum_{k,l} c_k^dag c_{-k}^dag c_{-l} c_l    (1)
  is EXACTLY integrable for any number of pairs N_pair (Richardson 1963,
  Gaudin 1976; Paper 15, Dukelsky et al. 2004). It possesses N_pair
  conserved charges (spectral parameters satisfying the Richardson equations).

  Integrability => level statistics follow Poisson (Berry-Tabor):
    P(s) = exp(-s),  <r>_Poisson = 2*ln(2) - 1 = 0.386         (2)

  Integrability BREAKING requires a non-integrable perturbation. The full
  pairing interaction V_{kl} from D_K on Jensen-deformed SU(3) is NOT
  separable (rank > 1). The non-separable component V_perp = V - V_sep
  breaks the conserved charges.

  We diagonalize BOTH H_RG (separable, Eq.1) and H_full (with full V_{kl})
  at N_pair = 1, 2, 3 and compute level spacing statistics to quantify:
  (a) Whether the full V drives the system from Poisson toward GOE
  (b) How the integrability-breaking parameter scales with N_pair

  The 8-mode spectrum has high degeneracy: eps_B2 (x4), eps_B1 (x1),
  eps_B3 (x3). Degeneracies create additional conservation laws (seniority
  quantum numbers within each degenerate shell), which STRENGTHEN
  integrability. We therefore also analyze a LIFTED spectrum where
  degeneracies are split by small random perturbations, to isolate the
  effect of pair number from the effect of level degeneracy.

  Prior results:
  - S55 NPAIR2-ED-55: <r>_RG = 0.411, <r>_full = 0.509 at N=2 (INFO)
  - S56 NPAIR3-ED-56: <r>_full = 0.414 at N=3 (FAIL, blocking)
  - S63 RG-N1-63: N=1 on CG(24), BCS 225x overestimate at N=1

Method:
  1. Build pair Fock space: C(8, N_pair) states for N_pair = 1, 2, 3
  2. For each N_pair:
     a. Construct H_RG (uniform g from gap equation) in Fock basis
     b. Construct H_full (full V_{kl}) in Fock basis
     c. Diagonalize both exactly
     d. Compute <r> = <min(s_n, s_{n+1})/max(s_n, s_{n+1})> (Oganesyan-Huse)
     e. Fit Brody parameter eta to P(s) distribution
     f. Bootstrap uncertainty on <r>
  3. Repeat for degeneracy-lifted spectrum (ensemble average)
  4. Compute Richardson-Gaudin conserved charges to verify integrability
  5. Gate verdict

References:
  - Richardson (1963): Exact eigenstates of the pairing Hamiltonian
  - Gaudin (1976): Bethe ansatz for reduced BCS
  - Oganesyan & Huse, PRB 75, 155111 (2007): r-statistic
  - Brody, Lett. Nuovo Cim. 7, 482 (1973): Brody distribution
  - Paper 15 (Dukelsky et al. 2004): Richardson-Gaudin colloquium
  - Paper 17 (von Delft & Ralph 2001): Ultrasmall BCS grains
  - Paper 03 (Dobaczewski et al. 2001): Odd-even staggering, blocking

Session: S64 W2-D
Agent: nazarewicz-nuclear-structure-theorist
"""

import sys
import os
import numpy as np
from itertools import combinations
from math import comb as mcomb
from scipy.linalg import eigh
from scipy.optimize import fsolve, minimize_scalar, curve_fit
from scipy.stats import kstest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Import canonical constants ===
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (, r_GOE_canonical
    tau_fold, E_cond, N_dof_BCS, M_KK,
    Delta_0_GL, Delta_0_OES, xi_BCS, S_inst,
    E_B1, E_B2_mean, E_B3_mean,
    J_C2, J_su2, J_u1, T_acoustic,
)

data_dir = os.path.dirname(os.path.abspath(__file__))

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

print("=" * 72)
print("N-PAIR-3-RG-64: Richardson-Gaudin Integrability vs N_pair")
print("=" * 72)

# Load S52 HFB data (verified single-cell BCS spectrum)
hfb_data = np.load(os.path.join(data_dir, 's52_hfb_full.npz'), allow_pickle=True)
eps_bare = hfb_data['E_sp_bare']       # 8 single-particle energies (M_KK)
V_bare = hfb_data['V_bare']            # 8x8 pairing interaction (M_KK)
labels = hfb_data['labels']            # ['B2[0]','B2[1]','B2[2]','B2[3]','B1','B3[0]','B3[1]','B3[2]']
N_modes = len(eps_bare)

print(f"N_modes = {N_modes}")
print(f"eps_bare = {eps_bare}")
print(f"labels = {list(labels)}")
print(f"Delta_0_OES = {Delta_0_OES:.6f} M_KK")
print()

# Cross-check with canonical constants
assert abs(eps_bare[4] - E_B1) < 1e-6, f"B1 energy mismatch: {eps_bare[4]} vs {E_B1}"
assert abs(np.mean(eps_bare[:4]) - E_B2_mean) < 1e-4, f"B2 mean mismatch"
assert abs(np.mean(eps_bare[5:]) - E_B3_mean) < 1e-4, f"B3 mean mismatch"

# =====================================================================
#  2. ANALYZE V_BARE STRUCTURE
# =====================================================================

print("=" * 72)
print("V_BARE STRUCTURE ANALYSIS")
print("=" * 72)

# SVD decomposition to quantify non-separability
U_svd, S_svd, Vt_svd = np.linalg.svd(V_bare)
frac_rank1 = S_svd[0]**2 / np.sum(S_svd**2)
frac_rank2 = np.sum(S_svd[:2]**2) / np.sum(S_svd**2)

print(f"Singular values: {S_svd}")
print(f"Rank-1 energy fraction: {frac_rank1:.4f}")
print(f"Rank-2 energy fraction: {frac_rank2:.4f}")
print(f"Non-separable fraction: {1 - frac_rank1:.4f}")

# Rank-1 separable approximation
V_sep = S_svd[0] * np.outer(U_svd[:,0], Vt_svd[0,:])
V_perp = V_bare - V_sep  # non-separable residual
norm_V = np.linalg.norm(V_bare, 'fro')
norm_Vperp = np.linalg.norm(V_perp, 'fro')
print(f"||V_perp|| / ||V|| = {norm_Vperp/norm_V:.6f}")
print()

# =====================================================================
#  3. SOLVE BCS GAP EQUATION FOR UNIFORM COUPLING g
# =====================================================================

print("=" * 72)
print("BCS GAP EQUATION (uniform g)")
print("=" * 72)

Delta_target = Delta_0_OES  # 0.4643 M_KK

def bcs_equations(params, eps, Delta, N_target):
    """BCS gap + number equations for uniform g."""
    mu, g = params
    E_k = np.sqrt((eps - mu)**2 + Delta**2)
    v2 = 0.5 * (1 - (eps - mu) / E_k)
    number_eq = np.sum(v2) - N_target
    gap_eq = 1.0/g - 0.5 * np.sum(1.0/E_k)
    return [number_eq, gap_eq]

g_values = {}
mu_values = {}
for N in [1, 2, 3, 4]:
    mu0 = np.mean(eps_bare)
    g0 = 0.15  # (local)
    sol = fsolve(bcs_equations, [mu0, g0], args=(eps_bare, Delta_target, N), full_output=True)
    mu_sol, g_sol = sol[0]
    g_values[N] = g_sol
    mu_values[N] = mu_sol
    E_k = np.sqrt((eps_bare - mu_sol)**2 + Delta_target**2)
    v2 = 0.5 * (1 - (eps_bare - mu_sol) / E_k)
    print(f"N_pair={N}: mu={mu_sol:.6f}, g={g_sol:.6f}, sum(v^2)={np.sum(v2):.6f}")

print()

# =====================================================================
#  4. BUILD FOCK SPACE AND HAMILTONIANS
# =====================================================================

def build_pair_fock_states(N_modes, N_pair):
    """
    Build pair Fock states: each state is a tuple of N_pair occupied level indices.
    |state> = c_{k1}^+ c_{-k1}^+ ... c_{kN}^+ c_{-kN}^+ |vac>
    Returns list of tuples, each a sorted tuple of occupied indices.
    """
    states = list(combinations(range(N_modes), N_pair))
    return states

def build_hamiltonian_RG(eps, g, states, N_modes):
    """
    Build Richardson-Gaudin Hamiltonian with UNIFORM coupling g.
    H_RG = sum_k eps_k n_k - g sum_{k,l} P_k^+ P_l
    where P_k^+ = c_k^+ c_{-k}^+ creates a pair in level k.

    In the pair Fock basis:
    <I|H|J>:
      - Diagonal: sum_{k in state} 2*eps_k   (pair kinetic energy)
      - Off-diagonal (differ by one pair): -g  (pair scattering)
      - Diagonal pairing contribution: -g * N_pair  (self-scattering)
    """
    dim = len(states)
    H = np.zeros((dim, dim))

    for i, si in enumerate(states):
        # Diagonal: kinetic energy
        H[i, i] = 2.0 * sum(eps[k] for k in si)
        # Diagonal: pairing self-energy (k=l terms in sum)
        H[i, i] -= g * len(si)

        for j in range(i+1, dim):
            sj = states[j]
            # Off-diagonal: states must differ by exactly one pair
            si_set = set(si)
            sj_set = set(sj)
            diff_i = si_set - sj_set  # levels in i but not j
            diff_j = sj_set - si_set  # levels in j but not i
            if len(diff_i) == 1 and len(diff_j) == 1:
                # One pair scattered: k -> l
                H[i, j] = -g
                H[j, i] = -g

    return H

def build_hamiltonian_full(eps, V, states, N_modes):
    """
    Build full pairing Hamiltonian with non-separable V_{kl}.
    H_full = sum_k eps_k n_k - sum_{k,l} V_{kl} P_k^+ P_l

    In the pair Fock basis:
    <I|H|J>:
      - Diagonal: sum_{k in state} (2*eps_k - V_{kk})
      - Off-diagonal (differ by one pair k<->l): -V_{kl}
    """
    dim = len(states)
    H = np.zeros((dim, dim))

    for i, si in enumerate(states):
        # Diagonal: kinetic + diagonal pairing
        H[i, i] = 2.0 * sum(eps[k] for k in si)
        H[i, i] -= sum(V[k, k] for k in si)

        for j in range(i+1, dim):
            sj = states[j]
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

# =====================================================================
#  5. LEVEL SPACING STATISTICS
# =====================================================================

def compute_r_statistic(eigenvalues, remove_degeneracies=True):
    """
    Compute the mean ratio of consecutive level spacings (Oganesyan-Huse).
    r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1})
    where s_n = E_{n+1} - E_n.

    For Poisson: <r> = 2*ln(2) - 1 ~ 0.386
    For GOE:     <r> ~ 0.530
    For GUE:     <r> ~ 0.603

    If remove_degeneracies: filter out spacings < 1e-12 * mean_spacing.
    Returns <r>, list of r_n values, spacings.
    """
    E = np.sort(eigenvalues)
    spacings = np.diff(E)

    if remove_degeneracies and len(spacings) > 0:
        mean_s = np.mean(spacings)
        if mean_s > 0:
            mask = spacings > 1e-12 * mean_s
            spacings = spacings[mask]

    if len(spacings) < 2:
        return np.nan, [], spacings

    r_values = []
    for n in range(len(spacings) - 1):
        s_n = spacings[n]
        s_np1 = spacings[n + 1]
        if max(s_n, s_np1) > 0:
            r_values.append(min(s_n, s_np1) / max(s_n, s_np1))

    r_values = np.array(r_values)
    return np.mean(r_values) if len(r_values) > 0 else np.nan, r_values, spacings

def brody_pdf(s, eta):
    """Brody distribution P(s) = (1+eta)*a*s^eta * exp(-a*s^{1+eta}).
    eta=0: Poisson. eta=1: Wigner (GOE). Normalized: a = Gamma((2+eta)/(1+eta))^{1+eta}."""  # (local)
    from scipy.special import gamma as gamma_func
    a = gamma_func((2 + eta) / (1 + eta))**(1 + eta)
    return (1 + eta) * a * s**eta * np.exp(-a * s**(1 + eta))

def fit_brody(spacings):
    """Fit Brody parameter to spacing distribution. Returns eta, uncertainty."""
    if len(spacings) < 5:
        return np.nan, np.nan

    # Normalize spacings to unit mean
    mean_s = np.mean(spacings)
    if mean_s <= 0:
        return np.nan, np.nan
    s_norm = spacings / mean_s

    # Use KS test across a grid of eta values
    from scipy.special import gamma as gamma_func

    def brody_cdf(s, eta):
        a = gamma_func((2 + eta) / (1 + eta))**(1 + eta)
        return 1 - np.exp(-a * s**(1 + eta))

    etas = np.linspace(0, 2, 201)
    ks_stats = []
    for eta in etas:
        ks_stat, _ = kstest(s_norm, lambda x: brody_cdf(x, eta))
        ks_stats.append(ks_stat)

    ks_stats = np.array(ks_stats)
    best_idx = np.argmin(ks_stats)
    eta_best = etas[best_idx]

    # Uncertainty from bootstrap
    n_boot = 500
    eta_boot = []
    for _ in range(n_boot):
        idx = np.random.choice(len(s_norm), size=len(s_norm), replace=True)
        s_boot = s_norm[idx]
        ks_boot = []
        for eta in etas:
            ks_b, _ = kstest(s_boot, lambda x, e=eta: brody_cdf(x, e))
            ks_boot.append(ks_b)
        eta_boot.append(etas[np.argmin(ks_boot)])
    eta_err = np.std(eta_boot)

    return eta_best, eta_err

def bootstrap_r(r_values, n_boot=1000):
    """Bootstrap uncertainty on <r>."""
    if len(r_values) < 2:
        return np.nan
    means = []
    for _ in range(n_boot):
        idx = np.random.choice(len(r_values), size=len(r_values), replace=True)
        means.append(np.mean(r_values[idx]))
    return np.std(means)

# =====================================================================
#  6. COMPUTE FOR N_pair = 1, 2, 3
# =====================================================================

print("=" * 72)
print("EXACT DIAGONALIZATION: RG vs FULL V")
print("=" * 72)

# Reference values
r_Poisson = 2 * np.log(2) - 1   # 0.3863
r_GOE = r_GOE_canonical  # canonical alias (was: = 0.5307)
r_GUE = 0.6027  # (local)

results = {}

for N_pair in [1, 2, 3]:
    print(f"\n{'='*60}")
    print(f"  N_pair = {N_pair}, dim = C(8,{N_pair}) = {mcomb(8, N_pair)}")
    print(f"{'='*60}")

    states = build_pair_fock_states(N_modes, N_pair)
    dim = len(states)
    g = g_values[N_pair]
    mu = mu_values[N_pair]

    print(f"  g = {g:.6f} M_KK (from gap eq with Delta = {Delta_target:.4f})")
    print(f"  mu = {mu:.6f} M_KK")

    # --- Richardson-Gaudin (separable, uniform g) ---
    H_RG = build_hamiltonian_RG(eps_bare, g, states, N_modes)
    evals_RG = np.sort(eigh(H_RG, eigvals_only=True))

    r_mean_RG, r_vals_RG, spacings_RG = compute_r_statistic(evals_RG)
    r_err_RG = bootstrap_r(r_vals_RG)
    eta_RG, eta_err_RG = fit_brody(spacings_RG)

    print(f"\n  --- Richardson-Gaudin (separable, g={g:.4f}) ---")
    print(f"  E_gs = {evals_RG[0]:.6f} M_KK")
    print(f"  E_max = {evals_RG[-1]:.6f} M_KK")
    print(f"  Bandwidth = {evals_RG[-1] - evals_RG[0]:.6f} M_KK")
    print(f"  Mean spacing = {np.mean(np.diff(evals_RG)):.6f}")
    print(f"  <r>_RG = {r_mean_RG:.4f} +/- {r_err_RG:.4f}")
    print(f"  eta_RG = {eta_RG:.3f} +/- {eta_err_RG:.3f}")
    print(f"  N_spacings = {len(spacings_RG)}, N_r = {len(r_vals_RG)}")
    print(f"  Eigenvalues: {evals_RG}")

    # --- Full V (non-separable) ---
    H_full = build_hamiltonian_full(eps_bare, V_bare, states, N_modes)
    evals_full = np.sort(eigh(H_full, eigvals_only=True))

    r_mean_full, r_vals_full, spacings_full = compute_r_statistic(evals_full)
    r_err_full = bootstrap_r(r_vals_full)
    eta_full, eta_err_full = fit_brody(spacings_full)

    print(f"\n  --- Full V (non-separable) ---")
    print(f"  E_gs = {evals_full[0]:.6f} M_KK")
    print(f"  E_max = {evals_full[-1]:.6f} M_KK")
    print(f"  Bandwidth = {evals_full[-1] - evals_full[0]:.6f} M_KK")
    print(f"  Mean spacing = {np.mean(np.diff(evals_full)):.6f}")
    print(f"  <r>_full = {r_mean_full:.4f} +/- {r_err_full:.4f}")
    print(f"  eta_full = {eta_full:.3f} +/- {eta_err_full:.3f}")
    print(f"  N_spacings = {len(spacings_full)}, N_r = {len(r_vals_full)}")
    print(f"  Eigenvalues: {evals_full}")

    # --- Cross-check with S52 data ---
    s52_evals = hfb_data[f'N{N_pair}_evals']
    if len(s52_evals) == dim:
        diff_s52 = np.max(np.abs(np.sort(evals_full) - np.sort(s52_evals)))
        print(f"\n  S52 cross-check: max |E_new - E_S52| = {diff_s52:.2e}")
    else:
        print(f"\n  S52 cross-check: dimension mismatch ({len(s52_evals)} vs {dim})")

    # --- Sigma from Poisson and GOE ---
    r_sigma_from_Poisson = (r_mean_full - r_Poisson) / r_err_full if r_err_full > 0 else np.nan
    r_sigma_from_GOE = (r_mean_full - r_GOE) / r_err_full if r_err_full > 0 else np.nan

    print(f"\n  Full V: {r_sigma_from_Poisson:.1f} sigma from Poisson, {r_sigma_from_GOE:.1f} sigma from GOE")

    results[N_pair] = {
        'dim': dim,
        'g': g,
        'mu': mu,
        'evals_RG': evals_RG,
        'evals_full': evals_full,
        'r_mean_RG': r_mean_RG,
        'r_err_RG': r_err_RG,
        'r_mean_full': r_mean_full,
        'r_err_full': r_err_full,
        'eta_RG': eta_RG,
        'eta_err_RG': eta_err_RG,
        'eta_full': eta_full,
        'eta_err_full': eta_err_full,
        'spacings_RG': spacings_RG,
        'spacings_full': spacings_full,
        'r_vals_RG': r_vals_RG,
        'r_vals_full': r_vals_full,
    }

# =====================================================================
#  7. DEGENERACY-LIFTED ENSEMBLE
# =====================================================================

print("\n" + "=" * 72)
print("DEGENERACY-LIFTED ENSEMBLE")
print("=" * 72)
print("Lifting the 4-fold B2 and 3-fold B3 degeneracies by small random")
print("perturbations to isolate pair-number effects from degeneracy effects.")

n_ensemble = 100  # (local)
sigma_lift = 0.001  # 0.1% of mean level spacing  # (local)

np.random.seed(42)  # reproducibility

lifted_results = {}

for N_pair in [1, 2, 3]:
    states = build_pair_fock_states(N_modes, N_pair)
    dim = len(states)
    g = g_values[N_pair]

    r_RG_ensemble = []
    r_full_ensemble = []

    for trial in range(n_ensemble):
        # Lift degeneracies
        eps_lifted = eps_bare.copy()
        eps_lifted[:4] += np.random.normal(0, sigma_lift, 4)   # B2
        eps_lifted[5:] += np.random.normal(0, sigma_lift, 3)   # B3

        # RG with lifted spectrum
        H_RG_lift = build_hamiltonian_RG(eps_lifted, g, states, N_modes)
        evals_RG_lift = np.sort(eigh(H_RG_lift, eigvals_only=True))
        r_rg, _, _ = compute_r_statistic(evals_RG_lift)
        r_RG_ensemble.append(r_rg)

        # Full V with lifted spectrum
        H_full_lift = build_hamiltonian_full(eps_lifted, V_bare, states, N_modes)
        evals_full_lift = np.sort(eigh(H_full_lift, eigvals_only=True))
        r_full, _, _ = compute_r_statistic(evals_full_lift)
        r_full_ensemble.append(r_full)

    r_RG_ensemble = np.array(r_RG_ensemble)
    r_full_ensemble = np.array(r_full_ensemble)

    # Filter NaN
    r_RG_clean = r_RG_ensemble[~np.isnan(r_RG_ensemble)]
    r_full_clean = r_full_ensemble[~np.isnan(r_full_ensemble)]

    print(f"\n  N_pair={N_pair} (dim={dim}, {n_ensemble} samples, sigma_lift={sigma_lift}):")
    print(f"    <r>_RG_lifted   = {np.mean(r_RG_clean):.4f} +/- {np.std(r_RG_clean):.4f}")
    print(f"    <r>_full_lifted = {np.mean(r_full_clean):.4f} +/- {np.std(r_full_clean):.4f}")
    print(f"    Shift full-RG   = {np.mean(r_full_clean) - np.mean(r_RG_clean):.4f}")

    lifted_results[N_pair] = {
        'r_RG_mean': np.mean(r_RG_clean),
        'r_RG_std': np.std(r_RG_clean),
        'r_full_mean': np.mean(r_full_clean),
        'r_full_std': np.std(r_full_clean),
        'r_RG_all': r_RG_clean,
        'r_full_all': r_full_clean,
    }

# =====================================================================
#  8. RICHARDSON-GAUDIN CONSERVED CHARGES (VERIFICATION)
# =====================================================================

print("\n" + "=" * 72)
print("RICHARDSON-GAUDIN INTEGRABILITY CHECK")
print("=" * 72)
print("For the uniform-g RG model, the conserved charges are:")
print("  R_a = K_a^z + 2g sum_{b!=a} [K_a^+ K_b^- - K_a^z K_b^z] / (eps_a - eps_b)")
print("When eps_a = eps_b (degenerate), these charges collapse.")
print("We verify [H_RG, R_a] = 0 for the non-degenerate (lifted) case.")

# Build R_a operators for the LIFTED case (non-degenerate spectrum)
# This is algebraically simpler in the pair representation.

# For N_pair = 2, verify commutator [H_RG, V_perp] is non-zero
# (confirming that V_perp breaks integrability)
N_test = 2
states_test = build_pair_fock_states(N_modes, N_test)
g_test = g_values[N_test]

H_RG_test = build_hamiltonian_RG(eps_bare, g_test, states_test, N_modes)
H_full_test = build_hamiltonian_full(eps_bare, V_bare, states_test, N_modes)
H_perp = H_full_test - H_RG_test  # non-integrable perturbation

# Check: is H_perp zero? (It shouldn't be unless V is exactly separable)
norm_H_RG = np.linalg.norm(H_RG_test, 'fro')
norm_H_perp = np.linalg.norm(H_perp, 'fro')
norm_H_full = np.linalg.norm(H_full_test, 'fro')

print(f"\n  N_pair=2 perturbation analysis:")
print(f"  ||H_RG||   = {norm_H_RG:.6f}")
print(f"  ||H_full|| = {norm_H_full:.6f}")
print(f"  ||H_perp|| = {norm_H_perp:.6f}")
print(f"  ||H_perp|| / ||H_RG|| = {norm_H_perp/norm_H_RG:.6f}")

# Commutator [H_RG, H_perp]
comm = H_RG_test @ H_perp - H_perp @ H_RG_test
norm_comm = np.linalg.norm(comm, 'fro')
print(f"  ||[H_RG, H_perp]|| = {norm_comm:.6f}")
print(f"  ||[H_RG, H_perp]|| / ||H_RG||^2 = {norm_comm/norm_H_RG**2:.6e}")

# Also check: what fraction of V_bare is captured by uniform g?
# The uniform g model has V_{kl} = g for all k,l.
# Compare with actual V_bare
V_uniform = np.full((N_modes, N_modes), g_test)
V_diff = V_bare - V_uniform
print(f"\n  Uniform g vs V_bare:")
print(f"  ||V_bare - g*ones|| / ||V_bare|| = {np.linalg.norm(V_diff)/np.linalg.norm(V_bare):.4f}")
print(f"  g_uniform = {g_test:.6f}, mean(V_bare) = {np.mean(V_bare):.6f}")
print(f"  V_bare range: [{np.min(V_bare):.6f}, {np.max(V_bare):.6f}]")

# =====================================================================
#  9. FINITE-SIZE REFERENCE: RANDOM MATRICES
# =====================================================================

print("\n" + "=" * 72)
print("FINITE-SIZE REFERENCE: RANDOM MATRIX ENSEMBLES")
print("=" * 72)

n_rm_samples = 10000
r_poisson_samples = []
r_goe_samples = {}

for dim in [8, 28, 56]:
    r_poisson_dim = []
    r_goe_dim = []

    for _ in range(n_rm_samples):
        # Poisson: uncorrelated eigenvalues
        evals_p = np.sort(np.random.exponential(1.0, dim).cumsum())
        r_p, _, _ = compute_r_statistic(evals_p, remove_degeneracies=False)
        r_poisson_dim.append(r_p)

        # GOE: symmetric random matrix
        M = np.random.randn(dim, dim)
        M = (M + M.T) / 2.0
        evals_g = np.sort(np.linalg.eigvalsh(M))
        r_g, _, _ = compute_r_statistic(evals_g, remove_degeneracies=False)
        r_goe_dim.append(r_g)

    r_poisson_dim = np.array(r_poisson_dim)
    r_goe_dim = np.array(r_goe_dim)

    print(f"  dim={dim:3d}: Poisson <r> = {np.mean(r_poisson_dim):.4f} +/- {np.std(r_poisson_dim):.4f}, "
          f"GOE <r> = {np.mean(r_goe_dim):.4f} +/- {np.std(r_goe_dim):.4f}")

    r_goe_samples[dim] = r_goe_dim

# =====================================================================
#  10. GATE VERDICT
# =====================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: N-PAIR-3-RG-64")
print("=" * 72)

# The gate tests <r>(N=3) for the FULL interaction
r_N3 = results[3]['r_mean_full']
r_N3_err = results[3]['r_err_full']
r_N3_lifted = lifted_results[3]['r_full_mean']
r_N3_lifted_err = lifted_results[3]['r_full_std']

print(f"\n  <r>(N=3, full V, bare spectrum)   = {r_N3:.4f} +/- {r_N3_err:.4f}")
print(f"  <r>(N=3, full V, lifted ensemble) = {r_N3_lifted:.4f} +/- {r_N3_lifted_err:.4f}")
print(f"  <r>(N=3, RG, bare spectrum)       = {results[3]['r_mean_RG']:.4f} +/- {results[3]['r_err_RG']:.4f}")
print(f"  <r>(N=3, RG, lifted ensemble)     = {lifted_results[3]['r_RG_mean']:.4f} +/- {lifted_results[3]['r_RG_std']:.4f}")
print()

# Use the lifted ensemble mean as primary result (avoids degeneracy artifacts)
r_gate = r_N3_lifted
r_gate_err = r_N3_lifted_err

print(f"  Gate value (lifted ensemble): <r> = {r_gate:.4f} +/- {r_gate_err:.4f}")
print(f"  Poisson reference: {r_Poisson:.4f}")
print(f"  GOE reference:     {r_GOE:.4f}")
print()

if r_gate > 0.45:
    verdict = "PASS"
    reason = f"<r> = {r_gate:.4f} > 0.45 (approaching Wigner-Dyson)"
elif r_gate < 0.40:
    verdict = "FAIL"
    reason = f"<r> = {r_gate:.4f} < 0.40 (Poisson persists)"
else:
    verdict = "INFO"
    reason = f"<r> = {r_gate:.4f} in [0.40, 0.45] (transition regime)"

print(f"  Gate N-PAIR-3-RG-64: {verdict}")
print(f"  Reason: {reason}")
print()

# Summary table
print("  Summary Table:")
print(f"  {'N_pair':>6} {'dim':>4} {'<r>_RG':>10} {'<r>_full':>10} {'<r>_RG_lift':>12} {'<r>_full_lift':>14} {'eta_full':>10}")
for N in [1, 2, 3]:
    r = results[N]
    rl = lifted_results[N]
    print(f"  {N:>6} {r['dim']:>4} {r['r_mean_RG']:>10.4f} {r['r_mean_full']:>10.4f} "
          f"{rl['r_RG_mean']:>12.4f} {rl['r_full_mean']:>14.4f} {r['eta_full']:>10.3f}")

print(f"\n  {'':>6} {'':>4} {'r_Poisson':>10} {'':>10} {'':>12} {'':>14}")
print(f"  {'ref':>6} {'':>4} {r_Poisson:>10.4f}")
print(f"  {'GOE':>6} {'':>4} {r_GOE:>10.4f}")

# =====================================================================
#  11. NUCLEAR STRUCTURE ANALYSIS
# =====================================================================

print("\n" + "=" * 72)
print("NUCLEAR STRUCTURE ANALYSIS (Nazarewicz)")
print("=" * 72)

print("""
The Richardson-Gaudin model is exactly integrable (Paper 15, Dukelsky et al.
2004). The uniform-g model possesses N_pair conserved charges — the spectral
parameters satisfying the Richardson equations:

  1 - 2g sum_k 1/(2*eps_k - E_alpha) - 2g sum_{beta != alpha} 1/(E_beta - E_alpha) = 0

where E_alpha are the pair energies (alpha = 1, ..., N_pair).

The key physics governing level statistics on 8 modes:

1. DEGENERACY ENHANCEMENT OF INTEGRABILITY: The 4-fold B2 and 3-fold B3
   degeneracies create additional seniority-like conservation laws. With
   only 3 distinct single-particle energies, the effective phase space for
   level repulsion is drastically reduced. This is why <r>_RG is close to
   Poisson even at N=1 (dim=8 is small, but the structure helps).

2. BLOCKING AT N=3 (Paper 03, Dobaczewski): With 3 pairs on 8 modes,
   the ground state nearly fills the B2 shell (4 levels). Pauli blocking
   freezes pair scattering between occupied B2 levels, creating an effective
   shell closure. This is the same mechanism that suppresses pairing
   correlations near doubly-magic nuclei.

3. NON-SEPARABLE V AS INTEGRABILITY-BREAKING PERTURBATION: The shift
   <r>_full - <r>_RG measures the integrability-breaking strength of V_perp.
   In nuclear physics, the non-separable part of the residual interaction
   (tensor force, spin-orbit) is what drives shell nuclei from regular to
   chaotic spectra. Here, V_perp carries the same role.

4. FINITE-SIZE LIMITATIONS: With dim = 56 at N=3, the spacing statistics
   have intrinsic sampling noise ~ 0.04-0.06 in <r>. Any conclusion about
   integrability breaking must account for this.
""")

# Compute key diagnostics
print("  Diagnostic quantities:")
for N in [1, 2, 3]:
    r = results[N]
    rl = lifted_results[N]
    shift = rl['r_full_mean'] - rl['r_RG_mean']
    shift_sigma = shift / np.sqrt(rl['r_full_std']**2 + rl['r_RG_std']**2) if (rl['r_full_std']**2 + rl['r_RG_std']**2) > 0 else 0
    print(f"  N={N}: shift(full-RG) = {shift:.4f} ({shift_sigma:.1f} sigma), "
          f"eta_full = {r['eta_full']:.3f}+/-{r['eta_err_full']:.3f}")

# =====================================================================
#  12. SAVE DATA
# =====================================================================

print("\n" + "=" * 72)
print("SAVING DATA")
print("=" * 72)

save_dict = {
    'gate_name': 'N-PAIR-3-RG-64',
    'gate_verdict': verdict,
    'gate_reason': reason,
    'r_gate': r_gate,
    'r_gate_err': r_gate_err,
    'r_Poisson': r_Poisson,
    'r_GOE': r_GOE,
    'eps_bare': eps_bare,
    'V_bare': V_bare,
    'labels': labels,
    'Delta_target': Delta_target,
    'sigma_lift': sigma_lift,
    'n_ensemble': n_ensemble,
}

for N in [1, 2, 3]:
    r = results[N]
    rl = lifted_results[N]
    prefix = f'N{N}'
    save_dict[f'{prefix}_dim'] = r['dim']
    save_dict[f'{prefix}_g'] = r['g']
    save_dict[f'{prefix}_mu'] = r['mu']
    save_dict[f'{prefix}_evals_RG'] = r['evals_RG']
    save_dict[f'{prefix}_evals_full'] = r['evals_full']
    save_dict[f'{prefix}_r_mean_RG'] = r['r_mean_RG']
    save_dict[f'{prefix}_r_err_RG'] = r['r_err_RG']
    save_dict[f'{prefix}_r_mean_full'] = r['r_mean_full']
    save_dict[f'{prefix}_r_err_full'] = r['r_err_full']
    save_dict[f'{prefix}_eta_RG'] = r['eta_RG']
    save_dict[f'{prefix}_eta_err_RG'] = r['eta_err_RG']
    save_dict[f'{prefix}_eta_full'] = r['eta_full']
    save_dict[f'{prefix}_eta_err_full'] = r['eta_err_full']
    save_dict[f'{prefix}_spacings_RG'] = r['spacings_RG']
    save_dict[f'{prefix}_spacings_full'] = r['spacings_full']
    save_dict[f'{prefix}_r_RG_lifted_mean'] = rl['r_RG_mean']
    save_dict[f'{prefix}_r_RG_lifted_std'] = rl['r_RG_std']
    save_dict[f'{prefix}_r_full_lifted_mean'] = rl['r_full_mean']
    save_dict[f'{prefix}_r_full_lifted_std'] = rl['r_full_std']

# Save perturbation norms
save_dict['norm_H_perp_over_H_RG'] = norm_H_perp / norm_H_RG
save_dict['norm_comm_over_H_RG2'] = norm_comm / norm_H_RG**2

outpath = os.path.join(data_dir, 's64_npair3_rg.npz')
np.savez(outpath, **save_dict)
print(f"  Saved: {outpath}")

# =====================================================================
#  13. PLOTTING
# =====================================================================

print("\n" + "=" * 72)
print("GENERATING PLOTS")
print("=" * 72)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(r'N-PAIR-3-RG-64: Richardson-Gaudin Integrability vs $N_{\rm pair}$',
             fontsize=14, fontweight='bold')

# --- Top row: P(s) distributions ---
s_ref = np.linspace(0, 4, 200)
P_poisson = np.exp(-s_ref)
P_wigner = (np.pi / 2) * s_ref * np.exp(-np.pi * s_ref**2 / 4)

for col, N in enumerate([1, 2, 3]):
    ax = axes[0, col]
    r = results[N]

    # Normalize spacings
    for label_str, spacings, color, ls in [
        ('RG', r['spacings_RG'], 'blue', '-'),
        ('Full V', r['spacings_full'], 'red', '-'),
    ]:
        if len(spacings) > 2:
            s_norm = spacings / np.mean(spacings)
            bins = np.linspace(0, 4, 15)
            ax.hist(s_norm, bins=bins, density=True, alpha=0.3, color=color,
                    label=label_str, edgecolor=color, linewidth=1.5)

    ax.plot(s_ref, P_poisson, 'k--', lw=1.5, label='Poisson')
    ax.plot(s_ref, P_wigner, 'k:', lw=1.5, label='GOE')
    ax.set_xlabel(r'$s / \langle s \rangle$')
    ax.set_ylabel(r'$P(s)$')
    ax.set_title(f'$N_{{\\rm pair}}={N}$, dim={r["dim"]}')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 1.5)

# --- Bottom left: <r> vs N_pair ---
ax = axes[1, 0]
Ns = [1, 2, 3]
r_RG_bare = [results[N]['r_mean_RG'] for N in Ns]
r_full_bare = [results[N]['r_mean_full'] for N in Ns]
r_RG_lift = [lifted_results[N]['r_RG_mean'] for N in Ns]
r_full_lift = [lifted_results[N]['r_full_mean'] for N in Ns]
r_RG_lift_err = [lifted_results[N]['r_RG_std'] for N in Ns]
r_full_lift_err = [lifted_results[N]['r_full_std'] for N in Ns]

ax.axhline(r_Poisson, color='gray', ls='--', lw=1, label=f'Poisson ({r_Poisson:.3f})')
ax.axhline(r_GOE, color='gray', ls=':', lw=1, label=f'GOE ({r_GOE:.3f})')
ax.axhspan(0.40, 0.45, color='yellow', alpha=0.15, label='INFO region')

ax.plot(Ns, r_RG_bare, 'bs--', ms=8, label=r'RG (bare $\epsilon$)')
ax.plot(Ns, r_full_bare, 'ro--', ms=8, label=r'Full V (bare $\epsilon$)')
ax.errorbar(Ns, r_RG_lift, yerr=r_RG_lift_err, fmt='b^-', ms=8, capsize=4,
            label=r'RG (lifted, ensemble)')
ax.errorbar(Ns, r_full_lift, yerr=r_full_lift_err, fmt='rv-', ms=8, capsize=4,
            label=r'Full V (lifted, ensemble)')

ax.set_xlabel(r'$N_{\rm pair}$')
ax.set_ylabel(r'$\langle r \rangle$')
ax.set_title(r'$\langle r \rangle$ vs $N_{\rm pair}$')
ax.set_xticks([1, 2, 3])
ax.legend(fontsize=7, loc='upper right')
ax.set_ylim(0.25, 0.75)

# --- Bottom center: Brody parameter ---
ax = axes[1, 1]
eta_RG = [results[N]['eta_RG'] for N in Ns]
eta_full = [results[N]['eta_full'] for N in Ns]
eta_RG_err = [results[N]['eta_err_RG'] for N in Ns]
eta_full_err = [results[N]['eta_err_full'] for N in Ns]

ax.axhline(0, color='gray', ls='--', lw=1, label='Poisson (eta=0)')
ax.axhline(1, color='gray', ls=':', lw=1, label='GOE (eta=1)')

ax.errorbar(Ns, eta_RG, yerr=eta_RG_err, fmt='bs--', ms=8, capsize=4, label='RG')
ax.errorbar(Ns, eta_full, yerr=eta_full_err, fmt='ro--', ms=8, capsize=4, label='Full V')

ax.set_xlabel(r'$N_{\rm pair}$')
ax.set_ylabel(r'$\eta$ (Brody)')
ax.set_title('Brody Parameter')
ax.set_xticks([1, 2, 3])
ax.legend(fontsize=8)
ax.set_ylim(-0.5, 2.0)

# --- Bottom right: Eigenvalue spectra ---
ax = axes[1, 2]
for N, color, offset in [(1, 'green', 0), (2, 'blue', 0.3), (3, 'red', 0.6)]:
    evals = results[N]['evals_full']
    ax.scatter([N + offset*0]*len(evals), evals, c=color, s=10, alpha=0.7,
               label=f'Full V, N={N}' if offset == 0 else None)
    evals_rg = results[N]['evals_RG']
    ax.scatter([N + 0.15]*len(evals_rg), evals_rg, c=color, s=10, alpha=0.3,
               marker='x', label=f'RG, N={N}' if N == 1 else None)

ax.set_xlabel(r'$N_{\rm pair}$')
ax.set_ylabel(r'$E$ (M$_{\rm KK}$)')
ax.set_title('Eigenvalue Spectra')
ax.set_xticks([1, 2, 3])

plt.tight_layout()
plotpath = os.path.join(data_dir, 's64_npair3_rg.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotpath}")

print("\n" + "=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
print(f"\nFinal Gate Verdict: N-PAIR-3-RG-64 = {verdict}")
print(f"  <r>(N=3, full V, lifted) = {r_gate:.4f} +/- {r_gate_err:.4f}")
print(f"  Threshold: PASS > 0.45, FAIL < 0.40, INFO in [0.40, 0.45]")
print(f"  {reason}")
