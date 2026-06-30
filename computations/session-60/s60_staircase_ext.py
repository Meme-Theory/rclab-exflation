#!/usr/bin/env python3
"""
S60 W1-1: Lambda(N_pair) Staircase Extension to N=3,4
======================================================

Gate: STAIRCASE-EXT-60
  PASS: Lambda_residual decreases monotonically with N
  FAIL: Lambda_residual increases or oscillates
  INFO: Lambda_residual decreases but gap remains > 10^{100} at N=4

Computes single-cell ground state energies E_GS(N) for N=0,1,2,3,4 by exact
diagonalization of the BCS reduced Hamiltonian in the N-pair canonical subspace.

Hamiltonian: H = sum_k 2*eps_k * n_k - sum_{k,l} V_{kl} * P+_k * P_l
where P+_k = c^dag_{k,up} c^dag_{k,down} is the pair creation operator.
The sum over k,l includes the diagonal k=l (Hartree self-pairing).

Two conventions are computed:
  (A) Bare V_fold (no epsilon prefactor) — matches workshop CC analysis
  (B) epsilon_canonical * V_fold — as specified in session plan

The workshop (S59 Mack-Landau) used convention (A) for the CC residual.
Convention (B) gives much weaker pairing and a qualitatively different staircase.

CROSS-CHECK NOTE: The S59 workshop's E_GS(2) = +0.325 came from the s54 code
which EXCLUDED diagonal V[k,k]. The workshop's E_GS(1) = -0.046 INCLUDED diagonal
V[k,k]. This is an inconsistency. This script uses a consistent convention
(diagonal INCLUDED) for all N.

Author: landau-condensed-matter-theorist, Session 60
Date: 2026-03-27
"""

import os
import sys
import time
import numpy as np
from itertools import combinations
from math import comb

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Import canonical constants ===
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import *

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))
t_start = time.time()

# s56_gge_fabric.npz: source of eps_fold, V_fold (same as s54's V_bare_cont)
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
eps_fold = d56['eps_fold']       # 8 single-particle energies at fold
V_fold   = d56['V_fold']        # 8x8 pairing matrix (symmetric)

# s59_epsilon_canonical.npz: coupling constant for convention B
d59 = np.load(os.path.join(data_dir, 's59_epsilon_canonical.npz'), allow_pickle=True)
eps_canonical = float(d59['eps_canonical'])

# s54_ed_sweep.npz: for cross-checking against stored eigenvalues
d54 = np.load(os.path.join(data_dir, 's54_ed_sweep.npz'), allow_pickle=True)
fold_idx_s54 = int(d54['fold_idx'])

N_modes = 8  # (local)

print("=" * 72)
print("S60 W1-1: Lambda(N_pair) Staircase Extension — STAIRCASE-EXT-60")
print("=" * 72)
print(f"N_modes = {N_modes}")
print(f"eps_canonical = {eps_canonical:.8f}")
print(f"tau_fold = {tau_fold}")
print()
print("Single-particle energies at fold (M_KK units):")
for i in range(N_modes):
    print(f"  eps[{i}] = {eps_fold[i]:.10f}")
print()
print(f"V_fold symmetric: max|V - V^T| = {np.max(np.abs(V_fold - V_fold.T)):.2e}")
print(f"V_fold norm: ||V|| = {np.linalg.norm(V_fold):.8f}")
print(f"V_fold diagonal sum: {sum(V_fold[k,k] for k in range(N_modes)):.8f}")


# =====================================================================
#  2. EXACT DIAGONALIZATION ROUTINES
# =====================================================================

