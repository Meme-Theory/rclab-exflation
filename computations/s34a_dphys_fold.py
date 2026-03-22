"""
Session 34a: D_phys = D_K + phi + J*phi*J^{-1} Construction and Fold Survival
=============================================================================
EXISTENTIAL GATE: Does the B2 eigenvalue fold at tau~0.190 survive inner fluctuations?

The inner fluctuation phi = sum_i a_i[D_K, b_i] with a_i, b_i in A_F = C + H + M_3(C)
introduces off-diagonal terms mixing U(2) branches (B1, B2, B3).

Method:
  1. Load bare D_K eigenvectors from s23a_kosmann_singlet.npz
  2. Construct A_F = C + H + M_3(C) action on H_F = C^{16}
  3. Compute phi = sum_i a_i[D_K, b_i] for independent generators b_i
  4. Identify WORST CASE phi direction (maximally perturbs B2 branch)
  5. Construct D_phys = D_K + phi + J*phi*J^{-1}
  6. Diagonalize across tau sweep; locate B2-analog minimum

Gate DPHYS-34a-1 (pre-registered):
  PASS:        B2 fold persists (d2 > 0 at some tau in [0.14, 0.24]) at |phi| = gap_{B2-B3} = 0.07
  STRONG PASS: Fold persists up to |phi| = 2*gap = 0.14
  FAIL:        Fold destroyed (d2 <= 0) at |phi| = gap_{B2-B3}

Author: bap (baptista-spacetime-analyst), Session 34a
Date: 2026-03-06
"""

import os
import time
import numpy as np
from numpy.linalg import eigh, inv
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

# ======================================================================
#  Constants
# ======================================================================

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])

# Branch indices in A_antisym 8x8 basis (positive eigenvalue sector)
B3_IDX = np.array([0, 1, 2])
B2_IDX = np.array([3, 4, 5, 6])
B1_IDX = np.array([7])

# Gap at tau=0.20: B2-B3 ~ 0.133, B2-B1 ~ 0.026
GAP_B2_B3 = 0.133   # Will be recomputed per tau

# ======================================================================
#  Part 0: J operator (charge conjugation on Cliff(R^8))
# ======================================================================

def build_J_operator(gammas):
    """Build J = C2 * complex_conjugation on C^{16}.

    For KO-dimension 0 (internal 8-manifold SU(3)):
      epsilon = +1: J D J^{-1} = +D  (J commutes with D)
      J^2 = +1

    The correct charge conjugation matrix is C2 = gamma_1 * gamma_3 * gamma_5 * gamma_7
    (product of the four REAL/SYMMETRIC gamma matrices in our tensor-product basis).
    This satisfies C2 gamma_a C2^{-1} = -gamma_a^T for all a.

    The alternative C1 = gamma_2 * gamma_4 * gamma_6 * gamma_8 (product of imaginary gammas)
    gives C1 gamma_a C1^{-1} = +gamma_a^T but J_C1 D J_C1^{-1} = -D (wrong sign).

    DERIVATION: D_K = i * Omega where Omega = (1/4) sum Gamma^b_{ac} gamma_a gamma_b gamma_c.
    Gamma^b_{ac} are real. D_K^* = -i * Omega^* where Omega^* involves gamma_a^*.
    For J(v) = C conj(v): J D J^{-1} = C D^* C^{-1}.
    D^* = (i*Omega)^* = -i * (product of gamma^*).
    Using C2 gamma_a^* C2^{-1}: since gamma_{odd} are real and gamma_{even} are pure-imaginary,
    gamma_a^* = gamma_a for odd, gamma_a^* = -gamma_a for even.
    C2 gamma_a^* C2^{-1} = C2 (sign_a * gamma_a) C2^{-1} = sign_a * (-gamma_a^T)
    For real gammas (odd): sign=+1, C2 gamma C2^{-1} = -gamma^T
    For imag gammas (even): sign=-1, C2 (-gamma) C2^{-1} = +gamma^T
    The product of 3 gammas picks up the transpose of each with reversed order,
    and the 3 signs from C2 and the 3 conjugation signs combine to give
    C2 (gamma_a gamma_b gamma_c)^* C2^{-1} = gamma_c^T gamma_b^T gamma_a^T
    = (gamma_a gamma_b gamma_c)^T.
    So C2 Omega^* C2^{-1} = Omega^T = -Omega (anti-hermitian).
    Then J D J^{-1} = C2 (-i Omega^*) C2^{-1} = -i * (-Omega) = i*Omega = D. QED.

    Returns:
        C2: (16,16) matrix such that J(v) = C2 @ conj(v), J D J^{-1} = +D
    """
    # C2 = gamma_1 * gamma_3 * gamma_5 * gamma_7 (0-indexed: gammas[0]*gammas[2]*gammas[4]*gammas[6])
    C2 = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]

    # Verify J^2 = +I: C2 * conj(C2) = I (C2 is real, so C2^2 = I)
    err_sq = np.max(np.abs(C2 @ C2 - np.eye(16)))
    assert err_sq < 1e-13, f"C2^2 != +I, err = {err_sq}"

    # Verify C2 gamma_a C2^{-1} = -gamma_a^T for all a
    C2_inv = np.linalg.inv(C2)
    for a in range(8):
        test = C2 @ gammas[a] @ C2_inv
        err = np.max(np.abs(test + gammas[a].T))
        assert err < 1e-13, f"C2 gamma_{a} C2^{{-1}} != -gamma_{a}^T, err = {err}"

    return C2


