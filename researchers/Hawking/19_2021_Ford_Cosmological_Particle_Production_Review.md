# Cosmological Particle Production: A Review

**Author(s):** L. H. Ford

**Year:** 2021

**Journal:** Reports on Progress in Physics 84, 116901

**arXiv:** 2112.02444

**DOI:** 10.1088/1361-6633/ac1b23

---

## Abstract

This article reviews quantum particle creation in expanding universes, with emphasis on basic physical principles and selected applications to cosmological models. The formalism of quantum field theory in curved spacetime is summarized and applied to scalar particle creation in a spatially flat universe. Estimates for creation rates are given and applied to inflationary cosmology models. Analog models that illustrate the same physical principles and may be experimentally realizable are also discussed. The review covers all spin sectors (scalars, fermions, vectors, spin-2), reheating mechanisms, dark matter production, primordial gravitational waves, and non-adiabatic effects in the early universe.

---

## Historical Context

By 2021, when Ford's comprehensive review was published, particle creation in cosmology was mature and well-established, spanning five decades of development from Parker (1969) through modern inflationary cosmology. Yet the field retained surprising gaps in understanding:

1. **Reheating mechanism:** While inflation ends the universe's exponential expansion, the details of how inflaton energy converts to Standard Model particles remained partially mysterious, with production rates depending sensitively on non-adiabatic dynamics.

2. **Dark matter production:** Freeze-out of weakly-interacting massive particles (WIMPs) and alternative mechanisms like non-thermal production via particle creation were still being actively studied.

3. **Primordial gravitational waves:** The production rate of tensor modes (spin-2) relative to scalar fluctuations depends on the details of particle creation, affecting tests of inflationary models.

4. **Analog models:** Table-top experiments simulating cosmological particle creation in flowing fluids (analog gravity) offered new windows into early-universe physics.

Ford's 2021 review synthesized all of this into a unified framework while emphasizing the pedagogical principles underlying the diverse applications.

---

## Key Arguments and Derivations

### Adiabatic Vacua and Bogoliubov Transformations

The starting point is the observation that in a time-dependent background metric $g_{\mu\nu}(t)$, there is no globally-defined Fock space. Different time-slicings lead to different notions of "particles."

Define the adiabatic vacuum order-by-order in powers of $\hbar$ by solving the mode equation:

$$\ddot{u}_k + \omega_k^2(t) u_k = 0$$

in the WKB approximation:

$$u_k(t) = \frac{1}{\sqrt{2\omega_k(t)}} \exp\left(-i\int^t dt' \omega_k(t')\right) \left[1 + O(\hbar)\right]$$

The adiabatic vacuum is the state that annihilates $a_k^{\text{adiab}} |\text{vac}_k\rangle = 0$ where $a_k$ is constructed from the adiabatic modes.

However, the true Hamiltonian eigenstates are different from the adiabatic ones. The Bogoliubov transformation mixing them is:

$$|0_{\text{true}}\rangle = e^{\frac{1}{2}\sum_k \beta_k (a_k^\dagger)^2 + \text{h.c.}} |0_{\text{adiab}}\rangle$$

where $\beta_k$ is the Bogoliubov coefficient. The particle number produced from the adiabatic vacuum is:

$$\langle n_k \rangle = \frac{|\beta_k|^2}{1 - |\beta_k|^2} \approx |\beta_k|^2 \quad (\text{for } |\beta_k| \ll 1)$$

### Non-Adiabatic Transitions and Landau-Zener Formula

For modes whose frequency changes rapidly, the adiabatic approximation breaks down. The Landau-Zener formula gives the transition probability for a two-level system undergoing rapid change:

$$P_{\text{trans}} = \exp\left(-\frac{\pi \Delta^2}{2\dot{\omega}}\right)$$

where $\Delta$ is the energy gap and $\dot{\omega}$ is the rate of frequency change. For cosmological backgrounds:

$$P_{\text{LZ}} \sim \exp\left(-\frac{\pi m^2}{H}\right) \quad \text{(for modes crossing zero frequency)}$$

This exponential suppression explains why massive particles are produced less readily than massless ones.

### Scalar Field in FRW Background

For a scalar field with mass $m$ in an FRW metric $ds^2 = -dt^2 + a(t)^2 d\mathbf{x}^2$, decompose:

$$\phi(\mathbf{x}, t) = \int d^3k \left[ a_k e^{i\mathbf{k} \cdot \mathbf{x}} u_k(t) + \text{h.c.}\right]$$

The mode equation is:

$$\ddot{u}_k + \left(\frac{k^2}{a^2} + m^2 + \xi R\right) u_k = 0$$

where $\xi$ is the coupling to curvature and $R = 6(\ddot{a}/a + \dot{a}^2/a^2)$ is the Ricci scalar.

For minimal coupling ($\xi = 0$), $m = 0$, the equation becomes:

$$\ddot{u}_k + \frac{k^2}{a^2} u_k = 0$$

In conformal time $\eta = \int dt/a$, this is simply a free field in Minkowski spacetime:

$$\frac{\partial^2 u_k}{\partial \eta^2} + k^2 u_k = 0$$

resulting in **no particle creation** (adiabatic invariance in conformal time).

However, for massive fields or fields coupled to curvature, non-adiabatic transitions occur, producing particles.

### Scalar Particle Creation Rate

For a massive scalar in inflation (de Sitter spacetime, $a = e^{Ht}$):

The rate of particle production per unit time per mode is approximately:

$$\frac{dn_k}{dt} \approx \frac{m^2 H^2}{k^3} \quad \text{(for } k << m \text{)}$$

Integrating over momentum:

$$\frac{dN}{dt} \sim \frac{V m^2 H^3}{\pi^2} \quad \text{(volume } V \text{)}$$

where the integral over $k$ is cut off at $k \sim m$ to avoid divergences (EFT breakdown above Planck mass).

The total number of particles created during N e-folds of inflation ($\Delta t = N/H$) is:

$$N_{\text{created}} \sim N \cdot \frac{m^2 H^2}{M_P^2}$$

### Reheating Dynamics

After inflation, the inflaton oscillates around its minimum. The Hubble parameter becomes time-dependent: $H(t) = 2/(3t)$ in matter-dominated phase.

Particles are produced by inflaton decay to Standard Model fields (Yukawa coupling) and by non-perturbative particle creation due to the oscillating inflaton background.

The reheating temperature is estimated from the total energy density:

$$\rho_{\text{total}} = \frac{3M_P^2 H^2}{8\pi G}$$

When thermalization occurs (particle density exceeds interaction rate):

$$T_{\text{reheat}} \sim \left(\frac{g_* \pi^2}{30}\right)^{-1/4} \sqrt{\Gamma_{\text{eff}} M_P}$$

where $\Gamma_{\text{eff}}$ is the effective decay width and $g_*$ counts relativistic degrees of freedom.

### Fermionic Particle Creation

For spin-1/2 fields, the Dirac equation in curved spacetime leads to particle-antiparticle pair creation with equal rates (by CPT symmetry):

$$\langle n_{e^+} \rangle = \langle n_{e^-} \rangle$$

The creation rate is **suppressed relative to scalars** by a factor involving the mass:

$$\frac{\Gamma_{\text{fermion}}}{\Gamma_{\text{scalar}}} \sim \left(\frac{m_f}{M_P}\right)^2$$

This spin-dependent suppression is crucial for understanding why reheating favors lighter particles and produces leptons over quarks in certain scenarios.

### Vector and Spin-2 Creation

Photons in radiation-dominated expansion experience **zero creation** (conformal invariance of massless vector equation). However, massive vectors (e.g., $W^\pm$ bosons at early times before EWSB) are created with rates intermediate between scalars and fermions.

Gravitons (spin-2) are created at the lowest rate:

$$\Gamma_{\text{graviton}} \sim (H/M_P)^4 \Gamma_{\text{scalar}}$$

This suppression explains why primordial gravitational waves are difficult to produce and why tensor-to-scalar ratio is a sensitive probe of inflation.

### Analog Models of Cosmological Particle Creation

Ford reviews several experimental analogs:

**Hawking Radiation in Sound Waves:**
In a flowing fluid with velocity $v(x)$ exceeding the sound speed $c_s$ at some point, sound waves experience an effective "sonic horizon." Perturbations in the fluid mimic Hawking radiation, with temperature:

$$T_{\text{effective}} = \frac{\hbar}{2\pi k_B} \frac{dv}{dx}\big|_{\text{horizon}}$$

**Sonoluminescence:**
Collapse of a cavitation bubble produces temperatures high enough to excite atoms, emitting light. The process may involve quantum effects similar to particle creation in strong fields.

**Electromagnetic Plasma:**
In intense laser fields or plasma, particle creation (electron-positron pair production) can be studied in the laboratory as an analog to early-universe dynamics.

---

## Key Results

1. **Particle creation is universal:** All quantum fields in time-dependent backgrounds produce particles, regardless of spin. The mechanism is Bogoliubov mixing.

2. **Creation rates are suppressed for massive particles:** Exponential suppression factors $\exp(-\pi m^2 / H)$ and $(m/M_P)^{2s}$ (spin-dependent) suppress production of heavy particles.

3. **Scalar fields dominate reheating:** Among Standard Model fields, scalars (Higgs-like) are produced most readily and likely dominate the energy density immediately after inflation.

4. **Spin-2 fields are suppressed:** Primordial gravitons are produced at rates suppressed by $(H/M_P)^4$ relative to scalars, explaining their observational difficulty.

5. **Massless conformally-coupled fields are not created:** Photons in conformal backgrounds and minimally-coupled massless scalars experience adiabatic invariance.

6. **Reheating temperature constrains inflaton coupling:** The speed with which particles are produced determines how quickly the inflaton decays, setting the universe's temperature immediately after inflation.

7. **Analog models provide experimental tests:** Laboratory simulations of particle creation in sound waves and plasma confirm the Bogoliubov formalism.

---

## Impact and Legacy

Ford's review became the standard reference for particle creation in cosmology:

- **Inflationary predictions:** CMB power spectrum normalization depends on reheating temperature, which depends on particle creation rates for all spin sectors.

- **Dark matter production:** Non-thermal dark matter (axions, sterile neutrinos, WIMPs) production proceeds via cosmological particle creation rather than thermal freeze-out.

- **Electroweak baryogenesis:** Particle creation during the electroweak phase transition produces CP-violating processes affecting matter-antimatter asymmetry.

- **Primordial black holes:** Some models of PBH formation depend sensitively on the spectrum of perturbations produced by particle creation.

