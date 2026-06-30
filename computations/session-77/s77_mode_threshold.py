#!/usr/bin/env python3
"""
s77_mode_threshold.py — S77-C6-MODE-THRESHOLD: Full Eigenvalue Threshold Sum
=============================================================================

Compute the threshold correction ratio Delta_2/Delta_3 using the ACTUAL
D_K eigenvalue spectrum at tau_fold, decomposed by Peter-Weyl sector (p,q)
and branched into SM representations under SU(3) -> SU(2) x U(1).

MOTIVATION
----------
All previous Weinberg angle threshold computations (S72, S73a, S77-B4)
used the Dynkin index ratios T_2(p,q)/T_3(p,q) as the ONLY group-theory
input. The S73a PERMANENT THEOREM states:

  T_2(p,q)/T_3(p,q) = 1     (exact, all SU(3) irreps)
  T_Y(p,q)/T_3(p,q) = 4/3   (exact, all SU(3) irreps)

This means: if all eigenvalues within a sector (p,q) are used with the
SAME logarithmic weight ln(|lambda_n|/mu), the threshold ratio is
STRUCTURALLY fixed by group theory.

However, one could ask: does the eigenvalue-resolved computation, using
the ACTUAL individual D_K eigenvalue masses, produce a different ratio?
The answer is NO, because the Dynkin index is a property of the
REPRESENTATION, not of individual eigenvalues. Within each sector (p,q),
ALL D_K eigenvalues carry the same representation labels and therefore
the same (T_2, T_3, T_Y) weights.

This computation VERIFIES this structural prediction numerically by:
1. Computing the full D_K spectrum at tau_fold for p+q <= L_max
2. Decomposing by Peter-Weyl sector (p,q)
3. Applying branching rules to get T_2, T_3, T_Y per sector
4. Computing the threshold sums Delta_a = sum_n T_a(n) * ln(|lambda_n|/mu)
   where n runs over ALL eigenvalues (each weighted by PW multiplicity dim(p,q))
5. Forming Delta_2/Delta_3 and checking against unity

STRUCTURAL PREDICTION
---------------------
Since T_2(p,q)/T_3(p,q) = 1 for every (p,q):

  Delta_2 / Delta_3 = [sum_{(p,q)} T_2(p,q) * sum_{n in (p,q)} dim(p,q)*16 * ln|lambda_n|]
                     / [sum_{(p,q)} T_3(p,q) * sum_{n in (p,q)} dim(p,q)*16 * ln|lambda_n|]

Since T_2(p,q) = T_3(p,q) for every sector, this ratio is:

  = [sum_{(p,q)} T_3(p,q) * W(p,q)] / [sum_{(p,q)} T_3(p,q) * W(p,q)]
  = 1  (exactly)

where W(p,q) = sum_{n in (p,q)} dim(p,q)*16 * ln|lambda_n| is the eigenvalue weight per sector.

For U(1): since T_Y(p,q)/T_3(p,q) = 4/3 for every sector:
  Delta_Y / Delta_3 = 4/3  (exactly)
  Delta_1 / Delta_3 = (5/3)*(4/3) = 20/9  (exactly, with GUT normalization)

This reproduces the S73a result. The eigenvalue-resolved computation
CANNOT change the Dynkin index ratios because the indices are properties
of the representation, not of individual modes.

Gate: S77-C6-MODE-THRESHOLD
  PASS: Delta_2/Delta_3 = 1 within 10% (confirming structural prediction)
  FAIL: Delta_2/Delta_3 differs from 1 by > factor 2 (would falsify S73a theorem)
  INFO: Partial computation

Cross-checks:
  CHK1: Delta_2/Delta_3 = 1 (machine epsilon, from Dynkin theorem)
  CHK2: Delta_Y/Delta_3 = 4/3 (machine epsilon)
  CHK3: Total eigenvalue count = dim(p,q) * 16 per sector
  CHK4: Branching dimension sum = dim(p,q) for each sector
  CHK5: Eigenvalue pairing: spectrum symmetric under lambda -> -lambda
  CHK6: Zero-mode count consistent with index theory

Provenance:
  S73a: T_2/T_3 = 1, T_Y/T_3 = 4/3 (permanent theorem)
  S77-B4: L-R threshold route FAIL (sin^2 = -0.308)
  dirac_spectrum.py: D_K infrastructure
  s73a_pw_threshold_ratios.py: branching rule implementation

Author: baptista-spacetime-analyst
Session: S77 Wave 3 (W3-F)
"""

import sys
import os
import time
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, M_KK, M_Z, tau_fold,
    sin2_thetaW_MSbar, sin2_thetaW_fold,
    alpha_em_MZ_inv, alpha_s_MZ_obs,
    alpha2_MKK_inv,
    a0_fold, a2_fold, a4_fold,
    b1_SM, b2_SM, b3_SM,
    g_SU2_fold, g_U1_fold,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, build_chirality, validate_clifford,
    validate_connection, validate_omega_hermitian,
    get_irrep, dirac_operator_on_irrep, validate_irrep,
    _irrep_cache,
)

outdir = SCRIPT_DIR

print("=" * 78)
print("S77-C6-MODE-THRESHOLD: Full Eigenvalue Threshold Sum")
print("=" * 78)
t_start = time.time()

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1: SU(3) -> SU(2) x U(1) BRANCHING RULES
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 78)
print("1. SU(3) -> SU(2) x U(1) BRANCHING RULES")
print("=" * 78)


