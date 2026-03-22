"""
Session 21c P0-5: Gauss-Bonnet BRUTE FORCE via epsilon tensor contraction.

The pair-partition formula gives nonzero Euler density for ANALYTIC round SU(3),
which must be wrong (chi(SU(3)) = 0). The 4D cross-checks pass perfectly.

This script computes the double-epsilon contraction DIRECTLY using numpy's
Levi-Civita symbol and einsum, avoiding the pair-partition decomposition entirely.

The Euler density in dim=2n is proportional to:
E = eps^{a_1...a_{2n}} eps^{b_1...b_{2n}} * R_{a1 a2 b1 b2} * ... * R_{a_{2n-1} a_{2n} b_{2n-1} b_{2n}}

We compute this for:
- S^4 (dim=4, chi=2) -- quick cross-check
- U(1) x SU(2) (dim=4, chi=0) -- Lie group check
- Analytic SU(3) (dim=8, chi=0) -- THE test
"""

import numpy as np

print("=" * 70)
print("BRUTE FORCE EULER DENSITY VIA EPSILON TENSOR")
print("=" * 70)

# =====================================================================
# Build Levi-Civita symbols
# =====================================================================

def levi_civita(n):
    """Build the n-dimensional Levi-Civita symbol as a numpy array."""
    from itertools import permutations
    eps = np.zeros([n] * n, dtype=np.float64)
    identity = list(range(n))
    for perm in permutations(identity):
        # Count inversions to get sign
        sign = 1
        perm_list = list(perm)
        for i in range(n):
            for j in range(i + 1, n):
                if perm_list[i] > perm_list[j]:
                    sign *= -1
        eps[tuple(perm)] = sign
    return eps

eps4 = levi_civita(4)
print(f"4D Levi-Civita built: shape {eps4.shape}")

# =====================================================================
# 4D TEST: S^4 (chi = 2)
# =====================================================================
print("\n--- 4D: S^4 ---")

R_S4 = np.zeros((4, 4, 4, 4))
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                R_S4[a,b,c,d] = float(a==c)*float(b==d) - float(a==d)*float(b==c)

# E_4 = eps^{a1 a2 a3 a4} eps^{b1 b2 b3 b4} R_{a1 a2 b1 b2} R_{a3 a4 b3 b4}
# Using einsum:
S_S4 = np.einsum('abcd,efgh,aebf,cgdh', eps4, eps4, R_S4, R_S4)
print(f"S(S^4) = {S_S4:.6f}")
print(f"chi = S * Vol / ((2^4 * 2!) * (2pi)^2) = S / 48 * (8pi^2/3) / (4pi^2)")
# chi = S * Vol / (32 * 4pi^2) = S * 8pi^2/(3 * 128pi^2) = S/48
print(f"chi(S^4) via S/48: {S_S4/48:.6f} (expected 2)")

# =====================================================================
# 4D TEST: U(1) x SU(2) (chi = 0)
# =====================================================================
print("\n--- 4D: U(1) x SU(2) ---")

R_U2 = np.zeros((4, 4, 4, 4))
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            for l in range(1, 4):
                R_U2[i,j,k,l] = (1.0/8.0) * (float(i==k)*float(j==l) - float(i==l)*float(j==k))

S_U2 = np.einsum('abcd,efgh,aebf,cgdh', eps4, eps4, R_U2, R_U2)
print(f"S(U(1)xSU(2)) = {S_U2:.10e} (expected 0)")

# =====================================================================
# 8D TEST: Analytic SU(3)
# =====================================================================
print("\n--- 8D: Analytic SU(3) ---")

