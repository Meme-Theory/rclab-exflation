#!/usr/bin/env python3
"""
Session 21c — P0-2: T''(0) Sign Gate + P0-3: S_signed(tau)

Computes:
  1. SU(3) -> SU(2) x U(1) branching coefficients b_1(p,q), b_2(p,q), Delta_b(p,q)
  2. T''(0) from eigenvalue derivatives at tau=0 (PRE-REGISTERED CONSTRAINT: T''(0) <= 0 = CLOSED)
  3. S_signed(tau) = Sum_{(p,q)} Sum_n [b_1-b_2] * ln(lambda_n^2(tau))
     (Pre-registered: minimum near tau ~ 0.12)

SU(3) branching: weights of D^{(p,q)} are enumerated, grouped by U(1) hypercharge Y,
and decomposed into SU(2) multiplets with isospin j.
  b_1(p,q) = Sum over all states of Y^2
  b_2(p,q) = Sum over all SU(2) multiplets of (2j+1)*j*(j+1)

Author: kaluza-klein-theorist (Session 21c)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict
import os
import sys

# ============================================================
# PART 1: SU(3) -> SU(2) x U(1) BRANCHING RULES
# ============================================================

def su3_weights(p, q):
    """
    Enumerate all weights of the SU(3) irrep D^{(p,q)} with multiplicities.

    Uses the convex hull of the Weyl orbit to determine which weights exist,
    then Freudenthal recursion for multiplicities.

    Weights in Dynkin basis (m1, m2).
    Convention: I_3 = m1/2, Y = (m1 + 2*m2)/3.

    Returns: list of (m1, m2, multiplicity) tuples.
    """
    # The weights of D^{(p,q)} lie in the convex hull of the Weyl orbit of (p,q).
    # For SU(3), a weight (m1, m2) in Dynkin labels is in this hull iff:
    #   e1 >= e3 and e2 >= e3 and e1 >= e2 ... no, that's dominant weights only.
    #
    # More correctly: the weight (m1, m2) is in D^{(p,q)} iff the three
    # "edge distances" are all non-negative. These are computed as follows.
    #
    # In the orthogonal basis (e1, e2, e3) with e1+e2+e3=0:
    #   e1 = (2*m1 + m2)/3, e2 = (-m1 + m2)/3, e3 = -(m1 + 2*m2)/3
    # Highest weight: E1 = (2p+q)/3, E2 = (-p+q)/3, E3 = -(p+2q)/3
    #
    # The convex hull is the set of all (e1,e2,e3) that can be written as
    # convex combinations of the 6 Weyl images. Equivalently, for SU(3):
    # (m1, m2) is a weight of D^{(p,q)} iff it can be written as
    # (p,q) - a*alpha_1 - b*alpha_2 with a,b non-negative integers
    # AND the result lies in the weight diagram.
    #
    # The simplest correct check: enumerate ALL integer points (m1, m2) on the
    # root lattice translated to (p,q), and keep those in the convex hull.
    # For SU(3), the convex hull has 6 vertices (Weyl orbit), or 3 if p=0 or q=0.

    # Weyl orbit of (p,q):
    vertices = [
        (p, q), (-p, p+q), (p+q, -q),
        (-p-q, p), (q, -p-q), (-q, -p)
    ]
    # Convert to orthogonal coordinates for the convex hull test
    def to_orth(m1, m2):
        e1 = (2*m1 + m2) / 3.0
        e2 = (-m1 + m2) / 3.0
        return (e1, e2)

    v_orth = [to_orth(m1, m2) for m1, m2 in vertices]

    # Compute the convex hull boundary as half-plane inequalities.
    # For SU(3), a weight (m1, m2) is in the convex hull of D^{(p,q)} iff:
    #   e1 - e2 <= p     (i.e., m1 <= p)
    #   e2 - e3 <= q     (i.e., m2 <= q)
    #   e1 - e3 <= p+q   (i.e., m1+m2 <= p+q)
    #   e2 - e1 <= q     (i.e., -m1 <= q, or m1 >= -q)
    #   e3 - e2 <= p     (i.e., -m2 <= p, or m2 >= -p)
    #   e3 - e1 <= p+q   (i.e., -(m1+m2) <= p+q, or m1+m2 >= -(p+q))
    #
    # Wait: in Dynkin labels, m1 = e1-e2 and m2 = e2-e3. The six conditions are:
    # (1) e1 - e2 <= (e1-e2)_max over Weyl orbit = max(p, p+q, q, ...). Hmm.
    # Actually the conditions for (m1, m2) to be in the convex hull are simply:
    # the weight must satisfy the half-space conditions defined by the hexagonal boundary.
    # For SU(3) with highest weight (p,q), the weight (m1,m2) is inside iff:
    #   m1 <= p + min(0, m2)  ... no, this isn't right either.
    #
    # Let me just use the known SU(3) result directly.
    # A weight mu = (m1, m2) is in D^{(p,q)} iff there exist non-negative integers a, b such that:
    # m1 = p - 2a + b and m2 = q + a - 2b
    # with 0 <= a, 0 <= b.
    # From these: a = (2*m2 - 2*q + m1 - p + 2*a_again... )
    # Let me solve: a = (p - m1 + b)/2 ... wait, need integer solutions.
    # m1 = p - 2a + b => 2a = p - m1 + b => a = (p - m1 + b)/2
    # m2 = q + a - 2b => a = m2 - q + 2b
    # So: (p - m1 + b)/2 = m2 - q + 2b
    # p - m1 + b = 2m2 - 2q + 4b
    # p - m1 - 2m2 + 2q = 3b
    # b = (p + 2q - m1 - 2m2) / 3
    # a = m2 - q + 2b = m2 - q + 2(p + 2q - m1 - 2m2)/3
    #   = (3m2 - 3q + 2p + 4q - 2m1 - 4m2)/3
    #   = (2p + q - 2m1 - m2)/3
    #
    # So given (m1, m2):
    #   a = (2p + q - 2m1 - m2) / 3
    #   b = (p + 2q - m1 - 2m2) / 3
    # Weight exists iff a, b are non-negative integers.
    # Also need a+b = (3p + 3q - 3m1 - 3m2)/3 = (p+q) - (m1+m2)/... wait:
    # a + b = (2p+q-2m1-m2 + p+2q-m1-2m2)/3 = (3p+3q-3m1-3m2)/3 = p+q-m1-m2
    # Hmm, that means a+b = p+q - (m1+m2).
    # And c (depth in alpha_1+alpha_2 direction) is related to the third positive root.
    #
    # Conditions: a >= 0, b >= 0, and both are integers.
    # From a = (2p+q-2m1-m2)/3 and b = (p+2q-m1-2m2)/3:
    # - a >= 0: 2p+q >= 2m1+m2
    # - b >= 0: p+2q >= m1+2m2
    # - Integer: (2p+q-2m1-m2) mod 3 = 0 and (p+2q-m1-2m2) mod 3 = 0
    # Note: if one is divisible by 3, the other is too (since their sum is 3(p+q-m1-m2)).
    # Also need: a >= 0 AND b >= 0 AND a+b >= 0 (which is automatic).
    # Additionally, the weight should have non-negative multiplicity (checked by Freudenthal).

    # Enumerate weights: scan (m1, m2) on the lattice where (2p+q-2m1-m2) mod 3 = 0.
    # The range of m1: from the conditions, m1 <= p+q (from m2 >= -(p) and a>=0)
    # and m1 >= -(p+q).
    # Similarly m2 ranges from -(p+q) to p+q.

    all_weights = {}
    max_range = p + q + 1

    for m1 in range(-max_range, max_range + 1):
        for m2 in range(-max_range, max_range + 1):
            a3 = 2*p + q - 2*m1 - m2
            b3 = p + 2*q - m1 - 2*m2
            if a3 % 3 != 0 or b3 % 3 != 0:
                continue
            a = a3 // 3
            b = b3 // 3
            if a < 0 or b < 0:
                continue
            all_weights[(m1, m2)] = 0

    if len(all_weights) == 0:
        return [(p, q, 1)]

    # Verify dimension count matches expected
    expected_dim = (p + 1) * (q + 1) * (p + q + 2) // 2
    # (The sum of multiplicities should equal expected_dim, checked after Freudenthal)

    # Freudenthal recursion for multiplicities
    pos_roots = [(2, -1), (-1, 2), (1, 1)]

    def inner(mu, nu):
        return (2*mu[0]*nu[0] + mu[0]*nu[1] + mu[1]*nu[0] + 2*mu[1]*nu[1]) / 3.0

    Lambda = (p, q)
    Lambda_rho_sq = inner((p+1, q+1), (p+1, q+1))

    # Sort by decreasing "height" relative to highest weight
    # Height = a + b = p + q - m1 - m2
    weight_list = sorted(all_weights.keys(), key=lambda w: -(w[0] + w[1]))

    all_weights[Lambda] = 1

    for mu in weight_list:
        if mu == Lambda:
            continue

        mu_rho_sq = inner((mu[0]+1, mu[1]+1), (mu[0]+1, mu[1]+1))
        denom = Lambda_rho_sq - mu_rho_sq

        if abs(denom) < 1e-10:
            all_weights[mu] = 0
            continue

        numer = 0.0
        for alpha in pos_roots:
            k = 1
            while True:
                shifted = (mu[0] + k*alpha[0], mu[1] + k*alpha[1])
                if shifted in all_weights and all_weights[shifted] > 0:
                    numer += 2 * inner(shifted, alpha) * all_weights[shifted]
                    k += 1
                else:
                    break

        mult = numer / denom
        all_weights[mu] = max(0, int(round(mult)))

    result = [(m1, m2, mult) for (m1, m2), mult in all_weights.items() if mult > 0]
    return result


def branch_su3_to_su2_u1(p, q):
    """
    Branch D^{(p,q)} of SU(3) into SU(2) x U(1) multiplets.

    Convention: SU(2) = upper-left block of SU(3).
      I_3 = m1/2  (half the first Dynkin label)
      Y = (m1 + 2*m2)/3  (hypercharge)

    Returns: list of (j, Y_value, multiplicity_of_multiplet) where each SU(2) multiplet
    contributes (2j+1) states all with the same Y.

    Also returns b_1, b_2, Delta_b:
      b_1 = sum over all states of Y^2
      b_2 = sum over all SU(2) multiplets of (2j+1) * j*(j+1)
      Delta_b = b_1 - b_2
    """
    weights = su3_weights(p, q)

    # Group by Y value
    y_groups = defaultdict(list)  # Y -> list of (I_3, multiplicity)
    for m1, m2, mult in weights:
        Y = (m1 + 2*m2) / 3.0
        I3 = m1 / 2.0
        y_groups[Y].append((I3, mult))

    # For each Y value, decompose into SU(2) multiplets
    # States at fixed Y with I_3 values form SU(2) multiplets.
    # A j-multiplet has I_3 = -j, -j+1, ..., j (2j+1 values)

    multiplets = []
    b_1 = 0.0
    b_2 = 0.0
    total_dim = 0

    for Y, states in y_groups.items():
        # states is a list of (I3, mult) pairs
        # Sort by decreasing |I3|
        i3_mults = defaultdict(int)
        for i3, mult in states:
            i3_mults[i3] += mult  # should just be mult since weights are unique

        # Decompose: find highest I3, that determines j, subtract the multiplet, repeat
        remaining = dict(i3_mults)

        while any(v > 0 for v in remaining.values()):
            # Find the maximum |I3| with nonzero multiplicity
            max_i3 = max((i3 for i3, m in remaining.items() if m > 0), key=abs, default=None)
            if max_i3 is None:
                break

            j = abs(max_i3)
            # This j-multiplet has I3 = -j, -j+1/2, ..., j (step 1)
            # Wait: I3 steps by integers for integer j, half-integers for half-integer j
            # Actually I3 takes values -j, -j+1, ..., j (always step 1)

            # Check we have all the I3 values for this j
            valid = True
            for i3_val_2 in range(int(-2*j), int(2*j) + 1, 2):
                i3_val = i3_val_2 / 2.0
                if remaining.get(i3_val, 0) <= 0:
                    valid = False
                    break

            if not valid:
                # Something wrong -- try the other sign
                # This shouldn't happen with correct weight enumeration
                print(f"WARNING: Cannot form j={j} multiplet at Y={Y} in ({p},{q})")
                # Remove this problematic I3 value
                remaining[max_i3] = 0
                continue

            # Subtract one j-multiplet
            for i3_val_2 in range(int(-2*j), int(2*j) + 1, 2):
                i3_val = i3_val_2 / 2.0
                remaining[i3_val] -= 1

            dim_multiplet = int(2*j + 1)
            multiplets.append((j, Y, 1))

            # b_1: each state in this multiplet contributes Y^2
            b_1 += dim_multiplet * Y**2

            # b_2: this multiplet contributes (2j+1) * j*(j+1)
            b_2 += dim_multiplet * j * (j + 1)

            total_dim += dim_multiplet

    # Verify dimension
    expected_dim = (p + 1) * (q + 1) * (p + q + 2) // 2
    if total_dim != expected_dim:
        print(f"WARNING: dimension mismatch for ({p},{q}): got {total_dim}, expected {expected_dim}")

    Delta_b = b_1 - b_2
    return multiplets, b_1, b_2, Delta_b


def compute_all_branching(max_pq=6):
    """Compute branching coefficients for all (p,q) sectors with p+q <= max_pq."""
    results = {}
    print("Computing SU(3) -> SU(2) x U(1) branching coefficients:")
    print(f"{'(p,q)':>8s} {'dim':>6s} {'b_1':>10s} {'b_2':>10s} {'Delta_b':>10s}")
    print("-" * 50)

    for p in range(max_pq + 1):
        for q in range(max_pq + 1 - p):
            multiplets, b1, b2, db = branch_su3_to_su2_u1(p, q)
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            results[(p, q)] = {'b1': b1, 'b2': b2, 'Delta_b': db, 'dim': dim_pq}
            print(f"({p},{q}):   {dim_pq:6d} {b1:10.4f} {b2:10.4f} {db:10.4f}")

    return results


# ============================================================
# PART 2: Verify branching with known cases
# ============================================================

def verify_branching():
    """Verify branching rules against known decompositions."""
    print("\n=== VERIFICATION ===")

    # Fundamental (1,0) = 3: decomposes as (j=1/2, Y=1/3) + (j=0, Y=-2/3)
    m, b1, b2, db = branch_su3_to_su2_u1(1, 0)
    print(f"\n(1,0) = 3: b1={b1:.4f}, b2={b2:.4f}, Delta_b={db:.4f}")
    print(f"  Expected: b1 = 2*(1/3)^2 + 1*(-2/3)^2 = 2/9 + 4/9 = 6/9 = {6/9:.4f}")
    print(f"  Expected: b2 = 2*(1/2)*(3/2) + 0 = 3/2 ... no")
    # b2 = sum over multiplets of (2j+1)*j*(j+1)
    # j=1/2 multiplet (dim 2): 2 * (1/2)*(3/2) = 3/2
    # j=0 multiplet (dim 1): 1 * 0 = 0
    # b2 = 3/2
    print(f"  Expected: b2 = 2*(1/2)*(3/2) + 0 = {3/2:.4f}")
    assert abs(b1 - 6/9) < 1e-10, f"b1 mismatch for (1,0): {b1} vs {6/9}"
    assert abs(b2 - 3/2) < 1e-10, f"b2 mismatch for (1,0): {b2} vs {3/2}"
    print("  PASS")

    # Anti-fundamental (0,1) = 3-bar: (j=1/2, Y=-1/3) + (j=0, Y=2/3)
    m, b1, b2, db = branch_su3_to_su2_u1(0, 1)
    print(f"\n(0,1) = 3-bar: b1={b1:.4f}, b2={b2:.4f}, Delta_b={db:.4f}")
    print(f"  Expected: b1 = 2*(1/3)^2 + 1*(2/3)^2 = 2/9 + 4/9 = {6/9:.4f}")
    print(f"  Expected: b2 = {3/2:.4f}")
    assert abs(b1 - 6/9) < 1e-10, f"b1 mismatch for (0,1): {b1}"
    assert abs(b2 - 3/2) < 1e-10, f"b2 mismatch for (0,1): {b2}"
    print("  PASS")

    # Check conjugation: Delta_b(p,q) vs Delta_b(q,p)
    # For (1,0) and (0,1), b1 and b2 should be the same (same Casimirs).
    db_10 = branch_su3_to_su2_u1(1, 0)[3]
    db_01 = branch_su3_to_su2_u1(0, 1)[3]
    print(f"\nConjugation check: Delta_b(1,0) = {db_10:.6f}, Delta_b(0,1) = {db_01:.6f}")
    print(f"  Same? {abs(db_10 - db_01) < 1e-10}")
    # NOTE: Delta_b(p,q) = Delta_b(q,p) by conjugation symmetry!
    # This means simple Delta_b weighting PRESERVES conjugation symmetry.
    # The escape from the conjugation trap requires ANISOTROPIC weights
    # that distinguish different eigenvalues within the same (p,q) sector.
    # But wait -- the eigenvalues ARE sector-specific. The sum S_signed
    # weights EACH EIGENVALUE by Delta_b of its sector. Since Delta_b(p,q) = Delta_b(q,p),
    # and eigenvalues of (p,q) and (q,p) are identical, the signed sum is:
    # S_signed = sum_{p<=q} 2*Delta_b(p,q)*sum_n ln(lambda_n^2) + sum_{p=q} Delta_b(p,p)*sum_n ln(lambda_n^2)
    # This is NOT necessarily zero because ln(lambda^2) != 0.
    # The SIMPLE charge (p-q) gives zero because (p-q) + (q-p) = 0.
    # But Delta_b is SYMMETRIC under (p,q)<->(q,p), so the sum doesn't cancel.

    # Adjoint (1,1) = 8
    m, b1, b2, db = branch_su3_to_su2_u1(1, 1)
    dim_11 = 8
    print(f"\n(1,1) = 8 (adjoint): b1={b1:.4f}, b2={b2:.4f}, Delta_b={db:.4f}")
    # 8 -> (j=1, Y=0) + (j=1/2, Y=1) + (j=1/2, Y=-1) + (j=0, Y=0)
    # b1 = 3*0 + 2*1 + 2*1 + 1*0 = 4
    # b2 = 3*1*2 + 2*(1/2)*(3/2) + 2*(1/2)*(3/2) + 0 = 6 + 3/2 + 3/2 = 9
    print(f"  Expected: b1 = 4.0000, b2 = 9.0000, Delta_b = -5.0000")
    assert abs(b1 - 4.0) < 1e-10, f"b1 mismatch for (1,1): {b1}"
    assert abs(b2 - 9.0) < 1e-10, f"b2 mismatch for (1,1): {b2}"
    print("  PASS")

    # (2,0) = 6 (symmetric tensor)
    m, b1, b2, db = branch_su3_to_su2_u1(2, 0)
    print(f"\n(2,0) = 6: b1={b1:.4f}, b2={b2:.4f}, Delta_b={db:.4f}")
    # 6 -> (j=1, Y=2/3) + (j=1/2, Y=-1/3) + (j=0, Y=-4/3)
    # b1 = 3*(2/3)^2 + 2*(1/3)^2 + 1*(4/3)^2 = 3*4/9 + 2/9 + 16/9 = 12/9 + 2/9 + 16/9 = 30/9 = 10/3
    # b2 = 3*1*2 + 2*(1/2)*(3/2) + 0 = 6 + 3/2 = 15/2
    print(f"  Expected: b1 = {10/3:.4f}, b2 = {15/2:.4f}")
    assert abs(b1 - 10/3) < 1e-10, f"b1 mismatch for (2,0): {b1}"
    assert abs(b2 - 15/2) < 1e-10, f"b2 mismatch for (2,0): {b2}"
    print("  PASS")

    print("\n=== ALL VERIFICATIONS PASSED ===")


# ============================================================
# PART 3: T''(0) COMPUTATION
# ============================================================

def compute_T_double_prime(branching, data_file='tier0-computation/s19a_sweep_data.npz'):
    """
    Compute T''(0) = (1/64pi^2) Sum_n Delta_b(n) * [d^2 lambda_n/dtau^2 * (1/lambda_n) - (d lambda_n/dtau)^2 * (1/lambda_n^2)] at tau=0

    Uses forward 2nd-order finite differences from the 21-point tau grid (dtau = 0.1).
    """
    print("\n" + "="*60)
    print("P0-2: T''(0) SIGN GATE COMPUTATION")
    print("="*60)

    d = np.load(data_file, allow_pickle=True)
    tau_values = d['tau_values']
    dtau = tau_values[1] - tau_values[0]
    print(f"tau grid: {tau_values[:5]}... dtau={dtau}")

    # Load eigenvalues at tau=0, 0.1, 0.2, 0.3 for derivatives
    evals = []
    sectors_p = []
    sectors_q = []
    for i in range(4):
        evals.append(d[f'eigenvalues_{i}'])
        sectors_p.append(d[f'sector_p_{i}'])
        sectors_q.append(d[f'sector_q_{i}'])

    # Eigenvalues are lambda (not lambda^2). They should be positive (|eigenvalue|).
    # At tau=0, the eigenvalues are the D_K eigenvalues on round SU(3).

    n_evals = len(evals[0])
    print(f"Number of eigenvalues per tau: {n_evals}")

    # Check: are eigenvalues sorted consistently across tau values?
    # They should be indexed consistently (same sector assignment).
    # Verify sector labels are the same at all tau
    assert np.all(sectors_p[0] == sectors_p[1]) and np.all(sectors_p[0] == sectors_p[2])
    assert np.all(sectors_q[0] == sectors_q[1]) and np.all(sectors_q[0] == sectors_q[2])
    print("Sector labels consistent across tau values: YES")

    p_arr = sectors_p[0]
    q_arr = sectors_q[0]
    lam0 = np.abs(evals[0])  # eigenvalues at tau=0
    lam1 = np.abs(evals[1])  # at tau=0.1
    lam2 = np.abs(evals[2])  # at tau=0.2
    lam3 = np.abs(evals[3])  # at tau=0.3

    # Forward 2nd-order finite differences at tau=0:
    # d(lambda)/dtau |_0 = (-3*lam0 + 4*lam1 - lam2) / (2*dtau)
    # d^2(lambda)/dtau^2 |_0 = (2*lam0 - 5*lam1 + 4*lam2 - lam3) / dtau^2

    dlam = (-3*lam0 + 4*lam1 - lam2) / (2*dtau)
    d2lam = (2*lam0 - 5*lam1 + 4*lam2 - lam3) / (dtau**2)

    # Get Delta_b for each eigenvalue based on its (p,q) sector
    delta_b = np.zeros(n_evals)
    missing_sectors = set()
    for i in range(n_evals):
        key = (int(p_arr[i]), int(q_arr[i]))
        if key in branching:
            delta_b[i] = branching[key]['Delta_b']
        else:
            missing_sectors.add(key)
            delta_b[i] = 0.0

    if missing_sectors:
        print(f"WARNING: Missing branching for sectors: {missing_sectors}")

    # T''(0) = (1/64pi^2) * Sum_n Delta_b(n) * [d2lam_n/lam_n - (dlam_n/lam_n)^2]
    # Guard against division by zero
    safe_mask = lam0 > 1e-10

    term1 = np.zeros(n_evals)
    term2 = np.zeros(n_evals)
    term1[safe_mask] = d2lam[safe_mask] / lam0[safe_mask]
    term2[safe_mask] = (dlam[safe_mask] / lam0[safe_mask])**2

    integrand = delta_b * (term1 - term2)

    T_double_prime = np.sum(integrand) / (64 * np.pi**2)

    print(f"\n--- T''(0) RESULT ---")
    print(f"T''(0) = {T_double_prime:.6e}")
    print(f"Sign: {'POSITIVE' if T_double_prime > 0 else 'NEGATIVE or ZERO'}")
    print(f"")

    # Decompose by sector for diagnostics
    print(f"{'(p,q)':>8s} {'Delta_b':>10s} {'N_evals':>8s} {'Contribution':>14s} {'Cumulative':>14s}")
    print("-" * 60)

    cum_sum = 0.0
    sector_contributions = {}
    for p in range(7):
        for q in range(7 - p):
            mask = (p_arr == p) & (q_arr == q)
            if mask.sum() == 0:
                continue
            contrib = np.sum(integrand[mask]) / (64 * np.pi**2)
            cum_sum += contrib
            sector_contributions[(p,q)] = contrib
            key = (p, q)
            db = branching.get(key, {}).get('Delta_b', 0)
            print(f"({p},{q}):   {db:10.4f} {mask.sum():8d} {contrib:14.6e} {cum_sum:14.6e}")

    # Also compute with multiplicities (each eigenvalue represents mult_n states)
    mults = d['multiplicities_0']
    integrand_weighted = delta_b * (term1 - term2) * mults
    T_double_prime_weighted = np.sum(integrand_weighted) / (64 * np.pi**2)
    print(f"\nT''(0) with multiplicities: {T_double_prime_weighted:.6e}")
    print(f"Sign (weighted): {'POSITIVE' if T_double_prime_weighted > 0 else 'NEGATIVE or ZERO'}")

    # Also try the fermionic multiplicities
    fmults = d['fermionic_mult_0']
    integrand_fweighted = delta_b * (term1 - term2) * fmults
    T_double_prime_fweighted = np.sum(integrand_fweighted) / (64 * np.pi**2)
    print(f"T''(0) with fermionic mults: {T_double_prime_fweighted:.6e}")

    # Constraint Gate ASSESSMENT
    print("\n" + "="*60)
    print("T''(0) Constraint Gate ASSESSMENT")
    print("="*60)

    # Use the unweighted version (each distinct eigenvalue counted once)
    T_val = T_double_prime
    if T_val <= 0:
        print("*** CLOSED: T''(0) <= 0 ***")
        print("The self-consistency map has NO non-trivial fixed point at tau > 0.")
        print("The self-consistency route is CLOSED at perturbative level.")
        verdict = "CLOSED"
    else:
        # Assess magnitude
        # T'(0) should be 1 at tree level (identity map). Ratio T''(0)/T'(0) matters.
        ratio = abs(T_val) / 1.0  # T'(0) = 1 at tree level
        if ratio < 0.1:
            print(f"INTERESTING: T''(0) > 0 but T''(0)/T'(0) = {ratio:.4f} < 0.1 (weak)")
            verdict = "INTERESTING"
        elif ratio > 0.5:
            print(f"COMPELLING: T''(0) > 0 AND T''(0)/T'(0) = {ratio:.4f} > 0.5 (strong)")
            verdict = "COMPELLING"
        else:
            print(f"INTERESTING-to-COMPELLING: T''(0)/T'(0) = {ratio:.4f}")
            verdict = "INTERESTING"

    print(f"\nVERDICT: {verdict}")

    # Also report T''(0) for weighted version
    print(f"\n--- Weighted results ---")
    T_val_w = T_double_prime_weighted
    if T_val_w <= 0:
        print(f"Weighted (multiplicities): CLOSED (T''(0) = {T_val_w:.6e})")
    else:
        print(f"Weighted (multiplicities): T''(0) = {T_val_w:.6e} > 0 (ALIVE)")

    return T_double_prime, T_double_prime_weighted, sector_contributions, verdict


# ============================================================
# PART 4: S_signed(tau) COMPUTATION
# ============================================================

def compute_S_signed(branching, data_file='tier0-computation/s19a_sweep_data.npz'):
    """
    Compute S_signed(tau) = Sum_{(p,q)} Sum_{n in (p,q)} [b_1(p,q) - b_2(p,q)] * ln(lambda_n^2(tau))

    for all 21 tau values in the sweep data.
    """
    print("\n" + "="*60)
    print("P0-3: S_signed(tau) COMPUTATION")
    print("="*60)

    d = np.load(data_file, allow_pickle=True)
    tau_values = d['tau_values']
    n_tau = len(tau_values)

    # Get sector labels (same at all tau)
    p_arr = d['sector_p_0']
    q_arr = d['sector_q_0']
    mults = d['multiplicities_0']
    n_evals = len(p_arr)

    # Build Delta_b array
    delta_b = np.zeros(n_evals)
    for i in range(n_evals):
        key = (int(p_arr[i]), int(q_arr[i]))
        if key in branching:
            delta_b[i] = branching[key]['Delta_b']

    # Compute S_signed at each tau
    S_signed = np.zeros(n_tau)
    S_signed_weighted = np.zeros(n_tau)  # with multiplicities

    # Also compute per-sector contributions for diagnostic
    sector_S = {}

    for t_idx in range(n_tau):
        tau = tau_values[t_idx]
        evals = np.abs(d[f'eigenvalues_{t_idx}'])

        # Guard against log(0)
        safe_mask = evals > 1e-15
        ln_lam_sq = np.zeros(n_evals)
        ln_lam_sq[safe_mask] = np.log(evals[safe_mask]**2)

        S_signed[t_idx] = np.sum(delta_b * ln_lam_sq)
        S_signed_weighted[t_idx] = np.sum(delta_b * ln_lam_sq * mults)

    print(f"\nS_signed(tau) results:")
    print(f"{'tau':>6s} {'S_signed':>14s} {'S_signed_wt':>14s}")
    print("-" * 40)
    for t_idx in range(n_tau):
        print(f"{tau_values[t_idx]:6.2f} {S_signed[t_idx]:14.4f} {S_signed_weighted[t_idx]:14.4f}")

    # Find minimum
    min_idx = np.argmin(S_signed)
    min_tau = tau_values[min_idx]
    min_val = S_signed[min_idx]

    min_idx_w = np.argmin(S_signed_weighted)
    min_tau_w = tau_values[min_idx_w]
    min_val_w = S_signed_weighted[min_idx_w]

    print(f"\nS_signed minimum (unweighted): tau = {min_tau:.2f}, S = {min_val:.4f}")
    print(f"S_signed minimum (weighted):   tau = {min_tau_w:.2f}, S = {min_val_w:.4f}")

    # Check monotonicity
    dS = np.diff(S_signed)
    is_monotonic = np.all(dS >= 0) or np.all(dS <= 0)
    direction = "increasing" if np.all(dS >= 0) else ("decreasing" if np.all(dS <= 0) else "non-monotonic")

    dS_w = np.diff(S_signed_weighted)
    is_monotonic_w = np.all(dS_w >= 0) or np.all(dS_w <= 0)
    direction_w = "increasing" if np.all(dS_w >= 0) else ("decreasing" if np.all(dS_w <= 0) else "non-monotonic")

    print(f"\nMonotonicity (unweighted): {direction}")
    print(f"Monotonicity (weighted):   {direction_w}")

    # Constraint Gate ASSESSMENT
    print("\n" + "="*60)
    print("S_signed Constraint Gate ASSESSMENT")
    print("="*60)

    if is_monotonic:
        print("*** CLOSED: S_signed is monotonic (signed sum also trapped) ***")
        verdict = "CLOSED"
    else:
        # Check if minimum is near predicted tau ~ 0.12
        if 0.08 <= min_tau <= 0.20:
            depth = abs(S_signed[0] - min_val) / abs(S_signed[0]) * 100 if abs(S_signed[0]) > 0 else 0
            if depth > 10:
                print(f"DECISIVE: Minimum at tau = {min_tau:.2f} in [0.08, 0.20] with depth {depth:.1f}%")
                verdict = "DECISIVE"
            else:
                print(f"COMPELLING: Minimum at tau = {min_tau:.2f} in [0.08, 0.20] (near prediction 0.12)")
                verdict = "COMPELLING"
        elif not is_monotonic:
            print(f"INTERESTING: S_signed non-monotonic, minimum at tau = {min_tau:.2f}")
            verdict = "INTERESTING"

    print(f"VERDICT: {verdict}")

    # PLOT
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: unweighted
    ax = axes[0]
    ax.plot(tau_values, S_signed, 'b-o', markersize=4, label='S_signed (unweighted)')
    ax.axvline(x=0.12, color='r', linestyle='--', alpha=0.7, label='Predicted min (0.12)')
    ax.axvline(x=0.15, color='g', linestyle='--', alpha=0.7, label='phi_paasch (0.15)')
    ax.axvline(x=0.30, color='orange', linestyle='--', alpha=0.7, label='Weinberg angle (0.30)')
    if not is_monotonic:
        ax.axvline(x=min_tau, color='purple', linestyle=':', linewidth=2, label=f'Actual min ({min_tau:.2f})')
        ax.plot(min_tau, min_val, 'r*', markersize=15)
    ax.set_xlabel('tau')
    ax.set_ylabel('S_signed(tau)')
    ax.set_title(f'S_signed (unweighted) — {direction}')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Right: weighted by multiplicity
    ax = axes[1]
    ax.plot(tau_values, S_signed_weighted, 'r-o', markersize=4, label='S_signed (multiplicity-weighted)')
    ax.axvline(x=0.12, color='r', linestyle='--', alpha=0.7, label='Predicted min (0.12)')
    ax.axvline(x=0.15, color='g', linestyle='--', alpha=0.7, label='phi_paasch (0.15)')
    ax.axvline(x=0.30, color='orange', linestyle='--', alpha=0.7, label='Weinberg angle (0.30)')
    if not is_monotonic_w:
        ax.axvline(x=min_tau_w, color='purple', linestyle=':', linewidth=2, label=f'Actual min ({min_tau_w:.2f})')
        ax.plot(min_tau_w, min_val_w, 'r*', markersize=15)
    ax.set_xlabel('tau')
    ax.set_ylabel('S_signed(tau)')
    ax.set_title(f'S_signed (weighted) — {direction_w}')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.suptitle('Session 21c P0-3: S_signed(tau) — Flux-Spectral Sum', fontsize=13)
    plt.tight_layout()
    plt.savefig('tier0-computation/s21c_S_signed.png', dpi=150)
    print(f"\nPlot saved: tier0-computation/s21c_S_signed.png")

    # Save data
    np.savez('tier0-computation/s21c_S_signed.npz',
             tau_values=tau_values,
             S_signed=S_signed,
             S_signed_weighted=S_signed_weighted,
             delta_b_by_eigenvalue=delta_b,
             verdict=verdict,
             min_tau=min_tau,
             min_val=min_val)
    print(f"Data saved: tier0-computation/s21c_S_signed.npz")

    return tau_values, S_signed, S_signed_weighted, verdict


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == '__main__':
    print("Session 21c — P0-2: T''(0) + P0-3: S_signed(tau)")
    print("=" * 60)

    # Step 1: Verify branching rules
    verify_branching()

    # Step 2: Compute all branching coefficients
    branching = compute_all_branching(max_pq=6)

    # Step 3: P0-2 — T''(0) sign gate
    T_val, T_val_w, sector_contribs, verdict_T = compute_T_double_prime(branching)

    # Step 4: P0-3 — S_signed(tau)
    tau_vals, S_signed, S_signed_w, verdict_S = compute_S_signed(branching)

    # Step 5: Write T''(0) result file
    with open('tier0-computation/s21c_T_double_prime_result.txt', 'w') as f:
        f.write("Session 21c — P0-2: T''(0) Sign Gate Result\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"T''(0) (unweighted, per eigenvalue): {T_val:.6e}\n")
        f.write(f"T''(0) (multiplicity-weighted):       {T_val_w:.6e}\n")
        f.write(f"Sign (unweighted): {'POSITIVE' if T_val > 0 else 'NON-POSITIVE'}\n")
        f.write(f"Sign (weighted):   {'POSITIVE' if T_val_w > 0 else 'NON-POSITIVE'}\n")
        f.write(f"\nVERDICT: {verdict_T}\n")
        f.write(f"\nPre-registered gate: T''(0) > 0 = ALIVE, T''(0) <= 0 = CLOSED\n")
        f.write(f"\nS_signed verdict: {verdict_S}\n")
        if not np.all(np.diff(S_signed) >= 0) and not np.all(np.diff(S_signed) <= 0):
            min_idx = np.argmin(S_signed)
            f.write(f"S_signed minimum at tau = {tau_vals[min_idx]:.2f}\n")
            f.write(f"Pre-registered prediction: tau ~ 0.12\n")

        f.write(f"\n\nBranching coefficients Delta_b(p,q):\n")
        f.write(f"{'(p,q)':>8s} {'dim':>6s} {'b_1':>10s} {'b_2':>10s} {'Delta_b':>10s}\n")
        f.write("-" * 50 + "\n")
        for (p, q), vals in sorted(branching.items()):
            f.write(f"({p},{q}):   {vals['dim']:6d} {vals['b1']:10.4f} {vals['b2']:10.4f} {vals['Delta_b']:10.4f}\n")

        f.write(f"\n\nSector-by-sector T''(0) contributions:\n")
        for (p, q), contrib in sorted(sector_contribs.items()):
            f.write(f"  ({p},{q}): {contrib:14.6e}\n")

    print(f"\nResult file saved: tier0-computation/s21c_T_double_prime_result.txt")

    # Summary
    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)
    print(f"P0-2 (T''(0)):   {verdict_T}  (T''(0) = {T_val:.6e})")
    print(f"P0-3 (S_signed): {verdict_S}")
    print("="*60)
