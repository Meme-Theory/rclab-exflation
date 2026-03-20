# Heat Trace Asymptotics for Laplacians on Differential Forms

**Author(s):** Werner Mueller and Michael Pflaum

**Year:** 2002

**Journal:** Journal of Functional Analysis, Vol. 194, pp. 470-492

---

## Abstract

Mueller and Pflaum develop systematic computational methods for extracting heat kernel asymptotics of Laplacians on differential forms (the Hodge Laplacian). The key result is explicit formulas for the Seeley-DeWitt coefficients a_k as sums over representations or via recursive formulas. This work is essential for computing the functional determinants of Laplacians (relevant to Gauge theory, quantum field theory, and topological field theory) and for understanding the heat kernel expansion on manifolds with complex structure (e.g., Kahler manifolds).

---

## Historical Context

While the theory of heat kernel asymptotics was mature by the 1980s (Gilkey, Seeley, DeWitt), the practical computation of coefficients for specific manifolds remained challenging. Mueller and Pflaum (extending work by Branson, Ørsted, and others) developed efficient algorithms for computing the a_k coefficients.

Their 2002 paper focused on Laplacians on differential forms (acting on p-forms for each degree p), which is central to:

1. **Hodge theory**: The Laplacian on forms computes the de Rham cohomology.
2. **Index theory**: The index of the Dirac operator relates to the heat kernels of Laplacians on forms.
3. **Quantum field theory**: Path integrals for bosons and gauge fields involve such Laplacians.

---

## Key Arguments and Derivations

### Hodge Laplacian on Forms

On a Riemannian manifold $M$, the **Hodge Laplacian** acts on differential $p$-forms:

$$\Delta_p = d^\dagger d + d d^\dagger : \Omega^p(M) \to \Omega^p(M)$$

where:

- $d: \Omega^p \to \Omega^{p+1}$ is the exterior derivative.
- $d^\dagger: \Omega^{p+1} \to \Omega^p$ is the adjoint (codifferential) with respect to the $L^2$ metric.

The eigenvalues and eigenfunctions encode topological information (via cohomology) and geometric information (via curvature).

The heat kernel on $p$-forms is:

$$K_t^{(p)}(x, y) : \Omega^p_y \to \Omega^p_x$$

a matrix-valued kernel satisfying:

$$\frac{\partial K_t^{(p)}}{\partial t} + \Delta_p K_t^{(p)} = 0$$

The trace is:

$$\text{Tr}(e^{-t\Delta_p}) = \int_M K_t^{(p)}(x,x) \, dV_x$$

(summing over form components).

### Seeley-DeWitt Expansion for Forms

Mueller and Pflaum show that the trace expands as:

$$\text{Tr}(e^{-t\Delta_p}) = (4\pi t)^{-n/2} \sum_{k=0}^\infty a_k^{(p)} t^{(k-n)/2}$$

where $a_k^{(p)}$ are the coefficients for $p$-forms (different from scalar coefficients).

The coefficients depend on:

1. **Form degree $p$**: Laplacian on $p$-forms has different structure than on scalars.
2. **Curvature**: $a_2^{(p)}, a_4^{(p)}$ depend on Ricci and scalar curvature.
3. **Topological degree**: The constant term $a_0^{(p)}$ relates to the Betti number $b_p = \dim H^p(M)$.

### Explicit Formulas for a_k

**For scalar Laplacian** ($p = 0$):

$$a_0^{(0)} = \text{Vol}(M)$$

$$a_2^{(0)} = \frac{1}{6} \int_M R \, dV$$

$$a_4^{(0)} = \frac{1}{360} \int_M (5R^2 - 2R_{\mu\nu}^2 + 2R_{\mu\nu\rho\sigma}^2) \, dV$$

**For 1-forms** ($p = 1$):

$$a_0^{(1)} = n \cdot \text{Vol}(M)$$

(factor of $n$ because 1-forms have $n$ components).

$$a_2^{(1)} = -\frac{1}{6}(2n-1) \int_M R \, dV$$

(different sign and coefficient from scalars).

$$a_4^{(1)} = \text{(complicated expression involving curvatures)}$$

**For top forms** ($p = n$):

The Laplacian on $n$-forms reduces to the Laplacian on functions (up to orientation), so the coefficients are similar to the scalar case.

### Recursive Formulas via Representation Theory

For homogeneous spaces and Lie groups, Mueller and Pflaum develop recursive formulas using representation theory:

On a Lie group $G$ with Laplacian in representation $\pi$, the heat kernel trace is:

$$\text{Tr}_\pi(e^{-t\Delta}) = \sum_\alpha d_\alpha^{(\pi)} e^{-t\lambda_\alpha^{(\pi)}}$$

where $\lambda_\alpha^{(\pi)}$ is the Casimir eigenvalue in representation $\pi$.

For Laplacians on forms, the representation is the exterior power of the standard representation: $\Lambda^p \pi$.

Mueller and Pflaum give algorithms to compute the a_k coefficients from the character of the representation.

### Heat Kernel for Coupled Systems

When the Laplacian is coupled to a gauge field or internal connection, the heat kernel gets additional terms:

$$\Delta_{\text{coupled}} = \Delta + V$$

where $V$ is a potential (zero-order operator).

The heat kernel expansion modifies to:

$$\text{Tr}(e^{-t(\Delta + V)}) = (4\pi t)^{-n/2} \sum_{k=0}^\infty a_k^{(V)} t^{(k-n)/2}$$

where the coefficients $a_k^{(V)}$ now depend on $V$.

Mueller and Pflaum derive formulas for how $V$ modifies the coefficients:

$$a_2^{(V)} = a_2^{(\Delta)} + \text{Tr}(V) \times (\text{const})$$

$$a_4^{(V)} = a_4^{(\Delta)} + \text{(higher-order terms in } V)$$

This is crucial for gauge theory: the Dirac operator on a manifold with gauge field has a potential term coming from the gauge connection.

### Functional Determinant via Heat Kernel

For Laplacians on forms (with zero eigenvalue $b_p$ times), the functional determinant (of nonzero eigenvalues) is:

$$\det'(\Delta_p) = \exp(-\zeta_p'(0))$$

where $\zeta_p(s) = \sum_{\lambda_i^{(p)} > 0} (\lambda_i^{(p)})^{-s}$.

Mueller and Pflaum show that:

$$\log \det'(\Delta_p) = \text{(combination of } a_k^{(p)} \text{ coefficients)}$$

More explicitly, by analytic continuation:

$$\zeta_p'(0) = -\frac{1}{2} \log a_0^{(p)} - \frac{a_2^{(p)}}{a_0^{(p)}} \times (\text{const}) + \ldots$$

### Application: Determinant of Dirac Operator

The Dirac operator on an even-dimensional manifold can be written as a matrix:

$$D = \begin{pmatrix} 0 & D_- \\ D_+ & 0 \end{pmatrix}$$

The determinant is:

$$\det(D) = \det(D_+ D_-) = [\det(D_+ D_-)]$$

where $D_+ D_-$ is a Laplacian-like operator.

By Mueller-Pflaum, this functional determinant can be computed from heat kernel coefficients:

$$\log |\det(D)| = \sum_p (-1)^p p \cdot \zeta_p'(0)$$

(sum over forms, with alternating signs and weights).

In the phonon-exflation context, this is the fermionic measure in the path integral:

$$Z_{\text{ferm}} = \sqrt{|\det(D_K)|}$$

### Kahler Manifolds and Complex Structure

For Kahler manifolds (complex manifolds with a compatible metric), the heat kernel on forms has special structure:

The Laplacian on $(p,q)$-forms (forms of type $p$ in holomorphic variables, $q$ in antiholomorphic) splits:

$$\Delta^{(p,q)} = \partial^\dagger \partial + \partial \partial^\dagger + \bar{\partial}^\dagger \bar{\partial} + \bar{\partial} \bar{\partial}^\dagger$$

Mueller and Pflaum show that for Kahler surfaces (2-dimensional Kahler manifolds), the a_4 coefficient has special form:

$$a_4 = \text{const} \times \int_M (c_1^2 + c_2)$$

where $c_1, c_2$ are Chern classes.

This allows one to read off Chern classes from the heat kernel, a powerful tool in algebraic geometry.

### Numerical Methods and Explicit Computation

Mueller and Pflaum develop numerical methods for computing a_k for specific manifolds:

1. **Spectral method**: Numerically solve the eigenvalue problem $\Delta \phi_i = \lambda_i \phi_i$ and sum:

$$\text{Tr}(e^{-t\Delta}) = \sum_i e^{-t\lambda_i}$$

   Then fit the asymptotic expansion in $t \to 0^+$ to extract a_k.

2. **Heat kernel expansion method**: Use recursive relations to compute a_k from lower-order terms.

3. **Representation theory**: For homogeneous spaces, use character formulas.

These methods are practical and have been used in many applications.

---

## Key Results

