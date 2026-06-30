# Hyperbolic Band Theory

**Author(s):** Joseph Maciejko, Steven Rayan
**Year:** 2021
**Journal:** Science Advances 7, eabe9170
**arXiv:** 2008.05489
**Relevance:** HIGH

---

## Abstract

The notions of Bloch wave, crystal momentum, and energy bands are commonly regarded as unique features of crystalline materials with commutative translation symmetries. Motivated by the recent realization of hyperbolic lattices in circuit quantum electrodynamics, we exploit ideas from algebraic geometry to construct the first hyperbolic generalization of Bloch theory, despite the absence of commutative translation symmetries. For a quantum particle propagating in a hyperbolic lattice potential, we construct a continuous family of eigenstates that acquire Bloch-like phase factors under a discrete but noncommutative group of hyperbolic translations, the Fuchsian group of the lattice. A hyperbolic analog of crystal momentum arises as the set of Aharonov-Bohm phases threading the cycles of a higher-genus Riemann surface associated with this group. This crystal momentum lives in a higher-dimensional Brillouin zone torus, the Jacobian of the Riemann surface, over which a discrete set of continuous energy bands can be computed.

---

## Key Arguments and Derivations

### Introduction: From Euclidean to Hyperbolic

Bloch's theorem (1928) describes quantum-mechanical propagation in crystalline solids -- the key condition is periodicity under discrete translations. Bloch waves acquire predictable phase shifts under translations, defining crystal momentum $\mathbf{k}$ in the Brillouin zone (topologically a $d$-torus). The nontrivial topology of the Brillouin zone underlies the topological revolution in condensed matter (Haldane's Chern insulator, topological band theory).

Hyperbolic lattices -- ordered but aperiodic tessellations of the hyperbolic plane -- have been recently realized in circuit quantum electrodynamics (Kollar, Fitzpatrick, Houck, Nature 2019). These are qualitatively distinct from quasicrystals (which tile Euclidean space aperiodically). The negative curvature of hyperbolic space allows patterns impossible in Euclidean space, such as tilings by regular heptagons.

Prior to this work, "no hyperbolic equivalent of Bloch theory currently exists" (quoting Kollar et al.). The authors construct the first such generalization.

### Euclidean Lattices and Bloch Phases (Review)

Free-particle Hamiltonian $H_0 = p^2/2m$ on $\mathbb{R}^2$ has continuous SE(2) symmetry. A periodic potential $V(x,y)$ with square lattice symmetry reduces this to the discrete translation group $G \cong \mathbb{Z} \times \mathbb{Z}$. Bloch's theorem: eigenstates satisfy $\psi(x+1,y) = e^{ik_x}\psi(x,y)$, $\psi(x,y+1) = e^{ik_y}\psi(x,y)$.

**Key reinterpretation:** The construction involves TWO homeomorphic 2-tori:
1. $\Sigma$ = quotient of configuration space $\mathbb{E}$ by $G$: $\mathbb{E}/G \cong \mathbb{R}^2/\mathbb{Z}^2 \cong T^2$
2. $\text{Jac}(\Sigma)$ = Jacobian of $\Sigma$, parametrizing $U(1)$-representations of $\pi_1(\Sigma)$

The Bloch phases $e^{ik_x}, e^{ik_y}$ are Aharonov-Bohm phases threading the two noncontractible cycles of the real-space torus. $\Sigma$ is an elliptic curve (genus-1 Riemann surface); the Abel-Jacobi map provides an isomorphism between $\Sigma$ and $\text{Jac}(\Sigma)$ -- this is particle-wave duality in algebraic-geometric language.

### Hyperbolic Lattices and Automorphic Bloch Phases

**Hyperbolic Laplacian:** On the Poincare disk $|z|<1$ with metric $ds^2 = 4(1-|z|^2)^{-2}(dx^2+dy^2)$:
$$\Delta = \frac{1}{4}(1-|z|^2)^2\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right)$$
The free-particle Hamiltonian $H_0 = -\Delta$ commutes with Mobius transformations.

**Fuchsian group:** A potential $V(x,y)$ with the symmetry of a $\{4g,4g\}$ hyperbolic tiling ($g \geq 2$) is invariant under a discrete Fuchsian subgroup $\Gamma \subset \text{PSU}(1,1)$. This group acts properly discontinuously, tiling all of $\mathbb{H}$ with geometrically identical copies of a fundamental domain $D$ (compact, finite area under Poincare metric).

