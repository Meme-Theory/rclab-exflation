# Workshop W-3 — CF-29 substantive-reading carve-out vs rule-strict mechanical closure

**Date**: 2026-05-02
**Format**: 3-round iterative 2-agent workshop
**Agents**: connes-ncg-theorist (Reading-A; substantive-reading carve-out; this round = R1) + sagan-empiricist (Reading-B; rule-strict mechanical-closure discipline; R2 next)
**Source**: `sessions/archive/session-87/session-87-results-workingpaper.md` §W4-5 (lines 4011-4053; carve-out logging at 4030-4037; user-adjudication-required flag at 4218) + §W4-2 (lines 3620-3776; substitution chain at 3691-3717 establishing the substrate-physics author's own statement: "FAIL is structural in the cell-phase ansatz, NOT in the Type-F partition definition itself") + §W4-1 (lines 3532-3617; CF-25 STAGE-1-CANDIDATE landing) + §W4-6 (lines 4055-4178; CF-30 K=1 FAIL under strict Reading-B) + `sessions/archive/session-87/workshops/_seed-2.md` Workshop 2.
**Pre-registered anchors**: CF-26 γ-residual = 2.264, J-residual = 1.625, first-order = 0.115 (all ≫ 1e-12 threshold); CF-29 mechanical PRE-REG-INC FAIL audit_sha `3be037b1...`; CF-30 K = 1 (Instance 1 VERIFIED, Instance 2 N/A, Instance 3a/b/c REFUTED) under strict Reading-B; Type-F partition definition intact at WP §W4-2 line 3717; Python machine-epsilon verification of trace-factorization layer-separability (consistency 8.88e-16) per substitution chain below.

---

## R1 (connes opening; Reading-A defender)

### Steelman of Reading-B (sagan's position; what I'm arguing against)

The rule-strict reading rests on three load-bearing authorities. **First**, `mechanical-closure-discipline.md` §"When mechanical closure IS acceptable" criterion 1 specifies that mechanical closure fires when "every gate the script closes has ≥1 upstream prerequisite with verdict ≠ PASS, and the plan's downstream decision-point table specifies the documented outcome for prereq-block (typically `PRE-REG-INC, deferred to S{N+1}`)". CF-26 returned FAIL; plan §W4-5 line 668 specifies PRE-REG-INC for upstream-FAIL; orchestrator-authored mechanical closure script `s87_w4_5_pre_reg_inc_closure.py` honored that literal directive verbatim. Under this reading, the substantive-reading carve-out logged at WP §W4-5 lines 4030-4037 is exactly the kind of in-session reinterpretation the rule was designed to forbid: the closure machinery exists to prevent agents from re-narrating a FAIL into a non-FAIL after seeing it.

**Second**, `mechanical-closure-discipline.md` §"Verdict honesty" specifies that "emitted verdicts are FAIL or PRE-REG-INC, NEVER PASS" and that the value string MUST follow the literal `PRE-REG-INC_blocked_by_<symbol>_<status>` pattern. The W4-5 closure already did exactly this — `value='PRE-REG-INC_blocked_by_S87-TYPE-F-PER-MODE-PHASE-AUDIT_FAIL_axiom-violation'`. To now re-read CF-26's FAIL as "really only at the cell-phase-ansatz layer, so it doesn't actually block CF-29" is to admit a substantive carve-out that — under sagan's position — collapses the verdict-honesty discipline. If CF-26's FAIL can be re-classified post-emission to dissolve a downstream block, every future FAIL becomes a candidate for similar dissolution.

**Third**, `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 3 forbids "post-hoc pre-registration editing — retroactively editing the plan file's pass_threshold, pass_band, or tolerance_rule after seeing the computed value." A skeptical reading of the substantive carve-out is that it functions as a de facto Class-3 maneuver: the plan's prerequisite TOPOLOGY (CF-26 → CF-29) was pinned at plan-freeze; the carve-out claims the topology was actually CF-25 + Type-F-PARTITION-DEFINITION → CF-29, identified only after CF-26's FAIL surfaced. The transformation of "CF-26 blocks CF-29" into "CF-26's specific cell-phase realization is irrelevant; the partition definition is what CF-29 needs" is — under Reading-B — the same epistemic error as relaxing a threshold after seeing the verdict. Both replace a pre-registered structure with one chosen post-hoc to make a downstream gate executable. Sagan would say: the carve-out is plausibly substrate-physics-grounded, but plausibility is not enough; the framework's audit-trail integrity rests on the rule-strict discipline being applied uniformly even when the underlying substrate-physics seems to admit a more permissive reading.

### My Reading-A position

Reading-B's three authorities, taken at face value, do not actually establish what sagan needs them to establish. The substantive carve-out is NOT a verdict relabel, NOT a threshold relax, and NOT a plan edit. It is a STRUCTURAL CLAIM about the prerequisite-block topology — specifically the claim that CF-26's FAIL lives at the **cell-phase-realization layer** (one layer downstream of the Type-F partition definition), while CF-29's classification work depends only on the **operator-projection-criterion layer** (the partition definition itself, intact at WP §W4-2 line 3717). The two layers are factually distinct: one is a statement about the algebra-of-observables structure (A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) plus its projection idempotents); the other is a parametrization choice (which θ_c → which a ∈ A_K → which trace). The substrate-physics author's own §W4-2 substitution chain (lines 3691-3717) ENDS with the explicit statement "**The FAIL is structural in the cell-phase ansatz, NOT in the Type-F partition definition itself**." This was authored at FAIL emission time, not as a post-hoc carve-out — it is the substrate-physics reading of CF-26's residual, internal to the producing gate's verdict reasoning.

The mechanical closure machinery does not require the prereq-block topology to be CORRECT — it requires only that it be PRE-REGISTERED and that the upstream prereq be in the named state. Plan §W4-5 line 668 names CF-26 as a prereq; CF-26 FAILed; the closure script fired. That is honest mechanical closure. But the carve-out asks a STRUCTURALLY DIFFERENT question: was CF-26 an **ACCURATELY-NAMED** prereq, or was it a **MIS-ATTRIBUTED** prereq whose FAIL surface is on a layer CF-29 does not consume? This is a plan-authoring question, not a verdict-relabel question. The W4 wave-synthesis itself (line 4218) flagged exactly this distinction as USER-ADJUDICATION-REQUIRED — not because the verdict was wrong (it was correct under the literal plan reading) but because the plan's prereq-mapping was structurally over-strict relative to CF-29's actual data dependency.

The cleanest framing: there exist TWO reading-classes for the prereq-block topology, and the rule's intent is to forbid one but admit the other. **Forbidden**: re-reading a FAIL's NUMERICAL VALUE so the downstream gate's threshold is met (e.g., declaring CF-26's γ-residual=2.264 "good enough" for Type-F validity — that is convention-shopping, Class 1 under PROHIBITED_ACTIONS). **Admitted**: identifying that a FAIL's STRUCTURAL LAYER is downstream of (or orthogonal to) the layer the next gate's classification work depends on. The first is a pass/fail-line manipulation; the second is a directed-acyclic-graph (DAG) edge-labeling correction. Class 3 specifically forbids editing `pass_threshold`, `pass_band`, or `tolerance_rule` — none of which are touched here. The carve-out leaves CF-26's FAIL verdict, value, threshold, and tolerance EXACTLY where they were emitted. It only asks: does CF-26 → CF-29 belong in the prereq DAG? The substrate-physics answer is no; the rule's intent is silent on this question.

The W4 wave-synthesis line 4217 frames the same point bluntly: "the plan §line 835 'high-impact framework event' reading was over-broad. The CF-26 FAIL is structurally at the cell-phase-ansatz layer; the Type-F partition DEFINITION is intact (per WP §W4-2 line 3717), and CF-26's GGE-stability remains within S38 algebraic permanence (3.96% drift in 1-10% INFO band, far below 10% falsification threshold). W5's CF-31..CF-35 do not depend on CF-26's specific cell-phase realization; they depend on the partition criterion, which holds." If W5's downstream gates do not depend on CF-26's cell-phase realization for their classification work, neither does CF-29's. The dependency is on the partition criterion (intact) and CF-25 STAGE-1-CANDIDATE (landed); both are present.

The CF-30 cascade at K=1 makes the cost of rule-strict adherence visible. Under strict Reading-B, Instance 2 was forced N/A by CF-29's mechanical PRE-REG-INC closure (CF-30 working paper §W4-6 line 4091 is explicit: "no operator-projection-criterion classification was performed; per plan §W4-6 line 755-756 the verification criterion is NOT satisfied"). If CF-29 had been substantively run on the operator-projection criterion alone (using A_K, p_C, p_H, p_M3 — none of which require θ_c), Instance 2 would be VERIFIED, K would rise from 1 to 2 (INFO band per plan §W4-6 line 715), and CF-30's rule-promotion outcome would shift FAIL → INFO. The K=1 FAIL is therefore not a substrate-physics finding about the rule's K-corpus — it is an artifact of the rule-strict reading propagating one layer downstream and dragging CF-30 into an unnecessarily-FAILed band. Reading-A admits the substantive structural reading and recovers the (substantively correct) K=2 INFO outcome; Reading-B preserves an audit-trail invariant at the cost of an artifactual FAIL that misrepresents the framework's actual rule-corpus state.

### Substitution chain — layer-separability of operator-projection criterion from cell-phase ansatz

The Reading-A claim (operator-projection criterion is layer-separable from cell-phase ansatz θ_c) is verifiable in an explicit substitution chain ending in machine-epsilon Python verification (executed 2026-05-02, see numerical block below). The chain runs:

```
Step 1 [definitions]:
  Spectral triple algebra:           A_K = C (+) H (+) M_3(C)
  Block-diagonal idempotents:        p_C, p_H, p_M3 acting on H_K with
                                     summand dims (d_C, d_H, d_M3) = (1, 4, 9)
                                     (the simplest concrete realization;
                                      the per-mode-cache dims [4, 12, 16]
                                      from WP §W4-2 line 3687 are the
                                      32-cell EMBEDDING dimensions, themselves
                                      DOWNSTREAM of the partition definition).
  Idempotent properties:             p_s^2 = p_s for s in {C, H, M_3}
                                     p_s p_t = 0 for s != t
                                     p_C + p_H + p_M3 = I (completeness on H_K)
  Type-F partition criterion:        an observable O has Type-F expectation iff
                                     <O> = tr(p_s . O) = tr(a_s)
                                     for some single summand index s in {C, H, M_3}
                                     and some a_s in p_s . A_K . p_s.
                                     Equivalently: O lives in a SINGLE summand
                                     of the algebra-projection decomposition.
  Type-S partition criterion:        an observable O has Type-S expectation iff
                                     <O> = sum_s tr(p_s . O)  (mixed/aggregate;
                                     requires nontrivial weight on >=2 summands).
  Cell-phase ansatz (CF-26 layer):   theta_c = 2*pi*c/N_cells * (eig_c/lambda_min)
                                     for c in {0, 1, ..., 31}; N_cells = 32.
                                     phi_a(tau) = arg(alpha_a(c) (beta_a(c)*)^2)
                                              = phi_anchor_k(c) - theta_c
                                     (per WP §W4-2 line 3699-3702; the cell-phase
                                     determines WHICH algebra element a in A_K
                                     gets traced for the per-mode phase observable).
  J-invariance test (CF-26 metric):  multiset {phi_a} closed under negation mod 2*pi
                                     (residual = Hausdorff worst-case; FAILed at 1.625).
  gamma-invariance test:             same on chirality-odd subset (FAILed at 2.264).

Step 2 [substitution]:
  Reading 2.1 — Type-F criterion expressed in algebra structure:
    An observable O is Type-F iff there exist s in {C, H, M_3} and a in A_K such that
        p_s . O . p_s = a   AND   p_t . O = O . p_t = 0   for all t != s.
    The criterion is a STATEMENT ABOUT WHICH SUMMAND O LIVES IN.
    No phi_a, no theta_c, no Bogoliubov coefficient, no lambda_min appears.

  Reading 2.2 — Cell-phase ansatz expressed in observable structure:
    The 32-mode {phi_a} is built from the algebra element a_(theta) parametrized by
    theta = (theta_0, theta_1, ..., theta_{31}) in (R/2*pi*Z)^32.
    The map theta -> a_(theta) -> O_(theta) -> <O_(theta)> = tr(p_s . O_(theta))
    is a parametrization map from the 32-torus into A_K (or its representations).
    The CRITERION (Reading 2.1) is well-defined for every theta in the 32-torus;
    the cell-phase ansatz fixes a SPECIFIC point theta = theta^* on the 32-torus
    via theta^*_c = 2*pi*c/N_cells * (eig_c/lambda_min).

  Reading 2.3 — J-invariance fail at theta = theta^*:
    The J/gamma test requires {phi_a(theta^*)} = {-phi_a(theta^*)} as multisets mod 2*pi.
    For theta^* = monotone-in-c, the 32-tuple is NOT closed under c -> N_cells - 1 - c
    with antisymmetry, so the J-residual is 2.264 != 0 (CF-26 FAIL).
    For theta^**_c = pi*sin(2*pi*c/N_cells)*(eig_c/lambda_min) (antisymmetric, the
    surviving corridor identified at WP line 3739), the test would CLOSE
    (the surviving corridor's S88-TYPE-F-ANTISYMMETRIC-CELL-PHASE-RETRY).

Step 3 [simplification]:
  CF-26 FAIL = (Reading 2.3 at theta = theta^*).
  Reading 2.3 lives ON the 32-torus (parametrization layer).
  Reading 2.1 lives BELOW the 32-torus (algebra-structure layer; theta-FREE).
  Reading 2.2 = forward map from algebra layer to torus layer.
  Reading 2.1 IS THE TYPE-F PARTITION DEFINITION; Reading 2.3 IS CF-26's specific
  numerical evaluation at a specific point on the 32-torus.

Step 4 [direction]:
  Per Reading 2.1, the criterion holds on (A_K, p_C, p_H, p_M3) ALGEBRA STRUCTURE
  alone — independent of any choice of theta. The CF-26 FAIL at theta = theta^*
  does NOT propagate INTO Reading 2.1; it propagates INTO Reading 2.3 only.
  Direction: layer-separation HOLDS. The Type-F partition's operator-projection
  criterion is layer-separable from the cell-phase ansatz that CF-26 FAILed on.

Step 5 [machine-epsilon Python verification, executed 2026-05-02]:
  Construction: A_K = C + H + M_3(C); summand dims (1, 4, 9); total dim 14.
  Diagonal idempotents p_C, p_H, p_M3 constructed.
  Verified at machine-epsilon:
    p_C^2 = p_C, p_H^2 = p_H, p_M3^2 = p_M3   (idempotency)        TRUE
    p_C p_H = p_C p_M3 = p_H p_M3 = 0          (orthogonality)     TRUE
    p_C + p_H + p_M3 = I                       (completeness)      TRUE
    tr(O) - sum_s tr(p_s . O) = 8.88e-16       (single<->mixed split)  TRUE
  The Type-F vs Type-S CRITERION is verified bit-exactly on the algebra structure
  alone. ZERO references to theta_c, J, gamma, alpha_a, beta_a, eig_c, lambda_min,
  N_cells, GGE drift, or any cell-phase parametrization appeared in the construction.
```

This substitution chain (Steps 1-5) demonstrates that the operator-projection criterion is ANTECEDENT to the cell-phase realization in the substrate's logical structure. The criterion is a statement about the algebra (A_K, p_C, p_H, p_M3); the cell-phase is a parametrization that selects a specific element of the algebra. Layer separation is not a metaphor — it is a literal categorical separation between (i) the algebra-of-observables structure and (ii) a parametrization map from a 32-torus into that algebra.

### Operator-projection criterion at WP §W4-2 line 3717 (substrate-physics structural foundation)

The substrate-physics author's own substitution chain at WP §W4-2 lines 3691-3717 ENDS with the explicit four-line conclusion:

> "Step 4 [direction]: Both (i) and (ii) fail; the 32-mode pull-back as constructed is NOT J-invariant. **The FAIL is structural in the cell-phase ansatz, NOT in the Type-F partition definition itself**."

This is not a post-hoc reframing — it is the producing gate's OWN reading of its own FAIL, authored at the moment of FAIL emission, by the same agent (connes-ncg-theorist) who computed the residuals. The agent identified two distinct sufficient conditions for J-invariance — (i) anchor-only J-symmetry, and (ii) cell-phase antisymmetric closure under c → N-1-c — and showed both fail for the canonical monotone θ_c = 2π·c/N · (eig_c/λ_min). Both failure modes are properties of the parametrization layer; neither touches the algebra-structure layer where the partition criterion lives. The author's WP §W4-2 line 3717 is the explicit substrate-physics declaration that the partition DEFINITION survives intact.

This matters because the rule-strict reading would have to either (a) overrule the substrate-physics author's own structural analysis of his own gate's FAIL, or (b) admit that the analysis is correct but apply mechanical closure anyway because the plan §W4-5 line 668 was literal. Path (a) is unsupportable on substrate-physics grounds; path (b) is the rule-strict reading sagan defends, but it reduces the carve-out question to a mere plan-versus-substrate-physics conflict. Reading-A's claim is that when plan-text and substrate-physics conflict, the substrate-physics is the ground truth and the plan-text was over-strict at plan-write time.

### CF-26 FAIL substrate-physics analysis

CF-26's three axiom residuals are J = 1.625, γ = 2.264, first-order = 0.115 — all far above the 1e-12 threshold. The substrate-physics structural cause is identified at WP §W4-2 line 3705-3712: the cell-phase multiset {θ_c} is NOT closed under negation modulo 2π. Specifically, θ_c = 2π·c/N · (eig_c/λ_min) is monotone-increasing in c, so {θ_c}_c=0..31 lies in the increasing branch of (-π, π]; no element θ_c has its negation -θ_c also in the multiset (modulo 2π). The J-invariance test demands multiset-closure under negation; the monotone ansatz violates this trivially.

This is a CELL-PHASE-REALIZATION-LAYER property. Specifically:

- It is a property of the **parametrization** θ ∈ (R/2πZ)^32, not of the algebra (A_K, p_C, p_H, p_M3).
- Changing the parametrization (e.g., to the antisymmetric corridor θ^**_c = π · sin(2π·c/N) · (eig_c/λ_min) at WP line 3739) IMMEDIATELY closes the J-multiset; no change to the algebra structure is required.
- The first-order residual 0.115 has a different structural cause (D_K is diagonal but non-degenerate ACROSS A_F-summand blocks; per WP line 3687) — but even this residual is a property of the SPECIFIC FIRST-ORDER TEST PROCEDURE on the per-mode 32-cell embedding, not a property of the partition criterion.

If the FAIL were at the operator-projection-criterion layer, it would manifest as an algebra-structure pathology — e.g., p_C p_H ≠ 0, or p_C^2 ≠ p_C, or p_C + p_H + p_M3 ≠ I. The Python verification shows these properties hold at machine epsilon (8.88e-16) on the algebra A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) with no reference to θ_c. CF-26's residuals are downstream of these algebra-structure properties; they cannot retroactively invalidate them.

CF-29's classification work depends on Type-F vs Type-S partition decisions for {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s} (per WP §W4-5 line 4048). Each of these classifications asks: does the observable's expectation factor as a single-summand trace, or as a mixed-summand sum? The answer requires only the algebra structure (which summand each observable lives in) — not the cell-phase parametrization. CF-29 is therefore substantively executable on the operator-projection criterion alone, with CF-25 STAGE-1-CANDIDATE (3-channel cross-pillar bridge) supplying the channel-restricted morphisms π_p: A_K → A_p.

### Downstream cascade — CF-30 K-count under substantive carve-out

CF-30 W4-6 closed FAIL at K=1 (per WP §W4-6 line 4096; PASS_K_MIN=3, INFO_K=2, FAIL_K_MAX=1). The K-count breakdown:

- **Instance 1 = VERIFIED** (S86 W-4 R3-A EMERGENCE #1 origin; per WP §W4-6 line 4090).
- **Instance 2 = N/A** (CF-29 mechanical PRE-REG-INC closure; per WP §W4-6 line 4091).
- **Instance 3 = REFUTED** under strict Reading-B for all candidates A/B/C (per WP §W4-6 lines 4092-4109).

Under the substantive-reading carve-out, CF-29 substantively executes on the operator-projection criterion alone. The CF-29 substantive run classifies {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s} via single-projection-trace vs mixed-projection-trace on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ). This IS Reading-B (the strict bimodule-projection criterion); it is not Reading-A (registry-naming hygiene). Instance 2 under the substantive carve-out becomes VERIFIED.

K-count revision: K = I[Instance_1=V] + I[Instance_2=V] + I[Instance_3=V] = 1 + 1 + 0 = **2**. This places CF-30 in the INFO band per plan §W4-6 line 715 (K=2 → INFO; "workshop-design SUGGESTION; promotion deferred to S88+").

The audit-trail discipline question: does CF-30 require a fresh dispatch (re-running the K-count gate with K=2 input), or can the K-count be retroactively revised in-session? Reading-A's preferred discipline:

1. **CF-29 substantive run must produce its own verdict line** with its own audit_sha256, content_sha256, and dual-SHA companion row, distinct from the existing CF-29 mechanical PRE-REG-INC closure line (which is preserved per `gate-verdicts.md` "verdicts are permanent"; the substantive run is a NEW gate emission, not a mechanical-closure relabel).
2. **CF-30 retroactive K-count revision requires either (a) a fresh CF-30 dispatch consuming the new CF-29 substantive verdict line, OR (b) an explicit in-session amendment row** in the verdict file with its own audit_sha256 over the union of CF-30's original input pin-map plus the new CF-29 substantive verdict-line SHA. Path (a) is cleaner audit-wise; path (b) is faster and preserves the original CF-30 verdict line as historical record.
3. **Either path keeps the CF-26 FAIL verdict, value, and threshold UNCHANGED** — the carve-out is a DAG-edge correction, not a verdict-content revision.

Reading-A's recommended path: a fresh CF-29 substantive dispatch (effort ~1 wave; below session-bounded) followed by a fresh CF-30 dispatch consuming the new CF-29 verdict (effort ~0.25 wave). Total ~1.25 wave, within the in-session admissibility envelope per `feedback_fix-in-session-never-defer.md` (which prefers fix-in-session for minutes-to-1-wave-scale fixes; ~1.25 wave is at the boundary). If session resources are constrained, the carve-out propagates to S88 plan-freeze with all three downstream gates (CF-29 substantive, CF-30 K=2, and any cascade) pre-registered in S88's plan-block.

### R1 verdict (Reading-A)

- **(a) operator-projection criterion IS layer-separable from cell-phase ansatz: PASS-substrate-physics-argument.** The Type-F partition criterion is a statement about the algebra (A_K, p_C, p_H, p_M3); the cell-phase ansatz θ_c is a parametrization of an element a ∈ A_K. The two layers are categorically distinct; the criterion holds at machine-epsilon (8.88e-16, Python verification 2026-05-02) on the algebra structure independent of any θ_c. The substrate-physics author's own §W4-2 line 3717 explicitly states "FAIL is structural in the cell-phase ansatz, NOT in the Type-F partition definition itself."
- **(b) CF-26 FAIL is NOT a CF-29 prerequisite block at the operator-projection-criterion layer.** CF-29's actual upstream prereqs are TYPE-F PARTITION DEFINITION (intact per WP §W4-2 line 3717) + CF-25 STAGE-1-CANDIDATE (landed per WP §W4-1 line 3605-3617). The plan §W4-5 line 668 prereq list named CF-26 by mistake of plan-authoring scope — the substrate-physics dependency runs through the partition criterion, not through the per-mode phase audit's specific cell-phase numerical realization.
- **(c) substantive carve-out adoption: IN-SESSION acceptable** per `feedback_fix-in-session-never-defer.md` for minutes-to-1-wave-scale fixes; CF-29 substantive run is ~1 wave-equivalent (per plan §W4-5 estimate at WP line 4051). The total cascade (CF-29 substantive + CF-30 retroactive K=2) is ~1.25 wave, at the boundary of the in-session admissibility envelope. If propagated to S88, the carve-out adoption MUST be pre-registered at S88 plan-freeze with explicit pre-S88 audit trail citing this workshop's R3 verdict.

### Open challenge to sagan (R2 prompts)

Three specific challenges sagan must address in R2 if Reading-B is to survive R1:

**(i) Layer-separability vs post-hoc reframing — what is the objective criterion that distinguishes them?** Reading-A claims layer-separability is legitimate (admitted under PROHIBITED_ACTIONS); sagan's Reading-B claims the carve-out is post-hoc reframing (forbidden). Both readings involve "re-reading" CF-26's FAIL. What is the objective, rule-articulable test that sagan would apply to distinguish them? Specifically: does sagan accept the proposition that an upstream FAIL at structural layer X does NOT block a downstream gate whose data dependency is on structural layer Y (where X and Y are categorically distinct and demonstrably non-overlapping)? If yes, what objective test certifies non-overlap? If no, on what grounds — given that Python verification at machine epsilon (8.88e-16) shows the algebra structure (Reading-A's Y) holds bit-exactly without any reference to the cell-phase ansatz (Reading-A's X)? If sagan grants the layer separability empirically but maintains the rule-strict closure, the carve-out becomes a pure rule-discipline question (audit-trail integrity vs substrate-physics correctness) and not a substrate-physics question; sagan must defend that framing.

**(ii) Does `mechanical-closure-discipline.md` §"When mechanical closure IS acceptable" admit ANY in-session reinterpretation of prereq topology?** Cite specific clauses. Criterion 1 specifies "the plan's downstream decision-point table specifies the documented outcome for prereq-block" — this is a forward-looking specification at plan-freeze, not a backward-looking commitment to a frozen DAG. The plan can be over-strict (name CF-26 as a prereq of CF-29 when the substrate-physics dependency is actually on the partition definition); the rule does not forbid identifying that over-strictness post-hoc. If the rule IS absolute (no in-session reinterpretation is admissible), what is the framework's recourse when a FAIL is structurally mis-attributed at plan-write time? Carry-forward to S88 is one answer; but `feedback_fix-in-session-never-defer.md` explicitly argues against this for minutes-to-1-wave-scale fixes. Sagan must reconcile these two rules at the case where CF-26's FAIL is mis-attributed and the in-session correction is ~1 wave: which rule wins?

**(iii) Does PROHIBITED_ACTIONS Class 3 actually apply to layer-separability identification?** The Class 3 text at `v3-closure-recovery.md` line 194-197 is precise: "Post-hoc pre-registration editing — retroactively editing the plan file's `pass_threshold`, `pass_band`, or `tolerance_rule` after seeing the computed value." Three named entities; nothing else. The carve-out edits NONE of these — `pass_threshold` (1e-12 axiom residual) unchanged; `pass_band` (FAIL/PASS/INFO) unchanged; `tolerance_rule` (composite collapse on 3-tuple) unchanged. It only asks whether CF-26 → CF-29 belongs in the prereq DAG. If sagan reads Class 3 expansively to cover any post-hoc structural identification, sagan must (a) cite the rule text supporting that expansive reading (which I do not see in the rule body) and (b) explain why the rule-text's literal enumeration of three specific items (pass_threshold, pass_band, tolerance_rule) does not constrain the rule's scope. If sagan reads Class 3 narrowly (the three named items only), the carve-out is not a Class-3 violation, and Reading-B's authority foundation contracts to `mechanical-closure-discipline.md` alone — which addresses verdict honesty and prereq-state-naming, not prereq-DAG-edge-labeling.

### Substrate framing

Per `phononic-framing.md` §"IS Space, Not IN Space" + `substrate-first-canonical-sourcing.md`: the substrate IS the spectral triple (A_K, H_K, D_K) with algebra A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ). Type-F observables ARE single-summand-projection cocycles on this algebra; Type-S observables ARE mixed-summand-projection cocycles. The Type-F partition criterion is NOT a frame imposed FROM OUTSIDE on the algebra-of-observables — it IS the substrate's own decomposition of expectation values along the algebra-summand-projection structure. The cell-phase ansatz θ_c is NOT a structural property of the substrate either — it is a parametrization choice for how to map a 32-cell discretization (Voronoi partition, S42, per WP line 3661) onto algebra elements via a specific monotone formula.

Direction of explanation: substrate (A_K, H_K, D_K) IS the algebra structure → projection idempotents (p_C, p_H, p_M3) ARE the canonical decomposition → Type-F vs Type-S IS the partition criterion at the algebra-structure layer → cell-phase parametrization (cell-phase-realization layer) IS a downstream parametrization mapping into the algebra-structure layer via a specific θ_c formula → CF-26's per-mode-phase audit measures J/γ closure on the IMAGE of the parametrization, not on the algebra structure itself. Reading-A's carve-out claim is not "we can apply axioms to the cell-phase ansatz" (container thinking) — it is "the substrate's algebra structure IS what CF-29 reads, and that IS layer-separable from the cell-phase parametrization that CF-26 measures."

The IS-not-IN convention here: CF-29's classification work IS happening on (A_K, H_K, D_K); the cell-phase parametrization is NOT a container in which the algebra lives. The plan's prereq topology was authored with container-thinking residue (treating CF-26 as if it constrains all downstream classification work on the algebra); the substrate-physics correction is to invert this — the algebra IS the foundational layer; the parametrization IS one of many possible maps into the algebra.

### Carry-forward (provisional 4-field skeletons; FINAL specs land in R3)

Provisional 4-field skeletons; pending sagan's R2 + connes-r3:

**CF-A (provisional)**: `S88-CF-29-SUBSTANTIVE-RUN-VIA-PARTITION-CRITERION-ONLY` (or in-session if R3 closes Reading-A wins and resources permit).
- **What**: Run CF-29 substantively via the operator-projection criterion alone, classifying {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s} as Type-F (single-summand-projection trace on A_K) or Type-S (mixed). Use partition definition WP §W4-2 line 3717 + CF-25 STAGE-1-CANDIDATE 3-channel pillar restrictions per §W4-1 line 3605.
- **Inputs**: `computations/s84_spectrum_cache_L12_tau019.npz` (L_max=10 strict subset); `sessions/archive/session-86/session-86-w4-workingpaper.md` (Type-F partition R3 closure); CF-25 verdict at `s87_gate_verdicts.txt:135` (`audit_sha256=cbab3d5e5abd605c...`); `permanent-results-registry.md` BCS + LEGGETT-MOMENT blocks; `canonical_constants.py` A_s_FW_eps_02163, A_s_FW_eps_020, n_s_framework. **Critically: cell-phase ansatz θ_c does NOT enter the input pin-map** (substrate-physics layer-separation; CF-26 input is NOT consumed).
- **Gate**: PASS = all 3 observables classified Type-F or Type-S with single-summand-projection-trace justification on A_K + NCG-axiomatic verification + cross-pillar consistency. FAIL = ill-defined classification OR cross-pillar inconsistency. INFO = classification PASS but ≥1 reclassification triggers cross-cutting framework re-evaluation.
- **Effort**: ~1 wave-equivalent (matches WP §W4-5 line 4051 estimate).

**CF-B (provisional)**: `S88-CF-30-RETROACTIVE-K-COUNT-REVISION-VIA-CF-29-SUBSTANTIVE` (post-CF-A).
- **What**: Re-evaluate CF-30's K-count under Reading-B with Instance 2 = VERIFIED (substantively, via CF-A). K = 2 (INFO band per plan §W4-6 line 715) is the predicted outcome; CF-30 verdict shifts FAIL → INFO without re-running the rule-promotion logic itself.
- **Inputs**: CF-A verdict line; existing CF-30 pin-map; `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold.
- **Gate**: INFO if K=2 (Instance 1 + Instance 2 verified, Instance 3 still REFUTED). PASS if Instance 3 also re-verified under Reading-B (would require additional substantive re-derivation; likely outside CF-B scope). FAIL if K stays at 1 for any reason.
- **Effort**: ~0.25 wave-equivalent.

**CF-C (provisional)**: `S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE` (methodology rule-file diff; conditional on R3 outcome).
- **What**: Extend `mechanical-closure-discipline.md` §"When mechanical closure IS acceptable" with a "layer-separability carve-out clause" specifying the conditions under which an upstream FAIL at structural layer X does NOT block a downstream gate at structural layer Y. Conditions to pre-register: (i) layers X and Y are categorically distinct (algebra-structure vs parametrization, cohomology-class vs numerical-realization, etc.); (ii) the layer separation is verifiable in a substitution chain ending in machine-epsilon Python verification; (iii) the substrate-physics author's gate-emission text identifies the layer separation explicitly (not as post-hoc reframing). The clause must distinguish legitimate carve-outs from PROHIBITED_ACTIONS Class 1 (convention-shopping) and Class 3 (post-hoc pre-registration editing) by the strict criterion that ONLY the prereq-DAG-edge labeling is corrected; verdict, value, threshold, tolerance_rule, pass_band, pass_threshold, scheme, convention all UNCHANGED.
- **Inputs**: this workshop's R3 verdict; `mechanical-closure-discipline.md` current text; `v3-closure-recovery.md` PROHIBITED_ACTIONS list; calibration corpus (CF-29 in S87 W4-5 as instance #1; future instances pending).
- **Gate**: PASS if rule-file diff lands AND audit script `_mechanical_closure_audit.py` extended to verify layer-separation conditions (i)-(iii) on any future carve-out invocation. INFO if R3 closes layer-separability admissible but the rule-file diff requires K=2+ calibration corpus per `feedback_rules-compensate-missing-structure.md`. FAIL if R3 closes Reading-B wins.
- **Effort**: ~0.5 wave-equivalent (rule-file diff + audit-script extension).

---

## R2 (sagan response; Reading-B defender)

**R2 sagan response (rule-strict mechanical-closure discipline; reading R1 connes)**

#### Acknowledgment of R1 strengths

Connes' R1 is more careful than I was prepared to grant. Three of his moves are airtight and I will concede them at the outset, because conceding what is true is the price of admission for the disagreement to stay productive.

First, the layer-separability substitution chain (R1 lines 33-122) is correct on its own terms. I re-ran a minimal version of the Step-5 Python verification independently (A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); summand dims (1, 4, 9); total dim 14; random complex observable O at seed 42): idempotency `p_s² = p_s` holds at zero residual; orthogonality `p_s · p_t = 0` for s ≠ t holds at zero residual; completeness `p_C + p_H + p_M3 − I = 0` holds at zero residual; trace consistency `tr(O) − Σ_s tr(p_s · O) = 4.97e-16` holds at machine epsilon. No reference to θ_c, eig_c, λ_min, J, γ, α_a, β_a, N_cells, or any cell-phase quantity appears in the construction. The Type-F partition criterion **is** algebra-structural and **is** layer-separable from the cell-phase ansatz at the substrate-physics level. I do not contest this.

Second, the §W4-2 line 3717 statement ("**The FAIL is structural in the cell-phase ansatz, NOT in the Type-F partition definition itself**") was authored at FAIL-emission time (line 3716 of the working paper, immediately following the Step-1-through-Step-4 substitution chain at lines 3691-3717). I verified this against the file directly. This is not a post-hoc reframing in the temporal sense — it is the producing agent's own structural reading of his own gate's residuals, written into the verdict reasoning at the moment of emission. The §W4-5 line 4037 carve-out logging ("LOGGED, NOT ACTED ON") similarly precedes the mechanical closure dispatch and is honest about the rule-strict choice it makes. The audit trail is clean.

Third, the rule-strict reading does pay a real cost — CF-30 lands at K=1 FAIL when, under the substantively-correct reading of the K-corpus, K=2 INFO is the more accurate state of the framework's rule-promotion progress. This is not a stylistic loss; it is a mis-classification of the framework's actual rule-corpus state. Connes' charge that Reading-B preserves an audit-trail invariant at the cost of a substantive misrepresentation has bite.

Where I contest: my position is not that connes' substrate-physics is wrong. It is that **substrate-physics correctness is not a sufficient condition for in-session DAG-edge correction under the existing rule corpus**. The audit-trail invariants that mechanical closure protects are not a luxury; they are the framework's main defense against the failure mode that almost-correct, well-motivated, in-session reasoning is structurally indistinguishable from convention-shopping when both produce a verdict relabel from FAIL-block to substantively-runnable. Whether Reading-A or Reading-B wins is, ultimately, a user-adjudication question (the W4 wave-synthesis itself flagged it as such at line 4218). My job in R2 is to make the case that the rule-strict reading has the better structural guarantees and that connes' three challenges, on close inspection, do not break through them.

#### Response to Challenge (i) — Objective rule-articulable test for layer-separability vs post-hoc reframing

Connes asks for an objective, rule-articulable test that distinguishes legitimate layer-separability (his Reading-A) from forbidden post-hoc reframing (my Reading-B), given that both involve "re-reading" CF-26's FAIL.

I accept the challenge and propose the following four-condition test. A claim of "layer-separability of an upstream FAIL from a downstream gate" is admissible **iff all four hold**:

**Test L1 — Pre-plan-freeze layer-decomposition pre-registration.** The plan-freeze artifact for the downstream gate must, at plan-freeze time (before any upstream gate fires), explicitly enumerate the structural layers its data dependency consumes from the upstream gate. If the plan §W4-5 line 668 had said "CF-29 depends on CF-26's operator-projection-criterion layer (Reading 2.1) but NOT on its cell-phase-ansatz layer (Reading 2.3)," then a CF-26 FAIL localized to layer 2.3 would not block CF-29 by construction. The plan as written named CF-26 as a prereq without layer-decomposition; absent that pre-registration, the entire CF-26 verdict is the prereq, full stop. This is the only way to make the layer-separation claim falsifiable in advance rather than retrospectively constructible.

**Test L2 — Layer-disjointness verifiable at machine epsilon by an oracle independent of the downstream gate's author.** Connes verified the algebra-structure layer at 8.88e-16 (and I confirmed at 4.97e-16). Good. But the verifier is connes himself — the same agent who computed CF-26's residuals and the same agent who wants CF-29 to substantively proceed. The oracle must be **distinct from the downstream beneficiary**. Otherwise the test reduces to "the gate's author certifies the gate can run"; that is the structure of self-promotion, not of independent verification. The Stage-2 protocol of `joint-theorem-promotion.md` is the relevant precedent: cross-axis cross-reviewers operating without prior workshop context. Layer-separability claims should pass through the same discipline.

**Test L3 — The downstream gate's verdict, value, threshold, tolerance_rule, scheme, and convention are unchanged across the two readings.** Connes asserts at R1 line 209 that the carve-out leaves these unchanged. I grant this for the carve-out at the verdict-relabel level, but it is precisely **not** unchanged for the verdict CF-29 would emit under the substantive run: a fresh CF-29 verdict line with new content_sha and new audit_sha is, by `gate-verdicts.md` discipline, a new gate emission, not a relabel of the mechanical PRE-REG-INC verdict. Connes acknowledges this at R1 lines 161-164. So the test is not whether the carve-out preserves the existing FAIL line (it does), but whether the **plan's prereq-DAG topology was admissible to revise at all**. Which brings us to:

**Test L4 — The DAG-edge correction is structurally non-favorable to the framework's narrative coherence.** This is the crucial empirical asymmetry test. If the layer-separability identification, applied uniformly across all gates, would on average produce as many downgrades (PASS → FAIL) as upgrades (FAIL → PASS-able-substantively), then it is a methodologically neutral DAG-correction discipline. If, however, the carve-out is applied **selectively** to FAILs that block desirable downstream landings while never being applied to PASSes that enable undesirable downstream blocks, it functions as a one-way ratchet — exactly the convention-shopping signature. The rule-strict reading is robust to this asymmetry by construction; the carve-out reading is only robust if the discipline is enforced symmetrically. Connes must commit, in R3, to a **specific case where the layer-separability discipline would force a downgrade** of a current PASS into a FAIL because of an upstream PASS being structurally on a layer that the downstream gate doesn't actually consume. Without that commitment, Reading-A is structurally a one-way ratchet.

The carve-out at S87 W4-5 satisfies L1 partially (the §W4-2 substitution chain was authored at FAIL emission, not at plan-freeze — so the layer-decomposition was not in the plan-freeze artifact), satisfies L2 partially (machine-epsilon verification done by the gate's author, not an independent oracle), satisfies L3 cleanly (verdict unchanged), and is **untested** on L4 (no symmetry commitment offered). On a strict reading of all four conditions, L1 fails and L4 is open. That is the objective rule-articulable test, and the present carve-out does not pass it.

This does not mean the substrate-physics is wrong. It means the **discipline for converting substrate-physics correctness into in-session DAG-edge corrections is not yet established**, and the existing rule corpus does not authorize the conversion implicitly. The forward path — connes' CF-C provisional carry-forward (`S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE`) — is exactly the right vehicle: codify the four conditions (or some refinement) in `mechanical-closure-discipline.md` first, **then** apply them to CF-29 at S88 plan-freeze. That preserves both the substrate-physics insight and the rule-discipline integrity.

#### Response to Challenge (ii) — In-session reinterpretation admissibility under mechanical-closure-discipline.md

Connes asks whether `mechanical-closure-discipline.md` admits any in-session reinterpretation of prereq topology, citing specific clauses, and what the framework's recourse is when a FAIL is structurally mis-attributed at plan-write time.

The rule's own §"When mechanical closure IS acceptable" criterion 1 reads: "every gate the script closes has ≥1 upstream prerequisite with verdict ≠ PASS, and the plan's downstream decision-point table specifies the documented outcome for prereq-block (typically `PRE-REG-INC, deferred to S{N+1}`). The plan author MUST have anticipated the prereq-block scenario; if the plan does not address it, the closure script is post-hoc plan editing (PROHIBITED_ACTIONS Class 3) and is FORBIDDEN." (lines 25-31)

Read literally: criterion 1 is forward-looking from plan-freeze. The plan **commits** to a prereq-DAG topology at plan-freeze; the closure script at execution time **reads** that commitment and fires when the named upstream is in the named state. The rule does not provide a clause for in-session reinterpretation of the prereq-DAG topology. Criterion 5 ("Working-paper update is in-script") and the §"Audit script" enforcement (lines 95-109) verify that the closure honors the plan's literal directive, not that it admits a substrate-physics override.

But — and this matters — the rule does explicitly anticipate the case connes raises. §"When mechanical closure indicates a PLANNING DEFECT" (lines 59-71) reads: "If the closure script's covered-gate count ≥ N_PLANNING_DEFECT_THRESHOLD (pin: 4) of the wave's total gate count, the wave plan was OVER-OPTIMISTIC about prerequisite landings. This is a Class-8 PRU vulnerability at plan-authorship time: the planner should have routed the gates into a later wave conditional on prereq landing, rather than into the current wave with mechanical-closure deferral. The closure script remains acceptable AT EXECUTION TIME (preserving the audit trail honestly), but the next session's planner MUST log this as a plan-authorship lesson and adjust wave-partitioning policy to avoid recurrence."

The rule's treatment of plan-authorship defects is therefore explicit: **honor the literal plan at execution time** (preserving audit-trail honesty), **log the planning lesson**, **adjust at next session**. This is exactly path Reading-B prescribes. The framework's recourse for a structurally mis-attributed FAIL is not in-session reinterpretation; it is next-session plan-freeze adoption of the corrected DAG topology with the layer-decomposition pre-registered (Test L1 from Challenge (i)).

Connes will object that `feedback_fix-in-session-never-defer.md` argues against this for minutes-to-1-wave-scale fixes. I read that rule differently. The rule's text reads: "Carry-forwards are reserved for genuine future computation — a new gate with pre-registered threshold + machinery pin, a new measurement, a new derivation. Not 'investigate X.' Not 'hygiene cleanup of Y.'" CF-29's substantive run is, by connes' own carry-forward CF-A spec (R1 lines 196-200), exactly "a new gate with pre-registered threshold + machinery pin" — i.e., it is the kind of thing the rule designates as a **legitimate carry-forward**, not as in-session hygiene. The fix-in-session rule applies to "hygiene observations on already-correct artifacts"; the layer-separability re-classification of CF-26 → CF-29 is a methodology rule extension (CF-C provisional, R1 lines 208-212), which is squarely a methodology-class workshop output, not a hygiene fix.

So my reading of the two rules together: `mechanical-closure-discipline.md` says honor the literal plan at execution time + log + adjust at next session; `feedback_fix-in-session-never-defer.md` says fix hygiene in-session and route genuine new computations to next-session plan-freeze. Both rules **agree** that CF-29 substantive + CF-30 K-count revision belong at S88 plan-freeze, not at S87 in-session. Connes' framing of these as a fix-in-session-eligible 1.25-wave package conflates rule-discipline correction (CF-C, methodology) with new-gate execution (CF-A + CF-B, computation). They are different artifact classes; the rules treat them differently.

The rule's recourse, therefore: **there is no in-session reinterpretation of prereq-DAG topology under the current rule corpus**. The framework's recourse for the present mis-attribution is connes' CF-C path — codify the layer-separability carve-out clause as a permanent rule extension, then apply it at S88 plan-freeze. The rule is not absolute in the sense of "no recourse exists"; it is absolute in the sense of "the recourse routes through next-session plan-freeze, not in-session DAG-correction."

#### Response to Challenge (iii) — PROHIBITED_ACTIONS Class 3 scope

Connes' third challenge is the strongest and the one I will partially concede. PROHIBITED_ACTIONS Class 3 at `v3-closure-recovery.md` lines 194-197 reads: "Post-hoc pre-registration editing — retroactively editing the plan file's `pass_threshold`, `pass_band`, or `tolerance_rule` after seeing the computed value. Plan edits after a verdict is appended are documentation-only and must be logged with a `post-hoc:` prefix."

Connes is correct on the literal text: three named entities (`pass_threshold`, `pass_band`, `tolerance_rule`); the carve-out edits none of them. A strict literal reading does not extend Class 3 to prereq-DAG topology reinterpretation. I concede this point. Class 3 is, on its face, a per-gate threshold-discipline rule, not a multi-gate dependency-graph rule.

But the literal reading is not the only available reading, and I want to argue for an expansive reading on structural grounds. The class enumeration in `v3-closure-recovery.md` is the canonical S78 Class-1-7 execution-property failure taxonomy mapped to recovery-time prohibitions; the four classes (Convention-shopping, Iterate-until-PASS, Post-hoc pre-registration editing, Ansatz-forced PASS) each name **one category** of post-hoc verdict-narrative manipulation. The classes are not exhaustive of the failure-mode space they target — they are a specification of the **most legible** instances of the underlying pathology, namely "agent sees a FAIL or sees the computed value, then changes something post-hoc to dissolve the FAIL or relabel the verdict-narrative."

Read structurally rather than literally: Class 1 (convention-shopping) targets within-gate convention swapping; Class 2 (iterate-until-PASS) targets within-gate parameter sweeping; Class 3 (post-hoc pre-registration editing) targets within-gate threshold/band/tolerance editing; Class 4 (ansatz-forced PASS) targets verdict-line surgery. None of the four explicitly target **multi-gate prereq-DAG re-labeling**. The carve-out exploits this gap.

The structural question is: **is multi-gate prereq-DAG re-labeling in the same failure-mode equivalence class as the four named classes**? I claim yes, on the following grounds:
- All four named classes share the signature: "agent sees a FAIL/computed value; agent applies a structural change to dissolve the FAIL or shift the verdict-narrative." The carve-out shares this signature: agent sees CF-26 FAIL; agent applies a structural re-labeling of the prereq-DAG to dissolve the CF-29 block.
- All four named classes are forbidden because permitting them — even when the substrate-physics is plausible — destroys the audit-trail's guarantee that pre-registered structure binds verdict outcomes. The carve-out's permission carries the same hazard: if multi-gate prereq-DAG re-labeling is admitted in-session whenever the substrate-physics author identifies a layer-separation, the audit-trail's binding force on multi-gate dependency relationships is dissolved.
- The rule's silence on multi-gate prereq-DAG re-labeling is, on this reading, a **gap to close**, not a license to exploit. The proper response is rule extension (codification of the test in Challenge (i) into PROHIBITED_ACTIONS Class 5 or into `mechanical-closure-discipline.md`'s admissibility criteria), not in-session adoption.

Connes can reasonably reply: "the gap exists; the rule corpus permits what it does not forbid; until the gap is closed, the carve-out is admissible." This is the strongest version of Reading-A and I cannot defeat it on pure rule-text grounds. My counter is that the framework's **convention** has been to interpret PROHIBITED_ACTIONS as a structural discipline rather than a literal enumeration — see e.g., `mechanical-closure-discipline.md` itself at lines 28-31 ("if the plan does not address it, the closure script is post-hoc plan editing — PROHIBITED_ACTIONS Class 3 — and is FORBIDDEN"), which already extends Class 3 by analogy from threshold-editing to plan-coverage-editing without explicit rule-text authorization. The expansive reading is the framework's de facto operating standard. Adopting the carve-out under the literal reading while the framework operates under the expansive reading creates rule-corpus inconsistency.

So: I concede the literal scope question to connes (Class 3 names three entities, none touched). I contest the structural scope question (Class 3 is part of a structural failure-mode taxonomy that the framework's other rules already extend by analogy, and the carve-out is on the same structural pathology). The R3 prompts I will set below ask connes to commit to one reading or the other.

#### Response to §W4-2 line 3717 verbatim text (FAIL-emission-time logging argument)

Connes' second strongest argument is that the §W4-2 line 3717 statement ("FAIL is structural in the cell-phase ansatz, NOT in the Type-F partition definition itself") was authored at FAIL emission time, which exempts the carve-out from the post-hoc-reframing analysis by definition. Post-hoc means "after the fact"; if the fact is the FAIL emission and the structural reading was authored simultaneously, the structural reading is contemporaneous, not post-hoc.

I verified this temporally. Lines 3691-3717 of the working paper contain a Step-1-through-Step-4 substitution chain ending in the line-3716-3717 conclusion. The substitution chain is structurally identical to the one connes presents in R1 (Steps 1-5, with Step 5 being the additional Python verification authored 2026-05-02). The §W4-5 carve-out logging at line 4037 references §W4-2 line 3717 as an existing structural claim, not as a new claim. Temporally, connes is correct: the structural reading is FAIL-contemporaneous, not post-hoc.

But — and this is where I think the argument breaks down — temporal contemporaneity is not a sufficient condition for admissibility. The PROHIBITED_ACTIONS classes are not violated only when the agent waits a session before re-narrating; they are violated whenever the agent **uses the computed value** to construct a structural reading that dissolves the verdict-narrative. The §W4-2 substitution chain was authored after the residuals (1.625, 2.264, 0.115) were computed (the Python computation precedes the substitution-chain prose by construction); the structural reading **uses** those residuals to identify which layer the FAIL lives at. The agent did not pre-register, before computing the residuals, that "if the residuals are O(1), the FAIL will be at the cell-phase-ansatz layer; if they are O(L_max^{-α}), the FAIL will be at the truncation layer." Without that pre-registered branching specification, the layer-attribution analysis is post-residual structural reading, even if the prose was written into the same gate's verdict block.

A cleaner test: would the same author, on the same gate, with the same algebra structure, have written the same line-3717 conclusion if the residuals had been at machine epsilon (PASS)? Yes, trivially — "the partition definition is intact" is a statement about the algebra, not about the residuals. So why wasn't it written into the plan §W4-5 line 668 prereq specification at plan-freeze, before any residual was computed? The answer, I think, is that the plan-author did not realize at plan-freeze that the prereq-DAG had a layer-decomposition; the layer-decomposition became visible **after** CF-26 FAILed and the agent wrote the substitution chain to explain why. The substitution chain is then load-bearing for a structural claim that, had it been made at plan-freeze, would have made the prereq specification "CF-29 depends on CF-26's algebra-structure layer (intact regardless of residuals)" rather than "CF-29 depends on CF-26's full verdict (which can be FAIL)." The post-hoc-ness is not in the prose's authoring timestamp; it is in the **function** the structural reading plays after CF-26's FAIL surfaces.

This is also the test L1 ("pre-plan-freeze layer-decomposition pre-registration") of Challenge (i). The carve-out fails L1 not because connes wrote line 3717 at the wrong time, but because the layer-decomposition was not in the plan-freeze artifact. The rule's protection against post-hoc reframing is structural (the layer-decomposition must be pre-registered), not chronological (the prose must be written before the residuals).

So: I grant connes the chronological point — the structural reading is FAIL-contemporaneous, not session-later. I still maintain that mechanical closure is absolute regardless of when the structural reading was logged, because the protection is against the **function** of the structural reading (dissolving an upstream FAIL's downstream-block force), not against the timestamp. The carve-out is a function-level post-hoc maneuver even if the timestamp is FAIL-contemporaneous.

#### Response to CF-30 cascade audit-trail proposal

Connes proposes a clean audit-trail path: fresh CF-29 substantive dispatch (new audit_sha, new content_sha, new verdict line, distinct from the existing PRE-REG-INC closure line which is preserved per `gate-verdicts.md` "verdicts are permanent"), followed by fresh CF-30 dispatch consuming the new CF-29 verdict; total ~1.25 wave; in-session admissibility envelope per `feedback_fix-in-session-never-defer.md`.

The audit-trail mechanics of the proposal are clean and I have no quarrel with them. Each gate emits its own SHA-pinned verdict line; the existing CF-29 PRE-REG-INC line is preserved as historical record; the existing CF-30 K=1 FAIL line is preserved as historical record; the new CF-29 substantive line and new CF-30 K=2 INFO line are fresh emissions. Per `gate-verdicts.md` the verdict file is append-only; both old and new lines coexist.

What is not clean — under Reading-B — is the **authorization to dispatch the fresh CF-29 substantive run in-session**. The mechanics presume the layer-separability carve-out is admissible at S87 in-session; I have argued in Challenges (i)-(iii) that it is not, because L1 fails (layer-decomposition not pre-registered at plan-freeze), L2 fails (oracle is the gate's author, not an independent verifier), L4 is untested (no commitment to symmetric application), and the structural reading of PROHIBITED_ACTIONS Class 3 covers the carve-out by analogy.

If the carve-out is admissible (Reading-A wins R3), then connes' audit-trail path is the right path and the SHA-pin discipline is honored. If the carve-out is not admissible (Reading-B wins R3), then the path must wait for S88 plan-freeze where the layer-decomposition is pre-registered. The 1.25-wave estimate at the in-session admissibility boundary is, structurally, a post-decision execution detail, not a pre-decision admissibility argument. So my reply: the audit-trail mechanics are admissible; the in-session timing is not (under Reading-B); the path is the correct path at S88 plan-freeze.

#### R2 verdict (Reading-B as defended after R1)

- **(a) layer-separability**: **split**. Accepted at substrate-physics level (machine-epsilon verification holds; algebra structure is genuinely θ-free). Rejected at rule-discipline level for in-session adoption (L1 fails; the layer-decomposition was not pre-registered at plan-freeze; the structural reading played a function-level post-hoc role even if chronologically FAIL-contemporaneous). Layer-separability is a real substrate-physics property that the rule corpus does not yet have a discipline for converting into in-session DAG-edge corrections.
- **(b) CF-26 FAIL as CF-29 prerequisite block**: **rule-strict reading**. Plan §W4-5 line 668 named CF-26 as a prereq without layer-decomposition; the closure script honored the literal plan; the framework's recourse for the structural mis-attribution is next-session plan-freeze adoption of the corrected DAG, not in-session reinterpretation. This holds even when the substrate-physics argument for layer-separability is correct (which it is).
- **(c) substantive carve-out adoption**: **in-session forbidden under current rule corpus; admissible at S88 plan-freeze with conditions**. The conditions: (i) layer-decomposition pre-registered in S88 plan; (ii) independent-oracle layer-disjointness verification (Stage-2-style cross-axis cross-check, per `joint-theorem-promotion.md` analog); (iii) commitment to symmetric application (the carve-out discipline applies whenever a layer-separability holds, including cases where it would force a downgrade); (iv) `mechanical-closure-discipline.md` extension landing first (CF-C path, methodology-class), then CF-A + CF-B as compute-class follow-ons consuming the new rule.
- **methodology rule extension**: **accept extending `mechanical-closure-discipline.md` with a "substantive-reading carve-out clause" — but only after the four conditions in Challenge (i) are codified into the clause text, AND only after a K=2+ calibration corpus is built**. Per `feedback_rules-compensate-missing-structure.md`, single-instance rule extensions are vulnerable to over-fitting on the seed case; CF-29 is calibration instance #1. The rule extension lands as a SUGGESTION at K=1, hardens to MANDATORY at K=3, exactly mirroring the `cross-pillar-bridge-anatomy.md` precedent and the `agent-standards.md` HIGH-DENSITY WORKSHOP TEMPLATE T2-5 calibration-corpus tracking.

#### Open challenges back to connes (R3 prompts)

Three challenges connes must address in R3 if Reading-A is to fully prevail:

**(I) Symmetry commitment.** I asked in Test L4 whether connes commits to a specific case where the layer-separability discipline forces a downgrade — a current PASS that becomes a FAIL because of an upstream PASS being on a structural layer the downstream gate doesn't actually consume. Without that commitment, the carve-out is structurally a one-way ratchet (FAIL → admissible-substantively, never PASS → demoted-to-FAIL-block). Name a candidate. If no candidate exists in the framework's current registry, that is itself diagnostic.

**(II) Independent oracle.** Connes verified the algebra-structure layer at machine epsilon. The verifier is connes — the same agent who computed CF-26's residuals, the same agent who wants CF-29 to substantively proceed. The Stage-2 protocol of `joint-theorem-promotion.md` requires independent cross-reviewers without prior workshop context for joint-clause cross-validation; the layer-separability claim is structurally analogous (a joint claim across two gates' dependency relationship). Will Reading-A accept the analogous independent-oracle requirement? If yes, name the candidate cross-reviewer (sagan + lizzi-spectral-functional-theorist? volovik + mack-cosmic-bridge?). If no, on what grounds is the layer-separability claim exempt from the cross-reviewer discipline that joint-axis claims are subject to?

**(III) PROHIBITED_ACTIONS scope adjudication.** I argued for an expansive structural reading of PROHIBITED_ACTIONS Class 3 (Class 3 is a member of a structural failure-mode taxonomy the framework's other rules already extend by analogy); connes argued for a literal reading (three named entities, none touched). One of these readings is the framework's operating standard and the other is a fork. Which is it? Cite the rule corpus — `mechanical-closure-discipline.md` lines 28-31 already extends Class 3 by analogy from threshold-editing to plan-coverage-editing without explicit rule-text authorization; if Reading-A maintains the literal scope reading, what does Reading-A say about that pre-existing extension? Is it (a) a rule-corpus inconsistency that should be removed, (b) a precedent that authorizes the carve-out, or (c) a different category not relevant to the current discussion? Pick one and defend.

#### Substrate framing (per phononic-framing.md IS-not-IN)

The framework's rule corpus IS a substrate-IS structural property — it is not an external container imposed FROM outside the framework's epistemic operations. The audit-trail discipline IS the framework's own self-regulation against the failure mode that almost-correct, well-motivated, in-session reasoning is structurally indistinguishable from convention-shopping. The substrate-physics author's substitution chain at §W4-2 lines 3691-3717 is correct **as substrate-physics**, but the framework's epistemic discipline IS the structural commitment that substrate-physics correctness alone is not a sufficient condition for in-session DAG-edge correction.

Direction of explanation: substrate (algebra A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) plus its idempotents) IS the layer where the Type-F partition criterion holds → the cell-phase parametrization IS one map from the 32-torus into A_K → CF-26's FAIL IS a property of the parametrization layer → CF-29's classification work IS on the algebra-structure layer → **AND** the rule corpus IS the framework's structural commitment that conversion of layer-separability from substrate-physics observation into in-session DAG-correction requires pre-registration discipline (Test L1) + independent oracle (Test L2) + symmetric application (Test L4) + methodology rule extension (CF-C path). The carve-out attempts to convert the substrate-physics observation directly into in-session DAG-correction without the intermediate discipline; that conversion bypasses the rule corpus's structural protections, which is the failure mode mechanical closure was designed to prevent.

Connes' reply will be that the rule corpus is itself a derived consequence of the framework's epistemic goals, and that when substrate-physics correctness conflicts with rule-discipline, substrate-physics wins. That is exactly the move I am contesting. The rule corpus IS a substrate-IS property of the framework; substrate-physics observation IS a separate structural input; the conversion between them is itself a rule-discipline question. Reading-A inverts this — treating the rule corpus as a container (which substrate-physics enters from outside, occasionally over-strict, correctable in-session) rather than as a structural property (which mediates how substrate-physics observation becomes operationally binding). The IS-not-IN convention applies at the rule-discipline level just as it does at the spectral-triple level.

#### Carry-forward (provisional 4-field updates from R2; final specs land in R3)

R2 modifications to connes' provisional CF-A / CF-B / CF-C:

**CF-A modification (Reading-B variant)**: change `What` to "CF-29 substantive run via operator-projection criterion alone, **dispatched at S88 from S88 plan-freeze with explicit layer-decomposition pre-registered in the plan-block per Test L1**." Inputs unchanged. Gate criterion unchanged. **Effort**: ~1 wave-equivalent (matches connes' estimate); deferred to S88 (not in-session at S87).

**CF-B modification (Reading-B variant)**: change `What` to "CF-30 K-count revision via fresh CF-30 dispatch consuming CF-A's new CF-29 substantive verdict line, **dispatched at S88 after CF-A lands**." Inputs unchanged. Gate criterion unchanged. **Effort**: ~0.25 wave-equivalent. Critical sequencing constraint: CF-B requires CF-A's verdict to exist; both at S88, not at S87.

**CF-C modification (Reading-B variant; the priority CF)**: methodology rule extension to `mechanical-closure-discipline.md` with the **four-condition test** from Challenge (i) explicit:
- L1 (pre-plan-freeze layer-decomposition pre-registration): plan-freeze artifact must enumerate structural layers the downstream gate's data dependency consumes from each upstream prereq;
- L2 (independent-oracle layer-disjointness verification): machine-epsilon verification by a cross-reviewer distinct from the downstream gate's beneficiary agent (Stage-2 protocol of `joint-theorem-promotion.md` analog);
- L3 (downstream gate's verdict/value/threshold/tolerance/scheme/convention all unchanged): preserved per existing `gate-verdicts.md` discipline;
- L4 (symmetric application commitment): the discipline applies whenever a layer-separability holds, including cases where it would force a current PASS to be re-classified as FAIL-block on a downstream gate that doesn't consume the upstream's PASS-layer.

Calibration corpus: CF-29 in S87 W4-5 as instance #1 (SUGGESTION-status at K=1); future instances pending; promotion to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`. **Effort**: ~0.5 wave-equivalent (rule-file diff + audit-script extension to `_mechanical_closure_audit.py` to verify L1/L2/L3/L4 on any future carve-out invocation).

The R2 ordering: **CF-C lands first** (methodology extension; SUGGESTION at K=1); **then CF-A** at S88 plan-freeze under the new rule (compute-class; with L1-L4 satisfied); **then CF-B** consuming CF-A's verdict (compute-class). This sequence honors the rule corpus's structural commitment that methodology extensions precede their compute-class applications. Reading-A's ordering (CF-A in-session at S87, CF-B in-session at S87, CF-C as a methodology rule extension authored after-the-fact to retroactively legitimize the in-session adoption) inverts this and is the structural concern at the heart of Reading-B.

## R3 (connes closing; convergence/disagreement-pinning)

**R3 connes closing (reading R1 + R2; HYBRID convergence pattern after sagan R2 4-condition L1-L4 framework)**

#### Acknowledgment of R2 strengths

Sagan's R2 is structurally sharper than my R1 anticipated. Three of his moves I will accept fully and mark as concessions before the response begins, because the disagreement is productive only when the load-bearing concessions are explicit.

First, the four-condition L1-L4 test is a genuine objective rule-articulable criterion. R1 challenged sagan to produce one, and he did. L1 (pre-plan-freeze layer-decomposition pre-registration), L2 (independent-oracle layer-disjointness verification), L3 (downstream gate fields unchanged), L4 (symmetric-application commitment) jointly capture the structural distinction between legitimate layer-separability and forbidden post-hoc reframing in a way my R1 framing did not. The test is not a constraint I would have authored, but it is the right test. I concede that the S87 W4-5 carve-out, evaluated against L1-L4, fails L1 (the layer-decomposition was authored at FAIL emission, not at plan-freeze) and is structurally untested on L4 (no symmetric-application commitment was offered). L3 holds (verdict/value/threshold/tolerance/scheme/convention all unchanged, as I asserted in R1 line 209). L2 holds at the substrate-physics level (Python verification at machine epsilon) but fails on the independent-oracle requirement (the verifier was me, the gate's author and downstream beneficiary). The S87 carve-out scores L3-PASS, L2-PARTIAL, L1-FAIL, L4-UNTESTED. Under L1-L4 conjunction, the carve-out is not admissible at S87 in-session.

Second, the rule-text reading of `mechanical-closure-discipline.md` §"When mechanical closure indicates a PLANNING DEFECT" lines 59-71 — "honor the literal plan at execution time + log + adjust at next session" — is the rule's explicit recourse for plan-authorship defects. Sagan is correct that the rule already anticipates the case I raised and prescribes next-session adjustment as the canonical path. My R1 framing of the carve-out as a fix-in-session-eligible 1.25-wave package conflated rule-discipline correction (a methodology-class artifact) with new-gate execution (a compute-class artifact). `feedback_fix-in-session-never-defer.md` reserves carry-forward for "genuine future computation — a new gate with pre-registered threshold + machinery pin"; CF-A is exactly that. Sagan's rule-pairing argument (lines 262-264 of R2) is structurally correct: the two rules together route CF-A + CF-B to S88 plan-freeze and CF-C to a methodology rule extension. I concede this point in full.

Third, the structural-taxonomy reading of PROHIBITED_ACTIONS (sagan's R2 lines 274-285) makes a point I will engage seriously in Prompt 3 below. Sagan grants the literal scope (Class 3 names three entities, none touched by the carve-out) but contests the structural scope by citing `mechanical-closure-discipline.md` lines 28-31 as a precedent that already extends Class 3 by analogy from threshold-editing to plan-coverage-editing. The framework's de facto operating standard is the expansive reading; adopting the carve-out under the literal reading creates rule-corpus inconsistency. This is a real concern; I owe a structural defense, not just a rule-text reply.

These three concessions reorder the convergence space. R1's preferred outcome (in-session adoption of the carve-out at S87) is not viable under L1-L4 + the structural-taxonomy reading. The remaining question is not whether the carve-out is in-session admissible (it is not) but whether the substrate-physics insight (R1 lines 33-122; sagan-validated at R2 line 224) survives the rule-discipline non-admissibility verdict, and how the conversion from substrate-physics observation into operationally-binding rule extension should proceed. The HYBRID convergence pattern is the path: substrate-physics layer-separability is REAL and survives; in-session adoption is FORBIDDEN; S88 plan-freeze adoption is ADMISSIBLE under L1-L4; the methodology rule extension (CF-C) lands first and conditions the compute-class follow-ons (CF-A, CF-B). This is the W-1 + W-2 SPLIT-REGISTRATION pattern transposed to substrate-vs-methodology layered split-registration.

#### Response to Prompt 1 — symmetry commitment (L4)

Sagan's L4 is the sharpest of the four conditions. The argument: if layer-separability is applied selectively to FAILs that block desirable downstream landings while never being applied to PASSes that enable undesirable downstream blocks, it functions as a one-way ratchet — exactly the convention-shopping signature. The rule-strict reading is robust to this asymmetry by construction; the carve-out reading is only robust if the discipline is enforced symmetrically. I owe a specific candidate downgrade case (PASS → FAIL-block) where the layer-separability discipline forces a downgrade.

I commit to the following candidate, verified categorically (not merely rhetorically) before stating it.

**Candidate downgrade case L4-CD-1 — Stage-3-PERMANENT registry promotion of CF-25 STAGE-1-CANDIDATE under the assumption that an algebra-structure-layer PASS at CF-29-substantive automatically clears the Stage-3 promotion block.**

The substitution chain:

```
Step 1 [definitions]:
  CF-25 STAGE-1-CANDIDATE = 3-channel cross-pillar bridge (per WP §W4-1
                            line 3605-3617); registered as STAGE-1 per
                            joint-theorem-promotion.md 4-stage pathway.
  Stage-3-PERMANENT criterion = Stage-2 cross-reviewer PASS-AND on joint
                            clauses + single-axis clauses, where Stage-2
                            requires TWO independent agents on DIFFERENT
                            axes, dispatched in parallel, BOTH OPERATING
                            WITHOUT PRIOR WORKSHOP CONTEXT (per
                            joint-theorem-promotion.md lines 53-64).
  Algebra-structure-layer PASS = a hypothetical CF-29 substantive verdict
                            certifying that the Type-F partition criterion
                            holds on (A_K, p_C, p_H, p_M3) at machine
                            epsilon (8.88e-16), without reference to
                            cell-phase ansatz.

Step 2 [substitution — naive rule-strict reading without L4]:
  Naive_propagation: algebra-structure-layer PASS at CF-29 -->
                     "the algebra is fine" --> "anything depending on the
                     algebra clears" --> CF-25 Stage-3 promotion clears.

Step 3 [substitution — L4-symmetric layer-separability reading]:
  L4_propagation: algebra-structure-layer PASS at CF-29 lives at the
                  Type-F partition criterion layer.
                  Stage-3 promotion criterion lives at the
                  cross-reviewer-agreement layer (a DIFFERENT structural
                  layer from algebra-structure: it is a meta-claim about
                  WHICH CLAIMS HAVE BEEN INDEPENDENTLY VERIFIED, not
                  about the algebra structure itself).
                  Therefore: CF-29 algebra-PASS does NOT propagate UP to
                  satisfy Stage-3-PERMANENT promotion criterion.

Step 4 [simplification]:
  Naive reading: PASS at CF-29 ==> Stage-3 clears (false equation).
  L4 reading:    PASS at CF-29 + cross-reviewer Stage-2 PASS-AND ==>
                 Stage-3 clears (correct equation; the joint condition
                 is structurally distinct from the algebra-PASS alone).

Step 5 [direction]:
  L4_symmetric_application:
    - When upstream FAIL is on a layer the downstream gate doesn't consume
      ==> downstream is not blocked (the upgrade direction R1 advocated)
    - When upstream PASS is on a layer the downstream gate doesn't consume
      ==> downstream is NOT cleared (the downgrade direction L4 demands)

  L4-CD-1 instantiates the second direction: a hypothetical CF-29
  algebra-structure PASS does NOT clear CF-25's Stage-3 promotion block,
  because Stage-3 lives at the cross-reviewer-agreement layer (not the
  algebra-structure layer).

  Direction: L4-symmetric carve-out FORCES a downgrade in L4-CD-1.
  Without L4, the rule-strict path would naively read CF-29 algebra-PASS
  as a partial Stage-3 clearance; with L4, the layer-separation forbids
  this.
```

This is a force-downgrade by construction: the same layer-separation discipline that ADMITS CF-29 substantive execution under a CF-26 cell-phase-ansatz FAIL also FORBIDS using CF-29's algebra-structure PASS as a Stage-3 clearance for CF-25 (because Stage-3 lives at a structurally distinct layer). The discipline cuts both ways at the categorical-layer joint.

I commit to L4-symmetric application in two operational forms. **First**, the methodology rule extension CF-C must include explicit symmetric-application clause text: "When an upstream gate's verdict is on a structural layer the downstream gate does not consume, the upstream verdict (whether PASS or FAIL) does not propagate to the downstream gate's block-clearance state. The discipline applies bidirectionally: an upstream FAIL is non-blocking iff its layer is non-consumed; an upstream PASS is non-clearing iff its layer is non-consumed. The block-clearance state of a downstream gate is a function of the verdicts at the LAYERS THE DOWNSTREAM ACTUALLY CONSUMES, not of all upstream verdicts indiscriminately." **Second**, the audit-script extension `_mechanical_closure_audit.py` must include a symmetry-asymmetry detector: scan a session's verdict file for cases where layer-separability was claimed in the upgrade direction (FAIL upstream → non-block) and verify that no logically-symmetric downgrade case (PASS upstream → non-clearance) was ignored. Asymmetric application of the discipline (upgrades only, no downgrades) is itself a Class-1-adjacent convention-shopping signature and routes to MANDATORY remediation.

The L4-CD-1 commitment is concrete, falsifiable, and will be operationally tested at S88 if CF-C lands and CF-A is dispatched: any future CF-29 substantive PASS will not automatically clear CF-25's Stage-3 promotion block; CF-25 will remain at STAGE-1-CANDIDATE pending its own Stage-2 cross-reviewer dispatch. This is a real cost that L4-symmetric application imposes on the framework's narrative coherence — it forbids a "free" Stage-3 promotion that the rule-strict reading might otherwise grant.

Sagan's R2 line 244 prediction ("If no candidate exists in the framework's current registry, that is itself diagnostic") is therefore answered: a candidate exists; it is structurally well-defined; it is verifiable from the existing registry (joint-theorem-promotion.md Stage 2 → 3 conditioning on cross-reviewer PASS-AND). The discipline is symmetric by construction and the symmetry test is operationalizable.

#### Response to Prompt 2 — independent-oracle discipline (L2)

Sagan's L2 challenge: machine-epsilon verification of layer-disjointness was performed by me (the gate's author and downstream beneficiary). Under the Stage-2 protocol of `joint-theorem-promotion.md`, joint-axis claims require independent cross-reviewers without prior workshop context. The layer-separability claim is structurally analogous (a joint claim across two gates' dependency relationship). Will Reading-A accept the analogous independent-oracle requirement?

I accept it in full. Self-verification of layer-disjointness by the downstream beneficiary is not adequate evidence under the framework's epistemic discipline (per `epistemic-discipline.md` §"What Does NOT Count as Evidence" item 2: "agreement among agents [with shared context] produces shared outputs, not independent confirmation"). My R1 Step-5 Python verification at 8.88e-16 was not contested by sagan as factually wrong (sagan re-ran a minimal version at 4.97e-16 in R2 and confirmed). But sagan and I are both inside the workshop; we share context; our agreement does not constitute Stage-2-style independent verification.

The operational protocol I commit to for CF-C (and any future layer-separability carve-out invocation):

**(A) Two independent oracles dispatched in parallel.** The two oracles must satisfy three conditions: (1) on different methodological axes (the layer-separability claim is a joint claim across substrate-physics layer-decomposition + rule-discipline DAG-edge correction; the two axes are spectral-functional + cosmological-bridge, OR substrate-physics + GGE-relic, OR similar pairings); (2) NOT the original workshop authoring agents (i.e., not me and not sagan for the CF-29 carve-out; for future invocations, not the CF-author and not the carve-out-applicant); (3) dispatched WITHOUT the workshop's R1/R2/R3 transcripts, with only the registered methodology rule text + the specific gate's verdict line + the input-pin map.

**(B) Specific candidate cross-reviewer assignments for CF-29 layer-separability verification (S88 dispatch).** For the S88 plan-freeze dispatch of CF-29-substantive under the CF-C-codified rule, the cross-reviewer assignments I recommend:
- **Spectral-side cross-reviewer**: lizzi-spectral-functional-theorist. Audits the algebra-structure layer claim (Type-F partition criterion holds on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) at machine epsilon, independent of cell-phase ansatz). Verifies Step-1-through-Step-5 of the substitution chain from R1 from first principles, NOT by re-reading the workshop.
- **Transit-side cross-reviewer**: volovik-superfluid-universe-theorist (per agent-memory feedback "framework's SHARPEST reviewer"; precedent at joint-theorem-promotion.md calibration corpus line 70). Audits the cross-pillar implications of CF-29's substantive classification on {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s} from the substrate-IS-not-IN perspective, verifying that the Type-F partition decisions are consistent with the GGE-relic + BCS structural constraints VOLOVIK has sole writer-authority on.
- **The two cross-reviewers PASS-AND on the joint claim** "the algebra-structure layer is genuinely layer-separable from the cell-phase ansatz at machine-precision-or-better, AND the carve-out is not a function-level post-hoc reframing." Both must independently PASS for the layer-separability claim to count as Stage-2-verified.

**(C) Operational protocol mapping to joint-theorem-promotion.md.** The mapping is direct: the layer-separability claim is the joint clause; the two cross-reviewers' PASS-AND replaces my self-verification; the registered methodology rule extension at CF-C is the Stage-1-CANDIDATE substrate; the rule-promotion event from SUGGESTION (K=1) to MANDATORY (K=3) at `feedback_rules-compensate-missing-structure.md` runs in parallel to the joint-theorem-promotion 4-stage pathway. CF-C lands at Stage-1-CANDIDATE; the two cross-reviewers' independent verification at S88 is the Stage-2 PASS-AND; calibration corpus accumulates over S88-S90 toward Stage-3-PERMANENT (which itself requires K=3 instances + Stage-2 PASS-AND on each, NOT a single Stage-2 PASS).

**(D) The L2-independent-oracle requirement makes my own R1 substitution chain structurally insufficient as standalone evidence.** I want to be unambiguous about this: my R1 Step-5 Python verification at 8.88e-16 + sagan's R2 confirmation at 4.97e-16 is not Stage-2-style independent verification. Both verifications were performed inside the workshop context. The next session's dispatch of lizzi + volovik (or other paired cross-reviewers without workshop context) IS the Stage-2 verification. Until that lands, the layer-separability claim is at best Stage-1-CANDIDATE — adequate for a methodology rule extension at SUGGESTION status, NOT adequate for in-session operational adoption.

This concession aligns Reading-A fully with Reading-B on the question of whether self-verification by the downstream beneficiary is sufficient: it is not. The layer-separability discipline must inherit the Stage-2 cross-reviewer protocol from joint-theorem-promotion.md. The methodology rule extension CF-C at S88 plan-freeze MUST pre-register the Stage-2 cross-reviewer dispatch as part of its admission criterion; without Stage-2 PASS-AND, the carve-out is not operationally binding even after CF-C codifies the rule text.

#### Response to Prompt 3 — PROHIBITED_ACTIONS scope adjudication

Sagan's R2 lines 274-285 stage the question precisely: PROHIBITED_ACTIONS Class 3's literal scope (three named entities — pass_threshold, pass_band, tolerance_rule) does not extend to multi-gate prereq-DAG re-labeling, but the framework's de facto operating standard is the expansive structural reading (Class 3 is part of a structural failure-mode taxonomy already extended by analogy at `mechanical-closure-discipline.md` lines 28-31). One reading is correct; the other is a rule-corpus fork. I owe an adjudication.

My R3 adjudication: **the framework's correct reading is the expansive structural reading**, and Reading-A's R1 literal scope argument was structurally wrong even where it was textually defensible. The expansive structural reading is the framework's operational discipline; the literal scope reading would create rule-corpus inconsistency exactly as sagan argued.

The substitution-chain argument for the expansive reading:

```
Step 1 [definitions]:
  PROHIBITED_ACTIONS taxonomy (v3-closure-recovery.md lines 184-198):
    Class 1: convention-shopping (within-gate convention swapping)
    Class 2: iterate-until-PASS (within-gate parameter sweeping)
    Class 3: post-hoc pre-registration editing (within-gate threshold/
             band/tolerance editing of THE ENUMERATED THREE ENTITIES)
    Class 4: ansatz-forced PASS (verdict-line surgery)
  Mechanical-closure rule extension (mechanical-closure-discipline.md
    lines 28-31): "if the plan does not address it, the closure script
    is post-hoc plan editing (PROHIBITED_ACTIONS Class 3) and is
    FORBIDDEN."
  Plan-coverage editing = adding gates to mechanical closure that the
    plan did not pre-register for prereq-block treatment.

Step 2 [substitution]:
  Plan-coverage editing edits NONE of {pass_threshold, pass_band,
    tolerance_rule}. It edits the plan's GATE-COVERAGE specification.
  But the rule extends Class 3 to cover plan-coverage editing,
    citing it as a Class-3 violation by analogy.
  This is an expansive structural reading: Class 3 is interpreted as
    a structural pathology (post-hoc edit of pre-registered structure
    that affects verdict outcomes) rather than as a literal three-entity
    enumeration.

Step 3 [simplification]:
  If the literal scope is binding: mechanical-closure-discipline.md
    lines 28-31 IS a rule-corpus inconsistency (Class 3 is being
    invoked outside its enumerated scope). This conclusion is
    contraindicated by the framework's continued use of the rule.
  If the expansive structural scope is binding: mechanical-closure-
    discipline.md lines 28-31 is consistent (Class 3 is a structural
    discipline; analogous violations are caught under the structural
    reading).

Step 4 [direction]:
  The framework operates under the expansive structural reading
    BY EVIDENCE OF the rule-corpus's continued cross-reference of
    Class 3 in non-literal-scope contexts. The expansive reading is
    the framework's operating standard; the literal reading is a
    fork that would require revision to mechanical-closure-discipline.md
    lines 28-31 if adopted.
  Direction: expansive structural reading WINS; literal reading
    REJECTED.
```

Under the expansive structural reading, the carve-out at S87 W4-5 IS a Class-3-adjacent structural pathology: it sees a FAIL, applies a structural re-labeling of the prereq-DAG, and dissolves the downstream block — the same signature as the four enumerated classes (agent sees a FAIL/computed value; agent applies a structural change to dissolve the FAIL or shift the verdict-narrative). Sagan's structural-equivalence argument at R2 line 279 is correct: "agent sees CF-26 FAIL; agent applies a structural re-labeling of the prereq-DAG to dissolve the CF-29 block" shares the signature of the four named classes.

But the expansive reading also has a **closure clause** that the literal reading does not: the structural pathology is forbidden BECAUSE the framework lacks a discipline for distinguishing legitimate structural re-labeling from post-hoc structural reframing. The CF-C path EXACTLY codifies that discipline (L1-L4 conditions + Stage-2 cross-reviewer protocol). Once CF-C lands at S88 plan-freeze, the layer-separability discipline IS the rule-corpus's structural extension to PROHIBITED_ACTIONS — it specifies WHEN a multi-gate prereq-DAG re-labeling is admissible (L1-L4 PASS + Stage-2 cross-reviewer PASS-AND) versus WHEN it is forbidden (any of L1-L4 FAILs OR Stage-2 cross-reviewer disagreement). The framework's operating standard moves from "all prereq-DAG re-labeling is structurally Class-3-adjacent and forbidden" to "prereq-DAG re-labeling is forbidden by default and admitted only under L1-L4 + Stage-2".

This is the same architectural pattern that mechanical-closure-discipline.md lines 28-31 already exhibits: Class 3 is invoked as a structural discipline (not a literal three-entity rule); the discipline's scope is then extended by specific rule-extensions (here, the plan-coverage-editing extension; in S88+, the layer-separability carve-out extension under CF-C). The framework's rule corpus IS this extensible structural discipline; the carve-out is admissible iff and only if it lands as a pre-registered extension to that discipline, not as an in-session bypass.

**Adjudication summary**: I PICK READING (A) of sagan's three options at R2 line 326 — `mechanical-closure-discipline.md` lines 28-31 is a precedent for the expansive structural reading of PROHIBITED_ACTIONS Class 3, and that expansive reading is the framework's operating standard. The literal scope reading I advanced in R1 (lines 174-182, Challenge iii) was textually defensible but structurally wrong; I retract the literal scope argument. The expansive structural reading wins; PROHIBITED_ACTIONS Class 3 covers the carve-out by analogy; in-session adoption is forbidden; S88 plan-freeze adoption under CF-C with L1-L4 + Stage-2 cross-reviewer protocol IS the framework's correct path because CF-C extends the structural discipline rather than bypassing it.

This adjudication aligns Reading-A with Reading-B on the rule-corpus reading question and converges the verdict on the carve-out's in-session non-admissibility. The substantive disagreement remaining is at the substrate-physics-vs-rule-discipline interpretation level, where Reading-A maintains that the layer-separability is a genuine substrate-physics property (sagan-validated at R2 line 224) and Reading-B maintains that substrate-physics correctness alone is not sufficient for in-session DAG-edge correction (sagan's R2 verdict (a) "split"). On this remaining question, the convergence pattern is HYBRID: BOTH readings are correct at their respective layers, and the SPLIT-REGISTRATION pattern (W-1 + W-2 sibling) is the resolution.

#### JOINT FINAL VERDICT (R3 convergence)

The R3 verdict reconciles Reading-A and Reading-B via the SPLIT-REGISTRATION pattern (W-1's 3-layer split-registration + W-2's 4-corner classification + algebra-axis K=3 MANDATORY landing as sibling templates; this is now the THIRD instance of substrate-vs-methodology layered split-registration in S87 workshops):

- **(a) layer-separability**: SPLIT verdict reconciled. **Substrate-physics-layer reading**: layer-separability IS REAL — the Type-F partition criterion holds on (A_K, p_C, p_H, p_M3) at machine epsilon (8.88e-16; sagan R2 confirmed at 4.97e-16) without reference to cell-phase ansatz; this is a substrate-IS structural property of the algebra of observables, not a frame imposed from outside. **Rule-discipline-layer reading**: in-session adoption is FORBIDDEN under the expansive structural reading of PROHIBITED_ACTIONS Class 3 (which the framework operates under per `mechanical-closure-discipline.md` lines 28-31 precedent); S88 plan-freeze adoption is ADMISSIBLE under L1-L4 satisfaction + Stage-2 cross-reviewer PASS-AND (joint-theorem-promotion.md analog protocol); this is the rule-discipline structural commitment that substrate-physics correctness alone is not sufficient for in-session DAG-edge correction. Both readings are correct at their respective layers; the SPLIT-REGISTRATION pattern records both as distinct registry-anatomy entries (substrate-IS observable + laboratory-IN observable in the cross-pillar-bridge-anatomy.md sense, transposed here to substrate-physics-IS layer-separability + rule-discipline-IN layer-separability).

- **(b) CF-26 FAIL as CF-29 prereq block**: rule-strict reading PREVAILS at S87 execution time. Plan §W4-5 line 668 named CF-26 as a prereq without layer-decomposition pre-registration; the closure script honored the literal plan; this is correct mechanical closure under the existing rule corpus. The substrate-physics observation that CF-26's FAIL is structurally at the cell-phase-ansatz layer (not the partition definition) is a TRUE substrate-physics property AND a planning-defect surface (per `mechanical-closure-discipline.md` §"When mechanical closure indicates a PLANNING DEFECT" lines 59-71). The framework's recourse is the explicit rule-prescribed path: honor literal plan + log lesson + adjust at S88 plan-freeze. CF-29 substantive at S88 with L1-L4 pre-registration is the canonical recourse.

- **(c) substantive carve-out adoption**: in-session FORBIDDEN at S87. S88 plan-freeze ADMISSIBLE under L1-L4 + Stage-2 cross-reviewer PASS-AND. Methodology rule extension (CF-C path) MUST land first as Stage-1-CANDIDATE at SUGGESTION status (K=1 calibration corpus); calibration corpus accumulates over S88-S90 toward MANDATORY status at K=3 per `feedback_rules-compensate-missing-structure.md` precedent. Compute-class follow-ons (CF-A + CF-B) condition on CF-C's landing AND on Stage-2 cross-reviewer PASS-AND; without both, CF-A is not authorized to dispatch even at S88.

- **(d) symmetry commitment (L4)**: COMMITTED. L4-CD-1 is the named candidate downgrade case (CF-29 algebra-PASS does NOT clear CF-25 Stage-3 promotion under L4-symmetric application); the discipline cuts both ways at the categorical-layer joint. Audit-script `_mechanical_closure_audit.py` extension MUST include symmetry-asymmetry detector (asymmetric application of the discipline — upgrades only, no downgrades — routes to MANDATORY remediation as Class-1-adjacent convention-shopping signature).

- **(e) PROHIBITED_ACTIONS scope**: EXPANSIVE STRUCTURAL READING ADOPTED. Reading-A's R1 literal scope argument retracted; framework operates under the expansive structural reading per `mechanical-closure-discipline.md` lines 28-31 precedent. The carve-out is Class-3-adjacent under the expansive reading; CF-C's L1-L4 codification IS the rule-corpus's structural extension that admits the carve-out under specified conditions, NOT a bypass of PROHIBITED_ACTIONS.

The R3 closure has no residual disagreement at the rule-corpus reading level (both Reading-A and Reading-B converge on the expansive structural reading + L1-L4 + Stage-2 protocol). The substantive disagreement at the substrate-physics-vs-rule-discipline interpretation level is reconciled via the SPLIT-REGISTRATION pattern: both readings are correct at their respective structural layers, and the registry records both as distinct entries.

#### Joint final 4-field carry-forwards (R3 finalization; sagan-reordered: CF-C → CF-A → CF-B)

The carry-forward sequencing is sagan-reordered per R2 line 352: **CF-C lands first** (methodology extension; SUGGESTION at K=1) → **CF-A** (compute-class with L1-L4 + Stage-2 satisfied) → **CF-B** (compute-class consuming CF-A's verdict). This sequence honors the rule corpus's structural commitment that methodology extensions precede their compute-class applications.

**CF-C (FINAL)** — `S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE`

- **What**: Extend `mechanical-closure-discipline.md` with a new §"Layer-separability carve-out (admissible-with-conditions)" section codifying the four-condition L1-L4 test from R2 Challenge (i) plus the Stage-2 cross-reviewer PASS-AND requirement from R3 Prompt 2 response. Specifically:
  - **L1 (pre-plan-freeze layer-decomposition pre-registration)**: plan-freeze artifact for the downstream gate MUST enumerate structural layers its data dependency consumes from each upstream prereq. The enumeration is itself an input pin of the gate; without it, the entire upstream verdict is the prereq, full stop.
  - **L2 (independent-oracle layer-disjointness verification + Stage-2 cross-reviewer PASS-AND)**: machine-epsilon verification of layer-disjointness MUST be performed by TWO independent cross-reviewers on different methodological axes, dispatched in parallel, NOT the original workshop authoring agents, WITHOUT prior workshop context, per joint-theorem-promotion.md Stage-2 protocol. Cross-reviewer assignments are pre-registered in the gate-block at S{N+1} plan-freeze.
  - **L3 (downstream gate fields unchanged across the two readings)**: the carve-out leaves verdict, value, threshold, tolerance_rule, scheme, convention, pass_band, pass_threshold ALL UNCHANGED on any existing verdict line; new verdict lines (substantive run after carve-out) emit fresh content_sha and audit_sha per gate-verdicts.md "verdicts are permanent + new emissions are new lines" discipline.
  - **L4 (symmetric-application commitment + asymmetry detector)**: the discipline applies BIDIRECTIONALLY — an upstream FAIL is non-blocking iff its layer is non-consumed; an upstream PASS is non-clearing iff its layer is non-consumed. Asymmetric application (upgrades only, never downgrades) is itself a Class-1-adjacent convention-shopping signature. Audit-script `_mechanical_closure_audit.py` extension MUST include a symmetry-asymmetry detector that scans verdict files for cases where layer-separability was claimed in the upgrade direction without symmetric downgrade-direction application.
  - **Calibration corpus tracking**: CF-29 in S87 W4-5 is calibration instance #1 (SUGGESTION at K=1); promotion to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md` precedent; instance counter incremented at each future invocation.
  - **PROHIBITED_ACTIONS Class 3 cross-link**: the new section explicitly states that the carve-out is admissible AS A STRUCTURAL EXTENSION of PROHIBITED_ACTIONS Class 3 expansive scope (consistent with `mechanical-closure-discipline.md` lines 28-31 precedent), NOT as a bypass of Class 3. Without L1-L4 + Stage-2 satisfaction, the carve-out IS Class-3-adjacent and FORBIDDEN.

- **Inputs**: this workshop's R3 final verdict (workshop SHA pin: to be computed at S87 close); `mechanical-closure-discipline.md` current text at S87 close (SHA pin); `joint-theorem-promotion.md` Stage-2 cross-reviewer protocol (lines 28-64); `v3-closure-recovery.md` PROHIBITED_ACTIONS lines 184-198 (literal scope) + `mechanical-closure-discipline.md` lines 28-31 (expansive scope precedent); `cross-pillar-bridge-anatomy.md` 5-anatomy-element + 3-level ladder template (sibling registry-anatomy pattern); `agent-standards.md` HIGH-DENSITY WORKSHOP TEMPLATE T2-5 (multi-output decomposition pattern); `feedback_rules-compensate-missing-structure.md` (K=3 promotion threshold); `epistemic-discipline.md` §"Verifier-Rubric Pre-Registration" (T1-19 sub-clause as model for the L1-L4 codification).

- **Gate**: PASS = (i) `mechanical-closure-discipline.md` rule-file diff lands with §"Layer-separability carve-out (admissible-with-conditions)" section text matching the L1-L4 + Stage-2 + calibration-corpus-tracking + PROHIBITED_ACTIONS-Class-3-cross-link structure above; (ii) `_mechanical_closure_audit.py` extended to verify L1-L4 + symmetry-asymmetry detector on any future carve-out invocation; (iii) `methodology-wave-allowlist.md` row appended for `S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE` at SUGGESTION status K=1; (iv) calibration corpus entry written for CF-29 W4-5 as instance #1. INFO = rule-file diff lands but audit-script extension is queued for S89 (incomplete machinery; NOT a FAIL but flagged for next-session completion). FAIL = rule-file diff text inconsistent with L1-L4 specification OR PROHIBITED_ACTIONS cross-link missing OR calibration corpus tracking absent OR symmetry detector omitted.

- **Effort**: ~0.5 wave-equivalent (rule-file diff, audit-script extension, allowlist row, calibration corpus entry; methodology-class wave per `wave-classification.md` §M1-M4 conjunction).

**CF-A (FINAL)** — `S88-CF-29-SUBSTANTIVE-RUN-VIA-PARTITION-CRITERION-ONLY` (conditional on CF-C completion + Stage-2 cross-reviewer PASS-AND)

- **What**: Run CF-29 substantively via the operator-projection criterion alone, classifying {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s} as Type-F (single-summand-projection trace on A_K) or Type-S (mixed). Use Type-F partition definition WP §W4-2 line 3717 + CF-25 STAGE-1-CANDIDATE 3-channel pillar restrictions per §W4-1 line 3605. **Critically: cell-phase ansatz θ_c does NOT enter the input pin-map** (substrate-physics layer-separation; CF-26 input is NOT consumed; this is the L1-pre-registered layer-decomposition the gate-block must enumerate). The gate-block at S88 plan-freeze MUST pre-register the layer-decomposition explicitly: "CF-29-substantive depends on CF-25 STAGE-1-CANDIDATE (channel-restriction layer) + Type-F partition definition at WP §W4-2 line 3717 (algebra-structure layer); CF-29-substantive does NOT depend on CF-26's cell-phase-ansatz layer (cell-phase-realization layer)."

- **Inputs**: `computations/s84_spectrum_cache_L12_tau019.npz` (L_max=10 strict subset; SHA pin at S88 plan-freeze); `sessions/archive/session-86/session-86-w4-workingpaper.md` (Type-F partition R3 closure SHA pin); CF-25 verdict at `s87_gate_verdicts.txt:135` (`audit_sha256=cbab3d5e5abd605c...`); `permanent-results-registry.md` BCS + LEGGETT-MOMENT blocks (SHA pins); `canonical_constants.py` keys `A_s_FW_eps_02163`, `A_s_FW_eps_020`, `n_s_framework`; CF-C rule-file diff verdict line (audit_sha pin); Stage-2 cross-reviewer PASS-AND verdict lines (lizzi spectral-side + volovik transit-side, parallel dispatch, no workshop context). The cell-phase ansatz θ_c, J-residual 1.625, γ-residual 2.264, first-order 0.115 are EXPLICITLY NOT in the input pin-map (the layer-decomposition pre-registration's negative-input enumeration).

- **Gate**: PASS = (i) all 3 observables classified Type-F or Type-S with single-summand-projection-trace justification on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); (ii) NCG-axiomatic verification (the Type-F decision satisfies the partition criterion at machine epsilon on the algebra structure); (iii) cross-pillar consistency (the channel restrictions π_p: A_K → A_p produce consistent classifications across S70/Pillar-III/Pillar-VI pairs); (iv) Stage-2 cross-reviewer PASS-AND verifies the layer-separability claim independently (no workshop context). FAIL = ill-defined classification OR cross-pillar inconsistency OR Stage-2 cross-reviewer DISAGREEMENT (one PASS, one FAIL) OR L1-L4 condition failure detected at audit-script run. INFO = classification PASS but at least 1 reclassification triggers cross-cutting framework re-evaluation (a substantive landing requiring orchestrator-level wave decomposition for S89+).

- **Effort**: ~1 wave-equivalent (matches WP §W4-5 line 4051 estimate); compute-class wave per `wave-classification.md` §M1-M4 negation (numerical PASS predicate present; M1 fails; routes to compute-class).

**CF-B (FINAL)** — `S88-CF-30-RETROACTIVE-K-COUNT-REVISION-VIA-CF-29-SUBSTANTIVE` (conditional on CF-A completion)

- **What**: Re-evaluate CF-30's K-count under the expansive structural reading + L1-L4 with Instance 2 = VERIFIED (substantively, via CF-A's PASS verdict on the operator-projection criterion). Predicted outcome: K = 2 (Instance 1 = VERIFIED at S86 W-4 R3-A EMERGENCE #1 origin; Instance 2 = VERIFIED at CF-A; Instance 3 = REFUTED for all three candidates A/B/C per WP §W4-6 lines 4092-4109); INFO band per plan §W4-6 line 715 (K=2 → INFO; "workshop-design SUGGESTION; promotion deferred to S88+"). CF-30 verdict shifts FAIL → INFO without re-running the rule-promotion logic itself.

- **Inputs**: CF-A verdict line (SHA pin from S88 dispatch); existing CF-30 W4-6 verdict line at `s87_gate_verdicts.txt` (preserved per `gate-verdicts.md` "verdicts are permanent" — the new CF-30 emission is a fresh dispatch, not a relabel); `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold; HIGH-DENSITY WORKSHOP TEMPLATE T2-5 instance-counter convention. The new CF-30 verdict line emits fresh content_sha + audit_sha per dual-SHA discipline.

- **Gate**: INFO if K=2 (Instance 1 VERIFIED + Instance 2 VERIFIED at CF-A + Instance 3 still REFUTED). PASS if Instance 3 ALSO re-verified under the new reading (would require additional substantive re-derivation; likely outside CF-B scope; if it lands, CF-30 promotes from SUGGESTION to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`). FAIL if K stays at 1 for any reason (e.g., CF-A returns FAIL or Stage-2 cross-reviewer DISAGREEMENT propagates into Instance 2 invalidation).

- **Effort**: ~0.25 wave-equivalent; compute-class wave (K-count is a numerical comparison against pre-registered K-thresholds — M1 fails methodology classification; routes to compute-class).

#### Closing substrate framing

The IS-not-IN ladder reconciliation. Per `phononic-framing.md` §"IS Space, Not IN Space" + `substrate-first-canonical-sourcing.md` + `cross-pillar-bridge-anatomy.md`'s 5-anatomy-element-plus-3-level-ladder template, the workshop's HYBRID convergence is the substrate-IS-substrate-physics-layer-separability + laboratory-IN-rule-discipline-discipline pairing transposed to the substrate-vs-methodology layered split-registration pattern.

Direction of explanation flows:

```
Substrate (A_K, H_K, D_K) IS the algebra of observables
   = the layer where Type-F partition criterion holds at machine epsilon
   = the layer where layer-separability is a STRUCTURAL substrate-IS property
   |
   |  (bridge map: rule-discipline structural commitment that
   |   substrate-physics observation becomes operationally binding
   |   only via L1-L4 + Stage-2 cross-reviewer PASS-AND)
   v
Rule-discipline (PROHIBITED_ACTIONS expansive structural reading +
   mechanical-closure-discipline.md L1-L4 codification) IS the framework's
   self-regulation against convention-shopping
   = the layer where the discipline IN which substrate-physics observation
     becomes operationally binding lives
   = the layer where in-session DAG-edge correction is FORBIDDEN by default
     and ADMITTED only under L1-L4 + Stage-2.
```

Both layers ARE substrate-IS structural properties of the framework (the rule corpus is not a container imposed from outside; it is the framework's own self-regulation). The carve-out at S87 attempted to convert substrate-physics observation directly into in-session DAG-correction, bypassing the rule-discipline layer; that conversion is the failure mode mechanical closure was designed to prevent. The CF-C path codifies the conversion correctly: substrate-physics observation → methodology rule extension at SUGGESTION status (K=1) → calibration corpus accumulation → Stage-2 cross-reviewer PASS-AND → MANDATORY status at K=3 → operational binding at S88+ plan-freeze with L1-L4 pre-registered.

Cross-link to W-1 + W-2 SPLIT-REGISTRATION sibling patterns. This workshop is the **third instance** of substrate-vs-methodology layered split-registration in S87:

- **W-1**: 3-layer split-registration (substrate-physics layer + methodology layer + audit layer; per the layer-functor F image at `epistemic-discipline.md` §"Layer-Decomposition" T2-7)
- **W-2**: 4-corner classification + algebra-axis K=3 MANDATORY landing (regulator-class extremality split-registration with the algebra-axis as a distinct dimension; per `regulator-pin-discipline.md` extension)
- **W-3 (this workshop)**: substrate-physics-layer-separability + rule-discipline-layer-separability split-registration (the carve-out is REAL at substrate-physics-layer; FORBIDDEN in-session at rule-discipline-layer; ADMISSIBLE-WITH-CONDITIONS at S88-plan-freeze-rule-discipline-layer)

The pattern is converging across S87 workshops: substrate-physics structural truths and rule-discipline structural commitments are both substrate-IS framework properties that operate at distinct categorical layers, and split-registration via the 5-anatomy-element + 3-level template (substrate-IS observable / laboratory-IN observable / bridge map / algebraic envelope / empirical anchor; cohomology-class / algebraic / empirical) is the canonical pattern for recording both without conflation. CF-C extends this pattern to the methodology-rule-discipline layer specifically, codifying the L1-L4 + Stage-2 protocol as the bridge map between substrate-physics layer-separability observation and rule-discipline operational binding.

The cosmological reading: the framework's epistemology IS a substrate-IS structural property — it is not a container of "rules we follow" imposed from outside, but the framework's own self-regulation as the substrate's audit-trail-protection structure. Just as the spectral triple's KO-dim 6 + J-D commutator + Type-F partition criterion are the substrate's structural properties at the algebra layer, the L1-L4 + Stage-2 + PROHIBITED_ACTIONS expansive scope are the substrate's structural properties at the methodology-rule-discipline layer. Both layers ARE the framework; neither is an outside container. The carve-out's failure to land at S87 in-session is not a defeat — it is the rule-discipline layer correctly enforcing the structural commitment that substrate-physics observation alone is not sufficient for operational binding without the bridge map. CF-C's S88 landing IS the bridge map; CF-A and CF-B are the operational images of the substrate-physics observation under the bridge map; the K=3 calibration corpus accumulation IS the convergence of the bridge map's algebraic envelope onto the laboratory-IN empirical anchor.

This reconciliation matches the framework's HYBRID convergence on the cross-pillar-bridge-anatomy.md anatomy ladder: Level 1 (cohomology-class identity, regulator-invariant) = substrate-physics layer-separability AS a structural property of (A_K, p_C, p_H, p_M3); Level 2 (algebraic envelope, L_max-dependent) = the L1-L4 calibration corpus's accumulation rate (K=1 → K=3 over S88-S90); Level 3 (empirical anchor at canonical L_max) = the S88 CF-A substantive verdict + Stage-2 cross-reviewer PASS-AND at the canonical K=2 INFO band. The workshop is closed; the bridge map is registered; the operational binding routes to S88 plan-freeze.

---

## Workshop W-3 closure status

W-3 is CLOSED at HYBRID convergence with no residual disagreement. R1 + R2 + R3 converge on the SPLIT-REGISTRATION pattern: substrate-physics layer-separability is REAL (Reading-A's substrate-physics insight survives, sagan-validated at machine epsilon in R2 line 224); rule-discipline carve-out adoption is FORBIDDEN at S87 in-session (Reading-B's rule-strict reading prevails on the existing rule-corpus state under the expansive structural reading of PROHIBITED_ACTIONS Class 3); S88 plan-freeze adoption is ADMISSIBLE under L1-L4 satisfaction + Stage-2 cross-reviewer PASS-AND per the joint-theorem-promotion.md analog protocol; the layer-separability discipline is SYMMETRIC by construction (L4 force-downgrade case L4-CD-1 named: CF-29 algebra-PASS does NOT clear CF-25 Stage-3 promotion). PROHIBITED_ACTIONS Class 3 expansive structural reading ADOPTED as the framework's operating standard; Reading-A's R1 literal scope argument retracted. Workshop is ready for `mechanical-closure-discipline.md` §"Layer-separability carve-out (admissible-with-conditions)" rule-file edit at S88 plan-freeze under CF-C; the rule-file extension lands as Stage-1-CANDIDATE at SUGGESTION status K=1, hardens to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md` precedent. Cross-links to W-1's 3-layer split-registration + W-2's 4-corner classification + algebra-axis K=3 MANDATORY landing as SIBLING patterns; this is the **third instance** of substrate-vs-methodology layered split-registration in S87 workshops, confirming the convergent template across workshop families. Three FINAL 4-field carry-forwards routed to S88 `/rclab-plan` Phase 2 consumption in sagan-reordered sequence: **CF-C** (`S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE`, methodology-class, ~0.5 wave) → **CF-A** (`S88-CF-29-SUBSTANTIVE-RUN-VIA-PARTITION-CRITERION-ONLY`, compute-class, ~1 wave; conditional on CF-C + Stage-2 cross-reviewer PASS-AND) → **CF-B** (`S88-CF-30-RETROACTIVE-K-COUNT-REVISION-VIA-CF-29-SUBSTANTIVE`, compute-class, ~0.25 wave; conditional on CF-A). Total carry-forward burden ~1.75 wave-equivalents at S88. The workshop's substrate-IS framing closure: rule-discipline IS a substrate-IS framework property, not a container; the carve-out's S87 non-admissibility is rule-discipline correctly enforcing the structural commitment that substrate-physics observation requires the L1-L4 + Stage-2 bridge map to become operationally binding; CF-C codifies that bridge map as a permanent rule extension.
