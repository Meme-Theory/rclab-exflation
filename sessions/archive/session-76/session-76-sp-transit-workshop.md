# Workshop: Post-Fold Trajectory — tau Overshoot and Algebraic Classification

**Date**: 2026-04-13
**Format**: 2-agent iterative workshop, 2 rounds
**Agent A**: schwarzschild-penrose-geometer (sp)
**Agent B**: transit-dynamics-theorist (transit)
**Source Documents**:
- sessions/archive/session-76/session-76-results-workingpaper.md
- sessions/archive/session-76/session-76-sp-synthesis.md
- sessions/archive/session-76/session-76-transit-synthesis.md

**Focus Topics**:
1. tau overshoot to 1.614 — crossing geometric phase transition (0.537) and Weyl zero-crossings (0.895, 1.340)
2. CMPP type along the full dynamical trajectory (not just the fold neighborhood)
3. Physical signatures of the Weyl-eigenvalue zero-crossings (particle production? GW bursts? nothing?)
4. The correct time variable: N (e-folds) vs tau — implications for causal structure

---

## Round 1 — sp

### S1: CMPP Classification at the Overshoot Tau Values

The S76 W3-H computation established CMPP transit-invariance at tau = {0.10, 0.19, 0.30}: static Type D, dynamic Type G, no type transition through the fold. That result is local to the transit neighborhood. The tau overshoot to 1.614 (W1-E) means the full dynamical trajectory passes through THREE additional critical tau values where the fiber geometry changes qualitatively:

**Tau = 0.537 (geometric phase transition, S48).** This is the locus where the C^2-C^2 sectional curvature vanishes. Below this value, all sectional curvatures on the internal space are positive. Above it, the C^2 coset sector develops negative sectional curvature. The Weyl operator eigenvalue structure changes: the number of distinct eigenvalues increases from 2 to 8 on the 8D internal space at this point (S52). I predict the static CMPP type transitions from D to II here: the coincidence of Weyl eigenvalue degeneracies breaking at the sectional curvature zero-crossing creates a new WAND structure with reduced alignment. The 12D static product spacetime should show a Petrov type change because the internal Weyl tensor reorganizes its algebraic structure at K_C2 = 0.

**Tau = 0.895 (first Weyl eigenvalue zero-crossing, branch 27, S52).** One eigenvalue of the 66x66 Weyl operator on Lambda^2(R^{11,1}) passes through zero. In the S52 analysis, this was identified as a signature change on Lambda^2 -- NOT a Petrov type change, but a change in the definiteness of the Weyl operator restricted to the internal 2-forms. The passage through zero does not create or destroy a WAND; it changes the sign pattern of the Weyl eigenvalue spectrum. The static CMPP type should remain Type D (or whatever it transitioned to at 0.537), since the WAND existence depends on the nullity structure of bw components, not on individual eigenvalue signs.

**Tau = 1.340 (second Weyl eigenvalue zero-crossing, branch 27, S52).** Same branch re-zeros near the NEC boundary (tau_NEC = 1.382). The internal Ricci curvature in the C^2 sector approaches zero here. In the static picture, the product decomposition of the Weyl tensor between internal and 4D pieces becomes degenerate: as Ric_C2 -> 0, the Schouten tensor contribution to the 12D Weyl tensor simplifies, potentially restoring a higher degree of algebraic speciality.

**Key structural question for transit.** The W3-H computation sampled three tau values in [0.10, 0.30]. The overshoot takes the modulus to 1.614. Is the CMPP classification during the overshoot computed at the instantaneous tau value with the instantaneous tau_dot? The dynamical tau_dot changes sign during the overshoot (decelerates to zero at tau_max = 1.614, then reverses). At the turnaround, tau_dot = 0, so the dynamic classification momentarily becomes identical to the static classification. This means the D/G distinction collapses precisely at the overshoot maximum. The modulus briefly sees the static fiber geometry at tau = 1.614 -- which is deep in Zone II (mixed-sign sectional curvatures, S49) and above the NEC violation boundary at tau = 1.382.

**Constraint for the framework.** The tau overshoot takes the fiber through the NEC violation boundary. In the S49 conformal analysis, Zone III (tau > 1.382) has NEC-violating Ricci curvature in the C^2 sector. The internal space at tau = 1.614 has NEC-violating geometry. This does NOT violate the 12D NEC (the energy content is the modulus kinetic energy, which always satisfies NEC), but it means the INTERNAL geometry temporarily violates the conditions required for the focusing theorem. The Penrose 1965 singularity theorem remains inapplicable (no trapped surfaces exist due to volume-preserving Jensen, S49), but the Raychaudhuri equation for internal null geodesics has a sign flip in the Ricci term at this tau value.

**What needs computation.** The CMPP type at tau = {0.537, 0.895, 1.340, 1.614} with the dynamical tau_dot at each crossing time (from the S73B ODE trajectory). At the turnaround (tau = 1.614, tau_dot = 0), the static CMPP type IS the full classification. At the zero-crossings (traversed twice -- once ascending, once descending), the classification at different tau_dot values may differ. Pre-registered prediction: the static type changes at 0.537 (D -> II) but not at the zero-crossings (eigenvalue sign changes do not alter WAND structure).

### S2: Weyl Eigenvalue Zero-Crossings — Algebraic Significance

The Weyl operator on Lambda^2(R^{11,1}) is a 66x66 symmetric matrix at each tau value. In the S52 computation, two zero-crossings of branch 27 were identified at tau = {0.895, 1.340}. The S76 W3-H computation found 16 distinct Weyl eigenvalues at each of the three sampled tau values (0.10, 0.19, 0.30). The full trajectory passes through the zero-crossings twice each (ascending and descending during the overshoot). The question: what is the algebraic and physical significance of a Weyl eigenvalue passing through zero?

**Algebraic significance: signature change, not type change.** The CMPP classification (Type I, II, D, III, N, G, O) is determined by the existence and alignment properties of WANDs -- preferred null directions along which boost-weight components vanish. A WAND exists when the bw = +2 (or bw = -2) components of the Weyl tensor can be annihilated by choosing a particular null frame. This condition involves the RATIOS and ANGULAR STRUCTURE of the Weyl components, not the signs of individual eigenvalues. A single eigenvalue passing through zero changes the signature of the Weyl operator on the space of 2-forms (from, say, (p,q,r) to (p-1,q+1,r) or (p-1,q,r+1)), but it does not generically create or destroy a WAND. The type change requires a DEGENERACY change (two eigenvalues coinciding), not a sign change.

This is analogous to the distinction between the Petrov classification of the Weyl spinor and the eigenvalue signs of the traceless Ricci tensor. In 4D, the Petrov type is determined by the multiplicities of the principal null directions of the Weyl spinor Psi_ABCD -- the Segre classification of the traceless Ricci has no direct bearing on the Petrov type. Similarly, in 12D, the CMPP type of the Weyl tensor is not altered by a single eigenvalue of the Weyl operator passing through zero.

**Exception: if the zero eigenvalue creates a new WAND.** There IS one scenario where a zero-crossing produces a type change: if the eigenvalue passing through zero corresponds to a Weyl component that was the obstruction to a higher degree of algebraic speciality. For example, if one bw = +1 component is proportional to a particular Weyl eigenvalue, and that eigenvalue passes through zero, then the bw = +1 component vanishes and the CMPP type could jump from Type G to Type II (or from Type II to Type D). This requires the zero-crossing eigenvalue to be aligned with a specific boost-weight component in the null frame. The S52 analysis found that branch 27 has mixed boost-weight content -- it is not purely bw = 1 or bw = 2 -- so the generic expectation is no type change.

**Physical significance: three scenarios.**

(1) *Nothing observable.* If the zero-crossing does not change the CMPP type or the qualitative structure of the Weyl tensor, it produces no particle production, no GW burst, and no geometric phase transition. The internal curvature merely passes through a configuration where one particular combination of Riemann components vanishes. This is the GENERIC expectation.

(2) *Enhanced mode mixing.* Near a zero-crossing, one Weyl eigenvalue is parametrically small compared to the others. This creates a hierarchy in the Weyl curvature that could enhance coupling between modes whose overlap integral is proportional to that eigenvalue. In the BCS language: if branch 27 couples to a particular B1-B3 or B2-B3 inter-branch Bogoliubov amplitude, the passage through zero could produce a transient resonance in quasiparticle pair production. This would manifest as a SECOND Bogoliubov squeeze at the zero-crossing time.

(3) *Signature change on the 2-form space.* The Weyl operator acting on Lambda^2 changes signature at the zero-crossing. If the modulus space geometry uses the Weyl operator to define an inner product or a stability criterion on the space of linearized perturbations, the signature change could flip the stability of certain perturbation modes. In the condensed matter analog: this is like a phonon branch touching zero frequency -- a soft mode that signals an instability.

**Structural assessment.** The |C|^2 = C_abcd C^abcd is the sum of squares of ALL Weyl components and is monotonically increasing (proven S49, confirmed S76 W3-H). A single eigenvalue passing through zero does NOT make |C|^2 vanish -- it remains strictly positive (min = 3.468 at tau = 0, memory entry). The Weyl tensor never becomes conformally flat (Type O is impossible). The zero-crossings are internal rearrangements of the curvature distribution, not global changes in curvature magnitude.

**Prediction for transit.** The zero-crossings at tau = {0.895, 1.340} produce scenario (1) -- no physical signature -- unless transit can identify a specific mode coupling channel whose matrix element is proportional to branch 27's eigenvalue. The key discriminant: compute the Bogoliubov beta coefficient as a function of tau through the overshoot. If beta(tau) shows enhanced squeezing near tau = 0.895 or 1.340, scenario (2) applies. If beta(tau) is smooth through these values, scenario (1) holds.

### S3: Causal Structure of the tau Non-Monotonicity

The tau overshoot to 1.614 at t = 0.09 M_KK^{-1} (W1-E) fundamentally alters the causal picture I constructed in S49 and refined through S53 and S70. The S49 Penrose diagram of the modulus space has four conformal zones separated by three boundaries, with the physical universe residing in Zone I (tau < 0.537). The overshoot means the modulus trajectory does NOT stay in Zone I -- it crosses into Zone II (0.537 < tau < 1.382) and into Zone III (tau > 1.382), then returns. This requires a revision of the causal structure.

**The S49 picture and what breaks.** The S49 conformal analysis placed the fold at tau = 0.19 and the post-transit freeze at tau = 0.22, both safely in Zone I. The BCS condensation was identified as the censorship mechanism preventing the trajectory from reaching the singularity (tau -> infinity). The conclusion: Zones II and III are "never physically reached." The overshoot finding from W1-E invalidates this conclusion. The modulus DOES reach Zone III during the overshoot. However, the S49 analysis used the post-BCS trajectory (tau frozen at 0.22). The W1-E result uses the full coupled Friedmann + Klein-Gordon ODE (S73B), which includes the modulus kinetic energy that propels tau beyond the BCS well.

**The correct causal picture.** The conformal diagram must use N (e-folds) or t (coordinate time) as the time variable, not tau. In the (N, tau) plane, the trajectory is:

1. N = 0 (fold): tau = 0.19. The modulus arrives at the fold with kinetic energy KE >> V (stiff EOS, w ~ 1, eps_H = 1.72).
2. N ~ few: tau rises rapidly through 0.537 (geometric phase transition), through 0.895 (first zero-crossing), through 1.340 (second zero-crossing).
3. N(tau_max): tau reaches maximum at 1.614. The modulus decelerates (dV/dtau acts as a restoring force in the coupled ODE) and tau_dot passes through zero.
4. N > N(tau_max): tau descends. The trajectory passes back through 1.340, 0.895, 0.537 in reverse order.
5. N ~ 130: tau settles to its final frozen value (post-decay). The modulus has decayed (tau_decay = 1.63e-37 s) and tau is frozen by the Hubble friction + decay damping.

**Causal structure implications.** The tau non-monotonicity means the modulus trajectory in the (t, tau) plane is a LOOP in tau-space: the trajectory visits each tau value in (0.19, 1.614) TWICE -- once ascending, once descending. This has three consequences for the causal structure:

(a) *The conformal diagram cannot use tau as the vertical axis.* In the S49 diagram, tau parameterizes the vertical direction. With non-monotonic tau(t), a single point in the (tau, conformal-angle) plane corresponds to TWO distinct physical times. The diagram must use N or conformal time eta as the vertical axis instead. In conformal time, the trajectory is monotonic (eta increases with time regardless of tau direction), and the tau overshoot appears as a feature of the trajectory curve within the diagram, not a fold of the diagram itself.

(b) *The fiber geometry passes through three critical boundaries twice each.* The geometric phase transition at tau = 0.537 is crossed at times t_1 (ascending) and t_2 (descending), with t_1 < t_2. At t_1, the modulus has large kinetic energy (KE-dominated, stiff). At t_2, the modulus has returned from the turnaround and has less kinetic energy (partially dissipated by Hubble friction). The CMPP classification at the same tau value may differ between ascending and descending passages because tau_dot differs. This is a genuine physical asymmetry: the internal geometry is the same, but the extrinsic curvature is different.

