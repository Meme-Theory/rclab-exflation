# Gauge Threshold Corrections in Warped Geometry

**Author(s):** Kiwoon Choi, Ian-Woo Kim and Chang Sub Shin
**Year:** 2010
**Journal:** Journal of High Energy Physics 2010(05):010
**arXiv:** 1001.1473
**Relevance:** HIGH

---

## Abstract

We discuss the Kaluza-Klein threshold correction to low energy gauge couplings in theories with warped extra-dimension, which might be crucial for the gauge coupling unification when the warping is sizable. Explicit expressions of one-loop thresholds are derived for generic 5D gauge theory on a slice of AdS5, where some of the bulk gauge symmetries are broken by orbifold boundary conditions and/or by bulk Higgs vacuum values. Effects of the mass mixing between the bulk fields with different orbifold parities are included as such mixing is required in some class of realistic warped unification models.

---

## Key Arguments and Derivations

### Section 1: Introduction

In theories with unified gauge symmetry at high energy, threshold corrections due to heavy particles significantly affect predicted low energy gauge couplings. Higher-dimensional gauge theories have infinite towers of KK states, producing large thresholds. The paper focuses on warped (AdS5) geometry where thresholds are enhanced by the large logarithmic factor ln(e^Omega), with e^Omega an exponentially small warp factor.

### Section 2: Generic Features of KK Threshold Corrections

The 5D gauge theory is defined on a Wilsonian effective field theory with action S_W on a spacetime with metric ds^2 = e^{2 Omega(y)} eta_{mu nu} dx^mu dx^nu + R^2 dy^2 for 0 <= y <= pi.

The tree-level 4D gauge coupling is (1/g_a^2)_tree = pi R / g_{5a}^2 + (kappa_a + kappa'_a)/(8 pi^2), with kappa_a, kappa'_a boundary kinetic terms.

One-loop corrections decompose as: Delta_a/(8pi^2) = gamma_a Lambda pi R/(24 pi^3) + [b-tilde_a ln(Lambda pi R) - b_a ln(p pi R) + Delta-tilde_a(R, lambda)]/(8 pi^2).

The coefficient b_a is determined by zero-mode content (standard 4D beta function). The logarithmic divergence coefficient b-tilde_a is determined solely by orbifold boundary conditions of 5D fields. The finite calculable threshold Delta-tilde_a depends on all parameters.

For a flat-space massless 5D complex scalar, KK masses are m_n = n/R (++) or (2n+1)/2R (+-, -+) or (n+1)/R (--). The threshold correction is computed explicitly.

### Section 3: Generic 5D Gauge Theory on AdS5

The AdS5 metric has warp factor Omega(y) = -ky, with AdS curvature k. The paper derives the N-function whose zeros give KK masses for arbitrary bulk mass, boundary conditions, and mass mixing. Explicit threshold formulas are provided for all field types:

**Scalars (Table 1-3):** Thresholds for phi_{zz'} with all orbifold parities (++, +-, -+, --), including effects of bulk mass parameter alpha and warping. Key formula involves sinh and exponential functions of (alpha +/- k/2) pi R.

**Gauge/Vector fields (Table 4):** Similar structure, with the added complication of ghost contributions and gauge fixing. The 5D gauge threshold involves both A_mu and A_5 components.

**Fermions (Tables 5-6):** Dirac fermion thresholds with bulk mass M_F and mixing. Two Dirac fermions with different parities can mix via boundary mass terms. Mixing angles c_0, c_pi, s_0, s_pi parametrize the threshold.

**Key warped enhancement:** In the strongly warped limit kR >> 1, the threshold grows as pi k R (proportional to the logarithm of the hierarchy), enhancing gauge threshold corrections.

### Section 4: Conclusions

The results cover most warped GUT models discussed in the literature. The threshold corrections are scheme-independent and provide the finite calculable part of quantum corrections to low energy gauge couplings.

## Key Results

1. Complete one-loop KK threshold corrections for generic 5D gauge theory on AdS5 slice, including orbifold breaking and bulk Higgs VEVs
2. Explicit expressions for all field types (scalar, vector, fermion) with arbitrary orbifold boundary conditions
3. Warped threshold enhancement proportional to pi k R ~ ln(M_Planck/M_KK) for strong warping
4. Mass mixing effects between bulk fields of different orbifold parities included for realistic warped GUT models
5. Clear separation of power-divergent (scheme-dependent), log-divergent (boundary-determined), and finite (KK threshold) contributions

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Warped metric | $ds^2 = e^{2\Omega(y)}\eta_{\mu\nu}dx^\mu dx^\nu + R^2 dy^2$ | Sec. 2 |
| Tree coupling | $(1/g_a^2)_{\text{tree}} = \pi R / g_{5a}^2 + (\kappa_a + \kappa'_a)/(8\pi^2)$ | Eq. (4) |
| 1-loop structure | $\frac{1}{8\pi^2}\Delta_a = \frac{\gamma_a}{24\pi^3}\Lambda\pi R + \frac{1}{8\pi^2}[\tilde{b}_a\ln(\Lambda\pi R) - b_a\ln(p\pi R) + \tilde{\Delta}_a]$ | Eq. (6) |
| Zero-mode beta | $b_a = \frac{1}{6}\sum_{\phi^{(0)}}\text{Tr}(T_a^2) + \frac{2}{3}\sum_{\psi^{(0)}}\text{Tr}(T_a^2) - \frac{11}{3}\sum_{A_\mu^{(0)}}\text{Tr}(T_a^2)$ | Eq. (9) |
| Boundary coefficient | $\tilde{b}_a = \sum_{zz'}\frac{z+z'}{24}[\text{Tr}(T_a^2(\phi_{zz'})) - 23\,\text{Tr}(T_a^2(A^M_{zz'}))]$ | Eq. (12) |
| Flat scalar KK | $m_n(\phi_{++}) = n/R,\quad m_n(\phi_{+-}) = (2n+1)/(2R)$ | Eq. (15) |

## Relevance to Phonon-Exflation

1. **KK threshold corrections for M4 x SU(3):** The project's framework has an internal SU(3) manifold with tau-dependent geometry. As tau evolves, the KK spectrum shifts, producing threshold corrections to the effective 4D gauge couplings. This paper's formalism (adapted from AdS5 to the project's SU(3) fiber) provides the mathematical framework for computing such effects.

2. **Warping analog:** The tau-dependent left-invariant metric on SU(3) introduces position-dependent scales analogous to warping. The warp-enhanced threshold corrections proportional to ln(hierarchy) parallel the project's analysis of gauge coupling running during the tau-transit.

3. **Orbifold vs. SU(3) breaking:** The orbifold boundary conditions that break gauge symmetry in 5D are analogous to the Jensen K_7 symmetry breaking in the project's framework, where [iK_7, D_K] = 0 breaks SU(3) -> U(1)_7.

4. **Mass mixing and BCS:** The paper's treatment of mass mixing between fields of different orbifold parities parallels the BCS gap structure in the project, where pairing mixes states across the spectral gap.
