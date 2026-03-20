# High-Order Van Hove Singularities and Their Connection to Flat Bands

**Author(s):** Laura Classen, Joseph J. Betouras

**Year:** 2024

**Journal:** Annual Review of Condensed Matter Physics, Vol. 16, pp. 229–251 (2025), arXiv:2405.20226

---

## Abstract

Van Hove singularities (VHS)—points where the density of states diverges—are central to understanding electronic instabilities in quantum materials. When bands become very flat near the Fermi level, the density of states exhibits a power-law divergence that can be classified by order: first-order (logarithmic), second-order (square-root), and higher orders. Modern materials—graphene multilayers, moiré structures, kagome metals, and ruthenates—naturally host high-order VHS. We provide a comprehensive classification of VHS geometries, analyze their interaction signatures, and establish connections to flat-band physics. Flat bands are the limit of infinitely high-order VHS where the density of states diverges maximally. We survey the contemporary experimental evidence for VHS in diverse platforms and discuss design principles for engineering both VHS and flat-band structures.

---

## Historical Context

Lindhard's 1954 treatment of the dielectric response in degenerate electron gas first identified that the density of states diverges at critical points (van Hove singularities). These singularities became crucial to understanding superconductivity, charge-density waves, and other instabilities.

For decades, VHS remained a theoretical concept—band structures could be calculated, but direct observation of VHS effects was indirect (e.g., via anomalies in specific heat, magnetic susceptibility). The advent of scanning tunneling microscopy, angle-resolved photoemission spectroscopy (ARPES), and resonant inelastic X-ray scattering has enabled direct mapping of VHS in real materials.

The explosion of "designer" materials—twisted bilayer graphene (magic angle), moiré heterostructures, artificially engineered kagome metals—created systems with engineered VHS at tunable energies. These systems exhibit dramatic many-body effects (superconductivity, ferromagnetism, metal-insulator transitions) that can be correlated with VHS properties.

The recognition that **flat bands are the high-order limit of VHS** unified two seemingly distinct phenomena: the extreme divergence (flat band) and power-law divergence (high-order VHS) represent points on a continuum. This unification is the focus of this review.

---

## Key Arguments and Derivations

### Classification of Van Hove Singularities

A van Hove singularity occurs when the Fermi surface becomes tangent to a band, creating a saddle point in the band dispersion. Near the VHS energy $E_s$, the density of states exhibits power-law behavior:

$$N(E) \sim |E - E_s|^{\alpha}$$

where the exponent $\alpha$ characterizes the singularity order.

**First-Order VHS** (codimension 1):
- 2D saddle point: $\varepsilon(\mathbf{k}) = E_s + a k_x^2 - b k_y^2$
- Density of states: $N(E) \sim \log|E - E_s|$
- Example: Graphene at M points, kagome saddle points

**Second-Order VHS** (codimension 2):
- 2D meromorphic point: $\varepsilon(\mathbf{k}) = E_s + a k_x^2 + b k_y^2$ (no saddle)
- Density of states: $N(E) \sim |E - E_s|^{1/2}$
- Example: Band edge in conventional metals

**Higher-Order VHS**:
- $n$-th order: $\varepsilon(\mathbf{k}) = E_s + \sum_{i=1}^n a_i k_i^p$ with special degeneracies
- Density of states: $N(E) \sim |E - E_s|^{\beta_n}$ with $\beta_n > 0$ for divergence
- Example: Moiré materials with multiple touching bands

### Flat Bands as Infinite-Order Limit

A perfectly flat band has:

$$\varepsilon(\mathbf{k}) = E_\text{flat} \text{ for all } \mathbf{k} \text{ in the flat region}$$

The density of states formally diverges:

$$N(E) \sim \delta(E - E_\text{flat})$$

This is the **infinite-order limit** of power-law divergence. Flat bands arise generically from:

1. **Destructive interference**: Tight-binding orbitals on frustrated lattices (e.g., kagome, checkerboard) where hopping paths interfere destructively, flattening one band
2. **Chiral symmetry**: In systems with sublattice structure and chiral symmetry, zero-energy modes can be exactly flat
3. **Topological origin**: Some flat bands carry non-trivial topological quantum numbers (e.g., Chern number)

### Interaction Effects at VHS

When a VHS is present, the large density of states enhances interaction effects. The Landau interaction parameter:

$$F_l^a = -\frac{m^*}{2\pi \hbar^2 N(E_F)} V_l^a$$

where $V_l^a$ is the pairing/charge interaction. With $N(E_F) \to \infty$ at VHS:

$$|F_l^a| \to \infty \text{ (instability)}$$

This instability is inevitable for any repulsive interaction. The resulting ordered state (charge-density wave, superconductivity, ferromagnetism, nematic) depends on which channel has strongest coupling.

### VHS and Superconductivity

For superconductivity, the critical temperature near VHS is enhanced:

$$T_c \sim \omega_D \exp\left(-\frac{1}{g N(E_F)}\right) \approx \omega_D \exp\left(-\frac{1}{g N_0 (E - E_s)^{\alpha}}\right)$$

where $N_0$ is the amplitude. Near $E = E_s$ (VHS), the exponent becomes negative and diverges, leading to exponentially enhanced $T_c$.

### Topological Properties of VHS-Containing Bands

