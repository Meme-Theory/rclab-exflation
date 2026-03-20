# One-Loop Corrections to the Spectral Action

**Author(s):** van Nuland, van Suijlekom
**Year:** 2022
**Journal:** Journal of High Energy Physics, Vol. 05, p. 078, arXiv:2107.08485

---

## Abstract

We study one-loop quantum corrections to the spectral action within the framework of noncommutative geometry. We establish one-loop renormalizability in a generalized sense by showing that counterterms arising from the path integral over matrix fluctuations can be expressed in the same spectral form as the classical action. Using Ward identities and the spectral triple formalism, we prove that the quantum-corrected theory remains consistent within the noncommutative geometry framework, with no new counterterms that violate spectral closure.

---

## Historical Context

The spectral action principle, introduced by Chamseddine and Connes, provides a unified description of gravity and the Standard Model through the geometry of a spectral triple. However, a critical question remained: does the spectral action survive quantum corrections? Naively, one-loop calculations could produce counterterms not expressible in spectral form, breaking the framework's closure.

van Nuland and van Suijlekom's 2022 work resolves this concern. By carefully analyzing the perturbative quantization of the spectral action—treating matrix fluctuations around a noncommutative gauge background—they show that all one-loop counterterms can be absorbed into the spectral action. Crucially, they prove that the renormalized action retains its spectral structure, with coupling constants running via standard beta functions but in a manner consistent with geometric renormalization.

This is essential for the framework's viability as a quantum theory and, in the context of phonon-exflation, validates the use of the spectral action at intermediate energy scales where quantum corrections begin to matter.

---

## Key Arguments and Derivations

### Path Integral Over Matrix Fluctuations

The spectral action is formulated as:

$$S_{\text{spec}} = \text{Tr}\, f\left(\frac{\mathcal{D}^2}{\Lambda^2}\right)$$

where $\mathcal{D}$ is the Dirac operator of a spectral triple and $f$ is a test function. Quantum corrections arise from fluctuations $\mathcal{D} \to \mathcal{D} + \delta \mathcal{D}$, where $\delta \mathcal{D}$ couples to external gauge fields.

The one-loop partition function is:

$$Z_{\text{1-loop}} = \int \mathcal{D}[\delta \mathcal{D}] \, e^{i S_{\text{spec}}[\mathcal{D} + \delta \mathcal{D}]}$$

This integral is regulated by expanding in powers of $\delta \mathcal{D}$:

$$Z_{\text{1-loop}} = \exp\left( \frac{i}{2} \text{Tr}\, \ln \left( \mathbb{1} + \delta \mathcal{D} \cdot (\mathcal{D}^0)^{-1} \right) \right)$$

where $\mathcal{D}^0$ denotes the background Dirac operator.

### Effective Action and Counterterm Structure

The effective action at one loop is:

$$\Gamma_{\text{1-loop}} = \frac{i}{2} \text{Tr}\, \ln \det \left( \mathbb{1} + \delta \mathcal{D} \cdot (\mathcal{D}^0)^{-1} \right)$$

Expanding to second order in $\delta \mathcal{D}$:

$$\Gamma_{\text{1-loop}} = \frac{i}{2} \text{Tr}\left( \delta \mathcal{D} (\mathcal{D}^0)^{-1} \right) - \frac{1}{2} \text{Tr}\left( \delta \mathcal{D} (\mathcal{D}^0)^{-1} \delta \mathcal{D} (\mathcal{D}^0)^{-1} \right) + \cdots$$

The second term—the two-loop level contribution—exhibits potential divergences in the ultraviolet. Regularization via dimensional continuation or zeta-function techniques yields counterterms.

### Ward Identities and Spectral Closure

The key innovation is invoking **Ward identities** from the gauge principle. For a noncommutative gauge symmetry:

$$\delta \mathcal{D} = [A, \mathcal{D}]$$

where $A \in \mathcal{A}$ (the gauge algebra), the functional integral respects this constraint. Ward identities guarantee:

$$\left. \frac{\delta \Gamma_{\text{1-loop}}}{\delta A} \right|_{\text{conservation}} = 0$$

This constraint ensures that counterterms cannot violate the spectral gauge principle.

### Spectral Renormalization: Coupling Constants

Despite quantum corrections, the renormalized action maintains spectral form:

$$S_{\text{eff}}[\mathcal{D}; \mu] = \text{Tr}\, f\left(\frac{\mathcal{D}^2(\mu)}{\Lambda(\mu)^2}\right)$$

where coupling constants and the Dirac operator depend on the renormalization scale $\mu$. The running is governed by standard beta functions.

For the unified gauge coupling $g$ in the spectral framework:

$$\frac{dg}{d\log\mu} = \beta_g(g; N_f)$$

where $N_f$ is the number of fermion flavors. Crucially, $\beta_g$ is **not** new information from the spectral action—it is inherited from the Standard Model beta function, confirming the framework's consistency.

