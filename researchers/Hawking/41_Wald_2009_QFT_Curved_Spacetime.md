# The Formulation of Quantum Field Theory in Curved Spacetime

**Author(s):** Robert M. Wald
**Year:** 2009
**Journal:** Proceedings (Enrico Fermi Institute, University of Chicago)
**arXiv:** 0907.0416
**Relevance:** HIGH

---

## Abstract

The usual formulations of quantum field theory in Minkowski spacetime make crucial use of Poincare symmetry, positivity of total energy, and the existence of a unique, Poincare invariant vacuum state. These and other key features of quantum field theory do not generalize straightforwardly to curved spacetime. We discuss the conceptual obstacles to formulating quantum field theory in curved spacetime and how they can be overcome.

---

## Key Arguments and Derivations

### The Problem: QFT in Minkowski vs Curved Spacetime
Wald identifies the fundamental tension: QFT in Minkowski spacetime relies on structures that have no analogue in general curved spacetimes. He systematically examines the Wightman axioms and shows which ones generalize and which do not:

**Wightman axioms** (Streater & Wightman 1964):
1. States lie in a Hilbert space H carrying a unitary representation of the Poincare group
2. The 4-momentum spectrum is contained in the closed future light cone ("spectrum condition")
3. There exists a unique, Poincare invariant vacuum state
4. Quantum fields are operator-valued distributions on a dense domain D in H that is Poincare invariant and invariant under field action
5. Fields transform covariantly under Poincare transformations
6. At spacelike separations, fields commute or anticommute

**What goes wrong in curved spacetime**:
- No symmetries in general: cannot require Poincare invariance/covariance
- Unitarily inequivalent Hilbert space constructions exist (for noncompact Cauchy surfaces), none preferred
- No preferred vacuum state
- No analogue of the spectrum condition (total energy is not well-defined or positive)
- **Only axiom 6 (spacelike commutativity) generalizes straightforwardly**

### Specific Difficulties
**Total energy**: While the stress-energy tensor T_{ab} is conserved (nabla^a T_{ab} = 0) and one can define E = integral T_{ab} t^a n^b d Sigma, this quantity:
- Is conserved only if t^a is a Killing field (stationary spacetime)
- Can be negative in quantum field theory (dominant energy condition fails quantum mechanically)
- Even in simple examples (massless scalar on S^1 x R), E can be explicitly negative

**No preferred vacuum state**: For a free field, quasi-free Hadamard states provide a notion of "vacuum," but:
- This notion is highly non-unique
- Different choices give unitarily inequivalent Hilbert spaces (for noncompact Cauchy surfaces)
- "The quest for a preferred vacuum state in QFT in curved spacetime is much like the quest for a preferred coordinate system in classical general relativity"

### The Resolutions

**1. The Algebraic Approach**:
- Start with a *-algebra A of field observables, not a Hilbert space
- A state omega is a positive linear map omega: A -> C with omega(A* A) >= 0
- The GNS (Gelfand-Naimark-Segal) construction recovers a Hilbert space from any state: define inner product (A_1, A_2) = omega(A_1* A_2), factor by zero-norm vectors, complete
- This allows simultaneously considering all states from all Hilbert space constructions without choosing a representation
- Essential for studying phenomena in the early universe where no preferred state exists

**2. The Microlocal Spectrum Condition**:
- Replaces the spectrum condition (positivity of total energy) with a local condition on the wavefront set of correlation functions
- The wavefront set WF(D) of a distribution D characterizes its singularity structure in phase space
- In Minkowski spacetime, the spectrum condition is equivalent to requiring "locally positive frequency" singularity behavior of n-point functions
- This microlocal condition generalizes directly to curved spacetimes, even without a global notion of "positive frequency"
- States satisfying this condition are called Hadamard states

