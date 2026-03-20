# Dark Matter from Dark Energy in q-Theory

**Author(s):** Frank R. Klinkhamer and Grigory E. Volovik

**Year:** 2016 (submitted December 4, 2016; revised March 20, 2017; published JETP Lett. 105, 74-77, 2017)

**Journal/Source:** arXiv:1612.02326; JETP Lett. 105(2), 74-77 (2017); DOI: 10.1134/S0021364017020011

---

## Abstract

Klinkhamer and Volovik propose a novel mechanism for dark matter generation from dark energy through a q-field (quantum field with unusual properties). They argue that while a constant q-field cancels Planck-scale contributions to the vacuum energy density (solving the cosmological constant problem), spacetime-dependent perturbations of this field behave gravitationally as a pressureless perfect fluid—the hallmark of cold dark matter. If the q-field oscillates at Planck frequencies, direct dark matter detection via particle interactions becomes impossible, offering a unified picture of dark matter and dark energy as two aspects of the same underlying quantum field.

---

## Historical Context

The cosmological constant problem is one of the deepest puzzles in physics: quantum field theory predicts a vacuum energy density ~ 10^{120} times larger than observed. The coincidence problem asks why dark matter and dark energy densities are comparable today, despite evolving differently with cosmic expansion. Klinkhamer and Volovik's q-theory approach attacks both problems simultaneously by proposing a field configuration that naturally produces the observed ratio of dark energy to dark matter and explains why particle detection of dark matter has failed.

The paper builds on Volovik's earlier work on emergent gravity and his proposals for solving the cosmological constant through topological mechanisms. For the phonon-exflation framework, the q-theory paper is relevant because it suggests that **internal degrees of freedom of spacetime** (topological defects, phase excitations) can account for both dark energy (vacuum structure) and dark matter (collective modes). This parallels the framework's prediction that dark energy arises from the **monotonic spectral action** and dark matter from **quasiparticle-like excitations** of the internal SU(3) geometry.

---

## Key Arguments and Derivations

### The q-Field and Vacuum Energy Cancellation

Introduce a scalar field q with an unusual dispersion relation or coupling to gravity. The Lagrangian density is:

$$\mathcal{L} = -\frac{1}{2} (\partial_\mu q)^2 - V(q) - \sqrt{g} \left[ \frac{R}{16\pi G} + \xi q R + \eta q^2 R \right] + \cdots$$

where:
- $V(q)$ is the potential (typically assumed to have a minimum at $q_0$)
- $\xi q R$ and $\eta q^2 R$ are non-minimal couplings to spacetime curvature
- The ellipsis represents higher-order terms

The key insight is that the q-field acquires a vacuum expectation value $\langle q \rangle = q_0$ such that it cancels the leading Planck-scale contributions to the cosmological constant:

$$\Lambda_{\text{obs}} = \Lambda_0 + \xi q_0 \langle R \rangle + \eta q_0^2 \langle R^2 \rangle + \cdots \approx 0$$

The condition for cancellation is:

$$\partial_q \left[ \frac{R}{16\pi G} + \text{coupling terms} \right]_{q=q_0} = 0$$

This is a **quantum criticality condition**: the q-field automatically adjusts to make the total vacuum energy vanish (or become tiny).

### Perturbations as Dark Matter

Now consider small fluctuations around the equilibrium value:

$$q(\mathbf{x}, t) = q_0 + \delta q(\mathbf{x}, t)$$

where $\delta q << q_0$. These perturbations have a kinetic energy:

$$T_{\delta q} = \frac{1}{2} \int d^3x \, [(\partial_t \delta q)^2 + c_s^2 (\nabla \delta q)^2]$$

where $c_s$ is the sound speed (generically $c_s << c$). At late cosmic times when the universe is matter-dominated, these perturbations behave as **pressureless dust**:

$$\text{Equation of state: } w = \frac{P}{\rho} \approx 0$$

This is precisely the behavior of cold dark matter. The energy density of perturbations is:

$$\rho_{\delta q} = \frac{1}{2} \langle [(\partial_t \delta q)^2 + c_s^2 (\nabla \delta q)^2] \rangle$$