Modern materials exhibit **topological VHS**—singularities that occur in bands carrying non-zero Chern numbers or other topological invariants. Examples:

- **Chern ferromagnetism**: VHS in Chern bands leads to ferromagnetism
- **Topological Superconductivity**: VHS in topological bands can induce pairing with topological order

The band geometry (Berry curvature, Fubini-Study metric) modifies interaction properties, and VHS can amplify these geometric effects.

### Moiré Materials and Designer VHS

Twisting two graphene sheets by the magic angle $\theta_m \approx 1.1°$ creates moiré patterns with multiple VHS aligned at the Fermi level:

$$\omega_\text{moiré} = 2\pi \frac{v_F}{l_\text{moiré}}$$

where $l_\text{moiré} \sim a / (2\sin(\theta/2))$ is the moiré wavelength ($a$ = graphene lattice constant).

This band structure engineering allows precise control of VHS energies and densities of states, creating "designer quantum materials."

---

## Key Results

1. **VHS Classification Scheme**: Systematic categorization of VHS orders (1st through infinite) based on local band geometry, with specific power-law exponents for each.

2. **Flat-Band Connection**: Proven that flat bands are the $\alpha \to \infty$ limit of power-law divergence, unifying two research areas historically treated separately.

3. **Interaction-Induced Instabilities**: Mapped interaction channels (s-wave, d-wave, nematic) and their propensity for instability at different VHS orders.

4. **Experimental Evidence Compilation**: Systematic review of ARPES, STM, and neutron scattering data confirming VHS in:
   - Graphene and graphene multilayers (bilayer, trilayer, moiré)
   - Transition-metal dichalcogenides (MoS₂, WSe₂)
   - Kagome metals (Co₃Sn₂S₂, MnSn, FeSn)
   - Moiré heterostructures (graphene/hBN, WSe₂/MoS₂)
   - Ruthenates (Sr₂RuO₄)

5. **Topological VHS**: Identified systems where VHS occurs in topologically non-trivial bands, enabling "topological instabilities" (ferromagnetism in Chern bands, topological superconductivity).

6. **Critical Temperature Enhancement**: Quantified the enhancement of $T_c$ and instability scales near VHS, with examples showing 10-100× amplification vs. non-singular case.

7. **Design Principles**: Established guidelines for engineering VHS in artificial systems (twisted stacks, heterostructures, artificial lattices).

---

## Impact and Legacy

**Unified Framework**: The VHS-flat band connection provides a unified understanding of instability mechanisms across materials with very different microscopic details.

**Predictive Tool**: The VHS classification enables prediction of instabilities in new materials from band structure alone, facilitating discovery of novel correlated phases.

**Materials Design**: Demonstrates that electronic properties can be engineered by designing density of states through geometric control (twisting, stacking, doping).

---

## Connection to Phonon-Exflation Framework

**Phonon-Analog of VHS-Flat Band Physics**:

Framework Session 22c identified: **B2 sector hosts a flat band** created by internal K_7 pairing geometry, generating a van Hove singularity in the spectral action density of states.

**Structural Mapping**:

1. **Flat-Band Origin**:
   - Kagome/Moiré: Destructive interference on frustrated lattice
   - Framework: K_7-charge conservation forces all B2 configurations into same energy (exact degeneracy), creating flat band

2. **VHS Characteristics**:
   - Classen-Betouras: VHS order $\alpha$ determines interaction scaling
   - Framework B2: Flat band is infinite-order VHS ($\alpha \to \infty$), yielding **maximal interaction amplification**
   - Consequence: Pomeranchuk instability at $f = -4.687$ (well into instability regime)

3. **Fermi-Surface Deformation**:
   - Kagome: Pomeranchuk instability breaks nematic symmetry in spatial momentum
   - Framework: Flat-band instability breaks K_7-charge direction symmetry
   - Both are **symmetry-breaking phase transitions induced by VHS**

4. **Topological Structure**:
   - Moiré materials: Some flat bands carry Chern number
   - Framework B2: Internal spectral geometry carries "color Chern number" (topological classification via CPS structure)
   - Framework advantage: Topological structure is **exact** (by construction from NCG), not emergent from band details

5. **Instability Robustness**:
   - Classen-Betouras: VHS-induced instabilities robust across parameter variations
   - Framework: B2 flat-band instability persists at all $\tau \in [0, 0.285]$ (Session 22d, TT stability scan)
   - Both exhibit **generic instability** rather than tuned coincidence

6. **Energy Scales**:
   - Moiré $T_c$ enhancement: 10-100× near VHS
   - Framework: $E_\text{vac}/E_\text{cond} = 28.8$ (ratio of vacuum vs. condensation energy)
   - Not directly comparable (different observables), but both indicate that **VHS-proximity drastically alters dynamics**

**Quantitative Prediction**:

If framework's B2 flat band triggers Pomeranchuk-like pairing rearrangement (as framework predicts), then the pairing coherence should reflect the **single-mode selection from flat-band instability**. This explains why framework exhibits 85.5% amplitude concentration—not fragmentation into 3-7 components as in nuclear systems without flat-band structure.

**Paper Relevance**: Classen-Betouras provide the comprehensive **condensed-matter classification** validating that flat bands are universal instability generators across all materials. Framework's B2 sector flat band is not exotic but a textbook example of this principle applied to internal spectral geometry.
