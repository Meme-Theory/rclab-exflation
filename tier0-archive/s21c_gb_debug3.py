"""
Debug part 3: The partition pairing issue.
The partition sum formula pairs k-th pair of partition_i with k-th pair of partition_j.
But the full epsilon*epsilon*RRRR contraction has the pairs of the a-indices and c-indices
independently determined. The issue is whether pair k of the a-partition should always
contract with pair k of the c-partition (position-matched) or whether all pairings
should be independent.

In the full sum:
S = sum_{sigma_a, sigma_c in S_{2n}} sgn(sigma_a) sgn(sigma_c)
    * R_{sigma_a(0)sigma_a(1), sigma_c(0)sigma_c(1)} * ... * R_{sigma_a(2n-2)sigma_a(2n-1), sigma_c(2n-2)sigma_c(2n-1)}

The k-th R factor takes its first index pair from positions (2k, 2k+1) of sigma_a
and its second index pair from positions (2k, 2k+1) of sigma_c.
The position k is FIXED — it's not summed over. So the pairing IS position-matched.

BUT: when we decompose sigma_a into (partition, pair-ordering, within-pair swaps),
the pair-ordering part REORDERS which pair goes in which position.
Similarly for sigma_c.

For partition_a with pairs (P_a[0], P_a[1], ..., P_a[n-1]) and pair-ordering tau_a in S_n:
sigma_a puts P_a[tau_a(0)] in positions (0,1), P_a[tau_a(1)] in positions (2,3), etc.

Similarly sigma_c puts P_c[tau_c(0)] in positions (0,1), etc.

So: prod_k R_{P_a[tau_a(k)], P_c[tau_c(k)]}

The full sum over all sigma_a, sigma_c decomposes as:
S = sum_{P_a, P_c} sum_{tau_a, tau_c in S_n} sum_{flips}
    sgn(P_a)*sgn(tau_a)*sgn_flips * sgn(P_c)*sgn(tau_c)*sgn_flips
    * prod_k R_{P_a[tau_a(k)], P_c[tau_c(k)]}

The flip factor: each pair can be flipped (2^n choices each). R is antisymmetric in each pair,
so flipping gives (-1). Epsilon also flips sign. Net: +1 per flip. Factor: (2^n)^2.

So: S = (2^n)^2 * sum_{P_a, P_c} sgn(P_a) sgn(P_c)
    * sum_{tau_a, tau_c in S_n} sgn(tau_a) sgn(tau_c) * prod_k R_{P_a[tau_a(k)], P_c[tau_c(k)]}

The inner sum over tau_a, tau_c:
sum_{tau_a, tau_c} sgn(tau_a) sgn(tau_c) * prod_k R_{P_a[tau_a(k)], P_c[tau_c(k)]}

This is the PERMANENT-like sum of a matrix M where M_{ij} = R_{P_a[i], P_c[j]},
weighted by sgn(tau_a) sgn(tau_c).

Actually: prod_k R_{P_a[tau_a(k)], P_c[tau_c(k)]} with the sum over tau_a, tau_c.
Define sigma = tau_c . tau_a^{-1}, then tau_c = sigma . tau_a.
Sum over tau_a, sigma: sgn(tau_a) sgn(sigma . tau_a) = sgn(tau_a)^2 * sgn(sigma) = sgn(sigma).
Product: prod_k R_{P_a[tau_a(k)], P_c[sigma(tau_a(k))]}
       = prod_k R_{P_a[k], P_c[sigma(k)]}  (relabeling tau_a(k) -> k)
Multiplied by n! (from the sum over tau_a with constant value for each sigma).

So: inner sum = n! * sum_{sigma in S_n} sgn(sigma) * prod_k R_{P_a[k], P_c[sigma(k)]}
             = n! * det(M)
where M_{kl} = R_{P_a[k], P_c[l]}.

THIS IS THE KEY! The inner sum is n! * det(M), not just the diagonal product.

My partition formula used only the DIAGONAL of M (sigma = identity):
my_sum = prod_k R_{P_a[k], P_c[k]}

But the CORRECT formula sums over ALL permutations sigma of the pairs:
correct_sum = sum_sigma sgn(sigma) prod_k R_{P_a[k], P_c[sigma(k)]}
            = det(M)

So: S = (2^n)^2 * n! * sum_{P_a, P_c} sgn(P_a) sgn(P_c) * det(M_{P_a, P_c})

And chi = (1/(2pi)^n) * S * Vol / (normalization...)

Wait, but for the sphere S^4 (n=2), my diagonal-only formula gave partition_sum = 3
and chi = (1/(4pi^2)) * 3 * Vol = 2. This was CORRECT.
If the correct formula includes the determinant, for S^4 with n=2:
M is a 2x2 matrix. det(M) = M_{00}M_{11} - M_{01}M_{10}.
For S^4 with constant curvature: R_{[ab],[cd]} = delta_ac*delta_bd - delta_ad*delta_bc.
For partition P_a = [(0,1),(2,3)] and P_c = [(0,1),(2,3)]:
M_{00} = R_{01,01} = 1, M_{01} = R_{01,23} = 0, M_{10} = R_{23,01} = 0, M_{11} = R_{23,23} = 1.
det(M) = 1. Same as diagonal product.

For P_a = [(0,1),(2,3)], P_c = [(0,2),(1,3)]:
M_{00} = R_{01,02} = 0, M_{01} = R_{01,13} = 0, M_{10} = R_{23,02} = 0, M_{11} = R_{23,13} = 0.
det(M) = 0. Same as diagonal product (which was also 0).

So for S^4, diagonal and det give the same answer because cross-terms are zero.
For SU(3), they might differ!
"""

