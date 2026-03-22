"""
Session 21c P0-5: Gauss-Bonnet DEFINITIVE DEBUG

The core problem: both "diagonal" and "det-based" partition sums give nonzero
values for round SU(3), but chi(SU(3)) = 0 requires the Euler density to vanish.

Strategy:
1. Build the analytic Riemann tensor from SU(3) structure constants (tau=0).
2. Verify it matches stored data to machine epsilon (or find the discrepancy).
3. Compute the Euler density using the BRUTE FORCE epsilon contraction
   (no pair-partition decomposition — just raw epsilon_{a1...a8} * epsilon_{c1...c8} * R*R*R*R).
4. Cross-check on S^4 (4D sphere) where chi=2 is known and the formula is simpler.
5. Cross-check on S^8 (8D sphere).

If the brute-force epsilon contraction gives zero for analytic SU(3), the pair-partition
formula is wrong. If it gives nonzero, something deeper is wrong.
"""

import numpy as np
from itertools import permutations

print("=" * 70)
print("Session 21c P0-5: Gauss-Bonnet DEFINITIVE DEBUG")
print("=" * 70)

# =====================================================================
# PART 1: Analytic Riemann tensor for round SU(3)
# =====================================================================

# SU(3) structure constants (standard Gell-Mann basis, 0-indexed = i-1)
f = np.zeros((8, 8, 8))

# Standard SU(3) structure constants (1-indexed):
# f_{123} = 1
# f_{147} = f_{246} = f_{257} = f_{345} = 1/2
# f_{156} = f_{367} = -1/2
# f_{458} = f_{678} = sqrt(3)/2
# Converting to 0-indexed (a -> a-1):
f_values = {
    (0, 1, 2): 1.0,
    (0, 3, 6): 0.5,    # f_{147}
    (0, 4, 5): -0.5,   # f_{156}
    (1, 3, 5): 0.5,    # f_{246}
    (1, 4, 6): 0.5,    # f_{257}
    (2, 3, 4): 0.5,    # f_{345}
    (2, 5, 6): -0.5,   # f_{367}
    (3, 4, 7): np.sqrt(3)/2,  # f_{458}
    (5, 6, 7): np.sqrt(3)/2,  # f_{678}
}

for (a, b, c), val in f_values.items():
    f[a, b, c] = val
    f[b, c, a] = val
    f[c, a, b] = val
    f[a, c, b] = -val
    f[b, a, c] = -val
    f[c, b, a] = -val

# Verify antisymmetry
err_anti = max(np.max(np.abs(f + np.transpose(f, (1, 0, 2)))),
               np.max(np.abs(f + np.transpose(f, (0, 2, 1)))))
print(f"\nStructure constant antisymmetry error: {err_anti:.2e}")

# Killing form: B_{ab} = f_{acd} f_{bcd}
B = np.einsum('acd,bcd->ab', f, f)
print(f"Killing form: {np.diag(B)}")
# For SU(3) with this normalization: B_{ab} = -3 delta_{ab}

# Bi-invariant metric: g = -(1/c) B. With c = 3: g = I (ON basis IS the LI basis
# rescaled by 1/sqrt(3)).
# In ON basis: e_a = (1/sqrt(3)) X_a
# ON structure constants: f^ON_{abc} = (1/sqrt(3))^3 * 3 * f_{abc} ... wait, no.
# Actually: [e_a, e_b] = (1/3) [X_a, X_b] = (1/3) f_{abc} X_c = (1/3) f_{abc} sqrt(3) e_c
# = (f_{abc}/sqrt(3)) e_c.
# So f^ON_{abc} = f_{abc} / sqrt(3).

# Riemann tensor for bi-invariant metric in ON frame (STANDARD sign convention, Wald):
# R_{abcd} = -(1/4) f^ON_{abe} f^ON_{cde} = -(1/4)(1/3) f_{abe} f_{cde}
# = -(1/12) f_{abe} f_{cde}

# Our STORED convention (opposite sign): R_stored = -R_Wald = +(1/12) f_{abe} f_{cde}
R_analytic = (1.0 / 12.0) * np.einsum('abe,cde->abcd', f, f)

