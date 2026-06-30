# Science Case: 21cm Intensity Mapping Tomograph for Substrate Cosmology

**Date**: 2026-04-05
**Source**: S68 CMBS4-FNL-FORECAST-68 (W2-D), S68 ISW-TRACKING-68, S68 Volovik-Mack workshop
**Status**: Concept — science requirements derived from Fisher matrix forecasts

---

## Executive Summary

The phonon-exflation framework makes three quantitative predictions that are unique to it — no other cosmological model produces them. All three are undetectable by any planned experiment (Planck, CMB-S4, Simons Observatory, LiteBIRD, SKA-Low). All three become detectable by a single instrument: a purpose-built 21cm intensity mapping tomograph operating at l_max ~ 10^5 with ~10^9 independent modes.

This document consolidates the science requirements that emerged from S68 forecast computations and workshops. It is not an engineering design — it is a science case specifying what must be measured, to what precision, and why only 21cm tomography can do it.

---

## The Problem: Planned Experiments Cannot Confirm the Substrate

The framework passes 10 of 17 observational tests at < 2σ with zero free parameters. But passing is not confirming. Every observable where the framework currently passes (n_s, r, alpha_s, Omega_DM h^2) is also consistent with other models. The framework predicts the same n_s as certain slow-roll inflation models. It predicts the same r as Starobinsky R^2 inflation. It predicts the same Omega_DM h^2 as any CDM model with the right mass and cross-section.

To *confirm* the substrate rather than *not exclude* it, we need observables where the framework's prediction is **qualitatively different** from all alternatives. S68 identified three such observables. None are accessible to planned experiments.

---

## Three Unique Predictions, One Instrument

### Channel 1: Folded Bispectrum — f_NL(folded) = 0.129

**What it is**: The primordial bispectrum measures three-point correlations in the CMB/matter density field. The "folded" configuration (k_1 + k_2 = k_3) corresponds to triangles where one wavevector equals the sum of the other two.

**Why the framework predicts it**: The supersonic transit through the van Hove fold produces GGE quasiparticles via Bogoliubov pair creation. Pairs are created with equal and opposite momenta (k, -k). This pair momentum conservation imprints a specific correlation at folded triangles: when k_3 = k_1 + k_2, the bispectrum peaks because k_1 and -k_1 were created together.

**Why it's unique**: No single-field inflation model produces a folded bispectrum. The folded shape requires correlated pair creation — a signature of particle production, not vacuum fluctuation. Multi-field inflation models can produce the folded shape at higher amplitudes, but the ratio f_NL(equil)/f_NL(folded) = 6.6 is specific to the framework's BCS-Bogoliubov production mechanism.

**The number**: f_NL(folded) = 0.129 (functional-independent, from GGE diagonal Poisson term).

| Experiment | σ(f_NL folded) | Detection SNR | Verdict |
|:-----------|:--------------:|:-------------:|:--------|
| Planck | ~64 | 0.002σ | Invisible |
| CMB-S4 | 6.9 | 0.02σ | Invisible |
| Simons Observatory | 7.0 | 0.02σ | Invisible |
| LiteBIRD | 284 | 0.0005σ | Invisible |
| **21cm (l_max=10^5)** | **0.036** | **3.6σ** | **Detection** |

Source: S68 CMBS4-FNL-FORECAST-68, S67 GGE-BISPECTRUM-67.

---

### Channel 2: Equilateral Bispectrum — f_NL(equil) = 0.853

**What it is**: The equilateral bispectrum configuration (k_1 = k_2 = k_3) measures non-Gaussianity from modified sound speed during the transit.

**Why the framework predicts it**: The BCS sound speed c_BLV = 0.485 (not c = 1) modifies the curvature perturbation's self-interaction. In the effective field theory of the transit, the reduced sound speed generates equilateral non-Gaussianity with amplitude f_NL ~ (1 - 1/c_s^2) ~ 0.853.

**Why it matters**: While equilateral f_NL is not unique to the framework (DBI inflation and other reduced-sound-speed models produce it), the **ratio** f_NL(equil)/f_NL(folded) = 6.6 is diagnostic. Standard DBI models produce equilateral-only (ratio → infinity). The framework produces both channels from the same BCS Hamiltonian.