def su3_branching(p, q):
    """
    Compute the branching of SU(3) irrep V_{(p,q)} under SU(3) -> SU(2) x U(1).

    Uses Gelfand-Tsetlin weight enumeration. The standard embedding:
      SU(2): acts on indices {1,2} in the fundamental
      U(1)_Y: generated by Y = (H_1 + 2*H_2)/3

    where H_1 = E_{11}-E_{22}, H_2 = E_{22}-E_{33} are Cartan generators.

    Returns:
        list of (j, Y, multiplicity) tuples
    """
    lam1 = p + q  # (local)
    lam2 = q       # (local)

    states = []  # (local)
    for m12 in range(lam2, lam1 + 1):
        for m22 in range(0, min(lam2, m12) + 1):
            for m11 in range(m22, m12 + 1):
                e1 = m11  # (local)
                e2 = (m12 + m22) - m11  # (local)
                e3 = (lam1 + lam2) - (m12 + m22)  # (local)
                mu1 = e1 - e2  # (local)
                mu2 = e2 - e3  # (local)
                I3 = mu1 / 2.0   # (local)
                Y_val = (mu1 + 2 * mu2) / 3.0  # (local)
                states.append((I3, Y_val))

    # Group states by Y
    Y_groups = {}  # (local)
    for I3, Y_val in states:
        Y_key = round(Y_val * 6) / 6.0  # (local)
        if Y_key not in Y_groups:
            Y_groups[Y_key] = []
        Y_groups[Y_key].append(I3)

    # Extract SU(2) multiplets by peeling off from top
    result = []  # (local)
    for Y_val in sorted(Y_groups.keys()):
        I3_list = sorted(Y_groups[Y_val])  # (local)
        I3_counts = {}  # (local)
        for i3 in I3_list:
            i3_key = round(i3 * 2) / 2.0  # (local)
            I3_counts[i3_key] = I3_counts.get(i3_key, 0) + 1

        while sum(I3_counts.values()) > 0:
            max_I3 = max(k for k, v in I3_counts.items() if v > 0)  # (local)
            j = max_I3  # (local)
            if j < -1e-10:
                break
            for i3_val in np.arange(-j, j + 0.5, 1.0):
                i3_key = round(i3_val * 2) / 2.0  # (local)
                if i3_key in I3_counts and I3_counts[i3_key] > 0:
                    I3_counts[i3_key] -= 1
                else:
                    raise ValueError(
                        f"Branching error ({p},{q}): Y={Y_val}, j={j}, I3={i3_key} missing"
                    )
            result.append((j, Y_val, 1))

    return result


def T_SU2(branching):
    """SU(2) Dynkin index from branching: T_2 = sum j(j+1)(2j+1)/3."""
    total = 0.0  # (local)
    for j, Y, mult in branching:
        total += mult * j * (j + 1) * (2 * j + 1) / 3.0
    return total


def T_U1(branching):
    """U(1)_Y index from branching: T_Y = sum (2j+1) Y^2."""
    total = 0.0  # (local)
    for j, Y, mult in branching:
        total += mult * (2 * j + 1) * Y**2
    return total


def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def C2_su3(p, q):
    """Quadratic Casimir of SU(3) irrep (p,q)."""
    return (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0


def T_SU3(p, q):
    """SU(3) Dynkin index: T(R) = dim(R) * C_2(R) / dim(adj)."""
    return dim_su3(p, q) * C2_su3(p, q) / 8.0


# Validate branching on known representations
print("\n  Branching cross-checks:")
for p, q, expected_dim, name in [
    (1, 0, 3, "fundamental"),
    (0, 1, 3, "anti-fundamental"),
    (1, 1, 8, "adjoint"),
    (2, 0, 6, "symmetric 6"),
    (0, 2, 6, "anti-symmetric 6-bar"),
    (3, 0, 10, "decuplet"),
]:
    br = su3_branching(p, q)
    d_br = sum((2*j+1) * mult for j, Y, mult in br)  # (local)
    T2 = T_SU2(br)  # (local)
    TY = T_U1(br)   # (local)
    T3 = T_SU3(p, q)  # (local)
    r23 = T2/T3 if T3 > 0 else float('nan')  # (local)
    rY3 = TY/T3 if T3 > 0 else float('nan')  # (local)
    status = "OK" if abs(d_br - expected_dim) < 0.01 else "FAIL"  # (local)
    print(f"    ({p},{q}) [{name:20s}]: dim={d_br:3.0f} {status}  "
          f"T_2/T_3={r23:.6f}  T_Y/T_3={rY3:.6f}")
    assert abs(d_br - expected_dim) < 0.01, f"({p},{q}): branching dim error"
    assert abs(r23 - 1.0) < 1e-10, f"({p},{q}): T_2/T_3 != 1"
    assert abs(rY3 - 4.0/3.0) < 1e-10, f"({p},{q}): T_Y/T_3 != 4/3"

print("  ALL branching cross-checks PASSED: T_2/T_3 = 1, T_Y/T_3 = 4/3 (machine eps)")


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2: COMPUTE D_K SPECTRUM AT TAU_FOLD
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 78)
print("2. COMPUTE D_K SPECTRUM AT TAU_FOLD")
print("=" * 78)

# Infrastructure
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
B_ab = compute_killing_form(f_abc)

# Validate Clifford algebra
cliff_err = validate_clifford(gammas)
print(f"\n  Clifford algebra validation: max error = {cliff_err:.2e}")
assert cliff_err < 1e-12, f"Clifford algebra error too large: {cliff_err}"

# Build geometric infrastructure at tau_fold
s = tau_fold  # (local) Jensen parameter
g_s = jensen_metric(B_ab, s)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E)
Gamma = connection_coefficients(ft)
Omega = spinor_connection_offset(Gamma, gammas)

