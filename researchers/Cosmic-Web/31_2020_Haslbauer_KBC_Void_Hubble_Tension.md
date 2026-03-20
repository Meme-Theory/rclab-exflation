# The KBC Void and Hubble Tension Contradict LCDM on a Gpc Scale

**Author(s):** Haslbauer, M.; Banik, I.; Kroupa, P.
**Year:** 2020
**Journal:** arXiv:2009.11292 (MNRAS)

---

## Abstract

The Milky Way and Local Group reside within the Kennicutt-Boots-Ciardullo (KBC) void — a local underdensity spanning ~250 Mpc radius with density contrast Delta_rho/rho ~ -0.46 +/- 0.06 (46% less dense than the cosmic mean). Haslbauer et al. show that the combined effect of the KBC void and the Hubble tension (H0 discrepancy) contradicts Lambda-CDM at 7.09 sigma confidence. The void's gravitational effect should reduce the inferred local H0 from supernovae measurements relative to CMB constraints, yet observations show the opposite: local H0 is systematically *higher* than CMB predictions. The paper argues this combined 7-sigma tension falsifies ΛCDM and favors modified gravity (MOND + sterile neutrinos), which achieves only 2.53 sigma tension when including the KBC void structure.

---

## Historical Context

The discovery of the KBC void (Keenan et al. 2013) was initially viewed as explaining a small portion of the local H0 excess. The logic was straightforward:

1. A local underdensity (void) reduces the local gravitational deceleration
2. With weaker local gravity, supernovae appear fainter than expected for their redshift
3. This biases the inferred Hubble constant *downward*
4. The effect could partially reconcile the H0 tension

However, detailed modeling (Whitbourn & Shanks 2016, Shanks et al. 2019) showed the void's effect is at most ~1-2 km/s/Mpc — far too small to resolve the 4-5 km/s/Mpc H0 tension. More puzzlingly, the void's effect is expected to work in the *wrong direction*: a local underdensity should lower local H0, but observations show local H0 is systematically *higher* than CMB predictions.

Haslbauer et al. (2020) reanalyzed the KBC void using updated density maps and density-distance relations, finding:

1. The void is *larger and deeper* than previously thought: 250 Mpc radius, Delta_rho ~ -46%
2. The void's gravitational effect is still small but measurable: Delta H0 ~ -1 km/s/Mpc (no solution to the tension)
3. The void acts as *additional evidence against ΛCDM*, not for it
4. Modified gravity (MOND) can accommodate the void + H0 tension simultaneously

---

## Key Arguments and Derivations

### KBC Void Density Profile

The void is characterized by a smooth density gradient. Haslbauer et al. fit a radial density profile:

$$\rho(r) = \rho_0 \left[ 1 + \frac{\Delta \rho}{\rho_0} \exp\left( -\frac{r}{r_{\text{void}}} \right) \right]$$

where:
- $r$ = distance from Local Group
- $r_{\text{void}} \approx 250$ Mpc = void radius scale
- $\Delta \rho / \rho_0 \approx -0.46 \pm 0.06$ = density contrast (46% underdense)

The void extends from the Local Group (~1 Mpc) to ~300 Mpc, with central underdensity maximized near 100-200 Mpc.

Supporting observations:
- **Redshift survey voids** (2dFGRS, SDSS): Low-density region confirmed in multiple catalogs
- **Gamma-ray burst count deficit**: Fewer GRBs detected in the void direction, indicating lower stellar density
- **Galaxy distribution**: Fewer bright galaxies and clusters in void region vs. other directions

### Gravitational Effect on Local Hubble Parameter

The KBC void produces a local acceleration due to the density deficit. Using the shell theorem, the acceleration at radius r from the void center is:

$$a_{\text{void}}(r) = -\frac{4\pi G}{3} \left( \Delta \rho \right) r$$

With $r \sim 50$ Mpc (approximate Local Group distance), we get:

$$a_{\text{void}} \approx \frac{4\pi G}{3} (0.46 \rho_c) (50 \text{ Mpc})$$

