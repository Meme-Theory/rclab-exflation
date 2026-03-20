# Lectures on Twistor Theory

**Author(s):** Adamo
**Year:** 2017
**Journal:** arXiv:1712.02196

---

## Abstract

These pedagogical lectures provide a comprehensive introduction to twistor theory, Penrose's approach to spacetime geometry via complex geometry in twistor space. The lectures cover: (1) twistor space as a fibration of the Riemann sphere over spacetime; (2) integrable structure and the definition of null geodesics; (3) twistor description of conformal geometry; (4) applications to gravitational waves and radiation; (5) scattering amplitudes in Yang-Mills and gravity (modern developments). The lectures emphasize the power of twistor methods in simplifying calculations and revealing hidden geometric structures. Applications include gluon scattering amplitudes, gravitational wave propagation, and the holomorphic structure of self-dual Yang-Mills theory.

---

## Historical Context

Roger Penrose introduced twistor theory in 1967 as a radical reformulation of spacetime geometry. Rather than starting with a 4D spacetime $\mathbb{R}^{3,1}$ with metric structure, twistor theory starts with the space of null geodesics (light rays). Each null geodesic corresponds to a **null twistor**, a point in complex 4D projective space $\mathbb{CP}^3$.

The key insight is **conformal invariance**: the null geodesics of a spacetime are determined entirely by the **conformal structure** (angles and light cones, but not distances). Conversely, the conformal structure is reconstructed from the set of null geodesics. This suggests that twistor space $\mathbb{CP}^3$ is the "fundamental" arena, and spacetime is a secondary construction.

Early applications (1960s-1980s) of twistor theory were limited to exact solutions (plane waves, self-dual Yang-Mills theory) and conformal field theory. The approach seemed elegant but lacked practical utility for realistic scattering processes.

This changed dramatically in the 2000s with the discovery of the **BCFW recursion relations** (Britto-Cachazo-Feng-Witten, 2005) for scattering amplitudes. These relations revealed that gluon and gravity amplitudes have a **hidden holomorphic structure** that is naturally visible in twistor space. The twistor formulation is often far simpler than the Feynman diagram approach, leading to rapid progress in perturbative gravity and Yang-Mills theory.

The 2017 Adamo lectures synthesize both the foundational geometric picture and the modern amplitude applications, providing the first truly modern pedagogical treatment of the subject.

---

## Key Arguments and Derivations

### Twistor Space Geometry

**Twistor space** is $\mathbb{PT} = \mathbb{CP}^3$, the complex 3-dimensional projective space. A point in twistor space is a null twistor $Z^\alpha = (\lambda^a, \mu^{\dot{a}})$ (using spinor notation), where:

- $\lambda^a$ (with $a=0,1$) is a 2-component complex spinor
- $\mu^{\dot{a}}$ (with $\dot{a} = 0, 1$) is another 2-component complex spinor
- Projective equivalence: $(Z^\alpha) \sim (\kappa Z^\alpha)$ for $\kappa \in \mathbb{C}^*$

The **Penrose fibration** is the map:
$$\pi: \mathbb{PT} \to \mathbb{M}$$
$$Z^\alpha = (\lambda^a, \mu^{\dot{a}}) \mapsto x^{a\dot{a}} = \mu^{\dot{a}} \lambda^a$$

In coordinates, this becomes a map from $\mathbb{CP}^3$ to complexified compactified spacetime $\mathbb{CM}$ (Minkowski space with conformal compactification).

Each **null geodesic** in spacetime corresponds to a **Riemann sphere** $\mathbb{CP}^1 \subset \mathbb{CP}^3$ in twistor space. Conversely, each point in spacetime (null or timelike) corresponds to either a null plane in twistor space or a conic surface.

### Conformal Structure from Twistor Geometry

The **conformal metric** in spacetime is reconstructed from the twistor space geometry:

$$g_{\mu\nu} dx^\mu dx^\nu = \frac{1}{2} (\lambda \sigma^{\mu\dot{a}} \lambda^* d\mu_{\dot{a}})^2$$

where $\sigma^\mu$ are the Pauli matrices (spinor representation of spacetime vectors).

The key property: **angles are preserved** under the Penrose fibration. Two null geodesics intersect at a spacetime point with a certain angle; this angle is encoded in the intersection geometry of the corresponding $\mathbb{CP}^1$ curves in twistor space.

This explains why twistor theory is naturally **conformally invariant**: the conformal group $SO(4,2)$ acts as a group of projective transformations on $\mathbb{PT} = \mathbb{CP}^3$.

### Scattering Amplitudes and Twistor Momentum Space

In Yang-Mills theory, the scattering amplitude for $n$ gluons with momenta $p_i$ and helicities $h_i$ is written as:
$$\mathcal{A}_n(p_1, ..., p_n; h_1, ..., h_n)$$

In **twistor momentum space**, each gluon is represented by a twistor:
$$Z_i = (\lambda_i, \mu_i)$$

where $\lambda_i$ encodes the momentum $p_i$ and $\mu_i$ encodes the helicity $h_i$.

A remarkable fact: **scattering amplitudes become more "holomorphic"** in this representation. For instance:

- **MHV amplitudes** (maximally-helicity-violating, with two negative helicity gluons and $n-2$ positive): The amplitude is a rational function of the $\lambda_i$ only (not $\bar{\lambda}_i$), indicating holomorphic structure.

$$A_n^{\text{MHV}} = \frac{1}{\prod_{i=1}^n \langle i, i+1 \rangle} \quad (\text{Parke-Taylor formula})$$

where $\langle i, j \rangle = \lambda_i \cdot \lambda_j$ is the spinor inner product.

