"""
Debug script: Verify the Gauss-Bonnet / Euler density computation.
Key question: is our partition formula correct?
Cross-check: use a completely different computation method (brute force via Levi-Civita).
"""

import numpy as np
from itertools import permutations

d = np.load('C:/sandbox/Ainulindale Exflation/tier0-computation/r20a_riemann_tensor.npz', allow_pickle=True)
R0 = d['R_abcd'][0]  # tau=0, round SU(3)

# ============================================================================
# METHOD 1: Partition-based (from main script)
# ============================================================================
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

partitions = list(partitions_into_pairs(list(range(8))))
print(f"Number of partitions: {len(partitions)}")

partition_signs = []
for part in partitions:
    perm = []
    for a, b in part:
        perm.extend([a, b])
    partition_signs.append(perm_sign(perm))

# Partition sum
part_sum = 0.0
for pi_idx, pi_part in enumerate(partitions):
    sgn_i = partition_signs[pi_idx]
    for pj_idx, pj_part in enumerate(partitions):
        sgn_j = partition_signs[pj_idx]
        prod = 1.0
        for k in range(4):
            a1, a2 = pi_part[k]
            b1, b2 = pj_part[k]
            prod *= R0[a1, a2, b1, b2]
        part_sum += sgn_i * sgn_j * prod

print(f"Partition sum: {part_sum:.15e}")
print(f"Euler density (method 1) = 384 * partition_sum = {384 * part_sum:.15e}")

# ============================================================================
# METHOD 2: Direct epsilon contraction (brute force, a subset)
# ============================================================================
# For speed, use the fact that the epsilon tensor is nonzero only for permutations.
# Full sum: 8!^2 = 1.6 billion terms. Too slow for brute force.
# But we can use a smarter approach with the 28x28 curvature matrix.

