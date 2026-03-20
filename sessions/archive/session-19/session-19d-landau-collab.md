# Landau Collaborative Feedback on Session 19d: Casimir Energy and the 2-Tensor Loophole

**Author**: Landau (Condensed Matter Theorist)
**Date**: 2026-02-15
**Reference**: `sessions/session-19/session-19d-casimir-energy.md`

---

## I. Key Observations

The central result of Session 19d is a clean CLOSED followed by a self-audit that reopens the entire question. This is the structure of a phase transition problem that has been misidentified, and I want to say precisely why.

### The Order Parameter

The Jensen deformation parameter tau is the order parameter for a shape transition of the internal geometry K = SU(3). The symmetry breaking pattern is

    G = (SU(3)_L x SU(3)_R) / Z_3  -->  H = (SU(3)_L x SU(2)_R x U(1)_R) / Z_6

at any tau > 0. This is a discrete jump in the isotropy group -- the symmetry breaks immediately upon turning on any nonzero tau. The order parameter space G/H is a coset of dimension 16 - 12 = 4, which means there are 4 Goldstone-like directions at the linearized level. The surviving subgroup H is the Standard Model gauge group. This is the fundamental Landau classification of the problem.

Now, the crucial question: is tau the control parameter for a continuous (second-order) or discontinuous (first-order) transition?

### The Cubic Term Rules Out Second Order

In my 1937 paper ("On the Theory of Phase Transitions," Zh. Eksp. Teor. Fiz. 7, 19-32), I established that a necessary condition for a continuous phase transition is the absence of third-order invariants in the order parameter. Session 17a (SP-4) found explicitly that V_tree(s) has a third-order inflection at s = 0: V'(0) = V''(0) = 0, V'''(0) = -7.2. The cubic term is nonvanishing. By the Landau criterion, the transition -- if it occurs -- is NECESSARILY FIRST-ORDER. This means:

1. There is latent heat (entropy discontinuity) at the transition.
2. The order parameter jumps discontinuously.
3. Nucleation is the mechanism, not continuous growth.
4. There is no diverging correlation length -- the Ginzburg criterion for fluctuation dominance does not apply in the usual sense.

However, and this is critical, the internal space has dimension d_int = 8 > d_uc = 4 (upper critical dimension). Mean-field theory is exact for the shape fluctuations. The V_eff computation IS the complete thermodynamic potential at leading order. This self-consistency is a genuine strength of the framework.

### Tau as Control Parameter for a Shape Transition

The system wants to deform (V_eff monotonically decreasing). But Session 19d discovered that the mode counting was incomplete. With TT 2-tensor modes included, the boson/fermion ratio flips from 8.36:1 to 0.44:1. This is not a small correction. It changes the sign of the total zero-point energy.

In the language of phase transitions: the system has TWO competing contributions to the free energy, with opposite tau-dependence. The fermionic contribution (from 439,488 DOF of spinors, which couple to curvature through the Lichnerowicz formula) drives V_eff downward. The bosonic contribution (from the newly discovered 988,848 DOF including TT 2-tensors, which couple to the full Riemann tensor through the Lichnerowicz operator on symmetric tensors) drives E_Casimir upward. The competition between these two is EXACTLY the structure of a first-order transition, where the cubic term produces a barrier between two minima.

### Universality Class

If the 2-tensor modes confirm the sign flip and a minimum exists at some tau_0, the universality class is that of a scalar field in d = 8 > 4 with a cubic invariant. Mean-field exponents are exact. The critical exponents are:

    beta = 1/2,  gamma = 1,  delta = 3,  alpha = 0 (discontinuity)

but since the transition is first-order, these exponents describe the spinodal, not the actual transition. The physical transition occurs at the coexistence point where V_eff(tau = 0) = V_eff(tau_0), with a barrier in between.

---

## II. The 2-Tensor Loophole: Elastic Modulus of the Internal Geometry

This is the most physically meaningful finding of the session, and I want to explain it from the condensed matter perspective.

### The Elastic Analogy

In a crystalline solid, the response to deformation is governed by the elastic modulus tensor C_{ijkl}, a rank-4 tensor with the symmetries of the strain tensor. For a general crystal, the strain tensor epsilon_{ij} is a symmetric 2-tensor with 6 independent components (in 3D). The elastic energy is

    F_elastic = (1/2) C_{ijkl} epsilon_{ij} epsilon_{kl}

