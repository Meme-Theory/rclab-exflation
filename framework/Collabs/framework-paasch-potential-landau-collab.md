# Landau Condensed-Matter Theorist -- Collaborative Feedback on framework-paasch-potential

**Author**: Landau Condensed-Matter Theorist
**Date**: 2026-03-06
**Re**: Framework Reframe: Paasch Mass Quantization as Wall-Intersection Physics

---

## Section 1: Key Observations

The document under review proposes a conceptual pivot from "particles as eigenvalue ratios of D_K" to "particles as collective excitations localized at Z_3 domain walls." I assess this reframing through the lens of Landau phase transition theory (Paper 04), Ginzburg-Landau superconductivity (Paper 08), Landau-Lifshitz domain wall solutions (Paper 03), and Fermi liquid quasiparticle theory (Paper 11). The reframe is largely consistent with what condensed matter physics knows about excitations at topological defects, but several claims require careful scrutiny.

### 1.1 The Poschl-Teller Claim

The document asserts (Section 4.1) that a B2 quasiparticle propagating along a tanh-shaped domain wall sees a Poschl-Teller potential:

$$V_{\text{eff}}(x) \approx \lambda_0 + \frac{a_2(\Delta\tau)^2}{8}\tanh^2(x/L_{\text{wall}})$$

This is NOT a Poschl-Teller potential. The Poschl-Teller potential is $V(x) = -V_0/\cosh^2(x/L)$, which is attractive and goes to zero at infinity. What is written above is a potential that starts at $\lambda_0$ and RISES to $\lambda_0 + a_2(\Delta\tau)^2/8$ at large $|x|$. It is a potential WELL, not a potential barrier, and is related to the Poschl-Teller form by the identity $\tanh^2 = 1 - \text{sech}^2$:

$$V_{\text{eff}}(x) = \left[\lambda_0 + \frac{a_2(\Delta\tau)^2}{8}\right] - \frac{a_2(\Delta\tau)^2}{8\cosh^2(x/L_{\text{wall}})}$$

So the claim is correct in substance -- the attractive part IS a Poschl-Teller well with depth $V_0 = a_2(\Delta\tau)^2/8$ -- but the notation in Section 4.1 obscures this, and the later Section 5.2 presents the corrected form. More importantly, this mapping is valid ONLY under the assumption that the B2 eigenvalue at the wall center is at the fold minimum ($d\lambda_{B2}/d\tau = 0$ at the dump point). The fold gives $\lambda_{B2}(\tau) \approx \lambda_0 + (a_2/2)(\tau - \tau_0)^2$, which combined with $\tau(x) = \tau_0 + (\Delta\tau/2)\tanh(x/L)$ yields the stated form. The Poschl-Teller structure is a consequence of the FOLD CATASTROPHE, not a generic feature of domain walls. Without the fold, the effective potential would be asymmetric and not exactly solvable.

The Poschl-Teller potential supports exactly $n$ bound states where $n = \lfloor(1/2)(-1 + \sqrt{1 + 8mV_0 L^2/\hbar^2})\rfloor + 1$. The document's formula in Section 5.2 uses a dimensionless form. What matters physically is the product $V_0 L^2$ in units of $\hbar^2/(2m^*)$, where $m^*$ is the effective mass of the B2 quasiparticle at the fold. This effective mass is $m^* = 1/a_2$ in natural units (from the dispersion $\epsilon = a_2(\tau - \tau_0)^2/2$; this is the INVERSE fold curvature, not the bare mass). The dimensionless parameter governing the number of bound states is then $\lambda_{\text{PT}} = m^* V_0 L^2 = (\Delta\tau)^2 L^2/(8)$, where I used $V_0 = a_2(\Delta\tau)^2/8$ and $m^* = 1/a_2$.

