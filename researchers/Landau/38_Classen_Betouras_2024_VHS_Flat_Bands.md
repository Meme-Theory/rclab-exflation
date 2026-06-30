# High-order Van Hove singularities and their connection to flat bands

**Author(s):** Laura Classen, Joseph J. Betouras
**Year:** 2024
**Journal:** Annu. Rev. Condens. Matter Phys. (2024)
**arXiv:** 2405.20226
**Relevance:** HIGH

---

## Abstract

The flattening of single-particle band structures plays an important role in the quest for novel quantum states of matter due to the crucial role of interactions. Recent advances in theory and experiment made it possible to construct and tune systems with nearly flat bands, ranging from graphene multilayers and moire materials to kagome metals and ruthenates. While theoretical models predict exactly flat bands under certain ideal conditions, evidence was provided that these systems host high-order Van Hove points, i.e., points of high local band flatness and power-law divergence in energy of the density of states. In this review, we examine recent developments in engineering and realising such weakly dispersive bands. We focus on high-order Van Hove singularities and explore their connection to exactly flat bands. We provide classification schemes and discuss interaction effects. We also review experimental evidence for high-order Van Hove singularities and point out future research directions.

---

## Key Arguments and Derivations

### Definition and classification of HOVHS

A critical point k_0 of the dispersion epsilon_n(k) is high-order when both the gradient and the Hessian determinant vanish: nabla epsilon(k_0) = 0 and det[d^2 epsilon/dk_mu dk_nu] = 0. The Taylor expansion must go beyond quadratic order.

Classification uses four integer indices from catastrophe theory:
- **Corank**: number of zero eigenvalues of the Hessian
- **Codimension**: number of effective control parameters in the universal unfolding
- **Determinacy**: truncation order of the characteristic Taylor expansion
- **Winding**: number of sign changes of the function around the critical point (resolves 2D degeneracies)

The DOS near a HOVHS diverges as rho(E) ~ D_+/- |E|^{-gamma}, where gamma = sum_i a_i - 1 from scaling exponents a_i of the dispersion epsilon(lambda^{a_i} k_i) = lambda epsilon(k_i). The ratio D_+/D_- is universal (preserved under smooth coordinate transformations). For ordinary VHS: gamma = 0 (logarithmic), D_+/D_- = 1. For HOVHS: gamma > 0 (power-law), possibly D_+/D_- != 1.

### Connection to flat bands

Flat bands from destructive interference in lattices (line graphs, split graphs) can be perturbed to produce HOVHS. For singular flat bands (with immovable band-crossing discontinuities), perturbations that lift the degeneracy make the flat band dispersive, but it retains flatness along one direction -- producing a HOVHS.

The general continuum model for a singular flat band touching a quadratic band is:

H_k = h_0(k) sigma_0 + sum_i h_i(k) sigma_i

with det H_k = 0 (flat-band condition). Adding a perturbation m sigma_z can create two Dirac points with a HOVHS between them.

### Tuning from ordinary to high-order

Demonstrated on the triangular lattice with nearest- and next-nearest-neighbor hopping. At the critical ratio t'/t = 1/9, the quadratic term vanishes at the M-point saddle, producing a cusp HOVHS with canonical form ~ k_x^4 - k_y^2 and DOS diverging as |delta E|^{-1/4}.

### Interaction effects

HOVHS enhance all susceptibilities. Key results:
- **Bare susceptibilities**: diverge as power laws (not just logarithms) in both particle-hole and particle-particle channels
- **Ladder series**: enhanced pairing susceptibility, with power-law divergent Cooper logarithm
- **Competing orders**: RG analysis shows superconductivity, density waves, and nematic (Pomeranchuk) orders compete at HOVHS, with the hierarchy depending on symmetry and the specific HOVHS type
- **Supermetal**: near a HOVHS, a "supermetal" phase may exist where the system resists instabilities despite large DOS
- **Self-energy effects**: interactions can self-consistently generate HOVHS by flattening the band via Hartree corrections

### Materials overview

- **Sr2RuO4**: surface band hosts HOVHS achievable via strain or surface reconstruction
- **Sr3Ru2O7**: HOVHS under magnetic field (metamagnetic transition)
- **Kagome metals**: AV3Sb5 family (charge density waves), Co3Sn2S2 (Pomeranchuk instability)
- **Twisted bilayer graphene**: magic angle produces HOVHS with |delta E|^{-1/4} DOS
- **Bernal bilayer graphene**: displacement field tunes to HOVHS

---

## Key Results

1. Comprehensive classification of HOVHS using catastrophe theory: 17 singularities with codimension <= 7 in 2D
2. Crystal symmetry drastically reduces the number of control parameters needed to reach HOVHS
3. Flat bands generically produce HOVHS when perturbed
4. DOS exponent gamma = sum_i a_i - 1 from dispersion scaling exponents
5. HOVHS can be particle-hole asymmetric (D_+/D_- != 1), unlike ordinary VHS
6. Poincare-Hopf theorem constrains total topological index of all critical points to zero
7. Interaction-induced HOVHS possible via self-energy band flattening

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Triangular lattice | $H_0 = -t\sum_{\langle i,j\rangle} c^\dagger_i c_j - t'\sum_{\langle\langle i,j\rangle\rangle} c^\dagger_i c_j - \mu$ | Eq. (1) |
| HOVHS expansion | $\varepsilon_c(M_1+k) = -\frac{4}{3}tk_y^2 + \frac{1}{48}tk_x^4 + \frac{3}{8}tk_x^2k_y^2$ at $t'_c = t/9$ | Eq. (3) |
| Singular flat band | $H_k = h_0(k)\sigma_0 + \sum_i h_i(k)\sigma_i$ with $\det H_k = 0$ | Eq. (4) |
| DOS scaling | $\rho(\varepsilon) = \begin{cases} D_+|\varepsilon|^{-\gamma}, & \varepsilon > 0 \\ D_-|\varepsilon|^{-\gamma}, & \varepsilon < 0 \end{cases}$, $\gamma = \sum_i a_i - 1$ | Eq. (6) |
| Dispersion scaling | $\varepsilon(\lambda^{a_i}k_i) = \lambda\varepsilon(k_i)$ | Sec. 3.1 |
| Topological index (2D) | $I = \frac{1}{2\pi}\text{Im}\oint_C \frac{d\upsilon_x + id\upsilon_y}{\upsilon_x + i\upsilon_y}$, $\sum_i I_i = 0$ | Eq. (5) |
| Poincare-Hopf | $\sum_i I_i = 0$ (Euler characteristic of torus) | Sec. 3.1 |
| Quadratic VHS at M | $\varepsilon(M_1+k) = \frac{1}{2}(t-9t')k_x^2 - \frac{3}{2}(t-t')k_y^2 + O(k^4)$ | Eq. (2) |

## Relevance to Phonon-Exflation

This review provides the theoretical framework for understanding how the framework's Van Hove singularity at M_max = 1.674 (Session 35) may be a HOVHS rather than an ordinary VHS. The catastrophe-theory classification scheme can be applied directly to the SU(3) Dirac spectrum to determine the type and codimension of the spectral singularity at the fold. The connection between flat bands and HOVHS is particularly relevant: the framework's near-flat B2 sector (Casimir = 0.1557, irreducible) may host a HOVHS that drives the Pomeranchuk instability at f(0,0) = -4.687. The interaction-induced HOVHS mechanism (self-energy flattening) maps onto the BCS self-consistent gap affecting the spectral geometry.
