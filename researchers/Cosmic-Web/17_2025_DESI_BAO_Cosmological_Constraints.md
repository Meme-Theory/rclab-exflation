# DESI 2024-2025: Cosmological Constraints from the Dark Energy Spectroscopic Instrument

**Author(s):** DESI Collaboration (including Adame et al., Adame et al., and others)

**Year:** 2024-2025

**Journal:** Journal of Cosmology and Astroparticle Physics; Astronomy & Astrophysics

---

## Abstract

The Dark Energy Spectroscopic Instrument (DESI) represents the state-of-the-art galaxy redshift survey, measuring spectra for ~14 million galaxies and quasars. DESI's early data releases (2024-2025) provide precision measurements of baryon acoustic oscillations, redshift-space distortions, and large-scale structure. These results constrain cosmological parameters (matter density $\Omega_m$, dark energy equation of state $w$, Hubble constant $H_0$) to unprecedented precision, while also revealing tensions with other measurements (S8 tension, H0 tension) that challenge ΛCDM and motivate new physics.

---

## Historical Context

DESI began operations in 2020 and has been systematically obtaining spectra for unprecedented numbers of galaxies. The 2024-2025 data releases represent the first major cosmological results from DESI, providing independent constraints on dark energy and structure growth that are already reshaping cosmological inference.

---

## Key Arguments and Derivations

### Baryon Acoustic Oscillations at Multiple Redshifts

DESI's primary targets include:
- **Luminous Red Galaxies (LRGs)**: Massive, red galaxies out to z ~ 1
- **Emission Line Galaxies (ELGs)**: Star-forming galaxies out to z ~ 1.6
- **Quasars**: High-redshift tracers to z ~ 3.5

For each sample, DESI measures the two-point correlation function or power spectrum and extracts the BAO peak position. By measuring BAO at multiple redshifts, one constrains the expansion history $H(z)$:

$$d_c(z) = c \int_0^z \frac{dz'}{H(z')}$$

The BAO scale is a standard ruler set in the early universe. Comparing the observed BAO scale to theoretical predictions constrains the comoving distance to each redshift, directly measuring the expansion history.

**DESI early results**:
- **LRGs (z ~ 0.5)**: BAO distance scale measured to 0.3% precision
- **ELGs (z ~ 1.1)**: BAO distance scale measured to 0.4% precision
- **Quasars (z ~ 2.3)**: BAO distance scale measured to 0.6% precision

Combined with prior information from the CMB, these measurements tightly constrain $\Omega_m$ and $w$.

### Redshift-Space Distortions and Growth Rate

In redshift space, galaxy distances are inferred from redshifts, which include both cosmological recession and peculiar velocities. This introduces **redshift-space distortions** (RSD) in the correlation function:

$$\xi(r_\perp, r_\parallel) \neq \xi_{\text{real}}(r)$$

The anisotropy encodes the **growth rate** of structure:

$$f = \frac{d \ln D}{d \ln a}$$

where $D(a)$ is the linear growth factor. DESI measures RSD by fitting the correlation function and extracting $f$.

**DESI results on growth rate**:
- Consistent with ΛCDM+GR predictions
- Moderate tension with Planck CMB predictions for $\sigma_8$
- No strong evidence for modified gravity

### Sigma-8 Tension

A lingering tension in cosmology: weak lensing surveys (DES, KiDS) measure $\sigma_8$ lower than CMB predictions. DESI's measurement:

$$\sigma_8 = 0.777 \pm 0.020 \quad \text{(DESI)}$$
$$\sigma_8 = 0.811 \pm 0.006 \quad \text{(Planck CMB)}$$

This ~1.5σ tension remains, though DESI's result is slightly higher than weak lensing, suggesting possible systematics or new physics.

### Hubble Tension

Independent distance measurements (supernovae, Cepheid variables) give:
$$H_0 = 73.0 \pm 1.0 \text{ km/s/Mpc} \quad \text{(Riess et al.)}$$

CMB measurements give:
$$H_0 = 67.4 \pm 0.5 \text{ km/s/Mpc} \quad \text{(Planck)}$$

