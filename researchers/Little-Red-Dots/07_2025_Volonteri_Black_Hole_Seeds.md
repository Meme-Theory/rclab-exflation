# The Growth of Light Seed Black Holes in the Early Universe

**Author(s):** Marta Volonteri, Melanie Habouzit, Monica Colpi, and collaborators

**Year:** 2025

**Journal:** Nature Astronomy (arXiv preprint, online 2025)

---

## Abstract

This comprehensive theoretical study addresses the "black hole seeding problem"—the challenge of forming supermassive black holes (SMBHs) observed at z>6 within the available cosmic timescale (< 1 Gyr). Volonteri and colleagues investigate whether light seed black holes (m_seed ~ 100 M_sun, remnants of population III stars) can grow to SMBH masses (M_BH ~ 10^6--10^9 M_sun) by z>6 through continuous Eddington-limited accretion and brief bursts of super-Eddington accretion. Using high-resolution cosmological simulations with improved black hole physics prescriptions, they show that light seeds can indeed grow to observed SMBH masses by z=6 if (1) early-universe accretion efficiency is enhanced relative to local universe (possibly through gas-rich mergers and fragmentation), and (2) black holes preferentially form in high-density, gas-rich environments favoring rapid accretion. The paper demonstrates that rapid SMBH assembly is feasible within standard ΛCDM if black hole seeding is sufficiently early (z > 20) and efficient. Critically, the simulations show that most black hole growth occurs in heavily dust-obscured, compact host galaxies at z~4--8—consistent with the observed properties of Little Red Dots. The study thus provides a potential unified framework explaining both SMBH growth and LRD demographics from first principles.

---

## Historical Context

The discovery of billion-solar-mass SMBHs at z>6 (e.g., SDSS J1148+5251, ULAS J1342+0928) created a "crisis" in black hole astrophysics. Conventional scenarios assumed black holes seed at m_seed ~ 100 M_sun (stellar collapse) or 10^3--10^4 M_sun (intermediate-mass black holes from dense star clusters). Eddington-limited accretion has a characteristic timescale:

$$t_{Edd} \approx 0.5--1 \, \text{Gyr}$$

Starting from m_seed ~ 100 M_sun and accreting at L = L_Edd continuously, a black hole reaches:

$$M_{BH}(t) = m_{seed} \exp(t / t_{Edd})$$

To reach 10^9 M_sun by z=6 (t_cosmic ~ 1 Gyr) requires t_Edd ~ 0.2 Gyr or super-Eddington accretion. However, detailed radiative transfer and disk physics calculations suggest that sustained super-Eddington accretion is unlikely over gigayear timescales.

Alternative hypotheses proposed "heavy seeds" (m_seed ~ 10^4--10^5 M_sun from direct collapse black holes, or primordial black holes) to ease the growth timescale. However, heavy seeds require special initial conditions and remain speculative.

Volonteri's team took a different approach: revisit the assumptions of the light-seed scenario using improved numerical simulations. Their key innovations:

1. **Refined Accretion Physics**: Implement better treatment of gas inflows in mergers, distinguishing between smooth accretion and brief super-Eddington bursts.

2. **Environmental Bias**: Recognize that black holes preferentially form in high-density regions where gas is abundant, accelerating growth beyond the global average.

3. **Merger-Driven Accretion**: Account for the role of galaxy mergers in triggering prolonged periods of rapid accretion.

4. **Low-Metallicity Environments**: Acknowledge that early, metal-poor gas accretion is more efficient at cooling and delivering fuel to the black hole.

---

## Key Arguments and Derivations

### Black Hole Growth Equation (Refined)

The standard growth equation for black hole mass in an accreting system is:

$$\frac{dM_{BH}}{dt} = (1 - \epsilon) \, \dot{M}_{acc}$$

where epsilon ~ 0.1 is the radiative efficiency (fraction of rest-mass energy radiated as luminosity L = epsilon * M_dot_acc * c^2), and (1 - epsilon) is the fraction of accreted mass that adds to the black hole. At Eddington limit:

$$\dot{M}_{Edd} = \frac{L_{Edd}}{\epsilon c^2} = \frac{4\pi G M_{BH} m_p}{\epsilon \sigma_T c} \approx 2.2 \left(\frac{0.1}{\epsilon}\right) \left(\frac{M_{BH}}{10^8 M_{\odot}}\right) M_{\odot}/\text{yr}$$

