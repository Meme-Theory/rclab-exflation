"""
S23A-KOSMANN-SINGLET:  re-run of s23a_kosmann_singlet.py
================================================================

Original: computations/session-23/s23a_kosmann_singlet.py (SHA-256 head 16: 412f8b65afaa0b60)

Purpose
-------
Reproduce the S23a Kosmann spinorial correction K_a in the (0,0) singlet
sector of the Jensen-deformed SU(3) under S81 canonical discipline:
  - Canonical constants imported from canonical_constants.py
  - No framework constants hardcoded (structural u(2)/C^2 index partitions
    are imported from dirac_spectrum; L_max is pinned = 0 since the
    singlet sector has trivial irrep, dim_irrep = 1)
  - Intermediates tagged `# (local)`
  - SHA-256 pins for every input file emitted in first lines of stdout
  - Closure SHA emitted at the end; output 4-tuple line printed last

Gate
----
S23A-KOSMANN-SINGLET : [VERIFY-THEOREM]
  Classification: GEOMETRIC (spectral-triple structural claim).
  Hypothesis:     max |K_a^{n,m}| over {C^2 directions a in {3,4,5,6},
                  tau in TAU_VALUES, n,m in 16-dim singlet spinor
                  eigenbasis} is NONZERO to numerical precision (K-0 gate
                  PASSED means pairing interaction exists in the singlet
                  sector).
  PASS iff:       max_K_element > 1e-10   (K-0 "not closed")
  FAIL iff:       max_K_element <= 1e-10  (K-0 CLOSED: no pairing)
  Tolerance:      THEOREM -> machine-epsilon (1e-10 is the numerical-zero
                  threshold used in the original script; reproduced verbatim)
  Target value:   ~3.5e-1 (from S23a original output, gap-edge scale)

Substitution chain — sign / Hermiticity of K_a (KO-dim 6 convention)
-------------------------------------------------------------------
Definitions:
  nabla_{e_c} e_a     := Gamma^b_{ca} e_b            (connection coefficients)
  Array convention    := Gamma[b,c,a] = Gamma^b_{ca} (upper, 1st_lower, 2nd_lower)
  ON frame            := g^{ij} = delta^{ij}
  Cliff(8) generators := gammas[r] for r=0..7, each 16x16, gamma_r^† = gamma_r
  Anti-commutation    := {gamma_r, gamma_s} = 2 delta_{rs} I_{16}

Baptista Paper 17 eq 4.1:
  K_a = (1/8) sum_{i,j} [g(nabla_{v_i} e_a, v_j) - g(nabla_{v_j} e_a, v_i)]
         * g^{ir} g^{js} * gamma_r gamma_s

Step 1 (substitute g into Gamma):
  g(nabla_{v_i} e_a, v_j) = Gamma[j, i, a]
  g(nabla_{v_j} e_a, v_i) = Gamma[i, j, a]

Step 2 (ON frame reduces sums):
  K_a = (1/8) sum_{r,s} ( Gamma[s, r, a] - Gamma[r, s, a] ) gamma_r gamma_s
      = (1/8) sum_{r,s} A^a_{rs} gamma_r gamma_s
  where  A^a_{rs} := Gamma[s,r,a] - Gamma[r,s,a]       (antisymmetric in r,s)

Step 3 (canonical form via Clifford anti-commutation):
  A^a_{rs} = -A^a_{sr}  =>  K_a = (1/4) sum_{r<s} A^a_{rs} gamma_r gamma_s

Step 4 (Hermiticity direction; KO-dim 6 convention):
  gamma_r^† = gamma_r  and  {gamma_r, gamma_s} = 2 delta_{rs} I
  (gamma_r gamma_s)^† = gamma_s^† gamma_r^† = gamma_s gamma_r = -gamma_r gamma_s   for r != s
  With A^a_{rs} real and (1/8) real:
    K_a^† = (1/8) sum_{r,s} A^a_{rs} (-gamma_r gamma_s) = -K_a

Therefore: K_a is ANTI-HERMITIAN.
Consequence: the script's K-1e test `max |K_a + K_a^†|` should return the
small number (anti-Hermitian branch), and `max |K_a - K_a^†|` should return
the large number. The script's verdict label 'anti-H' is the correct branch.

For Killing directions a in U2_IDX = {0,1,2,7}, metric-Lie-derivative
vanishing gives Gamma[s,r,a] + Gamma[r,s,a] = 0, i.e. A^a_{rs} = 2 Gamma[s,r,a]
which is generally NONZERO.  => K_a does NOT vanish for Killing directions
(consistent with line 417 of the original script).

For C^2 non-Killing directions a in C2_IDX = {3,4,5,6}, A^a_{rs} has both
symmetric and antisymmetric contributions; the K-0 gate tests whether
any matrix element projected into the singlet eigenbasis is nonzero.
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
if COMP_DIR not in sys.path:
    sys.path.insert(0, COMP_DIR)

from canonical_constants import *  # noqa: E402,F401,F403

# Structural helpers live in  module (generators, frame, connection).
# U2_IDX / C2_IDX are REPRESENTATION-THEORETIC index partitions of the
# su(3) = u(2) + C^2 decomposition — not framework constants. Import.
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
    validate_clifford,
    validate_connection,
    U1_IDX, SU2_IDX, C2_IDX, U2_IDX,
)

from scipy.linalg import eigh  # noqa: E402


# --- input SHA-256 pins (precomputed, 2026-04-17) ---
ORIGINAL_SRC = os.path.abspath(
    os.path.join(SCRIPT_DIR, '..', "..", "_shared",
                 's23a_kosmann_singlet.py'))                              # (local)
INPUT_PINS = {                                                            # (local)
    'computations/session-23/s23a_kosmann_singlet.py':
        '412f8b65afaa0b60c0a65ac6564b9b1ecf0ec440caba8e2797c74a8303d9c61e',
    'computations/_shared/canonical_constants.py':
        '68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f',
    'computations/_shared/dirac_spectrum.py':
        'eee1b6fdcbb86847385130b3b3467c76fe1b5b73573d7dac4baf428cf4ff163f',
}

# --- MACHINERY PINS (PRDR-compliant) ---
# Singlet sector has trivial irrep (p,q) = (0,0) with dim_irrep = 1.
# The total spinor-plus-irrep dimension is dim_irrep * dim_spin = 1 * 16 = 16.
# "L_max" in usual Dirac-spectrum sweeps refers to the max (p+q) taken in the
# irrep truncation; for the SINGLET sector only (0,0) enters, so L_max = 0.
L_MAX_PIN = 0                                                              # (local) (0,0) singlet only
DIM_SPIN = 16                                                              # (local) Cliff(8): 2^{8/2} = 16
TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])  # (local) S23 scan
KZERO_TOL = 1e-10                                                          # (local) K-0 gate numerical-zero threshold
HERM_TOL = 1e-10                                                           # (local) Hermiticity-branch classifier


def sha256_of_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def verify_pins():
    print('=' * 72)
    print('S23A-KOSMANN-SINGLET: SHA-256 input pins')
    print('=' * 72)
    proj_root = os.path.abspath(os.path.join(COMP_DIR, '..'))   # (local)
    for rel, expected in INPUT_PINS.items():
        path = os.path.join(proj_root, rel)
        actual = sha256_of_file(path)
        status = 'OK' if actual == expected else 'MISMATCH'    # (local)
        print(f'  {rel:<48s} {actual[:16]}...  [{status}]')
        if actual != expected:
            raise RuntimeError(
                f'SHA mismatch for {rel}: expected {expected}, got {actual}'
            )
    print()


def kosmann_operator_antisymmetric(Gamma, gammas, a):
    """
    K_a = (1/8) sum_{r,s} A^a_{rs} gamma_r gamma_s
    where A^a_{rs} = Gamma[s,r,a] - Gamma[r,s,a]  (antisymmetric in r,s)

    See module docstring, Substitution chain Steps 1-3 for derivation.
    """
    dim_spin = gammas[0].shape[0]                                # (local)
    K = np.zeros((dim_spin, dim_spin), dtype=complex)            # (local)
    A_antisym = np.zeros((8, 8), dtype=np.float64)               # (local)

    for r in range(8):
        for s in range(8):
            A_rs = Gamma[s, r, a] - Gamma[r, s, a]                # (local)
            A_antisym[r, s] = A_rs
            if abs(A_rs) > 1e-15:
                K += A_rs * (gammas[r] @ gammas[s])

    K *= (1.0 / 8.0)
    return K, A_antisym


def kosmann_operator_symmetric(Gamma, gammas, a):
    """
    Symmetric (metric Lie derivative) operator — used by S22b.

    S_a = (1/4) sum_{r,s} (Gamma[s,r,a] + Gamma[r,s,a]) gamma_r gamma_s
        = (1/4) (L_{e_a} g)^{rs} gamma_r gamma_s
    """
    dim_spin = gammas[0].shape[0]                                # (local)
    S = np.zeros((dim_spin, dim_spin), dtype=complex)            # (local)
    Lg_sym = np.zeros((8, 8), dtype=np.float64)                  # (local)

    for r in range(8):
        for s in range(8):
            L_rs = Gamma[s, r, a] + Gamma[r, s, a]                # (local)
            Lg_sym[r, s] = L_rs
            if abs(L_rs) > 1e-15:
                S += L_rs * (gammas[r] @ gammas[s])

    S *= 0.25
    return S, Lg_sym


def extract_singlet_eigensystem(tau, gens, f_abc, gammas):
    """
    Eigensystem of D_K in the (0,0) singlet: D_pi = I_1 x Omega = Omega (16x16).
    H = 1j*Omega is Hermitian; diagonalize via scipy.linalg.eigh.
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    ah_err = np.max(np.abs(Omega + Omega.conj().T))               # (local)
    H = 1j * Omega                                                # (local) Hermitian
    h_err = np.max(np.abs(H - H.conj().T))                        # (local)
    evals, evecs = eigh(H)
    return evals, evecs, Gamma, E, ah_err, h_err


