# Session 116 Wave 7 — Q33 §VII.AJ.STATE-PROJ derivation (Results Working Paper)

**Session**: 116 | **Wave**: 7 | **Plan**: session-116-plan-w7.md | **Theme**: Q33 — resolve the `§VII.AJ.STATE-PROJ` companion slot (OPEN/NEEDS-COMPUTATION since S88 W7+W10). Derive the substrate-IS BCS-occupation state-pair functional `R_STATE = (a−b)/(a+b)` and pre-register whether it reproduces the laboratory 3He A/B gap-square asymmetry `R_3HeB_lit = +0.03536` at the polycritical point `P_pc = 21.22 bar` — and, the load-bearing discriminator, whether the controlling gap ratio `Δ_B/Δ_A` is a substrate-first q-theory prediction (Track A, genuine 0-parameter) or the lab strong-coupling ratio re-expressed (Track B, consistency-check / circular); then adjudicate (volovik × landau) whether STATE-PROJ (algebra-DEPENDENT, `+0.03536`) is ORTHOGONAL to OP-PROJ (algebra-INVARIANT, `R_∞ ≈ −1.892`) under the algebra-axis orthogonality K-counter, or whether the two projection-side readings COLLAPSE.

**Gate-type mix**: compute × 1 (`§W7-1`, `[SIGN]` verdict-line closure) + workshop × 1 (`§W7-2`, artifact-existence closure). MIXED wave per `.claude/rules/wave-classification.md`.

## Gate Sections

### §W7-1. S116-W7-STATEPROJ-BCS (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S116-W7-STATEPROJ-BCS`
**Gate type**: `compute` (dual-SHA verdict-line closure; `[SIGN]` ⇒ SIGN/MAGNITUDE/REGIME 3-tuple companion row REQUIRED)
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (BCS occupation of the substrate BdG state inherited via ι : ℂ⊕ℍ⊕M₃(ℂ) → M₂(ℂ))
**Agent**: `volovik-superfluid-universe-theorist` (3He-B inheritance + substrate-IS BCS-state owner; `nazarewicz-nuclear-structure-theorist` = math cross-check for the strong-coupling gap equation)
**Hypothesis**: The substrate's BdG BCS occupation distribution admits an algebra-DEPENDENT state-pair functional `R_STATE = (a−b)/(a+b)` (a, b = condensation-energy / pairing-occupation weights of the two inherited gap sectors at the polycritical point) reproducing `R_3HeB_lit = +0.03536` with `sign=PASS` by `SC_A = 1.151 > SC_B = 1.111`; the load-bearing discriminator is the PROVENANCE of `Δ_B/Δ_A`. **Composite PASS iff (3-tuple PASS ∧ Track A substrate-first q-theory gap ratio); composite INFO iff (3-tuple PASS ∧ Track B lab-SC-ratio re-expressed — near-tautological, NOT a prediction); composite FAIL iff magnitude FAIL (>0.25 relative)** per the plan's `dual_prior` track-discriminator, which OVERRIDES the generic 3-tuple collapse (plan-frozen operator precedence, `gate-verdicts.md`).
**Plan reference**: `sessions/session-plan/session-116-plan-w7.md` §W7-1 (PRDR 8-item machinery pin, composite-precedence `dual_prior` track discriminator, substitution chain Def1–Def3, conditional 5-anatomy + 3-level registry-landing block, input-SHA ledger, SOURCE-RECON pre-step).

**Output Artifacts** (closure-verification checklist — verified on disk):

| Artifact | Path | must_contain (grep-verified) |
|:--|:--|:--|
| script | `computations/session-116/s116_w7_stateproj_bcs.py` | `from canonical_constants import` (1) + `print_verdict_payload` (2) — PASS |
| data | `computations/session-116/s116_w7_stateproj_bcs.npz` | exists (13,195 B) — PASS |
| plot | `computations/session-116/s116_w7_stateproj_bcs.png` | exists (176,048 B) — PASS |
| verdict line | `computations/session-116/s116_gate_verdicts.txt:59` | `^S116-W7-STATEPROJ-BCS:.* audit_sha256=[a-f0-9]{64}` — PASS |
| dual-SHA companion | line 60 | `content_sha256=f8bf65949efc2fe8...` — PASS |
| `[SIGN]` 3-tuple | line 61 | `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` — PASS |
| composite-precedence | line 62 | `# composite-precedence: dual_prior-track-discriminator (W7-1; generic-collapse PASS overridden to INFO under Track B)` — PASS |
| provenance rows | lines 63-64 | Δ_B/Δ_A LAB provenance + BdG-occupation realization — PASS |
| canonical anchors | `computations/_shared/canonical_constants.py:721-727` | SC_corr_A / SC_corr_B / delta_A_over_kBTc / delta_B_over_kBTc / P_pc / T_pc / R_3HeB_lit — all LABORATORY-IN — PASS |

