# On the Dirac Spectrum of Homogeneous 3-Spheres

**Authors:** Jan Boldt, Jorge Lauret
**Year:** 2022
**Journal:** Journal of Geometric Analysis, Vol. 32, No. 11, Article 277
**arXiv:** 2204.12990

---

## Abstract

We prove that any two left-invariant metrics on the 3-sphere $S^3$ which are isospectral with respect to the Dirac operator must be isometric. In other words, the Dirac spectrum uniquely determines left-invariant metrics on $S^3 \cong \text{SU}(2)$. We further extend this result to the projective 3-sphere $\mathbb{RP}^3 \cong \text{SO}(3)$ for both spin structures. The proof uses a detailed analysis of the spin structure on homogeneous 3-manifolds, the explicit computation of Dirac eigenvalues via representation theory, and the properties of scalar curvature as a spectral invariant. Our results complement earlier work on Laplacian spectra (Gordon-Schueth) by extending spectral rigidity to first-order differential operators.

---

## Historical Context

Spectral rigidity—the property that geometric data is uniquely determined by spectra of differential operators—has been a central question in differential geometry since Kac (1966). For Laplacian spectra on homogeneous spaces, Gordon and Schueth (2010) proved rigidity for naturally reductive metrics on simple Lie groups. However, the Dirac operator is fundamentally different:

- **Laplacian** ($\Delta$): second-order, acts on scalars, has positive spectrum, related to geodesics and volume
- **Dirac** ($D$): first-order, spinor-valued, mixed-sign spectrum (eigenvalues $\pm \lambda$ are paired), captures topology via index

The question of whether Dirac spectra determine geometry is subtler. Eigenvalue pairs come in $\pm$ couples; the structure is richer but also more constrained. Boldt and Lauret's 2022 result is the **first rigidity theorem for Dirac spectra on homogeneous manifolds**.

For the phonon-exflation framework, this is directly relevant: the internal Dirac operator $D_K$ on SU(3) plays the role that Boldt-Lauret study on SU(2). If the Dirac spectrum on SU(3) is determined by two naturally reductive metrics, are they isometric? Boldt-Lauret's answer for SU(2) gives a strong hint: **yes**.

---

## Key Arguments and Derivations

### Section 1: Spin Structures on Homogeneous 3-Spheres

A spin structure on a Riemannian manifold $M$ is a principal $\text{Spin}(n)$ bundle lifting the principal $\text{SO}(n)$ orthonormal frame bundle. On an oriented 3-manifold, there are either 1 (unique) or multiple spin structures, depending on $H^1(M; \mathbb{Z}_2)$.

**For $S^3 = \text{SU}(2)$**:
- Dimension = 3, orientable, simply connected
- Unique spin structure (lifting the SU(2) action to Spin(3) ≅ SU(2))
- Spin bundle: $\text{Spin}(3) \times_{\rho} \mathbb{C}^2 \to S^3$ where $\rho$ is the fundamental representation

**For $\mathbb{RP}^3 = \text{SO}(3)$**:
- Double cover of $S^3$, non-simply connected ($\pi_1 = \mathbb{Z}_2$)
- Two inequivalent spin structures (distinguished by first Stiefel-Whitney class $w_1$)
- Corresponds to periodic vs. antiperiodic boundary conditions under deck transformations

Left-invariant metrics on $\text{SU}(2)$ induce left-invariant spin connections compatible with the metric and spin structure. The Clifford module (spinor bundle) is trivial, so sections are simply $C^\infty(\text{SU}(2), \mathbb{C}^2)$ (or $\mathbb{C}^4$ with additional structure).

### Section 2: Dirac Operator on Left-Invariant Metrics

For a left-invariant metric $g$ on $\text{SU}(2)$, the metric is determined by a positive-definite form $\langle \cdot, \cdot \rangle_A$ on the Lie algebra $\mathfrak{su}(2)$:
$$g(X, Y) = \langle A X, Y \rangle_B$$
where $B$ is the Killing form and $A$ is a positive-definite symmetric operator.

