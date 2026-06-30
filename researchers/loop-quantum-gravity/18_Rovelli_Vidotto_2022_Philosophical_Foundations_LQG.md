# Philosophical Foundations of Loop Quantum Gravity

## Citation

- **Authors**: Carlo Rovelli (Aix-Marseille Univ./Univ. de Toulon/CPT-CNRS; Perimeter Institute; Univ. Western Ontario, Dept. of Philosophy and Rotman Institute) and Francesca Vidotto (Univ. Western Ontario, Dept. of Physics & Astronomy, Dept. of Philosophy, Rotman Institute).
- **Title**: Philosophical Foundations of Loop Quantum Gravity.
- **Year**: 2022 (v2 dated 27 Nov 2022). Preprint of the chapter to appear in the *Handbook of Quantum Gravity*, eds. Cosimo Bambi, Leonardo Modesto and Ilya Shapiro, 2023, Springer.
- **arXiv**: 2211.06718v2 [gr-qc].
- **Length**: 27 pages, 11 sections, 99 references.

## Abstract (paraphrased)

Understanding the quantum aspects of gravity is not only a matter of equations and experiments; gravity is intimately tied to the structure of space and time, so understanding quantum gravity requires a conceptual structure appropriate to making sense of the quantum aspects of space and time. The authors review the conceptual foundation of LQG, addressing: the sense in which space and time are *emergent*, the notion of *locality*, the role of *truncation* that enables physical computations on *finite graphs*, the *problem of time*, and the characterization of *observable quantities* in quantum gravity.

## Section-by-section content

### Section 1 — Introduction

States the guiding questions: What is a quantum spacetime? Are space and time emergent? From what? Does quantum gravity require a Schrodinger-like canonical time variable? How is evolution described in the absence of a fixed background spacetime structure? Which empirically observable quantities are well defined? Frames the discussion as resolving routine confusions for newcomers and grounding the conceptual structure of LQG, citing four foundational references: Rovelli 2004 *Quantum Gravity*, Rovelli & Vidotto 2015 *Covariant LQG*, Thiemann's modern canonical exposition, and Gambini-Pullin *Loops, Knots, Gauge Theory and Quantum Gravity*.

### Section 2 — Two distinct notions of space

The paper sharply distinguishes **relational space** (contiguity relations between physical entities -- "I am in London", "the electron has reached the detector"; non-metric; survives in quantum gravity) from **Newtonian container space** (an entity that exists by itself, independently of dynamical degrees of freedom; can be empty; carries a fixed Euclidean geometry; this is what does NOT survive in quantum gravity).

Three-step emergence chain for the container-space notion:

1. Newtonian space emerges from Minkowski space in the $c \to \infty$ low-relative-velocity limit.
2. Minkowski space emerges from a (pseudo-)Riemannian geometry at scales small compared to the curvature radius (formally identifiable with the tangent space at a point).
3. (Pseudo-)Riemannian geometry emerges from the quantum geometry defined by LQG states and their dynamics in a $\hbar \to 0$ classical limit.

"Emergence" here is the standard physics sense: in some contexts, the system admits a convenient approximate description in terms of an emergent self-standing theory whose own notions can be related to particular configurations of the underpinning theory.

**Spinnetwork states** $|\Gamma, j_\ell, v_n\rangle$ form a basis for the quantum gravitational field, where $\Gamma$ is an abstract (not-embedded) labelled graph, $\ell$ labels links, $n$ labels nodes, $j_\ell$ are spin labels (irreps of $SU(2)$), and $v_n$ are intertwiners. Intertwiners are a basis of $SU(2)$-invariant tensors in $H_n = \otimes_{\ell \in n} V_{j_\ell}$, where the tensor product runs over links $\ell$ adjacent to node $n$ and $V_j$ is the spin-$j$ representation Hilbert space. Nodes describe elementary quantum excitations ("elementary quanta") of the gravitational field; links define contiguity between nodes -- the quanta ARE the relational space, they are not located IN a container space. Matter degrees of freedom are likewise defined as labels on the same graphs.

Polemical line: claims that physics is inconsistent unless formulated in terms of observables "located in space" (citing Maudlin [8]) "has no base." Pre-Newtonian humankind found the world perfectly conceivable in terms of relative localization.

### Section 3 — Emergence of continuous metric space

