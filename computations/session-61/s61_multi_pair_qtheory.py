#!/usr/bin/env python3
"""
S61 W3-13: Multi-Pair Q-Theory at Finite N (MULTI-PAIR-QTHEORY-61)
====================================================================

Gate: MULTI-PAIR-QTHEORY-61
  PASS: oscillation amplitude decays as 1/N (3He-B thermodynamic limit)
  FAIL: O(1) at N=8 (discrete q-theory locked)
  INFO: non-monotone

Extends BCS staircase from S60 (N=0..4) to N=0..8 (full 8-mode Fock space).
For each N-pair sector, diagonalize exactly in C(8,N)-dimensional subspace.

Computes:
  1. E_GS(N) for N = 0, 1, ..., 8
  2. epsilon(N) = E_GS(N) - E_GS(N-1) [chemical potential / stair step]
  3. Lambda_residual(N) = E_GS(N) - N*epsilon_bar [deviation from linear fit]
  4. Delta^(3)(N) = (-1)^N * [E(N+1) - 2E(N) + E(N-1)] / 2 [odd-even staggering]
  5. Oscillation envelope fit: 1/N, 1/sqrt(N), or constant
  6. Quadratic interpolation for continuous n_eq

Physical context (Volovik q-theory):
  Lambda = partial F / partial q at equilibrium q_eq.
  If oscillation amplitude decays as 1/N -> thermodynamic limit gives Lambda=0
  (3He-B analog: superfluid energy density vanishes in the thermodynamic limit).
  If O(1) -> discrete frustration locks in finite CC (q-theory with discrete charge).

Author: volovik-superfluid-universe-theorist, Session 61
Date: 2026-03-28
"""

import os
import sys
import time
import numpy as np
from itertools import combinations
from math import comb
from scipy.optimize import curve_fit

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

# Load from s60_rg_integrals.npz (primary source for eps_fold, V_fold)
d60 = np.load(os.path.join(data_dir, 's60_rg_integrals.npz'), allow_pickle=True)
eps_fold = d60['eps_fold']       # 8 single-particle energies at fold
V_fold   = d60['V_fold']        # 8x8 pairing matrix (symmetric)

# Load S60 baseline for cross-check
d60s = np.load(os.path.join(data_dir, 's60_staircase_ext.npz'), allow_pickle=True)
E_GS_A_s60 = d60s['E_GS_A']    # S60 Convention A results for N=0..4

N_modes = 8  # (local)

print("=" * 72)
print("S61 W3-13: Multi-Pair Q-Theory at Finite N — MULTI-PAIR-QTHEORY-61")
print("=" * 72)
print(f"N_modes = {N_modes}")
print(f"tau_fold = {tau_fold}")
print(f"Fock space: 2^{N_modes} = {2**N_modes} total states")
print()
print("Sector dimensions: ", end="")
for N in range(N_modes + 1):
    print(f"C(8,{N})={comb(N_modes, N)}", end="  ")
print()
print()
print("Single-particle energies at fold (M_KK units):")
for i in range(N_modes):
    print(f"  eps[{i}] = {eps_fold[i]:.12f}")
print()
print(f"V_fold symmetric: max|V - V^T| = {np.max(np.abs(V_fold - V_fold.T)):.2e}")
print(f"V_fold norm: ||V|| = {np.linalg.norm(V_fold):.8f}")
print(f"V_fold diagonal: [{', '.join(f'{V_fold[k,k]:.6f}' for k in range(N_modes))}]")
print(f"V_fold trace: {np.trace(V_fold):.8f}")

# Sector identification
# B2: modes 0,1,2,3 (4 modes)
# B1: mode 4 (1 mode)
# B3: modes 5,6,7 (3 modes)
sector_labels = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3']


# =====================================================================
#  2. EXACT DIAGONALIZATION ROUTINES
# =====================================================================

