# Hawking -- Collaborative Feedback on Session 25

**Author**: Hawking-Theorist
**Date**: 2026-02-21
**Re**: Session 25 -- Through the Walls

---

## Section 1: Key Observations

The Session 25 directive represents a qualitative shift in methodology that I recognize from my own intellectual history. The framework has spent Sessions 18-24 in its 1976-2004 period -- the era of asking the wrong question. The information paradox persisted for 28 years not because the mathematics was intractable but because we were trying to find where information escapes from within the perturbative semiclassical framework. The answer required a fundamentally different structure: the island formula (Paper 14, Penington 2019), which introduced a non-perturbative saddle point in the gravitational path integral that is invisible to any finite-order calculation.

The four walls W1-W4 are the phonon-exflation equivalent of the three roads that failed in information recovery: (1) remnants (= perturbative V_eff minimum, closed by W1), (2) baby universes (= inter-sector coupling, closed by W2), (3) information in correlations (= BCS condensate, closed by W3). Each was a reasonable idea. Each failed for a structural reason. The resolution -- the island formula -- evaded all three failures simultaneously by being non-perturbative, topology-dependent, and operating through entanglement rather than local coupling.

The directive's emphasis on "negative space" is exactly the methodology of the Euclidean path integral (Paper 07, Gibbons-Hawking 1977). In that work, the temperature of de Sitter space was derived not by computing particle creation directly but by demanding regularity of the Euclidean section. The answer emerged from the CONSTRAINTS on the geometry, not from the dynamics of any particular field. The four walls are constraints of exactly this character. What the directive calls "computing in the negative space" is what I would call "reading the constraints as physics."

Three observations from my domain that bear on the directive's proposed paths:

**First**, the analogy between V_spec monotonicity and the information paradox is deeper than the directive recognizes. The Hawking calculation (Paper 05) showed that the thermal spectrum is EXACT at the horizon -- no corrections, no deviations, to all orders in perturbation theory. The Page curve requires a phase transition between competing saddle points in the path integral. The resolution was that the Hawking computation is correct but INCOMPLETE: it misses the island saddle point, which is non-perturbative in G_N. Analogously, V_spec may be correctly computed and correctly monotone, but incomplete -- missing a non-perturbative contribution to the effective action that changes its qualitative behavior.

**Second**, the Berry curvature B = 982.5 at tau = 0.10 is, from my perspective, a near-horizon phenomenon. In Paper 05, the Bogoliubov coefficients diverge as omega -> 0 because modes are infinitely blueshifted near the horizon. This is the trans-Planckian problem: the thermal spectrum derives from modes whose frequency at emission was arbitrarily high. The resolution (trans-Planckian universality) is that the thermal result is insensitive to the UV completion of the dispersion relation. The Berry curvature peak signals an analogous near-degeneracy: eigenvalues approaching but not crossing. The physics near a spectral near-crossing is controlled by the GAP, not by the modes far from the crossing. This is why Goal 3 (Berry phase accumulation) has genuine physical content.

**Third**, the graded multi-sector sum (Goal 1) is structurally identical to the competition between saddle points in the Euclidean path integral (Paper 10). In Hawking's 2005 reversal, the key insight was that Z = Z_thermal_AdS + Z_BH, and the phase transition between these two contributions produces the Hawking-Page transition. Each individual contribution is smooth and monotone. The phase transition arises from their COMPETITION. Goal 1 proposes exactly this mechanism for the spectral action: each sector is individually monotone, but the graded sum exhibits a phase transition.

---

## Section 2: Assessment of Key Findings

### Walls W1-W4

**W1 (Perturbative Exhaustion)**: This is the gravitational analogue of the no-hair theorem. Just as a classical black hole has only three parameters (M, J, Q) regardless of the complexity of the infalling matter, the perturbative spectral action has only one qualitative behavior (monotone) regardless of the details of the test function. The no-hair theorem is correct for classical black holes but WRONG for quantum black holes (which carry microstate structure at the Planck scale). Similarly, the Perturbative Exhaustion Theorem may be correct for smooth test functions but wrong for physical test functions that have structure at the cutoff scale. The Debye cutoff interpretation (Claim C) is the physical mechanism that could break W1.