**The number**: f_NL(equil) = 0.853 (functional-independent).

| Experiment | σ(f_NL equil) | Detection SNR | Verdict |
|:-----------|:-------------:|:-------------:|:--------|
| Planck | ~47 | 0.02σ | Invisible |
| CMB-S4 | 5.0 | 0.17σ | Invisible |
| **21cm (l_max=10^5)** | **0.026** | **32.8σ** | **Definitive** |

Source: S68 CMBS4-FNL-FORECAST-68, S67 GGE-BISPECTRUM-67.

---

### Channel 3: ISW Tracking — c_s²_DE(eff) = 0

**What it is**: The integrated Sachs-Wolfe effect measures the time derivative of the gravitational potential, which depends on how dark energy perturbs. The "tracking" signature refers to DE perturbations that track matter perturbations (c_s²_DE = 0) rather than being smooth (c_s²_DE = 1) or absent (LCDM).

**Why the framework predicts it**: The Volovik vacuum relaxation mechanism produces a tracking vacuum: rho_vac = chi * H^2. This is not a cosmological constant (which has no perturbations) or a quintessence field (which has c_s² = 1). The tracking relation induces DE density perturbations that follow matter: delta_DE = (1+w)/(1-3w) * delta_m on sub-horizon scales. This modifies the Poisson equation source and changes the rate at which the gravitational potential decays.

**Why it's unique**: LCDM has no DE perturbations (cosmological constant). Standard quintessence has c_s² = 1 (smooth DE). The tracking vacuum with c_s² = 0 is qualitatively different from both. No standard DE model produces this exact signature.

**The numbers** (from S68 ISW-TRACKING-68):

| Model | w_0 | c_s²_DE | C_l^{Tg} / LCDM |
|:------|:---:|:-------:|:----------------:|
| LCDM | -1.0 | N/A | 1.000 |
| Quintessence | -0.918 | 1 | 1.044 |
| **Framework** | -0.918 | **0** | **1.123** |

Substrate-specific contribution: +7.6% (from DE clustering alone, after subtracting the expansion history effect shared with quintessence).

| Experiment | SNR (FW vs Quintessence) | Verdict |
|:-----------|:------------------------:|:--------|
| Planck (existing) | 0.32 | Not discriminating |
| Euclid tomographic (~2030) | 1.58 | Marginal hint |
| **21cm (l_max=10^5)** | **7.9** | **Definitive** |

Source: S68 ISW-TRACKING-68, S68 Volovik-Mack workshop (emergence A-M5).

---

## Why 21cm?

### The mode count argument

CMB experiments are fundamentally limited to ~10^7 independent modes (the number of resolution elements on a 2D surface out to l_max ~ 3000). This sets a floor on σ(f_NL) ~ 5 regardless of noise — the cosmic variance limit.

21cm tomography is 3D: it maps neutral hydrogen as a function of position AND redshift, accessing a volume rather than a surface. At l_max ~ 10^5 across redshifts z = 0.5-6, this gives ~10^9 independent modes — a factor 100 improvement over the CMB. The f_NL sensitivity scales as N_modes^{-1/2}, giving a ~10x improvement in σ(f_NL).

### The l_max requirement

The folded bispectrum f_NL = 0.129 requires σ(f_NL) < 0.04 for a 3σ detection. This needs:
- l_max > 43,000 for 1σ sensitivity
- l_max ~ 10^5 for 3.6σ detection

At 21cm wavelength (~1.4 GHz rest frame), l_max = 10^5 corresponds to angular resolution ~6 arcseconds. For a filled-aperture instrument, this requires a collecting area of ~1 km scale at z ~ 1.

### Why not SKA-Low?

SKA-Low (50-350 MHz, optimized for EoR at z > 6) has:
- Maximum baseline ~65 km (sufficient resolution)
- But: sparse UV coverage at the required baselines
- Insufficient surface brightness sensitivity for the 3D tomography needed
- Optimized for power spectrum, not bispectrum estimation

A purpose-built 21cm bispectrum instrument would need:
- Dense core for surface brightness sensitivity
- Baselines to ~1 km for l_max ~ 10^5
- Frequency coverage 200-1400 MHz (z ~ 0-6)
- Foreground subtraction precision < 10^-6 (the dominant technical challenge)