With $\Delta\tau \sim 0.19$ (from the wall excursion $\tau_0 \sim 0.19$ to $\tau \sim 0$) and $L \sim 1.3$--$2.7$ $M_{\text{KK}}^{-1}$: $\lambda_{\text{PT}} \sim (0.19)^2 \times (1.3)^2 / 8 \sim 0.0076$ to $(0.19)^2 \times (2.7)^2 / 8 \sim 0.033$. These values are SMALL. A Poschl-Teller well with $\lambda \ll 1$ supports AT MOST ONE bound state. The PT-count gate (requiring $\geq 3$ bound states) appears likely to fail unless I have misidentified the relevant $\Delta\tau$. If the full wall excursion is $\Delta\tau \sim 0.44$ (from $\tau \sim 0$ to $\tau \sim 0.44$), then $\lambda_{\text{PT}} \sim 0.033$ to $0.14$, still insufficient for three bound states.

This is a testable quantitative prediction, not a qualitative objection. The computation should be performed with the full wall profile from `s33w3_modulus_equation.npz`.

### 1.2 The Z_3 Domain Wall Junction Physics

The mapping of Paasch's six sequences to six oriented Z_3 wall types (three walls with two orientations each) is combinatorially natural. In the Z_3 Potts model, domain walls between the three degenerate ground states are the fundamental topological defects, classified by $\pi_0(Z_3) = Z_3$. The oriented wall types form six objects in three conjugate pairs, matching Paasch's structure.

What condensed matter actually knows about Z_3 Potts domain walls:

1. **In 2D**: The 3-state Potts model has a FIRST-ORDER phase transition for $q > 4$ in mean field, but in 2D the transition is SECOND-ORDER for $q \leq 4$ (Baxter 1973). The $Z_3$ Potts model at its critical point is described by the $W_3$ minimal model CFT with central charge $c = 4/5$. The excitation spectrum of domain walls in the near-critical Potts model has been studied by Delfino and Mussardo (1998) and others. The mass spectrum in the ordered phase contains a rich structure of kink-antikink bound states.

2. **Y-junctions**: When three $Z_3$ walls meet at a point, the junction carries additional energy from the core region where all three phases coexist. This Y-junction energy has been computed for the 3-state Potts model by Hasenbusch and Pinn (1997). The junction angle is 120 degrees by the discrete rotational symmetry, as stated in the document.

3. **Mass ratios**: In the integrable scattering theory of the near-critical Potts model, mass ratios of kink excitations are algebraic numbers determined by the $W_3$ algebra. These are generically NOT related to $\phi_{\text{paasch}} = 1.53158$ or to the golden ratio. The golden ratio appears in the $E_8$ scattering theory (Zamolodchikov 1989), which governs the Ising model in a magnetic field, not the Potts model.

4. **The 45-degree incommensurability**: The document correctly identifies that $45^\circ$ (the Paasch sequence separation) and $120^\circ$ (the $Z_3$ junction angle) are incommensurable. This is a structural obstruction that cannot be resolved by parameter tuning within the Z_3 Potts framework. The document's two proposed resolutions (approximate angle, or junction-energy encoding) are speculative but not ruled out.

### 1.3 The Ratio phi_paasch = L_wall / xi_BCS

This is the most physically substantive claim in the document (Section 3.4). The proposal is that the transcendental equation $x = e^{-x^2}$ arises as the self-consistency condition for the ratio of the domain wall width to the BCS coherence length.

From Ginzburg-Landau theory (Paper 08), the two fundamental length scales are:
- Coherence length: $\xi = \hbar/\sqrt{2m^*|\alpha|}$ (scale of order parameter variation)
- Penetration depth: $\lambda = \sqrt{m^* c^2 \beta/(4\pi e^{*2} |\alpha|)}$ (scale of field variation)

The GL parameter $\kappa = \lambda/\xi$ classifies Type I ($\kappa < 1/\sqrt{2}$) vs Type II ($\kappa > 1/\sqrt{2}$). In the present context, the "penetration depth" analog is the wall width $L_{\text{wall}}$ (the scale over which the modulus field $\tau$ varies), and the coherence length $\xi_{\text{BCS}} = v_{B2}/\Delta$ is the BCS coherence length at the wall. The ratio $L_{\text{wall}}/\xi_{\text{BCS}}$ is the analog of $\kappa$ -- it determines whether the wall is "Type I" (condensate extends beyond the wall, $L < \xi$) or "Type II" (wall is wider than the condensate, $L > \xi$).

