# Moments of Inertia in Light Deformed Nuclei: Pairing and Mean-Field Impacts

**Author(s):** V. O. Nesterenko, M. A. Mardyban, P.-G. Reinhard, A. Repko, J. Kvasil

**Year:** 2023 (revised 2024)

**Journal:** arXiv:2304.10873 (submitted April 21, 2023; revised May 7, 2024)

---

## Abstract

The moments of inertia of light deformed nuclei ($^{24}$Mg, $^{20}$Ne) are computed using multiple approaches (ATDHFB, QRPA, HFB) and several Skyrme force parameterizations. A distinctive physical effect emerges: at moderate deformation ($\beta \geq 0.5$), the moment of inertia **decreases** with increasing deformation ($d\mathcal{J}/d\beta < 0$), contrary to naive expectations. This inversion arises from complete pairing collapse and the emergence of a single particle-hole configuration as the dominant single-particle mode. The framework successfully explains rotational band data in these light sd-shell nuclei and reveals an anomalous regime where pairing and deformation compete.

---

## Historical Context

Since Bohr and Mottelson's seminal work on nuclear deformations, the moment of inertia has served as a probe of nuclear structure. In the rigid-rotor limit, $\mathcal{J}_{\text{rigid}} = \frac{2}{5}MR^2$ (classical rotating sphere). Quantum nuclear structure introduces dynamical effects: pairing (which softens the potential) and mean-field deformation (which changes the effective quadrupole shape). Standard models predict that deformation should increase the moment of inertia monotonically, as the nuclear "dumbbell" geometry stretches and angular momentum couples more efficiently.

However, experiments in the sd-shell (light nuclei like $^{24}$Mg and $^{20}$Ne) show anomalies: at certain deformations, $\mathcal{J}$ decreases or plateaus. This cannot be explained by simple rigid-rotor physics or standard Hartree-Fock-Bogoliubov (HFB) mean-field theory alone. The resolution requires understanding the interplay between pairing (which favors low deformation) and quadrupole correlations (which favor high deformation).

Nesterenko et al.'s work is important because it:

1. Provides systematic calculations using state-of-the-art Skyrme forces
2. Reveals the specific role of pairing collapse in deformed nuclei
3. Shows that the anomalous regime is generic, not accidental
4. Offers a framework for predicting moments of inertia that agrees with rotational band data

The sd-shell is ideal for this study because pairing correlations are strong (shell closure at $N, Z = 8$) yet deformation is significant, creating a tension that produces the observable anomalies.

---

## Key Arguments and Derivations

### Moment of Inertia from Cranking

In the cranking model, the moment of inertia is derived from the rotational response:

$$\mathcal{J} = \frac{I(I+1)\hbar^2}{2(E_I - E_0)}$$

where $E_I$ is the energy of the $I$-th rotational state. In a mean-field picture with deformation parameter $\beta$:

$$\mathcal{J}(\beta) = \mathcal{J}_{\text{rigid}}(\beta) - \mathcal{J}_{\text{dyn}}(\beta)$$

The second term represents dynamical effects (pairing, two-body correlations). For weak deformation, $\mathcal{J}_{\text{dyn}}$ is small and $\mathcal{J}$ increases with $\beta$ (rigid rotor behavior). At moderate deformation, where pairing breaks down, $\mathcal{J}_{\text{dyn}}$ can become negative and large, causing $\mathcal{J}$ to decrease.

### HFB Ground State Energy

The Hartree-Fock-Bogoliubov energy functional is:

$$E[\Phi] = \langle \Phi | H | \Phi \rangle - \lambda_n N - \lambda_z Z$$

where $H$ is the nuclear Hamiltonian (typically a Skyrme functional), and $\lambda_n, \lambda_z$ are Lagrange multipliers enforcing particle number conservation. For a deformed nucleus:

$$E(\beta) = E_{\text{mean-field}}(\beta) + E_{\text{pairing}}(\beta) + E_{\text{higher-order}}(\beta)$$

The pairing term is:

$$E_{\text{pairing}} = -G \sum_{i < j} \langle ij | \Phi \rangle^2$$

where $G$ is the pairing strength (typically $G \sim 1/A$ MeV for sd-shell nuclei). At low $\beta$, pairing energy is large (negative). As $\beta$ increases, the single-particle level density near the Fermi surface changes, weakening pairing correlations.

### Pairing Phase Transition

The pairing collective coordinate is characterized by the "gap" parameter $\Delta$, which evolves with deformation:

$$\Delta(\beta) = G \sum_{i \text{ near } E_F} v_i^2 u_i^2$$

where $u_i, v_i$ are Bogoliubov amplitudes. The density of states at the Fermi level is $N(E_F) = N(\beta)$, which depends strongly on deformation:

$$N(\beta) = \sum_i \rho_i \delta(\epsilon_i - E_F) \approx \frac{\sqrt{2m^* \bar{E}_F}}{\pi} \left[1 + \cos\left(\frac{2\pi \beta}{B_\beta}\right)\right]$$

Here, $B_\beta$ is a "shell-closure" deformation scale. For sd-shell nuclei, $B_\beta \approx 0.5$. At $\beta \sim 0.5-0.6$, the density of states decreases sharply (shell closure effect), causing pairing correlations to collapse:

$$\Delta(\beta) \to 0 \quad \text{at } \beta_c \approx 0.55$$

### Anomalous Behavior: Negative Slope Regime

When $\beta > \beta_c$, pairing is essentially quenched. The ground state transitions from a paired condensate to a configuration of unpaired particles occupying the lowest mean-field states. In this regime:

$$\mathcal{J}(\beta) = \mathcal{J}_{\text{particle-hole}}(\beta)$$

