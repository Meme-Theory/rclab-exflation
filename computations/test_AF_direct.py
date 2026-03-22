"""
TEST: Direct Connes A_F = C + H + M_3(C) construction on Baptista's H_F.

Tests whether Connes' finite algebra, constructed using the LEFT x RIGHT
tensor product action on the 4x4 internal matrix, lives inside the
R_{u(2)} J-compatible commutant and satisfies the order-zero condition.

The A_F representation on Psi_+ (4x4 internal matrix):
  pi(lambda, q, m) . Psi = L_{lambda,q} . Psi . R_m
where:
  L_{lambda,q} = diag(lambda, lambda-bar, q) [4x4, acts on row = weak isospin]
  R_m = diag(1, m) [4x4, acts on col = color]

Author: KK Theorist Agent
Date: 2026-02-12
"""

import numpy as np
from scipy.linalg import null_space, orth
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import (
    su3_basis, u2_basis_in_su3,
    L_action_matrix, R_action_matrix,
)

np.set_printoptions(precision=8, linewidth=130, suppress=True)

# ── Infrastructure from Phase 2a ──

particle_names_plus = [
    'nu_R', 'u_R^r', 'u_R^g', 'u_R^b',
    'e_R^-', 'nu_L', 'e_L^-',
    'd_R^r', 'd_R^g', 'd_R^b',
    'u_L^r', 'u_L^g', 'u_L^b',
    'd_L^r', 'd_L^g', 'd_L^b',
]

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

gamma_F = np.zeros((32, 32))
gamma_F[:16, :16] = np.eye(16)
gamma_F[16:, 16:] = -np.eye(16)

n = 32
basis_u2 = u2_basis_in_su3()

def rho_minus(rho_plus_v):
    return G5 @ np.conj(rho_plus_v) @ G5

def build_full_32(gens_16):
    gens_32 = []
    for g16 in gens_16:
        g32 = np.zeros((32, 32), dtype=complex)
        g32[:16, :16] = g16
        g32[16:, 16:] = rho_minus(g16)
        gens_32.append(g32)
    return gens_32

# R_{u(2)} generators
R_u2_gens_16 = [R_action_matrix(v) for v in basis_u2]
R_u2_gens_32 = build_full_32(R_u2_gens_16)

# ── Flat index mapping (Baptista convention) ──
# Psi_+ as 4x4 matrix:
#   (0,0)=0:nu_R   (0,1)=1:u_R^r  (0,2)=2:u_R^g  (0,3)=3:u_R^b
#   (1,0)=4:e_R    (1,1)=7:d_R^r  (1,2)=8:d_R^g  (1,3)=9:d_R^b
#   (2,0)=5:nu_L   (2,1)=10:u_L^r (2,2)=11:u_L^g (2,3)=12:u_L^b
#   (3,0)=6:e_L    (3,1)=13:d_L^r (3,2)=14:d_L^g (3,3)=15:d_L^b

def flat_idx(row, col):
    """Convert 4x4 matrix index (row, col) to Baptista flat 16-index."""
    if row == 0 and col == 0: return 0
    if row == 0: return col
    if col == 0: return row + 3
    return 7 + 3 * (row - 1) + (col - 1)

def build_pi_16(L4, R4):
    """Build 16x16 representation matrix from 4x4 left and right actions.

    pi(a).Psi = L4 . Psi . R4, so pi_{flat(i,j), flat(k,l)} = L4[i,k] * R4[l,j].
    """
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L4[i, k] * R4[l, j]
    return gen


# ── Build the 24 A_F generators ──

print("=" * 72)
print("DIRECT A_F CONSTRUCTION: C + H + M_3(C) on H_F = C^32")
print("=" * 72)

AF_gens_16 = []
AF_names = []

# --- C FACTOR (2 real dims: Re(lambda), Im(lambda)) ---
# L = diag(lambda, lambda-bar, lambda, lambda-bar) [embedding C -> H on rows 2-3]
# R = I_4
# Re: lambda=1 -> L=I_4 (=identity)
# Im: lambda=i -> L=diag(i, -i, i, -i)

