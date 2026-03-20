"""Test non-degenerate Yukawa D_F with corrected (flipped) chirality grading."""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from branching_computation import su3_basis, u2_basis_in_su3, L_action_matrix, R_action_matrix

def get_column_index(flat_idx):
    if flat_idx == 0: return 0
    elif 1 <= flat_idx <= 3: return flat_idx
    elif 4 <= flat_idx <= 6: return 0
    else: return (flat_idx - 7) % 3 + 1

def get_row_index(flat_idx):
    if flat_idx == 0: return 0
    elif 1 <= flat_idx <= 3: return 0
    elif 4 <= flat_idx <= 6: return flat_idx - 3
    else: return (flat_idx - 7) // 3 + 1

def flat_idx(row, col):
    if row == 0 and col == 0: return 0
    if row == 0: return col
    if col == 0: return row + 3
    return 7 + 3 * (row - 1) + (col - 1)

gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])
G5_signs = np.array([-gamma5_diag[get_column_index(k)] for k in range(16)])
G5 = np.diag(G5_signs)
Xi = np.zeros((32, 32))
Xi[:16, 16:] = -G5
Xi[16:, :16] = -G5

# Chirality grading (rows 0-1 = RH = +1, rows 2-3 = LH = -1)
chirality_16 = np.zeros(16)
for k in range(16):
    row = get_row_index(k)
    chirality_16[k] = 1.0 if row <= 1 else -1.0

# Flipped: +chirality on Psi_+, -chirality on Psi_-
gamma_F_flip = np.diag(np.concatenate([chirality_16, -chirality_16]))

def rho_minus(rho_plus_v):
    return G5 @ np.conj(rho_plus_v) @ G5

def build_full_32(gen_16):
    g32 = np.zeros((32, 32), dtype=complex)
    g32[:16, :16] = gen_16
    g32[16:, 16:] = rho_minus(gen_16)
    return g32

def build_bimodule_16(L4, R4):
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L4[i, k] * R4[l, j]
    return gen

# Non-degenerate Yukawa: different for leptons vs quarks
y_nu = 0.1
y_e = 0.5
y_u = 1.0
y_d = 0.3

D_nondeg_16 = np.zeros((16, 16), dtype=complex)
for col in range(4):
    y_up = y_nu if col == 0 else y_u
    y_dn = y_e if col == 0 else y_d
    i02 = flat_idx(0, col)
    i20 = flat_idx(2, col)
    D_nondeg_16[i02, i20] = y_up
    D_nondeg_16[i20, i02] = y_up
    i13 = flat_idx(1, col)
    i31 = flat_idx(3, col)
    D_nondeg_16[i13, i31] = y_dn
    D_nondeg_16[i31, i13] = y_dn

print("Non-degenerate Yukawa D_F built.")
print(f"D_F Hermitian: {np.allclose(D_nondeg_16, D_nondeg_16.conj().T)}")

chirality_diag = np.diag(chirality_16)
ac = np.max(np.abs(D_nondeg_16 @ chirality_diag + chirality_diag @ D_nondeg_16))
print(f"D_F anticommutes with chirality_16: {ac:.2e}")

DF32 = np.zeros((32, 32), dtype=complex)
DF32[:16, :16] = D_nondeg_16
DF32[16:, 16:] = rho_minus(D_nondeg_16)

ac32 = np.max(np.abs(DF32 @ gamma_F_flip + gamma_F_flip @ DF32))
jc = np.max(np.abs(DF32 @ Xi - Xi @ np.conj(DF32)))
print(f"D_F_32 anticommutes with gamma_F_flip: {ac32:.2e}")
print(f"D_F_32 J-compatible: {jc:.2e}")

# Build A_F generators
AF_gens_16 = []
AF_names = []
AF_factor = []

