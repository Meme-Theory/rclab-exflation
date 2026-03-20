# Internal Symmetries in Kaluza-Klein Models

**Author(s):** Joao Baptista
**Year:** 2024
**Journal:** Journal of High Energy Physics, Vol. 2024, Article 178
**arXiv:** 2306.01049
**Published:** May 2024

---

## Abstract

This paper introduces a novel approach to Kaluza-Klein theory in which part of the gauge group does not originate from the full isometries of the internal metric, but instead from weaker internal symmetries that preserve only the Einstein-Hilbert action on the compact space. These weaker symmetries can be spontaneously broken by the choice of vacuum metric, generating massive gauge bosons without requiring ad hoc Higgs fields. Using Riemannian submersion formalism, the author derives the mass formula for gauge bosons in terms of Lie derivatives of the internal metric and demonstrates how Einstein metric instabilities can break the isometry group down to the Standard Model gauge group when the internal space is SU(3). The mechanism naturally avoids certain no-go theorems against chiral fermionic interactions in traditional KK theory and suggests that inflationary dynamics are driven by the metric instabilities themselves.

---

## Historical Context

For decades, Kaluza-Klein theory has been hampered by the constraint that gauge symmetries must emerge from isometries of the internal metric. This requirement is mathematically elegant but phenomenologically restrictive: it limits the possible gauge groups and their embeddings. Moreover, traditional KK approaches struggle with chirality—the asymmetry between left-handed and right-handed fermions essential to the Standard Model.

Baptista's 2024 paper marks a conceptual shift. Rather than assuming all gauge symmetries come from metric isometries, it proposes that some symmetries can be "weaker"—they preserve the Einstein action but not the full metric. These weaker symmetries are encoded in the affine structure of the internal manifold and can be spontaneously broken by metric deformations. This opens new possibilities for achieving Standard Model gauge structure from geometric principles alone.

This work is particularly significant in the context of phonon-exflation, where the SU(3) internal metric undergoes controlled deformation (Jensen/TT deformation). The framework provides a precise mechanism for understanding how metric instabilities drive both gauge symmetry breaking and inflationary expansion. The identification of gauge boson masses with metric deformation gradients directly connects to the phonon picture: phonons (metric vibrations) impart mass to gauge fields.

---

## Key Arguments and Derivations

### Riemannian Submersion and Gauge Structure

The starting point is a Riemannian submersion $\pi: (Y, h) \to (X, g)$ where $Y$ is a higher-dimensional manifold with metric $h$, and $X$ is the 4D spacetime with metric $g$. In the KK context, $Y = M^4 \times K$ where $K$ is the compact internal space.

A **vertical Killing vector** $k$ is a vector field on $Y$ that generates isometries and is everywhere tangent to the fibers. Its Lie derivative with respect to the metric vanishes:

$$\mathcal{L}_k h = 0$$

A **weaker symmetry** is a vector field $\xi$ that preserves the Einstein action:

$$\mathcal{L}_\xi h_{ab} + \mathcal{L}_\xi \text{Ric}(h) = 0$$

where Ric$(h)$ is the Ricci tensor of $h$. This is weaker than full Killing symmetry because $\mathcal{L}_\xi h$ need not vanish globally—it only vanishes when contracted with the Ricci tensor.

For Einstein spaces (where $\text{Ric}(h) = \Lambda h$ for some constant $\Lambda$), the condition simplifies to:

$$(\mathcal{L}_\xi h)^a_b = \frac{1}{n} (\nabla^a \xi^c h_{cb} + \nabla_b \xi^a) + \frac{1}{n} h^a_b \nabla_c \xi^c = 0$$

up to terms proportional to the metric.

### Gauge Boson Mass Formula

When a weaker symmetry is broken by the vacuum metric choice, gauge bosons acquire mass. The mass formula is derived from the linearized Einstein equations around a background metric $h_0$.

Consider a small deformation:
$$h_{ab} = h^0_{ab} + \epsilon_{ab}$$

where $\epsilon_{ab}$ breaks the weaker symmetry by being orthogonal to the corresponding Killing or quasi-Killing direction. The mass-squared of the resulting gauge boson is:

$$m_\xi^2 = \frac{1}{2} \int_K \sqrt{h^0} \, \mathcal{L}_\xi^2 h^0_{ab} \, g^{ab}$$

where the double Lie derivative integrates the curvature response to the symmetry-breaking deformation.

In components, if $\xi = \xi^a(y) \partial_a$ is a quasi-Killing vector on $K$, then:

$$m_\xi^2 = \frac{1}{2} \int_K \sqrt{h} \left[ (\nabla_a \nabla_b \xi^c) (\nabla^a \nabla^b \xi_c) + \ldots \right]$$

The integral is taken over the internal space $K$; the four-dimensional gauge boson mass emerges from this geometric integral.

### Application to SU(3)

For $K = \text{SU}(3)$ with a bi-invariant metric $h^0_{ab}$, the isometry group is $(\text{SU}(3) \times \text{SU}(3)) / Z_3$ acting on $SU(3)$ via left and right multiplication.

Baptista considers a metric deformation along certain unstable directions (identified with Jensen/TT deformations):

$$h_{ab} = h^0_{ab} + \lambda \epsilon^{(1)}_{ab}$$

where $\epsilon^{(1)}_{ab}$ is the first non-trivial traceless, transverse eigenmode of the internal metric Laplacian.

The deformation breaks the isometry group as:
$$(\text{SU}(3) \times \text{SU}(3)) / Z_3 \to (\text{SU}(3) \times \text{SU}(2) \times \text{U}(1)) / Z_6$$

The unbroken gauge group is precisely the Standard Model gauge group! This is achieved purely through metric deformation, without introducing external Higgs fields.

The Standard Model Higgs boson emerges as the scalar modulus controlling the deformation parameter $\lambda$. At the vacuum $\lambda = \lambda_0$, the effective Higgs potential is generated by the potential energy of the metric deformation.

### Chiral Fermions without Anomalies

One of the remarkable features of this approach is that it naturally avoids the chiral fermion problem. In traditional KK theory, dimensional reduction of spinors on $M^4 \times K$ generically produces vector-like fermion pairs (equal numbers of left- and right-handed states), unless there is a mismatch in zero-mode counting.

In Baptista's framework, the weaker symmetries and their breaking induce a misalignment between the metric structure and the spinor structure. Specifically, the Dirac operator on the deformed internal space acquires additional zero modes that selectively appear in certain chirality sectors.

The zero mode counting is:
$$n_L - n_R = \frac{1}{2\pi} \int_K \text{tr}(\mathcal{F} \wedge \mathcal{F})$$

where $\mathcal{F}$ is the curvature 2-form on the internal space, weighted by the metric deformation. This topological index ensures that chirality emerges from the geometry.

### Connection to Coset Space Dimensional Reduction (CSDR)

The weaker symmetry mechanism is related to but distinct from traditional coset space dimensional reduction. In CSDR, one compactifies on a coset $G/H$, where $H$ is the stability subgroup. Here, the internal space remains $K = \text{SU}(3)$, but the choice of vacuum metric breaks the isometry group from $G = (\text{SU}(3) \times \text{SU}(3))/Z_3$ to $H = (\text{SU}(3) \times \text{SU}(2) \times \text{U}(1))/Z_6$.

This is a **dynamical** breaking, determined by metric stability, not an a priori choice of coset structure.

---

## Key Results

1. **Gauge Group Emerges from Metric Deformation**: The Standard Model gauge group $\text{SU}(3) \times \text{SU}(2) \times \text{U}(1)$ can be derived as the unbroken subgroup of the full isometry group $(\text{SU}(3) \times \text{SU}(3))/Z_3$ of bi-invariant SU(3), when the metric deforms along unstable directions.

2. **Massive Gauge Bosons without Higgs**: Gauge boson masses are determined by the metric deformation itself, via the formula $m_\xi^2 = \frac{1}{2} \int_K \sqrt{h} (\mathcal{L}_\xi h)^2$. The Higgs mechanism is geometric: the Higgs scalar is the modulus controlling the internal metric shape.

