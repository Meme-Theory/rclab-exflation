# S58 Plan Review: Cosmological Perspective

**Reviewer**: Katie Mack (Cosmic Bridge)
**Date**: 2026-03-23
**Source**: session-58-plan.md, Phononic-to-Cosmos assessment (sessions/framework/Phononic-to-Cosmos.md)

---

## 1. Plan Overview

Session 58 proposes 23 computations across 4 waves, all organized around the central bottleneck identified unanimously by S57's five reviewers: the Josephson-to-Lambda partition. The plan's thesis is that the S57 Bayesian emulator returned NROY = 0% because it placed the Josephson condensation energy (F_Josephson = -336.6 M_KK, 95.9% of the fabric budget) in the matter sector rather than the vacuum sector. Rebuilding the emulator under the Volovik partition -- where F_Josephson is vacuum energy and only the quasiparticle excitations (E_BCS + E_BA + E_Leggett = 11.4 M_KK) constitute matter -- is the single most important computation (W0-1, 5/5 unanimous).

The secondary thrust is attacking the integrability lock that keeps the CC 114 orders of magnitude above observation. Two specific computations target this: exact diagonalization at N_pair = 2 to test whether pair-pair interactions break Richardson-Gaudin integrability (W1-1), and the 8x8 Hessian in Richardson-Gaudin integral space to determine whether the GGE sits at a saddle or a minimum (W1-2). If the GGE is at a saddle, a "Penrose process" -- canonical transformations that reduce vacuum energy without breaking integrability -- becomes algebraically possible.

The remaining computations (Waves 2-3) test the robustness of the DM prediction against graph topology (W2-1, gap scaling on CG(24)), off-Jensen deformations (W2-2, W3-9, W3-12), and various integrability-breaking candidates (Pomeranchuk instability W2-3, multi-mode resonance W2-4, anharmonic Leggett coupling W1-3). Wave 3 is a catch-all of 13 computations from all five S57 collaboration reviews plus the Volovik-SP workshop. Nothing is deferred to S59, which is good discipline.

From a cosmological perspective, this session is almost entirely internally focused. It is asking: "Does the microscopic physics produce the right energy partition?" rather than "What do cosmological observables look like?" This is understandable -- the partition question is genuinely the bottleneck -- but it means S58 risks another session of beautiful condensed-matter physics with minimal cosmological contact. I will flag where cosmological tests should be inserted.

---

## 2. Gate-by-Gate Evaluation

### W0-1: VOLOVIK-PARTITION-58

- **What it tests**: Whether rebuilding the Bayesian emulator with F_Josephson as vacuum (not matter) produces NROY > 5%.
- **Cosmological relevance**: HIGH. This directly determines whether the framework's DM abundance prediction survives confrontation with Planck Omega_DM h^2 = 0.1186 +/- 0.0020 (Paper 29). The Volovik partition changes f_DM from ~0.012 (E_DM/E_total) to ~0.312 (E_DM/E_matter), which is the difference between catastrophic failure and 18% agreement.
- **Effectiveness assessment**: STRONG. The emulator with the correct partition will produce a genuine confrontation between framework predictions and four observables (Omega_DM h^2, Omega_Lambda, f_DM, w). The sensitivity analysis (which parameter dominates NROY) will identify the next computation target. The variant B (ZPE-inclusive f_DM = 0.440) is important -- it brackets the interpretation ambiguity.
- **Recommendation**: **KEEP** -- this is correctly identified as the top priority.
- **Notes**: The w observable in the emulator needs careful treatment. The pre-Shattering values (w_0 in [-0.430, -0.589]) were computed from the GGE equation of state under a static picture. The Shattering paradigm (S57) changed the physical picture fundamentally -- the transit is a sudden quench, not an adiabatic evolution. The emulator should document which w values it uses and whether they have been recalculated post-Shattering. See Section 4 below.

### W0-2: CC-CANCELLATION-SWEEP-58

- **What it tests**: Whether the near-cancellation (+0.316 - 0.315 = +0.00145 M_KK) is structural across 50 tau values or accidental at the fold.
- **Cosmological relevance**: MEDIUM-HIGH. If R_cancel stays in [0.001, 0.01] at all tau, this is evidence that the Volovik equilibrium theorem operates as a structural constraint, which would make the CC problem "merely" a matter of achieving the final 111 OOM of cancellation rather than 114. More importantly, the tau-dependence of Lambda_eff is directly related to w(z) -- if Lambda_eff evolves during transit, the dark energy equation of state evolves too.
- **Effectiveness assessment**: GOOD for structural characterization, but the gate is INFO only. The real discriminant is whether the cancellation can be extended beyond 3 sectors (see Observational Gauntlet Test 2 in my Phononic-to-Cosmos assessment, the "cancellation scaling with KK level" computation).
- **Recommendation**: **KEEP**, but **STRENGTHEN** by adding a derivative: compute dLambda_eff/dtau at each point. If this quantity maps to a late-time w_a through the BLV metric, the computation gains direct DESI relevance.
- **Notes**: The pre-registered criterion (R_cancel in [0.001, 0.01]) is reasonable. The one-order-of-magnitude variation test is a meaningful threshold for "structural."