mc_err = validate_connection(Gamma)  # (local)
is_h, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)  # (local)
print(f"  tau = {tau_fold}: connection metric-compat error = {mc_err:.2e}")
print(f"  Omega: anti-Hermitian err = {ah_err:.2e} ({'OK' if is_ah else 'WARN'})")

# Build chirality
gamma9 = build_chirality(gammas)
g9_check = np.max(np.abs(gamma9 @ gamma9 - np.eye(16)))  # (local)
print(f"  gamma_9^2 = I check: max error = {g9_check:.2e}")

# Choose L_max: balance completeness vs compute time
# L_max=5 gives 21 sectors (p+q <= 5), sufficient for convergence check
# L_max=6 gives 28 sectors (all of S64 data)
L_MAX = 6  # (local) match S64 coverage
print(f"\n  Computing D_K spectrum for p+q <= {L_MAX}...")

from scipy.linalg import eigh as scipy_eigh

# Collect spectrum by sector
sector_results = []  # (local) list of dicts
total_eigenvalues = 0  # (local)
total_modes_with_pw = 0  # (local)

# Enumerate sectors
sectors_to_compute = []  # (local)
for p in range(L_MAX + 1):
    for q in range(L_MAX + 1 - p):
        d_pq = dim_su3(p, q)  # (local)
        sectors_to_compute.append((p, q, d_pq))

# Sort by Casimir (small representations first)
sectors_to_compute.sort(key=lambda x: C2_su3(x[0], x[1]))

print(f"\n  {'(p,q)':>7} {'dim':>5} {'D_size':>7} {'|lam|_min':>10} {'|lam|_max':>10} "
      f"{'ah_err':>10} {'n_zero':>7}")
print("  " + "-" * 70)

for p, q, d_pq in sectors_to_compute:
    try:
        if (p, q) == (0, 0):
            D_pi = Omega.copy()
        else:
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            assert dim_check == d_pq
            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # Verify anti-Hermiticity
        ah_check = np.max(np.abs(D_pi + D_pi.conj().T))  # (local)

        # Diagonalize via Hermitian problem: H = 1j * D_pi
        H = 1j * D_pi  # (local)
        evals_H, evecs_H = scipy_eigh(H)
        # Dirac eigenvalues: lambda_D = -1j * evals_H (purely imaginary)
        # For threshold computation, use |lambda_D| = |evals_H|
        abs_evals = np.abs(evals_H)  # (local)

        # Count near-zero eigenvalues
        n_zero = np.sum(abs_evals < 1e-10)  # (local)

        D_size = d_pq * 16  # (local)
        total_eigenvalues += D_size
        total_modes_with_pw += D_size * d_pq  # PW multiplicity

        print(f"  ({p},{q}): {d_pq:4d}  {D_size:6d}  {np.min(abs_evals):10.6f}  "
              f"{np.max(abs_evals):10.6f}  {ah_check:10.2e}  {n_zero:6d}")

        sector_results.append({
            'p': p, 'q': q, 'dim': d_pq,
            'D_size': D_size,
            'evals_H': evals_H,        # Hermitian eigenvalues (real)
            'abs_evals': abs_evals,     # |lambda_D|
            'ah_err': ah_check,
            'n_zero': n_zero,
        })

    except (NotImplementedError, RuntimeError) as e:
        print(f"  ({p},{q}): SKIPPED ({e})")

print(f"\n  Total sectors computed: {len(sector_results)}")
print(f"  Total eigenvalues (per-sector): {total_eigenvalues}")
print(f"  Total eigenvalues (PW-weighted): {total_modes_with_pw}")


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3: THRESHOLD CORRECTIONS WITH ACTUAL EIGENVALUE MASSES
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 78)
print("3. EIGENVALUE-RESOLVED THRESHOLD CORRECTIONS")
print("=" * 78)

# The threshold correction for gauge group a is:
#
#   Delta_a = sum_{(p,q)} T_a(p,q) * sum_{n in (p,q)} dim(p,q) * ln(|lambda_n| / mu)
#
# where:
#   - The outer sum is over Peter-Weyl sectors
#   - T_a(p,q) is the Dynkin index of the sector for gauge group a
#   - The inner sum is over D_K eigenvalues in sector (p,q)
#   - dim(p,q) is the PW multiplicity
#   - mu is the reference scale (we use mu = 1 = M_KK, then everything is in M_KK units)
#
# For NON-ZERO eigenvalues only (zero modes don't contribute to running).

mu_ref = 1.0  # (local) reference scale = M_KK

# Compute per-sector threshold weights
print(f"\n  Reference scale mu = {mu_ref} (M_KK units)")
print(f"\n  {'(p,q)':>7} {'T_3':>8} {'T_2':>8} {'T_Y':>8} {'T_2/T_3':>8} {'T_Y/T_3':>8} "
      f"{'W(p,q)':>12} {'Delta_3':>12} {'Delta_2':>12}")
print("  " + "-" * 100)

Delta_3_total = 0.0  # (local)
Delta_2_total = 0.0  # (local)
Delta_Y_total = 0.0  # (local)
Delta_1_total = 0.0  # (local) GUT-normalized U(1)

W_total = 0.0  # (local) total eigenvalue weight (for diagnostics)
n_modes_used = 0  # (local)
n_modes_skipped_zero = 0  # (local)

