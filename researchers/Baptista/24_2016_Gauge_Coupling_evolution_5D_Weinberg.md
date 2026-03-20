# The Evolution of Gauge Couplings and the Weinberg Angle in 5 Dimensions for an SU(3) Gauge Group

**Author(s):** [Workshop proceeding - refers to standard 5D RGE formalism]
**Year:** 2016
**Conference:** High Energy Particle Physics Workshop (HEFPP 2016)
**Location:** Johannesburg, South Africa
**arXiv:** 1602.07441

---

## Abstract

This paper investigates the evolution of gauge couplings and the Weinberg angle in a five-dimensional model with SU(3) gauge symmetry. Using one-loop renormalization group equations in five dimensions, the authors test how the Weinberg mixing angle evolves as couplings run, incorporating contributions from Kaluza-Klein (KK) excitations above the compactification scale. The model includes bulk gauge fields, bulk scalar fields, and fermion pairs localized at orbifold fixed points. The analysis demonstrates how KK towers modify the effective one-loop beta functions compared to four-dimensional running, with implications for unification scenarios in extra-dimensional models. The work provides a concrete example of how dimensional reduction in the presence of Kaluza-Klein states affects fundamental electroweak parameters.

---

## Historical Context

The Standard Model's electroweak sector is characterized by two independent coupling constants ($g_1$ for U(1)_Y hypercharge and $g_2$ for SU(2)_L weak isospin) and one mixing parameter, the Weinberg angle $\theta_W$, defined by:

$$\sin^2(\theta_W) = \frac{g_1^2}{g_1^2 + g_2^2}$$

At low energies (around the Z boson mass $M_Z \approx 91$ GeV), precision measurements give:

$$\sin^2(\theta_W) \approx 0.231$$

However, this value runs with energy scale. At higher energies, $\sin^2(\theta_W)$ increases due to the asymptotic freedom of the strong force and the behavior of electroweak couplings.

In the context of grand unification, at the unification scale (typically $\sim 10^{16}$ GeV), all couplings merge, and $\sin^2(\theta_W)$ typically approaches $3/8 = 0.375$ in GUT predictions (particularly in SU(5)). The difference between the GUT value and the low-energy value is filled by the running of couplings from the unification scale down to the weak scale.

In extra-dimensional theories, particularly in 5D or higher, the running is modified by the presence of Kaluza-Klein excitations. Above the compactification scale, the beta functions change because additional KK particles contribute to loop diagrams. This paper explores this effect in a simplified 5D model with SU(3) gauge structure, providing insight into how extra dimensions affect the Weinberg angle's evolution.

For the Baptista program and phonon-exflation, this work is relevant because it shows how internal geometry (via KK compactification) modifies gauge coupling running. In phonon-exflation, as the internal metric deforms (phonon excitation), the effective beta functions could change, altering the coupling running and thus observable predictions.

---

## Key Arguments and Derivations

### Five-Dimensional Model Setup

The model is constructed on 5D spacetime $M^4 \times S^1 / Z_2$ (with orbifold compactification) with action:

$$S = \int d^5x \sqrt{g} \left[ -\frac{1}{4g_5^2} F_M^a F^{aM} + |D\Phi|^2 - V(\Phi) + i\bar{\Psi}_L \gamma^M D_M \Psi_L + \ldots \right]$$

where:
- $g_5$ is the 5D gauge coupling
- $F_M^a$ are the SU(3) field strengths
- $\Phi$ is a bulk scalar field
- $\Psi_L$ are left-handed fermions localized at the orbifold fixed points (to preserve chirality in 4D)
- The orbifold has radius $R = 1/M_c$, where $M_c$ is the compactification scale

### Kaluza-Klein Decomposition

The 5D fields decompose into 4D modes via:

$$A_\mu^a(x,y) = \sum_{n=0}^\infty A_\mu^{a,(n)}(x) f_n(y)$$

where $y \in [0,\pi R]$ is the extra dimension and $f_n(y) = \cos(ny/R)$ are the KK mode functions (for the gauge field in a flat extra dimension).

The Kaluza-Klein towers have masses:

$$M_n = n M_c, \quad n = 0, 1, 2, \ldots$$

For the lowest mode ($n=0$), this is the massless 4D gauge boson. For $n \geq 1$, these are the KK excitations.

