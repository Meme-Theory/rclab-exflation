"""
S21C-GB-DEBUG6: Brute-force Gauss-Bonnet via double-epsilon contraction.

Rerun of computations/session-21/s21c_gb_debug6.py with canonical constants import
and local-variable tagging (S81 T3 form).

Goal: verify chi(SU(3)) = 0 via direct Levi-Civita contraction
    S = eps_A * eps_B * R_{A1 B1} * R_{A2 B2} * R_{A3 B3} * R_{A4 B4}
on analytic SU(3), U(1)xSU(2), S^4, S^8 plus the stored Riemann tensor at tau=0.

Canonical direction: Poincare-Hopf asserts chi(G) = 0 for any compact Lie group
of rank r >= 1 (nonvanishing vector field exists via left-invariant generators).
SU(3) has rank 2, so chi(SU(3)) = 0. The double-epsilon integrand S(SU(3))
must therefore vanish to machine epsilon (integrand is pointwise zero for
left-invariant curvature on a constant-curvature Lie group of nonzero rank).
"""

import sys
sys.path.insert(0, r'C:\sandbox\Ainulindale Exflation\computations')

from canonical_constants import PI  # canonical pi
import numpy as np

# -------------------------------------------------------------------
# Levi-Civita symbol builder
# -------------------------------------------------------------------
def levi_civita(n):
    """Build the n-dimensional Levi-Civita symbol as a numpy array."""
    from itertools import permutations
    eps = np.zeros([n] * n, dtype=np.float64)  # (local)
    identity = list(range(n))  # (local)
    for perm in permutations(identity):
        sign = 1  # (local)
        perm_list = list(perm)  # (local)
        for i in range(n):
            for j in range(i + 1, n):
                if perm_list[i] > perm_list[j]:
                    sign *= -1
        eps[tuple(perm)] = sign
    return eps


print("=" * 70)
print("S21C-GB-DEBUG6: BRUTE FORCE EULER DENSITY VIA EPSILON")
print("=" * 70)

eps4 = levi_civita(4)  # (local)
print(f"4D Levi-Civita built: shape {eps4.shape}")

# -------------------------------------------------------------------
# 4D: S^4 (chi = 2)
# -------------------------------------------------------------------
print("\n--- 4D: S^4 ---")
R_S4 = np.zeros((4, 4, 4, 4))  # (local)
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                R_S4[a, b, c, d] = float(a == c) * float(b == d) - float(a == d) * float(b == c)

# Correct pairing: factor k = R[a_{2k-1},a_{2k},b_{2k-1},b_{2k}]
S_S4 = np.einsum('pqrs,wxyz,pqwx,rsyz', eps4, eps4, R_S4, R_S4)  # (local)
chi_S4 = S_S4 / 48.0  # (local)
print(f"S(S^4) = {S_S4:.6f}, chi via S/48 = {chi_S4:.6f} (expected 2)")

# -------------------------------------------------------------------
# 4D: U(1) x SU(2) (chi = 0)
# -------------------------------------------------------------------
print("\n--- 4D: U(1) x SU(2) ---")
R_U2 = np.zeros((4, 4, 4, 4))  # (local)
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            for ll in range(1, 4):
                R_U2[i, j, k, ll] = (1.0 / 8.0) * (
                    float(i == k) * float(j == ll) - float(i == ll) * float(j == k)
                )
S_U2 = np.einsum('pqrs,wxyz,pqwx,rsyz', eps4, eps4, R_U2, R_U2)  # (local)
print(f"S(U(1)xSU(2)) = {S_U2:.10e} (expected 0)")

# -------------------------------------------------------------------
# 8D: Analytic SU(3)
# -------------------------------------------------------------------
print("\n--- 8D: Analytic SU(3) ---")
f = np.zeros((8, 8, 8))  # (local)
f_values = {  # (local)
    (0, 1, 2): 1.0,
    (0, 3, 6): 0.5,
    (0, 4, 5): -0.5,
    (1, 3, 5): 0.5,
    (1, 4, 6): 0.5,
    (2, 3, 4): 0.5,
    (2, 5, 6): -0.5,
    (3, 4, 7): np.sqrt(3) / 2,
    (5, 6, 7): np.sqrt(3) / 2,
}
for (a, b, c), val in f_values.items():
    f[a, b, c] = val
    f[b, c, a] = val
    f[c, a, b] = val
    f[a, c, b] = -val
    f[b, a, c] = -val
    f[c, b, a] = -val

# R_{abcd} = (1/12) f_{abe} f_{cde}  (Killing normalization, our sign convention)
R_SU3 = (1.0 / 12.0) * np.einsum('abe,cde->abcd', f, f)  # (local)

print("Building 8D Levi-Civita symbol...")
eps8 = levi_civita(8)  # (local)
print(f"8D Levi-Civita built: shape {eps8.shape}")