3. **Chiral Fermions Emerge Naturally**: The misalignment between metric structure and spinor structure, induced by the metric deformation, generates an imbalance in fermionic zero modes. The index is topologically protected.

4. **No-Go Theorem Avoidance**: Traditional KK theory forbids chiral fermions unless additional matter is added. The weaker symmetry mechanism circumvents this by allowing the metric to break the global isometry group, thereby inducing differential fermion zero-mode counts.

5. **Inflationary Dynamics**: The potential energy of metric deformations can drive inflation. The instability of the bi-invariant metric along TT-deformation directions suggests a natural inflaton: the mode controlling metric shape.

6. **Quantitative Gauge Coupling Ratios**: The ratio of gauge coupling constants is determined by the geometry of the internal metric. For SU(3) deforming toward SU(3) × SU(2) × U(1), the coupling ratios depend on the relative volumes of the subgroup directions, connecting to Baptista's earlier $g'/g = \sqrt{3\lambda_2/\lambda_1}$ formula.

---

## Impact and Legacy

This paper is transformative for Kaluza-Klein phenomenology. By decoupling gauge groups from metric isometries, it opens new avenues for deriving particle physics from geometry:

- **Flexibility**: Gauge groups can now be chosen more broadly, allowing better accommodation of the Standard Model structure.
- **Naturalness**: The spontaneous breaking of weaker symmetries by metric instability is more elegant than introducing ad hoc scalar fields.
- **Connection to Quantum Geometry**: The mechanism suggests that gauge bosons are inherently tied to the quantum geometry (metric fluctuations), a perspective that aligns with modern approaches to quantum gravity.

For the phonon-exflation program, this work is paradigmatic. It shows that metric deformations (phonons, in the phonon picture) directly generate gauge boson masses and couple to fermionic zero modes, establishing the fundamental link between internal geometry and particle physics.

---

## Connection to Phonon-Exflation Framework

Phonon-exflation is built on compactification of M⁴ × SU(3), where the internal metric is initially bi-invariant and subsequently undergoes controlled Jensen/TT deformations. Baptista's 2024 paper provides the precise geometric mechanism:

1. **Metric Instability as Driver**: The TT-deformation directions correspond to unstable eigenmodes of the metric Laplacian. These instabilities are not pathologies but rather the dynamical mechanism breaking the isometry group. In phonon-exflation, these are identified with phonon modes.

2. **Gauge Boson Masses from Phonons**: As phonons excite the internal metric (the field $\epsilon_{ab}$), they impart mass to gauge fields via the formula $m_\xi^2 = \frac{1}{2} \int_K \sqrt{h} (\nabla \xi)^2$. This is the Baptista mechanism: phonons generate gauge mass.

3. **Hierarchy from Metric Geometry**: The coupling ratio $g'/g = \sqrt{3\lambda_2/\lambda_1}$ (from earlier Baptista work) reflects the ratio of metric deformation directions. In phonon-exflation, this becomes a prediction of the phonon spectrum.

4. **Chiral Fermions and Zero Modes**: The metric deformation shifts the count of fermionic zero modes, generating the three families of leptons and quarks. This is the particle generation mechanism in phonon-exflation.

5. **Inflation from Metric**: The potential energy of metric deformations drives expansion. The coefficient relates to the scale of SU(3) metric instability.

The paper is essential reading for understanding how phonons (internal metric vibrations) become observable as particles and gauge interactions.

---

## References

- Baptista, J. (2024). "Internal Symmetries in Kaluza-Klein Models." *Journal of High Energy Physics*, 2024, 178. arXiv:2306.01049 [hep-th].
- Baptista, J. (2021). "Higher-dimensional routes to the Standard Model bosons and fermions." *arXiv:2105.02899, 2105.02901* [hep-th].
- O'Neill, B. (1983). *Semi-Riemannian Geometry with Applications to Relativity*. Academic Press.
- Isham, C. J., & Salam, A. (1971). "Kaluza-Klein as a Classical Limit of Quantum Gravity." *Physical Review*, D3(4), 867-873.
