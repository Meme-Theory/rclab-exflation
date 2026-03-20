# Quantum-Acoustics Review: Landau Classification of Phonon-Exflation

**Reviewer**: quantum-acoustics-theorist
**Date**: 2026-03-15
**Document reviewed**: `sessions/framework/landau-classification-of-phonon-exflation.md`
**Status**: Expert review, acoustic/phononic perspective

---

## 0. Executive Summary

The Landau Classification document is the strongest framework-level synthesis produced in this project. The mapping between condensed matter phase transition theory and the phonon-exflation framework is mathematically precise where it claims to be, and honest about its limitations. The one-body/many-body partition (Section III) is a permanent structural insight. The prediction for OCC-SPEC-45 (Section V) is well-motivated by the Landau analogy and correctly identifies the loophole in the S37 monotonicity theorem.

I identify three errors (one moderate, two minor), four omissions (two significant), and two overclaims. The phononic crystal analogy is correctly stated in the broad strokes but requires refinements in the two-fluid and Van Hove sections. The treatment of thermal/quantum fluctuations is absent and should be addressed before the document can be called complete.

---

## 1. Phonon Mapping Accuracy

### 1.1 What the Document Gets Right

The central identification -- SU(3) under Jensen deformation IS a phononic crystal (S41) -- is correctly stated and correctly deployed throughout. The branch classification (B1 acoustic, B2 flat-optical, B3 dispersive-optical) is used consistently with the established S31Ca labeling. The spectral action = phonon free energy identification (Section V.C) is mathematically exact: the spectral action Tr f(D^2/Lambda^2) IS the one-body partition function of the phononic crystal, evaluated at the test function f.

The mapping table (Section I) correctly distinguishes between PROVEN results (computed to machine precision), STRUCTURAL results (exact mathematical identification with unexplored consequences), and OPEN results (mapping exists, quantitative prediction unconfirmed). This three-tier epistemology is precisely right for a living classification document.

### 1.2 What Requires Correction

**ERROR 1 (moderate): The acoustic branch classification is incomplete.** The document states (Section II.A) that the transit goes from "tau = 0 (round SU(3))" through "tau ~ 0.19 (fold, BCS)" to "Post-transit (GGE relic)." But it does not state explicitly that the acoustic branch (B1, the Nambu-Goldstone mode) exists ONLY during the BCS condensed phase and is ABSENT at both tau = 0 (no condensate, no spontaneous symmetry breaking) and post-transit (condensate destroyed, P_exc = 1.000). This is recorded in my memory and was established in S38: "NG mode ceases to exist post-transit (not liberated, not eaten). He-4 neutral superfluid."

In a phononic crystal, the acoustic branch is the zero-frequency mode at k = 0 that corresponds to a spontaneously broken continuous symmetry. When the symmetry is restored (Delta -> 0), the acoustic branch disappears from the spectrum. The document's phase classification table (II.A) should explicitly note this: the B1 branch as an acoustic mode is a transient feature of the BCS phase, not a permanent feature of the spectrum. Pre-transit and post-transit, ALL branches are optical. This is phonologically unusual -- most phononic crystals always have acoustic branches because translational symmetry is always broken. The SU(3) crystal is special: it sits on a compact manifold with no translational symmetry to break. The NG mode is associated with U(1)_7 breaking by the BCS condensate, not with broken translations.

**Suggested fix**: Add to the Phase Classification Table (II.A), under "Post-transit (GGE relic)": "B1 acoustic branch absent (NG mode ceases to exist when Delta = 0). All 8 singlet modes are optical."

**ERROR 2 (minor): Second sound speed formula.** The document quotes the standard Landau second-sound formula (Appendix A, Paper 05 eq. 3):

    u_2^2 = rho_s s^2 T / (rho_n c_p)