# Build structure constants
f = np.zeros((8, 8, 8))
f_values = {
    (0, 1, 2): 1.0,
    (0, 3, 6): 0.5,
    (0, 4, 5): -0.5,
    (1, 3, 5): 0.5,
    (1, 4, 6): 0.5,
    (2, 3, 4): 0.5,
    (2, 5, 6): -0.5,
    (3, 4, 7): np.sqrt(3)/2,
    (5, 6, 7): np.sqrt(3)/2,
}
for (a, b, c), val in f_values.items():
    f[a, b, c] = val
    f[b, c, a] = val
    f[c, a, b] = val
    f[a, c, b] = -val
    f[b, a, c] = -val
    f[c, b, a] = -val

# R_{abcd} = (1/12) f_{abe} f_{cde}  (our sign convention)
R_SU3 = (1.0 / 12.0) * np.einsum('abe,cde->abcd', f, f)

# 8D Levi-Civita
print("Building 8D Levi-Civita symbol...")
eps8 = levi_civita(8)
print(f"8D Levi-Civita built: shape {eps8.shape}")

# For 8D (n=4):
# E_8 = eps^{a1...a8} eps^{b1...b8} R_{a1 a2 b1 b2} R_{a3 a4 b3 b4} R_{a5 a6 b5 b6} R_{a7 a8 b7 b8}
#
# Direct einsum with 16 indices would be insane. Instead, use a step-by-step contraction.
#
# Strategy: Contract eps_a with R's step by step.
# Define intermediate tensors.

# Step 1: Contract eps^{a1...a8} with R_{a1 a2, :, :} to get a rank-8 tensor.
# Actually, let's think about this differently.
#
# We can write:
# S = eps^A eps^B * R_{A1, B1} * R_{A2, B2} * R_{A3, B3} * R_{A4, B4}
# where A = (a1,...,a8), B = (b1,...,b8), and Ak = (a_{2k-1}, a_{2k}), Bk = (b_{2k-1}, b_{2k}).
#
# An efficient approach: define the "curvature matrix" as a linear map on bivectors.
# R: Lambda^2 -> Lambda^2, with matrix elements R_{[ab],[cd]}.
# Then S = (some combinatorial factor) * sum_sigma sgn(sigma) * prod R entries.
#
# Actually, the cleanest approach: use the identity that
# eps^{a1...a8} eps^{b1...b8} * prod_k R_{a_{2k-1} a_{2k} b_{2k-1} b_{2k}}
# = sum_{sigma, rho in S_8} sgn(sigma) sgn(rho) * prod_k R_{sigma(2k-1) sigma(2k) rho(2k-1) rho(2k)}
#
# This is a sum over 40320^2 ~ 1.6 billion terms — too many.
#
# BUT: we can compute it as a DETERMINANT.
# The key identity: for a 2n x 2n antisymmetric matrix M (viewed as element of so(2n)),
# Pf(M)^2 = det(M).
# And the Euler density involves Pf of the curvature 2-form MATRIX.
#
# More concretely: the Riemann tensor defines a symmetric bilinear form on Lambda^2(R^8).
# The dimension of Lambda^2(R^8) = C(8,2) = 28.
# The curvature acts as a 28x28 symmetric matrix.
# BUT the Euler density is NOT the determinant of this matrix.
#
# Let me try a different numerical approach: iterate over permutations of {0,...,7}
# but only over the 40320 permutations sigma, and for each sigma, compute the
# "row" sum over rho. The sum over rho can be done efficiently using the fact that
# it's an epsilon contraction with a product of R tensors.

print("Computing via stepwise contraction...")

# Method: Compute the quantity
# T_{b1...b8} = eps^{a1...a8} * R_{a1 a2 b1 b2} * R_{a3 a4 b3 b4} * R_{a5 a6 b5 b6} * R_{a7 a8 b7 b8}
#
# Then S = eps^{b1...b8} * T_{b1...b8} = full contraction.
#
# Computing T:
# T_{b1 b2 b3 b4 b5 b6 b7 b8} = eps_{a1 a2 a3 a4 a5 a6 a7 a8}
#   * R_{a1 a2 b1 b2} * R_{a3 a4 b3 b4} * R_{a5 a6 b5 b6} * R_{a7 a8 b7 b8}
#
# Step 1: W1_{a3 a4 a5 a6 a7 a8, b1 b2} = eps_{a1 a2 a3 a4 a5 a6 a7 a8} * R_{a1 a2 b1 b2}
# This has 8^8 entries but most are zero. Let me use a more memory-efficient approach.
#
# For each fixed (b1,b2,...,b8):
# T = eps * R * R * R * R (contracted over a-indices).
# This is expensive for 8^8 output entries.
#
# Better: compute T as an 8-tensor using sequential contractions.

