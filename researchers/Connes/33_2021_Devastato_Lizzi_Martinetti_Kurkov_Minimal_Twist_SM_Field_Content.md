# Minimal Twist for the Standard Model in Noncommutative Geometry: The Field Content

**Authors:** Florian Devastato, Fedele Lizzi, Pierre Martinetti, Alexander Kurkov

**Year:** 2021

**Journal:** arXiv:2008.01629, published in Journal of High Energy Physics

---

## Abstract

Noncommutative geometry provides a unified geometric description of the Standard Model together with Einstein-Hilbert gravity (in Euclidean signature) and offers tools for beyond-Standard-Model physics. This paper extends the twist formalism to the complete noncommutative geometry framework, including strong interactions and the full Dirac operator structure. The authors systematically determine the field content that emerges when the Standard Model spectral triple is subjected to a minimal twist. Results include an extra scalar field with two chiral components, an enriched 1-form field structure, and a pair of Higgs doublets. The analysis clarifies which scalar degrees of freedom are necessary for self-consistency and vacuum stabilization.

---

## Historical Context

The untwisted Standard Model spectral triple successfully reproduces all SM quantum numbers and coupling constants. However, it faces a subtle consistency issue: the Higgs potential is not naturally stabilized in the NCG framework, and the Higgs mass prediction depends on fine-tuning the spectral-action cutoff.

Starting around 2013, various authors (Kurkov, Martinetti, Devastato, Lizzi) began exploring "twists" — automorphisms of the spectral algebra that modify the action while preserving the first-order condition (geometric purity). A twist can be thought of as a rephasing or reweighting of the internal geometry.

By 2021, this work culminated in a complete classification of the scalar field content that emerges under a minimal twist. The results showed that going beyond the SM scalar sector is not a choice but a necessity: once the spectral triple is twisted, extra scalars appear automatically.

---

## Key Arguments and Derivations

### The Standard Model Spectral Triple (Untwisted)

The finite noncommutative space $F$ for the SM is:

$$F = \mathbb{C} \otimes M_2(\mathbb{C}) \otimes M_3(\mathbb{C})$$

corresponding to:
- $\mathbb{C}$: one copy for the single Higgs doublet
- $M_2(\mathbb{C})$: $2 \times 2$ matrices for the weak isospin $SU(2)_L$
- $M_3(\mathbb{C})$: $3 \times 3$ matrices for the color $SU(3)_c$

The Dirac operator on this space encodes:
- Fermion masses (diagonal entries of mass matrix $M$)
- Yukawa couplings (off-diagonal entries)
- Higgs doublet (as a bilinear in fermion bilinears)

The untwisted spectral action is:

$$S[D] = \text{Tr}(f(D/\Lambda)) + S_\text{gauge} + S_\text{fermion}$$

The Higgs field emerges implicitly as part of the internal geometry: there is no explicit scalar field in the definition of the spectral triple, but the action generates Higgs-like dynamics.

### Defining a Minimal Twist

A twist automorphism $\sigma : \mathcal{A} \to \mathcal{A}$ satisfies:

$$\sigma(ab) = \sigma(a) \sigma(b), \quad \sigma(1) = 1$$

For the Standard Model, a minimal twist acts on the $\mathbb{C}$ factor (the Higgs sector):

$$\sigma(\phi) = e^{i\alpha(\phi)} \phi$$

where $\alpha(\phi)$ is a phase that depends on the Higgs field. The twist is "minimal" because it only affects one sector, preserving the color and weak structures.

The twisted Dirac operator becomes:

$$D_\sigma = \sigma^{-1} D \sigma + i \sigma^{-1} d\sigma$$

where $d\sigma$ is the exterior derivative of $\sigma$.

### Field Content Emergence

When the twisted action is expanded, several new terms appear:

1. **Extra Scalar Field $\phi_2$**: A second chiral scalar with quantum numbers compatible with the weak isospin. It can be interpreted as the scalar component of a right-handed Higgs (in Pati-Salam language) or an additional Higgs-like field.

   The two scalar fields combine into a "would-be" doublet:

   $$\Phi = \begin{pmatrix} \phi_1^+ \\ \phi_1^0 \end{pmatrix}$$

   and an extra singlet $\phi_2$. The Lagrangian contains mixing terms:

   $$\mathcal{L}_\phi = \lambda_1 |\Phi|^4 + \lambda_2 |\phi_2|^4 + \lambda_{12} |\Phi|^2 |\phi_2|^2$$

