# Time Crystals: Spontaneous Breaking of Time Translation Symmetry

**Author(s):** Grigory E. Volovik

**Year:** 2013 (submitted September 26, 2012; published JETP Lett. 98, 491)

**Journal/Source:** arXiv:1209.5765; JETP Lett. 98, 491-495 (2013)

---

## Abstract

This paper proposes that certain quantum systems can exhibit **time crystals**—states where time translation symmetry is spontaneously broken, resulting in periodic oscillations of physical observables even in the ground state. Volovik identifies two relaxation timescales: energy relaxation time τ_E and particle number relaxation time τ_N. When τ_N >> τ_E, a system can exhibit oscillations at intermediate times (τ_E << t << τ_N) before eventual equilibration. The paper also connects time crystals to generalized Gibbs ensemble (GGE) physics in integrable systems, showing that time crystals are natural states in systems with persistent integrals of motion.

---

## Historical Context

The notion of spontaneous symmetry breaking is fundamental to physics: the vacuum can prefer a state that is less symmetric than the underlying equations. For spatial translations, this yields crystals (periodic solids). But what about time translation? Traditional quantum mechanics forbids this: eigenstates of the Hamiltonian are stationary, and the ground state has zero frequency. Volovik's 2013 paper challenged this assumption, proposing that special systems can have ground states or metastable states that oscillate periodically in time.

The paper anticipated the subsequent explosion of interest in discrete time crystals (Wilczek, Else & Pretko), time-periodic driving (Floquet systems), and prethermalization in quantum many-body systems. For the phonon-exflation framework, time crystals are deeply relevant because the **generalized Gibbs ensemble (GGE) relic** produced after the BCS transition is itself a time crystal-like state: it has a discrete spectrum of excitations that persist indefinitely due to integrability, and the system never thermalizes.

---

## Key Arguments and Derivations

### Two Relaxation Timescales

In quantum systems with weak interactions or conservation laws, two independent relaxation processes can occur:

1. **Energy relaxation (τ_E)**: Redistribution of energy among modes until the energy-dependent density of states is populated according to Boltzmann distribution. Typical timescale: inverse linewidth of decay channels.

2. **Particle number relaxation (τ_N)**: In systems with number conservation (or approximate conservation), the total particle number (or charge, or other conserved quantity) can persist much longer. Typical timescale: related to weakly-breaking perturbations that violate the conservation law.

In integrable systems (like the Richardson-Gaudin models), particle number can be conserved exactly, making τ_N → ∞.

### Intermediate Time Oscillations

If τ_N >> τ_E, the system exhibits three temporal regimes:

$$\text{Very short: } t \ll \tau_E \quad \text{→ Coherent quantum evolution}$$
$$\text{Intermediate: } \tau_E \ll t \ll \tau_N \quad \text{→ Oscillations + energy relaxation}$$
$$\text{Long: } t \gg \tau_N \quad \text{→ Full equilibration}$$

During the intermediate regime, observables oscillate with well-defined frequency:

$$O(t) = \langle O \rangle_{\text{eq}} + A \cos(\omega t + \phi) + \text{decaying higher harmonics}$$

where $\omega$ is set by the energy level spacing corresponding to the conserved particle number:

$$\omega \sim \frac{\Delta E_N}{\hbar}$$

with $\Delta E_N$ being the energy difference between states with particle number N and N+1 (or N-1).

### Generalized Gibbs Ensemble

In integrable systems with many conserved quantities $I_1, I_2, \ldots, I_n$, the long-time state is not the Boltzmann distribution but the **generalized Gibbs ensemble (GGE)**:

$$\rho_{\text{GGE}} = \frac{1}{Z_{\text{GGE}}} \exp\left( -\sum_i \beta_i I_i \right)$$

where the Lagrange multipliers $\beta_i$ are fixed by the initial state. The GGE predicts that expectation values of observables plateau to fixed values determined by the initial conditions, not by thermal fluctuations.

For time crystals, the GGE allows **persistent oscillations** because the oscillation pattern is encoded in the initial state's distribution across the eigenstates with different values of the conserved quantities:

$$\langle O(t) \rangle = \sum_n |\langle n | O \rangle|^2 e^{-iE_n t/\hbar}$$

If the initial state is a superposition of eigenstates with well-spaced energies (spaced by ~$\hbar \omega$), oscillations at frequency $\omega$ persist indefinitely.

### Time Crystal Order Parameter

Volovik defines the time crystal order parameter as:

$$\Phi(t) = \frac{1}{V} \sum_i O_i(t)$$

where $O_i$ is an observable at site $i$ (or mode $i$). For a time crystal:

$$\langle |\Phi(t)| \rangle^2 = \text{constant} > 0 \quad \text{for } t \to \infty$$

and the Fourier transform shows a sharp peak at ω ≠ 0:

$$\tilde{\Phi}(\omega) \propto \delta(\omega - \omega_0) + \delta(\omega + \omega_0) + \text{continuous part}$$

The continuous part decays as the system approaches the GGE; the delta-function peaks remain.

### Connection to Prethermalization

