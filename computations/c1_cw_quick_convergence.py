"""
C-1 QUICK: CW Convergence at 5 s-values only
==============================================

Uses the same infrastructure as the full C-1 but only computes
the CW potential at the 5 s-values from Diagnostic 1 (0.0, 0.15, 0.30, 0.50, 1.0)
for all 4 truncation levels. This gives the key convergence answer
without waiting for the 61-point sweep.

Also computes ratio stability (Diagnostic 5) and Weyl law (Diagnostic 4).
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, validate_clifford,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    collect_spectrum,
)
from tier1_spectral_action import (
    dim_su3_irrep, compute_heat_kernel, extract_seeley_dewitt,
    spectral_zeta,
)
from tier1_coleman_weinberg import (
    V_tree, V_CW_boson, compute_fermionic_CW_nf,
)


def main():
    print("="*72)
    print("C-1 QUICK: CW + RATIO + WEYL CONVERGENCE (5 s-values)")
    print("="*72)

    t0 = time.time()

    # Build infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    validate_clifford(gammas)

    s_values = [0.0, 0.15, 0.30, 0.50, 1.0]
    max_pq_sums = [3, 4, 5, 6]

    # Phase 1: Compute all eigenvalue data
    print("\nPhase 1: Computing Dirac spectra...")
    eval_cache = {}  # (s, mps) -> eval_data
    sd_cache = {}    # (s, mps) -> {a_0, a_2, a_4}

    for s in s_values:
        for mps in max_pq_sums:
            t1 = time.time()
            _, eval_data = collect_spectrum(
                s, gens, f_abc, gammas, max_pq_sum=mps, verbose=False
            )
            eval_cache[(s, mps)] = eval_data
            dt = time.time() - t1

            # Extract SD coefficients
            coeffs, fit = extract_seeley_dewitt(
                eval_data, t_range=(0.005, 0.3), n_points=200,
                n_coeffs=4, verbose=False
            )
            sd_cache[(s, mps)] = coeffs

            n_evals = sum(len(ev) for _, _, ev in eval_data)
            n_weighted = sum(dim_su3_irrep(p, q) * len(ev) for p, q, ev in eval_data)
            print(f"  s={s:.2f}, mps={mps}: {n_evals} raw, {n_weighted} weighted, "
                  f"a_0={coeffs['a_0']:.4e}, time={dt:.1f}s", flush=True)

    t_phase1 = time.time() - t0
    print(f"\nPhase 1 complete: {t_phase1:.1f}s")

    # =========================================================================
    # CW CONVERGENCE
    # =========================================================================
    print("\n" + "="*72)
    print("CW FERMIONIC CONVERGENCE")
    print("="*72)

    print(f"\nV_CW^fermion at each (s, mps) for mu^2=1.0, n_f=1:")
    print(f"{'s':>5}", end="")
    for mps in max_pq_sums:
        print(f"  {'V_f(mps='+str(mps)+')':>16}", end="")
    print(f"  {'rel_chg(5->6)':>14}")

    for s in s_values:
        print(f"{s:5.2f}", end="")
        vals = []
        for mps in max_pq_sums:
            Vf, _ = compute_fermionic_CW_nf(eval_cache[(s, mps)], n_f=1, mu_sq=1.0)
            vals.append(Vf)
            print(f"  {Vf:16.8e}", end="")

        if abs(vals[-2]) > 1e-30:
            rc = abs(vals[-1] - vals[-2]) / abs(vals[-2])
            print(f"  {rc:14.6f}")
        else:
            print()

    # V_CW^fermion with n_f=4
    print(f"\nV_CW^fermion at each (s, mps) for mu^2=1.0, n_f=4:")
    print(f"{'s':>5}", end="")
    for mps in max_pq_sums:
        print(f"  {'V_f(mps='+str(mps)+')':>16}", end="")
    print(f"  {'rel_chg(5->6)':>14}")

    for s in s_values:
        print(f"{s:5.2f}", end="")
        vals = []
        for mps in max_pq_sums:
            Vf, _ = compute_fermionic_CW_nf(eval_cache[(s, mps)], n_f=4, mu_sq=1.0)
            vals.append(Vf)
            print(f"  {Vf:16.8e}", end="")

        if abs(vals[-2]) > 1e-30:
            rc = abs(vals[-1] - vals[-2]) / abs(vals[-2])
            print(f"  {rc:14.6f}")
        else:
            print()

    # V_total convergence (tree + boson + fermion)
    print(f"\nV_total = V_tree + V_boson + V_fermion:")
    for mu_sq in [0.1, 1.0, 10.0]:
        for n_f in [1, 4]:
            print(f"\n  mu^2={mu_sq}, n_f={n_f}:")
            print(f"  {'s':>5}", end="")
            for mps in max_pq_sums:
                print(f"  {'V_tot('+str(mps)+')':>14}", end="")
            print(f"  {'delta(5->6)':>12}")

            for s in s_values:
                Vt = float(np.squeeze(V_tree(s)))
                Vb = float(np.squeeze(V_CW_boson(np.atleast_1d(s), mu_sq, c_b=5.0/6.0, n_b=4)))
                print(f"  {s:5.2f}", end="")

                vtots = []
                for mps in max_pq_sums:
                    Vf, _ = compute_fermionic_CW_nf(eval_cache[(s, mps)], n_f, mu_sq)
                    vtot = Vt + Vb + Vf
                    vtots.append(vtot)
                    print(f"  {vtot:14.6e}", end="")

                delta = vtots[-1] - vtots[-2]
                print(f"  {delta:12.4e}")

    # =========================================================================
    # SECTOR CONTRIBUTION ANALYSIS
    # =========================================================================
    print("\n" + "="*72)
    print("SECTOR CONTRIBUTION ANALYSIS (WHY CW DIVERGES OR CONVERGES)")
    print("="*72)

    print("\nKey question: does V_CW^fermion grow because NEW sectors (high p+q)")
    print("contribute large |lambda|^4 terms, or because they add small corrections?")
    print("\nSector-by-sector |lambda|^4 contribution at s=0.30, mu^2=1.0:")

    s_test = 0.30
    for mps in max_pq_sums:
        eval_data = eval_cache[(s_test, mps)]
        print(f"\n  max_pq_sum = {mps}:")
        total_lam4 = 0
        for p, q, evals in eval_data:
            d_pq = dim_su3_irrep(p, q)
            abs_ev = np.abs(evals)
            nonzero = abs_ev[abs_ev > 1e-12]
            if len(nonzero) > 0:
                lam4_contrib = d_pq * np.sum(nonzero**4)
                total_lam4 += lam4_contrib
                shell = p + q
                print(f"    ({p},{q}) [shell {shell}]: dim={d_pq}, "
                      f"n_evals={len(evals)}, "
                      f"|lambda|_max={np.max(abs_ev):.4f}, "
                      f"sum |lambda|^4 * dim = {lam4_contrib:.4e}")
        print(f"    TOTAL sum |lambda|^4 * dim = {total_lam4:.4e}")

    # New sectors only (those not present in previous truncation)
    print("\n\nCONTRIBUTION FROM NEW SHELLS ONLY:")
    print(f"{'shell':>6} {'sum_lam4_new':>14} {'sum_lam4_total':>16} {'fraction':>10}")

    s_test = 0.30
    prev_total = 0
    for mps_idx, mps in enumerate(max_pq_sums):
        eval_data = eval_cache[(s_test, mps)]
        total = 0
        new_shell = 0
        for p, q, evals in eval_data:
            d_pq = dim_su3_irrep(p, q)
            abs_ev = np.abs(evals)
            nonzero = abs_ev[abs_ev > 1e-12]
            if len(nonzero) > 0:
                contrib = d_pq * np.sum(nonzero**4)
                total += contrib
                if p + q == mps:
                    new_shell += contrib

        if total > 0:
            frac = new_shell / total
        else:
            frac = 0

        print(f"{mps:6d} {new_shell:14.4e} {total:16.4e} {frac:10.4f}")
        prev_total = total

    # =========================================================================
    # RATIO STABILITY (a_2/a_0, a_4/a_0)
    # =========================================================================
    print("\n" + "="*72)
    print("RATIO STABILITY (PHYSICS-RELEVANT)")
    print("="*72)

    print(f"\n  a_2/a_0 encodes scalar curvature / volume")
    print(f"  a_4/a_0 encodes gauge couplings")

    print(f"\n  {'s':>5} {'ratio':>10}", end="")
    for mps in max_pq_sums:
        print(f"  {'mps='+str(mps):>12}", end="")
    print(f"  {'rel_chg(5->6)':>14}")

    for s in s_values:
        for rname, nkey, dkey in [('a_2/a_0', 'a_2', 'a_0'),
                                    ('a_4/a_0', 'a_4', 'a_0'),
                                    ('a_4/a_2', 'a_4', 'a_2')]:
            vals = []
            for mps in max_pq_sums:
                c = sd_cache[(s, mps)]
                den = c[dkey]
                if abs(den) > 1e-30:
                    vals.append(c[nkey] / den)
                else:
                    vals.append(float('nan'))

            print(f"  {s:5.2f} {rname:>10}", end="")
            for v in vals:
                if np.isfinite(v):
                    print(f"  {v:12.4e}", end="")
                else:
                    print(f"  {'nan':>12}", end="")

            if len(vals) >= 2 and np.isfinite(vals[-1]) and np.isfinite(vals[-2]):
                if abs(vals[-2]) > 1e-30:
                    rc = abs(vals[-1] - vals[-2]) / abs(vals[-2])
                    print(f"  {rc:14.6f}")
                else:
                    print(f"  {'---':>14}")
            else:
                print()

    # =========================================================================
    # WEYL LAW
    # =========================================================================
    print("\n" + "="*72)
    print("WEYL LAW AND SPECTRAL DIMENSION")
    print("="*72)

    for s in s_values:
        print(f"\n  s = {s:.2f}:")
        for mps in max_pq_sums:
            eval_data = eval_cache[(s, mps)]

            # Weighted eigenvalue count
            all_abs = []
            for p, q, evals in eval_data:
                d_pq = dim_su3_irrep(p, q)
                for ev in evals:
                    all_abs.extend([abs(ev)] * d_pq)
            all_abs = np.sort(all_abs)
            N_total = len(all_abs)
            nonzero = all_abs[all_abs > 1e-12]
            N_nz = len(nonzero)

            if N_nz > 20:
                lam_max = nonzero[-1]
                # Weyl exponent from upper half
                mid = N_nz // 2
                log_lam = np.log(nonzero[mid:])
                log_N = np.log(np.arange(mid+1, N_nz+1))
                alpha = np.polyfit(log_lam, log_N, 1)[0]

                # Spectral dimension from heat kernel
                t_test = np.array([0.01, 0.02, 0.05, 0.1])
                K_test, _ = compute_heat_kernel(eval_data, t_test)
                if np.all(K_test > 0):
                    d_s = -2 * np.polyfit(np.log(t_test), np.log(K_test), 1)[0]
                else:
                    d_s = float('nan')
            else:
                lam_max = 0
                alpha = float('nan')
                d_s = float('nan')

            print(f"    mps={mps}: N={N_total}, lam_max={lam_max:.3f}, "
                  f"Weyl alpha={alpha:.2f}, d_spectral={d_s:.2f}")

    # =========================================================================
    # VERDICT
    # =========================================================================
    print("\n" + "="*72)
    print("CONVERGENCE VERDICT")
    print("="*72)

    # Compute key metrics
    max_rc_vf = 0  # max relative change in V_fermion
    for s in s_values:
        v5, _ = compute_fermionic_CW_nf(eval_cache[(s, 5)], n_f=1, mu_sq=1.0)
        v6, _ = compute_fermionic_CW_nf(eval_cache[(s, 6)], n_f=1, mu_sq=1.0)
        if abs(v5) > 1e-30:
            rc = abs(v6 - v5) / abs(v5)
            max_rc_vf = max(max_rc_vf, rc)

    max_rc_a0 = 0
    max_rc_a2 = 0
    for s in s_values:
        for cname, tracker_name in [('a_0', 'max_rc_a0'), ('a_2', 'max_rc_a2')]:
            v5 = sd_cache[(s, 5)][cname]
            v6 = sd_cache[(s, 6)][cname]
            if abs(v5) > 1e-30:
                rc = abs(v6 - v5) / abs(v5)
                if cname == 'a_0':
                    max_rc_a0 = max(max_rc_a0, rc)
                else:
                    max_rc_a2 = max(max_rc_a2, rc)

    print(f"\n  1. INDIVIDUAL SD COEFFICIENTS (5->6):")
    print(f"     Max relative change a_0: {max_rc_a0:.2%}")
    print(f"     Max relative change a_2: {max_rc_a2:.2%}")
    print(f"     Verdict: {'NOT CONVERGED' if max_rc_a0 > 0.1 else 'CONVERGED'}")

    print(f"\n  2. CW FERMIONIC POTENTIAL (5->6):")
    print(f"     Max relative change V_f: {max_rc_vf:.2%}")
    print(f"     Verdict: {'NOT CONVERGED' if max_rc_vf > 0.1 else 'CONVERGED'}")

    # Check if V_total shape is stable (gradient direction preserved)
    print(f"\n  3. V_total SHAPE STABILITY:")
    for n_f in [1, 4]:
        vtot_5 = []
        vtot_6 = []
        for s in s_values:
            Vt = float(np.squeeze(V_tree(s)))
            Vb = float(np.squeeze(V_CW_boson(np.atleast_1d(s), 1.0, 5.0/6.0, n_b=4)))
            Vf5, _ = compute_fermionic_CW_nf(eval_cache[(s, 5)], n_f, 1.0)
            Vf6, _ = compute_fermionic_CW_nf(eval_cache[(s, 6)], n_f, 1.0)
            vtot_5.append(Vt + Vb + Vf5)
            vtot_6.append(Vt + Vb + Vf6)

        vtot_5 = np.array(vtot_5)
        vtot_6 = np.array(vtot_6)

        # Normalize to compare shapes
        vtot_5n = vtot_5 - vtot_5[0]
        vtot_6n = vtot_6 - vtot_6[0]
        if np.max(np.abs(vtot_5n)) > 1e-30:
            vtot_5n /= np.max(np.abs(vtot_5n))
        if np.max(np.abs(vtot_6n)) > 1e-30:
            vtot_6n /= np.max(np.abs(vtot_6n))

        shape_diff = np.max(np.abs(vtot_6n - vtot_5n))
        print(f"     n_f={n_f}: normalized shape difference (5->6) = {shape_diff:.4f}")
        print(f"     Verdict: {'SHAPE STABLE' if shape_diff < 0.1 else 'SHAPE UNSTABLE'}")

    # Cost estimate for higher truncations
    n_irreps = {mps: sum(1 for p in range(mps+1) for q in range(mps+1-p))
                for mps in [3, 4, 5, 6, 8, 10, 12]}
    dim2_total = {mps: sum(dim_su3_irrep(p, q)**2 for p in range(mps+1) for q in range(mps+1-p))
                  for mps in [3, 4, 5, 6, 8, 10, 12]}

    print(f"\n  4. COST PROJECTIONS:")
    for mps in [6, 8, 10, 12]:
        ratio = dim2_total[mps] / dim2_total[6]
        est_time = ratio * 8.7  # seconds per s-value at mps=6
        print(f"     mps={mps:2d}: {n_irreps[mps]:3d} irreps, "
              f"dim^2={dim2_total[mps]:>8d}, "
              f"ratio vs 6: {ratio:5.1f}x, "
              f"est time/s-value: {est_time:.0f}s")

    print(f"\n  OVERALL RECOMMENDATION:")
    if max_rc_vf < 0.2:
        print(f"  V_CW fermionic is MARGINALLY converged ({max_rc_vf:.0%} change 5->6).")
        print(f"  CW minimum at mps=6 is INDICATIVE with ~{max_rc_vf:.0%} systematic uncertainty.")
        print(f"  Pushing to mps=8 would reduce uncertainty but not change qualitative picture.")
    else:
        print(f"  V_CW fermionic is NOT converged ({max_rc_vf:.0%} change 5->6).")
        print(f"  CW minimum at mps=6 should be treated as ORDER-OF-MAGNITUDE estimate.")
        print(f"  Pushing to mps=8 is RECOMMENDED if quantitative s_0 is needed.")

    t_total = time.time() - t0
    print(f"\n  Total runtime: {t_total:.1f}s")
    print("="*72)


if __name__ == "__main__":
    main()
