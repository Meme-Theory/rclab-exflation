# Vacuum Energy and Cosmological Constant: View from Condensed Matter

**Author(s):** Grigory E. Volovik
**Year:** 2005
**Journal:** Annalen der Physik, 517(3), 165-176
**arXiv:** gr-qc/0405012, gr-qc/0101111

---

## Abstract

This landmark paper applies condensed matter physics to solve the cosmological constant problem. Volovik demonstrates that in a quantum liquid (superfluid or Bose gas) with no external perturbations, the vacuum energy density is exactly zero without any fine-tuning. However, four types of perturbations induce nonzero vacuum energy:

1. External forces acting on the liquid
2. Presence of quasiparticles (matter)
3. Space-time curvature
4. Boundaries (Casimir effect)

The key insight: **In each epoch of cosmic history, the vacuum energy density is of order the energy density of the dominant perturbation** — either matter density, radiation density, curvature energy, or boundary contributions. This naturally explains why the observed cosmological constant is small and why its magnitude tracks other energy components (the coincidence problem).

The paper bridges quantum field theory, particle physics, and cosmology by treating the vacuum as a **quantum liquid rather than an infinite sea of virtual particles**. This perspective fundamentally reframes the cosmological constant problem.

---

## Historical Context

The cosmological constant problem is arguably the deepest mystery in physics. Einstein (1917) introduced $\Lambda$ to achieve a static universe. When Hubble discovered expansion (1929), Einstein called the introduction of $\Lambda$ his "greatest blunder" — yet it reappeared as observations of accelerating expansion (1998) demanded its existence.

The mystery comes in two parts:

### The "Old" Cosmological Constant Problem

Why is the cosmological constant so **small relative to its theoretical value**?

In quantum field theory, the vacuum energy is the sum of zero-point energies of all quantum fields:

$$\rho_{vac,QFT} = \sum_i \frac{\hbar \omega_i}{2}$$

The sum diverges at high energies. If we cut it off at the Planck scale $E_P = 1.22 \times 10^{19}$ GeV, we get:

$$\rho_{vac,QFT} \sim \left(\frac{E_P}{\hbar c}\right)^4 \sim 10^{113} \text{ J/m}^3$$

But observation gives $\rho_\Lambda \sim 10^{-9} \text{ J/m}^3$ (energy density needed to explain acceleration). The ratio is $10^{122}$ — the worst prediction in physics.

### The "New" Cosmological Constant Problem (Coincidence)

Why are we living at the epoch when matter density $\rho_m$ and vacuum density $\rho_\Lambda$ are comparable?

$$\frac{\rho_\Lambda}{\rho_m} \sim 0.7 \text{ today}$$

If $\rho_\Lambda$ is a true constant and $\rho_m \propto a^{-3}$ (decaying with expansion), their ratio changes dramatically with cosmic time. That we observe them equal is a 1-in-$10^{60}$ coincidence.

### Volovik's Condensed Matter Perspective

By 2005, Volovik had completed decades of research on superfluidity, showing that gravity and spacetime geometry **emerge** from condensed matter physics. This paper extends that insight to the vacuum energy problem.

The core realization: **The quantum vacuum is not an infinite Dirac sea but a macroscopic quantum system** — a superfluid-like condensate filling spacetime. In superfluid physics, the vacuum energy (zero-point energy) is exactly known and calculable.

---

## Key Arguments and Derivations

### Part I: Vacuum Energy in Quantum Liquids

#### The Superfluid Ground State

Consider a weakly interacting Bose gas (superfluid or condensate) with Hamiltonian:

$$H = \sum_i \frac{{\bf p}_i^2}{2m} + \frac{g}{2N} \sum_{i \neq j} \delta({\bf r}_i - {\bf r}_j)$$

where $g$ is the interaction strength and $N$ is the particle number. The ground state is a Bose-Einstein condensate with all particles in the zero-momentum state $|0\rangle$.

