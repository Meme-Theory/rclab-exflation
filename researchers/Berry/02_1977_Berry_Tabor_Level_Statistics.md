# Level Spacing Statistics in Integrable Systems and the Berry-Tabor Conjecture

**Author(s):** M.V. Berry and M. Tabor

**Year:** 1977

**Journal:** Proceedings of the Royal Society of London, Series A, Vol. 356, pp. 375-394

---

## Abstract

For quantum systems whose classical counterparts are integrable (possessing N independent constants of motion for N degrees of freedom), the energy level spacing statistics are conjectured to follow Poisson statistics. This is in contrast to chaotic systems, which follow random matrix theory predictions (Wigner-Dyson statistics). The Berry-Tabor conjecture establishes a fundamental connection between classical dynamics and quantum spectral statistics, providing a precise bridge between chaos and order in quantum mechanics. The spacing distribution P(s) for nearest-neighbor level spacings follows:

$P(s) = e^{-s}$

for integrable systems, whereas chaotic systems show level repulsion with $P(s) \sim s^{\beta}$ near $s = 0$ (Wigner-Dyson).

---

## Historical Context

The relationship between classical and quantum mechanics has long been mysterious. The old quantum theory (pre-1925) used action-angle variables to quantize integrable systems. Modern quantum mechanics seemed to dissolve this distinction until the 1970s, when Wigner and others noticed that nuclear energy levels follow statistical patterns similar to random matrices.

Wigner's discovery that spectra of complex nuclei obey random matrix theory suggested a deep connection: if classical mechanics is chaotic, then quantum statistics are "chaotic" (level-repulsive). This observation was fragmentary until Berry and Tabor formulated their conjecture in 1977.

