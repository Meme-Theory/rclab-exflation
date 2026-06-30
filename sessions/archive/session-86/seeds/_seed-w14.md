# Seed file — sessions/archive/session-86/session-86-w14-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w14-workingpaper.md` (832 lines, 141 KB)

## Candidates

### Candidate 1 — SW3 / ¹⁷³Yb λ_8 unique-direction substrate-falsification audit

**What it would do**: A 2-agent workshop interrogating the W14-6 §VII synthesis claim that SW3 (¹⁷³Yb sweet-spot, δE_a = 2.85 at λ_8) is the framework's unique single-row λ_8 substrate-direction trigger. The workshop would (a) verify whether the claim is structural (no other lab platform projects onto λ_8 at 5-yr decisive precision) or contingent (other platforms could resolve λ_8 at lower precision but were excluded by EVOI level cuts); (b) test whether a FAIL-AT-LAB on SW3 closes ALL of the substrate's λ_8 content or only the lab-energy-scale portion that ¹⁷³Yb's 3-body Γ-channel probes; (c) quantify the lambda_8 / lambda_6 / lambda_7 EVOI weight asymmetry that gives SW3 outsized leverage.

**Why it's worthwhile**: The W14-6 working paper §"Substrate-direction coverage analysis" claims SW3 is the *strongest single-row substrate-direction-falsification trigger* in the lab portfolio (line 769) and that "a FAIL-AT-LAB on SW3 closes the lambda_8 substrate direction at lab precision, an exposure no other row supplies" (line 712). This claim was surfaced as a NEW structural observation at suite level — meaning P11 (W13) landed the 9-row class without seeing it, and only the W14-6 audit-pin upgrade exposed the asymmetry by reading per-row platform/lambda cells together. A single-row trigger of this leverage deserves explicit verification: is it irreducibly unique, or is it an artifact of how W11 C6 EVOI-tree pre-pruned the candidate observable list? If unique, it should be promoted to a top-3 EVOI item in the next session's lab portfolio. If contingent, its prominence in the W14-6 narrative is overstated.

**Type**: 2-agent workshop

**Suggested agents**: volovik-superfluid-universe-theorist, mack-cosmic-bridge

**Rounds (workshops only)**: 2 default (R1 = volovik steelman SW3-uniqueness via 3He-A / FeSe / Yb λ-coverage analysis; R2 = mack adjudication on EVOI-tree branch sensitivity)

**Context the workshop will need**: W14-6 §"Substrate-direction coverage analysis" (line 769) + §"Substrate-framing assessment" (lines 700-705) of W14 WP; `s85_w8_su3_op_lab_predictions.py` proj_kelvin = {6: 0.90, 7: 0.30, 8: 0.10} (cited line 618); 9 atomic rows in falsifier-master-inventory.md #13-#21; W11 C6 EVOI-tree at `s86_w11_lab_falsifier_evoi_tree.json` (path cited line 712); 7 newly-promoted dE_a constants in canonical_constants.py SECTION E (W14-6 promotion); W12 C30 detector-readiness verdict at `s86_gate_verdicts.txt:178`.

---

### Candidate 2 — (A)/(C) regulator-class adjudication: which class wins under LISA observation?

**What it would do**: A solo synthesis (1 agent) that walks the (A)/(C) regulator-class partition introduced as standalone audit-paragraph content in W14-3 row 7.audit. The W14-3 paragraph names F_4 = {ζ, Zubarev, SDW} (A-class, predicting Ω_GW(LISA) ~ 10⁻¹⁰ band, LISA-detectable) vs M = {cutoff_sqrt, anomaly} (C-class, predicting Companion-null Ω_GW(LISA) = 8.299e-58, 45-OOM null). The synthesis would (a) audit whether the framework's a_4 spectral-moment derivation under each of the 5 regulators is structurally complete or whether some are approximations; (b) determine if the (A)/(C) bipolar split is structurally exhaustive or whether intermediate regulator classes exist; (c) interrogate whether the LISA discrimination is binary-clean (A wins → 11 OOM band, C wins → 45 OOM null, no overlap) or carries scheme-uncertainty in the A-class band itself.

**Why it's worthwhile**: W14-3 §"Substrate-framing assessment" (line 291-296) treats (A)/(C) as a substrate-internal regulator-class commitment INSIDE the spectral triple, not a framework-vs-LCDM split. The audit-pin sub-row landed full-64-hex W13-2 closure but introduced the new bipolar discriminator content without independent verification. The discriminator paragraph cites lizzi S-7 §V.6 Mellin Strip Theorem as the partition source — this should be cross-checked structurally. If the (A)/(C) partition is exhaustive and binary-clean, the LISA reading at the 2030s mid-decade horizon becomes a single-experiment regulator-class adjudication for the framework's spectral-action regulator commitment. If it has internal scheme-spread within the A-class, the LISA-detection threshold is fuzzier than the 11-OOM-band claim suggests.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist

**Context the synthesis will need**: W14-3 §"Route adjudication" (lines 224-243), §"Substrate-framing assessment" (lines 289-295), and Notes-section content in `sessions/framework/registry/falsifier-master-inventory.md` row 7.audit; W13-2 verdict `S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT` at `s85_gate_verdicts.txt:201` value = (alpha_s=-0.068968, Omega_GW_LISA=8.299e-58, rho_cc=0.0, Fisher_PD=1); lizzi S-7 §V.6 Mellin Strip Theorem source; `s85_w13_2_cgwb_alpha_s_joint.py` Fisher pin SIGMA_LISA_OMEGA_GW = 1.0e-12 (cited W14-3 line 215); `.claude/rules/regulator-pin-discipline.md` for a_n^{<regulator>} canonical-form rule.

---

### Candidate 3 — f_NL_folded 14× pathway-spread: scheme-dependence diagnostic vs scheme-canonicalization theorem

**What it would do**: A 2-agent workshop (volovik + landau via lizzi) examining the W14-4 §"Solution-space interpretation" claim (line 430) that the 14× spread across 3 pathway values (S82 0.0547 / S67 0.129 / S85 W9-3 0.7685) is a "SCHEME-DEPENDENCE diagnostic of the spectral-projection convention, NOT a model uncertainty." The workshop would (a) verify whether the 3 pathways are mutually consistent under a substrate-level scheme-canonicalization (i.e., do they collapse to one number under a canonical projection, or are they irreducibly distinct shape-projection conventions?); (b) test whether the 14× spread is dominated by L_max difference (Pathway C uses L_max=100000, Pathways A/B use L_max=10) or by genuine convention difference; (c) determine which pathway dominates SKA-1's 21cm bispectrum Fisher-template inner product, since SKA-1 σ ≈ 0.15 (folded ridge) is the only 2030s instrument with non-trivial sensitivity to any pathway value.

**Why it's worthwhile**: The W14-4 working paper §"Substrate-framing assessment" (lines 414-422) establishes that the 3 pathways are "three DIFFERENT spectral-derivation routes through the SAME substrate triple D_K" — meaning they are not competing models but different observable-projection coordinates on the same substrate manifold. The 14× spread is therefore a measure of how much downstream observation depends on which projection the detector inner-product effectively performs. SKA-1 σ ≈ 0.15 is 1+ OOM smaller than Pathway C (0.7685) but ≥ 5× larger than Pathways A/B — meaning the framework's detection prediction depends crucially on which pathway dominates SKA-1's response. A null detection at SKA-1 closes Pathway C but leaves A/B detector-sterile and unfalsifiable until next-generation instruments. The workshop would clarify whether this ambiguity is fundamental (different shape-projections genuinely disagree on what folded f_NL means) or technical (one pathway is the "right" SKA-1-coupled projection and the others are convention errors).

**Type**: 2-agent workshop

**Suggested agents**: volovik-superfluid-universe-theorist, lizzi-spectral-functional-theorist

**Rounds (workshops only)**: 2 default (R1 = volovik on substrate origin of each pathway shape projection; R2 = lizzi on Fisher-cosine inner product canonicalization with SKA-1 template)

**Context the workshop will need**: W14-4 §"Source-resolution table" (lines 351-356) with the 3 canonical verdict pairs; `f-nl-folded-pathway-registry.md` (P10) at `sessions/framework/`; `s67_gge_bispectrum.py`, `s85_w9_folded_triangle_21cm_shape.py`, `s82_w3_4_gge_fnl.py` source scripts; SKA-1 σ ≈ 0.15 Fisher pin (W14-4 line 428); session-67-final.md:1393 prose anchor for f_NL^diag = 1/sqrt(N_pair) Bogoliubov-pair Poisson statistics derivation; CMB-S4 σ ≈ 5.0–6.9 from S68 CMBS4-FNL-FORECAST (W14-4 line 394).

---

### Candidate 4 — Inventory-as-canonical-source: registry-coupling architectural review

**What it would do**: A solo synthesis examining the structural fact W14 surfaced — that `sessions/framework/registry/falsifier-master-inventory.md` has become the de-facto canonical source for 5 framework headline observables (w_0, α_s, Ω_GW_LISA, f_NL_folded, A_s) while `computations/canonical_constants.py` (the official canonical-constants module imported by computation scripts S34+) has not been kept in sync. Review whether (a) the inventory should be a derived view of canonical_constants.py + verdict files, or whether canonical_constants.py should be a derived view of the inventory; (b) what the canonical write-order should be when a new framework-prediction is generated (verdict file → canonical_constants.py → inventory? or verdict file → inventory → canonical_constants.py?); (c) what hooks should fire on `/weave --update` to enforce sync; (d) whether the audit-pin sub-row pattern (3.audit / 7.audit / 9.audit / 12.audit / 21.audit-block) should be a permanent inventory-row schema convention or scaffolding for one-time SHA-discipline migration.

