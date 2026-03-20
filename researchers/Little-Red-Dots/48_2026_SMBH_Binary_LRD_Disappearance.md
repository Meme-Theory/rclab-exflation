# Where Have All the Little Red Dots Gone? Supermassive Black Hole Binary Dynamics and its Impact on Galaxy Properties

**Author(s):** Fazeel Mahmood Khan, Benjamin L. Davis, Andrea Valerio Macciò, Kelly Holley-Bockelmann

**Year:** 2026

**Journal:** arXiv:2503.07711

---

## Abstract

The discovery of Little Red Dots (LRDs)—compact, high-redshift galaxies (z > 5) with overmassive black holes and dense stellar cores—presents an evolutionary puzzle: such objects are nearly absent at z < 4, despite their prevalence at higher redshift. This work explores the hypothesis that LRDs disappear due to rapid dynamical evolution triggered by supermassive black hole (SMBH) binary interactions during galaxy mergers. We conduct high-resolution N-body simulations of merging galaxies hosting SMBH binaries, tracking the long-term evolution of stellar density profiles, black hole trajectories, and dynamical stability. We find that SMBH binaries can eject large amounts of mass from galactic cores via three-body gravitational scattering (the "slingshot effect"), reducing central stellar surface density by an order of magnitude on timescales of 100-800 Myr. Gravitational wave recoil from SMBH merger events contributes additional perturbations, further reducing core density and driving the system away from the compact, dense configuration characteristic of LRDs. The model naturally explains both the high-z prevalence of LRDs and their apparent absence at z < 4: LRDs evolve rapidly into lower-density elliptical galaxies within ~500 Myr, consistent with the observed redshift distribution of quiescent high-mass galaxies. The result supports a continuous LCDM evolutionary pathway from early compact galaxies through intermediate quiescent systems to present-day red ellipticals.

---

## Historical Context

The discovery of LRDs by JWST revealed an unexpected population of compact, high-redshift galaxies with overmassive central black holes. These objects are most common at z ~ 5-7, with declining abundance at lower redshift. Their absence as a distinct population at z < 4 poses a puzzle: if LRDs are the progenitors of present-day massive elliptical galaxies or quiescent systems, where do they go?

Proposed solutions included:
1. **Spectral confusion**: LRDs merge into larger systems and lose their "red dot" appearance due to dilution by older stellar populations
2. **Rapid quenching**: Feedback processes quench star formation and alter colors, making LRDs invisible to redshift z ~ 4-5 surveys
3. **Exotic physics**: Non-standard cosmology or modified gravity affecting structure formation timescales

Khan et al. 2026 proposes a dynamical evolution scenario: LRDs disappear because mergers of galaxies hosting SMBH binaries trigger rapid core expansion and mass ejection, transforming compact cores into lower-density systems within ~500 Myr. This process is inevitable in LCDM hierarchical merging and does not require exotic physics.

---

## Key Arguments and Derivations

### Three-Body Slingshot Mechanism

When two SMBH binaries merge (i.e., two galaxies with central SMBH each collide and bring their black holes into a binary configuration), the SMBH binary interacts with stars and dark matter in the galactic core via three-body scattering.

Consider an SMBH binary with masses M_1, M_2 and semi-major axis a. A passing star (mass m_* << M_1, M_2) with impact parameter b < a_capture ~ 2a is scattered via gravitational interactions. The energy transfer is:

$$\Delta E = \frac{G M_1 M_2}{a} \times \left(\frac{r_*}{a}\right)^2 \times f(e_*)$$

where r_* is the star's distance from the binary center-of-mass, and f(e_*) depends on the encounter geometry. Stars with $\Delta E > 0$ (gaining energy) escape from the core, while stars with $\Delta E < 0$ are bound and sink toward the center.

The cumulative effect of many encounters is:
1. **Core expansion**: Stars gaining energy escape, reducing the central density
2. **Black hole recoil**: The SMBH binary experiences a net momentum kick from asymmetric scattering, further perturbing the core

The characteristic timescale for significant core expansion is:

$$t_{\text{expansion}} \sim \frac{M_{\text{core}}}{m_*} \times t_{\text{dyn}}$$

where M_core is the mass in the galactic core, m_* is the typical stellar mass, and t_dyn is the dynamical timescale. For a core with M_core ~ 1e10 solar masses, stellar mass m_* ~ 0.5 solar masses, and t_dyn ~ 10-100 Myr (at z ~ 4-5):

$$t_{\text{expansion}} \sim 10-100 \text{ Myr} \times 2 \times 10^{10} \sim 0.1-1 \text{ Gyr}$$

This is consistent with the observed timescale of LRD disappearance.

### N-Body Simulation: Core Density Evolution

N-body simulations are conducted with 10^6-10^7 particles representing stars and dark matter. Initial conditions are two disk galaxies on a collision course, each hosting a central SMBH with mass M_BH ~ 1e7-1e8 solar masses.

The simulation evolves the gravitational dynamics via direct N-body integration or via more efficient codes (Tree-code, GPU acceleration). Key diagnostics tracked are:

1. **Density profile**: $\rho(r) = M(r) / (4\pi r^2 dr)$ (logarithmic slope)
2. **Projected surface density within 1 kpc**: $\Sigma_{\text{core}} = \int \rho(r < 1 \text{ kpc}) dr$
3. **SMBH separation**: $a(t)$ (semi-major axis of SMBH binary)
4. **Escape velocity**: $v_{\text{esc}}(r) = \sqrt{2 GM(r) / r}$

