# Heat kernel expansion: user's manual

**Author(s):** D.V. Vassilevich
**Year:** 2003
**Journal:** Physics Reports (Elsevier)
**arXiv:** hep-th/0306138
**Relevance:** CRITICAL

---

## Abstract

The heat kernel expansion is a very convenient tool for studying one-loop divergences, anomalies and various asymptotics of the effective action. The aim of this report is to collect useful information on the heat kernel coefficients scattered in mathematical and physical literature. We present explicit expressions for these coefficients on manifolds with and without boundaries, subject to local and non-local boundary conditions, in the presence of various types of singularities (e.g., domain walls). In each case the heat kernel coefficients are given in terms of several geometric invariants. These invariants are derived for scalar and spinor theories with various interactions, Yang-Mills fields, gravity, and open bosonic strings. We discuss the relations between the heat kernel coefficients and quantum anomalies, corresponding anomalous actions, and covariant perturbation expansions of the effective action (both "low-" and "high-energy" ones).

---

## Key Arguments and Derivations

### 1. Introduction and Motivation (Section 1)

Vassilevich traces the heat kernel method from Fock (1937), through Schwinger's proper-time representation, to DeWitt's manifestly covariant approach to quantum field theory and quantum gravity. The heat kernel $K(t; x, y; D) = \langle x | \exp(-tD) | y \rangle$ satisfies the heat conduction equation $(\partial_t + D_x)K = 0$ with $K(0;x,y;D) = \delta(x,y)$. The short-time expansion of $K$ in powers of $t$ generates the heat kernel coefficients $b_k(x,x)$, which encode:
- Short-distance behaviour of the propagator
- One-loop divergences and counterterms
- $1/m$ expansion of the effective action
- Quantum anomalies
- Various perturbative expansions of the effective action

### 2. Spectral Functions (Section 2)

The paper establishes the foundational differential geometry: operators of Laplace type $D = -(g^{\mu\nu}\nabla_\mu\nabla_\nu + E)$ on a vector bundle $V$ over a compact Riemannian manifold $M$. The connection $\omega$ and endomorphism $E$ are uniquely determined from the operator. Three spectral functions are related:
- **Heat kernel**: $K(t,f,D) = \text{Tr}_{L^2}(f \exp(-tD)) \sim \sum_{k\geq 0} t^{(k-n)/2} a_k(f,D)$
- **Zeta function**: $\zeta(s,f,D) = \text{Tr}_{L^2}(f D^{-s})$, related to the heat kernel via Mellin transform
- **Resolvent**: $R_l(z) = (D+z^2)^{-l}$

The heat kernel coefficients appear as residues of $\Gamma(s)\zeta(s,f,D)$ at poles $s = (n-k)/2$.

### 3. Relevant Operators and Boundary Conditions (Section 3)

Explicit expressions for $\omega$ and $E$ are derived for:
- **Scalar fields**: $E^{AB} = -\frac{1}{2}(U(\bar{\Phi})'')^{AB} - \xi R \delta^{AB}$
- **Bosonic strings**: Non-linear sigma model with B-field and gauge field; natural boundary conditions contain tangential derivatives
- **Spinor fields**: $D = \slashed{D}^2$ with $E = -\frac{1}{4}R + \frac{1}{4}[\gamma^\mu,\gamma^\nu]F_{\mu\nu} + \ldots$; bag boundary conditions via projector $\Pi_- = \frac{1}{2}(1 \pm i\gamma_n\gamma_5)$
- **Vector fields (Yang-Mills)**: $E^{\alpha\rho}_{\nu\beta} = -R^\rho_\nu\delta^\alpha_\beta + 2F(B)^{\gamma\rho}_\nu c^\gamma_{\beta\alpha}$; absolute and relative boundary conditions
- **Graviton**: Transverse-traceless decomposition; conformal factor problem

### 4. Heat Kernel on Manifolds Without Boundary (Section 4)

The central calculation uses Gilkey's method: write $a_k$ as a sum over all independent invariants of dimension $k$, then determine coefficients using:
- Product formula: $a_k(D) = \sum_{p+q=k} a_p(D_1) a_q(D_2)$ for $D = D_1 \otimes 1 + 1 \otimes D_2$
- Variational equations under local scale transformations (eqs. 4.7-4.9)
- Direct computation on $\mathbb{R}^n$ using plane-wave basis

The coefficients $\alpha_I$ are shown to be dimension-independent (only the overall $(4\pi)^{-n/2}$ factor depends on $n$).

### 5. Manifolds with Boundaries (Section 5)

Half-integer powers of $t$ appear when boundaries are present. Explicit formulas are given for:
- Dirichlet boundary conditions ($a_1$ through $a_5$)
- Neumann/Robin boundary conditions
- Mixed boundary conditions
- Oblique boundary conditions with tangential derivatives (Born-Infeld from open strings)
- Spectral (Atiyah-Patodi-Singer) boundary conditions with $\ln t$ asymptotics

### 6. Singularities (Section 6)

Covers non-integrable potentials, conical singularities, domain walls/brane world geometries, non-smooth boundaries, and dielectric bodies.

### 7-9. Applications

- **Anomalies**: Conformal anomaly from $a_n(D)$ in $n$ dimensions; chiral anomaly from $a_n(\gamma_5, \slashed{D}^2)$; Index theorem
- **Resummation**: Modified large mass expansion, covariant perturbation theory, low-energy expansion, heat kernel on homogeneous spaces
- **Exact results**: Polyakov action; duality symmetry of the effective action