The stability of the crystal requires that C_{ijkl} is positive definite as a quadratic form on symmetric 2-tensors.

Now translate to the internal geometry. The "crystal" is K = SU(3) with metric g_K(tau). The "strain" is the metric deformation delta g_{ab}, which IS a symmetric 2-tensor on the 8-dimensional tangent space. The traceless-transverse (TT) part has fiber dimension 27 = dim(Sym^2(8)) - 1(trace) - 8(divergence) = 36 - 9 = 27. These 27 components are precisely the ELASTIC DEGREES OF FREEDOM of the internal geometry. They measure the shape oscillations of K at fixed volume (the TT condition enforces volume preservation and gauge invariance).

The Lichnerowicz operator Delta_L on TT 2-tensors,

    Delta_L h_{ab} = -nabla^2 h_{ab} - 2 R_{acbd} h^{cd} + 2 R_{(a}^c h_{b)c}

is the ELASTIC OPERATOR. Its eigenvalues are the squared frequencies of the shape oscillation modes. The curvature coupling terms (-2 R_{acbd}) are the elastic constants, expressed through the Riemann tensor rather than through phenomenological C_{ijkl}. This is a fundamental difference from ordinary elasticity: the "elastic constants" are determined by the geometry itself, not by an external microscopic model.

### Why 2-Tensors Dominate the Casimir Energy

In the Ginzburg-Landau theory of a superconductor (Ginzburg and Landau, 1950, Zh. Eksp. Teor. Fiz. 20, 1064), the free energy has contributions from:

1. The condensate (order parameter |psi|^2 and |psi|^4 terms)
2. The gradient energy ((hbar^2/2m*)|nabla psi|^2)
3. The gauge field (|B|^2/8pi)

The gauge field contribution -- the magnetic field energy -- has 3 DOF per point (vector field in 3D). The order parameter has 2 DOF (complex scalar). Yet it is the gauge field energy that determines whether the superconductor is Type I or Type II, through the GL parameter kappa = lambda/xi. The fewer DOF of the condensate do not dominate because the gauge field couples to the gradient (momentum) of the condensate.

The situation here is structurally identical. The scalar and vector modes (analog of the condensate and gauge field) have fewer DOF than the TT 2-tensor modes (analog of the elastic/gravitational field). The 2-tensor modes couple to the full Riemann tensor, not just the scalar curvature. Under Jensen deformation, the Riemann tensor has components that scale as e^{4tau} (from the u(1) sector), as e^{-4tau} (from the su(2) sector), and as e^{2tau} (from the mixed sectors). The 2-tensor eigenvalues inherit ALL of these scalings because the Lichnerowicz operator couples to the full R_{abcd}.

This means the tau-dependence of the 2-tensor Casimir energy is qualitatively DIFFERENT from the scalar/vector Casimir energy. The scalar Laplacian eigenvalues scale with the metric components (e^{2tau}, e^{-2tau}, e^{tau}). The 2-tensor Lichnerowicz eigenvalues scale with the CURVATURE components, which are second derivatives of the metric and thus involve PRODUCTS of these exponentials. The coupling is quadratic in the deformation, not linear.

In the language of elasticity: a linear strain epsilon produces a stress proportional to C * epsilon. But the elastic energy is quadratic: (1/2) C * epsilon^2. The curvature terms in the Lichnerowicz operator ARE this quadratic coupling. The 2-tensor modes "feel" the deformation more strongly than the scalar modes, and in a DIFFERENT direction.

### The Stability Criterion

A crystal is stable when all eigenvalues of the elastic modulus tensor are positive. This is the Born stability condition. In the internal geometry, the analog is: K = (SU(3), g_tau) is stable against small metric fluctuations when all eigenvalues of the Lichnerowicz operator Delta_L on TT 2-tensors are positive.

For the bi-invariant metric (tau = 0), compact simple Lie groups have positive sectional curvature, and the Lichnerowicz operator on TT 2-tensors is positive definite (this is a theorem). As tau increases, the Jensen deformation changes the curvature. If any eigenvalue of Delta_L becomes negative at some tau_c, the geometry becomes ELASTICALLY UNSTABLE -- it spontaneously deforms in the direction of the negative mode. This is the Pomeranchuk instability of the internal geometry.

