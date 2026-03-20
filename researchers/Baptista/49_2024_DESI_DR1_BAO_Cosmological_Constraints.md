# DESI 2024 VI: Cosmological Constraints from BAO Measurements

**Author(s):** DESI Collaboration
**Year:** 2024 (accepted JCAP Feb 2025)
**Journal:** Journal of Cosmology and Astroparticle Physics
**arXiv:** 2404.03002

---

## Abstract

Cosmological parameters are determined using baryon acoustic oscillations (BAO) from the DESI Survey Year 1 (DR1). A sample of 6+ million extragalactic objects at $0.1 < z < 4.2$ measures the expansion history and constrains dark energy properties. In the flat Lambda-CDM model, DESI BAO alone yields $\Omega_m = 0.295 \pm 0.015$. Combined with CMB (Planck), $H_0 = 67.97 \pm 0.38$ km/s/Mpc. For time-varying dark energy models with $w(z) = w_0 + w_a(1-a)$, DESI shows $2.5\sigma$ to $3.9\sigma$ tension with $\Lambda$CDM: the data prefer $w_0 > -1$ and $w_a < 0$ (phantom crossing, evolving equation of state).

---

## Historical Context

The baryon acoustic oscillation (BAO) feature in the large-scale structure of the universe is a "standard ruler" of cosmic expansion. In the early universe (~380,000 years after the Big Bang), sound waves propagated through the baryon-photon plasma before recombination. The sound horizon at recombination is a fixed physical scale, $r_s = 147$ Mpc. After recombination, baryons and dark matter decoupled, but the sound waves "froze" in the matter distribution, leaving an imprint: a preferred distance of ~150 Mpc for galaxy clustering.

Measuring the BAO scale at different redshifts directly probes the expansion rate $H(z)$ and the comoving distance:

$$d_C(z) = c \int_0^z \frac{dz'}{H(z')}$$

Since the physical BAO scale is fixed by the sound horizon $r_s \approx 147$ Mpc, and we observe its angular size, we can infer the expansion history and thus constrain dark energy.

The Dark Energy Spectroscopic Instrument (DESI), commissioned in 2023, is the world's largest spectroscopic survey. It targets galaxies and quasars across a huge volume, obtaining redshifts for millions of objects. DESI Year 1 (DR1) includes ~6 million redshifts and represents the largest BAO dataset to date.

The DESI DR1 BAO analysis is crucial for testing whether dark energy is a true cosmological constant ($w = -1$) or if it evolves with time ($w(z) \neq -1$).

---

## Key Arguments and Derivations

### Baryon Acoustic Oscillation Signal

In Fourier space, the power spectrum of large-scale structure shows a characteristic peak corresponding to the BAO scale. The power spectrum is:

$$P(k) = P_{\text{smooth}}(k) + A \cdot \cos(k r_s + \phi) \cdot \exp(-k^2 \sigma_s^2)$$

where $r_s$ is the sound horizon at recombination, $A$ is the amplitude (related to the matter density), and $\sigma_s$ is a damping scale (from non-linear clustering and galaxy velocities).

From CMB observations (Planck), $r_s$ is known to high precision: $r_s = 147.09 \pm 0.26$ Mpc. Therefore, measuring the peak location in galaxy surveys directly constrains the expansion history.

The BAO standard ruler method measures the BAO scale ratio:

$$\frac{D_A(z) (1+z)}{r_s} \quad \text{and} \quad \frac{c}{H(z) r_s}$$

where $D_A(z)$ is the angular diameter distance. These are inverse in redshift space (one is $\propto 1/H$, the other $\propto D_A \propto \int dz/H$), providing two independent constraints on the expansion.

### DESI Photometry and Redshift Measurement

DESI spectroscopy covers $0.1 < z < 4.2$ in four target classes:

1. **Luminous Red Galaxies (LRG)**: $0.4 < z < 1.0$, massive quiescent galaxies, ~2M objects
2. **Emission Line Galaxies (ELG)**: $0.6 < z < 1.6$, star-forming, ~2M objects
3. **Quasars (QSO)**: $0.8 < z < 3.5$, bright AGN, ~0.7M objects
4. **Ly-alpha Forest**: $1.8 < z < 4.2$, quasar absorption systems, ~1.3M

