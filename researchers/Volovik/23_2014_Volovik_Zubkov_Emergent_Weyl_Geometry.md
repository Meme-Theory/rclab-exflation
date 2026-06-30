# Emergent Weyl fermions and the origin of i = sqrt(-1) in quantum mechanics

**Author(s):** G.E. Volovik, M.A. Zubkov
**Year:** 2014
**Journal:** Pis'ma v ZhETF 99, 552-557 (2014); JETP Lett. 99, 481-486 (2014)
**arXiv:** 1404.4084
**Relevance:** HIGH

---

## Abstract

Conventional quantum mechanics is described in terms of complex numbers. However, all physical quantities are real. This indicates that the appearance of complex numbers in quantum mechanics may be the emergent phenomenon, i.e. complex numbers appear in the low energy description of the underlined high energy theory. We suggest a possible explanation of how this may occur. Namely, we consider the system of multi-component Majorana fermions. There is a natural description of this system in terms of real numbers only. In the vicinity of the topologically protected Fermi point this system is described by the effective low energy theory with Weyl fermions. These Weyl fermions interact with the emergent gauge field and the emergent gravitational field.

---

## Key Arguments and Derivations

### Real Microscopic Theory
The system of $N$-component real-valued Majorana spinor $\chi(Q)$ evolves as $\partial_t \chi = \hat{A}\chi$ where $\hat{A}$ is a real operator. The partition function:

$$Z = \int D\psi \exp\left(-\int dt \sum_Q \psi^T_Q(t)(\partial_t + \hat{A})\psi_Q(t)\right)$$

contains no imaginary unit. Only one $N$-component Grassmann spinor $\psi$ appears.

### Reduction to Weyl Spinors
Near a topologically protected Fermi point, the $N$-component system reduces to 4 components (minimum allowed by topology). The block-diagonal form is $A_{\text{block}} = \text{diag}(E_1(P)\hat{i}_{\text{eff}}, E_2(P)\hat{i}_{\text{eff}}, ...)$ where:

$$\hat{i}_{\text{eff}} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \quad \hat{i}^2_{\text{eff}} = -1$$

The effective imaginary unit $i$ emerges from the topology of the Fermi point.

### Emergent Complex Spinors
Introducing two-component spinors from the four real components:

$$\Psi_P = \begin{pmatrix} \psi^1_P + i\psi^2_P \\ \psi^3_P + i\psi^4_P \end{pmatrix}$$

the partition function becomes:

$$Z = \int D\Psi D\bar{\Psi} \exp\left(\frac{i}{2}\int dt \sum_P [\bar{\Psi}_P(i\partial_t - \hat{H})\Psi_P + \text{h.c.}]\right)$$

with Hamiltonian $\hat{H} = m^L_k(P)\hat{\sigma}_k + m(P)$.

### Topological Protection
The Fermi point is protected by the topological invariant:

$$N = \frac{\epsilon_{ijk}}{8\pi} \int_\sigma dS_i \hat{m}^L \cdot \left(\frac{\partial \hat{m}^L}{\partial P_j} \times \frac{\partial \hat{m}^L}{\partial P_k}\right)$$

For $N = \pm 1$, the expansion near the hedgehog point gives the Weyl equation with emergent vierbein $e^j_a$ and emergent U(1) gauge field $B_\mu = p^{(0)}_\mu$.

### Emergent Action
The final action for Weyl fermions in emergent gravity:

$$S = \frac{1}{2}\left(\int dt \, e \sum_X \bar{\Psi}_X(t) e^j_a \hat{\sigma}^a i\hat{D}_j \Psi_X(t) + \text{h.c.}\right)$$

This is teleparallel gravity (torsion without curvature) — the spin connection is absent.

## Key Results

1. Complex numbers in quantum mechanics emerge from real Majorana fermion system
2. The imaginary unit $i_{\text{eff}}$ is a real $2 \times 2$ antisymmetric matrix emerging at the Fermi point
3. Multi-component Majorana fermions reduce to two-component Weyl fermions near topologically protected nodes
4. Emergent gauge field $B_\mu$ and gravitational vierbein $e^j_a$ arise from collective excitations
5. The emergent gravity is teleparallel (Weitzenblock geometry with torsion, no curvature)
6. Weyl equation appears as extremum of the emergent action
7. The hierarchy problem may be solved: masses are small because fermions emerge gapless

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Real partition function | $Z = \int D\psi \exp(-\int dt \sum_Q \psi^T(\partial_t + \hat{A})\psi)$ | Eq. (5) |
| Effective $i$ | $\hat{i}_{\text{eff}} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | Eq. (3) |
| Weyl Hamiltonian | $\hat{H} = m^L_k(P)\hat{\sigma}_k + m(P)$ | Eq. (7) |
| Topological invariant | $N = \frac{\epsilon_{ijk}}{8\pi} \int dS_i \hat{m}^L \cdot (\partial_j \hat{m}^L \times \partial_k \hat{m}^L)$ | Eq. (8) |
| Emergent Weyl action | $S = \frac{1}{2} \int dt \, e \, \bar{\Psi} e^j_a \sigma^a i D_j \Psi + \text{h.c.}$ | Eq. (10) |
| Vierbein from expansion | $m^L_i(P) \approx f^j_i (P_j - P^{(0)}_j)$, $e \cdot e^j_i = f^j_i$ | Eq. (9) |

## Relevance to Phonon-Exflation

- The emergence of complex quantum mechanics from real Majorana fermions is foundational for the framework: it shows that the Standard Model's structure (complex Weyl fermions, gauge fields, gravity) can emerge from a simpler real-valued system
- The topologically protected Fermi point with invariant $N = \pm 1$ corresponds to the framework's Weyl points in the Dirac spectrum on SU(3)
- The emergent teleparallel gravity (torsion without curvature) connects to the framework's elasticity-tetrad gravity from the vacuum crystal
- The reduction from $N$ components to 2 (Weyl) parallels the framework's reduction from the full $\mathbb{C}^{16}$ spinor to the low-energy sector
- The emergent imaginary unit connects to the $\mathbb{Z}_4$ symmetry discussed in paper 18
- The hierarchy problem solution (massless emergence) is precisely the framework's mechanism: particles are gapless excitations near topological nodes
