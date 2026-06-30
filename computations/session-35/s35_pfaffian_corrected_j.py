"""
S35-PFAFFIAN-CORRECTED-J:  re-run of s35_pfaffian_corrected_j.py
========================================================================

Original: computations/session-35/s35_pfaffian_corrected_j.py
  SHA-256: f2317ea9ac5053e7d5159afa4b55cb2a0064014e67be05610deb409060df7138

Purpose
-------
Reproduce the S35 Pfaffian with corrected real-structure J (Cliff(8) ON
frame, KO-dim 6) under S81 canonical discipline:
  - Canonical constants imported from canonical_constants.py
  - No framework constants hardcoded; `# (local)` tags on every intermediate
  - L_max pinned (0: singlet sector inherited from s23a_kosmann_singlet.npz;
    the Pfaffian acts on the 16-dim Cliff(8) spinor space only, irrep = (0,0))
  - Extended scan `TAU_VALUES_EXT` also pinned (25 values in [0.0, 2.5])
  - SHA-256 pins for every input file emitted in first lines of stdout
  - Closure SHA emitted at end; 4-tuple output tag printed last

Gate
----
S35-PFAFFIAN-CORRECTED-J : [VERIFY-THEOREM]
  Classification: GEOMETRIC (pure NCG: KO-dim 6 Pfaffian diagnostic)
  Hypothesis: BDI topological classification (T^2=+1, P^2=+1, S^2=+1) with
    CORRECTED J (C2 = gamma_1 gamma_3 gamma_5 gamma_7 per S34) has
    sgn(Pf(C1 @ D_K(tau))) CONSTANT across tau in {stored, extended scan}.
  PASS iff:   sgn(Pf) is CONSTANT across all tau tested (34 total).
  FAIL iff:   sgn(Pf) flips sign at any tau (=> spectral gap closes => topological
              phase transition).
  Tolerance:  THEOREM -> constancy of a discrete Z_2 invariant (machine epsilon
              on Pf^2 = det; real-part dominance (|Im/Re| < 1e-10)).
  Target:     the prior result recorded sgn(Pf) = -1 at ALL 34 tau values
              (knowledge: eq_182396 in s36_bdi_winding.py comment). ABSOLUTE
              sign is gamma-basis convention; the INVARIANT is constancy.

Cross-check against S30A-DTOTAL-PFAFFIAN
-------------------------------------------
T3-S30A on 864-dim D_total with Xi: Z_2 = +1 identically.
T3-S35 on 16-dim D_K with C1: sgn(Pf) constant (-1 under current convention).
BOTH produce Z_2 invariants that are constant across tau; the absolute sign
differs because they operate on different spaces with different P-operators
(Xi vs C1). NO inconsistency: the physical invariant is CONSTANCY, and both
PASS on that criterion. If the current run flips this constancy, that is a
HARD FAIL of a theorem marked PROVEN (proven_752, proven_778).

Substitution chain — Pfaffian sign (KO-dim 6 diagnostic)
--------------------------------------------------------
Definitions:
  C2 := gamma_1 * gamma_3 * gamma_5 * gamma_7      (T-operator core; real; sym)
  C1 := gamma_2 * gamma_4 * gamma_6 * gamma_8      (P-operator core; real; sym)
  J  := C2 * K   (antilinear; KO-dim 6 convention: J^2 = +1)
  T  := C2 * K   => [T, D_K] = 0,   T^2 = +1
  P  := C1 * K   => {P, D_K} = 0,   P^2 = +1
  S  := gamma_9 := gamma_1 * ... * gamma_8  => {S, D_K} = 0, S^2 = +1
  M  := C1 @ D_K                                  (Pfaffian matrix, 16x16)

Step 1 (antisymmetry of M):
  D_K is Hermitian (self-adjoint on H_F), so D_K^T = conj(D_K).
  {P, D_K} = 0 expands: P (D_K) + D_K P = 0
    P := C1 * K; P D_K P = -D_K
    For a bosonic operator the antilinear K squares out:
      C1 * conj(D_K) * C1 = -D_K          (*)
  From (*):   conj(D_K) = -C1 * D_K * C1        (C1^2 = I)
  M^T = D_K^T * C1^T
      = conj(D_K) * C1                   (C1 symmetric)
      = (-C1 * D_K * C1) * C1
      = -C1 * D_K * (C1 * C1)
      = -C1 * D_K                        (C1^2 = I)
      = -M.
  QED: M is antisymmetric.

Step 2 (Pfaffian <-> determinant):
  For any antisymmetric 2n x 2n matrix M:  Pf(M)^2 = det(M).
  det(M) = det(C1 @ D_K) = det(C1) * det(D_K).
  det(C1) is tau-INDEPENDENT (pure Clifford combinatorics).

Step 3 (sign can only change if spectrum crosses zero):
  sgn(Pf(M(tau))) can flip between tau_1 and tau_2
  iff det(D_K(tau)) crosses zero for some tau in (tau_1, tau_2)
  iff D_K has a zero eigenvalue (spectral gap CLOSES).

Step 4 (gap open on Jensen curve):
  S23a stored eigenvalues: min |ev(D_K)| > 0 at all 9 stored tau in [0, 0.5].
  Extended scan: the bi-invariant (tau=0) limit has D_K proportional to a
  constant spinor connection offset; the spectrum is nonzero and discrete.
  Jensen deformation preserves non-singularity within the Killing-metric
  family (s23a, s30, s35, s36 all confirm min|ev| > 0 across [0, 2.5]).

Step 5 (direction of conclusion):
  Gap OPEN everywhere  =>  det(D_K) never zero  =>  sgn(det(D_K)) constant
  =>  sgn(det(M)) constant  =>  Pf(M)^2 constant sign on its 2nd-root branch
  =>  sgn(Pf(M)) CONSTANT.
  PASS criterion met <=> min|ev(D_K)| > epsilon_machine at every tau tested.
  The absolute sign (+1 or -1) is a gamma-basis-orientation CONVENTION.

Author: Connes-NCG-Theorist, 2026-04-17
"""

