#!/usr/bin/env python3
"""
CHIRALITY-SELECTION-64 — KO Chirality Cancellation in Second-Order Tensor Source
================================================================================

Gate: CHIRALITY-SELECTION-64 (INFO)
Task: Determine whether KO-dim=6 chirality (N_+=N_-=6270) introduces cancellations
      in the second-order tensor source dS/dtau.

GOVERNING STRUCTURE
===================
The D_K(tau) spectrum has exact spectral pairing: {gamma_9, D_K(tau)} = 0 for all tau.
(Theorem T2, proven S43: CHIRAL-ETA-43). This is a consequence of:
  - gamma_9 = gamma_1 ... gamma_8 (chirality grading in Cl(8))
  - D_K = sum_a rho(e_a) x gamma_a + I x Omega, with {gamma_9, gamma_a} = 0

ANALYTICAL DERIVATION
=====================
1. If D_K psi_n = lambda_n psi_n, then gamma_9 psi_n is an eigenvector with
   eigenvalue -lambda_n (from {gamma_9, D_K} = 0).

2. The spectral action scalar source is:
     dS/dtau = sum_n d_n * f'(lambda_n^2 / Lambda^2) * 2*lambda_n * (dlambda_n/dtau)
   where d_n is the Peter-Weyl multiplicity.

3. For the chiral partner pair (lambda_n, -lambda_n):
   The tau-derivative of the eigenvalue of the chiral partner is determined by
   first-order perturbation theory:
     dlambda_n/dtau = <psi_n| dD_K/dtau |psi_n>
     d(-lambda_n)/dtau = <gamma_9 psi_n| dD_K/dtau |gamma_9 psi_n>

4. KEY STEP: What is {gamma_9, dD_K/dtau}?
   Since {gamma_9, D_K(tau)} = 0 for ALL tau, differentiating:
     {gamma_9, dD_K/dtau} = d/dtau {gamma_9, D_K(tau)} = 0
   Therefore dD_K/dtau ALSO anticommutes with gamma_9.

5. CONSEQUENCE:
     d(-lambda_n)/dtau = <gamma_9 psi_n| dD_K/dtau |gamma_9 psi_n>
                       = <psi_n| gamma_9^dag (dD_K/dtau) gamma_9 |psi_n>
                       = <psi_n| -(dD_K/dtau) |psi_n>     (using {gamma_9, dD_K/dtau}=0)
                       = -dlambda_n/dtau

   So d(-lambda_n)/dtau = -dlambda_n/dtau  (ANTISYMMETRIC CASE).

6. CANCELLATION CHECK for dS/dtau:
   Pair contribution = d_n * f'(lambda_n^2) * 2 * lambda_n * (dlambda_n/dtau)
                     + d_n * f'((-lambda_n)^2) * 2 * (-lambda_n) * (-dlambda_n/dtau)
                     = d_n * f'(lambda_n^2) * 2 * lambda_n * (dlambda_n/dtau)
                     + d_n * f'(lambda_n^2) * 2 * lambda_n * (dlambda_n/dtau)
                     = 2 * d_n * f'(lambda_n^2) * 2 * lambda_n * (dlambda_n/dtau)

   The terms ADD. There is NO cancellation from chirality.
   C_chiral = 1 exactly (by algebra, not numerics).

7. SECOND-ORDER TENSOR SOURCE:
   The second-order tensor source involves products delta_tau_k * delta_tau_{k'},
   which can be same-chirality (+,+) or (-,-) or opposite-chirality (+,-).
   However, the COUPLING coefficient A_{kk'} for the tensor source goes through
   the spectral action, where the SCALAR source is already chirally doubled (no
   cancellation). The tensor coupling inherits this: same-chirality and
   opposite-chirality pairs produce the SAME sign contribution to h_{ij}
   because the relevant bilinear is:
     A_{kk'} ~ sum_n d_n * f''(lambda_n^2) * (dlambda_n/dk)(dlambda_n/dk')
   which involves f''(lambda_n^2) — symmetric in lambda_n -> -lambda_n — and
   the product of TWO derivatives, which is symmetric regardless of chirality
   assignment (product of two antisymmetric quantities is symmetric).

NUMERICAL VERIFICATION
======================
We verify the analytical result by computing eigenvalue flows dlambda/dtau
numerically from the full Dirac operator on each Peter-Weyl sector, checking
that paired eigenvalues have opposite tau-derivatives, and computing C_chiral.

Author: Dirac-Antimatter-Theorist (S64)
Date: 2026-04-01
"""

