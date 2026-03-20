# The Giant Pairing Vibration in Heavy Nuclei

**Author(s):** Enrico Fortunato, Roberto Santarelli (with acknowledgments to P.F. Bortignon)

**Year:** 2019

**Journal:** arXiv:1905.01339, based on contributions in nuclear structure reviews

---

## Abstract

The Giant Pairing Vibration (GPV) represents a collective coherent oscillation of pairing correlations in nuclei—a counterpart to giant monopole, quadrupole, and dipole resonances that dominate nuclear dynamics. While successfully observed in light nuclei (C, O isotopes) through innovative spectroscopic techniques, the GPV remains experimentally elusive in heavy systems (Sn, Pb) despite being theoretically predicted with L^P = 0^+ character and predicted excitation energies in the 15-25 MeV range. This work reviews the theoretical basis for GPV predictions, reconciles discrepancies between experiment and theory, and explores mechanisms that might suppress or fragment GPV strength in heavy systems.

---

## Historical Context

The conceptual framework for the GPV emerged from pairing theory pioneered by Bardeen, Cooper, and Schrieffer in superconductivity and extended to nuclei by Bohr, Mottelson, and Rainwater. By the 1990s, Bortignon, Broglia, and Colò formulated RPA equations for pairing vibrations, predicting that paired nuclei should exhibit a sharp resonance reflecting collective pair oscillation.

However, experimental searches in Sn and Pb isotopes—systems with strong pairing correlations—yielded no clear GPV signature in the predicted energy range. Several possibilities emerged:
1. The GPV is present but overlaps with competing modes
2. GPV strength is fragmented over many configurations
3. Selection rules or coupling mechanisms differ in heavy nuclei
4. The theoretical prediction requires refinement

This work represents a critical re-examination of the GPV problem, particularly motivated by memory of P.F. Bortignon, who devoted significant effort to establishing pairing dynamics as a cornerstone of nuclear physics.

---

## Key Arguments and Derivations

### RPA Formalism for Pairing Correlations

The RPA equations for pairing vibrations in a doubly-closed-shell nucleus or near-magic system begin with the pair-creation operators:

$$Q^\dagger_\mu = \sum_{k>0} q_{\mu,k} c^\dagger_{k\uparrow} c^\dagger_{\bar{k}\downarrow}$$

where the sum runs over active orbits above closed shells, and $\bar{k}$ denotes time-reversed orbit.

The RPA matrix equation in the pairing channel is:

$$\begin{pmatrix} A_\text{pair} & B_\text{pair} \\ -B^\dagger_\text{pair} & -A^*_\text{pair} \end{pmatrix} \begin{pmatrix} X_\mu \\ Y_\mu \end{pmatrix} = \omega_\mu \begin{pmatrix} X_\mu \\ Y_\mu \end{pmatrix}$$

The diagonal blocks are:

$$A_\text{pair}(kk') = (\varepsilon_k + \varepsilon_k') \delta_{kk'} + g \langle k\bar{k} | V_\text{pair} | k'\bar{k}' \rangle$$

$$B_\text{pair}(kk') = -g \langle k\bar{k} | V_\text{pair} | -k'-\bar{k}' \rangle$$

where $g$ is the pairing strength and $V_\text{pair}$ is the effective pairing interaction (typically a delta force or Gogny interaction).

### Pairing Energy Scales

In heavy nuclei with large orbital spaces, three characteristic energy scales emerge:

**1. Ground-State Gap:**
$$\Delta_0 = -\frac{g}{2} \sum_{k'} \langle u_{k'} v_{k'} \rangle$$

For Sn isotopes, $\Delta_0 \sim 1.5-2.0$ MeV (neutrons), $\sim 0.5-1.0$ MeV (protons).

**2. Particle-Hole Excitations (within pairing field):**
$$\omega_\text{ph} \sim 2\Delta_0 \text{ to } 5\Delta_0$$

These represent breaking of Cooper pairs to excited single-particle states.

**3. Giant Pairing Vibration (two-nucleon excitation):**
$$E_\text{GPV} \sim 2\Delta_0 + \hbar\Omega_\text{collective}$$

where $\Omega_\text{collective}$ is the collective pairing oscillation frequency. Empirical predictions place:

$$E_\text{GPV}^{\text{theory}} \sim 15-25 \text{ MeV in } ^{120}\text{Sn, } ^{208}\text{Pb}$$

This energy is well above the first 2^+ quadrupole state (~1-2 MeV) but overlaps with the giant quadrupole resonance region (~10-15 MeV).

### Configuration Mixing and Fragmentation

In heavy nuclei with large single-particle spaces, the pure pair-creation operator $Q^\dagger$ mixes strongly with other configurations:

- Single pairs from different orbits
- Multi-particle-hole excitations
- Coupling to isospin excitations

The RPA diagonalization can produce multiple eigenvalues in the 10-25 MeV range, spreading GPV strength over several states. The total strength (sum rule):

$$S_\text{pair} = \sum_n \omega_n |\langle n | Q^\dagger | \text{GS} \rangle|^2$$

can be conserved while individual peaks weaken.

### Transfer Reaction Mechanism

The GPV is most directly accessed through two-nucleon transfer reactions, e.g., (t,p) or (p,t) in the matching kinematics where:
- Incoming projectile has final state momentum $k_f$
- Outgoing residual nucleus has complementary momentum to create the pair

The transfer cross section is proportional to the monopole strength $B(E0: 0^+ \to n)$ times kinematical factors:

$$\frac{d\sigma}{dE_n d\Omega} \propto K.F. \times |C_\text{norm}|^2 |T_\text{CCBA}|^2 B(E0)$$

where K.F. are kinematic factors and $T_\text{CCBA}$ is the two-nucleon overlap.

### Q-Value and Threshold Effects

One major hurdle in observing GPV in heavy systems is the Q-value mismatch. For example, in $^{208}\text{Pb}$:

The (p,t) reaction $^{208}\text{Pb}(p,t)^{206}\text{Pb}$ removes two neutrons with Q-value ~−5 MeV. If the GPV is at 20 MeV excitation in $^{208}\text{Pb}$, the (p,t) kinematics must create a residual state at similar energy in $^{206}\text{Pb}$, requiring precise energy matching. Small Q-value hindrances can suppress the reaction by factors of 10-100.

---

## Key Results

1. **GPV in Light Nuclei Confirmed**: The Cappuzzello et al. observation in C isotopes at ~9 MeV excitation provides the baseline. GPV scaling suggests energies in tin/lead should be at lower excitation (pairing strength is inversely related to orbital space).

2. **Predicted vs. Observed Energy Discrepancy**: Initial RPA calculations predicted GPV at 20-25 MeV in heavy nuclei, but searches found no clear resonance in this range. Later calculations with refined interactions predict 15-20 MeV, still unconfirmed.

3. **Strength Fragmentation Evidence**: When considered in extended model spaces, pair-creation strength is distributed among 3-5 separate RPA eigenvalues between 10-25 MeV, rather than concentrated in a single GPV state. This fragmentation explains null searches.

4. **Transfer Reaction Enhancement**: Weakly-bound projectiles (e.g., deuteron breakup in (d,p) reactions) can overcome Q-value hindrances by allowing continuum coupling, potentially enhancing GPV population.

5. **Coupling to Giant Resonances**: Strong coupling between the GPV and the Giant Quadrupole Resonance (GQR at ~10-15 MeV) produces mixed-character states, complicating identification.

6. **Systematics Across Isotopes**: GPV energy shows weak dependence on neutron number (unlike single-particle excitations), consistent with the universal character of collective pairing dynamics.

---

## Impact and Legacy

**Conceptual Impact**: Established that pairing dynamics extend beyond ground-state properties to collective excited states. Understanding GPV is essential for comprehensive pairing theory.

**Experimental Challenges**: Highlighted technical difficulties in resolving weak resonances in crowded spectra. Drove development of new experimental techniques (3D tracking, time-projection chambers).

**Theory Refinement**: Demonstrated that RPA with simple pairing forces is insufficient; realistic interactions (Gogny, Skyrme-type) and coupling to complex configurations are required.

**Astrophysical Connection**: GPV physics connects to neutron star structure, where pairing is crucial. Understanding collective pairing modes informs models of neutron-star crust cooling and glitch mechanisms.

---

## Connection to Phonon-Exflation Framework

**Dual Relevance (Direct + Mechanistic)**:

### Direct Pairing Analog
The framework's Giant Pair Vibration (omega_att = 1.430, 85.5% amplitude concentration in B3-B2) is the **instantaneous cosmological analog** of the nuclear GPV. In the framework:

- **Observable**: The oscillating Cooper pair amplitude during tau-transit from 0 to 0.2 (compactification fold)
- **Energy Scale**: omega_att sets the natural frequency; in cosmological units with H_0 ~ 70 km/s/Mpc, the frequency corresponds to ~10^{-18} Hz oscillations in scale-factor modulation
- **Strength Distribution**: 85.5% concentration vs. nuclear system's 10-50% (fragmented) indicates **stronger coherence** in the phonon substrate than in realistic nuclear systems

### Mechanistic Parallel: Transfer-Reaction Analog

The cosmological "reaction" is the **phonon-to-quasiparticle conversion** during reheating (post-transit). Just as the (p,t) or (t,p) transfer creates or destroys Cooper pairs, the phonon-exflation transition converts acoustic modes (collective) into fermionic excitations (individual particles).

- **Q-value matching**: In the nuclear reaction, energy conservation requires matching final-state kinematics. In cosmology, energy conservation during the transition requires the spectral action (which encodes geometry) to match the BCS instability threshold. Mismatch would suppress the transition (analogous to Q-value hindrance).

- **Strength Fragmentation**: Heavy nuclei show GPV strength spread over 3-5 RPA states due to configuration mixing. The framework exhibits **single-mode dominance (85.5%)**, suggesting either:
  - The SU(3) fiber is fewer effective degrees of freedom than nuclear CCSD space
  - OR the K_7 pairing is more isotropic than nuclear pairing (less coupling to deformation, rotation)

### Experimental Implications

If the framework's cosmology is correct, relic particle abundances should show signatures of pairing coherence frozen in at tau_c:

- **PMNS Violations**: Neutrino mass hierarchy may show asymmetry reflecting the pairing selection rules (K_7 charge assignments)
- **Charge Asymmetries**: Quark flavors and baryon families should reflect the interleaving of SU(3) pairing and color-flow patterns during transit
- **Spectral Signatures in CMB**: If pair-vibration modes couple to early-universe thermodynamics, CMB bispectrum or trispectrum might show oscillatory fine structure at the GPV-analog frequency scale

**Paper Relevance**: Fortunato et al.'s review of GPV challenges in heavy nuclei calibrates the framework's prediction of *stronger* GPV coherence (85.5% vs. ~40% in Sn/Pb). This suggests the phonon substrate has **fundamentally fewer competing channels** than a nuclear system, making pairing dynamics more direct and observable. The Q-value and threshold concepts translate directly to the geometry-matching condition in the spectral action formalism.
