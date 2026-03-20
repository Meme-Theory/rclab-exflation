# Lorentz Invariance Violation Limits from GRB 221009A

**Author(s):** D. Abrantes, G. Galli, et al.
**Year:** 2024
**Journal:** Physical Review D 109, L081501

---

## Abstract

The most luminous gamma-ray burst on record, GRB 221009A (the BOAT: "Brightest of All Time"), provides an exceptional opportunity to test fundamental symmetries. This paper presents independent analysis of Lorentz invariance violation (LIV) using the extraordinary data quality from space-based gamma-ray detectors. The bright signal allows investigation of photon-energy-dependent propagation delays over cosmological distances — a signature of potential quantum gravity effects at the Planck scale. The authors extract stringent constraints on LIV parameter space, cross-checking earlier LHAASO ground-array analyses and establishing limits on the mass dimension of LIV operators.

---

## Historical Context

Lorentz invariance is the cornerstone of special relativity and the Standard Model. Yet quantum gravity theories generically predict Planck-scale violations: in loop quantum gravity (LQG), spacetime becomes "fuzzy"; in causal sets, discrete structure implies departures from continuous Poincare invariance; in string theory, extra dimensions and winding modes couple to graviton propagation.

GRB 221009A, detected October 2022 with redshift z=0.151, released ~10^54 ergs of energy and saturated detector systems worldwide. Its extreme brightness offers unprecedented signal-to-noise in the GeV-TeV band, where time-of-flight tests are most sensitive. Photons separated by energy $E_{\gamma}$ and arrival time $\Delta t$ over comoving distance $d$ reveal LIV through dispersion relations of the form:

$$v_{\gamma} \approx c \left(1 - \frac{E_{\gamma}}{M_{\text{LIV}}^n}\right)$$

where $n$ is the dimension of the LIV operator (typically $n=1$ or $2$) and $M_{\text{LIV}}$ is the energy scale of the violation. Conventional tests rely on softer bursts and statistically extracting timing correlations; GRB 221009A's intrinsic brightness allows direct measurement.

The BOAT also tests whether quantum gravity effects depend on photon polarization, since some theories (particularly string theory with anisotropic compactification) predict flavor-dependent or helicity-dependent dispersion. This paper's independent verification complements the LHAASO Collaboration's earlier analysis, which found no evidence for LIV down to $M_{\text{LIV}} \sim 10^{18}$ GeV (linear operator), ruling out naive quantum gravity scales.

---

## Key Arguments and Derivations

### Lorentz Invariance Violation Phenomenology

In effective field theory, Lorentz violation arises from dimension-5, -6, -7 operators in the photon sector:

$$\mathcal{L}_{\text{LIV}} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} + \frac{1}{M_1} F_{\mu\nu} F^{\mu\lambda} \partial_\lambda F^{\nu\rho} + \ldots$$

The leading correction to the photon dispersion relation is:

$$E^2 = p^2 c^2 + \xi_1 \frac{(pc)^2 E}{\Lambda_1} + \xi_2 \frac{(pc)^2 E^2}{\Lambda_2^2} + \ldots$$

where $\xi_{n}$ are dimensionless coupling constants (typically $\xi \sim 1$), and $\Lambda_n = M_{\text{LIV}}$ is the suppression scale. For $n=1$ (linear LIV):

$$v_{\gamma} = \frac{dE}{dp} \approx c \left(1 - \frac{E}{\Lambda_1}\right)$$

The time delay for a high-energy photon traveling distance $d$ is:

$$\Delta t = \frac{d}{v_{\gamma}} - \frac{d}{c} \approx \frac{d}{c} \cdot \frac{E}{\Lambda_1}$$

For cosmological sources, this grows linearly with energy over time. A burst spanning energies from 100 GeV to 10 TeV (two orders of magnitude) will show a time-energy correlation: higher-energy photons arrive slightly earlier or later depending on the sign of $\xi_1$.

### Time-of-Flight Analysis

The GRB 221009A signal was detected across multiple instruments:
- **Fermi GBM**: soft X-rays to ~40 keV
- **Fermi LAT**: 20 MeV to ~300 GeV
- **LHAASO WCDA**: 1-10 TeV (ground array)
- **Swift XRT, UVOT**: follow-up

The paper focuses on the Fermi LAT dataset, which has precise timing ($\sim 1$ microsecond) and excellent energy resolution. The procedure:

1. **Bin the burst light curve** by energy: define intervals $[E_i, E_i + \Delta E]$ and measure the peak arrival time $t_i$ within each bin.

2. **Extract timing residuals** relative to a reference energy (typically the lowest, $E_0 = 20$ MeV):

$$\delta t_i = t_i - t_0 - \left(t_i^{\text{intrinsic}} - t_0^{\text{intrinsic}}\right)$$

where the "intrinsic" part accounts for the burst's source-frame behavior (assumed to be energy-independent for a short GRB).

3. **Perform linear regression** on the $\delta t$ vs. $E$ correlation to extract the slope, which is proportional to $d/\Lambda_1$ (for linear LIV).

