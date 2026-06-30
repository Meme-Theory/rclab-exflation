#!/usr/bin/env python3
"""
CSDR-BRANCHING-63 (W5-07): Forgacs-Manton CSDR Branching Rules
================================================================

Computes CSDR branching for SU(3) irreps decomposed under U(2) ⊂ SU(3).
Determines B/F sector assignment for LOG-SIGNED-41 conditional pass resolution.

MATHEMATICAL SETUP
==================

The framework M^4 × SU(3) has isometry (SU(3)_L × SU(3)_R) / Z_3.
After Jensen deformation, the isometry breaks to (SU(3)_L × U(2)_R) with:
    SU(3)_C = SU(3)_L  (color)
    SU(2)_L × U(1)_Y = U(2) ⊂ SU(3)_R  (electroweak)

U(2) embedding (Baptista eq 3.61):
    phi: U(2) → SU(3),  phi(a) = diag(det(a)^{-1}, a)

KK modes in Dirac sector (p,q):
    Under SU(3)_L: transform as (p,q) of SU(3)_C
    Under SU(3)_R: transform as (q,p) (dual, right action)
        → branches into SU(2)_L × U(1)_Y representations

BRANCHING RULES
===============

For the Baptista embedding phi(a) = diag(det(a)^{-1}, a), the fundamental
representation 3 = (1,0) of SU(3) decomposes under SU(2) × U(1) as:

    (1,0)|_{SU(2)×U(1)} = (0)_{-2} ⊕ (1/2)_{+1}

where (j)_Y denotes SU(2) spin j and hypercharge Y (the U(1) charge from
the embedding, with Y = diag(-2, 1, 1) on the fundamental).

The anti-fundamental 3bar = (0,1) decomposes as:

    (0,1)|_{SU(2)×U(1)} = (0)_{+2} ⊕ (1/2)_{-1}

Higher representations are computed by tensor products + symmetrization.

CSDR B/F ASSIGNMENT
===================

In the Forgacs-Manton CSDR framework on a coset S = G/H:
- Higher-D gauge fields A_M decompose as A_μ (4D vectors = bosons) and
  A_I (internal = 4D scalars = bosons)
- Higher-D spinors Ψ decompose according to their Spin(D_int) representation
  under H, giving 4D spinors (fermions)

For our setup with P = M^4 × SU(3):
- Bosonic KK modes come from the metric and gauge field fluctuations
  → these transform under the ADJOINT of SU(3) (from isometry generators)
- Fermionic KK modes come from the spinor field Δ_8
  → these transform under SPINOR representations of Spin(8) restricted to SU(3)

The B/F classification per (p,q) sector:
- BOSONIC: modes from metric/gauge fluctuations. The adj(SU(3)) = (1,1) sector
  plus scalar modes from symmetric tensors.
- FERMIONIC: modes from spinor fluctuations. The spinor Δ_8|_{SU(3)} content.

For the LOG-SIGNED-41 resolution, we need the B/F weight per eigenvalue in
each (p,q) sector. This is determined by:
1. The SU(3)_R representation content of that sector
2. The U(2) branching of that representation
3. The Spin statistics: integer-spin (bosonic) vs half-integer-spin (fermionic)
   in the 4D theory

COMPUTATION
===========

We compute:
1. Branching of ALL (p,q) sectors up to p+q ≤ 6 under SU(2)×U(1)
2. The adjoint (1,1) decomposition (gives gauge + Higgs content)
3. The spinor Δ_8 decomposition (gives fermionic content)
4. Complete B/F assignment table
5. Effective A parameter for LOG-SIGNED-41

Output: s63_csdr_branching.npz
Gate: INFO with complete branching table

Author: KK Theorist Agent
Date: 2026-03-30
"""

import numpy as np
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *

print("=" * 78)
print("CSDR-BRANCHING-63: Forgacs-Manton CSDR Branching Rules for M^4 × SU(3)")
print("=" * 78)

# =============================================================================
# SECTION 1: SU(3) → SU(2) × U(1) Branching via Weight Theory
# =============================================================================

# The weights of SU(3) irrep (p,q) in the Dynkin basis are labeled by
# (m_1, m_2) with constraints from the Young diagram structure.
# The highest weight is (p, q) in Dynkin labels.
#
# For the Baptista U(2) embedding phi(a) = diag(det(a)^{-1}, a):
# - The Cartan subalgebra of SU(2)×U(1) maps to:
#   T_3 = diag(0, 1/2, -1/2)  (isospin)
#   Y   = diag(-2, 1, 1)       (hypercharge)
# - On a weight state |w⟩ of SU(3), the SU(2) and U(1) quantum numbers are
#   determined by the restriction of the weight to these generators.

def su3_weights(p, q):
    """
    Compute all weights of SU(3) irrep (p,q) in the (T_3, Y) basis.

    Uses the Gelfand-Tsetlin pattern enumeration.

    Returns: list of (T3, Y, multiplicity) tuples.

    A weight of (p,q) in the orthogonal basis (e_1, e_2, e_3) is
    (n_1, n_2, n_3) with n_1 ≥ n_2 ≥ n_3 and sum = 0 (traceless).

    More efficiently: use the standard branching formula.
    For SU(3) → SU(2) × U(1) with the standard embedding:

    (p,q)|_{SU(2)×U(1)} = ⊕ (j)_Y

    where the sum runs over all states in the weight diagram.
    """
    # We use the explicit weight enumeration via Gelfand-Tsetlin patterns.
    # For SU(3), the patterns are:
    #   m_13 ≥ m_12 ≥ m_23 ≥ 0 (standard ordering for SU(3))
    #   m_13 ≥ m_11 ≥ m_12
    #   m_12 ≥ m_22 ≥ m_23
    #
    # Highest weight in partition notation: (p+q, q, 0)
    # GT pattern top row: (m_13, m_23) = (p+q, q) [with implicit 0]

    # Actually, let's use a cleaner approach: enumerate all SU(2) content.

    # The branching SU(3) → SU(2)×U(1) with the STANDARD maximal embedding
    # where SU(2) acts on indices {2,3} and U(1) is generated by diag(-2,1,1)/3
    # is given by:
    #
    # (p,q) → ⊕_{k=0}^{q} ⊕_{l=0}^{p} (j = (k+l)/2)_{Y = p - q - 3(k-l)... }
    #
    # NO. Let me use the CORRECT standard formula.
    #
    # For SU(3) → SU(2) × U(1) with the block embedding
    #   SU(2) ⊂ SU(3) acts on last 2 indices
    #   U(1) generated by Y = diag(-2, 1, 1)
    #
    # The SU(3) irrep (p,q) with Dynkin labels has the branching:
    #
    # (p,q) = ⊕_{k=0}^{min(p,q)} ⊕_{j=0}^{(p+q-2k)} [j_SU2 = (p+q-2k-j)/2 ??]

    # CORRECT APPROACH: Use the weight system directly.
    # SU(3) fundamental weights: ω_1, ω_2
    # (p,q) has highest weight p*ω_1 + q*ω_2
    # In the orthogonal basis: ω_1 = (2/3, -1/3, -1/3), ω_2 = (1/3, 1/3, -2/3)
    # So highest weight = ((2p+q)/3, (q-p)/3, -(p+2q)/3)

    # Under SU(2) × U(1) with SU(2) on {2,3}:
    # T_3 = (e_2 - e_3)/2  (measures isospin)
    # Y = -(2*e_1 - e_2 - e_3)  (measures hypercharge, convention: Y = diag(-2,1,1))

    # For each weight (w_1, w_2, w_3) of (p,q):
    #   T_3 = (w_2 - w_3)/2
    #   Y = -(2*w_1 - w_2 - w_3) = -2*w_1 + w_2 + w_3
    #   Since w_1 + w_2 + w_3 = 0: Y = -3*w_1

    # So Y = -3 * w_1, T_3 = (w_2 - w_3)/2

    # The SU(2) representation content: group weights by Y value.
    # For each Y sector, T_3 ranges from -j to +j in integer steps → j = max(T_3)

    # Now enumerate all weights of (p,q).
    # Use the tensor method: (p,q) = Sym^p(fund) ⊗ Sym^q(antifund), then subtract.
    # Or use Gelfand-Tsetlin patterns directly.
    pass