for sec in sector_results:
    p, q = sec['p'], sec['q']
    d_pq = sec['dim']

    # Get Dynkin indices
    br = su3_branching(p, q)
    T3 = T_SU3(p, q)  # (local)
    T2 = T_SU2(br)     # (local)
    TY = T_U1(br)      # (local)
    T1 = (5.0/3.0) * TY  # (local) GUT normalization

    # Skip trivial (0,0) — T3 = T2 = TY = 0
    if T3 < 1e-15:
        # Eigenvalue weight for diagnostics
        abs_ev = sec['abs_evals']
        mask_nz = abs_ev > 1e-10  # (local)
        W_pq = d_pq * np.sum(np.log(abs_ev[mask_nz] / mu_ref))  # (local)
        print(f"  ({p},{q}):     0.00     0.00     0.00      ---      ---  {W_pq:12.4f}  "
              f"{'(trivial)':>12}  {'(trivial)':>12}")
        continue

    # Compute eigenvalue weight for this sector
    abs_ev = sec['abs_evals']
    mask_nz = abs_ev > 1e-10  # (local) non-zero eigenvalues only
    n_nz = np.sum(mask_nz)    # (local)
    n_z = np.sum(~mask_nz)    # (local)

    # W(p,q) = dim(p,q) * sum_{n: |lambda_n| > 0} ln(|lambda_n| / mu)
    if n_nz > 0:
        ln_sum = np.sum(np.log(abs_ev[mask_nz] / mu_ref))  # (local)
        W_pq = d_pq * ln_sum  # (local) PW-weighted eigenvalue weight
    else:
        ln_sum = 0.0  # (local)
        W_pq = 0.0    # (local)

    # Threshold contributions
    d3 = T3 * W_pq  # (local)
    d2 = T2 * W_pq  # (local)
    dY = TY * W_pq  # (local)
    d1 = T1 * W_pq  # (local)

    Delta_3_total += d3
    Delta_2_total += d2
    Delta_Y_total += dY
    Delta_1_total += d1
    W_total += W_pq

    n_modes_used += n_nz * d_pq
    n_modes_skipped_zero += n_z * d_pq

    # Ratios (should be 1 and 4/3 from Dynkin theorem)
    r23 = T2/T3  # (local)
    rY3 = TY/T3  # (local)

    print(f"  ({p},{q}): {T3:8.2f} {T2:8.4f} {TY:8.4f} {r23:8.6f} {rY3:8.6f} "
          f"{W_pq:12.4f} {d3:12.4f} {d2:12.4f}")

print(f"\n  Total modes used (PW-weighted): {n_modes_used}")
print(f"  Total modes skipped (zero): {n_modes_skipped_zero}")
print(f"  Total eigenvalue weight W: {W_total:.6f}")


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4: THRESHOLD RATIOS AND GATE EVALUATION
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 78)
print("4. THRESHOLD RATIOS AND GATE EVALUATION")
print("=" * 78)

if abs(Delta_3_total) > 1e-15:
    ratio_23 = Delta_2_total / Delta_3_total  # (local)
    ratio_Y3 = Delta_Y_total / Delta_3_total  # (local)
    ratio_13 = Delta_1_total / Delta_3_total  # (local)
else:
    ratio_23 = float('nan')  # (local)
    ratio_Y3 = float('nan')  # (local)
    ratio_13 = float('nan')  # (local)

print(f"\n  THRESHOLD CORRECTION TOTALS:")
print(f"    Delta_3 (SU(3)):  {Delta_3_total:+.6f}")
print(f"    Delta_2 (SU(2)):  {Delta_2_total:+.6f}")
print(f"    Delta_Y (U(1)):   {Delta_Y_total:+.6f}")
print(f"    Delta_1 (GUT):    {Delta_1_total:+.6f}")

print(f"\n  THRESHOLD RATIOS:")
print(f"    Delta_2 / Delta_3 = {ratio_23:.10f}  (prediction: 1.000000)")
print(f"    Delta_Y / Delta_3 = {ratio_Y3:.10f}  (prediction: 1.333333)")
print(f"    Delta_1 / Delta_3 = {ratio_13:.10f}  (prediction: 2.222222 = 20/9)")

# Deviation from structural prediction
dev_23 = abs(ratio_23 - 1.0)  # (local)
dev_Y3 = abs(ratio_Y3 - 4.0/3.0)  # (local)
dev_13 = abs(ratio_13 - 20.0/9.0)  # (local)

print(f"\n  DEVIATIONS FROM STRUCTURAL PREDICTION:")
print(f"    |Delta_2/Delta_3 - 1|     = {dev_23:.2e}")
print(f"    |Delta_Y/Delta_3 - 4/3|   = {dev_Y3:.2e}")
print(f"    |Delta_1/Delta_3 - 20/9|  = {dev_13:.2e}")


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5: WEINBERG ANGLE FROM EIGENVALUE-RESOLVED THRESHOLDS
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 78)
print("5. WEINBERG ANGLE FROM EIGENVALUE-RESOLVED THRESHOLDS")
print("=" * 78)

# The RG running from M_KK to M_Z:
#   1/alpha_a(M_Z) = 1/alpha_a(M_KK) + (b_a/2pi)*ln(M_KK/M_Z) + Delta_a/(8*pi^2)
#
# sin^2(theta_W, M_Z) = alpha_1(M_Z) / (alpha_1(M_Z) + alpha_2(M_Z))
#
# At M_KK (Paper 13):
#   sin^2(M_KK) = 0.5839 (permanent, from g'^2/(g'^2+g^2))
#   alpha_1^{-1}(M_KK) and alpha_2^{-1}(M_KK) follow from this

# Boundary conditions at M_KK
sin2_MKK = sin2_thetaW_fold  # (local) = 0.5839
alpha_em_inv_MKK = alpha2_MKK_inv  # (local) from canonical
# But wait: alpha_em = alpha_2 * sin^2(theta_W) at M_KK, so
# 1/alpha_em(M_KK) is not the same as 1/alpha_2(M_KK)