def apply_J_to_matrix(C2, M):
    """Compute J M J^{-1} for a linear operator M.

    J is antilinear: J(psi) = C2 conj(psi).
    C2 is real (C2* = C2) and C2^2 = I (C2^{-1} = C2).

    For linear M:
        J M J^{-1}(v) = C2 conj(M C2 conj(v)) = C2 M* C2* v = C2 M* C2 v

    Returns:
        J M J^{-1}: (16,16) matrix
    """
    return C2 @ np.conj(M) @ C2


# ======================================================================
#  Part 1: A_F = C + H + M_3(C) generators on C^16
# ======================================================================

def flat_idx(row, col):
    """Convert 4x4 internal matrix position to flat 16-index (Baptista convention)."""
    if row == 0 and col == 0:
        return 0
    elif row == 0:
        return col
    elif col == 0:
        return row + 3
    else:
        return 7 + 3 * (row - 1) + (col - 1)


def build_AF_gen_16(L_4x4, R_4x4):
    """Build 16x16 A_F generator from 4x4 left and right actions.

    pi(a)_{flat(i,j), flat(k,l)} = L_{ik} * R_{lj}
    """
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L_4x4[i, k] * R_4x4[l, j]
    return gen


def build_AF_generators():
    """Build all independent A_F generators as 16x16 matrices.

    A_F = C + H + M_3(C):
      C: 2 real generators (Re(lambda), Im(lambda))
      H: 4 real generators (1, i, j, k) -- but H_1 = identity on doublet sector
         We use 3 traceless generators (i, j, k) for the fluctuation.
      M_3(C): 18 real generators (9 Re + 9 Im of elementary matrices)

    For inner fluctuations phi = a[D,b], only the TRACELESS part matters
    (identity commutes with everything). So we use:
      C: Im(lambda) only (Re is part of identity)
      H: i, j, k (3 generators)
      M_3: 8 traceless generators of su(3) embedded as M_3(C) gens

    Returns:
        list of (name, 16x16 matrix) tuples
    """
    gens = []

    # --- C: Im(lambda) ---
    L = np.zeros((4, 4), dtype=complex)
    L[0, 0] = 1j       # lambda = i on up-RH
    L[1, 1] = -1j      # lambda-bar = -i on down-RH
    L[2, 2] = 1j       # lambda on nu_L
    L[3, 3] = -1j      # lambda-bar on e_L
    R = np.eye(4, dtype=complex)
    gens.append(('C_Im', build_AF_gen_16(L, R)))

    # --- H: i, j, k generators (act on LH doublet rows 2-3) ---
    # H_i: diag(i, -i) on doublet
    L = np.zeros((4, 4), dtype=complex)
    L[0, 0] = 1j       # q0+iq1 -> i
    L[1, 1] = -1j      # q0-iq1 -> -i
    L[2, 2] = 1j       # diag(i,-i) on doublet
    L[3, 3] = -1j
    R = np.eye(4, dtype=complex)
    gens.append(('H_i', build_AF_gen_16(L, R)))

    # H_j: [[0,1],[-1,0]] on doublet, 0 on RH
    L = np.zeros((4, 4), dtype=complex)
    L[2, 3] = 1.0
    L[3, 2] = -1.0
    R = np.eye(4, dtype=complex)
    gens.append(('H_j', build_AF_gen_16(L, R)))

    # H_k: [[0,i],[i,0]] on doublet, 0 on RH
    L = np.zeros((4, 4), dtype=complex)
    L[2, 3] = 1j
    L[3, 2] = 1j
    R = np.eye(4, dtype=complex)
    gens.append(('H_k', build_AF_gen_16(L, R)))

    # --- M_3(C): traceless hermitian generators (Gell-Mann-like on color indices) ---
    # These act on cols 1-3 via right multiplication: R = diag(0, m^T)
    # We use 8 su(3) generators plus scaling for the trace part
    # For off-diagonal real: E_{ab} + E_{ba} (a<b, 3 of them)
    # For off-diagonal imag: i(E_{ab} - E_{ba}) (a<b, 3 of them)
    # For diagonal: lambda_3 and lambda_8 analogs (2 of them)

    def m3_gen(m_3x3):
        """Build 16x16 from a 3x3 matrix acting on color (cols 1-3)."""
        L = np.eye(4, dtype=complex)
        R = np.zeros((4, 4), dtype=complex)
        R[0, 0] = 0  # No action on lepton column
        R[1:4, 1:4] = m_3x3.T  # Right action by m^T on quark colors
        return build_AF_gen_16(L, R)

    # 8 traceless hermitian generators of su(3)_color
    # Using Gell-Mann matrices
    gm = []
    gm.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))  # lambda_1
    gm.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))  # lambda_2
    gm.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))  # lambda_3
    gm.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))  # lambda_4
    gm.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))  # lambda_5
    gm.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))  # lambda_6
    gm.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))  # lambda_7
    gm.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex)/np.sqrt(3))  # lambda_8

    for k, g in enumerate(gm):
        gens.append((f'M3_{k}', m3_gen(g)))

    # Also add the trace part of M_3 (identity on colors)
    # This acts as identity on quarks, 0 on leptons
    m_id = np.eye(3, dtype=complex)
    gens.append(('M3_id', m3_gen(m_id)))

    return gens


# ======================================================================
#  Part 2: Construct phi = sum_i a_i [D_K, b_i] in eigenspinor basis
# ======================================================================