def branching_su3_to_su2xu1(p, q):
    """
    Compute the branching of SU(3) irrep (p,q) under SU(2) × U(1)
    with the Baptista embedding phi(a) = diag(det(a)^{-1}, a).

    This means:
    - SU(2) acts on indices {2,3} (the lower-right 2×2 block)
    - U(1) is generated by Y = diag(-2, 1, 1) (from det(a)^{-1} on index 1)

    Returns: list of (j, Y) tuples, where j is the SU(2) spin and Y the U(1) charge.
             Each tuple appears with multiplicity 1 (no duplicate tuples).

    Method: Enumerate all weights of (p,q) using Gelfand-Tsetlin patterns,
    extract (T_3, Y) for each, then group into SU(2) multiplets.
    """

    # Step 1: Enumerate weights via Gelfand-Tsetlin patterns
    # For SU(3), the GT pattern for highest weight λ = (λ_1, λ_2) in partition form
    # where λ_1 = p + q, λ_2 = q (the partition with at most 2 parts):
    #
    # Top row: (λ_1, λ_2) = (p+q, q)
    # Second row: (m_1, m_2) with λ_1 ≥ m_1 ≥ λ_2, m_1 ≥ m_2 ≥ 0
    #   But wait, we need to be careful: standard GT for SU(3) has
    #   top row (m_{13}, m_{23}, m_{33}=0) and
    #   middle row (m_{12}, m_{22})
    #   bottom row (m_{11})
    #   with interleaving: m_{13} ≥ m_{12} ≥ m_{23}, m_{12} ≥ m_{11} ≥ m_{22}, m_{23} ≥ m_{22} ≥ 0

    # For (p,q): top row = (p+q, q, 0)
    lam1, lam2, lam3 = p + q, q, 0

    weights_orthogonal = []  # (w1, w2, w3) with w1+w2+w3=0

    for m12 in range(lam2, lam1 + 1):       # lam1 ≥ m12 ≥ lam2
        for m22 in range(lam3, min(lam2, m12) + 1):  # min(m12, lam2) ≥ m22 ≥ lam3 = 0
            for m11 in range(m22, m12 + 1):  # m12 ≥ m11 ≥ m22
                # Weight in orthogonal basis:
                # w_i = (sum of i-th column entries) - (sum of (i+1)-th column entries) + correction
                # Standard: w_1 = m11 - 0 = m11 (wait, need to be more careful)

                # GT weight formula for SU(3):
                # w_1 = m11 - (m12 + m22)/2 + (lam1 + lam2)/3
                # Wait, let me use the standard formula.

                # The weight vector (in the orthogonal e_i basis) for a GT pattern is:
                # w_k = (sum of k-th row entries) - (sum of (k+1)-th row entries)
                # where row numbering starts from bottom (row 1 = bottom = m11)

                # For SU(3), 3 rows:
                # Row 1 (bottom): m11
                # Row 2 (middle): m12, m22
                # Row 3 (top):    lam1, lam2, 0

                # w_1 = m11 - (m12 + m22)
                # w_2 = (m12 + m22) - (lam1 + lam2 + 0)
                # w_3 = (lam1 + lam2) - ... NO. This isn't right either.

                # CORRECT GT weight formula: the weight in the epsilon basis is
                # w = sum_i m_{1i} * epsilon_i  (using appropriate level sums)
                #
                # Actually, the standard result for SU(n) is:
                # w_k = (sum of entries in row k) - (sum of entries in row k-1)
                # where row n is the top (fixed) row and row 0 is empty.

                # For SU(3):
                # Row 3 (top): m13=lam1, m23=lam2, m33=0 → sum = lam1 + lam2
                # Row 2 (mid): m12, m22 → sum = m12 + m22
                # Row 1 (bot): m11 → sum = m11

                # Weight components:
                # w_1 = m11 - 0 = m11
                # w_2 = (m12 + m22) - m11
                # w_3 = (lam1 + lam2) - (m12 + m22)
                # Check: w_1 + w_2 + w_3 = lam1 + lam2 ≠ 0 in general

                # Hmm. The weight needs to be in the CENTERED basis.
                # For SU(3), the weight w = (w_1, w_2, w_3) satisfies w_1+w_2+w_3 = const.
                # We subtract the average to get traceless weights.

                w1_raw = m11
                w2_raw = (m12 + m22) - m11
                w3_raw = (lam1 + lam2) - (m12 + m22)

                # Subtract mean to get traceless (ε-basis):
                avg = (w1_raw + w2_raw + w3_raw) / 3.0
                w1 = w1_raw - avg
                w2 = w2_raw - avg
                w3 = w3_raw - avg

                weights_orthogonal.append((w1, w2, w3))

    # Verify dimension
    dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
    assert len(weights_orthogonal) == dim_pq, \
        f"(p,q)=({p},{q}): got {len(weights_orthogonal)} weights, expected {dim_pq}"

    # Step 2: Extract (T_3, Y) for each weight
    # T_3 = (w_2 - w_3) / 2   (isospin)
    # Y = -3 * w_1             (hypercharge, from Y = diag(-2,1,1) convention)
    # Actually: Y = -(2*w_1 - w_2 - w_3) = -(2*w_1 - (-w_1)) = -3*w_1
    #   since w_1 + w_2 + w_3 = 0 → w_2 + w_3 = -w_1

    t3_y_list = []
    for w1, w2, w3 in weights_orthogonal:
        T3 = (w2 - w3) / 2.0
        Y = -3.0 * w1
        t3_y_list.append((T3, Y))

    # Step 3: Group into SU(2) multiplets
    # Sort by Y value; for each Y, find max |T_3| → j = max(T_3)
    # Then subtract the j-multiplet, repeat

    remaining = list(t3_y_list)
    branches = []  # list of (j, Y)

    # Round to avoid floating point issues
    def round_qn(x):
        """Round to nearest half-integer."""
        return round(2 * x) / 2.0

    remaining_rounded = [(round_qn(t3), round_qn(y)) for t3, y in remaining]

    # Group by Y
    from collections import Counter

    y_values = sorted(set(y for _, y in remaining_rounded))

    for y_val in y_values:
        # Get all T_3 values for this Y
        t3_vals = sorted([t3 for t3, y in remaining_rounded if y == y_val])

        # Extract SU(2) multiplets
        t3_counter = Counter(t3_vals)

        while sum(t3_counter.values()) > 0:
            # Find maximum T_3 with nonzero count
            max_t3 = max(t3 for t3, cnt in t3_counter.items() if cnt > 0)
            j = max_t3  # this is the spin

            # Remove one complete multiplet: T_3 = -j, -j+1, ..., j
            t3_in_multiplet = [round_qn(-j + k) for k in range(int(2*j + 1))]

            for t3 in t3_in_multiplet:
                if t3 in t3_counter and t3_counter[t3] > 0:
                    t3_counter[t3] -= 1
                else:
                    # This shouldn't happen for a valid representation
                    raise ValueError(
                        f"(p,q)=({p},{q}), Y={y_val}: "
                        f"expected T3={t3} in multiplet j={j} but count is 0. "
                        f"Counter: {dict(t3_counter)}"
                    )

            branches.append((j, y_val))

    # Verify: total dimension matches
    total_dim = sum(int(2*j + 1) for j, _ in branches)
    assert total_dim == dim_pq, \
        f"(p,q)=({p},{q}): branching gives dim={total_dim}, expected {dim_pq}"

    return branches


# =============================================================================
# SECTION 2: Validate with Known Branchings
# =============================================================================

print("\n--- VALIDATION: Known SU(3) → SU(2)×U(1) Branchings ---\n")

# Fundamental (1,0) = 3: should give (0)_{-2} ⊕ (1/2)_{+1}
# (singlet with Y=-2 and doublet with Y=+1)
br_10 = branching_su3_to_su2xu1(1, 0)
print(f"(1,0) = 3:  branches = {br_10}")
# Check: expect [(0.0, -2.0), (0.5, 1.0)] or similar
assert len(br_10) == 2, f"Expected 2 branches for (1,0), got {len(br_10)}"

# Verify dimensions
for j, Y in br_10:
    print(f"  (j={j}, Y={Y}): dim = {int(2*j+1)}")

# Anti-fundamental (0,1) = 3bar: should give (0)_{+2} ⊕ (1/2)_{-1}
br_01 = branching_su3_to_su2xu1(0, 1)
print(f"\n(0,1) = 3bar:  branches = {br_01}")
assert len(br_01) == 2, f"Expected 2 branches for (0,1), got {len(br_01)}"

# Adjoint (1,1) = 8: should give (0)_0 ⊕ (1/2)_{-3} ⊕ (1/2)_{+3} ⊕ (1)_0
# (1 singlet + 2 doublets + 1 triplet)
# These correspond to: U(1) generator, C^2 doublet, C^2bar doublet, SU(2) triplet+singlet
# Total dim: 1 + 2 + 2 + 3 = 8 ✓
br_11 = branching_su3_to_su2xu1(1, 1)
print(f"\n(1,1) = 8 (adjoint):  branches = {br_11}")
total_11 = sum(int(2*j+1) for j, _ in br_11)
print(f"  Total dimension: {total_11}")