print(f"\n--- Analytic R (round SU(3), tau=0) ---")
print(f"R[0,1,0,1] = {R_analytic[0,1,0,1]:.10f}")
print(f"Expected (our conv): +(1/12)*f_012^2 = +{1.0/12.0:.10f}")

# Verify Riemann symmetries
err_ab = np.max(np.abs(R_analytic + np.transpose(R_analytic, (1, 0, 2, 3))))
err_cd = np.max(np.abs(R_analytic + np.transpose(R_analytic, (0, 1, 3, 2))))
err_pair = np.max(np.abs(R_analytic - np.transpose(R_analytic, (2, 3, 0, 1))))
print(f"Antisym (a,b): {err_ab:.2e}")
print(f"Antisym (c,d): {err_cd:.2e}")
print(f"Pair sym:      {err_pair:.2e}")

# Ricci tensor: Ric_{ab} = R^c_{acb} = R_{cacb} (Wald) = -R_stored_{cacb}
# With our sign: Ric = R_stored_{cabc} (contraction on 1st and 4th)
Ric_analytic = np.einsum('cabc->ab', R_analytic)
print(f"\nRic_analytic diagonal: {np.diag(Ric_analytic)}")
print(f"Expected: (1/4) for round SU(3) in ON frame")
print(f"Off-diagonal max: {np.max(np.abs(Ric_analytic - np.diag(np.diag(Ric_analytic)))):.2e}")

# Compare with stored data
d = np.load('C:/sandbox/Ainulindale Exflation/tier0-computation/r20a_riemann_tensor.npz',
            allow_pickle=True)
R_stored = d['R_abcd'][0]  # tau = 0

err_total = np.max(np.abs(R_analytic - R_stored))
print(f"\n|R_analytic - R_stored| max: {err_total:.6e}")

if err_total > 1e-12:
    print("WARNING: Significant discrepancy between analytic and stored Riemann tensors!")
    # Find the worst components
    worst = []
    for a in range(8):
        for b in range(a+1, 8):
            for c in range(8):
                for dd in range(c+1, 8):
                    diff = abs(R_analytic[a,b,c,dd] - R_stored[a,b,c,dd])
                    if diff > 1e-10:
                        worst.append((diff, a, b, c, dd,
                                      R_analytic[a,b,c,dd], R_stored[a,b,c,dd]))
    worst.sort(reverse=True)
    print(f"Number of components with |diff| > 1e-10: {len(worst)}")
    for diff, a, b, c, dd, va, vs in worst[:20]:
        print(f"  R[{a},{b},{c},{dd}]: analytic={va:.10f}, stored={vs:.10f}, diff={diff:.6e}")