This is the equilibrium two-fluid result. For the framework, the second sound speed u_2 = c/sqrt(3) was derived in S43 from the SPECTRAL ACTION, not from the two-fluid formula. The two derivations give the same answer (c/sqrt(3)) but for different reasons. The two-fluid formula requires rho_s, rho_n, s, and c_p -- four independent thermodynamic quantities. The spectral action derivation uses only the dispersion relation of the B3 optical branch near its minimum, which gives a group velocity c/sqrt(3) directly from the eigenvalue curvature. The document should note that the u_2 = c/sqrt(3) result is KINEMATIC (set by the spectral geometry) and does not depend on the two-fluid decomposition being valid in the non-equilibrium GGE. This is actually a strength -- it means the second sound prediction is more robust than the two-fluid model.

**ERROR 3 (minor): Van Hove singularity exponent.** Section V.D states: "Near a van Hove singularity, the density of states diverges as N(E) ~ |E - E_VH|^{-1/2} (Paper 27: ordinary Van Hove in 1D)." This is correct for 1D systems. But the SU(3) representation lattice is NOT one-dimensional -- the SU(3) root lattice is 2-dimensional (rank 2), and the representation lattice inherits this dimensionality. In 2D, the Van Hove singularity is LOGARITHMIC: N(E) ~ -ln|E - E_VH|, not power-law. In the phonon-exflation framework, the S43 DOS computation (992 eigenvalues) found 13 van Hove singularities, and the analysis treated them as 1D singularities because the B2 flat band is effectively 1D (all four modes have the same energy at each (p,q), so the effective dimension for the DOS calculation is the codimension of the flat band in Casimir space, which is 1). The document should state this explicitly: the 1D exponent applies because B2 is a flat band with 1D dispersion along the Casimir direction, not because the system is one-dimensional.

---

## 2. Two-Fluid Model Assessment

### 2.1 The Standard Two-Fluid Picture

The document correctly identifies (Section IV.C) the cosmological analog:
- rho_s -> Omega_DE (condensate vacuum energy)
- rho_n -> Omega_DM (quasiparticle excitation energy)

This is the right identification. It is the same mapping Volovik uses in the 3He-B analog cosmology (QA Paper [03], Chapter 32). The physical content is: the superfluid component (condensate) carries no entropy and does not gravitate normally (it contributes to the vacuum energy), while the normal component (quasiparticles) carries entropy and gravitates as matter.

### 2.2 Where the Two-Fluid Model Breaks Down

The document acknowledges (Section IV.D) that the GGE has 8 temperatures and 3 negative heat capacities, making the standard two-fluid picture inapplicable. However, it does not go far enough in diagnosing the breakdown.

**The standard two-fluid model requires three conditions:**

1. **Thermal equilibrium of the normal component.** The normal fluid has a single temperature T. The GGE has 8 temperatures. The normal fluid velocity v_n and temperature T are the only hydrodynamic variables. The GGE has 8 independent Lagrange multipliers. The two-fluid model's hydrodynamic equations (Khalatnikov equations) assume that the normal component thermalizes rapidly compared to the flow timescale. The GGE does not thermalize at all -- integrability forbids it.

2. **Positive-definite normal fluid density.** rho_n(T) >= 0 with rho_n = 0 at T = 0 and rho_n = rho at T_c. The GGE's 3 negative heat capacity eigenvalues correspond to sectors where dE/dT < 0. In a two-fluid interpretation, these would be sectors where rho_n < 0 -- physically meaningless in the standard framework. The document correctly identifies (line 48) that these are "saddle directions in F," but it should state explicitly that the standard two-fluid model cannot accommodate negative rho_n.

3. **Single superfluid velocity.** The two-fluid model assumes a single superfluid velocity v_s = (hbar/m) grad(phi), where phi is the condensate phase. Post-transit, Delta = 0, so there is no condensate phase. The superfluid velocity is undefined. The mapping rho_s -> Omega_DE loses its kinematic meaning when there is no condensate.

