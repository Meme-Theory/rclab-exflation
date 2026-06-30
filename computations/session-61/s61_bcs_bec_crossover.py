#!/usr/bin/env python3
"""
s61_bcs_bec_crossover.py — BCS-BEC Crossover Diagnostic (BCS-BEC-61)

Compute the crossover parameter 1/(k_F*a_s) and condensate fraction n_0/N
for the 8-mode BCS system at tau_fold, at each pair number N=1,2,3,4.

Physics:
  The 8-mode system with pairing matrix V_{kl} and single-particle energies
  eps_k is solved by exact diagonalization in the N-pair Fock subspace.

  From the ground-state pair wavefunction |Psi> = sum_{config} c_{config} |config>,
  we extract:
    (a) The pair occupation numbers <n_k> = <Psi| c_k^dag c_{-k}^dag c_{-k} c_k |Psi>
    (b) The anomalous expectation <Delta_k> = <Psi| c_{-k} c_k |Psi_(N-1)>
        (pair-removal amplitude connecting N and N-1 sectors)
    (c) BCS coherence factors: v_k^2 = <n_k>/1 (occupation), u_k^2 = 1 - v_k^2
    (d) Condensate fraction: n_0/N = (1/N)|sum_k u_k v_k|^2
        (ODLRO = largest eigenvalue of pair density matrix)
    (e) 1/(k_F*a_s) from the Leggett crossover formula using mu/E_F

  For N pairs in M=8 modes, the Hilbert space dimension is C(8,N).

Author: Landau-Condensed-Matter-Theorist agent
Session: S61, Wave 5, Task W5-18
Gate: BCS-BEC-61
"""

import numpy as np
from itertools import combinations
from pathlib import Path
import sys
import os

# --- Import canonical constants ---
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    Delta_0_GL, Delta_0_OES, xi_BCS, E_cond, Delta_B3,
    E_B2_mean, N_dof_BCS
)

# --- Load s60 data ---
data_path = Path(__file__).parent / "s60_rg_integrals.npz"
d60 = np.load(data_path, allow_pickle=True)
eps_fold = d60['eps_fold']      # (8,) single-particle energies at tau_fold
V_fold = d60['V_fold']          # (8,8) pairing matrix at tau_fold
tau_fold = float(d60['tau_fold'])

M = 8  # number of modes

print("=" * 70)
print("BCS-BEC CROSSOVER DIAGNOSTIC (BCS-BEC-61)")
print("=" * 70)
print(f"System: {M}-mode BCS, tau_fold = {tau_fold:.6f}")
print(f"eps_fold = {eps_fold}")
print(f"V_fold diagonal = {np.diag(V_fold)}")
print(f"V_fold off-diag mean = {(np.sum(np.abs(V_fold)) - np.sum(np.abs(np.diag(V_fold)))) / (M*(M-1)):.6f}")
print()

# ===========================================================================
#  SECTION 1: Exact Diagonalization in N-pair Fock subspace
# ===========================================================================
# Basis: |config> = |n_1, n_2, ..., n_M> where n_k in {0,1} and sum(n_k) = N
# Hamiltonian: H = sum_k 2*eps_k * n_k - sum_{k,l} V_{kl} * c_k^dag c_{-k}^dag c_{-l} c_l
# The factor 2 on eps accounts for the pair (k, -k) both having energy eps_k.
# The pairing interaction scatters a pair from level l to level k.

