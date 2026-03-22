"""
Debug part 2: Check if R_abcd is in coordinate (left-invariant) frame vs ON frame.
If in LI frame, the Euler density computation needs the metric determinant.
"""

import numpy as np

d = np.load('C:/sandbox/Ainulindale Exflation/tier0-computation/r20a_riemann_tensor.npz', allow_pickle=True)
tau_vals = d['tau']
R_abcd = d['R_abcd']
Ric = d['Ric']
R_scalar = d['R_scalar']

# KEY TEST: If the Riemann tensor is in the LEFT-INVARIANT (LI) frame with metric g_ab,
# then contractions need the inverse metric. If it's in the ON frame, contractions use delta.
#
# At tau=0: g_LI = 3*I_8. In LI frame, Ric_{ab} = R_{cabc} (or similar) but this gives
# Ric in the LI frame, and R_scalar = g^{ab} Ric_{ab} = (1/3) Tr(Ric_LI).
#
# Test: if LI frame, R = (1/3) * sum_a Ric_{aa} = (1/3) * 8 * Ric_{11}
# At tau=0: R_scalar = 2.0. If Ric_{aa} = 0.25 in LI, then (1/3)*8*0.25 = 0.667 != 2.0.
# If ON frame: R = sum Ric_{aa} = 8*0.25 = 2.0. MATCHES.
# So Ric is in ON frame.

# But wait: check at tau=0.5.
# In LI frame with g = 3*diag(e^{2*0.5}*[3 dirs], e^{-2*0.5}*[4 dirs], e^{0.5}*[1 dir])
# = 3*diag(e, e, e, e^{-1}, e^{-1}, e^{-1}, e^{-1}, e^{0.5})
# Ric values at tau=0.5: [0.464, 0.464, 0.464, 0.161, 0.161, 0.161, 0.161, 0.250]
# R = sum = 3*0.464 + 4*0.161 + 0.250 = 1.393 + 0.645 + 0.250 = 2.288
# R_scalar at tau=0.5: 2.288. MATCHES (so it IS ON frame for Ric).

# Now the question: is R_abcd ALSO in ON frame?
# At tau=0: if ON, R[0,1,0,1] should be the sectional curvature K(e0,e1) * something.
# For round SU(3) with our normalization (R=2):
# K(X,Y) = R(X,Y,Y,X) / (|X|^2|Y|^2 - <X,Y>^2) = R_{0101} for ON vectors.
# For a bi-invariant metric: K(X,Y) = (1/4)|[X,Y]|^2 / (|X|^2|Y|^2 - <X,Y>^2)
# For ON basis: K(e_0, e_1) = (1/4)|[e_0,e_1]|^2

# With our structure constants f_ON_{abc} = f_{abc}/sqrt(3):
# [e_0, e_1] = sum_c f_ON_{01c} e_c = f_ON_{012} e_2 = (1/sqrt(3)) e_2
# |[e_0,e_1]|^2 = 1/3
# K(e_0,e_1) = (1/4)(1/3) = 1/12

# So R_ON_{0101} = +K(e_0,e_1) = +1/12 = 0.0833... (with convention R_{0101} = K for spheres)
# Or R_ON_{0101} = -K = -1/12 with opposite convention.
# Our stored: R[0,1,0,1] = -1/12 = -0.0833.
# So R_stored_{abcd} uses the convention where R_{0101} = -K (e.g., MTW, Wald).

# CRITICAL QUESTION: Is the Riemann tensor in ON frame or LI frame at tau > 0?
# Test: compute |Riem|^2 = sum R_{abcd}^2 (if ON) vs sum g^{aa'}g^{bb'}g^{cc'}g^{dd'} R_{a'b'c'd'} R_{abcd} (if LI).

# At tau=0.5:
# If ON: |Riem|^2 = sum R[5]^2 = K_stored[5]
# If LI: |Riem|^2 = sum (R[5]_{abcd})^2 * (g^{-1})_a (g^{-1})_b (g^{-1})_c (g^{-1})_d

K_05 = np.sum(R_abcd[5]**2)
print(f"|Riem|^2 at tau=0.5 from sum R^2: {K_05:.10f}")
print(f"K_stored at tau=0.5: {d['K'][5]:.10f}")
print(f"K_exact at tau=0.5: {d['K_exact'][5]:.10f}")

