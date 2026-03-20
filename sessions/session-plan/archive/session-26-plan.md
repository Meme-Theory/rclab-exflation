# Session 26 Plan Scrub Report

**Date**: 2026-02-25
**Author**: Baptista-Spacetime-Analyst
**Document Under Review**: `artifacts/session-26-plan.md` (2026-02-23)
**Method**: Cross-reference every item against computational history (Sessions 17-26), collab source documents, proven/closed mechanism registry, and Priority 1 results (`sessions/session-26/session-26-priority-1.md`)

---

## 0. Summary

The plan has 10 priorities, 10 quality gates, 10 piggyback outputs, 12 investigation items, 3 structural theorems, and a physical units bundle. After scrub:

- **KEEP**: 3 priorities, 3 quality gates, 4 piggyback outputs, 3 investigation items
- **CUT**: 4 priorities, 5 quality gates, 4 piggyback outputs, 7 investigation items, 2 structural theorems
- **DEMOTE**: 3 priorities, 2 quality gates, 2 piggyback outputs, 2 investigation items, 1 structural theorem

The plan should collapse from 10 priorities to 3. The rest is either already resolved by Priority 1, testing closed mechanisms, structurally impossible given known results, or attributed to agent proposals that do not exist in the source documents.

---

## 1. KEEP

### Priority 1: Multi-Mode BCS Gap Equation
**Status**: ALREADY COMPUTED (Session 26, `s26_multimode_bcs.py`/`.npz`). Results in `sessions/session-26/session-26-priority-1.md`. Condensation confirmed at mu > 0.875 * lambda_min. No tau lock in static singlet profile. [V,J] != 0 discovery.

**What remains**: Multi-sector BCS (Priority 1b in Baptista evaluation, Section 7.1). The (0,0) singlet is computed; the (1,0), (0,1), (1,1), (2,0), (0,2) sectors are not. This is the single most important remaining computation. The framework needs the TOTAL condensation energy across sectors to assess tau-locking.

**Keep because**: The decisive open question. Different sectors have different Kosmann couplings, different eigenvalue structures, and potentially different F_cond(tau) profiles.

### Priority 7: Cooling Trajectory + Frequency Profile (DEMOTED from P7 to P2)
**Status**: Uncomputed. Depends on P1 sector data.

**Keep because**: The cooling trajectory (coupled system: Delta, tau, mu, H) is the framework's actual locking mechanism per the Baptista evaluation (Section 2.1). The static F_cond profile at mu = lambda_min is not the answer; the dynamical trajectory is. The Bogoliubov coefficients from the transition ARE the terminal output.

**Caveat**: Must be preceded by multi-sector BCS. Running this on singlet-only data would produce garbage.

### Priority 6: Higher-Order Seeley-DeWitt (a_6)
**Status**: Uncomputed. Uses existing Riemann tensor data (`r20a_riemann_tensor.npz`).

**Keep because**: The B-1 minimum at rho = 0.000510 uses V_spec truncated at a_4. Multiple Session 25 reviewers (Connes, Berry, Hawking) warned that the Seeley-DeWitt series may not converge at Lambda = 5.72, and a_4/a_2 = 1000:1 at tau = 0 signals poor convergence. a_6 could either stabilize or destroy the B-1 minimum. This is a genuine unknown. 2-4 hours of compute with existing data.

**Caveat**: Einstein and Feynman both rated this low priority in Session 25 (the exact eigenvalue sum bypasses the truncation). But with the B-1 bridge now the only remaining V_spec structure, testing its robustness against a_6 is warranted.

### Quality Gates to Keep (3)

| Gate | Reason to Keep |
|:-----|:---------------|
| **Kernel eigenvalue** (Master V) | The decisive BCS gate. Already passed in singlet (M_max = 6.3-9.7). Must be checked per-sector in multi-sector BCS. |
| **Spectral pairing** (Dirac S-2) | Zero-cost numerical integrity check. Already passed at machine epsilon in P1. Keep for new sectors. |
| **Confinement threshold** (Baptista S.4) | g*Delta^2 = 0.01 in singlet. Genuinely concerning. Must evaluate in higher sectors. The 0.109 threshold has caveats (B-1 well geometry is approximate) but the weakness of coupling IS framework-level. |

### Piggyback Outputs to Keep (4)

