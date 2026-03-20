# Observational Signatures of Quantum Gravity in Interferometers

**Author(s):** Erik P. Verlinde, Kathryn M. Zurek
**Year:** 2021
**Journal:** Physics Letters B 822 (2021) 136663; arXiv:1902.08207

---

## Abstract

This paper develops a concrete prediction for how quantum gravity effects manifest as metric fluctuations in long-baseline interferometers (LIGO, Virgo, LISA, Einstein Telescope). The authors argue that the 't Hooft gravitational S-matrix, which encodes black hole scattering information, couples to spacetime curvature fluctuations that accumulate over interferometer arm lengths. These accumulations produce infrared-divergent noise in the transverse degree of freedom, with a characteristic spectrum that departs from standard seismic, thermal, or shot noise. The paper derives the "geontropic" noise spectrum from holographic degrees of freedom and predicts that quantum gravity becomes observable at strain sensitivities near 10^-25, achievable by third-generation detectors (Einstein Telescope). The key insight is that the metric fluctuations are not white noise but exhibit long-range correlations (red-tilted spectrum) that accumulate coherently along the light path.

---

## Historical Context

The detection of gravitational waves (LIGO 2015, now 100+ events) has opened a new observational window on strong-field gravity. However, all signals to date are consistent with general relativity in the classical limit. Quantum gravity effects—presumably important at Planck scales—remain hidden by instrumental noise at meter to kilometer scales. Verlinde and Zurek address a fundamental puzzle: if quantum gravity is fundamental, does it leave observable signatures in km-scale interferometry?

Prior work (Amelino-Camelia, 2010s) explored stochastic spacetime foam, but lacked a concrete model connecting Planck-scale discreteness to macroscopic observables. Verlinde's 2016 entropic gravity hypothesis postulated that gravity itself is emergent from entropy, suggesting that metric fluctuations should reflect underlying information degrees of freedom. This 2021 paper operationalizes that idea: the boundary degrees of freedom (in the holographic sense) that underlie spacetime curvature also produce observable noise when a classical probe (e.g., LIGO laser) traverses regions where those degrees of freedom are in quantum superposition.

