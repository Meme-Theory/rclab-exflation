# Tolerance Relations and Quantization

**Authors:** F. D'Andrea, G. Landi, Fedele Lizzi
**Year:** 2021
**arXiv:** 2112.09698v3

---

## Abstract

We study tolerance relations (reflexive, symmetric but NOT transitive equivalence relations) in geometry and show how quantization naturally produces operator systems from these "bad" quotient spaces. We relate this to NCG and positive operator valued measures (POVMs), providing a framework for imperfect measurements and approximate locality.

---

## Key Results

### 1. Tolerance Relations in Geometry
Classical geometry uses equivalence relations (transitive: if a~b and b~c then a~c).

**Tolerance relations**: Drop transitivity. Result: overlapping but non-transitive groupings.

Example: "approximately equal" in metric spaces with tolerance ε:
$$x \sim_\epsilon y \iff |x-y| < \epsilon$$

This is reflexive and symmetric BUT NOT transitive (can chain together to relate distant points).

### 2. Quantization via Tolerance
Associating a C*-algebra to tolerance relation:

$$C^*_\text{tol}(\sim) = \lim_{\text{tolerance}} C^*(R)$$

where R ranges over transitive relations contained in the tolerance.

**Result**: Operator system with:
- Non-associative product (intrinsic to quantization)
- Natural connection to POVMs
- Partial locality structure

### 3. POVM Interpretation
Positive operator valued measures generalize projectors:

$$\sum_i M_i = 1, \quad M_i \geq 0, \quad M_i M_j \neq 0 \text{ (overlapping)}$$

These are ideal for imperfect/fuzzy measurements where outcome projectors overlap.

Tolerance relations provide the **geometric origin** of POVM structure.

### 4. Non-associative Product
The operator system carries a natural (non-associative) product:

$$(A \star B) \star C \neq A \star (B \star C)$$

This is NOT an algebra (violates associativity) but an **operator system**.

**Physical meaning**: Composition of fuzzy measurements is non-associative—the order matters fundamentally.

---

## Key Findings

1. **Tolerance structures are geometric primitives**: More fundamental than classical equivalence relations.

2. **Quantization is natural**: The operator system arises without postulating quantum mechanics—just from handling approximate equivalences.

3. **POVMs emerge from geometry**: Fuzzy measurements have geometric origin in tolerance structure.

4. **Non-associativity fundamental**: At Planck scale, the order of operations becomes observable (path-dependent).

---

## Connection to Phonon-Exflation

**Framework interpretation**: The internal geometry might be described by tolerance relations rather than sharp equivalence. This would mean:

1. **Phonons are not sharply defined**: They have fuzzy identity (tolerance-relation-based)
2. **Measurements are inherently fuzzy**: Measuring a phonon number leaves overlap with neighboring phonon states (POVM)
3. **Order matters**: Sequentially measuring two phonon observables gives path-dependent results (non-associativity)
4. **Approximate locality**: The fabric has regions that are "approximately the same" but not transitively so

This provides a **geometric justification** for why phonons are collective excitations with undefined boundaries—they are defined by tolerance relations on the fabric.

**Framework opportunity**: If D_K eigenspaces are related by tolerance relations (rather than sharp eigenspace decomposition), this would explain why:
- Particle identity is quantum-blurred
- There is no absolute particle number (only approximate)
- The GGE relic can have overlapping occupation numbers in different channels

**Speculative but conceptually deep**: This might be the framework's **most elegant picture**—quantum mechanics emerges from tolerance geometry.
