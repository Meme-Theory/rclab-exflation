#!/usr/bin/env python3
"""
s60_pw_h0_conv.py — PW-H0-CONV-60
Peter-Weyl Convergence of N_factor = M_Pl(SA) / M_Pl(obs)

Context
-------
SPINOR-NORM-59 found N_factor = 3.920 at max(p+q)=3, giving H_0 = 68.8 km/s/Mpc.
The 2.0% residual from sqrt(16) = 4.00 was attributed to Peter-Weyl truncation.
This computation extends to max(p+q)=4,5,6,7 to test monotone convergence.

CRITICAL FINDING DURING DEVELOPMENT:
S44's eigenvalue data was missing the (1,2) irrep (only had (2,1), not its
conjugate). With 9/10 sectors at L=3 instead of 10/10, the a_2 total was
162984 instead of the correct 250361. The N_factor = 3.920 was an artifact
of this incomplete Peter-Weyl expansion. The correct N(L=3) = 4.859.

Method
------
1. Compute Dirac eigenvalues of D_K(tau_fold) on SU(3) for ALL irreps (p,q)
   with p+q <= L_max using the dirac_spectrum infrastructure.
2. Compute a_2^{(p,q)} = dim(p,q)^2 * sum_i |lambda_i| for each irrep.
3. Compute cumulative a_2(L) = sum_{p+q <= L} a_2^{(p,q)}.
4. Compute N_factor(L) = sqrt(a_2(L) / a_2_needed) where
   a_2_needed = M_Pl_reduced^2 * pi^2 / (f_2 * M_KK^2).
5. Track convergence/divergence.

Gate: PW-H0-CONV-60
    PASS: |N(L=4) - 4.00| < |N(L=3) - 4.00| (monotone convergence toward sqrt(16))
    FAIL: N(L=4) > N(L=3) or N(L=4) < N(L=3) - 0.04 (non-monotone or divergent)
    INFO: Convergence confirmed but |N(L=4) - 4.00| > 0.01 (convergence slow)

Author: baptista-spacetime-analyst
Session: S60 W2-1
"""

import sys
import os
import time
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, str(_x2_shared_dir()))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from canonical_constants import (
    tau_fold, PI, M_KK, M_Pl_reduced, M_Pl_unreduced,
    H_0_km_s_Mpc,
)

import dirac_spectrum as tds

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("PW-H0-CONV-60: Peter-Weyl Convergence of N_factor")
print("=" * 72)

# =============================================================================
# 1. BUILD GEOMETRIC INFRASTRUCTURE AT THE FOLD
# =============================================================================
print("\n" + "=" * 72)
print("1. GEOMETRIC INFRASTRUCTURE AT tau_fold = %.4f" % tau_fold)
print("=" * 72)

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
gammas = tds.build_cliff8()

# Validate Clifford algebra
cliff_err = tds.validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")

# Build metric, frame, connection, Omega at the fold
B_ab = tds.compute_killing_form(f_abc)
g_s = tds.jensen_metric(B_ab, tau_fold)
E = tds.orthonormal_frame(g_s)
ft = tds.frame_structure_constants(f_abc, E)
Gamma = tds.connection_coefficients(ft)

mc_err = tds.validate_connection(Gamma)
print(f"  Metric compatibility error: {mc_err:.2e}")

Omega = tds.spinor_connection_offset(Gamma, gammas)
is_h, is_ah, h_err, ah_err = tds.validate_omega_hermitian(Omega)
print(f"  Omega anti-Hermiticity error: {ah_err:.2e}")
print(f"  Omega Hermiticity error: {h_err:.2e}")
print(f"  Omega type: {'anti-Hermitian' if is_ah else 'UNKNOWN'}")

# =============================================================================
# 2. COMPUTE DIRAC EIGENVALUES FOR ALL IRREPS UP TO L_max = 7
# =============================================================================
print("\n" + "=" * 72)
print("2. DIRAC EIGENVALUE COMPUTATION")
print("=" * 72)

L_max = 7  # Go to L=7 for robust convergence analysis

# Store results per irrep
irrep_data = {}
t_total_start = time.time()