# Actually, let me use a small matrix method.
# The Euler density in 2n=8 can be written as:
# E = Pf(Omega) where Omega is the curvature 2-form matrix.
#
# Omega^a_b = (1/2) R^a_{bcd} e^c ^ e^d
# In ON frame: Omega^a_b_{cd} = (1/2)(R_{abcd} - R_{abdc}) = R_{abcd} (antisymmetry already)
# Wait, the curvature 2-form has 2-form indices cd AND matrix indices ab.
# Omega is an 8x8 matrix of 2-forms, or equivalently a 2-form with values in so(8).
#
# As a map: Lambda^2(R^8) -> so(8), or equivalently as a (28x28) matrix:
# M_{[ab],[cd]} = R_{abcd} where [ab] with a<b labels the 28 bivectors.
# This matrix is SYMMETRIC (from R_{abcd} = R_{cdab}).
#
# The Pfaffian of the curvature form:
# For the Euler density, we compute the Pfaffian of the so(8)-valued curvature 2-form.
# This is NOT the Pfaffian of the 28x28 symmetric matrix.
#
# The correct computation involves the "Pfaffian of a matrix of 2-forms":
# Pf(Omega) = (1/(n! * 2^n)) * epsilon_{a1...a_{2n}} * Omega^{a1a2} ^ Omega^{a3a4} ^ ... ^ Omega^{a_{2n-1}a_{2n}}
#
# where Omega^{ab} is the curvature 2-form (antisymmetric in a,b since it's so(8)-valued).
# Each Omega^{ab} = (1/2) R^{ab}_{cd} e^c ^ e^d = R^{ab}_{cd} for c<d.
# The wedge product of 4 two-forms on an 8-manifold gives a number:
# Omega^{a1a2} ^ Omega^{a3a4} ^ Omega^{a5a6} ^ Omega^{a7a8}
#   = sum over permutations of (c1c2)(c3c4)(c5c6)(c7c8)...
#   but actually on an 8-manifold, the top form has just one component.
#   e^{c1}^e^{c2}^...^e^{c8} = epsilon^{c1...c8} * vol_8
#
# So:
# Omega^{a1a2} ^ Omega^{a3a4} ^ Omega^{a5a6} ^ Omega^{a7a8}
#   = sum R^{a1a2}_{c1c2} R^{a3a4}_{c3c4} R^{a5a6}_{c5c6} R^{a7a8}_{c7c8} * e^{c1}^...^e^{c8}
#   (here each R_{cd} with c<d, factor 1/2 x 4 copies... need to be careful)
#
# Actually more precisely:
# Omega^{ab} = (1/2) R^{ab}_{cd} e^c ^ e^d (sum over all c,d)
# = R^{ab}_{cd} e^c ^ e^d (for c < d, because of antisymmetry in cd)
#
# Omega^{a1a2} ^ ... ^ Omega^{a7a8} = product of 4 such 2-forms:
# = sum_{c1<d1,...,c4<d4} R^{a1a2}_{c1d1} R^{a3a4}_{c2d2} R^{a5a6}_{c3d3} R^{a7a8}_{c4d4}
#   * e^{c1} ^ e^{d1} ^ e^{c2} ^ e^{d2} ^ e^{c3} ^ e^{d3} ^ e^{c4} ^ e^{d4}
#
# The 8-form: e^{c1}^e^{d1}^e^{c2}^e^{d2}^e^{c3}^e^{d3}^e^{c4}^e^{d4}
# = epsilon^{c1 d1 c2 d2 c3 d3 c4 d4} * vol_8
# (nonzero only when (c1,d1,c2,d2,c3,d3,c4,d4) is a permutation of (0,...,7))
#
# So:
# Pf(Omega) = (1/(4! * 2^4)) epsilon_{a1...a8} * sum_{sigma} epsilon^{sigma}
#             * R^{a1a2}_{sigma(0)sigma(1)} R^{a3a4}_{sigma(2)sigma(3)} ...
#
# In ON frame R^{ab}_{cd} = R_{abcd}.
#
# Pf(Omega) = (1/(4! * 2^4)) * epsilon_{a1...a8} * epsilon_{c1 d1 c2 d2 c3 d3 c4 d4}
#             * R_{a1a2,c1d1} R_{a3a4,c2d2} R_{a5a6,c3d3} R_{a7a8,c4d4}
#             (sum over partitions of {0..7} into ordered pairs for both a and c/d indices)
#
# Wait, in the expression for Pf(Omega), epsilon_{a1...a8} contracts with the so(8) indices
# of the 4 copies of Omega, while the wedge product gives epsilon for the form indices.
#
# So: Pf(Omega) * vol_8 = (1/(4! * 2^4)) * epsilon_{a1...a8} * Omega^{a1a2} ^ ... ^ Omega^{a7a8}
# = (1/384) * epsilon_{a1...a8} * epsilon_{c1...c8} * R_{a1a2,c1c2} * ... * R_{a7a8,c7c8}
# where I used Omega^{ab} ^ ... giving epsilon in the c-indices.
#
# Wait, this is only ONE epsilon, not two! Let me be precise.
#
# The wedge product expansion:
# Omega^{a1a2} ^ Omega^{a3a4} ^ Omega^{a5a6} ^ Omega^{a7a8}
# = sum over ordered (c1<d1), (c2<d2), (c3<d3), (c4<d4) that form a perm of {0..7}:
#   epsilon_perm * R_{a1a2,c1d1} R_{a3a4,c2d2} R_{a5a6,c3d3} R_{a7a8,c4d4}
# where epsilon_perm = sign of (c1,d1,c2,d2,...,c4,d4) as a permutation of (0,...,7).
#
# In partition notation: = sum_{partitions pj} sgn(pj) * prod_k R_{a_{2k-1}a_{2k}, pj_k}
# where the sum has 105 terms (pair partitions) and sgn(pj) = sign of concatenated permutation.
# Correction: need to account for the factor from going to ordered pairs. Each partition
# with pairs (c<d) represents 2^4 permutations with the same |R| product (antisymmetry of R
# flips sign). But the epsilon also flips sign for each pair swap, so the net factor =
# 2^4 (from pair swaps, each giving (-1)*(-1) = +1) * 4! (from pair reordering).
# Actually no -- the wedge product is already antisymmetric, so pair ordering matters.
# Let me just use the ordered-pair formula:
# Sum = 2^4 * 4! * sum_{partitions pj} sgn(pj) * prod_k R_{a1a2, pj_k}  -- for each fixed a-partition.
# NO -- the factor arises differently. Let me just trust the partition formula and verify numerically.

