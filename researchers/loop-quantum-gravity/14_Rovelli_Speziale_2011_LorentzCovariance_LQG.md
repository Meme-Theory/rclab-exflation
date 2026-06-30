# Lorentz covariance of loop quantum gravity

## Citation

- **Authors**: Carlo Rovelli and Simone Speziale
- **Affiliation**: Centre de Physique Theorique de Luminy, Case 907, F-13288 Marseille, EU (Unite mixte de recherche du CNRS et des Universites de Aix-Marseille I, Aix-Marseille II et Toulon-Var; affilie a la FRUMAM)
- **Year**: 2011 (v3 posted 18 Apr 2011; original 8 Dec 2010)
- **arXiv**: 1012.1739v3 [gr-qc]
- **Companion paper**: W. Wieland, "Complex Ashtekar variables and reality conditions for Holst's action," arXiv:1012.1738 (appearing in parallel; derives the same space $\mathcal{K}$ directly from canonical quantization)

## Abstract (verbatim)

"The kinematics of loop gravity can be given a manifestly Lorentz-covariant formulation: the conventional $SU(2)$-spin-network Hilbert space can be mapped to a space $\mathcal{K}$ of $SL(2, \mathbb{C})$ functions, where Lorentz covariance is manifest. $\mathcal{K}$ can be described in terms of a certain subset of the 'projected' spin networks studied by Livine, Alexandrov and Dupuis. It is formed by $SL(2, \mathbb{C})$ functions completely determined by their restriction on $SU(2)$. These are square-integrable in the $SU(2)$ scalar product, but not in the $SL(2,\mathbb{C})$ one. Thus, $SU(2)$-spin-network states can be represented by Lorentz-covariant $SL(2, \mathbb{C})$ functions, as two-component photons can be described in the Lorentz-covariant Gupta-Bleuler formalism. As shown by Wolfgang Wieland in a related paper, this manifestly Lorentz-covariant formulation can also be directly obtained from canonical quantization. We show that the spinfoam dynamics of loop quantum gravity is locally $SL(2, \mathbb{C})$-invariant in the bulk, and yields states that are precisely in $\mathcal{K}$ on the boundary. This clarifies how the $SL(2, \mathbb{C})$ spinfoam formalism yields an $SU(2)$ theory on the boundary. These structures define a tidy Lorentz-covariant formalism for loop gravity."

## Position in the LQG arc

This is a **technical refinement + conceptual resolution** paper: it resolves the long-standing tension that canonical LQG's state space $\mathcal{H}_{SU(2)}$ is defined in a fixed time-gauge, breaking manifest local Lorentz covariance, while spin-foam dynamics (EPRL/FK vertex, references [1-7]) is built in the $SL(2, \mathbb{C})$-covariant formalism. The paper unifies the two: it shows that the boundary states of the $SL(2, \mathbb{C})$ spinfoam dynamics live in a subspace $\mathcal{K} \subset \{\text{functions on } SL(2, \mathbb{C})\}$ that is **linearly isomorphic to $\mathcal{H}_{SU(2)}$** (the canonical LQG space), via the Dupuis-Livine map [15].

The covariance status is sharper than just "consistent with Lorentz invariance":

- **In the bulk**: spinfoam transition amplitudes are exactly $SL(2, \mathbb{C})$-invariant (Theorem 2).
- **On the boundary**: amplitudes are $SL(2, \mathbb{C})$-**covariant** -- they transform under local Lorentz transformations like the $SL(2, \mathbb{C})$ holonomy under gauge transformations (Theorem 3).

This mirrors the classical situation in general relativity: local Lorentz transformations are a gauge symmetry of the bulk and act covariantly on boundary data.

The framework draws on Alexandrov's "manifestly Lorentz-covariant spin networks" program [12-14], Livine's projected spin networks [9], Alexandrov-Livine covariant LQG [10-12], Dupuis-Livine lifting map [15], and Conrady-Freidel path-integral spin-foam representation [16].

## Central definitions

### Dupuis-Livine map $f: \psi \mapsto \tilde\psi$

For a function $\psi(h)$ on $SU(2)$, the map produces a function $\tilde\psi(g)$ on $SL(2, \mathbb{C})$:

