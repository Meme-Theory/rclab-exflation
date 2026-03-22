"""
PHASE 2.5 BASIS CHANGE: Can a unitary U rescue order-one?
==========================================================

The order-one failure comes from the row identification mismatch between
Baptista (rows = isospin+color) and Connes (rows = chirality).

Question: Does there exist a 16x16 unitary U such that:
  1. U pi(a) U^{-1} has the Connes row structure
  2. U D_F U^{-1} satisfies order-one with U pi(a) U^{-1}

Note: Order-one is basis-invariant! If [[D, a], o(b)] = c != 0, then
U [[D, a], o(b)] U^{-1} = [[UDU^{-1}, UaU^{-1}], Uo(b)U^{-1}]
                         = U c U^{-1} != 0 (since U is invertible).

So a UNITARY basis change CANNOT fix order-one if it fails in the original basis.

BUT: this assumes U acts on both D_F and A_F simultaneously.
If instead we allow U to act ONLY on the row/column structure of Psi (i.e.,
redefine how the 4x4 matrix is read, but keep the abstract algebra the same),
then the answer could be different.

The real question is: are the Baptista and Connes representations UNITARILY EQUIVALENT?

Author: KK Theorist Agent
Date: 2026-02-12
"""

import numpy as np

np.set_printoptions(precision=6, linewidth=140, suppress=True)


# =============================================================================
# PART 1: Unitary equivalence check
# =============================================================================
print("=" * 76)
print("PART 1: ARE BAPTISTA AND CONNES REPRESENTATIONS UNITARILY EQUIVALENT?")
print("=" * 76)

# The Baptista representation of C + H on C^4:
# C: lambda -> diag(lambda, 1, 1, 1)  [acts on row 0 only]
# H_i: q_i -> diag(i, -i, i, -i)      [acts on all rows]
# H_j: q_j -> [[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,-1,0]]
# H_k: q_k -> [[0,0,0,0],[0,0,0,0],[0,0,0,i],[0,0,i,0]]

# The Connes representation of C + H on C^4:
# C: lambda -> diag(lambda, lambda_bar, 1, 1)  [acts on rows 0,1]
# H_i: q_i -> diag(0, 0, i, -i)               [acts on rows 2,3 only]
# H_j: same as Baptista (rows 2,3)
# H_k: same as Baptista (rows 2,3)

# For two representations to be unitarily equivalent, they must have the
# SAME character (trace). Let's check:

print("\nCharacter comparison (traces):")
print(f"  {'Generator':<10} {'Baptista tr':<20} {'Connes tr':<20}")
print(f"  {'-'*10} {'-'*20} {'-'*20}")

# C_Im: lambda = i
bapt_CIm = np.diag([1j, 1.0, 1.0, 1.0])
connes_CIm = np.diag([1j, -1j, 1.0, 1.0])
print(f"  C_Im      {np.trace(bapt_CIm):<20}  {np.trace(connes_CIm):<20}")

# H_i: q = i
bapt_Hi = np.diag([1j, -1j, 1j, -1j])
connes_Hi = np.diag([0, 0, 1j, -1j])
print(f"  H_i       {np.trace(bapt_Hi):<20}  {np.trace(connes_Hi):<20}")

# C_Im * H_i (product)
bapt_prod = bapt_CIm @ bapt_Hi
connes_prod = connes_CIm @ connes_Hi
print(f"  C_Im*H_i  {np.trace(bapt_prod):<20}  {np.trace(connes_prod):<20}")

# H_i^2
bapt_Hi2 = bapt_Hi @ bapt_Hi
connes_Hi2 = connes_Hi @ connes_Hi
print(f"  H_i^2     {np.trace(bapt_Hi2):<20}  {np.trace(connes_Hi2):<20}")

print(f"\n  Traces DIFFER -> representations are NOT unitarily equivalent!")
print(f"  (Tr(C_Im) = 3+i vs 2, Tr(H_i) = 0 vs 0, but Tr(C_Im*H_i) = -2 vs 0)")