# (2,0) = 6:
br_20 = branching_su3_to_su2xu1(2, 0)
print(f"\n(2,0) = 6:  branches = {br_20}")
total_20 = sum(int(2*j+1) for j, _ in br_20)
print(f"  Total dimension: {total_20}")

# (0,0) = 1: trivial
br_00 = branching_su3_to_su2xu1(0, 0)
print(f"\n(0,0) = 1 (trivial):  branches = {br_00}")


# =============================================================================
# SECTION 3: Complete Branching Table for All Sectors up to p+q ≤ 6
# =============================================================================

print("\n" + "=" * 78)
print("COMPLETE BRANCHING TABLE: SU(3) → SU(2)×U(1) [Baptista embedding]")
print("=" * 78)

max_pq_sum = 6
sectors = []
for p in range(max_pq_sum + 1):
    for q in range(max_pq_sum + 1 - p):
        sectors.append((p, q))

# Store all branching data
branching_data = {}

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

for p, q in sectors:
    br = branching_su3_to_su2xu1(p, q)
    branching_data[(p, q)] = br
    dim = dim_su3(p, q)

    # Format the branches
    br_str = " ⊕ ".join([f"({j})_{{{Y:.0f}}}" if j == int(j) else f"({j:.1f})_{{{Y:.0f}}}"
                          for j, Y in sorted(br, key=lambda x: (x[1], x[0]))])

    print(f"\n({p},{q}) [dim={dim}]:  {br_str}")


# =============================================================================
# SECTION 4: Adjoint Decomposition — Gauge + Higgs Content
# =============================================================================

print("\n" + "=" * 78)
print("ADJOINT DECOMPOSITION: (1,1) = 8 → Gauge + Higgs Content")
print("=" * 78)

br_adj = branching_data[(1, 1)]

print("\nThe adjoint (1,1) = 8 of SU(3) decomposes under SU(2)×U(1) as:")
for j, Y in sorted(br_adj, key=lambda x: (x[1], x[0])):
    dim_j = int(2*j + 1)
    # Physical identification
    if j == 1.0 and Y == 0:
        phys = "→ SU(2)_L gauge bosons (W^±, W^3)"
    elif j == 0.0 and Y == 0:
        phys = "→ U(1)_Y gauge boson (B)"
    elif abs(Y) == 3.0 and j == 0.5:
        phys = f"→ C² leptoquark-type Higgs (Y={Y:.0f})"
    else:
        phys = "→ ?"
    print(f"  (j={j}, Y={Y:.0f}): dim={dim_j}  {phys}")

# The u(2) subalgebra of su(3) corresponds to:
# - (1)_0: the SU(2) adjoint (3 generators T_1, T_2, T_3)
# - (0)_0: the U(1) generator (Y)
# Together: u(2) = su(2) ⊕ u(1), dimension 3 + 1 = 4
#
# The coset su(3)/u(2) ≅ C² corresponds to:
# - (1/2)_{+3}: complex doublet (2 real dimensions)
# - (1/2)_{-3}: conjugate complex doublet (2 real dimensions)
# Together: dimension 2 + 2 = 4
# Total: 4 + 4 = 8 = dim(su(3)) ✓

print(f"\nu(2) = su(2) ⊕ u(1) content: (1)_0 ⊕ (0)_0  [dim = 3 + 1 = 4]")
print(f"C² coset content: (1/2)_{{+3}} ⊕ (1/2)_{{-3}}  [dim = 2 + 2 = 4]")
print(f"Total: 4 + 4 = 8 ✓")


# =============================================================================
# SECTION 5: Spinor Content — Fermionic KK Modes
# =============================================================================

print("\n" + "=" * 78)
print("SPINOR CONTENT: Δ_8 = 16 → Fermionic KK Mode Assignment")
print("=" * 78)

# From the branching_computation.py (existing script), the spinor Δ_8 of Spin(8)
# restricted to SU(3) ⊂ Spin(8) decomposes as:
#
# Δ_8|_{SU(3)} = (0,0) ⊕ (1,0) ⊕ (0,1) ⊕ (1,1)_traceless_part
#
# Actually, from Baptista's explicit construction (eq 2.62, 2.66):
# The 16-dim spinor Ψ_+ has blocks:
#   a (1×1):  (0,0) singlet         → 1 dim
#   c (3×1):  (1,0) fundamental     → 3 dim
#   b (3×1):  (0,1) antifundamental → 3 dim  [actually this needs checking]
#   D (3×3):  (1,1) ⊕ (0,0)        → 9 dim = 8 + 1
#
# Wait — D is a general 3×3 matrix = (1,0)⊗(0,1) under SU(3)_L × SU(3)_R.
# Under SU(3) (diagonal or specific action), this decomposes as:
#   3 ⊗ 3̄ = 8 ⊕ 1 = (1,1) ⊕ (0,0)
#
# Total: 1 + 3 + 3 + 8 + 1 = 16 ✓

# But the LEFT and RIGHT actions are DIFFERENT. The spinor decomposition under
# the COMBINED L+R action of U(2) (which is what gives SM quantum numbers)
# was computed in branching_computation.py. Let me extract the actual result.

# From the branching_computation.py, the 16-dim spinor decomposes under
# U(2) = SU(2) × U(1) (via L+R combined action) as:
#
# Based on Baptista eq 2.66, the particle identification gives:
# Slot 0 (a=1):   ν_R    → SU(2) singlet, Y = 0      → (0)_0
# Slots 1-3 (c=3): u_R^{r,g,b} → SU(2) singlet each?, Y = ...
#   Actually, c transforms as: L: -2v_{11}·c, R: v̄·c
#   Under U(2): combined action depends on whether v ∈ u(2)
#
# This is getting complicated. Let me compute it directly using the L+R matrices
# from branching_computation.py logic.

# We need the COMBINED L+R representation matrices for U(2) generators
# acting on the 16-dim spinor space.

# U(2) generators in su(3):
# Y_gen = diag(-2i, i, i) * t (hypercharge, normalized as a real parameter t)
# T_a = diag(0, -i*sigma_a/2)  (isospin, a=1,2,3)

# For the LEFT action (Baptista eq 2.62):
# L_v(a) = 0
# L_v(c) = -2*v_{11}*c    [v_{11} = v[0,0]]
# L_v(b) = (2*v_{11}*I_3 + v)*b
# L_v(D) = v*D             [left matrix multiplication]

# For the RIGHT action:
# R_v(a) = 0
# R_v(c) = conj(v)*c       [v̄ = complex conjugate of v]
# R_v(b) = 0
# R_v(D) = -D*v            [right matrix multiplication by -v]

# Combined: (L+R)_v on each block.

def compute_LplusR_16x16(v):
    """
    Compute 16×16 matrix for combined L+R action of v ∈ su(3) on Δ_8.

    Ordering: [a(1), c(3), b(3), D(9)] = 16 components
    D stored row-major: D[0,0], D[0,1], D[0,2], D[1,0], ..., D[2,2]
    """
    M = np.zeros((16, 16), dtype=complex)
    v11 = v[0, 0]
    v_conj = np.conj(v)

    # a: L(a)=0, R(a)=0 → row 0 all zero

    # c: L(c) = -2*v11*c,  R(c) = v̄*c  → (L+R)(c) = (-2*v11*I + v̄)*c
    Mc = -2 * v11 * np.eye(3, dtype=complex) + v_conj
    M[1:4, 1:4] = Mc

    # b: L(b) = (2*v11*I + v)*b,  R(b) = 0  → (L+R)(b) = (2*v11*I + v)*b
    Mb = 2 * v11 * np.eye(3, dtype=complex) + v
    M[4:7, 4:7] = Mb

    # D: L(D) = v*D,  R(D) = -D*v  → (L+R)(D) = v*D - D*v = [v, D]
    # In index form: (L+R)(D)_{ij} = sum_k v_{ik}*D_{kj} - sum_k D_{ik}*v_{kj}
    # Flattened (row-major): index = 3*i + j
    for i in range(3):
        for j in range(3):
            for k in range(3):
                # v*D term: v_{ik} * D_{kj}
                M[7 + 3*i + j, 7 + 3*k + j] += v[i, k]
                # -D*v term: -D_{ik} * v_{kj}
                M[7 + 3*i + j, 7 + 3*i + k] -= v[k, j]

    return M

# Define U(2) generators in su(3)
# Y generator: v_Y = i * diag(-2, 1, 1) * t  [we use t=1/2 for normalization]
# Note: su(3) uses anti-Hermitian convention, so v_Y = (i/2)*diag(-2, 1, 1)
v_Y = (1j / 2) * np.diag([-2.0, 1.0, 1.0])

