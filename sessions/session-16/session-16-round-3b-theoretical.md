# Session 16, Round 3b: Theoretical Action Items — Executable Specifications
## QA-Theorist + Baptista-Analyst + Paasch-Analyst
## Date: 2026-02-13
## Status: FINAL

---

## EXECUTIVE SUMMARY

Six theoretical action items specified with executable pass/fail criteria: (1) Z_3 test procedure, (2) Bell roadmap milestones, (3) G-decomposition formalism, (4) Paasch FINAL binding prediction table, (5) order-one with physical D_K, (6) phonon-NCG dictionary final update with analogy break classification.

Every item follows the mandated format: Type, Specification, Pass/Fail, Feasibility, Timeline, Owner, Decisiveness, Dependencies, Code.

**Converged test counts**: 11 Tier 1 tests (executable from current infrastructure), 9 deferred to Tier 2 (8 require spinor transport or inter-generation identification; 1 requires higher irreps for convergence).

**Critical correction (verified)**: phi^{3/2} = 1.53158^{1.5} = **1.8954** (not 1.8985 as in earlier drafts). All instances corrected.

**Key structural insight (Paasch-analyst, Paper 18)**: Baptista's Z_3 has TWO layers:
- **LEFT Z_3 = (p-q) mod 3**: Commutes with D_K. Labels conserved quantum numbers. Does NOT create mass splitting. Visible in Tier 1 eigenvalues.
- **RIGHT Z_3**: Does NOT commute with D_K at s>0. THIS is the generation mechanism. Creates mass splitting within each dim(p,q)-fold degeneracy. Invisible in Tier 1 D_{(p,q)} eigenvalues. Requires spinor transport computation (~1 week, ~145 lines new code).
- Paper 18 lines 2560-2567: Inter-generation splitting occurs at "perturbation scale" (electroweak), NOT Jensen/Planck scale.

Consequence: Table B (inter-generation tests B3-B6) is **entirely deferred to Tier 2**. Only structural tests B1-B2 and a new coarse B3 (Jensen-level splitting bound) remain at Tier 1.

---

## 1. Z_3 TEST PROCEDURE
- Type: Test
- Specification:
  **Step 1 (TRIVIAL)**: For each (p,q) sector in the Tier 1 eigenvalue catalog, assign generation = (p-q) mod 3. Three sectors: Gen 0 [(p-q)=0 mod 3: (0,0), (1,1), (3,0), (0,3), (2,2), ...], Gen 1 [(p-q)=1 mod 3: (1,0), (0,2), (2,1), ...], Gen 2 [(p-q)=2 mod 3: (0,1), (2,0), (1,2), ...].

  **IMPORTANT**: This assigns LEFT Z_3, which labels conserved quantum numbers but does NOT produce inter-generation mass splitting. The physical generation mechanism requires RIGHT Z_3 (Tier 2, spinor transport).

  **Step 2 (MEDIUM)**: Modify `collect_spectrum()` in `tier1_dirac_spectrum.py` to use `np.linalg.eigh(1j * D_pi)` instead of `np.linalg.eigvals(D_pi)`, storing eigenvectors. Physical masses = |evals_h|. Net speedup expected (eigh ~3x faster than eigvals for Hermitian).

  **Step 3 (MEDIUM)**: Construct U(2) generators on V_{(p,q)} tensor C^16. Use existing `rho_pq[0], rho_pq[1], rho_pq[2]` (SU(2) generators) and `rho_pq[7]` (U(1) generator). Extract `Y_spinor` and `T_spinor[a]` from `branching_computation.py` (Session 7 U(2) embedding in Spin(8)). Total hypercharge: `Y_total = kron(rho_pq[7], I_16) + kron(I_dim, Y_spinor)`. Total SU(2) Casimir: `C2_total = sum[(kron(rho_pq[a], I_16) + kron(I_dim, T_spinor[a]))^2 for a=0,1,2]`.

  **Step 4 (MEDIUM)**: For each eigenvector, compute expectation values `<psi|Y_total|psi>` and `<psi|C2_total|psi>`. Round Y to nearest physical value; solve j(j+1)=|C2| for half-integer j. Map (Y,j) to SM particle type via Baptista eq 2.66.

  **Step 5 (TRIVIAL)**: Group eigenvalues by (generation, Y, j). For each particle type, extract lightest mass per generation.

  **Step 6 (EASY)**: Compute inter-generation mass ratios: m_gen1/m_gen0, m_gen2/m_gen0, m_gen2/m_gen1 for each particle type. Compare to SM mass ratios.

  **Step 7 (EASY)**: Evaluate at s = {0, 0.15, 0.30, 0.50, 0.60, 1.14} and at s_0 from V_eff (if available). Special attention to s=0.30 (gauge-coupling-derived backup from Round 2d-ii).

- Pass/Fail:

  **Tier 1 Tests** (from LEFT Z_3 + U(2) quantum numbers):

  | Criterion | Condition | Verdict |
  |-----------|-----------|---------|
  | B1: Three generations | Each Z_3 sector has identical (Y,j) content | STRUCTURAL (expected PASS by construction) |
  | B2: Degeneracy broken | Gen 1/Gen 2 degenerate at s=0, split at s>0 | STRUCTURAL (from C_2(1,0) = C_2(0,1) = 4/3) |
  | B3: Jensen-level splitting bound | All inter-generation mass ratios from LEFT Z_3 are O(1), specifically ratio < 10 | PASS if < 10, FAIL if > 100, INCONCLUSIVE if 10-100 |

  NOTE on B3: LEFT Z_3 splitting is from Casimir differences O(1), so ratios should be O(1). The physical O(200) hierarchy (e.g., m_tau/m_e = 3477) must come from RIGHT Z_3 at electroweak perturbation scale, not Jensen deformation. If LEFT Z_3 already produces O(100+) splitting, it contradicts the two-scale structure of Paper 18.

  **Tier 2 Tests** (deferred, require RIGHT Z_3 spinor transport):

  | Criterion | Condition | Tier 2 requirement |
  |-----------|-----------|-------------------|
  | B4: Hierarchy exists | At least one RIGHT Z_3 inter-generation ratio > 2 | Spinor transport eigenvectors (~1 week) |
  | B5: Non-uniform hierarchy | m_gen1/m_gen0 differs from m_gen2/m_gen1 by > factor 2 | Same |
  | B6: Lepton OOM | Charged lepton ratio within factor 10 of 207 (i.e., 20-2070) | Same |
  | B7: Quark OOM | Up-type quark ratio within factor 10 of 500 (i.e., 50-5000) | Same |

  **Scorecard**: B1-B2 PASS = generation mechanism works (+5-10%). B3 PASS (< 10) = two-scale structure confirmed (+3%). B4-B5 PASS = nontrivial hierarchy (+5%). B6 or B7 PASS = quantitative success (+10-15%). B1 FAIL = generation mechanism closed (-5%).

  **Consensus priors** (Round 2c, revised): B1-B2: ~80%. B3: ~75% (LEFT splitting SHOULD be O(1)). B4 (Tier 2): ~45%. B6 (Tier 2): ~12%. B7 (Tier 2): ~12%.

