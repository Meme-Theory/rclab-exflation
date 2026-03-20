# Entanglement Wedge Reconstruction and the Information Problem

**Authors**: Geoffrey Penington
**Year**: 2019
**Journal**: *Journal of High Energy Physics*, **2020**, 002 (arXiv: 1905.08255)

(Also: Almheiri, Engelhardt, Marolf, Maxfield, "The Entropy of Bulk Quantum Fields and the Entanglement Wedge of an Evaporating Black Hole," *JHEP* 2019, arXiv: 1905.08762)

---

## Abstract (Analytical Summary)

Penington derives the Page curve for an evaporating black hole in AdS/CFT using the quantum extremal surface (QES) prescription, demonstrating that semiclassical gravity, when properly applied, preserves unitarity. The key insight is that the entanglement wedge of the radiation -- the bulk region that can be reconstructed from the radiation degrees of freedom -- undergoes a phase transition at the Page time. Before the Page time, the entanglement wedge of the radiation does not include the black hole interior. After the Page time, a quantum extremal surface appears *inside* the black hole, and the entanglement wedge of the radiation suddenly includes an "island" -- a region of the black hole interior. The entanglement entropy of the radiation is then given by the island formula, which naturally reproduces the Page curve. This paper, along with the simultaneous work of Almheiri, Engelhardt, Marolf, and Maxfield (AEMM), is widely regarded as the resolution of the information paradox in the semiclassical regime.

---

## Historical Context

### The State of the Information Paradox in 2019

By 2019, the situation was:

1. **AdS/CFT guarantees unitarity**: The boundary CFT is unitary, so the bulk must be. This is a proof of principle, but it doesn't explain *how* information escapes.

2. **The AMPS firewall argument (2012)**: Three seemingly reasonable postulates -- unitarity, effective field theory outside the horizon, and the equivalence principle at the horizon -- are mutually inconsistent. This "firewall paradox" sharpened the crisis.

3. **Quantum extremal surfaces (Engelhardt--Wall, 2015)**: The Ryu--Takayanagi (RT) formula for holographic entanglement entropy was generalized to include quantum corrections:
$$S_{\text{gen}}(\mathcal{X}) = \frac{A(\mathcal{X})}{4G_N} + S_{\text{bulk}}(\Sigma_\mathcal{X})$$
where $\mathcal{X}$ is a codimension-2 surface, $A(\mathcal{X})$ is its area, and $S_{\text{bulk}}(\Sigma_\mathcal{X})$ is the bulk entanglement entropy of quantum fields in the region bounded by $\mathcal{X}$ and the boundary. The entropy is given by the minimum over all extremal surfaces:
$$S = \min_\mathcal{X} \left\{ \text{ext}_\mathcal{X} \, S_{\text{gen}}(\mathcal{X}) \right\}$$

4. **Entanglement wedge reconstruction**: The entanglement wedge of a boundary region $R$ is the bulk domain of dependence of the region bounded by $R$ and the RT/QES surface. Any bulk operator in the entanglement wedge can be reconstructed from boundary operators in $R$.

### The Missing Piece

The QES formula was established, but no one had applied it systematically to an evaporating black hole to check whether the Page curve emerges. This was Penington's (and AEMM's) contribution.

---

## Key Arguments and Derivations

### The Setup: Evaporating Black Hole in AdS

Consider a black hole formed in AdS by the collapse of matter. The black hole evaporates by emitting Hawking radiation. In the AdS/CFT setup, the radiation is collected in a non-gravitational bath region coupled to the AdS boundary.

The total system has three components:
1. **The black hole interior** (behind the horizon)
2. **The black hole exterior** (between the horizon and the AdS boundary)
3. **The radiation bath** (the non-gravitational reservoir collecting Hawking quanta)

The question: what is the entanglement entropy of the radiation bath as a function of time?

### Two Competing QES Saddle Points

The QES prescription instructs us to find *all* extremal surfaces of $S_{\text{gen}}$ and take the minimum. For the radiation bath $R$, there are two candidate quantum extremal surfaces:

**Saddle 1: The empty surface (no island)**

$$S_{\text{gen}}^{(1)} = S_{\text{bulk}}(R)$$

There is no codimension-2 surface; the entanglement wedge of $R$ is just $R$ itself. The entropy is simply the von Neumann entropy of the quantum fields in $R$. This grows linearly in time as more Hawking quanta are emitted (each entangled with its interior partner):

$$S_{\text{gen}}^{(1)}(t) \approx c \cdot t$$

where $c$ is a constant proportional to the emission rate.

**Saddle 2: The island surface**

A quantum extremal surface $\mathcal{X}$ appears *inside* the black hole, just behind the horizon. The region inside $\mathcal{X}$ is the "island" $I$. The entropy is:

$$S_{\text{gen}}^{(2)} = \frac{A(\mathcal{X})}{4G_N} + S_{\text{bulk}}(I \cup R)$$

The key: $S_{\text{bulk}}(I \cup R)$ is much smaller than $S_{\text{bulk}}(R)$ alone. The reason is that the Hawking pair modes (one in $I$, one in $R$) are purified: their joint entropy is much less than their individual entropies. The island "absorbs" the interior partners, reducing the entropy.

The area term $A(\mathcal{X})/4G_N$ is approximately the Bekenstein--Hawking entropy of the black hole, which decreases over time:

$$S_{\text{gen}}^{(2)}(t) \approx S_{\text{BH}}(t) + (\text{small corrections})$$

### The Phase Transition at the Page Time

The QES prescription takes the minimum of the two saddle points:

$$S_{\text{rad}}(t) = \min\left\{S_{\text{gen}}^{(1)}(t), \, S_{\text{gen}}^{(2)}(t)\right\}$$

- **Early times** ($t < t_P$): $S_{\text{gen}}^{(1)} < S_{\text{gen}}^{(2)}$ (the growing linear term is less than the large but decreasing $S_{\text{BH}}$). The empty surface wins. $S_{\text{rad}} \approx c \cdot t$.

- **Late times** ($t > t_P$): $S_{\text{gen}}^{(2)} < S_{\text{gen}}^{(1)}$ (the Bekenstein--Hawking entropy has decreased below the growing radiation entropy). The island surface wins. $S_{\text{rad}} \approx S_{\text{BH}}(t)$.

The crossover occurs at $t = t_P$ (the Page time), when $S_{\text{gen}}^{(1)} = S_{\text{gen}}^{(2)}$. This reproduces the **Page curve** exactly.

### The Island Formula

The general result is encapsulated in the **island formula** (also called the QES formula for the radiation):

$$S_{\text{rad}} = \min_I \left\{ \text{ext}_{\partial I} \left[ \frac{A(\partial I)}{4G_N} + S_{\text{bulk}}(I \cup R) \right] \right\}$$

where the extremization is over the boundary $\partial I$ of the island $I$ (which can be empty), and the minimization is over all extremal surfaces.

### Entanglement Wedge Reconstruction and the Interior

After the Page time, the entanglement wedge of the radiation $R$ includes the island $I$ inside the black hole. By the entanglement wedge reconstruction theorem (Dong, Harlow, Wall, 2016; Cotler et al., 2019), any bulk operator in the entanglement wedge can be reconstructed from boundary operators in $R$. This means:

**After the Page time, the black hole interior can be reconstructed from the radiation.**

This is the precise sense in which information is "in" the Hawking radiation. Before the Page time, the interior is in the entanglement wedge of the *black hole's* boundary region. After the Page time, it transitions to the radiation's entanglement wedge.

### The Location of the QES

The quantum extremal surface $\mathcal{X}$ is located just inside the event horizon, at a distance of order the scrambling length:

$$r_{\mathcal{X}} - r_H \sim \frac{G_N}{r_H} \sim \ell_P^2 / r_H$$

This is a Planck-scale distance from the horizon (when measured in the appropriate near-horizon coordinates). The QES tracks the shrinking horizon as the black hole evaporates.

### Derivation from the Gravitational Path Integral (Replica Trick)

The island formula can be derived from first principles using the gravitational path integral and the replica trick. To compute the entropy $S_{\text{rad}} = -\text{Tr}(\rho_R \ln \rho_R)$, one uses:

$$S_{\text{rad}} = \lim_{n \to 1} \frac{1}{1-n} \ln \text{Tr}(\rho_R^n)$$

$\text{Tr}(\rho_R^n)$ is computed by the gravitational path integral on $n$ replicas of the spacetime, sewn together along the radiation region $R$. The gravitational path integral includes a sum over topologies of the bulk geometry.

**Before the Page time**: The dominant saddle is the "disconnected" geometry (each replica is independent). This gives $S_{\text{rad}} = S_{\text{bulk}}(R)$.

**After the Page time**: A new saddle appears -- the "replica wormhole" -- where the bulk geometries of different replicas are connected through the black hole interior. This saddle gives the island contribution $A(\partial I)/4G_N + S_{\text{bulk}}(I \cup R)$.

The transition between saddles is the gravitational analogue of a phase transition and precisely implements the Page curve.

---

## Physical Interpretation

### How Information Escapes

The island formula provides a clear (if counterintuitive) picture: after the Page time, the interior of the black hole is encoded in the radiation. A "decoder" with access to all the radiation could, in principle, reconstruct the black hole interior. The information is not carried out bit by bit by individual Hawking quanta; it is encoded non-locally in the correlations among all the radiation quanta.

### The Fate of the Firewall Argument