The claim that this ratio equals $\phi_{\text{paasch}} \approx 1.53$ would place the system in an intermediate regime between Type I and Type II. In standard GL theory, the ratio $\kappa$ is a material parameter with no self-consistency constraint forcing it to a universal value. The proposed self-consistency equation $x = e^{-x^2}$ would need to arise from a COUPLED system where the wall width depends on the BCS gap (because the condensate energy modifies the modulus potential) AND the BCS gap depends on the wall width (because the wall profile determines the DOS). This mutual dependence is physically real in the phonon-exflation framework, where the modulus field and the BCS order parameter are coupled dynamical variables. Whether the self-consistency reduces to $x = e^{-x^2}$ rather than some other transcendental equation is a quantitative question that requires solving the coupled GL + modulus equations.

I regard the WALL-phi gate as well-posed but the theoretical motivation for obtaining $x = e^{-x^2}$ specifically (rather than some other implicit equation) as weak. The gate will test whether the LENGTH SCALE RATIO matches $\phi_{\text{paasch}}$, which is meaningful regardless of whether the transcendental equation is derived.

### 1.4 The Single-Band BCS Constraint

The document correctly inherits from Session 33: Trap 4 (Schur orthogonality) and Trap 5 (J-reality) force BCS condensation exclusively in the B2 channel. $\Delta_{B1} = \Delta_{B3} = 0$ exactly. This is permanent mathematics (my Session 32 collab, Section 1.4; Paper 11 Fermi liquid selection rule analog).

The consequence for wall-localized excitations is important. In standard BCS, Andreev bound states at a normal-superconductor interface involve ALL bands that participate in the condensate. Here, only B2 modes are gapped. B1 and B3 remain gapless (or rather, they retain their bare D_K gap from the spectral geometry but have no BCS gap). At a domain wall between two Z_3 BCS vacua, the Andreev reflection occurs only for B2 quasiparticles. B1 and B3 modes pass through the wall without Andreev reflection -- they see no phase difference across the wall.

This means the wall-localized spectrum is SOLELY determined by B2 physics. The "six sequences" in the Paasch mapping must all arise from the 4-fold B2 multiplet (U(2) fundamental), not from B1 or B3 contributions. Whether 4 degrees of freedom can produce 6 sequences is a counting question the document does not address.

### 1.5 The "Particles Live at Walls" Claim

The document's central thesis -- that particles are not bulk eigenvalues but wall-localized collective excitations -- is physically well-motivated in the condensed matter context. Several established examples:

1. **Andreev bound states**: At an N-S interface, quasiparticles undergo retroreflection (electron -> hole and vice versa), forming bound states localized within $\xi_{\text{BCS}}$ of the interface. The bound state energies $E_n$ are discrete for a clean interface and depend on the phase difference across the junction.

2. **Caroli-de Gennes-Matricon (CdGM) states**: Inside a vortex core (radius $\sim\xi$), the order parameter vanishes, creating a potential well for quasiparticles. Bound states have energies $E_n \approx (n + 1/2)\Delta^2/E_F$, with the lowest mode at the "minigap" $\sim \Delta^2/E_F$. These are the fermion zero modes of the Jackiw-Rossi theorem, lifted from exact zero by particle-hole asymmetry.

3. **Jackiw-Rebbi modes**: At a domain wall where the mass parameter changes sign, a single zero-energy bound state exists, protected by index theorem. This requires a mass sign change, which does NOT occur at the $Z_3$ walls (B2 eigenvalues remain positive on both sides, as I noted in my Session 32 collab Section 1.3). The Jackiw-Rebbi mechanism does not apply here.

4. **Shockley-Tamm surface states**: At a crystal surface, the broken translational symmetry admits surface-localized states in the bulk band gap. These exist generically when the bulk Bloch Hamiltonian has nontrivial winding.

