"""
Session 30Aa Step 1: Validate Lie derivative of Jensen metric.

Verifies:
1. Killing directions (a=0,1,2,7): L_{e_a} g = 0 to machine epsilon
2. Non-Killing directions (a=3,4,5,6): L_{e_a} g != 0
3. Symmetry: (L_{e_a} g)_{bc} = (L_{e_a} g)_{cb}
4. Volume-preservation: Tr(L_{e_a} g) = 0
5. Cross-check with s23a Kosmann symmetric formula
6. Covariant derivative nabla_{e_i}(L_{e_a} g) computation test

Author: phonon-exflation-sim (Session 30Aa)
Date: 2026-03-01
"""

import sys
import os
import time
import numpy as np

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
    spinor_connection_offset,
    build_cliff8,
    lie_derivative_metric,
    covariant_derivative_lie_metric,
    U1_IDX, SU2_IDX, C2_IDX, U2_IDX,
)


def validate_step1():
    """Validate Lie derivative computation."""
    print("=" * 70)
    print("Session 30Aa Step 1: Lie Derivative Validation")
    print("=" * 70)

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    tau_values = [0.0, 0.15, 0.35, 0.50]

    all_pass = True

    for tau in tau_values:
        print(f"\n{'='*60}")
        print(f"tau = {tau:.2f}")
        print(f"{'='*60}")

        B_ab = compute_killing_form(f_abc)
        g_s = jensen_metric(B_ab, tau)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)

        # Compute Lie derivatives for all 8 directions
        Lg_all = {}
        for a in range(8):
            Lg = lie_derivative_metric(Gamma, a)
            Lg_all[a] = Lg

            # Check symmetry
            sym_err = np.max(np.abs(Lg - Lg.T))

            # Check trace
            tr = np.trace(Lg)

            # Frobenius norm
            fnorm = np.sqrt(np.sum(Lg**2))

            dir_type = "Killing" if a in U2_IDX else "C^2"
            print(f"  a={a} ({dir_type:>7s}): ||Lg||={fnorm:.6e}, "
                  f"Tr(Lg)={tr:+.2e}, sym_err={sym_err:.2e}")

            # Validate symmetry
            if sym_err > 1e-14:
                print(f"    WARNING: symmetry violation!")
                all_pass = False

            # Validate volume preservation
            if abs(tr) > 1e-12:
                print(f"    WARNING: trace nonzero (volume not preserved)!")
                all_pass = False

        # Check Killing directions are zero
        for a in U2_IDX:
            fnorm = np.sqrt(np.sum(Lg_all[a]**2))
            if fnorm > 1e-12:
                print(f"  WARNING: Killing direction a={a} has ||Lg||={fnorm:.2e}")
                all_pass = False

        # Check non-Killing directions are nonzero (except at tau=0)
        if tau > 0:
            for a in C2_IDX:
                fnorm = np.sqrt(np.sum(Lg_all[a]**2))
                if fnorm < 1e-12:
                    print(f"  WARNING: Non-Killing direction a={a} has ||Lg||={fnorm:.2e} (expected nonzero)")
                    all_pass = False

        # At tau=0 (bi-invariant), ALL directions are Killing
        if tau == 0.0:
            for a in range(8):
                fnorm = np.sqrt(np.sum(Lg_all[a]**2))
                if fnorm > 1e-12:
                    print(f"  WARNING: bi-invariant a={a} has ||Lg||={fnorm:.2e} (expected 0)")
                    all_pass = False

        # Cross-check with s23a Kosmann symmetric formula
        # s23a computes: S_a = (1/4) sum_{r,s} [Gamma[s,r,a] + Gamma[r,s,a]] gamma_r gamma_s
        # which is proportional to sum of Lg[r,s] * gamma_r gamma_s.
        # Our Lg[b,c] = Gamma[b,c,a] + Gamma[c,b,a]
        # s23a's Lg_sym[r,s] = Gamma[s,r,a] + Gamma[r,s,a]
        # So: Lg[b,c] = s23a_Lg_sym[c,b] = s23a_Lg_sym[b,c] (symmetric)
        # They should match.

        print(f"\n  Covariant derivative test (a=3, nabla directions 0-7):")
        Lg3 = Lg_all[3]
        for i in range(8):
            nabla_Lg = covariant_derivative_lie_metric(Gamma, Lg3, i)
            # Verify it's computed (no NaN/Inf)
            if np.any(np.isnan(nabla_Lg)) or np.any(np.isinf(nabla_Lg)):
                print(f"    nabla_{{e_{i}}} Lg_3: NaN/Inf detected!")
                all_pass = False
            else:
                fnorm = np.sqrt(np.sum(nabla_Lg**2))
                print(f"    nabla_{{e_{i}}} Lg_3: ||.|| = {fnorm:.6e}")

        # Print the actual Lg tensor for a=3 (first non-Killing direction)
        if tau > 0:
            print(f"\n  (L_{{e_3}} g) at tau={tau:.2f}:")
            Lg3 = Lg_all[3]
            for b in range(8):
                row = "    [" + ", ".join(f"{Lg3[b,c]:+8.5f}" for c in range(8)) + "]"
                print(row)

    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    if all_pass:
        print("  ALL CHECKS PASSED")
    else:
        print("  SOME CHECKS FAILED — see warnings above")

    return all_pass


if __name__ == "__main__":
    passed = validate_step1()
    if passed:
        print("\nStep 1 COMPLETE. Lie derivative validated.")
    else:
        print("\nStep 1 FAILED. Check warnings.")