# CROSS-CHECK: Compute using the Pfaffian of the 8x8 antisymmetric "curvature matrix"
# defined as follows. In 8D, the curvature 2-form Omega^a_b has two matrix indices (a,b)
# that are in so(8) (antisymmetric). The "flat" representation is to think of Omega as a
# single 2-form, and the Pfaffian in the so(8) sense involves the epsilon tensor.
#
# For a direct numerical check, let me try yet another approach:
# construct the 8x8 matrix A_{ab} = (1/2) epsilon_{abcdefgh} R_{cdef} R_{gh??}
# No, this doesn't work dimensionally.
#
# Let me try the simplest check: verify that on a 4-sphere (or use a known 8D result).
# Instead, let me verify analytically for round SU(3).

# For ROUND SU(3) (bi-invariant metric), the Riemann tensor is:
# R_{abcd} = (K/4) (g_{ac}g_{bd} - g_{ad}g_{bc})
# where K is the sectional curvature. For our normalization, R = 2, dim = 8,
# so R_{abcd} = (R/(d(d-1))) * (delta_{ac}*delta_{bd} - delta_{ad}*delta_{bc})
# Wait, for constant sectional curvature K: R_{abcd} = K(g_{ac}g_{bd} - g_{ad}g_{bc})
# => Ric_{ab} = (d-1)*K*g_{ab}, R = d*(d-1)*K. So K = R/(d*(d-1)) = 2/(8*7) = 1/28.

# But SU(3) does NOT have constant sectional curvature! (Only spheres do in 8D.)
# It has a more complex structure. So this simplification won't work.

# Let me just try a MUCH simpler topological check that doesn't require the full Euler computation.

# ============================================================================
# SIMPLER TOPOLOGICAL CHECK: Pontryagin class p_1
# ============================================================================
# For a 4k-manifold, the Pontryagin number is topological.
# p_1 = -(1/(8pi^2)) integral Tr(R^2) dvol_4 (for a 4-manifold)
# For our 8-manifold, we need the integral of p_1 ^ p_1 = (Tr R^2)^2 contribution.
# But p_1 is a 4-form, and its integral over M^8 is zero (wrong degree).
# The relevant invariant is p_2 or the Euler class.

# Let me try the Hirzebruch signature for 8-manifolds:
# sigma(M^8) = (1/45) integral (7p_2 - p_1^2)
# This is topological.

# OK, I realize there is a much simpler approach to the P0-5 check.
# The PROMPT says to use the formula E_4 = (1/8pi^2)(|Riem|^2 - 4|Ric|^2 + R^2).
# This is the 4D Gauss-Bonnet formula, NOT the 8D one.
# In 8D, this combination is NOT topological.
# But we can still use it as a DATA INTEGRITY check: if the Riemann tensor is
# computed consistently, the curvature invariants should obey specific algebraic
# identities that are dimension-independent.

# The REAL purpose of P0-5 is to validate the Riemann tensor data.
# We can do this by checking:
# 1. Symmetries (already verified to machine epsilon) - PASS
# 2. Bianchi identity (already verified) - PASS
# 3. Kretschner consistency with stored values - PASS
# 4. Ricci contraction consistency - need to resolve sign convention
# 5. Known values at tau=0 (round SU(3) is well-known)

# Let me do check 5: verify R_{abcd} at tau=0 against the analytic formula.
# For a bi-invariant metric on a compact Lie group G, in ON frame:
# R_{abcd} = -(1/4) f_{abe} f_{cde}  (summed over e)
# where f_{abc} are structure constants in the ON basis.

# For our SU(3) with g_0 = 3*B (B = -Killing form, so g_0 = -3*Killing):
# In ON frame: e_a = sqrt(3) * lambda_a (Gell-Mann generators)
# [e_a, e_b] = sqrt(3) f_{abc} e_c
# where f_{abc} are the standard SU(3) structure constants.
# Wait, the ON frame diagonalizes g_0 = 3*I, so e_a = (1/sqrt(3)) * tilde_lambda_a
# where tilde_lambda are the generators with [tilde_lambda_a, tilde_lambda_b] = f_{abc} tilde_lambda_c.
# In ON basis: [e_a, e_b] = f_{abc}/sqrt(3) * e_c... no this is getting confused.

# Let me just verify numerically. The structure constants of SU(3) satisfy:
# f_{123} = 1, f_{147} = f_{165} = f_{246} = f_{257} = f_{345} = f_{376} = 1/2,
# f_{458} = f_{678} = sqrt(3)/2 (standard Gell-Mann convention).
# But our basis might differ.

