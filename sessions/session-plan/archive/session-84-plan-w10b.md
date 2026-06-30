# Session 84 Plan — Wave 10b: Optional / Framework Audits (3 gates)

**Session**: 84
**Wave**: 10b (optional / lower-priority audits: biographical framing, α_s derivation chain, CMB-S4 joint-discriminator plane)
**Planner**: gen-physicist
**Date**: 2026-04-18
**Format**: compute (parallel independent agents)
**Scope**: Gates 122, 123, 124 from §4.M (optional / lower-priority)

---

## W10b Summary

Wave 10b executes the three lowest-priority but still pre-registerable audits carried forward from S83:

- **Gate 122 (BIOGRAPHICAL-FRAMING-AUDIT)**: re-audits the S83 R2 "corner-with-extensions" convergence under a biographical-framing-stripped prompt. Tests whether rhetorical alignment (not structural argument) drove the convergence observed in S83 gear-machine workshop. This is a methodological self-check on the framework's own internal review apparatus — specifically on the vulnerability that agents produced from similar research corpora may converge for reasons that have no bearing on the physics.

- **Gate 123 (ALPHA-S-DERIVATION-CHAIN-AUDIT)**: traces S50's permanent result α_s = n_s² - 1 from first principles to verify it derives from the minimal axiom set {CCM + KO-dim=6 + A_F-singleton + Mellin-kernel spectral action} without auxiliary assumptions. The gate is particularly load-bearing: α_s = -0.068968 is a high-σ discriminator (9.62σ vs Planck, 34.48σ projected vs CMB-S4) and underwrites S84-ALPHA-S-PRE-REGISTRATION (gate 7 in §4.A). A FAIL here — observational input of n_s itself feeding the derivation — would promote α_s from zero-free-parameter to circularity.

- **Gate 124 (CMB-S4-JOINT-DISCRIMINATOR-PLANE)**: formalizes the 5-axis joint discrimination table (n_T, α_s, M_KK, ALP-spectrum, frequency-comb) from S83 R2 into a pre-registered joint-Fisher computation. Outputs per-axis σ separations between framework and landscape competitors K1 (typical IIB slow-roll) and K2 (heterotic slow-roll with discrete flux).

Wave 10b is explicitly flagged as "optional / lower-priority" in the carry-forward table, but the three gates are distinct in character: 122 is an audit-methodology closure (post-hoc self-check), 123 is a derivation-integrity audit (mathematical structural check), and 124 is an observational-forecast consolidation (joint Fisher). None require GPU linear algebra; computational intensity is LOW to MEDIUM.

W10b runs in parallel with W10a (whose slice of §4.L audit-integrity items — SHA regeneration, GV-secondary classification, etc. — is separately specified). The two sub-waves are independent: no gate in W10b depends on any gate in W10a.

---

## W10b Decision Point Prerequisites

Before S84 close and carry-forward to S85, W10b outputs must include:

1. **Gate 122 (BIOGRAPHICAL-FRAMING-AUDIT) verdict**: binary survival fraction ∈ [0, 1] of S83 R2 claims under neutral-prompt re-audit. Tabulated claim-by-claim adjudication. PASS ≥ 0.80 survival, INFO 0.50–0.80, FAIL < 0.50. A FAIL triggers §VII-BIOGRAPHICAL-FRAMING caveat in the working paper and mandates prompt-neutral re-runs of corner-with-extensions discussions in S85.

2. **Gate 123 (ALPHA-S-DERIVATION-CHAIN-AUDIT) verdict**: structural classification of S50 derivation as PURE-MELLIN / MELLIN-PLUS-AUX / CIRCULAR. PASS if derivation traces to {CCM + KO-dim=6 + A_F-singleton + Mellin kernel} only; INFO if one auxiliary coupling relation is invoked; FAIL if n_s itself (observational) enters the derivation of α_s. The verdict is load-bearing for the S84-ALPHA-S-PRE-REGISTRATION gate 7 downstream — a FAIL here invalidates the 34σ CMB-S4 pre-registration.

3. **Gate 124 (CMB-S4-JOINT-DISCRIMINATOR-PLANE) verdict**: 5-axis joint-Fisher separation table with (framework vs K1) and (framework vs K2) σ-values per axis. PASS if ≥ 5σ on ≥ 2 axes for both K1 and K2 pairs; INFO if ≥ 3σ on ≥ 2 axes; FAIL if < 3σ on fewer than 2 axes. The verdict feeds directly into S84's §VII-DETECTOR-FORECAST landing and the EVOI ranking for S85 observational priorities.

---

## §W10b-122. S84-BIOGRAPHICAL-FRAMING-AUDIT

**Gate ID**: S84-BIOGRAPHICAL-FRAMING-AUDIT
**Trigger**: `[AUDIT]` (post-hoc re-examination of prior workshop convergence)
**Classification**: NON-PHONONIC (methodological audit of agent-interaction pattern, not a physics gate)
**Script**: `computations/s84_w10b_biographical_framing_audit.py` + neutral-prompt re-dispatches
**Agent type**: sagan-empiricist (primary) — neutral-prompt re-auditor; optional einstein-theorist for structural-argument adjudication on disputed claims

### Hypothesis

The S83 gear-machine workshop R2 "corner-with-extensions" convergence (framework's structural position described as corner of the landscape's output cone plus well-characterized extensions) may have been driven by mutual rhetorical agreement between the workshop participants rather than by independent structural argument. The biographical framing of agents (einstein-theorist, connes-ncg-theorist, kaku-speculative-theorist, etc.) may have primed them to converge on a shared narrative. Specifically, we test whether ≥ 80% of R2 claims survive a neutral-prompt re-audit that strips biographical framing, agent-name anchoring, and prior-workshop-transcript priming.

Hypothesis in formal terms: let C_R2 = set of load-bearing claims from S83 R2 corner-with-extensions wrap-up. Let C_neutral = claims surviving neutral-prompt re-audit. Gate PASSes if |C_R2 ∩ C_neutral| / |C_R2| ≥ 0.80.

### Background

- S83 gear-machine workshop produced R1 (first-pass) and R2 (corner-with-extensions) outputs, the latter convergent across the four workshop participants on the structural position of the framework within the landscape's output cone.
- The convergence was cited in S83 gen-physicist-s6 synthesis §V.6 as rank-6 gear-machine verification evidence.
- User feedback (`.claude/agent-memory/.../feedback_compute-environment.md` and related) documents that agents trained on shared corpora can produce correlated outputs without independent verification — shared context produces shared outputs, not independent confirmation (per epistemic-discipline.md).
- The S83 convergence is NOT pre-registered: it is an organizational insight (per §What Counts as a Result, organizational insights are useful but not evidential). Its role in §V.6 was framed as corroborative, not as gate-passing evidence.
- This gate tests whether the organizational insight is robust to prompt-structure — a meta-check on the agent-workshop apparatus itself.

### Method

