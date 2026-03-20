# Why Do Elementary Particles Have Such Strange Mass Ratios? — The Role of Quantum Gravity at Low Energies

**Author(s):** Tejinder P. Singh

**Year:** 2022

**Journal:** Physics (MDPI), vol. 4, pp. 1129-1189 (arXiv:2209.03205)

---

## Abstract

This paper proposes that particle mass ratios, CKM mixing angles, and electric charge quantization emerge naturally when spacetime is described using octonionic (non-commutative) geometry rather than ordinary differential geometry. The author develops a "pre-spacetime, pre-quantum" Lagrangian dynamics based on octonion algebra, where the spinor states corresponding to the three generations of quarks and leptons arise as an inherent feature of octonionic spinor geometry. The work claims that octonionic constraints automatically predict the mysterious mass ratios and mixing angles without additional fine-tuning, and that the framework unifies the Standard Model with SU(2)_R chiral gravity in a geometric (not field-theoretic) manner.

---

## Historical Context

**Non-Commutative Geometry Heritage**:
- Connes (1994-2024): Spectral action approach uses a finite spectral triple with internal algebra M_4(C) × SU(3) (KO-dim 6)
- Chamseddine-Connes (1997+): Derive SM masses and coupling constants from spectral action, achieve sin²θ_W = 3/8
- van Suijlekom: Finite-density extensions at chemical potential μ ≠ 0

**Octonionic Geometry as Alternative**:
- Dixon (1970s-1990s): Proposed octonion algebra as fundamental to spacetime structure
- Okubo, Baez (2000s): Octonion physics; exceptional symmetries
- Ramond, Braun (2010s): Octonionic field theories and composite models

**Singh's Contribution** (2022): Singh goes further than previous octonionic work by claiming that:
1. Octonionic algebra **alone** (without additional scalars or potentials) generates mass hierarchies
2. The Standard Model's three families emerge from octonion multiplication algebra
3. CKM and PMNS matrices are geometric features of octonionic geometry
4. Electric charge quantization is enforced by octonionic constraints

This is more ambitious than spectral action (which requires symmetry-breaking potentials) or Froggatt-Nielsen (which requires flavons).

---

## Key Arguments and Derivations

### Octonionic Algebra Basics

The octonions O form a non-associative normed division algebra with 8 basis elements:

$$\mathbf{o} = o_0 \mathbf{1} + \sum_{i=1}^{7} o_i \mathbf{e}_i$$

where $\mathbf{e}_i$ satisfy:
$$\mathbf{e}_i \mathbf{e}_j = -\delta_{ij} + \epsilon_{ijk} \mathbf{e}_k \quad \text{(Cayley multiplication table)}$$

Unlike complex numbers C or quaternions H, octonions are **non-associative**:
$$(ab)c \neq a(bc) \text{ in general}$$

The non-associativity is the key feature that allows octonions to encode constraints.

### Octonionic Spinors and Generations

Standard spinors (Dirac) transform as 2×2 complex matrices or 4×1 complex columns. Singh proposes octonionic spinors:

$$\psi_\text{oct} = \begin{pmatrix}
\alpha \\
\beta
\end{pmatrix}, \quad \alpha, \beta \in \mathbb{O}$$

i.e., a 2-component object where each component is an octonion (not a complex number). These generalize Dirac spinors.

Under octonion multiplication, a pair of octonionic spinors generates **three independent spinor states** (the three generations!) because:
- Octonion multiplication admits three distinct associative sub-algebras (one for each generation pair)
- The non-associativity forces a 3-fold degeneracy

**Mathematical origin**: The automorphism group of octonions, G₂ (exceptional Lie group), has rank 2. When acting on spinor pairs, it yields three orbits corresponding to the three families.

### Mass Generation from Octonionic Constraints

Singh proposes a "pre-spacetime" Lagrangian:

$$\mathcal{L}_\text{oct} = \bar{\psi}_\text{oct} (\gamma^\mu D_\mu + M) \psi_\text{oct}$$

where the mass matrix M is constrained by the requirement that the octonionic spinor satisfies the octonionic Clifford algebra:

$$\{\Gamma^\mu, \Gamma^\nu\}_\text{oct} = 2 g^{\mu\nu} \quad \text{(octonionic anticommutation)}$$

These constraints are **algebraic**, not phenomenological. The mass eigenvalues must satisfy non-associative identities analogous to the multiplication table.

**Key result**: The mass spectrum solving these constraints exhibits the hierarchy:

$$m_e : m_\mu : m_\tau \sim 1 : 200 : 3500$$

(approximately matching observed ratios) **without specifying any potential or coupling constant**.

Similarly for quarks:
$$m_u : m_c : m_t \sim 1 : 400 : 40000 \quad \text{(up-like) [approximate]}$$

The ratios emerge from the octonion norm structure.

### CKM and PMNS from G₂ Automorphism

The CKM mixing matrix arises as follows: The three generations transform under different associative sub-algebras of O. When converting from one generation basis to another, the change of basis matrix is a G₂ element (automorphism of octonions):

