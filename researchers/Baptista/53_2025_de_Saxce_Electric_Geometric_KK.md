# Electric? Then it is Geometric

**Author(s):** Géry de Saxcé
**Year:** 2025
**Journal:** arXiv:2503.08718 [physics.gen-ph]

---

## Abstract

We revisit the Kaluza-Klein program through the lens of coadjoint orbit classification and particle physics. The central thesis: electric charge is not a fundamental quantity, but an emergent label arising from the geometric structure of the internal manifold when the Lorentz group $SO(1,3)$ is embedded into a larger symmetry group (here, $SO(1,4)$ or $SO(1,5)$ with internal coordinates). By reconstructing Maxwell's equations from a non-Riemannian connection built on the orbit structure, we show that charge quantization follows from topological properties of the coadjoint orbits, without invoking additional gauge structure. This approach competes with the standard KK mechanism (where charge is the coefficient of the five-form flux) and with the Connes-Chamseddine framework (where charge arises from spectral action). We argue that the geometric charge—derived from orbits—is more fundamental because it is prior to any choice of connection or Lagrangian.

---

## Historical Context

The problem of geometric charge dates to Kaluza's 1921 five-dimensional unification: a charged particle moving in five dimensions, when projected to four, acquires an effective electric charge proportional to the component of its velocity in the fifth direction. This worked but was geometrically opaque — there was no intrinsic reason why the fifth coordinate should "mean" electric charge.

Subsequent advances:
- **Classical KK** (Kaluza, Klein, Thiry, 1920s--1950s): Charge is the "winding number" around the compact dimension; charge quantization follows from single-valuedness of the wave function.
- **Modern KK** (Duff, Pope, 1980s--2000s): In higher-dimensional supergravity, charge is the coefficient of the flux through the internal manifold (e.g., electric flux through $S^7$ in 11D).
- **Connes-NCG** (1990s--2020s): Charge appears as a coupling constant in the spectral action; the Weinberg angle and charge itself are both geometric (related to KK and NCG together).

De Saxcé proposes a fourth approach: coadjoint orbit classification of the Lie algebra $\mathfrak{so}(1,4)$ (or $\mathfrak{so}(1,5)$) furnishes a natural assignment of quantum numbers to particles, and these numbers are \emph{by definition} charges in the orbit interpretation.

---

## Key Arguments and Derivations

### Coadjoint Orbits of SO(1,4)

The Lie algebra $\mathfrak{so}(1,4)$ (Lorentz + one internal direction) has dual space $\mathfrak{so}(1,4)^*$ on which the group acts by the coadjoint representation:
$$\text{Ad}_g^* : f \in \mathfrak{so}(1,4)^* \mapsto (\text{Ad}_g^{-1})^* f$$

Coadjoint orbits are the maximal orbits under this action. For $SO(1,4)$, they are classified by the invariants (Casimir operators):
$$C_1 = \text{Tr}(X^2), \quad C_2 = \text{Tr}(X \wedge X)$$

where $X \in \mathfrak{so}(1,4)$.

An orbit is determined by the pair $(C_1, C_2)$. De Saxcé's key observation: particles (irreps of SO(1,4)) that "live on" a given orbit all share the same values of $(C_1, C_2)$, and these values are \emph{precisely} the mass and charge of the particle in the 4D interpretation.

Specifically, if we parametrize orbits by $(m^2, q)$ where $m$ is mass and $q$ is electric charge, then:
$$C_1 \sim m^2, \quad C_2 \sim q \cdot m$$

The ratios and exact formulae depend on conventions, but the crucial fact is that the Casimir values \emph{classify} particles.

### Embedding into Higher Dimensions

To recover 4D from 5D, we decompose $\mathfrak{so}(1,4) = \mathfrak{so}(1,3) \oplus \mathfrak{u}(1)$ (in a suitable basis). The $\mathfrak{so}(1,3)$ part encodes 4D Lorentz symmetry; the $\mathfrak{u}(1)$ part (one additional generator) encodes the internal direction.

A linear functional $f \in \mathfrak{so}(1,4)^*$ can be written:
$$f(X) = f_{\text{Lorentz}}(X_{\text{Lorentz}}) + f_{\text{int}}(X_{\text{int}})$$

where $X_{\text{Lorentz}} \in \mathfrak{so}(1,3)$ and $X_{\text{int}} \in \mathfrak{u}(1)$.

A particle state $|\psi\rangle$ in 5D is a section of a homogeneous bundle over the coadjoint orbit. Upon reduction to 4D (setting the fifth coordinate to zero in the wave function), the term $f_{\text{int}}(X_{\text{int}})$ becomes a label — the charge $q$ in 4D.

### Non-Riemannian Connection and Maxwell Equations

De Saxcé constructs a non-Riemannian connection $\nabla$ on the orbit by postulating that parallel transport preserves the coadjoint action. The connection is not metric-compatible (no Levi-Civita property), but instead satisfies:
$$\nabla_X \text{Ad}_g^* = \text{Ad}_g^* \nabla_X$$

i.e., the covariant derivative respects the orbit structure.

From this connection, one derives the curvature 2-form:
$$\Omega = d\omega + \omega \wedge \omega$$

where $\omega$ is the connection 1-form. The curvature is then related to the electromagnetic field strength by identifying a specific component:
$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu = \text{(curvature component)}$$

The remarkable result: integrating the Bianchi identity $d\Omega = 0$ over the orbit yields:
$$d*F = 0 \quad \text{(Maxwell, vacuum)}$$
$$d*\Omega = J \quad \text{(Maxwell, with source)}$$