# Actually, the most efficient numerical method:
# 1. Build R as a 28x28 matrix (curvature on bivectors)
# 2. Compute Pf of this matrix? No — the Euler density isn't simply Pf of the curvature matrix.
#
# Let me think again...
#
# The curvature 2-form is an element of Omega^2(so(8)).
# Written as a matrix of 2-forms: Omega^a_b, where each entry is a 2-form.
# Omega^a_b is ANTISYMMETRIC in (a,b): Omega^a_b = -Omega^b_a.
# So Omega lives in Lambda^2(R^8) tensor-product Lambda^2(R^8), with the first Lambda^2
# coming from the matrix indices and the second from the form indices.
#
# The Pfaffian of an 8x8 antisymmetric matrix of 2-forms produces an 8-form.
# On an 8-manifold, this is a top form.
#
# For constant curvature (left-invariant metric), each Omega^a_b is a constant 2-form:
# Omega^a_b = (1/2) R^a_{bcd} e^c ^ e^d = sum_{c<d} R^a_{bcd} e^c ^ e^d
#
# The Pfaffian:
# Pf(Omega) = (1/(2^4 * 4!)) * eps_{a1...a8} * Omega^{a1 a2} ^ Omega^{a3 a4} ^ Omega^{a5 a6} ^ Omega^{a7 a8}
#
# Each Omega^{ai ai+1} is a 2-form. The wedge of four 2-forms is an 8-form.
# On evaluating: Omega^{a1 a2} ^ Omega^{a3 a4} ^ Omega^{a5 a6} ^ Omega^{a7 a8}
# = (1/2^4) * R^{a1}_{a2 c1 d1} R^{a3}_{a4 c3 d4} ... * (e^c1^e^d1^...^e^c4^e^d4)
#
# Wait, R^{a1}_{a2 c d} = g^{a1 e} R_{e a2 c d} = R_{a1 a2 c d} in ON frame.
# So Omega^{a1 a2} = (1/2) R_{a1 a2 cd} e^c ^ e^d.
# But CAREFUL: Omega^a_b means first index UP, second DOWN.
# For a metric connection: R_{abcd} = -R_{bacd}, so Omega^{ab} = -Omega^{ba}.
# The matrix is antisymmetric.
#
# In ON frame Omega^{ab} (both up) = Omega^a_b (first up, second... for so(n),
# the Lie algebra is antisymmetric matrices, so Omega^{ab} = -Omega^{ba}).
# And Omega^{ab} = (1/2) R^{ab}_{cd} e^c e^d = (1/2) R_{abcd} e^c e^d.
#
# Now the key: in the Pfaffian formula, the matrix indices a1,...,a8 are contracted with
# EPSILON_{a1...a8}. The Pfaffian treats the 8x8 antisymmetric matrix Omega as having
# INDEPENDENT entries Omega^{ab} for a < b. There are 28 such entries, each a 2-form.
#
# Pf(Omega) = (1/(2^4 * 4!)) * eps_{a1 a2 a3 a4 a5 a6 a7 a8}
#           * Omega^{a1 a2} ^ Omega^{a3 a4} ^ Omega^{a5 a6} ^ Omega^{a7 a8}
#
# The 1/(2^4) accounts for the fact that eps sums over all orderings of each pair (a_{2k-1}, a_{2k})
# while Omega^{ab} is already antisymmetric, so we're double-counting by 2 per pair.
# The 1/4! accounts for the reordering of the 4 blocks.
#
# Substituting Omega^{ab} = (1/2) R_{ab,cd} e^c e^d:
# Omega^{a1a2} ^ ... ^ Omega^{a7a8}
# = (1/2^4) * sum_{c,d indices} R_{a1a2 c1d1} ... R_{a7a8 c4d4} * (e^{c1}^e^{d1}^...^e^{c4}^e^{d4})
#
# The wedge product e^{c1}^e^{d1}^...^e^{c4}^e^{d4} = eps_{c1 d1 c2 d2 c3 d3 c4 d4} * vol_8
# where vol_8 = e^0 ^ ... ^ e^7.
#
# So:
# Pf(Omega) = (1/(2^4 * 4!)) * (1/2^4) * eps_A * eps_B * prod R_{Ak, Bk} * vol
# = (1/(2^8 * 24)) * S * vol
# = S / 6144 * vol
#
# And chi = integral (1/(2pi)^4) Pf(Omega) = S / (6144 * (2pi)^4) * Vol
#
# For the sphere: S = 6144 * 105 (from our partition analysis).
# chi = 6144 * 105 / (6144 * 16 * pi^4) * 32 pi^4 / 105 = 32/16 = 2. CORRECT.
#
# For SU(3): need S = 0.
# Our partition analysis gives: S = 6144 * det_partition_sum = 6144 * 1.085e-4.
# This should be 0 but isn't. So either the partition analysis is wrong or the
# structure constants are wrong or there's a deeper issue.
#
# Let me compute S DIRECTLY for 4D first to verify the epsilon approach,
# then do 8D with a smart contraction.

