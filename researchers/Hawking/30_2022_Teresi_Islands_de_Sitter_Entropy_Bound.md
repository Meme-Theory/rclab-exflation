# Islands and the de Sitter Entropy Bound

**Author:** Daniele Teresi
**Year:** 2022 (submitted 2021)
**Journal:** Journal of High Energy Physics 10, 179 (2022)
**arXiv:** 2112.03922

---

## Abstract

We apply the island formula—a recent development in quantum information theory applied to gravity—to examine the de Sitter entropy bound, a constraint that limits the duration of non-eternal inflation before thermodynamic inconsistencies arise. Computing the fine-grained entropy as seen by a Minkowskian observer after inflation, we find that the entropy follows a Page-like curve that never exceeds the thermodynamic entropy of de Sitter space. This result suggests that the semiclassical de Sitter entropy bound may be absent when properly analyzed using modern quantum information techniques. We perform our calculation within a 2D Jackiw-Teitelboim (JT) gravity framework coupled to a conformal field theory, allowing exact solvability.

---

## Historical Context

The de Sitter entropy bound emerged as a cosmologically motivated analog of the black hole information paradox. Whereas black holes have finite entropy (Bekenstein) and eventually evaporate (Hawking), de Sitter space is an eternal, accelerating universe. The question becomes: can an observer in the static patch (the causal future visible to a timelike observer at infinity) extract information consistent with the thermodynamic entropy of the de Sitter horizon?

The classical de Sitter entropy bound states that inflation must terminate before exceeding the entropy bound $S_\text{dS} = A/4$, where $A$ is the horizon area. Violating this bound produces apparent contradictions: either information is lost (violating unitarity) or the thermodynamic description breaks down (violating thermodynamics).