**Why it's worthwhile**: W14 surfaced a 5-gate consistent registry-coupling deficiency (W14-2/3/4/5/6 all hit `Constant 'X_FW' not found` for their respective observables). The W14 wave-synthesis §3 (line 761-763) frames this as a "systemic canonical-constants registry deficiency" and consolidates it to S87 W0 cleanup. But the underlying architectural question — which artifact is the canonical source for framework predictions — is not addressed. If S87 W0 cleanup just adds entries without resolving the source-of-truth ambiguity, the same deficiency will re-surface in S88+ when new predictions land. The inventory-vs-canonical_constants synchronization should be designed once at architecture level, not patched session-by-session.

**Type**: solo (1 agent)

**Suggested agents**: gen-physicist (or alternatively, mack-cosmic-bridge as the W14 producing-agent with full registry context)

**Context the synthesis will need**: W14 wave-synthesis §3 (lines 761-763) + §6 (lines 783-794) of W14 WP; `computations/canonical_constants.py` (current state, post-W14-6 SECTION E expansion); `sessions/framework/registry/falsifier-master-inventory.md` (post-W14 state); `.claude/rules/agent-standards.md` §"What must NOT live in agent memory" → `sessions/framework/<registry>.md` template; `.claude/rules/math-scripts.md` §"Canonical Constants (MANDATORY)"; the consolidated `S87-CANONICAL-CONSTANTS-W14-RESIDUAL` carry-forward 4-field spec (W14-3, W14-4, W14-5, W14-6 contributions accumulated).

---

### Candidate 5 — Parallel-session race detection and prevention: W14-1 timing-honest FAIL postmortem

**What it would do**: A short solo synthesis examining the W14-1 / P11 (W13) timing race that produced the only FAIL in the wave. W14-1 was authored expecting Row #1 = w_0; on-disk Row #1 was = r tensor-to-scalar; meanwhile P11 was concurrently creating Row #1 = w_0 (the row W14-1 expected). The FAIL is timing-induced ("clean route-b FAIL" with proper diagnostic), but the carry-forward `S86-INVENTORY-W14-1-ROW-W_0-CREATION` became MOOT minutes later when P11 landed independently. Synthesis examines (a) whether the orchestrator-side parallel-session lock-detection mechanism that should have caught this exists; (b) whether plan §W14-1 should have been authored against post-P11 inventory state in the first place (i.e., wave dependency declaration W14 → W13 P11); (c) what the cleanup pattern is when a FAIL becomes MOOT due to parallel-session resolution (re-dispatch W14-1 against post-P11 state? close as MOOT? convert FAIL → INFO retroactively? — the WP §6 line 789 marks W14-1 retry as "Optional: re-dispatch W14-1 against post-P11 state to convert FAIL → PASS via incremental delta ... LOW priority since W14-1 carry-forward is moot").

**Why it's worthwhile**: The FAIL preserves audit honesty — that part is correct (W14 §1 line 745). But the systemic issue is that wave-dependency was implicit, not declared. P11 was executed in W13 and W14-1 was authored against an inventory snapshot that predated P11; the orchestrator dispatch of W14 did not check that P11 had already landed. The same race could happen again at S87+ if not addressed structurally. The fix is at the plan-authorship and orchestrator-dispatch level, not at the per-gate retry level. Low priority but architecturally clarifying — and the WP itself flags W14-1 retry as "LOW priority" but does not address the systemic prevention question.

**Type**: solo (1 agent)

**Suggested agents**: gen-physicist (orchestrator-protocol-discipline scope, fits gen-physicist's rules-and-procedures domain)

**Context the synthesis will need**: W14 WP §1 (lines 741-748) "Structural outcome — parallel-session race surfaced", §6 (line 789) downstream-implications W14-1 retry candidacy row; P11 verdict line at `s86_gate_verdicts.txt:203` (S86-MASTER-INVENTORY-W6-W13-LAND); W14-1 verdict at `s86_gate_verdicts.txt:199` (FAIL); `.claude/rules/v3-closure-recovery.md` Stage-1/2/3 procedure (does it cover MOOT-by-parallel-resolution case?); `.claude/rules/teammate-behavior.md` "One writer per output" rule (W14 was sequential single-owner, mack-cosmic-bridge for all 6 — so the race was inter-WAVE, not intra-wave).
