# The Effects of Dark Matter Annihilation and Dark Matter-Baryon Velocity Offsets at Cosmic Dawn

**Author(s):** Liqiang Hou, Katherine J. Mack

**Year:** 2024

**Journal/ArXiv:** arXiv:2411.10626

---

## Abstract

Dark matter annihilation has the potential to leave an imprint on the properties of the first luminous structures at Cosmic Dawn as well as the overall evolution of the intergalactic medium (IGM). This work employs a semi-analytic method to model dark matter annihilation during Cosmic Dawn (approximately redshift z = 20 to 40), examining potential modifications to IGM evolution as well as gas collapse, cooling, and star formation in mini-halos.

The analysis takes into account the effects of dark matter-baryon velocity offsets, utilizing the public 21cmvFAST code, and producing predictions for the 21cm global signal. The results from the simplified model suggest that dark matter annihilation can suppress the gas fraction in small halos and alter the molecular cooling process. The impact on star formation might be positive or negative depending on parameters of the dark matter model, the redshift, and assumptions about velocity offsets.

This underscores the need for more comprehensive simulations of the effects of exotic energy injection at Cosmic Dawn as observational probes provide new insights into the process of reionization and the formation of first stars and galaxies.

---

## Historical Context

Cosmic Dawn marks the end of the universe's Dark Ages, following recombination and preceding the formation of the first galaxies and stars. This epoch (approximately z = 20-40) is a promising target for investigations of the impact of Beyond-the-Standard-Model physics such as dark matter particle interactions.

Previous studies have investigated various potential signals of dark matter annihilation in the local universe, including excess gamma-ray emission from the galactic center, but uncertainties in astrophysical contributions make interpretation challenging. The high-redshift universe presents an alternative target, with the complexity of disentangling signals from mature astrophysical sources replaced by new observational and interpretive challenges.

Dark matter annihilation during Cosmic Dawn can inject energy into primordial gas prior to and during the epoch of first star formation, potentially substantially altering the evolution of early galaxies and the intergalactic medium. Prior work has shown that dark matter annihilation can alter the recombination history and imprint observable signals on cosmic microwave background anisotropy.

The 21cm neutral hydrogen line (from the hyperfine transition) presents a promising avenue for exploring Cosmic Dawn, as it is sensitive to the state of neutral hydrogen gas from which early stars and galaxies form. Dark matter annihilation's energy injection directly affects the 21cm signal through modifications to the spin temperature and ionization state of the intergalactic medium.

---

## Key Arguments and Derivations

### Dark Matter Annihilation Energy Injection

For a dark matter particle with mass m_DM and annihilation cross-section times relative velocity <sigma v>:

The annihilation rate per unit volume is:

Gamma_ann = <sigma v> * n_DM^2 / 2

where n_DM is the dark matter number density. The energy injection rate per unit volume is:

dE/dV dt = m_DM * c^2 * Gamma_ann = m_DM * c^2 * <sigma v> * n_DM^2 / 2

This injected energy ionizes and heats the intergalactic medium. The ionization fraction x_e increases due to energy injection, while the temperature increases as:

dT_IGM/dt ~ (dE/dV dt) / (c_v * rho_baryon)

where c_v is the specific heat capacity.

### Effects on Gas Collapse and Cooling

In mini-halos (M ~ 10^5 - 10^7 solar masses at z ~ 20), the Jeans mass increases with IGM temperature:

M_J ~ T^(3/2) / (rho_baryon)^(1/2)

Increased temperature from dark matter annihilation increases M_J, suppressing the formation of the smallest structures. Additionally, the injected energy ionizes hydrogen, creating free electrons that increase the cooling timescale through collisional excitation processes.

Molecular cooling in mini-halos proceeds through H2 formation and excitation. Dark matter annihilation produces UV radiation that photodissociates H2 molecules via the Lyman-Werner process:

H2 + photon(11.2-13.6 eV) --> 2H + (photon)

This suppresses H2 abundance and cooling efficiency, preventing gas collapse and star formation in the smallest halos.

### Dark Matter-Baryon Velocity Offsets

In the early universe, dark matter and baryons decouple after recombination due to the difference in their interaction mechanisms. This creates relative velocities between dark matter and baryonic flows:

v_relative ~ a_acoustic * k_B * T / m_baryon ~ 100-300 m/s at recombination

These velocities decay with the scale factor (v ~ a^-1 in matter domination), but their effects persist at Cosmic Dawn. Velocity offsets modify:

1. **Halo Formation Rates**: Relative flows alter the halo assembly history, affecting the population of mini-halos available for star formation.

