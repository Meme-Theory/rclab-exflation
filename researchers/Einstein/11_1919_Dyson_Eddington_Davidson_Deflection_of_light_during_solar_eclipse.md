# A Determination of the Deflection of Light by the Sun's Gravitational Field, from Observations Made at the Total Eclipse of May 29, 1919

**Authors:** Frank Watson Dyson, Arthur Stanley Eddington, Charles Rundle Davidson
**Year:** 1920 (observations 1919)
**Journal:** *Philosophical Transactions of the Royal Society of London*, Series A, **220**, 291--333

---

## Abstract

This paper reports the results of two British expeditions organized to observe the total solar eclipse of May 29, 1919, from Sobral (Brazil) and Principe (West Africa), with the specific goal of testing Einstein's general theory of relativity against the Newtonian prediction for the deflection of starlight passing near the Sun. GR predicts a deflection of $1.75''$ for a ray grazing the solar limb, exactly twice the Newtonian value of $0.87''$. The Sobral astrographic plates gave $1.98'' \pm 0.12''$ and the Principe plates gave $1.61'' \pm 0.30''$, both consistent with Einstein's prediction and inconsistent with both zero deflection and the Newtonian value. The announcement of these results at a joint meeting of the Royal Society and the Royal Astronomical Society on November 6, 1919, catapulted Einstein to worldwide fame and established general relativity as the successor to Newtonian gravity.

---

## Historical Context

### The Two Predictions

Einstein himself had predicted the deflection of light by gravity on two separate occasions, arriving at two different answers:

**1911 (Equivalence Principle only):** Using only the equivalence principle -- that a photon in a gravitational field gains energy (blueshift) and thus behaves as though it has an effective mass $m = E/c^2$ -- Einstein predicted a deflection angle:

$$\delta_{Newton} = \frac{2GM}{c^2 b}$$

where $M$ is the Sun's mass and $b$ is the closest approach distance (impact parameter). For grazing incidence ($b = R_\odot$):

$$\delta_{Newton} = \frac{2 \times 6.674\times10^{-11} \times 1.989\times10^{30}}{(2.998\times10^8)^2 \times 6.96\times10^8} \approx 0.87''$$

This is identically the value that follows from Newtonian gravity applied to a particle of mass $m = E/c^2$ passing the Sun. (Soldner had computed essentially this value in 1801, though using corpuscular theory.)

**1915 (Full General Relativity):** The complete GR calculation, using the Schwarzschild metric (or equivalently, the linearized GR solution), gives exactly twice this value:

$$\delta_{GR} = \frac{4GM}{c^2 b} = 2\delta_{Newton}$$

For grazing incidence:

$$\delta_{GR} \approx 1.75''$$

The factor of 2 arises because, in GR, both the temporal curvature (gravitational time dilation, equivalent to the Newtonian calculation) AND the spatial curvature (the bending of space near the Sun) contribute equally to the total deflection. The Newtonian/equivalence-principle calculation captures only the temporal part.

### Why a Solar Eclipse?

To observe starlight deflected by the Sun requires seeing stars very close to the Sun on the sky -- which is normally impossible because of the Sun's glare. During a total solar eclipse, the Moon blocks the Sun's disk, allowing stars within a few solar radii to be photographed. By comparing the positions of these stars during the eclipse with their normal (nighttime) positions (photographed months earlier or later), the deflection can be measured.

### The 1919 Eclipse

The eclipse of May 29, 1919, was particularly favorable: the Sun was in the Hyades star cluster (part of Taurus), an unusually rich field of bright stars near the Sun's position on the sky. This maximized the number of measurable star images.

Frank Dyson, the Astronomer Royal, organized two expeditions:
- **Sobral, Brazil:** Led by Andrew Crommelin and Charles Davidson, using two instruments (an astrographic telescope and a 4-inch lens).
- **Principe Island, West Africa:** Led by Arthur Eddington and Edwin Cottingham, using an astrographic telescope.

### Eddington's Motivations

Eddington was one of the few British scientists who understood general relativity (having been introduced to it through de Sitter). He was also a Quaker and conscientious objector; the eclipse expeditions partly shielded him from conscription controversies. Beyond personal considerations, Eddington was genuinely convinced of GR's elegance and saw the eclipse test as an opportunity to demonstrate a British-German scientific collaboration in the aftermath of World War I.

---

