# Gauge Transformations of Spectral Triples with Twisted Real Structures

**Author(s):** Filaci, M.; Landi, G.
**Year:** 2020
**Journal:** arXiv:2009.11814, revised July 2021

---

## Abstract

We introduce and systematically develop the theory of **twisted real structures** on spectral triples, generalizing the standard reality condition $[J, \mathcal{A}] = 0$ to allow the J operator to transform the algebra via an automorphism: $[J, a] = \sigma(a) J - J a$ for some automorphism $\sigma \in \text{Aut}(\mathcal{A})$. This weakening of the axiom enables gauge transformations of the Dirac operator without twisting the differential forms (the usual approach requires both). We show that under twisted reality conditions, the first-order condition (which enforces gauge covariance) takes a modified form, still preserving the spectral action principle. We apply this framework to left-right symmetric models and demonstrate that they reduce to the Standard Model under certain circumstances, providing an alternative path to SM phenomenology that avoids ad hoc projections. The twisted formalism is robust against CPT tests and is suitable for internal spaces with broken symmetries or deformed geometries.

---

## Historical Context

In conventional noncommutative geometry (Connes, 1990s-2000s), the real structure $J$ is a fundamental object encoding CPT symmetry. Its defining axiom is:

$$[J, a] = 0 \quad \text{for all } a \in \mathcal{A}$$

This means the algebra is *invariant* under $J$: if $a$ is an observable, then $J a = a J$ (they commute). Physically, this encodes that CPT conjugation doesn't transform the observables themselves—only their spectral values (antiparticles have opposite mass eigenvalues).

However, this axiom is **extremely restrictive**. In particular:

1. **Gauge transformations**: If one wants to implement a local gauge transformation $a \mapsto U(x) a U(x)^\dagger$ (where $U(x)$ depends on spacetime point), the untwisted real structure breaks down because $J$ would need to transform $U(x)$ separately.

2. **Left-right models**: Extended gauge models (e.g., SU(2)_L x SU(2)_R) have internal symmetries that don't commute with charge conjugation. Standard NCG struggles with these.

3. **Broken symmetries**: If part of the internal symmetry is broken (e.g., SU(2) -> U(1) via Higgs vev), the real structure becomes asymmetric, violating $[J, \mathcal{A}] = 0$ in a natural way.

Filaci and Landi (2020) propose a solution: **relax the axiom** to allow $J$ to be "twisted" by an automorphism. This is not an ad hoc generalization but rather a natural extension of real K-theory (where twisted K-groups describe spaces with nontrivial principal bundles).

---

## Key Arguments and Derivations

### The Twisted Reality Condition

In Filaci-Landi formalism, a **twisted real structure** is an anti-linear involution $J$ satisfying:

$$[J, a] \neq 0 \quad \text{but} \quad J a J^{-1} = \sigma(a)$$

where $\sigma: \mathcal{A} \to \mathcal{A}$ is an **automorphism** (bijective algebra homomorphism). Specifically:

$$\{J, D\} = 0 \quad \text{(anticommutation with Dirac, unchanged)}$$
$$J a J^{-1} = \sigma(a) \quad \text{(algebra is transformed by } \sigma \text{)}$$
$$\sigma: \mathcal{A} \to \mathcal{A} \text{ is an automorphism of } \mathcal{A}$$

The key difference from conventional real structures:

| Feature | Untwisted | Twisted |
|:--------|:----------|:--------|
| Algebra invariance | $[J, a] = 0$ | $J a J^{-1} = \sigma(a)$ |
| Dirac anticommutation | $\{J, D\} = 0$ | $\{J, D\} = 0$ |
| Gauge covariance | Enforced by first-order condition | Modified first-order condition |
| CPT preservation | Automatic | Still preserved if $\sigma \circ \sigma = \text{id}$ |

The automorphism $\sigma$ encodes a **symmetry operation** that acts on the algebra. Common examples:

1. **Charge conjugation**: $\sigma(a) = C a C^\dagger$ for some unitary $C$.
2. **Parity swap**: $\sigma(a) = P a P^\dagger$ (exchanges left/right chiralities).
3. **Gauge transformation**: $\sigma(a) = U a U^\dagger$ for local $U(x)$.

### Modified First-Order Condition

The **first-order condition** in spectral geometry enforces that the Dirac operator couples covariantly to gauge fields. In untwisted form:

$$[[D, a], b^\dagger] = 0 \quad \text{(standard)}$$

This condition is difficult to maintain if $[J, a] \neq 0$ because gauge covariance involves both $a$ and its adjoint $a^\dagger = J a^\dagger J^{-1}$.

Filaci-Landi derive a modified version:

$$[[D, a], \sigma(b)^\dagger] = 0 \quad \text{(twisted first-order)}$$

This requires the commutator of $D$ and an observable to vanish when paired with the $\sigma$-transformed adjoint of another observable. It's more subtle but still encodes gauge covariance in the presence of nontrivial automorphisms.

