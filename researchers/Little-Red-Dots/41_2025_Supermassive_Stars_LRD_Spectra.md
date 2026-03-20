# Supermassive Stars Match Spectral Signatures of JWST's Little Red Dots

**Author(s):** Nandal & Loeb
**Year:** 2025
**Journal:** The Astrophysical Journal (arXiv:2507.12618, accepted)

---

## Abstract

Little Red Dots observed by JWST at z~5-7 are typically interpreted as heavily obscured, accreting supermassive black holes. However, detailed spectral modeling shows that metal-free supermassive stars with masses $M \sim 10^6 M_\odot$ and quasi-stellar envelopes can reproduce the observed spectral energy distributions, hydrogen-line widths, and infrared colors of LRDs to remarkable precision. Non-LTE (non-local thermodynamic equilibrium) effects in supermassive stellar atmospheres naturally produce the characteristic broad Balmer-line wings (FWHM > 1000 km/s) observed in LRDs without invoking black hole orbital motion. The stellar model predicts a V-shaped Balmer break (discontinuity at 3646 Å) that matches JWST spectroscopy. The quasi-stellar envelope, with effective temperatures $T_{eff} \sim 10^4-10^5$ K and photospheric density $\rho \sim 10^{-4}$ g/cm^3, naturally produces the infrared colors (F277W-F356W colors matching LRD observations) through blackbody emission. This alternative interpretation suggests that JWST may be discovering the stellar progenitors of supermassive black holes rather than the black holes themselves—systems captured in the brief phase before stellar core collapse produces an event horizon. We present synthetic spectra for models with spin parameters $a = 0-0.9$, rotation rates $\Omega = 0-0.95 \Omega_K$, and metallicities $Z = 0-0.1 Z_\odot$, demonstrating robustness of the supermassive star interpretation across a wide parameter space.

---

## Historical Context

The standard interpretation of LRDs posits that they are young supermassive black holes accreting gas in the early universe. However, an alternative interpretation has received increasing attention: what if LRDs are not black holes at all, but rather **supermassive stars**—gravitationally bound objects with masses >10^6 M_sun, supported by radiation pressure and non-relativistic gravity, that have not yet undergone core collapse to form black holes?

Supermassive stars are theoretically viable. In the early universe with metal-free (or nearly metal-free) gas, primordial compositions of hydrogen and helium allow stars to reach masses far exceeding the classical Eddington limit for metal-rich stars. The reason is that opacity scales with metallicity:

$$\kappa = \kappa_0 (1 + Z/Z_\odot)$$

In metal-free gas, opacity is dominated by electron scattering (Thomson scattering), which is relatively low, allowing dense objects to form.

A supermassive star would display unusual properties:

1. **Quasi-stellar envelope**: The outer layer is a thick, cool photosphere with $T_{eff} \sim 10^3-10^4$ K (compared to normal stars' $T_{eff} \sim 10^4$ K)
2. **Non-LTE atmosphere**: The dense, hot photosphere deviates from LTE due to high optical depth and anisotropic radiation fields
3. **Broad hydrogen lines**: Non-LTE effects in hydrogen recombination produce artificial broadening of Balmer lines, mimicking orbital velocity-broadening in black hole accretion disks
4. **Lack of X-ray emission**: No accretion disk → no strong X-ray source, matching LRD X-ray faintness
5. **Transience**: The supermassive star is dynamically unstable and will collapse to a black hole within ~10^4-10^6 years, making the observable phase brief

The question becomes: can supermassive stars quantitatively reproduce the observed LRD spectra?

---

## Key Arguments and Derivations

### Supermassive Star Structure

A self-supporting star in hydrostatic equilibrium obeys:

$$\frac{dP}{dr} = -\frac{GM(r) \rho(r)}{r^2}$$

where $P$ is the total pressure (gas + radiation), $M(r)$ is the enclosed mass, and $\rho(r)$ is the density.

For a massive star dominated by radiation pressure (which is true for $M > 10^5 M_\odot$ in metal-free gas), the pressure gradient is:

$$\frac{dP_{rad}}{dr} \sim \frac{1}{3c} \frac{dE_{rad}}{dr}$$

In a steady state, the star radiates energy at luminosity $L$. The energy balance requires:

$$L = 4\pi r^2 F_r = 4\pi r^2 c \frac{1}{3 \kappa \rho} \frac{dP_{rad}}{dr}$$

For a supermassive star with $M \sim 10^6 M_\odot$ and $R \sim 10^{13}-10^{14}$ cm (a few solar radii—very compact due to enormous gravity), the radiative luminosity is:

$$L \sim \frac{GM^2}{R \tau_{dyn}}$$

where $\tau_{dyn} \sim \sqrt{R^3 / GM}$ is the dynamical timescale. This gives:

$$L \sim \frac{GM^{3/2}}{R^{1/2}} \sim 10^{45}-10^{46} \text{ erg/s}$$

consistent with LRD bolometric luminosities.

### Non-LTE Hydrogen Line Formation

In a dense stellar atmosphere, hydrogen atoms interact via:

$$H + \gamma \leftrightarrow H^* \leftrightarrow H + \gamma'$$

where the superscript $*$ denotes excited states. In local thermodynamic equilibrium (LTE), the populations of levels follow the Saha-Boltzmann distribution. However, at high densities and with anisotropic radiation (radiation field not isotropic), LTE breaks down.

The Boltzmann factor for level $n$ to level $m$ ($n > m$) is:

$$\frac{N_n}{N_m} = \frac{g_n}{g_m} \exp\left(-\frac{E_n - E_m}{k_B T}\right)$$

where $g$ is the statistical weight. This assumes detailed balance. But in the non-LTE case, photon escape probabilities become important: a photon emitted in a transition $n \to m$ may escape the star without being reabsorbed. The escape probability $P_{esc}$ depends on optical depth:

$$P_{esc} \sim \frac{1}{\sqrt{\tau}}$$

where $\tau$ is the monochromatic optical depth at line center. In a dense atmosphere with $\tau \gg 1$:

$$\frac{N_n}{N_m} \neq \frac{g_n}{g_m} \exp\left(-\frac{E_n - E_m}{k_B T}\right)$$

Instead, the population becomes underpopulated in upper levels compared to LTE (because photons escape, removing excitation). This suppresses line emission in the optically thick region but enhances it in the optically thin photosphere.

For hydrogen, the Balmer lines (transitions from $n > 3$ to $n = 2$) have high optical depth in the supermassive star's photosphere. Non-LTE effects produce:

1. **Wings**: The line wings (far from line center) form in optically thin regions where scattering and Doppler shifts dominate, producing broad features
2. **Artificial velocity broadening**: The wings mimic velocity broadening from orbital motion (Doppler shifts in infalling/outflowing gas)
3. **FWHM enhancement**: The effective line width increases from intrinsic stellar rotation (typically $v_{rot} \sim 10-100$ km/s for massive stars) to $\sim 1000-5000$ km/s due to non-LTE scattering

The paper quantifies this using the Sobolev approximation and non-LTE line-formation codes (TLUSTY, code ATLAS12). The computed line profile for Hα (6563 Å) in a supermassive star with:
- $M = 10^6 M_\odot$
- $T_{eff} = 10^4.5$ K
- $\log g = 3.5$ (where $g = GM/R^2$ is surface gravity)
- $v_{rot} = 200$ km/s

produces:

$$\text{FWHM}_{Halpha} \sim 2000-4000 \text{ km/s}$$

matching LRD observations.

### Quasi-Stellar Envelope Spectral Properties

The outer layer of a supermassive star is a "quasi-stellar envelope"—a tenuous envelope that is extended relative to the stellar core but still bound. This envelope has:

- **Effective temperature**: $T_{eff} \sim 10^4-3 \times 10^4$ K (depending on mass and luminosity)
- **Photospheric density**: $\rho \sim 10^{-4}-10^{-3}$ g/cm^3
- **Optical properties**: Neutral hydrogen (not ionized) dominates opacity; heavy elements are absent (metal-free composition)

The envelope emits as an approximate blackbody (or modified blackbody) with temperature $T_{eff}$. For a supermassive star with $L \sim 10^{45}$ erg/s and $R \sim 10^{13}$ cm:

$$T_{eff} = \left(\frac{L}{4\pi \sigma R^2}\right)^{1/4} = \left(\frac{10^{45}}{4\pi \times 5.67 \times 10^{-5} \times (10^{13})^2}\right)^{1/4} \sim 10^{4.3} \text{ K}$$

The spectral energy distribution (SED) is:

$$F_\nu = \frac{R^2}{d_L^2} (1 + z) B_\nu(T_{eff})$$

where $B_\nu$ is the Planck function and $d_L$ is luminosity distance. At infrared wavelengths (JWST F277W ~2.77 μm, F356W ~3.56 μm), this produces:

$$F_\nu \propto \nu^\beta$$

with $\beta \sim 2$ (Rayleigh-Jeans tail), giving a rising infrared continuum consistent with LRD colors.

### Balmer Break and V-Shape Feature

One of the most distinctive features of supermassive stars is the **Balmer break**—a discontinuity in the continuum at the Balmer-series limit (3646 Å). In a normal (LTE) stellar atmosphere, the Balmer continuum (bound-free absorption from $n=2$ state to continuum) produces a break. In non-LTE, the break is modified and can show a characteristic V-shape profile:

The non-LTE Balmer break arises because:

1. **Below 3646 Å**: Balmer continuum dominates the opacity. The optical depth is high, and photons are absorbed. The spectrum appears dark (low flux relative to continuum)
2. **Above 3646 Å**: Balmer continuum is absent. Other opacity sources (bound-free from higher levels, Thomson scattering) dominate. Flux is higher
3. **At 3646 Å**: Sharp transition, appearing as a V-shaped dip in the log-linear SED plot

The paper's synthetic spectra reproduce this V-shaped break in LRD spectral data, matching JWST observations remarkably well.

### Observability Timescale

A supermassive star is not a permanent object. It is dynamically unstable and will eventually undergo core collapse to form a black hole. The timescale is:

$$\tau_{collapse} \sim \frac{M}{dM/dt}$$

where $dM/dt$ is the mass-loss rate due to winds or other processes. For a supermassive star in the early universe with minimal mass loss:

$$\tau_{collapse} \sim 10^4-10^6 \text{ years}$$

(shorter timescales for higher luminosity). This means:

- The supermassive star phase is brief (~10^4-10^6 yr) compared to the age of the universe at z~5-7 (~1 Gyr)
- Observation of a supermassive star is rare—only ~1 in 10^5 systems would be caught in this phase
- Yet if supermassive stars are the precursors of ALL supermassive black holes, the expected number of observable supermassive stars at any given redshift is non-negligible given the abundance of early quasars

---

## Key Results

1. **Synthetic supermassive star spectra match LRD observations**: Models with M ~ 10^6 M_sun, T_eff ~ 10^4-10^5 K, and non-LTE hydrogen line formation reproduce LRD spectral features including H-beta widths, infrared colors, and the V-shaped Balmer break.

2. **Non-LTE effects produce artificial velocity broadening**: Broad hydrogen lines (FWHM > 1000 km/s) arise from non-LTE scattering in dense atmospheres, not from orbital motion around black holes.

3. **Infrared colors naturally explained**: The quasi-stellar envelope with T_eff ~ 10^4 K produces a rising infrared continuum matching JWST F277W and F356W colors of LRDs.

4. **X-ray faintness explained**: Supermassive stars lack accretion disks and jets, producing minimal X-ray emission—consistent with observed LRD X-ray non-detections.

5. **Metal-free composition viable**: The models assume Z = 0 (primordial composition), consistent with early-universe star formation before metal enrichment.

6. **Observability window ~10^4-10^6 years**: Supermassive stars are transient objects. The observable phase is brief, making individual detections rare but not implausible if the precursor population is abundant.

7. **Alternative to black hole interpretation**: The supermassive star model offers a self-consistent, single-component explanation for LRDs, without requiring multi-component models (dusty torus + AGN continuum + scattering).

---

## Impact and Legacy

This paper elevated supermassive stars from a theoretical curiosity to a viable interpretation of real astrophysical observations. It has stimulated:

- Detailed follow-up spectroscopy to search for supermassive star signatures (V-shaped Balmer break, non-LTE hydrogen features)
- Hydrodynamic simulations of supermassive star formation and evolution
- Population synthesis models predicting the expected number of observable supermassive stars at different redshifts
- Debate over the relative abundance of supermassive stars vs. early black holes in the z>5 universe

---

## Connection to Phonon-Exflation Framework

**ALTERNATIVE MECHANISM**: The supermassive star interpretation presents a fundamentally different scenario from both the CDM and exotic dark matter seeding pathways.

**Framework implication**: If LRDs are indeed supermassive stars (not black holes), then the "early SMBH problem" does not exist. There are no 10^8-10^9 M_sun black holes at z>5—only 10^6 M_sun stars on the verge of collapse.

**Compatibility assessment**:
- **If LRDs are supermassive stars**: The framework's CDM-based black hole seeding is **preserved**. Seeds form at z~8-10 via direct collapse or mergers (as the framework predicts), starting at 10^5-10^6 M_sun. Some precursor systems (supermassive stars) may be observable at z~5-7 as LRDs.
- **If LRDs are actually black holes**: The framework must rely on either (a) CDM + rapid growth via near-Eddington accretion (consistent with Paper 40's findings), or (b) exotic dark matter seeding (inconsistent with the framework).

**Observational test**: Detailed near-infrared spectroscopy searching for the predicted V-shaped Balmer break and non-LTE hydrogen features will discriminate between supermassive stars and black holes. Current JWST data are insufficient for this discrimination.

**Verdict**: This paper is an **alternative interpretation** that, if correct, **eliminates the tension** that phonon-exflation addresses. It is compatible with the framework's predictions but represents a more economical (simpler) explanation if supermassive stars are confirmed.