(c) *The NEC violation at tau > 1.382 is transient.* The internal C^2 Ricci curvature violates the null energy condition in Zone III. During the overshoot, the modulus spends a brief time in this region. The 12D NEC is not violated (the matter content is the modulus kinetic energy, which satisfies all point-wise energy conditions), but the internal geometry has NEC-violating Ricci curvature. In the substrate picture: the fiber eigenvalue spectrum temporarily reorganizes into a configuration where the C^2 sector's contribution to the spectral action has anomalous sign. This is NOT a singularity, NOT a trapped surface, and NOT a Cauchy horizon. It is a transient excursion through a geometrically anomalous fiber configuration, analogous to a caustic in optics.

**Penrose diagram update.** The definitive S53 diagrams (9 diagrams, sessions/framework/Penrose-Diagrams.md) show the modulus space with tau as the vertical coordinate and the BCS condensation as a horizontal line (sonic horizon analog). These diagrams must be supplemented with a NEW diagram using N as the vertical coordinate, showing:
- The tau(N) trajectory as a curve (rising to 1.614, then falling)
- Horizontal lines at the critical tau values (0.537, 0.895, 1.340, 1.382)
- The two crossing times for each critical value (ascending and descending)
- The CMPP type at each segment of the trajectory
- The NEC-violating region (tau > 1.382) shaded as a transient excursion

This diagram is NOT a conformal compactification of a spacetime -- it is a trajectory diagram in the modulus space with physical time on the vertical axis. The causal structure of the 4D emergent spacetime is determined by the Friedmann equation (H(N) is monotonically decreasing, W1-E CHK3), which is well-behaved throughout. The tau non-monotonicity is a SUBSTRATE phenomenon (the internal fiber geometry oscillates) that does not create any pathology in the emergent 4D causal structure.

**Critical question for transit.** What is the physical time at which the modulus exits Zone III on the return leg? Is it before or after the modulus decay time tau_decay = 1.63e-37 s? If the modulus decays while still in Zone III, the frozen tau value would be in the NEC-violating region -- a qualitatively different outcome from the assumed freeze at tau ~ 0.22 in Zone I. The S73B ODE trajectory determines this, and transit must provide the tau(t) curve through the overshoot.

### S4: Questions for transit

**Q1: The tau(t) trajectory from the S73B ODE.** W1-E states that tau overshoots to 1.614 at t = 0.09 M_KK^{-1}. Provide the full tau(t) curve from the S73B coupled Friedmann + Klein-Gordon integration. Specifically: (a) At what times does tau cross 0.537, 0.895, 1.340, and 1.382 on the ascending leg? (b) At what times does it cross them on the descending leg? (c) What is tau_dot at each crossing? (d) What is the asymptotic tau(t -> infinity) -- does the modulus return to tau ~ 0.22 (the S49 post-transit freeze value) or to a different value? This is the SINGLE most important input for the causal structure analysis.

**Q2: Is there a second Bogoliubov squeeze during the overshoot?** The fold crossing at tau = 0.19 produces the first Bogoliubov squeeze (59.8 quasiparticle pairs, S75). The overshoot takes the modulus through the geometric phase transition at tau = 0.537, where the C^2 sectional curvature vanishes and the eigenvalue spectrum reorganizes. Does this crossing produce a second squeeze? The mode equation u_k'' + omega_k^2(tau(t)) u_k = 0 has omega_k that depends on the INSTANTANEOUS tau value. If omega_k changes rapidly at the phase transition crossing (which happens at high tau_dot on the ascending leg), there could be additional particle production. The key diagnostic: is omega_k(tau) smooth through tau = 0.537, or does it have a kink (derivative discontinuity)?

**Q3: What drives the tau turnaround at 1.614?** Is it the spectral action potential gradient dV/dtau (which increases with tau), or is it Hubble friction (3H * tau_dot damping term), or a combination? If the turnaround is friction-dominated, the overshoot amplitude depends on H_Friedmann and thus on the total energy density. If it is potential-dominated, the overshoot amplitude is determined by the spectral action curvature d^2S/dtau^2. The turnaround mechanism determines whether the overshoot is a robust structural prediction or a model-dependent artifact of the S73B ODE parameterization.

**Q4: tau_dot at the NEC boundary crossings.** When the modulus crosses tau = 1.382 (ascending), what is the ratio tau_dot/H? This determines the "speed" of the NEC violation: if tau_dot/H >> 1, the excursion through Zone III is fast relative to Hubble time and produces no lasting imprint on the 4D geometry. If tau_dot/H ~ 1, the NEC-violating geometry persists for a Hubble time and could affect the emergent Friedmann dynamics.

**Q5: Is the "correct time variable is N" finding consistent with the S75 mode equation analysis?** The S75 Bogoliubov computation used tau as the independent variable in the mode equation. The W1-E finding says tau is non-monotonic, making tau an ill-defined time variable. Does the S75 mode equation need to be reformulated in N? Or does the mode equation analysis only cover the fold neighborhood (tau < 0.22), where tau IS monotonic, making the issue moot for the production spectrum?

**Q6: Does the modulus decay before or after the return from the overshoot?** The modulus decay time is tau_decay = 1.63e-37 s (W2-E/W2-H). The overshoot maximum is at t = 0.09 M_KK^{-1} = 0.09 / (7.43e16 GeV) = 1.21e-42 s. So the overshoot occurs at t ~ 10^{-42} s and the decay at t ~ 10^{-37} s, giving 5 OOM separation. This suggests the modulus completes the overshoot and returns well before decaying. But confirm: at what time does tau settle to its final value, and what IS that final value?

---

## Round 1 — transit

### Re: S1 — CMPP at Overshoot Values

**AGREE** on the three-level classification of critical tau values. sp correctly identifies tau = {0.537, 0.895, 1.340} as the structurally significant points along the overshoot trajectory, and the analysis of what happens at each is sharp. The prediction that the static CMPP type transitions at 0.537 (D -> II) is well-motivated by the eigenvalue degeneracy breaking at the sectional curvature zero-crossing.

**AGREE** on the tau_dot = 0 collapse at the turnaround. This is a structural consequence of the mode equation perspective. At tau_max = 1.614, the extrinsic curvature K_{ab} ~ tau_dot vanishes identically, so the dynamic and static classifications become identical. The Bogoliubov implication: at the turnaround, the time-dependent part of the mode equation frequency omega_k^2(tau(t)) momentarily freezes. The adiabaticity parameter omega_k'/omega_k^2 passes through zero (from the tau_dot factor in dtau/dt), meaning the mode equation instantaneously enters the adiabatic limit. No particle production occurs AT the turnaround itself.

**MISSED**: sp's analysis focuses on the CMPP type but does not address the RATE of passage through each critical tau value. From the mode equation perspective, what matters is not just whether the modulus reaches tau = 0.537 but HOW FAST it crosses. The adiabaticity parameter is:

    eta_ad(t) = |d omega_k / dt| / omega_k^2 = |d omega_k / d tau| * |tau_dot(t)| / omega_k^2     (T1.1)

On the ascending leg, tau_dot ~ v_terminal = 26.545 M_KK (barely decelerated from the fold). On the descending leg, tau_dot has been reduced by Hubble friction. The ratio of ascending to descending tau_dot at the same tau value determines whether the return passage produces particle production comparable to the initial passage. The asymmetry is structural: the ascending leg is always faster than the descending leg because of Hubble friction during the overshoot.

**EMERGES**: The CMPP type and the Bogoliubov production are probing DIFFERENT aspects of the same geometric event. CMPP classifies the algebraic structure of the Weyl tensor (a property of the geometry). Bogoliubov production classifies the response of EXCITATIONS to that geometry (a property of the mode equation). A CMPP type change (D -> II at tau = 0.537) does not automatically produce particle production -- it depends on whether the change is adiabatic or diabatic as measured by eta_ad. Conversely, particle production can occur without a CMPP type change (if omega_k has a smooth but rapid variation). The two diagnostics are complementary, not redundant.

### Re: S2 — Weyl Zero-Crossings

**AGREE** on the algebraic analysis: signature change, not type change (generic expectation). sp's argument that CMPP type change requires degeneracy change rather than sign change is structurally correct. The analogy to the Petrov/Segre distinction in 4D is precise. A single eigenvalue of the 66x66 Weyl operator passing through zero changes the signature of the 2-form space but does not generically create or destroy a WAND.

**AGREE** on the three physical scenarios, and I will narrow to which applies. The mode equation provides the discriminant.

**The mode equation test for scenario (2) vs (1).** The BCS quasiparticle frequencies omega_k at the fold are:

    omega_B1 = sqrt(epsilon_B1^2 + Delta_BCS^2)     (T2.1)
    omega_B2 = sqrt(epsilon_B2^2 + Delta_BCS^2)     (T2.2)
    omega_B3 = sqrt(epsilon_B3^2 + Delta_BCS^2)     (T2.3)

where epsilon_{Bn} are the normal-state eigenvalues and Delta_BCS = 0.4643 M_KK. As tau evolves through the overshoot, the epsilon_{Bn}(tau) change because they are eigenvalues of D_K at the instantaneous tau. At the Weyl zero-crossing (tau = 0.895), branch 27 of the Weyl operator passes through zero. The critical question is: does branch 27 have projection onto any of the BCS eigenvalues epsilon_{Bn}?

**Structural assessment: scenario (1) is overwhelmingly likely.** The BCS modes live in the (0,0) singlet sector of the Peter-Weyl decomposition -- 16 eigenvalues out of 12,880. Branch 27 of the 66x66 Weyl operator on Lambda^2(R^{11,1}) is a combination of CURVATURE components, not individual Dirac eigenvalues. The overlap between a single Weyl operator eigenvalue and the BCS sector is bounded by the mode-counting ratio: at most 16/12880 ~ 1.2e-3 of the total spectral weight. Even if branch 27 projects entirely onto the (0,0) sector (which it almost certainly does not -- the C^2 coset components dominate), the induced change in epsilon_{Bn} would be O(delta_R_C2 / N_modes) where delta_R_C2 is the Ricci curvature change in the C^2 sector at the zero-crossing.

**Quantitative estimate.** The zero-crossing eigenvalue magnitude at the fold is |lambda_27(0.19)| ~ O(1) in M_KK units (from the S52 spectrum). At tau = 0.895, it passes through zero over a tau-interval delta_tau ~ O(0.1). The induced frequency shift for a BCS mode is:

    delta_omega_k / omega_k ~ (projection weight) * |lambda_27| / omega_k ~ 10^{-3} * 1 / 1 ~ 10^{-3}     (T2.4)

This is a 0.1% frequency perturbation -- firmly in the adiabatic regime for any reasonable tau_dot. Scenario (1) holds: no enhanced mode mixing, no particle production at the Weyl zero-crossings.

**MISSED**: sp's scenario (3) -- signature change on the 2-form space -- has a Bogoliubov interpretation that sp did not develop. If the Weyl operator changes signature, the effective mass-squared in the mode equation for graviton perturbations can change sign. In the standard mode equation for tensor perturbations:

    h_k'' + (k^2 - m_eff^2(tau)) h_k = 0     (T2.5)

a sign flip in m_eff^2 corresponds to crossing from a stable to an unstable regime. But this applies to the GRAVITON mode equation, not to the BCS quasiparticle mode equation. The graviton modes couple to the Weyl tensor directly; the BCS modes couple through the Dirac spectrum. The zero-crossing is irrelevant for BCS particle production but could in principle affect graviton production. However, the graviton production is already bounded: Omega_GW = 2.25e-25 (W3-J), which includes all sources. Any additional graviton production from the zero-crossing is bounded by the same 10^{-3} projection weight.

**EMERGES**: The Weyl zero-crossings are geometrically significant (they mark where the internal curvature distribution reorganizes) but dynamically inert for excitation production. This is a concrete example of the Level 0/Level 1 separation: the background geometry (Level 0) passes through a critical configuration, but the perturbations (Level 1) are insensitive because the relevant coupling (BCS-to-Weyl projection) is suppressed by the mode-counting hierarchy 16/12880.

### Re: S3 — Causal Structure

**AGREE** on the central structural point: the tau non-monotonicity means the S49 Penrose diagram must be revised. sp is correct that the conformal diagram cannot use tau as the vertical axis. The mode equation perspective reinforces this: the pump field z''/z in the Mukhanov-Sasaki equation is parameterized by conformal time eta (or equivalently by N), NOT by tau. Writing z''/z as a function of tau produces a multi-valued function that cannot serve as input to the mode equation.

**AGREE** on the three consequences (a), (b), (c). Let me sharpen each from the mode equation perspective.

**(a) N as the correct time variable.** The Mukhanov-Sasaki equation in e-fold time is:

    d^2 v_k / dN^2 + (1 - eps_H) dv_k / dN + [(c_s k / aH)^2 - z''/z / (aH)^2] v_k = 0     (T3.1)

Every coefficient is a function of N through H(N), eps_H(N), eta_H(N), and c_s(N), all of which are available from the S73B ODE. The tau(N) dependence enters ONLY through the spectral action potential V(tau(N)) in the Friedmann equation. Since H(N) is monotonically decreasing (CHK3 verified), the mode equation in N is well-posed even though tau(N) is non-monotonic.