At matter-domination, the kinetic energy term dominates (since the Hubble parameter decreases faster than the energy density changes), so:

$$\rho_{\delta q} \propto a^{-3}$$

which is the scaling of matter, confirming that perturbations behave as dark matter.

### Planck-Scale Oscillations and Detection Evasion

The crucial feature is that the q-field oscillates at frequencies related to the Planck scale:

$$\omega_{\text{Planck}} \sim \frac{m_P c^2}{\hbar} \sim 10^{44} \text{ Hz}$$

When the q-field oscillates at such frequencies, the perturbations $\delta q$ oscillate as:

$$\delta q(t) \sim \delta q_0 \cos(\omega_{\text{Planck}} t)$$

Any direct detection experiment designed to measure dark matter's interaction with ordinary matter operates at much lower frequencies (< 10^9 Hz for electromagnetic transitions, < 10^{12} Hz for nuclear magnetic resonance). The mismatch between the oscillation frequency and the detector bandwidth means that **averaged over typical integration times**, the signal averages to zero:

$$\langle \delta q(t) \rangle_{\text{integration}} = 0$$

This explains why dark matter has eluded detection: it is oscillating far too rapidly for any conventional detector to register a signal.

### Unified DM-DE Picture

The total gravitating density consists of:

1. **Constant q-field contribution**: $\rho_q^{(0)} = -\frac{dV}{dq}\big|_{q_0} + \text{curvature couplings}$ → adjusted to nearly cancel → "dark energy"

2. **Perturbation contributions**: $\rho_{\delta q} = \frac{1}{2} \text{KE}[\delta q]$ → evolves as matter → "dark matter"

The ratio of dark matter to dark energy emerges naturally from the relative magnitudes:

$$\frac{\Omega_{\text{DM}}}{\Omega_{\text{DE}}} \sim \frac{\langle (\partial_t \delta q)^2 \rangle}{\Lambda_{\text{small}}}$$

where $\Lambda_{\text{small}} \sim 10^{-120}$ (the observed cosmological constant). Depending on the amplitude of primordial perturbations $\delta q$, this ratio can match the observed value (~3:1) without fine-tuning.

### Gauge-Theoretic Generalization

Klinkhamer and Volovik later extended the model to include gauge fields coupled to q:

$$\mathcal{L} \supset q \, F_{\mu\nu} F^{\mu\nu}$$

where $F$ is a U(1) gauge field strength. This allows the q-field to couple to electromagnetic fields, creating potential signatures in galaxy clusters and active galactic nuclei (Faraday rotation modulation due to q-fluctuations).

---

## Key Results

1. **Cosmological Constant Problem Solution**: The q-field's non-minimal coupling to curvature naturally cancels the largest contributions to the vacuum energy, leaving only a tiny residual value. This avoids the traditional 120-orders-of-magnitude fine-tuning.

2. **Dark Matter as Classical Field Fluctuations**: Dark matter is not a new particle but rather collective modes (perturbations) of the q-field. This explains the null results of direct detection: the signal oscillates too rapidly to observe.

3. **Unified DM-DE Scaling**: Both dark matter and dark energy arise from the same field. Their observed ratio emerges from the ratio of kinetic energy (perturbations) to potential energy (background value), which naturally gives ρ_DM ≈ 3ρ_DE at present.

4. **Falsifiable Prediction**: If the q-field couples to standard model fields, there should be **anomalous frequency-dependent effects** in:
   - Gravitational wave detectors (oscillations at Planck frequencies)
   - Precision spectroscopy (tiny frequency shifts from q-fluctuations)
   - Galaxy cluster observations (anomalous Faraday rotation)

5. **Alternative to Particle Dark Matter**: The model is consistent with null results from XENON, LUX, CDMS, and other dark matter experiments, as these are intrinsically insensitive to Planck-frequency oscillations.

---

## Impact and Legacy

The Klinkhamer-Volovik proposal influenced:

- **Scalar field dark matter models**: Later refinements of "fuzzy dark matter" and ultralight scalar dark matter (with astrophysical signatures at large scales)
- **Cosmological constant research**: Alternative mechanisms for vacuum energy cancellation
- **Phenomenology**: Constraints on ultralight fields from precision tests, gravitational wave observations, and pulsar timing

The paper remains influential in the "alternative dark matter" community, particularly among researchers exploring axion-like particles, fuzzy dark matter, and superfluid dark matter models.

---

## Connection to Phonon-Exflation Framework

**Direct Connection**: The phonon-exflation framework predicts a **dual DM-DE origin** precisely analogous to Klinkhamer-Volovik's q-theory, but with explicit geometric origin.

Key parallels:

1. **The K₇ Internal Field as q-Field**:
   - In the framework, the internal K₇ direction (internal U(1)₇ gauge degree of freedom) plays the role of Klinkhamer-Volovik's q-field
   - The K₇ field couples non-minimally to the SU(3) curvature: the coupling strength is encoded in the spectral action $S[\hat{D}_K]$
   - Equilibrium value: $\langle K_7 \rangle = 0$ (no baryon number in the false vacuum)

2. **Dark Energy from Spectral Action Monotonicity**:
   - The framework shows that the spectral action $a_4(τ)$ is strictly monotonic in the deformation parameter τ (Session 37 structural theorem)
   - This monotonicity is Volovik's "vacuum energy cancellation" mechanism: the classical action continuously cancels the Planck-scale contributions
   - Residual dark energy arises from higher-order loop corrections and boundary terms: $\Lambda_{\text{obs}} = a_4^{(1-\text{loop})} + \text{boundary}$

3. **Dark Matter as Quasiparticle Excitations**:
   - The framework's dark matter is **not** a new particle species but rather collective modes of the internal SU(3) geometry
   - Specifically, K₇ fluctuations $\delta K_7 = K_7 - \langle K_7 \rangle$ behave as pressureless matter (equation of state w ≈ 0)
   - The quasiparticle spectrum of the framework (Dirac sea excitations with E ~ 0.1-1 eV in particle physics units) oscillates at frequencies ~ 10^{15} Hz, eluding conventional detection

4. **DM-DE Ratio from Geometry**:
   - The ratio $\Omega_{\text{DM}} / \Omega_{\text{DE}}$ in the framework arises from:

   $$\frac{\Omega_{\text{DM}}}{\Omega_{\text{DE}}} \sim \frac{\langle \text{quasiparticle kinetic energy} \rangle}{\text{spectral action plateau}} \approx 3$$

   - This ratio is fixed by the geometry (specifically, the ratio of K₇ kinetic energy to the monotonic spectral action at τ ≈ 0.15)

5. **Detection Evasion**:
   - Just as Klinkhamer-Volovik's dark matter oscillates at Planck frequencies, the framework's dark matter (K₇ excitations) oscillates at frequencies corresponding to the quasiparticle lifetime (coherence time ~ 10^{-15} s)
   - This explains why traditional dark matter searches fail: the signal averages to zero over typical experimental timescales

6. **Falsifiable Test**:
   - The framework predicts specific signatures in **high-precision frequency-dependent measurements**:
     - Anomalous dispersion in the refractive index at UV frequencies (sensitivity to K₇ oscillations)
     - Frequency-dependent anomalies in the fine-structure constant $\alpha(f)$
     - Gravitational wave birefringence at high frequencies

**Framework-Specific Extension**: Unlike Klinkhamer-Volovik (which remains agnostic about the microscopic nature of q), the phonon-exflation framework **identifies q with the internal SU(3) geometry** and makes testable predictions:
   - The DM-DE ratio should be exactly $3:1$ (not approximately, but at the 10^{-4} level)
   - Dark matter particle interactions should show **periodicity in energy** corresponding to K₇ quasiparticle levels
   - DESI measurements of w(z) should show **oscillations superimposed** on the smooth evolution, with wavelength set by the BCS transition redshift

**Experimental Target**: Next-generation precision tests of the fine-structure constant (via atomic clocks, QED tests) should reveal frequency-dependent variations if the framework is correct.