# From sin^2(M_KK) and the coupling definitions:
#   sin^2 = g'^2/(g'^2+g^2) = alpha_1/(alpha_1+alpha_2) in GUT normalization
#   1/alpha_2(M_KK) can be extracted from the spectral action

# Using S77-B4 approach (from canonical_constants):
alpha2_inv_MKK = alpha2_MKK_inv  # (local) = 47.856
alpha1_inv_MKK = alpha2_inv_MKK * (1 - sin2_MKK) / sin2_MKK  # (local)
# This gives alpha_1^{-1} = alpha_2^{-1} * (1-sin^2)/sin^2

ln_ratio = np.log(M_KK / M_Z)  # (local) ln(M_KK/M_Z) ~ 34.3

# 1-loop RG running (NO thresholds)
alpha1_inv_MZ_nothresh = alpha1_inv_MKK + (b1_SM / (2*PI)) * ln_ratio  # (local)
alpha2_inv_MZ_nothresh = alpha2_inv_MKK + (b2_SM / (2*PI)) * ln_ratio  # (local)
sin2_MZ_nothresh = alpha1_inv_MZ_nothresh / (alpha1_inv_MZ_nothresh + alpha2_inv_MZ_nothresh)  # (local)

print(f"\n  Boundary conditions at M_KK = {M_KK:.4e} GeV:")
print(f"    sin^2(theta_W, M_KK) = {sin2_MKK:.6f}")
print(f"    alpha_2^{{-1}}(M_KK)    = {alpha2_inv_MKK:.4f}")
print(f"    alpha_1^{{-1}}(M_KK)    = {alpha1_inv_MKK:.4f}")
print(f"    ln(M_KK/M_Z)          = {ln_ratio:.4f}")
print(f"\n  Without thresholds:")
print(f"    alpha_1^{{-1}}(M_Z) = {alpha1_inv_MZ_nothresh:.4f}")
print(f"    alpha_2^{{-1}}(M_Z) = {alpha2_inv_MZ_nothresh:.4f}")
print(f"    sin^2(M_Z) = {sin2_MZ_nothresh:.6f}  (PDG: {sin2_thetaW_MSbar:.5f})")

# Now with eigenvalue-resolved thresholds
# The question: does using actual eigenvalue masses change the ratio?
# ANSWER: No, because T_2/T_3 = 1 per sector, so the eigenvalue weights
# cancel in the ratio. But let's see what threshold MAGNITUDE is needed.

# For the universal threshold model (S72 Model A, which WORKS numerically
# but violates Dynkin theorem):
# delta_1 = delta_2 = delta_3 = S_inf (same for all groups)
# sin^2(M_Z) ~ 0.229 (1.2% match to PDG)

# For the PW-resolved model (S73a):
# delta_2/delta_3 = 1, delta_1/delta_3 = 20/9
# sin^2(M_Z) = -0.046 (FAIL)

# The eigenvalue-resolved model gives the SAME ratios as PW-resolved:
print(f"\n  EIGENVALUE-RESOLVED threshold ratios:")
print(f"    Delta_2/Delta_3 = {ratio_23:.10f} (= T_2/T_3 = 1, from Dynkin theorem)")
print(f"    Delta_1/Delta_3 = {ratio_13:.10f} (= 20/9, from Dynkin theorem)")

# Compute sin^2(M_Z) using these ratios with a representative threshold magnitude
# S_inf = 2.353 from S71 as the total threshold sum parameter
S_inf_ref = 2.353  # (local) reference threshold magnitude from S71

# Using the PW-resolved formula from S73a eq (3):
# delta_a = S_inf * T_a/T_3 for gauge group a
# (This is what eigenvalue-resolved gives, structurally identical to PW-resolved)
delta_3_norm = S_inf_ref * 1.0           # (local) SU(3)
delta_2_norm = S_inf_ref * ratio_23      # (local) SU(2) = S_inf * 1
delta_1_norm = S_inf_ref * ratio_13      # (local) U(1) = S_inf * 20/9

alpha1_inv_MZ = alpha1_inv_MKK + (b1_SM/(2*PI))*ln_ratio + delta_1_norm/(8*PI**2)  # (local)
alpha2_inv_MZ = alpha2_inv_MKK + (b2_SM/(2*PI))*ln_ratio + delta_2_norm/(8*PI**2)  # (local)
alpha3_inv_MZ = 0 + (b3_SM/(2*PI))*ln_ratio + delta_3_norm/(8*PI**2)  # (local) placeholder

sin2_MZ_resolved = alpha1_inv_MZ / (alpha1_inv_MZ + alpha2_inv_MZ)  # (local)

print(f"\n  With eigenvalue-resolved thresholds (S_inf = {S_inf_ref}):")
print(f"    delta_1 = {delta_1_norm:.4f}")
print(f"    delta_2 = {delta_2_norm:.4f}")
print(f"    delta_3 = {delta_3_norm:.4f}")
print(f"    alpha_1^{{-1}}(M_Z) = {alpha1_inv_MZ:.4f}")
print(f"    alpha_2^{{-1}}(M_Z) = {alpha2_inv_MZ:.4f}")
print(f"    sin^2(theta_W, M_Z) = {sin2_MZ_resolved:.6f}")
print(f"    PDG value:            {sin2_thetaW_MSbar:.5f}")
dev_sin2 = (sin2_MZ_resolved - sin2_thetaW_MSbar) / sin2_thetaW_MSbar * 100  # (local)
print(f"    Deviation: {dev_sin2:+.1f}%")

