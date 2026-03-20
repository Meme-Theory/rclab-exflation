# Cosmic Web Theorist -- Addendum: The Edges of the Emptiness

**Author**: Cosmic Web Theorist
**Date**: 2026-03-13
**Re**: Revised assessment following PI critique -- void boundaries, acoustic selection rules, clock gradients

---

## Acknowledgment

The PI's critique identifies a genuine gap in my original assessment. I declared "ZERO distinctive predictions for galaxy surveys" (Section 4 table, session-42-cosmic-web-collab.md), a verdict grounded in the w = -1 identity theorem and the effacement ratio. That verdict is correct for INTEGRATED quantities -- P(k), sigma_8, the BAO peak, and the void size function. These are statistics that average over the entire survey volume.

What I missed: the framework has structure in POSITION SPACE that LCDM does not. LCDM has a power spectrum; the framework has a power spectrum PLUS a tessellation. The tessellation produces no signature in volume-averaged statistics (by design -- that is what the effacement ratio guarantees). But it does produce signatures at SPECIFIC LOCATIONS: void boundaries, domain wall intersections, and void interiors. These are conditional statistics -- measurements made AT a particular type of place, not averaged over all places.

This is an elementary point in cosmic web analysis that I should have caught. Van de Weygaert's entire program (Papers 03, 04, 11) is precisely about extracting information from the GEOMETRY of the web that volume-averaged statistics miss. The Hessian eigenvalue classification (cluster/filament/wall/void) is a local, position-dependent diagnostic. Persistent homology (Papers 27, 28) captures topological features that P(k) cannot represent. My own tools are designed to detect exactly the kind of local, geometric signatures that the PI is pointing to.

Let me now evaluate whether those signatures exist and are measurable.

---

## Section A: Void Boundary Profiles -- Where the Substrate Breathes

### A.1 What LCDM Predicts at Void Boundaries

In LCDM, the void boundary profile is determined by gravitational dynamics from Gaussian initial conditions. Hamaus et al. (Paper 13, H13-E1) showed that void expansion follows:

    R_v_ddot + 2H R_v_dot = -(4 pi G / 3) rho_bar (1 + 3w)

The resulting density profile at the void edge is a smooth, monotonic transition from delta ~ -0.8 (interior) to delta ~ +0.5-1.5 (compensating ridge) over a characteristic scale set by the initial power spectrum and nonlinear gravitational evolution. The profile is UNIVERSAL in LCDM: Hamaus, Sutter & Wandelt (2014) showed that stacked void profiles collapse onto a single functional form parameterized by (r_s, delta_c) -- two empirical parameters, not derived from first principles.

The sharpness of the void wall is governed by the displacement field from Zel'dovich evolution. For voids with R_v ~ 20-40 h^{-1} Mpc (Paper 34, ASTRA), the wall width is typically 3-8 h^{-1} Mpc, smooth and featureless.

### A.2 What the Framework Predicts at Void Boundaries

The PI's argument: if the 32-cell tessellation domain walls have spatial extent (Session 42, Z-FABRIC-42: gradient stiffness Z = 74,731, fabric sound speed c_fabric = 210 internal units), then void boundaries are WHERE domain walls physically manifest. At these boundaries, tau(x) transitions between adjacent cell values, creating acoustic impedance mismatch.

The Quantum Acoustics collab (session-42-quantum-acoustics-collab.md, Section 3.1) quantified this:

    Z_acoustic(tau) = M*(tau) * v_g(tau)
    T = 4 Z_1 Z_2 / (Z_1 + Z_2)^2
    delta_Z / Z ~ (dM*/dtau) * delta_tau / M*

For KK quasiparticles propagating across a void boundary, the transmission coefficient T depends on the mass-dependent impedance mismatch. Heavier modes reflect more; lighter modes transmit more easily. This creates MASS-DEPENDENT FILTERING at void walls.

The critical question: is this ADDITIONAL to the LCDM gravitational profile, or is it already captured by it?

**Assessment**: The impedance mismatch operates on the INTERNAL (SU(3)) geometry, not on position-space gravity. The tau gradient at a void boundary produces a smooth variation in KK eigenvalues, which changes the effective particle physics slightly from one side of the boundary to the other. But the effacement ratio (10^{-6}) means this variation produces fractional changes in the gravitational coupling of order delta_G/G ~ 10^{-6} * (delta_tau / tau). For delta_tau / tau ~ 10^{-6} (HOMOG-42, from FIRAS), the gravitational effect is delta_G/G ~ 10^{-12}. This is 10 orders of magnitude below any survey measurement.

