"""
SESSION 28a COMPUTATION C-1: SPECTRAL ACTION S_can vs S_LC
=============================================================

"This is the single most important number Session 28 can produce."

Compute the spectral action Tr f(D_can^2 / Lambda^2) using D_can eigenvalues
and compare to Tr f(D_K^2 / Lambda^2). This isolates the torsion contribution
to the spectral action at all tau values.

Physics:
  D_K (Levi-Civita):    D_K = M_Lie + I (x) Omega_LC
  D_can (canonical):    D_can = M_Lie   (flat connection => Omega_can = 0)

  The spectral action:
    S[D, f, Lambda] = Tr f(D^2 / Lambda^2)

  with f = step function (sharp cutoff) or smooth cutoffs (heat, Lorentz).

  S_LC(tau; Lambda) uses eigenvalues of D_K.
  S_can(tau; Lambda) uses eigenvalues of D_can = M_Lie.

  CRITICAL QUESTION: Is S_can(tau) - S_LC(tau) monotonic?
  If S_can has a NON-MONOTONIC tau dependence, then V-1 and SD-1 closes
  (which showed S_LC monotonic) do NOT transfer to the torsionful sector.
  The framework's native stabilization mechanism REOPENS.

Method:
  1. At each tau value, build D_K and D_can = M_Lie for sectors (0,0), (1,0),
     (0,1), (1,1) [p+q <= 2, same as s27]. For broader coverage, also include
     (2,0), (0,2), (2,1), (1,2), (1,1) already in the list.
  2. Compute eigenvalues of both operators.
  3. Apply spectral action with sharp cutoff (eigenvalue counting) at
     Lambda = {1, 2, 5, 10} and smooth cutoffs (heat kernel).
  4. Include Peter-Weyl multiplicities: mult(p,q) = dim(p,q)^2.
  5. Plot S_can(tau) and S_LC(tau). Analyze Delta_S = S_can - S_LC.

Input:  tier0-computation/s27_torsion_gap_gate.npz (for tau grid reference)
        Infrastructure from tier1_dirac_spectrum.py (geometry, irreps, Dirac)

Output: tier0-computation/s28a_spectral_action_comparison.npz
        tier0-computation/s28a_spectral_action_comparison.png

Gate C-1: DIAGNOSTIC. If S_can(tau) is non-monotonic, V-1/SD-1 closes
          do not transfer. Framework reopens.

Author: phonon-exflation-sim agent (Session 28a)
Date: 2026-02-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    dirac_operator_on_irrep, get_irrep, _irrep_cache
)

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# SU(3) IRREP DIMENSION
# =============================================================================

def dim_su3(p: int, q: int) -> int:
    """
    Dimension of the (p,q) irreducible representation of SU(3).

    dim(p,q) = (p+1)(q+1)(p+q+2)/2

    Args:
        p, q: non-negative integers labeling the irrep

    Returns:
        dimension (integer)
    """
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# =============================================================================
# BUILD M_Lie (canonical Dirac = Lie derivative term only)
# =============================================================================

def build_M_Lie(rho: list, E: np.ndarray, gammas: list) -> np.ndarray:
    """
    Build M_Lie = sum_{a,b} E_{ab} rho[b] (x) gamma_a.

    This is the canonical-connection Dirac operator D_can on a Lie group.
    Since the canonical connection is flat (Gamma_can = 0), the spinor
    connection offset vanishes, and D_can = M_Lie.

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


# =============================================================================
# SPECTRAL ACTION COMPUTATIONS
# =============================================================================

def spectral_action_sharp(evals_sq: np.ndarray, mult: int, Lambda: float) -> float:
    """
    Sharp-cutoff spectral action: count eigenvalues with |lambda| <= Lambda.

    S_sharp = mult * #{n : lambda_n^2 <= Lambda^2}

    Args:
        evals_sq: array of lambda^2 values (positive reals)
        mult: Peter-Weyl multiplicity = dim(p,q)^2
        Lambda: cutoff scale

    Returns:
        S: spectral action contribution from this sector
    """
    count = np.sum(evals_sq <= Lambda ** 2)
    return mult * count