The relevant analog for $Z_3$ BCS walls is Andreev bound states, NOT Jackiw-Rebbi. The mass does not change sign, but the ORDER PARAMETER PHASE rotates by $2\pi/3$ across the wall. Andreev reflection off a phase gradient creates bound states whose energies depend on the phase difference $\delta\phi$ across the junction. For a clean BCS junction with phase difference $\delta\phi$:

$$E_n = \Delta \cos\left(\frac{\delta\phi + 2\pi n}{N}\right)$$

where $N$ depends on the junction width in units of $\xi$. For $\delta\phi = 2\pi/3$ (the Z_3 phase difference), the lowest Andreev state sits at $E_0 = \Delta\cos(\pi/3) = \Delta/2$ -- half the BCS gap. This gives a FIXED RATIO between the Andreev bound state energy and the gap, independent of $\Delta$. Whether this ratio has any connection to $\phi_{\text{paasch}}$ requires computing the Andreev spectrum of a B2 BCS wall with the specific gap profile at the fold.

---

## Section 2: Assessment of Key Findings

### 2.1 The Closure of the Particle-as-Scalar Program

The document's Section 2 provides a thorough accounting of why bulk eigenvalue ratios cannot be physical mass predictions. All three stated failures are valid:

- **Failure 1** (wrong tau): The operating point tau = 0.190 and phi_paasch tau = 0.150 are algebraically distinct features. No dynamics connects them. This is a permanent constraint.
- **Failure 2** (dressing destroys ratios): BCS dressing either has no effect (Trap 4, diagonal Hamiltonian) or exponentially distorts ratios ($\exp(-1/M)$). Neither regime preserves phi_paasch.
- **Failure 3** (geometric series absent): Only $\phi^1$ is real in the D_K spectrum; $\phi^2$, $\phi^3$ are generic. This is a permanent spectral geometry fact.

The conclusion that phi_paasch is a "mathematical property of D_K, not a physical prediction" is correctly drawn from the constraint map.

### 2.2 The Geometric Mean Equilibrium Mass

The observation that $m^*(i,j) = (m_i \cdot m_j)^{1/2}$ corresponds to the log-midpoint of the wall profile is a clean geometric insight (Section 4.2). The numerical check -- geometric mean of ratios at $\tau = 0.10$ and $\tau = 0.20$ giving 1.5285, within 0.20% of phi_paasch -- is suggestive but requires caution. The geometric mean of two quantities $a$ and $b$ with $a > \phi > b$ will naturally be close to $\phi$ if $a$ and $b$ are close to each other. The relevant question is whether the geometric mean equals phi_paasch for a wall whose endpoints are determined by the DYNAMICS (the modulus equation solutions), not by hand-chosen $\tau$ values.

### 2.3 The n_3 = dim(3,0) Identification

The identification $n_3 = 10 = \dim(3,0)$ in Paasch's alpha derivation is numerologically exact and representation-theoretically natural. But "numerologically exact and natural" describes many coincidences. The alpha-dim gate is well-structured: it asks whether the derivation chain reconstructs with $\dim(3,0)$ in place of the empirical integer. If it passes, the structural connection is established. If it fails, the coincidence is accidental. This is a clean conceptual test.

### 2.4 The Pre-Registered Gate Structure

The five-priority computation program (WALL-phi, PT-count/ratio, JUNCTION-E/angle, WALL-spectrum, alpha-dim) is well-organized with clear dependencies. TRAP-1 as the existential prerequisite is correctly identified. The pass/fail criteria are quantitative. This is how pre-registration should be done.

One concern: the WALL-phi gate tolerance of 5% ($L_{\text{wall}}/\xi_{\text{BCS}} \in [1.455, 1.608]$) is generous. For a ratio of two length scales, 5% accommodates a wide range of parameter combinations. A more stringent test would require the transcendental equation $x = e^{-x^2}$ to emerge from the self-consistency condition itself, not just the numerical value.

---

## Section 3: Collaborative Suggestions

### 3.1 Andreev Bound States at Z_3 Walls -- The Correct Condensed Matter Analog