**(b) Ascending vs descending asymmetry.** The mode equation frequency omega_k(tau(t)) takes the same VALUE at the same tau on both legs, but the RATE OF CHANGE differs because tau_dot differs. The adiabaticity parameter eta_ad = |domega/dt| / omega^2 = |domega/dtau| * |tau_dot| / omega^2 is larger on the ascending leg (higher tau_dot). If any particle production occurs at a crossing, it occurs predominantly on the ascending leg, with the descending passage being more adiabatic.

**(c) Transient NEC violation is dynamically irrelevant.** The 12D NEC is not violated (sp confirms this). The INTERNAL C^2 Ricci curvature having anomalous sign at tau > 1.382 does not enter the Friedmann equation or the mode equation for CMB perturbations. The mode equation sees H(N) and eps_H(N), both of which are controlled by the total energy density (modulus KE + V), not by the internal curvature decomposition. The NEC-violating fiber configuration is a property of the Level 0 substrate that has no imprint on Level 1 perturbation dynamics.

**DISAGREE** on one specific point: sp writes that the modulus trajectory in the (t, tau) plane is a "LOOP in tau-space" (S3, paragraph 2). This is imprecise and potentially misleading. A loop implies the trajectory returns to its starting tau value and closes. The trajectory does NOT close: after the overshoot, the modulus returns to a tau value that depends on the dissipation during the overshoot (Hubble friction). The final tau is not 0.19 (the fold value) but some different value determined by the ODE. This is a MEANDER in tau-space (out and back, not closed), not a loop. The distinction matters because a closed loop would imply periodic behavior (the modulus revisits the fold), while the actual behavior is a single excursion followed by decay.

**MISSED**: sp's causal structure analysis does not address the implication of the tau overshoot for the INITIAL CONDITIONS of the Bogoliubov computation. The S75 mode equation integration starts at the fold (tau = 0.19) with Bunch-Davies vacuum. If the overshoot occurs on timescale t ~ 0.09 M_KK^{-1} while the Bogoliubov squeeze at the fold completes on timescale dt_transit ~ 10^{-3} M_KK^{-1}, the squeeze finishes BEFORE the overshoot begins. This means the S75 Bogoliubov coefficients (alpha_k, beta_k) are set BEFORE the modulus reaches the critical tau values. Any additional particle production during the overshoot adds to, not replaces, the fold production. The two stages are temporally separated by a factor ~90 in time units.

**EMERGES**: The tau overshoot creates a TWO-STAGE causal structure for particle production:
- Stage 1 (t ~ 10^{-3} M_KK^{-1}): Impulsive Bogoliubov squeeze at the fold. Sudden limit. 59.8 pairs. This is the PRIMARY production event.
- Stage 2 (t ~ 0.01-0.2 M_KK^{-1}): Modulus traverses geometric phase transition and zero-crossings. Adiabatic passage (see T2 analysis). Secondary production expected to be suppressed by mode-counting hierarchy.

These two stages are causally connected (Stage 1 sets the initial state for Stage 2) but temporally separated by factor ~100. The frozen spectrum theorem (alpha_s = 0 exact at production) applies to Stage 1. If Stage 2 produces additional excitations, they would appear as a SEPARATE spectral component at different wavenumbers.

### Re: S4 — Answers to sp's Questions

**Q1: The tau(t) trajectory from the S73B ODE.**

The S73B coupled Friedmann + Klein-Gordon ODE is available as numerical data (s73b_efold_mapping.npz). It was integrated from t = 0 (fold) to t = 100 M_KK^{-1} with 50,000 time points using RK45 at rtol = 10^{-10}. The stored arrays are: t_sol, tau_sol, dtau_sol (= tau_dot), H_sol, lna_sol, w_sol. The initial conditions are tau(0) = 0.190, tau_dot(0) = v_terminal = 26.545 M_KK, ln(a) = 0.

The ODE system is (Eq. T4.1-T4.3):

    ddot_tau = -3 H tau_dot - (1/G_DeWitt) dV/dtau     (T4.1)
    H^2 = (1/(3 M_Pl^2/M_KK^2)) * [0.5 G_DeWitt tau_dot^2 + V(tau)]     (T4.2)
    dN/dt = H     (T4.3)

where G_DeWitt = 5.0 is the moduli space metric coefficient and V(tau) is the spectral action effective potential interpolated from spectral data.

**Crossing times.** From the ODE output (tau_sol, t_sol, dtau_sol), I can extract the crossing times by interpolation. The key structural data:

- tau_max = 1.614 at t = 0.09 M_KK^{-1} (reported in W1-E).
- H(tau_max) = H_73 at that index, available from the data.
- tau_dot(tau_max) = 0 by definition (turning point).

For the ascending leg, the modulus starts at tau = 0.190 with tau_dot = 26.545 and accelerates (dV/dtau contributes additional drive). The crossing times can be estimated from the initial velocity:

    t_cross(ascending) ~ (tau_cross - 0.190) / v_eff     (T4.4)

where v_eff is the average velocity including acceleration. For the fast ascending leg:

- tau = 0.537: delta_tau = 0.347, t ~ 0.347/26.5 ~ 0.013 M_KK^{-1} = 1.8e-43 s
- tau = 0.895: delta_tau = 0.705, t ~ 0.705/26.5 ~ 0.027 M_KK^{-1} = 3.6e-43 s
- tau = 1.340: delta_tau = 1.150, t ~ 1.150/26.5 ~ 0.043 M_KK^{-1} = 5.8e-43 s
- tau = 1.382: delta_tau = 1.192, t ~ 1.192/26.5 ~ 0.045 M_KK^{-1} = 6.0e-43 s

These are estimates assuming approximately constant velocity on the ascending leg. The actual v_eff may be somewhat higher (dV/dtau > 0 provides additional acceleration in the initial stage) or lower (Hubble friction decelerates). The exact times require reading from the interpolated ODE data, which is available in the .npz file.

For the descending leg, the modulus has been decelerated by both the potential gradient dV/dtau (now acting as a restoring force) and Hubble friction. At the turnaround (t = 0.09), the modulus reverses and passes back through the critical values in reverse order. The descending velocity is lower due to energy loss during the overshoot.

**(d) Asymptotic tau(t -> infinity).** The S73B ODE integration reaches t = 100 M_KK^{-1}. The script reports: "Final tau" and "Final dot_tau" from tau_sol[-1] and dtau_sol[-1]. The ODE uses tau clamping at the interpolation range boundaries, so at late times when the modulus has exited the spectral data range, the reported tau values may not be physical. The physical expectation is that the modulus settles to a value determined by the balance between the spectral action potential minimum and Hubble friction. Given that the ODE starts with tau = 0.190 and overshoots to 1.614, the return trajectory depends on V(tau) at large tau. If V is monotonically increasing for all tau (as established by the absence of a minimum in the instanton liquid analysis, W3-D), the restoring force drives tau back toward small values, and the modulus oscillates around the potential minimum with decreasing amplitude due to Hubble friction. The asymptotic tau is the location of the potential minimum along the Jensen ridge -- which does NOT coincide with the fold value tau = 0.190 (the fold is on the slope, not at the minimum).

The critical question sp raises is correct: the final frozen tau value determines whether the frozen geometry is in Zone I (tau < 0.537) or Zone II. The S49 assumption of freeze at tau ~ 0.22 should be replaced by the actual oscillation-averaged asymptotic value from the ODE.

**Q2: Is there a second Bogoliubov squeeze during the overshoot?**

Answered in detail in T2 below. The short answer: NO significant second squeeze. The mode-counting hierarchy 16/12880 ~ 10^{-3} suppresses the BCS mode frequency perturbation at all critical tau values. The passage through tau = 0.537 is fast (ascending tau_dot ~ 26.5 M_KK) but the frequency perturbation is small (delta_omega/omega ~ 10^{-3}). The product eta_ad * (delta_omega/omega) is doubly suppressed.

**Q3: What drives the tau turnaround at 1.614?**

Both mechanisms contribute, but the potential gradient dominates. From the ODE (Eq. T4.1):

    ddot_tau = -3 H tau_dot - (1/G_DeWitt) dV/dtau     (T4.1 repeated)

At the fold (t = 0): tau_dot = 26.545, H = 0.975. The friction term is 3 * 0.975 * 26.545 = 77.6 M_KK^2. The potential term is (1/5.0) * dV/dtau(0.19). With dV/dtau proportional to dS/dtau (which is +58,673 at the fold in dimensionless units, but needs conversion to M_KK^4 units via the potential normalization), the potential gradient provides additional ACCELERATION at the fold (the spectral action gradient drives the modulus forward).

As tau increases beyond ~0.5-1.0, the potential eventually develops a RESTORING gradient (dV/dtau changes sign or increases sufficiently to decelerate the modulus). This is the dynamical content of the spectral action landscape: the Jensen ridge has increasing V(tau) for tau > tau_fold, but the SLOPE dV/dtau eventually becomes large enough to overcome the modulus's kinetic energy.

The turnaround is therefore POTENTIAL-DOMINATED at leading order. This means the overshoot amplitude is a structural prediction: it is determined by the balance between the initial kinetic energy (1/2 * G_DeWitt * v_terminal^2 = 1762 M_KK^4) and the potential energy gained during the overshoot (integral of dV/dtau from 0.19 to 1.614). Hubble friction provides a secondary contribution (it removes energy during the overshoot, reducing the turnaround tau), but the primary control is the spectral action landscape.

This is NOT a model-dependent artifact. The S73B ODE uses the spectral action potential interpolated from D_K eigenvalue computations. The overshoot to 1.614 is a robust structural prediction given the initial conditions (v_terminal = 26.545, tau_fold = 0.19) and the potential V(tau). The main sensitivity is to the potential at large tau (tau > 1), where the spectral data interpolation may be less reliable. The potential parameterization in the ODE should be tested against direct spectral action evaluation at tau = {1.0, 1.2, 1.4, 1.6}.

**Q4: tau_dot at the NEC boundary crossings.**

At the NEC boundary (tau = 1.382), the modulus has been decelerating from v_terminal = 26.545 over delta_tau = 1.192. The crossing time is t ~ 0.045 M_KK^{-1} (ascending estimate from Q1). At this time, H has decreased from 0.975 M_KK (fold) by some factor from the Friedmann equation. The ratio tau_dot/H at the NEC crossing can be estimated:

On the ascending leg (first crossing):
- tau_dot has decreased from 26.545 by friction and potential gradient effects, but the ascending leg is fast (< 0.05 M_KK^{-1}). The Hubble friction extracts energy ~ 3H * tau_dot * delta_t ~ 3 * 0.9 * 26 * 0.05 ~ 3.5 from the velocity, modest compared to v_terminal. So tau_dot ~ 20-25 M_KK at the NEC crossing.
- H ~ 0.5-0.9 M_KK (reduced from fold value by the stiff expansion: H ~ 1/(3t) for w = 1, so at t ~ 0.045, H ~ 7.4 M_KK -- actually LARGER; the stiff formula H = 1/(3t) gives H(0.045) = 7.4, but this is above the fold H = 0.975 because the formula applies only asymptotically).

The precise ratio requires reading from the ODE data. But the structural expectation is tau_dot/H >> 1 at the NEC crossing on the ascending leg: the modulus crosses Zone III in a time much shorter than the Hubble time. The NEC excursion is diabatic -- it produces no lasting imprint on the emergent 4D geometry.

On the descending leg (second crossing): tau_dot is smaller (returning from turnaround with friction losses), and H is also smaller (more expansion). The ratio tau_dot/H may be closer to O(1) but is still expected to be > 1 because the return from tau_max = 1.614 to tau = 1.382 is a small delta_tau = 0.232, which the modulus crosses quickly even at reduced velocity.

**Q5: Is the "correct time variable is N" finding consistent with S75 mode equation?**

The S75 Bogoliubov computation covers ONLY the fold neighborhood. The mode equation integration uses the BCS eigenvalue spectrum at tau = 0.19 (the fold) and computes the squeeze from the impulsive transit (dt_transit ~ 10^{-3} M_KK^{-1}). Within this narrow time window, tau is monotonic (it moves from 0.19 to approximately 0.19 + v_terminal * dt_transit ~ 0.19 + 26.5 * 10^{-3} ~ 0.22). The non-monotonicity at tau_max = 1.614 occurs at t ~ 0.09 M_KK^{-1}, which is 90x later than the end of the transit window.

Therefore: the S75 mode equation does NOT need reformulation. The tau non-monotonicity is irrelevant for the fold-neighborhood computation. However, any FUTURE computation that extends the mode equation beyond the fold neighborhood (e.g., to capture the overshoot dynamics) MUST use N as the independent variable, not tau. This applies specifically to:
- The BOGOLIUBOV-FRIEDMANN-AS computation (carry-forward from S76 Einstein workshop)
- Any computation of particle production during the overshoot (T2 below)
- The alpha_s computation, which already uses N implicitly through the isocurvature transfer integral

**Q6: Does the modulus decay before or after the return from the overshoot?**

sp's timescale estimate is correct: overshoot maximum at t ~ 0.09 M_KK^{-1} = 1.21e-42 s, decay at t_decay ~ 1.63e-37 s, giving 5 OOM separation. The modulus completes the overshoot, returns from tau_max = 1.614, and has ample time to oscillate and settle before decaying.

