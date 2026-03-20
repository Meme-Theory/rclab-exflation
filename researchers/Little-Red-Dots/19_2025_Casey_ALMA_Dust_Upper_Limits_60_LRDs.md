# An Upper Limit of 10^6 M_sun in Dust from ALMA Observations in 60 Little Red Dots

**Author(s):** Caitlin M. Casey, Hollis B. Akins, Steven L. Finkelstein, Maximilien Franco,
Seiji Fujimoto, Daizhong Liu, Arianna S. Long, Georgios Magdis, Sinclaire M. Manning,
Jed McKinney, Marko Shuntov, Takumi S. Tanaka
**Year:** 2025
**Journal:** Submitted to AAS journals (preprint)
**arXiv:** 2505.18873
**Submitted:** May 24, 2025

---

## Abstract

Casey et al. present ALMA 1.3 mm continuum observations targeting 60 photometrically selected
little red dots (LRDs) drawn from the COSMOS-Web and other JWST surveys. None of the 60 LRDs
are individually detected at the average depth of $\sigma_{\rm rms} = 22$ microJy per beam.
A statistical stack of all 60 sources also yields a non-detection. Converting the stacked flux
density upper limit to a dust mass constraint using modified blackbody models, the authors
find a $3\sigma$ upper limit of $M_{\rm dust} < 10^6 M_\odot$ per LRD. This is far below
the dust masses expected if the red optical continuum of LRDs arises from a dusty starburst
or heavily dust-obscured AGN at sub-mm wavelengths. The results favor interpretations in which
LRDs are reddened by compact but modest dust reservoirs, or alternatively by dense gas
producing extreme Balmer breaks rather than dust attenuation.

---

## Historical Context

### The Redness Problem

The defining spectral feature of LRDs -- beyond broad Balmer lines -- is the red optical
continuum: $F277W - F444W > 1$ mag (rest-frame $\sim 0.5$--$0.8$ micron in sources at $z \sim 5$).
Two broad explanations are debated:

1. **Dust reddening of AGN continuum**: The AGN power-law continuum ($F_\nu \propto \nu^{-\alpha}$
   with $\alpha \sim 1$--$2$) is reddened by dust along the line of sight. For visual extinction
   $A_V \sim 5$--$15$ mag, the UV is nearly extinguished while the near-IR remains visible,
   producing the observed red colors. This dust-reddened AGN model predicts substantial
   far-infrared/sub-mm emission from the warm dust: $F_{\rm 1.3mm} \sim$ microJy to tens of
   microJy for dust temperatures $T_{\rm dust} \sim 40$--$60$ K.

2. **Balmer break + dense gas**: High-column-density gas with $N_H \sim 10^{23}$--$10^{25}$
   cm$^{-2}$ can produce a steep Balmer break mimicking dust reddening in the rest-frame
   optical, without requiring large dust masses. This is the "gas cocoon" model. ALMA would
   not detect these sources since cold dust is absent.

ALMA observations directly discriminate between these scenarios: if dust is responsible for
LRD redness, ALMA should detect warm-to-cold dust emission at 1.3 mm; if gas is responsible,
ALMA should be silent.

### ALMA's Sensitivity and the LRD Scale

At $z \sim 5$, rest-frame far-infrared emission (at, say, $\lambda_{\rm rest} = 100$ micron,
$T_{\rm dust} = 50$ K) redshifts to $\lambda_{\rm obs} \approx 600$ micron. ALMA band 4
($\sim 1.3$ mm observed) probes rest-frame $\sim 220$ micron at $z = 5$, on the
Rayleigh-Jeans tail of a $T_{\rm dust} = 50$ K modified blackbody. Prior to Casey et al.,
individual ALMA observations of a handful of LRDs had found non-detections, but no systematic
study of 60 sources with consistent depth existed.

---

## Key Arguments and Derivations

### 1. Modified Blackbody Dust Mass Conversion

The observed 1.3 mm flux density from a modified blackbody at redshift $z$ is:

$$S_{\rm 1.3mm} = \frac{(1+z)}{D_L^2} \cdot \kappa_{\rm dust}(\nu_{\rm rest}) \cdot M_{\rm dust}
\cdot B_\nu(T_{\rm dust}, \nu_{\rm rest})$$

where $D_L$ is the luminosity distance, $\kappa_{\rm dust}$ is the dust mass opacity
coefficient (commonly taken as $\kappa_\nu \propto \nu^\beta$ with $\beta = 1.5$--$2.0$,
and $\kappa(850 \, \mu{\rm m}) \approx 0.077$ m$^2$ kg$^{-1}$), and $B_\nu$ is the Planck
function.

Inverting for dust mass:

$$M_{\rm dust} = \frac{S_{\rm 1.3mm} D_L^2}{(1+z) \kappa_{\rm dust}(\nu_{\rm rest}) B_\nu(T_{\rm dust})}$$

For $z = 5$, $D_L = 47$ Gpc, $T_{\rm dust} = 50$ K, and the $3\sigma$ upper limit
$S_{\rm 1.3mm} < 66$ microJy (from the stack), this yields:

$$M_{\rm dust} < 10^6 M_\odot$$

This upper limit is robust to temperature assumptions within the plausible range
$T_{\rm dust} = 30$--$100$ K at the factor-of-few level.

### 2. Comparison to Dust-Reddened AGN Predictions