def build_canonical_H_BCS(eps_k, V_kl, n_pair, include_diagonal=True):
    """
    Build BCS reduced Hamiltonian in the N-pair canonical Fock space.

    H = sum_k 2*eps_k * n_k - sum_{k,l} V_{kl} * P+_k * P_l

    where P+_k creates a Cooper pair in mode k, n_k = P+_k P_k is pair number.
    """
    N = len(eps_k)
    if n_pair == 0:
        return np.zeros((1, 1)), [()], 1
    if n_pair > N:
        raise ValueError(f"n_pair={n_pair} > N_modes={N}")

    basis = list(combinations(range(N), n_pair))
    dim = len(basis)
    assert dim == comb(N, n_pair)

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
#  3. COMPUTE FULL STAIRCASE: E_GS(N) for N = 0, 1, ..., 8
# =====================================================================

print("\n" + "=" * 72)
print("  EXACT DIAGONALIZATION: N = 0 .. 8")
print("  H = 2*eps_k * n_k - V_{kl} * P+_k * P_l  (Convention A: bare V_fold)")
print("=" * 72)

E_GS = np.zeros(N_modes + 1)  # E(0) through E(8)
E_GS[0] = 0.0  # Vacuum

eigs_all = {}
gs_vecs = {}
sector_dims = np.zeros(N_modes + 1, dtype=int)
gaps = np.zeros(N_modes + 1)

for N_pair in range(0, N_modes + 1):
    dim = comb(N_modes, N_pair)
    sector_dims[N_pair] = dim
    t0 = time.time()

    H, basis, dim_check = build_canonical_H_BCS(eps_fold, V_fold, N_pair,
                                                 include_diagonal=True)
    assert dim == dim_check

    if dim == 1:
        # 1D sector: eigenvalue is the matrix element itself
        E_GS[N_pair] = H[0, 0]
        eigs_all[N_pair] = np.array([H[0, 0]])
        gs_vecs[N_pair] = np.array([1.0])
        gaps[N_pair] = np.inf
    else:
        evals, evecs = np.linalg.eigh(H)
        E_GS[N_pair] = evals[0]
        eigs_all[N_pair] = evals
        gs_vecs[N_pair] = evecs[:, 0]
        gaps[N_pair] = evals[1] - evals[0] if dim > 1 else np.inf

    dt = time.time() - t0
    gap_str = f"{gaps[N_pair]:.6f}" if np.isfinite(gaps[N_pair]) else "inf"
    print(f"\n  N = {N_pair}: dim = {dim:4d}, E_GS = {E_GS[N_pair]:+.10f} M_KK, "
          f"gap = {gap_str}, t = {dt:.4f}s")
    if dim > 1:
        n_show = min(5, dim)
        print(f"    First {n_show} eigenvalues: {eigs_all[N_pair][:n_show]}")

    # Ground state occupation analysis
    if dim > 1:
        occ = np.zeros(N_modes)
        for idx_state, state in enumerate(basis):
            for k in state:
                occ[k] += gs_vecs[N_pair][idx_state]**2
        print(f"    GS pair occupations: [{', '.join(f'{o:.4f}' for o in occ)}]")


# =====================================================================
#  4. CROSS-CHECK AGAINST S60 (N=0..4)
# =====================================================================

print("\n" + "=" * 72)
print("  CROSS-CHECK: S61 vs S60 (Convention A, N=0..4)")
print("=" * 72)

crosscheck_ok = True
for N_pair in range(5):
    diff = abs(E_GS[N_pair] - E_GS_A_s60[N_pair])
    ok = "OK" if diff < 1e-8 else "MISMATCH"
    if diff >= 1e-8:
        crosscheck_ok = False
    print(f"  N={N_pair}: S61={E_GS[N_pair]:+.10f}, S60={E_GS_A_s60[N_pair]:+.10f}, "
          f"diff={diff:.2e} [{ok}]")

print(f"\n  Cross-check: {'PASSED' if crosscheck_ok else 'FAILED'}")


# =====================================================================
#  5. CHEMICAL POTENTIAL (STAIR STEPS)
# =====================================================================

print("\n" + "=" * 72)
print("  CHEMICAL POTENTIAL: epsilon(N) = E_GS(N) - E_GS(N-1)")
print("=" * 72)

epsilon = np.zeros(N_modes)  # epsilon[0] = E(1)-E(0), ..., epsilon[7] = E(8)-E(7)
for N in range(1, N_modes + 1):
    epsilon[N-1] = E_GS[N] - E_GS[N-1]
    print(f"  epsilon({N}) = {epsilon[N-1]:+.8f} M_KK")