The document uses "Poschl-Teller bound states" as the wall excitation mechanism. This is one contribution, but the dominant mechanism for excitations at a BCS domain wall is ANDREEV REFLECTION, not single-particle potential scattering. In the BCS state, a quasiparticle incident on a domain wall where the order parameter phase changes undergoes Andreev retroreflection: an electron-like quasiparticle reflects as a hole-like quasiparticle (and vice versa), with the phase mismatch encoding the topological charge of the wall.

For the $Z_3$ walls, the BCS order parameter $\Delta(x) = |\Delta(x)| e^{i\theta(x)}$ rotates its phase by $\pm 2\pi/3$ across the wall. The Bogoliubov-de Gennes (BdG) equation in the presence of an inhomogeneous order parameter:

$$\begin{pmatrix} H_0 - \mu & \Delta(x) \\ \Delta^*(x) & -(H_0 - \mu) \end{pmatrix} \begin{pmatrix} u(x) \\ v(x) \end{pmatrix} = E \begin{pmatrix} u(x) \\ v(x) \end{pmatrix}$$

admits subgap solutions ($|E| < |\Delta_\infty|$) localized at the wall. The spectrum of these Andreev bound states depends on:
1. The phase difference $\delta\phi = 2\pi/3$ (topological, fixed by Z_3)
2. The wall width $L$ relative to $\xi_{\text{BCS}}$ (dynamical, from the modulus equation)
3. The gap profile $|\Delta(x)|$ through the wall (self-consistent, from BdG)

I propose a specific computation:

**ANDREEV-Z3**: Solve the 1D BdG equation for a B2 quasiparticle at a Z_3 domain wall with:
- $\Delta(x) = \Delta_0 \tanh(x/L) e^{i\pi/3 \cdot \text{sgn}(x)}$ (simplest Z_3 wall profile with $\delta\phi = 2\pi/3$)
- $H_0$ = B2 Dirac eigenvalue at the fold, with the Poschl-Teller effective mass from the fold curvature
- Input: wall width $L$ from `s33w3_modulus_equation.npz`, $\Delta_0$ from TRAP-1

**Pre-registered gate**: Andreev bound state spectrum has at least one state at $E = \Delta_0/2$ (the $\cos(\pi/3)$ prediction for a clean junction).

This computation is more physically grounded than the pure Poschl-Teller analysis because it incorporates the BCS order parameter structure. The Poschl-Teller bound states are the NORMAL-STATE analog (no pairing); the Andreev bound states are the SUPERCONDUCTING analog (with pairing). Since the wall separates two BCS vacua with different phases, the Andreev mechanism dominates.

### 3.2 The BdG Equation at an Inhomogeneous Order Parameter

In standard condensed matter, the Bogoliubov-de Gennes equation in the presence of a spatially varying order parameter $\Delta(\mathbf{r})$ is solved self-consistently:

1. Assume a trial $\Delta(\mathbf{r})$
2. Solve BdG for eigenstates $(u_n, v_n, E_n)$
3. Recompute $\Delta(\mathbf{r}) = -g \sum_n u_n(\mathbf{r}) v_n^*(\mathbf{r}) \tanh(E_n/2T)$
4. Iterate until convergence

For the domain wall, the 1D version along the wall normal is tractable. The self-consistent solution gives both the gap profile $|\Delta(x)|$ and the bound state spectrum $\{E_n\}$. In practice, for clean s-wave superconductors, $|\Delta(x)|$ recovers over a distance $\sim \xi$ from the wall center, and the bound states have a minigap $\sim \Delta^2/E_F$ (the CdGM spacing).

The critical question for the framework is whether the SELF-CONSISTENT gap profile at the wall produces a bound state spectrum organized by $\phi_{\text{paasch}}$. This is different from the two separate computations proposed in the document (Poschl-Teller from the normal-state potential, and BCS gap from TRAP-1). The self-consistent BdG incorporates BOTH effects simultaneously.

### 3.3 Z_3 Potts Model Wall Excitation Spectra