# Let me extract f_{abc} from R at tau=0 using R_{abcd} = -(1/4) sum_e f_{abe} f_{cde} (or + with our convention).
# Actually, with our sign: Ric = R_{cabc} (positive), so:
# Ric_{ab} = sum_c R_{cabc} = +(1/4) sum_{c,e} f_{cae} f_{cbe} = (1/4) C_2 delta_{ab}
# where C_2 is the quadratic Casimir in the adjoint. For SU(3), C_2(adj) = 3.
# So Ric_{ab} = (1/4) * 3 * delta_{ab} = 0.75 * delta_{ab}.
# But stored Ric = 0.25 * I. Factor of 3 off!

# The issue is the metric normalization. g_0 = 3*I means our ON frame has
# e_a = (1/sqrt(3)) * X_a where X_a satisfy [X_a, X_b] = f_{abc} X_c.
# Then [e_a, e_b] = (1/3) f_{abc} X_c = (1/sqrt(3)) f_{abc} e_c.
# So the ON structure constants are f_ON_{abc} = f_{abc}/sqrt(3).
# R_{abcd} = +(1/4) sum_e f_ON_{abe} f_ON_{cde} = (1/4) * (1/3) sum_e f_{abe} f_{cde}
# = (1/12) sum_e f_{abe} f_{cde}
# Ric_{ab} = sum_c R_{cabc} = (1/12) sum_{c,e} f_{cae} f_{cbe} = (1/12) * C_2(adj) * delta_{ab}
# = (1/12) * 3 * delta_{ab} = 0.25 * delta_{ab}. MATCHES!

# Great. So R_{abcd} at tau=0 should satisfy:
# R_{abcd} = (1/12) sum_e f_{abe} f_{cde}
# where f_{abc} are standard SU(3) structure constants.
# Let me verify R_{0,1,0,1}:
# R_{0101} = (1/12) sum_e f_{01e} f_{01e} = (1/12) sum_e f_{01e}^2
# For Gell-Mann: f_{123} = 1 (if indices are 1-based) => f_{012} = 1 (0-based).
# So f_{01e} != 0 only for e=2: f_{012} = 1.
# R_{0101} = (1/12) * 1 = 0.0833...
# BUT stored R[0,1,0,1] = -0.0833!

# So the stored tensor has OPPOSITE SIGN: R_stored = -R_standard.
# This is consistent with the contraction: Ric = -R_stored_{cacb} = R_{cacb}.
# And Ric = R_stored_{cabc} because R_stored_{cabc} = -R_standard_{cabc} = +Ric
# (since R_standard_{cabc} = -R_standard_{cacb} = -Ric, wait that's wrong...)

# Hmm, let me be careful.
# Standard convention (R > 0 for sphere):
# R_std_{abcd} = (1/12) f_{abe} f_{cde}  (for our normalization)
# Ric_std_{ab} = R_std_{cacb} = (1/12) sum_{c,e} f_{cae} f_{cbe} = 0.25 * I

# With R_stored = -R_std:
# R_stored_{cacb} = -R_std_{cacb} = -0.25 * I
# R_stored_{cabc} = -R_std_{cabc}
# But R_std_{cabc} = -R_std_{cacb} (antisymmetry in 3rd and 4th indices)
# = -0.25 * I. Wait: R_std_{cabc} = -R_std_{cabc}??? No.
# R_std_{cabc}: contract c with positions 0,3. Sum over c: sum_c R_std[c,a,b,c].
# R_std[c,a,b,c] = R_std_{cabc}. By antisymmetry in cd: R_{cabc} = -R_{cabk}... no, antisymmetry is in (c,d) meaning positions (2,3).
# R_std_{cabc}: positions are (0=c, 1=a, 2=b, 3=c). Antisymmetry in positions (0,1): R_{cabc} = -R_{acbc}.
# And antisymmetry in positions (2,3): R_{cabc} = -R_{cacb}.
# So R_stored_{cabc} = -R_std_{cabc} = -(-R_std_{cacb}) = R_std_{cacb} = +Ric. YES!

# So: R_stored = -R_standard (where standard = positive sectional curvature on sphere).
# This is a common alternative convention (used e.g. by Penrose, d'Inverno).
# For the Euler density computation, since it involves R^4, the sign cancels.

