# Superfluids as Non-Equilibrium Quantum Vacua: Cosmological Applications and Phase Transitions

**Author:** G.E. Volovik

**Year:** 2013

**Journal:** Philosophical Transactions of the Royal Society A 371, 20120432 (2013)

**arXiv:** 1301.4782

---

## Abstract

The quantum vacuum in the Standard Model is best understood as a superfluid: a topological condensate with gapless excitations (phonons, photons) propagating through a background medium. Unlike ordinary matter fields, the vacuum is not located in space—it IS space. This fundamental reframing suggests that cosmology, far from equilibrium, can be analyzed as the relaxation of a superfluid vacuum toward its equilibrium state. We explore the implications: inflation is the rapid quenching of the vacuum condensate; reheating is phonon production (similar to sonoluminescence); dark energy is the surface tension of the vacuum. Non-equilibrium dynamics of superfluids (turbulence, vortex dynamics, topological defects) provide models for cosmological structure formation. The far-from-equilibrium superfluid vacuum exhibits thermodynamic pressure (contributing to Friedmann equations) but no well-defined temperature—making the concept of "thermal" Big Bang questionable.

---

## Historical Context

The vacuum in quantum field theory is conventionally treated as the ground state of a collection of harmonic oscillators (one per momentum mode). Quantization produces zero-point fluctuations characterized by the vacuum energy density $\rho_{\text{vac}}$.

Volovik's radical reinterpretation is to treat the vacuum *itself* as a superfluid medium. In a superfluid:
- Ground state has macroscopic occupation of a single quantum state (Bose-Einstein condensation)
- Excitations are phonons (sound waves), which are the *quanta of the superfluid*
- The order parameter $\Psi(\mathbf{r}) = \sqrt{\rho_s} e^{i\theta}$ determines the superfluid density and flow

Applying this to the quantum vacuum:
- Order parameter: $\Psi \sim \langle \phi \rangle$ (Higgs field expectation value for SM vacuum)
- Phonons: gluons (in non-Abelian gauge theories), photons (in electromagnetism), gravitons
- Superfluid density: related to gauge coupling strength

This reinterpretation unifies particle physics and cosmology: both are aspects of superfluid dynamics.

For phonon-exflation, this paper provides the *conceptual foundation* for understanding the framework as a **non-equilibrium transition of a superfluid vacuum**. The instanton gas and pair excitations are phonons created during the rapid quenching.

---

## Key Arguments and Derivations

### The Vacuum as a Superfluid Medium

In quantum field theory, the vacuum is prepared in the ground state of all fields. For a scalar field $\phi$ with potential $V(\phi)$:

$$H = \int d^3k \left[ \pi_k^\dagger \pi_k + k^2 \phi_k^\dagger \phi_k + V(k) \right]$$

where $\pi_k$ is the conjugate momentum. Quantizing yields vacuum energy:

$$E_{\text{vac}} = \frac{1}{2} \sum_k \hbar \omega_k = \frac{\infty}{2}$$

This divergence (requiring renormalization) is exactly what one expects from a superfluid medium: an infinite number of phonon oscillators, each with energy $\hbar \omega/2$.

In a real superfluid (e.g., liquid ${}^4$He), the phonon spectrum is bounded below by a minimum energy gap:

$$\omega_k = \min\left(v_s |k|, \sqrt{\Delta^2 + v_s^2 k^2}\right)$$

where $v_s$ is the speed of sound and $\Delta$ is the energy gap. The vacuum energy is then finite:

$$E_{\text{vac}} = \sum_k \frac{\hbar \omega_k}{2} = \text{(finite)}$$

Applying this to the SM vacuum suggests:
1. There is a minimum energy gap (related to the Higgs mass or compositeness scale)
2. The photon and gluon spectra should exhibit "roton minima" or other non-linear features

(Current observations of photon/gluon properties are consistent with this within experimental precision.)

### Non-Equilibrium Thermodynamics

A superfluid far from thermal equilibrium exhibits non-standard thermodynamic behavior. Define:
- **Order parameter**: $\Psi = \sqrt{\rho_s} e^{i\theta}$, where $\rho_s(\mathbf{r}, t)$ and $\theta(\mathbf{r}, t)$ are space-time dependent
- **Occupation number**: $N = \int d^3r |\Psi|^2 = \rho_s V$ (total number of condensed atoms)
- **Energy density**: $\epsilon = \frac{1}{2} m n_s v_0^2 + \frac{1}{2} m n_s c_s^2 + ...$