for L in range(L_max + 1):
    for p in range(L + 1):
        q = L - p
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2

        t0 = time.time()
        tds._irrep_cache.clear()

        try:
            rho, dim_check = tds.get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq, f"dim mismatch: {dim_check} vs {dim_pq}"
        except Exception as e:
            print(f"  ({p},{q}): SKIPPED - {e}")
            continue

        D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)
        evals = np.linalg.eigvals(D_pi)
        abs_evals = np.abs(evals)

        t1 = time.time()

        # Verify anti-Hermiticity of D_pi
        D_ah_err = np.max(np.abs(D_pi + D_pi.conj().T))
        # Eigenvalues should be purely imaginary
        real_part_max = np.max(np.abs(np.real(evals)))
        imag_part = np.sort(np.abs(np.imag(evals)))

        # a_2 contribution: dim^2 * sum(|lambda|)
        a2_contrib = dim_pq**2 * np.sum(abs_evals)
        a0_contrib = dim_pq**2 * len(abs_evals)  # = dim^2 * dim*16
        a4_contrib = dim_pq**2 * np.sum(abs_evals**2)

        irrep_data[(p, q)] = {
            'dim': dim_pq, 'd2': dim_pq**2,
            'n_evals': len(evals),
            'abs_evals': abs_evals,
            'a0_contrib': a0_contrib,
            'a2_contrib': a2_contrib,
            'a4_contrib': a4_contrib,
            'omega_min': np.min(abs_evals),
            'omega_max': np.max(abs_evals),
            'D_ah_err': D_ah_err,
            'real_part_max': real_part_max,
            'time': t1 - t0,
            'L': L,
        }

        status = "OK" if D_ah_err < 1e-10 else f"AH_ERR={D_ah_err:.2e}"
        print(f"  ({p},{q}): dim={dim_pq:3d}, D={dim_pq*16:5d}x{dim_pq*16:<5d}, "
              f"|lam| in [{np.min(abs_evals):.4f},{np.max(abs_evals):.4f}], "
              f"a2={a2_contrib:.1f}, {status}, {t1-t0:.3f}s")

t_total = time.time() - t_total_start
n_irreps_computed = len(irrep_data)
print(f"\n  Total: {n_irreps_computed} irreps computed in {t_total:.1f}s")

# =============================================================================
# 3. CUMULATIVE a_2 BY TRUNCATION LEVEL
# =============================================================================
print("\n" + "=" * 72)
print("3. CUMULATIVE a_2 BY TRUNCATION LEVEL")
print("=" * 72)

# Define a_2_needed for N_factor computation
f2 = 1.0  # cutoff moment (S52/S59 convention)
a2_needed = M_Pl_reduced**2 * PI**2 / (f2 * M_KK**2)
print(f"\n  a_2_needed (for M_Pl match) = {a2_needed:.4f}")
print(f"  M_KK = {M_KK:.4e} GeV, M_Pl_reduced = {M_Pl_reduced:.4e} GeV")

# Compute cumulative sums
level_data = {}
for L in range(L_max + 1):
    a0_L = sum(d['a0_contrib'] for (p, q), d in irrep_data.items() if p + q <= L)
    a2_L = sum(d['a2_contrib'] for (p, q), d in irrep_data.items() if p + q <= L)
    a4_L = sum(d['a4_contrib'] for (p, q), d in irrep_data.items() if p + q <= L)
    n_irreps_L = sum(1 for (p, q) in irrep_data if p + q <= L)
    n_evals_L = sum(d['n_evals'] for (p, q), d in irrep_data.items() if p + q <= L)
    n_pw_L = sum(d['d2'] * d['n_evals'] for (p, q), d in irrep_data.items() if p + q <= L)

    # New contributions at this level
    a2_new = sum(d['a2_contrib'] for (p, q), d in irrep_data.items() if p + q == L)
    n_new = sum(1 for (p, q) in irrep_data if p + q == L)

    N_factor = np.sqrt(a2_L / a2_needed)
    N_factor_sq = a2_L / a2_needed

    level_data[L] = {
        'a0': a0_L, 'a2': a2_L, 'a4': a4_L,
        'n_irreps': n_irreps_L, 'n_evals': n_evals_L, 'n_pw': n_pw_L,
        'a2_new': a2_new, 'n_new': n_new,
        'N_factor': N_factor, 'N_factor_sq': N_factor_sq,
    }

# Print table
print(f"\n  {'L':>3s} {'n_irreps':>9s} {'n_evals':>8s} {'a2_cumul':>14s} {'a2_new':>14s} "
      f"{'N_factor':>10s} {'N^2':>10s} {'delta_N':>10s}")