# If these match, R is in ON frame (since K_stored was presumably computed in ON frame too).
# If they don't match, one or both are in LI frame.
print(f"Match: {'YES' if abs(K_05 - d['K'][5]) < 1e-10 else 'NO'}")

# Also check: the stored Riemann tensor should satisfy specific algebraic identities.
# For ON frame: R_{abab} = sectional curvature K(a,b) (up to sign convention).
# For LI frame: R_{abab} != K(a,b) (need metric factors).

# At tau=0.5, for directions 0 and 3 (different subspaces):
# If ON: K(e_0, e_3) = R_{0303}
# If LI: K(e_0, e_3) = R_{0303} / (g_{00} g_{33} - g_{03}^2) = R_{0303} / (g_0 * g_3)
print(f"\nR[0,3,0,3] at tau=0.5: {R_abcd[5][0,3,0,3]:.10f}")

# For the Jensen metric at tau=0.5:
tau = 0.5
# Metric: g = 3 * diag(scale factors)
# From the Ric pattern: indices 0,1,2 scale together, 3,4,5,6 scale together, 7 alone.
# Let me figure out the scaling. For the Jensen deformation of SU(3):
# The metric in the LI basis {e_1,...,e_8} (Gell-Mann basis) is:
# g(tau) = 3 * diag(lambda_1(tau),...,lambda_8(tau))
# where the three eigenvalues of the deformation are:
# lambda for u(1): 3 directions (indices 0,1,2?) or 1 direction?

# Actually, the index ordering matters. From Paper 15 eq 3.68:
# The Jensen metric has eigenvalues along the three SU(3) root spaces:
# mu_alpha: corresponding to SU(2) generators (3 directions)
# mu_beta: corresponding to C^2 coset generators (4 directions)
# mu_gamma: corresponding to U(1) generator (1 direction)
# With the volume-preserving constraint: mu_alpha^3 * mu_beta^4 * mu_gamma = 1

# Standard parametrization:
# mu_su2 = e^{-2tau}, mu_C2 = e^{tau}, mu_u1 = e^{2tau}... but 3*(-2) + 4*1 + 1*2 = -6+4+2 = 0. YES!
# OR: mu_su2 = e^{2tau}, mu_C2 = e^{-tau}, mu_u1 = e^{-2tau}: 3*2 + 4*(-1) + 1*(-2) = 6-4-2 = 0. Also.

# From Session 17 memory: "u(1): 1 direction, scale e^{2s}. su(2): 3 directions, e^{-2s/3}..."
# Actually from the memory: g_s = 3*diag(e^{2s}x3, e^{-2s}x4, e^{s})
# Volume: e^{2s*3} * e^{-2s*4} * e^{s*1} = e^{6s-8s+s} = e^{-s}. NOT zero!
# This can't be right for volume-preserving.

# Wait, from Session 17a B-1: g_1/g_2 = e^{-2s}.
# g_1 = U(1) coupling, g_2 = SU(2) coupling.
# The coupling ratio depends on metric components: g_1/g_2 = sqrt(vol_su2/vol_u1) = e^{-2s}.
# This constrains the metric but doesn't fully specify it.

# Let me just READ the Ric pattern more carefully.
# At tau=0.5: indices 0,1,2 have Ric=0.464, indices 3,4,5,6 have Ric=0.161, index 7 has Ric=0.250.
# At tau=0.0: all Ric = 0.250.
# As tau increases: 0,1,2 increase (0.25 -> 0.464), 3,4,5,6 decrease (0.25 -> 0.161), 7 constant (0.25).
# Pattern: 3 directions "stretch" (higher Ric), 4 directions "compress" (lower Ric), 1 direction constant.
# Multiplicities: 3, 4, 1 corresponds to u(1)[3?], su(2)[4?], C^2[1?]
# But standard: su(2) has 3 generators, C^2 has 4, u(1) has 1.
# So: indices 0,1,2 = su(2) [3 dirs], indices 3,4,5,6 = C^2 [4 dirs], index 7 = u(1) [1 dir].
# Ric(su2) increases, Ric(C2) decreases, Ric(u1) constant.

