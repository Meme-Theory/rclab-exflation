# Information Loss in Black Holes

**Authors**: Stephen W. Hawking
**Year**: 2005
**Journal**: *Physical Review D*, **72**, 084013

---

## Abstract (Analytical Summary)

Hawking reverses his 30-year position and argues that information is NOT lost in black hole evaporation. The argument is based on the Euclidean path integral approach to quantum gravity, applied to asymptotically anti-de Sitter (AdS) spacetimes. Hawking proposes that the path integral should be taken over all topologies -- including those without a black hole -- and that the trivial (no-black-hole) topology dominates at late times, ensuring that the S-matrix is unitary. The information about the initial state is encoded in correlations in the Hawking radiation. This paper represents Hawking's concession of his famous bet with John Preskill (made in 1997), which he paid by giving Preskill a baseball encyclopedia (symbolizing information recovery). The paper was presented at the GR17 conference in Dublin in July 2004.

---

## Historical Context

### Thirty Years of Information Loss

From 1976 to 2004, Hawking maintained that information is irreversibly lost in black hole evaporation. This was a minority position among string theorists (who believed in unitarity, largely because of AdS/CFT) but was supported by some general relativists (notably Unruh and Wald).

### The AdS/CFT Revolution

Maldacena's 1997 discovery of the AdS/CFT correspondence provided the strongest argument for unitarity. In AdS/CFT, a quantum gravity theory in anti-de Sitter space is exactly dual to a conformal field theory on the boundary. The boundary CFT is manifestly unitary -- it is an ordinary quantum field theory. Therefore, any process in the bulk (including black hole formation and evaporation) must also be unitary.

This argument convinced most string theorists but left open the question: *how* does unitarity work in the bulk? What is wrong with Hawking's 1976 argument? This question was not fully answered until the island formula (2019).

### The Dublin Conference

Hawking announced his change of mind at the 17th International Conference on General Relativity and Gravitation (GR17) in Dublin, July 2004. The talk was a major media event. He conceded his bet with Preskill (but not Thorne, who did not concede). The paper was published in 2005.

---

## Key Arguments and Derivations

### The Path Integral Over Topologies

Hawking's argument uses the Euclidean path integral for gravity in asymptotically AdS space. The partition function is:

$$Z = \int \mathcal{D}[g] \, e^{-I_E[g]}$$

In the saddle-point approximation, this sum is dominated by classical solutions (Euclidean metrics that satisfy the Einstein equations). For asymptotically AdS boundary conditions, there are (at least) two classical saddle points:

1. **Thermal AdS**: Euclidean AdS with periodic time (no black hole). The Euclidean metric is smooth and has no horizon.

2. **Euclidean AdS black hole**: The analytic continuation of the Schwarzschild-AdS black hole. This has a different topology (it has a "bolt" at the horizon).

### The Hawking--Page Transition

Hawking and Page (1983) showed that for boundary conditions corresponding to temperature $T$:

- For $T < T_c$ (the Hawking--Page temperature), thermal AdS has lower action and dominates the path integral. No black hole.
- For $T > T_c$, the black hole has lower action and dominates. A large black hole is the dominant saddle.

The partition function receives contributions from both topologies:

$$Z = Z_{\text{thermal AdS}} + Z_{\text{BH}} + \ldots$$

At late times (or in the Lorentzian interpretation, after the black hole evaporates), the thermal AdS topology dominates.

### The Unitarity Argument

Hawking's argument for unitarity proceeds as follows:

**Step 1**: The path integral for the S-matrix in asymptotically AdS space receives contributions from different topologies. The topology with a black hole contributes at intermediate times, but at asymptotically late times, the trivial (no-black-hole) topology dominates.

**Step 2**: On the trivial topology, there is no event horizon, no singularity, and no place for information to be lost. The S-matrix on this topology is unitary.

**Step 3**: The full S-matrix, summed over topologies, is therefore unitary. Information about the initial state is not lost -- it is encoded in the correlations of the outgoing radiation.

**Step 4**: The apparent information loss in Hawking's original calculation arises from considering only the black hole topology. When the sum over topologies is performed, the non-trivial topology (with the black hole) gives exponentially suppressed corrections to the unitary evolution on the trivial topology.

### The Formal Structure

In more detail, Hawking considers the two-point correlation function of the boundary theory:

$$\langle \mathcal{O}(t_1) \mathcal{O}(t_2) \rangle = \frac{1}{Z} \int \mathcal{D}[g] \, \mathcal{D}[\phi] \, \phi(t_1) \, \phi(t_2) \, e^{-I_E[g, \phi]}$$

On the trivial topology, this correlator decays as a power law at large separations (consistent with unitary CFT). On the black hole topology, it decays exponentially (the quasinormal mode decay, corresponding to information falling into the black hole). The full correlator is the sum:

$$\langle \mathcal{O}(t_1) \mathcal{O}(t_2) \rangle = A(|t_1 - t_2|) + B \, e^{-\Gamma |t_1 - t_2|} + \ldots$$

where $A$ is the power-law contribution from thermal AdS and $B e^{-\Gamma t}$ is the exponentially decaying contribution from the black hole. At late times, the power-law term dominates, and the correlator has the structure expected from unitary evolution.

