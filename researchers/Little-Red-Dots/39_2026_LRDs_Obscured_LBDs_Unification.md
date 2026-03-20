# Little Red Dots as Obscured Little Blue Dots: Super-Eddington Unification

**Author(s):** Madau & Maiolino
**Year:** 2026
**Journal:** arXiv:2602.22386

---

## Abstract

The apparent dichotomy between "Little Blue Dots" (LBDs)—compact, blue, super-Eddington AGN at z~5-7—and "Little Red Dots" (LRDs)—compact, red, dust-obscured AGN at the same redshift—is reconciled in a unified model based on viewing geometry. Both populations represent the same physical phenomenon: compact, super-Eddington accretion systems. The difference arises from inclination angle and dust distribution. LBDs are viewed at low inclination (face-on), where direct view of the blue ultraviolet-to-optical continuum from the accretion disk dominates, combined with super-Eddington radiative winds. LRDs are the same systems viewed at high inclination (edge-on), where an equatorially concentrated dusty screen obscures the continuum while permitting infrared reprocessed light and scattered ultraviolet to escape. The geometrically thick, radiation-pressure-supported accretion flow naturally produces the required anisotropy in UV/optical continuum and broad-line emission. Self-shadowing suppresses the optical continuum in edge-on views, explaining the observed infrared-dominated colors and low optical luminosity of LRDs despite their high bolometric luminosity. The unification model predicts correlated trends in black hole mass estimates, Eddington ratios, and spectral properties as functions of inclination, and it resolves the apparent "overabundance" of both LRDs and LBDs: they are different views of a single population of early super-Eddington accreting systems. Implications for number density, redshift evolution, and formation mechanisms are reassessed.

---

## Historical Context

JWST discoveries at z~5-7 revealed two populations of compact, luminous sources previously unknown or extremely rare in lower-redshift surveys:

1. **Little Blue Dots (LBDs)**: Compact (r ~ 100-300 pc), blue (UV-optical colors), luminous (L ~ 10^45-10^47 erg/s) sources with clear evidence of super-Eddington accretion ($\lambda > 1-10$).

2. **Little Red Dots (LRDs)**: Compact (r ~ 100-300 pc), red (infrared-bright), luminous (L ~ 10^44-10^46 erg/s), dust-obscured sources with extreme infrared colors and X-ray faintness.

Initial interpretations treated these as distinct populations with different physical origins:
- **LBDs**: Young, recently assembled black holes at early epochs of rapid assembly, possibly with modified spectral energy distributions due to super-Eddington physics
- **LRDs**: Dust-enshrouded black holes with different seed origins (soliton collapse, direct collapse, mergers), dustier environments, or more advanced evolutionary state

However, this two-population model created difficulties:
- Why should super-Eddington accretion produce a compact LBD population AND a separately obscured LRD population?
- Why are the redshift distributions, number densities, and sizes so similar if they represent different physical systems?
- Why would dust distribution vary so dramatically between nominally similar early-epoch AGN?

Madau & Maiolino proposed an alternative: **the dichotomy is observational, not physical**. LRDs and LBDs are the same super-Eddington AGN systems viewed at different inclination angles.

---

## Key Arguments and Derivations

### Geometry of Super-Eddington Accretion Flows

At super-Eddington accretion rates ($\dot{M} > \dot{M}_{Edd}$), radiation pressure becomes important in the accretion disk dynamics. The disk structure transitions from a thin Shakura-Sunyaev disk (for $\lambda < 1$) to a thick, geometrically extended structure (for $\lambda > 1$).

The scale height of a super-Eddington disk is:

$$\frac{H}{R} \sim \frac{c_s}{v_K} \sim \sqrt{\frac{\lambda P}{w_e \rho_e c^2}}$$

where $c_s$ is the sound speed, $v_K$ is the Keplerian velocity, $P$ is the radiation pressure, $w_e$ is the electron scattering opacity, and $\rho_e$ is the electron density.

For $\lambda > 1$, radiation pressure dominates gas pressure, and $H/R$ can exceed unity—the disk becomes thicker than it is wide, transitioning to a "radiatively-inflated" or "slim disk" configuration.

The temperature in such a disk is:

$$T(R) \sim 10^4-10^5 \text{ K}$$

regardless of radius (in contrast to thin-disk Shakura-Sunyaev disks, where $T \propto R^{-3/4}$). This means the entire disk is hot, producing copious ultraviolet-to-optical radiation—the "blue" continuum characteristic of LBDs.

### Anisotropic Radiation and Dusty Torus

A key feature of thick accretion flows is **anisotropic radiation emission**. The radiation is preferentially beamed along the disk axis (the poles) due to:

1. **Radiation pressure winds**: Hot gas at the disk surface experiences strong radiation-driven outflows (winds) that create a low-density polar funnel
2. **Disk oblateness**: The inflated disk is thicker in the equatorial plane, naturally creating a hollow structure along the rotation axis
3. **Comptonization**: Radiation scattered in the hot disk preferentially escapes along directions of minimum optical depth—the polar axis

The result is an angular radiation pattern:

$$I(\theta) \propto \cos^2 \theta + \epsilon$$

where $\theta = 0$ is the polar axis and $\epsilon \sim 0.1-0.3$ is the isotropic component. Most radiation (70-80%) escapes along the poles; only ~10-30% escapes equatorially.

Now consider dust distribution. If dust surrounds the accretion flow with covering factor $f_c \sim 0.7-0.9$ and height profile concentrated toward the equator (as expected from viscous settling), then:

**For a face-on observer ($i \sim 0°$ inclination):**
- Direct view of the disk's ultraviolet-optical continuum: bright, blue
- Dust is "on the side," minimally obscuring the direct continuum
- Observed color: blue (dominated by direct UV/optical)
- Observed type: **Little Blue Dot**

**For an edge-on observer ($i \sim 90°$ inclination):**
- Direct view to disk blocked by equatorial dust
- Preferentially sees infrared-reprocessed dust emission (self-shadowing suppresses the optical continuum)
- Also sees scattered/reflected radiation from the polar outflow
- Observed color: red (dominated by thermal dust and scattered IR)
- Observed type: **Little Red Dot**

### Spectral Modeling and Self-Shadowing

The paper employs radiative transfer simulations to compute the observedspectral energy distribution (SED) as a function of inclination angle. The model includes:

1. **Accretion disk continuum**: Temperature profile assuming radiation-pressure-dominated disk: $T(R) \sim 10^4$ K
2. **Dust distribution**: Dusty torus with inner radius $R_{in} \sim 100$ gravitational radii, outer radius $R_{out} \sim 1000-10000 R_g$, vertical scale height $H/R \sim 0.3$
3. **Obscuration**: Compton-thick obscuration if dust column exceeds ~10^{24} cm^-2; partial obscuration otherwise
4. **Scattering**: Multiple scattering and dust reprocessing (absorption and re-emission in infrared)

Key results:

**Face-on view (i = 0°)**:
- Blue continuum flux: ~100% of intrinsic disk flux (unobscured)
- Infrared flux: ~10-20% (thermal dust emission in the outer torus, heated by scattered photons)
- Net color: B - V ~ -0.5 (blue)
- Apparent luminosity: L_obs ~ 0.9 L_intrinsic (only ~10% energy missing to dust heating)

**Edge-on view (i = 90°)**:
- Blue continuum flux: ~1-5% of intrinsic disk flux (obscured and scattered)
- Infrared flux: ~70-90% (thermal dust emission, reprocessing of absorbed UV/optical)
- Net color: B - V ~ +3-5 (very red)
- Apparent luminosity: L_obs ~ 0.8 L_intrinsic (energy is reprocessed, not lost; bolometric luminosity conserved)

The "self-shadowing" effect is crucial: the dust-obscured accretion disk does not emit blue optical light directly, but all the absorbed UV/optical energy is re-radiated in the infrared. Thus, edge-on sources appear infrared-luminous and blue-continuum-faint, matching LRD observations.

### Broad Emission Line Region Anisotropy

The broad-line region (BLR) in the super-Eddington geometry is expected to be clumpy and geometrically extended. A key prediction of the orientation-dependent model is that broad-line properties depend on inclination:

**Face-on geometry**:
- BLR clouds distributed throughout polar funnel
- Observer sees direct UV/optical continuum for photoionization
- Broad lines have profile set by cloud velocities plus radiation-driven outflow: FWHM ~ 1000-3000 km/s
- Broad-line equivalent widths are modest (EW ~ 50-200 Å)

**Edge-on geometry**:
- BLR clouds still distributed, but observer's line of sight to the continuum source (the disk) is obscured
- The disk's far side is illuminated; clouds there see the bright polar outflow or scattered radiation
- Broad-line equivalent widths become large (EW ~ 200-500 Å) because the observed optical continuum is suppressed by dust, making lines relatively more prominent
- Balmer lines (Hα, Hβ) show larger EW than [OIII] lines, consistent with observations

The paper quantifies:

$$\text{EW} = \frac{f_{line}}{f_{continuum}}$$

where $f_{line}$ is the line flux and $f_{continuum}$ is the continuum flux. For the same intrinsic line flux but suppressed continuum:

$$\text{EW}_{edge-on} = \text{EW}_{face-on} \times \frac{f_{continuum,face-on}}{f_{continuum,edge-on}} \sim 5-10 \times \text{EW}_{face-on}$$