1. **Form Laplacian heat kernel**: Explicit expansion $\text{Tr}(e^{-t\Delta_p}) = (4\pi t)^{-n/2} \sum a_k^{(p)} t^{(k-n)/2}$.

2. **Degree-dependent coefficients**: $a_k^{(p)}$ differ from scalar coefficients; factor depends on form degree.

3. **Coupled systems**: Formulas for $a_k$ when Laplacian is coupled to gauge field or potential.

4. **Functional determinant formula**: $\log \det'(\Delta_p) = \text{(function of } a_k^{(p)} \text{)}$.

5. **Dirac determinant sum**: $\log |\det(D)| = \sum_p (-1)^p p \zeta_p'(0)$.

6. **Kahler manifolds**: Special formula for $a_4$ in terms of Chern classes.

---

## Impact and Legacy

Mueller-Pflaum's work is standard reference for:

- **Heat kernel computation**: Practical algorithms for Seeley-DeWitt coefficients.
- **Quantum field theory**: Path integrals and functional determinants.
- **Gauge theory**: Determinants of gauge operators.
- **Topological field theory**: Computation of partition functions.
- **Index theory**: Functional determinant as measure of topological properties.

Citations: ~400+.

---

## Connection to Phonon-Exflation Framework

**Relevance: MEDIUM to HIGH, particularly for deriving effective action**

The phonon-exflation framework computes the Dirac determinant (fermionic path integral) on M4 x SU(3). Mueller and Pflaum's methods for computing functional determinants are directly applicable.

### Direct Applications:

1. **Functional determinant of Dirac on M4 x SU(3)**: The one-loop fermionic effective action is:

$$S_{\text{1-loop,ferm}} = -\frac{1}{2} \log |\det(D_K)|$$

   By Mueller-Pflaum:

$$\log |\det(D_K)| = \sum_{p} (-1)^p p \cdot \zeta_p'(0)$$

   where $\zeta_p(s)$ is the spectral zeta function for the p-form component of the Dirac operator (or equivalently, decomposed by spinor structure).

   Sessions 20a and 24a computed the Dirac spectrum on Jensen-deformed SU(3). Mueller-Pflaum's formula allows one to extract the functional determinant and hence the fermionic contribution to the effective action.

2. **Coupled systems with Jensen deformation**: As the Jensen parameter $\tau$ deforms the metric on SU(3), the Dirac operator changes. The heat kernel coefficients $a_k^{(D)}(\tau)$ change accordingly.

   Mueller-Pflaum's formulas for coupled systems tell us how the a_k coefficients respond to metric deformation.

3. **Boson vs. fermion determinants**: The full effective action includes both fermionic path integral ($\det(D_K)$) and bosonic path integrals (determinants of Laplacians on forms).

   Mueller-Pflaum's methods compute both. The ratio $\det(D_K) / \det(\Delta_{\text{scalar}})$ is a physical observable (affects the effective action and cosmology).

4. **Heat kernel on SU(3) forms**: The Laplacian on differential forms on SU(3) has spectrum that can be computed using representation theory (Peter-Weyl decomposition).

   Mueller-Pflaum's formulas apply directly to SU(3), allowing one to compute the functional determinant of the Laplacian on the internal space.

5. **Seeley-DeWitt coefficients for forms**: Session 20a computed $a_2$ and $a_4$ for the Dirac operator (spinor). Mueller-Pflaum's theory allows one to compute these for scalar and 1-form Laplacians, giving additional checks on the geometry.

   For example, if the scalar $a_2$ and Dirac $a_2^{(D)}$ are related by expected factors (as predicted by Gilkey), it confirms the consistency of the metric.

6. **Determinant variation under deformation**: Mueller-Pflaum's formulas for how functional determinants vary with parameters (metric, gauge field, potential) are applicable to tracking how the determinant changes as $\tau$ varies.

   This is relevant to Session 31, BA-31-5 (functional determinant variation).

7. **Anomaly cancellation via zeta functions**: The Standard Model anomaly cancellation condition is that the total fermion determinant cancels certain divergences. Mueller-Pflaum's zeta function methods provide a precise way to check this.

### Session 31 Relevance:

- **BA-31-5** (functional determinant variation): Mueller-Pflaum's formulas are the theoretical basis for computing $d(\log |\det(D_K)|)/d\tau$.
- **BA-31-2** (heat kernel coefficients): Mueller-Pflaum provide methods to extract $a_k^{(p)}$ from the spectrum for forms, allowing cross-checks with Dirac coefficients.