If LRD redness is due to dust extinction with $A_V \sim 5$ mag (a typical value inferred from
fitting the red slope), the gas-to-dust ratio implies a total dust mass along the line of
sight:

$$M_{\rm dust,los} = N_H m_H \frac{1}{\delta_{\rm gas/dust}} \cdot A_{\rm cover}$$

For a standard Milky Way gas-to-dust ratio $\delta \sim 100$, a column $N_H \sim 10^{23}$
cm$^{-2}$, and a covering area $A_{\rm cover} \sim (10 \, \rm pc)^2 = (3 \times 10^{19} \,
\rm cm)^2$:

$$M_{\rm dust,los} \sim 10^6 M_\odot$$

So the ALMA upper limit is right at the edge of what is needed to produce the observed $A_V$
if the dust geometry is compact and the gas-to-dust ratio is Milky Way-like. However, for
a larger covering area or warmer dust temperatures, the predicted ALMA flux would be
detectable but is not seen. This places LRDs in the regime of "compact but modest" dust
reservoirs, not the massive dusty starbursts seen in submillimeter galaxies (SMGs).

### 3. Stacking Methodology

The stack uses a weighted mean:

$$S_{\rm stack} = \frac{\sum_i w_i S_i}{\sum_i w_i}, \quad w_i = \frac{1}{\sigma_i^2}$$

where $S_i$ is the flux density in a fixed aperture centered on the JWST-determined LRD
position and $\sigma_i$ is the local ALMA noise. The stack reaches an effective depth of
$\sigma_{\rm stack} = 22/\sqrt{60} \approx 2.8$ microJy -- an order of magnitude deeper
than individual pointings. Non-detection at this depth requires:

$$M_{\rm dust} < 1.3 \times 10^5 M_\odot \quad (T_{\rm dust} = 50 \, \rm K, z = 5)$$

for the average LRD, or $< 10^6 M_\odot$ allowing for colder temperatures and lower redshift.

### 4. Implications for the Blue UV Component

Interestingly, the blue UV arm of the V-shape SED constrains the star formation rate (SFR)
in LRDs. If the UV is star-formation-powered:

$${\rm SFR} = 1.4 \times 10^{-28} \, L_{1500} \, M_\odot \, {\rm yr}^{-1}$$

Typical LRD UV luminosities imply SFR $\sim 1$--$10 M_\odot$ yr$^{-1}$. At these SFRs,
the infrared luminosity from dust heated by star formation (via the Kennicutt relation) is:

$$L_{\rm IR} \approx 10^{10}$--$10^{11} L_\odot$$

corresponding to $S_{\rm 1.3mm} \sim 0.1$--$1$ microJy at $z \sim 5$ -- well below the
ALMA detection limit per pointing but marginally consistent with the stack upper limit.
The ALMA non-detection is therefore consistent with SFR-heated dust at the levels implied
by the UV.

---

## Key Results

1. None of 60 LRDs individually detected by ALMA at 1.3 mm ($\sigma_{\rm rms} = 22$ microJy).
2. Stacked upper limit: $M_{\rm dust} < 10^6 M_\odot$ per LRD at $3\sigma$.
3. Tension with dusty-AGN models predicting $M_{\rm dust} \gg 10^6 M_\odot$ for $A_V > 5$ mag
   over extended (>100 pc) dust distributions.
4. Results favor compact but modest dust reservoirs or gas-dominated Balmer break models (no
   large cold dust component).
5. Upper limits consistent with SFR $\sim 1$--$10 M_\odot$ yr$^{-1}$ from UV-heated dust.
6. Largest homogeneous ALMA LRD study to date: N = 60 with consistent observing strategy.

---

## Impact and Legacy

Casey et al. (2025) provides a decisive observational constraint that rules out the most
extreme "massive dusty starburst" interpretation of LRDs. The result shifts the debate toward
the "gas cocoon" models (Rusakov et al. 2025; Inayoshi et al. 2024), in which dense ionized
gas rather than cold dust produces the spectral redness. It also motivates ALMA follow-up at
shorter wavelengths (Band 6, 7, 8) where warmer, compact dust would be more detectable, and
where the radio spectral energy distribution can be better characterized to search for
synchrotron vs. free-free dominated emission.

As a co-author list, this paper concentrates much of the LRD observational community
(Casey, Finkelstein, Akins, Fujimoto, McKinney, Shuntov, Tanaka) and represents a community-
wide consensus effort on the dust content question.

---

## Connection to Phonon-Exflation Framework

The ALMA non-detection of cold dust in LRDs is conceptually related to a recurring theme in
phonon-exflation: quantities that are "missing" from observations despite naive theoretical
expectations. In the framework, the spectral action predicts certain features of the particle
mass spectrum (phi_paasch ratio, inter-sector mass ratios) that require specific internal
geometry; similarly, the dust content of LRDs is expected from naive reddening models but not
observed. Both cases involve constraints that rule out the "obvious" mechanism and point to
something more subtle.

The dust mass upper limit ($< 10^6 M_\odot$) corresponds to a dust-to-gas ratio constraint
in the early universe. If phonon-exflation modifies the effective nucleosynthesis yields by
altering particle masses (a prediction of the framework in principle, though Session 24a found
the neutrino R ~ 10^14, far outside the observed range [17, 66]), the dust production history
would be affected. This LRD constraint is thus part of the broader observational dataset
against which any modification of early-universe particle physics must be tested.