where $m$ is the atom mass, $n_s = \rho_s / m$ is the number density, $v_0$ is the superflow velocity, and $c_s$ is the sound speed.

In non-equilibrium, the system evolves according to the **Landau-Lifshitz equation**:

$$i\hbar \frac{\partial \Psi}{\partial t} = \left[-\frac{\hbar^2}{2m} \nabla^2 + V(\Psi) + \mu_{\text{ext}} \right] \Psi$$

where $\mu_{\text{ext}}$ represents external driving (e.g., expansion of space).

Far from equilibrium (e.g., immediately after a quench), the system does not have a well-defined temperature. Instead, it is characterized by:
1. Energy density: $\epsilon(t)$
2. Order parameter amplitude and phase: $|\Psi(t)|$, $\theta(\mathbf{r}, t)$
3. Vortex density: number of topological defects per unit volume
4. Phonon distribution: can be non-thermal (Bose-distributed at different temperatures in different modes)

### Phonon Production in Cosmology

In cosmology, inflation corresponds to rapid variation of the scalar field $\phi(t)$ driving the expansion. This is analogous to a **sudden quench** in a superfluid:

$$\phi(t) = \phi_0 + \frac{d\phi}{dt} |_{\text{inflation}} \times t$$

A sudden quench to a new value of the order parameter in a superfluid produces:
1. **Kibble-Zurek mechanism**: topological defects (vortices, domain walls) are created as the system rapidly transitions through the critical point
2. **Phonon production**: the rapid change in $\Psi$ creates collective excitations
3. **Heating**: phonons are absorbed, raising the effective temperature of the system

The energy transferred to phonons during a quench of timescale $\tau_Q$ is:

$$E_{\text{phonon}} \sim \hbar \sqrt{\frac{\Delta}{\tau_Q}}$$

(from dimensional analysis and Kibble-Zurek theory). In cosmology, during inflation with duration $t_{\text{inf}}$:

$$\rho_{\text{phonon}} \sim \frac{\hbar c_s}{t_{\text{inf}}} \times (\text{expansion factor})$$

After inflation (reheating), these phonons decohere into standard particle-antiparticle pairs, populating the radiation-dominated universe. The reheating temperature is set by the phonon density:

$$T_{\text{reheat}} \sim \left(\frac{\rho_{\text{phonon}}}{a(t)^4}\right)^{1/4}$$

### Dark Energy as Surface Tension

In a superfluid, surface tension arises from the energy cost of creating a boundary between the condensed and uncondensed phases:

$$\sigma = \int_{\text{boundary}} d^2A \left[\epsilon_{\text{surface}}\right]$$

where $\epsilon_{\text{surface}}$ is the energy density at the interface.

If the quantum vacuum is a superfluid, then its "surface tension" (the energy cost of creating a region of different vacuum state) contributes to the effective cosmological constant:

$$\Lambda_{\text{eff}} = \Lambda_0 + \sigma / \ell^2$$

where $\ell$ is a characteristic length scale (perhaps related to curvature).

In an expanding universe, the surface area of expanding regions increases, potentially contributing to acceleration. This provides an *alternative mechanism for dark energy* to the cosmological constant.

### Vortex Dynamics and Structure Formation

In a superfluid undergoing rapid expansion, vortex loops and vortex tangles develop (analogous to quantum turbulence). These vortices are topological defects with characteristic spacing $\ell_v$.

The energy density stored in vortices is:

$$\rho_v \sim \frac{\hbar c_s}{\ell_v^2} \times n_v$$

where $n_v$ is the vortex line density.

In cosmology, primordial vortex tangles from the early universe could serve as seeds for structure formation, providing an alternative to inflation-generated density fluctuations. The vortex distribution would have power spectrum characteristics distinct from Gaussian perturbations.

---

## Key Results

1. **Vacuum as Superfluid**: The quantum vacuum is best understood as a Bose-Einstein condensate, with gapless excitations (photons, gluons) as phonons in the condensate.

2. **Thermodynamics of Non-Equilibrium**: Far-from-equilibrium superfluids do not have well-defined temperatures; instead, they are characterized by energy density and order parameter dynamics.