# But the FORMULA for the Euler density must use the same convention consistently.
# The Gauss-Bonnet-Chern formula is:
# chi = (1/Omega_{2n}) * integral Pf(Omega)
# where Pf(Omega) is defined with ONE epsilon (not two) and one factor of (-1)^n.

# For 2n = 8, n = 4:
# chi = integral (1/(2^4 * 4! * (2pi)^4)) * epsilon_{a1..a8} * R_{a1a2,c1c2} * R_{a3a4,c3c4} * R_{a5a6,c5c6} * R_{a7a8,c7c8} * epsilon^{c1..c8}
# = (1 / (384 * (2pi)^4)) * epsilon * epsilon * R^4

# Hmm, but this has TWO epsilons. Let me look up the precise formula.

# From Nakahara "Geometry, Topology and Physics", the Euler class in 2n=8:
# chi(M) = (1/(2pi)^4) integral e(M)
# e(M) = Pf(Omega/(2pi)) where Omega is the curvature 2-form.
# For an SO(8) bundle:
# Pf(Omega) = (1/(2^4 * 4!)) * epsilon_{a1..a8} * Omega^{a1a2} ^ Omega^{a3a4} ^ Omega^{a5a6} ^ Omega^{a7a8}
#
# Now Omega^{ab} = (1/2) R^{ab}_{cd} e^c ^ e^d (antisymmetric in a,b and in c,d).
# In our convention: R^{ab}_{cd} = R_{stored,abcd} (raising with delta in ON frame).
#
# The 4-fold wedge product:
# Omega^{a1a2} ^ Omega^{a3a4} ^ Omega^{a5a6} ^ Omega^{a7a8}
# = (1/2)^4 * sum_{c,d indices} R_{a1a2,c1d1} R_{a3a4,c2d2} R_{a5a6,c3d3} R_{a7a8,c4d4}
#   * e^{c1}^e^{d1}^e^{c2}^e^{d2}^e^{c3}^e^{d3}^e^{c4}^e^{d4}
# = (1/16) * sum R R R R * epsilon_{c1d1c2d2c3d3c4d4} * vol_8
#
# So Pf(Omega) = (1/(384)) * epsilon_{a1..a8} * (1/16) * sum_{c-perms} epsilon_{c-perm} * R R R R * vol_8
# = (1/6144) * epsilon_a * epsilon_c * R R R R * vol_8
#
# And chi = (1/(2pi)^4) * integral Pf(Omega)
# = (1/(2pi)^4) * (1/6144) * S * Vol
# where S = sum_{a-perm, c-perm} sgn(a) sgn(c) R_{a1a2,c1c2} ... R_{a7a8,c7c8}
# = (2^4 * 4!)^2 * partition_sum = 147456 * partition_sum
#
# chi = (1/(2pi)^4) * (1/6144) * 147456 * partition_sum * Vol
# = (1/(2pi)^4) * 24 * partition_sum * Vol
# = 24 * partition_sum * Vol / (16 pi^4)
# = (3/(2 pi^4)) * partition_sum * Vol

# For chi(SU(3)) = 0: partition_sum must be 0 (Vol > 0).
# Our partition_sum at tau=0 = euler_density / 384 = 0.0677 / 384 = 1.76e-4.
# This is NOT zero.

# HOWEVER: the formula I wrote might not account for the pairing correctly.
# In the partition sum, each pair represents ORDERED indices (a1,a2) with a1<a2.
# But in the full sum over all 8! permutations, each (a1,a2) can have either order.
# The factor 2^4 from within-pair swaps: each swap gives (-1) from epsilon AND (-1) from
# R_{abcd} antisymmetry, net factor +1. So within-pair reordering is accounted for.
# The factor 4! from pair reordering: reordering pairs (a1a2)(a3a4)(a5a6)(a7a8) ->
# (a3a4)(a1a2)(a5a6)(a7a8) changes the epsilon sign by the pair permutation sign.
# But it also re-associates which R factor goes with which pair.
# In our partition sum, the k-th pair of partition i is always contracted with the k-th pair
# of partition j. If we reorder the pairs of partition i, we should also reorder the pairs
# of partition j (since each pair is bound to its position in the product).
# But our independent summation over all partitions for i and j already covers all orderings.
# So the factor should be (2^4)^2 from within-pair swaps = 256, NOT (2^4 * 4!)^2.