# For a bi-invariant metric with Ric = (1/4)*I, the Jensen deformation:
# mu_su2 directions: Ric grows -> these directions are COMPRESSING (shorter, higher curvature)
# mu_C2 directions: Ric shrinks -> these directions are STRETCHING
# mu_u1: constant Ric -> this direction doesn't change in the ON frame Ric

# The metric in LI basis: g = 3 * diag(a^2[su2], b^2[C2], c^2[u1])
# Volume-preserving: a^6 * b^8 * c^2 = 1 (or some power)
# Wait: g = 3 * diag(a, a, a, b, b, b, b, c) where a,b,c are functions of tau.
# det(g) = 3^8 * a^3 * b^4 * c. Volume-preserving: a^3 * b^4 * c = 1.

# In ON frame, the metric is I_8 by definition. The curvature in ON frame encodes
# both the shape of the manifold and the metric. The key question for our computation
# is whether the STORED R_abcd has ON components or LI components.

# We established: K_stored = sum R^2 at all tau. This is correct for ON frame.
# In LI frame, |Riem|^2 = g^{-1} g^{-1} g^{-1} g^{-1} R R (8 metric inverses for 4 pairs of indices).
# Actually for a diagonal metric g = diag(g_1,...,g_8) in LI frame:
# |Riem|^2 = sum_{abcd} R_{abcd}^2 / (g_a * g_b * g_c * g_d)
# This equals sum R^2 only when g = I (ON frame).
# At tau=0, g=3*I, so |Riem|^2_LI = sum R^2 / 3^4 = sum R^2 / 81.
# We got sum R^2 = K_stored = 0.5. If LI: |Riem|^2 = 0.5/81 = 0.00617.
# But K_stored = 0.5, so if K_stored is the actual |Riem|^2, then R is in ON frame.
#
# UNLESS K_stored was computed the same wrong way (just sum R^2 regardless of frame).
# We need an independent check.
#
# Independent check: at tau=0, round SU(3).
# For round SU(3) with Killing form B, R = constant.
# Our normalization: Ric = 0.25*I, R = 2.
# Standard result: for a compact simple Lie group with metric g = -c*B (c>0):
# Ric = (1/(4c)) * g in ON frame, so Ric_{ab} = 1/(4c) * delta_{ab}.
# Our Ric_{ab} = 0.25 = 1/(4c) => c = 1.
# g = -B. For SU(3), B(X,Y) = 6*Tr(XY) = -6*Tr_fund(XY) (if X,Y in su(3) represented as 3x3 antihermitian).
# Actually B_{ab} = -3*delta_{ab} for our Gell-Mann basis normalization.
# g = -B = 3*delta. So g_LI = 3*I.
# In LI frame: g = 3*I. ON frame: e_a = (1/sqrt(3)) X_a where X_a are the LI generators.
# |Riem|^2 in ON = sum R_ON_{abcd}^2.
# R_ON_{abcd} = R_LI_{abcd} / sqrt(g_a g_b g_c g_d) = R_LI / (3^2) = R_LI / 9 at tau=0.
# (Because R_ON = e^*_a e^*_b e^*_c e^*_d R = (1/sqrt(3))^4 R_LI = R_LI / 9)
# Wait: R_ON_{abcd} = R_LI_{efgh} * (e^{-1})^e_a * (e^{-1})^f_b * (e^{-1})^g_c * (e^{-1})^h_d
# For diagonal: = R_LI_{abcd} * 1/sqrt(g_a) * 1/sqrt(g_b) * 1/sqrt(g_c) * 1/sqrt(g_d)
# At tau=0: = R_LI_{abcd} / (sqrt(3))^4 = R_LI / 9.
# So |Riem|^2_ON = sum (R_LI/9)^2 = (1/81) sum R_LI^2.
# And |Riem|^2_ON should equal K_exact for ON computation.

# For bi-invariant SU(3) with g = 3*I:
# R_LI_{abcd} = +(1/4) f_{abe} f_{cde} (using our sign convention, Ric_{ab} = R_{cabc}).
# R_LI_{0101} = (1/4) sum_e f_{01e}^2 = (1/4)*1 = 0.25 (f_{012}=1 for Gell-Mann).
# R_ON_{0101} = R_LI / 9 = 0.25/9 = 0.0278.
# BUT stored R[0,1,0,1] = -0.0833, which is -(1/12) = -(3/4)/9 ???
# Let me check: 0.0833 = 1/12. And 0.25/9 = 0.0278. These don't match.
# So our R is NOT R_LI/9. It must be directly in ON frame.