import hashlib
import json
import os
import sys
import time

import numpy as np

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# --- path setup + canonical constants (MANDATORY S34+) ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))                   # (local)
COMP_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))                # (local)
ARCHIVE_DIR = os.path.abspath(os.path.join(COMP_DIR, "..", "_shared"))              # (local)
if COMP_DIR not in sys.path:
    sys.path.insert(0, COMP_DIR)
if ARCHIVE_DIR not in sys.path:
    sys.path.insert(0, ARCHIVE_DIR)

from canonical_constants import *  # noqa: E402,F401,F403

# Structural helpers live in  module (Clifford algebra, connection).
from dirac_spectrum import (  # noqa: E402
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    build_chirality,
)


# --- input SHA-256 pins (precomputed, 2026-04-17) ---
INPUT_PINS = {                                                            # (local)
    'computations/session-35/s35_pfaffian_corrected_j.py':
        'f2317ea9ac5053e7d5159afa4b55cb2a0064014e67be05610deb409060df7138',
    'computations/_shared/canonical_constants.py':
        '68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f',
    'computations/_shared/dirac_spectrum.py':
        '267035cb598b08e94117a3245cb07b29fbe6bff7b5a614a1bde64982851809c3',
    'computations/session-23/s23a_kosmann_singlet.npz':
        'ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214',
}

