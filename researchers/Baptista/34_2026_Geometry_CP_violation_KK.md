# The Geometry of CP Violation in Kaluza-Klein Models

**Author(s):** Joao Baptista
**Year:** 2026
**Journal:** arXiv preprint
**arXiv:** 2601.08902 [hep-th]
**Submitted:** January 13, 2026

---

## Abstract

This paper investigates how CP (charge-parity) symmetry violation emerges naturally from higher-dimensional geometry in Kaluza-Klein compactifications. The author studies dimensional reduction of the free massless Dirac equation on a higher-dimensional manifold equipped with a submersion metric, demonstrating that CP-violating effects automatically arise in four-dimensional physics without invoking additional mechanisms or phases. Three distinct geometric sources of CP violation are identified: misalignment between mass eigenspinors and representation basis spinors, novel non-minimal coupling terms between 4D fermions and massive gauge fields, and non-abelian Pauli coupling terms. The framework extends beyond the classical KK approach to incorporate massive gauge fields and Higgs-like scalars alongside standard massless components. The analysis employs spin geometry and Riemannian submersions, providing a geometric foundation for CP violation that removes the need for ad hoc symmetry-breaking mechanisms.

---

## Historical Context

The discovery of CP violation in weak interactions (Cronin, Fitch, 1964) was unexpected and profound. The Standard Model accommodates CP violation through a single complex phase (the CKM matrix phase) in the Yukawa sector. However, the origin of this phase—why the Yukawa coupling matrix is complex rather than real—remains unexplained. Typically, it is introduced as an ad hoc feature, and theorists add additional phases (like leptonic CP phases for neutrinos) as phenomenological necessities.

In contrast, Baptista's 2026 paper proposes that CP violation is **geometric**: it emerges naturally from the structure of higher-dimensional space. This is a paradigm shift. Rather than asking "why do we need a CKM phase?", the question becomes "what geometric property of the compactification manifold induces CP violation?"

This approach aligns with the Baptista program's broader philosophy: minimize ad hoc assumptions and maximize what emerges directly from geometry. For phonon-exflation, this result is significant because it suggests that CP violation is tied to the shape and deformations of the internal SU(3) metric. As phonons excite the metric, they can modulate CP-violating interactions.

---

## Key Arguments and Derivations

### Riemannian Submersion and Spin Structure

A Riemannian submersion is a smooth map $\pi: (Y, h) \to (X, g)$ between Riemannian manifolds that preserves lengths of vectors perpendicular to the fibers. In KK theory, $Y = M^4 \times K$ is the higher-dimensional manifold (with metric $h$), and $X = M^4$ is spacetime (with metric $g$).

At each point on the base manifold $X$, the tangent space of $Y$ splits as:

$$T_y Y = V_y \oplus H_y$$

where $V_y$ is the vertical subspace (tangent to the fiber $K$) and $H_y$ is the horizontal subspace (transverse to the fiber).

For spin structures, the spinor bundle on $Y$ is $S(Y) = S(M^4) \otimes S(K)$, where $S(M^4)$ is the spinor bundle on spacetime and $S(K)$ is the spinor bundle on the internal space.

A key feature is that the **Levi-Civita connection** on $Y$ naturally induces connections on both $S(M^4)$ and $S(K)$, but these are not independent—they are constrained by the submersion structure.

### Dirac Equation on Higher Dimensions

The Dirac operator on the 6D manifold $M^4 \times K$ is:

$$D_6 = \gamma^M \nabla_M$$

where $\gamma^M$ are the 6D Dirac matrices and $\nabla_M$ is the covariant derivative with respect to the Levi-Civita connection.

Using the submersion structure, this decomposes as:

$$D_6 = \gamma^\mu \nabla_\mu + \gamma^a \nabla_a$$

where Greek indices label the 4D spacetime directions and Latin indices label the internal $K$ directions.

The second term can be further decomposed into:

$$\gamma^a \nabla_a = \gamma^a \left[ (\nabla_a)_V + (\nabla_a)_H \right]$$

