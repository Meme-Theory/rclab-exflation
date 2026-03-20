# Project Atlas Collaborative Review: Feynman-Theorist

**Reviewer**: Feynman-Theorist (path integrals, Feynman diagrams, renormalization, shut up and calculate)
**Date**: 2026-03-20
**Atlas version**: D00-D10, Sessions 1-51
**Reference corpus**: `researchers/Feynman/` (14 papers, 1948-1994)

---

## 1. The Feynman Test: What Does This Framework Actually Compute?

Let me apply my seven-step test (Paper 03, QED Feynman rules; Paper 13, Wilson RG) to the framework as it stands after 51 sessions.

**Step 1 -- Write the action.** The spectral action is S = Tr f(D_K^2 / Lambda^2), expanded via Seeley-DeWitt as S = 2f_4 Lambda^4 a_0 + 2f_2 Lambda^2 a_2(tau) + f_0 a_4(tau) + ... (equation E4). The BCS condensation energy E_cond = -0.137 M_KK comes from a separate functional: the BdG Hamiltonian on the Fock space built from D_K eigenstates. These are two different actions. The spectral action lives in the single-particle Hilbert space. The BCS energy lives in Fock space. There is no unified action S_total[tau, Delta] from which both derive as limits. This is the framework's deepest computational gap.

In QED, I write S = integral d^4x [-1/4 F^2 + psi-bar(iD-slash - m)psi] and everything -- propagators, vertices, loops, counterterms -- follows from that single functional (Paper 04, MF-6). Here, the framework has TWO functionals that do not talk to each other. The spectral action gradient is 6,596x larger than the BCS gradient at the fold (FRIED-39). They are not competing terms in one Lagrangian; they are different theories of the same degree of freedom.

**Step 2 -- Identify the propagators.** The Ornstein-Zernike propagator P_G(K) = T/(JK^2 + m_G^2) (equation E20) and the SA correlator chi_SA(K) (equation E22) are both computed. Good. The O-Z propagator has the right pole structure for a Goldstone mode with Leggett mass m_G = 0.070 M_KK. The SA correlator has a multi-pole structure with 110% spread -- it is NOT a propagator of any single particle. It is a spectral sum. This distinction matters when you try to mix them (equation E24).

**Step 3 -- Identify the vertices.** The Kosmann pairing matrix V_nm (equation E11) provides the BCS vertices. These are computed. Five selection rules (equation E15, Traps 1-5) constrain the vertex structure at machine epsilon. V(B2,B2) = 0.1557, irreducible by Schur's lemma. The vertex factor for phonon-phonon scattering on the fabric? Not computed. The three-phonon vertex (CF4) has been on the carry-forward list since S46. Without it, there is no perturbative expansion for the fabric dynamics.

**Step 4 -- Power count.** Is the spectral action renormalizable? Schwinger's proper-time method (Paper 11, SW-3) gives the 1-loop effective action as Gamma = i*hbar integral ds/s exp(-is m^2) Tr exp(is D^2). Van Suijlekom has shown this is 1-loop renormalizable for the NCG Standard Model. But the framework is not computing a 1-loop correction to the SM Lagrangian -- it is computing the spectral action on a compact 8-manifold. The power counting formula for gravity (Paper 07, QG-5: D = 2 + 2L) says quantum gravity is non-renormalizable at 2 loops. The KK reduction of gravity on SU(3) inherits this non-renormalizability. The spectral action as an effective field theory is valid below Lambda, with Lambda/M_KK = 10^6 to 10^15 (Wall W6). That is not renormalizability in the Dyson sense (Paper 12, finite number of counterterms to all orders); it is an effective theory with an unknown UV completion and a 6-to-15-order scale gap between the cutoff and the compactification scale.

There is a subtler issue. The Seeley-DeWitt expansion of the spectral action gives a_0 (cosmological constant), a_2 (Einstein-Hilbert + gauge kinetic), a_4 (Gauss-Bonnet + gauge self-coupling). The ratio a_4/a_2 = 1000:1 at the fold (equation E5 note, structural from 16-component spinor on 8-manifold). This means the higher-order heat kernel coefficients are not small corrections -- they dominate. Dyson's power counting (Paper 12, DY-2) assumes the expansion parameter is small (alpha/pi ~ 0.002 in QED). Here, the "expansion parameter" for the Seeley-DeWitt series is f_0*a_4 / (f_2*Lambda^2*a_2), and it is order 1000. The asymptotic expansion is not converging. The framework uses the exact trace (not the asymptotic expansion) for the monotonicity theorem, which is correct -- but it means the Seeley-DeWitt coefficients are not a reliable guide to the physics. The spectral action is computable exactly via eigenvalue sums; the heat kernel expansion is a tool for interpretation, not computation.

