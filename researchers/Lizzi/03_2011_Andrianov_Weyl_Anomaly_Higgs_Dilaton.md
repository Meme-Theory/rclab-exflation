# Spectral action, Weyl anomaly and the Higgs-Dilaton potential

**Authors:** A.A. Andrianov, M.A. Kurkov, Fedele Lizzi
**Year:** 2011
**arXiv:** 1106.3263v1
**Journal:** JHEP

---

## Abstract

The bosonic spectral action emerges from the fermionic action through the Weyl (conformal) anomaly in the presence of a dilaton field. Unlike the scale anomaly (Paper 02), the Weyl anomaly captures local conformal invariance, providing a natural framework for the entire Standard Model coupled to gravity. The dilaton—a scalar field with conformal weight—plays a central role in generating the Higgs potential dynamically.

---

## Key Arguments

### 1. Weyl Invariance vs. Scale Invariance

**Scale invariance** (Paper 02): Global transformation $x^\mu \to e^\phi x^\mu$. This is a change of units.

**Weyl (conformal) invariance**: Local transformation $g_{\mu\nu} \to e^{2\alpha(x)} g_{\mu\nu}$ of the metric, coupled to appropriate scalar field transformations:

$$g_{\mu\nu} \to e^{2\alpha} g_{\mu\nu}, \quad \psi \to e^{-3\alpha/2} \psi, \quad \phi \to e^{-\alpha} \phi$$

where $\alpha(x)$ is a local function. The dilaton field $\phi(x)$ with conformal weight -1 couples to all mass-like terms:

$$\mathcal{L}_{\text{dilaton}} = \phi \cdot (\text{all dimension-2 operators})$$

### 2. Fermionic Action in Fixed Background

In a fixed gravitational and dilaton background, the fermionic action under Weyl transformation is:

$$S_\psi = \int d^4x \sqrt{g} \, \bar{\psi} D \psi$$

where D is the covariant Dirac operator. The **Weyl anomaly** arises from the functional integral measure:

$$\mathcal{D}[\tilde{\psi}]\mathcal{D}[\tilde{\bar{\psi}}] = e^{S_{\text{anom}}[g,\phi]} \mathcal{D}[\psi]\mathcal{D}[\bar{\psi}]$$

The anomalous action is:

$$S_{\text{anom}}[g,\phi] = -\int d^4x \sqrt{g} \, \left( c_0 \phi^4 + c_1 \phi^2 R + c_2 \phi^2 \square \phi + \cdots \right)$$

where coefficients $c_i$ are determined by Weyl anomaly coefficients (related to Seeley-DeWitt coefficients).

### 3. Dilaton Coupling to Matter

The **Higgs doublet** H in the Standard Model can be rewritten in terms of a dilaton-like field:

$$H = h(x) e^{-\phi(x)/f}, \quad h \equiv \text{real Higgs field}, \quad f \equiv \text{scale constant}$$

Under Weyl transformation, this automatically generates the correct conformal weight if $\phi$ is chosen appropriately.

The **Yukawa couplings** to fermions become:

$$\mathcal{L}_Y = y_t \bar{\psi}_L H \psi_R e^{-\alpha} = y_t \bar{\psi}_L h e^{-\phi/f} e^{-\alpha} \psi_R$$

When integrated over the conformal field, these generate specific couplings between the dilaton and Standard Model fields.

### 4. Effective Potential from Weyl Anomaly

The dilaton effective potential emerges from the loop integral over fermions:

$$V_{\text{eff}}(\phi) = \int \mathcal{D}[\psi]\mathcal{D}[\bar{\psi}] e^{-S_\psi[\phi]} = e^{-S_{\text{anom}}[\phi]}$$

Taking the leading order from the Weyl anomaly:

$$V_{\text{eff}}(\phi) \propto \Lambda^4 e^{-4\phi/f} + m^2 \phi^2 + \lambda \phi^4 + \cdots$$

This has the desired structure: two phases.

1. **Unbroken phase** ($\phi$ large): Exponential dominates, potential is steep.
2. **Broken phase** ($\phi$ small): Quadratic term dominates, potential has a minimum.