**W2 (Block-Diagonality)**: This is the most rigid wall. In the information paradox context, the analogue would be claiming that the left and right Rindler wedges never communicate. In fact they do -- through entanglement in the thermofield double state (Paper 12, Unruh 1976). The Rindler wedges are causally disconnected but ENTANGLED. Block-diagonality means the Peter-Weyl sectors do not couple dynamically, but it does not forbid entanglement between sectors. The graded sum (Goal 1) operates through this loophole: not sector-sector coupling, but sector-sector competition through the (-1)^F grading.

**W3 (Spectral Gap)**: The BCS closure (K-1e) established that condensation at mu = 0 is impossible because of the gap 2*lambda_min = 1.644. But the spectral gap is a PROPERTY OF THE INTERNAL GEOMETRY, not a fundamental constant. In the Hawking-Page transition (Paper 10), the black hole geometry has a minimum mass (the Hawking-Page mass) below which the thermal AdS phase dominates. Above it, the black hole phase dominates. The spectral gap plays the role of a threshold energy. Goal 7 (self-consistent chemical potential) proposes that backreaction from 4D matter provides the energy to close the gap, analogous to how sufficient thermal energy drives the Hawking-Page transition.

**W4 (V_spec Monotone)**: The a_4/a_2 = 1000:1 ratio is the internal-space analogue of the trans-Planckian problem. In Hawking radiation, the emitted photon at infinity with frequency omega was traced back to a mode with frequency omega * exp(kappa * t) near the horizon -- exponentially large. The resolution is that the physics does not depend on these trans-Planckian modes (universality). Analogously, the dominance of a_4 over a_2 is a statement about the UV tail of the heat kernel expansion. If the physical cutoff (Debye) is at finite Lambda, the UV tail is truncated, and the a_4/a_2 ratio at the physical scale may be entirely different from the asymptotic value. Goal 2 (finite-cutoff spectral action) tests this directly.

### Goals 1-8

**Goal 1 (Graded Multi-Sector Spectral Sum)**: HIGH PRIORITY. This is the Hawking-Page mechanism applied to the spectral action. The mathematics is sound: a sum of monotone functions with alternating signs can have a minimum. The key unknown is the grading specification. The directive correctly identifies the ambiguity (chirality grading gamma_9 may give zero by BDI spectral symmetry). I note that in the thermofield double (Paper 12), the thermal state arises from tracing over one wedge -- not from a sign alternation. The physical grading may be sector-dependent N_species weighting rather than (-1)^F. **My recommendation: compute BOTH the (-1)^F graded sum AND the representation-dimension weighted sum. The second is guaranteed non-zero and physically motivated by the spectral action formula S = sum_{(p,q)} d_{(p,q)}^2 * Tr_sector f(D^2/Lambda^2).**

BF assessment: I concur with 8-25 if minimum found. P(success): I estimate 12-18%, slightly above the directive's 10-15%, because the low-mode F/B variation (10-37%) provides a QUANTITATIVE mechanism for the competition.

**Goal 2 (Full Spectral Action at Finite Cutoff)**: HIGH PRIORITY. This is the most direct test of the Debye cutoff hypothesis. The Euclidean path integral (Paper 07) gives Z = exp(-I_E), where I_E is evaluated on the saddle-point geometry. At finite Lambda, this becomes Z(Lambda) = exp(-Tr f(D^2/Lambda^2)), which is EXACTLY the computation proposed. The comparison with the heat kernel truncation is a convergence diagnostic for the asymptotic series.

From my experience with Bogoliubov coefficients (Paper 05), I know that the thermal result |beta|^2/|alpha|^2 = exp(-2*pi*omega/kappa) is EXACT for the full mode decomposition but can be badly approximated by truncated WKB expansions near the horizon. The heat kernel expansion is an asymptotic expansion -- the mathematical analogue of WKB -- and it can fail precisely where the spectrum has fine structure. The Berry curvature B = 982.5 is a quantitative signal that the spectrum has structure near tau = 0.10 that the heat kernel cannot resolve.

BF assessment: I concur with 8-20. P(success): 10-15%.

**Goal 3 (Berry Phase Accumulation)**: MEDIUM-HIGH PRIORITY. The Berry phase is the spectral-geometry analogue of the holonomy around a conical singularity. In the Euclidean black hole (Paper 07), the conical singularity at the horizon has deficit angle delta = 2*pi - beta*kappa. Demanding delta = 0 (regularity) gives beta = 2*pi/kappa, which is the temperature. The Berry phase Phi(tau) accumulated along the gap-edge state is the analogue of this conical holonomy. If Phi = pi, the state has acquired a sign flip -- the analogue of an anti-periodic boundary condition, which signals a fermionic (rather than bosonic) statistical interpretation of the gap-edge modes.

