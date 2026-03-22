"""
DEBUG v8: The correct gauge for computing A_F.

Key insight from v7: Baptista's L+R combines left pi(A_F) action with
right J*pi(A_F)*J^{-1} action. To find A_F, we need the commutant of
JUST the LEFT action of the gauge group, then impose J.

In Connes' NCG:
- The algebra A_F acts from the LEFT: pi(a) for a in A_F
- The gauge group U(A_F) = unitaries of A_F act via pi(u)
- The commutant of the gauge group = commutant of pi(A_F)

In Baptista's framework:
- L_v: LEFT action of su(3) on Psi -- this is the gauge transformation
- R_v: RIGHT action of su(3) -- this is the coordinate (fiber) action
- L+R: combined action (only a homomorphism for u(2))

The LEFT gauge action (L restricted to u(2)) should be the Lie algebra
of U(A_F) acting via pi. The commutant of L_{u(2)} should contain pi(A_F).

But actually:
- L_v acts by LEFT multiplication on the 4x4 internal matrix
- R_v acts by RIGHT multiplication
- The gauge fields in Baptista are A_L (valued in u(2)) and A_R (valued in su(3))
- A_L transforms via L, A_R transforms via R

Wait -- A_L and A_R are BOTH gauge fields. The full gauge group is
U(2)_L x SU(3)_R. In Connes' language:
- U(2)_L corresponds to the SU(2)_L x U(1)_Y part of SM gauge
- SU(3)_R corresponds to the color SU(3)_c part

This means the FULL gauge algebra is u(2)_L + su(3)_R.
The algebra A_F should be the commutant of the FULL gauge, not just L.

But v3 test (b) showed: commutant of u(2)_{L+R} + R_{su(3)} = 14-dim.
And test (c): commutant of L_{u(2)} + R_{su(3)} = 14-dim (same!).

Both give 14-dim, which is NOT A_F.

So maybe the issue is that L_{u(2)} is NOT the correct left gauge.
The L action involves BOTH L and R (since L is LEFT multiplication
on the internal matrix, which acts on both row and column indices).

Let me reconsider from scratch.

The fundamental question: what is the GAUGE GROUP in Baptista's framework?

From Baptista 2024 (paper 15), the gauge group is:
- Isometry group of the internal metric g_s on K = SU(3)
- For the deformed metric: Isom(SU(3), g_s) = (SU(3)_L x U(2)_R) / Z_6
- The LEFT SU(3) acts as left translations on SU(3)
- The RIGHT U(2) acts as right translations by the stabilizer

The LEFT SU(3) gives the color gauge group SU(3)_c.
The RIGHT U(2) gives the electroweak gauge group SU(2)_L x U(1)_Y.

WAIT: this is the OPPOSITE of what I assumed! The COLOR group comes
from the LEFT action, and the ELECTROWEAK comes from the RIGHT.

In terms of actions on Psi:
- Left SU(3): this is the L action -- corresponds to SU(3)_color
- Right U(2): this is the R action restricted to U(2) -- corresponds to SU(2)_L x U(1)_Y

This means:
- The FULL gauge group = SU(3)_L x U(2)_R = L_{su(3)} x R_{u(2)}
- The algebra A_F should be the commutant of this gauge action on H_F, with J.

But the L+R combined action (which is what Phase 1 used) is the
DIAGONAL u(2) acting via L+R -- this is NEITHER the left gauge
nor the right gauge, but a specific combination.

Let me test: commutant of L_{su(3)} + R_{u(2)} (the CORRECT gauge group).
"""

import numpy as np
from scipy.linalg import null_space, orth
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import (
    gell_mann_matrices, su3_basis, u2_basis_in_su3,
    L_action_matrix, R_action_matrix, LR_action_matrix,
)

np.set_printoptions(precision=6, linewidth=120, suppress=True)

# Setup
def get_column_index(flat_idx):
    if flat_idx == 0: return 0
    elif 1 <= flat_idx <= 3: return flat_idx
    elif 4 <= flat_idx <= 6: return 0
    else: return (flat_idx - 7) % 3 + 1

gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])
G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)

Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

basis_u2 = u2_basis_in_su3()
basis_su3 = su3_basis()

n = 32

def compute_full(label, gens_16):
    """Full pipeline: gauge commutant -> J-compat -> center -> Wedderburn."""
    print(f"\n{'='*70}")
    print(f"GAUGE: {label}")
    print(f"{'='*70}")

    # Build 32x32 generators
    rho_gens = []
    for g16 in gens_16:
        g_minus = G5 @ np.conj(g16) @ G5
        g32 = np.zeros((32, 32), dtype=complex)
        g32[:16, :16] = g16
        g32[16:, 16:] = g_minus
        rho_gens.append(g32)

    # Gauge commutant
    constraint_blocks = []
    for rv in rho_gens:
        block = np.zeros((n*n, n*n), dtype=complex)
        for i in range(n):
            for j in range(n):
                row = i*n + j
                for k in range(n):
                    block[row, i*n+k] += rv[k, j]
                    block[row, k*n+j] -= rv[i, k]
        constraint_blocks.append(block)

    A = np.vstack(constraint_blocks)
    ns = null_space(A, rcond=1e-10)
    d_gauge = ns.shape[1]
    print(f"  Gauge commutant complex dim: {d_gauge}")

    if d_gauge == 0:
        print(f"  Trivial!")
        return

    comm_basis = [ns[:, k].reshape(n, n) for k in range(d_gauge)]

    # J-constraint
    d = d_gauge
    A_mats = []
    B_mats = []
    for k in range(d):
        Tk = comm_basis[k]
        A_mats.append((Tk @ Xi - Xi @ np.conj(Tk)).flatten())
        B_mats.append((Tk @ Xi + Xi @ np.conj(Tk)).flatten())

    C_mat = np.zeros((2 * n * n, 2 * d))
    for m in range(n * n):
        for k in range(d):
            C_mat[2*m, k] = A_mats[k][m].real
            C_mat[2*m, d+k] = -B_mats[k][m].imag
            C_mat[2*m+1, k] = A_mats[k][m].imag
            C_mat[2*m+1, d+k] = B_mats[k][m].real

    ns_J = null_space(C_mat, rcond=1e-10)
    J_null_dim = ns_J.shape[1]

    Jbasis = []
    for idx in range(J_null_dim):
        coeffs = ns_J[:, idx]
        T = sum((coeffs[k] + 1j*coeffs[d+k]) * comm_basis[k] for k in range(d))
        Jbasis.append(T)

    # Real basis
    real_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in Jbasis]
    V = np.column_stack(real_vecs)
    Q = orth(V)
    d_orth = Q.shape[1]
    print(f"  J-compatible commutant real dim: {d_orth}")

    if d_orth == 0:
        return

    n_flat = n * n
    orth_basis = [(Q[:, k][:n_flat] + 1j * Q[:, k][n_flat:]).reshape(n, n) for k in range(d_orth)]

    # Closure
    struct_const = np.zeros((d_orth, d_orth, d_orth))
    max_resid = 0
    for i in range(d_orth):
        for j in range(d_orth):
            prod = orth_basis[i] @ orth_basis[j]
            pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
            coeffs = Q.T @ pv
            struct_const[i, j, :] = coeffs
            resid = np.linalg.norm(pv - Q @ coeffs)
            max_resid = max(max_resid, resid)
    print(f"  Closure: {max_resid:.2e}")

    # Center (real)
    comm_sc = struct_const - struct_const.transpose(1, 0, 2)
    center_rows = []
    for j in range(d_orth):
        for k in range(d_orth):
            center_rows.append(comm_sc[:, j, k])
    center_mat = np.array(center_rows)
    center_ns = null_space(center_mat, rcond=1e-8)
    center_dim = center_ns.shape[1]
    print(f"  Center dim: {center_dim}")
    print(f"  (A_F target: real dim 24, center dim 5)")

    # Quick Wedderburn via generic center element
    if center_dim > 0 and center_dim <= d_orth:
        center_basis = [sum(center_ns[i, idx] * orth_basis[i] for i in range(d_orth))
                       for idx in range(center_dim)]

        np.random.seed(42)
        rc = np.random.randn(center_dim)
        gc = sum(c * T for c, T in zip(rc, center_basis))

        evals, evecs = np.linalg.eig(gc)

        # Merge conjugate pairs
        tol = 1e-3
        used = np.zeros(32, dtype=bool)
        factors = []
        for i in range(32):
            if used[i]: continue
            ev = evals[i]
            close = np.abs(evals - ev) < tol
            close_conj = np.abs(evals - np.conj(ev)) < tol
            idx_set = np.where(close | close_conj)[0]
            for idx in idx_set: used[idx] = True
            V_ev = evecs[:, idx_set]

            proj_vecs = [np.concatenate([(V_ev.conj().T @ T @ V_ev).flatten().real,
                                         (V_ev.conj().T @ T @ V_ev).flatten().imag])
                        for T in orth_basis]
            P = np.column_stack(proj_vecs)
            fr = np.linalg.matrix_rank(P, tol=1e-6)

            ftype = f"dim_V={len(idx_set)}, alg_rank={fr}"
            # Identify
            for nn in range(1, 10):
                if fr == nn**2 and len(idx_set) == nn: ftype += f" = M_{nn}(R)"
                if fr == 2*nn**2 and len(idx_set) == nn: ftype += f" = M_{nn}(C)"
                if fr == 4*nn**2 and len(idx_set) == 2*nn: ftype += f" = M_{nn}(H)"
            if fr == 1 and len(idx_set) == 1: ftype += " = R"
            if fr == 2 and len(idx_set) == 2: ftype += " = C"
            if fr == 4 and len(idx_set) == 2: ftype += " = H"

            is_real = np.abs(ev.imag) < tol
            print(f"    Factor: {'REAL' if is_real else 'COMPLEX'} ev, {ftype}")
            factors.append((len(idx_set), fr))

        total_V = sum(f[0] for f in factors)
        total_A = sum(f[1] for f in factors)
        print(f"  Total: dim_V={total_V}, alg_dim={total_A}")

    return d_orth, center_dim