def compute_phi_generators(D_K_diag, evecs, af_gens):
    """Compute [D_K, b_i] for each A_F generator b_i in the D_K eigenspinor basis.

    In the eigenspinor basis:
        [D_K, b_i]_{nm} = (lambda_n - lambda_m) * <psi_n|b_i|psi_m>

    This gives the INDEPENDENT fluctuation directions. The space of inner
    fluctuations is spanned by these matrices.

    Args:
        D_K_diag: (16,) eigenvalues of D_K
        evecs: (16,16) columns are eigenspinors
        af_gens: list of (name, 16x16 matrix) from build_AF_generators

    Returns:
        phi_basis: list of (name, 16x16 matrix in eigenspinor basis) -- the [D_K, b_i]
    """
    phi_basis = []
    for name, gen in af_gens:
        # Transform generator to eigenspinor basis
        gen_eig = evecs.conj().T @ gen @ evecs

        # Apply [D_K, gen]: multiply by (lambda_n - lambda_m)
        n = len(D_K_diag)
        comm = np.zeros((n, n), dtype=complex)
        for i in range(n):
            for j in range(n):
                comm[i, j] = (D_K_diag[i] - D_K_diag[j]) * gen_eig[i, j]

        # Check if this is non-negligible
        norm = np.max(np.abs(comm))
        if norm > 1e-12:
            phi_basis.append((name, comm, norm))

    return phi_basis


def find_worst_case_phi(phi_basis, B2_mode_indices, B3_mode_indices, B1_mode_indices):
    """Find the phi direction that maximally perturbs B2 eigenvalues.

    The worst case is the phi that maximizes the B2-B3 or B2-B1 mixing,
    as this would destroy the fold structure.

    Strategy: for each phi generator, compute the coupling between B2 and
    other branches. The worst case is the one with largest off-diagonal
    norm in the B2 rows/columns connecting to B3 or B1.

    Returns:
        worst_idx: index into phi_basis
        worst_name: name of worst generator
        mixing_strength: maximum |phi_{B2,B3}| or |phi_{B2,B1}| per unit phi amplitude
    """
    worst_mixing = 0
    worst_idx = 0
    worst_name = ''
    mixing_details = []

    for idx, (name, comm, norm) in enumerate(phi_basis):
        # Extract B2-B3 mixing block
        b2_b3_block = comm[np.ix_(B2_mode_indices, B3_mode_indices)]
        b2_b1_block = comm[np.ix_(B2_mode_indices, B1_mode_indices)]

        b2_b3_mix = np.max(np.abs(b2_b3_block)) if b2_b3_block.size > 0 else 0
        b2_b1_mix = np.max(np.abs(b2_b1_block)) if b2_b1_block.size > 0 else 0

        # Also check intra-B2 mixing (lifts degeneracy)
        b2_b2_block = comm[np.ix_(B2_mode_indices, B2_mode_indices)]
        b2_b2_offdiag = np.max(np.abs(b2_b2_block - np.diag(np.diag(b2_b2_block))))

        total_mix = max(b2_b3_mix, b2_b1_mix)
        mixing_details.append((name, b2_b3_mix, b2_b1_mix, b2_b2_offdiag, norm))

        if total_mix > worst_mixing:
            worst_mixing = total_mix
            worst_idx = idx
            worst_name = name

    return worst_idx, worst_name, worst_mixing, mixing_details


# ======================================================================
#  Part 3: D_phys construction and eigenvalue computation
# ======================================================================

def construct_D_phys(D_K_diag, evecs, phi_eig, phi_amplitude, B):
    """Construct D_phys = D_K + phi_VEV + J phi_VEV J^{-1} and diagonalize.

    Works in the ORIGINAL (non-eigenspinor) basis for J consistency.

    Args:
        D_K_diag: (16,) eigenvalues
        evecs: (16,16) eigenspinor columns
        phi_eig: (16,16) phi in eigenspinor basis (one generator direction)
        phi_amplitude: scalar amplitude |phi_VEV|
        B: (16,16) J operator matrix

    Returns:
        evals_phys: (16,) sorted eigenvalues of D_phys
        evecs_phys: (16,16) eigenvectors of D_phys
    """
    # D_K in original basis
    D_K_orig = evecs @ np.diag(D_K_diag) @ evecs.conj().T

    # phi in original basis
    phi_orig = evecs @ (phi_amplitude * phi_eig) @ evecs.conj().T

    # J phi J^{-1} in original basis
    J_phi_J = apply_J_to_matrix(B, phi_orig)

    # D_phys = D_K + phi + J phi J^{-1}
    D_phys = D_K_orig + phi_orig + J_phi_J

    # Hermiticity check (D_K is NOT hermitian -- it's anti-hermitian in math convention)
    # Actually D_K has real eigenvalues from the data, so it IS hermitian in the
    # stored eigenbasis. Let me check.
    herm_err = np.max(np.abs(D_phys - D_phys.conj().T))

    # Diagonalize
    evals, evecs_out = eigh(D_phys)

    return evals, evecs_out, herm_err


