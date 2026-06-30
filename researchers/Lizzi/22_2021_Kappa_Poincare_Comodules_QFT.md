# κ-Poincaré-comodules, Braided Tensor Products and Noncommutative Quantum Field Theory

**Authors:** Fedele Lizzi, F. Mercati
**Year:** 2021
**arXiv:** 2101.09683v1

---

## Abstract

We construct multiparticle field theory on κ-Minkowski spacetime respecting κ-Poincaré quantum group symmetry. The obstacle—multilocal functions respecting deformed symmetries—is solved using **braided tensor products**. κ-Poincaré-invariant N-point functions are commutative (abelian algebra), enabling consistent quantization. We show 2-point Wightman and Pauli-Jordan functions are identical to undeformed ones, while free scalar field can be constructed consistently.

---

## Key Arguments

### 1. Multiparticle Problem
Standard QFT: Two-point functions defined on $\mathcal{O}(x_1) \times \mathcal{O}(x_2)$ at distinct spacetime points. In κ-Minkowski, defining $\mathcal{O}(x_1) \otimes \mathcal{O}(x_2)$ requires care: tensor product must respect κ-Poincaré coaction.

### 2. Braided Tensor Products
Solution: Use **braided tensor products** $\otimes_B$ where braiding operation relates factors:

$$(A \otimes_B B) \cdot (C \otimes_B D) = (A \cdot_R C) \otimes_B (B \cdot_R D)$$

with $\cdot_R$ denoting right-action of κ-Poincaré group.

### 3. Abelian Subspace
**Crucial result**: κ-Poincaré-invariant N-point functions lie in an **abelian subalgebra**—they form commutative observables. This ensures:
- Consistency with locality (order-independence of measurements)
- Vanishing commutator: $[W(x_1), W(x_2)] = 0$ for κ-Poincaré invariants
- Proper Fock space structure

### 4. Wightman and Pauli-Jordan Functions
Remarkably, the 2-point correlation functions are **identical to undeformed QFT**:

$$\langle \Omega | \phi(x_1) \phi(x_2) | \Omega \rangle = \int \frac{d^4 p}{(2\pi)^4} e^{ip(x_1-x_2)} \Theta(p_0) \delta(p^2-m^2)$$

despite the entire κ-deformation. The deformation is **hidden in higher N-point functions**.

### 5. Free Scalar Field Construction
Full κ-Poincaré-invariant free scalar field theory can be constructed with:
- Ladder operator representations
- Fock space with standard commutation relations
- Propagators matching standard QFT at 2-point level

Open problems: Interactions and perturbation theory.

---

## Key Results

1. **Braided tensor products solve consistency**: Multiparticle theory exists in κ-framework with proper symmetry coaction.

2. **2-point functions undeformed**: Paradoxically, Wightman function unchanged despite κ-deformation.

3. **Higher correlations deformed**: 3-point and higher N-point functions carry κ-dependence.

4. **Fock space consistent**: Free field Fock space has canonical structure despite noncommutativity.

5. **Interactions still open**: How to construct κ-invariant interaction vertices and compute scattering amplitudes remains unsolved.

---

## Connection to Phonon-Exflation

**Critical application**: The framework's GGE relic quasiparticles must satisfy κ-Poincaré-invariant QFT (if internal geometry is κ-deformed). This paper shows:

1. **Multiparticle states possible**: 59.8 quasiparticle pairs can coexist with κ-deformed symmetries.

2. **Fock space structure**: Creation/annihilation operators can be consistently defined.

3. **Interaction problem**: How phonons interact (coupling constants, scattering rates) requires extending this formalism to κ-invariant perturbation theory.

**Framework implication**: The framework must either:
- Specify what κ-parameter value characterizes the internal geometry, or
- Work in undeformed (κ=0) limit and explain why quantum gravity effects are negligible

The paper suggests κ-deformation provides **fundamental mechanism for quantum gravity effects** without explicit Planck-scale suppression.