| Output | Reason to Keep |
|:-------|:---------------|
| **Saxion mass** (Tesla T-2) | m^2_saxion = d^2 V_eff/d tau^2 at the locked point. If the coupled system produces a lock, this is the immediate test of stability. Zero cost once lock is found. |
| **Q_tau of lock** (Tesla T-3) | If lock exists, Q < 1 means smeared. Genuine diagnostic. Zero cost. |
| **Solution uniqueness** (SP-7) | Number of fixed points matters. If multi-sector BCS + cooling produces a lock, need to know if it is unique. |
| **Jacobian stability** (Baptista B-7) | Eigenvalues of coupled-system Jacobian at any found fixed point. Whether the lock is an attractor. Already checked for singlet (all eigenvalues have negative real part); must recheck for multi-sector. |

### Investigation Items to Keep (3)

| ID | Item | Reason |
|:---|:-----|:-------|
| I-9 | Paper 18 modified Lie derivative L-tilde vs L | The Baptista evaluation (Section 5.3) identifies this as a genuine open computation that could change coupling strength systematically. If L-tilde gives stronger pairing than L, g*Delta^2 could increase. Moderate cost, existing data. |
| I-4 | DNP growth rate vs. condensation rate at tau_0 | The tau_0 = 0.15 point lies inside the DNP-unstable region (Session 22a SP-5, tau in [0, 0.285]). Whether condensation rate exceeds DNP growth rate is a genuine stability question. |
| I-3 | Correct Gamow tunneling calculation | The B-1 barrier is Delta V = 0.0003 with zero-point energy 0.0548 (183x excess). The bare well has no localized state. If multi-sector BCS deepens the well, the tunneling rate through the (possibly deeper) barrier matters. Low cost. |

---

## 2. CUT

### Priority 2: Geodesic Completeness of (tau, Delta) Space
**CUT. The tau lock does not exist in the static singlet profile.** The Priority 1 results show F_cond has a local MAXIMUM near tau = 0.20, not a minimum. Constructing the mini-superspace metric and checking geodesic completeness tests a scenario (static BCS locking at tau_0) that does not materialize. S-P's geodesic completeness check was motivated by the assumption that the condensate censors the decompactification singularity. The condensation energy reinforces the preference for tau = 0, not for tau_0 = 0.15.

If multi-sector BCS changes this picture (producing a tau lock), geodesic completeness becomes relevant. But spending 1 hour on it now, when the prerequisite (a lock to censor) does not exist, is premature.

### Priority 3: Spectral Bianchi Identity at Finite mu (standalone)
**CUT. Redundant with P1 quality gate.** The plan itself states (line 73): "Also built into Priority 1 as a quality gate, but worth running independently as a standalone verification." This is the definition of redundancy. The gate version (Einstein E-2) is adequate. Running it as a standalone priority wastes an agent's time producing a document that says the same thing.

### Priority 4: GSL Balance Sheet
**CUT. The prerequisite does not exist.** The Hawking evaluation (Section 1.3) explicitly states: "The GSL diagnostic is moot because the condensation energy does not have a minimum at tau_0 in the first place. I was analyzing the entropy cost of a locking mechanism that does not exist." Hawking himself closed this. The "revised delocalization entropy" enhancement (HT-3) is analyzing a scenario the computation disproved.

If multi-sector BCS produces a lock, the GSL becomes relevant. But now, with no lock, this is a computation about nothing.

### Priority 5: Resonant Cavity Self-Consistency
**CUT. Depends on Priority 1 results that show the wrong picture.** The transfer function T(tau) = Delta_out/Delta_in requires a tau-dependent gain profile with |T| = 1 at some tau_0. The Priority 1 results show the gain is strongest at tau = 0 and weakest near tau = 0.20. The cavity "self-consistency" would select tau = 0 (round metric), which is the trivial solution.

Tesla's resonant cavity interpretation is elegant but the gain profile from the singlet BCS does not support it. Running this produces a 50-line script that confirms |T| > 1 at tau = 0 and |T| < 1 at tau_0. Not informative.

### Priority 8: Multi-Dimensional Stability
**CUT. Premature -- no minimum to test.** The plan says this checks whether "1D minimum is a saddle" in the 8D space. Which minimum? The B-1 minimum at rho = 0.000510 (from Seeley-DeWitt truncation at a_4, untested against a_6)? The BCS F_cond profile has no minimum at any tau_0 in the singlet. The "Euclidean bounce mode" enhancement (Hawking HT-6) tests whether d^2 V/d phi^2 < 0 "at the B-1 point" -- but the B-1 point is an a_4-truncated result whose robustness against a_6 is unknown (Priority 6).