### W0-3: EPSILON-DIRECT-58

- **What it tests**: Whether the dipolar coupling epsilon can be refined from 50% to ~5% uncertainty by direct projection onto the V_bare matrix.
- **Cosmological relevance**: MEDIUM. Epsilon controls the Leggett gap, which controls the DM energy fraction. Reducing sigma(epsilon) from 50% to 5% would tighten the Omega_DM h^2 bracket from [0.017, 0.188] to roughly [0.10, 0.15] -- which would either confirm or exclude agreement with 0.120. This is the difference between "consistent with" and "predicts."
- **Effectiveness assessment**: GOOD. A direct extraction from the pairing matrix eliminates the dominant uncertainty source in the DM prediction.
- **Recommendation**: **KEEP**.
- **Notes**: The gate bounds [0.0005, 0.010] for FAIL seem generous. If epsilon_direct turns out to be 0.001 (factor 2.5 below S49), the Leggett gap drops by factor sqrt(2.5) and the DM energy fraction drops correspondingly. The downstream consequences should be mapped explicitly.

### W1-1: NPAIR2-INTEG-58

- **What it tests**: Whether Richardson-Gaudin integrability survives at N_pair = 2 on a 2-cell system.
- **Cosmological relevance**: HIGH (indirect). If integrability breaks at N_pair = 2, the CC solution path opens. The CC magnitude (10^114 above observation) is the framework's most severe cosmological problem. Any mechanism that can reduce it is of the highest importance.
- **Effectiveness assessment**: STRONG. This is a clean binary test. The level spacing ratio <r> has well-calibrated thresholds: Poisson (0.386), GOE (0.531). The 0.40/0.45 boundaries in the gate are conservative and appropriate. The 560-state Fock space is tractable.
- **Recommendation**: **KEEP** -- correctly identified as the next decisive frontier.
- **Notes**: Even if integrability breaks (<r> > 0.45), the thermalization timescale matters. A thermalization time of 10^{100} Planck times would still not solve the CC problem within the age of the universe. The computation should report the thermalization rate, not just the level statistics. This is acknowledged in the plan's decision point but not in the gate itself.

### W1-2: RG-HESSIAN-58

- **What it tests**: Whether the GGE sits at a saddle in Richardson-Gaudin integral space, allowing CC reduction through canonical transformations.
- **Cosmological relevance**: HIGH (indirect). Same logic as W1-1 -- any CC reduction mechanism has cosmological significance.
- **Effectiveness assessment**: MODERATE. The "Penrose process" analogy is physically motivated (the Kerr ergosphere allows energy extraction via phase space geometry, not thermalization), but the 8x8 Hessian at N_pair = 1 is very small. At N_pair = 1, the Richardson-Gaudin integrals are just the occupation numbers, so the Hessian of Omega reduces to something close to the curvature of the free energy in the occupation number space. The question is whether this is really testing anything new beyond what S57 W0-3 already established (the GGE has an O(1) departure from equilibrium in occupation space).
- **Recommendation**: **KEEP** but manage expectations. The Hessian eigenvalues should be interpreted carefully: a negative eigenvalue in I^8 means the GGE is a saddle of the thermodynamic potential, but it does NOT mean the system can access the lower-energy state -- integrability constrains the allowed trajectories in phase space to surfaces of constant I_k. The "Penrose process" would require a mechanism to convert between different integrals of motion.
- **Notes**: The computation should check whether the negative eigenvalue direction (if it exists) is accessible given the integrability constraints. If the direction requires changing an I_k that is exactly conserved, the saddle is irrelevant.

### W1-3: ANHARMONIC-LEGGETT-58

- **What it tests**: Whether cubic and quartic coupling between Leggett modes redistributes energy during transit.
- **Cosmological relevance**: LOW-MEDIUM. This affects the DM energy fraction by potentially a factor of 2 (QA estimate), which matters for the Omega_DM prediction, but the QA pre-estimate already suggests Gamma_scat * dt_transit ~ 10^{-6} (harmonic approximation safe). The computation is expected to confirm the independent-mode result.
- **Effectiveness assessment**: MODERATE. The pre-estimate makes this likely to be a confirmation rather than a surprise. But the pre-estimate used an order-of-magnitude argument; the full vertex computation is worth doing.
- **Recommendation**: **KEEP** but at lower priority than W1-1/W1-2.

### W2-1: GAP-CG-58