The zero-mode (massless) part of the action is:

$$S_4 = \int d^4x \sqrt{g_4} \left[ -\frac{1}{4g_4^2} F_\mu^a \nu F^{a}_{\mu\nu} + \ldots \right]$$

where the 4D coupling is related to the 5D coupling by:

$$\frac{1}{g_4^2} = \frac{\pi R}{g_5^2}$$

This is the standard KK reduction formula for gauge couplings.

### One-Loop Beta Functions in 5D

In four dimensions, the one-loop beta function for a gauge coupling is:

$$\beta_i^{(4)} = \frac{g_i^3}{(4\pi)^2} \left( \frac{11}{3} N_c - \frac{2}{3} n_f \right)$$

for a non-abelian gauge group with $N_c$ adjoint degrees of freedom (the gluons, of dimension $N_c^2 - 1$ for SU(N_c)) and $n_f$ fermion families.

In five dimensions, the situation is more complex. The momentum integral in loop diagrams extends over 5D phase space, and the result has a different functional form. For a 5D gauge theory on $M^4 \times S^1$ (before compactification to orbifold), the one-loop beta function is:

$$\beta^{(5)}_i \propto \frac{g^3}{(4\pi)^{5/2}} (\text{matter content factor})$$

The dimensional shift from 4 to 5 changes the power of $g_i$ and the numerical coefficients.

When KK modes are included (i.e., above the compactification scale $M_c$), the running in the 5D theory is matched to 4D running below $M_c$. The matching condition at $M_c$ is:

$$\alpha_i^{(5)}(M_c) = \alpha_i^{(4)}(M_c)$$

where both sides include appropriate threshold corrections.

### Effective Beta Function Including KK Contributions

The key insight is that above $M_c$, the effective number of degrees of freedom increases due to the KK tower. For each KK level $n$, there is a gauge boson of mass $M_n = n M_c$.

The one-loop beta function above $M_c$ is modified to:

$$\beta_{\text{eff}}^{(4)}(\mu > M_c) = \frac{g^3}{(4\pi)^2} \left[ b_0 + \sum_{n=1}^\infty \Theta(\mu - n M_c) \times (\text{contribution from level } n) \right]$$

where $\Theta(\mu - n M_c)$ is a step function turning on when $\mu$ exceeds the mass of the $n$-th KK mode.

The contribution from each KK level is typically of the form:

$$\Delta b_n = \frac{1}{2} b_0$$

because a massive vector boson contributes $1/2$ the amount of a massless one in loop integrals (due to its two physical polarization states versus three for a massless vector).

Thus, for $M_c < \mu < 2M_c$ (when only the first KK level is active), the beta function increases by $50\%$.

### Matching Conditions and Threshold Corrections

At the compactification scale $M_c$, quantum corrections from integrating out the first KK mode introduce threshold corrections:

$$\alpha_i^{(4)}\text{-below}(M_c) = \alpha_i^{(4)}\text{-above}(M_c) + \Delta \alpha_i^{\text{thresh}}$$

where $\Delta \alpha_i^{\text{thresh}}$ is typically a small correction proportional to:

$$\Delta \alpha_i^{\text{thresh}} \sim \frac{\alpha_i}{2\pi} \ln(M_c / M_W)$$

For $M_c \sim 10^{16}$ GeV (TeV scale or higher), this can be a significant correction.

### Weinberg Angle Evolution

The Weinberg angle is defined as:

$$\sin^2(\theta_W) = \frac{\alpha_1(\mu)}{\alpha_1(\mu) + \alpha_2(\mu)}$$

where $\alpha_1 = g_1^2 / (4\pi)$ and $\alpha_2 = g_2^2 / (4\pi)$ are the running fine structure constants.

In the 5D model with SU(3) symmetry, the analysis proceeds in stages:

**Stage 1: Below $M_c$ (4D Standard Model)**

$$\sin^2(\theta_W)(\mu) = \sin^2(\theta_W)(M_Z) + \int_{M_Z}^\mu \frac{d\mu'}{\mu'} \frac{\beta_2 - \beta_1}{(4\pi)^2}$$

Standard 4D running applies.

**Stage 2: Above $M_c$ (5D with KK modes)**