# 4D Direct computation using tensor contractions (not iterating over permutations):
# S_4D = eps_{abcd} eps_{efgh} R_{ae bf} R_{cg dh}
# Note the index structure: the k-th R factor takes indices (a_{2k-1}, a_{2k}, b_{2k-1}, b_{2k}).

# Let me verify the einsum string is correct.
# S = eps_{a1 a2 a3 a4} * eps_{b1 b2 b3 b4} * R_{a1 a2, b1 b2} * R_{a3 a4, b3 b4}
# einsum: 'ABCD,EFGH,AEBF,CGDH' where A=a1, B=a2, C=a3, D=a4, E=b1, F=b2, G=b3, H=b4

S_check = np.einsum('abcd,efgh,aebf,cgdh', eps4, eps4, R_S4, R_S4)
print(f"\n4D direct S(S^4) = {S_check:.6f} (should be 96)")

S_check_U2 = np.einsum('abcd,efgh,aebf,cgdh', eps4, eps4, R_U2, R_U2)
print(f"4D direct S(U2) = {S_check_U2:.10e} (should be 0)")

# WAIT: the einsum indices might be wrong!
# Let me be very explicit.
# S = sum_{a1,a2,a3,a4,b1,b2,b3,b4} eps[a1,a2,a3,a4] * eps[b1,b2,b3,b4]
#     * R[a1,a2,b1,b2] * R[a3,a4,b3,b4]
#
# In einsum notation with single-letter indices:
# Let p=a1, q=a2, r=a3, s=a4, w=b1, x=b2, y=b3, z=b4
# S = eps[p,q,r,s] * eps[w,x,y,z] * R[p,q,w,x] * R[r,s,y,z]
# einsum: 'pqrs,wxyz,pqwx,rsyz->'

S_test1 = np.einsum('pqrs,wxyz,pqwx,rsyz', eps4, eps4, R_S4, R_S4)
print(f"\n4D S(S^4) [corrected einsum]: {S_test1:.6f}")
S_test2 = np.einsum('pqrs,wxyz,pqwx,rsyz', eps4, eps4, R_U2, R_U2)
print(f"4D S(U2)  [corrected einsum]: {S_test2:.10e}")