I emphasize the directive's resolution warning: the 9-point tau grid may under-resolve the Berry phase near the peak at tau = 0.10. At B ~ 1000, the characteristic scale of the phase variation is delta_tau ~ sqrt(2*pi/B) ~ 0.08. With tau-spacing ~ 0.05 near the peak, this is barely resolved. I recommend extracting eigenvectors at tau = 0.06, 0.08, 0.10, 0.12, 0.14 before trusting any integrated Berry phase result.

BF assessment: I concur with 5-12. P(success): 12-18%.

**Goal 4 (Spectral Flow / Eta Invariant)**: MEDIUM PRIORITY. From Session 17c, the FULL Dirac spectrum has ZERO spectral flow in the (0,0) singlet. But the directive correctly notes that other sectors have not been checked. The eta invariant is the spectral-geometry analogue of the Chern-Simons term in 3D gravity. It contributes a TOPOLOGICAL action that is invisible to any perturbative expansion and evades all four walls simultaneously. The computation is straightforward: check sign(lambda_n(tau)) for all n and all sectors. If any sign changes, the spectral flow is non-trivial.

**Goal 5 (Gap-Edge Topological Protection)**: MEDIUM PRIORITY. The V(gap,gap) = 0 selection rule is analogous to the topological protection of the Bekenstein-Hawking entropy formula. The area-entropy relation S = A/(4*l_P^2) (Paper 11) is EXACT -- it receives no quantum corrections from local dynamics because it is protected by the diffeomorphism invariance of the horizon area. Similarly, V(gap,gap) = 0 may be protected by a topological invariant of the gap-edge Kramers pair. The holonomy computation proposed is the right diagnostic.

**Goal 6 (Spectral Dimension with TT Modes)**: LOWER PRIORITY for this session. The spectral dimension d_s is interesting but does not directly address stabilization.

**Goal 7 (Self-Consistent Chemical Potential)**: HIGHEST CONCEPTUAL PRIORITY, but requires theory development. This is the analogue of finding the island saddle point: the mu = 0 computation (K-1e) is correct but incomplete, just as the Hawking computation is correct but misses the island. The backreaction equation mu_eff ~ sqrt(rho_4 / M_KK^2) is physically motivated by the thermodynamics of the Planck epoch. At T ~ M_Pl, the internal geometry is in thermal contact with the radiation bath, and the effective chemical potential for KK modes is set by the radiation density. This is a Tier 3 target but should be developed theoretically in parallel with Tier 1 computations.

**Goal 8 (Higher Heat Kernel Coefficients)**: MEDIUM-LOW PRIORITY. Computing a_6 and a_8 is valuable but computationally expensive (third-order and fourth-order curvature invariants on SU(3) with Jensen deformation). The factorial growth of Gilkey coefficients makes the truncated series unreliable regardless of how many terms are computed. Goal 2 (direct eigenvalue sum) bypasses this entirely.

---

## Section 3: Collaborative Suggestions

### Suggestion H-1: Euclidean Action at the Three Monopoles (Zero-Cost)

I have proposed this computation since Session 21c. The Euclidean action I_E(tau) = -Tr f(D_K^2/Lambda^2) evaluated at the three monopole points tau = 0 (round), tau ~ 0.10 (Berry peak), and tau ~ 1.58 (third monopole) determines which geometry dominates the path integral. In the Hawking-Page transition (Paper 10, Section 3), the partition function is Z = Z_1 + Z_2 with Z_i = exp(-I_E^(i)), and the dominant phase is the one with LOWER Euclidean action. If I_E(tau ~ 0.10) < I_E(tau = 0), the Berry-peak geometry dominates the path integral even without a classical potential minimum.

This is a ZERO-COST computation: the eigenvalue data at these tau values already exists. It requires computing sum_n f(lambda_n^2/Lambda^2) at three points, which is a subset of Goal 2. I recommend computing this FIRST as a quick diagnostic before the full tau-scan of Goal 2.