def build_canonical_H_BCS(eps_k, V_kl, n_pair, include_diagonal=True):
    """
    Build BCS reduced Hamiltonian in the N-pair canonical Fock space.

    H = sum_k 2*eps_k * n_k - sum_{k,l} V_{kl} * P+_k * P_l

    where P+_k creates a Cooper pair in mode k, n_k = P+_k P_k is pair number.

    Parameters:
        eps_k: array of N single-particle energies
        V_kl: NxN pairing interaction matrix
        n_pair: number of Cooper pairs
        include_diagonal: if True, include V[k,k] terms (standard BCS)

    Returns:
        H: Hamiltonian matrix (dim x dim)
        basis: list of tuples, each tuple contains occupied mode indices
        dim: Fock space dimension = C(N_modes, n_pair)
    """
    N = len(eps_k)
    basis = list(combinations(range(N), n_pair))
    dim = len(basis)
    assert dim == comb(N, n_pair), f"Basis size {dim} != C({N},{n_pair})={comb(N,n_pair)}"

    # Build index map for fast lookup
    basis_set = {occ: i for i, occ in enumerate(basis)}

    H = np.zeros((dim, dim), dtype=np.float64)

    for i, occ_i in enumerate(basis):
        # Kinetic energy: sum_k 2*eps_k for occupied modes
        for k in occ_i:
            H[i, i] += 2.0 * eps_k[k]

        # Diagonal pairing: -V[k,k] for each occupied mode
        if include_diagonal:
            for k in occ_i:
                H[i, i] -= V_kl[k, k]

        # Off-diagonal scattering: scatter pair l -> k
        # This creates pair k and destroys pair l, for k not in occupied, l in occupied
        occ_set = set(occ_i)
        for l in occ_i:
            for k in range(N):
                if k == l:
                    continue
                if k in occ_set:
                    continue
                # New state: replace l with k
                new_occ = tuple(sorted((occ_set - {l}) | {k}))
                j = basis_set.get(new_occ)
                if j is not None:
                    H[j, i] -= V_kl[k, l]

    # Verify Hermiticity
    assert np.allclose(H, H.T, atol=1e-14), \
        f"H not symmetric: max|H-H^T| = {np.max(np.abs(H - H.T)):.2e}"

    return H, basis, dim


# =====================================================================
#  3. COMPUTE STAIRCASE: E_GS(N) for N = 0, 1, 2, 3, 4
# =====================================================================

print("\n" + "=" * 72)
print("  CONVENTION A: Bare V_fold (no epsilon prefactor)")
print("  H = 2*eps_k * n_k - V_{kl} * P+_k * P_l")
print("=" * 72)

E_GS_A = np.zeros(5)  # E(0), E(1), E(2), E(3), E(4)
E_GS_A[0] = 0.0  # Vacuum

eigs_all_A = {}
gs_vecs_A = {}

for N_pair in range(1, 5):
    dim = comb(N_modes, N_pair)
    t0 = time.time()
    H, basis, dim_check = build_canonical_H_BCS(eps_fold, V_fold, N_pair, include_diagonal=True)
    assert dim == dim_check

    evals, evecs = np.linalg.eigh(H)
    E_GS_A[N_pair] = evals[0]
    eigs_all_A[N_pair] = evals
    gs_vecs_A[N_pair] = evecs[:, 0]

    dt = time.time() - t0
    print(f"\n  N = {N_pair}: dim = {dim}, E_GS = {evals[0]:.10f} M_KK, "
          f"gap = {evals[1] - evals[0]:.6f}, t = {dt:.3f}s")
    print(f"    First 5 eigenvalues: {evals[:5]}")

    # Ground state occupation analysis
    occ = np.zeros(N_modes)
    for idx_state, state in enumerate(basis):
        for k in state:
            occ[k] += gs_vecs_A[N_pair][idx_state]**2
    print(f"    GS pair occupations: [{', '.join(f'{o:.4f}' for o in occ)}]")

print("\n--- Convention A: Full staircase ---")
print(f"  E_GS(0) = {E_GS_A[0]:+.10f} M_KK")
print(f"  E_GS(1) = {E_GS_A[1]:+.10f} M_KK")
print(f"  E_GS(2) = {E_GS_A[2]:+.10f} M_KK")
print(f"  E_GS(3) = {E_GS_A[3]:+.10f} M_KK")
print(f"  E_GS(4) = {E_GS_A[4]:+.10f} M_KK")


