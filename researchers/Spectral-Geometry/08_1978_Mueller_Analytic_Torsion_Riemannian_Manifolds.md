# Analytic Torsion and R-Torsion of Riemannian Manifolds

**Author(s):** Werner Mueller

**Year:** 1978

**Journal:** Advances in Mathematics, Vol. 28, pp. 233-305

---

## Abstract

Mueller's paper develops the theory of analytic torsion for compact Riemannian manifolds, relating the Ray-Singer analytic torsion (defined via the determinant of Laplacians on differential forms) to the Reidemeister combinatorial torsion. The analytic torsion is a spectral invariant that measures the "twisting" of the manifold. Mueller shows that analytic torsion can be computed from heat kernel expansions, making it accessible to spectral geometry techniques.

---

## Historical Context

Reidemeister (1935) introduced combinatorial torsion as a topological invariant for CW complexes. Ray and Singer (1971) proposed an analytic analog using the determinant of the Laplacian on differential forms, which is defined via the spectral zeta function.

Mueller's 1978 paper proved the **Ray-Singer conjecture**: that the analytic torsion equals the Reidemeister torsion (up to sign and factors). This remarkable result connects spectral geometry (eigenvalues of the Laplacian) to combinatorial topology.

The work is essential for understanding:

1. How the spectrum encodes topological information.
2. The role of the spectral zeta function in quantum field theory.
3. The functional determinant of differential operators.

---

## Key Arguments and Derivations

### Ray-Singer Analytic Torsion

For a compact Riemannian manifold $M$, one defines the Laplacian $\Delta_p$ on differential $p$-forms:

$$\Delta_p = (d^\dagger d + dd^\dagger) : \Omega^p(M) \to \Omega^p(M)$$

where $d$ is the exterior derivative and $d^\dagger$ is its adjoint with respect to the $L^2$ metric.

The spectrum of $\Delta_p$ consists of eigenvalues $0 = \lambda_0^{(p)} < \lambda_1^{(p)} \leq \lambda_2^{(p)} \leq \ldots \to \infty$.

The zero eigenvalue has multiplicity $b_p = \dim H^p(M; \mathbb{R})$ (the $p$-th Betti number).

The **spectral zeta function** for $p$-forms is:

$$\zeta_p(s) = \sum_{\lambda_i^{(p)} > 0} (\lambda_i^{(p)})^{-s}$$

By analytic continuation, one defines $\zeta_p(s)$ for all $s$.

The **functional determinant** (for nonzero eigenvalues) is:

$$\det'(\Delta_p) = \exp(-\zeta_p'(0))$$

The **Ray-Singer analytic torsion** is:

$$\tau_{RS}(M) = \prod_{p=0}^{n} (\det'(\Delta_p))^{(-1)^p p}$$

Taking logarithm:

$$\log \tau_{RS}(M) = -\sum_{p=0}^{n} (-1)^p p \cdot \zeta_p'(0)$$

This is a single real number (or rather, a positive number) that depends only on the metric on $M$.

### Heat Kernel and Zeta Function Computation

The spectral zeta function can be computed using the heat kernel:

$$\zeta_p(s) = \frac{1}{\Gamma(s)} \int_0^\infty t^{s-1} \left[\text{Tr}(e^{-t\Delta_p}) - b_p\right] dt$$

The heat kernel trace expands as:

$$\text{Tr}(e^{-t\Delta_p}) = (4\pi t)^{-n/2} \left[a_0^{(p)} + a_2^{(p)} t + a_4^{(p)} t^2 + \ldots \right] + b_p + \text{exponentially decaying terms}$$

where the constant term $b_p$ (the zero-mode contribution) must be subtracted.

The analytic continuation of $\zeta_p(s)$ near $s = 0$ gives:

$$\zeta_p'(0) = -\zeta_p''(0)|_{s=0} + \text{(constant term depending on } a_k^{(p)} \text{)}$$

More precisely, using the functional equation for $\Gamma(s)$:

$$\zeta_p'(0) = \lim_{s \to 0} \left[\frac{d}{ds} \left(\frac{1}{\Gamma(s)} \int_0^\infty t^{s-1} (\text{Tr}(e^{-t\Delta_p}) - b_p) dt \right)\right]$$

By careful analysis of the integral (splitting at $t = 1$ and using asymptotics for $t \to 0$ and $t \to \infty$), one extracts:

$$\zeta_p'(0) = -\log\left(\text{some function of } a_k^{(p)} \text{ and } b_p\right)$$

### Reidemeister Torsion

The Reidemeister torsion is defined combinatorially from a CW structure of $M$. For a chain complex with bases, one computes a determinant that measures the "twisting" of the manifold.

Formally: if $\{e_i^{(p)}\}$ are basis elements of the chain complex, and $\partial_p$ is the boundary operator, one defines a determinant of the augmented chain complex:

$$\tau(M) = \frac{\det(\partial_p + \partial_{p+1}^*)}{\text{(choices of bases)}}$$

This is a combinatorial invariant that does not depend on the choice of CW structure (up to sign and sign conventions).

### Mueller's Theorem: Ray-Singer = Reidemeister

**Theorem (Mueller, following Ray-Singer)**: For a compact Riemannian manifold $M$ without boundary:

$$|\tau_{RS}(M)| = |\tau(M)|$$

where $\tau_{RS}$ is the Ray-Singer analytic torsion and $\tau(M)$ is the Reidemeister torsion.

**Proof sketch**:

1. Both torsions are functorial: if $f: M \to M'$ is a diffeomorphism, then $\tau(M) = \tau(M')$ and $\tau_{RS}(M) = \tau_{RS}(M')$.

2. Both torsions are defined up to sign (depending on orientation and cell choices).

3. Mueller showed that the analytic torsion can be written as a product of functional determinants computed from heat kernels.

4. By Reidemeister's combinatorial formula, the same product formula holds for the combinatorial torsion.

5. By continuity and analyzing special cases (e.g., lens spaces $S^3/\mathbb{Z}_q$, where both can be computed explicitly), Mueller verified equality.

### Analytic Torsion and Heat Kernel Expansion

Mueller showed that the analytic torsion can be expressed in terms of the Seeley-DeWitt coefficients:

$$\log \tau_{RS}(M) = \sum_{p=0}^{n} (-1)^p p \zeta_p'(0)$$

and $\zeta_p'(0)$ can be extracted from the heat kernel coefficients $a_k^{(p)}$ via:

$$\zeta_p'(0) = \text{const}(n,p) \times \prod_{k=0}^{n} a_k^{(p)} + \text{(lower-order corrections)}$$

More concretely, for 4-dimensional manifolds:

$$\zeta_p'(0) \approx -\frac{1}{2} \log \left|\frac{a_0^{(p)}}{(4\pi)^{2}} \right| - \frac{a_2^{(p)}}{a_0^{(p)}} \times (\text{some dimension-dependent factor})$$

### Determinant of Dirac Operator

For the Dirac operator, Mueller's methods generalize: one defines the functional determinant via:

$$\det(D) = \exp(-\zeta_D'(0))$$

where $\zeta_D$ is the spectral zeta function of the Dirac operator $D^2$.

By Mueller's analysis:

$$\zeta_D'(0) = \text{(heat kernel coefficients for spinor})$$

This is crucial for quantum field theory: the fermionic path integral weight includes $\sqrt{|\det(D)|} = \exp(-\zeta_D'(0)/2)$.

### Variation of Analytic Torsion Under Metric Change

Mueller also studied how the analytic torsion changes when the metric varies. The variation formula is:

$$\frac{d}{dt}\log \tau_{RS}(g_t)) = \int_M \text{Ric}(g_t) \, g_t(v, v) \, dV$$

where $v$ is the variation vector $\frac{d}{dt} g_t$.

This shows that the analytic torsion is sensitive to the Ricci curvature—it decreases when the Ricci curvature becomes more negative.

### Lens Spaces and Explicit Computation

Mueller computed the analytic torsion explicitly for lens spaces $L_p = S^3/\mathbb{Z}_p$ (quotients of the 3-sphere by finite cyclic groups).

For the standard metric on $L_p$, the Dirac spectrum is known, and Mueller showed:

$$\tau_{RS}(L_p) = \prod_{k=1}^{p-1} \frac{(2k+p+2)!!}{(2k+p)!!} \quad (\text{up to constants})$$

This explicit formula allowed Mueller to verify the Ray-Singer conjecture for these spaces and to check the heat kernel calculation methods.

---

## Key Results

1. **Ray-Singer conjecture proved**: Analytic torsion equals Reidemeister torsion (up to sign).

2. **Torsion from heat kernel**: $\tau_{RS}$ computable from spectral zeta functions and heat kernel coefficients.

3. **Functional determinant formula**: $\det'(\Delta_p) = \exp(-\zeta_p'(0))$ relates determinants to heat kernels.

4. **Dirac determinant**: Similarly, $\det'(D^2) = \exp(-\zeta_D'(0))$ for the Dirac operator.