# Hmm, the first einsum might have been wrong! Let me check.
# 'abcd,efgh,aebf,cgdh':
# eps[a,b,c,d] * eps[e,f,g,h] * R[a,e,b,f] * R[c,g,d,h]
# This contracts: a1=a, a2=b, a3=c, a4=d with b1=e, b2=f, b3=g, b4=h.
# R factors: R[a,e,b,f] = R[a1,b1,a2,b2] !!
# This is R_{a1 b1 a2 b2}, NOT R_{a1 a2 b1 b2}!
# The index pairing is WRONG in the first einsum!

# The CORRECT contraction is:
# R factor k takes (a_{2k-1}, a_{2k}) as first pair and (b_{2k-1}, b_{2k}) as second pair.
# Factor 1: R[a1, a2, b1, b2] = R[p, q, w, x]
# Factor 2: R[a3, a4, b3, b4] = R[r, s, y, z]
# So: 'pqrs,wxyz,pqwx,rsyz->' is correct.

# But wait, my first einsum also gave 96 for S^4. Let me check why.
# For constant curvature: R_{abcd} = delta_{ac}delta_{bd} - delta_{ad}delta_{bc}.
# R_{a1,b1,a2,b2} and R_{a1,a2,b1,b2} might give the same S due to the pair symmetry
# R_{abcd} = R_{cdab}. Let me check:
# R[a,e,b,f]: this is R_{aebf}. Pair symmetry: R_{aebf} = R_{bfae}.
# R[a,b,e,f]: this is R_{abef}. These are generally different!
# For constant curvature: R_{aebf} = delta_{ab}delta_{ef} - delta_{af}delta_{eb}.
# R_{abef} = delta_{ae}delta_{bf} - delta_{af}delta_{be}.
# These ARE different tensors. But the double-epsilon contraction might give the same result
# for constant curvature due to the symmetry of the sphere.
# For SU(3), they will differ. So I need to be careful.

# OK so the CORRECT 8D computation should use the 'pqrs...' style.
# For 8D: 16 indices in the einsum. numpy can handle up to 26 (a-z).
# S = eps[a,b,c,d,e,f,g,h] * eps[i,j,k,l,m,n,o,p]
#   * R[a,b,i,j] * R[c,d,k,l] * R[e,f,m,n] * R[g,h,o,p]
# einsum: 'abcdefgh,ijklmnop,abij,cdkl,efmn,ghop->'

# BUT: eps8 is a rank-8 tensor with 8^8 = 16M entries. This should be manageable.
# The einsum with 16 free indices contracted... numpy might struggle.

# Let me try a step-by-step approach instead.
print("\n--- 8D: Step-by-step contraction for SU(3) ---")

# Step 1: Contract first R with first epsilon.
# W1[c,d,e,f,g,h, i,j] = eps[a,b,c,d,e,f,g,h] * R[a,b,i,j]
# This is a rank-8 tensor: 8^8 = 16M entries. Too big.

# Better approach: contract BOTH epsilons with ALL R factors in stages.
#
# Alternative: use the 28-dimensional bivector representation.
# Map (a,b) with a<b to a single index I in {0,...,27}.
# R_{abcd} -> R_IJ where I=(a,b), J=(c,d).
# eps_{a1...a8} -> E_I1I2I3I4 where Ik = (a_{2k-1}, a_{2k}).
# Then S = E * E * R * R * R * R contracted over I and J indices.
#
# E_I1I2I3I4 = eps_{a1,a2,...,a8} * (normalization for ordering within pairs)
# When a1<a2, a3<a4, etc., and I1<I2<I3<I4 in some ordering:
# E is related to the 4-form part of the exterior algebra on Lambda^2.
# This is getting complicated. Let me just do the brute force over permutations.

# For 8D, iterating over S_8 x S_8 is 40320^2 ~ 1.6e9 — too slow.
# But iterating over S_8 once and computing the partial contraction is feasible.