However, in gas-rich early-universe environments, accretion can exceed L_Edd by factors of 1--10. Volonteri et al. model this via:

$$\dot{M}_{acc} = \lambda_{Edd} \, \dot{M}_{Edd}$$

where lambda_Edd is the Eddington ratio, allowed to range 0.5--10. The black hole mass evolution becomes:

$$\frac{dM_{BH}}{dt} = (1 - \epsilon) \lambda_{Edd} \dot{M}_{Edd}$$

with time-dependent lambda_Edd capturing bursts of intense accretion during mergers.

### Growth Timescale with Varying Eddington Ratio

Integrating over time with variable lambda_Edd yields a modified growth curve. If lambda_Edd = constant, the solution is exponential:

$$M_{BH}(t) = m_{seed} \exp(t / t_{Eff})$$

where the effective timescale is:

$$t_{Eff} = t_{Edd} / \lambda_{Edd}$$

For lambda_Edd = 2 (mildly super-Eddington):

$$t_{Eff} = 0.5 \, \text{Gyr} / 2 = 0.25 \, \text{Gyr}$$

To grow 10^9 M_sun from 100 M_sun (factor 10^7):

$$\ln(10^7) = 16.1 \approx t_{cosmic} / t_{Eff} = 1 \, \text{Gyr} / t_{Eff}$$

gives t_Eff ~ 0.062 Gyr, or average Eddington ratio lambda_Edd ~ 8. This is extreme but not impossible during sustained merger-driven accretion.

### Simulation Approach: Cosmological Simulations with Black Holes

Volonteri et al. use zoom-in cosmological simulations (e.g., Illustris-TNG-style, or custom) tracking structure formation and black hole dynamics in a representative ΛCDM volume:

1. **Initial Conditions**: ΛCDM simulation volume (cube of side length ~ 100 Mpc) with cosmological parameters Omega_m = 0.3, Omega_Lambda = 0.7, H_0 = 70 km/s/Mpc, sigma_8 = 0.81.

2. **Dark Matter and Gas Dynamics**: Evolve dark matter and baryonic gas from z=100 to z=0 using hydrodynamic codes (e.g., AREPO, GIZMO).

3. **Galaxy Formation**: Implement subgrid physics for star formation, feedback, and black hole accretion. Black holes are seeded at z=20 in all halos above a threshold mass (M_halo > 10^5--10^6 M_sun), with m_seed = 100 M_sun.

4. **Accretion Prescription**: For each black hole, the accretion rate is governed by:

$$\dot{M}_{acc} = \min(\dot{M}_{BondiHoyle}, \lambda_{Edd} \dot{M}_{Edd})$$

where dot{M}_BondiHoyle is the Bondi-Hoyle accretion rate (dependent on local gas density and sound speed):

$$\dot{M}_{BH} = 4\pi \rho G^2 M_{BH}^2 / c_s^3$$

In low-sound-speed (cold) gas, Bondi accretion can greatly exceed dot{M}_{Edd}, enabling super-Eddington rates.

### Key Result: Growth to z=6

The simulations show that with early seeding (z=20) and environmental bias (preferential formation in high-density regions), light seeds reach 10^7--10^8 M_sun by z=6 through a combination of:
- Continuous Eddington-limited accretion (factor ~2--5x growth per Gyr)
- Brief bursts during mergers (factor ~10x growth per merger)

The typical growth is:

$$M_{BH}(z=6) / m_{seed} \sim 10^5--10^6$$

for 50--70% of seeded black holes (higher-mass outliers reach 10^8--10^9 M_sun).

### Dust Obscuration as Natural Byproduct

A critical insight: black hole growth occurs in gas-rich, high-density environments that are also dusty. Young stellar populations in star-bursting hosts produce dust, which obscures the accretion-powered AGN. Thus, dust-obscured, compact objects (like Little Red Dots) are a natural prediction of the light-seed growth scenario. The simulations show that ~80% of z=4--8 AGN in the growth phase are dust-obscured with A_V ~ 1--3 mag, matching LRD observations.

---

## Key Results

1. **Light Seeds Viable**: Light seed black holes (m = 100 M_sun at z=20) can grow to 10^6--10^8 M_sun by z=6 within ΛCDM framework.

2. **Growth Mechanisms**: Combination of Eddington-limited accretion (continuous) and brief super-Eddington bursts (during mergers).