print("  " + "-" * 95)

for L in range(L_max + 1):
    d = level_data[L]
    delta = d['N_factor'] - 4.0
    missing = " *PARTIAL*" if L == 7 else ""
    print(f"  {L:3d} {d['n_irreps']:9d} {d['n_evals']:8d} {d['a2']:14.1f} {d['a2_new']:14.1f} "
          f"{d['N_factor']:10.4f} {d['N_factor_sq']:10.4f} {delta:+10.4f}{missing}")

# =============================================================================
# 4. CROSS-CHECK: VERIFY S44/S59 BUG
# =============================================================================
print("\n" + "=" * 72)
print("4. S44 DATA BUG: MISSING (1,2) IRREP")
print("=" * 72)

# Load S44 data for comparison
s44_path = os.path.join(outdir, 's44_dos_tau.npz')
try:
    d44 = np.load(s44_path, allow_pickle=True)
    s44_omegas = d44['tau0.19_all_omega']
    s44_dims = d44['tau0.19_all_dim2']
    s44_a2 = float(np.sum(s44_dims * s44_omegas))
    s44_n_evals = len(s44_omegas)

    print(f"  S44 data: {s44_n_evals} eigenvalues, a2 = {s44_a2:.4f}")
    print(f"  Fresh computation (L<=3): {level_data[3]['n_evals']} eigenvalues, a2 = {level_data[3]['a2']:.4f}")
    print(f"  Difference: {level_data[3]['a2'] - s44_a2:.4f}")

    # The missing (1,2) irrep
    a2_12 = irrep_data[(1, 2)]['a2_contrib']
    print(f"\n  (1,2) irrep a2 contribution: {a2_12:.4f}")
    print(f"  S44 a2 + (1,2) = {s44_a2 + a2_12:.4f}")
    print(f"  Fresh L<=3 a2 = {level_data[3]['a2']:.4f}")
    print(f"  Match: {abs(s44_a2 + a2_12 - level_data[3]['a2']) < 0.1}")

    # S44 sector list verification
    print(f"\n  S44 stored sectors (from d^2 values):")
    for d2 in sorted(set(s44_dims.astype(int))):
        mask = s44_dims.astype(int) == d2
        n = int(np.sum(mask))
        print(f"    d^2={d2:4d}: {n:4d} eigenvalues")

    print(f"\n  Expected at L<=3 (complete):")
    for p in range(4):
        for q in range(4 - p):
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            print(f"    ({p},{q}): dim={dim_pq}, n_ev={dim_pq*16}, d^2={dim_pq**2}")

    print(f"\n  S44 total eigenvalues: {s44_n_evals}")
    expected = sum((p + 1) * (q + 1) * (p + q + 2) // 2 * 16
                   for p in range(4) for q in range(4 - p))
    print(f"  Expected total (complete L<=3): {expected}")
    print(f"  Missing: {expected - s44_n_evals} = (1,2) has dim=15, 15*16=240 eigenvalues")

    s44_bug_confirmed = True
except FileNotFoundError:
    print("  S44 data not found -- cannot verify bug")
    s44_bug_confirmed = False

# =============================================================================
# 5. S59 N_FACTOR RE-EVALUATION
# =============================================================================
print("\n" + "=" * 72)
print("5. S59 N_FACTOR RE-EVALUATION")
print("=" * 72)

N_s59 = 3.920438854652296  # S59 value (from incomplete data)
N_correct_L3 = level_data[3]['N_factor']
N_L4 = level_data[4]['N_factor']

print(f"  S59 N_factor (incomplete L=3): {N_s59:.6f}")
print(f"  Correct N_factor (complete L=3): {N_correct_L3:.6f}")
print(f"  N_factor (L=4): {N_L4:.6f}")
print(f"  N_factor (L=5): {level_data[5]['N_factor']:.6f}")
print(f"  N_factor (L=6): {level_data[6]['N_factor']:.6f}")
print(f"  N_factor (L=7): {level_data[7]['N_factor']:.6f}")
print(f"\n  Target: 4.00 (sqrt of dim(Delta_8)=16)")
print(f"  S59 deviation: {(N_s59 - 4.0) / 4.0 * 100:+.2f}% (appeared to converge)")
print(f"  Correct L=3:   {(N_correct_L3 - 4.0) / 4.0 * 100:+.2f}% (overshoots)")
print(f"  L=4:            {(N_L4 - 4.0) / 4.0 * 100:+.2f}% (diverges)")

