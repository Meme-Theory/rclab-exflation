# Dark Energy Spectroscopic Instrument (DESI) 2024 Baryon Acoustic Oscillation Results

**Author(s):** DESI Collaboration (300+ authors)
**Year:** 2024
**Journal/ArXiv:** Physical Review / arXiv

---

## Abstract

The Dark Energy Spectroscopic Instrument (DESI), which began full operations in May 2021, has obtained spectroscopy for over 35 million galaxies and quasars by 2024. This paper reports baryon acoustic oscillation (BAO) measurements from the first year of DESI data, covering approximately 850 square degrees of sky and redshift ranges 0.1 < z < 2.1.

DESI measures the BAO peak (a standard ruler imprinted in galaxy clustering at large scales, ~150 Mpc) to high precision, constraining the comoving angular-diameter distance D_A(z) and Hubble parameter H(z) at multiple redshifts. Combined with CMB and Type Ia supernovae data, DESI BAO measurements provide the most precise constraints on the expansion history and equation of state of dark energy (w(z)) across cosmic time.

Key result: DESI 2024 BAO shows ~2.6 sigma evidence for dynamical dark energy (w not equal to -1), with the possibility that dark energy becomes phantom (w < -1) at recent redshifts (z < 0.3).

---

## Historical Context

The baryon acoustic oscillation (BAO) feature arises from acoustic oscillations in the primordial baryon-photon fluid before recombination. These oscillations imprint a characteristic length scale (150 Mpc comoving) on galaxy correlations. Because this scale is well-predicted from theory and relatively insensitive to uncertain galaxy physics, BAO serves as a standard ruler for cosmography.

Previous BAO measurements:
- **SDSS**: Baryon Oscillation Spectroscopic Survey (BOSS, 2012-2014) — redshifts 0.1-0.7
- **Spectroscopic Surveys** (2016+): eBOSS, 4MOST, 2dFLenS extended to z ~ 1.2

DESI dramatically increases sample size and redshift range, enabling measurements of w(z) with unprecedented precision.

---

## Key Results

### BAO Distance Measurements

DESI 2024 presents BAO measurements at multiple redshifts:

| Redshift Bin | z | D_A(z) / D_A^{Planck} | H(z) / H_0^{Planck} |
|---|---|---|---|
| ELG (low) | 0.51 | 1.001 ± 0.026 | 0.990 ± 0.033 |
| ELG (mid) | 0.71 | 1.003 ± 0.033 | 1.009 ± 0.025 |
| LRG | 0.82 | 1.032 ± 0.037 | 1.030 ± 0.037 |
| Quasar | 1.49 | 1.091 ± 0.068 | 1.021 ± 0.091 |

**Key observation**: D_A and H measurements are 1-3 percent measurements, consistent with LCDM but showing ~1-2 sigma hints of deviation.

### Equation of State (w(z)) Constraints

Combining DESI BAO with Planck CMB and Pan-STARRS Type Ia SNe:

$$w_0 = -0.72 \pm 0.08 \text{ (present day)}$$
$$w_a = -0.41 \pm 0.31 \text{ (evolution parameter)}$$

where w(z=0) = w_0 and w(z) = w_0 + w_a * z/(1+z).

**Interpretation**:
- If w_0 < -1, dark energy is phantom (energy density increases with expansion)
- Current best fit: w_0 ~ -0.72, suggesting dark energy is weaker than cosmological constant
- Posterior includes w_0 = -1 (LCDM) at ~1.5 sigma confidence

### H_0 Tension Implications

DESI BAO + Planck yields:
$$H_0 = 67.9 \pm 1.1 \text{ km/s/Mpc}$$

still in tension with local supernova ladder measurements (73.0 ± 1.0). DESI does not resolve this discrepancy; the tension persists at 3.5+ sigma.

However, if dark energy evolves (w_a ≠ 0), the inferred H_0 from BAO + CMB shifts slightly. Early dark energy models (EDE) that modify H_0 are disfavored by DESI, as they predict different w(z) evolution incompatible with BAO.

### Growth of Structure

DESI measures galaxy clustering amplitude sigma_8(z), constraining growth rate:

$$\frac{d \ln D}{d \ln a} = \Omega_m^{0.545} / b$$

where b is galaxy bias. Current results:
- sigma_8(z ~ 0.5): consistent with Planck + LCDM to 1 percent
- sigma_8(z ~ 1.5): 2 sigma below Planck prediction

This hints at either modified gravity (f(R), scalar-tensor theories reduce growth) or systematics. DESI's larger sample will resolve this in full data release.

### Key Statistical Results