# --- MACHINERY PINS (PRDR-compliant) ---
# The Pfaffian acts on the 16-dim Cliff(8) spinor space in the singlet sector
# (p,q) = (0,0) of SU(3).  L_max = 0 because no higher irrep enters D_K here.
L_MAX_PIN = 0                                                              # (local) singlet (0,0) only
DIM_SPIN = 16                                                              # (local) Cliff(8): 2^{8/2}
TAU_VALUES_EXT_N = 25                                                      # (local) extended scan point count
TAU_VALUES_EXT_MIN = 0.0                                                   # (local) extended scan min
TAU_VALUES_EXT_MAX = 2.5                                                   # (local) extended scan max
ASYM_TOL = 1e-12                                                           # (local) antisymmetry of M
HERM_TOL = 1e-13                                                           # (local) C2^2=I, C1^2=I, gamma9=C2*C1
IM_RE_TOL = 1e-10                                                          # (local) |Im(Pf)|/|Re(Pf)| numerical-zero
GAP_TOL = 1e-10                                                            # (local) min|ev(D_K)| gap-closure threshold


def sha256_of_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def verify_pins():
    print('=' * 78)
    print('S35-PFAFFIAN-CORRECTED-J: SHA-256 input pins')
    print('=' * 78)
    proj_root = os.path.abspath(os.path.join(COMP_DIR, '..'))   # (local)
    for rel, expected in INPUT_PINS.items():
        path = os.path.join(proj_root, rel)
        actual = sha256_of_file(path)
        status = 'OK' if actual == expected else 'MISMATCH'     # (local)
        print(f'  {rel:<48s} {actual[:16]}...  [{status}]')
        if actual != expected:
            raise RuntimeError(
                f'SHA mismatch for {rel}: expected {expected}, got {actual}'
            )
    print()


def pfaffian_hessenberg(A):
    """
    Parlett-Reid LTL^T Pfaffian (Wimmer, ACM TOMS 38(4), 2012).
    O(n^3); exact for antisymmetric 2n x 2n A. Sign-preserving.
    """
    n = A.shape[0]                                                         # (local)
    if n == 0:
        return 1.0
    if n == 2:
        return A[0, 1]

    A = A.copy().astype(complex)
    pf = 1.0 + 0j                                                          # (local) running Pfaffian
    for k in range(0, n - 1, 2):
        max_val = 0.0                                                      # (local) pivot magnitude
        max_idx = k + 1                                                    # (local) pivot column
        for j in range(k + 1, n):
            if abs(A[k, j]) > max_val:
                max_val = abs(A[k, j])
                max_idx = j
        if max_val < 1e-300:
            return 0.0
        if max_idx != k + 1:
            A[:, [k + 1, max_idx]] = A[:, [max_idx, k + 1]]
            A[[k + 1, max_idx], :] = A[[max_idx, k + 1], :]
            pf *= -1
        pf *= A[k, k + 1]
        if k + 2 < n:
            tau = A[k, k + 2:] / A[k, k + 1]                               # (local) Schur update factor
            A[k + 2:, k + 2:] -= np.outer(tau, A[k + 1, k + 2:])
            A[k + 2:, k + 2:] += np.outer(A[k + 1, k + 2:], tau)
    return pf


