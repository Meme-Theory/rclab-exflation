# Failure of the Goldstone Theorem for Vector Fields and Boundary-Mode Proliferation in Hyperbolic Lattices

**Author(s):** Daniel Sela, Nan Cheng, Kai Sun

**Year:** 2025

**arXiv:** 2511.16328

---

## Abstract

Demonstrates that the classical Goldstone theorem fails fundamentally for vector fields (phonons) in hyperbolic lattices where negative curvature reshapes collective excitations. Unlike Euclidean crystals where acoustic phonons remain gapless, hyperbolic lattices with coordination number z > 2d exhibit a finite bulk phonon gap. Goldstone modes belong to nonunitary irreps of the translation group, topologically disconnected from unitary bulk bands. Boundary modes fill the gap, exhibiting topological-like properties.

---

## Historical Context

The Goldstone theorem (1961-1962) is a pillar of condensed matter and particle physics. If a continuous symmetry breaks, gapless Goldstone modes exist. In crystals, translational symmetry breaking creates gapless acoustic phonons. Yet this assumes Euclidean space. As researchers explored condensed matter on curved spaces—motivated by topological phases and now experimentally realizable hyperbolic lattices—this assumption came into question. Sela, Cheng, and Sun show the theorem is not universal; Euclidean geometry is special.

---

## Key Arguments and Derivations

### Crystal Symmetries and Representations

In Euclidean crystals with translational symmetry, the order parameter (displacement field u(r) for phonons) transforms as a vector. In momentum space:

$$T_a u_k = e^{i k \cdot a} u_k$$

The translation group is isomorphic to R^d, and its irreps are one-dimensional: rho_k = e^{i k \cdot a}. All irreps are unitary.

A phonon mode with momentum k->0 transforms trivially. It is a valid bulk eigenstate and is gapless by Goldstone.

### Breakdown in Hyperbolic Lattices

Hyperbolic lattices are embedded in hyperbolic space with metric:

$$ds^2 = dho^2 + \sinh^2(ho) d	heta^2$$

The translation group is noncompact and nonabelian. When a vector field is displaced, it must be parallel-transported (rotated to align with local axes). Parallel transport depends on path taken:

$$	ext{Parallel transport} 
e 	ext{scalar displacement}$$

Phonon displacements are vector fields undergoing nontrivial parallel transport. The irreps of the translation group acting on vectors are nonunitary. This is the key distinction:

$$	ext{Nonunitary rep} 
ot\subset 	ext{Unitary bulk bands}$$

### Nonunitary Representations and Goldstone Failure

Bulk bands form unitary irreps. Goldstone modes belong to nonunitary irreps. Since nonunitary irreps are topologically disconnected from unitary irreps:

$$\mathcal{H}_G \perp \mathcal{H}_{	ext{bulk}}$$

Goldstone modes cannot couple to bulk states. They decouple, creating a bulk gap.

### Boundary Mode Proliferation

For a hyperbolic lattice with exponentially many sites near boundary:

$$N_{	ext{boundary}} \sim e^{L}$$

where L is system size. Boundary modes include genuine edge modes, topological modes, and pseudomodes coupling to nonunitary Goldstone structure.

---

## Key Results

1. Goldstone theorem fails in hyperbolic geometries for vector fields
2. Bulk phonon gap is generic when z > 2d
3. Boundary modes fill gap, carry spectral weight
4. Nonunitary representations cause breakdown
5. Phononic engineering opportunity: design bands via geometry
6. Vector vs. scalar: scalars may retain Goldstone modes; vectors do not

---

## Impact and Legacy

This work challenges a fundamental assumption: Goldstone's theorem is universal. It shows Euclidean geometry is special; exotic geometries reveal new physics. Recent work: hyperbolic phononic metamaterials, topological phonons, quantum simulation in Rydberg/photonic systems.

---

## Connection to Phonon-Exflation Framework

**Relevance: HIGH (Constraint on Phonon Dispersion)**

This paper directly constrains phonon behavior in Phonon-Exflation:

1. **SU(3) fiber curvature is non-Euclidean** -- The SU(3) fiber is a curved manifold. If phonons propagate on curved geometry, this analysis applies.

2. **Goldstone modes and SM phonons** -- In Phonon-Exflation, phonons should exhibit Goldstone modes. If SU(3) is sufficiently curved, Goldstone theorem fails and phonon gaps emerge. This is a new constraint.

3. **Boundary modes and localization** -- Session 42 investigates phononic crystal substrate. SU(3) boundary (compactness condition) generates boundary modes. If fiber geometry is hyperbolic-like, boundary modes are abundant.

4. **Coordination number and SU(3) rank** -- In lattice gauge theory on curved spaces, coordination depends on curvature and lattice type. For SU(3), effective coordination might determine whether phonon gaps appear.

5. **Non-Euclidean phonon engineering** -- Non-Euclidean lattices offer new degrees of freedom for phonon engineering. Phonon-Exflation's SU(3) fiber structure inherits these possibilities.

6. **Vector phonons vs. scalar phonons** -- Sela-Cheng-Sun distinguish vector (gapped in hyperbolic) from scalar (can be gapless). In SU(3), color charges couple to both vector (gluons) and scalar (Higgs). Goldstone failure for vectors could explain mass generation.

**Closest Session Connections:** Session 42 (phononic crystal, boundary modes), Session 35 (phonon spectrum, Goldstone modes)

**Critical Implication:** If z > 2d in SU(3) fiber, acoustic phonons are generically gapped. This contradicts naive expectations. Instead, phonon imprints appear in boundary states or coupled many-body modes (BCS pairs, S35).

---

## References

- D. Sela, N. Cheng, K. Sun, "Failure of the Goldstone Theorem for Vector Fields and Boundary-Mode Proliferation in Hyperbolic Lattices", arXiv:2511.16328 (2025).
- J. Goldstone, "Field theories with 'superconductor' solutions", Nuovo Cim. 19, 154 (1961).
- J. Goldstone, A. Salam, S. Weinberg, "Broken symmetries", Phys. Rev. 127, 965 (1962).