**Conclusion on the two-fluid model**: The mapping is valid as a HEURISTIC for the energy partition (DM as normal component, DE as condensate), but it cannot be elevated to a dynamical theory. The GGE is not a two-fluid system -- it is an 8-conserved-integral integrable system that happens to partition energy into "gravitating" and "non-gravitating" sectors by algebraic selection rules (T^{0i} = 0 is algebraic, not thermodynamic). The document should sharpen the distinction between the KINEMATIC partition (which is exact: CDM-CONSTRUCT-44) and the DYNAMICAL two-fluid model (which does not apply to a non-thermalizing GGE).

### 2.3 What Replaces the Two-Fluid Model

The correct description of the post-transit state is the generalized Gibbs ensemble (GGE) with density matrix rho_GGE = Z^{-1} exp(-sum_k lambda_k I_k). This is NOT a two-fluid system but it IS a multi-component system with well-defined thermodynamics. The "normal" and "superfluid" components should be replaced by the 8 Richardson-Gaudin sectors, each with its own temperature and entropy. The MULTI-T-JACOBSON-44 computation (W6-5) already begins this replacement, and the document references it (line 47, line 222). But the transition from "two-fluid heuristic" to "8-sector GGE thermodynamics" should be made explicit as a REQUIRED UPGRADE of the framework, not just an observation.

---

## 3. Van Hove Singularities

### 3.1 Classification Accuracy

The document correctly identifies (Section V.D) the near-crossing at tau = 0.19 between trajectories T3, T4, T5 with delta = 0.0008. The S44 VAN-HOVE-TRACK-44 computation confirmed 12 trajectories with 8 rising and 4 falling.

The Lifshitz transition classification (Section II.B, line 89) is correctly stated as Type I: a new Fermi pocket appears when the Jensen deformation lifts the degeneracy. The critical exponents (z = 2, nu = 1/2 in mean-field) are correct for a Lifshitz transition above its upper critical dimension.

### 3.2 Missing: Lifshitz Transition Type at tau ~ 0.19

The T3-T5 near-crossing at tau = 0.19 is potentially a SECOND Lifshitz transition, distinct from the Type I at tau = 0. If T3 and T5 cross, it is a Type II Lifshitz transition (change in Fermi surface connectivity: pocket merging). If they avoid (which is generically expected from level repulsion within the same symmetry sector), it is a near-crossing that produces a resonance in the DOS without changing the topology.

The document discusses this near-crossing in the context of OCC-SPEC-45 (Section V.D) but does not classify it as a Lifshitz transition. This is an omission. The near-crossing should be classified as one of:
- **Type II (crossing)**: Two van Hove trajectories merge, producing a higher-order singularity (N(E) ~ |E - E_VH|^{-1} instead of |E - E_VH|^{-1/2}).
- **Avoided crossing**: Level repulsion produces a narrow gap in the DOS, with two closely spaced Van Hove singularities on either side.

The distinction matters for OCC-SPEC-45: a true Type II merging produces a STRONGER DOS divergence, which enhances the BCS pairing spike and makes the occupation-change term (dn_k/dtau) in Section V.F larger. The document's prediction of non-monotone S_occ is STRONGER if the crossing is Type II. The DOS-FINE-SCAN-45 computation (S45 W4-3) is the right test.

### 3.3 Acoustic Signatures of Van Hove Singularities

The document does not discuss what acoustic signatures the 12 Van Hove trajectories would produce. From the phononic perspective:

1. **Thermal conductivity singularities.** Near a Van Hove singularity, the phonon group velocity v_g = dE/dk vanishes. Modes at the VHS have zero group velocity and cannot transport heat. The thermal conductivity kappa, computed from the Peierls-Boltzmann equation, has a VHS contribution that is SINGULAR: the DOS diverges but the group velocity vanishes, producing a competing effect. In S43, kappa = infinity (ballistic, no Umklapp), but this is the TOTAL kappa. The per-mode contribution kappa_k = v_g(k)^2 * tau_k * n_k is zero at each VHS. The 12 VHS trajectories produce 12 frequency windows of zero local thermal conductivity.