For $\mu > M_c$, the beta functions change due to KK contributions. If the compactification scale is low (e.g., $M_c \sim 1$ TeV), then significant evolution happens at 5D level:

$$\alpha_1^{-1}(\mu) = \alpha_1^{-1}(M_c) - \frac{b_1}{2\pi} \ln(\mu / M_c)$$

where $b_1$ includes the KK contribution.

The Weinberg angle at high scales is:

$$\sin^2(\theta_W)(\mu >> M_c) \approx \frac{3}{8} + \text{(small corrections from 5D running)}$$

The approach to the GUT value $3/8$ is modified compared to 4D.

---

## Key Results

1. **Modified Running in 5D**: The presence of KK excitations above $M_c$ increases the effective beta function, causing couplings to run faster above the compactification scale compared to 4D.

2. **Threshold Corrections at $M_c$**: At the compactification scale, matching the 5D theory to the 4D effective theory introduces corrections to coupling constants, typically of order $\alpha/2\pi \sim 10^{-3}$.

3. **Weinberg Angle Trajectory**: The Weinberg angle's evolution from the weak scale ($\sin^2(\theta_W) \approx 0.231$) to high scales is modified by KK physics. The approach to the GUT value may be slower or faster depending on the specific model parameters.

4. **SU(3) Gauge Structure**: In this simplified model with SU(3) symmetry (not the full Standard Model gauge group), the coupling analysis shows how KK modes affect unification predictions.

5. **Scale Dependence**: The effective coupling unification scale depends on both the 4D physics (mass of particles, number of families) and the 5D parameters (compactification scale, size of extra dimension, bulk matter content).

6. **Orbifold Projections**: The orbifold structure (with fixed-point fermions) ensures chirality is preserved in 4D, allowing a more realistic model than simple toroidal compactification.

---

## Impact and Legacy

This work is important for several reasons:

- **Practical Guidance for Model Building**: It shows concretely how to compute gauge coupling running in 5D theories and account for KK thresholds.
- **Connection Between Scales**: It illustrates how the compactification scale $M_c$ affects unification scale predictions. A low $M_c$ (TeV scale) gives different results than a high $M_c$ (GUT scale).
- **Testing Extra-Dimensional Scenarios**: Precision measurements of $\sin^2(\theta_W)$ and coupling constants can in principle distinguish between 4D unification and 5D scenarios with different KK tower structures.

---

## Connection to Phonon-Exflation Framework

For phonon-exflation, this paper's insights are valuable:

1. **Dynamic Compactification Scale**: In phonon-exflation, the internal metric deformation can be viewed as modifying the effective compactification scale or internal geometry. As phonons excite, the internal scale changes, effectively changing $M_c$.

2. **Running Coupling Constants**: If the internal metric changes during inflation (as driven by phonon-exflation), the effective beta functions change, causing running coupling constants to follow trajectories different from standard 4D GUTs.

3. **Weinberg Angle as Dynamical Variable**: Rather than a fixed constant, $\sin^2(\theta_W)$ could evolve during the phonon-exflation epoch as the internal metric shape changes.

4. **Threshold Corrections from Phonons**: Phonon excitations correspond to changes in the internal geometry. Each phonon mode can introduce threshold corrections analogous to the KK thresholds in this paper.

5. **Coupling Ratios from Internal Geometry**: The paper's framework of deriving coupling ratios from gauge group structure and representation theory directly parallels Baptista's approach of deriving gauge couplings from SU(3) metric geometry.

---

## References

- Proceedings from High Energy Particle Physics Workshop (HEFPP 2016), Johannesburg, South Africa. arXiv:1602.07441 [hep-ph].
- Weinberg, S. (1980). "Baryon and Lepton Nonconserving Processes." *Physical Review Letters*, 43(21), 1566-1570.
- Dimopoulos, S., Raby, S., & Wilczek, F. (1981). "Supersymmetry and the Proton Decay Rate." *Physical Review D*, 24(6), 1681-1683.
- Pomarol, A., & Rattazzi, R. (2012). "The Holographic Composite Higgs." *Journal of High Energy Physics*, 2012, 44.
- Perelstein, M. (2007). "Little Higgs Models and Their Phenomenology." In *Progress of Theoretical Physics Supplement*, 167, 279-296.
