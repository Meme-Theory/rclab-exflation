# Formation of the Little Red Dots from the Core-Collapse of Self-Interacting Dark Matter Halos

**Author(s):** Fangzhou Jiang, Zixiang Jia, Haonan Zheng, Luis C. Ho, Kohei Inayoshi, Xuejian Shen, Mark Vogelsberger, Wei-Xiang Feng

**Year:** 2026

**Journal:** arXiv:2503.23710

---

## Abstract

The origin of supermassive black holes (SMBHs) in Little Red Dots at z > 5 remains puzzling: standard LCDM black hole formation via hierarchical merging and Eddington-limited accretion struggles to produce black holes of the observed masses (M_BH ~ 1e6-1e9 solar masses) in the available cosmic time. This work proposes that LRDs form via gravothermal collapse in ultra-strongly self-interacting dark matter (uSIDM) halos. In uSIDM, the dense cores that develop during collapse naturally trigger rapid black hole formation via efficient capture of baryon material and sustained super-Eddington accretion. We employ cosmological simulations and semi-analytic models with velocity-dependent SIDM cross-sections (sigma ~ 30 cm^2/g at v ~ 80 km/s) to demonstrate that gravothermal core collapse naturally produces black holes with masses M_BH ~ 1e6-1e8 solar masses in halos with mass M_h ~ 1e10-1e11 solar masses. The formation timescale is t_collapse ~ 10-100 Myr, consistent with observed LRD redshift distribution. The predicted black hole and halo mass distributions match JWST observations without fine-tuning. If correct, LRDs are a uniquely sensitive probe of dark matter self-interactions at early cosmic times, offering independent evidence for SIDM models and revealing a heretofore-unknown pathway for early black hole assembly via dark matter halo dynamics.

---

## Historical Context

The "early black hole problem" has motivated exploration of alternative pathways beyond standard LCDM:

1. **Primordial black holes (PBHs)**: Formed from collapse of density fluctuations in the early universe, potentially seeding the observed population. Challenges: requires specific primordial power spectrum modifications, PBH abundance not well-constrained.

2. **Direct collapse black holes (DCBHs)**: Collapse of supermassive primordial gas clouds (Pop III-like) without stellar phase. Challenges: requires fine-tuned gas conditions, low gas clumping.

3. **Intermediate-mass black holes (IMBHs) from runaway stellar collisions**: Rapid growth from 100-1000 solar mass seeds via stellar mergers. Challenges: requires very high stellar densities.

4. **Rapid accretion at super-Eddington rates**: Standard seeds growing via L >> L_Edd accretion. Challenges: requires sustained super-Eddington conditions, limited by radiation pressure.

Jiang et al. 2026 proposes a new mechanism: **dark matter-driven black hole formation** via gravothermal collapse in self-interacting dark matter halos. The mechanism is elegant: SIDM halos naturally develop dense cores on dynamical timescales (~ 10 Myr at z ~ 6), these cores concentrate baryons, and black hole formation occurs via efficient baryon capture.

---

## Key Arguments and Derivations

### Gravothermal Collapse in SIDM Halos

In ultra-strongly self-interacting dark matter, the self-interaction cross-section is parameterized as:

$$\sigma(v) = \sigma_0 \left( \frac{v}{v_0} \right)^\gamma$$

where $v$ is the relative velocity between dark matter particles. For velocity-dependent SIDM with typical parameters:
- $\sigma_0 \sim 30$ cm^2/g (at reference velocity v_0 ~ 80 km/s)
- $\gamma \sim 0$ to $-1$ (weak velocity dependence to inverse velocity dependence)

The optical depth for self-scattering within a halo of radius R and velocity dispersion sigma_v is:

$$\tau = \sigma(v) \times \rho(r) \times l_{\text{mfp}} \sim 1$$

where l_mfp ~ 1/rho sigma(v) is the mean free path. For SIDM halos at z ~ 6, tau ~ 1 is readily achieved, enabling rapid isotropization of the velocity distribution.

The isotropized halo then undergoes gravothermal collapse. The mechanism is as follows:

1. **Initial condition**: A halo with mass M_h ~ 1e10 solar masses and radius R_h ~ 100 kpc forms via hierarchical merging at z ~ 10-15. The density profile is initially cuspy (profile alpha ~ 1 in rho ~ r^-alpha), similar to LCDM.

2. **Isotropization phase**: Self-scattering isotropizes the velocity distribution in the core. The central velocity dispersion becomes approximately constant: sigma_v(r < r_core) ~ 100-200 km/s.

3. **Contraction phase**: As the core isotropizes and becomes hotter (higher sigma_v), it is no longer supported by rotation (as in LCDM cuspy halos where rotation provides support at small radii). The core contracts under gravity. The contraction timescale is the central dynamical time:

$$t_{\text{dyn}} \sim \frac{1}{\sqrt{G \rho_0}} \sim \frac{1}{\sqrt{G \times 1e6 M_\odot / \text{kpc}^3}} \sim 1-10 \text{ Myr}$$

(for central density rho_0 ~ 1e6 solar masses/kpc^3).

4. **Gravothermal runaway**: As the core contracts, the central density increases dramatically: rho_0(t) ~ rho_0(0) exp(t/t_collapse), where t_collapse ~ few Myr. The density grows exponentially on the dynamical time.

5. **Core-collapse singularity**: In the absence of a physical cutoff (e.g., quantum degeneracy pressure, black hole formation), the density would diverge in finite time (gravithermal catastrophe). However, once the density reaches threshold rho_threshold ~ 1e10 solar masses/kpc^3, baryons (which are mixed with dark matter) become gravitationally unstable and undergo rapid collapse, forming a black hole.

### Black Hole Formation Condition and Mass

The threshold density for black hole formation is set by the Jeans condition: perturbations with wavelength > lambda_Jeans are unstable. For a self-gravitating baryonic component in a dark matter background:

$$\lambda_{\text{Jeans}} = c_s \sqrt{\frac{\pi}{G \rho_{\text{eff}}}}$$

where $c_s$ is the sound speed and rho_eff is the effective density. For a gas temperature T ~ 1e4 K (shock-heated during core collapse), c_s ~ 10 km/s. For rho_eff ~ 1e8 solar masses/kpc^3:

$$\lambda_{\text{Jeans}} \sim 10 \text{ km/s} \times \sqrt{\frac{\pi}{G \times 1e8}} \sim 1 \text{ pc}$$

Clumps of baryons with size > 1 pc collapse on the Jeans timescale (~ few Myr). The mass of material that collapses is approximately the baryon mass within the Jeans scale:

$$M_{\text{collapse}} \sim \rho_{\text{baryon}} \times (\lambda_{\text{Jeans}})^3 \sim (0.15 \rho_{\text{DM}}) \times (1 \text{ pc})^3$$

For a SIDM halo with central dark matter density rho_DM ~ 1e8 solar masses/kpc^3 (high concentration due to collapse), this gives:

$$M_{\text{collapse}} \sim 0.15 \times 1e8 \times (10^{-6} \text{ kpc})^3 \sim 1e7 M_\odot$$

(rough order of magnitude). The collapsing baryon clump forms a black hole with mass M_BH ~ f_BH x M_collapse, where f_BH ~ 0.1-1 is the fraction that directly forms the black hole (remainder forms a stellar cluster or dissipates as radiation). Thus:

$$M_{\text{BH}} \sim 1e6 - 1e7 M_\odot$$

matching LRD masses.

### Semi-Analytic Model with Monte Carlo Merger Trees

The formation rate of LRDs via SIDM core-collapse is computed using semi-analytic models (SAMs). The SAM tracks the following for each halo:

1. **Halo assembly history**: Monte Carlo realization of the merger tree (based on extended Press-Schechter formalism with SIDM-modified merger rates)
2. **Halo structure**: Density profile and central concentration, accounting for SIDM isotropization and core-collapse dynamics
3. **Baryon assembly**: Gas accretion and star formation (standard recipes, modified for SIDM halo structure)
4. **Black hole formation**: Triggered when central density exceeds rho_threshold during core-collapse phase

For each halo in the merger tree that undergoes core-collapse, a black hole is "born" with mass M_BH sampled from the predicted mass distribution (derived from the analysis above).

The predicted redshift distribution of LRDs is computed by integrating over all halos undergoing collapse at each redshift:

$$\frac{dN_{\text{LRD}}}{dz dV} = \int_{M_h} \frac{dn}{dM_h}(M_h, z) \times P_{\text{collapse}}(z | M_h) \times \frac{dM_{\text{BH}}}{dM_h} \, dM_h$$

where:
- $dn/dM_h$ is the halo mass function (modified for SIDM)
- $P_{\text{collapse}}(z | M_h)$ is the probability that halo M_h undergoes core-collapse by redshift z
- $dM_{\text{BH}}/dM_h$ is the black hole mass as function of halo mass

### Comparison to JWST Observations

The predicted black hole mass distribution and halo mass distribution from the SAM are compared to observed JWST LRD properties:

- **Observed black hole masses**: M_BH ~ 1e6-1e9 solar masses (from broad-line virial estimates, with ~50% systematic downward revision from direct measurements like Paper 51)
- **Predicted masses**: M_BH ~ 1e6-1e8 solar masses (from gravothermal collapse mechanism, accounting for revised direct measurements)
- **Agreement**: Excellent, within factor 2

- **Observed halo masses** (inferred from clustering or abundance): M_h ~ 1e10-1e11 solar masses (from low-spin halo or environmental clustering analysis)
- **Predicted halo masses**: M_h ~ 1e10-1e11 solar masses (from SIDM collapse condition and density threshold)
- **Agreement**: Good, within 0.5 dex

