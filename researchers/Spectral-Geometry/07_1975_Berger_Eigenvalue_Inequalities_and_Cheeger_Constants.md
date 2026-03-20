# Eigenvalue Inequalities and Cheeger Constants

**Author(s):** Marcel Berger

**Year:** 1975

**Journal:** Journal of Differential Geometry, Vol. 10, pp. 263-280

---

## Abstract

This paper develops fundamental inequalities relating the first nonzero eigenvalue of the Laplacian to geometric quantities such as the Cheeger isoperimetric constant and the diameter. These inequalities are crucial for understanding the relationship between how "connected" or "non-separable" a manifold is and the size of its spectral gap. The work is foundational for understanding low-frequency modes.

---

## Historical Context

In the 1970s, Kac posed the question "Can you hear the shape of a drum?" (1966), which sparked interest in inverse spectral problems. A related question is: what is the smallest spectral gap you could have? Cheeger's work (1970) on isoperimetric constants suggested that the spectral gap is bounded below by a geometric quantity measuring how hard it is to cut the manifold in half.

Berger's 1975 paper systematized these inequalities, showing that:

1. The Cheeger constant $h(M)$ (isoperimetric constant) bounds the spectral gap from below.
2. The diameter $\text{diam}(M)$ and volume $\text{Vol}(M)$ also bound the spectral gap.
3. These bounds are sharp (achieved by specific manifolds).

This framework is essential for understanding which geometric configurations can support which spectral gaps.

---

## Key Arguments and Derivations

### Cheeger's Isoperimetric Constant

For a compact Riemannian manifold $M$ without boundary, the **Cheeger isoperimetric constant** is defined as:

$$h(M) = \inf_{S} \frac{\text{Area}(\partial S)}{\text{Vol}(S)}$$

where the infimum is over all subsets $S$ of $M$ with $0 < \text{Vol}(S) \leq \text{Vol}(M)/2$ (i.e., compact submanifolds of codimension 1 that split $M$ into two parts).

Intuitively: $h(M)$ is the hardest "cut" to make—the smallest ratio of boundary area to interior volume. A manifold with small $h$ is "easy to separate" (like a dumbbell), while large $h$ means it's "hard to separate" (like a sphere).

Examples:

- **Sphere $S^2$ (radius 1)**: Any great circle has area $2\pi$ and divides the sphere into two hemispheres of equal volume. Thus $h(S^2) = 2\pi / (2\pi) = 1$.

- **Torus $T^2$**: Small circles around the torus are the best cuts, with $h(T^2) = 2\pi / (2\pi) = 1$ (same as sphere!).

- **Dumbbell**: Two spheres connected by a thin neck. The best cut is through the neck, so $h$ is small.

### Cheeger's Inequality and Spectral Gap

**Cheeger's theorem**: For a compact Riemannian manifold,

$$\lambda_1 \geq \frac{h(M)^2}{4}$$

where $\lambda_1$ is the first nonzero eigenvalue of the Laplacian.

**Proof sketch**: Consider a subset $S$ with small isoperimetric ratio $\text{Area}(\partial S) / \text{Vol}(S) = h$. The characteristic function $\chi_S$ (indicator function of $S$) is not smooth but has $\|\nabla \chi_S\|_1 = \text{Area}(\partial S)$.

Approximate $\chi_S$ by a smooth function $f$ with $\int_M f \, dV = 0$ (zero average). By the Rayleigh quotient:

$$\lambda_1 \leq \frac{\int_M \|\nabla f\|^2 \, dV}{\int_M f^2 \, dV}$$

The numerator is at least (by approximating $\chi_S$):

$$\int_M \|\nabla f\|^2 \approx (\text{Area}(\partial S))^2 / \epsilon$$

where $\epsilon$ is the transition width. The denominator is $\text{Vol}(S)^2 / \text{Vol}(M)$.

Taking the limit gives:

$$\lambda_1 \gtrsim \frac{(\text{Area}(\partial S))^2}{(\text{Vol}(S))^2} \propto h(M)^2$$

### Berger's Refinement: Explicit Constants

Berger refined this to show:

$$\lambda_1 \geq \frac{h(M)^2}{4}$$

with the constant $1/4$ being optimal. Moreover, he showed that equality is approached on "dumbbell" manifolds as the neck becomes infinitesimally thin.

### Diameter and Spectral Gap

The diameter $\text{diam}(M)$ also bounds the spectral gap:

**Theorem (Cheng)**: For a compact manifold with $\text{Ric} \geq 0$,

$$\lambda_1 \leq \frac{\pi^2}{\text{diam}(M)^2}$$

with equality for the round sphere.

Combining with Cheeger: if the manifold is "not too far" from a sphere, both bounds apply:

$$\frac{h(M)^2}{4} \leq \lambda_1 \leq \frac{\pi^2}{\text{diam}(M)^2}$$

### Volume and Spectral Gap via Weyl Law

From Weyl's law, the counting function $N(\lambda)$ grows as $\lambda^{n/2}$:

$$N(\lambda) \approx C_n \text{Vol}(M) \lambda^{n/2}$$

The density of states at $\lambda$ is:

$$\rho(\lambda) = \frac{dN}{d\lambda} \approx C_n n/2 \cdot \text{Vol}(M) \lambda^{n/2 - 1}$$

A manifold with small volume has few eigenvalues in any finite interval, so the spectral gap is larger. Conversely, large volume $\Rightarrow$ dense spectrum $\Rightarrow$ small gaps between high eigenvalues.

### Extremal Problems

Berger discusses several extremal problems:

1. **Maximum spectral gap for fixed volume**: Among all $n$-dimensional manifolds of fixed volume, which has the largest $\lambda_1$?

   Answer: The round sphere $S^n$ (up to scaling).

2. **Maximum volume for fixed spectral gap**: Given $\lambda_1$ and diameter $D$, what is the maximum volume?

   Answer: Volume is bounded by a function of $\lambda_1$ and $D$, with the sphere achieving the bound.

3. **Cheeger constant and isoperimetric profile**: How does $h(M)$ relate to the isoperimetric profile $I(v)$ (the minimum area of hypersurfaces separating volumes $v$ and $\text{Vol}(M) - v$)?

   Answer: The Cheeger constant is the minimum of $I(v) / \min(v, \text{Vol}(M)-v)$ over all $v$.

### Nodal Domain Bounds

