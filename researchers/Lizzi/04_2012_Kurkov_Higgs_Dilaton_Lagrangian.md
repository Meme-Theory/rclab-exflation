# Higgs-Dilaton Lagrangian from Spectral Regularization

**Authors:** M.A. Kurkov, Fedele Lizzi
**Year:** 2012
**arXiv:** 1210.2663
**Journal:** Modern Physics Letters A

---

## Abstract

We derive the complete Higgs-dilaton Lagrangian using spectral regularization methods. The dilaton appears as a natural scalar degree of freedom when treating the spectral action with conformal symmetry. The framework predicts couplings between the Higgs, dilaton, and gravitational fields with specific numerical coefficients determined by the Dirac operator's spectral structure.

---

## Key Results

### 1. Spectral Regularization Scheme

Define a momentum-space cutoff on the Dirac operator eigenvalues. Instead of Euclidean heat kernel methods, use **zeta function regularization**:

$$S_{\text{zeta}} = \zeta_D(0) = \lim_{s \to 0^+} \text{Tr} D^{-2s}$$

This is equivalent to extracting the coefficient of the conformal anomaly (a₄ heat kernel coefficient) directly. The resulting Lagrangian contains all dimension-≤4 operators but NO higher-dimension terms.

### 2. Higgs-Dilaton Potential

The effective potential emerges as:

$$V(\phi, H) = \lambda_\phi \phi^4 + \lambda_H H^4 + \lambda_{HH} \phi^2 H^2 + \mu_\phi^2 \phi^2 + \mu_H^2 H^2$$

where:
- $\lambda_\phi$ and $\lambda_H$ are quartic self-couplings
- $\lambda_{HH}$ is the cross-coupling (Higgs-dilaton mixing)
- $\mu_\phi^2$, $\mu_H^2$ are mass-squared parameters

**Critical coupling**: The Higgs mass at the minimum depends on the dilaton vev:

$$m_H^2 = \mu_H^2 + \lambda_{HH} \langle \phi \rangle^2$$

With $\langle \phi \rangle \approx 200$ GeV (dilaton vev), the Higgs mass can be adjusted to match the observed 125 GeV by varying the spectral action coefficients.

### 3. Kinetic Terms and Metric Coupling

The kinetic structure couples both fields to the metric:

$$\mathcal{L}_{\text{kin}} = \frac{M_P^2}{16\pi} R + \xi_\phi \phi^2 R + \xi_H H^2 R + \frac{1}{2}(\partial_\mu \phi)^2 + |D_\mu H|^2 + \cdots$$

where $\xi_\phi, \xi_H$ are conformal coupling constants ($\xi = 1/6$ for conformal coupling in 4D).

The non-minimal couplings to curvature R mean both Higgs and dilaton are **gravitational scalar fields**, not merely matter fields.

### 4. Yukawa and Gauge Coupling Structure

The Yukawa couplings depend on the dilaton:

$$\mathcal{L}_Y = -y_t(H) \, \bar{\psi}_L H \psi_R$$

where $y_t$ is itself a function of $\phi$ under renormalization. The renormalization group equations become coupled differential equations for both $y_t$ and the dilaton vev.

Gauge couplings similarly run with dilaton vev according to the beta function:

$$\beta_{g_i}(\phi) = \frac{\partial g_i}{\partial \ln \mu} \bigg|_\phi$$

### 5. Phenomenological Predictions

**Higgs mass prediction**: Using Kurkov-Lizzi spectral data:
- At unification scale: g₁ = g₂ = g₃ (unified couplings)
- Higgs vev: v_H ≈ 246 GeV
- Dilaton vev: v_φ ≈ 10¹⁴-10¹⁷ GeV (unification scale)
- Predicted Higgs mass: m_H ≈ 125-140 GeV

This is an order-of-magnitude success given no free parameters beyond fermion masses (Yukawa couplings).

---

## Key Innovations

1. **Complete Lagrangian**: First paper to write out the full Standard Model coupled to gravity WITH dilaton, all coefficients determined by spectral geometry.

2. **Renormalizability**: The Lagrangian is renormalizable to all loop orders (unlike cutoff spectral action). No dimension->4 operators appear; the theory is UV-safe.

3. **Naturalness perspective**: The Higgs mass problem is reframed: instead of asking "why is m_H ~ 100 GeV?", ask "why is the dilaton vev ~ 10¹⁶ GeV?" This is a hierarchy problem between two scales, potentially solvable via conformal symmetry breaking.

4. **Axial vector coupling to dilaton**: The dilaton couples to the trace of the energy-momentum tensor:

$$T_\mu^\mu = \phi \cdot (\text{trace of stress-energy})$$

This means the dilaton naturally couples to all massive fields, explaining why it appears in cosmology (dark energy, inflation).

---

## Impact and Legacy

Established the **standard form** of the Higgs-dilaton Lagrangian in NCG. Subsequent papers by:
- Connes-Chamseddine (2012): "Resilience" incorporating grand symmetry
- Devastato-Lizzi-Martinetti (2014): Extended scalar sector from Clifford algebra structure
- Van Suijlekom (2014+): Comprehensive reviews

This paper is the **bridge** between abstract spectral action and concrete phenomenology.

---

## Connection to Phonon-Exflation Framework

**Direct relevance**: The framework's internal geometry is M⁴ × SU(3) where the SU(3) is the spectral interior. The **compactification scale** (radius of SU(3)) plays a role analogous to the dilaton vev.

If the Jensen deformation parameter tau is identified as a **dilaton-like scalar** coupling to the spectral action, then:

1. tau → 0 (undeformed): Large dilaton vev, "unbroken" conformal phase
2. tau → τ_fold (critical): Phase transition, dilaton vev drops, conformal symmetry breaking
3. tau → 1 (deformed): Small dilaton vev, "broken" phase, Standard Model masses dynamically generated

**Cosmological implication**: The transit through the van Hove fold in phonon-exflation corresponds to a **dilaton-driven phase transition**, not a slow-roll inflation. The dilaton rolls from large vev (pre-transit) to small vev (post-transit), with the field's kinetic energy driving the expansion.

**Current framework status**: Kurkov-Lizzi establish the machinery for dilaton-SM coupling. The phonon-exflation framework must now identify how the internal SU(3) geometry couples to the dilaton sector to achieve the measured observables (n_s, r, Ω_Λ).

**Critical gap**: The Higgs-dilaton potential (Paper 04) still requires ad-hoc parameter tuning (μ², λ coefficients) to match observations. The phonon-exflation program claims to COMPUTE these from first principles via spectral geometry. This gap is addressed in subsequent Lizzi papers (Papers 05-10) on anomaly sources and modified spectral functionals.