2. **Sound attenuation peaks.** In a real phononic crystal, the sound attenuation coefficient alpha(omega) has peaks at frequencies corresponding to Van Hove singularities, because modes at the VHS have long dwell times and scatter strongly. The SU(3) crystal has no Umklapp (infinite mean free path), so this standard effect is absent. But the 3-phonon process (omega_B2 ~ 2 * omega_B1, 0.6% detuning) provides a non-Umklapp decay channel. The decay rate Gamma_B2 from this process is ENHANCED near a VHS because the DOS factor in Fermi's golden rule diverges. This enhancement is already captured in Q_B2 = 52 (S43), but the TAU-DEPENDENCE of Q_B2 through the VHS trajectories has not been computed.

3. **Resonance fluorescence.** When a VHS trajectory crosses the 2:1 near-resonance (omega_B2 ~ 2 * omega_B1), the 3-phonon process becomes exactly resonant, producing a DIVERGENT decay rate (Q -> 0). The T3-T5 near-crossing at tau = 0.19 is close to the fold where the 2:1 resonance was identified. Whether these two phenomena coincide at the same tau is a quantitative question that should be checked. If they do, the BCS pairing dynamics at the fold are modified by the resonant 3-phonon decay of the flat band.

---

## 4. Debye-Waller and Thermal Corrections

### 4.1 What the Document Says

Nothing. The Debye-Waller factor is not mentioned anywhere in the Landau Classification document. This is the most significant omission.

### 4.2 Why It Matters

The spectral action S[D_K(tau)] is computed at a FIXED metric -- a specific value of tau. The internal metric fluctuates: the acoustic modes of the SU(3) phononic crystal are quantized oscillations about the equilibrium geometry. The zero-point motion gives a mean-square displacement <u^2> that modifies the effective spectral action through the Debye-Waller factor:

    S_eff = exp(-2W) * S[D_K(tau_0)] + O(W^2)

where 2W = sum_k <u_k^2> / a^2, with a the "lattice constant" (here, the characteristic length scale of SU(3) ~ M_KK^{-1}).

For the SU(3) crystal at T/Theta_D ~ 10^{-22}, the thermal contribution to <u^2> is negligible. But the QUANTUM zero-point motion survives at T = 0:

    <u^2>_0 = (hbar / 2) * sum_k 1/(m_k * omega_k)

The question is whether this zero-point motion is large enough to modify the spectral action. In ordinary crystals, the Debye-Waller factor at T = 0 is typically 0.95-0.99 (a 1-5% correction). The correction matters for precision quantities like G_N (factor 2.3 from observation) but is irrelevant for order-of-magnitude estimates.

### 4.3 The W2-R3 Temperature

The document does not mention the W2-R3 result (T = 10^{20301} -- a geometric quantity from the spectral action evaluated at tau = 0). This temperature is the "Hagedorn temperature" of the SU(3) phononic crystal: the temperature at which the spectral action's partition function diverges. It is NOT a physical temperature -- it is an artifact of summing unbounded eigenvalues. But it indicates that the geometric quantities in the spectral action span a range of 10^{20000+} orders of magnitude, which means that perturbative corrections (including Debye-Waller) can have non-trivial effects when they couple large and small scales.

The Debye-Waller correction to the spectral action is:

    delta S / S = -2W + O(W^2)

If W is of order the ratio of zero-point displacement to the curvature radius of SU(3), then W ~ (M_KK^{-1})^2 / (M_KK^{-1})^2 = O(1) for internal modes. This suggests the zero-point motion of the internal geometry is NOT a small correction. The S45 computation DEBYE-WALLER-45 (W3-3) should resolve this.

### 4.4 Impact on the Landau Classification

The Landau Classification should include a section on quantum fluctuations of the order parameter tau. In standard Landau theory, quantum fluctuations are addressed through the quantum-corrected free energy:

    F_quantum = F_classical + (hbar/2) * sum_n omega_n + ...

