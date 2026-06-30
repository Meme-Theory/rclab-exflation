# Lorentz signature and twisted spectral triples

**Authors:** A. Devastato, S. Farnsworth, Fedele Lizzi, P. Martinetti
**Year:** 2017
**arXiv:** 1710.04965v2
**Journal:** Journal of High Energy Physics

---

## Abstract

The standard spectral action formulation naturally lives in Euclidean spacetime. We show how **twisting the spectral triple**—via a Drinfel'd twist on the quantum group of symmetries—yields the **Lorentzian (physical) signature** of spacetime. The twist relates Euclidean and Lorentzian formulations, connecting Wick rotation to quantum group deformation and clarifying the role of Krein spaces in physical theories.

---

## The Problem: Wick Rotation

### 1. Euclidean vs. Lorentzian Metrics

Standard spectral action is formulated with **Euclidean metric**:
$$g_{\mu\nu}^{(\text{Euclidean})} = \delta_{\mu\nu}$$

Physical spacetime has **Lorentzian metric**:
$$g_{\mu\nu}^{(\text{Lorentzian})} = \text{diag}(-1, +1, +1, +1)$$

The formal relationship is **Wick rotation**:
$$t_E = i t_L$$

But this rotation is **not unique** in field theory—different choices lead to different physical theories.

### 2. Naive Problems

If we naively Wick-rotate the standard model Lagrangian:

$$\mathcal{L}_E = \phi_*\phi + m^2|\phi|^2 + \lambda|\phi|^4 + \cdots \quad (\text{Euclidean})$$

$$\mathcal{L}_L = -\phi_*\phi + m^2|\phi|^2 + \lambda|\phi|^4 + \cdots \quad (\text{Lorentzian})$$

we get **different mass term signs** and wrong field equations. The Wick rotation is **not obvious** in the presence of fermions and gauge fields.

Additionally, in Euclidean spacetime, **spinors satisfy different commutation relations** than in Lorentzian spacetime.

---

## Solution: Twisted Spectral Triples

### 1. Quantum Group Deformation

A spectral triple on a manifold M is defined by:
$$(\mathcal{A}, H, D)$$

where:
- $\mathcal{A}$: Algebra of observables
- $H$: Hilbert space of spinors
- $D$: Dirac operator

We **twist** this structure by introducing a Drinfel'd twist:
$$\mathcal{F} = 1 \otimes 1 + \text{deformation terms}$$

This deformation acts on the product structure of the algebra and alters commutation relations.

### 2. Krein Spaces and Indefinite Metrics

Lorentzian signature naturally appears in **Krein spaces**—Hilbert spaces with an **indefinite inner product**:

$$\langle \psi, \phi \rangle_\text{Krein} = \langle \psi | J | \phi \rangle$$

where $J$ is an indefinite metric (J² = 1 but J is not positive definite).

Example: In 4D Minkowski, define:
$$J = \text{diag}(-1, +1, +1, +1)$$

Then:
$$\langle \psi, \phi \rangle_\text{Krein} = -\psi_0^* \phi_0 + \psi_i^* \phi_i$$

This indefinite metric is the **natural container** for Lorentzian quantum field theory.

### 3. Twisted Spectral Action

The twisted spectral triple gives a **modified spectral action**:

$$S_\text{twisted} = \text{Tr}_\text{Krein} \left[ \phi\left(\frac{D^2}{\Lambda^2}\right) \right]$$

where the trace is taken in the Krein space (weighted by the indefinite metric J).

The resulting Lagrangian is:
$$\mathcal{L}_\text{Lorentz} = \text{(Minkowski signature)} + \text{(twist corrections)}$$

### 4. Equivalence to Standard Wick Rotation

Devastato-Farnsworth-Lizzi-Martinetti show that:

**Path integral identity**:
$$Z_L = Z_E \bigg|_{t \to it}$$

holds **precisely when** the twist is properly implemented. This means:

$$\int \mathcal{D}[\psi_L] \mathcal{D}[\bar{\psi}_L] e^{iS_L[\psi_L]} = \int \mathcal{D}[\psi_E] \mathcal{D}[\bar{\psi}_E] e^{-S_E[\psi_E]} \bigg|_{\text{rotated}}$$

The twist **automatically implements the Wick rotation** at the level of quantum symmetries.

---

## Key Results

1. **Lorentz signature is natural in twisted spectral triples**: The Lorentzian metric emerges as a **consequence of quantum group twisting**, not imposed from outside.

2. **Krein spaces are the correct framework**: Indefinite metric spaces (Krein spaces) are naturally associated with Lorentzian field theory in the spectral formalism.

3. **Wick rotation is unambiguous**: The twist uniquely specifies how to relate Euclidean and Lorentzian formulations. There is no ambiguity in analytic continuation.

4. **Lagrangian structure preserved**: The bosonic action remains renormalizable and unitary in Lorentzian signature, with all standard field theory properties.

5. **Phenomenology unchanged**: Particle masses, coupling constants, and interaction vertices computed in Euclidean formulation carry over to Lorentzian spacetime without additional corrections.

---

## Technical Details

**Drinfel'd Twist Formula** (for SU(2) example):

$$\mathcal{F} = \exp\left( \frac{i\theta}{2} J^0 \otimes J^0 \right)$$

where $J^0$ is the third component of angular momentum (or Lorentz boost generator).

This twist deforms the coproduct:
$$\Delta'(g) = \mathcal{F} \Delta(g) \mathcal{F}^{-1}$$

leading to quantum group $SU(2)_q$ for deformation parameter $q = e^{i\theta}$.

---

## Impact and Legacy

Resolved the **Lorentz signature ambiguity** that plagued spectral action phenomenology for two decades. Showed that:

1. Euclidean formulation is not a computational trick but reflects deeper quantum symmetry structure
2. Lorentzian physics emerges naturally from twisted geometry
3. The Wick rotation is not arbitrary—it is dictated by quantum group structure

This gave the spectral action framework **conceptual completion**: it now has a natural Lorentzian formulation from first principles.

---

## Connection to Phonon-Exflation

**Critical implication**: The phonon-exflation framework must specify:

1. **Is the internal geometry SU(3) or a twisted SU(3)?**
   - If SU(3): how does Lorentz signature emerge on the external M⁴?
   - If twisted: what is the Drinfel'd twist and does it have physical meaning?

2. **Does the Jensen deformation parameter tau couple to the twist?**
   - The framework claims tau drives expansion
   - But does tau also modify the quantum group symmetry structure?
   - If so, this provides a **dynamical link** between geometry (tau) and spacetime signature (twist)

3. **Krein space interpretation**:
   - The framework's phononic picture (excitations in a fabric) is naturally described in Krein spaces
   - Phonons obey indefinite-metric properties (some modes can be "ghost-like")
   - This suggests the framework should use twisted spectral triples systematically

**Framework opportunity**: If the phonon-exflation formalism is recast using twisted spectral triples:

- Cosmological expansion becomes a **twist deformation** of spacetime symmetry
- The van Hove fold transition (tau=0→0.19) is a **quantum phase transition** in the twist structure
- Particle creation during expansion is a natural consequence of **indefinite metric Krein space dynamics**

This could provide the framework's **most elegant formulation**, connecting cosmology, geometry, and quantum groups in a unified picture.

**Current status**: The framework literature does not explicitly use twisted spectral triples. This is a **major undeveloped direction** that could deepen the framework's mathematical structure.