The zero-point energy per particle in a box of volume $V$ is:

$$E_0 = \frac{1}{N} \langle 0 | H | 0 \rangle$$

This is **finite and well-defined** — no ultraviolet divergence. The ground state energy depends on density and interaction strength, both microscopic parameters.

Crucially: if the system is isolated and uniform (no external forces, no boundaries, no particles in excited states), then $E_0$ is **exactly zero by definition of the ground state**. The energy is relative — we always measure energy differences, never absolute energy.

#### Vacuum Energy Density

In the condensed matter analogy, the "vacuum" is the ground state of the superfluid. The vacuum energy density is:

$$\rho_\Lambda = \frac{E_0}{V}$$

For an isolated, uniform superfluid: $\rho_\Lambda = 0$ exactly.

For a superfluid with perturbations, we compute the energy of the perturbed state and subtract the ground state energy. The **vacuum energy is entirely perturbative** — it arises from deviations from perfect uniformity and isolation.

### Part II: Four Sources of Vacuum Energy

#### 1. External Forces

Suppose an external potential $U({\bf r})$ acts on the superfluid. The Hamiltonian becomes:

$$H = \sum_i \left(\frac{{\bf p}_i^2}{2m} + U({\bf r}_i)\right) + \ldots$$

The ground state shifts. The vacuum energy density is no longer zero; it is of order:

$$\rho_\Lambda^{(ext)} \sim \frac{\text{energy of external field}}{V}$$

For gravity to couple, we need spacetime curvature or tidal forces — these act as external potentials on the vacuum.

#### 2. Quasiparticles (Matter)

In a superfluid at finite temperature, excited quasiparticles (phonons, rotons) are present. Each quasiparticle carries energy $\epsilon_k$ and contributes to the vacuum energy:

$$\rho_\Lambda^{(quasi)} = \sum_k n_k \epsilon_k$$

where $n_k$ is the occupation number. At low density of excitations:

$$\rho_\Lambda^{(quasi)} \sim n_{quasi} \times \epsilon_{typical} \sim \rho_{matter}$$

This is the key insight: **The vacuum energy is proportional to the matter density**.

#### 3. Spacetime Curvature

In a curved spacetime, the superfluid experiences an effective "deformation." The effective metric modifies the quasiparticle spectrum. The Riemann curvature tensor acts as an inhomogeneous perturbation:

$$\rho_\Lambda^{(curv)} \sim \frac{R}{\ell_P^2} \times E_P$$

where $R$ is the scalar curvature and $\ell_P$ is the Planck length. This gives a vacuum energy proportional to the curvature energy:

$$\rho_\Lambda^{(curv)} \sim \rho_{curv}$$

#### 4. Boundaries and Casimir Effect

Finite-size effects and boundaries (e.g., a cavity in the superfluid) introduce surface energy. The Casimir effect in QED and the Casimir-like effect in superfluids produce vacuum energy contributions proportional to the boundary energy.

### Part III: The Coincidence Problem Solved

In an epoch where matter dominates ($\rho_m >> \rho_r, \rho_\Lambda$), the vacuum energy is:

$$\rho_\Lambda \sim \rho_m$$

by mechanism (2) above. Thus:

$$\frac{\rho_\Lambda}{\rho_m} \sim 1$$

In an epoch where radiation dominates:

$$\rho_\Lambda \sim \rho_r$$

Thus:

$$\frac{\rho_\Lambda}{\rho_m} = \frac{\rho_r}{\rho_m}$$

which evolves as $\propto a$ (rises as the universe expands and matter dilutes faster than radiation).

In an epoch where curvature dominates (early universe):

$$\rho_\Lambda \sim \rho_{curv}$$

These mechanisms explain why $\rho_\Lambda / \rho_m \sim \mathcal{O}(1)$ is **generic and unsurprising**. We are not at a special time — the coincidence is natural.

### Part IV: Absence of Fine-Tuning