def build_hamiltonian(N_pairs):
    """Build exact Hamiltonian in the N-pair subspace of M modes."""
    # Generate all configurations: N_pairs modes occupied out of M
    configs = list(combinations(range(M), N_pairs))
    dim = len(configs)
    config_to_idx = {c: i for i, c in enumerate(configs)}

    H = np.zeros((dim, dim))

    for i, cfg in enumerate(configs):
        # Diagonal: kinetic energy (2*eps_k per occupied pair level)
        E_kin = sum(2.0 * eps_fold[k] for k in cfg)
        H[i, i] += E_kin

        # Diagonal pairing (k=l terms): -V_{kk} for each occupied level
        for k in cfg:
            H[i, i] -= V_fold[k, k]

        # Off-diagonal pairing: scatter pair from level l to level k
        # |cfg> has levels in cfg occupied. Remove l, add k.
        for l in cfg:
            for k in range(M):
                if k == l:
                    continue
                if k in cfg:
                    continue  # k already occupied, Pauli blocked
                # New config: remove l, add k
                new_cfg = tuple(sorted((set(cfg) - {l}) | {k}))
                j = config_to_idx.get(new_cfg)
                if j is not None:
                    H[i, j] -= V_fold[k, l]

    # Symmetrize (should be symmetric by construction, but enforce)
    H = 0.5 * (H + H.T)
    return H, configs


def compute_pair_occupations(psi, configs, N_pairs):
    """Compute <n_k> = probability that mode k is occupied in ground state."""
    n_k = np.zeros(M)
    for i, cfg in enumerate(configs):
        prob = np.abs(psi[i])**2
        for k in cfg:
            n_k[k] += prob
    return n_k


def compute_pair_density_matrix(psi, configs, N_pairs):
    """
    Compute the pair density matrix rho_{kl} = <c_k^dag c_{-k}^dag c_{-l} c_l>.

    For N-pair states, this is:
      rho_{kl} = sum_{configs alpha, beta} psi_alpha^* psi_beta
                 * <alpha| c_k^dag c_{-k}^dag c_{-l} c_l |beta>

    The operator c_k^dag c_{-k}^dag c_{-l} c_l removes a pair from level l
    and creates a pair at level k.

    If k=l: this is the number operator n_k, giving diagonal <n_k>.
    If k!=l: |beta> must have l occupied and k unoccupied.
             The resulting state has l removed and k added.
    """
    config_to_idx = {c: i for i, c in enumerate(configs)}
    rho = np.zeros((M, M), dtype=complex)

    for k in range(M):
        for l in range(M):
            if k == l:
                # Diagonal: <n_k>
                for i, cfg in enumerate(configs):
                    if k in cfg:
                        rho[k, k] += np.abs(psi[i])**2
            else:
                # Off-diagonal: scatter l -> k
                for j, cfg_beta in enumerate(configs):
                    if l not in cfg_beta:
                        continue
                    if k in cfg_beta:
                        continue
                    # Apply: remove l, add k
                    new_cfg = tuple(sorted((set(cfg_beta) - {l}) | {k}))
                    i = config_to_idx.get(new_cfg)
                    if i is not None:
                        rho[k, l] += np.conj(psi[i]) * psi[j]

    return rho


def compute_condensate_fraction_ODLRO(rho_pair, N_pairs):
    """
    Condensate fraction from Off-Diagonal Long-Range Order (ODLRO).

    The condensate fraction is n_0/N = lambda_max / N_pairs
    where lambda_max is the largest eigenvalue of the pair density matrix.

    In the BCS limit: lambda_max ~ Delta/E_F * N (small fraction).
    In the BEC limit: lambda_max ~ N (all pairs in one state, n_0/N -> 1).
    In the crossover: lambda_max ~ O(1) * N.
    """
    eigenvalues = np.linalg.eigvalsh(rho_pair.real)
    lambda_max = eigenvalues[-1]
    n0_over_N = lambda_max / N_pairs
    return n0_over_N, lambda_max, eigenvalues