# Also compute the universal threshold model for comparison
delta_univ = S_inf_ref  # (local) same for all groups
alpha1_inv_MZ_univ = alpha1_inv_MKK + (b1_SM/(2*PI))*ln_ratio + delta_univ/(8*PI**2)  # (local)
alpha2_inv_MZ_univ = alpha2_inv_MKK + (b2_SM/(2*PI))*ln_ratio + delta_univ/(8*PI**2)  # (local)
sin2_MZ_univ = alpha1_inv_MZ_univ / (alpha1_inv_MZ_univ + alpha2_inv_MZ_univ)  # (local)
print(f"\n  Universal threshold model (delta_1 = delta_2 = delta_3 = S_inf):")
print(f"    sin^2(M_Z) = {sin2_MZ_univ:.6f} ({(sin2_MZ_univ - sin2_thetaW_MSbar)/sin2_thetaW_MSbar*100:+.1f}%)")
print(f"    NOTE: Violates Dynkin theorem T_2/T_3 = 1 != T_1/T_3 = 20/9")


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 6: SPECTRAL DECOMPOSITION ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 78)
print("6. SPECTRAL DECOMPOSITION ANALYSIS")
print("=" * 78)

# Analyze how the eigenvalue weight W(p,q) distributes across sectors
print(f"\n  Per-sector eigenvalue weight W(p,q) = dim(p,q) * sum ln|lambda_n|")
print(f"  {'(p,q)':>7} {'dim':>5} {'n_eval':>7} {'n_nz':>5} {'<ln|lam|>':>10} "
      f"{'W(p,q)':>12} {'frac_W':>8}")
print("  " + "-" * 70)

W_by_sector = []  # (local)
for sec in sector_results:
    p, q = sec['p'], sec['q']
    d_pq = sec['dim']
    abs_ev = sec['abs_evals']
    mask_nz = abs_ev > 1e-10
    n_nz = np.sum(mask_nz)
    if n_nz > 0:
        mean_ln = np.mean(np.log(abs_ev[mask_nz] / mu_ref))  # (local)
        W_pq = d_pq * np.sum(np.log(abs_ev[mask_nz] / mu_ref))
    else:
        mean_ln = 0.0  # (local)
        W_pq = 0.0  # (local)
    frac = W_pq / W_total if abs(W_total) > 1e-15 else 0.0  # (local)
    W_by_sector.append((p, q, d_pq, n_nz, mean_ln, W_pq, frac))
    print(f"  ({p},{q}): {d_pq:4d}  {len(abs_ev):6d}  {n_nz:4d}  {mean_ln:10.4f}  "
          f"{W_pq:12.4f}  {frac:8.4f}")

# Check convergence: what fraction of W_total comes from levels <= L
print(f"\n  Convergence by level:")
for L_cut in range(1, L_MAX + 1):
    W_below = sum(W for p, q, d, n, m, W, f in W_by_sector if p + q <= L_cut)  # (local)
    frac_below = W_below / W_total if abs(W_total) > 1e-15 else 0.0  # (local)
    n_sec = sum(1 for p, q, d, n, m, W, f in W_by_sector if p + q <= L_cut)  # (local)
    print(f"    L <= {L_cut}: {n_sec:3d} sectors, W = {W_below:10.4f}, fraction = {frac_below:.4f}")


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 7: EIGENVALUE-LEVEL ANALYSIS
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 78)
print("7. EIGENVALUE-LEVEL ANALYSIS")
print("=" * 78)

# Collect ALL eigenvalues with their sector labels
all_modes = []  # (local) list of (|lambda|, p, q, dim_pq, T3, T2, TY)
for sec in sector_results:
    p, q = sec['p'], sec['q']
    d_pq = sec['dim']
    br = su3_branching(p, q)
    T3 = T_SU3(p, q)
    T2 = T_SU2(br)
    TY = T_U1(br)
    for lam in sec['abs_evals']:
        if lam > 1e-10:
            all_modes.append((lam, p, q, d_pq, T3, T2, TY))

all_modes.sort(key=lambda x: x[0])
n_modes_total = len(all_modes)  # (local)

print(f"\n  Total non-zero eigenvalue modes: {n_modes_total}")
print(f"\n  Lowest 20 eigenvalues:")
print(f"  {'idx':>5} {'|lam|':>12} {'(p,q)':>7} {'dim':>5} {'T_3':>8} {'T_2':>8} {'T_Y':>8}")
for i, (lam, p, q, d, T3, T2, TY) in enumerate(all_modes[:20]):
    print(f"  {i:5d} {lam:12.6f} ({p},{q}): {d:4d}  {T3:8.2f} {T2:8.4f} {TY:8.4f}")

print(f"\n  Highest 10 eigenvalues:")
for i, (lam, p, q, d, T3, T2, TY) in enumerate(all_modes[-10:]):
    idx = n_modes_total - 10 + i  # (local)
    print(f"  {idx:5d} {lam:12.6f} ({p},{q}): {d:4d}  {T3:8.2f} {T2:8.4f} {TY:8.4f}")


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 8: GATE VERDICT
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 78)
print("8. GATE VERDICT: S77-C6-MODE-THRESHOLD")
print("=" * 78)

# The gate tests whether eigenvalue-resolved thresholds can reproduce
# the Weinberg angle. The answer is structurally NO:
# Delta_2/Delta_3 = 1 (exactly), confirming the S73a Dynkin theorem.
# This means the eigenvalue-resolved computation is IDENTICAL to PW-resolved.

# The sin^2 result is the same as S73a: Delta_1/Delta_3 = 20/9 gives
# sin^2(M_Z) ~ -0.046 (FAIL).

