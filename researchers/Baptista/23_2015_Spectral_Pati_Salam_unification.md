# Grand Unification in the Spectral Pati-Salam Model

**Author(s):** Ali H. Chamseddine, Alain Connes, Walter D. van Suijlekom
**Year:** 2015
**Journal:** Journal of High Energy Physics, Vol. 2015, Article 11
**arXiv:** 1507.08161
**Published:** July 29, 2015

---

## Abstract

This paper extends the spectral action framework beyond the Standard Model to derive the Pati-Salam grand unified theory from noncommutative geometry principles. The authors construct a spectral triple whose finite part encodes the Pati-Salam gauge group $\text{SU}(2)_L \times \text{SU}(2)_R \times \text{SU}(4)_c$ and analyze the running of gauge couplings at one-loop order in the resulting theory. A key finding is that unification of the Pati-Salam gauge couplings occurs across all scalar content scenarios determined by the Dirac operator structure in the finite noncommutative space. The unification scale is approximately $10^{16}$ GeV, consistent with proton decay constraints. The paper demonstrates that gauge coupling unification is not imposed as an external condition but emerges naturally from the geometric structure of the noncommutative algebra.

---

## Historical Context

Grand Unified Theories (GUTs) have long promised to unify the strong, weak, and electromagnetic interactions within a single gauge group. The Standard Model provides three independent coupling constants $g_1, g_2, g_3$, with no explanation for their relative strengths. GUTs like SU(5) and SO(10) propose that at high energies, these couplings merge into a single coupling constant $g_{\text{GUT}}$.

Pati-Salam theory, proposed by Pati and Salam in 1974, is an alternative to SU(5) that unifies quarks and leptons by treating leptons as a "fourth color" in an SU(4) group. The gauge group is $\text{SU}(2)_L \times \text{SU}(2)_R \times \text{SU}(4)_c$, where the left and right SU(2) factors implement custodial symmetry (protecting the $\rho$ parameter from large corrections).

The Pati-Salam model is attractive because it naturally predicts different running of coupling constants compared to SU(5), and it can be embedded in SO(10) at higher scales. However, the traditional approach required adding a Higgs mechanism to break Pati-Salam symmetry to the Standard Model.

Chamseddine, Connes, and van Suijlekom show in this 2015 paper that Pati-Salam unification emerges naturally from spectral geometry—without ad hoc Higgs fields. The gauge group structure is encoded in the algebra of the noncommutative space, and the coupling unification follows from the spectral action principle.

For the Baptista program and phonon-exflation, this paper is significant because it shows that a non-Standard-Model gauge group can be derived from geometric principles. If internal metric deformations can realize Pati-Salam structure (in addition to Standard Model structure), it would suggest that the phonon-exflation framework is flexible enough to encompass various unified theories.

---

## Key Arguments and Derivations

### Almost-Commutative Geometry for Pati-Salam

The authors construct an almost-commutative space $M \times F_{\text{PS}}$ where:
- $M$ is 4D Minkowski spacetime
- $F_{\text{PS}}$ is a finite noncommutative space encoding Pati-Salam structure

The algebra is:
$$\mathcal{A} = C^\infty(M) \otimes \mathcal{A}_F$$

where $\mathcal{A}_F$ is built from:
$$\mathcal{A}_F = \mathbb{C} \otimes M_4(\mathbb{C}) \otimes M_2(\mathbb{C})$$

This encodes:
- The first $\mathbb{C}$: a singlet (for the vector-like component of the Standard Model)
- $M_4(\mathbb{C})$: the SU(4) color and lepton number structure (4×4 matrices)
- $M_2(\mathbb{C})$: the custodial SU(2) structure (2×2 matrices)

The Dirac operator on the finite space $F_{\text{PS}}$ is a matrix acting on the fermionic representation space:

$$D_F = \begin{pmatrix} 0 & M \\ M^\dagger & 0 \end{pmatrix}$$

where $M$ is a mass matrix whose entries contain the Yukawa couplings and Higgs field couplings.

### Full Dirac Operator and Spectral Action

The Dirac operator on the full space $M \times F_{\text{PS}}$ is:

$$D = \gamma^\mu \partial_\mu \otimes 1_F + 1_M \otimes D_F$$

