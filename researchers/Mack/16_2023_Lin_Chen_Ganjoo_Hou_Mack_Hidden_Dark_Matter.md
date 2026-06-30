# Cosmology of Single Species Hidden Dark Matter

**Author(s):** Weikang Lin, Xingang Chen, Himanish Ganjoo, Liqiang Hou, Katherine J. Mack

**Year:** 2023

**Journal/ArXiv:** arXiv:2305.08943

---

## Abstract

Cosmology and astrophysics provide various ways to study the properties of dark matter even if it has negligible non-gravitational interactions with the Standard Model particles and remains hidden.

This work studies a type of hidden dark matter model in which the dark matter is completely decoupled from the Standard Model sector except gravitationally, and consists of a single species with conserved comoving particle number and conserved comoving entropy. This category of hidden dark matter includes models that act as warm dark matter but is more general.

In particular, in addition to having an independent temperature from the Standard Model sector, it includes cases in which dark matter is in its own kinetic equilibrium or is free-streaming, obeys fermionic or bosonic statistics, and possesses a chemical potential that controls the particle occupation number. While the usual parameterization using the free-streaming scale or the particle mass no longer applies, the authors show that all cases can be well approximated by a set of functions parameterized by only one parameter (the characteristic scale factor at the time of the relativistic-to-nonrelativistic transition), as long as the chemical potential is nonpositive.

The work studies constraints from Big Bang Nucleosynthesis, the cosmic microwave background, the Lyman-alpha forest, and the smallest halo mass. The most significant phenomenological impact is the suppression of the small-scale matter power spectrum--a typical feature when dark matter has a velocity dispersion or pressure at early times. The strongest constraints come from the Lyman-alpha forest and small dark matter halo population, limiting the transition redshift to z_transition > 6.2 x 10^7.

---

## Historical Context

Cold dark matter (CDM) has been the standard paradigm for understanding cosmic structure formation. However, CDM faces challenges at small scales: the "core-cusp problem" (observed galaxy cores are less dense than CDM predictions), the "too big to fail" problem (observed satellite galaxy mass functions differ from simulations), and potential conflicts with Milky Way satellite observations.

Warm dark matter (WDM) and similar scenarios--where dark matter has velocity dispersion or pressure at early times--suppress small-scale structure, potentially addressing these tensions. However, many such models couple to the Standard Model sector, creating additional constraints.

Purely gravitationally-coupled hidden dark matter offers an alternative: all dark matter properties are determined internally, decoupled from Standard Model thermodynamics. This includes warm dark matter-like behavior but extends to more exotic cases with independent temperatures, fermionic or bosonic statistics, and chemical potentials.

Prior work studied specific models (warm dark matter, sterile neutrinos). This work systematically analyzes the entire class of single-species gravitationally-decoupled hidden dark matter, deriving a universal parameterization and comprehensive constraints.

---

## Key Arguments and Derivations

### Hidden Dark Matter Model Framework

For a hidden sector dark matter particle completely decoupled from the Standard Model (except through gravity):

1. **Conserved Particle Number**: The number density n_chi satisfies:

   d(n_chi a^3)/dt = 0

   preserving comoving particle number.

2. **Conserved Entropy**: The entropy satisfies:

   S_chi = g_chi * (2 pi / 45) * T_chi^3 * a^3 = constant

   in the absence of interactions, where g_chi is the number of degrees of freedom and T_chi is the dark matter temperature.

3. **Statistics**: Dark matter obeys either Fermi-Dirac (fermionic) or Bose-Einstein (bosonic) statistics, controlled by the chemical potential mu_chi.

### Kinetic Equilibrium vs. Free-Streaming

The model admits two limiting cases:

**Kinetic Equilibrium Case**: Collisions among hidden sector particles maintain a thermal (Fermi-Dirac or Bose-Einstein) distribution:

f(p) = 1 / (exp((E - mu_chi)/T_chi) +/- 1)

The velocity dispersion evolves with temperature and mass:

<v^2> = integral p^2 f(p) dp / integral f(p) dp

**Free-Streaming Case**: Collisions are absent or negligible. Particles maintain a fixed velocity distribution established early, evolving ballistically:

<v^2> = constant (comoving frame)

### Universal Parameterization

The authors demonstrate that both cases, plus intermediate scenarios, can be approximated by a single parameter: the scale factor a_tr at which dark matter transitions from relativistic (temperature-dominated) to non-relativistic (mass-dominated):

a_tr ~ (m_chi / T_chi)|_0

All thermodynamic quantities (density, pressure, velocity dispersion) scale universally with a_tr. This parameter encodes:
- The dark matter mass m_chi
- Initial temperature T_chi at freeze-out
- Statistics type (fermionic/bosonic)
- Chemical potential history (if present)

### Matter Power Spectrum Suppression

For dark matter with velocity dispersion, perturbations are suppressed at scales below the free-streaming scale (or, more generally, the velocity-dispersion scale):

k_fs ~ H(a_nr) / v_DM(a_nr)

where a_nr is the nonrelativistic transition and v_DM is the characteristic dark matter velocity.

The suppression factor in the transfer function is:

T(k) / T_CDM(k) ~ [1 + (k / k_fs)^{-2p}]^{-q}

where p, q are fitting parameters depending on the transition sharpness and statistics.

### Constraints from Observations

**Big Bang Nucleosynthesis**: Early universe synthesis of light elements constrains the effective number of relativistic degrees of freedom N_eff. Hidden dark matter that is still relativistic at BBN epoch contributes to N_eff > 3.046 (Standard Model prediction). The constraint z_BBN > 10^9 limits the transition redshift.

**Cosmic Microwave Background**: Planck CMB measurements constrain the integrated effect of hidden dark matter through:
- Changes to large-scale (super-horizon) gravitational potentials
- Effects on the recombination epoch and sound speed
- Integrated Sachs-Wolfe effect modifications

**Lyman-Alpha Forest**: The distribution of neutral hydrogen in the intergalactic medium at z ~ 2-4 traces the matter power spectrum on scales 10-100 h^-1 kpc. WDM and similar models produce a characteristic suppression visible in Ly-alpha spectra. Observed Ly-alpha power spectra constrain the suppression scale.

**Halo Mass Function**: N-body simulations and observations of Milky Way satellites and dwarf galaxies constrain the abundance of dark matter halos at low masses (M_halo ~ 10^6-10^8 solar masses). Hidden dark matter with early pressure suppresses low-mass halo formation. Observed galaxy counts limit the suppression.

### Transition Redshift Constraints

The authors combine all constraints to determine allowed ranges for a_tr (equivalently, the transition redshift z_tr):

From Lyman-alpha: z_tr > 10^6
From halo mass function: z_tr > 10^7
Combined: z_tr > 6.2 x 10^7

This extraordinarily high transition redshift indicates that any gravitationally-decoupled single-species dark matter must remain highly relativistic through most of cosmic history if it is to avoid conflicting with observations.

---

## Key Results

1. **Universal Parameterization**: All single-species hidden dark matter models (kinetic equilibrium, free-streaming, fermionic, bosonic) can be approximated by functions of a single parameter: the relativistic-to-nonrelativistic transition scale factor a_tr.

2. **Power Spectrum Suppression**: The characteristic suppression scale in the matter power spectrum is set by the velocity dispersion or pressure at the transition epoch, with scale k_fs ~ H(a_tr) / v_DM(a_tr).

3. **BBN Constraint**: Big Bang Nucleosynthesis limits the abundance of relativistic hidden dark matter at z ~ 10^9, excluding scenarios where dark matter remains relativistic to recombination.

4. **CMB Constraint**: Planck CMB measurements limit deviations from CDM to ~ 10%, constraining the hidden dark matter's effect on large-scale structure.

5. **Lyman-Alpha Constraint**: Lyman-alpha forest observations provide the strongest constraint, limiting z_tr > 10^6 by requiring insufficient small-scale power suppression to conflict with observed structures.

6. **Halo Mass Function Constraint**: Dwarf galaxy and Milky Way satellite observations limit the smallest dark matter halos to z_tr > 10^7, tightening the overall constraint to z_tr > 6.2 x 10^7.

7. **Chemical Potential Role**: For negative chemical potentials (fermionic cases with occupied states), properties depend on T_chi^3 effective degrees of freedom; for bosonic cases (zero chemical potential), on T_chi^4.

---

## Impact and Legacy

This work unified the study of gravitationally-decoupled dark matter by providing a universal parameterization and comprehensive constraint framework. The single-parameter approximation accelerated phenomenological studies of beyond-CDM dark matter models.

The high transition redshift constraint demonstrates that pure gravitational decoupling is highly constrained. Most hidden dark matter models must either couple to the Standard Model (violating "hidden" assumption) or remain extremely relativistic (warmer than typical WDM scenarios).

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework addresses dark matter through emergent quasiparticles in M4 x SU(3) spectral geometry. The framework's dark matter candidate must satisfy these same observational constraints on the matter power spectrum and halo mass function.

Specific connections include:

- **Decoupled Dark Sector**: In phonon-exflation, dark matter emerges from spectral geometry--a completely gravitationally-coupled hidden sector with no direct Standard Model interactions beyond gravity. This parallels the hidden dark matter framework studied here.

- **Velocity Dispersion and Pressure**: The framework's dark matter phonons inherit velocity dispersion from internal compactification modes. This creates power spectrum suppression similar to WDM, providing testable signatures examined in this work.

- **Transition Dynamics**: Phonon-exflation's cosmological evolution includes transitions between different geometric regimes (e.g., during compactification fold). These transitions affect dark matter properties, potentially creating the relativistic-to-nonrelativistic conversion studied here.

- **Matter Power Spectrum Test**: The Lyman-alpha constraints and halo mass function limits directly test whether phonon-exflation's dark matter production mechanism creates excessive small-scale suppression.

- **Observational Consequences**: If phonon-exflation produces the correct dark matter density with appropriate velocity dispersion, the matter power spectrum predictions must match observations, providing a quantitative test of the framework's internal geometry dynamics.

This work provides the observational framework for testing whether phonon-exflation's emergent dark matter sector satisfies fundamental structure formation constraints.