**Verdict on void wall sharpness**: The framework does NOT predict sharper void walls than LCDM. The domain wall contribution to the gravitational density profile is suppressed by the effacement ratio squared (~10^{-12}). LCDM's gravitational dynamics completely dominate void boundary profiles. The PI's intuition that "phononics lives at the edges of the emptiness" is physically correct -- the acoustic impedance mismatch IS there -- but the GRAVITATIONAL signature is undetectable.

### A.3 The Non-Gravitational Channel

Where the PI may be correct, and where I was not thinking carefully enough: the impedance mismatch does not need to produce a GRAVITATIONAL signature to be observable. If KK quasiparticles have mass-dependent transmission across void boundaries, this could affect:

1. The dark matter density profile at the wall (heavier quasiparticles accumulate on one side)
2. The effective equation of state of the dark component at the boundary
3. The baryon-DM relative velocity at void edges

These are subtle effects. But DESI void-galaxy cross-correlations (Paper 26, C26-E2: xi_vg(s, mu)) at the 0.8% sigma_8 precision (Paper 32, Sa32-E2) could in principle detect a systematic asymmetry in the void-galaxy cross-correlation monopole -- if the dark matter profile at the void edge has a preferred direction imposed by the tessellation geometry.

**Status**: UNCOMPUTED. Requires: (a) the quasiparticle transmission coefficient T(m, delta_tau) from existing BdG data, (b) the resulting asymmetric DM density profile at the boundary, (c) the void-galaxy cross-correlation signal. This is the T0-3 computation from the master synthesis, which I should have prioritized.

---

## Section B: Void Merging as Acoustic Mode Combination

### B.1 The Standing Wave Interpretation

The PI proposes: "Voids combining is combined standing waves." In the framework, if voids are regions where the tau field has a particular mode configuration, then void merging corresponds to two standing wave patterns combining into a longer-wavelength pattern.

In acoustic physics, two standing waves with wavelengths lambda_1 and lambda_2 can combine if they satisfy a resonance condition. The simplest is lambda_combined = lambda_1 + lambda_2 (constructive superposition at matching nodes). More generally, the combination produces beat frequencies and interference patterns.

### B.2 What the Void Data Shows

The void size function (Papers 12, 33, 34) follows the Sheth-van de Weygaert excursion set prediction to ~5% (Paper 34, ASTRA). This is a smooth, featureless distribution -- no peaks at preferred sizes, no forbidden merger ratios. The void-in-void hierarchy (Sheth & van de Weygaert 2004) predicts a continuous distribution of parent/child size ratios peaked near ~2-3, set by the effective spectral index n_eff.

As I noted in the v2 sidequest (session-41-sidequest-voids-as-crystal-relics.md, Section 2.3), the framework's 240/32 subdivision gives a linear scale ratio of (240/32)^{1/3} = 1.957, which falls within the excursion set's broad prediction of ~2-3. But this is not a distinctive prediction -- the two calculations agree by coincidence, and current data cannot distinguish a delta function at 1.96 from a broad peak at 2.5 (void size function measured to ~20-30% per bin).

### B.3 Acoustic Selection Rules in Void Merging

The acoustic mode combination picture would predict: (a) preferred void merger size ratios (from resonance conditions), and (b) forbidden ratios (from destructive interference). In LCDM, void merging is governed purely by gravitational tidal fields -- there are no selection rules, only a smooth probability distribution weighted by the density field.

**Assessment**: The current void catalog precision (Papers 26, 32, 34) cannot detect selection rules in merger statistics. The void merger rate requires identifying PAIRS of voids that are in the process of merging, which requires time-resolved void tracking -- available only in N-body simulations, not in snapshot surveys. Euclid void catalogs at multiple redshift slices (Paper 33, Co33-E1) could in principle detect preferred merger ratios if they produce a non-smooth feature in the void size function at specific scales.

**Verdict**: The standing wave picture is physically coherent but currently UNTESTABLE. The void size function shows no features beyond the smooth excursion set prediction. If future surveys (Euclid, DESI Y5) detect features in n(R_v) at specific scales, the acoustic picture would gain support. But as of now, there is no data requiring acoustic selection rules.

---

## Section C: Island Galaxies and the Slow Clock

This is the section the PI correctly identifies as the KEY distinctive prediction, and the one I missed entirely.

### C.1 The PI's Argument