where $1_F$ and $1_M$ are identity operators on the finite and spacetime parts, respectively.

The spectral action is:

$$S[\mathcal{A}, D] = \int_M \sqrt{g} \, \text{Tr}(f(D/\Lambda))$$

When expanded, this yields:

$$S = S_{\text{gravitational}} + S_{\text{Pati-Salam}} + S_{\text{matter}} + S_{\text{Higgs}}$$

### Pati-Salam Action from Spectral Action

The Pati-Salam part of the action is:

$$S_{\text{PS}} = \int d^4x \sqrt{g} \left[ \frac{1}{4g_L^2} \text{tr}(F_L^2) + \frac{1}{4g_R^2} \text{tr}(F_R^2) + \frac{1}{4g_C^2} \text{tr}(F_C^2) \right]$$

where $F_L, F_R, F_C$ are the field strengths for the three gauge groups SU(2)_L, SU(2)_R, and SU(4)_c.

The coupling constants are determined by:

$$\frac{1}{g_L^2} = \frac{f(0)}{2\pi^2} \int d^4x \sqrt{g} \, \text{tr}(T_L^a T_L^b) F_L^a_{\mu\nu} F_L^{b\mu\nu}$$

and similarly for $g_R$ and $g_C$. Here $T_L^a, T_R^a, T_C^a$ are the generators in the appropriate representations.

### Gauge Coupling Unification

To analyze unification, the authors compute the one-loop beta functions for the three gauge couplings:

$$\frac{dg_i}{d\ln \mu} = \frac{\beta_i}{16\pi^2} g_i^3$$

where $\beta_i$ are the one-loop beta function coefficients. For Pati-Salam, these depend on the matter content.

The running equations are:

$$\alpha_i^{-1}(\mu) = \alpha_i^{-1}(M_Z) - \frac{\beta_i}{2\pi} \ln \left(\frac{\mu}{M_Z}\right)$$

where $\alpha_i = g_i^2 / (4\pi)$.

The authors find that for appropriate choices of the Dirac operator (which determine the matter content), the three couplings meet at a single scale $M_{\text{GUT}} \approx 10^{16}$ GeV with:

$$g_L(M_{\text{GUT}}) = g_R(M_{\text{GUT}}) = g_C(M_{\text{GUT}}) = g_{\text{GUT}}$$

### Unification Condition and Coupling Ratios

The condition for unification is that the inverse couplings satisfy:

$$\alpha_L^{-1}(M_{\text{GUT}}) = \alpha_R^{-1}(M_{\text{GUT}}) = \alpha_C^{-1}(M_{\text{GUT}})$$

Substituting the running equations:

$$\alpha_L^{-1}(M_Z) - \frac{\beta_L}{2\pi} \ln \left(\frac{M_{\text{GUT}}}{M_Z}\right) = \alpha_R^{-1}(M_Z) - \frac{\beta_R}{2\pi} \ln \left(\frac{M_{\text{GUT}}}{M_Z}\right)$$

This determines $M_{\text{GUT}}$ and the boundary condition at the GUT scale.

The key insight is that the beta function coefficients $\beta_i$ are determined by the spectral triple structure. Different choices of the matrix $M$ in $D_F$ lead to different matter content and thus different beta functions. However, the authors show that **regardless of which valid Pati-Salam spectral triple is chosen**, the three couplings unify.

This is remarkable: unification is not fine-tuned but a robust feature of the framework.

### Normalization of Couplings from Trace Formulas

The coupling constants in the spectral action framework are determined by:

$$g_i^{-2} \propto \text{tr}(T_i \text{ generators in representation } R_i)$$

For Pati-Salam:
- $g_L^{-2}$ involves traces over the SU(2)_L representation (dimension 2 for fermions)
- $g_R^{-2}$ involves traces over the SU(2)_R representation (also dimension 2)
- $g_C^{-2}$ involves traces over the SU(4)_c representation (dimension 4 for quarks/leptons)

The ratio of couplings at the GUT scale is:

$$\frac{g_L}{g_R} = \sqrt{\frac{\text{tr}(T_L^2)}{\text{tr}(T_R^2)}} = 1$$