def identify_B2_branch(evals_phys, evals_bare, evecs_phys, evecs_bare):
    """Identify which eigenvalues of D_phys correspond to the B2 branch.

    Uses overlap with bare B2 eigenvectors to track the branch through
    the fluctuation.

    The B2 bare modes are indices 9-12 (positive evals sorted ascending:
    B1=8, B2=9,10,11,12, B3=13,14,15). But eigenvalue ordering may differ.

    Uses maximum overlap criterion.

    Returns:
        b2_phys_indices: indices into evals_phys that correspond to B2
        overlaps: overlap matrix
    """
    # Positive eigenvalues of bare D_K (sorted)
    pos_bare = np.where(evals_bare > 0)[0]
    pos_bare_sorted = pos_bare[np.argsort(evals_bare[pos_bare])]
    # B1 = lowest positive = pos_bare_sorted[0]
    # B2 = next 4 = pos_bare_sorted[1:5]
    # B3 = top 3 = pos_bare_sorted[5:8]
    b2_bare_indices = pos_bare_sorted[1:5]

    # Positive eigenvalues of D_phys
    pos_phys = np.where(evals_phys > 0)[0]
    pos_phys_sorted = pos_phys[np.argsort(evals_phys[pos_phys])]

    # Compute overlap matrix: |<psi_phys_i | psi_bare_j>|^2
    # Sum over bare B2 modes to assign each phys mode a B2-ness
    b2_ness = np.zeros(len(pos_phys_sorted))
    for i_ph, idx_ph in enumerate(pos_phys_sorted):
        for idx_b in b2_bare_indices:
            overlap = np.abs(np.dot(evecs_phys[:, idx_ph].conj(), evecs_bare[:, idx_b]))**2
            b2_ness[i_ph] += overlap

    # Select the 4 modes with highest B2-ness
    b2_phys_local = np.argsort(b2_ness)[-4:]
    b2_phys_indices = pos_phys_sorted[b2_phys_local]

    return b2_phys_indices, b2_ness


# ======================================================================
#  Part 4: Main computation
# ======================================================================