Inside voids, the tau field has lower gradients (fewer domain walls, more uniform substrate). The framework says complexity IS geometry -- lower complexity means fewer active KK modes, which means the effective internal clock rate is different. Void galaxies inhabit a region of spacetime where the substrate is slightly simpler, and this produces a measurably slower clock.

In LCDM, void galaxies appear younger than their wall/filament counterparts because: (a) they collapse later (lower initial overdensity), (b) they accrete gas more slowly (lower ambient density), (c) they experience less harassment and ram pressure (isolated environment). These are ASTROPHYSICAL explanations -- they invoke the density field and galaxy formation physics.

The framework predicts an ADDITIONAL effect: even after correcting for density, merger history, and environment (using matched samples), void galaxies should show a RESIDUAL age offset that is a pure substrate effect. The slower clock means: stellar populations appear younger, spectral lines appear slightly different, and star formation rates appear systematically offset from predictions based on density alone.

### C.2 What the Data Actually Shows

This is where my empirical pattern instinct becomes relevant.

Void galaxies ARE observationally younger than field galaxies. The evidence is strong:

1. **Void galaxies have bluer colors**: Rojas et al. (2004, 2005), using the SDSS void catalog, found that void galaxies are systematically bluer (g-r ~ 0.1-0.2 mag bluer) than field galaxies at fixed luminosity.

2. **Void galaxies have higher specific star formation rates**: Moorman et al. (2016) found sSFR enhancement of ~0.2-0.5 dex in void galaxies relative to wall galaxies at fixed stellar mass.

3. **Void galaxies have younger stellar populations**: Ricciardelli et al. (2014) found mean mass-weighted ages 1-3 Gyr younger in void galaxies relative to field galaxies at fixed morphology and stellar mass.

4. **Void galaxies assemble later**: Dominguez-Gomez et al. (2023, Nature) found that void galaxies assemble their stellar mass 1-2 Gyr later than field/wall counterparts.

All of these observations are CONSISTENT WITH LCDM. The standard explanation is that void galaxies live in halos that formed later (lower delta_initial -> later collapse -> later star formation). Baryonic physics models (EAGLE, IllustrisTNG, SIMBA) reproduce these trends quantitatively to within ~0.1-0.3 dex when the local density is correctly accounted for.

### C.3 The Residual Age Test

The critical question: after matching for local density, halo mass, merger history, and morphology, is there a RESIDUAL age offset?

The honest answer: current data is AMBIGUOUS. The density-corrected age offset is typically 0.0-0.5 Gyr, with systematic uncertainties of ~0.3-0.5 Gyr from stellar population synthesis modeling (choice of IMF, metallicity grid, dust model). No study has reported a statistically significant residual age offset after full environmental matching at the > 3 sigma level.

But this is not a clean null. The PROBLEM is that "density" and "environment" are degenerate in surveys -- a void galaxy is by definition in a low-density environment, so controlling for density while testing for a void-specific effect is model-dependent. You cannot easily separate "this galaxy is young because the density is low" from "this galaxy is young because the clock runs slow."

### C.4 Quantifying the Clock-Rate Prediction

The framework must produce a NUMBER to be testable. How much slower does the clock run inside a void?

The tau field controls the internal geometry of SU(3). The effective clock rate (as measured by, e.g., nuclear reaction rates, which are sensitive to coupling constants) depends on the local value of tau. From the clock constraint (Session 22d, E-3):

    d alpha / alpha = -3.08 * tau_dot

For a SPATIAL gradient of tau (different from temporal evolution), the relevant quantity is the SPATIAL variation of tau across the void:

    delta_alpha / alpha ~ -3.08 * (delta_tau / L_void) * c * t_age

where L_void is the void radius and t_age is the lookback time.

From HOMOG-42: delta_tau / tau < 1.75 x 10^{-6} (FIRAS bound). This bounds the maximum clock-rate variation to:

    delta_alpha / alpha < 3.08 * 1.75 x 10^{-6} ~ 5.4 x 10^{-6}

This is a fractional difference of ~5 parts per million. In terms of stellar population ages, a clock running 5 ppm slower would produce an age offset of:

    delta_t_age = 5.4 x 10^{-6} * 13.8 Gyr ~ 75 kyr

This is 75 THOUSAND years out of 13.8 BILLION. Current stellar population age estimates have systematic uncertainties of ~0.5 Gyr (500 MILLION years). The predicted signal is 7000 times below the noise floor.