The **transition** from unbroken to broken occurs when:
$$\frac{d V}{d\phi} = 0 \implies 4\Lambda^4 e^{-4\phi/f} = 2m^2\phi + 4\lambda\phi^3$$

At the minimum:
$$\langle \phi \rangle = v_\phi \approx \frac{\Lambda^2}{m f}$$

### 5. Higgs Mass in Terms of Dilaton

If the Higgs field is coupled to the dilaton as $H = h e^{-\phi/f}$, then the Higgs mass becomes:

$$m_H^2 = m_h^2 e^{-2\langle\phi\rangle/f} + (\text{dilaton contributions})$$

Numerically, the framework predicts a Higgs mass around 125-140 GeV (pre-2012 experimental value: 125 GeV, an order-of-magnitude success).

---

## Key Results

1. **Weyl anomaly induces spectral action**: Unlike global scale invariance (which was a change of units), local Weyl invariance is a genuine gauge symmetry. The Weyl anomaly is non-vanishing and forces a bosonic counterterm—the spectral action.

2. **Dilaton is fundamental**: The dilaton field appears naturally in conformal field theory and is essential for maintaining Weyl invariance at the quantum level. It is not an ad hoc addition.

3. **Two-phase potential**: The effective potential naturally exhibits both an unbroken phase (large field values) and a broken phase (small field values), with a rolling trajectory connecting them. This is essential for early-universe cosmology.

4. **Dynamical mass generation**: The Higgs mass is not put in by hand; it emerges from the interplay of dilaton vev and Yukawa couplings. The zero of the potential is not at $\phi = 0$ but at a dynamically determined value.

5. **RG flow determines dilaton couplings**: Under renormalization group flow (running from high to low energy), the dilaton couples to all dimension-two operators with coefficients determined by Weyl anomaly coefficients.

---

## Impact and Legacy

This paper elevated the Higgs-dilaton sector from a phenomenological add-on to a **fundamental consequence of quantum conformal symmetry**. It unified the treatment of:
- Gravity (via Einstein-Hilbert term from Weyl anomaly)
- Gauge fields (from spectral action)
- Higgs field (from dilaton bosonization)
- Neutrino masses (from Majorana terms in D_F)

The framework became a blueprint for subsequent work on:
- **Kurkov-Lizzi 2012 (arXiv:1210.2663)**: Full Higgs-dilaton Lagrangian and refined phenomenology
- **Devastato-Lizzi-Martinetti 2014**: Grand symmetry and extended scalar sector
- **Van Suijlekom 2014**: Comprehensive review incorporating all developments

---

## Connection to Phonon-Exflation Framework

**Spectral action structure**: The Weyl anomaly derivation shows that a₀, a₂, and a₄ Seeley-DeWitt coefficients are **independently accessible** through anomaly calculations:

- a₀ → cosmological constant/M⁴ term
- a₂ → Einstein-Hilbert/R term
- a₄ → Gauss-Bonnet/Weyl tensor term

**For the CC problem**: The dilaton-Higgs coupling mechanism suggests that IF the internal geometry (SU(3) fiber in the framework) undergoes a phase transition driven by spectral deformation (tau parameter), then:

1. The dilaton vev $\langle \phi \rangle$ shifts
2. The ratio a₀/a₂ changes
3. The observed cosmological constant becomes a function of the phase transition point, not an external tuning

This is the **conceptual bridge** between NCG spectral action and phonon-exflation cosmology: the transition through the van Hove fold (tau=0.19) is a dilaton-driven conformal phase transition.

**Current framework status**: The paper does not yet achieve decoupling of a₀ from a₂. However, the Weyl anomaly approach is more flexible than cutoff regularization, opening the possibility of modified anomaly coefficients through spectral geometry changes.

**Critical insight**: The framework's claim that expansion is driven by internal compactification (tau increasing) maps naturally to dilaton dynamics if the compactification parameter couples to the conformal sector. Lizzi's subsequent papers on spectral regularization variants (Papers 04-08) explore this possibility systematically.
