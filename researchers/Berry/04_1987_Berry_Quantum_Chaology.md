# The Bakerian Lecture 1987: Quantum Chaology

**Author(s):** Michael V. Berry

**Year:** 1987

**Journal:** Proceedings of the Royal Society of London, Series A, Vol. 413, pp. 183-198

---

## Abstract

The relationship between classical chaos and quantum mechanics is subtle and counterintuitive. Berry distinguishes between "quantum chaos" (a misnomer) and "quantum chaology"—the study of quantum mechanics of classically chaotic systems. The paper refutes the idea that quantum mechanics is chaotic. Instead, quantum mechanics is fundamentally deterministic and reversible; chaos is a classical phenomenon. The quantum mechanical analogs of classical chaos appear in the statistical properties of energy levels, spectral correlations, and scattering time delays. The semiclassical limit, not the quantum mechanics itself, exhibits chaos. This distinction is crucial and has profound implications for understanding the quantum-classical transition.

---

## Historical Context

By the late 1980s, the field of quantum chaos had produced many results but remained conceptually confused. Researchers spoke of "quantum chaos" without clearly defining what they meant. Naively, one might ask: if quantum mechanics is unitary and reversible, how can it be chaotic (sensitive dependence on initial conditions)?

The resolution came in stages: The quantum Hall effect (1980s) showed that quantum systems can encode classical chaos in their spectral statistics. Gutzwiller's trace formula (1971) provided a bridge via periodic orbits. But the foundational question remained philosophical: what does it mean for a quantum system to be "chaotic"?

Berry's 1987 Bakerian Lecture systematically addressed this confusion. He argued that the term "quantum chaos" is oxymoronic—quantum mechanics is never chaotic, but the quantum properties of classically chaotic systems are highly structured and nontrivial. The proper term is "quantum chaology": the science of quantum systems whose classical limits are chaotic.

---

## Key Arguments and Derivations

### The Quantum Determinism Argument

The time-dependent Schrodinger equation is:

$i\hbar \frac{\partial |\psi(t)\rangle}{\partial t} = H |\psi(t)\rangle$

This is deterministic: given $|\psi(0)\rangle$, the future state is uniquely determined by:

$|\psi(t)\rangle = e^{-iHt/\hbar} |\psi(0)\rangle$

The evolution operator $U(t) = e^{-iHt/\hbar}$ is unitary: $U^{\dagger}U = 1$. This means information is conserved and time evolution is reversible. There is no exponential divergence of nearby states in Hilbert space.

Classical chaos, by contrast, is characterized by Lyapunov exponents $\lambda > 0$:

$|\delta x(t)| \sim |\delta x(0)| e^{\lambda t}$

Nearby initial conditions diverge exponentially. This cannot happen in quantum mechanics because unitary evolution preserves the norm of state vectors.

Therefore, **quantum mechanics itself is not chaotic**. The confusion arises from conflating different aspects of the quantum-classical correspondence.

### Quantum Analogs of Classical Chaos

If quantum mechanics is not chaotic, how do we characterize quantum systems whose classical limits are chaotic? Berry identified three main quantum signatures:

**1. Level spacing statistics**: For a chaotic classical system, the quantum energy levels show level repulsion (Wigner-Dyson statistics). The spacing distribution near zero is:

$P(s) \sim s^{\beta}$ (Gaussian Orthogonal Ensemble, $\beta = 1$)

rather than Poisson ($P(s) = e^{-s}$) for integrable systems.

**2. Scattering time delays**: In a scattering problem, the quantum time delay (Eisenbud-Wigner time delay) is:

$\tau(E) = \hbar \frac{d\phi(E)}{dE}$

where $\phi(E)$ is the scattering phase shift. For chaotic scattering, $\tau(E)$ exhibits large fluctuations and a distribution with long tails, unlike integrable scattering.

**3. Form factors and correlations**: The spectral form factor is:

$K(k) = \frac{1}{N} |\sum_{n} e^{2\pi i k E_n}|^2$

For chaotic systems, $K(k)$ follows predictions from random matrix theory (dip at small $k$, smooth at large $k$). For integrable systems, $K(k)$ shows oscillations from periodic orbits.

### The Gutzwiller Trace Formula

The bridge between classical and quantum chaos is the Gutzwiller trace formula:

$\rho(E) = \rho_{\text{smooth}}(E) + \sum_{p} A_p e^{iS_p(E)/\hbar}$

where $\rho(E)$ is the density of states, $\rho_{\text{smooth}}$ is the smooth (Weyl) part, and the sum is over all periodic orbits $p$ of the classical system. $S_p(E)$ is the action (phase space integral) along periodic orbit $p$, and $A_p$ encodes the stability of the orbit.

For a chaotic system with many periodic orbits, the oscillatory sum becomes a quasi-random superposition of phases. This quasi-randomness manifests as the random matrix statistics observed in level spacings.

For an integrable system, only a few periodic orbits exist (closed tori), so the oscillatory sum is structured, producing oscillations in the level spacing statistics.

### Semiclassical Chaos vs Quantum Determination

The resolution of the apparent paradox is that **chaos appears in the semiclassical limit $\hbar \to 0$**, not in quantum mechanics itself. In the limit of large action (small $\hbar$), quantum mechanics becomes increasingly sensitive to fine details of the initial conditions and the semiclassical trajectories become chaotic.