2. **Gas Infall**: The relative velocity changes the effective equation of motion for gas infalling into dark matter potential wells.

3. **21cm Signal**: The velocity offset affects the Doppler heating of gas and the spin temperature calculation.

### 21cm Global Signal Modeling

The 21cm brightness temperature contrast is:

Delta T_21 ~ T_spin / (1 + z) * x_HI * [1 - T_CMB / T_spin] * (df/dnu)|_obs

where:
- T_spin is the spin temperature of neutral hydrogen
- x_HI is the neutral hydrogen fraction
- T_CMB is the CMB temperature at the epoch
- df/dnu is the differential brightness temperature

The spin temperature depends on collisional coupling and Lyman-alpha radiation:

T_spin = [T_k + y_A * T_alpha] / [1 + y_A]

where T_k is the kinetic temperature, T_alpha is the Lyman-alpha effective temperature, and y_A is the collisional coupling coefficient.

Dark matter annihilation affects T_spin through:
- Increasing T_k (heating the IGM)
- Modifying x_HI (ionization)
- Changing Lyman-alpha intensity (photodissociation feedback)

### Semi-Analytic Model Framework

The work develops a semi-analytic model incorporating:

1. **Halo Model**: Based on the Press-Schechter formalism, modified by dark matter-baryon velocity offsets

2. **Dark Matter Annihilation**: Energy injection as a function of halo mass and redshift

3. **Gas Physics**: Collapse, cooling, and star formation in mini-halos with temperature-dependent Jeans mass

4. **21cm Integration**: Transfer of astrophysical effects to 21cm observables via 21cmvFAST code

---

## Key Results

1. **Gas Fraction Suppression**: Dark matter annihilation can suppress the gas fraction in small halos (M < 10^7 solar masses) by factors of 2-10 depending on the dark matter model and annihilation cross-section.

2. **Molecular Cooling Alteration**: Lyman-Werner feedback from dark matter annihilation reduces H2 abundance by factors of 3-100, reducing cooling efficiency and increasing cooling timescales by one or more orders of magnitude.

3. **Star Formation Dual Impact**: The effect on star formation is model-dependent. Increased heating suppresses star formation through Jeans mass increase, but reduced gas infall to small halos can either enhance or suppress star formation depending on redshift and dark matter model parameters.

4. **Velocity Offset Sensitivity**: Dark matter-baryon velocity offsets produce variations in the predicted 21cm signal of order 5-20%, introducing an important uncertainty in forward modeling.

5. **21cm Global Signal**: Dark matter annihilation with m_DM ~ 100 MeV produces measurable changes to the 21cm global signal of order 10-50 mK, within reach of experiments like LOFAR and HERA.

6. **Redshift Dependence**: Effects are strongest at z ~ 20-30, coinciding with the onset of star formation. By z > 40, reionization effects dominate.

---

## Impact and Legacy

This work demonstrated that dark matter annihilation leaves observable imprints on the earliest structures in the universe through multiple channels: gas heating, ionization, and molecular photodissociation. The semi-analytic framework enabled rapid exploration of parameter space for various dark matter models.

The emphasis on dark matter-baryon velocity offsets highlighted an often-overlooked effect in early-universe physics that affects both large-scale structure formation and 21cm observables. This motivated subsequent detailed simulations incorporating velocity offsets.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework addresses both dark matter and the expansion history through spectral geometry. Early-universe implications of the framework must be consistent with Cosmic Dawn observations.

Specific connections include:

- **Dark Matter Annihilation Signals**: If phonon-exflation's dark matter candidate experiences annihilation or decay at Cosmic Dawn, the framework must predict consistent energy injection rates to avoid conflicts with observations.

- **Molecular Gas Suppression**: The framework's predictions for early star formation and reionization depend on molecular cooling in mini-halos. If internal compactification produces excess radiation or heating, it must be accounted for in star formation models.

- **21cm Observable**: The framework's expansion history predictions affect the 21cm signal through the Hubble parameter's effect on T_spin and redshift evolution. Matching observed 21cm features tests the framework's Cosmic Dawn predictions.

- **Gas Infall and Dynamics**: The framework's geometry evolution affects the baryon-dark matter dynamics at Cosmic Dawn. If phonon-exflation produces velocity offsets or modified infall dynamics, these must be incorporated in structure formation simulations.

- **Early Ionization Constraints**: If phonon-exflation's dark matter or other framework components produce ionization at Cosmic Dawn, the resulting ionization fraction must match both 21cm constraints and CMB polarization limits.

The semi-analytic framework here provides tools for testing whether phonon-exflation's Cosmic Dawn predictions are consistent with emerging 21cm observations.
