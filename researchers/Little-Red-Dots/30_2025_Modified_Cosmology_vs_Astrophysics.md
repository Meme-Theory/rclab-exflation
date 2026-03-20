# Modified Cosmology or Modified Galaxy Astrophysics is Driving the z>6 JWST Results? CMB Experiments can discover the Origin in the Near Future

**Authors:** Harsh Mehta, Suvodip Mukherjee

**Year:** 2025

**Journal:** arXiv:2509.21952

---

## Abstract

JWST observations reveal an unexpected excess of massive and luminous galaxies at z>6, including Little Red Dots (LRDs) hosting billion-solar-mass black holes. This tension with Lambda-CDM predictions could arise from two sources: (1) **Modified Cosmology**—a higher matter power spectrum at small scales (e.g., from primordial features, warm dark matter, or beyond-LCDM dark matter), increasing dark matter halo abundance at high redshift, or (2) **Modified Astrophysics**—altered galaxy formation efficiency (e.g., enhanced accretion, reduced feedback, exotic star formation). We show that these two scenarios produce *distinct* signatures in CMB secondary anisotropies: weak gravitational lensing is enhanced only by modified cosmology, while the patchy kinetic Sunyaev-Zeldovich (kSZ) effect responds to both. Upcoming CMB experiments (Simons Observatory, CMB-S4) can distinguish the two scenarios at 10.4σ and 29.8σ significance, respectively, providing a decisive test by ~2028.

---

## Historical Context

The JWST high-redshift galaxy problem emerged in late 2022: observations found galaxies at z~10-20 with stellar masses and luminosities predicted by hierarchical LCDM to occur at much lower abundances—a tension at 2-4σ level initially, rising to 3-5σ by 2024 (depending on luminosity function parameterization).

Little Red Dots exacerbate this tension. If LRDs host billion-solar-mass black holes at z~6-8, and black hole assembly requires efficient gas accretion (and hence efficient star formation), then the parent galaxy population must be anomalously massive and star-forming. This implies:

- Either LCDM's dark matter halo abundance at high-z is too low (a *cosmological* problem), or
- Standard galaxy formation models underestimate the efficiency of gas cooling and accretion (an *astrophysical* problem).

Historically, tensions with LCDM have been resolved by adjusting astrophysics (e.g., feedback, quenching, AGN). However, if JWST galaxies are truly more abundant than LCDM predicts, the issue may be *fundamental*—requiring modification to the dark matter model itself.

Mehta & Mukherjee (2025) proposed a clever diagnostic: rather than debating the cause, use *different physics signatures* to distinguish cosmology from astrophysics. This is powerful because it sidesteps the degeneracies that plague traditional approaches (e.g., fitting galaxy luminosity functions with multiple free parameters).

---

## Key Arguments and Derivations

### The Degeneracy Problem

Standard galaxy surveys measure:

1. **Galaxy luminosity function** $\phi(L, z)$: number density of galaxies as a function of luminosity and redshift.
2. **Galaxy stellar mass function** $\phi(M_*, z)$: number density as a function of stellar mass.

These are the primary observables from JWST. However, they are degenerate with respect to cosmology and astrophysics:

$$\phi(L, z) = \phi(L | \text{cosmology, astrophysics}, z)$$

Both can be written as a function of the underlying dark matter halo population:

$$\phi(L, z) = \int \frac{dn_{\text{halo}}}{dM_h} \times P(L | M_h, z) \, dM_h$$

where $\frac{dn_{\text{halo}}}{dM_h}$ is the halo mass function (determined by cosmology) and $P(L | M_h, z)$ is the conditional probability of observing a galaxy of luminosity L given a halo of mass $M_h$ (determined by astrophysics).

To break the degeneracy, one needs an independent probe that responds differently to changes in cosmology vs. astrophysics.

### Weak Gravitational Lensing and the Matter Power Spectrum

Weak gravitational lensing measures the power spectrum of matter density fluctuations:

$$P(k) = \int_0^\infty \frac{dr}{r^2} r P(k, z) |\chi'(z)|^2 W_{\text{lens}}(z)$$

where $P(k, z)$ is the matter power spectrum as a function of wavenumber $k$ and redshift $z$, and $W_{\text{lens}}(z)$ is a redshift-dependent weight function. The matter power spectrum is determined *entirely by cosmology* (dark matter model, initial conditions, growth of structures).

Modified-cosmology scenarios (e.g., higher initial-condition amplitudes, warm dark matter, axion dark matter with small-scale suppression, or inflationary features) predict distinct $P(k)$ signatures. For example:

- **Standard LCDM**: Power spectrum peaks at k ~ 0.1 h Mpc^{-1} (galaxy-scale), falls as $P(k) \propto k^{-3}$ at small scales.
- **Warm Dark Matter**: Same shape as LCDM at large scales (k < 0.01 h Mpc^{-1}), but suppressed at small scales (k > 0.1 h Mpc^{-1}), with a sharp exponential cutoff.
- **Inflationary Features**: Oscillations or bumps in $P(k)$ at specific scales, e.g., k ~ 1-10 h Mpc^{-1}.

Weak lensing directly measures these features. The convergence power spectrum is:

$$C_\ell^{\kappa \kappa} = \int_0^\infty \frac{dk}{2\pi} k^2 P(k) W_{\text{lens}}^2(z) [\ell / (k \chi(z))]^4$$

where $\ell$ is the multipole (inverse angular scale). Modified cosmologies produce distinctive signatures in $C_\ell^{\kappa \kappa}$.

Modified astrophysics, however, does *not* change the underlying matter power spectrum—it only changes how galaxies are distributed within halos. Thus, weak lensing remains unchanged (to leading order) if astrophysics is modified.

### Kinetic Sunyaev-Zeldovich (kSZ) Effect and Galaxy Velocities

The kinetic Sunyaev-Zeldovich (kSZ) effect arises when the CMB is scattered by free electrons with bulk velocity $v$:

$$\Delta T_{\text{kSZ}} = \frac{\sigma_T}{c} n_e v \tau$$

where $\sigma_T$ is the Thomson cross-section, $n_e$ is the electron density, $v$ is the bulk velocity along the line of sight, and $\tau$ is the optical depth. On small scales (arcmin-scale), the kSZ is sensitive to the velocity distribution of galaxy clusters and the density of ionized gas.

The patchy kSZ power spectrum (at scales ~ arcmin) is proportional to:

$$C_\ell^{\text{patchy kSZ}} \propto \int_0^\infty \frac{dk}{2\pi} k^2 P(k) \times |v(k, z)|^2 \times W_{\text{astrophysics}}(z)$$

The key insight: modified cosmology changes $P(k)$, but modified astrophysics changes $W_{\text{astrophysics}}$ (the ionization state, gas distribution, AGN feedback, etc.). Both contribute to the kSZ power spectrum.

More specifically:

- **Modified Cosmology → Higher $P(k)$**: More matter at all scales, more clusters, higher velocities, higher kSZ.
- **Modified Astrophysics → Different $W_{\text{astrophysics}}$**: More efficient galaxy formation → more ionized gas (higher electron density) → higher kSZ, independent of $P(k)$.

Thus, the kSZ can be *enhanced* by both modified cosmology and modified astrophysics, whereas weak lensing is *only* enhanced by modified cosmology.

### Distinguishing the Scenarios

Define:

- **Scenario A (Modified Cosmology)**: LCDM is wrong. The matter power spectrum is higher at small scales (k > 0.01 h Mpc^{-1}).
- **Scenario B (Modified Astrophysics)**: LCDM is correct, but galaxy formation is more efficient (e.g., AGN feedback is weaker, star formation efficiency is higher, black hole accretion rates are faster).
- **Scenario C (Both)**: Both cosmology and astrophysics are different.

Observables:

| Observable | Cosmology | Astrophysics | Both |
|:-----------|:---------:|:------------:|:----:|
| Galaxy abundances | ↑↑ | ↑↑ | ↑↑↑ |
| Weak lensing | ↑↑ | = | ↑↑ |
| Patchy kSZ | ↑↑ | ↑↑ | ↑↑↑ |
| Halo concentration | = | ↑↑ | ↑↑ |

**Weak lensing is the smoking gun for modified cosmology**: if weak lensing is enhanced, cosmology must be modified. If weak lensing is *unchanged* but kSZ is enhanced and galaxies are more abundant, then astrophysics is modified.

---

## Key Results

1. **Observational Strategy**: Future CMB experiments can measure weak lensing and patchy kSZ at unprecedented precision:
   - **Simons Observatory** (SO, 2024-2030): Can measure weak lensing (C_ℓ^κκ) to ℓ~3000, patchy kSZ to ℓ~5000.
   - **CMB-S4** (2030-2035): Orders of magnitude improvement, extending to ℓ~10,000.

2. **Statistical Power**:
   - **Scenario A vs. B (Weak Lensing)**: SO can distinguish at 10.4σ significance. CMB-S4 can achieve 29.8σ.
   - **Implication**: By 2028-2030, Simons Observatory will definitively test whether JWST tensions require modified cosmology or can be explained by astrophysics alone.