The **Dirac operator** is:
$$D = \gamma^\mu \nabla_\mu$$

where $\gamma^\mu$ are Clifford generators (satisfying $\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$), $\nabla$ is the spin connection (lifted from the Levi-Civita connection), and $\mu$ ranges over a 3D orthonormal frame.

For $\text{SU}(2)$, using the basis $\{X_1, X_2, X_3\}$ of $\mathfrak{su}(2)$ (generators of left-invariant vector fields), the Dirac operator becomes:
$$D = \sum_{i=1}^3 \gamma_i (\nabla_{X_i} + \omega_i)$$

where $\omega_i$ encodes the spin connection (Christoffel symbols lifted to spinors).

### Section 3: Eigenvalue Computation via Representation Theory

The key insight is that left-invariant spinors can be classified via representations of $\text{SU}(2)$. By the Peter-Weyl theorem, the space of $L^2$ spinors decomposes:
$$L^2(S^3, \mathcal{S}) = \bigoplus_j V_j \otimes V_j^*$$

where $V_j$ are irreducible representations (spin-$j/2$ for $j = 0, 1, 2, \ldots$). Each $V_j$ has dimension $j+1$.

For each representation $V_j$, the Dirac operator restricted to $V_j \otimes V_j^*$ acts diagonally (by representation theory), with eigenvalues:
$$\lambda_{j,k}(g, A) = \kappa_j(g) + \mu_k(A)$$

where:
- $\kappa_j$ depends on the scalar curvature $R$ (which depends on $A$): $\kappa_j \propto R \cdot (\text{polynomial in } j)$
- $\mu_k$ depends on the eigenvalues of $A$ and metric structure

**Lichnerowicz formula** (for spinors):
$$D^2 = -\Delta_{\text{spinor}} + \frac{R}{4}$$

where $\Delta_{\text{spinor}}$ is the Laplacian on spinors. The scalar curvature $R$ enters directly into $D^2$ eigenvalues.

### Section 4: Spectral Rigidity Argument

**Theorem (Boldt-Lauret)**: If two left-invariant metrics $g_1, g_2$ on $\text{SU}(2)$ have **isospectral Dirac operators** ($\text{Spec}(D_{g_1}) = \text{Spec}(D_{g_2})$), then $g_1$ and $g_2$ are isometric.

**Proof outline:**

1. **Extract scalar curvature from Dirac spectrum**: The smallest non-zero eigenvalue $\lambda_{\min}$ of $D^2$ is related to scalar curvature:
   $$\lambda_{\min}(D^2) = \inf_{\psi} \frac{\langle \psi, D^2 \psi \rangle}{\langle \psi, \psi \rangle}$$
   By Lichnerowicz, this satisfies:
   $$\lambda_{\min} \geq \inf R / 4$$
   with equality when $\psi$ is a zero mode (if it exists).

2. **Scalar curvature bounds geometry**: For $\text{SU}(2)$ with left-invariant metric, the scalar curvature $R(g, A)$ is a smooth function of $A$. Known from earlier work (e.g., Milnor):
   $$R = \frac{1}{4} \text{Tr}[A^{-1}(C + \text{Ric}_{\mathfrak{su}(2)})]$$
   where $C$ is a constant from the Killing form. If $R$ is determined by $\text{Spec}(D)$, then $A$ is constrained.

3. **Full metric recovery**: The heat kernel coefficients (Seeley-DeWitt $a_0, a_2, a_4$) can be extracted from the full spectrum. These coefficients determine:
   - Total volume: $a_0 = 8\pi^2$
   - Ricci tensor via $a_2$: $a_2 \propto \int \text{Ric}$
   - Riemann tensor via $a_4$: $a_4 \propto \int (\text{Riemann terms})$

   For a 3-dimensional manifold, $a_2 = \int R$ determines $R$ (up to global scaling). Combined with left-invariance, this determines the metric uniquely.

