# Lonely Little Red Dots: Challenges to the AGN-nature of Little Red Dots through Their Clustering and Spectral Energy Distributions

**Author(s):** Maria Carranza-Escudero, Christopher J. Conselice, Nathan Adams, Thomas Harvey,
Duncan Austin, Peter Behroozi, Leonardo Ferreira, Katherine Ormerod, Qiao Duan,
James Trussler, Qiong Li, Lewi Westcott, Rogier A. Windhorst, Dan Coe, Seth H. Cohen,
Cheng Cheng, Simon P. Driver, Brenda Frye, Lukas J. Furtak, Norman A. Grogin,
Nimish P. Hathi, Rolf A. Jansen, Anton M. Koekemoer, Madeline A. Marshall,
Rosalia O'Brien, Norbert Pirzkal, Maria Polletta, Aaron Robotham, Michael J. Rutkowski,
Jake Summers, Stephen M. Wilkins, Christopher N. A. Willmer, Haojing Yan, Adi Zitrin
**Year:** 2025
**Journal:** The Astrophysical Journal Letters, Volume 989, L50 (2025)
**arXiv:** 2506.04004

---

## Abstract

Carranza-Escudero et al. present a multi-survey photometric study of 124 LRDs at $z \sim 3$--$10$
drawn from the CEERS, NEP-TDF, JADES, and JEMS JWST surveys. Two independent lines of
evidence challenge the AGN-dominated interpretation: (1) SED fitting using Bayesian model
comparison shows that models WITHOUT an AGN component are preferred over models WITH an AGN
component, especially when MIRI data constrain the rest-frame near-infrared; and (2) clustering
analysis reveals that LRDs reside in significantly LESS dense environments than typical
galaxies at matched redshifts and magnitudes -- they are "lonely," not found in the
overdense protoclusters where massive AGN-hosting haloes are expected. The authors interpret
LRDs as primarily compact, massive galaxies with Balmer breaks and/or strong emission lines,
rather than AGN-dominated objects. They argue that the LRD classification may encompass a
heterogeneous population, with AGN comprising only a minority subset.

---

## Historical Context

### The AGN-vs-Galaxy Debate

Since the first LRD catalogues, two camps have debated their dominant nature:

**Camp 1 (AGN)**: Broad Balmer lines (FWHM $\sim 1000$--$5000$ km/s) are the hallmark of
broad-line AGN in the local universe; the same lines in LRDs indicate black hole accretion.
The V-shape SED is naturally explained by a dust-reddened AGN at the red end plus stellar
or scattered AGN light at the blue end. This camp (Greene, Matthee, Kocevski, Pacucci, et al.)
has been dominant in the literature.

**Camp 2 (Compact galaxy)**: Broad lines in high-redshift compact galaxies could arise from
bulk gas motions (turbulence, winds, supernovae) without requiring a black hole. The Balmer
break interpretation (dense stellar atmospheres with Balmer series absorption) explains the
red continuum without dust. This camp is minority but has gained traction with the Balmer-
break models of Labbe et al. (2023) and the gas-cocoon models of Inayoshi et al. (2024).

Carranza-Escudero et al. add a third line of evidence -- clustering -- to the Camp 2 side.

### Bayesian Model Comparison in SED Fitting

Previous SED fitting studies of LRDs typically found "good fits" for AGN+galaxy models but
did not rigorously compare to galaxy-only models using Bayesian model selection. The Bayesian
Information Criterion (BIC) penalizes models with more parameters:

$${\rm BIC} = k \ln(n) - 2 \ln(\hat{L})$$

where $k$ is the number of model parameters, $n$ is the number of data points, and
$\hat{L}$ is the maximum likelihood. A model with lower BIC is preferred. Adding an AGN
component adds $\sim 4$--$6$ free parameters (AGN luminosity, power-law slope, dust
attenuation, covering factor), so the improvement in $\ln\hat{L}$ must be substantial to
justify inclusion.

---

## Key Arguments and Derivations

### 1. SED Fitting with and without AGN

The authors use the SED fitting code BAGPIPES with two model sets:

**Model A (Galaxy only)**: Composite stellar population with exponentially declining or
bursty star formation history, dust attenuation following a Calzetti law, optional nebular
emission. Free parameters: age, mass, dust, metallicity, SFR history.

**Model B (Galaxy + AGN)**: As above, plus an AGN component parameterized by AGN luminosity
$L_{\rm AGN}$, power-law slope $\Gamma$, and AGN dust attenuation $\tau_{V,AGN}$.

For 83 of 124 LRDs, the chi-squared fit improves when adding the AGN component -- as expected,
since more free parameters generally improve fits. However, when comparing BIC values:

$$\Delta {\rm BIC} = {\rm BIC}_A - {\rm BIC}_B = (k_A - k_B)\ln(n) - 2\ln(\hat{L}_A/\hat{L}_B)$$

the AGN model is only preferred ($\Delta {\rm BIC} > 10$) for 31 of 124 LRDs (25%). For the
remaining 75%, the galaxy-only model is preferred by BIC criteria, meaning there is no
statistical evidence for AGN contribution beyond what is already explained by stellar emission.

The preference for the galaxy-only model increases dramatically when MIRI photometry is
available (F770W, F1000W probing rest-frame 1--2 micron at $z \sim 5$): MIRI data breaks
the degeneracy between a red AGN continuum and a Balmer break from old/dense stellar
populations. For the 28 LRDs with MIRI detections, galaxy-only models are preferred in 22
cases (79%).