# In ON frame: R_ON_{abcd} = -(1/4) [e_a, e_b]·[e_c, e_d]_{ON} (Wald convention)
# With [e_a, e_b]_ON = f_ON_{abc} e_c where f_ON = f/sqrt(3).
# R_ON_{0101} = -(1/4) sum_e (f_ON_{01e})^2 = -(1/4)(f_{012}/sqrt(3))^2 = -(1/4)(1/3) = -1/12.
# MATCHES -0.0833! So R IS in ON frame with the Wald sign convention (R < 0 for positive curvature).

# Great. So the R_abcd data IS in ON frame. Now why does the Euler density vary?

# For a LEFT-INVARIANT metric on a Lie group, the curvature in the ON frame IS constant
# over the manifold (because left-translations are isometries, and the ON frame is
# left-invariant). So the Euler density is a constant function on the manifold.
# chi = euler_density * Vol.
# chi(SU(3)) = 0 for ALL metrics (topological invariant of SU(3)).
# Vol > 0.
# Therefore euler_density = 0 for all tau.

# But we computed euler_density != 0. This means our formula is WRONG.

# The issue: the Gauss-Bonnet formula involves the curvature 2-FORM, which has both
# matrix (fiber) indices and form (base) indices. In ON frame, the curvature 2-form is:
# Omega^a_b = (1/2) R^a_{bcd} e^c ^ e^d
# The Pfaffian involves the ANTISYMMETRIC matrix structure. We have:
# R^a_{bcd} = g^{ae} R_{ebcd}
# In ON: R^a_{bcd} = R_{abcd}. But note R_{abcd} is antisymmetric in (a,b) AND in (c,d).
# So the "matrix" Omega_{ab} is antisymmetric (as it should be for so(8)).

# The Pfaffian of an antisymmetric matrix M:
# Pf(M) = (1/(2^n n!)) epsilon_{i1...i_{2n}} M_{i1 i2} ... M_{i_{2n-1} i_{2n}}
# This involves ONE epsilon, contracted with the matrix indices.

# For the curvature, we have a MATRIX of 2-forms, and we need to wedge them.
# Pf(Omega) = (1/(2^n n!)) epsilon_{a1...a_{2n}} Omega^{a1 a2} ^ ... ^ Omega^{a_{2n-1} a_{2n}}
# = (1/384) epsilon_{a1...a8} (1/2)^4 R^{a1}_{a2 c1 d1} R^{a3}_{a4 c2 d2} ... R^{a7}_{a8 c4 d4}
#   * epsilon^{c1 d1 c2 d2 c3 d3 c4 d4} * vol_8

# NOTE: R^a_{bcd} NOT R_{abcd}! The Pfaffian uses the curvature with one index UP.
# For the Levi-Civita connection, R^a_{bcd} = g^{ae} R_{ebcd}. In ON: R^a_bcd = R_{abcd}.
# So in ON frame, R^a_{bcd} = R_{abcd}. The formula uses R_{abcd} directly.

# BUT: the Pfaffian involves epsilon_{a1...a8} with the FIRST index of each pair SUMMED.
# Pf(Omega) involves:
# epsilon_{a1 a2 a3 a4 a5 a6 a7 a8} * R^{a1}_{a2, c1d1} * R^{a3}_{a4, c2d2} * ...
# = epsilon_{a1 a2 ...} * R_{a1 a2 c1d1} * R_{a3 a4 c2d2} * ...    (in ON frame)
# And the wedge product gives epsilon_{c1 d1 c2 d2 c3 d3 c4 d4}.
# But the form indices (c,d) pairs run through DIFFERENT ordering than the matrix index pairs.

# CRITICAL: there is only ONE epsilon for the matrix indices, and the second "epsilon"
# comes from the wedge product of the 2-forms. So:
# Pf(Omega) * vol = (1/384) * (1/16) * epsilon_{a-perm} * epsilon_{c-perm} * prod R
# = (1/6144) * S