# SU(2) generators: T_a = diag(0, -i*sigma_a/2)
sigma = [
    np.array([[0, 1], [1, 0]], dtype=complex),    # sigma_1
    np.array([[0, -1j], [1j, 0]], dtype=complex),  # sigma_2
    np.array([[1, 0], [0, -1]], dtype=complex)      # sigma_3
]

v_T = []
for a in range(3):
    v = np.zeros((3, 3), dtype=complex)
    v[1:, 1:] = -1j * sigma[a] / 2
    v_T.append(v)

# Verify these are in su(3) (anti-Hermitian, traceless)
for name, v in [("Y", v_Y)] + [(f"T_{a+1}", v_T[a]) for a in range(3)]:
    assert np.allclose(v + v.conj().T, 0), f"{name} not anti-Hermitian"
    assert abs(np.trace(v)) < 1e-14, f"{name} not traceless"

# Compute the 16×16 matrices for each U(2) generator
M_Y = compute_LplusR_16x16(v_Y)
M_T = [compute_LplusR_16x16(v_T[a]) for a in range(3)]

# Verify Lie algebra: [T_a, T_b] = i * eps_{abc} * T_c (in anti-Hermitian convention)
# Actually [T_a, T_b] = f_{abc} T_c where f is structure constants
# For su(2): [T_1, T_2] = T_3 (in our -i*sigma/2 convention: [-i*s1/2, -i*s2/2] = -i*s3/2)
comm_12 = M_T[0] @ M_T[1] - M_T[1] @ M_T[0]
assert np.allclose(comm_12, M_T[2]), "Lie algebra check failed: [T_1, T_2] ≠ T_3"
print("[T_1, T_2] = T_3 verified ✓")

comm_YT = M_Y @ M_T[0] - M_T[0] @ M_Y
assert np.allclose(comm_YT, 0, atol=1e-12), "[Y, T_a] should be 0 (U(1) commutes with SU(2))"
print("[Y, T_a] = 0 verified ✓ (U(1) commutes with SU(2))")

# Now diagonalize M_Y and M_T[2] (Cartan elements) simultaneously
# Y eigenvalues → hypercharge
# T_3 eigenvalues → isospin z-component

Y_evals = np.linalg.eigvalsh(1j * M_Y)  # M_Y is anti-Hermitian, so i*M_Y is Hermitian
T3_evals = np.linalg.eigvalsh(1j * M_T[2])

print(f"\nY eigenvalues (i*M_Y): {sorted(np.round(Y_evals, 6))}")
print(f"T_3 eigenvalues (i*M_T3): {sorted(np.round(T3_evals, 6))}")

# Better: simultaneous diagonalization via joint eigenvectors
# Since [Y, T_3] = 0, they share a common eigenbasis
# Use the combined matrix Y + alpha*T_3 with irrational alpha to break degeneracies
alpha_break = np.sqrt(7)  # irrational number to break accidental degeneracies
H_combined = 1j * M_Y + alpha_break * 1j * M_T[2]
evals_combined, evecs_combined = np.linalg.eigh(H_combined)

# Extract Y and T_3 from each eigenvector
spinor_quantum_numbers = []
print(f"\n{'Slot':>5} {'Y':>8} {'T_3':>8} {'2j+1':>6}  Identification")
print("-" * 60)

for i in range(16):
    v = evecs_combined[:, i]
    Y_val = np.real(v.conj() @ (1j * M_Y) @ v)
    T3_val = np.real(v.conj() @ (1j * M_T[2]) @ v)

    # Round to nearest half-integer
    Y_r = round(2 * Y_val) / 2.0
    T3_r = round(2 * T3_val) / 2.0

    spinor_quantum_numbers.append((Y_r, T3_r))

# Sort by (Y, T_3)
sq_sorted = sorted(enumerate(spinor_quantum_numbers), key=lambda x: (x[1][0], x[1][1]))

# Group into SU(2) multiplets and identify
multiplets_spinor = []
y_groups = {}
for idx, (Y, T3) in sq_sorted:
    Y_key = round(Y * 2) / 2.0
    if Y_key not in y_groups:
        y_groups[Y_key] = []
    y_groups[Y_key].append((T3, idx))

print("\nSpinor Δ_8 decomposition under SU(2)×U(1):")
for Y_key in sorted(y_groups.keys()):
    states = sorted(y_groups[Y_key], key=lambda x: x[0])
    t3_vals = [s[0] for s in states]
    j = max(t3_vals)
    dim_j = int(2 * j + 1)
    n_multiplets = len(states) // dim_j

    for m in range(n_multiplets):
        multiplets_spinor.append((j, Y_key))

    indices = [s[1] for s in states]
    print(f"  Y = {Y_key:+5.1f}: T_3 = {t3_vals}, j = {j}, "
          f"count = {n_multiplets}, indices = {indices}")

print(f"\nSpinor multiplets: {sorted(multiplets_spinor, key=lambda x: (x[1], x[0]))}")
total_spinor_dim = sum(int(2*j+1) for j, _ in multiplets_spinor)
print(f"Total spinor dimension: {total_spinor_dim}")
assert total_spinor_dim == 16, f"Expected 16, got {total_spinor_dim}"


# =============================================================================
# SECTION 6: Physical Identification — Baptista eq 2.66
# =============================================================================

print("\n" + "=" * 78)
print("PHYSICAL IDENTIFICATION: SM Particle Content from Spinor Decomposition")
print("=" * 78)

# From Baptista eq 2.66, one generation of SM fermions:
#
# Block a (1 component):   ν_R           Y=0, SU(2) singlet
# Block c (3 components):  u_R^{r,g,b}   Y=?, SU(2) multiplet
# Block b (3 components):  (e_R, d_R^{r,g,b})  ...
# Block D (9 components):  mixed
#
# The COMBINED L+R action gives the SM quantum numbers.
# Let's check what Y and T_3 each slot actually carries.

print("\nPer-slot quantum numbers from simultaneous Y, T_3 diagonalization:")
print(f"{'Slot':>5} {'Block':>8} {'Y':>8} {'T_3':>8}")
print("-" * 40)

block_labels = ['a'] + ['c']*3 + ['b']*3 + ['D']*9
for i in range(16):
    v = evecs_combined[:, i]
    Y_val = np.real(v.conj() @ (1j * M_Y) @ v)
    T3_val = np.real(v.conj() @ (1j * M_T[2]) @ v)

    # Determine which block this eigenvector mainly belongs to
    block_weights = {
        'a': abs(v[0])**2,
        'c': np.sum(np.abs(v[1:4])**2),
        'b': np.sum(np.abs(v[4:7])**2),
        'D': np.sum(np.abs(v[7:16])**2),
    }
    dominant_block = max(block_weights, key=block_weights.get)

    print(f"{i:5d} {dominant_block:>8} {Y_val:8.3f} {T3_val:8.3f}")


# =============================================================================
# SECTION 7: B/F Assignment per (p,q) Sector
# =============================================================================

print("\n" + "=" * 78)
print("B/F ASSIGNMENT PER (p,q) SECTOR FOR LOG-SIGNED-41")
print("=" * 78)

