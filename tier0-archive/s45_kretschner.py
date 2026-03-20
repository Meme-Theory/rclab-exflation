#!/usr/bin/env python3
"""
KRETSCHNER-12D-45: Kretschner Scalar on M^4 x SU(3)
====================================================

Session 45, Wave 4-2 — Schwarzschild-Penrose-Geometer

Computes the full Kretschner scalar K = R_{abcd} R^{abcd} on the 12D
product manifold M^4 x K, where:
    M^4  = 4D Friedmann spacetime (FLRW, spatially flat)
    K    = SU(3) with Jensen-deformed left-invariant metric g_tau

For a PRODUCT metric g_12D = g_4D + g_8D (no warping, no off-diagonal):
    K_total = K_4D + K_internal + K_mixed
    K_mixed = 0 exactly (Riemann tensor of a product is block-diagonal)

The internal Kretschner K_internal is computed from the EXACT ANALYTIC
formula K(tau) derived in SP-2 (Session 17a, verified at machine epsilon
against full numerical Riemann tensor in R-1, Session 20a).

The 4D Kretschner for FLRW:
    K_4D = 12 [H^4 + (H_dot)^2 + H^2 H_dot]     (Friedmann, k=0)
         = 12 [H^4 + H^2 H_dot]                   (for matter-dominated)

At the fold (BCS transit), the equation of state w = 1 (stiff matter/
kinetic-dominated), giving K_4D in terms of H_fold.

CRITICAL POINT (Maia-Chaves, Paper 29): For a WARPED product
    ds^2 = g_4D + R(t)^2 g_8D
the Kretschner does NOT simply add — the extrinsic curvature terms
K_{mu,nu} contribute mixed terms via the Gauss equation. However, at
the fold (where R_dot/R can be related to H_fold), the mixed terms
are O(H^2 * K_internal/M_KK^2) << K_internal, because H_fold/M_KK << 1.

We compute both cases:
    (A) Pure product metric (K_mixed = 0)
    (B) Warped product with extrinsic curvature corrections

Gate: KRETSCHNER-12D-45 — INFO (geometric diagnostic)

Author: Schwarzschild-Penrose-Geometer
Date: 2026-03-15
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from canonical_constants import (
    tau_fold, H_fold, M_KK, M_KK_gravity, M_KK_kerner,
    g0_diag,
)

# =========================================================================
# SECTION 1: EXACT ANALYTIC CURVATURE FORMULAS (SP-2)
# =========================================================================

def K_exact(s):
    """
    Exact Kretschner scalar K(s) = R_{abcd} R^{abcd} on (SU(3), g_s).

    Jensen metric: g_s = g_0 * diag(e^{2s}, e^{-2s}x3, e^{s}x4)
    where g_0 = 3 * I_8 is the Killing metric normalization.

    Derived in SP-2 (Session 17a), verified at machine epsilon.
    At s=0: K = 1/2 (bi-invariant SU(3)).
    """
    return (
        (23.0/96) * np.exp(-8*s)
        - 1.0 * np.exp(-5*s)
        + (5.0/16) * np.exp(-4*s)
        + (11.0/6) * np.exp(-2*s)
        - (3.0/2) * np.exp(-s)
        + 17.0/32
        + (1.0/12) * np.exp(4*s)
    )


def K_prime(s):
    """dK/ds — first derivative of Kretschner scalar."""
    return (
        (23.0/96) * (-8) * np.exp(-8*s)
        + (-1.0) * (-5) * np.exp(-5*s)
        + (5.0/16) * (-4) * np.exp(-4*s)
        + (11.0/6) * (-2) * np.exp(-2*s)
        + (-3.0/2) * (-1) * np.exp(-s)
        + (1.0/12) * 4 * np.exp(4*s)
    )


def K_double_prime(s):
    """d^2K/ds^2."""
    return (
        (23.0/96) * 64 * np.exp(-8*s)
        + (-1.0) * 25 * np.exp(-5*s)
        + (5.0/16) * 16 * np.exp(-4*s)
        + (11.0/6) * 4 * np.exp(-2*s)
        + (-3.0/2) * 1 * np.exp(-s)
        + (1.0/12) * 16 * np.exp(4*s)
    )


def R_scalar_exact(s):
    """Exact scalar curvature R(s) on (SU(3), g_s). R(0) = 2."""
    return -0.25 * np.exp(-4*s) + 2.0 * np.exp(-s) - 0.25 + 0.5 * np.exp(2*s)


def Ric2_exact(s):
    """Exact |Ric|^2(s). |Ric|^2(0) = 0.5."""
    return (
        (1.0/12) * np.exp(-8*s)
        + (-1.0/2) * np.exp(-5*s)
        + (1.0/8) * np.exp(-4*s)
        + (13.0/12) * np.exp(-2*s)
        + (-1.0/2) * np.exp(-s)
        + 1.0/8
        + (1.0/12) * np.exp(4*s)
    )


def Weyl2_from_bianchi(s):
    """
    |Weyl|^2 via Bianchi decomposition:
        |C|^2 = K - (4/(n-2))|Ric|^2 + 2R^2/((n-1)(n-2))
    for n=8 (dim SU(3)).
    """
    n = 8
    K = K_exact(s)
    Ric2 = Ric2_exact(s)
    R = R_scalar_exact(s)
    return K - (4.0/(n-2)) * Ric2 + 2.0 * R**2 / ((n-1)*(n-2))


# =========================================================================
# SECTION 2: NUMERICAL VERIFICATION VIA FULL RIEMANN TENSOR
# =========================================================================

def compute_K_numerical(s):
    """
    Compute K(s) numerically from the full 8x8x8x8 Riemann tensor.

    Uses the infrastructure from r20a_riemann_tensor.py:
    - Build Jensen-deformed metric
    - Construct ON frame
    - Compute structure constants in ON frame
    - Compute Levi-Civita connection
    - Build Riemann tensor from Christoffel symbols (pure algebra for Lie groups)
    - Contract: K = sum_{abcd} R_{abcd}^2 (in ON frame)
    """
    from tier1_dirac_spectrum import (
        su3_generators,
        compute_structure_constants,
        compute_killing_form,
        jensen_metric,
        orthonormal_frame,
        frame_structure_constants,
        connection_coefficients,
    )

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # Riemann tensor: R^d_{abc} (mixed)
    term1 = np.einsum('ebc,dae->dabc', Gamma, Gamma)
    term2 = np.einsum('eac,dbe->dabc', Gamma, Gamma)
    term3 = np.einsum('abe,dec->dabc', ft, Gamma)
    R_mixed = term1 - term2 - term3  # R_mixed[d,a,b,c] = R^d_{abc}

    # Lower: R_{abcd} = R^d_{abc} (trivial in ON frame)
    R_abcd = np.einsum('dabc->abcd', R_mixed)

    # Kretschner: K = R_{abcd} R^{abcd} = sum R_{abcd}^2 (ON frame)
    K = float(np.sum(R_abcd**2))

    # Also extract Ricci tensor and scalar curvature for cross-check
    Ric = np.einsum('abca->bc', R_abcd)
    R_scalar = float(np.trace(Ric))
    Ric2 = float(np.sum(Ric**2))

    # Weyl via Bianchi
    n = 8
    Weyl2 = K - (4.0/(n-2)) * Ric2 + 2.0 * R_scalar**2 / ((n-1)*(n-2))

    # Ricci eigenvalues (sectoral structure)
    Ric_eigs = np.sort(np.linalg.eigvalsh(Ric))

    return {
        'K': K,
        'R_scalar': R_scalar,
        'Ric2': Ric2,
        'Weyl2': Weyl2,
        'Ric_eigs': Ric_eigs,
        'R_abcd': R_abcd,
        'Ric': Ric,
        'g_s': g_s,
    }


# =========================================================================
# SECTION 3: 4D KRETSCHNER FOR FLRW SPACETIME
# =========================================================================

def K_FLRW(H, H_dot, k=0):
    """
    Kretschner scalar for FLRW spacetime ds^2 = -dt^2 + a(t)^2 [dr^2/(1-kr^2) + r^2 dOmega^2].

    For k=0 (spatially flat):
        R^{abcd} R_{abcd} = 12 * (H_dot^2 + H^4 + H_dot * H^2 + (k/a^2)^2 + ...)

    More precisely, from the FLRW Riemann tensor:
        R^0_{i0j} = (a_ddot/a) delta_{ij}
        R^i_{jkl} = (H^2 + k/a^2)(delta_{ik}delta_{jl} - delta_{il}delta_{jk})

    Kretschner (k=0):
        K_4D = 12 * [(a_ddot/a)^2 + H^4]
             = 12 * [(H_dot + H^2)^2 + H^4]

    For w=1 (stiff matter): a ~ t^{1/3}, H = 1/(3t), H_dot = -1/(3t^2) = -3H^2
        K_4D = 12 * [(-3H^2 + H^2)^2 + H^4] = 12 * [4H^4 + H^4] = 60 H^4

    For w=1/3 (radiation): a ~ t^{1/2}, H = 1/(2t), H_dot = -1/(2t^2) = -2H^2
        K_4D = 12 * [(-2H^2 + H^2)^2 + H^4] = 12 * [H^4 + H^4] = 24 H^4
    """
    a_ddot_over_a = H_dot + H**2
    return 12.0 * (a_ddot_over_a**2 + H**4)


def K_FLRW_stiff(H):
    """K_4D for w=1 (stiff matter / kinetic dominated). K = 60 H^4."""
    return 60.0 * H**4


def K_FLRW_radiation(H):
    """K_4D for w=1/3 (radiation). K = 24 H^4."""
    return 24.0 * H**4


# =========================================================================
# SECTION 4: WARPED PRODUCT CORRECTIONS (Maia-Chaves / Gauss-Codazzi)
# =========================================================================

def K_warped_correction(H, K_int, R_int, n_int=8, R_dot_over_R=None):
    """
    Correction to Kretschner from warping in ds^2 = g_4D + R(t)^2 g_8D.

    For a warped product M^4 x_R K^n with warp factor R(t), the Gauss
    equation (Paper 29, Maia-Chaves) gives additional terms:

    The extrinsic curvature of the K^n fibers embedded in the 12D space is:
        K_{ij} = -(R_dot/R) h_{ij}
    where h_{ij} is the metric on K^n, and the dot is d/dt.

    The Gauss equation:
        R^{(12)}_{ijkl} = R^{(n)}_{ijkl} + K_{ik}K_{jl} - K_{il}K_{jk}
                        = R^{(n)}_{ijkl} + (R_dot/R)^2 (h_{ik}h_{jl} - h_{il}h_{jk})

    The mixed Kretschner corrections (schematically):

    K_mixed ~ 2 * n_int * (R_dot/R)^2 * R_int   (from cross-terms)
            + n_int * (n_int-1) * (R_dot/R)^4     (from extrinsic x extrinsic)

    At the fold, R_dot/R ~ H_fold (the internal space Hubble rate).

    In our framework, R(t) = e^{-tau(t)} (for su(2) sector) or e^{tau(t)/2}
    (for C^2 sector), so R_dot/R ~ tau_dot ~ v_terminal.

    The key point: tau_dot at fold ~ v_terminal = 26.5 (in M_KK units), but
    the internal curvature K_internal ~ 0.53 (in M_KK units). The ratio
    (R_dot/R)^2 / K_internal ~ v^2 / K ~ 26.5^2 / 0.53 ~ 1325.

    So the warped corrections are NOT negligible — they dominate at the
    fold due to the large transit velocity!

    However, this is the transit regime. At the present epoch (tau frozen
    near fold, tau_dot ~ 0), the warped corrections vanish.

    Args:
        H: Hubble parameter
        K_int: internal Kretschner
        R_int: internal scalar curvature
        n_int: internal dimension (8 for SU(3))
        R_dot_over_R: d(ln R)/dt for the internal warp factor
                      If None, estimated as H (equal rates)

    Returns:
        dict with correction terms
    """
    if R_dot_over_R is None:
        R_dot_over_R = H

    beta = R_dot_over_R  # shorthand

    # Extrinsic curvature squared: K_{ij}K^{ij} = n * beta^2
    # (since K_{ij} = -beta h_{ij}, K^{ij}K_{ij} = n * beta^2)
    KK_sq = n_int * beta**2

    # K_{ij}K_{kl} cross terms contribute to Kretschner:
    # From (K_{ik}K_{jl} - K_{il}K_{jk})^2 contracted:
    # = beta^4 * (h_{ik}h_{jl} - h_{il}h_{jk})^2 contracted
    # = beta^4 * 2 * n_int * (n_int - 1)
    K_extrinsic_sq = 2.0 * n_int * (n_int - 1) * beta**4

    # Cross term between intrinsic and extrinsic Riemann:
    # 2 * R^{(n)}_{ijkl} * (K_{ik}K_{jl} - K_{il}K_{jk})
    # = 2 * beta^2 * R^{(n)}_{ijkl} * (h_{ik}h_{jl} - h_{il}h_{jk})
    # The contraction R^{(n)}_{ijkl}(h_{ik}h_{jl} - h_{il}h_{jk}) = 2*R_scalar^{(n)}
    # (by definition of scalar curvature: R = R^{ij}_{ij})
    K_cross = 4.0 * beta**2 * R_int

    # Mixed components R^0_{i0j} contribute:
    # R^0_{i0j} = -(R_ddot/R) h_{ij} for each internal direction
    # Their Kretschner contribution: 2*n * (R_ddot/R)^2
    # Estimate R_ddot/R ~ H^2 + H_dot (from Friedmann)
    # For w=1: H_dot = -3H^2, so R_ddot/R ~ -2H^2
    # Contribution: 2*n*4*H^4 = 8*n*H^4
    K_0i0j = 2.0 * n_int * (2.0 * beta**2)**2  # rough estimate assuming R_ddot/R ~ 2*beta^2

    return {
        'K_extrinsic_sq': K_extrinsic_sq,
        'K_cross': K_cross,
        'K_0i0j': K_0i0j,
        'K_total_correction': K_extrinsic_sq + K_cross + K_0i0j,
        'beta': beta,
        'beta_sq': beta**2,
    }


# =========================================================================
# SECTION 5: MAIN COMPUTATION
# =========================================================================

def main():
    t0 = time.time()

    print("=" * 78)
    print("  KRETSCHNER-12D-45: Kretschner Scalar on M^4 x SU(3)")
    print("  Schwarzschild-Penrose-Geometer — Session 45, Wave 4-2")
    print("=" * 78)

    # =================================================================
    # PART 1: Internal Kretschner K_internal at key tau values
    # =================================================================

    print("\n" + "=" * 78)
    print("  PART 1: INTERNAL KRETSCHNER K(tau) ON JENSEN-DEFORMED SU(3)")
    print("=" * 78)

    tau_values = [0.0, 0.10, 0.15, 0.190, 0.20, 0.285, 0.30, 0.50, 1.0, 2.0]
    tau_labels = {
        0.0: 'round (tau=0)',
        0.190: 'FOLD (tau_fold)',
        0.285: 'DNP crossing',
        0.15: 'phi_paasch',
    }

    print(f"\n  Analytic K(tau) formula (SP-2, verified machine epsilon):")
    print(f"    K(s) = (23/96)e^{{-8s}} - e^{{-5s}} + (5/16)e^{{-4s}}")
    print(f"         + (11/6)e^{{-2s}} - (3/2)e^{{-s}} + 17/32 + (1/12)e^{{4s}}")
    print()

    print(f"  {'tau':>6}  {'K (analytic)':>14}  {'K (numerical)':>14}  {'err':>10}  {'Label'}")
    print(f"  {'------':>6}  {'------------':>14}  {'-------------':>14}  {'---':>10}  {'-----'}")

    results_by_tau = {}
    for tau in tau_values:
        K_an = K_exact(tau)
        res = compute_K_numerical(tau)
        K_num = res['K']
        err = abs(K_an - K_num) / max(abs(K_an), 1e-15)
        label = tau_labels.get(tau, '')
        print(f"  {tau:6.3f}  {K_an:14.8f}  {K_num:14.8f}  {err:10.2e}  {label}")
        results_by_tau[tau] = {
            'K_analytic': K_an,
            'K_numerical': K_num,
            'err': err,
            'R_scalar': res['R_scalar'],
            'Ric2': res['Ric2'],
            'Weyl2': res['Weyl2'],
            'Ric_eigs': res['Ric_eigs'],
        }

    # =================================================================
    # PART 2: Detailed analysis at tau_fold = 0.190
    # =================================================================

    print("\n" + "=" * 78)
    print("  PART 2: DETAILED ANALYSIS AT tau_fold = 0.190")
    print("=" * 78)

    tau_f = tau_fold  # = 0.19
    K_fold = K_exact(tau_f)
    K_round = K_exact(0.0)
    K_prime_fold = K_prime(tau_f)
    K_pp_fold = K_double_prime(tau_f)
    R_fold = R_scalar_exact(tau_f)
    R_round = R_scalar_exact(0.0)
    Ric2_fold = Ric2_exact(tau_f)
    Ric2_round = Ric2_exact(0.0)
    Weyl2_fold = Weyl2_from_bianchi(tau_f)
    Weyl2_round = Weyl2_from_bianchi(0.0)

    res_fold = results_by_tau[0.190]

    print(f"\n  INTERNAL GEOMETRY AT tau_fold = {tau_f}:")
    print(f"    K_internal(fold)   = {K_fold:.10f}   (M_KK^4 units)")
    print(f"    K_internal(round)  = {K_round:.10f}   (exact = 1/2)")
    print(f"    K(fold)/K(round)   = {K_fold/K_round:.6f}")
    print(f"    K'(fold)           = {K_prime_fold:.10f}")
    print(f"    K''(fold)          = {K_pp_fold:.10f}")
    print()
    print(f"    R(fold)            = {R_fold:.10f}   (scalar curvature)")
    print(f"    R(round)           = {R_round:.10f}   (exact = 2)")
    print(f"    |Ric|^2(fold)      = {Ric2_fold:.10f}")
    print(f"    |Ric|^2(round)     = {Ric2_round:.10f}  (exact = 1/2)")
    print(f"    |C|^2(fold)        = {Weyl2_fold:.10f}  (Weyl)")
    print(f"    |C|^2(round)       = {Weyl2_round:.10f}  (exact = 5/14)")
    print()

    # Bianchi decomposition fractions at fold
    n_dim = 8
    frac_weyl = Weyl2_fold / K_fold
    frac_traceless_ric = (4.0/(n_dim-2)) * (Ric2_fold - R_fold**2/n_dim) / K_fold
    frac_scalar = 2.0 * R_fold**2 / (n_dim*(n_dim-1)) / K_fold

    print(f"  BIANCHI DECOMPOSITION at fold:")
    print(f"    K = |C|^2 + (4/(n-2))|Ric_0|^2 + 2R^2/(n(n-1))")
    print(f"    Weyl fraction:            {frac_weyl:.6f}  ({frac_weyl*100:.2f}%)")
    print(f"    Traceless Ricci fraction:  {frac_traceless_ric:.6f}  ({frac_traceless_ric*100:.2f}%)")
    print(f"    Scalar fraction:           {frac_scalar:.6f}  ({frac_scalar*100:.2f}%)")
    print(f"    Sum check:                 {frac_weyl + frac_traceless_ric + frac_scalar:.10f}")
    print()

    # Ricci eigenvalues at fold (sectoral structure)
    eigs = res_fold['Ric_eigs']
    print(f"  RICCI EIGENVALUES at fold (ON frame, sorted):")
    for i, e in enumerate(eigs):
        sector = ''
        if i < 3:
            sector = '  su(2)'
        elif i < 7:
            sector = '  C^2'
        else:
            sector = '  u(1)'
        print(f"    lambda_{i} = {e:.8f}{sector}")

    # Numerical cross-check
    print(f"\n  NUMERICAL CROSS-CHECK:")
    print(f"    K (analytic) = {K_fold:.10f}")
    print(f"    K (numerical) = {res_fold['K_numerical']:.10f}")
    print(f"    Relative error: {res_fold['err']:.2e}")

    # =================================================================
    # PART 3: 4D Kretschner from FLRW
    # =================================================================

    print("\n" + "=" * 78)
    print("  PART 3: 4D KRETSCHNER FROM FLRW COSMOLOGY")
    print("=" * 78)

    # At the fold: stiff matter (w=1) equation of state
    # H_fold = 586.53 M_KK
    K_4D_stiff = K_FLRW_stiff(H_fold)
    K_4D_rad = K_FLRW_radiation(H_fold)

    print(f"\n  H_fold = {H_fold:.4f} M_KK (from canonical_constants)")
    print(f"  M_KK = {M_KK:.4e} GeV (gravity route)")
    print()
    print(f"  4D Kretschner (w=1, stiff):     K_4D = {K_4D_stiff:.6e}  M_KK^4")
    print(f"  4D Kretschner (w=1/3, radiation): K_4D = {K_4D_rad:.6e}  M_KK^4")
    print()

    # Key ratio
    ratio_stiff = K_fold / K_4D_stiff
    ratio_rad = K_fold / K_4D_rad
    print(f"  K_internal / K_4D (stiff):       {ratio_stiff:.6e}")
    print(f"  K_internal / K_4D (radiation):   {ratio_rad:.6e}")
    print()
    print(f"  K_4D / K_internal (stiff):       {1.0/ratio_stiff:.2f}")
    print(f"  K_4D / K_internal (radiation):   {1.0/ratio_rad:.2f}")

    # =================================================================
    # PART 4: Physical units
    # =================================================================

    print("\n" + "=" * 78)
    print("  PART 4: PHYSICAL UNITS (GeV)")
    print("=" * 78)

    # In M_KK units, curvature has units of M_KK^{-2} (for Riemann, 2 indices)
    # The Kretschner K = R^{abcd}R_{abcd} has units M_KK^{-4} (for 4 indices on Riemann)
    # WAIT: In our convention, the metric g_tau is dimensionless (on the Lie algebra),
    # and tau is dimensionless. The curvature R_{abcd} has units of 1/L^2 where L
    # is the physical radius of SU(3).
    #
    # The physical metric is g^{phys} = R_{KK}^2 * g_tau where R_{KK} = 1/M_KK.
    # Under rescaling g -> lambda^2 g:
    #   R_{abcd} -> lambda^{-2} R_{abcd} (one factor of lambda^{-2} from the inverse metric)
    #   K = R^{abcd}R_{abcd} -> lambda^{-4} K
    #
    # So K_phys = K_dimless * M_KK^4 (converting from 1/R_KK^4)

    K_internal_GeV4 = K_fold * M_KK**4
    K_4D_GeV4 = K_4D_stiff * M_KK**4

    print(f"\n  K_internal(fold) in GeV^4:")
    print(f"    K_internal = {K_fold:.8f} * M_KK^4")
    print(f"              = {K_fold:.8f} * ({M_KK:.4e})^4")
    print(f"              = {K_internal_GeV4:.6e} GeV^4")
    print()
    print(f"  K_4D(fold) in GeV^4 (w=1):")
    print(f"    K_4D = {K_4D_stiff:.6e} * M_KK^4")
    print(f"        = {K_4D_GeV4:.6e} GeV^4")
    print()
    print(f"  12D total (pure product, K_mixed=0):")
    K_total_dimless = K_fold + K_4D_stiff
    print(f"    K_12D = K_4D + K_internal = {K_total_dimless:.6e}  (M_KK^4)")
    print(f"    K_12D = {K_total_dimless * M_KK**4:.6e}  GeV^4")
    print(f"    Internal fraction: {K_fold / K_total_dimless:.6e}")
    print(f"    4D fraction:       {K_4D_stiff / K_total_dimless:.10f}")

    # =================================================================
    # PART 5: Warped product corrections
    # =================================================================

    print("\n" + "=" * 78)
    print("  PART 5: WARPED PRODUCT CORRECTIONS (Maia-Chaves)")
    print("=" * 78)

    # At the fold during transit: the internal dimensions are dynamical
    # tau_dot ~ v_terminal = 26.5 M_KK (from s38_kz_defects)
    from canonical_constants import v_terminal

    # The warp factor for each sector:
    # su(2): R_{su2} = e^{-tau}, so R_dot/R = -tau_dot
    # C^2:   R_{C2} = e^{tau/2}, so R_dot/R = tau_dot/2
    # u(1):  R_{u1} = e^{tau}, so R_dot/R = tau_dot

    print(f"\n  Transit velocity: v_terminal = {v_terminal:.4f} M_KK")
    print(f"  (from canonical_constants, S38 Kibble-Zurek)")
    print()

    # Effective R_dot/R for internal space as a whole
    # The volume-preserving condition means the overall R doesn't change
    # But the SHAPE changes, and Kretschner cares about shape

    # For the Gauss-Codazzi analysis, the key quantity is the extrinsic curvature
    # K_{ij} = -(1/2) dg_{ij}/dt for the internal metric evolving in time
    # For Jensen: g_{ij}(t) = g_{ij}(tau(t)), so dg_{ij}/dt = tau_dot * dg_{ij}/dtau

    # The time derivative of the internal metric:
    # d(g_s)/dtau has sectoral structure:
    #   su(2): 2*e^{-2tau} -> dg/dtau = -2*g_{su2} -> (1/2g)(dg/dtau) = -1
    #   C^2:   e^{tau}     -> dg/dtau = g_{C2}     -> (1/2g)(dg/dtau) = 1/2
    #   u(1):  2*e^{2tau}  -> dg/dtau = 2*g_{u1}   -> (1/2g)(dg/dtau) = 1

    # Extrinsic curvature: K_{ij} = -(1/2) dg_{ij}/dt = -(tau_dot/2) dg_{ij}/dtau
    # For su(2): K_{aa} = -tau_dot * (-1) * g_{aa} = +tau_dot * g_{aa}  (NOT isotropic!)

    # The extrinsic curvature contribution to Kretschner is:
    # Delta K ~ 4 * sum_{i<j} (K_ii K_jj - K_ij^2)^2 + ...
    # This is complicated for anisotropic K_ij.

    # Let me compute it properly from the diagonal extrinsic curvature.
    # K_{aa} is diagonal in the ON frame with values:
    #   su(2) (3 dirs): k_su2 = tau_dot * 1  (from d(ln g_{su2})/dt = -2*tau_dot, K=-dg/2dt)
    #   C^2   (4 dirs): k_c2 = -tau_dot/2    (from d(ln g_{c2})/dt = tau_dot, K=-dg/2dt)
    #   u(1)  (1 dir):  k_u1 = -tau_dot       (from d(ln g_{u1})/dt = 2*tau_dot)

    # WAIT: Be more careful. The physical internal metric in ON frame is delta_{ij}.
    # The extrinsic curvature of the spatial slice in the (t, internal) spacetime:
    # K_{ij} = -(1/(2N)) (dg_{ij}/dt) where N=1 (lapse=1 in cosmic time)

    # For the coordinate metric g_{ij}(tau(t)):
    # dg_{ij}/dt = tau_dot * dg_{ij}/dtau

    # In ON frame e_a = E_{ab} X_b, the induced metric is delta_{ab}.
    # The extrinsic curvature in ON frame:
    # K_{ab} = -(1/2) E_{ai} E_{bj} dg^{coord}_{ij}/dt

    # For diagonal metric g_s = diag(g_1, ..., g_8) with g_a = g_0 * L_a(tau):
    # In ON frame: e_a = (1/sqrt(g_a)) X_a, so E_{ab} = delta_{ab}/sqrt(g_a)
    # K_{ab} = -(1/2) (1/sqrt(g_a*g_b)) * delta_{ab} * tau_dot * dg_a/dtau
    #        = -(tau_dot/2) * (1/g_a) * dg_a/dtau * delta_{ab}
    #        = -(tau_dot/2) * d(ln g_a)/dtau * delta_{ab}

    # d(ln g_a)/dtau for each sector:
    # su(2): g = g_0 * e^{-2tau}, d(ln g)/dtau = -2
    # C^2:   g = g_0 * e^{tau},   d(ln g)/dtau = +1
    # u(1):  g = g_0 * e^{2tau},  d(ln g)/dtau = +2

    tau_dot = v_terminal

    k_su2 = -(tau_dot/2) * (-2)   # = +tau_dot
    k_c2  = -(tau_dot/2) * (1)    # = -tau_dot/2
    k_u1  = -(tau_dot/2) * (2)    # = -tau_dot

    print(f"  Extrinsic curvature eigenvalues (ON frame):")
    print(f"    K_su2 (x3) = {k_su2:+.4f}  M_KK")
    print(f"    K_C2  (x4) = {k_c2:+.4f}   M_KK")
    print(f"    K_u1  (x1) = {k_u1:+.4f}  M_KK")

    # Mean curvature
    K_trace = 3*k_su2 + 4*k_c2 + 1*k_u1
    print(f"    Trace K = {K_trace:.6f}  (should be 0 for volume-preserving)")
    print(f"    (Volume-preserving: d(ln Vol)/dt = -K_trace = 0)")

    # Extrinsic Kretschner contribution:
    # From Gauss: R^{(12)}_{ijkl} = R^{(8)}_{ijkl} + K_{ik}K_{jl} - K_{il}K_{jk}
    # The correction to the internal Kretschner is:
    # Delta K = 2 * K_{ij}K_{kl} R^{(8)ijkl} + (K_{ik}K_{jl} - K_{il}K_{jk})^2

    # For diagonal K_{ab} = k_a delta_{ab}:
    # (K_{ik}K_{jl} - K_{il}K_{jk})^2 summed = sum_{i<j} (k_i k_j)^2 * 4
    # = 4 * [C(3,2)*k_su2^4 + C(4,2)*k_c2^4 + 3*4*k_su2^2*k_c2^2
    #        + 3*1*k_su2^2*k_u1^2 + 4*1*k_c2^2*k_u1^2]
    # Wait, let me be more careful.

    # The "extrinsic-extrinsic" Kretschner contribution is:
    # (K_{ik}K_{jl} - K_{il}K_{jk})^2 summed over all i,j,k,l
    # For diagonal K: only i!=j contribute (the antisymmetric part vanishes when i=j)
    # Term = sum_{i,j} (k_i k_j)^2 - sum_{i,j} k_i k_j k_i k_j  <- wait
    # (K_{ik}K_{jl} - K_{il}K_{jk}) for i=k,j=l: k_i^2 delta_{ij} delta_{ij} - k_i k_j delta_{ii}delta_{jj}...

    # Let me just compute the full contraction numerically.
    n_int = 8
    k_diag = np.array([k_su2]*3 + [k_c2]*4 + [k_u1]*1)

    # K_ext[i,j] = k_diag[i] * delta[i,j]
    K_ext = np.diag(k_diag)

    # Construct the extrinsic Riemann-like tensor:
    # C_{ijkl} = K_{ik}K_{jl} - K_{il}K_{jk}
    C_ext = np.einsum('ik,jl->ijkl', K_ext, K_ext) - np.einsum('il,jk->ijkl', K_ext, K_ext)

    # ||C_ext||^2
    K_ext_sq = float(np.sum(C_ext**2))

    # Cross term: 2 * R^{(8)}_{ijkl} * C_{ijkl}
    # Need the full Riemann tensor at fold
    res_fold_full = compute_K_numerical(tau_f)
    R8 = res_fold_full['R_abcd']
    K_cross_term = 2.0 * float(np.sum(R8 * C_ext))

    # Full Gauss Kretschner:
    # ||R^{(12)}_{int}||^2 = ||R^{(8)} + C_ext||^2 = ||R^{(8)}||^2 + 2<R^{(8)},C_ext> + ||C_ext||^2
    K_gauss = K_fold + K_cross_term + K_ext_sq

    print(f"\n  GAUSS EQUATION ANALYSIS (warped product at fold during transit):")
    print(f"    K_intrinsic  (||R^(8)||^2):  {K_fold:.8f}")
    print(f"    K_cross      (2<R,C_ext>):   {K_cross_term:+.8f}")
    print(f"    K_extrinsic  (||C_ext||^2):  {K_ext_sq:.8f}")
    print(f"    K_Gauss_total:               {K_gauss:.8f}")
    print(f"    Extrinsic/Intrinsic ratio:   {K_ext_sq/K_fold:.2f}")
    print(f"    Cross/Intrinsic ratio:       {abs(K_cross_term)/K_fold:.2f}")

    print(f"\n  INTERPRETATION:")
    print(f"    During transit (tau_dot = {v_terminal:.1f} M_KK), the extrinsic")
    print(f"    curvature contribution is {K_ext_sq/K_fold:.0f}x the intrinsic Kretschner.")
    print(f"    The 12D curvature is dominated by the MOTION of the internal space,")
    print(f"    not by the curvature of the internal space itself.")
    print(f"    This is the geometric signature of the stiff matter (w=1) epoch.")
    print(f"\n    POST-TRANSIT (tau_dot -> 0):")
    print(f"    K_ext -> 0, K_cross -> 0, K_Gauss -> K_intrinsic = {K_fold:.6f}")
    print(f"    The frozen modulus means the internal geometry is the static")
    print(f"    Jensen-deformed SU(3). Only the intrinsic Kretschner remains.")

    # =================================================================
    # PART 6: K(tau) monotonicity and derivative structure
    # =================================================================

    print("\n" + "=" * 78)
    print("  PART 6: K(tau) MONOTONICITY AND DERIVATIVE STRUCTURE")
    print("=" * 78)

    tau_dense = np.linspace(0, 2.0, 201)
    K_dense = K_exact(tau_dense)
    Kp_dense = K_prime(tau_dense)

    # Check monotonicity
    dK = np.diff(K_dense)
    is_monotone = np.all(dK > 0)

    print(f"\n  K(tau) monotonically increasing on [0, 2]: {is_monotone}")
    print(f"  K(0) = {K_exact(0.0):.10f}")
    print(f"  K(0.190) = {K_fold:.10f}")
    print(f"  K(2.0) = {K_exact(2.0):.6f}")
    print(f"  K(fold)/K(round) = {K_fold/K_round:.6f}")
    print(f"  K'(fold) = {K_prime_fold:.10f}  (> 0: increasing)")
    print(f"  K''(fold) = {K_pp_fold:.10f}  (> 0: convex)")
    print()

    # Find where K' = 0 (if any)
    Kp_sign_changes = np.where(Kp_dense[:-1] * Kp_dense[1:] < 0)[0]
    if len(Kp_sign_changes) == 0:
        print(f"  K'(tau) has no zeros on [0, 2]. K is strictly monotone.")
    else:
        for idx in Kp_sign_changes:
            tau_zero = tau_dense[idx] + (tau_dense[idx+1] - tau_dense[idx]) * (-Kp_dense[idx]) / (Kp_dense[idx+1] - Kp_dense[idx])
            print(f"  K'(tau) = 0 near tau = {tau_zero:.4f}")

    # K'(0): check analytically
    # K'(0) = (23/96)*(-8) + (-1)*(-5) + (5/16)*(-4) + (11/6)*(-2) + (-3/2)*(-1) + (1/12)*4
    K_prime_0 = K_prime(0.0)
    print(f"\n  K'(0) = {K_prime_0:.10f}")
    print(f"  (Should be positive if K strictly increasing from tau=0)")

    # =================================================================
    # PART 7: Petrov classification context
    # =================================================================

    print("\n" + "=" * 78)
    print("  PART 7: PETROV CLASSIFICATION AND WEYL STRUCTURE")
    print("=" * 78)

    # For 8D, the Petrov classification generalizes to CMPP (Paper 23, Ortaggio)
    # The key object is the Weyl tensor. At the fold:
    n_dim = 8

    # Bianchi decomposition at round and fold
    for label, tau_val in [('round (tau=0)', 0.0), ('fold (tau=0.190)', 0.190)]:
        K_v = K_exact(tau_val)
        R_v = R_scalar_exact(tau_val)
        Ric2_v = Ric2_exact(tau_val)
        Weyl2_v = Weyl2_from_bianchi(tau_val)
        Ric0_2 = Ric2_v - R_v**2 / n_dim  # traceless Ricci squared

        f_w = Weyl2_v / K_v
        f_r = (4.0/(n_dim-2)) * Ric0_2 / K_v
        f_s = 2.0 * R_v**2 / (n_dim*(n_dim-1)) / K_v

        print(f"\n  {label}:")
        print(f"    K = {K_v:.8f}")
        print(f"    |C|^2 = {Weyl2_v:.8f}  ({f_w*100:.1f}%)")
        print(f"    (4/(n-2))|Ric_0|^2 = {(4.0/(n_dim-2))*Ric0_2:.8f}  ({f_r*100:.1f}%)")
        print(f"    2R^2/(n(n-1)) = {2*R_v**2/(n_dim*(n_dim-1)):.8f}  ({f_s*100:.1f}%)")
        print(f"    Tidal ratio |C|^2/K = {f_w:.6f}")

    print(f"\n  WEYL CURVATURE HYPOTHESIS:")
    print(f"    |C|^2(round) = {Weyl2_round:.8f} = 5/14 = {5.0/14:.8f}")
    print(f"    |C|^2(fold)  = {Weyl2_fold:.8f}")
    print(f"    |C|^2(fold)/|C|^2(round) = {Weyl2_fold/Weyl2_round:.6f}")
    print(f"    Weyl curvature INCREASES from round to fold.")
    print(f"    WCH direction: tau=0 -> fold -> large tau is entropy-increasing")
    print(f"    (Consistent with Penrose: round = low Weyl = initial state)")

    # =================================================================
    # PART 8: 12D Summary Table
    # =================================================================

    print("\n" + "=" * 78)
    print("  PART 8: 12D KRETSCHNER SUMMARY")
    print("=" * 78)

    print(f"""
  ========================================================
   KRETSCHNER SCALAR: M^4 x SU(3) at tau_fold = 0.190
  ========================================================

  A. INTERNAL K (Jensen-deformed SU(3), 8D)
  -------------------------------------------
    K_internal(round, tau=0)  = {K_round:.10f}  (exact = 1/2)
    K_internal(fold, tau=0.19)= {K_fold:.10f}
    Ratio fold/round:           {K_fold/K_round:.6f} (= 1 + {K_fold/K_round - 1:.4f})
    K'(fold):                   {K_prime_fold:.6f} (positive, increasing)
    K''(fold):                  {K_pp_fold:.6f} (positive, convex)

  B. 4D KRETSCHNER (FLRW, at fold)
  -------------------------------------------
    K_4D (w=1, stiff):         {K_4D_stiff:.6e}
    K_4D (w=1/3, rad):         {K_4D_rad:.6e}

  C. RATIO K_internal / K_4D
  -------------------------------------------
    At fold (w=1):              {ratio_stiff:.6e}
    At fold (w=1/3):            {ratio_rad:.6e}
    K_4D dominates by factor:   {1.0/ratio_stiff:.0f}x (stiff)

  D. 12D PRODUCT (no warping)
  -------------------------------------------
    K_12D = K_4D + K_internal = {K_total_dimless:.6e} M_KK^4
    Internal fraction:          {K_fold/K_total_dimless*100:.4f}%

  E. 12D WARPED (during transit, v = {v_terminal:.1f})
  -------------------------------------------
    K_Gauss (intrinsic + extrinsic): {K_gauss:.4f}
    Extrinsic dominates by:          {K_ext_sq/K_fold:.0f}x

  F. 12D POST-TRANSIT (frozen modulus)
  -------------------------------------------
    K_ext -> 0 (v -> 0)
    K_12D = K_4D(present) + K_internal(fold)
    Present-epoch K_4D negligible (H_0 << M_KK)
    K_12D ~ K_internal(fold) = {K_fold:.8f} M_KK^4

  ========================================================
    """)

    # =================================================================
    # PART 9: Dimensional analysis and Planck comparison
    # =================================================================

    print("=" * 78)
    print("  PART 9: COMPARISON WITH PLANCK CURVATURE")
    print("=" * 78)

    # Planck Kretschner: K_Pl ~ M_Pl^4 (in natural units)
    from canonical_constants import M_Pl_unreduced
    K_Pl = M_Pl_unreduced**4  # GeV^4

    print(f"\n  K_internal(fold) = {K_internal_GeV4:.6e} GeV^4")
    print(f"  K_Planck ~ M_Pl^4 = {K_Pl:.6e} GeV^4")
    print(f"  K_internal / K_Planck = {K_internal_GeV4/K_Pl:.6e}")
    print(f"  = (M_KK / M_Pl)^4 * K(fold)_dimless")
    print(f"  = ({M_KK/M_Pl_unreduced:.4e})^4 * {K_fold:.4f}")
    print(f"  = {(M_KK/M_Pl_unreduced)**4:.4e} * {K_fold:.4f}")
    print(f"  = {(M_KK/M_Pl_unreduced)**4 * K_fold:.6e}")
    print(f"\n  The internal curvature at the fold is {K_internal_GeV4/K_Pl:.1e}")
    print(f"  of the Planck curvature. Sub-Planckian by ~{np.log10(K_Pl/K_internal_GeV4):.0f} orders.")
    print(f"  (This is consistent: M_KK ~ 10^{{17}} GeV << M_Pl ~ 10^{{19}} GeV)")

    # =================================================================
    # SAVE
    # =================================================================

    print("\n" + "=" * 78)
    print("  SAVING DATA")
    print("=" * 78)

    out_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's45_kretschner.npz')

    # Build tau sweep for dense output
    tau_sweep = np.array(tau_values)
    K_sweep = np.array([K_exact(t) for t in tau_values])
    R_sweep = np.array([R_scalar_exact(t) for t in tau_values])
    Ric2_sweep = np.array([Ric2_exact(t) for t in tau_values])
    Weyl2_sweep = np.array([Weyl2_from_bianchi(t) for t in tau_values])

    np.savez(out_file,
        # Fold values
        tau_fold=tau_f,
        K_internal_fold=K_fold,
        K_internal_round=K_round,
        K_fold_over_K_round=K_fold/K_round,
        K_prime_fold=K_prime_fold,
        K_double_prime_fold=K_pp_fold,
        R_fold=R_fold,
        Ric2_fold=Ric2_fold,
        Weyl2_fold=Weyl2_fold,

        # 4D
        K_4D_stiff=K_4D_stiff,
        K_4D_rad=K_4D_rad,
        H_fold=H_fold,

        # Ratios
        K_ratio_stiff=ratio_stiff,
        K_ratio_rad=ratio_rad,

        # 12D product
        K_12D_product=K_total_dimless,
        internal_fraction=K_fold/K_total_dimless,

        # Warped
        K_Gauss_total=K_gauss,
        K_extrinsic_sq=K_ext_sq,
        K_cross_term=K_cross_term,
        v_terminal_used=v_terminal,

        # Bianchi fractions at fold
        frac_weyl=frac_weyl,
        frac_traceless_ric=frac_traceless_ric,
        frac_scalar=frac_scalar,

        # Sweep
        tau_sweep=tau_sweep,
        K_sweep=K_sweep,
        R_sweep=R_sweep,
        Ric2_sweep=Ric2_sweep,
        Weyl2_sweep=Weyl2_sweep,

        # Physical units
        K_internal_GeV4=K_internal_GeV4,
        M_KK_used=M_KK,

        # Ricci eigenvalues at fold
        Ric_eigs_fold=res_fold['Ric_eigs'],

        # Gate
        gate_name=np.array(['KRETSCHNER-12D-45']),
        gate_verdict=np.array(['INFO']),
    )

    print(f"\n  Saved: {out_file}")

    dt = time.time() - t0
    print(f"  Runtime: {dt:.1f}s")

    # =================================================================
    # FINAL SUMMARY
    # =================================================================

    print("\n" + "=" * 78)
    print("  KRETSCHNER-12D-45: FINAL SUMMARY")
    print("=" * 78)
    print(f"""
  Gate: KRETSCHNER-12D-45 — INFO (geometric diagnostic)

  KEY RESULTS:

  1. K_internal(fold) = {K_fold:.8f} (M_KK^4 units)
     K_internal(round) = {K_round:.8f} = 1/2 exact
     Ratio: {K_fold/K_round:.6f} ({(K_fold/K_round-1)*100:.2f}% increase at fold)

  2. K_4D(w=1) = {K_4D_stiff:.4e} >> K_internal = {K_fold:.4f}
     The 4D Friedmann curvature at H_fold = {H_fold:.1f} M_KK DOMINATES
     internal curvature by factor {1.0/ratio_stiff:.0f}x

  3. During transit: extrinsic curvature (from v_terminal = {v_terminal:.1f})
     dominates by {K_ext_sq/K_fold:.0f}x. The 12D Kretschner is motion-dominated.

  4. Post-transit (frozen modulus): K_ext -> 0. Internal K_internal = {K_fold:.6f}
     is the sole contribution from the internal space. K_4D(present epoch) ~ 0.
     The present-day 12D Kretschner is entirely internal = {K_fold:.6f} M_KK^4.

  5. Bianchi decomposition at fold:
     Weyl: {frac_weyl*100:.1f}%, Traceless Ricci: {frac_traceless_ric*100:.1f}%, Scalar: {frac_scalar*100:.1f}%
     (vs round: Weyl=71.4%, Traceless Ricci=0%, Scalar=28.6%)

  6. WCH consistent: |C|^2 INCREASES from round to fold.
     Round metric IS the Weyl-minimal state.

  CONSTRAINT:
     The 12D Kretschner at the fold is sub-Planckian by {np.log10(K_Pl/K_internal_GeV4):.0f} orders.
     No curvature singularity. The internal space is mildly deformed (K changes 7%).
     The dominant curvature source during transit is the MOTION (extrinsic K),
     not the SHAPE (intrinsic K). After transit, only the mild intrinsic K remains.
    """)

    return results_by_tau


if __name__ == '__main__':
    main()