A ~5σ discrepancy. DESI's measurements of $H(z)$ via BAO and RSD will help constrain this tension. Early DESI results favor the lower (Planck) value slightly, but the tension persists.

### Constraints on Dark Energy Equation of State

By measuring $H(z)$ at multiple redshifts, DESI constrains the dark energy equation of state $w(z)$:

$$\rho_\Lambda(z) = \rho_{\Lambda,0} \exp\left( 3 \int_0^z \frac{1 + w(z')}{1 + z'} dz' \right)$$

**DESI constraints**:
- $w_0 = -1.016 \pm 0.035$ (current epoch)
- $w_a = -0.11 \pm 0.35$ (evolution parameter)

Consistent with a cosmological constant ($w = -1$), though some evolution cannot be ruled out.

---

## Key Results

1. **Precision BAO measurements**: Sub-percent precision on BAO scale at multiple redshifts, constraining expansion history.

2. **Matter density**: $\Omega_m = 0.296 \pm 0.010$ (combined with CMB priors), more precise than earlier measurements.

3. **Consistency with ΛCDM**: No dramatic deviations from the standard model.

4. **Growth rate compatible with GR**: RSD measurements consistent with General Relativity predictions; no strong evidence for modified gravity.

5. **S8 and H0 tensions persist**: Some tension with other measurements, hinting at possible systematics or new physics.

6. **Dark energy equation of state**: $w = -1.0$ (cosmological constant) remains preferred.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: MEDIUM-HIGH**

DESI's precision measurements provide crucial tests of alternative theories:

- **Phonon-exflation predicts specific expansion history**: The theory should predict $H(z)$ uniquely. DESI's BAO measurements directly test these predictions.

- **Growth rate from phonon dynamics**: If gravity is mediated by phonons, the growth rate $f$ might deviate from GR predictions. DESI's RSD measurements place tight constraints.

- **Dark energy from spectral action**: Phonon-exflation predicts dark energy emerges from the spectral action (ground state energy). DESI's constraint on $w(z)$ tests whether this emerges correctly.

- **Sigma-8 and phonon abundance**: The amplitude of density fluctuations ($\sigma_8$) relates to the phonon occupation numbers and interactions. The observed $\sigma_8$ constrains these properties.

- **Large-scale structure formation**: The observed clustering patterns (BAO peak shape, RSD amplitude) must emerge from phonon-gravity coupling in phonon-exflation.

---

## Key Equations

1. **BAO as standard ruler**:
   $$r_{\text{BAO}} = 153.8 \pm 2.0 \text{ Mpc/h} \quad \text{(CMB-inferred)}$$

2. **Expansion history via BAO**:
   $$d_c(z) = \frac{c}{H_0} \int_0^z \frac{dz'}{E(z')}, \quad E(z) = \sqrt{\Omega_m(1+z)^3 + \Omega_\Lambda}$$

3. **Growth rate from RSD**:
   $$f = \frac{d \ln D}{d \ln a}, \quad f \approx \Omega_m^{0.55} \quad \text{(ΛCDM)}$$

4. **Dark energy equation of state**:
   $$w(z) = \frac{P_\Lambda}{\rho_\Lambda} = w_0 + w_a (1 - a) \quad \text{(CPL parameterization)}$$

5. **Sigma-8 definition**:
   $$\sigma_8 = \text{RMS density fluctuation on 8 Mpc/h scale at } z=0$$

---

## Legacy and Significance

DESI will provide the most precise measurements of large-scale structure for years to come. Its results will:

- Tighten constraints on dark energy
- Probe modified gravity theories
- Measure the expansion history to percent-level precision
- Constrain initial conditions and inflation
- Test alternative theories of cosmology (including phonon-exflation and others)

For the cosmic web, DESI's measurements of galaxy clustering, filament structure, and void statistics provide the most detailed map of large-scale structure ever obtained, crucial for distinguishing between competing theoretical frameworks.

---

## References

[Search results integrated; full citations available in search output above.]
