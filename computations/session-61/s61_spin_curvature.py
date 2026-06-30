#!/usr/bin/env python3
"""
S61 SPIN-CURV-61: Spin Connection Curvature Term in Gilkey a_2
===============================================================

Determines whether (1/12)*tr(Omega^2) in the Gilkey a_2 formula is
negligible compared to (R/6)*tr(id) on Jensen-deformed SU(3).

Mathematical Framework
----------------------

The Gilkey a_2 coefficient for the operator P = D^2 on a spin bundle
(where D is the Dirac operator) has the standard form:

    a_2(x, P) = (4*pi)^{-d/2} * tr_S[ (R/6)*Id_S + E ]        (*)

where:
    d = 8 (dim SU(3))
    Id_S = 16x16 identity (spinor bundle on 8-manifold, rank 2^4 = 16)
    E = endomorphism term from D^2 = -( nabla^2 + E )  # (local)
    R = scalar curvature

For the Dirac operator on a spin manifold (Lichnerowicz formula):

    D^2 = nabla^* nabla + (R/4)*Id_S

So E = -R/4 * Id_S (the Lichnerowicz endomorphism). But the FULL
Gilkey a_2 for a general Laplace-type operator is:

    a_2 = (4*pi)^{-d/2} * integral tr_S( R/6 * Id - E + (1/6)*Omega_{ij}Omega^{ij} ) dvol

Wait -- let me be precise. Gilkey's formula (see Gilkey, "Invariance Theory",
Theorem 4.1.6) for the heat kernel coefficient a_2 of a Laplace-type operator
P = -(g^{ij} nabla_i nabla_j + E) acting on sections of a vector bundle V:

    a_2(P) = (4*pi)^{-d/2} * integral_M tr_V[ (R/6)*Id_V - E + (1/6)*Omega_{ij}Omega^{ij} ] dvol

where Omega_{ij} is the curvature of the connection on V, and the 1/6 is
Gilkey's convention (some authors write 1/12 with a factor of 2 absorbed).

For D^2 with Lichnerowicz: E = -R/4 * Id_S, so:
    R/6 * Id - E = R/6 * Id + R/4 * Id = (5R/12) * Id

The spin connection curvature on spinors is:
    Omega_{ab} = (1/4) R_{abcd} gamma^c gamma^d

And the trace:
    tr_S(Omega_{ab} Omega^{ab}) = (1/16) R_{abcd} R_{abef} tr_S(gamma^c gamma^d gamma^e gamma^f)

Using:
    tr(gamma^c gamma^d gamma^e gamma^f) = 2^{d/2} * (delta^{cd}delta^{ef} - delta^{ce}delta^{df} + delta^{cf}delta^{de})

for d=8: 2^4 = 16, so:
    tr_S(gamma^c gamma^d gamma^e gamma^f) = 16*(delta_{cd}delta_{ef} - delta_{ce}delta_{df} + delta_{cf}delta_{de})

Therefore:
    tr_S(Omega_{ab}Omega^{ab}) = (1/16)*R_{abcd}*R_{abef}*16*(delta_{cd}delta_{ef} - delta_{ce}delta_{df} + delta_{cf}delta_{de})
                                = R_{abcd}*R_{abef}*(delta_{cd}delta_{ef} - delta_{ce}delta_{df} + delta_{cf}delta_{de})
                                = R_{abcc}*R_{abee} - R_{abcd}*R_{abcd} + R_{abcd}*R_{abdc}

Note: R_{abcc} = 0 (by antisymmetry R_{abcc} = -R_{abcc} = 0).
And R_{abdc} = -R_{abcd} (antisymmetry in last pair).

So: tr_S(Omega_{ab}Omega^{ab}) = 0 - |Riem|^2 - |Riem|^2 = -2*|Riem|^2

where |Riem|^2 = R_{abcd}*R^{abcd} is the Kretschner scalar.

WAIT -- let me re-derive more carefully.

Omega_{ab} = (1/4) R_{abcd} gamma^c gamma^d.

Sum over ON frame a,b:
    sum_{a<b} Omega_{ab} Omega^{ab}  -- but we need the full contraction.

Actually, the curvature 2-form Omega = (1/2) Omega_{ab} e^a wedge e^b,
so the trace we need is:

    tr(Omega_{ij} Omega^{ij}) = sum_{i,j} tr_S(Omega_{ij} Omega_{ij})

where Omega_{ij} = (1/4) R_{ijkl} gamma^k gamma^l.

    = sum_{i,j} (1/16) R_{ijkl} R_{ijmn} tr_S(gamma^k gamma^l gamma^m gamma^n)

    = (1/16) R_{ijkl} R_{ijmn} * 16 * (delta_{kl}delta_{mn} - delta_{km}delta_{ln} + delta_{kn}delta_{lm})

    = R_{ijkl} R_{ijmn} (delta_{kl}delta_{mn} - delta_{km}delta_{ln} + delta_{kn}delta_{lm})

Term 1: R_{ijkk} R_{ijmm} = 0  (antisymmetry in last pair)
Term 2: -R_{ijkl} R_{ijkl} = -|Riem|^2
Term 3: R_{ijkl} R_{ijlk} = -R_{ijkl} R_{ijkl} = -|Riem|^2

So: tr_S(Omega_{ij} Omega^{ij}) = -2 * |Riem|^2

Thus the spin connection curvature term in a_2 is:

    (1/6) * tr_S(Omega_{ij} Omega^{ij}) = -(1/3) * |Riem|^2

And the scalar curvature + endomorphism term is:

    tr_S( (R/6)*Id - E ) = (5R/12) * 16 = (20R/3)

So the integrand of a_2 (before (4*pi)^{-d/2} and volume) is:

    (20R/3) - (1/3)*|Riem|^2

The RATIO we want is:

    ratio = (1/3)*|Riem|^2 / (20R/3) = |Riem|^2 / (20R)

Gate: SPIN-CURV-61
    Let spin_term = (1/3)*|Riem|^2
    Let scalar_term = 20R/3
    ratio = spin_term / scalar_term = |Riem|^2 / (20R)

    PASS if ratio < 0.1
    INFO if 0.1 <= ratio <= 1.0
    FAIL if ratio > 1.0

Cross-checks:
    - |Riem|^2 = Kretschner scalar (exact formula from SP-2)
    - R = scalar curvature (exact formula from SP-2)
    - Numerical Riemann tensor contraction vs exact Kretschner

Output:
    - s61_spin_curvature.npz
    - s61_spin_curvature.png (ratio vs tau)

Author: Spectral Geometer (Session 61)
Date: 2026-03-28
"""

