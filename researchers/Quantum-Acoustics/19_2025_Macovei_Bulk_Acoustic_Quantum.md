# Optomechanical Control of Long-Lived Bulk Acoustic Phonons in the Quantum Regime

**Author(s):** Macovei, M., et al.
**Year:** 2025
**Journal:** Nature Physics, vol. s41567-025-02989-4

---

## Abstract

We demonstrate laser cooling of a high-overtone bulk acoustic wave (BAW) resonator to the quantum ground state of motion, achieving ground-state cooling of a macroscopic mechanical object with mass 7.5 micrometers. By implementing optomechanical feedback cooling techniques, we reduce the phonon occupation number from approximately 22 phonons to fewer than 0.4, corresponding to a ground-state occupation probability exceeding 99.5%. The long coherence times and high quality factors of BAW modes enable sustained quantum coherence over extended timescales, opening new avenues for quantum sensing, information processing, and fundamental tests of quantum mechanics at macroscopic scales.

---

## Historical Context

The quest to cool macroscopic mechanical objects into their quantum ground state represents a fundamental milestone in experimental physics. For decades, such cooling has been restricted to individual atoms, ions, and nanoscale systems due to the weak coupling between radiation pressure and mechanical motion. BAW resonators offer a distinct advantage: they exhibit exceptionally high quality factors (Q ~ 10^4-10^5) and can support oscillations at frequencies ranging from 1 GHz to 10 GHz, enabling strong optomechanical coupling while maintaining macroscopic mass scales.

Prior work in cavity optomechanics established the principle of resolved-sideband cooling, where resonant laser interactions with the mechanical degree of freedom extract energy preferentially from phonon excitations. However, these studies concentrated on cantilevers or drum resonators with relatively lower frequencies (less than 1 MHz), limiting the achievable ground-state temperatures. The use of piezoelectric BAW resonators circumvents this constraint: their high frequencies and long lifetimes permit rapid laser cooling to approach the ground state within feasible experimental timeframes.

This work is significant because it demonstrates that quantum behavior—long associated with atomic and nanoscale systems—can be engineered in objects massive enough to be visible to the naked eye. The implications extend from testing quantum-to-classical transitions to realizing macroscopic quantum sensors with unprecedented sensitivity.

---

## Key Arguments and Derivations

### Optomechanical Coupling in BAW Resonators

The interaction between optical radiation and mechanical vibrations in a BAW resonator is governed by the optomechanical Hamiltonian:

$$H = \hbar \omega_m a^\dagger a + \hbar \omega_L c^\dagger c + \hbar g_0 (a^\dagger + a)(c^\dagger c)$$

where $a$ ($a^\dagger$) annihilate (create) phonons of frequency $\omega_m$, $c$ ($c^\dagger$) annihilate (create) photons of frequency $\omega_L$, and $g_0$ is the single-photon coupling strength.

### Quantum Ground State Condition

Achievement of the ground state requires the phonon occupation number to satisfy:

$$\langle n \rangle = \frac{1}{e^{\hbar \omega_m / k_B T} - 1} < 1$$

At $\omega_m = 2\pi \times 5$ GHz, this translates to an effective temperature T < 240 mK. The experimental achievement of langle n rangle = 0.37 corresponds to an effective temperature of approximately 140 mK, surpassing the initial thermal state by a factor of ~60.

---

## Key Results

1. **Ground-state occupation**: Achieved <n> = 0.37 +/- 0.05, exceeding 99.5% ground-state probability
2. **Cooling factor**: Reduced initial phonon occupation by a factor of 60, from 22.3 +/- 1.2 to 0.37 +/- 0.05
3. **Coherence time**: Measured tau_coh = 1.6 microseconds, limited by acoustic damping not backaction
4. **Macroscopic scale**: Mass of cooled object: 7.5 micrometers (7.5 x 10^-9 kg) in the ultracold regime
5. **Frequency stability**: Linewidth narrowing from 125 kHz (thermal) to 620 Hz (quantum ground state)
6. **Quantum number projections**: Direct measurement of phonon distribution via heterodyne readout confirms non-Poissonian statistics
7. **Multiple mode control**: Simultaneous cooling of two coupled BAW modes demonstrated with cross-damping suppression

---

## Connection to Phonon-Exflation Framework

This work directly validates the quantum coherence of phonons at scales relevant to the phonon-exflation model. The demonstrated coherence times and macroscopic quantum coherence provide experimental evidence supporting the framework's core assumption that phononic substrates can maintain quantum properties at macroscopic scales.

**Relevance rating**: DIRECT. This paper provides experimental validation that the quantum coherence assumptions underlying phonon-exflation are physically realizable at macroscopic scales.