A continuous (intrinsic) 3d Riemannian geometry $g$ is approximated by a 3d Regge triangulation of flat tetrahedra $\tau_n$ connected by triangles $t_\ell$. The two-skeleton of the dual triangulation defines a graph $\Gamma$. Its geometry is captured by:

$$G_n^{\ell\ell'} = A_\ell A_{\ell'} \, \vec{n}_\ell \cdot \vec{n}_{\ell'} \qquad (1)$$

where $A_\ell$ are areas and $\vec{n}_\ell$ unit normals to faces of $\tau_n$. The corresponding operators act on the spinnetwork Hilbert space $\mathcal{H}_\Gamma$:

$$\hat{G}_n^{\ell\ell'} |\Gamma, j_\ell, v_n\rangle = (\hbar G)^2 |\Gamma, j_\ell, \vec{E}_n^\ell \cdot \vec{E}_n^{\ell'} v_n\rangle \qquad (2)$$

where $\vec{E}_n^\ell$ are $SU(2)$ generators on the $V_{j_\ell}$ tensor component. There exist **intrinsic coherent states** $|\psi_g\rangle \in \mathcal{H}_\Gamma$ satisfying:

$$\langle \psi_g | \hat{G}_n^{\ell\ell'} | \psi_g \rangle = G_n^{\ell\ell'} + O(\hbar) \qquad (3)$$

with variance $\to 0$ as $\hbar \to 0$ (refs Thiemann complexifier states; Livine-Speziale quantum tetrahedron; Bianchi-Dona-Speziale polyhedra in LQG). Extrinsic geometry (4d dihedral angles $\theta_\ell$ between tetrahedra-normals) has a corresponding operator $\hat{\theta}_\ell$ (Bianchi-Magliaro-Perini coherent spin-networks; Freidel-Speziale twisted geometries), and there are minimally-spread **extrinsic coherent states** $|\psi_{g,k}\rangle$ satisfying eq.(3) plus:

$$\langle \psi_{g,k} | \hat{\theta}_\ell | \psi_{g,k} \rangle = \theta_\ell + O(\hbar) \qquad (4)$$

**Three prominent quantum features** of LQG metric structure:

(i) **Granularity** from the discrete spectrum of $\hat{G}_n^{\ell\ell'}$ -- "the most distinct feature and the key result of LQG" (Rovelli-Smolin 1995 [15]; Vidotto atomism-relationalism [16]; possible discreteness of time [17]; experimental detection [18]).

(ii) **Quantum superposition of geometries** with interference and entanglement (Christodoulou-Rovelli [19] on possibility of testing).

(iii) **Short-scale fuzziness** because not all $\hat{G}_n^{\ell\ell'}$ operators commute (Ashtekar-Corichi-Zapata non-commutativity of Riemannian structures [20]) -- they cannot be diagonalized together.

Resolves two philosophy-literature objections (Huggett-Wuthrich [9]): (a) superpositions of different graphs $\Gamma'$, $\Gamma''$ are resolved as states in $\mathcal{H}_\Gamma$ where $\Gamma'$ and $\Gamma''$ are subgraphs; (b) mismatch between graph-adjacency and emergent-geometry adjacency is no worse than GR wormhole pathologies and does not jeopardize intelligibility. Justifies the graph-locality as physical: locality experienced in nature is rooted in what directly affects what, and LQG dynamics IS local on the graph (in both Hamiltonian and covariant formulations).

### Section 4 — Observability in gravitational physics

Coordinate confusion: GR coordinates $x, t$ have no metric meaning (unlike SR/Newtonian $X, T$). Physical distances/times in GR are integrals such as

$$T = \int_\gamma \sqrt{g_{ab} dx^a dx^b} \qquad (5)$$

Einstein equations being diffeomorphism-invariant entails that coordinate-dependent quantities cannot be predicted. **Three equally valid interpretations** of the gauge degrees of freedom of GR:

1. **Diffeomorphism-invariant only**: keep only coordinate-invariant observables (e.g. Earth-Moon laser-bounce return time).
2. **Gauge-fixed**: coordinates are labels of concrete reference objects whose dynamics is determined by the theory (standard cosmology homogeneous approximation).
3. **Relational degrees of freedom**: coordinates label concrete reference objects but disregard their dynamics -- the gauge freedom becomes the freedom in choosing an arbitrarily-moving external physical reference system (cf. "Why Gauge?" [22]).

All three localizations are relative. Examples (gravitational-wave detection, Solar System ranging) are NOT diffeomorphism-invariant local functions, yet they are practically observable and routinely predicted. Lesson: claims that "absence of local observables is a major obstacle" are not borne out by classical GR practice. The third reading especially clarifies the hole argument [23] and the apparent reality of a manifold.

### Section 5 — General relativistic evolution

Newtonian evolution: equations for $A(T), B(T), \dots$ where $T$ is the preferred time. GR evolution: relations $f(T_n, A, B, \dots) = 0$ between *all* variables including clock variables $T_n$; parametrized by an arbitrary 4d label $(x, t)$. No single canonical time variable: launching one clock upward and holding another shows $T_1 \neq T_2$ between same launch/catch events.

**Hamiltonian generalization**: Newtonian dynamics has a Hamiltonian $H$ on phase space $\Gamma$ (symplectic manifold). GR-style dynamics has a constraint $C$ on an *extended* symplectic phase space $\Gamma_{ex}$; the symplectic form induces a presymplectic form on the constraint surface $C = 0$; motions are lines (surfaces in field theory) on the constraint surface whose tangents are null directions of the presymplectic form. Newtonian case is recovered for $\Gamma_{ex} = \Gamma \times \{(T, p_T)\}$ with $C = H + p_T$.

**Partial observables**: variables $T, A, B, \dots$ that include both dependent and independent dynamical variables (Rovelli [31]). They can be measured but cannot individually be predicted; what the theory predicts is *relations* among them.

**Quantum form**: partial observables become self-adjoint operators on an extended Hilbert space $\mathcal{H}_{ex}$; dynamics is a constraint operator $C$; transition amplitudes are

$$W(a, b) = \langle a | P | b \rangle \qquad (6)$$

with $P$ the projector onto $\ker C$ (or via distributional techniques when zero lies in the continuum spectrum). Probabilities are well-defined when summed only over a subset of partial observables at fixed values of complementary ones:

$$\sum_{a_1} |W(a_1, a_0, b)|^2 = 1 \qquad (7)$$

Unitarity in the usual sense requires a symmetry variable $t$; without it, probabilities can still be well-defined (cf. Colosi-Rovelli [34] simple background-independent model; Oeckl general boundary [35]).

### Section 6 — Observability in quantum physics

Properties are eigenvalues of observables; QM assigns properties only in interactions across a **Heisenberg cut** (von Neumann [36]). Copenhagen, relational, and Many-Worlds interpretations differ on what "actualization" means but all require the cut. With preparation values $a$ and measurement values $b$:

$$P(b|a) = |W(b, a)|^2 \qquad (8), \qquad W(b; a) = \langle b | a \rangle \qquad (9)$$

Time-evolution version (Hamiltonian $H$, elapsed $t' - t$):

$$W(b, t'; a, t) = \langle b | e^{-\frac{i}{\hbar}(t'-t) H} | a \rangle \qquad (10)$$

GR-case (time included among partial observables):

$$W(b, t'; a, t) = \langle b, t' | P | a, t \rangle \qquad (11)$$

A **boundary Hilbert space** $H_b = H_{in} \otimes H_{out}$ expresses dynamics as a single bra:

$$W(b, t'; a, t) = \langle W | b, t'; a, t \rangle \qquad (12)$$

### Section 7 — Observability in quantum gravity

Combine GR + QM observability: identify the **Heisenberg cut with the boundary of a 4d spacetime region $\mathcal{R}$** (Conrady-Doplicher-Oeckl-Rovelli-Testa [37]). Take $\mathcal{R}$ compact, bounded by a 3-surface $\Sigma = \Sigma_- \cup \Sigma_+$ (past and future spacelike surfaces joined along a 2-sphere), naturally expressed in the time gauge. LQG transition amplitudes are interpreted as transitions from $\Sigma_-$ to $\Sigma_+$. Quantum states on $\Sigma_\pm$ represent quantum geometries on these surfaces. Two natural application contexts: **early cosmology** and **near black hole singularities**.

Covariant transition amplitude as boundary bra:

$$\langle W | \psi \rangle = \langle \Psi_+ | P | \Psi_- \rangle \qquad (13)$$

Formal Wheeler-Misner functional integral form (boundary 3-metric $g$ on $\Sigma$):

$$\langle W | \Psi_g \rangle = \int_{\partial g_4 = g} D g_4 \, e^{-\frac{i}{\hbar} \int \sqrt{-g_4} R[g_4]} \qquad (14)$$

The spinfoam formalism transforms this (ill-defined) integral into something computable within arbitrary truncations. **Semiclassical recovery**:

$$\langle W | \Psi_g \rangle \sim \sum_n e^{-\frac{i}{\hbar} S_n[g]} \qquad (15)$$

summed over solutions $g_4[g]$ of Einstein equations on $\mathcal{R}$ inducing $g$ on $\Sigma$, with Hamilton function

$$S_n[g] = \int_\mathcal{R} \sqrt{-g_4[g]} R[g_4[g]] \qquad (16)$$

Crucial conceptual point: observables can sit on the Heisenberg cut and be partial observables; they need NOT be fully gauge invariant. The boundary strategy circumvents the infamous problem of constructing explicit Dirac observables on the GR phase space (whose long list of attempts is cited: refs [39-56]: Bergmann-Komar, Page-Wootters, Rovelli quantum reference systems, Perez-Rovelli, Dittrich partial/complete observables, Giddings-Marolf-Hartle, Giesel-Tambornino-Thiemann LTB-Dirac observables, Kaminski-Lewandowski-Pawlowski LQC group-averaging, Donnelly-Giddings observables/dressing/nonlocal algebra, Duch-Kaminski-Lewandowski-Swiezewski geometry observables, Bodendorfer Gaussian-normal coordinates). With deparametrization possible, $W(x, t; x', t') \equiv \langle x | e^{-\frac{i}{\hbar} H (t-t')} | x' \rangle \qquad (18)$; intuitively:

$$W(x, t; x', t') \sim \langle x, t | \delta(C) | x', t' \rangle \sim \int_{(x',t') \to (x,t)} DX \, e^{\frac{i}{\hbar} S[X]} \qquad (19)$$

Applications: **end-of-black-hole-evaporation** transition amplitudes (Bianchi-Christodoulou-D'Ambrosio-Haggard-Rovelli white holes as remnants [60]; Rovelli-Vidotto Planck stars [61]; D'Ambrosio et al. Parts I-II [62, 64]; Christodoulou-D'Ambrosio time scales [63]; Haggard-Rovelli quantum-gravity effects outside horizon spark BH-to-WH tunneling [65]); and the **big bang / big bounce** via covariant formalism (Bianchi-Rovelli-Vidotto towards spinfoam cosmology [66]; Gozzini-Vidotto primordial fluctuations [67]; Vidotto many-nodes/many-links spinfoam [68]). In the cosmological context, the average value of the spins serves as the independent variable -- a *discretized version of the cosmological scale factor*.

### Section 8 — Truncation, finite graphs, finite spinfoams

The bra $\langle W |$ is defined order by order in truncations -- each truncation specifies a 2-complex $\mathcal{C}$ with $\Gamma$ as boundary; the spinfoam amplitude defines $\langle W_\mathcal{C} | \in \mathcal{R}_\Gamma^*$ (refs Engle-Pereira-Rovelli flipped vertex [71]; Freidel-Krasnov new spin foam [72]; Kaminski-Kisielowski-Lewandowski spin-foams for all LQG [73]). The theory is well defined if amplitudes converge under refinement (Frisoni-Gozzini-Vidotto MCMC graph refinement [74] gives partial positive numerical evidence).

**Dispelling a recurring conceptual confusion**: quantum theory is NOT a theory only about elementary components -- it is the theory of the quantum behavior of any physical variable irrespectively of compositeness. Molecule angular momentum is quantized regardless of internal quarks. Likewise LQG describes quantum properties of gravitational degrees of freedom at any relevant scale. A state captures only a subset of degrees of freedom measured.

Lattice QCD analogy: hadron masses are computed on lattices of finite size large enough to include the hadron and fine enough to see quark wavelengths, but no more. QED/electroweak perturbation theory has finite (real + virtual) particle count at each order. Concrete LQG calculations involve spin networks and spinfoams with finite graphs and finite two-complexes; suggestions that finite-graph calculations are unreliable are "conceptually ill-founded."

**Measurement model**: given metric $g$, simplicial decomposition, $A_\ell$ areas of 2-simplices, $\vec{n}_\ell \cdot \vec{n}_{\ell'}$ parallel-transported normal-angles between adjacent 2-simplices; eq.(1) gives a family of geometric observables. These do not commute; a maximal commuting subset is given by areas $A_\ell$ and **3-simplex volumes $V_n$** (up to signs disregarded for simplicity); a volume operator $V_n$ acts on $\mathcal{H}_\Gamma$; $(A_\ell, V_n)$ have discrete spectrum [15]. The basis $|\Gamma, j_\ell, v_n\rangle$ diagonalizes them, with $(j_\ell, v_n)$ interpreted as eigenvalues of the measurement outcomes.

### Section 9 — Physical discreteness

Crucial distinction: **truncation discreteness** (the graph/two-complex; analog of lattice QCD; theoretical tool) vs **physical Planck-scale discreteness** (hard prediction of LQG; analog of discrete Hydrogen energy levels, discrete photons; derived from spectral analysis of geometric operators [15]). Physical discreteness is compatible with local Lorentz invariance (Rovelli-Speziale [75]); it is responsible for **UV-finiteness of LQG and resolution of GR singularities** (Ashtekar singularity resolution in LQC [76]; Rovelli-Vidotto evidence for maximal acceleration and singularity resolution in covariant LQG [77]).

The spinfoam sum vs lattice QCD: lattice QCD requires BOTH refining the lattice (sites $\to \infty$) AND lattice spacing $\to 0$; LQG, because of underlying diffeomorphism invariance, requires only refinement (the magic of "Ditt-invariance" -- Rovelli [79]). "Limit" is in the sense of potential, not actual -- physics is always done at arbitrary but finite truncation (Vidotto "Infinities as a measure of our ignorance" [80]).

**Classical limit requires both continuum and large-spin limits taken TOGETHER**. The earlier LQG "flatness problem" expectation that the classical limit could be taken before the continuum limit was wrong (Han large spin regime [81]; Han Einstein equation in semiclassical continuum limit [82]; Asante-Dittrich-Haggard effective spin foams [83]; Engle-Rovelli "accidental flatness constraint does not mean a wrong classical limit" [84]). Footnote 5: at fixed triangulation, LQG amplitudes approximate Regge theory only if the triangulation is sufficiently fine.

### Section 10 — Three distinct notions of time

Parallels space:

1. **Relational time**: counting of happenings in successions; local; survives in quantum gravity (transition amplitudes between successions of local events).
2. **Newtonian time**: well-defined only under heavy approximations; loses metric structure, global simultaneity, single canonical-clock-variable, etc. as approximations are undone.
3. **Experienced time**: rich phenomenology depending on environment, especially entropy-gradient irreversibility and brain functioning in terms of deliberations.

The "problem of time" is two distinct questions conflated:

- *Question 1*: how to describe dynamical evolution without a canonical time variable. ANSWER: Section 5 machinery (constraint $C$ on extended phase space; partial observables; Page-Wootters [41] is one quantum instance of this same solution).
- *Question 2*: why time "flows". ANSWER: misunderstanding -- experienced flow is due to specific accidental environmental facts: Newtonian-limit regime, coarse-graining, strong-entropy-gradient cosmological state, brain deliberations; epistemic and agential arrows align with entropy gradient. References to Rovelli's broader work: "Is Time's Arrow Perspectival?" [85]; "Memory and entropy" [86]; "Agency in Physics" [87]; "Back to Reichenbach" [88]; *The Order of Time* [89].

Side remark: a consistent thermodynamic/statistical theory of the classical gravitational field is still missing (let alone the quantum one) -- reason for confusion around black-hole entropy; partial attempts in Rovelli relativistic observables/states [90]; Haggard-Rovelli zeroth principle [91]; Chirco-Josset-Rovelli reparametrization-invariant statistical mechanics [92].

**Change vs time** distinction: "change" is the generic temporal-contingency aspect (local, not necessarily oriented, no single time variable); "time" is a particular variable with the Newtonian set of qualities (monotonic, clock-measurable, brain-perceived). Quantum gravity carries the first, not the second.

### Section 11 — Conclusion

LQG is summarized as offering both a mathematical formalism and a coherent conceptual picture: relational notions of space and time, general-covariant dynamics via partial observables, observables sitting on a 3-surface boundary (Heisenberg cut = boundary of 4d region), relational interpretation of QM as natural setting. Footnote 6 names an open technical issue: **infrared "bubble" divergences** (Riello self-energy of Lorentzian EPRL-FK [95]; Frisoni-Gozzini-Vidotto numerical self-energy [96]; Dona-Frisoni-Wilson-Ewing radiative corrections to EPRL propagator [97]; Han 4d spinfoam with cosmological constant: finiteness and semiclassical limit [98]).

## Key definitions introduced or sharply formulated

- **Relational space** / **Newtonian (container) space**: contiguity-based vs entity-based notions; first survives, second emerges only in approximations.
- **Spinnetwork state** $|\Gamma, j_\ell, v_n\rangle$: labelled abstract graph $\Gamma$ with link spins $j_\ell$ and node intertwiners $v_n$ in $H_n = \otimes_{\ell \in n} V_{j_\ell}$.
- **Intrinsic / extrinsic coherent states** $|\psi_g\rangle, |\psi_{g,k}\rangle$ on $\mathcal{H}_\Gamma$: minimally-spread states approximating 3d Riemannian intrinsic geometry $g$ and embedded extrinsic geometry $k$.
- **Partial observable**: quantity that is measurable but cannot be individually predicted (Rovelli [31]); includes both dependent and independent dynamical variables. The theory predicts *relations* among partial observables.
- **Extended phase space** $\Gamma_{ex}$, **constraint** $C$: replace Hamiltonian-on-phase-space with constraint-on-extended-phase-space; motions are null directions of the induced presymplectic form on $C = 0$.
- **Heisenberg cut**: the boundary across which a quantum system interacts with its (classically-treated) context (von Neumann); generalized in LQG to the 3-surface $\Sigma$ bounding a compact 4-region $\mathcal{R}$.
- **Boundary Hilbert space** $H_b = H_{in} \otimes H_{out}$; dynamics encoded by a single bra $\langle W |$.
- **Truncation**: a finite 2-complex $\mathcal{C}$ with boundary $\Gamma$; spinfoam amplitudes $\langle W_\mathcal{C} |$ define the truncated theory.
- **Hamilton function** $S_n[g] = \int_\mathcal{R} \sqrt{-g_4[g]} R[g_4[g]]$: value of the EH action on a solution with given boundary data.
- **Ditt-invariance**: diffeomorphism-invariance feature of LQG/spinfoam discretizations meaning that only the refinement limit (not the spacing-to-zero limit) is needed for the continuum.
- **Three notions of time**: relational / Newtonian / experienced.
- **Change** vs **time**: change is generic temporal contingency; time is a specific privileged variable used only in approximations.
- **Three readings of GR gauge**: (1) unphysical redundancy, (2) gauge-fixed, (3) relational coupling to an external reference system.

## Connection to LQG's broader program

Landmark *review / philosophical-foundations chapter* in the *Handbook of Quantum Gravity* (Springer 2023). Not a new computation; rather a senior-authored synthesis of the conceptual structure underpinning the entire LQG/spinfoam program. Cites and frames:

- Foundational textbooks: Rovelli 2004; Rovelli-Vidotto 2015; Thiemann modern canonical; Gambini-Pullin.
- Core technical results: Rovelli-Smolin discrete area/volume spectra (1995, ref [15]); Ashtekar-Corichi-Zapata non-commutativity of Riemannian structures [20]; LQG coherent states (Thiemann complexifier [10]; Livine-Speziale quantum tetrahedron [11]; Bianchi-Dona-Speziale polyhedra [12]; Bianchi-Magliaro-Perini coherent spin-networks [13]; Freidel-Speziale twisted geometries [14]).
- Spinfoam vertex amplitudes: Engle-Pereira-Rovelli flipped vertex [71]; Freidel-Krasnov [72]; Kaminski-Kisielowski-Lewandowski [73].
- Singularity-resolution applications: Planck-star BH evaporation [60-64]; BH-to-WH tunneling outside the horizon [65]; LQC [76]; covariant LQG maximal acceleration and singularity resolution [77].
- Cosmology applications: spinfoam cosmology [66]; primordial fluctuations [67]; many-nodes/many-links spinfoam homogeneous-isotropic case [68].
- Open technical issues: spinfoam "bubble" infrared divergences [95-98]; cosmological-constant finite spinfoams [98].

The chapter belongs to the conceptual / interpretive arc of the program: it does not advance technical machinery but sharpens the philosophical claims (emergence, locality, observability, time) that LQG can defensibly make in 2022.

## Connection to the phonon-exflation project

Both LQG and phonon-exflation are background-independent quantum gravity programs that produce gauge-invariant discrete spectra on a finite kinematical Hilbert space, share a single-parameter substrate, and rely on a sum over substrate configurations. Several structural parallels and non-analogs surface from this paper:

### (1) Discreteness origin (parallel)

- **LQG structural feature**: discrete spectra of geometric operators $\hat{G}_n^{\ell\ell'}$, $\hat{A}_\ell$, $\hat{V}_n$ on spinnetwork Hilbert space (eq.(2); Rovelli-Smolin 1995 [15]). Section 9 emphasizes this is "the most characteristic feature of LQG", responsible for UV-finiteness and singularity resolution, and is compatible with local Lorentz invariance [75].
- **Phonon-exflation analog**: discrete spectrum of the Dirac operator $D_K$ on the finite spectral triple $(A_K, H_K, D_K)$ with $A_K = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$. The 155,984 eigenvalues at $L_{\max} = 10$ are the substrate's "vibrational modes" and play the structural role LQG assigns to area/volume eigenvalues. In both programs the laboratory observable (Riemannian metric / phononic excitation) emerges from a discrete substrate spectrum.

### (2) Single-parameter substrate (parallel)

- **LQG**: although the Immirzi parameter does not appear explicitly in this philosophical-foundations chapter, the broader program carries it as the single dimensionless parameter setting the area-spectrum scale.
- **Phonon-exflation**: Jensen deformation parameter $\tau$ drives the spectral action gradient ($\tau_{\text{fold}} = 0.190$). One-parameter substrate description parallels the LQG single-parameter discretization.

### (3) Background independence (parallel)

- **LQG**: Section 2 explicitly: "the quanta represented by the nodes of the graph are spatially located with respect to one another. Notice that they are not located -- in any sense -- into an external container space." Section 9 footnote 5 underscores that only the refinement limit (Ditt-invariance) is needed because of underlying diffeomorphism invariance.
- **Phonon-exflation**: substrate IS the spectral triple; emergent space is the F-image of the algebra-INVARIANT family. Both programs share the "IS-not-IN" framing: substrate is logically prior to emergent space.

### (4) Sum-over-substrate-configurations (parallel)

- **LQG**: covariant dynamics is the Wheeler-Misner functional integral (eq.(14)) regulated by spinfoam vertex amplitudes; semiclassical recovery via saddle-point sum over solutions of Einstein equations (eq.(15)) weighted by the Hamilton function $S_n[g]$ (eq.(16)).
- **Phonon-exflation**: spectral action $\text{Tr} f(D_K / \Lambda)$ at saddle-points generates the Einstein-Hilbert action via the $a_2$ Seeley-DeWitt coefficient and the Yang-Mills action via $a_4$. The structural parallel is "emergent classical action = saddle-point sum over substrate configurations." (Direction in phonon-exflation: substrate is prior; LQG's $S_n[g]$ is the Hamilton-function image at large-spin/continuum joint limit.)

### (5) Singularity resolution mechanisms (NON-analog, structurally informative)

- **LQG structural feature**: as section 7 emphasizes, the typical LQG cosmological dispatch takes $\Sigma$ as either (a) a single 3-sphere after the big bang (Hartle-Hawking-like transition from nothing) or (b) two disconnected 3-spheres (LQC-style Big Bounce, ref [68]). The mechanism is a **quasi-equilibrium polymer-Friedmann bounce**: the cosmological scale factor evolves as a discretized variable parametrized by the average of the spin labels. The Hamiltonian/holonomy regularization regularizes the singularity into a finite-density bounce.
- **Phonon-exflation structural feature**: cosmogenesis is a **supersonic transit (Mach 13.75) through the van Hove fold** at $\tau_{\text{fold}} = 0.190$ -- impulsive, non-equilibrium, with $dS/d\tau = +58{,}673$. GGE relic formation produces ~59.8 quasiparticle pairs from Parker pair production with $P_{\text{exc}} = 1.000$. The pre-/post-transit regions are causally disconnected (acoustic white hole, $\Gamma_{\text{eff}} = 0.99970$).
- **Non-analog content**: LQC bounces are quasi-equilibrium polymer effects; phonon-exflation transit is impulsive and supersonic. Both resolve the classical singularity, but the *kinematic regime* differs (quasi-equilibrium vs supersonic transit). The shared structural feature is "no singularity"; the differing feature is *how* the singularity is replaced. Useful for cross-program comparison: a future workshop could ask whether LQC's bounce time-scale (set by the Immirzi parameter and the matter content) parallels the substrate $\tau_{\text{fold}}$ time-scale.

### (6) Partial observables vs gauge-invariant Dirac observables (methodological parallel)

Section 7 articulates a position that is structurally close to phonon-exflation's anchor citations: predictions are extractable WITHOUT writing fully gauge-invariant Dirac observables explicitly. The boundary-strategy approach (Heisenberg cut on a 4d region boundary; partial observables on $\Sigma$) circumvents the long-standing Dirac-observable construction problem. In phonon-exflation language, this corresponds to taking the substrate's algebra-INVARIANT family as primary and reading the laboratory-IN observable as the boundary image via an HKR / Connes-Karoubi bridge map -- not as a Dirac-observable evaluation on a phase space.

### (7) Truncation discipline (methodological parallel)

Section 8 firmly defends finite-graph calculations as analogous to lattice QCD (finite size + finite resolution): "Suggestions that calculations on finite graphs and finite spinfoams are unreliable are therefore conceptually ill-founded." Phonon-exflation operates by the same truncation discipline ($L_{\max} = 10$ canonical, $L_{\max} = 12$ master cache, with structural-saturation theorems like Friedrich-Bar bounding the truncation envelope). Both programs take the operative theory to live "at arbitrary but finite truncation."

### (8) Relational interpretation (methodological parallel)

Section 7 closes by noting that the relational interpretation of quantum mechanics merges naturally with quantum gravity's relational structure: "the Heisenberg cut is identified with spacetime partitions." This aligns with phonon-exflation's substrate framing where observables are intrinsic to algebra-axis cells (algebra-INVARIANT vs algebra-DEPENDENT) and laboratory observables are boundary images.

## Open questions / limitations the paper names

- **Infrared "bubble" divergences** in spinfoam amplitudes (footnote 6, refs [95-98]). Self-energy of the Lorentzian EPRL-FK model and radiative corrections to the Lorentzian EPRL propagator are open numerical/analytic problems; Han's 4d spinfoam with cosmological constant offers a finiteness route but is not yet fully integrated.
- **Refinement convergence** of $\langle W_\mathcal{C} |$ under refinement of the 2-complex is only partially supported numerically (Frisoni-Gozzini-Vidotto MCMC graph refinement [74]); the theory is "well defined if refining the 2-complex the amplitude converges."
- **No direct empirical support** for LQG predictions (acknowledged in Section 11 opening). Christodoulou-Rovelli proposals for experimental detection of discreteness of time [18] and laboratory evidence for quantum superposition of geometries [19] remain *possibilities*, not measurements.
- **Classical limit requires joint continuum + large-spin limits** (Section 9). The earlier "flatness problem" expectation that limits could be taken sequentially was wrong; the correct prescription is the joint limit (refs [81-84]). At fixed triangulation, LQG amplitudes only approximate Regge theory if the triangulation is sufficiently fine (footnote 5).
- **No consistent thermodynamic / statistical theory of the classical (let alone quantum) gravitational field** (Section 10). Source of confusion around black-hole entropy. Partial attempts cited [90-92] are "hints and clumsy attempts."
- **Dirac-observable construction problem** (Section 7) remains "infamously hard" -- the boundary strategy circumvents but does not solve it.
- **Two-notions-of-adjacency mismatch** (Section 3) -- the notion defined by the graph need not match the macroscopic averaged-geometry notion. Wild geometries / wild states exist in both classical GR and LQG; their physical relevance "if any" is unknown.

## Provenance

- Source PDF: `C:\sandbox\Ainulindale Exflation\downloads\loop-quantum-gravity\2211.06718v2.pdf` (413 KB, 27 pages).
- Read in three 10-page chunks via the `pdf` skill (chunker `tools/archive/pdf-extract-pages.py`).
- Chunks deleted after transcription.
- All content extracted directly from the paper text; no supplementation from training knowledge.
