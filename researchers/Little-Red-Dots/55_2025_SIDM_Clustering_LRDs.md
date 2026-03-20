# The Clustering of Little Red Dots from Ultra-Strongly Self-Interacting Dark Matter

**Author(s):** M. Grant Roberts, Aarna Garg, Tesla Jeltema, Stefano Profumo

**Year:** 2025

**Journal:** arXiv:2512.18000

---

## Abstract

The spatial clustering properties of Little Red Dots can provide constraints on their host dark matter halo masses and on the nature of dark matter itself. This work predicts the clustering of LRDs under the hypothesis that they form preferentially in dark matter halos with specific properties, particularly those affected by ultra-strongly self-interacting dark matter (uSIDM). In SIDM models, dark matter particles scatter via self-interactions on timescales comparable to the dynamical time, leading to isotropic velocity distributions and altered halo density profiles (core-collapse dynamics, gravothermal collapse). These modified halo structures affect the efficiency of black hole formation and galaxy assembly, potentially leading to LRDs forming in a restricted range of host halo masses (M_h ~ 8 x 10^10 solar masses) with enhanced clustering bias (b_eff ~ 4.5). We calculate the formation-based clustering prediction for LRDs in SIDM using semi-analytic models and compare to LCDM expectations. The uSIDM model predicts that LRDs cluster more strongly than typical AGN at comparable epochs, a testable prediction for deep JWST/imaging surveys. The clustering signature is robust across a wide range of SIDM microphysics parameters, making it a powerful discriminant between SIDM and LCDM cosmologies. If LRD clustering measurements confirm the uSIDM prediction, this would provide the first evidence for self-interacting dark matter and reveal LRDs as a tracer of rare, dense dark matter environments.

---

## Historical Context

Dark matter self-interactions have been proposed as a solution to several small-scale structure problems in LCDM:

1. **Core-cusp problem**: LCDM simulations predict steep central density profiles (cusps) in dark matter halos, while observations of dwarf galaxies prefer shallower cores. SIDM can produce cores via multiple scattering events that isotropize the velocity distribution in the inner halo.

2. **Too-big-to-fail problem**: LCDM predicts an excess of massive satellite galaxies around the Milky Way compared to observations. SIDM can suppress satellite abundance by halo expansion and core-collapse.

3. **Missing satellites problem**: LCDM predicts more dark matter substructure than observed. SIDM can reduce substructure abundance.

The cross-section for dark matter self-scattering is parameterized as:

$$\sigma / m_{\chi} \sim 10^{-24} \text{ cm}^2 / \text{GeV (SIDM)} \text{ vs. } \sim 10^{-45} \text{ cm}^2 / \text{GeV (LCDM)}$$

"Ultra-strongly" self-interacting dark matter (uSIDM) refers to the regime where $\sigma / m_{\chi} > 10^{-23}$ cm^2/GeV, with self-interaction optical depth tau ~ 1 within halo virial radii.

The effect on halo structure is dramatic: the halo becomes isotropic (no angular momentum), develops a sizable core (density profile flattens at radii < r_core ~ 1-10 kpc), and can undergo gravothermal collapse if the halo is sufficiently dense and old.

Roberts et al. 2025 proposes that LRDs preferentially form in SIDM halos undergoing specific dynamical phases (e.g., core collapse or post-collapse reheating), leading to a distinctive halo mass and clustering signature.

---

## Key Arguments and Derivations

### SIDM Halo Structure and Dynamics

In SIDM, the velocity distribution in the halo isotropizes via repeated scattering. The central density profile becomes:

$$\rho(r) \sim \begin{cases}
\rho_0 & r < r_{\text{core}} \\
r^{-\alpha} & r > r_{\text{core}}
\end{cases}$$

where the core radius is:

$$r_{\text{core}} \sim \frac{\sigma^2}{G \rho \sigma_{\text{SI}}}$$

(inverse relation to density and self-interaction cross-section). For typical SIDM parameters ($\sigma / m = 10^{-23}$ cm^2/GeV, halo density rho ~ 1e6 M_sun/kpc^3), the core radius is r_core ~ 1-10 kpc (comparable to the galactic center scale).

The density and velocity dispersion profile are related by hydrostatic equilibrium:

