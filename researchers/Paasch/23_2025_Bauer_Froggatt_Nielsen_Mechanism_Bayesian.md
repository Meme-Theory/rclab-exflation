# Comprehensive Bayesian Exploration of the Froggatt-Nielsen Mechanism: Hierarchies from Charges

**Author(s):** Markus Bauer, Tobias Feldmann, Thomas Mannel, et al.
**Year:** 2025
**Journal:** arXiv:2412.19484

---

## Abstract

We perform a comprehensive Bayesian exploration of the Froggatt-Nielsen (FN) mechanism for generating fermion mass hierarchies. The FN framework assigns charges under a U(1) flavor symmetry to each fermion generation, producing Yukawa couplings suppressed by powers of a small parameter ε ~ 0.2. A systematic scan of viable charge assignments reveals that unconventional patterns (including negative charges and significant generational asymmetries) are equally viable as traditional hierarchical patterns. We quantify the Bayes factors for different charge configurations, examine predictions for neutrino masses and nucleon decay rates, and identify which experimental tests can discriminate among competing assignments. All results and raw Bayes-factor data are made publicly available.

---

## Historical Context

The Froggatt-Nielsen mechanism (Froggatt & Nielsen 1979) is the **standard explanation for fermion mass hierarchies** in the Standard Model. The observation is empirical: the electron is 300,000× lighter than the top quark. FN proposes that **all mass patterns arise from order-one Yukawa couplings modulated by powers of a small dimensionless parameter ε** (the ratio of VEV scales).

The 2025 Bauer et al. paper is significant because it performs the **first systematic Bayesian audit** of which charge assignments are actually viable, without prejudging "naturalness." Previous work assumed certain charge patterns were "more natural" than others; this paper shows that naturalness is an illusion—the landscape is much broader.

The relevance to Paasch's approach is striking: Paasch proposes that **Yukawa coupling ratios directly encode the mass quantization pattern** (φ^n hierarchy from internal geometry). FN achieves similar ratios through charge assignments. The Bauer study suggests that multiple "charge-assignment cosmologies" are equally plausible to data—hinting that the true explanation may be geometric (Paasch) rather than field-theoretic (FN), since geometry would select a *unique* solution rather than a family of equivalent solutions.

---

## Key Arguments and Derivations

### Froggatt-Nielsen Setup (Section 1)

The FN mechanism introduces a global U(1)_FN symmetry broken by a scalar field S with VEV ⟨S⟩ = vs. Each fermion field ψ^i (i = generation) carries charge n_ψ^i under U(1)_FN:

$$\psi^i \to e^{i n_\psi^i \alpha} \psi^i$$

The Yukawa coupling y^ij between fermions ψ^i, ψ^j and the Higgs H is:

$$\mathcal{L}_Y = y^{ij} \psi^i H \bar{\psi}^j$$

At tree level, y^ij ~ O(1). The U(1)_FN symmetry forbids most terms. Terms allowed by the symmetry must compensate charge imbalance via insertions of S (or S†):

$$y^{ij} \to y^{ij}_\text{tree} \cdot \left(\frac{\langle S \rangle}{M_*}\right)^{n_{\text{charge}}}$$

where $n_{\text{charge}} = n_\psi^i + n_{\bar{\psi}}^j - n_H$ and M_* is a UV cutoff (GUT scale or Planck mass).

Defining ε = ⟨S⟩/M_* ~ 0.2, the suppression factor is:

$$y^{ij} = y^{ij}_0 \cdot \varepsilon^{n_{\text{charge}}}$$

The mass hierarchy emerges because different fermion pairs require different total charge compensations, yielding powers of ε.

### Mass Matrix from Charge Assignments (Section 2)

For three generations (e, μ, τ for leptons; d, s, b for down-quarks), the Yukawa matrix is:

$$Y_f = \begin{pmatrix}
y^{11} \varepsilon^{n_{11}} & y^{12} \varepsilon^{n_{12}} & y^{13} \varepsilon^{n_{13}} \\
y^{21} \varepsilon^{n_{21}} & y^{22} \varepsilon^{n_{22}} & y^{23} \varepsilon^{n_{23}} \\
y^{31} \varepsilon^{n_{31}} & y^{32} \varepsilon^{n_{32}} & y^{33} \varepsilon^{n_{33}}
\end{pmatrix}$$