L_C_Re = np.eye(4, dtype=complex)
AF_gens_16.append(build_pi_16(L_C_Re, np.eye(4, dtype=complex)))
AF_names.append('C_Re=I')

L_C_Im = np.diag([1j, -1j, 1j, -1j])
AF_gens_16.append(build_pi_16(L_C_Im, np.eye(4, dtype=complex)))
AF_names.append('C_Im')

# --- H FACTOR (4 real dims: 1, i, j, k quaternion basis) ---
# L = diag(q_+, q_-, q) where q_+ = q_0 + i*q_1, q_- = q_0 - i*q_1,
#   and q = [[q_0+iq_1, q_2+iq_3], [-q_2+iq_3, q_0-iq_1]]
# R = I_4

# q=1: L = I_4 (same as C_Re, redundant)
AF_gens_16.append(build_pi_16(np.eye(4, dtype=complex), np.eye(4, dtype=complex)))
AF_names.append('H_1=I')

# q=i: q_0=0, q_1=1 -> q_+=i, q_-=-i, q=diag(i,-i)
L_H_i = np.diag([1j, -1j, 1j, -1j])
AF_gens_16.append(build_pi_16(L_H_i, np.eye(4, dtype=complex)))
AF_names.append('H_i')  # same as C_Im

# q=j: q_0=0, q_2=1 -> q_+=0, q_-=0, q=[[0,1],[-1,0]]
L_H_j = np.zeros((4, 4), dtype=complex)
L_H_j[0, 0] = 0  # q_+ = 0
L_H_j[1, 1] = 0  # q_- = 0
L_H_j[2, 3] = 1.0   # q_12 = q_2 + i*q_3 = 1
L_H_j[3, 2] = -1.0   # q_21 = -q_2 + i*q_3 = -1
AF_gens_16.append(build_pi_16(L_H_j, np.eye(4, dtype=complex)))
AF_names.append('H_j')

# q=k: q_0=0, q_3=1 -> q_+=0, q_-=0, q=[[0,i],[i,0]]
L_H_k = np.zeros((4, 4), dtype=complex)
L_H_k[2, 3] = 1j   # q_12 = i
L_H_k[3, 2] = 1j    # q_21 = i
AF_gens_16.append(build_pi_16(L_H_k, np.eye(4, dtype=complex)))
AF_names.append('H_k')

# --- M_3(C) FACTOR (18 real dims: Re and Im of 9 E_{ab} entries) ---
# L = I_4, R = diag(1, m) where m is 3x3 color matrix
# For E_{ab} generator: m has 1 (or i) at position (a,b), zeros elsewhere.
# R = diag(1, E_{ab}) -> R[0,0]=1, R[a+1,b+1] = value

for a in range(3):
    for b in range(3):
        for part, val in [('Re', 1.0), ('Im', 1j)]:
            R_m = np.zeros((4, 4), dtype=complex)
            R_m[0, 0] = 1.0  # lepton column: unchanged
            R_m[a + 1, b + 1] = val
            AF_gens_16.append(build_pi_16(np.eye(4, dtype=complex), R_m))
            AF_names.append(f'M3_E{a}{b}_{part}')

# Remove duplicates (C_Re = H_1 = I, H_i = C_Im, M3_E00_Re+E11_Re+E22_Re includes I)
# For now keep all and measure the independent rank.

print(f"\n  Total generators: {len(AF_gens_16)}")

# Extend to C^32 via J
AF_gens_32 = build_full_32(AF_gens_16)

# ── Test 1: Verify the pi formula by checking L action ──
print("\n[TEST 1] Verify build_pi_16 against known L action")
# L_v(Psi) = v * Psi for su(3) LEFT action.
# This is the special case L = v, R = I_4 (ignoring the subtleties of Baptista's L
# which has the anomalous (2v_11*I + v) term on b).
# Actually, our build_pi_16 formula gives L.Psi.R (ordinary matrix multiplication).
# Baptista's L action is NOT ordinary left multiplication! It has the anomaly term.
# So build_pi_16(v, I) != L_action_matrix(v).
# Let's just verify that build_pi_16(I, I) = I_{16}.
test_id = build_pi_16(np.eye(4, dtype=complex), np.eye(4, dtype=complex))
print(f"  pi(I, I) = I_16: {np.max(np.abs(test_id - np.eye(16))):.2e}")