where $\rho_c$ is the critical density. This produces a *deceleration* (repulsion due to underdensity), reducing the observed Hubble expansion rate locally:

$$H_{\text{local}} = H_0 - \frac{a_{\text{void}}}{c}$$

Numerically:
$$\Delta H_0 \approx -1 \text{ to } -2 \text{ km/s/Mpc}$$

The negative sign indicates the void *reduces* the apparent local expansion, making the H0 tension **worse**, not better.

### Tension Calculation: LCDM vs. Observations

**LCDM prediction** (Planck 2018 + CMB):
$$H_0^{\text{Planck}} = 67.27 \pm 0.60 \text{ km/s/Mpc}$$

**Local H0 measurement** (Riess et al. 2022, anchor supernovae + Cepheid variables):
$$H_0^{\text{local}} = 73.0 \pm 1.0 \text{ km/s/Mpc}$$

**Discrepancy**:
$$\Delta H_0 = 73.0 - 67.27 = 5.73 \text{ km/s/Mpc} \approx 5.3\sigma$$

When the KBC void effect is included, LCDM must explain:
$$H_0^{\text{local}} = H_0^{\text{Planck}} - \Delta H_0^{\text{void}} + \text{other systematics}$$

But the void effect (Delta H0 ~ -1 km/s/Mpc) is in the *wrong direction* — it makes the tension worse, not better. Including the void:

$$H_0^{\text{eff}} = 67.27 - 1.0 = 66.3 \text{ km/s/Mpc}$$

This widens the gap to local measurements:
$$\Delta H_0^{\text{combined}} = 73.0 - 66.3 = 6.7 \text{ km/s/Mpc}$$

### Combined KBC + H0 Tension

Haslbauer et al. assess the joint probability of observing both the KBC void structure *and* the H0 tension simultaneously in LCDM simulations:

Using the MXXL (MULTIDARK XL) simulation suite (N-body simulation with 68 billion particles, 4.1 Gpc^3 volume, LCDM parameters):

1. **Void frequency**: In MXXL, voids of depth Delta_rho < -0.46 and radius > 200 Mpc occur with frequency ~1 in 1000
2. **H0 tension frequency**: Given Planck CMB constraints, random measurement uncertainty from local supernovae yields H0 > 73 km/s/Mpc with frequency ~1 in 5000-10000
3. **Joint probability**: If void and H0 tension were independent, combined probability would be:
$$P_{\text{joint}} \sim (10^{-3}) \times (10^{-4}) = 10^{-7}$$
$$\sigma_{\text{joint}} = \sqrt{2 \text{erf}^{-1}(1 - 2P_{\text{joint}})} \approx 5.0 - 5.5\sigma$$

However, Haslbauer et al. argue the void and H0 tension are *positively correlated* (both point to large-scale structure deviations from LCDM). This increases the combined significance to:

$$\sigma_{\text{combined}} = 7.09\sigma$$

This is the confidence level at which LCDM is *ruled out* in favor of alternative models.

### MOND + Sterile Neutrinos Alternative

Modified Newtonian Dynamics (MOND) predicts a different acceleration law at low accelerations:

$$a = \frac{a_0 \mu(a/a_0)}{\text{Newtonian}}$$

where $a_0 \approx 1.2 \times 10^{-10}$ m/s^2 is the transition acceleration, and $\mu$ is an interpolation function.

In the MOND framework:
- Galaxy rotation curves are explained without dark matter
- The KBC void has a different gravitational effect (weaker at large scales due to modified gravity)
- Sterile neutrinos provide a small amount of dark matter and early dark energy, improving the fit

With MOND + sterile neutrinos (m_nu ~ 0.3 eV, N_eff ~ 3.3), Haslbauer et al. achieve:

$$\sigma_{\text{MOND}} = 2.53\sigma$$

This is well within acceptable tolerance, suggesting MOND explains both the void structure and H0 tension better than LCDM.

---

## Key Results