- **What it tests**: Whether the gap scaling exponent alpha = -1.84 survives on the physical Cayley graph CG(24) versus the linear chain.
- **Cosmological relevance**: MEDIUM. The gap scaling determines how the DM prediction extrapolates from 2-cell to 32-cell. If alpha on CG(24) is more negative (faster gap collapse), the 32-cell fabric is even more excitable than the chain estimate. If alpha > 0, the DM prediction collapses entirely.
- **Effectiveness assessment**: GOOD. The CG graph has higher connectivity (degree 2-4) than the chain (degree 2), so the Fiedler eigenvalue (1.016 vs ~2/N for the chain) should produce faster gap collapse. The spectral dimension measurement (step 6 in the method) adds structural information about the fabric topology.
- **Recommendation**: **KEEP**.
- **Notes**: The Feynman cross-check (analytical derivation) is valuable. An analytical formula for alpha in terms of the graph spectral dimension would make the prediction independent of the specific graph.

### W2-2: OFF-JENSEN-TRANSIT-58

- **What it tests**: Whether the physical trajectory deviates from the Jensen manifold (sigma = 0) during transit.
- **Cosmological relevance**: LOW-MEDIUM. If sigma grows, the entire energy partition changes. But the pre-registered constraint (Workshop V4/V8: growth factor 1.000039) already shows sigma is frozen. This computation will almost certainly confirm the kinematic suppression.
- **Effectiveness assessment**: MODERATE. The result is predictable from the pre-estimate (transit too fast for sigma to grow), so the computation is a validation rather than a discovery.
- **Recommendation**: **KEEP** but at lower priority.

### W2-3: POMERANCHUK-GGE-58

- **What it tests**: Whether the GGE is Pomeranchuk-stable (Landau parameters satisfy stability bounds).
- **Cosmological relevance**: MEDIUM (indirect). Another integrability-breaking candidate for the CC.
- **Effectiveness assessment**: MODERATE. The plan acknowledges the conceptual issue: the 0D discrete 8-mode system may not admit a Landau parameter decomposition. Mapping 8 modes onto angular channels using representation theory is creative but introduces interpretation ambiguity. The result will be meaningful only if the Landau framework is applicable -- and for a system with 8 discrete modes and N_pair = 1, this is questionable.
- **Recommendation**: **KEEP** but flag that the result may be inconclusive due to the 0D/discrete issue.

### W2-4: MULTIMODE-RESONANCE-58

- **What it tests**: Whether 3-mode resonances among 63 collective modes have sufficient coupling to transfer energy.
- **Cosmological relevance**: LOW. The plan itself acknowledges that the broadening Gamma ~ 885 M_KK is so large that every triplet satisfies the resonance condition. The physical question is the coupling strength, which the plan correctly identifies.
- **Effectiveness assessment**: LOW. In the sudden-quench limit (confirmed by multiple S57 computations), the modes have no time to interact. The coupling coefficients will be computed, but the effective interaction time is dt_transit ~ 10^{-3} M_KK^{-1}, which is too short for any resonance to develop. This computation is likely to confirm the sudden-quench picture rather than discover new physics.
- **Recommendation**: **DEPRIORITIZE**. The sudden-quench limit has been confirmed so thoroughly (W1-1 rate scan: P_exc saturates above 10 M_KK, physical rate is 442 M_KK) that any in-transit energy redistribution is implausible.

### W3-1: ACOUSTIC-METRIC-58

- **What it tests**: Whether the Unruh acoustic metric for phonon propagation is self-consistent with the geometric Gibbons-Hawking temperature.
- **Cosmological relevance**: MEDIUM-HIGH. The acoustic metric is the bridge between the microscopic BCS physics and the macroscopic FRW expansion. If T_acoustic = T_GH, the framework's two descriptions (phononic and geometric) are unified. If they differ, it identifies where the mapping breaks.
- **Effectiveness assessment**: GOOD. This is one of the few Wave 3 computations that directly addresses the convention-mapping gap I identified in my Phononic-to-Cosmos assessment (Appendix, "No Friedmann equation from spectral action").
- **Recommendation**: **STRENGTHEN** -- promote to Wave 1 or early Wave 2. This computation builds the bridge between the internal SU(3) physics and the 4D FRW observer. It is more cosmologically relevant than several Wave 1 computations.
- **Notes**: The acoustic metric also provides the physical interpretation of the sound speed hierarchy c_fabric/c_Gold = 229.5, which enters the CMB multipole prediction (l ~ 721). Getting the acoustic metric right is prerequisite to making the CMB prediction quantitative.

### W3-2: ANDREEV-PHASE-58

- **What it tests**: Whether any loop on the CG(24) graph has a pi-phase Andreev shift (frustrated ground state).
- **Cosmological relevance**: LOW. Pi-junctions are interesting condensed-matter physics but have no direct cosmological observable.
- **Effectiveness assessment**: MODERATE. The result would constrain the topological structure of the fabric but does not connect to any cosmological test.
- **Recommendation**: **KEEP** at current priority (Wave 3).

### W3-3: SA-SADDLE-58

- **What it tests**: Whether the spectral action has a saddle at the fold in the (tau, sigma) plane.
- **Cosmological relevance**: MEDIUM. If the spectral action has a saddle where E_J does, the tension between geometric (SA) and many-body (BCS) physics (identified in S37) would be resolved. The spectral action is the natural object for deriving the Friedmann equation, so understanding its landscape matters for cosmological contact.
- **Effectiveness assessment**: GOOD. The comparison between SA Hessian and E_J Hessian eigenvalues is a clean structural test.
- **Recommendation**: **KEEP**.

