# Superconductivity in Hyperbolic Spaces: Cayley Trees, Hyperbolic Continuum, and BCS Theory

**Author(s):** Mykhailo Pavliuk, Tomas Bzdusek, Askar Iliasov
**Year:** 2025
**Journal:** [not stated in PDF]
**arXiv:** 2510.26528
**Relevance:** MEDIUM

---

## Abstract

We investigate $s$-wave superconductivity in negatively curved geometries, focusing on Cayley trees and the hyperbolic plane. Using a self-consistent Bogoliubov-de Gennes approach for trees and a BCS treatment of the hyperbolic continuum, we establish a unified mean-field framework that captures the role of boundaries in hyperbolic spaces. For finite Cayley trees with open boundaries, the superconducting order parameter localizes at the edge while the interior can remain normal, leading to two distinct critical temperatures: $T_c^{\text{edge}} > T_c^{\text{bulk}}$. A corresponding boundary-dominated phase also emerges in hyperbolic annuli and horodisc regions, where radial variations of the local density of states enhance edge pairing. We also demonstrate that the enhancement of the density of states at the boundary is significantly more pronounced for the discrete tree geometry. Our results show that, owing to the macroscopic extent of the boundary, negative curvature can stabilize boundary superconductivity as a phase that persists in the thermodynamic limit on par with the bulk superconductivity. These results highlight fundamental differences between bulk and boundary ordering in hyperbolic matter, and provide a theoretical framework for future studies of correlated phases in negatively curved systems.

---

## Key Arguments and Derivations

### Section II: Tree Graphs

#### IIA: Bethe Lattices (Uniform Case)

Starting from the attractive Hubbard model $H = t\sum_{\langle i,j\rangle\sigma} c_{i\sigma}^\dagger c_{j\sigma} - \mu\sum_{i\sigma} n_{i\sigma} + U\sum_i n_{i\uparrow}n_{i\downarrow}$ ($U > 0$), the BdG approach on vertex-transitive graphs yields the standard BCS gap equation in terms of the density of states:

$\Delta = U\int_{-\infty}^{\infty} \frac{\Delta\nu(\lambda)}{2\sqrt{(\lambda-\mu)^2 + \Delta^2}} \tanh\frac{\sqrt{(\lambda-\mu)^2 + \Delta^2}}{2T} d\lambda$

For the Bethe lattice with connectivity $K$ (degree $q = K+1$), the density of states is $\nu_K(\lambda) = \frac{1}{2\pi}\frac{\sqrt{4K - \lambda^2}}{(K+1)^2 - \lambda^2}$, and the weak-coupling critical temperature follows $T_c \sim e^{-1/U\nu(\mu)}$.

#### IIB: Cayley Trees (Open Boundaries)

For finite Cayley trees, a symmetry-adapted block decomposition is introduced. The tree is divided into radial shells $S_l$, and the Hamiltonian is written using forward/backward propagation operators $P_l, P_l^\dagger$. Symmetric and nonsymmetric basis states are constructed following the Lanczos algorithm, block-diagonalizing the BdG Hamiltonian.

Key finding: two distinct critical temperatures emerge -- $T_c^{\text{edge}} > T_c^{\text{bulk}}$. The ratio of boundary to bulk critical temperatures is significantly higher than in flat (Euclidean) systems. The order parameter localizes at the boundary while the bulk remains normal in an intermediate temperature range.

### Section III: Continuous Hyperbolic Spaces (BCS Treatment)

The BCS gap equation is formulated for the hyperbolic continuum using the metric tensor on a two-dimensional manifold with negative curvature. Exact calculations of the local density of states in the horodisc region show boundary enhancement controlled by the curvature. Small curvature gives boundary enhancement analogous to flat 2D systems; the extremely curved limit gives stronger amplification analogous to flat 1D systems. Numerical solutions confirm robust boundary-localized superconductivity persisting above the bulk $T_c$.

## Key Results

1. The BCS gap equation on uniform (vertex-transitive) lattices depends only on the single-particle density of states, reproducing the standard BCS theory. Curvature enters solely through the DOS.
2. On finite Cayley trees with open boundaries, two distinct superconducting transitions exist: $T_c^{\text{edge}} > T_c^{\text{bulk}}$, with the order parameter localized at the boundary in the intermediate regime.
3. The boundary-to-bulk critical temperature ratio is significantly enhanced in hyperbolic geometry compared to Euclidean systems, because the boundary constitutes a macroscopic fraction of the volume.
4. Boundary superconductivity persists in the thermodynamic limit as a stable phase, on par with bulk superconductivity.
5. The discrete tree geometry provides more pronounced LDOS enhancement at the boundary than the continuum hyperbolic plane.
6. The symmetry-adapted block decomposition enables self-consistent BdG calculations for trees with $\sim 10^{100}$ sites.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Hubbard model | $H = t\sum_{\langle i,j\rangle\sigma} c_{i\sigma}^\dagger c_{j\sigma} - \mu\sum_{i\sigma} n_{i\sigma} + U\sum_i n_{i\uparrow}n_{i\downarrow}$ | Eq. (1) |
| BdG eigenvalue eq. | $H_{\text{BdG}}\binom{u_n}{v_n} = \begin{pmatrix} h-\mu & \Delta \\ \Delta & -h+\mu \end{pmatrix}\binom{u_n}{v_n} = E_n\binom{u_n}{v_n}$ | Eq. (2) |
| Self-consistency | $\Delta_i = \frac{U}{2}\sum_n u_{n,i}v_{n,i}^* \tanh\frac{E_n}{2T}$ | Eq. (3) |
| BCS gap equation | $\Delta = U\int_{-\infty}^{\infty} \frac{\Delta\nu(\lambda)}{2\sqrt{(\lambda-\mu)^2+\Delta^2}}\tanh\frac{\sqrt{(\lambda-\mu)^2+\Delta^2}}{2T}d\lambda$ | Eq. (4) |
| Weak-coupling $T_c$ | $T_c \sim e^{-1/U\nu(\mu)}$ | Eq. (5) |
| Bethe lattice DOS | $\nu_K(\lambda) = \frac{1}{2\pi}\frac{\sqrt{4K-\lambda^2}}{(K+1)^2-\lambda^2}$ | Eq. (6) |
| Bethe lattice gap | $\Delta = \frac{U}{4\pi}\int_{-2\sqrt{K}}^{2\sqrt{K}} \frac{\Delta\sqrt{4K-\lambda^2}}{[(K+1)^2-\lambda^2]\xi(\lambda,\Delta)}\tanh\frac{\xi(\lambda,\Delta)}{2T}d\lambda$ | Eq. (7) |
| Shell Hamiltonian | $H = P_0 + \sum_{l=1}^{M-1}(P_l^\dagger + P_l) + P_M^\dagger$ | Eq. (9) |

## Relevance to Phonon-Exflation

This paper establishes BCS superconductivity on curved spaces with rigorous mean-field theory, directly relevant to the phonon-exflation framework's BCS condensate on $SU(3)/T$. The key insight -- that curvature enters the gap equation solely through the density of states -- validates the framework's approach of computing the DOS on the internal manifold and feeding it into a BCS gap equation. The boundary superconductivity phenomenon (two distinct $T_c$'s, edge-localized order parameter) has a potential analog in the framework where the "boundary" of the instanton gas region in tau-space could support enhanced pairing. The symmetry-adapted block decomposition technique may be applicable to the shell structure of $SU(3)/T$ under the Ricci flow.