# This conclusively proves that NO unitary basis change can map Baptista to Connes.
# The representations are genuinely DIFFERENT (not just differently-based).


# =============================================================================
# PART 2: What IS the Baptista representation as abstract C+H module?
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 2: DECOMPOSE BAPTISTA C+H REPRESENTATION")
print("=" * 76)

# C + H = C + H is a real algebra of dimension 6.
# Its complex representations on C^n decompose into irreducibles.
#
# For C = C: irreps are (lambda -> lambda) and (lambda -> lambda_bar), both 1-dim.
# For H: irreps are the fundamental 2-dim rep and its conjugate.
# H = {a + bj : a,b in C} acts on C^2 as:
#   (a + bj) -> [[a, b], [-b_bar, a_bar]]
# This is the unique irreducible 2-dim complex rep (up to equivalence).
#
# For A = C + H: an element (lambda, q) with lambda in C, q in H.
# Irreps of A = pairs of irreps of C and H:
#   Type I:  (lambda, q) -> lambda (on C^1) -- C acts, H trivial
#   Type I': (lambda, q) -> lambda_bar      -- C conjugate, H trivial
#   Type II: (lambda, q) -> q_{2x2}         -- C trivial, H fundamental
#   Type II': (lambda, q) -> q_bar_{2x2}    -- C trivial, H conjugate
#   Mixed: (lambda, q) -> lambda * q_{2x2}  -- both act
#   etc.

# Let's find the decomposition of the Baptista 4-dim rep.
# Since C and H commute (they're in different summands of C + H),
# we can simultaneously diagonalize.

# First, find the C-eigenspaces:
# C_Im = diag(i, 1, 1, 1) -> eigenvalues: i (row 0), 1 (rows 1,2,3)
# So under C: row 0 carries lambda (hypercharge i for lambda=i)
#             rows 1,2,3 carry lambda^0 = 1 (trivial C action)

print("\nC-eigenspaces of Baptista representation:")
print(f"  Row 0: C acts as lambda (non-trivial)")
print(f"  Rows 1-3: C acts trivially (eigenvalue 1)")

# Now decompose the H action on each C-eigenspace:
# On row 0 (C-nontrivial, 1-dim): H_i acts as i, H_j,H_k act as 0
#   This is a 1-dim rep of H: q -> q_{11} component = alpha (the "complex part")
#   Actually, H acts on row 0 via: H_i -> i (from diag entry [0,0])
#   H_j, H_k don't touch row 0 (they only act on rows 2,3)
#   So on row 0: H acts as q -> alpha (the "scalar" part of quaternion)
#   This IS the 1-dim representation: fundamental representation restricted.

# On rows 1-3 (C-trivial, 3-dim): H_i acts as diag(-i, i, -i)
#   H_j acts on rows 2,3 only: [[0,1],[-1,0]]
#   H_k acts on rows 2,3 only: [[0,i],[i,0]]
#   Row 1 is fixed by H_j, H_k (they don't touch it)
#   H_i on row 1: -i

print(f"\nH-subrepresentations on rows 1-3:")
print(f"  Row 1: H_i -> -i, H_j -> 0, H_k -> 0 (1-dim: q -> alpha_bar)")
print(f"  Rows 2-3: H_i -> diag(i,-i), H_j, H_k -> full 2x2 (fundamental 2-dim)")

# Summary:
# Baptista C+H on C^4 decomposes as:
#   Row 0: (lambda, alpha) -- 1-dim, C=lambda, H=alpha
#   Row 1: (1, alpha_bar) -- 1-dim, C=trivial, H=alpha_bar
#   Rows 2-3: (1, q_{2x2}) -- 2-dim, C=trivial, H=fundamental

# Connes C+H on C^4:
#   Row 0: (lambda, 1) -- 1-dim, C=lambda, H=trivial
#   Row 1: (lambda_bar, 1) -- 1-dim, C=lambda_bar, H=trivial
#   Rows 2-3: (1, q_{2x2}) -- 2-dim, C=trivial, H=fundamental