def compute_crossover_parameter(n_k, N_pairs):
    """
    Compute the BCS-BEC crossover parameter 1/(k_F * a_s) using the
    Leggett approach.

    The key observable is the chemical potential mu relative to E_F.
    In the crossover:
      - BCS side (1/(k_F*a_s) << -1): mu ~ E_F > 0
      - Unitarity (1/(k_F*a_s) = 0): mu ~ 0.59 * E_F
      - BEC side (1/(k_F*a_s) >> 1): mu < 0 (bound state)

    For our discrete system, we define:
      mu = dE/dN = E(N) - E(N-1)  (chemical potential from pair addition)
      E_F = bandwidth / 2 (half the single-particle bandwidth at half-filling)

    The Leggett crossover formula:
      1/(k_F*a_s) = (8/pi*e^2) * (1/Delta_eff) * (mu/Delta_eff - (2/pi)*arctan(mu/Delta_eff))

    But for a discrete system, the more robust diagnostic is:
      mu/E_F:
        > 0.5 -> BCS side
        ~ 0 -> unitarity
        < 0 -> BEC side

    We use the occupation-based Tan contact parameter approach:
      v_k^2 = n_k (occupation of mode k in ground state)
      u_k^2 = 1 - n_k
      The momentum distribution n(k) ~ (C/k^4) at large k defines the contact.
      The crossover is diagnosed by the shape of n_k vs eps_k.
    """
    # For the discrete system, extract effective mu from the step in n_k
    # Sort modes by energy
    idx = np.argsort(eps_fold)
    eps_sorted = eps_fold[idx]
    n_sorted = n_k[idx]

    # Effective Fermi energy: average of highest occupied and lowest unoccupied
    # In a discrete system with N pairs, the "Fermi surface" is between
    # the N-th and (N+1)-th levels
    if N_pairs < M:
        mu_eff = 0.5 * (eps_sorted[N_pairs - 1] + eps_sorted[N_pairs])
    else:
        mu_eff = eps_sorted[-1]

    # Single-particle bandwidth
    W = eps_sorted[-1] - eps_sorted[0]  # (local)
    E_F_eff = W / 2.0  # half-bandwidth as effective Fermi energy

    return mu_eff, E_F_eff


def compute_bcs_coherence_factors(n_k):
    """
    Extract BCS coherence factors from occupation numbers.
    v_k^2 = <n_k>, u_k^2 = 1 - <n_k>
    u_k * v_k = sqrt(<n_k> * (1 - <n_k>))
    """
    v_k_sq = np.clip(n_k, 0, 1)
    u_k_sq = 1.0 - v_k_sq
    uv_k = np.sqrt(np.maximum(v_k_sq * u_k_sq, 0))
    return u_k_sq, v_k_sq, uv_k


# ===========================================================================
#  SECTION 2: Run for N = 1, 2, 3, 4
# ===========================================================================

results = {}