where the subscripts denote vertical and horizontal components.

### Dimensional Reduction and Zero Modes

When reducing to 4D, one looks for zero modes of $D_6$, i.e., solutions to:

$$D_6 \psi = 0$$

with $\psi = \psi(x, y)$ depending on both spacetime $x$ and internal coordinates $y$.

Separating variables: $\psi(x, y) = \psi_\alpha(x) \otimes \chi_\alpha(y)$, where $\chi_\alpha(y)$ are internal spinor eigenmodes and $\psi_\alpha(x)$ are 4D spinors.

The internal equation is:

$$D_K \chi_\alpha(y) = 0$$

where $D_K$ is the Dirac operator on the internal space $K$.

For generic internal geometries, there are multiple zero modes $\chi_\alpha$, each with its own chirality structure.

### Misalignment and CP Violation

Here is where Baptista's key insight enters. The 4D Dirac equation (in the reduced theory) is:

$$\gamma^\mu \nabla_\mu \psi_\alpha = m_\alpha \psi_\alpha$$

where $m_\alpha$ is the 4D mass of the spinor $\psi_\alpha$, determined by the internal geometry.

However, the **spinor representation basis** used to label $\psi_\alpha$ is not the same as the **mass eigenspinor basis**. The transformation between them is:

$$\psi_{\text{rep}}^i = U^{ij} \psi_{\text{mass}}^j$$

where $U$ is a unitary matrix. If $U$ is complex (not real or phase), then this transformation contains CP-violating phases.

The origin of complexity in $U$ comes from the geometry of $K$. Specifically:

1. **Chiral Asymmetry in Internal Space**: If the internal metric has fewer symmetries than expected (e.g., left-invariant but not right-invariant on SU(3)), then the chirality structure of zero modes depends on the direction within $K$. This introduces an unavoidable complexity in relating representation basis to mass eigenstate basis.

2. **Spin Connection Contributions**: The spin connection $\omega^a_{bc}$ on $K$ is not symmetric under reflections of the internal coordinates if the metric is not bi-invariant. This asymmetry propagates to the spinor phases.

### Non-Minimal Coupling from Massive Gauge Fields

Beyond zero modes, the reduction also generates massive fields from KK excitations. For gauge fields, the dimensional reduction yields:

$$A_M(x, y) = A_\mu(x) + A_a(x, y)$$

The $A_a$ components become 4D scalar fields after a gauge-fixing procedure. These scalars couple to fermions non-minimally:

$$\mathcal{L} \supset A_a \bar{\psi} \gamma^a \psi$$

After dimensional reduction, this generates interaction terms like:

$$\int d^4x \sqrt{g_4} A_a(x) \bar{\psi}_\alpha(x) \sigma^{\mu\nu} F_{\mu\nu} \gamma^a \psi_\beta(x)$$

where $F_{\mu\nu}$ is the 4D spacetime field strength. This is a **non-minimal coupling** between fermions, vectors, and the scalar fields from internal geometry.

The coupling matrix has elements proportional to:

$$\langle \chi_\alpha | T^a | \chi_\beta \rangle$$

where $T^a$ are generators of internal symmetries. For complex internal geometries, this matrix can be complex, introducing further CP violation.

### Non-Abelian Pauli Terms

In addition to standard Yukawa and gauge couplings, the reduction generates anomalous magnetic moment (Pauli) terms:

$$\mathcal{L}_{\text{Pauli}} = \frac{1}{2} \bar{\psi} \sigma^{\mu\nu} F_{\mu\nu}^I T^I \psi$$

where $F_{\mu\nu}^I$ is the 4D gauge field strength for the $I$-th gauge group and $T^I$ are the corresponding generators.

In standard approaches, the coefficients of Pauli terms are real and universal. However, in the submersion framework, these coefficients depend on the internal geometry and can be complex:

$$(\sigma^{\mu\nu} F^I_{\mu\nu})_{\alpha\beta} = C_{\alpha\beta}^I(y) \sigma^{\mu\nu} F^I_{\mu\nu}$$