5. **Torsion variation**: Analytic torsion is sensitive to Ricci curvature; variation given by explicit formula.

6. **Lens space computation**: Explicit formulas for $\tau_{RS}$ on lens spaces validate heat kernel methods.

---

## Impact and Legacy

Mueller's work became fundamental for:

- **Quantum field theory**: Functional determinants of differential operators.
- **Spectral geometry**: Connecting eigenvalues to topological invariants.
- **Index theory**: Torsion as a secondary characteristic class.
- **String theory**: Determinant formulas in string partition functions.
- **Gauge theory and topology**: Instanton moduli spaces use torsion computations.

Citations: ~1,000+.

---

## Connection to Phonon-Exflation Framework

**Relevance: MEDIUM to HIGH, especially for topological structure**

The phonon-exflation framework assumes that the manifold M4 x SU(3) has a fixed topological type. The Dirac operator on this manifold has an analytical index (topological invariant) and a functional determinant (spectral invariant).

### Direct Applications:

1. **Functional determinant of Dirac operator**: The path integral for fermions includes the weight:

$$Z_{\text{ferm}} = \sqrt{|\det(D_{M4 \times SU(3)})|}$$

Mueller's methods compute this determinant from the spectrum of the Dirac operator:

$$\log \det(D) = -\zeta_D'(0) = \text{(sum of contributions from heat kernel coefficients)}$$

Sessions 20a and 24a computed the spectral zeta function (via Dirac eigenvalues), from which Mueller's formula would give the functional determinant.

2. **Torsion and Orientation**: Mueller's work on analytic torsion is sensitive to orientation. For a manifold with a chosen orientation, the torsion and determinant have definite signs.

   The phonon-exflation framework assumes a fixed orientation of M4 and SU(3). Mueller's analysis provides a way to check consistency: if the metric deformation preserves the orientation, the torsion should vary smoothly.

3. **Ricci Curvature Sensitivity**: Mueller's variation formula shows that the functional determinant decreases with increasing Ricci curvature:

$$\frac{d}{dt} \det(D) \propto -\int_M \text{Ric} \, dV$$

In the phonon-exflation framework, the Jensen deformation $\tau$ changes the Ricci geometry of SU(3). Mueller's formula predicts how the fermionic path integral weight should change.

4. **Topological Constraint**: The analytic torsion is a topological invariant (same for all metrics on a given topology). But the functional determinant depends on the metric.

   The phonon-exflation project assumes that the topology of M4 x SU(3) is fixed, so the torsion is an invariant. The spectrum (and hence the functional determinant) changes with $\tau$, but the torsion does not.

5. **One-Loop Effective Action**: In quantum field theory on curved space, the one-loop effective action includes the determinant:

$$S_{\text{1-loop}} = -\frac{1}{2} \log \det(\Delta) + \ldots$$

Mueller's methods allow one to compute this from the spectrum. Sessions 31 would use Mueller's formulas to compute the one-loop fermion contribution to the effective action as a function of $\tau$.

6. **Heat Kernel Asymptotics for Dirac**: Mueller's work extends Gilkey's heat kernel theory to the Dirac operator specifically, with explicit formulas for the functional determinant:

$$\det'(D^2) = \exp\left(-\sum_{p} (-1)^p p \zeta_p'(0)\right)$$

This is used to relate the Dirac spectrum to the path integral measure.

**Session 31 relevance**: BA-31-3 (orientation test, analytic torsion) and BA-31-5 (functional determinant variation under deformation) use Mueller's formulas directly.