for N_pairs in range(1, 5):
    print(f"\n{'='*60}")
    print(f"  N_pairs = {N_pairs}, Hilbert space dim = C({M},{N_pairs}) = ", end="")

    H, configs = build_hamiltonian(N_pairs)
    dim = len(configs)
    print(f"{dim}")

    # Diagonalize
    eigenvalues, eigenvectors = np.linalg.eigh(H)
    E_gs = eigenvalues[0]
    psi_gs = eigenvectors[:, 0]

    # Ground state degeneracy check
    if dim > 1:
        gap = eigenvalues[1] - eigenvalues[0]
    else:
        gap = np.inf
    print(f"  E_gs = {E_gs:.10f} M_KK")
    print(f"  First excitation gap = {gap:.6f} M_KK")

    # Pair occupations <n_k>
    n_k = compute_pair_occupations(psi_gs, configs, N_pairs)
    print(f"  <n_k> = {n_k}")
    print(f"  sum(<n_k>) = {np.sum(n_k):.6f} (should be {N_pairs})")

    # BCS coherence factors
    u_k_sq, v_k_sq, uv_k = compute_bcs_coherence_factors(n_k)
    print(f"  u_k*v_k = {uv_k}")

    # Pair density matrix (ODLRO)
    rho_pair = compute_pair_density_matrix(psi_gs, configs, N_pairs)

    # Verify: Tr(rho_pair) = N_pairs
    tr_rho = np.trace(rho_pair).real
    print(f"  Tr(rho_pair) = {tr_rho:.6f} (should be {N_pairs})")

    # Condensate fraction
    n0_over_N, lambda_max, eig_rho = compute_condensate_fraction_ODLRO(
        rho_pair, N_pairs
    )
    print(f"  Pair density matrix eigenvalues: {eig_rho}")
    print(f"  lambda_max = {lambda_max:.6f}")
    print(f"  n_0/N = {n0_over_N:.6f}")

    # BCS-style condensate fraction (Yang criterion)
    # n_0^BCS / N = (1/N) * |sum_k u_k v_k|^2
    sum_uv = np.sum(uv_k)
    n0_bcs = sum_uv**2 / N_pairs
    print(f"  n_0^BCS/N = (sum u_k v_k)^2 / N = {n0_bcs:.6f}")

    # Crossover parameter
    mu_eff, E_F_eff = compute_crossover_parameter(n_k, N_pairs)
    print(f"  mu_eff = {mu_eff:.6f} M_KK")
    print(f"  E_F_eff (half-BW) = {E_F_eff:.6f} M_KK")
    print(f"  mu/E_F = {mu_eff/E_F_eff:.6f}")

    # Chemical potential from pair addition/removal energies
    # Also compute E(N-1) if N > 1
    if N_pairs > 1:
        H_m1, configs_m1 = build_hamiltonian(N_pairs - 1)
        evals_m1, _ = np.linalg.eigh(H_m1)
        E_gs_m1 = evals_m1[0]
        mu_add = E_gs - E_gs_m1  # pair addition chemical potential
    else:
        E_gs_m1 = 0.0  # vacuum  # (local)
        mu_add = E_gs

    # Also E(N+1) if N < 4
    if N_pairs < 4:
        H_p1, configs_p1 = build_hamiltonian(N_pairs + 1)
        evals_p1, _ = np.linalg.eigh(H_p1)
        E_gs_p1 = evals_p1[0]
        mu_remove = E_gs_p1 - E_gs
    else:
        mu_remove = None

    print(f"  mu_pair (addition) = E(N)-E(N-1) = {mu_add:.6f}")
    if mu_remove is not None:
        print(f"  mu_pair (removal)  = E(N+1)-E(N) = {mu_remove:.6f}")

    # Leggett crossover parameter from the number equation
    # For a discrete system, 1/(k_F*a_s) is related to mu/Delta:
    # In the continuum Leggett formula:
    #   -1/(k_F*a_s) = integral_0^{E_c} d(eps) rho(eps) [1/sqrt((eps-mu)^2+Delta^2) - 1/eps]
    # For discrete system with levels eps_k:
    #   sum_k [1/sqrt((eps_k - mu)^2 + Delta^2) - 1/eps_k] = -M/(k_F*a_s*rho_0)
    # Use Delta from GL and mu from pair addition

    # Effective gap from the pair density matrix off-diagonal elements
    Delta_eff = np.sqrt(np.sum(np.abs(rho_pair - np.diag(np.diag(rho_pair)))**2) / M)

    # Sharpness of occupation: in BCS limit n_k is a smeared Fermi step,
    # in BEC limit n_k is flat (all modes equally occupied)
    n_k_sorted = n_k[np.argsort(eps_fold)]
    occupation_sharpness = np.max(np.abs(np.diff(n_k_sorted)))

    # Classify regime
    if n0_over_N > 0.8:
        regime = "BEC"
    elif n0_over_N > 0.5:
        regime = "BEC-crossover"
    elif n0_over_N > 0.3:
        regime = "Crossover"
    elif n0_over_N > 0.15:
        regime = "BCS-crossover"
    else:
        regime = "BCS"

    print(f"  Delta_eff (off-diag rho) = {Delta_eff:.6f}")
    print(f"  Occupation sharpness = {occupation_sharpness:.6f}")
    print(f"  REGIME: {regime}")

    results[N_pairs] = {
        'E_gs': E_gs,
        'gap': gap,
        'n_k': n_k,
        'u_k_sq': u_k_sq,
        'v_k_sq': v_k_sq,
        'uv_k': uv_k,
        'rho_pair': rho_pair,
        'eig_rho': eig_rho,
        'lambda_max': lambda_max,
        'n0_over_N': n0_over_N,
        'n0_bcs': n0_bcs,
        'mu_eff': mu_eff,
        'E_F_eff': E_F_eff,
        'mu_add': mu_add,
        'Delta_eff': Delta_eff,
        'occupation_sharpness': occupation_sharpness,
        'regime': regime,
    }

