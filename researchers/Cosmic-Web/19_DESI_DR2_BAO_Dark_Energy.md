# DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints

**Author(s):** DESI Collaboration (Adame et al., many co-authors)
**Year:** 2025
**Journal:** Physical Review D, Volume 112, Issue 8, arXiv:2503.14738
**Key Dates:** Submitted 2025-03-18, Published 2025-03

---

## Abstract

The DESI Data Release 2 (DR2) presents baryon acoustic oscillation (BAO) measurements from more than 14 million galaxies and quasars, obtained during the first three years of DESI observations. These measurements probe the distance-redshift relation across a redshift range z ~ 0.1 to z ~ 1.5, providing unprecedented precision constraints on cosmic expansion and dark energy. The BAO scale is measured to ~0.24% statistical precision, representing a factor of ~2 improvement over DR1 and the largest spectroscopic BAO dataset compiled to date. When combined with Planck CMB measurements, the DESI DR2 BAO data show a mild 2.3-sigma tension with ΛCDM-preferred parameters, with dynamical dark energy (w0wa parametrization) preferred over ΛCDM at 3.1-sigma significance. The data suggest evolution in the dark energy equation of state, with w0 > -1 (quintessence-like today) and wa < 0 (suggesting transition from phantom-dominated past). Upper limits on the sum of neutrino masses are derived: Σm_ν < 0.064 eV (ΛCDM) and Σm_ν < 0.16 eV (w0wa model).

---

## Historical Context

The baryon acoustic oscillation technique, pioneered in the early 2000s, emerged as a crucial standard ruler for measuring cosmic expansion. The physics stems from sound waves propagating through the primordial baryon-photon plasma before recombination: these waves freeze in at decoupling, leaving an imprint on galaxy clustering statistics. Unlike supernovae (which measure luminosity distance), BAO measures the sound horizon directly, making it fundamentally sensitive to the expansion history integrated from recombination to observation.

For decades, BAO measurements came from spectroscopic surveys with limited sample sizes (SDSS, 2dF) or photometric surveys with modest precision. DESI represents a transformational leap: it is a massively multiplexed spectrograph capable of obtaining ~5000 simultaneous spectra. The instrument's science goal is to observe ~35 million spectra of galaxies and quasars over 5 years, making it the largest spectroscopic survey ever assembled. DR2, representing three years of data, already surpasses all prior spectroscopic BAO measurements.

The existential importance of DR2 for the phonon-exflation framework lies in a single observable: **the measured dark energy equation of state w.** The phonon-exflation framework predicts that cosmic acceleration arises from the monotonic evolution of a spectral action (the Dirac operator spectrum of the internal space M4 x SU(3)). This evolution implies w = -1 + O(10^{-29}), meaning deviations from w = -1 must be sub-percent at best, and more realistically unobservable. Yet DESI DR2 reports:

- w0 = -0.72 +/- 0.08 (favoring w0 > -1, i.e., quintessence-like current equation of state)
- wa = -0.65 +/- 0.40 (suggesting phantom behavior in the past, crossing -1 near z ~ 0.5)
- Joint significance of dynamical dark energy over ΛCDM: 3.1-sigma

This is the first high-confidence observational evidence that the dark energy density parameter may not be a true cosmological constant. For a framework predicting w ≈ -1.000...0001, this result is either (a) the opening of a new observational window onto physics beyond the standard model, or (b) a decisive falsification.

---

## Key Arguments and Measurements

### Baryon Acoustic Oscillation Technique

The BAO method exploits a "standard ruler" — the sound horizon at the epoch of recombination, **r_s** ≈ 150 Mpc. This scale is imprinted in the two-point correlation function of matter density:

$$\xi(r) = \int_0^\infty \frac{dk}{2\pi^2} P(k) j_0(kr)$$

where P(k) is the power spectrum and j_0 is the spherical Bessel function. Recombination leaves a sharp acoustic peak in ξ(r) at r ≈ r_s, corresponding to the maximum distance a sound wave travels before being damped.

Galaxies preferentially cluster at separations near r_s (because density perturbations at the sound horizon grow preferentially), creating a BAO peak in the two-point correlation function of observed galaxy positions. When galaxies are mapped to comoving distances using their redshift, the peak shifts due to the expansion history:

$$r_{\text{obs}} = \frac{D_M(z)}{D_M(z_{\text{fiducial}})} r_{\text{true}}$$

where D_M(z) is the comoving distance at redshift z. By measuring the shift of the BAO peak as a function of redshift, one directly constrains D_M(z).

### DESI DR2 Geometry and Sample Composition

DESI observed galaxies and quasars across redshift ranges:

- **Luminous red galaxies (LRGs):** z ~ 0.4 to 1.0, number density ~10^{-4} h^3 Mpc^{-3}
- **Emission line galaxies (ELGs):** z ~ 0.6 to 1.1, enabling access to lower redshifts than previous surveys
- **Quasars:** z ~ 0.8 to 2.1, extending BAO measurements to high redshift
- **Lya forest:** z ~ 2.0 to 4.4 (Lya-quasar pairs), probing early cosmic history

Total sample: >14 million objects with secure spectroscopic redshifts.

### DESI DR2 Cosmological Measurements

The comoving distance measurements are reported at multiple redshift bins:

**In the w0wa parametrization** (dark energy equation of state w(a) = w0 + wa(1-a), where a is scale factor):

- **Best-fit w0:** -0.72 +/- 0.08 (68% CL)
- **Best-fit wa:** -0.65 +/- 0.40 (68% CL)
- **Significance of dynamical DE over ΛCDM:** 3.1-sigma (when combined with Planck)

This is interpreted as:
- Current dark energy behaves like quintessence (w0 > -1), contrary to the cosmological constant
- Past dark energy was phantom-like (w < -1), suggesting a crossing of the phantom divide near z ~ 0.5

### Baryon Acoustic Oscillation Precision

The BAO scale is reported at multiple redshifts with unprecedented precision:

- **Combined BAO constraint:** Δr_BAO/r_BAO ~ 0.24% (68% CL)
- **Comparison to SDSS:** ~6x improvement in precision
- **Consistency with DR1:** DESI DR2 is fully consistent with and supersedes DESI DR1 measurements

The BAO measurement is performed through a power-spectrum analysis, measuring the distance scale in both the radial (line-of-sight) and transverse directions:

$$\alpha_\parallel = \frac{D_M(z) \Delta z}{D_M(z_{\text{fid}}) \Delta z_{\text{fid}}}$$

$$\alpha_\perp = \frac{D_A(z)}{D_A(z_{\text{fid}})}$$

where D_A is the angular diameter distance. These constraints directly probe the expansion rate H(z) and angular size evolution.

### Neutrino Mass Constraints

The enhanced statistical power of DESI DR2 enables tighter constraints on the sum of neutrino masses, a key parameter linking particle physics to cosmology:

- **ΛCDM:** Σm_ν < 0.064 eV (95% CL) — approaching sensitivity to the normal hierarchy floor (0.06 eV)
- **w0wa model:** Σm_ν < 0.16 eV (95% CL) — broader when allowing dark energy freedom

These constraints are particularly important for neutrino physics, as they constrain whether the neutrino mass hierarchy is normal (sum ~0.06 eV) or inverted (sum ~0.10 eV).

### Tension with CMB

A key finding is the emergence of persistent tension between BAO/geometry and CMB measurements:

- **2.3-sigma tension** on the Hubble parameter H0 between BAO/SN/lensing combination and Planck
- Planck acoustic angular scale $\theta_s$ and BAO scale agree, but the inferred expansion rate H0 differs

This suggests either (a) systematics in one dataset, (b) local inhomogeneity reducing H0 in our neighborhood, or (c) new physics affecting the late-time expansion.

---

## Key Results

1. **DESI DR2 provides the largest spectroscopic BAO dataset to date** (14+ million objects), with 0.24% precision on the sound ruler — a 2x improvement over DR1.

2. **Dynamical dark energy is favored over ΛCDM at 3.1-sigma** when combining DESI BAO with Planck CMB, with w0 ~ -0.72 (quintessence today) and wa ~ -0.65 (phantom in past).

