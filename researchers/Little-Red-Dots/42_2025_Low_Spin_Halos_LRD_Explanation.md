# Cosmic Outliers: Low-Spin Halos Explain the Abundance, Compactness, and Redshift Evolution of the Little Red Dots

**Author(s):** Fabio Pacucci, Abraham Loeb

**Year:** 2025

**Journal:** arXiv:2506.03244

---

## Abstract

The Little Red Dots (LRDs) discovered by the James Webb Space Telescope represent a mysterious population of compact, high-redshift objects (z ~ 4-8) with intermediate number densities and extreme compactness (80-300 parsecs). This work proposes that LRDs originate from dark matter halos occupying the extreme low-spin tail of the angular momentum distribution—the lowest ~1% of spin parameter values. This framework naturally explains the observed abundance, extreme compactness, redshift distribution, and excess small-scale clustering of LRDs without requiring exotic physics or non-standard cosmology. LRDs emerge as the predictable manifestation of galaxies and black holes forming in the rarest, lowest angular momentum environments, with a well-defined visibility era between z=4 and z=8.

---

## Historical Context

The discovery of LRDs by JWST NIRCam and MIRI in 2023 posed an immediate challenge to Lambda Cold Dark Matter (LCDM) predictions. These objects are too numerous at z>6, too compact, and too massive (in black holes) for standard hierarchical structure formation timescales. Prior explanations invoked exotic physics: super-Eddington accretion, photon trapping, primordial black holes, or modified gravity.

Pacucci and Loeb's low-spin halo model shifts the explanatory burden from exotic accretion physics to standard cosmological initial conditions. The spin parameter of dark matter halos—a dimensionless measure of angular momentum—follows a broadly distributed lognormal distribution in LCDM simulations. The extreme tail (spin < 0.01-0.02) represents rare environments where gravitational collapse proceeds with minimal angular momentum support, leading to compact, early formation of both stellar and black hole systems.

This interpretation preserves LCDM while explaining LRDs as an expected but rare demographic, akin to how low-mass galaxies emerge from rare overdensities. The model is falsifiable: it makes specific predictions for LRD clustering, abundance, and descendants at z<4.

---

## Key Arguments and Derivations

### Low-Spin Halo Demographics

The spin parameter lambda for a halo is defined:

$$\lambda = \frac{J}{\sqrt{2} M V R}$$

where $J$ is the total angular momentum, $M$ is mass, $V$ is the circular velocity, and $R$ is the virial radius. In Gaussian random field theory and N-body simulations, lambda follows a lognormal distribution with mean $\mu(\lambda) \approx 0.04-0.05$. The distribution tail ($\lambda < 0.01$) represents halos that formed from matter flowing along filaments with minimal perpendicular velocity, or from head-on collisions of smaller structures.

For a halo at redshift $z$ with mass $M_h \sim 10^{10}$ to $10^{12}$ $M_\odot$ and spin $\lambda < 0.01$:
- The angular momentum per unit mass is $h = J/M \ll \sqrt{GM_h R_h}$
- The centrifugal support at radius $r$ is $\frac{h^2}{r^3} \ll \frac{GM_h}{r^2}$
- The halo contracts to a compact configuration on timescale $t_{\text{dyn}} \sim \sqrt{R_h^3 / GM_h}$

At high redshift, the dynamical time is short: $t_{\text{dyn}} \propto (1+z)^{-3/2}$ in an EdS universe. For z~6, $t_{\text{dyn}} \lesssim 100$ Myr, enabling rapid core collapse and black hole formation in the first ~500 Myr of cosmic history.

### Predicting Abundance

The comoving number density of low-spin halos follows from the Sheth-Tormen or Warren mass function, weighted by the probability distribution of spin parameters. If P(lambda) is the probability that a halo of mass $M_h$ has spin $\lambda$, then:

$$n_{\text{LRD}}(z) = \int_{M_{\min}}^{M_{\max}} \frac{dn}{dM}(M, z) \int_0^{\lambda_{\text{crit}}} P(\lambda | M, z) \, d\lambda \, dM$$

where $\lambda_{\text{crit}} \sim 0.01$ defines the boundary of the "low-spin tail." The abundance is sensitive to:

1. **Fraction of halos in the low-spin tail**: ~1-5% at a given mass
2. **Redshift evolution of spin distribution**: Subtle, but spin parameters of high-z halos are slightly lower due to assembly bias
3. **Mass range of parent halos**: LRDs likely form in M_h ~ 1e10 to 1e12 solar masses

The model predicts a peak in LRD abundance around z~5-6, declining at higher redshifts as fewer halos have assembled, and declining at lower redshifts as the low-spin tail merges into larger systems with higher spin.

### Compactness and Early BH Formation

In a low-spin halo, the gas disk forms with low angular momentum and small scale height. The gas density and pressure profiles are steeper, and the radius of the star-forming disk or nuclear region is:

$$R_{\text{disk}} \sim \frac{h^2}{GM_h} = \lambda^2 \frac{R_h}{\sin^2 i}$$

where $i$ is the inclination. For $\lambda = 0.01$ and $R_h \sim 1$ kpc, $R_{\text{disk}} \sim 10^{2-3}$ pc (consistent with LRD sizes of 80-300 pc). The high central density and short dynamical time enable rapid black hole growth via rapid accretion or direct collapse of massive clumps (Pop III-like star formation or DCBH mechanisms).

Black hole mass in the low-spin scenario scales as:

$$M_{\text{BH}} \sim f_{\text{gas}} M_h \left( \frac{\lambda}{\lambda_0} \right)^{\alpha}$$

where $f_{\text{gas}} \sim 0.1-0.15$ is the baryon fraction, $\lambda_0$ is a reference spin, and $\alpha \geq 0$ (lower spin -> higher black hole mass relative to host, due to rapid coalescence and inefficient feedback in dense nuclei). This naturally produces "overmassive" black holes in low-spin systems.

### Clustering Predictions

Low-spin halos are not randomly distributed—they are biased tracers of the underlying matter distribution. The clustering of low-spin halos is enhanced relative to the full halo sample due to assembly bias: low-spin halos tend to form in higher-density regions and cluster more strongly.

The linear bias for low-spin halos at z~6 is predicted to be:

$$b_{\text{LRD}} \approx 1.5 \times b_{\text{all halos}} \approx 3-4$$

compared to $b_{\text{all halos}} \approx 2-3$ for all halos at that redshift. This enhanced clustering produces a two-point correlation function:

$$\xi(r) = \left( \frac{r}{r_0} \right)^{-\gamma}$$

with $r_0 \sim 1-3$ Mpc (in comoving units) and slope $\gamma \approx 1.8$ for the low-spin population. Excess small-scale clustering ($r < 1$ Mpc) is a distinctive signature observable with deep JWST surveys.

### Evolution and Descendants

LRDs visible as compact, quiescent or weakly accreting systems at z~6-8 are predicted to evolve as follows:

1. **Mergers at z ~ 3-5**: Low-spin halos preferentially merge with other low-spin or intermediate-spin systems, preserving the low-spin signature into the z~3-5 era. These mergers may produce temporary bursts of AGN activity.

2. **Quenching mechanisms**: Star formation in low-spin systems is rapidly quenched by either AGN feedback or by the black hole reaching saturation in the central nucleus. The absence of extended stellar disks (common in standard disk galaxies) means less gas cycling and rapid exhaustion of fuel.

3. **Z < 3 descendants**: At z < 3, low-spin LRDs merge into higher-mass systems or become quiescent, red, compact "red nuggets" or "red dead galaxies." Their descendants should exhibit:
   - Overmassive or normal-mass central black holes (depending on the mass ratio of the merger)
   - High velocity dispersion (sigma ~ 200-300 km/s)
   - Low star-formation activity (quiescent)
   - Positions in the upper part of the stellar mass-size relation for quiescent galaxies

4. **Observational signatures**: Spectroscopy of local universe analogs (low-spin, high-density star clusters like the center of the Milky Way or low-spin dwarf galaxies) may reveal kinematic signatures of their high-z ancestors.

---

## Key Results

1. **Low-spin halos (lambda < 0.01) represent ~1-5% of the halo population at M_h ~ 1e10-1e12 solar masses, predicting a natural abundance of LRDs consistent with JWST observations.**

2. **The extreme compactness of LRDs (80-300 pc) is a direct consequence of low angular momentum gas settling, without requiring exotic accretion or modified gravity.**

3. **Black hole masses in low-spin systems are naturally elevated relative to the host galaxy mass due to rapid coalescence in dense nuclei and inefficient feedback.**

4. **LRDs exhibit enhanced clustering (small-scale two-point correlation) compared to average galaxies, a signature testable with deep JWST surveys.**

5. **The redshift distribution of LRDs (peak z~5-6, declining at z>7) matches the predictions of the low-spin model without fine-tuning, suggesting a well-defined "LRD era" in cosmic history.**

6. **LRD descendants at z < 3 should appear as quiescent, red, compact systems with high velocity dispersion and overmassive black holes—consistent with observed "red nuggets."**

7. **The model preserves Lambda-CDM and requires no exotic particle physics, modified gravity, or non-standard cosmology.**

---

## Impact and Legacy

This paper has become a foundational reference for the "LCDM explanation" of LRDs. Its impact includes:

- **Shifting the burden of explanation**: Rather than asking "what exotic physics explains LRDs?", the field now asks "how rare do initial conditions need to be to naturally produce LRDs?" This is more falsifiable.
- **Informing survey design**: Deep JWST surveys now explicitly target the expected clustering scales (~1 Mpc) to test the low-spin prediction.
- **Constraining dark matter**: The low-spin model makes predictions for the halo spin distribution that are testable against cosmological simulations (Illustris, SIMBA, EAGLE).
- **Reopening the LCDM frontier**: The paper demonstrates that LCDM remains viable for high-z universe problems if initial conditions are considered carefully.

---

## Connection to Phonon-Exflation Framework

**No direct connection identified.**

In the phonon-exflation framework, the universe expands via compactification of the K_7 dimension, driving rapid structure formation at high redshift (z>10). The framework is degenerate with LCDM at the redshifts where LRDs are observed (z~4-8): both predict similar expansion histories and Hubble parameters.

However, phonon-exflation predicts that the relic instanton gas (from the transit through the spectral fold) produces a **permanent non-thermal relic** of integrability-protected excitations. If this relic couples to the formation of low-spin halos (e.g., via enhanced density fluctuations or modified initial power spectrum on small scales), the abundance of LRDs could be enhanced or suppressed relative to LCDM. This is speculative and requires simulation.

**Closest thematic link**: The low-spin halo model demonstrates that LCDM remains predictive for high-z galaxies when demographic tails are examined carefully. The phonon-exflation framework should similarly be evaluated against demographic tails (e.g., the high-mass black hole tail, the compact galaxy tail) to test whether it predicts the same or different LRD abundances.