## Key Arguments and Derivations

### I. The GR Deflection Calculation

The deflection of light in the Schwarzschild geometry can be derived from the null geodesic equation. For a photon with impact parameter $b$ passing a mass $M$, the deflection angle in the weak-field limit ($r_s = 2GM/c^2 \ll b$) is:

$$\delta = \frac{2r_s}{b} = \frac{4GM}{c^2 b}$$

**Derivation sketch:** In Schwarzschild coordinates, a null geodesic in the equatorial plane satisfies:

$$\left(\frac{du}{d\phi}\right)^2 = \frac{1}{b^2} - u^2 + r_s u^3$$

where $u = 1/r$. The unperturbed solution (straight line) is $u_0 = \sin\phi/b$. The perturbation from the $r_s u^3$ term gives:

$$u = \frac{\sin\phi}{b} + \frac{r_s}{2b^2}(1 + \cos^2\phi)$$

The asymptotic angles (where $u \to 0$) are $\phi = -\delta/2$ and $\phi = \pi + \delta/2$, giving:

$$\delta = \frac{2r_s}{b} = \frac{4GM}{c^2 b}$$

The factor-of-2 difference from the Newtonian prediction can be traced to the spatial metric perturbation $h_{rr} = r_s/r$, which contributes equally to the deflection as the temporal perturbation $h_{00} = -r_s/r$.

### II. The Observational Method

The measurement involves comparing two photographic plates:
1. **Eclipse plate:** Stars near the Sun, photographed during totality.
2. **Comparison plate:** The same star field photographed at night (months before or after), when the Sun is far away.

The positions of stars on both plates are measured with a micrometer. The differences in position (eclipse minus comparison) should show a radial pattern centered on the Sun's position, with amplitude:

$$\delta(r) = \frac{1.75''}{r/R_\odot}$$

where $r$ is the angular distance from the Sun's center.

In practice, the measurement is complicated by:
- **Plate scale differences:** The two plates may have slightly different magnifications due to temperature changes in the optics.
- **Plate rotation and translation:** The overall orientation and center of the plates must be matched.
- **Optical aberrations:** The telescope optics introduce systematic distortions.
- **Atmospheric refraction:** Differential refraction across the field.

These systematic effects must be modeled and removed before the gravitational deflection can be extracted.

### III. Results

**Sobral (astrographic):** 7 stars measured. Mean deflection at the limb: $1.98'' \pm 0.12''$.

**Sobral (4-inch):** 5 stars measured, but images were out of focus due to a mirror distortion from solar heating. These gave $0.93''$, close to the Newtonian prediction, but were judged unreliable due to the systematic focus error.

**Principe:** 5 stars measured, only 2 with useful precision (clouds obscured the field for most of totality). Mean deflection at the limb: $1.61'' \pm 0.30''$.

**Combined result:** Consistent with the GR prediction of $1.75''$. Inconsistent with the Newtonian prediction of $0.87''$ at $>2\sigma$. Inconsistent with zero deflection at $>10\sigma$.

### IV. Statistical Assessment

By modern standards, the 1919 measurements were marginal. The Principe result barely discriminated between GR and Newton (the error bar of $0.30''$ is comparable to the $0.88''$ difference between the two predictions). The rejection of the Sobral 4-inch data was scientifically justified (the focus problem was documented) but has attracted retrospective criticism.

However, the combination of the two independent measurements, from different instruments at different sites, showing consistent GR-level deflection, was compelling to the contemporary scientific community.

---

## Physical Interpretation

### Light Has Weight (But Not the Newtonian Amount)

The observation demonstrates that photons are affected by gravity, as expected from the equivalence principle. But the magnitude of the effect reveals the additional contribution of spatial curvature, which is unique to GR. In Newtonian gravity (treating light as particles with mass $E/c^2$), only the time-time component of the metric contributes. In GR, the spatial components contribute equally, doubling the deflection.

### Curved Spacetime is Physical