# Define: T[b1,...,b8] = sum_{a in S_8} sgn(a) * R[a0,a1,b0,b1] * R[a2,a3,b2,b3] * R[a4,a5,b4,b5] * R[a6,a7,b6,b7]
# Then S = sum_{b in S_8} sgn(b) * T[b0,...,b7]
# But T has 8^8 entries, and computing each requires 40320 terms.
# That's 40320 * 8^8 ~ 6.7e11 operations. Way too slow.

# Instead: partial contraction approach.
# Define: A[c,d,e,f,g,h, i,j] = sum_{a,b} eps[a,b,c,d,e,f,g,h] * R[a,b,i,j]
# This is 8^8 entries but the eps makes most zero.
# For fixed (c,d,e,f,g,h), eps is nonzero only when (a,b,c,d,e,f,g,h) is a permutation of (0,...,7).
# So a,b are determined by c,...,h: they're the two missing values.
# So A is really a mapping: given 6 distinct values from {0,...,7}, determine the missing 2.

# Even simpler: use numpy einsum with chunks.
# S = eps_A * eps_B * R_{A1 B1} * R_{A2 B2} * R_{A3 B3} * R_{A4 B4}
# = eps_A * eps_B * RRRR
#
# Step 1: T1_{c d e f g h, i j} = sum_{a b} eps_{a b c d e f g h} R_{a b i j}
# This is eps contracted on first 2 indices with R's first 2.
#
# Actually, eps_{abcdefgh} is antisymmetric in ALL indices.
# sum_{a,b} eps_{a,b,c,d,e,f,g,h} * R_{a,b,i,j}
# For this to be nonzero, we need (a,b) to be a pair NOT in {c,d,e,f,g,h}.
# Since all 8 values must be distinct (else eps=0), (a,b) is determined.
# BUT the order matters: eps with (a,b) vs (b,a) differs by sign, and R_{ab,ij} = -R_{ba,ij}.
# So the sum over (a,b) gives 2 * eps_{a0,b0,...} * R_{a0,b0,i,j} where (a0,b0) is the
# canonical ordering (a0 < b0).

# Actually, let me just use numpy directly.
# T1_{cdefgh,ij} = einsum('abcdefgh,abij->cdefghij', eps8, R_SU3)
# This creates a rank-8 tensor (8^6 * 8^2 = 2^18 * ... actually 8^8 = 16M floats = 128MB.
# That's manageable.

print("Step 1: Contract eps with first R factor...")
# T1_{cdefghij} = eps_{ab cdefgh} * R_{ab ij}
# einsum: 'abcdefgh,abij->cdefghij'
T1 = np.einsum('abcdefgh,abij->cdefghij', eps8, R_SU3)
print(f"  T1 shape: {T1.shape}, max |T1|: {np.max(np.abs(T1)):.6e}")

print("Step 2: Contract T1 with second R factor...")
# T2_{efghklij} = T1_{cd efgh ij} * R_{cd kl}
# Wait, I need to be more careful about which indices go where.
#
# After step 1: T1[c,d,e,f,g,h,i,j] = sum_{a,b} eps[a,b,c,d,e,f,g,h] * R[a,b,i,j]
#
# Now contract with R[c,d,k,l]:
# T2[e,f,g,h,i,j,k,l] = sum_{c,d} T1[c,d,e,f,g,h,i,j] * R[c,d,k,l]
# einsum: 'cdefghij,cdkl->efghijkl'
T2 = np.einsum('cdefghij,cdkl->efghijkl', T1, R_SU3)
del T1  # free memory
print(f"  T2 shape: {T2.shape}, max |T2|: {np.max(np.abs(T2)):.6e}")

print("Step 3: Contract T2 with third R factor...")
# T3[g,h,i,j,k,l,m,n] = sum_{e,f} T2[e,f,g,h,i,j,k,l] * R[e,f,m,n]
T3 = np.einsum('efghijkl,efmn->ghijklmn', T2, R_SU3)
del T2
print(f"  T3 shape: {T3.shape}, max |T3|: {np.max(np.abs(T3)):.6e}")

