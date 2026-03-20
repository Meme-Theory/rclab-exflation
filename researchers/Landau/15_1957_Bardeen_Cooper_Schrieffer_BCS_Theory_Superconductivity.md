# Theory of Superconductivity

**Author(s):** John Bardeen, Leon N. Cooper, J. Robert Schrieffer

**Year:** 1957

**Journal:** Physical Review, Vol. 108, pp. 1175–1204

---

## Abstract

A theory of superconductivity is presented based upon the existence of an energy gap in the spectrum of elementary excitations. Electrons are treated as scattering via an attractive phonon-mediated interaction, leading to a ground state with a condensate of correlated electron pairs. The BCS ground state is shown to be a coherent superposition of terms with different particle numbers, stabilized by the pairing energy. Elementary excitations are quasi-particle excitations (with broken Cooper pairs) whose spectrum possesses an energy gap Delta at the Fermi surface. The theory reproduces the Meissner effect, critical field, specific heat, and electromagnetic response of superconductors.

---

## Historical Context

Prior to 1957, superconductivity remained one of the most mysterious phenomena in condensed matter physics. The Meissner effect (expulsion of magnetic field from a superconductor) had been established in 1933, but the microscopic mechanism was unknown. BCS proposed a revolutionary answer: electrons near the Fermi surface attract each other through phonon exchange, forming a quantum collective state of paired electrons.

Cooper had shown in 1956 that even a weak attractive interaction can bind a pair of electrons into a bound state near the Fermi surface—the Cooper pair. Bardeen, Cooper, and Schrieffer extended this observation to a macroscopic system, discovering that the ground state contains a condensate of all such pairs with a common phase. This order parameter Delta distinguishes the normal metal from the superconducting state.

The BCS theory unified superconductivity with the Landau-Ginzburg phenomenology (developed in 1950) by providing a microscopic derivation. It explained the critical temperature in terms of the electron-phonon coupling constant, predicted new phenomena (gap anisotropy, ultrasonic attenuation), and established the paradigm that dominated condensed matter physics for decades.

The BCS framework remains foundational: from nuclear pairing to cold atoms to color superconductivity in QCD. It is the prototype for spontaneous symmetry breaking via fermion condensation in quantum field theory.

---

## Key Arguments and Derivations

### The Pairing Hamiltonian

