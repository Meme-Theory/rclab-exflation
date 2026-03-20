---
name: dm-de-ratio-44-result
description: S44 DM-DE-RATIO-44 PASS. 7/11 methods within 10x of observed 0.387. Best=1.060 (2.74x). S43 5.4e5 RETRACTED (chi_q was wrong quantity). DM/DE = specific heat exponent alpha, O(1) by Volovik equilibrium theorem.
type: project
---

## DM-DE-RATIO-44: Omega_DM/Omega_DE from Three Methods

### Gate Result: PASS (2026-03-15, S44 W6-4)

7 of 11 methods within 10x of observed Omega_DM/Omega_DE = 0.387. Best: Method 3a (flat-band partition with Volovik vacuum response) = 1.060 (2.74x observed).

### Key Finding

**DM/DE ratio = specific heat exponent (alpha) of the quantum vacuum.**

- Phonon gas (Bose): alpha = 3, ratio = 3.0 (7.8x obs)
- Fermi liquid: alpha = 2, ratio = 2.0 (5.2x obs)
- Flat band (B2): alpha = 1, ratio = 1.0 (2.6x obs)
- Energy-weighted GGE: alpha_eff = 1.06-1.16, ratio = 1.06-1.16 (2.7-3.0x obs)
- Observed requires alpha_eff ~ 0.39 (sublinear specific heat, non-Fermi liquid)

### S43 GGE-DM-43 RETRACTED

The 5.4e5 overshoot used chi_q = 300,338 (spectral action curvature/susceptibility). This is the WRONG quantity. The physical vacuum response follows the Volovik equilibrium theorem (Paper 05): rho_vac ~ -rho_perturbation/alpha, with alpha = specific heat exponent. DM/DE is NOT a CC problem manifestation -- it is a thermodynamic ratio, O(1) by construction in any quantum liquid.

### Methods that PASS (within 10x)

1. 1d: Volovik T<<T_c phonon analog = 3.0 (7.8x)
2. 2a: q-theory Bose = 3.0 (7.8x)
3. 2b: q-theory Fermi = 2.0 (5.2x)
4. 2c: q-theory mixed GGE = 2.258 (5.8x)
5. 2d: q-theory flat-band corrected = 1.156 (3.0x)
6. 3a: Flat-band partition = 1.060 (2.74x) -- BEST
7. 3c: Fermionic vacuum polarization = 3.821 (9.9x)

### Sensitivity

alpha_B2 = 0.5 gives ratio = 0.545 (1.4x obs, closest match).
Observed 0.387 requires alpha_eff ~ 0.39.

### Downstream

- Non-equilibrium alpha computation (GGE Gibbs-Duhem) queued for S45
- S43 GGE-DM-43 retraction confirmed (was formula error, not physics)
- DM/DE problem DECOUPLED from CC problem (ratio is O(1), absolute scale is 113 orders)

### Files

- Script: tier0-archive/s44_dm_de_ratio.py
- Data: tier0-archive/s44_dm_de_ratio.npz
- Plot: tier0-archive/s44_dm_de_ratio.png

**Why:** Established that DM/DE is a low-energy thermodynamic observable, not UV-sensitive. The Volovik equilibrium theorem makes this O(1) regardless of microscopic scale.

**How to apply:** Never use chi_q for DM/DE ratio again. Use Volovik vacuum response: rho_vac = -rho_perturbation/alpha. For B2 flat band, alpha=1. For exact match, need non-equilibrium alpha computation.
