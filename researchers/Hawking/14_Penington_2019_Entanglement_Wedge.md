# Entanglement Wedge Reconstruction and the Information Problem

**Author(s):** Geoffrey Penington
**Year:** 2019
**Journal:** Journal of High Energy Physics 2020, 002 (2020)
**arXiv:** 1905.08255
**Relevance:** CRITICAL

---

## Abstract

When absorbing boundary conditions are used to evaporate a black hole in AdS/CFT, we show that there is a phase transition in the location of the quantum Ryu-Takayanagi surface, at precisely the Page time. The new RT surface lies slightly inside the event horizon, at an infalling time approximately the scrambling time $\beta/2\pi \log S_{BH}$ into the past. We can immediately derive the Page curve, using the Ryu-Takayanagi formula, and the Hayden-Preskill decoding criterion, using entanglement wedge reconstruction. Because part of the interior is now encoded in the early Hawking radiation, the decreasing entanglement entropy of the black hole is exactly consistent with the semiclassical bulk entanglement of the late-time Hawking modes, despite the absence of a firewall.

By studying the entanglement wedge of highly mixed states, we can understand the state dependence of the interior reconstructions. A crucial role is played by the existence of tiny, non-perturbative errors in entanglement wedge reconstruction. Directly after the Page time, interior operators can only be reconstructed from the Hawking radiation if the initial state of the black hole is known. As the black hole continues to evaporate, reconstructions become possible that simultaneously work for a large class of initial states. Using similar techniques, we generalise Hayden-Preskill to show how the amount of Hawking radiation required to reconstruct a large diary, thrown into the black hole, depends on both the energy and the entropy of the diary. Finally we argue that, before the evaporation begins, a single, state-independent interior reconstruction exists for any code space of microstates with entropy strictly less than the Bekenstein-Hawking entropy, and show that this is sufficient state dependence to avoid the AMPSS typical-state firewall paradox.

---

## Key Arguments and Derivations

### Setup: Evaporating Black Hole in AdS/CFT

A black hole in AdS is coupled to an external bath (Minkowski region) via absorbing boundary conditions. The Hawking radiation escapes into the bath. The question is: what is the entanglement entropy of the radiation as a function of time?

### Phase Transition at the Page Time

Before the Page time, the quantum RT surface for the radiation is empty -- the entanglement wedge of the radiation is the bath itself. The entropy grows linearly as Hawking pairs are produced.

After the Page time, a new quantum RT surface appears slightly inside the event horizon, at an infalling time approximately $t_{\text{scr}} = \beta/(2\pi) \log S_{BH}$ into the past. The entanglement wedge of the radiation now includes part of the black hole interior.

### The Island Formula

The entanglement entropy of the radiation $R$ is computed via the quantum Ryu-Takayanagi formula:

$$S(R) = \min \left\{ \text{ext}_I \left[ \frac{\text{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I) \right] \right\}$$

where $I$ is the "island" -- a region in the bulk whose boundary $\partial I$ is the quantum extremal surface.

### Hayden-Preskill Decoding

After the Page time, a diary thrown into the black hole can be decoded from the radiation after waiting a scrambling time $t_{\text{scr}} \sim \beta \log S_{BH}$. The amount of radiation needed depends on both the energy $E_d$ and entropy $S_d$ of the diary.

### State Dependence

Interior operators are state-dependent near the Page time. As more radiation is collected, state-independent reconstructions become possible. Before evaporation, state-independent interior reconstruction exists for code spaces with entropy strictly less than $S_{BH}$.

---

## Key Results

1. The quantum RT surface undergoes a phase transition at the Page time, jumping from empty to a surface slightly inside the horizon.
2. The Page curve is derived from the RT formula without any new dynamical input beyond entanglement wedge reconstruction.
3. The Hayden-Preskill protocol is derived: a diary can be decoded from radiation after the scrambling time $t_{\text{scr}} = \beta/(2\pi) \log S_{BH}$.
4. Interior operators are state-dependent immediately after the Page time, becoming state-independent as evaporation continues.
5. The AMPSS typical-state firewall paradox is avoided by the state dependence inherent in entanglement wedge reconstruction.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Island formula | $S(R) = \min\left\{\text{ext}_I\left[\frac{\text{Area}(\partial I)}{4G_N} + S_{\text{bulk}}(R \cup I)\right]\right\}$ | Eq. (1.1) |
| Scrambling time | $t_{\text{scr}} = \frac{\beta}{2\pi} \log S_{BH}$ | Sec. 1 |
| Before Page time | $S(R) = S_{\text{bulk}}(R) \approx \frac{c}{6} \log t$ (growing) | Sec. 2 |
| After Page time | $S(R) \approx S_{BH}(t) - S_{\text{bulk}}(\text{interior modes})$ (decreasing) | Sec. 2 |
| Bekenstein-Hawking entropy | $S_{BH} = \frac{\text{Area}}{4G_N}$ | Throughout |
| Diary decoding condition | $S_{\text{rad}} \geq S_{BH} + S_d - E_d / T_H$ | Sec. 4 |

## Relevance to Phonon-Exflation

The island formula and entanglement wedge reconstruction provide the modern resolution of the information paradox in AdS/CFT. The phonon-exflation framework has no horizon and no information paradox: the transit is a Parker-type particle creation process (no thermal spectrum), the post-transit state is a GGE with $S_{\text{ent}} = 0$ (product state), and no island formula is needed. The framework evades Penington's setup entirely by producing no event horizon.