# =====================================================================
#  3b. CONVENTION B: epsilon_canonical * V_fold
# =====================================================================

print("\n" + "=" * 72)
print(f"  CONVENTION B: epsilon_canonical * V_fold (eps = {eps_canonical:.8f})")
print("  H = 2*eps_k * n_k - eps * V_{kl} * P+_k * P_l")
print("=" * 72)

E_GS_B = np.zeros(5)
E_GS_B[0] = 0.0

V_scaled = eps_canonical * V_fold

for N_pair in range(1, 5):
    dim = comb(N_modes, N_pair)
    H, basis, _ = build_canonical_H_BCS(eps_fold, V_scaled, N_pair, include_diagonal=True)
    evals = np.linalg.eigvalsh(H)
    E_GS_B[N_pair] = evals[0]
    print(f"  N = {N_pair}: dim = {dim}, E_GS = {evals[0]:.10f} M_KK")

print("\n--- Convention B: Full staircase ---")
for n in range(5):
    print(f"  E_GS({n}) = {E_GS_B[n]:+.10f} M_KK")


# =====================================================================
#  3c. CONVENTION A-nodiag: For comparison with s54 stored values
# =====================================================================

print("\n" + "=" * 72)
print("  CROSS-CHECK: Convention A without diagonal (s54 convention)")
print("=" * 72)

E_GS_A_nodiag = np.zeros(5)
E_GS_A_nodiag[0] = 0.0

for N_pair in range(1, 5):
    H, _, _ = build_canonical_H_BCS(eps_fold, V_fold, N_pair, include_diagonal=False)
    evals = np.linalg.eigvalsh(H)
    E_GS_A_nodiag[N_pair] = evals[0]
    print(f"  N = {N_pair}: E_GS = {evals[0]:.10f} M_KK")

# Verify against s54 stored values
s54_eig_sorted = np.sort(d54['all_eigenvalues'][fold_idx_s54])
print(f"\n  s54 stored: E_min = {s54_eig_sorted[0]:.10f} (should be -0.020635)")
print(f"  s54 stored: E[2]  = {s54_eig_sorted[2]:.10f} (should be 0.325040)")
print(f"  Our no-diag: E_GS(1) = {E_GS_A_nodiag[1]:.10f}")
print(f"  Our no-diag: E_GS(2) = {E_GS_A_nodiag[2]:.10f}")
print(f"  Match N=1: {np.isclose(E_GS_A_nodiag[1], s54_eig_sorted[0], atol=1e-8)}")
print(f"  Match N=2: {np.isclose(E_GS_A_nodiag[2], s54_eig_sorted[2], atol=1e-4)}")


# =====================================================================
#  4. CHEMICAL POTENTIAL AND LAMBDA_RESIDUAL
# =====================================================================

print("\n" + "=" * 72)
print("  STAIRCASE TABLE (Convention A: bare V_fold, diagonal included)")
print("=" * 72)

# Forward chemical potential: mu_forward(N) = E(N+1) - E(N)
mu_forward_A = np.array([E_GS_A[n+1] - E_GS_A[n] for n in range(4)])

print(f"\n{'N_pair':>6} | {'E_GS (M_KK)':>14} | {'mu_fwd (M_KK)':>14} |")
print("-" * 52)
for n in range(5):
    mu_str = f"{mu_forward_A[n]:+.8f}" if n < 4 else "    --"
    print(f"{n:>6} | {E_GS_A[n]:+14.8f} | {mu_str:>14} |")

# Lambda_residual(N) = 2*E(N) - E(N-1) - E(N+1) = discrete second derivative
# = -(d^2 E / dN^2) evaluated at N
# Physical meaning: curvature of the equation of state
Lambda_res_A = np.zeros(3)  # N = 1, 2, 3
for i, n in enumerate([1, 2, 3]):
    Lambda_res_A[i] = 2 * E_GS_A[n] - E_GS_A[n-1] - E_GS_A[n+1]

