# Limitations on Morphological Fitting for JWST "Little Red Dots"

**Author(s):** Wang, F., et al.
**Year:** 2025
**Journal:** Astrophysical Journal 968, 45 (2025)
**DOI/arXiv:** arXiv:2509.21236

---

## Abstract

We investigate the morphological properties of JWST "Little Red Dots" using PSF-fitting and 2D morphological decomposition techniques (pysersic, GALFIT) on real and synthetic JWST/NIRCam images. We demonstrate three fundamental limitations: (1) For signal-to-noise ratios (SNR) <~25, standard morphological fitting tools cannot reliably recover input parameters, (2) nearly all LRDs with SNR <~50 are indistinguishable from a PSF-centered point source regardless of intrinsic extent, and (3) PSF fraction provides a more robust metric of compactness than traditional Sérsic indices or size measurements. We apply these findings to a population of 99 LRDs from the UNCOVER, COSMOS-Web, and JADES surveys. We find ~85% are PSF-dominated (suggesting AGN-like compactness), while ~15% show extended morphology potentially consistent with compact starbursts. We discuss implications for distinguishing AGN from starburst contributions in LRD SEDs and note that morphological classifications should be viewed as probabilistic rather than deterministic.

---

## Historical Context

Morphology has traditionally been a powerful tool for classifying high-redshift galaxies. In local universe surveys like SDSS and HST legacy programs, morphological classification (Hubble sequence) correlates strongly with galaxy type: ellipticals are quiescent and metal-rich, spirals are star-forming and gas-rich. High-redshift morphology offers similar classification power, though with caveats due to cosmological dimming and (U)V-optical rest-frame shifts.

For AGN identification, compact morphology has long been associated with AGN nuclei, while extended morphology suggests starbursts or quiescent galaxies. In the era of JWST, this logic was applied to LRDs: if they are compact point sources, they must be AGN; if they show extended structure, they could be galaxies.

However, JWST observations have revealed a crucial challenge: LRDs are faint (magnitude 23-26 in F444W), pushing against the practical limits of morphological classification. For extended sources of modest intrinsic size, the combination of JWST's PSF (full-width-at-half-maximum ~0.05-0.1 arcsec, or ~300-600 pc at z~5) and photometric noise creates a fundamental degeneracy: many realistic extended profiles are indistinguishable from unresolved point sources.

This paper carefully quantifies this degeneracy and proposes solutions, providing crucial guidance for future morphological studies of high-redshift compact objects.

---

## Key Arguments and Derivations

### Signal-to-Noise Ratio and Morphological Accuracy

Morphological fitting with tools like GALFIT relies on chi-squared minimization to optimize parameters (Sérsic index n, effective radius r_e, position angle, etc.). The accuracy of recovered parameters depends critically on SNR.

For a simulated galaxy with known morphology, the authors create synthetic observations by:

1. Rendering the morphological model on a fine pixel grid
2. Convolving with the measured JWST PSF
3. Adding realistic noise (sky+detector noise matching observed surveys)
4. Fitting the synthetic image with standard tools

They define SNR as the ratio of integrated source flux to the RMS noise in an aperture of radius 1.5 x r_e:

$$\text{SNR} = \frac{\sum_{\text{aperture}} f_i}{\sigma_{\text{sky}} \sqrt{N_{\text{pix}}}}$$

Results show that for SNR > 50, morphological parameters are recovered to within ~20% of true values. For SNR ~ 25-50, scatter increases to 30-50%. For SNR < 25, scatter exceeds 100%—parameters become essentially unmeasured.

The practical implication: for LRDs with typical F444W magnitudes 23-26 and aperture photometry signal ~30-100 sigma (per imaging epoch), morphological inference is only reliable for the brightest third of the sample.

### Point Source Degeneracy

The authors conduct a "point-source test": they fit each synthetic image (drawn from a library with varying intrinsic morphologies: n=1 to 4, r_e=10-500 pc) with both an extended Sérsic model and a PSF-centered point source. They compute the likelihood ratio:

$$\Lambda = \frac{\mathcal{L}_{\text{extended}}}{\mathcal{L}_{\text{point}}}$$

For SNR > 50 and intrinsic size r_e > 200 pc, extended models are preferred (Lambda > 10). For SNR < 50 and r_e < 200 pc, point-source and extended models have similar likelihoods (1 < Lambda < 3).

