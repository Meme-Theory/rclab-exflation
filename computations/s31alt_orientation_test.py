"""
BA-31-3: Orientation Reversal (Skew-Whiffing) Test
====================================================

Tests whether reversing the orientation of SU(3) changes the D_K spectrum.

Orientation reversal acts as gamma_9 -> -gamma_9 on the spinor bundle.
We implement this by negating one Clifford generator: gamma_8 -> -gamma_8.
This changes the chirality operator gamma_9 = gamma_1...gamma_8 -> -gamma_9
while preserving the Clifford algebra {gamma_a, gamma_b} = 2*delta_{ab}.

The effect on D_K: the spin connection Omega involves triple products
gamma_a gamma_b gamma_c. Changing gamma_8 -> -gamma_8 changes the sign
of all terms involving an ODD number of gamma_8 factors.

Gate BA-31-or:
  INSENSITIVE if D_K eigenvalue spectra identical to machine epsilon
  DEPENDENT if any eigenvalue differs by more than 10^{-10}

Author: sim (phonon-exflation-sim), Session 31Aa
Date: 2026-03-02
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, build_chirality, collect_spectrum,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    dirac_operator_on_irrep, get_irrep
)


def collect_spectrum_with_gammas(tau, gens, f_abc, gammas, max_pq_sum=6):
    """
    Collect spectrum using specified gamma matrices (possibly modified).

    Returns list of (complex_eigenvalue, PW_multiplicity) and per-sector data.
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    eval_data = []
    all_eigenvalues = []

    # Trivial irrep: D = Omega
    evals_trivial = np.linalg.eigvals(Omega)
    eval_data.append((0, 0, evals_trivial))
    for ev in evals_trivial:
        all_eigenvalues.append((ev, 1))

    # Non-trivial irreps
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if p == 0 and q == 0:
                continue
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            try:
                rho, dim_check = get_irrep(p, q, gens, f_abc)
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                evals_pi = np.linalg.eigvals(D_pi)
                eval_data.append((p, q, evals_pi))
                for ev in evals_pi:
                    all_eigenvalues.append((ev, dim_pq))
            except NotImplementedError:
                continue

    return all_eigenvalues, eval_data