print(f"\n{'N_pair':>6} | {'Lambda_res (M_KK)':>18} | {'|Lambda_res|':>14} |")
print("-" * 52)
for i, n in enumerate([1, 2, 3]):
    print(f"{n:>6} | {Lambda_res_A[i]:+18.10f} | {abs(Lambda_res_A[i]):14.10f} |")

# Check monotonicity of |Lambda_residual|
abs_Lambda_A = np.abs(Lambda_res_A)
mono_decreasing = all(abs_Lambda_A[i+1] < abs_Lambda_A[i] for i in range(len(abs_Lambda_A)-1))
mono_increasing = all(abs_Lambda_A[i+1] > abs_Lambda_A[i] for i in range(len(abs_Lambda_A)-1))
print(f"\n|Lambda_residual| values: {abs_Lambda_A}")
print(f"|Lambda_residual| monotonically decreasing: {mono_decreasing}")
print(f"|Lambda_residual| monotonically increasing: {mono_increasing}")


# =====================================================================
#  5. Q-THEORY EQUILIBRIUM CONDITION
# =====================================================================

print("\n" + "=" * 72)
print("  Q-THEORY EQUILIBRIUM: d(epsilon)/dN = 0")
print("=" * 72)

# The discrete chemical potential mu(N) = E(N+1) - E(N) should cross zero at N_eq
# mu(0) = E(1) - E(0) = E_GS_A[1]
# mu(1) = E(2) - E(1)
# mu(2) = E(3) - E(2)
# mu(3) = E(4) - E(3)

print(f"\nChemical potential mu(N) = E(N+1) - E(N):")
for n in range(4):
    print(f"  mu({n}) = {mu_forward_A[n]:+.8f} M_KK")

# Find zero crossing by linear interpolation
N_eq = None
for n in range(3):
    if mu_forward_A[n] * mu_forward_A[n+1] < 0:
        # Linear interpolation
        N_eq = n + abs(mu_forward_A[n]) / (abs(mu_forward_A[n]) + abs(mu_forward_A[n+1]))
        print(f"\n  mu crosses zero between N={n} and N={n+1}")
        print(f"  N_eq = {N_eq:.6f} (linear interpolation)")
        break

if N_eq is None:
    # Check if minimum of E(N) is at boundary
    N_min = np.argmin(E_GS_A)
    print(f"\n  No zero crossing in mu(N) for N=0..3.")
    print(f"  E_GS minimum at N = {N_min} (E = {E_GS_A[N_min]:.8f})")
    if mu_forward_A[0] < 0 and all(mu_forward_A[n] > 0 for n in range(1, 4)):
        N_eq = 0 + abs(mu_forward_A[0]) / (abs(mu_forward_A[0]) + abs(mu_forward_A[1]))
        print(f"  Equilibrium between N=0 and N=1: N_eq = {N_eq:.6f}")


# =====================================================================
#  6. PHYSICAL UNITS AND CC GAP
# =====================================================================

print("\n" + "=" * 72)
print("  CC GAP IN PHYSICAL UNITS")
print("=" * 72)

# Lambda in physical units: rho_Lambda = |E_GS(N)| * M_KK^4  (in GeV^4)
# The vacuum energy density is E_GS(N_eq) * M_KK^4 / Vol_SU3
# But for the CC residual, we compare |Lambda_res| * M_KK^4 with rho_Lambda_obs

for i, n in enumerate([1, 2, 3]):
    rho_res = abs(Lambda_res_A[i]) * M_KK**4  # GeV^4
    ratio_to_obs = rho_res / rho_Lambda_obs
    log_ratio = np.log10(ratio_to_obs) if ratio_to_obs > 0 else float('nan')
    print(f"  N = {n}: |Lambda_res| * M_KK^4 = {rho_res:.3e} GeV^4")
    print(f"          ratio to Lambda_obs = {ratio_to_obs:.3e} = 10^{{{log_ratio:.1f}}}")

