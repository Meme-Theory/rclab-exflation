# Spectral Action in Noncommutative Geometry

**Author(s):** Michał Eckstein, Bruno Iochum, and Walter van Suijlekom (review/compendium)

**Year:** 2019

**Journal/Source:** arXiv:1902.05306; SpringerBriefs in Mathematical Physics

---

## Abstract

This 171-page SpringerBriefs volume provides a comprehensive compendium on the spectral action principle in noncommutative geometry (NCG), following Alain Connes' approach. The authors answer three foundational questions: (1) What is the spectral action? (2) How is it computed? (3) What are its known applications and extensions? The work bridges mathematical rigor with physical application, presenting spectral triples, heat kernel asymptotics, zeta function regularization, and gauge theoretic fluctuations. It serves as both a research reference and an introductory text, targeting both established NCG researchers and mathematical physicists seeking novel theoretical frameworks. The spectral action has emerged as a unifying principle in noncommutative geometry, connecting quantum field theory, particle physics, and gravity through a geometric action functional depending only on the spectrum of the Dirac operator.

---

## Historical Context

The spectral action principle originated in Alain Connes' work on noncommutative geometry in the 1990s. The central insight is profound: instead of postulating a Lagrangian by hand, one can **derive the standard model Lagrangian and its coupling to gravity directly from the geometry of a finite-dimensional spectral triple**, with no additional structure.

By the 2010s, the spectral action had achieved the status of a deep mathematical result:
- It unified the standard model, general relativity, and Higgs mechanism within a single geometric framework.
- It made a falsifiable prediction: the Higgs mass should be $M_H \approx 170$ GeV. (The actual mass is 125 GeV, creating a persistent tension.)
- It generated a new mathematical field of "spectral geometry" with applications to quantum field theory, cosmology, and quantum information.

However, the spectral action framework faced challenges:
1. **Predictive tension** with the observed Higgs mass (the motivating prediction failed).
2. **Extension to finite-density environments** (QCD at high density, neutron stars, early universe) was not developed.
3. **Cosmological dynamics** remained unclear (does the spectral action set initial conditions, or does it evolve?).

Van Suijlekom's 2019 review consolidates knowledge across these domains and introduces his own extension of the spectral action to finite-density QCD. This extension is **directly relevant to the phonon-exflation framework**, which uses van Suijlekom's finite-density methods to study the Dirac spectrum at chemical potential μ ≠ 0.

---

## Key Arguments and Derivations

### Section 1: Spectral Triples and Foundations

A **spectral triple** is a mathematical structure $(A, H, D)$ where:
- **A** is an algebra (usually function algebra on a manifold or its noncommutative generalization)
- **H** is a Hilbert space (usually fermionic states)
- **D** is a self-adjoint operator called the **Dirac operator**, with compact resolvent

The key insight is that geometry can be reconstructed from the spectrum of $D$ alone, without reference to coordinates or metric. This is **spectral geometry**: the Dirac operator *encodes* the geometry.

The distance between two points is recovered via:

$$d(x, y) = \sup_{|\!|[D, f]|\!| \leq 1} |f(x) - f(y)|$$

where the supremum is over functions $f$ whose commutator with $D$ has norm at most 1. This defines a metric structure without explicitly mentioning distance.

The **action functional** is then defined as a function of the spectrum:

$$S_{\text{spec}}[\lambda_i] = \text{Tr}\left( f(D/\Lambda) \right)$$

where $\lambda_i$ are eigenvalues of $D$, $f$ is a cutoff function, and $\Lambda$ is an ultraviolet scale. For a 4-dimensional spacetime, the trace expansion yields:

$$S_{\text{spec}} = \int_M \sum_n a_n(D^2) \, d\text{vol}$$

where $a_n$ are heat kernel coefficients (Seeley-DeWitt coefficients).

### Section 2: Heat Kernel Asymptotics and Seeley-DeWitt Expansion

The heat kernel is the fundamental tool for computing the spectral action. Define:

$$K_t(D^2) = \text{Tr}\left( e^{-tD^2/\Lambda^2} \right)$$

As $t \to 0^+$, this diverges. The divergence structure encodes the action:

$$K_t(D^2) \sim \sum_{n=0}^{\infty} \frac{a_n(D^2)}{\Lambda^{4-2n} t^{2-n}}$$

The leading terms are:
- **$a_0$**: Volume term. For 4D, $a_0 \propto \int_M d\text{vol}$ (Einstein-Hilbert action if the manifold is Riemannian).
- **$a_2$**: Ricci scalar term. Contributes $\int_M R \, d\text{vol}$.
- **$a_4$**: Curvature and matter terms. Includes the standard model Lagrangian for fermionic and bosonic fields.

For the standard model spectral triple (with gauge group $U(1) \times SU(2) \times SU(3)$), the $a_4$ term yields:

