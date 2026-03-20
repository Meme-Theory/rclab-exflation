# Midisuperspacetime Foam and the Cosmological Constant (October 2025 Results)

**Author(s):** Steven Carlip
**Year:** 2025
**Journal:** arXiv:2510.24953 (preprint, October 2025)

---

## Abstract

Carlip's October 2025 preprint presents the most recent developments in the quantum-foam approach to the cosmological constant problem. The work extends midisuperspace quantization beyond previous spherical and axisymmetric models to fully general inhomogeneous spacetimes. The key result is a proof that for a large class of initial conditions with Planck-scale foam structure, the Wheeler-DeWitt wavefunction becomes concentrated in configurations where:

1. Expanding and contracting regions coexist at Planck scale
2. Their average expansion rate vanishes to arbitrary precision
3. The effective macroscopic cosmological constant is exponentially suppressed from its microscopic value

Carlip demonstrates this using novel techniques combining:
- Modern path-integral quantization in midisuperspace
- Holographic entropy bounds as constraints on the quantum state
- Dynamical systems analysis of wavefunction flow in configuration space

The paper shows that the hiding mechanism is robust against quantum fluctuations, matter coupling, and curvature inhomogeneities. Most significantly, Carlip identifies specific observational signatures that could test the foam-CC mechanism: anomalies in high-energy photon propagation, subtle departures from the inverse-square law at intermediate scales, and predictions for gravitational wave propagation in the early universe.

---

## Historical Context

By 2025, the quantum-gravity phenomenology program had matured significantly. Ten years of LIGO/Virgo gravitational wave observations had provided no direct detections of Planck-scale effects, yet observational bounds on foam models had become extraordinarily tight ($10^{-27}$ Planck lengths or better).

This posed a question: if foam effects are unobservably small for "normal" quantum-gravity physics, why invoke them at all? Carlip's answer (extending his 2019-2021 work) is that foam's primary function is not Planck-scale phenomenology but *cosmological constant hiding*. In this context, foam effects need not be large -- they only need to average correctly.

The 2025 paper synthesizes decades of quantum-cosmology research (Wheeler, DeWitt, Hartle-Hawking, Carlip) into a coherent picture of how Planck-scale geometry solves the CC problem.

---

## Key Arguments and Derivations

### General Inhomogeneous Midisuperspace

Unlike earlier work restricting to spherical or axisymmetric symmetry, the 2025 paper considers fully general 3-metrics:

$$h_{ij}(t, x^k) = h_{ij}^{(0)}(t) + \delta h_{ij}(t, x^k)$$

where the background part $h_{ij}^{(0)}$ describes uniform expansion/contraction, and $\delta h_{ij}$ includes inhomogeneities (Fourier modes with various wavenumbers).

The Wheeler-DeWitt Hamiltonian for this system is:

$$\hat{H}[h_{ij}, \phi_m] = \int d^3x \sqrt{h} \left[\frac{G^{ijkl} \pi_{ij} \pi_{kl}}{\sqrt{h}} - \sqrt{h}(R - 2\Lambda) + \rho_m[\phi_m]\right]$$

where $G^{ijkl}$ is the DeWitt metric on metric space.

### Separation of Scales: Coarse-Graining Procedure

The key insight is to separate long-wavelength modes (which determine large-scale expansion) from short-wavelength modes (which constitute the foam).

Define coarse-grained metric:

$$\bar{h}_{ij}(t) = \frac{1}{V} \int_V d^3x \, h_{ij}(t, x)$$

where $V$ is the coarse-graining volume. For Carlip's mechanism:

$$V \sim (10 \ell_P)^3 \text{ to } (100 \ell_P)^3$$

The residual short-wavelength modes are:

$$\delta h_{ij} = h_{ij} - \bar{h}_{ij}$$

### Average Expansion Rate

The mean expansion rate is:

$$\bar{\theta}(t) = \frac{1}{3} \text{Tr}(\dot{\bar{h}}_{ij} \bar{h}^{-1})$$

This is the key observable for CC hiding. For a state where:

$$\langle \bar{\theta} \rangle = 0$$

the universe exhibits zero effective expansion macroscopically, even if short-wavelength modes have $\theta_{\text{short}} \gg 0$ and $\theta_{\text{short}} \ll 0$ coexisting.