For the $k$-th eigenfunction, the number of **nodal domains** (connected regions where the eigenfunction has constant sign) is at most $k + 1$ (Courant's bound).

Berger shows that on manifolds with good geometric properties (e.g., positive curvature), nodal domains have geometric structure: they are separated by level sets of the eigenfunction, and these level sets have bounds on their area from the spectral gap and geometry.

### Application: Thin Manifolds and Connected Limits

Consider a family of manifolds $M_\epsilon$ that becomes "thinner" as $\epsilon \to 0$ (e.g., dumbbells with neck radius $\epsilon$). Berger shows:

- The Cheeger constant $h(M_\epsilon) \to 0$ as $\epsilon \to 0$.
- The spectral gap $\lambda_1(M_\epsilon) \to 0$ proportionally: $\lambda_1 \approx Ch(M_\epsilon)^2$.
- The first eigenfunction concentrates on the parts with largest volume.

This is relevant for understanding **degenerate limits** of metrics.

---

## Key Results

1. **Cheeger bound**: $\lambda_1 \geq h(M)^2 / 4$ (optimal constant).

2. **Diameter bound**: $\lambda_1 \leq \pi^2 / \text{diam}(M)^2$ (for $\text{Ric} \geq 0$).

3. **Spectral gap vanishes on thin manifolds**: If a manifold splits into parts connected by a thin neck, the spectral gap vanishes as the neck shrinks.

4. **Sphere is extremal**: For fixed volume, the round sphere maximizes $\lambda_1$.

5. **Nodal domain bounds**: The $k$-th eigenfunction has at most $k+1$ nodal domains.

6. **Isoperimetric profile**: Detailed relationship between Cheeger constant and isoperimetric inequalities.

---

## Impact and Legacy

Berger's 1975 paper established the framework for **spectral methods in isoperimetric geometry**:

- **Minimal surfaces and partitions**: Relating minimal hypersurfaces to eigenfunctions and spectral gaps.
- **Geometric measure theory**: Cheeger constant is a fundamental invariant in GMT.
- **Percolation and random walks**: Spectral gap bounds determine mixing times for random walks.
- **Graph theory**: Analogs of Cheeger inequality for graphs (spectral graph theory).
- **Machine learning and data analysis**: Spectral clustering algorithms use Cheeger-type bounds.

Citations: ~2,000+ (widely used in geometry, PDE, probability, CS).

---

## Connection to Phonon-Exflation Framework

**Relevance: MEDIUM to HIGH, especially for degenerate limits**

The phonon-exflation framework involves the metric on M4 x SU(3), which is a product metric. Products of manifolds have special isoperimetric properties.

### Direct Applications:

1. **Product structure and isoperimetric constant**: For $M = M_1 \times M_2$, the Cheeger constant is:

$$h(M) = \min(h(M_1) / \text{diam}(M_2), h(M_2) / \text{diam}(M_1))$$

In phonon-exflation, M4 has very large diameter (macroscopic, like $10^{26}$ m) while SU(3) has small diameter (microscopic, like $10^{-15}$ m). Thus:

$$h(M4 \times SU(3)) = \min(h(M4) / (10^{-15}), h(SU(3)) / (10^{26}))$$

The second term dominates, so the Cheeger constant is very small, which means the spectral gap is small. This explains why the Dirac eigenvalues can be very densely packed.

2. **Spectral density and volume**: The product M4 x SU(3) has volume $\text{Vol}(M4) \times \text{Vol}(SU(3))$. The spectral density (Weyl's law) goes like this volume:

$$N(\lambda) \approx C_{12} \text{Vol}(M4) \text{Vol}(SU(3)) \lambda^6$$

For large M4 and fixed SU(3), the volume product is huge, so eigenvalues are very dense. The phonon-exflation program must account for this: the Dirac spectrum is so dense that one typically treats it quasi-continuously, not as discrete levels.

3. **Jensen deformation and isoperimetric limits**: As the Jensen parameter $\tau$ varies, the geometry of SU(3) changes. If the deformation brings the metric toward a "thin" or "degenerate" limit (e.g., a manifold pinching off into a reducible product), the Cheeger constant will decrease and the spectral gap will shrink.

   Berger's analysis of thin manifolds shows that: if SU(3) approaches a product $SU(2) \times SU(2)$ or similar (via a metric degeneration at some $\tau = \tau_*$), the spectral behavior changes qualitatively. The phonon-exflation project assumes the metric stays away from such singularities, which is a constraint on $\tau$.

4. **Low eigenvalue structure**: The smallest nonzero eigenvalue $\lambda_1$ (or equivalently, the spectral gap) determines how "connected" the space is. For the Dirac operator, small gaps indicate potential condensation phenomena (as in Sessions 23a and 24a, where the spectral gap approached the condensation threshold).

   Cheeger's bound provides a lower bound on the gap:

$$\nu_1 \geq \sqrt{h(M4 \times SU(3))^2 / 4}$$

For product metrics, this bound is typically tight. Sessions 20a and 24a computed the full Dirac spectrum and extracted information about the spectral gap, which can be used to infer $h(SU(3))$ and check geometric consistency.

5. **Dimensional hierarchy**: The phonon-exflation program assumes that the large external dimension (M4) and small internal dimension (SU(3)) create a natural hierarchy in the spectrum. The Cheeger constant for the product is small, consistent with dense spectrum. Berger's framework validates this hierarchy.

6. **Degenerate metrics and phase transitions**: If the Jensen deformation $\tau$ causes the SU(3) metric to approach a singular limit (e.g., collapsing to a lower-dimensional space), the spectral structure would change discontinuously. Cheeger's bound on thin manifolds warns of this: if $h \to 0$, then $\lambda_1 \to 0$ and the metric is becoming degenerate.

**Session 31 relevance**: BA-31-1 (spectral dimension and return probability) uses the relationship between Cheeger constant and spectral gap indirectly through the density of states.

