# Beyond the Spectral Standard Model: Emergence of Pati-Salam Unification

**Author(s):** Chamseddine, Connes, van Suijlekom
**Year:** 2013
**Journal:** Journal of High Energy Physics, Vol. 1311, p. 132, arXiv:1304.8050

---

## Abstract

We explore noncommutative geometry models that extend beyond the Standard Model by relaxing the first-order condition on the Dirac operator of the spectral triple. This relaxation naturally leads to larger gauge groups and produces the Pati-Salam unified model with gauge group $SU(4)_C \times SU(2)_L \times SU(2)_R$. We analyze the symmetry breaking pattern, the unification scale, and the predictions for fermion masses and mixings.

---

## Historical Context

The spectral action principle, by 2010-2012, had successfully reconstructed the Standard Model from noncommutative geometry. However, this reconstruction was achieved by imposing a **first-order condition**:

$$D \text{ is of first order in } \nabla$$

This condition ensures that the Dirac operator is a differential operator (acting as $\partial + A$ where $A$ is a gauge field), not a higher-order pseudodifferential operator. Mathematically, the condition is powerful—it selects a unique minimal model. Physically, however, it seemed somewhat arbitrary.

Chamseddine, Connes, and van Suijlekom asked: **What if we relax this condition?** The answer was remarkable: a larger class of models becomes available, including grand unified theories that naturally incorporate the Standard Model.

The most elegant outcome is **Pati-Salam unification**, where quarks and leptons are unified into a single representation via an extended color (SU(4) instead of SU(3)), and left-right symmetry is explicitly implemented.

For phonon-exflation, this is relevant because the framework might naturally extend to Pati-Salam if the SU(3) fiber is generalized to SU(4), opening new physics channels (e.g., right-handed W bosons, leptoquarks) that could affect cosmological predictions.

---

## Key Arguments and Derivations

### The First-Order Condition and Its Relaxation

In the standard spectral triple formulation, the Dirac operator $D$ on the finite geometry is a differential operator:

$$D: A_F \to A_F$$

where $A_F$ is the algebra of the finite space. The first-order condition demands:

$$[[D, a], b] = 0 \quad \forall a, b \in A_F$$

This ensures that the commutator $[D, a]$ (which encodes gauge fields via $A = [D, \cdot]$) closes algebraically, producing a consistent gauge theory.

Relaxing this condition means allowing:

$$[[D, a], b] \neq 0$$

for some $a, b$. Geometrically, this permits **higher-order differential geometry** (curvature tensors beyond the connection) to couple to the Dirac operator.

Algebraically, it opens the possibility of larger gauge algebras and more complex fermion representations.

### The Pati-Salam Algebra

The finite algebra for Pati-Salam unification is:

$$A_{\text{PS}} = \mathbb{C} \oplus \mathbb{H}_L \oplus \mathbb{H}_R \oplus M_4(\mathbb{C})$$

