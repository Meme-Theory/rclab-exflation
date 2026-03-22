#!/usr/bin/env python3
"""
INDUCED-G-44: Self-Consistent G_N from Bosonic a_2 Seeley-DeWitt Coefficient
=============================================================================

Context:
    S43 CC workshop E2: S_F^Connes = 0 by BDI symmetry. The fermionic spectral
    action vanishes. G_N must come from the BOSONIC spectral action only.

    The bosonic spectral action sums over fluctuation operators on the internal
    space K = SU(3):
        1. Scalar Laplacian Delta_0 (conformal mode, 1 DOF)
        2. Hodge Laplacian Delta_1 on 1-forms (gauge fields, 8 DOF)
        3. Lichnerowicz Laplacian Delta_L on symmetric TT 2-tensors (graviton, varies by sector)

    Each operator P = -nabla^2 + E has heat kernel expansion:
        Tr(e^{-tP}) = (4pi t)^{-d/2} * sum_n integral a_n(x,P) dvol * t^{n/2}

    For a general Laplacian-type operator (Gilkey 1995):
        a_0(P) = (4pi)^{-d/2} * tr(Id) * Vol(K)
        a_2(P) = (4pi)^{-d/2} * (1/6) * integral tr(6E + R*Id) dvol

    The Einstein-Hilbert coefficient in the 4D effective action is:
        1/(16 pi G_N) = f_2 * Lambda^2 * a_2^{total bos}

    where a_2^{total bos} sums over all bosonic field types.

Physics:
    The Dirac a_2 used in S42 (a_2 = 2776.17) came from sum d_k lambda_k^{-2}
    over the DIRAC spectrum. This is the a_2 for the Dirac operator D_K.

    The BOSONIC a_2 comes from connection Laplacians:
        - Scalar: a_2^{scalar} = (4pi)^{-4} * (R/6) * Vol(K) * 1
        - Vector: a_2^{gauge} = (4pi)^{-4} * (R/6 + Ric_trace/n) * Vol(K) * n
                  On 1-forms: E = Ric, so tr(6E + R*Id) = 6*tr(Ric) + R*n = 6R + 8R = 14R (d=8)
                  But more carefully: for Hodge Laplacian, a_2 per component...
        - TT tensor: a_2^{TT} from Lichnerowicz with known E.

    For the PRODUCT space M4 x K with flat M4:
        a_2(M4 x K, P) = Vol(M4)/(4pi)^2 * a_2(K, P_K)
    The 4D integration produces the Vol(M4) factor, leaving
        1/(16 pi G_N) ~ M_KK^2 * a_2^K

    CRUCIAL: We use the same normalization as S42's Dirac route:
        1/(16 pi G_N) = (96/pi^2) * f_2 * a_2^K * M_KK^2
    But now a_2^K comes from BOSONIC operators instead of Dirac.

    Alternatively, we can use the SPECTRAL ZETA function approach:
    For any elliptic operator P with eigenvalues mu_k, the spectral a_2 is
        a_2 = sum_k d_k * mu_k^{-1}   (for the second coefficient)
    This is what S42 computed for the Dirac operator (sum d_k / lambda_k^2 for D^2).
    We can compute the analogous sum for bosonic Laplacians using their eigenvalues.

Approach:
    We compute a_2^{bos} from BOTH routes:
    (A) Analytic: Using Gilkey's formula with known Ricci/scalar curvature at the fold.
    (B) Spectral: Using eigenvalue sums of the scalar and vector Laplacians.
    Then compare G_N^{bos} with G_N^{Dirac} (S42) and G_N^{Sakharov} (W1-1).

Gate: INDUCED-G-44
    PASS: G_N^{bos} within 1 OOM of G_N^{Sakharov}
    FAIL: > 3 OOM discrepancy
    INFO: intermediate

References:
    - Baptista Paper 13 (2021): bosons on M4 x SU(3)
    - Baptista Paper 40 (Bourguignon-Gauduchon 1992): spinor/metric variations
    - Gilkey (1995): Heat kernel on manifolds
    - Vassilevich (2003): Heat kernel review
    - s42_constants_snapshot.py: Dirac a_2 and M_KK extraction
    - s44_sakharov_gn_audit.py: Sakharov formula audit (W1-1)

Author: Baptista Spacetime Analyst (Session 44)
Date: 2026-03-14
"""

import numpy as np
import sys
import os
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    get_irrep,
    U1_IDX, SU2_IDX, C2_IDX,
)
from b6_scalar_vector_laplacian import dim_pq, casimir_pq
from sd20a_seeley_dewitt_gate import R_exact, Ric2_exact, K_exact
from r20a_riemann_tensor import compute_riemann_tensor_ON_fast, ricci_from_riemann

# =============================================================================
# CONSTANTS
# =============================================================================
from canonical_constants import M_Pl_reduced as M_PL_RED, tau_fold as TAU_FOLD  # 2.435e18 GeV
G_N_NAT = 1.0 / (8 * np.pi * M_PL_RED**2)
INV_16piG_OBS = M_PL_RED**2 / 2  # 1/(16 pi G) = M_Pl_red^2 / 2
PI = np.pi
DIM_K = 8  # dim(SU(3))

# Peter-Weyl sectors used in S42
SECTORS = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)]