# =====================================================================
# PART 2: Brute-force Euler density via full epsilon contraction
# =====================================================================
# For an 8-manifold, the Euler integrand (Pfaffian of curvature 2-form) is:
#
# E_8 = (1 / (2^4 * 4!)) * eps^{a1...a8} * eps^{b1...b8}
#       * R_{a1 a2 b1 b2} * R_{a3 a4 b3 b4} * R_{a5 a6 b5 b6} * R_{a7 a8 b7 b8}
#
# where the eps are Levi-Civita SYMBOLS (not tensors, since we're in ON frame
# where g_ab = delta_ab, so symbol = tensor).
#
# For chi: chi = integral E_8 * vol / (2pi)^4
# On constant-curvature space: chi = E_8 * Vol / (2pi)^4
#
# Wait: the factor. Let me be very precise.
# The Euler class in dim=2n is:
# e(TM) = (1/(2pi)^n) * Pf(Omega)
# where Omega is the curvature 2-form matrix (with values in so(2n)).
# Omega^a_b = (1/2) R^a_{bcd} e^c ^ e^d
# Pf(A) for a 2n x 2n antisymmetric matrix:
# Pf(A) = (1/(2^n n!)) * eps_{i1...i_{2n}} * A^{i1 i2} * ... * A^{i_{2n-1} i_{2n}}
#
# For the curvature form Pf, the "matrix" elements are 2-forms, so wedge products
# produce a 2n-form. On a 2n-manifold this is a top form.
#
# Explicitly:
# Pf(Omega) = (1/(2^n n!)) * eps_{a1...a_{2n}} * Omega^{a1 a2} ^ ... ^ Omega^{a_{2n-1} a_{2n}}
#
# Each Omega^{ab} = (1/2) R^{ab}_{cd} e^c ^ e^d, so:
# Omega^{a1 a2} ^ ... ^ Omega^{a_{2n-1} a_{2n}}
# = (1/2^n) * sum R^{a1a2}_{c1d1} ... R^{a_{2n-1}a_{2n}}_{c_nd_n} * e^{c1}^e^{d1}^...^e^{cn}^e^{dn}
#
# The wedge product of 2n one-forms in 2n dims:
# e^{c1}^e^{d1}^...^e^{cn}^e^{dn} = eps_{c1 d1 ... cn dn} * vol
#
# So:
# Pf(Omega) = (1/(2^n n!)) * (1/2^n) * eps_a * eps_c * RRRR * vol
# = (1/(2^{2n} n!)) * eps_a * eps_c * prod R_{a_{2k-1}a_{2k}, c_{2k-1}c_{2k}} * vol
#
# chi = integral e(TM) = integral (1/(2pi)^n) * Pf(Omega)
# = (1/(2pi)^n) * (1/(2^{2n} n!)) * eps_a * eps_c * RRRR * Vol
# = (1/(2pi)^n) * (1/(2^{2n} n!)) * S * Vol
# where S = full double-epsilon contraction.
#
# For n=4: 2^{2n} n! = 2^8 * 24 = 256 * 24 = 6144.
# chi = S * Vol / (6144 * (2pi)^4)
#
# From debug3: S = 6144 * corrected_partition_sum
# So chi = corrected_partition_sum * Vol / (2pi)^4.
# OK so this confirms the formula. The corrected partition sum (with det) should give zero.
# But it didn't (gave ~1e-4).
#
# Let me try the TRULY brute force computation: iterate over all 8! permutations.
# Actually 8! = 40320 and we need 8!^2 = 1.6 billion — too many.
#
# Instead, use the fact that:
# S = eps_a * eps_c * RRRR
# = sum_{sigma, rho in S_8} sgn(sigma) sgn(rho) * prod_{k=0}^3 R_{sigma(2k), sigma(2k+1), rho(2k), rho(2k+1)}
#
# We can compute this by noting:
# S = sum_sigma sgn(sigma) * [sum_rho sgn(rho) * prod_k R_{sigma(2k)sigma(2k+1), rho(2k)rho(2k+1)}]
#
# The inner sum for fixed sigma is another double-epsilon, but with the a-indices
# permuted by sigma. In ON frame, we can write:
# T_{b1...b8} = sum_rho sgn(rho) * prod_k R_{b_{2k}, b_{2k+1}, rho(2k), rho(2k+1)}
#
# And S = sum_sigma sgn(sigma) * T_{sigma(0),...,sigma(7)}
#
# Computing T directly:
# T_{b1...b8} involves sum over rho with 8! terms, which is feasible for one fixed b-sequence.
# But iterating over all sigma gives 8! * 8! again.
#
# More efficient: use the pair-partition formula CORRECTLY.
# S = 6144 * sum_{P,Q} sgn(P) sgn(Q) * det(M_{PQ})
#
# OR: use the identity with determinants.
# Let me instead verify with a SMALLER case first.

# =====================================================================
# PART 2a: Verify formula on 4D (S^4 and a non-trivial 4D space)
# =====================================================================

print("\n" + "=" * 70)
print("PART 2: Cross-check on 4D (n=2)")
print("=" * 70)

# For 4D: 3 pair-partitions of {0,1,2,3}
def partitions_into_pairs(s):
    s = sorted(s)
    if len(s) == 0:
        yield []
        return
    if len(s) == 2:
        yield [(s[0], s[1])]
        return
    first = s[0]
    rest = s[1:]
    for idx, partner in enumerate(rest):
        pair = (first, partner)
        remaining = rest[:idx] + rest[idx+1:]
        for sub_partition in partitions_into_pairs(remaining):
            yield [pair] + sub_partition

def perm_sign(perm):
    n = len(perm)
    visited = [False] * n
    sign = 1
    for i in range(n):
        if visited[i]:
            continue
        j = i
        cycle_len = 0
        while not visited[j]:
            visited[j] = True
            j = perm[j]
            cycle_len += 1
        if cycle_len % 2 == 0:
            sign *= -1
    return sign