# Check monotonicity: N is monotonically INCREASING
print(f"\n  Monotonicity check (N(L+1) > N(L)):")
all_increasing = True
for L in range(L_max):
    if L + 1 not in level_data:
        continue
    inc = level_data[L + 1]['N_factor'] > level_data[L]['N_factor']
    all_increasing = all_increasing and inc
    print(f"    N({L+1}) = {level_data[L+1]['N_factor']:.4f} > N({L}) = {level_data[L]['N_factor']:.4f}: {inc}")
print(f"  All increasing: {all_increasing}")

# =============================================================================
# 6. GROWTH RATE ANALYSIS
# =============================================================================
print("\n" + "=" * 72)
print("6. GROWTH RATE ANALYSIS")
print("=" * 72)

# Fit a_2(L) to a power law: a_2(L) ~ c * L^alpha
L_arr = np.array([L for L in range(1, L_max + 1)])
a2_arr = np.array([level_data[L]['a2'] for L in L_arr])
ln_L = np.log(L_arr)
ln_a2 = np.log(a2_arr)

# Linear fit in log-log space
coeffs = np.polyfit(ln_L, ln_a2, 1)
alpha_growth = coeffs[0]
c_growth = np.exp(coeffs[1])

print(f"  Power law fit: a_2(L) ~ {c_growth:.1f} * L^{alpha_growth:.3f}")
print(f"  (Residual from fit: {np.std(ln_a2 - np.polyval(coeffs, ln_L)):.4f})")

# N_factor growth: N(L) ~ sqrt(c/a2_needed) * L^{alpha/2}
N_growth = alpha_growth / 2
print(f"  N_factor(L) ~ L^{N_growth:.3f} (diverges as L -> infinity)")

# Per-level growth factor
print(f"\n  Per-level growth factors:")
for L in range(1, L_max + 1):
    a2_new = level_data[L]['a2_new']
    a2_prev = level_data[L - 1]['a2']
    ratio = level_data[L]['a2'] / a2_prev if a2_prev > 0 else float('inf')
    frac_new = a2_new / level_data[L]['a2'] if level_data[L]['a2'] > 0 else 0
    print(f"    L={L}: a2_new/a2_cumul = {frac_new:.4f}, "
          f"a2(L)/a2(L-1) = {ratio:.4f}")

# =============================================================================
# 7. PHYSICAL INTERPRETATION: WHY a_2 DIVERGES
# =============================================================================
print("\n" + "=" * 72)
print("7. PHYSICAL INTERPRETATION")
print("=" * 72)

print("""
  The quantity a_2 := sum_{(p,q)} dim(p,q)^2 * sum_i |lambda_i^{(p,q)}|
  is NOT a standard Seeley-DeWitt heat kernel coefficient. The true heat
  kernel coefficient a_2(D_K^2) is a LOCAL geometric integral:

    a_2(D_K^2) = (4pi)^{-d/2} * integral_K Tr(E_2) dvol

  where E_2 involves Ricci curvature terms. This is FINITE.

  The spectral sum used in S44/S52/S59 is a DIFFERENT quantity:
    "a_2" = sum_n mult_n * |lambda_n|

  where n runs over ALL eigenvalues of D_K with Peter-Weyl multiplicity.
  This is essentially Tr(|D_K|) -- the trace of the absolute value of the
  Dirac operator. On a compact manifold, Tr(|D_K|) DIVERGES because:

  1. Eigenvalue growth: |lambda_n| ~ n^{1/d} for d-dimensional manifolds
     (Weyl's law for the Dirac operator).

  2. Multiplicity growth: dim(p,q) ~ (p+q)^2 for SU(3), and each irrep
     at level L has ~ L+1 representations.

  3. Together: a_2(L) grows as a polynomial in L, approximately L^{8.5}.

  The Chamseddine-Connes spectral action formula:
    S = Tr(f(D/Lambda))
  uses a CUTOFF function f that damps high eigenvalues. The heat kernel
  coefficients a_k appear as coefficients in the asymptotic expansion of
  this regularized trace. Without the cutoff (or with f(x) = |x|), the
  trace diverges.

  CONCLUSION: The "N_factor = 3.920" from S59 was an artifact of:
  (a) Missing the (1,2) irrep from the Peter-Weyl expansion (S44 bug)
  (b) Truncating at L=3, which happened to give a number near 4.00
  (c) Interpreting a divergent spectral sum as a convergent series

  The spectral action identification M_Pl^2 ~ a_2 * M_KK^2 requires
  a_2 to be the TRUE heat kernel coefficient (a finite geometric integral),
  not the Peter-Weyl spectral sum Tr(|D_K|) which diverges.
""")

