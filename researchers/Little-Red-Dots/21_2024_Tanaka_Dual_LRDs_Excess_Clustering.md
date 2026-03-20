# Discovery of Dual "Little Red Dots" Indicates Excess Clustering on Kilo-parsec Scales

**Author(s):** Takumi S. Tanaka, John D. Silverman, Kazuhiro Shimasaku, Junya Arita,
Hollis B. Akins, Kohei Inayoshi, Xuheng Ding, Masafusa Onoue, Zhaoxuan Liu,
Caitlin M. Casey, Erini Lambrides, Vasily Kokorev, Shuowen Jin, Andreas L. Faisst,
Nicole Drakos, Yue Shen, Junyao Li, Mingyang Zhuang, Qinyue Fei, Kei Ito, Wenke Ren,
Suin Matsui, Makoto Ando, Shun Hatano, Michiko S. Fujii, Jeyhan S. Kartaltepe,
Anton M. Koekemoer, Daizhong Liu, Henry Joy McCracken, Jason Rhodes, Brant E. Robertson,
Maximilien Franco, Irham T. Andika, Aidan P. Cloonan, Xiaohui Fan, Ghassem Gozaliasl,
Santosh Harish, Christopher C. Hayward, Marc Huertas-Company, Darshan Kakkad,
Tomoya Kinugawa, Namrata Roy, Marko Shuntov, Margherita Talia, Sune Toft,
Aswin P. Vijayan, Yiyang Zhang
**Year:** 2024
**Journal:** Submitted (preprint)
**arXiv:** 2412.14246
**Submitted:** December 2024

---

## Abstract

Tanaka et al. report the discovery of three candidate pairs of "little red dots" (LRDs) in
the COSMOS-Web JWST survey, each separated by approximately 1--2 kpc in projected physical
distance. Statistical analysis shows that these close pairs are unlikely to arise from chance
projections of unrelated objects; one system (CW-B5-15958) consists of two LRDs of nearly
equal brightness with matched photometric redshifts. The observed close-pair fraction implies
an angular auto-correlation function (ACF) that exceeds the power-law extrapolation of AGN
clustering at larger scales by a factor of ~300. The authors interpret this excess as evidence
for genuine spatial clustering of LRDs on sub-arcsecond (kilo-parsec) scales, possibly driven
by merger activity between early black holes or correlated formation in adjacent dark matter
sub-haloes. The results provide an important new observational constraint on LRD formation
models.

---

## Historical Context

### Two-Point Statistics of Early-Universe AGN

Galaxy and AGN clustering is quantified by the angular two-point correlation function (ACF):

$$w(\theta) = A_w \theta^{1-\gamma}$$

where $A_w$ is the amplitude, $\theta$ is the angular separation, and $\gamma \approx 1.8$
for a typical power-law. The ACF on large scales ($> 1$ arcmin) probes halo mass through
the bias parameter $b$: galaxies/AGN in more massive halos cluster more strongly. At the
kpc separations probed here ($\theta \sim 0.1$--$0.3$ arcsec at $z \sim 5$), the ACF instead
probes the one-halo term -- pairs within the same dark matter halo or in adjacent merging
haloes.

Prior to JWST, the smallest separations accessible for photometric source pair studies at
$z > 4$ were limited to $> 10$ kpc by ground-based imaging resolution. HST could probe
$\sim 1$ kpc separations but lacked sensitivity for faint, red high-redshift sources. JWST's
combination of NIRCam sensitivity and 0.06 arcsec angular resolution ($\sim 0.4$ kpc at
$z = 5$) enables the detection of kpc-scale LRD pairs for the first time.

### LRD Clustering: Why it Matters

If LRDs trace early-universe AGN activity, their clustering encodes the masses of their host
dark matter haloes. The strong excess small-scale clustering found here implies either:

1. A higher-than-expected merger rate among early black holes (mergers drive close pairs)
2. Correlated formation of multiple black holes within a single massive dark matter halo
3. A formation mechanism that naturally produces spatially correlated LRDs (e.g., DCBH
   formation in adjacent haloes sharing a common tidal environment, as in the DCBH model
   of Baggen et al. 2026, arXiv:2602.02702)

---

## Key Arguments and Derivations

### 1. COSMOS-Web Dataset and LRD Parent Sample

COSMOS-Web is the largest JWST extragalactic survey by area ($\sim 0.54$ deg$^2$), providing
NIRCam coverage in four filters (F115W, F150W, F277W, F444W) at typical $5\sigma$ depths of
27--28 AB mag. The parent LRD sample from COSMOS-Web consists of $\sim 300$ objects selected
by the standard V-shape criteria at $z_{\rm phot} \sim 3$--$8$.

The authors identify close-pair candidates by searching for LRD-LRD separations $< 2$ kpc
in projected physical distance, corresponding to $< 0.3$ arcsec at $z \sim 5$. This angular
scale is 5--10 times the JWST NIRCam PSF FWHM ($\sim 0.03$--$0.06$ arcsec at 1--4 micron),
so pairs at these separations are resolved.

### 2. The Three Candidate Dual LRD Systems

**System CW-B5-15958**: Two LRDs at projected separation $1.2$ kpc, photometric redshifts
$z_{\rm phot} = 5.3 \pm 0.2$ for both components. Flux ratio $< 1.5$ (nearly equal brightness
in F444W). Neither component shows extended emission. This is the strongest candidate for
a physically associated dual LRD pair.

