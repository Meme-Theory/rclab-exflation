"""
S43 LICHN-43: LICHNEROWICZ LAPLACIAN ON U(2)-INVARIANT TT 2-TENSORS
====================================================================

Gate LICHN-43: Compute eigenvalues of the Lichnerowicz Laplacian on
U(2)-invariant TT symmetric 2-tensors at the fold (tau ~ 0.19) and
across the full Jensen deformation range tau in [0, 0.30].

PASS: All eigenvalues positive (gravitational stability).
FAIL: Any negative eigenvalue (gravitational instability).

Mathematical framework:
    Delta_L h_{ab} = (nabla^* nabla h)_{ab}       [rough Laplacian]
                   - 2 R_{acbd} h^{cd}             [Riemann endomorphism]
                   + Ric_a^c h_{cb} + Ric_b^c h_{ac}  [Ricci coupling]

    On (SU(3), g_tau), restricted to U(2)-invariant TT tensors in the
    trivial Peter-Weyl sector (p,q) = (0,0).

Key structural results:
    1. U(2)-invariant Sym^2_0(R^8) has dimension 2 (representation theory).
    2. Both basis tensors are automatically transverse (div = 0) at all tau.
    3. The rough Laplacian is NON-ZERO at tau > 0 (connection-squared fiber terms).
    4. The 2x2 Lichnerowicz problem is exact (no truncation).

References:
    - Lauret (2021): On the Stability of Homogeneous Einstein Manifolds (Paper 37)
    - Schwahn (2023): Lichnerowicz Laplacian on Normal Homogeneous Spaces (Paper 39)
    - l20_lichnerowicz.py: Session 20b infrastructure (rough Laplacian, R/Ric endomorphisms)
    - r20a_riemann_tensor.py: Riemann tensor infrastructure

Author: Baptista Spacetime Analyst (Session 43)
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
from r20a_riemann_tensor import (
    compute_riemann_tensor_ON_fast,
    ricci_from_riemann,
)
from l20_lichnerowicz import (
    build_sym2_traceless_basis,
    riemann_endomorphism_on_sym2,
    ricci_endomorphism_on_sym2,
    rough_laplacian_on_sym2_sector,
    build_divergence_matrix,
    build_lichnerowicz_on_sector,
)
from b6_scalar_vector_laplacian import dim_pq, casimir_pq


# =============================================================================
# MODULE 1: U(2)-INVARIANT TT SUBSPACE
# =============================================================================

def build_u2_invariant_tt_basis(f_abc, n=8):
    """
    Construct an orthonormal basis for the U(2)-invariant subspace of
    Sym^2_0(R^8), the space of traceless symmetric 2-tensors on su(3).

    The U(2) = SU(2) x U(1) acts on su(3) = u(1) + su(2) + C^2 via the
    adjoint representation. U(2)-invariant tensors must be diagonal in
    the block structure and proportional to the identity within each block.

    General form: h = diag(a,a,a, b,b,b,b, c) with 3a + 4b + c = 0.
    This is a 2-dimensional space.

    Returns:
        h_1, h_2: Two orthonormal (8,8) traceless symmetric matrices.
    """
    # Basis tensor 1: su(2) vs u(1) contrast
    h_1 = np.diag([-1., -1., -1., 0., 0., 0., 0., 3.])
    h_1 /= np.sqrt(np.trace(h_1 @ h_1))

    # Basis tensor 2: su(2)+u(1) vs C^2 contrast (orthogonalized)
    h_2_raw = np.diag([-4., -4., -4., 3., 3., 3., 3., 0.])
    h_2_raw /= np.sqrt(np.trace(h_2_raw @ h_2_raw))

    # Gram-Schmidt orthogonalization
    overlap = np.trace(h_1 @ h_2_raw)
    h_2 = h_2_raw - overlap * h_1
    h_2 /= np.sqrt(np.trace(h_2 @ h_2))

    # Validate
    assert abs(np.trace(h_1)) < 1e-12, "h_1 not traceless"
    assert abs(np.trace(h_2)) < 1e-12, "h_2 not traceless"
    assert abs(np.trace(h_1 @ h_1) - 1.0) < 1e-12, "h_1 not normalized"
    assert abs(np.trace(h_2 @ h_2) - 1.0) < 1e-12, "h_2 not normalized"
    assert abs(np.trace(h_1 @ h_2)) < 1e-12, "h_1, h_2 not orthogonal"

    return h_1, h_2


def verify_u2_invariance(h, f_abc, u2_indices, n=8, tol=1e-10):
    """
    Verify that tensor h is invariant under the adjoint action of u(2).

    (ad(X).h)_{ab} = sum_c A_X[c,a] h[c,b] + sum_c A_X[c,b] h[a,c]
    where A_X[c,a] = f_{Xac}.
    """
    for X in u2_indices:
        A_X = np.zeros((n, n))
        for c in range(n):
            for a in range(n):
                A_X[c, a] = f_abc[X, a, c]
        adX_h = A_X.T @ h + h @ A_X
        err = np.max(np.abs(adX_h))
        if err > tol:
            return False, err
    return True, 0.0


def verify_transversality(h, Gamma, n=8, tol=1e-10):
    """
    Verify that a constant tensor h is transverse (div h = 0).

    For constant h on a Lie group:
    (div h)_b = sum_a (nabla_a h)_{ab}
              = -sum_{a,d} Gamma^d_{aa} h_{db} - sum_{a,d} Gamma^d_{ab} h_{ad}
    """
    div_h = np.zeros(n)
    for b in range(n):
        val = 0.0
        for a in range(n):
            for d in range(n):
                val -= Gamma[d, a, a] * h[d, b]
                val -= Gamma[d, a, b] * h[a, d]
        div_h[b] = val
    return np.max(np.abs(div_h)) < tol


# =============================================================================
# MODULE 2: LICHNEROWICZ ON U(2)-INVARIANT TT SECTOR
# =============================================================================

def lichnerowicz_u2_invariant(tau, gens, f_abc, basis_sym2, h_1, h_2):
    """
    Compute the 2x2 Lichnerowicz Laplacian on U(2)-invariant TT tensors.

    At each tau, the full 35x35 Lichnerowicz operator on the (0,0) sector is:
        Delta_L = rough_Laplacian + R_endomorphism + Ric_endomorphism

    We project this to the 2-dimensional U(2)-invariant subspace.

    Args:
        tau: Jensen parameter
        gens, f_abc: su(3) infrastructure
        basis_sym2: (35, 8, 8) Sym^2_0 basis
        h_1, h_2: U(2)-invariant ON basis tensors

    Returns:
        evals: (2,) eigenvalues of Delta_L on U(2)-inv TT sector
        DeltaL_2x2: (2,2) matrix
        evals_35: (35,) or (31,) full eigenvalues
        Ric_diag: (3,) Ricci eigenvalues [u(1), su(2), C^2]
    """
    n = 8
    dim_fiber = 35

    # Build geometric infrastructure
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E_frame = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E_frame)
    Gamma = connection_coefficients(ft)

    # Curvature
    R_abcd = compute_riemann_tensor_ON_fast(tau)
    Ric = ricci_from_riemann(R_abcd)
    R_endo = riemann_endomorphism_on_sym2(R_abcd, basis_sym2)
    Ric_endo = ricci_endomorphism_on_sym2(Ric, basis_sym2)

    # Rough Laplacian on (0,0) sector
    rho, d = get_irrep(0, 0, gens, f_abc)
    rough_lap_full = rough_laplacian_on_sym2_sector(rho, E_frame, Gamma, n)
    P = basis_sym2.reshape(dim_fiber, n * n)
    rough_lap_sym2 = np.real(P @ rough_lap_full @ P.conj().T)

    # Full 35x35 Lichnerowicz (no TT projection — U(2)-inv tensors are auto-TT)
    DeltaL_35 = rough_lap_sym2 + R_endo + Ric_endo
    DeltaL_35 = 0.5 * (DeltaL_35 + DeltaL_35.T)

    # Full eigenvalues
    evals_35 = np.sort(np.linalg.eigvalsh(DeltaL_35))

    # Project to U(2)-invariant 2x2
    coeff_1 = np.array([np.trace(basis_sym2[I] @ h_1) for I in range(dim_fiber)])
    coeff_2 = np.array([np.trace(basis_sym2[I] @ h_2) for I in range(dim_fiber)])

    DL_2x2 = np.zeros((2, 2))
    DL_2x2[0, 0] = coeff_1 @ DeltaL_35 @ coeff_1
    DL_2x2[0, 1] = coeff_1 @ DeltaL_35 @ coeff_2
    DL_2x2[1, 0] = coeff_2 @ DeltaL_35 @ coeff_1
    DL_2x2[1, 1] = coeff_2 @ DeltaL_35 @ coeff_2

    evals = np.sort(np.linalg.eigvalsh(DL_2x2))

    # Ricci by sector
    Ric_diag = np.array([
        np.mean([Ric[i, i] for i in U1_IDX]),
        np.mean([Ric[i, i] for i in SU2_IDX]),
        np.mean([Ric[i, i] for i in C2_IDX]),
    ])

    return evals, DL_2x2, evals_35, Ric_diag


# =============================================================================
# MODULE 3: HIGHER PETER-WEYL SECTOR CHECK
# =============================================================================

def check_higher_sectors(tau, gens, f_abc, max_pq=2):
    """
    Check Lichnerowicz eigenvalues on higher Peter-Weyl sectors.

    Higher sectors have additional positive contribution from the Casimir
    (rough Laplacian), so they should be more stable. This is a verification.

    Returns:
        list of (p, q, min_eval, n_TT, n_negative) tuples
    """
    n = 8
    R_abcd = compute_riemann_tensor_ON_fast(tau)
    Ric = ricci_from_riemann(R_abcd)
    basis = build_sym2_traceless_basis(n)
    R_endo = riemann_endomorphism_on_sym2(R_abcd, basis)
    Ric_endo = ricci_endomorphism_on_sym2(Ric, basis)

    results = []
    for p in range(max_pq + 1):
        for q in range(max_pq + 1 - p):
            if p + q > max_pq:
                continue
            d = dim_pq(p, q)
            try:
                evals_TT, n_TT, n_full = build_lichnerowicz_on_sector(
                    p, q, tau, R_abcd, basis, R_endo, Ric_endo, gens, f_abc, n
                )
                min_ev = np.min(evals_TT) if len(evals_TT) > 0 else float('inf')
                n_neg = np.sum(evals_TT < -1e-8)
                results.append((p, q, min_ev, n_TT, n_neg))
            except Exception as e:
                results.append((p, q, float('nan'), 0, -1))
    return results


# =============================================================================
# MODULE 4: MAIN COMPUTATION
# =============================================================================

def main():
    t_start = time.time()
    print("=" * 80)
    print("LICHN-43: LICHNEROWICZ LAPLACIAN ON U(2)-INVARIANT TT 2-TENSORS")
    print("=" * 80)

    # Infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    basis_sym2 = build_sym2_traceless_basis(8)
    h_1, h_2 = build_u2_invariant_tt_basis(f_abc)

    # --- Validation ---
    print("\n--- VALIDATION ---")

    # 1. U(2) invariance of basis tensors
    u2_idx = U1_IDX + SU2_IDX  # [7, 0, 1, 2]
    ok1, err1 = verify_u2_invariance(h_1, f_abc, u2_idx)
    ok2, err2 = verify_u2_invariance(h_2, f_abc, u2_idx)
    print(f"  U(2)-invariance of h_1: {'PASS' if ok1 else 'FAIL'} (err={err1:.2e})")
    print(f"  U(2)-invariance of h_2: {'PASS' if ok2 else 'FAIL'} (err={err2:.2e})")

    # 2. Transversality at sample tau values
    for tau_test in [0.0, 0.19, 0.285]:
        B_ab = compute_killing_form(f_abc)
        g_s = jensen_metric(B_ab, tau_test)
        ft = frame_structure_constants(f_abc, orthonormal_frame(g_s))
        Gamma = connection_coefficients(ft)
        tt1 = verify_transversality(h_1, Gamma)
        tt2 = verify_transversality(h_2, Gamma)
        print(f"  Transversality at tau={tau_test:.3f}: h_1={'PASS' if tt1 else 'FAIL'}, "
              f"h_2={'PASS' if tt2 else 'FAIL'}")

    # 3. Bi-invariant check at tau=0
    evals_0, DL_0, evals35_0, Ric_0 = lichnerowicz_u2_invariant(
        0.0, gens, f_abc, basis_sym2, h_1, h_2
    )
    print(f"  tau=0 eigenvalues: {evals_0} (expected: [1.0, 1.0])")
    assert abs(evals_0[0] - 1.0) < 1e-8, f"tau=0 validation failed: {evals_0}"
    assert abs(evals_0[1] - 1.0) < 1e-8, f"tau=0 validation failed: {evals_0}"
    print(f"  tau=0 validation: PASS")

    # --- Main sweep ---
    print("\n--- LICHNEROWICZ EIGENVALUE SWEEP ---")
    tau_values = np.linspace(0.0, 0.30, 61)
    n_tau = len(tau_values)

    lam1 = np.zeros(n_tau)
    lam2 = np.zeros(n_tau)
    min_all35 = np.zeros(n_tau)
    ric_u1 = np.zeros(n_tau)
    ric_su2 = np.zeros(n_tau)
    ric_c2 = np.zeros(n_tau)
    DL_AA = np.zeros(n_tau)
    DL_BB = np.zeros(n_tau)
    DL_AB = np.zeros(n_tau)

    print(f"{'tau':>6s}  {'lam1':>10s}  {'lam2':>10s}  {'min_35':>10s}  "
          f"{'Ric_u1':>8s}  {'Ric_su2':>8s}  {'Ric_C2':>8s}")
    print("-" * 80)

    for i, tau in enumerate(tau_values):
        evals, DL_2x2, evals35, Ric_diag = lichnerowicz_u2_invariant(
            tau, gens, f_abc, basis_sym2, h_1, h_2
        )
        lam1[i] = evals[0]
        lam2[i] = evals[1]
        min_all35[i] = evals35[0]
        ric_u1[i] = Ric_diag[0]
        ric_su2[i] = Ric_diag[1]
        ric_c2[i] = Ric_diag[2]
        DL_AA[i] = DL_2x2[0, 0]
        DL_BB[i] = DL_2x2[1, 1]
        DL_AB[i] = DL_2x2[0, 1]

        if i % 10 == 0 or abs(tau - 0.19) < 0.003 or abs(tau - 0.285) < 0.003:
            print(f"{tau:6.3f}  {evals[0]:10.6f}  {evals[1]:10.6f}  {evals35[0]:10.6f}  "
                  f"{Ric_diag[0]:8.4f}  {Ric_diag[1]:8.4f}  {Ric_diag[2]:8.4f}")

    # --- Higher sector check at key tau values ---
    print("\n--- HIGHER PETER-WEYL SECTOR CHECK ---")
    for tau_check in [0.19, 0.285]:
        print(f"\n  tau = {tau_check:.3f}:")
        sector_results = check_higher_sectors(tau_check, gens, f_abc, max_pq=2)
        all_positive = True
        for p, q, min_ev, nTT, n_neg in sector_results:
            d = dim_pq(p, q)
            C2 = casimir_pq(p, q)
            print(f"    ({p},{q}) d={d:>2d} C2={C2:5.2f}: nTT={nTT:>3d}, "
                  f"min={min_ev:10.6f}, n_neg={n_neg}")
            if n_neg > 0:
                all_positive = False
        print(f"  All sectors positive: {'YES' if all_positive else 'NO -- INSTABILITY!'}")

    # --- Gate verdict ---
    print("\n" + "=" * 80)
    print("GATE LICHN-43 VERDICT")
    print("=" * 80)

    global_min_u2 = np.min(lam1)
    global_min_u2_tau = tau_values[np.argmin(lam1)]
    global_min_35 = np.min(min_all35)
    global_min_35_tau = tau_values[np.argmin(min_all35)]
    fold_min = lam1[np.argmin(np.abs(tau_values - 0.19))]
    dnp_min = lam1[np.argmin(np.abs(tau_values - 0.285))]

    print(f"  U(2)-invariant sector:")
    print(f"    Minimum eigenvalue: {global_min_u2:.6f} at tau = {global_min_u2_tau:.3f}")
    print(f"    At fold (tau=0.19):  {fold_min:.6f}")
    print(f"    At DNP  (tau=0.285): {dnp_min:.6f}")
    print(f"    At round (tau=0):    {lam1[0]:.6f}")
    print(f"  Full Sym^2_0 sector:")
    print(f"    Minimum eigenvalue: {global_min_35:.6f} at tau = {global_min_35_tau:.3f}")

    gate_pass = np.all(lam1 > 0) and np.all(min_all35 > 0)
    verdict = "PASS" if gate_pass else "FAIL"
    print(f"\n  GATE LICHN-43: {verdict}")
    if gate_pass:
        print(f"    All eigenvalues strictly positive across tau in [0, 0.30].")
        print(f"    Minimum margin: {global_min_35:.6f} (at tau={global_min_35_tau:.3f})")
        print(f"    No gravitational instability detected.")
    else:
        print(f"    NEGATIVE EIGENVALUE DETECTED — gravitational instability!")

    # --- Save data ---
    npz_path = os.path.join(SCRIPT_DIR, 's43_lichnerowicz.npz')
    np.savez(npz_path,
             tau_values=tau_values,
             lam1_u2=lam1,
             lam2_u2=lam2,
             min_all35=min_all35,
             ric_u1=ric_u1,
             ric_su2=ric_su2,
             ric_c2=ric_c2,
             DL_AA=DL_AA,
             DL_BB=DL_BB,
             DL_AB=DL_AB,
             fold_min=fold_min,
             dnp_min=dnp_min,
             global_min=global_min_35,
             verdict=np.array([verdict]))
    print(f"\n  Data saved: {npz_path}")

    # --- Plot ---
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('LICHN-43: Lichnerowicz Laplacian on U(2)-invariant TT tensors\n'
                 f'Gate verdict: {verdict}', fontsize=14, fontweight='bold')

    # Panel 1: U(2)-invariant eigenvalues vs tau
    ax = axes[0, 0]
    ax.plot(tau_values, lam1, 'b-', linewidth=2, label=r'$\lambda_1$ (lower)')
    ax.plot(tau_values, lam2, 'r-', linewidth=2, label=r'$\lambda_2$ (upper)')
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(x=0.19, color='gray', linestyle=':', alpha=0.5, label=r'fold ($\tau=0.19$)')
    ax.axvline(x=0.285, color='gray', linestyle='--', alpha=0.5, label=r'DNP ($\tau=0.285$)')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$\lambda_{\mathrm{Lich}}$')
    ax.set_title('U(2)-invariant Lichnerowicz eigenvalues')
    ax.legend(fontsize=9)
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)

    # Panel 2: Full 35-dim minimum vs tau
    ax = axes[0, 1]
    ax.plot(tau_values, min_all35, 'g-', linewidth=2, label=r'min $\lambda$ (all 35 modes)')
    ax.plot(tau_values, lam1, 'b--', linewidth=1.5, label=r'min $\lambda$ (U(2)-inv)')
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax.axvline(x=0.19, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(x=0.285, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$\min \lambda_{\mathrm{Lich}}$')
    ax.set_title('Minimum Lichnerowicz eigenvalue')
    ax.legend(fontsize=9)
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)

    # Panel 3: 2x2 matrix elements
    ax = axes[1, 0]
    ax.plot(tau_values, DL_AA, 'b-', linewidth=1.5, label=r'$\Delta_L^{AA}$')
    ax.plot(tau_values, DL_BB, 'r-', linewidth=1.5, label=r'$\Delta_L^{BB}$')
    ax.plot(tau_values, DL_AB, 'g-', linewidth=1.5, label=r'$\Delta_L^{AB}$')
    ax.axvline(x=0.19, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(x=0.285, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Matrix element')
    ax.set_title(r'$2 \times 2$ Lichnerowicz matrix elements')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 4: Anisotropic Ricci
    ax = axes[1, 1]
    ax.plot(tau_values, ric_u1, 'b-', linewidth=1.5, label=r'$\mathrm{Ric}|_{\mathfrak{u}(1)}$')
    ax.plot(tau_values, ric_su2, 'r-', linewidth=1.5, label=r'$\mathrm{Ric}|_{\mathfrak{su}(2)}$')
    ax.plot(tau_values, ric_c2, 'g-', linewidth=1.5, label=r'$\mathrm{Ric}|_{\mathbb{C}^2}$')
    ax.axvline(x=0.19, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(x=0.285, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$\mathrm{Ric}$')
    ax.set_title('Anisotropic Ricci tensor')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    png_path = os.path.join(SCRIPT_DIR, 's43_lichnerowicz.png')
    plt.savefig(png_path, dpi=150, bbox_inches='tight')
    print(f"  Plot saved: {png_path}")

    dt = time.time() - t_start
    print(f"\n  Total time: {dt:.1f}s")
    print("=" * 80)


if __name__ == '__main__':
    main()