| Measurement | Value | Implication |
|---|---|---|
| Omega_m (matter density) | 0.299 ± 0.014 | 30% of critical density |
| Omega_Lambda (dark energy) | 0.701 ± 0.014 | 70% dark energy (at z=0) |
| w (if constant) | -0.98 ± 0.05 | LCDM (w=-1) preferred |
| Dynamical w evidence | 2.6 sigma | Hint of dark energy evolution |
| Curvature (Omega_K) | -0.003 ± 0.006 | Flat universe confirmed |

### Large-Scale Structure Systematics

DESI carefully models:
- **Redshift errors** (2% typical for emission-line galaxies)
- **Fiber collisions** (adjacent galaxies on same fiber not always observed)
- **Dust extinction** (dust-corrected magnitudes and colors)
- **Foreground contamination** (stellar and QSO contaminants removed)

Systematic uncertainties on BAO measurements are sub-dominant (< 0.5% for most bins).

---

## Technical Highlights

### DESI Instrument

- 5,000 optical fibers on 3.8-meter Mayall telescope (Kitt Peak)
- Covers 14,000 square degrees (final target: ~200 sq deg/night)
- Spectra cover 360-1000 nm (Z-band to I-band)
- Redshift precision: sigma_z ~ 100 km/s (0.1% for BAO analysis)

### Target Selection

DESI focuses on:
- **ELG** (Emission-Line Galaxies): z ~ 0.3-1.1, ~4 million targets
- **LRG** (Luminous Red Galaxies): z ~ 0.4-1.0, ~0.9 million targets
- **QSO** (Quasars): z ~ 0.9-3.5, ~0.6 million targets

Each population probes different cosmic epochs with BAO peaks of varying signal-to-noise.

---

## Cosmological Implications

### Dynamical Dark Energy

The 2.6 sigma hint of w < -1 (phantom crossing) is intriguing but not definitive. Possible explanations:
1. **Statistical fluctuation** (most likely at current sigma level)
2. **Dynamical dark energy** (scalar field with time-varying equation of state)
3. **Modified gravity** (w is effectively time-varying due to growth modifications)
4. **Early dark energy + phantom crossing** (phase transition in dark sector)

### Tensions in Lambda-CDM

DESI results highlight two unresolved discrepancies:
1. **H_0 tension**: Local ladder (73 km/s/Mpc) vs CMB+DESI (67.9 km/s/Mpc)
2. **S_8 tension**: Growth rate from large-scale structure weaker than Planck predictions

Both tensions persist with DESI 2024 data, requiring either:
- Improved systematics understanding
- New physics (modified gravity, early dark energy)
- Unknown observational biases

---

## Connection to Phonon-Exflation Framework

DESI 2024 BAO measurements directly test the phonon-exflation model:

1. **Dark energy equation of state**: Phonon-exflation predicts dark energy emerges from spectral geometry (analogous to cosmological constant, w ~ -1). DESI's hint of w < -1 challenges this if confirmed. The framework would need to include mechanisms for phantom-like behavior (e.g., kinetic dominance, multiple condensate species).

2. **Expansion history H(z)**: DESI measures H(z) at multiple redshifts. Phonon-exflation predictions for H(z) depend on fiber dynamics during cosmic expansion. Comparison with DESI data can test whether the internal SU(3) geometry satisfies observational constraints.

3. **Growth rate of structure (sigma_8(z))**: The hint of reduced growth at high z (z ~ 1.5) could indicate modified gravity from internal SU(3) dynamics. If the fiber couples to matter growth, this is a testable signature.

4. **H_0 tension resolution**: If phonon-exflation provides a unified description of dark matter and dark energy, it might offer a new resolution to the H_0 discrepancy. Early-universe dynamics from fiber could shift the sound horizon, affecting both CMB-inferred H_0 and BAO-inferred H_0 differently.

5. **BAO peak location**: The comoving BAO scale (~150 Mpc) is a standard ruler. If M4 x SU(3) geometry modifies the sound speed in the early universe (different from GR+LCDM), the inferred distances from BAO would shift systematically.

---

## Impact and Legacy

DESI's 2024 BAO results represent the largest spectroscopic redshift survey to date. The precision achieved constrains dark energy evolution and large-scale structure growth to unprecedented levels. Full DESI data release (5 years, ~35 million redshifts) will enable:

- Measurement of w(z) to 2% precision (currently ~7%)
- Test of modified gravity theories at z ~ 1
- Identification of new clustering-based dark energy signatures
- Improved H_0 measurements that may resolve or sharpen existing tensions

Combined with future CMB experiments and gravitational wave standard sirens, DESI will likely determine whether dark energy is the cosmological constant or something more exotic.
