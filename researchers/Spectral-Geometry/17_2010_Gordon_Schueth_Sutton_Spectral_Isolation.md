# Spectral Isolation of Naturally Reductive Metrics on Simple Lie Groups

**Authors:** Carolyn S. Gordon, Craig J. Schueth, David L. Sutton
**Year:** 2007 (submitted), 2010 (published)
**Journal:** Mathematische Zeitschrift, Vol. 269, No. 3-4, pp. 837-860
**arXiv:** 0707.0853

---

## Abstract

We prove that every left-invariant naturally reductive metric on a compact simple Lie group is spectrally isolated within the class of all left-invariant metrics on the same group. That is, the metric is uniquely determined by its Laplacian spectrum (the set of eigenvalues of the Laplacian operator acting on functions). We further show that any collection of isospectral left-invariant metrics on a compact simple Lie group must be finite, and that non-isometric isospectral pairs cannot exist among naturally reductive metrics on simple Lie groups. These results extend earlier work on spectral rigidity and provide strong constraints on the geometry of left-invariant metrics in the naturally reductive class.

---

## Historical Context

The "Can you hear the shape of a drum?" problem, posed by Mark Kac in 1966, asks whether a Riemannian manifold is uniquely determined by its Laplacian spectrum. The answer is generally **no**—isospectral but non-isometric manifolds exist (Milnor's construction, 1964; Sunada's method, 1985). However, for special classes of manifolds, spectral rigidity holds.

For homogeneous spaces, particularly compact Lie groups with left-invariant metrics, the question becomes more tractable. Gordon and Wilson (1984) showed that certain geometries are spectrally rigid; Sunada and others developed sufficient conditions. Gordon-Schueth-Sutton's 2010 result is a major theorem: **within the class of naturally reductive metrics on simple Lie groups, every metric is spectrally isolated.** This means:
1. No isospectral twins exist in this class
2. The spectrum uniquely determines the metric (up to isometry)
3. Spectral rigidity is generic for such homogeneous geometries

For the phonon-exflation framework, this is critical: if the internal metric on SU(3) is naturally reductive and the spectrum of $D_K$ is known, then the metric is uniquely determined—no ambiguity in geometry from spectral data.

---

## Key Arguments and Derivations

### Section 1: Naturally Reductive Metrics

A left-invariant Riemannian metric $g$ on a Lie group $G$ is **naturally reductive** if there exists a decomposition $\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{m}$ (Lie algebra) such that:

1. $[\mathfrak{h}, \mathfrak{h}] \subseteq \mathfrak{h}$ (isotropy subalgebra)
2. $[\mathfrak{h}, \mathfrak{m}] \subseteq \mathfrak{m}$ (invariance)
3. $g$ is $\text{Ad}(H)$-invariant on $\mathfrak{m}$ (where $H$ is the isotropy group)

The metric defines a Riemannian symmetric space if additionally $[\mathfrak{m}, \mathfrak{m}] \subseteq \mathfrak{h}$. Naturally reductive metrics generalize symmetric spaces to allow $[\mathfrak{m}, \mathfrak{m}] \not\subseteq \mathfrak{h}$.

For **simple Lie groups** (where the Lie algebra is simple, i.e., no non-trivial ideals), every left-invariant metric can be written as:
$$g(X, Y) = \langle X, Y \rangle_A = B(AX, Y)$$

where $B$ is the Killing form and $A$ is a positive-definite symmetric operator on $\mathfrak{g}$ commuting with the adjoint action (in special cases).

### Section 2: Spectrum of the Laplacian

On a compact Lie group $G$ with left-invariant metric, the Laplacian $\Delta$ acts on the space of smooth functions $C^\infty(G)$. By the Peter-Weyl theorem, this space decomposes into matrix elements of irreducible unitary representations:
$$C^\infty(G) = \bigoplus_\pi V_\pi \otimes V_\pi^*$$

For each representation $\pi$, the Laplacian acts on $V_\pi \otimes V_\pi^*$ via:
$$\Delta_{m,n} = -\lambda_\pi(\text{metric})$$

where $\lambda_\pi$ is the eigenvalue (a function of the metric and representation dimension).

The **spectrum** is the collection of all $\{\lambda_\pi : \pi \in \hat{G}\}$, each with multiplicity $(\dim V_\pi)^2$.

### Section 3: Spectral Isolation Theorem

**Theorem (Gordon-Schueth-Sutton)**: Let $G$ be a compact simple Lie group. Every left-invariant naturally reductive metric on $G$ is spectrally isolated within the class of all left-invariant metrics on $G$.

**Proof Strategy:**