### 2. Clustering Analysis: The "Lonely" Finding

The authors measure LRD clustering relative to galaxies in the same fields using two methods:

**Method 1: Nearest-neighbor statistics**. For each LRD, the projected distance to the
nearest non-LRD galaxy (matched in photometric redshift within $\Delta z = 0.3$) is measured.
LRDs have nearest-neighbor distances $\sim 1.5$--$2 \times$ larger than expected for randomly
placed objects in the same fields. This implies LRDs avoid dense environments.

**Method 2: Kolmogorov-Smirnov test on environment density**. The local galaxy surface density
$\Sigma_5$ (density within the 5th nearest neighbor projected at matching photometric redshift)
is computed for LRDs and a control sample of non-LRD galaxies. The KS test gives $p < 0.01$,
rejecting the hypothesis that LRDs and normal galaxies trace the same environment -- LRDs
are systematically in lower-density environments.

This is the opposite of what is expected for AGN-dominated objects: locally, AGN prefer
group/cluster environments (where mergers and gas supply are enhanced). At high redshift,
massive AGN hosts are found in protoclusters (e.g., Chiang et al. 2017). If LRDs are truly
AGN in massive ($M_h \sim 10^{12} M_\odot$) haloes, they should cluster strongly. The
"lonely" result argues against this.

### 3. Halo Mass Inferences

From the projected angular correlation function $w(\theta)$ measured for the 124 LRDs across
the four fields:

$$w(\theta) = A_w \left(\frac{\theta}{1''}\right)^{-0.8}$$

The amplitude $A_w$ is converted to a large-scale bias $b$ via:

$$b^2 = \frac{w_{\rm LRD}(\theta)}{w_{\rm DM}(\theta)}$$

where $w_{\rm DM}$ is the expected dark matter correlation function from linear theory. The
inferred bias $b \sim 1.5$--$2.5$ corresponds to halo masses $M_h \sim 10^{10}$--$10^{11.5}
M_\odot$ -- at the LOW end of the AGN host halo mass distribution, inconsistent with the
massive haloes expected for $10^8 M_\odot$ black holes (which should have $b > 5$ and
$M_h > 10^{13} M_\odot$).

### 4. Physical Interpretation

The authors argue that the low halo masses and isolated environments are most consistent with
LRDs being compact massive galaxies (proto-ellipticals or compact star-forming galaxies) at
intermediate redshifts, not the hosts of massive black holes. The "broad" lines in
spectroscopic LRDs may arise from:

- Stellar velocity dispersions in dense, compact stellar systems ($\sigma_* \sim 200$--$400$
  km/s is not unusual for $M_* \sim 10^{10} M_\odot$ compact galaxies)
- Galactic winds and supernovae-driven outflows in high-sSFR systems
- Dense warm gas producing absorption features that mimic broad emission line wings

---

## Key Results

1. BIC model comparison: AGN component statistically preferred in only 25% of LRDs; galaxy-
   only model preferred for 75%, rising to 79% when MIRI photometry is available.
2. LRDs reside in significantly LESS dense environments than normal galaxies at matched $z$
   and magnitude -- they are "lonely."
3. KS test rejects common environment for LRDs and control galaxies ($p < 0.01$).
4. Large-scale bias $b \sim 1.5$--$2.5$ implies halo masses $M_h \sim 10^{10}$--$10^{11.5}
   M_\odot$ -- too low for massive AGN hosts.
5. Published in ApJL 989, L50 -- a Letters paper, indicating community recognition of the
   significance.

---

## Impact and Legacy

Carranza-Escudero et al. (2025) is one of the most significant "counter-narrative" papers in
the LRD debate. By combining rigorous Bayesian SED model comparison with an independent
clustering analysis, it provides two correlated lines of evidence against the AGN-dominated
interpretation for the majority of LRDs.

The paper immediately generated responses from the AGN camp: Inayoshi & Ho (2025,
arXiv:2512.03130) argue that the clustering analysis may be affected by photometric redshift
uncertainties and that the AGN-heated cocoon scenario naturally produces low halo mass biases
because these objects are in the rapid-growth phase before feedback operates. The debate
remains active and unresolved as of early 2026.

The ApJL publication format (Letters) and the broad authorship (35+ co-investigators from
multiple survey teams) indicate this is a high-impact, widely read result.

---

## Connection to Phonon-Exflation Framework

The Carranza-Escudero result is philosophically relevant to the phonon-exflation project's
own self-assessment. Just as the LRD SED can be fit by both an AGN model and a galaxy-only
model (with BIC preferring the simpler one), the phonon-exflation spectral features (phi ratio,
KO-dimension, CPT) can be fit by both the "non-trivial NCG compactification" model and by
null models (coincidence, mathematical artifact). The BIC-style reasoning applied to LRDs --
more parameters require proportionally stronger evidence -- mirrors the Sagan/Bayesian
framework applied to the phonon-exflation probability assessment in Sessions 23a and 24a.

The "lonely" clustering finding also resonates with the structural floor concept in phonon-
exflation: just as LRDs in under-dense environments are "lonely" in a statistical sense (below
the expected clustering signal), the phonon-exflation framework has a structural floor of 3%
probability (Sagan) -- not zero, because the mathematical coincidences are real, but far
below the naive expectation for a complete physical theory.
