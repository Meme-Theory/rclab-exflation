# Phonon-Assisted Casimir Interactions between Piezoelectric Materials

**Authors:** Dai-Nam Le, Pablo Rodriguez-Lopez, Alejandra Woods
**Year:** 2024
**Journal:** Communications Materials, Vol. 5, Article 701

---

## Abstract

This paper investigates how lattice vibrations (phonons) in piezoelectric materials modulate the Casimir force—a quantum vacuum effect mediated by virtual photons. The strong coupling between electromagnetic fields and lattice oscillations in piezoelectrics gives rise to hybrid excitations (phonon polaritons) with mixed character. Using the Born-Huang hydrodynamics model and generalized Lifshitz theory, the authors calculate Casimir interactions for systems involving SiC and other piezoelectrics, accounting for longitudinal optical (LO) phonons, transverse optical (TO) phonons, and mixed phonon-polariton modes. Key findings: (1) The Casimir force magnitude and sign are sensitively dependent on piezoelectric phonon modes; (2) Tuning phonon frequencies (via strain, temperature, or doping) allows active control of Casimir attraction/repulsion; (3) Hybrid longitudinal-transverse modes produce unusual quantum-thermal effects in finite-thickness structures; (4) Different piezoelectric polytypes exhibit distinct Casimir signatures, making the Casimir effect a probe of phonon polariton structure. The paper demonstrates that piezoelectric materials provide a platform for engineering quantum vacuum forces through control of phononic excitations—with implications for quantum devices, precision metrology, and fundamental tests of quantum field theory.

---

## Historical Context

The Casimir effect has a rich history bridging quantum mechanics and materials science:

1. **Casimir prediction (1948)**: Dutch physicist Hendrik Casimir predicted that two uncharged conducting plates separated by a small gap experience an attractive force due to quantum vacuum fluctuations. Virtual photon-electron pairs pop in and out of the vacuum, and the boundary conditions at the plates modify the density of virtual photons, leading to a net pressure.

2. **Casimir force measurement (1997)**: Over 50 years later, Lamoreaux experimentally confirmed Casimir's prediction, measuring the force with torsion balance precision. The effect was real and matched theory to ~1%.

3. **Lifshitz theory (1956)**: Evgeny Lifshitz generalized Casimir's calculation to arbitrary materials (not just perfect conductors), deriving the force in terms of the dielectric function $\epsilon(\omega)$ of the materials. This opened the way to engineering the Casimir force via material properties.

4. **Casimir in metamaterials (2000s-2010s)**: Researchers began exploring how engineered materials—metamaterials, photonic crystals, phononic crystals—could modify the Casimir force. The idea emerged that the optical/phononic response of materials, not just electromagnetic properties, could mediate quantum vacuum effects.

5. **Phonon-photon coupling (2020s)**: The recognition that piezoelectric materials strongly couple photons to phonons opened a new frontier. By controlling phonons, one could modulate quantum vacuum forces—a direct bridge between condensed matter and quantum field theory.

Le et al.'s 2024 paper represents the cutting edge of this development, explicitly calculating Casimir forces in piezoelectrics where phonon-photon coupling is strongest.

---

## Key Arguments and Derivations

### Casimir Force in Vacuum and in Media

In vacuum, the Casimir force between two metallic plates separated by distance $d$ is:

$$F_{\text{Casimir}} = -\frac{\pi^2 \hbar c}{240 d^4}$$

This is an attractive force, and its magnitude is independent of the material—it arises purely from boundary conditions on electromagnetic modes.

When materials are present (with dielectric function $\epsilon(\omega)$), the Lifshitz formula gives:

$$F = \frac{\hbar}{2\pi} \int_0^\infty d\omega \, \text{Tr} \ln \left[ 1 - r_1(\omega) r_2(\omega) e^{2i k(\omega) d} \right]$$

where:
- $r_1(\omega), r_2(\omega)$ are Fresnel reflection coefficients for the two materials
- $k(\omega) = \sqrt{\epsilon(\omega)} \omega / c$ is the wavenumber in the material
- $d$ is the separation

The reflection coefficients depend on the dielectric function $\epsilon(\omega, T)$, which encodes the material's response to electromagnetic fields at all frequencies.

### Dielectric Function of Piezoelectrics: Phonon Polaritons

For piezoelectric materials like SiC, the dielectric function exhibits resonances at phonon frequencies:

$$\epsilon(\omega) = \epsilon_\infty \frac{\omega^2 + i\gamma \omega - \omega_{\text{TO}}^2}{\omega^2 + i\gamma \omega - \omega_{\text{LO}}^2}$$

where:
- $\epsilon_\infty$ is the high-frequency dielectric constant
- $\omega_{\text{TO}}$ is the transverse optical phonon frequency (resonance)
- $\omega_{\text{LO}}$ is the longitudinal optical phonon frequency
- $\gamma$ is a damping rate

Between the TO and LO frequencies, the dielectric function is negative ($\epsilon < 0$), a regime where electromagnetic waves cannot propagate—they are evanescent. This is the reststrahlen band, a frequency range where the material is reflective.

