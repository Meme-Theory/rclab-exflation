# The Ray-Singer Torsion

**Author(s):** John Lott
**Year:** 2023
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 2309.05688
**Relevance:** HIGH

---

## Abstract

In 1971, Ray and Singer proposed an analytic equivalent of a classical topological invariant, the R-torsion. This Ray-Singer torsion has had many ramifications in mathematics and physics. I will describe the background, the Ray-Singer papers and some subsequent work.

---

## Key Arguments and Derivations

### 1. R-Torsion (Topological Precedent)

The R-torsion was developed by Reidemeister, Franz, and de Rham to classify lens spaces up to combinatorial equivalence. For a finite chain complex C with preferred bases c_q for C_q and h_q for H_q, the torsion is:

log tau(C) = sum_{q=0}^{N} (-1)^q log[(b_q, h_q, b_{q-1})/c_q]

It is a PL (piecewise linear) invariant, not a homotopy invariant. Key properties: vanishes for even-dimensional oriented closed manifolds, satisfies a product formula T_{K x K'}(rho-hat) = chi(K) T_{K'}(rho).

### 2. Applications: Lens Spaces and Hauptvermutung

R-torsion distinguishes lens spaces that homotopy theory cannot. For instance, L(7,1) and L(7,2) are homotopy equivalent but not homeomorphic, as shown by their different R-torsion values. Milnor used a variant of R-torsion to disprove the Hauptvermutung for simplicial complexes.

### 3. Analytic Predecessors

The paper traces the analytic thread from the Riemann zeta function through Minakshisundaram-Pleijel (1948), who defined the zeta function of the Laplacian on compact Riemannian manifolds:

zeta_Delta(s) = sum_j (-lambda_j)^{-s}

and proved it extends meromorphically to C. McKean-Singer (1967) computed the first heat coefficients U_1(x,x) = R(x)/6 where R is scalar curvature.

### 4. The Ray-Singer Definition

For an acyclic chain complex, log tau(C) = (1/2) sum_{q=0}^{N} (-1)^{q+1} q log det(-Delta_q^{(c)}). Ray and Singer (1971) replaced combinatorial Laplacians with differential form Laplacians and regularized the determinant using zeta function regularization:

log det(Delta_q) = -zeta'_{Delta_q}(0)

The Ray-Singer analytic torsion is:

T_{RS} = exp((1/2) sum_{q=0}^{N} (-1)^{q+1} q log det(Delta_q))

They conjectured T_{RS} equals the R-torsion for acyclic representations.

### 5. Cheeger-Muller Theorem

The equality of Ray-Singer torsion and R-torsion was proved independently by Cheeger and Muller (1978-1979), later extended by Muller (1993) to unimodular representations and by Bismut-Zhang to arbitrary flat vector bundles.

### 6. Further Developments

The paper describes: the determinant line bundle (Quillen), holomorphic torsion forms (Bismut-Gillet-Soule), and analytic torsion forms. The determinant line bundle gives a geometric interpretation of torsion as a section of a line bundle over the moduli space of flat connections. The analytic torsion form is an "even form" generalization to families of manifolds.

---

## Key Results

1. **R-torsion** classifies lens spaces up to homeomorphism and disproves the Hauptvermutung.

2. **Ray-Singer analytic torsion** provides an analytic equivalent of R-torsion via zeta-regularized determinants of Hodge Laplacians.

3. **Cheeger-Muller theorem**: T_{RS} = T_{R-torsion} for compact manifolds with acyclic flat bundles.

4. **Minakshisundaram-Pleijel**: zeta_{Delta}(s) extends meromorphically with simple poles at d/2 - j.

5. **McKean-Singer**: Heat kernel expansion Tr(e^{t Delta}) ~ (4pi t)^{-N/2}(c_0 + c_1 t^{1/2} + c_2 t + ...) with boundary terms.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| R-torsion | $\log\tau(C) = \sum_{q=0}^{N}(-1)^q \log[(b_q, h_q, b_{q-1})/c_q]$ | Eq. (2.5) |
| Combinatorial det | $\log\tau(C) = \frac{1}{2}\sum_{q=0}^{N}(-1)^{q+1} q\log\det(-\Delta_q^{(c)})$ | Eq. (2.8) |
| Riemann zeta | $\zeta(s) = 1 + \frac{1}{2^s} + \frac{1}{3^s} + \ldots$ | Eq. (3.1) |
| Heat trace circle | $\mathrm{Tr}(e^{t\partial_x^2}) = 1 + 2\sum_{j=1}^{\infty} e^{-t(2\pi j/L)^2}$ | Eq. (3.4) |
| Zeta-heat relation | $2\left(\frac{L}{2\pi}\right)^{2s}\zeta(2s) = \frac{1}{\Gamma(s)}\int_0^\infty t^{s-1}(\mathrm{Tr}(e^{t\partial_x^2})-1)dt$ | Eq. (3.5) |
| Heat kernel | $K(t,x,y) = \frac{1}{\sqrt{4\pi t}}\sum_{k\in\mathbb{Z}} e^{-|x-y-kL|^2/4t}$ | Eq. (3.6) |
| M-P zeta function | $\zeta_\Delta(s) = \sum_j (-\lambda_j)^{-s}$ | Eq. (3.11) |
| M-P parametrix | $H(t,x,y) = (4\pi t)^{-N/2}e^{-r^2/4t}(U_0 + U_1 t + \ldots + U_n t^n)$ | Eq. (3.9) |
| Product formula | $T_{K\times K'}(\hat{\rho}) = \chi(K) T_{K'}(\rho)$ | Eq. (2.7) |
| McKean-Singer | $U_1(x,x) = R(x)/6$ | Sec. 3.3 |

---

## Relevance to Phonon-Exflation

The Ray-Singer torsion and zeta-regularized determinants are the mathematical backbone of the spectral action. The project's computation of spectral action coefficients a_0, a_2, a_4 on M4 x SU(3) relies on exactly the Minakshisundaram-Pleijel heat kernel expansion and zeta function regularization described here. The Cheeger-Muller theorem's connection between analytic and topological invariants underlies the topological robustness of the spectral action approach. The eta invariant extension (connecting to paper 15 in this collection) is directly relevant to the project's BDI classification and APS boundary conditions.
