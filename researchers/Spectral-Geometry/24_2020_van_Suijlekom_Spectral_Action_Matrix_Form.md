# Spectral action in matrix form

**Author(s):** Ali H. Chamseddine, John Iliopoulos, Walter D. van Suijlekom
**Year:** 2020
**Journal:** [not explicitly stated in source; arXiv preprint]
**arXiv:** 2009.03367
**Relevance:** HIGH

---

## Abstract

Quantization of the noncommutative geometric spectral action has so far been performed on the final component form of the action where all traces over the Dirac matrices and symmetry algebra are carried out. In this work, in order to preserve the noncommutative geometric structure of the formalism, we derive the quantization rules for propagators and vertices in matrix form. We show that the results in the case of a product of a four-dimensional Euclidean manifold by a finite space, could be cast in the form of that of a Yang-Mills theory. We illustrate the procedure for the toy electroweak model.

---

## Key Arguments and Derivations

### Section 1 — Introduction

The authors motivate the work by observing that in the standard noncommutative geometry (NCG) approach, the spectral action is expanded and all traces over Clifford algebra and symmetry algebra matrices are performed before quantization. This loses the unified structure: looking at the component-form propagators one cannot see the unified picture from which they were derived. In particular, relations among coupling constants (known to be unstable under renormalization in the traditional SM framework) might be better understood if the matrix structure is preserved at the quantum level.

The key point: all fermionic fields assemble into one spinor acted on by a Dirac operator $D$ which is a $384 \times 384$ matrix. The fermionic propagator $D^{-1}$ is a matrix of the same dimension. To preserve the noncommutative nature at the quantum level, one must derive all propagators and vertices in matrix form without taking traces.

The paper works on a flat four-dimensional Euclidean manifold (gravity excluded for simplicity), with the product geometry $M \times F$ where $F$ is a finite noncommutative space.

### Section 2 — Action in matrix form

The noncommutative space is defined by the spectral data $(A, H, D, J, \gamma)$ as the product of a four-dimensional manifold $M$ with a finite space $(A_F, H_F, D_F, J_F, \gamma_F)$. The Dirac operator including inner fluctuations is $D_A = i\gamma^\mu \partial_\mu + A$, where $A$ is the connection formed from commutators $[D, b]$ with algebra elements.

The authors square $D$ to obtain $D^2 = -(\partial_\mu \partial_\mu + A_\mu \partial_\mu + B)$ and rewrite it in Bochner-Lichnerowicz form $D^2 = -\nabla_\mu \nabla_\mu - E$ with connection $\omega_\mu = \frac{1}{2}A_\mu$ and endomorphism $E$. They compute the curvature $\Omega_{\mu\nu} = \partial_\mu \omega_\nu - \partial_\nu \omega_\mu + [\omega_\mu, \omega_\nu]$.

Using the Gilkey (Seeley-DeWitt) heat kernel coefficients $a_0$, $a_2$, $a_4$ (in flat space), the spectral action is $I = \Lambda^4 f_4 a_0 + \Lambda^2 f_2 a_2 + f_0 a_4$. The key achievement is expressing $I$ entirely in terms of $A$ without taking traces over Clifford or matrix algebra. The result: all cubic terms combine into a total divergence, and the action takes the explicit matrix form of Eq. (2), containing quadratic (mass), cubic, and quartic terms in $A$, with all Dirac gamma matrix contractions left unevaluated.

### Section 3 — Gauge fixing and Feynman rules

The gauge transformation is $A \mapsto u^* A u + u^* \delta u$ with $\delta u = i\gamma^\nu \partial_\nu u$, under which $E$ and $\Omega_{\mu\nu}$ transform covariantly. For the product of continuous and finite spaces, $A = i\gamma^\mu B_\mu + \gamma_5 \phi$, and the connection $\omega_\mu = B_\mu$ depends only on gauge fields.

A gauge-fixing term $G = \partial_\mu \omega_\mu$ is added (Feynman gauge $\xi = 1$), along with ghost fields $c, \bar{c}$ with the same matrix structure as $u$.

**Propagators (Section 3.1):** The fields are decomposed as $B^B_{\mu A} = i B^i_\mu (T^i)^B_A$ (block-diagonal, hermitian basis) and $\phi^B_A = \phi^m (\lambda^m)^B_A$ (off-diagonal, hermitian basis), with normalization $\text{Tr}(T^i T^j) = \frac{1}{2}\delta^{ij}$, $\text{Tr}(\lambda^m \lambda^n) = \frac{1}{2}\delta^{mn}$. The quadratic action yields propagators:

$$\langle B^i_\mu B^j_\nu \rangle = \frac{12\pi^2}{f_0} \delta^{ij} \delta_{\mu\nu} \frac{1}{p^2}, \qquad \langle \phi^m \phi^n \rangle = \frac{8\pi^2}{f_0} \delta^{mn} \frac{1}{p^2}$$