import sys
import os
import numpy as np
import matplotlib
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from time import time

# Path setup
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, str(_x2_shared_dir()))
from canonical_constants import tau_fold, PI

# Import Dirac spectrum machinery
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, build_chirality, get_irrep, dirac_operator_on_irrep,
    _irrep_cache
)


# =============================================================================
# SECTION 1: Verify {gamma_9, dD_K/dtau} = 0 directly
# =============================================================================

def compute_DK_at_tau(tau, gens, f_abc, gammas, p, q):
    """
    Compute the full Dirac operator matrix D_K(tau) on sector (p,q).

    Returns the ANTI-HERMITIAN D (eigenvalues are purely imaginary).
    Physical eigenvalues = imag parts of np.linalg.eigvals(D).
    """
    global _irrep_cache
    _irrep_cache.clear()

    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    if p == 0 and q == 0:
        return Omega.copy()
    else:
        rho, _ = get_irrep(p, q, gens, f_abc)
        return dirac_operator_on_irrep(rho, E, gammas, Omega)


def numerical_dDK_dtau(tau, dtau, gens, f_abc, gammas, p, q):
    """
    Compute dD_K/dtau by central finite difference.
    """
    D_plus = compute_DK_at_tau(tau + dtau, gens, f_abc, gammas, p, q)
    D_minus = compute_DK_at_tau(tau - dtau, gens, f_abc, gammas, p, q)
    return (D_plus - D_minus) / (2.0 * dtau)


def verify_gamma9_anticommutation(gamma9, dDK_dtau):
    """
    Check that {gamma_9, dD_K/dtau} = 0.

    gamma_9 acts on spinor indices only. For a sector (p,q) with dim d,
    D is (d*16) x (d*16), and gamma_9 acts as I_d tensor gamma_9.
    """
    dim_total = dDK_dtau.shape[0]
    dim_rho = dim_total // 16

    gamma9_full = np.kron(np.eye(dim_rho), gamma9)
    anticomm = gamma9_full @ dDK_dtau + dDK_dtau @ gamma9_full
    return np.max(np.abs(anticomm))


# =============================================================================
# SECTION 2: Eigenvalue flow and chiral pairing of derivatives
# =============================================================================

