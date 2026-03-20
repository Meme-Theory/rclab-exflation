# Unified Pati-Salam from Noncommutative Geometry: Overview and Phenomenological Remarks

**Author(s):** Ufuk Aydemir
**Year:** 2025
**Conference:** 28th Bled Workshop on Physics Beyond the Standard Model
**Journal:** Bled Workshop Proceedings
**arXiv:** 2511.07672 [hep-th]
**Submitted:** November 25, 2025

---

## Abstract

This paper reviews and extends recent developments in deriving gauge-coupling-unified Pati-Salam models from the noncommutative geometry (NCG) framework using the spectral action principle. The author examines the phenomenological implications of spectral NCG Pati-Salam models, with particular emphasis on the S₁ scalar leptoquark particle. The work addresses the challenge of discovering new physics at the Large Hadron Collider by proposing theoretically grounded models derived from geometric principles rather than ad hoc assumptions. The framework unifies the Standard Model, General Relativity, and extensions beyond the Standard Model through a common geometric foundation based on spectral triples. The paper demonstrates that gauge coupling unification emerges naturally, the unification scale is robustly predicted, and the scalar leptoquark spectrum offers testable predictions for future collider searches.

---

## Historical Context

The Pati-Salam model (Pati and Salam, 1974) has long been an attractive alternative to SU(5) grand unification. By treating leptons as a "fourth color," it naturally accommodates the quark-lepton complementarity. However, traditional Pati-Salam approaches required ad hoc mechanisms for symmetry breaking and scalar sector specification.

The spectral action framework, developed by Chamseddine and Connes since the 1990s, provides a principled way to derive gauge theories from the geometric structure of spectral triples—generalizations of Dirac operators on manifolds. This framework has successfully reproduced the Standard Model action, and subsequent work extended it to Pati-Salam and other grand unified theories.

Aydemir's 2025 paper is a timely review that consolidates recent progress and addresses a persistent question: do these geometrically-derived models make predictions that distinguish them from traditional approaches? The focus on the S₁ scalar leptoquark—a particle unique to Pati-Salam models—provides a concrete target for experimental searches.

For the Baptista program and phonon-exflation, this paper is valuable because it demonstrates that multiple grand unified theories (SU(5), Pati-Salam, others) can all be derived from spectral geometry. This suggests that the internal SU(3) metric in phonon-exflation can potentially realize different GUT structures depending on how it deforms.

---

## Key Arguments and Derivations

### Spectral Triple Construction for Pati-Salam

A spectral triple is a triple $(A, H, D)$ consisting of:
- $A$: A $*$-algebra of operators
- $H$: A Hilbert space
- $D$: An unbounded self-adjoint operator (Dirac-like) on $H$

For Pati-Salam in the NCG framework, the algebra is:

$$\mathcal{A} = C^\infty(M) \otimes \mathcal{A}_F$$

where $M$ is 4D spacetime and $\mathcal{A}_F$ is a finite-dimensional algebra encoding the particle content:

$$\mathcal{A}_F = M_4(\mathbb{C}) \oplus M_4(\mathbb{C}) \oplus M_2(\mathbb{C})$$

This represents:
- First $M_4(\mathbb{C})$: SU(4) color-lepton structure acting on left-handed fermions
- Second $M_4(\mathbb{C})$: SU(4) acting on right-handed fermions (under custodial symmetry)
- $M_2(\mathbb{C})$: Left-right symmetry mixing

The Dirac operator $D$ on the finite space $F$ is:

$$D_F = \begin{pmatrix} 0 & M_D \\ M_D^\dagger & 0 \end{pmatrix}$$

where $M_D$ is the fermion mass matrix. Its eigenvalues are related to physical fermion masses and Yukawa couplings.

### Spectral Action and Pati-Salam Action

The spectral action is:

$$S = \text{Tr}(f(D/\Lambda))$$

where $f$ is a smooth cutoff function and $\Lambda$ is the energy scale. When expanded using heat kernel methods, this yields:

$$S = S_{\text{gravity}} + S_{\text{Yang-Mills}} + S_{\text{matter}} + S_{\text{scalar}}$$

The Yang-Mills part is:

$$S_{\text{YM}} = \int d^4x \sqrt{g} \sum_{i} \frac{1}{4g_i^2} \text{tr}(F_i^{\mu\nu} F_{i\mu\nu})$$

where the sum is over the three Pati-Salam gauge groups: $i = L, R, C$ for the SU(2)_L, SU(2)_R, and SU(4)_c factors.

The coupling constants are determined by:

$$g_i^{-2} = \frac{f(0)}{2\pi^2} \int d^4x \sqrt{g} \, \text{tr}_F(T_i^a T_i^a)$$

where $T_i^a$ are the generators of the $i$-th gauge group and the trace is over the finite algebra.

### Gauge Coupling Unification

A central result is that the three couplings unify. At the one-loop level, the running equations are:

$$\alpha_i^{-1}(\mu) = \alpha_i^{-1}(\Lambda_{\text{GUT}}) + \frac{b_i}{2\pi} \ln(\mu / \Lambda_{\text{GUT}})$$

where $\alpha_i = g_i^2 / (4\pi)$ and $b_i$ are the beta function coefficients.

The unification condition is that at some scale $\Lambda_{\text{GUT}}$:

$$g_L(\Lambda_{\text{GUT}}) = g_R(\Lambda_{\text{GUT}}) = g_C(\Lambda_{\text{GUT}}) = g_{\text{GUT}}$$

This occurs when the beta function coefficients satisfy a specific relationship determined by the matter content. The remarkable finding (from Chamseddine, Connes, and van Suijlekom, 2015) is that for the spectral Pati-Salam algebra, this unification **always** occurs, regardless of which specific spectral triple (i.e., which choice of fermion content and Yukawa structure) is used.

The unification scale is typically:

$$\Lambda_{\text{GUT}} \approx 1.5 \times 10^{16} \text{ GeV}$$

consistent with minimal proton decay constraints.

### Scalar Sector and the S₁ Leptoquark

The scalar sector of the Pati-Salam model includes:
- The Higgs doublet (from electroweak symmetry breaking)
- Leptoquark and diquark scalars (from Pati-Salam symmetry breaking)

The primary interest in this paper is the **S₁ scalar leptoquark**, which carries baryon number $B = -1/3$ and lepton number $L = -2$. It couples to a quark of any color and a lepton as:

$$\mathcal{L} \supset \lambda_{ij} \bar{q}_i^c S_1 \ell_j + \text{h.c.}$$

where $q_i$ is a quark, $\ell_j$ is a lepton, and $\lambda_{ij}$ is a coupling matrix.

The mass of S₁ is expected to be of order the Pati-Salam breaking scale:

$$m_{S_1} \sim v_{PS} \sim 10^{15} - 10^{16} \text{ GeV}$$

However, in some scenarios (e.g., with vector-like fermions), lighter leptoquarks with masses around 1-10 TeV are possible.

From the spectral action, the scalar potential is:

$$V = \lambda_H (|H|^2 - v_H^2)^2 + \lambda_S (|S_1|^2 - v_S^2)^2 + \lambda_{HS} (|H|^2 - v_H^2)(|S_1|^2 - v_S^2)$$

where the coupling constants $\lambda_H, \lambda_S, \lambda_{HS}$ are determined by the spectral action (Seeley-DeWitt coefficients).

### Phenomenological Predictions

The key phenomenological predictions from spectral NCG Pati-Salam are:

1. **Unification of Gauge Couplings**: All three gauge couplings unify at $10^{16}$ GeV with coupling strength $\alpha_{\text{GUT}} \approx 1/24$.

2. **Proton Decay**: The proton decays dominantly via the process $p \to e^+ \pi^0$ with lifetime:

$$\tau_p \sim 10^{34} \text{ years}$$

within reach of next-generation proton decay experiments.

3. **Leptoquark Masses**: The S₁ scalar leptoquark has mass:

$$m_{S_1} \sim (10^{15} \text{ GeV}) \times \left( \frac{m_Z}{m_W} \right)^{1/2} \sim 2-5 \times 10^{15} \text{ GeV}$$

for the minimal model, though extensions can lower this.

4. **Flavor-Changing Neutral Currents (FCNCs)**: The leptoquark couplings $\lambda_{ij}$ are constrained by FCNC measurements (particularly $\mu \to e\gamma$, $K \to \mu e$, etc.).