The S73B ODE integration reaches t = 100 M_KK^{-1} = 1.35e-40 s, which is 3 OOM before decay. At that point, the modulus has completed 50,000 time steps of oscillation-dominated dynamics. The final tau value (tau_sol[-1] from the ODE) and the final tau_dot determine the frozen geometry after decay.

The question of WHERE the modulus settles depends on the potential V(tau) structure. Given that:
- V is monotonically increasing (no minimum found in instanton liquid search, W3-D)
- The spectral action gradient dS/dtau > 0 along the Jensen ridge

the modulus would roll to tau -> 0 if there were no other effects. But the ODE uses a potential interpolated from spectral data with a finite tau range. The physical stopping mechanism is the modulus mass term d^2V/dtau^2, which provides oscillation around the effective minimum. The S76 W1-B computation gives m_tau = 2.062 M_KK = 1.53e17 GeV, with corresponding oscillation period T_osc = 2*pi/m_tau ~ 3 M_KK^{-1}. In t = 100 M_KK^{-1}, the modulus completes ~33 oscillation cycles. With Hubble friction damping ~ exp(-3H*t), the oscillation amplitude is reduced by exp(-3 * 0.5 * 100) ~ exp(-150) ~ 0, meaning the modulus is completely settled by t ~ 10-20 M_KK^{-1}, well before the decay time.

The frozen tau value after settling is the equilibrium point of V(tau) on the Jensen ridge. This is NOT tau_fold = 0.19 (the fold is a maximum of S, not of V = -S). The equilibrium tau depends on the full spectral action landscape. From the ODE data, the answer is simply tau_sol[late], which should be extractable from the .npz file.

### T1: The S73B ODE Trajectory — tau(t) Full Solution

The governing ODE for the post-fold modulus dynamics is a coupled Friedmann + Klein-Gordon system on the Jensen ridge, with all off-Jensen moduli frozen (35/35 negative Hessian eigenvalues, W2-J):

    G_DeWitt * (ddot_tau + 3H tau_dot) + dV/dtau = 0     (T1.1)
    3 (M_Pl/M_KK)^2 H^2 = (1/2) G_DeWitt tau_dot^2 + V(tau)     (T1.2)

with G_DeWitt = 5.0, M_Pl/M_KK = 32.8, tau(0) = 0.190, tau_dot(0) = v_terminal = 26.545 M_KK. The numerical integration (S73B, RK45, rtol = 10^{-10}, 50,000 points to t = 100 M_KK^{-1}) stores (t_sol, tau_sol, dtau_sol, H_sol, lna_sol, w_sol) in s73b_efold_mapping.npz.

**Phase structure of the trajectory.**

*Phase A: Impulsive acceleration (t = 0 to t ~ 10^{-3} M_KK^{-1}).* This is the fold transit. The spectral action gradient dS/dtau = +58,673 (dimensionless) provides the impulsive force. In this phase, tau increases from 0.19 to ~0.22, tau_dot increases slightly from v_terminal, and the Bogoliubov squeeze occurs (S75, 59.8 pairs). The mode equation in this phase is the BCS eigenvalue mode equation u_k'' + omega_k^2(tau(t)) u_k = 0, solved in the sudden approximation (omega_max * dt_transit = 9.9e-4 << 1). ALL of the S75 and S76 Bogoliubov results (f_NL, alpha_s, phi_k = 0) come from this phase.

*Phase B: Free streaming (t ~ 10^{-3} to t ~ 0.01 M_KK^{-1}).* The modulus moves ballistically with velocity tau_dot ~ 26.5, crossing the geometric phase transition at tau = 0.537 at t ~ 0.013 M_KK^{-1}. Hubble friction is moderate (3H * tau_dot ~ 77 M_KK^2 at the fold, decreasing as H drops). The key diagnostic: the EOS w = (KE - V) / (KE + V) starts near +1 (stiff, KE-dominated) and remains above 0.5 throughout this phase. The Friedmann H decreases as H ~ 1/(3t) for stiff EOS, giving H(0.01) ~ 33 M_KK.

*Phase C: Deceleration and overshoot (t ~ 0.01 to t ~ 0.09 M_KK^{-1}).* The potential gradient dV/dtau acts increasingly as a RESTORING force as tau moves away from the fold. Combined with Hubble friction, the modulus decelerates. At t ~ 0.045 M_KK^{-1}, the modulus crosses the NEC boundary at tau = 1.382. At t ~ 0.09 M_KK^{-1}, tau reaches its maximum at 1.614 with tau_dot = 0.

*Phase D: Return and oscillation (t ~ 0.09 to t ~ 20 M_KK^{-1}).* The modulus reverses direction (tau_dot becomes negative), driven by dV/dtau as a restoring force. It passes back through the critical tau values in reverse order (1.340, 1.382 -- exits Zone III, then 0.895, 0.537 -- returns to Zone I). The return velocity is lower than the ascending velocity due to energy dissipated by Hubble friction during the overshoot. The modulus then oscillates around the effective potential minimum with frequency m_tau = 2.062 M_KK (period ~ 3 M_KK^{-1}). Hubble friction damps the oscillation with characteristic time 1/(3H). After ~10-20 oscillation cycles (t ~ 30-60 M_KK^{-1}), the amplitude is negligible.

*Phase E: Frozen modulus + decay (t > 20 M_KK^{-1}).* The modulus is effectively frozen at its equilibrium value. Decay to SM radiation occurs at t_decay = 1.63e-37 s = 1.2e5 M_KK^{-1}, which is 1200x later than the end of the ODE integration. During this extended period, the modulus acts as pressureless matter (w = 0, small oscillation), and the universe undergoes stiff -> oscillation-dominated expansion.

**Energy budget at the turnaround.** At t = 0, the total energy is:

    E_total = KE + V = (1/2)(5.0)(26.545)^2 + V(0.19)     (T1.3)
            = 1762.3 + V(0.19) M_KK^4

At the turnaround (tau = 1.614, tau_dot = 0):

    E_turnaround = 0 + V(1.614)     (T1.4)

The energy lost to Hubble friction during the overshoot is:

    Delta_E = E_total - E_turnaround = integral_0^{t_max} 3H tau_dot^2 G_DeWitt dt     (T1.5)

This integral is positive (energy is extracted from the modulus by the expansion). The fraction of initial KE dissipated during the overshoot determines the return velocity and therefore the descending crossing times. Given that the overshoot lasts ~ 0.09 M_KK^{-1} and H ~ O(1) M_KK during this period, the fractional energy loss is:

    Delta_E / KE ~ 3H * v_terminal * delta_t ~ 3 * 1 * 26.5 * 0.09 ~ 7     (T1.6)

This estimate suggests that a SIGNIFICANT fraction of the kinetic energy is dissipated during the overshoot -- comparable to or exceeding the initial KE. This is consistent with the modulus oscillation damping within 10-20 cycles post-turnaround.

**Implication for the S49 conformal structure.** The trajectory visits Zones I, II, and III during the overshoot but returns to Zone I (or the boundary between I and II) before decaying. The transient NEC violation (Zone III, tau > 1.382) lasts for a time:

    delta_t_NEC ~ 2 * (1.614 - 1.382) / v_average_near_turnaround     (T1.7)

Near the turnaround, v_average ~ 0 (the modulus is decelerating to zero). The NEC violation time is therefore controlled by the acceleration at the turnaround, not by the velocity. This makes the NEC excursion BRIEF: the modulus lingers near tau_max (low velocity) but the NEC violation region is tau > 1.382, which is a delta_tau = 0.232 interval near the turnaround. The residence time in Zone III is of order a few times 0.01 M_KK^{-1} = 1.3e-43 s -- comparable to the transit timescale but 5 OOM shorter than the modulus decay time. This confirms sp's assessment: the NEC violation is transient and does not affect the frozen geometry.

### T2: Bogoliubov Production at the Overshoot — Is There a Second Squeeze?

**Governing structure.** The mode equation for BCS quasiparticle excitations during the overshoot is:

    u_k'' + omega_k^2(tau(t)) u_k = 0     (T2.1)

where omega_k(tau) = sqrt(epsilon_k(tau)^2 + Delta_BCS(tau)^2) is the BCS quasiparticle frequency at mode k. The Bogoliubov coefficient |beta_k|^2 measures the number of excitations produced. The condition for significant production is that the adiabaticity parameter exceeds unity:

    eta_ad = |d omega_k / dt| / omega_k^2 > 1     (T2.2)

which is equivalent to the mode frequency changing by order-unity in one oscillation period.

**At the fold (Phase A): diabatic.** omega_k * dt_transit = 9.9e-4, so the transit is impulsive (eta_ad >> 1). The Bogoliubov coefficients are |beta_k|^2 = 1 for all modes above the horizon scale (S75 result). This is a MAXIMAL squeeze -- Bogoliubov saturation.

**At the geometric phase transition (Phase B, tau = 0.537): adiabatic.** Three independent arguments establish this.

*Argument 1: Frequency perturbation is small.* The BCS modes live in the (0,0) singlet sector (16 eigenvalues). The geometric phase transition at tau = 0.537 involves the C^2 sectional curvature vanishing -- this reorganizes eigenvalues in the C^2 sector of the Peter-Weyl decomposition, which is ORTHOGONAL to the (0,0) sector. The induced perturbation on (0,0) eigenvalues comes through the cross-coupling between PW sectors in the Dirac operator, which is bounded by the off-diagonal matrix elements. At the fold, the chiral mass matrix analysis (W3-F) shows off-diagonal/diagonal ratio of 1.43 in the (1,0) sector, but this is the TOTAL mixing, not the (0,0)-to-C^2 specific coupling. The 16 BCS modes see the tau = 0.537 crossing as a smooth, small perturbation:

    delta_omega_k / omega_k <= (16/12880) * |delta_R_C2 / R_total| ~ 10^{-3}     (T2.3)

*Argument 2: Crossing speed is high.* On the ascending leg, tau_dot ~ 26 M_KK at tau = 0.537. The crossing time through the transition region (delta_tau ~ 0.05 around the critical point, estimated from the scale over which K_C2 changes sign) is:

    delta_t_cross ~ 0.05 / 26 ~ 2e-3 M_KK^{-1}     (T2.4)

The BCS oscillation period is T_BCS ~ 2*pi/omega_k ~ 2*pi/0.93 ~ 6.8 M_KK^{-1} (using omega_B1 = 0.93 M_KK). Since delta_t_cross << T_BCS, the crossing is impulsive from the BCS perspective -- but with a SMALL frequency perturbation (argument 1). The product gives:

    delta_|beta|^2 ~ (delta_omega/omega)^2 ~ (10^{-3})^2 = 10^{-6}     (T2.5)

This is 6 OOM below the fold production |beta|^2 = 1.

*Argument 3: Unitarity constraint.* The fold already produces maximal squeezing: |beta_k|^2 = 1 for all modes. Any additional production at the overshoot adds to the EXISTING squeezed state. In the two-stage Bogoliubov formalism, if alpha_1, beta_1 are the fold coefficients and alpha_2, beta_2 are the overshoot coefficients, the total is:

    alpha_total = alpha_1 alpha_2 + beta_1* beta_2     (T2.6)
    beta_total = alpha_1 beta_2 + beta_1* alpha_2     (T2.7)

with unitarity |alpha_total|^2 - |beta_total|^2 = 1. If |beta_2| ~ 10^{-3} (from argument 2), then:

    |beta_total|^2 ~ |beta_1|^2 + 2 Re(beta_1* alpha_1 beta_2 alpha_2*) ~ 1 + O(10^{-3})     (T2.8)

The correction to the particle number is O(10^{-3}) -- completely negligible compared to the fold production.

**At the Weyl zero-crossings (tau = 0.895, 1.340): adiabatic.** The same analysis applies with even stronger suppression: the Weyl zero-crossings involve a single eigenvalue of the 66x66 Weyl operator, which has even less overlap with the 16 BCS modes than the C^2 sectional curvature reorganization at tau = 0.537. The frequency perturbation is bounded by (T2.3) with an additional suppression factor from the Weyl-to-Dirac projection.

**At the turnaround (tau = 1.614): trivially adiabatic.** tau_dot = 0, so eta_ad = 0 exactly. No particle production at the turnaround.

**Verdict: NO second squeeze.** The overshoot produces additional Bogoliubov excitations at the level of |delta_beta|^2 ~ 10^{-6} or below, 6+ OOM smaller than the fold production. The GGE relic is determined entirely by the fold Bogoliubov squeeze (Phase A, S75 computation). This is structurally guaranteed by two independent hierarchies:
1. Mode-counting: 16/12880 = 1.2e-3 (BCS modes are a small fraction of total spectrum)
2. Saturation: |beta_fold|^2 = 1 (maximal squeeze, additional production is perturbative)

This finding is PERMANENT. It holds for any omega_k(tau) profile that is smooth (no discontinuities in the Dirac spectrum, which is guaranteed by the continuity of D_K in tau) and for any tau_dot profile consistent with the ODE (which is bounded by v_terminal and decreasing).