More precisely, the quantum mechanical propagator is:

$K(x, x'; t) = \int (Dx) e^{iS[x(t)]/\hbar}$

In the semiclassical limit, saddle-point approximation picks out classical trajectories with stationary phase. For chaotic systems, there are exponentially many such trajectories, and their interference produces complex patterns. The quantum outcome depends sensitively on which classical paths contribute most—an apparent "quantum sensitivity" that is actually a semiclassical phenomenon.

### The Distinction: Three Regimes

Berry clarified that the quantum-classical correspondence has three regimes:

1. **Classical limit ($\hbar \to 0$)**: Chaotic systems exhibit exponential sensitivity to perturbations. Quantum corrections are small.

2. **Semiclassical regime ($\hbar$ small but nonzero)**: The WKB approximation is valid, and quantum mechanics can be understood via classical trajectories. Many trajectories contribute to quantum paths, leading to quantum signatures of classical chaos (level repulsion, scattering correlations).

3. **Deep quantum regime ($\hbar$ comparable to action)**: Quantum mechanics is fully wave-like. There is no classical limit, and the notion of classical chaos becomes meaningless. Quantum mechanics is deterministic and reversible.

Most experiments and practical systems operate in regime 2, explaining why classical chaos has such profound quantum mechanical signatures.

---

## Key Results

1. **"Quantum chaology, not quantum chaos"** — Quantum mechanics is deterministic; chaos appears only in the behavior of quantum systems whose classical limit is chaotic.

2. **Three quantum signatures of classical chaos**:
   - Level statistics follow Wigner-Dyson (random matrix) ensemble
   - Scattering time delays show large fluctuations and non-Poisson statistics
   - Spectral correlations exhibit the "dip" and saturation predicted by random matrix theory

3. **Semiclassical origin**: Chaos in quantum systems is fundamentally a semiclassical phenomenon, arising from the exponential proliferation of classical paths in the path integral.

4. **Trace formula universality**: The Gutzwiller trace formula connects periodic orbits to spectral oscillations, explaining level statistics as interference of classical trajectories.

5. **Reversibility and information**: Despite quantum signatures of chaos, quantum evolution remains reversible. Information about initial conditions is never lost; it becomes increasingly fine-grained (encoded in phases and correlations).

---

## Impact and Legacy

Berry's distinction between "quantum chaos" and "quantum chaology" resolved decades of philosophical confusion in the field. His careful language became standard:

- **Foundational clarity**: Distinguished between quantum mechanical reversibility (always true) and quantum signatures of classical chaos (level repulsion, spectral forms).
- **Periodic orbit theory**: Elevated the Gutzwiller trace formula from a technical result to the central conceptual tool linking classical orbits to quantum spectra.
- **Random matrix theory**: Explained the empirical success of random matrix ensembles in nuclear and atomic spectroscopy as a consequence of classical chaos in the underlying dynamics.
- **Scattering theory**: Extended the chaos-to-quantum correspondence to scattering amplitudes and time delays, showing the signature in observable quantities.
- **Thermalization and equilibration**: The framework clarified how isolated quantum systems can appear to equilibrate (through level statistics and mixing) while remaining fully reversible.

The Bakerian Lecture became a canonical reference for any discussion of quantum chaos, and Berry's terminology ("chaology") became standard in the literature.

---

## Connection to Phonon-Exflation Framework

In the phonon-exflation model, the internal compactification geometry (SU(3) with parameter $s$) can be treated as a dynamical system. The question arises: is the classical limit of this internal geometry chaotic or integrable?

1. **Spectral statistics of the Dirac operator**: The eigenvalues of $D_s$ (the Dirac operator on deformed SU(3)) can be studied for level spacing statistics. If the internal classical dynamics is chaotic, we expect Wigner-Dyson statistics and strong level repulsion. If integrable, Poisson statistics. This test determines whether the internal geometry is "chaotic" or "ordered."

2. **Semiclassical phonons**: In the effective description where phonons are quasiparticles in the internal space, the phonon-phonon interactions correspond to a classical phase space. If this classical phase space is chaotic, phonon properties encode quantum signatures of chaos (level repulsion in the phonon spectrum, scattering correlations, etc.).

3. **Avoided crossings and periodic orbits**: The avoided crossings in the Dirac spectrum as $s$ varies (e.g., the (3,0)-(2,0) crossing near $s = 0.15$) can be analyzed via the Gutzwiller trace formula. If numerous periodic orbits contribute, the spectrum is chaotic; if few, integrable.

4. **Spectral action sensitivity**: The spectral action $S_{\text{spec}} = \text{Tr} f(D^2/\Lambda^2)$ depends sensitively on the eigenvalue distribution. If the spectrum has chaos-induced level repulsion, the spectral action will show enhanced sensitivity to perturbations to the geometry.

5. **Implications for stability**: If the internal dynamics are chaotic (Wigner-Dyson statistics), the phonon spectrum is more robust against perturbations. If integrable (Poisson statistics), small perturbations could more easily shift energy levels. This has implications for the stabilization of the cosmological modulus $s$.

The Berry-Tabor conjecture (integrability -> Poisson) and this Bakerian Lecture (chaos -> Wigner-Dyson) provide the framework for testing whether the phonon-exflation internal geometry is fundamentally ordered or chaotic.