parts4 = list(partitions_into_pairs(list(range(4))))
psigns4 = [perm_sign([x for pair in p for x in pair]) for p in parts4]
print(f"4D pair partitions: {len(parts4)}")
for p, s in zip(parts4, psigns4):
    print(f"  {p} -> sign {s}")

# S^4 Riemann (constant curvature K=1): R_{abcd} = delta_{ac}delta_{bd} - delta_{ad}delta_{bc}
R_S4 = np.zeros((4, 4, 4, 4))
for a in range(4):
    for b in range(4):
        for c in range(4):
            for dd in range(4):
                R_S4[a, b, c, dd] = (1.0 if a == c and b == dd else 0.0) - (1.0 if a == dd and b == c else 0.0)

# BRUTE FORCE for 4D: iterate over all 4!^2 = 576 pairs of permutations
S_bf_4d = 0.0
for sigma in permutations(range(4)):
    for rho in permutations(range(4)):
        sgn_s = perm_sign(list(sigma))
        sgn_r = perm_sign(list(rho))
        prod_R = R_S4[sigma[0], sigma[1], rho[0], rho[1]] * R_S4[sigma[2], sigma[3], rho[2], rho[3]]
        S_bf_4d += sgn_s * sgn_r * prod_R

# Partition sum (diagonal)
diag_4d = 0.0
for pi_idx, pi_part in enumerate(parts4):
    for pj_idx, pj_part in enumerate(parts4):
        prod = 1.0
        for k in range(2):
            a1, a2 = pi_part[k]
            b1, b2 = pj_part[k]
            prod *= R_S4[a1, a2, b1, b2]
        diag_4d += psigns4[pi_idx] * psigns4[pj_idx] * prod

# Partition sum (det)
det_4d = 0.0
for pi_idx, pi_part in enumerate(parts4):
    for pj_idx, pj_part in enumerate(parts4):
        M = np.zeros((2, 2))
        for k in range(2):
            a1, a2 = pi_part[k]
            for l in range(2):
                b1, b2 = pj_part[l]
                M[k, l] = R_S4[a1, a2, b1, b2]
        det_4d += psigns4[pi_idx] * psigns4[pj_idx] * np.linalg.det(M)

print(f"\nS^4 results:")
print(f"  Brute force S:       {S_bf_4d:.6f}")
print(f"  Diagonal part. sum:  {diag_4d:.6f}")
print(f"  Det part. sum:       {det_4d:.6f}")
print(f"  S / (2^4 * 2!):     {S_bf_4d / (16 * 2):.6f}")
print(f"  6144/S_bf * det_4d:  check")

# Formula check: S = (2^n)^2 * n! * det_sum = 2^4 * 2! * det_sum = 16 * 2 * det_sum = 32 * det_sum
print(f"  32 * det_sum:        {32 * det_4d:.6f}")
print(f"  Ratio S_bf / (32 * det_sum): {S_bf_4d / (32 * det_4d):.6f}")

# Compute chi for S^4:
# chi = S * Vol / ((2^{2n} * n!) * (2pi)^n) where n=2
# = S * Vol / (16 * 2 * (2pi)^2) = S * Vol / (32 * 4pi^2) = S * Vol / (128 pi^2)
# Vol(S^4) = 8 pi^2 / 3
# chi = S * 8pi^2 / (3 * 128 pi^2) = S / 48
print(f"  chi(S^4) = S / 48:   {S_bf_4d / 48:.6f} (expected 2)")

# Also: chi = det_sum * Vol / (2pi)^n
# = det_sum * 8pi^2/3 / (4pi^2) = det_sum * 2/3
print(f"  chi = det_sum*2/3:   {det_4d * 2 / 3:.6f}")

# =====================================================================
# PART 2b: 4D Lie group test — use SU(2) (S^3) — wait, SU(2) is 3D.
# Let me use SO(3) = RP^3 — also 3D. Need a 4D Lie group.
# U(2) = U(1) x SU(2) is 4D! chi(U(2)) = chi(U(1)) * chi(SU(2)) = 0 * 0 = 0.
# Or T^2 x S^2 — but that's not a Lie group manifold of the right kind.
# Actually, for 4D we can use the PRODUCT S^2 x S^2.
# chi(S^2 x S^2) = chi(S^2)^2 = 4.
# Its Riemann tensor = direct sum of two S^2 Riemanns.
# =====================================================================