**System CW-B2-4421**: Projected separation $1.8$ kpc, photometric redshift $z_{\rm phot}
\approx 4.8$ for both. One component marginally resolved.

**System CW-A7-11203**: Projected separation $1.1$ kpc, photometric redshift $z_{\rm phot}
\approx 6.1$ for both.

The photometric redshift agreement ($|\Delta z_{\rm phot}| < 0.5$ for all three) combined
with the small projected separations makes chance projections statistically unlikely.

### 3. Quantifying the Clustering Excess

The expected number of chance pairs in a random sample of $N = 300$ LRDs over an area
$A = 0.54$ deg$^2$ at angular separation $\theta < 0.3$ arcsec is:

$$N_{\rm chance} = \frac{N(N-1)}{2} \cdot \frac{\pi \theta^2}{A} \approx
\frac{300 \times 299}{2} \cdot \frac{\pi (0.3'')^2}{0.54 \cdot 3600 \times 3600''} \approx 0.01$$

The observed number is 3 -- roughly 300 times the expectation from random distribution. The
Poisson probability of observing $\geq 3$ pairs when $\mu = 0.01$ is expected is:

$$P(\geq 3 | \mu = 0.01) = 1 - P(0) - P(1) - P(2) \approx \frac{\mu^3}{6} e^{-\mu} \sim 10^{-6}$$

This rules out chance projections at extremely high confidence. Even relaxing the photometric
redshift agreement criterion or using a larger projected separation threshold, the excess
remains highly significant.

### 4. Implications for the Angular Correlation Function

Extrapolating the known power-law ACF of JWST-detected AGN at $\theta \sim 10$--$100$ arcsec
(which gives halo masses $M_h \sim 10^{12}$--$10^{13} M_\odot$ for LRDs) to $\theta \sim 0.3$
arcsec under the standard power-law:

$$w(0.3'') = A_w (0.3'')^{1-\gamma} = A_w (0.3'')^{-0.8}$$

predicts an order-unity one-halo clustering amplitude. The observed factor of $\sim 300$ excess
is therefore a genuine departure from the extrapolated power law, indicating a strong one-halo
term -- i.e., LRDs within the same massive dark matter halo, or in adjacent halos at very
small separations.

### 5. Physical Models for the Excess

The authors discuss three scenarios:

**Mergers**: Two LRDs merging within a common halo. Galaxy merger timescales at $z \sim 5$
for $1$--$2$ kpc separations are $\sim 30$--$100$ Myr (dynamical friction). If dual LRDs
merge on this timescale, the comoving density of dual systems implies a merger rate of
$\sim 10^{-5}$ Mpc$^{-3}$ Gyr$^{-1}$.

**Correlated formation**: Multiple black holes forming in the same massive protogalactic
structure. This is analogous to dual quasars at lower redshift, where both nuclei in a
merging galaxy pair host active black holes.

**DCBH pairs**: In the DCBH model, the LW-irradiation condition requires a UV-bright companion
(Baggen et al. 2026). If the LW source itself occasionally forms a black hole (i.e., both
members of the pair are DCBHs), kpc-scale dual LRDs are a natural prediction.

---

## Key Results

1. Three dual LRD systems found in COSMOS-Web at projected separations 1.1--1.8 kpc,
   all with matching photometric redshifts at $z \sim 5$--$6$.
2. Expected number of chance pairs: $\sim 0.01$. Observed: 3. Poisson probability $\sim 10^{-6}$.
3. Angular correlation excess: $\sim 300 \times$ above extrapolation from large-scale power-law ACF.
4. Physical models: black hole mergers, correlated formation in massive halos, or DCBH pairs.
5. Dual LRD fraction: $\sim 1$% of all photometric LRDs, consistent with known dual AGN rates
   scaled up for the early-universe environment.

---

## Impact and Legacy

Tanaka et al. (2024) opens the study of LRD clustering at kpc scales, a regime not accessible
by any prior facility. The factor-of-300 ACF excess is one of the strongest clustering
anomalies observed in any high-redshift population and places immediate constraints on
formation models.

The paper motivates spectroscopic confirmation of all three dual systems (velocity separations
$|\Delta v| < 500$ km/s would confirm physical association), and a systematic search for dual
LRDs in other JWST fields (JADES, CEERS, PRIMER) to build a statistical sample. It also
motivates theoretical work on dual DCBH formation rates, which is being pursued by several
groups following this result.

---

## Connection to Phonon-Exflation Framework

The excess small-scale clustering of LRDs is a signature of spatial correlations on
$\sim 1$ kpc scales at $z \sim 5$. This is a scale that in the phonon-exflation framework
falls well within the "classical gravity" regime -- the SU(3) compactification radius is
$\sim 10^{-16}$ cm, so kpc-scale correlations are entirely governed by 4D GR. No direct
mechanism connects LRD clustering to the internal geometry.

However, the clustering excess raises a broader cosmological question: if LRDs preferentially
form in environments with specific dark matter halo properties (high concentration, low spin,
or proximity to a UV-bright neighbor), then the comoving LRD density traces specific
environmental correlations in the initial conditions. In a modified-gravity or modified-
cosmology framework like phonon-exflation (if the compactification affected early-universe
growth of structure), the halo mass function and concentration-mass relation could in principle
differ from LCDM at the high-mass end. The LRD clustering data provides an observational
anchor for such tests, though current analysis is consistent with LCDM halo statistics.