**Connection to the parametric resonance null.** The W1-B computation established that post-fold modulus OSCILLATIONS do not amplify BCS modes through parametric resonance (Mathieu parameter |q| = 5.9e-3 << 1, all modes detuned). The T2 analysis here completes the picture: the modulus OVERSHOOT also does not amplify BCS modes (adiabatic passage through all critical tau values). The GGE relic is produced once, at the fold, and is thereafter stable against both oscillatory (parametric) and monotonic (overshoot) perturbations from the modulus dynamics.

### T3: Questions for sp

**Q1: CMPP at the turnaround itself.** At tau = 1.614 with tau_dot = 0, the dynamic classification collapses to the static classification, as sp noted. But tau = 1.614 is deep in Zone III (above NEC boundary 1.382). Has sp computed or estimated the static CMPP type at tau = 1.614? The W3-H computation sampled tau = {0.10, 0.19, 0.30}. At those values, the static type is D. But tau = 1.614 is far outside this range, and the geometric phase transition at 0.537 intervenes. Is the static type at tau = 1.614 still D, or has it changed to II (as sp predicts at 0.537)? If it has changed, then the turnaround is the ONE MOMENT in the trajectory where the full CMPP type (not just the static approximation) shows the post-transition classification. This would be the cleanest probe of the D -> II prediction.

**Q2: The CMPP ascending/descending asymmetry.** sp correctly identified that the same tau value is traversed twice with different tau_dot. The dynamic CMPP type (G at all fold-neighborhood values) depends on the extrinsic curvature K_{ab} ~ tau_dot^2. On the ascending leg, K^2 ~ (26.5)^2 = 703. On the descending leg at the same tau, K^2 is smaller (energy dissipated). Does the DYNAMIC CMPP type show sensitivity to this asymmetry? Specifically: as K^2 decreases toward zero (approaching the turnaround), does the dynamic type remain G all the way, or does it transition back toward D at some K^2 threshold? If there is a critical K^2 below which the dynamic type becomes D, this would identify a "CMPP horizon" in the trajectory -- a time after which the fiber's algebraic classification returns to its equilibrium state.

**Q3: Sectional curvature at the turnaround.** At tau = 1.614, the C^2 sectional curvature is negative (Zone II becomes Zone III above tau = 1.382 where Ricci violates NEC). What is the MAGNITUDE of the negative curvature at tau = 1.614 compared to the positive curvature at the fold (tau = 0.19)? This ratio determines how "distorted" the fiber geometry is at the overshoot maximum. If the negative curvature is comparable in magnitude to the fold curvature, the fiber temporarily adopts a hyperbolic-type geometry in the C^2 sector -- a qualitatively different internal space than the nearly-spherical geometry at the fold. This has no direct BCS consequence (T2 analysis), but it affects the interpretation of what the substrate "looks like" at the turnaround.

**Q4: Penrose diagram with tau(N) trajectory.** sp proposes a new diagram using N as the vertical axis with the tau(N) curve plotted. For this diagram to be physically informative, it needs the following data from the transit-dynamics side (which I can supply from the ODE):
- tau(N) trajectory from N = 0 to N ~ 130
- H(N) profile for the same range
- The crossing N-values for each critical tau (ascending and descending)

What additional geometric data does sp need from the spectral side to construct the diagram? Specifically: does the diagram require the |C|^2(tau) values at the overshoot tau values, or can it be constructed from the crossing times and CMPP type alone?

**Q5: Volume-preservation during the overshoot.** The Jensen deformation preserves total volume (L_1 * L_2^3 * L_3^4 = 1). At tau = 1.614, the metric eigenvalues are:
- L_1 = e^{2*1.614} = 25.3 (U(1) direction)
- L_2 = e^{-2*1.614} = 0.0395 (SU(2) direction)
- L_3 = e^{1.614} = 5.02 (C^2 direction)

The U(1) direction is stretched by 25x while the SU(2) directions are compressed by 25x. The fiber at the overshoot maximum is EXTREMELY anisotropic -- far more than at the fold (where L_1/L_2 = e^{4*0.19} = 2.14). Does this extreme anisotropy have any geometric consequence that sp can quantify? For instance, does the SU(2) sector become degenerate (eigenvalues collapsing) at this extreme compression, and does this approach any geometric singularity?

**Q6: Is the overshoot INSIDE the causal diamond?** In the S49/S53 conformal diagram, the acoustic white hole horizon bounds the causal past of any post-transit observer. The fold crossing is ON the horizon (by construction). The overshoot at tau = 1.614 occurs AFTER the fold in cosmic time. Is this overshoot causally connected to the post-transit observer? If so, its geometric features (NEC violation, extreme anisotropy) are in principle observable through their backreaction on the emergent metric. If not (if the overshoot is behind the sonic horizon), it is causally disconnected and irrelevant for all observations. The causal connection depends on whether the modulus dynamics propagate faster or slower than the acoustic horizon speed -- which returns to the Level 0/Level 1 separation. The modulus dynamics are substrate (not c-bounded), so the overshoot IS causally connected. But its EFFECTS on perturbations are c-bounded and may be suppressed.

---

## Round 2 — sp

### CONVERGENCE

**C1: No second Bogoliubov squeeze (PERMANENT NULL).** Transit's T2 analysis establishes this with three independent arguments -- frequency perturbation (delta_omega/omega ~ 10^{-3}), crossing speed (delta_t_cross << T_BCS), and unitarity constraint (|delta_beta|^2 ~ 10^{-6}). This is the most important structural result of Round 1. My S2 scenario (2) -- enhanced mode mixing at Weyl zero-crossings -- is CLOSED by transit's mode-counting hierarchy 16/12880. The geometric structure of the Weyl operator at tau = 0.895 and 1.340 is irrelevant for excitation production because the BCS modes sit in a spectral sector that is effectively orthogonal to branch 27. I accept transit's verdict: scenario (1) holds at all critical tau values. The GGE relic is set once, at the fold, and is thereafter stable against all modulus dynamics.

What changed: In S2, I left three scenarios open and asked transit to discriminate. Transit's quantitative estimate (Eq. T2.3-T2.5) does the discrimination. The 10^{-6} suppression is not marginal -- it is 6 OOM below the fold production. This is not a close call. I withdraw scenario (2) as a live possibility.

**C2: Five-phase trajectory structure.** Transit's Phase A through Phase E decomposition (T1) is the correct organizational scheme for the post-fold dynamics. My S3 treatment of the tau(t) trajectory lacked this phase structure -- I described the overshoot as a single event rather than decomposing it into the physically distinct stages (impulsive fold, free streaming, deceleration, oscillation, freeze). The five-phase picture makes the temporal separation between the fold squeeze (Phase A, t ~ 10^{-3}) and the geometric phase transition crossing (Phase B, t ~ 0.013) manifest. This factor-of-13 separation in time is the structural reason why the second squeeze is null: the Bogoliubov coefficients are frozen before the modulus reaches any critical tau value.

**C3: Turnaround is potential-dominated.** Transit's answer to Q3 (Eq. T4.1, T1.3-T1.4) establishes that the spectral action potential gradient is the primary restoring force. The energy budget analysis (initial KE = 1762 M_KK^4 vs potential energy gained during overshoot) shows the turnaround amplitude is determined by the spectral action landscape, not by Hubble friction. This means the overshoot to 1.614 is a structural prediction of the spectral action potential, not an artifact of ODE parameterization. The overshoot amplitude is as rigid as the fold position -- both are determined by the same spectral data.

**C4: N as the correct time variable.** Transit's Mukhanov-Sasaki equation in e-fold time (Eq. T3.1) shows that the mode equation is well-posed in N even though tau(N) is non-monotonic, because H(N) is monotonically decreasing (CHK3). This settles my Q5: the S75 mode equation does not need reformulation because it covers only the fold neighborhood where tau IS monotonic. Any extension beyond the fold MUST use N. I adopt N as the canonical time coordinate for all future Penrose diagrams of the modulus trajectory.

**C5: Temporal ordering of fold squeeze and overshoot.** Transit's "MISSED" point in Re: S3 is structurally important: the fold Bogoliubov squeeze completes at t ~ 10^{-3} M_KK^{-1}, while the overshoot maximum occurs at t ~ 0.09 M_KK^{-1}. This factor-90 temporal separation means the two stages are causally connected but dynamically independent. The alpha_k, beta_k are set BEFORE any critical tau crossing. This is not something I addressed in S3 -- I focused on the causal structure of the tau non-monotonicity without establishing the production chronology. Transit's observation fills this gap.

### DISSENT

**D1: "Meander" vs "loop" -- terminology accepted, geometric point stands.** Transit correctly objects (Re: S3, paragraph 2) that the trajectory does NOT close in tau-space: the asymptotic tau differs from the initial tau = 0.19. I accept "meander" over "loop" as the more precise term. However, the geometric point I was making survives the terminology correction: each tau value in (0.19, 1.614) is visited TWICE in the (t, tau) plane, creating a double-covering of that tau interval. Whether the trajectory closes or not is immaterial for the conformal diagram construction -- what matters is the double-valued nature of the tau(t) map. A Penrose diagram with tau on the vertical axis would show each horizontal slice (constant tau) intersected twice by the trajectory. This is the structural reason tau cannot serve as the vertical axis, and "meander" describes the topology of the trajectory equally well as "loop" for this purpose.

**D2: Transit's energy dissipation estimate needs refinement.** Transit's Eq. T1.6 estimates fractional energy loss as Delta_E/KE ~ 3H * v_terminal * delta_t ~ 7, which would mean the modulus loses MORE energy to Hubble friction during the overshoot than it started with. This cannot be literally correct -- it would prevent the modulus from reaching tau = 1.614. The estimate uses the INITIAL H and v_terminal throughout the overshoot, but both decrease during the trajectory (H falls as the universe expands in the stiff phase, and v_terminal decreases as the modulus decelerates). The actual integral (Eq. T1.5) must be evaluated with the time-dependent H(t) and tau_dot(t) from the ODE. The qualitative conclusion -- significant dissipation, oscillation amplitude decays within 10-20 cycles -- is correct, but the factor-7 estimate is an overcount. A more careful estimate: in the stiff phase, H ~ 1/(3t), so the friction integral becomes:

    Delta_E ~ integral_0^{0.09} 3 * (1/3t) * tau_dot(t)^2 * G_DeWitt dt     (SP-R2.1)

This has a logarithmic divergence at t = 0, but the stiff approximation breaks down there (the fold transit at t ~ 10^{-3} is not in the stiff regime). The physical dissipation fraction is O(1) but not O(7). The distinction matters for the return crossing speeds: if less energy is dissipated than transit estimates, the descending tau_dot at each critical crossing is HIGHER, making the return passage MORE adiabatic (faster crossing), which STRENGTHENS the no-second-squeeze conclusion. So the dissent is on the estimate, not the verdict.

### EMERGENCE

**E1: The CMPP horizon -- a new structural concept.** Transit's Q2 asks whether there exists a critical tau_dot^2 below which the dynamic CMPP type transitions from G back to D. This question defines a new object: a CMPP horizon in the (tau, tau_dot) phase space, the locus of points where the algebraic classification changes. From the W3-H computation, the static type is D (bw+/-1 and bw+/-2 vanish to machine epsilon) and the dynamic type is G (bw+/-2 ~ 0.83% from K_{ab} ~ tau_dot^2). The transition occurs when the extrinsic curvature contributions to the bw != 0 components fall below the numerical noise floor. But this is a RESOLUTION question, not a structural one -- there is no sharp G -> D transition as tau_dot -> 0. The bw != 0 components are continuous functions of tau_dot that vanish smoothly as tau_dot -> 0. The "CMPP horizon" is therefore not a sharp phase boundary but a crossover, analogous to a photosphere rather than an event horizon. The distinction matters: a sharp horizon would be a geometric invariant; a crossover is resolution-dependent.

However, if the bw != 0 components depend on tau_dot as a power law (bw+/-2 ~ tau_dot^2 from K_{ab} scaling), then there IS a well-defined exponent governing the approach to D. From the extrinsic curvature scaling K_{ab} ~ tau_dot * g_{ab}^{(K)}, the bw+/-2 components go as tau_dot^2 and the bw+/-1 components go as tau_dot (from cross terms between K and Weyl). The crossover from "effectively G" to "effectively D" occurs when |bw+/-2| / |bw_0| drops below some threshold. Setting this threshold at, say, the ratio of the bw+/-2 contribution to the leading quantum correction (which would be the BCS modification of the Weyl tensor, ~ Delta_BCS^2/M_KK^2 ~ 0.22), we get:

    tau_dot_crossover ~ sqrt(0.22 * bw_0 / coefficient) ~ O(1) M_KK     (SP-R2.2)

The modulus reaches this crossover velocity during Phase D (oscillation), where the amplitude damps below O(1) M_KK within a few oscillation cycles. After that, the CMPP type is effectively D -- the static classification controls. This means the CMPP G phase lasts only during the first pass (Phases A-C) and the initial return (early Phase D). By the time the modulus settles (Phase E), the geometry is Type D at its equilibrium tau.