The 1919 result provided the first direct evidence that spacetime is curved by mass. The Mercurian perihelion advance (43"/century) was explainable by GR but had pre-existing alternative explanations (oblateness of the Sun, an additional planet). The light deflection had no Newtonian explanation at the correct magnitude and was therefore a cleaner test.

### The Breakdown of Euclidean Space

The spatial curvature that produces the extra factor of 2 means that the geometry of space near the Sun is non-Euclidean. The spatial metric near the Sun is:

$$dl^2 = \left(1 + \frac{r_s}{r}\right)dr^2 + r^2(d\theta^2 + \sin^2\theta\,d\phi^2)$$

The radial distances are stretched relative to Euclidean geometry. This departure from flat space is directly observable through the light deflection.

---

## Impact and Legacy

### Einstein Becomes Famous

The announcement of the results on November 6, 1919, at a joint meeting of the Royal Society and the Royal Astronomical Society, was front-page news worldwide. The *Times* of London headlined: "REVOLUTION IN SCIENCE / NEW THEORY OF THE UNIVERSE / NEWTONIAN IDEAS OVERTHROWN." Einstein became the most famous scientist in the world, a status he retained for the rest of his life.

J.J. Thomson, President of the Royal Society, declared it "one of the greatest achievements in the history of human thought."

### Subsequent Eclipse Measurements

Later eclipse measurements (1922, 1929, 1947, 1952, 1973) improved the precision but were always limited by the systematics of optical astrometry during the few minutes of totality. The best optical results achieved uncertainties of about 10%.

### Radio Interferometry

The decisive improvement came with radio astronomy. Quasars (distant, compact radio sources) pass behind the Sun annually, and their positions can be measured with very long baseline interferometry (VLBI) to milliarcsecond precision. Shapiro et al. (1971) and subsequent VLBI measurements confirmed the GR deflection to better than 0.01%.

### Gravitational Lensing

The deflection of light by gravity has become one of the most powerful tools in observational astronomy:

- **Strong lensing:** Multiple images, arcs, and Einstein rings from galaxies and clusters (first observed by Walsh et al., 1979).
- **Weak lensing:** Statistical distortion of background galaxy shapes, used to map dark matter distributions.
- **Microlensing:** Transient brightening of background stars by foreground objects, used to detect exoplanets and compact dark objects.

All of these phenomena are quantitative predictions of GR, computed from the lens equation:

$$\beta = \theta - \frac{D_{LS}}{D_S}\alpha(\theta)$$

where $\alpha(\theta) = 4GM/(c^2 D_L \theta)$ is the deflection angle, $D_L$, $D_S$, $D_{LS}$ are angular diameter distances, and $\beta$, $\theta$ are source and image positions.

---

## Connections to Modern Physics

### Gravitational Lensing and Cosmology

Gravitational lensing is now one of the primary probes of cosmological parameters. Weak lensing surveys (DES, HSC, Euclid, Rubin Observatory) constrain the matter power spectrum and the growth of structure. The lensing power spectrum:

$$C_\ell^{\kappa\kappa} = \int_0^{\chi_s} d\chi\;\frac{W^2(\chi)}{\chi^2}\;P_\delta\left(\frac{\ell}{\chi}, z(\chi)\right)$$

depends on the matter power spectrum $P_\delta$ and the expansion history, making it sensitive to dark energy, neutrino masses, and modified gravity.

### Light Deflection as a Test of Alternative Theories

The parameterized post-Newtonian (PPN) framework parameterizes the light deflection as:

$$\delta = \frac{(1 + \gamma)}{2}\frac{4GM}{c^2 b}$$

where $\gamma = 1$ in GR. The Cassini spacecraft measurement (Bertotti et al., 2003) gives $\gamma = 1 + (2.1 \pm 2.3) \times 10^{-5}$, confirming GR to 0.002%.

### Lensing Without Dark Matter?

The observed gravitational lensing in galaxy clusters (including the Bullet Cluster, 1E 0657-56) is often cited as evidence for dark matter, since the lensing mass centroid is offset from the visible baryonic mass. However, the interpretation depends on assumptions about the gravitational theory. In modified gravity theories (MOND, TeVeS) or in frameworks that reinterpret mass-energy contributions, the lensing data constrains but does not uniquely determine the dark matter hypothesis. The distinction between observational data (lensing maps) and theoretical interpretation (dark matter particles) is precisely the epistemological issue at stake in evaluating alternative frameworks.

### The Shadow of M87*

The Event Horizon Telescope image of M87* (2019) shows the shadow of the black hole surrounded by a bright ring of lensed emission. The ring diameter is determined by the photon orbit at $r = 3GM/c^2$, where the deflection becomes infinite. This is the strong-field generalization of the weak-field deflection measured in 1919.