epsilon_bar = np.mean(epsilon)
print(f"\n  epsilon_bar (mean) = {epsilon_bar:+.8f} M_KK")

# Also compute from linear regression: E(N) ~ a + b*N
N_arr = np.arange(N_modes + 1, dtype=float)
coeffs_lin = np.polyfit(N_arr, E_GS, 1)
epsilon_bar_fit = coeffs_lin[0]
E0_fit = coeffs_lin[1]
print(f"  Linear fit: E(N) = {E0_fit:+.6f} + {epsilon_bar_fit:+.6f} * N")
print(f"  epsilon_bar from fit = {epsilon_bar_fit:+.8f} M_KK")


# =====================================================================
#  6. LAMBDA RESIDUAL
# =====================================================================

print("\n" + "=" * 72)
print("  LAMBDA RESIDUAL: Lambda_res(N) = E_GS(N) - (a + b*N)")
print("=" * 72)

Lambda_res = np.zeros(N_modes + 1)
for N in range(N_modes + 1):
    Lambda_res[N] = E_GS[N] - (E0_fit + epsilon_bar_fit * N)
    print(f"  Lambda_res({N}) = {Lambda_res[N]:+.8f} M_KK")

# Compute amplitude as |Lambda_res| for N >= 1
Lambda_res_amp = np.abs(Lambda_res[1:])  # N=1..8
print(f"\n  |Lambda_res| for N=1..8: {Lambda_res_amp}")
print(f"  max |Lambda_res| = {np.max(Lambda_res_amp):.8f}")
print(f"  min |Lambda_res| = {np.min(Lambda_res_amp):.8f}")
print(f"  max/min ratio = {np.max(Lambda_res_amp) / np.min(Lambda_res_amp):.4f}")


# =====================================================================
#  7. ODD-EVEN STAGGERING: Delta^(3)(N)
# =====================================================================

print("\n" + "=" * 72)
print("  ODD-EVEN STAGGERING: Delta^(3)(N) = (-1)^N * [E(N+1)-2E(N)+E(N-1)] / 2")
print("=" * 72)

Delta3 = np.zeros(N_modes - 1)  # N = 1..7
for N in range(1, N_modes):
    Delta3[N-1] = ((-1)**N) * (E_GS[N+1] - 2*E_GS[N] + E_GS[N-1]) / 2.0
    print(f"  Delta^(3)({N}) = {Delta3[N-1]:+.8f} M_KK")

print(f"\n  Mean |Delta^(3)| = {np.mean(np.abs(Delta3)):.8f}")
print(f"  Std  |Delta^(3)| = {np.std(np.abs(Delta3)):.8f}")


# =====================================================================
#  8. OSCILLATION ENVELOPE FIT
# =====================================================================

print("\n" + "=" * 72)
print("  OSCILLATION ENVELOPE FIT")
print("=" * 72)

# Three models for the envelope of |Lambda_res(N)|:
# Model 1: A / N  (thermodynamic decay -> PASS)
# Model 2: A / sqrt(N)  (intermediate)
# Model 3: A (constant -> FAIL)

N_fit = np.arange(1, N_modes + 1, dtype=float)

# Model 1: |Lambda| = A/N + B
def model_1oN(N, A, B):
    return A / N + B

# Model 2: |Lambda| = A/sqrt(N) + B
def model_1sqrtN(N, A, B):
    return A / np.sqrt(N) + B

# Model 3: |Lambda| = A (constant)
def model_const(N, A):
    return A * np.ones_like(N)

# Also test power law: |Lambda| = A * N^(-alpha)
def model_power(N, A, alpha):
    return A * N**(-alpha)

results = {}

# Fit 1/N
try:
    p1, cov1 = curve_fit(model_1oN, N_fit, Lambda_res_amp, p0=[0.1, 0.05])
    res1 = Lambda_res_amp - model_1oN(N_fit, *p1)
    rss1 = np.sum(res1**2)
    results['1/N'] = {'params': p1, 'rss': rss1, 'label': f'A/N+B: A={p1[0]:.4f}, B={p1[1]:.4f}'}
    print(f"  1/N model: A={p1[0]:.6f}, B={p1[1]:.6f}, RSS={rss1:.2e}")
except Exception as e:
    print(f"  1/N model: FAILED ({e})")