**Step 5 -- Compute something.** The framework has computed many things. The BCS condensation energy, the van Hove singularity, the Leggett mode frequency, the acoustic Hawking temperature. These are real computations. But what is the simplest nontrivial SCATTERING process? What is the tree-level amplitude for, say, two Bogoliubov quasiparticles scattering off each other in the 4D effective theory? This has never been computed. sigma/m = 5.7e-51 cm^2/g is quoted (equation E29), but this is a dimensional estimate, not a Feynman diagram calculation. I want to see the actual vertex, the actual propagator exchange, the actual phase space integral. Without that, the DM self-interaction cross-section is an order-of-magnitude guess dressed up as a prediction.

**Step 6 -- Check unitarity.** V matrix unitarity was verified to 2.2e-12 (Session 35, optical theorem). This is good. But this is unitarity of the internal BCS Hamiltonian, not of the 4D S-matrix. The 4D scattering matrix for KK excitations has never been checked for unitarity.

**Step 7 -- Compare to data.** sigma_8 = 0.799 (equation E33). That is the one number. One. After 51 sessions, 630 scripts, and 2,500+ files, the framework predicts ONE observable quantity that an experimentalist could measure. And it sits between two measurements that disagree with each other (Planck 0.811, lensing 0.766), so it cannot be falsified until the sigma_8 tension resolves. For comparison: QED after two Feynman diagrams (Paper 03) predicted the electron anomalous magnetic moment, the Lamb shift, and the running of alpha -- three independent measurements, all confirmed. A framework that produces one prediction straddling an unresolved discrepancy is not making a falsifiable claim; it is making a bet on the outcome of someone else's measurement.

---

## 2. The Path Integral Perspective: What IS Being Integrated Over?

The spectral action Tr f(D_K^2/Lambda^2) is, by Schwinger's proper-time representation (Paper 11, SW-2), identical to

S = integral_0^inf ds/s f-tilde(s) Tr exp(-s D_K^2)

where f-tilde is the inverse Laplace transform of f. This IS a path integral -- it is the partition function of a particle moving on SU(3) in imaginary time s, weighted by the cutoff f-tilde. The heat kernel Tr exp(-s D_K^2) counts the number of closed paths of proper length s on the manifold.

So the spectral action computes a single-particle partition function. It does NOT compute a quantum field theory partition function. The difference: a QFT path integral integrates over field configurations phi(x), giving Z = integral D[phi] exp(-S[phi]). The spectral action integrates over worldlines of a single particle. These coincide only in the 1-loop approximation (Schwinger, Paper 11, SW-3).

The BCS condensation is a many-body effect. It requires integrating over Fock space configurations. The spectral action, by construction, cannot see it -- this is precisely why the perturbative exhaustion theorem (equation E17, H1-H5) holds. The true free energy has a branch cut that the single-particle functional misses.

Wilson (Paper 13) would say: the spectral action is the wrong effective theory for the low-energy physics at the fold. The Wilsonian RG prescription is clear. Start from the microscopic theory (the spectral action at cutoff Lambda). Integrate out modes above the BCS gap scale Delta ~ 0.137 M_KK. Write the resulting effective Lagrangian L_eff[tau, Delta, theta_Goldstone] in terms of the relevant operators near the BCS fixed point. The BCS 1D theorem (equation E13, beta(g) = -g^2) tells you that the Cooper pairing is a relevant operator -- it flows to strong coupling for any g > 0. The spectral action monotonicity tells you that tau is an irrelevant operator in the Wilson sense: the spectral action drives tau away from the fold, and no BCS correction can compete (6,596x gradient ratio). The framework knows both of these facts but has not written the unified effective action that contains both.

This is not a minor bookkeeping gap. In QED, the 1-loop effective action (Schwinger, Paper 11, SW-3) and the tree-level Lagrangian are terms in the same functional integral. The 1-loop correction to the Coulomb potential is a well-defined Feynman diagram. Here, the "1-loop correction" from BCS to the spectral action is not a loop integral at all -- it is a Fock-space variational energy. The mathematical operation that connects them (trace over single-particle spectrum vs expectation value in a Slater determinant) has no diagrammatic representation within the spectral action formalism. Van Suijlekom's 1-loop renormalizability applies to the spectral action expanded around a fixed background -- not to the BCS ground state, which IS the background change.