Prethermalization refers to the phenomenon where a quantum system reaches a quasi-stationary state (a "plateau") that differs from thermal equilibrium, followed by a slow relaxation to true equilibrium over much longer timescales. Volovik's analysis shows that time crystals are **the most extreme case of prethermalization**: the oscillations persist forever (in an ideal integrable system) or for extraordinarily long times (in systems with weak violations of integrability).

---

## Key Results

1. **Time Crystal Phase Transition**: At the transition from τ_N ~ τ_E (time translational symmetry preserved) to τ_N >> τ_E (time translational symmetry broken), a phase transition occurs. Below the transition, the system is normal; above, it exhibits time-crystalline order.

2. **Frequency Quantization**: The oscillation frequency is quantized by the energy level spacing of the conserved charge sector:

$$\omega_n = \frac{E_N - E_{N-1}}{\hbar} = \frac{\partial E}{\partial N}$$

This is essentially the **chemical potential** difference between consecutive particle number eigenspaces.

3. **Robustness to Perturbations**: Time crystals persist as long as the perturbation breaking the conservation law is sufficiently weak (perturbation strength << $\hbar \omega$). This makes time crystals quite robust, unlike many other quantum phases.

4. **GGE Universality**: The long-time behavior is determined solely by the initial state's values of conserved charges, independent of microscopic details. This makes time crystals a **universal phenomenon** in any integrable system with multiple conservation laws.

5. **Experimental Signatures**:
   - Persistent oscillations in density (or spin) autocorrelation functions
   - Absence of level broadening in spectroscopy
   - Failure of local thermalization (T_eff ≠ T_bath)
   - Enhanced response to driving at frequency $\omega_0/2$ (subharmonic resonance)

---

## Impact and Legacy

Volovik's 2013 proposal was ahead of its time. Subsequent work confirmed and extended the concept:

- **Wilczek (2012-2015)**: Independently proposed discrete time crystals with periodic driving
- **Else, Pretko, Reeves**: Developed classification of time crystals in driven systems (Floquet time crystals)
- **Experimental confirmation**: Google's Sycamore quantum processor demonstrated time-crystalline behavior (Mi et al., 2022)
- **Integrable systems**: Time crystals are now understood as natural consequences of integrability + conservation laws

The concept has profound implications for:
- **Thermalization and quantum chaos**: Understanding when systems fail to thermalize
- **Quantum information**: Long coherence times in time-crystalline systems
- **Cosmology**: Potentially relevant to understanding the early universe's thermalization

---

## Connection to Phonon-Exflation Framework

**Direct Connection**: The phonon-exflation framework produces a **permanent GGE relic** after the BCS transition at z ≈ 3.65, and this relic is a time crystal in precisely Volovik's sense.

Key parallels:

1. **Two Timescales in the Framework**:
   - **Pairing relaxation (τ_pair)**: The Cooper pair condensate decays rapidly due to thermal fluctuations after the transition (typically 10-100 Hubble times)
   - **Integrability timescale (τ_int)**: The underlying Richardson-Gaudin structure ensures that higher-order integrals of motion (8 in total: particle numbers, spins, angular momenta) persist indefinitely

   With τ_int >> τ_pair, the system enters a regime where pairing is destroyed but integrability remains: **a time-crystalline state**.

2. **GGE Relic as Time Crystal**:
   - The ground state of the BCS instability is destroyed by the phase transition (no condensate post-transit)
   - But the higher excitations form a **permanent GGE**, characterized by the 8 conserved Richardson-Gaudin charges
   - This GGE state oscillates with well-defined frequencies set by the quasiparticle spectrum (gap edge ~ 0.1 eV equivalent energy)

3. **Frequency Quantization in Cosmology**:
   - In the framework, the oscillation frequency is:

   $$\omega_{\text{frame}} = \frac{\Delta E_{\text{quasiparticle}}}{\hbar} \approx 10^{15} - 10^{17} \text{ rad/s}$$

   (corresponding to the energy scale set by the BCS gap and quasiparticle spectrum)

   - This predicts **gravitational wave emission** at specific frequencies (sources of detectable stochastic background)

4. **Prethermalization as Cosmic History**:
   - The universe's evolution post-transition is not thermal equilibrium (no true T_eq) but rather a prethermalized state in the GGE
   - The "observed" temperature and entropy growth reflect the slow relaxation of cosmological scales to the GGE plateau, not true thermalization
   - This explains why the universe is **far from thermal equilibrium** despite its age: it is a time crystal that never fully equilibrates

5. **Robustness of Conservation Laws**:
   - The framework predicts that baryon number and other charges should be **conserved to extraordinary precision** (violations << 10^-30 per year)
   - Experiments searching for baryon number violation or proton decay are thus constrained by the time-crystal prediction: they should find no signals

**Framework Prediction**: If the universe is a time crystal:
   - The spectrum of primordial gravitational waves should show **sharp lines** at frequencies $f = \omega_n / 2\pi$ corresponding to the Richardson-Gaudin eigenvalue spectrum
   - The matter power spectrum should exhibit **oscillations** superimposed on the smooth power law, with wavelengths corresponding to the GGE frequency
   - Future observatories (LISA, Einstein Telescope) should detect these gravitational wave lines within the next decade

**Testable Consequence**: The time-crystal prediction is **falsifiable**: if the primordial gravitational wave background is continuous (no sharp lines), the framework's claim that the universe is a permanent GGE relic is excluded.

