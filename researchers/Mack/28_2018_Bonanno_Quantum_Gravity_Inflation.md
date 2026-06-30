# Cosmological Bounds on the Field Content of Asymptotically Safe Gravity-Matter Models

**Author(s):** Alfio Bonanno, Alessia Platania, Frank Saueressig
**Year:** 2018
**Journal/ArXiv:** arXiv:1803.02355

---

## Abstract

The authors use non-Gaussian fixed points (NGFPs) appearing in the renormalization group flow of gravity and gravity-matter systems to construct models of NGFP-driven inflation via a renormalization group improvement scheme. The cosmological predictions of these models depend sensitively on the characteristic properties of the NGFPs, including their position and stability coefficients, which are determined by the field content of the underlying matter sector. The authors demonstrate that NGFPs appearing in gravity-matter systems where the matter content is close to that of the Standard Model are compatible with cosmological data. Interestingly, a negative fixed point value of the dimensionless cosmological constant is essential for these findings.

---

## Historical Context

Asymptotic safety in quantum gravity is an alternative to string theory and loop quantum gravity. The idea, developed by Weinberg in the 1970s and revived in recent years, proposes that gravity is renormalizable (UV-finite) despite being non-renormalizable in the traditional sense.

The mechanism relies on a non-Gaussian fixed point (NGFP) in the renormalization group flow of Newton's constant and the cosmological constant. At this fixed point, the couplings approach finite values in the ultraviolet (UV), protecting the theory from divergences.

This paper applies this framework to early-universe cosmology: the NGFP-driven inflation uses the RG flow itself to generate inflationary dynamics. As the universe cools from Planck scales, the RG evolution of couplings naturally produces a period of acceleration (inflation).

---

## Key Arguments and Derivations

### Non-Gaussian Fixed Point (NGFP)

In asymptotic safety, the RG flow of the effective gravitational action includes:

$$S_{\text{eff}} = \int d^4x \sqrt{g} \left[ \frac{Z_N}{16\pi G(\mu)} R - \Lambda(\mu) \right]$$

where G(mu) and Lambda(mu) are running couplings, and mu is the RG scale. The beta functions at the NGFP satisfy:

$$\beta_g^* = 0, \quad \beta_\lambda^* = 0$$

at some values g* and lambda*. The stability matrix gamma_ij describes the flow near the fixed point:

$$\frac{d}{d \ln \mu} \delta g_i = \gamma_{ij} \delta g_j$$

For a UV-attractive NGFP (relevant for UV completion), the critical exponents are typically 2-3, meaning the couplings approach the fixed point as mu -> infinity.

### RG-Improved Inflation

In the early universe, the effective potential is modified by RG running:

$$V_{\text{eff}}(\phi, \mu) = V(\phi) + \Delta V(\phi, \mu)$$

where Delta V contains loop corrections evaluated at scale mu ~ phi. As the field evolves, the RG scale mu ~ phi changes, effectively modifying the potential shape dynamically.

For NGFP-driven inflation, the Hubble parameter during inflation is determined by the RG flow itself:

$$H^2 \sim \Lambda(\mu) / M_{\text{Pl}}^2$$

As mu decreases (field decays), Lambda(mu) evolves along the RG trajectory, producing the inflationary epoch. The spectral index and tensor-to-scalar ratio depend on the NGFP properties and the matter content.

### Matter Content Sensitivity

The NGFP properties depend on the number and types of fields in the theory. For a Standard Model-like matter sector with:
- 2 scalar Higgs doublets
- 3 generations of leptons and quarks
- SU(3) × SU(2) × U(1) gauge bosons

The beta functions are modified by matter loop contributions. The NGFP fixed point values and critical exponents shift with the matter content.

The authors compute the NGFPs for various matter scenarios and compare predictions to Planck CMB data:
- Scalar spectral index: n_s = 0.968 +/- 0.006
- Scalar power normalization: ln(10^{10} A_s) = 3.062 +/- 0.029
- Tensor-to-scalar ratio: r < 0.11

### Negative Cosmological Constant at Fixed Point

A counterintuitive finding: the NGFP has lambda* < 0 (negative dimensionless CC). This means at the fixed point, the cosmological constant is negative (anti-de Sitter-like). However, during RG evolution away from the fixed point (as the universe expands and mu decreases), Lambda(mu) flows from negative to positive, eventually producing the observed small positive CC today.

This automatic transition from negative to positive CC during cosmic evolution is a key feature:

$$\Lambda(\mu_{\text{early}}) < 0, \quad \Lambda(\mu_{\text{today}}) > 0$$

The flow path in (G, Lambda) space determines the inflation duration and exit conditions.

---

## Key Results

1. **NGFP exists for SM-like matter**: Asymptotically safe gravity coupled to Standard Model fields admits a non-Gaussian fixed point with appropriate stability properties.

2. **Cosmological predictions match observations**: The spectral index, power spectrum normalization, and tensor modes predicted by NGFP-driven inflation are compatible with Planck 2015 data.

3. **Matter content determines NGFP properties**: Adding or removing matter fields shifts the fixed point location and critical exponents. SM-like content is singled out as observationally preferred.

4. **Automatic CC sign change**: The RG flow naturally transitions from Lambda < 0 (UV) to Lambda > 0 (IR), resolving some fine-tuning issues in inflation and dark energy.

5. **Critical exponents constrain inflation duration**: The number of e-folds and exit from inflation depend sensitively on gamma_ij values, which are set by matter content.

6. **Predictive power in field content**: The framework predicts that if new matter fields exist (beyond SM), they would shift the NGFP and render the model incompatible with observations. This constrains BSM physics.

---

## Impact and Legacy

This work demonstrates that asymptotic safety can be applied to early-universe cosmology quantitatively. It shows that gravity alone (without additional inflation field) may be sufficient for inflation if UV completion is asymptotically safe.

The paper influenced research on:
- Alternative inflation mechanisms
- Quantum gravity effects in early universe
- Connections between fundamental physics and CMB observations
- Matter content determination from cosmology

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework uses spectral geometry (Dirac operator, heat kernel) to determine physics. The connection to asymptotic safety is:

1. **UV completion from geometry**: Just as asymptotic safety provides UV completion of gravity, spectral geometry provides a fundamental UV description of the Standard Model. Both avoid infinities through geometric mechanisms.

2. **RG flow and spectral action**: The spectral action is the leading-order heat-kernel expansion of the Dirac operator. Its RG evolution (via Callan-Symanzik equation) parallels the RG flow of asymptotic gravity.

3. **Inflation mechanism**: Both frameworks propose inflation from fundamental physics (NGFP for asymptotic safety, internal compactification dynamics for phonon-exflation) without exotic inflaton fields.

4. **Matter content sensitivity**: Asymptotic safety shows that matter content determines UV behavior (NGFP properties). Phonon-exflation similarly encodes matter content in SU(3) fiber structure.

5. **Difference in approach**: Asymptotic safety uses perturbative RG near a fixed point. Phonon-exflation uses non-perturbative spectral geometry. Both may be complementary paths to understanding UV physics.

The frameworks could potentially be unified: phonon-exflation's SU(3) spectral geometry might be the UV-fixed-point structure underlying asymptotic safety for matter coupled to gravity.