# Wait, this is the crux. Let me think again.
# The full sum S = sum over sigma_i, sigma_j in S_8:
#   sgn(sigma_i) sgn(sigma_j) R_{sigma_i(0)sigma_i(1),sigma_j(0)sigma_j(1)} * ... * R_{sigma_i(6)sigma_i(7),sigma_j(6)sigma_j(7)}
#
# Each permutation sigma_i can be decomposed as:
# (1) Choose a pair-partition P_i (105 choices)
# (2) Choose an ordering of pairs in P_i (4! choices)
# (3) Choose an orientation within each pair (2^4 choices)
# Total: 105 * 24 * 16 = 40320 = 8!. Correct.
#
# For a fixed pair-partition P_i and a fixed pair-partition P_j:
# - Pair reordering of P_i: changes sgn(sigma_i) by the sign of the pair permutation.
#   Also changes which R factors we multiply: R_{P_i(k),P_j(k)} becomes R_{P_i(tau(k)),P_j(k)}.
#   This is NOT the same product for general P_j! So pair reorderings of P_i are NOT
#   trivially accounted for.
#
# My partition formula sums:
# M = sum_{P_i, P_j} sgn(P_i) sgn(P_j) prod_{k=0}^3 R_{P_i[k], P_j[k]}
#
# The full sum S relates to M as:
# S = sum_{sigma_i, sigma_j} sgn(sigma_i) sgn(sigma_j) prod_{k=0}^3 R_{sigma_i(2k:2k+2), sigma_j(2k:2k+2)}
#
# Decompose sigma_i into (P_i, within-pair swaps, pair reordering).
# Within-pair swaps: R_{ba,cd} = -R_{ab,cd} and epsilon flips, net +1. Factor: 2^4 for sigma_i, 2^4 for sigma_j.
# Pair reordering tau of P_i: sigma_i(2k:2k+2) = P_i[tau(k)].
#   So prod_k R_{P_i[tau(k)], P_j[k]} = prod_k R_{P_i[tau(k)], P_j[k]}.
#   This is NOT the same as prod_k R_{P_i[k], P_j[k]} unless P_j is also reordered.
#
# So the pair reordering factor does NOT simply multiply M.
# We need: S = 256 * sum_{P_i, P_j} sum_{tau in S_4} sgn(tau) prod_k R_{P_i[tau(k)], P_j[k]}
# Wait actually the sgn decomposition is:
# sgn(sigma_i) = sgn(P_i) * sgn(tau) * 1  (within-pair swaps don't change overall sign because... actually they do)
#
# Let me just directly verify with a small example. Let me take n=4 (2 copies of R) and verify
# the 4D Gauss-Bonnet formula.

# SIMPLER: just verify that my code gives the right answer for a sphere.
# For S^8 with constant sectional curvature K:
# R_{abcd} = K (delta_{ac} delta_{bd} - delta_{ad} delta_{bc})
# chi(S^8) = 2.
# Let me plug this in.

K_sphere = 1.0  # arbitrary (chi is topological)
R_sphere = np.zeros((8, 8, 8, 8))
for a in range(8):
    for b in range(8):
        for c in range(8):
            for dd in range(8):
                R_sphere[a, b, c, dd] = K_sphere * (
                    (1 if a == c else 0) * (1 if b == dd else 0) -
                    (1 if a == dd else 0) * (1 if b == c else 0)
                )

# Verify symmetries
print("\nSphere Riemann symmetries:")
print(f"  R_sphere[0,1,0,1] = {R_sphere[0,1,0,1]}")
print(f"  R_sphere[0,1,1,0] = {R_sphere[0,1,1,0]}")
print(f"  Antisym ab: {np.max(np.abs(R_sphere + np.transpose(R_sphere, (1,0,2,3))))}")
print(f"  Antisym cd: {np.max(np.abs(R_sphere + np.transpose(R_sphere, (0,1,3,2))))}")
print(f"  Pair sym: {np.max(np.abs(R_sphere - np.transpose(R_sphere, (2,3,0,1))))}")

# Compute partition sum for sphere
part_sum_sphere = 0.0
for pi_idx, pi_part in enumerate(partitions):
    sgn_i = partition_signs[pi_idx]
    for pj_idx, pj_part in enumerate(partitions):
        sgn_j = partition_signs[pj_idx]
        prod = 1.0
        for k in range(4):
            a1, a2 = pi_part[k]
            b1, b2 = pj_part[k]
            prod *= R_sphere[a1, a2, b1, b2]
        part_sum_sphere += sgn_i * sgn_j * prod