def main():
    t_start = time.time()

    print("=" * 70)
    print("BA-31-3: ORIENTATION REVERSAL (SKEW-WHIFFING) TEST")
    print("=" * 70)

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)

    # Standard gammas
    gammas_std = build_cliff8()
    gamma9_std = build_chirality(gammas_std)

    # Reversed orientation: negate gamma_8 -> -gamma_8
    # This flips gamma_9 = prod(gamma_a) -> -gamma_9
    gammas_rev = [g.copy() for g in gammas_std]
    gammas_rev[7] = -gammas_rev[7]  # gamma_8 -> -gamma_8 (0-indexed: index 7)

    # Verify Clifford algebra still satisfied
    for a in range(8):
        for b in range(8):
            ac = gammas_rev[a] @ gammas_rev[b] + gammas_rev[b] @ gammas_rev[a]
            target = 2.0 * (1 if a == b else 0) * np.eye(16)
            err = np.max(np.abs(ac - target))
            assert err < 1e-14, f"Clifford violation: {err} at ({a},{b})"

    # Verify gamma_9 sign flip
    gamma9_rev = build_chirality(gammas_rev)
    flip_err = np.max(np.abs(gamma9_rev + gamma9_std))  # should be ~ 0
    print(f"gamma_9 flip check: ||gamma9_rev + gamma9_std|| = {flip_err:.2e}")

    tau_values = [0.0, 0.15, 0.21, 0.50]
    N_max = 6

    results = {}

    for tau in tau_values:
        print(f"\n--- tau = {tau:.2f} ---")

        # Standard orientation
        t0 = time.time()
        evals_std, sectors_std = collect_spectrum_with_gammas(
            tau, gens, f_abc, gammas_std, max_pq_sum=N_max
        )
        dt_std = time.time() - t0

        # Reversed orientation
        t0 = time.time()
        evals_rev, sectors_rev = collect_spectrum_with_gammas(
            tau, gens, f_abc, gammas_rev, max_pq_sum=N_max
        )
        dt_rev = time.time() - t0

        # Compare sector by sector
        max_sector_diff = 0.0
        sector_diffs = []

        for (p_s, q_s, ev_s), (p_r, q_r, ev_r) in zip(sectors_std, sectors_rev):
            assert p_s == p_r and q_s == q_r, f"Sector mismatch: ({p_s},{q_s}) vs ({p_r},{q_r})"

            # Sort by absolute value for comparison
            abs_s = np.sort(np.abs(ev_s))
            abs_r = np.sort(np.abs(ev_r))

            diff = np.max(np.abs(abs_s - abs_r))
            sector_diffs.append((p_s, q_s, diff, len(ev_s)))
            max_sector_diff = max(max_sector_diff, diff)

        # Also compare full sorted |eigenvalue| sets
        abs_all_std = np.sort(np.array([np.abs(ev) for ev, _ in evals_std]))
        abs_all_rev = np.sort(np.array([np.abs(ev) for ev, _ in evals_rev]))
        full_diff = np.max(np.abs(abs_all_std - abs_all_rev))

        print(f"  Standard: {len(evals_std)} eigenvalues, {dt_std:.1f}s")
        print(f"  Reversed: {len(evals_rev)} eigenvalues, {dt_rev:.1f}s")
        print(f"  Max |lambda| difference (full): {full_diff:.2e}")
        print(f"  Max |lambda| difference (per sector): {max_sector_diff:.2e}")

        # Report per-sector differences
        print(f"  Per-sector details:")
        for p, q, d, n in sector_diffs:
            flag = " ***" if d > 1e-10 else ""
            print(f"    ({p},{q}): {n} evals, max diff = {d:.2e}{flag}")

        results[tau] = {
            'full_diff': full_diff,
            'max_sector_diff': max_sector_diff,
            'sector_diffs': sector_diffs,
            'n_evals': len(evals_std),
            'abs_all_std': abs_all_std,
            'abs_all_rev': abs_all_rev,
        }

    # ========================================================================
    # Gate verdict
    # ========================================================================
    print("\n" + "=" * 70)
    print("GATE BA-31-or ASSESSMENT")
    print("=" * 70)

    all_diffs = [results[tau]['full_diff'] for tau in tau_values]
    max_diff_overall = max(all_diffs)

    for tau in tau_values:
        r = results[tau]
        print(f"  tau={tau:.2f}: max |lambda| diff = {r['full_diff']:.2e}")

    if max_diff_overall > 1e-10:
        verdict = "DEPENDENT"
        print(f"\n  --> BA-31-or: ORIENTATION-DEPENDENT")
        print(f"      Max difference: {max_diff_overall:.2e}")
        print(f"      Framework must justify orientation choice.")
    else:
        verdict = "INSENSITIVE"
        print(f"\n  --> BA-31-or: ORIENTATION-INSENSITIVE")
        print(f"      Max difference: {max_diff_overall:.2e} (machine epsilon)")
        print(f"      D_K robust against skew-whiffing on Jensen-deformed SU(3).")

    # ========================================================================
    # Save
    # ========================================================================
    save_dict = {
        'tau_values': np.array(tau_values),
        'verdict': np.array(verdict),
        'max_diff_overall': np.array(max_diff_overall),
    }
    for tau in tau_values:
        prefix = f'tau_{tau:.2f}_'.replace('.', 'p')
        r = results[tau]
        save_dict[prefix + 'full_diff'] = np.array(r['full_diff'])
        save_dict[prefix + 'max_sector_diff'] = np.array(r['max_sector_diff'])
        save_dict[prefix + 'abs_std'] = r['abs_all_std']
        save_dict[prefix + 'abs_rev'] = r['abs_all_rev']

    np.savez('tier0-computation/s31alt_orientation_test.npz', **save_dict)
    print(f"\nSaved: tier0-computation/s31alt_orientation_test.npz")

    elapsed = time.time() - t_start
    print(f"Total runtime: {elapsed:.1f}s")
    print(f"\nGATE BA-31-or: {verdict}")

    return verdict


if __name__ == '__main__':
    main()
