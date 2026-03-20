# Cosmological Gravitational Particle Creation and its Implications for Cosmological Relics

**Author(s):** Edward W. Kolb, Andrew J. Long

**Year:** 2023 (revised 2025)

**Journal:** Reviews of Modern Physics (invited review)

**arXiv:** 2312.09042 [astro-ph.CO]

---

## Abstract

Cosmological gravitational particle production (CGPP) is the creation of particles in an expanding universe due solely to gravitational interactions—that is, without requiring coupling to other fields or explicit potential energy. This review synthesizes theoretical and phenomenological results for CGPP across all particle spins (scalars, spinors, vectors, tensors) and masses. The authors catalog the resulting particle spectra, the abundance of produced particles relative to cosmic expansion, and the implications for dark matter, dark radiation, gravitational waves, and baryon asymmetry. CGPP provides a unified framework for understanding how the expansion of spacetime generates different particle populations, generalizing Parker's mechanism to include gravitational effects not captured by purely kinetic particle creation.

---

## Historical Context

Leonard Parker's 1966 discovery established that quantum field expansion creates particles (Paper #25). However, Parker's analysis focused on the kinetic coupling of a quantum field to the metric: the field's effective mass changes with the scale factor $a(t)$, causing mode mixing and particle creation. A separate question remained: **Can gravity itself (without fields coupling to the metric via masses or interactions) create particles?**

The answer is YES, and it is the subject of Kolb and Long's review. Gravitational particle creation arises from fundamental aspects of quantum field theory:

1. **Operator Redefinition**: In expanding spacetime, the definition of "positive frequency" changes with time. A state that is an eigenstate of annihilation operators at early times becomes a superposition of creation and annihilation eigenstates at late times—particle creation.

2. **Backreaction**: Gravitationally produced particles carry energy-momentum, which curves spacetime further, affecting particle production. This backreaction is typically small but can be crucial for the final relic abundance.

3. **Spin-Dependent Effects**: Particles of different spin (scalar, fermion, vector, tensor) couple to spacetime curvature differently, producing different spectra. For example, gravitons couple only to the Riemann tensor; scalars also couple to the Ricci scalar.