# where S = sum_{sigma_a, sigma_c} sgn(sigma_a) sgn(sigma_c) prod R.
# S = 384^2 * partition_sum.
# Pf(Omega) = (1/6144) * 147456 * partition_sum = 24 * partition_sum.

# chi = integral Pf(Omega) / (2pi)^4 ... hmm, the normalization.
# Actually let me look this up properly.

# STANDARD FORMULA (Nakahara, eq 11.92):
# chi(M^{2m}) = integral_{M^{2m}} e(M)
# e(M) = ((-1)^m / ((4pi)^m * m!)) * epsilon_{a1...a_{2m}} Omega^{a1 a2} ^ ... ^ Omega^{a_{2m-1} a_{2m}}
#
# For 2m = 8, m = 4:
# e(M) = ((-1)^4 / ((4pi)^4 * 4!)) * epsilon * Omega^4
# = (1 / (256 pi^4 * 24)) * epsilon * Omega^4
# = (1 / 6144 pi^4) * epsilon * Omega^4
#
# Now Omega^{a_1 a_2} = (1/2) R^{a_1}_{a_2 c d} e^c ^ e^d
# and we need to RAISE the second index: Omega^{ab} = g^{bc} Omega^a_c = R^{ab}_{cd} e^c^e^d / 2.
# Wait, the Pfaffian uses Omega^{ab} antisymmetric. But R^{ab}_{cd} = g^{be} R^a_{ecd}.
# In ON: R^{ab}_{cd} = R_{abcd} (raising b with delta).
# Since R_{abcd} is already antisymmetric in (a,b), this is antisymmetric.
# And from pair symmetry: R_{abcd} = R_{cdab}, so Omega^{ab} ^ Omega^{cd} terms...

# Actually I realize the key formula is:
# Omega^{ab}_{cd} = R^{ab}_{cd} (antisymmetric in ab AND cd)
# Omega^{ab} = (1/2) R^{ab}_{cd} e^c ^ e^d

# Pf(Omega^{ab}) = (1/(2^4 * 4!)) epsilon_{a1...a8} Omega^{a1a2} ^ ... ^ Omega^{a7a8}

# Each Omega^{ab} = (1/2) R^{ab}_{cd} e^c^e^d. Product of 4:
# Omega^{a1a2}^...^Omega^{a7a8} = (1/16) sum R...R * 8-form
# 8-form = epsilon_{c-perm} * vol

# So: Pf = (1/384) * (1/16) * epsilon_a * epsilon_c * RRRR = (1/6144) * S

# e(M) = (1/(6144 pi^4)) * (1/6144) * S ...
# No wait. e(M) = (1/(6144 pi^4)) * epsilon_a * Omega^4
# = (1/(6144 pi^4)) * (1/16) * epsilon_a * epsilon_c * RRRR * vol
# Hmm I keep getting confused. Let me just USE THE SPHERE RESULT.

# From sphere: chi(S^8) = 2.
# Our formula: chi = (1/(2pi)^4) * euler_density * Vol
# = (1/(2pi)^4) * 384 * partition_sum * Vol.
# This WORKS for the sphere (verified numerically).

# For SU(3): chi = 0, so partition_sum SHOULD be 0.
# It's not.

# POSSIBLE EXPLANATION:
# The formula chi = euler_density * Vol / (2pi)^4 assumes the manifold is CONNECTED
# and the density is CONSTANT. For the round SU(3) (tau=0), the density IS constant.
# So either:
# (1) chi(SU(3)) != 0 (wrong), or
# (2) Our partition sum has a computational error.

# Let me double-check chi(SU(3)).
# SU(3) is a compact, connected, simply-connected Lie group.
# chi(G) = 0 for any compact Lie group of positive dimension (because of the
# existence of a nowhere-vanishing left-invariant vector field).
# This is a standard result. chi(SU(3)) = 0. Confirmed.