print("Step 4: Contract T3 with fourth R factor...")
# T4[i,j,k,l,m,n,o,p] = sum_{g,h} T3[g,h,i,j,k,l,m,n] * R[g,h,o,p]
T4 = np.einsum('ghijklmn,ghop->ijklmnop', T3, R_SU3)
del T3
print(f"  T4 shape: {T4.shape}, max |T4|: {np.max(np.abs(T4)):.6e}")

print("Step 5: Contract T4 with second epsilon...")
# S = sum_{i,j,k,l,m,n,o,p} eps[i,j,k,l,m,n,o,p] * T4[i,j,k,l,m,n,o,p]
S_SU3 = np.einsum('ijklmnop,ijklmnop', eps8, T4)
del T4
print(f"\nS(SU(3)) = {S_SU3:.15e}")
print(f"S / 6144 = {S_SU3 / 6144:.15e}")
print(f"Expected: 0 (chi = 0)")

# =====================================================================
# Cross-check: S^8 via same method
# =====================================================================
print("\n--- 8D: Cross-check with S^8 ---")

R_S8 = np.zeros((8, 8, 8, 8))
for a in range(8):
    for b in range(8):
        for c in range(8):
            for dd in range(8):
                R_S8[a,b,c,dd] = float(a==c)*float(b==dd) - float(a==dd)*float(b==c)

T1 = np.einsum('abcdefgh,abij->cdefghij', eps8, R_S8)
T2 = np.einsum('cdefghij,cdkl->efghijkl', T1, R_S8)
del T1
T3 = np.einsum('efghijkl,efmn->ghijklmn', T2, R_S8)
del T2
T4 = np.einsum('ghijklmn,ghop->ijklmnop', T3, R_S8)
del T3
S_S8 = np.einsum('ijklmnop,ijklmnop', eps8, T4)
del T4

print(f"S(S^8) = {S_S8:.6f}")
print(f"S / 6144 = {S_S8 / 6144:.6f}")
print(f"chi(S^8) via S/(6144*(2pi)^4)*Vol = {S_S8 / (6144 * (2*np.pi)**4) * 32*np.pi**4/105:.6f} (expected 2)")

# =====================================================================
# Now do stored R at tau=0 to compare
# =====================================================================
print("\n--- 8D: Stored R at tau=0 ---")
d = np.load('C:/sandbox/Ainulindale Exflation/tier0-computation/r20a_riemann_tensor.npz',
            allow_pickle=True)
R_stored = d['R_abcd'][0]

T1 = np.einsum('abcdefgh,abij->cdefghij', eps8, R_stored)
T2 = np.einsum('cdefghij,cdkl->efghijkl', T1, R_stored)
del T1
T3 = np.einsum('efghijkl,efmn->ghijklmn', T2, R_stored)
del T2
T4 = np.einsum('ghijklmn,ghop->ijklmnop', T3, R_stored)
del T3
S_stored = np.einsum('ijklmnop,ijklmnop', eps8, T4)
del T4

print(f"S(stored, tau=0) = {S_stored:.15e}")
print(f"S / 6144 = {S_stored / 6144:.15e}")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"S(S^4, brute force):    {S_test1:.6f}  (chi via formula: {S_test1/48:.6f}, expected 2)")
print(f"S(U2, brute force):     {S_test2:.10e}  (expected 0)")
print(f"S(SU(3), analytic):     {S_SU3:.15e}")
print(f"S(SU(3), stored):       {S_stored:.15e}")
print(f"S(S^8):                 {S_S8:.6f}")
print(f"\nPartition sum (= S/6144):")
print(f"  SU(3) analytic:       {S_SU3/6144:.15e}")
print(f"  SU(3) stored:         {S_stored/6144:.15e}")
print(f"  S^8:                  {S_S8/6144:.6f} (expected 105)")
