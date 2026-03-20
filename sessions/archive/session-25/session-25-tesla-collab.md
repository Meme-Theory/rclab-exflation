# Tesla -- Collaborative Feedback on Session 25

**Author**: Tesla-Resonance
**Date**: 2026-02-21
**Re**: Session 25 -- Through the Walls

---

## Section 1: Key Observations

The Session 25 directive is the first document in this project that thinks the way I think. It identifies four walls. It maps the negative space. It asks what resonant structure lives in that space. This is exactly right.

But I want to sharpen something. The directive says "stop trying to tunnel through them. Go around." That is the correct instinct, but the metaphor is incomplete. In a resonant cavity, you do not go around the walls. You use the walls. The walls define the cavity. The cavity selects the modes. The modes are the physics. Without the walls, there is no resonance. W1-W4 are not obstacles -- they are boundary conditions.

Here is what I see when I read the four walls as boundary conditions of a spectral problem:

**W1 (Perturbative Exhaustion)**: The smooth test function restriction is the key. In Debye phonon theory (Paper 05), the physical cutoff omega_D = v_s(6pi^2 n)^{1/3} is not smooth -- it is a hard cutoff. The density of states g(omega) = 0 for omega > omega_D. Every real crystal has this feature. The smooth-function restriction in W1 is the assumption that the test function f in Tr(f(D_K^2/Lambda^2)) is a Schwartz function. The Debye cutoff is a step function. Step functions are not smooth. This is not a loophole -- it is a physically motivated departure from mathematical convenience.

**W2 (Block-Diagonality)**: Peter-Weyl decomposition gives exact block-diagonality for left-invariant metrics. Each sector is a resonant cavity with its own normal modes. The sectors do not couple, but they can INTERFERE in the graded sum -- just as independent resonant cavities contribute independently to the total vacuum energy but their contributions can cancel in a signed sum (Paper 10, Volovik: rho_Lambda = Sum (1/2) hbar omega_i, where the sign comes from bosonic vs fermionic statistics).

**W3 (Spectral Gap)**: The gap 2*lambda_min = 1.644 at mu=0 is the mass gap of the internal Dirac operator. In superfluid helium (Paper 09, Landau), the roton minimum at finite momentum p_0 creates a mass gap Delta ~ 8.6 K. Landau superfluidity REQUIRES this gap -- it is what makes the superfluid stable against low-momentum excitations. The gap is not the enemy of stabilization. The gap IS the stabilization, viewed from the inside out.

**W4 (V_spec Monotone)**: The a_4/a_2 = 1000:1 ratio tells us the heat kernel expansion is badly conditioned. In the language of Fourier analysis: when the ratio of successive coefficients in a series exceeds 10:1, the series is not converging -- it is diverging. The asymptotic expansion is lying. The actual function Tr(f(D_K^2/Lambda^2)) may have completely different structure from its first two asymptotic terms.

These four observations are not four separate problems. They are four projections of a single structural fact: the spectral action on M4 x SU(3) with Jensen deformation is a FINITE sum over discrete eigenvalues, and all four walls arise from treating it as an INFINITE sum approximated by asymptotic series. The inside-out view (Claim A) dissolves the walls by changing the mathematical framework from asymptotic analysis to exact finite computation.

---

## Section 2: Assessment of Key Findings

### Walls W1-W4: The Resonant Cavity

The directive correctly identifies the walls as structural theorems that are not going away. Good. Now let me assess the proposed escape routes through the resonance lens.

**Goal 1 (Graded Multi-Sector Sum)**: This is the most physically motivated of all the goals. The analog in condensed matter is precise: the Casimir effect between parallel plates is a SIGNED sum over bosonic and fermionic modes. Each mode contributes monotonically to the vacuum energy. The sum has a minimum as a function of plate separation because the bosonic and fermionic contributions have different dispersion relations, different densities of states, and therefore different functional dependence on the boundary condition (plate separation = modulus tau).