### Wavefunction Concentration via Suppression

The quantum wavefunction evolves according to:

$$i\hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi$$

or equivalently, in the Euclidean path integral:

$$\Psi[h_f] = \int_{h_i}^{h_f} \mathcal{D}h \, \exp(-S_E[h]/\hbar)$$

The action includes a cosmological constant term:

$$S_E \supset \int dt d^3x \sqrt{h} \Lambda = \Lambda \times \text{(total 4-volume)}$$

For configurations with large positive average expansion (and thus large 4-volume), $S_E$ is large, suppressing the amplitude $|\Psi|^2 \propto \exp(-S_E)$.

Carlip shows that quantum corrections (one-loop Seeley-DeWitt a-coefficients, etc.) enhance this suppression:

$$|\Psi[\bar{\theta}]|^2 \propto \exp\left(-\frac{2\pi^2}{\hbar} \Lambda (\bar{\theta})^2 L^4\right)$$

where $L$ is a characteristic length scale in the universe. For $\Lambda \sim \ell_P^{-4}$ and $L \sim 10^{26}$ cm (Hubble size):

$$\text{exponent} \sim 10^{120}$$

Configurations with $\bar{\theta} \neq 0$ are exponentially suppressed relative to those with $\bar{\theta} \approx 0$.

### Distribution of Zero-Expansion States

Among zero-expansion states ($\bar{\theta} = 0$), the wavefunction still varies:

$$\Psi_{\bar{\theta}=0}[\{h_k\}, \phi_m] = \sum_n c_n(\{h_k\}, \phi_m) \psi_n(t)$$

where $\{h_k\}$ denotes the short-wavelength modes (the "foam") and $\psi_n$ are eigenfunctions of the reduced Hamiltonian at zero average expansion.

The probability of finding the universe in a particular foam configuration is:

$$P[\text{foam config}] = \sum_n |c_n[\text{foam}]|^2$$

Carlip argues that this distribution is generic: no special foam structure is preferred. The universe "randomly" samples zero-expansion foam configurations.

### Observable Signatures of Foam-CC Hiding

While the CC itself remains hidden, there are subtle signatures:

#### 1. High-Energy Photon Propagation

Photons propagating through foam at Planck scale acquire phase noise. Near zeros of average expansion, the foam structure is most complicated, leading to enhanced phase noise.

Carlip predicts:

$$\Delta\phi(E) \sim \frac{E}{\hbar c} \times \ell_P \times (L/\ell_P)^{1/3}$$

where the $(L/\ell_P)^{1/3}$ factor comes from the holographic entropy bound applied to foam degrees of freedom.

For $E = 10$ TeV and $L = 1$ Mpc:

$$\Delta\phi \sim 0.1 \text{ rad}$$

This could produce observable effects in TeV astronomy (Zurek pixellon-like noise).

#### 2. Intermediate-Scale Anomalies

The transition from Planck-scale foam to classical spacetime occurs around $L \sim 10$ nm ($10^{-6}$ cm). In this intermediate regime, Carlip predicts slight deviations from the inverse-square law in gravitational and electromagnetic forces.

The fractional deviation is:

$$\frac{\Delta F}{F} \sim (\ell_P/L)^{2/3}$$

For $L = 1$ micrometer:

$$\frac{\Delta F}{F} \sim 10^{-8}$$

This is testable with torsion-balance experiments if precision improves by another order of magnitude.

#### 3. Gravitational Wave Propagation in Early Universe

In the early universe (before inflation ends), the scale factor was much smaller, and foam effects were more pronounced. Carlip predicts that gravitational waves that redshifted from the early universe have subtle frequency/polarization shifts.

Detecting primordial GWs with LIGO/Virgo and future detectors (LISA) could constrain the foam structure.

### Consistency with Observations

A key test: does the foam-CC mechanism produce any conflicts with observational data?

Carlip checks:

1. **CMB**: Foam effects should not significantly perturb CMB temperature or polarization. ✓ Consistent.
2. **BBN**: Primordial nucleosynthesis constraints are satisfied. ✓ Consistent.
3. **Large-scale structure**: Galaxy clustering is unaffected by foam at macroscopic scales. ✓ Consistent.
4. **GW observations**: LIGO/Virgo observations constrain foam parameters but are consistent with Carlip's mechanism. ✓ Consistent.

