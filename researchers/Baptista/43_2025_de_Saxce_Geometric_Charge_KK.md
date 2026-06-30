# Electric? Then it is geometric

**Author(s):** G. de Saxce
**Year:** 2025
**Journal:** arXiv preprint (presented at 66th Souriau Colloquium, Bastia, 2024 and GDR CNRS 2043, La Rochelle, 2024)
**arXiv:** 2503.08718
**Relevance:** MEDIUM

---

## Abstract

In this work, we revisit Kaluza-Klein theory from the perspective of the classification of elementary particles based on the coadjoint orbit method. We propose a symmetry group for which the electric charge is invariant and, on this basis, a cosmological scenario in which the three former spatial dimensions inflate quickly while the fifth one shrinks, leading to a 4D era where the particles correspond to the coadjoint orbits of this group. By this mechanism, the elementary particles can acquire electric charge as a by-product of the $4+1$ symmetry breaking of the Universe. By pullback over the space-time, we construct the non-Riemannian connection corresponding to this symmetry group, allowing to recover conservation of the charge and the equation of motion with the Lorentz force. On this ground, we develop a five dimensional extension of the variational relativity allowing to deduce in the classical limit Maxwell's equation.

---

## Key Arguments and Derivations

### 1. The Coadjoint Orbit Method (Section 2)

The paper uses Souriau's coadjoint orbit method (geometric quantization) to classify elementary particles. For a symmetry group $G$ with Lie algebra $\mathfrak{g}$, the coadjoint orbits in $\mathfrak{g}^*$ classify particles. Each orbit is a symplectic manifold; the momentum map $\psi$ is a symplectomorphism from the space of motions into the orbit.

**Poincare group example**: $G = \mathbb{R}^4 \rtimes \text{SO}(1,3)$ (dimension 10). The momentum $\hat{\mu} = (\Pi, M)$ has two invariants: rest mass $m_0 = \sqrt{\Pi^*\Pi}$ and spin $s = \sqrt{-W^*W}/\sqrt{\Pi^*\Pi}$.

### 2. The Kaluza-Klein Group $\hat{G}_1$ (Section 2.2)

Moving to 5D: $\hat{G}_1 = \mathbb{R}^5 \rtimes \text{SO}(1,4)$ (dimension 15). The 5-momentum decomposes as $\hat{\Pi} = [\Pi, q]^T$ where $q$ is the electric charge. Under the coadjoint representation:
$$\Pi = P\Pi' + q'\beta P^{*-1}F, \quad q = F^*\Pi + \beta q'$$

**The charge is not an invariant** of $\hat{G}_1$ — it depends on the reference frame, contradicting experiment. Hence $\hat{G}_1$ is not the symmetry group of physics today.

### 3. The Group $\hat{G}_0$ for Physics Today (Section 2.3)