**3. Local and Covariant Fields**:
- Replaces Poincare covariance with the requirement that quantum fields are "locally and covariantly constructed out of the spacetime geometry"
- Formulated using causality-preserving isometric embeddings: if i: M -> O' subset M' is such an embedding, it must induce a natural isomorphism between A(M) and the subalgebra of A(M') associated with O'
- In Minkowski spacetime, this reduces to Poincare covariance (Poincare transformations are isometric embeddings of Minkowski into itself)
- Key insight: the theory must be formulated for ALL globally hyperbolic curved spacetimes to make sense of "nothing changes far from a local metric change"

**4. Operator Product Expansion (OPE) as Replacement for the Vacuum**:
- Hollands and Wald propose that the existence of an OPE replaces the Poincare-invariant vacuum axiom
- OPE: phi^{(i_1)}(x_1) ... phi^{(i_n)}(x_n) ~ sum_j C^{(i_1)...(i_n)}_{(j)}(x_1,...,x_n; y) phi^{(j)}(y)
- The distributional coefficients C of the identity element in OPE expansions play the role of vacuum expectation values
- Example: phi(x_1) phi(x_2) = H(x_1, x_2) 1 + phi^2(y) + ..., where H is a locally and covariantly constructed Hadamard distribution
- The OPE is proven for free fields in curved spacetime and holds order-by-order in perturbation theory for renormalizable interacting fields (Hollands 2007)

### Consequences and Results

**Spin-statistics and PCT in curved spacetime**: Hollands and Wald prove both theorems within the OPE framework. The PCT theorem relates processes in a given spacetime to processes involving charge-conjugate fields in a spacetime with opposite time orientation (e.g., particles in an expanding universe are related to antiparticles in a contracting universe).

**Renormalization in curved spacetime**:
- Composite fields (Wick powers, T_{ab}) and time-ordered products can be defined in a local and covariant manner
- Normal ordering CANNOT be used to define composite fields (it requires a preferred vacuum)
- Renormalization ambiguities include local curvature terms beyond the Minkowski counterparts
- Theories renormalizable in Minkowski spacetime remain renormalizable in curved spacetime
- Renormalization group flow defined via scaling: g_{ab} -> lambda^2 g_{ab}
- Conservation of the stress-energy tensor (nabla^a T_{ab} = 0) can be maintained in perturbation theory for arbitrary covariant interactions

### Summary of the Viewpoint
The background structure M of QFT in curved spacetime is the spacetime (M, g_{ab}) with time/space orientations and spin structure. For each M, one has an algebra A(M) of local field observables. All nontrivial information is contained in the OPE. States are positive linear maps satisfying the OPE relations and microlocal spectrum conditions. No preferred vacuum or particle interpretation is needed.

"The attempt to describe quantum field phenomena in curved spacetime has directly led to a viewpoint where symmetries and notions of 'vacuum' and 'particles' play no fundamental role."

---

## Key Results

1. **Only spacelike commutativity generalizes**: Of the six Wightman axioms, only the sixth (fields commute/anticommute at spacelike separation) extends straightforwardly to curved spacetime.

2. **Algebraic approach resolves Hilbert space ambiguity**: The *-algebra of observables + GNS construction allows simultaneous consideration of all unitarily inequivalent representations.

3. **Microlocal spectrum condition replaces positivity of energy**: The wavefront set condition on correlation functions provides a local replacement for the global spectrum condition.

4. **Local covariance replaces Poincare covariance**: The requirement that fields are locally and covariantly constructed from the metric generalizes Poincare invariance to arbitrary spacetimes.

5. **OPE replaces the vacuum axiom**: The operator product expansion, whose distributional coefficients of the identity play the role of vacuum expectation values, is the correct replacement for the Poincare-invariant vacuum.

6. **PCT theorem in curved spacetime**: Relates processes in a spacetime to processes involving charge-conjugate fields in the time-reversed spacetime.

7. **Normal ordering fails in curved spacetime**: Composite fields must be defined via the OPE and Hadamard regularization, not normal ordering.

8. **Renormalizability is preserved**: Theories renormalizable in flat spacetime remain so in curved spacetime, with additional local curvature ambiguities.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Free Klein-Gordon equation | $\partial^a \partial_a \phi - m^2 \phi = 0$ | Eq. 1 |
| Mode decomposition | $\phi_{\vec{k}} = L^{-3/2} \int e^{-i\vec{k}\cdot\vec{x}} \phi(t,\vec{x})\, d^3x$ | Eq. 2 |
| Hamiltonian (decoupled oscillators) | $H = \sum_{\vec{k}} \frac{1}{2}(|\dot{\phi}_{\vec{k}}|^2 + \omega_{\vec{k}}^2 |\phi_{\vec{k}}|^2)$ | Eq. 3 |
| Mode expansion | $\phi_{\vec{k}} = \frac{1}{\sqrt{2\omega_{\vec{k}}}} (a_{\vec{k}} + a^\dagger_{-\vec{k}})$ | Eq. 5 |
| Commutation relations | $[a_{\vec{k}}, a^\dagger_{\vec{k}'}] = \delta_{\vec{k}\vec{k}'} I$ | Eq. 6 |
| Heisenberg field operator | $\phi(t,\vec{x}) = L^{-3/2} \sum_{\vec{k}} \frac{1}{\sqrt{2\omega_{\vec{k}}}} (e^{i\vec{k}\cdot\vec{x} - i\omega_{\vec{k}} t} a_{\vec{k}} + \text{h.c.})$ | Eq. 7 |
| Smeared field (distribution) | $\phi(f) = \int f(t,\vec{x})\, \phi(t,\vec{x})\, d^4x$ | Eq. 8 |
| Total energy | $E = \int_\Sigma T_{ab}\, t^a n^b\, d\Sigma$ | Eq. 9 |
| State in algebraic approach | $\omega(A) = \langle \Psi | \pi(A) | \Psi \rangle$ | Eq. 10 |
| GNS inner product | $(A_1, A_2) = \omega(A_1^* A_2)$ | Eq. 11 |
| OPE (general) | $\phi^{(i_1)}(x_1) \cdots \phi^{(i_n)}(x_n) \sim \sum_{(j)} C^{(i_1)\ldots(i_n)}_{(j)}(x_1,\ldots,x_n; y)\, \phi^{(j)}(y)$ | Eq. 12 |
| OPE (free scalar) | $\phi(x_1)\phi(x_2) = H(x_1,x_2)\, \mathbf{1} + \phi^2(y) + \ldots$ | Eq. 13 |

## Relevance to Phonon-Exflation

Wald's formulation of QFT in curved spacetime is the mathematical foundation for the phonon-exflation framework's particle creation mechanism. The framework's transit through the KK fold occurs in a time-dependent geometry (the SU(3) fiber evolving with tau) where there is no preferred vacuum state or natural notion of "particles" --- precisely the situation Wald addresses. The algebraic approach (Section on the algebraic approach) is the correct framework for the framework's GGE relic state: after transit, the post-quench state is defined by its expectation values on the algebra of observables, not by reference to a particular Fock space. The fact that normal ordering fails in curved spacetime (and must be replaced by Hadamard regularization) is directly relevant to the framework's composite operator definitions in the spectral action. Wald's curved-spacetime PCT theorem, relating particles in an expanding universe to antiparticles in a contracting universe, connects to the framework's CPT hardwiring ([J, D_K(tau)] = 0, Session 17a) and the BDI topological classification. The OPE replacement for the vacuum axiom is particularly apt: in the framework, there is no stable vacuum at the fold --- the "vacuum" is the dynamical GGE state, fully specified by its OPE coefficients and Richardson-Gaudin conserved quantities.