import numpy as np
import sys
import os
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
#  Path setup
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from canonical_constants import tau_fold, PI

ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')
sys.path.insert(0, ARCHIVE_DIR)

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    validate_connection,
)
from r20a_riemann_tensor import (
    compute_riemann_tensor_ON_fast,
    scalar_curvature_our_metric,
    kretschner_exact,
)


# =============================================================================
# COMPUTATION
# =============================================================================

def compute_spin_curvature_ratio(s):
    """
    Compute the ratio of spin-connection curvature term to scalar curvature
    term in the Gilkey a_2 coefficient, at Jensen parameter s.

    Returns dict with all intermediate quantities.
    """
    # Exact analytic values (from SP-2, verified to machine epsilon)
    R_exact = scalar_curvature_our_metric(s)
    K_exact = kretschner_exact(s)

    # Numerical Riemann tensor for cross-check
    R_abcd = compute_riemann_tensor_ON_fast(s)

    # Numerical Kretschner
    K_numerical = np.einsum('abcd,abcd->', R_abcd, R_abcd)

    # Numerical Ricci tensor and scalar curvature
    # R_{ab} = R^c_{acb} = sum_c R_{acbc} ... wait, need to be careful with index convention.
    # R_abcd[a,b,c,d] = R_{abcd}. Ricci: Ric_{bd} = g^{ac} R_{abcd} = sum_a R_{abad}
    # In ON frame g^{ac} = delta^{ac}, so Ric_{bd} = sum_a R_{abad}
    Ric_ab = np.einsum('abac->bc', R_abcd)
    R_numerical = np.trace(Ric_ab)  # scalar curvature = g^{ab} Ric_{ab} = sum_a Ric_{aa}

    # Validate: cross-check numerical vs exact
    K_err = abs(K_numerical - K_exact) / abs(K_exact)
    R_err = abs(R_numerical - R_exact) / abs(R_exact)

    # The spin connection curvature on spinors:
    #   Omega_{ab} = (1/4) R_{abcd} gamma^c gamma^d
    #   tr_S(Omega_{ab} Omega^{ab}) = -2 * |Riem|^2
    # (derived in docstring above, using tr(gamma^c gamma^d gamma^e gamma^f) identity)

    tr_Omega_sq = -2.0 * K_exact  # = tr_S(sum_{a,b} Omega_{ab} Omega_{ab})

    # Gilkey a_2 integrand (before (4*pi)^{-d/2} * Vol):
    # Full:   tr_S(R/6 * Id - E) + (1/6) * tr_S(Omega Omega)
    # where E = -R/4 * Id (Lichnerowicz) and Id is 16x16
    # Scalar + endomorphism part: (R/6 + R/4) * 16 = (5R/12) * 16 = 20R/3
    # Spin connection part: (1/6) * tr_S(Omega Omega) = (1/6) * (-2 * K) = -K/3

    scalar_term = 20.0 * R_exact / 3.0      # = (5R/12) * 16
    spin_term = -K_exact / 3.0               # = (1/6) * (-2K)

    # The full a_2 integrand = scalar_term + spin_term = 20R/3 - K/3

    # RATIO: |spin_term| / |scalar_term|
    ratio = abs(spin_term) / abs(scalar_term) if abs(scalar_term) > 1e-15 else float('inf')
    # Equivalently: K / (20R) for positive R

    return {
        's': s,
        'R_exact': R_exact,
        'K_exact': K_exact,
        'R_numerical': R_numerical,
        'K_numerical': K_numerical,
        'R_err': R_err,
        'K_err': K_err,
        'Ric_ab': Ric_ab,
        'tr_Omega_sq': tr_Omega_sq,
        'scalar_term': scalar_term,
        'spin_term': spin_term,
        'a2_integrand_full': scalar_term + spin_term,
        'ratio': ratio,
    }