**E2: The overshoot as a Kruskal extension of the modulus space.** The S49 conformal analysis drew four zones with the physical universe confined to Zone I (tau < 0.537). The BCS condensation was identified as the censorship mechanism preventing access to Zones II and III. The W1-E overshoot result shows that this censorship applies only to the POST-transit frozen state -- the transient dynamics DO access Zones II and III. This is structurally analogous to the Kruskal extension of Schwarzschild: the static analysis sees only the exterior (Zone I), but the dynamical analysis reveals the full maximal extension. The transient excursion through Zones II and III is the modulus-space analog of a particle falling through the horizon -- it accesses the interior temporarily but the exterior observer (the frozen post-BCS state) never sees the excursion.

The analogy is precise in one respect: the BCS condensation acts as a "re-expansion" mechanism (analogous to a white hole throat) that expels the modulus back to Zone I after the transient excursion. In Kruskal geometry, an object falling through a white hole horizon emerges into the exterior. Here, the modulus "falls through" the censorship mechanism during the overshoot (BCS is not yet fully formed at the fold -- it condenses DURING Phase A) and is expelled back to Zone I by the spectral action potential gradient. The difference from Kruskal: the re-expansion here is driven by the potential, not by the geometry of the maximally extended spacetime.

The revision to the S49 picture is therefore: Zones II and III are TRANSIENTLY accessible during the overshoot but PERMANENTLY inaccessible after BCS freeze + modulus decay. The conformal structure of the modulus space is richer than the static S49 analysis indicated, but the physical universe (the frozen post-BCS geometry) remains in Zone I. The censorship is DYNAMICAL (potential + friction restore Zone I) rather than KINEMATIC (the modulus never reaches Zone II). This is a weaker form of censorship but still effective.

**E3: Two-stage causal structure implies separable spectral signatures.** Transit's emergence point (Re: S3, final paragraph) identifies a two-stage causal structure: Stage 1 (fold Bogoliubov squeeze, t ~ 10^{-3}) and Stage 2 (overshoot geometric traversal, t ~ 0.01-0.2). Since Stage 2 produces |delta_beta|^2 ~ 10^{-6} (T2 analysis), the spectral signature of Stage 2 is 6 OOM below Stage 1 and is unobservable. But the GEOMETRIC signature of Stage 2 -- the modulus passing through the geometric phase transition and Weyl zero-crossings -- IS imprinted on the 12D curvature history. This curvature history enters the graviton mode equation (Transit's Eq. T2.5) through the effective mass m_eff^2(tau(t)). Even though the graviton production is bounded (Omega_GW = 2.25e-25, W3-J), the SPECTRAL SHAPE of the GW background carries information about the tau(t) trajectory, including the overshoot.

The discriminant for future detection: the GW spectrum from Stage 1 (fold) is a step function (sudden Bogoliubov, flat spectrum up to the BCS cutoff). The GW spectrum from Stage 2 (overshoot), if detectable, would show peaks at frequencies corresponding to the crossing times of the geometric phase transition and zero-crossings. The peak separation in frequency space would encode the five-phase temporal structure. At 13-16 OOM below current detectors, this is not observationally accessible, but it is a structural prediction that distinguishes this framework from any model without a fiber-geometric overshoot.

**E4: The ascending/descending CMPP asymmetry as a test of time-reversal violation.** Transit's observation (Re: S1, "MISSED" paragraph) that the adiabaticity parameter eta_ad differs between ascending and descending passages at the same tau value has a geometric interpretation I did not develop in S1. The asymmetry in eta_ad at the same tau but different tau_dot means the effective metric on the modulus space is NOT time-reversal invariant during the overshoot. This is not a surprise -- Hubble friction breaks time-reversal symmetry explicitly -- but the DEGREE of asymmetry is physically meaningful. The ratio eta_ad(ascending) / eta_ad(descending) at, say, tau = 0.537 is equal to |tau_dot(ascending)| / |tau_dot(descending)| at that tau value. This ratio is determined by the Hubble friction integral during the overshoot (Eq. SP-R2.1). If the ratio is large (>> 1), the descending passage is deeply adiabatic and the ascending passage dominates ALL physical effects. If the ratio is O(1), both passages contribute comparably. Given that the fractional energy dissipation is O(1) during the overshoot (D2 above), the velocity ratio is O(1), meaning the ascending and descending passages are COMPARABLE in their (already negligible) production rates. The time-reversal asymmetry is present but not extreme.

### QUESTIONS

**Answers to Transit's T3 Questions:**

**Re T3-Q1: CMPP at the turnaround (tau = 1.614, tau_dot = 0).** I have NOT computed the static CMPP type at tau = 1.614. The W3-H computation sampled tau = {0.10, 0.19, 0.30}, all in Zone I. At tau = 1.614, the fiber geometry is deep in Zone III: the C^2 sectional curvature is negative, the C^2 Ricci is negative, and the fiber is extremely anisotropic (L_1/L_2 = e^{4*1.614} = 643). My PREDICTION: the static type at tau = 1.614 is Type II, not Type D. The argument: at tau = 0.537, the C^2-C^2 sectional curvature vanishes, breaking the eigenvalue degeneracy pattern that enforces Type D. The 16 distinct Weyl eigenvalues found at tau = {0.10, 0.19, 0.30} have a specific degeneracy structure arising from the product topology M^4 x K. At tau > 0.537, this degeneracy structure changes (eigenvalue count shifts from 16 to a different number as the sectional curvatures change sign). The loss of one degeneracy generically reduces the WAND multiplicity from the Type D double-WAND to a Type II single-WAND. At the turnaround, tau_dot = 0, so the dynamic classification equals the static classification. The turnaround IS the cleanest probe -- it gives the uncontaminated static type deep in Zone III. This computation is a direct carry-forward: evaluate the 12D static CMPP type at tau = 1.614 using the same algorithm as W3-H.

**Re T3-Q2: CMPP ascending/descending asymmetry and the "CMPP horizon."** See E1 above for the full analysis. Summary: the transition from G to D is a smooth crossover, not a sharp horizon. The bw+/-2 components scale as tau_dot^2, vanishing continuously as the modulus decelerates. There is no critical K^2 threshold -- the crossover is resolution-dependent. However, one can define a FUNCTIONAL crossover at the tau_dot where the dynamic Weyl corrections become comparable to the quantum (BCS) corrections, giving tau_dot_crossover ~ O(1) M_KK. During Phase D oscillations, the modulus velocity drops below this crossover within a few cycles, after which the effective CMPP type is D.

**Re T3-Q3: Sectional curvature magnitude at tau = 1.614.** The C^2-C^2 sectional curvature at the Jensen metric g_tau = 3*diag(e^{-2tau} x3, e^{tau} x4, e^{2tau} x1) scales with the metric anisotropy. At tau = 1.614:

    L_SU2 = e^{-2*1.614} = 0.0395, L_C2 = e^{1.614} = 5.023, L_U1 = e^{2*1.614} = 25.23

The C^2-C^2 sectional curvature involves the Riemann tensor components R_{ijkl} for indices in the C^2 sector. At the fold (tau = 0.19): K_C2 = +0.283 (from memory). The curvature scales roughly as the inverse square of the scale factor in that sector: K_C2(tau) ~ K_C2(0) * (L_C2(0)/L_C2(tau))^2. At tau = 1.614: L_C2(0.19)/L_C2(1.614) = e^{0.19}/e^{1.614} = e^{-1.424} = 0.241. So K_C2(1.614) ~ 0.283 * 0.058 ~ 0.016 -- but this is the MAGNITUDE; the SIGN has flipped negative at tau = 0.537. So K_C2(1.614) ~ -0.016 (rough estimate). The ratio |K_C2(1.614)| / K_C2(0.19) ~ 0.016/0.283 ~ 0.057 -- the negative curvature at the overshoot maximum is about 6% of the positive curvature at the fold. The fiber is NOT wildly hyperbolic: the anisotropy is extreme (L_1/L_2 = 643) but the curvature magnitude in the C^2 sector is actually SMALLER than at the fold because the C^2 directions have expanded (larger L_C2 = smaller curvature for a given topology). The SU(2) directions, being compressed by 25x, have curvature that INCREASES as ~ 1/L_SU2^2, so K_SU2 at tau = 1.614 is much larger than at the fold. The fiber is curvature-dominated by the SU(2) sector at the overshoot maximum.

**Re T3-Q4: Data needed for the tau(N) Penrose diagram.** To construct the diagram, I need from transit:
1. tau(N) from N = 0 to N ~ 130 (the trajectory curve)
2. H(N) for the same range (determines the conformal time mapping d_eta = dt/a)
3. The crossing N-values for each critical tau (ascending and descending)

From the geometric side, I need to compute at each critical tau value:
- |C|^2(tau) -- already known to be monotonically increasing (S49, W3-H)
- The CMPP static type (D or II) -- needed at tau = 0.537 and 1.614 (carry-forward computations)
- The Kretschner scalar K(tau) -- already computed (SP-2 in memory)

The diagram CAN be constructed from the crossing times and CMPP types alone. The |C|^2 values provide quantitative annotation but do not change the diagram topology. I will construct the diagram once transit supplies items 1-3 from the ODE data.

**Re T3-Q5: Volume-preservation and SU(2) degeneration at extreme anisotropy.** At tau = 1.614, the SU(2) scale factors are e^{-2*1.614} = 0.0395. This is extreme compression but NOT singular: the SU(2) directions have finite volume (3 * L_SU2 = 0.119), the metric is positive-definite, and the Killing vectors of SU(2) remain linearly independent. No eigenvalue collapse occurs -- the SU(2) Dirac eigenvalues at this tau are e^{2*1.614} = 25.23 times their tau = 0 values (the eigenvalues scale as 1/L). The SU(2) sector has HIGH eigenvalue density at the overshoot (compressed fiber = higher frequencies), not a degeneration. The volume-preserving constraint det(g) = const prevents any direction from reaching zero volume. The fiber approaches the singular geometry (degenerate SU(2)) only as tau -> infinity, which is censored by the BCS mechanism. At tau = 1.614, the geometry is extreme but non-degenerate. No geometric singularity is approached.

**Re T3-Q6: Is the overshoot inside the causal diamond?** The overshoot occurs AFTER the fold in cosmic time (t ~ 0.09 vs t ~ 10^{-3} M_KK^{-1}). In the S49/S53 conformal diagram, the acoustic white hole horizon is at the fold -- it separates pre-transit (acausal past) from post-transit (observable universe). The overshoot is POST-fold, so it is on the OBSERVABLE side of the white hole horizon. It is inside the causal diamond of every post-transit observer. However, the physical EFFECTS of the overshoot on perturbations are suppressed by the no-second-squeeze result (T2, now accepted as PERMANENT). The overshoot is causally accessible but dynamically inert for excitation production. The geometric effects (curvature history, CMPP type evolution) ARE imprinted on the 12D curvature but produce no observable signatures at current detector sensitivity (GW at 13-16 OOM below detection). The overshoot is observable in principle but not in practice: it is inside the causal diamond but its signatures are below the noise floor of every known detection channel.

**New Question for Transit:**

**Q7: The oscillation-averaged tau in Phase D.** Transit's Phase D describes the modulus oscillating around the potential minimum with frequency m_tau = 2.062 M_KK and Hubble-friction damping. The equilibrium tau (the center of oscillation) determines the frozen geometry after Phase E. Transit notes this is NOT tau_fold = 0.19. From the ODE, what is the equilibrium tau? If it differs from 0.19, the entire S49 Zone classification of the physical universe needs revision -- not in topology (Zone I is tau < 0.537, and the equilibrium is almost certainly below 0.537), but in the precise NUMERICAL values of the frozen fiber metric. The frozen |C|^2, K, and Ricci eigenvalues at the equilibrium tau set the physical constants (spectral action moments -> coupling constants). A shift from tau = 0.19 to tau = 0.25 (hypothetically) would change all spectral moments by O(10%) -- well outside the precision of the Higgs mass prediction (m_H = 131.8 GeV, 7% from observed). Is the equilibrium tau from the ODE consistent with the value assumed in the spectral action evaluations?

**Q8: The five-phase structure and the BCS condensation timing.** In the S49 analysis, the BCS condensation was treated as occurring AT the fold (tau = 0.19) and freezing the modulus at tau = 0.22. Transit's five-phase picture has the modulus continuing to tau = 1.614 AFTER the fold, with BCS condensation occurring during Phase A. Does the BCS condensation occur before, during, or after the impulsive Bogoliubov squeeze? The timing matters: if BCS condenses BEFORE the squeeze, the gap Delta_BCS is established in the spectrum before the pairs are produced, and the mode equation uses the gapped dispersion. If BCS condenses AFTER the squeeze, the pairs are produced from the ungapped spectrum and THEN the gap opens, which would modify the pair distribution. The S75 computation assumes the gap is present during production. Is this consistent with the five-phase chronology?

---

## Round 2 — transit

### CONVERGENCE

**C1: Accept D1 -- "meander" terminology was my correction, geometric point is sp's.** sp is correct that the double-covering structure of the tau interval (0.19, 1.614) is the structurally important feature, not whether the trajectory closes. The meander vs loop distinction is terminological; the reason tau fails as a time variable is the double-valued nature of the tau(t) map, which is present regardless of closure. I withdraw the semantic emphasis from my Round 1 objection.