The $Z_3$ Potts model near criticality has been studied extensively in 2D statistical mechanics. The relevant results:

- **Integrable field theory** (Delfino-Mussardo 1998): The off-critical 3-state Potts model in the ordered phase is described by an integrable massive field theory with 4 particles and a rich S-matrix. Mass ratios: $m_2/m_1 = 2\cos(\pi/5) = 1.618$ (golden ratio appears in the Potts model too, through the $\phi_{2,1}$ perturbation of the $W_3$ minimal model).
- **Kink-antikink spectrum**: Domain walls between Z_3 vacua carry internal excitations whose mass spectrum is determined by the scattering amplitude of the integrable theory.
- **Near-critical universality**: The mass ratios are UNIVERSAL at the critical point, depending only on the symmetry and dimension.

This is potentially relevant: if the BCS condensate in the (3,0)/(0,3) sector operates near the Z_3 critical temperature (i.e., near the first-order BCS transition), the domain wall excitation spectrum may inherit universal mass ratios from the Z_3 Potts universality class. The golden ratio $m_2/m_1 = 1.618$ would then appear for a DIFFERENT reason than Paasch's empirical observation -- but the mechanism (near-critical Z_3 domain wall) would be specific.

The computation: determine where the system sits relative to the Z_3 BCS critical temperature. If $c^2/(4b) \sim 10^{-6}$ (weakly first-order), the system is CLOSE to the critical point, and the near-critical mass ratios may apply. If the system is deep in the ordered phase (strong BCS), the universal ratios are washed out by corrections.

### 3.4 The kappa = L_wall / xi_BCS Classification

From GL theory (Paper 08), the ratio $\kappa = \lambda/\xi$ determines Type I vs Type II behavior. In the wall context, $L_{\text{wall}}/\xi_{\text{BCS}}$ plays the same role:

- $L/\xi < 1$ ("Type I wall"): The BCS condensate extends beyond the wall. The wall core is fully superconducting. Bound states are delocalized over a distance larger than the wall.
- $L/\xi > 1$ ("Type II wall"): The condensate is narrower than the wall. The wall core has a partially normal region. Bound states are localized within the condensate region, which is SMALLER than the wall.
- $L/\xi \sim 1/\sqrt{2}$ (Bogomolnyi analog): The wall surface energy vanishes. This is the crossover.

If $\phi_{\text{paasch}} = 1.53$ is the value of $L/\xi$, the system is in the "Type II" regime: the wall is wider than the condensate. This means the condensate does not fill the entire wall, and there is a partially normal region near the wall edges. Quasiparticles in this normal region experience the Poschl-Teller potential from the bare eigenvalue spectrum, while those in the condensate core experience Andreev physics. Both contributions would be present simultaneously.

This is testable: measure the spatial profile of $|\Delta(x)|$ through the self-consistent BdG solution and compare the ratio of the condensate width to the wall width.

---

## Section 4: Connections to Framework

### 4.1 Domain Walls Are the Natural Excitations of a First-Order Transition

Paper 04 establishes that when a cubic invariant is present ($c \neq 0$ in $F = a|\Delta|^2 + b|\Delta|^4 + c|\Delta|^3\cos(3\theta)$), the transition is FIRST-ORDER. First-order transitions generically produce domain walls separating the coexisting phases. This is not an assumption of the framework -- it is a CONSEQUENCE of the L-9 cubic invariant ($c = 0.006$--$0.007$) established in Session 33.

The domain walls are therefore structural predictions of the BCS mechanism: any Z_3 first-order BCS transition on the Jensen-deformed SU(3) MUST produce domain walls, and these walls MUST carry topological charge classified by $\pi_0(Z_3) = Z_3$. The question is not whether walls exist (they must) but whether their excitation spectrum has any connection to particle physics.

### 4.2 Quasiparticle Concept at Domain Walls

