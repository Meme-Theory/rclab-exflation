# An Explicit Kaluza-Klein Reduction of Einstein's Gravity in 6D on S2

**Author(s):** Tekin Dereli and Yorgo Senikoglu
**Year:** 2026
**Journal:** (preprint)
**arXiv:** 2601.08443
**Relevance:** HIGH

---

## Abstract

We study a six-dimensional Kaluza-Klein theory with spacetime topology M4 x S2 and analyze the gauge sector arising from dimensional reduction. Using normalized Killing vectors on S2, we explicitly construct the reduced Yang-Mills action and determine the corresponding gauge kinetic matrix. Despite the SO(3) isometry of S2, we show that only two physical gauge fields propagate in four dimensions. The gauge kinetic matrix therefore has rank two and possesses a single zero eigenvalue. We demonstrate that this degeneracy is a direct consequence of the coset structure S2 = SO(3)/SO(2) and reflects a non-dynamical gauge direction rather than an inconsistency of the reduction. Our results clarify the geometric origin of gauge degrees of freedom in Kaluza-Klein reductions on coset spaces.

---

## Key Arguments and Derivations

### Section 1: Introduction

The paper starts from pure 6D Einstein gravity on M4 x S2 and shows that Yang-Mills gauge structure emerges naturally from the geometry. Unlike the CSDR framework where the gauge field is an independent higher-dimensional ingredient, here the internal metric components play the role of gauge potentials. The resulting 4D theory reproduces Einstein-Yang-Mills with canonical gauge kinetic terms and scalar fields from internal curvature.

### Section 2: Theoretical Framework

The six-dimensional manifold M6 has product topology M4 x S2, with S2 = SO(3)/SO(2). Frame indices A, B = 0,1,2,3,5,6, with a,b = 0,1,2,3 for M4 and alpha = 5,6 for S2.

The three Killing vectors on S2 (coordinates xi, eta) are:
- K_1 = -sin(eta) d/d xi - cos(eta) cot(xi) d/d eta
- K_2 = cos(eta) d/d xi - sin(eta) cot(xi) d/d eta
- K_3 = d/d eta

The KK ansatz for the coframe is:
- e^a(x, y^m) = e^a(x) for a = 0,1,2,3
- e^alpha = phi(x) [b^alpha + A^i b_alpha(K_i)] for alpha = 5,6 and i = 1,2,3

where b^5 = d xi, b^6 = sin(xi) d eta, phi(x) is a scalar field, and A^i are gauge 1-forms on M4.

The full 6D metric is: G = g + phi^2(x) delta_{alpha beta} (b^alpha + A^i b_alpha(K_i))(b^beta + A^j b_beta(K_j))

The torsion-free Levi-Civita connection is computed via Cartan structure equations, yielding connection 1-forms Omega^{AB} involving the gauge field strengths F^i and scalar field phi.

### Gauge Kinetic Matrix

The Yang-Mills term from the dimensional reduction produces a gauge kinetic matrix:

M = [[sin^2(eta) + cos^2(xi)cos^2(eta), -sin^2(xi)sin(eta)cos(eta), -cos(xi)sin(xi)cos(eta)],
     [-sin^2(xi)sin(eta)cos(eta), cos^2(eta) + cos^2(xi)sin^2(eta), -cos(xi)sin(xi)sin(eta)],
     [-cos(xi)sin(xi)cos(eta), -cos(xi)sin(xi)sin(eta), sin^2(xi)]]

This matrix has det(M) = 0, eigenvalues lambda_1 = 0 (multiplicity 1) and lambda_2 = 1 (multiplicity 2).

The zero eigenvalue means one gauge field is non-dynamical. An orthogonal diagonalization yields eigenfield 2-forms:
- F-bar^1 = cos(eta)sin(xi)F^1 + sin(eta)sin(xi)F^2 + cos(xi)F^3 (non-dynamical, lambda = 0)
- F-bar^2 = -cos(eta)cos(xi)F^1 - sin(eta)cos(xi)F^2 + sin(xi)F^3 (dynamical)
- F-bar^3 = -sin(eta)F^1 + cos(eta)F^2 (dynamical)

### Reduced 4D Lagrangian

After integrating over S2 (L_6 = L_4 wedge d xi wedge sin(xi) d eta):

L_4 = (phi^2/2) R^{ab} wedge *e_{ab} - (phi^4/8)(F-bar^2 wedge *F-bar^2 + F-bar^3 wedge *F-bar^3) + d phi wedge *d phi + *1