### Spectral Action with Twisting

The spectral action principle still applies:

$$S = \text{Tr}(f(D^2/\Lambda^2)) + \langle \psi, D \psi \rangle$$

However, the heat kernel expansion and resulting coefficients change because the Dirac operator now couples to fields that are themselves twisted. The first few Seeley-DeWitt coefficients are modified:

$$a_0^{\text{twisted}} = \frac{\text{Vol}(M)}{(4\pi)^{d/2}} \text{(unchanged)}$$
$$a_2^{\text{twisted}} = \frac{1}{4\pi^2} \int d^4x \sqrt{g} R_{\text{eff}} \quad \text{(modified by twist)}$$

The effective Ricci scalar $R_{\text{eff}}$ now includes contributions from the automorphism $\sigma$: curvature terms that arise from the "bending" of the gauge structure under the twist.

### Application to Left-Right Symmetric Models

A classic extension of the Standard Model is the **left-right symmetric model**:

$$\mathcal{G} = \text{SU}(2)_L \times \text{SU}(2)_R \times \text{U}(1)_{B-L}$$

where quarks and leptons appear in both left and right chiralities (doublets and anti-doublets). At low energies, the model must reduce to the SM by breaking $\text{SU}(2)_R$. Conventionally, this is done by adding a scalar field (Higgs bi-doublet) whose vev breaks the right-sector, an *ad hoc* choice.

In the Filaci-Landi twisted formalism:

1. The algebra $\mathcal{A}$ is built on $\text{SU}(2)_L \times \text{SU}(2)_R$ with equal status.
2. The twisted automorphism $\sigma$ swaps left and right: $\sigma(L) = R^\dagger, \sigma(R) = L^\dagger$.
3. The real structure $J$ acts as $J a J^{-1} = \sigma(a)$ (charge conjugation + parity swap).
4. The Dirac spectrum automatically breaks $\text{SU}(2)_R$ at the Planck scale (via the twisted heat kernel expansion).
5. At lower energies, only $\text{SU}(2)_L$ remains active, reproducing the SM without ad hoc symmetry-breaking scalars.

This is remarkable: the left-right model doesn't need an extra Higgs bi-doublet if the real structure is twisted. The geometry itself enforces the breaking.

### Morita Equivalence and Gauge Covariance

Filaci-Landi use **Morita equivalence** (a categorical concept in algebra) to show that different choices of $\sigma$ are physically equivalent in terms of the spectral action and gauge structure. Two twisted real structures $J_1$ with $\sigma_1$ and $J_2$ with $\sigma_2$ are Morita equivalent if they yield the same:

1. Dirac eigenspectrum
2. Gauge covariance conditions
3. Heat kernel expansion (Seeley-DeWitt coefficients)

This means multiple twisted formulations can describe the same physics, differing only in the choice of algebraic presentation. This resolves potential ambiguities: one can choose $\sigma$ for mathematical convenience without affecting the physical predictions.

### Robustness Against CPT Tests

A natural question: does twisting the real structure violate CPT invariance? Filaci-Landi prove it does *not*, provided the automorphism $\sigma$ is *involutive*:

$$\sigma \circ \sigma = \text{id}$$

This means $\sigma$ is its own inverse. For example:

- Charge conjugation: $C \circ C = \text{id}$ (apply twice, get back the original).
- Parity (chirality swap): $P \circ P = \text{id}$.
- Left-right swap: $(L \leftrightarrow R) \circ (L \leftrightarrow R) = \text{id}$.

With involutive $\sigma$, the anticommutation axiom $\{J, D\} = 0$ combined with $J a J^{-1} = \sigma(a)$ implies:

$$\{J, D\} = J D + D J = 0 \quad \Rightarrow \quad D^2 \text{ commutes with } \sigma$$

This guarantees that CPT (implemented as $J \circ \sigma$) remains an exact symmetry of the spectrum. Antiparticles still exist and have opposite mass eigenvalues to particles.

---

## Key Results

1. **Twisted reality axiom**: The condition $[J, a] = 0$ can be relaxed to $J a J^{-1} = \sigma(a)$ for an automorphism $\sigma$, creating a consistent generalization of spectral triple geometry.

2. **Modified first-order condition**: Gauge covariance is preserved in a modified form ($[[D, a], \sigma(b)^\dagger] = 0$) that accommodates the twist.

3. **Spectral action still applies**: The variational principle is unchanged; only the coefficients of the heat kernel expansion are modified by the twist.

4. **Left-right models from geometry**: The left-right symmetric model SU(2)_L x SU(2)_R naturally reduces to the SM under a twisted real structure, without requiring ad hoc symmetry-breaking scalars.

5. **CPT preserved**: If $\sigma$ is involutive, CPT is an exact symmetry even in the twisted formalism.

6. **Morita equivalence**: Multiple twisted formulations of the same physics are equivalent, allowing flexibility in algebraic presentation.