Paper 11 (Fermi Liquid Theory) establishes the quasiparticle concept: excitations of an interacting system are in one-to-one correspondence with the excitations of the non-interacting system, but with renormalized parameters (effective mass $m^* = m(1 + F_1^s/3)$, finite lifetime $1/\tau \sim (E - E_F)^2$, residual interactions $f_{\ell}$). The quasiparticle description is valid when the spectral weight $Z$ at the Fermi surface is nonzero and the quasiparticle lifetime exceeds the inverse energy: $\hbar/(E\tau) \ll 1$.

At a domain wall, the quasiparticle description must be re-examined because:
1. Translational symmetry is broken in the wall-normal direction, so momentum is not a good quantum number perpendicular to the wall.
2. The order parameter is spatially varying, so the self-energy $\Sigma(x, E)$ is position-dependent.
3. Near the wall center (the fold), the group velocity $v_{B2} \to 0$, and the quasiparticle picture may break down (incoherent spectral weight).

The relevant diagnostic is the spectral function $A(x, E) = -2\text{Im}\, G^R(x, x; E)$ at the wall center. If $A$ shows a sharp quasiparticle peak at $E = E_n$ (with width $\ll E_n$), the excitations are well-defined quasiparticles and the wall-localized mass spectrum is meaningful. If $A$ is broad and featureless, the wall excitations are incoherent and cannot be identified with particles.

This is computable from the BdG Green's function at the wall. It should be added as a diagnostic to the wall-intersection program.

### 4.3 The Kibble-Zurek Connection

If the BCS transition at the wall is first-order, domain walls within the BCS condensate (i.e., Z_3 walls) are produced via the Kibble mechanism during the phase transition. The density of walls after a quench depends on the Kibble-Zurek scaling:

$$n_{\text{defect}} \sim (\tau_Q/\tau_0)^{-d\nu/(1+z\nu)}$$

where $\tau_Q$ is the quench rate, $\tau_0$ the microscopic time scale, $d$ the spatial dimension, and $\nu$, $z$ the critical exponents. For a first-order transition, the Kibble mechanism operates through bubble nucleation rather than critical slowing down, and the wall density is set by the nucleation rate $\Gamma \sim \exp(-S_{\text{bounce}}/T)$.

The modulus dynamics (tau rolling down the potential) provides a natural quench rate. The density of Z_3 walls in the resulting BCS state is then a PREDICTION of the framework, not a free parameter. Whether the wall network is dense enough to account for the observed particle spectrum, and whether it reaches a stable configuration (as opposed to coarsening to a single domain), are open dynamical questions.

---

## Section 5: Open Questions

### 5.1 Can Four B2 Degrees of Freedom Produce Six Sequences?

Paasch identifies six sequences S1--S6 in three conjugate pairs. The document maps these to six oriented Z_3 wall types. But the BCS condensate lives exclusively in the 4-fold B2 multiplet. Each wall type hosts B2 Andreev states with at most 4 internal degrees of freedom. How do 4 internal states produce 6 external sequences? The mismatch is 6/4 = 1.5 -- suggestively close to $\phi_{\text{paasch}}$, but this is likely a numerical coincidence. The counting problem requires specifying exactly which B2 quantum numbers (the U(2) indices within the 4-fold multiplet) distinguish the sequences.

### 5.2 What Sets the BCS Gap Profile at the Wall?

The self-consistent BdG gap profile $|\Delta(x)|$ at a Z_3 domain wall depends on the pairing interaction strength, the density of states, and the phase structure of the order parameter. In standard BCS near a phase boundary, $|\Delta|$ is suppressed over a distance $\sim \xi$ from the wall center (the "proximity effect" of the two BCS phases on each other). If the gap is fully suppressed at the wall center ($|\Delta(0)| = 0$), the wall hosts a normal core analogous to a vortex core, with CdGM-type bound states. If the gap is merely reduced (phase rotation without amplitude suppression), the bound states are Andreev type with higher energies.

The distinction matters quantitatively for the mass spectrum. A vortex-core-type wall (with normal core) has CdGM spacing $\sim \Delta^2/E_F$, which is much smaller than $\Delta$ for weak coupling. An Andreev-type wall (without normal core) has spacing $\sim \Delta$. The ratio of bound state energies to the gap is different in the two cases.