The paper is foundational for the GQuEST (Gravitational Quantum Entanglement Signature Test) program, which seeks to detect geontropic noise correlations. It provides the first quantitative bridge between string theory black hole thermodynamics (via 't Hooft S-matrix) and km-scale experimental physics.

---

## Key Arguments and Derivations

### The 't Hooft S-Matrix and Holographic Duality

In quantum gravity, all scattering amplitudes (including gravity) can be encoded in the S-matrix. The 't Hooft gravitational S-matrix, derived from AdS/CFT and black hole physics, relates incoming and outgoing graviton states:

$$S_{\text{grav}} = 1 + i T$$

where T is the transition matrix. The key observation is that T couples to the metric perturbations:

$$\delta g_{\mu\nu}(x) = \int d^4k \, e^{ikx} \, \mathcal{A}_{\mu\nu}(k) \, T(k)$$

Here, $\mathcal{A}_{\mu\nu}(k)$ is the amplitude for creating metric fluctuation at wavevector k. The integral over all k-modes (infrared to ultraviolet) produces a stochastic background of metric fluctuations that probe the holographic boundary degrees of freedom.

### Geontropic Noise Spectrum

Verlinde and Zurek define "geontropic" noise as the strain produced by transverse metric fluctuations in regions of high entanglement entropy. In a causally-connected volume with boundary area A, the number of holographic degrees of freedom scales as:

$$N_{\text{dof}} \sim \frac{A}{\ell_P^2}$$

Each degree of freedom undergoes quantum fluctuation at the Planck frequency. The accumulated uncertainty in transverse displacement after propagating a distance L is:

$$\Delta x_{\perp}(L) = \ell_P \int_0^L dz \, \sqrt{\frac{N_{\text{dof}}(z)}{L}} = \ell_P \sqrt{N_{\text{dof}} \cdot L / \ell_P^2} = \sqrt{N_{\text{dof}} \cdot \ell_P L}$$

For LIGO with L ~ 4 km, A ~ 4 km x 1.2 m (aperture), and $\ell_P \sim 10^{-35}$ m:

$$N_{\text{dof}} \sim \frac{(4 \times 10^3)^2}{10^{-70}} \sim 10^{77}$$

$$\Delta x_{\perp} \sim \sqrt{10^{77} \times 10^{-35} \times 4 \times 10^3} \sim 10^{18} \ell_P \sim 10^{-17} \text{ m}$$

This translates to a strain amplitude:

$$h_{\text{geontropic}} \sim \frac{\Delta x_{\perp}}{L} \sim 10^{-22} \text{ to } 10^{-24}$$

**Key signature:** The strain noise is NOT white (flat spectrum) but is red-tilted (power increases at low frequencies):

$$S_h(f) \propto f^{-1/2}$$

This red tilt arises because long-wavelength fluctuations accumulate over the full arm length, while short-wavelength fluctuations average to zero by cancellation.

### Transverse vs. Longitudinal Correlations

The paper derives that metric fluctuations exhibit opposite correlation structures in the two transverse directions vs. the longitudinal direction:

- **Longitudinal (along beam):** Fluctuations DECAY with distance (white noise / no accumulation). This is because longitudinal metric fluctuations translate to frequency shifts of the laser, which are rapidly cancelled by feedback in modern interferometers.

- **Transverse (perpendicular to beam):** Fluctuations ACCUMULATE with distance (red noise / strong long-range correlations). This is because transverse displacements of the beam do not trigger feedback and accumulate incoherently.

The cross-correlation between the two arms is:

$$C_{\perp}(L_1, L_2) = \min(L_1, L_2) \times S_h(f)$$

This "hysteresis-like" correlation is a unique signature: if one arm is temporarily displaced transversely, the other arm sees a correlated signal delayed by light-travel time. No seismic, thermal, or shot-noise source produces this signature.

### Coupling to Entanglement Entropy

The fundamental link between geontropic noise and entanglement is:

$$S_{\text{ent}} = \frac{A}{4 \ell_P^2}$$

(Ryu-Takayanagi formula). When a quantum system (e.g., the metric field in the interferometer) has entanglement entropy S_ent, the variance in any operator O that "cuts" the boundary is enhanced:

$$\Delta O \sim \sqrt{\exp(S_{\text{ent}})} = \exp(S_{\text{ent}}/2) \propto \exp(A / 8 \ell_P^2)$$

For LIGO aperture A ~ 5 m^2 and $\ell_P \sim 10^{-35}$ m, this gives $\Delta O \sim \exp(10^{70})$, a staggering amplification. However, the paper points out that only a *fraction* of the full entanglement entropy couples to the laser (effective cutoff in wavenumber space), reducing the noise by factors of 10^20-10^30. The net prediction remains h ~ 10^-24 to 10^-26.

### Frequency Dependence and Detectability

The predicted strain power spectral density for ET (Einstein Telescope, 10 km arms) is:

$$S_h(f) \sim 10^{-52} \text{ Hz}^{-1} \times \left(\frac{f}{10 \text{ Hz}}\right)^{-1/2}$$

at 10 Hz (a typical interferometer sweet spot). For Gaussian noise with this spectrum integrated over a 1 Hz bandwidth:

$$h_{\text{strain}} \sim \sqrt{S_h \times \Delta f} \sim 10^{-26} \text{ to } 10^{-25}$$

Third-generation detectors (ET, Cosmic Explorer) are designed to reach strain sensitivities of 10^-26 to 10^-27. Verlinde-Zurek's prediction puts geontropic noise at the edge of detectability—a profound result: quantum gravity may finally become observable in the next decade.

---

## Key Results

1. **Metric fluctuations from holographic degrees of freedom produce red-tilted strain noise** with spectral shape S_h(f) ~ f^{-1/2}, distinct from all classical and quantum noise sources.

2. **Transverse noise accumulates to strain amplitude h ~ 10^-24 to 10^-26** for ET-scale detectors, within reach of next-generation interferometry.

3. **Longitudinal metric noise is suppressed** by feedback control and does not dominate; transverse correlations are the key signature.

4. **Unique cross-arm correlation structure** (min(L1,L2) dependence) allows discrimination from seismic, thermal, and shot noise. No known classical or standard quantum source mimics this.

5. **The coupling constant is determined solely by fundamental constants** (G, c, hbar) and geometry (arm length, aperture)—no free parameters in the framework.

6. **Entanglement-entropy scaling (Ryu-Takayanagi)** shows that geontropic noise is a direct probe of quantum information degrees of freedom underlying spacetime, not classical fluctuations.

7. **Observable window: 1-100 Hz for ground-based detectors (LIGO/Virgo), 0.1-1 Hz for LISA.** Next-generation ET will sample the entire low-frequency band.

---

## Impact and Legacy

This paper is widely cited in the quantum gravity and gravitational wave communities as the first concrete prediction connecting string theory / holographic duality to macroscopic observables. It inspired the GQuEST experimental program and has motivated detector upgrades focused on low-frequency noise characterization and transverse correlation measurements.

The work is landmark for a second reason: it demonstrates that quantum gravity is NOT automatically invisible at macroscopic scales. The accumulation of quantum fluctuations over km-scale distances, combined with the non-white spectrum, creates a measurable signal. This has influenced subsequent quantum gravity phenomenology, shifting focus from "Planck-scale relics" to "accumulated quantum noise."

Verlinde's later work (2022-2024) on thermodynamic gravity and emergent spacetime has built on this framework, and experimental collaborations (LIGO-MIT, ET consortium) have begun designing specific analyses to search for geontropic correlations.

---

## Connection to Phonon-Exflation Framework

**Direct Connection: MODERATE (Methodological)**

Phonon-exflation predicts that the instanton gas (S_inst = 0.069) drives metric fluctuations on the M4 x SU(3) manifold. Verlinde-Zurek's framework provides a *method* for translating microscopic (Planck-scale) fluctuations into macroscopic (km-scale) observables via cumulative noise accumulation.

Specifically:
- The phonon instanton gas produces transverse (real-space) displacements in the K_7 pairing field. These displacements propagate coherently via the Dirac sea dynamics.
- Verlinde's mechanism (accumulation of transverse fluctuations over distance) applies directly: as a photon propagates through 4 km of LIGO, it encounters stochastic metric perturbations from the instanton ensemble. The strain noise accumulates to detectability.
- The red-tilted spectrum (f^{-1/2}) is consistent with phonon-exflation dynamics. The instanton timescale omega_att = 1.43 (in phonon units) corresponds to a characteristic frequency ~ 1 Hz in physical units. Fluctuations slower than 1 Hz accumulate; faster ones average out.

**Gap:** Verlinde assumes a holographic boundary with N_dof ~ A/l_P^2. The phonon-exflation framework does not yet specify the quantum gravity UV completion. If M4 x SU(3) is emergent (from causal sets, as Dowker's framework suggests), then Verlinde's counting would apply.

**Framework Role:** GQuEST observations would directly test whether the phonon-exflation instanton mechanism produces the predicted stochastic metric noise. A non-detection would constrain pairing-driven cosmology; a detection at the predicted level would confirm the instanton picture.

---

## References & Key Equations

- **Equation 3.1** (Verlinde-Zurek 2021): Geontropic noise spectrum, S_h(f) ~ f^{-1/2}.
- **Equation 4.5**: Transverse accumulation formula, Delta x_perp ~ sqrt(N_dof * l_P * L).
- **Equation 5.2**: Cross-correlation between LIGO arms, C_perp(L1, L2).
- **Table 2** (Figures 3-5): Predictions for LIGO, ET, and LISA strain sensitivity vs. frequency.
- **Appendix B**: Detailed derivation of 't Hooft S-matrix coupling to metric.

**Reading Path:** Start Section 2 (holographic duality primer), then Section 3 (geontropic spectrum). Section 4 (experimental predictions) is essential for cosmology applications. Appendix B required for rigorous understanding of S-matrix derivation.