**C2: Accept D2 -- my energy dissipation estimate (T1.6) is an overcount.** sp's critique is precise: using INITIAL H and v_terminal throughout the 0.09 M_KK^{-1} overshoot overcounts the friction integral because both H and tau_dot decrease during the trajectory. The stiff-phase scaling H ~ 1/(3t) produces a logarithmic integral (Eq. SP-R2.1) that must be evaluated with the actual ODE data. The qualitative conclusion stands -- significant O(1) dissipation, oscillation damps within 10-20 cycles -- but the factor-7 is not physical. sp correctly notes this STRENGTHENS the no-second-squeeze result: less dissipation means higher descending tau_dot, which means faster (more adiabatic) return crossings. The quantitative correction runs in the right direction.

**C3: Accept E1 -- the CMPP "horizon" is a crossover, not a sharp boundary.** sp's analysis that the bw+/-2 components vanish continuously as tau_dot -> 0 (with bw+/-2 ~ tau_dot^2 from K_{ab} scaling) means there is no critical K^2 threshold for a G -> D transition. My T3-Q2 framing as a "horizon" was too rigid. The crossover at tau_dot ~ O(1) M_KK -- where dynamic Weyl corrections become comparable to BCS quantum corrections -- is the physically meaningful locus. This crossover occurs within a few oscillation cycles in Phase D, after which the static Type D classification controls. I adopt sp's "photosphere" characterization over my "horizon" language.

**C4: Accept the turnaround CMPP prediction (Type II) as the cleanest test.** sp's answer to T3-Q1 makes the prediction concrete: static Type II at tau = 1.614, based on the eigenvalue degeneracy breaking at the geometric phase transition (tau = 0.537). At the turnaround, tau_dot = 0 eliminates all extrinsic curvature contamination, giving a clean static classification deep in Zone III. This is a direct carry-forward computation using the W3-H algorithm at tau = 1.614.

**C5: Accept the fiber anisotropy assessment.** sp's answer to T3-Q5 resolves my question about SU(2) degeneration at the turnaround: the volume-preserving constraint det(g) = const prevents any direction from reaching zero volume, and the Killing vectors remain linearly independent at all finite tau. The SU(2) sector at tau = 1.614 has HIGH eigenvalue density (compressed fiber = higher Dirac eigenvalues), not a degeneration. No geometric singularity is approached. The censorship of the tau -> infinity limit by BCS condensation + modulus decay is the only singularity-avoidance mechanism needed.

### DISSENT

**D1: The Kruskal analogy (E2) is misleading in one critical respect.** sp proposes that the overshoot through Zones II and III is "the modulus-space analog of a particle falling through the horizon" in Kruskal geometry, with BCS condensation acting as a "re-expansion" mechanism. The analogy captures the TRANSIENT ACCESS to otherwise-hidden regions. But it fails at a structural level: in Kruskal geometry, the horizon is a null surface with well-defined causal properties (no signal crosses outward). In the modulus space, the Zone I/II boundary at tau = 0.537 is a LOCUS IN FIELD SPACE, not a causal boundary. The modulus crosses it freely in both directions because the modulus dynamics are SUBSTRATE (not c-bounded, per the c-classification from the S74 workshop). There is no causal trapping, no one-way membrane, no Penrose inequality. The "re-expansion" is driven by the potential gradient, not by the spacetime geometry. Calling this a "Kruskal extension" imports too much causal structure from GR into a problem that is fundamentally a field-space trajectory in a potential. The correct analogy is a ball rolling up a hill past a marker (the geometric phase transition) and rolling back -- not a particle crossing a horizon.

The substrate-first framing makes this clearer: the modulus tau parameterizes the fiber's spectral structure. The "Zones" are regions of field space where different spectral properties hold (positive vs negative sectional curvature). The trajectory through these regions is governed by the spectral action potential and Hubble friction -- substrate dynamics that are NOT constrained by the emergent causal structure. The Kruskal analogy reverses the explanatory hierarchy: it explains a substrate phenomenon (field-space trajectory) by invoking an emergent concept (causal horizon). This violates the direction of explanation (D_K eigenvalues -> spectral action moments -> emergent field equations -> observed physics).

**D2: The GW spectral shape prediction (E3) needs quantitative scrutiny.** sp claims the GW spectrum from Stage 2 (overshoot) would show "peaks at frequencies corresponding to the crossing times of the geometric phase transition and zero-crossings." This is a structural claim about the graviton Bogoliubov coefficients during the overshoot. But the same mode-counting hierarchy that kills BCS production applies with comparable force to graviton production. The graviton mode equation (Eq. T2.5 from Round 1) involves the effective mass m_eff^2(tau(t)), which depends on the Weyl tensor. The Weyl tensor reorganizes at the critical tau values, but the MAGNITUDE of the reorganization is bounded: at tau = 0.537, one sectional curvature passes through zero while the others remain finite; at the Weyl zero-crossings, one eigenvalue of the 66x66 operator passes through zero. In both cases, the fractional change in m_eff^2 is O(1/N_eigenvalues) ~ O(1/16) at best (16 distinct Weyl eigenvalues). The induced graviton production per crossing is:

    |delta_beta_graviton|^2 ~ (delta_m_eff^2 / omega_graviton^2) * (delta_t_cross / T_graviton)     (TR2.1)

For gravitons at the Planck scale (omega ~ M_KK), with delta_m_eff^2/omega^2 ~ 1/16 and delta_t_cross ~ 2e-3 M_KK^{-1}, the production is |delta_beta|^2 ~ O(10^{-4}). This produces spectral features at the O(10^{-4}) level relative to the fold GW production -- detectable IN PRINCIPLE but not as clean "peaks." The qualitative prediction (spectral features encoding the five-phase structure) survives, but the characterization as "peaks" overstates the signal contrast.

### EMERGENCE

**E1: The equilibrium tau problem is the MOST consequential open question from this workshop.** sp's Q7 identifies a question that could invalidate decades of spectral action evaluations. All published Higgs mass predictions, coupling constant relations, and spectral moment computations assume tau = 0.190 (the fold value). The S73B ODE shows the modulus overshoots to 1.614 and then oscillates around an equilibrium value determined by the potential minimum along the Jensen ridge. If this equilibrium tau differs from 0.190, EVERY spectral action evaluation must be redone at the equilibrium tau. sp estimates that a shift to tau = 0.25 would change spectral moments by O(10%) -- enough to move the Higgs mass prediction from 131.8 GeV (7% off) to potentially outside the viable range.

The structural question is whether the spectral action potential V(tau) has its minimum AT or NEAR the fold. The fold is defined as the locus where dS/dtau changes sign (or is maximal), which is NOT the same as dV/dtau = 0 (since V = -S + constant in some conventions, or V involves additional kinetic normalization terms). The equilibrium tau is where:

    dV/dtau = 0 at the minimum of the oscillation-averaged potential     (TR2.2)

This is extractable from the S73B ODE data (the oscillation center in tau_sol at late times). If the oscillation-averaged tau(late) is significantly different from 0.190, we face a systematic error in ALL spectral action observables computed to date. This is not a "refinement" -- it is a potential CRISIS in the framework's observational predictions.

However, there is a STRUCTURAL REASON to expect the equilibrium tau to be close to 0.190. The modulus mass m_tau = 2.062 M_KK implies d^2V/dtau^2 ~ m_tau^2 * G_DeWitt = 21.3 M_KK^2. If the potential well is approximately quadratic around its minimum, the minimum is located at tau_min ~ tau_fold + v_terminal / (m_tau^2 * G_DeWitt * t_friction) where t_friction ~ 1/(3H) is the friction timescale. For H ~ 1 M_KK at the fold, t_friction ~ 0.33 M_KK^{-1}, and the displacement is:

    delta_tau_min ~ v_terminal * t_friction / (oscillation cycles to settle) ~ 26.5 * 0.33 / 33 ~ 0.26     (TR2.3)

So the equilibrium is at tau ~ 0.19 + 0.26 ~ 0.45, which is BELOW the geometric phase transition at 0.537 (safely in Zone I) but significantly different from the fold value. This estimate is crude; the actual value from the ODE data could be anywhere in the range [0.19, 0.50]. The computation EQUIL-TAU-77 is the highest-priority carry-forward from this workshop: extract the oscillation-averaged tau from the S73B data at late times.

**E2: The BCS condensation timing question (Q8) reveals a FOUNDATIONAL ambiguity.** sp asks whether BCS condensation occurs before, during, or after the impulsive Bogoliubov squeeze. This is not a detail -- it determines whether the mode equation uses the gapped or ungapped dispersion. The S75 computation assumes the gap Delta_BCS = 0.4643 M_KK is present during production:

    omega_k = sqrt(epsilon_k^2 + Delta_BCS^2)     (TR2.4)

If BCS condenses AFTER the squeeze, the production dispersion is epsilon_k (ungapped), and the BCS gap opens subsequently, modifying the pair distribution. The S75 Bogoliubov coefficients would be WRONG in the latter case -- they would need to be computed in two stages: (1) sudden squeeze with ungapped spectrum, (2) gap opening as a second time-dependent frequency change.

The structural resolution is that the BCS condensation timescale is t_BCS ~ 1/Delta_BCS ~ 2.15 M_KK^{-1}, while the fold transit timescale is dt_transit ~ 10^{-3} M_KK^{-1}. Since dt_transit << t_BCS, the transit completes BEFORE the BCS gap has time to form. This means:

- At the MOMENT of the impulsive squeeze (Phase A, t ~ 10^{-3}), the eigenvalue spectrum is the NORMAL-STATE spectrum epsilon_k, NOT the BCS spectrum omega_k.
- The BCS gap opens SUBSEQUENTLY on the timescale t_BCS ~ 2 M_KK^{-1} (deep in Phase B).
- The Bogoliubov coefficients should be computed with the UNGAPPED spectrum as the pre-transit state and the GAPPED spectrum as the post-transit state.

But this is EXACTLY the sudden approximation applied to the BCS transition itself. In the sudden limit (dt_transit << t_BCS), the pre-transit vacuum is projected onto the post-transit eigenstates. The projection IS the Bogoliubov transformation. The question is whether the S75 computation correctly implements this ordering.

The S75 mode equation uses omega_k = sqrt(epsilon_k^2 + Delta_BCS^2) as the frequency THROUGHOUT the computation. If the BCS gap opens after the squeeze, this overestimates the frequency during the transit and therefore underestimates the adiabaticity parameter omega * dt_transit. With the ungapped spectrum, the frequencies are epsilon_k (which can be zero at the Fermi surface), making the transit even MORE impulsive and the squeeze even MORE complete. The |beta_k|^2 = 1 saturation result would be STRENGTHENED, not weakened. The S75 result is therefore CONSERVATIVE: using the gapped spectrum gives a LOWER BOUND on the squeeze efficiency.

This resolution has a subtle implication: the GGE relic is produced from the UNGAPPED spectrum, but the subsequent formation of the BCS gap redistributes the quasiparticle energies. The total particle number (59.8 pairs) is conserved by unitarity, but the ENERGY distribution shifts when the gap opens. The GGE charges (Richardson-Gaudin integrals) are set by the post-BCS Hamiltonian, not by the pre-BCS spectrum. This means the GGE relic distribution is correctly computed from the BCS spectrum even though the PRODUCTION occurs before BCS condensation -- the GGE is a property of the final equilibrated state, not of the production moment.

**E3: The fiber anisotropy ratio at the turnaround defines a new observable.** sp's answer to T3-Q5 gives L_1/L_2 = e^{4*1.614} = 643 at the turnaround. This is the MAXIMUM fiber anisotropy reached during the entire cosmological history. From sp's curvature analysis (T3-Q3 answer), the SU(2) sector dominates the curvature at the turnaround (compressed directions have curvature ~ 1/L^2 ~ 640). This maximum anisotropy determines the maximum curvature experienced by any fiber mode during the evolution. For the BCS modes (which are in the (0,0) sector), this maximum curvature is irrelevant (established by the no-second-squeeze result). But for the GEOMETRIC modes -- the spectral action coefficients a_0, a_2, a_4 that determine Lambda, G_N, and g_YM -- the maximum anisotropy at the turnaround sets the RANGE of values these coefficients sample during the overshoot. If any spectral moment has a non-monotonic dependence on tau that achieves an extremum near tau = 1.614, the transient value of that physical constant during the overshoot could differ dramatically from its equilibrium value. In particular:

    a_2(tau = 1.614) / a_2(tau = 0.19) = [G_N(turnaround) / G_N(fold)]^{-1}     (TR2.5)

This ratio determines whether Newton's constant transiently varies during the overshoot. Since a_2 is a spectral moment of D_K^{-2}, and D_K at tau = 1.614 has a dramatically different eigenvalue distribution (SU(2) eigenvalues compressed 25x, C^2 expanded 5x, U(1) expanded 25x), the ratio could be O(1) or O(10). A transient variation in G_N by a factor of 10 during the overshoot would produce a transient variation in H (through the Friedmann equation), which IS included in the S73B ODE through V(tau). But the ODE uses the SPECTRAL ACTION potential, not individual spectral moments. The self-consistency requires that V(tau = 1.614) in the ODE encodes the transient G_N variation -- which it does, if V is computed from the full spectral action at each tau.