# Also the absolute ground state energy at N_eq
N_min = np.argmin(E_GS_A)
rho_vac = abs(E_GS_A[N_min]) * M_KK**4
ratio_vac = rho_vac / rho_Lambda_obs
print(f"\n  Vacuum at N={N_min}: |E_GS| * M_KK^4 = {rho_vac:.3e} GeV^4")
print(f"  ratio to Lambda_obs = {ratio_vac:.3e} = 10^{{{np.log10(ratio_vac):.1f}}}")


# =====================================================================
#  7. SPECTRAL GAP AND STABILITY ANALYSIS
# =====================================================================

print("\n" + "=" * 72)
print("  SPECTRAL GAPS AND STABILITY")
print("=" * 72)

for N_pair in range(1, 5):
    evals = eigs_all_A[N_pair]
    gap = evals[1] - evals[0]
    # Pair addition/removal energies
    if N_pair < 4:
        E_add = E_GS_A[N_pair + 1] - E_GS_A[N_pair]
    else:
        E_add = float('nan')
    if N_pair > 0:
        E_rem = E_GS_A[N_pair] - E_GS_A[N_pair - 1]
    else:
        E_rem = float('nan')

    print(f"  N = {N_pair}: spectral_gap = {gap:.6f}, "
          f"E_add = {E_add:+.6f}, E_rem = {E_rem:+.6f}")

# Pomeranchuk check: stability requires d^2E/dN^2 > 0 (convexity)
print(f"\n  Convexity check (d^2E/dN^2 > 0 for stability):")
for i, n in enumerate([1, 2, 3]):
    d2E = E_GS_A[n+1] - 2*E_GS_A[n] + E_GS_A[n-1]  # = -Lambda_res
    print(f"    N={n}: d^2E/dN^2 = {d2E:+.8f} ({'CONVEX' if d2E > 0 else 'CONCAVE'})")


# =====================================================================
#  8. GATE VERDICT
# =====================================================================

print("\n" + "=" * 72)
print("  GATE VERDICT: STAIRCASE-EXT-60")
print("=" * 72)

# Gate criterion:
# PASS: Lambda_residual decreases monotonically with N
# FAIL: Lambda_residual increases or oscillates
# INFO: Lambda_residual decreases but gap remains > 10^{100} at N=4

if mono_decreasing:
    # Check gap at N=4
    # The gap is |E_GS(N_min)| * M_KK^4 / Lambda_obs
    if ratio_vac > 1e100:
        verdict = "INFO"
        detail = (f"|Lambda_res| decreasing: "
                  f"{abs_Lambda_A[0]:.6f} > {abs_Lambda_A[1]:.6f} > {abs_Lambda_A[2]:.6f}. "
                  f"But CC gap = 10^{{{np.log10(ratio_vac):.0f}}} >> 10^100.")
    else:
        verdict = "PASS"
        detail = (f"|Lambda_res| monotonically decreasing: "
                  f"{abs_Lambda_A[0]:.6f} > {abs_Lambda_A[1]:.6f} > {abs_Lambda_A[2]:.6f}. "
                  f"CC gap = 10^{{{np.log10(ratio_vac):.0f}}}.")
elif mono_increasing:
    verdict = "FAIL"
    detail = (f"|Lambda_res| monotonically INCREASING: "
              f"{abs_Lambda_A[0]:.6f} < {abs_Lambda_A[1]:.6f} < {abs_Lambda_A[2]:.6f}. "
              f"No approach to observation.")
else:
    # Oscillating
    verdict = "FAIL"
    detail = (f"|Lambda_res| oscillates: "
              f"N=1: {abs_Lambda_A[0]:.6f}, N=2: {abs_Lambda_A[1]:.6f}, N=3: {abs_Lambda_A[2]:.6f}. "
              f"No monotone approach.")

