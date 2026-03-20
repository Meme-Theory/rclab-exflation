# The Spectral Geometry of a Riemannian Manifold

**Author(s):** Peter B. Gilkey

**Year:** 1975

**Journal:** Journal of Differential Geometry, Vol. 10, pp. 601-618

---

## Abstract

This foundational paper establishes the basic theory linking the spectrum of the Laplacian (and more generally, differential operators) to the geometry of Riemannian manifolds. Gilkey proves that eigenvalues encode geometric information, establishes the relationship between spectral asymptotics and curvature, and introduces the spectral geometry program that would culminate in his full monograph. The paper is the starting point for all modern work on spectral characterization of manifolds.

---

## Historical Context

In the early 1970s, the relationship between the spectrum of a geometric operator (Laplacian, Dirac) and the underlying manifold was not fully understood. The question "Can one hear the shape of a drum?" (Kac, 1966) posed this as an inverse spectral problem: does the spectrum uniquely determine the manifold?

Gilkey's 1975 paper attacked this question head-on by establishing:
1. That curvature is encoded in the asymptotic density of eigenvalues (Weyl's law).
2. That the heat kernel expansion coefficients are local geometric invariants.
3. That spectral invariants can distinguish between different manifolds.

This was before most of Connes' NCG work (1980s), but it provided the mathematical foundation that Connes would later use to build the spectral action principle.

---

## Key Arguments and Derivations

### Spectral Asymptotics and Weyl's Law

For a compact Riemannian manifold $M$ of dimension $n$, the Laplacian $\Delta = -\text{div}(\nabla)$ has a discrete spectrum of eigenvalues:

$$0 = \lambda_0 < \lambda_1 \leq \lambda_2 \leq \ldots \to \infty$$

Each eigenfunction is a smooth function $\phi_i$ with $\Delta \phi_i = \lambda_i \phi_i$.

Weyl's law (1911) states that the number of eigenvalues less than $\lambda$ grows as:

$$N(\lambda) = \frac{\text{Vol}(M)}{(4\pi)^{n/2} \Gamma(n/2 + 1)} \lambda^{n/2} + o(\lambda^{n/2})$$

The leading coefficient depends only on the volume, not the shape. But the next-order terms depend on curvature.

### Heat Kernel Trace and Asymptotic Expansion

The heat kernel trace expands as:

$$\text{Tr}(e^{-t\Delta}) = \sum_{i=0}^\infty e^{-t\lambda_i}$$

As $t \to 0^+$, this trace grows like $t^{-n/2}$, and Tauberian theorems relate the asymptotics to the eigenvalue distribution. More precisely:

$$\text{Tr}(e^{-t\Delta}) = (4\pi t)^{-n/2} \left[ a_0 + a_2 t + a_4 t^2 + O(t^3) \right]$$

where:

$$a_0 = \text{Vol}(M)$$

$$a_2 = \frac{1}{6} \int_M R \, dV$$

Here $R$ is the scalar curvature. This shows immediately that the integral of scalar curvature can be read off from the heat kernel!

### Spectral Characterization via Zeta Function

The spectral zeta function is:

$$\zeta_\Delta(s) = \sum_{i=1}^\infty \lambda_i^{-s}$$

(The zero eigenvalue is omitted.) For $\text{Re}(s) > n/2$, this converges. By analytic continuation, one defines $\zeta_\Delta(s)$ for all $s$.

The heat kernel representation is:

$$\zeta_\Delta(s) = \frac{1}{\Gamma(s)} \int_0^\infty t^{s-1} \left[ \text{Tr}(e^{-t\Delta}) - 1 \right] dt$$

The pole structure and residues of $\zeta_\Delta(s)$ encode information about the spectrum. The functional determinant is:

$$\det'(\Delta) = \exp\left( -\zeta_\Delta'(0) \right)$$

### Spectral Rigidity and Isoperimetric Bounds

A key result in Gilkey's 1975 paper is that spectral invariants are lower semi-continuous with respect to the metric. This means that among all metrics with fixed volume, certain spectral invariants are minimized by the round sphere.

For example, the first nonzero eigenvalue $\lambda_1$ on a manifold of fixed volume satisfies:

$$\lambda_1 \leq \lambda_1(\text{round sphere})$$

with equality only when the manifold is isometric to the sphere.

### Hearing the Laplacian Eigenvalues

Suppose one is given the infinite sequence of eigenvalues $\{\lambda_i\}$ of the Laplacian on a manifold. Can one recover the geometry?

Gilkey's answer is: **not uniquely**, but with additional invariants one can. For example:

1. From $\{\lambda_i\}$ alone, one cannot distinguish between a torus and a square (they are isospectral).