# The CSDR B/F classification:
#
# BOSONIC modes (integer spin in 4D):
# - From metric fluctuations: transform under sym^2(cotangent) of SU(3)
#   → symmetric tensor representations
# - From gauge field A_μ: transform under adjoint of isometry group
#   → (1,1) = adjoint representation
# - From scalar (dilaton): (0,0) = singlet
#
# FERMIONIC modes (half-integer spin in 4D):
# - From spinor Ψ: transform under Δ_8 restricted to SU(3)
#   → determined by the spinor decomposition above
#
# The key insight from the CSDR framework:
# In the KK reduction of a GRAVITATIONAL theory on M^4 × K:
# - The Dirac operator D_K has eigenvalues λ_n
# - EACH eigenvalue generates both bosonic AND fermionic 4D modes
# - The bosonic/fermionic CHARACTER is determined by the 4D spin,
#   which comes from the representation of Spin(4) × H(K)
#
# For our spectral action computation (LOG-SIGNED-41):
# The spectral action Tr[f(D²/Λ²)] sums over ALL eigenvalues of D_K.
# The B/F sign comes from whether the 4D field is bosonic or fermionic.
#
# In the Connes spectral action framework:
# The FULL Dirac operator is D = D_4 ⊗ 1 + γ_5 ⊗ D_K
# Its square: D² = D_4² ⊗ 1 + 1 ⊗ D_K² (when D_4 and D_K anticommute via γ_5)
# The spectral action is Tr[f(D²/Λ²)] where the trace is over BOTH 4D and K.
#
# The 4D trace gives: Tr_4[f(D_4²/...)] which for each D_K eigenvalue λ_n
# contributes Seeley-DeWitt coefficients a_0, a_2, a_4...
# The 4D Dirac operator includes BOTH chiralities → both bosons and fermions
# contribute with FIXED signs determined by the spin-statistics theorem.
#
# THE KEY RESULT (from NCG / spectral action formalism):
# Each (p,q) sector contributes to Tr[f(D²)] with a weight that is:
#   w(p,q) = d_B(p,q) - d_F(p,q)
# where d_B and d_F count the number of bosonic and fermionic 4D DOF
# that arise from the (p,q) sector.
#
# For the M^4 × SU(3) reduction:
# The (p,q) sector of D_K has multiplicity dim(p,q)² (from L × R Peter-Weyl)
# Under (SU(3)_L) × (SU(2)_R × U(1)_R):
# - (p,q) ⊗ (q,p)|_{SU(2)×U(1)} = (p,q) ⊗ [branching of (q,p)]
#
# The CSDR branching of the RIGHT representation (q,p) under U(2)
# determines how many of the dim(q,p) = dim(p,q) right-action modes
# fall into each SM representation.
#
# For B/F assignment: in the full 12D theory, bosons come from D_K² eigenvalues
# through the metric/gauge sector, and fermions come through the spinor sector.
# The NET B-F difference per sector is:
#
# n_B(p,q) - n_F(p,q) = [bosonic DOF from (p,q)] - [fermionic DOF from (p,q)]
#
# From the 12D decomposition:
# - Bosonic: graviton (44 DOF in 12D) + 3-form (84 DOF) → 44 + 84 = 128 bosonic
# - Fermionic: gravitino (128 DOF in 12D) → 128 fermionic
# This is the D=12 N=1 SUGRA content: 128 = 128 (B = F if SUSY)
#
# BUT: our framework is NOT supersymmetric. The Jensen deformation breaks any
# putative SUSY. So B ≠ F in general.
#
# The PRACTICAL B/F assignment for LOG-SIGNED-41:
# We need the B-F weight AS A FUNCTION OF THE (p,q) SECTOR AND THE EIGENVALUE.
# This is determined by which 4D fields each KK mode generates.

# The Forgacs-Manton CSDR tells us:
# From the METRIC sector (bosonic):
#   - Graviton modes: transform as symmetric traceless rank-2 tensors of K
#   - Vector modes: transform as Killing vectors of K = isometry generators
#   - Scalar modes: transform as trace part + moduli
#
# From the SPINOR sector (fermionic):
#   - Dirac fermion modes: transform as spinor harmonics of K

# For a COMPACT group manifold K = SU(3):
# The Peter-Weyl expansion gives:
#   Metric modes: expand in (p,q) sectors weighted by symmetric tensor content
#   Spinor modes: expand in (p,q) sectors weighted by spinor content

# The ADJOINT decomposition tells us the GAUGE sector content:
print("\nADJOINT (1,1) branching under U(2) = SU(2)×U(1):")
for j, Y in sorted(branching_data[(1, 1)], key=lambda x: (x[1], x[0])):
    dim_j = int(2*j + 1)
    # In CSDR: these become 4D gauge bosons (from A_μ) and 4D scalars (from A_I)
    # Gauge bosons: the u(2) part → W^±, W^3, B (4 gauge bosons)
    # Scalars (Higgs): the C² part → Higgs doublet
    field_type = "BOSONIC (gauge)" if (j == 0 and Y == 0) or (j == 1 and Y == 0) else "BOSONIC (Higgs)"
    print(f"  (j={j}, Y={Y:+.0f}): dim={dim_j}  [{field_type}]")


# =============================================================================
# SECTION 8: Compute B/F Weight Per (p,q) Sector
# =============================================================================

print("\n" + "=" * 78)
print("B/F WEIGHT PER (p,q) SECTOR")
print("=" * 78)

# For the spectral action, the signed trace is:
#   V_log^signed = Σ_{p,q} w(p,q) * Σ_n d_n * ln(λ_n²)
# where w(p,q) is the B-F weight per sector.
#
# In a KK reduction on a group manifold, EACH eigenvalue of D_K generates
# both bosonic AND fermionic 4D fields. The net sign depends on the
# representation content:
#
# For the BOSONIC contribution (from metric + gauge fluctuations):
# The relevant representations that contribute to the KK tower are:
#   (a) Symmetric traceless tensors: S²(tangent) = various (p,q) sectors
#   (b) Vectors: tangent bundle = adjoint (1,1) → enters at level 1
#   (c) Scalars: (0,0) → enters at level 0
#
# For the FERMIONIC contribution (from spinor):
# The spinor Δ_8|_{SU(3)} has specific (p,q) decomposition
# Each spinor KK mode at eigenvalue λ_n gives 4D fermions

# CRITICAL INSIGHT: The B/F assignment per (p,q) sector comes from
# comparing the BOSONIC and FERMIONIC mode counts in each sector.
#
# Bosonic modes in sector (p,q): from metric harmonics
#   - Scalar harmonics: Y^{(p,q)}, dim = dim(p,q)²
#   - Vector harmonics: from grad(Y) + killing-type
#   - Tensor harmonics: from ∇∇Y + Ricci-type
#
# Fermionic modes in sector (p,q): from spinor harmonics
#   - Spinor harmonics: Ψ^{(p,q)}, dim = dim(p,q)² × (spinor multiplicity)
#
# The RELATIVE multiplicity between bosonic and fermionic modes in each
# sector is what determines the B/F weight.

# From our framework's established results:
# - Total bosonic DOF on fiber: 44 (graviton) per MEMORY
# - Total fermionic DOF on fiber: 16 (spinor Δ_8) per MEMORY
# - Trap 1: F/B = 16/44 = 4/11 (tau-independent, geometric)
#
# This means globally, the B/F ratio is 44:16.
# But the distribution across (p,q) sectors is NOT uniform.

# The spinor Δ_8 under SU(3) action decomposes into specific sectors.
# From the computation in branching_computation.py and Session 6-8 results:
# Δ_8|_{SU(3)} contains: (0,0) with mult, (1,0), (0,1), (1,1)
# These are the sectors that carry fermionic weight.

# For the metric/gauge sector, the relevant decompositions are:
# - Scalar harmonics: all (p,q) contribute (1 scalar per eigenvalue)
# - Vector harmonics: related to ∇·(scalar harmonics) → same sectors shifted
# - Tensor harmonics: sym^2(vector) content

# THE DEFINITIVE B/F ASSIGNMENT from the CSDR perspective:
#
# For M^4 × K with K = SU(3):
# The 12D metric g_MN decomposes as:
#   g_μν: 4D graviton (10 DOF) → gives KK tower of spin-2 fields
#   g_μI: 8 vectors (16 DOF) → gives KK tower of spin-1 fields
#   g_IJ: symmetric tensor on K (36 DOF) → gives KK tower of spin-0 fields
# Plus gauge conditions reduce these.
#
# The 12D Dirac spinor Ψ decomposes as:
#   Ψ_4 ⊗ Ψ_8: 4D spinor ⊗ internal spinor (4 × 16 = 64 DOF)
# Each internal spinor harmonic gives one 4D Dirac fermion.

# THE B-F WEIGHT:
# In each (p,q) sector, the number of bosonic minus fermionic 4D fields is:
#
# For sector (p,q) at eigenvalue λ_n:
#   n_B(p,q) = (metric sector modes) = 1 (scalar) + ...
#   n_F(p,q) = (spinor sector modes) × multiplicity in Δ_8
#
# The net contribution to the signed spectral sum is:
#   w(p,q) = n_B(p,q) - n_F(p,q)

# Let me compute the spinor content per (p,q) sector directly.
# The Δ_8|_{SU(3)} decomposition can be extracted from the L+R action.

# We already have the 16×16 matrices for the U(2) action.
# But what we actually need is the SU(3)×SU(3) Peter-Weyl decomposition
# of Δ_8, i.e., which (p,q) sectors of D_K carry spinor modes.

# From the Casimir computation:
# The Casimir of the L+R action on each block of Δ_8:
# Block a (dim 1): singlet (0,0) → C_2 = 0
# Block c (dim 3): fundamental under R → (0,1) under R, but L has -2v11 → need full analysis
# Block b (dim 3): fundamental under L → (1,0) under L
# Block D (dim 9): adjoint under L-R → (1,1) ⊕ (0,0) under adj