# Fit 1/sqrt(N)
try:
    p2, cov2 = curve_fit(model_1sqrtN, N_fit, Lambda_res_amp, p0=[0.1, 0.05])
    res2 = Lambda_res_amp - model_1sqrtN(N_fit, *p2)
    rss2 = np.sum(res2**2)
    results['1/sqrt(N)'] = {'params': p2, 'rss': rss2, 'label': f'A/sqrt(N)+B: A={p2[0]:.4f}, B={p2[1]:.4f}'}
    print(f"  1/sqrt(N) model: A={p2[0]:.6f}, B={p2[1]:.6f}, RSS={rss2:.2e}")
except Exception as e:
    print(f"  1/sqrt(N) model: FAILED ({e})")

# Fit constant
try:
    p3, cov3 = curve_fit(model_const, N_fit, Lambda_res_amp, p0=[0.1])
    res3 = Lambda_res_amp - model_const(N_fit, *p3)
    rss3 = np.sum(res3**2)
    results['const'] = {'params': p3, 'rss': rss3, 'label': f'A: A={p3[0]:.4f}'}
    print(f"  Constant model: A={p3[0]:.6f}, RSS={rss3:.2e}")
except Exception as e:
    print(f"  Constant model: FAILED ({e})")

# Fit power law: A * N^{-alpha}
try:
    p4, cov4 = curve_fit(model_power, N_fit, Lambda_res_amp, p0=[0.1, 0.5],
                          bounds=([0, -2], [10, 5]))
    res4 = Lambda_res_amp - model_power(N_fit, *p4)
    rss4 = np.sum(res4**2)
    results['power'] = {'params': p4, 'rss': rss4, 'label': f'A*N^{{-alpha}}: A={p4[0]:.4f}, alpha={p4[1]:.4f}'}
    print(f"  Power law: A={p4[0]:.6f}, alpha={p4[1]:.6f}, RSS={rss4:.2e}")
except Exception as e:
    print(f"  Power law: FAILED ({e})")

# Determine best fit
best_model = min(results.keys(), key=lambda k: results[k]['rss'])
print(f"\n  Best fit: {best_model} ({results[best_model]['label']})")
print(f"  RSS ranking: ", end="")
for k in sorted(results.keys(), key=lambda k: results[k]['rss']):
    print(f"{k}={results[k]['rss']:.2e} ", end="")
print()


# =====================================================================
#  9. MONOTONICITY ANALYSIS
# =====================================================================

print("\n" + "=" * 72)
print("  MONOTONICITY ANALYSIS")
print("=" * 72)

# Check if |Lambda_res| is monotonically decreasing for N >= 2
amp_diff = np.diff(Lambda_res_amp)
monotone_decreasing = all(d < 0 for d in amp_diff[1:])  # from N=2 onward
any_increase = any(d > 0 for d in amp_diff)

print(f"  Successive differences in |Lambda_res(N)|:")
for i in range(len(amp_diff)):
    direction = "decrease" if amp_diff[i] < 0 else "INCREASE"
    print(f"    N={i+1} -> N={i+2}: {amp_diff[i]:+.8f}  [{direction}]")

print(f"\n  Monotone decreasing (N>=2): {monotone_decreasing}")
print(f"  Any increase: {any_increase}")

# Ratio test: |Lambda_res(N+1)| / |Lambda_res(N)|
print(f"\n  Ratio |Lambda_res(N+1)/Lambda_res(N)|:")
for i in range(len(Lambda_res_amp) - 1):
    if Lambda_res_amp[i] > 1e-15:
        ratio = Lambda_res_amp[i+1] / Lambda_res_amp[i]
        print(f"    N={i+1} -> N={i+2}: ratio = {ratio:.6f}")

# Check for convergence: last 3 points
if len(Lambda_res_amp) >= 3:
    last3 = Lambda_res_amp[-3:]
    spread = (max(last3) - min(last3)) / np.mean(last3)
    print(f"\n  Last 3 points spread: {spread:.4f} (fractional)")


# =====================================================================
#  10. QUADRATIC INTERPOLATION FOR CONTINUOUS n_eq
# =====================================================================

print("\n" + "=" * 72)
print("  QUADRATIC INTERPOLATION: F(q) = a*q^2 + b*q + c")
print("=" * 72)