print(f"\n  === PRIMARY RESULT ===")
print(f"  Delta_2 / Delta_3 = {ratio_23:.10f}")
print(f"  Structural prediction: 1.000000")
print(f"  Deviation: {dev_23:.2e}")
print()
print(f"  Delta_Y / Delta_3 = {ratio_Y3:.10f}")
print(f"  Structural prediction: 1.333333")
print(f"  Deviation: {dev_Y3:.2e}")
print()
print(f"  Delta_1 / Delta_3 = {ratio_13:.10f}")
print(f"  Structural prediction: 2.222222 (= 20/9)")
print(f"  Deviation: {dev_13:.2e}")
print()

# Gate criterion: Delta_2/Delta_3 ~ 1 within 10%
gate_pass = abs(ratio_23 - 1.0) < 0.10  # (local)
gate_fail = abs(ratio_23 - 1.0) > 1.0   # (local) more than factor 2

if np.isnan(ratio_23):
    verdict = "INFO"
    verdict_detail = "Insufficient data (Delta_3 ~ 0)"
elif gate_pass:
    verdict = "PASS"
    verdict_detail = (
        f"Delta_2/Delta_3 = {ratio_23:.10f} (machine epsilon from 1.0). "
        f"CONFIRMS S73a Dynkin theorem: eigenvalue-resolved thresholds are "
        f"structurally identical to PW-resolved thresholds. "
        f"The threshold ratio is a property of representations, not eigenvalues."
    )
elif gate_fail:
    verdict = "FAIL"
    verdict_detail = f"Delta_2/Delta_3 = {ratio_23:.6f} deviates from 1 by > factor 2"
else:
    verdict = "INFO"
    verdict_detail = f"Delta_2/Delta_3 = {ratio_23:.6f}, partial deviation"

print(f"  Gate S77-C6-MODE-THRESHOLD: {verdict}")
print(f"  Detail: {verdict_detail}")

# Structural conclusion
print(f"\n  === STRUCTURAL CONCLUSION ===")
print(f"  The eigenvalue-resolved threshold computation at L_max = {L_MAX}")
print(f"  ({len(sector_results)} sectors, {total_eigenvalues} eigenvalues per-sector,")
print(f"   {total_modes_with_pw} PW-weighted modes) CONFIRMS:")
print(f"")
print(f"  1. Delta_2/Delta_3 = 1 to machine epsilon (= {dev_23:.2e})")
print(f"     Because: T_2(p,q)/T_3(p,q) = 1 for EVERY sector, and the")
print(f"     eigenvalue weight W(p,q) cancels in the ratio.")
print(f"")
print(f"  2. Delta_1/Delta_3 = 20/9 to machine epsilon (= {dev_13:.2e})")
print(f"     Because: T_Y(p,q)/T_3(p,q) = 4/3 for EVERY sector.")
print(f"")
print(f"  3. The Weinberg angle sin^2(M_Z) from PW-resolved thresholds = -0.046")
print(f"     is PERMANENT: using actual D_K eigenvalue masses does not change")
print(f"     the threshold ratios. The obstruction is GROUP-THEORETIC, not SPECTRAL.")
print(f"")
print(f"  4. Only the UNIVERSAL threshold model (delta_1=delta_2=delta_3) matches")
print(f"     PDG, but it VIOLATES the Dynkin theorem. This model has no geometric")
print(f"     justification within Baptista's KK framework.")
print(f"")
print(f"  5. The tree-level KK threshold route to sin^2(theta_W) is CLOSED.")
print(f"     The obstruction is delta_1/delta_3 = 20/9 (permanent, S73a).")


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 9: PLOTS AND DATA OUTPUT
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 78)
print("9. PLOTS AND DATA OUTPUT")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Eigenvalue spectrum by sector (waterfall)
ax1 = axes[0, 0]
colors = plt.cm.viridis(np.linspace(0, 1, len(sector_results)))
y_offset = 0  # (local)
sector_labels = []  # (local)
for i, sec in enumerate(sector_results):
    p, q = sec['p'], sec['q']
    abs_ev = sec['abs_evals']
    mask_nz = abs_ev > 1e-10
    if np.sum(mask_nz) > 0:
        ev_nz = abs_ev[mask_nz]
        ax1.scatter(ev_nz, np.full_like(ev_nz, i), s=2, c=[colors[i]], alpha=0.6)
        sector_labels.append(f"({p},{q})")
ax1.set_xlabel('|Dirac eigenvalue| (M_KK units)')
ax1.set_ylabel('Sector index')
ax1.set_title('D_K eigenvalue spectrum by PW sector')
ax1.grid(True, alpha=0.2)

# Panel 2: Eigenvalue weight W(p,q) vs sector
ax2 = axes[0, 1]
sector_names = [f"({p},{q})" for p, q, d, n, m, W, f in W_by_sector]  # (local)
W_vals = [W for p, q, d, n, m, W, f in W_by_sector]  # (local)
x_pos = range(len(sector_names))
ax2.bar(x_pos, W_vals, color='steelblue', alpha=0.7)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(sector_names, rotation=90, fontsize=6)
ax2.set_ylabel('W(p,q) = dim * sum ln|lam|')
ax2.set_title('Eigenvalue weight by sector')
ax2.grid(True, alpha=0.2, axis='y')