def compute_spin_connection_explicit(s):
    """
    Compute the spin connection and its curvature EXPLICITLY as matrices
    acting on spinors, for independent cross-check.

    The spin connection 1-form is:
        omega_a = (1/4) * Gamma_{bca} * gamma^b gamma^c

    Wait -- more carefully. The spin connection is:
        omega_a = (1/2) * omega_{a,bc} * Sigma^{bc}
    where Sigma^{bc} = (1/4)[gamma^b, gamma^c] = (1/2) gamma^b gamma^c for b != c.
    And omega_{a,bc} = Gamma^b_{ac} (the connection coefficients from Levi-Civita).

    Actually, the standard relation is:
        omega_a = (1/4) * omega_{abc} * gamma^b gamma^c
    where omega_{abc} = Gamma_{bac} (connection coefficients, antisymmetric in bc
    due to metric compatibility).

    For our convention: Gamma[c,a,b] = Gamma^c_{ab}, and metric compatibility
    gives Gamma^c_{ab} = -Gamma^b_{ac}, i.e., Gamma[c,a,b] = -Gamma[b,a,c].

    The spin connection acting on spinor Psi is:
        nabla_a Psi = e_a(Psi) + omega_a Psi
    where omega_a = (1/4) Gamma_{bca} gamma^b gamma^c
    Note: Gamma_{bca} = Gamma^b_{ca} in ON frame (lower b = raise b trivially).

    Hmm, let me use the cleaner formulation. The spin connection 1-form is:
        omega_a^{(spin)} = (1/4) sum_{b<c} omega_{a,bc} gamma^b gamma^c
    where omega_{a,bc} = <nabla_{e_a} e_b, e_c> = Gamma^c_{ab} ... no, that's wrong too.

    OK, let me be very precise. In an ON frame {e_a}:
        nabla_{e_a} e_b = Gamma^c_{ab} e_c
    The spin connection lifts this to the spinor bundle:
        omega_a^{spin} = (1/4) Gamma^c_{ab} (for each pair b,c, antisym in b,c)
            ... wait, need to sum over b.

    Actually: the connection 1-form (matrix-valued) is:
        (omega_a)^b_c = Gamma^b_{ac}

    And the spin lift is:
        omega_a^{spin} = (1/4) sum_{b,c} (omega_a)_{bc} gamma^b gamma^c
                       = (1/4) sum_{b,c} Gamma_{bac} gamma^b gamma^c

    where Gamma_{bac} = Gamma^b_{ac} in ON frame. Due to antisymmetry
    Gamma^b_{ac} = -Gamma^c_{ab}... no.

    Metric compatibility: Gamma^c_{ab} + Gamma^b_{ac} = 0.
    So (omega_a)_{bc} = Gamma^b_{ac} is antisymmetric in (b,c): yes, because
    Gamma^b_{ac} = -(Gamma^c_{ab}) ... wait, that's not right either.

    Metric compatibility says: Gamma_{cab} + Gamma_{bac} = 0 where Gamma_{cab} = Gamma^c_{ab}.
    Wait no: from the code above, metric compatibility is Gamma^c_{ab} + Gamma^b_{ac} = 0,
    i.e., Gamma[c,a,b] + Gamma[b,a,c] = 0. So Gamma[b,a,c] = -Gamma[c,a,b].

    The connection 1-form matrix: (omega_a)_b^c = Gamma^c_{ab} = Gamma[c,a,b].
    Lower: (omega_a)_{bc} = delta_{bd} Gamma^d_{ac} = Gamma^b_{ac} = Gamma[b,a,c].
    Antisymmetry: (omega_a)_{bc} = Gamma[b,a,c] = -Gamma[c,a,b] = -(omega_a)_{cb}. Good.

    Spin connection: omega_a^{spin} = (1/4) sum_{b,c} (omega_a)_{bc} gamma^b gamma^c
                   = (1/4) sum_{b,c} Gamma[b,a,c] gamma^b gamma^c

    The curvature of the spin connection:
        Omega_{ab}^{spin} = [nabla_a^{spin}, nabla_b^{spin}] - nabla_{[e_a,e_b]}^{spin}

    On a Lie group with left-invariant frame, e_a(f) = 0 for left-invariant f.
    So nabla_a^{spin} acting on a left-invariant spinor section is just omega_a^{spin}.
    And [e_a, e_b] = ft^c_{ab} e_c, so nabla_{[e_a,e_b]} = ft^c_{ab} omega_c^{spin}.

    Therefore:
        Omega_{ab}^{spin} = omega_a omega_b - omega_b omega_a - ft^c_{ab} omega_c
                          = [omega_a, omega_b] - ft^c_{ab} omega_c

    where I dropped the 'spin' superscript.

    This should equal (1/4) R_{abcd} gamma^c gamma^d by the general relation.
    Let's verify this numerically!

    Returns curvature Omega_{ab} as 8x8 array of 16x16 matrices, and the trace.
    """
    # Build geometric infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E_frame = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E_frame)
    Gamma = connection_coefficients(ft)

    n = 8       # dimension
    ns = 16     # spinor rank = 2^4 for d=8

    # Build gamma matrices for Cliff(8) using standard recursive construction
    # Cliff(2n): use n pairs of creation/annihilation operators
    # gamma_{2k} = sigma_z^{otimes k} otimes sigma_x otimes I^{otimes (n-k-1)}
    # gamma_{2k+1} = sigma_z^{otimes k} otimes sigma_y otimes I^{otimes (n-k-1)}
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    def kron_list(mats):
        result = mats[0]
        for m in mats[1:]:
            result = np.kron(result, m)
        return result

    gammas = []
    for k in range(4):  # 4 pairs for d=8
        # gamma_{2k}
        parts_x = [sigma_z]*k + [sigma_x] + [I2]*(3-k)
        gammas.append(kron_list(parts_x))
        # gamma_{2k+1}
        parts_y = [sigma_z]*k + [sigma_y] + [I2]*(3-k)
        gammas.append(kron_list(parts_y))

    # Verify: {gamma_a, gamma_b} = 2 delta_{ab}
    cliff_err = 0.0  # (local)
    for a in range(n):
        for b in range(n):
            anticomm = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
            expected = 2.0 * (1 if a == b else 0) * np.eye(ns, dtype=complex)
            cliff_err = max(cliff_err, np.max(np.abs(anticomm - expected)))

    # Build spin connection matrices omega_a = (1/4) sum_{b,c} Gamma[b,a,c] gamma^b gamma^c
    omega_spin = np.zeros((n, ns, ns), dtype=complex)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                omega_spin[a] += 0.25 * Gamma[b, a, c] * (gammas[b] @ gammas[c])

    # Build spin curvature: Omega_{ab} = [omega_a, omega_b] - ft^c_{ab} omega_c
    Omega_spin = np.zeros((n, n, ns, ns), dtype=complex)
    for a in range(n):
        for b in range(n):
            comm = omega_spin[a] @ omega_spin[b] - omega_spin[b] @ omega_spin[a]
            struct_term = np.zeros((ns, ns), dtype=complex)
            for c in range(n):
                struct_term += ft[a, b, c] * omega_spin[c]
            Omega_spin[a, b] = comm - struct_term

    # Expected curvature from Riemann tensor:
    # Omega_{ab}^{expected} = (1/4) R_{abcd} gamma^c gamma^d
    R_abcd = compute_riemann_tensor_ON_fast(s)
    Omega_expected = np.zeros((n, n, ns, ns), dtype=complex)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    Omega_expected[a, b] += 0.25 * R_abcd[a, b, c, d] * (gammas[c] @ gammas[d])

    # Cross-check: Omega_spin vs Omega_expected
    curv_err = np.max(np.abs(Omega_spin - Omega_expected))

    # Compute tr_S(Omega_{ab} Omega^{ab}) = sum_{a,b} tr(Omega_{ab} Omega_{ab})
    tr_Omega_sq_explicit = 0.0  # (local)
    for a in range(n):
        for b in range(n):
            tr_Omega_sq_explicit += np.trace(Omega_spin[a, b] @ Omega_spin[a, b]).real

    return {
        'cliff_err': cliff_err,
        'curv_err': curv_err,
        'tr_Omega_sq_explicit': tr_Omega_sq_explicit,
        'Omega_spin_sample': Omega_spin[0, 1],  # a sample for inspection
        'omega_spin_sample': omega_spin[0],
    }