The paper appeared during the birth of quantum chaos (sometimes called "quantum chaology" after Berry's later terminology). It provided one of the first rigorous quantitative predictions connecting global dynamical properties (integrability vs. chaos) to local spectral properties (spacing statistics). The conjecture became a cornerstone of quantum chaos theory.

---

## Key Arguments and Derivations

### Classical Integrability and Quantization

An integrable classical system with N degrees of freedom possesses N independent conserved quantities (constants of motion). The flow is confined to N-dimensional tori in 2N-dimensional phase space. Action-angle variables $(I_1, \ldots, I_N, \theta_1, \ldots, \theta_N)$ describe this structure, where:

$\dot{I}_i = 0, \quad \dot{\theta}_i = \Omega_i(I)$

For a system with N degrees of freedom, the density of states at energy E is:

$\rho(E) = \sum_{\alpha} \delta(E - E_\alpha)$

where the sum is over all quantum levels. In the semiclassical limit, for an integrable system:

$\rho(E) = \frac{1}{(2\pi\hbar)^N} \int d^N p \, d^N q \, \delta(E - H(p,q))$

This integral counts the number of states per unit energy—the density of states.

### Spacing Distribution

Define the unfolded level spacing $s$ as the spacing between consecutive levels normalized by the local density of states:

$s_n = (E_{n+1} - E_n) \rho(E_n)$

where $\rho(E_n)$ is the density at level $n$. Unfolding removes the effect of varying density and focuses on short-range correlations.

For an integrable system, the levels are essentially uncorrelated (statistically independent). A Poisson process produces nearest-neighbor spacings that follow:

$P(s) = e^{-s}$

The mean spacing is $\langle s \rangle = 1$ (by definition of unfolding). The variance is $\sigma^2(s) = 1$.

### Distinction from Chaotic Systems

In a chaotic system, the classical dynamics is sensitive to initial conditions and orbits are dense in available phase space. Quantum mechanically, this leads to strong level repulsion: states avoid crossing in energy. The spacing distribution near $s = 0$ goes as:

- **Gaussian Orthogonal Ensemble (GOE)** (chaotic, time-reversal symmetric): $P(s) \propto s$ (linear repulsion)
- **Gaussian Unitary Ensemble (GUE)** (broken time-reversal symmetry): $P(s) \propto s^2$ (quadratic repulsion)
- **Gaussian Symplectic Ensemble (GSE)** (spin-orbit coupling): $P(s) \propto s^4$

The exponent $\beta$ in $P(s) \sim s^\beta$ is the **level repulsion exponent**, zero for Poisson, nonzero for random matrix ensembles.

### Spectral Rigidity

Berry and Tabor also introduced the concept of **spectral rigidity**, defined as:

$\Delta_3(L) = \min_{a,b} \frac{1}{L} \int_0^L (N(E) - a - bE)^2 dE$

where $N(E)$ is the cumulative number of states (spectral staircase). For Poisson statistics:

$\Delta_3(L) \sim L/15$

For chaotic systems:

$\Delta_3(L) \sim \ln(L)/\pi^2$

Spectral rigidity measures long-range correlations: integrable systems show linear growth (minimal structure), while chaotic systems show logarithmic growth (strong correlations).

### Rational Tori and Quantum Antiscars

The conjecture applies strictly to generic integrable systems where the classical tori are irrational (incommensurate frequencies $\Omega_i$). For rational tori (commensurate frequencies), there are periodic orbits that close. These create subtle deviations from Poisson statistics.

Berry showed that periodic orbits introduce periodic repeats in the spectral autocorrelation function, visible in the "number variance" $\Sigma^2(L) = \langle (N(E+L) - N(E) - L\rho)^2 \rangle$. For pure Poisson:

$\Sigma^2(L) = L$

Corrections appear at scales corresponding to the periods of closed orbits.

---

## Key Results

1. **Poisson statistics for integrability**: Generic integrable quantum systems show Poisson spacing statistics, $P(s) = e^{-s}$, with no level repulsion. This contrasts sharply with chaotic systems.

2. **Spectral rigidity signature**: Integrable systems show linear spectral rigidity $\Delta_3(L) \sim L/15$ (minimal structure), uniquely distinguishing them from random matrix statistics.

3. **Universal Wigner-Dyson statistics for chaos**: All chaotic systems with the same time-reversal properties fall into the same universality class (GOE, GUE, or GSE), independent of microscopic details.

4. **Intermediate regime**: Systems that are partially integrable (mixed phase space with regular islands and chaotic regions) show intermediate spacing statistics—a crossover between Poisson and Wigner-Dyson. This was confirmed experimentally decades later.

5. **Connection to trace formula**: The distribution of spacings is related to the periodic orbit sum (Gutzwiller trace formula). Periodic orbits act as perturbations on the Poisson baseline.

---

## Impact and Legacy

The Berry-Tabor conjecture transformed quantum chaos from a phenomenological observation into a precise, testable framework. It answered the fundamental question: **what property of classical dynamics determines quantum spectral statistics?** The answer is global integrability.

Impact across disciplines:

- **Nuclear physics**: Explained observations in heavy nuclei (chaotic) vs. magic nuclei with closed shells (more integrable).
- **Atomic physics**: Hydrogen atom in strong magnetic fields shows the crossover from Poisson to Wigner-Dyson as the field is increased from low to high (classical ionization).
- **Billiards and quantum chaos**: Rectangular billiards are integrable (Poisson); chaotic billiards like the Sinai billiard show Wigner-Dyson statistics.
- **Condensed matter**: Applied to disordered systems, quantum dots, and mesoscopic physics.
- **Quantum information**: Spectral statistics encode information about quantum correlations and decoherence.

The conjecture has been verified experimentally in microwave cavities, quantum dots, and atomic spectra. It remains one of the most elegant results connecting classical and quantum worlds.

---

## Connection to Phonon-Exflation Framework

In the phonon-exflation model, the internal compactification geometry (SU(3) with Jensen deformation parameter $s$) defines a quantum system on the internal space. The Dirac spectrum on the deformed SU(3) can be studied via spectral statistics:

1. **Integrable vs. chaotic internal dynamics**: If the SU(3) dynamics is effectively integrable (e.g., if the system separates into independent harmonic oscillators in internal coordinates), the phonon eigenvalues should show Poisson statistics. If perturbations break integrability, a crossover to Wigner-Dyson should appear.

2. **Spectral rigidity of the SM spectrum**: The Standard Model fermion spectrum (electron, muon, tau; quarks) might encode classical integrability properties. The observed spacings (mass ratios) could be checked against Poisson or Wigner-Dyson predictions to test whether internal dynamics are ordered or chaotic.

3. **Avoided crossings as periodic orbits**: The avoided crossings observed in the Dirac spectrum as $s$ varies (e.g., sector (3,0)-(2,0) crossings) are analogous to periodic orbits in the classical system. The density and spacing of these crossings contain information about the classical limit of the internal geometry.

4. **Semiclassical quantization**: If the phonon-exflation model has a valid semiclassical limit (phonons as quasiparticles in the internal space), the Berry-Tabor framework provides a consistency check: the phonon spectrum should be compatible with either integrable or chaotic internal classical dynamics.

The Berry-Tabor conjecture is most relevant when testing the self-consistency of the effective internal quantum dynamics in the NCG framework.