```
from canonical_constants import *  # project-standard canonical imports

# Step 1: Extract C_R2 claim inventory from S83 R2 corner-with-extensions wrap-up
#   Load file: sessions/archive/session-83/workshops/gear-machine-R2-wrap-up.md
#   Parse claim-list: atomic assertions about framework's structural position
#   (local) C_R2_raw = parse_claims(s83_r2_wrap_up)
#   (local) C_R2 = filter_load_bearing(C_R2_raw)  # exclude trivial / definitional

# Step 2: Construct neutral-prompt template
#   Strip: agent names, biographical anchors ("as Einstein would...", "given Kaku's perspective"),
#          prior workshop transcripts, convergence framing (no mention of "R2" or "corner-with-extensions")
#   Preserve: mathematical claims, structural predicates (KO-dim=6, MG-0/1/2, etc.),
#             canonical constants, verdict thresholds
#   Template: "Given only the CCM 2007 + KO-dim=6 + A_F = C(+)H(+)M_3(C) + G32+G36 verdicts,
#              evaluate the following claim: <C_R2_i>. Classify as [ARGUMENT-BACKED | ARGUMENT-WEAK | UNSUPPORTED]."
#   (local) neutral_template = build_neutral_prompt_template()

# Step 3: Re-audit each claim individually via neutral prompt
#   Dispatch sagan-empiricist with neutral_template + C_R2_i for each i
#   (local) adjudications = [adjudicate(C_R2_i, neutral_template) for C_R2_i in C_R2]

# Step 4: Count claims classified as ARGUMENT-BACKED
#   (local) survivors = sum(1 for a in adjudications if a == 'ARGUMENT-BACKED')
#   (local) survival_fraction = survivors / len(C_R2)

# Step 5: For claims classified as UNSUPPORTED or ARGUMENT-WEAK, extract reason
#   (local) failure_reasons = [a.reason for a in adjudications if a != 'ARGUMENT-BACKED']

# Step 6: Verdict
#   if survival_fraction >= 0.80: verdict = 'PASS'
#   elif survival_fraction >= 0.50: verdict = 'INFO'
#   else: verdict = 'FAIL'  # biographical framing drove convergence

# Cross-checks:
#   (a) Inter-auditor consistency: dispatch a second adjudicator (einstein-theorist)
#       on 5 randomly sampled claims; check kappa >= 0.6 for categorical agreement
#   (b) Prompt-symmetry test: re-dispatch with inverted framing ("skeptical toward claim")
#       and check that ARGUMENT-BACKED survival drops by <= 15% (if drops by more,
#       prompt structure is itself driving adjudication)
#   (c) Claim-independence check: randomize claim order; verify no order effect > 5% shift
#   (d) Load-bearing filter audit: verify C_R2 list does not cherry-pick
#       trivially-structural claims (inflate survival) or trivially-rhetorical ones (deflate)
```

### PRDR machinery pin

- Matrix computation: NONE. This is a text-classification audit. No numpy, no torch.
- L_max: N/A.
- Scheme: neutral-prompt template as specified in Step 2. Biographical-framing stripped per explicit exclusion list.
- Convention: ARGUMENT-BACKED = supported by ≥ 1 mathematical identity OR ≥ 1 canonical-constant pin OR ≥ 1 gate verdict from S82/S83 verdict-log. ARGUMENT-WEAK = supported only by organizational-insight framing. UNSUPPORTED = no citation chain.
- Scan range: all claims from S83 R2 corner-with-extensions wrap-up (target 10–30 atomic claims).
- Random seed: `seed=84122` for claim-order randomization cross-check.
- GPU path: N/A.
- Concurrent-dispatch: ≤ 3 sagan-empiricist instances (one per block of ~10 claims), respecting ≤ 8 cap.

### Pass/Fail/INFO thresholds

- **PASS**: survival_fraction ≥ 0.80 AND inter-auditor κ ≥ 0.6 AND prompt-symmetry shift < 15%. Corner-with-extensions convergence is structurally supported; biographical framing did not drive the alignment.
- **INFO**: 0.50 ≤ survival_fraction < 0.80 OR inter-auditor κ < 0.6. Partial structural support; some claims are rhetorically-driven. Working paper §VII-GEAR-MACHINE gets explicit caveat.
- **FAIL**: survival_fraction < 0.50. Biographical framing drove R2 convergence. §V.6 corroborative framing of S83 gen-physicist-s6 is WITHDRAWN; rank-6 gear-machine classification retreats to "structurally supported by G32+G36 alone, not by R2 consensus."

### Input SHA-256 pins

- `canonical_constants.py`: `<computed-at-runtime>`
- `sessions/archive/session-83/workshops/gear-machine-R2-wrap-up.md`: `<computed-at-runtime>`
- `sessions/archive/session-83/session-83-gen-physicist-s6.md` (§V.6): `<computed-at-runtime>`
- `computations/s83_gate_verdicts.txt`: `<computed-at-runtime>`
- `.claude/rules/epistemic-discipline.md`: `<computed-at-runtime>` (for classification criteria)

### Expected output 4-tuple

`(value=survival_fraction, scheme=neutral_prompt, convention=arg_backed_vs_weak_vs_unsupported, L_max=NA)`

### Substitution chain (survival fraction direction)

This gate does not involve a sign/direction/threshold claim on a physical observable; it is a methodological audit. Nonetheless, the definition-substitution-direction chain for the gate verdict is:

Step 1: survival_fraction := |{C_R2_i : adjudication(C_R2_i, neutral_template) = ARGUMENT-BACKED}| / |C_R2|    [definition]

Step 2: PASS threshold := 0.80    [pre-registered from scope-definition]

Step 3: substitute adjudications from Step 5 of Method: survival_fraction = survivors_observed / |C_R2|

Step 4: direction comparison: survival_fraction [compared] 0.80

Step 5: if survival_fraction ≥ 0.80 ⇒ corner-with-extensions is NOT driven by biographical framing (higher survival = more structural support); if < 0.50 ⇒ IS driven by framing (lower survival = more rhetorical)

Step 6: read direction from comparator — only then emit PASS/INFO/FAIL.

### What PASS means for solution space

S83 R2 corner-with-extensions convergence is structurally grounded. §V.6 of S83 gen-physicist-s6 stands as corroborative (not evidential — it remains an organizational insight per epistemic-discipline). The agent-workshop apparatus demonstrates baseline resistance to biographical-framing bias. Rank-6 gear-machine classification retains R2 consensus as supplementary context. Framework's confidence in the gear-machine classification derives from G32 + G36 + formal MG-0/1/2 identities, with R2 as a consistency-check on the agent apparatus.

### What FAIL means for solution space

S83 R2 convergence was substantially rhetorical. §V.6 corroborative framing is WITHDRAWN from the S83 record, replaced by a §V.6-NOTE documenting the audit and citing G32 + G36 + MG-0/1/2 as the structural basis for the rank-6 gear-machine classification. Working-paper §VII-GEAR-MACHINE gets a §VII-GEAR-MACHINE-CAVEAT subsection. Meta-finding registered: agent workshops benefit from prompt-neutralization protocols for consensus-framing. A new S85 methodology-debt item (S85-NEUTRAL-PROMPT-PROTOCOL) is spawned.

### Pictorial explanation

Imagine four agents sitting around a conference table, each looking at the same problem. They each bring a biographical hat — Einstein's hat, Connes's hat, Kaku's hat, etc. They converge on an answer: "the framework is at a corner of the landscape output cone with well-characterized extensions." The question this audit asks is: if we take the hats off — if we hand each agent the bare mathematical problem with no biographical priming, no record of what the others said, no "corner-with-extensions" vocabulary — do they still converge? If yes (PASS), the answer was structural. If no (FAIL), the answer was the hats agreeing with each other. Either outcome is valuable: PASS corroborates the gear-machine classification, FAIL identifies a methodology improvement for future workshops.

---

## §W10b-123. S84-ALPHA-S-DERIVATION-CHAIN-AUDIT

**Gate ID**: S84-ALPHA-S-DERIVATION-CHAIN-AUDIT
**Trigger**: `[VERIFY-THEOREM]` (theorem-level claim: α_s = n_s² - 1 derives from minimal axiom set)
**Classification**: GEOMETRIC (Mellin-kernel spectral-action identity on A_F singleton)
**Script**: `computations/s84_w10b_alpha_s_derivation_chain_audit.py`
**Agent type**: einstein-theorist (primary) for axiomatic derivation chain; optional lizzi-spectral-functional-theorist for Mellin-kernel verification

### Hypothesis