# Actually, the L×R decomposition is what Peter-Weyl gives.
# The KEY question for B/F assignment is simpler:
# In the Dirac spectrum, each eigenvalue λ of D_K has a definite (p,q) sector.
# The question is: does that eigenvalue contribute to BOSONIC or FERMIONIC
# modes in the 4D theory?
#
# The answer is BOTH — every eigenvalue of D_K² contributes to both
# the heat kernel coefficients of the bosonic AND fermionic 4D actions.
# The SIGN difference comes from the spin-statistics factor in the
# one-loop effective action:
#
# V_eff = (1/2) Σ_B ln det(D²_B) - (1/2) Σ_F ln det(D²_F)
#       = (1/2) Σ_n d_n [n_B - n_F](p,q) * ln(λ_n²)
#
# where [n_B - n_F](p,q) is the B-F index for sector (p,q).

# For a GRAVITATIONAL theory on M^4 × K:
# Each KK level n contributes:
#   Bosonic: graviton (helicity ±2) + vectors (helicity ±1) + scalars (helicity 0)
#   Fermionic: gravitino (helicity ±3/2) + spinors (helicity ±1/2)
#
# The count per level depends on the representation content at that level.
# For a group manifold K = SU(3):
#   Level (p,q): dim(p,q)² states
#   Of these:
#     - Metric fluctuations contribute dim(symmetric tensors in (p,q))
#     - Spinor fluctuations contribute dim(spinors in (p,q))

# However, for the DIRAC operator D_K specifically:
# D_K acts on sections of the spinor bundle S(K).
# Its eigenvalues are ALL fermionic modes (they ALL generate 4D spinors).
# The BOSONIC modes come from a DIFFERENT operator: the Laplacian Δ_K
# acting on scalars, vectors, and tensors.
#
# Therefore, for the signed spectral action of D_K:
# V_log^signed = (1/2) Σ_n d_n * sign(n) * ln(λ_n²)
# where sign(n) = +1 for bosonic ???
#
# NO. The spectral action Tr[f(D²/Λ²)] already includes BOTH bosonic
# and fermionic contributions because D = D_boson ⊕ D_fermion in the
# Connes framework. The full Dirac operator is:
# D = (0    D*)
#     (D    0 )
# which acts on the total Hilbert space H = H_+ ⊕ H_-.
# The grading γ distinguishes H_+ (particles) from H_- (antiparticles),
# not bosons from fermions.
#
# The B/F distinction in the spectral action comes from the SECOND
# quantization: the one-loop effective action is:
# Γ = (1/2) Tr_B[ln(D²)] - Tr_F[ln(D²)]
# where Tr_B sums over bosonic modes and Tr_F over fermionic modes.

# RESOLUTION: In the PHYSICAL signed sum, the sign per eigenvalue
# is determined by whether that eigenvalue belongs to a mode that
# produces a 4D boson or a 4D fermion.
#
# For D_K on SU(3):
# ALL eigenvalues of D_K produce 4D FERMIONS (Dirac spinors).
# The bosonic KK modes come from the LAPLACIAN Δ_K, not D_K.
#
# However, the spectral action Tr[f(D²)] CAN reproduce both
# bosonic and fermionic effective actions because:
# D² = Δ + (curvature terms)
# and the Seeley-DeWitt expansion of Tr[f(D²)] gives:
# a_0 = dim(spinor bundle) × Vol(K) → cosmological constant
# a_2 = (1/6) × R × dim(S) × Vol(K) → Einstein-Hilbert
# a_4 = spectral action gauge kinetic terms
#
# The signed version WITHIN the Dirac operator would be:
# Tr[γ * f(D²)] = supertrace
# But γ here is the grading, NOT the B/F grading.
#
# CONCLUSION for LOG-SIGNED-41:
# The B/F assignment per eigenvalue of D_K is determined by the
# PHYSICAL CONTENT of the corresponding 4D field.
#
# In the simplest KK framework:
# - D_K eigenvalue λ_n in sector (p,q) with multiplicity d_n = dim(p,q)²
# - The 4D field content from this mode:
#   * 4D Dirac fermion: ALWAYS present (from the spinor KK reduction)
#   * 4D scalars/vectors: from the metric KK reduction at the SAME λ²
#     (because D² = Δ + curvature, and the bosonic Laplacian has related eigenvalues)
#
# The net B-F per (p,q) sector is thus:
# w(p,q) = [# bosonic DOF from metric at this level] - [# fermionic DOF from spinor]
#         = [n_scalar + 2*n_vector + ... ] - [4 * d_spinor(p,q)]
#         (factor 4 from 4D Dirac spinor DOF)

# For concreteness, let me compute the SPIN CONTENT of each sector.

# The spinor bundle S(SU(3)) has fiber dimension 2^4 = 16.
# The Peter-Weyl expansion of L²(S(SU(3))) = ⊕_{(p,q)} V_{(p,q)} ⊗ V_{(p,q)}* ⊗ C^{16}
# But the spinor bundle is NOT the trivial bundle × C^{16}.
# The spinor bundle twists the representation content.
#
# The correct decomposition was computed in Session 6-8 and the Dirac script.
# The eigenvalues of D_K in sector (p,q) have multiplicity dim(p,q)²
# (from Peter-Weyl) when the spinor bundle is trivial, but the actual
# multiplicity is dim(p,q) × dim_spinor((p,q)) where dim_spinor is the
# dimension of the spinor-valued part.

# Let me take a different, cleaner approach to the B/F assignment.

print("\n--- APPROACH: CSDR Branching of Each Sector Under U(2) ---")
print("--- This determines SM quantum numbers per KK mode ---\n")

# For the LOG-SIGNED-41 resolution, what we ACTUALLY need is:
# For each (p,q) sector in the Dirac spectrum of D_K:
#   1. How many SM BOSONS does this sector produce? (integer-spin reps under SU(2))
#   2. How many SM FERMIONS does this sector produce? (half-integer-spin reps under SU(2))
#
# The right-action representation is (q,p).
# Under U(2) ⊂ SU(3)_R, (q,p) branches into SU(2)_j × U(1)_Y components.
# INTEGER j → these modes are BOSONIC in the 4D theory
# HALF-INTEGER j → these modes are FERMIONIC in the 4D theory
#
# Wait — this is the SM quantum number (isospin), not the spin.
# The 4D SPIN comes from the 4D Lorentz group, not the internal symmetry.
# Isospin j is a GAUGE quantum number, not a spacetime quantum number.
#
# The 4D spin is:
# - Spin 2: from metric g_μν → graviton modes
# - Spin 1: from metric g_μI → vector modes (KK photons)
# - Spin 0: from metric g_IJ → scalar modes (moduli, Higgs)
# - Spin 1/2: from spinor Ψ → Dirac fermion modes
# - Spin 3/2: from gravitino Ψ_μ → (if present)
#
# The 4D spin is FIXED by the type of higher-D field, not by the
# representation content of the KK mode.
#
# Therefore: the B/F assignment is:
# - ALL eigenvalues of D_K (the internal Dirac operator) generate
#   4D spin-1/2 fields → ALL FERMIONIC
# - The Laplacian eigenvalues generate 4D spin-0, spin-1, spin-2 → ALL BOSONIC
#
# But D² = Laplacian + curvature, so the eigenvalues of D² are related
# to (but not identical to) the Laplacian eigenvalues.
# The SIGNED spectral sum uses the DIFFERENCE between bosonic and fermionic
# contributions at each mass level.
#
# KEY REALIZATION: In the Connes spectral action framework, the B/F
# distinction is built into the FULL Dirac operator D which includes
# both the bosonic (scalar + gauge) and fermionic (spinor) sectors.
# The GRADING operator γ (chirality) provides the sign:
# Tr[f(D²)] = bosonic + fermionic (both positive)
# Tr[γ f(D²)] = bosonic - fermionic (signed)
#
# For our D_K on SU(3):
# The grading is γ_9 (the 8D chirality operator).
# The spectral pairing theorem ({γ_9, D_K} = 0) means:
# Tr[γ_9 f(D_K²)] = 0 identically (this was Variant B in S41)
#
# So the γ_9 grading CANNOT be the B/F grading.
# The B/F grading must come from a DIFFERENT source.

# What Variant E (the one with a minimum) uses is the BCS anomalous amplitude
# u_k v_k as the weight function. This is a DYNAMICAL weight, not a
# representation-theoretic one. The CSDR branching gives us the
# REPRESENTATION-THEORETIC content that determines the PHYSICAL B/F assignment.

# FINAL CLEAR STATEMENT of what the CSDR branching gives us:

print("=" * 78)
print("CSDR BRANCHING: REPRESENTATION-THEORETIC B/F CONTENT")
print("=" * 78)
print()
print("For each (p,q) sector, the RIGHT representation (q,p) under U(2) branches as:")
print("  (q,p)|_{SU(2)×U(1)} = ⊕_i (j_i)_{Y_i}")
print()
print("The number of bosonic vs fermionic 4D DOF from this sector is determined by")
print("the 4D SPIN (from the higher-D field type), NOT the isospin j_i.")
print()
print("However, the CSDR branching IS physically meaningful for:")
print("  1. Gauge coupling running (DDG power-law, S63)")
print("  2. SM quantum number assignment (which modes are doublets vs singlets)")
print("  3. Yukawa coupling structure (Higgs-fermion couplings)")
print()