For the phonon-exflation framework, CGPP is relevant because:
- The framework produces particles from internal-geometry expansion (analogous to external spacetime expansion)
- Different types of particles (scalars in the form of Higgs field, fermions in the form of quark/lepton components, vectors in the form of gauge bosons) should have different production rates according to CGPP
- The KK tower (Paper #13 in Baptista's list) is a manifestation of CGPP in extra dimensions

---

## Key Arguments and Derivations

### The Bogoliubov Transformation for Gravitational Particle Creation

For a quantum field in a time-dependent spacetime, the creation/annihilation operators evolve according to the field equation. In the in-vacuum state (early times), we have:

$$a_{\vec{k}}^{\text{in}} |\Omega^{\text{in}} \rangle = 0$$

In the out-vacuum state (late times):

$$a_{\vec{k}}^{\text{out}} |\Omega^{\text{out}} \rangle = 0$$

The relationship between them is:

$$a_{\vec{k}}^{\text{out}} = \alpha_k a_{\vec{k}}^{\text{in}} + \beta_k a_{-\vec{k}}^{\text{in} \dagger}$$

The Bogoliubov coefficient $\beta_k$ determines the number of particles created:

$$N_k = |\beta_k|^2$$

For gravitational creation (no coupling to matter except through spacetime), the Bogoliubov coefficients are computed from the Wronskian of the solutions to the field equation in curved spacetime:

$$\beta_k \propto \int_0^\infty \frac{d\eta}{\eta} \, \omega_k(\eta) \, u_k^*(\eta) \, u_k'(\eta) e^{2i \int \omega_k d\eta}$$

where $u_k(\eta)$ is the mode function and $\eta$ is conformal time. The phase accumulation (WKB integral) determines whether modes are created or destroyed.

### Scalar Field Particle Creation in FRW

For a scalar field with mass $m$ in an FRW universe, the mode equation is:

$$u_k'' + \left( k^2 + m^2 a^2 - \xi R a^2 \right) u_k = 0$$

where $\xi$ is the coupling to the Ricci scalar $R$, and primes denote conformal time derivatives. The key regimes are:

1. **Adiabatic (slowly-varying) modes**: $k^2 + m^2 a^2 \gg (\partial_\eta a)^2 / a^2$. No particle creation; modes oscillate with slowly-changing frequency (WKB approximation exact). $\beta_k \sim e^{-2\pi k / \omega}$ (exponentially suppressed).

2. **Non-adiabatic (rapid-change) modes**: $k^2 + m^2 a^2 \sim (\partial_\eta a)^2 / a^2$. Modes cannot follow the changing frequency; Bogoliubov coefficients are order unity. Significant particle creation.

For inflation with $a(t) = a_0 e^{Ht}$ (constant Hubble $H$), the non-adiabatic regime spans wavenumbers:

$$k \sim H \quad \text{(at horizon crossing)}$$

Modes with $k \lesssim H$ are non-adiabatic and create particles. The total number is:

$$N_{\text{total}} \sim \int_0^{aH} \frac{dk}{2\pi^2} k^2 |\beta_k(a)|^2 \sim \left( \frac{H}{\text{UV cutoff}} \right)^3$$

### Spinor (Fermion) Particle Creation

For a Dirac fermion with mass $m$, the gravitational creation rate differs from scalars. The mode equation is:

$$i \gamma^\mu (\partial_\mu + \Gamma_\mu) \psi_k - m \psi_k = 0$$

where $\Gamma_\mu$ are spin connection coefficients. The Bogoliubov coefficient for fermions in FRW is:

$$|\beta_k|^2 \sim \left( \frac{m^2 a^2}{k^2 + m^2 a^2} \right)^2 \times \mathcal{F}(k/H)$$

where $\mathcal{F}$ is a function encoding the non-adiabaticity. For relativistic fermions ($m \ll H$ during inflation):

$$|\beta_k|^2 \sim \left( \frac{k}{H} \right)^4 e^{-2\pi k / H}$$

Much more suppressed than scalars at the same wavenumber. Heavy fermions (with $m > H$) are barely created during inflation.

### Vector Boson Particle Creation

For a massless vector field (like photons or gluons in the early universe), the action is:

$$S = -\frac{1}{4} \int d^4x \sqrt{-g} \, F_{\mu\nu} F^{\mu\nu}$$

The mode equation for the transverse electric field is:

$$E_k'' + k^2 E_k = 0$$

(the metric enters only indirectly through the definition of the conformal time interval). For most FRW scenarios, massless vectors are NOT produced significantly by gravity alone—they are too "stiff" to couple efficiently.

However, if the vector field is massive (e.g., intermediate bosons in the electroweak era with thermal mass $m_V \sim gT$), the production rate is:

$$|\beta_k|^2 \sim \left( \frac{m_V}{H} \right)^3 e^{-2\pi k / H}$$

comparable to scalar production if $m_V$ is order $H$.

### Tensor (Graviton) Particle Creation

Gravitons (tensor perturbations of the metric) interact with themselves through gravity. The equation for graviton polarization is:

$$h_k'' + k^2 h_k - \frac{a''}{a} h_k = 0$$

where $a''$ is the second derivative of the scale factor. During inflation with $a \propto e^{Ht}$:

$$h_k'' + (k^2 - H^2/4) h_k = 0$$

The coefficient $H^2/4$ represents the effective "mass" of the graviton mode. Modes with $k \lesssim H$ are created significantly:

$$|\beta_k|^2 \sim e^{-2\pi k / H}$$

This is the origin of the primordial gravitational wave background observable in CMB polarization and future detector networks.

### Spectrum Shape Across Spins

Kolb and Long derive that the produced particle spectrum has a universal shape, determined by the adiabatic mismatch parameter $\lambda \equiv \dot{\omega} / \omega^2$ evaluated at the non-adiabatic transition:

- **Scalars**: $N(k) \propto e^{-2\pi k / H} \times (\text{polynomial in } k)$ → broad spectrum peaking near $k \sim H/2$
- **Fermions**: $N(k) \propto e^{-4\pi k / H} \times (\text{polynomial})$ → sharper cutoff, peaks near $k \sim 0$
- **Vectors**: $N(k) \propto e^{-2\pi k / H} \times (\text{polynomial})$ → similar to scalars, depends on mass
- **Tensors**: $N(k) \propto e^{-2\pi k / H} \times (\text{polynomial})$ → same as scalars for massless gravitons

The key insight: **spin determines the power-law prefactor and the exponential rate**, but all particles are exponentially suppressed above the Hubble scale $H$.

### Cosmological Abundances

For a particle with production spectrum $N_k$, the relic abundance (ratio of particle density to radiation density) is:

$$\Omega_X h^2 = \int_0^\infty \frac{dk}{2\pi^2} k^2 N_k(k) \times \left( \frac{\text{energy of particle with mode } k}{\text{entropy density}} \right)$$

For scalars created during inflation with $N_k \sim e^{-2\pi k / H}$:

$$\Omega_X h^2 \sim \left( \frac{H}{M_P} \right)^2 \times g_*^{-1/2}$$

where $g_*$ is the number of relativistic degrees of freedom at reheating. For $H \sim 10^{14}$ GeV (inflation scale):

$$\Omega_X h^2 \sim 10^{-3}$$

This is the dark matter abundance range! Suggesting that some dark matter is produced gravitationally during inflation.

---

## Key Results

1. **Universality of Gravitational Particle Creation**: All particles (scalar, spinor, vector, tensor) are created in expanding spacetime, with spin determining the spectrum shape but not preventing creation.

2. **Spectrum Hierarchy**: Scalars are most efficiently produced, fermions are moderately suppressed (factor of $\exp(-2\pi k / H)$ additional), and vectors/tensors depend on their masses.

3. **Hawking Temperature Analog**: The exponential distribution $e^{-k/k_T}$ (where $k_T \sim H$) resembles a thermal spectrum with effective temperature $T \sim H / (2\pi)$. Gravitational particle creation is thermal for kinematic reasons.

4. **Dark Matter from Gravity**: If a particle has no couplings to standard fields (hence a "hidden sector" particle), CGPP is the only production mechanism. The resulting abundance is naturally of order the observed dark matter density.

5. **Dark Radiation (Sterile Neutrinos)**: Fermions with no electromagnetic/weak interactions are produced as "dark radiation." The spectrum is sharp, peaking at $k \sim 0$, matching observations of extra radiation in cosmology.

6. **Primordial Gravitational Waves**: Tensor modes (gravitons) produced during inflation have a spectrum measurable via CMB polarization and future laser interferometers. The tensor-to-scalar ratio $r$ is related to the graviton production rate.

7. **Backreaction is Small but Measurable**: The energy density in produced particles modifies the Hubble evolution slightly, but this is observable in precision measurements (e.g., number of e-folds in inflation).

8. **KK Tower Production**: In theories with extra dimensions, CGPP produces the entire Kaluza-Klein tower of particles. The spectrum is broadened (many more modes available) compared to 4D particle creation, but the principles are the same.

---

## Impact and Legacy

Kolb and Long's review unified cosmological particle production across spins and masses:

- **Inflation Phenomenology** (2023+): CGPP is now the standard framework for calculating inflationary spectra, including dark matter and dark radiation.

- **Dark Matter Candidates** (2023+): Axions, hidden-sector scalars, primordial black holes, and other candidates are evaluated using CGPP predictions.

- **Gravitational Wave Backgrounds** (2023+): Primordial GWs are understood as CGPP of tensors; networks like LIGO, Virgo, and LISA search for these signals.

- **Extra-Dimensional Phenomenology** (2023+): CGPP in KK theories provides predictions for LHC searches and astrophysical signatures of extra dimensions.

- **Cosmological Relics** (2023+): All exotic particles (dark photons, dark matter, sterile neutrinos, etc.) are cataloged through their CGPP spectra.

---

## Framework Relevance

**Application to KK Tower Production in M^4 × SU(3)**

The phonon-exflation framework's spacetime is M^4 × SU(3). The internal SU(3) dimension is compact (radius $R \sim \ell_{\text{comp}}$), producing a KK tower of particles:

$$m_n^2 = m_0^2 + \frac{n^2}{R^2}$$

where $n = 0, 1, 2, \ldots$ is the KK number and $m_0$ is the mass of the 4D field. Kolb-Long's CGPP results apply directly:

1. **Scalar KK Tower**: Higgs, dilaton, and other scalars decompose into KK modes. Each mode $n$ is produced with abundance:
$$\Omega_{H,n} h^2 \sim \left( \frac{H}{M_P} \right)^2 \times f(n, R, \ell_{\text{comp}})$$
where $f$ includes the mode density. The total is:
$$\Omega_H h^2 = \sum_{n=0}^\infty \Omega_{H,n} h^2$$

2. **Fermion KK Tower**: Quarks, leptons, and neutrinos produce KK modes with rates set by CGPP. The $n$-th mode is suppressed relative to the zero mode by the spin factor:
$$\frac{N_{n}}{N_0} \sim \left( \frac{m_n}{m_0} \right)^2 e^{-2\pi (m_n - m_0) / H}$$

For light modes ($m_n < H$), significant production. For heavy modes ($m_n > H$), production is suppressed.

3. **Vector KK Tower**: Gauge bosons (photon, W/Z, gluons) on the KK tower. The production rate depends on whether the mode is massive (electroweak scale) or massless (photons). Massive vector production: $N_V \propto (m_V/H)^3 e^{-2\pi k/H}$ (Kolb-Long result for massive vectors).

4. **Tensor KK Tower**: Gravitons on the KK tower are produced at the same rate as 4D gravitons, but there are exponentially more modes:
$$\rho_{\text{grav, KK}} = \sum_{n=0}^\infty \rho_{\text{grav}, n} \sim (\text{volume of SU(3)}) \times \rho_{\text{grav, 4D}}$$
This can be significant if $\ell_{\text{comp}}$ is comparable to the Hubble radius.

**Connection to Framework's Instanton Mechanism (S38)**

The framework's instanton-mediated particle creation (Cooper pairs in S38) is **not purely gravitational**—it involves the spectral action $S_{\text{spec}}[D_K]$ and the Dirac operator coupling to internal geometry. However, the CGPP framework provides:

1. **Bogoliubov Picture**: The instanton gas can be reinterpreted as Bogoliubov transformation between the "in" vacuum (free electrons) and "out" vacuum (BCS condensate). CGPP provides the Bogoliubov coefficient formula.

2. **Spin Statistics**: The Cooper pairs are spinless (two fermions coupled to spin singlet), consistent with CGPP scalar production rates.

3. **Thermal-Like Spectrum**: CGPP predicts a spectrum with shape $e^{-k/k_T}$, similar to the framework's instanton creation rate $e^{-S_{\text{inst}}} \approx 0.069$. The effective temperature is:
$$T_{\text{eff}} = \frac{|\partial_\tau E_{\text{cond}}|}{k_B}$$
(from S38, $\partial_\tau E_{\text{cond}} = -0.115$ MeV / unit $\tau$).

4. **Relic Abundance**: The framework's particle population (59 pairs in S38) should match CGPP predictions for internal-geometry production. Testing: run CGPP code for M^4 × SU(3) KK tower with $R = \ell_{\text{comp}}$, compute total particle count, compare to framework simulation (S43 plan).

**Phenomenological Predictions**

- **Dark Matter**: If the framework's Cooper pairs couple weakly to 4D matter (via $D_K$ off-diagonal elements), they contribute to dark matter. The relic abundance:
$$\Omega_{\text{pairs}} h^2 \sim \left( \frac{\Delta}{M_P} \right)^2 \sim 10^{-66}$$
(negligible directly, but masses are set by KK normalization, S33b result)

- **Dark Radiation**: If some KK modes escape to infinity without annihilating, they are "dark radiation." The effective number of neutrinos:
$$N_{\text{eff}}^{\text{KK}} \sim \frac{\text{number of produced KK modes}}{3} \sim 10 - 100$$
depending on $\ell_{\text{comp}}$ (S33a computed $R = 1/2$ exactly; S43 should scan phase space)

- **Primordial Gravitational Waves**: The KK tower has $O(V_{\text{SU(3)}) / \text{horizon}^3$ modes contributing to the tensor background. This could be observable at future detectors if $V_{\text{SU(3)}}$ is large (early universe) or detectable if small (late universe).

**Current Framework Status**

The framework has NOT yet applied CGPP systematically to the M^4 × SU(3) sector. S43+ should:
1. Compute the full KK spectrum $m_n(R)$ for all particle types
2. Apply CGPP formulas to compute production rates for each KK mode
3. Sum to obtain total relic abundances (dark matter, dark radiation, gravitons)
4. Compare to DESI, CMB, and other observational constraints
5. Use the fit to refine estimates of the compactification radius $R$

This is one of the **highest-priority validation tests** for the framework's viability as a cosmological model.