import numpy as np
from itertools import permutations

d = np.load('C:/sandbox/Ainulindale Exflation/tier0-computation/r20a_riemann_tensor.npz', allow_pickle=True)
R0 = d['R_abcd'][0]

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

parts8 = list(partitions_into_pairs(list(range(8))))
psigns8 = [perm_sign([x for pair in p for x in pair]) for p in parts8]
print(f"Partitions of {{0,...,7}}: {len(parts8)}")

# CORRECT formula:
# S = (2^n)^2 * n! * sum_{P_a, P_c} sgn(P_a) sgn(P_c) * det(M_{P_a, P_c})
# where M_{kl} = R_{P_a[k], P_c[l]} (with R_{P_a[k], P_c[l]} meaning R_{a1,a2,c1,c2} for pair k of P_a and pair l of P_c)
#
# But wait: the formula chi = (1/(2pi)^n) * partition_sum * Vol worked for the sphere
# with partition_sum = diagonal-only. For the sphere, det = diagonal because cross-terms vanish.
#
# So for the sphere, the det formula gives the same partition_sum.
# For SU(3), the det formula might give a DIFFERENT result.
#
# My original formula (WRONG for SU(3)):
# partition_sum_wrong = sum_{P_a, P_c} sgn(Pa) sgn(Pc) * prod_k R_{Pa[k], Pc[k]}
#
# Correct formula:
# partition_sum_correct = sum_{P_a, P_c} sgn(Pa) sgn(Pc) * det(M)
# where M_{kl} = R_{Pa[k], Pc[l]}
#
# And S = (2^n)^2 * n! * partition_sum_correct
# chi = (1/(2pi)^n) * (2^n)^2 * n! * partition_sum_correct * Vol / ???
#
# Wait, for the sphere: S = (2^n)^2 * partition_sum_wrong (my formula)
# and chi = (1/(2pi)^n) * partition_sum_wrong * Vol (confirmed numerically).
# With the correct formula:
# S_correct = (2^n)^2 * n! * partition_sum_correct
# and chi = (1/(2pi)^n) * (S_correct / 384^2) * 384 * Vol...
#
# I'm getting confused with the normalization. Let me just redo the derivation carefully.
#
# The FULL sum: S = sum_{sigma, rho in S_8} sgn(sigma) sgn(rho) prod_{k=0}^3 R_{sigma(2k), sigma(2k+1), rho(2k), rho(2k+1)}
#
# Decompose sigma: partition P, pair-order tau in S_4, flips f in (Z_2)^4.
# Similarly rho: partition Q, pair-order mu in S_4, flips g in (Z_2)^4.
#
# prod_k R_{P[tau(k)] with flip f_k, Q[mu(k)] with flip g_k}
# Flips: R_{ba,cd} = -R_{ab,cd}. Each flip introduces (-1) from R and (-1) from sgn(sigma). Net: +1.
# So flips contribute (2^4)^2 = 256 with all signs canceling.
#
# Pair-orders:
# prod_k R_{P[tau(k)], Q[mu(k)]}
# = prod_k R_{P[tau(k)], Q[mu(k)]}
#
# Sum over tau, mu with signs:
# Sum_{tau, mu} sgn(tau) sgn(mu) * prod_k R_{P[tau(k)], Q[mu(k)]}
# Let sigma_pq = mu . tau^{-1}. Then mu = sigma_pq . tau.
# Sum_{tau, sigma_pq} sgn(tau) sgn(sigma_pq . tau) = Sum sgn(sigma_pq) * (Sum_{tau} 1)
# Wait: sgn(mu) = sgn(sigma_pq . tau) = sgn(sigma_pq) * sgn(tau).
# So sgn(tau) * sgn(mu) = sgn(tau) * sgn(sigma_pq) * sgn(tau) = sgn(sigma_pq).
# Product: prod_k R_{P[tau(k)], Q[sigma_pq(tau(k))]}
#        = prod_j R_{P[j], Q[sigma_pq(j)]}  (relabeling j = tau(k))
# This is independent of tau! So sum over tau gives factor n! = 4! = 24.
# And sum over sigma_pq:
# Sum_{sigma_pq in S_4} sgn(sigma_pq) * prod_j R_{P[j], Q[sigma_pq(j)]} = det(M_{PQ})
# where M_{PQ}[j, l] = R_{P[j], Q[l]}.
#
# So: S = 256 * 24 * sum_{P, Q} sgn(P) sgn(Q) * det(M_{PQ})
# = 6144 * corrected_partition_sum
# where corrected_partition_sum = sum_{P, Q} sgn(P) sgn(Q) * det(M_{PQ})
#
# For the sphere: corrected_partition_sum = partition_sum_diagonal (because det = diagonal for constant curvature)
# chi_sphere = (1/(2pi)^4) * 6144 * 3 * Vol_S8 ... hmm this gives a different normalization.
# Wait: partition_sum_sphere = 105 (from diagonal formula).
# corrected_sphere = 105 (det = diagonal for sphere).
# S_sphere = 6144 * 105 = 645120.
# chi = normalization * S * Vol.
#
# For sphere: chi = 2. S = 645120. Vol = 32pi^4/105.
# normalization = 2 / (645120 * 32pi^4/105) = 2 * 105 / (645120 * 32 * pi^4) = 210 / (20643840 * pi^4)
# = 1/(98304 pi^4).
# Is this (1/(2pi)^4) / (something)?
# (2pi)^4 = 16 pi^4. So 1/(98304 pi^4) = 1/(6144 * 16 pi^4) = 1/(6144 * (2pi)^4).
# So chi = S / (6144 * (2pi)^4) * Vol = corrected_ps / ((2pi)^4) * Vol.
# Wait: chi = (1/(6144 * (2pi)^4)) * S * Vol = (1/(6144 * (2pi)^4)) * 6144 * corrected_ps * Vol
# = (1/(2pi)^4) * corrected_ps * Vol.
# Same as before! The 6144 cancels.
# chi = corrected_ps * Vol / (2pi)^4.

