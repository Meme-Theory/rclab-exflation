# Constraints on Lorentz Invariance Violation from Rest-Frame Spectral Lags

**Author(s):** Multiple authors (lead: updated Fermi LAT collaboration analysis)
**Year:** 2025
**Journal:** MDPI Universe 11(6), 183

---

## Abstract

The spectral lag technique — measuring the delay between arrival times of low-energy and high-energy photons in gamma-ray bursts — remains one of the most direct tests of Lorentz invariance violation (LIV). This paper presents an updated analysis using 56 GRBs observed by the Fermi Large Area Telescope (LAT) with improved data processing, energy calibration, and statistical methods. Particular attention is paid to correcting for intrinsic spectral-lag correlations from the GRB source physics (jet dynamics, emission mechanisms) to isolate genuine propagation delays from LIV. The analysis yields constraints on the linear LIV scale to $\Lambda_1 > 1.2 \times 10^{18}$ GeV and quadratic LIV to $\Lambda_2 > 3.8 \times 10^{18}$ GeV at 90% CL, consistent with prior limits and ruling out a broad parameter space of quantum gravity models.

---

## Historical Context

The spectral lag is a simple but powerful concept: in a GRB, low-energy and high-energy photons are generally emitted simultaneously at the source. If spacetime is continuous and Poincare-invariant, they arrive at Earth within microseconds of each other (given the GRB duration, which is seconds to minutes).

However, if Lorentz invariance is violated, high-energy photons travel at a different speed:

$$v_\gamma(E) = c \left(1 - \frac{E}{\Lambda_n}\right)$$

A photon of energy $E_{\text{high}} = 10$ GeV and one of $E_{\text{low}} = 100$ keV will be delayed by:

$$\Delta t = \frac{d}{c} \cdot \frac{\Delta E}{\Lambda_1} = \frac{d}{c} \cdot \frac{(10 \text{ GeV} - 100 \text{ keV})}{\Lambda_1}$$

For a source at redshift $z = 1$ (distance $d \sim 3$ Gpc), this delay can be seconds — observable with timing-sensitive detectors.

Early analyses (e.g., Amelino-Camelia et al., 2010s) used single bright GRBs. This paper scales the approach by applying it to a **sample of 56 bursts**, averaging over source properties to extract the constraint more robustly.

---

## Key Arguments and Derivations

### Spectral Lag Definition

The spectral lag is defined in reference to a light curve binned by energy. For a given energy range $[E_1, E_2]$, one measures the peak arrival time $t_{\text{peak}}(E)$ of the light curve in that band. The spectral lag relative to a reference energy $E_0$ is:

$$\Delta t_{\text{lag}}(E) = t_{\text{peak}}(E) - t_{\text{peak}}(E_0)$$

In standard GRB emission (inverse Compton, synchrotron), the spectral lag depends on the acceleration of electrons and the magnetic field structure — this is **intrinsic** to the burst. However, an additional lag from LIV propagation adds linearly:

$$\Delta t_{\text{lag}}^{\text{obs}}(E) = \Delta t_{\text{lag}}^{\text{intrinsic}}(E) + \Delta t_{\text{lag}}^{\text{LIV}}(E)$$

The LIV contribution is:

$$\Delta t_{\text{lag}}^{\text{LIV}}(E) = \frac{d(z)}{c} \left[\frac{E}{\Lambda_1} + \frac{E^2}{\Lambda_2^2} + \ldots\right]$$

where $d(z)$ is the comoving distance to redshift $z$.

### Source Physics Correction

The challenge is disentangling the intrinsic lag from the LIV lag. The paper uses several methods:

**Method 1: Multi-wavelength correlation**

For GRBs with simultaneous X-ray and optical observations, the intrinsic spectral lag can be independently estimated using lower-energy data (X-ray to optical). The assumption is that if the intrinsic lag is small in the X-ray band, it is also small in the GeV band — a reasonable assumption if the burst's bulk Lorentz factor (which determines the cooling timescale and hence the intrinsic lag) is constant across frequencies.

The authors model:
$$\Delta t_{\text{intrinsic}}(E) = a_0 + a_1 \log(E / 100 \text{ keV}) + a_2 [\log(E)]^2$$

and fit $a_0, a_1, a_2$ using X-ray data, then extrapolate to GeV energies.

**Method 2: Ensemble average**

If the intrinsic lag has significant event-to-event scatter (due to varying jet properties), then averaging over many bursts should suppress the intrinsic contribution relative to the LIV contribution, which is the same for all bursts from the same distance.

The paper defines the **mean spectral lag** across 56 bursts:

$$\langle \Delta t_{\text{lag}} \rangle = \frac{1}{56} \sum_{i=1}^{56} \Delta t_{\text{lag}}^{(i)}$$

If intrinsic lags are drawn from a distribution with mean zero and scatter $\sigma_{\text{intrinsic}}$, the scatter of the ensemble mean is reduced by $\sqrt{56}$, improving LIV sensitivity.

**Method 3: Energy-dependence model**

The intrinsic lag's energy dependence is predicted by GRB theory. For synchrotron emission:

$$\Delta t_{\text{intrinsic}} \propto (E / E_{\text{peak}})^{-p}$$