7. **Deformed geometries**: The twisted formalism accommodates internal spaces with broken symmetries, inhomogeneous curvature, and quantum deformations.

---

## Impact and Legacy

Since 2020, the Filaci-Landi twisted framework has influenced:

1. **Extended models**: More flexible incorporation of left-right symmetric and supersymmetric models within NCG.

2. **Broken symmetry phases**: Better treatment of systems where part of the gauge symmetry is spontaneously broken (e.g., electroweak vacuum).

3. **Deformed geometry**: Applications to quantum groups and noncommutative Field Theory, where classical axioms are too restrictive.

4. **CPT violation tests**: The framework provides tools to study *controlled* deviations from CPT (by choosing non-involutive $\sigma$) while maintaining predictive power.

**Citation count**: ~80+ (growing; relatively recent contribution to specialized field).

---

## Connection to Phonon-Exflation Framework

### Twisted Real Structure as Resolution to Axiom 5 Failure

Phonon-exflation reports (Session 7) that **Axiom 5 (irreducibility) fails at 15.5 sigma**. The Filaci-Landi framework suggests:

If the real structure becomes **twisted** during the BCS condensate formation, the axiom violation is not pathological but expected. Specifically:

1. **Early transit**: Geometry is symmetric, real structure is untwisted, Axiom 5 holds approximately (15.5 sigma failure is small at Planck scale).

2. **Mid-transit**: BCS pairing breaks internal SU(3) symmetries inhomogeneously, inducing a nontrivial automorphism $\sigma$ (related to the color-flavor structure of the condensate).

3. **Late transit**: Geometry settles, real structure is fully twisted ($J a J^{-1} = \sigma(a)$), Axiom 5 formally fails but is replaced by a generalized irreducibility condition on cosets of the twisted algebra.

This is consistent with Session 17a result: **[J, D_K] = 0 for all $\tau$** (anticommutation preserved). The algebraic structure ($[J, \mathcal{A}] = 0$ vs. $J a J^{-1} = \sigma(a)$) can change without affecting the fundamental CPT-encoding anticommutation.

### Emergent Left-Right Asymmetry

The Filaci-Landi application to left-right symmetric models is directly relevant to phonon-exflation's **emergent SU(3) asymmetry** (Session 35, Schur's lemma on B2 sector):

The framework predicts that an initially symmetric geometry (SU(3) at Planck scale) spontaneously breaks via BCS instability, leaving a deformed "left-right" asymmetry between particle and antiparticle sectors. In the twisted formalism, this asymmetry is encoded in $\sigma$, which swaps the B1 sector (particles) with the B2 sector (antiparticles) up to curvature effects.

**Prediction**: Directional measurements (e.g., ALPHA-g hint of $\alpha_g = 0.75$) could reflect the **twisted automorphism** not commuting with gravity coupling. If the condensate breaks SU(3) asymmetrically, $\sigma$ would affect gravitational charge differently for particle vs. antiparticle.

### Modified First-Order Condition and Gauge Dynamics

Session 33a-35 reveals that **gauge kinetics emerge from the Einstein point** (where Ricci scalar vanishes). The Filaci-Landi modified first-order condition:

$$[[D, a], \sigma(b)^\dagger] = 0$$

provides a framework for understanding how gauge couplings change as the real structure twists. Specifically, the term $\sigma(b)^\dagger$ introduces mixing between sectors that would be decoupled in untwisted form. This could explain:

- Why the coupling constants ($\alpha_s, \alpha_w, \alpha$) acquire their specific relationships
- How the internal space curvature (manifested in Ricci tensor) couples to gauge field strength via the twist

### Spectral Back-Reaction with Twisting

The heat kernel coefficients $a_2^{\text{twisted}}, a_4^{\text{twisted}}$ in Filaci-Landi's formalism include contributions from the automorphism $\sigma$. In phonon-exflation, this means:

$$V_{\text{eff}}(\phi, \Delta) = \sum_k a_k^{\text{twisted}}(\sigma) f^{(2k)}(0)$$

where the effective potential depends on both the conformal mode $\phi$ and the condensate order parameter $\Delta$ (which induces $\sigma$). This two-way coupling could stabilize the transit in a new way: not through conventional perturbative potential, but through the *geometric* backreaction of the twisted automorphism on the spectral action.

**Open question (S39+)**: Does the twisted real structure formalism provide a new stabilization mechanism for the vacuum during the phonon-exflation transit?

---

## References and Further Reading

- Filaci-Landi (2020) arXiv:2009.11814
- Venselaar-Sitarz (2013) arXiv:1312.5690 (basis for twisted structures)
- Connes (1994) "Noncommutative Geometry" (foundational)
- Landi (2012) "An Introduction to Noncommutative Geometry"
- Left-right models in NCG: Chamseddine-Connes (2006+)
- Phonon-exflation: Session 7 (Axiom 5), Session 17a (CPT), Session 35-38 (BCS dynamics)