### W3-4: EJ-3D-LANDSCAPE-58

- **What it tests**: Whether the E_J saddle persists on the full 3D U(2)-invariant surface (including volume-breaking direction).
- **Cosmological relevance**: LOW-MEDIUM. Relevant if the volume-preservation constraint is broken by cosmological dynamics, which is speculative.
- **Effectiveness assessment**: GOOD as a structural characterization.
- **Recommendation**: **KEEP** at current priority.

### W3-5: BKT-KUBO-58

- **What it tests**: Superfluid stiffness and exact BKT transition temperature on the finite graph.
- **Cosmological relevance**: LOW. BKT is a 2D phenomenon; the CG(24) graph has higher-dimensional topology. The cosmological consequences are unclear.
- **Effectiveness assessment**: MODERATE. The finite-size correction is useful for understanding the microscopic physics but does not connect to observables.
- **Recommendation**: **KEEP** at current priority.

### W3-6: SQ-OMEGA-GGE-58

- **What it tests**: The dynamic structure factor S(q, omega) of the post-transit GGE state.
- **Cosmological relevance**: MEDIUM-HIGH. This is "what the dark matter excitation spectrum looks like" (TES-collab 3.4). The DM dispersion relation is the input to the transfer function T(k) that I identified as the single most impactful cosmological computation in my Phononic-to-Cosmos recommendations (Section 8.1). S(q, omega) is a necessary precursor.
- **Effectiveness assessment**: GOOD. The hard gap, sub-gap continuum, and non-thermal Leggett features are all observable signatures that distinguish phononic DM from CDM/WDM.
- **Recommendation**: **STRENGTHEN** -- promote to Wave 2 or add a follow-up computation that converts S(q, omega) to a transfer function T(k). This is the bridge to Paper 15's methods.
- **Notes**: The comparison with thermal equilibrium S(q, omega) at the best-fit temperature (step 7) is exactly the right test. Non-thermal features in S(q, omega) would be a genuine novel prediction.

### W3-7: IMPEDANCE-BOUNDARY-58

- **What it tests**: Whether post-transit excitations are trapped within cells or propagate.
- **Cosmological relevance**: MEDIUM. If excitations are trapped (T < 0.5), the DM is confined to Planck-scale domains and cannot cluster gravitationally as CDM does. If transparent (T > 0.5), the DM can form large-scale structure.
- **Effectiveness assessment**: GOOD. The answer directly affects whether the DM candidate behaves like CDM at cosmological scales.
- **Recommendation**: **KEEP** -- and note that the result feeds into the transfer function T(k) calculation.

### W3-8: OMEGA-J-SWEEP-58

- **What it tests**: Whether omega_J tracks omega_att across the full transit.
- **Cosmological relevance**: LOW. Internal consistency check.
- **Effectiveness assessment**: MODERATE.
- **Recommendation**: **KEEP** at current priority.

### W3-9: OFF-JENSEN-DW-58

- **What it tests**: Whether cells at different sigma values produce domain walls with nonzero energy.
- **Cosmological relevance**: LOW-MEDIUM. If domain walls exist, they could contribute to the DM density or modify the CC.
- **Effectiveness assessment**: MODERATE. But S57 W3-6 already proved the GGE universality theorem (all cells have identical occupations). Off-Jensen differentiation would need a mechanism to break this universality.
- **Recommendation**: **KEEP** at current priority.

### W3-10: MASS-VARIATION-58

- **What it tests**: Whether Paper 16 eq 7.1 geometric mass variation changes the DM prediction by > 10%.
- **Cosmological relevance**: MEDIUM-HIGH. This directly addresses my recommendation 8.6 from Phononic-to-Cosmos: test the free-streaming constraint from Paper 16 (z_tr > 6.2 x 10^7). The mass variation integral determines how particle masses evolve during transit, which affects the production mechanism and the late-time velocity dispersion.
- **Effectiveness assessment**: GOOD. This is a straightforward computation using existing formulas.
- **Recommendation**: **STRENGTHEN** -- this should be paired with a free-streaming constraint check. Compute the phononic DM velocity dispersion at production and compare to the Paper 16 bound z_tr > 6.2 x 10^7. This would be the first direct confrontation between the DM candidate and hidden-sector constraints.

### W3-11: SQUEEZING-COVARIANCE-58

- **What it tests**: Whether Leggett modes are independently or correlatedly squeezed.
- **Cosmological relevance**: LOW-MEDIUM. Affects the DM energy partition at the ~factor-2 level.
- **Effectiveness assessment**: GOOD. The off-diagonal ratio ||C_off-diag||/||C_diag|| is a clean measure of mode-mode correlations.
- **Recommendation**: **KEEP** at current priority.

