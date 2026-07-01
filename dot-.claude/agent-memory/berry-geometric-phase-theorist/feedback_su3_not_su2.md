---
name: SU(3) not SU(2)
description: Framework is built on SU(3) fiber, not SU(2). All decompositions and representation theory must use SU(3) and its automorphisms.
type: feedback
---

Do NOT default to SU(2) decompositions, binary/two-level thinking, or qubit language when analyzing the framework.

**Why:** The fiber manifold is SU(3), 8-dimensional, with Lie algebra su(3) = u(1) + su(2) + C^2 (1+3+4). The Dirac spectrum has ~1000 eigenvalues in 10 Peter-Weyl sectors, not a two-level system. The moduli space is 36-dimensional Sym^2(R^8), not a Bloch sphere. The residual symmetry at the fold is the adjoint U(2) action on su(3), not SU(2) acting on spin-1/2. Writing "SU(2) fundamental" when you mean "C^2 coset of SU(3)/U(2)" is wrong.

**How to apply:**
- When decomposing representations, use the U(2) action on Sym^2(su(3)), not abstract SU(2).
- When discussing level crossings, use multi-level LZ (992 eigenvalues, block-diagonal sectors), not two-level.
- When discussing Berry phase, specify the mechanism for SU(3) (Kosmann anti-Hermiticity, J-symmetry), not generic two-level geometry.
- The Berry-Tabor mechanism on this system is Schur orthogonality (block-diagonality), not classical action-angle variables.
- Paper 06 (superadiabatic LZ) generalizes from 2-level to multi-level only qualitatively -- state the caveat explicitly.
- Paper 14's Omega^2 = 4det(g) is a 2-band identity; on SU(3) it constrains 2-band projections, not the full QGT.
