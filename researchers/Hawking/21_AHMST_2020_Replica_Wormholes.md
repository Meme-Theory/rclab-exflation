# Replica Wormholes and the Entropy of Hawking Radiation

**Author(s):** Ahmed Almheiri, Thomas Hartman, Juan Maldacena, Edgar Shaghoulian, Amirhossein Tajdini
**Year:** 2020
**Journal:** Journal of High Energy Physics 2020, 013 (2020)
**arXiv:** 1911.12333
**Relevance:** HIGH

---

## Abstract

The information paradox can be realized in anti-de Sitter spacetime joined to a Minkowski region. In this setting, we show that the large discrepancy between the von Neumann entropy as calculated by Hawking and the requirements of unitarity is fixed by including new saddles in the gravitational path integral. These saddles arise in the replica method as complexified wormholes connecting different copies of the black hole. As the replica number $n \to 1$, the presence of these wormholes leads to the island rule for the computation of the fine-grained gravitational entropy. We discuss these replica wormholes explicitly in two-dimensional Jackiw-Teitelboim gravity coupled to matter.

---

## Key Arguments and Derivations

### The Information Paradox in AdS + Bath

The setup consists of an AdS$_2$ black hole (described by Jackiw-Teitelboim gravity) coupled to a flat-space bath where Hawking radiation can escape. Hawking's calculation gives a monotonically increasing entropy for the radiation, violating unitarity.

### The Replica Method

To compute the von Neumann entropy $S = -\text{Tr}(\rho \log \rho)$, one uses the replica trick:

$$S = -\lim_{n \to 1} \frac{\partial}{\partial n} \text{Tr}(\rho^n)$$

In the gravitational path integral, $\text{Tr}(\rho^n)$ involves $n$ copies of the spacetime glued together. The key insight is that there exist new saddle points: **replica wormholes** connecting different copies.

### The Island Rule

As $n \to 1$, the replica wormhole saddle yields the **island rule** for gravitational entropy:

$$S(R) = \min\left\{\text{ext}_{I}\left[\frac{\text{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I)\right]\right\}$$

where:
- $R$ is the radiation region
- $I$ is the "island" -- a region of spacetime that is encoded in the radiation
- $\partial I$ is the quantum extremal surface (boundary of the island)
- $S_{\text{bulk}}$ is the bulk entanglement entropy of quantum fields

### Two Saddles and the Page Curve

There are two competing saddles in the gravitational path integral:

1. **No-island saddle** (Hawking): $S(R) = S_{\text{bulk}}(R)$, which grows monotonically.
2. **Island saddle**: $S(R) = \frac{\text{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I)$, which decreases as the BH shrinks.

The physical entropy is the minimum of the two, giving the **Page curve**: the entropy rises until the Page time, then decreases.

### JT Gravity Calculation

In 2D JT gravity with action:

$$I = -\frac{S_0}{4\pi}\left[\int_M R + 2\int_{\partial M} K\right] - \frac{1}{4\pi}\left[\int_M \phi(R+2) + 2\int_{\partial M} \phi K\right]$$

the island boundary is at the quantum extremal surface where:

$$\frac{\partial}{\partial x}\left[\frac{\phi(x)}{4G_N} + S_{\text{bulk}}(R \cup I)\right] = 0$$

The replica wormholes are solutions where the $n$ copies of the geometry are connected through the region near the horizon, and they contribute a factor $e^{(1-n)S_0}$ relative to the disconnected geometry.

### Generalized Entropy and the QES

The generalized entropy is:

$$S_{\text{gen}} = \frac{\text{Area}}{4G_N} + S_{\text{bulk}}$$

The quantum extremal surface (QES) extremizes $S_{\text{gen}}$. The island rule states that the gravitational entropy of a region is the minimum of $S_{\text{gen}}$ over all possible QES locations, including the empty surface.

---

## Key Results

1. **Replica wormholes** -- new saddles in the gravitational path integral connecting $n$ replicas -- resolve the information paradox by producing the island contribution to the entropy.
2. The island rule $S(R) = \min\{\text{ext}[\text{Area}/4G_N + S_{\text{bulk}}]\}$ emerges naturally from the $n \to 1$ limit of replica wormholes.
3. The Page curve is reproduced: two saddles compete, with a transition at the Page time.
4. The calculation is explicit in JT gravity coupled to a CFT, providing the first derivation of the Page curve from a gravitational path integral.
5. The island saddle dominates at late times, encoding part of the black hole interior in the radiation.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Island rule | $S(R) = \min\left\{\text{ext}_I\left[\frac{\text{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I)\right]\right\}$ | Eq. (1.2) |
| Replica trick | $S = -\lim_{n\to 1}\frac{\partial}{\partial n}\text{Tr}(\rho^n)$ | Sec. 2 |
| Generalized entropy | $S_{\text{gen}} = \frac{\text{Area}}{4G_N} + S_{\text{bulk}}$ | Sec. 1 |
| QES condition | $\frac{\partial S_{\text{gen}}}{\partial x} = 0$ | Sec. 3 |
| JT gravity action | $I = -\frac{S_0}{4\pi}[\int R + 2\int K] - \frac{1}{4\pi}[\int \phi(R+2) + 2\int \phi K]$ | Sec. 2 |
| Hawking entropy (no island) | $S(R) = \frac{c}{6}\log t$ (growing) | Sec. 1 |
| Island entropy (late time) | $S(R) \approx 2S_0 + 2\phi_h/(4G_N)$ (BH entropy, decreasing) | Sec. 3 |
| Wormhole weight | $\sim e^{(1-n)S_0}$ relative to disconnected | Sec. 2 |

## Relevance to Phonon-Exflation

Replica wormholes provide the gravitational path integral derivation of the Page curve. In the phonon-exflation framework, no replica wormhole calculation is needed: the transit produces a product state with $S_{\text{ent}} = 0$ exactly (GGE from integrability, 8 Richardson-Gaudin conserved quantities). There is no entanglement between "early" and "late" radiation because there is no radiation at all -- the transit is a single coherent event, not a prolonged evaporation process. The replica method itself is a tool for Euclidean quantum gravity; the framework's spectral action = entropy identity (Paper 20) provides the entropy directly without need for replicas.
