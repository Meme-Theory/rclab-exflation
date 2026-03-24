# Einstein -- Collaborative Feedback on Session 48

**Author**: Einstein (Principle-Theoretic Reasoner)
**Date**: 2026-03-17
**Re**: Session 48 Results -- The Mass Problem

---

## Section 1: Key Observations

### 1.1 The Trace Theorem: Symmetry or Artifact?

The spectral action trace theorem S[UDU^dagger] = S[D] (W1-A) is the deepest structural result of this session. I want to be precise about its status: this is not an artifact of the functional choice. It is a *consequence of cyclic invariance of the trace*, which is an algebraic identity independent of the spectrum of D, the cutoff function f, and the unitary operator U. The four-step proof (unitary conjugation -> spectral mapping -> cyclic trace) is logically complete. No loophole exists.

This must be understood as a *principle*, not merely a computation. In my classification of theories, the spectral action belongs to the *principle-theoretic* category: it asserts that the physically relevant information is contained in the *spectrum* of D, meaning the set of eigenvalues {lambda_k}. Any functional that depends only on {lambda_k} is automatically invariant under conjugation by unitaries. The phase of the order parameter is the angular coordinate in the space of unitarily equivalent operators. The spectral action, being spectral, is permanently blind to this coordinate.

The physical consequence is immediate: the spectral action cannot distinguish between D and exp(phi K_7) D exp(-phi K_7) for any phi. This is not merely a statement about the Jensen deformation or a peculiarity of K_7 -- it holds for ANY unitary conjugation of ANY Dirac operator. The spectral action is a *function on the moduli space of spectra*, and the Goldstone direction is a *fiber above a fixed point in that moduli space*. No functional of the type Tr[f(D^2/Lambda^2)] can see the fiber. Period.