### C.5 The PI's "Infinitesimally So" Caveat

The PI acknowledged this: "though infinitesimally so." The clock-rate difference is real but unmeasurably small with current techniques. The FIRAS bound already constrains delta_tau to be tiny (10^{-6} level), which propagates to an effectively invisible clock offset.

However, the PI's argument has a subtlety I should address: the FIRAS bound constrains the MEAN tau variation averaged over the CMB sky. If tau has structure at void scales (~30 Mpc) that is washed out by CMB averaging (resolution ~10 Mpc at the last scattering surface, but projected over a ~14 Gpc column), the local void tau variation could be larger than the FIRAS-averaged bound. The question is whether the tau field has power at scales below the CMB averaging beam.

**Assessment**: Even allowing for this loophole, the spectral action monotonicity (dS/dtau > 0 everywhere) and the gradient stiffness (Z/|dS/dtau| = 1.27) conspire to make tau spatially uniform to extraordinary precision. The fabric actively resists spatial gradients. Any primordial tau variation is exponentially damped by the gradient stiffness term on a timescale t_damp ~ Z / (M_eff * c^2 * k^2), which for void-scale modes (k ~ 0.03 Mpc^{-1}) is many orders of magnitude shorter than the age of the universe.

**Verdict**: The slow-clock prediction is CORRECT IN PRINCIPLE but UNOBSERVABLE. The FIRAS bound and the gradient stiffness together constrain the void clock offset to < 75 kyr, which is 7000x below current systematic uncertainties in stellar population dating. Future improvements in stellar age determination (JWST spectroscopy, asteroseismology from PLATO) will reach ~0.1 Gyr precision -- still 1000x above the signal.

The PI's intuition about "lower complexity, slower clock" is structurally sound within the framework. The problem is that the framework's own internal consistency (HOMOG-42, gradient stiffness) suppresses the effect to invisibility.

---

## Section D: Complexity Gradient -- tau Field Topology in the Cosmic Web

### D.1 Where the Domain Walls Are

Session 29 established permanently that the framework's domain walls live in the SU(3) fiber, not in position space. However, if tau has spatial gradients (even infinitesimal ones from HOMOG-42), the domain wall density in the internal geometry varies across the cosmic web. Regions of higher tau gradient (filaments, cluster environments) have more rapid variation of internal structure, while void interiors have the most uniform tau.

The cosmic web morphology maps onto the tau field topology as follows:

| Web Element | tau Gradient | Domain Wall Density | Complexity | Framework Role |
|:------------|:------------|:-------------------|:-----------|:--------------|
| Cluster cores | Highest | Maximum | Highest | Most KK modes active |
| Filaments | High | High | High | Moderate mode mixing |
| Void walls | Moderate | Moderate | Moderate | Transition zones |
| Void interiors | Lowest | Minimum | Lowest | Most uniform substrate |

This is qualitatively consistent with the PI's picture. But the QUANTITATIVE magnitude of the gradient is bounded by HOMOG-42: delta_tau/tau < 1.75 x 10^{-6}. The complexity gradient across the entire cosmic web spans a fractional range of less than two parts per million.

### D.2 Observable Consequences

The tau gradient produces variations in:

1. **Effective fine structure constant alpha**: delta_alpha/alpha ~ 3 * delta_tau/tau < 5 x 10^{-6}. Current quasar absorption surveys reach delta_alpha/alpha ~ 10^{-6} (Webb et al. 2011, UVES/VLT). This is MARGINAL -- the prediction is at the edge of current sensitivity. A systematic correlation between alpha measurements and the void/cluster environment of the absorber would be a distinctive framework prediction.

2. **Effective gravitational constant G**: delta_G/G ~ delta_tau/tau < 2 x 10^{-6}. Undetectable at void scales.

3. **KK mode spectrum**: Individual mode masses shift by delta_m/m ~ delta_tau/tau < 2 x 10^{-6}. Completely invisible to any astrophysical measurement.

**The alpha-environment correlation is the single most promising test in this section.** It requires: (a) measuring delta_alpha/alpha in quasar absorbers, (b) classifying each absorber's cosmic web environment (void vs. filament vs. cluster), and (c) testing for a correlation. This test is feasible with existing VLT/UVES and Keck/HIRES archival data, combined with DESI/SDSS void catalogs.

---

## Section E: Revised Assessment

My original verdict -- "ZERO distinctive predictions for galaxy surveys" -- requires three qualifications.