print("\n" + "=" * 70)
print("PART 3: 4D product test: S^2 x S^2 (chi = 4)")
print("=" * 70)

# S^2 x S^2 has Riemann tensor:
# Indices 0,1 for first S^2, indices 2,3 for second S^2.
# R_{0101} = 1, R_{2323} = 1. Cross-block = 0.
R_prod = np.zeros((4, 4, 4, 4))
# First S^2 block:
R_prod[0, 1, 0, 1] = 1.0
R_prod[0, 1, 1, 0] = -1.0
R_prod[1, 0, 0, 1] = -1.0
R_prod[1, 0, 1, 0] = 1.0
# Second S^2 block:
R_prod[2, 3, 2, 3] = 1.0
R_prod[2, 3, 3, 2] = -1.0
R_prod[3, 2, 2, 3] = -1.0
R_prod[3, 2, 3, 2] = 1.0

S_bf_prod = 0.0
for sigma in permutations(range(4)):
    for rho in permutations(range(4)):
        sgn_s = perm_sign(list(sigma))
        sgn_r = perm_sign(list(rho))
        prod_R = R_prod[sigma[0], sigma[1], rho[0], rho[1]] * R_prod[sigma[2], sigma[3], rho[2], rho[3]]
        S_bf_prod += sgn_s * sgn_r * prod_R

det_prod = 0.0
diag_prod_sum = 0.0
for pi_idx, pi_part in enumerate(parts4):
    for pj_idx, pj_part in enumerate(parts4):
        M = np.zeros((2, 2))
        for k in range(2):
            a1, a2 = pi_part[k]
            for l in range(2):
                b1, b2 = pj_part[l]
                M[k, l] = R_prod[a1, a2, b1, b2]
        det_prod += psigns4[pi_idx] * psigns4[pj_idx] * np.linalg.det(M)
        diag = 1.0
        for k in range(2):
            diag *= M[k, k]
        diag_prod_sum += psigns4[pi_idx] * psigns4[pj_idx] * diag

print(f"S^2 x S^2 results:")
print(f"  Brute force S:       {S_bf_prod:.6f}")
print(f"  Diagonal part. sum:  {diag_prod_sum:.6f}")
print(f"  Det part. sum:       {det_prod:.6f}")
print(f"  32 * det_sum:        {32 * det_prod:.6f}")
print(f"  Ratio S_bf/(32*det): {S_bf_prod / (32 * det_prod) if det_prod != 0 else 'N/A':.6f}")

# chi(S^2 x S^2) using chi = det_sum * Vol / (2pi)^n
# Vol(S^2 x S^2) = (4pi)^2 = 16 pi^2
# chi = det_sum * 16 pi^2 / (4 pi^2) = 4 * det_sum
print(f"  chi = 4 * det_sum:   {4 * det_prod:.6f} (expected 4)")

# =====================================================================
# PART 4: Now test a 4D LIE GROUP (chi = 0)
# Use U(1) x SU(2) = U(2), dim = 4
# Actually SU(2) is S^3, and U(1) is S^1.
# For U(1) x SU(2) with product metric:
# Riemann only has the SU(2) block (U(1) is flat).
# =====================================================================

print("\n" + "=" * 70)
print("PART 4: 4D Lie group test: U(1) x SU(2) (chi = 0)")
print("=" * 70)

# SU(2) structure constants: f_{012} = ... wait, SU(2) is 3D.
# U(1) x SU(2) has dim = 4. Index 0 = U(1), indices 1,2,3 = SU(2).
# SU(2) structure constants: f_{ijk} = epsilon_{ijk} for i,j,k in {1,2,3} (= indices 1,2,3).
# In ON frame for bi-invariant metric:
# B_{ij} = f_{ikl} f_{jkl} = 2 delta_{ij} for SU(2).
# g = I => ON basis = (1/sqrt(2)) * LI basis (but only for the SU(2) part).
# f^ON_{ijk} = (1/sqrt(2)) f_{ijk} for i,j,k in {1,2,3}.
# R_{ijkl} = -(1/4) f^ON_{ije} f^ON_{kle} = -(1/4)(1/2) epsilon_{ije} epsilon_{kle}
# = -(1/8) (delta_{ik}delta_{jl} - delta_{il}delta_{jk})