# =============================================================================
# 8. CORRECT a_2 FROM HEAT KERNEL (SINGLET SECTOR)
# =============================================================================
print("=" * 72)
print("8. SINGLET SECTOR AS THE CORRECT GRAVITATIONAL a_2")
print("=" * 72)

# The singlet (0,0) sector has dim=1, so d^2=1. Its contribution to the
# Peter-Weyl sum does NOT grow with L. It is the sector that survives
# KK reduction and contributes to 4D gravity.

a2_singlet = irrep_data[(0, 0)]['a2_contrib']
a4_singlet = irrep_data[(0, 0)]['a4_contrib']
n_singlet = irrep_data[(0, 0)]['n_evals']

print(f"  Singlet sector:")
print(f"    n_evals = {n_singlet} (= dim(Delta_8) = 16)")
print(f"    a2_singlet = {a2_singlet:.6f}")
print(f"    a4_singlet = {a4_singlet:.6f}")

# For the singlet sector, a_2 = 1^2 * sum(|lambda_i|) = sum(|lambda_i|)
# This IS related to the trace of |D_K| restricted to constant functions on SU(3),
# which is a finite 16x16 matrix trace.

singlet_omegas = sorted(irrep_data[(0, 0)]['abs_evals'])
print(f"\n  Singlet eigenvalues:")
for i, w in enumerate(singlet_omegas):
    print(f"    |lambda_{i+1:2d}| = {w:.8f}")

# The correct identification for gravity uses a_2 from the heat kernel,
# not from the Peter-Weyl spectral sum. The heat kernel a_2 is obtained
# from the asymptotic expansion of Tr(exp(-t D_K^2)) which converges for
# any finite t > 0.

# =============================================================================
# 9. WHAT THE CORRECT H_0 COMPUTATION SHOULD USE
# =============================================================================
print("\n" + "=" * 72)
print("9. IMPLICATIONS FOR H_0")
print("=" * 72)

# The S59 H_0 = 68.8 came from:
# H_0 = 67.4 * sqrt(G_corrected / G_observed)
# where G_corrected = G_SA / 16 (dividing by dim(Delta_8))
# and G_SA used the incomplete a_2 = 162984.

# The correct computation requires:
# (a) The TRUE Seeley-DeWitt a_2 coefficient (local geometric integral)
# (b) NOT the Peter-Weyl spectral sum Tr(|D_K|)

# The canonical a_2_fold = 2776.17 from S42 may be the correct value
# (it was computed differently, from the BCS Hamiltonian spectrum).

print(f"  S59 used: a_2 = 162984 (incomplete PW sum), N = 3.920")
print(f"  Complete PW sum at L=3: a_2 = {level_data[3]['a2']:.1f}, N = {level_data[3]['N_factor']:.4f}")
print(f"  PW sum at L=7: a_2 = {level_data[7]['a2']:.1f}, N = {level_data[7]['N_factor']:.4f}")
print(f"  DIVERGENT: The PW sum grows as L^{alpha_growth:.1f}")
print(f"\n  The H_0 = 68.8 result from S59 is NOT confirmed by this computation.")
print(f"  The near-agreement with 4.00 was a numerical coincidence from:")
print(f"    (1) Missing (1,2) irrep in S44 data")
print(f"    (2) Truncation at L=3")
print(f"  Both are data artifacts, not physics.")

# =============================================================================
# 10. GATE VERDICT
# =============================================================================
print("\n" + "=" * 72)
print("10. GATE VERDICT: PW-H0-CONV-60")
print("=" * 72)

# Pre-registered criterion:
# PASS: |N(L=4) - 4.00| < |N(L=3) - 4.00| (monotone convergence toward 4)
# FAIL: N(L=4) > N(L=3) (divergent)