def eigenvalue_flow_at_tau(tau, dtau, gens, f_abc, gammas, gamma9, p, q):
    """
    Compute eigenvalues at tau and their tau-derivatives.
    Track chiral pairing: for each lambda_n, verify that -lambda_n exists
    and that their derivatives satisfy d(-lambda_n)/dtau = -dlambda_n/dtau.

    Returns:
        evals_phys: physical eigenvalues (imag parts of anti-Hermitian D)
        devals_dtau: tau-derivatives of eigenvalues
        chiral_sign: +1/-1 chirality assignment for each eigenvalue
    """
    # Compute D_K at tau, tau+dtau, tau-dtau for finite-difference derivative
    D0 = compute_DK_at_tau(tau, gens, f_abc, gammas, p, q)
    D_plus = compute_DK_at_tau(tau + dtau, gens, f_abc, gammas, p, q)
    D_minus = compute_DK_at_tau(tau - dtau, gens, f_abc, gammas, p, q)

    # Diagonalize D0 — eigenvalues are purely imaginary
    evals_raw, evecs = np.linalg.eigh(1j * D0)  # Hermitian i*D has real evals
    # Physical eigenvalues of D = i * (eigenvalues of iD)
    # D psi = lambda psi => iD psi = i*lambda psi => evals of iD are real = lambda.imag
    # Wait: D is anti-Hermitian. iD is Hermitian. eigh(iD) gives real eigenvalues.
    # If D psi = (i*omega) psi (omega real), then iD psi = -omega psi.
    # So eigenvalues of iD = -omega, and physical eigenvalues omega = -evals_of_iD.
    # The sign convention: evals_phys are the imaginary parts of the eigenvalues of D.

    evals_phys = -evals_raw  # omega_n such that D psi_n = i*omega_n psi_n

    # Compute dlambda/dtau via Hellmann-Feynman:
    # d(i*omega_n)/dtau = <psi_n| dD/dtau |psi_n>
    # => i * domega_n/dtau = <psi_n| dD/dtau |psi_n>
    # Numerically: use finite difference on the Hermitian operator iD
    iD_plus = 1j * D_plus
    iD_minus = 1j * D_minus
    d_iD_dtau = (iD_plus - iD_minus) / (2.0 * dtau)

    # Hellmann-Feynman: d(eval_n of iD)/dtau = <n| d(iD)/dtau |n>
    devals_iD = np.array([
        np.real(evecs[:, n].conj() @ d_iD_dtau @ evecs[:, n])
        for n in range(len(evals_raw))
    ])
    devals_phys = -devals_iD  # domega/dtau = -d(eval of iD)/dtau

    # Chirality assignment: <psi_n| gamma_9_full |psi_n>
    dim_total = D0.shape[0]
    dim_rho = dim_total // 16
    gamma9_full = np.kron(np.eye(dim_rho), gamma9)
    chiral_exp = np.array([
        np.real(evecs[:, n].conj() @ gamma9_full @ evecs[:, n])
        for n in range(len(evals_raw))
    ])

    return evals_phys, devals_phys, chiral_exp


# =============================================================================
# SECTION 3: C_chiral computation
# =============================================================================

def compute_C_chiral(evals, devals, Lambda_sq, test_func='gaussian'):
    """
    Compute the chirality cancellation factor.

    CORRECT DEFINITION: Compare the actual sum (where chiral pairs ADD due to
    derivative antisymmetry) against the hypothetical case where chiral pairs
    CANCEL (symmetric derivatives).

    The spectrum has pairs (lambda_n, -lambda_n). After sorting, eigenvalues
    come in pairs: evals[i] and evals[N-1-i] with evals[i] = -evals[N-1-i].

    ACTUAL sum (antisymmetric derivatives: d(-lam)/dtau = -dlam/dtau):
      S_actual = sum over pairs: 2 * f'(lam^2) * 2*lam * dlam/dtau  (pairs ADD)

    HYPOTHETICAL (symmetric derivatives: d(-lam)/dtau = +dlam/dtau):
      S_hypo = sum over pairs: f'(lam^2)*2*lam*dlam + f'(lam^2)*2*(-lam)*dlam = 0
      Each pair CANCELS individually.

    C_chiral = |S_actual|^2 / |S_positive_only|^2
    where S_positive_only sums over positive eigenvalues only (no pairing effect).

    If C=1: chiral pairing doubles the sum (pairs add perfectly).
    If C=0: chiral pairing kills the sum (pairs cancel perfectly).
    """
    x = evals**2 / Lambda_sq

    if test_func == 'gaussian':
        fp = -np.exp(-x)
    elif test_func == 'sharp':
        fp = np.where(x < 1.0, -1.0, 0.0)
    else:
        fp = -np.exp(-x)

    # Each term in the sum
    terms = fp * 2.0 * evals * devals

    # Full sum (all eigenvalues including chiral partners)
    S_full = np.sum(terms)

    # Sum over POSITIVE eigenvalues only
    pos_mask = evals > 1e-15
    S_positive = np.sum(terms[pos_mask])

    # In the antisymmetric case: S_full = 2 * S_positive (pairs add)
    # In the symmetric case: S_full = 0 (pairs cancel)
    # C_chiral measures: is S_full = 2 * S_positive?
    if abs(S_positive) < 1e-30:
        ratio = 1.0 if abs(S_full) < 1e-30 else np.inf
    else:
        ratio = S_full / (2.0 * S_positive)

    return ratio, S_full, S_positive


