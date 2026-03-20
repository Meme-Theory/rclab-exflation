# Gate-controlled BCS-BEC Crossover in a Two-dimensional Superconductor

**Author(s):** Yuji Nakagawa, Yuichi Kasahara, Takuya Nomoto, Ryotaro Arita, Tsutomu Nojima, Yoshihiro Iwasa

**Year:** 2021

**Journal:** Science, vol. 372, article 190

---

## Abstract

The BCS-BEC crossover is experimentally realized in a two-dimensional superconductor (electron-doped zirconium nitride chloride) by tuning the carrier density via ionic gating. The phase diagram, measured simultaneously with resistivity and tunneling spectroscopy under varying gate voltages, reveals a pseudogap phase at low carrier density. The ratio of the superconducting transition temperature to the Fermi temperature in the low-carrier-density limit is consistent with the theoretical upper bound predicted by BCS-BEC crossover theory. This work provides the first direct experimental confirmation of the complete crossover from BCS pairing (weak coupling, large coherence length) to BEC condensation (strong coupling, small coherence length) in a pure, well-defined two-dimensional system.

---

## Historical Context

The BCS-BEC crossover is a fundamental concept in quantum many-body physics, originally developed by Leggett (1980) as a theoretical possibility—a smooth evolution of a fermionic superfluid from the weak-coupling regime (BCS), where Cooper pairs form with large size and large number of particles in the gap, to the strong-coupling regime (BEC), where pairs become tightly bound molecules. For decades, this crossover remained inaccessible experimentally because materials rarely allow systematic tuning across the entire crossover regime.

The breakthrough came in cold-atom physics (Hulet et al., 2003; Ketterle group, 2004-2005), where ultracold Fermi gases allowed experimental realization of the complete crossover by tuning the s-wave scattering length via Feshbach resonances. However, condensed-matter systems—the original motivation for Leggett's work—proved more difficult. Most superconductors operate in the BCS limit or only marginally approach the crossover.

Nakagawa et al.'s work is groundbreaking because it:

1. Realizes the crossover in a **solid-state system** (not cold atoms), proving the physics is material-independent
2. Uses **ionic gating** (not Feshbach resonances), a technique applicable to many materials
3. Measures **both the pairing mechanism and thermodynamics** simultaneously (tunneling spectra + resistivity)
4. Provides **quantitative agreement** with theoretical predictions

The material (electron-doped ZrNCl) is a van der Waals-bonded layered compound with intrinsic 2D superconductivity, making it ideal for this study.

---

## Key Arguments and Derivations

### BCS-BEC Crossover Parameter

The crossover is controlled by the dimensionless interaction parameter:

$$\frac{1}{k_F a_s} = \frac{m}{4\pi \hbar^2 k_F a_s}$$

where $k_F$ is the Fermi wavenumber, $a_s$ is the s-wave scattering length, and $m$ is the electron mass. In 2D, the scattering length is related to the 2D binding energy via:

$$|E_b| = \frac{\hbar^2}{2m a_s^2}$$

The crossover occurs at $1/(k_F a_s) = 0$ (Feshbach resonance), with BCS regime at $1/(k_F a_s) \to -\infty$ (attractive interaction, large scattering length) and BEC regime at $1/(k_F a_s) \to +\infty$ (repulsive interaction, small scattering length, tightly bound pairs).

### Carrier Density Tuning

In ZrNCl, the carrier density is tuned via electrochemical ion intercalation:

$$n = e N_{\text{ions}} / A$$

where $N_{\text{ions}}$ is the number of intercalated lithium ions and $A$ is the sample area. This directly controls the Fermi level $E_F = \hbar^2 k_F^2 / (2m)$. For a 2D system with quadratic dispersion:

$$k_F = \sqrt{2\pi n}$$

By varying the intercalation level from $n = 0$ (undoped) to $n \sim 10^{14}$ cm$^{-2}$ (heavily doped), the authors span more than one order of magnitude in $k_F$.

### Superconducting Transition Temperature

In the BCS regime, $T_c$ is exponentially suppressed:

$$T_c^{\text{BCS}} \propto E_D \exp\left(-\frac{1}{\lambda N(E_F)}\right)$$

where $\lambda$ is the electron-phonon (or electron-magnon) coupling strength. As the system approaches the crossover ($1/(k_F a_s) \to 0^-$), $T_c$ increases dramatically. In the BEC limit, $T_c$ saturates at:

$$T_c^{\text{BEC}} \sim \frac{1}{3} E_b$$

where $E_b = \hbar^2/(2m a_s^2)$ is the molecular binding energy. The authors find that at the lowest densities (BEC limit), $T_c / E_F$ reaches the theoretical bound $\sim 0.2-0.3$.

### Pseudogap and Tunneling Spectroscopy

Tunneling spectroscopy (differential conductance $dI/dV$) directly probes the quasiparticle density of states:

$$N(\omega) = \int d^2k \, \rho_\mathbf{k}(\omega)$$

In the BCS regime, $N(\omega)$ shows a single gap $\Delta$ above which states are sparse. In the pseudogap regime (just above $T_c$), a suppression of states persists above $T_c$ due to pairing fluctuations:

$$N(\omega, T > T_c) \sim N_0 \left[1 - \frac{|\Delta_{\text{pg}}(\omega, T)|^2}{\omega^2 + (\text{damping})^2}\right]$$

The pseudogap $\Delta_{\text{pg}}$ decreases as $T$ increases above $T_c$ but remains visible up to a characteristic temperature $T^*$. In the low-density regime, $T^* / T_c$ becomes large (approaching 1 in the BEC limit), indicating strong pairing fluctuations—the hallmark of the crossover.

### Quantum Critical Point Hypothesis

The authors argue that the crossover center (Feshbach resonance, $1/(k_F a_s) = 0$) may be a quantum critical point (QCP). At a QCP, observables exhibit non-Fermi-liquid scaling:

$$\sigma(\omega) \sim \omega^\beta, \quad C(T) \sim T^\alpha$$

However, near the crossover, they find Fermi-liquid-like behavior persists, suggesting the crossover is smooth (not a true QCP) or that quantum criticality is masked by finite-size effects.

---

## Key Results

1. **Complete Crossover Realization** — The carrier-density tuning spans the entire BCS-BEC crossover in a single material, from $1/(k_F a_s) \approx -2$ (BCS) to $+2$ (BEC-like).

2. **Phase Diagram Mapping** — Simultaneous measurement of $T_c$ and pseudogap temperature $T^*$ reveals that the ratio $T^* / T_c$ grows from $\sim 1.2$ (BCS) to $\sim 2-3$ (BEC), indicating increasing pairing fluctuations.

3. **Tunneling Spectroscopy Evidence** — Quasiparticle spectra transition from a single sharp gap (BCS) to a broader, softer suppression (BEC-like), consistent with a crossover from fermionic to molecular excitations.

4. **Theoretical Upper Bound Achieved** — In the low-density limit, $T_c / E_F$ reaches $\sim 0.2$, matching the theoretical prediction for the BEC limit where $T_c / E_F \sim (1/3) E_b / E_F$.

5. **No First-Order Transition** — The crossover is smooth, with no discontinuities in any measured observable, confirming the absence of a true phase transition within the crossover.

6. **Gate-Tunable Superconductivity** — The reversibility and reproducibility of the tuning demonstrate that ionic gating is a powerful tool for exploring crossover phenomena in condensed matter.

---

## Impact and Legacy

This landmark experimental work validated decades of theoretical BCS-BEC crossover theory by providing the first systematic, complete realization in a condensed-matter system. It has motivated:

- Theoretical refinements of BCS-BEC physics in 2D systems
- Development of new 2D materials amenable to similar gate-tuning studies
- Renewed interest in understanding the quantum critical point at the crossover center
- Applications to understanding exotic superconductivity in other layered materials

The work has been cited extensively in both condensed-matter and ultracold-atom communities, bridging the two fields.

---

## Framework Relevance

**Density-Tuning Analog**: Nakagawa et al. vary carrier density to sweep the BCS-BEC crossover. The framework's control parameter is the fold coordinate $\tau$, which varies the SU(3) geometry and thereby the Dirac spectrum. Both processes tune the pairing physics from weak (BCS) to strong coupling (BEC-like) regimes.

**2D Superconductivity**: ZrNCl is intrinsically 2D. The framework's BCS mechanism occurs in the 0D limit ($L/\xi_{GL} = 0.031$, Session 38), even more confined than 2D. The present work's finite-size effects should be even stronger in the framework—a regime where quantum fluctuations dominate completely.

**Pseudogap and Pairing Fluctuations**: Nakagawa et al. observe a pseudogap that persists above $T_c$, growing stronger in the BEC-like regime. The framework predicts no Goldstone mode above the fold (Session 35: NG mode ceases). This is consistent with the observation that the BEC-like regime has no true long-range order (only molecular-like pairing), paralleling the framework's absence of a symmetry-breaking phase transition at the fold.

**$T_c$ Enhancement from van Hove Singularities**: The framework places the Dirac sea at a van Hove singularity at the fold (Session 35). Nakagawa et al.'s observation that $T_c$ enhancement is most dramatic in the low-density, low-$N(E_F)$ limit (BEC regime) suggests that high density of states is NOT the only path to strong pairing. Rather, the BEC physics itself (tightly bound pairs, high binding energy) replaces the weak-coupling enhancement. The framework's off-Jensen BCS (Session 35, Session 40) operates in this "anomalous" regime where weak bare coupling yields strong effective pairing—analogous to a BEC-like phase born from Dirac-sea topology.

---

## References

- Nakagawa, Y., Kasahara, Y., Nomoto, T., Arita, R., Nojima, T., & Iwasa, Y. (2021). Gate-controlled BCS-BEC crossover in a two-dimensional superconductor. *Science*, 372(6538), 190-195.
- Leggett, A. J. (1980). Cooper instability of "normal" metals at T = 0. *Physical Review B*, 14(9), 3503-3507.
- Hulet, R. G., et al. (2003). Observation of Feshbach resonances in a Bose-Einstein condensate. *Nature*, 426, 537-540.
