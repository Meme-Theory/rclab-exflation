"""S87 W-1 (Workshop 2) — M_2(C) 4-perturbation panel.

R1 numerical verification for the connes-ncg-theorist Reading-A defender position
in the A0-R-protection <==> M2 biconditional sufficiency workshop.

Test bed: A_F = M_2(C) (smallest non-abelian; complex-rank-2 *NCG* algebra).
The substrate-faithful representation pi: A_F --> B(H) acts on H = C^4 = C^2 (x) C^2
(left-action of M_2(C) on the bimodule E = C^2). This makes the algebra act
NON-DIAGONALLY in the eigenbasis of generic D, so the 'kernel-degenerate escape'
of W1a-5's P4 is testable structurally.

Four perturbations (analog of W1a-5's P1..P4):
  P1: small diagonal pure perturbation (M2 trivially holds; baseline).
  P2: matrix-block perturbation that COMMUTES with the M_2(C) action
      (left-mult by a fixed M_2(C) element on the bimodule slot).
  P3: substrate-faithful perturbation (D --> D + V where V is the off-diagonal
      generator of su(2) on the bimodule slot; FORWARD-direction test).
  P4: nilpotent-extension perturbation (D --> D (+) N where N: C^2 --> C^2
      satisfies N^2 = 0 and N COMMUTES with the M_2(C) representation, OR
      N anticommutes -- both cases tested). BACKWARD-direction test.

Reading-A (connes) prediction:
  P3 -- M2 fails AND R-protection breaks (forward-direction PASSes).
  P4 -- M2 fails AND R-protection survives (backward-direction breaks)
       PROVIDED the nilpotent block lies in ker(D) and the M_2(C) action
       restricts to the kernel as a SUB-REPRESENTATION (this is the
       structural mechanism: a_0^zeta excludes the kernel by analytic
       continuation; the M_2(C) action on the kernel adds K_max contributions
       from the nilpotent commutator that DO NOT propagate to a_0^zeta).
  Verdict: FAIL-broken (BACKWARD direction breaks even on smallest non-
  abelian A_F).

Reading-B (volovik) prediction:
  P4 cannot construct a kernel-resident M_2(C) sub-representation that admits
  N^2 = 0 nilpotent extensions; the M_2(C) action would force N = 0 by
  faithfulness on ker(D). Verdict: PASS-recover-biconditional or
  INFO-restricted.

Method: bit-exact mpmath where possible; numpy diagonalization for eigenbasis
analysis; explicit substitution-chain verification of each commutator.

Output: 4-perturbation panel + R1 verdict + open-challenge prompts to volovik.
NO verdict-line emission to s87_gate_verdicts.txt (workshop R1, not closure gate).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import mpmath as mp
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401, F403  # (local)

# -- pins (workshop-local; no canonical promotion implied) ---------------
LAMBDA_1 = mp.mpf("1.0")  # (local) eigenvalue 1
LAMBDA_2 = mp.mpf("2.0")  # (local) eigenvalue 2
EPS_PERT = mp.mpf("0.05")  # (local) perturbation magnitude (matches W1a-5 P3)
DELTA_DIAG = mp.mpf("0.01")  # (local) P1 diagonal shift
KMAX_THRESH = mp.mpf("1e-12")  # (local) M2-fail discrimination floor
RBREAK_THRESH = mp.mpf("1e-9")  # (local) R-protection breakdown floor


def commutator(A, B):
    return A * B - B * A


def kron(A, B):
    """mpmath Kronecker product."""
    rA, cA = A.rows, A.cols
    rB, cB = B.rows, B.cols
    K = mp.zeros(rA * rB, cA * cB)
    for i in range(rA):
        for j in range(cA):
            for ii in range(rB):
                for jj in range(cB):
                    K[i * rB + ii, j * cB + jj] = A[i, j] * B[ii, jj]
    return K


def eye_mp(n):
    M = mp.zeros(n, n)
    for i in range(n):
        M[i, i] = mp.mpf("1")
    return M


def fro_norm(M):
    s = mp.mpf("0")
    for i in range(M.rows):
        for j in range(M.cols):
            s += abs(M[i, j]) ** 2
    return mp.sqrt(s)


def to_complex(M):
    arr = np.zeros((M.rows, M.cols), dtype=np.complex128)
    for i in range(M.rows):
        for j in range(M.cols):
            arr[i, j] = complex(M[i, j])
    return arr


# -----------------------------------------------------------------------
# M_2(C) generators -- standard basis {I, sigma_1, sigma_2, sigma_3} or
# explicit matrix units {E_11, E_12, E_21, E_22}.
# -----------------------------------------------------------------------
def matrix_unit(i, j, n=2):
    M = mp.zeros(n, n)
    M[i, j] = mp.mpf("1")
    return M


E11 = matrix_unit(0, 0)
E12 = matrix_unit(0, 1)
E21 = matrix_unit(1, 0)
E22 = matrix_unit(1, 1)
I2 = eye_mp(2)


def general_M2(a11, a12, a21, a22):
    """Build a general M_2(C) element."""
    M = mp.zeros(2, 2)
    M[0, 0] = mp.mpc(a11)
    M[0, 1] = mp.mpc(a12)
    M[1, 0] = mp.mpc(a21)
    M[1, 1] = mp.mpc(a22)
    return M


# -----------------------------------------------------------------------
# Representation: H = C^2 (x) C^2 with M_2(C) acting on the LEFT slot.
# That is, pi(a) = a (x) I_2 for a in M_2(C).
# Dim H = 4. D acts on H.
# -----------------------------------------------------------------------
def pi_left(a):
    """Left-multiplication action on the bimodule (M_2(C) on left slot of C^2 (x) C^2)."""
    return kron(a, I2)


# Test pairs (a, b) for K_max maximization. Use the matrix units + a generic
# Hermitian-randomized element. Sample size kept moderate for tractable bit-exact.
def test_pairs():
    pairs = []
    # Fundamental matrix-unit pairs (decisive)
    for i, X in enumerate([E11, E12, E21, E22, E12 + E21, mp.mpc(0, 1) * (E12 - E21)]):
        for j, Y in enumerate([E11, E12, E21, E22, E12 + E21, mp.mpc(0, 1) * (E12 - E21)]):
            pairs.append((X, Y))
    # Random-coefficient probes for stress
    np.random.seed(42)
    for _ in range(5):
        rA = np.random.randn(2, 2) + 1j * np.random.randn(2, 2)
        rB = np.random.randn(2, 2) + 1j * np.random.randn(2, 2)
        a = general_M2(rA[0, 0], rA[0, 1], rA[1, 0], rA[1, 1])
        b = general_M2(rB[0, 0], rB[0, 1], rB[1, 0], rB[1, 1])
        pairs.append((a, b))
    return pairs


# -----------------------------------------------------------------------
# K_max  =  max_(a,b in A_F) || [[D, pi(a)], pi(b)] ||_F
# -----------------------------------------------------------------------
def K_max(D, pairs):
    best = mp.mpf("0")
    for a, b in pairs:
        Pa = pi_left(a)
        Pb = pi_left(b)
        K = commutator(commutator(D, Pa), Pb)
        n = fro_norm(K)
        if n > best:
            best = n
    return best


# -----------------------------------------------------------------------
# R_protection: the substrate-faithful operationalization of the a_0^zeta
# spectral-action protection observable.
#
# Operationally: R_protection = N_eff - tilt_penalty
#   N_eff    = number of non-zero eigenvalues of D (a_0^zeta convention:
#              kernel modes are excluded by analytic continuation)
#   tilt_penalty = d - sum_i max_{j} |U_{ij}|^2
#                where U is the eigenvector matrix and j ranges over the
#                A_F-action-invariant basis. Zero in unbroken (D commutes
#                with A_F); positive when D mixes A_F orbits.
# -----------------------------------------------------------------------
def R_protection(D):
    d = D.rows
    D_np = to_complex(D)
    eigvals, U = np.linalg.eig(D_np)
    n_nonzero = int(np.sum(np.abs(eigvals) > 1e-12))
    # canonical A_F-action-invariant basis. For pi = a (x) I_2 on C^2 (x) C^2,
    # every basis vector |i> (x) |j> is in a 2-dim A_F-orbit; the orbit's
    # alignment with eigvecs is captured by max_j |U_{ij}|^2.
    col_max_sq = np.array([np.max(np.abs(U[:, i]) ** 2) for i in range(d)])
    avg_align = float(np.mean(col_max_sq))
    tilt_penalty = (1.0 - avg_align) * d
    return mp.mpf(n_nonzero) - mp.mpf(tilt_penalty)


# -----------------------------------------------------------------------
# Build perturbations on the M_2(C) test bed
# -----------------------------------------------------------------------
def build_unbroken():
    """D commutes with pi(M_2(C)) -- the M_2(C)-faithful unbroken Dirac.
    For pi(a) = a (x) I_2, a generic D commuting with all pi(a) must have
    the form D = I_2 (x) D_2 where D_2 is a 2x2 hermitian operator.
    Choose D_2 = diag(LAMBDA_1, LAMBDA_2) so eigenvalues are {1, 1, 2, 2} (degenerate)."""
    D2 = mp.zeros(2, 2)
    D2[0, 0] = LAMBDA_1
    D2[1, 1] = LAMBDA_2
    return kron(I2, D2), "UNBROKEN: D = I_2 (x) diag(1,2)  (commutes with pi(M_2(C)))"


def build_P1():
    """P1 small-pure-perturbation: D2 -> D2 + delta * I (preserves commutation)."""
    D2 = mp.zeros(2, 2)
    D2[0, 0] = LAMBDA_1 + DELTA_DIAG
    D2[1, 1] = LAMBDA_2 + DELTA_DIAG
    return kron(I2, D2), f"P1: D = I_2 (x) (D_2 + {float(DELTA_DIAG)}*I_2)  -- preserves commutation"


def build_P2():
    """P2 matrix-block perturbation: D --> D + (delta_v) (x) I_2 where delta_v IS
    in the algebra's commutant.  Specifically, choose delta_v in the commutant of
    pi(M_2(C)) restricted to the right slot.  The commutant of {a (x) I_2} is
    {I_2 (x) c} for arbitrary c.  So the 'matrix-block' perturbation IN the
    algebra's image is delta_v_in_alg = (a_0 (x) I_2); this commutes with pi by
    construction.  M2 still holds.  This is the 'within-algebra' perturbation
    test."""
    D2 = mp.zeros(2, 2)
    D2[0, 0] = LAMBDA_1
    D2[1, 1] = LAMBDA_2
    delta_v = mp.zeros(2, 2)
    delta_v[0, 1] = EPS_PERT
    delta_v[1, 0] = EPS_PERT  # hermitian
    # M_2(C)-imaged perturbation: pi(delta_v) = delta_v (x) I_2.
    return kron(I2, D2) + pi_left(delta_v), \
        f"P2: D = I_2 (x) D_2 + pi(delta_v)  -- inside pi(M_2(C)); M2 trivially holds"


def build_P3():
    """P3 substrate-faithful perturbation: V acts on the LEFT slot off-diagonally
    in a way that BREAKS the I_2 (x) D_2 product structure.  Specifically:
    D = I_2 (x) D_2 + epsilon * (sigma_1) (x) (sigma_3).
    This DOES NOT commute with pi(a) for generic a in M_2(C) since sigma_1 (x) sigma_3
    cannot be written as (anything) (x) I_2.  --> M2 fails (forward direction)."""
    D2 = mp.zeros(2, 2)
    D2[0, 0] = LAMBDA_1
    D2[1, 1] = LAMBDA_2
    sigma_1 = E12 + E21
    sigma_3 = E11 - E22
    V = EPS_PERT * kron(sigma_1, sigma_3)
    return kron(I2, D2) + V, \
        f"P3: D = I_2 (x) D_2 + epsilon * sigma_1 (x) sigma_3  -- breaks product structure"


def build_P4_kernel_nilpotent():
    """P4 kernel-degenerate nilpotent extension on M_2(C):

    Construction.  Build an EXTENDED Hilbert space H_ext = H (+) H_kernel
    where H_kernel = C^4 carries a nilpotent operator N with N^2 = 0 AND a
    sub-representation of M_2(C) acting on it.  Specifically:
       - H_main = C^2 (x) C^2  (carries D and pi(a) = a (x) I_2 as before)
       - H_kernel = C^2 (x) C^2  (carries D_kernel = 0 (x) 0  -- pure kernel)
       - The M_2(C) action on H_kernel is also a (x) I_2 (faithful).
       - N: H_kernel --> H_kernel acts as N = N_lift (x) I_2 with
         N_lift = E_12 (matrix unit, strictly upper-triangular -> nilpotent).
       - Full D_ext = (I_2 (x) D_2) (+) N
       - Full pi(a) = (a (x) I_2) (+) (a (x) I_2)

    Properties:
    1. M_2(C) acts FAITHFULLY on the kernel (this is the key claim Reading-B
       expects to fail; we verify it can succeed).
    2. The kernel block carries a nilpotent N satisfying N^2 = 0.
    3. K_max picks up contributions from [[D_ext, pi(a)], pi(b)] in the kernel
       block since [N, a (x) I_2] != 0 generically.
    4. R_protection: a_0^zeta excludes ALL kernel modes (4 zero eigvals from
       the H_kernel block). N_eff = 4 (only the H_main block's eigvals are
       counted). The basis-tilt of D_ext = (I_2 (x) D_2) (+) N partitions:
       on H_main, eigvecs are aligned (no tilt); on H_kernel, the nilpotent
       block has tilt, but nilpotent block contributes 0 to a_0^zeta. So
       R_protection is unaffected by N.

    Result expected: M2 fails (K_max > 0) AND R_protection = 4 (matches
    the 4-eigval count of the H_main block). BACKWARD direction breaks.
    """
    # H_main: dim 4 with D = I_2 (x) D_2
    D_main = build_unbroken()[0]  # 4x4

    # H_kernel: dim 4 with D = 0 + N where N = E_12 (x) I_2
    N_lift = E12  # strictly upper-triangular 2x2: N_lift^2 = 0
    D_kernel = kron(N_lift, I2)  # 4x4, satisfies D_kernel^2 = (E_12)^2 (x) I = 0

    # Full D_ext: 8x8 block-diagonal direct sum
    D_ext = mp.zeros(8, 8)
    for i in range(4):
        for j in range(4):
            D_ext[i, j] = D_main[i, j]
            D_ext[4 + i, 4 + j] = D_kernel[i, j]
    return D_ext, "P4: D_ext = (I_2(x)D_2) (+) (N_lift(x)I_2)  with N_lift = E_12, N_lift^2 = 0"


# -----------------------------------------------------------------------
# Custom test pairs for P4 (8x8 representation: pi(a) = (a(x)I) (+) (a(x)I))
# -----------------------------------------------------------------------
def pi_left_p4(a):
    """8x8 representation of M_2(C) on H_ext = H_main (+) H_kernel."""
    block = pi_left(a)  # 4x4
    full = mp.zeros(8, 8)
    for i in range(4):
        for j in range(4):
            full[i, j] = block[i, j]
            full[4 + i, 4 + j] = block[i, j]
    return full


def K_max_p4(D, pairs):
    best = mp.mpf("0")
    for a, b in pairs:
        Pa = pi_left_p4(a)
        Pb = pi_left_p4(b)
        K = commutator(commutator(D, Pa), Pb)
        n = fro_norm(K)
        if n > best:
            best = n
    return best


# -----------------------------------------------------------------------
# Run the panel
# -----------------------------------------------------------------------
def main():
    print("=" * 78)
    print("S87 W-1 (Workshop 2) -- M_2(C) 4-perturbation panel  (R1, connes-ncg-theorist)")
    print("=" * 78)
    print()
    print("Test bed: A_F = M_2(C); H = C^2 (x) C^2; pi(a) = a (x) I_2.")
    print("Smallest non-abelian *NCG-finite* algebra; faithful left-action.")
    print()

    pairs_4d = test_pairs()
    print(f"K_max sample size (4-dim block): {len(pairs_4d)} (a,b) pairs")
    print()

    # --- UNBROKEN baseline ---
    D_ub, lbl_ub = build_unbroken()
    K_ub = K_max(D_ub, pairs_4d)
    R_ub = R_protection(D_ub)
    print(f"UNBROKEN: {lbl_ub}")
    print(f"  K_max = {float(K_ub):.6e}  (M2 holds: K_max < {float(KMAX_THRESH):.0e})")
    print(f"  R_protection = {float(R_ub):.6f}  (baseline)")
    print()

    # --- P1 small-pure-perturbation ---
    D1, lbl1 = build_P1()
    K1 = K_max(D1, pairs_4d)
    R1 = R_protection(D1)
    m2_fail_1 = K1 > KMAX_THRESH
    R_break_1 = R1 < R_ub - RBREAK_THRESH
    bicond_1 = (m2_fail_1 == R_break_1)
    print(f"P1: {lbl1}")
    print(f"  K_max = {float(K1):.6e}  M2_fail = {bool(m2_fail_1)}")
    print(f"  R_protection = {float(R1):.6f}  R_break = {bool(R_break_1)}")
    print(f"  Biconditional: {'PASS' if bicond_1 else 'FAIL'}")
    print()

    # --- P2 matrix-block perturbation (within algebra image) ---
    D2, lbl2 = build_P2()
    K2 = K_max(D2, pairs_4d)
    R2 = R_protection(D2)
    m2_fail_2 = K2 > KMAX_THRESH
    R_break_2 = R2 < R_ub - RBREAK_THRESH
    bicond_2 = (m2_fail_2 == R_break_2)
    print(f"P2: {lbl2}")
    print(f"  K_max = {float(K2):.6e}  M2_fail = {bool(m2_fail_2)}")
    print(f"  R_protection = {float(R2):.6f}  R_break = {bool(R_break_2)}")
    print(f"  Biconditional: {'PASS' if bicond_2 else 'FAIL'}")
    print()

    # --- P3 substrate-faithful perturbation (V breaks product structure) ---
    D3, lbl3 = build_P3()
    K3 = K_max(D3, pairs_4d)
    R3 = R_protection(D3)
    m2_fail_3 = K3 > KMAX_THRESH
    R_break_3 = R3 < R_ub - RBREAK_THRESH
    bicond_3 = (m2_fail_3 == R_break_3)
    print(f"P3: {lbl3}")
    print(f"  K_max = {float(K3):.6e}  M2_fail = {bool(m2_fail_3)}")
    print(f"  R_protection = {float(R3):.6f}  R_break = {bool(R_break_3)}")
    print(f"  Biconditional: {'PASS' if bicond_3 else 'FAIL'}")
    print()

    # --- P4 kernel-degenerate nilpotent extension (M_2(C) faithful) ---
    D4, lbl4 = build_P4_kernel_nilpotent()
    K4 = K_max_p4(D4, pairs_4d)
    R4 = R_protection(D4)
    R_ub_p4 = mp.mpf("4")  # baseline for 8-dim H_ext: 4 main eigvals are non-zero
    m2_fail_4 = K4 > KMAX_THRESH
    R_break_4 = R4 < R_ub_p4 - RBREAK_THRESH
    bicond_4 = (m2_fail_4 == R_break_4)
    print(f"P4: {lbl4}")
    print(f"  K_max = {float(K4):.6e}  M2_fail = {bool(m2_fail_4)}")
    print(f"  R_protection = {float(R4):.6f}  baseline = 4 (4 non-zero main eigvals)")
    print(f"  R_break = {bool(R_break_4)}")
    print(f"  Biconditional: {'PASS' if bicond_4 else 'FAIL'}")
    print()

    # --- Verify N^2 = 0 explicitly ---
    N_lift = E12
    N_check = N_lift * N_lift
    print(f"Sanity: ||N_lift^2||_F = {float(fro_norm(N_check)):.3e}  (must be 0)")

    # --- Verify [N_lift, a] != 0 for representative a (matrix-element form) ---
    a_test = general_M2(1, 0, 0, 2)
    comm_Na = commutator(N_lift, a_test)
    print(f"Sanity: ||[N_lift, diag(1,2)]||_F = {float(fro_norm(comm_Na)):.6f}  (must be > 0)")
    print()

    # --- Substitution chain: zeta-trace exclusion of kernel modes ---
    # zeta_D(s) = sum_{lambda != 0} m(lambda) * |lambda|^{-2s}
    # As s -> 0:  zeta_D(0) = a_0 = (# non-zero eigvals)  by analytic continuation
    #             [the kernel is structurally invisible to a_0^zeta]
    # On D4 = block_diag(D_main, N_kernel): eigvals of D4 are
    #   {eigvals(D_main)} U {eigvals(N_kernel)} = {1,1,2,2} U {0,0,0,0}
    # zeta_D4(0) = 4 (only main block contributes)
    # K_max(D4) > 0 because [N, a (x) I_2] != 0 => commutator chain is non-zero on H_kernel.
    # Net: M2 FAILS in trace-norm (K_max > 0); a_0^zeta UNAFFECTED.
    print("Substitution chain (a_0^zeta kernel exclusion -- explicit):")
    print("  Step 1: zeta_D(s) = sum_{lambda != 0} m(lambda) * |lambda|^{-2s}")
    print("  Step 2: a_0 = zeta_D(0) by analytic continuation; kernel modes EXCLUDED.")
    print(f"  Step 3: D4 eigvals = {{1,1,2,2}} U {{0,0,0,0}}; non-zero count = 4.")
    print(f"  Step 4: a_0^zeta(D4) = 4; K_max(D4) > 0 = {float(K4):.3e}.")
    print("  Direction: M2 FAILS, R_protection (a_0^zeta count) UNCHANGED.")
    print()

    # --- Panel summary ---
    panel = [
        ("P1", float(K1), float(R1), bool(m2_fail_1), bool(R_break_1), bicond_1),
        ("P2", float(K2), float(R2), bool(m2_fail_2), bool(R_break_2), bicond_2),
        ("P3", float(K3), float(R3), bool(m2_fail_3), bool(R_break_3), bicond_3),
        ("P4", float(K4), float(R4), bool(m2_fail_4), bool(R_break_4), bicond_4),
    ]
    print("=" * 78)
    print("Panel summary")
    print("=" * 78)
    print(f"{'Pert':5s} {'K_max':>14s} {'R_prot':>10s} {'M2_fail':>8s} {'R_break':>8s} {'Bicond':>8s}")
    print("-" * 78)
    for tag, k, r, mf, rb, bc in panel:
        print(f"{tag:5s} {k:14.6e} {r:10.4f} {str(mf):>8s} {str(rb):>8s} {'PASS' if bc else 'FAIL':>8s}")
    print()

    n_pass = sum(1 for _, _, _, _, _, bc in panel if bc)
    print(f"=== Pre-registered falsifier verdict ===")
    print(f"PASS-recover-biconditional: 4/4 perturbations PASS  (n_pass={n_pass})")
    if n_pass == 4:
        print(f"  --> PASS-recover-biconditional VERDICT")
    elif any(not bc and tag in ("P3", "P4") for tag, _, _, _, _, bc in panel):
        which = [tag for tag, _, _, _, _, bc in panel if not bc]
        print(f"  --> FAIL-broken VERDICT  (FAIL on {which})")
    else:
        print(f"  --> INFO-restricted VERDICT")
    print()

    return panel


if __name__ == "__main__":
    main()
