# Feynman (1949) — "The Theory of Positrons"

**Citation**: R. P. Feynman, *Phys. Rev.* **76**, 749 (Sept. 15, 1949). Cornell University. Received April 8, 1949. 11 pages + appendix.

---

## 1. Core Thesis

Feynman replaces Dirac's hole theory (second quantization of the electron field with a filled negative-energy sea) by a reinterpretation of solutions to the Dirac equation itself. Positrons are not missing electrons in a filled sea — they are electrons whose world-lines are directed backward in time. The over-all space-time picture (Stückelberg) supersedes the Hamiltonian time-evolution picture.

Key operational claim proved in the Appendix: this one-particle reinterpretation is mathematically equivalent to hole theory / second quantization, provided the propagator is chosen with the correct analytic prescription.

---

## 2. Technical Structure

### 2.1 The Propagator K_+ (p. 752, Eq. 17)

The central object. Defined so that
- for t₂ > t₁: K_+(2,1) sums over positive-energy Dirac eigenstates propagating forward,
- for t₂ < t₁: K_+(2,1) is the negative of a sum over negative-energy eigenstates (i.e., the positron amplitude propagating backward).

This analytic splitting is what distinguishes K_+ from K_0, and is the origin of the iε prescription.

### 2.2 The Perturbation Expansion (p. 752, Eqs. 13–16)

$$K_+^{(A)}(2,1) = K_+(2,1) - i \int K_+(2,3)\, A(3)\, K_+(3,1)\, d\tau_3 + (-i)^2 \iint K_+(2,4)\, A(4)\, K_+(4,3)\, A(3)\, K_+(3,1)\, d\tau_4 d\tau_3 + \cdots$$

Each insertion of A is a vertex; each K_+ a propagator leg. This is the prototype Feynman expansion. Every term automatically includes virtual pair creation/annihilation — no separate hole-theory bookkeeping required.

### 2.3 Momentum-Space Form (p. 757, Eqs. 31–32)

$$K_+(2,1) = \frac{i}{4\pi^2} \int (\not p - m)^{-1}\, e^{-ip\cdot x_{21}}\, d^4p$$

with the iδ prescription m → m − iδ selecting the correct contour around the poles at p² = m². Note: $(\not p - m)^{-1} = (\not p + m)(p^2 - m^2)^{-1}$ — the on-shell condition is a scalar pole, not a matrix pole.

### 2.4 Many-Particle Amplitude (p. 755, Eqs. 27)

For two charges: $K(3,4;1,2) = K_{+a}(3,1)\,K_{+b}(4,2) - K_{+a}(4,1)\,K_{+b}(3,2)$. Antisymmetrization enforces Pauli only on external states. Intermediate states in K_+ automatically handle the sea correctly — a major computational simplification.

### 2.5 Vacuum-to-Vacuum Amplitude (p. 756, Eq. 30)

$$C_v = \exp(-L), \qquad L = \sum_n L^{(n)}$$

where $L^{(1)} = -\tfrac{1}{2}\iint \mathrm{Sp}[K_+(2,1) A(1) K_+(1,2) A(2)]\, d\tau_1 d\tau_2$ is the one-loop closed-fermion amplitude. The minus sign of L (fermions) vs the would-be plus sign (bosons) is a direct consequence of the Pauli principle acting on exchange in closed loops.

$P_v = |C_v|^2 = \exp(-2\,\mathrm{Re}\,L)$ is the vacuum-persistence probability. Im(L) is infinite at one loop (the first vacuum-polarization divergence); Feynman notes this will require renormalization in the sequel paper.

---

## 3. Relevance to the Phonon-Exflation Framework

★ Insight ─────────────────────────────────────
The framework's permanent result [J, D_K] = 0 (charge-conjugation commutes with the Dirac operator at the spectral-triple level) is the NCG-native form of exactly what Feynman did in 1949: antimatter is not a separate sector, it is an analytic/spectral property of the same operator governing matter. Feynman achieved it via contour prescription; Connes-style NCG achieves it via the real structure J on the spectral triple.
─────────────────────────────────────────────────

Five structural connections, in order of decreasing directness:

### 3.1 CPT and [J, D_K] = 0 (Permanent Result)