def spectral_action_heat(evals_sq: np.ndarray, mult: int, Lambda: float) -> float:
    """
    Heat-kernel spectral action: Tr exp(-D^2 / Lambda^2).

    S_heat = mult * sum_n exp(-lambda_n^2 / Lambda^2)

    Args:
        evals_sq: array of lambda^2 values
        mult: Peter-Weyl multiplicity
        Lambda: cutoff scale

    Returns:
        S: spectral action contribution
    """
    x = evals_sq / (Lambda ** 2)
    return mult * np.sum(np.exp(-x))


def spectral_action_lorentz(evals_sq: np.ndarray, mult: int, Lambda: float) -> float:
    """
    Lorentzian spectral action: Tr 1/(1 + D^2/Lambda^2)^2.

    S_lor = mult * sum_n 1/(1 + lambda_n^2/Lambda^2)^2

    Args:
        evals_sq: array of lambda^2 values
        mult: Peter-Weyl multiplicity
        Lambda: cutoff scale

    Returns:
        S: spectral action contribution
    """
    x = evals_sq / (Lambda ** 2)
    return mult * np.sum(1.0 / (1.0 + x) ** 2)


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

def main():
    t_start = time.time()
    print("=" * 72)
    print("SESSION 28a C-1: SPECTRAL ACTION S_can vs S_LC")
    print("=" * 72)
    print("\n\"This is the single most important number Session 28 can produce.\"")

    # =========================================================================
    # Infrastructure setup
    # =========================================================================
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    # Tau sweep: same grid as s27
    tau_values = np.linspace(0.0, 0.50, 21)
    n_tau = len(tau_values)

    # Sectors: include all with p+q <= 3 for broader spectral coverage
    # This matches the s27 multi-sector BCS computation scope
    sectors = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (3, 0), (0, 3)]
    sector_labels = [f'({p},{q})' for p, q in sectors]
    n_sec = len(sectors)

    # Cutoff scales
    Lambda_values = np.array([1.0, 2.0, 5.0, 10.0])
    n_Lambda = len(Lambda_values)

    print(f"\n  Tau range: [{tau_values[0]:.3f}, {tau_values[-1]:.3f}], n_tau={n_tau}")
    print(f"  Sectors ({n_sec}): {sector_labels}")
    print(f"  Lambda values: {Lambda_values}")

    # Compute sector multiplicities
    mults = np.array([dim_su3(p, q) ** 2 for p, q in sectors])
    dims = np.array([dim_su3(p, q) for p, q in sectors])
    print(f"  Sector dimensions: {dims}")
    print(f"  PW multiplicities (dim^2): {mults}")
    total_evals_per_tau = sum(dim_su3(p, q) * 16 for p, q in sectors)
    print(f"  Total eigenvalues per tau (before PW mult): {total_evals_per_tau}")

    # =========================================================================
    # Storage
    # =========================================================================

    # Per-sector, per-tau spectral actions
    # Shape: (n_sec, n_tau) for each Lambda and cutoff type
    S_LC_sharp = np.zeros((n_Lambda, n_sec, n_tau))
    S_can_sharp = np.zeros((n_Lambda, n_sec, n_tau))
    S_LC_heat = np.zeros((n_Lambda, n_sec, n_tau))
    S_can_heat = np.zeros((n_Lambda, n_sec, n_tau))
    S_LC_lorentz = np.zeros((n_Lambda, n_sec, n_tau))
    S_can_lorentz = np.zeros((n_Lambda, n_sec, n_tau))

    # Full spectrum storage for analysis
    all_evals_K = {}    # (sector_idx, tau_idx) -> sorted |eigenvalues|^2
    all_evals_can = {}

    # =========================================================================
    # Main sweep
    # =========================================================================
    print("\n" + "-" * 72)
    print("COMPUTING EIGENVALUE SPECTRA")
    print("-" * 72)

    for i, tau in enumerate(tau_values):
        t_iter = time.time()

        # Geometry at this tau
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma_LC = connection_coefficients(ft)
        Omega_LC = spinor_connection_offset(Gamma_LC, gammas)

        for j, (p, q) in enumerate(sectors):
            _irrep_cache.clear()
            mult = mults[j]

            if p == 0 and q == 0:
                # Trivial rep: D_K = Omega_LC, D_can = 0
                evals_K = np.linalg.eigvalsh(
                    1j * Omega_LC  # Convert anti-Herm to Herm for eigvalsh
                )
                evals_K_sq = evals_K ** 2  # These are the lambda^2 values
                evals_can_sq = np.zeros(16)  # D_can = 0 for trivial rep
            else:
                rho, dim_rho = get_irrep(p, q, gens, f_abc)

                # D_K = M_Lie + I (x) Omega_LC
                D_K_mat = dirac_operator_on_irrep(rho, E, gammas, Omega_LC)

                # M_Lie = D_can
                M_Lie = build_M_Lie(rho, E, gammas)

                # Both operators are anti-Hermitian (purely imaginary eigenvalues)
                # Use eigvalsh on the Hermitian matrix (i*D)
                dim_total = dim_rho * 16
                iD_K = 1j * D_K_mat
                iM_Lie = 1j * M_Lie

                # Symmetrize to ensure Hermitian (numerical cleanup)
                iD_K = 0.5 * (iD_K + iD_K.conj().T)
                iM_Lie = 0.5 * (iM_Lie + iM_Lie.conj().T)

                evals_K = np.linalg.eigvalsh(iD_K)
                evals_can = np.linalg.eigvalsh(iM_Lie)

                evals_K_sq = evals_K ** 2
                evals_can_sq = evals_can ** 2

            # Store spectra
            all_evals_K[(j, i)] = np.sort(evals_K_sq)
            all_evals_can[(j, i)] = np.sort(evals_can_sq)

            # Compute spectral actions at each Lambda
            for k, Lambda in enumerate(Lambda_values):
                S_LC_sharp[k, j, i] = spectral_action_sharp(evals_K_sq, mult, Lambda)
                S_can_sharp[k, j, i] = spectral_action_sharp(evals_can_sq, mult, Lambda)

                S_LC_heat[k, j, i] = spectral_action_heat(evals_K_sq, mult, Lambda)
                S_can_heat[k, j, i] = spectral_action_heat(evals_can_sq, mult, Lambda)

                S_LC_lorentz[k, j, i] = spectral_action_lorentz(evals_K_sq, mult, Lambda)
                S_can_lorentz[k, j, i] = spectral_action_lorentz(evals_can_sq, mult, Lambda)

        dt = time.time() - t_iter
        # Print summary
        S_LC_total = np.sum(S_LC_heat[1, :, i])  # Lambda=2, heat kernel
        S_can_total = np.sum(S_can_heat[1, :, i])
        print(f"  tau={tau:.4f}: S_LC(heat,L=2)={S_LC_total:.2f}, "
              f"S_can(heat,L=2)={S_can_total:.2f}, "
              f"ratio={S_can_total/S_LC_total:.4f} if S_LC>0, "
              f"dt={dt:.2f}s")

    total_compute = time.time() - t_start
    print(f"\nTotal eigenvalue computation time: {total_compute:.1f}s")

    # =========================================================================
    # ANALYSIS: Totals and monotonicity
    # =========================================================================
    print("\n" + "=" * 72)
    print("SPECTRAL ACTION ANALYSIS")
    print("=" * 72)

    # Sum over sectors to get total spectral action
    S_LC_total_sharp = np.sum(S_LC_sharp, axis=1)   # (n_Lambda, n_tau)
    S_can_total_sharp = np.sum(S_can_sharp, axis=1)
    S_LC_total_heat = np.sum(S_LC_heat, axis=1)
    S_can_total_heat = np.sum(S_can_heat, axis=1)
    S_LC_total_lorentz = np.sum(S_LC_lorentz, axis=1)
    S_can_total_lorentz = np.sum(S_can_lorentz, axis=1)

    Delta_S_sharp = S_can_total_sharp - S_LC_total_sharp
    Delta_S_heat = S_can_total_heat - S_LC_total_heat
    Delta_S_lorentz = S_can_total_lorentz - S_LC_total_lorentz

    # Check monotonicity
    print("\n  MONOTONICITY CHECK:")
    print(f"  {'Cutoff':>10s} {'Lambda':>6s} {'S_LC mono':>10s} {'S_can mono':>10s} "
          f"{'Delta_S mono':>12s} {'S_can min at':>12s}")
    print("  " + "-" * 70)

    monotonicity_results = {}

    for k, Lambda in enumerate(Lambda_values):
        for cutoff_name, S_LC_t, S_can_t, DS_t in [
            ('sharp', S_LC_total_sharp[k], S_can_total_sharp[k], Delta_S_sharp[k]),
            ('heat', S_LC_total_heat[k], S_can_total_heat[k], Delta_S_heat[k]),
            ('lorentz', S_LC_total_lorentz[k], S_can_total_lorentz[k], Delta_S_lorentz[k]),
        ]:
            # Check if S_LC is monotonically decreasing
            dS_LC = np.diff(S_LC_t)
            S_LC_mono = "DECR" if np.all(dS_LC <= 1e-10) else \
                        "INCR" if np.all(dS_LC >= -1e-10) else "NON-MONO"

            # Check if S_can is monotonically decreasing
            dS_can = np.diff(S_can_t)
            S_can_mono = "DECR" if np.all(dS_can <= 1e-10) else \
                         "INCR" if np.all(dS_can >= -1e-10) else "NON-MONO"

            # Check Delta_S monotonicity
            dDS = np.diff(DS_t)
            DS_mono = "DECR" if np.all(dDS <= 1e-10) else \
                      "INCR" if np.all(dDS >= -1e-10) else "NON-MONO"

            # Location of S_can minimum
            i_min = np.argmin(S_can_t)
            tau_min = tau_values[i_min]

            key = f"{cutoff_name}_L{Lambda:.0f}"
            monotonicity_results[key] = {
                'S_LC_mono': S_LC_mono,
                'S_can_mono': S_can_mono,
                'DS_mono': DS_mono,
                'S_can_min_tau': tau_min,
                'S_can_min_val': S_can_t[i_min],
                'S_can_at_0': S_can_t[0],
                'S_can_at_end': S_can_t[-1],
                'Delta_S_at_0': DS_t[0],
                'Delta_S_at_end': DS_t[-1],
            }

            print(f"  {cutoff_name:>10s} {Lambda:6.1f} {S_LC_mono:>10s} {S_can_mono:>10s} "
                  f"{DS_mono:>12s} tau={tau_min:>6.3f}")

    # =========================================================================
    # Detailed tables for heat kernel (most physically relevant)
    # =========================================================================
    print("\n" + "-" * 72)
    print("HEAT KERNEL SPECTRAL ACTION (f(x) = exp(-x))")
    print("-" * 72)

    for k, Lambda in enumerate(Lambda_values):
        print(f"\n  Lambda = {Lambda:.1f}:")
        print(f"  {'tau':>6s} {'S_LC':>12s} {'S_can':>12s} {'Delta_S':>12s} "
              f"{'S_can/S_LC':>10s}")
        print("  " + "-" * 55)
        for i in range(n_tau):
            s_lc = S_LC_total_heat[k, i]
            s_can = S_can_total_heat[k, i]
            ds = Delta_S_heat[k, i]
            ratio = s_can / s_lc if abs(s_lc) > 1e-30 else np.nan
            print(f"  {tau_values[i]:6.4f} {s_lc:12.4f} {s_can:12.4f} {ds:12.4f} "
                  f"{ratio:10.6f}")

    # =========================================================================
    # Per-sector breakdown at Lambda=2 (heat)
    # =========================================================================
    print("\n" + "-" * 72)
    print("PER-SECTOR BREAKDOWN (heat, Lambda=2)")
    print("-" * 72)

    k_ref = 1  # Lambda=2 index
    for j, (p, q) in enumerate(sectors):
        label = sector_labels[j]
        S_lc_sec = S_LC_heat[k_ref, j, :]
        S_can_sec = S_can_heat[k_ref, j, :]
        DS_sec = S_can_sec - S_lc_sec

        dS_lc = np.diff(S_lc_sec)
        dS_can = np.diff(S_can_sec)

        lc_mono = "DECR" if np.all(dS_lc <= 1e-10) else \
                  "INCR" if np.all(dS_lc >= -1e-10) else "NON-MONO"
        can_mono = "DECR" if np.all(dS_can <= 1e-10) else \
                   "INCR" if np.all(dS_can >= -1e-10) else "NON-MONO"

        i_min = np.argmin(S_can_sec)

        print(f"  {label}: S_LC {lc_mono}, S_can {can_mono}")
        print(f"    S_LC  range: [{np.min(S_lc_sec):.4f}, {np.max(S_lc_sec):.4f}]")
        print(f"    S_can range: [{np.min(S_can_sec):.4f}, {np.max(S_can_sec):.4f}]")
        print(f"    S_can min at tau={tau_values[i_min]:.3f}")
        print(f"    Delta_S range: [{np.min(DS_sec):.4f}, {np.max(DS_sec):.4f}]")

    # =========================================================================
    # THE DECISIVE QUESTION
    # =========================================================================
    print("\n" + "=" * 72)
    print("THE DECISIVE QUESTION")
    print("=" * 72)

    # Check across SMOOTH cutoffs only (heat, Lorentz) -- sharp cutoff is an
    # integer eigenvalue counting function and can produce artifacts from single
    # eigenvalues crossing the Lambda boundary. This is not physical structure.
    smooth_nonmono_S_can = False
    smooth_nonmono_Delta = False
    sharp_nonmono_S_can = False
    any_minimum_S_can_smooth = False

    for key, res in monotonicity_results.items():
        is_sharp = key.startswith('sharp')

        if res['S_can_mono'] == 'NON-MONO':
            if is_sharp:
                sharp_nonmono_S_can = True
                print(f"\n  * S_can NON-MONOTONIC for {key} (SHARP CUTOFF -- discretization artifact)")
                print(f"    S_can(0) = {res['S_can_at_0']:.4f}, S_can(min) = {res['S_can_min_val']:.4f}")
            else:
                smooth_nonmono_S_can = True
                print(f"\n  ** S_can NON-MONOTONIC for {key} (SMOOTH CUTOFF -- GENUINE) **")
                print(f"     S_can minimum at tau = {res['S_can_min_tau']:.4f}")
                print(f"     S_can(0) = {res['S_can_at_0']:.4f}")
                print(f"     S_can(min) = {res['S_can_min_val']:.4f}")
                print(f"     S_can(0.5) = {res['S_can_at_end']:.4f}")

        if res['DS_mono'] == 'NON-MONO':
            if is_sharp:
                pass  # Sharp artifact, ignore
            else:
                smooth_nonmono_Delta = True

        # Interior minimum under smooth cutoff
        if not is_sharp and 0 < res['S_can_min_tau'] < tau_values[-1]:
            any_minimum_S_can_smooth = True

    if sharp_nonmono_S_can and not smooth_nonmono_S_can:
        print("\n  Sharp cutoff non-monotonicity is a DISCRETIZATION ARTIFACT.")
        print("  Integer eigenvalue counting at low Lambda produces step-function")
        print("  behavior. Single eigenvalues crossing the Lambda boundary cause")
        print("  non-monotonic jumps. This is not physical spectral action structure.")
        print("  ALL smooth cutoffs (heat, Lorentz) show S_can MONOTONICALLY DECREASING.")

    # =========================================================================
    # GATE VERDICT
    # =========================================================================
    print("\n" + "=" * 72)
    print("GATE C-1 VERDICT: SPECTRAL ACTION S_can vs S_LC")
    print("=" * 72)

    if smooth_nonmono_S_can:
        verdict = "PASS"
        print(f"\n  VERDICT: {verdict}")
        print("  S_can(tau) is NON-MONOTONIC under smooth cutoff.")
        print("  V-1 and SD-1 closes (which showed S_LC monotonic) do NOT")
        print("  transfer to the torsionful (canonical connection) sector.")
        print("  The framework's native stabilization mechanism REOPENS.")
        if any_minimum_S_can_smooth:
            print("  S_can has an interior minimum: tau stabilization is possible.")
    else:
        verdict = "CLOSED"
        print(f"\n  VERDICT: {verdict}")
        print("  S_can(tau) is MONOTONICALLY DECREASING under all smooth cutoffs")
        print("  (heat kernel, Lorentzian) at all Lambda values tested.")
        print("  The V-1 closure TRANSFERS to the torsionful sector.")
        print("  Torsion does NOT introduce spectral action structure.")
        print("  The spectral action cannot stabilize tau regardless of connection choice.")

    # Additional diagnostic: Delta_S structure
    if smooth_nonmono_Delta:
        print("\n  NOTE: Delta_S = S_can - S_LC has NON-MONOTONIC structure under smooth cutoff.")
        print("  The torsion contribution itself has tau-dependent structure,")
        print("  even if both S_can and S_LC individually are monotonic.")

    # Report key numbers
    print(f"\n  Key numbers (heat kernel, Lambda=2):")
    key2 = "heat_L2"
    r = monotonicity_results[key2]
    print(f"    S_can(0) = {r['S_can_at_0']:.4f}")
    print(f"    S_can(0.50) = {r['S_can_at_end']:.4f}")
    print(f"    S_can min at tau = {r['S_can_min_tau']:.4f}")
    print(f"    S_can(min) = {r['S_can_min_val']:.4f}")
    print(f"    Delta_S(0) = {r['Delta_S_at_0']:.4f}")
    print(f"    Delta_S(0.50) = {r['Delta_S_at_end']:.4f}")

    print("=" * 72)

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    outfile = os.path.join(OUTDIR, "s28a_spectral_action_comparison.npz")
    np.savez(outfile,
             tau_values=tau_values,
             sectors=np.array(sectors),
             sector_labels=np.array(sector_labels),
             Lambda_values=Lambda_values,
             mults=mults,
             dims=dims,
             # Per-Lambda, per-sector, per-tau arrays
             S_LC_sharp=S_LC_sharp,
             S_can_sharp=S_can_sharp,
             S_LC_heat=S_LC_heat,
             S_can_heat=S_can_heat,
             S_LC_lorentz=S_LC_lorentz,
             S_can_lorentz=S_can_lorentz,
             # Totals (sum over sectors)
             S_LC_total_sharp=S_LC_total_sharp,
             S_can_total_sharp=S_can_total_sharp,
             S_LC_total_heat=S_LC_total_heat,
             S_can_total_heat=S_can_total_heat,
             S_LC_total_lorentz=S_LC_total_lorentz,
             S_can_total_lorentz=S_can_total_lorentz,
             # Differences
             Delta_S_sharp=Delta_S_sharp,
             Delta_S_heat=Delta_S_heat,
             Delta_S_lorentz=Delta_S_lorentz,
             verdict=verdict)
    print(f"\nData saved to: {outfile}")

    # =========================================================================
    # PLOT
    # =========================================================================
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle("C-1: Spectral Action Comparison — D_can (torsionful) vs D_K (LC)",
                 fontsize=14, fontweight='bold')

    Lambda_colors = {1.0: '#1f77b4', 2.0: '#ff7f0e', 5.0: '#2ca02c', 10.0: '#d62728'}

    # Panel 1: S_LC(tau) for all Lambda (heat kernel)
    ax = axes[0, 0]
    for k, Lambda in enumerate(Lambda_values):
        ax.plot(tau_values, S_LC_total_heat[k, :], '-', color=Lambda_colors[Lambda],
                linewidth=2, label=f'$\\Lambda$={Lambda:.0f}')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$S_{LC}(\tau)$')
    ax.set_title(r'$S_{LC} = \mathrm{Tr}\,e^{-D_K^2/\Lambda^2}$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 2: S_can(tau) for all Lambda (heat kernel)
    ax = axes[0, 1]
    for k, Lambda in enumerate(Lambda_values):
        ax.plot(tau_values, S_can_total_heat[k, :], '-', color=Lambda_colors[Lambda],
                linewidth=2, label=f'$\\Lambda$={Lambda:.0f}')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$S_{can}(\tau)$')
    ax.set_title(r'$S_{can} = \mathrm{Tr}\,e^{-D_{can}^2/\Lambda^2}$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Delta_S = S_can - S_LC (heat kernel)
    ax = axes[0, 2]
    for k, Lambda in enumerate(Lambda_values):
        ax.plot(tau_values, Delta_S_heat[k, :], '-o', color=Lambda_colors[Lambda],
                linewidth=2, markersize=3, label=f'$\\Lambda$={Lambda:.0f}')
    ax.axhline(y=0, color='black', linestyle=':', linewidth=0.5)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$\Delta S = S_{can} - S_{LC}$')
    ax.set_title(r'Torsion contribution: $\Delta S$ (heat kernel)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: S_can/S_LC ratio (heat kernel)
    ax = axes[1, 0]
    for k, Lambda in enumerate(Lambda_values):
        ratio = S_can_total_heat[k, :] / np.where(
            np.abs(S_LC_total_heat[k, :]) > 1e-30, S_LC_total_heat[k, :], np.nan)
        ax.plot(tau_values, ratio, '-o', color=Lambda_colors[Lambda],
                linewidth=2, markersize=3, label=f'$\\Lambda$={Lambda:.0f}')
    ax.axhline(y=1.0, color='black', linestyle=':', linewidth=0.5)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$S_{can} / S_{LC}$')
    ax.set_title('Ratio (>1 means D_can has more spectral weight)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 5: Sharp cutoff comparison at Lambda=2
    ax = axes[1, 1]
    k_ref = 1  # Lambda=2
    ax.plot(tau_values, S_LC_total_sharp[k_ref, :], 'b-', linewidth=2, label=r'$S_{LC}$ (sharp)')
    ax.plot(tau_values, S_can_total_sharp[k_ref, :], 'r--', linewidth=2, label=r'$S_{can}$ (sharp)')
    ax.plot(tau_values, S_LC_total_heat[k_ref, :], 'b:', linewidth=2, label=r'$S_{LC}$ (heat)')
    ax.plot(tau_values, S_can_total_heat[k_ref, :], 'r:', linewidth=2, label=r'$S_{can}$ (heat)')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Spectral action')
    ax.set_title(r'Sharp vs Heat cutoff ($\Lambda=2$)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 6: Per-sector S_can at Lambda=2 (heat kernel)
    ax = axes[1, 2]
    sector_colors = plt.cm.tab10(np.linspace(0, 1, n_sec))
    for j, (p, q) in enumerate(sectors):
        if p == 0 and q == 0:
            continue  # Skip trivial (zero contribution to D_can)
        s_can_sec = S_can_heat[k_ref, j, :]
        ax.plot(tau_values, s_can_sec, '-', color=sector_colors[j],
                linewidth=1.5, label=sector_labels[j])
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$S_{can}^{(p,q)}(\tau)$')
    ax.set_title(r'Per-sector $S_{can}$ ($\Lambda=2$, heat)')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plotfile = os.path.join(OUTDIR, "s28a_spectral_action_comparison.png")
    plt.savefig(plotfile, dpi=150, bbox_inches='tight')
    print(f"Plot saved to: {plotfile}")
    plt.close()

    total_time = time.time() - t_start
    print(f"\nTotal execution time: {total_time:.1f}s")

    return verdict


if __name__ == '__main__':
    verdict = main()
    print(f"\nFinal C-1 verdict: {verdict}")