### The Mechanism of Information Return

Hawking's proposal is that information escapes the black hole through the path integral over topologies. This is NOT a mechanism where information is carried out by the Hawking radiation in a localized sense (e.g., by subtle correlations between early and late radiation). Rather, it is a fundamentally non-perturbative quantum gravitational effect: the path integral "knows" about both topologies, and the interference between them restores unitarity.

This is philosophically similar to quantum tunneling: a particle behind a potential barrier classically never escapes, but the path integral includes paths that go over or around the barrier (or through it in Euclidean time), and the total amplitude includes all paths.

---

## Physical Interpretation

### What Changed Hawking's Mind

Hawking was primarily convinced by AdS/CFT. The argument is:

1. The boundary CFT is a well-defined quantum theory.
2. It is unitary.
3. It is exactly dual to the bulk gravity theory.
4. Therefore, the bulk theory is unitary.
5. Therefore, information is not lost.

The path integral argument in the paper is Hawking's attempt to see unitarity directly in the bulk, without relying on the boundary theory. It is an important conceptual step, though the detailed mechanism was not fully understood until the island formula.

### What Hawking Did NOT Say

Hawking did not identify which of his 1976 assumptions was wrong. He did not derive the Page curve. He did not explain how the Hawking radiation carries information at the level of individual quanta. He did not address the firewall problem (which had not yet been formulated). The paper is more of a change of philosophical position than a solution of the information paradox.

### The Bet

Hawking had bet Preskill (and Thorne) in 1997 that information is lost. Hawking conceded and gave Preskill a baseball encyclopedia (the *Total Baseball* encyclopedia, representing information about a game -- a nod to the information content). Thorne never conceded.

---

## Impact and Legacy

### Validation of AdS/CFT

Hawking's concession was seen as a validation of the AdS/CFT approach to quantum gravity. If even the inventor of the information paradox accepted that information is preserved, the case for AdS/CFT was strengthened.

### The Page Curve

The paper does not derive the Page curve (the expected behavior of the entanglement entropy of the radiation over the lifetime of the black hole). Page (1993) had shown that unitarity requires the entanglement entropy to increase during the first half of the evaporation and decrease during the second half (after the "Page time"), returning to zero when the black hole has fully evaporated. Hawking's paper is consistent with but does not derive this behavior.

The Page curve was finally derived from semiclassical gravity by Penington (2019) and Almheiri et al. (2019) using the island formula. This is widely considered the resolution of the information paradox in the semiclassical regime.

### Sum Over Topologies and Replica Wormholes

Hawking's idea of summing over topologies has been vindicated in a precise sense by the replica trick calculations of 2019--2020. The "replica wormholes" that give the island formula are precisely the non-trivial topologies that Hawking proposed contribute to the path integral. In this sense, Hawking's 2005 paper was more correct than he knew -- the mechanism he proposed (sum over topologies) IS the mechanism that resolves the paradox.

### Open Questions

1. **Asymptotically flat space**: The argument uses AdS boundary conditions. Does information recovery work in asymptotically flat spacetimes (our universe)?

2. **Real-time mechanism**: How does information actually escape? The path integral argument is Euclidean and does not provide a real-time narrative.

3. **Firewalls**: Does the information escape *at* the horizon (firewall/fuzzball) or only in the global path integral sense?

4. **The bag of gold**: Can spacetimes with large interiors behind small horizons (bags of gold) exist? These seem to violate the Bekenstein bound.

---

## Connections to Modern Physics

1. **Island formula (2019)**: The entanglement entropy of the Hawking radiation receives contributions from "islands" -- regions inside the black hole that are entangled with the radiation. The entropy is:
   $$S_{\text{rad}} = \min \left\{ \text{ext} \left[ \frac{A(\partial I)}{4G_N} + S_{\text{bulk}}(I \cup R) \right] \right\}$$
   where $I$ is the island and $R$ is the radiation region. This formula gives the Page curve and resolves the information paradox at the semiclassical level.

2. **Replica wormholes**: The island formula arises from saddle points of the gravitational path integral computed using the replica trick. The non-trivial saddle points are "replica wormholes" -- geometries that connect different replicas. These are the specific realization of Hawking's "sum over topologies."

3. **Quantum extremal surfaces**: The generalization of the Ryu--Takayanagi formula to include quantum corrections (Engelhardt and Wall, 2015) is the key ingredient in the island formula. The quantum extremal surface competes with the classical RT surface, and the transition between them corresponds to the Page time.

4. **Black hole interior reconstruction**: In AdS/CFT, operators behind the horizon can be reconstructed from the boundary using state-dependent (Papadodimas--Raju, 2013) or island-based methods. This connects to the question of whether the black hole interior is "real" or an emergent description.

5. **For the exflation framework**: The sum-over-topologies approach is naturally compatible with Kaluza--Klein frameworks, where the topology of the internal space is an additional variable. The path integral over internal topologies could provide the KK analogue of replica wormholes. If the internal space has nontrivial topology changes (e.g., the Jensen deformation changing the topology of the SU(3) fiber), these could contribute to information recovery in the same way that replica wormholes do in the standard calculation.