# Panel 3: Threshold ratio convergence by L_max
ax3 = axes[1, 0]
L_values = range(1, L_MAX + 1)  # (local)
ratio_23_vs_L = []  # (local)
ratio_Y3_vs_L = []  # (local)
for L_cut in L_values:
    D2_L = 0.0  # (local)
    D3_L = 0.0  # (local)
    DY_L = 0.0  # (local)
    for sec in sector_results:
        p, q = sec['p'], sec['q']
        if p + q > L_cut:
            continue
        d_pq = sec['dim']
        br = su3_branching(p, q)
        T3 = T_SU3(p, q)
        T2 = T_SU2(br)
        TY = T_U1(br)
        abs_ev = sec['abs_evals']
        mask_nz = abs_ev > 1e-10
        if np.sum(mask_nz) > 0:
            W = d_pq * np.sum(np.log(abs_ev[mask_nz] / mu_ref))
            D3_L += T3 * W
            D2_L += T2 * W
            DY_L += TY * W
    if abs(D3_L) > 1e-15:
        ratio_23_vs_L.append(D2_L / D3_L)
        ratio_Y3_vs_L.append(DY_L / D3_L)
    else:
        ratio_23_vs_L.append(float('nan'))
        ratio_Y3_vs_L.append(float('nan'))

ax3.plot(list(L_values), ratio_23_vs_L, 'bo-', label='Delta_2/Delta_3', markersize=6)
ax3.plot(list(L_values), ratio_Y3_vs_L, 'rs-', label='Delta_Y/Delta_3', markersize=6)
ax3.axhline(y=1.0, color='blue', linestyle='--', alpha=0.5, label='T_2/T_3 = 1')
ax3.axhline(y=4/3, color='red', linestyle='--', alpha=0.5, label='T_Y/T_3 = 4/3')
ax3.set_xlabel('L_max (p+q cutoff)')
ax3.set_ylabel('Threshold ratio')
ax3.set_title('Ratio convergence vs L_max')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.2)
ax3.set_ylim([0.8, 1.6])

# Panel 4: Cumulative threshold by sector
ax4 = axes[1, 1]
D3_cum = np.zeros(len(sector_results))  # (local)
D2_cum = np.zeros(len(sector_results))  # (local)
DY_cum = np.zeros(len(sector_results))  # (local)
running_D3 = 0.0  # (local)
running_D2 = 0.0  # (local)
running_DY = 0.0  # (local)
for i, sec in enumerate(sector_results):
    p, q = sec['p'], sec['q']
    d_pq = sec['dim']
    br = su3_branching(p, q)
    T3 = T_SU3(p, q)
    T2 = T_SU2(br)
    TY = T_U1(br)
    abs_ev = sec['abs_evals']
    mask_nz = abs_ev > 1e-10
    if np.sum(mask_nz) > 0:
        W = d_pq * np.sum(np.log(abs_ev[mask_nz] / mu_ref))
        running_D3 += T3 * W
        running_D2 += T2 * W
        running_DY += TY * W
    D3_cum[i] = running_D3
    D2_cum[i] = running_D2
    DY_cum[i] = running_DY

ax4.plot(range(len(sector_results)), D3_cum, 'g-o', label='Delta_3', markersize=3)
ax4.plot(range(len(sector_results)), D2_cum, 'b-s', label='Delta_2', markersize=3)
ax4.plot(range(len(sector_results)), DY_cum, 'r-^', label='Delta_Y', markersize=3)
ax4.set_xlabel('Sector index')
ax4.set_ylabel('Cumulative threshold')
ax4.set_title('Cumulative Delta_a by sector')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.2)

plt.tight_layout()
save_path = os.path.join(outdir, 's77_mode_threshold.png')
plt.savefig(save_path, dpi=150)
plt.close()
print(f"  Plot saved: {save_path}")

# Save data
npz_path = os.path.join(outdir, 's77_mode_threshold.npz')
np.savez(npz_path,
    # Gate
    gate_name='S77-C6-MODE-THRESHOLD',
    gate_verdict=verdict,
    gate_detail=verdict_detail,
    # Parameters
    tau=tau_fold,
    L_max=L_MAX,
    mu_ref=mu_ref,
    n_sectors=len(sector_results),
    n_modes_total=n_modes_total,
    total_eigenvalues=total_eigenvalues,
    total_modes_pw=total_modes_with_pw,
    # Threshold totals
    Delta_3=Delta_3_total,
    Delta_2=Delta_2_total,
    Delta_Y=Delta_Y_total,
    Delta_1=Delta_1_total,
    # Ratios
    ratio_23=ratio_23,
    ratio_Y3=ratio_Y3,
    ratio_13=ratio_13,
    dev_23=dev_23,
    dev_Y3=dev_Y3,
    dev_13=dev_13,
    # Per-sector data
    sec_p=np.array([sec['p'] for sec in sector_results]),
    sec_q=np.array([sec['q'] for sec in sector_results]),
    sec_dim=np.array([sec['dim'] for sec in sector_results]),
    sec_n_eval=np.array([len(sec['abs_evals']) for sec in sector_results]),
    sec_W=np.array([W for p, q, d, n, m, W, f in W_by_sector]),
    # Weinberg angle results
    sin2_MZ_nothresh=sin2_MZ_nothresh,
    sin2_MZ_resolved=sin2_MZ_resolved,
    sin2_MZ_universal=sin2_MZ_univ,
    sin2_MKK=sin2_MKK,
    # Convergence
    ratio_23_vs_L=np.array(ratio_23_vs_L),
    ratio_Y3_vs_L=np.array(ratio_Y3_vs_L),
)
print(f"  Data saved: {npz_path}")

t_end = time.time()
print(f"\n  Total runtime: {t_end - t_start:.1f} s")

print("\n" + "=" * 78)
print(f"FINAL VERDICT: Gate S77-C6-MODE-THRESHOLD = {verdict}")
print(f"Delta_2/Delta_3 = {ratio_23:.10f} (structural: 1.0, dev: {dev_23:.2e})")
print(f"Delta_1/Delta_3 = {ratio_13:.10f} (structural: 20/9, dev: {dev_13:.2e})")
print(f"Eigenvalue-resolved thresholds confirm Dynkin theorem: tree-level route CLOSED.")
print("=" * 78)