S50's permanent result α_s = n_s² - 1 (atlas-registered identity, currently evaluated at α_s_framework = -0.068968 for n_s = 0.9649 Planck-central) derives from the minimal axiom set {CCM 2007 + KO-dim=6 + A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) singleton + Mellin-kernel spectral action} WITHOUT any auxiliary coupling relation and WITHOUT observational input of n_s itself. If the derivation requires no auxiliary relations and no observational n_s input, α_s = n_s² - 1 stands as a zero-free-parameter theorem; if it requires one auxiliary coupling, α_s is zero-free-parameter-modulo-coupling; if it requires n_s as observational input, the identity is circular.

Formally: let Axioms_minimal = {CCM + KO_dim=6 + A_F_singleton + Mellin_kernel}. Let Derivation = chain(axioms → α_s = n_s² - 1). Gate PASSes if Derivation ⊆ Axioms_minimal (closed under minimal set). INFO if Derivation = Axioms_minimal ∪ {one_aux_coupling}. FAIL if n_s ∈ Derivation as observational input (self-reference).

### Background

- S50 atlas-registered identity: α_s = n_s² - 1 (see `summary/atlas-02-theorems.md` or equivalent atlas registry for S50 latent identity).
- Current evaluation: α_s_framework = (0.9649)² - 1 = -0.068968. Verified in this planning step: exact to 1e-8 relative.
- CCM 2007 = Chamseddine-Connes-Marcolli Standard Model with neutrino mixing, axioms A1–A6.
- A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) singleton result from G32 (S83, d=12 singleton). Admissibility lattice collapses to this under KO-dim=6 + 4 axiom constraints.
- Mellin kernel: spectral action Tr(f(D/Λ)) expanded via Mellin transform, giving the Seeley-DeWitt coefficient expansion a_0 + a_2 · Λ² + a_4 + ... with spectral moments as coefficients.
- Running of spectral index: n_s(k) = n_s(k_pivot) + α_s · ln(k/k_pivot) + (1/2) · β_s · (ln(k/k_pivot))² + ... where α_s = d n_s / d ln k |_{k_pivot}.
- Candidate derivation chains for α_s = n_s² - 1:
  - (A) Pure functional form: if ln P_ζ = A + (n_s - 1) · ln k + ((n_s - 1)² / 2) · (ln k)² + ... at the pivot, then α_s = d n_s / d ln k and structural inspection yields α_s = n_s² - 1 under specific Mellin-kernel closure conditions.
  - (B) CC-5 propagation: α_s as a composed-observable ratio whose span propagates via §VII.K-PROP with a Mellin-inherited exponent.
  - (C) Pair-creation bridge (project-memory `project_ns-acoustic-optical-pair-creation.md`): acoustic-to-optical pair creation at fold-time contributes a universal second-order spectral-index correction.

### Method

```
from canonical_constants import *

# Step 1: Formalize the axiom set as explicit list
# (local) axioms_minimal = {
#     'CCM_2007_A1_A6': 'Chamseddine-Connes-Marcolli axioms A1..A6',
#     'KO_dim': 6,
#     'A_F_singleton': 'C (+) H (+) M_3(C)',
#     'Mellin_kernel': 'Tr(f(D/Lambda)) via Mellin transform',
# }

# Step 2: Load S50 derivation chain from atlas registry
# (local) s50_derivation = load_atlas_entry('alpha_s_is_ns2_minus_1')
# (local) derivation_steps = parse_steps(s50_derivation)

# Step 3: For each step in s50_derivation, classify the axiom source
# (local) step_classifications = []
# for step in derivation_steps:
#     src = classify_source(step, axiom_list=axioms_minimal,
#                           aux_relations=known_aux_relations,
#                           observational_inputs=['n_s_observed', 'A_s_observed'])
#     step_classifications.append(src)

# Step 4: Check for n_s observational input (circularity test)
# (local) observational_n_s_used = any(s == 'n_s_observed' for s in step_classifications)
# if observational_n_s_used: verdict = 'FAIL_CIRCULAR'

# Step 5: Check auxiliary coupling relations
# (local) aux_used = [s for s in step_classifications if s.startswith('aux_')]
# (local) n_aux = len(set(aux_used))

# Step 6: Verdict classification
# if observational_n_s_used: verdict = 'FAIL'
# elif n_aux == 0: verdict = 'PASS'  # pure minimal axioms
# elif n_aux == 1: verdict = 'INFO'  # one auxiliary coupling
# else: verdict = 'FAIL'  # requires multiple auxiliary relations

# Step 7: For PASS, emit the derivation as a formal proof sketch
# (local) proof_sketch = format_derivation_chain(s50_derivation, axioms_minimal)

# Cross-checks:
#   (a) Mellin-kernel closure: verify that the ln P_ζ expansion to O((ln k)²)
#       is closed under the A_F = C(+)H(+)M_3(C) spectral-action truncation.
#       Explicit: check that d²(ln P_ζ) / d(ln k)² at k_pivot = α_s (not just linear term).
#   (b) Substrate-level check: compute α_s directly from first-principles via
#       d²(ln P_ζ) / d(ln k)² using G7-G10 UNIFIED-AS-79 machinery at n_s = 0.9649;
#       verify that it matches -0.068968 to within numerical accuracy.
#   (c) Alternative-n_s test: evaluate α_s = n_s² - 1 at n_s = 0.95 (non-Planck)
#       and at n_s = 0.97 (non-Planck) — check that the identity holds FUNCTIONALLY
#       (not just at the Planck point). If identity holds only at n_s = 0.9649,
#       that is evidence of observational input.
#   (d) Independent-derivation cross-check: derive α_s via CC-5 propagation
#       (CC-5 exponent = 2 for n_s² → α_s); compare to the functional-form derivation.
#       Independent paths should yield same α_s expression.
```

### PRDR machinery pin

- Matrix computation: closed-form Mellin-kernel verification via symbolic differentiation (sympy). No large-matrix linear algebra required. GPU path: N/A.
- L_max: N/A for identity verification. For the cross-check (b), use L_max = 5 UNIFIED-AS-79 machinery at canonical pins (Zubarev scheme, TD branch, H_tilde = 5.907e-3 per H_TD canonical constant).
- Scheme: Mellin-kernel spectral action in the standard CCM 2007 normalization. Cutoff Λ = M_KK per canonical (`M_KK = 1.05e17 GeV`, S73B sole-convergent extrapolation).
- Convention: n_s defined at pivot k_pivot = 0.05 Mpc⁻¹ (Planck convention); α_s = d n_s / d ln k |_{k = k_pivot}.
- Scan range: n_s evaluation at {0.95, 0.96, 0.9649, 0.97, 0.98} to test functional-form holding (cross-check c).
- Random seed: N/A (deterministic derivation).
- GPU path: N/A.

### Pass/Fail/INFO thresholds

- **PASS**: Derivation traces to {CCM + KO-dim=6 + A_F-singleton + Mellin kernel} with zero auxiliary coupling relations invoked AND no observational n_s input. α_s = n_s² - 1 is a zero-free-parameter identity. Cross-check (a) closure verified AND cross-check (b) substrate-level α_s matches -0.068968 to ≤ 1% AND cross-check (c) identity holds at all 5 scan n_s values AND cross-check (d) CC-5 and functional-form derivations agree.
- **INFO**: Derivation requires ONE auxiliary coupling relation (e.g., an A_F-internal gauge-coupling identity). α_s = n_s² - 1 is zero-free-parameter-modulo-coupling. Cross-check (b) substrate-level value matches within 5%.
- **FAIL**: Derivation requires n_s itself as observational input, OR requires ≥ 2 auxiliary couplings, OR cross-check (c) shows identity holds ONLY at n_s = 0.9649 (circularity proxy), OR cross-check (b) substrate-level value disagrees by > 10%. α_s = n_s² - 1 is CIRCULAR or under-axiomatized.

### Input SHA-256 pins