The key hybrid excitation is the **phonon polariton**—a bound state of a photon and a phonon. These modes exist at frequencies where photon and phonon energies are resonant:

$$\omega_{\text{polariton}} = \sqrt{\frac{\omega_{\text{TO}}^2 + \omega_{\text{LO}}^2}{2}} \pm \sqrt{\frac{(\omega_{\text{LO}}^2 - \omega_{\text{TO}}^2)^2}{4} + \Delta}$$

where $\Delta$ accounts for coupling strength.

### Phonon-assisted Casimir Force Calculation

Le et al. compute the Casimir force using the generalized Lifshitz formula but with the full dielectric function of the piezoelectric, including all three types of contributions:

1. **Longitudinal optical (LO) phonon contribution**: At frequencies near $\omega_{\text{LO}}$, the material becomes strongly polarizable, modifying the reflection coefficient. This enhances the Casimir force.

2. **Transverse optical (TO) phonon contribution**: At frequencies near $\omega_{\text{TO}}$, the reflection coefficient changes sign, switching from attractive to repulsive Casimir interaction.

3. **Phonon-polariton contribution**: The hybrid modes create interference patterns in the reflection coefficient, producing oscillatory behavior in the Casimir force as a function of separation.

The net result is:

$$F_{\text{Casimir}}^{\text{piezo}} = F_{\text{electronic}} + F_{\text{LO}} + F_{\text{TO}} + F_{\text{polariton}} + \ldots$$

Each term can be positive (repulsive) or negative (attractive), depending on frequency and material parameters.

### Born-Huang Hydrodynamics

To account for the full dynamics of phonon modes (not just dispersion relations), Le et al. employ the Born-Huang hydrodynamic model. This treats lattice vibrations as a fluid, with density $\rho$, velocity $\mathbf{u}$, and elastic stiffness tensor $C_{ijkl}$:

$$\rho \ddot{u}_i = \nabla_j (\sigma_{ij}) + f_i$$

where $\sigma_{ij} = C_{ijkl} \partial_k u_l$ is the stress tensor and $f_i$ is the electromagnetic force on the lattice from the electric field.

The coupling between phonons and photons is:

$$f_i = -e E_i$$

(effective charge on lattice interacting with electric field). This couples the hydrodynamic equations to Maxwell's equations, yielding a system of differential equations whose solutions include the phonon-polariton modes.

---

## Key Results

1. **Casimir force enhancement via LO resonance**: Near the longitudinal optical phonon frequency $\omega_{\text{LO}}$, the Casimir force is significantly enhanced (magnitude doubled or tripled compared to non-piezoelectric materials). This is because the LO resonance creates a strong polarization response, amplifying the vacuum fluctuation effects.

2. **Casimir force reversal via TO resonance**: Near the transverse optical phonon frequency $\omega_{\text{TO}}$, the Casimir force can reverse from attractive to repulsive, or exhibit sign changes as separation or temperature varies. This is a novel effect specific to piezoelectrics.

3. **Active tunability through phonon control**: By externally tuning the phonon frequencies (via strain, temperature, doping, or piezoelectric gating), the Casimir force can be actively modulated. For example, applying a strain shifts $\omega_{\text{LO}}$ and $\omega_{\text{TO}}$, which changes the Casimir force magnitude by ~10-50%.

4. **Temperature-dependent switching**: The Casimir force in piezoelectrics exhibits temperature dependence distinct from non-piezoelectric materials. At low T, electronic contributions dominate; at high T, thermal phonon contributions become important, allowing temperature-controlled switching between attractive and repulsive regimes.

5. **Finite-thickness effects**: For thin piezoelectric films (thickness comparable to or smaller than the separation $d$), unusual quantum-thermal effects emerge. The hybrid nature of phonon polaritons in confined geometry leads to additional resonances not present in bulk materials.

6. **Polytype-dependent Casimir signatures**: Different crystal structures (polytypes) of SiC and other piezoelectrics have different phonon frequencies due to stacking variations. The Casimir force exhibits polytype-specific signatures, making it a sensitive probe of crystal structure.

7. **Precision measurement platform**: The enhancement of the Casimir force near resonances allows for more sensitive measurements. Casimir force sensors based on piezoelectric materials could achieve better sensitivity than conventional metallic systems.

---

## Impact and Legacy

This 2024 paper opens new directions in quantum engineering and materials science:

1. **Quantum vacuum engineering**: For the first time, the Casimir effect—a purely quantum vacuum phenomenon—can be actively controlled via phonons, a classical degree of freedom. This bridges quantum and classical physics.

2. **Quantum devices**: The controllable Casimir force could be used for friction-free bearings, quantum switches (toggling repulsive-to-attractive), or actuation in nanodevices—all based on quantum vacuum effects.

3. **Fundamental physics tests**: Anomalies in the Casimir force (deviations from Lifshitz theory) have been reported but are still unexplained. Piezoelectric systems provide new geometries for testing these anomalies and potentially discovering new physics beyond QED.