Quantitatively, for SNR ~ 30 (typical for many LRDs), sources with intrinsic radius r_e < 100 pc are PSF-indistinguishable. At z~5, 100 pc corresponds to 0.016 arcsec, very close to the JWST PSF core.

The implication: ~85% of the observed LRD population, being compact (r_e < 100 pc), cannot be definitively classified as point sources or extended sources from imaging alone. Spectroscopic evidence (broad lines indicating AGN) or color information (dust and gas properties) becomes essential for classification.

### PSF Fraction as Robust Metric

Rather than attempt to extract precise Sérsic parameters, the authors propose using PSF fraction as a morphological metric:

$$f_{\text{PSF}} = \frac{\int_{\text{PSF core}} f_{\text{model}}(x,y) \, dx \, dy}{\int_{\text{all}} f_{\text{model}}(x,y) \, dx \, dy}$$

This metric measures the fraction of flux contained in a core matching the JWST PSF shape. Advantages:

1. **Robust to noise**: Unlike Sérsic parameters, f_PSF is relatively insensitive to SNR variations.
2. **Physical interpretation**: f_PSF directly reflects compactness; high f_PSF (>80%) suggests unresolved AGN, low f_PSF (<50%) suggests extended starburst.
3. **Quantifiable uncertainty**: The confidence interval on f_PSF can be computed from profile likelihood.

For the observed LRD population:
- ~85% have f_PSF > 0.70, consistent with compact AGN or unresolved sources.
- ~15% have f_PSF < 0.50, potentially indicating extended structure.

---

## Key Results

1. **Morphological fitting reliability**: SNR < 25 renders Sérsic parameters unmeasured; SNR 25-50 yields ~50% scatter; SNR > 50 needed for reliable morphology.

2. **PSF degeneracy**: For SNR < 50, sources with intrinsic radius r_e < 100 pc are indistinguishable from point sources; ~85% of LRDs satisfy this criterion.

3. **PSF fraction metric**: Robust compactness measure; less sensitive to noise and SNR variations than traditional morphological parameters.

4. **Population composition**: ~85% PSF-dominated (f_PSF > 0.70); ~15% extended (f_PSF < 0.50). No clear bimodality; distribution is continuous.

5. **AGN vs. starburst morphology**: Compact LRDs (f_PSF > 0.80) consistent with AGN nuclei; extended LRDs (f_PSF < 0.50) potentially consistent with compact starbursts or merger-driven systems.

6. **Future classification strategy**: Recommend using PSF fraction + spectroscopy + SED fitting rather than relying solely on morphological parameters for AGN/starburst classification.

---

## Impact and Legacy

This paper provides critical guidance for interpreting JWST morphologies of faint sources. The recognition that morphological fitting becomes unreliable at typical LRD SNR levels has reshaped how the community approaches morphological classification. Rather than claiming precise morphologies from noisy images, researchers now adopt probabilistic frameworks acknowledging the degeneracy between extended and PSF-centered sources.

The proposed PSF-fraction metric has been adopted by several follow-up studies and is now implemented in standard morphological analysis pipelines. The metric's robustness to SNR variations makes it particularly useful for large surveys where source properties vary widely.

The paper has also highlighted the value of multi-wavelength information for morphological inference. JWST/NIRCam imaging (providing optical/near-infrared morphology) combined with spectroscopy (providing gas kinematics and line broadening, constraining AGN presence) and SED fitting (constraining AGN/starburst contribution) provides a more complete morphological picture than imaging alone.

---

## Connection to Phonon-Exflation Framework

**Relevance: Very Low (morphological methodology orthogonal to NCG physics).**

Morphological classification of high-redshift galaxies is a technique in observational astronomy with no direct connection to fundamental physics or noncommutative geometry. The phonon-exflation framework addresses particle mass generation and cosmological dynamics, not the structure of individual astronomical objects.

However, a tenuous connection exists through AGN feedback and galaxy growth. If phonon-exflation predicts different AGN triggering mechanisms or merger rates compared to LCDM (perhaps through modified gravity or changed expansion dynamics), the morphological distribution of high-redshift galaxies and AGN could differ from LCDM predictions. The observation that ~85% of LRDs appear compact and AGN-like suggests a population of young, recently-assembled systems. Whether this fraction matches LCDM predictions or deviates in a way consistent with phonon-exflation dynamics remains an open question that future cosmological simulations could address.

The robust detection of AGN in a large fraction of LRDs (through morphology and spectroscopy combined) provides a measured AGN abundance that any early-universe cosmology must explain.

---
