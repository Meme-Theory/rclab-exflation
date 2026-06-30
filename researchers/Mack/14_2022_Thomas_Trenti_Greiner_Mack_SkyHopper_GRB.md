# SkyHopper Mission Science Case I: Identification of High Redshift Gamma-Ray Bursts through Space-Based Near-Infrared Afterglow Observations

**Author(s):** M. Thomas, M. Trenti, J. Greiner, M. Skrutskie, Duncan A. Forbes, S. Klose, Katherine J. Mack, R. Mearns, B. Metha, G. Tagliaferri, N. Tanvir, E. Skafidas

**Year:** 2022

**Journal/ArXiv:** arXiv:2205.05694

---

## Abstract

Long-duration gamma-ray burst (GRB) afterglow observations offer cutting-edge opportunities to characterize the star formation history of the Universe back to the epoch of reionization, and to measure the chemical composition of interstellar and intergalactic gas through absorption spectroscopy.

The main barrier to progress is the low efficiency in rapidly and confidently identifying which bursts are high redshift (z > 5) candidates before they fade. This requires low-latency follow-up observations at near-infrared wavelengths to determine a reliable photometric redshift estimate. Since no current or planned gamma-ray observatories carry near-infrared telescopes on-board, complementary facilities are needed. Ground-based observatories suffer from sky visibility and weather constraints that limit the number of GRB targets observable and follow-up speed.

This work develops a Monte Carlo simulation framework to investigate a rapid-response near-infrared nano-satellite capable of simultaneous imaging in four bands from 0.8 to 1.7 micrometers (the SkyHopper mission concept). Using a reference sample of 88 afterglows from the GROND instrument on the MPG/ESO telescope, the authors find that such a nano-satellite can detect in the H band (1.6 micrometers) 72.5 +/- 3.1% of GRBs concurrently observable with Swift via its UVOT instrument, and 44.1 +/- 12.3% of high-redshift (z > 5) GRBs within 60 minutes of the GRB prompt emission. This corresponds to detecting 55 GRB afterglows per year, of which 1-3 have z > 5.

---

## Historical Context

Long-duration gamma-ray bursts are among the most luminous explosions in the observable universe. These are relativistic, jetted explosions of very massive stars at the end of their lives, detectable out to redshifts z = 10-20 and outshining their host galaxy by several orders of magnitude. Only 23 z > 5 GRBs have been collectively discovered by the entire astronomical community over the preceding 24 years prior to this work.

GRBs serve as probes of:
- The cosmic star formation history, particularly at the epoch of reionization (z > 6)
- The chemical composition of intergalactic and interstellar gas through absorption spectroscopy
- Dust properties in high-redshift galaxies
- The physics of relativistic jets

The primary challenge has been the rapid identification of high-redshift candidates before their afterglows fade below detectability. Current approaches rely on ground-based facilities that face inherent limitations: observing only the night-side of Earth, limited sky visibility from any single location, and weather-dependent interruptions.

The Gamma-Ray Burst Optical/Near-Infrared Detector (GROND) on the ground-based MPG/ESO 2.2-meter telescope was designed specifically for observing GRB afterglows in visible and near-infrared bands with demonstrated success. However, ground-based observatories fundamentally cannot compete with space-based systems for rapid, all-sky coverage.

---

## Key Arguments and Derivations

### GRB Detection and Follow-Up Requirements

Gamma-ray observatories (primarily Swift and Fermi) detect the initial prompt gamma-ray emission and transmit rapid alerts (within seconds to minutes). Follow-up observations must occur within this window to capture the fading afterglow. At high redshifts (z > 5), the optical/ultraviolet afterglow is significantly redshifted into the near-infrared, requiring infrared observations to determine photometric redshifts.

The challenge is temporal: optical afterglows typically fade as t^-1 to t^-2 power laws. An unobserved GRB at z = 5 with an optical afterglow magnitude of 20 at 10 minutes post-burst will fade to magnitude 24-25 within 60 minutes, rendering it unobservable from the ground for photometric redshift estimation.

Space-based infrared follow-up offers immediate advantages:
- No dawn/dusk constraints (24/7 sky access)
- No weather interruption
- Instantaneous slew to target (versus ground coordination delays)

### Photometric Redshift Determination

At z > 5, the Lyman break (the 912 angstrom absorption feature) shifts from ultraviolet into near-infrared. By observing the GRB afterglow simultaneously in four near-infrared bands (0.8 to 1.7 micrometers), one can identify the Lyman break location and estimate the redshift from the color distribution.