Zooming in on the fifth dimension ($\hat{X}'_5 = \hat{X}_5/\omega$, $\omega \to 0$): the metric degenerates to $\hat{G}_0$ which preserves a degenerate bilinear form $\hat{G}'_0$ and a vector $\hat{\Omega}_0$. The group $\hat{G}_0$ (also dimension 15) has elements with linear part:
$$\hat{P} = \begin{pmatrix} P_L & 0 \\ F^* & 1 \end{pmatrix}$$

Under the coadjoint representation of $\hat{G}_0$: $q = q'$ — **the electric charge IS invariant**. Three invariants: rest mass, spin, and electric charge.

### 4. Cosmological Scenario (Section 2.4)

Three episodes:
1. **Near Big Bang**: 5D isotropic universe, particles classified by $\hat{G}_1$ momenta
2. **Symmetry breaking**: first 3 spatial dimensions expand rapidly, fifth shrinks
3. **Today**: 4D era, particles characterized by $\hat{G}_0$ momenta

By this mechanism, particles acquire electric charge as a by-product of $4+1$ symmetry breaking.

### 5. Pullback Connection (Section 3)

The $\hat{G}_0$-connection on the frame bundle leads, via five hypotheses (H1-H5), to:
- Parallel transport of 5-momentum $\hat{\Phi}$ along worldlines: $(\mathfrak{f}^*\hat{\nabla})_U(\mathfrak{f}^*\hat{\Phi}) = 0$
- Torsion-free condition recovers Levi-Civita connection
- The electromagnetic field emerges as $F_{ij} = \partial_i A_j - \partial_j A_i$
- The equation of motion is the Lorentz force: $m_0 U^k\nabla_k U_i = -qF_i{}^j U_j$
- Rest mass $m_0$ and charge $q$ are integrals of the motion
- Section changes correspond to gauge transformations

### 6. Variational Relativity (Section 4)

Palatini variational approach with Lagrangian $L_G = L_g(R, G) + L_{em}(\tilde{R}, G, A^*)$:
$$L_G = -\Lambda + \frac{1}{2}G^{ij}R_{ij} - \tilde{k}A_r G^{ri}G^{jk}\tilde{R}_{ijk}$$

where $\tilde{R}_{ijk} = \nabla_k F_{ji} + 2A_p R^p{}_{ijk}$. The field equations (14 equations for 14 unknowns $G_{ij}, A_i$) reduce in the classical limit to:
- Einstein equations (with coupling terms)
- Maxwell equations: $\partial_j F^{ji} = -\frac{1}{\epsilon_0}\rho_e U_i$

The second coupling constant $\tilde{k} = 8\pi G_N \epsilon_0$ relates gravity and electromagnetism. The ratio $\tilde{k}$ is proportional to Dirac's large number $\sim 10^{-40}$.

---

## Key Results

1. **Charge frame-dependence resolved**: In Kaluza-Klein with SO(1,4), electric charge depends on observer. The degenerate group $\hat{G}_0$ (obtained by shrinking the fifth dimension) makes charge invariant.
2. **Coadjoint orbit classification**: Particles in 5D ($\hat{G}_1$) have 2 invariants (mass, spin); today's particles ($\hat{G}_0$) have 3 invariants (mass, spin, charge).
3. **Cosmological charge acquisition**: Electric charge emerges from $4+1$ symmetry breaking of the universe.
4. **Lorentz force from parallel transport**: The 5-momentum parallel transport condition in the pullback connection reproduces the equation of motion with Lorentz force.
5. **Maxwell from variational principle**: A 5D extension of Palatini variational relativity yields Maxwell's equations in the classical (Newtonian) limit.
6. **Dilaton problem avoided**: The approach uses 14 field equations for 14 unknowns, sidestepping the traditional KK dilaton problem (15 equations for 15 unknowns with physically meaningless 15th equation).
7. **Dirac large number**: The coupling $\tilde{k} = (l_K / 2\sqrt{\lambda_C \lambda_{C,p}})^2$ where $l_K = 0.238 \times 10^{-31}$ cm is Klein's cylinder radius.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Poincare invariants | $m_0 = \sqrt{\Pi^*\Pi}$, $s = \sqrt{-W^*W}/\sqrt{\Pi^*\Pi}$ | Sec. 2.1 |
| $\hat{G}_1$ charge non-invariance | $q = F^*\Pi + \beta q'$ | Sec. 2.2 |
| $\hat{G}_0$ charge invariance | $q = q'$ | Sec. 2.3 |
| Degenerate metric | $\hat{G}'_0 = \begin{pmatrix} G & 0 \\ 0 & 0 \end{pmatrix}$ | Sec. 2.3 |
| Electromagnetic field | $F_{ij} = \partial_i A_j - \partial_j A_i$ | Sec. 3.3 |
| Lorentz force | $m_0 U^k\nabla_k U_i = -qF_i{}^j U_j$ | Sec. 3.3 |
| Mixed curvature | $\tilde{R}_{ijk} = \nabla_k F_{ji} + 2A_p R^p{}_{ijk}$ | Sec. 4.3 |
| Einstein+EM field equations | $R_{ij} - \frac{1}{2}RG_{ij} + \Lambda G_{ij} - \tilde{k}[\ldots] = \kappa[(\rho+p)U_iU_j - pG_{ij}]$ | Sec. 4.3 |
| Maxwell equations | $\partial_j F^{ji} = -\frac{1}{\epsilon_0}\rho_e U_i$ | Sec. 4.4 |
| Second coupling constant | $\tilde{k} = 8\pi G_N\epsilon_0$ | Sec. 4.4 |

---

## Relevance to Phonon-Exflation

This paper offers a complementary perspective on Kaluza-Klein theory through Souriau's geometric mechanics:

1. **Charge from dimensional symmetry breaking**: The $4+1$ scenario where electric charge emerges from symmetry breaking of the 5D isometry group parallels the framework's mechanism where quantum numbers emerge from the SU(3) fiber structure during the exflation transit. The key difference: de Saxce works with U(1) (electromagnetism only), while the framework uses SU(3) (full color + generation structure).

2. **Degenerate metric limit**: The $\omega \to 0$ limit where the 5D metric degenerates to a rank-4 form is analogous to the framework's $\tau \to 0$ limit where the SU(3) fiber emerges from unity. Both involve a singular limit that changes the symmetry group structure.

3. **Coadjoint orbit classification**: The method of classifying particles via coadjoint orbits of the symmetry group provides a rigorous group-theoretic framework. The framework's classification of particles via irreducible representations of $\text{SU}(3) \times \text{U}(1)_7$ could be reformulated in this language.

4. **Dilaton problem**: The traditional KK dilaton problem (15th equation) is a well-known obstruction. The framework avoids this by working with a non-Riemannian spectral geometry (Connes NCG) rather than classical KK metrics.