### 5.3 Does the Wall Network Stabilize or Coarsen?

In condensed matter, domain wall networks after a quench typically COARSEN: larger domains grow at the expense of smaller ones, driven by the wall tension. In 2D, the coarsening rate goes as $L(t) \sim t^{1/2}$ (curvature-driven motion). The final state is a single domain -- no walls, no wall-localized excitations.

For the phonon-exflation framework to produce a stable wall network, a STABILIZATION MECHANISM against coarsening is needed. Possible candidates:
- Pinning by the modulus field inhomogeneity (the wall is pinned at the barrier-fold merger location)
- Topological protection (if the wall network forms a closed lattice with no free boundary, like the Abrikosov vortex lattice in Type II superconductors)
- Coupling to other conserved quantities that prevent wall motion

Without a stabilization mechanism, the wall network is transient and cannot account for stable particles.

### 5.4 The Deepest Question

The document reframes particles as wall-localized excitations. But in condensed matter, wall-localized excitations are QUASIPARTICLES -- they carry quantum numbers, have finite lifetime, and scatter off each other. They are NOT the fundamental particles of the theory; they are emergent. The phonon-exflation framework claims that SM particles are precisely this kind of emergent excitation.

The deepest question is then: what determines the LIFETIME of these wall-localized quasiparticles? In condensed matter, quasiparticle lifetime at a domain wall is set by the scattering rate off the wall's thermal fluctuations and off other quasiparticles. For Landau quasiparticles (Paper 11), $1/\tau \sim (E - E_F)^2$, ensuring stability near the Fermi surface. For wall-localized states, $1/\tau$ depends on the wall's rigidity (stiffness against transverse fluctuations) and the density of other bound states.

If the wall-localized "particles" have lifetime $\tau \gg \hbar/E$ (where $E$ is their energy), they are well-defined quasiparticles and the mass spectrum is meaningful. If $\tau \sim \hbar/E$, the states are incoherent resonances and cannot be identified with sharp particle masses. This is the Landau criterion for the existence of quasiparticles, applied to wall excitations.

---

## Closing Assessment

The reframe from "particles as eigenvalue ratios" to "particles as wall-localized collective excitations" is a natural evolution of the phonon-exflation framework and is well-motivated by condensed matter precedent. Andreev bound states, CdGM modes, and Jackiw-Rebbi zero modes are all established mechanisms for generating localized excitations at topological defects in ordered media. The Z_3 domain wall structure follows necessarily from the L-9 cubic invariant, and the six oriented wall types match Paasch's six-sequence phenomenology combinatorially.

However, the quantitative program faces three obstacles that the document acknowledges but does not resolve: (1) the Poschl-Teller well at the fold appears too shallow for multiple bound states at the estimated wall parameters; (2) the 45-degree Paasch sequence angle and the 120-degree Z_3 junction angle are incommensurable; (3) the BCS condensate lives exclusively in the 4-fold B2 channel, requiring 4 internal degrees of freedom to generate 6 external sequences.

The TRAP-1 gate remains the existential prerequisite. Without a BCS condensate at the wall, there are no Andreev states, no Z_3 phases, no domain walls in the order parameter, and no wall-localized excitations. Everything downstream is contingent on a single number: $\Delta_{\text{wall}}$.

The correct condensed matter analog for excitations at a Z_3 BCS domain wall is Andreev bound states in the presence of a $2\pi/3$ phase twist, NOT pure Poschl-Teller scattering off a normal-state potential. Both mechanisms contribute, but in a gapped system the Andreev physics dominates. The self-consistent BdG equation at the wall -- incorporating the tanh gap profile, the fold effective mass, and the Z_3 phase structure simultaneously -- is the computation that will determine whether the wall-intersection hypothesis survives or joins the 18 closed mechanisms.

The framework's claim that SM particles emerge as quasiparticle excitations of a domain wall condensate is the most Landau-like statement in the entire project: particles as collective modes, masses from the defect geometry, quantum numbers from the topology. Whether Nature agrees is decided by the numbers, not the narrative.