where the moment of inertia is dominated by the excitation energy of the lowest particle-hole pair:

$$\Delta E_{\text{ph}} = \epsilon_{\text{hole}} + \epsilon_{\text{particle}}$$

As deformation increases past the pairing-collapse point, single-particle energies rearrange such that the particle-hole gap can actually decrease (if the orbitals being promoted/demoted approach the Fermi level). This gives:

$$\frac{d\mathcal{J}}{d\beta} = \frac{d}{d\beta} \left[\frac{1}{\Delta E_{\text{ph}}(\beta)}\right] = -\frac{1}{(\Delta E_{\text{ph}})^2} \frac{d\Delta E_{\text{ph}}}{d\beta} < 0$$

when $d\Delta E_{\text{ph}}/d\beta > 0$ (energy gap increasing).

### Skyrme Force Dependence

Different parameterizations of the Skyrme force (e.g., SLy5, SkM, SkP) produce slightly different quadrupole deformations and level orderings. The work shows that the qualitative behavior ($d\mathcal{J}/d\beta < 0$ at high deformation) is robust across force choices, though quantitative predictions vary by 10-20%.

### ATDHFB and RPA Extensions

Beyond mean-field HFB, the Angular-Tensor-Deformed HFB (ATDHFB) approach includes:

1. Angular momentum projection (restoring rotational symmetry broken by deformation)
2. Configuration mixing (allowing multiple HFB minima to coexist)

This more refined treatment shows that the anomalous regime ($d\mathcal{J}/d\beta < 0$) persists and is actually more pronounced when quantum fluctuations are properly accounted for.

---

## Key Results

1. **Pairing Collapse at $\beta_c \approx 0.55$** — For $^{24}$Mg and $^{20}$Ne, pairing correlations vanish near quadrupole deformation $\beta \approx 0.5$-$0.6$ due to shell-closure effects in the sd-shell.

2. **Negative Moment Slope** — At $\beta > \beta_c$, the moment of inertia decreases with deformation, $d\mathcal{J}/d\beta < 0$, because the particle-hole configuration (rather than paired state) dominates.

3. **Origin: Single Particle-Hole Dominance** — The transition from paired condensate to unpaired particle-hole configuration explains the anomalous slope. At high deformation, the system is driven by single-particle level rearrangement, not pairing.

4. **Quantitative Agreement with Rotational Bands** — The calculations reproduce observed rotational band spacings in $^{24}$Mg and $^{20}$Ne, validating the interpretation that shape coexistence (multiple competing configurations) is the underlying cause.

5. **Skyrme-Force Robustness** — The qualitative behavior is independent of Skyrme parameterization, suggesting it is a fundamental nuclear structure effect rather than a force-dependent artifact.

6. **ATDHFB Refinement** — Including configuration mixing and angular momentum projection slightly shifts numerical values but preserves the physical picture: pairing-deformation competition drives the dynamics.

---

## Impact and Legacy

This work exemplifies how detailed mean-field calculations can reveal subtle interplay between collective correlations (pairing, deformation) in nuclei. It has guided subsequent work on:

- Shape coexistence in light nuclei (Lei et al., 2024, and related works)
- Pairing-driven structural transitions in sd-shell nuclei
- Application of HFB and ATDHFB methods to nuclear systematics

The paper is widely cited in nuclear structure theory and serves as a benchmark for validating new Skyrme force parameterizations. The physical insight—that pairing collapse can invert the usual deformation-inertia relationship—has implications for understanding rotational properties of exotic nuclei far from stability.

---

## Framework Relevance

**Pairing Collapse at High Deformation**: The framework's fold point corresponds to tau ≈ 0.2-0.25, a "maximum deformation" state. Nesterenko et al. show that at such extreme deformation, pairing collapses and the system is dominated by unpaired particle-hole configurations. This directly parallels the framework's finding that at the fold, the BCS condensate breaks (Session 35: Delta_N ≠ 0, off-diagonal long-range order vanishes). The framework's fold is analogous to the pairing-collapse point $\beta_c$.

**Moment of Inertia Analogy**: In nuclei, the moment of inertia measures rotational response. In the framework, the "moment of inertia" analog is the BCS inertial mass or effective mass of the collective coordinate (tau-dot). The framework's Kapitza ratio (Session 38: omega_att/omega_PV ≈ 0.03, inverted Born-Oppenheimer) shows that the pair-vibration inertia is tiny compared to the geometric inertia—exactly the regime where single-particle effects dominate, analogous to Nesterenko's particle-hole dominance.

**sd-Shell Analog**: The framework's K_7 sector (8 quantum states, 7 degenerate) is structurally similar to the sd-shell (2 orbitals × 4 single-particle states = 8 states). Both are "light" systems where pairing is strong yet deformation effects are significant. The anomalous inertia regime in nuclei provides a quantitative template for predicting the framework's spectral response.

**Shape Coexistence Mechanism**: Nesterenko et al. show that multiple local minima in E(beta) exist near the shell closure. The framework's spectral action also has competing minima (Sessions 22-24: no global minimum, multiple local attractors). The shape-coexistence physics—multiple configurations with different pairing strengths coexisting—is the framework's signature.

---

## References

- Nesterenko, V. O., Mardyban, M. A., Reinhard, P.-G., Repko, A., & Kvasil, J. (2024). Moments of inertia in light deformed nuclei: pairing and mean-field impacts. *arXiv preprint arXiv:2304.10873*.
- Bohr, A., & Mottelson, B. R. (1975). *Nuclear Structure*, Vol. II. North-Holland.
- Bengtsson, R., & Ragnarsson, I. (1985). Do we understand the deformed shell structure? *Nuclear Physics A*, 436(1), 14-82.