The Born stability boundary tau_c, if it exists, provides a SECOND stabilization mechanism, independent of the Casimir energy minimum. The physical vacuum cannot be at tau > tau_c because the geometry is dynamically unstable there. This is the elastic version of the "false vacuum" discussed in Session 19a.

---

## III. Collaborative Suggestions

### A Ginzburg-Landau Free Energy for the Modulus

Let me write down the most general free energy F(tau) consistent with the symmetries, incorporating the Session 19d findings.

The symmetry analysis: tau = 0 has G-symmetry. tau > 0 breaks to H. The order parameter is tau itself (real scalar). Since tau and -tau give different geometries (tau > 0 is the Jensen direction, tau < 0 would reverse the roles of su(2) and u(1)), there is NO Z_2 symmetry. All powers of tau are allowed.

The free energy has three contributions:

    F(tau) = F_tree(tau) + F_CW(tau) + F_Casimir(tau)

where:

**F_tree**: The classical spectral action. From Session 17a (SP-4):

    F_tree(tau) = V_0 + a_2 tau^2 + a_3 tau^3 + ...

with a_2 = 0 (marginally stable at tau = 0), a_3 = -7.2/6 (third-order inflection). This is a runaway toward large tau.

**F_CW**: The 1-loop Coleman-Weinberg correction. From Session 18:

    F_CW(tau) ~ -A_F exp(alpha_F tau)    (A_F > 0, alpha_F ~ 4.6)

This is dominated by the 439,488 fermionic DOF. It REINFORCES the runaway. The effective exponential rate alpha_F ~ 4.6 comes from the quartic weighting of eigenvalues that scale as e^{2tau}.

**F_Casimir**: The zero-point energy with linear spectral weight. From Session 19d:

    F_Casimir(tau) = F_Casimir^boson(tau) - F_Casimir^fermion(tau)