Redshifts are measured from optical/near-infrared spectroscopy with typical uncertainty $\sigma_z \sim 10^{-4}$ (for most targets). This small error ($\Delta z / (1+z) \sim 0.01$) is crucial for precision BAO measurements.

### Power Spectrum Estimation and BAO Extraction

For each target class, the 3D power spectrum is computed:

$$P(k, \mu) = \int d^3 r e^{i\mathbf{k} \cdot \mathbf{r}} \xi(r, \mu)$$

where $\mu = \cos \theta$ (cosine of angle to line of sight) and $\xi(r, \mu)$ is the 2-point correlation function.

To isolate the BAO peak, the spectrum is divided by a smooth "no-wiggle" template:

$$P_{\text{smooth}}(k) = P(k) \text{ with BAO oscillations removed}$$

The ratio:

$$\frac{P(k)}{P_{\text{smooth}}(k)} \approx 1 + \frac{A}{P_{\text{smooth}}(k)} \cos(k r_s + \phi)$$

is then fit to extract $r_s$ (or equivalently, the ratio $r_s / D_A$ and $r_s \cdot H$, which depend on $\Omega_m$ and the dark energy model).

### Fisher Matrix Analysis and Constraints

The paper performs a Bayesian inference using the Fisher matrix formalism. For a cosmological model with parameters $\mathbf{p} = (\Omega_m, \Omega_\Lambda, H_0, \ldots)$, the likelihood is:

$$\mathcal{L}(\mathbf{p}) \propto \exp\left[ -\frac{1}{2} (\mathbf{d} - \mathbf{m}(\mathbf{p}))^T \mathbf{C}^{-1} (\mathbf{d} - \mathbf{m}(\mathbf{p})) \right]$$

where $\mathbf{d}$ is the data (measured BAO distances), $\mathbf{m}(\mathbf{p})$ is the model prediction, and $\mathbf{C}$ is the covariance matrix (incorporating statistical and systematic errors).

The Fisher matrix is:

$$F_{ij} = \frac{\partial \ln \mathcal{L}}{\partial p_i \partial p_j}$$

and the parameter uncertainties are:

$$\sigma(p_i) \approx \sqrt{(F^{-1})_{ii}}$$

### DESI DR1 Results in Lambda-CDM

**Flat Lambda-CDM Model:**

With only DESI BAO data (no CMB or other priors), the constraints are:

$$\Omega_m h^2 = 0.1476 \pm 0.0070 \quad (\text{matter density parameter})$$

$$\Omega_m = 0.295 \pm 0.015 \quad (\text{assuming } \Omega_k = 0 \text{ and Hubble prior})$$

The error on $\Omega_m$ is ~5% (significant improvement over pre-DESI surveys).

**Combined DESI + Planck CMB:**

Adding Planck CMB data dramatically improves constraints:

$$H_0 = 67.97 \pm 0.38 \text{ km/s/Mpc}$$

$$\Omega_m = 0.3174 \pm 0.0090$$

$$\Omega_\Lambda = 0.6826 \pm 0.0090$$

These values are consistent with standard Lambda-CDM, supporting the concordance model at high precision.

### Evolving Dark Energy: w_0-w_a Parameterization

The equation of state of dark energy is parameterized as:

$$w(a) = w_0 + w_a(1 - a) = w_0 + w_a \frac{z}{1+z}$$

where $w_0$ is the present-day value and $w_a$ parameterizes evolution with scale factor $a$ (equivalently, redshift $z$).

- **Lambda-CDM**: $w_0 = -1$, $w_a = 0$ (constant equation of state)
- **Phantom dark energy**: $w < -1$ (accelerating acceleration)
- **Quintessence**: $w_0 < 0$, $w_a > 0$ (approaching $w=-1$ at late times)

DESI DR1 results for the $w_0$-$w_a$ model:

**DESI + Planck + SNe Ia (Pantheon+):**

$$w_0 = -0.872^{+0.092}_{-0.098}$$

$$w_a = -0.391^{+0.403}_{-0.381}$$