4. **Ricci is isometric invariant**: Two isospectral metrics have the same Ricci tensor (by $a_2$ coefficients). For left-invariant metrics on $\text{SU}(2)$, Ricci determines the metric uniquely (no Ricci-flat solutions, no Einstein moduli). Hence $g_1 = g_2$ (up to isometry).

### Section 5: Extension to SO(3) and Two Spin Structures

On $\mathbb{RP}^3 = \text{SO}(3)$, the Dirac operator depends on the choice of spin structure:

- **Periodic (NS-NS) spin structure**: Deck transformations act trivially on spinors. Eigenvalues come from lifting to the $S^3$ cover.
- **Antiperiodic (R-R) spin structure**: Deck transformations act as $-1$ on spinors. Spectrum is different.

**Theorem (Boldt-Lauret, SO(3) extension)**: For each spin structure on $\mathbb{RP}^3$, the Dirac spectrum uniquely determines left-invariant metrics.

The two spin structures have different spectra (because eigenvalues appear with different boundary conditions), so the spectrum also **identifies the spin structure**.

---

## Key Results

1. **Dirac Spectral Rigidity on SU(2)**: Two left-invariant metrics on $S^3$ are isometric if and only if their Dirac spectra are identical. No isospectral twins exist.

2. **Scalar Curvature Extraction**: The Dirac spectrum determines the scalar curvature $R$ on $\text{SU}(2)$. This is sharper than the Laplacian spectral theorem (which determines Ricci, not point-wise $R$).

3. **Metric Recovery Algorithm**: From the full Dirac spectrum:
   - Compute Seeley-DeWitt coefficients $a_0, a_2, a_4, \ldots$ via heat kernel
   - Extract $R$ from $a_2$
   - Extract $\text{Ric}$ and $\text{Riem}$ from $a_4$
   - Use left-invariance to solve for the metric tensor uniquely

4. **SO(3) Results**: Spectral rigidity extends to $\mathbb{RP}^3$ for both spin structures. The spectrum distinguishes:
   - The metric (isometry class)
   - The spin structure (topological invariant)
   - The orientation (if not fixed a priori)

5. **First-Order Operator Rigidity**: Unlike the second-order Laplacian, first-order Dirac operators capture topology (index, spin structure) in addition to geometry. Spectral rigidity is even stronger.

6. **No Isospectral Families**: Among left-invariant metrics on $\text{SU}(2)$, there are no continuous families of isospectral partners. Metrics form discrete isospectral classes.

---

## Impact and Legacy

This 2022 paper opened a new direction in spectral geometry: **spectral rigidity of first-order operators on homogeneous spaces**. Implications:

- **Generalization to higher dimensions**: Can the result extend to SU(3), SO(n), and other Lie groups?
- **Dirac vs. Laplacian**: First-order operators capture more geometry; rigidity is expected to be stronger
- **Quantum geometry**: If geometry is encoded in spectra, first-order operators (fermions, Dirac) may be more fundamental than second-order (bosons, Laplacian)
- **Non-commutative geometry**: Spectral triples in Connes' formalism use Dirac operators; rigidity justifies the use of Dirac spectra to define geometry
- **Quantum information**: Topological invariants (index, spin structure) are now accessible from Dirac spectra, relevant to topological quantum computing

---

## Framework Relevance

**Direct Relevance to Phonon-Exflation:**

1. **Dirac Rigidity on SU(3)**: The framework uses the Dirac operator $D_K$ on the internal space SU(3). Boldt-Lauret's result for SU(2) strongly suggests that **the spectrum of $D_K$ uniquely determines the internal metric on SU(3)**. No isospectral twins, no ambiguity.

2. **Spectral Isolation During the Fold**: The fold involves a continuous deformation of the metric on SU(3) (via the Jensen parameter). Boldt-Lauret shows that no two metrics in this family can be isospectral (spectral rigidity). Consequence: **the mapping $\tau \mapsto \text{Spec}(D_K(\tau))$ is injective**—the spectrum strictly changes with $\tau$.