# OK so the formula IS: chi = corrected_partition_sum * Vol / (2pi)^n
# where corrected_partition_sum = sum_{P, Q} sgn(P) sgn(Q) * det(M_{PQ}).
# And my ORIGINAL formula used the DIAGONAL only, which equals the det for spheres but NOT for SU(3).

# NOW LET ME COMPUTE THE CORRECTED SUM FOR SU(3).

n = 4  # n = dim/2

print("\nComputing CORRECTED partition sum with det(M) for SU(3) at tau=0...")

tau_vals = d['tau']
R_all = d['R_abcd']

corrected_sums = []
diagonal_sums = []

for ti in range(len(tau_vals)):
    R = R_all[ti]

    corrected_sum = 0.0
    diagonal_sum = 0.0

    for pi_idx, pi_part in enumerate(parts8):
        sgn_i = psigns8[pi_idx]
        for pj_idx, pj_part in enumerate(parts8):
            sgn_j = psigns8[pj_idx]

            # Build n x n matrix M where M[k][l] = R_{P_a[k], P_c[l]}
            M = np.zeros((n, n))
            for k in range(n):
                a1, a2 = pi_part[k]
                for l in range(n):
                    b1, b2 = pj_part[l]
                    M[k, l] = R[a1, a2, b1, b2]

            det_M = np.linalg.det(M)
            corrected_sum += sgn_i * sgn_j * det_M

            # Diagonal-only (my original formula)
            diag_prod = 1.0
            for k in range(n):
                diag_prod *= M[k, k]
            diagonal_sum += sgn_i * sgn_j * diag_prod

    corrected_sums.append(corrected_sum)
    diagonal_sums.append(diagonal_sum)

    if ti % 5 == 0 or ti == len(tau_vals) - 1:
        print(f"  tau={tau_vals[ti]:.2f}: corrected={corrected_sum:.15e}, diagonal={diagonal_sum:.15e}")

