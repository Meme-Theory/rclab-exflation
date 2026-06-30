# DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations

**Author(s):** DESI Collaboration (A. G. Adame, J. Aguilar, S. Ahlen, S. Alam, et al.)
**Year:** 2024
**Journal:** Prepared for submission to JCAP
**arXiv:** 2404.03002
**Relevance:** CRITICAL

---

## Abstract

[INCOMPLETE - abstract not fully extractable from PDF due to file size. The following is reconstructed from the paper's introduction and results sections.]

The DESI collaboration presents cosmological constraints from baryon acoustic oscillation (BAO) measurements using the first year of DESI data (Data Release 1). BAO distances are measured from galaxies, quasars, and the Lyman-alpha forest across the redshift range 0.1 < z < 4.2. Combined with CMB and Type Ia supernovae data, DESI BAO measurements provide constraints on dark energy that show hints of deviation from a cosmological constant when the dark energy equation of state is allowed to vary with redshift.

---

## Key Arguments and Derivations

### 1. DESI Instrument and Survey

DESI is a Stage IV dark energy spectroscopic survey installed on the 4-meter Mayall telescope at Kitt Peak National Observatory. It uses 5,000 robotic fiber positioners to simultaneously obtain spectra of galaxies, quasars, and Lyman-alpha forest systems. The DR1 data release covers the first year of observations.

### 2. BAO Tracers

DESI measures BAO using multiple tracers spanning a wide redshift range:
- Bright Galaxy Sample (BGS): z ~ 0.1-0.4
- Luminous Red Galaxies (LRG): z ~ 0.4-0.8 (two bins: LRG1 and LRG2)
- Emission Line Galaxies (ELG): z ~ 0.8-1.6 (two bins: ELG1 and ELG2)
- Quasars (QSO): z ~ 0.8-2.1
- Lyman-alpha forest (Lya): z ~ 1.77-4.16

### 3. BAO Distance Measurements

From the BAO feature in the two-point correlation function and power spectrum, DESI measures:
- D_M(z)/r_d: the comoving angular diameter distance divided by the sound horizon
- D_H(z)/r_d: the Hubble distance divided by the sound horizon
- D_V(z)/r_d: the volume-averaged distance (for isotropic fits)

### 4. Dark Energy Equation of State

Using the CPL parameterization w(a) = w_0 + w_a(1-a), where a = 1/(1+z):

**DESI BAO + CMB + Pantheon+ SNe:**
- w_0 = -0.45 +/- 0.21 (stat)
- w_a = -1.79 (+0.48/-0.65)
- Preference over LCDM (w_0 = -1, w_a = 0): ~2.5 sigma

**DESI BAO + CMB + Union3 SNe:**
- w_0 = -0.65 +/- 0.24
- w_a = -1.27 (+0.64/-0.82)
- Preference over LCDM: ~3.9 sigma

### 5. Flat LCDM Parameters

**DESI BAO + CMB:**
- Omega_m = 0.307 +/- 0.005
- H_0 = 67.97 +/- 0.38 km/s/Mpc
- r_d = 147.09 +/- 0.26 Mpc

## Key Results

1. DESI provides the most precise BAO measurements to date across 0.1 < z < 4.2
2. Flat LCDM: Omega_m = 0.307 +/- 0.005, H_0 = 67.97 +/- 0.38 km/s/Mpc (DESI+CMB)
3. In the w_0-w_a parameterization, DESI+CMB+SN data prefer dynamical dark energy over a cosmological constant at 2.5-3.9 sigma depending on the SN dataset
4. The preferred values w_0 > -1, w_a < 0 indicate dark energy that was less negative (closer to matter-like) in the past and is becoming more negative with time
5. The deviation from LCDM is driven primarily by the combination of low-z and high-z BAO measurements
6. Curvature constraint: Omega_k = 0.0024 +/- 0.0016 (DESI+CMB), consistent with flatness
7. Neutrino mass: sum m_nu < 0.072 eV (95% CL, DESI+CMB, flat LCDM)

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| CPL parameterization | $w(a) = w_0 + w_a(1-a)$ | Chevallier-Polarski-Linder |
| Hubble distance | $D_H(z) = c/H(z)$ | Standard |
| Comoving angular diameter distance | $D_M(z) = c\int_0^z dz'/H(z')$ | Standard |
| Volume-averaged distance | $D_V(z) = [z D_M^2(z) D_H(z)]^{1/3}$ | Standard |
| Friedmann with dark energy | $H^2(z) = H_0^2[\Omega_m(1+z)^3 + \Omega_\text{DE}(1+z)^{3(1+w_0+w_a)}e^{-3w_a z/(1+z)}]$ | CPL extension |

## Relevance to Phonon-Exflation

The DESI DR1 BAO results are the single most important observational test for the phonon-exflation framework. The hint of dynamical dark energy (w_0 > -1, w_a < 0) at 2.5-3.9 sigma is precisely the kind of signal the framework predicts: if the dark energy density arises from the spectral action evaluated on the evolving internal geometry, w(z) should deviate from -1 in a tau-dependent way. The framework closed the DESI dynamical DE channel (Session 22d) because the rolling quintessence mechanism required a specific tau trajectory incompatible with the clock constraint. However, the instanton gas paradigm (Session 37+) reopens this question: the GGE relic from the transit may produce an effective w(z) that evolves with redshift. The DESI DR2 data (2503.14738) provides the decisive test. The DESI+CMB constraint on Omega_m = 0.307 +/- 0.005 must be reproduced by the DM/CC partition from the instanton gas, which predicted Omega_L/Omega_M = 1500:1 (Session 46) vs. the observed ~2.2:1 -- a 700x discrepancy being investigated.