The AMPS argument assumed that the entanglement structure is fixed: an outgoing Hawking mode is entangled with either its interior partner (smooth horizon) or the early radiation (unitarity), but not both (monogamy). The island formula modifies this picture: after the Page time, the "interior partner" mode is itself in the entanglement wedge of the radiation. The interior mode IS part of the radiation's description. There is no contradiction because the interior mode has been "transferred" to the radiation's entanglement wedge.

This does not completely resolve the firewall debate (there are subtleties about state dependence and computational complexity), but it removes the sharpest version of the paradox.

### What the Island Formula Does NOT Say

1. It does not provide a **real-time mechanism** for information escape. The derivation is Euclidean.
2. It does not identify the **microstates** of the black hole. It is a semiclassical result.
3. It does not resolve the **interior paradox**: if the interior is encoded in the radiation, what does an infalling observer experience?
4. It applies rigorously only in **AdS** (or in certain toy models with non-gravitational baths). Extension to asymptotically flat spacetimes is an active area of research.

---

## Impact and Legacy

### The "Resolution" of the Information Paradox

The Penington/AEMM result is widely (though not universally) regarded as the resolution of the information paradox at the semiclassical level. The key achievement: **the Page curve follows from the gravitational path integral without new physics**. The ingredients are:
- General relativity (the gravitational action)
- Quantum field theory (the bulk entropy)
- The QES prescription (a generalization of Ryu--Takayanagi)

No string theory, no AdS/CFT, no new principles. The resolution was *already implicit in semiclassical gravity* -- it just required the correct identification of the saddle points in the gravitational path integral.

### The Massive Entropy of Black Holes

The island formula explains why the Hawking calculation gives the wrong answer after the Page time: Hawking computed only one saddle point (the "no-island" saddle). The island saddle was missed because it is a non-perturbative effect in $G_N$ -- it is invisible in perturbation theory.

### Generalization to Cosmology

The island formula has been applied to cosmological settings:
- **De Sitter space**: Islands inside the cosmological horizon (Hartman, Shaghoulian, Strominger, 2020)
- **FRW cosmology**: Islands at the Big Bang (Chen, Gorbenko, Maldacena, 2020)
- **Baby universes**: The sum over topologies connects to the baby universe/alpha-parameter framework

### Open Problems

1. **Beyond semiclassical**: The island formula is a semiclassical result. What replaces it in full quantum gravity?
2. **Flat space**: Does the island formula work in asymptotically flat spacetimes (our universe)?
3. **Complexity**: Reconstructing the interior from the radiation requires exponential computational resources. Is there a complexity barrier (Harlow--Hayden)?
4. **Baby universes and ensembles**: The gravitational path integral seems to compute ensemble averages, not individual-theory quantities. What does this mean for a single universe?
5. **Interior observers**: What does an infalling observer experience after the Page time?

---

## Connections to Modern Physics

1. **Ryu--Takayanagi and holographic entanglement**: The island formula is a generalization of the RT formula (2006) to settings with gravitational dynamics in the bulk. The RT formula $S = A_{\min}/4G_N$ is the leading-order (classical gravity) version; the QES formula adds quantum corrections; the island formula extends to non-holographic (radiation bath) regions.

2. **Quantum error correction in gravity**: The entanglement wedge reconstruction theorem implies that the holographic correspondence is a quantum error-correcting code. The island phase transition corresponds to a change in the code structure: after the Page time, the "logical operators" (interior modes) can be decoded from a different "physical subsystem" (the radiation).

3. **JT gravity and matrix models**: The island formula has been verified exactly in Jackiw--Teitelboim (JT) gravity, a 2D dilaton gravity model that is dual to a random matrix ensemble (Saad, Shenker, Stanford, 2019). The replica wormholes in JT gravity reproduce the Page curve precisely, including non-perturbative corrections.

4. **Doubly holographic models**: Karch--Randall braneworld models provide "doubly holographic" setups where the island formula can be derived from the RT formula in a higher-dimensional bulk. This provides an independent confirmation and a clear geometric picture.

5. **For the exflation framework**: The island formula is formulated in terms of generalized entropy, which involves the area of a codimension-2 surface. In a Kaluza--Klein framework, the "area" is computed in the full higher-dimensional geometry: $A = A_{4D} \times \text{Vol}(K)$, where $K$ is the internal space. If the internal space evolves (exflation), the island surface and the Page curve would be modified. The island might extend into the internal dimensions, leading to "internal islands" -- regions of the internal geometry that are reconstructible from the radiation. This would connect the information paradox to the compactification dynamics, providing a novel perspective on both. Furthermore, the entanglement wedge reconstruction theorem, applied to the full higher-dimensional spacetime, could in principle reconstruct the internal geometry from the 4D Hawking radiation, providing a holographic encoding of the compact dimensions in the radiation.