**Compactification:** The quotient $\mathbb{H}/\Gamma$ is a smooth, compact Riemann surface $\Sigma_g$ of genus $g \geq 2$ (uniformization theorem). This surface has $2g$ noncontractible cycles through which $2g$ Aharonov-Bohm fluxes $k_a^{(1)}, k_b^{(1)}, \ldots, k_a^{(g)}, k_b^{(g)} \in [0, 2\pi)$ can be threaded. The $2g$ phase factors form a $U(1)$-representation $\chi$ of $\pi_1(\Sigma_g)$.

**Hyperbolic crystal momentum:** A $2g$-dimensional vector
$$\mathbf{k} = \left(k_a^{(1)}, k_b^{(1)}, \ldots, k_a^{(g)}, k_b^{(g)}\right) \in T^{2g} \cong \text{Jac}(\Sigma_g)$$
lives in a higher-dimensional Brillouin zone -- the Jacobian of the Riemann surface.

**Automorphic Bloch condition (generalized Bloch theorem):**
$$\psi(\gamma(z)) = \chi(\gamma)\psi(z)$$
where $\gamma \in \Gamma$ acts by Mobius transformations and $\chi$ is the $U(1)$-representation. Functions obeying this condition are known as automorphic functions with factor of automorphy $\chi$ (Poincare).

**Schrodinger equation on unit cell:** The potential $V$ is automorphic: $V(\gamma(z)) = V(z)$. Solve
$$(- \Delta + V)\psi = E\psi$$
on the single reference unit cell $D$ with automorphic Bloch boundary conditions. The hyperbolic Laplacian is self-adjoint on $D$ with these boundary conditions. Since the region is compact, one obtains a discrete set of real eigenvalues $\{E_n(\mathbf{k})\}$ for each $\mathbf{k}$.

### The Abel-Jacobi Map and Particle-Wave Duality

For genus $g \geq 2$, the two complex manifolds $\Sigma_g$ and $\text{Jac}(\Sigma_g)$ are NO LONGER isomorphic (unlike genus 1). $\Sigma_g$ is 2-dimensional; $\text{Jac}(\Sigma_g)$ is $2g$-dimensional.

**Period matrix:** Choose a symplectic basis of loops $a_i, b_i$ ($i = 1,\ldots,g$) and dual basis of holomorphic one-forms $\theta_1, \ldots, \theta_g$ with $\oint_{a_i}\theta_j = \delta_{ij}$. The remaining integrals form the $g \times g$ period matrix $\Omega$ (symmetric, positive-definite imaginary part, living in Siegel upper half-space). The period lattice $\Lambda$ defines the Jacobian: $\text{Jac}(\Sigma_g) = \mathbb{R}^{2g}/\Lambda$.

**Abel-Jacobi map:** For a point $p \in \Sigma_g$ and path $c_p$ from basepoint $p_0$ to $p$:
$$a(p) = \left(\int_{c_p}\theta_1, \ldots, \int_{c_p}\theta_g\right) \mod \Lambda$$
This maps position space to crystal momentum. For $g = 1$, this is the standard particle-wave duality (Fourier transform). For $g \geq 2$, the map from the $g$-fold symmetric product of $\Sigma_g$ to $\text{Jac}(\Sigma_g)$ is "almost an isomorphism" (birational), with a special "high-symmetry" submanifold that must be blown down -- related to the theta divisor.

### The Bolza Lattice ($g = 2$)

The simplest hyperbolic analog of the square lattice: the $\{8,8\}$ tiling. The unit cell $D$ is a regular hyperbolic octagon centered at $z = 0$. The Fuchsian group $\Gamma$ is generated by four Mobius transformations $\gamma_j$ ($j = 1,\ldots,4$) with explicit $\text{PSU}(1,1)$ matrices:
$$\gamma_j = \begin{pmatrix} 1+\sqrt{2} & (2+\sqrt{2})\lambda e^{i(j-1)\pi/4} \\ (2+\sqrt{2})\lambda e^{-i(j-1)\pi/4} & 1+\sqrt{2} \end{pmatrix}$$
where $\lambda = \sqrt{\sqrt{2}-1}$. The hyperbolic crystal momentum is $\mathbf{k} = (k_1, k_2, k_3, k_4) \in T^4$.