Feynman's positron-as-backward-electron is the spacetime-embedded expression of what the substrate encodes as the real structure J acting on D_K. The framework's result that J and D_K commute (permanent-results registry) is the spectral-triple formalism of Feynman's claim that the same propagator kernel handles both particle directions. Feynman needs the iε prescription; the substrate gets it for free from KO-dim = 6 and [J, D_K] = 0.

### 3.2 Propagator ↔ Resolvent of D_K

The Feynman propagator K_+(2,1) = ⟨2 | (D − iε)^(−1) | 1⟩ is the time-ordered resolvent of the Dirac operator. In the substrate framework, $(D_K - \lambda)^{-1}$ is the spectral object whose trace gives the spectral action. The propagator expansion Feynman wrote IS the perturbative expansion of the spectral action around a flat-fiber reference. The S34+ spectral-action computations on the 155,984-eigenvalue D_K are, in this sense, non-perturbative completions of Feynman's 1949 series.

### 3.3 Relay Patterns ↔ Particle Paths

The framework's relay-pattern picture (particles = propagating excitations of the fiber through the gauge connection between fibers) is the substrate-native form of Feynman's sum-over-paths. Each "path" in Feynman is a spectral trajectory through D_K's eigenbasis; the relay pattern is the physical realization of that trajectory in the fiber bundle.

### 3.4 Exclusion-Principle-Free Intermediate States

Feynman's demonstration (§4, p. 755) that the exclusion principle need NOT be enforced in intermediate states because K_+ already encodes it — this is a methodological gift to the substrate framework. When computing multi-particle spectral processes on D_K, we can use the raw spectral propagator without antisymmetrizing intermediate sums, provided our K_+-analog is built from the J-symmetric spectral decomposition. This significantly simplifies any future multi-excitation substrate calculation.

### 3.5 Vacuum Loops and the Spectral a_0 Moment

Feynman's closed-loop sum L gives the vacuum persistence amplitude. In the substrate framework, the analogous object is the zeroth Seeley-DeWitt coefficient a_0 — the cosmological-constant moment of D_K. Feynman's 1949 result that L is UV-divergent is the 1949 shadow of the same problem the substrate framework confronts at the spectral level (CC hierarchy, spectral-post-mortem result from S36, re-derived S77). The sign structure is inherited: exp(−L) for fermions, exp(+L) for bosons ↔ KO-dim-6 supertrace structure in the spectral action.

---

## 4. Explicit Framework Mappings (terminology translation)

| Feynman 1949 term | Substrate-framework term |
|---|---|
| Positron | J-conjugate of electron eigenstate; [J, D_K]=0 ensures pairing |
| K_+(2,1) with iε | Time-ordered resolvent of D_K |
| Perturbation series in A | Spectral-action expansion in gauge fluctuation $\omega = [D_K, a]$ |
| Vacuum loop L | Contribution to a_0 Seeley-DeWitt moment |
| Pauli sign in loops | KO-dim-6 supertrace sign in Tr(f(D_K/Λ)) |
| Stückelberg backward-in-time | Spectral action is direction-agnostic; J implements it geometrically |
| Divergence of Im(L) | CC-hierarchy problem; spectral regularization required |

---

## 5. Historical/Methodological Note for the Project

This paper is the first of Feynman's 1949 pair; the companion "Space-Time Approach to Quantum Electrodynamics" (Phys. Rev. 76, 769) adds the photon, diagrammatics proper, and the UV renormalization. For the substrate framework, this first paper is the more foundational one because the substrate doesn't second-quantize a field on top of a fixed vacuum — it works with one Dirac operator whose spectrum IS the particle content. Feynman's first-paper program (derive QED from solutions to Dirac's equation rather than from field operators) is structurally closer to the NCG/spectral-triple program than standard canonical QFT is.

---

## 6. What This Paper Does NOT Contribute

- No self-energy or vertex renormalization (that's the Sept. 15 companion paper, Phys. Rev. 76, 769).
- No treatment of gauge-field quantization — the EM field here is a fixed external A_μ.
- No thermal or finite-density physics.
- No connection to gravitation. The Lorentz structure is flat-space throughout.