# ===================================================================
# Test different gauge groups
# ===================================================================

# (a) L_{su(3)} + R_{u(2)}: CORRECT gauge group from isometry analysis
print("\n*** TEST (a): L_{su(3)} + R_{u(2)} ***")
print("This should be the CORRECT gauge for recovering A_F")
gens_a = [L_action_matrix(v) for v in basis_su3]
# R restricted to u(2): need to embed u(2) into su(3) for R
# The R action uses the FULL su(3) basis, but restricted to u(2)
# The u(2) subalgebra of su(3) for R: same embedding phi_*(a) = diag(-tr(a), a)
for v in basis_u2:
    gens_a.append(R_action_matrix(v))
compute_full("L_{su(3)} + R_{u(2)}", gens_a)

# (b) L_{su(3)} only (no R at all)
print("\n*** TEST (b): L_{su(3)} only ***")
gens_b = [L_action_matrix(v) for v in basis_su3]
compute_full("L_{su(3)} only", gens_b)

# (c) R_{u(2)} only
print("\n*** TEST (c): R_{u(2)} only ***")
gens_c = [R_action_matrix(v) for v in basis_u2]
compute_full("R_{u(2)} only", gens_c)

# (d) L_{u(2)} only (L restricted to u(2))
print("\n*** TEST (d): L_{u(2)} only ***")
gens_d = [L_action_matrix(v) for v in basis_u2]
compute_full("L_{u(2)} only", gens_d)

# (e) L_{su(3)} + R_{su(3)} (both full)
print("\n*** TEST (e): L_{su(3)} + R_{su(3)} ***")
gens_e = [L_action_matrix(v) for v in basis_su3]
gens_e += [R_action_matrix(v) for v in basis_su3]
compute_full("L_{su(3)} + R_{su(3)}", gens_e)

print("\nDone.")
