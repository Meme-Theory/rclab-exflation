# The spectral geometry of operators of Dirac and Laplace type

**Author(s):** P. Gilkey
**Year:** 2004 (published 2007)
**Journal:** Handbook of Global Analysis, Elsevier
**arXiv:** N/A (handbook chapter)
**Relevance:** CRITICAL

---

## Abstract

[No formal abstract; this is a handbook chapter.] The chapter surveys recent developments in spectral geometry, covering operators of Laplace and Dirac type, heat trace asymptotics for closed manifolds and manifolds with boundary, hearing the shape of a drum, index theory, heat content asymptotics, spectral boundary conditions, non-Laplace operators, and Riemannian submersions.

---

## Key Arguments and Derivations

### 1. Operators of Laplace and Dirac Type (Section 2)

Gilkey establishes the fundamental structural result: for any operator $D$ of Laplace type, there exist a unique connection $\nabla$ on $V$ and a unique endomorphism $E$ such that $D\phi = -\phi_{;ii} - E\phi$. The connection 1-form and $E$ are given explicitly in terms of the operator coefficients (Lemma 2.1). For the Spin Laplacian, $E = -\frac{1}{4}\tau\,\text{id}$ (Lichnerowicz formula).

The DeRham complex is introduced: $d + \delta$ is an operator of Dirac type, and $\Delta_M = (d+\delta)^2$ decomposes into $p$-form Laplacians $\Delta_M^p$. The Weitzenb\"ock formula relates the ordinary Laplacian to the Bochner Laplacian: $\Delta_M = \tilde{\Delta}_M + \frac{1}{2}\gamma(dx^\mu)\gamma(dx^\nu)R_{\mu\nu}$.

### 2. Heat Trace Asymptotics for Closed Manifolds (Section 3)