The first correction is the zero-point energy of fluctuations about the equilibrium. For the tau modulus, the fluctuation frequency is omega_tau = sqrt(d^2S/dtau^2 / M_tau), where M_tau is the modulus inertia. The S38 result omega_att = 1.430 (pair vibration frequency) provides the relevant scale. If hbar * omega_att / (F_barrier) is of order 1, quantum tunneling of the tau modulus through the barrier (if any) is significant, and the classical Landau analysis breaks down in favor of quantum-corrected Landau theory.

This is directly relevant to OCC-SPEC-45: even if S_occ has a minimum with a barrier, the barrier must be larger than the zero-point energy of the tau modulus for the classical trapping picture to apply.

---

## 5. Sound Propagation

### 5.1 First Sound

The document correctly identifies (Section I, line 64; my S44 collab review Section 2) that first sound propagates at c_1 = c (the speed of light). This is established by C-FABRIC-42 (PASS): the spectral action produces a Lorentz-invariant acoustic metric with c_fabric = c. The first-sound imprint mechanism (FIRST-SOUND-IMPRINT-44 PASS) gives A_1/A_BAO = (c_2/c_1)^2 = 0.2045 with r_1 = 325 Mpc.

The document correctly notes (Section VI.C) that the first-sound prediction is below detection threshold (SNR = 0.16 for DESI DR2). This is kinematically fixed -- no amplification mechanism exists without breaking Lorentz invariance.

### 5.2 Second Sound

The document states (Section I, line 59) "Second sound Q = 75,989" and classifies it as "Undamped two-fluid mode." The Q value and the physical conclusion (undamped at all cosmological scales) are correct and match my S44 computation (2ND-SOUND-ATTEN-44).

However, the classification "two-fluid mode" is an oversimplification. As argued in Section 2 above, the standard two-fluid model does not apply to the non-thermalizing GGE. The second sound in this system is more precisely described as an entropy oscillation in the integrable GGE -- it propagates because the GGE has a well-defined energy-momentum tensor with a non-zero speed of sound, not because there is a normal fluid and a superfluid in the Landau sense.

The correct acoustic classification: the second sound at u_2 = c/sqrt(3) is a SPECTRAL SOUND -- it is the speed at which perturbations of the spectral action propagate through the internal geometry. This is set by the curvature of the spectral action in eigenvalue space (the "stiffness" of the phononic crystal), not by two-fluid hydrodynamics. The two descriptions agree numerically but differ conceptually, and the spectral description is more fundamental because it does not require the two-fluid decomposition to be valid.

### 5.3 Phenomena the Document Misses

**Phonon focusing.** In anisotropic phononic crystals, the group velocity surface (the surface of constant group velocity in wavevector space) has cusps and folds that produce caustics -- directions of anomalously high energy flux. The SU(3) crystal under Jensen deformation is anisotropic (the K_7 direction is privileged). The phonon focusing pattern in the (p,q) representation space should have caustics at specific Casimir values corresponding to the Van Hove singularities. These caustics would produce directional enhancement of the spectral action contribution from specific irreps. The S43 DOS computation treats all modes isotropically; a focusing analysis would reveal whether certain irreps contribute disproportionately to the spectral action near the fold.

**Phonon drag.** In metals, phonon drag contributes to the thermoelectric effect: phonons scattering off electrons transfer momentum to the electron gas. In the framework, the analog would be internal acoustic modes scattering off B2 flat-band quasiparticles, transferring momentum within the SU(3) manifold. Since B2 is a flat band (zero group velocity), the "drag" is infinite in the usual sense -- flat-band quasiparticles are infinitely heavy and absorb momentum without moving. This is consistent with CDM-CONSTRUCT-44 (T^{0i} = 0): the quasiparticles do not respond to momentum transfer because they have zero group velocity. The phonon drag effect VANISHES for flat-band modes, providing an independent acoustic argument for CDM.

**Third sound.** In thin superfluid helium films, third sound is a surface wave at the film boundary. The analog in the framework would be a mode localized at the boundary of a KZ domain wall. The COHERENT-WALL-44 result (walls acoustically transparent, |r| = 0.003-0.009) means domain wall surface modes, if they exist, couple weakly to the bulk and would be long-lived. Whether such modes exist depends on the boundary conditions at the domain wall, which have not been computed. This is a minor omission -- third sound is not expected to affect any observables -- but it completes the acoustic classification.