### W3-12: OFF-JENSEN-BCS-58

- **What it tests**: Sensitivity of the BCS gap and DM/CC partition to off-Jensen deformations.
- **Cosmological relevance**: MEDIUM. If Delta_BCS changes by > 5% at sigma = 0.01, the DM prediction has an additional systematic uncertainty.
- **Effectiveness assessment**: GOOD.
- **Recommendation**: **KEEP**.

### W3-13: EPSILON-CONSISTENCY-58

- **What it tests**: Cross-check of epsilon from the two-speed hierarchy against direct extraction (W0-3).
- **Cosmological relevance**: LOW. Internal consistency.
- **Effectiveness assessment**: MODERATE. If W0-3 already gives a precise epsilon, this is redundant. If they disagree, something fundamental is wrong.
- **Recommendation**: **KEEP** at current priority.

---

## 3. Missing Cosmological Tests

These are gates and computations that SHOULD be in S58 but are not. I draw from my Observational Gauntlet (Phononic-to-Cosmos Section 6) and the convention translation gap (Section 5.9).

### Proposed Gate: TRANSFER-FUNCTION-58

- **What it tests**: Whether the phononic DM transfer function T(k) is compatible with Lyman-alpha forest constraints.
- **Observable**: Small-scale matter power spectrum P(k) at k > 10 h/Mpc.
- **Framework prediction**: T(k) from phononic dispersion omega(K) = 2J(1 - cos Ka). Should produce a specific cutoff and oscillatory features.
- **LCDM prediction**: T(k) = 1 (CDM, no cutoff).
- **Suggested wave**: Wave 3 (uses S(q, omega) from W3-6 as input). Or a dedicated Wave 2 computation if W3-6 is promoted.
- **Priority**: CRITICAL. This is my top recommendation (Phononic-to-Cosmos Section 8.1). The phononic DM has a specific dispersion relation and a specific production mechanism. Paper 15 (Ganjoo-Erickcek-Lin-Mack 2022) provides the exact method: compute the transfer function for a hidden-sector particle with known dispersion, production temperature, and equation of state. If T(k) passes Lyman-alpha constraints (WDM mass equivalent > 5.3 keV), the DM candidate gains substantial credibility. If it fails, the candidate is excluded. Either way, this is decisive.

### Proposed Gate: FREE-STREAMING-58

- **What it tests**: Whether the phononic DM satisfies the free-streaming bound z_tr > 6.2 x 10^7 (Paper 16).
- **Observable**: Characteristic redshift at which phononic DM becomes non-relativistic.
- **Framework prediction**: z_tr from the Leggett mode group velocity c_Gold = 0.915 M_KK and the M_KK scale.
- **LCDM prediction**: No prediction (CDM is cold by assumption).
- **Suggested wave**: Wave 2 or 3. Can be computed alongside W3-10 (mass variation).
- **Priority**: HIGH. This is a necessary condition the DM candidate must satisfy. The computation is straightforward: compare the DM velocity dispersion at production to the NR transition criterion.

### Proposed Gate: FRIEDMANN-DERIVATION-58

- **What it tests**: Whether the Friedmann equation can be derived from the spectral action source terms, closing the H(z) gap.
- **Observable**: H^2 = (8 pi G / 3) rho_total, with rho decomposed into matter (quasiparticle) and vacuum (GGE excess) contributions.
- **Framework prediction**: H(z) from the spectral geometry.
- **LCDM prediction**: H(z) from Omega_m, Omega_Lambda, Omega_r.
- **Suggested wave**: New computation in Wave 2 (builds on W0-2 Lambda_eff(tau) and W2-1 gap scaling).
- **Priority**: CRITICAL. Without the Friedmann equation, the framework cannot produce distances, ages, or BAO scales. Every comparison between framework predictions and observational cosmology currently passes through an assumed (not derived) identification of E_matter with Omega_m. The convention translation table in my Phononic-to-Cosmos Appendix has "Not derived" in the H(z) row. This is the single most important unresolved mapping issue.

### Proposed Gate: W-RECALCULATION-58

- **What it tests**: What the post-Shattering equation of state w(z) actually is (see Section 4).
- **Observable**: w_0 and w_a from the GGE after the Shattering.
- **Framework prediction**: Needs recalculation. Pre-Shattering: w_0 in [-0.430, -0.589], w_a = 0. Post-Shattering: unknown.
- **LCDM prediction**: w_0 = -1, w_a = 0.
- **Suggested wave**: Wave 0 (should be computed alongside W0-1, since the emulator needs w as an input).
- **Priority**: CRITICAL. See Section 4.

### Proposed Gate: N-S-SURVIVING-ROUTE-58