# Compute the branching for the RIGHT-action representation (q,p)
# for all sectors up to p+q ≤ 6

print("\nCOMPLETE CSDR BRANCHING TABLE: (q,p)|_{SU(2)×U(1)}")
print("-" * 78)
print(f"{'(p,q)':>8} {'dim':>5} {'(q,p) branches':>60}")
print("-" * 78)

# Store for saving
csdr_table = {}

for p, q in sectors:
    dim = dim_su3(p, q)
    # The right-action is on (q,p), so branch (q,p)
    br_right = branching_su3_to_su2xu1(q, p)

    csdr_table[(p, q)] = {
        'dim': dim,
        'right_rep': (q, p),
        'branches': br_right,
        'n_integer_j': sum(1 for j, Y in br_right if j == int(j)),
        'n_half_j': sum(1 for j, Y in br_right if j != int(j)),
        'dim_integer_j': sum(int(2*j+1) for j, Y in br_right if j == int(j)),
        'dim_half_j': sum(int(2*j+1) for j, Y in br_right if j != int(j)),
    }

    br_str = " ⊕ ".join([
        f"({j})_{{{Y:+.0f}}}" if j == int(j) else f"({j:.1f})_{{{Y:+.0f}}}"
        for j, Y in sorted(br_right, key=lambda x: (x[1], x[0]))
    ])

    int_count = csdr_table[(p,q)]['n_integer_j']
    half_count = csdr_table[(p,q)]['n_half_j']
    int_dim = csdr_table[(p,q)]['dim_integer_j']
    half_dim = csdr_table[(p,q)]['dim_half_j']

    print(f"({p},{q}):  {br_str}")
    print(f"         dim={dim}, integer-j: {int_count} multiplets ({int_dim} states), "
          f"half-j: {half_count} multiplets ({half_dim} states)")

# =============================================================================
# SECTION 9: Summary Statistics and B/F Ratio per Sector
# =============================================================================

print("\n" + "=" * 78)
print("B/F CONTENT SUMMARY PER (p,q) SECTOR")
print("=" * 78)

print(f"\n{'(p,q)':>8} {'dim':>5} {'#singlet':>9} {'#doublet':>9} {'#triplet':>9} "
      f"{'#higher':>8} {'ratio(int/half)':>16}")
print("-" * 80)

# For SM content: singlets are j=0, doublets are j=1/2, triplets are j=1, etc.
# SM-relevant: SU(2) doublets (j=1/2) and singlets (j=0)

for p, q in sectors:
    if dim_su3(p, q) <= 0:
        continue
    d = csdr_table[(p, q)]
    br = d['branches']

    n_singlet = sum(1 for j, Y in br if j == 0)
    n_doublet = sum(1 for j, Y in br if j == 0.5)
    n_triplet = sum(1 for j, Y in br if j == 1)
    n_higher = sum(1 for j, Y in br if j > 1)

    dim_int = d['dim_integer_j']
    dim_half = d['dim_half_j']
    ratio = f"{dim_int}/{dim_half}" if dim_half > 0 else f"{dim_int}/0"

    print(f"({p},{q}):  {d['dim']:5d} {n_singlet:9d} {n_doublet:9d} {n_triplet:9d} "
          f"{n_higher:8d} {ratio:>16}")


# =============================================================================
# SECTION 10: Effective A Parameter for LOG-SIGNED-41
# =============================================================================

print("\n" + "=" * 78)
print("EFFECTIVE A PARAMETER FOR LOG-SIGNED-41")
print("=" * 78)

# The A parameter in Variant E of LOG-SIGNED-41 encodes the gap-edge F/B
# asymmetry. From the CSDR branching, we can now compute this.
#
# Variant E uses: V_E = (B-F)/(B+F) * V_unsigned
# where B = dim(integer-j states) and F = dim(half-integer-j states)
# in the RIGHT representation (q,p) branching.
#
# For the full spectral sum over all sectors:
# The asymmetry parameter A measures how much the B/F ratio VARIES
# between sectors.

# Compute per-sector asymmetry
print(f"\n{'(p,q)':>8} {'dim':>5} {'B_dim':>7} {'F_dim':>7} {'(B-F)/(B+F)':>14} {'weight':>10}")
print("-" * 65)

total_B_weighted = 0
total_F_weighted = 0
sector_asymmetries = []

for p, q in sectors:
    dim = dim_su3(p, q)
    if dim <= 0:
        continue
    d = csdr_table[(p, q)]

    B_dim = d['dim_integer_j']  # integer-j states
    F_dim = d['dim_half_j']     # half-integer-j states

    total = B_dim + F_dim
    asymmetry = (B_dim - F_dim) / total if total > 0 else 0
    weight = dim**2  # Peter-Weyl multiplicity

    total_B_weighted += B_dim * weight
    total_F_weighted += F_dim * weight

    sector_asymmetries.append({
        'pq': (p, q),
        'dim': dim,
        'B_dim': B_dim,
        'F_dim': F_dim,
        'asymmetry': asymmetry,
        'weight': weight,
    })

    print(f"({p},{q}):  {dim:5d} {B_dim:7d} {F_dim:7d} {asymmetry:14.6f} {weight:10d}")

# Weighted average asymmetry
A_effective = (total_B_weighted - total_F_weighted) / (total_B_weighted + total_F_weighted)
print(f"\nWeighted B/F asymmetry (A_eff) = {A_effective:.6f}")
print(f"Total weighted B = {total_B_weighted}, F = {total_F_weighted}")
print(f"B/F ratio = {total_B_weighted / total_F_weighted:.6f}")

# Check if A falls in the viable window [0.025, 0.295] for LOG-SIGNED-41
A_min_viable = 0.025  # (local)
A_max_viable = 0.295  # (local)
in_window = A_min_viable <= abs(A_effective) <= A_max_viable
print(f"\nLOG-SIGNED-41 viable window: A ∈ [{A_min_viable}, {A_max_viable}]")
print(f"|A_eff| = {abs(A_effective):.6f}")
print(f"In viable window: {in_window}")


# =============================================================================
# SECTION 11: Dynkin Index per Gauge Factor (for DDG Running)
# =============================================================================

print("\n" + "=" * 78)
print("DYNKIN INDICES PER GAUGE FACTOR (CSDR → DDG Power-Law Running)")
print("=" * 78)

# For each (p,q) sector, the KK modes contribute to the running of
# SU(3)_C, SU(2)_L, and U(1)_Y with Dynkin indices:
#
# SU(3)_C: T_3(p,q) = C_2(p,q) * dim(p,q) / 2*N  [from left-regular action]
#   where C_2(p,q) = (p² + q² + pq + 3p + 3q) / 3 (quadratic Casimir)
#
# SU(2)_L: from branching (q,p)|_{U(2)}
#   T_2(q,p) = Σ_i T_2(j_i)  where T_2(j) = j(j+1)(2j+1)/3
#
# U(1)_Y: from branching (q,p)|_{U(2)}
#   T_1(q,p) = Σ_i Y_i² * dim(j_i)  (sum of charge-squared times dimension)

def casimir_su3(p, q):
    """Quadratic Casimir C_2(p,q) of SU(3) irrep."""
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

def dynkin_su2(j):
    """Dynkin index T(j) of SU(2) irrep with spin j.
    T(j) = j(j+1)(2j+1)/3 for the fundamental normalization T(1/2)=1/2."""
    return j * (j + 1) * (2*j + 1) / 3.0

print(f"\n{'(p,q)':>8} {'dim':>5} {'C2_SU3':>8} {'T_SU3':>8} {'T_SU2':>8} {'T_U1':>8}")
print("-" * 55)

dynkin_data = {}

