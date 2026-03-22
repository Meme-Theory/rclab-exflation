"""
Debug part 4: The curvature 2-form Pfaffian.

The curvature 2-form is: Omega^a_b = (1/2) R^a_{bcd} e^c ^ e^d
In ON frame: R^a_{bcd} = delta^{ae} R_{ebcd} = R_{abcd}.
BUT: the Pfaffian of a skew-symmetric matrix involves the matrix structure Omega^a_b,
NOT Omega_{ab}. The key distinction:
- Omega^a_b: first index up, second down. Antisymmetric?
  R^a_{bcd} is NOT antisymmetric in (a,b) — it's antisymmetric in (c,d) only.
  But the curvature of a metric connection has R_{abcd} antisymmetric in (a,b) AND (c,d).
  So R^a_{bcd} = R_{abcd} in ON frame, which IS antisymmetric in (a,b).
  But Omega^a_b = (1/2) R^a_{bcd} e^c^e^d with the MATRIX indices being (a,b).
  The antisymmetry R_{abcd} = -R_{bacd} means R^a_b = -R^b_a, so Omega^a_b = -Omega^b_a.
  Good: the matrix is antisymmetric.

But wait: the SIGN CONVENTION matters.
Our stored tensor has Ric = R_{cabc} (= -R_standard contracted).
This means R_stored = -R_Wald.
The curvature 2-form with our convention: Omega_stored = -Omega_Wald.
Pf(-Omega) = (-1)^n Pf(Omega) where n = dim/2 = 4.
(-1)^4 = +1. So Pf(Omega_stored) = Pf(Omega_Wald).
The Euler density is unchanged. OK so sign is not the issue.

Let me try a completely different approach: compute the Euler characteristic of SU(3)
directly from the structure constants, using the known formula for Lie groups.

For a compact Lie group G:
chi(G) = 0 if dim(G) > 0.

This follows because G has a nowhere-zero left-invariant vector field.
By the Poincare-Hopf theorem, chi(G) = 0.

So the Euler density integrated over G must be zero for ANY left-invariant metric.
For a homogeneous metric (left-invariant), the Euler density is constant.
So the density itself must be zero.

Let me verify this with a KNOWN formula for the Euler density on Lie groups.
For a compact Lie group G with bi-invariant metric:
R_{abcd} = -(1/4) f_{abe} f_{cde}  (standard convention)

The Euler density should be zero. Let me check this using the EXACT structure constants
of SU(3), without relying on the stored data.
"""

import numpy as np

# SU(3) structure constants (standard Gell-Mann basis, 0-indexed)
# f_{abc} with a,b,c in {0,...,7} (mapping from 1-indexed lambda_i)
# Non-zero values (and their antisymmetric permutations):
f = np.zeros((8, 8, 8))

# From standard tables (0-indexed = i-1):
# f_{012} = 1 (i.e., f_{123} = 1 in 1-indexed)
f[0, 1, 2] = 1.0
# f_{034} = 1/2 (f_{147} = 1/2 in 1-indexed... wait, let me be precise)

# Standard SU(3) structure constants (1-indexed):
# f_{123} = 1
# f_{147} = f_{246} = f_{257} = f_{345} = 1/2
# f_{156} = f_{367} = -1/2
# f_{458} = f_{678} = sqrt(3)/2
# Converting to 0-indexed (i -> i-1):
# f_{012} = 1
# f_{036} = 1/2, f_{135} = 1/2, f_{146} = 1/2, f_{234} = 1/2
# f_{045} = -1/2, f_{256} = -1/2
# f_{347} = sqrt(3)/2, f_{567} = sqrt(3)/2

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

# Fill in f with full antisymmetry
f = np.zeros((8, 8, 8))
for (a, b, c), val in f_values.items():
    # All even permutations get +val, odd permutations get -val
    f[a, b, c] = val
    f[b, c, a] = val
    f[c, a, b] = val
    f[a, c, b] = -val
    f[b, a, c] = -val
    f[c, b, a] = -val