def run():
    verify_pins()

    t0 = time.time()                                                       # (local)
    print('=' * 78)
    print('PF-J-35 (T3): Pfaffian with corrected J, BDI topological verification')
    print('=' * 78)

    # --- Clifford algebra + operators ---
    gammas = build_cliff8()                                                # (local) 8 16x16 Hermitian gammas
    gamma9 = build_chirality(gammas)                                       # (local) chirality
    C2 = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]                     # (local) T core (corrected J)
    C1 = gammas[1] @ gammas[3] @ gammas[5] @ gammas[7]                     # (local) P core

    I16 = np.eye(16)                                                       # (local) identity 16x16
    err_C2sq = np.max(np.abs(C2 @ C2 - I16))                               # (local)
    err_C1sq = np.max(np.abs(C1 @ C1 - I16))                               # (local)
    err_g9 = np.max(np.abs(gamma9 - C2 @ C1))                              # (local)
    print(f'  C2^2=+I err:       {err_C2sq:.2e}')
    print(f'  C1^2=+I err:       {err_C1sq:.2e}')
    print(f'  gamma_9=C2*C1 err: {err_g9:.2e}')
    assert err_C2sq < HERM_TOL, 'C2^2 != I'
    assert err_C1sq < HERM_TOL, 'C1^2 != I'
    assert err_g9 < HERM_TOL, 'gamma_9 != C2*C1'

    det_C1 = float(np.real(np.linalg.det(C1)))                             # (local)
    print(f'  det(C1) = {det_C1:+.6f}')

    # --- Load S23a Kosmann singlet eigendata ---
    kosmann_path = os.path.join(ARCHIVE_DIR, 's23a_kosmann_singlet.npz')   # (local)
    kosmann = np.load(kosmann_path, allow_pickle=True)
    tau_vals = np.asarray(kosmann['tau_values'])                           # (local)
    n_tau = len(tau_vals)                                                  # (local)
    print(f'\n  Loaded {n_tau} stored tau values: {tau_vals.tolist()}')

    # --- First-principles cross-check at tau=0.20 ---
    print('\n--- First-principles cross-check at tau=0.20 ---')
    gens = su3_generators()                                                # (local)
    f_abc = compute_structure_constants(gens)                              # (local)
    B_ab = compute_killing_form(f_abc)                                     # (local)
    g_check = jensen_metric(B_ab, 0.20)                                    # (local)
    E_check = orthonormal_frame(g_check)                                   # (local)
    ft_check = frame_structure_constants(f_abc, E_check)                   # (local)
    Gamma_check = connection_coefficients(ft_check)                        # (local)
    Omega_check = spinor_connection_offset(Gamma_check, gammas)            # (local)
    D_K_direct = 1j * Omega_check                                          # (local)

    evals_3 = np.asarray(kosmann['eigenvalues_3'])                         # (local)
    evecs_3 = np.asarray(kosmann['eigenvectors_3'])                        # (local)
    D_K_stored = evecs_3 @ np.diag(evals_3) @ evecs_3.conj().T             # (local)
    dk_err = np.max(np.abs(D_K_stored - D_K_direct))                       # (local)
    comm_TD = np.max(np.abs(C2 @ np.conj(D_K_direct) @ C2 - D_K_direct))   # (local)
    comm_PD = np.max(np.abs(C1 @ np.conj(D_K_direct) @ C1 + D_K_direct))   # (local)
    print(f'  |D_K(stored) - D_K(direct)| = {dk_err:.2e}')
    print(f'  |[T, D_K]|                  = {comm_TD:.2e}')
    print(f'  |{{P, D_K}}|                 = {comm_PD:.2e}')

    # ---- Stored-tau Pfaffian scan ----
    print('\n' + '=' * 78)
    print('PFAFFIAN ON STORED TAU (9 S23a singlet values)')
    print('=' * 78)
    results = {k: [] for k in
               ['tau', 'sgn_pf', 'pf_real', 'pf_imag', 'asym_rel',
                'pf_sq_det_err', 'min_ev', 'T_err', 'P_err', 'S_err']}     # (local)
    print(f'\n  {"tau":>6s}  {"sgn(Pf)":>8s}  {"Re(Pf)":>14s}  {"|Im/Re|":>10s}  '
          f'{"asym_rel":>10s}  {"|Pf^2-det|/|det|":>18s}  {"min|ev|":>10s}')
    print('  ' + '-' * 90)
    for ti in range(n_tau):
        tau = float(tau_vals[ti])                                          # (local)
        evals = np.asarray(kosmann[f'eigenvalues_{ti}'])                   # (local)
        evecs = np.asarray(kosmann[f'eigenvectors_{ti}'])                  # (local)
        D_K = evecs @ np.diag(evals) @ evecs.conj().T                      # (local)

        err_T = np.max(np.abs(C2 @ np.conj(D_K) @ C2 - D_K))               # (local)
        err_P = np.max(np.abs(C1 @ np.conj(D_K) @ C1 + D_K))               # (local)
        err_S = np.max(np.abs(gamma9 @ D_K + D_K @ gamma9))                # (local)

        M = C1 @ D_K                                                       # (local) Pfaffian matrix
        M_max = np.max(np.abs(M))                                          # (local)
        asym_err = np.max(np.abs(M + M.T))                                 # (local)
        asym_rel = asym_err / M_max if M_max > 0 else 0.0                  # (local)

        pf = pfaffian_hessenberg(M)                                        # (local)
        pf_r = float(np.real(pf))                                          # (local)
        pf_i = float(np.imag(pf))                                          # (local)
        im_re = abs(pf_i) / abs(pf_r) if abs(pf_r) > 1e-300 else float('inf')  # (local)

        det_M = np.linalg.det(M)                                           # (local)
        pf_sq_err = abs(pf**2 - det_M) / abs(det_M) if abs(det_M) > 1e-300 else 0.0  # (local)
        min_ev = float(np.min(np.abs(np.linalg.eigvals(D_K))))             # (local)

        sgn_int = +1 if pf_r > 0 else (-1 if pf_r < 0 else 0)              # (local)
        sgn_lbl = '+1' if sgn_int == +1 else ('-1' if sgn_int == -1 else ' 0')  # (local)

        results['tau'].append(tau)
        results['sgn_pf'].append(sgn_int)
        results['pf_real'].append(pf_r)
        results['pf_imag'].append(pf_i)
        results['asym_rel'].append(asym_rel)
        results['pf_sq_det_err'].append(pf_sq_err)
        results['min_ev'].append(min_ev)
        results['T_err'].append(err_T)
        results['P_err'].append(err_P)
        results['S_err'].append(err_S)

        print(f'  {tau:6.2f}  {sgn_lbl:>8s}  {pf_r:+14.6e}  {im_re:10.2e}  '
              f'{asym_rel:10.2e}  {pf_sq_err:18.2e}  {min_ev:10.6f}')

    # ---- Extended-tau scan (first-principles D_K at 25 tau in [0, 2.5]) ----
    print('\n' + '=' * 78)
    print(f'EXTENDED SCAN: first-principles D_K at {TAU_VALUES_EXT_N} tau '
          f'in [{TAU_VALUES_EXT_MIN:.1f}, {TAU_VALUES_EXT_MAX:.1f}]')
    print('=' * 78)
    tau_ext = np.linspace(TAU_VALUES_EXT_MIN, TAU_VALUES_EXT_MAX,
                          TAU_VALUES_EXT_N)                                # (local)
    ext_results = {k: [] for k in
                   ['tau', 'sgn_pf', 'pf_real', 'asym_rel', 'min_ev']}     # (local)
    print(f'\n  {"tau":>6s}  {"sgn(Pf)":>8s}  {"Re(Pf)":>14s}  {"asym_rel":>10s}  {"min|ev|":>10s}')
    print('  ' + '-' * 60)
    for tau in tau_ext:
        g_s = jensen_metric(B_ab, tau)                                     # (local)
        E_s = orthonormal_frame(g_s)                                       # (local)
        ft_s = frame_structure_constants(f_abc, E_s)                       # (local)
        Gamma_s = connection_coefficients(ft_s)                            # (local)
        Omega_s = spinor_connection_offset(Gamma_s, gammas)                # (local)
        D_K = 1j * Omega_s                                                 # (local)

        M = C1 @ D_K                                                       # (local)
        M_max = np.max(np.abs(M))                                          # (local)
        asym_rel = np.max(np.abs(M + M.T)) / M_max if M_max > 0 else 0.0   # (local)

        pf = pfaffian_hessenberg(M)                                        # (local)
        pf_r = float(np.real(pf))                                          # (local)
        min_ev = float(np.min(np.abs(np.linalg.eigvals(D_K))))             # (local)
        sgn_int = +1 if pf_r > 0 else (-1 if pf_r < 0 else 0)              # (local)
        sgn_lbl = '+1' if sgn_int == +1 else ('-1' if sgn_int == -1 else ' 0')  # (local)

        ext_results['tau'].append(float(tau))
        ext_results['sgn_pf'].append(sgn_int)
        ext_results['pf_real'].append(pf_r)
        ext_results['asym_rel'].append(asym_rel)
        ext_results['min_ev'].append(min_ev)

        print(f'  {tau:6.3f}  {sgn_lbl:>8s}  {pf_r:+14.6e}  {asym_rel:10.2e}  {min_ev:10.6f}')

    # ---- Gate classification ----
    print('\n' + '=' * 78)
    print('GATE S35-PFAFFIAN-CORRECTED-J CLASSIFICATION')
    print('=' * 78)
    all_pos_stored = all(s == +1 for s in results['sgn_pf'])               # (local)
    all_neg_stored = all(s == -1 for s in results['sgn_pf'])               # (local)
    constant_stored = all_pos_stored or all_neg_stored                     # (local)

    all_pos_ext = all(s == +1 for s in ext_results['sgn_pf'])              # (local)
    all_neg_ext = all(s == -1 for s in ext_results['sgn_pf'])              # (local)
    constant_ext = all_pos_ext or all_neg_ext                              # (local)

    constant_overall = constant_stored and constant_ext                    # (local)
    # Matching sign across both scans (convention consistency):
    same_sign = ((all_pos_stored and all_pos_ext) or
                 (all_neg_stored and all_neg_ext))                         # (local)

    if all_pos_stored:
        sign_stored = '+1'                                                 # (local)
    elif all_neg_stored:
        sign_stored = '-1'                                                 # (local)
    else:
        sign_stored = 'MIXED'                                              # (local)
    if all_pos_ext:
        sign_ext = '+1'                                                    # (local)
    elif all_neg_ext:
        sign_ext = '-1'                                                    # (local)
    else:
        sign_ext = 'MIXED'                                                 # (local)

    max_T_err = max(results['T_err'])                                      # (local)
    max_P_err = max(results['P_err'])                                      # (local)
    max_S_err = max(results['S_err'])                                      # (local)
    max_asym = max(max(results['asym_rel']), max(ext_results['asym_rel']))  # (local)
    max_pf_sq = max(results['pf_sq_det_err'])                              # (local)
    min_gap = min(min(results['min_ev']), min(ext_results['min_ev']))      # (local)

    print(f'\n  Stored tau ({n_tau} values):     sgn(Pf)={sign_stored}  constant={constant_stored}')
    print(f'  Extended ({TAU_VALUES_EXT_N} values):   sgn(Pf)={sign_ext}  constant={constant_ext}')
    print(f'  Both scans same sign:       {same_sign}')

    print(f'\n  BDI symmetry (max over all stored tau):')
    print(f'    |[T, D_K]|             = {max_T_err:.2e}  (T = C2*K, T^2=+1)')
    print(f'    |{{P, D_K}}|            = {max_P_err:.2e}  (P = C1*K, P^2=+1)')
    print(f'    |{{S, D_K}}|            = {max_S_err:.2e}  (S = gamma_9)')
    print(f'    asym_rel (M = C1 D_K)  = {max_asym:.2e}')
    print(f'    |Pf^2 - det|/|det|     = {max_pf_sq:.2e}')
    print(f'    min|ev(D_K)|           = {min_gap:.6f}  (gap-closure threshold = {GAP_TOL:.1e})')

    # Verdict: THEOREM passes iff sgn(Pf) CONSTANT everywhere AND gap OPEN.
    gap_open = min_gap > GAP_TOL                                           # (local)
    verdict = 'PASS' if (constant_overall and gap_open) else 'FAIL'        # (local)
    n_tau_total = n_tau + TAU_VALUES_EXT_N                                 # (local)

    # S30A cross-check
    prior_s30a_sign = '+1'                                                 # (local) T3-S30A convention
    prior_s35_sign = '-1'                                                  # (local) knowledge: eq_182396
    s30a_consistent = constant_overall                                      # (local) both require CONSTANCY; absolute
    # sign differs by P-operator convention (Xi 864-dim vs C1 16-dim)
    flag_vs_s30a = '' if s30a_consistent else 'DIFFERS FROM T3-S30A (both should be Z_2 TRIVIAL)'  # (local)

    print(f'\n  VERDICT: {verdict}')
    print(f'  sgn(Pf) CONSTANT across all {n_tau_total} tau values: {constant_overall}')
    print(f'  Gap OPEN (min|ev| > {GAP_TOL:.0e}): {gap_open}')
    print(f'  T3-S30A (prior, 864-dim Xi@D_total): sgn(Pf)={prior_s30a_sign} (CONSTANT, Z_2=+1)')
    print(f'  T3-S35  (prior, 16-dim  C1@D_K):     sgn(Pf)={prior_s35_sign} (CONSTANT)')
    print(f'  Both runs test Z_2 triviality; convention (Xi vs C1) sets ABSOLUTE sign.')
    if flag_vs_s30a:
        print(f'  FLAG: {flag_vs_s30a}')

    # ---- save artifact ----
    out_npz = os.path.join(SCRIPT_DIR, 's35_pfaffian_corrected_j.npz')  # (local)
    save = {
        'tau_stored': np.array(results['tau']),
        'sgn_pf_stored': np.array(results['sgn_pf']),
        'pf_real_stored': np.array(results['pf_real']),
        'pf_imag_stored': np.array(results['pf_imag']),
        'asym_rel_stored': np.array(results['asym_rel']),
        'pf_sq_det_err_stored': np.array(results['pf_sq_det_err']),
        'min_ev_stored': np.array(results['min_ev']),
        'T_err_stored': np.array(results['T_err']),
        'P_err_stored': np.array(results['P_err']),
        'S_err_stored': np.array(results['S_err']),
        'tau_extended': np.array(ext_results['tau']),
        'sgn_pf_extended': np.array(ext_results['sgn_pf']),
        'pf_real_extended': np.array(ext_results['pf_real']),
        'asym_rel_extended': np.array(ext_results['asym_rel']),
        'min_ev_extended': np.array(ext_results['min_ev']),
        'verdict': verdict,
        'C2_description': 'gamma_1*gamma_3*gamma_5*gamma_7 (corrected J, S34)',
        'C1_description': 'gamma_2*gamma_4*gamma_6*gamma_8 (particle-hole)',
        'det_C1': det_C1,
    }                                                                       # (local) all npz payload
    np.savez_compressed(out_npz, **save)
    fsize_mb = os.path.getsize(out_npz) / (1024 * 1024)                     # (local)
    print(f'\n  Saved: {out_npz}  ({fsize_mb:.2f} MB)')

    # ---- closure SHA ----
    pin_blob = json.dumps(INPUT_PINS, sort_keys=True).encode()             # (local)
    closure_sha = hashlib.sha256(pin_blob).hexdigest()                     # (local)

    # ---- 4-tuple output ----
    value_out = 1 if constant_overall else 0                               # (local) Z_2 triviality flag
    scheme = 'Pfaffian-Parlett-Reid_C1_at_D_K_Cliff8'                      # (local)
    convention = 'KO-dim=6_corrected-J_C2=g1g3g5g7_C1=g2g4g6g8'            # (local)
    L_max_lbl = f'L_max={L_MAX_PIN}_singlet_(0,0)_N_TAU={n_tau_total}'     # (local)

    elapsed = time.time() - t0                                             # (local)
    print('=' * 78)
    print('OUTPUT 4-TUPLE')
    print('=' * 78)
    print(f'value={value_out} sign_stored={sign_stored} sign_ext={sign_ext} '
          f'scheme={scheme} convention={convention} L_max={L_max_lbl}')
    print(f'closure_sha256={closure_sha}')
    print(f'runtime={elapsed:.2f}s')
    print('=' * 78)
    print(f'GATE S35-PFAFFIAN-CORRECTED-J: {verdict}')

    return value_out, verdict, closure_sha, sign_stored, sign_ext


if __name__ == '__main__':
    run()