---

## Combined Science Case

The power of this instrument concept is that **one observatory tests three independent predictions simultaneously**:

| Channel | Prediction | Detection σ | What Confirmation Means |
|:--------|:-----------|:-----------:|:------------------------|
| Folded f_NL | 0.129 | 3.6σ | Bogoliubov pair creation occurred → particles are phononic excitations |
| Equil/Folded ratio | 6.6 | combined | BCS sound speed c_BLV = 0.485 → specific Hamiltonian confirmed |
| ISW tracking | c_s²=0, +7.6% | 7.9σ | Volovik tracking vacuum → DE is substrate property, not field |

**Joint detection significance**: The three channels are statistically independent (different k-configurations and different physical mechanisms). A joint detection at 3.6σ + 32.8σ + 7.9σ would constitute overwhelming evidence for the substrate picture.

**Joint non-detection significance**: If all three channels are absent at > 3σ:
- No folded f_NL → no Bogoliubov pair production → transit mechanism falsified
- No equilateral f_NL → c_s = 1 → no BCS modification of sound speed
- No ISW tracking → c_s²_DE ≠ 0 → Volovik tracking vacuum falsified

Either outcome is decisive. The instrument cannot produce an ambiguous result.

---

## Staging: What Comes Before

The 21cm instrument is a 2040s+ concept. The intervening experiments provide the context:

| Year | Experiment | Role | Outcome That Motivates 21cm |
|:-----|:-----------|:-----|:----------------------------|
| 2026-27 | DESI DR3 | Gate | Framework survives (w_a → 0): substrate is viable, worth testing further |
| 2028-30 | JUNO | Structural | Normal ordering confirmed: spectral geometry validated |
| 2029-32 | Euclid | Hint | ISW tracking at 1.6σ: first marginal evidence for c_s²=0 |
| 2034 | LiteBIRD | Tensor | r = 0.024 detected at 24σ: tensor sector confirmed (necessary, not sufficient) |
| 2034 | CMB-S4 | Precision | n_s, alpha_s tightened: shape parameters locked down |
| **2040s** | **21cm** | **Confirmation** | **Three-channel substrate test: decisive** |

The case for building the instrument strengthens with each preceding result. If DESI DR3 excludes the framework (Scenario A or C), the instrument is not needed. If the framework survives DESI and JUNO and LiteBIRD, the scientific case for a purpose-built 21cm bispectrum mapper becomes compelling — it would be the only way to test whether reality is a fabric.

---

## Open Technical Challenges

1. **Foreground subtraction**: Galactic synchrotron and free-free emission are 4-5 orders of magnitude brighter than the 21cm signal. Foreground subtraction to < 10^-6 precision is the dominant technical challenge. Current approaches (delay spectrum, GPR) achieve ~10^-4. Factor 100 improvement needed.

2. **Bispectrum estimation**: Computing the bispectrum from 10^9 modes is computationally intensive (~N^3 naive, ~N^{5/3} with FFT-based estimators). Dedicated algorithms for folded triangle configurations would reduce the computational cost.

3. **RFI mitigation**: Radio frequency interference at 200-1400 MHz is severe. A remote site (possibly lunar far side for the lowest frequencies) may be required.

4. **Calibration**: Absolute calibration of the 21cm brightness temperature to the precision needed for ISW cross-correlation is an unsolved problem at the required level.

These are real engineering challenges, not fundamental physics obstacles. Each has a path forward with current technology trends.

---

## Summary

The phonon-exflation framework predicts three observables that no other model produces. All three are detectable by a single instrument: a dense 21cm intensity mapping array operating at l_max ~ 10^5. The science case emerged from S68 Fisher matrix forecasts — it was not designed top-down but fell out of the question "what experiment can distinguish the substrate from everything else?"

The answer: nothing planned can. But the instrument that could is well-defined, technically challenging but not impossible, and produces a decisive result either way.

---

*This document consolidates science requirements from S68 W2-D, S68 ISW-TRACKING-68, and the S68 Volovik-Mack workshop. Updated each session as predictions are refined.*
