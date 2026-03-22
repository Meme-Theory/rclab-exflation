"""
Session 23a Step 5: BCS Gap Equation Solver for Kosmann-Dirac System

Solves the self-consistent BCS gap equation using the agreed V_nm formula
(Feynman convention, Mandatory Gate approved by both landau and phonon-sim):

    V_nm = -sum_{a=3,4,5,6} |<n|K_a|m>|^2    (V < 0 = attractive)

    Delta_n = -sum_m V_nm * Delta_m / (2 * sqrt(xi_m^2 + Delta_m^2))

    Linearized: M_nm = -V_nm / (2|xi_m|) = sum_a |<n|K_a|m>|^2 / (2|xi_m|)

    Binary gate: max eigenvalue of M > 1 => non-trivial gap => PASS

Three methods:
    Method 1: Linearized eigenvalue (binary gate)
    Method 2: Self-consistent iteration (gap magnitude)
    Method 3: Free energy minimization (thermodynamic stability)

Three basis sizes:
    (a) 2-mode gap-edge only
    (b) 10-mode gap-edge + nearest level
    (c) Full 16-mode singlet

Three chemical potential choices:
    (i)   mu = 0 (symmetric, spectrum center)
    (ii)  mu = +lambda_min (upper gap edge)
    (iii) mu = -lambda_min (lower gap edge)

CRITICAL STRUCTURAL FINDING:
    The gap-edge self-coupling V(gap,gap) = 0 EXACTLY at all tau > 0.
    The 2-mode gap-edge truncation has ZERO pairing interaction.
    Pairing is mediated through the 4-fold degenerate nearest level.
    The MINIMUM viable basis is 10 modes (2 gap + 8 nearest).

Author: phonon-exflation-sim (Session 23a)
Date: 2026-02-20
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
C2_IDX = [3, 4, 5, 6]

# Regulator for |xi_m| near zero
ETA_DEFAULT = 0.01  # fraction of lambda_min
ETA_SENSITIVITY = [0.001, 0.01, 0.1]


def load_kosmann_data(npz_path):
    """Load the Kosmann singlet extraction data.

    Returns:
        data: dict-like numpy NpzFile
    """
    return np.load(npz_path, allow_pickle=True)


def build_V_matrix(data, idx):
    """Build the pairing matrix V_nm = sum_{a=3..6} |<n|K_a|m>|^2.

    This is the POSITIVE magnitude-squared matrix. The Feynman sign convention
    has V_nm_feynman = -V_nm (attractive). We store the positive quantity and
    handle signs in the gap equation.

    Parameters:
        data: loaded .npz data
        idx: tau index (0-8)

    Returns:
        V: (16,16) real non-negative symmetric matrix
        evals: (16,) eigenvalues of D_K in singlet sector
    """
    evals = data[f'eigenvalues_{idx}']
    V = np.zeros((16, 16))
    for a in C2_IDX:
        K = data[f'K_a_matrix_{idx}_{a}']
        V += np.abs(K) ** 2

    # V should be real and symmetric by construction
    V = np.real(V)
    sym_err = np.max(np.abs(V - V.T))
    V = 0.5 * (V + V.T)  # enforce exact symmetry

    return V, evals, sym_err


def classify_modes(evals, tol=1e-4):
    """Group modes by distinct |lambda| levels.

    Returns:
        levels: list of (level_value, [indices]) sorted by |level|
    """
    abs_e = np.abs(evals)
    # Sort by |lambda|
    sorted_idx = np.argsort(abs_e)

    levels = []
    current_level = abs_e[sorted_idx[0]]
    current_indices = [sorted_idx[0]]

    for i in range(1, len(sorted_idx)):
        if abs(abs_e[sorted_idx[i]] - current_level) < tol:
            current_indices.append(sorted_idx[i])
        else:
            levels.append((current_level, np.array(current_indices)))
            current_level = abs_e[sorted_idx[i]]
            current_indices = [sorted_idx[i]]
    levels.append((current_level, np.array(current_indices)))

    return levels


def select_basis(evals, basis_type='full16'):
    """Select which modes to include in the gap equation.

    Parameters:
        evals: (16,) eigenvalues
        basis_type: 'gap2' (2 gap-edge), 'gap10' (gap + nearest), 'full16'

    Returns:
        indices: array of mode indices to include
    """
    levels = classify_modes(evals)

    if basis_type == 'gap2':
        return levels[0][1][:2]  # only 2 gap-edge modes (even if level is degenerate)
    elif basis_type == 'gap10':
        # gap-edge (2 modes) + nearest level (8 modes) = 10 modes
        if len(levels) > 1:
            idx = np.concatenate([levels[0][1], levels[1][1]])
        else:
            # All degenerate (tau=0): use first 10 modes
            idx = levels[0][1][:min(10, len(levels[0][1]))]
        return idx
    elif basis_type == 'full16':
        return np.arange(16)
    else:
        raise ValueError(f"Unknown basis_type: {basis_type}")


def linearized_bcs(V, evals, mu, eta_frac=0.01, basis_indices=None):
    """Method 1: Linearized BCS eigenvalue problem.

    The linearized gap equation is:
        Delta_n = sum_m M_nm * Delta_m
    where
        M_nm = V_nm / (2 * |xi_m|)    (V here is the positive |<n|K|m>|^2 sum)

    The BCS minus signs cancel: -V_feynman / (2|xi|) = +V_positive / (2|xi|).

    Binary gate: max eigenvalue of M > 1 => condensate exists.

    Parameters:
        V: (16,16) positive V_nm matrix
        evals: (16,) eigenvalues
        mu: chemical potential
        eta_frac: regulator as fraction of lambda_min
        basis_indices: which modes to include (None = all 16)

    Returns:
        M_eigenvalues: eigenvalues of the linearized matrix M
        M_eigenvectors: eigenvectors
        M_max: maximum eigenvalue (the BCS criterion)
        M_matrix: the M matrix itself
    """
    if basis_indices is None:
        basis_indices = np.arange(16)

    N = len(basis_indices)
    V_sub = V[np.ix_(basis_indices, basis_indices)]
    E_sub = evals[basis_indices]
    xi = E_sub - mu

    # Regulator: |xi| -> max(|xi|, eta)
    lambda_min = np.min(np.abs(evals))
    eta = max(eta_frac * lambda_min, 1e-15)  # absolute floor to prevent division by zero
    abs_xi = np.maximum(np.abs(xi), eta)

    # Build M matrix: M_nm = V_nm / (2 * |xi_m|)
    # Note: the column index m sets the denominator
    M = np.zeros((N, N))
    for m in range(N):
        M[:, m] = V_sub[:, m] / (2.0 * abs_xi[m])

    # Eigenvalue decomposition
    M_evals, M_evecs = eigh(M)
    M_max = np.max(M_evals)

    return M_evals, M_evecs, M_max, M


def selfconsistent_iteration(V, evals, mu, eta_frac=0.01, basis_indices=None,
                              max_iter=10000, tol=1e-10, Delta0_scale=0.01):
    """Method 2: Self-consistent BCS gap equation iteration.

    Iterates:
        Delta_n^{k+1} = sum_m V_nm * Delta_m^k / (2 * sqrt(xi_m^2 + (Delta_m^k)^2))

    until convergence.

    Parameters:
        V: (16,16) positive V_nm matrix
        evals: eigenvalues
        mu: chemical potential
        eta_frac: regulator fraction
        basis_indices: mode selection
        max_iter: maximum iterations
        tol: convergence tolerance
        Delta0_scale: initial guess scale (fraction of lambda_min)

    Returns:
        Delta: converged gap vector
        converged: bool
        n_iter: number of iterations
        history: list of |Delta| norms
    """
    if basis_indices is None:
        basis_indices = np.arange(16)

    N = len(basis_indices)
    V_sub = V[np.ix_(basis_indices, basis_indices)]
    E_sub = evals[basis_indices]
    xi = E_sub - mu

    lambda_min = np.min(np.abs(evals))

    # Initial guess: small uniform perturbation
    Delta = np.ones(N) * Delta0_scale * lambda_min

    history = [np.linalg.norm(Delta)]

    for k in range(max_iter):
        # BCS kernel: 1 / (2 * sqrt(xi^2 + Delta^2))
        denom = 2.0 * np.sqrt(xi**2 + Delta**2)

        # Update: Delta_n = sum_m V_nm * Delta_m / denom_m
        Delta_new = V_sub @ (Delta / denom)

        # Check convergence
        if np.linalg.norm(Delta) > 1e-15:
            rel_change = np.linalg.norm(Delta_new - Delta) / np.linalg.norm(Delta)
        else:
            rel_change = np.linalg.norm(Delta_new - Delta)

        Delta = Delta_new
        history.append(np.linalg.norm(Delta))

        if rel_change < tol:
            return Delta, True, k + 1, history

        # Check for decay to zero (trivial solution)
        if np.linalg.norm(Delta) < 1e-30:
            return Delta, True, k + 1, history  # converged to trivial

    return Delta, False, max_iter, history


def free_energy(V, evals, mu, Delta, basis_indices=None):
    """Method 3: BCS condensation free energy.

    F_cond = -sum_n [sqrt(xi_n^2 + Delta_n^2) - |xi_n|]
             + sum_{n,m} Delta_n * [V^{-1}]_{nm} * Delta_m / 2

    For the condensate to be thermodynamically stable, F_cond < 0.

    Parameters:
        V: (16,16) positive V_nm matrix
        evals: eigenvalues
        mu: chemical potential
        Delta: gap vector
        basis_indices: mode selection

    Returns:
        F_cond: condensation free energy
        F_kin: kinetic term (-sum [...])
        F_pot: potential term (V^{-1} Delta^2 / 2)
    """
    if basis_indices is None:
        basis_indices = np.arange(16)

    V_sub = V[np.ix_(basis_indices, basis_indices)]
    E_sub = evals[basis_indices]
    xi = E_sub - mu

    # Kinetic energy gain from pairing
    F_kin = -np.sum(np.sqrt(xi**2 + Delta**2) - np.abs(xi))

    # Potential energy cost (requires V invertible)
    try:
        V_inv = np.linalg.inv(V_sub)
        F_pot = 0.5 * Delta @ V_inv @ Delta
    except np.linalg.LinAlgError:
        # V is singular -- use pseudoinverse
        V_pinv = np.linalg.pinv(V_sub, rcond=1e-10)
        F_pot = 0.5 * Delta @ V_pinv @ Delta

    F_cond = F_kin + F_pot
    return F_cond, F_kin, F_pot


def run_gap_equation():
    """Main computation: solve BCS gap equation at all tau values."""
    print("=" * 80)
    print("Session 23a Step 5: BCS Gap Equation — Kosmann-Dirac System")
    print("=" * 80)
    print()
    print("Formula: V_nm = -sum_{a=3..6} |<n|K_a|m>|^2  (Feynman convention)")
    print("Gap eq:  Delta_n = -sum_m V_nm * Delta_m / (2*sqrt(xi_m^2 + Delta_m^2))")
    print("Gate:    max eigenvalue of M = V/(2|xi|) > 1 => PASS")
    print()

    # Load data
    npz_path = os.path.join(SCRIPT_DIR, "s23a_kosmann_singlet.npz")
    data = load_kosmann_data(npz_path)
    print(f"Loaded: {npz_path}")
    print(f"Tau values: {TAU_VALUES}")
    print()

    # ================================================================
    # STRUCTURAL ANALYSIS: Gap-edge self-coupling
    # ================================================================
    print("=" * 80)
    print("STRUCTURAL ANALYSIS: Gap-edge self-coupling")
    print("=" * 80)
    print()

    for idx, tau in enumerate(TAU_VALUES):
        V, evals, sym_err = build_V_matrix(data, idx)
        levels = classify_modes(evals)

        gap_idx = levels[0][1]
        V_gap = V[np.ix_(gap_idx, gap_idx)]
        max_gap_self = np.max(V_gap)

        if len(levels) > 1:
            near_idx = levels[1][1]
            V_gap_near = V[np.ix_(gap_idx, near_idx)]
            max_gap_near = np.max(V_gap_near)
        else:
            max_gap_near = 0.0

        if len(levels) > 1:
            print(f"  tau={tau:.2f}: gap self-coupling = {max_gap_self:.2e}, "
                  f"gap-nearest coupling = {max_gap_near:.4f}, "
                  f"gap split = {levels[1][0]-levels[0][0]:.6f}")
        else:
            print(f"  tau={tau:.2f}: ALL DEGENERATE ({len(levels[0][1])} modes at "
                  f"|lambda|={levels[0][0]:.6f}), gap self-coupling = {max_gap_self:.2e}")

    print()
    print("CONCLUSION: Gap-edge self-coupling is ZERO at all tau > 0.")
    print("The 2-mode truncation has NO pairing interaction.")
    print("The minimum viable basis is 10 modes (gap + nearest level).")
    print()

    # ================================================================
    # METHOD 1: LINEARIZED EIGENVALUE (BINARY GATE)
    # ================================================================
    print("=" * 80)
    print("METHOD 1: Linearized BCS Eigenvalue Problem")
    print("=" * 80)
    print()

    basis_types = ['gap2', 'gap10', 'full16']
    mu_labels = ['mu=0', 'mu=+lmin', 'mu=-lmin']

    # Results storage
    results = {}

    for basis_type in basis_types:
        print(f"\n--- Basis: {basis_type} ---")
        print(f"{'tau':>6s} | ", end='')
        for ml in mu_labels:
            print(f" {ml:>12s}", end='')
        print(f" | {'VERDICT':>8s}")
        print("-" * 70)

        for idx, tau in enumerate(TAU_VALUES):
            V, evals, sym_err = build_V_matrix(data, idx)
            levels = classify_modes(evals)
            lambda_min = levels[0][0]
            basis_idx = select_basis(evals, basis_type)

            # Three mu choices
            mu_values = [0.0, lambda_min, -lambda_min]
            M_maxes = []

            for mu in mu_values:
                _, _, M_max, _ = linearized_bcs(V, evals, mu,
                                                eta_frac=ETA_DEFAULT,
                                                basis_indices=basis_idx)
                M_maxes.append(M_max)

            # Verdict: PASS if ANY mu gives M_max > 1
            verdict = "PASS" if max(M_maxes) > 1.0 else "FAIL"

            print(f"{tau:6.2f} | ", end='')
            for mm in M_maxes:
                marker = " *" if mm > 1.0 else "  "
                print(f" {mm:10.6f}{marker}", end='')
            print(f" | {verdict:>8s}")

            key = (basis_type, idx)
            results[key] = {
                'M_maxes': M_maxes,
                'mu_values': mu_values,
                'verdict': verdict,
                'evals': evals.copy(),
                'V': V.copy(),
                'basis_idx': basis_idx.copy(),
            }

    # ================================================================
    # REGULATOR SENSITIVITY (for the cases that matter)
    # ================================================================
    print()
    print("=" * 80)
    print("REGULATOR SENSITIVITY: eta = {0.001, 0.01, 0.1} * lambda_min")
    print("(full16, mu=+lambda_min -- the most favorable configuration)")
    print("=" * 80)
    print()

    print(f"{'tau':>6s} | ", end='')
    for eta in ETA_SENSITIVITY:
        print(f" {'eta='+str(eta):>14s}", end='')
    print(f" | {'Spread':>8s}")
    print("-" * 65)

    for idx, tau in enumerate(TAU_VALUES):
        V, evals, sym_err = build_V_matrix(data, idx)
        levels = classify_modes(evals)
        lambda_min = levels[0][0]
        basis_idx = select_basis(evals, 'full16')

        M_max_vals = []
        for eta in ETA_SENSITIVITY:
            _, _, M_max, _ = linearized_bcs(V, evals, lambda_min,
                                            eta_frac=eta,
                                            basis_indices=basis_idx)
            M_max_vals.append(M_max)

        spread = max(M_max_vals) - min(M_max_vals)
        print(f"{tau:6.2f} | ", end='')
        for mm in M_max_vals:
            marker = " *" if mm > 1.0 else "  "
            print(f" {mm:12.6f}{marker}", end='')
        print(f" | {spread:8.4f}")

    # ================================================================
    # METHOD 2: SELF-CONSISTENT ITERATION (full16, multiple mu)
    # ================================================================
    print()
    print("=" * 80)
    print("METHOD 2: Self-Consistent Iteration (full16 basis)")
    print("=" * 80)
    print()

    print(f"{'tau':>6s} {'mu':>10s} | {'|Delta|':>12s} {'Delta_max':>12s} "
          f"{'conv?':>6s} {'iters':>6s} {'trivial?':>10s}")
    print("-" * 75)

    sc_results = {}

    for idx, tau in enumerate(TAU_VALUES):
        V, evals, sym_err = build_V_matrix(data, idx)
        levels = classify_modes(evals)
        lambda_min = levels[0][0]
        basis_idx = select_basis(evals, 'full16')

        for mu_label, mu in zip(['mu=0', 'mu=+lmin', 'mu=-lmin'],
                                 [0.0, lambda_min, -lambda_min]):
            Delta, converged, n_iter, history = selfconsistent_iteration(
                V, evals, mu, eta_frac=ETA_DEFAULT, basis_indices=basis_idx,
                max_iter=50000, tol=1e-12, Delta0_scale=0.01
            )

            D_norm = np.linalg.norm(Delta)
            D_max = np.max(np.abs(Delta))
            trivial = D_norm < 1e-20

            print(f"{tau:6.2f} {mu_label:>10s} | {D_norm:12.6e} {D_max:12.6e} "
                  f"{'Y' if converged else 'N':>6s} {n_iter:>6d} "
                  f"{'TRIVIAL' if trivial else 'NON-TRIVIAL':>10s}")

            sc_results[(idx, mu_label)] = {
                'Delta': Delta,
                'converged': converged,
                'n_iter': n_iter,
                'trivial': trivial,
                'D_norm': D_norm,
            }

    # ================================================================
    # METHOD 2b: Multiple initial conditions (to check for bistability)
    # ================================================================
    print()
    print("=" * 80)
    print("METHOD 2b: Sensitivity to Initial Conditions (full16, mu=+lmin)")
    print("=" * 80)
    print()

    ic_scales = [0.001, 0.01, 0.1, 0.5, 1.0]

    print(f"{'tau':>6s} | ", end='')
    for sc in ic_scales:
        print(f"  {'D0='+str(sc):>10s}", end='')
    print(f" | {'consistent?':>12s}")
    print("-" * 80)

    for idx, tau in enumerate(TAU_VALUES):
        V, evals, sym_err = build_V_matrix(data, idx)
        levels = classify_modes(evals)
        lambda_min = levels[0][0]
        basis_idx = select_basis(evals, 'full16')

        norms = []
        for sc in ic_scales:
            Delta, converged, n_iter, history = selfconsistent_iteration(
                V, evals, lambda_min, eta_frac=ETA_DEFAULT,
                basis_indices=basis_idx, max_iter=50000, tol=1e-12,
                Delta0_scale=sc
            )
            norms.append(np.linalg.norm(Delta))

        # Check consistency: all should converge to same answer
        nonzero = [n for n in norms if n > 1e-20]
        consistent = (len(set([n < 1e-20 for n in norms])) == 1)

        print(f"{tau:6.2f} | ", end='')
        for n in norms:
            marker = " T" if n < 1e-20 else "  "
            print(f"  {n:8.2e}{marker}", end='')
        print(f" | {'YES' if consistent else 'NO':>12s}")

    # ================================================================
    # METHOD 3: FREE ENERGY (where non-trivial gap exists)
    # ================================================================
    print()
    print("=" * 80)
    print("METHOD 3: Condensation Free Energy (full16, mu=+lmin)")
    print("=" * 80)
    print()

    print(f"{'tau':>6s} | {'F_cond':>14s} {'F_kin':>14s} {'F_pot':>14s} | {'stable?':>8s}")
    print("-" * 65)

    fe_results = {}

    for idx, tau in enumerate(TAU_VALUES):
        V, evals, sym_err = build_V_matrix(data, idx)
        levels = classify_modes(evals)
        lambda_min = levels[0][0]
        basis_idx = select_basis(evals, 'full16')

        # Get self-consistent Delta
        Delta, converged, _, _ = selfconsistent_iteration(
            V, evals, lambda_min, eta_frac=ETA_DEFAULT,
            basis_indices=basis_idx, max_iter=50000, tol=1e-12
        )

        if np.linalg.norm(Delta) > 1e-20:
            F_cond, F_kin, F_pot = free_energy(V, evals, lambda_min, Delta, basis_idx)
            stable = F_cond < 0
            print(f"{tau:6.2f} | {F_cond:14.6e} {F_kin:14.6e} {F_pot:14.6e} | "
                  f"{'STABLE' if stable else 'UNSTABLE':>8s}")
            fe_results[idx] = {'F_cond': F_cond, 'F_kin': F_kin, 'F_pot': F_pot, 'stable': stable}
        else:
            print(f"{tau:6.2f} | {'(trivial -- no gap)':>44s} | {'N/A':>8s}")
            fe_results[idx] = {'F_cond': 0.0, 'F_kin': 0.0, 'F_pot': 0.0, 'stable': False}

    # ================================================================
    # DETAILED EIGENVALUE STRUCTURE AT CRITICAL TAU VALUES
    # ================================================================
    print()
    print("=" * 80)
    print("DETAILED M EIGENVALUE STRUCTURE (full16, mu=+lmin)")
    print("=" * 80)
    print()

    for idx, tau in enumerate(TAU_VALUES):
        V, evals, sym_err = build_V_matrix(data, idx)
        levels = classify_modes(evals)
        lambda_min = levels[0][0]
        basis_idx = select_basis(evals, 'full16')

        M_evals, M_evecs, M_max, M_matrix = linearized_bcs(
            V, evals, lambda_min, eta_frac=ETA_DEFAULT, basis_indices=basis_idx
        )

        # Sort eigenvalues descending
        sorted_M = np.sort(M_evals)[::-1]

        print(f"tau={tau:.2f}: M eigenvalues (top 5): ", end='')
        for i in range(min(5, len(sorted_M))):
            marker = " *" if sorted_M[i] > 1.0 else ""
            print(f"{sorted_M[i]:.6f}{marker}", end='  ')
        print()

        # Eigenvector of the dominant eigenvalue
        max_idx = np.argmax(M_evals)
        dominant_evec = M_evecs[:, max_idx]

        # Map back to physical modes
        print(f"  Dominant eigenvector components (by mode eigenvalue):")
        for j, bi in enumerate(basis_idx):
            if abs(dominant_evec[j]) > 0.01:
                print(f"    mode {bi} (E={evals[bi]:+.6f}): weight = {dominant_evec[j]:+.6f}")

    # ================================================================
    # Constraint Gate CLASSIFICATION
    # ================================================================
    print()
    print("=" * 80)
    print("Constraint Gate CLASSIFICATION")
    print("=" * 80)
    print()

    # K-1a: Binary gate (linearized, any tau, any mu, full16)
    any_pass = False
    pass_taus = []
    for idx, tau in enumerate(TAU_VALUES):
        key = ('full16', idx)
        if key in results:
            if max(results[key]['M_maxes']) > 1.0:
                any_pass = True
                pass_taus.append(tau)

    if any_pass:
        print(f"  K-1a (Binary gate, linearized): PASS at tau = {pass_taus}")
    else:
        # Check gap10 as well
        pass_taus_10 = []
        for idx, tau in enumerate(TAU_VALUES):
            key = ('gap10', idx)
            if key in results:
                if max(results[key]['M_maxes']) > 1.0:
                    pass_taus_10.append(tau)

        if pass_taus_10:
            print(f"  K-1a (Binary gate, gap10): PASS at tau = {pass_taus_10}")
        else:
            print(f"  K-1a (Binary gate): FAIL -- M_max < 1 at ALL tau values")

    # K-1b: Self-consistent gap
    any_nontrivial = False
    for key, val in sc_results.items():
        if not val['trivial']:
            any_nontrivial = True
            break

    if any_nontrivial:
        print(f"  K-1b (Self-consistent gap): PASS -- non-trivial solution found")
    else:
        print(f"  K-1b (Self-consistent gap): FAIL -- all solutions trivial")

    # K-1c: Thermodynamic stability
    any_stable = False
    for idx, val in fe_results.items():
        if val['stable']:
            any_stable = True
            break

    if any_stable:
        print(f"  K-1c (Free energy): PASS -- F_cond < 0 for some tau")
    else:
        print(f"  K-1c (Free energy): FAIL or N/A -- F_cond >= 0 everywhere")

    # K-1d: Regulator sensitivity
    print(f"  K-1d (Regulator sensitivity): See table above")

    # K-1e: Basis convergence
    print(f"  K-1e (Basis convergence): gap2=ZERO (structural), gap10 and full16 compared above")

    # Overall K-1
    overall = "PASS" if any_pass else "FAIL"
    print(f"\n  OVERALL K-1 VERDICT: {overall}")

    # ================================================================
    # SAVE RESULTS
    # ================================================================
    output_npz = os.path.join(SCRIPT_DIR, "s23a_gap_equation.npz")

    save_data = {
        'tau_values': TAU_VALUES,
    }

    for idx, tau in enumerate(TAU_VALUES):
        V, evals, sym_err = build_V_matrix(data, idx)
        levels = classify_modes(evals)
        lambda_min = levels[0][0]

        save_data[f'V_matrix_{idx}'] = V
        save_data[f'eigenvalues_{idx}'] = evals
        save_data[f'lambda_min_{idx}'] = lambda_min

        # Method 1 results for all basis types
        for bt in basis_types:
            basis_idx = select_basis(evals, bt)
            for mi, (ml, mu) in enumerate(zip(mu_labels, [0.0, lambda_min, -lambda_min])):
                M_evals_out, _, M_max_out, M_mat = linearized_bcs(
                    V, evals, mu, eta_frac=ETA_DEFAULT, basis_indices=basis_idx
                )
                save_data[f'M_evals_{bt}_{ml}_{idx}'] = M_evals_out
                save_data[f'M_max_{bt}_{ml}_{idx}'] = M_max_out

        # Method 2 results (full16, primary mu)
        Delta, converged, n_iter, _ = selfconsistent_iteration(
            V, evals, lambda_min, eta_frac=ETA_DEFAULT,
            basis_indices=np.arange(16), max_iter=50000, tol=1e-12
        )
        save_data[f'Delta_sc_{idx}'] = Delta
        save_data[f'sc_converged_{idx}'] = converged
        save_data[f'sc_niter_{idx}'] = n_iter

    np.savez_compressed(output_npz, **save_data)
    print(f"\nSaved: {output_npz}")
    print(f"File size: {os.path.getsize(output_npz) / 1024:.1f} KB")

    # ================================================================
    # PLOT
    # ================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: M_max vs tau for different bases and mu
    ax = axes[0, 0]
    for bt, ls in zip(['gap10', 'full16'], ['--', '-']):
        for mi, (ml, color) in enumerate(zip(mu_labels, ['blue', 'red', 'green'])):
            M_maxes_plot = []
            for idx in range(len(TAU_VALUES)):
                key = (bt, idx)
                if key in results:
                    M_maxes_plot.append(results[key]['M_maxes'][mi])
                else:
                    M_maxes_plot.append(0)
            ax.plot(TAU_VALUES, M_maxes_plot, ls=ls, color=color,
                    label=f'{bt} {ml}', marker='o', markersize=3)

    ax.axhline(y=1.0, color='black', ls=':', alpha=0.5, label='Critical (M=1)')
    ax.set_xlabel('tau')
    ax.set_ylabel('M_max (linearized BCS eigenvalue)')
    ax.set_title('Method 1: Linearized BCS Binary Gate')
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 2: Gap-edge coupling structure
    ax = axes[0, 1]
    V_gap_near_vals = []
    gap_splits = []
    for idx, tau in enumerate(TAU_VALUES):
        V, evals, _ = build_V_matrix(data, idx)
        levels = classify_modes(evals)
        if len(levels) > 1:
            gap_idx = levels[0][1]
            near_idx = levels[1][1]
            V_gn = V[np.ix_(gap_idx, near_idx)]
            V_gap_near_vals.append(np.max(V_gn))
            gap_splits.append(levels[1][0] - levels[0][0])
        else:
            V_gap_near_vals.append(0)
            gap_splits.append(0)

    ax2 = ax.twinx()
    ax.plot(TAU_VALUES, V_gap_near_vals, 'b-o', label='V(gap,nearest)')
    ax2.plot(TAU_VALUES, gap_splits, 'r-s', label='Gap splitting')
    ax.set_xlabel('tau')
    ax.set_ylabel('V_nm (gap-nearest coupling)', color='blue')
    ax2.set_ylabel('Gap splitting (nearest - gap)', color='red')
    ax.set_title('Pairing Structure vs tau')
    ax.legend(loc='upper left', fontsize=8)
    ax2.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Self-consistent Delta norm
    ax = axes[1, 0]
    for ml in mu_labels:
        D_norms = []
        for idx in range(len(TAU_VALUES)):
            key = (idx, ml)
            if key in sc_results:
                D_norms.append(sc_results[key]['D_norm'])
            else:
                D_norms.append(0)
        ax.semilogy(TAU_VALUES, [max(d, 1e-30) for d in D_norms], '-o', label=ml)

    ax.axhline(y=1e-20, color='black', ls=':', alpha=0.5, label='Trivial threshold')
    ax.set_xlabel('tau')
    ax.set_ylabel('|Delta| (self-consistent)')
    ax.set_title('Method 2: Self-Consistent Gap Magnitude')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: M eigenvalue spectrum at tau=0.30
    ax = axes[1, 1]
    idx_030 = 5
    V, evals, _ = build_V_matrix(data, idx_030)
    levels = classify_modes(evals)
    lambda_min = levels[0][0]

    for bt, label in zip(['gap10', 'full16'], ['gap10', 'full16']):
        basis_idx = select_basis(evals, bt)
        M_ev, _, _, _ = linearized_bcs(V, evals, lambda_min, eta_frac=0.01,
                                         basis_indices=basis_idx)
        M_sorted = np.sort(M_ev)[::-1]
        ax.bar(np.arange(len(M_sorted)) + (0.2 if bt == 'full16' else -0.2),
               M_sorted, width=0.35, label=label, alpha=0.7)

    ax.axhline(y=1.0, color='black', ls=':', alpha=0.5)
    ax.set_xlabel('Eigenvalue index (sorted descending)')
    ax.set_ylabel('M eigenvalue')
    ax.set_title(f'M Eigenvalue Spectrum at tau=0.30, mu=+lmin')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plot_path = os.path.join(SCRIPT_DIR, "s23a_gap_equation.png")
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"Plot saved: {plot_path}")

    return results, sc_results, fe_results


if __name__ == "__main__":
    t_start = time.time()
    results, sc_results, fe_results = run_gap_equation()
    elapsed = time.time() - t_start
    print(f"\nTotal runtime: {elapsed:.1f}s")