# Verify: f is totally antisymmetric
print("Structure constants verification:")
err_antisym = np.max(np.abs(f + np.transpose(f, (1, 0, 2))))
print(f"  |f_{abc} + f_{bac}| max: {err_antisym:.2e}")

# Verify Jacobi identity: f_{abe}f_{ecd} + f_{ace}f_{edb} + f_{ade}f_{ebc} = 0
jacobi_err = 0.0
for a in range(8):
    for b in range(8):
        for c in range(8):
            for dd in range(8):
                val = (np.dot(f[a, b, :], f[:, c, dd]) +
                       np.dot(f[a, c, :], f[:, dd, b]) +
                       np.dot(f[a, dd, :], f[:, b, c]))
                jacobi_err = max(jacobi_err, abs(val))
print(f"  Jacobi identity max error: {jacobi_err:.2e}")

# Killing form: B_{ab} = f_{acd} f_{bcd} (summed over c,d)
B = np.einsum('acd,bcd->ab', f, f)
print(f"  Killing form diagonal: {np.diag(B)}")
print(f"  Killing form off-diag max: {np.max(np.abs(B - np.diag(np.diag(B)))):.2e}")
# For SU(3): B_{ab} = -3 delta_{ab} with our normalization
print(f"  Expected: -3 * I_8")

# Riemann tensor for bi-invariant metric in ON frame
# Our metric: g = -c*B = c*3*I. With c=1: g = 3*I.
# ON basis: e_a = (1/sqrt(3)) X_a
# ON structure constants: f_ON_{abc} = (1/sqrt(3)) f_{abc}
# Riemann (standard convention): R_{abcd} = -(1/4) sum_e f_ON_{abe} f_ON_{cde}
# = -(1/4)(1/3) sum_e f_{abe} f_{cde} = -(1/12) sum_e f_{abe} f_{cde}
# Riemann (our stored convention, opposite sign):
# R_stored_{abcd} = +(1/12) sum_e f_{abe} f_{cde}

R_analytic = np.zeros((8, 8, 8, 8))
for a in range(8):
    for b in range(8):
        for c in range(8):
            for dd in range(8):
                R_analytic[a, b, c, dd] = (1.0/12.0) * np.dot(f[a, b, :], f[c, dd, :])

# Check: does this match the stored data?
R_stored = d['R_abcd'][0]
err = np.max(np.abs(R_analytic - R_stored))
print(f"\n|R_analytic - R_stored| max: {err:.6e}")
print(f"R_analytic[0,1,0,1] = {R_analytic[0,1,0,1]:.10f}")
print(f"R_stored[0,1,0,1] = {R_stored[0,1,0,1]:.10f}")

# Verify Ric
Ric_analytic = np.einsum('cabc->ab', R_analytic)
print(f"\nRic_analytic diagonal: {np.diag(Ric_analytic)}")
print(f"Expected: 0.25 * I")

# OK now compute the Euler density using the analytic Riemann tensor.
# Using the CORRECTED formula with det(M).

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

nblocks = 4
corrected_sum_analytic = 0.0
diagonal_sum_analytic = 0.0

for pi_idx, pi_part in enumerate(parts8):
    sgn_i = psigns8[pi_idx]
    for pj_idx, pj_part in enumerate(parts8):
        sgn_j = psigns8[pj_idx]
        M = np.zeros((nblocks, nblocks))
        for k in range(nblocks):
            a1, a2 = pi_part[k]
            for l in range(nblocks):
                b1, b2 = pj_part[l]
                M[k, l] = R_analytic[a1, a2, b1, b2]
        corrected_sum_analytic += sgn_i * sgn_j * np.linalg.det(M)
        diag_prod = 1.0
        for k in range(nblocks):
            diag_prod *= M[k, k]
        diagonal_sum_analytic += sgn_i * sgn_j * diag_prod

print(f"\n=== ANALYTIC R (round SU(3)) ===")
print(f"Corrected partition sum: {corrected_sum_analytic:.15e}")
print(f"Diagonal partition sum:  {diagonal_sum_analytic:.15e}")
print(f"Expected: 0 (since chi(SU(3)) = 0)")