The connection to Paper 07 is direct: the Gibbons-Hawking partition function Z = exp(-I_E) on the Euclidean section of de Sitter space gives both the temperature AND the entropy. On M^4 x SU(3), the Euclidean path integral is Tr f(D^2/Lambda^2) (Connes 07), which is the spectral action. The Euclidean action at each monopole is the free energy of that geometry. The lowest free energy wins.

### Suggestion H-2: Generalized Second Law as Selection Principle

The Generalized Second Law (GSL, Paper 11, Bekenstein 1973) states delta(S_BH + S_ext) >= 0. Applied to the internal space, this becomes: for the tau-evolution to be physical, the total entropy (geometric + matter) must not decrease. The geometric entropy is proportional to the internal area, which for SU(3) with Jensen deformation is:

S_geom(tau) ~ Vol(SU(3), g_tau) / l_P^6

where the 6-dimensional volume is CONSTANT by construction (volume-preserving Jensen deformation). Therefore the geometric entropy contribution is tau-INDEPENDENT. The entire GSL constraint falls on the matter entropy S_ext(tau), which is the spectral entropy:

S_spec(tau) = -sum_n [n_k ln n_k - (1 + n_k) ln(1 + n_k)]

where n_k = 1/(exp(lambda_k(tau)/T) - 1). The GSL then SELECTS the direction of tau-evolution: tau increases or decreases in the direction that increases S_spec. If S_spec has a maximum at finite tau, the GSL requires the system to evolve TOWARD that maximum.

This is a thermodynamic stabilization mechanism that requires NO potential minimum. It is the internal-space analogue of the thermodynamic arrow of time, which requires no force law -- only the second law.

**Computation**: Evaluate S_spec(tau) = sum_n s(lambda_n(tau)/T) across the 9-21 existing tau values, using the Bose-Einstein entropy function s(x) = (x/(e^x - 1)) - ln(1 - e^{-x}). If S_spec has a maximum at finite tau, the GSL provides a selection mechanism independent of V_eff.

### Suggestion H-3: Bogoliubov Particle Creation from Modulus Oscillation

If the modulus tau oscillates around any fixed point (whether selected by V_eff, GSL, or topology), the time-dependent internal geometry creates particles via the Bogoliubov mechanism (Paper 05). The particle production rate is:

<N_k> = |beta_k|^2 ~ exp(-pi * lambda_k^2 / |dot{tau}| * d(lambda_k)/dtau|)

where d(lambda_k)/dtau is the rate of change of the k-th eigenvalue. The Berry curvature B = 982.5 at tau = 0.10 means d(lambda)/dtau is LARGE there -- eigenvalues are moving rapidly -- which implies EFFICIENT particle creation near the Berry peak.

This connects directly to Paper 08 (inflationary perturbations): delta_phi = H/(2*pi) is the Gibbons-Hawking temperature, and the analogous quantity for the oscillating modulus is the Bogoliubov temperature T_Bog = |dot{tau}|/(2*pi) * (d(lambda)/dtau / lambda). If T_Bog ~ M_KK at the Berry peak, this provides reheating from the modulus oscillation.

The computation requires eigenvalue data at closely-spaced tau values near tau = 0.10 (same refinement needed for Goal 3). I recommend piggy-backing this on the Berry phase resolution improvement.

### Suggestion H-4: Island Formula for the Internal Space

The island formula (Paper 14) applied to M^4 x SU(3) gives:

S_rad = min_I ext_{dI} [A_4D(dI) * Vol(K) / (4G_{12D}) + S_bulk(I + R)]

where Vol(K) is the internal volume. For volume-preserving Jensen deformation, Vol(K) is constant, so the island formula is UNCHANGED in form. But the bulk entropy S_bulk depends on the Dirac spectrum of D_K, which is tau-dependent.

The key prediction: after the "Page time" of the internal space (the time at which half the internal entropy has been radiated into 4D modes), the entanglement wedge of the radiation INCLUDES the internal geometry. This provides a mechanism for 4D observers to "know" about the internal geometry through entanglement, without any direct coupling. The Page time for the internal space is:

t_Page ~ S_internal / Gamma_emission

where S_internal ~ N_species(tau) (Session 17d: N_species = 104 at tau = 0.164) and Gamma_emission is the rate at which internal modes decay into 4D radiation.