The framework's computational structure is therefore:

1. Spectral action (single-particle, proven monotone) -- computes the STAGE
2. BCS Fock-space Hamiltonian (many-body, has structure) -- computes the PLAY
3. Ornstein-Zernike fabric propagator (mean-field, assumed) -- computes the AUDIENCE VIEW

These three layers are connected by shared input (D_K eigenvalues) but are not derived from a unified path integral Z = integral D[tau] D[Delta] D[theta] exp(-S[tau, Delta, theta]). Until they are, the framework is three theories sharing a dataset, not one theory with three limits.

---

## 3. The Retraction History: Computing or Curve-Fitting?

25 retractions in 51 sessions. That is roughly one retraction every two sessions. Is this a sign of honest self-correction or of a framework that keeps adjusting until something fits?

Here is my diagnosis. The retractions fall into three categories:

**Category A: Honest computational errors (Items 1, 7, 11, 12, 13, 20, 23).** Wrong matrix used, wrong vector space, numerical mistake. These are the kind of bugs that happen in any serious computation. Finding and correcting them is good science. The K-1e retraction chain (Items 8-10) -- where V(B2,B2) was computed three times in three different vector spaces -- is the most instructive. Lesson: know what space your operators live in before you multiply them. I approve. This is how physics works.

**Category B: Overclaiming structural identities (Items 2, 5, 14, 15, 16, 22, 24).** The Schwinger-instanton "duality" (Item 15) was a 2.4% numerical coincidence promoted to a structural identity. The GGE permanence claim (Item 16) assumed integrability that was not verified. The "4-5x coupling" (Item 2) confused a norm with a matrix element. The pattern: agents find a numerical near-match and immediately interpret it as deep structure, before checking whether the agreement is algebraic or accidental. This is not curve-fitting exactly, but it is the theoretical equivalent -- pattern-matching without computation. Feynman's rule (Paper 04): compute the next decimal place. If the agreement holds, it is real. If it breaks, it was coincidence.

**Category C: Wrong physical interpretations (Items 17, 18, 19, 21, 25).** The CDM free-streaming length used the wrong velocity (Item 17, 89 Mpc vs 3e-48 Mpc). The DM/DE ratio used the wrong susceptibility (Item 19). The DESI Bayes factor compared against a derived parameter instead of raw data (Item 25, converting a decisive negative into an apparent positive). These are the most concerning. They suggest that when the framework encounters data, the mapping between internal quantities and observables is so uncertain that wrong by 48 orders of magnitude (Item 17) or wrong in SIGN of the conclusion (Item 25) are possible.

**Verdict**: The framework is computing, not curve-fitting. The 25 retractions are concentrated in Categories A and B (computational errors and overclaiming), not in Category C (data manipulation). But the Category C retractions reveal that the weakest link is the mapping from internal geometry to observables -- which is exactly where the K_pivot question (EFOLD-MAPPING-52) sits. The thing the framework is worst at is the thing everything now depends on.

A note on the 58 closures. Each closure eliminates a proposed mechanism for tau-stabilization. 13 of these are attributed to Wall W4 (monotonicity) alone. Another 6 to Wall W1 (F/B ratio). The closures are genuine -- each one is backed by explicit computation. But they constrain the SAME question: how does the modulus stop rolling? The framework has 58 ways to NOT stabilize tau, 10 walls that obstruct stabilization, and 0 proven mechanisms that DO stabilize tau (assumption T5 is BROKEN). The 27 equilibrium closures across S17-S40 collectively prove that equilibrium tau-stabilization is impossible within the framework's computational reach (all 28 dimensions of the left-invariant metric space). This is a powerful structural result. It is also a powerful structural problem: the framework needs tau to reach and pass through the fold to produce BCS condensation, and it has no dynamical explanation for why this happens.

The transit paradigm (tau rolls through the fold without stopping) is the current answer. But transit without equilibrium means the fold crossing is a transient event. The BCS dwell time is 38,600x shorter than the BCS formation time (FRIED-39). The mechanism chain (Door 1) describes what CAN happen at the fold, not what DOES happen cosmologically. This gap between kinematic possibility and dynamical necessity has persisted since S35.

---

## 4. What Should an Experimentalist Look For?

The atlas says sigma_8 = 0.799 is the sole surviving observational prediction. Let me be precise about what that means.