# Stepwise contraction (memory safe)
print("Step 1: contract eps8 with first R factor...")
T1 = np.einsum('abcdefgh,abij->cdefghij', eps8, R_SU3)  # (local)
print(f"  T1 max |.|: {np.max(np.abs(T1)):.6e}")
print("Step 2...")
T2 = np.einsum('cdefghij,cdkl->efghijkl', T1, R_SU3)  # (local)
del T1
print(f"  T2 max |.|: {np.max(np.abs(T2)):.6e}")
print("Step 3...")
T3 = np.einsum('efghijkl,efmn->ghijklmn', T2, R_SU3)  # (local)
del T2
print(f"  T3 max |.|: {np.max(np.abs(T3)):.6e}")
print("Step 4...")
T4 = np.einsum('ghijklmn,ghop->ijklmnop', T3, R_SU3)  # (local)
del T3
print(f"  T4 max |.|: {np.max(np.abs(T4)):.6e}")
print("Step 5: full contraction with second epsilon...")
S_SU3 = np.einsum('ijklmnop,ijklmnop', eps8, T4)  # (local)
del T4
S_SU3_over_6144 = S_SU3 / 6144.0  # (local)
print(f"S(SU(3)) = {S_SU3:.15e}, S/6144 = {S_SU3_over_6144:.15e} (expected 0)")

# -------------------------------------------------------------------
# 8D: S^8 cross-check
# -------------------------------------------------------------------
print("\n--- 8D: S^8 ---")
R_S8 = np.zeros((8, 8, 8, 8))  # (local)
for a in range(8):
    for b in range(8):
        for c in range(8):
            for dd in range(8):
                R_S8[a, b, c, dd] = float(a == c) * float(b == dd) - float(a == dd) * float(b == c)

T1 = np.einsum('abcdefgh,abij->cdefghij', eps8, R_S8)  # (local)
T2 = np.einsum('cdefghij,cdkl->efghijkl', T1, R_S8)  # (local)
del T1
T3 = np.einsum('efghijkl,efmn->ghijklmn', T2, R_S8)  # (local)
del T2
T4 = np.einsum('ghijklmn,ghop->ijklmnop', T3, R_S8)  # (local)
del T3
S_S8 = np.einsum('ijklmnop,ijklmnop', eps8, T4)  # (local)
del T4

# Vol(S^8 unit) = 32 pi^4 / 105; chi = S / (6144 (2pi)^4) * Vol
vol_S8 = 32.0 * PI**4 / 105.0  # (local)
chi_S8 = S_S8 / (6144.0 * (2.0 * PI) ** 4) * vol_S8  # (local)
print(f"S(S^8) = {S_S8:.6f}, S/6144 = {S_S8/6144.0:.6f} (expected 105)")
print(f"chi(S^8) via formula = {chi_S8:.6f} (expected 2)")

# -------------------------------------------------------------------
# 8D: stored Riemann at tau=0
# -------------------------------------------------------------------
print("\n--- 8D: stored R at tau=0 ---")
stored_path = r'C:\sandbox\Ainulindale Exflation\computations/_shared\r20a_riemann_tensor.npz'  # (local)
d = np.load(stored_path, allow_pickle=True)  # (local)
R_stored = d['R_abcd'][0]  # (local)

T1 = np.einsum('abcdefgh,abij->cdefghij', eps8, R_stored)  # (local)
T2 = np.einsum('cdefghij,cdkl->efghijkl', T1, R_stored)  # (local)
del T1
T3 = np.einsum('efghijkl,efmn->ghijklmn', T2, R_stored)  # (local)
del T2
T4 = np.einsum('ghijklmn,ghop->ijklmnop', T3, R_stored)  # (local)
del T3
S_stored = np.einsum('ijklmnop,ijklmnop', eps8, T4)  # (local)
del T4
print(f"S(stored, tau=0) = {S_stored:.15e}, S/6144 = {S_stored/6144.0:.15e}")

# -------------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------------
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"S(S^4)                 = {S_S4:.6f}  (chi={chi_S4:.6f}, exp 2)")
print(f"S(U(1)xSU(2))          = {S_U2:.10e}  (exp 0)")
print(f"S(SU(3), analytic)     = {S_SU3:.15e}  (exp 0)")
print(f"S(SU(3), stored)       = {S_stored:.15e}  (exp 0)")
print(f"S(S^8)                 = {S_S8:.6f}  (chi={chi_S8:.6f}, exp 2)")

# Machine-epsilon gate for SU(3) entries
eps_machine = 1e-8  # (local) gate threshold for chi(SU(3))=0 detection
su3_analytic_ok = abs(S_SU3 / 6144.0) < eps_machine  # (local)
su3_stored_ok = abs(S_stored / 6144.0) < eps_machine  # (local)
print(f"\nchi(SU(3)) = 0 gate (|S/6144| < {eps_machine}):")
print(f"  analytic SU(3): {'PASS' if su3_analytic_ok else 'FAIL'}  |S/6144|={abs(S_SU3)/6144.0:.3e}")
print(f"  stored SU(3):   {'PASS' if su3_stored_ok else 'FAIL'}  |S/6144|={abs(S_stored)/6144.0:.3e}")

# Cross-check: S^4 chi, S^8 chi
s4_ok = abs(chi_S4 - 2.0) < 1e-6  # (local)
s8_ok = abs(chi_S8 - 2.0) < 1e-4  # (local)
u2_ok = abs(S_U2) < 1e-8  # (local)
print(f"\nCross-checks:")
print(f"  chi(S^4)=2:      {'PASS' if s4_ok else 'FAIL'}  ({chi_S4:.6f})")
print(f"  chi(S^8)=2:      {'PASS' if s8_ok else 'FAIL'}  ({chi_S8:.6f})")
print(f"  chi(U2)=0:       {'PASS' if u2_ok else 'FAIL'}  ({S_U2:.3e})")

all_ok = su3_analytic_ok and su3_stored_ok and s4_ok and s8_ok and u2_ok  # (local)
print(f"\nOVERALL: {'PASS' if all_ok else 'FAIL'}")