These are reassembled into a unified matrix propagator expressed through "Gamma matrices" $\Gamma^{\tau I}$ that encode both Clifford and algebra structure. The ghost propagator is $\langle c^{*B}_A c^D_C \rangle = (T^i)^B_A (T^i)^D_C \frac{1}{p^2}$.

**Vertices:** The mass vertex (valence 2) comes from the $\Lambda^2 f_2$ term. The cubic vertex arises from $\text{Tr}(\partial_\mu A \gamma^\mu A \gamma^\nu A \gamma_\nu - \gamma^\mu \partial_\mu A \gamma^\nu A \gamma_\nu A)$. The quartic vertex from $\text{Tr}(\gamma^\mu A \gamma^\nu A \gamma^\mu A \gamma^\nu A + 2\gamma^\mu A \gamma^\mu A \gamma^\nu A \gamma^\nu A)$. The ghost vertex from $-\frac{1}{2}i \text{Tr}(\partial_\mu \bar{c} [\{\gamma^\mu, A\}, c])$.

All Feynman rules are expressed diagrammatically as ribbon graphs (Figures 1 and 2), in one-to-one correspondence with Yang-Mills theory but with the crucial difference that Dirac matrices $\gamma^\mu$ and $\gamma_5$ appear in bosonic as well as fermionic propagators/vertices.

### Section 4 — The electroweak toy model

The procedure is illustrated for a toy electroweak model with fermions $\Psi = (\nu_L, e_L, e_R)^T$ and algebra $A = M_2(\mathbb{C}) \oplus \mathbb{H}$. The generators $T^i$ (block-diagonal) correspond to SU(2) generators plus a U(1) hypercharge, while $\lambda^m$ (off-diagonal) encode the Higgs doublet.

From the spectral action, normalizing the vector kinetic terms yields the unification condition $\sin^2 \theta_W = 1/4$ and the Higgs quartic coupling $\lambda = g^2/12$. The Higgs field requires rescaling $H \to \frac{g}{\sqrt{6}} H$, giving the electron mass $m_e = g\sqrt{1/6}\,\langle H \rangle$. These relations are consequences of the underlying geometric structure, and the authors wish to investigate their stability under renormalization using the matrix-form Feynman rules.

### Section 5 — Conclusions

The spectral action Feynman diagrams are in one-to-one correspondence with those of a Yang-Mills non-abelian gauge theory with a direct mass term. The main difference is the appearance of space-time Dirac matrices $\gamma^\mu$ and $\gamma_5$ for bosonic fields as well. The next step is a full renormalizability analysis, which involves ribbon diagrams (similar to those in noncommutative quantum field theory). The authors note that BRST quantization for the ghost sector would be a useful development.

---

## Key Results

1. **Spectral action in unexpanded matrix form (Eq. 2):** The bosonic spectral action on $M^4 \times F$ is written entirely in terms of the matrix-valued connection $A$ without taking traces over Clifford or algebra indices. Contains quadratic, cubic, and quartic terms.

2. **Cubic terms vanish up to total divergence:** All cubic contractions of Dirac gamma matrices cancel, and the remaining cubic terms combine into the total divergence $-i\partial_\mu \text{Tr}(\gamma^{\mu\nu}(A^2 \gamma_\nu A - A\gamma_\nu A^2))$.

3. **Unified matrix propagator (Eq. 3):** The bosonic propagator is $\langle A^{\beta B}_{\alpha A} A^{\delta D}_{\gamma C} \rangle = (\Gamma^{\tau I})^{\beta B}_{\alpha A} (\Gamma^{\tau I})^{\delta D}_{\gamma C} \frac{1}{p^2}$, where $\Gamma^{\tau I}$ encodes both Clifford ($\gamma^\mu, \gamma_5$) and algebra ($T^i, \lambda^m$) structure.

4. **Feynman rules as ribbon graphs (Figures 1-2):** All propagators and vertices (mass, cubic, quartic, ghost) are expressed diagrammatically as ribbon graphs, in one-to-one correspondence with Yang-Mills theory.

5. **Electroweak predictions from matrix form:** The toy model reproduces $\sin^2 \theta_W = 1/4$, $\lambda = g^2/12$, and $m_e = g\sqrt{1/6}\,\langle H\rangle$ — geometric constraints whose stability under renormalization is the target of the matrix-form quantization program.

6. **Ghost sector:** Ghost fields $c, \bar{c}$ carry the same matrix structure as the gauge parameter $u$, with propagator $\langle c^{*B}_A c^D_C \rangle = (T^i)^B_A (T^i)^D_C / p^2$ and a cubic ghost-gauge vertex.

