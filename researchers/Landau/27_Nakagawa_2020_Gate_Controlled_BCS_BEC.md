# Gate-controlled BCS-BEC crossover in a two-dimensional superconductor

**Author(s):** Yuji Nakagawa, Yuichi Kasahara, Takuya Nomoto, Ryotaro Arita, Tsutomu Nojima, Yoshihiro Iwasa
**Year:** 2020
**Journal:** Science (based on format and supplementary structure)
**arXiv:** 2012.05707
**Relevance:** MEDIUM

---

## Abstract

The Bardeen-Cooper-Schrieffer (BCS) condensation and the Bose-Einstein condensation (BEC) are the two extreme limits of the ground state of the paired fermion systems. We report crossover behavior from the BCS condensation to the BEC realized in the two-dimensional (2D) superconductor, electron doped layered material ZrNCl. The phase diagram, established by simultaneous experiments of resistivity and tunneling spectra under the ionic gating, demonstrates the pseudogap phase at the low doping regime. In the low carrier density limit, $T_{BKT}$ (Berezinskii-Kosterlitz-Thouless transition temperature for 2D superconductors) scales as $T_{BKT}/T_F = 0.12$, where $T_F$ is the Fermi temperature, which is consistent with the theoretical upper bound expected in the BCS-BEC crossover regime. The present results indicate that the gate-doped semiconductor provides an ideal platform for the 2D BCS-BEC crossover without any added complexity, such as magnetic orders and density waves.

---

## Key Arguments and Derivations

### Material and Method

The material Li$_x$ZrNCl is a lithium-intercalated layered nitride where Li supplies electrons to the double honeycomb ZrN layer (a band insulator at $x = 0$). A single conduction band from Zr 4d orbitals hybridized with N 2p orbitals exists at each K and K' point of the hexagonal Brillouin zone. Using an ionic-gating device structure, the Li concentration $x$ can be controlled electrochemically down to $x = 0.0038$, achieving unprecedented control of carrier density in a superconductor.

### Dimensional Crossover

A unique feature is a dimensional crossover from anisotropic 3D to 2D superconductivity upon reducing carrier density. Due to the rhombohedral stacking, interlayer hopping at the K point becomes exactly zero up to second-nearest-layer coupling by symmetry. As doping decreases and the Fermi surface converges to K, interlayer coupling weakens, and the BKT transition governs the superconducting transition.

The resistive transition is fitted to the Halperin-Nelson equation:
$$\rho(T) = a\rho_N \exp\left[-2\left\{\frac{b(T_c' - T)}{T - T_{BKT}}\right\}^{1/2}\right]$$

### BCS-BEC Crossover Evidence

Three key signatures demonstrate the crossover:

1. **Gap-to-Fermi-energy ratio**: $\Delta/E_F$ increases above 0.3 at low doping, entering the crossover regime. The coupling ratio $2\Delta/k_B T_c$ rises from 3.5 (BCS weak-coupling) to 6.0 at the lowest carrier density.

2. **$T_{BKT}/T_F$ saturation**: In the low carrier density limit, $T_{BKT}/T_F = 0.116$ ($T_c/T_F = 0.121$), approaching the theoretical upper bound of 0.125 for 2D fermion systems in the BCS-BEC crossover regime.

3. **Pseudogap state**: Tunneling spectroscopy reveals a pseudogap phase where pairs form without condensation. At low doping ($x = 0.0066$), $T^*$ is more than twice $T_c$, in contrast to highly doped samples where $T^* \approx T_c$.

### Phase Diagram

The phase diagram shows: $T_c$ peaks at 19.0 K ($x = 0.011$), then decreases at lower doping. The pseudogap region ($T_c < T < T^*$) broadens dramatically at low carrier density. The coherence length $\xi$ continues to decrease even after $T_c$ drops, indicating small, strongly-coupled Cooper pairs.

The $T_c$ decrease below $x = 0.011$ is attributed to the fundamental limitation of $T_c$ scaled by $T_F$ in the BCS-BEC crossover regime, not to disorder effects. The system remains metallic (far from the dirty limit).

## Key Results

1. First demonstration of a 2D BCS-BEC crossover in a solid-state superconductor by scanning doping over nearly two orders of magnitude ($x = 0.28$ to $0.0038$).
2. Record $T_c = 19.0$ K for ZrNCl systems, achieved by reducing (not increasing) the carrier density.
3. $\Delta/E_F > 0.3$ at lowest doping, entering the crossover regime; $1/(k_F\xi) \sim 0.36$ indicates only a few overlapping Cooper pairs.
4. $T_{BKT}/T_F = 0.116$ approaches the theoretical 2D upper bound of 0.125.
5. Pseudogap state observed with $T^*/T_c > 2$ at low doping, attributed to preformed pairs in the BCS-BEC crossover scenario.
6. Dimensional crossover from 3D to 2D driven by rhombohedral stacking symmetry at K point.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| BKT resistivity | $\rho(T) = a\rho_N \exp\left[-2\left\{\frac{b(T_c' - T)}{T - T_{BKT}}\right\}^{1/2}\right]$ | Eq. (1) |
| BKT criterion | $(d\ln\rho/dT)^{-2/3} \propto (T - T_{BKT})$ | Main text |
| 2D GL upper critical field | $\mu_0 H_{c2}^{\parallel}(T) \propto \sqrt{1 - T/T_c}$ | Main text |
| GL coherence length | $\mu_0 H_{c2\perp}(T) = \Phi_0/(2\pi\xi^2)(1 - T/T_c)$ | Main text |
| Crossover criterion | $\Delta/E_F > 0.3$ (BCS-BEC crossover boundary in 2D) | Ref. 20 |
| 2D upper bound | $T_{BKT}/T_F = 0.125$ (theoretical maximum) | Ref. 22 |

## Relevance to Phonon-Exflation

This paper demonstrates BCS-BEC crossover physics in a 2D solid-state system where carrier density (rather than interaction strength) drives the crossover, analogous to how the evolving SU(3) geometry during the fold transit modifies the effective density of states and coupling strength. The observation of a pseudogap phase with preformed pairs above $T_c$ directly parallels the GGE relic state identified in Session 38, where pairs exist without long-range condensate coherence. The 2D BKT physics is also relevant to the framework's treatment of phase transitions on the compactified fiber.