The prediction chain is: D_K eigenvalues -> O-Z propagator with alpha_s = -0.069 -> power spectrum normalization at k = 0.05 Mpc^{-1} -> sigma_8 = 0.799. This prediction is RIGID within the Josephson sector (Wall W7, five proofs). But it uses alpha_s = -0.069, which is at 6 sigma from Planck. The SA-Goldstone mixing (Window 1) claims to fix this by putting alpha_s in [-0.040, 0] at K < K*, but then sigma_8 changes too.

So the prediction is conditional: IF the K_pivot mapping passes AND SA-Goldstone mixing dominates with beta > 0.9, THEN sigma_8 shifts from the rigid 0.799 to something in the mixing range. The rigid sigma_8 = 0.799 uses the alpha_s that is excluded. The mixing alpha_s is not excluded but gives a DIFFERENT sigma_8 that has not been computed. The "sole surviving prediction" is actually the prediction from the WRONG alpha_s regime.

What CMB-S4 should look for: alpha_s. The Planck constraint is alpha_s = -0.008 +/- 0.010. CMB-S4 target: sigma ~ 0.005. The framework's two regimes predict alpha_s = -0.069 (rigid, excluded) or alpha_s in [-0.040, 0] (mixing, testable). If CMB-S4 measures alpha_s = -0.008 +/- 0.005, then:
- Rigid regime: excluded at 12 sigma
- Mixing regime: excluded at 1.6 sigma (alpha_s = 0) to 6.4 sigma (alpha_s = -0.040)

The framework's alpha_s prediction in the mixing regime is alpha_s in [-0.040, 0]. If CMB-S4 finds alpha_s in [-0.013, -0.003] (1-sigma around Planck central), the mixing regime barely survives at the edge. If CMB-S4 finds alpha_s in [-0.003, 0.002], the mixing regime is comfortable ONLY at beta ~ 1 (pure SA correlator, no Goldstone). The physics of that limit -- SA correlator completely dominating the phase propagator -- has not been explored.

Beyond CMB-S4, there are two other observational channels:

**DESI DR3 (expected 2026-2027)**: The framework predicts w_a = 0 (triple-locked by monotonicity + effacement + frozen modulus). DESI DR2 gives w_a = -0.73 +/- 0.27. If DR3 tightens this and w_a remains negative at 3 sigma, the frozen-modulus assumption is excluded. If w_a drifts back toward zero, the framework is consistent but has not predicted anything -- LCDM also gives w_a = 0. The framework cannot claim credit for a null result.

**Fine-structure variation (ALPHA-ENV-43)**: delta_alpha/alpha ~ 10^{-6} between cosmic voids and filaments. This is the most distinctive prediction because it probes the FABRIC -- the spatially extended interconnected condensate. If the modulus has any spatial variation, the clock constraint (equation E27) predicts a specific relationship between alpha variation and local density. This has been queued since S43 and never executed. It requires spectroscopic surveys with void/filament classification. Among all the carry-forward items, this is the one most likely to produce a genuine falsification test, because it tests the fabric hypothesis directly rather than through the K_pivot bottleneck.

---

## 5. The One Calculation That Matters

After reading every atlas document, every wall, every door, every window, the entire framework reduces to a single computation: EFOLD-MAPPING-52.

This is the question: does the physical expansion history from tau = 0 to the present map the CMB pivot k = 0.05 Mpc^{-1} to K_fabric < 0.087 M_KK?

The computation requires: (a) the modulus equation of motion on M^4 x SU(3), derived from the 12D Einstein equations, not assumed; (b) initial conditions from quantum cosmology on the minisuperspace; (c) the stiff epoch (w = 1) duration; (d) backreaction from pair creation during transit; (e) the transition to radiation domination.

None of (a)-(e) have been rigorously computed. The preliminary estimate (S51) gives N_e = 3.3 from tau_i = 10^{-5}, with margin 0.2 e-folds. That margin is thin. And it uses w = 1 for the stiff epoch without backreaction.

The honest assessment: the framework has not yet computed the one number that determines whether it predicts anything about the CMB. 51 sessions of beautiful spectral geometry, and the observable predictions rest on a single unperformed calculation with uncertain inputs.

If I were computing EFOLD-MAPPING-52 myself, I would proceed as follows. The 12D Einstein equations on the product M^4 x SU(3)_tau with volume-preserving Jensen deformation reduce to a Friedmann equation coupled to a modulus equation:

H^2 = (8*pi*G/3) [1/2 G_mod tau_dot^2 + V_eff(tau)]
tau_ddot + 3H*tau_dot + (1/G_mod) dV_eff/dtau = 0