def main():
    print("=" * 78)
    print("Session 34a: D_phys = D_K + phi + J*phi*J^{-1}")
    print("Gate DPHYS-34a-1: B2 fold survival under inner fluctuations")
    print("=" * 78)

    # --- Load data ---
    kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                      allow_pickle=True)
    tau_vals = kosmann['tau_values']
    print(f"\nLoaded s23a_kosmann_singlet.npz: {len(tau_vals)} tau values")

    # --- Build Clifford algebra and J operator ---
    from tier1_dirac_spectrum import (su3_generators as _su3g, compute_structure_constants as _csc,
        compute_killing_form as _ckf, jensen_metric as _jm, orthonormal_frame as _of,
        frame_structure_constants as _fsc, connection_coefficients as _cc,
        build_cliff8 as _bc8, spinor_connection_offset as _sco)

    gammas = _bc8()
    B_J = build_J_operator(gammas)
    print(f"J operator: C2 = gamma_1*gamma_3*gamma_5*gamma_7, C2^2 = +I verified")

    # Cross-check: J D_K J^{-1} = +D_K at tau=0.20 (from first principles)
    _gens = _su3g()
    _fabc = _csc(_gens)
    _Bk = _ckf(_fabc)
    _gs = _jm(_Bk, 0.20)
    _E = _of(_gs)
    _ft = _fsc(_fabc, _E)
    _Gam = _cc(_ft)
    _Om = _sco(_Gam, gammas)
    D_K_direct = 1j * _Om
    JDJ_check = apply_J_to_matrix(B_J, D_K_direct)
    jdj_err = np.max(np.abs(JDJ_check - D_K_direct))
    print(f"  Cross-check: |J D_K J^{{-1}} - D_K| = {jdj_err:.2e} at tau=0.20")
    assert jdj_err < 1e-10, f"J D J^{{-1}} != D, err = {jdj_err}"
    print(f"  PASS: J commutes with D_K (epsilon = +1, KO-dim 0)")

    # Cross-check: stored eigenvectors reconstruct i*Omega
    _ev3 = kosmann['eigenvalues_3']
    _ec3 = kosmann['eigenvectors_3']
    D_K_from_stored = _ec3 @ np.diag(_ev3) @ _ec3.conj().T
    dk_match_err = np.max(np.abs(D_K_from_stored - D_K_direct))
    print(f"  |D_K(stored) - i*Omega(direct)| = {dk_match_err:.2e} at tau=0.20")
    if dk_match_err > 1e-10:
        print(f"  WARNING: stored eigenvectors may use different convention!")

    # --- Build A_F generators ---
    af_gens = build_AF_generators()
    print(f"A_F generators: {len(af_gens)} total")
    for name, gen in af_gens:
        print(f"  {name}: max|entry| = {np.max(np.abs(gen)):.4f}")

    # ================================================================
    #  CROSS-CHECK 1: A_F generators commute with each other within factors
    # ================================================================
    print("\n--- Cross-check: A_F generator algebra ---")
    # C and H generators should commute with M_3 generators
    c_gens = [(n,g) for n,g in af_gens if n.startswith('C_')]
    h_gens = [(n,g) for n,g in af_gens if n.startswith('H_')]
    m3_gens = [(n,g) for n,g in af_gens if n.startswith('M3_')]

    max_ch_m3_err = 0
    for cn, cg in c_gens + h_gens:
        for mn, mg in m3_gens:
            comm = cg @ mg - mg @ cg
            err = np.max(np.abs(comm))
            max_ch_m3_err = max(max_ch_m3_err, err)
    print(f"  max |[C+H, M_3]| = {max_ch_m3_err:.2e} (should be ~0)")

    # ================================================================
    #  MAIN LOOP: Compute phi generators and D_phys across tau values
    # ================================================================

    # Use tau indices 1-5 (tau = 0.10, 0.15, 0.20, 0.25, 0.30) for the fold region
    tau_scan_indices = [1, 2, 3, 4, 5]
    phi_amplitudes = np.linspace(0, 0.20, 21)  # 0 to 0.20 in steps of 0.01

    results = {}

    # First pass: identify worst-case phi direction at tau=0.20 (fold center)
    print("\n--- Phase 1: Identify worst-case phi direction at tau=0.20 ---")
    ti_ref = 3  # tau=0.20
    evals_ref = kosmann[f'eigenvalues_{ti_ref}']
    evecs_ref = kosmann[f'eigenvectors_{ti_ref}']

    # Eigenvalue ordering: eigh returns sorted ascending
    sort_idx = np.argsort(evals_ref)
    evals_sorted = evals_ref[sort_idx]
    evecs_sorted = evecs_ref[:, sort_idx]

    print(f"  tau = {tau_vals[ti_ref]:.2f}")
    print(f"  Eigenvalues (sorted): {evals_sorted}")

    # Positive eigenvalue indices (sorted ascending)
    pos_mask = evals_sorted > 0
    pos_indices = np.where(pos_mask)[0]
    pos_evals = evals_sorted[pos_indices]
    print(f"  Positive evals: {pos_evals}")
    print(f"  B1 = {pos_evals[0]:.6f} (idx {pos_indices[0]})")
    print(f"  B2 = {pos_evals[1:5]} (idx {pos_indices[1:5]})")
    print(f"  B3 = {pos_evals[5:8]} (idx {pos_indices[5:8]})")

    gap_b2_b1 = pos_evals[1] - pos_evals[0]
    gap_b3_b2 = pos_evals[5] - pos_evals[4]
    print(f"  Gap B2-B1 = {gap_b2_b1:.6f}")
    print(f"  Gap B3-B2 = {gap_b3_b2:.6f}")

    # Mode indices in the SORTED eigenvalue basis
    B1_modes = pos_indices[0:1]
    B2_modes = pos_indices[1:5]
    B3_modes = pos_indices[5:8]

    # Compute phi generators at reference tau
    phi_basis_ref = compute_phi_generators(evals_sorted, evecs_sorted, af_gens)
    print(f"\n  Non-zero phi generators: {len(phi_basis_ref)}")
    for name, comm, norm in phi_basis_ref:
        print(f"    {name}: max|[D_K,b]| = {norm:.6f}")

    # Find worst-case direction
    worst_idx, worst_name, worst_mixing, mixing_details = find_worst_case_phi(
        phi_basis_ref, B2_modes, B3_modes, B1_modes)

    print(f"\n  Mixing analysis (each generator):")
    print(f"  {'Name':>10s}  B2-B3_mix  B2-B1_mix  B2-B2_off  |phi|_max")
    for name, b23, b21, b22, norm in mixing_details:
        print(f"  {name:>10s}  {b23:.6f}   {b21:.6f}   {b22:.6f}   {norm:.6f}")

    print(f"\n  WORST CASE: {worst_name}, max inter-branch mixing = {worst_mixing:.6f}")

    # ================================================================
    #  CROSS-CHECK 2: phi=0 reproduces D_K exactly
    # ================================================================
    print("\n--- Cross-check 2: D_phys(phi=0) = D_K ---")
    evals_check, _, herm_err = construct_D_phys(
        evals_sorted, evecs_sorted,
        np.zeros((16, 16), dtype=complex), 0.0, B_J)
    check_err = np.max(np.abs(np.sort(evals_check) - evals_sorted))
    print(f"  max|D_phys(0) - D_K| eigenvalues = {check_err:.2e}")
    print(f"  Hermiticity error = {herm_err:.2e}")
    assert check_err < 1e-12, f"CROSS-CHECK FAILED: phi=0 does not reproduce D_K"
    print(f"  PASS")

    # ================================================================
    #  CROSS-CHECK 3: First-order perturbation theory
    # ================================================================
    print("\n--- Cross-check 3: Perturbation theory at small phi ---")
    phi_small = 0.001
    phi_dir = phi_basis_ref[worst_idx][1]

    # First-order prediction: delta_lambda_n = <n|phi+JphiJ|n>
    # In eigenspinor basis, phi is phi_dir * phi_small
    phi_orig = evecs_sorted @ (phi_small * phi_dir) @ evecs_sorted.conj().T
    J_phi_J = apply_J_to_matrix(B_J, phi_orig)
    perturbation = phi_orig + J_phi_J
    pert_eig = evecs_sorted.conj().T @ perturbation @ evecs_sorted
    first_order_shifts = np.real(np.diag(pert_eig))

    # Exact computation
    evals_exact, _, _ = construct_D_phys(
        evals_sorted, evecs_sorted, phi_dir, phi_small, B_J)

    actual_shifts = np.sort(evals_exact) - evals_sorted
    pert_err = np.max(np.abs(actual_shifts - first_order_shifts))
    print(f"  |phi| = {phi_small}")
    print(f"  max|delta_exact - delta_1st_order| = {pert_err:.2e}")
    print(f"  Expected O(phi^2) = {phi_small**2:.2e}")
    pert_ratio = pert_err / phi_small**2 if phi_small > 0 else 0
    print(f"  Ratio (should be O(1)): {pert_ratio:.2f}")
    if pert_err < 10 * phi_small**2:
        print(f"  PASS (perturbation theory consistent)")
    else:
        print(f"  WARNING: perturbation theory deviation larger than expected")

    # ================================================================
    #  Phase 2: Sweep phi amplitude at ALL relevant tau values
    # ================================================================
    print("\n" + "=" * 78)
    print("Phase 2: D_phys eigenvalue sweep across tau and |phi|")
    print("=" * 78)

    # For each tau, use the SAME worst-case direction identified at tau=0.20
    # (but recomputed in the local eigenbasis)
    # Also test with a "composite" worst-case that adapts to each tau

    all_B2_min_tau = {}   # phi_amp -> tau of B2 minimum
    all_B2_d2 = {}        # phi_amp -> curvature at minimum
    all_B2_evals = {}     # (tau_idx, phi_amp) -> B2 eigenvalues

    # Dense tau grid via interpolation for fold location
    tau_dense = np.linspace(0.10, 0.30, 41)

    for phi_amp in phi_amplitudes:
        B2_mean_at_tau = []
        tau_points = []

        for ti in tau_scan_indices:
            tau = tau_vals[ti]
            evals_ti = kosmann[f'eigenvalues_{ti}']
            evecs_ti = kosmann[f'eigenvectors_{ti}']

            # Sort eigenbasis
            si = np.argsort(evals_ti)
            ev_s = evals_ti[si]
            ec_s = evecs_ti[:, si]

            if phi_amp == 0:
                evals_phys = ev_s.copy()
                evecs_phys = ec_s.copy()
            else:
                # Recompute phi generators in this eigenbasis
                phi_basis_ti = compute_phi_generators(ev_s, ec_s, af_gens)

                # Use same generator name as worst_name
                phi_dir_ti = None
                for name, comm, norm in phi_basis_ti:
                    if name == worst_name:
                        phi_dir_ti = comm
                        break

                if phi_dir_ti is None:
                    # Fallback: use the largest mixing generator
                    _, _, _, mix_d = find_worst_case_phi(
                        phi_basis_ti, B2_modes, B3_modes, B1_modes)
                    # Find the generator with largest total mixing
                    best_mix = 0
                    for idx_f, (_, comm_f, norm_f) in enumerate(phi_basis_ti):
                        b23 = np.max(np.abs(comm_f[np.ix_(B2_modes, B3_modes)])) if B3_modes.size > 0 else 0
                        b21 = np.max(np.abs(comm_f[np.ix_(B2_modes, B1_modes)])) if B1_modes.size > 0 else 0
                        if max(b23, b21) > best_mix:
                            best_mix = max(b23, b21)
                            phi_dir_ti = comm_f

                evals_phys, evecs_phys, _ = construct_D_phys(
                    ev_s, ec_s, phi_dir_ti, phi_amp, B_J)

            # Identify B2 branch via overlap
            b2_idx, b2_ness = identify_B2_branch(evals_phys, ev_s, evecs_phys, ec_s)
            b2_evals = evals_phys[b2_idx]
            b2_mean = np.mean(b2_evals)

            B2_mean_at_tau.append(b2_mean)
            tau_points.append(tau)
            all_B2_evals[(ti, phi_amp)] = b2_evals

        # Fit spline and find minimum
        tau_points = np.array(tau_points)
        B2_mean_at_tau = np.array(B2_mean_at_tau)

        if len(tau_points) >= 4:
            cs = CubicSpline(tau_points, B2_mean_at_tau)
            B2_dense = cs(tau_dense)
            min_idx = np.argmin(B2_dense)
            tau_min = tau_dense[min_idx]
            B2_min = B2_dense[min_idx]

            # Curvature at minimum (second derivative)
            d2_B2 = cs(tau_min, 2)  # Second derivative

            all_B2_min_tau[phi_amp] = tau_min
            all_B2_d2[phi_amp] = d2_B2
        else:
            all_B2_min_tau[phi_amp] = tau_points[np.argmin(B2_mean_at_tau)]
            all_B2_d2[phi_amp] = 0

    # ================================================================
    #  Phase 3: Report results
    # ================================================================
    print("\n" + "=" * 78)
    print("Phase 3: Results")
    print("=" * 78)

    print(f"\n  B2 fold analysis under worst-case phi direction ({worst_name}):")
    print(f"  {'|phi|':>8s}  {'tau_min':>8s}  {'d2(B2)':>10s}  {'B2_split':>10s}  Status")
    print(f"  {'-'*8:>8s}  {'-'*8:>8s}  {'-'*10:>10s}  {'-'*10:>10s}  ------")

    gate_phi_gap = gap_b3_b2  # Use actual gap as phi scale (was 0.07 nominal)
    gate_phi_2gap = 2 * gap_b3_b2
    fold_survives_at_gap = False
    fold_survives_at_2gap = False
    max_phi_survival = 0

    for phi_amp in phi_amplitudes:
        tau_min = all_B2_min_tau.get(phi_amp, np.nan)
        d2 = all_B2_d2.get(phi_amp, 0)

        # B2 splitting at fold location
        ti_closest = np.argmin(np.abs(tau_vals[tau_scan_indices] - tau_min))
        ti_fold = tau_scan_indices[ti_closest]
        b2_ev = all_B2_evals.get((ti_fold, phi_amp), np.array([0]))
        split = np.max(b2_ev) - np.min(b2_ev)

        fold_exists = d2 > 0 and 0.14 <= tau_min <= 0.24
        status = "FOLD" if fold_exists else "FLAT/DESTROYED"

        if fold_exists:
            max_phi_survival = phi_amp
            if phi_amp >= gate_phi_gap - 0.005:
                fold_survives_at_gap = True
            if phi_amp >= gate_phi_2gap - 0.005:
                fold_survives_at_2gap = True

        print(f"  {phi_amp:8.4f}  {tau_min:8.4f}  {d2:10.4f}  {split:10.6f}  {status}")

    # ================================================================
    #  Phase 4: Comprehensive phi direction survey
    # ================================================================
    print("\n" + "=" * 78)
    print("Phase 4: Survey ALL phi directions at |phi| = gap_B2-B3")
    print("=" * 78)

    phi_test = gap_b3_b2
    print(f"  Testing |phi| = {phi_test:.6f} (gap B3-B2 at tau=0.20)")

    # At reference tau=0.20, test every generator direction
    survival_by_gen = {}
    for gen_idx, (name, comm, norm) in enumerate(phi_basis_ref):
        evals_test, evecs_test, _ = construct_D_phys(
            evals_sorted, evecs_sorted, comm / norm, phi_test, B_J)

        # Track B2 branch
        b2_idx, _ = identify_B2_branch(evals_test, evals_sorted, evecs_test, evecs_sorted)
        b2_test = evals_test[b2_idx]
        b2_mean = np.mean(b2_test)
        b2_split = np.max(b2_test) - np.min(b2_test)

        survival_by_gen[name] = {
            'b2_mean': b2_mean,
            'b2_split': b2_split,
            'b2_evals': b2_test,
        }

    # Now check fold across tau for EACH generator at phi=gap
    print(f"\n  Per-generator fold check at |phi| = {phi_test:.6f}:")
    print(f"  {'Generator':>12s}  {'B2_mean':>8s}  {'B2_split':>10s}  {'d2_fold':>10s}  Status")

    fold_count = 0
    for gen_idx, (name, comm, norm) in enumerate(phi_basis_ref):
        b2_tau = []
        for ti in tau_scan_indices:
            ev = kosmann[f'eigenvalues_{ti}']
            ec = kosmann[f'eigenvectors_{ti}']
            si = np.argsort(ev)
            ev_s, ec_s = ev[si], ec[:, si]

            phi_local = compute_phi_generators(ev_s, ec_s, [(name, af_gens[gen_idx][1] if gen_idx < len(af_gens) else af_gens[0][1])])
            # Find matching generator
            phi_d = None
            for n2, c2, nm2 in phi_local:
                if n2 == name:
                    phi_d = c2 / nm2 if nm2 > 1e-12 else c2
                    break
            if phi_d is None:
                # Recompute properly
                phi_all = compute_phi_generators(ev_s, ec_s, af_gens)
                for n2, c2, nm2 in phi_all:
                    if n2 == name:
                        phi_d = c2 / nm2 if nm2 > 1e-12 else c2
                        break
            if phi_d is None:
                continue

            ev_ph, ec_ph, _ = construct_D_phys(ev_s, ec_s, phi_d, phi_test, B_J)
            b2i, _ = identify_B2_branch(ev_ph, ev_s, ec_ph, ec_s)
            b2_tau.append(np.mean(ev_ph[b2i]))

        if len(b2_tau) >= 4:
            cs = CubicSpline(tau_vals[tau_scan_indices[:len(b2_tau)]], b2_tau)
            b2_dense_gen = cs(tau_dense)
            min_i = np.argmin(b2_dense_gen)
            tm = tau_dense[min_i]
            d2_gen = cs(tm, 2)
            fold_ok = d2_gen > 0 and 0.14 <= tm <= 0.24
            if fold_ok:
                fold_count += 1
            status = "FOLD" if fold_ok else "DESTROYED"
            b2m = survival_by_gen[name]['b2_mean']
            b2s = survival_by_gen[name]['b2_split']
            print(f"  {name:>12s}  {b2m:8.5f}  {b2s:10.6f}  {d2_gen:10.4f}  {status}")

    print(f"\n  Fold survival: {fold_count}/{len(phi_basis_ref)} generators preserve fold")

    # ================================================================
    #  Gate classification
    # ================================================================
    print("\n" + "=" * 78)
    print("GATE DPHYS-34a-1 CLASSIFICATION")
    print("=" * 78)

    print(f"\n  Worst-case phi direction: {worst_name}")
    print(f"  Max inter-branch mixing: {worst_mixing:.6f}")
    print(f"  Gap B3-B2 at tau=0.20: {gap_b3_b2:.6f}")
    print(f"  Gap B2-B1 at tau=0.20: {gap_b2_b1:.6f}")
    print(f"  Max |phi| with fold survival: {max_phi_survival:.4f}")
    print(f"  Fold survival generators: {fold_count}/{len(phi_basis_ref)}")

    if fold_survives_at_gap:
        if fold_survives_at_2gap:
            verdict = "STRONG PASS"
            print(f"\n  VERDICT: STRONG PASS")
            print(f"  B2 fold persists up to |phi| = 2*gap = {gate_phi_2gap:.4f}")
        else:
            verdict = "PASS"
            print(f"\n  VERDICT: PASS")
            print(f"  B2 fold persists at |phi| = gap = {gate_phi_gap:.4f}")
    else:
        verdict = "FAIL"
        print(f"\n  VERDICT: FAIL")
        print(f"  B2 fold destroyed at |phi| = gap = {gate_phi_gap:.4f}")

    # ================================================================
    #  Save results
    # ================================================================
    save_dict = {
        'tau_values': tau_vals,
        'tau_scan_indices': np.array(tau_scan_indices),
        'phi_amplitudes': phi_amplitudes,
        'worst_name': worst_name,
        'worst_mixing': worst_mixing,
        'gap_b3_b2': gap_b3_b2,
        'gap_b2_b1': gap_b2_b1,
        'max_phi_survival': max_phi_survival,
        'fold_count': fold_count,
        'total_generators': len(phi_basis_ref),
        'verdict': verdict,
    }

    # Store B2 mean eigenvalue arrays
    for phi_amp in phi_amplitudes:
        tau_min = all_B2_min_tau.get(phi_amp, np.nan)
        d2 = all_B2_d2.get(phi_amp, 0)
        save_dict[f'tau_min_phi{phi_amp:.4f}'] = tau_min
        save_dict[f'd2_phi{phi_amp:.4f}'] = d2

    # Store mixing analysis
    mixing_names = [m[0] for m in mixing_details]
    mixing_b23 = [m[1] for m in mixing_details]
    mixing_b21 = [m[2] for m in mixing_details]
    mixing_b22 = [m[3] for m in mixing_details]
    save_dict['mixing_b2_b3'] = np.array(mixing_b23)
    save_dict['mixing_b2_b1'] = np.array(mixing_b21)
    save_dict['mixing_b2_b2_off'] = np.array(mixing_b22)

    out_npz = os.path.join(SCRIPT_DIR, 's34a_dphys_fold.npz')
    np.savez(out_npz, **save_dict)
    print(f"\n  Saved: {out_npz}")

    # ================================================================
    #  Plot
    # ================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: B2 mean eigenvalue vs tau for several phi amplitudes
    ax = axes[0, 0]
    for phi_amp in [0, 0.02, 0.05, 0.07, 0.10, 0.14, 0.20]:
        if phi_amp > max(phi_amplitudes):
            continue
        b2_tau_list = []
        for ti in tau_scan_indices:
            key = (ti, phi_amp)
            if key in all_B2_evals:
                b2_tau_list.append(np.mean(all_B2_evals[key]))
        if len(b2_tau_list) == len(tau_scan_indices):
            ax.plot(tau_vals[tau_scan_indices], b2_tau_list,
                    'o-', label=f'|phi|={phi_amp:.2f}', markersize=4)
    ax.set_xlabel('tau')
    ax.set_ylabel('B2 mean eigenvalue')
    ax.set_title(f'B2 branch under {worst_name} fluctuation')
    ax.legend(fontsize=7)
    ax.axvline(x=0.19, color='gray', ls='--', alpha=0.5, label='bare fold')

    # Panel 2: Fold curvature d2 vs phi amplitude
    ax = axes[0, 1]
    phis = sorted(all_B2_d2.keys())
    d2s = [all_B2_d2[p] for p in phis]
    ax.plot(phis, d2s, 'b-o', markersize=4)
    ax.axhline(y=0, color='r', ls='--', alpha=0.7)
    ax.axvline(x=gap_b3_b2, color='g', ls='--', alpha=0.5, label=f'gap={gap_b3_b2:.3f}')
    ax.axvline(x=2*gap_b3_b2, color='orange', ls='--', alpha=0.5, label=f'2*gap={2*gap_b3_b2:.3f}')
    ax.set_xlabel('|phi_VEV|')
    ax.set_ylabel('d^2(B2)/dtau^2 at minimum')
    ax.set_title('Fold curvature vs fluctuation amplitude')
    ax.legend(fontsize=8)

    # Panel 3: Fold location tau_min vs phi
    ax = axes[1, 0]
    taus_min = [all_B2_min_tau[p] for p in phis]
    ax.plot(phis, taus_min, 'r-o', markersize=4)
    ax.axhline(y=0.19, color='gray', ls='--', alpha=0.5, label='bare fold')
    ax.axvline(x=gap_b3_b2, color='g', ls='--', alpha=0.5)
    ax.set_xlabel('|phi_VEV|')
    ax.set_ylabel('tau_min (fold location)')
    ax.set_title('Fold location drift under fluctuation')
    ax.legend(fontsize=8)

    # Panel 4: B2 splitting at fold
    ax = axes[1, 1]
    splits = []
    for phi_amp in phis:
        tau_min = all_B2_min_tau.get(phi_amp, 0.19)
        ti_closest = tau_scan_indices[np.argmin(np.abs(tau_vals[tau_scan_indices] - tau_min))]
        b2_ev = all_B2_evals.get((ti_closest, phi_amp), np.array([0]))
        splits.append(np.max(b2_ev) - np.min(b2_ev))
    ax.plot(phis, splits, 'g-o', markersize=4)
    ax.axvline(x=gap_b3_b2, color='g', ls='--', alpha=0.5, label=f'gap={gap_b3_b2:.3f}')
    ax.set_xlabel('|phi_VEV|')
    ax.set_ylabel('B2 eigenvalue splitting')
    ax.set_title('Degeneracy lifting by inner fluctuation')
    ax.legend(fontsize=8)

    fig.suptitle(f'Gate DPHYS-34a-1: {verdict}', fontsize=14, fontweight='bold')
    plt.tight_layout()
    out_png = os.path.join(SCRIPT_DIR, 's34a_dphys_fold.png')
    plt.savefig(out_png, dpi=150)
    print(f"  Saved: {out_png}")

    elapsed = time.time() - t0
    print(f"\n  Total runtime: {elapsed:.1f}s")
    print(f"\n  GATE DPHYS-34a-1: {verdict}")

    return verdict


if __name__ == '__main__':
    main()
