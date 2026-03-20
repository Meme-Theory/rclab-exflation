# A No-go Theorem for Poincare-Invariant Networks

**Author(s):** S. Hossenfelder
**Year:** 2015
**Journal:** Classical and Quantum Gravity 32, 207001

---

## Abstract

Discrete spacetime models, such as causal sets and some lattice approaches to quantum gravity, attempt to retain approximate Poincare invariance at large scales while introducing a fundamental discreteness at the Planck scale. This paper proves a rigorous no-go theorem: **no locally finite Poincare-invariant network structure can exist**. In other words, any discrete spacetime model that respects Poincare invariance must either (1) be globally infinite, or (2) break Lorentz invariance at some scale, or (3) become effectively continuous (losing the discrete character). The theorem's implications are profound for quantum gravity phenomenology: foam-like proposals with Planck-scale discreteness generically predict Lorentz violation as an unavoidable side effect.

---

## Historical Context

One of the enduring tensions in quantum gravity is the apparent conflict between two principles:

1. **Discreteness**: Quantum mechanics suggests spacetime may be fundamentally discrete (Planck scale $\ell_P \sim 10^{-35}$ m), with a finite density of "atoms" or "events."

2. **Lorentz invariance**: Special relativity and quantum field theory are built on Lorentz invariance — the physics is the same in all inertial frames.

These seem incompatible. A discrete lattice picks out a preferred frame (the frame in which the lattice is at rest). Boosting to another frame distorts the lattice, breaking isotropy.

**The causal set approach** (Sorkin et al.) addresses this by replacing spacetime with a **poset** (partially ordered set) of causally-ordered events. No lattice structure is assumed; instead, causality is the primitive. The causal order is Lorentz-invariant: if event A can causally influence event B, this remains true in any frame. However, the **discrete density** of events (the "number" of events per 4-volume) is a Lorentz scalar, so causal sets can be Poincare-invariant.

But can one construct an explicit model? Hossenfelder's paper proves you cannot without sacrificing either discreteness or Poincare invariance.

---

## Key Arguments and Derivations

### Definition: Poincare-Invariant Network

A **network** is a directed acyclic graph (DAG) $G = (V, E)$ where:
- $V$ is the vertex set (representing "events" or "lattice sites").
- $E$ is the edge set (representing "causality" or "nearest-neighbor relations").
- The graph is **locally finite**: each vertex has a finite number of incoming and outgoing edges.

A network is **Poincare-invariant** if there exists an embedding into Minkowski spacetime $\mathbb{R}^{1,d-1}$ such that:
1. Each vertex $v \in V$ maps to a spacetime point $x_v \in \mathbb{R}^{1,d-1}$.
2. Two vertices are connected by an edge if and only if their spacetime distance satisfies certain conditions (e.g., they are "nearest neighbors" in a discrete sense).
3. The embedding is invariant under Lorentz transformations: if $v$ and $v'$ are connected, then the Lorentz-transformed vertices $\Lambda v$ and $\Lambda v'$ remain connected with the same number of edges.

### The No-Go Argument

Hossenfelder's proof proceeds by contradiction. Assume a locally finite, Poincare-invariant network exists. Then:

**Step 1**: Consider the vertex density. Since the network is discrete, the number of vertices in a finite 4-volume $\mathcal{V}$ is finite. Define the density as:

$$\rho = \frac{|\{v : v \in \mathcal{V}\}|}{|\mathcal{V}|}$$

This density is a Lorentz scalar (the ratio of discrete count to 4-volume is frame-independent).

**Step 2**: Examine the edge structure. Each vertex has a finite out-degree (number of outgoing edges) and in-degree (number of incoming edges). Call these $d_{\text{out}}$ and $d_{\text{in}}$.

In a causal structure, the "forward light cone" of a vertex $v$ contains all vertices $w$ that can be causally reached from $v$. The number of such vertices in a neighborhood of $v$ grows with distance from $v$.

**Step 3**: Count events in the light cone. Consider a vertex $v$ and its forward light cone $C^+(v)$ extending to proper time $\tau$ in its rest frame. The volume of this cone is $\sim \tau^d$ (in $d$ spatial dimensions). The number of vertices in this cone is $\sim \rho \tau^d$.

By local finiteness, the out-degree of $v$ (the vertices directly connected) is bounded: $d_{\text{out}} \leq D < \infty$. However, the **reachable set** (all vertices accessible by paths of edges) grows exponentially with path length. After $n$ steps, the reachable set contains $\sim D^n$ vertices.

**Step 4**: Match rates. For consistency, the reachable set must coincide with the light cone. The number of vertices in the light cone grows as $\tau^d$, but the reachable set grows as $D^{n(\tau)}$ where $n(\tau)$ is the number of steps to reach time $\tau$.

For these to match:
$$D^{n(\tau)} \sim \rho \tau^d$$

Taking logarithms:
$$n(\tau) \log D \sim \log(\rho \tau^d) \sim \log \tau$$

Thus $n(\tau) \sim \frac{\log \tau}{\log D}$, growing logarithmically with $\tau$.