# ===========================================================================
#  SECTION 3: Crossover parameter from Leggett number equation
# ===========================================================================
# For each N, solve the BCS number equation self-consistently:
#   N = sum_k v_k^2 = sum_k (1/2)(1 - (eps_k - mu)/sqrt((eps_k-mu)^2 + Delta^2))
# Given the exact n_k = v_k^2, extract the effective (mu, Delta) that best fits.
# Then 1/(k_F*a_s) from the Leggett gap equation:
#   -1/(k_F*a_s) propto sum_k [1/sqrt((eps_k-mu)^2+Delta^2) - 1/eps_k]

print("\n" + "="*60)
print("  LEGGETT CROSSOVER ANALYSIS")
print("="*60)

for N_pairs in range(1, 5):
    r = results[N_pairs]
    n_k = r['n_k']

    # Fit BCS form: v_k^2 = (1/2)(1 - (eps_k - mu)/E_k) where E_k = sqrt((eps_k-mu)^2 + Delta^2)
    # Minimize ||n_k - v_k^2(mu, Delta)||^2 over (mu, Delta)
    from scipy.optimize import minimize

    def bcs_occupation(params, eps):
        mu, Delta = params
        if Delta < 1e-12:
            Delta = 1e-12
        E_k = np.sqrt((eps - mu)**2 + Delta**2)
        v_sq = 0.5 * (1.0 - (eps - mu) / E_k)
        return v_sq

    def residual(params):
        v_sq = bcs_occupation(params, eps_fold)
        return np.sum((n_k - v_sq)**2)

    # Initial guess: mu at midpoint, Delta from GL
    mu0 = 0.5 * (eps_fold[N_pairs - 1] + eps_fold[min(N_pairs, M-1)])
    Delta0 = Delta_0_GL

    res = minimize(residual, [mu0, Delta0], method='Nelder-Mead',
                   options={'xatol': 1e-12, 'fatol': 1e-15, 'maxiter': 50000})
    mu_fit, Delta_fit = res.x
    Delta_fit = abs(Delta_fit)

    # Quality of BCS fit
    v_sq_fit = bcs_occupation([mu_fit, Delta_fit], eps_fold)
    fit_residual = np.sqrt(np.sum((n_k - v_sq_fit)**2))

    # Effective Fermi energy (half-bandwidth)
    E_F_hw = 0.5 * (eps_fold[-1] - eps_fold[0])

    # Leggett crossover parameter
    # In continuum: -1/(k_F*a_s) = (2/pi) * (mu/Delta) * F(mu/Delta)
    # Simplified: 1/(k_F*a_s) ~ -(2/pi) * mu/Delta at weak coupling
    # Better: use the ratio mu/E_F directly as the diagnostic
    # mu/E_F = 1 -> deep BCS, mu/E_F ~ 0.59 -> unitarity, mu/E_F < 0 -> BEC

    mu_over_EF = mu_fit / E_F_hw if E_F_hw > 0 else 0
    Delta_over_EF = Delta_fit / E_F_hw if E_F_hw > 0 else 0

    # Nozières-Schmitt-Rink (NSR) crossover parameter
    # 1/(k_F*a_s) = -(pi/(2*k_F)) * sum_k [1/E_k - 1/eps_k]
    # For discrete: use sum over modes, normalize by density of states
    E_k_fit = np.sqrt((eps_fold - mu_fit)**2 + Delta_fit**2)
    # Avoid division by zero for eps_fold[0] ~ 0
    eps_reg = np.where(np.abs(eps_fold) < 1e-10, 1e-10, eps_fold)
    leggett_sum = np.sum(1.0 / E_k_fit - 1.0 / eps_reg)

    # k_F from the effective Fermi energy: in 1D-like discrete system,
    # k_F = pi * N_pairs / (M * a_lattice). Use normalized form.
    # The ratio g = leggett_sum is proportional to 1/(k_F*a_s)
    # Normalize: in weak coupling (mu->E_F, Delta->0), leggett_sum -> 0
    # At unitarity: leggett_sum ~ O(1/Delta)
    # Convention: positive = BEC side, negative = BCS side
    inv_kFas = -leggett_sum * E_F_hw / (M * np.pi / 2)

    print(f"\n  N={N_pairs}:")
    print(f"    BCS fit: mu = {mu_fit:.6f}, Delta = {Delta_fit:.6f}")
    print(f"    Fit residual = {fit_residual:.6e}")
    print(f"    mu/E_F = {mu_over_EF:.4f}")
    print(f"    Delta/E_F = {Delta_over_EF:.4f}")
    print(f"    1/(k_F*a_s) = {inv_kFas:.4f}")
    print(f"    n_0/N = {r['n0_over_N']:.4f}")
    print(f"    n_0^BCS/N = {r['n0_bcs']:.4f}")

    results[N_pairs]['mu_fit'] = mu_fit
    results[N_pairs]['Delta_fit'] = Delta_fit
    results[N_pairs]['fit_residual'] = fit_residual
    results[N_pairs]['mu_over_EF'] = mu_over_EF
    results[N_pairs]['Delta_over_EF'] = Delta_over_EF
    results[N_pairs]['inv_kFas'] = inv_kFas