**Empty-lattice approximation:** Eigenvalues of the hyperbolic Laplacian with automorphic boundary conditions on the Bolza surface. At $\mathbf{k} = 0$: $E_0 = 0$, $E_1 \approx 3.839$ (3-fold degenerate), $E_2 \approx 5.354$ (4-fold degenerate), $E_3 \approx 14.726$ (2-fold degenerate). These degeneracies completely lift for generic $\mathbf{k} \neq 0$, as in conventional band theory.

**Von Neumann-Wigner theorem generalization:** Only codimension-3 level crossings are perturbatively stable. For $\{8,8\}$ tessellations, generically stable nodal-line crossings occur. For general $\{4g,4g\}$ tessellations, stable crossings form $(2g-3)$-dimensional submanifolds of $\text{Jac}(\Sigma_g)$.

**Automorphic potential:** Constructed by summing over $\Gamma$-translates of a localized potential:
$$V(z) = \sum_{\gamma \in \Gamma} U(\gamma(z))$$
This is a generalized theta series. Results: ground state energy lowered; degeneracies partially lifted (e.g., 3-fold $\to$ 2 $\oplus$ 1); probability density concentrated near potential well center.

### Hyperbolic Point-Group Symmetries

The analog of point group for $\{4g,4g\}$ lattices is $G \cong \text{Aut}(\Sigma_g)$, the finite group of automorphisms of the Riemann surface. For the Bolza surface: $|G| = 96$, generated by four operations:
- $R$: $C_8$ rotation (orientation-preserving)
- $U$: $C_3$ rotation-like (orientation-preserving)
- $S, T$: reflection-like (orientation-reversing)

The point group acts linearly on hyperbolic $\mathbf{k}$-space: $\mathbf{k}_h = M(h)\mathbf{k}$ where $M(h) \in \text{SL}(4,\mathbb{Z})$. Unlike Euclidean case, $M(h)$ are generally NOT orthogonal. Bandstructure invariance $E_n(\mathbf{k}_h) = E_n(\mathbf{k})$ verified numerically for all four generators.

### Tight-Binding Limit

A hyperbolic tight-binding formulation is constructed. In the limit of deep localized potentials, approximate eigenstates obeying the automorphic Bloch condition are built as linear combinations of "atomic" eigenstates and their $\Gamma$-translates (hyperbolic LCAO). Hyperbolic Wannier functions are also constructed.

### Open Questions

The paper constructs a continuous family of Bloch eigenstates but does NOT prove a hyperbolic Bloch theorem (that ALL eigenstates are of this form). Number-theoretic tools (Selberg trace formula, zeta functions) may address spectral questions. Higher-dimensional extensions to K3 surfaces and Calabi-Yau manifolds are envisioned, suggesting connections between high-energy physics and condensed matter via string theory and mirror symmetry.

---

## Key Results