# ── Test 2: Independence and dimension ──
print("\n[TEST 2] Real dimension of A_F generator span")
AF_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in AF_gens_32]
AF_mat = np.column_stack(AF_vecs)
AF_rank = np.linalg.matrix_rank(AF_mat, tol=1e-8)
print(f"  Rank: {AF_rank} (target: 24)")

# ── Test 3: In R_{u(2)} commutant? ──
print("\n[TEST 3] A_F generators in R_u(2) commutant?")
for idx, (T, name) in enumerate(zip(AF_gens_32, AF_names)):
    max_err = max(np.max(np.abs(T @ R_g - R_g @ T)) for R_g in R_u2_gens_32)
    if max_err > 1e-8:
        print(f"  FAIL: {name}: max [T, R_g] = {max_err:.6f}")

n_pass = sum(1 for T in AF_gens_32
             if all(np.max(np.abs(T @ R_g - R_g @ T)) < 1e-8 for R_g in R_u2_gens_32))
print(f"  PASS: {n_pass} / {len(AF_gens_32)}")

# ── Test 4: J-compatible? ──
print("\n[TEST 4] A_F generators J-compatible? (T Xi = Xi conj(T))")
for idx, (T, name) in enumerate(zip(AF_gens_32, AF_names)):
    err = np.max(np.abs(T @ Xi - Xi @ np.conj(T)))
    if err > 1e-8:
        print(f"  FAIL: {name}: max error = {err:.6f}")

n_pass_J = sum(1 for T in AF_gens_32
               if np.max(np.abs(T @ Xi - Xi @ np.conj(T))) < 1e-8)
print(f"  PASS: {n_pass_J} / {len(AF_gens_32)}")

# ── Test 5: Quaternion relations ──
print("\n[TEST 5] Quaternion relations")
Hi = AF_gens_32[AF_names.index('H_i')]
Hj = AF_gens_32[AF_names.index('H_j')]
Hk = AF_gens_32[AF_names.index('H_k')]
H1 = AF_gens_32[AF_names.index('H_1=I')]

for name, prod, exp in [
    ('i^2=-1', Hi@Hi, -H1), ('j^2=-1', Hj@Hj, -H1), ('k^2=-1', Hk@Hk, -H1),
    ('ij=k', Hi@Hj, Hk), ('jk=i', Hj@Hk, Hi), ('ki=j', Hk@Hi, Hj),
]:
    err = np.max(np.abs(prod - exp))
    print(f"  {name}: {'PASS' if err < 1e-10 else 'FAIL'} (err={err:.2e})")

# ── Test 6: Order-zero ──
print("\n[TEST 6] Order-zero condition [a, Xi b^T Xi] = 0")
max_oz = 0
n_viol = 0
worst_pair = ('', '', 0)
for i, (Ti, ni) in enumerate(zip(AF_gens_32, AF_names)):
    for j, (Tj, nj) in enumerate(zip(AF_gens_32, AF_names)):
        b_opp = Xi @ Tj.T @ Xi
        comm = Ti @ b_opp - b_opp @ Ti
        err = np.max(np.abs(comm))
        if err > max_oz:
            max_oz = err
            worst_pair = (ni, nj, err)
        if err > 1e-6:
            n_viol += 1

print(f"  Max |[a, o(b)]|: {max_oz:.6f}")
print(f"  Violations: {n_viol} / {len(AF_gens_32)**2}")
if max_oz > 1e-6:
    print(f"  Worst pair: [{worst_pair[0]}, o({worst_pair[1]})] = {worst_pair[2]:.6f}")

    # Detailed breakdown by factor pair
    print("\n  By factor combination:")
    C_idx = [i for i, n in enumerate(AF_names) if n.startswith('C_')]
    H_idx = [i for i, n in enumerate(AF_names) if n.startswith('H_')]
    M_idx = [i for i, n in enumerate(AF_names) if n.startswith('M3_')]

    for label_a, idx_a in [('C', C_idx), ('H', H_idx), ('M3', M_idx)]:
        for label_b, idx_b in [('C', C_idx), ('H', H_idx), ('M3', M_idx)]:
            max_err_pair = 0
            for i in idx_a:
                for j in idx_b:
                    b_opp = Xi @ AF_gens_32[j].T @ Xi
                    comm = AF_gens_32[i] @ b_opp - b_opp @ AF_gens_32[i]
                    err = np.max(np.abs(comm))
                    max_err_pair = max(max_err_pair, err)
            s = 'PASS' if max_err_pair < 1e-6 else f'{max_err_pair:.4f}'
            print(f"    [{label_a}, o({label_b})]: {s}")