Volovik's approach avoids the $10^{122}$ mismatch by rejecting the QFT premise that vacuum energy is a sum of infinitely many virtual particle energies. Instead:

- The "true" Theory of Everything (quantum liquid at Planck scale) has zero vacuum energy in the absence of perturbations.
- The effective low-energy field theory (QFT in 4D) emerges from this, and vacuum energy arises only from perturbations.
- No ultraviolet divergence; no cutoff; no mysterious cancellations required.

The cosmological constant is not a fundamental constant but a **derived quantity**, determined by the matter and curvature content of the universe.

---

## Key Results

1. **Vacuum energy is zero in an isolated, uniform quantum liquid**: No fine-tuning required. The ground state energy is a reference point, not a physical observable.

2. **Vacuum energy arises from four perturbations**: matter, curvature, external fields, boundaries. Each contributes proportionally to its own energy scale.

3. **The coincidence problem is solved**: $\rho_\Lambda$ is naturally of order $\rho_{matter}$ (or $\rho_{radiation}$, or $\rho_{curv}$), making their ratio $\sim 1$ generic.

4. **No ultraviolet catastrophe**: The condensed matter perspective avoids summing infinitely many virtual particle modes. The theory is well-defined at all scales.

5. **Predictions are testable**: The vacuum energy should evolve with cosmic history, tracking the dominant energy component. Current observations (dark energy not quite constant, possible time variation) may support this.

---

## Impact and Legacy

This paper has been cited over 500 times (as of 2025), inspiring:

- **Emergent gravity programs**: Sakharov-type induced gravity, holographic approaches to the cosmological constant.

- **Quintessence and dark energy models**: The idea that dark energy is dynamical (not a static constant) echoes Volovik's mechanism that $\rho_\Lambda$ depends on the matter content.

- **Effective field theory perspective**: Modern effective field theory approaches to dark energy acknowledge that the "vacuum energy" is an effective concept, not fundamental.

- **Quantum simulation of cosmology**: Experimental proposals to simulate cosmological expansion in ultracold atoms and condensates, inspired by Volovik's conceptual framework.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model proposes that dark energy arises from the spectral action on the internal SU(3) geometry, not from a fundamental cosmological constant. This aligns directly with Volovik's mechanism:

1. **Zero vacuum energy in a translationally invariant system**: The BCS condensate on SU(3) has zero energy density in a perfect ground state, analogous to Volovik's isolated superfluid.

2. **Perturbations induce vacuum energy**: The expansion of the universe, the presence of matter quanta (phonon excitations), and the curvature of spacetime all act as perturbations that induce an effective dark energy density.

3. **Spectral action as the perturbation energy**: The spectral action monotonically increases with the scale of the SU(3) geometry, acting as a natural source of vacuum energy that scales with the "matter" (phononic quanta) and curvature.

4. **Coincidence problem solved**: If dark energy arises from the spectral action's dependence on the condensate structure and expansion rate, its magnitude tracking the matter density is natural — not a coincidence.

5. **Testable predictions**: Both Volovik's condensed matter vacuum and phonon-exflation's spectral action predict **time variation in the dark energy equation of state**, potentially observable by DESI and other surveys.

---

## References

- Volovik, G. E. (2005). "Vacuum energy and cosmological constant: view from condensed matter." *Annalen der Physik*, 517(3), 165-176. arXiv:gr-qc/0405012.

- Volovik, G. E. (2001). "Vacuum energy and cosmological constant: View from condensed matter." *Journal of Low Temperature Physics*, 124(3), 23-39. arXiv:gr-qc/0101111.

- Weinberg, S. (2000). "The cosmological constant problems." arXiv preprint astro-ph/0005265.

- Carroll, S. M., Hoffman, M., & Trodden, M. (2003). "Can the dark energy equation-of-state parameter $w$ be less than $-1$?" *Physical Review D*, 68(2), 023509.