- Feasibility: GREEN (Tier 1); YELLOW (Tier 2, ~1 week additional for spinor transport)
- Timeline: ~2 days Tier 1 (Phase 1: eigenvectors 4h, Phase 2: U(2) generators 4h, Phase 3: Z_3+analysis 4h, Phase 4: multi-s evaluation 2h). ~1 additional week for Tier 2 (~145 lines new code for spinor transport).
- Owner: sim-specialist (code) + baptista-analyst (D_K validation) + qa-theorist (phonon interpretation)
- Decisiveness: 8/10 Tier 1 (parameter-free, representation-theoretic, independent of V_eff). 9/10 Tier 2 (generation hierarchy = SM litmus test).
- Dependencies:
  - `tier1_dirac_spectrum.py` (existing, all infrastructure)
  - `branching_computation.py` (Session 7, U(2) embedding -- must extract Y_spinor, T_spinor)
  - V_eff s_0 (Round 3a) for evaluation at physical point (can run independently at multiple s)
  - Tier 2: Baptista Paper 18 spinor transport formalism
- Code:
  - MODIFY: `tier0-computation/tier1_dirac_spectrum.py` (~20 lines: eigh instead of eigvals)
  - NEW: `tier0-computation/tier1_u2_projection.py` (~315 lines: U(2) generators, quantum number assignment, Z_3 labeling, generation analysis, phi test)
  - REUSE: `tier0-computation/branching_computation.py` (U(2) spinor embedding extraction)
  - NEW (Tier 2): `tier0-computation/tier2_spinor_transport.py` (~145 lines: RIGHT Z_3 eigenvectors, inter-generation splitting)

---

