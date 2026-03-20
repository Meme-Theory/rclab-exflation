# Causal Dynamical Triangulations: Gateway to Nonperturbative Quantum Gravity

**Authors:** Jan Ambjørn, Renate Loll

**Year:** 2024

**Journal:** arXiv:2401.09399; Encyclopedia of Mathematical Physics 2nd Edition (invited)

---

## Abstract

This paper reviews Causal Dynamical Triangulations (CDT) as a background-independent, nonperturbative approach to quantum gravity. The key result is the discovery of an anomalous spectral dimension $d_s(T)$ that varies with the scale $T$, ranging from approximately 2 at small scales (Planck regime) to 4 at large scales (classical limit). The paper discusses how CDT provides numerical evidence for the emergence of classical spacetime geometry from quantum fluctuations of the lattice, with explicit computation of dimensional flow and comparison to other approaches (causal sets, asymptotic safety, loop quantum gravity).

---

## Historical Context

The spectral dimension $d_s(T)$ is a fundamental probe of quantum geometry. Classically, a d-dimensional space is characterized by the scaling of the heat kernel: $\text{Tr}(e^{-tH}) \sim t^{-d_s/2}$, where d_s is the spectral dimension. In a smooth Riemannian manifold, $d_s = \text{dim}(M)$ exactly.

In quantum gravity, the short-distance structure is not a smooth manifold but a quantum superposition of geometries. If the true geometry at Planck scales is fractal or discrete, the spectral dimension should differ from 4. CDT provides the first numerical evidence for this phenomenon: $d_s(T) \approx 2$ for $T \ll l_P$ (Planck scale) but $d_s(T) \to 4$ as $T$ increases.

This dimensional flow has profound implications:
1. **UV stability**: The small dimensionality at short distances may provide natural UV cutoff, avoiding infinities.
2. **Emergence of spacetime**: Classical 4D spacetime emerges dynamically from quantum lattice fluctuations.
3. **Fractal structure**: Intermediate scales exhibit fractal geometry, consistent with Wheeler's quantum foam hypothesis.

Ambjørn-Loll's 2024 review synthesizes two decades of CDT results, providing a comprehensive map of the dimensional flow and its role in validating nonperturbative quantum gravity.

---

## Key Arguments and Derivations

### Causal Dynamical Triangulations Framework

CDT discretizes spacetime as a dynamical lattice of 4-simplices (5-cell polytopes in 4D), with the constraint that the lattice respects a global proper-time foliation. This causality constraint distinguishes CDT from earlier (Euclidean) dynamical triangulation approaches.

The action for CDT is:

$$S[T] = -\frac{1}{16\pi G_{\text{bare}}} \left( \kappa_0 N_0(T) + \kappa_4 N_4(T) \right)$$

where:
- $N_k(T)$ = number of k-simplices at "time" T
- $\kappa_0, \kappa_4$ are bare coupling constants
- The path integral is $Z = \sum_{\text{triangulations}} e^{-S[T]}$

The partition function is evaluated via Monte Carlo simulation on computers. By constructing many random triangulations with Boltzmann weight $e^{-S}$, the distribution of geometric observables (volume, dimension, curvature, etc.) is extracted.

### Spectral Dimension from Heat Kernel

On a finite lattice with metric (edge lengths), the spectral dimension is defined through:

$$d_s(T) = -2 \frac{d \log P(T)}{d \log T}$$

where $P(T)$ is the probability that a random walk returns to its origin after time $T$. Equivalently:

$$d_s(T) = \frac{d \log[\text{Tr}(e^{-tH})]}{d \log t} \bigg|_{t=T}$$

For a smooth 4D manifold, $P(T) \sim t^{-d_s/2} = t^{-2}$, giving $d_s = 4$ independent of T. In CDT, the exponent changes with T:

$$P(T) \sim T^{-d_s(T)/2}$$

with $d_s(T)$ measured numerically for various lattice sizes and couplings.

### Dimensional Flow Results

CDT simulations with $N \sim 100,000$ simplices find:

**UV Regime** ($T \ll 1$ in lattice units):
$$d_s(T) \approx 2 \quad \text{(highly anomalous, close to Hausdorff dimension of Brownian motion)}$$

This means the quantum geometry at short scales is almost 2-dimensional, not 4-dimensional. Geometric fluctuations are so large that the spatial dimension effectively collapses.

**IR Regime** ($T \gg 1$):
$$d_s(T) \to 4 \quad \text{(classical limit, smooth 4D Minkowski or de Sitter)}$$

The transition occurs around the Planck scale ($T \sim 1$ in lattice units = $l_P$ in physical units).

**Intermediate Regime** ($T \sim 1$):
$$d_s(T) \approx 3 \quad \text{(possible fractal structure)}$$

The smooth interpolation $d_s(T) = 2 + (4-2) \tanh(\alpha T / T_0)$ (approximate) captures the observed flow.

### Emergence of Classical Spacetime

The dimensional flow mechanism reveals how classical 4D spacetime emerges from quantum superposition:

1. **Quantum superposition**: Each Monte Carlo sample is a different triangulation (geometry).
2. **Coarse-graining**: Averaging over short-wavelength fluctuations effectively removes them.
3. **RG flow**: As one integrates out UV modes, the spectral dimension decreases, averaging toward the 4D background.

Mathematically:

$$Z[\Lambda] = \sum_{\text{modes}_{UV > \Lambda}} e^{-S[\text{modes}_{\text{IR < \Lambda}}]}$$