# Hmm. If this is still nonzero, let me check whether the issue is that
# the Euler density formula I'm using is WRONG for Lie groups.
# Maybe I'm confusing the two different "Gauss-Bonnet" theorems.
#
# In fact, let me reconsider: for an 8-manifold, the Euler CLASS is:
# e_8 = Pf(Omega / 2pi)
# where Omega is the curvature 2-form of the TANGENT BUNDLE.
# The Pfaffian of a 2m-form valued so(2m) matrix:
# Pf(Omega) = (1/(2^m m!)) epsilon_{a1...a_{2m}} Omega^{a_1 a_2} ^ ... ^ Omega^{a_{2m-1} a_{2m}}
#
# For m=4 (8-manifold):
# Pf(Omega) = (1/384) epsilon_{a1...a8} Omega^{a1 a2} ^ Omega^{a3 a4} ^ Omega^{a5 a6} ^ Omega^{a7 a8}
#
# chi = integral Pf(Omega/(2pi))
# = integral (1/(2pi)^4) Pf(Omega)
# = (1/(2pi)^4) * (1/384) * epsilon_a * [Omega^4]_top
#
# Now [Omega^{a1a2} ^ ... ^ Omega^{a7a8}]_top for specific a-values:
# Omega^{ab} = R^{ab}_{cd} e^c ^ e^d / 2 (summing over ALL c,d with antisymmetry)
# = sum_{c<d} R^{ab}_{cd} e^c ^ e^d
#
# The wedge of 4 two-forms:
# Omega^{a1a2} ^ Omega^{a3a4} ^ Omega^{a5a6} ^ Omega^{a7a8}
# = sum_{c_i < d_i} R^{a1a2}_{c1d1} ... R^{a7a8}_{c4d4} * e^{c1}^e^{d1}^...^e^{c4}^e^{d4}
# = sum_{c1<d1,...,c4<d4} R...R * epsilon(c1,d1,...,c4,d4) * vol_8
# (when (c1,d1,...,c4,d4) is a permutation of (0,...,7))
#
# This equals: sum over pair-partitions Q of {0,...,7}:
# sgn(Q) * prod_k R^{a_{2k-1} a_{2k}}_{Q[k]}
# where Q[k] = (q_{2k-1}, q_{2k}) with q_{2k-1} < q_{2k}.
# Actually: we need the sign of the permutation (c1,d1,c2,d2,c3,d3,c4,d4).
# For a partition Q with pairs in order, the permutation is the concatenation of the pairs.
# Its sign is the partition sign.
# But there's also the factor from going between "sum over c<d" and "sum over all c,d":
# Each pair (ci,di) with ci<di represents the 2-form e^{ci}^e^{di}.
# In the wedge product, we just concatenate: if all 8 indices are distinct,
# the result is epsilon(c1,d1,...,c4,d4) * vol_8.
# So: [Omega^{a1a2}^...^Omega^{a7a8}]_top = sum_{Q partitions} sgn(Q) * prod_k R^{a_{2k-1}a_{2k}}_{Q[k]}

# Then: epsilon_a * [Omega^4]_top
# = sum_{P partitions} sgn(P) * sum_{Q partitions} sgn(Q) * prod_k R^{P[k]}_{Q[k]}
# Wait no: epsilon_{a1...a8} contracts with specific a-values.
# The a-indices are free in Omega^{a1a2}^...^Omega^{a7a8}.
# The contraction (1/384) epsilon_{a1...a8} picks up the sum over partitions P of the a-indices.

# So: Pf(Omega) = (1/384) * sum_P sgn(P) * sum_Q sgn(Q) * prod_k R^{P[k]}_{Q[k]} * vol_8

# In ON frame: R^{ab}_{cd} = R_{abcd} (all indices equivalent).
# R^{P[k]}_{Q[k]} = R_{P[k], Q[k]} = R_{p1 p2 q1 q2} where P[k]=(p1,p2), Q[k]=(q1,q2).