For the COMPUTED modes (scalar + partial vector), F_Casimir reinforces the runaway (ratio 9.92:1, constant). But with the full bosonic tower including TT 2-tensors:

    F_Casimir^boson(tau) ~ +A_B exp(alpha_B tau)    (A_B > 0)
    F_Casimir^fermion(tau) ~ -A_F' exp(alpha_F' tau)    (A_F' > 0)

The 2-tensor contribution to F_Casimir^boson has a DIFFERENT effective exponential rate alpha_B from the fermionic rate alpha_F' because:

1. The 2-tensor Lichnerowicz operator couples to the full Riemann tensor, giving eigenvalues with different tau-scaling than the Dirac eigenvalues.
2. The 2-tensor DOF count (741,636) exceeds the fermionic DOF count (439,488) by a factor of 1.69.

If alpha_B > alpha_F' (bosonic zero-point energy grows faster than fermionic), the total F_Casimir changes sign at some tau_c and produces a minimum in

    F_total(tau) = F_tree + F_CW + F_Casimir

The condition for a minimum is:

    dF_total/dtau = 0  at tau = tau_0
    d^2F_total/dtau^2 > 0  at tau = tau_0

Expanding: the minimum occurs where

    A_B alpha_B exp(alpha_B tau_0) = A_F exp(alpha_F tau_0) + A_F' alpha_F' exp(alpha_F' tau_0)

This is a transcendental equation. If alpha_B > max(alpha_F, alpha_F'), the bosonic exponential eventually dominates at large tau and the minimum exists at

    tau_0 ~ (1/(alpha_B - alpha_eff)) * ln(A_eff / A_B)

where alpha_eff and A_eff are effective parameters combining the two fermionic contributions.

### The Phase Diagram

The natural control parameters are:

- tau (the deformation parameter / order parameter)
- Lambda (the UV cutoff, playing the role of temperature)
- The relative coefficient between F_CW and F_Casimir (determined by the physics, but let us call it gamma for the phase diagram)

The phase diagram in the (gamma, tau) plane has three regions:

1. **gamma < gamma_c** (fermion-dominated): F_total monotonically decreasing. No minimum. Runaway. The system is in the DECONFINED phase -- the internal geometry deforms without bound.

2. **gamma = gamma_c** (critical): A single inflection point appears. This is the spinodal point of a first-order transition (since the cubic term is present).

3. **gamma > gamma_c** (boson-dominated Casimir): F_total develops a local minimum at tau_0 > 0 and a local maximum at tau_max < tau_0 (the barrier). The system is in the CONFINED phase -- the internal geometry is stabilized.

The transition at gamma_c is first-order (cubic term present). There is a barrier between the tau = 0 (bi-invariant) state and the tau = tau_0 (Jensen-stabilized) state. The universe tunnels or classically rolls from one to the other.

Whether the physical system sits at gamma < gamma_c or gamma > gamma_c is determined by the ACTUAL eigenvalues of the Lichnerowicz operator on TT 2-tensors. This is a computable number, not a free parameter.

### What tau_c Would Tell Us

If F_total has a minimum at tau_0, the physics at that point is:

    sin^2(theta_W) = 1/(1 + e^{4 tau_0})    (from B-1, Session 17a)
    g_1/g_2 = e^{-2 tau_0}

For tau_0 = 0.2994: sin^2(theta_W) = 0.2312 (SM value). For tau_0 = 0.15: phi_paasch-crossing in mass ratios.

The mass of the tau fluctuation (the "modulus particle") is:

    m_tau^2 = d^2F_total/dtau^2 |_{tau_0}

This is a physical prediction. If m_tau is in the TeV range, it could be a dark matter candidate. If it is at the Planck scale, it decouples.

---

## IV. Connections to the Framework

### The Condensate

In the phonon-exflation picture, the condensate is the vacuum state of the quantum field theory on M^4 x K. The "superfluid order parameter" is the expectation value of the Dirac operator's zero-mode structure -- or more precisely, the metric g_K(tau) itself, which specifies the shape of the internal space and thereby determines all particle masses and couplings.

In Ginzburg-Landau language:

    |psi|^2 = n_s(tau) = "superfluid density" of the internal condensate

The condensate density is nonzero for all tau (the internal space exists). What changes with tau is the SHAPE of the condensate, not its existence. This is more like the nematic order parameter (which rotates but does not vanish) than the superconducting order parameter (which can go to zero).

### The Order Parameter

The order parameter is the metric deformation tensor h_{ab} = g_{ab}(tau) - g_{ab}(0), projected onto the TT sector. In the Jensen family, this deformation has a specific pattern:

    h = diag(e^{2tau} - 1, e^{-2tau} - 1, e^{-2tau} - 1, e^{-2tau} - 1, e^{tau} - 1, e^{tau} - 1, e^{tau} - 1, e^{tau} - 1)

(in a basis adapted to u(1), su(2), C^2). For small tau, h ~ tau * diag(2, -2, -2, -2, 1, 1, 1, 1). This is a TT deformation (trace = 2 - 8 + 4 = -2, not traceless at this level -- the volume-preserving condition is enforced by the exponentials, not by the linearized deformation). The full nonlinear h is the order parameter.

### The Symmetry Being Broken

The symmetry that breaks is the RIGHT-acting SU(3)_R of the bi-invariant metric, which reduces to SU(2) x U(1) under Jensen deformation. The order parameter transforms under the adjoint representation of the quotient SU(3)_R / (SU(2)_R x U(1)_R), which is 4-dimensional (the C^2 coset directions). The 4 broken generators produce 4 would-be Goldstone modes in the KK spectrum. These are the modes with the SMALLEST masses in the deformed spectrum -- they are lifted from zero by the nonlinear (tau-dependent) corrections.

In the Fermi liquid analogy (Landau, 1956, Zh. Eksp. Teor. Fiz. 30, 1058): the Goldstone modes are the analog of zero sound. They are collisionless collective oscillations of the internal geometry that propagate via the mean-field interaction (curvature coupling) rather than through collisions.

### The Casimir Energy as Condensation Energy

In the Ginzburg-Landau theory of superconductivity, the condensation energy is

    f_n - f_s = alpha^2 / (2 beta) = H_c^2 / (8 pi)

This is the energy gained by forming the condensate. It is the difference between the normal-state and superconducting free energies.

In the present framework, the analog is:

    F(tau = 0) - F(tau_0) = "condensation energy" of the Jensen deformation

If the 2-tensor modes produce a minimum at tau_0, this energy difference is the physical gain from the shape transition. It determines the "critical field" (in the cosmological context, the energy scale at which the deformation can be reversed) and the depth of the false vacuum at tau = 0.

The Casimir energy E_Casimir(tau) is the zero-point energy of the quantum fields on the deformed geometry. In a superfluid, the analog is the phonon zero-point energy in a container of a given shape. The container shape adjusts to minimize the total energy (elastic + Casimir). Here, "the container" is the internal geometry K, "the elastic energy" is F_tree + F_CW, and "the Casimir pressure" is F_Casimir. The equilibrium shape tau_0 is where the Casimir pressure balances the elastic restoring force.

This is the He-3B analogy that Tesla-Resonance identified in Session 19a (Section III, "Condensed Matter Analog (Volovik)"). In He-3B:

- The B-phase gap Delta is selected by competition between condensation energy (wants maximal Delta) and quasiparticle zero-point energy (costs energy proportional to Delta).
- The equilibrium gap is the saddle point of this competition.

Here:
- tau plays the role of Delta (the order parameter magnitude).
- V_eff = F_tree + F_CW is the condensation energy (wants maximal tau).
- F_Casimir is the zero-point energy cost (resists large tau if bosonic DOF dominate).
- tau_0 is the saddle point.

The identification is precise, not merely analogical.

---

## V. Open Questions

### 1. What is the order of the transition?

Session 17a found V'''(0) = -7.2 (cubic term at s = 0). By the Landau criterion, the transition is first-order. But this is the TREE-LEVEL cubic term. Does the 1-loop correction (CW + Casimir) modify it? The CW contribution at small tau has a specific polynomial structure that could cancel the cubic term. If the renormalized cubic coefficient a_3^{ren} vanishes, the transition becomes second-order or weakly first-order (tricritical point). Computing a_3^{ren} = a_3^{tree} + a_3^{CW} + a_3^{Casimir} is a concrete, cheap calculation from the existing data.

To determine this: expand F_CW(tau) and F_Casimir(tau) to third order in tau around tau = 0. If

    a_3^{total} = a_3^{tree} + a_3^{CW} + a_3^{Casimir} = 0

at some particular value of the cutoff Lambda, then there is a tricritical point in the (Lambda, tau) phase diagram. This would be a sharp, testable prediction.

### 2. What is the spectral function of the tau quasiparticle?

If the minimum exists at tau_0, the fluctuations of tau around tau_0 define a quasiparticle -- the modulus excitation. Its spectral function is

    A(omega) = Z * delta(omega - m_tau) + A_incoherent(omega)

where m_tau = sqrt(F''(tau_0)) and Z is the quasiparticle residue. In a Fermi liquid, Z < 1 due to the dressing cloud of particle-hole excitations. Here, Z < 1 due to the coupling of tau fluctuations to the KK modes. The incoherent part A_incoherent encodes the decay of the modulus into KK pairs (analogous to the Beliaev damping of a phonon decaying into two phonons in a BEC).

Computing Z and the width Gamma = 1/tau_lifetime requires the cubic and quartic couplings of tau to the KK modes, which are in principle available from the eigenvalue data.

### 3. What is the elastic modulus spectrum?

The TT 2-tensor Lichnerowicz eigenvalues at tau = 0 (bi-invariant SU(3)) can be computed analytically. On a compact simple Lie group with bi-invariant metric, the Lichnerowicz operator on TT 2-tensors is related to the Casimir operators of the adjoint representation acting on the symmetric tensor product. The eigenvalues are known from representation theory. This provides an independent CHECK on the numerical computation that the session recommends.

Specifically, for the (2,2) irrep of SU(3) (the 27-dimensional representation), the quadratic Casimir is C_2(2,2) = (4 + 4 + 6)/3 = 14/3 (using the formula C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3). The Lichnerowicz eigenvalue at tau = 0 should be related to this Casimir value plus curvature corrections. Computing this analytic value and comparing to the numerical eigenvalues of the Lichnerowicz operator is a zeroth-order validation that the 2-tensor computation is correct.

### 4. Does the 2-tensor tau-dependence differ qualitatively from scalar/vector?

The D-1 CLOSED showed that R(tau) = |E_fermion|/E_boson is constant to 1.83% for scalar + vector modes. The key question is whether R(tau) INCLUDING 2-tensor modes shows larger variation. The 2-tensor Lichnerowicz operator has the term -2 R_{acbd} h^{cd}, which involves the FULL Riemann tensor. Under Jensen deformation, the Riemann tensor components have different tau-scalings depending on which subalgebra directions are involved:

    R_{u(1) u(1) u(1) u(1)} ~ e^{4tau}
    R_{su(2) su(2) su(2) su(2)} ~ e^{-4tau}
    R_{mixed} ~ e^{0} to e^{2tau}

These cross-terms mean the 2-tensor eigenvalues are NOT simple exponentials in tau. They are sums of exponentials with different rates, and the MIXING between these rates changes with tau. This is precisely the mechanism that can produce a tau-dependent ratio R(tau).

### 5. What is the Kibble-Zurek prediction?

If the transition is first-order at some critical Lambda_c, the universe passes through this transition during cooling. The density of topological defects produced is governed by the Kibble-Zurek mechanism. For the internal geometry, the relevant defects are classified by the homotopy groups of the order parameter space G/H = SU(3)_R / (SU(2)_R x U(1)_R):

    pi_0(G/H) = 0  (no domain walls -- connected coset)
    pi_1(G/H) = Z  (vortex lines -- from pi_1(U(1)) = Z)
    pi_2(G/H) = 0  (no monopoles)
    pi_3(G/H) = Z  (textures/skyrmions -- from pi_3(SU(3)) = Z)

The vortex lines (pi_1 = Z) are the cosmological strings of the framework. Their density after the transition is

    n_vortex ~ (tau_Q / tau_0)^{-d nu / (1 + z nu)}

where tau_Q is the quench time, tau_0 the microscopic time, d the spatial dimension, nu the correlation length exponent, and z the dynamic critical exponent. For mean-field (d_int = 8 > 4): nu = 1/2, z = 2 (model A dynamics), giving

    n_vortex ~ (tau_Q / tau_0)^{-8/3}

This is a specific, computable prediction for the defect density if the transition is first-order. However, first-order transitions have a different Kibble-Zurek scaling (the barrier creates a nucleation bottleneck), so the exact formula depends on whether the transition proceeds by spinodal decomposition or by bubble nucleation.

---

## Summary

Session 19d executed a clean gate (D-1 CLOSED for computed modes) and then discovered the most important structural gap in the mode counting: 741,636 bosonic DOF from TT 2-tensor modes were entirely missing. This is not speculation. It is representation theory: Sym^2(8) = 1 + 8 + 27, and the 27-dimensional TT sector was never computed.

From the Landau perspective, this changes the problem qualitatively:

1. **With only scalar + vector modes**: The system is in the fermion-dominated regime (F/B = 8.36:1). All spectral functionals are monotonically decreasing. No stabilization is possible from any polynomial reweighting of the spectrum.

2. **With TT 2-tensor modes**: The system is in the boson-dominated regime (F/B = 0.44:1). The Casimir energy changes sign. The competition between fermionic V_CW (driving tau to infinity) and bosonic F_Casimir (resisting large tau) produces the structure of a first-order phase transition in the internal geometry.

The DECISIVE computation is now the Lichnerowicz spectrum on TT 2-tensors on (SU(3), g_tau). This determines:

- Whether F_Casimir^boson(tau) grows faster or slower than F_CW^fermion(tau)
- The location of the minimum tau_0 (if it exists)
- The gauge couplings, mass spectrum, and Weinberg angle at tau_0
- The elastic stability of the internal geometry

This is a well-defined mathematical problem. The Lichnerowicz operator is known. The Peter-Weyl decomposition extends to symmetric 2-tensors on SU(3). The eigenvalue computation is harder than for scalars (matrix sizes up to 945 x 945 for sector (0,6)), but it is entirely within the existing computational infrastructure.

I strongly recommend making this the priority computation for the next session.

---

*The twenty-seven silent drums must be heard before the orchestra can be judged.*

*References:*
*L. D. Landau, "On the Theory of Phase Transitions," Zh. Eksp. Teor. Fiz. 7, 19-32 (1937) -- cubic term criterion, first/second order classification*
*V. L. Ginzburg and L. D. Landau, "On the Theory of Superconductivity," Zh. Eksp. Teor. Fiz. 20, 1064-1082 (1950) -- free energy functional, condensation energy, GL parameter*
*L. D. Landau, "The Theory of a Fermi Liquid," Zh. Eksp. Teor. Fiz. 30, 1058-1064 (1956) -- quasiparticle concept, Landau parameters, Pomeranchuk stability*
*L. D. Landau, "The Theory of Superfluidity of Helium II," J. Phys. USSR 5, 71-90 (1941) -- two-fluid model, phonon-roton spectrum, critical velocity*