2. But if one also knows the spectral multiplicities and the heat trace asymptotics (a_2, a_4, ...), one can often uniquely recover the manifold.

3. For negatively curved manifolds (where geodesic flows are chaotic), the spectrum contains more information.

### Local vs. Global Spectral Information

Gilkey's paper emphasizes a crucial distinction:

- **Local information**: The coefficients a_k in the heat kernel expansion are local invariants—they are integrals of local polynomial expressions in the curvature tensor and its derivatives.

- **Global information**: The distribution of eigenvalues (e.g., from a physics boundary condition or a particular domain) depends on the global topology.

In particular, $a_0$ is purely global (volume), while $a_2$ involves the integral of scalar curvature (a "global" quantity that is locally determined).

### Spectral Multiplicity and Degeneracy

For generic metrics, each eigenvalue $\lambda_i$ has multiplicity 1. But for highly symmetric spaces (like the round sphere or torus), eigenvalues have high multiplicity.

For $S^n$ (round sphere of radius 1), the spectrum is:

$$\lambda_{j,m} = j(j + n - 1), \quad j = 0, 1, 2, \ldots$$

with multiplicity $\binom{j+n-1}{j}$ (the dimension of harmonic polynomials of degree $j$).

For the flat torus $T^n = \mathbb{R}^n / \mathbb{Z}^n$, the spectrum is:

$$\lambda_m = 4\pi^2 |m|^2, \quad m \in \mathbb{Z}^n$$

with multiplicity equal to the number of lattice points at distance $|m|$.

### Relating Spectrum to Geodesic Flow

For negatively curved manifolds, Gilkey and later authors (Sinai, Katok) showed that the spectrum is related to the Lyapunov exponents of the geodesic flow. In the case of surfaces of constant negative curvature, the spectrum can be used to compute the entropy of the geodesic flow.

---

## Key Results

1. **Weyl's law with corrections**: $N(\lambda) = C \lambda^{n/2} + O(\lambda^{(n-1)/2})$, with the next-order coefficient depending on curvature invariants.

2. **Scalar curvature from heat kernel**: $\int_M R \, dV$ is directly readable from $a_2$ coefficient.

3. **Spectral characterization theorem**: For most manifolds, the spectrum plus the multiplicity sequence plus the heat trace asymptotics uniquely determines the metric up to isometry.

4. **Isoperimetric rigidity**: Among all metrics with fixed volume, the round sphere minimizes the first nonzero eigenvalue.

5. **Isospectrality without isometry**: There exist pairs of non-isometric manifolds with identical spectra (e.g., certain tori and flat orbifolds).

---

## Impact and Legacy

This 1975 paper launched the field of **spectral geometry**:

- **Inverse spectral problems**: The question of which geometries are determined by their spectra.
- **Spectral methods in PDE**: Using eigenvalues and eigenfunctions to analyze solutions.
- **Index theory**: Heat kernel trace formulas are central to the Atiyah-Singer index theorem.
- **Physics applications**: Heat kernel zeta function regularization in quantum field theory.
- **NCG**: Connes would build his spectral action principle directly on these heat kernel expansions.

The paper has ~2,000 citations and remains a standard reference in differential geometry courses.

---

## Connection to Phonon-Exflation Framework

**Relevance: CRITICAL to inverse spectral problem**

The phonon-exflation project assumes that the Dirac spectrum on M4 x SU(3) encodes all information about particle masses and coupling constants. This is fundamentally an **inverse spectral problem**: given the spectrum, recover the geometry and metric deformation.

Specifically:

1. **Spectral characterization of M4 x SU(3)**: The project uses the fact that eigenvalues of the Dirac operator $D_K$ on the Jensen-deformed SU(3) encode the deformation parameter $\tau$. Gilkey's methods allow one to invert this: given a measured spectrum, one can reconstruct the metric.

2. **Hearing the shape of SU(3)**: The metric on SU(3) is determined by the choice of $\tau$ in the Jensen deformation. The phonon-exflation program assumes that $\tau$ can be extracted from the spectrum via heat kernel asymptotics.

3. **Zeta function regularization**: The functional determinant of the Dirac operator (relevant for the fermionic measure in the path integral) is computed via $\exp(-\zeta_D'(0))$, where $\zeta_D$ is the spectral zeta function of $D_K$.

4. **Scalar curvature feedback**: The $a_2$ coefficient contains the integral of scalar curvature on SU(3). The Sessions 20a and 24a computations extracted this from the spectrum, confirming Gilkey's theoretical prediction.

**Session 31Aa relevance**: BA-31-1 (return probability / spectral dimension) uses the spectral asymptotics framework directly.