# ===========================================================================
#  SECTION 4: Gate evaluation
# ===========================================================================
print("\n" + "="*60)
print("  GATE EVALUATION: BCS-BEC-61")
print("="*60)

n0_N1 = results[1]['n0_over_N']
n0_N4 = results[4]['n0_over_N']

print(f"  N=1: n_0/N = {n0_N1:.4f} (gate: > 0.8 for BEC)")
print(f"  N=4: n_0/N = {n0_N4:.4f} (gate: 0.3-0.7 for crossover)")

# Check all same regime
regimes = [results[N]['regime'] for N in range(1, 5)]
all_same = len(set(regimes)) == 1

# N-dependence direction
n0_trend = [results[N]['n0_over_N'] for N in range(1, 5)]
monotone_decreasing = all(n0_trend[i] >= n0_trend[i+1] for i in range(3))

if n0_N1 > 0.8 and 0.3 <= n0_N4 <= 0.7:
    gate_verdict = "PASS"
    gate_detail = (f"N=1 BEC (n0/N={n0_N1:.4f}>0.8), "
                   f"N=4 crossover (n0/N={n0_N4:.4f} in [0.3,0.7])")
elif all_same:
    gate_verdict = "FAIL"
    gate_detail = f"All N in same regime: {regimes[0]}"
else:
    gate_verdict = "INFO"
    n0_str = ", ".join(f"N={N}:{results[N]['n0_over_N']:.4f}({results[N]['regime']})"
                       for N in range(1, 5))
    gate_detail = f"Unexpected N-dependence: {n0_str}. Monotone decreasing: {monotone_decreasing}"

print(f"\n  VERDICT: {gate_verdict}")
print(f"  Detail: {gate_detail}")
print(f"  Regimes: {regimes}")
print(f"  n_0/N values: {n0_trend}")
print(f"  Monotone decreasing: {monotone_decreasing}")

# ===========================================================================
#  SECTION 5: Summary table
# ===========================================================================
print("\n" + "="*60)
print("  SUMMARY TABLE")
print("="*60)
print(f"{'N':>3} {'n0/N':>8} {'n0_BCS':>8} {'mu_fit':>10} {'Delta_fit':>10} "
      f"{'mu/EF':>8} {'D/EF':>8} {'1/kFas':>8} {'regime':>15}")