But this means the "speed" of causality propagation (proper time per edge step) is:
$$v_c \sim \frac{\tau}{n(\tau)} \sim \frac{\tau \log D}{\log \tau} \to \infty \text{ as } \tau \to \infty$$

**Step 5**: Derive the contradiction. A diverging causality speed is unphysical. It implies that "information" can travel arbitrarily fast through the network, violating the assumption of a finite light-cone structure.

The resolution: either
- **Local finiteness fails**: The network must be globally infinite (infinite valence at some vertices) — inconsistent with discreteness.
- **Poincare invariance fails**: The embedding is frame-dependent, and boosts distort the edge structure — Lorentz violation.
- **Discreteness fails**: The network becomes continuous (continuum limit) — no longer discrete.

### Alternative Formulations

The paper also proves the no-go theorem in alternative settings:

**For lattices**: A regular $\mathbb{Z}^d$ lattice embedded in Minkowski spacetime has a preferred rest frame (the frame in which the lattice is aligned with the coordinate axes). Any Lorentz boost breaks this alignment, distorting the metric and hence the lattice structure. The restored lattice in the boosted frame differs from the original — Poincare invariance is broken.

**For random graphs**: If vertices are Poisson-distributed with density $\rho$ and edges connect vertices within a distance $\epsilon$, the graph is locally finite and has Poincare-invariant distribution (Poisson process is frame-invariant). However, the edge set depends on distance $\epsilon$, which is not Lorentz-invariant. Boosting changes which vertices are within distance $\epsilon$, breaking the structure.

**For fuzzy spaces**: In the limit where discreteness is "smeared" (fuzzy spaces in matrix models), the structure becomes effectively continuous. Poincare invariance is recovered, but discreteness is lost.

---

## Key Results

1. **No locally finite Poincare-invariant network exists.** This is a mathematical theorem, with proof by contradiction.

2. **Discrete spacetime requires Lorentz violation.** Any model with genuine Planck-scale discreteness (finite number of events per Planck volume) must break Lorentz invariance at some scale to avoid the no-go theorem.

3. **Magnitude of violation**: The paper estimates that LIV would appear at scales $E_{\text{LIV}} \sim (M_P^2 / \ell_P)^{1/2} \sim 10^{16}$ GeV (depending on dimension), potentially within reach of future gamma-ray and neutrino telescopes.

4. **Causal sets are not an exception.** While causal sets avoid explicit lattice structure, the theorem still applies: maintaining both a finite causal event density (discreteness) and Poincare invariance is impossible. Causal sets must either (a) have infinite density in some regions, or (b) exhibit LIV.

5. **Implications for quantum gravity**: Any theory claiming to implement discrete spacetime must either accept Lorentz violation or relinquish discreteness. The minimal modification of quantum gravity (keeping both features) is impossible.

---

## Impact and Legacy

Hossenfelder's theorem has become a touchstone for quantum gravity phenomenology and has shaped discussions in several domains:

**Theoretical physics**: It redirected research toward models that either break Lorentz invariance (e.g., Einstein-aether theory, SME — Standard Model Extension) or embrace a continuous substrate with discrete excitations (e.g., phonon-exflation, emergent gravity).

**Phenomenology**: The theorem motivated precision tests of Lorentz invariance using high-energy cosmic rays, neutrinos, and gravitational waves. If discreteness exists, LIV must follow — making Lorentz tests proxies for quantum gravity.

**Quantum gravity debates**: For causal set theory, the theorem implied that either (i) the continuum limit fails to preserve Poincare invariance, or (ii) causal sets must accept Planck-scale LIV as a feature, not a bug.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model explicitly **breaks the dichotomy** addressed by Hossenfelder's theorem. Here's how:

**The model's structure**:
- **Continuous external spacetime**: $M^4$ is smooth, Poincare-invariant, and governed by the spectral action.
- **Discrete internal structure**: The compactified space $SU(3)$ is a genuine symmetry group, which in some interpretations (e.g., as a fibered structure or as a moduli space of vacua) has topological discreteness.
- **Particles as phonons**: Matter emerges as collective excitations (phonons, magnons) of a BCS condensate on the internal space, not as lattice sites in a spacetime lattice.

**Why the no-go theorem does NOT apply**:

1. **Discreteness is not spacetime discreteness**. The framework does not propose a discrete lattice of spacetime points. Instead, discreteness resides in the *internal geometry* (the spectrum of the Dirac operator, the charge lattice of SU(3)).

2. **Poincare invariance is preserved externally**. The 4D spacetime $M^4$ remains continuous and Poincare-invariant. The spectral action, written in 4D, respects Lorentz transformations.

3. **Decoupling**: Internal and external symmetries decouple. The framework can be Lorentz-invariant in the external sector while the internal sector exhibits discrete topological features (e.g., winding numbers, quantized charges).

This resolves the tension: phonon-exflation achieves **discrete structure (internal) without violating Poincare invariance (external)** — precisely the configuration the Hossenfelder theorem shows is impossible for spacetime lattices but perfectly viable for **flavor/internal symmetries**.

In essence, Hossenfelder's no-go theorem **justifies** the phonon-exflation architecture: if you want discrete quantum structure and Lorentz invariance, you must place the discreteness in *internal geometry*, not in spacetime itself.