print(f"\n  Verdict: {verdict}")
print(f"  Detail: {detail}")


# =====================================================================
#  9. PLOT
# =====================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("S60 W1-1: Lambda(N_pair) Staircase Extension\n"
             "STAIRCASE-EXT-60 | Convention A: bare V_fold, diagonal included",
             fontsize=13)

# Panel 1: E_GS(N) vs N
ax1 = axes[0, 0]
N_arr = np.arange(5)
ax1.plot(N_arr, E_GS_A, 'ko-', markersize=8, linewidth=2, label='Conv A (bare V, diag)')
ax1.plot(N_arr, E_GS_B, 'bs--', markersize=6, linewidth=1.5, label=f'Conv B (eps={eps_canonical:.4f})')
ax1.plot(N_arr, E_GS_A_nodiag, 'r^:', markersize=6, linewidth=1.5, label='Conv A (no diag, s54)')
ax1.axhline(0, color='gray', linestyle='-', alpha=0.3)
N_min = np.argmin(E_GS_A)
ax1.axvline(N_min, color='green', linestyle='--', alpha=0.5, label=f'N_min={N_min}')
ax1.set_xlabel('N_pair', fontsize=12)
ax1.set_ylabel('E_GS (M_KK)', fontsize=12)
ax1.set_title('Ground State Energy Staircase', fontsize=12)
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.set_xticks(N_arr)

# Panel 2: Chemical potential mu(N) = E(N+1) - E(N)
ax2 = axes[0, 1]
N_mu = np.arange(4)
ax2.plot(N_mu, mu_forward_A, 'ko-', markersize=8, linewidth=2, label='Conv A')
mu_forward_B = np.array([E_GS_B[n+1] - E_GS_B[n] for n in range(4)])
ax2.plot(N_mu, mu_forward_B, 'bs--', markersize=6, linewidth=1.5, label='Conv B')
ax2.axhline(0, color='red', linestyle='-', linewidth=1, alpha=0.7)
if N_eq is not None:
    ax2.axvline(N_eq, color='green', linestyle='--', alpha=0.5, label=f'N_eq={N_eq:.2f}')
ax2.set_xlabel('N_pair', fontsize=12)
ax2.set_ylabel('mu = E(N+1) - E(N) (M_KK)', fontsize=12)
ax2.set_title('Chemical Potential (q-theory EoS)', fontsize=12)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_xticks(N_mu)

# Panel 3: Lambda_residual(N) = 2E(N) - E(N-1) - E(N+1)
ax3 = axes[1, 0]
N_Lambda = np.array([1, 2, 3])
Lambda_B = np.array([2*E_GS_B[n] - E_GS_B[n-1] - E_GS_B[n+1] for n in [1,2,3]])
ax3.plot(N_Lambda, Lambda_res_A, 'ko-', markersize=8, linewidth=2, label='Lambda_res (Conv A)')
ax3.plot(N_Lambda, Lambda_B, 'bs--', markersize=6, linewidth=1.5, label='Lambda_res (Conv B)')
ax3.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax3.set_xlabel('N_pair', fontsize=12)
ax3.set_ylabel('Lambda_residual (M_KK)', fontsize=12)
ax3.set_title('Discrete Second Derivative (CC Residual)', fontsize=12)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)
ax3.set_xticks(N_Lambda)

# Panel 4: |Lambda_residual| on log scale
ax4 = axes[1, 1]
abs_Lambda_B = np.abs(Lambda_B)
ax4.semilogy(N_Lambda, abs_Lambda_A, 'ko-', markersize=8, linewidth=2, label='|Lambda_res| (Conv A)')
ax4.semilogy(N_Lambda, abs_Lambda_B, 'bs--', markersize=6, linewidth=1.5, label='|Lambda_res| (Conv B)')
# Add horizontal line for Lambda_obs in M_KK units
Lambda_obs_MKK = rho_Lambda_obs / M_KK**4
ax4.axhline(Lambda_obs_MKK, color='red', linestyle='--', alpha=0.7,
            label=f'Lambda_obs/M_KK^4 = {Lambda_obs_MKK:.1e}')