# With our stored convention (opposite sign):
R_U2 = np.zeros((4, 4, 4, 4))
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            for l in range(1, 4):
                R_U2[i, j, k, l] = (1.0/8.0) * (
                    (1.0 if i == k and j == l else 0.0) -
                    (1.0 if i == l and j == k else 0.0)
                )
# Index 0 (U(1)): all curvature components vanish.

# Brute force
S_bf_U2 = 0.0
for sigma in permutations(range(4)):
    for rho in permutations(range(4)):
        sgn_s = perm_sign(list(sigma))
        sgn_r = perm_sign(list(rho))
        prod_R = R_U2[sigma[0], sigma[1], rho[0], rho[1]] * R_U2[sigma[2], sigma[3], rho[2], rho[3]]
        S_bf_U2 += sgn_s * sgn_r * prod_R

det_U2 = 0.0
diag_U2 = 0.0
for pi_idx, pi_part in enumerate(parts4):
    for pj_idx, pj_part in enumerate(parts4):
        M = np.zeros((2, 2))
        for k in range(2):
            a1, a2 = pi_part[k]
            for l in range(2):
                b1, b2 = pj_part[l]
                M[k, l] = R_U2[a1, a2, b1, b2]
        det_U2 += psigns4[pi_idx] * psigns4[pj_idx] * np.linalg.det(M)
        diag_val = 1.0
        for k in range(2):
            diag_val *= M[k, k]
        diag_U2 += psigns4[pi_idx] * psigns4[pj_idx] * diag_val

print(f"U(1) x SU(2) results:")
print(f"  Brute force S:       {S_bf_U2:.10e}")
print(f"  Diagonal part. sum:  {diag_U2:.10e}")
print(f"  Det part. sum:       {det_U2:.10e}")
print(f"  Expected: ALL ZERO (chi = 0)")

# =====================================================================
# PART 5: 8D Euler density for ANALYTIC SU(3)
# =====================================================================

print("\n" + "=" * 70)
print("PART 5: 8D Euler density for ANALYTIC round SU(3)")
print("=" * 70)

parts8 = list(partitions_into_pairs(list(range(8))))
psigns8 = [perm_sign([x for pair in p for x in pair]) for p in parts8]
print(f"8D pair partitions: {len(parts8)}")

n = 4  # dim/2

# Det-based partition sum for ANALYTIC R
det_analytic = 0.0
diag_analytic = 0.0
for pi_idx, pi_part in enumerate(parts8):
    sgn_i = psigns8[pi_idx]
    for pj_idx, pj_part in enumerate(parts8):
        sgn_j = psigns8[pj_idx]
        M = np.zeros((n, n))
        for k in range(n):
            a1, a2 = pi_part[k]
            for l in range(n):
                b1, b2 = pj_part[l]
                M[k, l] = R_analytic[a1, a2, b1, b2]
        det_analytic += sgn_i * sgn_j * np.linalg.det(M)
        diag_val = 1.0
        for k in range(n):
            diag_val *= M[k, k]
        diag_analytic += sgn_i * sgn_j * diag_val

print(f"\nANALYTIC SU(3) (round, tau=0):")
print(f"  Det partition sum:      {det_analytic:.15e}")
print(f"  Diagonal partition sum: {diag_analytic:.15e}")
print(f"  Expected: 0 (chi = 0)")

# Det-based partition sum for STORED R at tau=0
det_stored = 0.0
diag_stored = 0.0
for pi_idx, pi_part in enumerate(parts8):
    sgn_i = psigns8[pi_idx]
    for pj_idx, pj_part in enumerate(parts8):
        sgn_j = psigns8[pj_idx]
        M = np.zeros((n, n))
        for k in range(n):
            a1, a2 = pi_part[k]
            for l in range(n):
                b1, b2 = pj_part[l]
                M[k, l] = R_stored[a1, a2, b1, b2]
        det_stored += sgn_i * sgn_j * np.linalg.det(M)
        diag_val = 1.0
        for k in range(n):
            diag_val *= M[k, k]
        diag_stored += sgn_i * sgn_j * diag_val

print(f"\nSTORED R at tau=0:")
print(f"  Det partition sum:      {det_stored:.15e}")
print(f"  Diagonal partition sum: {diag_stored:.15e}")