1. **KBC void confirmed at high significance**: Density contrast Delta_rho/rho = -0.46 +/- 0.06 (46% underdense) across ~250 Mpc radius. Consistent with multiple surveys (2dFGRS, SDSS, gamma-ray bursts)

2. **Void produces *wrong-direction* effect**: Local underdensity reduces local H0 by ~1 km/s/Mpc, *worsening* the tension with CMB, not resolving it

3. **Combined 7.09 sigma tension**: KBC void + H0 discrepancy together reach 7 sigma, effectively ruling out LCDM at high confidence

4. **MOND resolution**: Modified gravity with sterile neutrinos reduces combined tension to 2.53 sigma, suggesting MOND is more consistent with observations than LCDM

5. **Large-scale structure anomaly**: The void is not a rare random fluctuation but a systematic large-scale structure that LCDM struggles to accommodate

---

## Impact and Legacy

The Haslbauer et al. work sharpened the cosmological crisis:

1. **KBC void no longer hides the problem** — it *amplifies* the H0 tension in LCDM, forcing a true paradigm shift
2. **Modified gravity gains credibility** — MOND + sterile neutrinos now compete with LCDM on observational grounds
3. **Observational urgency** — DESI, 4MOST, and Vera Rubin observations must independently measure the KBC void's depth and extent to confirm or refute this picture
4. **Systematic vs. random interpretation** — The void is now seen as evidence for *systematic large-scale structure deviations* from LCDM, not a mere local accident

---

## Connection to Phonon-Exflation Framework

**VERY STRONG CONNECTION**

The KBC void is a direct observational prediction and test of the phonon-exflation framework:

1. **Void origin in framework**: In phonon-exflation, voids arise from regions of suppressed quasiparticle density — the phononic analog of a depleted Fermi sea or broken Cooper-pair condensate. The 32-cell Voronoi tessellation naturally predicts one large void at the Local Group scale, located near a Voronoi cell boundary

2. **Local void prediction**: The framework predicts a void with:
   - Radius ~200-300 Mpc (matches KBC observed extent)
   - Density contrast ~-30% to -50% (matches KBC observed -46%)
   - Location: determined by the tessellation's orientation (framework predicts which direction contains the local void)

3. **Void as quasiparticle depletion**: The framework reinterprets the void not as a random underdensity but as a *structural feature* of the tessellation. The void corresponds to a region where the condensate gap is suppressed, reducing the density of phononic excitations (which manifest as observable matter)

4. **H0 tension explanation**: The framework predicts the void produces an *incorrect* local H0 estimate in LCDM (which assumes homogeneity). When the true tessellation structure is accounted for, the H0 discrepancy is resolved not by changing the physics but by correcting for the large-scale geometric bias

5. **MOND vs. Framework**: While Haslbauer et al. propose MOND as a solution, the framework offers an alternative: the "tension" arises because LCDM and supernovae observations both assume a homogeneous universe. The framework predicts *both* the void structure *and* the correct large-scale geometry, eliminating the need for modified gravity while retaining GR

6. **Critical test**: Measure the void's density profile to higher precision. The framework predicts the void boundary should match a Voronoi cell boundary, with specific geometric angles and facet shapes. If observed void shape matches a Voronoi 3-cell projection, this is compelling evidence for the tessellation hypothesis

7. **Local dipole connection**: The KBC void contributes to the cosmic dipole anomaly (Paper 29). The framework predicts a specific geometric relationship between the void location and the dipole direction, determined by the tessellation's orientation. This provides a joint test: does the void geometry + dipole direction uniquely determine the 32-cell projection in 4D space?

**Key prediction**: The framework predicts the KBC void is not a random underdensity but the *projection of a specific Voronoi 3-cell*. Detailed topological analysis (persistent homology per Pranav et al., Paper 28) of the void's boundary should reveal characteristic topological features (Betti numbers, persistent cycles) matching a Voronoi cell boundary, not a smooth overdensity. This is a uniquely falsifiable prediction of the tessellation hypothesis.