The BCS model begins with a system of electrons near the Fermi surface interacting via an attractive potential $V(k,k')$:

$$H = \sum_k \epsilon_k c_{k\uparrow}^\dagger c_{k\uparrow} + \epsilon_k c_{k\downarrow}^\dagger c_{k\downarrow} - \sum_{k,k'} V(k,k') c_{k\uparrow}^\dagger c_{k'\uparrow}^\dagger c_{k'\downarrow} c_{k\downarrow}$$

Here $\epsilon_k = k^2/(2m) - \mu$ is the single-particle energy relative to the chemical potential $\mu$. The interaction is restricted to a narrow shell of thickness $\hbar \omega_D$ around the Fermi surface, where $\omega_D$ is the Debye cutoff.

For a constant coupling, $V(k,k') = -V$ if both $k$ and $k'$ lie within the Debye shell, and zero otherwise. This simplification captures the essence of the attractive interaction.

### The BCS Ground State

Bardeen, Cooper, and Schrieffer proposed an ansatz for the ground state:

$$|\text{BCS}\rangle = \prod_k (u_k + v_k c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger) |0\rangle$$

where $u_k$ and $v_k$ are amplitudes with $|u_k|^2 + |v_k|^2 = 1$. This state represents a macroscopic coherence of Cooper pairs: each pair $(k\uparrow, -k\downarrow)$ has amplitude $v_k$ to be occupied and amplitude $u_k$ to be empty.

The variational principle determines $u_k$ and $v_k$:

$$v_k^2 = \frac{1}{2}\left(1 - \frac{\epsilon_k}{E_k}\right), \quad u_k^2 = \frac{1}{2}\left(1 + \frac{\epsilon_k}{E_k}\right)$$

where $E_k = \sqrt{\epsilon_k^2 + \Delta^2}$ is the quasi-particle energy and $\Delta$ is the superconducting gap.

### The Gap Equation

Self-consistency requires that the order parameter $\Delta$ satisfies a self-consistency equation. In the mean-field approximation:

$$\Delta = V \sum_k \langle c_{-k\downarrow} c_{k\uparrow} \rangle = V \sum_k u_k v_k$$

At zero temperature, integrating over the density of states near the Fermi surface:

$$1 = V \int_0^{\hbar\omega_D} \frac{N(E_F)}{2E} dE$$

where $N(E_F)$ is the density of states at the Fermi surface. This integral gives:

$$\Delta_0 = 2 \hbar \omega_D \exp\left(-\frac{1}{V N(E_F)}\right)$$

The exponential dependence is striking: even a weak attractive interaction ($V N(E_F) \ll 1$) produces a finite gap, explaining why superconductivity occurs in nearly all metals with some electron-phonon coupling.

### Quasi-Particle Excitations

Elementary excitations are quasi-particles created by breaking a Cooper pair:

$$\gamma_{k\uparrow}^\dagger = u_k c_{k\uparrow}^\dagger - v_k c_{-k\downarrow}$$

These quasi-particles are neither pure electrons nor holes but coherent superpositions. Their energy is:

$$E_k = \sqrt{\epsilon_k^2 + \Delta^2}$$

At the Fermi surface ($\epsilon_k = 0$), the quasi-particle energy is exactly $\Delta$, confirming that the gap is the minimum energy to create an excitation.

The density of quasi-particle states is:

$$N_\text{qp}(E) = N(E_F) \frac{|E|}{\sqrt{E^2 - \Delta^2}} \quad \text{for } |E| > \Delta$$

This density of states vanishes at $E = \Delta$ (van Hove singularity) and diverges as $E \to \Delta$ with a square-root divergence.

### Condensation Energy

The energy of the BCS ground state relative to the normal metal is:

$$E_\text{cond} = -\frac{\Delta^2}{2V N(E_F)}$$

At zero temperature, this is the binding energy of the condensate. Its magnitude sets the superconducting transition energy scale.

### Thermodynamics and Critical Field

At temperature $T < T_c$, the gap decreases with increasing $T$. The critical temperature is:

$$k_B T_c = 1.13 \hbar \omega_D \exp\left(-\frac{1}{V N(E_F)}\right)$$

This result was one of the great triumphs of BCS: it predicted the dependence of $T_c$ on the coupling constant and electron-phonon frequency.

The upper critical field $H_{c2}$ (above which superconductivity is destroyed by orbital pairing breaking) is related to the Ginzburg-Landau parameter:

$$\kappa = \lambda / \xi \approx 0.96 \lambda / v_F \sqrt{\pi V N(E_F)}$$

where $\lambda$ is the London penetration depth and $\xi$ is the coherence length.

### The Meissner Effect

In the superconducting state, the vector potential inside the superconductor decays exponentially:

$$\mathbf{A}(x) \propto e^{-x/\lambda}$$

where $\lambda = \sqrt{m/(4\pi n_e e^2)}$ is the London penetration depth. The BCS theory reproduces this result, validating the coherent pair picture.

### Specific Heat

In the superconducting state, the specific heat is dominated by quasi-particle excitations:

$$C_v(T) = C_v^\text{normal}(T) + \text{exp. suppression from gap}$$

At $T = 0$, the electronic specific heat vanishes exponentially:

$$C_v(0) \propto T \exp(-\Delta/k_B T)$$

At the transition, the specific heat jumps by a factor of approximately 1.43, in excellent agreement with experiment.

---

## Key Results

1. **Cooper instability** — Any attractive interaction in a degenerate Fermi sea leads to pairing instability; no threshold interaction strength exists.

2. **Energy gap** — The superconducting ground state possesses an energy gap $\Delta$ that vanishes as $T \to T_c$ following $\Delta(T) \sim \Delta_0 (1 - T/T_c)^{1/2}$ near $T_c$.

3. **Exponential gap dependence** — The gap at $T=0$ depends exponentially on the coupling constant: $\Delta_0 \sim \exp(-1/\lambda)$ where $\lambda = V N(E_F)$.

4. **Critical temperature formula** — $T_c \propto \omega_D \exp(-1/V N(E_F))$, in excellent agreement with empirical isotope effect data.

5. **Coherence length** — The spatial extent of a Cooper pair, $\xi = \hbar v_F / \pi \Delta$, sets the penetration depth and London equation.

6. **Zero-temperature condensation energy** — $|E_\text{cond}| = \Delta^2 / (2 V N(E_F)) \approx 1.3 N(E_F) \Delta_0^2$ per unit volume.

7. **Specific heat jump** — At $T_c$, the electronic specific heat jumps from the normal-state value by a factor of $\gamma = C_v^\text{s}(T_c^-) / C_v^\text{n}(T_c) \approx 1.43$.

8. **Electromagnetic properties** — Flux expulsion (Meissner effect) and field penetration are natural consequences of the ordered ground state.

9. **Quasi-particle density of states** — Non-zero density of states only for $|E| > \Delta$; the gap opens fully at the Fermi surface.

10. **Universality** — The BCS mechanism applies to nuclear pairing, ultra-cold atomic gases, color superconductivity, and other fermion condensation phenomena.

---

## Impact and Legacy

BCS theory revolutionized condensed matter physics and remains the foundation of all pairing phenomena. The paper has been cited over 20,000 times and won the 1972 Nobel Prize in Physics for Bardeen, Cooper, and Schrieffer.

### Immediate Developments (1958–1970)
- Bogoliubov developed the general quasiparticle formalism, showing BCS is equivalent to Hartree-Fock with pairing
- Gor'kov rederived BCS from a Green's function perspective, establishing connection to GL theory
- Nambu developed the framework of spontaneous symmetry breaking in condensed matter
- Tunneling experiments by Giaever confirmed the energy gap prediction

### Extensions and Generalizations
- BCS-BEC crossover (Leggett, 1980; Nozières-Schmitt-Rink, 1985): connects weak-coupling pairing to Bose condensation of composite fermions
- Nuclear pairing (Ring-Schuck): BCS governs deformed nuclei, explaining superfluid properties and rotational spectra
- Color superconductivity in QCD (Alford et al., 1998): three-flavor quark superconductivity at neutron star densities
- Cold atoms (Jin, Ketterle et al., 2000s): direct realization of BCS-BEC crossover in trapped Fermi gases
- High-$T_c$ superconductivity (1987-present): unconventional (non-phonon-mediated) pairing mechanisms

### Modern Applications
- Superconducting qubits and quantum circuits
- Topological superconductors and Majorana fermions
- Proximity effects and proximity-induced superconductivity in heterostructures

The BCS mechanism—fermion pairing, condensation, collective excitations—defines the language of many-body quantum physics.

---

## Framework Relevance

### Direct Mechanism
The phonon-exflation framework is fundamentally a **BCS system on the SU(3) fiber**. The key structural identifications are:

1. **Pairing interaction** — K_7 pairing in the framework corresponds to BCS attractive interaction. The interaction is mediated by internal geometry (not phonons in the external sense) but follows the identical mathematica architecture.

2. **Gap equation** — The gap Delta in the framework satisfies a self-consistency equation identical to BCS (Sessions 33–38). The condensation energy $E_\text{cond} = -0.115$ at corrected van Hove singularity is a direct output of BCS with a geometric potential.

3. **Coherence length** — BCS coherence length $\xi = \hbar v_F / \pi \Delta$ sets the typical size scale of the Cooper pair. In the framework, $L / \xi_\text{GL} = 0.031$ (Session 38): the **ultrasmall grain regime** where *all 7 physical Cooper pairs coexist in one coherence volume*. This is precisely the regime where BCS collective effects dominate and fluctuations become crucial (E_vac / E_cond ~ 29×).

4. **Quasi-particle excitations** — The 59.8 quasiparticle pairs produced in the sudden quench (S38) are directly analogous to BCS quasi-particles created by breaking Cooper pairs. The energy of excitation is O(Delta) ~ 0.137, and the density of states near threshold shows van Hove enhancement.

5. **Integrability and GGE** — The Richardson-Gaudin integrability (Papers #16–17) arises because the BCS pairing Hamiltonian is **integrable**: it possesses 8 conserved quantities (the generalized momenta and pseudo-momenta of the RG model). The post-transit relic (S38) thermalizes to the GGE (Paper #20), not the Gibbs ensemble, precisely because of this integrability.

6. **Sudden quench and Kibble-Zurek** — The transit from tau=0 to tau=0.285 is a **Kibble-Zurek quench** (Paper #21): the system evolves through a critical point with diverging correlation length, creating a cascade of defects. In the framework, the "defect" is the instanton gas and the relic GGE state. The transit timescale is ultrashort compared to the timescale for thermalization, so no equilibrium description applies.

### Quantitative Predictions Enabled by BCS
- **Pairing-induced mass gap** — Explains why the internal spectrum gap is order Delta ~ 0.137, not the bare single-particle energies
- **N_eff from pairing** — The reduced effective DOF from pairing matches why N_eff ~ 2.48 from the GGE, not 5.5 from a naive Gibbs ensemble
- **Anti-trapping mechanism** — The spectral action wrongly tries to minimize F (seeking stable V potential). BCS says: *any* pairing reduces condensation energy, but the pair-vibrational mode (omega_att) is a *collective* excitation that can fight back. The F.5 "anti-trapping" (BdG shift wrong-sign vs E_cond) is a **collective effect**, not single-particle.

### Philosophical Connection
BCS is a **spontaneous symmetry breaking** mechanism: a disordered Fermi liquid spontaneously orders into a paired condensate, lowering energy via collective binding. The phonon-exflation framework applies this principle to the **internal compactified geometry** itself: SU(3) fiber "orders" by pairing up eigenvector components (via K_7 symmetry breaking), producing a relic GGE state that never thermalizes.

**In short: Phonon-exflation IS BCS applied to SU(3) geometry during a Kibble-Zurek quench.**

---

## References

- Bardeen, J., Cooper, L. N., & Schrieffer, J. R. (1957). Theory of Superconductivity. *Physical Review*, 108(5), 1175–1204.
- Bogoliubov, N. N. (1958). On a new method in the theory of superconductivity. *Il Nuovo Cimento*, 7(6), 794–805.
- Gor'kov, L. P. (1958). On the energy spectrum of superconductors. *Soviet Physics JETP*, 7, 505–508.
- Leggett, A. J. (1980). Cooper-pair breakdown in superconductors. *Science*, 210(4467), 280–288.
- Nambu, Y. (1960). Quasi-particles and gauge invariance in the theory of superconductivity. *Physical Review*, 117(3), 648–663.