5. **Yukawa Couplings**: The fermionic masses and Yukawa couplings are predictions of the spectral geometry, not independent parameters. This severely constrains the model and makes quantitative predictions for the fermion mass spectrum.

### Comparison to GUT Normalization

In standard grand unification (e.g., SU(5)), the coupling constant normalization factors differ. The relation between the Pati-Salam coupling and the Standard Model couplings at low energies is:

$$g_1(M_Z) = g_C(M_{\text{GUT}}) \sqrt{\frac{5}{3}}$$

(using the GUT normalization for U(1) hypercharge). In the spectral action framework, these normalization factors emerge naturally from the trace formulas:

$$g_i^{-2} \propto \text{tr}(\text{generators}^2)$$

For Pati-Salam, the relative normalizations of SU(2), SU(2), and SU(4) factors determine the exact coupling ratios, and these are encoded in the algebra.

---

## Key Results

1. **Pati-Salam from Spectral Geometry**: The gauge group and coupling structure emerge directly from the algebraic structure of the noncommutative space, requiring no ad hoc inputs.

2. **Universal Gauge Unification**: Across all valid spectral Pati-Salam models, gauge coupling unification is automatic at approximately $10^{16}$ GeV.

3. **Scalar Leptoquark Predictions**: The S₁ scalar leptoquark is a robust prediction of the model, with mass scale set by the Pati-Salam breaking scale.

4. **Fermion Mass Predictions**: The spectral action relates fermion masses to the Dirac operator eigenvalue spectrum, providing nontrivial constraints on the mass matrix.

5. **Gauge Anomaly Cancellation**: The spectral framework automatically ensures all gauge anomalies cancel—a consistency check that the model is quantum-mechanically sound.

6. **Testable Predictions**: Proton decay, precision electroweak observables, and FCNC processes provide multiple experimental handles on the model.

---

## Impact and Legacy

This work positions spectral NCG as a serious contender for physics beyond the Standard Model:

- **Principle-Driven Model Building**: Rather than guessing at extensions, the framework provides a systematic way to construct unified theories.
- **Connection to Experiment**: The predictions (unification scale, leptoquark mass, proton decay rate) are testable, making the framework falsifiable.
- **Guidance for Future Searches**: The identification of the S₁ leptoquark as a key signature particle guides experimental strategies.

---

## Connection to Phonon-Exflation Framework

This paper is highly relevant for phonon-exflation:

1. **Flexibility in Gauge Structure**: The demonstration that multiple GUT structures (SU(5), Pati-Salam, others) can be derived from spectral geometry suggests that the internal SU(3) metric in phonon-exflation is flexible enough to realize various unified theories.

2. **Metric as Algebraic Structure**: Just as different algebraic structures in the finite NCG space yield different gauge groups, different internal metric shapes could yield different gauge couplings or even extended gauge structures.

3. **Dynamical Unification**: As phonons excite the internal metric during inflation, the effective gauge structure could evolve. This opens the possibility of **dynamical grand unification** during the early universe.

4. **Leptoquark Physics from Phonons**: The scalar leptoquark, if realized in phonon-exflation, would emerge from internal metric fluctuations. Its mass and coupling strengths would depend on the internal geometry.

5. **Constraints from Precision Physics**: The paper's discussion of FCNC constraints and proton decay rates provides guidance for what precision physics constraints should be imposed on any phonon-exflation model.

---

## References

- Aydemir, U. (2025). "Unified Pati-Salam from Noncommutative Geometry: Overview and Phenomenological Remarks." In *Proceedings of the 28th Bled Workshop on Physics Beyond the Standard Model*. arXiv:2511.07672 [hep-th].
- Chamseddine, A. H., Connes, A., & van Suijlekom, W. D. (2015). "Grand Unification in the Spectral Pati-Salam Model." *Journal of High Energy Physics*, 2015(11), 011.
- Pati, J. C., & Salam, A. (1974). "Lepton Number as the Fourth 'Color'." *Physical Review D*, 10(1), 275-289.
- Connes, A. (2007). "Noncommutative Geometry and Physics: A Review." In *Handbook of the History of Logic*, Vol. 5, Elsevier.