# Fit E_GS(N) to a quadratic (Ginzburg-Landau free energy analog)
coeffs_quad = np.polyfit(N_arr, E_GS, 2)
a_quad, b_quad, c_quad = coeffs_quad
n_eq_quad = -b_quad / (2.0 * a_quad)

print(f"  Quadratic: F(q) = {a_quad:+.6f}*q^2 + {b_quad:+.6f}*q + {c_quad:+.6f}")
print(f"  n_eq (quadratic minimum) = {n_eq_quad:.6f}")
print(f"  LANDAU-1's n_eq = 0.074 (S60 GL fit)")
print(f"  F(n_eq) = {np.polyval(coeffs_quad, n_eq_quad):+.8f} M_KK")

# Also fit quartic for comparison
if len(N_arr) >= 5:
    coeffs_q4 = np.polyfit(N_arr, E_GS, 4)
    # Find minimum numerically
    N_dense = np.linspace(0, N_modes, 10000)
    F_dense = np.polyval(coeffs_q4, N_dense)
    idx_min = np.argmin(F_dense)
    n_eq_q4 = N_dense[idx_min]
    print(f"\n  Quartic fit minimum: n_eq = {n_eq_q4:.6f}")
    print(f"  F(n_eq) = {F_dense[idx_min]:+.8f} M_KK")
    print(f"  Quartic coefficients: {coeffs_q4}")

# Stiffness (compressibility analog): d^2 F / dq^2 at minimum
chi_q_quad = 2.0 * a_quad
print(f"\n  chi_q (quadratic) = {chi_q_quad:.6f} M_KK")
print(f"  LANDAU-1's chi_q = 0.024 (S60)")

# From quartic
if len(N_arr) >= 5:
    # d^2F/dq^2 at q = n_eq from quartic
    deriv2_q4 = np.polyder(np.poly1d(coeffs_q4), 2)
    chi_q_q4 = deriv2_q4(n_eq_q4)
    print(f"  chi_q (quartic at n_eq) = {chi_q_q4:.6f} M_KK")


# =====================================================================
#  11. VOLOVIK q-THEORY ANALYSIS
# =====================================================================

print("\n" + "=" * 72)
print("  VOLOVIK Q-THEORY ANALYSIS")
print("=" * 72)

# In q-theory, Lambda = dF/dq at equilibrium q.
# For discrete q (integer N_pair), Lambda_residual measures deviation from
# the smooth interpolation.
# Key question: does discreteness produce a finite CC or does it average out?

# Compute Lambda = [E(N+1) - E(N-1)] / 2 (symmetric derivative) at each N
Lambda_sym = np.zeros(N_modes - 1)  # N = 1..7
for N in range(1, N_modes):
    Lambda_sym[N-1] = (E_GS[N+1] - E_GS[N-1]) / 2.0

print("  Symmetric derivative Lambda(N) = [E(N+1) - E(N-1)] / 2:")
for N in range(1, N_modes):
    print(f"    Lambda({N}) = {Lambda_sym[N-1]:+.8f} M_KK")

# At the equilibrium, Lambda should be closest to zero
# Find where it changes sign
sign_changes = []
for i in range(len(Lambda_sym) - 1):
    if Lambda_sym[i] * Lambda_sym[i+1] < 0:
        sign_changes.append(i + 1)  # N value

print(f"\n  Lambda sign changes at N = {sign_changes}")

# Interpolate zero crossing
if len(sign_changes) > 0:
    for sc in sign_changes:
        N_lo = sc
        N_hi = sc + 1
        # Linear interpolation
        n_cross = N_lo + Lambda_sym[N_lo-1] / (Lambda_sym[N_lo-1] - Lambda_sym[N_hi-1])
        print(f"    Zero crossing between N={N_lo} and N={N_hi}: n_cross = {n_cross:.6f}")

# Deviation from smooth: |Lambda_res| at n_eq
# This is the CC in q-theory: the discrete jump in chemical potential
# that prevents exact self-tuning to Lambda=0
Lambda_res_at_neq = np.interp(n_eq_quad, N_arr, Lambda_res) if 0 <= n_eq_quad <= N_modes else np.nan
print(f"\n  Lambda_res at n_eq_quad = {n_eq_quad:.3f}: {Lambda_res_at_neq:+.8f} M_KK")

