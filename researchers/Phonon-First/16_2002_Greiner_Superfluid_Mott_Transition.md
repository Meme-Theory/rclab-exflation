# Quantum phase transition from a superfluid to a Mott insulator in a gas of ultracold atoms

**Author(s):** Markus Greiner, Olaf Mandel, Tilman Esslinger, Theodor W. Hansch, Immanuel Bloch
**Year:** 2002
**Journal:** Nature 415, 39-44 (2002)
**arXiv:** 2506.21303 (re-posted)
**Relevance:** HIGH

---

## Abstract

For a system at a temperature of absolute zero, all thermal fluctuations are frozen out, while quantum fluctuations prevail. These microscopic quantum fluctuations can induce a macroscopic phase transition in the ground state of a many-body system when the relative strength of two competing energy terms is varied across a critical value. Here we observe such a quantum phase transition in a Bose-Einstein condensate with repulsive interactions, held in a three-dimensional optical lattice potential. As the potential depth of the lattice is increased, a transition is observed from a superfluid to a Mott insulator phase. In the superfluid phase, each atom is spread out over the entire lattice, with long-range phase coherence. But in the insulating phase, exact numbers of atoms are localized at individual lattice sites, with no phase coherence across the lattice; this phase is characterized by a gap in the excitation spectrum. We can induce reversible changes between the two ground states of the system.

---

## Key Arguments and Derivations

### 1. The Bose-Hubbard Model
The physics is captured by the Bose-Hubbard Hamiltonian:
$$H = -J\sum_{\langle i,j\rangle} \hat{a}^\dagger_i \hat{a}_j + \sum_i \epsilon_i \hat{n}_i + \frac{1}{2}U\sum_i \hat{n}_i(\hat{n}_i - 1)$$
where $\hat{a}^\dagger_i$, $\hat{a}_i$ are bosonic creation/annihilation operators, $\hat{n}_i = \hat{a}^\dagger_i \hat{a}_i$, $\epsilon_i$ is the energy offset from harmonic confinement, $J$ is the hopping matrix element, and $U$ is the on-site interaction energy.

### 2. Hopping Matrix Element
$$J = -\int d^3x\, w^*(x - x_i)\left[-\frac{\hbar^2}{2m}\nabla^2 + V_{lat}(x)\right]w(x - x_j)$$
where $w(x - x_i)$ is a single-particle Wannier function localized to the $i$th lattice site and $V_{lat}(x)$ is the optical lattice potential.

### 3. On-Site Interaction
$$U = \frac{4\pi\hbar^2 a}{m}\int |w(x)|^4 d^3x$$
where $a$ is the s-wave scattering length.

### 4. The Two Ground States

**Superfluid phase** ($J \gg U$): Kinetic energy dominates. Each atom delocalizes over all $M$ lattice sites:
$$|\Psi_{SF}\rangle_{U=0} \propto \left(\sum_{i=1}^M \hat{a}^\dagger_i\right)^N |0\rangle$$
This is a product of identical Bloch states with Poissonian on-site number fluctuations (Var($n_i$) = $\langle \hat{n}_i \rangle$) and long-range phase coherence.

**Mott insulator phase** ($U \gg J$): Interaction energy dominates. Exact atom number $n$ localized per site:
$$|\Psi_{MI}\rangle_{J=0} \propto \prod_{i=1}^M (\hat{a}^\dagger_i)^n |0\rangle$$
This is a product of Fock states with no phase coherence and a gap $\Delta \approx U$ in the excitation spectrum.

### 5. Quantum Critical Point
In 3D with coordination number $z = 6$ (simple cubic), the transition for $\langle \hat{n}_i \rangle \approx 1$ occurs at:
$$U/J \approx z \times 5.8 \approx 34.8$$

### 6. Optical Lattice Implementation
Three orthogonal standing waves at $\lambda = 852$ nm create a 3D simple cubic potential:
$$V(x,y,z) = V_0[\sin^2(kx) + \sin^2(ky) + \sin^2(kz)]$$
with $k = 2\pi/\lambda$ and $V_0$ measured in units of the recoil energy $E_r = \hbar^2 k^2/(2m)$.

Harmonic trapping frequency per site: $\nu_r \approx (\hbar k^2/2\pi m)\sqrt{V_0/E_r}$, reaching ~30 kHz at $V_0 = 22 E_r$.

### 7. Observation of the Phase Transition

**Interference patterns**: After sudden release and 15 ms time-of-flight:
- At $V_0 \lesssim 13 E_r$: sharp interference maxima (superfluid, phase coherent)
- At $V_0 = 13$--$14 E_r$: maxima weaken, incoherent background grows
- At $V_0 = 20 E_r$: no interference pattern (Mott insulator, no phase coherence)

Key observation: interference peaks show **no broadening** before vanishing -- they disappear into the incoherent background. This is explained by the inhomogeneous system developing alternating Mott insulator and superfluid regions.