(by custodial symmetry), and

$$\frac{g_C}{g_L} = \sqrt{\frac{\text{tr}(T_C^2)}{\text{tr}(T_L^2)}} = \sqrt{\frac{\text{dim}(4)}{\text{dim}(2)}} = \sqrt{2}$$

(approximately, with exact numerical factors depending on the representation details).

---

## Key Results

1. **Pati-Salam Emerges from Spectral Geometry**: The Pati-Salam gauge group $\text{SU}(2)_L \times \text{SU}(2)_R \times \text{SU}(4)_c$ is the natural gauge structure arising from a finite noncommutative space almost-commutative geometry.

2. **Gauge Coupling Unification is Universal**: Across all Pati-Salam spectral triples consistent with the framework, the three gauge couplings unify at approximately $M_{\text{GUT}} \approx 10^{16}$ GeV.

3. **No Fine-Tuning Required**: Unlike traditional GUT approaches, unification emerges without adjusting parameters. It is a consequence of the geometric structure.

4. **Unification Scale from Geometry**: The unification scale and the unified coupling value are determined by the spectral properties of the Dirac operator—no ad hoc energy scale assumption is needed.

5. **Coupling Ratio Predictions**: The ratios of coupling constants at the GUT scale are predicted from group representation theory and geometry, not fit to data.

6. **Matter Content Flexibility**: Different valid Dirac operators on the finite space correspond to different matter content (different numbers of fermion families), but all lead to unification.

---

## Impact and Legacy

This work demonstrates that the spectral action framework is sufficiently powerful to encompass grand unified theories beyond the Standard Model. Key impacts include:

- **Legitimacy of Non-Standard Unification**: It shows that Pati-Salam unification, an alternative to SU(5), can be derived from first principles in spectral geometry.
- **Guidance for Physics Beyond the Standard Model**: Rather than guessing at unification groups, the framework suggests exploring which algebras lead to unification and what their physical implications are.
- **Predictive Power**: The framework makes predictions (unified coupling values, unification scale) that can be tested against future precision measurements.

The paper has spawned follow-up work on:
- Proton decay rates in spectral Pati-Salam models
- Neutrino mass patterns
- Dark matter candidates
- Supersymmetric extensions

---

## Connection to Phonon-Exflation Framework

For phonon-exflation, this paper has several important implications:

1. **Gauge Structure Flexibility**: Just as different spectral triples can yield different grand unified theories, different internal metric deformations in the SU(3) space could potentially realize different gauge structures beyond the Standard Model.

2. **Unification from Metric Geometry**: The paper suggests that gauge coupling unification is a geometric phenomenon tied to the internal metric structure. In phonon-exflation, this means the coupling ratios are determined by the shape of SU(3) after deformation.

3. **Coupling Predictions from First Principles**: Rather than assuming unification, phonon-exflation can predict coupling ratios from the geometry of internal metric deformations. The spectral action formula $g^{-2} \propto \text{tr}$ provides the tool.

4. **Robustness Across Deformations**: Just as Pati-Salam unification is robust across different spectral triple choices, phonon-exflation suggests that key predictions (like Standard Model gauge structure) are robust against variations in the specific form of metric deformation.

5. **Dynamical Unification**: In phonon-exflation, as phonons excite the internal metric during expansion, the gauge coupling unification can be dynamical—couplings run not just with energy scale but with the state of the internal metric.

---

## References

- Chamseddine, A. H., Connes, A., & van Suijlekom, W. D. (2015). "Grand Unification in the Spectral Pati-Salam Model." *Journal of High Energy Physics*, 2015, 11. arXiv:1507.08161 [hep-th].
- Pati, J. C., & Salam, A. (1974). "Lepton Number as the Fourth 'Color'." *Physical Review D*, 10(1), 275-289.
- Chamseddine, A. H., Connes, A., & van Suijlekom, W. D. (2013). "Beyond the Spectral Standard Model: Emergence of Pati-Salam Unification." *Journal of High Energy Physics*, 1304, 040. arXiv:1304.8050 [hep-th].
- Weinberg, S. (1980). "Baryon and Lepton Nonconserving Processes." *Physical Review Letters*, 43(21), 1566-1570.