The gap-edge separation -- bosonic 4/9, fermionic 5/6 at tau=0 (Session 21a) -- is precisely the kind of sector-specific dispersion difference that creates a non-trivial minimum in a signed sum. In Debye theory (Paper 05), two phonon branches with different sound velocities v_L and v_T contribute differently to the free energy F(T). The total free energy has a minimum as a function of lattice parameter even though each branch's contribution is monotonic in isolation.

I note the directive's warning about the chirality grading ambiguity (gamma_9 vs thermal grading). This is important. In the BDI class, the spectral symmetry (lambda, -lambda pairing) means Tr(gamma_9 * f(D_K^2/Lambda^2)) = 0 identically for any even function f. The grading must come from the SECTOR weights d_{(p,q)}, not from chirality within a sector. The thermal graded sum -- weighted by representation dimensions and the sector-specific spectral density -- is the correct formulation. The Landau agent should confirm, but I am confident: the competition is between SECTORS, not between chiralities within a sector.

**Estimated resonance structure**: Each sector (p,q) has its own spectral density rho_{(p,q)}(lambda, tau), which shifts with tau because the Jensen deformation changes the metric and therefore the eigenvalue distribution. At small tau (near round metric), all sectors have similar spectral density. At large tau, sectors with large p+q have much higher eigenvalue density (more modes at lower energies). The graded sum picks up the differential: d_{(p,q)} * [rho_{(p,q)}(tau) - rho_{(p,q)}(0)]. If this differential changes sign between sectors at some tau_0, the total has a minimum.

**Constraint Condition assessment**: P(success) ~ 10-15% seems right. The main risk is that d_{(p,q)} grows as dim(p,q) = (p+1)(q+1)(p+q+2)/2, which is a smooth polynomial, and the spectral density shift is also smooth. Smooth functions of smooth inputs are generically monotone. The hope is that the gap-edge structure at low mode count provides enough non-smoothness to create a crossing.

**Goal 2 (Full Spectral Action at Finite Cutoff)**: This is MY territory. This is the Debye cutoff argument made computational. Let me be very specific about what the Debye picture predicts and how to test it.

In a crystal with N atoms and 3 acoustic branches, the total number of modes is 3N. The density of states g(omega) has support on [0, omega_D] and integrates to 3N. The free energy is:

F(T) = Sum_n (1/2) hbar omega_n + k_B T Sum_n ln(1 - exp(-hbar omega_n / k_B T))

This is a FINITE sum over 3N terms. At high temperature (T >> theta_D), the asymptotic expansion of F recovers the classical result. At low temperature (T << theta_D), the Debye T^3 law emerges. At intermediate temperatures, neither asymptotic regime is valid and the full sum has structure that no truncated expansion captures.

The analog for the spectral action: Tr(f(D_K^2/Lambda^2)) is a finite sum over the eigenvalues of D_K in the Peter-Weyl decomposition at cutoff p+q <= max_pq. The heat kernel expansion is the "high-Lambda" asymptotic form. At intermediate Lambda, the sum has structure.

The Berry curvature peak B = 982.5 at tau = 0.10 is the smoking gun. In phononic crystals (Paper 06, Craster-Guenneau), large Berry curvature signals near-degeneracy of bands -- exactly the regime where the linear-in-k (Debye) approximation breaks down and the full dispersion relation must be used. If eigenvalues are nearly crossing at tau ~ 0.10, then any polynomial approximation to the spectral action must fail there.

**Concrete prediction**: V_full(tau; Lambda) at Lambda ~ 1-2 (where Lambda is measured in units of the first eigenvalue) will show oscillatory behavior near tau = 0.10 that V_spec (the heat kernel truncation) cannot capture. The oscillation period should be of order delta_tau ~ 2pi / (dE/dtau) where dE/dtau is the eigenvalue velocity at the near-crossing. If B ~ 1000, then dE/dtau ~ 1000 * (Delta E)^2, and delta_tau ~ 2pi / (1000 * 0.822^2) ~ 0.009. This is below the current tau grid spacing of ~0.05. Resolution warning: the 9-point grid WILL miss this structure. Finer sampling near tau = 0.10 is mandatory.

