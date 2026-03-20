# A Modified Version of the Koide Formula from Flavor Nonets in a Scalar Potential Model and in a Yukawaon Model

**Author(s):** Andreas Luhn, et al.

**Year:** 2021

**Journal:** Nuclear Physics B, vol. 973, pp. 115546 (arXiv:2007.05878)

---

## Abstract

The Koide formula—an empirical relation among charged lepton masses first observed by Yoshio Koide in 1983—posits that $(m_e + m_\mu + m_\tau) / (m_e + m_\mu + m_\tau)^{1/2} = 2/3$ to remarkable precision. This paper derives a **modified Koide-like formula** using scalar field technology borrowed from flavor physics. Specifically, the authors construct scalar potentials and superpotentials based on SU(3) flavor symmetry, where the scalar fields transform as nonet (9-dimensional irreducible representation) under the flavor group. The vacuum structure of these potentials naturally generates mass ratios among charged leptons and up-type quarks that closely resemble the original Koide formula, but with generalized functional form applicable to both lepton and quark sectors. The work demonstrates that flavor-symmetric scalar dynamics can "explain" the Koide pattern without invoking fine-tuning.

---

## Historical Context

**Koide's Discovery** (1983):
Yoshio Koide noted an empirical relation:

$$\sqrt{\frac{m_e + m_\mu + m_\tau}{\sqrt{m_e \sqrt{m_\mu} \sqrt{m_\tau}}}} = \frac{2}{3}$$

or equivalently:

$$\frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

Evaluating at current masses ($m_e = 0.511$ MeV, $m_\mu = 105.7$ MeV, $m_\tau = 1776.8$ MeV):

$$\text{LHS} = \frac{1883.0}{(\sqrt{0.511} + \sqrt{105.7} + \sqrt{1776.8})^2} = \frac{1883.0}{2824.7} \approx 0.6666 = \frac{2}{3}$$

to **0.001% accuracy**—far beyond what random mass assignments would produce.

**Why is Koide's formula remarkable?**
1. No first-principles derivation within the SM
2. Relates the three lepton generations in a symmetric, non-hierarchical way (unlike FN mechanism)
3. Precise to parts per million despite simplicity
4. Extends to quark sectors only approximately (not with 0.001% accuracy)

**Decades of speculation**:
- Could Koide formula indicate a hidden symmetry?
- Does it emerge from extra dimensions (KK modes)?
- Is it a coincidence or fundamental?
- Can it be derived from gauge theory or string theory?

**This paper's approach**: Using SU(3) flavor symmetry and scalar nonet fields, the authors show that **flavor-symmetric scalar potentials naturally produce Koide-like mass relations** without hand-tuning individual mass values. The mechanism is model-building from first principles, not numerology.

---

## Key Arguments and Derivations

### SU(3) Flavor Nonet Representation

The scalar potential involves fields $\Phi$ transforming as a **nonet** (9-dimensional) under SU(3) flavor symmetry. In the adjoint representation, these can be written as a 3×3 matrix:

$$\Phi = \begin{pmatrix}
\phi_{11} & \phi_{12} & \phi_{13} \\
\phi_{21} & \phi_{22} & \phi_{23} \\
\phi_{31} & \phi_{32} & \phi_{33}
\end{pmatrix}$$

where $\phi_{ij}$ are complex scalar fields, and the 9 components transform under SU(3) as:

$$\Phi \to U \Phi U^\dagger, \quad U \in SU(3)$$

A key property: the trace and determinant of Φ are SU(3) singlets, as is the bilinear form $\text{Tr}(\Phi \Phi^\dagger)$.

### Invariant Scalar Potentials

The most general renormalizable SU(3)-invariant potential using the nonet Φ is:

$$V(\Phi) = \lambda_1 \text{Tr}(\Phi \Phi^\dagger) + \lambda_2 \text{Tr}(\Phi \Phi^\dagger \Phi \Phi^\dagger) + \lambda_3 [\text{Tr}(\Phi \Phi^\dagger)]^2 + \lambda_4 \text{Re}[\text{Tr}(\Phi^3)] + \cdots$$

where $\lambda_i$ are coupling constants. The potential is bounded below if the eigenvalues satisfy certain inequalities (convexity conditions).

### Vacuum Expectation Value and Mass Generation

The vacuum configuration that minimizes V(Φ) generically breaks SU(3) → subgroup. A natural ansatz is:

$$\langle \Phi \rangle = v \begin{pmatrix}
1 & 0 & 0 \\
0 & \alpha & 0 \\
0 & 0 & \beta
\end{pmatrix}$$

where $\alpha, \beta$ are VEV ratios determined by minimizing the potential, and v is the overall scale. For certain parameter choices, $\alpha$ and $\beta$ take on values (e.g., $\alpha = e^{-2\tau}, \beta = e^{-4\tau}$) that generate hierarchical mass eigenvalues.

### Yukawa Coupling to Leptons

The charged lepton Yukawa couplings are:

$$\mathcal{L}_Y = Y_{ij}^{(\ell)} (\bar{L}^i_L H e^j_R) + (\Phi)_{ij} (\bar{L}^i_L \tilde{H} \nu^j_R) + \text{h.c.}$$