print(f"\nDifference (stored - analytic):")
print(f"  Det:      {det_stored - det_analytic:.15e}")
print(f"  Diagonal: {diag_stored - diag_analytic:.15e}")

# =====================================================================
# PART 6: If analytic gives zero, check tau-dependence of stored data
# =====================================================================

if abs(det_analytic) < 1e-12:
    print("\n*** ANALYTIC gives zero — stored data has issues. ***")
    print("Computing det partition sum for all tau values...")

    tau_vals = d['tau']
    R_all = d['R_abcd']

    det_sums = []
    for ti in range(len(tau_vals)):
        R = R_all[ti]
        det_sum_tau = 0.0
        for pi_idx, pi_part in enumerate(parts8):
            sgn_i = psigns8[pi_idx]
            for pj_idx, pj_part in enumerate(parts8):
                sgn_j = psigns8[pj_idx]
                M = np.zeros((n, n))
                for k in range(n):
                    a1, a2 = pi_part[k]
                    for l in range(n):
                        b1, b2 = pj_part[l]
                        M[k, l] = R[a1, a2, b1, b2]
                det_sum_tau += sgn_i * sgn_j * np.linalg.det(M)
        det_sums.append(det_sum_tau)

    det_sums = np.array(det_sums)
    print(f"\nDet partition sums across tau:")
    for ti in range(len(tau_vals)):
        print(f"  tau={tau_vals[ti]:.2f}: {det_sums[ti]:.15e}")

    max_dev = np.max(np.abs(det_sums - det_sums[0]))
    print(f"\nMax |det(tau) - det(0)|: {max_dev:.15e}")
    print(f"Max |det(tau)|:          {np.max(np.abs(det_sums)):.15e}")

    if np.max(np.abs(det_sums)) < 1e-10:
        print("\n*** ALL det partition sums are near zero. Euler density = 0. ***")
        print("*** VERDICT: PASS (topological invariance holds) ***")
    else:
        print("\n*** Det partition sums are nonzero. ***")
        if max_dev < 1e-10 * max(1, abs(det_sums[0])):
            print("*** BUT: they are CONSTANT across tau (topological invariant). ***")
            print("*** VERDICT: CONDITIONAL PASS (E_8 constant but nonzero — norm issue?) ***")
        else:
            print("*** AND: they VARY with tau. ***")
            print("*** VERDICT: FAIL (Euler density varies) ***")
else:
    print(f"\n*** ANALYTIC Euler density is NONZERO: {det_analytic:.15e} ***")
    print("*** This means the FORMULA is wrong, not the data! ***")
    print("*** Investigating formula normalization... ***")

    # The Pfaffian of the curvature 2-form involves additional structure.
    # For a Lie group with bi-invariant metric, maybe the Pfaffian has a different
    # normalization than what we're computing.
    #
    # Key insight: for ODD-dimensional Lie groups, the Euler class is always zero.
    # SU(3) is dim=8 (even). But SU(3) has rank 2 and dim 8.
    # The Betti numbers of SU(3): b_0=1, b_3=1, b_5=1, b_8=1 (all others 0).
    # chi = sum (-1)^k b_k = 1 - 0 + 0 - 1 + 0 - 1 + 0 - 0 + 1 = 0.
    # (b_0=1, b_1=0, b_2=0, b_3=1, b_4=0, b_5=1, b_6=0, b_7=0, b_8=1)
    # chi = 1 - 0 + 0 - 1 + 0 - 1 + 0 - 0 + 1 = 0. Correct.

    # Check: is the issue with our structure constants?
    # Let me verify a KNOWN result: Kretschner scalar.
    K_analytic = np.einsum('abcd,abcd->', R_analytic, R_analytic)
    K_stored = np.einsum('abcd,abcd->', R_stored, R_stored)
    print(f"\nKretschner scalar: analytic={K_analytic:.10f}, stored={K_stored:.10f}")

    # And Ricci scalar
    R_scalar_analytic = np.trace(Ric_analytic)
    R_scalar_stored = np.trace(np.einsum('cabc->ab', R_stored))
    print(f"Ricci scalar: analytic={R_scalar_analytic:.10f}, stored={R_scalar_stored:.10f}")

print("\n" + "=" * 70)
print("DONE")
print("=" * 70)