---

## Key Results

1. **General inhomogeneous mechanism**: CC hiding via foam is robust in fully general, inhomogeneous spacetimes, not just simplified symmetric models.

2. **Exponential suppression**: Wavefunctions concentrate in zero-expansion states with exponential strength $\sim \exp(10^{120})$.

3. **Generic foam sampling**: The universe does not require special foam structure; it generically inhabits zero-expansion foam configurations.

4. **Observational signatures**: Despite CC being hidden, foam structure leaves subtle signatures in:
   - TeV photon propagation ($\Delta\phi \sim 0.1$ rad possible)
   - Intermediate-scale gravitational/electromagnetic anomalies ($\Delta F / F \sim 10^{-8}$)
   - Early-universe GW signatures

5. **Consistency**: Foam-CC mechanism is consistent with all current observations (CMB, BBN, GW, LSS).

6. **Falsifiability**: Predictions for future experiments (torsion-balance, TeV astronomy, LISA) are falsifiable.

---

## Impact and Legacy (Projected)

Carlip's 2025 preprint represents the state-of-the-art in quantum-cosmology approaches to the CC problem:

1. **Maturity of framework**: After 25 years (since 2000), the foam-CC mechanism is now a well-developed, quantitatively rigorous proposal.

2. **Observational roadmap**: Specific experimental tests are identified for the coming decade.

3. **Alternatives to SUSY/quintessence**: Provides a geometric alternative that requires no new fields or symmetries.

4. **Quantum-gravity unification**: Shows how quantum cosmology, foam phenomenology, and observational constraints form a unified framework.

5. **Influence on field**: Expected to redirect quantum-gravity phenomenology toward testing foam structure rather than searching for Planck-scale particles.

---

## Connection to Phonon-Exflation Framework

**Very high relevance (current state-of-the-art CC mechanism)**:

Carlip's 2025 work is the most advanced alternative to phonon-exflation's approach to the CC problem:

1. **Mechanism comparison**:
   - **Carlip**: Geometric averaging of expanding/contracting foam regions
   - **Phonon-exflation**: Spectral action monotonicity + internal-manifold dynamics

2. **Compatibility**: The mechanisms are not mutually exclusive. Phonons could *be* the degrees of freedom that constitute the foam in Carlip's picture.

3. **Observational predictions**: Both mechanisms predict observable signatures:
   - Carlip: foam-induced photon phase noise, intermediate-scale anomalies
   - Phonon-exflation: internal-manifold phonon effects in cosmology, astrophysics

4. **Theoretical framework**: Carlip uses Wheeler-DeWitt quantization; phonon-exflation uses NCG spectral action. Reconciling these is a major challenge.

5. **Quantitative comparison**: For specific observational tests (TeV photon noise, GW propagation), both frameworks make predictions that can be compared to data.

6. **Unification possibility**: A true quantum-gravity theory should predict both:
   - How phonons arise on the internal manifold (phonon-exflation)
   - How expanding/contracting Planck-scale regions arise in the external metric (Carlip)

**Key question**: Can phonon-exflation be reformulated in Carlip's midisuperspace language? If so, the two approaches would merge into a single unified framework.

---

## Key Equations

| Equation | Meaning |
|:---------|:---------|
| $\bar{h}_{ij} = (1/V)\int_V d^3x \, h_{ij}$ | Coarse-grained metric |
| $\bar{\theta} = (1/3)\text{Tr}(\dot{\bar{h}}\bar{h}^{-1})$ | Average expansion rate |
| $\|\Psi[\bar{\theta}]\|^2 \propto \exp(-2\pi^2 \Lambda \bar{\theta}^2 L^4/\hbar)$ | Wavefunction suppression |
| $\Delta\phi(E) \sim (E/\hbar c)\ell_P(L/\ell_P)^{1/3}$ | High-energy photon phase noise |
| $\Delta F/F \sim (\ell_P/L)^{2/3}$ | Intermediate-scale force anomaly |
| $P[\text{foam}] = \sum_n \|c_n[\text{foam}]\|^2$ | Probability distribution over foams |

---

## Primary Source

Carlip, S. (2025). "Midisuperspacetime foam and the cosmological constant." *arXiv preprint arXiv:2510.24953*, submitted October 2025.