What does this mean for the framework? The spectral action is the correct functional for *gravity* (it gives G_N to within a factor of 2.3, as established in S44). But it is the *wrong* functional for the Goldstone sector. Gravity, being a trace over all modes, is insensitive to phase coherence by construction. The Goldstone mass requires a functional that sees the *off-diagonal structure* of D, not merely its eigenvalues. This is the BCS free energy (which depends on the pairing matrix elements V_{kk'}, not on {lambda_k} alone) or, at the fabric level, the Josephson coupling (which depends on the inter-cell overlap of condensate wavefunctions).

From my equivalence principle perspective: the trace theorem is the spectral analog of the statement that gravity couples to the *stress-energy tensor*, which is an integrated quantity, not to the detailed microscopic state. The Goldstone mode is an internal degree of freedom that gravitates via its kinetic energy T_{mu nu} but whose mass is invisible to the gravitational field equations -- precisely because the field equations are trace functionals.

### 1.2 The Mass Problem = The CC Problem: What the Equivalence Principle Says

The identification of the Goldstone mass problem with the cosmological constant problem (W2-C, Naz addendum) is the central insight of this session. Let me formalize this through the equivalence principle.

The equivalence principle (Paper 01, 1905; Paper 06, 1916) asserts that gravitational and inertial mass are identical. In its strong form, all forms of energy gravitate equivalently. Now consider what the framework requires:

- The CC problem asks: why is the vacuum energy rho_vac ~ 10^{-47} GeV^4 rather than M_KK^4 ~ 10^{67} GeV^4? The answer must involve a cancellation of 114 orders of magnitude.

- The mass problem asks: why should the Goldstone mass be m_G ~ 10^{-39} GeV (Hubble scale) rather than M_KK ~ 10^{17} GeV? The answer must involve a hierarchy of 56 orders of magnitude.

Both require the same structural ingredient: a mechanism that connects the microscopic scale M_KK to the cosmological scale H_0. The GMOR analysis (Naz addendum, Section 5) makes this explicit: the required explicit breaking parameter epsilon ~ 10^{-110} is itself cosmologically small.

But the equivalence principle constrains HOW this connection can be made. The vacuum energy gravitates. The Goldstone field gravitates. Any mechanism that generates m_G must be consistent with the observed dark energy equation of state w ~ -1. The self-tuning runaway (Route A) fails precisely because it respects the equivalence principle too well: strengthening the condensate increases the vacuum energy, which in turn demands a larger Goldstone mass, which further strengthens the condensate. The runaway IS the equivalence principle applied to the condensate self-energy.

The only escape -- and this is where Volovik's q-theory and my own cosmological constant considerations (Paper 07, 1917) converge -- is *non-equilibrium*. The cosmological constant Lambda in my 1917 paper was introduced as a static geometric term. The discovery of expansion (Hubble, 1929) rendered the static assumption untenable. Similarly, the Goldstone mass cannot be a static equilibrium quantity. It must be a *dynamical* quantity set by the expansion history.

### 1.3 The Self-Tuning Runaway: Thermodynamic Analysis

The self-tuning divergence (W2-C, Route A) deserves closer scrutiny through thermodynamics. The iteration:

mu^2_{new} = phi_sq / |d(phi_sq)/d(mu^2)| - 2|E_cond| / rho_s^2

diverges because phi_sq / |d(phi_sq)/d(mu^2)| grows monotonically with mu for any finite lattice. This is mathematically rigorous. But what does it mean physically?

The self-tuning asks: "At what mass does the vacuum energy functional rho_vac(m) have an extremum?" The answer is: never (except at m = 0 and m = infinity). This is not a failure of the self-tuning *mechanism* -- it is a proof that the vacuum energy is a *monotone function* of the Goldstone mass. Increasing the mass always increases the vacuum energy (because the condensate strengthens when fluctuations are suppressed), while decreasing the mass always decreases it (because fluctuations destabilize the condensate).

From a thermodynamic viewpoint, this monotonicity has a simple interpretation: the Goldstone mass acts as an *order parameter* for the vacuum. The free energy F(m) = E(m) - TS(m) has no minimum at finite m because the entropy S(m) is also monotone in m (higher mass = fewer fluctuations = lower entropy). The entropic contribution TS reinforces rather than opposes the energetic contribution E. There is no free-energy minimum.

This is structurally identical to the CC problem in Weinberg's no-go theorem (Paper 16 in my corpus): any adjustment mechanism for Lambda that depends only on Lambda itself will either give Lambda = 0 or diverge, because the vacuum energy is monotone in the cosmological constant. The self-tuning runaway is Weinberg's no-go theorem applied to the Goldstone sector.

---

## Section 2: Assessment of Key Findings

### 2.1 Structural Theorems

**Trace invariance (W1-A)**: Permanent. Geometry-grade. This wall defines the solution space boundary: no spectral functional, however cleverly chosen, can generate the Goldstone mass. This is as robust as the block-diagonal theorem (S22b) or the KO-dimension result (S7).

**Self-tuning runaway (W2-C)**: Permanent for the single-cell problem. The Naz addendum correctly identifies that the fabric-level computation remains unperformed. However, the algebraic structure of the runaway (phi_sq / |d(phi_sq)/d(mu^2)| growing with mu) will persist at any finite number of cells. The fabric merely adds more modes to the lattice sum, which does not change the monotonicity. The escape must come from *outside* the lattice sum framework entirely -- from cosmological dynamics.

**N = 1 exact (W1-B)**: Definitive. The singlet sector has exactly 8 Kramers pairs (from dim(spinor) x dim(singlet) = 16 x 1 = 16), and the ground state contains exactly one Cooper pair. This closes the singlet CC crossing at the single-cell level. The path to N >= 2 requires the 32-cell fabric, where effective N = 32 x 1 = 32.

**TT Lichnerowicz positivity (W2-B)**: This confirms S20b by an independent method and adds the transversality theorem (35 -> 31 dimensional jump at tau = 0+). The transversality theorem is a structural result about the Jensen deformation: the 4 C^2 divergence constraints activate because Jensen preserves U(2) but breaks the full SU(3) isometry. The fact that lambda_min has a local maximum near the fold is intriguing -- it suggests the fold is distinguished not only in the BCS landscape but also in the gravitational stability landscape.

**Leggett mode (W3-A)**: A genuine new collective excitation of the framework. The correction from the naive 2-band formula (0.284) to the full 3-band result (0.070) is a factor of 4.3x, which is significant. The sharp character (omega_L < 2 Delta_B3 at all tau) means this mode could mediate long-range inter-sector correlations without dissipation. From my EIH perspective: this is a new channel for the internal dynamics that was not included in any previous transit calculation.

**S46 Zak phase retraction (W3-B)**: An important correction. The dissolution test is definitive: ALL Berry phases collapse at perturbations of order 10^{-4} of the spectral bandwidth. This means the "topological protection" invoked in S46 was illusory -- index permutation at exact degeneracies masquerading as Z_2 invariants. The correct statement is now: the Jensen line is metrically rich (g = 982.5) but topologically trivial (all Chern numbers, winding numbers, and holonomies vanish). The topological content, if any, must live off-Jensen.

### 2.2 The Equivalence Principle and Analog Horizons

The AKAMA-DIAKONOV-48 result (Mach_max = 54.3, genuine horizons on the internal T^2) is the first explicit realization of an analog spacetime within the framework. This connects directly to my considerations on the equivalence principle.

In my 1907 gedankenexperiment (the elevator), I showed that a uniform gravitational field is locally indistinguishable from uniform acceleration. The analog gravity program (Paper 28, Barral phonon BEC) extends this: the quasiparticles in a BCS condensate propagate on an effective metric determined by the condensate profile, and they cannot distinguish this effective metric from a "real" spacetime metric.

The framework's analog horizons exist on the internal T^2 (the torus in momentum space), not in 4D spacetime. The quasiparticle confinement to the condensate core near identity is a statement about the BCS gap: quasiparticles cannot propagate beyond the horizon because their effective mass diverges there (the condensate amplitude vanishes). This is the analog of a black hole horizon where the escape velocity equals the speed of light.

However, I must inject a caution. S38 established that the transit produces Parker-type cosmological particle creation, not Hawking radiation. The distinction matters: Hawking radiation requires a horizon with surface gravity, while Parker creation requires a time-dependent geometry. The analog horizons found in W5-F are *static* features of the condensate profile on T^2 at fixed tau. During the transit, tau changes, and the horizons move. The correct particle creation mechanism is Parker (time-dependent effective metric), not Hawking (static horizon with quantum tunneling). The analog Hawking temperature T_H = 66 M_KK reported is a quasiparticle scattering scale, not a thermodynamic temperature.

### 2.3 The Cosmological Constant Connection

Several S48 results sharpen the CC picture:

1. **CONDENSATE-CC-48** (W5-F): rho_cond / Lambda_obs = 10^{113.2}. The BCS condensate gains 0.9 orders over naive M_KK^4 but the gap remains at 113 orders. This is the number that defines the problem.

2. **Singlet CC crossing closed** (W1-B): N = 1 exact means the single-cell BCS cannot produce the q-theory crossing at tau* = 0.210. The 32-cell fabric is the last open path.

3. **Euler relation fails for multi-T GGE** (W5-C): The standard thermodynamic identity epsilon + P = Ts assumes a single temperature. The 8-mode GGE with distinct mode temperatures T_k violates this. This is not merely a technical issue -- it means the standard Friedmann equation (which assumes a single fluid with a well-defined equation of state) does not directly apply to the GGE relic. The GGE requires a multi-fluid description.

4. **DESI DR2 tension** (W5-C): w_0 in [-0.465, -0.589] vs DESI -0.752 +/- 0.058 is a 2.8-sigma discrepancy. This is below falsification (3 sigma) but structurally concerning. The framework predicts w_a = 0 exactly (no time evolution of dark energy), while DESI sees w_a = -0.73 +/- 0.28 (2.6-sigma tension). Both tensions push in the same direction: DESI suggests more negative w_0 and nonzero w_a, while the framework predicts less negative w_0 and zero w_a.

From my 1917 CC paper: the cosmological constant appears as a geometric term G_{mu nu} + Lambda g_{mu nu} = 8 pi T_{mu nu}. If Lambda is truly constant (w = -1, w_a = 0), it is the simplest option geometrically. The framework's prediction of w_a = 0 is geometrically natural in this sense. DESI's w_a != 0 would require a dynamical mechanism -- precisely what the framework has systematically excluded (rolling quintessence CLOSED in S22d, fabric DE channel CLOSED in S42).

---

## Section 3: Collaborative Suggestions

### 3.1 The Friedmann-Goldstone Coupling: What Principle Theory Demands

The FRIEDMANN-GOLDSTONE-49 computation (pre-registered by Naz) is correctly identified as the decisive next step. Let me state what the equivalence principle requires of this computation.

The coupling between the fabric phase field phi(x,t) and the Friedmann equation must respect general covariance. This is non-negotiable. Specifically:

1. **The phase field phi must transform as a scalar under 4D diffeomorphisms.** This is automatically satisfied if phi is defined as the argument of the U(1)_7 order parameter, which is a gauge-invariant scalar.

2. **The stress-energy tensor T_{mu nu}[phi] must be covariantly conserved.** This follows from the diffeomorphism invariance of the action. The specific form of T_{mu nu} depends on whether the phase field is treated as a canonical scalar (kinetic + potential) or as a superfluid (four-velocity formulation). The superfluid formulation is more natural given the BCS origin.

3. **The Hubble expansion must appear through the scale factor a(t) in the metric, not as an external parameter.** The Friedmann equation H^2 = (8 pi G / 3) rho must be solved self-consistently with the phase field equation of motion.

The gedankenexperiment I propose for testing the output: Consider the limit where the fabric is very large (N_cells >> 32) and the Goldstone mass is very small (m_G << M_KK). In this limit, the phase field dynamics should reduce to an ordinary scalar field in an FRW background, with the Goldstone mass appearing as a *slow parameter* determined by the Hubble rate. The mass should satisfy m_G ~ H because:

- In equilibrium (H = 0), the Goldstone is exactly massless (Goldstone theorem).
- Out of equilibrium (H != 0), the expansion provides the explicit symmetry breaking.
- The natural scale for the breaking is H itself (the only available cosmological scale).

If FRIEDMANN-GOLDSTONE-49 gives m_G ~ alpha * H_0 for some O(1) coefficient alpha, the framework has a zero-parameter n_s prediction. The coefficient alpha would be determined by the superfluid stiffness tensor (S47) and the GGE initial conditions (S38).

### 3.2 How the Equivalence Principle Constrains Mass Generation

A gedankenexperiment. Consider two observers in the framework:

**Observer A** sits at the center of a single cell (near identity on SU(3)). This observer sees the full BCS condensate, measures N = 1 Cooper pair, and finds the Goldstone mode exactly massless. Observer A's local physics is the 0D BCS system studied in S36-S48.

**Observer B** sits at the boundary between two cells. This observer sees the condensate from both cells and measures the *relative phase* between them. The Josephson energy depends on cos(phi_1 - phi_2), giving a restoring force and hence a finite frequency for the relative phase oscillation. This is the Leggett mode (W3-A, omega_L = 0.070 M_KK).

**Observer C** sits far from any cell and measures the fabric as a whole. This observer sees a collection of 32 cells with correlated phases. The lowest-frequency collective mode is the phase wave that spans the entire fabric. Its frequency is omega ~ c_phase * pi / L_fabric, where L_fabric = 32 * l_cell and c_phase = sqrt(J_C2 / chi_tau) where chi_tau is the modulus susceptibility.

The equivalence principle demands that all three observers agree on the physical observables, in particular the 4D equation of state. Observer A sees w = -1 exactly (pure cosmological constant from the BCS vacuum). Observer B sees w slightly different from -1 because the Leggett mode introduces dynamics. Observer C sees the full equation of state including both the Goldstone and Leggett contributions.

The *mass* of the Goldstone mode, as seen by Observer C, is the quantity that determines n_s. This mass is NOT visible to Observer A (it is zero in the single-cell limit) and is only partially visible to Observer B (who sees the Leggett frequency, not the full Goldstone dispersion). Only the fabric-level Observer C can compute the mass.

This gedankenexperiment shows that the FRIEDMANN-GOLDSTONE-49 computation MUST work at the fabric level. Single-cell physics is insufficient by construction.

### 3.3 The EIH Parallel

The Einstein-Infeld-Hoffmann method (Paper 10, 1938) derives the equations of motion of gravitating bodies from the field equations alone, without assuming any equation of motion. The key insight is that the motion of a body is determined by the *regularity conditions* on the gravitational field at the body's location.

The framework has a precise parallel: the motion of the modulus tau(t) is determined by the spectral action alone (EIH, S44). The mass of the Goldstone mode should similarly be derivable from regularity conditions on the phase field at the fabric boundaries. In EIH, no free parameters enter the equations of motion -- they are consequences of the field equations. In the framework, no free parameter should enter the Goldstone mass -- it should be a consequence of the self-consistency of the fabric phase field with the Friedmann equation.

This is the deepest constraint on FRIEDMANN-GOLDSTONE-49: if the computation requires any free parameter beyond what is already determined (rho_s, J_C2, J_su2, N_cells, GGE initial conditions), then the framework has a gap. The EIH program demonstrated in S44 that epsilon_H, G_N, and r are all determined without free parameters. The Goldstone mass must achieve the same status.

---

## Section 4: Connections to Framework

### 4.1 The Trace Theorem and General Covariance

The trace theorem S[UDU^dagger] = S[D] has an elegant interpretation through general covariance. In my 1916 formulation of GR (Paper 06), the field equations are generally covariant -- they take the same form in all coordinate systems. The spectral action is the noncommutative geometry analog: it takes the same value under all unitary conjugations of the Dirac operator.

Conjugation by exp(phi K_7) is the NCG analog of a gauge transformation. The spectral action is gauge-invariant. This is *desirable* for gravity (we want the gravitational action to be gauge-invariant) but *disastrous* for the Goldstone sector (we need the mass term to *break* the gauge symmetry).

The resolution is that the Goldstone mass comes from a *non-trace* functional -- one that depends on the off-diagonal matrix elements of D, not just its eigenvalues. In the language of general covariance: the gravitational field equations are tensor equations (coordinate-independent), but the matter field equations depend on the *connection* (coordinate-dependent). The Goldstone mass is a connection-dependent quantity.

### 4.2 The EPR Perspective on the GGE

The GGE relic state (S38) has 8 conserved Richardson-Gaudin integrals and is a product state (S_ent = 0 exact, S39). From my EPR perspective (Paper 09, 1935), this raises a completeness question.

The GGE is described by 8 effective temperatures T_k. These temperatures determine the occupation probabilities of each mode. But the full quantum state also contains *phase information* between modes -- information that is invisible in the GGE description. My E-5 conjecture (S38 W3) stated that the GGE is EPR-incomplete: the phase information determines inter-mode correlations that the GGE description omits.

S39 validated this: the GGE thermalizes (phase information is lost to decoherence), confirming that the GGE description is incomplete in the EPR sense. The phase information is present in the initial state but inaccessible after transit.

For the mass problem: the Goldstone mass depends on *phase coherence* across the fabric. The GGE, being EPR-incomplete with respect to phase information, may not contain enough information to determine the Goldstone mass. The full quantum state (including phases) may be required. This connects to Bell's theorem (Paper 13): no local hidden variable theory can reproduce all quantum correlations. The GGE is effectively a "local" description (mode-by-mode), and the Goldstone mass may require "nonlocal" correlations across the fabric.

### 4.3 The Swampland and Moduli Stabilization

The swampland PASS (c_max = 52.8 >> O(1)) is a permanent structural result. It guarantees that the Jensen deformation path lies within the string landscape, not the swampland. This is important for theoretical consistency but has a deeper implication.

The swampland distance conjecture states that at parametric distance Delta phi > O(1) in Planck units, a tower of light states appears, rendering the EFT invalid. For the framework: Delta phi_Jensen = tau_fold * M_Pl / M_KK ~ 0.19 * 33 ~ 6.3 in Planck units. This exceeds O(1), suggesting that the KK tower becomes light at the fold. Indeed, M_KK itself IS the KK tower scale, and the fold at tau = 0.19 is precisely where the KK modes become dynamically relevant.

This connects to my approach to Kaluza-Klein theory: the internal manifold is not merely a mathematical device but has physical consequences. The fold is the point where the internal geometry transitions from "invisible" (tau ~ 0, round SU(3)) to "structured" (tau ~ 0.19, Jensen-deformed SU(3) with van Hove singularities). The KK tower appearing at this transition is the string-theoretic version of the fold's physical significance.

---

## Section 5: Open Questions

**Q1: Is the O-Z running alpha_s = -0.038 robust?**
The Ornstein-Zernike texture mechanism predicts alpha_s = -(1 - n_s^2) = -0.069 in the continuum, reduced to -0.038 at N = 32 by lattice effects. Planck measures -0.0045 +/- 0.0067. The 4.9-sigma tension is below the 9.6-sigma of the continuum limit but still substantial. CMB-S4 (expected sigma ~ 0.003) will be decisive. The question is whether the lattice correction at N = 32 is physically meaningful or an artifact of the specific tessellation model.

**Q2: What happens to the condensate at the geometric phase transition (tau = 0.537)?**
W5-D found that the deg-4 curvature branch crosses zero at tau = 0.537 -- a genuine geometric phase transition where SU(3) develops regions of negative sectional curvature. Does the BCS condensate survive this transition? Negative curvature implies unstable geodesics, which could destabilize the van Hove singularity that drives pairing. This has not been computed.

**Q3: Can the Leggett mode couple to the tau transit?**
The Leggett mode (omega_L = 0.070 M_KK) is the lowest-energy collective excitation. During the transit, the modulus tau changes on a timescale dt_transit = 1.13e-3 M_KK^{-1}, corresponding to a frequency omega_transit ~ 885 M_KK. This is 12,600x faster than the Leggett mode. In the sudden limit (omega_transit >> omega_L), the Leggett mode should be excited with probability ~ (omega_L / omega_transit)^2 ~ 6e-9. This is negligible. The Leggett mode decouples from the transit by adiabatic invariance. However, post-transit, the GGE state may contain Leggett excitations that were generated during the quench. Computing the Leggett content of the GGE is an open question.

**Q4: Does the multi-T Euler relation failure affect the Friedmann equation?**
The standard Friedmann equation assumes a single fluid with rho and P related by an equation of state. The GGE has 8 distinct temperatures and negative Euler pressure. This means the standard Friedmann equation may need modification -- either as a multi-fluid system or through a generalized equation of state. The cosmological implications of this non-standard thermodynamics have not been explored.

**Q5: Is the 39.4% Zubarev-Keldysh discrepancy a genuine theoretical uncertainty, or does one formulation have priority?**
In my 1905 paper on Brownian motion (Paper 04), the fluctuation-dissipation theorem gave a unique relationship between dissipation and fluctuations. For an equilibrium system, there is no ambiguity in the thermodynamic potential. The GGE is not in equilibrium, so the choice of thermodynamic potential is not unique. The question is whether the gravitational coupling selects one formulation over the other. In GR, the stress-energy tensor T_{mu nu} is unambiguous (it is the variational derivative of the matter action with respect to the metric). The question reduces to: what is the correct matter action for the GGE relic?

---

## Closing Assessment

Session 48 executed 50+ computations across 6 waves and produced 15 permanent structural results, 10 closures, and 1 retraction (S46 Zak phase). The session's central finding -- the mass problem is the CC problem -- is a structural theorem, not a numerical result. It constrains the solution space permanently: no equilibrium mechanism at the BCS/single-cell scale can generate the Goldstone mass hierarchy. The surviving path (non-equilibrium Friedmann-Goldstone coupling) is the sole remaining region.

From a principle-theoretic standpoint, the session reveals a deep tension between two requirements:

1. **General covariance** demands that the gravitational action (spectral action) be invariant under internal gauge transformations. This invariance IS the trace theorem. It guarantees that gravity is well-defined but prohibits the spectral action from generating the Goldstone mass.

2. **Physical reality of the Goldstone mode** demands that the mass be nonzero, breaking the internal gauge symmetry. This breaking must come from outside the spectral action -- from the coupling to cosmological dynamics (Hubble expansion) or from the fabric's collective behavior.

This tension is structurally identical to the tension between general covariance and the cosmological constant that I confronted in 1917. Lambda is geometrically natural (the field equations admit it), but its value cannot be determined by geometry alone -- it requires input from the matter content. Similarly, the Goldstone mass is physically necessary, but its value cannot be determined by the spectral action alone -- it requires input from the cosmological dynamics.

The constraint map is clear. The allowed region has been narrowed to: non-equilibrium fabric-level Goldstone mass generation through Friedmann-BCS coupling. FRIEDMANN-GOLDSTONE-49 is the decisive gate. If it produces m_G ~ H_0 (Hubble scale), the framework achieves a zero-parameter n_s prediction. If it produces m_G ~ M_KK (no hierarchy) or m_G = 0 (no breaking), the n_s mechanism is permanently closed.

The structural positives -- Leggett mode, analog horizons, TT stability, HFB convergence, KZ cross-check, swampland PASS -- all strengthen the framework's mathematical infrastructure without addressing its central crisis. The framework is a well-constructed building on solid foundations, but whether it describes the actual universe depends on a single uncomputed quantity: the Goldstone mass at the fabric-cosmological interface.