# So Pf(Omega) = (1/384) * sum_{P,Q} sgn(P) sgn(Q) * prod_k R_{P[k],Q[k]} * vol_8
# = (1/384) * my_diagonal_partition_sum * vol_8
# (because my original formula IS the sum over P,Q with position-matched pairing!)

# chi = (1/(2pi)^4) * Pf = (1/(2pi)^4) * (1/384) * diagonal_sum * Vol
# = diagonal_sum * Vol / (384 * (2pi)^4)

# For sphere: diagonal_sum = 105.
# chi = 105 * 32pi^4/105 / (384 * (2pi)^4) = 32pi^4 / (384 * 16pi^4) = 32/6144 = 1/192.
# That's NOT 2!

# Hmm, but earlier I showed chi = partition_sum * Vol / (2pi)^4 works for the sphere.
# Let me recheck: partition_sum = 105. Vol = 32pi^4/105.
# chi = 105 * 32pi^4/105 / (2pi)^4 = 32pi^4 / (16pi^4) = 2. YES.
# But with (1/384) factor: chi = 105 * 32pi^4/105 / (384 * (2pi)^4) = 2/384 = 1/192. NO.

# So the normalization WITHOUT the (1/384) gives chi = 2 for the sphere.
# The Pfaffian formula includes a (1/384) factor.
# This means: chi = (1/(2pi)^4) * Pf(Omega) = (1/(2pi)^4) * (1/384) * diagonal_sum * Vol
# = diagonal_sum * Vol / (384 * (2pi)^4)
# For sphere: = 105 * 32pi^4/(105 * 384 * 16pi^4) = 32/(384*16) = 32/6144 = 1/192. WRONG!

# There's a factor of 384 discrepancy. So the (1/384) factor in the Pfaffian formula
# is NOT the right normalization for our partition sum. Let me recount.

# The Pfaffian of an antisymmetric 2m x 2m matrix A:
# Pf(A) = (1/(2^m m!)) sum_{sigma in S_{2m}} sgn(sigma) prod_{i=1}^m A_{sigma(2i-1), sigma(2i)}
# For m=4: (1/(2^4 * 4!)) = 1/384.
# This sums over ALL 8! = 40320 permutations of {1,...,8}.

# For our partition sum: we sum over 105 x 105 = 11025 pairs of partitions.
# The full sum S over all sigma, rho in S_8:
# S = sum_{sigma,rho} sgn(sigma) sgn(rho) prod_k R_{sigma(2k),sigma(2k+1),rho(2k),rho(2k+1)}
# S has 40320^2 terms.
# Our partition sum has 105^2 terms.
# Each partition represents 384 = 2^4 * 4! permutations (pair reorderings + within-pair flips).
# Due to R antisymmetry and epsilon sign changes, each of the 384 perms gives the SAME
# contribution as the canonical partition ordering? NO!
# Within-pair flips: +1 each (as argued before). Factor: 2^4 = 16.
# Pair reorderings: this CHANGES which R factor gets which pair.
# For the i-indices: reordering pairs of P_i means changing which pair goes to position k.
# The product prod_k R_{P_i[tau(k)], P_j[k]} DEPENDS on tau.
# So pair reorderings do NOT simply multiply.

# This means my partition sum is NOT S/384^2. It's something else.
# The correct relationship involves the permanent/determinant of the M matrix.
# As derived in debug3:
# S = 256 * 24 * sum_{P,Q} sgn(P) sgn(Q) * det(M_{PQ})
# = 6144 * corrected_sum

# But for the sphere: S = 6144 * 105.
# And also S = (40320 perms)^2 * (average value per perm pair).
# For the sphere (constant curvature): S = ?
# Let me just compute S for the sphere numerically with a small approach.

# For the sphere with K=1: R_{abcd} = delta_ac delta_bd - delta_ad delta_bc
# The full sum S = sum_{sigma,rho} sgn(sigma) sgn(rho) prod_k R_{sigma(2k)sigma(2k+1),rho(2k)rho(2k+1)}
# = sum_{sigma,rho} sgn(sigma) sgn(rho) prod_k (delta_{sigma(2k),rho(2k)}*delta_{sigma(2k+1),rho(2k+1)} - delta_{sigma(2k),rho(2k+1)}*delta_{sigma(2k+1),rho(2k)})
# Each factor is +1 if sigma and rho agree on position pair (2k,2k+1), -1 if they disagree, 0 otherwise.
# This equals sum_{sigma,rho} sgn(sigma) sgn(rho) * sgn(rho^{-1} sigma restricted to pairs)
# ... complicated. Let me just trust the numerical result.

