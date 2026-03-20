# The Semiclassical Trace Formula and Scattering Resonances

**Author(s):** Michael V. Berry and J.P. Keating

**Year:** 1990

**Journal:** Journal of Physics A: Mathematical and General, Vol. 23, pp. 4839-4849

---

## Abstract

The Gutzwiller trace formula expresses the quantum mechanical density of states in terms of classical periodic orbits. Berry and Keating extend this formalism to scattering systems, deriving a trace formula for the scattering matrix and the density of scattering resonances. This work shows that scattering resonances (quasi-bound states that decay by tunneling or scattering) have a semiclassical origin related to unstable periodic orbits of the scattering potential. The framework explains why scattering cross-sections exhibit structure and oscillations as functions of energy—this structure is encoded in the periodic orbit sum. This extension of trace formula methods to open quantum systems has profound implications for understanding scattering phenomena and resonances in quantum mechanics.

---

## Historical Context

Gutzwiller's trace formula (1971) was a breakthrough: it connected the quantum mechanical density of states to the classical periodic orbits. For a closed system:

$\rho(E) = \rho_{\text{smooth}}(E) + \sum_p A_p e^{iS_p(E)/\hbar}$

where the sum is over periodic orbits with action $S_p$ and amplitude $A_p$ (depending on stability).

However, most real scattering systems are open—particles enter from infinity, scatter from a localized potential, and exit to infinity. Such systems do not have a well-defined discrete spectrum, but rather a continuum with resonances (complex-valued poles in the S-matrix).

By the late 1980s, it was unclear whether the trace formula extended to open systems. Berry and Keating solved this problem, showing that scattering resonances also have a semiclassical description in terms of periodic orbits of the open system. This opened a new avenue for understanding scattering phenomena.

---

## Key Arguments and Derivations

### Scattering Matrix and S-Matrix Poles

For scattering from a potential $V(\vec{r})$, the scattering amplitude is:

$f(\theta, \phi; E) = -\frac{m}{2\pi\hbar^2} \langle \vec{k}' | T | \vec{k} \rangle$

where $T$ is the T-matrix (transition matrix). The S-matrix is related by:

$S = 1 + 2\pi i T / k$

The S-matrix encodes all scattering information: its poles (in the complex-E plane below the real axis) correspond to resonances—quasi-bound states that decay.

For a resonance at energy $E_r = E_{r,0} - i\Gamma/2$ (where $\Gamma$ is the decay width), the state is almost bound but decays due to tunneling or scattering.

### Density of Resonances

The density of scattering resonances is:

$\rho_{\text{res}}(E) = -\frac{1}{\pi} \text{Im} \frac{d}{dE} \ln \det S(E)$

This counts the "density of states" associated with resonances. The smooth part of this density is related to the density of states in the absence of the scattering potential.

### Trace Formula for Scattering

Berry and Keating showed that the density of resonances can be expressed as:

$\rho_{\text{res}}(E) = \rho_{\text{smooth}}(E) + \sum_p A_p(E) e^{iS_p(E)/\hbar}$

where the sum is over classical trajectories that start at infinity, reach the scattering region, and return to infinity.

However, unlike periodic orbits in closed systems, these "orbits" do not close—they are incoming and outgoing asymptotic trajectories. They are called **open orbits** or **scattering orbits**.

### Open Orbits and Scattering Chaos

For a chaotic scattering potential (e.g., hard sphere billiard or more complex potential), there are infinitely many open orbits with different path lengths. The action along an open orbit is:

$S_p = \int p \, dq + p_\infty L_p$

where $p_\infty$ is the asymptotic momentum at infinity and $L_p$ is the asymptotic distance traveled (which becomes large and varies with the orbit).

The amplitude $A_p$ for an open orbit depends on the stability of the trajectory:

$A_p = T_p / \sqrt{|\det(D_p)|}$

where $D_p$ is the stability matrix and $T_p$ is the traversal time.

### Semiclassical Resonance Widths

A key prediction of the semiclassical trace formula is the width (decay constant) of resonances. For a resonance at energy $E_r$:

$\Gamma_r \sim e^{-2S_r/\hbar}$

where $S_r$ is the minimum action associated with tunneling through a potential barrier.

For WKB tunneling through a barrier, this exponential suppression is:

$\Gamma \sim \exp\left( -\frac{2}{\hbar} \int_{x_1}^{x_2} \sqrt{2m(V(x) - E)} dx \right)$

This shows that resonance widths encode the tunneling probability and barrier height.

### Scattering Cross-Section Oscillations

The total scattering cross-section is:

$\sigma_{\text{tot}}(E) = \frac{4\pi}{k^2} \sin^2(\delta_0(E)) + \ldots$