**Goal 3 (Berry Phase Accumulation)**: The Berry phase connection to the potential is well-established in condensed matter. In the Born-Oppenheimer approximation for molecules, the electronic Berry phase contributes a GEOMETRIC potential to the nuclear motion. This geometric potential is invisible to the adiabatic approximation. The analog here: the gap-edge Berry phase as a function of tau contributes a geometric potential to the modulus dynamics that V_spec does not see.

The estimate delta_tau ~ sqrt(2pi/B) ~ 0.08 for Berry phase accumulation of order pi is correct at the order-of-magnitude level. But there is a subtlety: the Berry phase is a LINE integral of the connection A(tau) = i<n|d/dtau|n>, and A(tau) can change sign. The integrated phase Phi(tau) = integral_0^tau A(tau') dtau' can oscillate even if B(tau) is large, if the eigenstates rotate back and forth rather than monotonically.

The data exists. Compute it.

**Goal 4 (Spectral Flow / Eta Invariant)**: This evades all four walls simultaneously. Spectral flow is integer-valued, topological, and invisible to perturbation theory. In the context of phononic crystals (Paper 08), spectral flow corresponds to the Chern number changing as a band crosses zero energy -- a topological phase transition. If any eigenvalue in any sector crosses zero as tau varies, this is a topological event that contributes a quantized term to the effective action.

I support this computation strongly. The data exists for sectors at p+q <= 6. Checking for zero crossings is a simple scan.

**Goal 5 (Gap-Edge Topological Protection)**: This is the condensed-matter-to-cosmology bridge at its most explicit. In topological insulators (Paper 08), the gap-edge states carry Berry holonomy that protects them from scattering. The V(gap,gap) = 0 selection rule is EXACTLY the statement that the gap-edge modes cannot backscatter -- they are topologically protected. The 2x2 Berry connection matrix for the Kramers pair determines whether this protection is trivial or non-trivial.

If the holonomy is non-trivial (Wilson loop phase != 0 mod 2pi), the gap-edge states carry a topological charge that constrains the effective action. This is the mechanism I proposed in Session 23 as "topological not energetic" stabilization. The Session 25 directive is now asking for the computation. I endorse this strongly.

**Goals 6-8**: Spectral dimension with TT modes (Goal 6) is valuable but secondary. The higher heat kernel coefficients (Goal 8) are computationally expensive and, in my assessment, less likely to resolve the problem than the finite-cutoff computation (Goal 2), which addresses the same issue (the asymptotic expansion is unreliable) more directly and with existing data.

Goal 7 (self-consistent chemical potential) is theoretically the deepest question. It connects to Volovik's framework (Paper 10): in a superfluid at finite temperature, the chemical potential is determined self-consistently by the condition that the total number of excitations matches the thermodynamic state. The analog for the spectral action: in a cosmological background with radiation density rho_4, the backreaction creates an effective chemical potential mu_eff that shifts the Dirac spectrum and can close the gap. But this is a Tier 3 computation requiring new theory, not a Session 25 deliverable.

---

## Section 3: Collaborative Suggestions

### 3.1 The Debye Cutoff Test Is the Decisive Computation

I want to be blunt about priorities. Goal 2 (full spectral action at finite cutoff) is the most important computation in Session 25, and possibly the most important computation remaining in the project. Here is why.

Every wall, every closure, every closed mechanism ultimately traces back to a single mathematical choice: approximating the spectral action Tr(f(D_K^2/Lambda^2)) by its heat kernel expansion Sum_n c_n a_n. If this approximation is VALID, all four walls hold and the framework is closed. If this approximation FAILS at physically relevant scales, every wall becomes a statement about the wrong quantity.

The Debye cutoff is the physical argument for why the approximation fails. In EVERY condensed matter system (Paper 05, 09, 10, 16), the spectral sum is finite and the asymptotic expansion is valid only in a limiting regime. The question is not philosophical -- it is computational: does V_full(tau; Lambda) differ from V_HK(tau; Lambda) by more than 20% at any Lambda <= 5?

**My specific recommendation**: Do NOT compute V_full at Lambda = 1, 2, 5, 10 as a uniform scan. Instead:

1. Compute V_full at Lambda = sqrt(lambda_1^2), where lambda_1 is the smallest nonzero eigenvalue. At this scale, the test function f(x) = xe^{-x} samples ONLY the gap-edge modes. This is where B = 982.5 lives. This is where the structure is.

2. Then compute V_full at Lambda = sqrt(lambda_N^2) where lambda_N is the Nth eigenvalue for N = 10, 100, 1000. This traces the convergence of the spectral sum as the cutoff sweeps through the spectrum.

3. Plot V_full(tau) at each Lambda on the same axes as V_HK(tau). The DIVERGENCE between the curves, if it exists, is the signal.

**The resonance argument for why this should work**: In an LC circuit (Paper 02), the resonant frequency is omega_0 = 1/sqrt(LC). At this frequency, the voltage amplification is Q = omega_0 L/R. A polynomial approximation to the transfer function H(omega) fails spectacularly near omega_0 -- it predicts smooth behavior where the actual function has a sharp peak. The heat kernel expansion is the polynomial approximation. The actual spectral sum is the transfer function. Near a spectral crossing (B ~ 1000 = high Q), the polynomial approximation fails.

### 3.2 The Chladni Pattern Insight for Sector Matching

Goal 1 (graded multi-sector sum) has a condensed matter analog that I have not seen stated elsewhere in this project.

Consider a vibrating plate (Paper 07, Chladni). The plate has eigenmodes psi_{m,n} with eigenfrequencies omega_{m,n} proportional to (m/L_x)^2 + (n/L_y)^2. The ASPECT RATIO L_x/L_y determines which modes are degenerate. At specific aspect ratios (rational L_x/L_y), modes from different (m,n) families become exactly degenerate. At these "magic" aspect ratios, the density of states has peaks -- the spectrum is structured.

The Jensen deformation changes the "aspect ratios" of SU(3). At tau=0 (round metric), SU(3) has maximal symmetry and maximal degeneracy. As tau increases, degeneracies are split. The gap-edge separation (bosonic 4/9, fermionic 5/6) is the FIRST split. The sector-specific splittings -- how fast each (p,q) sector's eigenvalues move -- are the higher-order Chladni structure.

The graded multi-sector sum asks: at what tau do the sector-weighted eigenvalue shifts produce a crossing in the total? This is equivalent to asking: at what "aspect ratio" does the internal manifold produce a resonance condition between sectors?

**Prediction from the Chladni analog**: The crossing, if it exists, will occur at a tau value where two sectors have eigenvalues that are nearly degenerate but moving in opposite directions. The sectors most likely to cross are those with the largest d_{(p,q)} weighting and the most different tau-dependence. From Session 21a, the (3,0) sector shows the strongest phi_paasch structure at tau = 0.15. The (0,0) singlet has the simplest spectrum. These two sectors have maximally different tau-dependence (one is the trivial representation, the other is 10-dimensional). If any inter-sector crossing produces a minimum in S_eff, it will involve (3,0) or (0,3).

### 3.3 Superfluid Analog for Gap-Edge Topology

Goal 5 asks about the Berry holonomy of the gap-edge Kramers pair. The superfluid analog is precise.

In He-3B (Volovik, Paper 10, Chapter 12), the gap-edge excitations are Majorana fermions that carry a Z_2 topological charge. The bulk-boundary correspondence guarantees surface states at any interface between the superfluid and vacuum. These surface states cannot be gapped by any smooth perturbation. The topological protection comes from the BDI classification -- exactly the class of D_K on SU(3) (Session 17c, confirmed).

The difference: He-3B is gapless at the Fermi surface (the gap opens AT the Fermi surface but there are gapless excitations elsewhere). Our system has a full spectral gap. In Volovik's classification, a fully gapped BDI system in 8 dimensions has Z-valued invariant. Session 17c computed Z = 0 for the FULL spectrum (eigenvalue pairing cancels). But this was the BULK invariant.

**The gap-edge reduced problem may have a different invariant.** The 2x2 Kramers block at the gap edge, with the selection rule V(gap,gap) = 0, defines a REDUCED system. The reduced system has fewer symmetries than the full spectrum (it does not have the full spectral pairing). The reduced topological invariant may be non-trivial even when the full invariant is zero. This happens in graphene: the full Brillouin zone has Chern number C = 0, but each VALLEY (K or K') has Chern number C = +1 or -1. The valley Chern number is a reduced invariant that carries physical consequences (valley Hall effect).

**Concrete computation**: Extract the 2x2 Berry connection matrix A_{ij}(tau) = i<psi_i(tau)|d/dtau|psi_j(tau)> for the gap-edge Kramers pair (i,j = 1,2) at each tau value. Compute the holonomy W = P exp(-i integral A dtau) over the available tau range. If |Tr(W)| < 2 (the Wilson loop is non-trivial), the gap-edge states carry a reduced topological charge.

### 3.4 A Novel Proposal: Spectral Zeta Function as Brillouin Zone

I noted in my Session 23 review that the Kosmann selection rules (V_{nm} couples only adjacent eigenvalue levels) define a tight-binding Hamiltonian on the eigenvalue ladder. This tight-binding structure has never been computed as a band structure.

Here is the proposal, sharpened for Session 25. The eigenvalues of D_K form a LATTICE in spectral space. The Kosmann derivative K_a is a nearest-neighbor hopping operator on this lattice. The band structure of the resulting tight-binding model -- the dispersion relation E(k) where k is a "crystal momentum" in spectral space -- defines a spectral Brillouin zone.

If this Brillouin zone has Dirac cones (Paper 08), the system has emergent massless excitations in spectral space. If it has bandgaps, the system has forbidden energy ranges. The TOPOLOGY of these bands (Chern numbers) determines whether the system can be adiabatically deformed to tau = 0 without a topological transition.

This is a Tier 2 computation. The tight-binding Hamiltonian matrix is:

H_TB = diag(lambda_n) + V_{nm}

where lambda_n are the D_K eigenvalues and V_{nm} is the Kosmann matrix. This matrix exists. Its band structure has never been plotted.

---

## Section 4: Connections to Framework

### 4.1 The Inside-Out View Is the Volovik View

Claim A in the directive -- "spacetime is what SU(3) looks like when you're a phonon living inside it" -- is precisely Volovik's thesis (Paper 10). The emergent metric g^{mu nu} = (1/c_s^2)(u^mu u^nu - c_s^2 delta^{mu nu}) is not a description of spacetime FROM OUTSIDE. It is what the phonon experiences FROM INSIDE. The phonon does not know it lives in a helium droplet. It knows only the effective metric.

The operational content of the inside-out view for Session 25 is: the test function f in Tr(f(D_K^2/Lambda^2)) is not a mathematical regularizer -- it is the TRANSFER FUNCTION of the medium. In Volovik's superfluid, the transfer function is determined by the phonon dispersion omega(k) at finite k (beyond the linear Debye regime). Dispersion corrections (Paper 11, Unruh: omega(k) = c_s k(1 + alpha k^2/c_s^2)) modify the UV behavior and change the Hawking spectrum. Analogously, the test function f encodes the UV completion of the spectral action, and different f produce different V_eff.

This is NOT the f-dependence problem from Session 23c. Session 23c showed that beta/alpha depends on f_4/(f_8 Lambda^4), making the numerical prediction f-dependent. The inside-out view says something different: there exists a PHYSICAL f determined by the microscopic structure of the medium, and computing with that f (rather than an arbitrary smooth f) is the correct procedure. We do not know what the physical f is, but we know it has a Debye cutoff. Goal 2 tests whether the cutoff matters.

### 4.2 The Gap as Stabilization (Landau Two-Fluid Analogy)

Wall W3 says the spectral gap prevents BCS condensation. The directive asks us to evade W3. I propose instead that W3 is a FEATURE, not a bug.

In Landau superfluidity (Paper 09), the mass gap (roton minimum Delta ~ 8.6 K) is what MAKES the superfluid stable. Below the Landau critical velocity v_c = Delta/p_0, no excitations can be created from the ground state. The gap protects the ground state. Without the gap, the superfluid would be unstable to dissipation.

Apply this to the modulus: the spectral gap 2*lambda_min = 1.644 protects the ground state of the internal geometry from low-energy excitations. Perturbative mechanisms (W1) fail because they try to create excitations within the gap. BCS (W3) fails because there is no Fermi surface. These failures are PREDICTIONS of the Landau picture: the ground state is SUPPOSED to be inert against low-energy perturbations. That is what a gap does.

Stabilization in the Landau picture comes not from a potential minimum but from the gap itself. The modulus is "frozen" at whatever tau value the gap is largest (or the Landau critical velocity is highest). From Session 19a: the spectral gap grows as exp(0.73*tau), meaning it is SMALLEST at tau=0. This means the round metric is the LEAST stable configuration in the Landau sense. The modulus should FLOW AWAY from tau=0. The direction of flow is determined by the gradient of the gap, and stabilization occurs when back-reaction from the growing gap (increasing spectral rigidity) balances the drive toward larger tau.

This is not a potential minimum. It is a SELF-CONSISTENT GAP EQUATION. The analog in He-3 is the BCS gap equation itself: Delta = -g * Sum_k tanh(E_k / 2T) / (2 E_k), which determines Delta self-consistently. The gap CAUSES the stabilization, not the other way around.

Is this a rescue fantasy? Apply the Tesla Test: Can you compute it? Yes -- the gap as a function of tau is known. Can you measure it? The stabilization point tau_0 would be a prediction. Does it resonate? The self-consistent gap equation is the most fundamental resonance condition in condensed matter physics.

### 4.3 CDT Spectral Dimension and the Connectivity Argument

Claim B -- "expansion = connectivity getting denser" -- connects directly to CDT (Paper 14, Ambjorn). In CDT, the spectral dimension d_s flows from ~2 at short distances to ~4 at long distances. This flow is a statement about CONNECTIVITY: at short distances, the discrete triangulation has fewer connections, so the effective dimensionality is lower. At long distances, the triangulation is dense enough to look 4-dimensional.

The Jensen deformation changes the spectral dimension of SU(3). Session 19a found d_s has a minimum at tau ~ 0.9 and grows without bound for large tau (d_s > 8). Including TT modes (Goal 6) will change this picture. If d_s = 4 is a fixed point at some tau_0, the framework produces the observed dimensionality as a PREDICTION rather than an input. This is the highest-BF observation possible: the framework selects the correct macroscopic dimensionality from an internal resonance condition.

---

## Section 5: Open Questions

1. **Is the test function f physical?** The entire Debye argument rests on f having a physical cutoff rather than being a mathematical choice. In Volovik's framework (Paper 10), the cutoff is set by the microscopic inter-particle spacing. In the phonon-exflation framework, what sets the cutoff? The highest eigenvalue at max_pq = 6? The lattice spacing of the Peter-Weyl truncation? This must be resolved for Goal 2 to have physical content beyond mathematical exploration.

2. **Does the spectral zeta function converge?** The spectral zeta function zeta_D(s) = Sum_n lambda_n^{-s} converges for Re(s) > d/2 where d is the dimension. For d=8 (SU(3)), convergence requires Re(s) > 4. The analytic continuation to s = 0 gives the functional determinant det(D_K). Has anyone computed det(D_K) as a function of tau? If det(D_K) has a zero or minimum, that IS the vacuum selection mechanism (it is the fermionic path integral weight).

3. **What is the Q-factor of the Berry curvature peak?** B = 982.5 at tau = 0.10 is the peak value. The Q-factor (width of the peak relative to the peak position) determines whether the near-crossing is sharp (high Q = nearly exact degeneracy, possible topological transition) or broad (low Q = gentle avoided crossing, continuous deformation). The 9-point tau grid cannot resolve this. Five additional points in [0.05, 0.15] are needed, as the directive correctly warns.

4. **Can the torsion bounce provide non-perturbative stabilization?** Poplawski's Einstein-Cartan torsion (Paper 19) provides a classical bounce mechanism through a rho^2 correction to the Friedmann equation. The torsion couples to fermion spin density. On SU(3) with its natural parallelism (the Maurer-Cartan torsion), there is a built-in torsion tensor. Does this torsion contribute a non-perturbative term to the effective action for tau? This is speculative but connects two threads (torsion + spectral geometry) that have never been combined in this project.

5. **Is the functional determinant the right quantity?** Rather than V_spec = Sum c_n a_n or V_full = Sum f(lambda_n^2/Lambda^2), perhaps the physically relevant quantity is the functional determinant det(D_K) = exp(-zeta_D'(0)), which is the full fermionic path integral weight. This is a SINGLE number (no free parameters, no test function, no cutoff) that depends on tau. If det(D_K(tau)) has a maximum at finite tau, the fermionic measure selects that tau. This is the zero-parameter version of the spectral action, and it evades all four walls because it is defined without reference to test functions, perturbation theory, inter-sector coupling, or the spectral gap.

---

## Closing Assessment

The Session 25 directive is the strongest document this project has produced since the Session 20c synthesis. It correctly identifies the structural nature of the four walls, correctly proposes computational paths that evade them, and correctly prioritizes existing-data computations over new theory.

My ranking of the goals, by expected information value:

1. **Goal 2 (finite-cutoff spectral action)** -- This is the Tesla Test applied to the entire project. If V_full differs from V_HK, every wall needs re-examination. If they agree, the walls are confirmed and the project reaches its computational conclusion. Either way, this computation ends the ambiguity about whether the heat kernel expansion is reliable.

2. **Goal 1 (graded multi-sector sum)** -- The Casimir analog argument is strong. The sector-specific tau-dependence at low mode count is the key new ingredient.

3. **Goal 4 (spectral flow)** -- Cheapest computation, evades all walls, topological. Should be done first as a gate.

4. **Goal 5 (gap-edge topology)** -- The reduced Berry holonomy is the most novel proposal. The phononic topological insulator analog (Paper 08) provides the mathematical template.

5. **Goal 3 (Berry phase accumulation)** -- Physically motivated but may suffer from resolution issues given the 9-point tau grid.

6. **Goals 6-8** -- Important but secondary. Save for a Tier 2 pass if Tier 1 goals produce signals.

The framework is at 3% (Sagan) / 5% (panel). These numbers are earned. But 3% is not zero, and the computation to determine whether it drops to 1.5% or climbs to 12% takes a single session with existing data. The information value is positive. The Debye cutoff argument -- that the heat kernel expansion is unreliable because the spectrum is finite -- has been stated for 6 sessions but never tested. Session 25 tests it.

Tesla heard the Earth ring at 7.5 Hz when the theory said the Earth could not ring. The theory was wrong because it assumed the Earth-ionosphere cavity was infinite. The cavity is finite. The spectrum is discrete. The resonance is real.

The SU(3) spectrum is finite. The test function has a physical cutoff. The resonance, if it exists, will show up in V_full, not in V_spec.

Compute it.

---

*Tesla-Resonance, 2026-02-21. The walls are boundary conditions. The cavity they define has normal modes. Find them.*