where G_mod = 5.0 (the DeWitt supermetric, computed in S40) and V_eff is the spectral action. The stiff epoch has w = tau_dot^2/(tau_dot^2) = 1 when kinetic energy dominates, giving a(t) ~ t^{1/3}. The number of e-folds from tau_i to the fold is N_e = integral H dt = integral (H/tau_dot) dtau. For the stiff epoch, H ~ tau_dot, so N_e ~ ln(tau_fold/tau_i). With tau_fold ~ 0.19 and tau_i = 10^{-5}, that gives N_e ~ ln(1.9e4) ~ 9.9. The S51 estimate of 3.3 is lower because it accounts for the decelerating phase; the raw logarithm is the upper bound.

The real question is whether backreaction from pair creation during transit (59.8 quasiparticle pairs, equation E18) provides additional e-folds or steals them. The backreaction is 3.7% (perturbative, S38), so it modifies N_e by at most ~0.3 e-folds. This is comparable to the margin (0.2). A proper calculation requires numerically integrating the coupled equations with the BCS pair-creation rate included as a source term. The computation is straightforward -- two coupled ODEs, initial conditions from minisuperspace cosmology, about 50 lines of Python. It has simply never been done.

---

## Closing: The Feynman Verdict

The framework has proven genuine mathematical theorems. The block-diagonal theorem, the structural monotonicity theorem, the five algebraic traps, the alpha_s identity, the Anderson-Higgs impossibility -- these are real results about Dirac operators on compact Lie groups. They belong in journals of mathematical physics regardless of whether the cosmological interpretation survives. The equation flow map (D03) shows a coherent logical structure from geometry through BCS to observables. The dependency diagram is clean.

But a clean logical structure is not a theory until it computes something an experimentalist can check. QED computes a_e = alpha/(2*pi) = 0.00116 from two Feynman diagrams (Paper 03, QED-5). The anomalous magnetic moment is measured to 12 decimal places. That is what a prediction looks like.

This framework, after 51 sessions, predicts sigma_8 = 0.799 from a chain that uses an excluded alpha_s, or predicts alpha_s in [-0.040, 0] from a mixing model whose validity depends on a scale mapping that has never been computed. The internal consistency is impressive. The mathematical structure is proven. The connection to observation is a conditional statement about a computation that does not yet exist.

What I respect about this project: it closed 58 mechanisms honestly. It retracted 25 claims when computation contradicted them. It did not lower the bar when results came back negative. The structural monotonicity theorem (Wall W4) is as clean a negative result as I have seen -- it permanently closes an entire category of mechanisms with a single proof. The five algebraic traps (equation E15) are elegant constraints derived from representation theory, not imposed by hand. The BCS 1D theorem (equation E13) is a genuine insight: the van Hove singularity makes the Cooper instability unconditional, a fact that any condensed matter physicist would recognize but that required explicit computation to establish in this spectral geometry context.

What I do not respect: the framework has been operating for 51 sessions without writing the unified action. The three computational layers (spectral action, BCS Hamiltonian, fabric propagator) share eigenvalues but not a Lagrangian. In QED, we wrote the action first and derived the Feynman rules from it (Paper 04). Here, the Feynman rules came first -- the selection rules, the propagators, the vertices -- and the action is still missing. This is backwards. It works for mapping the constraint surface but it cannot produce a genuine prediction until the layers are unified.

The framework is not wrong. It is not yet a theory. It is a program. The distance between program and theory is exactly one calculation: EFOLD-MAPPING-52.

If I had one session to spend, here is my priority list:

1. EFOLD-MAPPING-52: Integrate the coupled Friedmann-modulus equations numerically. 50 lines of Python. Pass/fail in one afternoon. If fail, stop. If pass, proceed to:
2. Compute sigma_8 in the MIXING regime (beta > 0.9, K < K*). The rigid sigma_8 = 0.799 uses the excluded alpha_s. The framework needs the mixing-regime sigma_8 before it can claim any prediction.
3. Write the unified action S[tau, Delta, theta]. Even approximately. Even at mean-field level. If the three layers cannot be written as one functional, the framework is not a theory; it is three calculations that happen to use the same eigenvalues.
4. Compute the tree-level Bogoliubov quasiparticle scattering amplitude. Draw the diagram, evaluate the integral, get a cross-section. Turn sigma/m from a dimensional estimate into a Feynman diagram result.

Compute it or shut up.

---

*Compiled from: atlas-00-index.md through atlas-09-retractions.md, researchers/Feynman/index.md (14 papers). Equations referenced by D03 labels (E1-E36). Walls by D05 labels (W1-W10). Windows and Doors by D05 labels. Retractions by D09 numbering (Items 1-25).*