# So there must be an error in the computation. Let me check with a 4D example.
# For S^4: dim=4, chi=2. K=1 (constant curvature).
# R_{abcd} = delta_ac delta_bd - delta_ad delta_bc
# Pairs of {0,1,2,3}: (01)(23), (02)(13), (03)(12) = 3 partitions.
# Signs: (01)(23) -> perm (0,1,2,3) -> sign +1
#         (02)(13) -> perm (0,2,1,3) -> sign -1
#         (03)(12) -> perm (0,3,1,2) -> sign +1
print("\n4D check: S^4 with K=1")
R4 = np.zeros((4,4,4,4))
for a in range(4):
    for b in range(4):
        for c in range(4):
            for dd in range(4):
                R4[a,b,c,dd] = (1 if a==c else 0)*(1 if b==dd else 0) - (1 if a==dd else 0)*(1 if b==c else 0)

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
print(f"Partitions of {{0,1,2,3}}: {len(parts4)}")
for p in parts4:
    perm = []
    for a,b in p:
        perm.extend([a,b])
    print(f"  {p} -> perm {perm} -> sign {perm_sign(perm)}")

psigns4 = [perm_sign([x for pair in p for x in pair]) for p in parts4]

# Partition sum for S^4
ps4 = 0.0
for i, pi in enumerate(parts4):
    for j, pj in enumerate(parts4):
        prod = 1.0
        for k in range(2):
            a1, a2 = pi[k]
            b1, b2 = pj[k]
            prod *= R4[a1, a2, b1, b2]
        ps4 += psigns4[i] * psigns4[j] * prod

print(f"\nPartition sum (S^4): {ps4}")
print(f"2^2 * 2! = 8 multiplier: {8 * ps4}")
# For S^4: chi = 2 = (1/(2pi)^2) * 8 * ps4 * Vol(S^4)
# Vol(S^4) = 8pi^2/3
vol_S4 = 8 * np.pi**2 / 3
chi4 = (1/(2*np.pi)**2) * 8 * ps4 * vol_S4
print(f"chi = (1/(2pi)^2) * 8 * ps4 * Vol(S^4) = {chi4:.6f} (expected 2)")

# Let me also compute for the WRONG formula (using 384 = 2^4 * 4!):
# In 4D: 2^2 * 2! = 8 (not 384).
# The general formula: 2^n * n! where 2n = dim.
# For 2n = 8: 2^4 * 4! = 384. For 2n = 4: 2^2 * 2! = 8.
# chi = (1/(2pi)^n) * (2^n * n!) * partition_sum * Vol
# n = dim/2.

# This CONFIRMS: chi = (1/(2pi)^n) * (2^n * n!) * partition_sum * Vol where 2n = dim.
# For S^4: chi = (1/(2pi)^2) * 8 * 3 * vol = (1/(2pi)^2) * 24 * 8pi^2/3 = 24*8/(3*4) = 16. WRONG!
# Hmm, ps4 = 3, 8*3 = 24, (1/(2pi)^2) * 24 * 8pi^2/3 = 24*8pi^2/(3*(2pi)^2) = 24*8/(3*4) = 16. Not 2!

# OK so the normalization is different. Let me recalibrate.
# chi_S^4 = 2. Vol_S^4 = 8pi^2/3. partition_sum = 3.
# chi = C * partition_sum * Vol => C = 2/(3 * 8pi^2/3) = 2/(8pi^2) = 1/(4pi^2).
# But (1/(2pi)^2) = 1/(4pi^2). So C = 1/(4pi^2).
# chi = (1/(4pi^2)) * partition_sum * Vol.
# For general 2n: chi = (1/(2pi)^n) * partition_sum * Vol?
# At n=2: (1/(2pi)^2) = 1/(4pi^2). With partition_sum=3, Vol=8pi^2/3:
# chi = 3 * 8pi^2/3 / (4pi^2) = 8/4 = 2. YES!
# So: chi = (1/(2pi)^n) * partition_sum * Vol. NOT (2^n * n!) * partition_sum * Vol / (2pi)^n.

# Wait, that contradicts the sphere check in 8D!
# In 8D: chi = (1/(2pi)^4) * partition_sum * Vol.
# partition_sum_sphere = 105. Vol_S^8 = 32pi^4/105.
# chi = 105 * 32pi^4 / (105 * (2pi)^4) = 32pi^4 / (16 pi^4) = 2. YES!

# So the correct formula is simply:
# chi = (1/(2pi)^n) * partition_sum * Vol
# where n = dim/2 and partition_sum is our partition-based double sum.