where:
- $\mathbb{C}$: Higgs sector (scalar, generation-independent)
- $\mathbb{H}_L$: Left-handed weak isospin (quaternions)
- $\mathbb{H}_R$: Right-handed weak isospin (quaternions, broken at high scale)
- $M_4(\mathbb{C})$: **Extended color** (4×4 matrices, instead of SM's 3×3)

The extra dimension in the color sector allows leptons to appear as a "fourth color." Explicitly:

$$\text{Quarks} = (r, g, b, \text{lepton}) \quad \text{in } SU(4)_C$$

The gauge group decomposes hierarchically:

$$SU(4)_C \times SU(2)_L \times SU(2)_R \stackrel{M_X}{\longrightarrow} SU(3)_C \times SU(2)_L \times U(1)_R \stackrel{M_Z}{\longrightarrow} SU(3)_C \times U(1)_{\text{EM}}$$

where:
- $M_X \sim 10^{14}$--$10^{16}$ GeV: Pati-Salam breaking scale (GUT-like)
- $M_Z \approx 91$ GeV: Electroweak scale

### The Dirac Operator on Pati-Salam Geometry

The finite Dirac operator encodes all Yukawa couplings:

$$D_F = \begin{pmatrix} 0 & Y_e^{\dagger} & Y_d^{\dagger} & Y_\nu^{\dagger} \\ Y_e & 0 & 0 & M_{\text{R,e}} \\ Y_d & 0 & 0 & M_{\text{R,d}} \\ Y_\nu & 0 & 0 & M_{\text{R,\nu}} \end{pmatrix}$$

where:
- Upper-left block ($0$): Left-handed fermion kinetic energy
- Off-diagonal ($Y_{e,d,\nu}$): Yukawa couplings linking left-handed doublets to right-handed singlets
- Lower-right diagonal ($M_R$): Majorana masses for right-handed fermions (emerge from spectral action)

The right-handed sectors couple via $\mathbb{H}_R$, allowing $W_R$ bosons and $Z_R$ bosons to mediate their interactions.

### Symmetry Breaking Pattern

**Stage 1**: $SU(4)_C \times SU(2)_L \times SU(2)_R \to SU(3)_C \times SU(2)_L \times U(1)_R$ (scale $M_X$)

A scalar field $\Phi_{(1,2,2)}$ (transforming as $(1, 2, 2)$ under the gauge group) acquires a VEV:

$$\langle \Phi_{(1,2,2)} \rangle = v_R \begin{pmatrix} 0 \\ 1 \end{pmatrix}_R$$

This breaks SU(4) to SU(3) (via Higgs mechanism on the 4th color) and breaks $SU(2)_R$ to $U(1)_R$ (via ordinary doublet mechanism).

**Stage 2**: $SU(3)_C \times SU(2)_L \times U(1)_R \to SU(3)_C \times U(1)_{\text{EM}}$ (scale $M_Z$)

The standard electroweak Higgs doublet $H$ acquires VEV $v = 246$ GeV, breaking $SU(2)_L$ and mixing $W_R$ with the $Z_R$ boson to produce the observed $Z$ boson.

---

## Key Predictions

### Grand Unification Scale

The running of gauge couplings in Pati-Salam predicts unification at:

$$\alpha_1(M_X) = \alpha_2(M_X) = \alpha_4(M_X) \quad \text{where } M_X \sim 10^{14.5} \text{ GeV}$$

(refined from early GUT estimates using beta function corrections).

### Proton Decay

The unification enables baryon number violation. Leptoquarks (which couple quarks to leptons) mediate proton decay:

$$p \to e^+ \pi^0, \quad \tau_p \sim 10^{34}--10^{35} \text{ years}$$

Current Super-Kamiokande limits: $\tau_p > 1.6 \times 10^{34}$ yr (still consistent).

### Neutrino Masses

Right-handed neutrino Majorana masses $M_R \sim 10^{13}$--$10^{15}$ GeV produce light left-handed neutrino masses via seesaw:

$$m_\nu = \frac{m_D^2}{M_R} \sim 0.01 \text{ eV}$$

consistent with oscillation data.

### Right-Handed W and Z Bosons

At the Pati-Salam scale, manifest left-right symmetry predicts $W_R$ and $Z_R$ bosons with masses:

$$M_{W_R}, M_{Z_R} \sim M_X \sim 10^{14}$--$10^{16}$ GeV$$

These are outside direct LHC reach but could produce signatures via precision electroweak tests or rare decays (e.g., $K_L \to \mu e$).

---

## Key Results

1. **First-Order Condition Relaxation is Consistent**: Relaxing the first-order condition does not destroy the mathematical coherence of the spectral triple framework. Instead, it opens a richer model space.

2. **Pati-Salam Emerges Naturally**: Without imposing Pati-Salam by hand, it arises as the minimal extension of the spectral SM consistent with left-right symmetry and fermion unification.

3. **Grand Unification Encoded in Geometry**: The GUT scale $M_X \sim 10^{14.5}$ GeV is a prediction of the spectral action, not a free parameter.

4. **Higgs Sector Enriched**: Pati-Salam introduces additional Higgs scalars beyond the SM doublet, with predictions for their masses and couplings.

5. **All SM Physics Recovered**: At low energies, Pati-Salam breaks down to the SM, recovering all known particles and interactions with correct couplings and mixings.

---

## Impact and Legacy

Chamseddine, Connes, and van Suijlekom's 2013 paper demonstrated that noncommutative geometry, rather than being locked into the Standard Model, could naturally produce GUT-like unification. This elevated NCG from a reformulation of known physics to a framework making genuine new predictions.

Subsequent work:
- **Marcolli et al.** (2014+): Computed cosmological implications of Pati-Salam NCG.
- **Chamseddine-Connes** (2015+): Explored SO(10) and other GUT extensions via NCG.
- **van Suijlekom** (2019+): Integrated Pati-Salam into the finite-density formalism.

Pati-Salam NCG remains an active area, with ongoing refinements to predictions for proton decay and the $W_R / Z_R$ mass scale.

---

## Framework Relevance

**Potential Extension Path**: The phonon-exflation framework currently operates within SU(3)×SU(2)×U(1) (Standard Model gauge structure on the 4D side, SU(3) flavor on the internal side). Chamseddine-Connes-van Suijlekom's Pati-Salam framework offers a natural generalization:

1. **Extended Color Sector**: If the SU(3) fiber is generalized to SU(4), the framework could incorporate leptoquarks and manifest left-right symmetry, opening new pairing channels (e.g., lepton-quark Cooper pairs).

2. **Right-Handed Neutrinos**: Pati-Salam naturally includes right-handed neutrinos with Majorana masses. The framework's mass generation mechanism could extend to predict the neutrino mass scale.

3. **Cosmological Implications**: Left-right symmetry breaking at $M_X$ could introduce new phase transitions in the framework's cosmological evolution, affecting predictions for inflation and dark energy.

4. **Grand Unification at the Fiber Level**: Just as Pati-Salam unifies quarks and leptons in 4D, the framework's internal geometry could unify different sectors of the SU(3) fiber, providing a deeper symmetry justification.

**Status**: EXPLORATORY. Pati-Salam NCG is a natural next step if the framework is generalized beyond the SM. However, full integration requires explicit calculations of the spectral action on SU(4) and verification that the finite-density formalism (Paper #32) can accommodate the extended gauge structure.

**Current Limitation**: The framework's mass predictions and cosmological evolution have not been computed in the Pati-Salam setting. This remains an open opportunity for extending the framework's predictive power.