$$\tilde\psi(g) = \int_{SU(2)} dh \; K(g, h) \; \psi(h), \quad g \in SL(2, \mathbb{C}) \quad \text{(Eq. 1)}$$

with kernel

$$K(g, h) = \sum_j d_j^2 \int_{SU(2)} dk \; \chi^{p(j), j}(gk) \; \chi^j(kh) \quad \text{(Eq. 2)}$$

where $j \in \mathbb{N}/2$, $d_j = 2j+1$, $\chi^j(h)$ is the spin-$j$ $SU(2)$ character, $\chi^{p, k}(g)$ is the $SL(2, \mathbb{C})$ character in the principal-series $(p, k)$ representation, and $p(j) \geq 0$ is the **degree** of the map.

### Casimirs of $SL(2, \mathbb{C})$ (footnote 1)

The two Casimirs of the $SL(2, \mathbb{C})$ algebra:

$$C_1 \equiv \tfrac{1}{2} J^{IJ} J_{IJ} = |\vec L|^2 - |\vec K|^2 = p^2 - k^2 \quad \text{(Eq. 3)}$$

$$C_2 \equiv \tfrac{1}{4} \epsilon^{IJKL} J_{IJ} J_{KL} = 2 \vec K \cdot \vec L = 2 p k \quad \text{(Eq. 4)}$$

with generators $L^i = -\tfrac{1}{2} \epsilon^i{}_{jk} J^{jk}$ (rotations) and $K^i = J^{0i}$ (boosts) (Eq. 5).

### Projected functions $\mathcal{K}$

The image of $f$ is the linear subspace $\mathcal{K} \subset \{\text{functions on } SL(2, \mathbb{C})\}$ characterized by

$$\tilde\psi(g) = \int_{SU(2)} dh \; K(g, h) \; \tilde\psi(h) \quad \text{(Eq. 7)}$$

These are "projected functions of degree $p(j)$." Key analyticity property: **they are fully determined by their restriction to $SU(2)$** -- this is the equation $(f\psi)|_{SU(2)} = \psi$ (Eq. 6).

In the Peter-Weyl basis on $SU(2)$:

$$\psi_{jmn} = \int_{SU(2)} dh \; \overline{D^j_{mn}(h)} \; \psi(h) \quad \text{(Eq. 8)}$$

so Eq. (1) becomes

$$\tilde\psi(g) = \sum_{jmn} d_j \; \psi_{jmn} \; D^{p(j), j}_{jm, jn}(g) \quad \text{(Eq. 9)}$$

