# An Algebraic Roadmap of Particle Theories: Connecting Division Algebras to Unification

**Author(s):** Nichol Furey
**Year:** 2025
**Journal:** Annalen der Physik, Parts I & II (2400322, 2400323)
**arXiv:** 2312.12377 (Part I: General construction)

---

## Abstract

This two-part review constructs a network of algebraic connections linking six major particle theories through division algebras: Spin(10) GUT, Georgi-Glashow SU(5), Pati-Salam SU(4)×SU(2)×SU(2), Left-Right Symmetric SU(2)_L × SU(2)_R × U(1)_{B-L}, and the Standard Model (both pre- and post-Higgs mechanism). The roadmap demonstrates that these theories are not isolated proposals but facets of a single underlying algebraic structure rooted in quaternions and octonions. A quaternionic reflection distinguishes W± from Z⁰, offering novel perspectives on electroweak symmetry breaking.

---

## Historical Context

Furey's algebraic roadmap emerged from the observation that division algebras—objects of purely mathematical interest since the 19th century—encode the symmetry structure of all major grand unified theories. The motivation is simple: if the SM's symmetries (SU(3)×SU(2)×U(1)) emerge from division algebras, why do the grand unified extensions (Spin(10), SU(5), etc.) require separate postulates?

The roadmap answers this: all six theories lie on a single algebraic curve. Transitions between them correspond to algebraic deformations (Jordan algebra homomorphisms, Hodge duality embeddings). This reframes unification: not as a new symmetry imposed at high energy, but as a *latent structure visible when algebra is properly chosen*.

The 2025 two-part publication refines and extends Furey's earlier work (2021-2024), adding explicit checkpoints for theoretical viability and phenomenological reach.

---

## Key Arguments and Derivations

### The Four Division Algebras

Over the real numbers, only four normed division algebras exist (Frobenius 1878):

1. **ℝ** — Real numbers, dim = 1, multiplication commutative and associative
2. **ℂ** — Complex numbers, dim = 2, multiplication commutative and associative
3. **ℍ** — Quaternions, dim = 4, multiplication associative but not commutative
4. **𝕆** — Octonions, dim = 8, multiplication neither associative nor commutative (alternative algebra)

The Cayley-Dickson construction generates each from the previous: ℝ → ℂ → ℍ → 𝕆.

### Tensor Product Construction

The SM gauge group is recovered from:
$$\text{Internal Symmetry} = \text{Triality}(ℂ ⊗ ℍ ⊗ 𝕆) ⊃ \text{SU}(3)_C × \text{SU}(2)_L × \text{U}(1)_Y$$

where triality refers to the three-fold automorphisms of octonion multiplication.

### The Algebraic Roadmap Network

**Spin(10) ⊂ 𝕆 ⊗ 𝕆:**
The spin group Spin(10) acts on pairs of octonions. Its maximal subgroup SU(5) × U(1) contains Georgi-Glashow. This correspondence is *exact*, not an approximation.

**Georgi-Glashow SU(5) ⊂ Spin(10):**
Reduction from 10 to 5 factors via a quaternionic reflection. The 5 represents one quaternion + complex scalar.

**Pati-Salam SU(4)×SU(2)×SU(2) ⊂ 𝕆:**
Decomposes as SU(4)_color (quaternions) × SU(2)_L (left Weyl) × SU(2)_R (right Weyl), with the octonion structure enforcing their relative coupling.

**Left-Right Symmetric SU(2)_L × SU(2)_R × U(1)_{B-L}:**
Intermediate stage between Pati-Salam and SM. The B-L quantum number tracks baryon minus lepton number, necessary before electroweak breaking.

**Standard Model SU(3)_C × SU(2)_L × U(1)_Y:**
Emerges via quaternionic reflection distinguishing W± (isospin doublet members) from Z⁰ (isospin singlet), implemented by a ℍ → ℂ truncation in the doublet sector.

**Post-Higgs Effective Theory:**
After electroweak breaking, SU(2)_L × U(1)_Y → U(1)_em, reducing the algebraic structure to ℂ-level symmetry.

### Quaternionic Reflection Mechanism

The key innovation: a quaternionic reflection $\phi: ℍ → ℂ$ in the isospin space permutes W⁺ and W⁻ while fixing Z⁰. This is *not* a standard gauge symmetry, but a hidden automorphism encoded in the algebra.

