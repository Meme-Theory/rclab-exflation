# Black Holes: Complementarity vs. Firewalls

**Author(s):** Ahmed Almheiri, Donald Marolf, Joseph Polchinski, James Sully
**Year:** 2013
**Journal:** Journal of High Energy Physics 2013, 062 (2013)
**arXiv:** 1207.3123
**Relevance:** HIGH

---

## Abstract

We argue that the following three statements cannot all be true: (i) Hawking radiation is in a pure state, (ii) the information carried by the radiation is emitted from the region near the horizon, with low energy effective field theory valid beyond some microscopic distance from the horizon, and (iii) the infalling observer encounters nothing unusual at the horizon. Perhaps the most conservative resolution is that the infalling observer burns up at the horizon. Alternatives would seem to require novel dynamics that nevertheless cause notable violations of semiclassical physics at macroscopic distances from the horizon.

---

## Key Arguments and Derivations

### The Three Postulates of Black Hole Complementarity

The paper examines the compatibility of three widely-held postulates:

1. **Postulate 1 (Unitarity):** The process of formation and evaporation of a black hole, as viewed by a distant observer, can be described entirely within the context of standard quantum mechanics. In particular, there exists a unitary S-matrix which describes the evolution from infalling matter to outgoing Hawking-like radiation.

2. **Postulate 2 (Effective Field Theory):** Outside the stretched horizon of a massive black hole, physics can be described to good approximation by a set of semi-classical field equations (low-energy effective field theory is valid beyond some microscopic distance from the horizon).

3. **Postulate 3 (No Drama):** An observer falling into a black hole encounters nothing out of the ordinary at the horizon. The equivalence principle holds at the horizon.

### The AMPS Argument

AMPS show these three postulates are mutually inconsistent for an old black hole (past the Page time). The argument proceeds:

**Step 1:** By Postulate 1, the radiation is in a pure state. After the Page time, an early Hawking mode $B$ is maximally entangled with the early radiation $R_B$.

**Step 2:** By Postulate 3, the late Hawking mode $B$ must be maximally entangled with its interior partner $A$ (this is the near-horizon vacuum entanglement required by the equivalence principle).

**Step 3:** But by strong subadditivity of entanglement entropy, a system cannot be maximally entangled with two independent systems simultaneously:

$$S(B) + S(ABR_B) \leq S(AB) + S(BR_B)$$

If $B$ is maximally entangled with both $A$ and $R_B$, this inequality is violated.

### The Firewall Resolution

AMPS propose that the most conservative resolution is to give up Postulate 3: the infalling observer encounters a "firewall" -- a high-energy curtain of radiation at the horizon that destroys anything falling in. This means the interior of the black hole may not exist as a smooth spacetime.

### Extensions

- The argument extends to all partial waves, not just the $s$-wave.
- Black hole mining (extracting energy from just outside the horizon) strengthens the argument by forcing the effective field theory region closer to the horizon.
- Relaxing Postulate 2 requires radical modifications to physics at macroscopic distances from the horizon.

---

## Key Results

1. The three postulates of black hole complementarity (unitarity, EFT outside horizon, no drama at horizon) are **mutually inconsistent** for old black holes.
2. Strong subadditivity of entanglement entropy is the key tool: a mode cannot be maximally entangled with two independent systems.
3. The "most conservative" resolution is a **firewall** at the horizon, violating the equivalence principle.
4. The argument applies for any black hole older than the Page time (when more than half the entropy has been radiated).
5. Black hole mining strengthens the argument by extending it to all angular momentum modes.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Strong subadditivity | $S(B) + S(ABR_B) \leq S(AB) + S(BR_B)$ | Sec. 2 |
| Maximal entanglement (purity) | $S(BR_B) = 0$ (after Page time, $B$ purified by $R_B$) | Sec. 2 |
| Near-horizon vacuum | $S(AB) = 0$ (equivalence principle requires $A$-$B$ entanglement) | Sec. 2 |
| Contradiction | $S(B) \leq 0$ (impossible for a nontrivial system) | Sec. 2 |
| Page time condition | $S_{\text{rad}} > S_{BH}$ (radiation entropy exceeds BH entropy) | Sec. 1 |
| Bekenstein-Hawking | $S_{BH} = A/(4G_N)$ | Throughout |

## Relevance to Phonon-Exflation

The AMPS firewall paradox arises from the tension between unitarity, horizon smoothness, and effective field theory. The phonon-exflation framework evades AMPS entirely: there is **no horizon** in the framework. The transit is a Parker-type cosmological particle creation process with no event horizon, no trapped surface, and no causal barrier. The post-transit GGE has $S_{\text{ent}} = 0$ exactly (product state from integrability). No firewall is needed because there is no horizon to burn up at.