where $\Lambda$ is a scale. The effective action for long-wavelength modes exhibits dimensional flow:

$$S_{\text{eff}}[g, \Lambda] = S_{\text{grav}}[g] + \delta S[\Lambda]$$

with $\delta S[\Lambda]$ encoding the effect of integrated-out short-wavelength fluctuations.

### Comparison to Other Approaches

CDT is not unique; other approaches also exhibit dimensional flow:

| Approach | UV Dimension | Mechanism | Status |
|:---------|:-------------|:----------|:-------|
| CDT | 2 | Triangulation fluctuations | Well-established, robust |
| Asymptotic Safety | 2-3 | RG fixed point | Theoretical, unconfirmed numerically |
| Causal Sets | 2 (conjectured) | Discrete poset structure | Limited numerical tests |
| Loop QG | ? (unknown) | Spin network fluctuations | Not yet measured directly |
| Horava-Lifshitz | Depends on $z$ exponent | Modified dispersion at short scales | Parameter-dependent |

The paper argues that CDT provides the most direct and least ambiguous evidence for dimensional flow, having been validated across multiple coupling regimes and lattice sizes.

### Connection to Quantum Foam

Wheeler's quantum foam hypothesis proposes that spacetime fluctuates wildly at Planck scales, with virtual black holes and wormholes proliferating. The CDT dimensional flow gives a concrete realization:

- Small dimension $d_s \approx 2$ means that distance measurements have very large relative uncertainty (quantum fluctuations).
- The return probability $P(T)$ is enhanced (compared to smooth 4D), indicating that random walks are "trapped" in highly connected fractal geometry.
- The correlation length $\xi(T) \sim \sqrt{T}$ (for $d_s=2$) is much shorter than in classical spacetime ($\xi(T) \sim T$), confirming rapid de-correlation.

---

## Key Results

1. **Spectral dimension anomaly is robust**: Measured across multiple lattice sizes and coupling parameters; convergence to $d_s(UV) \approx 2$ is systematic and reproducible.

2. **Dimensional flow interpolates UV to IR**: The function $d_s(T)$ smoothly connects quantum (2D-like) to classical (4D) regimes, confirming continuous emergence.

3. **Classical geometry is an attractor**: Starting from arbitrary initial conditions, the Monte Carlo dynamics flow toward classical configurations, indicating that 4D spacetime is thermodynamically stable (lowest free energy).

4. **Causality is essential**: Euclidean triangulations (no foliation constraint) do not exhibit dimensional flow; causality is necessary for emergence. This validates the importance of a universal time direction.

5. **Planck scale is natural cutoff**: The transition energy scale $T_0 \sim l_P^{-1}$ separates quantum and classical regimes without fine-tuning.

---

## Impact and Legacy

CDT has become one of the most successful nonperturbative approaches to quantum gravity. The dimensional flow discovery resolved a decades-long puzzle: how does 4D spacetime emerge from a quantum theory that knows nothing about dimensions a priori? CDT answers: through dimensional flow driven by quantum fluctuations.

The 2024 review consolidates CDT's status as a viable foundational theory, comparable in rigor to string theory or loop quantum gravity, with the advantage of being fully nonperturbative and finite.

Recent CDT work includes:
- Coupling to matter fields (fermions, gauge fields)
- Computation of scaling dimensions of cosmological operators
- Connection to holography and entropy bounds
- Derivation of gravitational wave spectra

---

## Connection to Phonon-Exflation Framework

**INDIRECT BUT IMPORTANT CONNECTION.** The phonon-exflation framework is a classical (zero-temperature) solution of the spectral action. CDT is a nonperturbative quantum gravity path integral. The two are complementary: phonon-exflation describes a classical soliton-like background; CDT studies quantum fluctuations around arbitrary backgrounds.

Specific connections:

1. **Spectral dimension as diagnostic**: The framework predicts that internal geometry (SU(3) fiber) undergoes a deformation (fold) parameterized by $\tau$. The deformation should exhibit dimensional flow analogous to CDT:
   - At $\tau = 0$ (vanishing internal complexity): $d_s^{\text{internal}} = 0$ (point)
   - At $\tau = \tau_*$ (current epoch): $d_s^{\text{internal}} \approx 3$ (3-dimensional manifold emerging from quantum averaging)
   - This is an **OPEN GATE** (S35: not yet computed)

2. **Emergence mechanism in framework**: The framework proposes that particles are phononic excitations of the SU(3) substrate. CDT's dimensional flow provides a quantum-gravity precedent for emergence: geometry itself (dimensionality) is emergent at large scales. Similarly, fermions and bosons may be emergent excitations of the phononic substrate.

3. **UV cutoff naturalness**: CDT shows that dimensional flow provides a natural UV cutoff ($d_s(UV) = 2$). The framework uses a similar idea: the internal SU(3) geometry has finite spectral width ($\sim$ TeV), providing a natural cutoff for the Dirac spectrum. This may be the framework's answer to the Planck scale divergence problem.

4. **Causality in cosmology**: CDT demonstrates that causality (global time foliation) is essential for emergent spacetime. The phonon-exflation framework assumes a classical Friedmann cosmology with a universal proper time. CDT suggests this causality structure is not imposed but dynamically preferred.

**Status: SPECULATIVE (connections are suggestive but not yet rigorously proven in the framework).** Future work should compute the internal spectral dimension of the SU(3) fiber as a function of deformation parameter $\tau$. If $d_s^{\text{internal}}(\tau)$ exhibits flow analogous to CDT, the framework would have a quantum-gravitational foundation beyond classical spectral action.