where $D^{p, k}_{jm, j'n}$ are matrix elements of the $(p, k)$ representation in the $|(p, k); j, m\rangle$ basis diagonalizing $L^2$ and $L_z$ of the canonical $SU(2)$ subgroup.

### Non-square-integrability of $\mathcal{K}$ in $L^2[SL(2, \mathbb{C})]$

The generalized basis vectors $|p, k, j, m, j', m'\rangle$ defined by $\langle g | p, k, j, m, j', m' \rangle = D^{p, k}_{jm, j'm'}(g)$ (Eq. 10) satisfy

$$\langle \tilde p, \tilde k, \tilde j, \tilde m, \tilde{j'}, \tilde{m'} | p, k, j, m, j', m' \rangle = \frac{\delta(p - p')}{(p^2 + k^2)} \delta_{k \tilde k} \delta_{j \tilde j} \delta_{j' \tilde{j'}} \delta_{m \tilde m} \delta_{m' \tilde{m'}} \quad \text{(Eq. 11)}$$

Since $p$ is **continuous**, normalizable states require integration in $p$. But for $|\psi\rangle \in \mathcal{K}$ one must have

$$\psi_{kjmj'm'}(p) = \frac{\delta(p - p(k))}{(p^2 + k^2)} \delta_{jk} \delta_{j'k} \psi_{jmm'} \quad \text{(Eq. 12)}$$

which is **not square-integrable in $p$**. The fixed delta-relation between continuous $p$ and discrete $k$ forces $\mathcal{K}$-states to be **discrete linear combinations of distributions** -- structurally analogous to the Bohr-compactified real line used in loop quantum cosmology (LQC) [20] (footnote 2).

The well-behaved $SU(2)$-induced scalar product on $\mathcal{K}$ is

$$\langle p(j), j, \tilde j, \tilde m, \tilde j, \tilde{m'} | p(j), j, j, m, j, m' \rangle = \frac{\delta_{j \tilde j}}{d_j} \delta_{m \tilde m} \delta_{m' \tilde{m'}} \quad \text{(Eq. 13)}$$

obtained by replacing the diverging Dirac delta in Eq. (11) with a Kronecker delta and adjusting measure factors.

## Fixing the degree -- linear simplicity constraints

### Degree pin

The paper fixes the degree of the Dupuis-Livine map to

$$p(j) = \gamma j \quad \text{(Eq. 14)}$$

where $\gamma > 0$ is a real parameter. With this choice, $\mathcal{K}$ is spanned by $D^{\gamma j, j}_{jm, jn}(g)$.

### Linear simplicity constraints

The space $\mathcal{K}$ implements the **linear simplicity constraints of general relativity** [1, 21, 22]. In the time gauge:

$$\vec K + \gamma \vec L = 0 \quad \text{(Eq. 15)}$$

Gauge-invariant part:

$$2 \gamma C_1 - (\gamma^2 - 1) C_2 = 0 \quad \text{(Eq. 16)}$$

For all $\tilde\psi, \tilde\psi' \in \mathcal{K}$:

- (Eq. 17, strong): $(2\gamma C_1 - (\gamma^2 - 1) C_2) | \tilde\psi \rangle = 0$
- (Eq. 18, weak, $j \to \infty$): $\langle \tilde\psi | \vec K + \gamma \vec L | \tilde\psi' \rangle = 0$, where the scalar product is the $SL(2, \mathbb{C})$ Haar.

The first condition imposes $p = \gamma k$; the second fixes $k = j$ (minimal spin of the canonical $SU(2)$ subgroup). These are precisely the linear simplicity constraints used in the **new spin-foam models** for quantum GR (EPRL [1] and references [21] = Rovelli arXiv:1004.1780; [22] = Ding-Rovelli arXiv:1006.1294).

Footnote 3 notes that one could instead choose $p = \gamma(j + 1)$ to satisfy Eq. (18) for all spins [12, 22], but this would violate cylindrical consistency of the spin-foam amplitude [23, 24].

### Classical Ashtekar-Barbero correspondence

At classical level, the simplicity constraints guarantee the covariant dynamics is encoded in the $SU(2)$ Ashtekar-Barbero connection [25, 26]:

$$A^i = \omega^i + \gamma \omega^{0i}, \quad \omega^i = -\tfrac{1}{2} \epsilon^i{}_{jk} \omega^{jk} \quad \text{(Eq. 19, 20)}$$

For an $SL(2, \mathbb{C})$ algebra element $\omega = \omega^{IK} J_{IK} = -\omega^{0i} K_i + \omega^i L_i$, if Eq. (15) holds then $\omega|_\mathcal{K} = (\omega^i + \gamma \omega^{0i}) L_i \equiv A^i L_i$.

At quantum level, no operator for the connection itself exists; only the holonomy. The discrete correspondence is

$$g|_\mathcal{K} = D^{\gamma j, j}_{jm, jn}(g) = \int_{SU(2)} dh \; K(g, h) \; D^j_{mn}(h) \quad \text{(Eq. 21)}$$

i.e., the $SL(2, \mathbb{C})$ holonomy is fully determined by its restriction to $SU(2)$.

## Spinfoam transition amplitudes

### Definition

Following [8, 29] (Rovelli arXiv:1010.1939 + Geloun-Gurau-Rivasseau EPRL/FK Group Field Theory):

$$Z_\mathcal{C}(h_l) = \int_{SL(2, \mathbb{C})} dg_{ev} \int_{SU(2)} dh_{ef} \sum_{j_f} \prod_f d_{j_f} \chi^{\gamma j_f, j_f}\!\left(\prod_{e \in \partial f} g_{ef}^{\epsilon_{ef}}\right) \prod_{e \in \partial f} \chi^{j_f}(h_{ef}) \quad \text{(Eq. 22)}$$

Here $\mathcal{C}$ is a combinatorial 2-complex with vertices $v$, edges $e$, faces $f$, bounded by a graph $\Gamma = \partial \mathcal{C}$ with nodes $n$ and links $l$. The sign $\epsilon_{ef} = \pm 1$ and

$$g_{ef} = \begin{cases} g_{e s_e} h_{ef} g_{e t_e}^{-1} & \text{for internal edges} \\ h_l \in SU(2) & \text{for boundary edges} \end{cases} \quad \text{(Eq. 23)}$$

(Figure 1 depicts a single-vertex two-complex.) The $SU(2)$ elements $h_l$ only enter inside $SL(2, \mathbb{C})$ characters, so $Z_\mathcal{C}(h_l)$ is the restriction to $SU(2)$ of an $SL(2, \mathbb{C})$ function

$$\tilde Z_\mathcal{C}(g_l) = \text{same as Eqs. (22, 23) with } h_l \to g_l \quad \text{(Eq. 24)}$$

### Theorem 1 (boundary states live in $\mathcal{K}$)

> $\tilde Z_\mathcal{C}(g_l)$ is a projected function with degree $p(j) = \gamma j$ in each of its entries. Equivalently:
> $$(\otimes_l f) Z_\mathcal{C} = \tilde Z_\mathcal{C}. \quad \text{(Eq. 25)}$$

**Mechanism of the proof**: the $h_l$ are sandwiched directly between $h_{ef}$ and $h_{e'f}$ on the face $f$ bounding $l$ (no $g$ integration at boundary nodes); the $h_{ef}, h_{e'f}$ integrations project on the $j = k$ $SU(2)$ subspace of the $SL(2, \mathbb{C})$ representation, trivializing the integrals in the definition of $f$.

**Consequence**: the $SU(2)$-invariant boundary space $\mathcal{H}_\mathrm{LQG}$ embeds naturally into the $SU(2)$-invariant tensor product of spaces $\mathcal{K}$ at each link:

$$\psi_{[\Gamma, j_l, i_n]}(h_l) = \otimes_l D^{j_l}(h_l) \otimes i_n \;\mapsto\; \tilde\psi_{[\Gamma, j_l, i_n]}(g_l) = \otimes_l D^{\gamma j_l, j_l}(g_l) \otimes i_n$$

where $i_n$ are $SU(2)$ intertwiners and magnetic-index contractions are tacit.

## Lorentz covariance theorems

### Frame-vector decoration $x_e$

In classical GR, $SL(2, \mathbb{C})$ is the double cover of the identity component $SO_0(3, 1)$ of the Lorentz group; $SU(2)$ covers $SO(3)_x$, the rotation subgroup fixing a Lorentz frame $x$ on the future hyperboloid $\mathbb{H}^3$. There is no preferred embedding $SU(2) \hookrightarrow SL(2, \mathbb{C})$ in physics; there is an $\mathbb{H}^3$-worth of them. For a reference $x_o = (1, 0, 0, 0)$, each $x$ defines a pure-boost $\Lambda_x$ with $\Lambda_x x_o = x$, and

$$h_x = \Lambda_x h \Lambda_x^{-1} \quad \text{(Eq. 27)}$$

More generally, $h_{x x'} = \Lambda_x h \Lambda_{x'}^{-1}$ (Eq. 28), with $SU(2)_{x x'}$ a subgroup only when $x = x'$.

The Dupuis-Livine map generalizes:

$$\tilde\psi_{x x'}(g) = \int_{SU(2)} dh \; K_{x x'}(g, h) \; \psi(h) \quad \text{(Eq. 30)}$$

with $K_{x x'}(g, h) = \sum_j d_j^2 \int_{SU(2)} dk \; \chi^{\gamma j, j}(g k_{x x'}) \; \chi^j(kh)$ and projection property $(f_{x x'} \psi)|_{SU(2)_{x x'}} = \psi$ (Eq. 31). The image $\mathcal{K}_{x x'}$ contains

$$\tilde\psi_{x x'}(g) = \sum_{jmn} d_j \; \psi_{jmn} \; D^{\gamma j, j}_{jm, jn}(\Lambda_{x'}^{-1} g \Lambda_x) \quad \text{(Eq. 33)}$$

### Frame-decorated amplitude

Pick a unit timelike vector $x_e$ at each edge of the 2-complex. The generalized transition amplitude $\tilde Z_{\mathcal{C}, x_e}(g_l)$ uses

$$g_{ef} = \begin{cases} g_{e s_e} (h_{ef})_{x_e} g_{e t_e}^{-1} & \text{for internal edges} \\ (h_l)_{x_{s(l)} x_{t(l)}} & \text{for boundary edges} \end{cases}$$

### Theorem 2 (bulk Lorentz invariance)

> $\tilde Z_{\mathcal{C}, x_e}(g_l)$ is **independent** from all $x_e$ where $e$ is a bulk edge.

**Proof**: all $\Lambda_x$ group elements can be reabsorbed into the $SL(2, \mathbb{C})$ integrations. The dynamics is Lorentz invariant in the bulk.

Hence $\tilde Z_{\mathcal{C}, x_e}$ depends only on the $x_n$ at boundary nodes; rewrite as $\tilde Z_{\mathcal{C}, x_n}(g_l)$.

### Theorem 3 (boundary Lorentz covariance)

> Under a local Lorentz transformation on the boundary, the transition amplitudes transform as
> $$\tilde Z_{\mathcal{C}, \Lambda_n x_n}(g_l) = \tilde Z_{\mathcal{C}, x_n}(\Lambda_{s_l} g_l \Lambda_{t_l}) \quad \text{(Eq. 34)}$$
> where $s_l$ and $t_l$ are the source and target of link $l$.

This is the correct covariance property of the $SL(2, \mathbb{C})$ holonomy under gauge transformations.

## Methods

- **Group representation theory**: principal-series unitary representations of $SL(2, \mathbb{C})$, labelled by $(p, k)$ with $p \in \mathbb{R}$ and $k \in \mathbb{N}/2$; reduction to $SU(2)$ basis $|(p, k); j, m\rangle$ diagonalizing $L^2, L_z$.
- **Peter-Weyl decomposition**: expansion of $SU(2)$ functions in Wigner matrices $D^j_{mn}(h)$.
- **Character orthogonality**: kernel $K(g, h)$ is constructed from $SU(2) \otimes SL(2, \mathbb{C})$ character products.
- **Generalized bases / distributional states**: Eq. (12) makes $\mathcal{K}$ a space of discrete delta-supported distributions, analogous to Bohr-compactification structures.
- **Spinfoam path integral**: Eq. (22) is the EPRL/FK-type vertex amplitude in the form summarized in Rovelli [8]; the boundary specialization uses the $j = k$ projection induced by Eq. (15)-(18).
- **Direct character computation** for Theorem 1: $h_l$ sandwiched between face $SU(2)$ characters trivialize the Dupuis-Livine kernel.
- **Reabsorption of $\Lambda_x$ into bulk integrations** for Theorem 2 (gauge-fixing argument).

## Gupta-Bleuler analogy

The structural parallel the paper repeatedly invokes: $\mathcal{K}$ is a **Lorentz-covariant function space without positive-definite Lorentz-invariant inner product**, in the same way that the Gupta-Bleuler formalism for QED [18, 19] describes two physical photon polarizations using four covariant photon states with an indefinite Minkowski inner product. The physical content is the $SU(2)$-restricted Hilbert space (analogous to the two physical photon polarizations); the covariant $SL(2, \mathbb{C})$ representation is a formal device to keep Lorentz transformations manifest.

## Bohr-compactification analogy

Footnote 2 and the conclusion note that $\mathcal{K}$ is not a proper subspace of $L^2[SL(2, \mathbb{C})]$ -- its elements are discrete linear combinations of distributions, structurally parallel to the Bohr compactification of the real line used in **loop quantum cosmology** [20] (Ashtekar-Bojowald-Lewandowski 2003). Both structures arise when a continuous classical variable is quantized via almost-periodic / projected functions of a discrete spin label.

## Connection to canonical quantization (Wieland's parallel result)

The companion paper Wieland arXiv:1012.1738 [17] derives $\mathcal{K}$ from canonical quantization of the **Holst action**:

$$S[e, \omega] = \int [(e \wedge e)^* + \tfrac{1}{\gamma}(e \wedge e)] \wedge F[\omega] \quad \text{(Eq. 35)}$$

In the time gauge ($ne = 0$ on the boundary, with $n$ a scalar with values in Minkowski space), the momentum conjugate to $\omega$ is

$$\pi = (e \wedge e)^* + \tfrac{1}{\gamma}(e \wedge e) \quad \text{(Eq. 36)}$$

and its electric/magnetic components in the time gauge are

$$K := n\pi = (e \wedge e)^*, \quad L := -n\pi^* = -\tfrac{1}{\gamma}(e \wedge e)^* \quad \text{(Eq. 37)}$$

The linear simplicity constraint Eq. (15) $\vec K + \gamma \vec L = 0$ follows immediately. Using the natural complex structure on $SL(2, \mathbb{C})$, complex variables $\Pi = K + iL$ and $\bar\Pi = K - iL$ interpret Eq. (15) as a **reality condition**. Quantizing in terms of $SL(2, \mathbb{C})$ cylindrical functions, the scalar product (Eq. 13) implements this reality condition -- recovering $\mathcal{K}$ via the "old idea of implementing the reality conditions as the conditions that determine the scalar product" (Rovelli 1991 [30]).

## Connection to the phonon-exflation project

Substrate-first framing: identify LQG structural features, then state phonon-exflation analogs/non-analogs.

### Parallel 1 -- Continuous classical group reduces to discrete-distribution Hilbert space

**LQG feature**: $\mathcal{K} \subset L^2[SL(2, \mathbb{C})]$ is **not square-integrable in the Haar measure**; the fixed relation $p = \gamma k$ between continuous $p$ and discrete $k$ (Eq. 12) forces states into discrete linear combinations of distributions. The well-defined scalar product (Eq. 13) is the $SU(2)$-induced one. The paper explicitly compares this to LQC's Bohr-compactification structure [20].

**Phonon-exflation analog**: the substrate spectral triple $(A_K, H_K, D_K)$ with $A_K = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ provides a finite-rank discrete eigenvalue spectrum of $D_K$ on a finite Hilbert space at any $L_\mathrm{max}$ truncation, without needing a continuous-to-discrete projection. The Bohr-like structure is one realization of the same general phenomenon (discrete-spectrum Hilbert space from gauge-invariant quantization); the substrate's finite spectral triple is a different realization (discreteness intrinsic, not via compactification of $\mathbb{R}$).

### Parallel 2 -- Single positive real parameter pins the dynamics

**LQG feature**: the degree $p(j) = \gamma j$ (Eq. 14) is pinned by the single real positive parameter $\gamma$ -- the **Barbero-Immirzi parameter**. The classical Ashtekar-Barbero connection $A^i = \omega^i + \gamma \omega^{0i}$ (Eq. 19-20) depends on $\gamma$; quantum simplicity constraints select $p = \gamma k, k = j$ from the principal-series $(p, k)$ labels.

**Phonon-exflation analog**: $\tau_\mathrm{fold} = 0.190$ is the single Jensen-deformation parameter pinning the substrate spectral triple. Both frameworks reduce the algebra-axis labels (LQG: $(p, k)$ on $SL(2, \mathbb{C})$ principal series; phonon-exflation: $(p, q)$ Peter-Weyl labels on Jensen-deformed $SU(3)$) to a one-parameter family selected by a substrate constraint. Note the structural difference: $\gamma$ in LQG is an **input** to the action (Holst term coefficient); $\tau_\mathrm{fold}$ in phonon-exflation is the **transit-dynamics** stabilization point of the deformation.

### Parallel 3 -- Background-independent quantization

**LQG feature**: the paper assumes (and references the LQG uniqueness theorems behind) the background-independent quantization of GR via holonomies of the $SL(2, \mathbb{C})$ connection (or its $SU(2)$ time-gauge reduction). Lorentz covariance is restored as a gauge symmetry of the bulk dynamics (Theorem 2) and a covariance property of boundary data (Theorem 3).

**Phonon-exflation analog**: the spectral action $\mathrm{Tr}\, f(D_K / \Lambda)$ on $(A_K, H_K, D_K)$ is similarly background-independent in the substrate-IS sense -- there is no pre-existing space the substrate is "embedded in"; space is emergent from the $a_2$ Seeley-DeWitt coefficient. Local Lorentz invariance of GR emerges from the $a_2$ moment; the LQG paper's bulk $SL(2, \mathbb{C})$ invariance at the operator algebra layer is structurally complementary.

### Parallel 4 -- Sum over substrate configurations with gauge group

**LQG feature**: transition amplitudes (Eq. 22) integrate over $SL(2, \mathbb{C})$ group elements $g_{ev}$ at each vertex-edge pair (and $SU(2)$ $h_{ef}$ at each edge-face pair), with face characters $\chi^{\gamma j_f, j_f}$ implementing the simplicity-constrained spin labels.

**Phonon-exflation analog**: the spectral action $\mathrm{Tr}\, f(D_K / \Lambda)$ at saddle-point yields integration over Jensen-deformation moduli on the substrate algebra. The LQG vertex amplitude (Eq. 22) is a discrete categorical sum over 2-complex labelings; the phonon-exflation spectral-action saddle is a continuous saddle over $\tau$ -- structural parallel rather than equivalence. Both are "sum over substrate configurations" with a gauge group constraining the labels.

### Non-parallel -- Singularity-resolution mechanisms differ

**LQG/LQC feature**: loop quantum cosmology resolves the Big Bang as a **quasi-equilibrium polymer-Friedmann bounce** -- the gravitational Hamiltonian carries quantum-geometry corrections, the scalar field $\phi$ serves as internal clock, and evolution across the deep Planck regime is deterministic with a critical matter density bounce (Ashtekar-Pawlowski-Singh 2006).

**Phonon-exflation feature**: cosmogenesis is an **impulsive non-equilibrium supersonic transit** through the van Hove fold at $\tau_\mathrm{fold} = 0.190$ at Mach 13.75, producing a GGE relic of 59.8 quasiparticle pairs via Parker pair production with $P_\mathrm{exc} = 1.000$. Not quasi-static, not equilibrium, not Friedmann-like.

The LQG paper itself is not about cosmogenesis (it is about kinematic Lorentz covariance + spinfoam bulk/boundary covariance), so the contrast is structural-program-level, not gate-level.

### Direct relevance to consumer agent (loop-quantum-gravity-theorist)

This paper supplies the **canonical citation** for: (i) how the EPRL/FK $SL(2, \mathbb{C})$ spinfoam vertex amplitude reduces to an $SU(2)$ boundary theory (Theorem 1); (ii) the linear simplicity constraints in operator form (Eqs. 15-18); (iii) the Dupuis-Livine map as a $SU(2) \to SL(2, \mathbb{C})$ lifting (Eqs. 1-9); (iv) bulk Lorentz invariance of spinfoam dynamics (Theorem 2); (v) boundary Lorentz covariance (Theorem 3, Eq. 34); (vi) the Gupta-Bleuler analogy for understanding non-positive-definite Lorentz-covariant function spaces in canonical quantization. Equation numbers and theorem numbers are stable for cross-citation.

## Open questions / limitations the paper itself names

1. **Time-gauge fixing**: the formulation assumes the time gauge $ne = 0$ for canonical quantization (companion paper Wieland [17]). Cianfrani-Montani [31] is cited as related work on LQG without the time gauge -- not pursued here.

2. **Choice $p(j) = \gamma j$ vs $p = \gamma(j+1)$**: footnote 3 notes the alternative degree $p = \gamma(j+1)$ satisfies the weak simplicity constraint Eq. (18) **for all spins**, not only asymptotically. But this choice violates cylindrical consistency of the spin-foam amplitude (Rovelli-Smerlak [23] arXiv:1010.5437, Magliaro-Perini [24] arXiv:1010.5227). The trade-off between strong/all-spin simplicity vs cylindrical consistency is acknowledged but unresolved.

3. **Connection operator does not exist**: at quantum level, the correspondence Eq. (20) $\omega|_\mathcal{K} = A^i L_i$ is lost because "the connection is not a well-defined operator by itself" -- only holonomy is. This is general to LQG; the paper notes it but does not develop alternative pointwise connection operators.

4. **General embeddings $h \to h_{xx'}$**: Eq. (28) introduces frame embeddings with $x \neq x'$, motivated by viewing $h$ as parallel transport between two points. The image $SU(2)_{xx'}$ is a subgroup only when $x = x'$ -- not pursued for general dynamics beyond the boundary-covariance theorems.

5. **Disentangling from Alexandrov's alternative models**: the paper explicitly notes it focuses on "aspects and results of this framework that are of direct value for LQG, disentangling them from Alexandrov's attempts to find alternative models" [12-14]. The relationship to alternative covariant LQG models is not exhaustively mapped.

6. **Theorem 1 proof omitted**: "The computation is straightforward, although somewhat tedious, and we omit the details." Reader is asked to take the explicit insertion of Eq. (22) into Eq. (1) as established.

## Notation summary (for downstream consumers)

| Symbol | Meaning |
|:-------|:--------|
| $\gamma$ | Barbero-Immirzi parameter, positive real |
| $\mathcal{K}$ | space of $SL(2, \mathbb{C})$ projected functions with degree $p(j) = \gamma j$ |
| $f$ | Dupuis-Livine map $\psi \mapsto \tilde\psi$ |
| $K(g, h)$ | kernel of $f$, Eq. (2) |
| $D^{p, k}_{jm, j'n}(g)$ | $(p, k)$ rep matrix element of $SL(2, \mathbb{C})$ |
| $D^j_{mn}(h)$ | Wigner matrices on $SU(2)$ |
| $\chi^{p, k}(g)$, $\chi^j(h)$ | $SL(2, \mathbb{C})$ and $SU(2)$ characters |
| $\vec L, \vec K$ | $SU(2)$ rotation and boost generators of $SL(2, \mathbb{C})$ |
| $C_1, C_2$ | $SL(2, \mathbb{C})$ Casimirs, Eqs. (3, 4) |
| $A^i = \omega^i + \gamma \omega^{0i}$ | Ashtekar-Barbero connection |
| $\mathcal{C}$ | 2-complex; $v$ vertices, $e$ edges, $f$ faces |
| $\Gamma = \partial\mathcal{C}$ | boundary graph; $n$ nodes, $l$ links |
| $g_{ev}$, $h_{ef}$, $h_l$ | $SL(2, \mathbb{C})$ and $SU(2)$ group variables on vertices/edges/links |
| $\mathbb{H}^3$ | future timelike hyperboloid; $x \in \mathbb{H}^3$ labels Lorentz frames |
| $\Lambda_x$ | pure boost $x_o \to x$ |

## Key references (selected for downstream)

- [1] Engle-Pereira-Rovelli 2007 (EPRL vertex), arXiv:0705.2388
- [4] Engle-Livine-Pereira-Rovelli 2008 (LQG vertex with finite Immirzi parameter), arXiv:0711.0146
- [6] Freidel-Krasnov 2008 (FK 4d gravity spin foam), arXiv:0708.1595
- [8] Rovelli 2010 (Simple model for quantum GR from LQG), arXiv:1010.1939
- [9] Livine 2002 (Projected spin networks for Lorentz connection), arXiv:gr-qc/0207084
- [12] Alexandrov 2010 (New vertices and canonical quantization), arXiv:1004.2260
- [15] Dupuis-Livine 2010 (Lifting SU(2) spin networks to projected spin networks), arXiv:1008.4093
- [17] Wieland 2010 (companion: Complex Ashtekar variables and reality conditions for Holst's action), arXiv:1012.1738
- [20] Ashtekar-Bojowald-Lewandowski 2003 (LQC mathematical structure, Bohr compactification), arXiv:gr-qc/0304074
- [25] Ashtekar 1987 (New Hamiltonian formulation of GR), Phys. Rev. D 36, 1587
- [26] Barbero 1996 (Euclidean to Lorentzian GR, real way), arXiv:gr-qc/9605066
- [30] Rovelli 1991 (Ashtekar formulation and loop space nonperturbative QG report), Class. Quant. Grav. 8, 1613

## Provenance

Transcribed from the actual arXiv PDF at `C:\sandbox\Ainulindale Exflation\downloads\loop-quantum-gravity\1012.1739v3.pdf` (217 KB, 6 pages). PDF read via the `pdf` skill (1 chunk: pages 1-6). All equation numbers, theorem statements, abstract text, and reference list are taken verbatim from the source. No content supplemented from training knowledge.