where $p \approx 0.3$–$0.7$ (the photon index). The LIV contribution, by contrast, is **linear** in energy (for $\Lambda_1$) or **quadratic** (for $\Lambda_2$).

The paper fits both components simultaneously:

$$\Delta t_{\text{lag}}^{\text{obs}} = a (E / 100 \text{ keV})^{-p} + \frac{d(z)}{c} \frac{E}{\Lambda_1}$$

where $a$ and $p$ are nuisance parameters specific to each burst, and $\Lambda_1$ is the LIV scale (same for all bursts, fitted globally).

### Redshift Dependence

Since $d(z) = c \int_0^z \frac{dz'}{H(z')}$ (comoving distance), the LIV signal grows with redshift. The paper uses 56 GRBs spanning $z = 0.3$ to $z \approx 6$, allowing a test of the redshift dependence.

For two bursts at redshifts $z_1$ and $z_2$, the ratio of LIV lags is:

$$\frac{\Delta t_{\text{LIV}}(z_2)}{\ \Delta t_{\text{LIV}}(z_1)} = \frac{d(z_2)}{d(z_1)}$$

The paper performs a **Bayesian hierarchical analysis**, allowing $\Lambda_1$ to vary but imposing a Gaussian prior on its value derived from the redshift scaling. This cross-checks consistency and reduces biases from single-burst systematics.

### Statistical Framework

The global likelihood is:

$$\mathcal{L}(\Lambda_1, \Lambda_2 | \{\Delta t_{\text{lag}}^{(i)}\}) = \prod_{i=1}^{56} \mathcal{L}_i(\Lambda_1, \Lambda_2)$$

where

$$\mathcal{L}_i = \exp\left(-\frac{(\Delta t_{\text{lag}}^{(i)} - \Delta t_{\text{lag}}^{\text{model,}(i)})^2}{2\sigma_i^2}\right)$$

and $\sigma_i$ includes both statistical uncertainty (photon counting statistics) and systematic uncertainty (source model dependence, energy calibration).

The 90% CL lower limit on $\Lambda_1$ is found from the integral:

$$P(\Lambda_1 > \Lambda_1^{90\%}) = 0.9$$

under the posterior distribution $P(\Lambda_1 | \text{data})$.

---

## Key Results

1. **Linear LIV constraint**: $\Lambda_1 > 1.2 \times 10^{18}$ GeV (90% CL).

2. **Quadratic LIV constraint**: $\Lambda_2 > 3.8 \times 10^{18}$ GeV (90% CL).

3. **Consistency with prior analyses**: The 56-burst sample yields limits consistent with early single-burst analyses (e.g., Amelino-Camelia et al. 2015, ~$10^{18}$ GeV), confirming robustness.

4. **High-redshift advantage**: GRBs at $z > 3$ contribute disproportionately to the LIV constraint, due to the large baseline distance. The five highest-redshift bursts ($z \geq 5$) provide ~40% of the constraining power.

5. **Systematic dominance**: The largest systematic uncertainty is the model of intrinsic source lag (±30% uncertainty in $\Lambda_1$). Photon-counting statistics and energy calibration are subdominant.

6. **No energy-dependent anomaly**: The paper searches for residual bias (intrinsic lags correlated with energy in a non-power-law way) and finds none beyond the canonical burst-physics model. This limits the possibility of a systematic mimicking LIV.

---

## Impact and Legacy

The spectral-lag technique remains among the most stringent and straightforward tests of LIV. The 2025 update, leveraging improved Fermi LAT data and refined statistical methods, continues to rule out naive quantum gravity scales (e.g., $E_{\text{QG}} \sim 10^{16}$ GeV) and motivates next-generation detectors (Cherenkov Telescope Array, next-generation gravitational-wave detectors with timing arms).

The paper also highlights the importance of **multi-messenger** approaches: combining Fermi LAT (GeV-scale timing), ground-based Cherenkov arrays (TeV-scale), and neutrino/gravitational-wave observations provides complementary constraints across energy scales and test different aspects of potential LIV.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model assumes **exact Lorentz invariance** in the external 4D spacetime $M^4$. The spectral-lag analysis provides an **empirical validation** of this assumption at the $10^{-18}$ GeV energy scale.

**Why this matters for the framework**:

1. **Photon dispersion**: If Planck-scale discretization (from the internal $SU(3)$ geometry) leaked into the external spacetime metric, photon propagation would be modified. The absence of LIV in GRBs up to $\Lambda_1 \sim 10^{18}$ GeV rules out such "leakage" at a 10-order-of-magnitude level.

2. **Hierarchy and decoupling**: The framework's success depends on the internal degrees of freedom (the SU(3) Dirac spectrum, the pairing condensate) remaining **decoupled** from the external geometry at scales below the Planck mass. The spectral-lag constraint validates this decoupling.

3. **Consistency with precision GRB astronomy**: High-redshift GRBs, especially those at $z > 5$ (only possible with the most energetic, rarest bursts), probe distance scales comparable to the Hubble radius. The framework must correctly predict light propagation over such scales, with no LIV corrections — and the data confirm this.

**Reframing**: Instead of saying "Lorentz invariance is fundamental," the framework can equivalently say "the internal compactification is decoupled from the metric tensor" — and spectral-lag GRBs provide **direct empirical evidence** for this decoupling.