# ── Test 7: Algebra closure ──
print("\n[TEST 7] Algebraic closure dimension")
# Remove redundant identity copies, keep only independent generators
unique_idx = []
seen_vecs = []
for i, T in enumerate(AF_gens_32):
    v = np.concatenate([T.flatten().real, T.flatten().imag])
    if not seen_vecs:
        unique_idx.append(i)
        seen_vecs.append(v)
    else:
        M = np.column_stack(seen_vecs)
        coeffs = np.linalg.lstsq(M, v, rcond=None)[0]
        resid = np.linalg.norm(v - M @ coeffs)
        if resid > 1e-8:
            unique_idx.append(i)
            seen_vecs.append(v)

print(f"  Independent generators: {len(unique_idx)} / {len(AF_gens_32)}")
print(f"  Independent names: {[AF_names[i] for i in unique_idx]}")

# Check if products of generators stay in the span
gen_mats = [AF_gens_32[i] for i in unique_idx]
gen_vecs = np.column_stack([np.concatenate([T.flatten().real, T.flatten().imag])
                            for T in gen_mats])
Q_gens = orth(gen_vecs)
d_gens = Q_gens.shape[1]

max_prod_resid = 0
for T1 in gen_mats:
    for T2 in gen_mats:
        prod = T1 @ T2
        pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
        coeffs = Q_gens.T @ pv
        resid = np.linalg.norm(pv - Q_gens @ coeffs)
        max_prod_resid = max(max_prod_resid, resid)

print(f"  Product closure: max residual = {max_prod_resid:.2e} "
      f"({'CLOSED' if max_prod_resid < 1e-6 else 'OPEN'})")

if max_prod_resid > 1e-6:
    # Compute full algebraic closure
    print("  Computing algebraic closure...")
    n_flat = 32 * 32
    current = list(gen_mats)
    cur_vecs = [np.concatenate([T.flatten().real, T.flatten().imag]) for T in current]
    Q_cur = orth(np.column_stack(cur_vecs))
    d_cur = Q_cur.shape[1]

    for iteration in range(10):
        cur_basis = [(Q_cur[:, k][:n_flat] + 1j * Q_cur[:, k][n_flat:]).reshape(32, 32)
                     for k in range(d_cur)]
        new_vecs = []
        for T1 in cur_basis:
            for T2 in gen_mats:
                prod = T1 @ T2
                pv = np.concatenate([prod.flatten().real, prod.flatten().imag])
                coeffs = Q_cur.T @ pv
                resid = np.linalg.norm(pv - Q_cur @ coeffs)
                if resid > 1e-8:
                    new_vecs.append(pv)
        if not new_vecs:
            break
        all_v = np.column_stack([Q_cur] + [np.column_stack(new_vecs)])
        Q_new = orth(all_v)
        d_new = Q_new.shape[1]
        if d_new == d_cur:
            break
        print(f"    Iteration {iteration+1}: dim {d_cur} -> {d_new}")
        Q_cur = Q_new
        d_cur = d_new

    print(f"  Algebraic closure dimension: {d_cur}")


# ── Summary ──
print("\n" + "=" * 72)
print("SUMMARY")
print("=" * 72)
print(f"  Independent dimension: {AF_rank} (target: 24)")
print(f"  In R_u(2) commutant: {n_pass}/{len(AF_gens_32)}")
print(f"  J-compatible: {n_pass_J}/{len(AF_gens_32)}")
print(f"  Order-zero max: {max_oz:.6f}")
print(f"  Order-zero violations: {n_viol}/{len(AF_gens_32)**2}")
print("=" * 72)