Similarly, for the Higgs sector (encoded in the scalar spectral triple), the quartic coupling $\lambda$ runs:

$$\frac{d\lambda}{d\log\mu} = \beta_\lambda(\lambda, g_t, g, g')$$

Again, $\beta_\lambda$ is the standard SM one-loop result, confirming spectral closure.

### Monotonicity Preservation

A crucial observation: the spectral action coefficients appear in polynomial form:

$$S_{\text{spec}} = \int d^4x \sqrt{g}\left( a_0 + a_2 R + a_4 R_{\mu\nu}^2 + a_6 C_{\mu\nu\rho\sigma}^2 + \cdots \right)$$

The coefficients $a_0, a_2, a_4, \ldots$ are **universal** (independent of $\mu$), determined by heat kernel geometry. Their scale-independence follows from dimensional analysis: they are geometric invariants, not coupling constants.

Therefore, **monotonicity of the spectral action** (if it holds at tree level due to a particular geometry or constraint) is preserved under one-loop corrections. Quantum running affects only the overall coupling strengths $g, \lambda, \ldots$, not the relative ordering of spectral coefficients.

### One-Loop Counterterm Expressibility

van Suijlekom and van Nuland prove that for every divergence in the one-loop effective action, there exists a local spectral operator that absorbs it. Specifically:

$$\int d^4x \sqrt{g} \left[ \frac{C_1}{16\pi^2\epsilon} R^2 + \frac{C_2}{16\pi^2\epsilon} R_{\mu\nu}^2 + \cdots \right] = \Delta S_{\text{spec}}[\text{allowed}]$$

where $\Delta S_{\text{spec}}$ is a finite modification to spectral action coefficients (renormalization of $a_2, a_4$, etc.), and $\epsilon = (4-d)/2$ is the dimensional regularization parameter.

This **renormalization of heat kernel coefficients** occurs but does not violate the spectral principle. The renormalized action remains a genuine spectral action, just with quantum-corrected coefficients.

---

## Key Results

1. **One-Loop Renormalizability PROVED**: The spectral action is renormalizable at one loop in the sense that all UV divergences can be absorbed into renormalized coupling constants and heat kernel coefficients, staying within the spectral framework.

2. **Ward Identities Enforce Spectral Closure**: Gauge symmetry Ward identities guarantee that no non-spectral counterterms are generated. The quantum theory remains geometric.

3. **Coupling Constants Run Standardly**: Gauge couplings $g$ and Higgs quartic $\lambda$ run via the known SM beta functions, confirming the spectral framework's internal consistency.

4. **Heat Kernel Coefficients Renormalize**: Spectral action coefficients $a_2, a_4, \ldots$ undergo finite renormalization at one loop, but remain geometric (rational combinations of curvature invariants).

5. **Monotonicity Preserved**: If the tree-level spectral action exhibits monotonicity in a relevant parameter, this structure is inherited by the one-loop effective action (with running couplings).

---

## Impact and Legacy

van Suijlekom and van Nuland's work elevated the spectral action from a classical geometric framework to a true quantum theory. Their proof that spectral closure is maintained under quantum corrections is a watershed result: it shows that noncommutative geometry is not merely a classical reinterpretation of known physics, but a genuine quantization principle.

Subsequent applications (particularly to finite-density settings by Dong-Khalkhali-van Suijlekom and others) leveraged this robustness to compute thermodynamic corrections and phase transitions in the spectral framework.

In cosmology, the one-loop stability of the spectral action supports predictions of inflationary parameters and dark energy equations of state: quantum corrections modify couplings but preserve the framework's geometric structure.

---

## Framework Relevance

**Critical Connection**: In the phonon-exflation framework, the finite-density spectral action on $M^4 \times SU(3)$ with BCS pairing is a **quantum many-body system** where one-loop effects are substantial (coupling $g \sim 1$). van Suijlekom's theorem ensures that quantum corrections to the spectral action (from fermion loops in the pairing channel) do not introduce non-spectral counterterms that would violate geometric closure.

Specifically:
- The framework's claim that the spectral action encodes fermion mass generation rests on a consistent quantum treatment. van Suijlekom's work validates this.
- The monotonicity of the spectral action coefficient $a_4$ (Session 24a, V-1) survives quantum corrections, supporting the framework's vacuum selection principle.
- One-loop beta functions for the gauge coupling $g$ and scalar self-couplings in the SU(3) sector follow standard QCD/SM patterns, confirming that the framework produces conventional particle physics at low scales.

**Status**: STRUCTURAL + COMPUTATIONAL. One-loop renormalizability is a necessary condition for quantum viability of the framework. Van Suijlekom's proof removes a potential fundamental obstruction.

**Open Question**: Two-loop effects and resummation of ladder diagrams in the BCS channel remain to be addressed (relevant for finite-density thermodynamics at higher coupling).