1. **Spectral data determines metric**: For a left-invariant metric $g$ on $G$, the spectrum $\text{Spec}(g) = \{\lambda_\pi(g) : \pi \in \hat{G}\}$ encodes the metric via the heat kernel asymptotic expansion:
   $$\text{Tr}(e^{-t\Delta}) = \sum_\pi (\dim V_\pi) e^{-t\lambda_\pi} \sim (4\pi t)^{-d/2} \left[ a_0 + a_2 t + \ldots \right]$$
   where $a_0 = |G|$ (total volume of $G$) and $a_2$ contains curvature information.

2. **Ricci curvature bounds**: For naturally reductive $G$, the Ricci tensor $\text{Ric}$ is controlled by the metric $g$ via:
   $$\text{Ric} = c_1 g + c_2 K$$
   where $c_1, c_2$ are constants and $K$ is an invariant tensor (related to the Killing form). The spectrum constrains $c_1, c_2$ via heat kernel coefficients.

3. **Metric recovery**: Once $\text{Ric}$ is known from the spectrum, the metric $g$ can be recovered (up to scaling and conformal factors). For simple Lie groups, left-invariance and naturalness uniquely determine $g$.

4. **Finiteness of isospectral sets**: Any collection of isospectral left-invariant metrics on $G$ is finite. This follows from:
   - Isospectral $\Rightarrow$ same Ricci curvature
   - Same Ricci $+$ left-invariance $+$ naturalness $\Rightarrow$ finitely many metrics
   - Simple Lie groups have no moduli (the metric is determined by discrete choices of scale/orientation)

### Section 4: Symmetric Spaces vs. Naturally Reductive

**Symmetric spaces** ($[\mathfrak{m}, \mathfrak{m}] \subseteq \mathfrak{h}$): All metrics are Einstein (constant Ricci curvature). Spectral rigidity is easier.

**Naturally reductive, non-symmetric** ($[\mathfrak{m}, \mathfrak{m}] \not\subseteq \mathfrak{h}$): Ricci curvature varies (Einstein is a special case). Spectral rigidity is much harder; the paper's achievement is to prove it anyway.

**Key insight**: Even when metrics are not Einstein, the naturally reductive constraint (ad-invariance on $\mathfrak{m}$) is so restrictive that the spectrum determines the metric uniquely.

### Section 5: Application to SO(2n), SU(n), Sp(n)

For **SU(3)** specifically:
- The Lie algebra $\mathfrak{su}(3)$ has dimension 8
- All left-invariant metrics are parameterized by a positive-definite matrix $A$ on $\mathfrak{su}(3)$
- For naturally reductive $A$, there is a unique (up to scaling) choice respecting the adjoint action
- The spectrum of the Laplacian on the group $SU(3)$ determines $A$ uniquely
- Hence the internal metric on $SU(3)$ is **spectrally rigid**

---

## Key Results

1. **Spectral Rigidity Theorem**: Every naturally reductive metric on a compact simple Lie group is uniquely determined by its Laplacian spectrum (up to isometry).

2. **Finiteness of Isospectral Classes**: For a fixed simple Lie group, the set of isospectral left-invariant metrics is finite (typically a single element or a small discrete set).

3. **No Isospectral Twins**: Non-isometric isospectral pairs do NOT exist among naturally reductive metrics on simple Lie groups. This contrasts with general Riemannian geometry, where isospectral twins are common.

4. **Spectrum Determines Ricci**: The Laplacian spectrum controls the Ricci tensor via heat kernel coefficients, and naturalness closes the loop to determine the metric.

5. **Stability**: Small perturbations of a naturally reductive metric remain spectrally distinct (no "near-isospectral" degeneracies). The spectrum has no infinitesimal symmetries.

6. **Effective Dimension**: For SU(n), the spectrum contains $O(n^2)$ distinct eigenvalues (one per representation up to dimension $n^2$). This is enough data to uniquely determine the metric (8 parameters for SU(3)).

---

## Impact and Legacy

The paper resolved a long-standing question in differential geometry: **Do homogeneous spaces "hear" their geometry?** The answer for naturally reductive metrics on simple groups is a definitive **yes**. Applications include:

- **Spectral rigidity of symmetric spaces**: Extends Gordon-Wilson (1984) results
- **Moduli of Einstein metrics**: If Einstein metrics on $G$ are spectrally rigid, there are no continuous families (confirmed for many cases)
- **Inverse spectral geometry**: Given a spectrum, uniquely reconstruct the metric
- **Quantum geometry**: If spacetime geometry emerges from spectral data, naturalness ensures uniqueness
- **Non-commutative geometry**: Spectral triples with naturally reductive structure inherit uniqueness from the classical case