---

## Key Results

1. Heat kernel coefficients $a_0$ through $a_6$ for operators of Laplace type on closed manifolds (eqs. 4.26-4.29)
2. Complete boundary corrections to $a_0$ through $a_5$ for Dirichlet, Neumann/Robin, and mixed boundary conditions
3. Universal relation: all $\alpha_I$ constants are dimension-independent
4. Product formula for heat kernel coefficients on product manifolds
5. Yang-Mills one-loop coefficient $a_4^{[tot]}$ recovering the 11/3 beta function coefficient
6. Table of $a_4$ for spins 0, 1/2, 1, 2 in curved space
7. Heat kernel on domain walls with matching conditions across the singular surface
8. Conformal anomaly $= a_n(D)$ in even dimensions
9. Chiral anomaly from $a_n(\gamma_5, \slashed{D}^2)$ yielding the Index theorem
10. Eta function $\eta(0, \slashed{D})$ measuring spectral asymmetry

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Heat kernel | $K(t;x,y;D) = \langle x \| e^{-tD} \| y \rangle$ | Eq. (1.9) |
| Heat equation | $(\partial_t + D_x)K(t;x,y;D) = 0$ | Eq. (1.10) |
| Asymptotic expansion | $\text{Tr}(f e^{-tD}) \sim \sum_{k\geq 0} t^{(k-n)/2} a_k(f,D)$ | Eq. (2.21) |
| Laplace type operator | $D = -(g^{\mu\nu}\nabla_\mu\nabla_\nu + E)$ | Eq. (2.2) |
| $a_0$ | $a_0(f,D) = (4\pi)^{-n/2} \int_M d^n x \sqrt{g}\,\text{tr}_V\{f\}$ | Eq. (4.26) |
| $a_2$ | $a_2(f,D) = (4\pi)^{-n/2} \frac{1}{6} \int_M d^n x \sqrt{g}\,\text{tr}_V\{f(6E + R)\}$ | Eq. (4.27) |
| $a_4$ | $a_4(f,D) = \frac{(4\pi)^{-n/2}}{360} \int_M d^n x \sqrt{g}\,\text{tr}_V\{f(60E_{;kk} + 60RE + 180E^2 + 12R_{;kk} + 5R^2 - 2R_{ij}R_{ij} + 2R_{ijkl}R_{ijkl} + 30\Omega_{ij}\Omega_{ij})\}$ | Eq. (4.28) |
| $a_6$ | [Full expression with 28 curvature invariants and bundle terms] | Eq. (4.29) |
| Product formula | $a_k(x;D) = \sum_{p+q=k} a_p(x_1;D_1) a_q(x_2;D_2)$ | Eq. (4.2) |
| One-loop effective action | $W = \frac{1}{2}\ln\det(D) = -\frac{1}{2}\zeta'(0,D) - \frac{1}{2}\ln(\mu^2)\zeta(0,D)$ | Eq. (2.32)-(2.33) |
| Zeta regularization | $W_s = -\frac{1}{2}\tilde{\mu}^{2s}\Gamma(s)\zeta(s,D)$ | Eq. (2.29) |
| Residue formula | $a_k(f,D) = \text{Res}_{s=(n-k)/2}(\Gamma(s)\zeta(s,f,D))$ | Eq. (2.26) |
| Spinor endomorphism | $E = -\frac{1}{4}R + \frac{1}{4}[\gamma^\mu,\gamma^\nu]F_{\mu\nu} + i\gamma_5 D_\mu A^5_\mu - (n-2)A^5_\mu A^{5\mu}$ | Eq. (3.27) |
| Conformal coupling | $\xi = \frac{n-2}{4(n-1)}$ | Eq. (3.5) |
| Eta function | $\eta(s,D) = \sum \text{sign}(\lambda)|\lambda|^{-s}$ | Eq. (2.35) |
| Divergent part | $W_\Lambda^{\text{div}} = -(4\pi)^{-n/2}\int d^n x \sqrt{g}\{\sum \Lambda^{n-2j-2l} b_{2j} \frac{(-m^2)^l}{l!(n-2j-2l)} + \ldots\}$ | Eq. (1.21) |
| Yang-Mills $a_4^{[tot]}$ | $a_4^{[tot]} = \frac{11}{96\pi^2}\int d^4 x\sqrt{g}\,F^\delta_{\rho\nu}F^\gamma_{\rho\nu}K_{\delta\gamma}$ | Eq. (4.34) |
| Resolvent expansion | $\text{Tr}(R_l(z)) = \sum_k \frac{\Gamma(l + (k-n)/2)}{\Gamma(l)} a_k(D) z^{-2l+n-k}$ | Eq. (2.37) |

---

## Relevance to Phonon-Exflation

This is the single most important reference for the spectral action computations in the M4 x SU(3) framework. The heat kernel coefficients $a_0$, $a_2$, $a_4$ directly determine the spectral action via the Chamseddine-Connes formula $\text{Tr}(f(D_K^2/\Lambda^2)) \sim \sum f_k a_k$. The explicit formulas for $E$, $\Omega$, and all curvature invariants on product geometries are used in every computation computation involving the Seeley-DeWitt expansion on the internal SU(3) fiber. The product formula (eq. 4.2) is the structural backbone for separating external ($M^4$) and internal contributions. The boundary/domain-wall results (Section 6) are directly relevant to the domain wall physics at the fold.