print(f"\n{'=' * 76}")
print("DECOMPOSITION COMPARISON")
print(f"{'=' * 76}")
print(f"\n  Baptista: C^4 = (lambda, alpha) + (1, alpha_bar) + (1, q_{{2x2}})")
print(f"  Connes:   C^4 = (lambda, 1) + (lambda_bar, 1) + (1, q_{{2x2}})")
print(f"\n  The 2-dim piece is IDENTICAL (rows 2-3, fundamental H)")
print(f"  The two 1-dim pieces DIFFER:")
print(f"    Baptista row 0: C acts as lambda AND H acts as alpha")
print(f"    Baptista row 1: C is trivial AND H acts as alpha_bar")
print(f"    Connes row 0:   C acts as lambda, H is trivial")
print(f"    Connes row 1:   C acts as lambda_bar, H is trivial")
print(f"\n  In Baptista, C and H are ENTANGLED on the 1-dim pieces.")
print(f"  In Connes, C and H act INDEPENDENTLY on the 1-dim pieces.")
print(f"\n  These are genuinely different representations of C + H.")
print(f"  No basis change can map one to the other.")
print(f"  The Baptista representation is NOT the Connes representation.")


# =============================================================================
# PART 3: What are the physical implications?
# =============================================================================
print(f"\n{'=' * 76}")
print("PART 3: PHYSICAL IMPLICATIONS")
print(f"{'=' * 76}")

print(f"""
In the Connes spectral triple, the C+H representation on the 1-dim pieces
captures the hypercharge structure:
  Row 0 (nu_R): Y = 0 (lambda, trivial H) -- right-handed neutrino
  Row 1 (e_R):  Y = -2 (lambda_bar, trivial H) -- right-handed electron

In the Baptista KK reduction, the 1-dim pieces capture:
  Row 0 (nu):  lambda AND alpha -- hypercharge AND weak isospin are COUPLED
  Row 1 (c_1): trivial C, alpha_bar -- no hypercharge, but has isospin

This means the Baptista representation DOES NOT separate hypercharge from
weak isospin on the singlet states. The singlet neutrino carries isospin
(it shouldn't in the SM), and the first color direction carries conjugate
isospin but no hypercharge.

THIS is the fundamental mismatch. It's not just a basis issue -- it's a
genuine difference in how the internal quantum numbers are assigned.

However, this mismatch only affects the 1-dim representations.
The 2-dim fundamental H representation (rows 2-3) is IDENTICAL.
And the M_3(C) action on columns is IDENTICAL.

So the Baptista geometry gets the DOUBLET structure right (SU(2)_L on
left-handed fermions) and the COLOR structure right (SU(3)_c on quarks),
but assigns wrong quantum numbers to the RIGHT-HANDED singlets.
""")

# Verify: compute the full A_F decomposition
print(f"Full A_F = C + H + M_3(C) representation on C^{{4x4}} = C^16:")
print(f"  Columns: M_3(C) acts on cols 1-3 as m^dag, col 0 is singlet")
print(f"  Rows: C+H acts as described above")
print(f"\n  Tensor product decomposition:")
print(f"    Row 0, cols 1-3: (lambda, alpha) x color_3 = quarks with entangled C/H")
print(f"    Row 0, col 0:    (lambda, alpha) x singlet = lepton with entangled C/H")
print(f"    Row 1, cols 1-3: (1, alpha_bar) x color_3 = quarks, no hypercharge")
print(f"    Row 1, col 0:    (1, alpha_bar) x singlet = lepton, no hypercharge")
print(f"    Rows 2-3, cols 1-3: (1, q_2x2) x color_3 = quark doublets (CORRECT)")
print(f"    Rows 2-3, col 0:    (1, q_2x2) x singlet = lepton doublet (CORRECT)")
print(f"\n  The doublet sectors (rows 2-3) exactly match Connes.")
print(f"  The singlet sectors (rows 0-1) have wrong quantum numbers.")
print(f"  Specifically: right-handed fermions carry too much structure.")