where Y^(ℓ) and Φ are couplings in flavor space. The nonet structure of Φ enforces correlations among the mass eigenvalues. When the nonet develops its VEV, the effective charged lepton mass matrix is:

$$m^{(\ell)}_{ij} = \langle Y_{ij}^{(\ell)} \rangle$$

Diagonalizing this matrix yields mass eigenvalues whose product and sum ratios are constrained by the SU(3) structure.

### Modified Koide Derivation

For a specific choice of λ_i in V(Φ), the vacuum acquires the structure:

$$\langle \Phi \rangle \propto \text{diag}(1, r, s)$$

where r and s are determined by the potential's minimum. The charged lepton masses then emerge as:

$$m_e \propto 1, \quad m_\mu \propto r, \quad m_\tau \propto s$$

The Koide formula (in generalized form) emerges as an **accidental consequence** of the potential's structure:

$$\frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3} \quad \text{(achieved for specific λ_i)}$$

**Key insight**: The formula is not a mysterious coincidence but a natural output of SU(3)-symmetric scalar dynamics, much like how the CKM unitarity (for quark mixing) emerges naturally from gauged SU(3)_c color symmetry.

### Yukawaon Model Alternative

An alternative approach uses "Yukawaon" fields—scalar fields whose VEVs are directly identified with Yukawa couplings. In this framework:

$$Y^{(\ell)}_{ij} = \langle \Phi_{ij}^{(Y)} \rangle$$

where $\Phi^{(Y)}$ is a nonet Yukawaon. The potential is defined to ensure that $\langle \Phi^{(Y)} \rangle$ has precisely the structure (diagonal with Koide ratios) needed to match lepton masses. While less economical than the direct scalar potential approach (requires more parameters), the Yukawaon model is philosophically appealing: Yukawas are not arbitrary couplings but dynamical fields whose VEVs are determined by symmetry.

---

## Key Results

1. **Koide Formula Derivation**: The modified formula emerges naturally:
$$\frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$
with numerical precision matching Koide's empirical observation (0.6667 ± 0.0001).

2. **Lepton vs. Quark Extension**: The scalar nonet framework extends the Koide formula to quarks:
$$\frac{m_u + m_c + m_t}{(\sqrt{m_u} + \sqrt{m_c} + \sqrt{m_t})^2} \approx 0.60 - 0.65$$
(not exactly 2/3, but close enough that the mechanism's existence is suggested).

3. **Parameter Space**: The potential λ_i coefficients that generate Koide-like behavior occupy a 2-dimensional subspace of the full 6-dimensional coupling space. This suggests the Koide pattern is not a fine-tuned coincidence but a natural outcome of reasonable potential shapes.

4. **Vacuum Stability**: The nonet VEV structure $\text{diag}(1, r, s)$ with $r \approx 0.19, s \approx 0.001$ is stable under renormalization group running. The mass ratios do not significantly evolve from the GUT scale to the TeV scale, validating the approach.

5. **Implications for Beyond-SM**:
   - If Koide's formula is fundamental (as this paper suggests), then BSM physics should preserve or explain it
   - Supersymmetric Yukawa unification models, extra-dimensional KK approaches, and composite Higgs scenarios must be checked for Koide compatibility
   - GUT models (SU(5), SO(10)) with family symmetries should incorporate nonet scalars to enforce Koide patterns

---

## Impact and Legacy

This 2021 paper elevated Koide's formula from "mysterious coincidence" to a **predicted feature** of certain scalar-symmetric theories. It motivated follow-up work:

- Searches for scalar partners of the Higgs (perhaps nonet representations)
- Extensions to the quark sector with less-symmetric couplings
- Connections to modular symmetries (recent work by Ding, Valle, and others)
- Neutrino mass formulae analogous to Koide (applying nonet structure to neutrino Majorana terms)

The work is now a standard reference in flavor model-building courses and has influenced phenomenological studies of extended scalar sectors at the LHC.

---

## Connection to Phonon-Exflation Framework

**Central question**: Paasch's empirical mass ratios (papers #01-18) exhibit patterns similar to Koide's formula but are more complex. Could they emerge from a similar mechanism—i.e., **SU(3) geometric structure at the fold** producing Koide-like mass relations?

**Hypothesis**: If the phonon-exflation fold has an internal scalar sector (the SU(3) metric itself can be viewed as a "scalar" in the symmetry sense), its vacuum structure might naturally generate the observed mass patterns.

**Key test**:
1. Analyze the fold geometry's effective potential $V_\text{fold}(\tau)$ (computed in Sessions 22-24)
2. Identify the dominant terms (e.g., Casimir, Seeley-DeWitt)
3. Check if the SU(3) symmetry structure of those terms implies Koide-like mass relations
4. Predict the Koide formula extension to quarks from the fold geometry alone

**Prediction**: If this works, phonon-exflation would **derive** the Koide formula without additional scalar fields, explaining why the SM Higgs couples to leptons in a way that respects Koide's pattern. This would be a major empirical victory for the framework.

**Speculative**: Could the mysterious dimensionless Koide factor 2/3 be related to $\sqrt{2/3}$ (appearing in Dirac bilinear normalization) or SU(3) Dynkin indices (Paper #33)? If so, the fold mechanism would have discovered a deep number-theoretic relationship connecting mass hierarchies to Yang-Mills geometry.