print(f"\nSphere partition sum: {part_sum_sphere}")
print(f"Sphere 384 * partition_sum: {384 * part_sum_sphere}")

# For S^8 with K=1:
# |Riem|^2 = 2*d*(d-1) = 2*8*7 = 112
# |Ric|^2 = d*(d-1)^2 = 8*49 = 392
# R = d*(d-1) = 56, R^2 = 3136
# The 8D Euler number chi(S^8) = 2.
# With vol(S^8) = 32*pi^4/105 * (for unit sphere):
# chi = (normalization) * partition_sum * vol
# We should find partition_sum proportional to chi/vol.
K_sph = np.sum(R_sphere**2)
Ric_sph = np.einsum('cabc->ab', R_sphere)  # our convention
R_sph = np.trace(Ric_sph)
print(f"\nSphere check: |Riem|^2 = {K_sph}, |Ric|^2 = {np.sum(Ric_sph**2)}, R = {R_sph}, R^2 = {R_sph**2}")
print(f"Expected for K=1, d=8: |Riem|^2=112, |Ric|^2=392, R=56")

# The Ricci for our convention: Ric = R_{cabc}
# For sphere: R_{cabc} = K(delta_cc * delta_ab - delta_cb * delta_ac) summed over c
# = K(8*delta_ab - delta_ab) = 7K * delta_ab
# So Ric_{ab} = 7*K*delta_{ab}. R = 8*7*K = 56K. Matches.

# For chi(S^8) = 2 with K=1:
# From Chern-Gauss-Bonnet: chi = integral E_4 dvol
# E_4 = (1/(2^4 * 4! * (2pi)^4)) * epsilon * epsilon * R^4
#
# For constant curvature, E_4 is a constant, so chi = E_4 * Vol(S^8).
# Vol(S^8, K=1) = 32*pi^4/105 (volume of unit 8-sphere).
# Note: this is the sphere of radius 1 embedded in R^9, which has K=1.
# Actually Vol(S^n) = 2*pi^{(n+1)/2} / Gamma((n+1)/2).
# Vol(S^8) = 2*pi^{9/2}/Gamma(9/2) = 2*pi^{9/2}/(105*sqrt(pi)/16) = 32*pi^4/105.

vol_S8 = 32 * np.pi**4 / 105
print(f"\nVol(S^8) = {vol_S8:.6f}")

# chi = 2 => E_4 = 2 / vol_S8 = 2 * 105 / (32 pi^4) = 210 / (32 pi^4)
E4_expected = 2.0 / vol_S8
print(f"Expected E_4 density for chi=2: {E4_expected:.10f}")

# Our computation: partition_sum = part_sum_sphere, euler_density = 384 * part_sum_sphere
# E_4 (our convention) = euler_density / normalization_factor
# We need: E_4 * Vol = chi
# => normalization = euler_density * Vol / chi
# = 384 * part_sum_sphere * vol_S8 / 2
normalization = 384 * part_sum_sphere * vol_S8 / 2
print(f"\n384 * partition_sum (sphere) = {384 * part_sum_sphere:.6f}")
print(f"Implied normalization factor: {normalization:.6f}")
print(f"= {normalization:.6f} / (2pi)^4 = {normalization / (2*np.pi)**4:.6f}")
print(f"Partition sum * Vol / chi = {part_sum_sphere * vol_S8 / 2:.10f}")
print(f"(2pi)^4 = {(2*np.pi)**4:.6f}")
print()

# So chi = (1/N) * 384 * partition_sum * Vol
# where N = 384 * partition_sum * Vol / chi = normalization
# Let me find N such that chi = (384 / N) * partition_sum * Vol for the sphere.
N = 384 * part_sum_sphere * vol_S8 / 2
print(f"Normalization N such that chi = (384/N) * part_sum * Vol:")
print(f"  N = {N:.6f}")
print(f"  384/N = {384/N:.15f}")
print(f"  Expected: 384/N should be 1/((2pi)^4) if the formula is chi = (1/(2pi)^4) * 384 * sum * vol?")
print(f"  1/(2pi)^4 = {1/(2*np.pi)**4:.15f}")
print(f"  Ratio: (384/N) / (1/(2pi)^4) = {(384/N) * (2*np.pi)**4:.10f}")