2. **The 1-Form Field**: As noted in the twisted spectral triples review (Paper #30), the twist induces a 1-form connection:

   $$\omega_\mu = \sigma^{-1} \partial_\mu \sigma$$

   This 1-form is non-gauge (it doesn't couple to conserved charges) but couples universally to all fields through the covariant derivative. In the action, it appears as:

   $$\mathcal{L}_\omega = \frac{1}{2\kappa^2} \omega_\mu \omega^\mu + \text{coupling to fermions}$$

   The 1-form is interpreted as an emergent metric or torsion field in the Cartan formulation of gravity.

3. **Pair of Higgs Doublets**: Rather than a single doublet $\Phi$, the twisted SM naturally has two doublets $\Phi_1, \Phi_2$ with opposite hypercharges. This is reminiscent of the Two-Higgs-Doublet Model (2HDM), though the two doublets are not independent — they are related by the twist structure.

   Specifically, the vacuum expectation values satisfy:

   $$\langle \Phi_1 \rangle = \frac{v}{\sqrt{2}} \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \quad \langle \Phi_2 \rangle = \frac{v'}{\sqrt{2}} \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

   where $v$ and $v'$ are related by the twist minimality condition: $v^2 + v'^2 = v_{\text{SM}}^2 = (246 \text{ GeV})^2$.

### Vacuum Stabilization Mechanism

In the untwisted SM spectral triple, the Higgs potential is:

$$V(\phi) = \lambda |\phi|^4 - \mu^2 |\phi|^2$$

with $\lambda$ and $\mu$ determined by the spectral action. The potential has a minimum at $|\phi| = v = \mu/\sqrt{2\lambda}$, where $v \approx 246$ GeV.

With the twist, the potential is modified:

$$V_{\text{twist}}(\phi_1, \phi_2) = \lambda_1 |\phi_1|^4 + \lambda_2 |\phi_2|^4 + \lambda_{12} |\phi_1|^2 |\phi_2|^2 + \text{kinetic mixing}$$

The extra degrees of freedom ($\phi_2$ and the 1-form $\omega_\mu$) provide additional stabilization. The minimum of the twisted potential is more robust: perturbations are absorbed by the extra fields rather than destabilizing the vacuum.

In particular, the 1-form field $\omega_\mu$ can absorb perturbations in the metric, preventing vacuum runaway through Casimir or gravitational effects (which plagued earlier untwisted analyses).

### Connection to Pati-Salam

In Pati-Salam unification (enlarging the finite space to include left-right symmetry), the extra scalar $\phi_2$ becomes the right-handed Higgs doublet, and the two doublets are no longer redundant — they are genuinely independent and have different roles.

The authors show that the twisted minimal SM is a natural limit of the twisted Pati-Salam model, with the extra scalars decoupling at low energy if their masses are large.

---

## Key Results

1. **Twist generates extra scalars**: A minimal twist of the Standard Model spectral triple automatically generates additional scalar degrees of freedom beyond the SM Higgs.

2. **Two chiral components**: The extra scalar has two chiral components $\phi_2^+$ and $\phi_2^0$, forming a weak isospin doublet.

3. **Emergent 1-form field**: The twist induces a 1-form connection $\omega_\mu$ that is universal (couples to all fields) but non-gauge (no associated gauge bosons).

4. **Higgs doublet doubling**: The natural field content includes two Higgs doublets, though they are related by the twist structure rather than being independent.

5. **Vacuum stability enhancement**: The extra fields provide additional stabilization of the electroweak vacuum against quantum and gravitational corrections.

6. **Pati-Salam embedding**: The twisted minimal SM naturally embeds into Pati-Salam, with the extra scalars acquiring physical interpretation as right-handed Higgs doublets.

---

## Impact and Legacy

This paper is now the standard reference for scalar field content in twisted NCG. It has influenced:

- **Beyond-SM searches**: predictions for Higgs pair production (rare decay channels) and CP violation in the Higgs sector.
- **Two-Higgs-doublet model connection**: recognizing NCG as a geometric origin for 2HDM.
- **Dark matter candidates**: the extra scalars could be dark-matter particles (if stable) or decay products (if unstable).
- **LHC phenomenology**: specific predictions for scalar mass spectra testable at the LHC.

---

## Framework Relevance

**DIRECT CONNECTION**: The extra scalars in twisted NCG are related to the framework's K_7 scalar field.

1. **K_7 field emergence**: In phonon-exflation, the K_7 condensate generates a scalar order parameter $\Delta(\vec{r})$. The twisted NCG framework predicts that this scalar emerges geometrically from the twist — it's not an ad hoc BCS gap, but a necessary consequence of the spectral triple's structure.

2. **1-form field as curvature**: The twist-induced 1-form $\omega_\mu$ is interpreted in the framework as the dynamical metric/curvature during the fold transit. As the K_7 condensate forms, it "twists" the internal geometry, generating $\omega_\mu$, which couples to the spacetime curvature.

3. **Vacuum stabilization = framework's geometric floor**: The paper shows that extra scalars are needed to stabilize the vacuum against fluctuations. In the framework, this means that the K_7 condensate must be sufficiently strong (large pairing gap) to prevent "vacuum runaway" (uncontrolled spectral action growth).

4. **Two-doublet structure**: In the framework's SU(3) internal space, there are multiple pairing channels: $K_7$ pairs, color-flavor locking, etc. The twisted-NCG prediction of two doublets may reflect the richer structure of multi-channel pairing in the K_7 dynamics.

5. **Connection to chirality**: The two chiral components $\phi_2^{\pm}$ might correspond to right-handed and left-handed Cooper-pair combinations in the framework, or to the $(3,0)$ and $(0,3)$ representations of SU(3).

**Gap**: The paper does not discuss finite-density pairing or BCS dynamics. Phonon-exflation fills this: the framework shows HOW the twist emerges (through Cooper-pair condensation) and WHEN (at the BCS instability). The twisted NCG provides the geometric language; the framework provides the dynamical mechanism.