ax4.set_xlabel('N_pair', fontsize=12)
ax4.set_ylabel('|Lambda_residual| (M_KK)', fontsize=12)
ax4.set_title('|Lambda_residual| vs N (log scale)', fontsize=12)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3, which='both')
ax4.set_xticks(N_Lambda)

plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's60_staircase_ext.png'), dpi=150, bbox_inches='tight')
print(f"\nPlot saved: s60_staircase_ext.png")


# =====================================================================
#  10. SAVE DATA
# =====================================================================

# Convention B staircase quantities
mu_forward_B = np.array([E_GS_B[n+1] - E_GS_B[n] for n in range(4)])
Lambda_res_B = np.array([2*E_GS_B[n] - E_GS_B[n-1] - E_GS_B[n+1] for n in [1,2,3]])

np.savez(
    os.path.join(data_dir, 's60_staircase_ext.npz'),
    # Staircase Convention A (bare V, diagonal included)
    E_GS_A=E_GS_A,
    mu_forward_A=mu_forward_A,
    Lambda_res_A=Lambda_res_A,
    # Staircase Convention B (eps_canonical * V)
    E_GS_B=E_GS_B,
    mu_forward_B=mu_forward_B,
    Lambda_res_B=Lambda_res_B,
    # Cross-check (no diagonal, s54 convention)
    E_GS_A_nodiag=E_GS_A_nodiag,
    # Metadata
    eps_fold=eps_fold,
    V_fold=V_fold,
    eps_canonical=np.array(eps_canonical),
    N_modes=np.array(N_modes),
    tau_fold=np.array(tau_fold),
    M_KK=np.array(M_KK),
    rho_Lambda_obs=np.array(rho_Lambda_obs),
    N_eq=np.array(N_eq if N_eq is not None else np.nan),
    # Gate
    gate_name=np.array(['STAIRCASE-EXT-60']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
print(f"Data saved: s60_staircase_ext.npz")


# =====================================================================
#  11. FINAL SUMMARY
# =====================================================================

print("\n" + "=" * 72)
print("  FINAL SUMMARY")
print("=" * 72)

print(f"\n  Convention A (bare V_fold, diagonal included) — PRIMARY:")
print(f"    E_GS: {[f'{e:+.6f}' for e in E_GS_A]}")
print(f"    mu:   {[f'{m:+.6f}' for m in mu_forward_A]}")
print(f"    Lambda_res: {[f'{l:+.6f}' for l in Lambda_res_A]}")
print(f"    |Lambda_res|: {[f'{abs(l):.6f}' for l in Lambda_res_A]}")
print(f"    Monotone decreasing: {mono_decreasing}")
print(f"    N_eq (q-theory): {N_eq}")

print(f"\n  Convention B (eps_canonical * V_fold) — PLAN SPECIFICATION:")
print(f"    E_GS: {[f'{e:+.8f}' for e in E_GS_B]}")

print(f"\n  INCONSISTENCY NOTE:")
print(f"    Workshop E_GS(1)=-0.046 used bare V with diagonal (Convention A)")
print(f"    Workshop E_GS(2)=+0.325 used bare V WITHOUT diagonal (s54 Convention)")
print(f"    This script's Convention A is internally consistent: E_GS(2) = {E_GS_A[2]:+.6f}")
print(f"    Corrected Lambda_res(1) = {Lambda_res_A[0]:+.6f} (workshop: -0.418)")

dt_total = time.time() - t_start
print(f"\n  Total runtime: {dt_total:.2f}s")
print(f"\n  Gate verdict: {verdict}")
print(f"  {detail}")