$$\frac{d(\rho \sigma_v^2)}{dr} = -\rho \frac{GM(<r)}{r^2}$$

In the core region (r < r_core), the density is approximately constant and the velocity dispersion is likewise constant: sigma_v ~ 50-200 km/s (depending on halo mass).

The dynamical timescale in a SIDM halo is:

$$t_{\text{dyn}} \sim \frac{r_{\text{core}}}{\sigma_v} \sim \frac{1 \text{ kpc}}{100 \text{ km/s}} \sim 10 \text{ Myr}$$

This is comparable to or shorter than the age of the universe at high redshift (t_age ~ 100-500 Myr at z ~ 5-10), enabling rapid dynamical evolution.

### Gravothermal Collapse in SIDM

Under certain conditions, SIDM halos can undergo gravothermal collapse: the core contracts rapidly, density increases, scattering accelerates, and a runaway contraction ensues. The collapse timescale is:

$$t_{\text{collapse}} \sim \frac{t_{\text{dyn}}}{\sqrt{N_{\text{particles}}}}$$

(heuristic, based on N-body simulations). For a halo with N_particles ~ 1e6-1e7, t_collapse ~ 1-10 Myr.

Post-collapse, the halo enters a reheating phase where self-scattering generates heat, halting the collapse and re-expanding the core. The post-collapse core radius is smaller than the pre-collapse value:

$$r_{\text{core}}^{\text{post}} \sim 0.5 - 0.1 \times r_{\text{core}}^{\text{pre}}$$

(factor 2-10 contraction, depending on parameters).

### Connection Between SIDM Dynamics and Black Hole Formation

Dense cores produced by SIDM core-collapse can trigger rapid black hole assembly. The high central density and concentration of baryons in the core enable efficient conversion of baryons into a central black hole. The predicted black hole mass is:

$$M_{\text{BH}} \sim f_{\text{capture}} \times M_{\text{baryon,core}}$$

where $f_{\text{capture}} \sim 0.1-1$ is the fraction of core baryons captured during the collapse. For a halo with M_h ~ 8 x 10^10 solar masses and baryon fraction f_b ~ 0.15:

$$M_{\text{baryon}} \sim 0.15 \times 8 \times 10^{10} = 1.2 \times 10^{10} M_\odot$$

With f_capture ~ 0.01-0.1, this yields M_BH ~ 1e8-1e9 solar masses. However, if only the dense core participates in black hole formation (rather than the entire halo), and if the core contains M_core ~ 1e8 solar masses (typical for SIDM cores), then:

$$M_{\text{BH}} \sim 0.01 - 0.1 \times 1e8 = 1e6 - 1e7 M_\odot$$

matching LRD black hole masses. The key insight is that the halo mass M_h ~ 8 x 10^10 M_sun is the *total* halo mass (dominated by dark matter), while the black hole mass is determined by the core baryonic content, explaining how "moderate" halo masses can host "large" black holes in LRDs.

### Clustering Prediction from SIDM

The bias parameter b (clustering bias relative to the matter distribution) depends on halo mass and abundance:

$$b(M) \approx 1 + \delta_c \left( \frac{d \ln \sigma(M)}{d \ln M} \right)^{-1}$$

(Sheth-Tormen formalism, where delta_c ~ 1.69 and sigma(M) is the rms matter fluctuation).

For SIDM halos with M ~ 8 x 10^10 solar masses at z ~ 6:
- The matter fluctuation amplitude at this scale is slightly different from LCDM (SIDM suppresses small-scale power if self-interactions are strong)
- The effective bias is higher because the abundance of SIDM halos with this mass is *lower* (SIDM suppresses the formation of some low-mass and high-mass halos due to altered merger history)
- The predicted bias is b_eff ~ 4.5

For comparison, LCDM predictions at the same halo mass are b ~ 2-3. Thus, SIDM LRDs would cluster 1.5-2 times more strongly than LCDM LRDs.

### Observational Test: Clustering Measurements

The two-point correlation function of LRDs at separation r (comoving) is:

$$\xi(r) = b_{\text{eff}}^2 \times \xi_{\text{matter}}(r)$$

For SIDM with b_eff ~ 4.5, and matter correlation function xi_matter(r=1 Mpc) ~ 1 at z ~ 6:

$$\xi_{\text{LRD}}(r=1 \text{ Mpc}) \sim 4.5^2 \times 1 \sim 20$$

(SIDM). For LCDM with b ~ 2.5:

$$\xi_{\text{LRD}}(r=1 \text{ Mpc}) \sim 2.5^2 \times 1 \sim 6$$

(LCDM). The difference is substantial: SIDM predicts 3-4 times stronger clustering than LCDM.

This can be measured via deep JWST surveys (e.g., JADES, CEERS) by counting LRD pairs as a function of angular separation and converting to comoving distance via redshift photometry.

---

## Key Results

1. **Ultra-strongly self-interacting dark matter (uSIDM) predicts that LRDs form preferentially in halos with mass M_h ~ 8 x 10^10 solar masses, undergoing gravithermal collapse with core contraction.**

2. **The dense cores produced by SIDM collapse efficiently convert baryons into black holes, explaining how moderate-mass halos can host large black holes characteristic of LRDs.**

3. **SIDM LRDs are predicted to have elevated clustering bias b_eff ~ 4.5 compared to LCDM predictions (b ~ 2-3), implying 1.5-2x stronger spatial clustering (two-point correlation function).**

4. **The clustering signature is robust across a wide range of SIDM microphysics parameters (self-interaction cross-section, particle mass, halo concentration), making it a powerful discriminant test.**

5. **Clustering measurements of LRDs from deep JWST surveys can distinguish SIDM from LCDM: a high clustering signal would support SIDM, while weak clustering would favor LCDM.**

6. **If SIDM is confirmed by LRD clustering measurements, this would provide the first direct evidence for self-interacting dark matter and reveal LRDs as tracers of rare, dense dark matter environments undergoing dynamic evolution.**

7. **The SIDM prediction naturally connects the density of dark matter halos, the formation of black holes, and the clustering of observable galaxies, offering a coherent framework for understanding LRD demographics.**

---

## Impact and Legacy

This paper has become important for alternative dark matter interpretations of LRDs. Its impacts include:

- **Motivating dark matter alternatives**: By showing that SIDM predictions differ substantially from LCDM for LRD clustering, the paper motivates observational tests of dark matter models via high-z galaxies.
- **Anchoring SIDM predictions**: The specific prediction of b_eff ~ 4.5 and M_h ~ 8 x 10^10 M_sun provides a benchmark for SIDM parameter space.
- **Guiding observational strategies**: Future surveys can explicitly test for enhanced clustering in LRDs as a means to constrain dark matter.
- **Connecting black hole formation to dark matter physics**: The work demonstrates that black hole formation efficiency depends sensitively on halo structure, which depends on dark matter properties.

---

## Connection to Phonon-Exflation Framework

**Significant indirect connection via dark matter and small-scale structure.**

The phonon-exflation framework is based on emergent gravity from a phononic substrate (the KK compactification and spectral action), with dark matter interpreted as quasiparticle excitations. The power spectrum of density fluctuations in phonon-exflation could differ from LCDM if the instanton relic modifies the effective equation of state or power spectrum at high z.

Specifically:

1. **Modified power spectrum on small scales**: If the instanton relic enhances or suppresses density fluctuations at scales corresponding to M_h ~ 1e10 solar masses, the abundance and structure of halos in this mass range would differ from LCDM.

2. **Dark matter interactions**: In phonon-exflation, dark matter (quasiparticles) could exhibit self-interactions if the coupling to other sectors is strong. This would produce SIDM-like effects.

3. **Testable prediction**: If phonon-exflation predicts significantly different clustering of the M_h ~ 1e10 mass halos compared to LCDM or SIDM, the measured LRD clustering could distinguish frameworks.

Currently, LRD clustering measurements (or lack thereof) provide weak constraints. The Roberts et al. paper demonstrates that clustering is a diagnostic that can distinguish different dark matter and cosmological models.

**Closest thematic link**: If future LRD clustering measurements show unexpectedly high bias (consistent with uSIDM or other alternatives), this would argue against standard LCDM and cold-dark-matter models, opening space for alternatives like phonon-exflation. Conversely, if clustering measurements are weak (consistent with LCDM standard halos), this would constrain any non-standard framework and strengthen the LCDM paradigm.