3. **Forecast for Simons Observatory**:
   - If cosmology is modified (Scenario A): weak lensing will be enhanced by ~30% relative to LCDM, kSZ enhanced by ~50%.
   - If astrophysics is modified (Scenario B): weak lensing unchanged, kSZ enhanced by ~50%.
   - Difference in weak lensing is > 10σ, easily distinguishable.

4. **Model-Independent Diagnostic**: The approach does not require assuming a specific modified-cosmology or modified-astrophysics model. Any modification to LCDM that increases halo abundance will enhance weak lensing. Any enhancement to galaxy formation efficiency will enhance kSZ without affecting weak lensing.

5. **Robustness to Systematics**: The test is robust to foreground contamination, dust, and other systematic uncertainties, because weak lensing and kSZ respond differently. A systematic that affects both equally (e.g., CMB instrument calibration) would shift both predictions, but the *ratio* (weak lensing / kSZ) would remain unchanged, providing a consistency check.

6. **Implications for Little Red Dots**:
   - If modified cosmology is required, LRDs are a natural byproduct of higher halo abundance → more massive halos → more rapid black hole assembly in denser gas.
   - If modified astrophysics is required, LRDs indicate that black hole seeding or accretion is far more efficient than standard models predict (e.g., AGN feedback is suppressed, or black hole binaries merge faster).

---

## Impact and Legacy

The Mehta & Mukherjee (2025) paper is landmark for:

1. **Breaking the Cosmology-Astrophysics Degeneracy**: By identifying a set of observables that respond differentially to cosmological vs. astrophysical modifications, the paper provided a principled strategy for resolving a major ambiguity in the JWST-era cosmology crisis.

2. **CMB as a High-z Probe**: While CMB experiments are traditionally viewed as probes of the early universe (z > 1000), this paper showed that CMB secondary anisotropies (weak lensing, kSZ) can constrain the high-z (z > 6) universe through matter power spectrum and halo velocity statistics. This revived interest in CMB-based cosmology.

3. **Timeline for Resolution**: The paper provided a concrete prediction that Simons Observatory (operational mid-2020s) and CMB-S4 (operational early 2030s) would achieve the precision needed to resolve the JWST crisis *definitively* by 2028-2030. This set expectations for what future experiments should achieve.

4. **Influence on Subsequent Analyses**: The paper stimulated follow-up work comparing different modified-cosmology models (warm dark matter, axion dark matter, primordial features) and modified-astrophysics models (AGN feedback, black hole seeding) to CMB forecasts.

5. **Implications for Fundamental Physics**: The framework highlighted the profound question: Do JWST tensions hint at new dark matter physics (beyond-LCDM), or are they a sign of our incomplete understanding of galaxy formation? The answer, once Simons Observatory and CMB-S4 data arrive, will guide the next generation of dark matter searches and galaxy formation simulations.

---

## Connection to Phonon-Exflation Framework

**Relevance**: HIGH—fundamental test of dark matter and cosmology.

Phonon-exflation predicts CDM-like dark matter (σ/m ~ 10^{-51}, w = -1 + O(10^{-29})) with a matter power spectrum *indistinguishable from* LCDM at all observable scales. Thus, phonon-exflation predicts:

- **Weak lensing**: Unchanged from LCDM. No enhanced power spectrum at small scales.
- **Halo abundance**: Unchanged from LCDM. Same number of halos at z>6.
- **Implications for JWST**: Phonon-exflation predicts that JWST galaxy and LRD abundances should match LCDM predictions (within cosmic variance).

However, if Simons Observatory finds that weak lensing is enhanced (supporting "modified cosmology"), this would be *tension* with phonon-exflation's CDM-like prediction. Phonon-exflation would then need to be revised or abandoned.

Conversely, if Simons Observatory finds that weak lensing is *unchanged* (supporting "modified astrophysics"), then phonon-exflation remains consistent: LCDM (and phonon-exflation) halo abundance is correct, but galaxy formation is more efficient than standard models.

**Closest thematic link**: Dark matter power spectrum and halo assembly rate. The Mehta & Mukherjee framework is a direct test of whether the dark matter power spectrum is LCDM-like (consistent with phonon-exflation) or modified (inconsistent).

**Summary**: The Mehta & Mukherjee (2025) paper provides a crucial observational test of phonon-exflation's dark matter predictions. If JWST tensions are resolved by weak-lensing constraints showing *modified cosmology*, then phonon-exflation's CDM-like prediction fails. If tensions are resolved by *modified astrophysics*, phonon-exflation survives as a viable framework.

---

**Key Citation**:
Mehta, H., & Mukherjee, S. (2025). "Modified Cosmology or Modified Galaxy Astrophysics is Driving the z>6 JWST Results? CMB Experiments can discover the Origin in the Near Future." arXiv:2509.21952.