This computation requires new eigenvalue data (high cost) and tests a minimum whose existence is unconfirmed. Wait for Priority 6 (does B-1 survive a_6?) and multi-sector BCS (does total F_cond have a minimum?) before investing in 8D stability.

### Priority 9: NEC Audit Along Cooling Trajectory
**CUT. Depends on Priority 7 results that do not exist.** The plan says "check R_{mu nu} k^mu k^nu >= 0 for all null k at each tau." This requires the cooling trajectory, which requires multi-sector BCS, which is the actual next computation. Running a NEC audit on a trajectory that has not been computed is not possible.

### Priority 10: No-Boundary Constraint on mu
**CUT. Hawking closed this himself.** The Hawking evaluation (Section 1.2) states: "The no-boundary proposal with the BCS condensate does not select a non-trivial tau_0 -- it cements the round metric as the preferred state." The "coupled zero-parameter derivation" (HT-2) was Hawking's proposal. Hawking's own evaluation of the Priority 1 results concludes: "The zero-parameter dream is closed for this mechanism."

The framework probability at 5-8% does not justify spending moderate theoretical effort on a mechanism its own proponent has retracted.

### Quality Gates to Cut (5)

| Gate | Reason to Cut |
|:-----|:--------------|
| **J-even projection** (Dirac S-1) | **FALSIFIED BY P1.** [V,J] != 0 at 14-30% level. The condensate has nearly equal J-even and J-odd content (ratio 0.94-0.99). Dirac predicted J-even; Paper 17 eq 1.6 predicts J-odd. The "BUG" threshold |Delta_-/Delta_+| > 10^{-12} would fire at every iteration -- because it is not a bug, it is the physics. Running this gate as written would produce a wall of false alarms. |
| **CPT gate** (Dirac S-3) | **FALSIFIED BY P1.** Delta(+lambda) >> Delta(-lambda) by 63x. m(particle) != m(antiparticle) in the gap function. This is a structural consequence of [V,J] != 0 (Paper 17 chirality mechanism). The gate as written would fire and incorrectly flag a geometric discovery as a bug. |
| **KO-dim 6 verify** (Dirac Q-1) | **ALREADY PROVEN.** KO-dim = 6 is machine-epsilon verified (Sessions 7-8, permanent structural result). J^2 = +1, JD_K = D_K J, J gamma = -gamma J are exact algebraic identities independent of mu. [J, D_K - mu] = [J, D_K] - mu[J,1] = 0 identically. This gate tests a result proved 19 sessions ago. Reverifying it is theater. |
| **Barrier threshold** (Tesla T-A.5) | **NO BARRIER EXISTS IN SINGLET.** g*Delta^2 = 0.01, which is 5000x below threshold. But more fundamentally, the F_cond profile has no minimum to form a barrier around. The barrier threshold is a constraint on the B-1 well, which has Delta V = 0.0003 -- far below the zero-point energy (183x excess). The condensate does not enhance the barrier; it inverts the landscape. This gate tests a scenario that the Priority 1 computation disproved. |
| **Trans-Planckian** (Hawking H-5) | **ALREADY CONFIRMED PASS.** The Hawking evaluation (Section 1.6) states: "The BCS computation converges at all tau values, and the self-consistent solution is regulator-independent." Delta acts as its own regulator. This gate already passed. Rechecking it in multi-sector BCS is reasonable as a sanity check but not as a named gate. |

### Piggyback Outputs to Cut (4)