1. **First hyperbolic generalization of Bloch theory** for quantum particles in lattice potentials with noncommutative (Fuchsian) translation symmetries.
2. **Hyperbolic crystal momentum** is $2g$-dimensional (for $\{4g,4g\}$ tilings), living in the Jacobian torus $T^{2g}$ of a genus-$g$ Riemann surface.
3. **Automorphic Bloch condition** $\psi(\gamma(z)) = \chi(\gamma)\psi(z)$ generalizes Bloch's theorem to hyperbolic lattices.
4. **Higher-dimensional Brillouin zone** arises naturally from algebraic geometry: the Jacobian $\text{Jac}(\Sigma_g)$ parametrizes $U(1)$-representations of $\pi_1(\Sigma_g)$.
5. **Abel-Jacobi map** replaces Fourier transform as algebraic particle-wave duality for $g \geq 2$.
6. **Degeneracy splitting** at generic $\mathbf{k}$ follows the same principles as Euclidean band theory, but stable codimension-3 crossings (nodal lines in 4D) are generically expected.
7. **Hyperbolic point group** $\text{Aut}(\Sigma_g)$ acts linearly on $\mathbf{k}$-space via $\text{SL}(2g,\mathbb{Z})$ matrices (not orthogonal).
8. **Bolza lattice bandstructure** computed numerically via finite element method on hyperbolic octagon with twisted boundary conditions.
9. **Tight-binding approximation** and **hyperbolic Wannier functions** constructed for deep potentials.
10. Construction anticipates emergence of algebro-geometric invariants alongside topological ones (Donaldson-Thomas invariants) in materials physics.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Hyperbolic Laplacian | $\Delta = \frac{1}{4}(1-|z|^2)^2\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right)$ | Eq. (1) |
| Automorphic Bloch condition | $\psi(\gamma(z)) = \chi(\gamma)\psi(z)$ | Eq. (2) |
| Hyperbolic Schrodinger equation | $(-\Delta + V)\psi = E\psi$ | Eq. (3) |
| Abel-Jacobi map | $a(p) = \left(\int_{c_p}\theta_1, \ldots, \int_{c_p}\theta_g\right) \mod \Lambda$ | Eq. (4) |
| Automorphic potential | $V(z) = \sum_{\gamma \in \Gamma} U(\gamma(z))$ | Eq. (5) |
| Poincare disk metric | $ds^2 = 4(1-|z|^2)^{-2}(dx^2 + dy^2)$ | Text |
| Bloch boundary conditions (Bolza) | $\psi(C_j) = e^{ik_j}\psi(C_{j+4}),\quad j=1,\ldots,4$ | Text |
| Fuchsian generators (Bolza) | $\gamma_j = \begin{pmatrix}1+\sqrt{2} & (2+\sqrt{2})\lambda e^{i(j-1)\pi/4} \\ (2+\sqrt{2})\lambda e^{-i(j-1)\pi/4} & 1+\sqrt{2}\end{pmatrix}$ | Eq. (S4) |
| Fuchsian relation | $\gamma_1\gamma_2^{-1}\gamma_3\gamma_4^{-1}\gamma_1^{-1}\gamma_2\gamma_3^{-1}\gamma_4 = I$ | Eq. (S6) |
| Fundamental group | $\pi_1(\Sigma_g) = \{a_1,b_1,\ldots,a_g,b_g : a_1 b_1 a_1^{-1}b_1^{-1}\cdots a_g b_g a_g^{-1}b_g^{-1} = 1\}$ | Eq. (S10) |
| Vertex positions | $p_j = 2^{-1/4}e^{i(2j-1)\pi/8},\quad j=1,\ldots,8$ | Eq. (S3) |
| Corner phase factors | $\psi_{p_1} = e^{i(k_1+k_2-k_3+k_4)}\psi_{p_5}$, etc. | Eq. (S24) |
| Bolza eigenvalues ($\mathbf{k}=0$) | $E_0 = 0$, $E_1 \approx 3.839$, $E_2 \approx 5.354$, $E_3 \approx 14.726$ | Fig. 2 |
| Weak form (variational) | $\int_D d^2r\sqrt{g}\left(g^{\mu\nu}\partial_\mu\phi^*\partial_\nu\psi + \phi^* V\psi\right) = E\int_D d^2r\sqrt{g}\,\phi^*\psi$ | Eq. (S15) |
| Reduced eigenvalue problem | $\tilde{A}\tilde{\psi} = E\tilde{B}\tilde{\psi}$, $\tilde{A} = U^\dagger AU$, $\tilde{B} = U^\dagger BU$ | Eqs. (S20-S21) |

---

## Relevance to Phonon-Exflation

Hyperbolic band theory bears HIGH relevance to the phonon-exflation framework in several ways. (1) The framework's internal geometry is $M^4 \times SU(3)$, where the compact fiber $SU(3)$ is a curved manifold. The Dirac spectrum on this fiber, which generates the particle spectrum, is computed via eigenvalue problems on compact curved spaces -- precisely the mathematical setting of this paper. (2) The transition from Euclidean band theory (genus 1, commutative translations) to hyperbolic band theory (genus $g \geq 2$, noncommutative Fuchsian groups) parallels the framework's transition from flat-space QFT to QFT on the curved SU(3) fiber, where the Peter-Weyl decomposition replaces Fourier analysis. (3) The paper's identification of the Jacobian as momentum space, with the Abel-Jacobi map replacing Fourier transforms, provides mathematical tools potentially applicable to characterizing the spectral structure on non-abelian group manifolds. (4) The appearance of higher-genus Riemann surfaces, moduli spaces, and algebro-geometric invariants connects to the framework's use of Connes' spectral geometry and noncommutative geometry, where spectral data encode geometric information. (5) The stable nodal-line crossings in hyperbolic bandstructures (codimension-3) may inform understanding of spectral degeneracies and level crossings in the $D_K(\tau)$ Dirac operator spectrum.