Gilkey presents the eigenvalue asymptotics (Weyl's law: $\lambda_n \sim n^{2/m}$) and the heat trace expansion $\text{Tr}(F e^{-tD}) \sim \sum_{n=0}^\infty a_n(F,D) t^{(n-m)/2}$. The coefficients $a_n(F,D) = 0$ for odd $n$ on closed manifolds.

**Theorem 3.2** gives explicit formulas for $a_0$ through $a_6$ with full endomorphism $E$ and curvature $\Omega_{ij}$ dependence. The $a_6$ formula is the most complete available, including all cross-terms between $E$, $\Omega$, $\tau$, $\rho$, and $R$.

**Theorem 3.3** provides the leading behaviour for general $a_{2n}$: the highest-order terms are $\epsilon_n(4\pi)^{-m/2}\int \text{Tr}\{F(-(8n+4)\Delta^{n-1}E - 2n\Delta^{n-1}\tau\,\text{id} + \ldots)\}$.

**Theorem 3.4** (Patodi) specializes to the form-valued Laplacian using combinatorial constants $c(m,p)$, $c_0(m,p)$, $c_1(m,p)$, etc.

### 3. Hearing the Shape of a Drum (Section 4)

Reviews isospectrality results:
- Milnor: isospectral non-isometric flat tori in dimension 16
- Vigneras: isospectral hyperbolic Riemann surfaces with different fundamental groups
- Ikeda: isospectral spherical space forms
- Urakawa: isospectral regions in flat space ($m \geq 4$)

Positive results: constant curvature is spectrally determined in dimensions $\leq 6$ (Berger-Tanno, Theorem 4.3). $p$-isospectrality for $p = 0,1,2$ determines constant scalar curvature, Einstein condition, and constant sectional curvature (Patodi, Theorem 4.4).

### 4. Boundary Asymptotics (Section 5)

Complete formulas through $a_5$ for:
- **Dirichlet** (Theorem 5.1): includes boundary invariants $L_{aa}$, $R_{amam}$, and normal derivatives $F_{;m}$, $F_{;mm}$
- **Robin** (Theorem 5.2): adds endomorphism $S$ terms
- **Mixed** (Theorem 5.3): full $\Pi_+/\Pi_-$ projector structure with 6 pages of terms for $a_5$
- **Transmission** and **Transfer** boundary conditions for coupled membranes

### 5. Index Theory (Section 6)

The Euler characteristic $\chi(M) = a_m(1, \Delta_M^{\text{even}}) - a_m(1, \Delta_M^{\text{odd}})$. For manifolds with boundary, absolute/relative boundary conditions enter through the Chern-Gauss-Bonnet theorem with boundary terms.

---

## Key Results

1. Unique decomposition $D\phi = -\phi_{;ii} - E\phi$ for any Laplace-type operator (Lemma 2.1)
2. Complete $a_0$ through $a_6$ for general Laplace-type operators on closed manifolds (Theorem 3.2)
3. Leading behaviour of $a_{2n}$ for all $n$ (Theorem 3.3, after Avramidi and Branson et al.)
4. Patodi's formulas for form-valued Laplacians (Theorem 3.4)
5. Spectral determination of constant curvature in $\dim \leq 6$ (Theorem 4.3)
6. Complete $a_0$ through $a_5$ for Dirichlet, Robin, and mixed boundary conditions (Theorems 5.1-5.3)
7. Euler characteristic from heat trace asymptotics with boundary corrections
8. Finiteness of isospectral sets of compact symmetric spaces (via Theorem 3.5)

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Unique decomposition | $D\phi = -\phi_{;ii} - E\phi$ | Lemma 2.1 |
| Connection 1-form | $\omega_\nu = \frac{1}{2}(g_{\nu\mu}a^\mu + g^{\sigma\epsilon}\Gamma_{\sigma\epsilon\nu}\,\text{id})$ | Lemma 2.1 |
| Weitzenb\"ock | $\Delta_M = \tilde{\Delta}_M + \frac{1}{2}\gamma(dx^\mu)\gamma(dx^\nu)R_{\mu\nu}$ | Section 2.1 |
| Lichnerowicz | $E = -\frac{1}{4}\tau\,\text{id}$ (spin Laplacian) | Section 2 |
| $a_0$ | $(4\pi)^{-m/2}\int_M \text{Tr}\{F\}\,dx$ | Thm 3.2(1) |
| $a_2$ | $(4\pi)^{-m/2}\frac{1}{6}\int_M \text{Tr}\{F(6E + \tau)\}\,dx$ | Thm 3.2(2) |
| $a_4$ | $(4\pi)^{-m/2}\frac{1}{360}\int_M \text{Tr}\{F(60E_{;kk} + 60\tau E + 180E^2 + 12\tau_{;kk} + 5\tau^2 - 2|\rho|^2 + 2|R|^2 + 30\Omega_{ij}\Omega_{ij})\}\,dx$ | Thm 3.2(3) |
| Weyl asymptotics | $\lambda_n \sim n^{2/m}$ | Thm 3.1 |
| Zeta-heat relation | $\zeta(s,P,Q) = \Gamma(s)^{-1}\int_0^\infty t^{s-1}\text{Tr}(Q e^{-tP})\,dt$ | Thm 3.5(1) |
| Dirichlet $a_1$ | $-(4\pi)^{-(m-1)/2}\frac{1}{4}\int_{\partial M}\text{Tr}\{F\}\,dy$ | Thm 5.1(2) |
| Schr\"odinger-Lichnerowicz | $\nabla^*\nabla = D^2 - \frac{R}{4}$ | Eq. (15) |
| Patodi $a_0$ | $(4\pi)^{-m/2}c(m,p)\text{Vol}(M)$ where $c(m,p) = \binom{m}{p}$ | Thm 3.4(1) |

---

## Relevance to Phonon-Exflation

Gilkey's handbook chapter is the authoritative reference for the structural decomposition $D = -\nabla^*\nabla - E$ used throughout the framework's Dirac spectrum computations on SU(3). The explicit $a_2$ and $a_4$ formulas with the endomorphism $E$ and bundle curvature $\Omega_{ij}$ directly determine the spectral action expansion. The Patodi formulas for form-valued Laplacians are essential for understanding the bosonic sector contributions. The boundary condition formulas (especially mixed conditions with projectors $\Pi_\pm$) are relevant to the domain wall geometry at the fold. The Weitzenb\"ock formula connects the Dirac spectrum to curvature invariants of the internal geometry.