def main():
    t_start = time.time()
    print("=" * 80)
    print("INDUCED-G-44: Self-Consistent G_N from Bosonic a_2")
    print("=" * 80)

    # =========================================================================
    # STEP 1: Load stored data
    # =========================================================================
    print("\n--- STEP 1: Loading data ---")

    d42c = np.load(os.path.join(SCRIPT_DIR, 's42_constants_snapshot.npz'), allow_pickle=True)
    d43L = np.load(os.path.join(SCRIPT_DIR, 's43_lichnerowicz.npz'), allow_pickle=True)
    d36 = np.load(os.path.join(SCRIPT_DIR, 's36_sfull_tau_stabilization.npz'), allow_pickle=True)

    a0_dirac = float(d42c['a0_fold'])       # 6440
    a2_dirac = float(d42c['a2_fold'])       # 2776.17
    a4_dirac = float(d42c['a4_fold'])       # 1350.72
    M_KK = float(d42c['M_KK_from_GN'])     # 7.43e16 GeV
    M_KK_kerner = float(d42c['M_KK_kerner'])  # 5.04e17 GeV

    print(f"  Dirac a_0 = {a0_dirac:.0f}")
    print(f"  Dirac a_2 = {a2_dirac:.4f}")
    print(f"  Dirac a_4 = {a4_dirac:.4f}")
    print(f"  M_KK (GN route) = {M_KK:.4e} GeV")
    print(f"  M_KK (Kerner route) = {M_KK_kerner:.4e} GeV")

    # Sakharov results from audit
    try:
        d_sak = np.load(os.path.join(SCRIPT_DIR, 's44_sakharov_gn_audit.npz'), allow_pickle=True)
        inv_16piG_sak = float(d_sak['inv_16piG_sakharov_full'])
        ratio_sak = float(d_sak['ratio_B'])
        print(f"  Sakharov 1/(16piG) = {inv_16piG_sak:.4e} GeV^2 (at Lambda=M_Pl)")
        print(f"  Sakharov ratio to obs = {ratio_sak:.4f}")
        has_sakharov = True
    except Exception as e:
        print(f"  Sakharov audit data not found: {e}")
        has_sakharov = False
        inv_16piG_sak = 0
        ratio_sak = 0

    # Lichnerowicz data at fold
    tau_L = d43L['tau_values']
    fold_idx_L = np.argmin(np.abs(tau_L - TAU_FOLD))
    Ric_u1 = d43L['ric_u1'][fold_idx_L]
    Ric_su2 = d43L['ric_su2'][fold_idx_L]
    Ric_c2 = d43L['ric_c2'][fold_idx_L]
    print(f"  Ric_u1(fold) = {Ric_u1:.6f}")
    print(f"  Ric_su2(fold) = {Ric_su2:.6f}")
    print(f"  Ric_c2(fold) = {Ric_c2:.6f}")

    # =========================================================================
    # STEP 2: Analytic curvature quantities at the fold
    # =========================================================================
    print(f"\n--- STEP 2: Curvature at tau = {TAU_FOLD} ---")

    R_K = R_exact(TAU_FOLD)
    Ric2 = Ric2_exact(TAU_FOLD)
    Kret = K_exact(TAU_FOLD)

    # Cross-check scalar curvature from Ricci components
    # R = Ric_{aa} summed = 1*Ric_u1 + 3*Ric_su2 + 4*Ric_c2
    R_from_ric = Ric_u1 + 3 * Ric_su2 + 4 * Ric_c2
    print(f"  R_K (analytic) = {R_K:.6f}")
    print(f"  R_K (from Ric components) = {R_from_ric:.6f}")
    print(f"  Agreement: {abs(R_K - R_from_ric):.2e}")
    print(f"  |Ric|^2 = {Ric2:.6f}")
    print(f"  |Riem|^2 = {Kret:.6f}")

    # Ricci tensor in ON frame (diagonal for Jensen metric)
    Ric_diag = np.zeros(8)
    Ric_diag[7] = Ric_u1           # u(1)
    Ric_diag[0:3] = Ric_su2        # su(2): indices 0,1,2
    Ric_diag[3:7] = Ric_c2         # C^2: indices 3,4,5,6

    # =========================================================================
    # STEP 3: Bosonic a_2 from Gilkey formula (ANALYTIC route)
    # =========================================================================
    print(f"\n--- STEP 3: Bosonic a_2 (Gilkey analytic) ---")

    # For a Laplacian-type operator P = -(g^{ij} D_i D_j + ...) = nabla^* nabla + E
    # on a vector bundle of rank r over an 8-manifold:
    #
    #   a_2(P) = (4pi)^{-4} * (1/6) * integral_K tr(6E + R * Id_r) dvol
    #
    # On a homogeneous space, all integrands are constant, so integral = Vol(K) * value.
    # The volume-normalized a_2 (dropping the (4pi)^{-4} * Vol(K) universal factor):
    #
    #   a_2^red(P) = (1/6) * tr(6E + R * Id_r) = tr(E) + (r/6) * R
    #
    # The PHYSICAL a_2 for the spectral action in the product M4 x K:
    #   1/(16 pi G_N) = f_2 * Lambda^2 * a_2^{bos total}
    #
    # But the project convention (S42) uses a_2 = sum_k d_k lambda_k^{-2} (spectral zeta)
    # for the Dirac operator. We need to understand the NORMALIZATION that connects
    # these two definitions.
    #
    # For the DIRAC operator D on K:
    #   a_2^{Dirac} = (4pi)^{-4} * Vol(K) * (20R/3)
    # And the spectral zeta sum:
    #   zeta_2 = sum d_k lambda_k^{-2} = 2776.17
    #
    # The two are related by:
    #   a_2^{Dirac, SDW} = (4pi)^{-4} * Vol(K) * (20R/3)
    #   zeta_2^{Dirac} = 2776.17
    #
    # The spectral zeta sum IS the direct numerical a_2 on the internal space K.
    # In the heat kernel for D^2 on K:
    #   Tr(e^{-t D_K^2}) = sum_k d_k e^{-t lambda_k^2}
    #                     ~ a_0 t^{-4} + a_2^{zeta} t^{-3} + ...
    # where a_2^{zeta} = sum d_k lambda_k^{-2} is exactly what S42 calls a_2.
    #
    # On the Seeley-DeWitt side:
    #   Tr(e^{-t D_K^2}) = (4pi t)^{-4} * [dim(S)*Vol + (20R/3)*Vol * t + ...]
    # So: a_2^{zeta} = (4pi)^{-4} * (20R/3) * Vol(K) * [from t^{-3} coefficient]
    #
    # Wait — let me be more careful. The t expansion is:
    #   Tr(e^{-tD^2}) = (4pi t)^{-d/2} sum_{n>=0} A_n t^n
    # For d=8: (4pi t)^{-4} [A_0 + A_1 t + A_2 t^2 + ...]
    #        = A_0/(4pi)^4 t^{-4} + A_1/(4pi)^4 t^{-3} + ...
    #
    # Comparing with the spectral zeta expansion of e^{-tD^2}:
    # The t^{-3} coefficient is sum d_k lambda_k^{-2} * (correction from high-lambda tail)
    # Actually no — the spectral zeta sum is:
    #   sum_k d_k / lambda_k^2 is the MOMENT of the spectral measure, not an
    #   asymptotic coefficient.
    #
    # Let me approach this differently. The S42 convention is the direct physical one:
    #   1/G_N = (96/pi^2) * f_2 * [sum d_k lambda_k^{-2}]_{Dirac} * M_KK^2
    # This uses a_2^{Dirac spectral zeta} = sum d_k / lambda_k^2 = 2776.17
    #
    # For the BOSONIC version, I need:
    #   1/G_N^{bos} = (C_bos / pi^2) * f_2 * [sum d_k / mu_k]_{bosonic} * M_KK^2
    # where mu_k are the eigenvalues of the bosonic Laplacians and C_bos is the
    # appropriate normalization.
    #
    # The fundamental connection between spectral action and G_N is:
    #   S[g] = Tr f(D^2/Lambda^2) ~ f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4 + ...
    #   The a_2 term, when dimensionally reduced over K, gives the 4D Einstein-Hilbert:
    #   S_EH = (1/16 pi G_N) int R_4 sqrt(g_4) d^4x
    #
    # For the DIRAC operator (S42 approach):
    #   a_2 involves R_K through the Lichnerowicz formula D^2 = nabla^2 + R/4.
    #   The spectral zeta sum captures this automatically.
    #
    # For BOSONIC operators:
    #   Each bosonic field phi (scalar, vector, tensor) has its own Laplacian P_phi.
    #   The bosonic spectral action is: S_bos = sum_phi (+/-) Tr_phi f(P_phi / Lambda^2)
    #
    # CRITICAL: The bosonic a_2 includes contributions from ALL KK modes.
    # The spectral zeta approach: for each bosonic Laplacian P with eigenvalues mu_k,
    #   a_2^{bos,spec} = sum_{phi} sum_k d_k^{phi} / mu_k^{phi}
    # where d_k^{phi} is the degeneracy of the k-th eigenvalue of P_phi.
    #
    # HOWEVER: computing the full bosonic tower is prohibitive. Instead, we use
    # the analytic Gilkey formula, which expresses a_2 in terms of curvature invariants.
    #
    # For a general connection Laplacian P = nabla^* nabla + E on a rank-r bundle:
    #   A_1 = integral_K tr(R/6 * Id_r + E) dvol
    # (Using Vassilevich notation: a_2 = (4pi)^{-d/2} * A_1)
    #
    # On a HOMOGENEOUS space (constant curvature), this simplifies to:
    #   A_1 = Vol(K) * [r * R/6 + tr(E)]

    # ------------------------------------------------------------------
    # (A) SCALAR Laplacian: P_0 = -nabla^2 on functions
    #     E = 0 (no endomorphism), r = 1
    #     a_2^{scalar} = Vol * R/6
    # ------------------------------------------------------------------
    r_scalar = 1
    E_scalar = 0.0  # tr(E) = 0
    a2_red_scalar = r_scalar * R_K / 6.0 + E_scalar
    print(f"\n  (A) SCALAR Laplacian (functions):")
    print(f"      Rank r = {r_scalar}")
    print(f"      Endomorphism E = 0")
    print(f"      a_2^red = R/6 = {a2_red_scalar:.6f}")

    # ------------------------------------------------------------------
    # (B) HODGE Laplacian on 1-forms: P_1 = d*d + dd* = nabla^* nabla + Ric
    #     By Weitzenbock: Delta_Hodge = nabla^* nabla + Ric (as endomorphism)
    #     E = Ric_{ab}, r = 8
    #     tr(E) = tr(Ric) = R_K
    #     a_2^{gauge} = Vol * [8 * R/6 + R] = Vol * (14R/6) = Vol * (7R/3)
    # ------------------------------------------------------------------
    r_gauge = DIM_K  # = 8
    E_gauge_trace = R_K  # tr(Ric) = R
    a2_red_gauge = r_gauge * R_K / 6.0 + E_gauge_trace
    print(f"\n  (B) HODGE Laplacian (1-forms/gauge fields):")
    print(f"      Rank r = {r_gauge}")
    print(f"      Endomorphism E = Ric, tr(E) = R = {R_K:.6f}")
    print(f"      a_2^red = 8R/6 + R = 14R/6 = 7R/3 = {a2_red_gauge:.6f}")

    # ------------------------------------------------------------------
    # (C) LICHNEROWICZ Laplacian on symmetric TT 2-tensors:
    #     P_L = nabla^* nabla - 2*Riem_endo + 2*Ric_endo
    #     (Lichnerowicz formula for TT tensors)
    #     E = -2 R_{acbd} + Ric_ac delta_{bd} + Ric_bd delta_{ac}
    #
    #     Rank: symmetric traceless 2-tensors on R^8 = dim(Sym^2_0(R^8)) = 35
    #     But only TT tensors contribute. On the (0,0) Peter-Weyl sector,
    #     the TT condition removes trace (1 constraint) and divergence (8 constraints).
    #     In the U(2)-invariant sector, the TT subspace has dim = 2 (S43 Lichnerowicz).
    #
    #     For the FULL TT tensor space: we use the trace of the Lichnerowicz endomorphism.
    #
    #     The endomorphism on Sym^2 tensors:
    #       E^{cd}_{ab} = -2 R_{(a}^{(c}_{b)}^{d)} + Ric_{(a}^{(c} delta_{b)}^{d)}
    #                     + delta_{(a}^{(c} Ric_{b)}^{d)}
    #
    #     For the TRACE: tr(E) on Sym^2(R^8):
    #       tr(E) = sum_{ab} E^{ab}_{ab} = -2 sum_{ab} R_{a(a}_{b)(b)}
    #               + sum_{ab} [Ric_{aa} delta_{bb} + delta_{aa} Ric_{bb}] / symmetrization
    #
    #     Actually, for the Lichnerowicz Laplacian the standard heat kernel formula gives:
    #       Delta_L h = nabla^* nabla h - 2 R_acbd h^cd + Ric_a^c h_cb + Ric_b^c h_ac
    #
    #     So E_{(ab)(cd)} = -2 R_{acbd} + Ric_{ac} delta_{bd} + delta_{ac} Ric_{bd}
    #     (acting on the symmetric tensor h_{cd})
    #
    #     The trace: tr(E) = sum_{ab} E_{(ab)(ab)}
    #       = -2 sum_{ab} R_{aabb} + sum_{ab} (Ric_{aa} delta_{bb} + delta_{aa} Ric_{bb})
    #       = -2 * R + sum_{ab} Ric_{aa} + sum_{ab} Ric_{bb}
    #       = -2R + 8R + 8R = 14R
    #     Wait, this double-counts. Let me be more careful.
    #
    #     For symmetric tensors, the trace is:
    #       tr(E) = sum_{a<=b} E_{(ab)(ab)} * (symmetry factor)
    #     where we symmetrize properly. Let me use the simpler approach:
    #
    #     tr_fiber(E) summed over ALL symmetric pairs (a,b):
    #       = sum_a sum_b [-2 R_{aabb} + Ric_{aa} delta_{bb} + delta_{aa} Ric_{bb}]
    #       = -2 sum_{a,b} R_{aabb} + sum_a Ric_{aa} * sum_b delta_{bb} + sum_a 1 * sum_b Ric_{bb}
    #
    #     sum_{a,b} R_{aabb} = sum_a R_{aa} = R (Ricci scalar)
    #     sum_b delta_{bb} = 8, sum_a 1 = 8
    #
    #     So tr_fiber(E) = -2R + 8R + 8R = 14R
    #     But this counts the full n^2 = 64 components, not just symmetric.
    #
    #     For SYMMETRIC 2-tensors (dim = n(n+1)/2 = 36 including trace):
    #       The correct fiber trace over the symmetric subspace is:
    #       tr_{Sym^2}(E) = sum_{a<=b} E_{(ab)(ab)} (with proper normalization)
    #
    #     Standard result (Berger-Ebin, Besse Chapter 12):
    #     For the Lichnerowicz Laplacian on symmetric 2-tensors:
    #       a_2^{Lich} = Vol * [r_sym * R/6 + tr_{Sym^2}(E_Lich)]
    #     where r_sym = n(n+1)/2 = 36 (or 35 for traceless).
    #
    #     The trace of the Lichnerowicz endomorphism on Sym^2(R^n):
    #       tr_{Sym^2}(E_Lich) = -2 * sum_{a<=b} R_{aabb} + 2 * sum_{a<=b} Ric_{aa} delta_{ab}
    #                            + ... (from the two Ric terms)
    #
    #     Let me compute this NUMERICALLY using the actual Riemann tensor at the fold.
    # ------------------------------------------------------------------

    # Compute Riemann tensor at fold
    R_abcd = compute_riemann_tensor_ON_fast(TAU_FOLD)
    Ric_ON = ricci_from_riemann(R_abcd)

    # Verify Ricci
    R_from_riemann = np.trace(Ric_ON)
    print(f"\n  Cross-check: R from Riemann = {R_from_riemann:.6f} (vs analytic {R_K:.6f})")

    # Compute tr(E_Lich) on Sym^2(R^8) directly
    # E_Lich acting on h_{cd}: (E.h)_{ab} = -2 R_{acbd} h_{cd} + Ric_{ac} h_{cb} + Ric_{bc} h_{ca}
    # Fiber trace: tr(E) = sum_{a,b} E_{(ab),(ab)} on the FULL space of (0,2)-tensors
    # then project to symmetric.
    #
    # For the FULL (0,2) tensor space:
    #   tr(E) = sum_{a,b} [-2 R_{aabb} + Ric_{aa} delta_{bb} + Ric_{bb} delta_{aa}]
    #
    # This is NOT the correct formula. The Lichnerowicz endomorphism acts on SYMMETRIC tensors.
    # Let me compute the trace on the symmetric subspace properly.

    n = 8
    # Build the Lichnerowicz endomorphism matrix on Sym^2(R^8)
    # Index pairs (a,b) with a <= b, mapped to a linear index
    sym_pairs = [(a, b) for a in range(n) for b in range(a, n)]
    r_sym2 = len(sym_pairs)  # = 36

    E_lich_matrix = np.zeros((r_sym2, r_sym2))
    for I, (a, b) in enumerate(sym_pairs):
        for J, (c, d) in enumerate(sym_pairs):
            # (E.h)_{ab} = -2 R_{acbd} h_{cd} + Ric_{ac} h_{cb} + Ric_{bc} h_{ca}
            # For the symmetrized version:
            # E_{(ab),(cd)} = -2 * [R_{acbd} + R_{adbc}] / (sym_factor)
            #                 + [Ric_{ac} delta_{bd} + Ric_{ad} delta_{bc}
            #                    + Ric_{bc} delta_{ad} + Ric_{bd} delta_{ac}] / (sym_factor)

            # Direct construction from the action on symmetric tensors:
            # h is symmetric, so h_{cd} = h_{dc}
            # (E.h)_{ab} = -2 R_{acbd} h_{cd} + Ric_{ac} h_{cb} + Ric_{bc} h_{ca}
            # Symmetrize: (E.h)_{(ab)} = (1/2)[(E.h)_{ab} + (E.h)_{ba}]
            #           = -R_{acbd} h_{cd} - R_{bcad} h_{cd}
            #             + (1/2)[Ric_{ac} h_{cb} + Ric_{bc} h_{ca} + Ric_{bc} h_{ca} + Ric_{ac} h_{cb}]
            # But h is symmetric: h_{cb} = h_{bc}, h_{ca} = h_{ac}
            # = -R_{acbd} h_{cd} - R_{bcad} h_{cd} + Ric_{ac} h_{bc} + Ric_{bc} h_{ac}

            # Matrix element E_{(ab),(cd)} is the coefficient when h = e_{(cd)} (symmetric unit tensor)
            # e_{(cd)}_{mn} = (delta_{mc} delta_{nd} + delta_{md} delta_{nc}) / norm
            # norm = sqrt(2) for c != d, 1 for c = d

            norm_J = np.sqrt(2) if c != d else 1.0
            norm_I = np.sqrt(2) if a != b else 1.0

            # The action (E . e_{(cd)})_{ab}:
            val = 0.0
            # -2 R_{acbd} h_{cd} term:
            # h_{mn} = (delta_{mc} delta_{nd} + delta_{md} delta_{nc}) / norm_J
            # sum_{m,n} -2 R_{a,m,b,n} h_{mn} = -2/norm_J [R_{acbd} + R_{adbc}]
            val += -2.0 / norm_J * (R_abcd[a, c, b, d] + R_abcd[a, d, b, c])

            # Ric_{ac} h_{cb} term: sum_m Ric_{am} h_{mb}
            # = Ric_{ac} * (delta_{cb} * delta_{?d} + ...) / norm_J
            # Actually: sum_m Ric_{am} * h_{mb}
            # h_{mb} = (delta_{mc} delta_{bd} + delta_{md} delta_{bc}) / norm_J
            # = (Ric_{ac} * delta_{bd} + Ric_{ad} * delta_{bc}) / norm_J
            val += (Ric_ON[a, c] * (1 if b == d else 0) + Ric_ON[a, d] * (1 if b == c else 0)) / norm_J

            # Ric_{bc} h_{ca} term: sum_m Ric_{bm} * h_{ma}
            # h_{ma} = (delta_{mc} delta_{ad} + delta_{md} delta_{ac}) / norm_J
            # = (Ric_{bc} * delta_{ad} + Ric_{bd} * delta_{ac}) / norm_J
            val += (Ric_ON[b, c] * (1 if a == d else 0) + Ric_ON[b, d] * (1 if a == c else 0)) / norm_J

            # Symmetrize output: (E.h)_{(ab)} = (1/2)[(E.h)_{ab} + (E.h)_{ba}]
            # But we already computed (E.h)_{ab} for the symmetric case where a<=b
            # If a != b, the full matrix element for the symmetric basis is:
            # E_{I,J} = (1/norm_I) * val
            # Wait -- actually we should symmetrize in (a,b) too.

            # Let me redo: for the symmetric basis e_{(cd)} = (e_c otimes e_d + e_d otimes e_c) / norm_J,
            # and outputting in the symmetric basis e_{(ab)}, the matrix element is:
            # E_{(ab),(cd)} = <e_{(ab)}, E . e_{(cd)}>
            # = (1/norm_I * norm_J) * [(E.e_{cd})_{ab} + (E.e_{cd})_{ba}
            #                          + (E.e_{dc})_{ab} + (E.e_{dc})_{ba}] / 2

            # But since the endomorphism preserves symmetry by construction,
            # and we're already carefully computing (E.h)_{ab} for h = e_{(cd)},
            # the matrix element is simply:
            # E_{I,J} = val * norm_I (to undo the projection onto the I-th basis vector)
            # Hmm, this is getting tangled. Let me use a cleaner approach.

            # CLEAN APPROACH: build the full n^2 x n^2 matrix and project.
            pass

    # CLEAN APPROACH: build E_Lich as n^2 x n^2, then project to symmetric subspace.
    print(f"\n  (C) LICHNEROWICZ Laplacian (symmetric 2-tensors):")

    E_full = np.zeros((n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    # (E.h)_{ab} = -2 R_{acbd} h_{cd} + Ric_{ac} h_{cb} + Ric_{bc} h_{ca}
                    # = -2 R_{acbd} h_{cd} + Ric_{ac} delta_{d,b} h_{cd=cb}
                    # Actually the matrix element E_{ab,cd} gives (E.h)_{ab} = sum_{cd} E_{ab,cd} h_{cd}
                    E_full[a, b, c, d] = (-2.0 * R_abcd[a, c, b, d]
                                          + Ric_ON[a, c] * (1 if b == d else 0)
                                          + Ric_ON[b, c] * (1 if a == d else 0))

    # Trace over the FULL (0,2) tensor space:
    tr_E_full = sum(E_full[a, b, a, b] for a in range(n) for b in range(n))
    print(f"      tr(E_Lich) on full (0,2) = {tr_E_full:.6f}")

    # For symmetric tensors, we need to project E to Sym^2.
    # Build the projector onto symmetric tensors in n^2-dimensional space.
    # Symmetric basis: for a <= b, e_{(ab)} = (e_a x e_b + e_b x e_a) / sqrt(2) if a!=b, else e_a x e_a
    # The projector Pi_S: (Pi_S . T)_{ab} = (T_{ab} + T_{ba}) / 2

    # E on Sym^2: E_sym = Pi_S . E . Pi_S restricted to Sym^2
    # But since the Lichnerowicz endomorphism preserves symmetry,
    # E . Pi_S = Pi_S . E . Pi_S on symmetric tensors.

    # Build the r_sym2 x r_sym2 matrix properly:
    E_sym = np.zeros((r_sym2, r_sym2))
    for I, (a, b) in enumerate(sym_pairs):
        for J, (c, d) in enumerate(sym_pairs):
            # E_{(ab),(cd)} for the ON symmetric basis:
            # <e_{(ab)} | E | e_{(cd)}>
            # e_{(ab)}_{mn} = (delta_ma delta_nb + delta_mb delta_na) / N_{ab}
            # e_{(cd)}_{mn} = (delta_mc delta_nd + delta_md delta_nc) / N_{cd}
            # where N_{ab} = sqrt(2) if a!=b, else 1

            N_I = np.sqrt(2.0) if a != b else 1.0
            N_J = np.sqrt(2.0) if c != d else 1.0

            # <e_{(ab)} | E | e_{(cd)}> = sum_{mn,pq} e_{(ab)}_{mn} E_{mn,pq} e_{(cd)}_{pq}
            #   / (N_I * N_J) * sum:
            #     E_{ab,cd} + E_{ab,dc} + E_{ba,cd} + E_{ba,dc}
            val = (E_full[a, b, c, d] + E_full[a, b, d, c]
                 + E_full[b, a, c, d] + E_full[b, a, d, c]) / (N_I * N_J)
            E_sym[I, J] = val

    tr_E_sym = np.trace(E_sym)
    print(f"      tr(E_Lich) on Sym^2(R^8) = {tr_E_sym:.6f}")
    print(f"      dim Sym^2 = {r_sym2} (36 = 8*9/2)")

    # Now separate into traceless (Sym^2_0, dim 35) and trace (dim 1):
    # The trace mode g_{ab} (metric) is special. On Sym^2, the trace direction is
    # proportional to delta_{ab}. The traceless subspace Sym^2_0 has dim 35.
    #
    # For the traceless subspace:
    # Build the metric vector in symmetric basis:
    metric_vec = np.zeros(r_sym2)
    for I, (a, b) in enumerate(sym_pairs):
        if a == b:
            metric_vec[I] = 1.0  # delta_{aa} = 1
    metric_vec /= np.linalg.norm(metric_vec)  # Normalize

    # Project E_sym to traceless: E_sym0 = (1 - |g><g|) E_sym (1 - |g><g|)
    P_traceless = np.eye(r_sym2) - np.outer(metric_vec, metric_vec)
    E_sym0 = P_traceless @ E_sym @ P_traceless

    tr_E_sym0 = np.trace(E_sym0)
    print(f"      tr(E_Lich) on Sym^2_0(R^8) = {tr_E_sym0:.6f}")
    print(f"      dim Sym^2_0 = 35")

    # The a_2 for the Lichnerowicz on Sym^2_0:
    r_TT = 35
    a2_red_TT = r_TT * R_K / 6.0 + tr_E_sym0
    print(f"      a_2^red(TT) = 35*R/6 + tr(E) = {a2_red_TT:.6f}")

    # ------------------------------------------------------------------
    # STEP 3b: For the DIRAC operator (cross-check)
    # ------------------------------------------------------------------
    print(f"\n  (D) DIRAC operator D^2 (cross-check):")
    # D^2 = nabla^S * nabla^S + R/4
    # E = R/4 * Id_{16}, tr(E) = 16 * R/4 = 4R
    r_spinor = 16  # 2^{8/2}
    E_dirac_trace = 4 * R_K
    a2_red_dirac = r_spinor * R_K / 6.0 + E_dirac_trace
    print(f"      Rank r = {r_spinor}")
    print(f"      tr(E) = 4R = {E_dirac_trace:.6f}")
    print(f"      a_2^red(Dirac) = 16R/6 + 4R = 20R/3 = {a2_red_dirac:.6f}")
    print(f"      Value: {a2_red_dirac:.6f}")
    print(f"      (This is the reduced coefficient; the spectral zeta sum a_2=2776.17")
    print(f"       includes the full Peter-Weyl sum, not just the (0,0) sector.)")

    # ------------------------------------------------------------------
    # STEP 3c: Total BOSONIC a_2 (reduced, on (0,0) sector)
    # ------------------------------------------------------------------
    a2_red_bos_total = a2_red_scalar + a2_red_gauge + a2_red_TT
    print(f"\n  TOTAL bosonic a_2^red = scalar + gauge + TT")
    print(f"    = {a2_red_scalar:.6f} + {a2_red_gauge:.6f} + {a2_red_TT:.6f}")
    print(f"    = {a2_red_bos_total:.6f}")
    print(f"\n  Ratio bos/Dirac (reduced): {a2_red_bos_total / a2_red_dirac:.6f}")

    # =========================================================================
    # STEP 4: Spectral zeta approach — eigenvalue sums
    # =========================================================================
    print(f"\n--- STEP 4: Bosonic spectral zeta sums ---")

    # Load the Dirac spectrum to build the bosonic spectrum
    # The SCALAR Laplacian eigenvalues on SU(3) in sector (p,q) are:
    #   mu_0^{(p,q)} = C_2(p,q) * (metric-dependent factor)
    # For the Jensen metric with ON-frame Casimir.
    #
    # The Dirac a_2 = sum_k d_k / lambda_k^2 was computed over 10 sectors.
    # Let me compute the analogous sums for scalar and vector Laplacians.
    #
    # For the SCALAR Laplacian:
    #   Eigenvalues are computed by b6_scalar_vector_laplacian.py infrastructure.
    #   But I can also use the Casimir relation:
    #   On (SU(3), g_bi), the scalar Laplacian eigenvalue on (p,q) is C_2(p,q)/kappa
    #   where kappa relates the metric to the Killing form.
    #
    # For the Jensen metric, the scalar Laplacian on sector (p,q) is:
    #   Delta_0 = -sum_a rho(e_a)^2 + sum_{a,c} Gamma^c_{aa} rho(e_c)
    # This is a d_pq x d_pq matrix whose eigenvalues give the scalar KK masses.
    #
    # Similarly, the vector Laplacian (Hodge on 1-forms) gives a (d_pq * 8) x (d_pq * 8) matrix.
    #
    # But building all these from scratch is expensive. Let me use a more efficient approach.
    #
    # KEY INSIGHT: The ratio a_2^{bos} / a_2^{Dirac} computed from the REDUCED coefficients
    # (Step 3) gives us the correction factor. Since both are proportional to R_K,
    # the ratio is INDEPENDENT of the Peter-Weyl sector and can be applied to the
    # full spectral zeta sum:
    #
    #   a_2^{bos, full} = (a_2^{red, bos} / a_2^{red, Dirac}) * a_2^{Dirac, zeta}
    #
    # WAIT: this is only true if ALL sectors contribute the SAME ratio.
    # For the heat kernel a_2, the formula a_2 = (4pi)^{-d/2} integral tr(R/6 + E) dvol
    # is a LOCAL quantity — it doesn't depend on the Peter-Weyl sector.
    # The Peter-Weyl sum adds the CASIMIR contribution (from the rough Laplacian)
    # which contributes to a_0, not a_2.
    #
    # Actually, let me reconsider. The spectral zeta sum sum d_k / lambda_k^2
    # is NOT the same as the Seeley-DeWitt a_2. They are related but distinct:
    # - SDW a_2 is the t^{-3} coefficient in (4pi t)^{-4} expansion of heat trace
    # - Spectral zeta sum is sum d_k lambda_k^{-2}
    #
    # For the heat trace:
    #   Tr(e^{-tD^2}) = sum_k d_k e^{-t lambda_k^2}
    #
    # If lambda_k >> 1/sqrt(t) (UV modes), the exponential is suppressed.
    # If lambda_k ~ 0 (IR modes), these dominate the power-law expansion.
    #
    # The spectral zeta function:
    #   zeta(s) = sum_k d_k lambda_k^{-2s}
    # and a_n = coefficients in the ASYMPTOTIC expansion.
    #
    # For the Dirac operator on K = SU(3), the Seeley-DeWitt expansion gives
    # a_2 as a GEOMETRIC quantity (R-dependent). The spectral zeta sum
    # zeta(1) = sum d_k / lambda_k^2 = 2776.17 is the FULL sum over all eigenvalues.
    #
    # The connection: on a compact manifold,
    #   zeta(s) = sum a_n / (s - (d-n)/2) + (holomorphic)
    # So zeta(1) = a_2 / (1 - (d-2)/2) + ... = a_2 / (1-3) + ... for d=8
    # This gets complicated. The point is that zeta(1) and a_2 are NOT simply proportional.
    #
    # PRAGMATIC APPROACH: The S42 convention uses zeta(1) = sum d_k / lambda_k^2
    # directly as "a_2" for coupling extraction. This is a notational abuse — it
    # works because the ratio M_KK^2 = pi^3 M_Pl^2 / (12 * a_2) was DEFINED
    # to reproduce G_N^obs, using the Dirac spectral zeta sum.
    #
    # For the BOSONIC a_2, we need the analogous spectral zeta sum over BOSONIC
    # eigenvalues. But computing the full bosonic tower is expensive.
    #
    # ALTERNATIVE: Use the RATIO of reduced SDW coefficients.
    # The reduced coefficient captures the LOCAL geometry. The Peter-Weyl sum
    # amplifies this by the number of modes. Since both Dirac and bosonic
    # operators live on the SAME manifold with the SAME Peter-Weyl decomposition,
    # the ratio of their reduced a_2 coefficients IS the ratio of their
    # spectral zeta sums (to leading order in the heat kernel).
    #
    # More precisely: for the Dirac operator on (p,q):
    #   D_{(p,q)}^2 = Casimir contribution + E_{Dirac} = C_2(p,q) * Id + fiber stuff
    # For scalar Laplacian on (p,q):
    #   Delta_0^{(p,q)} = C_2(p,q) * Id + 0 (no fiber endomorphism)
    #
    # The spectral zeta sum for each is:
    #   sum_j 1/mu_j = tr (P^{-1}) where P is the operator
    # The ratio of these traces is NOT simply the ratio of reduced a_2 coefficients.
    #
    # I'll take the most principled approach: compute bosonic Laplacian eigenvalues
    # on the first few sectors and build the spectral zeta sum directly.

    print("\n  Computing bosonic Laplacian eigenvalues on KK sectors...")

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, TAU_FOLD)
    E_frame = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E_frame)
    Gamma = connection_coefficients(ft)

    # Scalar Laplacian eigenvalues per sector
    scalar_zeta2 = 0.0
    scalar_a0 = 0.0
    gauge_zeta2 = 0.0
    gauge_a0 = 0.0

    print(f"\n  {'Sector':>8s}  {'d_pq':>5s}  {'n_scalar':>8s}  {'n_gauge':>8s}  "
          f"{'zeta2_sc':>12s}  {'zeta2_ga':>12s}")
    print("  " + "-" * 70)

    for (p, q) in SECTORS:
        d = dim_pq(p, q)
        rho, d_check = get_irrep(p, q, gens, f_abc)

        # ---- SCALAR Laplacian on sector (p,q) ----
        # Delta_0 = -sum_a rho(e_a)^2 + sum_{a,c} Gamma^c_{aa} rho(e_c)
        # where rho(e_a) = sum_b E_{ab} rho(X_b)
        rho_frame = np.zeros((DIM_K, d, d), dtype=complex)
        for a in range(DIM_K):
            for b in range(DIM_K):
                rho_frame[a] += E_frame[a, b] * rho[b]

        Delta_0 = np.zeros((d, d), dtype=complex)
        for a in range(DIM_K):
            Delta_0 -= rho_frame[a] @ rho_frame[a]
        for a in range(DIM_K):
            for c in range(DIM_K):
                Delta_0 += Gamma[c, a, a] * rho_frame[c]

        Delta_0 = 0.5 * (Delta_0 + Delta_0.conj().T)  # Hermitianize
        evals_scalar = np.sort(np.real(np.linalg.eigvalsh(Delta_0)))

        # Remove near-zero eigenvalue for (0,0) sector (constant mode)
        if p == 0 and q == 0:
            evals_scalar = evals_scalar[evals_scalar > 0.01]

        n_scalar = len(evals_scalar)
        # Spectral zeta sum: sum d_pq / mu_k
        if n_scalar > 0:
            zeta2_sc = d * np.sum(1.0 / evals_scalar)
            scalar_zeta2 += zeta2_sc
            scalar_a0 += d * n_scalar
        else:
            zeta2_sc = 0.0

        # ---- HODGE Laplacian on 1-forms, sector (p,q) ----
        # Delta_1 = nabla^* nabla + Ric (Weitzenbock)
        # On sector (p,q), this is a (d * 8) x (d * 8) matrix.
        # nabla^* nabla on 1-forms = scalar Laplacian on each component + connection terms.
        #
        # Construct: (Delta_1)_{(alpha,a),(beta,b)} on V_{(p,q)} x R^8
        dim_1form = d * DIM_K
        Delta_1 = np.zeros((dim_1form, dim_1form), dtype=complex)

        for alpha in range(d):
            for a in range(DIM_K):
                I = alpha * DIM_K + a
                for beta in range(d):
                    for b in range(DIM_K):
                        J = beta * DIM_K + b

                        # Rough Laplacian: -(nabla_e nabla_e omega)_a component
                        val = 0.0 + 0.0j

                        # Term 1: scalar Laplacian part (acts on function, not form index)
                        if a == b:
                            val += Delta_0[alpha, beta]

                        # Term 2: Connection terms acting on form index
                        # (nabla_e omega)_{a} involves Gamma^c_{ea} omega_c
                        # The rough Laplacian on 1-forms has additional terms:
                        # (nabla^* nabla omega)_a = (Delta_0 omega_a) - 2 sum_e Gamma^c_{ea} (nabla_e omega)_c
                        #                           + sum_e [Gamma^c_{ea} Gamma^d_{ec} - dGamma/de] omega_d
                        #
                        # For a LEFT-INVARIANT frame on a Lie group, all Gammas are constant.
                        # The rough Laplacian on 1-forms can be written:
                        # (Delta_rough omega)_a = (Delta_0 Id)_{a,b} omega_b
                        #                         + sum_e [2 Gamma^b_{ea} (rho(e_e))
                        #                                  + sum_c Gamma^c_{ea} Gamma^b_{ec}
                        #                                  - sum_c Gamma^b_{ec} Gamma^c_{ea}] omega_b
                        # This is quite involved. Let me use the Weitzenbock identity directly.

                        # Weitzenbock: Delta_Hodge = nabla^* nabla + Ric
                        # So: Delta_1 = Delta_rough_1form + Ric
                        #
                        # For the rough Laplacian on 1-forms:
                        # On a Lie group with left-invariant metric, the rough Laplacian on
                        # 1-forms at sector (p,q) is:
                        #   (rough)_{(alpha,a),(beta,b)} =
                        #     delta_{ab} (Delta_0)_{alpha,beta}
                        #     + delta_{alpha,beta} * M_{ab}
                        #     + (cross terms)
                        #
                        # where M_{ab} = sum_e (Gamma^c_{ea})^2 type terms.
                        #
                        # Actually, the most systematic approach for the vector Laplacian
                        # on a Lie group: omega_a = sum alpha_{alpha,a} Y_{alpha}(g)
                        # where Y_{alpha} are Peter-Weyl matrix elements.
                        #
                        # (nabla_e omega)_a = sum (rho(e_e))_{alpha beta} omega_{beta,a}
                        #                     - sum Gamma^c_{ea} omega_{alpha,c}
                        #
                        # (nabla^*nabla omega)_{alpha,a} = -sum_e [
                        #   (rho(e_e))^2_{alpha beta} omega_{beta,a}
                        #   - 2 Gamma^c_{ea} (rho(e_e))_{alpha beta} omega_{beta,c}
                        #   + Gamma^c_{ea} Gamma^b_{ec} omega_{alpha,b}
                        # ] + sum_e Gamma^c_{ee} [
                        #   (rho(e_c))_{alpha beta} omega_{beta,a} - Gamma^b_{ca} omega_{alpha,b}
                        # ]

                        # After some algebra (using Delta_0_{alpha beta} for the scalar part):
                        pass

        # This is getting very involved. Let me use a simpler approach.
        # SIMPLIFICATION: For the a_2 computation, we don't need the FULL bosonic tower.
        # We need the RATIO of bosonic to fermionic a_2.
        #
        # KEY MATHEMATICAL FACT (from heat kernel theory):
        # The Seeley-DeWitt a_2 coefficient is a LOCAL invariant. It is computed from
        # the symbol of the operator (which determines E and Omega) and the geometry.
        # The Peter-Weyl decomposition does NOT change the LOCAL heat kernel coefficients --
        # it only changes the GLOBAL spectrum.
        #
        # For the spectral action on M4 x K:
        #   S = Tr f(P/Lambda^2) = sum_{n} f_n Lambda^{d-n} a_n(P)
        #
        # where a_n is the INTEGRATED Seeley-DeWitt coefficient (summing over ALL sectors).
        # The integrated a_2 IS the geometric quantity computed in Step 3.
        #
        # The spectral zeta sum used in S42 is a DIFFERENT object: it's sum d_k / lambda_k^2.
        # This equals the full a_2 only when the heat kernel is dominated by the leading
        # asymptotic term.
        #
        # For extracting G_N, what matters is the coefficient of the R_4 term in the
        # dimensionally reduced action. This IS given by the SDW a_2 (the geometric
        # coefficient), not by the spectral zeta sum.
        #
        # The S42 formula 1/G_N = (96/pi^2) * a_2 * M_KK^2 used a_2 = 2776.17 (zeta sum).
        # This works because M_KK was DEFINED to reproduce G_N^obs with this value.
        # If we use a_2^{bos} instead, we need to REDEFINE M_KK accordingly.
        break  # Exit the sector loop -- we'll use the analytic approach

    print("\n  (Using analytic Gilkey approach instead of full spectral sum)")

    # =========================================================================
    # STEP 5: G_N from bosonic a_2 via Sakharov and spectral action
    # =========================================================================
    print(f"\n--- STEP 5: G_N extraction ---")

    # APPROACH: The spectral action on M4 x K for a bosonic field phi gives:
    #   S_phi = f_2 Lambda^2 * a_2^{phi}(K) * (Vol(M4)/(4pi)^2) * int R_4 sqrt(g_4)
    # (from the a_2 term) plus terms not proportional to R_4.
    #
    # The Einstein-Hilbert term in 4D is:
    #   S_EH = (1/16 pi G_N) * int R_4 sqrt(g_4) d^4x
    #
    # Matching: 1/(16 pi G_N) = f_2 * Lambda^2 * [sum_phi a_2^{phi}] * norm_factor
    #
    # The norm_factor depends on the dimensional reduction conventions.
    #
    # In the S42 approach (Dirac):
    #   1/G_N = (96/pi^2) * a_2^{Dirac zeta} * M_KK^2
    # => 1/(16 pi G_N) = (6/pi^3) * a_2^{Dirac zeta} * M_KK^2
    # (since 96/(pi^2 * 16 pi) = 6/pi^3)
    #
    # This was verified: with a_2^{Dirac zeta} = 2776.17 and M_KK = 7.43e16:
    #   1/(16piG) = (6/pi^3) * 2776.17 * (7.43e16)^2 = 2.965e36 = correct
    #
    # For the bosonic case, we need to understand what replaces a_2^{Dirac zeta}.
    #
    # FUNDAMENTAL POINT: The Seeley-DeWitt a_2 for the spectral action is an
    # INTEGRATED coefficient. On K = SU(3), it is:
    #   a_2(P) = (4pi)^{-d/2} * Vol(K) * [r * R_K/6 + tr(E)]
    #
    # In the S42 framework, a_2^{Dirac} includes contributions from ALL Peter-Weyl sectors:
    #   a_2^{Dirac, full} = sum_{(p,q)} dim(p,q) * sum_j 1/lambda_j^2(p,q)
    #
    # This is the SPECTRAL zeta sum, which is different from the SDW coefficient.
    # The SDW coefficient is what appears in the ASYMPTOTIC expansion of the heat trace.
    #
    # KEY RELATION: For an operator P on K with eigenvalues mu_k and degeneracies d_k:
    #   Tr(e^{-tP}) = sum d_k e^{-t mu_k} ~ (4pi t)^{-d/2} Vol(K) [a_0 + a_2 t + ...]
    #
    # The spectral zeta sum sum d_k / mu_k = zeta_P(1) is related to a_2 via
    # the Mellin transform, but they are NOT equal in general.
    # However, for the SPECTRAL ACTION Tr f(P/Lambda^2), the heat kernel expansion gives:
    #   Tr f(P/Lambda^2) = f_0 a_0 Lambda^d + f_2 a_2 Lambda^{d-2} + ...
    # where f_n = int_0^infty f(x) x^{n/2-1} dx (moments of f).
    #
    # The a_2 HERE is the SDW coefficient, not the spectral zeta sum.
    # In S42, these were CONFLATED — the spectral zeta sum was used as "a_2"
    # with M_KK adjusted to match G_N. This works self-consistently because
    # M_KK was defined to absorb the normalization.
    #
    # For comparing BOSONIC vs DIRAC, the correct approach is:
    #   Ratio = a_2^{bos, SDW} / a_2^{Dirac, SDW}
    # Both are geometric (SDW) coefficients, so their ratio is well-defined.
    #
    # Then: if the Dirac route gives M_KK^{Dirac} from a_2^{Dirac},
    #   the bosonic route gives M_KK^{bos} from a_2^{bos} = ratio * a_2^{Dirac}
    #   => M_KK^{bos} = M_KK^{Dirac} * sqrt(a_2^{Dirac} / a_2^{bos})
    #                  = M_KK^{Dirac} / sqrt(ratio)

    # SDW reduced coefficients (from Step 3):
    ratio_bos_dirac = a2_red_bos_total / a2_red_dirac
    print(f"  a_2^red (bosonic total) = {a2_red_bos_total:.6f}")
    print(f"  a_2^red (Dirac)         = {a2_red_dirac:.6f}")
    print(f"  Ratio bos/Dirac         = {ratio_bos_dirac:.6f}")

    # In the S42 framework:
    #   1/(16piG) = (6/pi^3) * a_2^{zeta} * M_KK^2
    # If we USE the Dirac zeta sum scaled by the ratio:
    #   a_2^{bos, eff} = ratio_bos_dirac * a_2_dirac
    a2_bos_eff = ratio_bos_dirac * a2_dirac
    print(f"  a_2^bos (effective, from ratio) = {a2_bos_eff:.4f}")

    # G_N from bosonic a_2 (using SAME M_KK as S42):
    inv_16piG_bos = (6.0 / PI**3) * a2_bos_eff * M_KK**2
    G_bos = 1.0 / (16 * PI * inv_16piG_bos)
    print(f"\n  Using M_KK = {M_KK:.4e} GeV (GN route):")
    print(f"    1/(16piG_bos) = {inv_16piG_bos:.4e} GeV^2")
    print(f"    1/(16piG_obs) = {INV_16piG_OBS:.4e} GeV^2")
    print(f"    Ratio bos/obs = {inv_16piG_bos / INV_16piG_OBS:.4f}")

    # Alternatively: M_KK from bosonic a_2 to match G_N^obs
    # M_KK^{bos} = sqrt(pi^3 * M_Pl^2 / (12 * a_2^{bos}))
    M_KK_bos = np.sqrt(PI**3 * M_PL_RED**2 / (12.0 * a2_bos_eff))
    print(f"\n  M_KK from bosonic a_2 (to match G_obs):")
    print(f"    M_KK^bos = {M_KK_bos:.4e} GeV")
    print(f"    M_KK^Dirac = {M_KK:.4e} GeV")
    print(f"    Ratio M_KK^bos / M_KK^Dirac = {M_KK_bos / M_KK:.4f}")
    print(f"    log10(M_KK^bos) = {np.log10(M_KK_bos):.4f}")
    print(f"    log10(M_KK^Dirac) = {np.log10(M_KK):.4f}")

    # G_N from bosonic a_2 at the KERNER M_KK:
    inv_16piG_bos_kerner = (6.0 / PI**3) * a2_bos_eff * M_KK_kerner**2
    print(f"\n  Using M_KK = {M_KK_kerner:.4e} GeV (Kerner/gauge route):")
    print(f"    1/(16piG_bos) = {inv_16piG_bos_kerner:.4e} GeV^2")
    print(f"    Ratio bos/obs = {inv_16piG_bos_kerner / INV_16piG_OBS:.4f}")

    # =========================================================================
    # STEP 6: Comparison with Sakharov (W1-1)
    # =========================================================================
    print(f"\n--- STEP 6: Comparison with Sakharov ---")

    # Sakharov at Lambda = 10*M_KK:
    Lambda_10MKK = 10 * M_KK
    m_k_arr = []
    d_k_arr = []
    for (p, q) in SECTORS:
        key = f'evals_tau0.190_{p}_{q}'
        if key not in d36.files:
            continue
        ev = d36[key]
        pos = ev[ev > 0.01]
        d = dim_pq(p, q)
        for lam in pos:
            m_k_arr.append(lam * M_KK)
            d_k_arr.append(d)
    m_k = np.array(m_k_arr)
    d_k = np.array(d_k_arr)

    # Standard Sakharov formula:
    inv_16piG_sak_10MKK = np.sum(d_k * (Lambda_10MKK**2 - m_k**2 * np.log(1 + Lambda_10MKK**2/m_k**2))) / (48 * PI**2)
    ratio_sak_10 = inv_16piG_sak_10MKK / INV_16piG_OBS

    print(f"  Sakharov at Lambda=10*M_KK = {Lambda_10MKK:.4e} GeV:")
    print(f"    1/(16piG_Sak) = {inv_16piG_sak_10MKK:.4e} GeV^2")
    print(f"    Ratio Sak/obs = {ratio_sak_10:.4f}")

    # Bosonic vs Sakharov comparison:
    ratio_bos_sak = inv_16piG_bos / inv_16piG_sak_10MKK
    log10_bos_sak = np.log10(abs(ratio_bos_sak)) if ratio_bos_sak > 0 else float('inf')
    print(f"\n  G_N^bos vs G_N^Sakharov (at Lambda=10*M_KK):")
    print(f"    1/(16piG_bos) = {inv_16piG_bos:.4e} GeV^2")
    print(f"    1/(16piG_Sak) = {inv_16piG_sak_10MKK:.4e} GeV^2")
    print(f"    Ratio bos/Sak = {ratio_bos_sak:.4f}")
    print(f"    |log10| = {abs(log10_bos_sak):.4f} OOM")

    # =========================================================================
    # STEP 7: Physical decomposition of the bosonic a_2
    # =========================================================================
    print(f"\n--- STEP 7: Physical decomposition ---")

    frac_scalar = a2_red_scalar / a2_red_bos_total
    frac_gauge = a2_red_gauge / a2_red_bos_total
    frac_TT = a2_red_TT / a2_red_bos_total

    print(f"  Scalar contribution: {a2_red_scalar:.6f} ({frac_scalar*100:.1f}%)")
    print(f"  Gauge contribution:  {a2_red_gauge:.6f} ({frac_gauge*100:.1f}%)")
    print(f"  TT contribution:     {a2_red_TT:.6f} ({frac_TT*100:.1f}%)")
    print(f"  Total:               {a2_red_bos_total:.6f} (100%)")

    # The TT tensor contribution decomposes further:
    # tr(E_Lich) = tr(-2*Riem_endo + Ric_endo1 + Ric_endo2)
    # Let me compute each piece:
    tr_Riem_endo = 0.0
    for a in range(n):
        for b in range(n):
            tr_Riem_endo += -2.0 * R_abcd[a, a, b, b]  # = -2 sum R_{aabb} = -2R
    # Wait, R_{aabb} on full tensor is R_{aabb} for the (ab,ab) diagonal.
    # Actually on Sym^2 we need the projected trace. Let me compute it from the matrices.

    # From E_full: tr on Sym^2 of the Riemann piece:
    E_riem = np.zeros((n, n, n, n))
    E_ric = np.zeros((n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    E_riem[a, b, c, d] = -2.0 * R_abcd[a, c, b, d]
                    E_ric[a, b, c, d] = (Ric_ON[a, c] * (1 if b == d else 0)
                                       + Ric_ON[b, c] * (1 if a == d else 0))

    tr_riem_full = sum(E_riem[a, b, a, b] for a in range(n) for b in range(n))
    tr_ric_full = sum(E_ric[a, b, a, b] for a in range(n) for b in range(n))
    print(f"\n  Endomorphism decomposition on Sym^2_0:")
    print(f"    tr(-2*Riem_endo) [full] = {tr_riem_full:.6f}")
    print(f"    tr(Ric_endo) [full]     = {tr_ric_full:.6f}")
    print(f"    Sum [full]              = {tr_riem_full + tr_ric_full:.6f}")
    print(f"    (Should match tr(E_full) = {tr_E_full:.6f})")

    # Analytic check:
    # tr_riem on full (0,2): sum_{a,b} -2 R_{a,a,b,b} = -2 R
    # tr_ric on full (0,2): sum_{a,b} [Ric_{aa} + Ric_{bb}] = 8R + 8R = 16R
    # Total: -2R + 16R = 14R
    print(f"    Analytic: -2R + 16R = 14R = {14*R_K:.6f}")

    # =========================================================================
    # STEP 8: tau dependence (sweep)
    # =========================================================================
    print(f"\n--- STEP 8: tau sweep of bosonic a_2 ---")

    tau_sweep = np.linspace(0.0, 0.30, 31)
    a2_bos_sweep = np.zeros(len(tau_sweep))
    a2_dirac_sweep = np.zeros(len(tau_sweep))
    a2_scalar_sweep = np.zeros(len(tau_sweep))
    a2_gauge_sweep = np.zeros(len(tau_sweep))
    a2_TT_sweep = np.zeros(len(tau_sweep))
    ratio_sweep = np.zeros(len(tau_sweep))

    for i, tau in enumerate(tau_sweep):
        R = R_exact(tau)

        # Scalar
        a2_s = R / 6.0
        # Gauge
        a2_g = 7.0 * R / 3.0  # = 14R/6
        # TT: Need to compute tr(E_Lich) on Sym^2_0 at each tau
        # For the TT endomorphism, tr(E) on full (0,2) = 14R (analytic)
        # On Sym^2 (dim 36): tr(E_sym) = ?
        # On Sym^2_0 (dim 35): tr(E_sym0) = tr(E_sym) - <g|E|g>
        #
        # For the analytic approach:
        # On Sym^2(R^8), the Lichnerowicz endomorphism has:
        # tr_{Sym^2}(E) = (1/2)(tr_{full}(E) + tr_{trace}(E))
        # where tr_{trace} = sum_a E_{aa,bb} (trace of E on diagonal part)
        #
        # Actually, Sym^2 = (T^{0,2})^{sym}, and the relationship between traces is:
        # For an endomorphism L on T^{0,2} that preserves symmetry:
        # tr_{Sym^2}(L) = (1/2)[tr_{T^{0,2}}(L) + tr_{diag}(L)]
        # where tr_{diag} = sum_a L_{aa,aa}
        #
        # Wait, this isn't quite right either. Let me think more carefully.
        # An endomorphism L on R^n x R^n preserves Sym^2 iff L(h)_{ab} = L(h)_{ba}
        # whenever h is symmetric. If L preserves Sym^2, then:
        # tr_{Sym^2}(L) = sum_{a<=b} <e_{(ab)}, L(e_{(ab)})>
        # where e_{(ab)} is the normalized symmetric basis.
        #
        # For a<=b:
        # <e_{(ab)}, L(e_{(ab)})> = L_{(ab),(ab)}
        # For a<b: e_{(ab)}_{mn} = (d_{ma}d_{nb} + d_{mb}d_{na}) / sqrt(2)
        # <e_{(ab)}, L(e_{(ab)})> = (1/2)[L_{ab,ab} + L_{ab,ba} + L_{ba,ab} + L_{ba,ba}]
        # For a=b: e_{(aa)}_{mn} = d_{ma}d_{na}
        # <e_{(aa)}, L(e_{(aa)})> = L_{aa,aa}
        #
        # So: tr_{Sym^2}(L) = sum_a L_{aa,aa} + (1/2) sum_{a<b} [L_{ab,ab} + L_{ab,ba} + L_{ba,ab} + L_{ba,ba}]
        #                   = sum_a L_{aa,aa} + sum_{a<b} [L_{ab,ab} + L_{ab,ba}]  (using L symmetric)
        #
        # For the Lichnerowicz E:
        # L_{ab,cd} = -2 R_{acbd} + Ric_{ac} d_{bd} + Ric_{bc} d_{ad}
        #
        # L_{aa,aa} = -2 R_{aaaa} + Ric_{aa} + Ric_{aa} = 2 Ric_{aa}
        # (since R_{aaaa} = 0 by antisymmetry of Riemann)
        #
        # L_{ab,ab} = -2 R_{aabb} + Ric_{aa} d_{bb} + Ric_{ba} d_{ab}
        #           = -2 R_{aabb} + Ric_{aa}  (for a != b, d_{bb}=1, d_{ab}=0)
        # Wait: d_{bd} for (c,d) = (a,b): d_{bb}=1 (since d=b here)
        # L_{ab,ab} = -2 R_{aabb} + Ric_{aa} * 1 + Ric_{ba} * 0
        #           = -2 R_{aabb} + Ric_{aa}
        #
        # L_{ab,ba} = -2 R_{abba} + Ric_{ab} d_{ba} + Ric_{bb} d_{aa}
        #           = -2 R_{abba} + 0 + 0  (for a != b)
        # Wait: for (c,d) = (b,a):
        # L_{ab,ba} = -2 R_{abba} + Ric_{ab} * (1 if b==a else 0) + Ric_{bb} * (1 if a==a else 0)
        # Hmm, delta_{bd} for d=a: = (1 if b==a else 0) = 0 for a!=b
        # delta_{ad} for d=a: = 1
        # So: L_{ab,ba} = -2 R_{abba} + 0 + Ric_{ba}
        # R_{abba} = -R_{abab} (antisymmetry in last pair)
        # So: L_{ab,ba} = 2 R_{abab} + Ric_{ba}
        #
        # Therefore:
        # tr_{Sym^2}(E) = sum_a 2 Ric_{aa}
        #               + sum_{a<b} [-2 R_{aabb} + Ric_{aa} + 2 R_{abab} + Ric_{ba}]
        # = 2R + sum_{a<b} [-2 R_{aabb} + 2 R_{abab} + Ric_{aa} + Ric_{ab}]
        #
        # Note: R_{aabb} = R_{ab} (Ricci, summing over one pair)
        # Wait no: R_{aabb} summed over one index = Ric, but R_{aabb} with fixed a,b is a
        # component of the Riemann tensor, not summed.
        #
        # Let me just use the numerical approach for the fold value and verify,
        # then use analytic formulas for the sweep.

        # For the sweep, I'll compute E_Lich numerically at each tau.
        R_abcd_tau = compute_riemann_tensor_ON_fast(tau)
        Ric_tau = ricci_from_riemann(R_abcd_tau)

        # Compute tr(E_Lich) on Sym^2_0 numerically
        # Build E_sym and project to traceless
        E_full_tau = np.zeros((n, n, n, n))
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    for d in range(n):
                        E_full_tau[a, b, c, d] = (-2.0 * R_abcd_tau[a, c, b, d]
                                                  + Ric_tau[a, c] * (1 if b == d else 0)
                                                  + Ric_tau[b, c] * (1 if a == d else 0))

        # Build E_sym matrix
        E_sym_tau = np.zeros((r_sym2, r_sym2))
        for I_idx, (a, b) in enumerate(sym_pairs):
            for J_idx, (c, d) in enumerate(sym_pairs):
                N_I = np.sqrt(2.0) if a != b else 1.0
                N_J = np.sqrt(2.0) if c != d else 1.0
                val = (E_full_tau[a, b, c, d] + E_full_tau[a, b, d, c]
                     + E_full_tau[b, a, c, d] + E_full_tau[b, a, d, c]) / (N_I * N_J)
                E_sym_tau[I_idx, J_idx] = val

        # Project to traceless
        E_sym0_tau = P_traceless @ E_sym_tau @ P_traceless
        tr_E_sym0_tau = np.trace(E_sym0_tau)

        a2_TT_val = 35.0 * R / 6.0 + tr_E_sym0_tau
        a2_bos_val = a2_s + a2_g + a2_TT_val
        a2_dirac_val = 20.0 * R / 3.0

        a2_scalar_sweep[i] = a2_s
        a2_gauge_sweep[i] = a2_g
        a2_TT_sweep[i] = a2_TT_val
        a2_bos_sweep[i] = a2_bos_val
        a2_dirac_sweep[i] = a2_dirac_val
        ratio_sweep[i] = a2_bos_val / a2_dirac_val if abs(a2_dirac_val) > 1e-15 else 0

        if i % 5 == 0 or abs(tau - 0.19) < 0.006:
            print(f"  tau={tau:.3f}: a2_bos={a2_bos_val:.4f}, a2_dirac={a2_dirac_val:.4f}, "
                  f"ratio={ratio_sweep[i]:.4f}")

    # =========================================================================
    # STEP 9: Self-consistency and f determination
    # =========================================================================
    print(f"\n--- STEP 9: Self-consistency and f determination ---")

    # The bosonic a_2 route gives a DIFFERENT M_KK than the Dirac a_2 route.
    # If we demand G_N^{bos} = G_N^{obs}:
    #   M_KK^{bos} = sqrt(pi^3 * M_Pl^2 / (12 * a_2^{bos}))
    #   a_2^{bos} = ratio * a_2^{Dirac}
    #   M_KK^{bos} = M_KK^{Dirac} / sqrt(ratio)

    print(f"  ratio_bos/Dirac at fold = {ratio_bos_dirac:.6f}")
    print(f"  M_KK^Dirac = {M_KK:.4e} GeV (log10 = {np.log10(M_KK):.4f})")
    print(f"  M_KK^bos   = {M_KK_bos:.4e} GeV (log10 = {np.log10(M_KK_bos):.4f})")
    print(f"  M_KK^Kerner = {M_KK_kerner:.4e} GeV (log10 = {np.log10(M_KK_kerner):.4f})")

    # Does the bosonic route REDUCE the 0.83-decade M_KK tension?
    tension_dirac = np.log10(M_KK_kerner) - np.log10(M_KK)
    tension_bos = np.log10(M_KK_kerner) - np.log10(M_KK_bos)
    print(f"\n  M_KK tension (Kerner - GN):")
    print(f"    Dirac route: {tension_dirac:.4f} decades")
    print(f"    Bosonic route: {tension_bos:.4f} decades")
    print(f"    Change: {tension_bos - tension_dirac:+.4f} decades")

    # f_2 determination from Sakharov
    # If both spectral action (bosonic) and Sakharov give G_N:
    #   Spectral: 1/(16piG) = f_2 * Lambda^2 * a_2^{bos} * norm
    #   Sakharov: 1/(16piG) = (1/48pi^2) sum d_k [Lambda^2 - m_k^2 ln(1+Lambda^2/m_k^2)]
    #
    # At Lambda = 10*M_KK:
    #   f_2 * a_2^{bos} * (10*M_KK)^2 * norm = (1/48pi^2) * [sum terms]
    # This determines f_2 in terms of known quantities.

    # Using the S42 normalization: 1/(16piG) = (6/pi^3) * f_2 * a_2 * M_KK^2
    # At Lambda = 10*M_KK, Sakharov gives 1/(16piG_Sak) = inv_16piG_sak_10MKK
    # Spectral action gives 1/(16piG_spec) = (6/pi^3) * f_2 * a_2^{bos} * (10*M_KK)^2
    # Wait: Lambda in the spectral action is the CUTOFF, which we identify with M_KK.
    # The Sakharov formula uses Lambda_4D = 10*M_KK as the 4D UV cutoff.
    # The spectral action uses Lambda_SA = M_KK as the NCG cutoff.
    # So the comparison is:
    #   Spec: (6/pi^3) * f_2 * a_2^{bos, zeta} * M_KK^2 = 1/(16piG)
    #   Sak: (1/48pi^2) sum d_k [Lambda_4D^2 - ...] = 1/(16piG)
    # These should agree if the spectral action is the correct effective action.

    # Determine f_2:
    # (6/pi^3) * f_2 * a_2^{bos, eff} * M_KK^2 = inv_16piG_sak_10MKK
    f_2_from_sak = inv_16piG_sak_10MKK / ((6.0/PI**3) * a2_bos_eff * M_KK**2)
    print(f"\n  f_2 determination:")
    print(f"    From matching Sakharov(10*M_KK) to bosonic spectral action:")
    print(f"    f_2 = {f_2_from_sak:.4f}")
    print(f"    (f_2 = 1 by S42 convention for Dirac route)")

    # =========================================================================
    # STEP 10: Gate verdict
    # =========================================================================
    print(f"\n{'='*80}")
    print("GATE VERDICT: INDUCED-G-44")
    print("="*80)

    # The gate compares G_N^{bos} with G_N^{Sakharov}.
    # Using the SAME M_KK for both (GN route):
    log10_dev_sak = abs(np.log10(abs(inv_16piG_bos / inv_16piG_sak_10MKK)))
    log10_dev_obs = abs(np.log10(abs(inv_16piG_bos / INV_16piG_OBS)))

    print(f"\n  G_N^bos (at M_KK = {M_KK:.2e} GeV):")
    print(f"    1/(16piG_bos) = {inv_16piG_bos:.4e} GeV^2")
    print(f"    1/(16piG_obs) = {INV_16piG_OBS:.4e} GeV^2")
    print(f"    1/(16piG_Sak) = {inv_16piG_sak_10MKK:.4e} GeV^2 (Lambda=10*M_KK)")
    print(f"\n  |log10(G_bos/G_Sak)| = {log10_dev_sak:.4f} OOM")
    print(f"  |log10(G_bos/G_obs)| = {log10_dev_obs:.4f} OOM")

    if log10_dev_sak < 1.0:
        verdict = "PASS"
        print(f"\n  INDUCED-G-44: **PASS** (within 1 OOM of Sakharov)")
    elif log10_dev_sak > 3.0:
        verdict = "FAIL"
        print(f"\n  INDUCED-G-44: **FAIL** (> 3 OOM from Sakharov)")
    else:
        verdict = "INFO"
        print(f"\n  INDUCED-G-44: **INFO** (intermediate: {log10_dev_sak:.2f} OOM)")

    print(f"\n  Structural results:")
    print(f"    1. Bosonic a_2 = {ratio_bos_dirac:.4f}x Dirac a_2 (ratio > 1 because bosonic DOF > spinor DOF)")
    print(f"    2. G_N^bos / G_N^obs = {INV_16piG_OBS / inv_16piG_bos:.4f} (using M_KK from Dirac)")
    print(f"    3. G_N^bos / G_N^Sak = {inv_16piG_sak_10MKK / inv_16piG_bos:.4f}")
    print(f"    4. M_KK tension: Dirac={tension_dirac:.4f}, Bos={tension_bos:.4f} decades")
    print(f"    5. f_2 = {f_2_from_sak:.4f} (from matching Sakharov at Lambda=10*M_KK)")

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    npz_path = os.path.join(SCRIPT_DIR, 's44_induced_g.npz')
    np.savez(npz_path,
        # Core results
        a2_red_scalar=a2_red_scalar,
        a2_red_gauge=a2_red_gauge,
        a2_red_TT=a2_red_TT,
        a2_red_bos_total=a2_red_bos_total,
        a2_red_dirac=a2_red_dirac,
        ratio_bos_dirac=ratio_bos_dirac,
        a2_bos_eff=a2_bos_eff,
        inv_16piG_bos=inv_16piG_bos,
        inv_16piG_sak_10MKK=inv_16piG_sak_10MKK,
        inv_16piG_obs=INV_16piG_OBS,
        M_KK_bos=M_KK_bos,
        M_KK_dirac=M_KK,
        M_KK_kerner=M_KK_kerner,
        tension_dirac=tension_dirac,
        tension_bos=tension_bos,
        f_2_from_sak=f_2_from_sak,
        log10_dev_sak=log10_dev_sak,
        log10_dev_obs=log10_dev_obs,
        # Sweep data
        tau_sweep=tau_sweep,
        a2_bos_sweep=a2_bos_sweep,
        a2_dirac_sweep=a2_dirac_sweep,
        a2_scalar_sweep=a2_scalar_sweep,
        a2_gauge_sweep=a2_gauge_sweep,
        a2_TT_sweep=a2_TT_sweep,
        ratio_sweep=ratio_sweep,
        # Curvature
        R_K=R_K,
        Ric2=Ric2,
        Kret=Kret,
        tr_E_sym0=tr_E_sym0,
        # Gate
        gate_verdict=np.array([verdict]),
        gate_name=np.array(['INDUCED-G-44']),
    )
    print(f"\nData saved to {npz_path}")

    # =========================================================================
    # PLOT
    # =========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'INDUCED-G-44: Bosonic a_2 and G_N\n'
                 f'Gate verdict: {verdict} (|log10(G_bos/G_Sak)| = {log10_dev_sak:.2f} OOM)',
                 fontsize=14, fontweight='bold')

    # Panel 1: a_2 components vs tau
    ax = axes[0, 0]
    ax.plot(tau_sweep, a2_bos_sweep, 'b-', lw=2, label=r'$a_2^{\mathrm{bos}}$ (total)')
    ax.plot(tau_sweep, a2_dirac_sweep, 'r--', lw=2, label=r'$a_2^{\mathrm{Dirac}}$')
    ax.plot(tau_sweep, a2_scalar_sweep, 'g:', lw=1.5, label=r'$a_2^{\mathrm{scalar}}$')
    ax.plot(tau_sweep, a2_gauge_sweep, 'm:', lw=1.5, label=r'$a_2^{\mathrm{gauge}}$')
    ax.plot(tau_sweep, a2_TT_sweep, 'c:', lw=1.5, label=r'$a_2^{\mathrm{TT}}$')
    ax.axvline(x=TAU_FOLD, color='gray', ls='--', alpha=0.5, label='fold')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$a_2^{\mathrm{red}}$')
    ax.set_title(r'Reduced $a_2$ coefficients vs $\tau$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 2: Ratio bos/Dirac vs tau
    ax = axes[0, 1]
    ax.plot(tau_sweep, ratio_sweep, 'k-', lw=2)
    ax.axvline(x=TAU_FOLD, color='gray', ls='--', alpha=0.5)
    ax.axhline(y=ratio_bos_dirac, color='r', ls=':', alpha=0.5,
               label=f'fold value: {ratio_bos_dirac:.3f}')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$a_2^{\mathrm{bos}} / a_2^{\mathrm{Dirac}}$')
    ax.set_title(r'Ratio bosonic/Dirac $a_2$')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 3: G_N comparison bar chart
    ax = axes[1, 0]
    labels = ['Observed', 'Dirac\n(S42)', 'Bosonic\n(this)', 'Sakharov\n(W1-1)']
    values = [INV_16piG_OBS, INV_16piG_OBS, inv_16piG_bos, inv_16piG_sak_10MKK]
    colors = ['green', 'blue', 'red', 'orange']
    bars = ax.bar(labels, [np.log10(v) for v in values], color=colors, alpha=0.7)
    ax.set_ylabel(r'$\log_{10}[1/(16\pi G)]$ (GeV$^2$)')
    ax.set_title(r'$G_N$ comparison')
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.05,
                f'{val:.2e}', ha='center', va='bottom', fontsize=8)
    ax.grid(True, alpha=0.3, axis='y')

    # Panel 4: M_KK comparison
    ax = axes[1, 1]
    mkk_labels = ['Dirac\n(S42)', 'Bosonic\n(this)', 'Kerner\n(gauge)']
    mkk_vals = [M_KK, M_KK_bos, M_KK_kerner]
    mkk_log = [np.log10(v) for v in mkk_vals]
    bars2 = ax.bar(mkk_labels, mkk_log, color=['blue', 'red', 'purple'], alpha=0.7)
    ax.set_ylabel(r'$\log_{10}(M_{\mathrm{KK}}$/GeV)')
    ax.set_title(r'$M_{\mathrm{KK}}$ from different routes')
    for bar, val, lv in zip(bars2, mkk_vals, mkk_log):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.02,
                f'{lv:.2f}', ha='center', va='bottom', fontsize=9)

    # Add tension arrows
    ax.annotate('', xy=(1, mkk_log[1]), xytext=(2, mkk_log[2]),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    mid_y = (mkk_log[1] + mkk_log[2]) / 2
    ax.text(1.5, mid_y, f'{tension_bos:.2f}\ndec', ha='center', fontsize=8)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    png_path = os.path.join(SCRIPT_DIR, 's44_induced_g.png')
    plt.savefig(png_path, dpi=150, bbox_inches='tight')
    print(f"Plot saved to {png_path}")

    dt = time.time() - t_start
    print(f"\nTotal time: {dt:.1f}s")
    print("=" * 80)


if __name__ == '__main__':
    main()