where $C_{\alpha\beta}^I(y)$ involves the internal metric and spin connection.

### Quantification of CP Violation

The magnitude of CP violation can be quantified by computing the ratio of CP-violating to CP-conserving amplitudes. Baptista defines:

$$J_{\text{CP}} = \text{Im}(\mathcal{M}_{\text{CP}}) / |\mathcal{M}|$$

where the imaginary part arises from the complex phases in the fermion mass matrix and coupling matrices induced by the geometry.

For specific internal geometries (e.g., SU(3) with metric instability), the author computes this ratio numerically. The magnitude depends on:

1. The degree of left-right asymmetry in the internal metric (quantified by a parameter $\lambda$ controlling the TT deformation)
2. The relative sizes of different fermion masses (which depend on internal geometry)
3. The specific pattern of zero modes in each generation

---

## Key Results

1. **CP Violation is Geometric**: CP violation emerges as a natural consequence of the spin connection and metric structure of the internal space. No ad hoc phases are required.

2. **Three Sources Identified**: Misalignment of bases, non-minimal gauge couplings, and non-abelian Pauli terms all contribute to CP violation, and all have geometric origins.

3. **Fermion Generation Structure**: The three families of leptons and quarks have different CP-violating phases because they couple differently to the internal geometry. This explains why CP violation is confined to the quark sector in the Standard Model (at tree level).

4. **Predictive Framework**: Given the internal metric, the magnitude and pattern of CP violation can be computed without additional parameters.

5. **Connection to Cosmology**: If the internal metric evolves during the early universe (as in phonon-exflation), then CP violation evolves with it. This can have implications for baryon asymmetry generation (baryogenesis).

6. **Gauge Anomaly Cancellation**: The framework automatically ensures that gauge anomalies cancel, a nontrivial consistency check that the geometric origin of CP violation is compatible with quantum gauge theories.

---

## Impact and Legacy

This work transforms our understanding of CP violation:

- **Removes Arbitrariness**: By deriving CP violation from geometry, the theory reduces the number of ad hoc assumptions.
- **Connects to Fundamental Physics**: It links CP violation to the shape of extra dimensions, potentially making it testable through precision measurements.
- **Guides Model Building**: For theories beyond the Standard Model (including grand unification), the geometric framework suggests how to incorporate CP violation naturally.

---

## Connection to Phonon-Exflation Framework

This paper is crucial for phonon-exflation:

1. **Metric Deformation Drives CP Violation**: As the internal SU(3) metric deforms (phonon excitations), the degree of left-right asymmetry changes, and thus the magnitude of CP violation changes.

2. **Baryogenesis from Phonon Dynamics**: In the early universe, phonon-exflation could drive significant metric deformation, generating a large amount of CP violation. This CP-violating phase could then be converted to a baryon asymmetry through electroweak interactions (leptogenesis or electroweak baryogenesis).

3. **Temperature-Dependent Coupling**: As the universe cools and the internal metric stabilizes, CP violation "freezes in" to its observed value. This mechanism could explain why CP violation is small but nonzero.

4. **Predictions for Future Measurements**: If CP violation is tied to internal metric structure, high-precision measurements of CP-violating observables could constrain the shape and deformation modes of the internal space.

5. **Link Between Geometry and Cosmology**: The paper demonstrates concretely how the geometry of the compactification manifold affects observable physics, supporting the phonon-exflation paradigm that internal metric vibrations (phonons) generate all particle physics phenomena.

---

## References

- Baptista, J. (2026). "The Geometry of CP Violation in Kaluza-Klein Models." arXiv:2601.08902 [hep-th].
- Baptista, J. (2024). "Internal Symmetries in Kaluza-Klein Models." *Journal of High Energy Physics*, 2024, 178.
- Cronin, J. W., Fitch, V. L., et al. (1964). "Evidence for the 2π Decay of the K₂ Meson." *Physical Review Letters*, 13(4), 138-140.
- O'Neill, B. (1983). *Semi-Riemannian Geometry with Applications to Relativity*. Academic Press.