Results show:
- **Early phase (t < 100 Myr)**: Galaxies approach, SMBHs enter close orbit (a ~ 1-10 kpc)
- **Slingshot phase (100 Myr < t < 500 Myr)**: Core expands, central density drops by factor 3-10. SMBH binary shrinks as energy is radiated via gravitational waves and ejected mass carries away angular momentum.
- **Late phase (t > 500 Myr)**: System settles into low-density configuration. SMBH merger occurs via GW radiation when a < 10 gravitational wave radii (~0.01 pc for 1e8 solar mass black holes). Final merger releases significant energy via gravitational wave recoil.

The density evolution is approximately exponential:

$$\rho(t) = \rho_0 \exp(-t / \tau_{\text{exp}})$$

with $\tau_{\text{exp}} ~ 200-500$ Myr.

### Gravitational Wave Recoil

The SMBH merger itself imparts a recoil velocity (kick) to the merged black hole due to asymmetric gravitational wave emission. The kick velocity depends on mass ratio q = M_2/M_1 and spins:

$$v_{\text{kick}} \sim 180 \, \text{km/s} \times \sin^2(\beta) \sin(2\alpha)$$

where $\beta$ relates to mass ratio and $\alpha$ depends on spin orientations. For nearly equal-mass mergers (q ~ 1), typical kicks are v_kick ~ 50-200 km/s.

The kicked black hole receives momentum $p = M_1 \, v_{\text{kick}}$, imparting energy to surrounding stars:

$$E_{\text{recoil}} = \frac{1}{2} M_1 v_{\text{kick}}^2 \sim 10^{55-56} \text{ erg}$$

(for M_1 ~ 1e8 solar masses, v_kick ~ 100 km/s). This is sufficient to eject stars from the core, accelerating core expansion by additional 10-30%.

---

## Key Results

1. **SMBH binary dynamics during galaxy mergers trigger rapid core expansion on timescales of 100-800 Myr, reducing central stellar surface density by an order of magnitude (factor 3-10).**

2. **The three-body slingshot mechanism ejects mass from galactic cores, transforming the compact, dense configurations characteristic of LRDs (Sigma_core ~ 1e10 solar masses/kpc^2) into lower-density systems (Sigma_core ~ 1e9 solar masses/kpc^2).**

3. **Gravitational wave recoil from SMBH merger events contributes ~10-30% additional core expansion, beyond the effect of three-body scattering alone.**

4. **The evolution timescale (100-800 Myr) is consistent with the redshift evolution of LRDs: systems present at z ~ 5-6 (age ~1 Gyr) undergo mergers and core expansion, disappearing as a recognizable population by z ~ 3-4 (age ~2 Gyr).**

5. **N-body simulations demonstrate that the density evolution from compact LRD-like configurations to lower-density elliptical-like systems is a natural outcome of LCDM hierarchical merging, without requiring exotic physics or modified gravity.**

6. **The evolved systems (post-LRD merger) have properties consistent with observed z ~ 2-3 quiescent galaxies: lower central densities, larger half-light radii, and elevated black hole masses relative to stellar velocity dispersion.**

7. **The model predicts that LRD descendants should be identified at z ~ 2-3 as a population of recently-quenched, low-density ellipticals with elevated black hole masses—a testable prediction for JWST observations.**

---

## Impact and Legacy

This paper has become important for understanding LRD evolution and demographics. Its impacts include:

- **Connecting high-z and low-z AGN populations**: By proposing a direct evolutionary pathway from LRDs (z > 5) through quiescent systems (z ~ 2-3) to present-day ellipticals, the paper unifies seemingly disparate populations.
- **Validating LCDM hierarchical merging**: The result that SMBH binary dynamics naturally produce the observed LRD disappearance suggests LCDM remains viable without exotic extensions.
- **Predicting descendant populations**: The identification of z ~ 2-3 LRD descendants as a distinctive population enables new surveys and observational tests.
- **Constraining black hole-galaxy co-evolution**: The timescales and efficiency of SMBH-driven core expansion constrain feedback mechanisms and black hole growth models.

---

## Connection to Phonon-Exflation Framework

**Indirect connection via structure formation timescales.**

In the phonon-exflation framework, if the expansion history differs from LCDM at z > 6 (via backreaction of the instanton relic), this would affect the redshift at which structures merge and SMBH binaries interact. Specifically:

1. **Modified Hubble parameter**: If phonon-exflation produces H(z) > H_LCDM(z) at z > 6, then the cosmic age is compressed, and mergers occur later in cosmic time. This would shift the redshift at which LRD core expansion occurs.

2. **Modified density fluctuations**: If the instanton relic enhances density fluctuations (e.g., via modified power spectrum), this could change merger rates and core expansion timescales.

3. **Different SMBH demographics**: If phonon-exflation produces different SMBH mass functions at high z (via enhanced/suppressed black hole growth), this would change the properties of SMBH binaries and their recoil velocities.

Currently, both LCDM and phonon-exflation are degenerate at z < 7. Thus, LRD evolution and disappearance should proceed similarly in both frameworks.

**Closest thematic link**: The disappearance of LRDs is a demographic prediction that can be tested. If future observations discover that LRD descendants at z ~ 2-3 differ systematically from LCDM predictions (e.g., different densities, different merger rates, different black hole masses), this would provide evidence for alternative cosmologies like phonon-exflation. The merger timescales and core expansion rates predicted by Khan et al. can serve as benchmarks for phonon-exflation models.