corrected_sums = np.array(corrected_sums)
diagonal_sums = np.array(diagonal_sums)

print(f"\n=== CORRECTED PARTITION SUM ===")
print(f"Range: [{corrected_sums.min():.15e}, {corrected_sums.max():.15e}]")
print(f"Max |corrected|: {np.max(np.abs(corrected_sums)):.15e}")
print(f"Corrected sum at tau=0: {corrected_sums[0]:.15e}")

print(f"\n=== DIAGONAL PARTITION SUM (original, WRONG) ===")
print(f"Range: [{diagonal_sums.min():.15e}, {diagonal_sums.max():.15e}]")
print(f"Max |diagonal|: {np.max(np.abs(diagonal_sums)):.15e}")

# Check: is the corrected sum zero (as required by chi(SU(3)) = 0)?
print(f"\n=== TOPOLOGICAL INVARIANCE CHECK ===")
print(f"Max |corrected_sum(tau)|: {np.max(np.abs(corrected_sums)):.15e}")
print(f"This should be 0 for chi(SU(3)) = 0.")

# Also check constancy
if np.max(np.abs(corrected_sums)) > 0:
    max_dev = np.max(np.abs(corrected_sums - corrected_sums[0]))
    print(f"Max |corrected(tau) - corrected(0)|: {max_dev:.15e}")
    if abs(corrected_sums[0]) > 1e-20:
        print(f"Relative: {max_dev/abs(corrected_sums[0]):.15e}")

# Cross-check with sphere
print("\n=== SPHERE CROSS-CHECK ===")
R_sphere = np.zeros((8, 8, 8, 8))
for a in range(8):
    for b in range(8):
        for c in range(8):
            for dd in range(8):
                R_sphere[a, b, c, dd] = (1 if a == c else 0) * (1 if b == dd else 0) - (1 if a == dd else 0) * (1 if b == c else 0)

corrected_sphere = 0.0
diagonal_sphere = 0.0
for pi_idx, pi_part in enumerate(parts8):
    sgn_i = psigns8[pi_idx]
    for pj_idx, pj_part in enumerate(parts8):
        sgn_j = psigns8[pj_idx]
        M = np.zeros((n, n))
        for k in range(n):
            a1, a2 = pi_part[k]
            for l in range(n):
                b1, b2 = pj_part[l]
                M[k, l] = R_sphere[a1, a2, b1, b2]
        corrected_sphere += sgn_i * sgn_j * np.linalg.det(M)
        diag_prod = 1.0
        for k in range(n):
            diag_prod *= M[k, k]
        diagonal_sphere += sgn_i * sgn_j * diag_prod

print(f"Sphere corrected: {corrected_sphere:.6f}")
print(f"Sphere diagonal:  {diagonal_sphere:.6f}")
print(f"chi(S^8) from corrected: {corrected_sphere * 32*np.pi**4/105 / (2*np.pi)**4:.6f} (expected 2)")
print(f"chi(S^8) from diagonal:  {diagonal_sphere * 32*np.pi**4/105 / (2*np.pi)**4:.6f}")