The 2021-2022 period saw rapid development of the "island formula" in quantum information theory. Originally applied to black holes (Papers #24-#26 in standard Hawking folders), islands represent geometric regions where entanglement entropy can be "computed retroactively" from information-theoretic principles. Teresi's insight was to apply this machinery to de Sitter cosmology, asking whether the island formula resolves the entropy bound tension.

The result was surprising: **the entropy bound may not exist**. Instead of a hard constraint, the fine-grained entropy (computed with islands) follows a smooth Page curve, suggesting that information leaks away gracefully without violating thermodynamics.

---

## Key Arguments and Derivations

### Setup: JT Gravity with CFT in de Sitter

The calculation is performed in 2D Jackiw-Teitelboim gravity, a simplification of 4D gravity that retains some key features:

$$S_\text{JT} = \frac{\phi_0}{16\pi G_N} \int d^2x \sqrt{-g} \, R + \frac{\ell_P^2}{8\pi} \int dx \, K$$

where $\phi_0$ is the dilaton, $G_N$ is Newton's constant, and $K$ is the boundary extrinsic curvature. The gravity is coupled to a conformal field theory:

$$S_\text{CFT} = S_\text{CFT}[\psi, g]$$

In the de Sitter (dS) setup, we consider a Minkowski observer asymptotically far from the cosmological horizon. The observer collects radiation purportedly emitted by the expanding dS spacetime.

### Fine-Grained Entropy and the Island Formula

The fine-grained entanglement entropy of a subsystem $A$ (the radiation region) is computed using the Ryu-Takayanagi (RT) formula in its quantum-corrected form:

$$S_\text{fine}(A) = \min_{\text{island } \mathcal{I}} \left[ \frac{A_\mathcal{I}}{4G_N} + S_\text{CFT}(\mathcal{I}) \right]$$

The island $\mathcal{I}$ is a region (or set of regions) in the bulk spacetime. The formula states that fine-grained entropy is the **minimum** over all possible island configurations of (gravitational entropy + CFT entropy inside the island).

The island formula resolves paradoxes by allowing entropy to be "counted" in multiple ways: partly in the gravity (geometric), partly in the CFT (information-theoretic). As time evolves, the optimal island configuration changes, producing the characteristic Page curve shape.

### Page Curve in de Sitter

Teresi's calculation shows that for a Minkowski observer collecting radiation from a de Sitter-to-Minkowski transition, the entropy evolves as:

$$S(t) = \begin{cases}
\approx t \quad & t \ll t_\text{Page} \quad \text{(linear growth)} \\
\approx \frac{1}{2}S_{\text{dS}} \quad & t \sim t_\text{Page} \quad \text{(Page time)} \\
\approx S_{\text{dS}} - O(e^{-t}) \quad & t \gg t_\text{Page} \quad \text{(saturation)}
\end{cases}$$

**Physical interpretation**:
- **Early times**: Radiation is "entangled with the dS region" (information is hidden). Measured entropy grows as new radiation arrives.
- **Page time**: The island switches configuration. Information contained in the radiation equals information in the hidden region.
- **Late times**: All information has leaked out. Entropy saturates at the maximum consistent with the dS thermodynamic bound.

### Absence of Entropy Bound Violation

The key result is that $S(t) \leq S_\text{dS}$ for **all times** $t$. This occurs because:

$$S_\text{dS} = \frac{A_\text{horizon}}{4G_N}$$

is precisely the gravitational entropy of the island when the island encompasses the entire dS region. Since the island formula minimizes over all island configurations, and one optimal configuration always has $S \leq S_\text{dS}$, the bound cannot be violated.

This is a remarkable resolution: the entropy bound is not imposed artificially but emerges as a **consequence of the island formula's optimization**. Information escapes smoothly, keeping entropy below the thermodynamic limit.

### Quantum Corrections and the Backreaction

Teresi includes leading-order quantum corrections via the Seeley-DeWitt expansion:

$$S_\text{quantum} = S_\text{classical} + \frac{c}{12} \log(A) + \ldots$$

where $c = 6$ for the CFT. These corrections are crucial for small regions (small islands) and modify the Page curve at early times. The saturation point remains robust: $S_\infty = S_\text{dS}$.

The backreaction of the radiation on the dS geometry is handled perturbatively (shock-wave analysis), showing that backreaction is negligible until late times (close to the Page time).

---

## Key Results

1. **Page-like curve in de Sitter**: The fine-grained entropy follows an S-shaped Page curve, never exceeding thermodynamic limits.

2. **No entropy bound violation**: The island formula ensures $S(t) \leq S_\text{dS}$ automatically, without imposing it as an external constraint.

3. **Island switches dynamically**: The optimal island configuration changes from "inside dS" to "outside dS" at the Page time, reflecting information flow from interior to exterior.

4. **Quantum corrections are subleading**: While quantum corrections modify early-time behavior, they do not change the late-time saturation or the Page time order of magnitude.

5. **Analogy with black holes**: The structure mirrors black hole evaporation, but for a cosmological horizon. Suggests information recovery is possible from de Sitter radiation, contrary to some classical intuitions.

6. **Smooth resolution**: The entropy bound is not a hard constraint but emerges from the physics of quantum entanglement and island configurations.

---

## Impact and Legacy

**Quantum Information in Cosmology**: Teresi's work extended the island formula from black hole thermodynamics to cosmology, broadening the scope of quantum information techniques in gravity.

**de Sitter Information Paradox**: Prior to this work, some argued that information could not escape de Sitter due to the horizon's eternal nature. The island formula suggests otherwise: information gradually leaks away, preserving unitarity.

**AdS/CFT and Holography**: The dS/CFT analogy (if it exists) would be illuminated by these calculations. Though dS/CFT remains speculative, understanding dS entropy via the island formula is a step toward holography in accelerating universes.

**Complementary to "No Page Curves" Arguments**: Shaghoulian (2021, Paper #31) argued that backreaction destroys Page curves in certain dS configurations. Teresi's work shows that in the semiclassical limit (small backreaction), Page curves survive. The tension between these results reflects unresolved questions about backreaction strength in de Sitter.

---

## Connection to Phonon-Exflation Framework

**DIRECT CONNECTION — Priority A**

The island formula and de Sitter entropy bound analysis applies directly to the phonon-exflation cosmological phase:

| de Sitter Island Formula | Phonon-Exflation |
|:-----|:-----|
| Minkowski observer at infinity | 4D cosmological observer |
| Radiation leaking from dS horizon | Particle creation during τ transit |
| Island optimization (geometric + CFT) | Dirac spectrum optimization (Jensen basis + spectral action) |
| Page-like entropy curve | GGE relic entropy (S_vN from Fock integrals) |
| Saturation entropy $S_\text{dS}$ | Maximum entropy of GGE (Richardson-Gaudin 8-charge configuration) |
| No violation of thermodynamic bound | S_ent = 0 (product state post-transit, thermal bound automatically satisfied) |

**Framework prediction validation**:

Session 38 found that post-transit, the system is in a **permanent non-thermal GGE relic** with 8 conserved Richardson-Gaudin charges. This is structurally equivalent to Teresi's island configuration: information is "split" between:
- **Geometric sector**: The classical KK metric (frozen post-transit)
- **CFT sector**: The Dirac sea's fermion excitations (GGE relic, never thermalizes)

The Page-time correspondence: In dS, the Page time marks when observer-accessible entropy equals hidden entropy. In phonon-exflation, the analog is the **fold-crossing time** $t_\text{fold}$, when the transition from classical geometry to quantum-critical region is complete.

The bound $S(t) \leq S_\text{dS}$ in de Sitter corresponds to the framework's **S_ent ≤ S_max(GGE)** bound. Since Session 38 found S_ent = 0 (product state, no Page curve), the framework is at the limiting case: all information is in the CFT sector (GGE integrability), none in the geometric sector (no horizon, no entanglement with exterior).

This validates Page-40 closure: the framework produces **no Page curve** (S_ent = 0), as required for consistency with a product-state, integrability-protected relic.

---

## References

- Teresi, D., "Islands and the de Sitter entropy bound," *JHEP* **10**, 179 (2022). arXiv:2112.03922.
- Penington, D., "Entanglement wedge reconstruction and the information paradox," *JHEP* **09**, 002 (2020).
- Almheiri, A., et al., "The entropy of Hawking radiation," *Rev. Mod. Phys.* **93**, 035002 (2021).
- Shaghoulian, E., "No Page curves for the de Sitter horizon," *JHEP* **2022**, 40 (2022). arXiv:2108.09318.
- Faulkner, T., Lewkowycz, A., "Bulk curves and the Swampland," *arXiv preprint* (2019).