The scalar kinetic term d phi wedge *d phi has positive definite sign (no ghosts). The Yang-Mills sector contains exactly two dynamical gauge fields, consistent with the coset structure SO(3)/SO(2).

### Section 3: Conclusions

The degeneracy of the gauge kinetic matrix is traced to the coset structure S2 = SO(3)/SO(2). The non-dynamical direction corresponds to the SO(2) isotropy subgroup. Only the coset directions SO(3)/SO(2) propagate as gauge fields, reflecting the general principle that the gauge group emerging from KK reduction on G/H has rank equal to dim(G/H) for the zero modes.

## Key Results

1. Pure 6D Einstein gravity on M4 x S2 reduces to 4D Einstein-Yang-Mills with two dynamical gauge fields
2. The gauge kinetic matrix has rank 2 despite 3 Killing vectors on S2, with eigenvalues (0, 1, 1)
3. The zero eigenvalue is a geometric consequence of the coset structure SO(3)/SO(2)
4. The non-dynamical gauge direction corresponds to the isotropy subgroup SO(2)
5. The scalar field phi (breathing mode) has positive-definite kinetic term
6. The reduced 4D Lagrangian contains Einstein, Yang-Mills (2 fields), and scalar sectors with no ghosts

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| KK coframe | $e^\alpha = \phi(x)[b^\alpha + A^i b_\alpha(K_i)]$ | Eq. (3) |
| 6D metric | $G = g + \phi^2\,\delta_{\alpha\beta}(b^\alpha + A^i b_\alpha(K_i))(b^\beta + A^j b_\beta(K_j))$ | After Eq. (3) |
| Eigenfield (null) | $\bar{F}^1 = \cos\eta\sin\xi\,F^1 + \sin\eta\sin\xi\,F^2 + \cos\xi\,F^3$ | Eq. (11) |
| 4D Lagrangian | $L_4 = \frac{\phi^2}{2}R^{ab}\wedge\ast e_{ab} - \frac{\phi^4}{8}(\bar{F}^2\wedge\ast\bar{F}^2 + \bar{F}^3\wedge\ast\bar{F}^3) + d\phi\wedge\ast d\phi + \ast 1$ | Eq. (14) |
| 6D curvature scalar | $\frac{1}{2}R^{AB}\wedge\#e_{AB} = [\frac{1}{2}\pi^{ab}\wedge\ast e_{ab} - \mu_a^5\wedge\ast e^a - \sigma_a^6\wedge\ast e^a + \Lambda\ast 1]\wedge e^5\wedge e^6$ | Eq. (10) |
| Killing vectors | $K_1 = -\sin\eta\,\partial_\xi - \cos\eta\cot\xi\,\partial_\eta,\; K_3 = \partial_\eta$ | Sec. 2 |

## Relevance to Phonon-Exflation

1. **Direct analog to M4 x SU(3):** This paper studies M4 x S2 = M4 x SO(3)/SO(2), which is the simplest analog of the project's M4 x SU(3). The result that only dim(G/H) gauge fields propagate from a G/H internal space is directly relevant: for SU(3) with its 8-dimensional group manifold, the full 8 gauge fields are expected (SU(3) is a group, not a coset, so there is no isotropy degeneracy — all Killing vectors contribute).

2. **Gauge kinetic matrix rank:** The rank deficiency of the gauge kinetic matrix on a coset G/H = SO(3)/SO(2) has no analog for the SU(3) group manifold (which has a non-degenerate Cartan-Killing metric). This confirms that the project's full SU(3) fiber produces all 8 gauge fields without degeneracy.

3. **Breathing mode scalar:** The scalar phi parametrizing the S2 radius is the direct analog of the project's tau parameter (the radius/shape modulus of SU(3)). The positive-definite kinetic term for phi parallels the project's expectation for the tau kinetic term. The key difference is that in the project, tau is dynamical and undergoes a transit (fold).

4. **Cartan formalism:** The Cartan (vielbein) formalism used here is the same used in the project's computation of the Riemann tensor (147/147 checks, Session 20a) and the tau-dependent connection on SU(3).

5. **Yang-Mills from pure gravity:** The emergence of Yang-Mills from pure 6D gravity demonstrates the Kaluza-Klein mechanism that underpins the entire phonon-exflation framework. The project extends this to M4 x SU(3) where both gauge fields and matter (phononic excitations) emerge from the geometry.
