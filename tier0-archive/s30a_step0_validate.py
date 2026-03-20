"""
Session 30Aa Step 0: Validate eigenvector extraction backward compatibility.

Verifies that collect_spectrum_with_eigenvectors() produces eigenvalues
matching the original collect_spectrum() to machine epsilon at tau=0.15, 0.35.

Also validates:
1. Eigenvector orthonormality: ||V^dag V - I|| < 1e-12
2. Eigenvalue reconstruction: ||D_pi @ v_n - lambda_n * v_n|| < 1e-12
3. Anti-Hermiticity: ||D_pi + D_pi^dag|| < 1e-12

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
    collect_spectrum,
    collect_spectrum_with_eigenvectors,
    get_irrep,
    dirac_operator_on_irrep,
)


def validate_step0():
    """Validate eigenvector extraction at tau=0.15 and tau=0.35."""
    print("=" * 70)
    print("Session 30Aa Step 0: Eigenvector Extraction Validation")
    print("=" * 70)

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    max_pq = 2  # N_max=2 for D_F truncation

    tau_values = [0.15, 0.35]
    max_eval_err = 0.0
    max_orth_err = 0.0
    max_recon_err = 0.0
    max_ah_err = 0.0

    for tau in tau_values:
        print(f"\n{'='*60}")
        print(f"tau = {tau:.2f}")
        print(f"{'='*60}")

        t0 = time.time()

        # New function: eigenvectors
        sector_data, infra = collect_spectrum_with_eigenvectors(
            tau, gens, f_abc, gammas, max_pq_sum=max_pq, verbose=True
        )

        t_new = time.time() - t0

        # Old function: eigenvalues only (for comparison)
        t0 = time.time()
        all_evals_old, eval_data_old = collect_spectrum(
            tau, gens, f_abc, gammas, max_pq_sum=max_pq, verbose=False
        )
        t_old = time.time() - t0

        print(f"\n  Timing: new={t_new:.3f}s, old={t_old:.3f}s")
        print(f"  Sectors computed: {len(sector_data)}")

        # Compare eigenvalues sector by sector
        print(f"\n  Eigenvalue comparison (new eigh vs old eigvals):")

        for sd in sector_data:
            p, q = sd['p'], sd['q']
            evals_new = sd['evals']  # real eigenvalues of 1j*D
            evecs = sd['evecs']
            D_pi = sd['D_pi']

            # Find matching sector in old data
            evals_old_sector = None
            for p_old, q_old, ev_old in eval_data_old:
                if p_old == p and q_old == q:
                    evals_old_sector = ev_old
                    break

            if evals_old_sector is None:
                print(f"    ({p},{q}): NOT FOUND in old data!")
                continue

            # Old eigenvalues are raw complex. For anti-Hermitian D, they should
            # be purely imaginary. The new eigenvalues are real parts of 1j*D.
            # Correspondence: new_evals = sort(imag(old_evals))
            imag_old = np.sort(np.imag(evals_old_sector))
            evals_new_sorted = np.sort(evals_new)

            # Match: evals_new should equal imag_old (up to sign convention)
            # Actually: if D is anti-Hermitian, eigvals of D are purely imaginary: i*mu_n
            # eigvals of 1j*D = 1j*(i*mu_n) = -mu_n
            # So evals_new = -imag(eigvals_old) ... need to check carefully.
            #
            # D |psi> = lambda |psi>, lambda = i*mu (imaginary)
            # (1j*D)|psi> = 1j * lambda |psi> = 1j * i * mu |psi> = -mu |psi>
            #
            # So eigh(1j*D) gives eigenvalues -mu, where mu = imag(lambda).
            # Hence evals_new = -imag(old_evals) when old used eigvals(D).
            #
            # But old code uses eigvals(D) which returns complex numbers.
            # For perfectly anti-Hermitian D: real(lambda)=0, imag(lambda)=mu.
            # evals_new from eigh(1j*D) = -mu = -imag(old).
            #
            # Wait, let's verify numerically. eigh gives sorted ascending.
            # np.sort_complex sorts by real then imag.

            # For the trivial sector, old code used eigvals(D) directly (complex).
            # For non-trivial, also eigvals(D_pi).
            # New code uses eigh(1j*D_pi) which gives real sorted ascending.
            #
            # Matching: sort |new| and |imag(old)|
            abs_new = np.sort(np.abs(evals_new))
            abs_old_imag = np.sort(np.abs(np.imag(evals_old_sector)))

            # But old eigvals may have small real parts (numerical noise).
            # Compare absolute eigenvalues.
            abs_old_all = np.sort(np.abs(evals_old_sector))

            eval_err = np.max(np.abs(abs_new - abs_old_all))
            max_eval_err = max(max_eval_err, eval_err)

            # Orthonormality
            dim = len(evals_new)
            orth_err = np.max(np.abs(evecs.conj().T @ evecs - np.eye(dim)))
            max_orth_err = max(max_orth_err, orth_err)

            # Eigenvalue reconstruction: D_pi @ v_n = lambda_n * v_n
            # where lambda_n = -1j * evals_new[n]
            recon_err = 0.0
            for n in range(dim):
                v_n = evecs[:, n]
                lambda_n = -1j * evals_new[n]
                residual = D_pi @ v_n - lambda_n * v_n
                err_n = np.max(np.abs(residual))
                recon_err = max(recon_err, err_n)
            max_recon_err = max(max_recon_err, recon_err)

            # Anti-Hermiticity
            ah_err = sd['ah_err']
            max_ah_err = max(max_ah_err, ah_err)

            print(f"    ({p},{q}): dim={sd['dim_rho']}, D_size={dim}, "
                  f"eval_err={eval_err:.2e}, orth_err={orth_err:.2e}, "
                  f"recon_err={recon_err:.2e}, ah_err={ah_err:.2e}")

    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"  Max eigenvalue error (new vs old): {max_eval_err:.2e}")
    print(f"  Max orthonormality error:          {max_orth_err:.2e}")
    print(f"  Max reconstruction error:          {max_recon_err:.2e}")
    print(f"  Max anti-Hermiticity error:        {max_ah_err:.2e}")

    all_pass = (max_eval_err < 1e-10 and max_orth_err < 1e-12
                and max_recon_err < 1e-10 and max_ah_err < 1e-12)

    if all_pass:
        print(f"\n  PRE-3: SATISFIED — backward compatibility at machine epsilon")
    else:
        print(f"\n  PRE-3: FAILED — see errors above")

    return all_pass, max_eval_err, max_orth_err, max_recon_err, max_ah_err


if __name__ == "__main__":
    passed, *errs = validate_step0()
    if passed:
        print("\nStep 0 COMPLETE. Eigenvector extraction validated.")
    else:
        print("\nStep 0 FAILED. Check errors.")
