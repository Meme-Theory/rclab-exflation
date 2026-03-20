# Thermodynamics of Black Holes in Anti-de Sitter Space

**Authors:** Stephen W. Hawking, Don N. Page
**Year:** 1983
**Journal:** Communications in Mathematical Physics 87, 577-588 (1983)

---

## Abstract

We investigate the thermodynamic properties of black holes in Anti-de Sitter (AdS) spacetime, where the black hole is immersed in a thermal bath at the temperature of the AdS boundary. Unlike asymptotically flat spacetime, where black holes are unstable to evaporation, AdS black holes can be in thermal equilibrium with their surroundings. We compute the free energy and entropy for black holes of various sizes and determine the conditions under which a black hole is thermodynamically favored over thermal AdS space. We show that there is a critical temperature below which thermal AdS is preferred, and above which an AdS black hole undergoes a phase transition to become the dominant configuration. This Hawking-Page phase transition has profound implications for the interpretation of gravity in terms of gauge theory via the AdS/CFT correspondence.

---

## Historical Context

By 1983, Hawking radiation and black hole thermodynamics were well-established. However, the interpretation remained puzzling: in asymptotically flat spacetime, black holes evaporate completely, a process that appears to violate quantum information conservation. In AdS spacetime, the situation is dramatically different.

Anti-de Sitter space is a spacetime of constant negative curvature, described by the metric:

$$ds^2 = -\left(1 + \frac{r^2}{L^2}\right) dt^2 + \left(1 + \frac{r^2}{L^2}\right)^{-1} dr^2 + r^2 (d\theta^2 + \sin^2\theta d\phi^2)$$

where $L$ is the AdS radius of curvature. The negative cosmological constant creates a confining boundary at $r \to \infty$, preventing radiation from escaping to infinity. This fundamentally changes the thermodynamic stability of black holes.

Hawking and Page discovered that AdS black holes can be in thermal equilibrium with thermal AdS space (the AdS vacuum at finite temperature). They computed the partition function and found a phase transition: at low temperatures, empty AdS dominates; at high temperatures, a black hole is thermodynamically favored.

This was a remarkable theoretical insight that would later become central to understanding AdS/CFT and the confinement-deconfinement transition in gauge theories.

---

## Key Arguments and Derivations

### Thermodynamic Setup

In AdS space with a black hole, the system is in thermal equilibrium at temperature $T$. The Hawking temperature of a Schwarzschild-AdS black hole with mass $M$ is:

$$T_H = \frac{\kappa}{2\pi} = \frac{r_+^2 + L^2}{4\pi L^2 r_+}$$

where $r_+$ is the event horizon radius and $\kappa$ is the surface gravity.

Unlike flat space, in AdS the thermal radiation is **confined**. The boundary condition at $r \to \infty$ (where AdS space approaches a "wall") reflects radiation back, maintaining thermal equilibrium.

### Free Energy Calculation

The thermodynamic potential is the Helmholtz free energy:

$$F = M - TS$$

where:
- $M$ is the ADM mass
- $T$ is the temperature
- $S$ is the entropy

For a black hole in AdS:

$$M = \frac{r_+^2 + L^2}{2L^2} r_+$$

(reduced to 4D; in higher dimensions, the formula is more complicated but analogous)

The entropy is given by the Bekenstein-Hawking formula:

$$S = \frac{A}{4} = \pi r_+^2$$

(in units where $\hbar = c = G = 1$)

The free energy of a black hole at temperature $T$ is:

$$F_\text{BH}(T) = M - TS = \frac{r_+(T)^2 + L^2}{2L^2} r_+(T) - T \pi r_+(T)^2$$

where $r_+(T)$ is determined by $T = T_H(r_+)$, the Hawking temperature relation.

### Phase Transition Condition

Hawking and Page compared this to the free energy of **pure AdS at temperature** $T$:

$$F_\text{AdS}(T) = 0$$

(by definition—we set AdS as the reference state)

The phase transition occurs when:

$$F_\text{BH}(T_*) = F_\text{AdS}(T_*) = 0$$

$$\Rightarrow \quad M(T_*) = T_* S(T_*)$$

Solving, they found:

$$T_* = \frac{1}{\pi L}$$

**Below** $T_*$: $F_\text{BH} > 0$, so thermal AdS is favored.
**Above** $T_*$: $F_\text{BH} < 0$, so the black hole is favored.

### Critical Radius

The phase transition corresponds to a critical horizon radius:

$$r_* = L$$

At this point, the black hole radius equals the AdS radius. For $r_+ < L$, the black hole is unstable; for $r_+ > L$, it is stable.

### Entropy Behavior

An important observation: as temperature increases, the black hole's entropy $S = \pi r_+^2$ increases. At the phase transition:

$$\frac{dS}{dT}\bigg|_{T=T_*} = \text{finite and positive}$$

This is unlike flat-space black holes, where the heat capacity $C = T \frac{dS}{dT}$ is negative (black holes cool as they evaporate).

For AdS black holes, the heat capacity can be positive or negative depending on size. Larger black holes have positive heat capacity and can be in stable thermal equilibrium.

---

## Key Results

1. **Phase transition in AdS**: At $T = T_* = 1/(\pi L)$, the system undergoes a first-order phase transition between thermal AdS (low-$T$) and AdS black hole (high-$T$).

2. **Critical horizon radius**: The transition occurs at $r_+ = L$, where black hole size equals the AdS length scale.

3. **Latent heat**: The entropy discontinuity across the transition is:

$$\Delta S = \pi L^2$$

representing a latent heat absorbed/released during the transition.

4. **Stability diagram**: For a given $T$, one can plot which configuration (AdS vs black hole) minimizes free energy. This creates a phase diagram analogous to liquid-gas transitions in ordinary thermodynamics.

5. **No evaporation in equilibrium**: Unlike flat-space black holes, AdS black holes in thermal equilibrium do not evaporate. The confining geometry stabilizes them.

6. **Confinement interpretation**: The phase transition reflects a confinement-deconfinement transition in the holographic dual gauge theory (realized later with AdS/CFT).

---

## Impact and Legacy

**Foundation for AdS/CFT**: The Hawking-Page phase transition became one of the key pieces of evidence supporting the AdS/CFT correspondence (discovered by Maldacena in 1997). In the dual gauge theory, the phase transition corresponds to the confinement-deconfinement transition (hadrons ↔ free quarks and gluons).

**Black Hole Thermodynamics in AdS**: The paper established that black holes in anti-de Sitter space are fundamentally different from their flat-space cousins. AdS confines radiation, allowing stable thermal equilibrium configurations.

**Phase Transitions in Gauge/Gravity Duality**: The Hawking-Page transition became a paradigm for studying phase transitions via holography, leading to a rich literature on conformal field theory phase diagrams and their gravitational duals.

**Information Recovery**: Unlike flat-space Hawking evaporation (where information escapes to infinity, raising paradoxes), AdS black hole evaporation is reversible and unitary in the confining geometry. This was crucial for resolving information paradoxes in holographic theories.

**Entropy and Confinement**: The entropy increase across the transition, $\Delta S = \pi L^2$, is proportional to the boundary area (in 2D, the boundary is a circle of circumference $2\pi L$). This holographic relation between bulk entropy and boundary area became a hallmark of modern quantum gravity.

**Black Hole Thermodynamics Review**: The paper is a standard reference in any comprehensive review of black hole thermodynamics and remains widely cited in research on holographic phase transitions.

---

## Connection to Phonon-Exflation Framework

**STRUCTURAL ANALOGY — Priority A**

The Hawking-Page phase transition between AdS black hole and thermal AdS is **structurally analogous** to the BCS phase transition in the phonon-exflation fold transit. Here is the correspondence:

| Hawking-Page AdS Transition | Phonon-Exflation BCS Phase Transition |
|:-----|:-----|
| Thermal AdS background (confined geometry) | Dirac sea vacuum (Jensen-normalized, confined spectral structure) |
| Black hole (macroscopic object) | BCS condensate (Cooper pairs, collective state) |
| Temperature $T$ | Fold parameter $\tau$ (controls correlation structure) |
| Free energy $F_\text{BH} = M - TS$ | Free energy of BCS state $F_\text{BCS}(\tau)$ |
| Critical temperature $T_* = 1/(\pi L)$ | Critical fold parameter $\tau_* \approx 0.20$ (Session 35) |
| Entropy jump $\Delta S = \pi L^2$ | Entropy change (GGE entropy increase during transit) |
| Confinement → deconfinement | Dirac sea (ordered) → GGE relic (integrably disordered) |
| Phase transition at $r_+ = L$ | Phase transition at K_7 condensate collapse |

**Framework correspondence in detail**:

In the Hawking-Page transition:
- **Order parameter**: Horizon radius $r_+$. Below $T_*$, $r_+$ is small (no stable black hole); above, it grows (black hole is thermodynamically favored).
- **Free energy landscape**: $F(r_+; T)$ has a minimum at small $r_+$ (AdS) for $T < T_*$ and at large $r_+$ (black hole) for $T > T_*$.

In the phonon-exflation fold transit:
- **Order parameter**: K_7 condensate amplitude $\Delta_K$ (Session 35 found this breaks U(1)_7 spontaneously at the fold).
- **Free energy landscape**: $F(\Delta_K; \tau)$ minimizes at $\Delta_K = 0$ (Dirac sea) for $\tau < \tau_*$ and at $\Delta_K > 0$ (Cooper pairs) for $\tau > \tau_*$.

The phase transition is **first-order** in both cases: the order parameter discontinuously jumps at the critical point.

**Thermodynamic consistency**:

Hawking-Page showed that the AdS black hole phase transition is thermodynamically consistent—entropy increases, free energy decreases, no information is lost. Similarly, Session 38 showed that the phonon-exflation fold transit is thermodynamically consistent: the GGE relic has entropy bounded by Richardson-Gaudin conserved charges, and integrability ensures no information is lost (S_ent = 0, all information in the 8 integrals).

**Prediction**:

The fold transit should exhibit a **latent heat** (energy discontinuity) analogous to Hawking and Page's black hole transition. This would manifest as:
1. A discontinuous jump in the effective Hubble parameter $H$ as $\tau$ crosses the fold
2. A spike in gravitational-wave production at the transition moment (from the entropy-flow dynamics)
3. A residual "fossil" entropy in the post-transit state (encoded in the GGE, not observable as thermal radiation)

Testing this prediction requires:
- Detailed numerical simulations of the fold transit (GPE solver in `phonon-exflation-sim/`)
- Computation of the gravitational-wave spectrum during the transition
- Comparison to LIGO/Virgo observations and PTA gravitational-wave backgrounds

**Confinement analog**: Just as the AdS boundary confines radiation and stabilizes the black hole, the **topological protection** of the BDI fermion sector confines the GGE relic. Information cannot escape the K_7-protected structure; it remains encoded in the 8 conserved charges. This is the framework's version of "no evaporation" in AdS.

---

## References

- Hawking, S. W., Page, D. N., "Thermodynamics of black holes in anti-de Sitter space," *Commun. Math. Phys.* **87**, 577–588 (1983).
- Maldacena, J. M., "The large-N limit of superconformal field theories and supergravity," *Adv. Theor. Math. Phys.* **2**, 231 (1998).
- Witten, E., "Anti de Sitter space and holography," *Adv. Theor. Math. Phys.* **2**, 253 (1998).
- Page, D. N., "Hawking radiation and black hole thermodynamics," *J. Phys. A* **36**, 9185 (2003).
- Chamblin, A., Emparan, R., Johnson, C. V., Myers, R. C., "Charged AdS black holes and catastrophic holography," *Phys. Rev. D* **60**, 064018 (1999).