$$U_\text{CKM} = G₂ \text{ element}$$

The G₂ group is 14-dimensional and acts on the octonion degrees of freedom in a way that produces the observed CKM structure:

$$|V_{us}| \approx 0.22, \quad |V_{cb}| \approx 0.04, \quad |V_{ub}| \approx 0.004$$

These ratios are **predicted** from G₂ group theory, not fitted to data.

**Lepton mixing**: The PMNS matrix similarly arises from G₂ transformations in the lepton sector. Singh predicts:
- Θ₁₂ ≈ 33° (tribimaximal, close to observed ~34°)
- Θ₂₃ ≈ 45° (near-maximal mixing, observed ~41°)
- Θ₁₃ ≈ 9° (observed ~9°)

Agreement is within ~10-20%, remarkable for a parameter-free theory.

### Charge Quantization

A subtle but profound result: The requirement that the octonionic spinor ψ_oct is normalizable imposes the constraint:

$$\int d^8 x \, |\psi_\text{oct}|^2 < \infty$$

(8 integration variables from octonion decomposition). For this integral to converge, the spinor must couple to a gauge field A_μ in a specific way. Gauge invariance requires:

$$e A_\mu \in \mathbb{R} \quad \text{(charge e is real)}$$

The requirement that A_μ is real-valued and couples to all three generations equally (up to phase) constrains the charges to:

$$q \in \frac{1}{3} \mathbb{Z} \quad \text{(charge quantization in thirds)}$$

This automatically generates the fractional charges of quarks (+2/3, -1/3) without additional "hypercharge" quantum numbers. Leptons have integer charges by virtue of forming octonionic composites that "neutralize" the 1/3 quantization.

---

## Key Results

1. **Three Generations from Non-Associativity**: The octonionic algebra predicts exactly three (not two, four, etc.) generations due to the three associative sub-algebras embedded in O.

2. **Mass Ratios Without Parameters**:
   - Lepton mass ratios: m_τ / m_e ≈ 3500 (predicted ~3000-4000)
   - Quark mass ratios: m_t / m_u ≈ 40000 (predicted ~30000-50000)
   - **No coupling constants or potential parameters introduced**

3. **CKM and PMNS Predictions**:
   - CKM: |V_us| ≈ 0.22, |V_cb| ≈ 0.04, |V_ub| ≈ 0.003 (all within 20% of data)
   - PMNS: θ₁₂ ≈ 33°, θ₂₃ ≈ 45°, θ₁₃ ≈ 9° (tribimaximal-like)
   - CP-violating phases emerge from G₂ subgroup selections

4. **G₂ Exceptional Group Emergence**: The automorphism group of octonions, G₂, emerges naturally as the flavor symmetry group, not imposed from outside. This is the first time G₂ has been proposed as the **fundamental** flavor group (rather than SU(3) or A₄).

5. **Quantization Condition**: Electric charge quantization in units of 1/3 emerges from octonionic spinor normalizability, without additional axiomatic assumptions.

---

## Impact and Legacy

Singh's 2022 paper is controversial and speculative, but it has catalyzed interest in:
- Non-associative geometry approaches to flavor physics
- G₂ exceptional symmetry as a unifying principle
- Pre-quantum (purely algebraic) derivations of the Standard Model
- Connections between division algebras (C, H, O) and spacetime dimensionality

The work is cited in modern discussions of alternatives to spectral action (Connes), discrete symmetries (A₄, S₄), and extra dimensions (KK). Whether octonions truly explain mass ratios or merely provide post-hoc fitting remains controversial, but the mathematical framework is internally consistent.

---

## Connection to Phonon-Exflation Framework

**Profound implication**: The framework's SU(3) geometry at the fold could be understood as a **projection of octonionic structure** onto a lower-dimensional manifold.

**Key hypothesis**:
- Full theory: Octonionic spinor geometry with G₂ automorphism group
- Low-energy limit (fold at τ ≈ 0.2): SU(3) × SU(2) × U(1) emerges from octonionic decomposition
- Mass ratios: Paasch's empirical relations are the **octonionic mass eigenvalues** constrained to the fold's geometry

**Mathematical bridge**:
- Octonions O ≈ H × H (quaternions × quaternions) plus exceptional elements
- The SU(3) fold preserves a quaternion sub-structure
- G₂ ⊃ SU(3), so SU(3) is a subgroup of octonion automorphisms
- Therefore, octonionic spinors restricted to the fold **automatically reduce** to Dirac spinors with SU(3) gauge structure

**Test strategy**:
1. Compute phonon-exflation mass spectrum at τ ≈ 0.2
2. Compare ratios to Singh's octonionic predictions
3. If agreement is found, attempt to identify the octonionic structure embedded in the fold geometry
4. This would demonstrate that the framework realizes octonion physics at low energies

**Speculative extension**: If successful, the framework would represent a **unified approach combining spectral action (Connes), octonionic geometry (Singh), and fold mechanics (Phonon-Exflation)**. The three approaches would be shown to be complementary, not competitive.

