#!/usr/bin/env python3
"""
Session 43 W5-1: Off-Jensen J-Symmetry Breaking (OFFJ-J-43)
================================================================

QUESTION: Does [J, D_K] = 0 persist for off-Jensen deformations?

CONTEXT:
  On Jensen: C2*conj(D_K(tau))*C2 = D_K(tau) for ALL tau. STRUCTURAL THEOREM (W3-3).
  J = C2*K is antilinear. The CPT condition is C2*D_K**C2 = D_K.
  This is proven to ALL orders on the Jensen family.

  The SOLE SURVIVING internal baryogenesis path requires off-Jensen deformation
  where connection coefficients are NOT guaranteed to preserve T-symmetry.

METHOD:
  1. Construct D_K at the fold (tau=0.15) for Jensen metric.
  2. Deform metric: g_ab -> g_ab + eps*(delta_a7*delta_b3 + delta_a3*delta_b7)
     This is the g_73 direction mixing u(1) and su(2) blocks.
  3. Recompute Christoffel symbols, Kosmann connection, Omega, D_K.
  4. Test C2*conj(D_K)*C2 = D_K for each epsilon.
  5. Compute ||C2*conj(D_K)*C2 - D_K|| / ||D_K|| = fractional J-breaking.

GATE OFFJ-J-43:
  PASS: nonzero AND < 10^{-12} (geometric epsilon_CP within CPT bounds)
  FAIL: > 10^{-12} (conflicts BASE 16 ppt)
  INFO: exactly zero (J-symmetry more general than proven)

Author: dirac-antimatter-theorist, Session 43 W5-1
Date: 2026-03-14
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import norm, inv, cholesky, eigvalsh
from scipy.linalg import eigh as scipy_eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants,
    compute_killing_form, jensen_metric, orthonormal_frame,
    frame_structure_constants, connection_coefficients,
    validate_connection, spinor_connection_offset,
    build_cliff8, build_chirality,
    U1_IDX, SU2_IDX, C2_IDX,
)

np.set_printoptions(precision=14, linewidth=140, suppress=True)
t0 = time.time()

# ======================================================================
#  Infrastructure
# ======================================================================
gens = su3_generators()
fabc = compute_structure_constants(gens)
Bk = compute_killing_form(fabc)
gammas = build_cliff8()
gamma9 = build_chirality(gammas)
I16 = np.eye(16, dtype=complex)

# J = C2*K (antilinear). Matrix part C2:
C2 = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]  # gamma_1*gamma_3*gamma_5*gamma_7
C1 = gammas[1] @ gammas[3] @ gammas[5] @ gammas[7]  # gamma_2*gamma_4*gamma_6*gamma_8

# Verify algebraic identities
assert np.max(np.abs(C2 @ C2 - I16)) < 1e-13, "C2^2 != +I"
assert np.max(np.abs(C1 @ C1 - I16)) < 1e-13, "C1^2 != +I"
assert np.max(np.abs(np.imag(C2))) < 1e-14, "C2 not real"
assert np.max(np.abs(np.imag(C1))) < 1e-14, "C1 not real"
g9_check = C2 @ C1
assert np.max(np.abs(g9_check - gamma9)) < 1e-13 or np.max(np.abs(g9_check + gamma9)) < 1e-13, \
    "gamma_9 != +-C2*C1"

print("=" * 78)
print("OFFJ-J-43: Off-Jensen J-Symmetry Breaking")
print("=" * 78)
print(f"  J = C2*K (antilinear), C2 = gamma_1*gamma_3*gamma_5*gamma_7")
print(f"  CPT condition: C2*conj(D_K)*C2 = D_K")
print(f"  Off-Jensen direction: g_73 (u(1)-su(2) cross-term)")
print(f"  Fold: tau = 0.15")
print()


# ======================================================================
#  Core function: build D_K for ARBITRARY positive-definite metric
# ======================================================================
def build_DK_general(g_metric, verbose=False):
    """
    Build the (0,0) sector Dirac operator D_K = i*Omega for a general
    left-invariant metric g_metric on SU(3).

    The metric need NOT be U(2)-invariant (i.e., can have off-diagonal blocks).

    Steps:
      1. Orthonormal frame E via Cholesky of g_metric
      2. Frame structure constants ft_{ab}^c in ON basis
      3. Levi-Civita connection Gamma^c_{ab} via Koszul formula
      4. Spinor connection offset Omega = (1/4) sum Gamma^b_{ac} gamma_a gamma_b gamma_c
      5. D_K = i * Omega (Hermitian Dirac operator)

    Args:
        g_metric: (8,8) positive definite metric tensor
        verbose: print diagnostics

    Returns:
        D_K: (16,16) Hermitian matrix
        Omega: (16,16) anti-Hermitian matrix
        Gamma: (8,8,8) connection coefficients
        E: (8,8) orthonormal frame
    """
    # Check positive definiteness
    evals_g = eigvalsh(g_metric)
    if np.min(evals_g) <= 0:
        raise ValueError(f"Metric not positive definite: min eigenvalue = {np.min(evals_g):.6e}")

    # Orthonormal frame
    L = cholesky(g_metric)  # g = L @ L.T
    E = inv(L)              # E @ g @ E.T = I

    # Frame structure constants
    ft = frame_structure_constants(fabc, E)

    # Connection coefficients
    Gamma = connection_coefficients(ft)
    mc_err = validate_connection(Gamma)
    if verbose:
        print(f"    Metric compatibility error: {mc_err:.2e}")

    # Spinor connection offset
    Omega = spinor_connection_offset(Gamma, gammas)

    # D_K = i * Omega
    D_K = 1j * Omega

    # Check Hermiticity of D_K
    h_err = np.max(np.abs(D_K - D_K.conj().T))
    if verbose:
        print(f"    D_K Hermiticity error: {h_err:.2e}")

    return D_K, Omega, Gamma, E


def test_j_symmetry(D_K):
    """
    Test the antilinear J-symmetry condition:
      C2 * conj(D_K) * C2 = D_K

    Returns:
        delta: ||C2*conj(D_K)*C2 - D_K||_F  (Frobenius norm of violation)
        relative: delta / ||D_K||_F           (fractional violation)
        plain_comm: ||[C2, D_K]||_F           (plain commutator, for reference)
        plain_rel: plain_comm / ||D_K||_F
    """
    # Antilinear J condition: C2 * conj(D_K) * C2 should equal D_K
    JDJ = C2 @ np.conj(D_K) @ C2
    diff = JDJ - D_K
    delta = norm(diff, 'fro')
    dk_norm = norm(D_K, 'fro')
    relative = delta / dk_norm if dk_norm > 1e-30 else 0.0

    # Plain commutator [C2, D_K] = C2*D_K - D_K*C2
    comm = C2 @ D_K - D_K @ C2
    plain_comm = norm(comm, 'fro')
    plain_rel = plain_comm / dk_norm if dk_norm > 1e-30 else 0.0

    return delta, relative, plain_comm, plain_rel


# ======================================================================
#  Deformed metric construction
# ======================================================================
def deformed_metric(tau, eps_73):
    """
    Construct metric g(tau, eps) = Jensen(tau) + eps * (delta_a7*delta_b3 + delta_a3*delta_b7).

    In 0-indexed arrays: direction 7 = index 7 (u(1)), direction 3 = index 2 (su(2), lambda_3).
    Wait — careful with indexing. Our generators are indexed 0-7 corresponding to
    lambda_1 through lambda_8. So:
      "direction 3" in the physical frame = index 2 (lambda_3, su(2))
      "direction 7" in the physical frame = index 6 (lambda_7, C^2)

    BUT the task says g_73 mixes u(1) and C^2. Let me re-read:
    "g_73 direction: off-diagonal metric component mixing the u(1) and C^2 blocks.
     In the orthonormal frame {e^1,...,e^8}, g_73 means adding a cross-term between
     direction 7 (u(1) generator) and direction 3 (one of the C^2 directions)."

    In our convention:
      U1_IDX = [7]  (lambda_8 = index 7)
      SU2_IDX = [0, 1, 2]  (lambda_1,2,3 = indices 0,1,2)
      C2_IDX = [3, 4, 5, 6]  (lambda_4,5,6,7 = indices 3,4,5,6)

    The task says direction 7 = u(1) and direction 3 = one of the C^2 directions.
    With 1-indexing: direction 7 = our index 6 (lambda_7, C^2), direction 3 = our index 2 (lambda_3, su(2)).

    Hmm, there's ambiguity. The task description says:
    "direction 7 (u(1) generator)" — but in our setup, u(1) is lambda_8 = index 7.
    "direction 3 (one of the C^2 directions)" — but lambda_3 = index 2 is su(2), not C^2.

    Re-reading: "g_73 direction: off-diagonal metric component mixing the u(1) and C^2 blocks."
    So g_73 means row 7, column 3 in the 8x8 metric. That's index (6, 2) in 0-based.
    But direction 7 is lambda_7 (index 6, C^2) and direction 3 is lambda_3 (index 2, su(2)).
    That mixes C^2 and su(2), not u(1) and C^2.

    The ZMATRIX-43 computation (W4-1) found g_73 as the softest off-Jensen direction.
    Let me check: the 3D off-Jensen space has coordinates {T1 = u(1) scale, T2 = cross-block,
    T3 = Jensen}. The "g_73" direction from W4-1 refers to directions in the HESSIAN of the
    spectral action, which may not literally be the (7,3) matrix element.

    I will test BOTH interpretations:
      (A) g_{73} in 1-indexed = g_{6,2} in 0-indexed (lambda_7 x lambda_3 = C^2 x su(2))
      (B) g_{7,3} in 0-indexed = lambda_8 x lambda_4 = u(1) x C^2

    Interpretation (B) is more physical: it breaks the U(2)-invariance by coupling
    the u(1) block to a C^2 direction. This is what the task description intends.

    Args:
        tau: Jensen parameter
        eps_73: off-diagonal perturbation strength

    Returns:
        g: (8,8) positive definite metric (if eps small enough)
    """
    g = jensen_metric(Bk, tau)

    # Interpretation B: index 7 (u(1), lambda_8) with index 3 (C^2, lambda_4)
    # This mixes u(1) and C^2, breaking the block-diagonal U(2)-invariant structure
    a, b = 7, 3  # 0-indexed: lambda_8 and lambda_4
    g[a, b] += eps_73
    g[b, a] += eps_73

    return g


def deformed_metric_su2_c2(tau, eps_73):
    """Alternative: mix su(2) direction (index 2, lambda_3) with C^2 (index 3, lambda_4)."""
    g = jensen_metric(Bk, tau)
    a, b = 2, 3  # lambda_3 and lambda_4
    g[a, b] += eps_73
    g[b, a] += eps_73
    return g


# ======================================================================
#  Also test ALL 28 off-diagonal directions
# ======================================================================
def test_all_offdiag_directions(tau, eps):
    """
    Test J-breaking for ALL 28 independent off-diagonal metric perturbations.

    Returns list of (i, j, relative_J_breaking) sorted by J_breaking descending.
    """
    results = []
    for i in range(8):
        for j in range(i+1, 8):
            g = jensen_metric(Bk, tau)
            g[i, j] += eps
            g[j, i] += eps
            # Check positive definiteness
            evals_g = eigvalsh(g)
            if np.min(evals_g) <= 0:
                results.append((i, j, np.nan, "NOT PD"))
                continue
            try:
                D_K, _, _, _ = build_DK_general(g)
                delta, relative, _, _ = test_j_symmetry(D_K)
                results.append((i, j, relative, "OK"))
            except Exception as e:
                results.append((i, j, np.nan, str(e)))

    results.sort(key=lambda x: -x[2] if not np.isnan(x[2]) else -1e30)
    return results


# ======================================================================
#  Main computation
# ======================================================================
print("=" * 78)
print("STEP 1: Jensen baseline at tau=0.15")
print("=" * 78)

TAU_FOLD = 0.15
g_jensen = jensen_metric(Bk, TAU_FOLD)
D_K_jensen, Omega_jensen, Gamma_jensen, E_jensen = build_DK_general(g_jensen, verbose=True)

# J-symmetry on Jensen (should be exact)
delta_j, rel_j, plain_j, plain_rel_j = test_j_symmetry(D_K_jensen)
print(f"\nJensen J-symmetry:")
print(f"  ||C2*conj(D_K)*C2 - D_K|| = {delta_j:.6e}")
print(f"  Relative = {rel_j:.6e}")
print(f"  ||[C2, D_K]|| = {plain_j:.6e}")
print(f"  Plain relative = {plain_rel_j:.6e}")
print(f"  ||D_K|| = {norm(D_K_jensen, 'fro'):.6f}")

# Eigenvalues of D_K on Jensen
evals_jensen = eigvalsh(D_K_jensen)
print(f"  D_K eigenvalues (Jensen): {np.sort(evals_jensen)}")

# ======================================================================
print("\n" + "=" * 78)
print("STEP 2: g_73 deformation (u(1) x C^2, indices [7,3])")
print("=" * 78)

epsilons = [0.001, 0.005, 0.01, 0.02, 0.05, 0.1]
results_73 = []

for eps in epsilons:
    g_def = deformed_metric(TAU_FOLD, eps)

    # Check positive definiteness
    evals_g = eigvalsh(g_def)
    min_eval = np.min(evals_g)

    if min_eval <= 0:
        print(f"  eps={eps:.3f}: NOT positive definite (min eigenvalue = {min_eval:.6e})")
        results_73.append({
            'eps': eps, 'delta_J': np.nan, 'relative_J': np.nan,
            'plain_comm': np.nan, 'min_g_eval': min_eval, 'status': 'NOT_PD'
        })
        continue

    D_K_def, Omega_def, Gamma_def, E_def = build_DK_general(g_def, verbose=False)
    delta, relative, plain_c, plain_r = test_j_symmetry(D_K_def)

    # Also compute eigenvalue shift
    evals_def = eigvalsh(D_K_def)
    max_eval_shift = np.max(np.abs(np.sort(evals_def) - np.sort(evals_jensen)))

    print(f"  eps={eps:.4f}: ||J-break||/||D_K|| = {relative:.6e}, "
          f"||[C2,D_K]||/||D_K|| = {plain_r:.6e}, "
          f"max_eval_shift = {max_eval_shift:.6e}, "
          f"min_g_eval = {min_eval:.4f}")

    results_73.append({
        'eps': eps, 'delta_J': delta, 'relative_J': relative,
        'plain_comm': plain_c, 'plain_rel': plain_r,
        'max_eval_shift': max_eval_shift,
        'min_g_eval': min_eval, 'status': 'OK',
        'evals': evals_def,
    })

# ======================================================================
print("\n" + "=" * 78)
print("STEP 3: Alternative direction su(2) x C^2 (indices [2,3])")
print("=" * 78)

results_23 = []
for eps in epsilons:
    g_def = deformed_metric_su2_c2(TAU_FOLD, eps)
    evals_g = eigvalsh(g_def)
    min_eval = np.min(evals_g)

    if min_eval <= 0:
        print(f"  eps={eps:.3f}: NOT positive definite")
        results_23.append({'eps': eps, 'relative_J': np.nan, 'status': 'NOT_PD'})
        continue

    D_K_def, _, _, _ = build_DK_general(g_def)
    delta, relative, plain_c, plain_r = test_j_symmetry(D_K_def)

    print(f"  eps={eps:.4f}: ||J-break||/||D_K|| = {relative:.6e}, "
          f"||[C2,D_K]||/||D_K|| = {plain_r:.6e}")

    results_23.append({
        'eps': eps, 'delta_J': delta, 'relative_J': relative,
        'plain_comm': plain_c, 'plain_rel': plain_r,
        'min_g_eval': min_eval, 'status': 'OK',
    })

# ======================================================================
print("\n" + "=" * 78)
print("STEP 4: All 28 off-diagonal directions at eps=0.01")
print("=" * 78)

EPS_SCAN = 0.01
all_dir_results = test_all_offdiag_directions(TAU_FOLD, EPS_SCAN)

print(f"\n  {'Dir':>8}  {'Block':>20}  {'||J-break||/||D_K||':>22}  {'Status':>8}")
print(f"  {'-'*8}  {'-'*20}  {'-'*22}  {'-'*8}")

# Label each direction by which blocks it connects
def label_dir(i, j):
    """Identify which su(3) subspaces indices i,j belong to."""
    labels = {}
    for idx in U1_IDX:
        labels[idx] = "u(1)"
    for idx in SU2_IDX:
        labels[idx] = "su(2)"
    for idx in C2_IDX:
        labels[idx] = "C^2"
    return f"{labels.get(i,'?')}({i})-{labels.get(j,'?')}({j})"

for i, j, rel, status in all_dir_results:
    lbl = label_dir(i, j)
    if np.isnan(rel):
        print(f"  ({i},{j})  {lbl:>20}  {'N/A':>22}  {status:>8}")
    else:
        print(f"  ({i},{j})  {lbl:>20}  {rel:>22.6e}  {status:>8}")


# ======================================================================
print("\n" + "=" * 78)
print("STEP 5: Epsilon scaling analysis (power law)")
print("=" * 78)

# For the g_73 direction, check if J-breaking scales as eps^n
valid_73 = [(r['eps'], r['relative_J']) for r in results_73 if r['status'] == 'OK' and r['relative_J'] > 1e-16]

if len(valid_73) >= 2:
    log_eps = np.log10([v[0] for v in valid_73])
    log_rel = np.log10([v[1] for v in valid_73])

    # Linear fit in log-log space
    if len(log_eps) >= 2:
        coeffs = np.polyfit(log_eps, log_rel, 1)
        power = coeffs[0]
        intercept = coeffs[1]
        print(f"  g_73 direction: J-breaking ~ eps^{power:.3f}")
        print(f"  Log-log fit: log10(rel) = {power:.3f} * log10(eps) + {intercept:.3f}")

        # At what epsilon would J-breaking reach 10^{-12}?
        if power > 0:
            eps_threshold = 10**( (-12 - intercept) / power )
            print(f"  J-breaking = 10^{{-12}} at eps = {eps_threshold:.6e}")

            # Physical interpretation: relate eps to energy scale
            # eps is a dimensionless deformation of the metric
            # In physical units: eps * M_KK^2 ~ energy^2 of deformation
            # For M_KK ~ 10^{16-17} GeV, even eps ~ 10^{-10} gives E ~ 10^{6-7} GeV
            print(f"  For M_KK = 10^16 GeV: eps_threshold corresponds to E_deform ~ {eps_threshold**0.5 * 1e16:.2e} GeV")
else:
    print("  Insufficient data for power law fit")
    power = None


# ======================================================================
print("\n" + "=" * 78)
print("STEP 6: Multi-tau scan of g_73 at eps=0.01")
print("=" * 78)

taus = [0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.50, 1.00, 1.50]
tau_results = []

for tau in taus:
    g_def = deformed_metric(tau, 0.01)
    evals_g = eigvalsh(g_def)
    if np.min(evals_g) <= 0:
        tau_results.append((tau, np.nan, 'NOT_PD'))
        continue

    D_K_def, _, _, _ = build_DK_general(g_def)
    delta, relative, _, _ = test_j_symmetry(D_K_def)
    tau_results.append((tau, relative, 'OK'))
    print(f"  tau={tau:.2f}: ||J-break||/||D_K|| = {relative:.6e}")


# ======================================================================
print("\n" + "=" * 78)
print("STEP 7: Comparison to experimental bounds")
print("=" * 78)

# BASE: m(pbar)/m(p) = 1 +/- 16 ppt => |delta_m/m| < 1.6e-11
# ALPHA: 1S-2S at 2 ppt => |delta_E/E| < 2e-12
# These constrain CPT-violating mass splitting.
# In NCG: mass from D_K eigenvalues. J-breaking delta means
# spec(D_K) != spec(conj(D_K)) shifted, i.e., m(particle) != m(antiparticle)

# The fractional J-breaking ||C2*D_K^**C2 - D_K||/||D_K|| directly measures
# the fractional CPT violation in the Dirac spectrum.
# Converting to SME coefficients:
# In the minimal SME, CPT-violating Dirac couplings enter as b_mu and d_mu_nu.
# The b_0 coefficient has dimension [Energy]. At the KK scale:
# |b_0| ~ delta_J * M_KK
# For M_KK ~ 10^16 GeV and delta_J = fractional J-breaking:

from canonical_constants import M_KK_gravity as M_KK  # 7.43e16 GeV (was 1e16)

print(f"\n  Experimental CPT bounds:")
print(f"  BASE: |m(pbar)/m(p) - 1| < 1.6e-11")
print(f"  ALPHA: |delta_E_1S2S / E| < 2e-12")
print(f"  Electron |b_0^e| < 2e-25 GeV (Kostelecky tables)")
print(f"  Quark |b^u| < 1e-21 GeV")
print()

valid_results = [(r['eps'], r['relative_J']) for r in results_73 if r['status'] == 'OK']
if valid_results:
    for eps, rel_J in valid_results:
        b0_estimate = rel_J * M_KK
        print(f"  eps={eps:.4f}: J-breaking = {rel_J:.4e}")
        print(f"    => |b_0| ~ {b0_estimate:.2e} GeV "
              f"({'BELOW' if b0_estimate < 2e-25 else 'ABOVE'} electron bound 2e-25 GeV)")
        print(f"    => |delta_m/m| ~ {rel_J:.2e} "
              f"({'BELOW' if rel_J < 1.6e-11 else 'ABOVE'} BASE 16 ppt)")


# ======================================================================
print("\n" + "=" * 78)
print("STEP 8: Cross-check with full (p,q) sectors at eps=0.01")
print("=" * 78)

# The J-symmetry on larger sectors (1,0), (0,1), (1,1) should also be tested
# D_pi = sum_a rho(e_a) x gamma_a + I x Omega
# For off-Jensen, the E frame and Omega change; rho does not.
# J acts on the spinor factor only: J_pi = I_{dim_rho} x C2 * K
# The antilinear condition becomes:
#   (I x C2) * conj(D_pi) * (I x C2) = D_pi
# This splits into:
#   sum_a conj(rho(e_a)) x C2*conj(gamma_a)*C2 + I x C2*conj(Omega)*C2
# = sum_a rho(e_a) x gamma_a + I x Omega
#
# For the rho part: conj(rho(e_a)) = -conj(e_a)^T for fundamental.
# For anti-Hermitian gens: conj(e_a) = e_a^dag = -e_a, so conj(rho(e_a)) = rho(e_a).
# For C2*conj(gamma_a)*C2: since gamma_a are real Hermitian in our basis,
# conj(gamma_a) = gamma_a, so C2*gamma_a*C2.
# If [C2, gamma_a] = 0 for all a: this just gives gamma_a, and the sum is unchanged.
# If {C2, gamma_a} = 0 for some a: those terms flip sign.
#
# C2 = gamma_1*gamma_3*gamma_5*gamma_7 (odd gammas).
# C2 commutes with gamma_1, gamma_3, gamma_5, gamma_7 (they anticommute with 3 others
# in C2 and commute with themselves, net = even number of sign flips = +1).
# C2 anticommutes with gamma_2, gamma_4, gamma_6, gamma_8 (odd number of sign flips).
#
# Wait, let me be precise. For gamma_a with a in {1,3,5,7} (0-indexed: 0,2,4,6):
# C2 = gamma_1*gamma_3*gamma_5*gamma_7. Moving gamma_a past C2:
# gamma_a * C2 = gamma_a * gamma_1*gamma_3*gamma_5*gamma_7
# For a=1 (index 0): gamma_1*gamma_1*gamma_3*gamma_5*gamma_7 = gamma_3*gamma_5*gamma_7
# C2*gamma_1 = gamma_1*gamma_3*gamma_5*gamma_7*gamma_1
# Move gamma_1 past gamma_7: -gamma_1*gamma_3*gamma_5*gamma_1*gamma_7
# ... this gets complicated. Let me just compute numerically.

print("  Checking C2*gamma_a*C2 vs gamma_a:")
for a in range(8):
    result = C2 @ gammas[a] @ C2
    # Compare to +gamma_a and -gamma_a
    plus_err = np.max(np.abs(result - gammas[a]))
    minus_err = np.max(np.abs(result + gammas[a]))
    sign = "+1" if plus_err < 1e-13 else ("-1" if minus_err < 1e-13 else "OTHER")
    print(f"    gamma_{a+1}: C2*gamma_{a+1}*C2 = {sign} * gamma_{a+1}")

# The D_pi on an irrep has the form:
#   D_pi = sum_{a,b} E_{ab} rho(X_b) x gamma_a + I x Omega
# The antilinear J condition on the full D_pi:
#   (I x C2) conj(D_pi) (I x C2) = D_pi
# Using the E frame (real) and rho(X_b) (anti-Hermitian, generally complex):
#   conj(D_pi) = sum E_{ab} conj(rho(X_b)) x conj(gamma_a) + I x conj(Omega)
# Since gammas are real: conj(gamma_a) = gamma_a.
# (I x C2) conj(D_pi) (I x C2) = sum E_{ab} conj(rho(X_b)) x C2*gamma_a*C2 + I x C2*conj(Omega)*C2
#
# For J-symmetry on the (0,0) sector (Omega only):
# C2*conj(Omega)*C2 = Omega is the condition.
# For higher sectors, we additionally need:
# conj(rho(X_b)) x C2*gamma_a*C2 = rho(X_b) x gamma_a for all a,b.
#
# The fundamental rho(X_b) = e_b (anti-Hermitian 3x3). conj(e_b) = e_b^* = -e_b^T = e_b^dag = -e_b.
# Wait: e_b = -i/2 * lambda_b. conj(e_b) = i/2 * conj(lambda_b).
# For Gell-Mann: lambda_1,3,4,6,8 are real, lambda_2,5,7 are imaginary.
# So conj(e_b) = -e_b for b in {2,5,7} (imaginary lambda), conj(e_b) = e_b for others... no.
# e_b = -i/2 * lambda_b. conj(e_b) = i/2 * conj(lambda_b).
# If lambda_b is real: conj(e_b) = i/2 * lambda_b = -e_b.
# If lambda_b is purely imaginary (lambda_2,5,7): conj(e_b) = i/2 * (-lambda_b) = -(-i/2*lambda_b) ...
# Actually: lambda_2 has entries +/-i, so conj(lambda_2) = -lambda_2. Then conj(e_b) = i/2*(-lambda_b) = -(i/2*lambda_b) = -conj(e_b)...
# This is getting circular. Just compute.

print("\n  Checking conj(e_b) vs e_b for fundamental rep:")
for b in range(8):
    eb_conj = np.conj(gens[b])
    plus_err = np.max(np.abs(eb_conj - gens[b]))
    minus_err = np.max(np.abs(eb_conj + gens[b]))
    if plus_err < 1e-14:
        print(f"    e_{b+1}: conj(e_{b+1}) = +e_{b+1}  (real generator)")
    elif minus_err < 1e-14:
        print(f"    e_{b+1}: conj(e_{b+1}) = -e_{b+1}  (imaginary generator)")
    else:
        print(f"    e_{b+1}: conj(e_{b+1}) != ±e_{b+1}  (mixed)")

# Now test (1,0) sector at eps=0.01
# IMPORTANT: J maps (p,q) -> (q,p). On the SAME sector (p,q), the antilinear
# condition is C2*conj(Omega)*C2 = Omega (spinor-only part). The representation
# matrices are mapped conj(rho_{(p,q)}(X_b)) = rho_{(q,p)}(X_b), so J
# interchanges (p,q) and (q,p) sectors entirely. Testing J within a single
# (p,q) != (q,p) sector is WRONG — it must compare D_{(p,q)} with conj(D_{(q,p)}).
# For self-conjugate (p,p), J acts within the sector.

print("\n  Testing higher sectors at eps=0.01:")
print("  NOTE: J maps (p,q) -> (q,p). Within a single non-self-conjugate sector,")
print("  the test is: spec(D_{(p,q)}) = -spec(D_{(q,p)}) [spectral pairing].")
print("  For self-conjugate (p,p): C2*conj(D_pi)*C2 = D_pi.")
from tier1_dirac_spectrum import get_irrep, dirac_operator_on_irrep

EPS_TEST = 0.01
g_def_test = deformed_metric(TAU_FOLD, EPS_TEST)
D_K_test, Omega_test, Gamma_test, E_test = build_DK_general(g_def_test)

# (1,0) vs (0,1): spectral comparison
rho_10, dim_10 = get_irrep(1, 0, gens, fabc)
D_pi_10 = dirac_operator_on_irrep(rho_10, E_test, gammas, Omega_test)
evals_10 = np.sort(eigvalsh(D_pi_10))

rho_01, dim_01 = get_irrep(0, 1, gens, fabc)
D_pi_01 = dirac_operator_on_irrep(rho_01, E_test, gammas, Omega_test)
evals_01 = np.sort(eigvalsh(D_pi_01))

# J maps (1,0) -> (0,1) with eigenvalue negation: spec(D_{(0,1)}) should equal -spec(D_{(1,0)})
spec_pairing_err = np.max(np.abs(evals_01 + evals_10[::-1]))
print(f"    (1,0) vs (0,1): max|lambda_{(0,1)} + lambda_{(1,0)}| = {spec_pairing_err:.6e}")
print(f"    (Jensen: spectral pairing from gamma_9 guarantees this)")

# (1,1) adjoint — self-conjugate, test J within sector
rho_11, dim_11 = get_irrep(1, 1, gens, fabc)
D_pi_11 = dirac_operator_on_irrep(rho_11, E_test, gammas, Omega_test)

# For the adjoint, rho(X_b) are REAL matrices (structure constants are real)
# So conj(rho(X_b)) = rho(X_b). The J condition reduces to:
# sum E_{ab} rho(X_b) x C2*gamma_a*C2 + I x C2*conj(Omega)*C2 = D_pi
# The Omega part is already proven exact. The rho part:
# C2*gamma_a*C2 = s_a * gamma_a where s_a = ±1 (computed above)
# For real rho: conj(rho(X_b)) = rho(X_b)
# So the J condition becomes: sum E_{ab} rho(X_b) x s_a*gamma_a = sum E_{ab} rho(X_b) x gamma_a
# This requires s_a = +1 for all a with nonzero E_{ab}. Since s_a = -1 for odd gammas,
# the full D_pi J condition is EXPECTED to fail on non-trivial sectors.
# This is NOT J-breaking — J maps the (1,1) sector to itself but with a representation
# conjugation that is trivial for real reps, so the Clifford sign matters.
# The correct test for mass equality is: spec(D_{(p,q)}) = {±lambda} (symmetric about 0)
# which follows from gamma_9 anticommuting with D_pi.

evals_11 = np.sort(eigvalsh(D_pi_11))
# Check spectral symmetry: eigenvalues come in ±pairs
n_11 = len(evals_11)
evals_pos = evals_11[n_11//2:]
evals_neg = evals_11[:n_11//2]
pair_err = np.max(np.abs(evals_pos + evals_neg[::-1]))
print(f"    (1,1) self-conjugate: spectral ± pairing error = {pair_err:.6e}")
print(f"    (Spectral pairing from {{gamma_9, D_pi}} = 0 guarantees CPT mass equality)")


# ======================================================================
print("\n" + "=" * 78)
print("STEP 9: Algebraic analysis — WHY J-breaking occurs (or not)")
print("=" * 78)

# The antilinear J condition C2*conj(D_K)*C2 = D_K decomposes as:
# D_K = Re(D_K) + i*Im(D_K), where Re and Im are Hermitian.
# conj(D_K) = Re(D_K) - i*Im(D_K)
# C2*conj(D_K)*C2 = C2*Re(D_K)*C2 - i*C2*Im(D_K)*C2
# Condition: C2*Re(D_K)*C2 = Re(D_K) AND C2*Im(D_K)*C2 = -Im(D_K)
# i.e., Re(D_K) commutes with C2, Im(D_K) anticommutes with C2.

D_K_off = D_K_test  # Already computed at eps=0.01
Re_DK = 0.5 * (D_K_off + D_K_off.conj().T)  # Should be D_K itself if Hermitian
Im_DK_mat = (D_K_off - D_K_off.conj().T) / (2j)

# But D_K is Hermitian! So Im part should be zero...
# Wait: D_K = i*Omega where Omega is anti-Hermitian. D_K is Hermitian.
# D_K^* = conj(i*Omega) = -i*conj(Omega) = -i*(-Omega^T) = i*Omega^T
# For anti-Hermitian Omega: Omega^dag = -Omega, so Omega^T = -conj(Omega) = -Omega^*.
# D_K^* = conj(D_K) = -i*Omega^*
#
# Hmm. D_K is Hermitian means D_K = D_K^dag. But conj(D_K) != D_K in general
# because D_K can have complex entries even though it's Hermitian (e.g., off-diag = z, z* pair).
#
# The condition C2*conj(D_K)*C2 = D_K with D_K Hermitian:
# Split D_K = A + iB where A = Re(D_K), B = Im(D_K) (element-wise real/imag parts)
# Hermitian: A = A^T, B = -B^T (A is real symmetric, B is real antisymmetric)
# conj(D_K) = A - iB
# C2*(A-iB)*C2 = C2*A*C2 - i*C2*B*C2 = A + iB
# => C2*A*C2 = A (C2 commutes with real part)
# => C2*B*C2 = -B (C2 anticommutes with imaginary part)

# Since C2 is real: these are plain matrix equations (no conjugation needed).

A = np.real(D_K_off)
B = np.imag(D_K_off)

comm_A = C2 @ A @ C2 - A
anticomm_B = C2 @ B @ C2 + B

print(f"  D_K decomposition (off-Jensen, eps=0.01):")
print(f"    ||Re(D_K)|| = {norm(A, 'fro'):.6f}")
print(f"    ||Im(D_K)|| = {norm(B, 'fro'):.6f}")
print(f"    ||C2*Re(D_K)*C2 - Re(D_K)|| = {norm(comm_A, 'fro'):.6e}")
print(f"    ||C2*Im(D_K)*C2 + Im(D_K)|| = {norm(anticomm_B, 'fro'):.6e}")
print(f"    J-breaking from Re part: {norm(comm_A, 'fro') / norm(D_K_off, 'fro'):.6e}")
print(f"    J-breaking from Im part: {norm(anticomm_B, 'fro') / norm(D_K_off, 'fro'):.6e}")

# Repeat for Jensen baseline
A_j = np.real(D_K_jensen)
B_j = np.imag(D_K_jensen)
comm_A_j = C2 @ A_j @ C2 - A_j
anticomm_B_j = C2 @ B_j @ C2 + B_j
print(f"\n  Jensen baseline:")
print(f"    ||Re(D_K)|| = {norm(A_j, 'fro'):.6f}")
print(f"    ||Im(D_K)|| = {norm(B_j, 'fro'):.6f}")
print(f"    ||C2*Re(D_K)*C2 - Re(D_K)|| = {norm(comm_A_j, 'fro'):.6e}")
print(f"    ||C2*Im(D_K)*C2 + Im(D_K)|| = {norm(anticomm_B_j, 'fro'):.6e}")


# ======================================================================
print("\n" + "=" * 78)
print("SUMMARY AND GATE VERDICT")
print("=" * 78)

# Collect key results
print("\n  g_73 direction (u(1) x C^2) J-breaking vs epsilon:")
print(f"  {'eps':>10}  {'||J-break||/||D_K||':>22}  {'||[C2,D_K]||/||D_K||':>22}")
for r in results_73:
    if r['status'] == 'OK':
        print(f"  {r['eps']:>10.4f}  {r['relative_J']:>22.6e}  {r['plain_rel']:>22.6e}")

print(f"\n  Jensen baseline: ||J-break||/||D_K|| = {rel_j:.6e}")

# Determine gate verdict
valid_offj = [r for r in results_73 if r['status'] == 'OK']
if valid_offj:
    max_J_break = max(r['relative_J'] for r in valid_offj)
    min_J_break = min(r['relative_J'] for r in valid_offj)

    if max_J_break < 1e-14:
        verdict = "INFO"
        verdict_desc = "J-symmetry preserved to machine precision even off-Jensen"
    elif min_J_break > 1e-12:
        verdict = "FAIL"
        verdict_desc = f"J-breaking {min_J_break:.2e} exceeds BASE 16 ppt at all tested eps"
    elif max_J_break > 1e-14 and max_J_break < 1e-12:
        verdict = "PASS"
        verdict_desc = f"Geometric epsilon_CP in range [{min_J_break:.2e}, {max_J_break:.2e}]"
    else:
        # Mixed: some eps give > 10^{-12}, some give < 10^{-12}
        # Need to find the eps at which J-breaking = 10^{-12}
        verdict = "CONDITIONAL"
        verdict_desc = f"J-breaking range [{min_J_break:.2e}, {max_J_break:.2e}] spans threshold"
else:
    verdict = "INCONCLUSIVE"
    verdict_desc = "No valid off-Jensen computations"

print(f"\n  GATE VERDICT: OFFJ-J-43 = {verdict}")
print(f"  {verdict_desc}")

if power is not None:
    print(f"  Scaling: J-breaking ~ eps^{power:.2f}")

elapsed = time.time() - t0
print(f"\n  Elapsed: {elapsed:.1f}s")


# ======================================================================
# Save data
# ======================================================================
out_npz = os.path.join(SCRIPT_DIR, 's43_offj_jsymm.npz')

save_dict = {
    'tau_fold': TAU_FOLD,
    'epsilons': np.array(epsilons),
    'jensen_J_break': rel_j,
    'jensen_plain_comm': plain_rel_j,
    'evals_jensen': evals_jensen,
}

# g_73 results
for i, r in enumerate(results_73):
    save_dict[f'g73_eps_{i}'] = r['eps']
    save_dict[f'g73_relJ_{i}'] = r.get('relative_J', np.nan)
    save_dict[f'g73_plain_{i}'] = r.get('plain_rel', np.nan)
    if 'evals' in r:
        save_dict[f'g73_evals_{i}'] = r['evals']

# All-direction scan
all_dir_arr = np.array([(i, j, rel) for i, j, rel, _ in all_dir_results])
save_dict['all_dir_scan'] = all_dir_arr

# Multi-tau scan
tau_scan_arr = np.array([(t, r, 1 if s == 'OK' else 0) for t, r, s in tau_results])
save_dict['tau_scan'] = tau_scan_arr

save_dict['verdict'] = verdict
save_dict['power_law'] = power if power is not None else np.nan

np.savez(out_npz, **save_dict)
print(f"\n  Saved: {out_npz}")


# ======================================================================
# Plot
# ======================================================================
out_png = os.path.join(SCRIPT_DIR, 's43_offj_jsymm.png')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('OFFJ-J-43: Off-Jensen J-Symmetry Breaking', fontsize=14, fontweight='bold')

# Panel 1: J-breaking vs epsilon for g_73
ax1 = axes[0, 0]
valid_eps = [r['eps'] for r in results_73 if r['status'] == 'OK']
valid_rel = [r['relative_J'] for r in results_73 if r['status'] == 'OK']
valid_plain = [r['plain_rel'] for r in results_73 if r['status'] == 'OK']

if valid_eps:
    ax1.semilogy(valid_eps, valid_rel, 'bo-', label=r'$\|C_2 D_K^* C_2 - D_K\|/\|D_K\|$ (antilinear)', markersize=8)
    ax1.semilogy(valid_eps, valid_plain, 'rs--', label=r'$\|[C_2, D_K]\|/\|D_K\|$ (plain)', markersize=6)
    ax1.axhline(y=1.6e-11, color='green', linestyle=':', alpha=0.7, label='BASE 16 ppt')
    ax1.axhline(y=2e-12, color='orange', linestyle=':', alpha=0.7, label='ALPHA 2 ppt')
    if power is not None:
        eps_fit = np.logspace(np.log10(min(valid_eps)), np.log10(max(valid_eps)), 50)
        rel_fit = 10**(power * np.log10(eps_fit) + intercept)
        ax1.semilogy(eps_fit, rel_fit, 'b:', alpha=0.4, label=rf'fit: $\varepsilon^{{{power:.1f}}}$')
ax1.set_xlabel(r'$\varepsilon_{73}$')
ax1.set_ylabel('Fractional J-breaking')
ax1.set_title(r'$g_{73}$ direction: J-breaking vs $\varepsilon$')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# Panel 2: All 28 off-diagonal directions
ax2 = axes[0, 1]
dir_labels = []
dir_vals = []
dir_colors = []
for i, j, rel, status in all_dir_results:
    if not np.isnan(rel):
        lbl = f"({i},{j})"
        dir_labels.append(lbl)
        dir_vals.append(rel)
        # Color by block type
        i_block = 'u1' if i in U1_IDX else ('su2' if i in SU2_IDX else 'c2')
        j_block = 'u1' if j in U1_IDX else ('su2' if j in SU2_IDX else 'c2')
        if i_block == j_block:
            dir_colors.append('blue')  # within-block
        else:
            dir_colors.append('red')   # cross-block

if dir_vals:
    bars = ax2.barh(range(len(dir_vals)), dir_vals, color=dir_colors, alpha=0.7)
    ax2.set_yticks(range(len(dir_labels)))
    ax2.set_yticklabels(dir_labels, fontsize=6)
    ax2.set_xlabel('Fractional J-breaking')
    ax2.set_title(r'All 28 off-diag dirs at $\varepsilon=0.01$')
    ax2.set_xscale('log')
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='red', alpha=0.7, label='cross-block'),
                       Patch(facecolor='blue', alpha=0.7, label='within-block')]
    ax2.legend(handles=legend_elements, fontsize=8)

# Panel 3: Multi-tau scan
ax3 = axes[1, 0]
valid_tau = [(t, r) for t, r, s in tau_results if s == 'OK']
if valid_tau:
    ts, rs = zip(*valid_tau)
    ax3.semilogy(ts, rs, 'go-', markersize=8)
    ax3.axhline(y=1.6e-11, color='green', linestyle=':', alpha=0.7, label='BASE 16 ppt')
    ax3.axhline(y=2e-12, color='orange', linestyle=':', alpha=0.7, label='ALPHA 2 ppt')
ax3.set_xlabel(r'$\tau$')
ax3.set_ylabel('Fractional J-breaking')
ax3.set_title(r'$g_{73}$ at $\varepsilon=0.01$: J-breaking vs $\tau$')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Panel 4: Eigenvalue spectrum shift
ax4 = axes[1, 1]
ax4.plot(np.arange(16), np.sort(evals_jensen), 'ko-', label='Jensen', markersize=6)
for r in results_73:
    if r['status'] == 'OK' and 'evals' in r:
        ax4.plot(np.arange(16), np.sort(r['evals']), 's--', alpha=0.6,
                 label=rf'$\varepsilon$={r["eps"]:.3f}', markersize=4)
ax4.set_xlabel('Eigenvalue index')
ax4.set_ylabel('D_K eigenvalue')
ax4.set_title('Eigenvalue spectrum shift')
ax4.legend(fontsize=7, ncol=2)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"  Saved: {out_png}")

print(f"\n  Total elapsed: {time.time()-t0:.1f}s")