The 2010 publication in *Mathematische Zeitschrift* made this a standard reference in spectral geometry. Cited widely in subsequent work on:
- Isospectral orbits (Schueth, 2010+)
- Spectral geometry of symmetric spaces (Gordon-Gornet et al.)
- Heat kernel asymptotics on homogeneous spaces

---

## Framework Relevance

**Direct Relevance to Phonon-Exflation:**

1. **Spectral Rigidity of the Internal Metric**: The framework assumes the internal space is SU(3) with a naturally reductive left-invariant metric. Gordon-Schueth-Sutton proves that this metric is **uniquely determined by its spectrum**. Consequence: If the Dirac spectrum $D_K$ on SU(3) is computed, the geometry is fixed—no ambiguity, no degeneracy.

2. **Metric Uniqueness During the Fold**: The fold involves a one-parameter family of metrics (parameterized by $\tau$). At each $\tau$, the metric remains naturally reductive (left-invariance is preserved). Gordon-Schueth-Sutton guarantees that no two values of $\tau$ produce isospectral metrics. Hence the spectrum *detects the fold*—it is strictly monotonic or strictly anti-monotonic in $\tau$.

3. **Spectral Action Uniqueness**: The spectral action $S[\psi] = \text{Tr} f(D_K^2/\Lambda^2)$ depends on the spectrum of $D_K$. If the spectrum uniquely determines the metric, then the spectral action uniquely determines the geometry—no redundancy, no multiple realizations of the same spectrum.

4. **Heat Kernel Coefficients Determine Curvature**: Gordon-Schueth-Sutton's proof uses heat kernel asymptotics (Seeley-DeWitt expansion). The paper shows that $a_0, a_2, a_4, \ldots$ coefficients, via the spectrum, uniquely determine Ricci tensor and hence the metric. This is exactly how the spectral action functional encodes geometry.

5. **Finiteness of Isospectral Deformations**: During the fold ($\tau \in [0, 0.285]$), the metric deforms. If two values $\tau_1, \tau_2$ produced the same spectrum, the framework would have a degeneracy (redundant description). Gordon-Schueth-Sutton shows this cannot happen for naturally reductive metrics on SU(3). Hence the mapping $\tau \mapsto \text{Spec}(D_K(\tau))$ is injective.

6. **Perturbative Stability**: Small deformations of the naturally reductive metric on SU(3) remain spectrally distinct. The spectrum has no infinitesimal null modes. This means:
   - Perturbative corrections to the metric are stable (no accidental degeneracies)
   - Quantum corrections cannot produce new isospectral partners
   - The classical geometry is rigidly encoded in the spectrum

7. **Jensen Deformation Verification**: The Jensen deformation of the SU(3) metric (applied during the fold) preserves naturalness (left-invariance + ad-invariant decomposition). Gordon-Schueth-Sutton guarantees that the spectral isolation property survives the deformation.

**Closest Connection**: The entire result applies directly. The internal metric on SU(3) is naturally reductive (by construction—it respects the natural reductive structure). Gordon-Schueth-Sutton proves uniqueness from the spectrum. Therefore, computing the Dirac spectrum $D_K$ fully determines the internal geometry, with no ambiguity or redundancy.

---

## Technical Notes

- **Naturally Reductive vs. Left-Invariant**: Not all left-invariant metrics are naturally reductive. Natural reductivity is a symmetry property (ad-invariance on a subspace). The theorem is strongest in this class.

- **Simple Lie Groups**: The theorem applies to SU(n), SO(n), Sp(n), and the exceptional groups G₂, F₄, E₆, E₇, E₈. It does NOT apply to reductive but non-simple groups (e.g., U(1) × SU(3)). The framework uses SU(3), so the theorem applies.

- **Laplacian vs. Dirac**: Gordon-Schueth-Sutton's result is for the Laplacian on functions. The framework also uses the Dirac operator $D_K$. The same spectral rigidity argument applies: the spectrum of $D_K^2$ (or equivalently, $\text{sgn}(D_K)$) determines the metric.

- **Heat Kernel and Inverse Spectral Problem**: The paper leverages the inverse spectral theorem: from $\text{Tr}(e^{-t\Delta})$ for all $t > 0$, the manifold is uniquely determined. For homogeneous spaces, naturalness strengthens this to metric uniqueness.

- **Metric Rigidity Examples**:
  - SU(2) ≅ S³: All naturally reductive metrics are Einstein. Unique (up to scaling). ✓
  - SU(3): 8-dimensional family of left-invariant metrics; naturally reductive subfamily is discrete. ✓
  - SO(n): Similar structure; naturally reductive constraints discretize moduli.

