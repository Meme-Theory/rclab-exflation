# DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints

**Authors:** DESI Collaboration (lead authors: A. G. Adame et al.)

**Year:** 2025

**Journal:** Physical Review D, vol. 112, no. 8, article 083515; arXiv:2503.14738

---

## Abstract

The Dark Energy Spectroscopic Instrument (DESI) Data Release 2 (DR2) presents baryon acoustic oscillation (BAO) measurements from spectroscopic redshift surveys of over 14 million galaxies and quasars, combined with Lyman-alpha forest (Ly-alpha) measurements from previous results. The BAO scale is a standard ruler imprinted in the matter power spectrum by acoustic oscillations in the early universe. This paper reports precise distance-redshift measurements across the redshift range 0.3 < z < 4.0, constraining the cosmic expansion history and testing the dark energy equation of state. The results show mild (2.3-2.5σ) tension with CMB predictions from Planck, increased preference for dynamical dark energy compared to ΛCDM, and refinement of constraints on modified gravity and curvature.

---

## Historical Context

Baryon acoustic oscillations were first identified by Sunyaev-Zeldovich and Silk in the 1960s as imprints of sound wave oscillations in the early universe photon-baryon fluid. These oscillations, driven by the competition between gravity (trying to collapse perturbations) and radiation pressure (trying to expand them), create a characteristic scale in the matter power spectrum at:

$$k_{\text{BAO}} \approx 0.05 \text{ Mpc}^{-1} \quad \text{(or } \lambda_{\text{BAO}} \approx 150 \text{ Mpc)}$$

The BAO scale at the recombination epoch is calibrated by measurements of the CMB's acoustic peaks. When we observe BAO in the matter distribution at later times (z ~ 0.5-3), the scale is redshifted and geometrically distorted by the expansion history, allowing us to measure distances at those redshifts.

The SDSS Baryon Oscillation Spectroscopic Survey (BOSS; 2010-2014) first definitively detected BAO in galaxy clustering. DESI (2021-2026) represents a factor of ~10 increase in target density and photometric depth, enabling the first precision measurements of BAO across the full redshift range where galaxies are accessible.

**Motivation for DR2 (March 2025)**: After two years of operations (2022-2024), DESI had collected sufficient redshifts to produce cosmologically meaningful constraints. DR2 includes:
- 8 million galaxy redshifts (vs. 5 million in DR1)
- 4 million quasar redshifts (new in DR2)
- 2 million Ly-alpha forest measurements
- Extended redshift coverage to z ~ 4 (primordial universe epoch)

---

## Key Arguments and Derivations

### BAO as a Standard Ruler

The BAO scale is determined by the sound speed in the baryon-photon plasma at recombination:

$$c_s = \frac{c}{\sqrt{3(1 + R_b)}}$$

where $R_b = 3 \rho_b / (4 \rho_\gamma)$ is the baryon-to-photon density ratio (R_b ~ 0.6 at decoupling). Solving the linear perturbation equations in the radiative era, the sound horizon at decoupling is:

$$r_s = \int_0^{a_{\text{dec}}} \frac{c_s}{aH} da \approx 147.6 \text{ Mpc}$$

This is the "standard ruler" imprinted in the matter power spectrum. In a linearly expanding universe (matter dominated), perturbations oscillate with wavelength ~2π r_s. At recombination (z ~ 1090), these oscillations freeze into the matter distribution.

At lower redshifts, the BAO scale appears at physical separations (in comoving coordinates):

$$\ell_{\text{BAO}}(z) = \frac{r_s}{D_M(z)} \Delta \theta$$

where $D_M(z) = (1+z)^{-1} \int_0^z dz' / H(z')$ is the comoving distance, and $\Delta \theta$ is the angular separation. By fitting the two-point correlation function $\xi(r)$ or power spectrum $P(k)$ in redshift slices, we extract the apparent BAO scale at each z, which depends on the expansion history H(z).

### Distance-Redshift Relation and Expansion History

The comoving distance to redshift z is:

$$D_C(z) = c \int_0^z \frac{dz'}{H(z')}$$

For a flat FRW universe with matter and dark energy:

$$H(z) = H_0 \sqrt{\Omega_m (1+z)^3 + (1-\Omega_m) f_{\text{DE}}(z)}$$

where $f_{\text{DE}}(z)$ describes the dark energy evolution. For ΛCDM, $f_{\text{DE}}(z) = 1$ (constant). For dynamical dark energy:

$$f_{\text{DE}}(z) = \exp\left(3 \int_0^z \frac{1+w(z')}{1+z'} dz'\right)$$

where $w(z) = p_{\text{DE}} / \rho_{\text{DE}}$ is the dark energy equation of state. Measuring $D_C(z)$ via BAO at multiple z allows us to constrain both $\Omega_m$ and the functional form of w(z).

### DESI DR2 Measurement Pipeline

The DESI collaboration measures BAO by fitting the galaxy correlation function:

$$\xi(r) = \int_0^\infty \frac{dk k^2}{2\pi^2} P_{\text{lin}}(k) j_0(kr)$$

in redshift-space distortion (RSD) bins. The measured correlation function has a peak near r ~ 150 Mpc (the BAO scale), which is sharpened by using reconstruction techniques (Eisenstein et al. 2007) that undo non-linear mode-coupling and redshift-space distortions.

The BAO scale measurement is performed via "two-step" fitting:

**Step 1**: Fit the monopole $\xi_0(r)$ to extract the isotropic BAO scale $\alpha_{\text{iso}} = D_C(z) / D_C(z_{\text{fid}})$, where $z_{\text{fid}}$ is a fiducial redshift.

**Step 2**: Fit the quadrupole $\xi_2(r)$ to extract the anisotropic scaling $\alpha_\parallel = H(z_{\text{fid}}) / H(z)$ and $\alpha_\perp = D_C(z) / D_C(z_{\text{fid}})$.

From these, the distance-redshift relation is extracted. Combining across multiple redshift bins and galaxy samples (LRGs, ELGs, QSOs) yields a measurement of $D_M(z)$ at 8 effective redshifts spanning 0.3 < z < 4.0.

### Cosmological Parameter Inference

The DESI DR2 paper fits standard ΛCDM and extended models using Bayesian inference:

$$P(\theta | \text{data}) \propto L(\text{data} | \theta) P(\theta)$$

where $\theta = \{\Omega_m h^2, \Omega_b h^2, H_0, n_s, \sigma_8, \text{etc.}\}$ are cosmological parameters. The likelihood is:

$$-2 \ln L = (\mathbf{D} - \mathbf{M}(\theta))^T \mathbf{C}^{-1} (\mathbf{D} - \mathbf{M}(\theta))$$

where $\mathbf{D}$ is the BAO data (distance measurements), $\mathbf{M}(\theta)$ is the model prediction, and $\mathbf{C}$ is the covariance matrix (including correlations between redshift bins).

For ΛCDM:

$$H(z) = H_0 \sqrt{\Omega_m (1+z)^3 + \Lambda}$$

with $\Omega_\Lambda = 1 - \Omega_m$. The best-fit parameters from DESI DR2 BAO alone are:

$$\Omega_m = 0.312 \pm 0.009, \quad H_0 = 68.5 \pm 1.2 \text{ km/s/Mpc}$$

**Tension with Planck**: Planck's CMB measurements give $\Omega_m = 0.315 \pm 0.007$ and $H_0 = 67.4 \pm 0.5$. DESI prefers slightly lower Omega_m and higher H_0, a ~2.3σ discrepancy.

### Evidence for Dynamical Dark Energy

Extending to dynamical dark energy with $w(z) = w_0 + w_a (1-a) = w_0 + w_a z/(1+z)$:

$$H(z) = H_0 \sqrt{\Omega_m (1+z)^3 + (1-\Omega_m) (1+z)^{3(1+w_0+w_a)} \exp(-3w_a z/(1+z))}$$

DESI DR2 combined with Pantheon+ Type Ia supernovae and Planck CMB (but NOT Planck BAO, which correlates with DESI) yields:

$$w_0 = -0.75 \pm 0.08, \quad w_a = -1.05 \pm 0.45$$

This is **2.8σ away from the ΛCDM prediction** ($w_0 = -1, w_a = 0$). The probability that ΛCDM is the correct model, given the combined data, is Δχ² ~ -5.5 (negative log-likelihood ratio), corresponding to ~4% likelihood vs. the dynamical DE model.

Alternatively, if we restrict to $w_a = 0$ (CPL parameterization with no evolution):

$$w = -0.76 \pm 0.06$$

is **2.5σ away from w = -1**.

---

## Key Results

1. **Precise BAO Distance Measurements**: DESI DR2 measures the comoving distance D_C(z) at 8 effective redshifts from z=0.3 to z=4.0 with statistical precision of 0.5-2%, and systematic uncertainty of 0.4-1.2%, depending on redshift.

2. **Tension with Planck**: DESI BAO+SNe prefer parameters (Omega_m ~ 0.31, H_0 ~ 68.5 km/s/Mpc) that are in mild (2.3-2.5σ) tension with Planck's CMB measurements, suggesting possible early dark energy, evolving dark energy, or unaccounted systematics.

3. **Dynamical Dark Energy Signal**: Combining DESI DR2 with Pantheon+ supernovae and Planck CMB yields **2.8σ preference for w != -1** (evolving dark energy over ΛCDM). The best-fit equation of state is w_0 ~ -0.75, w_a ~ -1.05, indicating dark energy that is more negative (phantom-like) than the cosmological constant.

4. **Consistency with Type Ia Supernovae**: The distance-redshift relation measured by DESI BAO is consistent with (but prefers lower values of) the distance moduli measured by Pantheon+ Type Ia SNe at overlapping redshifts (0.5 < z < 1.0).

5. **Constraints on Curvature**: In models allowing non-zero spatial curvature, DESI DR2 constrains $\Omega_k = 0.001 \pm 0.003$ (consistent with flatness to 0.3σ).

6. **Modified Gravity Tests**: Under the assumption of general relativity with modified gravity (parameterized by growth rate $f\sigma_8$), DESI constrains the growth index $\gamma \approx 0.55 \pm 0.05$, consistent with GR ($\gamma_{\text{GR}} = 0.545$) and constraining scalar-tensor and f(R) models.

7. **Ly-alpha Forest BAO**: The Ly-alpha forest BAO measurement at high redshift (z ~ 2.4) is consistent with DESI galaxy measurements, extending the BAO constraint to the matter-dominated era and improving the leverage on the expansion history.

---

## Impact and Legacy

DESI DR2 represents a watershed in observational cosmology:

- **Post-ΛCDM Era**: The first major survey-based evidence (>2.5σ) for evolution in the dark energy equation of state, moving beyond simple ΛCDM
- **Tension Resolution Path**: The Hubble tension (H_0 discrepancy between CMB and local measurements) may be partially resolved if early dark energy or time-varying Lambda is present
- **Precision Cosmology Maturation**: Distance measurements now reach 0.5-1% statistical precision, comparable to cosmic microwave background
- **Data-Driven Model Testing**: DESI enables falsification of specific dark energy models (quintessence, k-essence, modified gravity) via the time-dependence of w(z)

DESI DR2 is the most constraining BAO measurement to date and has set the stage for a global cosmological parameter estimation, with implications for fundamental physics (quantum field theory, quantum gravity, string theory).

---

## Connection to Phonon-Exflation Framework

**CRITICAL FALSIFICATION GATE.**

The phonon-exflation framework predicts:

$$w = -1 + O(10^{-29})$$

(exact cosmological constant, with corrections appearing only at the Planck scale and beyond the observational reach of any near-future survey).

**DESI DR2 Observation**:

$$w_0 = -0.75 \pm 0.08 \quad \text{(2.5σ away from w = -1)}$$

**Status**: The framework's prediction of w = -1 is **under severe tension with DESI DR2**.

**Framework's Interpretation Options**:

1. **Spectral Action is Wrong**: The spectral action (monotonically increasing with tau) is not the correct functional for the dark energy potential. This aligns with Session 37-38 findings that the spectral action has no minimum (dead route). If dark energy is driven by the instanton gas (not the spectral action), then w could evolve with the instanton density.

2. **Instanton-Driven Dynamical DE**: If the dark energy is generated by the time-dependent instanton density during the Kibble-Zurek transition, then w(z) evolves naturally. Computing the instanton density as a function of cosmological time could yield predictions compatible with DESI.

3. **Systematics in DESI**: If DESI's measurement of w is biased (e.g., by unaccounted lensing from the tessellation structure, as hypothesized in S42), the observed w != -1 could be an artifact. However, DESI's systematic error budget is 0.4-1.2%, not enough to absorb a 2.5σ deviation.

4. **New Physics Beyond Framework**: The observed w != -1 could indicate physics beyond the phonon-exflation picture (e.g., coupled dark energy, scalar-tensor gravity, extra dimensions with evolving moduli).

**Immediate Action Required**:

The framework needs to decide whether:
- **Path A** (Spectral Action): Recompute the spectral action to include Kibble-Zurek corrections or instanton-gas contributions, allowing w != -1
- **Path B** (Pure Instanton Gas): Abandon the spectral action as the dark energy driver and model dark energy entirely via the time-dependent instanton density
- **Path C** (Concede Failure): Acknowledge that the w = -1 prediction is falsified and the framework requires substantial revision

As of Session 43 (current), the framework is at the decision point. DESI DR2 has raised the bar significantly.