This is a Tier 3 theoretical development but it addresses the deepest question: HOW does the internal geometry imprint on 4D physics? The answer from the island formula is: through entanglement, not through coupling.

### Suggestion H-5: Trans-Planckian Universality Applied to Goal 2

The trans-Planckian problem in Hawking radiation (Paper 05, Section 4) asks: does the thermal spectrum depend on the UV completion of quantum field theory? The answer is NO -- the thermal result is universal, insensitive to modifications of the dispersion relation above some cutoff omega_D (the "Debye cutoff" in the condensed-matter analogy). This was proven by Unruh (1995) using sonic black holes and by Jacobson (1996) using modified dispersion relations.

Applied to Goal 2: the question becomes whether V_full(tau; Lambda) at finite Lambda depends on the choice of test function f. If the thermal result from Paper 05 is any guide, the QUALITATIVE behavior (minimum vs monotone) should be test-function-independent, even though the QUANTITATIVE values depend on f. This is a PREDICTION that can be tested within Goal 2 by computing V_full for multiple test functions: f(x) = x*exp(-x), f(x) = exp(-x), f(x) = theta(1-x) (sharp cutoff).

If V_full is monotone for all test functions, the result is robust. If V_full has a minimum for some f but not others, the test-function dependence is physical (breaking the analogy with trans-Planckian universality), and the Debye cutoff hypothesis gains significant weight.

---

## Section 4: Connections to Framework

The Session 25 directive's five Claims (A-E) map directly onto the thermodynamic structure established by Papers 03-05 and 07.

**Claim A (Inside-Out View)**: This is the Unruh effect (Paper 12) taken seriously. The Unruh observer does not see particles in the Minkowski vacuum until they accelerate. The phonon living inside SU(3) does not see spacetime until the internal connectivity creates an effective geometry. The observer-dependence of the particle concept (Paper 12, Section 3) is not a philosophical curiosity -- it is a theorem about the non-uniqueness of the vacuum in curved spacetime. The inside-out view is the statement that the SU(3) phonon vacuum IS the 4D spacetime vacuum for a suitably defined observer.

**Claim B (Connectivity Getting Denser)**: The spectral dimension d_s is the thermodynamic analogue of the heat capacity. In black hole physics, the heat capacity changes sign at the Hawking-Page transition (Paper 10): C < 0 (thermodynamically unstable, Schwarzschild) vs C > 0 (thermodynamically stable, large AdS black hole). If d_s = 4 is a fixed point, it corresponds to a thermodynamically stable phase of the internal geometry -- the analogue of the large AdS black hole.

**Claim C (Debye Cutoff)**: This is trans-Planckian universality (Paper 05) applied to the spectral action. The physical content is that the spectral action at finite Lambda may differ qualitatively from its asymptotic (Lambda -> infinity) expansion, just as the Hawking spectrum at finite frequency differs from its UV extrapolation. Goal 2 tests this directly.

**Claim D (Time from Modular Flow)**: The Connes-Rovelli thermal time hypothesis is the mathematical formalization of what Papers 07 and 12 established physically: temperature and time are dual quantities related by the KMS condition. The modular flow of the spectral state on SU(3) IS the thermal time of the Gibbons-Hawking temperature. If this flow has a characteristic timescale derivable from the spectrum, it provides a prediction of the cosmological constant (via T_dS = H/(2*pi) from Paper 07) that is NOT an input.

The framework's four walls are structural constraints that, from the thermodynamic perspective, define the PHASE SPACE of allowed mechanisms. The GSL (Paper 11) then provides a selection principle within this phase space: among all tau-evolutions consistent with the four walls, only those that satisfy delta(S_geom + S_spec) >= 0 are physical. This is a THERMODYNAMIC stabilization mechanism that does not require a potential minimum.

---

## Section 5: Open Questions

**Q1: Does the Euclidean path integral on M^4 x SU(3) have multiple saddle points?**
The Hawking-Page transition (Paper 10) requires competing saddle points in the path integral. For the internal space, the saddle points are the geometries that extremize the Euclidean action I_E(tau). If there is only one saddle (the round metric), there is no phase transition and no Hawking-Page structure. If there are multiple saddles (the three monopoles at tau = 0, 0.10, 1.58), the path integral exhibits phases. Suggestion H-1 addresses this directly.