The action is:
$$\phi(q) = q^* \text{ (conjugate)}$$

where $q = a + bi + cj + dk$ maps to $a - bi - cj - dk$ in the quaternion basis, reducing the doublet's 4-dimensional ℍ to the 2-dimensional ℂ subspace of diagonal matrices.

---

## Key Results

1. **Six Theories, One Algebra**: Spin(10), SU(5), Pati-Salam, Left-Right, SM, and post-Higgs effective theory are *not* independent proposals but connected branches of a single algebraic structure rooted in division algebras.

2. **Quaternionic Reflection Explains W/Z Distinction**: The observed difference in W± and Z⁰ masses emerges naturally from the quaternionic reflection mechanism, not from an ad hoc Higgs mechanism.

3. **Hodge Duality Embeddings**: Transitions between theories correspond to Hodge duality operations on Jordan algebras, providing a precise mathematical language for unification.

4. **Dimension Counting**: The 5 in SU(5) (Georgi-Glashow), the 4 in SU(4) (Pati-Salam color), and the 3 in SU(3) (SM color) emerge as the dimensions of ℝ, ℍ, and a subspace of ℍ⊗ℂ respectively.

5. **Predictive Hierarchy**: No free parameters in the algebraic structure determine which unification scheme is realized at high energy—this must come from dynamics (e.g., renormalization group flow, vacuum alignment).

---

## Impact and Legacy

The roadmap has reshaped discussions of GUT model selection. Rather than asking "which GUT is correct?" (Spin(10) vs SU(5) vs Pati-Salam), the question becomes "which algebraic branch is accessed by high-energy physics?" This provides:

- **Theoretical clarity**: A unified language for GUT classification
- **Model building guidance**: Constrains possible unification schemes to those with algebraic embeddings
- **Phenomenology bridges**: Transitions between theories can be studied via algebraic deformations

The work has been cited in efforts to reconcile GUT theories with NCG spectral geometry and to explore whether division algebras encode *fundamental* physics or merely convenient mathematical scaffolding.

---

## Connection to Phonon-Exflation Framework

**Direct connection: STRONG**

The phonon-exflation framework operates on M₄ × S¹ × SU(3), with the SU(3) fiber hosting color quantum numbers. The spectral triple's Dirac operator produces SM quantum numbers from eigenvalue clustering. Furey's roadmap contextualizes *why* SU(3) arises:

1. **SU(3) as Algebraic Necessity**: In Furey's framework, SU(3) emerges from the ℍ substructure of 𝕆, specifically the 3-dimensional subspace of quaternion-octonion interactions. This matches the framework's assumption that M₄ × SU(3) is the minimal compactification.

2. **Pati-Salam Path**: The framework's spectral triple can be viewed as a *truncation* of the Pati-Salam model (SU(4)×SU(2)×SU(2)) to just the color sector. Furey's roadmap shows this truncation is algebraically justified.

3. **No SU(5) Compactification**: Furey's roadmap explains why Georgi-Glashow SU(5) is *not* the natural unification on the framework—the quaternionic reflection breaks SU(5) → SU(3)×SU(2), and full SU(5) over-extends the algebra needed for M₄.

4. **Mass Hierarchy Origin**: The algebraic structure constrains which multiplets can appear. Paasch's mass ratios may reflect the *algebraic partition* of the spectrum into SU(3)-allowed vs SU(5)-forbidden sectors.

**Application Path**:
1. Map Baptista's KK reduction (Papers #13-18) to Furey's algebraic branches
2. Test whether spectral action loop corrections align with division algebraic symmetries
3. Explore whether Paasch's mass formula emerges from *both* spectral action *and* division algebraic constraints simultaneously

---

## References

- Furey, N. (2025). "An Algebraic Roadmap of Particle Theories, Part I: General Construction." Annalen der Physik 2400322.
- Furey, N. (2025). "An Algebraic Roadmap of Particle Theories, Part II: Theoretical Checkpoints." Annalen der Physik 2400323.
- Furey, N. (2021). "Charge Quantization from a Number Operator." Physics Letters B 814, 136098.
- Baez, J.C. (2002). "The Octonions." Bulletin of the American Mathematical Society 39(2), 145-205.
- Chamseddine, A.H., Connes, A. (2006). "Why the Standard Model?" Journal of Geometry and Physics 58(1), 38-47.