- **N^k MHV amplitudes** (with $2+k$ negative helicity gluons): These are quasi-holomorphic rational functions, with poles at specific incidence relations.

### Soft Theorems and Conformal Ward Identities

The **soft collinear bootstrap** uses the fact that as a gluon momentum $p_k \to 0$, the amplitude has a universal soft structure:
$$\mathcal{A}_n \to \frac{1}{p_k \cdot (p_i + p_j)} \mathcal{A}_{n-1} + \text{subleading}$$

In twistor space, this soft limit corresponds to a **conformal rescaling** that preserves the twistor geometry except in a localized region. The Ward identities for conformal symmetry directly yield the soft theorems.

This provides a **conformal/Weinberg soft theorem connection**: the universal long-distance behavior of amplitudes is a consequence of conformal symmetry, which is manifest in twistor space but hidden in spacetime.

### Twistor String Theory

A major application is **twistor string theory** (Witten, 2004), where scattering amplitudes in Yang-Mills and gravity are computed as correlation functions in a **topological B-model** on $\mathbb{CP}^3 \times \mathbb{CP}^3$:

$$\mathcal{A}_n = \oint \prod_{i=1}^n d^4 Z_i \, \frac{\delta^4(\sum_i Z_i \lambda_i) \text{[correlation function]}}{\text{[Jacobian]}}$$

This formulation makes the holomorphic structure manifest and enables new computational techniques (residue integrals, localization).

### Higher-Dimensional Generalizations

Twistor theory generalizes to higher dimensions by replacing $\mathbb{CP}^3$ with $\mathbb{CP}^{D+1}$ (for D spacetime dimensions). The fibration structure and conformal geometry principles remain unchanged.

---

## Key Results

1. **Twistor space formulation**: Spacetime geometry is reconstructed from the complex geometry of $\mathbb{CP}^3$ (or $\mathbb{CP}^{D+1}$ in higher D).

2. **Null geodesics as $\mathbb{CP}^1$ curves**: Each null ray corresponds to a Riemann sphere in twistor space; conformal rescalings act geometrically as projective transformations.

3. **Holomorphic amplitude structure**: Scattering amplitudes have hidden holomorphic properties that become manifest in twistor momentum space.

4. **MHV amplitudes**: Maximally-helicity-violating amplitudes are determined by spinor variables $\lambda_i$ only, greatly simplifying calculations.

5. **Soft theorems from conformal symmetry**: Ward identities in twistor space directly give soft collinear theorems without additional assumptions.

6. **Gravity from Yang-Mills**: Using gravity twistor string theory, gravitational amplitudes are obtained from Yang-Mills amplitudes via a CHY (Cachazo-He-Yuan) type formula.

7. **Integrability connection**: Self-dual Yang-Mills theory (integrable on-shell) is naturally formulated in twistor space, connecting to integrable systems literature.

8. **Recursion relations**: The BCFW recursion structure is visible as pole residues in twistor momentum space, enabling efficient computational algorithms.

---

## Impact and Legacy

The 2017 lectures consolidated twistor methods as central to modern theoretical physics:

- **Amplitude revolution**: Shifted focus from Feynman diagrams to amplitude-based methods, with 100x+ computational speedups in many cases
- **Soft theorems and asymptotic symmetries**: Connected soft limits to infrared structure and asymptotic symmetries (BMS group for gravity, soft color symmetry for Yang-Mills)
- **Loop integrals**: Extended to loop-level amplitudes via generalized unitarity and double copies
- **Quantum gravity implications**: Suggested that gravity is "double copy" of Yang-Mills, hinting at a unified structure
- **Twistor actions**: Led to new Lagrangian formulations of Yang-Mills and gravity in twistor space (non-local but holomorphic)

---

## Connection to Phonon-Exflation Framework

**Framework-relevant**: The phonon-exflation framework operates on the internal SU(3) manifold with a spectral action principle. Twistor methods are applicable in multiple ways:

1. **Conformal structure of the Dirac operator**: The Dirac operator on curved SU(3) has a conformal weight (dimension 3/2 in 4D). Twistor formalism naturally incorporates conformal scalings of the spectrum.

2. **Null geodesics in internal space**: The "light-like" paths in the SU(3) fiber (instantons connecting different topological sectors) can be understood as null geodesics in an appropriate twistor space of the internal manifold.

3. **Amplitudes for particle interactions**: The phonon-exflation framework predicts particle interactions (scattering amplitudes) from the emergent internal geometry. Twistor methods provide efficient ways to compute these amplitudes.

4. **Spectral action as holomorphic amplitude**: The spectral action $S_{\text{spec}} = \text{Tr}[f(D_K/\Lambda)]$ can potentially be rewritten as a "amplitude" in an internal twistor space, revealing hidden holomorphic structure in the particle spectrum.

5. **Conformal invariance of KK reduction**: When reducing from M4 x SU(3) to 4D, conformal symmetries of the internal space map to asymptotic symmetries of 4D gravity. Twistor formalism makes these mappings explicit.

**Closest connection**: The **conformal structure of internal geometry** and the natural appearance of holomorphic/null geometric structures make twistor theory a powerful tool for analyzing the Dirac spectrum and particle interactions in phonon-exflation.

---

## References

- Adamo, T. (2017). "Lectures on twistor theory." *arXiv* 1712.02196.
- Penrose, R. (1967). "Twistor algebra." *J. Math. Phys.* 8:345.
- Witten, E. (2004). "Perturbative gauge theory as a string theory in twistor space." *Commun. Math. Phys.* 252:189.
- Britto, R., Cachazo, F., Feng, B., Witten, E. (2005). "Direct proof of tree-level recursion relations." *Phys. Rev. Lett.* 94:181602.