def main():
    t0 = time.time()

    print("=" * 72)
    print("S61 SPIN-CURV-61: Spin Connection Curvature in Gilkey a_2")
    print("=" * 72)

    # =========================================================================
    # PART 1: Compute at tau_fold = 0.19
    # =========================================================================
    print(f"\n--- tau_fold = {tau_fold} ---")
    result = compute_spin_curvature_ratio(tau_fold)

    print(f"  R(tau_fold) = {result['R_exact']:.10f}")
    print(f"  K(tau_fold) = |Riem|^2 = {result['K_exact']:.10f}")
    print(f"  R numerical = {result['R_numerical']:.10f}  (err = {result['R_err']:.2e})")
    print(f"  K numerical = {result['K_numerical']:.10f}  (err = {result['K_err']:.2e})")
    print(f"  tr_S(Omega Omega) = {result['tr_Omega_sq']:.10f}")
    print(f"  Scalar term: (5R/12)*16 = 20R/3 = {result['scalar_term']:.10f}")
    print(f"  Spin term: (1/6)*tr(OmOm) = -K/3 = {result['spin_term']:.10f}")
    print(f"  Full a_2 integrand = {result['a2_integrand_full']:.10f}")
    print(f"  RATIO |spin/scalar| = {result['ratio']:.6f}")

    # =========================================================================
    # PART 2: Explicit spin connection cross-check at tau_fold
    # =========================================================================
    print(f"\n--- Explicit spin connection cross-check ---")
    explicit = compute_spin_connection_explicit(tau_fold)
    print(f"  Clifford algebra error: {explicit['cliff_err']:.2e}")
    print(f"  Spin curvature vs Riemann: {explicit['curv_err']:.2e}")
    print(f"  tr_S(Omega^2) explicit:   {explicit['tr_Omega_sq_explicit']:.10f}")
    print(f"  tr_S(Omega^2) from K:     {result['tr_Omega_sq']:.10f}")
    tr_err = abs(explicit['tr_Omega_sq_explicit'] - result['tr_Omega_sq'])
    print(f"  Agreement: {tr_err:.2e}")

    # =========================================================================
    # PART 3: Sweep over tau in [0, 0.5]
    # =========================================================================
    print(f"\n--- Sweep over tau ---")
    tau_vals = np.linspace(0.0, 0.50, 51)
    R_vals = np.zeros(len(tau_vals))
    K_vals = np.zeros(len(tau_vals))
    ratio_vals = np.zeros(len(tau_vals))
    scalar_term_vals = np.zeros(len(tau_vals))
    spin_term_vals = np.zeros(len(tau_vals))
    a2_full_vals = np.zeros(len(tau_vals))

    for i, tau in enumerate(tau_vals):
        res = compute_spin_curvature_ratio(tau)
        R_vals[i] = res['R_exact']
        K_vals[i] = res['K_exact']
        ratio_vals[i] = res['ratio']
        scalar_term_vals[i] = res['scalar_term']
        spin_term_vals[i] = res['spin_term']
        a2_full_vals[i] = res['a2_integrand_full']

    # Print table
    print(f"  {'tau':>6s}  {'R':>10s}  {'|Riem|^2':>10s}  {'ratio':>10s}  {'a2_full':>12s}")
    for i in range(0, len(tau_vals), 5):
        print(f"  {tau_vals[i]:6.3f}  {R_vals[i]:10.6f}  {K_vals[i]:10.6f}  {ratio_vals[i]:10.6f}  {a2_full_vals[i]:12.6f}")

    # =========================================================================
    # PART 4: Bi-invariant cross-check (tau=0)
    # =========================================================================
    print(f"\n--- Bi-invariant cross-check (tau=0) ---")
    res0 = compute_spin_curvature_ratio(0.0)
    # At tau=0 (Einstein manifold): R = 2.0, K = 1/2
    # (Kretschner for compact simple Lie group with bi-invariant metric)
    print(f"  R(0) = {res0['R_exact']:.10f}  (expect 2.0)")
    print(f"  K(0) = {res0['K_exact']:.10f}  (expect 0.5)")
    print(f"  ratio(0) = {res0['ratio']:.6f}")
    print(f"  a2 integrand(0) = 20*2/3 - 0.5/3 = {20*2/3 - 0.5/3:.6f} vs computed {res0['a2_integrand_full']:.6f}")

    # =========================================================================
    # PART 5: Gate verdict
    # =========================================================================
    ratio_fold = ratio_vals[np.argmin(np.abs(tau_vals - tau_fold))]
    ratio_max = np.max(ratio_vals)

    print(f"\n{'=' * 72}")
    print(f"GATE VERDICT: SPIN-CURV-61")
    print(f"{'=' * 72}")
    print(f"  Ratio at tau_fold = {tau_fold}: {ratio_fold:.6f}")
    print(f"  Max ratio over [0, 0.5]:   {ratio_max:.6f}")
    print(f"  Threshold PASS: < 0.1")
    print(f"  Threshold INFO: [0.1, 1.0]")
    print(f"  Threshold FAIL: > 1.0")

    if ratio_fold < 0.1:
        verdict = "PASS"
        print(f"  --> {verdict}: Spin connection curvature negligible (< 10% of scalar term)")
    elif ratio_fold <= 1.0:
        verdict = "INFO"
        print(f"  --> {verdict}: Spin connection curvature non-negligible but sub-dominant")
    else:
        verdict = "FAIL"
        print(f"  --> {verdict}: Spin connection curvature dominates scalar term")

    print(f"\n  Physical meaning:")
    print(f"    a_2 integrand = (20R/3) - (K/3)")
    print(f"    At fold: = {result['scalar_term']:.4f} + ({result['spin_term']:.4f}) = {result['a2_integrand_full']:.4f}")
    print(f"    The spin connection curvature is a {ratio_fold*100:.1f}% CORRECTION to the dominant term.")
    print(f"    Simplified formula (scalar-curvature only) overestimates by {ratio_fold*100:.1f}%.")

    # =========================================================================
    # PART 6: Compute actual a_2 coefficient
    # =========================================================================
    d = 8  # (local)
    prefactor = (4.0 * PI) ** (-d / 2.0)
    # a_2 = prefactor * integrand * Vol(SU3)
    # But we need Vol for the Jensen metric. From canonical_constants:
    # Vol_SU3_Haar = 1349.74 for the round metric.
    # Jensen deformation is volume-preserving, so Vol(g_tau) = Vol(g_0).
    # But wait -- our metric is g = |B| * diag(L1, L2, ...) where |B_{ab}| = 3*delta_{ab}.
    # The actual volume depends on the overall scale: g_0 = 3*I_8.
    # Vol = sqrt(det(g_0)) * Vol_SU3_Haar... no, Haar volume already uses the
    # Killing metric normalization. Let me not conflate these.
    #
    # The a_2 coefficient per unit volume (integrand density) is what matters
    # for the ratio. The volume factor cancels in the ratio.

    print(f"\n--- a_2 density summary ---")
    print(f"  a_2 integrand per point = (4*pi)^{{-4}} * [(20R/3) - (K/3)]")
    print(f"  (4*pi)^{{-4}} = {prefactor:.6e}")
    print(f"  At tau_fold: a_2_density = {prefactor * result['a2_integrand_full']:.6e}")
    print(f"  Simplified (no spin):     {prefactor * result['scalar_term']:.6e}")
    print(f"  Spin correction:          {prefactor * result['spin_term']:.6e}")
    print(f"  Relative error of simplified: {ratio_fold*100:.2f}%")

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    outpath = os.path.join(SCRIPT_DIR, 's61_spin_curvature.npz')
    np.savez(outpath,
             tau_vals=tau_vals,
             R_vals=R_vals,
             K_vals=K_vals,
             ratio_vals=ratio_vals,
             scalar_term_vals=scalar_term_vals,
             spin_term_vals=spin_term_vals,
             a2_full_vals=a2_full_vals,
             tau_fold=tau_fold,
             R_fold=result['R_exact'],
             K_fold=result['K_exact'],
             ratio_fold=ratio_fold,
             scalar_term_fold=result['scalar_term'],
             spin_term_fold=result['spin_term'],
             a2_full_fold=result['a2_integrand_full'],
             tr_Omega_sq_fold=result['tr_Omega_sq'],
             tr_Omega_sq_explicit=explicit['tr_Omega_sq_explicit'],
             curv_cross_check_err=explicit['curv_err'],
             cliff_err=explicit['cliff_err'],  # (local)
             verdict=verdict,
             )
    print(f"\n  Data saved: {outpath}")

    # =========================================================================
    # PLOT
    # =========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('S61 SPIN-CURV-61: Spin Connection Curvature in Gilkey a_2', fontsize=14)

    # Panel 1: R and K vs tau
    ax = axes[0, 0]
    ax.plot(tau_vals, R_vals, 'b-', linewidth=2, label=r'$R(\tau)$ (scalar curvature)')
    ax.plot(tau_vals, K_vals, 'r-', linewidth=2, label=r'$|Riem|^2(\tau)$ (Kretschner)')
    ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{fold}$')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Curvature invariants')
    ax.set_title('Scalar curvature and Kretschner scalar')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 2: ratio vs tau
    ax = axes[0, 1]
    ax.plot(tau_vals, ratio_vals, 'k-', linewidth=2)
    ax.axhline(0.1, color='green', linestyle='--', alpha=0.7, label='PASS threshold (0.1)')
    ax.axhline(1.0, color='red', linestyle='--', alpha=0.7, label='FAIL threshold (1.0)')
    ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{fold}$')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$|spin\;term| / |scalar\;term|$')
    ax.set_title(f'Ratio at fold = {ratio_fold:.4f}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 3: a_2 integrand decomposition
    ax = axes[1, 0]
    ax.plot(tau_vals, scalar_term_vals, 'b-', linewidth=2, label=r'$20R/3$ (scalar)')
    ax.plot(tau_vals, np.abs(spin_term_vals), 'r-', linewidth=2, label=r'$|K/3|$ (spin connection)')
    ax.plot(tau_vals, a2_full_vals, 'k--', linewidth=2, label=r'Full $a_2$ integrand')
    ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{fold}$')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('a_2 integrand (per point)')
    ax.set_title('a_2 integrand decomposition')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 4: Full a_2 density
    ax = axes[1, 1]
    a2_density_full = prefactor * a2_full_vals
    a2_density_simplified = prefactor * scalar_term_vals
    ax.plot(tau_vals, a2_density_full, 'k-', linewidth=2, label='Full (with spin)')
    ax.plot(tau_vals, a2_density_simplified, 'b--', linewidth=2, label='Simplified (scalar only)')
    ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=r'$\tau_{fold}$')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$a_2$ density $= (4\pi)^{-4} \times$ integrand')
    ax.set_title(r'$a_2$ coefficient density: full vs simplified')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    figpath = os.path.join(SCRIPT_DIR, 's61_spin_curvature.png')
    plt.savefig(figpath, dpi=150)
    plt.close()
    print(f"  Plot saved: {figpath}")

    elapsed = time.time() - t0
    print(f"\n  Total runtime: {elapsed:.2f}s")
    print(f"\n{'=' * 72}")
    print(f"DONE. Verdict: {verdict} (ratio = {ratio_fold:.6f})")
    print(f"{'=' * 72}")


if __name__ == '__main__':
    main()