### 8. Reversibility: Coherence Restoration
After bringing the system deep into the Mott insulator phase ($V_0 = 22 E_r$) and lowering to $V_0 = 9 E_r$:
- Phase coherence restored after only **4 ms** (comparable to tunneling time $\tau_{tunnel} = \hbar/J \sim 2$ ms)
- Full steady-state interference after 14 ms
- In contrast, a **phase-incoherent state** (created by dephasing) shows **no coherence recovery** even after 400 ms

This proves the Mott insulator state is fundamentally different from a random-phase state -- it is a quantum ground state from which coherence can be rapidly regenerated.

### 9. Excitation Spectrum: Gap Detection
Applying a potential gradient creates particle-hole excitations when the energy difference between neighboring sites equals the on-site energy $U$:
- At $V_0 = 10 E_r$: smooth excitation spectrum (superfluid)
- At $V_0 = 13 E_r$: two broad resonances emerge
- At $V_0 = 20 E_r$: two narrow, well-defined resonances on a flat background

The first resonance confirms the Mott gap $\Delta = U$. The second resonance at $2U$ is attributed to two-particle tunneling or second-order processes. The resonance positions agree with ab initio calculations of $U$ from Wannier functions.

### 10. Transition Point
Experimental transition: between $V_0 = 10 E_r$ and $13 E_r$, corresponding to $U/J \approx 36$ at $V_0 = 13 E_r$ -- in good agreement with the theoretical prediction $U/J \approx 34.8$.

## Key Results

1. First observation of the superfluid-to-Mott insulator quantum phase transition in an atomic gas
2. Transition driven by $U/J$ ratio, observed at $V_0 \approx 12$--$13 E_r$ ($U/J \approx 36$)
3. Coherence restoration from Mott insulator in ~4 ms (one tunneling time) -- vs. never for dephased states
4. Excitation gap $\Delta = U$ directly measured via resonant response to potential gradient
5. Second resonance at $2U$ observed (two-particle processes)
6. Phase transition fully reversible -- system can be driven between superfluid and insulator repeatedly
7. Mott insulator state extremely robust to perturbations except at resonance gradients
8. Transition point agrees quantitatively with Bose-Hubbard model prediction

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Bose-Hubbard Hamiltonian | $H = -J\sum_{\langle i,j\rangle}\hat{a}^\dagger_i \hat{a}_j + \sum_i \epsilon_i \hat{n}_i + \frac{1}{2}U\sum_i \hat{n}_i(\hat{n}_i - 1)$ | Eq. (1) |
| Hopping matrix element | $J = -\int d^3x\, w^*(x-x_i)[-\frac{\hbar^2}{2m}\nabla^2 + V_{lat}(x)]w(x-x_j)$ | Eq. (2) |
| On-site interaction | $U = \frac{4\pi\hbar^2 a}{m}\int\|w(x)\|^4 d^3x$ | Eq. (3) |
| Superfluid ground state | $\|\Psi_{SF}\rangle \propto (\sum_{i=1}^M \hat{a}^\dagger_i)^N\|0\rangle$ | Eq. (4) |
| Mott insulator ground state | $\|\Psi_{MI}\rangle \propto \prod_{i=1}^M (\hat{a}^\dagger_i)^n\|0\rangle$ | Eq. (5) |
| Optical lattice potential | $V(x,y,z) = V_0[\sin^2(kx) + \sin^2(ky) + \sin^2(kz)]$ | Eq. (6) |
| Critical ratio (3D) | $U/J \approx z \times 5.8 \approx 34.8$ | Sec. QPT |
| Recoil energy | $E_r = \hbar^2 k^2/(2m)$ | Sec. Exp |
| Tunneling time | $\tau_{tunnel} = \hbar/J$ | Sec. Restoring |
| Trapping frequency | $\nu_r \approx (\hbar k^2/2\pi m)\sqrt{V_0/E_r}$ | Sec. Exp |

## Relevance to Phonon-Exflation

The superfluid-to-Mott insulator transition is the canonical laboratory realization of the Bose-Hubbard model, which describes the framework's BCS condensate on the SU(3) lattice in the $N_{pair} \sim 1$ regime. The framework's pairing window ($L/\xi_{GL} = 0.031$) places it deep in the zero-dimensional limit where quantum fluctuations dominate -- precisely the regime where the Greiner experiment operates (average $\langle \hat{n}_i \rangle \approx 1$--$3$). The rapid coherence restoration from the Mott state (4 ms, one tunneling time) but permanent incoherence from a dephased state is a direct experimental analog of the framework's prediction that the post-transit GGE state (produced by sudden quench, $P_{exc} = 1.000$) is permanently non-thermal while the Mott-like ground state preserves quantum correlations. The gap $\Delta = U$ maps onto the framework's excitation gap protecting the condensate.