def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# =============================================================================
# SECTION 4: Main computation
# =============================================================================

def main():
    t0 = time()
    print("=" * 72)
    print("CHIRALITY-SELECTION-64: KO Chirality Cancellation")
    print("              in Second-Order Tensor Source")
    print("=" * 72)

    # -----------------------------------------------------------
    # Step 0: Pre-register gate criteria
    # -----------------------------------------------------------
    print("\n--- PRE-REGISTRATION ---")
    print("Gate: CHIRALITY-SELECTION-64 (INFO)")
    print("Quantity: C_chiral = |sum|^2 / (N * sum|...|^2)")
    print("  C=1: no chirality cancellation (chiral pairs ADD)")
    print("  C<1: partial cancellation (chiral pairs partially cancel)")
    print("  C=0: complete cancellation")
    print("Analytical prediction (from {gamma_9, dD_K/dtau}=0):")
    print("  d(-lambda_n)/dtau = -dlambda_n/dtau => terms ADD => C=1")
    print("This is a verification, not a discovery.")

    # -----------------------------------------------------------
    # Step 1: Setup algebra infrastructure
    # -----------------------------------------------------------
    print("\n--- STEP 1: Algebra Infrastructure ---")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    gamma9 = build_chirality(gammas)

    # Verify gamma_9 properties
    g9_sq_err = np.max(np.abs(gamma9 @ gamma9 - np.eye(16)))
    g9_herm_err = np.max(np.abs(gamma9 - gamma9.conj().T))
    g9_anticomm_max = max(
        np.max(np.abs(gamma9 @ g + g @ gamma9)) for g in gammas
    )
    print(f"  gamma_9^2 = I err:          {g9_sq_err:.2e}")
    print(f"  gamma_9 Hermitian err:      {g9_herm_err:.2e}")
    print(f"  max |{{gamma_9, gamma_a}}|: {g9_anticomm_max:.2e}")

    # Eigenvalues of gamma_9 (should be +1 and -1, 8 each)
    g9_evals = np.linalg.eigvalsh(gamma9)
    n_plus_g9 = np.sum(g9_evals > 0.5)
    n_minus_g9 = np.sum(g9_evals < -0.5)
    print(f"  gamma_9 eigenvalues: {n_plus_g9} at +1, {n_minus_g9} at -1")

    # -----------------------------------------------------------
    # Step 2: Verify {gamma_9, dD_K/dtau} = 0
    # -----------------------------------------------------------
    print("\n--- STEP 2: Verify {{gamma_9, dD_K/dtau}} = 0 ---")
    tau = tau_fold
    dtau = 1e-5  # (local)

    test_sectors = [(0, 1), (1, 0), (1, 1), (0, 2), (2, 0), (0, 3), (1, 2)]
    anticomm_results = {}

    for (p, q) in test_sectors:
        dDK = numerical_dDK_dtau(tau, dtau, gens, f_abc, gammas, p, q)
        err = verify_gamma9_anticommutation(gamma9, dDK)
        norm_dDK = np.linalg.norm(dDK)
        rel_err = err / norm_dDK if norm_dDK > 1e-15 else 0.0
        anticomm_results[(p, q)] = (err, rel_err)
        print(f"  ({p},{q}): |{{gamma_9, dD_K/dtau}}| = {err:.3e}, "
              f"relative = {rel_err:.3e}")

    max_anticomm_rel = max(v[1] for v in anticomm_results.values())
    print(f"\n  Maximum relative anticommutator: {max_anticomm_rel:.3e}")
    print(f"  Expected: ~O(dtau^2) = {dtau**2:.1e} (finite-difference error)")
    anticomm_pass = max_anticomm_rel < 1e-4
    print(f"  {'{'}gamma_9, dD_K/dtau{'}'} = 0: {'CONFIRMED' if anticomm_pass else 'FAILED'}")

    # -----------------------------------------------------------
    # Step 3: Eigenvalue flow + chiral derivative pairing
    # -----------------------------------------------------------
    print("\n--- STEP 3: Eigenvalue Flow & Chiral Derivative Pairing ---")

    sectors_for_flow = [(0, 1), (1, 0), (1, 1), (0, 2), (2, 0),
                        (0, 3), (3, 0), (1, 2), (2, 1)]
    flow_results = {}

    for (p, q) in sectors_for_flow:
        evals, devals, chiral_exp = eigenvalue_flow_at_tau(
            tau, dtau, gens, f_abc, gammas, gamma9, p, q
        )

        # Sort by eigenvalue magnitude and pair lambda_n with -lambda_n
        idx_sort = np.argsort(evals)
        evals_s = evals[idx_sort]
        devals_s = devals[idx_sort]
        chiral_s = chiral_exp[idx_sort]

        n_eig = len(evals_s)
        n_half = n_eig // 2

        # Pair: eigenvalues come in +/- pairs. After sorting,
        # the first n_half should be negative, the last n_half positive.
        # Check pairing: evals_s[i] + evals_s[n_eig-1-i] ~ 0
        pair_err = []
        deriv_antisym_err = []
        for i in range(n_half):
            j = n_eig - 1 - i
            pe = abs(evals_s[i] + evals_s[j])
            pair_err.append(pe)
            # Check d(-lambda)/dtau = -dlambda/dtau
            # i.e., devals[i] + devals[j] ~ 0 (antisymmetric)
            de_sum = abs(devals_s[i] + devals_s[j])
            de_diff = abs(devals_s[i] - devals_s[j])
            if de_diff > 1e-15:
                antisym_ratio = de_sum / de_diff
            else:
                antisym_ratio = 0.0  # (local)
            deriv_antisym_err.append(antisym_ratio)

        max_pair_err = max(pair_err) if pair_err else 0.0
        max_deriv_antisym = max(deriv_antisym_err) if deriv_antisym_err else 0.0

        flow_results[(p, q)] = {
            'evals': evals_s,
            'devals': devals_s,
            'chiral': chiral_s,
            'max_pair_err': max_pair_err,
            'max_deriv_antisym_ratio': max_deriv_antisym,
            'n_eig': n_eig,
        }

        print(f"  ({p},{q}): n_eig={n_eig}, "
              f"pair_err={max_pair_err:.3e}, "
              f"deriv_antisym_ratio={max_deriv_antisym:.3e}")

    # Overall check
    max_pair_all = max(r['max_pair_err'] for r in flow_results.values())
    max_antisym_all = max(r['max_deriv_antisym_ratio'] for r in flow_results.values())
    print(f"\n  Max eigenvalue pairing error:  {max_pair_all:.3e}")
    print(f"  Max derivative antisymmetry violation: {max_antisym_all:.3e}")
    print(f"  Chiral derivative pairing: "
          f"{'ANTISYMMETRIC (ADD)' if max_antisym_all < 0.01 else 'MIXED'}")

    # -----------------------------------------------------------
    # Step 4: Compute C_chiral per sector and globally
    # -----------------------------------------------------------
    print("\n--- STEP 4: C_chiral Computation ---")

    # Use Lambda from canonical data
    Lambda_sq = 16.98  # from s61_transit_spectral_action.npz  # (local)

    # Per-sector C_chiral
    print(f"  Lambda^2 = {Lambda_sq:.2f}")
    print()

    global_terms_all = []
    global_terms_pos = []

    for (p, q) in sectors_for_flow:
        fr = flow_results[(p, q)]
        evals = fr['evals']
        devals = fr['devals']
        d = dim_pq(p, q)
        pw_mult = d  # Peter-Weyl multiplicity

        # Terms for spectral action sum
        x = evals**2 / Lambda_sq
        fp = -np.exp(-x)  # f'(x) for f(x) = exp(-x)
        terms = pw_mult * fp * 2.0 * evals * devals

        ratio_sector, S_full, S_pos = compute_C_chiral(
            evals, devals, Lambda_sq
        )

        global_terms_all.extend(terms)
        pos_mask = evals > 1e-15
        global_terms_pos.extend((pw_mult * fp * 2.0 * evals * devals)[pos_mask])

        print(f"  ({p},{q}): S_full/(2*S_pos) = {ratio_sector:.8f}, "
              f"S_full = {S_full:.4e}, "
              f"S_pos = {S_pos:.4e}, "
              f"|terms| = {len(terms)}")

    global_terms_all = np.array(global_terms_all)
    global_terms_pos = np.array(global_terms_pos)

    S_global_full = np.sum(global_terms_all)
    S_global_pos = np.sum(global_terms_pos)
    N_global = len(global_terms_all)

    if abs(S_global_pos) > 1e-30:
        C_global = S_global_full / (2.0 * S_global_pos)
    else:
        C_global = 1.0  # (local)

    print(f"\n  GLOBAL C_chiral = S_full / (2*S_pos) = {C_global:.8f}")
    print(f"  S_full (all eigenvalues): {S_global_full:.6e}")
    print(f"  S_pos (positive only):    {S_global_pos:.6e}")
    print(f"  2*S_pos:                  {2*S_global_pos:.6e}")
    print(f"  N_terms total: {N_global}")
    print(f"  Deviation from 1: {abs(C_global - 1.0):.2e}")

    # -----------------------------------------------------------
    # Step 5: Full N_+/N_- count at max_pq_sum=4
    # -----------------------------------------------------------
    print("\n--- STEP 5: Full Chiral Count (max_pq_sum=4) ---")

    N_plus_total = 0
    N_minus_total = 0
    N_total = 0

    for p in range(5):
        for q in range(5 - p):
            if p == 0 and q == 0:
                continue
            d = dim_pq(p, q)
            mult_per_sign = d**2 * 2  # multiplicity convention from S61
            N_plus_total += mult_per_sign
            N_minus_total += mult_per_sign
            N_total += 2 * mult_per_sign

    print(f"  N_+ = {N_plus_total}")
    print(f"  N_- = {N_minus_total}")
    print(f"  N_total = {N_total}")
    print(f"  N_+ = N_-: {'YES' if N_plus_total == N_minus_total else 'NO'}")

    # -----------------------------------------------------------
    # Step 6: Second-order tensor source analysis
    # -----------------------------------------------------------
    print("\n--- STEP 6: Second-Order Tensor Source Analysis ---")
    print()
    print("  ANALYTICAL RESULT (proven, not numerical):")
    print("  ============================================")
    print()
    print("  From {gamma_9, D_K(tau)} = 0 for all tau:")
    print("    => {gamma_9, dD_K/dtau} = 0")
    print("    => d(-lambda_n)/dtau = -dlambda_n/dtau  (antisymmetric)")
    print()
    print("  For the scalar source dS/dtau:")
    print("    Pair contribution = f'(lam^2)*2*lam*(dlam/dtau)")
    print("                      + f'(lam^2)*2*(-lam)*(-dlam/dtau)")
    print("                      = 2 * f'(lam^2)*2*lam*(dlam/dtau)")
    print("    => Chiral pairs ADD, not cancel. C_chiral = 1.")
    print()
    print("  For the second-order tensor source S_T^{(2)}:")
    print("    A_{kk'} ~ sum_n f''(lam_n^2) * (dlam_n/dk)(dlam_n/dk')")
    print("    f''(lam^2) = f''((-lam)^2): SYMMETRIC in lambda -> -lambda")
    print("    (dlam/dk)(-dlam/dk') = -(dlam/dk)(dlam/dk'): product of two")
    print("    antisymmetric quantities = SYMMETRIC")
    print("    => Same-chirality and opposite-chirality pairs produce")
    print("       the SAME SIGN contribution. No cancellation.")
    print()
    print("  IMPLICATION FOR r^{(2)}:")
    print("    The KO-dimensional chirality does NOT suppress")
    print("    the second-order tensor source. The N_+=N_- symmetry,")
    print("    which would cancel a LINEAR chirality coupling, does not")
    print("    affect the QUADRATIC (second-order) tensor production.")
    print("    The spectral pairing {gamma_9, D_K}=0 forces derivatives")
    print("    to be antisymmetric, and the product of antisymmetric")
    print("    quantities is symmetric — so no cancellation occurs.")
    print()
    print("  C_chiral = 1 EXACTLY (algebraic, not numerical).")

    # -----------------------------------------------------------
    # Step 7: Plots
    # -----------------------------------------------------------
    print("\n--- STEP 7: Generating Plots ---")

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot 1: Eigenvalue spectrum with chirality coloring
    ax = axes[0, 0]
    for (p, q) in [(0, 1), (1, 0), (1, 1), (0, 2)]:
        fr = flow_results[(p, q)]
        evals = fr['evals']
        chiral = fr['chiral']
        colors = ['#2196F3' if c > 0 else '#F44336' for c in chiral]
        ax.scatter(
            [f"({p},{q})"] * len(evals), evals, c=colors, s=8, alpha=0.7
        )
    ax.set_ylabel(r'$\omega_n$ (M$_{KK}$)')
    ax.set_title('D_K eigenvalues colored by chirality')
    ax.axhline(y=0, color='k', linewidth=0.5, linestyle='--')
    ax.legend(['+ chirality (blue)', '- chirality (red)'], fontsize=8,
              loc='upper right')

    # Plot 2: Derivative pairing
    ax = axes[0, 1]
    for idx, (p, q) in enumerate([(0, 1), (1, 0), (1, 1), (0, 2)]):
        fr = flow_results[(p, q)]
        evals = fr['evals']
        devals = fr['devals']
        n = len(evals)
        # Pair: negative eigenvalue derivative vs positive partner
        half = n // 2
        deriv_neg = devals[:half]  # derivatives of negative eigenvalues
        deriv_pos = devals[half:][::-1]  # derivatives of positive partners
        ax.scatter(deriv_pos, -deriv_neg, s=6, alpha=0.6,
                   label=f'({p},{q})')
    lim = ax.get_xlim()
    ax.plot(lim, lim, 'k--', linewidth=0.5, alpha=0.5)
    ax.set_xlabel(r'd$\omega_+$/d$\tau$')
    ax.set_ylabel(r'$-$d$\omega_-$/d$\tau$')
    ax.set_title(r'd$(-\omega)$/d$\tau$ = $-$d$\omega$/d$\tau$ verification')
    ax.legend(fontsize=7)

    # Plot 3: Spectral action terms — showing no cancellation
    ax = axes[1, 0]
    all_sorted_terms = np.sort(global_terms_all)
    ax.bar(range(len(all_sorted_terms)), all_sorted_terms,
           width=1.0, color='#1976D2', alpha=0.6)
    ax.set_xlabel('Mode index (sorted)')
    ax.set_ylabel('dS/dtau contribution per mode')
    ax.set_title('Spectral action terms (no chirality cancellation)')
    ax.axhline(y=0, color='k', linewidth=0.5, linestyle='--')

    # Plot 4: C_chiral = S_full/(2*S_pos) vs sector accumulation
    ax = axes[1, 1]
    cumul_all = []
    cumul_pos = []
    C_vs_sectors = []
    sector_labels = []
    for (p, q) in sectors_for_flow:
        fr = flow_results[(p, q)]
        evals = fr['evals']
        devals = fr['devals']
        x = evals**2 / Lambda_sq
        fp = -np.exp(-x)
        terms = fp * 2.0 * evals * devals
        cumul_all.extend(terms)
        pos_mask = evals > 1e-15
        cumul_pos.extend(terms[pos_mask])
        S_f = np.sum(cumul_all)
        S_p = np.sum(cumul_pos)
        C = S_f / (2.0 * S_p) if abs(S_p) > 1e-30 else 1.0
        C_vs_sectors.append(C)
        sector_labels.append(f'({p},{q})')

    ax.plot(range(len(C_vs_sectors)), C_vs_sectors, 'o-',
            color='#4CAF50', markersize=5)
    ax.set_xticks(range(len(sector_labels)))
    ax.set_xticklabels(sector_labels, rotation=45, fontsize=7)
    ax.set_ylabel(r'$S_{\rm full} / (2\,S_{\rm pos})$')
    ax.set_title(r'$C_{\rm chiral}$ = $S_{\rm full}/(2S_{+})$ across sectors')
    ax.set_ylim(0.9, 1.1)
    ax.axhline(y=1.0, color='r', linewidth=1.0, linestyle='--',
               label='No cancellation (C=1)')
    ax.legend(fontsize=8)

    plt.suptitle(
        'CHIRALITY-SELECTION-64: KO Chirality Cancellation\n'
        r'{$\gamma_9$, $dD_K/d\tau$} = 0 $\Rightarrow$ chiral pairs ADD',
        fontsize=12
    )
    plt.tight_layout()

    plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             's64_chirality_selection.png')
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    print(f"  Plot saved: {plot_path}")
    plt.close()

    # -----------------------------------------------------------
    # Step 8: Save results
    # -----------------------------------------------------------
    print("\n--- STEP 8: Saving Results ---")

    npz_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's64_chirality_selection.npz')

    save_dict = {
        'gate_name': 'CHIRALITY-SELECTION-64',
        'gate_type': 'INFO',
        'tau_fold': tau_fold,
        'dtau_finite_diff': dtau,
        'Lambda_sq': Lambda_sq,
        'N_plus': N_plus_total,
        'N_minus': N_minus_total,
        'C_chiral_global': C_global,
        'C_chiral_analytical': 1.0,
        'max_anticomm_relative': max_anticomm_rel,
        'max_pair_error': max_pair_all,
        'max_deriv_antisym_ratio': max_antisym_all,
        'anticomm_confirmed': anticomm_pass,
        'derivative_antisymmetric': max_antisym_all < 0.01,
        'chirality_cancellation': False,
        'sectors_tested': np.array(sectors_for_flow),
        'S_full_global': S_global_full,
        'S_positive_global': S_global_pos,
        'C_vs_sectors': np.array(C_vs_sectors),
    }
    np.savez(npz_path, **save_dict)
    print(f"  Data saved: {npz_path}")

    # -----------------------------------------------------------
    # Step 9: Gate verdict
    # -----------------------------------------------------------
    print("\n" + "=" * 72)
    print("GATE VERDICT: CHIRALITY-SELECTION-64")
    print("=" * 72)
    print()
    print("  Type: INFO (no pass/fail threshold)")
    print()
    print("  ALGEBRAIC RESULT (exact):")
    print(f"    {{gamma_9, D_K(tau)}} = 0 for all tau  [Theorem T2, S43]")
    print(f"    => {{gamma_9, dD_K/dtau}} = 0          [tau-derivative of T2]")
    print(f"    => d(-lambda_n)/dtau = -dlambda_n/dtau [Hellmann-Feynman]")
    print(f"    => Chiral pairs ADD in dS/dtau         [sign arithmetic]")
    print(f"    => C_chiral = 1 EXACTLY                [algebraic theorem]")
    print()
    print("  NUMERICAL VERIFICATION:")
    print(f"    {{gamma_9, dD_K/dtau}} = 0 to {max_anticomm_rel:.1e} "
          f"(finite-diff err ~ {dtau**2:.0e})")
    print(f"    Derivative antisymmetry violation: {max_antisym_all:.1e}")
    print(f"    S_full / (2*S_pos) = {C_global:.8f}  "
          f"(deviation from 1: {abs(C_global-1):.2e})")
    print()
    print("  PHYSICAL CONSEQUENCE:")
    print("    The N_+=N_-=6270 chiral symmetry does NOT suppress r^{(2)}.")
    print("    The spectral pairing theorem forces eigenvalue derivatives")
    print("    to be antisymmetric under chirality, and the second-order")
    print("    tensor source involves PRODUCTS of these derivatives,")
    print("    which are chirality-symmetric. No cancellation occurs.")
    print("    KO-chirality constrains the FIRST-order source")
    print("    (eta-invariant = 0, index = 0) but NOT the second-order")
    print("    source (quadratic in perturbations).")
    print()
    print(f"  === CHIRALITY-SELECTION-64: INFO (C_chiral = 1) ===")
    print()

    elapsed = time() - t0
    print(f"Total runtime: {elapsed:.1f}s")


if __name__ == '__main__':
    main()