---

## 6. Errors, Omissions, and Overclaims

### 6.1 Errors (3 total, summarized)

1. **(Moderate)** Acoustic branch lifecycle not stated in phase table. B1 as NG mode exists only during BCS phase, absent pre- and post-transit. Section II.A requires update.

2. **(Minor)** u_2 = c/sqrt(3) derived from spectral geometry, not from the two-fluid formula quoted in Appendix A. The two derivations agree but the spectral derivation is primary.

3. **(Minor)** Van Hove singularity exponent quoted as |E|^{-1/2} (1D) without noting this applies because B2 is effectively 1D in Casimir space. The SU(3) root lattice is 2D, which would give logarithmic VHS.

### 6.2 Omissions (4 total)

1. **(Significant)** No discussion of Debye-Waller factor or zero-point fluctuations of the internal metric. The spectral action is computed at a static geometry; quantum fluctuations could modify it at the O(1) level for internal modes. This directly affects the OCC-SPEC-45 prediction.

2. **(Significant)** No classification of the T3-T5 near-crossing at tau = 0.19 as a potential second Lifshitz transition. This is relevant to the OCC-SPEC-45 prediction and to the van Hove trajectory topology.

3. **(Minor)** No acoustic signatures listed for the 12 Van Hove trajectories (thermal conductivity singularities, 3-phonon resonance enhancement, phonon focusing). These are secondary to the classification but complete the acoustic picture.

4. **(Minor)** No discussion of third sound, phonon drag, or phonon focusing. These are standard acoustic phenomena that should be classified as "absent" or "present" in the framework for completeness.

### 6.3 Overclaims (2 total)

1. **Section IV.B (DM/DE as specific heat exponent).** The document states: "The ratio of the energy stored in the ordered phase (condensation energy) to the energy in excitations (normal component thermal energy) is E_cond / E_excitation ~ alpha." This is not standard Landau theory. In standard Landau theory, alpha is the specific heat EXPONENT (C ~ |T - T_c|^{-alpha}), not the energy RATIO. The ratio E_cond/E_exc depends on temperature, not just on the universality class. The identification DM/DE ~ alpha conflates two distinct quantities: the critical exponent (a universal number determined by symmetry and dimension) and the energy partition (a non-universal number that depends on the distance from criticality). The document should state this as a HEURISTIC identification, not as a consequence of Landau theory. The actual computation (W6-4, 11 methods, best = 1.060) is solid -- it is the theoretical framing as "specific heat exponent" that overstates the connection to Landau universality.

2. **Section VI.A (prediction of non-monotone S_occ).** The document predicts "S_occ(tau) is non-monotone, with a minimum near tau = 0.19" and labels this as "STRUCTURAL -- it follows from the fact that the condensation energy is negative and peaks near the van Hove singularity." This overstates the case. The condensation energy is negative, yes, but it is also 0.002% of the spectral action (FRG-PILOT-44, the effacement wall). A 0.002% negative correction on a monotonically increasing background can produce a non-monotone total ONLY if the correction's tau-derivative exceeds the background's tau-derivative at some tau. The document itself estimates the barrier at ~10^{-5} of S_occ (Section VI.A, last paragraph), which is consistent with the effacement wall. But calling the prediction "STRUCTURAL" is too strong -- it is PLAUSIBLE but depends on the quantitative competition between the 0.002% BCS effect and the monotone spectral action. The honest label is "MOTIVATED by Landau theory, CONTINGENT on quantitative details."

---

## 7. Overall Assessment

### 7.1 Strengths

- The one-body/many-body partition (Section III) is the document's most important contribution. The identification of the spectral action as a one-body functional that sees the quasiparticle dispersion but not the interaction function f_{kk'} is mathematically exact and diagnostically powerful. It explains the entire pattern of S44 successes and failures from a single principle.