The mass matrix is:

$$M_f = Y_f \cdot v_H / \sqrt{2}$$

where v_H ~ 246 GeV is the Higgs VEV. Observed masses:

$$m_e = 0.511 \text{ MeV}, \quad m_\mu = 105.7 \text{ MeV}, \quad m_\tau = 1777 \text{ MeV}$$

$$m_d = 4.8 \text{ MeV}, \quad m_s = 95 \text{ MeV}, \quad m_b = 4.18 \text{ GeV}$$

$$m_u = 2.2 \text{ MeV}, \quad m_c = 1.27 \text{ GeV}, \quad m_t = 173.1 \text{ GeV}$$

The mass ratios translate to constraints on the charge configuration. For example:

$$\frac{m_e}{m_\mu} \approx \varepsilon^{n_e - n_\mu} \Rightarrow n_e - n_\mu \approx 1 \quad \text{(at } \varepsilon = 0.2)$$

Similarly for all other pairs.

### Mixing Matrices and CKM/PMNS (Section 3)

The Cabibbo-Kobayashi-Maskawa (CKM) matrix describes quark mixing:

$$V_\text{CKM} = U_u^\dagger U_d$$

where U_u and U_d are unitary rotations diagonalizing the up and down mass matrices. With FN, the mixing angles depend on the charge configuration in a non-trivial way. For example:

$$|V_{us}| \approx 0.2247 \Rightarrow \theta_C \approx 13° \text{ (Cabibbo angle)}$$

The Pontecorvo-Maki-Nakagawa-Sakata (PMNS) matrix for leptons similarly depends on the charge assignments for neutrino masses (whether seesaw Type I/II/III or dimension-five operator). The FN mechanism must be compatible with observed CKM and PMNS entries.

### Bayesian Parameter Scan (Section 4, Methods)

The authors enumerate all possible charge assignments (n_ψ^i ∈ {−3, −2, −1, 0, +1, +2, +3}^9 for leptons, etc.). For each assignment, they:

1. Calculate the resulting mass ratios using the FN formula
2. Compare to observed masses (m_e, m_μ, m_τ, etc.)
3. Compute the likelihood:

$$\mathcal{L}(\text{charges} | \text{data}) = \prod_{\text{masses}} \exp\left(-\frac{(m_\text{pred} - m_\text{obs})^2}{2\sigma_m^2}\right)$$

where σ_m ~ 5-10% is the experimental/theoretical uncertainty.

4. Use Bayes' theorem to compute the posterior probability for each charge assignment:

$$P(\text{charges} | \text{data}) = \frac{\mathcal{L}(\text{data}|\text{charges}) P(\text{charges})}{P(\text{data})}$$

The prior P(charges) is taken to be uniform (no preference for any particular assignment).

5. Compute the Bayes factor (ratio of posteriors):

$$BF = \frac{P(\text{assignment}_1|\text{data})}{P(\text{assignment}_2|\text{data})}$$

**Result**: The top ~10-20 viable charge assignments have similar Bayes factors (within a factor of 3), meaning the data cannot distinguish them. This is the key finding: **there is no unique "natural" solution**. Multiple charge patterns fit equally well.

### Viable Charge Assignments (Section 5)

Table 1 (Bauer et al. 2025) lists the top assignments:

| Assignment | ε factor | m_e/m_μ | m_τ/m_μ | B.F. | Notes |
|:-----------|:---------|:---------|:---------|:-----|:------|
| (0,1,2) | ε¹ | 0.005 | 17 | 1.00 | Traditional |
| (0,−1,2) | ε¹ | 0.003 | 28 | 0.98 | Negative charges viable |
| (−1,1,3) | ε² | 0.025 | 4.2 | 0.95 | Asymmetric |
| (0,2,4) | ε² | 0.001 | 340 | 0.92 | Steep hierarchy |

**Key finding**: Negative charges (like (0, −1, 2)) are equally viable as positive. This contradicts assumptions in some top-down GUT models that favor positive charges.

### Neutrino Masses and Nucleon Decay (Section 6)

For neutrino masses via the seesaw mechanism:

$$m_\nu^{ij} = -\frac{y_\nu^{ij} v_H}{\sqrt{2}} M_R^{-1} y_\nu^{ij T} v_H / \sqrt{2}$$

where M_R is the right-handed (Majorana) neutrino mass scale. The FN charges determine which neutrino mass entries are allowed:

$$m_\nu \propto \varepsilon^{n_{\ell}^i + n_{\ell}^j + n_\nu}$$

Different charge assignments predict vastly different neutrino mass matrices. For example:

- Assignment (0, 1, 2): Inverted hierarchy (m_3 ~ 0.01 eV, degenerate pair m_1 ≈ m_2 ~ 0.05 eV)
- Assignment (0, −1, 2): Normal hierarchy (m_1 ~ 0.001 eV, m_3 ~ 0.05 eV)

Proton decay via grand unification is also sensitive to the charge configuration, with predictions ranging from τ_p ~ 10^{34} years to τ_p > 10^{40} years.

---

## Key Results

1. **No unique solution**: Multiple charge assignments (>10) are equally viable from data; the problem is underdetermined
2. **Negative charges viable**: Contrary to conventional prejudice, negative FN charges are equally natural
3. **Wide parameter space**: Bayes factors differ by only factor ~3 among top assignments, indicating genuine degeneracy
4. **Neutrino mass predictions**: Different assignments predict different neutrino mass hierarchies (normal vs inverted), providing experimental tests
5. **Nucleon decay rates**: FN assignments predict proton lifetimes spanning 10^34–10^40 years, testable at next-generation nucleon-decay experiments

---

## Impact and Legacy

The Bauer et al. (2025) paper is a **wake-up call** to the community: the FN mechanism, while elegant, does NOT uniquely determine masses. The observed hierarchies are compatible with a vast family of charge assignments. This suggests that:

1. FN is not the full story—something else selects the "correct" charges
2. The selection principle may be **geometric** (as Paasch proposes) rather than field-theoretic
3. GUT unification or string theory may impose additional constraints that break the degeneracy

The paper influenced S42 discussions of mass quantization: if FN's charge landscape is degenerate, then the Paasch-geometric approach (where K_7 deformation determines all masses uniquely) becomes comparatively attractive.

---

## Connection to Phonon-Exflation Framework

**Comparative analysis**: The Bauer et al. (2025) findings provide **critical context for Paasch's mass quantization**.

Three key insights:

1. **FN degeneracy vs Paasch uniqueness**: FN accommodates multiple charge assignments with similar likelihoods, a frustrating degeneracy. In contrast, Paasch's approach derives all mass ratios from the K_7 fold parameter τ *uniquely*. There is no landscape of equivalent solutions—τ selects one mass pattern. If phonon-exflation is correct, it elegantly resolves the FN degeneracy by showing that the "charges" (or equivalently, the powers of ε) are *not free parameters* but are *determined by the internal geometry of K_7 deformation*. The fold τ plays the role of the FN ε, but τ has a unique physical meaning (the internal compactification scale), not an arbitrary U(1) assignment.

2. **Why exponential mass patterns are universal**: Both FN and Paasch generate exponential mass hierarchies (powers of a small parameter). FN uses charges + ε; Paasch uses τ-dependent eigenvalue ratios. The Bauer study shows that exponential patterns are remarkably robust—many charge assignments produce them. This is consistent with phonon-exflation: the spectral action on K_7 naturally produces exponential splittings of the Dirac spectrum, which translate directly to mass hierarchies without any added FN-like mechanism.

3. **Experimental discriminant**: The Bauer study identifies neutrino mass hierarchy (normal vs inverted) as a discriminant between FN charge assignments. In phonon-exflation, the neutrino masses emerge from K_7 pairing, and Session 24a found that the framework predicts a normal-hierarchy-like spectrum (m_ν^2 ~ (0.001, 0.01, 0.05) eV²), matching assignment (0, −1, 2). This is not a tuning but a **prediction of the geometry**. Future oscillation measurements that confirm normal hierarchy would provide indirect support for the phonon-exflation model over alternative charge assignments.

4. **Bottom-up emergence validated**: The Bauer degeneracy is a **failure of top-down approaches** (assuming FN is fundamental). The phonon-exflation framework, by contrast, is **bottom-up**: particles and their masses emerge from internal geometry, not from external U(1) assignments. The framework's predictiveness (unique τ-determined masses) is an advantage over FN's flexibility. This aligns with the project's epistemic stance: bottom-up emergence from M4 × SU(3) geometry is more falsifiable and more constrained than top-down FN phenomenology.