7. **Gauge covariance preserved:** $E \mapsto u^* E u$ and $\Omega_{\mu\nu} \mapsto u^* \Omega_{\mu\nu} u$ under the NCG gauge transformation $A \mapsto u^* A u + u^* \delta u$.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spectral data product | $D = i\gamma^\mu \partial_\mu \otimes 1 + \gamma_5 \otimes D_F$ | Eq. (1) |
| Spectral action (heat kernel) | $I = \Lambda^4 f_4 a_0 + \Lambda^2 f_2 a_2 + f_0 a_4$ | below Eq. (1) |
| Heat kernel $a_4$ | $a_4 = \frac{1}{16\pi^2} \frac{1}{12} \int d^4x\, \text{Tr}(\Omega_{\mu\nu}\Omega^{\mu\nu} + 6E^2)$ | Sec. 2 |
| Spectral action in matrix form | $I = \frac{1}{32\pi^2}\int d^4x \big[2\Lambda^4 f_4 \text{Tr}(1) + \Lambda^2 f_2 \text{Tr}(2A^2 + \gamma^\mu A \gamma_\mu A) - \frac{f_0}{6}\text{Tr}(\gamma^\mu \partial_\nu A \gamma_\mu \partial^\nu A + 2\gamma^\mu \partial_\mu A \gamma^\nu \partial_\nu A) + \frac{f_0}{24}\text{Tr}(\gamma^\mu A \gamma^\nu A \gamma_\mu A \gamma_\nu A + 2\gamma^\mu A \gamma_\mu A \gamma^\nu A \gamma_\nu A) + \text{cubic}\big]$ | Eq. (2) |
| Unified matrix propagator | $\langle A^{\beta B}_{\alpha A} A^{\delta D}_{\gamma C} \rangle = (\Gamma^{\tau I})^{\beta B}_{\alpha A} (\Gamma^{\tau I})^{\delta D}_{\gamma C} \frac{1}{p^2}$ | Eq. (3) |
| Mass vertex | $V^{\alpha A \gamma C}_{\beta B \delta D} = \frac{\Lambda^2 f_2}{32\pi^2}\big(2\delta^\gamma_\beta \delta^C_B \delta^\alpha_\delta \delta^A_D + (\gamma_\mu)^\gamma_\beta \delta^C_B (\gamma^\mu)^\alpha_\delta \delta^A_D\big)$ | Eq. (4) |
| Cubic vertex | $V^{\alpha A \gamma C \eta E}_{\beta B \delta D \tau F} = \frac{f_0}{96\pi^2} p_\mu \delta^C_B \delta^E_D \delta^A_F (\gamma_\nu)^\eta_\delta \big[(\gamma^\nu)^\gamma_\beta (\gamma^\mu)^\alpha_\tau - (\gamma^\mu)^\gamma_\beta (\gamma^\nu)^\alpha_\tau\big]$ | Eq. (5) |
| Quartic vertex | $V^{\alpha A \gamma C \eta E \kappa G}_{\beta B \delta D \tau F \lambda H} = \frac{f_0}{768\pi^2} \delta^C_B \delta^E_D \delta^G_F \delta^A_H (\gamma^\mu)^\alpha_\lambda (\gamma_\nu)^\kappa_\tau \big[(\gamma^\nu)^\gamma_\beta (\gamma^\mu)^\eta_\delta + 2(\gamma^\mu)^\gamma_\beta (\gamma^\nu)^\eta_\delta\big]$ | Eq. (6) |
| Ghost propagator | $\langle c^{*B}_A c^D_C \rangle = (T^i)^B_A (T^i)^D_C \frac{1}{p^2}$ | Eq. (7) |
| Ghost vertex | $\langle \bar{c}^B_A A^{\beta F}_{\alpha E} c^D_C \rangle = \frac{1}{4} p_\mu (\gamma^\mu)^\alpha_\beta \big(\delta^C_F \delta^E_B \delta^A_D - \delta^C_B \delta^E_D \delta^A_F\big)$ | Eq. (8) |
| Weinberg angle | $\sin^2 \theta_W = \frac{g'^2}{g^2 + g'^2} = \frac{1}{4}$ | Eq. (9) |
| Higgs quartic coupling | $\lambda = g^2/12$ | Sec. 4 |

---

## Relevance to Phonon-Exflation

This paper provides the quantization framework for the spectral action on product geometries $M^4 \times F$, which is the structural backbone of the phonon-exflation model where $F = SU(3)$. The matrix-form Feynman rules preserve the Clifford and algebra structure that the project's Dirac spectrum computations (Sessions 7-35) exploit. The unified propagator Eq. (3) encodes exactly the kind of gauge-Higgs unification that produces the coupling constant relations ($\sin^2\theta_W$, $\lambda$) whose stability under renormalization is critical to whether the spectral action can yield physical predictions. The ribbon-graph structure of the vertices connects to the project's spectral action computations (Seeley-DeWitt coefficients $a_0, a_2, a_4$) and to the one-loop program of van Nuland and van Suijlekom (paper 25 in this collection), which builds directly on this matrix formulation. The decomposition $A = i\gamma^\mu B_\mu + \gamma_5 \phi$ into block-diagonal gauge and off-diagonal Higgs sectors mirrors the project's analysis of $D_K(\tau)$ perturbations and the BCS pairing channel identification.
