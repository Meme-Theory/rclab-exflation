# The Structure of Non-Polynomial Closed String Field Theory

**Authors:** Michio Kaku, James Lykken
**Year:** 1990
**Journal:** Nuclear Physics B, Vol. 341, pp. 249–279

---

## Abstract

We develop a consistent formulation of closed string field theory including the metric tensor in the quantum field. Unlike open string field theory, which can be cast in polynomial form (cubic), closed string field theory contains the graviton as a dynamical field, and consistency requires allowing arbitrary polynomial interactions. We analyze the structure of anomalies in closed string field theory, establish the necessary form of counterterms, and show how the nonpolynomial structure emerges from consistency conditions. The theory is finite to all orders and unitary; the nonpolynomial terms encode the mixing between different sectors of the string spectrum and are essential for preserving gauge invariance and modular invariance on the worldsheet.

---

## Historical Context

The development of closed string field theory lagged behind open string field theory because of a fundamental difficulty: closed strings couple to gravity. The graviton (massless excitation of the closed string) must be included as a dynamical field in the action, leading to the question: How does gravity emerge from string field theory?

Moreover, closed strings have a key feature: they are oriented loops, not open lines. This means:

1. The spectrum includes both the graviton $h_{\mu\nu}$ and the dilaton $\Phi$ (both massless, metric-like).
2. Tree-level amplitudes automatically include gravitational interactions.
3. The vertex structure is fundamentally different from open strings (no "endpoints").

Kaku and Lykken's 1990 paper addressed these challenges. They showed that closed string field theory necessarily contains:

- **Quadratic terms**: Standard kinetic terms for the graviton and other fields.
- **Cubic vertices**: Graviton-to-graviton and graviton-to-matter interactions.
- **Quartic and higher**: Higher-point vertices mixing graviton, dilaton, and matter fields.

The reason for this nonpolynomial structure: **Consistency of the gravitational sector** forces higher-derivative and higher-point interactions to preserve the equivalence principle and diffeomorphism invariance.

---

## Key Arguments and Derivations

### The Closed String Spectrum

The closed string has independent left-moving and right-moving oscillators. The mass formula is:

$$M^2 = \frac{2}{\alpha'} (N_L + N_R - 2)$$

where $N_L = \sum_{n=1}^\infty n a_n^{i \dagger} a_n^i$ and $N_R = \sum_{n=1}^\infty n \tilde{a}_n^{i \dagger} \tilde{a}_n^i$. The constraint $N_L = N_R$ (level matching) ensures closed string consistency.

The massless spectrum ($M=0$) includes:

- **Graviton** $h_{\mu\nu}$ (symmetric): $a_1^{i \dagger} \tilde{a}_1^{j \dagger} |0\rangle$ with $(i,j)$ symmetric.
- **Dilaton** $\Phi$ (singlet): $(1/\sqrt{d-2}) a_1^{i \dagger} \tilde{a}_1^{i \dagger} |0\rangle$ (trace part).
- **Antisymmetric tensor** $B_{\mu\nu}$ (for superstrings, this couples to D-brane worldvolumes).

### Closure of the Graviton Sector

A fundamental consistency requirement: The graviton must decouple from/mix appropriately with the dilaton and other massless fields. This is encoded in the so-called "no-ghost theorem" for closed strings:

$$\langle \text{any state} | \text{any state} \rangle \geq 0$$

This requires the graviton to satisfy transversality and tracelessness:

$$\partial^\mu h_{\mu\nu} = 0, \quad h_\mu^\mu = 0$$

In the language of string field theory, these are **constraints** that must be imposed on the field Lagrangian to ensure unitarity. These constraints enforce gauge invariance.

### Nonpolynomial Structure from Consistency

The action for closed string field theory must have the form:

$$S = S_0 + S_{\text{int}}$$

where:

$$S_0 = \int d^d x \, \frac{1}{2\kappa^2} \left[ R - \frac{1}{2} (\partial \Phi)^2 - \frac{1}{12} H_{\mu\nu\lambda}^2 \right]$$

is the Einstein-Hilbert action (plus dilaton and antisymmetric tensor kinetic terms).

The interaction Lagrangian must include:

$$S_{\text{int}} = \int d^d x \, \left[ h \cdot h \cdot h + h \cdot h \cdot h \cdot h + h \cdot \Phi \cdot \Phi + \ldots \right]$$

where $h \cdot h$ denotes a vertex involving three graviton fields, etc. The precise form of each vertex is determined by:

1. **Dimensional analysis**: The coefficient of each term must have the correct dimension in $[M]^{d-4}$.
2. **Gauge invariance**: Diffeomorphisms must act consistently.
3. **Power counting**: To maintain finiteness, high-order interactions must be present with specific coefficients.

For the graviton, the cubic vertex is:

$$V_3^{hhh} = \frac{1}{\kappa} \int d^d x \, h^{\mu\nu} \partial_\mu h_{\rho\sigma} \partial^\rho h^\sigma_\nu + \text{permutations}$$

where $\kappa^2 = 16\pi G$ is the gravitational coupling. This is the familiar three-graviton vertex from Einstein gravity.

The quartic vertex appears:

$$V_4^{hhhh} \sim \frac{1}{\kappa^2} \int d^d x \, h \cdot h \cdot h \cdot h$$

with a coefficient fixed by consistency (it arises from closing two cubic vertices on internal momentum).

### Anomalies in Closed Strings

The closed string has potential anomalies related to:

1. **Modular invariance**: The one-loop partition function on a torus must be invariant under the $SL(2, \mathbb{Z})$ symmetry of the torus.
2. **Gravitational anomalies**: In 10 dimensions, chiral fermions (right-movers and left-movers) can contribute anomalies.
3. **Dilaton-Weyl anomalies**: The dilaton couples to the worldsheet Ricci scalar, introducing potential anomalies.

For the 10-dimensional superstring, these anomalies conspire to cancel if and only if:

$$\text{Tr}(F \wedge F) + \text{Tr}(R \wedge R) = 0$$

where $F$ is the Yang-Mills curvature and $R$ is the spacetime Ricci tensor. This **Green-Schwarz mechanism** shows that the heterotic string is self-consistent, while the Type II requires additional symmetries.

In the field theory language, the nonpolynomial terms serve to **encode these anomaly-cancellation conditions**. Different orderings of vertices and different high-point interactions are related by anomaly constraints.

### Finiteness and Renormalization

Despite the infinite series of nonpolynomial terms, the closed string field theory is **finite to all orders in perturbation theory**. This is because:

1. **Extended objects**: The string is not a point particle, so loop integrals have natural cutoffs.
2. **Topological constraints**: The worldsheet is a closed Riemann surface, and integration over moduli space is finite.
3. **Collective cancellation**: High-order terms are suppressed by powers of $1/M_s$ where $M_s = 1/\sqrt{\alpha'}$ is the string mass scale.

The effective action for long-distance physics (energies $E \ll M_s$) is:

$$S_{\text{eff}} = \frac{1}{2\kappa^2} \int d^d x \sqrt{g} \, [R - (\partial \Phi)^2 + \mathcal{O}(\alpha')]$$

which is Einstein gravity plus corrections suppressed by powers of $\alpha' E^2$.

---

## Key Results

1. **Closed string field theory requires nonpolynomial interactions**: Unlike open strings (where cubic is sufficient), closed strings require infinitely many vertex terms.

2. **Gravity is built in**: The graviton is automatically present as the massless excitation; its interactions arise consistently from the field theory formulation.

3. **Anomalies are encoded in vertices**: Cancellation of worldsheet anomalies is guaranteed by the structure of the nonpolynomial terms.

4. **Dilaton and metric couple inseparably**: The dilaton $\Phi$ and graviton $h_{\mu\nu}$ cannot be separated; they form a coupled system. The dilaton-coupling constant relationship:

$$g_s = e^{\langle \Phi \rangle / 2}$$

emerges from the vacuum expectation value of the dilaton field.

5. **Finiteness despite infinitude of terms**: The sum of all nonpolynomial vertices (to all orders) is finite, with loop corrections suppressed by $g_s^2$.

---

## Impact and Legacy

Kaku and Lykken's work on closed string field theory was important because it:

- **Addressed the gravity puzzle**: Showed that gravity emerges naturally from closed string quantization.
- **Clarified anomaly structure**: Connected worldsheet anomaly cancellation to spacetime field theory.
- **Established finiteness**: Proved that closed string field theory, despite its nonpolynomial appearance, is a finite quantum theory.
- **Influenced M-theory development**: The structure of nonpolynomial interactions in closed string theory foreshadowed the structure of M-theory and its dualities.

The paper is cited 100+ times and remains the standard reference for closed string field theory.

---

## Connection to Phonon-Exflation Framework

**Relevance: HIGH (gravity emergence)**

The phonon-exflation model aims to derive all forces—including gravity—from internal quantization. Kaku-Lykken's demonstration that gravity emerges from closed string field theory is a direct precedent.

**Parallels**:

1. **Gravity from internal quantization**: Just as closed string field theory generates gravitons as quantized excitations, phonon-exflation generates both gauge bosons (from oscillations) and the metric (from curvature fluctuations) of the internal space.

2. **Nonpolynomial structure**: Phonon-exflation likely requires an infinite series of interaction terms mixing the internal geometry and the Dirac spectrum. This mirrors Kaku-Lykken's nonpolynomial action.

3. **Massless spectrum from geometry**: In closed strings, massless fields (graviton, dilaton) are universal. In phonon-exflation, the massless modes (photon, W/Z, gluons) emerge from the Dirac spectrum at certain critical points (tau).

4. **Dilaton-metric coupling**: In Kaku-Lykken, the dilaton couples inseparably from the metric. In phonon-exflation, the scalar field(s) (responsible for Higgs mechanism) couple inseparably from the SU(3) structure.

**Application to framework**: The nonpolynomial structure in Kaku-Lykken suggests that the spectral action in phonon-exflation should include not just the Einstein-Hilbert term but an infinite series of higher-curvature corrections on the SU(3) fiber. These would be essential for consistency with the internal quantization.

---

## References & Further Reading

- Kaku, M., & Lykken, J. (1990). "The structure of non-polynomial closed string field theory," *Nucl. Phys. B*, 341(2), 249–279.
- Zwiebach, B. (1993). "Closed string field theory: Quantum action and the Batalin-Vilkovisky master equation," *Nucl. Phys. B*, 390(1), 77–120.
- Green, M. B., Schwarz, J. H., & Witten, E. (1987). *Superstring Theory*, Vol. 1 & 2. Cambridge University Press.
- Polchinski, J. (1998). *String Theory*, Vol. 1 & 2. Cambridge University Press.
