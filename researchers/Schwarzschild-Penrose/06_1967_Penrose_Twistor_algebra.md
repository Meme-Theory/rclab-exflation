# Penrose, "Twistor Algebra" (1967)

**Citation:** R. Penrose, "Twistor Algebra," *Journal of Mathematical Physics* **8**, 345--366 (1967).
**DOI:** 10.1063/1.1705200

---

## 1. Synopsis

This paper introduces a fundamentally new algebraic framework for Minkowski spacetime---**twistor algebra**---in which any conformally covariant or Poincare covariant operation can be expressed. The elements of the algebra, called *twistors*, obey tensor-type combination rules but differ from ordinary tensors and spinors in a decisive respect: they encode **locational** properties in addition to directional ones. Where a spinor at a point captures the local rotational/null structure, a twistor captures an entire null geodesic (light ray) or, dually, a point in complexified compactified Minkowski space.

The paper establishes twistor space $\mathbb{T} = \mathbb{C}^4$ and its projectivisation $\mathbb{PT} = \mathbb{CP}^3$ as the arena in which spacetime physics is to be reformulated. Points of $\mathbb{CP}^3$ represent null lines (or complexified null lines) in Minkowski space $\mathbb{M}$; lines in $\mathbb{CP}^3$ represent real or complex points of $\mathbb{M}$. The complexified Minkowski space, completed by a null cone at infinity, is thus the *Klein representation* of projective twistor space.

---

## 2. Motivation: Why Twistor Space?

### 2.1 The Problem with Points

Classical physics and general relativity treat spacetime points as the fundamental substrate. Fields are defined on them; dynamics evolves them. But several converging lines of reasoning suggest this is wrong at the deepest level:

1. **Quantum gravity:** The uncertainty principle applied to the gravitational field implies that spacetime points cannot be operationally defined below the Planck scale. A formalism that does not begin with points may be better adapted to quantization.

2. **Conformal primacy:** The causal (null-cone) structure of spacetime---which determines the conformal geometry---is arguably more fundamental than the full metric. The conformal group $C(1,3) \cong SO(2,4)/\mathbb{Z}_2$ acts naturally on null rays, not on individual points with their metrical baggage.

3. **Complex analyticity:** The massless free-field equations (Maxwell, linearized gravity, neutrino) possess a rich complex-analytic structure that is invisible in the real spacetime picture but becomes manifest when the fields are lifted to a complex projective space.

4. **Spinorial naturalness:** Two-component spinor calculus, already shown by Penrose and others to be the natural language for relativistic geometry, finds its most complete expression when spinor pairs encoding both direction and position are treated as single objects---twistors.

### 2.2 The Core Idea

Penrose's radical proposal: **spacetime points are derived concepts, not fundamental ones.** The primary objects are twistors---elements of $\mathbb{C}^4$---and spacetime points emerge as secondary constructs via the *incidence relation*. A point in Minkowski space is not a primitive entity but corresponds to a complex projective line $\mathbb{CP}^1 \subset \mathbb{CP}^3$ in twistor space. Conversely, a twistor (projectively) corresponds to a totally null two-plane ($\alpha$-plane) in complexified Minkowski space, whose intersection with the real Lorentzian slice is a null geodesic.

This inversion of ontological priority---from points to null rays, from real to complex---is the conceptual heart of twistor theory.

---

## 3. Two-Component Spinor Calculus: The Foundation

### 3.1 The Spinor-Vector Correspondence

Twistor theory is built on the two-component spinor formalism. The key identification exploits the exceptional isomorphism

$$\text{Spin}(3,1) \cong SL(2,\mathbb{C}).$$

A real Minkowski vector $x^a$ (with $a = 0,1,2,3$) is placed in correspondence with a $2 \times 2$ Hermitian matrix:

$$x^{AA'} = \frac{1}{\sqrt{2}} \begin{pmatrix} x^0 + x^3 & x^1 + ix^2 \\ x^1 - ix^2 & x^0 - x^3 \end{pmatrix},$$

where unprimed spinor indices $A \in \{0, 1\}$ transform under $SL(2,\mathbb{C})$ and primed indices $A' \in \{0', 1'\}$ under the conjugate representation $\overline{SL(2,\mathbb{C})}$. The Minkowski metric becomes:

$$g_{ab}\, x^a x^b = 2\,\det(x^{AA'}).$$

A vector is null if and only if this determinant vanishes, i.e., if $x^{AA'}$ factorises as

$$x^{AA'} = \xi^A \bar{\xi}^{A'}$$

for some spinor $\xi^A$. The spinor $\xi^A$ (up to phase) defines the *flag-pole direction* of the null vector.

### 3.2 Spinor Index Conventions

- **Unprimed indices** $A, B, C, \ldots \in \{0, 1\}$: fundamental representation of $SL(2,\mathbb{C})$.
- **Primed indices** $A', B', C', \ldots \in \{0', 1'\}$: complex conjugate representation.
- **Raising and lowering** via the Levi-Civita spinors:

$$\varepsilon_{AB} = \varepsilon_{A'B'} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad \varepsilon^{AB} = \varepsilon^{A'B'} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$

$$\xi_A = \varepsilon_{AB}\,\xi^B, \qquad \xi^A = \varepsilon^{AB}\,\xi_B.$$

- **Spinor inner product:** $\xi^A \eta_A = \xi^0 \eta_0 + \xi^1 \eta_1 = \varepsilon_{AB}\,\xi^A\,\eta^B$ (antisymmetric).

### 3.3 Null Lines and Spinor Pairs

A null geodesic $\gamma$ in Minkowski space is characterised by two pieces of data:

1. **Direction:** a spinor $\pi_{A'}$ (up to scale) such that the null tangent vector is $p^{AA'} = \pi^A \bar{\pi}^{A'}$ (for real rays, $\pi^A$ is the complex conjugate of $\pi_{A'}$ under the reality structure; in the complexified setting they are independent).

2. **Position (moment about the origin):** the angular momentum about the origin projected into the self-dual part gives a spinor $\omega^A$ defined by the *moment relation*

$$\omega^A = i\,x^{AA'}\,\pi_{A'},$$

where $x^{AA'}$ is any point on the null line. The pair $(\omega^A, \pi_{A'})$ is independent of which point on $\gamma$ is chosen (the freedom $x^{AA'} \mapsto x^{AA'} + \lambda\,\pi^A\bar{\pi}^{A'}$ leaves $\omega^A$ invariant since $\pi_{A'}\bar{\pi}^{A'}\pi^A = 0$ in the complexified context, or more precisely, $\omega^A$ shifts by a term proportional to $\pi^A$ which vanishes projectively).

This pair $(\omega^A, \pi_{A'})$---a spinor defining direction plus a spinor defining position---is the *simplest type of twistor*.

---

## 4. Twistor Space

### 4.1 Definition

**Twistor space** $\mathbb{T}$ is the four-dimensional complex vector space $\mathbb{C}^4$ whose elements are written

$$Z^\alpha = (\omega^A,\; \pi_{A'}), \qquad \alpha = 0,1,2,3,$$

where:
- $\omega^A$ ($A = 0, 1$) is an unprimed two-component spinor,
- $\pi_{A'}$ ($A' = 0', 1'$) is a primed two-component spinor,
- The Greek twistor index $\alpha$ runs over $\{0, 1, 2, 3\}$ and packages both spinor parts into a single four-component object.

Explicitly, the components are:

$$Z^0 = \omega^0, \quad Z^1 = \omega^1, \quad Z^2 = \pi_{0'}, \quad Z^3 = \pi_{1'}.$$

### 4.2 Dual Twistor Space

The **dual twistor space** $\mathbb{T}^*$ consists of elements $W_\alpha = (\lambda_A,\; \mu^{A'})$ with the natural contraction:

$$Z^\alpha W_\alpha = \omega^A \lambda_A + \pi_{A'} \mu^{A'}.$$

This pairing is $SL(4,\mathbb{C})$-invariant and descends to a well-defined pairing on the projective spaces.

### 4.3 Complex Conjugation and the Hermitian Structure

Penrose defines a **pseudo-Hermitian conjugation** mapping twistors to dual twistors:

$$Z^\alpha = (\omega^A, \pi_{A'}) \;\;\longmapsto\;\; \bar{Z}_\alpha = (\bar{\pi}_A, \bar{\omega}^{A'}),$$

where the bar denotes ordinary complex conjugation of components together with interchange of primed and unprimed index positions. This is not an involution on $\mathbb{T}$ itself but rather a map $\mathbb{T} \to \mathbb{T}^*$ (i.e., it lowers the twistor index). The conjugation reflects the pseudo-Hermitian structure of signature $(+\,+\,-\,-)$ on $\mathbb{C}^4$.

### 4.4 Higher-Valence Twistors

Just as one builds higher-rank tensors from vectors, one builds **multi-index twistors** by tensor products:

$$T^{\alpha\beta\cdots}{}_{\gamma\delta\cdots}$$

with the usual symmetrization, antisymmetrization, and contraction rules. These include:

- **Antisymmetric bi-twistors** $X^{\alpha\beta} = -X^{\beta\alpha}$: six-dimensional, corresponding to points or planes in $\mathbb{CP}^3$ (equivalently, to points in complexified compactified Minkowski space via the Klein correspondence).
- **Symmetric bi-twistors**, higher-valence objects, etc.

The algebra of twistors with these operations constitutes the **twistor algebra** of the paper's title.

---

## 5. The Incidence Relation

### 5.1 Statement

The bridge between twistor space and spacetime is the **incidence relation**:

$$\boxed{\omega^A = i\,x^{AA'}\,\pi_{A'}}$$

This is the central equation of twistor theory. Given a spacetime point $x^{AA'}$ and a primed spinor $\pi_{A'}$, the incidence relation determines $\omega^A$ and hence the full twistor $Z^\alpha = (\omega^A, \pi_{A'})$.

### 5.2 Geometric Interpretation

**From spacetime to twistor space:** Fix a point $x \in \mathbb{M}^{\mathbb{C}}$ (complexified Minkowski space). As $\pi_{A'}$ varies over $\mathbb{C}^2 \setminus \{0\}$, the incidence relation sweeps out a two-dimensional linear subspace of $\mathbb{T}$. Projectively, this is a complex projective line $\mathbb{CP}^1 \subset \mathbb{CP}^3$. Thus:

> **A point $x$ in complexified Minkowski space corresponds to a projective line $L_x \cong \mathbb{CP}^1$ in projective twistor space $\mathbb{PT}$.**

**From twistor space to spacetime:** Fix a twistor $Z^\alpha = (\omega^A, \pi_{A'})$ with $\pi_{A'} \neq 0$. The incidence relation $\omega^A = ix^{AA'}\pi_{A'}$ imposes two complex equations on the four complex parameters $x^{AA'}$, determining a two-complex-dimensional surface in $\mathbb{M}^{\mathbb{C}}$. This surface is a **totally null self-dual 2-plane** ($\alpha$-plane). Thus:

> **A point $Z$ in projective twistor space $\mathbb{PT}$ corresponds to an $\alpha$-plane in complexified Minkowski space.**

### 5.3 The Real Slice: Null Geodesics

When we restrict to *real* Minkowski space (requiring $x^{AA'}$ to be Hermitian), the $\alpha$-plane generically intersects the real slice in a **real null geodesic** (a light ray). This is the fundamental geometric correspondence:

> **A null twistor (satisfying $Z^\alpha \bar{Z}_\alpha = 0$) corresponds to a null geodesic in real Minkowski space.**

Two spacetime points $x$ and $y$ are **null-separated** (connected by a light ray) if and only if the corresponding projective lines $L_x$ and $L_y$ in $\mathbb{PT}$ intersect.

### 5.4 The Incidence Relation in Components

Writing out the matrix form with $x^{AA'} = \frac{1}{\sqrt{2}}\begin{pmatrix} t+z & x+iy \\ x-iy & t-z \end{pmatrix}$, the incidence relation becomes:

$$\begin{pmatrix} \omega^0 \\ \omega^1 \end{pmatrix} = \frac{i}{\sqrt{2}} \begin{pmatrix} t+z & x+iy \\ x-iy & t-z \end{pmatrix} \begin{pmatrix} \pi_{0'} \\ \pi_{1'} \end{pmatrix}.$$

Or in terms of the standard homogeneous twistor coordinates $(Z^0, Z^1, Z^2, Z^3)$:

$$\begin{pmatrix} Z^0 \\ Z^1 \end{pmatrix} = \frac{i}{\sqrt{2}} \begin{pmatrix} t+z & x+iy \\ x-iy & t-z \end{pmatrix} \begin{pmatrix} Z^2 \\ Z^3 \end{pmatrix}.$$

---

## 6. Projective Twistor Space and the Klein Correspondence

### 6.1 Projective Twistor Space $\mathbb{PT}$

Since the incidence relation $\omega^A = ix^{AA'}\pi_{A'}$ is preserved under the rescaling $Z^\alpha \mapsto \lambda Z^\alpha$ for $\lambda \in \mathbb{C}^*$, the geometrically meaningful space is the **projective twistor space**:

$$\mathbb{PT} = \mathbb{CP}^3 = (\mathbb{C}^4 \setminus \{0\})\,/\,\mathbb{C}^*.$$

This is a compact, three-complex-dimensional manifold. More precisely, one often removes the locus $\pi_{A'} = 0$ (the "infinity twistors") to work with the non-projective part, giving $\mathbb{PT} \setminus \mathbb{CP}^1 \cong \mathbb{C}^3$.

### 6.2 The Klein Correspondence

The relationship between $\mathbb{PT}$ and complexified compactified Minkowski space $\mathbb{M}^{\mathbb{C}\sharp}$ is a specific instance of the **Klein correspondence** from 19th-century projective geometry. In its classical form, the Klein correspondence establishes a bijection:

$$\{\text{lines in } \mathbb{CP}^3\} \;\longleftrightarrow\; \{\text{points of the Klein quadric } \mathcal{Q} \subset \mathbb{CP}^5\}.$$

In the twistor context:

| Projective twistor space $\mathbb{PT} = \mathbb{CP}^3$ | Complexified Minkowski space $\mathbb{M}^{\mathbb{C}\sharp}$ |
|---|---|
| Point $Z \in \mathbb{CP}^3$ | $\alpha$-plane in $\mathbb{M}^{\mathbb{C}\sharp}$ |
| Line $L \subset \mathbb{CP}^3$ | Point $x \in \mathbb{M}^{\mathbb{C}\sharp}$ |
| Two points $Z, W$ incident on $L$ | Two $\alpha$-planes intersecting at $x$ |
| $L_x \cap L_y \neq \varnothing$ | $x$ and $y$ are null-separated |

More precisely, the complexified compactified Minkowski space is identified with the **Grassmannian** $\text{Gr}_2(\mathbb{C}^4)$ of two-dimensional subspaces of $\mathbb{C}^4$, which is the same as the space of projective lines in $\mathbb{CP}^3$. The Plucker embedding maps $\text{Gr}_2(\mathbb{C}^4)$ into $\mathbb{CP}^5$, and its image is the Klein quadric $\mathcal{Q}$, a smooth four-dimensional quadric hypersurface.

### 6.3 The Double Fibration

The twistor correspondence is concisely encoded in the **double fibration** (or correspondence space) diagram:

$$\begin{array}{ccc}
 & \mathcal{F} & \\
\swarrow & & \searrow \\
\mathbb{PT} = \mathbb{CP}^3 & & \mathbb{M}^{\mathbb{C}\sharp} = \text{Gr}_2(\mathbb{C}^4)
\end{array}$$

where $\mathcal{F} = \text{Fl}_{1,2}(\mathbb{C}^4)$ is the partial flag manifold parametrising pairs (line $\subset$ 2-plane) in $\mathbb{C}^4$. The left projection sends a flag to its line component (a point of $\mathbb{CP}^3$); the right projection sends it to its 2-plane component (a point of $\text{Gr}_2(\mathbb{C}^4)$).

### 6.4 Simple Bi-Twistors and the Plucker Embedding

A point $x \in \mathbb{M}^{\mathbb{C}\sharp}$ is represented by the line $L_x$ in $\mathbb{CP}^3$ spanned by any two twistors $Y^\alpha, Z^\alpha$ incident with $x$. The **simple bi-twistor**

$$X^{\alpha\beta} = Y^\alpha Z^\beta - Z^\alpha Y^\beta$$

is antisymmetric and determined (up to scale) by the line $L_x$. It satisfies the simplicity condition:

$$\varepsilon_{\alpha\beta\gamma\delta}\,X^{\alpha\beta}\,X^{\gamma\delta} = 0.$$

The six independent components of $X^{\alpha\beta}$ serve as the **Plucker coordinates** of $L_x$ in $\mathbb{CP}^5$, and the simplicity condition is the equation of the Klein quadric.

---

## 7. The Infinity Twistor

### 7.1 Conformal vs. Poincare Invariance

Twistor space $\mathbb{T} = \mathbb{C}^4$ carries a natural action of $SL(4, \mathbb{C})$, which is the complexified conformal group. The full conformal structure of compactified Minkowski space is encoded in the projective and linear structure of $\mathbb{PT}$. To break conformal invariance down to Poincare invariance---thus distinguishing finite points from points at infinity and restoring the metric---an additional structure must be imposed on twistor space.

### 7.2 Definition

The **infinity twistor** $I_{\alpha\beta}$ is an antisymmetric twistor of valence $\binom{0}{2}$ defined by:

$$I_{\alpha\beta} = \begin{pmatrix} \varepsilon_{AB} & 0 \\ 0 & 0 \end{pmatrix},$$

where the $4 \times 4$ matrix is written in the block form corresponding to the decomposition $Z^\alpha = (\omega^A, \pi_{A'})$. The upper-left $2 \times 2$ block is the Levi-Civita symbol $\varepsilon_{AB}$; all other entries vanish.

Its **dual** (or inverse, up to normalisation) is:

$$I^{\alpha\beta} = \begin{pmatrix} 0 & 0 \\ 0 & \varepsilon^{A'B'} \end{pmatrix}.$$

### 7.3 Role of the Infinity Twistor

1. **Identifying infinity:** A point $x \in \mathbb{M}^{\mathbb{C}\sharp}$ (represented by a simple bi-twistor $X^{\alpha\beta}$) lies on the null cone at infinity if and only if

$$I_{\alpha\beta}\,X^{\alpha\beta} = 0.$$

This condition picks out the *infinity twistors*---the locus $\pi_{A'} = 0$ within $\mathbb{PT}$.

2. **Recovering the metric:** For two finite points represented by bi-twistors $X^{\alpha\beta}$ and $Y^{\alpha\beta}$, the **spacetime interval** (squared distance) is proportional to

$$I_{\alpha\beta}\,X^{\alpha\gamma}\,I_{\gamma\delta}\,Y^{\delta\beta}$$

(suitably contracted). More precisely, the metric structure on $\mathbb{M}$ is completely encoded in $I_{\alpha\beta}$.

3. **Breaking conformal to Poincare:** The subgroup of $SL(4,\mathbb{C})$ preserving $I_{\alpha\beta}$ (and the Hermitian structure) is precisely the Poincare group (plus dilatations in the conformal case). The infinity twistor therefore encodes exactly the information needed to reduce conformal geometry to metric geometry.

4. **Momentum and energy:** The four-momentum of a massless particle with twistor $Z^\alpha$ is extracted via

$$p_{AA'} = \pi_A\,\bar{\pi}_{A'},$$

and the angular momentum involves both $\omega^A$ and $\pi_{A'}$ through the infinity twistor.

---

## 8. The Twistor Norm and the Three Regions of $\mathbb{PT}$

### 8.1 The Hermitian Form

The pseudo-Hermitian conjugation $Z^\alpha \mapsto \bar{Z}_\alpha = (\bar{\pi}_A, \bar{\omega}^{A'})$ defines a **Hermitian inner product** (really a Hermitian form of signature $(+\,+\,-\,-)$) on $\mathbb{T}$:

$$\Sigma(Z, \bar{Z}) \;=\; Z^\alpha\,\bar{Z}_\alpha \;=\; \omega^A\,\bar{\pi}_A + \bar{\omega}^{A'}\,\pi_{A'}.$$

In components:

$$Z^\alpha\,\bar{Z}_\alpha = Z^0\bar{Z}^2 + Z^1\bar{Z}^3 + Z^2\bar{Z}^0 + Z^3\bar{Z}^1 = \omega^0\bar{\pi}_0 + \omega^1\bar{\pi}_1 + \bar{\omega}^{0'}\pi_{0'} + \bar{\omega}^{1'}\pi_{1'}.$$

This is a real-valued quantity (since $\overline{\omega^A\bar{\pi}_A} = \bar{\omega}^{A'}\pi_{A'}$).

### 8.2 Physical Interpretation: Helicity

The twistor norm has a direct physical meaning. For a null twistor (corresponding to a real null geodesic representing a massless particle), the **helicity** $s$ is:

$$s = \frac{1}{2}\,Z^\alpha\,\bar{Z}_\alpha = \frac{1}{2}\left(\omega^A\bar{\pi}_A + \bar{\omega}^{A'}\pi_{A'}\right).$$

This is the component of angular momentum along the direction of propagation.

### 8.3 The Three Regions

The sign of the Hermitian form partitions projective twistor space into three invariant regions:

| Region | Condition | Physical Meaning |
|---|---|---|
| $\mathbb{PT}^+$ | $Z^\alpha\bar{Z}_\alpha > 0$ | Positive helicity (right-handed massless particles) |
| $\mathbb{PN}$ | $Z^\alpha\bar{Z}_\alpha = 0$ | Zero helicity; null twistors corresponding to real null geodesics |
| $\mathbb{PT}^-$ | $Z^\alpha\bar{Z}_\alpha < 0$ | Negative helicity (left-handed massless particles) |

The null twistor space $\mathbb{PN}$ is a five-real-dimensional hypersurface in $\mathbb{PT}$ (which has six real dimensions), diffeomorphic to $S^2 \times \mathbb{R}^3$. It is precisely the space of real null geodesics (light rays) in Minkowski space.

The boundary $\mathbb{PN}$ separates $\mathbb{PT}^+$ from $\mathbb{PT}^-$. The decomposition $\mathbb{PT} = \mathbb{PT}^+ \cup \mathbb{PN} \cup \mathbb{PT}^-$ is preserved by the real conformal group $SU(2,2)$.

### 8.4 The Group Preserving the Norm

The group of linear transformations of $\mathbb{T} = \mathbb{C}^4$ preserving the Hermitian form $\Sigma$ of signature $(2,2)$ is $U(2,2)$. Restricting to unit determinant gives $SU(2,2)$. Since an overall phase acts trivially on projective space, the effective group on $\mathbb{PT}$ is $SU(2,2)/\mathbb{Z}_4$, which is the (restricted) conformal group $C(1,3)$ of compactified Minkowski space.

---

## 9. The Robinson Congruence

### 9.1 Definition

Given a non-null twistor $Z^\alpha \in \mathbb{PT}^+ \cup \mathbb{PT}^-$, the set of null twistors "associated" to it (i.e., the null twistors $W$ such that $Z^\alpha \bar{W}_\alpha = 0$) forms a three-real-parameter family of null geodesics in Minkowski space. This family is called the **Robinson congruence** associated with $Z$.

### 9.2 Structure

The Robinson congruence has remarkable geometric properties:

1. **Shear-free:** The congruence is geodesic and shear-free (its optical scalars satisfy $\sigma = 0$, $\kappa = 0$). This is a stringent geometric condition---the Goldberg-Sachs theorem relates shear-free congruences to algebraically special spacetimes.

2. **Twist:** The congruence is *twisting* (non-surface-forming). The null geodesics spiral around one another in a pattern that, when projected onto a spacelike slice $t = \text{const}$, appears as a family of linked circles---a **Hopf fibration** of $S^3$.

3. **Hopf structure:** At any instant of time, the projection of the Robinson congruence onto a spatial $\mathbb{R}^3$ slice yields a system of oriented circles. These circles are the fibres of the Hopf map $S^3 \to S^2$. The entire configuration propagates rigidly at the speed of light.

4. **Handedness:** For $Z \in \mathbb{PT}^+$ (positive helicity), the circles twist in a **right-handed** sense. For $Z \in \mathbb{PT}^-$ (negative helicity), they twist **left-handed**. This is the geometric origin of the name "twistor."

### 9.3 Connection to the Kerr Theorem

Penrose describes the **Kerr theorem**: the complex analytic surfaces in $\mathbb{CP}^3$ (twistor space) determine the *shear-free null geodesic congruences* in real Minkowski space. Specifically, given any holomorphic function $F(Z^0, Z^1, Z^2, Z^3)$, homogeneous of appropriate degree, the surface $F = 0$ in $\mathbb{CP}^3$ defines (via the incidence relation) a shear-free null geodesic congruence in $\mathbb{M}$. The Robinson congruence is the simplest case, arising from a *linear* function $F = W_\alpha Z^\alpha$ for fixed dual twistor $W_\alpha$.

---

## 10. Conformal Symmetry: $SU(2,2)$ as Linear Transformations

### 10.1 The Conformal Group

The conformal group of compactified Minkowski space $\mathbb{M}^\sharp$ is the 15-parameter group $C(1,3)$, which includes:

- **Lorentz transformations** (6 parameters)
- **Translations** (4 parameters)
- **Dilatations** (1 parameter)
- **Special conformal transformations** (4 parameters)

Its double cover is $SU(2,2)$, more precisely:

$$C_0(1,3) \cong SU(2,2)\,/\,\mathbb{Z}_4,$$

where $C_0(1,3)$ is the connected component of the identity in the conformal group.

### 10.2 Linear Action on Twistor Space

The decisive advantage of the twistor formulation is that the conformal group acts **linearly** on twistor space. An element $g \in SU(2,2)$ acts as:

$$Z^\alpha \;\longmapsto\; g^\alpha{}_\beta\,Z^\beta,$$

where $g^\alpha{}_\beta$ is a $4 \times 4$ complex matrix satisfying:

$$g^\dagger\,\Sigma\,g = \Sigma, \qquad \det g = 1,$$

with $\Sigma = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix}$ being the matrix of the Hermitian form.

### 10.3 Conformal Generators in Block Form

In the block decomposition $Z^\alpha = (\omega^A, \pi_{A'})$, the generators of $SU(2,2)$ act as $4 \times 4$ matrices partitioned into $2 \times 2$ blocks:

$$g = \begin{pmatrix} A & B \\ C & D \end{pmatrix}, \qquad \begin{pmatrix} \omega^A \\ \pi_{A'} \end{pmatrix} \mapsto \begin{pmatrix} A^A{}_B & B^A{}^{B'} \\ C_{A'B} & D_{A'}{}^{B'} \end{pmatrix} \begin{pmatrix} \omega^B \\ \pi_{B'} \end{pmatrix}.$$

The specific identifications are:

| Conformal transformation | Block structure | Conditions |
|---|---|---|
| **Lorentz** $\Lambda^A{}_B \oplus \bar{\Lambda}^{A'}{}_{B'}$ | $A = \Lambda$, $D = \bar{\Lambda}$, $B = C = 0$ | $\det \Lambda = 1$ |
| **Translation** $x^a \mapsto x^a + t^a$ | $A = D = I$, $B = 0$, $C_{A'B} = it_{A'B}$ | $t_{A'B}$ Hermitian |
| **Dilatation** $x^a \mapsto e^\lambda x^a$ | $A = e^{\lambda/2}I$, $D = e^{-\lambda/2}I$, $B = C = 0$ | $\lambda \in \mathbb{R}$ |
| **Special conformal** | $A = D = I$, $C = 0$, $B^A{}_{B'} = ik^A{}_{B'}$ | $k_{AB'}$ Hermitian |

The crucial point: operations that are *nonlinear* on spacetime (translations, special conformal transformations) become *linear* on twistor space. This is a profound simplification for the representation theory of the conformal group.

### 10.4 Discrete Symmetries

Penrose discusses in detail how space reversal $P$, time reversal $T$, and the combined $PT$ operation act on twistors. Complex conjugation $Z^\alpha \mapsto \bar{Z}_\alpha$ interchanges $\mathbb{PT}^+$ and $\mathbb{PT}^-$ (swapping helicity sign), and its spacetime interpretation involves combined $P$ and $T$ operations.

---

## 11. The Penrose Transform: Massless Fields as Cohomology

### 11.1 Overview

The **Penrose transform** is the analytic realisation of the twistor correspondence for physics. It establishes a bijection between:

- Solutions of the **massless free-field equations** of helicity $h$ on (regions of) Minkowski space, and
- Elements of the **first sheaf cohomology group** $H^1(U, \mathcal{O}(n))$ on (regions of) projective twistor space, where $n = -2h - 2$.

This transforms differential equations into problems of complex analytic geometry.

### 11.2 The Zero-Rest-Mass Field Equations

The massless free-field equations for a field of spin $s$ (helicity $h = \pm s$) in the two-component spinor formalism are:

**Positive helicity** ($h = +s$, $s > 0$): a totally symmetric spinor field $\varphi_{A'B'\cdots D'}$ with $2s$ primed indices satisfying

$$\nabla^{AA'}\,\varphi_{A'B'\cdots D'} = 0.$$

**Negative helicity** ($h = -s$, $s > 0$): a totally symmetric spinor field $\varphi_{AB\cdots D}$ with $2s$ unprimed indices satisfying

$$\nabla^{AA'}\,\varphi_{AB\cdots D} = 0.$$

**Scalar** ($s = 0$): the wave equation

$$\nabla^{AA'}\nabla_{AA'}\,\varphi = \Box\,\varphi = 0.$$

These include:

| Spin $s$ | Field | Equation |
|---|---|---|
| $0$ | Scalar (massless Klein-Gordon) | $\Box\,\varphi = 0$ |
| $\tfrac{1}{2}$ | Neutrino (Weyl) | $\nabla^{AA'}\varphi_A = 0$ |
| $1$ | Photon (Maxwell) | $\nabla^{AA'}\varphi_{AB} = 0$ |
| $\tfrac{3}{2}$ | Rarita-Schwinger | $\nabla^{AA'}\varphi_{ABC} = 0$ |
| $2$ | Graviton (linearized gravity) | $\nabla^{AA'}\varphi_{ABCD} = 0$ |

### 11.3 The Contour Integral Formula

Penrose's original approach (developed further in subsequent papers) uses **contour integrals** over projective lines in twistor space. For a field of helicity $h$, the twistor function $f(Z^\alpha)$ is homogeneous of degree $n = -2h - 2$ in $Z^\alpha$. The spacetime field is recovered via:

$$\varphi(x) = \frac{1}{2\pi i}\oint_\Gamma f\bigl(ix^{AA'}\pi_{A'},\;\pi_{A'}\bigr)\;\pi_{C'}\,d\pi^{C'},$$

where $\Gamma$ is a closed contour in the $\mathbb{CP}^1$ corresponding to the point $x$ (i.e., in the projective line $L_x \subset \mathbb{PT}$).

For the scalar case ($h = 0$, homogeneity $-2$):

$$\varphi(x) = \frac{1}{2\pi i}\oint_\Gamma f\bigl(ix^{AA'}\pi_{A'},\;\pi_{A'}\bigr)\;\pi_{C'}\,d\pi^{C'}.$$

Differentiating under the integral sign and using the incidence relation, one verifies directly that $\Box\,\varphi = 0$.

### 11.4 The Cohomological Interpretation

The rigorous mathematical formulation identifies the twistor function $f$ not as a single function but as a representative of a **Cech cohomology class**. Two twistor functions $f$ and $f'$ give the same spacetime field if and only if they differ by a function holomorphic on the entire contour (i.e., they are cohomologous).

The precise statement of the **Penrose transform** is:

$$\boxed{H^1\bigl(\mathbb{PT}^+,\;\mathcal{O}(n)\bigr) \;\cong\; \left\{\text{holomorphic solutions of the massless field equations of helicity } h = -\tfrac{1}{2}(n+2) \text{ on } \mathbb{CM}^+\right\}}$$

where:
- $\mathcal{O}(n)$ is the sheaf of holomorphic functions homogeneous of degree $n$ on $\mathbb{PT}$,
- $\mathbb{CM}^+$ is the forward tube domain in complexified Minkowski space (the domain corresponding to $\mathbb{PT}^+$ under the twistor correspondence),
- $H^1$ is the first Cech cohomology group.

The specific correspondences are:

| Helicity $h$ | Homogeneity $n = -2h-2$ | Sheaf | Physical field |
|---|---|---|---|
| $+2$ | $-6$ | $\mathcal{O}(-6)$ | Positive-helicity graviton |
| $+1$ | $-4$ | $\mathcal{O}(-4)$ | Positive-helicity photon |
| $+\tfrac{1}{2}$ | $-3$ | $\mathcal{O}(-3)$ | Positive-helicity neutrino |
| $0$ | $-2$ | $\mathcal{O}(-2)$ | Massless scalar |
| $-\tfrac{1}{2}$ | $-1$ | $\mathcal{O}(-1)$ | Negative-helicity neutrino |
| $-1$ | $0$ | $\mathcal{O}(0)$ | Negative-helicity photon |
| $-2$ | $2$ | $\mathcal{O}(2)$ | Negative-helicity graviton |

### 11.5 The Two-Stage Mechanism

The Penrose transform operates through the double fibration (Section 6.3) in two stages:

1. **Pullback:** Pull back the cohomology class from $\mathbb{PT}$ to the correspondence space $\mathcal{F}$ via the left projection. This is an isomorphism for the relevant sheaves.

2. **Pushdown (direct image):** Push down from $\mathcal{F}$ to $\mathbb{M}^{\mathbb{C}}$ via the right projection, using the **Leray spectral sequence**. The resulting direct image is then interpreted as a solution of differential equations---precisely the massless field equations for the given spin.

---

## 12. Connection to the Newman-Penrose Formalism

### 12.1 The NP Formalism

The **Newman-Penrose (NP) formalism** (1962) is a specialisation of the tetrad formalism in which the vector basis is a *null tetrad*: four null vectors $\{l^a, n^a, m^a, \bar{m}^a\}$ satisfying:

$$l^a n_a = 1, \qquad m^a \bar{m}_a = -1,$$

with all other inner products zero. The formalism introduces 12 complex **spin coefficients** ($\kappa, \sigma, \lambda, \nu, \rho, \mu, \tau, \pi, \varepsilon, \gamma, \alpha, \beta$) encoding the covariant derivatives of the null tetrad vectors.

### 12.2 Spinor Translation

The NP null tetrad translates into spinor language via:

$$l^{AA'} = o^A \bar{o}^{A'}, \qquad n^{AA'} = \iota^A \bar{\iota}^{A'}, \qquad m^{AA'} = o^A \bar{\iota}^{A'}, \qquad \bar{m}^{AA'} = \iota^A \bar{o}^{A'},$$

where $(o^A, \iota^A)$ is a normalised spin-frame ($o^A \iota_A = 1$). The NP spin coefficients become specific components of $\nabla_{AA'} o_B$ and $\nabla_{AA'} \iota_B$.

### 12.3 Twistors and the NP Framework

The twistor $Z^\alpha = (\omega^A, \pi_{A'})$ connects to the NP formalism through several channels:

1. **The spin-frame as twistor data:** The spinor $\pi_{A'}$ can be identified with one member of the primed spin-frame, so a null geodesic congruence generated by $l^a = \pi^A\bar{\pi}^{A'}$ is naturally twistorial.

2. **Shear-free congruences:** The NP optical scalar $\sigma$ (shear) vanishes precisely for the congruences arising from twistor geometry (Robinson congruences and their generalisations via the Kerr theorem). The NP equation

$$D\sigma - \delta\kappa = (\rho + \bar{\rho})\sigma - (3\varepsilon - \bar{\varepsilon})\sigma + \Psi_0 = 0$$

constrains shear-free congruences. The Goldberg-Sachs theorem states that in a vacuum spacetime, $\sigma = 0$ if and only if the Weyl tensor is algebraically special ($\Psi_0 = 0$).

3. **Weyl spinor and twistor contour integrals:** The Weyl spinor $\Psi_{ABCD}$ (equivalent to the five NP Weyl scalars $\Psi_0, \ldots, \Psi_4$) for linearised gravity is obtained from a twistor contour integral with homogeneity $-6$.

4. **The twistor equation in NP language:** The conformally invariant **twistor equation**

$$\nabla_{A'(A}\,\omega_{B)} = 0$$

(symmetrised covariant derivative), when expanded in the NP formalism using the spin coefficients, yields a system of coupled first-order PDEs. On flat spacetime, the general solution is $\omega^A(x) = \omega_0^A - ix^{AA'}\pi_{A'}$, recovering the incidence relation. In curved spacetime, solutions exist only under severe restrictions on the curvature (the spacetime must be conformally flat, or the Weyl curvature must be anti-self-dual).

---

## 13. Key Equations: Summary in LaTeX Notation

### 13.1 Twistor Coordinates
$$Z^\alpha = (\omega^A,\;\pi_{A'}), \qquad \alpha = 0,1,2,3, \qquad A = 0,1, \qquad A' = 0',1'$$

### 13.2 Incidence Relation
$$\omega^A = i\,x^{AA'}\,\pi_{A'}$$

### 13.3 Twistor Norm (Hermitian Form)
$$Z^\alpha\,\bar{Z}_\alpha = \omega^A\,\bar{\pi}_A + \bar{\omega}^{A'}\,\pi_{A'}$$

### 13.4 Helicity
$$s = \tfrac{1}{2}\,Z^\alpha\,\bar{Z}_\alpha$$

### 13.5 Complex Conjugation Map
$$Z^\alpha = (\omega^A, \pi_{A'}) \;\longmapsto\; \bar{Z}_\alpha = (\bar{\pi}_A, \bar{\omega}^{A'})$$

### 13.6 Infinity Twistor
$$I_{\alpha\beta} = \begin{pmatrix} \varepsilon_{AB} & 0 \\ 0 & 0 \end{pmatrix}, \qquad I^{\alpha\beta} = \begin{pmatrix} 0 & 0 \\ 0 & \varepsilon^{A'B'} \end{pmatrix}$$

### 13.7 Hermitian Form Matrix
$$\Sigma_{\alpha\bar{\beta}} = \begin{pmatrix} 0 & \delta^{A'}_{B'} \\ \delta^A_B & 0 \end{pmatrix}$$

### 13.8 Conformal Group Preservation
$$g^\dagger\,\Sigma\,g = \Sigma, \qquad g \in SU(2,2), \qquad \det g = 1$$

### 13.9 Plucker Coordinates (Bi-Twistor)
$$X^{\alpha\beta} = Y^\alpha Z^\beta - Z^\alpha Y^\beta, \qquad \varepsilon_{\alpha\beta\gamma\delta}\,X^{\alpha\beta}X^{\gamma\delta} = 0$$

### 13.10 Zero-Rest-Mass Field Equations
$$\nabla^{AA'}\,\varphi_{A'B'\cdots D'} = 0 \qquad (\text{positive helicity, } 2s \text{ primed indices})$$
$$\nabla^{AA'}\,\varphi_{AB\cdots D} = 0 \qquad (\text{negative helicity, } 2s \text{ unprimed indices})$$

### 13.11 Penrose Contour Integral
$$\varphi(x) = \frac{1}{2\pi i}\oint_\Gamma f\bigl(ix^{AA'}\pi_{A'},\;\pi_{A'}\bigr)\;\pi_{C'}\,d\pi^{C'}$$

### 13.12 Penrose Transform (Cohomological Form)
$$H^1\!\left(\mathbb{PT}^+,\;\mathcal{O}(-2h-2)\right) \;\cong\; \ker\!\left(\nabla^{AA'}\text{ on helicity-}h\text{ fields on }\mathbb{CM}^+\right)$$

### 13.13 The Twistor Equation
$$\nabla_{A'(A}\,\omega_{B)} = 0$$

### 13.14 Spinor-Vector Correspondence
$$x^{AA'} = \frac{1}{\sqrt{2}}\begin{pmatrix} x^0 + x^3 & x^1 + ix^2 \\ x^1 - ix^2 & x^0 - x^3 \end{pmatrix}$$

### 13.15 Null Condition
$$g_{ab}\,x^a x^b = 0 \quad\Longleftrightarrow\quad \det(x^{AA'}) = 0 \quad\Longleftrightarrow\quad x^{AA'} = \xi^A\,\bar{\xi}^{A'}$$

---

## 14. Subsequent Developments

The 1967 paper is the seed from which an enormous body of mathematics and physics has grown. Key subsequent developments include:

1. **Penrose (1968, 1969):** Elaboration of the contour integral formulae for massless fields; introduction of the "elementary states" as specific twistor functions.

2. **Penrose (1973), "Twistor theory: An approach to the quantisation of fields and space-time":** Systematic development of twistor quantisation, where $Z^\alpha$ and $\bar{Z}_\alpha$ become non-commuting operators satisfying $[Z^\alpha, \bar{Z}_\beta] = \hbar\,\delta^\alpha_\beta$.

3. **Eastwood, Penrose, Wells (1981), "Cohomology and Massless Fields":** The rigorous proof of the Penrose transform as an isomorphism between sheaf cohomology and massless field solution spaces.

4. **Ward (1977), the Ward Correspondence:** Extension to nonlinear fields---anti-self-dual Yang-Mills fields correspond to holomorphic vector bundles on twistor space.

5. **Penrose (1976), "Non-linear gravitons and curved twistor theory":** The nonlinear graviton construction: anti-self-dual vacuum spacetimes correspond to deformations of twistor space as a complex manifold.

6. **Witten (2003), "Perturbative gauge theory as a string theory in twistor space":** The modern renaissance, connecting twistor geometry to scattering amplitudes and launching the amplitudes revolution (BCFW recursion, Grassmannians, the amplituhedron).

---

## 15. Assessment

Penrose's 1967 paper is a work of extraordinary originality. Its central insight---that the complex projective geometry of $\mathbb{CP}^3$ provides a more natural arena for massless physics than real Minkowski space---has proven remarkably fertile across a sixty-year span. The paper introduces, in a single stroke, the twistor space, the incidence relation, the Robinson congruence, the twistor algebra, the treatment of conformal symmetry as linear symmetry, and the connection to shear-free null congruences via the Kerr theorem.

What makes the paper especially striking is the combination of geometric intuition with algebraic precision. The passage from spacetime points to null rays, from the real to the complex, from nonlinear conformal maps to linear twistor transformations---each of these is a conceptual leap that opened new mathematical territory.

The subsequent development of the Penrose transform, the Ward correspondence, the nonlinear graviton, and ultimately the twistor-string revolution of the 2000s, all trace their origins directly to this founding document.

---

## References

1. R. Penrose, "Twistor Algebra," *J. Math. Phys.* **8**, 345--366 (1967). [AIP Publishing](https://pubs.aip.org/aip/jmp/article-abstract/8/2/345/233824/Twistor-Algebra)
2. R. Penrose, "Twistor theory: An approach to the quantisation of fields and space-time," *Phys. Rep.* **6**, 241--316 (1973). [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0370157373900082)
3. R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 2: *Spinor and Twistor Methods in Space-Time Geometry* (Cambridge University Press, 1986).
4. S. A. Huggett and K. P. Tod, *An Introduction to Twistor Theory*, 2nd ed. (Cambridge University Press, 1994).
5. R. S. Ward and R. O. Wells Jr., *Twistor Geometry and Field Theory* (Cambridge University Press, 1990).
6. M. F. Atiyah, "The Penrose Transform," in *Twistors in Mathematics and Physics* (Cambridge University Press, 1990). [Cambridge Core](https://www.cambridge.org/core/books/abs/twistors-in-mathematics-and-physics/penrose-transform/797A015C7991A87C887DAE0614A195D6)
7. T. Adamo, "Lectures on twistor theory," arXiv:1712.02196 (2017). [arXiv](https://arxiv.org/abs/1712.02196)
8. M. Dunajski, "Twistor theory at fifty: from contour integrals to twistor strings," *Proc. R. Soc. A* **473**, 20170530 (2017). [Royal Society](https://royalsocietypublishing.org/doi/10.1098/rspa.2017.0530), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5666237/)
9. E. T. Newman and R. Penrose, "An Approach to Gravitational Radiation by a Method of Spin Coefficients," *J. Math. Phys.* **3**, 566--578 (1962).
10. E. Witten, "Perturbative gauge theory as a string theory in twistor space," *Commun. Math. Phys.* **252**, 189--258 (2004).