print("-" * 90)
for N in range(1, 5):
    r = results[N]
    print(f"{N:3d} {r['n0_over_N']:8.4f} {r['n0_bcs']:8.4f} {r['mu_fit']:10.6f} "
          f"{r['Delta_fit']:10.6f} {r['mu_over_EF']:8.4f} {r['Delta_over_EF']:8.4f} "
          f"{r['inv_kFas']:8.4f} {r['regime']:>15}")


# ===========================================================================
#  SECTION 6: Plot
# ===========================================================================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# --- Panel (a): n_0/N vs N ---
ax = axes[0, 0]
Ns = [1, 2, 3, 4]
n0_vals = [results[N]['n0_over_N'] for N in Ns]
n0_bcs_vals = [results[N]['n0_bcs'] for N in Ns]
ax.plot(Ns, n0_vals, 'o-', color='C0', markersize=10, linewidth=2, label='ODLRO (eigenvalue)')
ax.plot(Ns, n0_bcs_vals, 's--', color='C1', markersize=8, linewidth=1.5, label='BCS (sum u_k v_k)^2/N')
ax.axhline(0.8, color='gray', linestyle=':', alpha=0.5, label='BEC threshold')
ax.axhline(0.3, color='gray', linestyle='--', alpha=0.5, label='Crossover lower')
ax.axhline(0.7, color='gray', linestyle='--', alpha=0.5, label='Crossover upper')
ax.axhspan(0.3, 0.7, alpha=0.08, color='green', label='Crossover band')
ax.axhspan(0.8, 1.05, alpha=0.08, color='blue', label='BEC band')
ax.set_xlabel('N (pair number)', fontsize=13)
ax.set_ylabel('$n_0/N$ (condensate fraction)', fontsize=13)
ax.set_title('(a) Condensate fraction vs pair number', fontsize=13)
ax.set_xticks(Ns)
ax.set_ylim(-0.05, 1.1)
ax.legend(fontsize=9, loc='best')
ax.grid(True, alpha=0.3)

# --- Panel (b): BCS-BEC crossover map (mu/E_F vs n_0/N) ---
# mu/E_F is the robust crossover diagnostic for discrete systems:
#   BCS: mu/E_F -> 1 (Fermi surface exists)
#   Unitarity: mu/E_F ~ 0.59
#   BEC: mu/E_F -> 0 or negative (bound state, no Fermi surface)
ax = axes[0, 1]
mu_EF_vals = [results[N]['mu_over_EF'] for N in Ns]
colors = ['C0', 'C1', 'C2', 'C3']
for i, N in enumerate(Ns):
    ax.plot(mu_EF_vals[i], n0_vals[i], 'o', color=colors[i], markersize=12,
            label=f'N={N}', zorder=5)
    ax.annotate(f'N={N}', (mu_EF_vals[i], n0_vals[i]),
                textcoords="offset points", xytext=(8, 5), fontsize=11)

# Reference lines
ax.axhline(0.8, color='gray', linestyle=':', alpha=0.4)
ax.axhline(0.3, color='gray', linestyle='--', alpha=0.4)
ax.axhspan(0.3, 0.7, alpha=0.06, color='green')
ax.axvline(0.59, color='black', linestyle='--', alpha=0.4, label='Unitarity $\\mu/E_F=0.59$')
ax.axvspan(0.0, 0.59, alpha=0.06, color='blue', label='BEC side')
ax.axvspan(0.59, 1.2, alpha=0.06, color='red', label='BCS side')

# Draw trajectory arrow
for i in range(len(Ns)-1):
    ax.annotate('', xy=(mu_EF_vals[i+1], n0_vals[i+1]),
                xytext=(mu_EF_vals[i], n0_vals[i]),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.2))