L_CIm = np.diag([1j, -1j, 1.0, 1.0])
AF_gens_16.append(build_bimodule_16(L_CIm, np.eye(4, dtype=complex)))
AF_names.append("C_Im"); AF_factor.append("C")
L_CRe = np.diag([1.0, -1.0, 0.0, 0.0])
AF_gens_16.append(build_bimodule_16(L_CRe, np.eye(4, dtype=complex)))
AF_names.append("C_Re"); AF_factor.append("C")
L_Hi = np.diag([0.0, 0.0, 1j, -1j])
AF_gens_16.append(build_bimodule_16(L_Hi, np.eye(4, dtype=complex)))
AF_names.append("H_i"); AF_factor.append("H")
L_Hj = np.zeros((4, 4), dtype=complex); L_Hj[2, 3] = 1.0; L_Hj[3, 2] = -1.0
AF_gens_16.append(build_bimodule_16(L_Hj, np.eye(4, dtype=complex)))
AF_names.append("H_j"); AF_factor.append("H")
L_Hk = np.zeros((4, 4), dtype=complex); L_Hk[2, 3] = 1j; L_Hk[3, 2] = 1j
AF_gens_16.append(build_bimodule_16(L_Hk, np.eye(4, dtype=complex)))
AF_names.append("H_k"); AF_factor.append("H")
AF_gens_16.append(build_bimodule_16(np.eye(4, dtype=complex), np.eye(4, dtype=complex)))
AF_names.append("H_1=I"); AF_factor.append("H")
for a in range(3):
    for b in range(3):
        for part, val in [("Re", 1.0), ("Im", 1j)]:
            m_elem = np.zeros((3, 3), dtype=complex)
            m_elem[a, b] = val
            m_dag = m_elem.conj().T
            R_m = np.eye(4, dtype=complex)
            R_m[1:, 1:] = m_dag
            AF_gens_16.append(build_bimodule_16(np.eye(4, dtype=complex), R_m))
            AF_names.append(f"M3_E{a}{b}_{part}"); AF_factor.append("M3")

AF_gens_32 = [build_full_32(g) for g in AF_gens_16]

# Order-one test
n_gens = len(AF_gens_32)
o1_by_factor = {}
n_viol = 0
max_o1 = 0
max_pair = None
for i in range(n_gens):
    Da = DF32 @ AF_gens_32[i] - AF_gens_32[i] @ DF32
    for j in range(n_gens):
        ob = Xi @ AF_gens_32[j].T @ Xi
        dc = Da @ ob - ob @ Da
        err = np.max(np.abs(dc))
        if err > max_o1:
            max_o1 = err
            max_pair = (AF_names[i], AF_names[j])
        if err > 1e-6:
            n_viol += 1
        pk = f"[{AF_factor[i]}, o({AF_factor[j]})]"
        o1_by_factor[pk] = max(o1_by_factor.get(pk, 0), err)

print(f"\nOrder-one with non-degenerate Yukawa (y_nu={y_nu}, y_e={y_e}, y_u={y_u}, y_d={y_d}):")
print(f"  Max error: {max_o1:.6e}")
if max_pair:
    print(f"  Worst pair: {max_pair}")
print(f"  Violations: {n_viol}/{n_gens**2}")
for pk in sorted(o1_by_factor.keys()):
    v = o1_by_factor[pk]
    st = "PASS" if v < 1e-8 else f"FAIL ({v:.6e})"
    print(f"  {pk}: {st}")

# Also try: degenerate up/down but different lepton/quark
print("\n--- Degenerate Yukawa (y=1 everywhere) ---")
D_deg_16 = np.zeros((16, 16), dtype=complex)
for col in range(4):
    i02 = flat_idx(0, col)
    i20 = flat_idx(2, col)
    D_deg_16[i02, i20] = 1.0
    D_deg_16[i20, i02] = 1.0
    i13 = flat_idx(1, col)
    i31 = flat_idx(3, col)
    D_deg_16[i13, i31] = 1.0
    D_deg_16[i31, i13] = 1.0

DF32_deg = np.zeros((32, 32), dtype=complex)
DF32_deg[:16, :16] = D_deg_16
DF32_deg[16:, 16:] = rho_minus(D_deg_16)

o1_by_factor2 = {}
for i in range(n_gens):
    Da = DF32_deg @ AF_gens_32[i] - AF_gens_32[i] @ DF32_deg
    for j in range(n_gens):
        ob = Xi @ AF_gens_32[j].T @ Xi
        dc = Da @ ob - ob @ Da
        err = np.max(np.abs(dc))
        pk = f"[{AF_factor[i]}, o({AF_factor[j]})]"
        o1_by_factor2[pk] = max(o1_by_factor2.get(pk, 0), err)

for pk in sorted(o1_by_factor2.keys()):
    v = o1_by_factor2[pk]
    st = "PASS" if v < 1e-8 else f"FAIL ({v:.6e})"
    print(f"  {pk}: {st}")