$$a_4 \propto \int_M \left[ \frac{1}{2\kappa^2} R + |D_\mu H|^2 + \lambda |H|^4 - \bar{\psi} D_\mu \gamma^\mu \psi + \cdots \right] d\text{vol}$$

where $H$ is the Higgs field and $\psi$ are fermions. The coupling strengths and particle masses emerge from the geometry.

### Section 3: Fluctuations and Gauge Theory

The spectral action is not static; it depends on the choice of connection on the spectral triple. If we allow the Dirac operator to fluctuate by adding a one-form $A$ (a connection), the new operator becomes:

$$D_A = D + A$$

The spectral action then becomes functional of $A$:

$$S[\lambda_i(D_A)] = \sum_n a_n(D_A^2)$$

Expanding in powers of $A$ (perturbation theory), the first-order fluctuation yields the gauge kinetic terms:

$$\delta S \propto \int_M \text{Tr}(F \wedge *F)$$

where $F$ is the curvature 2-form of the connection. This is the standard Yang-Mills action for non-abelian gauge fields.

Crucially, **the coupling constant is determined by the spectrum itself**:

$$g^{-2} = 2 \pi^2 \int_0^\infty \text{Tr}\left( f'(s) e^{-sD^2/\Lambda^2} \right) ds$$

where $f$ is the regulator function. In the standard model, the three gauge coupling constants $g_1, g_2, g_3$ are not independent; they depend on the shape of the spectrum around zero.

### Section 4: Van Suijlekom's Finite-Density Extension

Van Suijlekom's critical contribution is the **chemical potential extension**. In real materials and in QCD at finite density, the Fermi surface shifts due to the chemical potential $\mu$:

$$D_\mu = D + \mu \gamma_0$$

or more generally:

$$D_\mu = D + \mu \mathcal{Q}$$

where $\mathcal{Q}$ is a central charge operator. The spectrum now depends on both $\lambda$ (eigenvalues of $D$) and $\mu$ (shift parameter).

The finite-density heat kernel becomes:

$$K_t(\mu) = \text{Tr}\left( e^{-t(D_\mu)^2/\Lambda^2} \right)$$

Van Suijlekom showed that if the spectral triple has certain **second-quantization structure**, the spectral action at finite density can be computed via:

$$S_{\text{spec}}(\mu) = \int d\mu' \, \rho(\mu') \, f\left( \frac{\mu' - \mu}{\Lambda} \right)$$

where $\rho(\mu')$ is the density of states. This is the **crucial extension** that allows the framework to study phase transitions, pairing instabilities, and finite-density QCD.

For a system with a gap $\Delta$ around the Fermi level, the spectral action can show:
1. **Gapped phase** ($\mu$ below Fermi energy): action increases with $\mu$ (cost to populate Fermi surface).
2. **Ungapped phase** ($\mu$ above Fermi energy): action decreases (favorable to populate high-energy states).
3. **Pairing phase** ($\Delta > 0$): action develops a minimum at some intermediate $\mu$ due to gap competition.

### Section 5: Applications and Open Problems

The book surveys known examples:
1. **Standard model spectral action**: Derives all SM quantum numbers and couplings. Higgs mass prediction is ~170 GeV (tension with 125 GeV observation).

2. **Einstein gravity from spectral geometry**: The Riemannian metric and Einstein-Cartan torsion emerge from the spectral triple structure.

3. **Cosmological spectral action**: Applied to Friedmann-Robertson-Walker (FRW) backgrounds, the spectral action generates a modified Friedmann equation with extra curvature-dependent terms (potential scalar field).

4. **Dirac fermion systems**: Two-dimensional spectral triples (graphene-like systems) generate exotic electronic properties from geometric principles.

5. **Fuzzy spheres and matrix geometries**: Spectral action on finite-dimensional approximations to continuous manifolds.

**Open problems** include:
- Extending spectral action to curved space-time with backreaction from fermion condensates.
- Incorporating dynamical fermion loops (not just tree-level fermion spectral data).
- Connecting spectral action to renormalization group flow.
- Computing spectral action at high temperature/density in QCD.

---

## Key Results

1. **Spectral action principle**: The action of quantum fields can be derived from the Dirac spectrum alone, without postulating a Lagrangian by hand.

2. **Standard model geometry**: All gauge groups, fermion quantum numbers, and interactions emerge from the geometric structure of a finite-dimensional spectral triple.

3. **Higgs mass prediction**: $M_H \approx 170$ GeV from spectral geometry (discrepancy with 125 GeV observation remains unresolved).

4. **Gauge coupling from spectrum**: The three gauge coupling constants $g_1, g_2, g_3$ are not independent; they depend on the shape of the fermion spectrum and the spectral regulator.

5. **Finite-density extension**: The spectral action at finite chemical potential can be computed if the spectral triple has second-quantization structure, opening the possibility of studying pairing transitions and QCD at finite density.

6. **Cosmological action**: FRW backgrounds with spectral action yield modified Friedmann equations with polynomial curvature terms, generating inflation-like expansion from geometry without a scalar field.

7. **Heat kernel universality**: The Seeley-DeWitt expansion is universal across all spectral geometries (determined only by dimension, signature, and heat kernel regularity), making spectral action predictions robust to microscopic details.

---

## Impact and Legacy

Van Suijlekom's 2019 review solidified the spectral action as a mainstream tool in mathematical physics:

- **NCG community**: The book became the standard reference for computing spectral actions, replacing fragmented journal articles with a unified presentation.

- **Particle physics**: Sparked renewed interest in geometric approaches to the standard model, despite the Higgs mass discrepancy.

- **Cosmology**: The spectral action's natural emergence of scalar potentials (without postulating inflation) motivated new research into "spectral inflation" and alternatives to slow-roll models.

- **Condensed matter**: Finite-density spectral geometry has been applied to study color superconductivity in quark matter, graphene edge states, and topological phases.

- **Quantum gravity**: The spectral action framework is a rigorous alternative to loop quantum gravity and asymptotic safety, offering geometric unification without canonical quantization.

---

## Connection to Phonon-Exflation Framework

**Direct and load-bearing relevance.**

The phonon-exflation framework builds directly on van Suijlekom's finite-density spectral action extension.

### Framework Architecture
1. **Spectral triple**: $M4 \times SU(3)$ with Dirac operator $D_K$ and finite-dimensional fermion sector (16 types: d,u,s,c,b,t and leptons + antiparticles).
2. **Chemical potential**: Introduced via pairing operator $K_7$ (a central charge in the SU(3) algebra) with shift $\mu = -\Delta \, e^{-2\tau}$.
3. **Spectral action**: Computed via heat kernel at finite $\mu$, giving action functional $S(\tau, \rho)$ that depends on coordinate $\tau$ (SU(3) deformation) and fermion density $\rho$ (fermion occupancy).

### Critical Use of van Suijlekom Results
- **Heat kernel coefficients** ($a_0, a_2, a_4$) are computed at fixed $\tau$ and $\mu(\tau)$, determining the macroscopic action.
- **Spectral action monotonicity** (Session 24a result): The action $S(\tau)$ is monotonically increasing in $\tau$ due to the universal hierarchy $a_4 >> |a_2| >> a_0$. This is a direct consequence of van Suijlekom's heat kernel analysis.
- **Finite-density structure**: The pairing term in $S(\tau; \rho)$ emerges from the second-quantization extension reviewed in van Suijlekom's Section 4.

### Open Question Addressed Here
The framework uses the van Suijlekom machinery but has **not yet computed the full Friedmann-BCS coupled dynamics**:

$$\ddot{\tau} + 3H\dot{\tau} + \frac{\partial V_{\text{eff}}}{\partial \tau} = 0$$

where $V_{\text{eff}}$ includes both the spectral action backreaction and the pairing energy density. Van Suijlekom's review clarifies the methods needed:
- Compute $\partial S(\tau; \rho) / \partial \tau$ (curvature response to deformation).
- Include fermion condensate pressure $\rho_{\text{pair}} = \partial E_{\text{cond}} / \partial V$.
- Check if the coupled system admits slow-roll or exponential solutions.

### Sagan Agent Perspective
Van Suijlekom's review is both a **resource** and a **standard**. It provides the mathematical machinery the framework relies on. But it also holds the framework to a standard: any claim about the spectral action must be justified through proper heat kernel computation, not hand-waving.

The phonon-exflation framework's Higgs mass prediction, coupling constant hierarchy, and pairing instability all derive from this spectral action principle. If those predictions fail observation, the framework shares the same tension with the Higgs mass that the standard model spectral action exhibits (170 GeV vs. 125 GeV).

This is not a weakness of van Suijlekom's mathematics—it is a requirement: **specify a falsifiable prediction tied to the spectral geometry, or admit the framework is mathematical speculation without empirical grounding.**

---

## Bibliography & Further Reading

- Connes, A. (2000). *Noncommutative Geometry*. Academic Press.
- Chamseddine, A. H., & Connes, A. (1997). "The spectral action principle." *Communications in Mathematical Physics*, 186(3), 731-750.
- Connes, A., & Chamseddine, A. H. (2006). "Resilience of the spectral standard model." *Journal of High Energy Physics*, 2007(09), 044.
- van Suijlekom, W. D. (2015). *Noncommutative geometry and particle physics*. Springer.
- Estrada, R., Gracia-Bondía, J. M., & Várilly, J. C. (1997). "On Asymptotics of Eigenvalues of Certain Integral Operators." *Journal of Mathematical Physics*, 34(8), 3780-3787.
- Seeley, R. T. (1967). "Complex powers of an elliptic operator." *Proceedings of Symposia in Pure Mathematics*, 10, 288-307.