ax.set_xlabel('$\\mu/E_F$ (BCS fit)', fontsize=13)
ax.set_ylabel('$n_0/N$ (ODLRO)', fontsize=13)
ax.set_title('(b) BCS-BEC crossover map', fontsize=13)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.3)
ax.set_xlim(-0.1, 1.3)

# --- Panel (c): Occupation numbers n_k vs eps_k ---
ax = axes[1, 0]
idx_sort = np.argsort(eps_fold)
for N in Ns:
    n_k = results[N]['n_k']
    ax.plot(eps_fold[idx_sort], n_k[idx_sort], 'o-', markersize=7,
            label=f'N={N}', linewidth=1.5)
ax.set_xlabel('$\\epsilon_k$ (M_KK)', fontsize=13)
ax.set_ylabel('$\\langle n_k \\rangle$', fontsize=13)
ax.set_title('(c) Pair occupation numbers', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.05, 1.1)

# --- Panel (d): mu/E_F and Delta/E_F vs N ---
ax = axes[1, 1]
mu_vals = [results[N]['mu_over_EF'] for N in Ns]
Delta_vals = [results[N]['Delta_over_EF'] for N in Ns]
ax.plot(Ns, mu_vals, 'o-', color='C0', markersize=10, linewidth=2, label='$\\mu/E_F$')
ax.plot(Ns, Delta_vals, 's-', color='C2', markersize=10, linewidth=2, label='$\\Delta/E_F$')
ax.axhline(0.59, color='C0', linestyle=':', alpha=0.5, label='Unitarity $\\mu/E_F=0.59$')
ax.axhline(0, color='black', linestyle='-', alpha=0.3)
ax.set_xlabel('N (pair number)', fontsize=13)
ax.set_ylabel('Ratio', fontsize=13)
ax.set_title('(d) Chemical potential and gap ratios', fontsize=13)
ax.set_xticks(Ns)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

fig.suptitle(f'BCS-BEC Crossover Diagnostic (BCS-BEC-61)\n'
             f'8-mode system, tau_fold={tau_fold:.4f}, Gate: {gate_verdict}',
             fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])

plot_path = Path(__file__).parent / "s61_bcs_bec_crossover.png"
plt.savefig(plot_path, dpi=150)
print(f"\nPlot saved: {plot_path}")


# ===========================================================================
#  SECTION 7: Save data
# ===========================================================================
save_path = Path(__file__).parent / "s61_bcs_bec_crossover.npz"

save_dict = {
    'eps_fold': eps_fold,
    'V_fold': V_fold,
    'tau_fold': tau_fold,
    'M': M,
}

for N in range(1, 5):
    r = results[N]
    prefix = f'N{N}_'
    save_dict[prefix + 'E_gs'] = r['E_gs']
    save_dict[prefix + 'gap'] = r['gap']
    save_dict[prefix + 'n_k'] = r['n_k']
    save_dict[prefix + 'eig_rho'] = r['eig_rho']
    save_dict[prefix + 'lambda_max'] = r['lambda_max']
    save_dict[prefix + 'n0_over_N'] = r['n0_over_N']
    save_dict[prefix + 'n0_bcs'] = r['n0_bcs']
    save_dict[prefix + 'mu_fit'] = r['mu_fit']
    save_dict[prefix + 'Delta_fit'] = r['Delta_fit']
    save_dict[prefix + 'mu_over_EF'] = r['mu_over_EF']
    save_dict[prefix + 'Delta_over_EF'] = r['Delta_over_EF']
    save_dict[prefix + 'inv_kFas'] = r['inv_kFas']
    save_dict[prefix + 'regime'] = r['regime']

save_dict['gate_name'] = 'BCS-BEC-61'
save_dict['gate_verdict'] = gate_verdict
save_dict['gate_detail'] = gate_detail

np.savez(save_path, **save_dict)
print(f"Data saved: {save_path}")

print(f"\n{'='*60}")
print(f"  GATE: {gate_verdict}")
print(f"  {gate_detail}")
print(f"{'='*60}")