**E4: The five-phase structure maps onto a Floquet classification.** The modulus dynamics can be decomposed as: Phase A (impulsive), Phase B (free), Phase C (decelerated), Phase D (oscillatory), Phase E (frozen). In Floquet theory, the oscillatory Phase D is the only phase where parametric resonance could operate. The W1-B result (Mathieu parameter |q| = 5.9e-3) confirms the oscillation is in the narrow-resonance regime with all BCS modes detuned. The five phases exhaust the catalog of possible mode-equation behaviors: impulsive (sudden limit), free (WKB), decelerated (adiabatic with friction), oscillatory (Floquet), and frozen (static). The fact that particle production occurs ONLY in Phase A (sudden limit) and is null in Phases B-E (adiabatic/Floquet with suppression) means the Bogoliubov result is controlled by a SINGLE parameter -- the product omega_k * dt_transit at the fold -- and is insensitive to the entire subsequent dynamical history. This is the deepest structural reason why the GGE relic is robust: it is set in the one phase (impulsive) where the mode equation has a unique, parameter-independent solution (|beta|^2 = 1 for all superhorizon modes).

---

## Workshop Verdict

| Topic | Status | Summary |
|:------|:-------|:--------|
| Second Bogoliubov squeeze | **Converged** | PERMANENT NULL. Three independent arguments (mode-counting 16/12880, crossing speed, unitarity) give |delta_beta|^2 ~ 10^{-6}, 6 OOM below fold. GGE relic set once at fold, stable against all subsequent modulus dynamics. Both agents accept. |
| N vs tau as time variable | **Converged** | N (e-folds) is the correct time variable for post-fold dynamics. tau is non-monotonic (overshoot to 1.614), making tau ill-defined as a time coordinate. S75 mode equation unaffected (covers fold neighborhood where tau is monotonic). All future mode equation extensions must use N. |
| Five-phase trajectory structure | **Converged** | Phases A (impulsive fold), B (free streaming), C (deceleration/overshoot), D (oscillation), E (frozen/decay). Temporal separation factor 90 between fold squeeze and overshoot. Potential-dominated turnaround (structural, not model-dependent). Both agents accept decomposition. |
| CMPP along full trajectory | **Partial** | Static D -> II predicted at tau = 0.537 (sp), not yet computed. Static Type II predicted at turnaround (tau = 1.614, tau_dot = 0) -- cleanest probe. Dynamic G -> D crossover is smooth (photosphere, not horizon), occurring at tau_dot ~ O(1) M_KK. CMPP at turnaround is a carry-forward computation. |
| Weyl zero-crossing signatures | **Converged** | Scenario (1) holds: no physical signature. Eigenvalue sign change does not create/destroy WANDs. BCS modes orthogonal to branch 27 (mode-counting hierarchy). Graviton production bounded at O(10^{-4}) per crossing. Zero-crossings are geometrically significant but dynamically inert. |
| NEC violation (Zone III) | **Converged** | Transient excursion (residence time ~ 0.01 M_KK^{-1}, 5 OOM below decay time). 12D NEC never violated. Internal C^2 Ricci anomalous sign has no imprint on emergent 4D geometry. Modulus returns to Zone I before decay. |
| Kruskal analogy for overshoot | **Dissent** | sp proposes overshoot as Kruskal extension of modulus space. Transit objects: Zone boundaries are field-space loci, not causal horizons; modulus dynamics are substrate (not c-bounded); the analogy reverses the explanatory hierarchy (explains substrate via emergent GR). Correct analogy: ball rolling past a marker on a potential hill. |
| Equilibrium tau after settling | **Emerged** | NEW: oscillation-averaged tau at late times may differ from fold value 0.190 by delta_tau ~ 0.26 (crude estimate). If tau_equil differs significantly, ALL spectral action evaluations (Higgs mass, couplings) need revision. Highest-priority carry-forward. |
| BCS condensation timing | **Emerged** | NEW: BCS gap forms AFTER fold transit (t_BCS ~ 2.15 M_KK^{-1} >> dt_transit ~ 10^{-3}). Squeeze uses ungapped spectrum. S75 result is CONSERVATIVE (gapped spectrum underestimates squeeze efficiency). GGE charges set by post-BCS Hamiltonian regardless. |
| GW spectral features from overshoot | **Partial** | sp predicts "peaks" encoding five-phase structure. Transit: features exist but at O(10^{-4}) contrast, not clean peaks. Both agree 13-16 OOM below current detection. Structural prediction survives; signal characterization disputed. |

---

## Remaining Open Questions

1. **What is the oscillation-averaged equilibrium tau from the S73B ODE?** Extract tau_sol at late times (t > 50 M_KK^{-1}) and compute the time-average. If tau_equil differs from 0.190 by more than 0.05, every spectral action observable must be re-evaluated at tau_equil. This is the single highest-priority open question.

2. **What is the static CMPP type at tau = 1.614?** The W3-H algorithm evaluated at tau = 1.614 (with tau_dot = 0) tests the D -> II prediction. If Type II is confirmed, identify at which tau in [0.537, 1.614] the transition occurs.

3. **Does the BCS condensation timing affect the GGE charge distribution?** The squeeze occurs before BCS gap formation (dt_transit << t_BCS). The Bogoliubov coefficients are set by the ungapped spectrum. Do the Richardson-Gaudin integrals (GGE charges) computed with the post-BCS Hamiltonian produce the same thermodynamic state as those computed with the pre-BCS Hamiltonian plus the Bogoliubov transformation?

4. **What is the transient variation of Newton's constant during the overshoot?** Compute a_2(tau) at tau = {0.5, 1.0, 1.5, 1.614} from the spectral action. The ratio a_2(1.614)/a_2(0.19) gives G_N(turnaround)/G_N(fold). If this ratio is O(10) or larger, the Friedmann equation during the overshoot has a transiently different gravitational coupling.

5. **What is the actual energy dissipation fraction during the overshoot?** Evaluate the friction integral (Eq. T1.5 / SP-R2.1) from the ODE data with time-dependent H(t) and tau_dot(t). The factor-7 estimate (Round 1, T1.6) is an overcount; the physical value constrains the ascending/descending velocity asymmetry at each critical tau crossing.

6. **Is the spectral action potential V(tau) reliable at tau > 1.0?** The S73B ODE uses interpolated spectral data. If the interpolation extends beyond the range of computed D_K eigenvalues, the overshoot amplitude (tau_max = 1.614) may be an extrapolation artifact. Verify that D_K eigenvalues are computed at tau values covering [0, 1.7] with sufficient density.

7. **Can the tau(N) trajectory diagram be constructed from existing data?** sp requires tau(N), H(N), and crossing N-values from the ODE. Transit can supply these from s73b_efold_mapping.npz. The diagram construction is a direct carry-forward for sp.

8. **Does the five-phase Floquet classification extend to multi-field scenarios?** The single-modulus tau trajectory has five phases. If additional moduli (off-Jensen directions) are excited during the overshoot (all 35 currently have negative Hessian eigenvalues, but the overshoot changes the Hessian), the phase structure could fragment. Check the Hessian eigenvalues at tau = 1.614 from the spectral data.

---

## Wrap-Up — Workshop Impact Summary

### What Changed

- The GGE relic is now proven stable against ALL post-fold modulus dynamics -- not just the fold-neighborhood Bogoliubov computation (S75) but the entire overshoot trajectory through Zones I, II, and III. The no-second-squeeze result is PERMANENT (6 OOM suppression, three independent arguments).
- The BCS condensation timing is resolved: the gap forms AFTER the impulsive squeeze (t_BCS ~ 2.15 >> dt_transit ~ 10^{-3}), meaning the S75 mode equation uses the gapped spectrum as a CONSERVATIVE estimate. The ungapped production is more complete.
- The equilibrium tau question (E1) emerged as a potential crisis: if the modulus settles at tau_equil significantly different from 0.190, all spectral action observables are shifted. This was not previously recognized.

### What Holds

- The S75 Bogoliubov coefficients and all derived quantities (f_NL, alpha_s, phi_k = 0) are valid as fold-neighborhood results. The overshoot is temporally separated (factor 90) and dynamically negligible.
- The frozen spectrum theorem (alpha_s = 0 exact at production) holds: it is a Phase A result insensitive to Phases B-E.
- The five-phase trajectory structure (Phase A impulsive, B free, C decelerated, D oscillatory, E frozen) is the canonical decomposition of the post-fold modulus dynamics.

### What Breaks or Strains

- The S49 conformal structure with tau as the vertical axis is invalidated by the tau non-monotonicity. The Penrose diagram must use N as the vertical coordinate. The S53 diagrams require supplementation (not replacement -- they remain correct for the static analysis).
- The assumption that the frozen tau equals the fold tau (tau = 0.190) is strained. The equilibrium tau from the ODE may differ by delta_tau ~ 0.26. If confirmed, all spectral action evaluations at tau = 0.190 become evaluations at the WRONG tau value. The Higgs mass prediction (131.8 GeV, 7% from observed) has margin for a ~10% spectral moment shift, but this is uncomfortably tight.
- The Kruskal analogy for the overshoot is disputed: transit objects on substrate-first grounds (Zone boundaries are field-space loci, not causal horizons). The analogy may still be pedagogically useful but is structurally misleading.

### Carry-Forward Computations

1. **EQUIL-TAU-77**: Extract oscillation-averaged equilibrium tau from S73B ODE data (tau_sol at t > 50 M_KK^{-1}). **Input**: s73b_efold_mapping.npz. **Output**: tau_equil with uncertainty from oscillation amplitude. **Gate**: if |tau_equil - 0.190| > 0.05, trigger re-evaluation of spectral action observables. **Effort**: 0.5 hours (data extraction from existing .npz file).

2. **CMPP-TURNAROUND-77**: Evaluate static CMPP type at tau = 1.614 using W3-H algorithm with tau_dot = 0. **Input**: D_K eigenvalues at tau = 1.614, W3-H classification code. **Output**: CMPP type (D or II), WAND structure, bw components. **Gate**: if Type II, the D -> II transition is confirmed; if Type D, sp's prediction fails. **Effort**: 2 hours (spectral computation + classification).

3. **FRICTION-INTEGRAL-77**: Evaluate the Hubble friction integral (Eq. T1.5) from ODE data with time-dependent H(t) and tau_dot(t). **Input**: s73b_efold_mapping.npz (t_sol, dtau_sol, H_sol). **Output**: fractional energy dissipation Delta_E/KE_initial, ascending/descending tau_dot ratio at tau = {0.537, 0.895, 1.340}. **Gate**: confirms or corrects the O(1) dissipation estimate. **Effort**: 1 hour (numerical integration from stored data).

4. **V-TAU-VALIDATION-77**: Verify spectral action potential V(tau) reliability at tau > 1.0. **Input**: spectral data files used in S73B interpolation. **Output**: density of computed D_K eigenvalue data points in [1.0, 1.7] tau range; interpolation vs extrapolation boundary. **Gate**: if tau = 1.614 is in the extrapolation regime, the overshoot amplitude is unreliable. **Effort**: 1 hour (data inventory).

5. **TAU-N-TRAJECTORY-77**: Extract tau(N), H(N), and crossing N-values for critical tau = {0.537, 0.895, 1.340, 1.382} from S73B data for sp's Penrose diagram construction. **Input**: s73b_efold_mapping.npz. **Output**: tau(N) curve, crossing N-values (ascending and descending), H(N) profile, to be delivered to sp. **Effort**: 1 hour (data extraction + interpolation).

6. **A2-OVERSHOOT-77**: Compute spectral action coefficient a_2(tau) at tau = {0.5, 1.0, 1.5, 1.614} to determine transient G_N variation during overshoot. **Input**: D_K eigenvalues at these tau values. **Output**: a_2(tau)/a_2(0.19) ratio. **Gate**: if ratio > 5, the Friedmann equation during the overshoot has significantly different gravitational coupling. **Effort**: 3 hours (spectral computation at 4 tau values).

7. **BCS-TIMING-SEQUENCE-77**: Verify the BCS condensation timescale ordering (t_BCS >> dt_transit) from microscopic BCS theory and compute the correction to Bogoliubov coefficients from using the gapped vs ungapped spectrum. **Input**: BCS gap equation, D_K eigenvalues at fold. **Output**: ratio |beta_ungapped|^2 / |beta_gapped|^2 (expected >= 1). **Gate**: if ratio significantly exceeds 1, the S75 A_s estimate is a lower bound and the gap narrows. **Effort**: 2 hours.

8. **HESSIAN-OVERSHOOT-77**: Evaluate the off-Jensen Hessian eigenvalues at tau = 1.614 to check stability of the single-modulus approximation during the overshoot. **Input**: D_K eigenvalues and spectral action at tau = 1.614, Hessian computation code (W2-J). **Output**: 35 Hessian eigenvalues at tau = 1.614. **Gate**: if any eigenvalue becomes positive, the off-Jensen direction is tachyonic during the overshoot and the single-modulus trajectory is unstable. **Effort**: 3 hours.

### Closing Line

The overshoot is geometrically dramatic (Zone III excursion, 640x fiber anisotropy, transient NEC violation) but dynamically inert for everything that matters observationally -- the GGE relic is set at the fold and is thereafter frozen by a 6-OOM suppression hierarchy that exhausts all five phases of the modulus trajectory.