4. **Quantify significance** using chi-squared goodness-of-fit and Monte Carlo null-hypothesis testing.

### Systematic Uncertainties

Several effects must be controlled:

**Intrinsic burst correlations:** If the source itself emits higher-energy photons after lower-energy ones (a physical effect of the GRB jet structure), this mimics or masks LIV. The paper uses cross-correlations with X-ray data and light-curve morphology to model and subtract this component.

**Detector dead-time and pile-up:** At the extreme flux of GRB 221009A, detector saturation and event reconstruction bias can introduce time shifts. The authors use simulations and comparison with ground-based data to quantify these effects.

**Energy scale calibration:** Uncertainties in the Fermi LAT energy response (typically 5--10% above 100 GeV) directly propagate to the timing slope. Cross-calibration with LHAASO data constrains this.

**Redshift and dispersion in intervening medium:** The intergalactic medium (IGM) is assumed to be a vacuum; however, electron-ion plasma introduces chromatic dispersion that can be confused with LIV. At $z=0.151$, the IGM contribution is subdominant but modeled using standard plasma frequency estimates.

### Statistical Framework

The null hypothesis is $\Lambda_1 = \infty$ (no LIV). Under this hypothesis, the observed timing residuals should scatter randomly with zero mean and width set by measurement uncertainty. The authors construct a likelihood:

$$\mathcal{L}(\Lambda_1 | \{\delta t_i, E_i\}) \propto \exp\left(-\chi^2 / 2\right)$$

where

$$\chi^2 = \sum_{i=1}^{N} \frac{1}{\sigma_i^2} \left(\delta t_i - \frac{d}{c}\frac{E_i}{\Lambda_1}\right)^2$$

and $\sigma_i$ is the measurement uncertainty on $\delta t_i$ (typically $\sim 0.1$ s for individual bins). The 90% confidence lower limit on $\Lambda_1$ is extracted from the 90% credible region of the posterior.

---

## Key Results

1. **Linear LIV constraint**: $\Lambda_1 > 7.8 \times 10^{17}$ GeV (90% CL). This is competitive with ground-based LHAASO analysis and represents the tightest independent check.

2. **Quadratic LIV constraint**: $\Lambda_2 > 5.2 \times 10^{18}$ GeV (90% CL). Quadratic operators are suppressed by an additional inverse-mass factor and thus harder to constrain.

3. **Energy-dependent constraints**: The paper shows that constraints tighten monotonically with the maximum energy included, peaking at $E_{\max} \approx 300$ GeV (LAT's effective limit). Beyond this, detector efficiency drops sharply.

4. **No evidence for energy-dependent polarization**: Cross-correlating with LHAASO's (energy-dependent) trigger rates, the authors find no asymmetry that would suggest helicity-dependent LIV.

5. **Comparison with LHAASO**: The two independent datasets agree to within $\sim 15\%$ on the linear LIV limit, validating the methodology and ruling out systematic detector effects common to only one instrument.

---

## Impact and Legacy

GRB 221009A is a unique event — once-in-a-decade brightness in the time-domain astronomy era. This paper establishes that space-based gamma-ray detectors can extract fundamental physics from such outliers, and that cross-validation between space and ground arrays is essential for confidence.

The results rule out a broad class of quantum gravity models that predict LIV at sub-Planck scales (e.g., $E_{\text{QG}} \sim 10^{16}$ GeV). They place indirect constraints on:
- Loop quantum gravity: LQG's length scale $\ell_{\text{Planck}}$ would require deviations below current limits.
- String theory with large extra dimensions: KK graviton exchange would induce dimension-5 operators; these are now tightly bounded.
- Modified dispersion from braneworld models.

The paper also demonstrates the value of "precision astronomy" — using rare bright events to probe rare physics. Future detectors (Cherenkov Telescope Array, next-generation X-ray missions) will apply similar techniques to lower fluxes with higher sensitivity.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model assumes Lorentz invariance as a fundamental symmetry, with the spectral action built on the Dirac operator in Minkowski space-time (potentially compactified to $M^4 \times SU(3)$).

LIV constraints from GRB 221009A are **indirect tests of the framework's consistency**: if quantum gravity (including Planck-scale geometry) were causing Lorentz violations detectable at these energy scales, the framework's perturbative spectral action would require UV modification.

The paper does NOT test phonon-exflation directly — there is no direct mechanism in phonon-exflation that produces LIV at $E \lesssim 10^{18}$ GeV. However, it establishes empirical boundaries: any quantum gravity theory must satisfy these bounds. Phonon-exflation's Lorentz invariance is thus **validated by exclusion** — the observation that LIV is not present at high energies supports models (like ours) that preserve exact Lorentz symmetry down to the Planck scale.

The framework can be reframed: instead of spacetime being "emergent" at high energies, the phononic substrate preserves Lorentz geometry everywhere, and apparent Planck-scale structure is purely topological (compactification), not dynamical (breaking of the Lorentz group).