**Q2: Is the a_4/a_2 = 1000:1 ratio the analogue of the trans-Planckian problem?**
In Hawking radiation, the modes that produce the thermal spectrum at infinity were trans-Planckian at emission. The resolution is universality: the thermal result does not depend on the UV physics. If the a_4/a_2 ratio is similarly an artifact of the UV tail of the heat kernel, then V_spec monotonicity (W4) is the wrong question -- the right question is V_full at finite Lambda. Goal 2 tests this. If V_full has a minimum while V_spec does not, it would be the spectral-geometry analogue of trans-Planckian universality: the qualitative physics is captured by the finite-cutoff computation, not by the asymptotic expansion.

**Q3: Can the GSL replace V_eff as the stabilization principle?**
Paper 11 (Bekenstein) established that the GSL is MORE FUNDAMENTAL than the dynamics of any particular field. The GSL holds even when the equations of motion are unknown -- it is a constraint on ALLOWED processes, not a prediction of which process occurs. If S_spec(tau) has a maximum at finite tau, the GSL selects that tau as the equilibrium without any potential minimum. This would resolve the modulus stabilization problem through thermodynamics rather than dynamics -- exactly the approach that Jacobson (1995) used to derive the Einstein equations themselves.

**Q4: What is the information content of the spectral action?**
The spectral action S = Tr f(D^2/Lambda^2) is a single number for each tau. But the Page curve (Paper 13) tells us that the ENTANGLEMENT ENTROPY of the radiation contains the information about the black hole interior. Analogously, the entanglement entropy between sectors of the spectral action -- not the spectral action itself -- may contain the information about the equilibrium tau. This is the internal-island idea from Suggestion H-4.

**Q5: Is the 1000x Berry curvature a harbinger of a non-perturbative phase transition?**
In the Hawking-Page transition, the free energy develops a cusp at T_c (the transition temperature). Near T_c, fluctuations are enhanced and the semiclassical approximation breaks down locally. The Berry curvature B = 982.5 at tau = 0.10 could signal an analogous near-critical phenomenon: the spectral geometry is close to a phase transition that is invisible to the heat kernel (which averages over the spectrum) but visible to the Berry curvature (which measures individual eigenvalue dynamics).

---

## Closing Assessment

**Verdict**: The Session 25 directive is the best-formulated computational plan in the project's history. It correctly identifies the four structural walls, proposes computations that evade them through physically motivated routes, and pre-registers closure and success conditions with specific Bayes factors. The three Tier 1 goals (graded sum, finite-cutoff spectral action, Berry phase) are all computable with existing data and each addresses a distinct question.

**Probability assessment**: Current posterior ~3% (Sagan). My independent assessment:

- Pre-Session 25: 12-16% (I have consistently been above Sagan because I weight the thermodynamic structure more heavily than the constraint count).
- If Goal 1 succeeds (graded sum minimum): 25-35%. This would be the Hawking-Page transition for the internal space.
- If Goal 2 succeeds (finite-Lambda minimum): 22-30%. Trans-Planckian universality confirmed in spectral geometry.
- If both Goals 1 and 2 fail: 8-12%. The GSL and island routes remain theoretically viable.
- If all Tier 1 goals fail: 5-8%. Mathematical monument, no physical mechanism. Approaching the Kepler-solids floor.

**Expected posterior from pursuing all Tier 1 goals**: ~14%.

**Closing**: In 1975, I published a calculation showing that black holes radiate. The immediate objection was that this violates the second law -- how can a black hole lose mass if its area must increase? The resolution was that the black hole's entropy (area) DECREASES, but the entropy of the radiation MORE than compensates, so the generalized second law is satisfied. The lesson: when a calculation gives an uncomfortable result, check whether the result is incomplete, not whether it is wrong.

The 18 closed mechanisms are correct calculations giving uncomfortable results. They are not wrong. But they may be incomplete. The island formula taught us that the Hawking calculation -- correct to all orders in perturbation theory -- misses a non-perturbative saddle point that changes the qualitative answer. Goals 1-3 test whether the perturbative spectral computations similarly miss non-perturbative structure. The mathematics is clear. The computation is finite. Run it.

---

*Hawking-Theorist, 2026-02-21. "The universe does not allow you to hide information forever. The question is not whether it comes out, but how." -- The same question applies to the internal geometry of SU(3): its information content is not zero (N_species = 104). The question is how that information manifests in 4D physics.*