- **What it tests**: Whether any surviving route to n_s ~ 0.965 produces a quantitative prediction.
- **Observable**: CMB spectral index n_s = 0.9655 +/- 0.0062 (Planck 2018, Paper 29).
- **Framework prediction**: 2.065 (CLOSED, naive KZ). Four routes survive but none computed.
- **LCDM prediction**: n_s = 1 - 2/N ~ 0.965 (slow-roll inflation).
- **Suggested wave**: Not in current plan. The plan explicitly defers this with the note "structurally obstructed." This is correct for the naive KZ route but the surviving routes (domain wall 1D DOS, instanton timescale, modulus fluctuations, multi-field interference) have not been attempted.
- **Priority**: HIGH (but I acknowledge the plan's argument that this requires qualitative breakthrough, not quantitative refinement). If N_pair = 2 (W1-1) reveals new physics, n_s routes should be re-evaluated as stated.

---

## 4. The w(z) Question

This is the user's top concern, and mine. Let me lay out the issue systematically.

### 4.1. The Pre-Shattering Prediction

The framework pre-registered (S49, P-8): w_0 = -0.509 +/- 0.079, w_a = -0.009 +/- 0.02.

This was computed from the GGE equation of state under a specific picture: the post-transit GGE is a static relic with 8 effective temperatures. The equation of state is w = P_vac/rho_vac, evaluated from the Volovik non-equilibrium formula. The S57 CC-SIGN computation (W2-3) gives w_GGE = -0.408.

### 4.2. What Changed with the Shattering

The Shattering (S57) introduced several physics changes that affect w:

1. **Channel decomposition**: The DM is now identified with specific channels (Leggett + BCS quasiparticles), and the CC with the GGE energy excess. The partition between DM and CC is different from the pre-Shattering picture.

2. **Sector cancellation**: The near-cancellation (+0.316 - 0.165 - 0.150 = +0.00145) in the Volovik formula means the effective vacuum energy is determined by a delicate balance between sectors. The equation of state w depends on how this balance evolves.

3. **Integrability protection**: The GGE is permanent (no thermalization). If the GGE is truly static, w_a = 0 exactly. But if the cancellation cascade extends through the KK tower (the "overshoot as fuel" reframing from Phononic-to-Cosmos Section 3b-ii), w_a != 0.

### 4.3. The Tension

Here is the specific tension I flagged in my assessment (Phononic-to-Cosmos Section 3b-ii):

The original w_a = 0 pre-registration assumed the GGE is a static relic. The reframing says the CC is dynamical because the sector cancellation cascade may still be active at late times. These cannot both be true:

- If integrability is exact and the GGE is static: w_a = 0 exactly. This is in 2.4-sigma tension with DESI DR2 (w_a = -0.73 +/- 0.31, where I am using the DR1 error bars as a rough guide since DR2 errors are not fully specified in the framework documents).

- If the cancellation cascade is ongoing: w_a < 0 (vacuum energy decreasing with time). This is qualitatively consistent with DESI but contradicts the integrability protection that makes the DM stable.

### 4.4. What Needs Recalculation

The S58 plan does not address this. The w observable appears in the W0-1 emulator, but the plan does not specify which w values are used or whether they have been recalculated post-Shattering.

Specifically, the following computations are needed:

1. **w from the Volovik partition**: Under the partition where F_Josephson is vacuum energy, what is the equation of state? The numerator (P_vac) and denominator (rho_vac) both change when you reassign 95.9% of the energy budget.

2. **w(tau) from W0-2**: The CC-CANCELLATION-SWEEP already computes Lambda_eff(tau) at 50 points. Computing w(tau) = P_vac(tau)/rho_vac(tau) at each point is a trivial extension. This would show whether w evolves during transit.

3. **w at late times**: What happens to w after the transit? The GGE is frozen by integrability, so the occupation numbers do not evolve. But the eigenvalues E_k do evolve if the SU(3) geometry continues to change. If tau is frozen at the fold value, E_k are fixed and w is constant. If tau continues to evolve, E_k change and w evolves. Which is it?

### 4.5. The DESI Confrontation

Current observational status:

| Dataset | w_0 | w_a | Source |
|:--------|:----|:----|:-------|
| DESI DR1 | -0.72 +/- 0.08 | -0.41 +/- 0.31 | Paper 30 |
| DESI DR2 | -0.752 | -0.73 | Framework docs |
| Framework (pre-S) | -0.509 +/- 0.079 | -0.009 +/- 0.02 | S49 P-8 |
| Framework (S57 W2-3) | -0.408 | not computed | S57 CC-SIGN |
| LCDM | -1 | 0 | Standard |

The framework's w_0 = -0.509 is 2.7-sigma from DESI DR1 and 3.1-sigma from DR2. The framework's w_0 = -0.408 (from S57) is even further -- 3.9-sigma from DR1. The tension is getting WORSE with each refinement, not better.

This needs to be confronted in S58. The W0-1 emulator should include w as a discriminant and report the tension explicitly. If the Volovik partition changes w (which it should -- different vacuum energy density means different P_vac/rho_vac), the new w must be compared to DESI.

### 4.6. Recommendation

Add a gate: **W-DESI-58** -- compute w_0 under the Volovik partition and compare to DESI DR2. PASS if |w_0 - w_0(DESI)| < 3-sigma. FAIL if > 5-sigma. This is the cleanest available observational test. It requires only combining W0-1 (Volovik partition) with W0-2 (Lambda_eff tau sweep) and existing E_J/E_c data.

---

## 5. Broader Cosmological Questions

### Hubble Tension

**Does S58 address it?** No. The framework does not produce H(z) and therefore cannot contribute to the H_0 = 67 vs 73 tension. My Paper 12 (Lin-Chen-Mack 2021) shows the tension cannot be resolved by pre-recombination physics alone. The framework's transit occurs at T ~ 10^{15} GeV, far before recombination. Without a late-time expansion history connecting T_init to the present, the framework is silent on this question.

**Should S58 address it?** Not directly. But the Friedmann derivation (proposed gate FRIEDMANN-DERIVATION-58) would be the first step. Without H(z), the framework cannot produce BAO scales, CMB distances, or SN Ia predictions -- the entire machinery of precision cosmology is inaccessible.

### S8 Tension

**Does S58 address it?** No. sigma_8 = 0.829 +/- 0.014 (Planck) vs lower values from weak lensing. The framework has not computed the matter power spectrum P(k) or the growth rate f*sigma_8.

**Should S58 address it?** The phononic DM transfer function T(k) (proposed gate TRANSFER-FUNCTION-58) would be the first step. If the phononic dispersion produces a characteristic cutoff at small scales, it could modify sigma_8 predictions. But this requires several prerequisite computations (S(q, omega), T(k), linear growth factor), making it a multi-session program.

### DESI w != -1 Hints

**Does S58 address it?** Partially. The W0-1 emulator includes w as an observable, and W0-2 maps Lambda_eff(tau). But the w values used in the emulator have not been recalculated post-Shattering (Section 4 above).

**Should S58 address it?** Yes, emphatically. This is the framework's cleanest confrontation with data. The pre-registered prediction (w_0 = -0.509) is already in 3+ sigma tension with DESI DR2. S58 should either (a) recalculate w under the Volovik partition and determine if the tension is reduced, or (b) acknowledge the tension and identify what modification would be needed.

### JWST High-z Galaxy Excess

**Does S58 address it?** No. The framework's T_init = 8.32 x 10^{15} GeV is GUT-scale. The JWST excess (massive galaxies at z > 10 appearing "too early") depends on the matter power spectrum at k ~ 1-10 h/Mpc and the star formation efficiency. The framework has not computed either.

**Should S58 address it?** Not directly, but the DM transfer function would be relevant. If phononic DM has less small-scale suppression than WDM, it could form halos earlier, potentially explaining the JWST excess. This is speculative but worth flagging.

### CMB Anomalies (Hemispherical Asymmetry, Cold Spot)

**Does S58 address it?** No. The framework predicts a specific CMB multipole feature at l ~ 721 with amplitude 24 muK^2 (Phononic-framework-hypothesis, P-9), but this is unrelated to the hemispherical asymmetry or cold spot.

**Should S58 address it?** Not until the framework has an expansion history H(z). The CMB predictions require integrating perturbation evolution from T_init through recombination, which needs the Friedmann equation.

### Matter-Antimatter Asymmetry

**Does S58 address it?** No. CP = 0 structurally (three proofs, S52). No baryon number violation mechanism has been identified. The framework satisfies the third Sakharov condition (out of equilibrium) abundantly but lacks the first two.

**Should S58 address it?** Not directly. The off-Jensen deformations (W2-2, W3-9, W3-12) could in principle break CP symmetry, but this is speculative. The Klein bottle cosmology parallel (Papers 25-26) suggests that non-orientable topology can provide CP violation, but SU(3) is orientable. This is a long-term challenge for the framework.

### Dark Matter Nature

**Does S58 address it?** Yes -- this is the session's primary focus. The DM is identified with quasiparticle excitations (Leggett + BCS) of the GGE relic. The W0-1 emulator tests whether this identification produces the correct Omega_DM h^2.

**Should S58 do more?** Yes. The framework makes specific predictions about the DM candidate that are testable:
- Self-interaction: sigma/m = 0 exactly (N_pair = 1). Testable against Bullet Cluster, cluster merger lensing.
- Annihilation: zero signal. Testable against 21cm observations (Papers 04, 17), gamma-ray searches.
- Free-streaming: determined by Leggett mode group velocity. Testable against Lyman-alpha (Paper 15-16).
- Neutron star heating: zero (no annihilation or interaction). Testable against nearby NS thermal emission (Paper 18).

None of these tests are in the S58 plan.

---

## 6. Priority Recommendations

Ranked by cosmological impact:

### 1. Recalculate w(z) Under the Volovik Partition (NEW -- highest priority)

**Cosmological question**: What is the dark energy equation of state?
**Observable**: w_0, w_a from DESI DR2/DR3.
**Connection**: The pre-registered w_0 = -0.509 is already 3+ sigma from DESI DR2 (w_0 = -0.752). The Volovik partition changes the vacuum energy definition, which changes w. This computation determines whether the tension is reduced, unchanged, or worsened. If worsened, the framework faces a serious observational challenge. If reduced, it is a genuine success. DESI DR3 will sharpen this to definitive levels within the next year.
**Effort**: Low -- extends W0-1 and W0-2 by computing P_vac/rho_vac at each tau under the new partition.

### 2. VOLOVIK-PARTITION-58 (W0-1 -- already top priority in the plan)

**Cosmological question**: What is the dark matter abundance?
**Observable**: Omega_DM h^2 = 0.1186 +/- 0.0020 (Planck 2018).
**Connection**: Direct confrontation of the framework's DM prediction with the most precisely measured cosmological parameter after the CMB acoustic scale.

### 3. Phononic DM Transfer Function T(k) (NEW)

**Cosmological question**: What is the small-scale matter power spectrum?
**Observable**: P(k) at k > 10 h/Mpc (Lyman-alpha, 21cm).
**Connection**: The phononic DM has a specific dispersion relation that produces a specific cutoff in P(k). Paper 15 methods apply directly. This is the most impactful cosmological computation the project could do (Phononic-to-Cosmos Section 8.1). S(q, omega) from W3-6 is a necessary precursor -- promote W3-6 to Wave 2 and add the T(k) calculation.

### 4. Promote W3-1 (Acoustic Metric) to Wave 1 or 2

**Cosmological question**: How does internal SU(3) physics map to 4D FRW expansion?
**Observable**: H(z), distances, BAO scale.
**Connection**: The acoustic metric is the bridge between the spectral geometry and FRW cosmology. Without it, the framework cannot produce any distance-based cosmological prediction. Getting the acoustic metric right is prerequisite to deriving the Friedmann equation, which is prerequisite to every other cosmological test (BAO, SN Ia, CMB distances).

### 5. RG-HESSIAN-58 (W1-2) + NPAIR2-INTEG-58 (W1-1) as a pair

**Cosmological question**: Can the CC be reduced from 10^{114} to 10^{0}?
**Observable**: Lambda_obs = 5.96 x 10^{-30} g/cm^3.
**Connection**: The CC magnitude is the framework's most severe problem. These two computations attack it from complementary directions (thermalization vs phase-space geometry). If either produces a positive result, the framework has a path to solving the CC problem -- which would be a major achievement in theoretical physics, not just in this framework.

---

## References

### Plan Sections Cited
- W0-1 (lines 156-184), W0-2 (187-204), W0-3 (208-226)
- W1-1 (249-279), W1-2 (283-306), W1-3 (309-329)
- W2-1 (355-377), W2-2 (380-400), W2-3 (404-427), W2-4 (430-448)
- W3-1 (472-489), W3-2 (493-509), W3-3 (513-529), W3-4 (533-549)
- W3-5 (553-569), W3-6 (573-591), W3-7 (594-611), W3-8 (614-631)
- W3-9 (634-651), W3-10 (654-671), W3-11 (674-691), W3-12 (694-711)
- W3-13 (714-731)
- Carry-Forward Registry (764-883)
- n_s note (883)
- What Success Looks Like (921-928)

### Phononic-to-Cosmos Assessment
- Section 3a (DM, lines 49-68)
- Section 3b (DE and CC, lines 69-145)
- Section 3b-ii (Overshoot as Fuel, lines 91-145)
- Section 5.9 (Convention mapping, lines 256-263)
- Section 6 (Observational Gauntlet, lines 266-383): Tests 1-8
- Section 8 (Recommendations, lines 404-433): 8.1-8.7
- Appendix (Convention Translation Table, lines 436-458)

### Mack/Greene Papers (by number, from researchers/Mack/)
- 09: Frieman-Turner-Huterer (2008), dark energy review
- 10: Lin (2019), TASI DM models
- 12: Lin-Chen-Mack (2021), uncalibrated cosmic standards
- 15: Ganjoo-Erickcek-Lin-Mack (2022), hidden sector transfer functions
- 16: Lin-Chen-Ganjoo-Hou-Mack (2023), hidden DM constraints
- 17: Hou-Mack (2024), DM annihilation cosmic dawn
- 18: Mack et al., nearest neutron stars DM heating
- 25: Greene (2025), non-orientable CP
- 26: Greene (2025), Klein bottle cosmology
- 29: Planck Collaboration (2018), cosmological parameters
- 30: DESI Collaboration (2024), BAO results

### S57 Results
- W0-3 (GGE equilibrium gap, ||delta_n|| = 0.195)
- W1-1 (finite rate transit, P_exc = 0.081)
- W1-2 (Leggett partition, f_DM = 0.119/0.312/0.440)
- W1-3 (gap scaling, alpha = -1.84)
- W2-3 (CC sign, Lambda_eff = +1.709, w_GGE = -0.408)
- W2-4 (DM abundance, Omega_DM h^2 bracket [0.017, 0.188])
- W3-5 (Bayesian emulator, NROY = 0%)