# For SU(3) at tau=0: partition_sum = 1.763e-4.
# chi should be 0.
# Vol(SU(3), g_0) = ... let me compute.
# g_0 = 3*I. Vol = integral sqrt(det(3*I)) d^8x over the group manifold.
# In terms of the group volume with bi-invariant measure:
# Vol(SU(3), B) (with B = Killing form) = (4pi)^4 * 2/(3! * ... )
# Actually Vol(SU(3)) in our normalization:
# With g_0 = 3*delta, det(g_0) = 3^8.
# Vol = sqrt(3^8) * Vol_unit = 3^4 * Vol_unit where Vol_unit is the volume with the metric delta.
# For SU(3) with Killing form -B: Vol = sqrt(2)^{-8} * product of root lengths * ...
# This is getting complicated. The exact value doesn't matter — what matters is that Vol > 0.

# So partition_sum should be 0 for SU(3). But it's 1.763e-4.
# Let me check: is our partition formula CORRECT?

# In 4D: partition_sum for S^4 = 3.
# Direct calculation: 3 partitions of {0,1,2,3}.
# P1 = [(0,1),(2,3)]: sign +1
# P2 = [(0,2),(1,3)]: sign -1
# P3 = [(0,3),(1,2)]: sign +1

# sum_{i,j} sgn_i * sgn_j * R_{P_i[0]} * R_{P_i[1]} * R_{P_j[0]} * R_{P_j[1]}
# Wait -- in 4D we have 2 pairs (n=2), so the product has 2 factors of R.
#
# For the double sum, each pair of the i-partition contracts with the CORRESPONDING
# pair of the j-partition. So:
# Term (P1, P1): sgn(+1)*sgn(+1) * R[0,1,0,1] * R[2,3,2,3] = 1 * 1 * 1 = 1
# Term (P1, P2): sgn(+1)*sgn(-1) * R[0,1,0,2] * R[2,3,1,3] = -1 * R[0,1,0,2] * R[2,3,1,3]
# For S^4: R[0,1,0,2] = delta_00*delta_12 - delta_02*delta_10 = 0. So this term = 0.
# Similarly many cross-terms vanish.

# All non-vanishing terms for S^4:
print("\nDetailed S^4 partition sum:")
for i, pi in enumerate(parts4):
    for j, pj in enumerate(parts4):
        prod = 1.0
        for k in range(2):
            a1, a2 = pi[k]
            b1, b2 = pj[k]
            prod *= R4[a1, a2, b1, b2]
        if prod != 0:
            print(f"  P_i={pi}, P_j={pj}: sgn_i={psigns4[i]}, sgn_j={psigns4[j]}, prod={prod:.1f}, contribution={psigns4[i]*psigns4[j]*prod:.1f}")

# For SU(3) at tau=0:
R0 = d['R_abcd'][0]
print(f"\nSU(3) tau=0: partition_sum = {1.763237847222218e-04}")
print(f"Expected: 0 (since chi(SU(3)) = 0)")
print(f"Discrepancy: {abs(1.763237847222218e-04):.6e}")

# The discrepancy is NOT at machine epsilon. It's O(10^{-4}).
# This suggests a GENUINE issue, not a floating point artifact.

# HYPOTHESIS: The Riemann tensor data might have a subtle error.
# OR: My formula might have pairing issues.

# Let me try a different approach: compute using the FULL permutation sum for a small subset.
# Use the first 1000 permutations of S_8 and check.
from itertools import islice
count = 0
sample_sum = 0.0
full_perms = list(permutations(range(8)))
N_sample = min(1000, len(full_perms))
for sigma_i in full_perms[:N_sample]:
    for sigma_j in full_perms[:N_sample]:
        sgn_i = perm_sign(list(sigma_i))
        sgn_j = perm_sign(list(sigma_j))
        prod = 1.0
        for k in range(4):
            prod *= R0[sigma_i[2*k], sigma_i[2*k+1], sigma_j[2*k], sigma_j[2*k+1]]
        sample_sum += sgn_i * sgn_j * prod

print(f"\nSample sum (first {N_sample} of {len(full_perms)} perms for each): {sample_sum:.10e}")
print(f"Estimated full sum: {sample_sum * (len(full_perms)/N_sample)**2:.10e}")
print(f"Our partition-based full sum S = 384^2 * partition_sum = {147456 * 1.763237847222218e-04:.6f}")