# The CC gap from discreteness
if abs(Lambda_res_at_neq) > 1e-15:
    Lambda_obs_in_MKK = rho_Lambda_obs / M_KK**4
    CC_gap_disc = abs(Lambda_res_at_neq) / Lambda_obs_in_MKK if Lambda_obs_in_MKK > 0 else np.inf
    print(f"  Lambda_obs in M_KK units: {Lambda_obs_in_MKK:.4e}")
    print(f"  CC gap from discreteness: {CC_gap_disc:.4e} ({np.log10(CC_gap_disc):.1f} orders)")


# =====================================================================
#  12. THERMODYNAMIC LIMIT EXTRAPOLATION
# =====================================================================

print("\n" + "=" * 72)
print("  THERMODYNAMIC LIMIT EXTRAPOLATION")
print("=" * 72)

# In 3He-B, the energy per particle approaches a smooth function as N -> inf.
# The residual oscillation (odd-even staggering) decays as 1/N.
# Here N_modes=8 is our "thermodynamic limit" proxy.

# Measure: amplitude of |Lambda_res(N)| as function of N
# Use only N >= 2 to avoid boundary effects
N_thermo = np.arange(2, N_modes + 1, dtype=float)
amp_thermo = Lambda_res_amp[1:]  # N=2..8

# Fit amplitude to: A * N^{-beta}
try:
    def power_fit(N, A, beta):
        return A * N**(-beta)
    p_thermo, cov_thermo = curve_fit(power_fit, N_thermo, amp_thermo,
                                      p0=[0.5, 0.5],
                                      bounds=([0, -2], [100, 5]))
    A_thermo, beta_thermo = p_thermo
    print(f"  Envelope fit (N>=2): A * N^{{-beta}}")
    print(f"    A = {A_thermo:.6f}")
    print(f"    beta = {beta_thermo:.6f}")
    if beta_thermo > 0.8:
        print(f"    -> Consistent with 1/N decay (beta ~ 1): PASS regime")
    elif beta_thermo > 0.3:
        print(f"    -> Intermediate decay (1/sqrt(N) ~ beta=0.5): INFO regime")
    elif beta_thermo > 0.05:
        print(f"    -> Slow decay: INFO regime")
    else:
        print(f"    -> No decay (beta ~ 0): FAIL regime (O(1) oscillations)")
except Exception as e:
    beta_thermo = np.nan
    print(f"  Power fit failed: {e}")

# Also check: does the variance of Lambda_res decrease?
var_first_half = np.var(Lambda_res_amp[:4])
var_second_half = np.var(Lambda_res_amp[4:])
print(f"\n  Variance of |Lambda_res|:")
print(f"    First half (N=1..4):  {var_first_half:.8f}")
print(f"    Second half (N=5..8): {var_second_half:.8f}")
print(f"    Ratio (second/first): {var_second_half/var_first_half:.4f}")


# =====================================================================
#  13. GATE VERDICT
# =====================================================================

print("\n" + "=" * 72)
print("  GATE VERDICT: MULTI-PAIR-QTHEORY-61")
print("=" * 72)

# Decision criteria:
# PASS: beta > 0.8 (amplitude decays ~ 1/N)
# FAIL: beta < 0.1 AND max/min ratio < 2 (O(1) constant oscillations)
# INFO: everything else (non-monotone, intermediate decay, etc.)

amp_ratio = np.max(Lambda_res_amp) / np.min(Lambda_res_amp) if np.min(Lambda_res_amp) > 1e-15 else np.inf

if not np.isnan(beta_thermo) and beta_thermo > 0.8:
    verdict = "PASS"
    detail = (f"Oscillation amplitude decays as N^{{-{beta_thermo:.2f}}} ~ 1/N. "
              f"Thermodynamic limit gives Lambda->0. 3He-B analog confirmed.")
elif not np.isnan(beta_thermo) and beta_thermo < 0.1 and amp_ratio < 2.0:
    verdict = "FAIL"
    detail = (f"Oscillation amplitude O(1) (beta={beta_thermo:.2f}). "
              f"Discrete q-theory locks finite CC. amp_ratio={amp_ratio:.2f}.")