`audit_sha256=0968093bd6272475641d88bd54b3cfef199b55b1c57ba14bd3298a6b78b07c0a` (unique across the session verdict file — sig_5 OK); `content_sha256=f8bf65949efc2fe85a5792fb5003051ea56603a0b5e520f2eefb000a00c23c36`. **CLASS = FULL** (built from `canonical_constants` + the cached D_K spectrum ONLY; no `_spectral_action_regulators.py` SCHEMATIC helper → no `-SCHEMATIC` suffix). No `a_n` Seeley-DeWitt regulator pin (condensation energy ∝ Δ² is not a spectral moment).

**MCP Pre-Compute Audit** (queries run BEFORE the script; per `knowledge-index-usage.md`):

- `search_knowledge("3He-B STATE-PROJ OP-PROJ gap asymmetry polycritical strong-coupling SC_corr")` → the S88 W4c cluster `SC_corr_A=1.151`, `SC_corr_B=1.111`, and **`delta_B_over_delta_A_q_theory = 0.96528 (= 1.9597/2.0302)`** + the §VII.AV OP-PROJ/STATE-PROJ slot-split precedent (S93 W3-1/W3-5). The parenthetical `(= 1.9597/2.0302)` is the decisive Track-B tell: a "q_theory"-NAMED ratio whose STRUCTURE is the lab reduced-gap ratio.
- `trace_entity("delta_B_over_delta_A_q_theory")` → `extraction_methods = ["Greywall_thermometric", "Halperin_Hammel_ladder", "Volovik_q_theory"]` — all three are LAB extractions of the SAME real-3He gap; NOT three independent substrate derivations.
- `get_constant("Delta_BCS")` → `0.4642547394830737` (R-protected; the substrate's SINGLE canonical gap).
- `get_constant("SC_corr_A")` / `get_constant("R_3HeB_lit")` → **NOT found** → SOURCE-RECON pre-step fired: 7 polycritical anchors ADDED to `canonical_constants.py` SECTION E with explicit LABORATORY-IN provenance (Greywall 1986 / Serene-Rainer 1983 / Volovik 2003 Ch.7) BEFORE script import.
- S87 npz inspection: `R_3HeB_lit = 0.0353559` built from `Delta_A_at_pc = 2.0302224`, `Delta_B_at_pc = 1.9596673`, `path_used = 'lit'`, `verdict = FAIL` (the `ratio_mismatch = 1.029` that split §VII.AJ).
- NOT PRE-CLOSED: §VII.AJ.STATE-PROJ is OPEN/NEEDS-COMPUTATION since S88 W7+W10; this is its first substrate-IS evaluation.

**Verdict**: **INFO** (Track B). `composite = INFO` via the plan-frozen `dual_prior` track-discriminator (the `[SIGN]` 3-tuple is all-PASS, but **Track B** overrides the generic-collapse PASS). 3-tuple: `sign_verdict=PASS` (R_STATE > 0; SC_A=1.151 > SC_B=1.111) · `magnitude_verdict=PASS` (`rel_match = 0.0`) · `regime_verdict=VALID` (single-point polycritical; closed form exact at common-N(0) coexistence). Had the controlling gap ratio been substrate-first (Track A), the identical 3-tuple would have closed **PASS**. `audit_sha256=0968093b…07c0a`.

**Results**:

**R_STATE = +0.0353559** — bit-identical to `R_3HeB_lit = 0.035355875960583226` (`rel_match = 0.0`).

*Substitution chain (the `[SIGN]` directional claim, with substituted numbers):*
- Def 1: `a := |E_cond^A| = ½ N(0) Δ_A²` — A-sector BCS condensation energy; a STATE-pair functional `ρ_BCS(P_A·H_pair)`, **algebra-DEPENDENT**.
- Def 2: `b := |E_cond^B| = ½ N(0) Δ_B²` — B-sector; common `N(0)` at A-B coexistence (polycritical).
- Def 3: `Δ_A = (π e^−γ)·SC_A`, `Δ_B = (π e^−γ)·SC_B`; `π e^−γ = 1.7638770`; `SC_A = 1.151`, `SC_B = 1.111`.
- Substitute Def1,Def2 → `R_STATE = (½N(0)Δ_A² − ½N(0)Δ_B²)/(½N(0)Δ_A² + ½N(0)Δ_B²)`; `½N(0)` cancels → `(Δ_A²−Δ_B²)/(Δ_A²+Δ_B²)`.
- Substitute Def3 → `(π e^−γ)²` cancels → `(SC_A²−SC_B²)/(SC_A²+SC_B²) = (1.324801−1.234321)/(1.324801+1.234321) = 0.090480/2.559122 = +0.0353559`.
- Direction: `SC_A > SC_B ⇒ SC_A² > SC_B² ⇒ numerator > 0 ⇒ R_STATE > 0`. **sign = PASS**. (The plan's `+0.0353564` used 4-sf SC; identical to 6 sf. The 4-sf reduced-gap reduction `(2.0302²−1.9597²)/(…) = +0.0353282` differs only by the 4-sf rounding of `2.0302/1.9597` vs `SC·π e^−γ`.)

**TRACK = B (lab strong-coupling ratio re-expressed; near-tautology, NOT a substrate-first prediction).** *This is the gate's PRIMARY deliverable — the provenance, not the arithmetic.*

*Factor-by-factor provenance of the controlling ratio `Δ_B/Δ_A = SC_B/SC_A = 0.965248`:*
- `π e^−γ = 1.7638770` — UNIVERSAL weak-coupling BCS prefactor; appears in BOTH `Δ_A` and `Δ_B` and **CANCELS** in the ratio → non-discriminating (cannot supply substrate-first content to the ratio).
- `SC_corr_A = 1.151` — **CONTROLLING factor; LABORATORY-IN**: 3He-A strong-coupling enhancement `= (Δ_A/k_BT_c)/(π e^−γ) = 2.0302/1.7639`; a spin-fluctuation FEEDBACK factor set by 3He's Landau parameters (Serene-Rainer 1983 weak-coupling-plus; Greywall 1986 thermometry).
- `SC_corr_B = 1.111` — **CONTROLLING factor; LABORATORY-IN** (Serene-Rainer / Greywall).
- The index constant NAMED `delta_B_over_delta_A_q_theory = 0.96528` has STRUCTURE `(= 1.9597/2.0302)` = the LAB reduced-gap ratio; the S88 W4c "three extraction methods" (Greywall thermometric / Halperin-Hammel ladder / Volovik q-theory) are three LAB extractions of the SAME real-3He gap, NOT three independent derivations. **NAME ≠ PROVENANCE** (Observable-Naming-History vs Parse-Tree-Structure, `cross-pillar-bridge-anatomy.md`).

*Why Track A is structurally unavailable (substrate-physics — the content the Volovik/superfluid authority is positioned to assert):*
1. The substrate is a SINGLE BDI-class object (3He-B child, `N_3 = 0`; S44). 3He-A is DIII (Fermi point, `N_3 = 2`). The substrate has NO intrinsic 3He-A sector → no substrate-first `Δ_A`; the "A-sector central projection `P_A`" is a formal algebra projection, not a second physical superfluid phase the substrate selects.
2. The SC corrections are 3He MATERIAL PROPERTIES (spin-fluctuation feedback set by 3He Fermi-liquid parameters `F_0^a, F_1^s`). The substrate's canonical `Δ_BCS = 0.4642547` (M_KK units) is a SINGLE weak-coupling-class gap; it does not split into an A/B pair carrying 3He-specific feedback.
3. The Volovik q-theory (the "S58 Volovik-partition canonical" the S88 plan invoked) governs the vacuum 4-form variable `q` and the equilibrium CC (`Λ = −P_vac = 0`; DILUTION-CC) — NOT the superfluid gap-anisotropy strong-coupling corrections. Naming the lab ratio "q_theory" conflates the vacuum-energy machinery with unrelated gap-feedback physics.

⇒ `substrate_first_SC_ratio_available = False`. The reproduction of `+0.03536` is a **TAUTOLOGY**: `R_STATE` and `R_3HeB_lit` are BOTH `(SC_A²−SC_B²)/(SC_A²+SC_B²)` from the same two lab numbers — 0 independent bits. The script confirms the S87 "lab gaps" ARE `SC_corr·π e^−γ` exactly (`gap_A_equals_SC_A_times_pieg = 0.0`, `gap_B = 0.0`).

*BdG-occupation realization (state-pair functional FORM check — confirms STATE-PROJ is genuinely algebra-DEPENDENT; NOT a provenance route):* on the cached substrate `D_K(τ_fold)` spectrum (78,080 modes, `p+q ≤ 10`), with `Δ_A^sub = Δ_BCS·SC_A`, `Δ_B^sub = Δ_BCS·SC_B`, the BCS condensation energy `E_cond(Δ) = Σ_k[|ξ_k| − E_k + Δ²/(2E_k)]` gives `a_BdG = ρ_BCS(P_A·H_pair)`, `b_BdG = ρ_BCS(P_B·H_pair)`, `R_BdG = +0.068847`. **SAME POSITIVE SIGN** as `R_STATE` → confirms `(a−b)/(a+b)` is a GENUINE state-pair functional on the substrate BdG occupation `v_k² = ½(1 − ξ_k/E_k)`, not a bare algebraic identity. The magnitude differs (`R_BdG − R_STATE = +3.35e−2`) — a finite-DOS-curvature correction: the substrate's own gap scale `Δ_BCS·SC ≈ 0.5 M_KK` is NOT in the weak-gap limit `Δ ≪ ξ` where `E_cond ∝ Δ²` exactly. The closed-form (`a,b ∝ Δ²`) is the common-N(0) coexistence idealization the LAB form uses; the form check (sign + algebra-dependence) is what feeds §W7-2.

**SIGN FLIP vs §VII.AJ.OP-PROJ** (structural input to §W7-2): STATE-PROJ `R_STATE = +0.0354 > 0` (condensation-energy occupation asymmetry; A-analog more deeply paired) vs OP-PROJ `R_∞ ≈ −1.892 < 0` (S87 substrate spectral count `R_substrate = −1.2122` at L_max=10). A spectrum-only count excess is NEGATIVE; a condensation-energy occupation asymmetry is POSITIVE. The sign flip + the ≈50× magnitude gap are structural evidence the two projection-side observables are ORTHOGONAL (different sign, different algebra-axis corner) — volovik's input to the W7-2 orthogonal-vs-collapse adjudication.

**`dual_prior` posterior**: INFO (3-tuple PASS ∧ Track B) → 0.85 mass to Track B. The slot is well-defined (algebra-DEPENDENT state-pair functional) but its substrate-first PREDICTION content is absent.

**4-tuple**: (scheme = `STATE-PROJ-BCS-condensation-energy-state-pair`, convention = `(a−b)/(a+b)-A-B-coexistence-condensation-energy + STATE-PROJ`, L_max = 10), `publication_precision = 4`. **CLASS = FULL**.

**SOURCE-RECON / SUBSTRATE-FIRST pre-step (effected in-session)**: 7 LABORATORY-IN polycritical anchors ADDED to `canonical_constants.py` SECTION E (lines 721-727) with explicit provenance (Greywall 1986 PRB 33 7520 / Serene-Rainer 1983 / Volovik 2003 Ch.7): `SC_corr_A=1.151`, `SC_corr_B=1.111`, `delta_A_over_kBTc=2.0302`, `delta_B_over_kBTc=1.9597`, `P_pc=21.22` bar, `T_pc=2.273e-3` K, `R_3HeB_lit=0.035355875960583226`. Each comment carries the "LABORATORY-IN … NOT substrate-first" tag — load-bearing for the Track determination.

**`fb_pair`** — forward: `S87-3HEB-EXCESS-INHERITANCE-COMPARISON` (the FAILED comparison motivating the OP/STATE split) + §VII.AJ.OP-PROJ STAGE-1-CANDIDATE companion + `Delta_BCS` canonical + the (absent) substrate q-theory gap ratio. backward: §VII.AJ.STATE-PROJ slot status + §W7-2 workshop (consumes `R_STATE` sign + Track) + the algebra-axis K-counter + future 3He-B polycritical falsifier rows.

**Conditional landing — INFO (Track B)**: §VII.AJ.STATE-PROJ is NOT registry-PASS-landed. The slot is RESERVED **`REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`** (S2 advisory; `cross-pillar-bridge-anatomy.md` "Deferred-pending intermediate verdict-class" — well-defined algebra-DEPENDENT state-pair functional, but its substrate-first prediction content awaits an independent substrate derivation of `SC_corr_A`, `SC_corr_B`). §VII is the `mack-cosmic-bridge` sole-writer surface → NO registry write here; the orchestrator routes the slot-status note to mack at §6. The 5-anatomy / 3-level spec is pre-registered in plan §W7-1's registry-landing block (Substrate-IS `R_STATE = (a−b)/(a+b)`; Lab-IN `R_3HeB_lit`; bridge `ι_* ∘ (Δ_B/Δ_A)^{p=0}`; Level-2 BCS gap-equation band binding; Level-3 `+0.03536`), to be ACTIVATED only when Track B → Track A.

**Carry-forward — `CF-S117-STATEPROJ-SC-FROM-SUBSTRATE`** (genuine future computation; 4-field):
- **What**: independent SUBSTRATE-FIRST derivation of the strong-coupling corrections `SC_corr_A`, `SC_corr_B` (equiv. `Δ_B/Δ_A`) from the framework's OWN q-theory Volovik-partition / spectral-action strong-coupling physics, with NO 3He lab input — converting Track B → Track A.
- **Inputs**: `Delta_BCS` (canonical); the q-theory partition machinery (S58/S66 DILUTION-CC); spectral-action strong-coupling corrections to the gap; the BdG sector structure on `A_K = ℂ⊕ℍ⊕M₃(ℂ)`.
- **Gate**: PASS iff a substrate-computed `Δ_B/Δ_A` reproduces `0.96525 ± (substrate band)` WITHOUT importing `SC_corr_A/SC_corr_B` → `R_STATE` becomes a genuine 0-parameter prediction and §VII.AJ.STATE-PROJ lands registry-PASS (Track A). **Pre-flight obstruction**: the substrate must FIRST exhibit two distinct gap sectors — the single-BDI-object / no-intrinsic-A-sector obstruction above must be resolved or shown to map to an `A_K` central-projection pair with computably-distinct couplings.
- **Effort**: 1-2 days; HIGH-RISK given the no-A-sector obstruction.

**dual-SHA**: `audit_sha256 = 0968093bd6272475641d88bd54b3cfef199b55b1c57ba14bd3298a6b78b07c0a` (over script‖`canonical_constants.py`‖pinmap{s84_spectrum_cache, s87_comparison_npz, Volovik #03}); `content_sha256 = f8bf65949efc2fe85a5792fb5003051ea56603a0b5e520f2eefb000a00c23c36` (script only). Artifacts: `s116_w7_stateproj_bcs.py/.npz/.png`.

**Substrate-first PHONONIC framing**: the substrate IS the BdG BCS ground state on `(A_K, H_K, D_K)`. The 3He-B cell is a CONTROLLED REALIZATION of the same BDI universality class via the parent→child inheritance morphism `ι : ℂ⊕ℍ⊕M₃(ℂ) → M₂(ℂ)` (NOT analogy; `3HeB-inheritance-canonical.md`). Direction: `D_K eigenvalues → BdG occupation v_k² in the BCS state → condensation-energy state-pair functional ρ_BCS(P_sector·H_pair) → R_STATE = (a−b)/(a+b) → the lab MEASURES R_3HeB_lit IN the cryostat at (P_pc, T_pc)`. What this gate establishes: the substrate's algebra-DEPENDENT state-pair FUNCTIONAL is well-formed and positive (a genuine occupation asymmetry), but the NUMBER it currently reports is the lab's own gap ratio fed back in — at present the substrate is MEASURING 3He, not PREDICTING it. The honest substrate-first claim is the FORM (STATE-PROJ is a genuine algebra-DEPENDENT functional, orthogonal-companion to the algebra-INVARIANT OP-PROJ), not the value.

---

### §W7-2. S116-W7-ALGEBRA-AXIS (volovik-superfluid-universe-theorist × landau-condensed-matter-theorist)

**Status**: NOT STARTED
**Gate ID**: `S116-W7-ALGEBRA-AXIS`
**Gate type**: `workshop` (2-agent adversarial panel; closes by artifact-existence-with-content per `wave-classification.md §M1` — NO verdict line)
**Trigger**: `[VERIFY]` (algebra-axis orthogonality adjudication, not a numerical SIGN gate)
**Classification**: **PHONONIC** (both projection-side observables are substrate-IS on (A_K, H_K, D_K); the workshop decides orthogonal companions vs collapse)
**Agents**: `volovik-superfluid-universe-theorist` (ORTHOGONAL pole — algebra-axis 4-corner separation + regulator-response sibling discriminator) × `landau-condensed-matter-theorist` (COLLAPSE pole — BCS gap-equation mean-field linkage steelman)
**Rounds**: 3 (R1 steelman both readings / R2 respond to opponent's best case / R3 converge → STRUCTURAL VERDICT)
**Hypothesis**: `§VII.AJ.STATE-PROJ` (`R = +0.03536`, algebra-DEPENDENT state-pair functional `ρ_BCS(P_sector · H_pair)`) and `§VII.AJ.OP-PROJ` (`R_∞ ≈ −1.892`, algebra-INVARIANT spectrum-only `F({λ_k, m_k}) = Σ m_k g(λ_k)`) are STRUCTURALLY ORTHOGONAL substrate-IS observables (distinct algebra-axis corners; cross-corner co-primary FORBIDDEN), NOT two readings of one observable that COLLAPSE — the wildly different values and the OP-PROJ-negative / STATE-PROJ-positive SIGN FLIP are EXPECTED evidence of orthogonality. The workshop derives orthogonal-vs-collapse from FIRST PRINCIPLES: **ORTHOGONAL** confirms the algebra-axis K-counter at its inaugural physical (3He-B) instance; **COLLAPSE** (landau prevails: OP-PROJ is a mis-specified image, one genuine + one spurious observable) registers a structural exception at the K-counter's first physical-realization test.
**Plan reference**: `sessions/session-plan/session-116-plan-w7.md` §W7-2 (`workshop:` block — agents, rounds, sources, `adjudication_question` sub-questions (a) parse-tree corner placement / (b) sign-flip reading / (c) BCS mean-field collapse, the volovik-vs-landau position context, numeric stakes).

**Artifact-Existence Closure Checklist** (workshop gate — closes by artifact-existence-with-content per `wave-classification.md §M1`; **NO verdict line, NO MCP Pre-Compute Audit block**):
*(pending — confirm the deliverable `sessions/session-116/workshops/s116-w7-algebra-axis.md` EXISTS (`ls`) AND paste `grep -E` output for every `must_contain` marker from the plan `output_artifacts.workshop_md` block: `## R1` (steelman both readings), `## R2` (respond to opponent's best case), `## R3` (converge), `## Structural Verdict` (the NEW pinned position resolving orthogonal-vs-collapse). Any marker returning empty ⇒ the workshop did not properly close — orchestrator SendMessage-continues the same panel per `feedback_dispatch-discipline.md`. Content presence by regex, never line/byte counts per `feedback_max-effort-full-fidelity.md`.)*

**Structural Verdict**:
*(pending — include: the NEW pinned position — either **ORTHOGONAL** (STATE-PROJ and OP-PROJ occupy DISTINCT cells of the §VII.U.2 4-corner partition; registered as structural-orthogonal companions, NEVER co-primary; the algebra-axis orthogonality K-counter advances at its inaugural physical 3He-B instance) OR **COLLAPSE** (the BCS gap equation links the spectral count and the occupation asymmetry so tightly they are one observable measured two ways; OP-PROJ is the mis-specified image, so §VII.AJ holds ONE genuine + one spurious observable — a structural EXCEPTION at the K-counter's first physical test, routed as a methodology carry-forward to re-examine the conjecture's physical-realization scope); the three sub-question answers — (a) PARSE-TREE: STATE-PROJ parses to a state-pair functional `ρ(P · A)` (Corner III/IV, algebra-DEPENDENT) and OP-PROJ to a spectrum-only `F({λ_k, m_k})` (Corner I/II, algebra-INVARIANT); (b) SIGN FLIP: is OP-PROJ-negative / STATE-PROJ-positive evidence of orthogonality or of OP-PROJ mis-specification (landau's steelman); (c) BCS MEAN-FIELD: does the gap equation force collapse, or does the gap-self-regularization of the state-pair functional (regulator-INVARIANT) vs the regulator-DEPENDENT spectrum count (algebra-axis sibling discriminator) keep them separate; the R1/R2/R3 positions (volovik ORTHOGONAL pole vs landau COLLAPSE steelman); the numeric stakes (OP-PROJ `R_∞ ≈ −1.892 ± 0.001`; STATE-PROJ `R = +0.03536`; S87 substrate count `R_substrate ≈ −1.2122` at L_max=10; `ratio_mismatch ≈ 1.03`, the S87 FAIL). Substrate framing: D_K eigenvalues → {spectrum-only count (OP-PROJ) | BCS-state occupation asymmetry (STATE-PROJ)} → lab 3He-B observables; the 4-corner algebra-axis partition is the structural arbiter, the BCS gap equation is landau's candidate collapse mechanism, the regulator-response sibling discriminator is volovik's candidate separation mechanism.)*

---

## Wave 7 Synthesis (team-lead)

**Wave 7 closed: 2/2 gates (1 compute INFO + 1 workshop artifact-existence). Q33's §VII.AJ.STATE-PROJ is resolved as a structural-ORTHOGONAL companion to OP-PROJ (level-separated); the algebra-axis K-counter is CONFIRMED at its first PHYSICAL (3He-B) instance at the identity layer, with the physical-realization anchor HELD Track-B.**

**Gate-by-gate.**
- **S116-W7-STATEPROJ-BCS** (compute, **INFO** — Track B). R_STATE=(a−b)/(a+b)=+0.0353559 reproduces the lab gap-asymmetry to rel=0 — but this is a **tautology**: the controlling gap ratio Δ_B/Δ_A = SC_corr_B/SC_corr_A is LABORATORY-IN (Serene-Rainer/Greywall). The decisive substrate-physics reason is structural: the substrate is a **single BDI object** (3He-B child, N_3=0); 3He-A is DIII (N_3=2), so the substrate has **no intrinsic A-sector** and cannot produce a substrate-first Δ_A. 3-tuple sign=PASS/mag=PASS/regime=VALID, but the **plan-frozen composite-precedence** (dual_prior track discriminator) held the generic all-PASS to **INFO** under Track B. What IS substrate-first: the **FORM** — a genuine algebra-DEPENDENT BdG-occupation state-pair functional (R_BdG=+0.0688>0 on 78,080 cached modes). **Sign flip** vs OP-PROJ (R_∞≈−1.892<0).
- **S116-W7-ALGEBRA-AXIS** (workshop, artifact-existence). Structural Verdict: **ORTHOGONAL** (level-separated). The two agents split the axes cleanly — **landau won value-provenance** (Track B: the value is lab-injected), **volovik held identity** (the FORM is a distinct 4-corner cell: STATE-PROJ Corner III algebra-DEPENDENT ⊥ OP-PROJ Corner I algebra-INVARIANT). COLLAPSE rejected at the identity layer: the BCS-gap-equation linkage is a **RELATION not an IDENTITY**; OP-PROJ images a *different* lab observable (Y, DOS-excess), so it is not "spurious"; the regulator-response sibling discriminator (STATE-PROJ regulator-INVARIANT/gap-self-regularized vs OP-PROJ regulator-DEPENDENT) keeps them separate. **Algebra-axis K-counter CONFIRMED** at its first PHYSICAL instance (Level-1/identity, value-free); the physical-realization anchor **HELD Track-B** (Level-3, vanishing-test FAIL on the lab-injected value) → CF-S117. Residual partial-collapse noted (shared mean-field: orthogonal in the sector-label subspace, co-vary in the overall-spectrum subspace).

**Joint reading.** Compute INFO (Track B) + workshop ORTHOGONAL → the §VII.AJ.STATE-PROJ slot is **RESERVED REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION** (landed by mack), NOT registry-PASS. The algebra-axis K-counter advances **structurally** (corpus N=3→N=4, Instance #4) while the **parent rule stays MANDATORY at K=3** — this is empirical-foundation reinforcement (the conjecture's first physical realization), NOT a re-promotion. The two-clause separation holds: per-entry registry-PASS is INCOMPLETE (value held), the rule-level calibration LANDING is the separate valid predicate.

**What holds.** The STATE-PROJ FORM is a genuine algebra-DEPENDENT state-pair functional in a distinct 4-corner cell, structural-orthogonal companion to OP-PROJ (cross-corner co-primary FORBIDDEN). The sign flip (+0.0688 vs −1.892) corroborates orthogonality.

**What strains.** The physical-realization anchor is Track-B (lab-injected value); the no-A-sector obstruction blocks the *direct* substrate-first SC extraction (CF-S117-STATEPROJ-SC-FROM-SUBSTRATE is HIGH-RISK / blocked). The productive forward path is the inter-summand reframe (ℍ vs M₃(ℂ) at common Δ_BCS, which sidesteps the no-A-sector obstruction — CF-S117-STATEPROJ-INTER-SUMMAND).

### Effected In-Session (NON-MATH — executed at wave-synthesis)

The §VII registry / falsifier surface is `mack-cosmic-bridge` SOLE-WRITER domain (`feedback_mack-bridge-role.md`) — so the curated §VII edits were ROUTED to mack via housekeeping §A7 (landau correctly did NOT touch them) and mack DISPATCHED at §6. Capstone-hygiene 5-question gate (landau, §A7): **Q3=YES** (§VII.AJ slot status + K-counter standing change) → §A; capstone prose NO-OP (grep-verified). All mack landings verified on disk:

- [x] **§VII.AJ.STATE-PROJ slot status** (mack) — `OPEN (NEEDS-COMPUTATION)` → `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` at `atlas-07-permanent-results.md:674` + `permanent-results-registry.md:179` (index) + `:16809` (entry-body, RETAIN-and-supersede; Level-1-ORTHOGONAL / Level-3-HELD-Track-B / no-A-sector-BLOCKED annotation; STRUCTURE-tag :16844).
- [x] **algebra-axis K-counter** (mack) — `cross-pillar-bridge-corpus.md §6:312` N=3→N=4 + Instance #4 row (OP-PROJ Corner I ⊥ STATE-PROJ Corner III; first PHYSICAL 3He-B; value-free/Track-B-tagged). Parent rule untouched (stays MANDATORY at K=3 per feedback #14 / subagent edit-deny).
- [x] **atlas-08 Q33** (mack) — dashboard `:23` + detailed `:264` → `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` + CF-S117-STATEPROJ-INTER-SUMMAND pointer.
- [x] **atlas-07:767 OPEN tally** (mack) — `PENDING-VERIFICATION` → `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (stays OPEN bucket).
- [x] **capstone** — NO-OP (mack re-confirmed: no §VII.AJ prose).
- [x] **volovik + landau agent memory** — recorded in-workshop (the level-separated verdict; landau side-fixed a stale clause in its own MEMORY.md, agent-private).
- [x] **housekeeping ledger** `§A7` (landau spec, precise current→corrected for all loci) + `§A7-LANDED (mack)` (line 191, verified line numbers).

**Self-audit (orchestrator)**: WP Effected-In-Session unchecked = 0; sig_5 10/10 distinct session SHAs; the curated §VII surface was landed by the sole writer (mack), NOT orchestrator-direct (correct domain routing); 7 LABORATORY-IN anchors added to canonical_constants.py with provenance (the W7-1 SOURCE-RECON pre-step).

## Carry-Forward Computations

### CF-S117-STATEPROJ-SC-FROM-SUBSTRATE — substrate-first strong-coupling corrections (HIGH-RISK, blocked)
1. **What**: Derive SC_corr_A, SC_corr_B (the 3He A/B strong-coupling gap corrections) from the substrate's OWN q-theory / spectral-action strong-coupling partition, converting the §VII.AJ.STATE-PROJ Track-B anchor → Track A. **Obstruction**: the substrate is a single BDI object (N_3=0) with no intrinsic 3He-A sector → no direct substrate-first Δ_A; HIGH-RISK / structurally blocked unless the A-sector is reconstructed.
2. **Inputs**: `computations/session-116/s116_w7_stateproj_bcs.npz`; the substrate q-theory Volovik-partition machinery; `Δ_BCS` (canonical, R-protected).
3. **Gate**: substrate-first Δ_B/Δ_A computed INDEPENDENT of the lab SC ratio; PASS iff |R_STATE^{substrate} − R_3HeB_lit|/|R_3HeB_lit| ≤ 0.05 AND provenance Track A (then §VII.AJ.STATE-PROJ → registry-PASS).
4. **Effort**: high (blocked by no-A-sector). **Depends on**: the W7-1 FORM result; a substrate A-sector reconstruction.

### CF-S117-STATEPROJ-INTER-SUMMAND — inter-summand asymmetry at common Δ_BCS (productive Track-A path)
1. **What**: Compute the inter-summand state-pair asymmetry R_summand = (a_ℍ − b_{M₃})/(a_ℍ + b_{M₃}) between the ℍ and M₃(ℂ) algebra summands at the COMMON substrate gap Δ_BCS — sidestepping the no-A-sector obstruction (the asymmetry is between two summands the substrate DOES carry, not between A/B phases it does not). Track-A-eligible (no lab SC ratio injected).
2. **Inputs**: `s84_spectrum_cache_L12_tau019.npz`; the A_K = ℂ⊕ℍ⊕M₃(ℂ) sector central projections (from S116-W5-BIMODULE-H); Δ_BCS canonical.
3. **Gate** (composite G1∧G2): G1 = R_summand computed substrate-first (Track A); G2 = R_summand sign + magnitude reported with the inter-summand interpretation (a genuine substrate-IS STATE-PROJ observable, even if it does NOT image the 3He A/B asymmetry — it images the substrate's own ℍ/M₃ pairing asymmetry).
4. **Effort**: medium. **Depends on**: S116-W5-BIMODULE-H sector projections; the W7 ORTHOGONAL verdict (STATE-PROJ is a valid algebra-DEPENDENT corner).

### CF-W7-1 — quantify the residual OP-PROJ ↔ STATE-PROJ partial-collapse [Q-other; OPTIONAL low-leverage verification gate]

1. **What**: Quantify the "residual partial-collapse" — the OP-PROJ ↔ STATE-PROJ co-variation in the overall-spectrum subspace under `{ξ_k}` / L_max / τ-moduli deformation. Both W7 agents agree it is BENIGN (orthogonal in the sector-label subspace; linked through the shared mean field; "neither erases the other"); quantifying it is a VERIFICATION gate (a numerical bound on the linkage), NOT an adjudication. LOW priority / optional — route only if a planner wants a numerical bound.
2. **Inputs**: `s116_w7_stateproj_bcs.npz` (R_STATE, R_BdG, OP-PROJ `R_∞`); the §VII.AJ STATE-PROJ + OP-PROJ observables; the `{ξ_k}` / L_max / τ-moduli deformation family.
3. **Gate**: a numerical bound on the OP-PROJ ↔ STATE-PROJ co-variation in the overall-spectrum subspace; PASS if the linkage is bounded below a pre-registered threshold (benign CONFIRMED); INFO if the bound is loose.
4. **Effort**: ~0.5 agent, LOW. **Depends on**: `s116_w7_stateproj_bcs.npz`; the W7 ORTHOGONAL verdict.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:---------|:-------|
| 2026-06-28 | §VII.AJ.STATE-PROJ (S116-W7-STATEPROJ-BCS) | OPEN (NEEDS-COMPUTATION) since S88 | **REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION** — FORM substrate-first (algebra-DEPENDENT BdG state-pair functional); VALUE Track-B/HELD (lab-injected, no-A-sector) | compute INFO (Track B) + workshop ORTHOGONAL |
| 2026-06-28 | algebra-axis orthogonality K-counter (S116-W7-ALGEBRA-AXIS) | conjecture MANDATORY at K=3 (no physical instance) | **CONFIRMED at first PHYSICAL (3He-B) instance** (corpus N=3→N=4, Instance #4, Level-1/identity value-free); parent rule STAYS MANDATORY at K=3 (empirical reinforcement, not re-promotion) | workshop ORTHOGONAL verdict (relation≠identity; OP-PROJ images Y not spurious; regulator-response discriminator) |
| 2026-06-28 | §VII.AJ.OP-PROJ ⊥ STATE-PROJ | split after S87 W11-5 REGISTRY-FAIL (ambiguous) | **structural-orthogonal companions (cross-corner co-primary FORBIDDEN); distinct 4-corner cells** | the FORM-level identity orthogonality (sign flip + regulator-response + parse-tree corners) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Deliverable md |
|:-----|:-------|:------------|:------------|:---------------|
| S116-W7-STATEPROJ-BCS | `s116_w7_stateproj_bcs.py` | `…_stateproj_bcs.npz` | `…_stateproj_bcs.png` | — |
| S116-W7-ALGEBRA-AXIS | — | — | — | `sessions/session-116/workshops/s116-w7-algebra-axis.md` |

*(Compute under `computations/session-116/`. Verdict: `S116-W7-STATEPROJ-BCS: INFO` (Track B; audit 0968093b…), dual-SHA-unique. The workshop closes by artifact-existence — no verdict line. mack landed the curated §VII edits; 7 LABORATORY-IN anchors added to canonical_constants.py SECTION E.)*