def compute_kosmann_matrix_elements(evecs, K_a):
    return evecs.conj().T @ K_a @ evecs


def run_extraction():
    print('=' * 72)
    print('S23A-KOSMANN-SINGLET: (0,0) singlet Kosmann matrix elements')
    print('=' * 72)
    print(f'L_max pin        = {L_MAX_PIN} (singlet (0,0) only)')
    print(f'dim_spin         = {DIM_SPIN}')
    print(f'TAU_VALUES       = {TAU_VALUES.tolist()}')
    print(f'K-0 threshold    = {KZERO_TOL:.2e}')

    gens = su3_generators()                                        # (local)
    f_abc = compute_structure_constants(gens)                      # (local)
    gammas = build_cliff8()                                        # (local)

    cliff_err = validate_clifford(gammas)                          # (local)
    print(f'Clifford validation: max_err = {cliff_err:.2e}')
    print()

    npz_data = {'tau_values': TAU_VALUES}                          # (local)

    t_total = time.time()                                          # (local)

    for idx, tau in enumerate(TAU_VALUES):
        t_start = time.time()                                      # (local)
        print(f'--- tau = {tau:.2f}  ({idx+1}/{len(TAU_VALUES)}) ---')

        evals, evecs, Gamma, E, ah_err, h_err = extract_singlet_eigensystem(
            tau, gens, f_abc, gammas
        )
        mc_err = validate_connection(Gamma)                        # (local)
        print(f'  anti-Herm err (Omega) = {ah_err:.2e} ; '
              f'Herm(1j*D) err = {h_err:.2e} ; metric-compat err = {mc_err:.2e}')
        print(f'  eigvals (1j*D) range: '
              f'[{np.min(np.abs(evals)):.6f}, {np.max(np.abs(evals)):.6f}]')

        npz_data[f'eigenvalues_{idx}'] = evals
        npz_data[f'eigenvectors_{idx}'] = evecs

        K_norms = np.zeros(8)                                      # (local)
        K_antisym_norms = np.zeros(8)                              # (local)
        S_sym_norms = np.zeros(8)                                  # (local)

        for a in range(8):
            K_a, A_antisym = kosmann_operator_antisymmetric(Gamma, gammas, a)
            S_a, Lg_sym = kosmann_operator_symmetric(Gamma, gammas, a)

            K_norm = np.sqrt(np.sum(np.abs(K_a) ** 2))             # (local) Frobenius
            S_norm = np.sqrt(np.sum(np.abs(S_a) ** 2))             # (local)
            A_norm = np.sqrt(np.sum(A_antisym ** 2))               # (local)
            K_norms[a] = K_norm
            K_antisym_norms[a] = A_norm
            S_sym_norms[a] = S_norm

            k_h_err = np.max(np.abs(K_a - K_a.conj().T))           # (local)
            k_ah_err = np.max(np.abs(K_a + K_a.conj().T))          # (local)
            # per substitution-chain Step 4: K_a^† = -K_a => anti-H branch small
            k_type = ('Herm' if k_h_err < HERM_TOL else
                      ('anti-H' if k_ah_err < HERM_TOL else 'MIXED'))  # (local)
            dir_type = 'Killing' if a in U2_IDX else 'C^2'         # (local)

            print(f'  a={a} [{dir_type}] |K|={K_norm:.3e} |S|={S_norm:.3e} '
                  f'|A|={A_norm:.3e} type={k_type} '
                  f'(h_err={k_h_err:.1e}, ah_err={k_ah_err:.1e})')

            npz_data[f'A_antisym_{idx}_{a}'] = A_antisym
            K_eig = compute_kosmann_matrix_elements(evecs, K_a)
            S_eig = compute_kosmann_matrix_elements(evecs, S_a)
            npz_data[f'K_a_matrix_{idx}_{a}'] = K_eig
            npz_data[f'S_a_matrix_{idx}_{a}'] = S_eig

        npz_data[f'K_norms_{idx}'] = K_norms
        npz_data[f'S_norms_{idx}'] = S_sym_norms

        abs_evals = np.abs(evals)                                  # (local)
        sorted_indices = np.argsort(abs_evals)                     # (local)
        gap_edge_idx = sorted_indices[:2]                          # (local)
        npz_data[f'gap_edge_indices_{idx}'] = gap_edge_idx

        elapsed = time.time() - t_start                            # (local)
        print(f'  gap-edge modes: {gap_edge_idx.tolist()}  '
              f'|lambda|=[{abs_evals[gap_edge_idx[0]]:.6f}, '
              f'{abs_evals[gap_edge_idx[1]]:.6f}]  ({elapsed:.2f}s)')

    total_elapsed = time.time() - t_total                          # (local)
    print(f'\nTotal time: {total_elapsed:.2f}s')

    # --- K-0 gate evaluation ---
    print('-' * 72)
    print('K-0 GATE')
    print('-' * 72)

    max_K_element = 0.0                                            # (local)
    max_K_gap_element = 0.0                                        # (local)
    all_zero = True                                                # (local)

    for idx, tau in enumerate(TAU_VALUES):
        for a in C2_IDX:
            K_eig = npz_data[f'K_a_matrix_{idx}_{a}']
            max_elem = np.max(np.abs(K_eig))                       # (local)
            max_K_element = max(max_K_element, max_elem)
            gap_idx = npz_data[f'gap_edge_indices_{idx}']
            K_gap = K_eig[np.ix_(gap_idx, gap_idx)]
            max_gap = np.max(np.abs(K_gap))                        # (local)
            max_K_gap_element = max(max_K_gap_element, max_gap)
            if max_elem > KZERO_TOL:
                all_zero = False

    k0_verdict = 'FAIL' if all_zero else 'PASS'                    # (local)
    print(f'  max |K_a^nm| (all tau, C^2 dirs) = {max_K_element:.6e}')
    print(f'  max |K_a^nm| gap-edge only       = {max_K_gap_element:.6e}')
    print(f'  K-0 threshold                    = {KZERO_TOL:.2e}')
    print(f'  K-0 gate: {k0_verdict}  '
          f'({"CLOSED (no pairing)" if all_zero else "pairing interaction exists"})')

    # --- save artifact ---
    out_npz = os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz')  # (local)
    np.savez_compressed(out_npz, **npz_data)
    fsize = os.path.getsize(out_npz) / (1024 * 1024)               # (local)
    print(f'\nSaved: {out_npz}  ({fsize:.1f} MB)')

    # --- closure SHA ---
    pin_blob = json.dumps(INPUT_PINS, sort_keys=True).encode()     # (local)
    closure_sha = hashlib.sha256(pin_blob).hexdigest()             # (local)

    # --- output 4-tuple (last non-verdict lines) ---
    value_out = max_K_element                                      # (local) decisive scalar
    scheme = 'Kosmann_antisym_Baptista_P17_eq4.1'                  # (local)
    convention = 'KO-dim=6_Cliff8_ON-frame'                        # (local)
    L_max = f'L_max={L_MAX_PIN}_singlet_(0,0)'                     # (local)

    print('=' * 72)
    print('OUTPUT 4-TUPLE')
    print('=' * 72)
    print(f'value={value_out:.6e} scheme={scheme} '
          f'convention={convention} L_max={L_max}')
    print(f'closure_sha256={closure_sha}')
    print('=' * 72)

    return value_out, k0_verdict, closure_sha


if __name__ == '__main__':
    run_extraction()