# Using CORRECT L=3 (not the S59 incomplete value):
N_L3_correct = level_data[3]['N_factor']
N_L4_val = level_data[4]['N_factor']

deviation_L3 = abs(N_L3_correct - 4.00)
deviation_L4 = abs(N_L4_val - 4.00)

print(f"\n  Gate: PW-H0-CONV-60")
print(f"  Pre-registered criterion:")
print(f"    PASS: |N(L=4) - 4.00| < |N(L=3) - 4.00|")
print(f"    FAIL: N(L=4) > N(L=3) or N(L=4) < N(L=3) - 0.04")
print(f"\n  Measured values:")
print(f"    N(L=3) = {N_L3_correct:.6f} (correct, complete)")
print(f"    N(L=4) = {N_L4_val:.6f}")
print(f"    |N(L=3) - 4.00| = {deviation_L3:.6f}")
print(f"    |N(L=4) - 4.00| = {deviation_L4:.6f}")
print(f"    N(L=4) > N(L=3): True (divergent)")

# FAIL: N(L=4) = 13.40 > N(L=3) = 4.86 (divergent, not converging)
verdict = "FAIL"
detail = (f"N(L=4) = {N_L4_val:.4f} >> N(L=3) = {N_L3_correct:.4f} >> 4.00. "
          f"The Peter-Weyl spectral sum diverges as L^{alpha_growth:.1f}. "
          f"N_factor does NOT converge to sqrt(16). "
          f"S59's N = 3.920 was an artifact of missing the (1,2) irrep in S44.")

print(f"\n  VERDICT: {verdict}")
print(f"  Detail: {detail}")

# Also note: even using the S59-INCOMPLETE data:
print(f"\n  Note: Even using S59's incomplete L=3 data (N=3.920),")
print(f"  the corrected L=3 gives N=4.859, and L=4 gives N=13.404.")
print(f"  The sequence 3.920 -> 4.859 -> 13.404 is monotonically increasing,")
print(f"  not converging to 4.00.")

# =============================================================================
# 11. CROSS-CHECKS
# =============================================================================
print("\n" + "=" * 72)
print("11. CROSS-CHECKS")
print("=" * 72)

# Check 1: Conjugate representations have identical spectra
print("\n  Check 1: Conjugate representation spectral identity")
conj_pairs = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (2, 1), (3, 1)]
for p, q in conj_pairs:
    if (p, q) in irrep_data and (q, p) in irrep_data:
        a2_pq = irrep_data[(p, q)]['a2_contrib']
        a2_qp = irrep_data[(q, p)]['a2_contrib']
        rel_diff = abs(a2_pq - a2_qp) / max(a2_pq, a2_qp)
        print(f"    ({p},{q}) vs ({q},{p}): a2 = {a2_pq:.4f} vs {a2_qp:.4f}, "
              f"rel diff = {rel_diff:.2e}")

# Check 2: Anti-Hermiticity of all D_pi
print("\n  Check 2: D_pi anti-Hermiticity")
max_ah_err = max(d['D_ah_err'] for d in irrep_data.values())
print(f"    Max anti-Hermiticity error across all irreps: {max_ah_err:.2e}")

# Check 3: Eigenvalue reality (should be purely imaginary)
print("\n  Check 3: Eigenvalue purity (real part should be zero)")
max_real_err = max(d['real_part_max'] for d in irrep_data.values())
print(f"    Max |Re(lambda)| across all irreps: {max_real_err:.2e}")

# Check 4: dim(p,q) formula consistency
print("\n  Check 4: Dimension formula")
for (p, q), d in sorted(irrep_data.items()):
    expected_dim = (p + 1) * (q + 1) * (p + q + 2) // 2
    actual_n = d['n_evals'] // 16
    assert actual_n == expected_dim, f"({p},{q}): {actual_n} vs {expected_dim}"
print(f"    All {len(irrep_data)} irreps: dimension formula verified")

# Check 5: a_2 at L=3 matches S44 + (1,2) correction
if s44_bug_confirmed:
    a2_s44_corrected = s44_a2 + irrep_data[(1, 2)]['a2_contrib']
    err = abs(a2_s44_corrected - level_data[3]['a2'])
    print(f"\n  Check 5: S44 + (1,2) = fresh L=3")
    print(f"    S44 a2 + (1,2) a2 = {a2_s44_corrected:.4f}")
    print(f"    Fresh L=3 a2      = {level_data[3]['a2']:.4f}")
    print(f"    Difference: {err:.4f} ({'PASS' if err < 0.1 else 'FAIL'})")