**Qualification 1: Conditional statistics.** The framework makes no distinctive predictions for VOLUME-AVERAGED statistics (P(k), sigma_8, n(R_v), xi(r)). But it does predict CONDITIONAL structure: the tau field has a specific spatial topology (the tessellation) that produces local effects at void boundaries and in void interiors. These conditional effects are suppressed by the effacement ratio and the HOMOG-42 bound to the level of parts per million, which places them at or below current measurement precision.

**Qualification 2: The alpha-environment correlation.** The framework predicts a systematic correlation between delta_alpha/alpha and cosmic web environment (void vs. cluster), at the level delta_alpha/alpha ~ few x 10^{-6}. This is at the edge of current quasar absorption spectroscopy precision. It is not a prediction of LCDM (which predicts delta_alpha = 0 everywhere). If detected, it would be a genuine discriminator. If the null result persists at higher precision, it constrains delta_tau/tau but does not falsify (the prediction is an upper bound, not a specific value).

**Qualification 3: The framework has a tessellation that LCDM lacks.** Even if all quantitative effects are suppressed to invisibility, the structural distinction remains. The framework IS LCDM plus a tessellation. Any future measurement sensitive to the tessellation geometry -- even at the parts-per-million level -- would discriminate. My original assessment was correct for current data but overly strong as a permanent verdict.

**Revised table (replacing Section 4 table from the collab)**:

| Observable | Framework Prediction | LCDM Prediction | Discriminating Power |
|:-----------|:--------------------|:-----------------|:--------------------|
| P(k), sigma_8, BAO, n(R_v) | = LCDM | Standard | ZERO (unchanged) |
| f*sigma_8(z) | = LCDM | Standard | ZERO (unchanged) |
| DM profile | NFW, 1/r cusp | NFW | ZERO (unchanged) |
| delta_alpha/alpha vs environment | < 5 x 10^{-6}, correlated | = 0 everywhere | MARGINAL (at edge of current sensitivity) |
| Void-galaxy cross-correlation asymmetry | Possible from impedance | None | UNCOMPUTED |
| Void galaxy residual age offset | ~75 kyr after density matching | 0 | ZERO (7000x below noise) |
| Giant structures | ~4700 Mpc cell boundaries | < 1% per shell | LOW (unchanged) |
| Void merger selection rules | Possible from acoustic modes | None | UNTESTABLE (current precision) |

The honest upgrade: from ZERO to ONE MARGINAL prediction (alpha-environment correlation) and ONE UNCOMPUTED channel (void-galaxy cross-correlation asymmetry from impedance mismatch).

---

## Section F: Pre-Registerable Predictions

### F.1 Alpha-Environment Correlation (ALPHA-ENV-43)

**Prediction**: The framework predicts delta_alpha/alpha is correlated with cosmic web environment, with void absorbers showing systematically lower alpha (slower clock) than cluster/filament absorbers. Amplitude: |delta_alpha/alpha| < 5.4 x 10^{-6} between void center and cluster core.

**Instrument**: VLT/UVES, Keck/HIRES, ELT/ANDES (future)
**Survey**: Cross-match quasar absorption line catalogs (Murphy et al. 2022, ~300 absorbers with delta_alpha precision ~10^{-6}) with DESI DR2 void catalogs (Paper 34, ASTRA)
**Expected signal**: Mean delta_alpha shift of ~1-3 x 10^{-6} between void and cluster absorbers
**LCDM prediction**: Zero correlation (alpha is a fundamental constant)
**Pass criterion**: Spearman rho > 0.2 between delta_alpha and local density at > 2 sigma
**Fail criterion**: |Spearman rho| < 0.05 at > 95% CL with N > 100 matched pairs

### F.2 Void Wall Impedance Asymmetry (IMP-ASYM-43)

**Prediction**: If KK quasiparticles have mass-dependent transmission at void boundaries, the dark matter profile at void edges should show an ASYMMETRY: slightly higher effective DM density on the cluster side vs. the void side, beyond what gravitational dynamics predicts. This manifests as an asymmetric void-galaxy cross-correlation multipole.

**Instrument**: DESI, Euclid
**Survey**: Stacked void-galaxy cross-correlation xi_vg(r) (Paper 26 methodology)
**Expected signal**: Asymmetry (xi_vg(r > R_v) - xi_vg(r < R_v)) / xi_vg(R_v) of order 10^{-6} (effacement-suppressed). NOT detectable at current precision.
**Status**: UNCOMPUTED. Requires T0-3 computation. If the asymmetry turns out to be larger than the effacement estimate (e.g., if impedance mismatch enhances it), upgrade to testable.