- `canonical_constants.py`: `<computed-at-runtime>`
- `summary/atlas-02-theorems.md` (S50 latent identity): `<computed-at-runtime>`
- `sessions/session-50/session-50-final.md`: `<computed-at-runtime>`
- CCM 2007 axioms reference (`researchers/Feynman/` or equivalent paper directory): `<computed-at-runtime>`
- G32 + G36 verdict lines (from `computations/s83_gate_verdicts.txt`): `<computed-at-runtime>`
- `computations/` — UNIFIED-AS-79 machinery scripts for cross-check (b): `<computed-at-runtime>`

### Expected output 4-tuple

`(value=n_aux_couplings OR 'FAIL_CIRCULAR', scheme=Mellin_kernel_CCM2007, convention=n_s_pivot_0.05_Mpc_inv, L_max=5_for_crosscheck_b)`

### Substitution chain (α_s from functional form)

Step 1: ln P_ζ(k) = A + (n_s(k_pivot) - 1) · ln(k/k_pivot) + (1/2) · α_s · (ln(k/k_pivot))² + ...    [definition of scale-dependent primordial power spectrum]

Step 2: α_s := d n_s / d ln k |_{k = k_pivot}    [definition of α_s per Planck/PDG convention]

Step 3: under the Mellin-kernel closure (candidate derivation A), the Seeley-DeWitt expansion yields n_s(k) = n_s(k_pivot) · f(ln(k/k_pivot)) where f has a specific closed form dictated by the A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) spectral-action truncation.    [substitution]

Step 4: specifically, if the Mellin closure gives n_s(k)² expansion with closure coefficient 1 (i.e., n_s(k)² appears as the natural functional variable of the spectral action at second order), then d n_s / d ln k = (1/(2n_s)) · d(n_s²) / d ln k    [chain rule]

Step 5: if the spectral-action truncation further imposes d(n_s²) / d ln k |_{k_pivot} = 2n_s · (n_s² - 1) [Mellin-kernel closure constraint], then α_s = (1/(2n_s)) · 2n_s · (n_s² - 1) = n_s² - 1    [simplification]

Step 6: substitute n_s = 0.9649 ⇒ α_s = 0.9649² - 1 = -0.068968    [numerical, verified at plan-write time: |computed - quoted| < 1e-8]

Step 7: Direction: α_s < 0 ⇔ n_s < 1 ⇔ red-tilted (confirmed by Planck). Magnitude: |α_s| ≈ 2·(1-n_s) at leading order for n_s near 1; exact formula gives |α_s| = (1-n_s)·(1+n_s) ≈ 0.069 for n_s = 0.9649.

The audit tests whether Step 3's "Mellin-kernel closure" is a LEGITIMATE consequence of {CCM + KO-dim=6 + A_F + Mellin} or requires an auxiliary input. PASS if Step 3 closure is proven from axioms; FAIL if Step 3 closure itself requires the observational n_s value.

### What PASS means for solution space

α_s = n_s² - 1 is a zero-free-parameter theorem of the framework. The 9.62σ separation from Planck (|α_s_framework - α_s_Planck| / σ_{α_s}_Planck with σ = 0.00717) and 34.48σ projected separation from CMB-S4 (σ ≈ 0.002) become GENUINE predictions rather than coincidental matches. S84-ALPHA-S-PRE-REGISTRATION (gate 7, §4.A) stands as a long-horizon discriminator. The framework makes a falsifiable observational claim about α_s that no alternative construction achieves without auxiliary inputs.

### What FAIL means for solution space

α_s = n_s² - 1 does NOT derive from minimal axioms. Either circularity (n_s observational input) or multi-parameter freedom (≥ 2 auxiliary relations). The high-σ separations lose their zero-free-parameter status. S84-ALPHA-S-PRE-REGISTRATION (gate 7) is DOWNGRADED from discriminator to consistency-check. S50 atlas entry requires amendment: identity moved from "permanent theorem" to "empirical regularity" or withdrawn pending structural derivation. EVOI priority drops for α_s-focused observational work.

### Pictorial explanation

Think of the framework as a stack of axioms like Lego blocks: CCM 2007 is the base, KO-dim=6 is the size constraint, A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) is the singleton color scheme, Mellin kernel is the joining rule. The claim α_s = n_s² - 1 is a beautiful arch built on top. The audit asks: is every brick in the arch accounted for by the blocks below? If yes (PASS), the arch stands on its own foundation. If one brick needs a separate support (INFO), the arch is stable but not purely self-supporting. If the arch is actually held up by an invisible hand pressing down from above (FAIL with n_s as observational input), the whole structure is self-referential and the "derivation" was really a fitting exercise disguised as a proof. The audit walks around the arch, inspects every brick, and reports which of the three structural pictures is correct.

---

## §W10b-124. S84-CMB-S4-JOINT-DISCRIMINATOR-PLANE

**Gate ID**: S84-CMB-S4-JOINT-DISCRIMINATOR-PLANE
**Trigger**: `[CHAIN]` (composite-ledger claim: joint-Fisher σ-separation across 5 axes for 2 competitor theories)
**Classification**: NON-PHONONIC (observational forecast / Fisher-information computation, not a substrate prediction)
**Script**: `computations/s84_w10b_cmbs4_joint_discriminator_plane.py`
**Agent type**: mack-cosmic-bridge (primary; observational liaison handles the detector-forecast Fisher chain)

### Hypothesis

The framework's 5-axis prediction vector (n_T, α_s, M_KK, ALP-spectrum, frequency-comb) — drawn from S83 R2 gear-machine workshop and anchored on S64 n_T, S50 α_s, S73B M_KK, Γ6 7-feature ALP comb, and the 4-speed hierarchy c_mod > c_BLV > c_BA > c_L — separates from the two nearest landscape competitors K1 (typical IIB slow-roll) and K2 (heterotic slow-roll with discrete flux) by ≥ 5σ on ≥ 2 axes for each competitor when evaluated under the joint sensitivity of CMB-S4 + LiteBIRD + SKA-2 + Hyper-K + (inferred-from-spectroscopic) M_KK constraints.

The gate formalizes the axes, projected sensitivities, and competitor predictions into a pre-registered joint-Fisher table with numerical σ-separations per axis per competitor.

### Background

- Framework prediction vector (anchors from §0 of this plan file and canonical constants):
  - n_T = +0.4676 (BLUE, transit-scale per S64/G50). Note: at CMB scales, G46 eps_H-flow transfer gives n_T_CMB ≈ -3×10⁻³ (RED). The axis used for CMB-scale discrimination is n_T_CMB, not the transit-scale value — which is observationally inaccessible per S84-41 BLUE-TRANSIT-TILT-INACCESSIBILITY.
  - α_s = -0.068968 (zero-free-parameter from S50 α_s = n_s² - 1, contingent on gate 123 PASS).
  - M_KK = 1.05×10¹⁷ GeV (S73B sole-convergent L_max → ∞ extrapolation).
  - ALP-spectrum: 7-feature frequency-comb from Γ6 regulator (Γ6 = 5-face master regulator family).
  - 4-speed hierarchy: c_mod > c_BLV > c_BA > c_L (strict inequality chain, substrate dispersion-relation).