| Output | Reason to Cut |
|:-------|:--------------|
| **Delta^4 coefficient** (Dirac D-7) | **ALREADY COMPUTED.** b = +0.41 (positive, second-order transition). This was a P1 piggyback that already ran. The Hawking evaluation Section 1.1 discusses it at length. Listing it again in the plan as a future output is a duplication. |
| **sin^2 theta_W benchmark** (Dirac D-11) | **NOT A GATE -- it is a downstream prediction.** The value 0.354 at tau_0 = 0.15 is already known from Session 25. It overshoots SM by 53%. No computation in P1-P10 changes this number. Running corrections (gauge coupling running) is a paper-preparation task, not a session priority. |
| **Hawking-Page map** (Hawking H-3) | **FALSIFIED.** The Hawking-Page analogy predicted first-order transition. The transition is second-order (b = +0.41). Hawking himself (evaluation Section 1.1) explains in detail why the analogy fails: "There is no analog of the topological change between thermal AdS and the black hole." Computing Z = Z_normal + Z_condensed when the transition is continuous produces a smooth crossover, not a first-order jump. The thermodynamics Hawking proposed does not apply. |
| **Path integral measure** (Hawking HT-5) | **MOOT.** HT-5 was about the Bekenstein bound on barrier height. The Hawking evaluation (Section 1.5) explicitly states: "This is a constraint on a minimum that does not exist." The path integral measure (BCS stiffness) is a real quantity, but it constrains a saddle-point approximation to a Euclidean integral whose saddle (per Hawking's own evaluation) is at tau = 0, not tau_0. Without a non-trivial saddle, the measure computation has nothing to stabilize. |

### Investigation Items to Cut (7)

| ID | Item | Reason to Cut |
|:---|:-----|:--------------|
| I-1 | Phononic crystal bandgap protection | Tesla speculation. No computation, no derivation. The bandgap analogy requires a periodic structure in the BCS spectrum that has not been identified. Zero probability of changing framework verdict. |
| I-2 | Loop gain |G| of recycling oscillator | Redundant with Priority 5 (which is itself cut). Tesla's resonance interpretation, while interesting, produced no computation. |
| I-5 | Actual CDL/Gamow bounce ODE for B-1 | The B-1 well has Delta V = 0.0003 with zero-point energy 0.0548 (183x excess). The Baptista evaluation S.2 and Hawking HT-1 both confirm: "No Euclidean thermal state. No localized ground state." The bare well is physically empty. Running the bounce ODE on an empty well produces B << 1 (transparent barrier), which we already know. |
| I-6 | Petrov type at tau_0 = 0.15 | Computed in Session 25 (SP-4): Type D at tau = 0, algebraically general at all tau > 0. The transition is discrete at tau = 0 exactly. Repeating at tau = 0.15 adds no information beyond "algebraically general," which is already the established result for all tau > 0. |
| I-7 | Bekenstein bound on minimum barrier height | Hawking HT-5, explicitly retracted by Hawking in his own evaluation (Section 1.5): "This is a constraint on a minimum that does not exist." |
| I-10 | Spectral equivalence principle test | Einstein E-4 proposed a gedankenexperiment comparing round SU(3) + gauge field background vs. deformed SU(3). This is a "Med-High" cost theoretical investigation that would test a conceptual analogy, not a framework prediction. At 5-8% probability and with the decisive multi-sector BCS uncomputed, this is pure luxury. |
| I-11 | Internal islands at finite density | Hawking H-6. Speculative theoretical physics (island formula on product spacetime with condensate). "High" cost. Zero connection to any computation in the pipeline. This is Hawking's research program, not the framework's next step. |

### Structural Theorems to Cut (2)

| Theorem | Reason to Cut |
|:--------|:--------------|
| **183x zero-point excess** (Baptista S.2) | Already verified and extensively discussed (master-collab S.2, Hawking HT-1). This is a known result, not something to "verify alongside computation." Including it as a "structural theorem to verify" implies it is unverified, which is false. |
| **ALPHA-g prediction** (Dirac D-4) | The prediction "a_g = g exactly" assumes a J-even condensate. The P1 results show the condensate is NOT J-even ([V,J] != 0, J-odd/J-even = 0.96). The prediction's premise is falsified. Pre-registering for ALPHA-g based on a J-even condensate that does not exist is not science -- it is a prediction from a model that the computation disproved. |

---

## 3. DEMOTE

### Priority 2 (Geodesic Completeness) --> Investigation bucket
**Demote because**: The computation is well-defined (1 hour, existing data) but its premise (condensate censors the decompactification singularity) is not established. Becomes actionable IF multi-sector BCS produces a tau lock. Mark as "contingent on P1b results."

### Priority 8 (Multi-Dimensional Stability) --> Investigation bucket
**Demote because**: High cost, requires new eigenvalue computations, and tests a minimum (B-1) whose robustness is unknown. Becomes actionable IF Priority 6 confirms B-1 survives a_6 AND multi-sector BCS changes the landscape. Two contingencies deep.

### Priority 9 (NEC Audit) --> Investigation bucket
**Demote because**: Requires the cooling trajectory (Priority 7). Cannot be run independently. Becomes a check after P7 produces results.

### Quality Gates to Demote (2)

| Gate | Demote to |
|:-----|:----------|
| **Spectral Bianchi** (Einstein E-2) | Keep as a P1b quality gate (zero-cost check per sector), but remove as standalone Priority 3. Already built into P1 solver. |
| **Trans-Planckian** (Hawking H-5) | Keep as a sanity check in multi-sector BCS. Remove as a named gate. Already passed in singlet. |

### Piggyback Outputs to Demote (2)

| Output | Demote to |
|:-------|:----------|
| **Clock constraint** (Dirac D-10) | Downstream of tau-locking. If the coupled system locks tau, then check delta-tau oscillation against ALPHA 2 ppt. Not computable until a lock exists. Move to "contingent on P7 results." |
| **J-decomp of coupling** (Dirac D-8) | Already computed (Priority 1, Section 3.4): [V,J] != 0 at 14-30% level. The J-decomposition of the kernel at intermediate mu is a refinement, not a new gate. Move to investigation bucket. |

### Investigation Items to Demote (2)

| ID | Item | Demote to |
|:---|:-----|:----------|
| I-8 | Coupled (tau, TT-modes) stability | Moderate cost. Worth doing IF a lock is found. Contingent on multi-sector BCS + cooling trajectory. Move to "post-P7 checklist." |
| I-12 | First-order condition at finite mu | Low-Med cost. Hawking H-7 proposed this. Conceptually relevant (does mu break the spectral triple's first-order condition?). But at 5-8% probability and with multi-sector BCS as the bottleneck, this is not urgent. Keep in investigation bucket but mark as "theoretically interesting, not blocking." |

### Structural Theorem to Demote (1)

| Theorem | Demote to |
|:--------|:----------|
| **Chirality-breaking** (Dirac D-9 / Master III.6) | The theorem states: "Nonzero J-even condensate CANNOT be chirality-definite." But the P1 results show the condensate is NOT J-even. The theorem's hypothesis (J-even condensate) is not satisfied. The chirality-breaking still occurs (the condensate breaks chirality through [V,J] != 0, which is a STRONGER result than the theorem), but the theorem as stated does not apply to the actual condensate. Demote to "historical note: the mechanism is correct but the pathway is different than predicted." |

---

## 4. HALLUCINATED SOURCE LABELS

The following source labels in the plan appear ONLY in `artifacts/session-26-plan.md` and do not exist in any collab document, meeting minute, or agent output from Sessions 17-26:

| Label | Appears in Plan as | Actual Source |
|:------|:-------------------|:-------------|
| **Dirac D-4** | ALPHA-g prediction | No "D-4" in any Dirac collab. The positronium BEC connection is labeled "Dirac S-6" in the master-collab (line 267), but the ALPHA-g prediction with specific a_g = g claim does not appear in the Dirac collab. |
| **Dirac D-5** | Sakharov-3 tracking | No "D-5" in any Dirac collab. Dirac discusses Sakharov conditions generically but never proposes a specific "D-5" computation. |
| **Dirac D-7** | Delta^4 Landau coefficient | No "D-7" in any Dirac collab. This is a standard BCS computation; attributing it to a specific Dirac proposal is fabricated. |
| **Dirac D-8** | J-decomposition of coupling | No "D-8" in any Dirac collab. Dirac discusses J-decomposition in generic terms (master-collab Section III.2) but never assigns it a numbered label. |
| **Dirac D-9** | Chirality-breaking theorem | Appears as "Master III.6" in the master-collab synthesis. The "Dirac D-9" label is fabricated; the correct attribution is "master-collab Section III.6." |
| **Dirac D-10** | Clock constraint | No "D-10" in any Dirac collab. The clock constraint is from Session 22d (E-3), attributed to Einstein's work, not Dirac's. |
| **Dirac D-11** | sin^2 theta_W benchmark | No "D-11" in any Dirac collab. The value 0.354 comes from the master-collab Theme 5 discussion. |
| **Baptista B-3** | Gamow tunneling | No "B-3" in any Baptista document. The CDL vs. Gamow distinction is from Hawking HT-2. |
| **Baptista B-4** | Two-field from Paper 15 | No "B-4" in any Baptista document. The two-field potential (Paper 15, eq 3.80-3.81) is referenced in the Baptista synthesis (S.5) but never given a "B-4" label. |
| **Baptista B-5** | Paper 18 modified Lie derivative | No "B-5" in any Baptista document. Paper 18 is discussed in the Baptista evaluation (Section 5.3) but never given a numbered label. |
| **Baptista B-6** | All thresholds in GeV | No "B-6" in any Baptista document. Unit conversion is a generic task, not an agent proposal. |
| **Baptista B-7** | Jacobian stability | No "B-7" in any Baptista document. Jacobian stability is a standard dynamical systems check, not a specific agent proposal. |
| **SP-6** | Petrov type at tau_0 | No "SP-6" in any S-P collab. Petrov type is from Session 25 SP-4. |
| **SP-7** | Solution uniqueness | No "SP-7" in any S-P collab. Solution uniqueness is discussed generically in the S-P collab but never assigned a numbered label. |
| **SP-8** | DNP growth rate vs. condensation | No "SP-8" in any S-P collab. The DNP instability is Session 22a SP-5; the comparison with condensation rate is a generic suggestion. |
| **SP-9** | CDL/Gamow bounce ODE | No "SP-9" in any S-P collab. This overlaps Hawking HT-2. |
| **SP-10** | Coupled tau + TT stability | No "SP-10" in any S-P collab. |
| **SP-11** | False vacuum energy in eV^4 | No "SP-11" in any S-P collab. Unit conversion. |
| **SP-12** | Penrose inequality | No "SP-12" in any S-P collab. The Penrose inequality is discussed generically in the S-P collab but never assigned "SP-12." |
| **Hawking H-3** (piggyback) | Hawking-Page map | The Hawking collab does discuss the Hawking-Page analogy (lines 112-126) but the numbered label "H-3" as a piggyback output is fabricated. Hawking's addendum labels are "HT-1" through "HT-13." |
| **Hawking H-4** (P7 diagnostic) | Bogoliubov coefficients | Hawking discusses Bogoliubov coefficients (lines 130-142 of the collab) but never assigns them "H-4" as a diagnostic label. |
| **Hawking HT-5** (piggyback) | Path integral measure | In the plan this appears as "Hawking HT-5: BCS stiffness." The actual HT-5 in the master-collab is "Information-Theoretic Bound on Modulus Stabilization" (Bekenstein bound), not path integral measure. The plan reassigns the label to a different computation. |
| **Tesla T-2, T-3, T-4** (various) | Saxion mass, Q_tau, Sonic horizon | Tesla's collab uses "Suggestion 1-5" and "T-A.1" through "T-A.12" as labels. "T-2", "T-3", "T-4" do not appear in the Tesla collab. These are fabricated shorthand. |

**Pattern**: The plan systematically assigns "Agent X-N" labels to generic computations and standard BCS outputs, creating the appearance that each item was proposed by a specific agent when in fact most are either (a) standard physics that any competent physicist would include, (b) derived from a different agent than attributed, or (c) not traceable to any specific agent proposal. This inflates the appearance of collaborative consensus while obscuring which items actually have agent backing.

---

## 5. REVISED PLAN SKELETON

### Priority 1: Multi-Sector BCS Gap Equation
**Cost**: Hours per sector | **Data**: Existing .npz files, Session 23a Kosmann matrices
**Action**: Extend `s26_multimode_bcs.py` to (1,0), (0,1), (1,1), (2,0), (0,2) sectors. For each sector, solve the matrix BCS gap equation at mu/lambda_min in [0, 5]. Extract:
- Linearized kernel eigenvalues (does M_max > 1?)
- Self-consistent Delta profile
- F_cond(tau) per sector
- TOTAL F_cond(tau) = sum over all computed sectors
- Kosmann coupling strength g*Delta^2 per sector

**Closure**: If TOTAL F_cond(tau) has no minimum at any tau_0 in (0, 0.5) for any physical mu, static locking is closed across all sectors. Combined with singlet result, this would reduce framework probability to <3%.

**Quality gates** (built into solver, zero cost):
1. Kernel eigenvalue M_max per sector (the decisive gate)
2. Spectral pairing (lambda <-> -lambda symmetry check, machine epsilon)
3. Confinement threshold: total g*Delta^2 across sectors vs. 0.109

### Priority 2: Cooling Trajectory + Frequency Profile
**Cost**: Days | **Depends on**: Priority 1 (multi-sector phase diagram)
**Action**: Solve coupled 4-variable system (Delta, tau, mu, H). Track whether the system locks tau before mu drops below lambda_min. Extract Bogoliubov coefficients |beta_k|^2 at the transition.

**Closure**: If mu drops below mu_c (0.875-0.925 * lambda_min) before condensation can lock tau, the transient condensate evaporates and no lock is possible.

**Diagnostics** (from existing agent proposals with verified provenance):
- Saxion mass: m^2_saxion = d^2 V_eff/d tau^2 at any found lock point. (Tesla Suggestion 2)
- Q_tau of lock: FWHM of the lock. (Tesla Suggestion 3)
- Landau-Zener transition probability along trajectory. (Einstein E-5)

### Priority 3: Higher-Order Seeley-DeWitt (a_6)
**Cost**: 2-4 hours | **Data**: `r20a_riemann_tensor.npz`
**Action**: Compute a_6(tau) at 21 tau values. Evaluate V_spec^(6) = -c_2 R_K + c_4 a_4 + c_6 a_6. Check whether B-1 minimum persists.

**Closure**: If a_6 destroys the B-1 minimum, the only known V_spec structure vanishes. The framework loses its anchor point.

### Investigation Bucket (post-priority, contingent)

| Item | Contingent on | Cost |
|:-----|:-------------|:-----|
| Paper 18 L-tilde vs L coupling | Independent | Moderate |
| DNP growth rate vs. condensation rate | P1 (need Delta at tau_0) | Low |
| Gamow tunneling with deepened well | P1 (need total well depth) | Low |
| Geodesic completeness of (tau, Delta) space | P1 + P2 (need a lock) | 1 hour |
| Multi-dimensional stability (8D) | P3 (need B-1 survival) + P1 | High |
| NEC audit along trajectory | P2 (need trajectory) | Medium |
| First-order condition at finite mu | Independent (theoretical) | Low-Med |
| Physical units bundle | P1 (need Delta values) | Zero |

### What Is Gone

Priorities 2-5, 8-10 of the original plan are either cut or demoted to investigation. The 10-quality-gate apparatus is reduced to 3 real gates, with the rest either falsified (J-even, CPT, barrier), already passed (KO-dim 6, trans-Planckian), or redundant (Spectral Bianchi standalone). The 10 piggyback outputs are reduced to 4, with the rest already computed (Delta^4), moot (Hawking-Page, path integral measure, clock constraint without lock), or based on falsified premises (ALPHA-g from J-even condensate).

The 3 structural theorems are reduced to 0 as standalone items: 183x excess is already verified, chirality-breaking theorem's hypothesis is falsified by P1, and ALPHA-g prediction assumes J-even condensate that does not exist.

---

## 6. Closing Assessment

The Session 26 plan was written BEFORE the Priority 1 computation ran. Many of its items were reasonable pre-registrations at that time. But the P1 results -- particularly the [V,J] != 0 discovery, the F_cond profile peaking at tau = 0, and the weak coupling g*Delta^2 = 0.01 -- invalidated a large fraction of the plan's structure.

The plan was not updated after P1 ran. It is a pre-computation document being treated as a post-computation agenda. This scrub removes the closed weight so that the actual next computation (multi-sector BCS) is not buried under 7 priorities and 15 gates that test scenarios the P1 results already resolved.

The hallucinated source labels are a separate concern. They do not affect the physics but they create false provenance: items attributed to "Dirac D-7" or "SP-12" carry an authority they do not earn. Future plans should cite the actual source document and section (e.g., "master-collab Section III.6" or "Tesla Suggestion 2"), not fabricated agent-number labels.

---

*Baptista-Spacetime-Analyst, 2026-02-25.*
*Cross-referenced against: Priority 1 results (`sessions/session-26/session-26-priority-1.md`), Baptista evaluation (`sessions/session-26/session-26-priority-1-baptista-eval.md`), Hawking evaluation (`sessions/session-26/session-26-priority-1-hawking-eval.md`), Master collab + addenda (`sessions/framework/framework-mechanism-discussion-master-collab.md`), Tesla collab (`sessions/framework/framework-mechanism-discussion-tesla-collab.md`), Einstein collab (`sessions/framework/framework-mechanism-discussion-einstein-collab.md`), Dirac collab (`sessions/framework/framework-mechanism-discussion-dirac-collab.md`), S-P collab (`sessions/framework/framework-mechanism-discussion-sp-collab.md`), Hawking collab (`sessions/framework/framework-mechanism-discussion-hawking-collab.md`).*