4. **Materials design**: The paper demonstrates a paradigm for engineering materials to control quantum vacuum forces. By choosing materials with specific phonon frequencies, one could design Casimir forces "to order."

5. **Connections to quantum field theory**: The phonon-polariton-mediated Casimir force illustrates how macroscopic condensed matter properties (phonons) couple directly to quantum vacuum fluctuations. This is a concrete realization of how emergent phenomena (phonons) couple to fundamental quantum fields.

6. **Metamaterial design**: Phononic and photonic metamaterials could be engineered to have phonon frequencies and couplings optimized for Casimir force control—opening a new subfield of "Casimir metamaterials."

---

## Connection to Phonon-Exflation Framework

**Relevance: QUANTUM VACUUM MEDIATION OF COMPACTIFICATION DYNAMICS**

Le et al.'s work on phonon-assisted Casimir forces provides crucial insights into how quantum vacuum effects can mediate compactification geometry in phonon-exflation:

1. **Quantum vacuum as a dynamical substrate**: The Casimir effect shows that quantum vacuum fluctuations are not passive—they exert real forces on material boundaries. In phonon-exflation, the 4D-5D boundary (the compactification interface between M4 and K_7) is subject to "Casimir-like" quantum vacuum stresses that can influence geometric evolution.

2. **Phonon-mediated vacuum energy**: Le et al. show that phonon resonances dramatically enhance or suppress Casimir forces. Analogously, in the framework, the K_7 phonon spectrum (determined by the compactification metric $\tau$) should mediate the vacuum energy density. The spectral action $S_{\text{spec}}[\tau]$ (which sums over all Dirac eigenvalues) is the analogous "effective force" arising from quantum vacuum fluctuations at the compactification scale.

3. **Tunability of geometric forces**: Just as strain and temperature tune Casimir forces via phonons, the compactification metric $\tau$ tunes the spectral action and hence the "geometric forces" driving evolution. Sessions 36-38 explored how $\tau$ evolution changes the BCS gap, instability landscape, and particle production—analogous to tuning Casimir forces by varying material parameters.

4. **Active control via order parameter**: Piezoelectric materials couple electric fields to lattice strain. In the framework, the K_7 order parameter (the BCS gap $\Delta(\tau)$) couples the compactification metric to fermionic dynamics. This is a "geometric piezoelectric effect"—the order parameter mediates phonon-geometric coupling, just as piezoelectric coupling mediates photon-phonon coupling.

5. **Resonance enhancement and instability**: Le et al. show enhanced Casimir effects near phonon resonances. In phonon-exflation, resonances in the K_7 compactification (where two eigenvalues of the Dirac spectrum become degenerate) should enhance geometric instabilities and accelerate the transit. Session 22 found several such resonances (Trap 3, exceptional points) where the geometric dynamics become singular.

6. **Polariton-like hybrid modes in geometry**: Phonon polaritons are hybrid photon-phonon excitations. In the framework, the hybrid modes are SM particles themselves—fermionic excitations (electrons, quarks) that are simultaneously:
   - Excitations of the K_7 lattice (phonons in the pairing channel)
   - Excitations of the 4D spacetime (Standard Model particles)

This particle-phonon duality is the central mechanism of the framework, directly parallel to photon-phonon duality in Le et al.'s work.

7. **Quantum vacuum and compactification stability**: The Casimir force can be repulsive (pushing plates apart) or attractive (pulling them together). In the framework, quantum vacuum effects should contribute to either stabilizing or destabilizing the compactification radius. If repulsive Casimir-like forces dominate, they could resist compactification and favor large extra dimensions. If attractive, they favor small compact dimensions. The observed small compactification radius suggests that attractive "Casimir-like" forces win out—a prediction of phonon-exflation that could be tested numerically.

8. **Temperature and cosmological evolution**: Le et al. show temperature-dependent Casimir effects. In phonon-exflation, the compactification temperature (related to the BCS energy scale or instanton gas thermal properties, Sessions 37-38) should similarly affect the vacuum energy density and geometric evolution. Early universe (hot compactification) should have different vacuum properties than late time (cold), affecting inflation and dark energy.

**Specific prediction**: The phonon-assisted Casimir force formula:

$$F_{\text{Casimir}} \propto \left| \frac{\partial \epsilon(\omega)}{\partial \omega} \bigg|_{\omega_{\text{phonon}}} \right|$$

(force enhanced near phonon resonances) suggests that in the framework, the geometric force should be enhanced near resonances in the Dirac spectrum. Sessions 22-24 found that the spectral action gradient $\nabla_\tau S_{\text{spec}}$ has singularities (where it diverges) at special points $\tau_*$ in the compactification parameter space. Near these singularities, the geometric evolution should be accelerated—analogous to enhanced Casimir forces near phonon resonances. This could explain why the transit in Sessions 37-38 exhibits sudden jumps at certain $\tau$ values (the unstable crossings at high coupling).