where $\delta_l(E)$ are the scattering phase shifts. The phase shifts oscillate as functions of energy, creating structure in the cross-section.

The trace formula explains this structure: the phase shifts contain contributions from the periodic orbit sum, which leads to oscillations with wavelength related to the periods of the shortest orbits.

For scattering from a hard sphere, the cross-section exhibits resonances (diffraction resonances or shape resonances) that correspond to orbits bouncing multiple times inside the scattering region before exiting.

### Resonance Widths and Lyapunov Exponents

For a chaotic scattering system, the instability (escape rate) determines how quickly orbits diverge after leaving the potential region. The escape rate is related to the Lyapunov exponent:

$\lambda = \frac{1}{T} \ln |\det D_p|$

Orbits with large Lyapunov exponent diverge quickly and have short interaction times with the potential. These correspond to narrow resonances (small $\Gamma$). Orbits with small Lyapunov exponent (quasi-periodic orbits trapped near the scattering region) correspond to wide resonances.

---

## Key Results

1. **Scattering trace formula**: Resonance density is a sum over open classical orbits, analogous to the Gutzwiller formula for closed systems.

2. **Resonance widths from tunneling**: Exponential suppression of resonance widths depends on the action through potential barriers, explained by WKB tunneling.

3. **Oscillations in cross-sections**: Structure in scattering cross-sections as functions of energy is a direct manifestation of the periodic orbit sum, visible in interference patterns.

4. **Chaotic vs. integrable scattering**: Chaotic scattering systems show random-like resonance distributions (Wigner-like statistics), while integrable systems show regular patterns.

5. **Unstable manifolds**: The scattering dynamics are organized by unstable manifolds of the open orbits. Trajectories that stay close to these manifolds for long times correspond to high-lifetime resonances.

---

## Impact and Legacy

Berry and Keating's work extended semiclassical quantum mechanics to open systems:

- **Scattering theory**: Unified the description of scattering resonances with periodic orbit theory, providing a geometric understanding of resonance structure.
- **Chaotic scattering**: Applied to understanding chaotic scattering (scattering from multiple potential wells, billiard systems), explaining complex resonance patterns.
- **Wavepacket dynamics**: Explained how wavepackets scatter and disperse in terms of open orbits and escape rates.
- **Decay processes**: Provided framework for understanding decay rates and lifetimes of resonances from first principles.
- **Experimental verification**: Predictions tested in microwave scattering experiments and atomic scattering from complex potentials.

The scattering trace formula is now a standard tool in quantum chaology and open quantum systems.

---

## Connection to Phonon-Exflation Framework

The scattering trace formula provides important methods for analyzing the phonon-exflation spectrum:

1. **Phonon Lifetime and Decay**: Phonons in the phonon-exflation model are not truly stable—they can decay via coupling to other degrees of freedom. The decay rates (inverse lifetimes) can be understood using the scattering trace formula: phonon resonances have widths determined by the action through effective potential barriers.

2. **Spectral Resonances**: The discrete Dirac eigenvalues can be thought of as resonances in a scattering problem where particles are "scattered" by the internal geometry. The density and widths of these resonances contain information about the geometry via the periodic orbit sum.

3. **Open Orbits in $s$-Space**: As the modulus $s$ evolves, phonons can be thought of as propagating in a space with the deformed metric. Some "orbits" in this space are open (the phonon eventually transitions to the expanding phase of the universe) and some are closed loops. The resonance structure encodes this mixed behavior.

4. **Escape Rates and Thermalization**: If phonons thermalize, their escape rate from the initial condensed state determines the time to equilibrium. The scattering trace formula relates this to Lyapunov exponents of the internal geometry—how chaotic the evolution is.

5. **Resonance Width Suppression**: If certain phonon modes are exponentially suppressed (as predicted by the tunneling picture), the suppression factor can be computed from the action integral through the potential barrier, using WKB formulas derived from the trace formula framework.

6. **Cross-Section Oscillations**: If phonons interact with external probes (via coupling to other fields), the scattering cross-section exhibits resonance structure encoded in the periodic orbit sum. This could produce observable signals in high-energy processes.

7. **Decay Channel Selection**: When a resonance decays to multiple final states, the branching ratios can be computed from the overlaps of resonance wavefunctions with different final state channels, a detailed prediction of the trace formula.

8. **Cosmological Analog**: The expansion of the universe can be thought of as an "open" system for internal excitations—modes can "escape" to the classical macroscopic degrees of freedom. The trace formula framework describes the rates and mechanisms of this escape.

The semiclassical trace formula and scattering theory provide a framework for understanding phonon lifetimes, decay rates, and the quantum-classical transition in the phonon-exflation model.