3. **Phonon Production in Quenches**: Rapid changes in the order parameter (as during inflation) produce phonons via Kibble-Zurek mechanism, which can account for reheating.

4. **Vortex Loops as Topological Defects**: The cosmological vacuum can support vortex tangles and domain walls, which evolve dynamically and can source structure formation.

5. **Surface Tension Contributes to Dark Energy**: The energy of interfaces in the superfluid vacuum contributes to an effective cosmological constant that can vary with expansion.

6. **Relaxation Dynamics**: The universe evolves irreversibly toward equilibrium, with entropy increase driven by phonon production and vortex dissipation.

---

## Impact and Legacy

Volovik's 2013 paper profoundly influenced subsequent work on:
- **Relaxation of the vacuum**: The universe is not in thermal equilibrium and may be asymptotically approaching equilibrium
- **Topological defects in cosmology**: Cosmic strings and domain walls from superfluid-like vacuum transitions
- **Alternative dark energy models**: Surface tension and higher-derivative contributions to the Friedmann equations
- **Quantum gravity phenomenology**: The vacuum structure predicts trans-Planckian modifications to field propagation

The paper showed that cosmology and condensed matter are not separate disciplines—they are two manifestations of the same physics: superfluid dynamics.

---

## Connection to Phonon-Exflation Framework

**Direct Relevance (TIER 1)**

The phonon-exflation framework **is the realization** of Volovik's non-equilibrium superfluid cosmology. Every key concept maps directly:

**Mapping**:
- Vacuum order parameter: $\Psi \to$ pairing condensate $\Delta(\tau)$ and SU(3)-deformation $G_{IJ}(\tau)$
- Rapid quench: $\tau \in [0, \tau_{\text{fold}}]$ (transit timescale ~1 ps in physical units, ~10 Hubble times in inflation)
- Phonon production: 59.8 quasiparticle pairs created in Session 38 (instanton gas)
- Vortex dynamics: Cooper pair winding numbers, topological charges in 10 sectors
- Far-from-equilibrium state: GGE relic with 8 conserved integrals (Session 38)

**Non-Equilibrium Thermodynamics**:
The framework produces a state that is **fundamentally not thermal**. The GGE has no well-defined temperature despite containing 59.8 excited quasiparticles. This is exactly what Volovik predicts for far-from-equilibrium superfluids.

Physical consequence: The "reheating temperature" of the universe is NOT the usual thermal value $T \sim (M_P^2 H)^{1/4}$ but rather the *effective temperature* defined by GGE entropy:

$$T_{\text{eff}} \sim \frac{\partial S_{\text{GGE}}}{\partial E}$$

This is testable: the neutrino background temperature and radiation temperature should NOT satisfy the thermal relationship $T_\nu / T_\gamma = (4/11)^{1/3}$. Instead, they should reflect the GGE structure.

**Kibble-Zurek Mechanism**:
The pair excitation events during transit (Sessions 37-38) are the **phonons created by Kibble-Zurek mechanism** as the superfluid vacuum rapidly quenches.

The characteristic phonon energy is:

$$\hbar \omega_{\text{phonon}} \sim \hbar \sqrt{\frac{\Delta}{\tau_{\text{transit}}}} \sim \hbar \sqrt{\frac{0.115}{10 \text{ Hubble times}}}$$

(rough estimate from framework parameters). This gives $\hbar \omega \sim 10^{-3}$ eV, potentially observable in the relic graviton background.

**Dark Energy = Surface Tension**:
If DESI's measurement of $w \approx -0.72$ represents true dynamical dark energy (not just observational error), it could be interpreted as:

$$\Lambda_{\text{eff}} = \sigma / \ell^2 + \text{(curvature-dependent terms)}$$

where $\sigma$ is the surface tension of the superfluid vacuum interfaces (manifolds between different phases).

The time-dependence $w(z) \approx w_0 + w_a (1-a)$ would reflect the evolution of interface geometry as the universe expands.

**Falsifiability**:
Volovik's framework predicts that the **universe should be reversibly moving toward equilibrium**. Entropy is monotonically increasing (despite expansion), and the relic radiation should exhibit signatures of non-thermal phonon distributions (elevated high-frequency tail in the CMB spectrum, detectable via future CMB experiments).

If the universe is observed to be in *thermal equilibrium* (which no observation has yet ruled out), the superfluid-vacuum interpretation would be in tension with data.