- K1 (typical IIB slow-roll): α_s ≈ -0.001 (slow-roll minimal running), n_T ≈ -2ε_H ≈ -0.02 (for ε_H ≈ 0.01), M_KK ≈ 10¹⁶ GeV (one OOM below framework), typical 1-feature ALP, single light-speed c.
- K2 (heterotic slow-roll with discrete flux): α_s ≈ -0.001, n_T ≈ -0.01, M_KK ≈ 5×10¹⁵ GeV (1.3 OOM below framework), typical 0–1 ALP feature, single light-speed c.
- Projected sensitivities:
  - CMB-S4: σ(α_s) ≈ 0.002, σ(n_T) ≈ 0.005 at full-survey (Abazajian et al. 2022+ forecasts).
  - LiteBIRD: σ(n_T) ≈ 0.054 at 3yr → ≈ 0.04 at 6.5yr extended.
  - Joint LB+S4 Fisher: σ_joint(n_T) = 1/√(1/σ_LB² + 1/σ_S4²) = 1/√(1/0.04² + 1/0.005²) ≈ 0.005 (S4-dominated).
  - SKA-2: σ(α_f_NL) ≈ 0.80.
  - Hyper-K: ALP phenomenology constraints (frequency-comb feature identification, per-feature detection threshold ≈ 2σ per feature).
  - M_KK: no direct measurement; inferred via KK-mode search at LHC/HL-LHC (current bound M_KK > 10¹³ GeV for warped models; no precision measurement at 10¹⁷ GeV scale). Use log₁₀(M_KK) as discriminator with σ_log10 ≈ 1 (detector-sterile at framework's M_KK).

### Method

```
from canonical_constants import *  # M_KK=1.05e17, tau_fold=0.19, H_TD, etc.
import numpy as np

# Step 1: Framework prediction vector (from canonical constants + gate verdicts)
# (local) fw_pred = {
#     'n_T_CMB':  -3.0e-3,   # G46 transfer output (RED at CMB, not +0.468 transit-scale)
#     'alpha_s':  -0.068968, # S50 + gate 123 verdict
#     'log10_M_KK': np.log10(1.05e17),  # S73B sole-convergent
#     'N_ALP_features': 7,  # Gamma6 7-feature comb
#     'speed_hierarchy': 'strict_4_ordering',  # c_mod > c_BLV > c_BA > c_L
# }

# Step 2: Competitor K1 (typical IIB slow-roll) prediction vector
# (local) K1_pred = {
#     'n_T_CMB':  -0.020,   # -2*eps_H for eps_H=0.01 typical
#     'alpha_s':  -0.001,   # slow-roll minimal
#     'log10_M_KK': np.log10(1.0e16),
#     'N_ALP_features': 1,  # typical single ALP
#     'speed_hierarchy': 'c_universal',  # no hierarchy
# }

# Step 3: Competitor K2 (heterotic slow-roll with discrete flux)
# (local) K2_pred = {
#     'n_T_CMB':  -0.010,
#     'alpha_s':  -0.001,
#     'log10_M_KK': np.log10(5.0e15),
#     'N_ALP_features': 0,  # typical heterotic: no light ALPs in simplest models
#     'speed_hierarchy': 'c_universal',
# }

# Step 4: Projected sensitivities (per-axis σ)
# (local) sigma = {
#     'n_T_CMB':  1.0 / np.sqrt(1/0.04**2 + 1/0.005**2),  # joint LB+S4, ~0.005
#     'alpha_s':  0.002,  # CMB-S4 full survey
#     'log10_M_KK': 1.0,   # detector-sterile: collider + indirect only
#     'N_ALP_features': 0.5,  # Hyper-K per-feature resolution (binary-count sigma)
#     'speed_hierarchy': 0.0,  # binary detection (fw vs competitor is {present, absent})
# }

# Step 5: Per-axis sigma separation (framework vs competitor)
# For continuous axes: sigma_sep = |fw_pred - comp_pred| / sigma
# For ALP features: sigma_sep ≈ |N_fw - N_comp| / sqrt(N_fw + N_comp) [Poisson-like]
# For speed hierarchy: binary {present, absent} → effectively infinite-sigma if
#     detector can distinguish; else zero.
# (local) separations = {}
# for comp_name, comp_pred in [('K1', K1_pred), ('K2', K2_pred)]:
#     for axis in fw_pred:
#         sep = compute_sigma_separation(fw_pred[axis], comp_pred[axis], sigma[axis], axis_type)
#         separations[(comp_name, axis)] = sep

# Step 6: PASS/INFO/FAIL computation
# PASS_crit = ≥ 5σ on ≥ 2 axes for each competitor
# INFO_crit = ≥ 3σ on ≥ 2 axes for each competitor
# FAIL otherwise
# (local) pass_per_comp = {}
# for comp_name in ['K1', 'K2']:
#     axes_above_5sigma = sum(1 for axis in fw_pred
#                              if separations[(comp_name, axis)] >= 5.0)
#     axes_above_3sigma = sum(1 for axis in fw_pred
#                              if separations[(comp_name, axis)] >= 3.0)
#     pass_per_comp[comp_name] = {
#         '5sigma': axes_above_5sigma,
#         '3sigma': axes_above_3sigma,
#     }
# (local) joint_pass = all(pass_per_comp[c]['5sigma'] >= 2 for c in ['K1','K2'])
# (local) joint_info = all(pass_per_comp[c]['3sigma'] >= 2 for c in ['K1','K2'])

# Step 7: Emit verdict + per-axis table
# if joint_pass: verdict = 'PASS'
# elif joint_info: verdict = 'INFO'
# else: verdict = 'FAIL'

# Cross-checks:
#   (a) Prior-predictive range: compute log10(prior_range/posterior_width) for each
#       continuous axis. Framework achieves high log-BF if prior is wide (e.g., ≥ 5 OOM)
#       and framework prediction sits in narrow posterior. Report log10_BF per axis.
#   (b) Correlation matrix: Fisher-information matrix has off-diagonal entries for
#       (n_T, r) and (alpha_s, n_s). Include the 5x5 Fisher matrix for the continuous axes;
#       invert to get full covariance; joint Mahalanobis distance is the proper multi-axis
#       separation metric beyond per-axis sigma.
#   (c) Degeneracy-breaking count: how many axes require joint analysis to distinguish?
#       If fw and K1 are degenerate on axis i alone but separated jointly with axis j,
#       that is a degeneracy-breaking pair. Report the pair.
#   (d) Landscape K1/K2 range: instead of single K1/K2 predictions, use a distribution
#       over typical slow-roll parameters (eps_H in [0.003, 0.03], etc.) and report
#       fw vs landscape-distribution separation. Robust to K1/K2 point-choice.
```

### PRDR machinery pin

- Matrix computation: 5×5 Fisher matrix inversion — CPU numpy.linalg sufficient (trivial size). GPU path: N/A.
- L_max: N/A for Fisher. M_KK uses the canonical L_max → ∞ extrapolation from S73B.
- Scheme: Fisher-information formalism at the projected full-survey sensitivities (Abazajian 2022+ for CMB-S4; LiteBIRD 3yr and 6.5yr both tabulated).
- Convention:
  - Continuous axes: |Δ_fw_vs_comp| / σ as per-axis separation.
  - Discrete axes (N_ALP_features): Poisson-approximation sigma = √(N_fw + N_comp); separation = |N_fw - N_comp| / √(N_fw + N_comp).
  - Binary axes (speed_hierarchy): classified as DETECTOR-STERILE at the current observational horizon (no instrument directly measures c_BLV, c_BA, c_L independently); axis counts as 0σ separation in PASS/INFO/FAIL determination but is reported as "structural prediction" in the output table.
- Scan range: K1 and K2 predictions per background §. Alternative competitor sets (K3 = LVS, K4 = KKLT) tabulated as diagnostic but not part of gate determination.
- Random seed: N/A (deterministic Fisher).
- GPU path: N/A.

### Pass/Fail/INFO thresholds

- **PASS**: for EACH of {K1, K2}, the number of axes with σ-separation ≥ 5 is ≥ 2. Framework is a genuine 5σ discriminator against both nearest competitors on at least 2 axes each.
- **INFO**: for EACH of {K1, K2}, the number of axes with σ-separation ≥ 3 is ≥ 2, but the 5σ threshold is not met for at least one competitor.
- **FAIL**: for at least one of {K1, K2}, the number of axes with σ-separation ≥ 3 is < 2. Framework does not discriminate at 3σ joint on the 5-axis plane.

### Input SHA-256 pins

- `canonical_constants.py`: `<computed-at-runtime>`
- `computations/s83_gate_verdicts.txt` (G46, G50, S73B M_KK extrapolation): `<computed-at-runtime>`
- `sessions/archive/session-83/workshops/gear-machine-R2-wrap-up.md` (5-axis R2 framing): `<computed-at-runtime>`
- Abazajian et al. 2022 CMB-S4 forecast tables (hard-coded σ values documented with citation): `<computed-at-runtime>`
- LiteBIRD projected sensitivities (hard-coded per collaboration public projections, cited): `<computed-at-runtime>`
- SKA-2 σ(α_f_NL) projection: `<computed-at-runtime>`

### Expected output 4-tuple

`(value=(σ_sep_K1_per_axis, σ_sep_K2_per_axis), scheme=Fisher_joint, convention=continuous_Gaussian_plus_discrete_Poisson, L_max=NA)`

### Substitution chain (separation direction per axis)

Definition: for continuous axis X with fw-prediction X_fw, competitor prediction X_comp, and projected sensitivity σ_X, the separation is sep(X) := |X_fw - X_comp| / σ_X.

Step 1: axis n_T_CMB. fw = -3.0×10⁻³, K1 = -0.020, σ_joint = 1/√(1/0.04² + 1/0.005²) = 0.00498. Substitute: sep = |(-3.0×10⁻³) - (-0.020)| / 0.00498 = 0.017 / 0.00498 = 3.41σ vs K1. Plan-write Python verification: 3.43σ (rounding in σ_joint).

Step 2: axis α_s. fw = -0.068968, K1 = -0.001, σ = 0.002. sep = |(-0.068968) - (-0.001)| / 0.002 = 0.067968 / 0.002 = 33.98σ vs K1. Plan-write Python: 34.48σ for fw vs Planck-central baseline; 24.03σ as "joint separation with factor √2 for fw-vs-K1 double-variance." For gate purposes (single-σ axis separation of fw from K1 prediction), sep ≈ 34σ. Well above 5σ ⇒ PASS-eligible on this axis against K1.

Step 3: axis log10(M_KK). fw = log10(1.05×10¹⁷) = 17.02, K1 = log10(1.0×10¹⁶) = 16.00, σ_log10 ≈ 1.0 (detector-sterile). sep = |17.02 - 16.00| / 1.0 = 1.02σ. NOT 5σ. Detector-sterile axis does not contribute to PASS but is reported structurally. K2: sep = |17.02 - log10(5×10¹⁵)| / 1.0 = |17.02 - 15.70| / 1.0 = 1.32σ.

Step 4: axis N_ALP_features. fw = 7, K1 = 1. Poisson sep = |7-1| / √(7+1) = 6 / √8 = 6/2.828 = 2.12σ. Below 3σ for per-feature counting. BUT the more appropriate detection statistic is feature-by-feature χ² accumulation: if each framework feature has detection SNR S_i at Hyper-K, and K1 predicts only one, then joint detection of 6 extra features gives χ² ≈ 6 · S̄² where S̄ is mean per-feature SNR. At Hyper-K per-feature resolution ≈ 2σ, joint significance ≈ 2·√6 = 4.90σ (approximate). Report BOTH the Poisson and the χ² accumulation.

Step 5: axis speed_hierarchy. fw = strict_4_ordering, K1 = c_universal. Binary axis, DETECTOR-STERILE at current/projected 2030s instruments — no direct measurement of c_BLV, c_BA, c_L as independent propagation speeds in CMB/GW/neutrino channels at ≤ σ/c ≈ 10⁻⁵. Report as structural prediction; 0σ in PASS/INFO/FAIL determination.

Step 6: aggregate per-competitor. For K1: axes ≥ 5σ = {α_s (34σ)}. Axes ≥ 3σ = {α_s (34σ), n_T (3.43σ)}. One 5σ axis, two 3σ axes. For K2: similar, with n_T separation slightly lower (sep = |(-3×10⁻³)-(-0.010)|/0.005 = 1.40σ). K2 axes ≥ 3σ = {α_s (34σ), ALP (~2–5σ per statistic)}; axes ≥ 5σ = {α_s}.

Step 7: verdict computation. PASS requires ≥ 2 axes at ≥ 5σ for EACH of K1 and K2. Current plan-write analysis shows:
- K1: 1 axis ≥ 5σ (α_s). Potentially 2 if ALP χ² accumulation counts as 5σ.
- K2: 1 axis ≥ 5σ (α_s).
Both likely fall short of PASS (2 axes at 5σ) under the strict reading. INFO likely: ≥ 2 axes at 3σ for both. Actual verdict is computed by the dispatched agent with the formal Fisher matrix.

Direction: higher σ = more discrimination = PASS-favorable. The α_s axis dominates; the framework's discrimination power on the 5-axis plane rests primarily on α_s = n_s² - 1 being a zero-free-parameter prediction (contingent on gate 123 PASS).

### What PASS means for solution space

Framework is a genuine ≥ 5σ discriminator on ≥ 2 axes against both nearest landscape competitors. The joint 5-axis plane provides hard observational distinguishability by the 2030 era. CMB-S4 + LiteBIRD + SKA-2 + Hyper-K become falsifiers, not consistency-checks. The S84 §VII-DETECTOR-FORECAST synthesis cites gate 124 as the pre-registered joint discriminator. EVOI for 2026-2030 observational priorities: α_s-precision instruments (CMB-S4, CMB-HD, LiteBIRD extended) top the list.

### What INFO means for solution space

Framework achieves ≥ 3σ joint on ≥ 2 axes against both competitors — observationally distinguishable but not at the 5σ gold-standard level for unambiguous detection. 2030s observations can CONSTRAIN the framework but cannot DECISIVELY falsify. EVOI focus shifts to reducing the σ on the axes currently at 3–5σ, particularly n_T_CMB (joint LB+S4) and ALP-feature χ² accumulation (Hyper-K extended).

### What FAIL means for solution space

Framework does not discriminate at the 3σ joint level against one of the nearest competitors. The 5-axis plane is DEGENERATE — continuous observational parameters alone do not distinguish. Framework would retain its structural-theory status via G32 + G36 + MG-0/1/2, but the 5-axis detector plane ceases to be a decisive test. EVOI shifts to qualitatively-new axes (e.g., UHF-GW at 1 mHz, 21-cm tomography α_f_NL, CGWB absolute tensor power) identified in other §4.D gates.

### Pictorial explanation

Imagine the framework and its two nearest competitors (K1, K2) as three distinct dots in a 5-dimensional space where each axis is an observable that CMB-S4 + LiteBIRD + SKA-2 + Hyper-K can measure. Around each dot, the projected 1σ sensitivity of the 2030s detector suite draws a fuzzy ellipsoid. The question is: do the three fuzzy ellipsoids overlap, or are they cleanly separated? The 5σ PASS threshold asks for ≥ 2 axes where framework's ellipsoid does not overlap competitor's along that axis. Think of it as "can the 2030 telescope pick out the framework's fingerprint from the landscape crowd?" PASS: yes, unambiguously, on two or more axes. INFO: yes, but it requires the full instrument suite working to its 3σ limit. FAIL: no — the framework and competitors are indistinguishable with available instruments. The gate PRE-REGISTERS the numerical σ-separations before running, converting a qualitative "the framework makes many predictions" narrative into a quantitative falsifiability test.

---

## W10b → W10a Parallel Dispatch Note

W10b (gates 122, 123, 124) and W10a (§4.L audit-integrity items — SHA regeneration, GV-secondary classification, S80 header repair, rank-universality proof write-up, etc.) are INDEPENDENT parallel sub-waves. No gate in W10b depends on any gate in W10a.

Dispatch cap (≤ 8 concurrent agents per session) trivially accommodates W10b's 3 gates + W10a's audit load. Recommended concurrent dispatch: W10b-122 (sagan-empiricist), W10b-123 (einstein-theorist), W10b-124 (mack-cosmic-bridge) all in parallel with up to 5 W10a agents.

Cross-wave coupling NOTE:
- W10b-123 ALPHA-S-DERIVATION-CHAIN-AUDIT outcome affects the α_s entry in W10b-124 CMB-S4-JOINT-DISCRIMINATOR-PLANE. If gate 123 returns FAIL, the 34σ α_s separation becomes a consistency-check rather than a discriminator, and W10b-124 verdict should be re-evaluated with α_s axis removed. Plan accommodates this by running gate 123 first-in-dispatch and gate 124 second; if gate 123 verdict arrives before gate 124 computation completes, dispatched mack-cosmic-bridge agent updates the α_s σ-separation accordingly. If gate 123 is still pending when gate 124 is dispatched, gate 124 uses the PASS-scenario α_s value and flags the contingency in the verdict-log.
- W10b-122 BIOGRAPHICAL-FRAMING-AUDIT does not gate any other W10b computation (it is a methodology audit) and does not block any S84 downstream gate. Its FAIL outcome triggers §VII-GEAR-MACHINE-CAVEAT in the working paper but does not invalidate any observational prediction.

---

## W10b → (session close) Decision Point

At S84 close, W10b contributes to three distinct landings:

**Landing 1 (methodology)**: gate 122 verdict determines whether S83 §V.6 "corner-with-extensions" framing stands, gets caveated, or is withdrawn. Working-paper §VII-GEAR-MACHINE is annotated accordingly. A FAIL here also registers S85-NEUTRAL-PROMPT-PROTOCOL as a new methodology-debt item.

**Landing 2 (theorem-registry)**: gate 123 verdict determines whether S50 atlas-entry α_s = n_s² - 1 is registered as a PERMANENT theorem of the framework (PASS), an EMPIRICAL regularity (INFO), or WITHDRAWN pending re-derivation (FAIL). This feeds the `permanent-results-registry` maintenance task and affects S84-ALPHA-S-PRE-REGISTRATION (gate 7, §4.A).

**Landing 3 (detector-forecast)**: gate 124 verdict lands the pre-registered joint-discriminator plane into working-paper §VII-DETECTOR-FORECAST. Outcome determines whether the 5-axis plane is cited as a decisive falsifier (PASS), a constraining but non-decisive test (INFO), or is replaced by qualitatively-new observables (FAIL).

Decision rule for W10b landing:
- If (gate 122 = PASS OR INFO) AND (gate 123 = PASS) AND (gate 124 = PASS OR INFO): S84 closes with all three §VII sections landed without caveats.
- If gate 123 = FAIL: S84 §VII-THEOREM-REGISTRATION (gate 10, §4.A) drops the S50 identity; gate 124 α_s axis demoted; alpha-s pre-registration (gate 7) downgraded to consistency-check.
- If gate 122 = FAIL: §VII-GEAR-MACHINE-CAVEAT appended to working paper; S83 §V.6 framing amended; S85 methodology-protocol item spawned.
- If gate 124 = FAIL: §VII-DETECTOR-FORECAST synthesis emphasizes qualitatively-new-axes (UHF-GW, 21-cm tomography, CGWB absolute power) as primary 2030s EVOI drivers.

---

## W10b Machinery-Enumeration Pin (§0.11)

Per PRDR (Pre-Registration Dry-Run) requirement (`.claude/rules/epistemic-discipline.md` §PRU), every gate-relevant machinery parameter is enumerated below. Any parameter listed as "<free>" signals PRU vulnerability — the plan MUST declare it as diagnostic or pin a value before dispatch.

| Gate | Parameter | Pinned value | Source |
|:-----|:----------|:-------------|:-------|
| 122 | neutral_prompt_template | strips {agent_names, biographical_anchors, prior_transcripts, convergence_framing}; preserves {math_identities, structural_predicates, canonical_constants, verdict_thresholds} | this plan §W10b-122 Method Step 2 |
| 122 | adjudication_categories | {ARGUMENT-BACKED, ARGUMENT-WEAK, UNSUPPORTED} | this plan §W10b-122 PRDR |
| 122 | PASS_threshold | survival_fraction ≥ 0.80 | scope-definition, §4.M row 122 |
| 122 | INFO_band | 0.50 ≤ survival < 0.80 | scope-definition |
| 122 | inter_auditor_kappa_threshold | κ ≥ 0.6 | standard categorical-agreement floor (Cohen 1960) |
| 122 | prompt_symmetry_tolerance | shift ≤ 15% under inverted-framing prompt | plan-write choice; documents prompt-structure robustness |
| 122 | claim_inventory_filter | "load-bearing" = cited in S83 §V.6 OR appears in gear-machine R2 wrap-up OR referenced in rank-6 classification | plan-write operational definition |
| 122 | random_seed | 84122 | reproducibility |
| 122 | concurrent_auditors | ≤ 3 sagan-empiricist instances | .claude/rules/ concurrent-dispatch-cap |
| 122 | GPU_path | N/A | text-classification, no matrix algebra |
| 123 | axiom_set_minimal | {CCM_2007_A1_A6, KO_dim=6, A_F=C(+)H(+)M_3(C), Mellin_kernel} | S83 G32 (d=12 singleton), CCM 2007 |
| 123 | auxiliary_relation_count_thresholds | PASS if n_aux=0, INFO if n_aux=1, FAIL if n_aux≥2 or observational_n_s_used | scope-definition, §4.M row 123 |
| 123 | observational_input_blacklist | {n_s_observed, A_s_observed, any PDG/Planck point-value entering derivation} | plan-write choice; prevents circularity |
| 123 | pivot_scale_convention | k_pivot = 0.05 Mpc⁻¹ (Planck standard) | Planck 2018 inflation |
| 123 | cross_check_b_machinery | UNIFIED-AS-79 at L_max=5, Zubarev, TD branch, H_TD = 5.907e-3 | canonical_constants.py, S82/S83 verdicts |
| 123 | n_s_functional_form_scan | n_s ∈ {0.95, 0.96, 0.9649, 0.97, 0.98} | plan-write choice; tests identity holding at non-Planck values |
| 123 | sympy_symbolic_differentiation | version-pinned sympy in phonon-exflation-sim venv | reproducibility |
| 123 | CC-5_exponent | p = 2 (for n_s² → α_s propagation) | S83 §VII.K-PROP |
| 123 | random_seed | 84123 (for any stochastic cross-check numerics; derivation itself is deterministic) | reproducibility |
| 123 | GPU_path | N/A | closed-form derivation, small matrix cross-check |
| 124 | CMB-S4_sigma_alpha_s | 0.002 | Abazajian et al. 2022 forecast (full-survey) |
| 124 | CMB-S4_sigma_n_T | 0.005 | Abazajian et al. 2022 forecast (full-survey) |
| 124 | LiteBIRD_sigma_n_T_3yr | 0.054 | LiteBIRD collaboration projections |
| 124 | LiteBIRD_sigma_n_T_6.5yr | 0.040 | LiteBIRD extended-mission projection |
| 124 | SKA-2_sigma_alpha_f_NL | 0.80 | S83 G45 (SKA-2 Phase-2) |
| 124 | Hyper-K_per_feature_resolution | ≈ 2σ per ALP feature | Hyper-K collaboration ALP phenomenology |
| 124 | M_KK_sigma_log10 | 1.0 | detector-sterile at framework value; inferred from collider + indirect |
| 124 | K1_prediction_vector | (n_T_CMB=-0.020, α_s=-0.001, log10_M_KK=16.00, N_ALP=1, c_universal) | typical IIB slow-roll, landscape average |
| 124 | K2_prediction_vector | (n_T_CMB=-0.010, α_s=-0.001, log10_M_KK=15.70, N_ALP=0, c_universal) | typical heterotic slow-roll with discrete flux |
| 124 | framework_n_T_axis | n_T_CMB (not n_T_transit); n_T_transit is DETECTOR-STERILE per S84-41 | G46 eps_H-flow transfer, canonical constant |
| 124 | framework_α_s_value | -0.068968 | gate 123 PASS contingent; if FAIL, α_s axis demoted |
| 124 | framework_M_KK_value | 1.05×10¹⁷ GeV | S73B L_max → ∞ sole-convergent extrapolation |
| 124 | framework_N_ALP_features | 7 | Γ6 regulator 7-feature comb |
| 124 | speed_hierarchy_axis | DETECTOR-STERILE at 2030s horizon; 0σ in PASS/INFO/FAIL; reported structurally | substrate dispersion-relation, no CMB/GW/ν c_BLV,c_BA,c_L direct access |
| 124 | ALP_statistic | both Poisson (|ΔN|/√(N_fw+N_comp)) AND χ² accumulation (√(6·S̄²) for 6 extra features at per-feature 2σ) reported | plan-write choice; two estimators for ALP axis |
| 124 | PASS_threshold | for EACH competitor: ≥ 2 axes at ≥ 5σ | scope-definition, §4.M row 124 |
| 124 | INFO_threshold | for EACH competitor: ≥ 2 axes at ≥ 3σ but NOT PASS | scope-definition |
| 124 | Fisher_matrix_dimension | 5×5 full; inverted to give covariance; Mahalanobis distance as diagnostic | plan-write choice; cross-check (b) |
| 124 | random_seed | 84124 | reproducibility |
| 124 | GPU_path | N/A | 5×5 matrix, CPU numpy.linalg trivial |

Diagnostic-declared (non-PASS/FAIL impact):

- Gate 122: inter-auditor κ (diagnostic; PASS requires κ ≥ 0.6 as gate-relevant, but specific κ value is reported as diagnostic)
- Gate 122: failure reason distribution (diagnostic; informs future methodology-protocol)
- Gate 123: per-step axiom-source classification table (diagnostic; documents the full derivation chain)
- Gate 123: cross-check (b) substrate-level α_s value (diagnostic; corroborates Mellin-kernel closure)
- Gate 123: cross-check (c) functional-form holding at non-Planck n_s values (diagnostic; identifies circularity if identity holds only at n_s = 0.9649)
- Gate 123: cross-check (d) CC-5 vs functional-form derivation agreement (diagnostic; tests independence of derivation paths)
- Gate 124: Mahalanobis-distance joint metric (diagnostic; corroborates per-axis σ)
- Gate 124: per-axis log_10(prior_range / posterior_width) Bayes-factor-proxy (diagnostic; reports zero-free-parameter evidence weight)
- Gate 124: landscape-distribution (K1/K2 extended) separation (diagnostic; robustness of K1/K2 point-choice)

---

## W10b Input-SHA Ledger

All ledger entries are `<computed-at-runtime>` — SHAs written to verdict lines upon script execution. Canonical SHA discipline: 64-character hexdigest mandatory (per `.claude/rules/gate-verdicts.md`); dual-SHA schema_version=S84+ with both `audit_sha256` and `content_sha256`.

| Gate | Inputs | SHA status |
|:-----|:-------|:-----------|
| 122 | canonical_constants.py, s83_r2_wrap_up.md, s83_gen_physicist_s6.md (§V.6), s83_gate_verdicts.txt, epistemic-discipline.md | all `<computed-at-runtime>` |
| 123 | canonical_constants.py, atlas-02-theorems.md (S50 entry), session-50-final.md, CCM_2007_axioms.md, s83_gate_verdicts.txt (G32, G36), UNIFIED-AS-79 computation scripts | all `<computed-at-runtime>` |
| 124 | canonical_constants.py, s83_gate_verdicts.txt (G46, G50, S73B M_KK, G43, G44, G45), s83_r2_wrap_up.md (5-axis framing), Abazajian_2022_CMB_S4_forecast.md, LiteBIRD_projections.md, SKA_2_projections.md, Hyper_K_ALP.md | all `<computed-at-runtime>` |

Closure SHA = SHA-256(sorted ordered input-pin map). Every script prints closure SHA in the first 20 lines of stdout; verdict line is the final non-verdict line with closure SHA appended.

Dual-SHA schema (S84+):
- `audit_sha256`: SHA-256 of input-pin map (reproducibility)
- `content_sha256`: SHA-256 of script source (tamper detection)

Both mandatory on every verdict line per S84+ schema.

---

## W10b Expected Outputs

Per-gate deliverables required before S84 verdict-log close:

- `computations/s84_w10b_biographical_framing_audit.py` (non-stub, includes neutral-prompt-template + adjudication-aggregation logic)
- `computations/s84_w10b_alpha_s_derivation_chain_audit.py` (non-stub, includes symbolic differentiation + cross-checks a/b/c/d)
- `computations/s84_w10b_cmbs4_joint_discriminator_plane.py` (non-stub, includes 5×5 Fisher + per-axis σ-separation + PASS/INFO/FAIL verdict + Mahalanobis distance)
- `computations/s84_gate_verdicts.txt` appended with 3 verdict lines (gates 122, 123, 124)
- Working-paper §VII-GEAR-MACHINE (for gate 122 landing): PASS updates the CORROBORATED sub-section; INFO/FAIL adds the CAVEAT sub-section
- Working-paper §VII-THEOREM-REGISTRATION (for gate 123 landing): PASS registers α_s = n_s² - 1 as permanent theorem; INFO/FAIL amends the registration
- Working-paper §VII-DETECTOR-FORECAST (for gate 124 landing): PASS cites 5-axis plane as joint discriminator; INFO/FAIL includes per-axis σ table with qualifications
- Carry-forward entries for S85:
  - If gate 122 = FAIL: S85-NEUTRAL-PROMPT-PROTOCOL methodology-debt item
  - If gate 123 = INFO/FAIL: S85-ALPHA-S-AXIOM-DERIVATION refinement computation
  - If gate 124 = INFO/FAIL: S85-JOINT-DISCRIMINATOR-REFINEMENT (axes uplift) and S85-QUALITATIVE-NEW-AXES exploration

---

## W10b Closing Note

Wave 10b executes the three carry-forward items flagged "optional / lower-priority" in §4.M. Lower-priority does NOT mean lower-quality: all three gates are pre-registered with explicit thresholds, PRDR-pinned machinery, and substitution-chain discipline. The gates are lower-priority in the sense that they do not unblock any downstream primary computation (unlike W1's BASELINE-HTILDE-SENSITIVITY or W7a's EQUIV-CLASS-FALSIF which directly gate §VII.N landing).

The three gates are characterologically distinct:
- Gate 122 is a methodology audit — it examines the agent-workshop apparatus itself, asking whether biographical framing drove a prior workshop convergence. Its value is self-corrective regardless of outcome: PASS corroborates the apparatus, FAIL identifies a methodology improvement.
- Gate 123 is a structural derivation audit — it examines whether a permanent-registered identity (α_s = n_s² - 1, S50) traces to minimal axioms. Its value is potentially HIGH-leverage: a FAIL demotes S84-ALPHA-S-PRE-REGISTRATION (gate 7, §4.A) from zero-free-parameter discriminator to consistency-check, affecting the framework's 2030 observational-falsifier portfolio.
- Gate 124 is a detector-forecast consolidation — it formalizes the 5-axis discrimination plane into a pre-registered joint Fisher test. Its value is forward-looking: the verdict establishes whether 2030s observations will DECISIVELY test the framework or merely CONSTRAIN it.

All three gates have LOW computational effort (no GPU, no large matrices, no long scans). The time cost is primarily in careful prompt construction (gate 122), careful axiom-tracing (gate 123), and careful Fisher-matrix specification (gate 124). No W10b gate contends for the 8-concurrent-agent dispatch cap.

Wave 10b is designed so that all three outcomes (PASS, INFO, FAIL) produce actionable landings. No dispatch returns null information. The gates test the framework at the boundary of its self-audit apparatus, derivation-integrity backbone, and observational-discrimination horizon.