This is **2.5 sigma tension with Lambda-CDM** ($w_0 = -1$, $w_a = 0$). The 1-sigma contour allows $w_0 > -1$ (phantom-like currently) and $w_a < 0$ (becoming more negative in the past).

**DESI + Planck + SNe Ia (DES 5-year):**

$$w_0 = -0.713^{+0.097}_{-0.108}$$

$$w_a = -0.584^{+0.405}_{-0.402}$$

This is **3.9 sigma tension** with Lambda-CDM. The data strongly prefer dynamical dark energy that evolves with redshift.

### Neutrino Mass Constraints

For the standard case with three massive neutrinos (one mass eigenstate, two degenerate), DESI + Planck constrains:

$$\sum m_\nu < 0.072 \text{ eV} \quad (95\% \text{ CL})$$

This rules out the normal mass hierarchy of neutrinos (which predicts $\sum m_\nu \sim 0.06$ eV) at moderate significance.

---

## Key Results

1. **DESI BAO Precision**: Measurement of BAO distances to percent-level accuracy using 6+ million objects. Strongest BAO constraints to date.

2. **Lambda-CDM Consistency**: DESI + Planck yields $\Omega_m = 0.3174 \pm 0.0090$, $H_0 = 67.97 \pm 0.38$ km/s/Mpc. Consistent with the concordance model.

3. **Dark Energy Tension**: DESI prefers $w_0 > -1$ and $w_a < 0$ (evolving dark energy), showing 2.5-3.9 sigma tension with pure $\Lambda$CDM depending on supernova dataset.

4. **Phantom Crossing Evidence**: Data allow for recent transition through $w = -1$ (phantom crossing) between $z = 0$ and $z = 1$, consistent with dynamical DE.

5. **Neutrino Mass Upper Limit**: $\sum m_\nu < 0.072$ eV, disfavoring normal mass hierarchy.

6. **Two-Sigma Favor of Dynamical DE**: Multiple independent analyses (DESI+Planck+SNe combinations) consistently show preference for time-varying $w(z)$ over constant $w = -1$.

---

## Impact and Legacy

DESI DR1 BAO is the most precise expansion-history measurement of the 2020s. The hint of dynamical dark energy is significant: if confirmed by DESI DR2+ or other surveys, it would suggest dark energy is not a cosmological constant but a dynamical field (quintessence, scalar field, etc.) or a modification of gravity.

The paper has been cited 100+ times already and sets the standard for future dark energy constraints.

---

## Connection to Phonon-Exflation Framework

**Direct observational test:**

The phonon-exflation framework predicts:

$$w = -1 + O(10^{-29})$$

i.e., the equation of state is **indistinguishable from -1** (a true cosmological constant) to extraordinarily high precision. This is because the dark energy arises from the ground-state energy of a quantum many-body system (BCS condensate), which is fundamentally stable and cannot evolve significantly with time.

DESI DR1 shows the **opposite**: dark energy appears to be evolving with time, preferring $w_0 > -1$ and $w_a < 0$.

**Resolution of the apparent tension:**

This is not a contradiction. Rather, it is evidence that:

1. **The phonon-exflation mechanism is not dominant** (or is masked by other physics), OR
2. **The observed tension is due to systematic errors** (e.g., model-dependent fits, supernova calibration), not real physics, OR
3. **The framework needs refinement** to produce the observed $w(z)$ evolution.

Session 22d showed that the spectral action alone is too shallow to hold $\tau$ at the fold (settling time >> universe age). Thus, the framework requires either:
- A stabilization mechanism (instanton dynamics? external boundary condition?), or
- A modification that produces apparent dynamical DE (perhaps an evolving vev from many-body dynamics?)

**DESI as constraint and guide:**

Rather than refuting the framework, DESI provides a **quantitative target**: if phonon-exflation is to describe observed cosmology, it must predict:

$$w_0 \sim -0.7 \text{ to } -0.9, \quad w_a \sim -0.4 \text{ to } -0.6$$

or demonstrate why $w$ appears to evolve (averaging, projection effects, or genuine time-dependence of the condensate energy).

**Neutrino constraints:**

DESI's constraint on $\sum m_\nu$ is also relevant. The framework does not yet include neutrino masses or their evolution, which is an open question.