This matches the observed difference in broad-line equivalent widths between LBDs and LRDs.

### Number Density Reconciliation

A puzzle was the apparent overabundance of both LBDs and LRDs: if they were separate populations, their combined number density would exceed hierarchical predictions. Under the unification model:

$$n_{total}(z) = n_{LBD}(z) + n_{LRD}(z) = n_{super-Eddington}(z)$$

is a single population viewed at different inclinations. The observed numbers are not additive but rather two views of one intrinsic population.

Under random inclination distribution, the fraction of the super-Eddington population appearing as LRDs is roughly the fraction of lines of sight with high inclination ($i > 60°$):

$$f_{LRD} = \int_{60°}^{90°} \sin i \, di / \int_{0°}^{90°} \sin i \, di = (1 - \sin 60°) / 1 \approx 0.13$$

Similarly, $f_{LBD} \approx 0.13$ (for low inclination, $i < 30°$), and $f_{intermediate} \approx 0.74$ (for intermediate inclinations).

The intrinsic number density of super-Eddington systems at z~5-7 must be:

$$n_{super-Edd}(z) = \frac{n_{LBD}(z)}{f_{LBD}} = \frac{n_{LRD}(z)}{f_{LRD}}$$

If observed $n_{LBD} \sim n_{LRD} \sim 0.01$ Gpc^{-3}, then:

$$n_{super-Edd} \sim 0.08 \text{ Gpc}^{-3}$$

This is still high but can be accommodated if super-Eddington accretion is a transient phase of black hole assembly, affecting ~10% of the high-z AGN population briefly (1-10 Myr timescales at a given epoch).

---

## Key Results

1. **Unified model explains LRD and LBD dichotomy**: Both populations are super-Eddington accreting systems; the observational differences (color, optical brightness) arise from viewing geometry, not fundamental physical differences.

2. **Self-shadowing effect naturally produces LRD colors**: Edge-on viewing of a thick accretion disk, combined with dust obscuration and reprocessing, produces the infrared-dominat continuum and red colors characteristic of LRDs.

3. **Broad-line equivalent widths depend on inclination**: Dust obscuration of the continuum source artificially inflates equivalent widths in edge-on views, explaining why LRDs show larger broad-line EW than LBDs.

4. **Number density resolved**: The apparent overabundance of LRDs + LBDs vanishes when recognized as a single population; the intrinsic density is ~0.08 Gpc^{-3}, consistent with (though still high) hierarchical assembly.

5. **Bolometric luminosity conserved**: LRDs are not intrinsically more luminous than LBDs; the infrared bright appearance is due to reprocessed (not newly emitted) radiation.

6. **Testable predictions**: The model predicts correlations between inclination indicator, black hole mass estimate, Eddington ratio, and spectral properties. Multi-wavelength follow-up should reveal systematic trends with viewing angle.

7. **Black hole growth timescale unified**: Both LRDs and LBDs represent the rapid-growth phase of early black holes, all occurring at z~5-7, not spread across redshifts.

---

## Impact and Legacy

This paper reframed the LRD problem from a population-abundance crisis to a pure viewing-geometry effect. It provided a unified framework for understanding compact, super-Eddington systems at all inclinations, parallel to the successful unification of Seyfert 1 and Seyfert 2 galaxies in local AGN.

The work has inspired:
- Detailed forward-modeling of individual LRD SEDs with geometric orientation parameters
- High-resolution infrared spectroscopy to measure dust column densities and geometry
- Searches for LBD/LRD pairs at similar redshifts to test orientation predictions
- Dust-emission mapping via submillimeter interferometry to constrain the torus structure

---

## Connection to Phonon-Exflation Framework

**PHENOMENOLOGICAL RELEVANCE**: The unification model addresses the *demographics* and *viewing geometry* of early AGN, not the *seeding mechanism*. It is compatible with any seed formation pathway (CDM direct collapse, ULDM, uSIDM, etc.).

**Seed mass implications**: If LRDs and LBDs are unified and both represent super-Eddington accretion at z~5-7, then their inferred black hole masses are the measured masses of this population. Under the unification model:
- Observed LRD masses (10^7-10^9 M_sun, before viewing-angle corrections) remain unchanged
- But the unification model suggests that orientation-dependent radiative transfer (self-shadowing) may affect mass estimates just as much as scattering processes do (Paper 37)
- Combined with selection bias corrections (Paper 38) and radiative transfer corrections (Paper 37), true masses may be lower by an order of magnitude, bringing them into CDM consistency

**Verdict**: This paper is a **geometry/phenomenology paper** that affects LRD mass estimates and number density interpretation. It does not directly test phonon-exflation's dark matter prediction but constrains the demographics of the early AGN population, which is relevant to the framework's predictions for early black hole assembly.