else:
    verdict = "INFO"
    beta_str = f"{beta_thermo:.2f}" if not np.isnan(beta_thermo) else "N/A"
    detail = (f"beta={beta_str}, amp_ratio={amp_ratio:.2f}. "
              f"Non-monotone or intermediate decay. Larger N needed.")

print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")
print(f"  beta (envelope exponent): {beta_thermo:.4f}" if not np.isnan(beta_thermo) else "  beta: UNDEFINED")
print(f"  max |Lambda_res| / min |Lambda_res| = {amp_ratio:.4f}")
print(f"  n_eq (quadratic) = {n_eq_quad:.6f}")
print(f"  chi_q (quadratic) = {chi_q_quad:.6f}")
print(f"  Cross-check S60: {'PASSED' if crosscheck_ok else 'FAILED'}")


# =====================================================================
#  14. SAVE DATA
# =====================================================================

print("\n" + "=" * 72)
print("  SAVING DATA")
print("=" * 72)

save_path = os.path.join(data_dir, 's61_multi_pair_qtheory.npz')

save_dict = {
    # Input parameters
    'N_modes': N_modes,
    'tau_fold': tau_fold,
    'eps_fold': eps_fold,
    'V_fold': V_fold,
    'M_KK': M_KK,
    'rho_Lambda_obs': rho_Lambda_obs,

    # Core results
    'E_GS': E_GS,                    # E_GS[N] for N=0..8
    'epsilon': epsilon,               # chemical potential steps, N=1..8
    'epsilon_bar_fit': epsilon_bar_fit,
    'E0_fit': E0_fit,
    'Lambda_res': Lambda_res,         # N=0..8
    'Lambda_res_amp': Lambda_res_amp, # |Lambda_res| for N=1..8
    'Delta3': Delta3,                 # odd-even staggering, N=1..7
    'Lambda_sym': Lambda_sym,         # symmetric derivative, N=1..7

    # Fits
    'n_eq_quad': n_eq_quad,
    'chi_q_quad': chi_q_quad,
    'coeffs_quad': coeffs_quad,
    'coeffs_lin': coeffs_lin,
    'beta_thermo': beta_thermo,

    # Sector dimensions
    'sector_dims': sector_dims,
    'gaps': np.array([gaps[N] for N in range(N_modes + 1)]),

    # Gate
    'gate_name': np.array(['MULTI-PAIR-QTHEORY-61']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([detail]),

    # S60 cross-check
    'E_GS_A_s60': E_GS_A_s60,
    'crosscheck_ok': crosscheck_ok,
}

np.savez(save_path, **save_dict)
print(f"  Saved: {save_path}")


# =====================================================================
#  15. PLOT
# =====================================================================

print("\n" + "=" * 72)
print("  GENERATING PLOT")
print("=" * 72)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(f'MULTI-PAIR-QTHEORY-61: BCS Staircase N=0..8 | Verdict: {verdict}',
             fontsize=14, fontweight='bold')

N_arr_full = np.arange(N_modes + 1)

# Panel 1: E_GS(N) with quadratic fit
ax = axes[0, 0]
ax.plot(N_arr_full, E_GS, 'ko-', markersize=8, label='E_GS(N)', linewidth=2)
N_smooth = np.linspace(0, N_modes, 200)
ax.plot(N_smooth, np.polyval(coeffs_quad, N_smooth), 'r--', label=f'Quadratic (n_eq={n_eq_quad:.3f})')
ax.plot(N_smooth, E0_fit + epsilon_bar_fit * N_smooth, 'b:', label='Linear fit', alpha=0.7)
ax.axvline(n_eq_quad, color='red', linestyle=':', alpha=0.5)
ax.set_xlabel('N (pair number)')
ax.set_ylabel('E_GS (M_KK)')
ax.set_title('Ground State Energy')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Chemical potential
ax = axes[0, 1]
ax.plot(np.arange(1, N_modes + 1), epsilon, 'bs-', markersize=8, linewidth=2)
ax.axhline(epsilon_bar_fit, color='r', linestyle='--', label=f'epsilon_bar={epsilon_bar_fit:.4f}')
ax.set_xlabel('N')
ax.set_ylabel('epsilon(N) (M_KK)')
ax.set_title('Chemical Potential Steps')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Lambda residual
ax = axes[0, 2]
ax.plot(N_arr_full, Lambda_res, 'ro-', markersize=8, linewidth=2)
ax.axhline(0, color='k', linestyle='-', alpha=0.3)
ax.axvline(n_eq_quad, color='blue', linestyle=':', alpha=0.5, label=f'n_eq={n_eq_quad:.3f}')
ax.set_xlabel('N')
ax.set_ylabel('Lambda_res (M_KK)')
ax.set_title('CC Residual (deviation from linear)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: |Lambda_res| with envelope fits
ax = axes[1, 0]
N_fit_arr = np.arange(1, N_modes + 1)
ax.semilogy(N_fit_arr, Lambda_res_amp, 'ko', markersize=10, zorder=5)
N_smooth2 = np.linspace(1, N_modes, 200)
if '1/N' in results:
    ax.semilogy(N_smooth2, model_1oN(N_smooth2, *results['1/N']['params']),
                'r-', label=results['1/N']['label'])
if '1/sqrt(N)' in results:
    ax.semilogy(N_smooth2, model_1sqrtN(N_smooth2, *results['1/sqrt(N)']['params']),
                'b--', label=results['1/sqrt(N)']['label'])
if 'const' in results:
    ax.axhline(results['const']['params'][0], color='g', linestyle=':', label=results['const']['label'])
if 'power' in results:
    ax.semilogy(N_smooth2, model_power(N_smooth2, *results['power']['params']),
                'm-.', label=results['power']['label'], linewidth=2)
ax.set_xlabel('N')
ax.set_ylabel('|Lambda_res| (M_KK)')
ax.set_title('Oscillation Envelope')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 5: Odd-even staggering
ax = axes[1, 1]
ax.plot(np.arange(1, N_modes), Delta3, 'gD-', markersize=8, linewidth=2)
ax.axhline(0, color='k', linestyle='-', alpha=0.3)
ax.set_xlabel('N')
ax.set_ylabel('Delta^(3)(N) (M_KK)')
ax.set_title('Odd-Even Staggering')
ax.grid(True, alpha=0.3)

# Panel 6: Symmetric derivative (q-theory Lambda)
ax = axes[1, 2]
ax.plot(np.arange(1, N_modes), Lambda_sym, 'ms-', markersize=8, linewidth=2)
ax.axhline(0, color='k', linestyle='-', alpha=0.3)
for sc in sign_changes:
    ax.axvline(sc + 0.5, color='red', linestyle=':', alpha=0.7)
ax.set_xlabel('N')
ax.set_ylabel('Lambda_sym(N) (M_KK)')
ax.set_title('dF/dq (q-theory CC)')
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plot_path = os.path.join(data_dir, 's61_multi_pair_qtheory.png')
plt.savefig(plot_path, dpi=150)
print(f"  Saved: {plot_path}")
plt.close()


# =====================================================================
#  16. SUMMARY
# =====================================================================

t_total = time.time() - t_start
print("\n" + "=" * 72)
print("  SUMMARY")
print("=" * 72)
print(f"  Total runtime: {t_total:.2f}s")
print(f"  Gate: MULTI-PAIR-QTHEORY-61 = {verdict}")
print(f"  Envelope exponent beta = {beta_thermo:.4f}" if not np.isnan(beta_thermo) else "  beta = UNDEFINED")
print(f"  n_eq (quadratic) = {n_eq_quad:.6f}")
print(f"  n_eq (LANDAU-1 S60) = 0.074")
print(f"  chi_q (quadratic) = {chi_q_quad:.6f}")
print(f"  chi_q (LANDAU-1 S60) = 0.024")
print()
print("  E_GS staircase:")
for N in range(N_modes + 1):
    print(f"    E_GS({N}) = {E_GS[N]:+.10f} M_KK  (dim={sector_dims[N]})")
print()
print("  |Lambda_res| envelope:")
for N in range(1, N_modes + 1):
    print(f"    N={N}: |Lambda_res| = {Lambda_res_amp[N-1]:.8f}")
print()
print("  3He-B parallel: in the thermodynamic limit of a BCS superfluid,")
print("  Lambda -> 0 requires beta >= 1. The microscopic theory determines")
print("  whether discrete charge locking persists or washes out.")
print("=" * 72)