where $J$ is the "source" current naturally appearing in the geometry of the orbit. Charge conservation ($\partial \rho/\partial t + \nabla \cdot J = 0$) follows from the topological closure of the orbit.

### Quantization and Charge Spectrum

In quantum mechanics, an irrep of SO(1,4) is labeled by quantum numbers $(j_0, j_1, j_2)$ (angular momenta in different planes). The coadjoint orbit method assigns each irrep to a unique orbit, and hence to a unique charge.

The charge spectrum is determined by the topological classification of orbits:
$$q \in \{0, \pm e, \pm 2e, \pm 3e, \ldots\}$$

where $e$ is a fundamental charge unit. Fractional charges (e.g., $1/3$ for quarks) arise if the orbit is "multiply connected" (e.g., if one uses $\text{Spin}(1,4)$ instead of $SO(1,4)$, or higher covers).

This is \emph{fundamentally different} from the Connes-Chamseddine approach:
- **Connes**: Charge is a coupling constant in the Lagrangian (spectral action), subject to the constraint $\sin^2\theta_W = 3/8$ from KK+NCG.
- **de Saxcé**: Charge is a topological quantum number prior to any Lagrangian; it arises purely from group representation theory.

### Adversarial Elements: Non-Uniqueness of the Embedding

De Saxcé notes (Section 5) that the embedding $SO(1,3) \hookrightarrow SO(1,4)$ is not unique. One can also embed via $SO(1,3) \times SO(2)$, or $SO(1,3) \times SU(2)$, leading to different charge assignments.

This non-uniqueness is presented as a strength: it explains why quarks (with charge $q = \pm e/3$) and leptons (with charge $q = \pm e$) have different charges — they correspond to different embeddings or different orbit branches.

However, this also means the framework \emph{does not uniquely predict} the charge spectrum; additional input is needed to select the embedding.

In contrast, Baptista's framework (using NCG + KK on SU(3)) does make a unique prediction for $\sin^2\theta_W = 3/8$ (from Connes), and charge follows as a derived quantity.

---

## Key Results

1. **Charge as orbit invariant**: Electric charge is the Casimir invariant $C_2$ of the coadjoint orbit in $SO(1,4)$ (up to normalization).

2. **Maxwell equations from geometry**: The non-Riemannian connection on orbits naturally encodes the electromagnetic field; the structure equations yield Maxwell's equations without invoking a separate gauge principle.

3. **Quantization is topological**: Charge quantization ($q \in e\mathbb{Z}$) follows from the topological closure of orbits, not from periodic boundary conditions in an extra dimension.

4. **Fractional charges**: Quarks' fractional charges arise from non-simply-connected orbits (or from spinorial covers of the group).

5. **Non-uniqueness of embedding**: Multiple embeddings of the 4D Lorentz group into higher-dimensional algebras are possible, each giving a different charge spectrum. The physical choice requires additional principle (e.g., anomaly freedom, unification constraints).

---

## Impact and Legacy

De Saxcé's work is part of a broader recent trend in geometric physics to recover electromagnetism from purely topological and algebraic structures, without invoking a separate gauge field "by hand."

Related approaches:
- **Loop quantum gravity**: Charge emerges from quantized holonomies around loops (no continuum gauge field).
- **Ashtekar variables**: Electromagnetic field rewritten as curvature of a connection on gauge space.
- **Higher-category theory**: Charges and fluxes viewed as generalizations of geometric invariants in higher-dimensional categories.

De Saxcé's coadjoint orbit method is more algebraically minimal than these alternatives, relying only on representation theory of Lie groups.

Criticism: The framework has not yet been tested against precision electromagnetism experiments, and the prediction of the fine-structure constant ($\alpha \sim 1/137$) remains open.

---

## Connection to Phonon-Exflation Framework

**Comparative**: Paper 53 offers an adversarial perspective on how charge arises geometrically.

In the phonon-exflation framework (Baptista + Connes):
- **Charge is derived** from the spectral action on the spectral triple $(C(\mathbb{C}), H, D)$ where $\mathbb{C} \cong \text{SU}(3)/SU(2)$ (the "flavor diagonal"); coupling to the Dirac operator fixes all charges.
- **The Weinberg angle is also derived**: $\sin^2\theta_W = 3/8$ from KK normalization on SU(3).
- **Uniqueness**: The SM Lagrangian is fully determined by the geometry and the choice of spectral triple.

De Saxcé's coadjoint orbit approach:
- **Charge is prior to the Lagrangian**, emerging from orbit topology.
- **Non-unique**: Multiple embeddings allow different charge assignments; additional principle needed.
- **Elegant**: No need to compute spectral action or loop integrals; charges read off immediately.

**Thematic connection**: Both frameworks attempt to ground the SM in geometry. The phonon-exflation approach (via Connes) is "bottom-up" (Dirac spectrum → charges). De Saxcé's approach is "top-down" (group structure → charges).

**Hybrid possibility**: One could imagine a framework where the coadjoint orbit classification (de Saxcé) is used to fix the \emph{global} charge quantum (e.g., $e = 1/3 \times$ fundamental unit), while the NCG spectral action (Connes) specifies \emph{which charges appear in the SM} (U(1), SU(2), SU(3)). This has not been explored in the literature.

**Tension on uniqueness**: If both frameworks are correct, they must agree on charge values. The phonon-exflation framework predicts $\sin^2\theta_W = 3/8$, which constrains the fine-structure constant and thence the absolute charge scale. De Saxcé's non-uniqueness (multiple embeddings) would have to be broken by imposing the Baptista/Connes constraint. Conversely, if de Saxcé's framework is more fundamental, it predicts a \emph{family} of possible charge spectra, and the phonon-exflation selection of SU(3) must correspond to the "right" coadjoint orbit family.