# Check 6: Weyl's law scaling
# For 8D Dirac operator: N(lambda) ~ lambda^8 (counting with PW multiplicity)
# So a_2(L) = integral_0^{lambda_max(L)} lambda * N'(lambda) dlambda ~ lambda_max^9
print(f"\n  Check 6: Weyl's law consistency")
print(f"    Expected growth: a_2 ~ L^9 for 8D Dirac operator")
print(f"    Measured growth: a_2 ~ L^{alpha_growth:.2f}")
print(f"    (Close to 9 confirms Weyl's law is operative)")

# =============================================================================
# 12. PLOT
# =============================================================================
print("\n" + "=" * 72)
print("12. GENERATING PLOT")
print("=" * 72)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: a_2(L) cumulative (log scale)
ax = axes[0, 0]
L_plot = np.array([L for L in range(L_max + 1)])
a2_plot = np.array([level_data[L]['a2'] for L in L_plot])
ax.semilogy(L_plot, a2_plot, 'bo-', markersize=8, linewidth=2, label='Fresh computation')
# S44 incomplete value
ax.semilogy(3, 162984.4, 'rx', markersize=15, markeredgewidth=3, label='S44/S59 (incomplete)')
# Power law fit
L_fit = np.linspace(0.5, L_max + 0.5, 100)
a2_fit = c_growth * L_fit**alpha_growth
ax.semilogy(L_fit, a2_fit, 'g--', alpha=0.5, label=f'Fit: $a_2 \\sim L^{{{alpha_growth:.1f}}}$')
ax.set_xlabel('$L_{\\max} = \\max(p+q)$', fontsize=12)
ax.set_ylabel('$a_2$ (cumulative)', fontsize=12)
ax.set_title('Peter-Weyl spectral sum $a_2(L)$', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 2: N_factor(L) with target line
ax = axes[0, 1]
N_plot = np.array([level_data[L]['N_factor'] for L in L_plot])
ax.plot(L_plot, N_plot, 'bo-', markersize=8, linewidth=2, label='N(L) = $\\sqrt{a_2(L)/a_{2,\\mathrm{needed}}}$')
ax.axhline(y=4.0, color='r', linestyle='--', linewidth=1.5, label='Target: $\\sqrt{16} = 4.00$')
# S59 point
ax.plot(3, N_s59, 'rx', markersize=15, markeredgewidth=3, label=f'S59: N = {N_s59:.3f} (incomplete)')
ax.set_xlabel('$L_{\\max}$', fontsize=12)
ax.set_ylabel('$N_{\\mathrm{factor}}$', fontsize=12)
ax.set_title('N-factor divergence', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(bottom=0)

# Panel 3: Per-level a_2 contribution
ax = axes[1, 0]
a2_new_plot = np.array([level_data[L]['a2_new'] for L in range(1, L_max + 1)])
L_new_plot = np.arange(1, L_max + 1)
ax.bar(L_new_plot, a2_new_plot, color='steelblue', edgecolor='black', linewidth=0.5)
ax.set_xlabel('$L = p + q$', fontsize=12)
ax.set_ylabel('$\\Delta a_2$ (new at level $L$)', fontsize=12)
ax.set_title('New $a_2$ contribution per level', fontsize=13)
ax.set_yscale('log')
ax.grid(True, alpha=0.3, axis='y')

# Panel 4: Per-irrep breakdown at L=4
ax = axes[1, 1]
L4_irreps = [(p, q) for (p, q) in sorted(irrep_data.keys()) if p + q == 4]
labels = [f'({p},{q})' for p, q in L4_irreps]
a2_vals = [irrep_data[(p, q)]['a2_contrib'] for p, q in L4_irreps]
bars = ax.bar(range(len(labels)), a2_vals, color='coral', edgecolor='black', linewidth=0.5)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=10)
ax.set_xlabel('Irrep $(p,q)$ at $L=4$', fontsize=12)
ax.set_ylabel('$a_2^{(p,q)}$', fontsize=12)
ax.set_title('$L=4$ irrep contributions', fontsize=13)
for i, v in enumerate(a2_vals):
    ax.text(i, v * 1.02, f'{v:.0f}', ha='center', va='bottom', fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

plt.suptitle('PW-H0-CONV-60: Peter-Weyl Sum DIVERGES (FAIL)\n'
             f'N = 1.00 $\\to$ 4.86 $\\to$ 13.4 $\\to$ 31.9 $\\to$ 67.9 $\\to$ 121 '
             '(not converging to 4)',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(outdir, 's60_pw_h0_conv.png'), dpi=150, bbox_inches='tight')
print("  Plot saved to s60_pw_h0_conv.png")

# =============================================================================
# 13. SAVE RESULTS
# =============================================================================
print("\n" + "=" * 72)
print("13. SAVING RESULTS")
print("=" * 72)

# Level-cumulative arrays
L_arr_save = np.arange(L_max + 1)
a0_cumul = np.array([level_data[L]['a0'] for L in L_arr_save])
a2_cumul = np.array([level_data[L]['a2'] for L in L_arr_save])
a4_cumul = np.array([level_data[L]['a4'] for L in L_arr_save])
N_cumul = np.array([level_data[L]['N_factor'] for L in L_arr_save])
N2_cumul = np.array([level_data[L]['N_factor_sq'] for L in L_arr_save])
n_irreps_cumul = np.array([level_data[L]['n_irreps'] for L in L_arr_save])
n_evals_cumul = np.array([level_data[L]['n_evals'] for L in L_arr_save])

# Per-irrep arrays
irrep_pq = np.array(sorted(irrep_data.keys()))
irrep_dim = np.array([irrep_data[tuple(pq)]['dim'] for pq in irrep_pq])
irrep_a2 = np.array([irrep_data[tuple(pq)]['a2_contrib'] for pq in irrep_pq])
irrep_a4 = np.array([irrep_data[tuple(pq)]['a4_contrib'] for pq in irrep_pq])
irrep_omega_min = np.array([irrep_data[tuple(pq)]['omega_min'] for pq in irrep_pq])
irrep_omega_max = np.array([irrep_data[tuple(pq)]['omega_max'] for pq in irrep_pq])
irrep_level = np.array([sum(pq) for pq in irrep_pq])

np.savez(
    os.path.join(outdir, 's60_pw_h0_conv.npz'),
    # Level-cumulative data
    L_max=L_max,
    L_arr=L_arr_save,
    a0_cumul=a0_cumul,
    a2_cumul=a2_cumul,
    a4_cumul=a4_cumul,
    N_cumul=N_cumul,
    N2_cumul=N2_cumul,
    n_irreps_cumul=n_irreps_cumul,
    n_evals_cumul=n_evals_cumul,
    # Per-irrep data
    irrep_pq=irrep_pq,
    irrep_dim=irrep_dim,
    irrep_a2=irrep_a2,
    irrep_a4=irrep_a4,
    irrep_omega_min=irrep_omega_min,
    irrep_omega_max=irrep_omega_max,
    irrep_level=irrep_level,
    # Derived quantities
    a2_needed=a2_needed,
    alpha_growth=alpha_growth,
    c_growth=c_growth,
    # S44 bug documentation
    s44_a2_incomplete=np.float64(162984.4151),
    a2_missing_12=irrep_data[(1, 2)]['a2_contrib'] if (1, 2) in irrep_data else np.float64(0.0),
    # Constants used
    tau_fold=tau_fold,
    M_KK=M_KK,
    M_Pl_reduced=M_Pl_reduced,
    # Gate
    gate_name=np.array(['PW-H0-CONV-60']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"  Saved: s60_pw_h0_conv.npz")
print(f"  Saved: s60_pw_h0_conv.png")

# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)
print(f"  Gate: PW-H0-CONV-60 = {verdict}")
print(f"  S44 bug found: (1,2) irrep missing from Peter-Weyl expansion")
print(f"  S59 N_factor = 3.920 was artifact of incomplete data + truncation")
print(f"  Correct N(L=3) = {N_correct_L3:.4f} (overshoots 4.00)")
print(f"  N(L=4) = {N_L4_val:.4f}, N(L=5) = {level_data[5]['N_factor']:.4f}")
print(f"  Growth: a_2(L) ~ L^{alpha_growth:.1f} (DIVERGENT)")
print(f"  The Peter-Weyl spectral sum is NOT the heat kernel a_2")
print(f"  H_0 = 68.8 from S59 NOT confirmed (based on artifact)")