for p, q in sectors:
    dim = dim_su3(p, q)
    if dim <= 0:
        continue

    # SU(3)_C Dynkin index
    C2 = casimir_su3(p, q)
    # Dynkin index: T(R) = C_2(R) * dim(R) / (2 * dim(adj))
    # For SU(3): dim(adj) = 8, so T(R) = C_2(R) * dim(R) / 16
    # But standard convention: T(fund) = 1/2
    # C_2(fund) = 4/3, dim(fund) = 3, so T(fund) = 4/3 * 3 / 16 = 1/4 ???
    # No: T(R) = C_2(R) * dim(R) / (2 * N) for SU(N)
    # T(fund) = (N²-1)/(2N) * N / (2N) = (N²-1)/(4N)
    # For N=3: T(fund) = 8/12 = 2/3 ??? Still wrong.
    # Standard: T(R) defined by Tr(T^a T^b) = T(R) δ^{ab}
    # For fundamental of SU(N): T(fund) = 1/2
    # C_2(fund) = (N²-1)/(2N), dim(fund) = N
    # Relation: T(R) * dim(adj) = C_2(R) * dim(R)
    # → T(R) = C_2(R) * dim(R) / dim(adj)
    # For fund: T = [(N²-1)/(2N)] * N / (N²-1) = 1/2 ✓

    T_su3 = C2 * dim / 8.0  # dim(adj(SU(3))) = 8

    # SU(2)_L and U(1)_Y from branching of (q,p)
    br = branching_data.get((q, p))
    if br is None:
        br = branching_su3_to_su2xu1(q, p)
        branching_data[(q, p)] = br

    T_su2 = sum(dynkin_su2(j) for j, Y in br)
    T_u1 = sum(Y**2 * (2*j + 1) for j, Y in br)  # needs normalization

    # Store
    dynkin_data[(p, q)] = {
        'C2_su3': C2,
        'T_su3': T_su3,
        'T_su2': T_su2,
        'T_u1': T_u1,
    }

    print(f"({p},{q}):  {dim:5d} {C2:8.3f} {T_su3:8.3f} {T_su2:8.3f} {T_u1:8.1f}")


# =============================================================================
# SECTION 12: Cross-Check with Known Results
# =============================================================================

print("\n" + "=" * 78)
print("CROSS-CHECKS")
print("=" * 78)

# Check 1: Adjoint branching dimensions
br_adj = branching_data[(1, 1)]
u2_dim = sum(int(2*j+1) for j, Y in br_adj if (j == 0 and Y == 0) or (j == 1 and Y == 0))
coset_dim = sum(int(2*j+1) for j, Y in br_adj if not ((j == 0 and Y == 0) or (j == 1 and Y == 0)))
print(f"\nAdjoint (1,1): u(2) content dim = {u2_dim}, C² coset dim = {coset_dim}")
print(f"  Expected: 4 + 4 = 8.  Got: {u2_dim} + {coset_dim} = {u2_dim + coset_dim}")

# Check 2: Fundamental branching
br_fund = branching_data[(1, 0)]
print(f"\nFundamental (1,0): {br_fund}")
print(f"  Expected: (0)_{{-2}} ⊕ (1/2)_{{+1}}")

# Check 3: Total dimension conservation for all sectors
all_ok = True
for p, q in sectors:
    dim = dim_su3(p, q)
    br = branching_data[(p, q)]
    br_dim = sum(int(2*j+1) for j, Y in br)
    if br_dim != dim:
        print(f"  DIMENSION MISMATCH: ({p},{q}) dim={dim} but branching gives {br_dim}")
        all_ok = False
print(f"\nDimension conservation: {'ALL PASS' if all_ok else 'FAILURES DETECTED'}")

# Check 4: Conjugate symmetry: (p,q) branches should be conjugate of (q,p)
# Under charge conjugation: j stays same, Y → -Y
conj_ok = True
for p, q in sectors:
    if (q, p) not in branching_data:
        continue
    br_pq = set((j, Y) for j, Y in branching_data[(p, q)])
    br_qp_conj = set((j, -Y) for j, Y in branching_data[(q, p)])
    if br_pq != br_qp_conj:
        print(f"  CONJUGATION MISMATCH: ({p},{q}) vs ({q},{p})")
        conj_ok = False
print(f"Conjugation symmetry: {'ALL PASS' if conj_ok else 'FAILURES DETECTED'}")


# =============================================================================
# SECTION 13: Save Results
# =============================================================================

print("\n" + "=" * 78)
print("SAVING RESULTS")
print("=" * 78)

save_path = Path("computations") / "s63_csdr_branching.npz"

# Prepare arrays for saving
pq_list = [(p, q) for p, q in sectors if dim_su3(p, q) > 0]
n_sectors = len(pq_list)

p_arr = np.array([p for p, q in pq_list])
q_arr = np.array([q for p, q in pq_list])
dim_arr = np.array([dim_su3(p, q) for p, q in pq_list])

# B/F content per sector
B_dim_arr = np.array([csdr_table[(p,q)]['dim_integer_j'] for p, q in pq_list])
F_dim_arr = np.array([csdr_table[(p,q)]['dim_half_j'] for p, q in pq_list])
asymmetry_arr = np.array([(csdr_table[(p,q)]['dim_integer_j'] - csdr_table[(p,q)]['dim_half_j']) /
                           (csdr_table[(p,q)]['dim_integer_j'] + csdr_table[(p,q)]['dim_half_j'])
                           if csdr_table[(p,q)]['dim_integer_j'] + csdr_table[(p,q)]['dim_half_j'] > 0
                           else 0.0
                           for p, q in pq_list])

# Branching data as structured strings
branches_str = []
for p, q in pq_list:
    br = branching_data[(p, q)]
    br_s = ";".join([f"{j},{Y}" for j, Y in br])
    branches_str.append(br_s)

# Dynkin indices (where available)
T_su3_arr = np.array([dynkin_data.get((p,q), {}).get('T_su3', 0) for p, q in pq_list])
T_su2_arr = np.array([dynkin_data.get((p,q), {}).get('T_su2', 0) for p, q in pq_list])
T_u1_arr = np.array([dynkin_data.get((p,q), {}).get('T_u1', 0) for p, q in pq_list])

# Spinor quantum numbers
spinor_Y = np.array([Y for Y, T3 in spinor_quantum_numbers])
spinor_T3 = np.array([T3 for Y, T3 in spinor_quantum_numbers])

np.savez(save_path,
         # Sector data
         p=p_arr, q=q_arr, dim=dim_arr,
         # B/F content
         B_dim=B_dim_arr, F_dim=F_dim_arr, asymmetry=asymmetry_arr,
         A_effective=np.array([A_effective]),
         # Dynkin indices
         T_su3=T_su3_arr, T_su2=T_su2_arr, T_u1=T_u1_arr,
         # Spinor decomposition
         spinor_Y=spinor_Y, spinor_T3=spinor_T3,
         # Metadata
         max_pq_sum=np.array([max_pq_sum]),
         n_sectors=np.array([n_sectors]),
         branches=np.array(branches_str),
)

print(f"Saved to: {save_path}")
print(f"  {n_sectors} sectors with branching data")
print(f"  A_effective = {A_effective:.6f}")
print(f"  Spinor decomposition: 16 states with (Y, T_3) quantum numbers")


# =============================================================================
# FINAL VERDICT
# =============================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: CSDR-BRANCHING-63 — INFO")
print("=" * 78)

print(f"""
Complete CSDR branching table computed for {n_sectors} SU(3) sectors (p+q ≤ {max_pq_sum}).

KEY RESULTS:

1. ADJOINT (1,1) = 8 branches as:
   (0)_0 ⊕ (1)_0 ⊕ (0.5)_{{+3}} ⊕ (0.5)_{{-3}}
   = [U(1)_Y] ⊕ [SU(2)_L] ⊕ [C² Higgs] ⊕ [C² Higgs conjugate]
   u(2) content: 4 DOF (gauge), C² coset: 4 DOF (Higgs)

2. SPINOR Δ_8 = 16 decomposition under U(2):
   Quantum numbers computed via combined L+R action on Baptista spinor basis.

3. B/F ASYMMETRY per sector:
   Weighted A_effective = {A_effective:.6f}
   NOTE: This is the isospin-based B/F ratio (integer-j vs half-integer-j
   in the SU(2) branching), NOT the 4D spin-statistics B/F assignment.

4. DYNKIN INDICES for DDG running:
   Computed T_SU3, T_SU2, T_U1 per sector for CSDR-BRANCH-64 pre-registration.

5. LOG-SIGNED-41 RESOLUTION:
   The CSDR branching provides the SM quantum numbers (isospin, hypercharge)
   per KK mode, but does NOT directly determine the B/F sign in the
   one-loop effective action. The B/F sign is determined by the 4D spin
   (from the higher-D field type: metric → boson, spinor → fermion),
   which is INDEPENDENT of the internal (p,q) sector.

   The Variant E minimum mechanism requires a tau-DEPENDENT B/F modulation,
   which comes from the BCS gap dynamics, not from the static CSDR branching.
   The CSDR branching is a necessary INPUT for computing the A parameter,
   but A itself requires knowing the tau-dependent spectral flow.

   STATUS: LOG-SIGNED-41 remains CONDITIONAL. The A parameter cannot be
   extracted from CSDR alone — it requires the BCS gap function Δ(λ, τ).
""")