- **Observed redshift distribution**: Peak abundance z ~ 5-6, declining at z > 7 and z < 4
- **Predicted evolution**: Core-collapse timescales and halo assembly predict peak at z ~ 5-6, declining at higher and lower redshift
- **Agreement**: Excellent match

---

## Key Results

1. **Gravothermal core-collapse in ultra-strongly self-interacting dark matter (SIDM) halos naturally triggers rapid black hole formation via efficient capture and compression of baryons, producing black holes with masses M_BH ~ 1e6-1e8 solar masses.**

2. **The black hole formation timescale in SIDM core-collapse (t_collapse ~ 10-100 Myr) is fast enough to produce observationally-inferred black hole masses before z ~ 4, resolving the early black hole formation challenge.**

3. **The SIDM model predicts a characteristic halo mass for LRD host halos (M_h ~ 8 x 1e10 to 1e11 solar masses) set by the SIDM cross-section, consistent with clustering measurements and low-spin halo explanations.**

4. **Semi-analytic models with velocity-dependent SIDM (sigma ~ 30 cm^2/g at v ~ 80 km/s) successfully reproduce the observed black hole and halo mass distributions of JWST LRDs without fine-tuning.**

5. **The predicted redshift evolution of LRD abundance (peak z ~ 5-6) matches observations, explaining both the prevalence of LRDs at high z and their disappearance at z < 4 as a consequence of halo assembly timescales and core-collapse dynamics.**

6. **If SIDM is confirmed as the explanation for LRDs, this provides independent evidence for dark matter self-interactions beyond galactic-scale constraints, making LRDs a unique high-z probe of dark matter physics.**

7. **The SIDM core-collapse mechanism for black hole formation is an alternative to primordial black holes, direct collapse, and rapid accretion, offering a pathway that is inevitable in SIDM cosmologies.**

---

## Impact and Legacy

This paper has been influential for advocating SIDM as a solution to the early black hole problem. Its impacts include:

- **Unifying black hole and dark matter physics**: By linking LRD formation to SIDM dynamics, the paper creates a bridge between two disparate observational domains (black hole demographics and dark matter models).
- **Providing testable SIDM predictions**: The specific predictions for black hole mass distributions, halo masses, and clustering can be tested with JWST observations.
- **Constraining SIDM parameter space**: The velocity-dependent cross-section parameters needed to match LRD observations provide independent constraints on SIDM models, complementary to galactic-scale constraints.
- **Opening LRDs as dark matter probes**: The work establishes LRDs as a novel tool for constraining dark matter properties at high redshift.

---

## Connection to Phonon-Exflation Framework

**Significant connection via dark matter nature and alternative mechanisms for black hole formation.**

The phonon-exflation framework proposes that dark matter is composed of quasiparticle excitations in the KK compactification. If these "dark phonons" exhibit self-interactions (due to coupling to other sectors), they would behave similarly to SIDM particles.

In this interpretation:

1. **Dark matter self-interactions**: Phonon-exflation dark matter could naturally exhibit velocity-dependent self-interactions if the coupling to other fields is momentum-dependent. The cross-section sigma(v) would emerge from the phonon scattering amplitude.

2. **Core-collapse dynamics**: If phonon-exflation dark matter undergoes core-collapse similar to SIDM, it would produce dense cores capable of triggering black hole formation via baryon compression.

3. **Black hole formation efficiency**: The collapse timescale and black hole mass predictions from phonon-exflation would depend on the phonon mass, coupling strength, and the instanton relic properties.

4. **Testable prediction**: If phonon-exflation produces black hole mass and halo mass distributions identical to SIDM, the two frameworks are observationally degenerate. If phonon-exflation predicts *different* distributions (e.g., different collapse timescales due to the instanton relic), this would distinguish frameworks.

**Closest thematic link**: The Jiang et al. framework demonstrates that dark matter physics (via SIDM core-collapse) can explain LRD formation without exotic particle physics. Phonon-exflation, if its dark matter component exhibits SIDM-like properties, would make identical predictions. The comparison of LRD demographics across different dark matter models (SIDM, phonon-exflation dark phonons, standard cold dark matter) provides a window into the fundamental nature of dark matter at early cosmic times.

---

## Conclusion

Papers 42-56 collectively present a comprehensive supplementary analysis of Little Red Dots from multiple perspectives: LCDM explanations (low-spin halos, galaxy evolution, black hole demographics), observational challenges (dust, variability, spectroscopy), formation mechanisms (AGN vs. stellar, local analogs), environmental dependence, alternative models (SIDM, globular clusters), and direct black hole mass measurements. Together, they demonstrate that LRDs remain a frontier for testing cosmology, dark matter, black hole physics, and accretion astrophysics at the earliest cosmic times.
