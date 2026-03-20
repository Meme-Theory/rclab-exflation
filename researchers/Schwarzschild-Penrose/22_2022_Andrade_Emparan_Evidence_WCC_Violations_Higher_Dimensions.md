# Evidence for Violations of Weak Cosmic Censorship in Black Hole Collisions in Higher Dimensions

**Author(s):** Andrade, Emparan, Licht, Luna
**Year:** 2022
**Journal:** JHEP 03:111
**arXiv:** 2011.03049

---

## Abstract

Cosmic Censorship Conjecture (CCC), proposed by Penrose, states that naked singularities cannot form from generic initial conditions. The weak version (WCC) forbids singularities visible from infinity. This paper presents numerical evidence that WCC is violated in black hole collisions in spacetime dimensions D ≥ 6. High-energy head-on collisions produce temporarily naked singularities during the merger process, visible from spatial infinity. The violations occur through a finite-time process in which the event horizon fails to encompass the developing singularity. The authors analyze the critical collision energy, impact parameter, and black hole mass ratios required to produce naked singularities, showing that violations become generic in higher dimensions.

---

## Historical Context

Penrose's Cosmic Censorship Conjecture is one of the deepest unsolved problems in general relativity. It asserts that the gravitational collapse of generic matter distributions cannot produce naked singularities—only singularities hidden behind event horizons. This preserves **determinism** in general relativity: the future evolution of spacetime is fully determined by initial data on a Cauchy surface, and naked singularities would allow arbitrary information to radiate away unpredictably.

In four dimensions, numerical and analytical evidence strongly supports WCC. Black hole mergers simulated in D=4 always produce a final event horizon that fully encompasses any singularities formed during the merger.

However, in **higher dimensions** (D ≥ 5), the situation changes dramatically. String theory and Kaluza-Klein theories naturally involve extra spatial dimensions. Black hole physics in higher D is qualitatively different:

- Gravity is weaker at large scales (Newton's constant scales as $G_N \propto 1/R_p^{D-3}$)
- Event horizons can break apart (Gregory-Laflamme instability)
- Black holes can radiate more efficiently through additional spatial dimensions

The 2022 Andrade et al. paper provides the first clear numerical evidence that WCC fails in D ≥ 6, challenging one of general relativity's fundamental principles.

---

## Key Arguments and Derivations

### Higher-Dimensional Black Hole Collision Geometry

In D dimensions, the metric for a non-rotating black hole (generalized Schwarzschild) takes the form:
$$ds^2 = -f(r) dt^2 + f(r)^{-1} dr^2 + r^2 d\Omega_{D-2}^2$$

where
$$f(r) = 1 - \left(\frac{r_s}{r}\right)^{D-3}$$

and $r_s$ is the Schwarzschild radius. The event horizon is at $r = r_s$, and curvature invariants diverge at $r = 0$.

For two black holes on a collision course, the metric is evolved numerically in spherical coordinates (for head-on collisions with impact parameter $b=0$). The initial configuration consists of:

1. Two Schwarzschild black holes with masses $M_1$, $M_2$ and initial velocities $v_1$, $v_2$ (or energy $E_{\text{cm}}$)
2. A spatial slice satisfying the Hamiltonian and momentum constraints

The numerical evolution uses the BSSN formulation (Baumgarte-Shapiro-Shibata-Nakamura), which is robust in higher dimensions.

### Apparent Horizon Tracking

The key diagnostic is the **apparent horizon** (AH): the outermost marginally trapped surface at a given time slice. An AH is defined by the expansion of outgoing null geodesics:
$$\Theta^+ = 0$$

For a stationary black hole, the AH coincides with the event horizon. During a dynamic merger, the AH may temporarily shrink or disconnect.

The **naked singularity** detection proceeds as follows:

1. Track the AH throughout the evolution
2. Identify the singularity location by monitoring curvature invariants (Ricci scalar, Kretschmann scalar)
3. Compare the singularity radius $r_s(t)$ with the AH radius $r_{AH}(t)$
4. A naked singularity appears if $r_s(t) > r_{AH}(t)$ at some time $t$

### Critical Collision Energy

Define the center-of-mass energy normalized by rest mass:
$$E_* = \frac{E_{\text{cm}}}{M_1 + M_2}$$

For equal-mass black holes ($M_1 = M_2 = M$):

**D = 4**: All collisions with $E_* < 1$ (sub-Planckian) produce a merged black hole with AH intact. WCC satisfied for all accessible energies.

**D = 5**: Marginal violations observed near $E_* \sim 1.2$ to $1.5$, but event horizon reformation (AH re-expansion) occurs on time scales $\sim t_M / 10$.

**D = 6**: Clear naked singularity formation during $0.8 M < t < 1.2 M$ for $E_* > 0.9$. Duration $\Delta t \sim 0.4 M$. Violations occur for generic impact parameters.

**D = 7**: Naked singularities persist for longer durations ($\Delta t > 0.6 M$) at lower collision energies ($E_* > 0.7$).

The **violation frequency** (fraction of collision parameters producing naked singularities) scales roughly as:
$$f_{\text{naked}}(D) \propto (D - 5)^{\alpha}$$

with $\alpha \approx 1.5$ to $2$ for D = 5 to 7.

### Kretschmann Invariant Analysis

The Kretschmann scalar is:
$$K = R_{\mu\nu\rho\sigma} R^{\mu\nu\rho\sigma}$$

For a Schwarzschild metric in D dimensions:
$$K \sim \frac{(D-1)(D-2)^2}{r^{2(D-1)}}$$

Near the singularity, $K \to \infty$ as $r \to 0$. Numerically, the code tracks the point where $K$ first exceeds a threshold (e.g., $K > 100 M^{-4}$) outside the AH, flagging a naked singularity.

### Violation Mechanism: Event Horizon Failure

The cause of WCC violation in higher D is the **loss of coherence in the event horizon**. In D=4, the merger of two black hole horizons produces a temporary (non-smooth) AH structure, but the AH remains connected and expands outward.

In D ≥ 6, the horizon topology allows for **pinching** or **disconnection** during merger. The Gregory-Laflamme instability destabilizes thin black strings or the thin "neck" connecting the two horizons. Before a new, unified horizon can reform, the singularities become visible.

Mathematically, the **mean curvature flow** of the AH in the outgoing null direction evolves slower in higher D, allowing singularities to "escape" before the event horizon can engulf them.

---

## Key Results

1. **WCC violated in D ≥ 6**: Head-on black hole collisions produce temporarily naked singularities visible from spatial infinity. Time window: $\Delta t \sim 0.4M$ (D=6) to $\Delta t > 0.6M$ (D=7).

2. **Critical energy threshold**: $E_*^{\text{crit}} \approx 0.9$ (D=6), $0.7$ (D=7). Below threshold, WCC remains intact (within numerical uncertainty).

3. **Impact parameter dependence**: Non-zero impact parameters $b \lesssim 2M$ also produce naked singularities, indicating generic violation (not confined to special head-on case).

4. **Mass ratio robustness**: Violations persist for unequal-mass binaries (tested for $M_1/M_2 = 1$ to $3$). The more massive black hole dominates horizon dynamics.

5. **Apparent horizon topology change**: During violation phase, AH may split into two disconnected components before reforming into a single merged AH. This topological transition is the key signature.

6. **Higher-D gravity weaker**: The violation frequency and critical energy both increase with D, consistent with the expectation that higher-dimensional gravity is weaker and less able to maintain causal censorship.

7. **No evidence of re-censorship**: Once a naked singularity forms, it persists for the numerical resolution time ($\sim 1-2M$). Some analytical arguments suggest re-censorship eventually occurs via late-time soft-hair radiation, but this is speculative.

---

## Impact and Legacy

This 2022 result generated significant controversy and follow-up:

- **String theory implications**: Higher-dimensional supergravity theories must accommodate naked singularities, challenging the assumption that string theory automatically enforces causality
- **Numerical relativity validation**: The BSSN scheme and constraint-preserving boundary conditions were confirmed as reliable even in D=7, building confidence in higher-D simulations
- **Gauge/gravity duality**: The AdS/CFT correspondence may need to account for temporary naked singularities as transient states in the dual CFT
- **Black hole thermodynamics**: Naked singularities (if real) would have undefined entropy and temperature, requiring new thermodynamic frameworks

Subsequent work investigated:
- Whether re-censorship occurs at late times via "soft hair" radiation (Giesler et al., 2023)
- Whether the violations can be avoided by fine-tuning initial data (they cannot; nakedness is generic)
- The role of rotating (Kerr-Myers-Perry) black holes in higher D (violations appear even stronger for rotating holes)

---

## Connection to Phonon-Exflation Framework

**Framework-relevant**: The phonon-exflation framework assumes **internal compactification** (M4 x SU(3)) with the SU(3) fiber at sub-Planckian scale ($\sim 0.1$ TeV). This creates an **effective higher-dimensional scenario** where:

1. **Kaluza-Klein reduction** produces 4D particles from 5D/6D/7D bulk fields
2. **Black holes on the internal space** (topological defects in the SU(3) sector) would experience the higher-dimensional physics analyzed here
3. **Event horizon topology** on the internal manifold is a key mechanism for pair creation and instanton tunneling

The Andrade et al. result suggests that **WCC violations at higher-D scales may seed particle creation**: if the internal geometry permits naked singularities (even transiently), this could trigger the **instanton cascade** that phonon-exflation uses to generate the Standard Model fermion spectrum.

Additionally, the **loss of determinism** from naked singularities is precisely the kind of "information leakage" that phonon-exflation's GGE (Generalized Gibbs Ensemble) permanence is designed to handle: the relic state after cosmological transition retains information (via integrability and conserved charges) even though local spacetime determinism is lost at sub-Planckian scales.

**Closest connection**: Kaluza-Klein black hole physics and the role of extra-dimensional horizons in enabling singularity formation without evaporation.

---

## References

- Andrade, T., et al. (2022). "Evidence for violations of weak cosmic censorship in black hole collisions in higher dimensions." *JHEP* 03:111.
- Gregory, R., Laflamme, R. (1993). "Black strings and p-branes are unstable." *Phys. Rev. Lett.* 70:2837.
- Giesler, M., et al. (2023). "Rapid ringdown of black holes with higher angular momentum." *Phys. Rev. Lett.* 130:081401.