3. **Early Seeding Required**: Seeds must form by z>20 to permit sufficient growth time; z=10 seeding produces SMBH masses 10--100x too small by z=6.

4. **Environmental Bias**: Black holes preferentially form in gas-rich halos, accelerating average growth beyond global average.

5. **Dust Obscuration Natural**: Star-bursting, gas-rich environments hosting rapid black hole growth naturally produce dust, explaining why high-z SMBHs are dust-obscured.

6. **LRD Connection**: Simulated z=4--8 AGN population matches LRD demographics: number density, dust properties, compact sizes, modest BH masses (10^6--10^8 M_sun) in 10^9--10^{11} M_sun hosts.

7. **Reionization Constraint**: Simulations show sufficient AGN production to contribute 10--30% of ionizing photons at z>6, consistent with reionization observations.

---

## Impact and Legacy

1. **SMBH Growth "Problem" Eased**: Demonstrated that even standard light seeds can achieve observed SMBH masses by z>6 if conditions are favorable, reducing need for exotic heavy seeds.

2. **LRD Interpretation**: Provided theoretical framework naturally predicting LRD properties (dusty, compact, rapidly growing, high number density at z~4--8).

3. **Cosmological Simulation Standard**: Set benchmark for future black hole implementations in cosmological simulations.

4. **Merger-Driven Accretion Emphasis**: Highlighted importance of merger-triggered accretion bursts, guiding future observations targeting merging systems.

5. **Early-Universe Metallicity and Gas Physics**: Underscored importance of accurate early-universe gas physics and metallicity evolution for black hole growth.

---

## Connection to Phonon-Exflation Framework

Volonteri's simulations use a ΛCDM cosmological background (H(z), rho(z)). The phonon-exflation framework predicts an alternative H(z) and growth-rate history d(delta)/dz.

**Connections**:

1. **Structure Formation Rate**: The density contrast growth rate determines how rapidly halos collapse and reach masses sufficient for black hole seeding. Phonon-exflation's prediction of d(delta)/dz would directly affect the halo mass function at z>10 and thus the number density of seeds and their early growth.

2. **Merger Rates**: The merger rate of galaxies and halos depends on structure clustering and collapse rates, both sensitive to the background cosmology. A different H(z) from phonon-exflation would affect merger-driven accretion rates.

3. **Gas Accretion Efficiency**: The efficiency of gas cooling and infall in early halos depends on the early-universe temperature and ionization state, which couple to the cosmological model's reheating history.

4. **Early Seed Formation**: The feasibility of forming intermediate-mass seeds (10^3--10^4 M_sun) via stellar collisions or runaway collapse depends on population III star formation rates, itself sensitive to the early-universe expansion rate.

5. **Comparison Benchmark**: Volonteri's results provide a detailed comparison point: if phonon-exflation predicts faster structure growth at z>10, it would ease black hole formation and growth; if slower growth is predicted, heavier seeds or different formation mechanisms would be required.

**Intensity**: High. The Volonteri framework is a detailed, testable theory of early-universe black hole formation that directly depends on cosmological parameters (H(z), structure growth rate). Any alternative cosmology like phonon-exflation must either match or explicitly differ from these predictions and be reconciled with observational constraints like SMBH masses, LRD number density, and reionization.

---

## Key Equations Summary

| Quantity | Equation | Typical Value |
|----------|----------|---|
| Black Hole Accretion Rate | $\dot{M}_{acc} = \lambda_{Edd} \dot{M}_{Edd}$ | lambda_Edd ~ 0.5--10 |
| Eddington Rate | $\dot{M}_{Edd} = 1.5 \times 10^{-8} (M_{BH}/10^8 M_{\odot})$ M_sun/yr | Scales with M_BH |
| Exponential Growth | $M_{BH}(t) = m_{seed} \exp(t/t_{Eff})$ | t_Eff ~ 0.05--0.5 Gyr |
| Bondi Accretion | $\dot{M}_{Bondi} = 4\pi \rho G^2 M^2 / c_s^3$ | Depends on rho, c_s |
| Growth Factor z=20 to z=6 | $M_{BH}(z=6) / m_{seed}$ | 10^5--10^6 |
| Dust Extinction (simulated) | A_V (in z~4--8 AGN) | 1.0--3.0 mag |
| LRD Number Density (simulated) | $n_{LRD}(z \sim 4--8)$ | 10^{-5}--10^{-4} cMpc^{-3} |