# From debug3: corrected_sphere = 105.
# S_sphere = 6144 * 105 = 645120.
# chi = (1/(2pi)^4) * (1/(2^4 * 4!)) * S * Vol (from Pf formula)
# Wait the Pf formula is:
# Pf = (1/384) * epsilon_a * [Omega^4]_top
# And [Omega^4]_top involves a sum over FORM indices (the rho part).
# So Pf already has ONE epsilon from the matrix indices and gets the form-index sum from wedge.
# Let me reconsider.

# Actually I think the issue is that Pf(Omega) is NOT the double-epsilon contraction.
# Pf involves ONE epsilon (for the matrix indices a). The form indices c come from the wedge product.
# In the wedge product of 4 two-forms, the result on an 8-manifold is automatically a top form,
# which is proportional to vol_8 with coefficient = epsilon of the form indices.

# So: Pf(Omega) = (1/384) * epsilon_a * epsilon_c * RRRR * vol / ???
# NO! Pf(Omega) has ONE epsilon and the second epsilon comes from the wedge.
# Pf(Omega) = (1/384) * sum_{P_a} sgn(P_a) * [sum_{P_c} sgn(P_c) * prod R] * vol
# = (1/384) * sum_{P_a, P_c} sgn(P_a) sgn(P_c) * prod_k R_{Pa[k], Pc[k]} * vol
# = (1/384) * diagonal_sum * vol

# For sphere: (1/384) * 105 * vol_S8 = 105/(384) * 32pi^4/105 = 32pi^4/384.
# chi = (1/(2pi)^4) * 32pi^4/384 = 32/(384*16) = 1/192.
# This is NOT 2. Off by factor 384.

# I think the issue is that the formula for chi involves Pf(Omega/(2pi)) not (1/(2pi)^4)*Pf(Omega).
# Actually: e = Pf(Omega/(2pi)) = (1/(2pi))^4 * Pf(Omega)... no.
# Pf(A/c) = (1/c^m) Pf(A) for a 2m x 2m matrix. Here m=4.
# So Pf(Omega/(2pi)) = (1/(2pi))^4 * Pf(Omega).
# chi = integral e = integral Pf(Omega/(2pi)) = (1/(2pi)^4) * Pf(Omega) * Vol.
# = (1/(2pi)^4) * (1/384) * diagonal_sum * Vol.
# For sphere: = 105 / (384 * (2pi)^4) * 32pi^4/105 = 32/(384*16) = 1/192.
# Still wrong.

# Let me just empirically find the right formula by calibrating on the sphere.
# chi_sphere = 2.
# diagonal_sum_sphere = 105.
# Vol_S8 = 32pi^4/105.
# chi = C * diagonal_sum * Vol
# 2 = C * 105 * 32pi^4/105 = C * 32 pi^4
# C = 2/(32 pi^4) = 1/(16 pi^4) = 1/((2pi)^4 / pi^0)...
# (2pi)^4 = 16 pi^4. So C = 1/(2pi)^4.
# chi = (1/(2pi)^4) * diagonal_sum * Vol.
# For sphere: (1/(2pi)^4) * 105 * 32pi^4/105 = (1/16pi^4) * 32pi^4 = 2. YES!

# So: chi = diagonal_sum * Vol / (2pi)^4.
# And the (1/384) factor should NOT be there.

# This means: the number I call "diagonal_sum" is NOT the partition sum divided by 384.
# Let me trace through the sphere computation.

# In debug3: partition_sum_sphere = 105 = sum_{P,Q} sgn(P) sgn(Q) * prod_k R_{P[k],Q[k]}
# And I called "euler_density = 384 * partition_sum = 384*105 = 40320" in the main script.
# But in debug3 I called it "diagonal_sum" and got 105.
# So "partition_sum" in the main script = sum / 384 ??? No, let me re-check the main script.