# Critical test: Connes' EXACT D_F structure
# In Connes, D_F on one generation acts as:
# D_F |nu_R> = k_nu |nu_L>,  D_F |e_R> = k_e |e_L>
# D_F |u_R^c> = k_u |u_L^c>,  D_F |d_R^c> = k_d |d_L^c>
# Plus: Majorana mass M_R: |nu_R> <-> |nu_R^c>
# The Majorana term couples ACROSS Psi_+/Psi_- and is off-diagonal in the original gamma_F

print("\n--- With Majorana mass (off-diagonal in Psi+/Psi-) ---")
M_R = 10.0  # Majorana mass scale
# nu_R is at flat_idx(0,0) = 0 in Psi_+
# nu_R^c is at some position in Psi_- ... specifically, hat{Xi} maps nu_R to nu_L_bar
# In Psi_-, the particle at position matching nu_R in Psi_+ is nu_L_bar
# The Majorana term couples nu_R (Psi_+, idx 0) to ...
# Actually in Connes' framework, the Majorana mass is:
# D_F(nu_R, nu_R^bar) = M_R, which goes Psi_+ -> Psi_-

# For our flipped gamma_F:
# nu_R is in Psi_+ row 0 -> chirality +1
# nu_R^bar is in Psi_- ... what row?
# hat{Xi} maps (row 0, col 0) in Psi_+ to some position in Psi_-
# From Xi structure: Xi[:16, 16:] = -G5, so Xi maps Psi_- index k to Psi_+ index k' via -G5
# Actually Xi(Psi_+[0]) = Xi[0, 16:] = -G5[0, :]
# G5 is diagonal with signs based on column index
# For flat 0: col=0, gamma5_diag[0]=1, G5_signs[0] = -1
# So G5[0,0] = -1, and Xi[0, 16] = -G5[0,0] = 1
# Meaning Xi maps Psi_-[0] to Psi_+[0] with coefficient 1
# So nu_R (Psi_+[0]) is mapped by Xi to Psi_-[0]
# Psi_-[0] corresponds to nu_L_bar (the antiparticle of the LH neutrino)

# The Majorana mass couples Psi_+[0] <-> Psi_-[0]
DF32_maj = DF32.copy()
DF32_maj[0, 16] += M_R  # Psi_+[0] -> Psi_-[0]
DF32_maj[16, 0] += M_R  # Hermitian conjugate

# Check properties
herm = np.max(np.abs(DF32_maj - DF32_maj.conj().T))
ac_maj = np.max(np.abs(DF32_maj @ gamma_F_flip + gamma_F_flip @ DF32_maj))
jc_maj = np.max(np.abs(DF32_maj @ Xi - Xi @ np.conj(DF32_maj)))
print(f"  Hermitian: {herm:.2e}")
print(f"  anticommutes with gamma_F_flip: {ac_maj:.2e}")
print(f"  J-compatible: {jc_maj:.2e}")

# gamma_F_flip[0,0] = +1 (RH), gamma_F_flip[16,16] = -chirality_16[0] = -1
# So D_F[0,16] couples +1 to -1: this SHOULD anticommute
# D_F gamma_F: D_F[0,16] * gamma_F[16,16] = M_R * (-1) = -M_R
# gamma_F D_F: gamma_F[0,0] * D_F[0,16] = (+1) * M_R = +M_R
# Sum = 0. Good, anticommutes for this entry.
# For the conjugate: D_F[16,0] * gamma_F[0,0] = M_R * (+1) = +M_R
# gamma_F[16,16] * D_F[16,0] = (-1) * M_R = -M_R
# Sum = 0. Good.

if ac_maj < 1e-8:
    print("  Majorana term is compatible with gamma_F_flip!")
    # Test order-one
    o1_by_factor3 = {}
    for i in range(n_gens):
        Da = DF32_maj @ AF_gens_32[i] - AF_gens_32[i] @ DF32_maj
        for j in range(n_gens):
            ob = Xi @ AF_gens_32[j].T @ Xi
            dc = Da @ ob - ob @ Da
            err = np.max(np.abs(dc))
            pk = f"[{AF_factor[i]}, o({AF_factor[j]})]"
            o1_by_factor3[pk] = max(o1_by_factor3.get(pk, 0), err)

    for pk in sorted(o1_by_factor3.keys()):
        v = o1_by_factor3[pk]
        st = "PASS" if v < 1e-8 else f"FAIL ({v:.6e})"
        print(f"  {pk}: {st}")