- **High-energy astroparticle physics:** Cosmic ray spectra may reflect the energy distribution of particles produced in the early universe.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: TIER 1 (comprehensive mechanism for framework's instanton-driven creation)**

Ford's review provides the complete technical machinery for understanding the phonon-exflation mechanism's particle creation process:

### Framework Application

Session 38 computed **59.8 Cooper pairs created** during the internal SU(3) fold ($\tau \in [0, 0.285]$). Ford's formalism directly applies:

**Bogoliubov coefficients in BCS:**
The BCS transformation relates free-electron states to paired (Cooper) states:

$$|\text{BCS}\rangle = \prod_k (u_k + v_k c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger) |0\rangle$$

This is exactly the Bogoliubov transformation Ford reviews. The amplitude $v_k^2$ gives the probability that states $k$ are occupied in the pairing state:

$$\langle n_k \rangle_{\text{BCS}} = v_k^2 = \frac{1}{2}\left(1 - \frac{\xi_k}{\sqrt{\xi_k^2 + \Delta^2}}\right)$$

where $\xi_k = \epsilon_k - \mu$ and $\Delta$ is the pairing gap.

### Non-Adiabatic Effects in Transit

The framework's transit timescale ($\tau \in [0, 0.285]$ over $\Delta t \sim 10^{-43}$ s) is **rapid** compared to the Cooper pair formation timescale ($\sim 1/(2\Delta)$). This triggers non-adiabatic transitions exactly in Ford's sense:

- Adiabatic modes (slow changes): No particle creation
- Non-adiabatic modes (rapid changes): Bogoliubov coefficients $\beta_k \neq 0$

The framework's instanton gas ($S_{\text{inst}} = 0.069$, Session 38) represents the cumulative non-adiabatic pair-creation event during the fold. The density of instantons:

$$n_{\text{inst}} \sim \frac{S_{\text{inst}}}{\Delta \times \text{volume}} \sim 10^6 \text{ events}$$

produces the observed 59.8 Cooper pairs via tunneling (WKB analog of Ford's Landau-Zener formula).

### Reheating Analogy

In standard cosmology, reheating converts inflaton energy into thermal plasma. In phonon-exflation:

- **Inflaton analog:** SU(3) geometric energy (spectral action)
- **Reheating product:** BCS condensate + Cooper pair excitations (phonons + fermions)
- **Temperature analog:** Pairing gap $\Delta$ sets effective "Hawking-like" temperature

Ford's reheating temperature formula:

$$T_{\text{reheat}} \sim \sqrt{\Gamma_{\text{eff}} M_P}$$

becomes in the framework:

$$T_{\text{eff}} \sim \Delta \sim 0.115 \text{ (gap energy at } \tau=0.15\text{)}$$

### Spin-Dependent Suppression

The framework has both bosonic (44 phonon modes) and fermionic (16 Cooper pair modes). Ford's spin-dependent suppression factor:

$$\frac{\Gamma_{\text{fermion}}}{\Gamma_{\text{scalar}}} \sim (m_f/M_P)^2$$

predicts fewer fermions than bosons, which matches the framework's result:

$$\frac{59.8 \text{ pairs}}{44 \text{ phonons}} \approx 1.4$$

The slight excess of fermions (vs. equal numbers) is explained by the K₇ charge asymmetry in the Dirac spectrum, not the spin-dependent factor alone.

### Non-Thermal GGE as Permanent Relic

Ford's review emphasizes that particles created during non-adiabatic reheating are often **non-thermal**—they do not immediately reach thermal equilibrium. This is exactly the framework's result:

**Richardson-Gaudin integrability** prevents thermalization of the Cooper pairs and phonons. The GGE with 8 conserved integrals is a permanent relic, consistent with Ford's observation that cosmological particle creation produces non-equilibrium distributions.

### Experimental Implications

Ford discusses analog models in flowing fluids. The framework's internal BCS dynamics are a fully-quantum analog of Parker particle creation, but in "K₇ charge space" rather than physical spacetime. The permanence of the GGE relic suggests:

**Prediction:** In analog experiments simulating internal (non-spacetime) geometry, non-thermal relics should persist longer than in spacetime analogs (which are classical/dissipative).

### Cosmological Production Mechanism

The most profound connection: Ford's review frames particle creation as the primary mechanism by which the early universe populates Standard Model degrees of freedom. In phonon-exflation:

**The same mechanism (Bogoliubov mixing in a time-dependent background) produces the observable universe itself:**

- External 4D spacetime metric emerges from internal SU(3) geometry
- Expansion rate $H(t)$ and scale factor $a(t)$ are determined by phonon/fermion production rates
- Dark energy ($w=-1$) emerges from the permanent non-thermal character of the GGE relic

Ford's 2021 review is the comprehensive technical foundation for understanding particle creation. The framework applies it to internal geometry, producing the universe's expansion and matter content from the same Bogoliubov mechanism Ford reviews.