# Main script: euler_density = 384 * total, where total = sum_{P,Q} sgn*sgn*prod.
# So total (= my partition sum) = sum of 105*105 terms. For sphere: total = 105.
# euler_density = 384 * 105 = 40320.
# This was then printed as E_8 = 40320 for the sphere.
# And chi = (1/(2pi)^4) * 384 * total * Vol = (1/(2pi)^4) * 40320 * Vol_S8
# = 40320 * 32pi^4/(105*(2pi)^4) = 40320*32/(105*16) = 40320*2/105 = 768. NOT 2.

# Wait, that can't be right. Let me re-check the main debug script output.
# It said: "chi(S^8) from corrected: 2.000000 (expected 2)"
# with corrected_sphere = 105.
# The formula was: corrected_sphere * 32*pi**4/105 / (2*pi)**4 = 105 * 32pi^4/(105*16pi^4) = 2. YES.

# And in the main Gauss-Bonnet script: euler_density = 384 * total.
# For the sphere: total = 105 (this is my "partition_sum").
# euler_density = 384 * 105 = 40320.
# The implied formula for chi: chi = (1/(2pi)^4) * total * Vol (NOT euler_density * Vol).

# So the CORRECT formula is: chi = partition_sum * Vol / (2pi)^n
# where partition_sum = sum_{P,Q} sgn(P) sgn(Q) * prod_k R_{P[k],Q[k]}
# WITHOUT the 384 multiplier.

# For SU(3) at tau=0: partition_sum = 1.763e-4 (from main script: total = 1.763e-4).
# Wait, main script had: total -> euler_density = 384 * total.
# Let me check: euler_density at tau=0 was 0.0677.
# total = 0.0677 / 384 = 1.76e-4.
# From debug3: diagonal_sum = 1.76e-4. Confirmed.

# chi = 1.76e-4 * Vol(SU(3)) / (2pi)^4 should be 0.
# So either Vol(SU(3)) * 1.76e-4 / (2pi)^4 = 0, which it can't be,
# or our partition_sum is wrong.

# Let me compute the partition sum ANALYTICALLY for round SU(3).
# R_{abcd} = (1/12) f_{abe} f_{cde}
# partition_sum = sum_{P,Q} sgn(P) sgn(Q) * prod_k R_{P[k],Q[k]}
# = sum_{P,Q} sgn(P) sgn(Q) * prod_k (1/12) f_{P_a1 P_a2 e_k} f_{Q_c1 Q_c2 e_k}
# Hmm, this involves summing over internal e indices. Let me think differently.

# R_{p1 p2, q1 q2} = (1/12) sum_e f_{p1 p2 e} f_{q1 q2 e}

# prod_k R_{P[k],Q[k]} = prod_k (1/12) sum_{e_k} f_{P_a1 P_a2 e_k} f_{Q_c1 Q_c2 e_k}
# = (1/12)^4 * sum_{e1,e2,e3,e4} prod_k f_{Pa[k] e_k} f_{Qc[k] e_k}

# This is getting complicated. Let me just check if the computation is RIGHT by
# comparing against the stored data.

# We already checked: R_analytic matches R_stored to 6e-6 at tau=0.
# Wait, what was the error?
print(f"\nR_analytic vs R_stored max diff: {err:.10e}")

# 6e-6 is NOT machine epsilon! There might be an issue with the structure constants.
# Let me check specific components.
for a in range(8):
    for b in range(a+1, 8):
        for c in range(8):
            for dd in range(c+1, 8):
                v1 = R_analytic[a,b,c,dd]
                v2 = R_stored[a,b,c,dd]
                if abs(v1) > 1e-10 or abs(v2) > 1e-10:
                    if abs(v1 - v2) > 1e-10:
                        print(f"  R[{a},{b},{c},{dd}]: analytic={v1:.10f}, stored={v2:.10f}, diff={v1-v2:.10e}")