For a burst at redshift z, the rest-frame wavelength lambda_rest relates to observed wavelength lambda_obs by:

lambda_rest = lambda_obs / (1 + z)

For z = 5, the Lyman break at 912 Angstroms appears at approximately 5,472 Angstroms (0.55 micrometers), at the boundary of visible-to-infrared. For z = 10, it shifts to 1.0 micrometer.

The SkyHopper concept simulates simultaneous H-band (1.6 micrometer), I-band (0.8 micrometer), J-band (1.2 micrometer), and K-band (2.2 micrometer) observations to constrain this break location and hence the redshift.

### Light Curve Modeling and Detection Limits

The work models GRB afterglow light curves based on statistical properties from Swift UVOT observations. The modeled light curves account for:
- Typical power-law decay slopes (alpha = 0.5 to 2)
- Host galaxy dust extinction
- Intrinsic absorption at the host galaxy
- Cosmological dimming and redshifting

For each simulated GRB, the model calculates the expected flux in the H band at 60 minutes post-burst, accounting for:
- Redshift (z drawn from a cosmological probability distribution)
- Extinction parameters
- Dust properties
- Instrument sensitivity

Detection is determined by comparing predicted flux to instrument sensitivity limits.

### Monte Carlo Simulation Framework

The work implements a comprehensive Monte Carlo simulation that:

1. Draws GRB redshift distribution from the comoving volumetric rate of galaxy formation:

   dN/dV dz ~ (1 + z) * dV(z)/dz

2. Models Swift satellite detection and alert generation (assumptions about Field of View and detection efficiency)

3. Calculates orbital geometry and slew times for a near-infrared nano-satellite in Low Earth Orbit

4. Simulates light curve evolution from prompt emission through the observing window

5. Computes detection probability in each filter

6. Tabulates detection fractions for various redshift bins and catalogs

---

## Key Results

1. **Single Satellite Detection Rate**: A SkyHopper nano-satellite can detect 72.5 +/- 3.1% of GRBs concurrent with Swift UVOT observations within 60 minutes of the prompt emission.

2. **High-Redshift GRB Rate**: The mission detects 44.1 +/- 12.3% of high-redshift (z > 5) GRBs within 60 minutes, corresponding to 55 GRB afterglows per year total, with 1-3 at z > 5.

3. **Science Impact**: These discovery rates would roughly double the rate of z > 5 GRB discoveries compared to the prior 24-year historical rate (previously 23 events discovered).

4. **Constellation Enhancement**: Launching a mini-constellation of three near-infrared nano-satellites increases the detection fraction of afterglows to 83% and substantially reduces latency in photometric redshift determination.

5. **Dark GRB Population**: Systematic space-based near-infrared follow-up provides new insights into the population of dusty ('dark') GRBs primarily found at cosmic noon (z ~ 1-3).

6. **Synergy with Next-Generation Spectroscopy**: Rapid photometric redshift identification enables timely spectroscopic follow-up with next-generation ground telescopes (30-meter class) and the James Webb Space Telescope.

---

## Impact and Legacy

This work provided the scientific and technical motivation for nano-satellite missions dedicated to rapid GRB follow-up. The Monte Carlo simulation framework became a reference for assessing rapid-transient detection capabilities in space-based observatories.

The demonstration that space-based near-infrared follow-up is both feasible and scientifically compelling shaped subsequent mission concepts, including rapid-response small-satellite constellations. The work established the discovery rate requirements and latency constraints for next-generation GRB science.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework addresses the origins of particles and cosmic expansion through spectral geometry. GRBs and their afterglows probe the early universe star formation history and the properties of the intergalactic medium.

Specific connections include:

- **Early Universe Star Formation**: The framework's cosmological predictions for the expansion history directly affect the comoving volume evolution that determines GRB rates at high redshift. The star formation history prediction is central to phonon-exflation's account of cosmic structure formation.

- **Intergalactic Medium Properties**: The chemical composition measurements enabled by GRB spectroscopy test predictions about nucleosynthesis and chemical evolution, which the framework must accommodate.

- **Transient Cosmology**: GRBs as standardizable candles probe the cosmic expansion history across a wide redshift range. This provides independent tests of the framework's predictions for H(z) and dark energy evolution.

- **High-Redshift Constraints**: Discovering z > 5 GRBs pushes observational constraints to epochs where phonon-exflation's early universe dynamics are most distinctive, providing discriminating power against competing models.

The SkyHopper mission concept directly enhances the observational power available for testing phonon-exflation's cosmological predictions at high redshift.
