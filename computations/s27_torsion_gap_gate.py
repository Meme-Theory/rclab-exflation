"""
SESSION 27 PRIORITY 1: T-1 TORSION GAP GATE
=============================================

Gate T-1: Does the torsionful (canonical connection) Dirac operator have a
weaker spectral gap than the Levi-Civita Dirac operator D_K?

Physics:
  On a Lie group with left-invariant metric g_tau (Jensen deformation), there
  are two natural connections:
    1. Levi-Civita (torsion-free): Gamma_LC^c_{ab} = connection_coefficients(ft)
    2. Canonical (Cartan-Schouten minus): nabla_X Y = 0 for left-invariant X,Y
       => Gamma_can = 0, torsion T(X,Y) = -[X,Y]

  The contorsion tensor K = Gamma_can - Gamma_LC = -Gamma_LC.

  The canonical-connection Dirac operator is:
    D_can = M_Lie + I (x) Omega_can
  where Omega_can = spinor_connection_offset(Gamma_can, gammas) = 0 (flat).

  Equivalently: D_can = D_K + I (x) Omega_T, where Omega_T is the spinor
  offset from the contorsion K = -Gamma_LC, giving Omega_T = -Omega_LC.
  So D_can = D_K - I (x) Omega_LC = M_Lie (just the Lie derivative term).

  Session 26 computed interpolations D(t) = M_Lie + (1-t)*Omega at FIXED tau.
  This script sweeps TAU in [0, 0.50] and compares:
    gap_K(tau)   = min |eigenvalue| of D_K(tau)
    gap_T(tau)   = min |eigenvalue| of D_can(tau) = M_Lie(tau)
  across 4 sectors: (0,0), (1,0), (0,1), (1,1).

Gate verdict:
  PASS: gap_T < gap_K at any tau in any non-trivial sector
        (=> torsion weakens gap, BCS prerequisite survives)
  CLOSED: gap_T >= gap_K everywhere
        (=> torsion preserves/strengthens gap, no weakening)

NOTE: The singlet (0,0) is excluded from the gate because D_can on the
trivial rep has rho[b]=0 => M_Lie=0, so gap_T=0 trivially. The gate is
meaningful only for sectors where M_Lie is nonzero.

Cross-checks:
  C1: K = -Gamma_LC at all tau (contorsion identity)
  C2: Omega_T + Omega_LC = 0 at all tau (spinor offset cancellation)
  C3: D_can eigenvalues = M_Lie eigenvalues at all tau (reconstruction)

Author: phonon-exflation-sim agent (Session 27)
Date: 2026-02-26
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
import time

# Add tier0-computation to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    dirac_operator_on_irrep, get_irrep, _irrep_cache
)

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# CONTORSION COMPUTATION
# =============================================================================

def compute_contorsion_from_torsion(ft, sign=-1):
    """
    Compute the contorsion tensor K from the Schouten torsion (ON-frame
    structure constants).

    The canonical connection on a Lie group has torsion:
        T^c_{ab} = sign * ft[a, b, c]
    with sign = -1 for the Cartan convention T(X,Y) = -[X,Y].

    The contorsion (difference: full connection minus LC) is:
        K^c_{ab} = (1/2)(T^c_{ab} + T^a_{cb} + T^b_{ca})

    In ON frame all indices are equivalent (metric = delta), so T_{cab} = T^c_{ab}.

    The result is stored as K[c, a, b] = K^c_{ab}, matching the convention
    of connection_coefficients() and compatible with spinor_connection_offset().

    Mathematical verification:
        At all tau, the canonical connection has Gamma_can = 0, so:
        K = Gamma_can - Gamma_LC = -Gamma_LC
        This identity is checked as cross-validation C1.

    Args:
        ft: (8,8,8) ON-frame structure constants, ft[a,b,c] = f_tilde^c_{ab}
        sign: -1 for Cartan convention (default), +1 for alternative

    Returns:
        K: (8,8,8) contorsion tensor, K[c,a,b] = K^c_{ab}
    """
    n = ft.shape[0]
    K = np.zeros((n, n, n), dtype=np.float64)

    for c in range(n):
        for a in range(n):
            for b in range(n):
                # T^c_{ab} = sign * ft[a, b, c]
                T_c_ab = sign * ft[a, b, c]
                # T^a_{cb} = sign * ft[c, b, a]
                T_a_cb = sign * ft[c, b, a]
                # T^b_{ca} = sign * ft[c, a, b]
                T_b_ca = sign * ft[c, a, b]

                K[c, a, b] = 0.5 * (T_c_ab + T_a_cb + T_b_ca)

    return K


def build_M_Lie(rho, E, gammas):
    """
    Build the Lie derivative part of the Dirac operator on irrep sector (p,q).

    M_Lie = sum_{a,b} E_{ab} rho[b] (x) gamma_a

    This is D_K minus the spinor connection offset:
        D_K = M_Lie + I (x) Omega_LC

    For the canonical-connection Dirac: D_can = M_Lie (since Omega_can = 0).

    Args:
        rho: list of 8 representation matrices (dim_rho x dim_rho)
        E: (8,8) orthonormal frame matrix
        gammas: list of 8 Clifford generators (16x16)

    Returns:
        M: (dim_rho*16, dim_rho*16) complex matrix
    """
    dim_rho = rho[0].shape[0]
    dim_spin = gammas[0].shape[0]
    dim_total = dim_rho * dim_spin
    M = np.zeros((dim_total, dim_total), dtype=complex)

    for a in range(8):
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                M += E[a, b] * np.kron(rho[b], gammas[a])

    return M


def extract_gap(evals):
    """
    Extract the spectral gap = min |eigenvalue| from a set of eigenvalues.

    For anti-Hermitian operators, eigenvalues are purely imaginary.
    We take min of absolute values of imaginary parts.

    Args:
        evals: array of complex eigenvalues

    Returns:
        gap: float, minimum absolute eigenvalue magnitude
    """
    mags = np.abs(evals.imag)
    return np.min(mags) if len(mags) > 0 else 0.0


# =============================================================================
# MAIN GATE COMPUTATION
# =============================================================================

def run_torsion_gap_gate():
    """
    Execute the T-1 Torsion Gap Gate computation.

    Sweeps tau in [0, 0.50] across 21 values, computes gap_K and gap_T
    for 4 sectors, performs 3 cross-checks, renders verdict.
    """
    print("=" * 72)
    print("SESSION 27 PRIORITY 1: T-1 TORSION GAP GATE")
    print("=" * 72)
    t_start = time.time()

    # Infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    # Sweep parameters
    tau_values = np.linspace(0.0, 0.50, 21)
    sectors = [(0, 0), (1, 0), (0, 1), (1, 1)]
    sector_labels = ['(0,0)', '(1,0)', '(0,1)', '(1,1)']
    n_tau = len(tau_values)
    n_sec = len(sectors)

    # Storage
    gap_K = np.zeros((n_sec, n_tau))       # LC Dirac gap
    gap_T = np.zeros((n_sec, n_tau))       # Canonical (torsionful) Dirac gap
    gap_ratio = np.zeros((n_sec, n_tau))   # gap_T / gap_K
    c1_errors = np.zeros(n_tau)            # ||K + Gamma_LC||
    c2_errors = np.zeros(n_tau)            # ||Omega_T + Omega_LC||
    c3_errors = np.zeros((n_sec, n_tau))   # ||D_can - M_Lie||

    # Store full spectra for select tau values for plotting
    spectra_K = {}  # (sector_idx, tau_idx) -> sorted |imag eigenvalues|
    spectra_T = {}
    plot_tau_indices = [0, 5, 10, 15, 20]  # tau = 0, 0.125, 0.25, 0.375, 0.50

    print(f"\nSweeping {n_tau} tau values x {n_sec} sectors")
    print(f"Sectors: {sector_labels}")
    print("-" * 72)

    for i, tau in enumerate(tau_values):
        t_iter = time.time()

        # Build geometric infrastructure at this tau
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma_LC = connection_coefficients(ft)
        Omega_LC = spinor_connection_offset(Gamma_LC, gammas)

        # Contorsion and its spinor offset
        K = compute_contorsion_from_torsion(ft, sign=-1)
        Omega_T = spinor_connection_offset(K, gammas)

        # Cross-check C1: K should equal -Gamma_LC
        c1_err = np.max(np.abs(K + Gamma_LC))
        c1_errors[i] = c1_err

        # Cross-check C2: Omega_T should equal -Omega_LC
        c2_err = np.max(np.abs(Omega_T + Omega_LC))
        c2_errors[i] = c2_err

        # Process each sector
        for j, (p, q) in enumerate(sectors):
            _irrep_cache.clear()

            if p == 0 and q == 0:
                # Trivial rep: D_K = Omega_LC, D_can = 0
                D_K_mat = Omega_LC.copy()
                D_T_mat = np.zeros_like(Omega_LC)  # M_Lie = 0 for trivial rep

                evals_K = np.linalg.eigvals(D_K_mat)
                evals_T = np.linalg.eigvals(D_T_mat)
            else:
                rho, dim_rho = get_irrep(p, q, gens, f_abc)

                # D_K = M_Lie + I (x) Omega_LC
                D_K_mat = dirac_operator_on_irrep(rho, E, gammas, Omega_LC)

                # M_Lie (= D_can, the canonical-connection Dirac)
                M_Lie = build_M_Lie(rho, E, gammas)

                # D_T = D_K + I (x) Omega_T = M_Lie + I (x) (Omega_LC + Omega_T)
                # Since Omega_T = -Omega_LC, D_T = M_Lie
                D_T_mat = D_K_mat + np.kron(np.eye(dim_rho), Omega_T)

                # Cross-check C3: D_T should equal M_Lie
                c3_err = np.max(np.abs(D_T_mat - M_Lie))
                c3_errors[j, i] = c3_err

                evals_K = np.linalg.eigvals(D_K_mat)
                evals_T = np.linalg.eigvals(D_T_mat)

            gap_K[j, i] = extract_gap(evals_K)
            gap_T[j, i] = extract_gap(evals_T)

            # Avoid division by zero
            if gap_K[j, i] > 1e-15:
                gap_ratio[j, i] = gap_T[j, i] / gap_K[j, i]
            else:
                gap_ratio[j, i] = np.nan

            # Store spectra for plotting
            if i in plot_tau_indices:
                spectra_K[(j, i)] = np.sort(np.abs(evals_K.imag))[:20]
                spectra_T[(j, i)] = np.sort(np.abs(evals_T.imag))[:20]

        dt = time.time() - t_iter
        print(f"  tau={tau:.4f}: C1={c1_err:.2e}, C2={c2_err:.2e}, "
              f"gaps_K={[f'{gap_K[j,i]:.4f}' for j in range(n_sec)]}, "
              f"gaps_T={[f'{gap_T[j,i]:.4f}' for j in range(n_sec)]}, "
              f"dt={dt:.2f}s")

    total_time = time.time() - t_start
    print(f"\nTotal computation time: {total_time:.1f}s")

    # =========================================================================
    # CROSS-CHECK VALIDATION
    # =========================================================================
    print("\n" + "=" * 72)
    print("CROSS-CHECK VALIDATION")
    print("=" * 72)

    c1_max = np.max(c1_errors)
    c2_max = np.max(c2_errors)
    c3_max = np.max(c3_errors)

    c1_pass = c1_max < 1e-12
    c2_pass = c2_max < 1e-12
    c3_pass = c3_max < 1e-10  # slightly relaxed for eigenvalue accumulation

    print(f"  C1 (K = -Gamma_LC):      max error = {c1_max:.2e}  {'PASS' if c1_pass else 'FAIL'}")
    print(f"  C2 (Omega_T = -Omega_LC): max error = {c2_max:.2e}  {'PASS' if c2_pass else 'FAIL'}")
    print(f"  C3 (D_can = M_Lie):       max error = {c3_max:.2e}  {'PASS' if c3_pass else 'FAIL'}")

    if not (c1_pass and c2_pass and c3_pass):
        print("\n  *** CROSS-CHECK FAILURE: Results are UNRELIABLE ***")
        # Print details
        if not c1_pass:
            worst_tau = tau_values[np.argmax(c1_errors)]
            print(f"      C1 worst at tau={worst_tau:.4f}")
        if not c2_pass:
            worst_tau = tau_values[np.argmax(c2_errors)]
            print(f"      C2 worst at tau={worst_tau:.4f}")
        if not c3_pass:
            worst_idx = np.unravel_index(np.argmax(c3_errors), c3_errors.shape)
            print(f"      C3 worst at sector {sector_labels[worst_idx[0]]}, tau={tau_values[worst_idx[1]]:.4f}")

    all_checks_pass = c1_pass and c2_pass and c3_pass

    # =========================================================================
    # GATE VERDICT
    # =========================================================================
    print("\n" + "=" * 72)
    print("GATE T-1: TORSION GAP WEAKENING")
    print("=" * 72)

    # Analyze non-trivial sectors only (exclude singlet)
    nontrivial_mask = [j for j, (p, q) in enumerate(sectors) if not (p == 0 and q == 0)]

    any_weakening = False
    for j in nontrivial_mask:
        p, q = sectors[j]
        label = sector_labels[j]

        # Find tau values where gap_T < gap_K
        weakening = gap_T[j, :] < gap_K[j, :] - 1e-12  # tolerance for numerics
        n_weak = np.sum(weakening)

        if n_weak > 0:
            any_weakening = True
            max_reduction = np.max(gap_K[j, :] - gap_T[j, :])
            min_ratio = np.nanmin(gap_ratio[j, :])
            worst_tau = tau_values[np.argmin(gap_ratio[j, :])]
            print(f"  {label}: gap_T < gap_K at {n_weak}/{n_tau} tau values")
            print(f"          max reduction = {max_reduction:.6f}")
            print(f"          min ratio gap_T/gap_K = {min_ratio:.4f} at tau={worst_tau:.4f}")
        else:
            # Check if gaps are equal everywhere
            max_diff = np.max(np.abs(gap_T[j, :] - gap_K[j, :]))
            print(f"  {label}: gap_T >= gap_K everywhere (max |diff| = {max_diff:.2e})")

    # Singlet analysis (informational)
    j_singlet = 0
    print(f"\n  (0,0) singlet (informational, excluded from gate):")
    print(f"          gap_K range: [{np.min(gap_K[0,:]):.4f}, {np.max(gap_K[0,:]):.4f}]")
    print(f"          gap_T = 0 at all tau (M_Lie = 0 for trivial rep)")

    # Detailed table
    print("\n  Detailed gap table (non-trivial sectors):")
    print(f"  {'tau':>6s} ", end="")
    for j in nontrivial_mask:
        label = sector_labels[j]
        print(f" | {label:>8s}_K {label:>8s}_T  ratio", end="")
    print()
    print("  " + "-" * (8 + len(nontrivial_mask) * 32))

    for i in range(n_tau):
        print(f"  {tau_values[i]:6.4f} ", end="")
        for j in nontrivial_mask:
            r = gap_ratio[j, i]
            r_str = f"{r:.4f}" if not np.isnan(r) else "   NaN"
            print(f" | {gap_K[j,i]:8.5f} {gap_T[j,i]:8.5f} {r_str}", end="")
        print()

    # Final verdict
    print("\n" + "=" * 72)
    if not all_checks_pass:
        verdict = "INCONCLUSIVE (cross-checks failed)"
    elif any_weakening:
        verdict = "PASS"
    else:
        verdict = "CLOSED"

    print(f"  GATE T-1 VERDICT: {verdict}")
    if any_weakening:
        print("  Torsion (canonical connection) WEAKENS the spectral gap.")
        print("  BCS prerequisite: gap weakening confirmed.")
    else:
        print("  Torsion does NOT weaken the spectral gap.")
        print("  BCS prerequisite: gap weakening absent.")
    print("=" * 72)

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    outfile = os.path.join(OUTDIR, "s27_torsion_gap_gate.npz")
    np.savez(outfile,
             tau_values=tau_values,
             sectors=np.array(sectors),
             sector_labels=np.array(sector_labels),
             gap_K=gap_K,
             gap_T=gap_T,
             gap_ratio=gap_ratio,
             c1_errors=c1_errors,
             c2_errors=c2_errors,
             c3_errors=c3_errors,
             verdict=verdict)
    print(f"\nData saved to: {outfile}")

    # =========================================================================
    # PLOT
    # =========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("T-1 Torsion Gap Gate: D_K vs D_canonical", fontsize=14, fontweight='bold')

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    # Panel 1: Gaps vs tau
    ax = axes[0, 0]
    for j in nontrivial_mask:
        ax.plot(tau_values, gap_K[j, :], '-', color=colors[j], linewidth=2,
                label=f'{sector_labels[j]} D_K')
        ax.plot(tau_values, gap_T[j, :], '--', color=colors[j], linewidth=2,
                label=f'{sector_labels[j]} D_can')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Spectral gap')
    ax.set_title('Gap comparison: D_K (solid) vs D_canonical (dashed)')
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 2: Gap ratio vs tau
    ax = axes[0, 1]
    for j in nontrivial_mask:
        ax.plot(tau_values, gap_ratio[j, :], '-o', color=colors[j],
                linewidth=2, markersize=3, label=sector_labels[j])
    ax.axhline(y=1.0, color='black', linestyle=':', linewidth=1, alpha=0.5)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'gap$_T$ / gap$_K$')
    ax.set_title('Gap ratio (< 1 = torsion weakens gap)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Cross-check errors
    ax = axes[1, 0]
    ax.semilogy(tau_values, c1_errors, 'b-o', markersize=3, label='C1: ||K + Gamma_LC||')
    ax.semilogy(tau_values, c2_errors, 'r-s', markersize=3, label='C2: ||Omega_T + Omega_LC||')
    c3_max_per_tau = np.max(c3_errors[1:, :], axis=0)  # max over non-trivial sectors
    ax.semilogy(tau_values, c3_max_per_tau, 'g-^', markersize=3, label='C3: max ||D_can - M_Lie||')
    ax.axhline(y=1e-12, color='gray', linestyle='--', alpha=0.5, label='tolerance')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Max error')
    ax.set_title('Cross-check validation')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 4: Low-lying spectra at selected tau values
    ax = axes[1, 1]
    j_show = 1  # (1,0) sector
    n_show = min(10, 20)
    tau_show_indices = [0, 10, 20]  # tau = 0, 0.25, 0.50
    offsets = [0, 0.35, 0.7]
    for k, ti in enumerate(tau_show_indices):
        if (j_show, ti) in spectra_K and (j_show, ti) in spectra_T:
            sK = spectra_K[(j_show, ti)][:n_show]
            sT = spectra_T[(j_show, ti)][:n_show]
            x_K = np.full_like(sK, offsets[k])
            x_T = np.full_like(sT, offsets[k] + 0.15)
            ax.scatter(x_K, sK, c='blue', s=20, marker='_', linewidths=2, zorder=5)
            ax.scatter(x_T, sT, c='red', s=20, marker='_', linewidths=2, zorder=5)
            ax.text(offsets[k] + 0.075, -0.15, f'tau={tau_values[ti]:.2f}',
                    ha='center', fontsize=8)
    # Manual legend
    ax.scatter([], [], c='blue', marker='_', linewidths=2, label='D_K')
    ax.scatter([], [], c='red', marker='_', linewidths=2, label='D_canonical')
    ax.set_xlim(-0.1, 1.0)
    ax.set_ylabel('|eigenvalue|')
    ax.set_title(f'Low-lying spectrum, sector {sector_labels[j_show]}')
    ax.set_xticks([])
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plotfile = os.path.join(OUTDIR, "s27_torsion_gap_gate.png")
    plt.savefig(plotfile, dpi=150, bbox_inches='tight')
    print(f"Plot saved to: {plotfile}")
    plt.close()

    return verdict, all_checks_pass


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == '__main__':
    verdict, checks_ok = run_torsion_gap_gate()
    print(f"\nFinal: verdict={verdict}, all_checks_pass={checks_ok}")