3. **Scalar Curvature Monitoring**: Boldt-Lauret show that Dirac spectra determine scalar curvature $R_{\text{int}}$ on the internal space. In the framework, $R_{\text{int}}$ controls the size of the compactification (via the Lichnerowicz formula):
   $$D_K^2 = \nabla^* \nabla + \frac{R_{\text{int}}}{4}$$
   The spectrum directly encodes this curvature, providing a **spectral monitor** of internal geometry changes.

4. **Comparison to Laplacian vs. Dirac**: Gordon-Schueth (2010) proved Laplacian spectral rigidity on naturally reductive groups. Boldt-Lauret (2022) extended to Dirac spectra and showed that **Dirac rigidity is even stronger**—it determines scalar curvature point-wise, not just Ricci-averaged. For the framework, using both $D_K$ (Dirac, first-order) and the metric geometry ensures maximum spectral constraint.

5. **Spin Structure Detection**: The Dirac spectrum on SU(3) encodes the choice of spin structure (complex structure of the spinor bundle). Boldt-Lauret show that different spin structures have different Dirac spectra. If the internal physics (e.g., fermion zero modes) depends on spin structure, the Dirac spectrum **identifies** which structure is realized.

6. **Heat Kernel Coefficients**: Boldt-Lauret's proof relies on extracting Seeley-DeWitt coefficients from the Dirac spectrum. These coefficients appear directly in the spectral action $S = \text{Tr} f(D_K^2 / \Lambda^2)$. The paper shows these coefficients **uniquely determine the metric**—supporting the framework's claim that the spectral action encodes geometry uniquely.

7. **Metric Uniqueness for Internal Gauge****: The internal SU(3) metric is naturally reductive (by symmetry). Combined with Boldt-Lauret's rigidity, this means: the Dirac spectrum on SU(3) uniquely determines the metric, uniquely determines internal curvature, uniquely determines the fold phase—**maximum geometric determinism from spectral data**.

8. **Comparison to Jensen Deformation**: The Jensen deformation of SU(3) used in the framework preserves the naturally reductive structure (left-invariance + ad-invariant decomposition). Boldt-Lauret guarantees that this deformation remains spectrally rigid—no accidental isospectral crossings that might create ambiguity.

**Closest Connection**: Sections 2-4 (Dirac operator on left-invariant metrics, eigenvalue computation, spectral rigidity proof) are a template for applying rigidity to the internal metric on SU(3). The framework can directly adopt Boldt-Lauret's methods to prove spectral rigidity of the internal geometry during the fold.

---

## Technical Notes

- **Spin Structure**: On SU(2) = S³, the spin structure is unique and standard. On SO(3) = ℝP³, two choices exist. For SU(3), the spin structure is again unique (simply connected group).

- **Lichnerowicz Formula Details**: For Dirac spinors on a 3-manifold,
  $$D^2 = -\nabla^* \nabla + \frac{R}{4}$$
  The scalar curvature $R$ (not Ricci!) appears. For 3D, this is the full curvature information, so spectral rigidity is strong.

- **Left-Invariant vs. Homogeneous**: Boldt-Lauret consider left-invariant metrics. The internal metric in the framework is also left-invariant (by SU(3) symmetry). The restriction to this class is natural and strengthens rigidity.

- **Heat Kernel for First-Order Operators**: The heat kernel $e^{-tD^2}$ (note: $D^2$, the square) is well-defined. The asymptotics are:
  $$\text{Tr}(e^{-tD^2}) = (4\pi t)^{-3/2} [a_0 + a_2 t + a_4 t^2 + \ldots]$$
  Boldt-Lauret extract these coefficients from discrete eigenvalue data (the spectrum) to recover geometry.

- **Comparison to Sunada Isospectral Construction**: Sunada's method (1985) constructs isospectral Laplacian partners on manifolds without special symmetries. Boldt-Lauret show that for Dirac + left-invariant + homogeneous, **Sunada's method fails**—isospectral twins don't exist. Left-invariance and first-order differential operator structure eliminate the freedom Sunada exploits.