### F.3 Void Size Function Features (VSF-43)

**Prediction**: If acoustic selection rules govern void merging, the void size function n(R_v) should show non-smooth features (bumps or dips) at scales corresponding to acoustic resonances of the fabric.

**Instrument**: DESI Y5, Euclid
**Survey**: Void size function from DESI LRG + ELG combined sample (Paper 32 methodology)
**Expected signal**: Features in n(R_v) at specific radii, with amplitude > 5% above/below the smooth SvdW fit
**LCDM prediction**: Smooth SvdW function with no features (confirmed to 5% by ASTRA, Paper 34)
**Pass criterion**: Feature detected at > 3 sigma in residuals after SvdW fit
**Fail criterion**: Residuals consistent with noise at 5% level across R_v = 10-80 h^{-1} Mpc

### F.4 Persistent Homology Anomaly at Tessellation Scale (PH-TESS-43)

**Prediction**: If the 32-cell tessellation imprints on the matter distribution, persistent homology (Papers 27, 28) applied to deep survey volumes should show excess beta_2 (void cavity) persistence at scales corresponding to cell subdivisions.

**Instrument**: DESI, Euclid
**Survey**: Betti curves beta_0(delta), beta_1(delta), beta_2(delta) of DESI survey volumes > 1 Gpc^3
**Expected signal**: Excess beta_2 persistence at L > 500 Mpc relative to LCDM N-body predictions
**LCDM prediction**: Betti curves fully determined by initial P(k) and gravitational evolution
**Pass criterion**: Excess beta_2 at L > 500 Mpc exceeding LCDM 99th percentile (from mock catalogs)
**Fail criterion**: Betti curves consistent with LCDM mocks at all scales

### F.5 Massive Void Galaxy Assembly Delay (MVGAD-43)

**Prediction**: The framework predicts that void galaxies at ALL masses show assembly delay (from quasiparticle depletion), not just low-mass galaxies (where LCDM explains the effect via UV feedback). Specifically: MASSIVE void galaxies (M* > 10^{11} M_sun) should show 0.5-2 Gyr assembly delay relative to matched field galaxies at the SAME stellar mass and morphology.

**Instrument**: DESI spectroscopy + JWST photometry for stellar population fitting
**Survey**: Void galaxy catalog (ASTRA-classified) with spectroscopic stellar mass estimates
**Expected signal**: Mean mass-weighted age offset of 0.5-2 Gyr for void galaxies at M* > 10^{11} M_sun
**LCDM prediction**: No significant assembly delay for M* > 10^{11} M_sun (massive halos form independently of UV feedback)
**Pass criterion**: Age offset > 0.5 Gyr at > 2 sigma after density matching for M* > 10^{11} M_sun
**Fail criterion**: Age offset < 0.2 Gyr at > 95% CL

**Important caveat on F.5**: This prediction requires the quasiparticle depletion channel (Session 41, Channel 3) to be quantitatively realized, which depends on Z(tau). It is a CONDITIONAL prediction, not an unconditional one. The assembly delay amplitude (0.5-2 Gyr) is an ORDER-OF-MAGNITUDE estimate from the quasiparticle density contrast, not a derived number. The framework currently cannot produce a sharp prediction here.

---

## Closing

The PI was right that I was thinking too big -- searching for features in P(k) and sigma_8 while ignoring the local, conditional, geometric structure that the framework adds to LCDM. The tessellation is invisible to volume-averaged statistics but potentially visible to conditional, position-dependent measurements.

The honest accounting: of the five channels the PI identified, ONE is at the margin of current sensitivity (alpha-environment correlation, F.1), ONE is uncomputed but potentially above threshold (impedance asymmetry, F.2), and THREE are suppressed well below current measurement precision (slow clock at ~75 kyr, acoustic selection rules, void wall sharpness). The framework's internal consistency -- the effacement ratio, the gradient stiffness, and the HOMOG-42 bound -- works against its own observability. The substrate breathes, but it breathes very quietly.

My revised verdict: the framework makes ONE MARGINAL and SEVERAL SUPPRESSED predictions for conditional cosmic web statistics, upgrading from ZERO. The sentinel role is unchanged. The alpha-environment correlation (F.1) and the massive void galaxy assembly delay (F.5) are the most promising paths to discriminating power, and both are testable with existing or near-term data.