## 2. BELL ROADMAP MILESTONES
- Type: Test / Axiom (multi-phase theoretical program)
- Specification:
  Four phases, ordered by priority (Born rule FIRST, CHSH LAST). One independent phase (Pfaffian).

  **Phase D: Pfaffian Z_2 Invariant (INDEPENDENT)**
  - Compute sgn(Pf(J * D_F(s))) for s in [0, 2.0] at ~50 points
  - D_F = finite Dirac operator on H_F = C^32 extracted from D_K eigenvectors
  - J = real structure on C^32 (known from Session 8, branching_computation_32dim.py)
  - The product J*D_F is antisymmetric on the appropriate subspace (KO-dim 6 guarantees)
  - Binary outcome: sign CHANGES (topological transition) or CONSTANT (no transition)
  - If sign changes at s_c: gap closure at s_c = massless fermion (topologically protected)
  - Neutrino mass prediction: lightest neutrino massless or near-massless (Level 4 Venus Rule candidate)

  **Phase A: Born Rule Strengthening**
  - A1: Derive preferred measurement basis from spectral geometry of A_F = C+H+M_3(C)
    - The projective modules over A_F define natural "observables"
    - Check: do U(2) quantum numbers (from Z_3 test Step 3) define the measurement basis?
  - A2: Verify Gleason's theorem applies to A_F on H_F = C^32
    - Gleason requires dim >= 3 per factor. A_F has factors C (dim 1), H (dim 2), M_3(C) (dim 3).
    - C factor: dim 1, Gleason FAILS. H factor: dim 2, Gleason FAILS. M_3(C): dim 3, PASSES.
    - Expected result: Gleason applies to color sector only. Leptonic sector needs separate argument.
  - A3: Compute probability from fiber integration for spin-1/2 example
    - Use Baptista eq 2.26: integral_K Tr(D2^P dagger L_{X^H} D1^P) vol_K
    - Concrete setup: two-particle state in L^2(K x K), measure spin along axis n
    - Born rule probability |<n|psi>|^2 should emerge from geometric L^2 norm

  **Phase B: Measurement Definition**
  - B1: Define "measurement along axis n" as A_F operator on H_F
    - The spin observable is an element of A_F (specifically, an element of the H = quaternion factor)
    - The quaternion algebra H provides SU(2) spin algebra: sigma_x, sigma_y, sigma_z
    - "Spin measurement along n" = n . sigma where sigma = (sigma_x, sigma_y, sigma_z) in H
  - B2: Show U(2) quantum numbers define measurement basis
    - The (Y, j) quantum numbers from Z_3 test Step 3 determine which A_F observable is measured
    - This connects the algebraic structure to physical measurement outcomes
  - B3: Derive Stern-Gerlach outcome from spectral geometry
    - The A_F operator n.sigma on H_F has definite eigenvalues (+1, -1 for j=1/2)
    - The eigenprojections Pi_+ and Pi_- define the measurement outcomes
    - The probability is Tr(rho * Pi_+) where rho is the reduced state after partial trace over K

  **Phase C: Bell CHSH**
  - C0 (PREREQUISITE): Characterize fiber-averaged C*-algebra
    - Compute: is the algebra of observables after fiber integration isomorphic to B(H)?
    - If YES: standard CHSH computation applies. If NO: need modified Bell framework.
    - Method: take algebra generated by {integral_K f(h) O(h) dh : f in C(K), O in A_F}
    - Check: does this algebra contain all bounded operators on the 4D Hilbert space?
  - C1: With Born rule (Phase A) + measurement (Phase B), compute CHSH
    - Standard CHSH operator: S = a.sigma tensor (b+b').sigma + a'.sigma tensor (b-b').sigma
    - Optimize over measurement axes a, a', b, b'
    - Target: S_max = 2*sqrt(2) (Tsirelson bound)
  - C2: Identify entanglement mechanism
    - Two particles share state Psi(h1,h2) in L^2(K x K) that is non-factorizable
    - CG algebra governs mode coupling: C^k_{nm} connects sectors
    - Non-commutativity of CG coefficients (8_a = Umklapp channel) provides correlations beyond S=2
  - C3: Check Tsirelson bound saturation
    - If S_max = 2*sqrt(2): framework reproduces standard QM exactly
    - If S_max < 2*sqrt(2): framework is a SUBQUANTUM theory (new physics!)
    - If S_max > 2*sqrt(2): framework violates Tsirelson bound (inconsistent with QM)

- Pass/Fail:
  | Phase | PASS | FAIL | Timeline |
  |-------|------|------|----------|
  | D (Pfaffian) | Sign changes at s_c in [0,2] | Constant sign | Hours (once D_F available) |
  | A (Born rule) | Concrete probability calculation from fiber integration matches |<n|psi>|^2 | No convergence after 4 weeks | 2-4 weeks |
  | B (Measurement) | A_F operator reproduces Stern-Gerlach statistics | No clear projector from A_F | 1-3 months |
  | C (Bell) | S_max = 2*sqrt(2) from fiber-averaged observables | S_max <= 2 (hidden variable limit) | 3-12 months |

  **Phase D special rule (Pfaffian Override)**: If Pfaffian sign changes, it SUPERSEDES all other priorities. Gap closure -> massless fermion prediction -> Level 4 Venus test candidate. Both Giant pairs endorse this override.

  **Overall probability of deriving CHSH = 2*sqrt(2) within 1 year: 20-30%.**

- Feasibility: Phase D: GREEN. Phase A: YELLOW. Phase B: YELLOW-RED. Phase C: RED.
- Timeline: Phase D: hours-days (once D_F on C^32 available). Phase A: 2-4 weeks. Phase B: 1-3 months. Phase C: 3-12 months.
- Owner: qa-theorist (all phases) + gen-physicist (Phase C algebra)
- Decisiveness: Phase D: 9/10 (binary, zero params, topological). Phase A: 5/10. Phase B: 6/10. Phase C: 10/10 (Bell is THE foundational test).
- Dependencies:
  - Phase D requires: D_F on C^32 from D_K eigenvectors (-> order-one spec, Item 5)
  - Phase A requires: A_F extraction (partially complete), U(2) quantum numbers (Item 1)
  - Phase B requires: Phase A + A_F operators explicitly constructed
  - Phase C requires: Phases A + B + C0 (fiber-averaged algebra characterization)
  - Key dependency chain: Item 5 (order-one) -> D_F -> Phase D (Pfaffian) -> possible override
- Code:
  - Phase D: ~50 lines (Pfaffian computation on antisymmetric matrix). Uses `scipy.linalg` or direct determinant. J matrix from `branching_computation_32dim.py`.
  - Phase A: ~200 lines (fiber integration example, Gleason check). Primarily mathematical, not computational.
  - Phase B: ~300 lines (A_F projectors, measurement statistics). Requires A_F algebra explicitly.
  - Phase C: ~500+ lines (CHSH optimization, entanglement computation). Research-level code.

---

## 3. G-DECOMPOSITION FORMALISM
- Type: Formula
- Specification:
  Systematically express every Standard Model constant as a function of (s_0, SU(3) topology), eliminating G_4 as a fundamental parameter.

  **The Master Dictionary**: Every SM constant has a spectral origin.

  | SM Constant | Spectral Expression | Source |
  |-------------|-------------------|--------|
  | G_4 (Newton's constant) | G_12 / Vol(K, g_s) = G_12 / Vol(K, g_0) [TT preserves volume] | Handout Part C.I |
  | g_1 (U(1) coupling) | ~ e^{-s_0} [from Jensen metric on u(1) subspace] | Session 13, Round 2c |
  | g_2 (SU(2) coupling) | ~ e^{s_0} [from Jensen metric on su(2) subspace] | Session 13, Round 2c |
  | g_3 (SU(3) coupling) | ~ e^{-s_0/2} [from Jensen metric on C^2 coset] | Session 13, Round 2c |
  | g_1/g_2 | e^{-2*s_0} [parameter-free ratio once s_0 fixed] | Round 2d-ii |
  | hbar | From Klein 1926 periodicity: p_internal = n*hbar/R_K | Proven #10 |
  | Fermion masses | D_K eigenvalues lambda_n(s_0) [Paper 17 Corollary 3.4, line 833] | Round 2b |
  | Mass ratios | lambda_n(s_0)/lambda_m(s_0) [G cancels] | Round 2b |
  | Higgs VEV | Related to sigma_0 from coupled V(sigma, s) minimization | Baptista eq 3.87 |
  | Cosmological constant | V_eff(s_0) = spectral action at minimum | Round 2a |
  | Yukawa couplings | [D_K, L_X] matrix elements in eigenspinor basis | Paper 17 eq 1.4 |
  | CKM matrix | Misalignment between mass eigenstates and gauge eigenstates | Paper 18 Props 6.2-6.3 |
  | Weinberg angle | sin^2(theta_W) = g_1^2/(g_1^2+g_2^2) = e^{-2s_0}/(1+e^{-2s_0})... | Derived from g_1/g_2 |
  | Generation number | 3 (from Z_3 center of SU(3)) | Round 2b |

  **The key question** (from Handout Part C.I): Can EVERY SM constant be expressed as f(s_0, SU(3) topology)?

  **Computation**: For each entry, write the explicit formula in terms of s_0 and SU(3) spectral data. Then evaluate at s_0 from V_eff. Compare to measured values.

  **The gauge coupling test** (Sagan's Venus candidate, Round 2d-ii):
  - g_1/g_2 = e^{-2*s_0} at compactification scale
  - Measured at M_Z: g_1/g_2 ~ 0.55 (from sin^2(theta_W) ~ 0.231)
  - RG running from M_Pl to M_Z: ~10-15% systematic uncertainty
  - PASS: e^{-2*s_0} in [0.4, 0.7]. STRONG PASS: in [0.45, 0.60]. FAIL: outside [0.2, 0.8].
  - Diagnostic: s_0 = 0.30 gives e^{-0.60} = 0.549 (0.2% from measured).
  - Constraint on viable range: s_0 in [0.15, 0.50] for gauge consistency.
  - **Elevated to Rank 2 test** (Hawking-Sagan, Round 3b): This is the first Level 3 test (retrodiction, not prediction, but with zero fit parameters once s_0 is determined).

- Pass/Fail:
  | Criterion | Condition | Verdict |
  |-----------|-----------|---------|
  | Gauge coupling ratio | e^{-2*s_0} in [0.4, 0.7] | Level 3 consistency |
  | Multiple mass ratios match | >= 3 mass ratios within factor 3 of measured values at s_0 | Quantitative success |
  | All SM constants expressible | Every constant in the table has an explicit formula | Structural completeness |
  | FAIL: gauge coupling catastrophic | e^{-2*s_0} outside [0.2, 0.8] | s_0 inconsistent with known physics |

- Feasibility: YELLOW (formalism: GREEN; evaluation requires s_0 from V_eff which has DOF caveat)
- Timeline: Formalism document: ~1 day. Numerical evaluation: hours (after V_eff + Z_3 complete).
- Owner: baptista-analyst (Baptista equation identification) + kk-theorist (KK reduction formulas) + qa-theorist (phonon interpretation)
- Decisiveness: 7/10 (structural completeness test + first Level 3 test from gauge couplings)
- Dependencies:
  - V_eff s_0 (Round 3a, Item 1 in computational spec)
  - Z_3 + U(2) particle identification (Item 1 above)
  - Backup: if V_eff monotonic, use gauge-coupling-derived s_0 = 0.30 (Round 2d-ii proposal)
- Code:
  - NEW: `tier0-computation/g_decomposition.py` (~200 lines: SM constant formulas, evaluation at s_0, comparison table)
  - REUSE: `tier1_dirac_spectrum.py` (eigenvalues at any s), `tier1_spectral_action.py` (V_eff)

---

## 4. PAASCH FINAL BINDING PREDICTION TABLE
- Type: Test
- Specification:
  Four pre-registered prediction tables from Round 2c, incorporating the critical N(j)^{3/2} correction and the phi^{3/2} = **1.8954** target.

  **CRITICAL CORRECTION** (Round 2c, confirmed by all 4 Giants, computation-verified):
  Paasch's mass numbers satisfy N(j) = (mj/me)^{2/3}, giving mj = me * N(j)^{3/2}.
  Since D_K eigenvalues ARE masses (Paper 17 Corollary 3.4), eigenvalue ratio = mass ratio.
  The phi test target is lambda_i/lambda_j = phi^{3/2} = **1.8954**, NOT phi = 1.53158.
  The z=3.65 phi^1 signal at s=1.14 tested the WRONG quantity for Paasch validation.

  **Table A: Inter-Species Mass Ratios at s_0** (Tier 1, 5 tests)

  | # | Test | Target ratio (mi/mj) | 5% threshold | 1% threshold | Null model |
  |---|------|---------------------|-------------|-------------|------------|
  | A1 | lambda_p / lambda_K | 1.901 (= mp/mK) | <5%: SUGGESTIVE | <1%: STRONG | Permutation of sectors |
  | A2 | lambda_K / lambda_pi | 3.538 (= mK/m_pi) | <5%: SUGGESTIVE | <1%: STRONG | Same |
  | A3 | lambda_p / lambda_pi | 6.724 (= mp/m_pi) | <5%: SUGGESTIVE | <1%: STRONG | Same |
  | A4 | lambda_p / lambda_mu | 8.879 (= mp/m_mu) | <5%: SUGGESTIVE | <1%: STRONG | Same |
  | A5 | lambda_eta / lambda_pi | 3.929 (= m_eta/m_pi) | <5%: SUGGESTIVE | <1%: STRONG | Same |

  Prerequisite: particle-to-sector identification from U(2) quantum numbers (Item 1, Step 4). NOT fitted to match ratios.
  Scorecard: 0-1 matches at 5%: NULL. 2-3 matches: SUGGESTIVE. 4+ matches: STRONG. 3+ at 1%: DECISIVE.
  Venus Rule (Sagan, Round 2d-ii): Table A can REFUTE but NOT CONFIRM (mass ratios already known as SM inputs).

  **Table B: Inter-Generation (Z_3) Tests** (RESTRUCTURED per Paasch-analyst)

  **Tier 1** (from LEFT Z_3, Items B1-B3 in Item 1 above):
  - B1: Three generations (structural)
  - B2: Degeneracy broken at s>0 (structural)
  - B3: Jensen-level splitting O(1), specifically < 10 (two-scale consistency check)

  **Tier 2** (deferred, require RIGHT Z_3 spinor transport):
  - B4-B7: Hierarchy existence, non-uniformity, lepton OOM, quark OOM
  - **Rationale**: Paper 18 two-layer Z_3 means generation structure (mass hierarchy O(200)) is invisible in Tier 1 D_{(p,q)} eigenvalues. Generation splitting lives in dim(p,q)-fold degeneracy lifting. LEFT Z_3 = (p-q) mod 3 commutes with D_K and labels conserved quantum numbers but does NOT create mass splitting. RIGHT Z_3 does NOT commute with D_K at s>0 and THIS is the generation mechanism. Inter-generation splitting occurs at electroweak perturbation scale, not Jensen/Planck scale (Paper 18 lines 2560-2567).
  - **Timeline**: ~1 week after Tier 1 complete (~145 lines new spinor transport code)

  **Table C: Golden Ratio / Phi Tests** (REVISED)

  **Tier 1** (3 tests):

  | # | Test | Target | Tolerance | Note |
  |---|------|--------|-----------|------|
  | C1 | f_N in successive N-value ratio at s_0 | 1.5279 (= (2/Phi)^2) | <0.5% | Test on Paasch spiral ordering of identified particles |
  | C2 | phi in N-value ratio at s_0 | 1.53158 (= phi_paasch, from x=e^{-x^2}; NOT golden ratio) | <0.1% | N(p)/N(K) = 150/98 = 1.5306. THE Paasch prediction. |
  | C5 | phi^{3/2} in eigenvalue ratio at s_0 | **1.8954** (= phi^{3/2}) | <0.5% | THE corrected Paasch spectral test. NEVER RUN. |

  **C5 is the headline test.** It has never been computed. Pre-registered. Requires U(2) identification (Item 1) to assign sectors to particles. mp/mK = 938.272/493.677 = 1.9006. phi^{3/2} = 1.8954. Agreement: 0.27%. Jensen deformation at s_0 could close the gap.

  **Tier 2** (5 tests, deferred):

  | # | Test | Reason deferred | Tier 2 requirement |
  |---|------|-----------------|--------------------|
  | C3 | f_N in Seeley-DeWitt coefficient ratio | >100% systematic error at p+q<=3 | Higher irreps (p+q>=6) for convergence |
  | C4 | Golden ratio in M-value structure | Need 4+ M-values identified | Full particle identification from U(2)+Z_3 |
  | C6 | tau/proton mass ratio vs phi^{3/2} | tau is inter-generation (gen 2) | RIGHT Z_3 spinor transport |
  | C7 | tau/muon ratio test | tau is inter-generation | Same |
  | C8 | f_N chain WITHIN vs BETWEEN generations | NEW: two-scale prediction | RIGHT Z_3 spinor transport |

  **NOTE on C6**: m_tau/m_p = 1.8938 (0.089% from phi^{3/2} = 1.8954), which is 3x closer than p/K (0.271%). This is remarkably suggestive but is an INTER-generation test (tau = gen 2, proton = gen 0), so it must wait for RIGHT Z_3 identification at Tier 2.

  **NOTE on C8 (NEW)**: The f_N geometric chain N(pi)*f_N = N(g), N(g)*f_N = N(K), N(K)*f_N ~ N(p) should hold WITHIN each generation. The chain may BREAK between generations, giving a two-scale structure: intra-generation scaling by f_N, inter-generation scaling by a different factor from RIGHT Z_3. This is a PREDICTION, testable at Tier 2.

  **Table D: Paasch Empirical (Internal to Paasch Framework)** (separate section, 4 tests)

  | # | Test | Description | Threshold |
  |---|------|-------------|-----------|
  | D1 | N(j) = 7n pattern | All assigned N-values are multiples of 7 | 4+ of 5 particles |
  | D2 | f_N exponential chain | N(pi)*f_N = N(g), N(g)*f_N = N(K), N(K)*f_N ~ N(p) within 1% | All 3 links |
  | D3 | Alpha derivation | alpha = (1/f)^{2*n3} with n3=10, f from ln(x)=-x | Within 10^{-5} of 0.0072974 |
  | D4 | Proton mass formula | mp = F(me, alpha, N(b)=112, n3=10) | Within 10^{-6} of measured |

  Note: D1-D4 are internal to Paasch's framework, tested against measured masses, independent of D_K. They validate Paasch's algebraic structure, not the phonon-exflation geometry.

  **NOTE on D1**: The 7n pattern breaks at K* (20.71) and proton (21.43). The f_N geometric progression (D2) is more fundamental and SUBSUMES D1 where it holds. Retain D1 with note about f_N being the deeper structure.

  **Supplementary: f_M Late Amendment (Round 2c) -- SUPPLEMENTARY BINDING**
  - N_(3,0)/N_(1,1) = [lambda_(3,0)/lambda_(1,1)]^{2/3} = [sqrt(58/31)]^{2/3} = 1.232 at s=0
  - Compare: f_M = 2/Phi = 1.236 (0.32% off). f_N = f_M^2 = 1.528.
  - Check at s = {0.15, 0.30, s_0}: does 1.232 shift toward 1.236?
  - STATUS: SUPPLEMENTARY BINDING. Not a standalone test, but supports or undermines f_N significance. If f_M tracks toward 1.236 at s_0, it strengthens the case for f_N being geometric. If it drifts away, f_N agreement at s=0 is coincidental.

  **T_c estimate** (theoretical note, not formal test): Paasch T_c ~ O(100 MeV) from mE = sqrt(me*mp). This provides a rough freeze-out temperature scale. Informational only; not included in binding table.

  **Combined Decision Matrix** (Round 2c, endorsed by Giants, UPDATED):

  | Outcome | Tests passed | Framework impact | Paasch impact |
  |---------|-------------|-----------------|---------------|
  | FULL SUCCESS | A(4+), B-Tier2(B6+B7), C(C1 or C2 or C5) | +15-20% -> 65-80% | "Kepler finds Newton" |
  | PARTIAL SUCCESS | A(2-3), B-Tier1(B1-B3), C(none) | +5-10% -> 55-70% | Z_3 works, mass scaling approximate |
  | MIXED | A(0-1), B-Tier1(B1-B2), C(C5 only) | +/- 0 -> 50-62% | Phi real but mass numbers wrong |
  | NULL | A(0), B-Tier1(B1-B2), C(none) | -10% -> 40-52% | Paasch orphaned |
  | CATASTROPHIC | B(B1 fails) | -15% -> 35-47% | Z_3 mechanism closed |

  **Backup s_0**: If V_eff is monotonic (no classical or 1-loop minimum), use gauge-coupling-derived s_0 = 0.30 from Round 2d-ii (gives g_1/g_2 = e^{-0.60} = 0.549, within 0.2% of measured). All tests in Tables A-D can be evaluated at this backup value.

  **Converged Test Count Summary**:
  - **Tier 1**: A(5) + B(3: B1-B3) + C(3: C1,C2,C5) = **11 tests**
  - **Tier 2**: B(4: B4-B7) + C(5: C3,C4,C6,C7,C8) = **9 deferred** (but 8 require new infrastructure; C3 requires only higher irreps)
  - **Paasch-internal**: D(4) = **4 tests** (separate section, independent of D_K)

- Pass/Fail: See individual table criteria above.
- Feasibility: GREEN (all Tier 1 tests run from Z_3 + U(2) output)
- Timeline: Hours (after Item 1 Z_3 test complete) for Tier 1. ~1 week additional for Tier 2.
- Owner: paasch-analyst (table design, N-value analysis) + sim-specialist (numerical evaluation) + qa-theorist (phonon interpretation)
- Decisiveness: Table C5: 8/10 (pre-registered, untested, phi^{3/2} target). Table A: 6/10 (can refute). Table B Tier 1: 5/10 (structural). Table B Tier 2: 8/10 (generation hierarchy). Table D: 4/10 (internal).
- Dependencies:
  - Z_3 + U(2) particle identification (Item 1, Steps 3-5): HARD dependency for Tables A, B, C
  - V_eff s_0 (Round 3a): required to evaluate at physical point (backup: s_0 = 0.30)
  - Tier 1 eigenvalues at target s: already available from `tier1_dirac_spectrum.py`
  - Tier 2: RIGHT Z_3 spinor transport (Item 1, Tier 2 code)
- Code:
  - NEW: `tier0-computation/paasch_binding_tests.py` (~250 lines: N-value computation from eigenvalues, f_N chain test, phi^{3/2} test, mass ratio comparison, decision matrix evaluation)
  - REUSE: `tier1_u2_projection.py` (Item 1, generation-grouped eigenvalue catalog)

---

## 5. ORDER-ONE WITH PHYSICAL D_K
- Type: Test
- Specification:
  Test the NCG order-one condition [[D_F, a], Jb*J^{-1}] = 0 for a, b in A_F, using the PHYSICAL finite Dirac operator D_F extracted from D_K on (SU(3), g_s).

  **Background**: All toy D_F models failed (Session 10-11). The chirality catch-22 was diagnosed as an artifact of wrong gamma_F identification (Sessions 11, unanimous). The physical D_F must come from D_K via:

  **Step 1: D_K eigenvectors** (from Item 1 Step 2, already stored as part of Z_3 computation)
  - For each (p,q) sector and Jensen parameter s, the eigenvectors of D_{(p,q)} live in V_{(p,q)} tensor C^16
  - These are the internal-space spinor wavefunctions phi_alpha

  **Step 2: Finite Dirac operator construction**
  - Restrict to the LOWEST eigenvalue per (Y,j,generation) particle type
  - This gives ~16-32 eigenvectors spanning the physical fermion sector
  - D_F restricted to this subspace: D_F_{alpha beta} = lambda_alpha * delta_{alpha beta} in the mass basis
  - In the REPRESENTATION basis (for order-one): D_F_{alpha beta} = <phi_beta, D_K phi_alpha>
  - The representation basis is determined by U(2) quantum numbers (Item 1 Step 4)

  **Step 3: Order-one test**
  - Construct A_F generators in the eigenvector basis
  - For each pair (a, b) with a in A_F, b in A_F:
    - Compute commutator_1 = D_F @ a - a @ D_F
    - Compute Jb_conj = J @ b.conj() @ J^{-1}
    - Compute commutator_2 = commutator_1 @ Jb_conj - Jb_conj @ commutator_1
    - Check: ||commutator_2|| < epsilon (machine precision)
  - Test all 9 factor pairs: (C,C), (C,H), (C,M_3), (H,C), (H,H), (H,M_3), (M_3,C), (M_3,H), (M_3,M_3)

  **Step 4: Corrected chirality verification**
  - Verify {D_F, gamma_F^correct} = 0 where gamma_F^correct = product grading (gamma_PA x gamma_CHI)
  - This was confirmed in Session 11 to be the correct chirality
  - Lichnerowicz theorem GUARANTEES this for D_K on any even-dim spin manifold

  **Step 5: A_F identification**
  - If 9/9 pass: A_F is the full commutant restricted to the physical subspace
  - If partial pass: identify which factor pairs pass/fail, compare to toy D_F results (5/9 for Connes left Yukawa)
  - The -2y structural factor (gen-physicist, Session 11) predicts C+H self-interaction is the hardest

  **Subtlety from Round 2b**: D_F in the mass basis is DIAGONAL. Order-one for diagonal D_F is equivalent to: for each pair of distinct eigenvalues lambda_alpha != lambda_beta, the matrix element <phi_alpha|[a, Jb*J^{-1}]|phi_beta> = 0. This means the order-one condition reduces to: the A_F action preserves the D_K eigenspaces. This is a MUCH simpler test than the general case.

- Pass/Fail:
  | Criterion | Condition | Verdict |
  |-----------|-----------|---------|
  | 9/9 order-one | All factor pairs satisfy ||[[D_F, a], Jb*J^{-1}]|| < 1e-10 | FULL PASS: A_F extraction complete |
  | 5-8/9 order-one | M_3(C) cross-factor passes, C+H partial fail | PARTIAL: matches toy D_F pattern, improvements possible |
  | <5/9 order-one | Multiple factor pairs fail including M_3 | FAIL: physical D_K incompatible with A_F |
  | Chirality | {D_F, gamma_F^correct} = 0 at machine epsilon | Expected PASS (Lichnerowicz theorem) |

  **Conditional on eigenvector quality**: If U(2) quantum numbers are not cleanly quantized (Item 1 risk), the eigenspace identification may be ambiguous. Mitigation: use Casimir projectors instead of individual eigenvectors.

- Feasibility: YELLOW (clear algorithm, but requires eigenvectors + A_F in eigenvector basis)
- Timeline: ~1 week (after Item 1 eigenvectors available)
- Owner: baptista-analyst (D_K operator specification) + sim-specialist (numerical implementation) + qa-theorist (BdG interpretation)
- Decisiveness: 9/10 (resolves the chirality catch-22 definitively; determines if A_F extraction is possible)
- Dependencies:
  - Item 1 (Z_3 test): eigenvectors, U(2) quantum numbers, generation labeling (HARD)
  - `branching_computation_32dim.py`: J matrix, gamma_F (existing)
  - `branching_computation.py`: A_F generators in original basis (existing)
  - Basis change: A_F generators must be rotated into the D_K eigenvector basis (NEW computation)
- Code:
  - NEW: `tier0-computation/order_one_physical_dk.py` (~400 lines: D_F construction from eigenvectors, A_F basis rotation, order-one test for all 9 factor pairs, chirality verification)
  - REUSE: `branching_computation_32dim.py` (J, gamma_F), `branching_computation.py` (A_F generators), `tier1_u2_projection.py` (eigenvectors + quantum numbers)

---

## 6. PHONON-NCG DICTIONARY FINAL UPDATE
- Type: Axiom (classification document with executable criteria)
- Specification:
  Final version of the phonon-NCG dictionary: 17 entries with dual scoring (Rigor 0-3, Quality A-F), explicit pass/fail criteria for upgrading/downgrading each entry, and classification of analogy breaks as fixable vs fundamental.

  **Complete Dictionary (17 entries)**

  | # | NCG/KK Object | Phonon Analog | Rigor | Quality | Pass/Fail for Upgrade |
  |---|---------------|---------------|-------|---------|-----------------------|
  | 1 | Eigenspinor Y_n(h) | Phonon mode | 3 | A | LOCKED. Machine epsilon verified. |
  | 2 | CG coefficient C^k_{nm} | Anharmonic coupling vertex | 2 | B+ | -> 3/A: Compute specific CG vertex from D_K eigenvectors. Verify triple-product = scattering amplitude. |
  | 3 | Jensen deformation s | Anisotropic lattice distortion | 2 | A- | -> 3/A: Verify V_eff(s) behaves as phonon free energy under anisotropic strain. No lattice = permanent gap from A. |
  | 4 | Spectral action Tr(f(D^2/Lambda^2)) | Phonon free energy | 3 | A | LOCKED. Mathematical identity (Feynman, Session G3). |
  | 5 | Gauge field A_mu | Inner fluctuation D->D+A+JAJ^{-1} | 3 | B | -> A: Compute gauge coupling at s_0, compare to measured (Item 3 gauge test). |
  | 6 | Real structure J | Charge conjugation / BdG particle-hole | 3 | B+ | -> A: If Pfaffian shows topological transition (Item 2 Phase D). |
  | 7 | D_F (finite Dirac) | Mode converter / Yukawa | 1 | C+ | -> 2/B: If order-one with physical D_K passes (Item 5). -> 3/A: If Yukawa couplings match measured values. |
  | 8 | KO-dim 6 | Class DIII topological superconductor | 2 | B | -> 3/A: If Pfaffian Z_2 invariant shows physical content (sign change). -> 2/B- if Pfaffian constant AND no dynamical content. |
  | 9 | Order-one condition | Dynamical selection rule | 2 | B- | -> 3/B+: If order-one with physical D_K passes (Item 5). -> 1/C: If physical D_K fails order-one. |
  | 10 | Bell CHSH = 2*sqrt(2) | Non-commutative fiber observables | 0 | N/A | -> 1/C: If Born rule strengthened (Item 2 Phase A). -> 2/B: If CHSH = 2*sqrt(2) derived (Item 2 Phase C). ABSENT until Phase A progress. |
  | 11 | Measurement / collapse | Decoherence from partial trace over K | 0 | N/A | -> 1/C: If concrete projector from A_F (Item 2 Phase B). -> 2/B: If measurement statistics reproduced. ABSENT until Phase B progress. |
  | 12 | Fock space / Fermi statistics | BdG class DIII + real structure J | 1 | C | -> 2/B: If NCG Fock space construction carried through (J -> fermion doubling -> Lambda(H_phys)). KO-dim 6 gives correct signs. |
  | 13 | V_eff minimum s_0 | Equilibrium lattice distortion | 2 | B | -> 3/A: If V_eff minimum exists at natural parameters AND matches Baptista eq 3.87. -> 1/C: If V_eff monotonic at all parameters. |
  | 14 | Gauge coupling splitting | Anisotropic sound velocities | 2 | B | -> 3/A: If g_1/g_2 at s_0 matches measured ~0.55 within 20% (Item 3). -> 1/C: If gauge couplings at s_0 are wildly wrong. |
  | 15 | Z_3 generation mechanism | Zone-boundary mode tripling | 1 | C+ | -> 2/B: If Z_3 gives 3 generations with hierarchy (Item 1 B1-B3 Tier 1 + B4-B7 Tier 2). -> 3/A: If lepton/quark OOM match (Item 1 B6-B7). -> 0/N/A: If B1 fails. |
  | 16 | N(j)^{3/2} mass scaling | Sub-quadratic dispersion | 1 | C | -> 2/B: If phi^{3/2} = 1.8954 appears in eigenvalue ratio at s_0 (Item 4 Table C5). Phonon analog: omega ~ k^{3/2} (anomalous dispersion). |
  | 17 | Finite-T spectral corrections | Thermal phonon occupation | 2 | B+ | -> 3/A: If V_eff(s,T) shows symmetry restoration at high T and Kibble-Zurek mechanism. Implementation is straightforward from existing eigenvalues. |

  **Summary Statistics**:
  - Rigorous identification (score 3): 4/17 (24%) -- modes, spectral action, gauge field, J
  - Mathematical parallel (score 2): 7/17 (41%) -- CG, Jensen, KO-dim, order-one, V_eff, gauge couplings, finite-T
  - Suggestive analogy (score 1): 4/17 (24%) -- D_F, Fock, Z_3, N(j) scaling
  - Absent (score 0): 2/17 (12%) -- Bell, measurement
  - Average quality of scored entries: B (2.8/4). **No contradictions.**

  **ANALOGY BREAKS: FIXABLE VS FUNDAMENTAL**

  **Fixable Breaks (4)**:

  | Break | Current Status | Fix | Timeline | Confidence | Upgrade Criterion |
  |-------|---------------|-----|----------|------------|-------------------|
  | (a) Bell/CHSH | ABSENT (score 0) | Bell roadmap Phases A-C (Item 2) | Months-year | 20-30% | Phase C computation yields S >= 2*sqrt(2) |
  | (b) Measurement/Collapse | ABSENT (score 0) | Concrete projector from A_F operators; decoherence from partial trace over K | Weeks-months | 30-40% | Phase B yields Stern-Gerlach statistics from A_F |
  | (c) Fock space/Fermi statistics | INCOMPLETE (score 1) | NCG construction: J -> fermion doubling -> Lambda(H_phys). KO-dim 6 correct signs. | Weeks | 50-60% | Multi-particle states with correct exchange statistics derived from J |
  | (d) D_F/Yukawa | WEAK (score 1) | Extract D_F from physical D_K via U(2) projection + order-one (Item 5) | Days-weeks | 50-65% | Order-one passes with physical D_K |

  **Potentially Fundamental Breaks (3)**:

  | Break | Assessment | Severity | Upgrade to "proven fundamental" if: | Downgrade to "fixable" if: |
  |-------|-----------|----------|--------------------------------------|---------------------------|
  | (e) No physical lattice | SU(3) is smooth, not discrete. Phonon physics assumes lattice spacing a. Continuum phonon is approximation. | LOW | N/A (conceptual, not mathematical). Mathematics works on smooth manifolds. The phonon interpretation is a GUIDE, not a requirement. | N/A |
  | (f) Bosons vs fermions | Physical phonons are bosons; SM matter is fermionic. BdG class DIII provides fermionic quasiparticles in bosonic medium. | MEDIUM | If NCG Fock space construction PROVES that J-derived fermions cannot reproduce multi-particle entanglement patterns of fundamental fermions. | If NCG Fock space construction SUCCEEDS in reproducing all fermionic statistics from J + KO-dim 6. |
  | (g) K-locality (global spectral coupling) | Spectral action couples ALL (p,q) sectors globally through Tr(f(D^2)). No analog of "local phonon interaction." | MEDIUM-HIGH | If Bell computation (Item 2 Phase C) PROVES that global spectral coupling gives S < 2*sqrt(2). This would mean the framework is subquantum due to locality structure of K. | If global coupling EXPLAINS entanglement (two particles correlated because spectral action couples their eigenvalues). Bell Phase C is the test. |

  **Key Insight (from Round 2c convergence)**: Breaks (e)-(g) are all ultimately TESTED by the Bell computation (Phase C). If CHSH = 2*sqrt(2) emerges from the framework despite smooth K, bosonic substrate, and global coupling, then all three "potentially fundamental" breaks are resolved simultaneously. If CHSH < 2*sqrt(2), at least one is fatal. The Bell computation is the JOINT discriminator for all three breaks.

- Pass/Fail:
  | Criterion | Condition | Verdict |
  |-----------|-----------|---------|
  | Average score >= B | Mean rigor >= 2.0, mean quality >= B (2.5/4) | Dictionary is STRONG |
  | No new contradictions | No entry requires downgrade from computation results | CONSISTENT |
  | >= 2 entries upgrade | At least 2 entries move from score 1->2 or 2->3 | PROGRESSING |
  | Bell remains absent after 1 year | Score 0 on entries 10-11 persists | STRUCTURAL GAP unresolved |
  | Break (g) proven fundamental | CHSH < 2*sqrt(2) from framework | K-locality CLOSES phonon analogy for QM |

- Feasibility: GREEN (classification document; upgrades depend on other items)
- Timeline: Document: 1 day. Upgrades: contingent on Items 1-5 results.
- Owner: qa-theorist (primary author, phonon interpretation) + all agents (entry-specific input)
- Decisiveness: 6/10 (meta-document tracking program health; individual entries have their own decisiveness via linked items)
- Dependencies:
  - Item 1 (Z_3): upgrades entries 15, 16
  - Item 2 (Bell): upgrades entries 10, 11; classifies breaks (e)-(g)
  - Item 3 (G-decomposition): upgrades entries 5, 14
  - Item 4 (Paasch): upgrades entry 16
  - Item 5 (Order-one): upgrades entries 7, 9
  - Round 3a V_eff: upgrades entries 3, 13, 17
  - Pfaffian (Item 2 Phase D): upgrades entries 6, 8
- Code:
  - No new code. This is a DOCUMENT maintained as `sessions/phonon-ncg-dictionary-final.md`.
  - Each entry links to the relevant computation file and pass/fail criterion.

---

## DEPENDENCY GRAPH

```
[EXISTING] tier1_dirac_spectrum.py + branching_computation*.py
    |
    v
[Item 1] Z_3 Test Procedure
    |  Tier 1: 2 days        Tier 2: +1 week (spinor transport)
    |         |         |
    v         v         v
[Item 4]  [Item 3]  [Item 5]
Paasch    G-decomp  Order-one
(hours)   (1 day)   (1 week)
    |         |         |
    v         v         v
[Item 6: Dictionary upgrades from all items]
                        |
                        v
                  [Item 2 Phase D]
                  Pfaffian (hours)
                        |
                        v
              [Item 2 Phases A-C]
              Bell (weeks-months)
```

**Critical path**: Item 1 Tier 1 -> Item 5 -> Item 2 Phase D (Pfaffian). Everything else runs in parallel.

**Pfaffian Override**: If Pfaffian sign changes at ANY point, it supersedes all other priorities (endorsed by all 4 Giants).

---

## PARALLEL EXECUTION PLAN

| Days 1-2 | Track A: V_eff (Round 3a) | Track B: Z_3 + U(2) (Item 1 Tier 1) |
|----------|--------------------------|--------------------------------------|
| Day 3 | Gauge coupling test (Item 3) | Paasch tests Tier 1 (Item 4) |
| Day 3 | phi^{3/2} = **1.8954** test (Item 4 C5) | f_M check (Item 4 supplement) |
| Days 4-5 | Order-one prerequisites (Item 5) | Pfaffian prerequisites (Item 2 Phase D) |
| Days 4-5 | G-decomposition document (Item 3) | Dictionary update (Item 6) |
| Days 6-7 | Order-one computation (Item 5) | Pfaffian computation (Item 2 Phase D) |
| Week 2 | Tier 2 spinor transport (Item 1) | Tier 2 generation tests (Item 4 Table B) |

**Day 3 is THE critical day** (Einstein-Feynman + Hawking-Sagan convergence): gauge coupling check is the headline Level 3 test. phi^{3/2} is the headline phi test.

---

## PROBABILITY UPDATE

No change from Round 2d: **38-60%** (all-Giant range). Items 1-6 above are the specifications that will MOVE this number. The coming week's computations are the most consequential since the Tier 1 Dirac spectrum.

**If all items yield positive results**: 65-85% (success ceiling).
**If all items yield negative results**: 25-35% (failure floor).

**DOF inversion caveat** (Round 3b): 45 bosonic DOF vs 16 fermionic in spectral action weakens V_eff stabilization. P(no minimum) = 35-40%. Backup s_0 = 0.30 from gauge coupling if V_eff monotonic.

---

*Round 3b theoretical specifications FINAL. Six items, all with executable pass/fail criteria, explicit dependencies, and code specifications. 11 Tier 1 tests + 8 Tier 2 deferred + 4 Paasch-internal. The critical path runs through Z_3 Tier 1 (Item 1) -> Order-one (Item 5) -> Pfaffian (Item 2 Phase D). The phonon-NCG dictionary tracks 17 entries at average grade B with zero contradictions, 4 fixable breaks, and 3 potentially fundamental breaks all jointly discriminated by the Bell computation. Key correction: phi^{3/2} = 1.8954 (verified).*
