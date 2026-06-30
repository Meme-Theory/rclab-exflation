# Seed file — sessions/archive/session-86/session-86-w5a-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w5a-workingpaper.md` (180 lines read in full)

## Candidates

### Candidate 1 — Path-(c) anchor reassessment after DOUBLE-DOUBLE FAIL

**What it would do**: Adjudicate the actual state of the gen-physicist 9A §4.5a 2A SECTOR split now that BOTH legs have failed. The W5a synthesis cites plan §11's DOUBLE FAIL row ("SECTOR-2 becomes the only path-(c) anchor") on the assumption SECTOR-2 still anchors. The orchestrator review (line 143 of WP) explicitly flags that SECTOR-2 ALSO FAILed in the same batch (`S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT: FAIL` at line 108 of `s86_gate_verdicts.txt`, max_pair_ratio=0.924, max_pair_abs=0.146). Both anchors have collapsed. The workshop pins (a) what path-(c) of the gen-physicist 9A taxonomy still has live anchors, (b) whether BRANCH-IV (W4 P4) at xi_E_GGE_inv=13.6425 is structurally consistent with EITHER SR-LO or Mellin-kernel anchorings, (c) whether path-(c) collapses entirely back to path-(a) (zeta-normalization, S82 W1-2 Branch-A) or path-(b), and (d) what the effective hierarchy of substrate→A_s/n_s prediction routes is post-S86.

**Why it's worthwhile**: This is the single most consequential structural question raised by W5a. The orchestrator review explicitly defers it as "a `/rclab-investigate --session 86` deliverable" rather than a per-wave synthesis claim — but the reorganization can be addressed at workshop scope before the cross-session investigate. The W5a synthesis (line 147) declares "SECTOR-1 corridor closed, SECTOR-2 sole anchor" — which is **factually wrong as of the actual verdict file** because SECTOR-2 is also FAILed. Letting that incorrect framing propagate into S87 carry-forward planning would compound the error. Cross-references: WP §W5a-1 (plan §11 mapping); s86_gate_verdicts.txt line 108 (SECTOR-2 FAIL), lines 114+116 (SECTOR-1 PIVOT55+PIVOT312 FAIL), lines 110+112 (BRANCH-IV FAIL→PASS re-run pattern).

**Type**: 3-agent workshop

**Suggested agents**: gen-physicist, lizzi, transit-dynamics-theorist