3. **The dark energy equation of state crosses w = -1 near z ~ 0.5**, transitioning from phantom (w < -1 at high z) to quintessence (w > -1 at low z). This "phantom crossing" violates several quantum gravity no-go theorems and is disfavored in string theory constructions.

4. **Neutrino mass limits approach the normal hierarchy threshold:** Σm_ν < 0.064 eV in ΛCDM, beginning to discriminate between mass orderings.

5. **Mild 2.3-sigma tension persists with Planck CMB** on the expansion rate H0, hinting at possible new physics or unaccounted systematics.

6. **Consistency with standard inflation:** The measurements support the inflationary prediction of a nearly scale-invariant power spectrum and spatial flatness, ruling out many exotic early-universe models.

---

## Impact and Legacy

DESI DR2 represents a watershed moment for late-time cosmology and dark energy constraints. Prior to DESI, dark energy constraints came primarily from type Ia supernovae (distance measurements) and weak gravitational lensing (growth rate). BAO is fundamentally different: it measures the expansion history directly via a physics-independent standard ruler.

The emergence of dynamical dark energy at 3.1-sigma is significant for several reasons:

1. **It is the first high-confidence hint that w ≠ -1.** While not yet a discovery (3.1-sigma is >2-sigma but below the >5-sigma discovery threshold in particle physics), it opens the possibility of observational windows into dark energy dynamics.

2. **It creates a tension with fundamental theory.** General relativity + quantum field theory do not naturally predict time-evolving dark energy; ΛCDM (w = -1 always) is the simplest solution. Any dynamical dark energy requires either (a) a scalar field with a specific potential, (b) modifications to gravity, or (c) breakdown of the cosmological principle.

3. **It may be the key to the Hubble tension.** If dark energy evolved more slowly in the past, the inferred expansion rate at early times (from acoustic measurements) would differ from late-time H0 measurements, resolving some of the tension with CMB.

The DESI collaboration will release more data in subsequent years (DR3, DR4, DR5), which should clarify whether the dynamical dark energy signal is robust or a statistical fluctuation.

---

## Connection to Phonon-Exflation Framework

**Status: CRITICAL CONSTRAINT / EXISTENTIAL THREAT**

The phonon-exflation framework makes a precise prediction for the dark energy equation of state:

$$w_{\text{exflation}} = -1 + \frac{d \log S_{\text{spec}}}{d \log a} \cdot O(\epsilon_{\text{slow}})$$

where S_spec is the spectral action and ε_slow parametrizes departures from instantaneous spectral equilibrium. Given the monotonic structure of the spectral action across all redshifts (established in Session 36-37 closure), the framework predicts:

$$w_{\text{theory}} = -1 \pm O(10^{-29})$$

DESI DR2 reports w0 = -0.72 +/- 0.08, a deviation of **~3.5 sigma** from the predicted w ≈ -1.000...0001.

**Four possible resolutions:**

1. **Observational reassessment (least likely):** DESI systematics unaccounted; dynamical dark energy signal is a false positive. Future DESI DR3/DR4 data should sharpen this.

2. **Lensing bias (moderate likelihood):** The 32-cell tessellation of the cosmic void structure creates an apparent w ≠ -1 through differential magnification bias (PI hypothesis from Session 42). This would make w > -1 an artifact of observational geometry, not true physics.

3. **Non-monotonic spectral action (moderate-high likelihood):** The framework's assumption of monotonic evolution may fail at low redshifts (z < 0.5). This would require non-perturbative corrections to the spectral action or a breakdown of the single-field approximation.

4. **Framework falsification (high likelihood if other options exhaust):** The phonon-exflation mechanism may be incorrect, and the universe operates via ΛCDM, quintessence, or a modified gravity theory. The monotonic spectral action prediction would be a theoretical artifact with no cosmological realization.

**Action items:**
- Check DESI raw data for lensing bias correlations with large-scale structure (z ~ 0.5 void patterns).
- Examine whether non-monotonic corrections to the spectral action (e.g., from instanton back-reaction, Session 38) could change the dynamics at low z.
- If dynamical dark energy is confirmed by DR3/DR4, the framework must either pivot to a new mechanism or concede falsification.

This paper is **required reading** for all framework agents. It is the primary observational test of the phonon-exflation prediction.