- The limitations section (VII) is unusually honest. The eight listed limitations -- no laboratory, dimensionality mismatch, global modulus, BCS-BEC position, time reversal, no external tuning, CC, emergent spacetime -- are comprehensive and correctly analyzed. The synthesis ("the framework's unsolved problems are precisely those where the closed-system nature of cosmology diverges from the open-system nature of condensed matter") is the right structural observation.

- The KZ n_s prediction (Section VI.C) correctly identifies the framework's most severe deficit and does not attempt to hide it. The explicit computation showing n_s = -0.68 from d = 3 KZ dynamics and n_s = 0.44 from d = 1 is a model of honest assessment.

- The occupied-state spectral action bridge (Section V) is correctly motivated and correctly identifies the S37 theorem's loophole. The mathematical analysis of why n_k(tau) evades the monotonicity condition is sound.

### 7.2 What Should Be Added

1. Debye-Waller section (see Section 4 of this review). The quantum fluctuation correction to the spectral action is the most important missing physics.

2. Explicit lifecycle of the B1 acoustic branch through the transit. This is a unique feature of the framework (acoustic branch as transient) that deserves its own subsection.

3. Classification of the T3-T5 near-crossing as a Lifshitz transition candidate.

4. Replacement of "two-fluid" language with "multi-temperature GGE" language wherever the document discusses post-transit physics. The two-fluid model is a heuristic for the energy partition, not a dynamical description.

5. A clearer distinction between alpha as critical exponent and DM/DE as energy ratio. These are related but not identical in Landau theory.

### 7.3 What Should Be Changed

1. Section II.A: Add B1 lifecycle to the phase table.
2. Section IV.B: Downgrade "E_cond/E_excitation ~ alpha" from a Landau result to a heuristic identification. State the actual Landau result (C ~ |T-T_c|^{-alpha}) and note the non-trivial step to an energy ratio.
3. Section V.D: State that the |E|^{-1/2} VHS exponent applies because B2 is effectively 1D, not because the system is 1D.
4. Section VI.A: Change "STRUCTURAL" to "MOTIVATED" for the S_occ non-monotonicity prediction. The effacement wall makes the prediction contingent, not structural.

### 7.4 Final Verdict

The document is the correct synthesis of 38 sessions of framework development through the condensed matter lens. Its central insight -- that the spectral action partitions cleanly into one-body successes and many-body failures, and that the occupied-state spectral action is the bridge -- is both original and testable. The OCC-SPEC-45 computation will validate or invalidate the entire bridge construction.

The document should be updated with the corrections and additions noted above before being cited as a reference in future sessions. The additions (Debye-Waller, B1 lifecycle, Lifshitz classification) are substantive physics that affects the predictions, not editorial polish.

**Constraint map impact**: This review adds 3 corrections, 4 omissions, and 2 overclaim downgrades to the Landau Classification. None of these CLOSE or OPEN any mechanism. They refine the precision of the mapping without changing its scope. The document remains the authoritative framework-level synthesis.

---

## Appendix: Cross-Reference to My S44 Collab Review

| Issue in this review | Where I raised it in S44 collab | Status |
|:---|:---|:---|
| B1 lifecycle (transient NG mode) | Section 2 (W5-3), paragraph (c) | Raised, not reflected in Landau doc |
| u_2 from spectral geometry, not two-fluid | Section 2 (W6-2), pillar (1) | Raised, partially reflected |
| Van Hove 1D vs 2D exponent | Section 2 (W5-3), paragraph (d) | New in this review |
| Debye-Waller correction | Section 3.3, point 3 | Raised as S45 computation proposal |
| T3-T5 near-crossing classification | Section 3.1, fine tau scan | Raised as S45 computation proposal |
| Phonon focusing | Not raised in S44 | New in this review |
| Phonon drag and CDM | Section 4.4, CDM by construction | Partially raised, acoustic argument new |
| Two-fluid vs GGE language | Section 5.2, open question | Raised, not reflected in Landau doc |