**Rounds**: 3 (genuine ledger-dissonance: R1 each agent independently re-maps path-(c) status and proposes successor anchor; R2 each responds to others' maps; R3 converge to a single canonical path-(c) reorganization). The DOUBLE FAIL crosses two specialists' domains (SR-LO ODE vs Mellin-kernel K-invariant) — neither agent alone can adjudicate the joint collapse.

**Context the workshop will need**: (a) `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55: FAIL value=1.435284` and `S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT312: FAIL value=3.297605` (lines 114+116 of s86_gate_verdicts.txt); (b) `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT: FAIL value='max_pair_ratio=9.240439e-01;max_pair_abs=1.460926e-01;atlas=A_5;deviant=None'` (line 108); (c) `S86-BRANCH-IV-FORMULATION-COMMIT` shows FAIL→PASS pattern (lines 110+112) at xi_E_GGE_inv=13.642473425595973; (d) plan §11 DOUBLE FAIL mapping row of `session-86-plan-w5a.md`; (e) gen-physicist 9A §4.5a 2A SECTOR split definition; (f) S82 W1-2 UNIFIED-AS-79-FULL Branch-A zeta-normalization route as the surviving path-(a) candidate; (g) W4 P4 commit `S86-BRANCH-IV-FORMULATION-COMMIT` audit `acc751101c8ca6ce`. Adjudication rule: each round's agent must produce a single named successor anchor (not "TBD"), with a 4-field carry-forward spec (what / inputs / gate / effort), and explicit substitution chain showing the successor anchor remains internally consistent at xi_E_GGE_inv=13.6425.

---

### Candidate 2 — Plan-§10 placeholder failure as PRU/SOURCE-RECONCILIATION audit precedent

**What it would do**: Promote the W5a §10 placeholder failure pattern into a permanent rule-class. The §10 substitution chain at plan-freeze used `xi_E_GGE_inv ≈ O(10⁻²)` as a placeholder estimate while the W4 P4 actual pin landed at **13.6425** — a 3-OOM upward error in the magnitude prediction. The §10 SIGN was correct (Z_ratio > 1, ENHANCEMENT confirmed) but the §10 MAGNITUDE was off by 2× at PIVOT55 and 92× at PIVOT312 in the same direction. Per the SOURCE-RECONCILIATION 4-band calibration (`.claude/rules/epistemic-discipline.md` §"Source Reconciliation"), `D_max = log10(13.6425) − log10(0.01) ≈ 3.13` falls in the "≥ 3.0 → hard plan-freeze halt" band. The audit class (c) PIN-DRIFT-FROM-STALE-SOURCE applies if the placeholder was based on a since-superseded value, OR class (e) PIN-PROMOTES-TO-CANONICAL-ON-PASS if the W4 P4 commit landed AFTER the §10 plan-freeze. Workshop establishes which class fires, and whether the placeholder→canonical transition should have triggered an automatic SOURCE-RECON HALT (and didn't).

**Why it's worthwhile**: This is exactly the failure mode the SOURCE-RECONCILIATION rule was promoted to detect (S85 W-3 v2 + 5A v2 union, landed S86 W0a-1). W5a is the first compute-time instance where a 3-OOM placeholder→canonical promotion bypassed pre-compute audit and produced a structural FAIL. The audit script `computations/_source_reconciliation_audit.py` (S86 W0a-2) should have caught this at plan-freeze for W5a — but the W5a plan was authored alongside W4 (HARD-DEPENDENCY UNMET at dispatch time per WP line 41 of plan), and the plan declared `xi_E_GGE_inv: <computed-at-runtime: W4 P4 commit output SHA>` rather than a pinned value. This is a NEW audit-class case: placeholder estimates in derivation chains where the canonical doesn't yet exist at plan-freeze. Cross-references: plan §10 line 441 ("estimate O(10⁻²)"); W4 P4 actual pin 13.642473 (canonical commit `acc751101c8ca6ce`); WP §W5a-1 ¶ "Numerical substitution chain" Step 2; `.claude/rules/epistemic-discipline.md` §"Source Reconciliation".

**Type**: 2-agent workshop

**Suggested agents**: gen-physicist, sagan-empiricist

**Rounds**: 2 (R1 each agent independently classifies the §10 placeholder failure under SOURCE-RECON 5-class taxonomy + proposes rule extension; R2 converge on a single rule-extension diff to `epistemic-discipline.md`)

**Context the workshop will need**: (a) plan §10 substitution chain Step 2 from `sessions/session-plan/session-86-plan-w5a.md` lines 403-447 (the placeholder estimate); (b) the W4 P4 actual pin 13.6425 with provenance audit `acc751101c8ca6ce`; (c) WP §W5a-1 "Numerical substitution chain" Step 2 (the corrected substitution); (d) `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" 5-class taxonomy + 4-band calibration; (e) `computations/_source_reconciliation_audit.py` (S86 W0a-2 output); (f) calibration corpus precedents: W1c-8 n_s sig-fig case + W2-4 cluster-span canonical-metric case (already in epistemic-discipline.md). Adjudication: must produce a concrete diff to add a 6th audit class for "placeholder-estimate-pending-runtime-canonical" with HARD-HALT severity at D_max ≥ 3.0, AND a verdict on whether W5a's FAIL retroactively triggers MANDATORY remediation.

---

### Candidate 3 — Linear-regime breakdown timescale and the SR-LO domain-of-validity boundary

**What it would do**: Compute the boundary in (xi_E_GGE_inv, ε_0, η_0) space at which substrate-first ξ²(0) IC drives ε past 0.5 (SR breakdown) within N ≤ 1 e-fold. The W5a result shows breakdown at N ≈ 0.13 e-folds for canonical (xi_E_GGE_inv=13.6425, ε_0=0.020, η_0=0.005). This defines a 3-parameter surface where SR-LO truncation remains self-consistent. The carry-forward proposed in W5a synthesis line 159 ("rescaled-IC SR-LO Z-factor at S87") asks exactly this question but limited to a single rescaling scan. The workshop generalizes: solve the dε/dN ODE analytically near N=0 for the breakdown time τ_break(ξ²₀) where ε(τ_break) = 0.5; map the level set τ_break = 55 (the canonical N_pivot); identify whether ANY (substrate-IC-rescaling × ε_0-rescaling × η_0-rescaling) trajectory threads the linear regime through to N=55 OR proves no such region exists.

**Why it's worthwhile**: The W5a verdict closes "SECTOR-1 SR-LO + substrate-first ξ²(0) corridor" — but the closure is structurally weaker than a permanent constraint. It says: at the canonical xi_E_GGE_inv pin, the SR-LO truncation is broken within 0.13 e-folds. It does NOT say: "no admissible substrate-first IC closes SR-LO". The breakdown-surface mapping converts a single FAIL into a permanent structural theorem (the SR-LO domain of validity in (ξ²₀, ε_0, η_0) space, whose intersection with the canonical-pin point is the source of the FAIL). This is a textbook constraint-map gain per `feedback_reporting-framing.md`. Cross-references: WP §W5a-1 substitution chain Step 2 (initial-slope analytic); §W5a-1 Interpretation paragraph (breakdown at N=0.13); WP synthesis line 159 (S87 carry-forward spec). The work also tests whether the substrate-first IC route could close at all in any regime, or whether it is structurally incompatible with SR-LO.

**Type**: solo (1 agent)

**Suggested agents**: transit-dynamics-theorist

**Rounds**: N/A (solo)

**Context the workshop will need**: (a) the dε/dN ODE form from gen-physicist 9A §4.5a; (b) canonical (xi_E_GGE_inv=13.6425, ε_0=0.020, η_0=0.005); (c) SR-LO validity criterion ε ≪ 1 (use ε < 0.5 as breakdown); (d) target N_pivot ∈ {3.12, 55}; (e) W5a data file `computations/s86_w5a_p3_sector_1_z_factor.npz` with `eps_substrate, eta_substrate, alpha_s_substrate, xi2_substrate` arrays for cross-check at the canonical point; (f) the analytic initial slope (dε/dN)|N=0 = ε_0 · (2η_0 − 4ε_0 + 2ξ²_0). Pre-register: "rescaled-IC SR-LO Z-factor PASS" — does there exist (ξ²₀, ε_0, η_0) within ±0.5 OOM of canonical where |Z_ratio − 1| ≤ 0.05? If yes: PASS class with the rescaling factor reported. If no: FAIL with a permanent theorem that substrate-first IC is structurally incompatible with SR-LO.

---

### Candidate 4 — CC2 monotonicity test on a 0.13-e-fold window: bookkeeping vs physics

**What it would do**: Audit the CC2 cross-check in W5a §W5a-1. CC2 was pre-registered as "ε(N) monotone-non-decreasing on the integration window [0, min(55, N_breakdown)]". W5a reports CC2 PASS with N_breakdown = 0.13 e-folds, minimum diff +6.251e−03. The PASS is bookkeeping-correct but physics-empty: it confirms ε is monotone over 0.0024 of the intended N=55 window — i.e., the test's domain shrunk to 0.24% of the original under the actual pin value. This is exactly the kind of "vacuous-margin" failure mode flagged in `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1 ("convention-shopping"), where a pre-registered band gets technically satisfied because the test was calibrated for a different regime than the one realized at runtime. Workshop establishes whether CC2's threshold should have been re-evaluated at runtime, OR whether the pre-registration should have been "monotone over [0, N_pivot]" with no fallback shortening clause.

**Why it's worthwhile**: This is a methodology surface that affects all SR-LO-style integration gates. The W5a CC2 was structured with a clause (`min(55, N_breakdown)`) that automatically rescues monotonicity when the integration breaks down — turning a test of "ε grows for 55 e-folds" into "ε grows for 0.13 e-folds." The PASS is mathematically correct but conveys no information. Generalizing: when the domain-of-validity of a numerical method depends on the value of a runtime-pinned canonical, the cross-check threshold must either (a) be defined on the full domain unconditionally OR (b) emit INFO (not PASS) when the auto-shortening clause activates. Cross-references: WP §W5a-1 line 50 (CC2 description); plan §0.5 cross-check pre-registration; `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS; the same auto-shortening clause appeared in earlier sessions but is worth surfacing now that a 0.13-e-fold case exists.

**Type**: solo (1 agent)

**Suggested agents**: sagan-empiricist

**Rounds**: N/A (solo)

**Context the workshop will need**: (a) WP §W5a-1 "Cross-checks" CC2 paragraph (line 50); (b) plan §W5a-1 CC2 pre-registration block from `session-86-plan-w5a.md`; (c) `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS list; (d) `.claude/rules/agent-standards.md` §"Completion Verification"; (e) W5a data file with the actual ε-trajectory N=0..55 (so the audit can verify the breakdown timescale and minimum-diff claim independently). Pre-register: solo report yields a 4-field carry-forward to S87 W0 hygiene wave with diff to plan-template specifying that auto-shortening clauses must emit INFO (not PASS) when triggered.

---

### Candidate 5 — Z-factor unaffected channels: explicit hierarchy of surviving substrate→A_s/n_s routes

**What it would do**: Catalog and rank the surviving routes from BRANCH-IV (W4 P4) → A_s/n_s prediction now that path-(c) has DOUBLE-DOUBLE-FAILed. WP §W5a-1 line 121 ("What the FAIL does NOT close") lists three: (i) BRANCH-IV itself; (ii) the Z-factor concept; (iii) S82 W1-2 UNIFIED-AS-79-FULL Branch-A (zeta-normalization). Plus the W5a synthesis line 155 lists: (iv) c_sub / F_amp BASELINE chain (W5b C15/C16). This is at least four surviving channels but they are stated in scattered prose, not ranked. Workshop produces a single ranking by (a) strength of empirical anchor (PASS history), (b) regime-of-validity span (e-folds where the route holds), (c) sensitivity to xi_E_GGE_inv (does it amplify or saturate?), (d) cross-channel coherence (do these routes give consistent A_s/n_s when quantified?).

**Why it's worthwhile**: With path-(c) BOTH-legs collapsed, the framework's substrate→A_s/n_s prediction stack needs a clean post-S86 picture to feed S87 planning. The W5a synthesis assumes path-(c) survives via SECTOR-2, but with SECTOR-2 also FAILed the surviving channels need explicit catalog. This is structural housekeeping with downstream stakes: every S87 gate that cites "substrate-first A_s prediction" needs a pinned route. Cross-references: WP §W5a-1 line 121 (three NOT-closed items); WP synthesis line 155 (c_sub/F_amp chain); S82 W1-2 UNIFIED-AS-79-FULL Branch-A as the most-tested surviving route; W5b C15/C16 verdicts (currently in W5b WP, not in scope here, but cross-cited).

**Type**: solo (2 agents)

**Suggested agents**: gen-physicist, lizzi

**Rounds**: N/A (solo, two independent reports for cross-validation)

**Context the workshop will need**: (a) the four named surviving channels from WP §W5a-1 line 121 + synthesis line 155; (b) S82 W1-2 UNIFIED-AS-79-FULL Branch-A verdict + zeta-normalization scheme; (c) W5b C15/C16 verdicts (look up `S86-W5B-*` in s86_gate_verdicts.txt); (d) BRANCH-IV W4 P4 PASS commit `acc751101c8ca6ce` with xi_E_GGE_inv=13.6425; (e) gen-physicist 9A taxonomy of paths (a)/(b)/(c). Pre-register: each agent produces a ranked table with (route, anchor PASS history, regime span, xi-sensitivity, current A_s prediction) and identifies which route(s) S87 carry-forward should pursue first by EVOI.

---

### Candidate 6 — Sign-confirmed-magnitude-refuted as a structural classifier

**What it would do**: Promote "SIGN confirmed, MAGNITUDE refuted" into a permanent verdict classification. W5a establishes a clean instance: the §10 substitution chain SIGN prediction (Z_ratio > 1, substrate-first ENHANCES) was confirmed at both pivots; the §10 MAGNITUDE estimates (0.22, 0.025) were refuted by 2× and 92× IN THE SAME DIRECTION because of the placeholder→canonical 3-OOM mismatch. Currently this gets recorded as "DOUBLE FAIL" with no structural credit for the sign agreement. But sign-correct-magnitude-wrong is a fundamentally different epistemic state from sign-flipped or both-flipped; it tells us the substitution chain was structurally right and only the input pin was misjudged. The workshop establishes whether to introduce a 3-tuple verdict structure (SIGN, MAGNITUDE, REGIME) where each can independently PASS/FAIL/INFO, OR a single composite verdict with sign/magnitude split as a verdict-line annotation.

**Why it's worthwhile**: This is a recurring pattern across the project. S64 quantum-metric, S60 H_0, S78 various, and now S86 W5a all show direction-correct/magnitude-wrong outcomes that get binned as FAIL alongside direction-flipped outcomes. The framework's epistemic vocabulary loses information in this binning. The §10 substitution chain in W5a is structurally correct — the WP itself confirms this at line 91-93 ("§10 SIGN prediction is CONFIRMED in direction at both pivots"). Treating the gate as a flat FAIL discards the structural insight that the chain is reliable for sign-prediction at any future xi_E_GGE_inv value. Cross-references: WP §W5a-1 substitution-chain Step 4 (sign-confirmed); plan §10 lines 428-447 (analytic estimate); the same pattern in earlier sessions (S64, S60, S78). Pre-registered prediction: workshop produces a diff to gate-verdict template adding a `[SIGN_VERDICT|MAGNITUDE_VERDICT]` companion field to verdict lines, retroactively applicable to existing direction-correct/magnitude-wrong FAILs.

**Type**: 2-agent workshop

**Suggested agents**: sagan-empiricist, gen-physicist

**Rounds**: 2 (R1 each agent independently proposes verdict-vocabulary extension with tradeoffs; R2 converge on a single template diff to gate-verdicts.md)

**Context the workshop will need**: (a) WP §W5a-1 substitution-chain Step 4 + Solution-space implication paragraphs; (b) the precedent FAILs where SIGN-correct-MAGNITUDE-wrong applied (S64 quantum-metric, S60 H_0, S78 audit cases — agent should grep verdicts file); (c) `.claude/rules/gate-verdicts.md` current verdict-line schema; (d) `.claude/rules/epistemic-discipline.md` §"What Counts as a Result" + §"What Does Not Count as a Result"; (e) the S86 PRU + SOURCE-RECONCILIATION rule extensions from W0a as a parallel precedent for permitting structured sub-verdicts within a single gate. Adjudication: must produce concrete schema diff, not vague "verdict types should be richer" prose.

